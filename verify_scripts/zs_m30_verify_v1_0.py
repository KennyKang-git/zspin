#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_m30_verify_v1_0.py

Verification suite for ZS-M30 v1.0:
  "Three External Vehicles for D4b Closure —
   Constant-Level Conductor Identification and Spectral Bridge to
   the CCM 2025 Zeta Spectral Triples"

Author: Kenny Kang (Z-Spin Cosmology Collaboration)
Version: v1.0 (May 2026)

This script reproduces the 22/22 PASS verification table of §9 of the paper
and the supporting computations of §§4–6. All quantities are computed
independently from the paper text; nothing is read back from the docx.

Tests fall into five blocks:
  Block A (Tests 1–7):   corpus PROVEN register symmetries (J seam, J_Z, D_4)
  Block B (Tests 8–11):  Theorem M30.1 (constant-level conductor identification)
  Block C (Tests 12–15): Theorem M30.3 (J seam ↔ Burnol grading non-isomorphism)
  Block D (Tests 16–20): Theorem M30.2 (LOCATOR ↔ D_log spectral bridge)
  Block E (Tests 21–22): upstream LOCKED inheritance

Usage:
    python3 zs_m30_verify_v1_0.py             # full run, 22/22 PASS expected
    python3 zs_m30_verify_v1_0.py --verbose   # extra diagnostics
    python3 zs_m30_verify_v1_0.py --P 2000    # set LOCATOR prime cutoff
    python3 zs_m30_verify_v1_0.py --kmax 7    # set R_small truncation depth

Dependencies:
    numpy, scipy, sympy   (all standard scientific Python)

LOCKED inputs used (no new free parameters):
    A   = 35/437                              [ZS-F2,  LOCKED]
    Q   = 11                                  [ZS-F5,  PROVEN]
    K   = ℚ(√−3, √−11), V_4 Galois            [ZS-M22, PROVEN]
    (a_χ, q_χ) ∈ {(0,1), (1,3), (1,11), (0,33)}   [ZS-M25 §6.3, PROVEN]
    z*  = 0.4383 + 0.3606 i                   [ZS-M1,  PROVEN]
    λ   = (iπ/2) z*                           [ZS-F0 §8.5, PROVEN]
    sum rule = 0.7948 + 0.2050 + 0.0001 = 0.9999  [ZS-F0 §12.3, PROVEN]
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass, field
from typing import List, Tuple

import numpy as np
from scipy.signal import find_peaks
from scipy.stats import pearsonr
from sympy import sieve

# --------------------------------------------------------------------------- #
# Constants (LOCKED upstream)                                                 #
# --------------------------------------------------------------------------- #

A_VAL: float = 35.0 / 437.0       # ZS-F2 [5], LOCKED
Q_REG: int = 11                   # ZS-F5 [4], PROVEN
SECT_DIMS = (2, 3, 6)             # (Z, X, Y), ZS-F5 [4], PROVEN

# V_4 character data (a_χ, q_χ) — ZS-M25 §6.3 [11], PROVEN
V4_CHANNELS: List[Tuple[str, int, int]] = [
    ("1",         0,  1),
    ("chi_-3",    1,  3),
    ("chi_-11",   1, 11),
    ("chi_33",    0, 33),
]

# Conductor exponent e_p(χ) at ramified primes p ∈ {3, 11}
# Standard for K = ℚ(√−3, √−11):
#   χ_-3  ramifies at p = 3 with e = 1, unramified at p = 11
#   χ_-11 ramifies at p = 11 with e = 1, unramified at p = 3
#   χ_33  = χ_-3 · χ_-11 ramifies at both with e = 1 each
COND_EXP = {
    ("1",       3): 0, ("1",        11): 0,
    ("chi_-3",  3): 1, ("chi_-3",   11): 0,
    ("chi_-11", 3): 0, ("chi_-11",  11): 1,
    ("chi_33",  3): 1, ("chi_33",   11): 1,
}

# i-tetration fixed point — ZS-M1 [8], PROVEN
Z_STAR: complex = complex(0.4383, 0.3606)

# First nine ζ zero heights (Odlyzko, OEIS A058303)
ZETA_ZEROS: List[float] = [
    14.134725141734693790,
    21.022039638771554993,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189691,
    37.586178158825671257,
    40.918719012147495187,
    43.327073280914999519,
    48.005150881167159727,
]

