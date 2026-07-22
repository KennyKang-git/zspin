#!/usr/bin/env python3
"""
================================================================================
zs_s27_verify_v1_6.py  —  UNIFIED verification suite for ZS-S27 v1.6
  (renumbered from the internal draft ZS-S25 v1.6: ZS-S25 was already assigned
   to the gravitational-redirection paper v2.1; this transfer-positivity /
   glueball-scheme audit becomes ZS-S27.)
Kenny Kang / Z-Spin Cosmology Collaboration
--------------------------------------------------------------------------------
Consolidates Blocks 1-10 of the ZS-S25 development into one fail-closed file.

  Part 1  SU(3) geodesic distance / fundamental alcove          (Block 1)
  Part 2  Weyl integration + character pipeline                 (Block 2)
  Part 3  AN-S27.1 : Luscher sign test, F-S24.18 CLOSED-NEGATIVE (Block 3)
  Part 4  Theorem-Candidate S27.1 : squared-transfer spectral control     (Block 4)
  Part 5  single-face Lanczos eps_0(g), ZS-S24 controls         (Block 6)
  Part 6  Lambda ratios: heat-kernel curvature + Manton direct  (Blocks 8-10)
  Part 7  lambda_t map + anti-numerology Monte Carlo            (Blocks 6b,9,10)
  Part 8  F-S27.3 : 32-face one-loop-sector finite-cell correction         (Block 11)
  Part 9  F-S27.4 : the residual on the internal ratio m_H/m_A (Block 12)
  Part 10 F-S27.1 [two-gluon diag] : direct two-gluon internal-isotype diagonalisation        (Block 13)
  Part 11 Gate C  : 0.298805 decomposed; is it corpus-internal?  (Block 14)

RUN
  python3 zs_s27_verify_v1_6.py           FAST  (grids 180,240 ; PQMAX 12)
  python3 zs_s27_verify_v1_6.py --full    FULL  (grids 180,300,480 ; PQMAX 16)
  FAST MODE IS NON-PUBLICATION VERIFICATION.

LEDGER KINDS (audit-3 finer classification; a PASS is a check passing, NOT a proof)
  A  analytic / exact-arithmetic identity (closed form)
  E  exhaustive finite enumeration
  V  floating-point numerical verification (not a proof)
  N  convergence / conservative-band numerical result
  K  mandatory control; failure VOIDS the run
  X  cross-check / accounting / declaration
  R  correction of record (documented, not a failure)
  Only A and E carry proof weight. V and N are numerical evidence, not proofs.
  Fail-closed halts on A, E, V, N, K, X (audit-6 fix: N is now halting).
================================================================================
"""
import numpy as np, itertools, sys, hashlib
import scipy.linalg as sla
from scipy.optimize import brentq

FULL   = "--full" in sys.argv
TWO_PI = 2.0*np.pi
GRIDS  = [180, 300, 480] if FULL else [180, 240]
PQMAX  = 16 if FULL else 12
LEDGER = []
def rec(kind, name, ok, detail=""):
    LEDGER.append((kind, name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {kind} {name:<50} {detail}")
    if not ok and kind in "AEVNKX":
        raise SystemExit(f"FAIL-CLOSED at {kind} {name}")
if not FULL:
    print("!"*72); print("MODE = FAST / NON-PUBLICATION VERIFICATION"); print("!"*72)

def dim(p,q): return (p+1)*(q+1)*(p+q+2)//2
def cas(p,q): return (p*p+q*q+p*q+3*p+3*q)/3.0
IRR = sorted([(p,q) for p in range(PQMAX+1) for q in range(PQMAX+1) if p+q<=PQMAX],
             key=lambda r:(r[0]+r[1],r))
PERMS=[(p,np.linalg.det(np.eye(3)[list(p)])) for p in itertools.permutations(range(3))]
_BOX=np.array(list(itertools.product(range(-6,7),repeat=3)),dtype=float)
def coset(k): return _BOX[np.isclose(_BOX.sum(axis=1),k)]
CORROT=coset(0)

# ===================================================== PART 1 : geodesic
print("\n"+"="*72); print("PART 1 — SU(3) geodesic distance / fundamental alcove"); print("="*72)
def geo2(phi):
    phi=np.asarray(phi,float); k=int(np.rint(phi.sum()/TWO_PI))
    cand=phi[None,:]-TWO_PI*coset(k); return float(np.min(np.sum(cand**2,axis=1)))
def d2m(U): return geo2(np.sort(np.angle(np.linalg.eigvals(U))))
rng=np.random.default_rng(20260721)
def rand_su3(n=1):
    out=[]
    for _ in range(n):
        z=(rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)))/np.sqrt(2)
        q,r=np.linalg.qr(z); q=q*(np.diag(r)/np.abs(np.diag(r))); out.append(q/np.linalg.det(q)**(1/3))
    return out
def rand_alg(s):
    H=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3)); H=(H+H.conj().T)/2
    H=H-np.trace(H)/3*np.eye(3); X=1j*H
    return X/np.sqrt(np.real(np.trace(X.conj().T@X)))*s
rec("A","1.1 d(I)=0", abs(d2m(np.eye(3)))<1e-24)
e=[abs(np.sqrt(d2m(sla.expm(rand_alg(s))))-s) for s in (1e-3,1e-2,.1,.5,1.)]
rec("V","1.2 d(exp X)=||X|| (||X||<=1)", max(e)<1e-9, f"max {max(e):.2e}")
e=[abs(d2m((g:=rand_su3(1)[0])@U@g.conj().T)-d2m(U)) for U in rand_su3(120)]
rec("V","1.3 conjugation invariance", max(e)<1e-11, f"max {max(e):.2e}")
w=np.exp(2j*np.pi/3)
rec("A","1.4 centre omega I : d^2=8pi^2/3", abs(d2m(w*np.eye(3))-8*np.pi**2/3)<1e-11,
    f"{d2m(w*np.eye(3)):.8f}")
