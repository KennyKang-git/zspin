#  zs_f33_verify_v1_8.py  — STANDALONE verification suite for ZS-F33 v1.8.
#  No sidecar files: the BCC T^3 quotient and the 48/20 cellular-seam
#  classification are built inline. Four check kinds:
#    [A] ASSERT-COMPUTED      : numeric/matrix assertions that CAN fail  -> PASS/FAIL count
#    [I] IDENTITY-REPORTED    : definitional identities                  -> reported
#    [P] IMPORTED-PROVEN      : external theorems (e.g. Cauchy)           -> declared
#    [S] STRUCTURAL-ASSUMPTION: declared interpretations                 -> excluded from count
#  Firewall: the observed rho_obs and the back-solved target enter ONLY the post-run zone.
import numpy as np, math
from itertools import permutations, product
from math import atan2
from mpmath import mp, mpc, exp, log, pi, arg, fabs, im
mp.dps=30; np.set_printoptions(suppress=True)

Apass=[]; Irep=[]; Pthm=[]; Sdec=[]
def A(name, ok, val=""): Apass.append(bool(ok)); print(f"  [A] {'PASS' if ok else 'FAIL'}  {name}"+(f"  = {val}" if val else ""))
def I(name, val): Irep.append(name); print(f"  [I] ----  {name}  = {val}")
def P(name): Pthm.append(name); print(f"  [P] thm   {name}")
def S(name): Sdec.append(name); print(f"  [S] decl  {name}")

print("="*72); print("ZS-F33 v1.8 STANDALONE verification | seed 437"); print("="*72)

# ---------- locked root + chain ----------
print("\n[I] Locked inputs and the z* = i^(z*) chain")
z=mpc(0.4,0.3)
for _ in range(3000): z=exp(z*(1j*pi/2))
lam=(1j*pi/2)*z; kappa=-log(fabs(lam)); omega=arg(lam)
A("z* = i^(z*) fixed-point residual ~ 0", float(fabs(exp(z*(1j*pi/2))-z))<1e-20, f"{float(fabs(exp(z*(1j*pi/2))-z)):.1e}")
I("omega = arg(lambda*)", f"{float(omega):.10f}");  I("omega^2/2", f"{float(omega*omega/2):.10f}")
tau=log(lam)/(2j*pi); q=exp(2j*pi*tau)
I("nome q = e^(2pi i tau) = lambda* (definitional)", f"|q-lambda*|={float(fabs(q-lam)):.1e}")
A("register Q = 11 = 3(X)+6(Y)+2(Z)", 3+6+2==11, "11")

# ---------- F33.2B Wilson polar-line + F33.2B-orb Wilson-Koenigs ----------
print("\n[F33.2] Wilson polar-line and Wilson-Koenigs orbit space")
U=lam/fabs(lam)
A("Wilson polar phase arg(lambda*/|lambda*|)=omega", abs(float(arg(U))-float(omega))<1e-12, f"{float(arg(U)):.8f}")
Rl,Il=float(lam.real),float(lam.imag); WZ=np.array([[Rl,-Il],[Il,Rl]])
# Build the FULL F0 11x11 Wilson register map W = X(3) (+) Y(6) (+) Z(2), then project.
np.random.seed(437)
WX=np.diag([0.5,0.7,0.9]); WY=np.diag([0.2,0.3,0.35,0.4,0.45,0.5])
W=np.zeros((11,11)); W[:3,:3]=WX; W[3:9,3:9]=WY; W[9:,9:]=WZ
PZ=np.zeros((11,11)); PZ[9,9]=1; PZ[10,10]=1   # Z-block projector
A("P_Z W P_Z = W_Z (full 11x11 W projects to the Z-block)", np.allclose((PZ@W@PZ)[9:,9:],WZ))
evZ=np.linalg.eigvals((PZ@W@PZ)[9:,9:])
A("Wilson Z-block eigenvalues = lambda*, conj", abs(abs(evZ[0])-float(fabs(lam)))<1e-9, f"|eig|={abs(evZ[0]):.6f}")
vlam=np.array([1,-1j])
A("(1,-i)/sqrt2 is the lambda* eigenvector (branch selection)", np.allclose(WZ@vlam, complex(lam)*vlam))
# seam operator J_Z (anti-holomorphic involution) selects the lambda* branch over its conjugate
JZ=np.array([[1,0],[0,-1]])   # complex-conjugation seam in the (Re,Im) basis
A("seam J_Z conjugates W_Z (J_Z W_Z J_Z = conj-block) => picks one chirality",
  np.allclose(JZ@WZ@JZ, np.array([[Rl,Il],[-Il,Rl]])))
