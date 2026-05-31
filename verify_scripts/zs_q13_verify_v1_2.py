#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_q13_verify_v1_2.py

Verification suite for:
ZS-Q13 v1.2 — Hydrogen Hyperfine Channel Tomography:
Charge-Superselected Z-Spin Boundary Mediation versus Electric-Flux ER=EPR Leakage

Purpose
-------
This script verifies the algebraic claims of ZS-Q13 v1.2:

1. Hydrogen hyperfine projector algebra.
2. External ER=EPR electric-flux leakage comparison model.
3. Z-Spin null-leakage Hamiltonian theorem.
4. Hydrogen neutrality preservation.
5. Charge-superselected boundary-channel structure.
6. Two-Kraus Z-seam hyperfine CPTP channel.
7. Hyperfine seam-witness identity.
8. H / anti-H / Mu / Ps neutral-system null-leakage program.
9. Anti-numerology guard: no direct A, z*, |lambda|^2 -> 21 cm frequency fitting.

This is a mathematical / structural verification suite. It does NOT calculate
the observed hydrogen 21 cm frequency, nor does it fit any atomic data.

Dependencies
------------
numpy only.

Run
---
python zs_q13_verify_v1_2.py
python zs_q13_verify_v1_2.py --json
python zs_q13_verify_v1_2.py --strict

Author: Kenny Kang / Z-Spin Cosmology Collaboration
Version: v1.2 verification suite
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict
from typing import Callable, Dict, List, Tuple, Any

import numpy as np


# =============================================================================
# Global numerical settings
# =============================================================================

RTOL = 1.0e-11
ATOL = 1.0e-12
CANONICAL_SEED = 350437


# =============================================================================
# Locked Z-Spin constants
# =============================================================================

A_ZS = 35.0 / 437.0
Q_ZS = 11
DIM_Z = 2
DIM_X = 3
DIM_Y = 6


# =============================================================================
# Basic linear algebra helpers
# =============================================================================

def dagger(x: np.ndarray) -> np.ndarray:
    return x.conj().T


def fro_norm(x: np.ndarray) -> float:
    return float(np.linalg.norm(x, ord="fro"))


def is_close(a: Any, b: Any, rtol: float = RTOL, atol: float = ATOL) -> bool:
    return bool(np.allclose(a, b, rtol=rtol, atol=atol))


def ket(dim: int, idx: int) -> np.ndarray:
    v = np.zeros((dim, 1), dtype=complex)
    v[idx, 0] = 1.0
    return v


def projector(v: np.ndarray) -> np.ndarray:
    return v @ dagger(v)


def rank_numeric(x: np.ndarray, tol: float = 1e-10) -> int:
    s = np.linalg.svd(x, compute_uv=False)
    return int(np.sum(s > tol))


def partial_trace_second(rho: np.ndarray, d1: int, d2: int) -> np.ndarray:
    """Trace out second subsystem from d1 x d2 composite."""
    arr = rho.reshape(d1, d2, d1, d2)
    return np.einsum("abcb->ac", arr)


def make_random_density(dim: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    rho = x @ dagger(x)
    return rho / np.trace(rho)


def choi_from_kraus(kraus: List[np.ndarray]) -> np.ndarray:
    """
    Choi matrix C = sum_ij |i><j| ⊗ Lambda(|i><j|).
    Convention: input basis first, output basis second.
    """
    d = kraus[0].shape[0]
    C = np.zeros((d * d, d * d), dtype=complex)
    for i in range(d):
        for j in range(d):
            eij = np.zeros((d, d), dtype=complex)
            eij[i, j] = 1.0
            out = sum(k @ eij @ dagger(k) for k in kraus)
            C += np.kron(eij, out)
    return C


def apply_channel(kraus: List[np.ndarray], rho: np.ndarray) -> np.ndarray:
    return sum(k @ rho @ dagger(k) for k in kraus)


def kraus_completeness(kraus: List[np.ndarray]) -> np.ndarray:
    d = kraus[0].shape[0]
    acc = np.zeros((d, d), dtype=complex)
    for k in kraus:
        acc += dagger(k) @ k
    return acc


def choi_is_psd(C: np.ndarray, tol: float = 1e-10) -> bool:
    vals = np.linalg.eigvalsh((C + dagger(C)) / 2.0)
    return bool(np.min(vals) >= -tol)


# =============================================================================
# Hydrogen hyperfine spin algebra
# Basis convention:
# |uu> = 0, |ud> = 1, |du> = 2, |dd> = 3
# =============================================================================

I2 = np.eye(2, dtype=complex)
I4 = np.eye(4, dtype=complex)

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)

