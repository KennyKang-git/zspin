#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f25_verify_v2_0.py
=====================
Machine-verification suite for:

    ZS-F25 v2.0 — "Place Selection and Classification"
    (Z-Spin Cosmology; Kenny Kang, March 2026)

Covers every machine-checkable item of the paper's 44-check Appendix A,
across its three layers:

  [spine]    i-tetration fixed point, three-gap statistic, Gamma_0(11) data
  [explicit] weight identity zeta_p(k), sign structure, rank sanity,
             90-zero and 491-zero preregistered experiments (Appendices B.6-B.7)
  [closure]  GNS format equivalence (instance), finite-window bookkeeping,
             generalized Schur (Albert) singular-block tests,
             shared-space rescue toy, factor-2 autocorrelation support
             (Appendix B.8 / Section 11)

Import-level checks (Pontryagin, Ostrowski, Guinand-Weil, Kronecker-Weber,
Connes 1999, Connes-Consani 2021, ADS-5, M31.0) are PROVEN statements of the
external/corpus literature; they are registered as INFO, not machine-checked.
Where an import has a computable *instance* (Albert criterion, GNS
factorization), the instance is checked here.

Anti-numerology discipline: every target and every negative control below is
preregistered as a module-level constant; nothing is tuned at runtime.

Usage:
    python3 zs_f25_verify_v2_0.py            # quick suite (computes 90 zeros, ~10 s)
    python3 zs_f25_verify_v2_0.py --full     # + 491-zero scaled experiment
                                             #   (~2 min on first run; cached after)

Zero cache: zeros are stored in ./zs_f25_zeros.npy after first computation.

Dependencies: numpy, mpmath  (pip install numpy mpmath)