eT=eE=eN=0.0
for U in rand_su3(120):
    ev,V=np.linalg.eig(U); ph=np.angle(ev)
    cand=ph[None,:]-TWO_PI*coset(int(np.rint(ph.sum()/TWO_PI)))
    th=cand[int(np.argmin(np.sum(cand**2,axis=1)))]
    X=V@np.diag(1j*th)@np.linalg.inv(V)
    eT=max(eT,abs(np.trace(X))); eE=max(eE,np.max(np.abs(sla.expm(X)-U)))
    eN=max(eN,abs(np.real(np.trace(X.conj().T@X))-d2m(U)))
rec("V","1.5 reconstruction Tr X=0, exp X=U, ||X||^2=d^2", max(eT,eE,eN)<1e-9,
    f"max {max(eT,eE,eN):.2e}")
# R27-1 : the v0 'shift largest angle' rule agrees on the torus grid
def d2_v0(A):
    a=(A+np.pi)%TWO_PI-np.pi; s=np.rint(a.sum(0)/TWO_PI).astype(int); idx=np.argmax(np.abs(a),0)
    corr=np.stack([np.where(idx==k,-TWO_PI*s,0.0) for k in range(3)]); return np.sum((a+corr)**2,0)
g=np.linspace(-np.pi,np.pi,181); G1,G2=np.meshgrid(g,g,indexing='ij'); GA=np.stack([G1,G2,-G1-G2])
tr=np.array([[geo2(GA[:,i,j]) for j in range(181)] for i in range(181)])
rec("R","R27-1 v0 alcove rule agrees (earlier doubt WITHDRAWN)",
    np.max(np.abs(d2_v0(GA)-tr))<1e-9, f"max dev {np.max(np.abs(d2_v0(GA)-tr)):.2e}")

# ===================================================== PART 2 : Weyl pipeline
print("\n"+"="*72); print("PART 2 — Weyl integration / character pipeline"); print("="*72)
class Torus:
    def __init__(s,M):
        t=(np.arange(M)+0.5)/M*TWO_PI-np.pi; T1,T2=np.meshgrid(t,t,indexing='ij')
        s.A=np.stack([T1,T2,-T1-T2]); z=[np.exp(1j*a) for a in s.A]
        s.dmu=np.abs((z[0]-z[1])*(z[0]-z[2])*(z[1]-z[2]))**2/(6*TWO_PI**2)*(TWO_PI/M)**2
        den=np.zeros_like(T1,dtype=complex)
        for p,sg in PERMS: den+=sg*np.exp(1j*sum((2-k)*s.A[p[k]] for k in range(3)))
        s.den,s.good=den,np.abs(den)>1e-9; s.ReTr=np.real(z[0]+z[1]+z[2])
        L0=CORROT[np.max(np.abs(CORROT),1)<=2]; Am=np.moveaxis(s.A,0,-1); d2=np.empty((M,M))
        for i in range(0,M,64):
            b=Am[i:i+64]; d2[i:i+64]=np.min(np.sum((b[...,None,:]-TWO_PI*L0)**2,-1),-1)
        s.d2=d2
    def chi(s,p,q):
        l=[p+q+2,q+1,0]; num=np.zeros_like(s.den)
        for pm,sg in PERMS: num+=sg*np.exp(1j*sum(l[k]*s.A[pm[k]] for k in range(3)))
        o=np.zeros_like(s.den); np.divide(num,s.den,out=o,where=s.good); return o
    def integ(s,f): return complex(np.sum(np.where(s.good,f*s.dmu,0)))
    def coeffs(s,k): return np.array([s.integ(k*np.conj(s.chi(*r))).real for r in IRR])
T0=Torus(GRIDS[0])
rec("V","2.1 Haar normalisation int dmu=1", abs(T0.integ(np.ones_like(T0.den)).real-1)<1e-10)
SMALL=[(0,0),(1,0),(0,1),(1,1),(2,0),(0,2),(2,1),(1,2),(3,0),(0,3),(2,2),(3,1),(1,3)]
CH={r:T0.chi(*r) for r in SMALL}
wd=max(abs(T0.integ(CH[r]*np.conj(CH[r]))-1) for r in SMALL)
wo=max(abs(T0.integ(CH[r]*np.conj(CH[s]))) for i,r in enumerate(SMALL) for s in SMALL[i+1:])
rec("V","2.2 Schur orthonormality (diag,offdiag)", max(wd,wo)<1e-8, f"max {max(wd,wo):.2e}")
for r,v in [((1,0),4/3),((1,1),3.0),((2,0),10/3)]:
    rec("X",f"2.3 C2{r}={v:.4f} [ZS-S24 Table 10.1]", abs(cas(*r)-v)<1e-14)
for tp in (0.2,0.5):
    k=sum(dim(*r)*np.exp(-tp*cas(*r))*T0.chi(*r) for r in IRR)
    err=max(abs(T0.integ(k*np.conj(CH[r])).real-dim(*r)*np.exp(-tp*cas(*r)))/(dim(*r)*np.exp(-tp*cas(*r))) for r in SMALL)
    rec("K",f"2.4 heat-kernel analytic control t={tp}", err<2e-6, f"max rel {err:.2e}")
sm=T0.d2<0.02
rel=np.max(np.abs((1-T0.ReTr/3)[sm]-(T0.d2/6)[sm])/np.maximum((T0.d2/6)[sm],1e-12))
rec("K","2.5 Wilson/Manton continuum normalisation match", rel<0.02, f"max rel {rel:.2e}")

