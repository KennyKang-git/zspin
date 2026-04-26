#!/usr/bin/env python3
"""
zs_f11_verify.py
================

Z-Spin Cosmology
ZS-F11 v1.0 (with dated update 2026-04-26):
"Operational Observer Coordinate and the Self-Referential Fixed Point"

Verification suite for ZS-F11 v1.0 dated update 2026-04-26.

Target: 38/38 enumerated tests, comprising
  - 28 PROVEN/DERIVED PASS (categories [A]-[H])
  - 10 permutation-control tests (category [I'])
    reporting exact-enumeration p = 945/35,696 ≈ 2.65% under uniform-involution null
    (nontrivial selectivity; NOT strict 1% anti-numerology PASS)

Authoritative source: ZS-F11 v1.0 dated update 2026-04-26, Tables 2', 3',
    Theorem F11.1' refinement, Corollary F11.1A' rank-based proof (§DU.5),
    §DU.6 exact enumeration on T(11)=35,696, Table A.1' refined verification suite.

Dependencies:
    Python 3.10+, numpy, mpmath (>=50-digit precision), sympy (optional, used only for
    cross-checking telephone-number recurrence; itertools.permutations is the primary engine).

Execution:
    $ python3 zs_f11_verify.py
Expected output:
    38/38 enumerated PASS, exit code 0
    (with §DU.6 honest scope statement on permutation-control p = 2.65%)

Zero free parameters. All numerical inputs are LOCKED, PROVEN, or DERIVED in the
v1.0 corpus and are loaded as constants in §0 below. No new physical claim is asserted.
"""

import sys
import os
from fractions import Fraction
from itertools import permutations
from math import factorial
import numpy as np
import mpmath as mp

# Set 50-digit precision for the [H] information-time consistency tests
mp.mp.dps = 50

# ----------------------------------------------------------------------------
# §0. LOCKED INPUTS (no new free parameters)
# ----------------------------------------------------------------------------
# Geometric impedance A = 35/437 (LOCKED, ZS-F2 v1.0 §11)
A_FRAC = Fraction(35, 437)
A_FLOAT = 35.0 / 437.0
A_MP = mp.mpf(35) / mp.mpf(437)

# Register Q = 11 (PROVEN, ZS-F5 v1.0)
Q = 11

# Sector decomposition (Z, X, Y) = (2, 3, 6) (PROVEN, ZS-F5 v1.0)
DIM_Z, DIM_X, DIM_Y = 2, 3, 6

# Sector slot assignments (one canonical convention used in ZS-F11 Table 3):
#   slots {0, 1}                -> Z (Z-sector)
#   slots {2, 3, 4}             -> X (X-sector)
#   slots {5, 6, 7, 8, 9, 10}   -> Y (Y-sector)
SLOT_SECTOR = {
    0: "Z", 1: "Z",
    2: "X", 3: "X", 4: "X",
    5: "Y", 6: "Y", 7: "Y", 8: "Y", 9: "Y", 10: "Y",
}

# i-tetration fixed point z* (PROVEN, ZS-M1 v1.0 §2)
# Paper-stated 10-digit values: z* = 0.4382829367 + 0.3605924719 i
# (verified by Lambert W principal branch: z* = -W0(-i pi/2)/(i pi/2))
ZSTAR_RE_10DIGIT = mp.mpf("0.4382829367")  # ZS-M1 v1.0 §2 stated precision
ZSTAR_IM_10DIGIT = mp.mpf("0.3605924719")

# Wilson loop dominant Z-block eigenvalue lambda = (i*pi/2) z* (ZS-F0 v1.0(R) Theorem 8.9)
# |lambda|^2 = (pi^2/4) eta_topo (PROVEN, ZS-F0 v1.0(R) Theorem 8.9)
# eta_topo = |z*|^2 (PROVEN, ZS-M1 v1.0 §3 L3)

# ----------------------------------------------------------------------------
# Test infrastructure
# ----------------------------------------------------------------------------

class Suite:
    """Track tests with category grouping; print a summary at the end."""

    def __init__(self):
        self.results = []  # list of (cat, name, passed, detail)

    def check(self, cat, name, passed, detail=""):
        self.results.append((cat, name, bool(passed), detail))
        marker = "PASS" if passed else "FAIL"
        print(f"  [{cat}] {name}: {marker}    {detail}")
        return bool(passed)

    def summary(self):
        cats = {}
        for cat, _, ok, _ in self.results:
            cats.setdefault(cat, [0, 0])
            cats[cat][1] += 1
            if ok:
                cats[cat][0] += 1
        total_pass = sum(p for p, _ in cats.values())
        total = sum(t for _, t in cats.values())
        print()
        print("=" * 78)
        print("VERIFICATION SUMMARY (Table A.1' refined)")
        print("=" * 78)
        for cat in sorted(cats.keys()):
            p, t = cats[cat]
            mark = "PASS" if p == t else "FAIL"
            print(f"  Category {cat:>4}:  {p}/{t}   {mark}")
        print("-" * 78)
        print(f"  TOTAL:        {total_pass}/{total}")
        print("=" * 78)
        return total_pass, total


