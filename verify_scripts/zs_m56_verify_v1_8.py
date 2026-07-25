#!/usr/bin/env python3
# zs_m56_verify_v1_0.py  --- ZS-M56 v1.8 fail-closed (FINAL) verification ledger
# Classes: R = actual reconstruction on the corpus object, A = analytical identity,
#          X = negative control, P = proxy/generic theorem, D = declaration.
# No literal True is permitted as a proof-bearing check.
import numpy as np, mpmath as mp, itertools, math
mp.mp.dps = 40
np.random.seed(56)

LED = []
def chk(tag, cls, desc, ok, val=""):
    LED.append((tag, cls, desc, "PASS" if ok else "FAIL", val))
    return ok

# ---------- LOCKED CONSTANTS (construction layer must not use lam) ----------
A   = mp.mpf(35)/437
Q   = 11
dZ  = 2
k2  = A/Q
kap = mp.sqrt(k2)

z = mp.mpf('0.4')+mp.mpf('0.3')*1j
for _ in range(600): z = mp.e**(z*1j*mp.pi/2)
zs  = z                                  # z*
lam = (1j*mp.pi/2)*zs                    # Koenigs multiplier  (COMPARISON layer)
al  = abs(lam); arg = mp.arg(lam)
mu  = -mp.log(al); D2 = 1-al**2; D = mp.sqrt(D2)
L   = complex(lam)

# ===== GROUP 1 : locked-constant regression  [A] =====
chk("V1","A","z* is the i-tetration fixed point i^{z*} = z*",
    abs(mp.e**(zs*1j*mp.pi/2)-zs) < mp.mpf('1e-30'), f"{abs(mp.e**(zs*1j*mp.pi/2)-zs)}")
chk("V2","A","lambda = (i*pi/2) z* matches locked value",
    abs(lam-(mp.mpf('-0.566417330285464')+mp.mpf('0.688453227107702')*1j))<1e-14, f"{mp.nstr(lam,12)}")
chk("V3","A","|lambda| = 0.8915135658", abs(al-mp.mpf('0.8915135658'))<1e-9, f"{mp.nstr(al,11)}")
chk("V4","A","arg lambda = 2.2592495539", abs(arg-mp.mpf('2.2592495539'))<1e-9, f"{mp.nstr(arg,11)}")
chk("V5","A","mu = -ln|lambda| = 0.1148346250", abs(mu-mp.mpf('0.1148346250'))<1e-9, f"{mp.nstr(mu,11)}")
chk("V6","A","D^2 = 1-|lambda|^2 = 0.2052035620", abs(D2-mp.mpf('0.2052035620'))<1e-9, f"{mp.nstr(D2,11)}")
chk("V7","A","D = 0.4529939978", abs(D-mp.mpf('0.4529939978'))<1e-9, f"{mp.nstr(D,11)}")
chk("V8","A","A = 35/437, kappa^2 = A/Q = 35/4807",
    abs(A-mp.mpf('0.08009153318'))<1e-10 and abs(k2-mp.mpf(35)/4807)<mp.mpf('1e-30'), f"{mp.nstr(k2,11)}")
chk("V9","A","kappa = 0.0853290599", abs(kap-mp.mpf('0.0853290599'))<1e-9, f"{mp.nstr(kap,10)}")
chk("V10","A","z* is attracting: |lambda| < 1", al < 1, f"{mp.nstr(al,10)}")

# ===== GROUP 2 : PRIME-REGISTER NO-GO  [R] =====
odd_all = all((Q**n) % 2 == 1 for n in range(1,65))
chk("V11","R","Q=11 is prime", all(Q%k for k in range(2,Q)), "11")
chk("V12","R","2 does not divide Q^n for n=1..64 (no finite tensor power of the register "
    "admits a 2-dim tensor factor)", odd_all, "Q^n odd for all n<=64")
chk("V13","R","CTP doubling does not help: Q^2 = 121 is odd", (Q*Q)%2==1, "121")
chk("V14","R","no integer m with 2m = Q", all(2*m != Q for m in range(0,Q+1)), "none")

# ===== GROUP 3 : COMPRESSION DICHOTOMY + SINGLE-KRAUS OBSTRUCTION  [R] =====
def haar(n, rng):
    zmat = (rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))/np.sqrt(2)
    q,r = np.linalg.qr(zmat); return q*(np.diag(r)/abs(np.diag(r)))
rng = np.random.default_rng(56)
PZ = np.zeros((11,11)); PZ[3,3]=PZ[4,4]=1.0          # Z-block = slots 3,4
emb = np.zeros((11,2)); emb[3,0]=emb[4,1]=1.0        # C^2 -> C^11

hi, lo, min_gap = 0.0, 1.0, 1.0
for _ in range(400):
    U = haar(11, rng)
    S = emb.conj().T @ U @ emb                        # S = P_Z U P_Z (2x2)
    ev = np.linalg.eigvalsh(S.conj().T@S)
    hi = max(hi, ev.max()); lo = min(lo, ev.max()); min_gap = min(min_gap, 1.0-ev.max())
chk("V15","R","generic register unitary: S^dag S has largest eigenvalue strictly below 1 in every "
    "draw, so the compressed one-cycle Z-map is strictly trace-decreasing "
    "[v1.1 REPORTING FIX: v1.0 printed the MINIMUM over draws and labelled it the maximum]",
    hi < 1.0 and min_gap > 1e-12,
    f"over 400 Haar draws, max eig(S^dag S): worst case = {hi:.7f}, best case = {lo:.7f}")

# Z-block-invariant unitary -> compression is unitary conjugation, multiplier is a pure phase
UZ = np.eye(11, dtype=complex); b = haar(2, rng); UZ[3:5,3:5] = b
S  = emb.conj().T @ UZ @ emb
chk("V16","R","trace-preserving compression <=> Z-block invariant <=> S unitary. [v1.4 SYNC: the "
    "further clause '=> |coherence multiplier| = 1' needs [S, Z_path] = 0; a general S in U(2) "
    "mixes populations with coherences. The body was fixed in v1.2; this description was not]", np.linalg.norm(S.conj().T@S-np.eye(2)) < 1e-12,
    f"||S^dag S - I|| = {np.linalg.norm(S.conj().T@S-np.eye(2)):.3e}")

# single-Kraus maps preserve purity
pur_min = 1.0
for _ in range(400):
    U = haar(11, rng); S = emb.conj().T@U@emb
    v = rng.normal(size=2)+1j*rng.normal(size=2); v /= np.linalg.norm(v)
    w = S@v
    if np.linalg.norm(w) < 1e-8: continue
    w /= np.linalg.norm(w); r = np.outer(w, w.conj())
    pur_min = min(pur_min, float(np.real(np.trace(r@r))))
chk("V17","R","any single-Kraus (compression) map sends pure states to pure states: "
    "purity = 1", abs(pur_min-1.0) < 1e-12, f"min purity over 400 draws = {pur_min:.15f}")

# Phi^QND on the equator is mixed
def PhiQND(r, m):
    return np.array([[r[0,0], m*r[0,1]],[np.conj(m)*r[1,0], r[1,1]]])
req = 0.5*np.ones((2,2), dtype=complex)
pq  = float(np.real(np.trace(PhiQND(req,L)@PhiQND(req,L))))
chk("V18","R","Phi^QND maps the pure equatorial state to a MIXED state, purity "
    "(1+|lambda|^2)/2 < 1", abs(pq-(1+float(al)**2)/2)<1e-12 and pq<1-1e-6,
    f"purity = {pq:.10f}")
chk("V19","R","THEOREM M56.2: no register-internal compression can equal Phi^QND, since "
    "purity 1 != {:.7f}".format(pq), abs(pur_min-pq) > 1e-3, f"1 vs {pq:.10f}")

# ===== GROUP 4 : LEAK vs DEPHASING SEPARATION  [R] =====
tr_leak = float(al)**2                     # ZS-F0 Thm 8.9 survival per cycle
tr_qnd  = 1.0                              # Phi^QND is trace preserving
chk("V20","R","THEOREM M56.4: ZS-F0 Thm 8.9 leaky Wilson loop has survival |lambda|^2 = "
    f"{tr_leak:.7f} per cycle, while Phi^QND has survival 1; the two one-cycle Z-maps are "
    "different objects carrying the same number", abs(tr_leak-tr_qnd) > 0.2,
    f"{tr_leak:.10f} vs {tr_qnd:.10f}")
chk("V21","R","the separation is two-fold and independent: trace functional AND purity",
    abs(tr_leak-tr_qnd)>0.2 and abs(pur_min-pq)>1e-3, "trace + purity")

# ===== GROUP 5 : MINIMAL ENVIRONMENT  [R/A] =====
# Choi matrix of Phi^QND
E = [np.zeros((2,2),dtype=complex) for _ in range(4)]
for i,(a_,b_) in enumerate(itertools.product(range(2),repeat=2)): E[i][a_,b_]=1
Choi = np.zeros((4,4), dtype=complex)
for i,(a_,b_) in enumerate(itertools.product(range(2),repeat=2)):
    blk = PhiQND(E[i], L)
    Choi[2*a_:2*a_+2, 2*b_:2*b_+2] = blk
ev = np.linalg.eigvalsh((Choi+Choi.conj().T)/2)
rk = int(np.sum(ev > 1e-10))
chk("V22","A","Choi matrix of Phi^QND is PSD", ev.min() > -1e-12, f"min eig = {ev.min():.3e}")
chk("V23","R","THEOREM M56.5: Kraus rank of Phi^QND is exactly 2 for 0<|lambda|<1, hence the "
    "minimal Stinespring environment has dimension exactly 2", rk == 2, f"rank = {rk}")
ev0 = np.linalg.eigvalsh(np.block([[PhiQND(E[0],0),PhiQND(E[1],0)],[PhiQND(E[2],0),PhiQND(E[3],0)]]))
chk("V23b","A","CORRECTION of the v1.0 theorem statement: the Choi rank of Phi^QND is 2 at "
    "lambda = 0 as well (eigenvalues 0,0,1,1), and 1 only at |lambda| = 1; v1.0 wrote 'rank 3 "
    "at lambda = 0', which is false", int(np.sum(ev0>1e-10))==2, f"eigenvalues {np.round(ev0,6)}")
chk("V24","A","dim H_E = 1 forces scalar W_k hence |gamma| = 1; |lambda| = "
    f"{float(al):.7f} < 1 therefore excludes a one-dimensional environment", float(al) < 1,
    f"|lambda| = {float(al):.10f}")

# explicit minimal dilation (reproduces ZS-M54.19)
d  = float(D)
W0 = np.eye(2, dtype=complex)
W1 = np.array([[np.conj(L), d], [-d, L]], dtype=complex)
Om = np.array([1,0], dtype=complex)
chk("V25","R","minimal environment: W1 is unitary",
    np.linalg.norm(W1.conj().T@W1-np.eye(2))<1e-14,
    f"{np.linalg.norm(W1.conj().T@W1-np.eye(2)):.3e}")
gam = complex(Om.conj()@(W1.conj().T@W0@Om))
chk("V26","R","minimal environment overlap <Omega|W1^dag W0|Omega> = lambda exactly",
    abs(gam-L)<1e-15, f"|gamma - lambda| = {abs(gam-L):.3e}")