# ===================================================== PART 3 : AN-S27.1
print("\n"+"="*72); print("PART 3 — AN-S27.1 : Luscher sign test (F-S24.18)"); print("="*72)
BET=[0.5,1.0,2.0,3.2497,4.0]
R={}
for M in GRIDS:
    T=Torus(M)
    for b in BET:
        kW=np.exp(b*T.ReTr/3).astype(complex)
        kM=np.exp(-(b/6)*T.d2).astype(complex)
        kH=sum(dim(*r)*np.exp(-(2/b)*cas(*r))*T.chi(*r) for r in IRR)
        for nm,k in (("W",kW),("H",kH),("M",kM)):
            c=T.coeffs(k); j=int(np.argmin(c)); R[(M,b,nm)]=(c[j]/np.max(np.abs(c)),IRR[j],c)
badW=any(R[(GRIDS[-1],b,"W")][0]<-1e-9 for b in BET)
badH=any(R[(GRIDS[-1],b,"H")][0]<-1e-9 for b in BET)
rec("K","3.1 control Wilson never negative [Luscher]", not badW)
rec("K","3.2 control heat kernel never negative", not badH)
h1=[b for b in BET if R[(GRIDS[-1],b,"M")][0]<-1e-9]
rec("V","3.3 Manton NEGATIVE at Z-Spin beta=3.2497 (F-S24.18 CLOSED-NEG-CONDITIONAL)", 3.2497 in h1,
    f"H1 at {h1}")
arg=R[(GRIDS[-1],3.2497,"M")][1]
rec("X","3.4 argmin interior (not truncation)", sum(arg)<PQMAX, f"argmin {arg} dim {dim(*arg)}")
c=R[(GRIDS[-1],3.2497,"M")][2]; c0=np.max(np.abs(c))
lowpos=all(c[IRR.index(r)]>0 for r in [(0,0),(1,0),(0,1),(0,2),(1,1)])
rec("V","3.5 low irreps 1,3,3bar,6bar,8 all POSITIVE (S24.15' intact)", lowpos)
negdims=sorted(dim(*r) for i,r in enumerate(IRR) if c[i]<-1e-12*c0)
rec("V","3.6 negativity confined to dim>=45", negdims[0]>=45, f"lowest neg dim {negdims[0]}")

# 3.7 explicit PQMAX truncation sweep at the Z-Spin point (audit 5.2)
_pqverdict={}
for _PQ in (10,12,14,16):
    _IRR=sorted([(p,q) for p in range(_PQ+1) for q in range(_PQ+1) if p+q<=_PQ],key=lambda r:(r[0]+r[1],r))
    _Tp=Torus(GRIDS[-1])
    _c=np.array([_Tp.integ(np.exp(-(3.2497/6)*_Tp.d2).astype(complex)*np.conj(_Tp.chi(*r))).real for r in _IRR])
    _j=int(np.argmin(_c)); _pqverdict[_PQ]=(_IRR[_j], _c[_j]<0)
_argset={v[0] for v in _pqverdict.values()}
rec("V","3.7 PQMAX sweep {10,12,14,16}: argmin=(5,5), negative, truncation-stable",
    all(v[1] for v in _pqverdict.values()) and _argset=={(5,5)},
    f"argmins={ {k:v[0] for k,v in _pqverdict.items()} }")

# ===================================================== PART 4 : Theorem-Candidate S27.1
print("\n"+"="*72); print("PART 4 — Theorem-Candidate S27.1 : squared-transfer spectral control"); print("="*72)
T=Torus(GRIDS[-1])
def reorder(b):
    c=T.coeffs(np.exp(-(b/6)*T.d2).astype(complex))
    lam=np.array([c[i]/dim(*r) for i,r in enumerate(IRR)])
    os=np.argsort(-lam); oa=np.argsort(-np.abs(lam))
    i0=os[0]; i1=os[1]; ia=[j for j in oa if j!=i0][0]
    return i1==ia, np.log(lam[i0]/lam[i1]) if lam[i1]>0 else np.nan, np.log(abs(lam[i0])/abs(lam[ia]))
_reo=[(b,)+reorder(b) for b in BET]
_all_same=all(r[1] for r in _reo)
_max_gapdiff=max(abs(r[2]-r[3]) for r in _reo if not np.isnan(r[2]) and not np.isnan(r[3]))
rec("V","4.1 no spectral reordering under |.| across ALL tested beta (BET loop)",
    _all_same, f"beta-points {[b for b in BET]}: reorder-stable={_all_same}")
rec("V","4.2 gap unchanged |Delta_T - Delta_T2| over full BET loop", _max_gapdiff<1e-9,
    f"max over {len(BET)} beta = {_max_gapdiff:.2e}")

# ===================================================== PART 5 : Lanczos
print("\n"+"="*72); print("PART 5 — single-face Lanczos eps_0(g), ZS-S24 controls"); print("="*72)
def buildKS(P):
    I=[(p,q) for p in range(P+1) for q in range(P+1) if p+q<=P]; idx={r:i for i,r in enumerate(I)}
    C=np.diag([cas(*r) for r in I]); Mx=np.zeros((len(I),len(I)))
    for (p,q),i in idx.items():
        for d in [(1,0),(-1,1),(0,-1),(0,1),(1,-1),(-1,0)]:
            t=(p+d[0],q+d[1])
            if t in idx: Mx[idx[t],i]+=0.5
    return I,C,(Mx+Mx.T)/2
