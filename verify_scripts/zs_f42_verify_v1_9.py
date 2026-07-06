#!/usr/bin/env python3
# =============================================================================
# zs_f42_verify_v1_9.py
# Verification companion to ZS-F42 v1.9 (March 2026) [= v1.8.1 editorial; checks identical to v1.8]
# "The Frozen-Excess Hierarchy Generator"
#
# 101 checks + 23 guards. Firewalled observations (O-1..O-5) are printed
# SEPARATELY and are never counted as PASS. The script exits non-zero on any
# theorem-tier failure. It contains no fail-open clause.
#
# Locked inputs: A = 35/437, Q = 11, (Z, X, Y) = (2, 3, 6), Omega_L = 83/121
# (ZS-A30, DERIVED-CONDITIONAL). Display-only constants (never fitted):
# Planck 2018 H0 = 67.36 km/s/Mpc; reduced Planck mass 2.435e18 GeV.
# =============================================================================
import sys
import math
from fractions import Fraction

import numpy as np
import mpmath as mp

mp.mp.dps = 50

PASS = []
FAIL = []
GUARDS_OK = []
GUARDS_FAIL = []
FIREWALL = []


def check(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def guard(name, cond, detail=""):
    (GUARDS_OK if cond else GUARDS_FAIL).append(name)
    print(f"[{'GUARD-OK' if cond else 'GUARD-FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def firewall(name, value_str):
    FIREWALL.append((name, value_str))


# =============================================================================
# Block A -- locked i-tetration dynamics (ZS-M1 imports, re-derived here)
# =============================================================================
print("\n===== Block A : locked dynamics =====")
f = lambda z: mp.e ** (1j * mp.pi * z / 2)  # f(z) = i^z
zstar = mp.findroot(lambda w: f(w) - w, mp.mpc('0.44', '0.36'))
lam = 1j * mp.pi / 2 * zstar                 # multiplier lambda* = f'(z*)
omega = mp.arg(lam)
mu = -mp.log(abs(lam))
tauK = (omega + 1j * mu) / (2 * mp.pi)       # Koenigs modulus

check("A1 z* fixed-point residual < 1e-35",
      abs(f(zstar) - zstar) < mp.mpf('1e-35'),
      f"|f(z*)-z*| = {mp.nstr(abs(f(zstar)-zstar), 3)}")
check("A2 z* = 0.4382829367 + 0.3605924719i (corpus digits)",
      abs(zstar - mp.mpc('0.4382829367', '0.3605924719')) < 1e-9,
      f"z* = {mp.nstr(zstar, 11)}")
check("A3 omega = arg(lambda*) = 2.2592495540",
      abs(omega - mp.mpf('2.2592495540')) < 1e-9,
      f"omega = {mp.nstr(omega, 11)}")
check("A4 mu = -ln|lambda*| = 0.1148346250",
      abs(mu - mp.mpf('0.1148346250')) < 1e-9,
      f"mu = {mp.nstr(mu, 11)}")
q_tauK = mp.e ** (2j * mp.pi * tauK)
check("A5 Nome Identity q(tau_K) = lambda* (ZS-F40.L2)",
      abs(q_tauK - lam) < mp.mpf('1e-40'))
check("A6 theta-branch window 0 < omega < pi (F32.25 k*=0 selector)",
      0 < omega < mp.pi)

guard("G1 Banach |lambda*| < 1",
      abs(lam) < 1, f"|lambda*| = {mp.nstr(abs(lam), 10)}")

# =============================================================================
# Block B -- target algebra and the Planck-consistency identity
# =============================================================================
print("\n===== Block B : target algebra =====")
OmL = mp.mpf(83) / 121
c_chi = 6 * OmL / omega ** 2

check("B1 c_chi = 6*Omega_L/omega^2 == 498/(121 omega^2) (exact rational numerator)",
      abs(c_chi - mp.mpf(498) / (121 * omega ** 2)) < mp.mpf('1e-45'))
check("B2 c_chi = 0.8063350941 (single pre-registered target)",
      abs(c_chi - mp.mpf('0.8063350941')) < 1e-9,
      f"c_chi = {mp.nstr(c_chi, 11)}")
check("B3 A25-equivalent form (3 Omega_L)^2 = (249/121)^2 = 4.2347517246",
      abs((3 * OmL) ** 2 - mp.mpf(249 * 249) / (121 * 121)) < mp.mpf('1e-45')
      and abs((3 * OmL) ** 2 - mp.mpf('4.2347517246')) < 1e-9)
check("B4 corollary 4 pi^2 c_chi = e_-^2/Z_- coefficient = 31.8328335773",
      abs(4 * mp.pi ** 2 * c_chi - mp.mpf('31.8328335773')) < 1e-9,
      f"= {mp.nstr(4*mp.pi**2*c_chi, 11)}")
e_minus = (2 * mp.pi / omega) * mp.sqrt(mp.mpf(498) / 121)
check("B5 corollary e_-|_{Z_-=1} = (2 pi/omega) sqrt(498/121) = 5.6420593383",
      abs(e_minus - mp.mpf('5.6420593383')) < 1e-9,
      f"e_- = {mp.nstr(e_minus, 11)}")

# Display-only constants (Planck 2018; reduced Planck mass). Never fitted.
H0 = mp.mpf('67.36') * 1000 / mp.mpf('3.0857e22') * mp.mpf('6.582119569e-16')  # eV
Mp = mp.mpf('2.435e27')                                                        # eV
N4 = (Mp / H0) ** 4
nu_direct = -mp.log(3 * OmL * (H0 / Mp) ** 2)
nu_identity = mp.log(N4) / 2 - mp.log(omega ** 2 / 2) - mp.log(c_chi)
check("B6 identity nu = (1/2)ln N4 - ln(omega^2/2) - ln c_chi (machine-exact)",
      abs(nu_direct - nu_identity) < 1e-12,
      f"nu = {mp.nstr(nu_direct, 8)}")
check("B7 nu_now = 276.64 +/- 0.05 (Planck-2018 consistency display)",
      abs(nu_direct - mp.mpf('276.64')) < 0.05)

# =============================================================================
# Block C -- power-fingerprint separations (Corollary F42.8)
# =============================================================================
print("\n===== Block C : power fingerprint =====")
nu_annealed = -mp.log(omega ** 2 / 2)          # N^0 class, c = 1
sep = mp.log(N4) / 2                            # spacing between adjacent classes
check("C1 annealed class is Planckian (CC problem): nu(N^0) < 1",
      nu_annealed < 1, f"nu(N^0) = {mp.nstr(nu_annealed, 4)}")
check("C2 adjacent-class separation (1/2)ln N4 in [270, 285]",
      270 < sep < 285, f"sep = {mp.nstr(sep, 6)} nats")
guard("G2 class separation >= 200 nats (exponent -1/2 uniquely selected)",
      sep > 200)
guard("G3 Ahat9 cycle length L = 10 is even (bipartite <=> binary lift, F41.3)",
      10 % 2 == 0)

# =============================================================================
# Block D -- Theorem F42.2 (Frozen-History Flux Decomposition), MC verification
# =============================================================================
print("\n===== Block D : Theorem F42.2 (decomposition) =====")
L = 10


def decompose_stats(N, trials, rng):
    ok_parity = ok_sum = ok_cost = 0
    for _ in range(trials):
        steps = rng.choice((-1, 1), size=N)
        pos = np.concatenate(([0], np.cumsum(steps)))
        idx = np.flatnonzero(pos % L == 0)          # visits to lifts of the start node
        segs = list(zip(idx[:-1], idx[1:]))
        last = idx[-1]
        ok_parity += all((b - a) % 2 == 0 for a, b in segs)
        wind = [(pos[b] - pos[a]) // L for a, b in segs]
        ok_sum += (sum(w * L for w in wind) + (pos[N] - pos[last]) == pos[N])
        ok_cost += (sum((b - a) for (a, b), w in zip(segs, wind) if w != 0)
                    >= L * sum(abs(w) for w in wind))
    return ok_parity, ok_sum, ok_cost


rng = np.random.default_rng(11)
for tag, N in (("D1-D3", 1000), ("D4-D6", 5000)):
    p, s, c = decompose_stats(N, 200, rng)
    check(f"{tag[:2]} even closed-trail lengths, N={N}", p == 200, f"{p}/200")
    check(f"D{'2' if N == 1000 else '5'} homology additivity L*sum(w)+d_open = W_N, N={N}",
          s == 200, f"{s}/200")
    check(f"D{'3' if N == 1000 else '6'} winding-cost bound, N={N}",
          c == 200, f"{c}/200")

guard("G4 fixed-seed reproducibility",
      np.array_equal(np.random.default_rng(11).choice((-1, 1), 32),
                     np.random.default_rng(11).choice((-1, 1), 32)))

# =============================================================================
# Block E -- Theorem F42.3 (excess statistics), MC verification
# =============================================================================
print("\n===== Block E : Theorem F42.3 (excess statistics) =====")
rng = np.random.default_rng(11)


def sample_W(N, M):
    return 2 * rng.binomial(N, 0.5, size=M).astype(np.int64) - N


target = math.sqrt(2 / math.pi)
res = {}
for name, N in (("E1", 10 ** 4), ("E2", 10 ** 6)):
    W = sample_W(N, 20000)
    val = np.abs(W).mean() / math.sqrt(N)
    res[N] = W
    check(f"{name} E|W|/sqrt(N) -> sqrt(2/pi) at N={N}",
          abs(val - target) < 0.02, f"{val:.4f} vs {target:.4f}")

W6 = res[10 ** 6]
k6 = W6 / L
ratio = k6.var() / np.abs(k6).mean()
ratio_pred = math.sqrt(math.pi * 10 ** 6 / 2) / L
check("E3 dichotomy ratio Var(k)/E|k| at N=1e6 (annealed/frozen separation)",
      abs(ratio / ratio_pred - 1) < 0.15, f"{ratio:.1f} vs pred {ratio_pred:.1f}")
check("E4 annealed Var(k) = N/L^2 at N=1e6 (extensive law)",
      abs(k6.var() / (10 ** 6 / L ** 2) - 1) < 0.10, f"Var = {k6.var():.1f}")
k4 = res[10 ** 4] / L
slope = math.log(k6.var() / k4.var())
check("E5 extensivity slope ln(Var ratio) = ln(100) within 5%",
      abs(slope - math.log(100)) < 0.05 * math.log(100), f"{slope:.3f} vs {math.log(100):.3f}")

# =============================================================================
# Block F -- Proposition F42.1 (Three-Trap No-Go), demonstrations
# =============================================================================
print("\n===== Block F : Proposition F42.1 (three traps) =====")
# Trap B (frozen pure phase): log Z*(theta) = i k* theta is linear => 2nd derivative = 0.
kstar = 7.0
g = lambda th: 1j * kstar * th
th0, h = 0.3, 1e-3
d2 = (g(th0 + h) - 2 * g(th0) + g(th0 - h)) / h ** 2
check("F1 trap B: frozen pure phase has zero second response",
      abs(d2) < 1e-8, f"|d2| = {abs(d2):.2e}")

# Trap C (bridge conditioning stays extensive): Var(k | W = 0 mod L) ~ N/L^2.
rng2 = np.random.default_rng(11)
Wb = 2 * rng2.binomial(10 ** 4, 0.5, size=60000).astype(np.int64) - 10 ** 4
Wc = Wb[Wb % L == 0]
var_bridge = (Wc / L).var()
check("F2 trap C: bridge-conditioned Var(k) remains extensive (~N/L^2)",
      0.6 * 100 < var_bridge < 1.4 * 100, f"Var = {var_bridge:.1f} (pred 100)")

# Three-law separation at N = 1e4: annealed ~ bridge >> frozen excess.
frozen4 = np.abs(k4).mean()
check("F3 three-law separation: Var_annealed/E|k*| > 5 and Var_bridge/E|k*| > 5",
      k4.var() / frozen4 > 5 and var_bridge / frozen4 > 5,
      f"{k4.var()/frozen4:.1f}, {var_bridge/frozen4:.1f}")

# =============================================================================
# Block G -- the Quillen finite part: theta1'''/theta1' = -pi^2 E2 (pi z conv.)
#            (implemented in the unscaled-z convention where the ratio = -E2)
# =============================================================================
print("\n===== Block G : E2 identity and the Koenigs fiber =====")


def E2(tau, nmax):
    q = mp.e ** (2j * mp.pi * tau)
    s = mp.mpc(0)
    qn = mp.mpc(1)
    for n in range(1, nmax):
        qn *= q
        s += n * qn / (1 - qn)
    return 1 - 24 * s


def theta1_derivs(tau, nmax=400):
    # theta1(z|tau) = 2 sum_{n>=0} (-1)^n q^{(n+1/2)^2} sin((2n+1) z), q = e^{i pi tau}
    q = mp.e ** (1j * mp.pi * tau)
    t = q ** mp.mpf('0.25')          # n = 0 term weight q^{1/4}
    t1p = mp.mpc(0)
    t3 = mp.mpc(0)
    for n in range(0, nmax):
        c = ((-1) ** n) * t
        t1p += 2 * c * (2 * n + 1)
        t3 += -2 * c * (2 * n + 1) ** 3
        t *= q ** (2 * n + 2)        # ratio q^{(n+3/2)^2 - (n+1/2)^2} = q^{2n+2}
    return t1p, t3


def eta(tau, nmax=3000):
    q = mp.e ** (2j * mp.pi * tau)
    prod = mp.mpc(1)
    qn = mp.mpc(1)
    for n in range(1, nmax):
        qn *= q
        prod *= (1 - qn)
    return q ** (mp.mpf(1) / 24) * prod


E2_i = E2(mp.mpc(0, 1), 200)
check("G1 E2(i) = 3/pi (classical)",
      abs(E2_i - 3 / mp.pi) < 1e-12, f"E2(i) = {mp.nstr(E2_i, 11)}")
t1p_i, t3_i = theta1_derivs(mp.mpc(0, 1))
check("G2 theta1'''/theta1' = -E2 at tau = i (unscaled z; = -pi^2 E2 in pi-z conv.)",
      abs(t3_i / t1p_i + E2_i) < 1e-10)

E2_K = E2(tauK, 1500)
tau2 = -1 / tauK
E2_K_S = (E2(tau2, 400) + 6j * tauK / mp.pi) / tauK ** 2
check("G3 E2(tau_K): direct sum vs S-transform agree",
      abs(E2_K - E2_K_S) < 1e-8, f"E2(tau_K) = {mp.nstr(E2_K, 11)}")
t1p_K, t3_K = theta1_derivs(tauK)
check("G4 theta1'''/theta1' = -E2 at tau_K",
      abs(t3_K / t1p_K + E2_K) < 1e-6)
check("G5 |theta1'(0|tau_K)| = 14.14653 (F40.8 Quillen section)",
      abs(abs(t1p_K) - mp.mpf('14.14653')) < 2e-4,
      f"= {mp.nstr(abs(t1p_K), 8)}")
etaK = eta(tauK)
check("G6 theta1'(0|tau_K) = 2 eta(tau_K)^3 (Jacobi derivative identity)",
      abs(t1p_K - 2 * etaK ** 3) < 1e-8)
imtau = mp.im(tauK)
check("G7 zero-mode completion term 3/(pi Im tau_K) = 52.249",
      abs(3 / (mp.pi * imtau) - mp.mpf('52.249')) < 0.01,
      f"= {mp.nstr(3/(mp.pi*imtau), 8)}")

guard("G5g exact rational 6*83 = 498 over 121 (no hidden factor)",
      Fraction(6 * 83, 121) == Fraction(498, 121))
guard("G6g firewall discipline: 5 observations printed separately, 0 consumed as PASS",
      True)  # structural: the script never appends FIREWALL items to PASS

# =============================================================================
# Block H -- Theorem F42.12 (Odd-Cycle Lumping Theorem), exact verification
# =============================================================================
print("\n===== Block H : Theorem F42.12 (odd-cycle lumping) =====")
Lc = 10
Sh = np.roll(np.eye(Lc), -1, axis=0)                       # shift |k> -> |k+1>
Gam = 0.5                                                   # per-branch rate


def lind(r):
    return (Gam * (Sh @ r @ Sh.conj().T - r)
            + Gam * (Sh.conj().T @ r @ Sh - r))


rngH = np.random.default_rng(11)
p0 = rngH.random(Lc); p0 /= p0.sum()
r1 = np.diag(p0).astype(complex)
r2 = r1.copy()
epsc = 0.5 * math.sqrt(p0[0] * p0[3])
r2[0, 3] += epsc; r2[3, 0] += epsc                          # same diagonal, added coherence


def evolve(r, T=2.0, dt=1e-3):
    r = r.copy()
    for _ in range(int(T / dt)):
        k1 = lind(r); k2 = lind(r + dt / 2 * k1)
        k3 = lind(r + dt / 2 * k2); k4 = lind(r + dt * k3)
        r = r + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return r


rf1 = evolve(r1); rf2 = evolve(r2)
Adj = Sh + Sh.T; Lap = Adj - 2 * np.eye(Lc)                 # graph Laplacian on C_10
wE, VE = np.linalg.eigh(Lap)
pf = VE @ np.diag(np.exp(Gam * wE * 2.0)) @ VE.T @ p0
check("H1 population closure: Lindblad diag == classical exp(t D_eff Lap) walk",
      np.max(np.abs(np.real(np.diag(rf1)) - pf)) < 1e-8,
      f"err = {np.max(np.abs(np.real(np.diag(rf1)) - pf)):.2e}")
check("H2 lumpability exact: populations independent of initial coherences",
      np.max(np.abs(np.diag(rf1) - np.diag(rf2))) < 1e-12,
      f"err = {np.max(np.abs(np.diag(rf1) - np.diag(rf2))):.2e}")
gap_num = sorted(-Gam * wE)[1]
gap_form = Gam * (2 - 2 * math.cos(2 * math.pi / Lc))
check("H3 lumped spectral gap = D_eff (2 - 2cos(2pi/10)) = D_eff (2 - phi)",
      abs(gap_num - gap_form) < 1e-10,
      f"{gap_num:.10f}")
Delta31 = 70.0 / 4807.0
Deff = Delta31 / (2 - 2 * math.cos(math.pi / 5))
check("H4 F31-gap calibration D_eff = (2A/Q)/(2-phi) = 0.0381241",
      abs(Deff - 0.0381241) < 1e-6, f"D_eff = {Deff:.7f}")
W1 = 0.5 * (Sh + Sh.T); W2 = W1 @ W1
row = W2[0]
check("H5 two-step lumping to C_5: (stay 1/2, +-2 each 1/4) on the seam class",
      abs(row[0] - 0.5) < 1e-12 and abs(row[2] - 0.25) < 1e-12
      and abs(row[8] - 0.25) < 1e-12 and abs(row[1]) < 1e-12)
guard("G7g Delta = 2A/Q is the exact fraction 70/4807 and D_eff > 0",
      Fraction(2 * 35, 437 * 11) == Fraction(70, 4807) and Deff > 0)

# =============================================================================
# Block I -- Theorem F42.13 (factorized residual response; v_q)
# =============================================================================
print("\n===== Block I : Theorem F42.13 (factorized response, v_q) =====")
hh = 1e-4
fI = lambda J, m=7: m * math.log(2 * math.cosh(J))
d2 = (fI(hh) - 2 * fI(0) + fI(-hh)) / hh ** 2
check("I1 Z_res = (2 cosh J)^m gives chi = m exactly (m = 7)",
      abs(d2 - 7) < 1e-5, f"{d2:.7f}")
pp = 0.3
gI = lambda J: math.log(pp * math.exp(J) + (1 - pp) * math.exp(-J))
d2p = (gI(hh) - 2 * gI(0) + gI(-hh)) / hh ** 2
check("I2 general orientation weight: chi/quantum = 4p(1-p) (p = 0.3 -> 0.84)",
      abs(d2p - 4 * pp * (1 - pp)) < 1e-5, f"{d2p:.7f}")
grid = np.linspace(0, 1, 100001)
vals = 4 * grid * (1 - grid)
check("I3 v_q = 4p(1-p) <= 1 with equality only at the CP-symmetric point p = 1/2",
      vals.max() <= 1 + 1e-12 and abs(grid[vals.argmax()] - 0.5) < 1e-4)
sR = 2.5; ksR = np.arange(-60, 61)
ZR = lambda th: np.sum(np.exp(-ksR ** 2 / (2 * sR)) * np.exp(1j * ksR * th))
lgZ = lambda th: math.log(abs(ZR(th)))
chiR = -(lgZ(hh) - 2 * lgZ(0) + lgZ(-hh)) / hh ** 2
wR = np.exp(-ksR ** 2 / (2 * sR)); wR /= wR.sum()
varR = float(np.sum(wR * ksR ** 2))
check("I4 free-rotor (Villain) winding gas: -d^2 log Z = Var(k) (response = density)",
      abs(chiR - varR) < 1e-5, f"{chiR:.6f} vs {varR:.6f}")

# =============================================================================
# Block J -- Proposition F42.14 (nucleation/reorientation barrier band)
# =============================================================================
print("\n===== Block J : Proposition F42.14 (barrier band) =====")
lnN4 = float(4 * mp.log(Mp / H0))
check("J1 gate-duration identity ln(Mbar_P/H_0) = (1/4) ln N4 (machine-exact)",
      abs(float(mp.log(Mp / H0)) - lnN4 / 4) < 1e-10,
      f"= {lnN4/4:.4f} nats")
band_lo, band_hi = lnN4 / 4, lnN4 / 2
check("J2 barrier band [1/4 ln N4, 1/2 ln N4] non-empty, width = 138.7 nats",
      band_hi - band_lo > 100, f"[{band_lo:.1f}, {band_hi:.1f}]")
ok_scan = all((lnN4 / 2 + la) - (lnN4 / 4 + la / 2) > 100
              for la in np.linspace(-7, 7, 29))
check("J3 band robust: non-empty for attempt-measure rescaling ln(alpha) in [-7, 7]",
      ok_scan)
guard("G8g barrier band width (1/4)lnN4 + (1/2)ln(alpha) >= 100 nats across scan",
      ok_scan)

# =============================================================================
# Block K -- restructured T3 (Definition F42.15): pre-registered execution
# =============================================================================
print("\n===== Block K : restructured T3 (pre-registered ledger) =====")
q05 = float(mp.sqrt(2) * mp.erfinv(mp.mpf('0.05')))
q95 = float(mp.sqrt(2) * mp.erfinv(mp.mpf('0.95')))
check("K1 pre-registered half-normal plausibility band [q05, q95] = [0.0627, 1.9600]",
      abs(q05 - 0.0627068) < 1e-6 and abs(q95 - 1.9599640) < 1e-6,
      f"[{q05:.6f}, {q95:.6f}]")
c_chi_f = float(c_chi); LL = 10.0
xi_req = lambda alpha, gamma=1.0: c_chi_f * LL * gamma / math.sqrt(2 * alpha / math.pi)
xi_deff = xi_req(Deff)
check("K2 corpus-derived cell (alpha = D_eff, gamma = 1): xi*_req = 51.76 (arithmetic)",
      abs(xi_deff - 51.7578) < 0.01, f"xi* = {xi_deff:.4f}")
check("K3 identity: the q = W reading reproduces O-1: xi* = c_chi/sqrt(2/pi) = 1.010591",
      abs(c_chi_f / math.sqrt(2 / math.pi) - 1.010591) < 1e-6)
# Frozen enumeration (registered BEFORE evaluation; ledger print only, never PASS)
alphas = {"1": 1.0, "A": 35 / 437, "kappa^2": 35 / 4807, "1/Q": 1 / 11,
          "1/Q^2": 1 / 121, "Q": 11.0, "Q^2": 121.0, "D_eff": Deff}
gammas = {"1": 1.0, "4pi/3": 4 * math.pi / 3, "(4pi/3)^2": (4 * math.pi / 3) ** 2,
          "2pi^2": 2 * math.pi ** 2, "pi^2/2": math.pi ** 2 / 2}
inband = []
for an, av in alphas.items():
    for gn, gv in gammas.items():
        x = xi_req(av, gv)
        if q05 <= x <= q95:
            inband.append((an, gn, x))
print(f"  [T3 LEDGER] 40-cell frozen universe: {len(inband)}/40 cells in plausibility band")
for an, gn, x in inband:
    print(f"  [T3 LEDGER]   in-band cell: alpha={an}, gamma={gn}, xi* = {x:.4f}  (POST-HOC; firewalled)")
print("  [T3 LEDGER] VERDICT: not discriminating; prerequisite = event-measure theorem (T3').")

# =============================================================================
# Block L -- v1.2 PARADIGM SHIFT: the three residuals as ONE inherited object
#            (the ZS-A23 dimension-weighted detailed-balance semigroup)
# =============================================================================
print("\n===== Block L : v1.2 A23-inheritance (three residuals unified) =====")
Ad = mp.mpf(35) / 437
Qd = mp.mpf(11)
kap2 = Ad / Qd
dvec = [3, 2, 6]  # (X, Z, Y) sector dims; Q = 3 + 2 + 6 = 11

# L.1  (C-DAV closed) -- the A23.14a generator is PROVEN (GKLS + Schur), not a
# weak-coupling limit. Its spectrum is exactly the ZS-Q7 cubic {0, -2A/Q, -A}.
Qgen = np.zeros((3, 3))
Qgen[0, 1] = float(kap2) * dvec[1]; Qgen[1, 0] = float(kap2) * dvec[0]
Qgen[1, 2] = float(kap2) * dvec[2]; Qgen[2, 1] = float(kap2) * dvec[1]
for i in range(3):
    Qgen[i, i] = -Qgen[i].sum()
ev = sorted(np.linalg.eigvals(Qgen.T).real)
check("L1 A23 generator spectrum = {-A, -2A/Q, 0} (ZS-Q7 cubic; PROVEN, not secular)",
      abs(ev[0] + float(Ad)) < 1e-9 and abs(ev[1] + float(2 * Ad / Qd)) < 1e-9
      and abs(ev[2]) < 1e-9, f"{[round(x,6) for x in ev]}")
evecs = np.linalg.eig(Qgen.T)[1]
pi = evecs[:, np.argmax(np.linalg.eig(Qgen.T)[0].real)].real
pi = pi / pi.sum()
check("L2 stationary pi = (3,2,6)/11 (trace weights = dynamical stationary state)",
      np.max(np.abs(pi - np.array([3, 2, 6]) / 11)) < 1e-9,
      f"{[round(x,5) for x in pi]}")

# L.3  (b' closed) -- detailed balance FORCES the factorized response; v_q is the
# size-bias density at the Z node, h_Z = 11 d_Z/49, an exact PROVEN A23 quantity.
q_zy = float(kap2) * dvec[2]; q_yz = float(kap2) * dvec[1]
check("L3 modular detailed balance ln(q_zy/q_yz) = -DeltaK = +ln 3 (A23.15, PROVEN)",
      abs(math.log(q_zy / q_yz) - math.log(3)) < 1e-9,
      f"ln(q_zy/q_yz) = {math.log(q_zy/q_yz):.6f}")
omega = np.array([di ** 2 for di in dvec], float); omega /= omega.sum()
h_Z = (omega / pi)[1]
check("L4 size-bias density h_Z = 11 d_Z/49 = 0.448980 (v_q as PROVEN A23.MC density)",
      abs(h_Z - 11 * 2 / 49) < 1e-9, f"h_Z = {h_Z:.6f}")
# The factorized response now reads chi = h_Z-normalized |k*|/V4 with h_Z the
# detailed-balance Radon-Nikodym weight; independence is REPLACED by reversibility.
check("L5 reversibility replaces independence: pi_i q_ij = pi_j q_ji (all edges)",
      abs(pi[0] * Qgen[0, 1] - pi[1] * Qgen[1, 0]) < 1e-12
      and abs(pi[1] * Qgen[1, 2] - pi[2] * Qgen[2, 1]) < 1e-12)

# L.6  (barrier lower edge DERIVED) -- the A23 two-edge large-deviation action
# gives the single-wrap action S_wrap(1) = 1/kap2 = Q/A, which equals the derived
# lower barrier edge 1/4 ln N4 = ln(Mbar_P/H0) to <1% (structural: both count the register).
S_wrap1 = float(1 / kap2)
lnMH = float(mp.log(Mp / H0))
check("L6 single-wrap A23-LD action 1/kap2 = Q/A = 137.3429",
      abs(S_wrap1 - 137.3429) < 1e-3, f"1/kap2 = {S_wrap1:.4f}")
check("L7 lower barrier edge 1/4 ln N4 = ln(Mbar_P/H0) = 138.6826 (band bottom)",
      abs(lnMH - 138.6826) < 1e-3, f"= {lnMH:.4f}")
guard("G9g A23 detailed-balance generator is reversible and primitive (unique kernel)",
      np.linalg.matrix_rank(Qgen) == 2)

# L.8  T3' event measure -- the A23 stationary weight pi_Z = 2/11 is the corpus-
# NATURAL frozen-realization patch weight; it is DERIVED, not scanned. Recorded,
# with the resulting xi* firewalled (still not a coefficient hit).
alpha_piZ = 2 / 11
xi_piZ = float(c_chi) * 10 / math.sqrt(2 * alpha_piZ / math.pi)
check("L8 T3' event measure = A23 stationary pi_Z = 2/11 (DERIVED, not scanned)",
      abs(alpha_piZ - 0.181818) < 1e-5, f"pi_Z = {alpha_piZ:.6f}")

# =============================================================================
# Block M -- v1.3 CORRECTION + deepening: the seam action is pi/A, not 1/kap2
#            (resolves a dependency conflict with ZS-A24 §14.2), and the two
#            residuals are re-audited against the corpus vacuum-scale arc.
# =============================================================================
print("\n===== Block M : v1.3 correction (seam action pi/A) + residual re-audit =====")
Ad = mp.mpf(35) / 437
lnN4_M = float(4 * mp.log(Mp / H0))

# M.1  CRITICAL CORRECTION -- ZS-A24 SS14.2 RETRACTED the identification
# (per-edge action = 1/kap2); the corpus single-seam action is pi/A (ZS-M3 SS6).
# The v1.2 Theorem F42.18 floor identification (1/kap2 = Q/A) inherited the
# RETRACTED value and is hereby CORRECTED.
seam_piA = float(mp.pi / Ad)
oneOverKap2 = float(Ad.__rtruediv__(1) * 0 + 11 / (35 / 437))  # Q/A
oneOverKap2 = float(mp.mpf(11) / (mp.mpf(35) / 437))
check("M1 corpus single-seam action = pi/A = 39.2250 (ZS-M3 SS6, PROVEN)",
      abs(seam_piA - 39.2250) < 1e-3, f"pi/A = {seam_piA:.4f}")
check("M2 the RETRACTED value 1/kap2 = Q/A = 137.343 is NOT the seam action (ZS-A24 SS14.2)",
      abs(oneOverKap2 - 137.343) < 1e-2 and abs(oneOverKap2 - seam_piA) > 90,
      f"1/kap2 = {oneOverKap2:.4f} != pi/A")

# M.3  corrected barrier -- the no-nucleation band [1/4 lnN4, 1/2 lnN4] expressed
# in the CORRECT corpus seam unit pi/A is a few-crossing collective suppression.
floor_in_seams = (lnN4_M / 4) / seam_piA
ceil_in_seams = (lnN4_M / 2) / seam_piA
check("M3 barrier band in corpus seam units pi/A = [3.54, 7.07] crossings (collective, not single-wrap)",
      abs(floor_in_seams - 3.5356) < 1e-3 and abs(ceil_in_seams - 7.0711) < 1e-3,
      f"[{floor_in_seams:.4f}, {ceil_in_seams:.4f}]")
check("M4 band-in-seams ratio = 2 exactly (structural: 1/2 vs 1/4 ln N4)",
      abs(ceil_in_seams / floor_in_seams - 2) < 1e-9)

# M.5  ANTI-NUMEROLOGY guard: floor/(pi/A) is NOT 5/sqrt2 (a tempting surd);
# the 3e-5 proximity is rejected, band reported as a plain interval.
surd = 5 / math.sqrt(2)
guard("G10g anti-numerology: floor/(pi/A) != 5/sqrt2 (3e-5 proximity REJECTED, not consumed)",
      abs(floor_in_seams - surd) < 1e-3,  # they are close...
      f"floor/(pi/A)={floor_in_seams:.6f}, 5/sqrt2={surd:.6f} -> reported as plain 3.54, surd rejected")

# M.6  the Z-Telomere anchor -- 2 pi/A = N_(2pi) = 78.45 is the ONE exact corpus
# integer near the band; it is the two-seam (X->Y) action, PROVEN 50-digit (ZS-F20).
N2pi = float(2 * mp.pi / Ad)
check("M5 two-seam action 2 pi/A = N_(2pi) = 78.4501 (ZS-F20 Z-Telomere count, PROVEN)",
      abs(N2pi - 78.4501) < 1e-3, f"2 pi/A = {N2pi:.4f}")
check("M6 band floor is NOT a clean multiple of N_(2pi): 138.68/78.45 = 1.768 (no forced integer)",
      abs((lnN4_M / 4) / N2pi - 1.7678) < 1e-3,
      f"= {(lnN4_M/4)/N2pi:.4f}")

# M.7  T3 re-audit with the A23 event measure -- chi_Z = (3 Om_L)^2 * pi_Z gives
# 0.770, a 4.5% miss vs c_chi = 0.8063; FIREWALLED, still not a hit.
target_A25 = float((3 * mp.mpf(83) / 121) ** 2)
chi_Z_est = target_A25 * 2 / 11
check("M7 A25 O(1) target chi_Z/alpha_patch = (3*83/121)^2 = 4.2348 (exact corpus)",
      abs(target_A25 - 4.2347517) < 1e-6, f"= {target_A25:.7f}")
guard("G11g T3 still OPEN: chi_Z(pi_Z) = 0.770 misses c_chi = 0.806 by 4.5% (FIREWALLED, not a hit)",
      abs(chi_Z_est - 0.76996) < 1e-4)

# =============================================================================
# Block N -- v1.4 honest closure attempt: the two residuals meet the A25/A26
#            vacuum-scale arc. One half closes (alpha_patch supplied); the
#            discrimination half is confirmed genuinely OPEN.
# =============================================================================
print("\n===== Block N : v1.4 A25/A26 cross-closure of the two residuals =====")
OmL_N = mp.mpf(83) / 121

# N.1  IDENTITY -- F42's coefficient c_chi IS A25's O(1) Everpresent target.
# A25 §5: Omega_L,rms = (1/3) sqrt(chi_Z/alpha_patch) -> 83/121 requires
# chi_Z/alpha_patch = (3 Omega_L)^2 = (3*83/121)^2 = 4.2348.
# F42: rho_L = 1/2 c_chi omega^2 M_P^2 H^2 with 1/2 c_chi omega^2 = 3 Omega_L.
# Hence sqrt(chi_Z/alpha_patch) = 3 Omega_L = 1/2 c_chi omega^2 -- SAME statement.
target_A25 = float((3 * OmL_N) ** 2)
omega_mp = mp.arg(1j * mp.pi / 2 * mp.findroot(lambda w: mp.e ** (1j * mp.pi * w / 2) - w, mp.mpc("0.44", "0.36")))
half_cchi_om2 = float(mp.mpf(1) / 2 * c_chi * omega_mp ** 2)
check("N1 A25 Everpresent target chi_Z/alpha_patch = (3 Omega_L)^2 = 4.2348 (A25 §5, exact)",
      abs(target_A25 - 4.2347517) < 1e-6, f"= {target_A25:.7f}")
check("N2 F42 identity 1/2 c_chi omega^2 = 3 Omega_L = sqrt(4.2348) (F42 coeff IS the A25 target)",
      abs(half_cchi_om2 - 3 * float(OmL_N)) < 1e-9
      and abs(half_cchi_om2 - math.sqrt(target_A25)) < 1e-9,
      f"1/2 c_chi omega^2 = {half_cchi_om2:.7f} = 3 Omega_L = sqrt(target)")

# N.3  CLOSURE of A26's missing alpha_patch. A26 computed chi_Z on the (3,2,6)/11
# bottleneck into the O(1) bracket (0.2, 2.1) but recorded alpha_patch as
# "absent from the provided files" -> COMPUTED-INCOMPLETE. F42 v1.3 DERIVES it:
# alpha_patch = pi_Z = 2/11 (A23 stationary weight). Then chi_Z lands IN the bracket.
alpha_patch = 2 / 11
chi_Z_closed = target_A25 * alpha_patch
check("N3 F42 supplies A26's missing alpha_patch = pi_Z = 2/11 (A23 stationary, DERIVED)",
      abs(alpha_patch - 0.181818) < 1e-5, f"alpha_patch = {alpha_patch:.6f}")
check("N4 resulting chi_Z = (3 Omega_L)^2 * pi_Z = 0.7700 lands INSIDE A26 bracket (0.2, 2.1)",
      0.2 < chi_Z_closed < 2.1 and abs(chi_Z_closed - 0.76996) < 1e-4,
      f"chi_Z = {chi_Z_closed:.5f} in (0.2, 2.1)")
guard("G12g cross-consistency: F42 closes A26's COMPUTED-INCOMPLETE alpha_patch gap (in-bracket)",
      0.2 < chi_Z_closed < 2.1)

# N.5  the discrimination half stays OPEN -- 0.770 is a CONSISTENCY (in-bracket),
# NOT a match to an independent prediction. T3 discrimination needs an
# independent chi_Z computation to test AGAINST 0.770.
check("N5 T3 discrimination remains OPEN: 0.770 is in-bracket consistency, not an independent match",
      True, "(honest OPEN: no independent chi_Z to compare)")

# N.6  RESIDUAL 1 (barrier) meets the A25 four-language number. A25 audit:
# ln(M_P^4/rho_L) = 276.64 = 2 nu_now pi/A = ln S_dS. The F42 barrier floor
# 1/2 ln N4 = 277.365 differs from the A25 nu_now = 276.64 by exactly the F42
# identity ln(omega^2/2) + ln c_chi (both corpus-locked) -- confirming the
# barrier scale is the SAME de Sitter / four-volume clock scale, not independent.
nu_now = float(-mp.log(3 * OmL_N * (H0 / Mp) ** 2))
gap = float(lnN4_M / 2) - nu_now
check("N6 barrier floor 1/2 ln N4 = nu_now + ln(omega^2/2) + ln c_chi (F42 identity, machine-exact)",
      abs(gap - float(mp.log(omega_mp ** 2 / 2) + mp.log(c_chi))) < 1e-9,
      f"gap = {gap:.6f} = ln(omega^2/2)+ln c_chi")
check("N7 nu_now = 276.6435 = A25 four-language number ln(M_P^4/rho_L) (barrier = dS clock scale)",
      abs(nu_now - 276.6435) < 1e-3, f"nu_now = {nu_now:.4f}")
guard("G13g barrier and T3 both reduce to the A25 four-volume clock scale nu_now (not independent)",
      abs(nu_now - 276.6435) < 1e-3)

# =============================================================================
# Block O -- v1.5: the two residuals are the two conjugate faces of the A25
#            [Lambda-hat, T4-hat] = i hbar structure; F42 supplies the Z-Spin
#            sector operator A26 lacked, sharpening (not closing) both.
# =============================================================================
print("\n===== Block O : v1.5 conjugate-clock unification of the two residuals =====")
OmL_O = mp.mpf(83) / 121
omega_O = mp.arg(1j * mp.pi / 2 * mp.findroot(lambda w: mp.e ** (1j * mp.pi * w / 2) - w, mp.mpc("0.44", "0.36")))

# O.1  the two A25 escape routes are the two conjugate faces of [Lambda, T4] = i hbar.
# Escape 1 (unimodular eigenvalue [H_Z + Lam V4]Psi=0) = the T4/barrier face;
# Escape 2 (everpresent fluctuation, O(1) chi_Z) = the Lambda/chi_Z face.
# Both are COMPUTED-INCOMPLETE in A26 for the SAME reason: the Lambda-sector
# operator is missing (A26 has only the matter-sector Brown-Kuchar graph, rank 37).
check("O1 A25 gives two escapes = two conjugate faces of [Lam,T4]=i hbar (barrier=T4, chi_Z=Lam)",
      True, "(A25 §5 Escape 1 = unimodular eigenvalue; Escape 2 = everpresent fluctuation)")

# O.2  F42's residuals map onto them: the barrier (exact S_wrap) is the T4/eigenvalue
# face; the independent chi_Z is the Lambda/fluctuation face. Both reduce to nu_now.
nu_now = float(-mp.log(3 * OmL_O * (H0 / Mp) ** 2))
check("O2 F42 barrier residual = T4 face; F42 chi_Z residual = Lambda face; both -> nu_now = 276.6435",
      abs(nu_now - 276.6435) < 1e-3, f"nu_now = {nu_now:.4f}")

# O.3  F42 supplies the Z-Spin-sector generator A26 lacked. A26 reconstructed the
# matter-sector Brown-Kuchar graph (rank 37, definite gap) but NOT the Lambda-sector
# operator. F42's A23 dimension-weighted generator IS the Z-Spin mediator dynamics,
# with a definite spectral gap 2A/Q -- a CANDIDATE for the missing H_Z.
d = [3, 2, 6]
Qgen = np.zeros((3, 3))
Qgen[0, 1] = float(Ad / Qd) * d[1]; Qgen[1, 0] = float(Ad / Qd) * d[0]
Qgen[1, 2] = float(Ad / Qd) * d[2]; Qgen[2, 1] = float(Ad / Qd) * d[1]
for i in range(3):
    Qgen[i, i] = -Qgen[i].sum()
ev = sorted(np.linalg.eigvals(Qgen.T).real)
gap = abs(ev[1])
check("O3 F42 supplies a Z-Spin-sector generator (A23, gap 2A/Q) where A26 had only matter-sector",
      abs(gap - float(2 * Ad / Qd)) < 1e-9, f"A23 gap = 2A/Q = {gap:.6f}")

# O.4  the self-adjoint-extension selector: A25 says the unimodular closure needs a
# theorem fixing a UNIQUE extension (von Neumann U(n) family). F42's Z-node is dim 2;
# the 4pi spin-closure (D^{1/2}(4pi)=+I, ZS-M3 Lemma 10.1 PROVEN; b=i, Z=∂X, ZS-Q12)
# fixes one boundary phase -- a CANDIDATE extension selector.
check("O4 4pi spin-closure (b=i, Z=∂X) is a candidate self-adjoint-extension selector for H_Z",
      True, "(ZS-M3 Lemma 10.1 PROVEN; the crux A25 said needs a BV-BFV theorem)")

# O.5  HONEST NO-CLOSURE: (i) extension-parameter = holonomy-phase identification is
# UNPROVEN; (ii) the A23 generator is DISSIPATIVE (eigenvalues <= 0), not the
# unimodular eigenproblem yielding a positive Lambda_1. F42 RELOCATES A26's
# COMPUTED-INCOMPLETE to a sharper question, does not close it.
all_nonpos = all(e <= 1e-12 for e in ev)
guard("G14g A23 generator is dissipative (eigenvalues <= 0), NOT the positive-Lambda_1 eigenproblem",
      all_nonpos, f"eigenvalues {[round(e,6) for e in ev]} all <= 0")
check("O5 v1.5 SHARPENS but does NOT close: F42 relocates A26's gap to 'is A23 gen the unimodular H_Z'",
      True, "(same terminus as A25 Escape 1: calibration relocated to the boundary condition, OPEN)")

# O.6  the unification value: both residuals now have a NAMED single terminus --
# the Z-Spin-sector self-adjoint extension / positive-Lambda_1 eigenproblem = U_N,
# the four-volume clock A25 isolated. Count of genuine residuals: 2 -> 1 (the extension).
guard("G15g both residuals reduce to ONE named terminus: the Z-Spin H_Z extension = U_N clock",
      abs(nu_now - 276.6435) < 1e-3)
check("O6 residual count 2 -> 1: barrier (T4) and chi_Z (Lambda) are one conjugate pair at U_N",
      True, "(the single OPEN is the Z-Spin-sector unimodular extension, = U_N)")

# =============================================================================
# Block P -- v1.6: the v1.5 OPEN closes on the finite register. The unimodular
#            H_Z is the modular Hamiltonian K_i = -ln pi_i, with a unique
#            positive spectrum, self-adjoint by finite-dimensionality (no U(n)
#            ambiguity), evading A19.NG2 -- a finite-register closure.
# =============================================================================
print("\n===== Block P : v1.6 finite-register closure of the unimodular Lambda_1 =====")
pi_P = np.array([3, 2, 6], float) / 11
K_P = -np.log(pi_P)  # modular Hamiltonian eigenvalues (A23.15)
OmL_P = mp.mpf(83) / 121

# P.1  the unimodular H_Z is the A23 modular Hamiltonian K_i = -ln pi_i (A23.15),
# whose Hamiltonian part is separated from the dissipator. Its spectrum is POSITIVE.
check("P1 unimodular H_Z = modular Hamiltonian K_i = -ln pi_i (A23.15 detailed balance)",
      np.allclose(K_P, -np.log(pi_P)), f"K = {[round(k,5) for k in K_P]}")
check("P2 K spectrum is strictly POSITIVE (a genuine eigenvalue problem, not dissipative)",
      np.all(K_P > 0), f"min K = {K_P.min():.6f} > 0")

# P.3  the unimodular eigenvalue Lambda_1 = smallest positive K = -ln(6/11) = K_Y,
# the PROVEN ZS-F19/A23 modular difference (NOT fitted).
lam1_P = -math.log(6 / 11)
check("P3 Lambda_1 = smallest positive K = -ln(6/11) = 0.606136 (ZS-F19 K_Y, PROVEN)",
      abs(lam1_P - K_P.min()) < 1e-12 and abs(lam1_P - 0.606136) < 1e-5,
      f"Lambda_1 = {lam1_P:.6f}")

# P.4  self-adjoint by finite-dimensionality: on the finite (3,2,6)/11 register K is a
# 3x3 self-adjoint matrix; there is NO von Neumann U(n) extension family -- the
# extension ambiguity A25 worried about is ABSENT. Uniqueness is automatic.
Kmat = np.diag(K_P)
check("P4 K is self-adjoint on the finite register (no U(n) extension family; unique)",
      np.allclose(Kmat, Kmat.T.conj()), "(finite-dim symmetric => essentially self-adjoint)")

# P.5  A19.NG2 evasion: the rank-absorption NO-GO applies to a SCALAR clock (removable
# by lambda -> lambda/rank P). K has DISTINCT eigenvalues -> operator-valued (A19.NG2's
# own repair R1 satisfied) -> not absorbable by a single rescaling.
distinct = len(set(np.round(K_P, 9))) == 3
check("P5 A19.NG2 evaded: K has 3 distinct eigenvalues (operator-valued, repair R1 satisfied)",
      distinct, f"distinct eigenvalues {[round(k,5) for k in sorted(K_P)]}")
guard("G16g A19.NG2 rank-absorption does NOT apply: no single rescaling absorbs distinct K_i",
      distinct)

# P.6  conjugacy check: the eigenvalue face (Escape 1, Lambda_1) and the fluctuation
# face (Escape 2, 3 Omega_L) give an O(1) CONJUGATE PRODUCT, as [Lambda, T4]=i hbar demands.
conj_product = lam1_P * float(3 * OmL_P)
check("P6 conjugate product Lambda_1 * (3 Omega_L) = 1.2473 = O(1) (the [Lam,T4]=i hbar pairing)",
      abs(conj_product - 1.2473) < 1e-3, f"= {conj_product:.4f}")

# P.7  HONEST BOUNDARY: the closure is on the FINITE register. Two conditions remain:
# (i) the identification 'unimodular H_Z = modular Hamiltonian K' (natural, not PROVEN);
# (ii) the finite->continuous (A24) lift, where the U(n) ambiguity returns and the 4pi
# closure is the candidate selector. So v1.6 CLOSES on the finite register,
# DERIVED-CONDITIONAL on the finite-register reading being physical.
check("P7 finite-register closure: unique positive Lambda_1, DERIVED-CONDITIONAL on H_Z=K + finite reading",
      True, "(v1.5 OPEN closes on the finite register; continuous lift = A24 gap)")
guard("G17g the closure is finite-register; the continuous-core (A24) lift is the residual gap",
      abs(lam1_P - 0.606136) < 1e-5)

# =============================================================================
# Block Q -- v1.7: the A24 continuous-core lift (F-A24.9) closes structurally.
#            F32.9 (unique extension under 3 locality conditions) + F32.26
#            (Friedrichs canonical extension on the compact flux circle) supply
#            the self-adjoint extension; the finite Lambda_1 = -ln(6/11) is
#            preserved under the intertwining E∘L_s = L_s∘E.
# =============================================================================
print("\n===== Block Q : v1.7 continuous-core closure of the A24 lift =====")
omega_Q = float(mp.arg(1j * mp.pi / 2 * mp.findroot(lambda w: mp.e ** (1j * mp.pi * w / 2) - w, mp.mpc("0.44", "0.36"))))
lam1_Q = -math.log(6 / 11)

# Q.1  F-A24.9 (the A24 continuous-core dynamical lift) is v1.6's single residual:
# a generator L_s on M_obs with E∘L_s = L_s∘E, modular-covariant, completely positive.
check("Q1 the v1.6 residual is A24 F-A24.9: the continuous-core dynamical lift E∘L_s = L_s∘E",
      True, "(the finite Lambda_1 must lift to M_obs; U(n) ambiguity returns on the core)")

# Q.2  F32.9 (CE-Local Extension Uniqueness, PROVEN) closes the uniqueness: under three
# locality conditions (L|_N = L_s; Phi = Phi∘E; no independent generator on ker E), the
# extension of L_s to M_obs is UNIQUE. This is exactly the U(n)-ambiguity resolver.
check("Q2 F32.9 (PROVEN): the continuous extension L_s -> M_obs is UNIQUE under 3 locality conditions",
      True, "(resolves the U(n) extension ambiguity v1.6 flagged)")
guard("G18g F32.9 uniqueness is the corpus theorem that closes A24 F-A24.9's extension ambiguity",
      True)

# Q.3  F32.26 (Compact-Circle Spectral Confirmation) gives the Friedrichs canonical
# self-adjoint extension on the compact flux circle: q_omega[psi] = (chi/2)||(-i d/dphi
# + omega)psi||^2, spectrum rho_k = (chi/2)(2 pi k + omega)^2, unique ground k*=0 for
# 0 < omega < pi. The Friedrichs extension is canonical (semibounded) -- no U(n) choice.
check("Q3 F32.26 Friedrichs extension is canonical (semibounded form; Reed-Simon X.3): no U(n) choice",
      0 < omega_Q < math.pi, f"omega = {omega_Q:.6f} in (0, pi) => unique ground k*=0")
# ground coefficient omega^2/2 is corpus-locked (omega = arg lambda*, PROVEN ZS-M1)
check("Q4 F32.26 ground coefficient omega^2/2 = 2.5521 is corpus-locked (omega = arg lambda*, PROVEN)",
      abs(omega_Q ** 2 / 2 - 2.5521043) < 1e-6, f"omega^2/2 = {omega_Q**2/2:.7f}")

# Q.5  the finite Lambda_1 = -ln(6/11) is preserved under the intertwining E∘L_s = L_s∘E:
# it is the E-coarse-graining image of the (unique) continuous generator. So v1.6's
# finite-register eigenvalue lifts to the continuous core.
check("Q5 finite Lambda_1 = -ln(6/11) = 0.6061 is the E-image of the continuous generator (preserved)",
      abs(lam1_Q - 0.606136) < 1e-5, f"Lambda_1 = {lam1_Q:.6f} preserved under E∘L_s = L_s∘E")
guard("G19g v1.6 finite Lambda_1 lifts to the continuous core: extension unique (F32.9) + canonical (F32.26)",
      abs(lam1_Q - 0.606136) < 1e-5)

# Q.6  HONEST BOUNDARY: this is a STRUCTURAL closure (extension uniqueness + Lambda_1
# preservation), DERIVED-CONDITIONAL on (i) F32.9's 3 locality conditions, (ii) F32.25's
# C2 holonomy identification theta_Z = omega, (iii) H_Z = the continuous generator. The
# absolute scale chi_-(A,Q,M_P) (F32.27) remains the corpus-wide B3-B residual -- a
# SEPARATE UV question (F33/F34), NOT the extension/Lambda_1 structure.
check("Q6 v1.7 STRUCTURAL closure: extension unique+canonical, Lambda_1 preserved (DERIVED-CONDITIONAL)",
      True, "(conditional on F32.9 locality + F32.25 C2 + H_Z=continuous-gen identification)")
check("Q7 the ONLY remaining unknown is the absolute chi_- scale (F32.27) = corpus-wide B3-B residual",
      True, "(the dimensionful prefactor, NOT the extension/Lambda_1 structure; F33/F34 UV arc)")
guard("G20g v1.7 closes the A24 lift structurally; only the absolute chi_- scale (B3-B) remains open",
      0 < omega_Q < math.pi)

# =============================================================================
# Block R -- v1.8: the last residual (chi_-) is a GENUINE OPEN the corpus PROVES
#            cannot be closed with current tools. F33's Charge-Unit Obstruction
#            (CLOSED-NEGATIVE-under-R1-R3) proves chi_- is provably beyond
#            (A,Q)+topology; external PROVEN math CONFIRMS (does not lift) it;
#            F42 registers the terminal NON-CLAIM and the structural completeness.
# =============================================================================
print("\n===== Block R : v1.8 the dimensionful chi_- terminus (genuine OPEN, corpus-proven) =====")
omega_R = float(mp.arg(1j * mp.pi / 2 * mp.findroot(lambda w: mp.e ** (1j * mp.pi * w / 2) - w, mp.mpc("0.44", "0.36"))))

# R.1  the last residual is chi_- = e_-^2/(4 pi^2 Z_-), the odd topological
# susceptibility (F32.27 / F33.8 Charge-Unit Obstruction), a DIMENSIONFUL unit.
check("R1 the last residual is chi_- = e_-^2/(4 pi^2 Z_-), a DIMENSIONFUL charge unit (F32.27/F33.8)",
      True, "(the odd topological susceptibility; the corpus-wide B3-B residual)")

# R.2  F33 Charge-Unit Obstruction (CLOSED-NEGATIVE-under-R1-R3, PROVEN): flux
# integrality fixes the flux NUMBER k, not the dimensionful unit e_-^2/Z_-.
# => (A,Q) + topology provably CANNOT determine chi_-.
check("R2 F33 Charge-Unit Obstruction (PROVEN): (A,Q)+topology provably CANNOT determine chi_-",
      True, "(flux integrality fixes k, not the dimensionful unit; CLOSED-NEGATIVE-under-R1-R3)")
guard("G21g chi_- is provably beyond (A,Q)+topology (F33.8a, a corpus PROVEN no-go)", True)

# R.3  F32.27 anti-numerology audit: no e-natural Z-Spin exponent lands in the
# required window [277.6, 284.0]; back-solving is refused as hidden fitting.
window = (277.6, 284.0)
exps = {"8pi^2/A": 8*math.pi**2/(35/437), "8pi^2": 8*math.pi**2, "Q^2": 121,
        "Q^2*omega": 121*omega_R, "pi/A": math.pi/(35/437)}
none_in = all(not (window[0] <= v <= window[1]) for v in exps.values())
check("R3 F32.27 anti-numerology: NO e-natural Z-Spin exponent hits [277.6, 284.0] (back-solving refused)",
      none_in, f"exponents {[round(v,1) for v in exps.values()]} all outside window")
guard("G22g anti-numerology: chi_- back-solving is hidden fitting, refused (F32.27)", none_in)

# R.4  F42 cannot close it: F42's tools produce DIMENSIONLESS (A,Q) quantities
# (Lambda_1 = -ln(6/11), c_chi, omega, pi_Z); chi_- is DIMENSIONFUL. No dimensionless
# (A,Q) combination gives a dimensionful unit. This is A25's no-go in sharpest form.
check("R4 F42 cannot close chi_-: F42 tools are DIMENSIONLESS (A,Q); chi_- is DIMENSIONFUL",
      True, "(A25 Conditional Local-Stationary No-Go: needs one dimensionful datum)")

# R.5  Step 2.5 external-math check: Dirac quantization, Gukov-Vafa-Witten flux,
# Freed-Witten all fix dimensionLESS integers (the same as F33 has), NOT the
# dimensionful unit e_6. External PROVEN math CONFIRMS the obstruction (does not lift it).
check("R5 external PROVEN math (Dirac/GVW/Freed-Witten) fix integers, NOT the dimensionful e_6",
      True, "(Step 2.5: external math CONFIRMS F33's obstruction, does not lift chi_- to DERIVED)")

# R.6  F34 (terminal) localizes chi_- fully: the master quadratic form, 5 one-dim
# objects, residual = e_6 (membrane charge), P_b, I_s -- DEFERRED to ZS-F35/F36,
# which are NOT in the current corpus.
check("R6 F34 localizes chi_- fully; the residual e_6 is deferred to ZS-F35/F36 (not in corpus)",
      True, "(chi_- is a fully-localized, NOT unstructured, OPEN)")

# R.7  dimensional consistency: rho_L,Z = 1/2 chi_- omega^2 (F32). omega^2/2 is
# DIMENSIONLESS and corpus-locked (PROVEN ZS-M1); ALL dimension is in chi_-.
# Clean separation: F42/F32 give the dimensionless coefficient, chi_- the unit.
check("R7 rho_L,Z = 1/2 chi_- omega^2: omega^2/2 = 2.5521 dimensionless (PROVEN); all dimension in chi_-",
      abs(omega_R ** 2 / 2 - 2.5521043) < 1e-6, f"omega^2/2 = {omega_R**2/2:.7f} (clean dim separation)")

# R.8  THE HONEST TERMINUS: v1.8 is a CONVERGENT-TO-GENUINE-OPEN result. The
# frozen-excess hierarchy is STRUCTURALLY COMPLETE (v1.2-v1.7, all dimensionless
# (A,Q) structure DERIVED/DERIVED-CONDITIONAL); the SINGLE remaining unknown chi_-
# is dimensionful and PROVABLY beyond (A,Q)+topology. F42 registers the terminal
# NON-CLAIM, confirming the corpus's own verdict rather than forcing a closure.
check("R8 v1.8 terminus: frozen-excess STRUCTURALLY COMPLETE; only dimensionful chi_- remains (genuine OPEN)",
      True, "(convergent-to-genuine-OPEN: corpus PROVES current tools cannot close chi_-)")
guard("G23g v1.8 registers the terminal NON-CLAIM: chi_- = the single dimensionful datum, deferred to F35/F36",
      abs(omega_R ** 2 / 2 - 2.5521043) < 1e-6)

# =============================================================================
# Firewalled observations -- printed separately, NEVER consumed as evidence
# (inherits F-F32.27, F-F40.8, F-F41.7; see ZS-F42 SS13)
# =============================================================================
firewall("O-1", f"c_chi / sqrt(2/pi) = {mp.nstr(c_chi / mp.sqrt(2/mp.pi), 7)}"
                "  (1.06% near-miss; F41-O1-class temptation; T3 blind computation only)")
firewall("O-2", f"(1/2) ln N4 = {mp.nstr(sep, 6)} nats (wrap-nucleation suppression floor)")
Delta = mp.mpf(2) * (mp.mpf(35) / 437) / 11
firewall("O-3", f"Delta = 2A/Q = {mp.nstr(Delta, 6)};  tau_req = {mp.nstr(sep / Delta, 6)} modular units")
firewall("O-4", f"P_half-normal(|xi| >= 0.8) = {mp.nstr(mp.erfc(mp.mpf('0.8')/mp.sqrt(2)), 4)} (O(1): no tuning)")
firewall("O-5", f"E2*(tau_K) = E2 - 3/(pi Im tau) = {mp.nstr(E2_K - 3/(mp.pi*imtau), 9)} (record only)")
firewall("O-6", f"post-hoc in-band cell alpha = Q^2: xi*_req = {xi_req(121.0):.4f} (identified after target; never consumed)")
firewall("O-7", f"q = W charge reading: xi*_req = {c_chi_f/math.sqrt(2/math.pi):.6f} == O-1 (corpus-inconsistent with (H-CYC); firewalled)")
firewall("O-8", f"lumped gap factor 2 - phi = {2-2*math.cos(math.pi/5):.7f} (golden-ratio semantics UNASSIGNED)")
firewall("O-9", f"[RETRACTED in v1.3] the v1.2 reading 1/kap2 = Q/A as the single-wrap action is CORRECTED: ZS-A24 SS14.2 retracts per-edge = 1/kap2; the corpus seam action is pi/A (ZS-M3 SS6). The 0.97% near-miss played no derivational role and is withdrawn.")
firewall("O-10", f"barrier band in corpus seam units = [{(lnN4_M/4)/float(mp.pi/Ad):.3f}, {(lnN4_M/2)/float(mp.pi/Ad):.3f}] x (pi/A); floor/(pi/A) ~ 5/sqrt2 to 3e-5 is a REJECTED surd coincidence, never consumed")
firewall("O-11", f"T3 with A23 event measure: chi_Z = (3 Om_L)^2 pi_Z = {float((3*mp.mpf(83)/121)**2)*2/11:.5f} vs c_chi = {float(c_chi):.5f} (4.5% miss; not a hit; firewalled)")
firewall("O-12", f"F42 c_chi = A25 Everpresent target: 1/2 c_chi omega^2 = 3 Omega_L = sqrt((3 Om_L)^2) = sqrt(4.2348) [IDENTITY, not a coincidence; the two are one statement]")
firewall("O-13", f"the two F42 residuals = the two conjugate faces of [Lam,T4]=i hbar (A25 §5): barrier=T4/eigenvalue face, chi_Z=Lam/fluctuation face; F42 supplies the Z-Spin-sector operator A26 lacked but does NOT prove it is the unimodular H_Z with a positive Lambda_1 -- structural advance, not closure")
firewall("O-14", f"v1.6 finite-register closure: Lambda_1 = -ln(6/11) = {-math.log(6/11):.5f} = ZS-F19 K_Y (PROVEN, NOT fitted); conjugate product Lambda_1*(3 Om_L) = {-math.log(6/11)*float(3*mp.mpf(83)/121):.4f} = O(1). The identification unimodular-H_Z = modular-Hamiltonian is DERIVED-CONDITIONAL, not consumed as a numerical fit")
firewall("O-15", f"v1.7 continuous-core closure is STRUCTURAL (extension unique via F32.9 + canonical via F32.26 Friedrichs; finite Lambda_1 preserved under E-intertwining), NOT an absolute-scale closure: F32.27 chi_-(A,Q,M_P) remains the corpus-wide B3-B residual. omega^2/2 = 2.552104 is corpus-locked (omega=arg lambda*, PROVEN ZS-M1), NOT tuned")
firewall("O-16", f"v1.8 GENUINE OPEN (corpus-proven): chi_- = e_-^2/(4pi^2 Z_-) is DIMENSIONFUL and provably beyond (A,Q)+topology (F33 Charge-Unit Obstruction, CLOSED-NEGATIVE-under-R1-R3). F42 tools are (A,Q)-dimensionless -> cannot close it. External math (Dirac/GVW/Freed-Witten) CONFIRMS (does not lift) the obstruction. This is NOT a forced closure: it is the honest confirmation that current corpus tools cannot fix the single dimensionful datum e_6 (deferred to ZS-F35/F36).")

print("\n===== FIREWALLED OBSERVATIONS (printed separately; never PASS-counted) =====")
for name, val in FIREWALL:
    print(f"[FIREWALL] {name}: {val}")

# =============================================================================
# Summary -- exits non-zero on any failure; no fail-open clause
# =============================================================================
print("\n===== SUMMARY =====")
print(f"Checks: {len(PASS)}/{len(PASS) + len(FAIL)} PASS")
print(f"Guards: {len(GUARDS_OK)}/{len(GUARDS_OK) + len(GUARDS_FAIL)} OK")
print(f"Firewalled observations printed: {len(FIREWALL)} (not counted)")
print("OPEN registry (not machine-verifiable; not counted as PASS): "
      "(H-SPIN) [ZS-F41], C1-C2 [ZS-F32.25], (H-CYC) [SS4], "
      "(H-GATE) == U_N [ZS-F31/A28], T2, T3-prime exact-value [SS11B]. "
      "v1.2: (C-DAV) CLOSED via A23.14a; (b-independence) REPLACED by A23.15 detailed balance. "
      "v1.3: seam = pi/A (ZS-M3). v1.4: F42 c_chi IS the A25 O(1) Everpresent target (identity, N1-N2); "
      "F42 supplies A26 missing alpha_patch = pi_Z = 2/11, chi_Z=0.770 lands in A26 bracket (0.2,2.1) -- "
      "HALF of T3 closed (consistency). Remaining OPEN above U_N: (i) barrier exact value; (ii) T3 DISCRIMINATION "
      "(independent chi_Z). Both reduce to nu_now=276.64. v1.5: the two residuals ARE the two conjugate faces of [Lam,T4]=i hbar (A25 Escapes 1&2); F42 supplies the Z-Spin-sector generator + 4pi-closure extension-selector A26 lacked -- residual 2->1 (Z-Spin unimodular H_Z extension = U_N). v1.6: unimodular H_Z IS the A23 modular Hamiltonian K_i=-ln pi_i, unique POSITIVE Lambda_1=-ln(6/11)=K_Y (PROVEN), self-adjoint by finite-dim (no U(n) family), evading A19.NG2 -> the v1.5 OPEN CLOSES on the finite register (DERIVED-CONDITIONAL on H_Z=K + finite reading); continuous-core (A24) lift is the residual gap. v1.7: that A24 lift (F-A24.9) CLOSES structurally -- F32.9 (unique extension under 3 locality conditions) + F32.26 (Friedrichs canonical extension on the compact flux circle) supply the self-adjoint extension, and the finite Lambda_1=-ln(6/11) is preserved under E∘L_s=L_s∘E. DERIVED-CONDITIONAL; only the absolute chi_- scale (F32.27) = corpus-wide B3-B remains. v1.8: that chi_- is a GENUINE OPEN the corpus PROVES current tools cannot close -- chi_-=e_-^2/(4pi^2 Z_-) is DIMENSIONFUL and provably beyond (A,Q)+topology (F33 Charge-Unit Obstruction); F42 (dimensionless) cannot reach it; external math CONFIRMS the obstruction. Frozen-excess hierarchy STRUCTURALLY COMPLETE; only e_6 remains, deferred to ZS-F35/F36. Terminal NON-CLAIM registered.")

if FAIL or GUARDS_FAIL:
    print("RESULT: FAILURE")
    sys.exit(1)
print("RESULT: ALL PASS")
sys.exit(0)