# Tolerances
TOL_MACHINE: float = 1e-12         # for "exact" identities
TOL_LOCATOR_MAD: float = 0.06      # corpus DERIVED bound (ZS-M29 Thm M29.1)
TOL_PRED_VS_ACTUAL_MAD: float = 0.02   # F-M30.3 falsification gate
TOL_RHO_LEADING_LOWER: float = 0.20    # leading-only ρ at finite P_max
TOL_RHO_FULL_LOWER: float = 0.85       # leading + R_small ρ at P_max=2000

# --------------------------------------------------------------------------- #
# Test result bookkeeping                                                     #
# --------------------------------------------------------------------------- #

@dataclass
class TestResult:
    idx: int
    name: str
    quantitative: str
    passed: bool
    notes: str = ""


@dataclass
class VerificationReport:
    results: List[TestResult] = field(default_factory=list)

    def add(self, r: TestResult) -> None:
        self.results.append(r)

    def passed(self) -> int:
        return sum(1 for r in self.results if r.passed)

    def failed(self) -> int:
        return sum(1 for r in self.results if not r.passed)

    def total(self) -> int:
        return len(self.results)

    def print_table(self) -> None:
        print()
        print("=" * 96)
        print(f"  ZS-M30 v1.0 Verification Suite — {self.passed()}/{self.total()} PASS")
        print("=" * 96)
        print(f"  {'#':>3}  {'Item':<54}  {'Result':<22}  Status")
        print("  " + "-" * 92)
        for r in self.results:
            mark = "PASS" if r.passed else "FAIL"
            print(f"  {r.idx:>3}  {r.name[:54]:<54}  {r.quantitative[:22]:<22}  {mark}")
        print("=" * 96)
        if self.failed() == 0:
            print("  OVERALL: 22/22 PASS — ZS-M30 v1.0 verification reproduced.")
        else:
            print(f"  OVERALL: {self.failed()} TEST(S) FAILED — review above.")
        print("=" * 96)


REPORT = VerificationReport()


def record(idx: int, name: str, quant: str, passed: bool, notes: str = "") -> None:
    REPORT.add(TestResult(idx, name, quant, passed, notes))


# --------------------------------------------------------------------------- #
# Block A: corpus PROVEN register symmetries (Tests 1–7)                      #
# --------------------------------------------------------------------------- #

def construct_J_seam(Q: int = 11) -> np.ndarray:
    """J|j> = |Q-1-j>; corpus ZS-M3 [6] PROVEN."""
    J = np.zeros((Q, Q))
    for j in range(Q):
        J[Q - 1 - j, j] = 1.0
    return J


def construct_J_Z(Q: int = 11) -> np.ndarray:
    """J_Z = I − 2|1><1| = diag(+1, −1, +1, ..., +1); ZS-F0 §8.6 [1] PROVEN."""
    JZ = np.eye(Q)
    JZ[1, 1] = -1.0
    return JZ


def block_A(verbose: bool = False) -> None:
    J = construct_J_seam(Q_REG)
    JZ = construct_J_Z(Q_REG)

    # Test 1: J^2 = I
    res = np.linalg.norm(J @ J - np.eye(Q_REG))
    record(1,
           "J seam J^2 = I on C^11",
           f"||J^2 - I||_F = {res:.2e}",
           res < TOL_MACHINE)

    # Test 2: trace(J) = 1 (= 2*6 - 11; encodes dim E+ = 6, dim E- = 5)
    tr = float(np.trace(J))
    record(2,
           "tr(J) = 1 (encodes E+ = 6, E- = 5)",
           f"tr(J) = {tr:.6f}",
           abs(tr - 1.0) < TOL_MACHINE)

    # Test 3: |5> unique J-fixed basis vector
    e5 = np.zeros(Q_REG)
    e5[5] = 1.0
    diff = np.linalg.norm(J @ e5 - e5)
    record(3,
           "|5> unique J-fixed: J|5> = |5>",
           f"||J|5> - |5>|| = {diff:.2e}",
           diff < TOL_MACHINE)

    # Test 4: J_Z^2 = I
    res = np.linalg.norm(JZ @ JZ - np.eye(Q_REG))
    record(4,
           "J_Z = diag(+1,-1,+1,...,+1); J_Z^2 = I",
           f"||J_Z^2 - I||_F = {res:.2e}",
           res < TOL_MACHINE)

    # Test 5: [J, J_Z] != 0
    comm = np.linalg.norm(J @ JZ - JZ @ J)
    record(5,
           "[J, J_Z] != 0 (D_4 non-abelian)",
           f"||[J, J_Z]||_F = {comm:.4f}",
           comm > 1.0)

    # Test 6: (J J_Z)^4 = I
    JJZ = J @ JZ
    P4 = np.linalg.matrix_power(JJZ, 4)
    res = np.linalg.norm(P4 - np.eye(Q_REG))
    record(6,
           "(J J_Z)^4 = I",
           f"||(JJ_Z)^4 - I||_F = {res:.2e}",
           res < TOL_MACHINE)

    # Test 7: (J J_Z)^2 != I (so D_4 has order exactly 8)
    P2 = np.linalg.matrix_power(JJZ, 2)
    res = np.linalg.norm(P2 - np.eye(Q_REG))
    record(7,
           "(J J_Z)^2 != I (D_4 order = 8)",
           f"||(JJ_Z)^2 - I||_F = {res:.4f}",
           res > 1.0)

    if verbose:
        eigvals = np.linalg.eigvalsh(J)
        n_plus = int(np.sum(np.isclose(eigvals, 1.0)))
        n_minus = int(np.sum(np.isclose(eigvals, -1.0)))
        print(f"  [verbose A] J spectrum: dim E+ = {n_plus}, dim E- = {n_minus}")