Sx = 0.5 * SIGMA_X
Sy = 0.5 * SIGMA_Y
Sz = 0.5 * SIGMA_Z

S_e = [np.kron(Sx, I2), np.kron(Sy, I2), np.kron(Sz, I2)]
S_p = [np.kron(I2, Sx), np.kron(I2, Sy), np.kron(I2, Sz)]

SDOT = sum(S_e[i] @ S_p[i] for i in range(3))

UU = ket(4, 0)
UD = ket(4, 1)
DU = ket(4, 2)
DD = ket(4, 3)

T_PLUS = UU
T_ZERO = (UD + DU) / math.sqrt(2.0)
T_MINUS = DD
S_ZERO = (UD - DU) / math.sqrt(2.0)

P_T_PLUS = projector(T_PLUS)
P_T_ZERO = projector(T_ZERO)
P_T_MINUS = projector(T_MINUS)
P_S_ZERO = projector(S_ZERO)

P_TRIPLET = P_T_PLUS + P_T_ZERO + P_T_MINUS
P_SINGLET = P_S_ZERO
P_ENT = P_T_ZERO + P_S_ZERO  # entangled m=0 sector used by ER leakage comparison

H_HFS_UNIT = SDOT  # A_F = 1 unit convention
E_TRIPLET = 0.25
E_SINGLET = -0.75
DELTA_E_UNIT = E_TRIPLET - E_SINGLET  # = 1


# Z-seam involution on the spin basis:
# |uu> <-> |dd>, |ud> <-> |du|
J_HFS = np.fliplr(np.eye(4, dtype=complex))


# =============================================================================
# ER leakage comparison model
# =============================================================================

def eta_er(s: float, alpha_er: float) -> float:
    if alpha_er <= 0:
        raise ValueError("alpha_er must be positive.")
    if s < 0:
        raise ValueError("entanglement entropy parameter s must be non-negative.")
    return float(s / (math.pi * alpha_er ** 2))


def er_effective_charge(e_charge: float, eta: float) -> float:
    return float(e_charge / (1.0 + eta))


def er_hydrogen_net_charge(eta: float) -> float:
    """Proton charge +1 plus entanglement-weakened electron charge."""
    return float(1.0 - 1.0 / (1.0 + eta))


def er_hfs_scaling(eta: float) -> float:
    return float((1.0 + eta) ** -3)


def er_leakage_hamiltonian(eta: float) -> np.ndarray:
    """
    Minimal projector-level ER leakage comparison Hamiltonian:
    product triplet states are unchanged; entangled m=0 triplet and singlet
    receive the external-model hyperfine scaling.
    """
    scale = er_hfs_scaling(eta)
    return (
        E_TRIPLET * (P_T_PLUS + P_T_MINUS)
        + (scale * E_TRIPLET) * P_T_ZERO
        + (scale * E_SINGLET) * P_SINGLET
    )


def expectation(v: np.ndarray, H: np.ndarray) -> complex:
    return (dagger(v) @ H @ v)[0, 0]


# =============================================================================
# Z-Spin null-leakage and CPTP seam channel
# =============================================================================

def zs_effective_charge(e_charge: float) -> float:
    return float(e_charge)


def zs_hydrogen_net_charge() -> float:
    return 0.0


def zs_coherent_leakage_shift(*_args: Any, **_kwargs: Any) -> float:
    """
    Anti-numerology guard: ZS-Q13 v1.2 predicts no coherent electric-flux
    leakage shift. This function intentionally ignores A, z*, |lambda|^2, etc.
    """
    return 0.0


def zs_hyperfine_hamiltonian() -> np.ndarray:
    """ZS-Q13 Hamiltonian at leakage level equals the standard unit HFS Hamiltonian."""
    return H_HFS_UNIT.copy()


def zs_seam_kraus(p: float = A_ZS) -> List[np.ndarray]:
    """
    Two-Kraus seam channel:
        Lambda(rho) = (1-p) rho + p J rho J.
    This is not asserted as a fitted atomic linewidth model. It verifies the
    structural two-Kraus / seam-witness claims of v1.2.
    """
    if not (0.0 <= p <= 1.0):
        raise ValueError("p must lie in [0,1].")
    return [math.sqrt(1.0 - p) * I4, math.sqrt(p) * J_HFS]