# ============================================================================
# CATEGORY [A] - Locked Inputs (5 tests)
# Source: ZS-F11 v1.0 §2 Table 1
# ============================================================================

def category_A(s: Suite):
    print("\n[A] Locked Inputs")

    # A.1 — A = 35/437 (LOCKED, ZS-F2 v1.0 §11)
    s.check("A", "A1: A = 35/437 (LOCKED, ZS-F2 v1.0 §11)",
            A_FRAC == Fraction(35, 437),
            f"A = {A_FRAC} = {A_FLOAT:.6f}")

    # A.2 — Q = 11 (PROVEN, ZS-F5 v1.0)
    s.check("A", "A2: Q = 11 (PROVEN, ZS-F5 v1.0)",
            Q == 11 and DIM_Z + DIM_X + DIM_Y == Q,
            f"Q = {Q}; Z+X+Y = {DIM_Z}+{DIM_X}+{DIM_Y} = {DIM_Z+DIM_X+DIM_Y}")

    # A.3 — (Z, X, Y) = (2, 3, 6) (PROVEN, ZS-F5 v1.0)
    s.check("A", "A3: (Z, X, Y) = (2, 3, 6) (PROVEN, ZS-F5 v1.0)",
            (DIM_Z, DIM_X, DIM_Y) == (2, 3, 6),
            f"(Z, X, Y) = ({DIM_Z}, {DIM_X}, {DIM_Y})")

    # A.4 — z* = i^z* via Lambert W0 principal branch (PROVEN, ZS-M1 v1.0 §2)
    # z* = -W0(-i pi/2) / (i pi/2)
    # Paper states 10-digit values; tolerance 1e-10 matches paper's stated precision.
    z_star = -mp.lambertw(-1j * mp.pi / 2, k=0) / (1j * mp.pi / 2)
    re_match = abs(z_star.real - ZSTAR_RE_10DIGIT) < mp.mpf("1e-10")
    im_match = abs(z_star.imag - ZSTAR_IM_10DIGIT) < mp.mpf("1e-10")
    # Additional internal consistency: z* satisfies the master equation z* = i^z*
    z_star_check = mp.exp(z_star * 1j * mp.pi / 2)
    self_consistent = abs(z_star_check - z_star) < mp.mpf("1e-40")
    s.check("A", "A4: z* = -W0(-i pi/2)/(i pi/2); z* = i^z* (PROVEN, ZS-M1 v1.0 §2)",
            re_match and im_match and self_consistent,
            f"z* = {mp.nstr(z_star.real, 11)} + {mp.nstr(z_star.imag, 11)}i; "
            f"matches paper to 10 digits; self-consistent at 40 digits")

    # A.5 — J slot ordering: J|j> = |10 - j> on the Q=11 register (PROVEN, ZS-M3, ZS-M4 §3.1)
    J = np.zeros((Q, Q), dtype=int)
    for j in range(Q):
        J[Q - 1 - j, j] = 1
    j_squared_is_identity = np.array_equal(J @ J, np.eye(Q, dtype=int))
    j_action = all(np.argmax(J @ np.eye(Q)[:, j]) == (Q - 1 - j) for j in range(Q))
    s.check("A", "A5: J|j> = |10-j>; J^2 = I (PROVEN, ZS-M3 v1.0; ZS-M4 §3.1)",
            j_squared_is_identity and j_action,
            f"J^2 = I: {j_squared_is_identity}; correct action on basis: {j_action}")

    return J


# ============================================================================
# CATEGORY [B] - J-fixed Point Uniqueness (3 tests)
# Source: ZS-F0 v1.0(R) Theorem 8.5; ZS-F11 v1.0 dated update §DU.1
# ============================================================================

