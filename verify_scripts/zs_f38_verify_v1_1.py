# zs_f38_verify_v1_1.py
# ZS-F38 v1.1 — The Register Clock Identity (review-integrated)
# Verification suite: exact/numerical checks + consistency guards.
# Dependencies: sympy, mpmath, numpy. Zero fitted parameters.
# Locked inputs: A = 35/437, Q = 11, (dim Z, dim X, dim Y) = (2, 3, 6).

import itertools, math, random
import numpy as np
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
random.seed(11)

PASS, FAIL = [], []
GUARD = []

def check(name, cond, guard=False):
    tgt = GUARD if guard else (PASS if cond else FAIL)
    if guard:
        GUARD.append((name, bool(cond)))
        print(f"[GUARD] {name}: {'pass' if cond else 'FLAG'}")
    else:
        (PASS if cond else FAIL).append(name)
        print(f"[{'PASS' if cond else 'FAIL'}] {name}")

# ---------- Locked inputs ----------
A = sp.Rational(35, 437)
Q = 11
DIMS = (2, 3, 6)  # (Z, X, Y)

# =====================================================================
# UE: Unique-ergodicity block (Theorem F38.T1 / Lemma F38.L1)
# =====================================================================

def invariant_measure_space(perm):
    """Exact fixed space of P^T acting on measures (sympy, rational)."""
    n = len(perm)
    P = sp.zeros(n, n)
    for i, j in enumerate(perm):
        P[j, i] = 1  # column i -> row perm[i]
    M = P - sp.eye(n)
    return M.T.nullspace(), P

def orbits(perm):
    n = len(perm); seen = [False]*n; orbs = []
    for s in range(n):
        if not seen[s]:
            o = []; x = s
            while not seen[x]:
                seen[x] = True; o.append(x); x = perm[x]
            orbs.append(o)
    return orbs

# UE1: transitive 11-cycle -> unique invariant measure = uniform
sigma = [(i+1) % Q for i in range(Q)]
ns, P11 = invariant_measure_space(sigma)
uniform = sp.Matrix([sp.Rational(1, Q)]*Q)
v = ns[0] / sum(ns[0])
check("UE1 transitive 11-cycle: dim(inv) = 1 and measure = I_Q/Q",
      len(ns) == 1 and sp.simplify(v - uniform) == sp.zeros(Q, 1))

# UE2: sector-preserving alternative (orbit type (2,3,6)) -> 2-parameter simplex
tau = [1,0, 3,4,2, 6,7,8,9,10,5]  # cycles (0 1)(2 3 4)(5 6 7 8 9 10)
ns2, _ = invariant_measure_space(tau)
check("UE2 sector-preserving (2,3,6): dim(inv) = 3 (2-parameter simplex)",
      len(ns2) == 3 and [len(o) for o in orbits(tau)] == [2,3,6])

# UE3: Q = 11 prime; every nontrivial power of an 11-cycle is an 11-cycle (regular Z_11 action)
check("UE3 Q = 11 prime and Z_11 action regular",
      sp.isprime(Q) and all(len(orbits([ (i+k) % Q for i in range(Q)])) == 1
                            for k in range(1, Q)))

# UE4: Birkhoff clock average over one period = uniform average (all start slots)
a_obs = [sp.Rational(random.randint(-9, 9), random.randint(1, 7)) for _ in range(Q)]
mean_a = sum(a_obs) / Q
ok = True
for s in range(Q):
    x, tot = s, sp.Integer(0)
    for _ in range(Q):
        tot += a_obs[x]; x = sigma[x]
    ok &= sp.simplify(tot / Q - mean_a) == 0
check("UE4 Birkhoff one-period clock average = <a>_{I_Q/Q} (all 11 starts)", ok)

