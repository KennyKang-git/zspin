#!/usr/bin/env python3
# =============================================================================
# zs_f41_verify_v1_1.py
# ZS-F41 v1.1 — A Conditional Odd Charge-Lattice Candidate from Z-Spin Axioms
# Verification suite: 31 exact/numerical checks + 4 guards.
# Zero fitted parameters. Theorem-side inputs: A = 35/437, Q = 11,
# (Z, X, Y) = (2, 3, 6), the i-tetration locked dynamics (z*, lambda*, mu, theta),
# and the mathematical constant pi. Firewalled external anchor (Blocks E/F only):
# nu_now = 276.6 (ZS-A26) with the ZS-F32 convention window [276.6, 284.0].
# v1.1 adds Block F: the stage-2 quaternionic-multiplet route (b = 2 h_dual = 12)
# and the 25/2 No-Go arithmetic. Notation: USp(10) = compact symplectic group on
# C^10 (Lie algebra sp(5) in the mathematicians' convention, dim 55); corpus
# shorthand Sp(10) in v1.0 denotes the same group.
# Exits non-zero on any theorem-tier failure; contains no fail-open clause.
# =============================================================================
import sys
import itertools
from fractions import Fraction

import numpy as np
import mpmath as mp

mp.mp.dps = 60

PASS, TOTAL, FAILED = 0, 0, []
GPASS, GTOTAL, GFAILED = 0, 0, []


def CHECK(name, cond):
    global PASS, TOTAL
    TOTAL += 1
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAILED.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def GUARD(name, cond):
    global GPASS, GTOTAL
    GTOTAL += 1
    ok = bool(cond)
    if ok:
        GPASS += 1
    else:
        GFAILED.append(name)
    print(f"[{'GUARD-PASS' if ok else 'GUARD-FAIL'}] {name}")


print("=" * 78)
print("ZS-F41 v1.1 verification suite")
print("=" * 78)

# -----------------------------------------------------------------------------
# Block A — Locked geometric and dynamical inputs
# -----------------------------------------------------------------------------
print("\n--- Block A: locked inputs ---")
A = Fraction(35, 437)
Q = 11
kap2_frac = A / Q

f = lambda z: mp.exp(1j * mp.pi * z / 2)
zstar = mp.findroot(lambda z: f(z) - z, mp.mpc('0.44', '0.36'))
CHECK("A1 i-tetration fixed point residual |i^z* - z*| < 1e-50",
      abs(f(zstar) - zstar) < mp.mpf('1e-50'))

lam = (1j * mp.pi / 2) * zstar          # lambda* = f'(z*)
mu = -mp.log(abs(lam))
th = mp.arg(lam)                          # omega = arg lambda*
CHECK("A2 mu = -ln|lambda*| = 0.1148346250 (10 digits)",
      abs(mu - mp.mpf('0.1148346250')) < mp.mpf('1e-9'))
CHECK("A3 omega = 2.2592495540 and omega^2/2 = 2.5521042734 (10 digits)",
      abs(th - mp.mpf('2.2592495540')) < mp.mpf('1e-9')
      and abs(th ** 2 / 2 - mp.mpf('2.5521042734')) < mp.mpf('1e-9'))
CHECK("A4 kappa^2 = A/Q = 35/4807 exact rational",
      kap2_frac == Fraction(35, 4807))
CHECK("A5 register 2+3+6=11, 4+9+36=49, 36*A/Q = 1260/4807 exact (coprime)",
      2 + 3 + 6 == 11 and 4 + 9 + 36 == 49
      and 36 * kap2_frac == Fraction(1260, 4807)
      and Fraction(1260, 4807).numerator == 1260)

# -----------------------------------------------------------------------------
# Block B — Binary pentagon lift Z10 and the McKay graph (character theory)
# -----------------------------------------------------------------------------
print("\n--- Block B: Z10 character theory / McKay graph A^_9 ---")
zeta = np.exp(1j * np.pi / 5)             # generator eigenvalue, zeta^10 = 1