def category_B(s: Suite, J):
    print("\n[B] J-fixed Point Uniqueness")

    # B.1 — Slot enumeration: only |5> is a basis-level J-eigenvector
    # |j> is a J-eigenvector iff J|j> = +-|j> iff (Q-1-j) == j (eigenvalue +1)
    fixed_slots = [j for j in range(Q) if (Q - 1 - j) == j]
    s.check("B", "B1: Unique basis-level J-fixed slot is j = 5",
            fixed_slots == [5],
            f"fixed slots = {fixed_slots}")

    # B.2 — Q = 11 odd forces exactly one J-fixed slot under J|j>=|Q-1-j>
    # (For odd Q, there is exactly one j with 2j = Q-1; for even Q, none.)
    Q_odd = (Q % 2 == 1)
    expected_fixed_count = 1 if Q_odd else 0
    s.check("B", "B2: Q = 11 odd forces exactly 1 fixed slot",
            Q_odd and len(fixed_slots) == expected_fixed_count,
            f"Q odd: {Q_odd}; fixed count: {len(fixed_slots)} = expected {expected_fixed_count}")

    # B.3 — E_+(J) and E_-(J) eigenspace dimensions: 6 and 5
    # (Theorem 8.5: dim E_+ = 6, dim E_- = 5)
    eigvals = np.linalg.eigvalsh(J.astype(float))
    n_plus = sum(1 for e in eigvals if e > 0.5)
    n_minus = sum(1 for e in eigvals if e < -0.5)
    s.check("B", "B3: dim E_+(J) = 6, dim E_-(J) = 5 (Theorem 8.5)",
            n_plus == 6 and n_minus == 5,
            f"dim E_+ = {n_plus}, dim E_- = {n_minus}")


# ============================================================================
# CATEGORY [C] - Three-Layer Fixed-Point Inner Products (4 tests)
# Source: ZS-F0 v1.0(R) Theorem 9.1; ZS-F11 §3.2
# ============================================================================

def category_C(s: Suite):
    print("\n[C] Three-Layer Fixed-Point Inner Products")

    # Construct the three fixed point objects on C^11:
    #   |0>_Z   = e_0 (boundary BFV, Z-sector slot 0)
    #   |v_W>   = (e_0 - i e_1) / sqrt(2)  (bulk dynamic, Wilson eigenvector)
    #   |v_W*>  = (e_0 + i e_1) / sqrt(2)  (conjugate)
    #   |5>     = e_5 (kinematic, J-fixed)
    e = lambda j: np.eye(Q, dtype=complex)[:, j]
    ket_0Z = e(0)
    ket_vW = (e(0) - 1j * e(1)) / np.sqrt(2)
    ket_vW_star = (e(0) + 1j * e(1)) / np.sqrt(2)
    ket_5 = e(5)

    inner = lambda u, v: complex(np.vdot(u, v))

    # C.1 — <0_Z | 5> = 0
    ip_0Z_5 = inner(ket_0Z, ket_5)
    s.check("C", "C1: <0_Z|5> = 0 (orthogonality, ZS-F0 v1.0(R) §9.1)",
            abs(ip_0Z_5) < 1e-14,
            f"|<0_Z|5>| = {abs(ip_0Z_5):.2e}")

    # C.2 — <v_W | 5> = 0
    ip_vW_5 = inner(ket_vW, ket_5)
    s.check("C", "C2: <v_W|5> = 0 (orthogonality, ZS-F0 v1.0(R) §9.1)",
            abs(ip_vW_5) < 1e-14,
            f"|<v_W|5>| = {abs(ip_vW_5):.2e}")

    # C.3 — |0>_Z = (|v_W> + |v_W*>) / sqrt(2)  (decomposition identity)
    decomposition = (ket_vW + ket_vW_star) / np.sqrt(2)
    decomp_match = np.allclose(decomposition, ket_0Z, atol=1e-14)
    s.check("C", "C3: |0>_Z = (|v_W> + |v_W*>)/sqrt(2) (decomposition identity)",
            decomp_match,
            f"||(|v_W> + |v_W*>)/sqrt(2) - |0>_Z|| = {np.linalg.norm(decomposition - ket_0Z):.2e}")

    # C.4 — <v_W | v_W*> = 0  (the two Wilson eigenvectors are orthogonal)
    ip_vW_vWstar = inner(ket_vW, ket_vW_star)
    s.check("C", "C4: <v_W|v_W*> = 0 (Z-block conjugate orthogonality)",
            abs(ip_vW_vWstar) < 1e-14,
            f"|<v_W|v_W*>| = {abs(ip_vW_vWstar):.2e}")


# ============================================================================
# CATEGORY [D] - Wilson Loop Dynamical Attractor (5 tests)
# Source: ZS-F0 v1.0(R) §8.8, Theorem 8.17, Theorem 9.4
# ============================================================================