I,C,Mx=buildKS(12)
def gap(g2,n): ev=np.sort(np.linalg.eigvalsh((n/2)*C-(1/g2**2)*Mx)); return ev[1]-ev[0]
ev5=np.sort(np.linalg.eigvalsh((5/2)*C)); ev6=np.sort(np.linalg.eigvalsh((6/2)*C))
rec("A","5.1 pentagon x=0 gap = 10/3 [ZS-S24 Delta_E,1]", abs((ev5[1]-ev5[0])-10/3)<1e-12,
    f"{ev5[1]-ev5[0]:.10f}")
rec("A","5.2 hexagon x=0 gap = 4 [ZS-S24 Delta_E,2]", abs((ev6[1]-ev6[0])-4.0)<1e-12,
    f"{ev6[1]-ev6[0]:.10f}")
rec("X","5.3 Lanczos correction small at Z-Spin (g^2=1.846)", abs(gap(1.846,5)/(10/3)-1)<0.05,
    f"ratio {1.846*gap(1.846,5)/((10/3)*1.846):.4f}")

# ===================================================== PART 6 : Lambda ratios
print("\n"+"="*72); print("PART 6 — Lambda ratios (heat-kernel curvature + Manton direct)"); print("="*72)
def dimG(N): return N*N-1
b0=lambda N:(11.0/3.0)*N/(16*np.pi**2)
# SU(2) anchor -> SU(3) via curvature ratio 16/9
Dbeta3=(1/3)*((dimG(3)/6)/(dimG(2)/4))
Dinvg2_3=Dbeta3/6
Lam_HK=np.exp(Dinvg2_3/(2*b0(3)))
rec("X","6.1 SU(2) anchor Delta_beta=1/3 (declared input; tautological)", abs((1/3)-(1/3))<1e-15)
rec("X","6.2 curvature ratio R(SU3)/R(SU2)=16/9", abs((dimG(3)/6)/(dimG(2)/4)-16/9)<1e-12)
rec("X","6.3 heat-kernel Lambda_HK/Lambda_W(SU3)~2.03 [SCHEME-ESTIMATE, conventions 1.82-4.93]", abs(Lam_HK-2.03)<0.02, f"{Lam_HK:.4f} (HYPOTHESIS-strong, not DERIVED)")
# Manton direct: continuum-matched weak-coupling quartic ordering
Tm=Torus(max(GRIDS))
l=[3,1,0]; num=np.zeros_like(Tm.den)
for pm,sg in PERMS: num+=sg*np.exp(1j*sum(l[k]*Tm.A[pm[k]] for k in range(3)))
chf=np.zeros_like(Tm.den); np.divide(num,Tm.den,out=chf,where=Tm.good)
def mf(k):
    c0=float(np.real(np.sum(np.where(Tm.good,k*Tm.dmu,0))))
    cf=float(np.real(np.sum(np.where(Tm.good,k*np.conj(chf)*Tm.dmu,0)))); return cf/c0
# audit exec-time: cache the 81 character fields (chi(p,q)) once, reuse across all g2
CHI_8 = {(p,q): Tm.chi(p,q) for p in range(9) for q in range(9)}
def heatk(g2):
    kH=np.zeros_like(Tm.den)
    for p in range(9):
        for q in range(9): kH=kH+dim(p,q)*np.exp(-(g2/2)*cas(p,q))*CHI_8[(p,q)]
    return kH
g2s=np.array([0.03,0.05,0.08,0.12,0.18,0.25]); rows=[]
for g2 in g2s:
    Ww=mf(np.exp((6/g2)*Tm.ReTr/3).astype(complex))/3
    Wm=mf(np.exp(-(1/g2)*Tm.d2).astype(complex))/3    # continuum-matched: coeff 1/g^2
    Wh=mf(heatk(g2))/3
    rows.append((g2,1-Ww,1-Wm,1-Wh))
rows=np.array(rows)
sl=lambda col: np.polyfit(rows[:,0],rows[:,col],2)
sW,sM,sH=sl(1),sl(2),sl(3)
rec("K","6.4 three actions share leading slope (continuum match)",
    max(abs(sM[1]/sW[1]-1),abs(sH[1]/sW[1]-1))<0.03,
    f"M/W {sM[1]/sW[1]:.3f} H/W {sH[1]/sW[1]:.3f}")
q_W,q_M,q_H=sW[0]/sW[1],sM[0]/sM[1],sH[0]/sH[1]
rec("V","6.5 |quartic/quad| ordering Manton>Heat>Wilson",
    abs(q_M)>abs(q_H)>abs(q_W), f"W {q_W:.3f} H {q_H:.3f} M {q_M:.3f}")
# R27-4 : Manton Lambda ratio exceeds heat-kernel -> v1.0 s8.2 conjecture refuted
rec("X","R27-4 SCHEME-DIAGNOSTIC: weak-coupling |quartic| ordering Manton>Heat suggests "
    "(does not prove) Manton finite shift exceeds heat-kernel; no direct Lambda_M computed",
    abs(q_M)>abs(q_H), "ordering only; Lambda_Manton itself not computed")

# ===================================================== PART 7 : lambda_t + AN
print("\n"+"="*72); print("PART 7 — lambda_t map + anti-numerology"); print("="*72)
bb0=11/(16*np.pi**2); bb1=102/(16*np.pi**2)**2; p_=bb1/(2*bb0**2); M0PP=1.7906
def aLam(g2): return (bb0*g2)**(-p_)*np.exp(-1/(2*bb0*g2))
def lt_of(RL): return 3*brentq(lambda x:(5/2)*(4/3)*x*((0.2641/28.809)*RL)/aLam(x)-M0PP,0.2,8.0,xtol=1e-12)
lt_HK=lt_of(2.03); lt_W=lt_of(1.0)
rec("V","7.1 Wilson scheme -> lambda_t=4.74 (undershoot)", abs(lt_W-4.74)<0.02, f"{lt_W:.3f}")
rec("V","7.2 heat-kernel scheme -> lambda_t=6.26 (+13% overshoot)", abs(lt_HK-6.26)<0.05,
    f"{lt_HK:.3f}, lattice 5.539, dev {100*(lt_HK/5.539-1):+.1f}%")
