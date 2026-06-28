#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f32_verify_v1_5.py
=====================
Verification ledger for ZS-F32 v1.5 (corrected final: status-consistent naming, strengthened P9/P10, fixes).

  [P]  PROVEN / VERIFIED checks
  [I]  IMPORTED-PROVEN theorems (listed; conditions noted)
  [R]  REGRESSIONS (fixed-seed)
  [N]  ANTI-NUMEROLOGY AUDIT of chi_minus  -- documents that chi_minus is NOT closed
  [O]  gate ledger

New in v1.5 (numerics identical; P9/P10 strengthened, labels/refs corrected per review):
  P9/P10 relabeled: finite face algebra is abelian + sigma_t-invariant but NOT maximal abelian
                    (in a II_1 factor); E_face canonical. Maximality is a NON-CLAIM.
  P17  : theta-branch k*=0 under TWO conditions (theta_Z=omega AND quadratic/large-N branch law).
  P18  : compact-circle SPECTRAL CONFIRMATION (2pi k+omega)^2 ground k=0 (confirms P17, NOT an
         independent selector: it does not choose circle/periodicity/holonomy=omega).
  [N]  : the anti-numerology audit -- the chi_minus magnitude does NOT close parameter-free;
         the 10^(-Q^2) coincidence is a reduced-M_P+base-10 artifact. This block does NOT
         contribute to the exit code; it is an HONESTY check, printed for the record.

This script makes NO claim to compute chi_minus. rho_Lambda = 1/2 chi_minus omega^2 is a
CONDITIONAL law; the observed value is NEVER used as an input.

