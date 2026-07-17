#!/usr/bin/env python3
# =====================================================================
# zs_f48_verify_v1_6.py  -- HONEST verification suite for ZS-F48 v1.6
# Revised after external review: separates load-bearing checks from
# structural/definitional ones; RETRACTS the v1.2 annihilation "zero";
# fixes the fibre-space, the F0 sum-rule, and the Q16 status.
#   (A,Q,dim Z)=(35/437,11,2), z*, lambda_1 LOCKED. Zero fitted params.
# Exit 0 iff all *computational* checks pass. Load-bearing operator/
# physical-bridge gates are reported as CONDITIONAL, not asserted.
# =====================================================================
import numpy as np, mpmath as mp
from math import comb
from itertools import product
mp.mp.dps=40
P=[]; COND=[]
def check(name,cond,got=""):
    P.append(bool(cond)); print(f"  [{'PASS' if cond else 'FAIL'}] {name}"+(f"  ({got})" if got else ""))
def cond(name,status,note=""):
    COND.append((name,status)); print(f"  [{status}] {name}"+(f"  -- {note}" if note else ""))

A=mp.mpf(35)/437; Q=11
print("="*68); print("ZS-F48 v1.6 verification (honest ledger; load-bearing gates conditional)"); print("="*68)

# [1] anchors
print("\n[1] i-tetration anchors")
f=lambda z: mp.e**((mp.pi*1j/2)*z); z=mp.mpc(0.44,0.36)
for _ in range(300): z=f(z)
lam=(mp.pi*1j/2)*z; absl=abs(lam); absl2=absl**2; leak=1-absl2; mu=-mp.log(absl)
check("|lambda|=0.891514", abs(absl-mp.mpf('0.891514'))<1e-5, mp.nstr(absl,7))
check("arg=129.45 deg", abs(mp.degrees(mp.arg(lam))-mp.mpf('129.4455'))<1e-3)
check("|lambda|^2=0.794796", abs(absl2-mp.mpf('0.794796'))<1e-5, mp.nstr(absl2,7))
check("leak 1-|lambda|^2=0.205204", abs(leak-mp.mpf('0.205204'))<1e-5, mp.nstr(leak,7))
check("mu=-log|lambda|=0.114835", abs(mu-mp.mpf('0.114835'))<1e-5)

# [2] F0 register block: internal degeneracy (equal moduli), NOT gap-from-vacuum
print("\n[2] F0 register 2x2 block")
rl,im=float(mp.re(lam)),float(mp.im(lam)); Mf=np.array([[rl,-im],[im,rl]])
ev=np.linalg.eigvals(Mf)
check("doublet moduli EQUAL (internal degeneracy)", abs(abs(ev[0])-abs(ev[1]))<1e-12)
check("doublet decays: |lambda|<1 so gap FROM vacuum is -ln|lambda|=0.1148>0",
      float(mu)>0.1, f"mu={float(mu):.4f}")
cond("Goldstone masslessness (needs Ward identity / physical zero mode)","HYPOTHESIS")

# [3] F0 sum rule -- present the EXACT two-way identity; cite F0 three-way separately
print("\n[3] F0 retain/leak sum rule")
check("EXACT: |lambda|^2 + (1-|lambda|^2) = 1", abs((absl2+leak)-1)<1e-30,
      f"{float(absl2):.4f}+{float(leak):.4f}=1")
print("      [F0 upstream three-way (rounded): 0.7948 + 0.2050 + 0.0001 = 0.9999]")

# [4] reduced rates
print("\n[4] reduced rates")
check("lambda_fast=-A", abs(float(-A)+0.0800915)<1e-6)
check("gamma_zy=6A/Q", abs(float(6*A/Q)-0.0436862)<1e-6)

# [5] TI face Laplacian
print("\n[5] TI face Hodge Laplacian (reproduce ZS-S7)")
phi=(1+5**0.5)/2
def ep(t): return [(t[0],t[1],t[2]),(t[1],t[2],t[0]),(t[2],t[0],t[1])]
Vs=set()
for b in [(0,1,3*phi),(1,2+phi,2*phi),(phi,2,2*phi+1)]:
    for s in product([1,-1],repeat=3):
        for pp in ep(tuple(si*x for si,x in zip(s,b))): Vs.add(tuple(round(c,6) for c in pp))