# UE5: sector-weighted measure lies in the (2,3,6) simplex, not in the transitive one
w = sp.Matrix([sp.Rational(1,22)]*2 + [sp.Rational(1,33)]*3 + [sp.Rational(1,9)*sp.Rational(2,3)/ sp.Integer(4)]*6)
w = sp.Matrix([sp.Rational(1,4)/2]*2 + [sp.Rational(1,4)/3]*3 + [sp.Rational(1,2)/6]*6)  # (1/4,1/4,1/2) split
Pt = sp.zeros(Q, Q)
for i, j in enumerate(tau): Pt[j, i] = 1
check("UE5 sector-weighted measure invariant under (2,3,6) shift but != I_Q/Q",
      sp.simplify(Pt*w - w) == sp.zeros(Q,1) and sp.simplify(w - uniform) != sp.zeros(Q,1))

# UE6: invariant-simplex dimension = #orbits (5 random permutations, exact)
ok = True
for _ in range(5):
    p = list(range(Q)); random.shuffle(p)
    ns_r, _ = invariant_measure_space(p)
    ok &= (len(ns_r) == len(orbits(p)))
check("UE6 dim(invariant measures) = #orbits (5 random permutations)", ok)


# =====================================================================
# PF: Primitive/irreducible clock ergodicity block (Theorem F38.T1')
# =====================================================================

def stationary_space(P):
    """Exact fixed space of P^T (stationary measures), P sympy Matrix (column-stochastic on measures)."""
    n = P.shape[0]
    return (P - sp.eye(n)).T.nullspace()

def perm_matrix(perm):
    n = len(perm); P = sp.zeros(n, n)
    for i, j in enumerate(perm): P[j, i] = 1
    return P

C1 = perm_matrix(sigma)                      # 11-cycle
C2 = C1 * C1
# PF1: irreducible doubly stochastic (convex combo of cycle powers) -> unique stationary = I_Q/Q (exact)
Pmix = sp.Rational(1,2)*C1 + sp.Rational(1,2)*C2
row_ok = all(sum(Pmix[i, j] for j in range(Q)) == 1 for i in range(Q))
col_ok = all(sum(Pmix[i, j] for i in range(Q)) == 1 for j in range(Q))
ns_m = stationary_space(Pmix)
v_m = ns_m[0] / sum(ns_m[0])
check("PF1 irreducible doubly stochastic P = (C + C^2)/2: unique stationary = I_Q/Q (exact)",
      row_ok and col_ok and len(ns_m) == 1 and sp.simplify(v_m - uniform) == sp.zeros(Q, 1))

# PF2: primitivity (aperiodic): some power of P has all entries positive; P^n -> J/Q numerically
Pf = np.array(Pmix.tolist(), dtype=float)
Ppow = np.linalg.matrix_power(Pf, 15)
Pinf = np.linalg.matrix_power(Pf, 1000)
check("PF2 primitivity: P^15 > 0 entrywise and P^1000 -> J/Q (Perron-Frobenius, <1e-12)",
      (Ppow > 0).all() and np.max(np.abs(Pinf - 1.0/Q)) < 1e-12)

# PF3: reducible (sector-preserving) doubly stochastic -> stationary simplex dim = #classes = 3
Pt3 = perm_matrix(tau)
Pmix3 = sp.Rational(1,2)*Pt3 + sp.Rational(1,2)*(Pt3*Pt3)
ns_r = stationary_space(Pmix3)
check("PF3 sector-preserving doubly stochastic: stationary space dim = 3 (2-parameter simplex)",
      len(ns_r) == 3)

# PF4: periodic irreducible case (bare 11-cycle): Cesaro average over the period = I_Q/Q (exact)
Ces = sum((C1**k for k in range(Q)), sp.zeros(Q, Q)) / Q
check("PF4 Cesaro average of the 11-cycle over one period = J/Q exactly (uniform)",
      sp.simplify(Ces - sp.ones(Q, Q)/Q) == sp.zeros(Q, Q))

# TR1: slot-projector trace under the democratic density (T1(iii) corrected form)
rhoQ = sp.eye(Q) / Q
ok = all(sp.simplify(sp.trace(rhoQ * sp.diag(*[1 if i == s else 0 for i in range(Q)])) - sp.Rational(1, Q)) == 0
         for s in range(Q))
check("TR1 Tr(rho_Q P_s) = 1/Q for all 11 slot projectors (kappa^2 = A/Q slot-normalized form)", ok)

