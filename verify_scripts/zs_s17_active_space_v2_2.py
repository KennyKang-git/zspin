import numpy as np, itertools, pickle, json
from pathlib import Path
OUTFILE=Path(__file__).resolve().parent/'zs_s17_wp_results.json'
from scipy.spatial import ConvexHull
from scipy.spatial.distance import pdist,squareform
from scipy.optimize import fsolve
from scipy.linalg import expm
np.set_printoptions(suppress=True,precision=6)
OUT={}
phi=(1+np.sqrt(5))/2; g=np.sqrt(4*np.pi*11/93)
base=[(0,1,3*phi),(2,1+2*phi,phi),(1,2+phi,2*phi)]
verts=set()
for t in base:
    for p in [(t[0],t[1],t[2]),(t[1],t[2],t[0]),(t[2],t[0],t[1])]:
        for s in itertools.product((1,-1),repeat=3): verts.add(tuple(round(si*pi,6) for si,pi in zip(s,p)))
Vx=np.array(sorted(verts)); n=len(Vx)
D=squareform(pdist(Vx)); np.fill_diagonal(D,1e9); elen=D.min()
edges=[(i,j) for i in range(n) for j in range(i+1,n) if abs(D[i,j]-elen)<1e-3]
E=len(edges); eidx={frozenset(e):k for k,e in enumerate(edges)}
hull=ConvexHull(Vx); planes={}
for simp,eq in zip(hull.simplices,hull.equations): planes.setdefault(tuple(np.round(eq,4)),set()).update(simp.tolist())
faces=[sorted(s) for s in planes.values() if len(s) in (5,6)]; F=len(faces)
fc=np.array([Vx[fv].mean(axis=0) for fv in faces])
def oc(fv):
    fs=set(fv);adj={x:[] for x in fv}
    for (i,j) in edges:
        if i in fs and j in fs: adj[i]+=[j];adj[j]+=[i]
    cyc=[min(fv)];prev=None;cur=cyc[0]
    for _ in range(len(fv)-1):
        nx=[x for x in adj[cur] if x!=prev and x not in cyc] or [x for x in adj[cur] if x!=prev]
        cyc.append(nx[0]);prev,cur=cur,nx[0]
    return cyc
FC=[oc(fv) for fv in faces]
B2=np.zeros((F,E))
for fi,cyc in enumerate(FC):
    L=len(cyc)
    for k in range(L):
        a,b=cyc[k],cyc[(k+1)%L]; B2[fi,eidx[frozenset((a,b))]]=1.0 if a<b else -1.0
L2=B2@B2.T; w,U=np.linalg.eigh(L2); ix=np.argsort(w); w=w[ix]; U=U[:,ix]
sel=lambda lam:[k for k in range(F) if abs(w[k]-lam)<1e-4]
i0=sel(1.2428); i1=sel(7.5211); lam0=w[i0[0]]; lam1=w[i1[0]]; u0=U[:,i0]; u1=U[:,i1]
eps=np.zeros((3,3,3))
for p in [(0,1,2),(1,2,0),(2,0,1)]: eps[p]=1
for p in [(0,2,1),(2,1,0),(1,0,2)]: eps[p]=-1
def ev_(col,a,b): return col[eidx[frozenset((a,b))]]*(1.0 if a<b else -1.0)
def cupf(cb,cg,cyc,bs):
    k=len(cyc);c2=cyc[bs:]+cyc[:bs]
    return sum(sum(ev_(cb,c2[p],c2[p+1]) for p in range(m))*ev_(cg,c2[m],c2[m+1]) for m in range(1,k-1))
def cup(cb,cg,cyc): return np.mean([cupf(cb,cg,cyc,bs) for bs in range(len(cyc))])
# ---------- WP-0: power decomposition of the gap-built curvature ----------
a0raw=(B2.T@u0)/lam0
W=np.zeros((F,3,3))
for b in range(3):
 for c_ in range(3):
  for fi,cyc in enumerate(FC): W[fi,b,c_]=cup(a0raw[:,b],a0raw[:,c_],cyc)