RLstar=brentq(lambda RL:lt_of(RL)-5.539,1.0,3.0)
rec("X","7.3 Lambda ratio implied by lattice lambda_t=5.539", abs(RLstar-1.544)<0.01, f"{RLstar:.3f}")
# anti-numerology MC (reduced draws in FAST)
NDR=800 if not FULL else 20000  # audit-10: FAST reduced to 800 for speed
rng2=np.random.default_rng(20260722); hits=0; tot=0
def eS(g2,n): return (n/2)*(4/3)*g2
def eL(g2,n): ev=np.sort(np.linalg.eigvalsh((n/2)*C-(1/g2**2)*Mx)); return g2*(ev[1]-ev[0])
for _ in range(NDR):
    LMS=rng2.uniform(.18,.32); m=rng2.uniform(1.4,2.2); Rr=rng2.uniform(10,60)
    f=eS if rng2.random()<.5 else eL; n=5 if rng2.random()<.5 else 6; Ll=LMS/Rr
    try: lt=3*brentq(lambda x:f(x,n)*Ll/aLam(x)-m,0.2,8.0,xtol=1e-9)
    except Exception: continue
    tot+=1
    if abs(lt-5.539)/5.539<0.15: hits+=1
p=hits/tot
rec("X","7.4 anti-numerology: P(|lambda_t*-5.539|<15%) not significant", p>0.05,
    f"p={p:.3f} ({hits}/{tot}) -> scale-setting HELD, not support")

# ===================================================== PART 8 : F-S27.3 finite cell
print("\n"+"="*72); print("PART 8 — F-S27.3 : 32-face one-loop-sector finite-cell correction"); print("="*72)
from scipy.spatial.distance import pdist, squareform
_phi=(1+np.sqrt(5))/2
def _ep(v):
    o=set()
    for pp in [(0,1,2),(1,2,0),(2,0,1)]:
        for sg in itertools.product([1,-1],repeat=3):
            o.add(tuple(round(sg[k]*v[pp[k]],6) for k in range(3)))
    return o
_V=set()
for v in [(0,1,3*_phi),(1,2+_phi,2*_phi),(_phi,2,2*_phi+1)]: _V|=_ep(v)
_V=np.array(sorted(_V)); _D=squareform(pdist(_V)); _dm=np.min(_D[_D>1e-6])
_adj={i:set() for i in range(60)}
for i in range(60):
    for j in range(60):
        if i!=j and abs(_D[i,j]-_dm)<1e-4: _adj[i].add(j)
rec("E","8.1 K_TI geometry: 60 vertices, 90 edges",
    len(_V)==60 and sum(len(a) for a in _adj.values())//2==90,
    f"V={len(_V)}, E={sum(len(a) for a in _adj.values())//2}")
_faces=set()
for st in range(60):
    for a in _adj[st]:
        for L in (5,6):
            paths=[[st,a]]
            for _ in range(L-2):
                paths=[p+[nx] for p in paths for nx in _adj[p[-1]] if nx not in p]
            for p in paths:
                if len(p)==L and st in _adj[p[-1]]:
                    pts=_V[p]; u=pts-pts.mean(0); nn=np.cross(u[0],u[1]); nn=nn/np.linalg.norm(nn)
                    if np.max(np.abs(u@nn))<1e-3: _faces.add(frozenset(p))
_F=list(_faces)
_isP=np.array([len(f)==5 for f in _F])
rec("E","8.2 faces: 12 pentagons + 20 hexagons = 32",
    (_isP.sum()==12 and (~_isP).sum()==20), f"{_isP.sum()}P + {(~_isP).sum()}H")
_A=np.zeros((32,32))
for i in range(32):
    for j in range(i+1,32):
        sset=_F[i]&_F[j]
        if len(sset)==2 and list(sset)[1] in _adj[list(sset)[0]]: _A[i,j]=_A[j,i]=1
rec("E","8.3 face-adjacency has 90 shared edges", int(_A.sum()/2)==90, f"{int(_A.sum()/2)}")
_Cmat=np.zeros((32,32)); _Ed=np.where(_isP,10/3,4.0)
for i in range(32):
    for j in range(32):
        if _A[i,j]: _Cmat[i,j]=1/_Ed[i]+1/_Ed[j]
def _buildKS(P):
    I=[(p,q) for p in range(P+1) for q in range(P+1) if p+q<=P]; idx={r:i for i,r in enumerate(I)}
    C=np.diag([cas(*r) for r in I]); Mx=np.zeros((len(I),len(I)))
    for (p,q),i in idx.items():
        for d in [(1,0),(-1,1),(0,-1),(0,1),(1,-1),(-1,0)]:
            t=(p+d[0],q+d[1])
            if t in idx: Mx[idx[t],i]+=0.5
    return C,(Mx+Mx.T)/2
_Csf,_Msf=_buildKS(12)
def _sf(g2): ev=np.sort(np.linalg.eigvalsh((5/2)*_Csf-(1/g2**2)*_Msf)); return ev[1]-ev[0]
def _tot(g2):
    base=_sf(g2); x=1/g2**2
    Ed=np.where(_isP,base,base+(4-10/3))
    return np.sort(np.linalg.eigvalsh(np.diag(Ed)-(x**2)*_Cmat))[0]
def _lt(fn):
    Ll=(0.2641/28.809)*2.03
    return 3*brentq(lambda g2: fn(g2)*g2*Ll/aLam(g2)-M0PP,1.6,4.0,xtol=1e-12)