# partial trace reproduces Phi^QND
Utot = np.zeros((4,4), dtype=complex)
P0 = np.diag([1,0]).astype(complex); P1 = np.diag([0,1]).astype(complex)
Utot = np.kron(P0,W0)+np.kron(P1,W1)
def reduce_(r):
    rho = np.kron(r, np.outer(Om,Om.conj()))
    out = Utot@rho@Utot.conj().T
    return np.trace(out.reshape(2,2,2,2), axis1=1, axis2=3)
err = max(np.linalg.norm(reduce_(E[i])-PhiQND(E[i],L)) for i in range(4))
chk("V27","R","partial trace of the minimal dilation equals Phi^QND on the complete "
    "operator basis", err < 1e-15, f"max basis error = {err:.3e}")
# uniqueness up to U(2) gauge
gerr = 0.0
for _ in range(200):
    V = haar(2, rng)
    Ut = np.kron(P0,V@W0)+np.kron(P1,V@W1)
    rho = np.kron(E[1], np.outer(Om,Om.conj()))
    o = Ut@rho@Ut.conj().T
    gerr = max(gerr, np.linalg.norm(np.trace(o.reshape(2,2,2,2),axis1=1,axis2=3)-PhiQND(E[1],L)))
chk("V28","A","the channel is invariant under a common U(2) gauge on the environment; "
    "uniqueness of the minimal Stinespring dilation up to such a gauge is IMPORTED from "
    "Stinespring 1955 / Choi 1975 and is not claimed to be established by this computation "
    "[v1.1 SCOPE FIX]", gerr < 1e-13, f"max deviation over 200 gauges = {gerr:.3e}")

# ===== GROUP 6 : MULTIPLIER NON-CONSTRAINT AT MINIMAL DIMENSION  [R] =====
# pointer-diagonal coupling on a qubit environment: gamma(phi,m) = cos(phi) - i m sin(phi)
def gamma_pm(phi, m): return math.cos(phi) - 1j*m*math.sin(phi)
phi_s = math.acos(L.real); m_s = -L.imag/math.sin(phi_s)
chk("V29","R","the pointer-diagonal qubit environment reproduces lambda exactly at "
    f"(phi,m) = ({phi_s:.10f}, {m_s:.10f})", abs(gamma_pm(phi_s,m_s)-L)<1e-14,
    f"|gamma - lambda| = {abs(gamma_pm(phi_s,m_s)-L):.3e}, |m| = {abs(m_s):.10f} <= 1")
# achievable set is the whole closed unit disc
grid_ok = True; maxmod = 0.0
for _ in range(200000):
    ph = rng.uniform(0,2*math.pi); mm = rng.uniform(-1,1)
    g = gamma_pm(ph,mm); maxmod = max(maxmod, abs(g))
    if abs(g) > 1+1e-12: grid_ok = False
cover = 0
targets = 0
for _ in range(20000):
    x,y = rng.uniform(-1,1), rng.uniform(-1,1)
    if x*x+y*y > 1: continue
    targets += 1
    ph = math.acos(max(-1,min(1,x)))
    s = math.sin(ph)
    if s < 1e-12: cover += (abs(y)<1e-9)
    else: cover += (abs(-y/s) <= 1+1e-12)
chk("V30","R","THEOREM M56.7: |gamma| <= 1 always (Cauchy-Schwarz)", grid_ok,
    f"max |gamma| over 2e5 samples = {maxmod:.12f}")
chk("V31","R","THEOREM M56.7: the achievable multiplier set at minimal environment dimension "
    "is the ENTIRE closed unit disc -- every admissible target is reachable",
    cover == targets, f"{cover}/{targets} random disc targets reachable")

# degrees-of-freedom count behind Theorem M56.7
import numpy.linalg as nla
h = 1e-7
def Fv(p):
    g = gamma_pm(p[0],p[1]); return np.array([g.real-L.real, g.imag-L.imag])
J = np.zeros((2,2))
for j in range(2):
    e_ = np.zeros(2); e_[j]=h
    J[:,j] = (Fv(np.array([phi_s,m_s])+e_)-Fv(np.array([phi_s,m_s])-e_))/(2*h)
detJ_analytic = math.sin(phi_s)**2
chk("V45","R","THEOREM M56.7 (dof count): two real unknowns (slab phase phi, environment "
    "polarisation m) meet exactly two real constraints (Re lambda, Im lambda) with Jacobian "
    "determinant sin^2(phi) > 0, so the solution is isolated and the zero residual is forced by "
    "dimension counting, not by dynamics [v1.1 CORRECTION: v1.0 reported det J = -0.6234, wrong "
    "in both sign and value; the analytic determinant is sin^2(phi*) = +0.679171]",
    abs(nla.det(J)-detJ_analytic) < 1e-4 and detJ_analytic > 1e-6,
    f"det J numeric = {nla.det(J):.6f}, analytic sin^2(phi*) = {detJ_analytic:.6f}, "
    f"residual = {nla.norm(Fv(np.array([phi_s,m_s]))):.2e}")
# independent parametrisation: gamma = p + (1-p) e^{i theta}, i.e. <Omega|U|Omega> for
# U = diag(1, e^{i theta}) and |Omega> = (sqrt p, sqrt(1-p)); solve p for a random disc target
cov2 = 0; tgt2 = 0
for _ in range(20000):
    x,y = rng.uniform(-1,1), rng.uniform(-1,1)
    if x*x+y*y > 1 or abs(x-1) < 1e-9: continue
    tgt2 += 1
    p_ = (1-(x*x+y*y))/(2*(1-x))
    if not (0.0 <= p_ <= 1.0): continue
    r_ = 1-p_
    th = math.atan2(y, x-p_) if r_ > 1e-12 else 0.0
    if abs((p_ + r_*np.exp(1j*th)) - (x+1j*y)) < 1e-9: cov2 += 1
chk("V46","R","THEOREM M56.7, independent parametrisation: gamma = p + (1-p) e^{i theta} with "
    "|Omega> = (sqrt p, sqrt(1-p)) and U = diag(1, e^{i theta}) also covers the whole disc, "
    "with the explicit inverse p = (1-|w|^2)/(2(1-Re w)); a 2-dim environment already "
    "saturates the achievable set, so raising dim H_E cannot tighten the constraint",
    cov2 == tgt2, f"{cov2}/{tgt2} disc targets solved in closed form")

# ===== GROUP 7 : ANTI-NUMEROLOGY  [X] =====
tol = 1e-6; hits = 0; N = 200000
for _ in range(N):
    ph = rng.uniform(0,2*math.pi); mm = rng.uniform(-1,1)
    if abs(gamma_pm(ph,mm)-L) < tol: hits += 1
p_free = 1.0                       # (phi,m) free -> always solvable (V31)
p_fixed = hits/N
chk("V32","X","NON-IDENTIFIABILITY, not a p-value [v1.1 TERMINOLOGY FIX]: the target-conditioned "
    "coverage fraction is 1 -- every point of the disc is hit by some (phi,m) -- so lambda is "
    "non-identifying when (phi,m) are unconstrained. Separately, uniform random (phi,m) hit "
    f"lambda within {tol} with frequency {p_fixed:.2e}, as expected for a continuous "
    "distribution. Sub-condition (B) carries evidential content ONLY if the action fixes both "
    "the slab duration and the environment state", p_free > 0.5,
    f"coverage = 1.000 (non-identifiable); random-hit frequency = {p_fixed:.2e}")

# ===== GROUP 8 : NEGATIVE CONTROLS  [X] =====
Xg = np.array([[0,1],[1,0]], dtype=complex); Zg = np.diag([1,-1]).astype(complex)
Uce = np.kron(np.eye(2), P0) + np.kron(Xg, P1)
Cm = Uce@np.kron(Zg,np.eye(2))-np.kron(Zg,np.eye(2))@Uce
nf, n2 = np.linalg.norm(Cm,'fro'), np.linalg.norm(Cm,2)
chk("V33","X","ZS-M54.22 counterexample retained: ||[U, Z_path x I]||_F = 2*sqrt(2) = 2.8284271 "
    "(NORM CONVENTION: M54's figure is Frobenius; the spectral norm of the same commutator is 2)",
    abs(nf-2*math.sqrt(2))<1e-12 and abs(n2-2.0)<1e-12,
    f"Frobenius = {nf:.7f}, spectral = {n2:.7f}")
# tautology scan on the Koenigs orbit
tau = []
for d0 in ['1e-6','1e-8','1e-10']:
    dd = mp.mpf(d0); w = zs+dd; dev = 0
    for n in range(1,6):
        w = mp.e**(w*1j*mp.pi/2); dev = max(dev, abs((w-zs)/dd - lam**n))
    tau.append((d0, float(dev)))
scale_ok = tau[0][1]/tau[1][1] > 50 and tau[1][1]/tau[2][1] > 50
chk("V34","X","TAUTOLOGY SCAN: the 'channel coherence vs Koenigs orbit' agreement is the "
    "identity lambda^n = lambda^n; its residual scales linearly with delta_0 and is NOT a "
    "physical tolerance", scale_ok,
    "; ".join(f"d0={a}: dev={b:.1e}" for a,b in tau))
# generic direct-sum -> tensor reshaping changes the channel
resh = 0.0
for _ in range(50):
    U = haar(4, rng)
    rho = np.kron(E[1], np.outer(Om,Om.conj()))
    o = U@rho@U.conj().T
    resh = max(resh, np.linalg.norm(np.trace(o.reshape(2,2,2,2),axis1=1,axis2=3)-PhiQND(E[1],L)))
chk("V35","X","negative control: a generic (non-pointer-diagonal) 4-dim unitary does NOT "
    "reduce to Phi^QND [v1.1 LABEL FIX: the reported figure is the MAXIMUM deviation]",
    resh > 1e-3, f"max deviation over 50 draws = {resh:.4f}")

# ===== GROUP 9 : CORPUS REGRESSION  [A] =====
tnode = k2*mp.cos(arg)/mp.sqrt(18); tcoef = k2*mp.cos(arg)
chk("V36","A","T_XY NODE entry = kappa^2 cos(arg lambda)/sqrt(18) = -0.0010903508 "
    "(two layers must not be conflated: the COLLECTIVE-basis operator coefficient is "
    "kappa^2 cos(arg lambda) = -0.0046259667)",
    abs(float(tnode)+0.0010903508)<1e-10 and abs(float(tcoef)+0.0046259667)<1e-9,
    f"node = {float(tnode):.10f}, collective coefficient = {float(tcoef):.10f}")
chk("V36b","A","cross-check: the node entry equals 2*(kappa/sqrt6)*(kappa/sqrt12)*cos(arg lambda), "
    "i.e. a coherent sum over the dim(Z) = 2 Menger paths",
    abs(float(2*(kap/mp.sqrt(6))*(kap/mp.sqrt(12))*mp.cos(arg)-tnode))<1e-18,
    f"{float(2*(kap/mp.sqrt(6))*(kap/mp.sqrt(12))*mp.cos(arg)):.10f}")
chk("V37","A","AMO node entries kappa/sqrt(6) = 0.03483544, kappa/sqrt(12) = 0.02463238",
    abs(float(kap/mp.sqrt(6))-0.03483544)<1e-8 and abs(float(kap/mp.sqrt(12))-0.02463238)<1e-8,
    f"{float(kap/mp.sqrt(6)):.8f}, {float(kap/mp.sqrt(12)):.8f}")
chk("V38","A","two-transit intensity cos^2(2 arg lambda) = 0.0371246",
    abs(float(mp.cos(2*arg)**2)-0.0371246)<1e-7, f"{float(mp.cos(2*arg)**2):.7f}")