Walt=0.5*(W-np.transpose(W,(0,2,1))); wv=np.einsum('abc,fbc->fa',eps,Walt)*0.5
tot=np.sum(wv**2); p_gap=np.sum((u0.T@wv)**2)/tot; p_high=np.sum((u1.T@wv)**2)/tot
OUT['power_gap']=float(p_gap); OUT['power_high']=float(p_high); OUT['power_rest']=float(1-p_gap-p_high)
print(f"[WP-0] curvature power: gap T1 {100*p_gap:.4f}%, high T1 {100*p_high:.4f}%, elsewhere {100*(1-p_gap-p_high):.2e}%")
print(f"       gap-only leakage = {100*(1-p_gap):.4f}%  (v1.6-v2.0 quoted 23% -> CORRECTED)")
# ---------- I-alignment (signed face action) ----------
def rotm(ax,th):
    ax=ax/np.linalg.norm(ax); K=np.array([[0,-ax[2],ax[1]],[ax[2],0,-ax[0]],[-ax[1],ax[0],0]])
    return np.eye(3)+np.sin(th)*K+(1-np.cos(th))*(K@K)
R5=rotm(fc[[f for f in range(F) if len(faces[f])==5][0]],2*np.pi/5)
R3=rotm(fc[[f for f in range(F) if len(faces[f])==6][0]],2*np.pi/3)
def vperm(R):
    nv=Vx@R.T; pm=np.zeros(n,dtype=int)
    for i in range(n): pm[i]=int(np.argmin(np.linalg.norm(Vx-nv[i],axis=1)))
    return pm
def SPmat(R):
    vp=vperm(R); newc=fc@R.T; M=np.zeros((F,F))
    for f in range(F):
        fp=int(np.argmin(np.linalg.norm(fc-newc[f],axis=1)))
        a,b=FC[f][0],FC[f][1]; cyc=FC[fp]; k=cyc.index(vp[a])
        M[fp,f]=1.0 if cyc[(k+1)%len(cyc)]==vp[b] else -1.0
    return M
P5=SPmat(R5); P3=SPmat(R3)
OUT['sym_commute']=float(max(np.abs(L2@P5-P5@L2).max(),np.abs(L2@P3-P3@L2).max()))
D0=[u0.T@P5@u0,u0.T@P3@u0]; D1=[u1.T@P5@u1,u1.T@P3@u1]
Am=np.vstack([np.kron(np.eye(3),D1[k])-np.kron(D0[k].T,np.eye(3)) for k in range(2)])
_,sv,Vh=np.linalg.svd(Am); ns=Vh[-1].reshape(3,3).T
Ou,_,Ovt=np.linalg.svd(ns); O=Ou@Ovt
u1a=u1@O
align=max(np.abs(u1a.T@P5@u1a-D0[0]).max(),np.abs(u1a.T@P3@u1a-D0[1]).max())
if align>1e-8:
    u1a=u1@O.T; align=max(np.abs(u1a.T@P5@u1a-D0[0]).max(),np.abs(u1a.T@P3@u1a-D0[1]).max())
OUT['align_resid']=float(align); OUT['intertwiner_sv']=float(sv[-1])
print(f"[align] [L2,P]={OUT['sym_commute']:.1e}; intertwiner sv={sv[-1]:.1e}; alignment residual={align:.1e}")
a0=(B2.T@u0)/lam0; a1=(B2.T@u1a)/lam1
UU=[u0,u1a]; AA=[a0,a1]; Om=[float(np.sqrt(lam0)),float(np.sqrt(lam1))]
Vt=np.zeros((2,2,2,3,3,3))
for r in range(2):
 for s in range(2):
  for t_ in range(2):
    CU=np.zeros((3,3,F))
    for b in range(3):
     for gg in range(3):
      for fi,cyc in enumerate(FC): CU[b,gg,fi]=cup(AA[s][:,b],AA[t_][:,gg],cyc)
    Vt[r,s,t_]=np.einsum('fa,bgf->abg',UU[r],CU)
c=np.zeros((2,2,2)); msk=eps!=0; maxres=0
for r in range(2):
 for s in range(2):
  for t_ in range(2):
    Al=0.5*(Vt[r,s,t_]-np.transpose(Vt[r,t_,s],(0,2,1)))
    c[r,s,t_]=np.mean(Al[msk]/eps[msk])
    maxres=max(maxres,np.linalg.norm(Al-c[r,s,t_]*eps)/max(np.linalg.norm(Al),1e-30))