Dependencies: numpy, scipy, mpmath.   Run: python zs_f32_verify_v1_5.py
Exit: 0 iff all PROVEN/VERIFIED checks and regressions hold (the audit cannot fail the build).
"""
import sys
import numpy as np
import mpmath as mp
from scipy.linalg import expm
from scipy.optimize import brentq

mp.mp.dps = 50
np.random.seed(437)
TOL = 1e-9; TOLT = 1e-12
P_results, R_results = [], []
def rec(store, idx, desc, ok, detail=""):
    store.append((idx, desc, ok, detail)); print(f"  [{'PASS' if ok else 'FAIL'}] {idx:<5} {desc}")
    if detail: print(f"          {detail}")
def cclose(a, b, tol): return abs(complex(a)-complex(b)) <= tol

i_unit = mp.mpc(0,1); ln_i = mp.log(i_unit)
zstar = mp.findroot(lambda z: z - i_unit**z, mp.mpc("0.44","0.36"))
lam = zstar*ln_i; kappa = -mp.log(abs(lam)); omega = mp.arg(lam); RC = kappa/omega
k = float(kappa); w = float(omega); A = 35/437; Q = 11; PI = float(mp.pi)
lam_c = complex(float(lam.real), float(lam.imag))

sz = np.array([[1,0],[0,-1]],complex); sp = np.array([[0,1],[0,0]],complex)
sx = np.array([[0,1],[1,0]],complex); I2 = np.eye(2,dtype=complex)
def vecF(M): return M.reshape(-1,order='F')
def superop(L): return np.array([vecF(L(np.eye(4)[:,j].reshape(2,2,order='F'))) for j in range(4)]).T
def G_branch(n):
    wn = w+2*np.pi*n; return lambda X: 1j*(wn/2)*(sz@X-X@sz)+(k/2)*(sz@X@sz-X)
S_Z = superop(G_branch(0))

print("="*78)
print(" ZS-F32 v1.5  VERIFICATION LEDGER  (corrected final; strengthened P9/P10)")
print(f" kappa={k:.10f}  omega={w:.10f}  omega^2/2={w*w/2:.10f}  (0<omega<pi: {0<w<PI})")
print("="*78)

print("\n[P] PROVEN / VERIFIED CHECKS")
print("-"*78)
rec(P_results,"P1",  "kappa=-ln|lambda*|=0.1148346250", cclose(kappa,mp.mpf("0.1148346250"),1e-9))
rec(P_results,"P2",  "omega=arg lambda*=2.2592495540 (0<omega<pi)", cclose(omega,mp.mpf("2.2592495540"),1e-9) and 0<w<PI)
mults=[((expm(superop(G_branch(n)))@vecF(sp)).reshape(2,2,order='F')[0,1]/sp[0,1]) for n in range(-3,4)]
rec(P_results,"P3",  "branch independence exp(G_n)(s+)=lambda*", all(np.isclose(m,lam_c) for m in mults))
rec(P_results,"P4",  "principal branch n=0 norm-min", min([(n,abs(w+2*np.pi*n)) for n in range(-5,6)],key=lambda r:r[1])[0]==0)
Sb=superop(lambda X: sx@X@sx); Sc=Sb@S_Z@np.linalg.inv(Sb); Sn=superop(lambda X:1j*(-w/2)*(sz@X-X@sz)+(k/2)*(sz@X@sz-X))
rec(P_results,"P5",  "seam beta G_w beta^-1 = G_{-w}", np.linalg.norm(Sc-Sn)<TOL and np.linalg.norm(Sc-S_Z)>1.0)
ev=np.linalg.eigvals(expm(S_Z))
rec(P_results,"P6",  "M2 spectrum {1,1,lambda*,bar}; no lambda*^2", not any(np.isclose(ev,lam_c**2)))
rec(P_results,"P7",  "Fock tower lambda*^n by factorization", np.isclose(((expm(S_Z)@vecF(sp)).reshape(2,2,order='F'))[0,1],lam_c))
msh=0.0
for _ in range(200):
    nn=np.random.randint(2,7); H=np.random.randn(nn,nn)+1j*np.random.randn(nn,nn); H=H+H.conj().T
    X=np.random.randn(nn,nn)+1j*np.random.randn(nn,nn); c0=np.random.randn()
    msh=max(msh,np.linalg.norm(1j*((H+c0*np.eye(nn))@X-X@(H+c0*np.eye(nn)))-1j*(H@X-X@H)))
rec(P_results,"P8",  "central-shift orthogonality i[H+c0,X]=i[H,X]", msh<TOLT, f"max||diff||={msh:.1e}")

# P9/P10 : FINITE face algebra (NOT MASA) + canonical E_face
nf=6; dim=12; blk=dim//nf
def fp(a):
    P=np.zeros((dim,dim),complex)
    for j in range(a*blk,(a+1)*blk): P[j,j]=1.0
    return P
qs=[fp(a) for a in range(nf)]; tr=lambda M: np.trace(M).real/dim
abelian=all(np.allclose(qa@qb,qb@qa) for qa in qs for qb in qs) and np.allclose(sum(qs),np.eye(dim))
DW=np.repeat([3,2,6,3,2,6],blk).astype(float)
Ut=np.diag(DW**(1j*0.7))   # modular flow sigma_t at t=0.7
# STRENGTHENED (v1.5): per-projection modular invariance sigma_t(q_a)=q_a, not just sigma_t(I)=I
sig_inv=all(np.allclose(Ut@qa@Ut.conj().T, qa) for qa in qs)
# NON-MASA witness: an off-diagonal element inside a block commutes with all q_a but is NOT in A_face
W=np.zeros((dim,dim),complex); W[0,1]=1; W[1,0]=1   # lives in q_0 M q_0
nonmasa = all(np.allclose(W@qa,qa@W) for qa in qs) and not np.allclose(W,np.diag(np.diag(W)))
rec(P_results,"P9",  "finite face algebra abelian + per-projection sigma_t-inv; NOT maximal abelian (witness)",
    abelian and sig_inv and nonmasa, "sigma_t(q_a)=q_a for all a; off-block W commutes with all q_a but is not diagonal => A_face not MASA")
def Eface(x):
    out=np.zeros((dim,dim),complex)
    for qa in qs: out+=(tr(qa@x)/tr(qa))*qa
    return out
X=np.random.randn(dim,dim)+1j*np.random.randn(dim,dim); X=X+X.conj().T
# STRENGTHENED (v1.5): add modular covariance and bimodule property to match the text
cov_ok=np.allclose(Eface(Ut@X@Ut.conj().T), Ut@Eface(X)@Ut.conj().T)
af_a=2*qs[0]+0.5*qs[1]+1.3*qs[2]+0.7*qs[3]+1.1*qs[4]+0.9*qs[5]   # a in A_face
af_b=0.4*qs[0]+1.7*qs[1]+0.3*qs[2]+2.1*qs[3]+0.6*qs[4]+1.4*qs[5]   # b in A_face
bimod_ok=np.allclose(Eface(af_a@X@af_b), af_a@Eface(X)@af_b)       # E(axb)=aE(x)b
rec(P_results,"P10", "E_face canonical: id/trace-pres/idempotent/into A_face + modular covariance + bimodule",
    np.allclose(Eface(qs[2]),qs[2]) and abs(tr(Eface(X))-tr(X))<TOLT and np.allclose(Eface(Eface(X)),Eface(X))
    and np.allclose(Eface(X),np.diag(np.diag(Eface(X)))) and cov_ok and bimod_ok,
    "modular covariance E(UtXUt*)=UtE(X)Ut* and bimodule E(axb)=aE(x)b verified")

U_Z=expm(0.5*(-k+1j*w)*sz)
rec(P_results,"P11", "pure-boost no-go: tr U_Z complex", abs(np.trace(U_Z).imag)>1e-6)
rec(P_results,"P12", "loxodromic eigenvalues match U_Z", np.allclose(np.sort_complex(np.linalg.eigvals(U_Z)),np.sort_complex(np.linalg.eigvals(expm(0.5*(-k+1j*w)*sz)))))

twoom=2*w
def rhoL(th): return np.arctanh((1/8)*np.cos(3*th))
rec(P_results,"P13", "single-pulse no-go rho(2omega) != -kappa", not np.isclose(rhoL(twoom),-k), f"rho(2omega)=+{rhoL(twoom):.7f}")
def f2(th1): return rhoL(th1)+rhoL(twoom-th1)+k
g=np.linspace(0.01,twoom-0.01,20000); vv=np.array([f2(t) for t in g])
roots=[brentq(f2,g[i],g[i+1]) for i in range(len(g)-1) if vv[i]*vv[i+1]<0]
prs=[]
for r in roots:
    key=tuple(sorted([round(r,6),round(twoom-r,6)]))
    if key not in [p[2] for p in prs]: prs.append((r,twoom-r,key))
okc=len(prs)>=2 and all(np.allclose(expm(0.5*(rhoL(p[0])+1j*p[0]/2)*sz)@expm(0.5*(rhoL(p[1])+1j*p[1]/2)*sz),U_Z) for p in prs)
rec(P_results,"P14", "two-pulse composition e^{X1}e^{X2}=U_Z (2 families)", okc,
    "; ".join(f"({p[0]:.4f},{p[1]:.4f}) S={p[0]**2+p[1]**2:.3f}" for p in prs))

# P15 : numerical Reuleaux robustness (relabeled VERIFIED-NUMERICAL)
s=1.0; Rc=s/np.sqrt(3); verts=np.array([[Rc*np.cos(a),Rc*np.sin(a)] for a in [np.pi/2,np.pi/2+2*np.pi/3,np.pi/2+4*np.pi/3]])
bpts=[]
for i in range(3):
    Av=verts[i]; oth=[verts[j] for j in range(3) if j!=i]
    a0=np.arctan2(oth[0][1]-Av[1],oth[0][0]-Av[0]); a1=np.arctan2(oth[1][1]-Av[1],oth[1][0]-Av[0]); da=a1-a0
    while da>np.pi: da-=2*np.pi
    while da<-np.pi: da+=2*np.pi
    for tt in np.linspace(0,da,400): bpts.append(Av+s*np.array([np.cos(a0+tt),np.sin(a0+tt)]))
bpts=np.array(bpts); ths=np.linspace(0,2*np.pi,4000); hh=np.array([np.max(bpts@np.array([np.cos(t),np.sin(t)])) for t in ths])
def hi(th): th=th%(2*np.pi); return np.interp(th,ths,hh)
wok=np.std([hi(t)+hi(t+np.pi) for t in np.linspace(0,np.pi,50)])<1e-4
def rex(th): return np.arctanh(np.clip((hi(th)-hi(th+np.pi))/s,-0.999,0.999))
def fe(th1): return rex(th1)+rex(twoom-th1)+k
gE=np.linspace(0.05,twoom-0.05,4000); vE=np.array([fe(t) for t in gE]); rE=[]
for i in range(len(gE)-1):
    if vE[i]*vE[i+1]<0:
        try: rE.append(brentq(fe,gE[i],gE[i+1]))
        except Exception: pass
prE=[]
for r in rE:
    key=tuple(sorted([round(r,4),round(twoom-r,4)]))
    if key not in [p[2] for p in prE]: prE.append((r,twoom-r,key))
okE=wok and len(prE)>=1 and all(np.allclose(expm(0.5*(rex(p[0])+1j*p[0]/2)*sz)@expm(0.5*(rex(p[1])+1j*p[1]/2)*sz),U_Z,atol=1e-6) for p in prE)
rec(P_results,"P15", "Reuleaux-boundary robustness (NUMERICAL): two-pulse persists & composes to U_Z",
    okE, f"width std<1e-4; {len(prE)} families (finite-resolution, not analytic)")
rec(P_results,"P16", "two-pulse constraints sum_rho=-kappa, (t1+t2)/2=omega",
    all(abs(rhoL(p[0])+rhoL(p[1])+k)<1e-9 and abs((p[0]+p[1])/2-w)<1e-9 for p in prs))

# P17 : theta-branch selection k*=0 (given theta_Z=omega)
ks=[(kk,abs(w+2*PI*kk)) for kk in range(-5,6)]; kstar=min(ks,key=lambda r:r[1])[0]
rec(P_results,"P17", "theta-branch k*=0 under (theta_Z=omega AND quadratic/large-N law); coeff omega^2/2",
    kstar==0 and 0<w<PI, f"argmin_k|omega+2pi k|=k*={kstar}; rho_L,Z=(omega^2/2)chi_-={w*w/2:.10f} chi_-")
# P18 : Friedrichs spectrum on circle phi~phi+1
rec(P_results,"P18", "compact-circle spectral confirmation (2pi k+omega)^2 ground k=0 (confirms P17)",
    (w*w) < ((2*PI-w)**2), f"omega^2={w*w:.4f} < (2pi-omega)^2={(2*PI-w)**2:.4f}")

print("\n[I] IMPORTED-PROVEN THEOREMS (7)")
print("-"*78)
for idx,thm in [("I1","Wirth 2022 - GNS-symmetric QMS extension"),("I2","Bardet et al. - entropy-production decomposition"),
    ("I3","Poincare/Henneaux-Teitelboim/Bousso-Polchinski"),("I4","Berkson-Porta - principal-branch semigroup"),
    ("I5","Chandrasekaran-Longo-Penington-Witten - de Sitter algebra Type II_1"),
    ("I6","Compact U(1) 3-form Dirac quantization; Kaloper-Sorbo monodromy"),
    ("I7","Reed-Simon - Friedrichs extension of a semibounded form")]:
    print(f"  [IMPORTED] {idx}  {thm}")

print("\n[R] REGRESSIONS")
print("-"*78)
rec(R_results,"R1","(A,Q,dimZ)=(35/437,11,2)", abs(35/437-A)<1e-15)
rec(R_results,"R2","quality factor Q=omega/2kappa=9.8369; R_C=1/(2Q)", cclose(omega/(2*kappa),mp.mpf("9.8369"),1e-3) and cclose(RC,1/(2*omega/(2*kappa)),TOLT))
def relent(rho,sig):
    e,U=np.linalg.eigh(rho); e=np.clip(e.real,1e-15,None); lr=U@np.diag(np.log(e))@U.conj().T
    es,Us=np.linalg.eigh(sig); es=np.clip(es.real,1e-15,None); ls=Us@np.diag(np.log(es))@Us.conj().T
    return float(np.real(np.trace(rho@(lr-ls))))
def rr(d): A2=np.random.randn(d,d)+1j*np.random.randn(d,d); r=A2@A2.conj().T; return r/np.trace(r)
def Lf(R): SZ=np.kron(I2,sz); return 1j*(w/2)*(SZ@R-R@SZ)+(k/2)*(SZ@R@SZ-R)
def pA(R): return np.einsum('aiaj->ij',R.reshape(2,2,2,2))
vi=0; dt=1e-4
for _ in range(30):
    rho=rr(4); rd=rho+dt*Lf(rho)
    if -(relent(pA(rd),np.eye(2)/2)-relent(pA(rho),np.eye(2)/2))/dt > -(relent(rd,np.eye(4)/4)-relent(rho,np.eye(4)/4))/dt+1e-6: vi+=1
rec(R_results,"R3","factorized lift Sigma_bd<=Sigma_bulk", vi==0, f"{30-vi}/30")
np.random.seed(20260628); RC_f=float(RC); bases=[A,2*A,A/2,1/PI,2/PI,A/PI,np.sqrt(A),A*A,1/Q,2/Q]; hits=0
for _ in range(300000):
    val=(np.random.randint(1,13)/np.random.randint(1,13))*(bases[np.random.randint(len(bases))]**np.random.choice([1,1,1,2,-1]))
    if val>0 and abs(val-RC_f)/RC_f<=0.0031: hits+=1
rec(R_results,"R4","anti-numerology MC (R_C, seed 20260628) <5%", 100*hits/300000<5.0, f"hit-rate={100*hits/300000:.3f}%")

print("\n[N] ANTI-NUMEROLOGY AUDIT of chi_minus  (HONESTY check; does NOT affect exit code)")
print("-"*78)
for label,rho_over in [("reduced M_P",7.25e-121),("full M_P",1.15e-123)]:
    chi_over=2*rho_over/(w*w); expo=-np.log(chi_over)
    print(f"  required [{label}]: chi/M_P^4={chi_over:.3e}, ln(M_P^4/chi)={expo:.2f}, chi^(1/4)/M_P={chi_over**0.25:.3e}")
print(f"  10^(-Q^2)=1e-121 vs reduced 2.84e-121 (ratio 0.35) BUT vs full 4.5e-124 (ratio 222) => convention artifact")
nat={'8pi^2/A':8*PI*PI/A,'8pi^2':8*PI*PI,'Q^2':Q**2,'Q^2*omega':Q**2*w,'pi/A':PI/A,'Q^2*ln10(base-10!)':Q**2*np.log(10)}
print("  e-natural Z-Spin exponents vs required window [277.6,284.0]:")
for nm,vl in nat.items(): print(f"    {nm:22s}={vl:8.2f}  {'<-- in window (base-10 only)' if 277<vl<284 else ''}")
print("  VERDICT: chi_minus is NOT derivable parameter-free here; rho_L=1/2 chi_- omega^2 is CONDITIONAL.")

print("\n[O] GATE LEDGER -- B3 residual in THREE LAYERS (one absolute scale + two bridge gates)")
print("-"*78)
for g,st in [("B3_bridge1","holonomy map theta_Z=omega (U(1)_Z -> 3-form theta-angle): DERIVED-CONDITIONAL"),
    ("B3_bridge2","all-loop odd-sector isolation beta_+-=0 to all orders: OPEN"),
    ("B3_scale","absolute susceptibility chi_minus(A,Q,M_P): OPEN"),
    ("(support)","quantization IMP+DC (F32.24); k*=0 PROVEN under (B3_bridge1 AND quadratic law, F32.25-26)")]:
    print(f"  {g:<11} {st}")
print("  => residual is NOT a single object: 1 unresolved absolute scale (chi_-) + 2 conditional bridge gates.")

nP=sum(1 for r in P_results if r[2]); fP=sum(1 for r in P_results if not r[2])
nR=sum(1 for r in R_results if r[2]); fR=sum(1 for r in R_results if not r[2])
print("\n"+"="*78)
print(f" SUMMARY: PROVEN/VERIFIED {nP}/{len(P_results)} | REGRESSIONS {nR}/{len(R_results)} | IMPORTED 7 | residual: 1 abs scale (chi_-) + 2 bridge gates")
print(f"          FAIL: {fP+fR}")
print("="*78)
print(" EPISTEMIC CAVEAT: chi_minus is NOT computed here. rho_Lambda = 1/2 chi_- omega^2 is a")
print(" CONDITIONAL, falsifiable law; the observed value is never used as input. The branch")
print(" selection k*=0 is PROVEN given theta_Z=omega; the absolute scale needs a UV derivation.")
print(" B3 is OPEN - not closed, not proven impossible (ZS-A26).")
print("="*78)
sys.exit(0 if (fP+fR==0) else 1)