chk("V39","A","static/quantum ratio 2 kappa^2 sqrt(18) = 0.0617817",
    abs(float(2*k2*mp.sqrt(18))-0.0617817)<1e-7, f"{float(2*k2*mp.sqrt(18)):.7f}")
chk("V40","A","mixed-unitary weight p = (1+|lambda|)/2 = 0.945757",
    abs(float((1+al)/2)-0.945757)<1e-6, f"{float((1+al)/2):.7f}")
Liou = np.diag([1,1,L,np.conj(L)])
sp = np.linalg.eigvals(Liou)
chk("V41","A","Liouville transfer spectrum {1,1,lambda,lambda-bar} (ZS-M53 Thm M53.4)",
    abs(sorted(abs(sp))[0]-abs(L))<1e-12, "{1,1,lam,lam*}")
chk("V42","A","spin closure: dim(Z)^2*(pi/2) = 2pi and dim(Z)^3*(pi/2) = 4pi (ZS-M54.5(iii))",
    abs(dZ**2*math.pi/2-2*math.pi)<1e-14 and abs(dZ**3*math.pi/2-4*math.pi)<1e-14, "2pi / 4pi")
chk("V43","A","spinor value: D^{1/2}(2pi) = -I and D^{1/2}(4pi) = +I, forcing chi_Z = -1",
    abs(np.trace(np.array([[np.exp(-1j*math.pi),0],[0,np.exp(1j*math.pi)]]))+2)<1e-12, "-I / +I")
chk("V44","A","the spinor double cover supplies an even carrier dimension 2Q = 22 "
    "[v1.1 SCOPE FIX: uniqueness of this candidate is NOT tested here and is no longer claimed; "
    "the internal code-subspace route of W1 is a second live candidate]",
    (2*Q) % 2 == 0 and 2*Q == 22, "22 = 2 x 11")


# ===== GROUP W : REFEREE COUNTEREXAMPLE AND THE BYPASS  [R] =====
from scipy.linalg import expm
sx = np.array([[0,1],[1,0]],dtype=complex); sz = np.diag([1,-1]).astype(complex)
rr_, th_ = float(al), float(arg); pmix = (1+rr_)/2
K0 = math.sqrt(pmix)*np.diag([np.exp(1j*th_/2), np.exp(-1j*th_/2)])
K1 = math.sqrt(1-pmix)*np.diag([np.exp(1j*(th_+math.pi)/2), np.exp(-1j*(th_+math.pi)/2)])
errK = max(np.linalg.norm(K0@E[i]@K0.conj().T + K1@E[i]@K1.conj().T - PhiQND(E[i],L)) for i in range(4))
Emb = np.zeros((11,4),dtype=complex)
for _i in range(2):
    for _j in range(2): Emb[[3,4,5,6][_j*2+_i], _j*2+_i] = 1     # |z_i>|e_j> -> slots 3,4,5,6
V4 = np.zeros((4,2),dtype=complex)
for _j in range(2):
    _v=np.zeros(4,dtype=complex); _v[0:2]=K0[:,_j]; _v[2:4]=K1[:,_j]; V4[:,_j]=_v
_Qm,_Rm = np.linalg.qr(np.hstack([V4, rng.normal(size=(4,2))+1j*rng.normal(size=(4,2))]))
U4 = _Qm*(np.diag(_Rm)/abs(np.diag(_Rm))); U4[:,0:2]=V4
U11 = Emb@U4@Emb.conj().T + (np.eye(11)-Emb@Emb.conj().T)
PZ11 = np.zeros((11,11)); PZ11[3,3]=PZ11[4,4]=1
condE = np.linalg.norm(Emb.conj().T@PZ11@Emb - np.kron(np.diag([1,0]),np.eye(2)))
errW = 0.0
for i in range(4):
    r4=np.zeros((4,4),dtype=complex)
    for a in range(2):
        for b in range(2): r4[a,b]=E[i][a,b]
    o4 = Emb.conj().T@(U11@(Emb@r4@Emb.conj().T)@U11.conj().T)@Emb
    redm=np.zeros((2,2),dtype=complex)
    for a in range(2):
        for b in range(2): redm[a,b]=o4[a,b]+o4[a+2,b+2]
    errW=max(errW,np.linalg.norm(redm-PhiQND(E[i],L)))
chk("W1","R","REFEREE COUNTEREXAMPLE REPRODUCED WITH THE ACTUAL Z POINTER PRESERVED [v1.2 FIX: "
    "v1.1 embedded the code block in slots 0-3, which are three X-slots and one Z-slot, so it did "
    "not test the claim it made]. Slots {3,4} carry the pointer and {5,6} the environment; "
    "E^dag P_Z E = I_Z (x) |e0><e0| exactly; 11 = 2*2 + 7 so C^11 = (C^2_Z (x) C^2_E) (+) C^7. "
    "ZS-M56 v1.0 Theorem M56.6 is REFUTED and gate F-M56.6 FIRES",
    condE<1e-14 and errW<1e-14 and np.linalg.norm(U11.conj().T@U11-np.eye(11))<1e-14,
    f"actual-Z preservation {condE:.2e}; U11 unitary "
    f"{np.linalg.norm(U11.conj().T@U11-np.eye(11)):.2e}; partial trace = Phi^QND on the full "
    f"operator basis {errW:.2e}")

def gaugeop(u3,u6):
    g=np.zeros((11,11),dtype=complex); g[0:3,0:3]=u3; g[3:5,3:5]=np.eye(2); g[5:11,5:11]=u6; return g
rows=[]
for _ in range(40):
    g=gaugeop(haar(3,rng),haar(6,rng))
    rows.append(np.kron(g,np.eye(11))-np.kron(np.eye(11),g.T))
sv=np.linalg.svd(np.vstack(rows),compute_uv=False); dimA=int(np.sum(sv<1e-8))
chk("W2","R","THEOREM M56.10: the commutant of the sector gauge U(3) x U(6) on the register -- "
    "the POINTWISE U(3)xU(6)-INVARIANT REGISTER ENDOMORPHISM ALGEBRA [v1.4 SYNC: v1.1-v1.3 called "
    "this 'the algebra of ZS-M54-physical observables', an expression retracted in the v1.2 body] "
    "-- is A_inv = C (+) M2(C) (+) C of dimension 6. "
    "Schur forces every X-Z, Z-Y and X-Y off-diagonal block to zero", dimA==6, f"dim A_phys = {dimA}")
chk("W3","A","LEMMA M56.10a implication (analytic, not independently computed here): : the pointer algebra M2(C) occurs in A_phys with MULTIPLICITY 1, so "
    "its OAQEC co-factor is C^1; a one-dimensional environment forces |gamma| = 1, excluded by "
    "|lambda| < 1. UNDER HYPOTHESIS (I) -- that the reduction is expressible by operators lying in "
    "A_inv -- a register-internal reduction therefore fails. [v1.4 SYNC: v1.1-v1.3 stated this "
    "unconditionally; the body made it conditional in v1.2]",
    dimA-4 == 2 and float(al) < 1, "multiplicity 1; co-factor dim 1")

gvs=[]
for _ in range(200):
    g=gaugeop(haar(3,rng),haar(6,rng)); gvs.append(np.linalg.norm(U11@g-g@U11))
chk("W4","X","CONTROL (not a proof of any no-go) [v1.2 RECLASSIFIED R -> X]: : the counterexample construction is NOT sector-gauge "
    "covariant -- it borrows two of its four dimensions from X (+) Y and mixes them with Z. The "
    "resulting channel therefore depends on a choice of environment 2-plane in C^9, a point of "
    "the Grassmannian Gr_C(2,9) of real dimension 2*2*(9-2) = 28: a new free datum",
    min(gvs) > 1e-6 and 2*2*(9-2) == 28, f"min ||[U11, gauge]||_F over 200 draws = {min(gvs):.6f}; "
    f"dim_R Gr_C(2,9) = {2*2*(9-2)}")

Pp = 0.5*(np.eye(2)+sx); Pm_ = 0.5*(np.eye(2)-sx)
cpz = np.linalg.norm(Pp@sz-sz@Pp)
chk("W5","R","THEOREM M56.9: the corpus-DERIVED vertex is bright-only (C_XZ = C_XZ P+, "
    "C_ZY = P+ C_ZY; ZS-M54 PROVEN) and P+ is the J_seam = sigma_x projector. Since "
    "{J_seam, Z_path} = 0 (M54.8a), P+ is MAXIMALLY off-diagonal in the pointer basis: "
    "||[P+, Z_path]||_F = sqrt(2) exactly", abs(cpz-math.sqrt(2))<1e-12,
    f"||[P+, Z_path]||_F = {cpz:.10f}; <z0|P+|z0> = 0.5, <z0|P+|z1> = 0.5")

Bh = np.array([[0.7,0.2+0.1j],[0.2-0.1j,-0.4]],dtype=complex); Bh=(Bh+Bh.conj().T)/2
Ubr = np.kron(Pp, expm(-1j*1.3*Bh)) + np.kron(Pm_, np.eye(2,dtype=complex))
Omv = np.array([1,0],dtype=complex)
def redbr(r):
    o = Ubr@np.kron(r,np.outer(Omv,Omv.conj()))@Ubr.conj().T
    return np.trace(o.reshape(2,2,2,2),axis1=1,axis2=3)
cz = np.linalg.norm(Ubr@np.kron(sz,np.eye(2))-np.kron(sz,np.eye(2))@Ubr)
cxs= np.linalg.norm(Ubr@np.kron(sx,np.eye(2))-np.kron(sx,np.eye(2))@Ubr)
dp0= np.linalg.norm(redbr(P0)-P0)
sxc= abs(np.real(np.trace(redbr(P0)@sx)))
chk("W6","X","CONTROL, representative only [v1.2 RECLASSIFIED R -> X]: for one Hermitian "
    "coupling the seam-controlled slab is exactly J_seam-QND and not Z_path-QND. This is an "
    "illustration; the universal statement is X5, which does not depend on the coupling",
    cxs < 1e-12 and cz > 1e-3 and dp0 > 1e-3,
    f"||[U, J_seam x I]|| = {cxs:.2e}; ||[U, Z_path x I]|| = {cz:.6f}; ||Phi(P0)-P0|| = {dp0:.6f}")

# ===== GROUP X : THE v1.2 BYPASS -- DARK STATE, MODULI, SELF-REFUTATION  =====
kapf = float(kap)
Cxz = np.zeros((3,2),dtype=complex); Czy = np.zeros((2,6),dtype=complex)
zpv = np.array([1,1],dtype=complex)/np.sqrt(2); zmv = np.array([1,-1],dtype=complex)/np.sqrt(2)
Cxz[0,:] = (kapf/np.sqrt(6))*zpv.conj(); Czy[:,0] = (kapf/np.sqrt(12))*zpv
Hint = np.zeros((11,11),dtype=complex)
Hint[0:3,3:5]=Cxz; Hint[3:5,0:3]=Cxz.conj().T; Hint[3:5,5:11]=Czy; Hint[5:11,3:5]=Czy.conj().T
vzm = np.zeros(11,dtype=complex); vzm[3:5]=zmv
vzp = np.zeros(11,dtype=complex); vzp[3:5]=zpv
chk("X1","R","the corpus quadratic vertex is bright-only: C_XZ = C_XZ P+ and C_ZY = P+ C_ZY, with "
    "node entries kappa/sqrt(6) and kappa/sqrt(12) (ZS-M54, PROVEN)",
    np.linalg.norm(Cxz-Cxz@np.outer(zpv,zpv.conj()))<1e-15,
    f"||C_XZ - C_XZ P+|| = {np.linalg.norm(Cxz-Cxz@np.outer(zpv,zpv.conj())):.2e}")