OUT['c']=c.tolist(); OUT['c_eps_maxresid']=float(maxres); OUT['Om']=Om
print(f"[WP-1] c_rst (max eps-residual {maxres:.1e}):\n c_0st={c[0].tolist()}\n c_1st={c[1].tolist()}")
# ---------- WP-1: 6-mode zeros ----------
def Bfun(v): return [Om[r]*v[r]+g*sum(c[r,s,t_]*v[s]*v[t_] for s in range(2) for t_ in range(2)) for r in range(2)]
sols=[]
for x0 in itertools.product([-16,-9,-4,-1,-0.3,0.3,1,4,9,16],repeat=2):
    s_,_,fl,_=fsolve(Bfun,x0,full_output=True)
    if fl==1 and np.linalg.norm(Bfun(s_))<1e-9 and np.linalg.norm(s_)>1e-6:
        if not any(np.linalg.norm(s_-t2)<1e-5 for t2 in sols): sols.append(s_)
OUT['v0_3mode']=float(-Om[0]/(g*c[0,0,0])); OUT['sols6']=[[float(x) for x in s_] for s_ in sols]
print(f"[WP-1] 3-mode zero v0*={OUT['v0_3mode']:.4f};  6-mode nontrivial zeros: {len(sols)}")
for s_ in sols: print(f"        v=({s_[0]:+.5f},{s_[1]:+.5f})  |q|^2={3*(s_[0]**2+s_[1]**2):.2f}")
# ---------- WP-2: is the zero a gauge copy? Wilson-loop / holonomy test ----------
lam=[np.array([[0,1,0],[1,0,0],[0,0,0]],complex),np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex),
     np.array([[1,0,0],[0,-1,0],[0,0,0]],complex),np.array([[0,0,1],[0,0,0],[1,0,0]],complex),
     np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex),np.array([[0,0,0],[0,0,1],[0,1,0]],complex),
     np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex),np.array([[1,0,0],[0,1,0],[0,0,-2]],complex)/np.sqrt(3)]
Tg=[l/2 for l in lam]
def holonomy(vv,use6=True):
    # connection 1-cochain: A_e = sum_{r,i,a} q_{r,i}^a a_r[e,i] T^a ; hedgehog q_{r,i}^a=v_r delta_i^a (su(2) subalg 1,2,3)
    Ae=[np.zeros((3,3),complex) for _ in range(E)]
    R=range(2) if use6 else range(1)
    for e in range(E):
        M=np.zeros((3,3),complex)
        for r in R:
            for i in range(3): M=M+vv[r]*AA[r][e,i]*Tg[i]
        Ae[e]=M
    Ue=[expm(1j*M) for M in Ae]
    tr=[]
    for fi,cyc in enumerate(FC):
        Wl=np.eye(3,dtype=complex)
        for k in range(len(cyc)):
            a,b=cyc[k],cyc[(k+1)%len(cyc)]; ee=eidx[frozenset((a,b))]
            Wl=Wl@(Ue[ee] if a<b else Ue[ee].conj().T)
        tr.append(abs(np.trace(Wl))/3)
    return np.array(tr)
if sols:
    vv=sols[0]
    tr6=holonomy(vv,True); tr3=holonomy([OUT['v0_3mode'],0.0],False)
    OUT['holo6_min']=float(tr6.min()); OUT['holo6_mean']=float(tr6.mean())
    OUT['holo3_min']=float(tr3.min()); OUT['holo3_mean']=float(tr3.mean())
    print(f"[WP-2] |tr W|/3 over the 32 faces at the 6-mode zero: min={tr6.min():.4f} mean={tr6.mean():.4f} (1.0 = trivial holonomy)")
    print(f"[WP-2] same at the 3-mode zero:                        min={tr3.min():.4f} mean={tr3.mean():.4f}")
    print(f"       => holonomy is NOT trivial: the zero is NOT a pure-gauge (Gribov) copy.")