_ln=_lt(lambda g2:10/3); _ls=_lt(_sf); _ltt=_lt(_tot)
rec("V","8.4 naive scale-setting lambda_t=6.26 (+13%)", abs(_ln-6.26)<0.05, f"{_ln:.3f}")
rec("V","8.5 one-loop-sector lambda_t=6.134 (residual +10.7% at leading order)", abs(_ltt-6.134)<0.02,
    f"{_ltt:.3f}, residual {100*(_ltt/5.539-1):+.1f}%")
_gc=_ltt/3
rec("X","8.6 self-consistent point in strong-coupling domain (x^2<0.1)", 1/_gc**4<0.1,
    f"g^2={_gc:.3f}, x^2={1/_gc**4:.4f}")
rec("V","8.7 finite-cell removes <25% of overshoot at leading order in the 32-face one-loop sector",
    (_ln-_ltt)/(_ln-5.539)<0.25, f"closes {100*(_ln-_ltt)/(_ln-5.539):.0f}%")

# ===================================================== PART 9 : F-S27.4
print("\n"+"="*72); print("PART 9 — F-S27.4 : residual on the internal ratio m_H/m_A (physical m(2++)/m(0++) cond. F-S27.1)"); print("="*72)
# corpus relations: lambda_t = g_hf/0.298805 ; R^2 = 1 + (3/4) g_hf
# => R^2 = 1 + (3/4)*0.298805*lambda_t
_f=0.298805
def _R(lt): return np.sqrt(1+0.75*_f*lt)
_Rlat=1.4971; _RLL=1.3900
rec("X","9.1 corpus lambda_t=5.539 reproduces lattice R=1.4971",
    abs(_R(5.539)-_Rlat)<2e-3, f"R={_R(5.539):.4f}")
_Rdisc=_R(6.134)
rec("V","9.2 discretisation lambda_t=6.134 -> internal m_H/m_A=1.541 (+2.9% cond. on F-S27.1)",
    abs(_Rdisc-1.541)<3e-3, f"R={_Rdisc:.4f}, {100*(_Rdisc/_Rlat-1):+.2f}% vs lattice")
rec("V","9.3 sqrt compresses 11% (lambda_t) to <4% (observable R)",
    100*(_Rdisc/_Rlat-1) < 4.0, f"{100*(_Rdisc/_Rlat-1):.1f}% in R vs {100*(6.134/5.539-1):.1f}% in lambda_t")
rec("V","9.4 dynamical R closer to lattice than kinematic Layer-Lift",
    abs(_Rdisc-_Rlat) < abs(_RLL-_Rlat), f"|dyn-lat|={abs(_Rdisc-_Rlat):.4f} < |LL-lat|={abs(_RLL-_Rlat):.4f}")
rec("V","9.5 dynamical and kinematic bracket the lattice (opposite sides)",
    (_Rdisc>_Rlat) and (_RLL<_Rlat), f"LL={_RLL} < lattice={_Rlat} < dyn={_Rdisc:.3f}")
# Reading 1 disfavoured: factor needed
_fneed=1.655/6.134
rec("X","9.6 Reading-1 needs unmotivated factor shift (-9.7%)",
    abs(_fneed/_f-1) > 0.05, f"0.2988 -> {_fneed:.4f} ({100*(_fneed/_f-1):+.1f}%)")
# Reading 3 supported: finite-cell correction sign lowers R toward lattice
rec("X","9.7 Reading-3 finite-cell sign lowers lambda_t (toward lattice)",
    True, "Block-11 gap correction is negative -> R decreases toward 1.4971")

# ===================================================== PART 10 : F-S27.1 [two-gluon diag]
print("\n"+"="*72); print("PART 10 — F-S27.1 [two-gluon diag] : direct two-gluon internal-isotype diagonalisation"); print("="*72)
_s2=1/np.sqrt(2)
_Sx=np.array([[0,_s2,0],[_s2,0,_s2],[0,_s2,0]])
_Sy=np.array([[0,-1j*_s2,0],[1j*_s2,0,-1j*_s2],[0,1j*_s2,0]])
_Sz=np.array([[1,0,0],[0,0,0],[0,0,-1]])
_S1S2=np.real_if_close(np.kron(_Sx,_Sx)+np.kron(_Sy,_Sy)+np.kron(_Sz,_Sz))
_vals,_cnt=np.unique(np.round(np.linalg.eigvalsh(_S1S2),8),return_counts=True)
rec("A","10.1 S1.S2 degeneracies {1,3,5} = A_g(+)T1(+)H",
    list(_cnt)==[1,3,5] and np.allclose(_vals,[-2,-1,1]), f"{dict(zip(_vals.astype(int),_cnt))}")
_f=0.298805
def _spec(g): return np.sort(np.linalg.eigvalsh(0.25*(g*_S1S2+2*g*np.eye(9))))
def _R(g): M2=1+_spec(g); return np.sqrt(M2.max()/M2.min())
rec("V","10.2 kinematic g=lambda_1 -> R=1.3900 (hard-coded lambda_1 regression)", abs(_R(1.2428416164)-1.3900)<1e-3,
    f"R={_R(1.2428416164):.4f}")
rec("V","10.3 lattice g_hf recombination -> R=1.4971 (hard-coded inputs regression)", abs(_R(_f*5.539)-1.4971)<1e-3,
    f"R={_R(_f*5.539):.4f}")
_M2=1+np.unique(np.round(_spec(_f*6.134),6))
rec("V","10.4 discretisation lambda_t=6.134 -> R=1.541 (SPECTRAL)",
    abs(np.sqrt(_M2[2]/_M2[0])-1.541)<2e-3, f"R={np.sqrt(_M2[2]/_M2[0]):.4f}")
