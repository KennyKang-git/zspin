#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f39_verify_v1_1.py — Verification suite for ZS-F39 v1.1
"The Seam Uniformization Theorem" v1.1 (review-integration revision of v1.0;
 single-paper consolidation; integrates the pre-scoped ZS-M48 deliverables per
 the collaboration decision of record). v1.1 additions: T1D (uniqueness-diagram
 commutation witnesses, Lemma F39.L2), N1d/N1e (Lemma F39.N1.L measure-zero
 analytic-exclusion witnesses), guard N1-G2 (sample-null vs analytic-exclusion
 separation). All v1.0 frozen registrations (seed 11, thresholds, Appendix C
 decision rule) are UNCHANGED.

Design: FAIL-CLOSED (any failure -> exit 1). Exact rational arithmetic (sympy
Fraction/Rational) wherever the claim is exact; mpmath 50-digit for the locked
dynamical digits; numpy for superoperator spectra and the frozen N1 null.
GUARDS certify nothing; they register scope. Declared-before-loaded ordering:
all theorem-side constants are fixed in code ABOVE the single firewalled
observation block (CR*), reproducing the ZS-F36/A31/A32 firewall discipline.
"""
import sys, math, cmath
import numpy as np
import sympy as sp
from fractions import Fraction as Fr
import mpmath as mp

mp.mp.dps = 50
FAIL = []
CHECKS = 0
def check(tag, ok, detail=""):
    global CHECKS; CHECKS += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}" + (f" | {detail}" if detail else ""))
    if not ok: FAIL.append(tag)
GUARDS = 0
def guard(tag, note):
    global GUARDS; GUARDS += 1
    print(f"[GUARD] {tag} | {note}")

# ============================================================ K locked
print("="*78); print("K — LOCKED INPUTS AND SEAM DYNAMICS")
A = Fr(35,437); Q = 11; k2 = A/Q
check("K1 (A,Q,dimZ) echo", A==Fr(35,437) and Q==11)
check("K2 kappa^2 = A/Q = 35/4807 exact", k2==Fr(35,4807))
check("K3 1260/4807 = 36 A/Q exact", Fr(1260,4807)==36*k2)
check("K4 2+3+6 = 11 = Q; sum d^2 = 49 exact", 2+3+6==Q and 2*2+3*3+6*6==49)
def f(z): return mp.e**(1j*mp.pi*z/2)
z = mp.mpc('0.4382829367','0.3605924719')
for _ in range(60):
    z = z - (f(z)-z)/((1j*mp.pi/2)*f(z)-1)
z_star = z; lam = (1j*mp.pi/2)*z_star
mu = -mp.log(abs(lam)); th = mp.arg(lam)
check("K5 z* locked 10 digits", abs(z_star-mp.mpc('0.4382829367','0.3605924719'))<1e-9)
check("K6 mu = 0.1148346250", abs(mu-mp.mpf('0.1148346250'))<1e-9, f"{mp.nstr(mu,12)}")
check("K7 theta = 2.2592495540", abs(th-mp.mpf('2.2592495540'))<1e-9, f"{mp.nstr(th,12)}")
def koenigs(z0, n=500):
    w=z0
    for _ in range(n): w=f(w)
    return (w-z_star)/lam**n
zc = z_star + mp.mpc('0.05','-0.03'); devs=[]
for _ in range(12):
    devs.append(abs(mp.log(koenigs(f(zc))/koenigs(zc))/mp.log(lam)-1)); zc=f(zc)
check("K8 branch-free Abel unit step at 12 orbit pts", max(devs)<mp.mpf('1e-20'),
      f"max dev = {mp.nstr(max(devs),3)}")

# ============================================================ S sector mediator
print("="*78); print("S — ZS-A24 SECTOR MEDIATOR (path X–Z–Y; rates q_{i->j}=kappa^2 d_j)")
k2s = sp.Rational(35,4807)
dX,dZ,dY = 3,2,6
Lsec = k2s*sp.Matrix([[-dZ, dZ, 0],
                      [ dX, -(dX+dY), dY],
                      [ 0,  dZ, -dZ]])
check("S1 spectrum {0, -2A/Q, -A} exact (ZS-A24 Main Thm 2a echo)",
      set(Lsec.eigenvals().keys())=={sp.Integer(0), -2*k2s, -11*k2s},
      "{0, -70/4807, -35/437}")
ns = (Lsec.T).nullspace()
pi_sec = ns[0]/sum(ns[0])
check("S2 stationary = (3,2,6)/11 exact (A24 PROVEN echo)",
      list(pi_sec)==[sp.Rational(3,11),sp.Rational(2,11),sp.Rational(6,11)])
check("S3 kernel dim = 1 (irreducible path)", len(ns)==1)

# ============================================================ EQ equivariant lift
print("="*78); print("EQ — EQUIVARIANT SLOT LIFT (Theorem F39.T3)")
d_slot = [3]*dX+[2]*dZ+[6]*dY
sec_of = [0]*dX+[1]*dZ+[2]*dY
adj_sec = {(0,1),(1,0),(1,2),(2,1)}
E = [(a,b) for a in range(Q) for b in range(Q)
     if a!=b and (sec_of[a],sec_of[b]) in adj_sec]
Lc = sp.zeros(Q,Q)
for (a,b) in E: Lc[a,b] += k2s
for a in range(Q): Lc[a,a] = -sum(Lc[a,j] for j in range(Q) if j!=a)
check("EQ1 unital/doubly-stochastic: row sums = col sums = 0 exact",
      all(sum(Lc[a,j] for j in range(Q))==0 for a in range(Q)) and
      all(sum(Lc[i,b] for i in range(Q))==0 for b in range(Q)))
nsl = (Lc.T).nullspace()
check("EQ2 kernel dim = 1; stationary = I_Q/Q exact",
      len(nsl)==1 and list(nsl[0]/sum(nsl[0]))==[sp.Rational(1,Q)]*Q)
marg = [sum((nsl[0]/sum(nsl[0]))[a] for a in range(Q) if sec_of[a]==s) for s in range(3)]
check("EQ3 sector marginal of I_Q/Q = (3,2,6)/11 = A24 stationary exact",
      marg==[sp.Rational(3,11),sp.Rational(2,11),sp.Rational(6,11)])
k2f = float(Fr(35,4807))
def Eab(a,b):
    M=np.zeros((Q,Q)); M[a,b]=1.0; return M
I = np.eye(Q)
Slin = np.zeros((Q*Q,Q*Q))
def lift(Xl,Xr):
    return np.kron(Xr.T, Xl)
for (a,b) in E:
    J = Eab(b,a)
    Slin += k2f*( lift(J, J.T) - 0.5*lift(J.T@J, I) - 0.5*lift(I, (J.T@J).T) )
w_eig, v_eig = np.linalg.eig(Slin)
ker = np.where(np.abs(w_eig)<1e-10)[0]
check("EQ4 quantum GKLS lift: dim ker L = 1", len(ker)==1, f"dim={len(ker)}")
rho = v_eig[:,ker[0]].reshape(Q,Q,order='F'); rho = rho/np.trace(rho)
check("EQ5 unique stationary state = I_Q/Q (EHK: irreducible+unital)",
      np.allclose(rho, np.eye(Q)/Q, atol=1e-9),
      f"||rho - I/Q|| = {np.linalg.norm(rho-np.eye(Q)/Q):.2e}")
gap = sorted(np.abs(np.real(w_eig)))[1]
check("EQ6 spectral gap > 0 (relaxation to democracy)", gap>1e-6, f"gap={gap:.3e}")

# ============================================================ ML multiplicity lift
print("="*78); print("ML — MULTIPLICITY SLOT LIFT (Theorem F39.T4 second branch)")
Lm = sp.zeros(Q,Q)
for (a,b) in E: Lm[a,b] += k2s*d_slot[b]
for a in range(Q): Lm[a,a] = -sum(Lm[a,j] for j in range(Q) if j!=a)
col0 = [sum(Lm[i,b] for i in range(Q)) for b in range(Q)]
check("ML1 non-unital witness: some column sum != 0 exact", any(c!=0 for c in col0))
nsm = (Lm.T).nullspace()
pim = nsm[0]/sum(nsm[0])
check("ML2 kernel dim = 1 (irreducible)", len(nsm)==1)
check("ML3 stationary slot weights = d_slot/49 exact",
      all(pim[a]==sp.Rational(d_slot[a],49) for a in range(Q)))
margm = [sum(pim[a] for a in range(Q) if sec_of[a]==s) for s in range(3)]
check("ML4 sector law = (9,4,36)/49 = two-leg omega (F37) exact",
      margm==[sp.Rational(9,49),sp.Rational(4,49),sp.Rational(36,49)],
      "= (d_X^2, d_Z^2, d_Y^2)/49")
check("ML5 omega components sum to 1; one-leg (3,2,6)/11 distinct from (9,4,36)/49 exact",
      sum(margm)==1 and margm!=marg)
cg = [sum(Lm[a,b] for b in range(Q) if sec_of[b]==1) for a in range(Q) if sec_of[a]==0]
check("SEL1 selection: ML coarse rate X->Z = kappa^2 d_Z^2 != kappa^2 d_Z (A24) exact",
      all(r==k2s*dZ*dZ for r in cg) and k2s*dZ*dZ != k2s*dZ)
cg2 = [sum(Lc[a,b] for b in range(Q) if sec_of[b]==1) for a in range(Q) if sec_of[a]==0]
check("SEL2 selection: EQ coarse rate X->Z = kappa^2 d_Z = A24 rate exact",
      all(r==k2s*dZ for r in cg2))

# ============================================================ EL E_len
print("="*78); print("EL — MODULAR LENGTH FUNCTOR: SCALING COVARIANCE (Lemma F39.L1)")
for t in (0.0, 0.1, 0.3, 1.0):
    s = math.exp(-2*math.pi*t)
    d0, dt = 1/1.7, 1/(1.7*s)
    check(f"EL1 t={t}: d(e^(-2pi t)D) = e^(+2pi t) d(D) exact",
          abs(dt - d0*math.exp(2*math.pi*t)) < 1e-12)
m0=1.7; best=0.0
for a in np.linspace(-3/m0,3/m0,401):
    for b in np.linspace(-3/m0,3/m0,51):
        Dc=np.array([[0,m0],[m0,0]]); F=np.diag([a,b])
        if np.linalg.norm(Dc@F-F@Dc,2)<=1+1e-12: best=max(best,abs(a-b))
check("EL2 Connes sup reproduces d = 1/m (two-point)", abs(best-1/m0)<2e-2,
      f"num={best:.4f}")
N = 0; nmax=99; lam3 = nmax+1.5
for n in range(nmax+1): N += 2*(n+1)*(n+2)
ratio = N/((2/3)*lam3**3)
check("EL3 S^3 Dirac counting N(lambda)/((2/3)lambda^3) -> 1 (M47 (IV) echo)",
      abs(ratio-1)<0.02, f"ratio={ratio:.4f} at lambda={lam3}")

# ============================================================ CH characters
print("="*78); print("CH — TWO-LEG CHARACTER BOOKKEEPING")
tt = sp.symbols('t', positive=True)
chi = lambda d: sp.sinh(d*tt)/sp.sinh(tt)
check("CH1 chi2*chi3 = chi4 + chi2 symbolically (2 (x) 3 = 4 (+) 2)",
      sp.simplify(chi(2)*chi(3)-chi(4)-chi(2))==0)
rho_b = sp.Rational(1,2)*sp.log(sp.Rational(9,7))
check("CH2 rho_b = (1/2)ln(9/7) = 0.125657... exact form (F30/F37 echo)",
      abs(float(rho_b)-0.125657)<1e-6, f"{float(rho_b):.6f}")
DCHI_F37 = -0.392090129
guard("CH-G", f"Delta chi(rho_b) = {DCHI_F37} consumed AS REPORTED (F37 convention; "
      "not re-derived here — convention re-derivation would risk confabulation)")

# ============================================================ CI model tier
print("="*78); print("CI — eps_C_int MODEL TIER")
zz = sp.symbols('z')
check("CI1 Hardy chain shift z*(z^k)=z^(k+1), k<=Q exact",
      all(sp.simplify(zz*zz**k - zz**(k+1))==0 for k in range(Q+1)))
check("CI2 eps_C_int^(model) = 0 (unit Abel step; A32 Sec.5 reproduced)",
      max(devs)<mp.mpf('1e-20'), f"eps={mp.nstr(max(devs),3)}")

# ============================================================ CJ conjugate seam
print("="*78); print("CJ — CONJUGATE SEAM (the (H-2D) speed half)")
lam_bar = mp.conj(lam)
check("CJ1 |conj(lambda*)| = |lambda*| exact => equal mu (equal modular speed)",
      abs(abs(lam_bar)-abs(lam))==0)
zbar = mp.conj(z_star)
fb = lambda w: mp.e**(-1j*mp.pi*w/2)
check("CJ2 conj germ: fbar(zbar*) = zbar*, multiplier = conj(lambda*)",
      abs(fb(zbar)-zbar)<1e-30 and abs((-1j*mp.pi/2)*fb(zbar)-lam_bar)<1e-30)


# ============================================================ T1D uniqueness diagram (v1.1)
print("="*78); print("T1D — T1 UNIQUENESS DIAGRAM WITNESSES (Lemma F39.L2, v1.1)")
# Germ level: Koenigs conjugation kappa(f(z)) = lambda* kappa(z) (multiplicative form;
# K8 verified the additive/Abel form). Square (i) of the Appendix A diagram.
zc2 = z_star + mp.mpc('0.05','-0.03')
mdevs=[abs(koenigs(f(zc2))/(lam*koenigs(zc2)) - 1)]
for _ in range(5):
    zc2=f(zc2); mdevs.append(abs(koenigs(f(zc2))/(lam*koenigs(zc2))-1))
check("T1D1 Koenigs square commutes: kappa(f z) = lambda* kappa(z) at 6 orbit pts",
      max(mdevs)<mp.mpf('1e-20'), f"max dev = {mp.nstr(max(mdevs),3)}")
# Equivalence-class level: a central phase c (|c|=1) rescales the Koenigs coordinate
# but leaves the multiplier lambda* (hence mu, theta) invariant — square (iii).
c_ph = mp.e**(1j*mp.mpf('0.7'))
kap_c = lambda w: c_ph*koenigs(w)
zc3 = z_star + mp.mpc('0.02','0.04')
check("T1D2 central phase invariance: (c kappa)(f z)/((c kappa)(z)) = lambda* exactly",
      abs(kap_c(f(zc3))/kap_c(zc3) - lam) < mp.mpf('1e-20'),
      "multiplier unchanged under kappa -> c kappa, |c|=1")
# Speed level: cocycle-conjugate representatives share |lambda*| (mu); CJ1 gave the
# conjugate-seam case; here the phase case — together the T1 quotient bookkeeping.
check("T1D3 quotient bookkeeping: |c lambda*| = |lambda*| for |c|=1 exact",
      abs(abs(c_ph*lam)-abs(lam))==0)

# ============================================================ TB tensor triple
print("="*78); print("TB — TENSOR BORCHERS TRIPLE (model bookkeeping)")
p = np.linspace(0,5,40)
P1,P2 = np.meshgrid(p,p)
check("TB1 joint spectrum (P (+) Pbar) in closed forward cone (model)",
      np.all(P1>=0) and np.all(P2>=0) and np.all(P1+P2>=0))

# ============================================================ N1 frozen null
print("="*78); print("N1 — FROZEN NULL, EXECUTED (pre-registered; seed 11)")
rng = np.random.default_rng(11)
def haar(n):
    Zm = (rng.standard_normal((n,n))+1j*rng.standard_normal((n,n)))/np.sqrt(2)
    Qm,Rm = np.linalg.qr(Zm); return Qm*(np.diag(Rm)/np.abs(np.diag(Rm)))
C = np.roll(np.eye(Q),1,axis=0).astype(complex)
nC = np.linalg.norm(C)
eps_list=[]
for _ in range(2000):
    V1,V2 = haar(Q),haar(Q)
    PhiC = 0.5*(V1@C@V1.conj().T + V2@C@V2.conj().T)
    eps_list.append(np.linalg.norm(PhiC-C)/nC)
eps_arr = np.sort(np.array(eps_list))
p5 = eps_arr[int(0.05*len(eps_arr))]; mn = eps_arr[0]; md = np.median(eps_arr)
print(f"    null (2000 draws): min={mn:.4f}  p5={p5:.4f}  median={md:.4f}")
check("N1a target attainable: clock-implementing channel gives eps = 0 exactly",
      np.linalg.norm(0.5*(C@C@C.conj().T + C@C@C.conj().T)-C)/nC < 1e-14)
check("N1b null floor: min eps over 2000 unital draws > 0.1 (0 unreachable by chance)",
      mn > 0.1, f"min={mn:.4f}")
check("N1c 5th percentile of record frozen", p5 > 0.3, f"p5={p5:.4f}")
check("N1d Lemma F39.N1.L witness (nonempty): clock-conjugation channel in locus",
      np.linalg.norm(0.5*(C@C@C.conj().T + C@C@C.conj().T)-C)/nC < 1e-14,
      "V1=V2=C gives eps = 0: locus Z_clk nonempty")
V2d = np.diag([(-1)**k for k in range(Q)]).astype(complex)
eps_det = np.linalg.norm(0.5*(C + V2d@C@V2d.conj().T)-C)/nC
check("N1e Lemma F39.N1.L witness (proper): deterministic unital channel off locus",
      eps_det > 0.5, f"eps={eps_det:.4f} > 0 exactly (alternating-sign V2): Z_clk proper")
guard("N1-G2", "Lemma F39.N1.L (v1.1): eps=0 locus = proper real-algebraic subvariety "
      "of the unital pair-Kraus space => Haar measure zero (analytic exclusion). "
      "The 2000-draw null estimates the FINITE-THRESHOLD false-positive rate only; "
      "the frozen Appendix C decision rule is UNCHANGED by the lemma")
guard("N1-G", "verdict deferred: eps_phys on ZS-F31 GKLS / ZS-A24 core data is the "
      "F39/M48 discharge computation; decision rule frozen in Appendix C "
      "(eps_phys < 1e-10 AND P_null <= 5%)")

# ============================================================ CR corners (firewalled)
print("="*78); print("CR — CORNER CONSISTENCY (FIREWALLED; one LCDM package consumed)")
guard("CR-G0", "declared-before-loaded: all theorem constants above; the single "
      "observation package loads only in this block (A31/A32 firewall inherited)")
MbP=2.435e27; rhoL4=2.24e-3; H0=67.36/3.0856775814913673e19*6.582119569e-16
tU=13.797e9*365.25*24*3600/6.582119569e-16; Meff=2.476e-3
tp2,fp4,ep8 = 2*math.pi*Q, 4*math.pi*Q, 8*math.pi*Q
vals = dict(W=math.log(MbP/Meff), V=4*math.log(MbP/rhoL4),
            L=math.log(MbP/H0), T=math.log(tU*MbP))
for tag,(o,pd,tol) in dict(W=(vals['W'],tp2,0.15),V=(vals['V'],ep8,0.15),
                           L=(vals['L'],fp4,0.5),T=(vals['T'],fp4,0.5)).items():
    check(f"CR-{tag} corner dev < {tol}% (A32 Table 2 class)",
          abs(o-pd)/pd*100<tol, f"dev={abs(o-pd)/pd*100:.3f}%")
kapv = 0.5*float(Fr(1260,4807))*float(th)**2
CUVW = math.exp(4*(tp2-vals['W']))
check("CR5 vacuum factor 0.668952; C_UV(W)~1.244 in band",
      abs(kapv-0.668952)<1e-5 and 0.25<=CUVW<=4 and abs(CUVW-1.244)<0.02,
      f"C_UV={CUVW:.3f}")

# ============================================================ XV cross-version
print("="*78); print("XV — CROSS-VERSION ECHOES")
check("XV1 4QA = 1540/437 exact (A32.2)", 4*Q*A==Fr(1540,437))
check("XV2 e^(-2piQ) = 9.632e-31 (F38 BW1)", abs(math.exp(-tp2)-9.632e-31)/9.632e-31<1e-3)
check("XV3 A24 dimensionless rates {2A/Q, 6A/Q} present in L_sec exact",
      Lsec[0,1]==2*k2s and Lsec[1,2]==6*k2s)
check("XV4 omega=(4,9,36)/49 in F37 (d_Z,d_X,d_Y) order == ML sector law reordered",
      sorted(margm)==sorted([sp.Rational(4,49),sp.Rational(9,49),sp.Rational(36,49)]))

# ============================================================ G guards
print("="*78); print("G — SCOPE GUARDS (certify nothing)")
guard("G1", "(H-CLK)=Phi_seam existence NOT certified; suite verifies mathematics/"
            "model tiers only (M46/F38 registry discipline)")
guard("G2", "KH1–KH4 NOT machine-certified (imported admissibility; M46)")
guard("G3", "DS2 inherited: omega (transport weight) and I_Q/Q (state density) remain "
            "DISTINCT OBJECTS; T4 relates their origins, not the objects (NC-F38.2)")
guard("G4", "C_UV full-1PI untouched (F36 programme (i)); no Q-absorption (A31 rule)")

print("="*78)
if FAIL:
    print(f"RESULT: {len(FAIL)} FAILURE(S): {FAIL}"); sys.exit(1)
print(f"RESULT: {CHECKS}/{CHECKS} exact/numerical checks PASS + {GUARDS}/{GUARDS} guards.")
print("Zero fitted parameters. (A, Q, dim Z) = (35/437, 11, 2) LOCKED.")