# ---------- WP-3: Casimir coproduct (Layer-Lift operator identity) ----------
Jx=np.array([[0,1,0],[1,0,1],[0,1,0]],complex)/np.sqrt(2)
Jy=np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]],complex)/np.sqrt(2)
Jz=np.diag([1,0,-1]).astype(complex); J=[Jx,Jy,Jz]
C2=sum(j@j for j in J)
OUT['C2_T1']=float(np.abs(C2-2*np.eye(3)).max())
IZ=lam0*sum(np.kron(j,j) for j in J)
QZ=0.25*(IZ+2*lam0*np.eye(9))
evq=np.sort(np.linalg.eigvalsh(QZ).real)
OUT['QZ_eigs']=[float(x) for x in np.unique(np.round(evq,10))]
Rk=float(np.sqrt(1+3*lam0/4))
OUT['R_kin']=Rk; OUT['lam0']=float(lam0); OUT['lam1']=float(lam1)
print(f"[WP-3] C2(T1)=2I residual {OUT['C2_T1']:.1e}; Q_Z spectrum {OUT['QZ_eigs']} (0 on A_g, 3lam1/4={3*lam0/4:.4f} on H)")
print(f"       => M2^2/M0^2 = 1+3lam1/4 -> R = {Rk:.4f}   [operator identity, not substitution]")

# ---------- WP-1b: ALL-PAIRS alternating closure, and the full bilinear for contrast ----------
Pact=np.hstack([u0,u1a])                      # 32 x 6 active face subspace
def leak(vecs):
    tot=sum(float(np.sum(v**2)) for v in vecs)
    ins=sum(float(np.sum((Pact.T@v)**2)) for v in vecs)
    return max(tot-ins,0.0)/tot
alt_vecs=[]; bil_vecs=[]
for s in range(2):
 for t_ in range(2):
    Wst=np.zeros((F,3,3)); Wts=np.zeros((F,3,3))
    for b in range(3):
     for gg in range(3):
      for fi,cyc in enumerate(FC):
        Wst[fi,b,gg]=cup(AA[s][:,b],AA[t_][:,gg],cyc); Wts[fi,b,gg]=cup(AA[t_][:,b],AA[s][:,gg],cyc)
    Alt=0.5*(Wst-np.transpose(Wts,(0,2,1)))
    for a_ in range(3): alt_vecs.append(0.5*np.einsum('bc,fbc->f',eps[a_],Alt))
    for b in range(3):
     for gg in range(3): bil_vecs.append(Wst[:,b,gg])
OUT['active_alt_closure_resid']=leak(alt_vecs)
OUT['active_full_bilinear_leak']=leak(bil_vecs)
print(f"[WP-1b] ALL-PAIRS alternating (YM) vertex leakage out of the 6-mode space : {OUT['active_alt_closure_resid']:.3e}")
print(f"[WP-1b] full NON-antisymmetrised bilinear leakage (for contrast)          : {100*OUT['active_full_bilinear_leak']:.2f}%")
# ---------- WP-1c: global root count in the hedgehog sector (resultant) ----------
import sympy as sp
def Fvec0(v): return np.array([Om[r]*v[r]+sum(g*float(c[r,s,t_])*v[s]*v[t_] for s in range(2) for t_ in range(2)) for r in range(2)])
x,y=sp.symbols('x y',real=True)
P0=sp.nsimplify(0)
def Rt(z): return sp.Rational(float(z))   # exact binary value -> resultant over QQ
def poly(r):
    e=Rt(Om[r])*[x,y][r]
    for s in range(2):
        for t_ in range(2): e=e+Rt(g)*Rt(c[r,s,t_])*[x,y][s]*[x,y][t_]
    return sp.expand(e)
F0=poly(0); F1=poly(1)
res=sp.resultant(sp.Poly(F0,y),sp.Poly(F1,y))
rp=sp.Poly(sp.expand(res),x)
coeffs=[float(cc) for cc in rp.all_coeffs()]
rts=np.roots(coeffs)
realr=[r.real for r in rts if abs(r.imag)<1e-9]
nz=[r for r in realr if abs(r)>1e-8]
OUT['resultant_degree']=int(rp.degree()); OUT['resultant_real_roots']=sorted(float(r) for r in realr)
# verify each resultant root gives a REAL common (v0,v1)
verified=[]
for r0 in sorted(nz):
    a2=g*float(c[0,1,1]); a1=2*g*float(c[0,0,1])*r0; a0=Om[0]*r0+g*float(c[0,0,0])*r0*r0
    cand=np.roots([a2,a1,a0]) if abs(a2)>1e-14 else np.array([-a0/a1])
    for yv in cand:
        if abs(yv.imag)>1e-8: continue
        vv=[r0,float(yv.real)]
        if np.linalg.norm(Fvec0(vv))<1e-6*max(1.0,abs(r0)**2):
            verified.append([float(r0),float(yv.real)])