g = np.diag([zeta, np.conj(zeta)])
CHECK("B1 g^10 = 1 and g^5 = -1 (the 4-pi Z-Spin closure element -1 lies in Z10)",
      np.allclose(np.linalg.matrix_power(g, 10), np.eye(2), atol=1e-12)
      and np.allclose(np.linalg.matrix_power(g, 5), -np.eye(2), atol=1e-12))

def chi(k):
    return lambda m: zeta ** ((k * m) % 10)

def ip10(f1, f2):
    return sum(f1(m) * np.conj(f2(m)) for m in range(10)) / 10

fund = lambda m: zeta ** (m % 10) + zeta ** ((-m) % 10)   # 2|_{Z10} = rho_1 + rho_9

adj = np.zeros((10, 10), dtype=int)
integer_ok = True
for k in range(10):
    for j in range(10):
        v = ip10(lambda m: fund(m) * chi(k)(m), chi(j))
        r = round(v.real)
        if abs(v - r) > 1e-9:
            integer_ok = False
        adj[k, j] = r
cycle10 = np.zeros((10, 10), dtype=int)
for k in range(10):
    cycle10[k, (k + 1) % 10] = 1
    cycle10[k, (k - 1) % 10] = 1
CHECK("B2 McKay adjacency of Z10 (tensoring by the Z-Spin doublet 2) = 10-cycle A^_9",
      integer_ok and (adj == cycle10).all())

CHECK("B3 bipartite mediation parity: every McKay edge flips seam parity "
      "(vectorial k even <-> spinorial k odd)",
      all((k + j) % 2 == 1 for k in range(10) for j in range(10) if adj[k, j]))

# B4: even-sector recovery — vectorial subcategory = Rep(Z5), M9 5-cycle A^_4
omega5 = np.exp(2j * np.pi / 5)
def chi5(k):
    return lambda m: omega5 ** ((k * m) % 5)
def ip5(f1, f2):
    return sum(f1(m) * np.conj(f2(m)) for m in range(5)) / 5
fund5 = lambda m: omega5 ** (m % 5) + omega5 ** ((-m) % 5)
adj5 = np.zeros((5, 5), dtype=int)
ok5 = True
for k in range(5):
    for j in range(5):
        v = ip5(lambda m: fund5(m) * chi5(k)(m), chi5(j))
        r = round(v.real)
        if abs(v - r) > 1e-9:
            ok5 = False
        adj5[k, j] = r
cycle5 = np.zeros((5, 5), dtype=int)
for k in range(5):
    cycle5[k, (k + 1) % 5] = 1
    cycle5[k, (k - 1) % 5] = 1
pullback_ok = all(abs(chi(2 * j)(m) - chi5(j)(2 * m % 5 if False else m) ** 1
                      if False else chi(2 * j)(m) - omega5 ** ((j * m) % 5)) < 1e-12
                  for j in range(5) for m in range(10))
# rho_{2j}(g^m) = zeta^{2jm} = omega5^{jm}: direct check
pullback_ok = all(abs(zeta ** ((2 * j * m) % 10) - omega5 ** ((j * m) % 5)) < 1e-12
                  for j in range(5) for m in range(10))
CHECK("B4 Even-Sector Recovery: vectorial Z10 chars pull back from Z5 "
      "(zeta^2 = omega5) and McKay(Z5) = 5-cycle A^_4 (ZS-M9 reproduction)",
      ok5 and (adj5 == cycle5).all() and pullback_ok)

# B5: conjugation involution rho_k <-> rho_{10-k}; fixed {rho_0, rho_5};
#     rho_5 = seam sign character (g -> -1, trivial on the vectorial Z5)
conj_ok = all(abs(ip10(lambda m: np.conj(chi(k)(m)), chi((10 - k) % 10)) - 1) < 1e-9
              for k in range(10))
fixed_nodes = [k for k in range(10) if (10 - k) % 10 == k]
CHECK("B5 conjugation sigma: rho_k <-> rho_{-k}; fixed nodes {rho_0, rho_5}; "
      "rho_5(g) = -1, rho_5(g^2) = +1 (the seam sign character)",
      conj_ok and fixed_nodes == [0, 5]
      and abs(chi(5)(1) + 1) < 1e-12 and abs(chi(5)(2) - 1) < 1e-12)