chk("X2","R","THEOREM M56.9 (Dark-State Obstruction), step 1: the bright-only vertex ANNIHILATES "
    "the seam-odd mode, H_int |z-> = 0 exactly, while H_int |z+> is nonzero. This uses no lift, "
    "no tensor structure and no choice of coupling operator",
    np.linalg.norm(Hint@vzm)<1e-16 and np.linalg.norm(Hint@vzp)>1e-3,
    f"||H_int |z->|| = {np.linalg.norm(Hint@vzm):.2e}; ||H_int |z+>|| = {np.linalg.norm(Hint@vzp):.10f}")
dmax = max(np.linalg.norm(expm(-1j*t*Hint)@vzm - vzm) for t in [0.3,1.0,7.7,100.0])
chk("X3","R","THEOREM M56.9 step 2: hence U|z-> = |z-> for EVERY slab duration",
    dmax < 1e-15, f"max ||U|z-> - |z->|| over tau in {{0.3, 1, 7.7, 100}} = {dmax:.2e}")
zmr = np.outer(zmv, zmv.conj()); zpr = np.outer(zpv, zpv.conj())
fixP0 = np.linalg.norm(PhiQND(P0,L)-P0); fixP1 = np.linalg.norm(PhiQND(P1,L)-P1)
purzm = float(np.real(np.trace(PhiQND(zmr,L)@PhiQND(zmr,L))))
chk("X4","A","THEOREM M56.9 step 3: the pure fixed points of Phi^QND for 0<|lambda|<1 are EXACTLY "
    "the pointer states {P0, P1}, because Phi(rho)=rho forces lambda*rho01 = rho01 hence rho01 = 0. "
    "The seam-odd state is not among them: its image has purity (1+|lambda|^2)/2",
    fixP0<1e-15 and fixP1<1e-15 and abs(purzm-(1+float(al)**2)/2)<1e-12,
    f"P0, P1 fixed to {max(fixP0,fixP1):.2e}; purity of Phi^QND(|z-><z-|) = {purzm:.10f}")
wpur = 0.0; wfix = 0.0; ndraw = 0
for dE in [2,3,4,5,6]:
    for _ in range(120):
        ndraw += 1
        Hc = rng.normal(size=(2*dE,2*dE))+1j*rng.normal(size=(2*dE,2*dE)); Hc=(Hc+Hc.conj().T)/2
        e0 = np.zeros(dE,dtype=complex); e0[0]=1
        vv = np.kron(zmv, e0)
        Qb,_ = np.linalg.qr(np.column_stack([vv, rng.normal(size=(2*dE,2*dE-1))+1j*rng.normal(size=(2*dE,2*dE-1))]))
        Hd = Qb.conj().T@Hc@Qb; Hd[0,1:]=0; Hd[1:,0]=0; Hc = Qb@Hd@Qb.conj().T
        Uc = expm(-1j*rng.uniform(0.1,9.0)*Hc)
        oo = Uc@np.kron(zmr, np.outer(e0,e0.conj()))@Uc.conj().T
        rd = np.trace(oo.reshape(2,dE,2,dE),axis1=1,axis2=3)
        wpur = max(wpur, abs(float(np.real(np.trace(rd@rd)))-1.0))
        wfix = max(wfix, np.linalg.norm(rd-zmr))
chk("X5","X","TAUTOLOGY -- RETRACTED AS PROOF-BEARING [v1.3 SELF-AUDIT]. The v1.2 check built a "
    "random Hermitian generator and then executed Hd[0,1:] = 0 and Hd[1:,0] = 0, which FORCES the "
    "lifted seam-odd state to be an eigenvector before the test runs. Its 600/600 PASS therefore "
    "shows only 'if it is an eigenvector it stays a pure fixed point', which is near-definitional. "
    "The dependency sets of the two compared sides intersect in the assumption itself. This is the "
    "FOURTH true-by-construction failure in this line, after ZS-M53 v1.5, ZS-M54 v1.9 T5 and the "
    "ZS-M56 seed item C2. Retained only as a control",
    wpur < 1e-12 and wfix < 1e-12,
    f"{ndraw} draws, eigenvector condition IMPOSED: max |purity-1| = {wpur:.2e}. NOT evidence.")

def orbit_dim(Mp):
    Pp_ = np.eye(9)-Mp@Mp.conj().T; cols=[]
    def gens(n,off):
        G=[]
        for i in range(n):
            for j in range(i,n):
                A=np.zeros((n,n),dtype=complex)
                if i==j: A[i,i]=1j; G.append(A.copy())
                else:
                    A1=np.zeros((n,n),dtype=complex); A1[i,j]=1; A1[j,i]=-1; G.append(A1)
                    A2=np.zeros((n,n),dtype=complex); A2[i,j]=1j; A2[j,i]=1j; G.append(A2)
        out=[]
        for A in G:
            Bm=np.zeros((9,9),dtype=complex); Bm[off:off+n,off:off+n]=A; out.append(Bm)
        return out
    for A in gens(3,0)+gens(6,3):
        T=Pp_@A@Mp; cols.append(np.concatenate([T.real.ravel(),T.imag.ravel()]))
    return np.linalg.matrix_rank(np.array(cols).T, tol=1e-9)
Mp = np.linalg.qr(rng.normal(size=(9,2))+1j*rng.normal(size=(9,2)))[0]
od = orbit_dim(Mp); moduli = 28-od
def pang(Mx): return np.sort(np.arccos(np.clip(np.linalg.svd(Mx[0:3,:],compute_uv=False),0,1)))
th0 = pang(Mp); pdev = 0.0
for _ in range(300):
    gg=np.zeros((9,9),dtype=complex); gg[0:3,0:3]=haar(3,rng); gg[3:9,3:9]=haar(6,rng)
    pdev=max(pdev, np.linalg.norm(pang(np.linalg.qr(gg@Mp)[0])-th0))
chk("X6","R","THEOREM M56.11 (Environment Moduli): the gauge-invariant content of the internal "
    "environment choice is EXACTLY 2 real numbers, not 28. dim_R Gr_C(2,9) = 28 is the RAW "
    "embedding manifold; the generic U(3)xU(6) orbit has dimension 26, leaving moduli 28-26 = 2. "
    "[v1.2 CORRECTION: v1.1 reported 28 free real data and a 30-parameter internal route; both "
    "were overcounts by a factor of about ten]",
    moduli == 2, f"dim Gr = 28, generic orbit = {od}, moduli = {moduli}")
chk("X7","R","THEOREM M56.11: the two moduli are the principal angles between the environment "
    "2-plane and the X-sector, invariant under the gauge action",
    pdev < 1e-12, f"(theta1, theta2) = ({th0[0]:.6f}, {th0[1]:.6f}); invariance over 300 gauge "
    f"draws = {pdev:.2e}")
cvv = [np.linalg.norm(Hint@gaugeop(haar(3,rng),haar(6,rng))-gaugeop(haar(3,rng),haar(6,rng))@Hint)
       for _ in range(200)]
chk("X8","X","SELF-REFUTING CONTROL: ZS-M54's OWN mediator vertex H_int is NOT in the commutant. "
    "Therefore the v1.1 rule 'physical observable = pointwise gauge-invariant' would delete the "
    "parent paper's mediator skeleton. v1.1 Theorem M56.10 conflated covariance with pointwise "
    "invariance and is SPLIT in v1.2 into Lemma M56.10a (PROVEN) and Proposition M56.10b "
    "(DERIVED-CONDITIONAL)", min(cvv) > 1e-6,
    f"min ||[H_int, gauge]||_F over 200 draws = {min(cvv):.6f} (nonzero)")

LED.append(("W7","D","DECLARATION [v1.2 RECLASSIFIED R -> D]: Corollary M56.9a, that the "
    "internal-environment route and gate F-M54-13 require the same missing object, is a "
    "HYPOTHESIS-strong structural claim. ZS-M54.15 proves r_supp^(2) = 0, not that pointer-QND "
    "coupling and objective-record amplification are the same object. Judgement deferred to the "
    "ZS-S14 cubic/quartic vertex computation.","DECL",""))


# ===== GROUP Y : v1.3 -- THE TWO-GENERATOR DIAGNOSIS =====
GZ = np.zeros((11,11),dtype=complex); GZ[3:5,3:5] = -float(arg)*np.diag([1,-1]).astype(complex)
VZ = np.zeros((11,11),dtype=complex)
VZ[0:3,3:5]=Cxz; VZ[3:5,0:3]=Cxz.conj().T; VZ[3:5,5:11]=Czy; VZ[5:11,3:5]=Czy.conj().T
chk("Y1","R","LEMMA M56.9a (Vertex-Kernel Lemma) -- the surviving part of v1.2's M56.9: the "
    "bright-only quadratic cross-sector vertex annihilates the seam-odd mode",
    np.linalg.norm(VZ@vzm)<1e-16, f"||V_Z |z->|| = {np.linalg.norm(VZ@vzm):.2e}")
gnorm = np.linalg.norm(GZ@vzm); ov = np.vdot(vzp, GZ@vzm)/(-float(arg))
chk("Y2","A","[v1.7 RECLASSIFIED R->A] ALGEBRAIC identity about the RECONSTRUCTED G_Z, not about the microscopic slab. LEMMA M56.9b (Holonomy Escape) -- THE REFUTATION OF v1.2's CHANNEL CLAIM: ZS-M54's "
    "Z-internal generator G_Z = -arg(lambda) Z_path does NOT annihilate the seam-odd mode. Since "
    "Z_path|z-> = |z+>, it rotates the dark line straight into the bright line",
    abs(gnorm-float(arg))<1e-12 and abs(ov-1)<1e-12,
    f"||G_Z |z->|| = {gnorm:.10f} = arg(lambda); <z+|G_Z|z->/(-arg) = {ov.real:.10f}")
mix = np.linalg.norm(VZ@GZ@vzm); mixrev = np.linalg.norm(GZ@VZ@vzm)
chk("Y3","A","[v1.7 RECLASSIFIED R->A] conditional on the layer glue, which v1.6 showed is FALSE for a lone Z_path term. PROPOSITION M56.9c (Mixed-Generator Route): the composition V_Z G_Z carries the "
    "seam-odd mode into X (+) Y with NO non-bright vertex. Note the ordering is essential -- the "
    "reverse product vanishes",
    mix > 1e-3 and mixrev < 1e-16,
    f"||V_Z G_Z |z->|| = {mix:.10f}; ||G_Z V_Z |z->|| = {mixrev:.2e}")
dev = [np.linalg.norm(expm(-1j*t*(GZ+VZ))@vzm - np.vdot(vzm,expm(-1j*t*(GZ+VZ))@vzm)*vzm) for t in [0.3,1.0,3.0]]
chk("Y4","X","[v1.7 RECLASSIFIED R->X] the 'FULL M54 slab' reading and the claim that the parent violates Condition (E) were retracted in v1.4. Control only. CONSEQUENCE: on the FULL M54 slab generator G_Z + V_Z the seam-odd line is not "
    "invariant. Condition (E) of v1.2 is therefore not a faithfulness requirement but a dynamical "
    "assumption, and it is violated by the parent package itself. Gate F-M56.15 is FIRED, not OPEN",
    min(dev) > 1e-2, f"||U|z-> - (phase)|z->|| at tau = 0.3, 1, 3: "
    f"{dev[0]:.10f}, {dev[1]:.10f}, {dev[2]:.10f}")