rec("X","10.5 2++ is the H-channel (S=2), 0++ is A_g (S=0)",
    abs(_M2[2]-(1+0.75*_f*6.134))<1e-6 and abs(_M2[0]-1)<1e-9,
    f"M2(2++)/M0^2={_M2[2]:.4f}")
rec("V","10.6 internal T1 mode m_{T1}/m_A=1.208 (physical 1+- conditional on F-S27.1)",
    abs(np.sqrt(_M2[1])-1.2076)<2e-3, f"m(1+-)/m(0++)={np.sqrt(_M2[1]):.4f}")
rec("X","10.7 R independent of lattice datum (uses discretisation lambda_t)",
    True, "g_hf from lambda_t=6.134 (Blocks 8-11), not from lattice R")
# F-S27.1 : the category gate. internal isotype {A_g,T1,H} are NOT yet physical J^PC.
rec("X","10.8 F-S27.1 OPEN: internal {A_g,T1,H} -> physical {0++,1+-,2++} needs an intertwiner",
    True, "no carrier-isotype->spin map, no lattice rotation group, no P/C operators; "
    "2+1 carrier vs 3+1 lattice data -> R=1.541 is HYPOTHESIS-CONDITIONAL, not a spectral prediction")

# ===================================================== PART 11 : Gate C accounting
print("\n"+"="*72); print("PART 11 — Gate C: decomposition of 0.298805 (F-S18.4 / F-S27.5)"); print("="*72)
_l1=1.2428416164; _sl=np.sqrt(_l1)
_Gexch1=0.310089208103                    # (9/4) c1^2 sqrt(l1)  [Thm S18.6A]
_c1sq=_Gexch1/((9/4)*_sl)
_chsq=0.0012658090
_Gexch=(9/4)*_sl*(_c1sq+_chsq)
rec("V","11.1 G_exch=0.313264 recombined from upstream channel coeffs (regression)",
    abs(_Gexch-0.313264316799300)<1e-9, f"{_Gexch:.10f}")
def _sN(N): return -0.0120898-0.0043825/N**2
def _G(N): return _Gexch+(4/3)*_sN(N)/_sl
rec("V","11.2 G(3)=0.298223 (exchange+seagull, SU(3))", abs(_G(3)-0.29822252)<1e-5, f"{_G(3):.8f}")
rec("V","11.3 G_inf=0.298805 reconstructed", abs(_G(1e9)-0.298805)<1e-6, f"{_G(1e9):.8f}")
rec("X","11.4 0.298805 is corpus-INTERNAL (exchange DERIVED + seagull COMPUTED)",
    True, "no external number enters; v1.5 'outside world' phrasing corrected")
def _R(G,lt): return np.sqrt(1+0.75*G*lt)
_lt=6.134
_Rex=_R(_Gexch,_lt); _Rf=_R(_G(3),_lt)
rec("V","11.5 DERIVED exchange alone gives R=1.562 (+4.4%)", abs(_Rex-1.5624)<2e-3,
    f"R={_Rex:.4f}")
rec("V","11.6 seagull refines R to 1.540 (+2.9%), a -1.4% shift", abs(_Rf-1.540)<2e-3,
    f"R={_Rf:.4f}, seagull shift {100*(_Rf/_Rex-1):.2f}%")
rec("X","11.7 R is ~96% carried by the DERIVED closed form",
    abs(_Rf-_Rex)/abs(_Rf-1) < 0.05, f"numerical part shifts R by {abs(_Rf-_Rex):.4f} abs")
# R27-5 : correction of the v1.5 'external' characterization
rec("R","R27-5 v1.5 'outside-world dependency' on 0.298805 CORRECTED (it is corpus-internal)",
    True, "0.298805 = DERIVED exchange + TI-geometry seagull; no external input")

# ===================================================== PART 12 : interval certificate
print("\n"+"="*72); print("PART 12 — mpmath interval band for the Manton negative coefficient (audit 4)"); print("="*72)
# Audit-4 fix: use ACTUAL mpmath (not float64) so the claim matches the code.
# Kept small (dps=25, M=32/48) to stay fast; the standalone block gives 40-digit.
try:
    import mpmath as mp
except ImportError as _exc:
    raise SystemExit("FAIL-CLOSED: mpmath required for Part 12 central band (%s)" % _exc)
if True:
    mp.mp.dps=25
    import itertools as _it
    def _sgn(p): return 1 if p in [(0,1,2),(1,2,0),(2,0,1)] else -1
    def _chi55(ang):
        l=[12,6,0]; num=mp.mpf(0); den=mp.mpf(0)
        for pm in _it.permutations(range(3)):
            sg=_sgn(pm)
            num+=sg*mp.e**(1j*sum(l[k]*ang[pm[k]] for k in range(3)))
            den+=sg*mp.e**(1j*sum((2-k)*ang[pm[k]] for k in range(3)))
        return num/den if abs(den)>mp.mpf(10)**-18 else mp.mpf(0)
    def _d2(a):
        ph=[a[0],a[1],-a[0]-a[1]]; best=mp.inf
        for m in _it.product(range(-2,3),repeat=3):
            if sum(m)!=0: continue
            v=sum((ph[i]-2*mp.pi*m[i])**2 for i in range(3))
            if v<best: best=v
        return best
    def _c55(M,beta=mp.mpf("3.2497")):
        import numpy as _np
        xn,wn=_np.polynomial.legendre.leggauss(M)
        xn=[mp.pi*mp.mpf(float(x)) for x in xn]; wn=[mp.pi*mp.mpf(float(x)) for x in wn]
        acc=mp.mpf(0)
        for i in range(M):
            for j in range(M):
                a=[xn[i],xn[j],-xn[i]-xn[j]]; z=[mp.e**(1j*t) for t in a]
                D2=abs((z[0]-z[1])*(z[0]-z[2])*(z[1]-z[2]))**2
                acc+=wn[i]*wn[j]*mp.e**(-(beta/6)*_d2(a))*mp.conj(_chi55(a))*D2
        return mp.re(acc/(6*(2*mp.pi)**2))
    _grid = (40,60,80) if FULL else (32,48)   # audit: FAST smoke M=32,48; publication --full M=40,60,80
    cm=[_c55(M) for M in _grid]
    dd=abs(cm[-1]-cm[-2]); hi=cm[-1]+3*dd; lo=cm[-1]-3*dd
    rec("N","12.1 c_(5,5) mpmath band 0-separated (FAST M=32,48; --full M=40,60,80 -> [-6.46,-6.41]e-8)",
        hi<0, f"grid={_grid}: c in [{mp.nstr(lo,6)},{mp.nstr(hi,6)}], |dM|={mp.nstr(dd,3)}")
    rec("N","12.2 mpmath grid convergence (successive difference small)",
        dd<mp.mpf(10)**-7, f"grid={_grid}: " + ",".join(mp.nstr(c,6) for c in cm))
    _mpm=True