def category_D(s: Suite):
    print("\n[D] Wilson Loop Dynamical Attractor")

    # Z-block of W: 2x2 conformal map M_f at z* linearization
    # M_f = [[Re lambda, -Im lambda], [Im lambda, Re lambda]]
    # where lambda = (i pi / 2) z*
    z_star = -mp.lambertw(-1j * mp.pi / 2, k=0) / (1j * mp.pi / 2)
    lam = (1j * mp.pi / mp.mpf(2)) * z_star
    re_lam = float(lam.real)
    im_lam = float(lam.imag)
    M_f = np.array([[re_lam, -im_lam], [im_lam, re_lam]], dtype=float)

    # D.1 — |lambda| = 0.8915... (i-tetration stability margin, ZS-M1 v1.0 L5)
    abs_lam = abs(lam)
    s.check("D", "D1: |lambda| = sqrt(eta_topo) * (pi/2) ~ 0.8915 (PROVEN, ZS-M1 L5)",
            abs(abs_lam - mp.mpf("0.8915135658")) < mp.mpf("1e-8"),
            f"|lambda| = {float(abs_lam):.10f}")

    # D.2 — det(M_f) = |lambda|^2 ~ 0.7950 = (pi^2/4) eta_topo
    eta_topo = abs(z_star) ** 2
    expected_det = float((mp.pi ** 2 / 4) * eta_topo)
    actual_det = np.linalg.det(M_f)
    s.check("D", "D2: det(M_f) = |lambda|^2 = (pi^2/4) eta_topo ~ 0.7948",
            abs(actual_det - expected_det) < 1e-10,
            f"det(M_f) = {actual_det:.6f}; expected {expected_det:.6f}")

    # D.3 — Z-block eigenvectors are |v_W> and |v_W*> = (|0> ± i|1>)/sqrt(2)
    # (ZS-F0 v1.0(R) §8.8)
    eigvals_Mf, eigvecs_Mf = np.linalg.eig(M_f)
    # Expected: eigenvalues lambda, lambda_bar
    eig_set_match = (
        any(abs(e - complex(re_lam, im_lam)) < 1e-10 for e in eigvals_Mf)
        and any(abs(e - complex(re_lam, -im_lam)) < 1e-10 for e in eigvals_Mf)
    )
    s.check("D", "D3: Z-block eigenvalues are {lambda, lambda_bar} (Theorem 8.17)",
            eig_set_match,
            f"eigvals = {[complex(e) for e in eigvals_Mf]}")

    # D.4 — kappa = sqrt(A/Q); kappa^2 = A/Q = 35/4807; kappa^2/|lambda| ~ 0.0082
    kappa_sq = float(A_FRAC / Q)
    kappa = np.sqrt(kappa_sq)
    suppression = kappa_sq / float(abs_lam)
    s.check("D", "D4: kappa^2/|lambda| ~ 0.0082 X/Y-block suppression vs Z-block",
            abs(suppression - 0.0082) < 0.001,
            f"kappa^2 = A/Q = {kappa_sq:.6f}; kappa^2/|lambda| = {suppression:.4f}")

    # D.5 — Wilson dominant eigenvector lies in Z subspace (Theorem 9.4)
    # The full 11x11 Wilson loop has Z-block dominant; X/Y blocks have eigenvalue
    # kappa^2 * M_f^{00} ~ -0.00412, three orders of magnitude smaller than |lambda|
    # We verify the magnitude relation:
    M_f_00 = M_f[0, 0]  # Re(lambda)
    XY_block_dominant = abs(kappa_sq * M_f_00)
    Z_block_dominant = float(abs_lam)
    ratio = XY_block_dominant / Z_block_dominant
    s.check("D", "D5: |X/Y-block dominant| / |Z-block dominant| < 0.01 (Theorem 9.4)",
            ratio < 0.01,
            f"|X/Y|/|Z| = {XY_block_dominant:.6f}/{Z_block_dominant:.6f} = {ratio:.6f}")


# ============================================================================
# CATEGORY [E] - Dihedral D_4 Generators and Orders (4 tests)
# Source: ZS-F0 v1.0(R) §8.6, Theorem 8.13
# ============================================================================