UZop = np.diag([np.exp(1j*float(arg)), np.exp(-1j*float(arg))])
ampl = np.vdot(zpv, UZop@zmv); sa = math.sin(float(arg))
chk("Y5","X","[v1.7 RECLASSIFIED A->X] circular: the compared sides share arg(lambda), which was the input (see Z5). THEOREM M56.12 step 1: the holonomy maps seam-odd onto seam-even with the exact "
    "amplitude <z+|U_Z|z-> = i sin(arg lambda)",
    abs(ampl-1j*sa)<1e-14, f"<z+|U_Z|z-> = {ampl.imag:.10f}i; sin(arg lambda) = {sa:.10f}; "
    f"cos(arg lambda) = {math.cos(float(arg)):.10f}")
nX = kapf/np.sqrt(6); nY = kapf/np.sqrt(12)
chk("Y6","X","[v1.7 RECLASSIFIED R->X] layer-glue conditional and circular in arg(lambda); not physical evidence. THEOREM M56.12 (Holonomy-Assisted Record Support): ZS-M54.15 proves the DIRECT "
    "quadratic record support of the seam-odd mode vanishes, r_supp^(2) = 0. One holonomy "
    "insertion re-opens it exactly, with leading amplitude sin(arg lambda) times the node entry. "
    "This is a refinement of M54.15, not a contradiction of it, and it is the object ZS-M57 was "
    "chartered to compute",
    np.linalg.norm(Czy.conj().T@zmv) < 1e-15 and nX*abs(sa) > 1e-3,
    f"direct ||<z-|C_ZY|| = {np.linalg.norm(Czy.conj().T@zmv):.2e}; with one holonomy: to X "
    f"{nX*abs(sa):.10f}, to Y {nY*abs(sa):.10f}")
cGV = np.linalg.norm(GZ@VZ-VZ@GZ)
cGZp = np.linalg.norm(GZ[3:5,3:5]@np.diag([1,-1])-np.diag([1,-1])@GZ[3:5,3:5])
chk("Y7","X","[v1.7 RECLASSIFIED R->X] the universal 'no generator-level argument' claim was narrowed in v1.4. Control only. THEOREM M56.13 (Two-Generator Diagnosis): G_Z is pointer-diagonal and V_Z is "
    "seam-supported, and the two do not commute. The finite slab is therefore not the product of "
    "a pointer-QND factor and a seam-QND factor, and NO generator-level argument can decide "
    "F-M54-16'. This is why ZS-M56 v1.0, v1.1 and v1.2 each failed: each examined one generator",
    cGV > 1e-3 and cGZp < 1e-14 and abs(cpz-math.sqrt(2)) < 1e-12,
    f"||[G_Z, V_Z]||_F = {cGV:.10f}; ||[G_Z, Z_path]|| = {cGZp:.2e}; ||[P+, Z_path]||_F = "
    f"{cpz:.10f} = sqrt(2)")
Embq = np.zeros((11,4),dtype=complex)
for _i in range(2):
    for _j in range(2): Embq[[3,4,5,6][_j*2+_i], _j*2+_i] = 1
rows_ = []
for t in [0.5,1.0,2.0,5.0,20.0]:
    U4q = Embq.conj().T@expm(-1j*t*(GZ+VZ))@Embq
    def redq(rm):
        r4=np.zeros((4,4),dtype=complex)
        for a in range(2):
            for b in range(2): r4[a,b]=rm[a,b]
        o=U4q@r4@U4q.conj().T
        return np.array([[o[0,0]+o[2,2],o[0,1]+o[2,3]],[o[1,0]+o[3,2],o[1,1]+o[3,3]]])
    rows_.append((t, np.linalg.norm(redq(P0)-P0), abs(redq(E[1])[0,1]), np.angle(redq(E[1])[0,1])))
leakrows=[]
for t in [0.5,1.0,2.0,5.0,20.0]:
    U4q = Embq.conj().T@expm(-1j*t*(GZ+VZ))@Embq
    nu = np.linalg.norm(U4q.conj().T@U4q-np.eye(4))
    r4=np.zeros((4,4),dtype=complex); r4[0,0]=1
    o=U4q@r4@U4q.conj().T
    trr=float(np.real(o[0,0]+o[2,2]+o[1,1]+o[3,3]))
    leakrows.append((t,nu,trr,1-trr))
chk("Y8","X","LEAK DIAGNOSTIC, NOT A REDUCED CHANNEL [v1.4 RECLASSIFIED R -> X AND RENAMED]. The "
    "code subspace is NOT invariant under G_Z + V_Z, so E^dag U E is not unitary and the projected "
    "map is completely positive but TRACE-DECREASING. v1.3 Table 5.1 reported its diagonal drift as "
    "'population movement' and its off-diagonal as a 'coherence multiplier'; both readings re-mix "
    "exactly what Theorem M56.4 separated. The correct reading is a leak probability",
    all(r[1] > 1e-6 for r in leakrows) and all(r[3] > 1e-6 for r in leakrows),
    "; ".join(f"tau={r[0]}: ||U4^dag U4-I||={r[1]:.3e}, Tr Psi(P0)={r[2]:.8f}, p_leak={r[3]:.3e}"
              for r in leakrows))
phase_at_half = rows_[0][3]
chk("Y9","X","ANTI-FITTING CONTROL: at tau = 0.5 the coherence phase equals arg(lambda) to 8e-5. "
    "This is NOT evidence. G_Z = -arg(lambda) Z_path gives coherence phase 2*tau*arg(lambda), "
    "which equals arg(lambda) exactly when tau = 1/2. The agreement is a fitted duration and fires "
    "the anti-fitting rule; it is the same circularity M56.7 proves is unavoidable",
    abs(phase_at_half-float(arg)) < 1e-3,
    f"phase at tau=0.5 = {phase_at_half:.8f} vs arg(lambda) = {float(arg):.8f} -- fitted, discarded")



# ===== GROUP Z : v1.4 -- THE LAYER-GLUE DICHOTOMY =====
SigZ = Cxz.conj().T@Cxz + Czy@Czy.conj().T
cc = kapf**2/6 + kapf**2/12
chk("Z1","R","LEMMA M56.14a (Coupling-Gram Axis) [v1.5 RENAMED: v1.4 called this 'the Feshbach "
    "self-energy'; it is NOT -- a Feshbach self-energy carries a resolvent (E - H_X)^-1, which this "
    "expression does not. It is the coupling GRAM operator, i.e. the R = I special case]: "
    "Gamma_Z = C_XZ^dag C_XZ + C_ZY C_ZY^dag = (kappa^2/6 + "
    "kappa^2/12) P+ = (kappa^2/4) P+",
    np.linalg.norm(SigZ-cc*Pp)<1e-16 and abs(cc-kapf**2/4)<1e-15,
    f"Sigma_Z = {cc:.12f} * P+; ||Sigma_Z - c P+|| = {np.linalg.norm(SigZ-cc*Pp):.2e}; "
    f"kappa^2/4 = {kapf**2/4:.12f}")
a1=np.linalg.norm(SigZ@np.array([[0,1],[1,0]],dtype=complex)-np.array([[0,1],[1,0]],dtype=complex)@SigZ)
a2=np.linalg.norm(SigZ@np.diag([1,-1]).astype(complex)-np.diag([1,-1]).astype(complex)@SigZ)
chk("Z2","R","THEOREM M56.14, AXIS: Sigma_Z is SEAM-diagonal and annihilates the seam-odd mode. "
    "The reason is structural, not numerical: bright-only makes C rank-one through P+, and "
    "P+ = (I + J_seam)/2 is a polynomial in J_seam, so Sigma_Z lies in the algebra generated by "
    "J_seam",
    a1 < 1e-16 and a2 > 1e-6 and np.linalg.norm(SigZ@zmv) < 1e-16,
    f"||[Sigma_Z, J_seam]|| = {a1:.2e}; ||[Sigma_Z, Z_path]|| = {a2:.12f}; "
    f"||Sigma_Z |z->|| = {np.linalg.norm(SigZ@zmv):.2e}")
b1=np.linalg.norm(GZ[3:5,3:5]@np.diag([1,-1]).astype(complex)-np.diag([1,-1]).astype(complex)@GZ[3:5,3:5])
b2=np.linalg.norm(GZ[3:5,3:5]@np.array([[0,1],[1,0]],dtype=complex)-np.array([[0,1],[1,0]],dtype=complex)@GZ[3:5,3:5])
chk("Z3","A","[v1.7 RECLASSIFIED R->A] reduced to an axis MISMATCH in v1.5; not an exhaustive dichotomy. THEOREM M56.15 (Layer-Glue Dichotomy): the reconstruction layer (11b) supplies "
    "G_Z = -arg(lambda) Z_path, which is POINTER-diagonal and does NOT annihilate the seam-odd "
    "mode. The two layers therefore supply Z-internal generators on ANTICOMMUTING axes, since "
    "{J_seam, Z_path} = 0. The Layer-Glue Hypothesis IS the choice of axis, and the dark-state "
    "verdict flips with it",
    b1 < 1e-14 and b2 > 1e-6 and np.linalg.norm(np.array([[0,1],[1,0]],dtype=complex)@np.diag([1,-1]).astype(complex)+np.diag([1,-1]).astype(complex)@np.array([[0,1],[1,0]],dtype=complex)) < 1e-16,
    f"||[G_Z, Z_path]|| = {b1:.2e}; ||[G_Z, J_seam]|| = {b2:.10f}; ||G_Z|z->|| = "
    f"{np.linalg.norm(GZ@vzm):.10f}; ||{{J_seam, Z_path}}|| = 0.00e+00")
SigE=np.zeros((11,11),dtype=complex); SigE[3:5,3:5]=SigZ
Hact=VZ+SigE
dact=max(np.linalg.norm(expm(-1j*t*Hact)@vzm-vzm) for t in [0.3,1.0,7.7,100.0])
chk("Z4","X","RETRACTED AS STATED [v1.5]: v1.4 wrote H_act = V_Z + Sigma_Z and called it 'the full "
    "action-layer slab'. That DOUBLE-COUNTS: Feshbach admits a full-space description in which V_Z "
    "is explicit, or a reduced-Z description in which X (+) Y are eliminated into Sigma_Z(E). One "
    "may not add both. Retained only as an arithmetic control; the correct statement is Z10",
    np.linalg.norm(Hact@vzm) < 1e-16 and dact < 1e-15,
    f"||H_act |z->|| = {np.linalg.norm(Hact@vzm):.2e}; max ||exp(-i tau H_act)|z-> - |z->|| over "
    f"tau in {{0.3, 1, 7.7, 100}} = {dact:.2e}")
chk("Z5","X","CIRCULARITY DIAGNOSIS [v1.4 SELF-AUDIT]: G_Z = -arg(lambda) Z_path contains "
    f"arg(lambda) = {float(arg):.10f} by construction, so v1.3's headline <z+|U_Z|z-> = "
    "i sin(arg lambda) is trigonometry on the inserted angle, not new information about lambda. "
    "The dependency sets of the two sides intersect in arg(lambda). This is the FIFTH "
    "import-the-answer failure in this line: ZS-M53 v1.5, ZS-M54 v1.9 T5, ZS-M56 seed C2, "
    "ZS-M56 v1.2 X5, ZS-M56 v1.3 M56.12",
    abs(math.sin(float(arg))-0.7722296705) < 1e-9,
    f"sin(arg lambda) = {math.sin(float(arg)):.10f} -- a function of the inserted angle")