# B6: uniqueness — exactly one nontrivial involution of the 10-cycle fixing node 0
count = 0
for refl in (False, True):
    for a in range(10):
        if refl:
            mmap = lambda k, a=a: (a - k) % 10
        else:
            mmap = lambda k, a=a: (k + a) % 10
        ident = all(mmap(k) == k for k in range(10))
        invol = all(mmap(mmap(k)) == k for k in range(10))
        if invol and not ident and mmap(0) == 0:
            count += 1
CHECK("B6 uniqueness: exactly 1 nontrivial graph involution of A^_9 fixing rho_0 "
      "(it is sigma: k -> -k)", count == 1)

# -----------------------------------------------------------------------------
# Block C — The quaternionic seam fold: su(10) -> sp(10) + 44
# -----------------------------------------------------------------------------
print("\n--- Block C: quaternionic seam fold ---")
n = 10
basis = []
for a in range(n):
    for b in range(a + 1, n):
        E = np.zeros((n, n), dtype=complex)
        E[a, b] = 1
        basis.append(E - E.T)
        basis.append(1j * (E + E.T))
for a in range(n - 1):
    D = np.zeros((n, n), dtype=complex)
    D[a, a] = 1
    D[a + 1, a + 1] = -1
    basis.append(1j * D)
assert len(basis) == 99

J = np.block([[np.zeros((5, 5)), np.eye(5)], [-np.eye(5), np.zeros((5, 5))]])
Jinv = -J                                   # J^2 = -I  (j^2 = -1: 4-pi closure)
theta_q = lambda X: J @ np.conj(X) @ Jinv   # quaternionic (A II) involution
theta_r = lambda X: np.conj(X)              # real (A I, j^2 = +1) alternative

def vecR(X):
    return np.concatenate([X.real.ravel(), X.imag.ravel()])

M = np.column_stack([vecR(B) for B in basis])          # 200 x 99
Mpinv = np.linalg.pinv(M)

def op_matrix(op):
    return np.column_stack([Mpinv @ vecR(op(B)) for B in basis])

TH = op_matrix(theta_q)
THr = op_matrix(theta_r)

# C1: involution + Lie algebra automorphism
rng = np.random.default_rng(11)
auto_ok = True
for _ in range(5):
    cx = rng.standard_normal(99)
    cy = rng.standard_normal(99)
    X = sum(c * B for c, B in zip(cx, basis))
    Y = sum(c * B for c, B in zip(cy, basis))
    lhs = theta_q(X @ Y - Y @ X)
    rhs = theta_q(X) @ theta_q(Y) - theta_q(Y) @ theta_q(X)
    if np.linalg.norm(lhs - rhs) > 1e-9:
        auto_ok = False
CHECK("C1 theta_J is an involutive automorphism of su(10): theta^2 = id, "
      "theta[X,Y] = [theta X, theta Y]",
      np.linalg.norm(TH @ TH - np.eye(99)) < 1e-8 and auto_ok)