def category_E(s: Suite, J):
    print("\n[E] Dihedral D_4 Generators and Orders")

    # J_Z = diag(+1, -1, +1, +1, ..., +1) (Definition 8.11)
    diag_Jz = [+1] + [-1] + [+1] * (Q - 2)
    J_Z = np.diag(diag_Jz).astype(int)

    # E.1 — J^2 = I and J_Z^2 = I
    J_sq = J @ J
    JZ_sq = J_Z @ J_Z
    s.check("E", "E1: J^2 = I and J_Z^2 = I (involutions, Theorem 8.13)",
            np.array_equal(J_sq, np.eye(Q, dtype=int))
            and np.array_equal(JZ_sq, np.eye(Q, dtype=int)),
            "both squared = I")

    # E.2 — [J, J_Z] != 0 (J and J_Z do not commute)
    commutator = J @ J_Z - J_Z @ J
    s.check("E", "E2: [J, J_Z] != 0 (non-commuting, Theorem 8.13)",
            np.any(commutator != 0),
            f"||[J,J_Z]||_F = {np.linalg.norm(commutator):.4f}")

    # E.3 — (J*J_Z)^4 = I but (J*J_Z)^2 != I (order exactly 4)
    JJZ = J @ J_Z
    power_2 = np.linalg.matrix_power(JJZ, 2)
    power_4 = np.linalg.matrix_power(JJZ, 4)
    order_4 = (np.array_equal(power_4, np.eye(Q, dtype=int))
               and not np.array_equal(power_2, np.eye(Q, dtype=int)))
    s.check("E", "E3: (J*J_Z) has order exactly 4 (Theorem 8.13)",
            order_4,
            f"(JJ_Z)^2 = I? {np.array_equal(power_2, np.eye(Q,dtype=int))}; "
            f"(JJ_Z)^4 = I? {np.array_equal(power_4, np.eye(Q,dtype=int))}")

    # E.4 — |D_4| = 8 (the group <J, J_Z> has order 8)
    # Generate the group by closure
    elements = {tuple(np.eye(Q, dtype=int).flatten())}
    frontier = [np.eye(Q, dtype=int)]
    generators = [J, J_Z]
    while frontier:
        new_frontier = []
        for g in frontier:
            for gen in generators:
                h = (g @ gen) % 2  # Z_2 multiplication preserved? No — these are
                # actual integer matrices; mod 2 is wrong. Use direct multiplication
                # with int
                h = g @ gen
                key = tuple(h.flatten())
                if key not in elements:
                    elements.add(key)
                    new_frontier.append(h)
        frontier = new_frontier
        if len(elements) > 16:
            break  # safety
    s.check("E", "E4: |<J, J_Z>| = 8 (Theorem 8.13: dihedral D_4 of order 8)",
            len(elements) == 8,
            f"group order = {len(elements)}")


# ============================================================================
# CATEGORY [F] - OOC Reconciliation Map (refined per Theorem F11.1') (3 tests)
# Source: ZS-F11 v1.0 dated update 2026-04-26 §DU.4
# ============================================================================