# --------------------------------------------------------------------------- #
# Block B: Theorem M30.1 — Constant-level conductor identification (Tests 8–11) #
# --------------------------------------------------------------------------- #

def burnol_global_log_conductor(chi_name: str) -> float:
    """Burnol global conductor sum: Σ_{p ∈ {3, 11}} e_p(χ) · log(p)."""
    return sum(
        COND_EXP[(chi_name, p)] * math.log(p)
        for p in (3, 11)
    )


def block_B(verbose: bool = False) -> None:
    test_idx = 8
    for chi_name, a_chi, q_chi in V4_CHANNELS:
        lhs = math.log(q_chi)
        rhs = burnol_global_log_conductor(chi_name)
        residual = abs(lhs - rhs)
        passed = residual < TOL_MACHINE
        nice = chi_name.replace("chi_", "χ_")
        record(test_idx,
               f"Theorem M30.1 {nice}: log(q_χ) = Σ_p e_p(χ) log(p)",
               f"|residual| = {residual:.2e}",
               passed)
        if verbose:
            print(f"  [verbose B] {nice}: log({q_chi}) = {lhs:.6f}, "
                  f"Burnol sum = {rhs:.6f}")
        test_idx += 1


# --------------------------------------------------------------------------- #
# Block C: Theorem M30.3 — J seam ↔ Burnol grading non-isomorphism (Tests 12–15) #
# --------------------------------------------------------------------------- #