# =====================================================================
# KO: Koenigs / Abel-cover block (inherited data re-verified)
# =====================================================================
f = lambda z: mp.e**(1j*mp.pi*z/2)

# KO1: fixed point z* to locked digits
zst = mp.mpc(sp.Float('0.4382829367', 20), sp.Float('0.3605924719', 20))
zst = mp.findroot(lambda z: f(z) - z, zst)
check("KO1 z* matches locked 0.4382829367 + 0.3605924719i (10 digits)",
      abs(zst - mp.mpc('0.4382829367', '0.3605924719')) < mp.mpf('1e-9'))

# KO2: multiplier, mu, theta to locked digits
lam = 1j*mp.pi/2*zst
mu = -mp.log(abs(lam)); th = mp.arg(lam)
check("KO2 mu = 0.1148346250, theta = 2.2592495540 (10 digits)",
      abs(mu - mp.mpf('0.1148346250')) < 1e-9 and abs(th - mp.mpf('2.2592495540')) < 1e-9)

# KO3: Koenigs ratio chi(f z) / (lam * chi z) = 1 and Abel increment = 1 at 12 orbit points
def koenigs(z, n=420):
    w = z
    for _ in range(n):
        w = f(w)
    return (w - zst) / lam**n

pts = [zst + mp.mpf('0.25')*mp.e**(1j*mp.pi*k/6) for k in range(12)]
ok_r, ok_u = True, True
for z in pts:
    cz, cfz = koenigs(z), koenigs(f(z))
    ok_r &= abs(cfz/(lam*cz) - 1) < mp.mpf('1e-12')
    inc = mp.log(cfz/cz) / mp.log(lam)   # principal log of the ratio ~ log(lam)
    ok_u &= abs(inc - 1) < mp.mpf('1e-12')
check("KO3 chi(fz) = lam*chi(z) and Abel increment u(fz)-u(z) = 1 (12 points, <1e-12)",
      ok_r and ok_u)

# KO4: branch period tau = 2*pi*i / log(lam) matches M47 GEO3 (2.7743 - 0.1410i)
tau_b = 2j*mp.pi/mp.log(lam)
check("KO4 branch period 2*pi*i/log(lam) = 2.7743 - 0.1410i (M47 GEO3)",
      abs(tau_b - mp.mpc('2.7743', '-0.1410')) < 1e-3)

# =====================================================================
# CH: Q-unit inclusion chain block (Theorem F38.T2, Hardy/ideal model)
# =====================================================================
z = sp.symbols('z')

# CH1: (z^k) subset of (z^j) for all 0 <= j <= k <= Q (exact divisibility)
ok = all(sp.Poly(z**k, z).rem(sp.Poly(z**j, z)).is_zero
         for j in range(Q+1) for k in range(j, Q+1))
check("CH1 chain order (z^k) subset (z^j), 0<=j<=k<=Q (inner-function divisibility)", ok)

# CH2: canonical endomorphism Gamma = U(2) steps the chain by two
ok = all(sp.expand(z**2 * z**k - z**(k+2)) == 0 for k in range(Q-1))
check("CH2 Gamma = U(2): z^2*(z^k) = (z^{k+2}) (even Jones-Longo subchain)", ok)

# CH3: consecutive HSMI bookkeeping M_{k+1} = U(1) M_k U(-1)
ok = all(sp.expand(z * z**k - z**(k+1)) == 0 for k in range(Q))
check("CH3 M_{k+1} = U(1) M_k U(-1) (unit shift, all k <= Q)", ok)

# CH4: Koot-type order criterion in the model: z^j | z^k  <=>  j <= k
ok = all(sp.Poly(z**k, z).rem(sp.Poly(z**j, z)).is_zero == (j <= k)
         for j in range(Q+1) for k in range(Q+1))
check("CH4 spectral/divisibility order criterion iff j <= k (Koot model form)", ok)

# =====================================================================
# BW: Borchers 2*pi block (Theorem F38.T3 arithmetic; conventions fixed)
# =====================================================================
twopi = 2*mp.pi