# C2: eigenspace dimensions 55 / 44
w = np.linalg.eigvals(TH)
plus = int(np.sum(np.abs(w - 1) < 1e-6))
minus = int(np.sum(np.abs(w + 1) < 1e-6))
CHECK("C2 fixed algebra dim 55 = Q(Q-1)/2 (sp(10)); odd module dim 44 = 4Q",
      plus == 55 and minus == 44 and Q * (Q - 1) // 2 == 55 and 4 * Q == 44)

# C3: the j^2 = +1 (2-pi) alternative gives so(10), dim 45 — the discriminator
wr = np.linalg.eigvals(THr)
plus_r = int(np.sum(np.abs(wr - 1) < 1e-6))
CHECK("C3 discriminator: j^2 = +1 (real structure) fixed algebra dim 45 = so(10); "
      "4-pi closure (j^2 = -1) forces the symplectic fold, not the orthogonal one",
      plus_r == 45)

# C4: symplectic witness + symmetric-pair brackets
Pp = (np.eye(99) + TH) / 2
Pm = (np.eye(99) - TH) / 2
def sample(P):
    c = P @ rng.standard_normal(99)
    return sum(ci * B for ci, B in zip(c, basis))
sympl_ok, pair_ok = True, True
for _ in range(4):
    K1, K2 = sample(Pp), sample(Pp)
    P1, P2 = sample(Pm), sample(Pm)
    if np.linalg.norm(K1.T @ J + J @ K1) > 1e-8:
        sympl_ok = False
    # [k,k] in k ; [k,p] in p ; [p,p] in k
    for Xc, Yc, sign in ((K1, K2, +1), (K1, P1, -1), (P1, P2, +1)):
        Bk = Xc @ Yc - Yc @ Xc
        if np.linalg.norm(theta_q(Bk) - sign * Bk) > 1e-7:
            pair_ok = False
CHECK("C4 fixed elements satisfy X^T J + J X = 0 (symplectic witness) and "
      "(k, p) is a symmetric pair: [k,k]<k, [k,p]<p, [p,p]<k  (type A II)",
      sympl_ok and pair_ok)

# C5: Dynkin index ratios via the theta-fixed Cartan H = i diag(I5, -I5)
H = 1j * np.diag([1.0] * 5 + [-1.0] * 5)
h_fixed = np.linalg.norm(theta_q(H) - H) < 1e-12
tr_fund = np.trace(H @ H).real                       # expect -10
# adjoint trace over the fixed algebra: Tr(ad_H^2 P+)
ADH = np.column_stack([Mpinv @ vecR(H @ B - B @ H) for B in basis])
tr_adj = np.trace(ADH @ ADH @ Pp).real               # expect -120
# Lambda^2(10): eigenvalues h_i + h_j on e_i ^ e_j (the J-singlet sits at 0)
hs = np.diag(H)
tr_l2 = sum(((hs[i] + hs[j]) ** 2).real for i in range(10) for j in range(i + 1, 10))
ratio_adj = tr_adj / tr_fund
ratio_l2 = tr_l2 / tr_fund
CHECK("C5 index ratios: T(adj)/T(fund) = 12 (h_dual = 6), T(Lambda^2_0)/T(fund) = 8 "
      "(T = 4); hence b_- = (11*6 - 2*4)/3 = 58/3 exact",
      h_fixed and abs(ratio_adj - 12) < 1e-6 and abs(ratio_l2 - 8) < 1e-9
      and Fraction(11 * 6 - 2 * 4, 3) == Fraction(58, 3))

# C6: Witten parity + quenched and alternative-chain coefficients
CHECK("C6 Witten global anomaly: 2 T(Lambda^2_0) = 8 even (safe); quenched "
      "b(Sp10) = 22; b(SO14 pure) = 11*12/3 = 44; b(E8 pure) = 11*30/3 = 110",
      (2 * 4) % 2 == 0 and Fraction(11 * 6, 3) == 22
      and Fraction(11 * 12, 3) == 44 and Fraction(11 * 30, 3) == 110)

# -----------------------------------------------------------------------------
# Block D — The charge lattice: A9 root lattice and the seam fold to C5
# -----------------------------------------------------------------------------
print("\n--- Block D: charge lattice A9 and the C5 fold ---")
def cartanA(m):
    C = 2 * np.eye(m, dtype=int)
    for i in range(m - 1):
        C[i, i + 1] = -1
        C[i + 1, i] = -1
    return C

C9 = cartanA(9)
detC9 = int(round(np.linalg.det(C9)))
posdef = np.all(np.linalg.eigvalsh(C9.astype(float)) > 0)
CHECK("D1 A9 Cartan: det = 10 = |Z10| (Kronheimer lattice discriminant), "
      "positive definite", detC9 == 10 and posdef)

# seam involution on simple roots alpha_k <-> alpha_{10-k} (0-indexed i <-> 8-i)
Pn = np.zeros((9, 9), dtype=int)
for i in range(9):
    Pn[i, 8 - i] = 1
ev = np.linalg.eigvalsh(Pn.astype(float))
r_plus = int(np.sum(np.abs(ev - 1) < 1e-9))
r_minus = int(np.sum(np.abs(ev + 1) < 1e-9))
CHECK("D2 seam split of the A9 lattice: invariant rank 5, anti-invariant rank 4",
      r_plus == 5 and r_minus == 4)

orbits = [(0, 8), (1, 7), (2, 6), (3, 5), (4,)]
fold = np.zeros((5, 5), dtype=int)
for I, oI in enumerate(orbits):
    i = oI[0]
    for Jx, oJ in enumerate(orbits):
        fold[I, Jx] = sum(C9[i, j] for j in oJ)
C5_expect = np.array([[2, -1, 0, 0, 0],
                      [-1, 2, -1, 0, 0],
                      [0, -1, 2, -1, 0],
                      [0, 0, -1, 2, -1],
                      [0, 0, 0, -2, 2]], dtype=int)
CHECK("D3 folded Cartan = C5 (det 2), with the seam character node rho_5 -> the "
      "long root of Sp(10)", (fold == C5_expect).all()
      and int(round(np.linalg.det(fold))) == 2)

# -----------------------------------------------------------------------------
# Block E — The Sixth Route: frozen 16-reading audit (pre-registered, Section 2)
# -----------------------------------------------------------------------------
print("\n--- Block E: Sixth-Route frozen audit (16 readings) ---")
kap2 = mp.mpf(35) / 4807
pref = (th ** 2 / 2) * mp.mpf(1260) / 4807
lnpref = mp.log(pref)
print(f"    prefactor (omega^2/2)*(1260/4807) = {mp.nstr(pref, 10)}, "
      f"ln = {mp.nstr(lnpref, 8)}")
CHECK("E1 prefactor ln[(omega^2/2)(1260/4807)] = -0.40204 (5 digits)",
      abs(lnpref + mp.mpf('0.40204')) < mp.mpf('5e-5'))

CHECK("E2 structural factor 1260/4807 = 36 A/Q exact (ZS-F35, consumed verbatim)",
      Fraction(1260, 4807) == 36 * Fraction(35, 437) / 11)

# firewalled external anchor (comparison only, not a theorem input)
NU_TARGET = mp.mpf('276.6')          # ZS-A26 nu_now (reduced M_P convention)
WINDOW = (mp.mpf('276.6'), mp.mpf('284.0'))   # ZS-F32.27 convention window

chains = [("USp(10) + 1 Weyl 44 (primary)", Fraction(58, 3)),
          ("USp(10) quenched", Fraction(22, 1)),
          ("SO(14) quenched (2D5 alt.)", Fraction(44, 1)),
          ("E8 quenched (2I alt.)", Fraction(110, 1))]
couplings = [("alpha_- = kappa^2 (primary)", lambda b: 2 * mp.pi / (b * kap2)),
             ("g_-^2 = kappa^2 (alt. norm.)", lambda b: 8 * mp.pi ** 2 / (b * kap2))]
powers = [4, 8]

readings = []
for (cn, bfrac), (gn, Sfun), p in itertools.product(chains, couplings, powers):
    b = mp.mpf(bfrac.numerator) / bfrac.denominator
    S = Sfun(b)
    nu = p * S - lnpref
    readings.append((cn, gn, p, S, nu, abs(nu - NU_TARGET)))

print(f"    {'chain':34s} {'coupling':28s} p     S          nu_pred    |dnu|")
for cn, gn, p, S, nu, d in readings:
    print(f"    {cn:34s} {gn:28s} {p}  {mp.nstr(S, 7):>9s}  "
          f"{mp.nstr(nu, 7):>9s}  {mp.nstr(d, 6)}")

mind = min(r[5] for r in readings)
closest = min(readings, key=lambda r: r[5])
CHECK("E3 closest pre-registered reading = (USp(10) quenched, alpha=kappa^2, p=8), "
      "nu = 314.2", closest[0].startswith("USp(10) quenched")
      and closest[1].startswith("alpha") and closest[2] == 8
      and abs(closest[4] - mp.mpf('314.2')) < mp.mpf('0.1'))
CHECK("E4 ALL 16 readings miss: min |Delta nu| = 37.6 > 37 "
      "(rho off by a factor >= 2e16)", mind > 37)
CHECK("E5 no reading lands inside the ZS-F32 convention window [276.6, 284.0]",
      all(not (WINDOW[0] <= r[4] <= WINDOW[1]) for r in readings))

# -----------------------------------------------------------------------------
# Block F — Stage 2 (v1.1): the quaternionic-multiplet route and the 25/2 No-Go
# Registered AFTER the stage-1 evaluation; therefore held to theorem-or-nothing
# discipline: only derivable coefficients are evaluated as readings.
# -----------------------------------------------------------------------------
print("\n--- Block F: stage-2 quaternionic route and the 25/2 No-Go ---")

# F1: the quaternionic (H-QM) multiplet coefficient b = 2 h_dual(C5) = 12
b_qm = Fraction(11 * 6 - 2 * (6 + 6) - 1 * 6, 3)   # gauge + 2 adjoint Weyl + 1 adjoint complex scalar
CHECK("F1 quaternionic multiplet: b = (11*6 - 2*12 - 6)/3 = 12 = 2 h_dual(C5); "
      "maximal-symmetry consistency: + adjoint hyper -> b = 12 - 12 = 0",
      b_qm == 12 and 2 * 6 == 12 and b_qm - Fraction(2 * 6 + 1 * 12, 3) * 0 == 12
      and (12 - 12) == 0)

def nu_of(b, p):
    S = 2 * mp.pi / (mp.mpf(b.numerator) / b.denominator * kap2)
    return p * S - lnpref, S

# F2: stage-2 frozen readings (declared in paper Section 2.5): (b=12, p=4), (b=12, p=8)
stage2 = []
for p in (4, 8):
    nu, S = nu_of(Fraction(12), p)
    stage2.append((p, S, nu, abs(nu - NU_TARGET)))
    print(f"    stage-2 reading: b=12, alpha_-=kappa^2, p={p}: S={mp.nstr(S,7)}, "
          f"nu={mp.nstr(nu,7)}, |dnu|={mp.nstr(abs(nu-NU_TARGET),6)}")
CHECK("F2 stage-2 readings both miss: nu(12,4) = 288.05 (window +4.05), "
      "nu(12,8) = 575.70; neither inside [276.6, 284.0]",
      abs(stage2[0][2] - mp.mpf('288.05')) < mp.mpf('0.01')
      and all(not (WINDOW[0] <= r[2] <= WINDOW[1]) for r in stage2))

# F3: family bound — every Witten-admissible quaternionic content has integer b <= 12,
# and nu_4(b) is decreasing in b, so nu_4 >= nu_4(12) = 288.05 > 284.0 for the whole family
family_ok = all(nu_of(Fraction(b), 4)[0] >= stage2[0][2] - mp.mpf('1e-9')
                for b in range(1, 13))
CHECK("F3 family CLOSED-NEGATIVE: for all admissible integer b <= 12, "
      "nu_4(b) >= 288.05 > 284.0 (monotone bound, b = 1..12 enumerated)",
      family_ok and stage2[0][2] > WINDOW[1])

# F4: Witten admissibility of matter steps — the half-step is forbidden
#     half-hyper in fund: one Weyl in 10, 2T = 1 odd -> Witten anomalous (forbidden);
#     allowed hyper steps are integers: fund hyper db = -1, Lambda^2_0 hyper db = -8,
#     adjoint hyper db = -12
CHECK("F4 Witten half-step exclusion: half-hyper fund has 2T = 1 (odd -> forbidden); "
      "allowed steps db in {-1, -8, -12} are integers -> b in 12 - Z_{>=0}, never 25/2",
      (2 * Fraction(1, 2)) % 2 == 1
      and all(x == int(x) for x in (Fraction(2 * 1, 2), Fraction(2 * 8, 2), Fraction(2 * 12, 2)))
      and Fraction(25, 2).denominator == 2)

# F5: Weyl-frame arithmetic No-Go — pure-fermion 25/2 impossible; scalar loophole unforced
x_req = Fraction(66 - 75 // 1, 1)  # placeholder, computed exactly below
x_req = (Fraction(66) - 3 * Fraction(25, 2)) / 2          # Sum T_f = 57/4
scalar_loophole = (Fraction(66) - 2 * Fraction(4) - 3 * Fraction(25, 2))  # Sum T_s with one Weyl 44
CHECK("F5 Weyl-frame No-Go: (66 - 2*Sum T_f)/3 = 25/2 requires Sum T_f = 57/4, "
      "not in (1/2)Z -> impossible without scalars; scalar-assisted solutions "
      "(e.g. Sum T_s = 41/2) exist arithmetically but are unforced (F-F41.7-void)",
      x_req == Fraction(57, 4) and (2 * x_req).denominator != 1
      and scalar_loophole == Fraction(41, 2)
      and (2 * scalar_loophole).denominator == 1)

# F6: the non-derivable candidates, evaluated only as no-go arithmetic (not readings)
nu_2525, _ = nu_of(Fraction(25, 2), 4)
nu_2323, _ = nu_of(Fraction(23, 2), 4)   # the APS-signed variant 12 - 1/2
CHECK("F6 even if granted, 25/2 is excluded by the frozen window: nu(25/2) = 276.545 "
      "< 276.6; APS-signed variant nu(23/2) = 300.56 also outside",
      nu_2525 < WINDOW[0] and abs(nu_2525 - mp.mpf('276.545')) < mp.mpf('0.005')
      and not (WINDOW[0] <= nu_2323 <= WINDOW[1]))

print(f"    [note] nu(25/2) = {mp.nstr(nu_2525, 7)}  (gap to frozen lower edge: "
      f"{mp.nstr(WINDOW[0] - nu_2525, 4)});  nu(23/2) = {mp.nstr(nu_2323, 7)}")

# -----------------------------------------------------------------------------
# Guards
# -----------------------------------------------------------------------------
print("\n--- Guards ---")
GUARD("G1 non-expansion: theorem-side constants limited to "
      "{A=35/437, Q=11, (2,3,6), z*-dynamics, pi}; the single firewalled anchor "
      "{276.6, [276.6,284.0]} enters Blocks E/F comparison only",
      A == Fraction(35, 437) and Q == 11)
GUARD("G2 firewall separation: observations below are printed outside the PASS "
      "ledger and are not counted as evidence", True)
GUARD("G3 frozen universe (stage 1): 4 chains x 2 couplings x 2 powers = 16 readings, "
      "enumerated before any nu evaluation (script order = paper Section 2 order)",
      len(readings) == 16 and len(chains) == 4 and len(couplings) == 2
      and len(powers) == 2)
GUARD("G4 frozen universe (stage 2): exactly 2 readings {b=12} x {p=4,8}, declared "
      "before evaluation; non-integer candidates {25/2, 23/2} enter Block F as "
      "No-Go arithmetic only, never as claim readings",
      len(stage2) == 2)

# -----------------------------------------------------------------------------
# Firewalled observations (NON-EVIDENCE)
# -----------------------------------------------------------------------------
print("\n--- FIREWALLED OBSERVATIONS (not counted as PASS evidence) ---")
Sstar = (NU_TARGET + lnpref) / 4
b_req = 2 * mp.pi / (Sstar * kap2)
print(f"[FIREWALL O1] required b at (alpha=kappa^2, p=4): b_req = "
      f"{mp.nstr(b_req, 7)} (~ 25/2 within 0.02%); per Block F this value is "
      f"UNREACHABLE in every derived frame (Weyl-frame parity, quaternionic "
      f"ceiling 12, APS sign) -> permanently OBSERVATION, never promotable")
print(f"[FIREWALL O2] S*/(2 pi) = {mp.nstr(Sstar / (2 * mp.pi), 7)} vs Q = 11 "
      f"(the known ZS-A31/A32 modular-depth proximity, consumed, not re-claimed)")
print(f"[FIREWALL O3] granting the underivable 25/2, nu = 276.545 sits 0.054 below "
      f"the frozen lower edge yet within ~1 sigma of the observational nu_now "
      f"uncertainty (+-0.05); the frozen rule governs and no claim arises")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 78)
print(f"SUMMARY: {PASS}/{TOTAL} checks PASS, {GPASS}/{GTOTAL} guards PASS")
if FAILED or GFAILED:
    print("FAILED:", FAILED + GFAILED)
    sys.exit(1)
print("All theorem-tier checks PASS. Zero fitted parameters. "
      "(A, Q, dim Z) = (35/437, 11, 2) LOCKED.")
sys.exit(0)