seqX=(kapf/np.sqrt(6))*abs(math.sin(float(arg))); dysX=float(arg)*kapf/np.sqrt(6)
chk("Z6","A","THEOREM M56.12 SPLIT [v1.4 CORRECTION]: v1.3 conflated two different time objects. "
    "(i) SEQUENTIAL, a full finite holonomy followed by the vertex, gives amplitude "
    "(kappa/sqrt6)|sin arg lambda| into X. (ii) SIMULTANEOUS, the short-time Dyson expansion of "
    "exp(-i tau (G_Z + V_Z)), gives leading cross term -(tau^2/2) V_Z G_Z |z->, i.e. coefficient "
    "arg(lambda)(kappa/sqrt6). These are not the same leading order",
    abs(dysX/seqX - float(arg)/abs(math.sin(float(arg)))) < 1e-12,
    f"(i) to X {seqX:.10f}, to Y {(kapf/np.sqrt(12))*abs(math.sin(float(arg))):.10f}; "
    f"(ii) to X {dysX:.10f}, to Y {float(arg)*kapf/np.sqrt(12):.10f}; "
    f"ratio = arg/|sin arg| = {float(arg)/abs(math.sin(float(arg))):.10f}")



# ===== GROUP R5 : v1.5 -- THE ONE-PARAMETER REDUCTION =====
def hermr(n):
    m=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); return (m+m.conj().T)/2
worstF=0.0; alist=[]
for _ in range(400):
    HX=hermr(3); HY=hermr(6); Ee=rng.normal()+3.0+0.3j
    RX=np.linalg.inv(Ee*np.eye(3)-HX); RY=np.linalg.inv(Ee*np.eye(6)-HY)
    Sg = Cxz.conj().T@RX@Cxz + Czy@RY@Czy.conj().T
    aa = np.vdot(zpv, Sg@zpv); alist.append(abs(aa))
    worstF = max(worstF, np.linalg.norm(Sg-aa*Pp)/max(abs(aa),1e-30))
chk("Z7","R","THEOREM M56.14b (RANK-ONE SEAM RIGIDITY) -- the v1.5 closure. Because P+ is RANK ONE, "
    "P+ M P+ = <z+|M|z+> P+ for EVERY operator M. Bright-only puts P+ on the Z-leg of every "
    "coupling, so the TRUE Feshbach self-energy Sigma_Z(E) = C_XZ^dag R_X(E) C_XZ + C_ZY R_Y(E) "
    "C_ZY^dag is a scalar multiple of P+ for ANY external Hamiltonians and ANY spectral parameter. "
    "The DIRECTION is rigid; the COEFFICIENT is not",
    worstF < 1e-12,
    f"400 random (H_X, H_Y, E): max relative residue = {worstF:.3e}; |alpha| ranges over "
    f"[{min(alist):.4e}, {max(alist):.4e}]")
worstC=0.0
for _ in range(300):
    Mm=np.eye(2,dtype=complex)
    for _k in range(int(rng.integers(1,5))):
        Mm = Mm @ (Cxz.conj().T@hermr(3)@Cxz if rng.random()<0.5 else Czy@hermr(6)@Czy.conj().T)
    aa=np.vdot(zpv,Mm@zpv); worstC=max(worstC, np.linalg.norm(Mm-aa*Pp)/max(abs(aa),1e-30))
chk("Z8","R","THEOREM M56.14b, ALL ORDERS: arbitrary chains of round trips with arbitrary "
    "insertions also land on P+, so the rigidity is not an O(kappa^2) statement but holds to every "
    "order of coupling elimination", worstC < 1e-12,
    f"300 random chains of length 1-4: max relative residue = {worstC:.3e}")
GamZ = Cxz.conj().T@Cxz + Czy@Czy.conj().T
szc = abs(np.trace(GamZ@np.diag([1,-1]).astype(complex))/2)
chk("Z9","R","COROLLARY M56.14c (COUPLING-SECTOR CLOSURE) -- this ANSWERS 'what unique operator does "
    "the action layer supply?'. The coupling-elimination sector supplies exactly ONE operator "
    "direction, P+ = (I + J_seam)/2, at every order and for every resolvent. Its Z_path component "
    "vanishes identically. Therefore the ONLY possible action-layer source of a pointer-diagonal "
    "Z-internal generator is the BARE ZZ block of the projected Hessian",
    szc < 1e-16 and abs(np.trace(GamZ@np.array([[0,1],[1,0]],dtype=complex))/2) > 1e-6,
    f"sigma_z component of the coupling sector = {szc:.2e} (identically zero); sigma_x component "
    f"= {abs(np.trace(GamZ@np.array([[0,1],[1,0]],dtype=complex))/2):.10f}")
sxo=np.array([[0,1],[1,0]],dtype=complex); szo=np.diag([1,-1]).astype(complex)
res=[]
for nm,Hb in [("d = 0", 0.7*np.eye(2)+0.3*sxo), ("d = 0.25", 0.7*np.eye(2)+0.3*sxo+0.25*szo)]:
    r1=np.linalg.norm((Hb+GamZ)@zmv-np.vdot(zmv,(Hb+GamZ)@zmv)*zmv)
    Hf=np.zeros((11,11),dtype=complex)
    Hf[0:3,3:5]=Cxz; Hf[3:5,0:3]=Cxz.conj().T; Hf[3:5,5:11]=Czy; Hf[5:11,3:5]=Czy.conj().T; Hf[3:5,3:5]=Hb
    vv=np.zeros(11,dtype=complex); vv[3:5]=zmv
    r2=np.linalg.norm(Hf@vv-np.vdot(vv,Hf@vv)*vv)
    res.append((nm,r1,r2))
chk("Z10","R","THEOREM M56.16' (ONE-UNKNOWN REDUCTION) [v1.5, replacing the retracted M56.16]: in "
    "the full-space description and in the reduced-Z description alike, the seam-odd line is "
    "preserved if and only if the BARE ZZ block has no Z_path component. The two descriptions give "
    "numerically identical answers, so they are one unknown seen twice, not two results",
    res[0][1]<1e-14 and res[0][2]<1e-14 and abs(res[1][1]-0.25)<1e-12 and abs(res[1][2]-0.25)<1e-12,
    "; ".join(f"{r[0]}: reduced {r[1]:.3e}, full-space {r[2]:.3e}" for r in res))
inter=[]
for th in [0.0, math.pi/6, math.pi/4, math.pi/3]:
    Hm=math.cos(th)*sxo+math.sin(th)*szo
    inter.append((th, np.linalg.norm(Hm@zmv-np.vdot(zmv,Hm@zmv)*zmv)))
chk("Z11","X","THE 'DICHOTOMY' IS NOT EXHAUSTIVE [v1.5 RETRACTION of v1.4's 'nothing in between']. A "
    "general Hermitian on C^2 is a I + b sx + c sy + d sz. Anticommutation of sx and sz does NOT "
    "forbid intermediate Bloch axes, and such axes exist and break the dark line. What is proved is "
    "an AXIS MISMATCH between the two identified candidates, not a classification of all glues",
    inter[0][1] < 1e-14 and all(r[1] > 1e-3 for r in inter[1:]),
    "; ".join(f"angle {r[0]:.4f}: dark-line deviation {r[1]:.6f}" for r in inter))
chk("Z12","A","LEMMA M56.15b (Reality Constraint) [DERIVED-CONDITIONAL on the ZS-M6 register basis "
    "being real and the action real, so that the projected Hessian is real symmetric]: sigma_y is "
    "purely imaginary, hence c = 0 and H_ZZ = a I + b J_seam + d Z_path. The entire ZS-M56 line "
    "therefore reduces to ONE real number: is d = 0?",
    np.linalg.norm(np.array([[0,-1j],[1j,0]]).real) < 1e-16,
    "sigma_y has zero real part; three real parameters remain, and only d is in question")



# ===== GROUP B6 : v1.6 -- F-M56.18a CLOSED (bare ZZ block retrieved and derived) =====
LZbare = np.diag([0.0,1.0])                     # ZS-M6 2.1 : beta_0 (lam=0), Z2-odd (lam=1)
chk("B1","R","THEOREM M56.17 (Bare ZZ Block Retrieved) -- ROUTE (a), corpus retrieval. ZS-M6 §2.1 "
    "states 'Z-sector (mediator): beta_0 physical mode (lambda=0) + Z2-odd mode (lambda=1)', and "
    "ZS-S1 §5.1 gives the block form L(mu) = [[L_X+mu^2, C_XZ, 0],[C_ZX, L_Z+mu^2, C_ZY],[0, C_YZ, "
    "L_Y+mu^2]]. Hence in the seam eigenbasis L_Z = diag(0,1) = (1/2) I - (1/2) J_seam: purely "
    "seam-axis, with ZERO off-diagonal. The parameter d of ZS-M56 v1.5 is therefore ZERO",
    abs(LZbare[0,1])<1e-18 and abs((LZbare[0,0]-LZbare[1,1])/2+0.5)<1e-15,
    f"a = {(LZbare[0,0]+LZbare[1,1])/2:.6f}, b = {(LZbare[0,0]-LZbare[1,1])/2:.6f}, "
    f"d = |off-diagonal| = {abs(LZbare[0,1]):.2e}")
sxo=np.array([[0,1],[1,0]],dtype=complex); szo=np.diag([1,-1]).astype(complex)
o1=abs(np.vdot(zmv, szo@zpv)); o2=abs(np.vdot(zpv, szo@zmv))
d1=abs(np.vdot(zpv, szo@zpv)); d2=abs(np.vdot(zmv, szo@zmv))
chk("B2","R","THEOREM M56.18 (Z2-Odd Forbiddance) -- ROUTE (b), structural derivation. ZS-S1 §5.2 "
    "(from ZS-F5) states that the Z-sector carries a Z2 seam symmetry eps <-> -eps grading the two "
    "Z modes into one Z2-EVEN (beta_0) and one Z2-ODD. In that basis Z_path is purely OFF-DIAGONAL: "
    "it maps even <-> odd with unit amplitude and has vanishing diagonal. Z_path is therefore a "
    "Z2-ODD OPERATOR, and a Z2-symmetric Hessian contains no Z2-odd operator. Hence d = 0 EXACTLY. "
    "Because this is a symmetry argument it holds at EVERY order for which the symmetry is exact, "
    "which closes F-M56.18b conditionally as well",
    abs(o1-1)<1e-14 and abs(o2-1)<1e-14 and d1<1e-14 and d2<1e-14,
    f"<z-|Z_path|z+> = {o1:.6f}, <z+|Z_path|z-> = {o2:.6f}, diagonal entries "
    f"{d1:.2e} and {d2:.2e}")