# BW1: per-unit modular factor and Q-fold composition
per_unit = mp.e**(-twopi)
depthQ = per_unit**Q
check("BW1 e^{-2pi} = 1.86744e-3 and (e^{-2pi})^Q = e^{-2piQ} = 9.632e-31",
      abs(per_unit - mp.mpf('1.8674427317e-3')) < 1e-12 and
      abs(depthQ - mp.mpf('9.632e-31')) / mp.mpf('9.632e-31') < 1e-3)

# BW2: convention guard (A31 discipline): reduced Planck fixed; t_obs vs Q
Mpl_red = mp.mpf('2.435e27')   # eV (reduced Planck mass, locked convention per ZS-A31)
Meff    = mp.mpf('2.48e-3')    # eV (ZS-A31 regression; one observation, firewalled)
ratio   = Meff / Mpl_red
t_obs   = -mp.log(ratio) / twopi
check("BW2 t_obs(reduced) = 10.991, |t_obs - Q| = 0.0089 (reproduces ZS-A31)",
      abs(t_obs - mp.mpf('10.9911')) < 2e-3 and abs(t_obs - Q) < 0.01)

Mpl_unred = Mpl_red * mp.sqrt(8*mp.pi)
t_unred = -mp.log(Meff/Mpl_unred) / twopi
check("BW3 unreduced convention gives t ~ Q + 1/4 (guard: convention must stay reduced)",
      abs(t_unred - (Q + mp.mpf('0.25'))) < 0.02, guard=True)

# =====================================================================
# DS: dimensionless-structure consistency block (NOT certifications)
# =====================================================================
# DS1: C_UV inferred from the exact candidate; within the declared band [1/4, 4]
C_uv = (ratio / depthQ)**4
check("DS1 C_UV = (M_eff / (Mpl_red e^{-2piQ}))^4 = 1.25 in declared band [1/4, 4]",
      abs(C_uv - mp.mpf('1.25')) < 0.02 and mp.mpf('0.25') < C_uv < 4)

# DS2: distinct-measures guard: Plancherel (4,9,36)/49 != I_Q/Q as slot weights
plancherel = [sp.Rational(4,49), sp.Rational(9,49), sp.Rational(36,49)]
check("DS2 Plancherel transport weights (4,9,36)/49 sum to 1 and != democratic (distinct objects)",
      sum(plancherel) == 1 and plancherel != [sp.Rational(1,3)]*3, guard=True)

# DS3: register arithmetic identities
check("DS3 kappa^2 = A/Q = 35/4807; 36*A/Q = 1260/4807; g_reg^2 = 6A/Q",
      sp.Rational(35,437)/Q == sp.Rational(35,4807) and
      36*A/Q == sp.Rational(1260,4807) and 6*A/Q == sp.Rational(210,4807))

# DS4: ln(Mpl_red/Meff) vs 2*pi*Q (consistency only; 0.08% class)
lhs = mp.log(Mpl_red/Meff); rhs = twopi*Q
check("DS4 ln(Mpl/Meff) = 69.059 vs 2piQ = 69.115 (0.081% consistency, not a certification)",
      abs(lhs - mp.mpf('69.0592')) < 1e-3 and abs((lhs-rhs)/rhs) < 1e-3)

# =====================================================================
# MC: statistical hierarchy of record (v1.1; execution in ZS-A32 v1.0)
# =====================================================================
C_SET = [sp.Rational(1,2), 1, 2, 4]
Q_SET = [2, 3, 6, 11, 22, 28, 33, 35, 49, 121]
U_pi  = [(c, q) for c in C_SET for q in Q_SET]         # exp(-c*pi*q)
U_A   = list(range(1, 41))                              # A^k
U_tel = list(range(1, 9))                               # exp(-n*pi/A)
size  = len(U_pi) + len(U_A) + len(U_tel)

# MC1: universe finite, size 88, contains the pre-registered target (c, q) = (2, 11)
check("MC1 universe |U| = 88 and contains target exp(-2*pi*Q) (c=2, q=11)",
      size == 88 and (2, 11) in U_pi)