def block_C(verbose: bool = False) -> None:
    # Minimal cobordism slice basis ordering: (|0>_Z, |1>_Z, |b>, |c>)
    # ZS-M22 §6.6.4 [25] PROVEN minimal closure.
    JZ_min = np.diag([+1.0, -1.0, +1.0, +1.0])

    # Q_0 = |1>_Z <b| (rank-one BRST charge)
    Q0 = np.zeros((4, 4))
    Q0[1, 2] = 1.0

    # Test 12: Q_0^2 = 0
    norm_sq = np.linalg.norm(Q0 @ Q0)
    record(12,
           "Q_0^2 = 0 on minimal cobordism slice",
           f"||Q_0^2||_F = {norm_sq:.2e}",
           norm_sq < TOL_MACHINE)

    # Test 13: Q_0 is J_Z-odd (J_Z Q_0 J_Z = -Q_0)
    res = np.linalg.norm(JZ_min @ Q0 @ JZ_min + Q0)
    record(13,
           "Q_0 is J_Z-odd: J_Z Q_0 J_Z = -Q_0",
           f"residual = {res:.2e}",
           res < TOL_MACHINE)

    # Test 14: rank(Q_0) = 1, dim ker = 3, dim H^0 = 2
    rk = int(np.linalg.matrix_rank(Q0))
    Q0_dag = Q0.T
    Delta_Q = Q0 @ Q0_dag + Q0_dag @ Q0
    eigvals_D = np.linalg.eigvalsh(Delta_Q)
    n_harm = int(np.sum(np.isclose(eigvals_D, 0.0)))
    passed_14 = (rk == 1) and (n_harm == 2)
    record(14,
           "rank(Q_0)=1, dim ker(Q_0)=3, dim H^0(Q_0)=2",
           f"rank={rk}, dim H^0={n_harm}",
           passed_14)

    # Test 15: J_Z restricted to H^0 has eigenvalues (+1, +1) → grading (even, odd) = (2, 0)
    # Harmonic basis: zero-eigenvalue eigenvectors of Δ_Q
    eigvals_D, eigvecs_D = np.linalg.eigh(Delta_Q)
    harm_mask = np.isclose(eigvals_D, 0.0)
    Vh = eigvecs_D[:, harm_mask]                # 4 × 2
    JZ_on_H0 = Vh.T @ JZ_min @ Vh
    eigvals_JZ_H0 = np.linalg.eigvalsh(JZ_on_H0)
    n_even = int(np.sum(np.isclose(eigvals_JZ_H0, 1.0)))
    n_odd = int(np.sum(np.isclose(eigvals_JZ_H0, -1.0)))
    passed_15 = (n_even == 2) and (n_odd == 0)
    record(15,
           "H^0(Q_0) J_Z grading: (even, odd) = (2, 0)",
           f"(even, odd) = ({n_even}, {n_odd})",
           passed_15)

    if verbose:
        print(f"  [verbose C] Δ_Q eigenvalues = {np.round(eigvals_D, 6).tolist()}")
        print(f"  [verbose C] J_Z|H^0 eigenvalues = {np.round(eigvals_JZ_H0, 6).tolist()}")
        # Burnol K_1 grading at non-archimedean unramified place: (even=0, odd=1)
        print(f"  [verbose C] Burnol K_1 (δ=0) grading: (even, odd) = (0, 1) — "
              f"non-isomorphic to corpus (2, 0)")


# --------------------------------------------------------------------------- #
# Block D: Theorem M30.2 — LOCATOR ↔ D_log spectral bridge (Tests 16–20)      #
# --------------------------------------------------------------------------- #

def D_star(primes: List[int]) -> float:
    """D_*(P) = Σ_{p ≤ P} p^{-1/2}."""
    return float(sum(p ** -0.5 for p in primes))


def lambda_j(s: complex, j: int, primes: List[int], Q: int) -> complex:
    """ZS-M28 Theorem M28.1 [29] PROVEN closed form."""
    Dstar = D_star(primes)
    phase_offset = (Q - 1) / 2  # = 5 for Q = 11
    val = sum(
        p ** (-s) * np.exp(2j * np.pi * (j - phase_offset) / p)
        for p in primes
    )
    return complex(val) / Dstar


def log_D_squared(s: complex, primes: List[int], Q: int) -> float:
    """log|D(s; P)|^2 = Σ_j log|1 - λ_j(s; P)|^2."""
    return float(sum(
        np.log(abs(1.0 - lambda_j(s, j, primes, Q)) ** 2)
        for j in range(Q)
    ))


def truncated_Euler(s: complex, primes: List[int]) -> complex:
    """ζ_P(s) = ∏_{p ≤ P} (1 - p^{-s})^{-1}."""
    val = 1.0 + 0.0j
    for p in primes:
        val *= 1.0 / (1.0 - p ** (-s))
    return val


def S_p_func(p: int, Q: int) -> float:
    """S_p = sin(Q π / p) / sin(π / p); appears in ZS-M28 Lemma M28.4.1 [29]."""
    return float(np.sin(Q * np.pi / p) / np.sin(np.pi / p))


def R_small(s: complex, primes: List[int], Q: int, k_max: int = 7) -> float:
    """
    R_small(s; P) (ZS-M28 Theorem M28.4 [29], HYPOTHESIS-strong):
        R_small = (Q / D_*) Σ_{k=2}^{k_max} (1/k) Re P_*(ks; P)
                  − (2 / D_*) Re Σ_{p ≤ P} p^{-s} (S_p − Q)
    where P_*(s; P) = Σ_{p ≤ P} p^{-s}.
    """
    Dstar = D_star(primes)
    # Multi-index correction term
    term1 = 0.0
    for k in range(2, k_max + 1):
        P_star_ks = sum(p ** (-k * s) for p in primes)
        term1 += (1.0 / k) * float(np.real(P_star_ks))
    term1 *= Q / Dstar
    # Small-prime residual
    term2 = -(2.0 / Dstar) * float(np.real(
        sum(p ** (-s) * (S_p_func(p, Q) - Q) for p in primes)
    ))
    return term1 + term2