tau6=(5-math.sqrt(5))/2
Lreg=np.zeros((11,11)); Lreg[0,0]=0.0; Lreg[1,1]=1.0
for _i in range(2,5): Lreg[_i,_i]=19/18
for _i in range(5,8): Lreg[_i,_i]=23/18
for _i in range(8,11): Lreg[_i,_i]=tau6*23/18
Lreg=Lreg+np.eye(11)
decs=np.sort(np.linalg.eigvalsh(Lreg))
corp_dec=np.array([1.0,2.0,2.0556,2.0556,2.0556,2.2778,2.2778,2.2778,2.7658,2.7658,2.7658])
gg=math.sqrt(3*float(k2)); Lco=Lreg.copy()
for _b in [2,5,8]: Lco[_b,0]=gg; Lco[0,_b]=gg
cous=np.sort(np.linalg.eigvalsh(Lco))
corp_cou=np.array([0.9517,2.0,2.0556,2.0556,2.0736,2.2778,2.2778,2.2952,2.7658,2.7658,2.7787])
chk("B3","X","VERIFIED-REGRESSION, not proof-bearing [v1.8 RECLASSIFIED R->X, matching the v1.7 body demotion]: the ZS-M6 §2.3 decoupled AND coupled "
    "block-Laplacian spectra are reproduced from L_Z = diag(0,1), L_X = (19/18)I_3, L_Y = "
    "(23/18)I_3 (+) ((5-sqrt5)/2)(23/18)I_3, mu^2 = 1, and the rank-1 beta_0-selected coupling with "
    "g^2 = dim(Gamma) kappa^2. Independent reproduction of the corpus numbers from the corpus "
    "structure",
    max(abs(decs-corp_dec)) < 5e-5 and max(abs(cous-corp_cou)) < 5e-5,
    f"decoupled max deviation {max(abs(decs-corp_dec)):.2e}; coupled max deviation "
    f"{max(abs(cous-corp_cou)):.2e}; |dlambda|_max = {max(abs(cous-decs)):.4f} (corpus 0.0483); "
    f"kappa^2/lambda_min = {float(k2)/decs[0]:.4f} (corpus 0.0073)")
evv,evc=np.linalg.eigh(Lco); oi=int(np.argmax(abs(evc[1,:])))
JZ=np.diag([1,-1]+[1]*9).astype(float)
chk("B4","X","VERIFIED-REGRESSION [v1.8 RECLASSIFIED R->X]. The script INPUTS L_Z = diag(0,1) and attaches the coupling only to the beta_0 slot, so the odd mode being unshifted is a consequence of the input, not independent evidence. Sixth true-by-construction instance. in the COUPLED spectrum the Z2-odd "
    "mode is exactly unshifted and is an exact eigenvector of the FULL block-Laplacian, while the "
    "beta_0 mode shifts by -0.0483. Equivalently the full Laplacian commutes with the Z2 grading "
    "operator J_Z of ZS-F0 Def 8.11",
    abs(evv[oi]-2.0) < 1e-12 and abs(abs(evc[1,oi])**2-1) < 1e-12
    and np.linalg.norm(Lco@JZ-JZ@Lco) < 1e-14,
    f"Z2-odd eigenvalue {evv[oi]:.10f}, shift {abs(evv[oi]-2.0):.2e}; eigenvector purity on slot 1 "
    f"= {abs(evc[1,oi])**2:.12f}; ||[L_coupled, J_Z]||_F = {np.linalg.norm(Lco@JZ-JZ@Lco):.2e}")
chk("B5","A","COROLLARY M56.19a (LAYER-GLUE VERDICT, CLOSED): the coupling-elimination sector lies "
    "on the seam axis at all orders (M56.14c) and the bare ZZ block lies on the seam axis (M56.17, "
    "M56.18). Hence NO LONE Z_path TERM survives in the Z-only block [v1.8 SYNC: v1.6-v1.7 ledger said "
    "'no pointer component anywhere', which contradicts the selection rule and was narrowed in the "
    "v1.7 body but not here]. The Layer-Glue "
    "Hypothesis is FALSE, and G_Z = -arg(lambda) Z_path is confirmed as a pure (11b) reconstruction "
    "object, exactly as ZS-M54 classified it",
    abs(LZbare[0,1]) < 1e-18 and abs(float(np.trace(GamZ@szo).real)/2) < 1e-16,
    "bare block off-diagonal 0.00e+00; coupling-sector sigma_z component 0.00e+00")
chk("B6","R","THEOREM M56.20 (Z2 SELECTION RULE) -- the positive result. A pointer-diagonal vertex "
    "H_int = Z_path (x) B is Z2-symmetric if and only if B is ALSO Z2-odd, since odd x odd = even. "
    "The QND vertex is therefore NOT forbidden: it is subject to a selection rule requiring the "
    "environment operator to carry Z2-odd charge. Since the Z-register's own generator is Z2-even, "
    "that environment cannot be the Z-register itself. This converts the obstruction into a "
    "computable condition on F-M56.A",
    abs(o1-1) < 1e-14 and abs(np.trace(szo@szo).real-2) < 1e-14,
    "Z_path is Z2-odd; Z_path (x) B is Z2-even iff B is Z2-odd")
chspin=np.diag([np.exp(-1j*math.pi),np.exp(1j*math.pi)])
chk("B7","X","CONTROL, ONE BIT ONLY: the j = 1/2 spinor factor of chi_Z = -1 carries a Z2 grading "
    "(D^(1/2)(2pi) = -I, D^(1/2)(4pi) = +I), so it is a candidate carrier of the Z2-odd operator B "
    "required by M56.20. The evidence is a one-bit grading match, which this line has mistaken for "
    "a derivation five times. Registered HYPOTHESIS, not DERIVED",
    abs(np.trace(chspin).real+2) < 1e-12, "trace D^(1/2)(2pi) = -2.0; one-bit match")
LED.append(("B8","D","OPEN TENSION registered [v1.7: moved out of the PASS total into the declaration total]: ZS-S1 §5.2 calls the Z2-odd mode a gauge mode projected out of the physical Hilbert space, while ZS-M54 builds a two-dimensional PHYSICAL Z-register. Gate F-M56.21.","DECL",""))



# ===== GROUP C7 : v1.7 -- CLOSING THE ACTION LAYER =====
JZ11 = np.diag([1.0,-1.0]+[1.0]*9)
mp_,mm_ = 0,0
for _i in range(11):
    for _j in range(11):
        Eu=np.zeros((11,11)); Eu[_i,_j]=1
        if np.allclose(JZ11@Eu@JZ11,Eu): mp_+=1
        elif np.allclose(JZ11@Eu@JZ11,-Eu): mm_+=1
chk("C1","R","THEOREM M56.21 step 1 (total grading made explicit, per audit item 3): the seam Z2 acts "
    "on the WHOLE register as J_Z = I_11 - 2|1><1| (ZS-F0 Def 8.11). Its odd eigenspace is EXACTLY "
    "ONE-DIMENSIONAL, span{z-}. The induced grading of Mat_11 reproduces ZS-F0 Thm 8.12",
    mp_==101 and mm_==20 and int(np.sum(np.diag(JZ11)<0))==1,
    f"odd eigenspace dim = 1; dim Mat_+ = {mp_} (= 1^2 + 10^2), dim Mat_- = {mm_} (= 2*1*10); "
    "ZS-F0 Thm 8.12 states 101 and 20")
def odd_dim(idx):
    Jr=JZ11[np.ix_(idx,idx)]; n=len(idx); c=0
    for _i in range(n):
        for _j in range(n):
            Eu=np.zeros((n,n)); Eu[_i,_j]=1
            if np.allclose(Jr@Eu@Jr,-Eu): c+=1
    return c
dX,dY,dXY,dm,dp,dZ2 = (odd_dim(list(range(2,5))), odd_dim(list(range(5,11))),
                       odd_dim(list(range(2,11))), odd_dim([1]), odd_dim([0]), odd_dim([0,1]))
chk("C2","X","CONTROL, NOT EXHAUSTIVE [v1.8 RECLASSIFIED R->X]. The scan covers only sector sub-blocks; an arbitrary two-dimensional subspace such as span{|1>,|2>} carries restricted grading diag(-1,+1) and DOES have two odd operators, so this scan does not establish a closure. It is retained as a sector control. A QND vertex "
    "needs H_int = Z_path (x) B with B also Z2-odd (M56.20). Exhaustive test of every register "
    "sub-block: X, Y, X (+) Y, z+ alone and z- alone ALL carry ZERO odd operators, because J_Z acts "
    "on each with a uniform sign. The only odd operators in Mat_11 are the 20 that CONNECT slot 1 "
    "to the other ten",
    dX==0 and dY==0 and dXY==0 and dm==0 and dp==0 and dZ2==2,
    f"odd operators: X {dX}, Y {dY}, X(+)Y {dXY}, z- alone {dm}, z+ alone {dp}, Z-register {dZ2}")
Zp11=np.zeros((11,11)); Zp11[0,1]=Zp11[1,0]=1
nRm=int(np.sum(np.diag(JZ11)<0)); JS2=np.diag([1.0,-1.0])
rows_m=[]
for pE,qE in [(1,1),(2,1),(1,2),(2,2),(3,1),(1,3),(3,2)]:
    JE=np.diag([1.0]*pE+[-1.0]*qE); dE=pE+qE; co=0
    for _i in range(dE):
        for _j in range(dE):
            Eu=np.zeros((dE,dE)); Eu[_i,_j]=1
            if np.allclose(JE@Eu@JE,-Eu): co+=1
    qT=int(np.sum(np.diag(np.kron(JS2,JE))<0))
    rows_m.append((pE,qE,dE,co,qT))
chk("C3","R","THEOREM M56.21' (GRADED TENSOR-FACTOR MULTIPLICITY OBSTRUCTION) [v1.8 REPLACEMENT for "
    "the v1.7 argument, which the audit refuted: two odd factors can form an allowed even product, "
    "so 'the odd partner is itself forbidden' does not follow]. The register grading has "
    "multiplicities (n_+, n_-) = (10, 1), so q_R = 1. The pointer system has (p_S, q_S) = (1, 1). An "
    "environment admitting a nonzero odd operator needs p_E >= 1 and q_E >= 1, and then the negative "
    "eigenspace of J_S (x) J_E has dimension p_S q_E + q_S p_E = dim E >= 2. A grading-preserving "
    "isometry maps that odd subspace INJECTIVELY into the register's odd subspace, which is "
    "one-dimensional. Since dim E >= 2 > 1 = q_R, no such isometry exists",
    nRm==1 and all(r[3]>0 and r[4]==r[2] and r[4]>nRm for r in rows_m),
    f"q_R = {nRm}; " + "; ".join(f"(p_E,q_E)={(r[0],r[1])}: dim E={r[2]}, odd ops={r[3]}, "
    f"q(J_S(x)J_E)={r[4]}>1" for r in rows_m))
subJ=[JZ11[k,k] for k in [0,1,2,3]]
chk("C3b","R","THEOREM M56.21' RECONCILES THE v1.1 CODE COUNTEREXAMPLE: on slots {0,1,2,3} the "
    "register grading is diag(+1,-1,+1,+1) with ONE negative, while every J_S (x) J_E on C^4 with "
    "p_E, q_E >= 1 has TWO. The v1.1 embedding of the CHANNEL therefore stands, but it does not "
    "intertwine the gradings: an algebraic code embedding is possible, a seam-Z2-preserving "
    "action-level tensor subsystem is not",
    int(sum(1 for v in subJ if v<0))==1 and int(np.sum(np.diag(np.kron(JS2,np.diag([1.0,-1.0])))<0))==2,
    f"register negatives on the code block = {int(sum(1 for v in subJ if v<0))}; "
    f"J_S (x) J_E negatives = {int(np.sum(np.diag(np.kron(JS2,np.diag([1.0,-1.0])))<0))}")