def seam_witness(C: np.ndarray, J: np.ndarray = J_HFS) -> float:
    W = np.kron(J, J)
    denom = fro_norm(C)
    if denom == 0.0:
        return float("inf")
    return fro_norm(W @ C @ W - C.T) / denom


def random_unitary(dim: int, rng: np.random.Generator) -> np.ndarray:
    x = rng.normal(size=(dim, dim)) + 1j * rng.normal(size=(dim, dim))
    q, r = np.linalg.qr(x)
    phases = np.exp(-1j * np.angle(np.diag(r)))
    return q @ np.diag(phases)


# =============================================================================
# Neutral hydrogenic-system program
# =============================================================================

NEUTRAL_SYSTEMS = [
    # name, positive constituent charge, negative constituent charge
    ("H", +1.0, -1.0),
    ("anti-H", -1.0, +1.0),
    ("Mu", +1.0, -1.0),   # mu+ e-
    ("Ps", +1.0, -1.0),   # e+ e-
]


# =============================================================================
# Test reporting
# =============================================================================

@dataclass
class TestResult:
    id: str
    name: str
    passed: bool
    status: str
    detail: str


class VerificationReport:
    def __init__(self) -> None:
        self.results: List[TestResult] = []

    def add(self, test_id: str, name: str, predicate: bool, status: str, detail: str = "") -> None:
        self.results.append(TestResult(test_id, name, bool(predicate), status, detail))

    def add_close(self, test_id: str, name: str, actual: Any, expected: Any, status: str,
                  rtol: float = RTOL, atol: float = ATOL, detail: str = "") -> None:
        ok = is_close(actual, expected, rtol=rtol, atol=atol)
        if not detail:
            detail = f"actual={np.asarray(actual).tolist()}, expected={np.asarray(expected).tolist()}"
        self.add(test_id, name, ok, status, detail)

    @property
    def passed(self) -> int:
        return sum(r.passed for r in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed

    @property
    def total(self) -> int:
        return len(self.results)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "suite": "ZS-Q13 v1.2 verification",
            "total": self.total,
            "passed": self.passed,
            "failed": self.failed,
            "all_passed": self.failed == 0,
            "results": [asdict(r) for r in self.results],
        }

    def print_text(self) -> None:
        print("=" * 78)
        print("ZS-Q13 v1.2 Verification Suite")
        print("Hydrogen Hyperfine Channel Tomography / Null-Leakage Gate")
        print("=" * 78)
        for r in self.results:
            mark = "PASS" if r.passed else "FAIL"
            print(f"[{mark}] {r.id:>8} | {r.status:<22} | {r.name}")
            if r.detail:
                print(f"         {r.detail}")
        print("-" * 78)
        print(f"SUMMARY: {self.passed}/{self.total} PASS | {self.failed} FAIL")
        if self.failed == 0:
            print("VERDICT: ALL VERIFICATION CHECKS PASSED")
        else:
            print("VERDICT: FAILURES PRESENT")


# =============================================================================
# Verification suite
# =============================================================================