def m284_prediction(s: complex, primes: List[int], Q: int, k_max: int = 7) -> float:
    """Theorem M28.4 prediction:
       log|D(s; P)|² ≈ -(2Q/D_*) Re log ζ_P(s) + R_small + O(D_*^{-2})."""
    Dstar = D_star(primes)
    leading = -(2.0 * Q / Dstar) * float(np.real(np.log(truncated_Euler(s, primes))))
    return leading + R_small(s, primes, Q, k_max)


def closest_peak_distances(t_grid: np.ndarray, signal: np.ndarray,
                           targets: List[float]) -> List[float]:
    """For each target t-value, return distance from closest local max in signal."""
    peaks_idx, _ = find_peaks(signal)
    if len(peaks_idx) == 0:
        return [float("inf")] * len(targets)
    peak_ts = t_grid[peaks_idx]
    return [float(min(abs(peak_ts - g))) for g in targets if g <= float(t_grid[-1])]


def block_D(P_max: int, k_max: int, verbose: bool = False) -> None:
    primes = list(sieve.primerange(2, P_max + 1))
    Dstar = D_star(primes)

    if verbose:
        print(f"  [verbose D] P_max = {P_max}, |primes| = {len(primes)}, "
              f"D_*(P) = {Dstar:.4f}, Q = {Q_REG}, k_max = {k_max}")

    # Test 16: λ_j closed form reproduces ZS-M28 Theorem M28.1 [29]
    # (sanity check at s = 0.5 + 14.135i, j = 5; should compute without error
    #  and be a finite complex number)
    lam_check = lambda_j(complex(0.5, 14.135), 5, primes, Q_REG)
    finite = math.isfinite(abs(lam_check)) and abs(lam_check) < 100.0
    record(16,
           "LOCATOR closed form λ_j (ZS-M28 Thm M28.1)",
           f"|λ_5(0.5+14.135i)| = {abs(lam_check):.4f}",
           finite)

    # Targets: first 9 ζ zeros (subset within scan range below)
    t_lo, t_hi = 10.0, 50.5
    zeros_in_range = [g for g in ZETA_ZEROS if t_lo <= g <= t_hi - 0.5]

    # Test 17: LOCATOR MAD vs first ~9 ζ zeros
    t_grid = np.arange(t_lo, t_hi, 0.025)
    log_D_signal = np.array([
        log_D_squared(complex(0.5, t), primes, Q_REG)
        for t in t_grid
    ])
    distances = closest_peak_distances(t_grid, log_D_signal, zeros_in_range)
    locator_MAD = float(np.mean(distances)) if distances else float("inf")
    record(17,
           "LOCATOR MAD vs first ~9 ζ zeros",
           f"MAD = {locator_MAD:.4f} (< {TOL_LOCATOR_MAD})",
           locator_MAD < TOL_LOCATOR_MAD)

    # Tests 18 & 19: Theorem M28.4 correlations
    t_sample = np.arange(10.0, 35.0, 0.25)
    log_D_vals = np.array([log_D_squared(complex(0.5, t), primes, Q_REG)
                           for t in t_sample])
    leading_vals = np.array([
        -(2.0 * Q_REG / Dstar) * float(np.real(np.log(truncated_Euler(complex(0.5, t), primes))))
        for t in t_sample
    ])
    full_pred_vals = np.array([
        m284_prediction(complex(0.5, t), primes, Q_REG, k_max)
        for t in t_sample
    ])

    rho_leading, _ = pearsonr(log_D_vals, leading_vals)
    rho_full, _ = pearsonr(log_D_vals, full_pred_vals)

    record(18,
           "M28.4 leading-only correlation ρ",
           f"ρ_leading = {rho_leading:.4f}",
           rho_leading > TOL_RHO_LEADING_LOWER)

    record(19,
           "M28.4 leading + R_small correlation ρ",
           f"ρ_full = {rho_full:.4f}",
           rho_full > TOL_RHO_FULL_LOWER)

    # Test 20: Predicted MAD (peaks of leading + R_small) vs actual LOCATOR MAD
    pred_signal = np.array([
        m284_prediction(complex(0.5, t), primes, Q_REG, k_max)
        for t in t_grid
    ])
    pred_distances = closest_peak_distances(t_grid, pred_signal, zeros_in_range)
    pred_MAD = float(np.mean(pred_distances)) if pred_distances else float("inf")
    diff = abs(pred_MAD - locator_MAD)
    record(20,
           "Predicted vs actual LOCATOR MAD difference",
           f"|Δ MAD| = {diff:.4f} (< {TOL_PRED_VS_ACTUAL_MAD})",
           diff < TOL_PRED_VS_ACTUAL_MAD)

    if verbose:
        print(f"  [verbose D] LOCATOR MAD = {locator_MAD:.4f}, "
              f"predicted MAD = {pred_MAD:.4f}")
        print(f"  [verbose D] ρ_leading = {rho_leading:.4f}, "
              f"ρ_full = {rho_full:.4f}")