Vs=np.array(sorted(Vs))
from scipy.spatial.distance import pdist,squareform
from scipy.spatial import ConvexHull
Dm=squareform(pdist(Vs)); dmin=Dm[Dm>1e-6].min()
edges=[(i,j) for i in range(len(Vs)) for j in range(i+1,len(Vs)) if abs(Dm[i,j]-dmin)<1e-3]
ei={}
for k,(a,b) in enumerate(edges): ei[(a,b)]=k; ei[(b,a)]=k
hull=ConvexHull(Vs); nm=hull.equations[:,:3]; of=hull.equations[:,3]
used=np.zeros(len(hull.simplices),bool); faces=[]
for i in range(len(hull.simplices)):
    if used[i]:continue
    g=[i];used[i]=True
    for j in range(i+1,len(hull.simplices)):
        if not used[j] and np.allclose(nm[j],nm[i],atol=1e-3) and abs(of[j]-of[i])<1e-3: g.append(j);used[j]=True
    s=set()
    for k in g:
        for v in hull.simplices[k]: s.add(v)
    faces.append(sorted(s))
def oc(vl):
    p=Vs[vl];c=p.mean(0);n=np.cross(p[1]-p[0],p[2]-p[0]);n/=np.linalg.norm(n)
    u=p[0]-c;u/=np.linalg.norm(u);w=np.cross(n,u)
    return [vl[o] for o in np.argsort([np.arctan2(np.dot(q-c,w),np.dot(q-c,u)) for q in p])]
B2=np.zeros((len(faces),len(edges)))
for fi,fc in enumerate(faces):
    cy=oc(fc)
    for k in range(len(cy)):
        a,b=cy[k],cy[(k+1)%len(cy)];e=ei[(a,b)]
        B2[fi,e]=1.0 if edges[e]==(a,b) else -1.0
wL,UL=np.linalg.eigh(B2@B2.T)
check("lambda_1=1.2428 (T1), lambda_H=5-sqrt3", abs(wL[1]-1.2428)<1e-3 and abs(wL[4]-(5-3**0.5))<1e-3)
lamT1=wL[1]

# [6] channel gate sqrt(7/4) -- with EXPLICIT unit-kernel flag
print("\n[6] channel gate (parameter-free CANDIDATE ratio, unit-kernel normalization)")
Sx=np.array([[0,1,0],[1,0,1],[0,1,0]])/np.sqrt(2)
Sy=np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]])/np.sqrt(2)
Sz=np.array([[1,0,0],[0,0,0],[0,0,-1]])
S1S2=np.real(np.kron(Sx,Sx)+np.kron(Sy,Sy)+np.kron(Sz,Sz))
evs=np.sort(np.round(np.linalg.eigvalsh(S1S2),4))
check("S1.S2 eigenvalues {-2,-1(x3),+1(x5)}", list(evs[:1])==[-2.0] and list(evs[-5:])==[1.0]*5)
ratio=np.sqrt(7/4)
check("ratio=sqrt(7/4)=1.3229 (1.7 sigma vs lattice 1.390+/-0.039)", abs(ratio-1.3229)<1e-3,
      f"{abs(ratio-1.390)/0.039:.1f}sigma")
cond("unit hyperfine coefficient g_hf=1 (form g_hf*lambda1 fixed; value assumed)","ASSUMPTION")
cond("H irrep -> continuum J=2 subduction","DERIVED-CONDITIONAL")

# [7] fibre spectrum on the CORRECT space: Hermitian coherence algebra C^omega(w,w-bar)
print("\n[7] fibre spectrum {lambda^a lambda-bar^b} on coherence algebra (NOT Hol(D))")
lc=complex(lam); N=3
M=np.diag([lc**a*np.conj(lc)**b for a in range(N) for b in range(N)])
evm=np.linalg.eigvals(M)
check("{lambda^a lambda-bar^b} realized (needs z AND z-bar)",
      any(abs(e-lc)<1e-9 for e in evm) and any(abs(e-np.conj(lc))<1e-9 for e in evm))
cond("Hol(D) one-variable Koopman gives only {lambda^n} (v1.2 conflation fixed)","NOTE")

# [8] base transfer op 5^-k ; base FIXED POINT x=1/4 ; genuine skew leading eig=1
print("\n[8] base operator, saddle fixed point, genuine skew operator")
m=5; n=10; Lb=np.zeros((n+1,n+1))
for k in range(n+1):
    for i in range(k+1):
        Lb[i,k]+=comb(k,i)*sum(j**(k-i) for j in range(m))/m**(k+1)