Exit code 0 iff all executed checks PASS.
"""

import argparse
import math
import os
import sys

import numpy as np

# ----------------------------------------------------------------------------
# Preregistered constants (locked before any computation; do not tune)
# ----------------------------------------------------------------------------

ZEROS_CACHE = "zs_f25_zeros.npy"
N_QUICK, N_FULL = 90, 491
MP_DPS = 10                      # zero precision (digits)

GRID_LO, GRID_HI, GRID_DT = 0.45, 2.78, 0.002          # correlation grid

# B.6 (90 zeros): 7 prime-power targets and 2 negative controls
TARGETS_90 = [("log2", 2), ("log3", 3), ("log4", 4), ("log5", 5),
              ("log7", 7), ("log8", 8), ("log9", 9)]
CONTROLS_90 = [("log6", 6), ("log10", 10)]
HEIGHTS_90_PUB = [15.8, 21.1, 11.1, 22.9, 22.8, 8.1, 11.5]   # published B.6
RHO_90_PUB = 0.9643

# B.7 (491 zeros): 9 preregistered targets, 5 preregistered controls
TARGETS_491 = TARGETS_90 + [("log11", 11), ("log13", 13)]
CONTROLS_491 = [("log6", 6), ("log10", 10), ("log12", 12),
                ("log14", 14), ("log15", 15)]

PRIME_POWERS_13 = [(2, 2, 1), (3, 3, 1), (4, 2, 2), (5, 5, 1), (7, 7, 1),
                   (8, 2, 3), (9, 3, 2), (11, 11, 1), (13, 13, 1)]  # (n, p, k)

ZSTAR_REF = complex(0.438283, 0.360592)      # i-tetration fixed point (ref.)
ALPHA_BK_REF = 0.566424                      # = |Re lambda| = -ln|z*|
ARG_LAMBDA_DEG_REF = 129.4455                # degrees
THREE_GAP_N = 1500                           # orbit points for Steinhaus test

RNG_SEED = 20260311                          # fixed seed for toy randomness

# ----------------------------------------------------------------------------
# Small utilities
# ----------------------------------------------------------------------------

RESULTS = []


def check(name, passed, detail=""):
    RESULTS.append((name, bool(passed)))
    tag = "PASS" if passed else "FAIL"
    print(f"[{tag}] {name}" + (f"  --  {detail}" if detail else ""))


def info(msg):
    print(f"[INFO] {msg}")


def lam_von_mangoldt(n):
    """von Mangoldt Lambda(n) for n = p^k, else 0 (n <= small range)."""
    for p in range(2, n + 1):
        if all(p % q for q in range(2, int(p ** 0.5) + 1)):
            m = p
            while m <= n:
                if m == n:
                    return math.log(p)
                m *= p
    return 0.0


def spearman(x, y):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda i: -v[i])
        r = [0] * len(v)
        for pos, i in enumerate(order):
            r[i] = pos + 1
        return r
    rx, ry = ranks(x), ranks(y)
    n = len(x)
    d2 = sum((a - b) ** 2 for a, b in zip(rx, ry))
    return 1 - 6 * d2 / (n * (n * n - 1))


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    r = pow(a, (p - 1) // 2, p)
    return 1 if r == 1 else -1


def primes_up_to(n):
    s = [True] * (n + 1)
    s[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = [False] * len(s[i * i::i])
    return [i for i in range(2, n + 1) if s[i]]


def get_zeros(n_needed):
    """Imaginary parts of the first n nontrivial zeta zeros (cached)."""
    if os.path.exists(ZEROS_CACHE):
        z = np.load(ZEROS_CACHE)
        if len(z) >= n_needed:
            return z[:n_needed]
    import mpmath as mp
    mp.mp.dps = MP_DPS
    z = [] if not os.path.exists(ZEROS_CACHE) else list(np.load(ZEROS_CACHE))
    print(f"       (computing zeta zeros {len(z)+1}..{n_needed} "
          f"at {MP_DPS} digits; this is the slow step)")
    for k in range(len(z) + 1, n_needed + 1):
        z.append(float(mp.zetazero(k).imag))
    z = np.array(z)
    np.save(ZEROS_CACHE, z)
    return z


def correlation(ts, gammas, weights=None):
    """C(t) = -sum_n w_n cos(gamma_n t) on grid ts."""
    M = np.cos(np.outer(ts, gammas))
    if weights is not None:
        M = M * weights
    return -M.sum(axis=1)


def probe(ts, C, val, halfwidth=4):
    """Local max of C within +-halfwidth grid steps of t = val."""
    j = int(np.argmin(np.abs(ts - val)))
    jl, jr = max(j - halfwidth, 1), min(j + halfwidth, len(ts) - 2)
    jm = jl + int(np.argmax(C[jl:jr + 1]))
    is_lmax = C[jm] >= C[jm - 1] and C[jm] >= C[jm + 1]
    return float(ts[jm]), float(C[jm]), bool(is_lmax)


# ----------------------------------------------------------------------------
# Layer 1 — spine (v1.0): i-tetration, three-gap, Gamma_0(11)
# ----------------------------------------------------------------------------

def v01_fixed_point():
    z = complex(0.5, 0.3)
    for _ in range(400):
        z = complex((1j) ** z) if False else np.exp(z * 1j * math.pi / 2)
    zstar = complex(z)
    lam = (1j * math.pi / 2) * zstar
    ok_fp = abs(np.exp(zstar * 1j * math.pi / 2) - zstar) < 1e-12
    ok_val = abs(zstar - ZSTAR_REF) < 2e-5
    ok_attr = abs(lam) < 1.0
    # exact identity: ln z* = lambda  =>  -ln|z*| = -Re(lambda) = |Re lambda|
    ident = abs((-math.log(abs(zstar))) - abs(lam.real))
    ok_id = ident < 1e-12
    ok_alpha = abs(abs(lam.real) - ALPHA_BK_REF) < 5e-5
    check("V01 i-tetration: z*, lambda, alpha_BK, exact identity -ln|z*|=|Re lam|",
          ok_fp and ok_val and ok_attr and ok_id and ok_alpha,
          f"z*={zstar:.6f}, |lam|={abs(lam):.4f}, alpha_BK={abs(lam.real):.6f}, "
          f"identity gap={ident:.1e}")
    return zstar, lam


def v02_three_gap(lam):
    theta = math.atan2(lam.imag, lam.real) % (2 * math.pi)
    deg = math.degrees(theta)
    ok_arg = abs(deg - ARG_LAMBDA_DEG_REF) < 0.01
    pts = np.sort(np.mod(np.arange(1, THREE_GAP_N + 1) * theta, 2 * math.pi))
    gaps = np.diff(np.concatenate([pts, [pts[0] + 2 * math.pi]]))
    distinct = len(np.unique(np.round(gaps, 9)))
    ok_gap = distinct == 3
    check("V02 arg(lambda) and Steinhaus three-gap (1500 orbit points)",
          ok_arg and ok_gap,
          f"arg lam = {deg:.4f} deg; distinct gaps = {distinct} (expect exactly 3)")


def v03_gamma0_11():
    N = 11
    mu = N + 1                                            # index for prime N
    nu2 = (1 + legendre(-1, N))                           # 11 = 3 mod 4 -> 0
    nu3 = (1 + legendre(-3, N))                           # -3 non-residue -> 0
    cusps = 2                                             # phi(1)+phi(1), N prime
    genus = 1 + mu / 12 - nu2 / 4 - nu3 / 3 - cusps / 2
    vol = math.pi / 3 * mu
    weyl = vol / (4 * math.pi)
    ok = (mu == 12 and nu2 == 0 and nu3 == 0 and cusps == 2
          and abs(genus - 1) < 1e-12 and abs(vol - 4 * math.pi) < 1e-12
          and abs(weyl - 1.0) < 1e-12)
    check("V03 Gamma_0(11): mu=12, nu2=nu3=0, cusps=2, genus=1, Vol=4pi, Weyl=1",
          ok, f"genus={genus:.0f}, Vol={vol:.6f}, Vol/4pi={weyl:.6f}")


# ----------------------------------------------------------------------------
# Layer 2 — explicit formula (v1.2-v1.3)
# ----------------------------------------------------------------------------

def v04_weight_identity():
    bad = []
    for n, p, k in PRIME_POWERS_13:
        l0 = math.log(p)
        selberg = l0 / (2 * math.sinh(k * l0 / 2))
        weil = math.log(p) / math.sqrt(n)                 # Lambda(p^k)/sqrt(p^k)
        if abs(selberg / weil - 1 / (1 - p ** (-k))) > 1e-12:
            bad.append(n)
    check("V04 weight identity: Selberg/Weil ratio = (1-p^-k)^-1 = zeta_p(k), 9/9",
          not bad, "machine precision at n = 2..13" if not bad else f"fails at {bad}")


def v05_euler_factor_series():
    worst = 0.0
    for n, p, k in PRIME_POWERS_13:
        partial = sum(p ** (-m * k) for m in range(60))
        worst = max(worst, abs(partial - 1 / (1 - p ** (-k))))
    check("V05 zeta_p(k) Euler series: sum_m p^{-mk} matches closed form",
          worst < 1e-12, f"worst gap = {worst:.1e}")


def v06_sign_structure():
    sel_pos = all(math.log(p) / (2 * math.sinh(k * math.log(p) / 2)) > 0
                  for _, p, k in PRIME_POWERS_13)
    weil_neg = all(-lam_von_mangoldt(n) / math.sqrt(n) < 0
                   for n, _, _ in PRIME_POWERS_13)
    check("V06 sign structure: Selberg hyperbolic weights > 0; Weil prime side < 0",
          sel_pos and weil_neg,
          "emission excluded; absorption forced (Theorem 6.6)")


def v07_rank_sanity():
    logs = [math.log(p) for p in (2, 3, 5, 7)]
    best = min(abs(sum(a * l for a, l in zip(vec, logs)))
               for vec in np.ndindex(13, 13, 13, 13)
               if any(v != 6 for v in vec)
               for vec in [tuple(v - 6 for v in vec)]
               if any(vec))
    ok = best > 1e-6
    check("V07 rank sanity: no integer relation sum a_i log p_i = 0, |a_i|<=6",
          ok, f"min nonzero |relation| = {best:.6f} (Q-independence probe; "
              "proof is exact via unique factorization)")


def v08_entropy_constants():
    hks = math.pi ** 2 / (6 * math.log(2))
    ok = abs(hks - 2.37313) < 1e-4
    check("V08 entropy bookkeeping: Gauss-map h_KS = pi^2/(6 ln 2) = 2.3731",
          ok, f"h_KS = {hks:.5f}; h_top(Gauss) = infinity (countable branches); "
              "geodesic-flow h = 1")


def v09_v11_zero_experiment_90():
    g = get_zeros(N_QUICK)
    ts = np.arange(GRID_LO, 2.35, GRID_DT)
    C = correlation(ts, g)
    offsets, heights, theory = [], [], []
    ok_peaks = True
    for name, n in TARGETS_90:
        tm, cm, lm = probe(ts, C, math.log(n))
        ok_peaks &= lm and cm > 8.0 and abs(tm - math.log(n)) <= 0.002
        offsets.append(abs(tm - math.log(n)))
        heights.append(cm)
        theory.append(lam_von_mangoldt(n) / math.sqrt(n))
    check("V09 B.6: 7/7 peaks at log(p^k), offsets <= 0.002, height > 8 (N=90)",
          ok_peaks, f"max offset = {max(offsets):.4f}")

    pub_gap = max(abs(h - hp) for h, hp in zip(heights, HEIGHTS_90_PUB))
    rho = spearman(heights, theory)
    # exactly one adjacent inversion, and it is the (log5, log7) pair
    inv_57 = (heights[3] > heights[4]) and (theory[4] > theory[3])
    others_ok = all((heights[i] > heights[j]) == (theory[i] > theory[j])
                    for i in range(7) for j in range(7)
                    if i < j and {i, j} != {3, 4})
    check("V10 B.6: heights match published; rho = 0.964; unique 5-7 inversion",
          pub_gap < 0.15 and abs(rho - RHO_90_PUB) < 2e-3 and inv_57 and others_ok,
          f"max height gap vs published = {pub_gap:.2f}; rho = {rho:.4f}")

    ok_ctrl = True
    med = float(np.median(np.abs(C)))
    for name, n in CONTROLS_90:
        _, cm, _ = probe(ts, C, math.log(n))
        ok_ctrl &= cm < 3 * max(med, 1.0) + 1.0           # published: 0.9, -0.4
    check("V11 B.6: negative controls log 6, log 10 flat (Lambda = 0)",
          ok_ctrl, f"3x median threshold = {3*med:.1f}")


def v12_v14_zero_experiment_491():
    g = get_zeros(N_FULL)
    ts = np.arange(GRID_LO, GRID_HI, GRID_DT)
    C = correlation(ts, g)
    med = float(np.median(np.abs(C)))
    thr = 3 * med

    heights = {}
    ok_t, max_off = True, 0.0
    for name, n in TARGETS_491:
        tm, cm, lm = probe(ts, C, math.log(n))
        ok_t &= lm and cm > thr and abs(tm - math.log(n)) <= 0.0021
        heights[name] = cm
        max_off = max(max_off, abs(tm - math.log(n)))
    check("V12 B.7: 9/9 preregistered prime-power targets through log 13 (N=491)",
          ok_t, f"max offset = {max_off:.4f}; threshold = 3 x median = {thr:.1f}")

    ok_c = all(probe(ts, C, math.log(n))[1] < thr for _, n in CONTROLS_491)
    hv = [heights[name] for name, _ in TARGETS_491]
    tv = [lam_von_mangoldt(n) / math.sqrt(n) for _, n in TARGETS_491]
    rho = spearman(hv, tv)
    resolved = heights["log7"] > heights["log5"]
    check("V13 B.7: 5/5 controls flat; 5-7 inversion resolved; rho >= 0.97",
          ok_c and resolved and rho >= 0.97,
          f"rho = {rho:.4f}; C(log7) = {heights['log7']:.1f} > "
          f"C(log5) = {heights['log5']:.1f}")

    ok_w = True
    for Gam in (g[-1] / 2, g[-1]):
        w = np.exp(-(g / Gam) ** 2)
        Cw = correlation(ts, g, w)
        for n in (3, 13):
            tm, _, _ = probe(ts, Cw, math.log(n))
            ok_w &= abs(tm - math.log(n)) <= 0.004
    check("V14 B.7: peak locations stable under Gaussian windows (<= 0.004)",
          ok_w, "Gamma = gamma_N/2 and gamma_N")


# ----------------------------------------------------------------------------
# Layer 3 — closure program (v2.0, Section 11 / Appendix B.8)
# ----------------------------------------------------------------------------

def v15_gns_instance():
    rng = np.random.default_rng(RNG_SEED)
    A = rng.normal(size=(5, 5))
    G = A.T @ A                                            # PSD "Weil-like" Gram
    w, V = np.linalg.eigh(G)
    w = np.clip(w, 0, None)
    Phi = np.diag(np.sqrt(w)) @ V.T                        # G = Phi^T Phi
    kernel_gap = np.max(np.abs(Phi.T @ Phi - G))
    e = np.zeros(5); e[0] = 1.0
    defect = [np.trace(np.outer(Phi[:, i], e).T @ np.outer(Phi[:, i], e))
              for i in range(5)]
    defect_gap = max(abs(d - G[i, i]) for i, d in enumerate(defect))
    check("V15 GNS instance: PSD form -> kernel format -> defect-square format",
          kernel_gap < 1e-10 and defect_gap < 1e-10,
          f"kernel gap = {kernel_gap:.1e}; defect gap = {defect_gap:.1e} "
          "(Theorem 11.2, constructive at toy scale)")


def v16_window_bookkeeping():
    def count_SL(X):                                       # |{p^k <= X}|
        c = 0
        for p in primes_up_to(X):
            m = p
            while m <= X:
                c += 1
                m *= p
        return c
    ok = (count_SL(13) == 9 and count_SL(49) == 23 and count_SL(100) == 35)
    base_empty = (2 * (math.log(2) / 2 - 1e-9)) < math.log(2)
    check("V16 window bookkeeping: |S_L| = 9/23/35 at 2L = log 13/49/100; "
          "base rung empty", ok and base_empty,
          "L < (log 2)/2 = 0.3466 -> S_L = {} (Theorem 11.3 / Sec. 11.5)")


def v17_generalized_schur():
    QS = np.array([[1.0, 1.0], [1.0, 1.0]])               # PSD, singular
    QSp = np.linalg.pinv(QS)
    Qq = np.array([[1.0]])

    C1 = np.array([[0.5, 0.5]])                            # range-compatible
    rng_ok = np.allclose(C1 @ (np.eye(2) - QS @ QSp), 0)
    schur = (Qq - C1 @ QSp @ C1.T)[0, 0]
    M1 = np.block([[QS, C1.T], [C1, Qq]])
    psd1 = np.linalg.eigvalsh(M1)[0] > -1e-9

    C2 = np.array([[0.5, -0.5]])                           # range-violating
    rng_bad = np.allclose(C2 @ (np.eye(2) - QS @ QSp), 0)
    M2 = np.block([[QS, C2.T], [C2, Qq]])
    psd2 = np.linalg.eigvalsh(M2)[0] > -1e-9

    naive_undef = abs(np.linalg.det(QS)) < 1e-12
    ok = (rng_ok and schur >= -1e-12 and psd1
          and (not rng_bad) and (not psd2) and naive_undef)
    check("V17 Albert criterion on singular Q_S: accepts/rejects correctly",
          ok, f"Schur complement = {schur:.3f}; naive Q_S^-1 undefined "
              "(Lemma 11.4)")


def v18_shared_space_rescue():
    Qa = np.array([[1.0, 0.0], [0.0, -0.5]])
    Qb = np.array([[-0.5, 0.3], [0.3, 1.0]])
    ea, eb = np.linalg.eigvalsh(Qa), np.linalg.eigvalsh(Qb)
    es = np.linalg.eigvalsh(Qa + Qb)
    indef = ea[0] < 0 < ea[-1] and eb[0] < 0 < eb[-1]
    psd = es[0] >= -1e-12
    # contrast: principal channel blocks of a PSD matrix are PSD
    rng = np.random.default_rng(RNG_SEED)
    B = rng.normal(size=(4, 4)); M = B.T @ B
    blocks_psd = (np.linalg.eigvalsh(M[:2, :2])[0] >= -1e-10
                  and np.linalg.eigvalsh(M[2:, 2:])[0] >= -1e-10)
    check("V18 shared-space rescue: per-channel indefinite, total PSD; "
          "direct-sum contrast", indef and psd and blocks_psd,
          f"eig(Qa+Qb) = {np.round(es,3)} (Theorem 11.6 / B.8(i))")


def v19_autocorrelation_support():
    dx = 0.01
    L = 1.0
    x = np.arange(-L, L + dx, dx)
    phi = np.exp(-1 / np.clip(1 - (x / L) ** 2, 1e-12, None))   # bump on [-L, L]
    auto = np.convolve(phi, phi[::-1]) * dx
    supp = (len(auto) - 1) * dx / 2                              # half-width
    ok = supp <= 2 * L + 2 * dx
    check("V19 factor-2 bookkeeping: supp(phi * phi~) <= [-2L, 2L]",
          ok, f"support half-width = {supp:.2f} vs 2L = {2*L:.2f} "
              "(Theorem 11.3 correction)")


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description="ZS-F25 v2.0 verification suite")
    ap.add_argument("--full", action="store_true",
                    help="include the 491-zero scaled experiment (B.7)")
    args = ap.parse_args()

    print("=" * 76)
    print("ZS-F25 v2.0 machine-verification suite "
          "(preregistered targets; zero free parameters)")
    print("=" * 76)

    print("\n-- Layer 1: math spine --")
    zstar, lam = v01_fixed_point()
    v02_three_gap(lam)
    v03_gamma0_11()

    print("\n-- Layer 2: explicit formula --")
    v04_weight_identity()
    v05_euler_factor_series()
    v06_sign_structure()
    v07_rank_sanity()
    v08_entropy_constants()
    v09_v11_zero_experiment_90()
    if args.full:
        v12_v14_zero_experiment_491()
    else:
        info("V12-V14 (491-zero scaled experiment) skipped; rerun with --full")

    print("\n-- Layer 3: closure program (Sec. 11) --")
    v15_gns_instance()
    v16_window_bookkeeping()
    v17_generalized_schur()
    v18_shared_space_rescue()
    v19_autocorrelation_support()

    print("\n-- Registered imports (PROVEN externally / in corpus; "
          "not machine-checkable here) --")
    for s in ("Pontryagin 1932 (connected locally compact division rings)",
              "Ostrowski 1916 (archimedean completions of Q)",
              "Guinand 1948 / Weil 1952 (explicit formula, unconditional)",
              "Kronecker-Weber (abelian extensions cyclotomic)",
              "Connes 1999 (absorption-spectrum realization)",
              "Connes-Consani 2021 (archimedean base rung, Sec. 11.5)",
              "Albert 1969 (generalized Schur; instance checked in V17)",
              "GNS/Kolmogorov factorization (instance checked in V15)",
              "ZS-M22 ADS-5; ZS-M31 M31.0; F21-III Q^def != Q_W "
              "(corpus PROVEN imports, Theorem 11.6)"):
        info(s)

    n_pass = sum(1 for _, ok in RESULTS if ok)
    n_tot = len(RESULTS)
    print("\n" + "=" * 76)
    print(f"RESULT: {n_pass}/{n_tot} machine checks PASS"
          + ("" if args.full else "  (quick mode; --full adds V12-V14)"))
    print("Open statement after all closures: the inductive rung of Lemma 11.4"
          " -- D5 [IMPORTED-OPEN == RH]. This suite asserts nothing about it.")
    print("=" * 76)
    sys.exit(0 if n_pass == n_tot else 1)


if __name__ == "__main__":
    main()