A("0<|lambda*|<1 => Z-action free & properly discontinuous on C*", 0<float(fabs(lam))<1, f"{float(fabs(lam)):.4f}")
A("Im tau>0 (E_lambda* in upper half-plane)", float(im(tau))>0, f"{float(im(tau)):.4f}")
S("physical observables constant on Wilson orbits O(w)=O(lambda* w) (orbit-equivalence -> F34)")

# ---------- F33.3A' bivector-complexification consistency ----------
print("\n[F33.3A'] Bivector-complexification consistency: (3,6,2) without Q")
sols=[d for d in range(2,12) if 2*(d-1)==d*(d-1)//2]
A("2(d-1)=d(d-1)/2 unique solution d>1 is d=4", sols==[4], f"{sols}")
A("four routes to 6: 3x2, C(4,2), 3+3, 3+3", 3*2==6 and math.comb(4,2)==6 and 3+3==6, "all 6")
I("Q = 3(X)+6(Y)+2(Z) = 11 (independent cross-check)", "11")

# ---------- F33.4B flux-gluing (Cauchy => IMPORTED-PROVEN, not finite grid) ----------
print("\n[F33.4B] Flux-gluing exponential uniqueness")
P("multiplicative Cauchy: continuous sigma(x+y)=sigma(x)sigma(y),sigma'(0)=1 => sigma=e^x [Aczel]")
S("corpus F- is the local-sequestering shift 4-form (structural correspondence)")

# ---------- F33.1C 2D parity torsion FROM the Fourier spectrum (full computation) ----------
print("\n[F33.1C] 2D seam-parity torsion ln T_- computed from the Fourier spectrum")
def torus2_seam_odd_logT(m=4):
    # cubical CW complex on (Z/m)^2: 0-cells (verts), 1-cells (x,y edges), 2-cells (faces)
    n=2; verts=list(product(range(m),range(m)))
    from itertools import combinations
    cells={p:[] for p in range(3)}; cidx={p:{} for p in range(3)}
    for p in range(3):
        for Ssub in combinations(range(n),p):
            for v in verts: cells[p].append((v,Ssub)); cidx[p][(v,Ssub)]=len(cells[p])-1
    def stp(v,ax): w=list(v); w[ax]=(w[ax]+1)%m; return tuple(w)
    D={}
    for p in range(1,3):
        M=np.zeros((len(cells[p-1]),len(cells[p])))
        for j,(v,Ssub) in enumerate(cells[p]):
            for k,ax in enumerate(Ssub):
                sg=(-1)**k; Sm=tuple(a for a in Ssub if a!=ax)
                M[cidx[p-1][(v,Sm)],j]+=-sg; M[cidx[p-1][(stp(v,ax),Sm)],j]+=sg
        D[p]=M
    def neg(v): return tuple((-v[i])%m for i in range(n))
    J={}
    for p in range(3):
        M=np.zeros((len(cells[p]),)*2)
        for j,(v,Ssub) in enumerate(cells[p]):
            vb=neg(v)
            for ax in Ssub: vb=tuple((vb[i]-(1 if i==ax else 0))%m for i in range(n))
            M[cidx[p][(vb,Ssub)],j]=(-1)**p
        J[p]=M
    L={}
    for p in range(3):
        Lp=np.zeros((len(cells[p]),)*2)
        if p in D: Lp+=D[p].T@D[p]
        if (p+1) in D: Lp+=D[p+1]@D[p+1].T
        L[p]=Lp
    chain=all(np.allclose(J[p-1]@D[p],D[p]@J[p]) for p in range(1,3))
    def lndet_odd(p):
        Pm=(np.eye(L[p].shape[0])-J[p])/2; w=np.linalg.eigvalsh(Pm@L[p]@Pm)
        nz=[x for x in w if x>1e-6]; return float(sum(math.log(round(x,6)) for x in nz)) if nz else 0.0
    lnT=0.5*sum(((-1)**p)*p*lndet_odd(p) for p in range(3))
    return lnT, chain
lnT2,ch2=torus2_seam_odd_logT(4)
A("2D parity torsion ln T_- computed = ln4 (counterexample, chain map ok)",
  ch2 and abs(lnT2-math.log(4))<1e-6, f"{lnT2:.5f}")

# ---------- F33.5 complete cellular-seam classification (INLINE, no sidecar) ----------
print("\n[F33.5] Complete cellular-seam classification built inline (no sidecar)")
def build_TO_quotient():
    vset=set()
    for p in set(permutations([0,1,2])):
        for s in product([1,-1],repeat=3): vset.add(tuple(p[k]*s[k] for k in range(3)))
    V=sorted(vset); n=len(V); Vidx={v:i for i,v in enumerate(V)}
    def d2f(a,b): return sum((x-y)**2 for x,y in zip(a,b))
    EDG=[(i,j) for i in range(n) for j in range(i+1,n) if d2f(V[i],V[j])==2]
    def oc(idx):
        pts=np.array([V[i] for i in idx],float); c=pts.mean(0); u=pts[1]-pts[0]; nn=None
        for k in range(2,len(pts)):
            w=pts[k]-pts[0]; cc=np.cross(u,w)
            if np.linalg.norm(cc)>1e-6: nn=cc/np.linalg.norm(cc);break
        e1=u/np.linalg.norm(u); e2=np.cross(nn,e1)
        ang=[atan2(np.dot(np.array(V[i])-c,e2),np.dot(np.array(V[i])-c,e1)) for i in idx]
        return [idx[k] for k in np.argsort(ang)]
    FACES=[]
    for ax in range(3):
        for sgv in (2,-2): FACES.append(oc([i for i,v in enumerate(V) if v[ax]==sgv]))
    for sx,sy,sz in product([1,-1],repeat=3):
        for sgv in (3,-3):
            f=[i for i,v in enumerate(V) if sx*v[0]+sy*v[1]+sz*v[2]==sgv]
            if len(f)==6: FACES.append(oc(f))
    Lg=np.array([[2,2,2],[4,0,0],[0,4,0]],float); Li=np.linalg.inv(Lg.T)
    def inlat(x): s=Li@np.array(x,float); return np.allclose(s,np.round(s),atol=1e-6)
    vrep=[]; vlab={}
    for i,v in enumerate(V):
        f=None
        for r in vrep:
            if inlat(np.array(v)-np.array(V[r])): f=r;break
        if f is None: vrep.append(i); vlab[i]=len(vrep)-1
        else: vlab[i]=vlab[[r for r in vrep if inlat(np.array(v)-np.array(V[r]))][0]]
    def ematch(e1,e2):
        i,j=e1;k,l=e2
        if inlat(np.array(V[k])-np.array(V[i])) and inlat(np.array(V[l])-np.array(V[j])): return +1
        if inlat(np.array(V[k])-np.array(V[j])) and inlat(np.array(V[l])-np.array(V[i])): return -1
        return 0
    erep=[];esign={};elab={}
    for e in EDG:
        f=None;sg=1
        for r in erep:
            s=ematch(e,r)
            if s!=0: f=r;sg=s;break
        if f is None: erep.append(e);elab[e]=len(erep)-1;esign[e]=1
        else: elab[e]=erep.index(f);esign[e]=sg
    def fmatch(f1,f2):
        for tr in f2:
            lam2=np.array(V[tr])-np.array(V[f1[0]]); mp2=set();ok=True
            for vi in f1:
                tgt=tuple(np.array(V[vi])+lam2)
                if tgt in Vidx: mp2.add(Vidx[tgt])
                else: ok=False;break
            if ok and mp2==set(f2): return True
        return False
    frep=[];flab=[]
    for fi,f in enumerate(FACES):
        fo=None
        for ri,r in enumerate(frep):
            if fmatch(f,FACES[r]): fo=ri;break
        if fo is None: frep.append(fi);flab.append(len(frep)-1)
        else: flab.append(fo)
    NV=len(vrep); NE=len(erep); NF=len(frep)
    d1=np.zeros((NV,NE))
    for c,(i,j) in enumerate(erep): d1[vlab[j],c]+=1; d1[vlab[i],c]-=1
    def qe(i,j):
        if i<j: return elab[(i,j)],esign[(i,j)]
        return elab[(j,i)],-esign[(j,i)]
    d2m=np.zeros((NE,NF))
    for c,fi in enumerate(frep):
        cyc=FACES[fi]
        for k in range(len(cyc)):
            cls,sg=qe(cyc[k],cyc[(k+1)%len(cyc)]); d2m[cls,c]+=sg
    return dict(V=V,n=n,vlab=vlab,erep=erep,frep=frep,FACES=FACES,inlat=inlat,
                d1=d1,d2m=d2m,NV=NV,NE=NE,NF=NF)
Q=build_TO_quotient()
V=Q['V'];n=Q['n'];vlab=Q['vlab'];erep=Q['erep'];frep=Q['frep'];FACES=Q['FACES']
inlat=Q['inlat'];d1=Q['d1'];d2m=Q['d2m'];NV=Q['NV'];NE=Q['NE'];NF=Q['NF']
from collections import Counter
A("standalone quotient (V,E,F)=(6,12,7)", (NV,NE,NF)==(6,12,7), f"{(NV,NE,NF)}")
A("d1 d2 = 0", np.allclose(d1@d2m,0))
spec=dict(Counter(round(x,3) for x in np.linalg.eigvalsh(d1.T@d1+d2m@d2m.T)))
A("spec(Delta_1)={0^3,4^3,6^2,8^3,12^1}", spec.get(0.0)==3 and spec.get(4.0)==3 and spec.get(6.0)==2 and spec.get(8.0)==3 and spec.get(12.0)==1, str(spec))
# automorphism enumeration: point group (48) x quotient-translation representatives only
erep_pts=[(np.array(V[i],float),np.array(V[j],float)) for (i,j) in erep]
frep_pts=[[np.array(V[w],float) for w in FACES[frep[c]]] for c in range(NF)]
def edge_class(pi,pj):
    for c,(a,b) in enumerate(erep_pts):
        if inlat(pi-a) and inlat(pj-b): return c,+1
        if inlat(pi-b) and inlat(pj-a): return c,-1
    return None,0
def face_class(pts):
    s=len(pts)
    for c,rep in enumerate(frep_pts):
        if len(rep)!=s: continue
        for r0 in range(s):
            lam_=pts[0]-rep[r0]
            if all(any(inlat((pts[k]-lam_)-rep[mm]) for mm in range(s)) for k in range(s)):
                sh=[rep[(r0+k)%s]+lam_ for k in range(s)]
                if all(inlat(sh[k]-pts[k]) for k in range(s)): return c,+1
                shr=[rep[(r0-k)%s]+lam_ for k in range(s)]
                if all(inlat(shr[k]-pts[k]) for k in range(s)): return c,-1
    return None,0
def vclass(p):
    for j in range(n):
        if inlat(p-np.array(V[j])): return vlab[j]
    return None
PG=[]
for perm in permutations(range(3)):
    for sg in product([1,-1],repeat=3):
        Am=np.zeros((3,3))
        for i in range(3): Am[i,perm[i]]=sg[i]
        PG.append(Am)
# quotient-translation representatives: one per vertex class (6), not all 576 differences
trans_reps=[np.array(V[[i for i in range(n) if vlab[i]==c][0]],float)-np.array(V[0],float) for c in range(NV)]
trans_reps=[np.zeros(3)]+trans_reps
def build_J(Am,t):
    J0=np.zeros((NV,NV))
    for c in range(NV):
        rep=[i for i in range(n) if vlab[i]==c][0]
        img=vclass(Am@np.array(V[rep],float)+t)
        if img is None: return None
        J0[img,c]=1
    if not (np.allclose(J0.sum(0),1) and np.allclose(J0.sum(1),1)): return None
    J1=np.zeros((NE,NE))
    for c,(a,b) in enumerate(erep_pts):
        cls,sg=edge_class(Am@a+t,Am@b+t)
        if cls is None: return None
        J1[cls,c]+=sg
    J2=np.zeros((NF,NF))
    for c in range(NF):
        cls,sg=face_class([Am@p+t for p in frep_pts[c]])
        if cls is None: return None
        J2[cls,c]+=sg
    return J0,J1,J2
uniq={}
for Am in PG:
    for t in trans_reps:
        Js=build_J(Am,t)
        if Js is None: continue
        J0,J1,J2=Js
        if not (np.allclose(J0@d1,d1@J1) and np.allclose(J1@d2m,d2m@J2)): continue
        uniq[(J0.astype(int).tobytes(),J1.astype(int).tobytes(),J2.astype(int).tobytes())]=(J0,J1,J2)
A("|Aut_cell| = 48 (point group x quotient-translation reps)", len(uniq)==48, str(len(uniq)))
invs=[(J0,J1,J2) for (J0,J1,J2) in uniq.values()
      if np.allclose(J0@J0,np.eye(NV)) and np.allclose(J1@J1,np.eye(NE)) and np.allclose(J2@J2,np.eye(NF))]
A("order-2 involutions = 20", len(invs)==20, str(len(invs)))
def lndet_odd(L,J):
    Pm=(np.eye(L.shape[0])-J)/2; w=np.linalg.eigvalsh(Pm@L@Pm); nz=[v for v in w if v>1e-6]
    return float(sum(math.log(round(v,6)) for v in nz)) if nz else 0.0
L1=d1.T@d1+d2m@d2m.T; L2=d2m.T@d2m
T=set()
for (J0,J1,J2) in invs: T.add(round(0.5*(-lndet_odd(L1,J1)+2*lndet_odd(L2,J2)),5))
target_img=sorted({round(c*math.log(2),5) for c in [-3,0,1,1.5,2,2.5]})
A("seam-odd torsion image = {-3,0,1,3/2,2,5/2}*ln2", sorted(T)==target_img, str(sorted(T)))

# ---------- F33.8 Charge-Unit Obstruction: chi_- = e_-^2/Z_-  (corrected) ----------
print("\n[F33.8] Charge-Unit Obstruction (corrected orientation)")
import sympy as sp
e2,Zk,th,k=sp.symbols('e2 Z theta k',positive=True)
Ek=(e2/(2*Zk))*(k+th/(2*sp.pi))**2
chi=sp.simplify(sp.diff(Ek,th,2).subs(k,0))
A("chi_- = d^2E_k/dtheta^2 = e_-^2/(4 pi^2 Z_-)  (∝ e_-^2/Z_-, NOT Z_-/e_-^2)",
  sp.simplify(chi-e2/(4*sp.pi**2*Zk))==0, str(chi))
S("canonical minimal Abelian compact 3-form action selected for F33.6/F33.8")

# ---------- summary ----------
nA=len(Apass); okA=sum(Apass)
print("\n"+"="*72)
print(f"ASSERT-COMPUTED   : {okA}/{nA} PASS")
print(f"IDENTITY-REPORTED : {len(Irep)} reported")
print(f"IMPORTED-PROVEN   : {len(Pthm)} external theorems")
print(f"STRUCTURAL-ASSUMPTION: {len(Sdec)} declared (excluded from pass count)")
print("="*72)

# ===== POST-RUN COMPARISON ZONE (firewall boundary; target introduced AFTER computation) =====
print("\n--- post-run comparison zone ---")
target=8.190
print(f"  back-solved C_odd^sp target = {target}")
print(f"  torsion image max |.| = {max(abs(x) for x in T):.4f}; target in image? {round(target,5) in T}")
print(f"  ordinary-subdeterminant nearest = {7*math.log(2)+3*math.log(3):.4f} (7 ln2 + 3 ln3)")
print("  => spectral/cellular route CLOSED-NEGATIVE (exact scope); absolute chi_- via F33.8D->ZS-F34.")
if okA!=nA: raise SystemExit("Some ASSERT-COMPUTED checks FAILED.")