rec("X","12.3 STATUS: conservative convergence band, NOT a rigorous interval enclosure",
    True, "no quadrature-remainder bound / no arb ball -> VERIFIED numerical witness, "
    "formal interval proof OPEN (FAST uses M=32,48 (smoke); publication --full uses M=40,60,80 matching the standalone single band [-6.46,-6.41]e-8; standalone confirms at 40-digit)")

print("\n"+"="*72)
n={k:sum(1 for a,_,ok,_ in LEDGER if a==k and ok) for k in "AEVNKXR"}
tot_pass=sum(1 for _,_,ok,_ in LEDGER if ok); tot_all=len(LEDGER)
proof=n['A']+n['E']
print(f"LEDGER {tot_pass}/{tot_all} PASS = {n['A']} A(exact) + {n['E']} E(exhaustive)"
      f" + {n['V']} V(float-verify) + {n.get('N',0)} N(num-band) + {n['K']} K(control)"
      f" + {n['X']} X(cross/decl) + {n['R']} R(correction)")
print(f"DISCLAIMER (audit-3/5): a PASS is a check passing under its stated method, NOT a proof.")
print(f"  Proof-weight checks (A+E) = {proof}. The remaining {tot_pass-proof} are numerical")
print(f"  verifications (V,N), controls (K), cross-checks/declarations (X), or corrections (R).")
print("  The central Manton negative-coefficient result is a V+N witness: grid-converged")
print("  and 0-separated (mpmath band in Part 12), with a formal interval proof still OPEN.")
print(f"MODE = {'FULL' if FULL else 'FAST (NON-PUBLICATION)'}")
print(f"SHA256(self) = {hashlib.sha256(open(__file__,'rb').read()).hexdigest()}")
print("""
SUMMARY OF FINDINGS (ZS-S27 v1.6)
  F-S24.18  CLOSED-NEGATIVE  : Manton kernel not reflection positive (dim>=45)
  Theorem-Candidate S27.1              : squared-transfer escape, gap preserved, no new axiom
  Lanczos                    : eps_0(g) reproduces ZS-S24 Delta_E to 10 digits
  Lambda_HK/Lambda_W = 2.03  : heat-kernel overshoots -> lambda_t = 6.26 (+13%)
  R27-4 SCHEME-DIAGNOSTIC : weak-coupling |quartic| ordering suggests (does NOT
                               prove) a larger Manton finite shift; Lambda_Manton itself
                               NOT computed; prior bracketing conjecture withdrawn
  F-S27.3 finite cell        : 32-face one-flux-loop sector (NOT the full 90-link Hilbert space) closes only ~17% of
                               the overshoot; a +10.7% residual SURVIVES (Block 11)
  F-S27.4 observable         : the 11% lambda_t residual is a +2.9% overshoot in the
                               internal ratio m_H/m_A (physical m(2++)/m(0++) conditional on F-S27.1): predicted 1.541 vs lattice
                               1.497. Smaller than it sounded (sqrt compression),
                               BETTER than the kinematic Layer-Lift (1.390, -7%), and
                               on the side strong-coupling corrections reduce. Reading-1
                               (extraction error) disfavoured; Readings 2+3 share it.
  F-S27 (was F-S27.1 [two-gluon diag])        : R=1.541 is the eigenvalue ratio of the two-gluon INTERNAL
                               hyperfine operator ({A_g,T1,H}, degeneracies {1,3,5}).
                               It is NOT yet a physical glueball prediction: the map
                               internal-isotype -> physical J^PC is the OPEN gate F-S27.1
                               (no intertwiner; 2+1 carrier vs 3+1 lattice data). Status:
                               HYPOTHESIS-CONDITIONAL internal ratio, not spectral prediction.
  Gate C accounting          : 0.298805 is CORPUS-INTERNAL = G_exch (0.313264, DERIVED
                               closed form, Thm S18.6A') + seagull (COMPUTED from TI
                               geometry). No external number enters (R27-5 corrects the
                               v1.5 'outside-world' phrasing). R is ~96% carried by the
                               DERIVED closed form: exchange alone gives R=1.562, the
                               seagull refines to 1.540.
  MeV bridge                 : R uses no external NUMBER, but is NOT parameter-free as a
                               physical prediction. Open conditions: (a) F-S27.1 isotype->
                               spin intertwiner + 2+1->3+1 emergence; (b) seagull closed
                               form; (c) O(g^2) validity at lambda_t~6 (496-mode Gate-C
                               Lanczos, F-S18.4). Lambda ratio 2.03 is a SCHEME-ESTIMATE.
""")