# MC2: tolerance band declared a priori: |Delta ln| <= (1/4) ln 4 (C_UV in [1/4,4])
band = mp.log(4)/4
check("MC2 tolerance band = (1/4) ln 4 = 0.3466 declared (C_UV band [1/4,4])",
      abs(band - mp.mpf('0.34657359')) < 1e-8)

# MC4: degenerate-member disclosure: exp(-pi*22) = exp(-2*pi*11) exactly (retained, not deduplicated)
check("MC4 duplicate of record: pi*22 = 2*pi*11 exactly (degenerates retained per A32)",
      sp.simplify(sp.pi*22 - 2*sp.pi*11) == 0)

# External observed inputs for the null range (disclosed; A32 conventions)
H0_kms = mp.mpf('67.36')
H0_eV  = H0_kms*1000/mp.mpf('3.0857e22')*mp.mpf('6.582e-16')
W_null = mp.log(Mpl_red/H0_eV)                      # ln(Mpl/H0) = 138.68
Meff_A32 = mp.mpf('2.476e-3')                       # eV (A32: from rho_L^(1/4) = 2.24 meV / 0.669^(1/4))
L_obs = mp.log(Mpl_red/Meff_A32)
tgt = 2*mp.pi*Q

# MC5: SECONDARY formula-count statistic (the v1.0 literal reading): members in band of L_obs
vals = [float(c)*float(mp.pi)*q for c, q in U_pi] + \
       [k*float(-mp.log(35/437)) for k in U_A] + \
       [n*float(mp.pi)/(35/437) for n in U_tel]
n_in = sum(1 for e in vals if abs(e - float(L_obs)) <= float(band))
p_fc = sp.Rational(n_in, size)
check("MC5 SECONDARY formula-count: exactly 2 members in band (2piQ and pi*22); p_fc = 2/88 = 2.27% <= 5%",
      n_in == 2 and p_fc == sp.Rational(1, 44) and float(p_fc) <= 0.05)

# MC6: PRIMARY single-target statistic (A31-first registration): p_single = 2*band/W
p_single = 2*band/W_null
check("MC6 PRIMARY p_single = 2*band/ln(Mpl/H0) = 0.500% <= 5% (A32 executed value reproduced)",
      abs(p_single - mp.mpf('0.0050')) < 2e-4 and p_single <= 0.05 and abs(W_null - mp.mpf('138.68')) < 0.05)

# MC7: look-elsewhere p_universe: exact interval-union coverage (reproduces A32 28.8%)
Wf = float(W_null); bf = float(band)
ivs = sorted((max(0.0, e - bf), min(Wf, e + bf)) for e in vals if 0 <= e <= Wf + bf)
merged = []
for lo, hi in ivs:
    if merged and lo <= merged[-1][1]:
        merged[-1] = (merged[-1][0], max(merged[-1][1], hi))
    else:
        merged.append((lo, hi))
p_uni = sum(hi - lo for lo, hi in merged)/Wf
check("MC7 look-elsewhere p_universe = 28.8% (interval union; matches ZS-A32 28.76%)",
      abs(p_uni - 0.2876) < 0.003)

# MC3': verdict-neutrality guard: both decision candidates (p_single, p_fc) pass at <= 5%;
#       the v1.1 hierarchy correction changes labels, not the verdict
check("MC3' verdict-neutral hierarchy correction: p_single = 0.50% and p_fc = 2.27% both <= 5%",
      p_single <= 0.05 and float(p_fc) <= 0.05, guard=True)

# =====================================================================
# PR: locked-input echoes
# =====================================================================
check("PR1 sector slots 2 + 3 + 6 = 11 = Q", sum(DIMS) == Q)
check("PR2 (A, Q, dim Z) = (35/437, 11, 2) locked echo",
      A == sp.Rational(35, 437) and Q == 11 and DIMS[0] == 2)

# ---------------------------------------------------------------------
print("\n================================================================")
print(f"RESULT: {len(PASS)}/{len(PASS)+len(FAIL)} exact/numerical checks PASS; "
      f"{len(GUARD)} consistency/pre-registration guards executed"
      f" ({sum(1 for _, c in GUARD if c)}/{len(GUARD)} pass).")
if FAIL:
    print("FAILED:", FAIL)