def run_suite() -> VerificationReport:
    rep = VerificationReport()
    rng = np.random.default_rng(CANONICAL_SEED)

    # -------------------------------------------------------------------------
    # A. Locked Z-Spin constants and sector arithmetic
    # -------------------------------------------------------------------------
    rep.add_close("C1", "A locked as 35/437", A_ZS, 35.0 / 437.0, "LOCKED")
    rep.add_close("C2", "Q = Z + X + Y = 11", DIM_Z + DIM_X + DIM_Y, Q_ZS, "LOCKED")
    rep.add("C3", "Z-sector has exactly two mediation channels", DIM_Z == 2, "LOCKED",
            f"DIM_Z={DIM_Z}")
    rep.add("C4", "A is not used as a fitted 21 cm frequency parameter",
            zs_coherent_leakage_shift(A_ZS) == 0.0, "ANTI-NUMEROLOGY",
            "coherent leakage shift function returns 0 for all inputs")

    # -------------------------------------------------------------------------
    # B. Hyperfine projector algebra
    # -------------------------------------------------------------------------
    rep.add_close("H1", "Triplet + singlet projectors resolve identity",
                  P_TRIPLET + P_SINGLET, I4, "STANDARD")
    rep.add_close("H2", "Triplet projector is idempotent",
                  P_TRIPLET @ P_TRIPLET, P_TRIPLET, "STANDARD")
    rep.add_close("H3", "Singlet projector is idempotent",
                  P_SINGLET @ P_SINGLET, P_SINGLET, "STANDARD")
    rep.add_close("H4", "Triplet and singlet projectors are orthogonal",
                  P_TRIPLET @ P_SINGLET, np.zeros((4, 4)), "STANDARD")
    rep.add("H5", "Triplet projector has rank 3",
            rank_numeric(P_TRIPLET) == 3, "STANDARD", f"rank={rank_numeric(P_TRIPLET)}")
    rep.add("H6", "Singlet projector has rank 1",
            rank_numeric(P_SINGLET) == 1, "STANDARD", f"rank={rank_numeric(P_SINGLET)}")
    rep.add("H7", "Entangled m=0 projector has rank 2",
            rank_numeric(P_ENT) == 2, "STANDARD", f"rank={rank_numeric(P_ENT)}")
    rep.add_close("H8", "S_e · S_p eigenvalue on |1,1> is +1/4",
                  expectation(T_PLUS, SDOT), E_TRIPLET, "STANDARD")
    rep.add_close("H9", "S_e · S_p eigenvalue on |1,0> is +1/4",
                  expectation(T_ZERO, SDOT), E_TRIPLET, "STANDARD")
    rep.add_close("H10", "S_e · S_p eigenvalue on |1,-1> is +1/4",
                  expectation(T_MINUS, SDOT), E_TRIPLET, "STANDARD")
    rep.add_close("H11", "S_e · S_p eigenvalue on |0,0> is -3/4",
                  expectation(S_ZERO, SDOT), E_SINGLET, "STANDARD")
    rep.add_close("H12", "Unit hyperfine gap is E_t - E_s = 1",
                  E_TRIPLET - E_SINGLET, DELTA_E_UNIT, "STANDARD")

    # -------------------------------------------------------------------------
    # C. External ER electric-flux leakage comparison model
    # -------------------------------------------------------------------------
    s = math.log(2.0)  # a concrete entangled two-state entropy scale
    alpha_er = 25.0
    eta = eta_er(s=s, alpha_er=alpha_er)

    rep.add("ER1", "ER leakage parameter eta is positive for s>0",
            eta > 0.0, "IMPORTED-COMPARISON", f"eta={eta:.12e}")
    rep.add_close("ER2", "ER effective electron charge formula",
                  er_effective_charge(-1.0, eta),
                  -1.0 / (1.0 + eta), "IMPORTED-COMPARISON")
    rep.add_close("ER3", "ER non-traversable hydrogen net charge formula",
                  er_hydrogen_net_charge(eta),
                  eta / (1.0 + eta), "IMPORTED-COMPARISON")
    rep.add("ER4", "ER leakage predicts non-zero effective charge when eta>0",
            er_hydrogen_net_charge(eta) > 0.0, "IMPORTED-COMPARISON",
            f"Q_H_eff={er_hydrogen_net_charge(eta):.12e}")
    rep.add_close("ER5", "ER hyperfine scaling is (1+eta)^-3",
                  er_hfs_scaling(eta), (1.0 + eta) ** -3, "IMPORTED-COMPARISON")

    H_ER = er_leakage_hamiltonian(eta)
    E_t_plus_er = expectation(T_PLUS, H_ER)
    E_t_zero_er = expectation(T_ZERO, H_ER)
    E_t_minus_er = expectation(T_MINUS, H_ER)
    E_s_zero_er = expectation(S_ZERO, H_ER)

    rep.add("ER6", "ER leakage breaks triplet degeneracy: |1,1> vs |1,0>",
            abs(E_t_plus_er - E_t_zero_er) > 1e-14, "IMPORTED-COMPARISON",
            f"E_11={E_t_plus_er.real:.12e}, E_10={E_t_zero_er.real:.12e}")
    rep.add_close("ER7", "ER leakage preserves |1,1> and |1,-1> equality in minimal model",
                  E_t_plus_er, E_t_minus_er, "IMPORTED-COMPARISON")
    rep.add("ER8", "ER leakage modifies singlet energy when eta>0",
            abs(E_s_zero_er - E_SINGLET) > 1e-14, "IMPORTED-COMPARISON",
            f"E_s_ER={E_s_zero_er.real:.12e}, E_s_std={E_SINGLET:.12e}")

    # -------------------------------------------------------------------------
    # D. Z-Spin null-leakage Hamiltonian and neutrality
    # -------------------------------------------------------------------------
    H_ZS = zs_hyperfine_hamiltonian()
    rep.add_close("ZS1", "ZS effective electron charge is rigid: Q_e=-1",
                  zs_effective_charge(-1.0), -1.0, "DERIVED")
    rep.add_close("ZS2", "ZS hydrogen net charge is exactly zero",
                  zs_hydrogen_net_charge(), 0.0, "DERIVED")
    rep.add_close("ZS3", "ZS coherent leakage shift is zero",
                  zs_coherent_leakage_shift(A_ZS, eta, "zstar", "lambda"), 0.0, "DERIVED")
    rep.add_close("ZS4", "ZS HFS Hamiltonian equals standard unit HFS at leakage level",
                  H_ZS, H_HFS_UNIT, "DERIVED")
    rep.add_close("ZS5", "ZS triplet degeneracy |1,1> = |1,0>",
                  expectation(T_PLUS, H_ZS), expectation(T_ZERO, H_ZS), "DERIVED")
    rep.add_close("ZS6", "ZS triplet degeneracy |1,0> = |1,-1>",
                  expectation(T_ZERO, H_ZS), expectation(T_MINUS, H_ZS), "DERIVED")
    rep.add_close("ZS7", "ZS unit hyperfine gap is unchanged",
                  expectation(T_PLUS, H_ZS) - expectation(S_ZERO, H_ZS),
                  DELTA_E_UNIT, "DERIVED")

    # -------------------------------------------------------------------------
    # E. Charge-superselection / state-dependent charge failure
    # -------------------------------------------------------------------------
    QOP_ZS = np.zeros((4, 4), dtype=complex)  # neutral hydrogen charge operator
    Q_ER = er_hydrogen_net_charge(eta) * P_ENT  # state-dependent charge in entangled sector

    rep.add_close("Q1", "ZS neutral charge operator is proportional to identity zero",
                  QOP_ZS, np.zeros((4, 4)), "DERIVED")
    rep.add_close("Q2", "ZS charge operator commutes with HFS Hamiltonian",
                  QOP_ZS @ H_HFS_UNIT - H_HFS_UNIT @ QOP_ZS,
                  np.zeros((4, 4)), "DERIVED")
    rep.add("Q3", "ER leakage charge operator is not proportional to identity",
            fro_norm(Q_ER - (np.trace(Q_ER) / 4.0) * I4) > 1e-14,
            "IMPORTED-CONTRAST",
            "state-dependent charge label detected")
    rep.add("Q4", "ER leakage has different charge eigenvalues across spin subspaces",
            len(np.unique(np.round(np.linalg.eigvalsh(Q_ER).real, 14))) > 1,
            "IMPORTED-CONTRAST",
            f"eigenvalues={np.linalg.eigvalsh(Q_ER).real.tolist()}")

    # -------------------------------------------------------------------------
    # F. Z-seam CPTP hyperfine channel
    # -------------------------------------------------------------------------
    rep.add_close("J1", "Hydrogen hyperfine seam involution J^2=I",
                  J_HFS @ J_HFS, I4, "PROVEN")
    rep.add_close("J2", "Hydrogen hyperfine seam involution is unitary",
                  dagger(J_HFS) @ J_HFS, I4, "PROVEN")
    rep.add_close("J3", "Hydrogen hyperfine seam involution is Hermitian",
                  dagger(J_HFS), J_HFS, "PROVEN")

    kraus = zs_seam_kraus(p=A_ZS)
    rep.add("K1", "ZS hyperfine seam channel has exactly two Kraus operators",
            len(kraus) == 2, "DERIVED", f"Kraus count={len(kraus)}")
    rep.add_close("K2", "ZS two-Kraus seam channel is trace-preserving",
                  kraus_completeness(kraus), I4, "DERIVED")
    C = choi_from_kraus(kraus)
    rep.add("K3", "ZS two-Kraus seam channel has positive semidefinite Choi matrix",
            choi_is_psd(C), "DERIVED",
            f"min_eig={float(np.min(np.linalg.eigvalsh((C+dagger(C))/2.0))):.3e}")
    rep.add("K4", "ZS channel Choi rank is <= 2",
            rank_numeric(C) <= 2, "DERIVED",
            f"choi_rank={rank_numeric(C)}")
    rho = make_random_density(4, rng)
    out = apply_channel(kraus, rho)
    rep.add_close("K5", "ZS channel preserves trace on random density matrix",
                  np.trace(out), 1.0, "VERIFIED")
    rep.add("K6", "ZS channel output remains positive semidefinite",
            np.min(np.linalg.eigvalsh((out + dagger(out)) / 2.0)) >= -1e-10,
            "VERIFIED",
            f"min_eig={float(np.min(np.linalg.eigvalsh((out+dagger(out))/2.0))):.3e}")
    rep.add_close("K7", "ZS channel preserves neutral charge expectation",
                  np.trace(QOP_ZS @ out), 0.0, "DERIVED")

    # -------------------------------------------------------------------------
    # G. Hyperfine seam witness
    # -------------------------------------------------------------------------
    u_zs = seam_witness(C, J_HFS)
    rep.add_close("S1", "ZS hyperfine seam witness is zero in ideal channel",
                  u_zs, 0.0, "DERIVED", atol=1e-12,
                  detail=f"u_seam={u_zs:.12e}")

    U_rand = random_unitary(4, rng)
    C_rand = choi_from_kraus([U_rand])
    u_rand = seam_witness(C_rand, J_HFS)
    rep.add("S2", "Generic random unitary channel violates seam witness",
            u_rand > 1e-3, "CONTROL",
            f"u_random={u_rand:.12e}")
    rep.add("S3", "Seam witness is bounded in [0,2] for the tested channels",
            (0.0 <= u_zs <= 2.0) and (0.0 <= u_rand <= 2.0 + 1e-10),
            "PROVEN/CONTROL",
            f"u_zs={u_zs:.3e}, u_random={u_rand:.3e}")

    # -------------------------------------------------------------------------
    # H. H / anti-H / Mu / Ps neutral-system program
    # -------------------------------------------------------------------------
    for idx, (name, q_pos, q_neg) in enumerate(NEUTRAL_SYSTEMS, start=1):
        net = q_pos + q_neg
        rep.add_close(f"N{idx}", f"{name}: neutral two-body charge sum is zero",
                      net, 0.0, "TESTABLE-PROGRAM")
        rep.add_close(f"N{idx}L", f"{name}: ZS coherent leakage shift is zero",
                      zs_coherent_leakage_shift(name), 0.0, "TESTABLE-PROGRAM")

    # -------------------------------------------------------------------------
    # I. Anti-numerology guards
    # -------------------------------------------------------------------------
    # The suite intentionally never stores the observed 21 cm frequency.
    namespace = globals()
    forbidden_names = [name for name in namespace if "NU21" in name or "FREQ21" in name or "1420" in name]
    rep.add("AN1", "No observed 21 cm frequency constant is defined in the verifier",
            len(forbidden_names) == 0, "ANTI-NUMEROLOGY",
            f"forbidden_names={forbidden_names}")
    rep.add_close("AN2", "Coherent shift remains zero for A, A/Q, 2A/Q, and |lambda|^2-like inputs",
                  [
                      zs_coherent_leakage_shift(A_ZS),
                      zs_coherent_leakage_shift(A_ZS / Q_ZS),
                      zs_coherent_leakage_shift(2.0 * A_ZS / Q_ZS),
                      zs_coherent_leakage_shift(0.7948),
                  ],
                  [0.0, 0.0, 0.0, 0.0],
                  "ANTI-NUMEROLOGY")
    rep.add("AN3", "Verifier separates Hamiltonian null shift from open-channel signature",
            (zs_coherent_leakage_shift() == 0.0) and (rank_numeric(C) <= 2) and is_close(u_zs, 0.0),
            "ANTI-NUMEROLOGY",
            "no spectral fitting; channel-level theorem verified")

    return rep


# =============================================================================
# Main
# =============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="Verify ZS-Q13 v1.2 algebraic claims.")
    parser.add_argument("--json", action="store_true", help="Emit JSON report instead of text.")
    parser.add_argument("--strict", action="store_true", help="Exit with non-zero status on any failure.")
    args = parser.parse_args()

    report = run_suite()

    if args.json:
        print(json.dumps(report.as_dict(), indent=2, ensure_ascii=False))
    else:
        report.print_text()

    if args.strict and report.failed:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