be=np.sort(np.abs(np.linalg.eigvals(Lb)))[::-1]
check("base T5 eigenvalues = 5^-k (Ruelle-Mayer)", np.allclose(be,[m**-k for k in range(n+1)],atol=1e-9))
check("x=1/4 is a FIXED POINT of {5x}", abs((5*0.25)%1-0.25)<1e-12)
mult=complex(2j*mp.pi*0.25*mp.e**(2j*mp.pi*0.25*z))
check("fibre multiplier at (z*,1/4) = lambda", abs(mult-lc)<1e-9)
cond("frozen C_f (x) L_base = saddle LINEARIZATION (base-global x fibre-linearized)","LOCAL-NORMAL-FORM")
cond("full skew-operator global resonances (x-averaging shifts them)","OPEN")

# [9] Koenigs coherence semiconjugacy -- MEAN channel only
print("\n[9] Koenigs coherence semiconjugacy (mean channel; NOT the Q16 instrument)")
def fn(z0,N):
    w=z0
    for _ in range(N): w=f(w)
    return w
def koen(z0,N=60): return complex((fn(z0,N)-z)/lam**N)
e2=max(float(abs(koen(f(z+dz))-lc*koen(z+dz))/abs(lc*koen(z+dz))) for dz in [0.01+0j,-0.005+0.008j])
check("phi(f(z))=lambda*phi(z) (coherence semiconjugacy EXACT)", e2<1e-4, f"err={e2:.1e}")
cond("F47 channel = Q16 Belavkin instrument","OPEN")
cond("Q16 measurement intertwiner (Born-random outcomes)","OPEN")

# [10] annihilation: v1.2 'zero' is ORIENTATION-DEPENDENT -> RETRACTED
print("\n[10] glueball annihilation: v1.2 'vanishes' RETRACTED (orientation-dependent)")
T1=UL[:,np.abs(wL-1.243)<1e-2]; harm=UL[:,np.abs(wL)<1e-6][:,0]
q0=abs(float(harm@np.sum(T1**2,axis=1)))
rng=np.random.default_rng(4); vals=[]
for _ in range(2000):
    D=rng.choice([1.0,-1.0],size=len(faces)); Bf=D[:,None]*B2
    wf,Uf=np.linalg.eigh(Bf@Bf.T); T1f=Uf[:,np.abs(wf-1.243)<1e-2]; hf=Uf[:,np.abs(wf)<1e-6][:,0]
    vals.append(abs(float(hf@np.sum(T1f**2,axis=1))))
check("v1.2 overlap is orientation-DEPENDENT (median>>0, not invariant zero)",
      np.median(vals)>0.01, f"orig={q0:.1e}, median={np.median(vals):.3f}")
sog=max(abs(float(harm@T1[:,a])) for a in range(3))
check("single-gluon <h|u_a>=0 (eigen-orthogonality, orientation-INVARIANT)", sog<1e-9)
cond("two-gluon annihilation coefficient (needs covariant cup-product vertex)","OPEN")


# [11] Saddle Diagonalization Lemma (fixes v1.3 wrong Lambda(x))
print("\n[11] Saddle Diagonalization Lemma: full-cocycle Jacobian ~ diag(lambda,5)")
zc=complex(z); lc=complex(lam)
beta=complex(2j*mp.pi*zc*mp.e**(2j*mp.pi*0.25*zc))   # = 2 pi i (z*)^2
J=np.array([[lc,beta],[0,5]])
check("Jacobian eigenvalues = {lambda,5} (beta cross-term nonzero)",
      any(abs(e-lc)<1e-9 for e in np.linalg.eigvals(J)) and any(abs(e-5)<1e-9 for e in np.linalg.eigvals(J)),
      f"beta={beta:.3f}")
sh=beta/(5-lc); T=np.array([[1,sh],[0,1]]); Jd=np.linalg.inv(T)@J@T
check("explicit shear conjugates J to diag(lambda,5)", abs(Jd[0,1])<1e-9)
cond("local product spectrum {lambda^a lambda-bar^b 5^-c} is the EXACT 1st-order normal form","PROVEN")

# [12] positive density-matrix embedding E(w), c=2 unique
print("\n[12] positive density matrix E(w): full mean-channel intertwiner")
K0=np.array([[1,0],[0,lc]],complex); K1=np.array([[0,np.sqrt(1-abs(lc)**2)],[0,0]],complex)
Phi=lambda r:K0@r@K0.conj().T+K1@r@K1.conj().T
def Ee(w,c=2.0): return np.array([[1-c*abs(w)**2, np.conj(w)],[w, c*abs(w)**2]],complex)
import random; random.seed(1); mx=0; ps=True
for _ in range(3000):
    w=random.uniform(-.5,.5)+1j*random.uniform(-.5,.5)
    if abs(w)>0.5: continue
    mx=max(mx,np.max(np.abs(Phi(Ee(w))-Ee(lc*w))))
    if np.linalg.eigvalsh(Ee(w)).min()<-1e-12: ps=False