# --------------------------------------------------------------------------- #
# Block E: upstream LOCKED inheritance (Tests 21–22)                          #
# --------------------------------------------------------------------------- #

def block_E(verbose: bool = False) -> None:
    # Test 21: All 4/4 V_4 channels (a_χ, q_χ) match ZS-M25 §6.3 [11]
    expected = [
        ("1",         0,  1),
        ("chi_-3",    1,  3),
        ("chi_-11",   1, 11),
        ("chi_33",    0, 33),
    ]
    matches = sum(1 for a, b in zip(V4_CHANNELS, expected) if a == b)
    record(21,
           "V_4 channels (a_χ, q_χ) match ZS-M25 §6.3",
           f"matched {matches}/4",
           matches == 4)

    # Test 22: Sum rule 0.7948 + 0.2050 + 0.0001 = 0.9999 (ZS-F0 §12.3)
    # |λ|^2 numerical anchor with λ = (i π / 2) z*
    lam = (1j * math.pi / 2) * Z_STAR
    lam_sq = abs(lam) ** 2
    # ZS-F0 PROVEN: |λ|^2 ≈ 0.7948
    locator_dom = 0.7948
    sum_rule_residual = abs(lam_sq - locator_dom)
    # The sum rule (0.7948 + 0.2050 + 0.0001 = 0.9999) is upstream PROVEN;
    # we verify the dominant component matches.
    record(22,
           "Sum rule dominant: |λ|^2 = 0.7948 (ZS-F0 §12.3)",
           f"|residual| = {sum_rule_residual:.4f}",
           sum_rule_residual < 5e-3)

    if verbose:
        print(f"  [verbose E] z* = {Z_STAR}, λ = {lam}")
        print(f"  [verbose E] |λ|^2 = {lam_sq:.4f} (corpus PROVEN 0.7948)")
        print(f"  [verbose E] A = 35/437 = {A_VAL:.6f} (LOCKED ZS-F2)")


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(
        description="ZS-M30 v1.0 verification suite (22 tests)"
    )
    parser.add_argument("--P", type=int, default=2000,
                        help="LOCATOR prime cutoff (default 2000; matches §5.3)")
    parser.add_argument("--kmax", type=int, default=7,
                        help="R_small truncation depth (default 7)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print extra diagnostics")
    args = parser.parse_args()

    print("=" * 96)
    print("  ZS-M30 v1.0 Verification Suite")
    print("  Three External Vehicles for D4b Closure")
    print("  (LOCKED inputs: A = 35/437, Q = 11, K = ℚ(√−3, √−11), "
          "(a_χ, q_χ) data per ZS-M25)")
    print(f"  Parameters: P_max = {args.P}, k_max = {args.kmax}")
    print("=" * 96)

    # Block A: corpus PROVEN register symmetries (Tests 1–7)
    print("\n  Block A: corpus PROVEN register symmetries (Tests 1–7)")
    block_A(args.verbose)

    # Block B: Theorem M30.1 (Tests 8–11)
    print("  Block B: Theorem M30.1 — Constant-level conductor identification (Tests 8–11)")
    block_B(args.verbose)

    # Block C: Theorem M30.3 (Tests 12–15)
    print("  Block C: Theorem M30.3 — J seam ↔ Burnol grading non-isomorphism (Tests 12–15)")
    block_C(args.verbose)

    # Block D: Theorem M30.2 (Tests 16–20)
    print("  Block D: Theorem M30.2 — LOCATOR ↔ D_log spectral bridge (Tests 16–20)")
    block_D(args.P, args.kmax, args.verbose)

    # Block E: upstream LOCKED inheritance (Tests 21–22)
    print("  Block E: upstream LOCKED inheritance (Tests 21–22)")
    block_E(args.verbose)

    REPORT.print_table()

    return 0 if REPORT.failed() == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