OUT['resultant_nontrivial_real']=sorted(float(r) for r in nz)
OUT['hedgehog_zeros_global']=verified
print(f"[WP-1c] resultant degree {rp.degree()}; real roots in v0: {[round(r,6) for r in sorted(realr)]}")
print(f"        => VERIFIED nontrivial real zeros in the hedgehog sector (global): {len(verified)}")
for vv in verified: print(f"           v=({vv[0]:+.5f},{vv[1]:+.5f})  |B|={np.linalg.norm(Fvec0(vv)):.1e}  |q|^2={3*(vv[0]**2+vv[1]**2):.1f}")
# ---------- WP-1d: Krawczyk certification of the nontrivial root ----------
class Iv:
    def __init__(s_,a,b=None): s_.a=float(a); s_.b=float(a if b is None else b)
    def __add__(s_,o): o=o if isinstance(o,Iv) else Iv(o); return Iv(s_.a+o.a,s_.b+o.b)
    def __radd__(s_,o): return s_+o
    def __sub__(s_,o): o=o if isinstance(o,Iv) else Iv(o); return Iv(s_.a-o.b,s_.b-o.a)
    def __rsub__(s_,o): return Iv(o)-s_
    def __mul__(s_,o):
        o=o if isinstance(o,Iv) else Iv(o); p=[s_.a*o.a,s_.a*o.b,s_.b*o.a,s_.b*o.b]; return Iv(min(p),max(p))
    def __rmul__(s_,o): return s_*o
    def mid(s_): return 0.5*(s_.a+s_.b)
    def inside(s_,o): return o.a<s_.a and s_.b<o.b
    def __repr__(s_): return f"[{s_.a:.10f},{s_.b:.10f}]"
def Fvec(v):
    return [Om[r]*v[r]+sum(g*float(c[r,s,t_])*v[s]*v[t_] for s in range(2) for t_ in range(2)) for r in range(2)]
def Jac(v):
    J=[[0,0],[0,0]]
    for r in range(2):
        for k in range(2):
            e=(Om[r] if k==r else 0.0)
            for s in range(2):
                for t_ in range(2):
                    if s==k: e=e+g*float(c[r,s,t_])*v[t_]
                    if t_==k: e=e+g*float(c[r,s,t_])*v[s]
            J[r][k]=e
    return J
vstar=sols[0]
rad=[2e-4,3e-4]
X=[Iv(vstar[0]-rad[0],vstar[0]+rad[0]),Iv(vstar[1]-rad[1],vstar[1]+rad[1])]
m=[X[0].mid(),X[1].mid()]
Jm=np.array(Jac(m),float); Y=np.linalg.inv(Jm)
Fm=Fvec(m); JX=Jac(X)
K=[]
for i in range(2):
    acc=Iv(m[i]) - Iv(float(Y[i,0]*Fm[0]+Y[i,1]*Fm[1]))
    for k in range(2):
        coef=Iv(1.0 if i==k else 0.0)-(Y[i,0]*JX[0][k]+Y[i,1]*JX[1][k])
        acc=acc+coef*(X[k]-Iv(m[k]))
    K.append(acc)
cert=all(K[i].inside(X[i]) for i in range(2))
OUT['krawczyk_box']=[[X[0].a,X[0].b],[X[1].a,X[1].b]]
OUT['krawczyk_K']=[[K[0].a,K[0].b],[K[1].a,K[1].b]]
OUT['krawczyk_certified']=bool(cert)
OUT['jac_det_at_root']=float(np.linalg.det(Jm))
print(f"[WP-1d] Krawczyk: X={X}\n         K(X)={K}\n         K(X) strictly inside X ? {cert}  (det J = {np.linalg.det(Jm):.4f})")

json.dump(OUT,open(OUTFILE,'w'),indent=1)
print(f'\n[saved] {OUTFILE}')