check("Phi(E(w))=E(lambda w) EXACT on full density matrix", mx<1e-12, f"err={mx:.1e}")
check("E(w) PSD for |w|<=1/2 and E(0)=|0><0|", ps and np.allclose(Ee(0),[[1,0],[0,0]]))
cs=np.linspace(1.01,4,400)
check("c=2 uniquely maximizes positivity domain (c-1)/c^2", abs(cs[np.argmax((cs-1)/cs**2)]-2)<0.02)
cond("positive density embedding + pointer limit","PROVEN")
cond("full mean-channel intertwiner (Q16 stochastic instrument still OPEN)","DERIVED")

# [13] global skew: constant section non-uniform; genuine chi_f sign is OPEN (v1.6 corrected)
print("\n[13] global skew resonances: constant section non-uniform; genuine chi_f OPEN")
check("constant section z* is NON-uniformly contracting (Im z* < 1/e)",
      zc.imag<1/np.e, f"Im z*={zc.imag:.4f} < 1/e={1/np.e:.4f}")
# the branch-averaged surrogate does NOT converge: sign varies with iteration count.
Ng=300; xs=[(i+0.5)/Ng for i in range(Ng)]
def surrogate(niter):
    zsec=[complex(z)]*Ng
    for _ in range(niter):
        nz=[]
        for x in xs:
            acc=0j
            for j in range(5):
                xp=(x+j)/5; k=min(int(xp*Ng),Ng-1); v=np.exp(2j*np.pi*xp*zsec[k])
                acc+=(v if abs(v)<1e6 else complex(z))/5
            nz.append(acc)
        zsec=nz
    return np.mean([np.log(2*np.pi*x)-2*np.pi*x*zz.imag for x,zz in zip(xs,zsec)])
svals=[surrogate(n) for n in (60,100,200,300,400,500)]
signs=set(np.sign(svals))
check("branch-averaged surrogate does NOT converge (sign varies) -> not a genuine chi_f",
      len(signs)>1, f"values={[round(v,3) for v in svals]}")
cond("genuine invariant measure / orbit-level fibre Lyapunov exponent / global resonances","OPEN")

# [14] g_hf: channel PATTERN derived; value OBSERVATION (error propagation kills 'four digits')
print("\n[14] hyperfine coefficient g_hf: pattern DERIVED; g_hf=lambda1 OBSERVATION")
r,sr=1.390,0.039; ghf_lat=(4/3)*(r**2-1); sg=(8*r/3)*sr
clebsch_ok=np.allclose(np.sort(np.linalg.eigvalsh(S1S2)),[-2,-1,-1,-1,1,1,1,1,1],atol=1e-10)
check("Clebsch pattern <S1.S2>={-2,-1(x3),+1(x5)} exact (splitting 3)", clebsch_ok)
check("g_hf=(4/3)(r^2-1)=1.243 +/- 0.145 (1-2 sig figs, NOT four)", abs(sg-0.145)<0.005,
      f"g_hf={ghf_lat:.3f}+/-{sg:.3f}")
check("lambda1=1.2428 is a re-expression at 0 sigma (NOT independent); g_hf=1 at 1.7 sigma",
      abs(ghf_lat-lamT1)/sg<0.1 and abs(ghf_lat-1)/sg>1.5)
cond("physical ordering K2>K0 (needs positive action-derived kernel)","DERIVED-CONDITIONAL")
cond("g_hf=lambda1 (action-level derivation + out-of-sample channels pending)","OBSERVATION")

# [15] annihilation: edge-potential lift correct; naive face-wise retracted
print("\n[15] annihilation vertex: edge-potential lift (fixes 2-form^2-form error)")
a0=B2.T@T1[:,0]/lamT1
check("edge-potential lift d a_alpha = u_alpha (a=B2^T u/lambda1)", np.linalg.norm(B2@a0-T1[:,0])<1e-9)
check("canonical edge-potential norm <a,a> = 1/lambda1 (basis freedom removed)",
      abs(a0@a0-1/lamT1)<1e-6, f"{a0@a0:.4f}=1/lambda1")
cond("covariant cup-product vertex (Whitney/DEC needed; naive combinatorial not invariant)","OPEN")

# ---------- summary ----------
print("\n"+"="*68)
print(f"COMPUTATIONAL CHECKS: {sum(P)}/{len(P)} PASS")
print("LOAD-BEARING / STRUCTURAL GATES (conditional, not asserted):")
for nm,st in COND: print(f"    [{st}] {nm}")
print("="*68)
import sys; sys.exit(0 if sum(P)==len(P) else 1)