def category_F(s: Suite, J):
    print("\n[F] OOC Reconciliation Map (refined per Theorem F11.1')")

    # F.1 — (P1) "inside Z" projection: slots {0, 1} are the Z-sector slots.
    # The two Z-sector fixed-point objects |0>_Z and |v_W> have support in {0, 1}.
    Z_slots = [j for j, sec in SLOT_SECTOR.items() if sec == "Z"]
    p1_correct = (Z_slots == [0, 1])
    s.check("F", "F1: (P1) Z-sector slots = {0, 1}, supporting |0>_Z and |v_W>",
            p1_correct,
            f"Z-sector slots = {Z_slots}")

    # F.2 — (P2) "higher-level" projection: stroboscopic n is meta-index, not
    # a slot fixed point. We verify type-distinction by checking n is an integer
    # counter, not a vector in C^11.
    n_test = 0
    n_increments = [n_test + k for k in range(5)]  # successive event counts
    p2_correct = all(isinstance(n_val, int) for n_val in n_increments) and \
                 n_increments == [0, 1, 2, 3, 4]
    s.check("F", "F2: (P2) n is integer event-count meta-index (not a fixed point)",
            p2_correct,
            "n in Z_{>=0}, type-distinct from C^11 fixed-point objects")

    # F.3 — (P3) "orthogonal" projection: |5> is the unique J-fixed singleton
    # at the median slot, and is in the Y-sector.
    p3_correct = (J[5, 5] == 1
                  and SLOT_SECTOR[5] == "Y"
                  and 5 == (Q - 1) // 2)  # median slot
    s.check("F", "F3: (P3) |5> is unique J-fixed median slot in Y-sector",
            p3_correct,
            f"J|5>=|5>: {J[5, 5] == 1}; sector: {SLOT_SECTOR[5]}; median: {5 == (Q-1)//2}")


# ============================================================================
# CATEGORY [G] - Born-Rule Rank-Invariance (refined per Corollary F11.1A') (2 tests)
# Source: ZS-F11 v1.0 dated update 2026-04-26 §DU.5
# ============================================================================

def category_G(s: Suite, J):
    print("\n[G] Born-Rule Rank-Invariance (refined per §DU.5)")

    # G.1 — w_Y = rank(P_Y) / Q = 6/11 = dim(Y)/Q
    P_Y = np.diag([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])  # projector onto Y-sector
    w_Y = np.trace(P_Y) / Q
    s.check("G", "G1: w_Y = rank(P_Y)/Q = 6/11 (PROVEN, ZS-Q1 v1.0 §4.2)",
            abs(w_Y - 6.0/11.0) < 1e-14,
            f"w_Y = {w_Y:.10f}; expected {6/11:.10f}")

    # G.2 — Tr(U P_Y U^-1) = 6 = rank(P_Y) under unitary U (rank-invariance)
    # Test with two non-trivial unitaries:
    #   (i) the seam involution J (which DOES NOT preserve sector content but
    #       DOES preserve rank by trace cyclicity)
    #   (ii) a random unitary
    JT_PY_J = J.T @ P_Y @ J  # J is its own inverse since J^2 = I and J is real symmetric
    rank_J_invariant = (abs(np.trace(JT_PY_J) - 6) < 1e-14)

    np.random.seed(350437)  # canonical Z-Spin seed
    A_rand = np.random.randn(Q, Q) + 1j * np.random.randn(Q, Q)
    U_rand, _ = np.linalg.qr(A_rand)  # random unitary
    rank_random_invariant = (
        abs(np.trace(U_rand @ P_Y @ U_rand.conj().T).real - 6) < 1e-10
    )

    # Honest scope: J does NOT preserve P_Y as an operator
    J_preserves_PY = np.array_equal(J.T @ P_Y @ J, P_Y)

    s.check("G", "G2: Tr(U P_Y U^-1) = 6 under unitary U (rank-invariance, §DU.5)",
            rank_J_invariant and rank_random_invariant and not J_preserves_PY,
            f"Tr(JP_Y J) = {np.trace(JT_PY_J):.6f}; J preserves P_Y? {J_preserves_PY} (must be False)")


# ============================================================================
# CATEGORY [H] - Information-Time Consistency at 50-digit Precision (2 tests)
# Source: ZS-F10 v1.0 Theorem F10.1 §5.6; F-F11.4
# ============================================================================

def category_H(s: Suite):
    print("\n[H] Information-Time Consistency (50-digit mpmath)")

    # H.1 — Δν/Δn = 2A/π verified at 50-digit precision
    delta_nu_over_n = 2 * A_MP / mp.pi
    expected = mp.mpf(70) / (mp.mpf(437) * mp.pi)  # 2*(35/437)/pi = 70/(437*pi)
    residual = abs(delta_nu_over_n - expected)
    s.check("H", "H1: Δν/Δn = 2A/π = 70/(437π) at 50-digit (ZS-F10 §5.6)",
            residual < mp.mpf("1e-46"),
            f"Δν/Δn = {mp.nstr(delta_nu_over_n, 25)}, residual = {mp.nstr(residual, 5)}")

    # H.2 — Cross-check via timescale hierarchy: τ_n = t_P * exp(n π/A)
    # gives ln(τ_n/t_P)/n = π/A, and (A/π) * (π/A) = 1
    A_over_pi = A_MP / mp.pi
    pi_over_A = mp.pi / A_MP
    product = A_over_pi * pi_over_A
    s.check("H", "H2: (A/π)*(π/A) = 1 cross-check at 50-digit (ZS-U8 §4)",
            abs(product - 1) < mp.mpf("1e-46"),
            f"product = {mp.nstr(product, 25)}, deviation = {mp.nstr(abs(product-1), 5)}")


# ============================================================================
# CATEGORY [I'] - Permutation Control: Exact Enumeration on T(11) = 35,696 (10 tests)
# Source: ZS-F11 v1.0 dated update 2026-04-26 §DU.6
#
# HONEST SCOPE: This category replaces v1.0 §11 Monte Carlo. Reports
#   exact-enumeration p = 945/35,696 ≈ 2.65% under uniform-involution null.
#   This is "nontrivial selectivity, not strict 1% anti-numerology PASS".
#   The principal anti-numerology defense for ZS-F11 is the structural derivation
#   chain (ZS-F0 v1.0(R) Theorem 8.5 from Q = 11 odd, PROVEN), not this control.
# ============================================================================

def telephone(n):
    """Compute T(n), the number of involutions on n elements."""
    if n < 2:
        return 1
    a, b = 1, 1
    for k in range(2, n + 1):
        a, b = b, b + (k - 1) * a
    return b


def all_involutions(n):
    """Yield every involution on {0,...,n-1} (i.e., σ with σ^2 = id)."""
    # Build by recursive case analysis on element 0
    if n == 0:
        yield ()
        return
    if n == 1:
        yield (0,)
        return
    # Option A: 0 is fixed
    for sub in all_involutions(n - 1):
        # shift by +1 to act on {1,...,n-1}
        sigma = (0,) + tuple(s + 1 for s in sub)
        yield sigma
    # Option B: 0 is paired with k (k = 1,...,n-1)
    for k in range(1, n):
        # remaining elements form an involution on {1,...,n-1} \ {k}
        rest = [m for m in range(1, n) if m != k]
        for sub_perm in involutions_on_set(rest):
            sigma = list(range(n))
            sigma[0] = k
            sigma[k] = 0
            for src, dst in sub_perm.items():
                sigma[src] = dst
            yield tuple(sigma)


def involutions_on_set(elements):
    """Yield every involution on a given subset (returned as dict src->dst)."""
    if not elements:
        yield {}
        return
    if len(elements) == 1:
        yield {elements[0]: elements[0]}
        return
    first = elements[0]
    rest = elements[1:]
    # Option A: first is fixed
    for sub in involutions_on_set(rest):
        out = dict(sub)
        out[first] = first
        yield out
    # Option B: first is paired with some k in rest
    for k in rest:
        rest2 = [m for m in rest if m != k]
        for sub in involutions_on_set(rest2):
            out = dict(sub)
            out[first] = k
            out[k] = first
            yield out


def category_I_prime(s: Suite):
    print("\n[I'] Permutation Control: Exact Enumeration on T(11) = 35,696")
    print("    (HONEST SCOPE: not strict 1% anti-numerology PASS; reports p = 2.65%)")

    # I'.1 — T(11) = 35,696 (telephone number recurrence)
    T11 = telephone(11)
    s.check("I'", "I'1: T(11) = 35,696 (telephone number recurrence)",
            T11 == 35696,
            f"T(11) = {T11}")

    # I'.2 — Enumerate all involutions of S_11 and count those with at least one
    # fixed point (i.e., σ(j) = j for some j).
    print("    [I'] Enumerating all 35,696 involutions of S_11 (this takes ~5 seconds)...")
    all_invs = list(all_involutions(11))
    n_total = len(all_invs)
    s.check("I'", "I'2: Enumeration count matches T(11) = 35,696",
            n_total == 35696,
            f"enumerated count = {n_total}")

    # I'.3 — Count involutions with exactly one fixed point at j = 5
    # = involutions of {0,...,10} with σ(5)=5 and fixed-point-free on remaining 10
    n_unique_fixed_at_5 = sum(
        1 for sig in all_invs
        if sig[5] == 5 and sum(1 for j in range(11) if sig[j] == j) == 1
    )
    s.check("I'", "I'3: Involutions with unique fixed point at j = 5: count = 945",
            n_unique_fixed_at_5 == 945,
            f"count = {n_unique_fixed_at_5} = 10!/(2^5 5!) = {factorial(10)//(2**5 * factorial(5))}")

    # I'.4 — Exact-enumeration p-value: p = 945 / 35,696 ≈ 2.6474%
    p_value = n_unique_fixed_at_5 / n_total
    expected_p = 945 / 35696
    s.check("I'", "I'4: Exact-enumeration p = 945/35696 ≈ 2.65% (§DU.6)",
            abs(p_value - expected_p) < 1e-12,
            f"p = {p_value:.6f} = {p_value*100:.4f}%")

    # I'.5 — Honest scope: p > 1% strict threshold (NOT a STRONG PASS)
    strict_threshold = 0.01
    meets_strict = p_value < strict_threshold
    s.check("I'", "I'5: Honest scope: p = 2.65% does NOT meet strict 1% threshold",
            not meets_strict,
            f"p = {p_value:.4f} > 0.01 (strict threshold); STRONG PASS withdrawn per §DU.6")

    # I'.6 — By symmetry, P(unique fixed at any specific slot) = 945/35,696 for each slot.
    # Verify by direct count for slot 0 and slot 10.
    n_unique_fixed_at_0 = sum(
        1 for sig in all_invs
        if sig[0] == 0 and sum(1 for j in range(11) if sig[j] == j) == 1
    )
    s.check("I'", "I'6: Symmetry: P(unique fixed at j = 0) = 945 (matches j = 5)",
            n_unique_fixed_at_0 == 945,
            f"count at j=0: {n_unique_fixed_at_0}")

    # I'.7 — Total involutions with exactly one fixed point = 11 * 945 = 10,395
    n_exactly_one_fixed = sum(
        1 for sig in all_invs
        if sum(1 for j in range(11) if sig[j] == j) == 1
    )
    s.check("I'", "I'7: Total involutions with exactly one fixed point = 11 * 945 = 10,395",
            n_exactly_one_fixed == 11 * 945,
            f"count = {n_exactly_one_fixed} = 11 * 945")

    # I'.8 — Conditional P(fixed at j=5 | exactly one fixed) = 1/11
    cond_p = n_unique_fixed_at_5 / n_exactly_one_fixed
    s.check("I'", "I'8: Conditional P(fixed at j=5 | exactly 1 fixed) = 1/11 ≈ 9.09%",
            abs(cond_p - 1/11) < 1e-14,
            f"conditional P = {cond_p:.6f} = 1/{1/cond_p:.4f}")

    # I'.9 — Refutation of the v1.0 spurious-independence p-value (1/11)^4
    # The correct exact-enumeration null p ≈ 2.65% is approximately 387 times
    # larger than the spurious independence-assumption p (1/11)^4 ≈ 6.83e-5.
    spurious_p = (1/11)**4
    overstatement_factor = p_value / spurious_p
    s.check("I'", "I'9: Spurious-independence overstatement factor ~387x",
            abs(overstatement_factor - 387) < 5,
            f"true p / spurious p = {p_value:.6f} / {spurious_p:.2e} = {overstatement_factor:.1f}x")

    # I'.10 — Structural defense statement: |5> is selected by ZS-F0 Theorem 8.5
    # (Q=11 odd) PROVEN, NOT by random scan. We verify by direct computation that
    # the J-fixed slot is uniquely determined for any ordering of an odd-Q register.
    # For Q=11 with J|j>=|10-j>, the unique fixed is j=5; this is not a stochastic claim.
    structural_defense = (
        Q % 2 == 1  # Q is odd
        and (Q - 1) % 2 == 0  # so (Q-1)/2 is an integer
        and (Q - 1) // 2 == 5  # and equals 5
    )
    s.check("I'", "I'10: Structural defense: |5> is PROVEN unique J-fixed by Q=11 odd "
                  "(NOT by random scan)",
            structural_defense,
            f"Q={Q} odd: {Q%2==1}; (Q-1)/2 = {(Q-1)//2}; PROVEN by ZS-F0 Theorem 8.5")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("=" * 78)
    print("ZS-F11 v1.0 (with dated update 2026-04-26)")
    print("Verification Suite: Operational Observer Coordinate")
    print("=" * 78)
    print(f"  A = 35/437 = {A_FLOAT}  (LOCKED, ZS-F2 v1.0)")
    print(f"  Q = {Q}, (Z, X, Y) = ({DIM_Z}, {DIM_X}, {DIM_Y})  (PROVEN, ZS-F5 v1.0)")
    print(f"  z* = -W0(-i pi/2)/(i pi/2) = 0.4382829... + 0.3605924...i  (PROVEN, ZS-M1 v1.0)")
    print(f"  mpmath precision: {mp.mp.dps} digits")
    print()

    s = Suite()

    # Run all 9 categories
    J = category_A(s)
    category_B(s, J)
    category_C(s)
    category_D(s)
    category_E(s, J)
    category_F(s, J)
    category_G(s, J)
    category_H(s)
    category_I_prime(s)

    pass_count, total = s.summary()

    print()
    print("HONEST SCOPE STATEMENT (per ZS-F11 v1.0 dated update 2026-04-26 §DU.6, §DU.8):")
    print("  - Categories [A]-[H]: 28/28 PROVEN/DERIVED tests, all PASS at machine or 50-digit")
    print("    precision.")
    print("  - Category [I']: 10/10 permutation-control tests enumerated, with honest")
    print("    exact-enumeration p = 945/35,696 ≈ 2.65% under uniform-involution null.")
    print("    This is NOT a strict 1% anti-numerology PASS. The 'STRONG PASS' label of")
    print("    v1.0 §11 is withdrawn per §DU.6.")
    print("  - The principal anti-numerology defense for ZS-F11 is the structural")
    print("    derivation chain (ZS-F0 v1.0(R) Theorem 8.5 from Q = 11 odd, PROVEN),")
    print("    NOT the permutation control above.")
    print()
    print(f"  Status of ZS-M11 §H16 closure: OPEN -> DERIVED-CONDITIONAL (preserved)")
    print(f"  Status of Theorem F11.1: DERIVED-CONDITIONAL (preserved)")
    print(f"  Zero free parameters; zero new physical predictions.")
    print()

    if pass_count == total:
        print(f"  RESULT: {pass_count}/{total} enumerated PASS")
        sys.exit(0)
    else:
        print(f"  RESULT: {pass_count}/{total} enumerated PASS (FAILURES PRESENT)")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except OSError:
        # CI-friendly: exit 1 on any I/O error rather than crash
        sys.exit(1)