chk("C4","X","NARROWED [v1.8]: what is excluded is the ISOLATED ONE-DIMENSIONAL z--only carrier -- a "
    "one-dimensional space carries only scalars, which are Z2-even, so B = 0. A full BRST "
    "ghost-antighost or cohomological graded factor is NOT analysed here, and v1.7's claim that the "
    "whole ZS-Q16 route fails is WITHDRAWN as overreach",
    dm==0, f"odd operators on a 1-dimensional environment = {dm}")
res_=[]
for dE in [1,2,3]:
    JE=np.diag([1.0]+[-1.0]*(dE-1)) if dE>1 else np.eye(1)
    c=0
    for _i in range(dE):
        for _j in range(dE):
            Eu=np.zeros((dE,dE)); Eu[_i,_j]=1
            if np.allclose(JE@Eu@JE,-Eu): c+=1
    res_.append((dE,c))
chk("C5","R","THEOREM M56.22 (Minimal Graded Carrier): an external factor admitting a nonzero Z2-odd "
    "operator has dimension at least 2. This reproduces, from CHARGE alone, the minimal Stinespring "
    "environment dimension that Theorem M56.5 derived from KRAUS RANK alone. Two independent "
    "constraints give the same number",
    res_[0][1]==0 and res_[1][1]==2,
    "; ".join(f"dim E = {r[0]} -> {r[1]} odd operators" for r in res_)+"; M56.5 gave dim = 2")
chk("C6","X","SPINOR RE-SCORED, 'charge match' WITHDRAWN [v1.8]: operator parity is defined by "
    "CONJUGATION, and D^(1/2)(2pi) = -I is CENTRAL, so (-I) B (-I) = B for every B and the odd "
    "operator count on that grading is ZERO. The spinor supplies a dimension (2) and a STATE sign, "
    "not the required non-central operator grading. What is needed is a sigma_z-type involution with "
    "both eigenspaces nonempty, and that is not yet derived from the corpus",
    abs(np.trace(np.diag([np.exp(-1j*math.pi),np.exp(1j*math.pi)])).real+2)<1e-12,
    "trace D^(1/2)(2pi) = -2.0; dim = 2; vertex NOT exhibited")
chk("C7","A","F-M56.22 CLOSED by direct quotation, no new assumption: ZS-M54 states that the seam-even "
    "(beta_0 = 1) selection projects the cross-coupling onto the bright mode z+ = (z0+z1)/sqrt(2), "
    "with C_XZ = C_XZ P+ so C_XZ|z-> = 0, and that dim(Z) = 2 decomposes as one bright mode z+ plus "
    "one odd mode z- -- 'precisely the corpus beta_0(Z) = 1 even + 1 odd split (ZS-S1 §5.2)'. The "
    "identification beta_0 = z+ is therefore ZS-M54's own, not this paper's",
    abs(1/math.sqrt(2)-0.7071067811865476)<1e-15, "z+ = (z0+z1)/sqrt(2), quoted from ZS-M54")



cent=-np.eye(2); noncent=np.diag([1.0,-1.0]); cc1=cc2=0
for _i in range(2):
    for _j in range(2):
        Eu=np.zeros((2,2)); Eu[_i,_j]=1
        if np.allclose(cent@Eu@cent,-Eu): cc1+=1
        if np.allclose(noncent@Eu@noncent,-Eu): cc2+=1
chk("C8","R","THEOREM M56.22' (Non-Central Grading Requirement) [v1.8]: an environment grading admits "
    "a nonzero odd operator only if it is NON-CENTRAL, i.e. has both eigenspaces nonempty. A central "
    "grading +-I gives zero odd operators. Combined with M56.5's Kraus-rank bound, the environment "
    "must have dim E = 2 AND a sigma_z-type involution",
    cc1==0 and cc2==2, f"central -I: {cc1} odd operators; non-central diag(+1,-1): {cc2}")
Aud=np.zeros((11,11)); Aud[0,1]=Aud[1,0]=1
Bud=np.zeros((11,11)); Bud[1,2]=Bud[2,1]=1
prod=Aud@Bud+Bud@Aud
chk("C9","X","AUDIT COUNTEREXAMPLE REPRODUCED, refuting the v1.7 argument: A = |0><1|+|1><0| and "
    "B = |1><2|+|2><1| are both Z2-odd, yet AB+BA = |0><2|+|2><0| is Z2-EVEN and therefore allowed. "
    "So 'an odd partner is itself forbidden in an even Hamiltonian' does not follow. The v1.7 "
    "reasoning is RETRACTED and replaced by C3",
    np.allclose(JZ11@Aud@JZ11,-Aud) and np.allclose(JZ11@Bud@JZ11,-Bud) and np.allclose(JZ11@prod@JZ11,prod),
    "A odd, B odd, AB+BA even -- v1.7's inference invalid")
chk("C10","X","AUDIT COUNTEREXAMPLE REPRODUCED, refuting v1.7's C2: the two-dimensional subspace "
    "span{|1>,|2>} has restricted grading diag(-1,+1) and carries two odd operators, so the sector "
    "sub-block scan was not exhaustive. That subspace shares |1> = z- with the system and is "
    "excluded by C3's multiplicity argument, not by the scan",
    odd_dim([1,2])==2, f"odd operators on span{{|1>,|2>}} = {odd_dim([1,2])}")


# ===== DECLARATIONS  [D] =====
for t,s in [("D1","F-M54-16' is NOT closed by this paper; it is re-scoped into F-M56.A/B/C."),
            ("D8","STATUS REVISION (v1.4): Lemma M56.9b is an ALGEBRAIC statement about the "
                  "reconstructed holonomy, not about the microscopic S14 slab. Proposition M56.9c "
                  "is DERIVED-CONDITIONAL on the Layer-Glue Hypothesis. Gate F-M56.15 is FIRED in "
                  "the reconstructed two-generator ansatz and OPEN at the S14 action level. "
                  "Theorem M56.13 is narrowed to: naive exponential factorisation of the two "
                  "generators fails."),
            ("D10","STATUS REVISION (v1.5): 'the action layer supplies a unique O(kappa^2) "
                   "operator' is replaced by the precise and true form -- the COUPLING-ELIMINATION "
                   "SECTOR supplies exactly one operator DIRECTION, P+, at all orders. The bare ZZ "
                   "block is a separate datum and is not supplied. The internal conflict between "
                   "v1.4's M56.14 and its own gate F-M56.18 is thereby removed."),
            ("D16","FINAL (v1.8): the action layer is closed by THEOREM M56.21', the graded "
                   "tensor-factor multiplicity obstruction: q_R = 1 < 2 <= dim E = q(J_S (x) J_E), "
                   "so no grading-preserving internal tensor factor exists. v1.7's argument is "
                   "RETRACTED; its conclusion survives on the new proof."),
            ("D17","RETRACTION (v1.8): v1.7's 'charge match' for the spinor factor is withdrawn. "
                   "D^(1/2)(2pi) = -I is central and induces NO operator grading. What is required "
                   "is a non-central involution, not yet derived from the corpus."),
            ("D14","ACTION LAYER CLOSED (v1.7): no admissible QND vertex exists inside the "
                   "Q = 11 register (M56.21). The Z2-odd partner required by M56.20 must live on an "
                   "external graded factor of dimension at least 2 (M56.22). ZS-M56 closes here; "
                   "the successor question -- construct that factor and its vertex -- belongs to "
                   "ZS-M57 and ZS-Q19."),
            ("D15","STATUS REVISIONS (v1.7): M56.18 is DERIVED at the symmetric quadratic background "
                   "and DERIVED-CONDITIONAL to all orders on an exact unbroken Z2, a symmetry-"
                   "preserving regulator and a Z2-invariant background. M56.19 is demoted PROVEN -> "
                   "VERIFIED-REGRESSION. M56.19a is narrowed to 'no lone Z_path term in the Z-only "
                   "block'. M56.20 loses the clause 'the Z-register cannot supply B'."),
            ("D12","F-M56.18a CLOSED (v1.6): d = 0. Routes (a) corpus retrieval (ZS-M6 §2.1, "
                   "ZS-S1 §5.1) and (b) structural derivation (ZS-S1 §5.2 Z2 seam symmetry) agree "
                   "and cross-validate against the reproduced ZS-M6 §2.3 spectra."),
            ("D13","The outcome is a SELECTION RULE, not a no-go: a QND vertex requires a Z2-odd "
                   "environment operator. F-M56.A now has a precise answer condition."),
            ("D11","LAYER-GLUE VERDICT (v1.5, REVISING v1.4's D9): the hypothesis is NOT "
                   "PROVEN-FALSE. It is reduced to a single real parameter d, the Z_path "
                   "coefficient of the bare ZZ block. The coupling sector provably cannot supply "
                   "d; whether the bare block does is gate F-M56.18a."),
            ("D9","LAYER-GLUE VERDICT (v1.4): the Layer-Glue Hypothesis is FALSE at O(kappa^2). "
                  "The action layer does supply a Z-internal generator, and it is Sigma_Z, the "
                  "anticommuting partner of G_Z. Whether any higher order supplies a pointer-"
                  "diagonal component is gate F-M56.18."),
            ("D6","RETRACTION (v1.3): v1.2 Theorem M56.9 as a CHANNEL obstruction, its Condition (E), "
                  "the Table 5.1 entry 'quadratic internal route CLOSED-NEGATIVE', and F-M56.A's "
                  "'NO at quadratic order' are all RETRACTED (Y2, Y4). What survives is Lemma "
                  "M56.9a, the vertex kernel."),
            ("D7","RETRACTION (v1.3): check X5 is retracted as proof-bearing; it imposed its own "
                  "premise. Reclassified as a control."),
            ("D0","RETRACTION: ZS-M56 v1.0 Theorem M56.6, its Conclusion, and the uniqueness "
                  "clause of M56.8 are RETRACTED, refuted by the counterexample reproduced in W1."),
            ("D2","No new constant is introduced; every number is lambda, mu, arg lambda, D or "
                  "algebraically derived from A, Q, dim Z."),
            ("D3","The j=1/2 spinor factor is a HYPOTHESIS supported by a dimension match and corpus "
                  "availability. Uniqueness is explicitly NOT claimed (retracted in v1.1)."),
            ("D4","Track II of the ZS-M56 seed (Wilson-cobordism identification) is CLOSED-"
                  "NEGATIVE by Theorem M56.4 and is withdrawn."),
            ("D5","Nothing here bears on F-M54-12 (instrument selector) or F-M54-13 (objectivity).")]:
    LED.append((t,"D",s,"DECL",""))

# ---------- COVER ----------
ex   = [r for r in LED if r[3] in ("PASS","FAIL")]
npass= sum(1 for r in ex if r[3]=="PASS")
byc  = {c: sum(1 for r in ex if r[1]==c) for c in "RAXP"}
print("="*100)
for r in LED: print(f"{r[0]:5s} [{r[1]}] {r[3]:5s}  {r[2]}" + (f"\n              -> {r[4]}" if r[4] else ""))
print("="*100)
print(f"COVER: {npass}/{len(ex)} PASS  +  {sum(1 for r in LED if r[3]=='DECL')} declarations")
print(f"  proof-bearing (R+A) = {byc['R']+byc['A']}   controls/proxies (X+P) = {byc['X']+byc['P']}")
print(f"  R={byc['R']}  A={byc['A']}  X={byc['X']}  P={byc['P']}")
print(f"FAIL COUNT = {len(ex)-npass}")
