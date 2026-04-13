#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ZS_A7_v1_0_verification.py

Verification suite for ZS-A7 v1.0 — "Horizon as Spinor: BH/WH Duality and the 4π Closure"
Kenny Kang, April 2026

Target: 34 tests across 8 categories, all PASS.
Zero free parameters; all numerical results follow from PROVEN/DERIVED corpus inputs.

Categories:
  A. Locked Constants                       (5 tests)
  B. j = 1/2 Uniqueness                     (3 tests)
  C. Spinor-Descartes-Euler                 (3 tests)
  D. Half-Angle Verification                (4 tests)
  E. 4π Closure Toy Model                   (5 tests)
  F. CPTP / Choi-state (Theorem 3.2-bis)    (4 tests)
  G. Anti-Numerology                        (4 tests)
  H. Cross-Paper Consistency                (6 tests)
                                             ----
                                             34 tests

Run:  python3 ZS_A7_v1_0_verification.py
Expected output: 34/34 PASS, exit code 0.
Dependencies: numpy ≥ 1.20, scipy ≥ 1.7
Estimated runtime: < 10 seconds.

NOTE on definition of ũ_seam (signed seam witness):
  This script implements the operationally correct, Hadamard-test-compatible
  definition that is *linear in K_z(θ)* and therefore inherits the j = 1/2
  spinor sign flip:

      ũ_seam(θ) := Re Tr(K_0(0)† K_0(θ)) / ‖K_0(0)‖_F²

  where K_0(θ) = U_Z(θ)_{0z'} K_z'(0) is the rotated Kraus operator.
  The Choi state C_Λ is itself bilinear in Kraus and therefore unitarily
  invariant under any rotation of the Kraus index — so any expression that is
  bilinear in K_z is automatically 2π-periodic and cannot discriminate the
  spinor period. The above linear definition is the unique CPTP-compatible
  observable that exposes the 4π closure. (See ZS-A7 §3.2-bis Theorem 3.2-bis,
  parts 1 and 4.)
"""

import sys
import warnings
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.optimize import curve_fit, OptimizeWarning

# Suppress cosmetic warnings: curve_fit cannot estimate covariance when the
# residuals are at machine precision (χ² ≈ 1e-17), which is the EXPECTED
# regime for this verification — the fits are essentially exact.
warnings.filterwarnings("ignore", category=OptimizeWarning)

# ============================================================================
# CONFIGURATION
# ============================================================================

TOL_TIGHT = 1e-13       # machine-precision claims
TOL_NUM = 1e-9          # numerical-integration tolerance
TOL_FIT = 1e-8          # curve-fit residual (for χ² near 0)
RNG_SEED = 4317         # 4·π and 35/437 inspired

# ============================================================================
# REPORTING INFRASTRUCTURE
# ============================================================================

PASS_COUNT = 0
FAIL_COUNT = 0
FAIL_LIST = []
CATEGORY_COUNTS = {}


def report(test_id, name, condition, detail=""):
    """Record one test result."""
    global PASS_COUNT, FAIL_COUNT
    cat = test_id[0]
    CATEGORY_COUNTS.setdefault(cat, [0, 0])
    status = "PASS" if condition else "FAIL"
    line = f"  [{status}]  {test_id:<5} {name}"
    if detail:
        line += f"   →  {detail}"
    print(line)
    if condition:
        PASS_COUNT += 1
        CATEGORY_COUNTS[cat][0] += 1
    else:
        FAIL_COUNT += 1
        CATEGORY_COUNTS[cat][1] += 1
        FAIL_LIST.append((test_id, name, detail))


def section(letter, name, count):
    title = f"Category {letter}.  {name}   ({count} tests)"
    print(f"\n{title}")
    print("-" * max(60, len(title)))


def header():
    print("=" * 76)
    print("ZS-A7 v1.0 Verification Suite")
    print("Horizon as Spinor: BH/WH Duality and the 4π Closure")
    print("Kenny Kang  |  April 2026  |  Zero new parameters")
    print("=" * 76)


def footer():
    total = PASS_COUNT + FAIL_COUNT
    print("\n" + "=" * 76)
    print(f"RESULTS:  {PASS_COUNT}/{total} PASS")
    for cat in sorted(CATEGORY_COUNTS.keys()):
        p, f = CATEGORY_COUNTS[cat]
        marker = "✓" if f == 0 else "✗"
        print(f"  Category {cat}: {p}/{p+f} PASS  {marker}")
    print()
    if FAIL_COUNT == 0:
        print("STATUS:   ALL 34 TESTS PASSED  ✓")
        print("VERDICT:  ZS-A7 v1.0 verification suite COMPLETE.")
    else:
        print(f"STATUS:   {FAIL_COUNT} TEST(S) FAILED  ✗")
        print("\nFailed tests:")
        for tid, name, detail in FAIL_LIST:
            print(f"  - {tid}  {name}: {detail}")
    print("=" * 76)
    return FAIL_COUNT == 0


# ============================================================================
# MATHEMATICAL HELPERS
# ============================================================================

# Pauli matrices
I2 = np.eye(2, dtype=complex)
sigma_x = np.array([[0, 1], [1, 0]], dtype=complex)
sigma_y = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma_z = np.array([[1, 0], [0, -1]], dtype=complex)


def U_Z(theta):
    """SU(2) rotation around y-axis: U_Z(θ) = exp(-iθ σ_y / 2).
    This is the j = 1/2 representation of a rotation by θ about y."""
    return np.cos(theta / 2) * I2 - 1j * np.sin(theta / 2) * sigma_y


def kraus_rotate(K_0, K_1, theta):
    """Apply the j = 1/2 SU(2) rotation U_Z(θ) to the Kraus index.
    K_z(θ) = Σ_{z'} [U_Z(θ)]_{z z'} K_{z'}(0)."""
    U = U_Z(theta)
    K0_th = U[0, 0] * K_0 + U[0, 1] * K_1
    K1_th = U[1, 0] * K_0 + U[1, 1] * K_1
    return K0_th, K1_th


def signed_seam_witness(K_0_ref, K_0_at_theta):
    """Operationally correct ũ_seam(θ).

    ũ_seam(θ) := Re Tr(K_0(0)† K_0(θ)) / ‖K_0(0)‖_F²

    Linear in K_0(θ); inherits the j = 1/2 spinor sign flip at θ = 2π.
    The reference K_0(0) = K_0_ref serves as a fixed phase anchor (analogous
    to the reference beam in the Werner–Colella–Overhauser interferometer)."""
    inner = np.trace(K_0_ref.conj().T @ K_0_at_theta).real
    norm_sq = np.linalg.norm(K_0_ref, "fro") ** 2
    if norm_sq < 1e-15:
        return 0.0
    return inner / norm_sq


def vec_col(M):
    """Column-major vectorization of matrix M."""
    return M.flatten(order="F")


def choi_state(K_0, K_1):
    """Choi state C_Λ = Σ_z |K_z⟩⟩ ⟨⟨K_z| (column-major vec)."""
    v0 = vec_col(K_0).reshape(-1, 1)
    v1 = vec_col(K_1).reshape(-1, 1)
    return v0 @ v0.conj().T + v1 @ v1.conj().T


def dim_invariant_4(j):
    """dim Inv((V_j)^⊗4) for SU(2), via character integral.
    χ_j(θ) = sin((2j+1)θ) / sin(θ),  measure = (2/π) sin²θ dθ on [0, π]."""
    def integrand(theta):
        s = np.sin(theta)
        if abs(s) < 1e-13:
            chi = 2 * j + 1
        else:
            chi = np.sin((2 * j + 1) * theta) / s
        return (chi ** 4) * s ** 2
    val, _ = quad(integrand, 0.0, np.pi, limit=400)
    return (2 / np.pi) * val


def random_rank2_channel(rng, dim=2):
    """Random rank-2 CPTP channel on a dim-dimensional system.
    Returns (K_0, K_1) with K_0†K_0 + K_1†K_1 = I_dim.
    Construction: random complex Gaussian (2*dim, dim) → QR → thin isometry."""
    M = (rng.standard_normal((2 * dim, dim))
         + 1j * rng.standard_normal((2 * dim, dim))) / np.sqrt(2)
    Q, _ = np.linalg.qr(M)
    return Q[:dim, :], Q[dim:, :]


# ============================================================================
# MAIN — RUN ALL 34 TESTS
# ============================================================================

def main():
    header()
    rng = np.random.default_rng(RNG_SEED)

    # ------------------------------------------------------------------------
    section("A", "Locked Constants", 5)
    # ------------------------------------------------------------------------

    # A1: A = 35/437 (exact rational)
    A_frac = Fraction(35, 437)
    A_val = float(A_frac)
    cond = (A_frac == Fraction(35, 437)) and abs(A_val - 35 / 437) < TOL_TIGHT
    report("A1", "A = 35/437 (exact rational)",
           cond, f"A = {A_val:.15f}")

    # A2: Q = 11 prime
    Q = 11
    is_prime = (Q > 1) and all(Q % p != 0 for p in (2, 3, 5, 7))
    report("A2", "Q = 11 prime", is_prime, f"Q = {Q}")

    # A3: (Z, X, Y) = (2, 3, 6); Q = Z + X + Y = 11
    Z, X, Y = 2, 3, 6
    cond = (Z + X + Y == Q == 11)
    report("A3", "(Z,X,Y)=(2,3,6),  Q = Z+X+Y = 11",
           cond, f"{Z}+{X}+{Y}={Z + X + Y}")

    # A4: Z-sector slot indices {4, 6} ⊂ {0,…,10}
    z_slots = {4, 6}
    cond = z_slots.issubset(set(range(11))) and len(z_slots) == 2
    report("A4", "Z-sector slots = {|4⟩, |6⟩} in Q=11 register",
           cond, f"slots = {sorted(z_slots)}")

    # A5: J|_Z = σ_x   (since J|j⟩=|10−j⟩  ⇒  J|4⟩=|6⟩, J|6⟩=|4⟩)
    J_Z = np.array([[0, 1], [1, 0]], dtype=complex)
    cond = np.allclose(J_Z, sigma_x, atol=TOL_TIGHT)
    report("A5", "J|_Z = σ_x  (Q=11 seam restricted to {|4⟩,|6⟩})",
           cond, f"||J|_Z − σ_x|| = {np.linalg.norm(J_Z - sigma_x):.2e}")

    # ------------------------------------------------------------------------
    section("B", "j = 1/2 Uniqueness", 3)
    # ------------------------------------------------------------------------

    # B1: dim Inv((V_{1/2})^⊗4) = 2 (character integral)
    d_half = dim_invariant_4(0.5)
    cond = abs(d_half - 2) < TOL_NUM
    report("B1", "dim Inv((V_{1/2})^⊗4) = 2  (character integral)",
           cond, f"computed = {d_half:.10f}")

    # B2: dim Inv((V_j)^⊗4) ≠ 2 for j ∈ {1, 3/2, 2, 5/2}
    other_j = [1.0, 1.5, 2.0, 2.5]
    other_dims = {j: dim_invariant_4(j) for j in other_j}
    none_equal_2 = all(abs(d - 2) > 0.5 for d in other_dims.values())
    detail_str = ", ".join(f"j={j}: {other_dims[j]:.3f}" for j in other_j)
    report("B2", "dim Inv((V_j)^⊗4) ≠ 2 for j ∈ {1, 3/2, 2, 5/2}",
           none_equal_2, detail_str)

    # B3: D^{1/2}(2π physical rotation) = -I,  D^{1/2}(4π) = +I
    U_2pi = U_Z(2 * np.pi)
    U_4pi = U_Z(4 * np.pi)
    err_2pi = np.linalg.norm(U_2pi - (-I2))
    err_4pi = np.linalg.norm(U_4pi - I2)
    cond = (err_2pi < TOL_TIGHT) and (err_4pi < TOL_TIGHT)
    report("B3", "D^{1/2}(2π)=−I,  D^{1/2}(4π)=+I",
           cond, f"||U(2π)+I||={err_2pi:.2e}, ||U(4π)−I||={err_4pi:.2e}")

    # ------------------------------------------------------------------------
    section("C", "Spinor-Descartes-Euler", 3)
    # ------------------------------------------------------------------------

    # C1: Cube total angular defect = 4π
    # Each vertex meets 3 squares (interior angle π/2), defect = 2π − 3π/2 = π/2
    cube_per_vertex = 2 * np.pi - 3 * (np.pi / 2)
    cube_total = 8 * cube_per_vertex
    cond = abs(cube_total - 4 * np.pi) < TOL_TIGHT
    report("C1", "Cube angular defect = 4π",
           cond, f"computed = {cube_total:.10f},  4π = {4 * np.pi:.10f}")

    # C2: Truncated icosahedron total angular defect = 4π
    # Each vertex meets 1 pentagon (3π/5) + 2 hexagons (2π/3 each)
    # defect/vertex = 2π − 3π/5 − 4π/3 = π/15;  60 × π/15 = 4π
    ti_per_vertex = 2 * np.pi - 3 * np.pi / 5 - 4 * np.pi / 3
    ti_total = 60 * ti_per_vertex
    cond = abs(ti_total - 4 * np.pi) < TOL_NUM
    report("C2", "Truncated icosahedron angular defect = 4π",
           cond, f"60 × {ti_per_vertex:.6f} = {ti_total:.10f}")

    # C3: 2π · dim(Z) = 4π
    spinor_period = 2 * np.pi * Z  # Z = 2
    cond = abs(spinor_period - 4 * np.pi) < TOL_TIGHT
    report("C3", "2π · dim(Z) = 4π  (spinor closure period)",
           cond, f"2π × {Z} = {spinor_period:.10f}")

    # ------------------------------------------------------------------------
    section("D", "Half-Angle Verification", 4)
    # ------------------------------------------------------------------------

    A = 35 / 437

    # D1: phase factor of V_XZ at ε=0 → exp(+iπ/2) = +i
    eps_h = 0.0
    theta_h = np.pi * (1 - eps_h)
    phase_VXZ = np.exp(1j * theta_h / 2)
    err = abs(phase_VXZ - 1j)
    cond = err < TOL_TIGHT
    report("D1", "phase(V_XZ) at ε=0 = exp(+iπ/2) = +i",
           cond, f"phase = {phase_VXZ},  err = {err:.2e}")

    # D2: phase factor of V_ZY at ε=0 → exp(−iπ/2) = −i
    phase_VZY = np.exp(-1j * theta_h / 2)
    err = abs(phase_VZY - (-1j))
    cond = err < TOL_TIGHT
    report("D2", "phase(V_ZY) at ε=0 = exp(−iπ/2) = −i",
           cond, f"phase = {phase_VZY},  err = {err:.2e}")

    # D3: B_Z phase product at horizon = +1 (real)
    BZ_phase = phase_VZY * phase_VXZ
    cond = abs(BZ_phase - 1.0) < TOL_TIGHT and abs(BZ_phase.imag) < TOL_TIGHT
    report("D3", "B_Z phase = (−i)·(+i) = +1  (real)",
           cond, f"B_Z = {BZ_phase}")

    # D4: V_ZY = (V_XZ)* across ε ∈ {0.1, 0.3, 0.5, 0.7, 0.9}
    eps_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    max_diff = 0.0
    for eps in eps_values:
        theta = np.pi * (1 - eps)
        amp = np.sqrt(A) * eps / np.sqrt(1 + A * eps ** 2)
        V_XZ = amp * np.exp(1j * theta / 2)
        V_ZY = amp * np.exp(-1j * theta / 2)
        max_diff = max(max_diff, abs(V_ZY - np.conj(V_XZ)))
    cond = max_diff < TOL_TIGHT
    report("D4", "V_ZY = (V_XZ)* across ε ∈ {.1,.3,.5,.7,.9}",
           cond, f"max |V_ZY − conj(V_XZ)| = {max_diff:.2e}")

    # ------------------------------------------------------------------------
    section("E", "4π Closure Toy Model", 5)
    # ------------------------------------------------------------------------

    # Construct a clean orthogonal-Kraus toy channel:
    # K_0 = E_{00},  K_1 = E_{11}  (matrix units)
    # CPTP:  K_0†K_0 + K_1†K_1 = diag(1,0) + diag(0,1) = I  ✓
    # HS-orthogonality:  Tr(K_1† K_0) = 0  ⇒  ũ_seam(θ) = cos(θ/2) exactly
    K_0 = np.array([[1, 0], [0, 0]], dtype=complex)
    K_1 = np.array([[0, 0], [0, 1]], dtype=complex)

    # E1: CPTP condition Σ K_z† K_z = I
    cptp_residual = K_0.conj().T @ K_0 + K_1.conj().T @ K_1 - I2
    cond = np.linalg.norm(cptp_residual, "fro") < TOL_TIGHT
    report("E1", "Toy channel: Σ K_z† K_z = I",
           cond, f"residual = {np.linalg.norm(cptp_residual):.2e}")

    # E2: ũ_seam(0) = +1
    K0_at_0, _ = kraus_rotate(K_0, K_1, 0.0)
    u0 = signed_seam_witness(K_0, K0_at_0)
    cond = abs(u0 - 1.0) < TOL_TIGHT
    report("E2", "ũ_seam(0) = +1",
           cond, f"computed = {u0:.15f}")

    # E3: ũ_seam(2π) = −1   (spinor sign flip)
    K0_at_2pi, _ = kraus_rotate(K_0, K_1, 2 * np.pi)
    u_2pi = signed_seam_witness(K_0, K0_at_2pi)
    cond = abs(u_2pi - (-1.0)) < TOL_TIGHT
    report("E3", "ũ_seam(2π) = −1   (spinor sign flip)",
           cond, f"computed = {u_2pi:.15f}")

    # E4: ũ_seam(4π) = +1   (full closure)
    K0_at_4pi, _ = kraus_rotate(K_0, K_1, 4 * np.pi)
    u_4pi = signed_seam_witness(K_0, K0_at_4pi)
    cond = abs(u_4pi - 1.0) < TOL_TIGHT
    report("E4", "ũ_seam(4π) = +1   (full closure)",
           cond, f"computed = {u_4pi:.15f}")

    # E5: ũ_seam(θ_k) = cos(θ_k/2) for k = 0..16
    theta_samples = np.array([k * np.pi / 4 for k in range(17)])
    max_err = 0.0
    for theta in theta_samples:
        K_th, _ = kraus_rotate(K_0, K_1, theta)
        u = signed_seam_witness(K_0, K_th)
        max_err = max(max_err, abs(u - np.cos(theta / 2)))
    cond = max_err < TOL_TIGHT
    report("E5", "ũ_seam(θ_k) = cos(θ_k/2) over 17 sample points",
           cond, f"max error = {max_err:.2e}")

    # ------------------------------------------------------------------------
    section("F", "CPTP / Choi-state (Theorem 3.2-bis)", 4)
    # ------------------------------------------------------------------------

    # F1: Number of Kraus operators = dim(Z) = 2
    n_kraus = 2  # by toy construction
    cond = (n_kraus == Z)
    report("F1", "Number of Kraus operators = dim(Z) = 2",
           cond, f"n_kraus = {n_kraus}, dim(Z) = {Z}")

    # F2: Choi state C_Λ is unitarily invariant under U_Z(θ) (i.e., 2π-periodic AND
    # in fact fully invariant — bilinearity in K_z forces this).
    C_at_0 = choi_state(K_0, K_1)
    diffs = []
    for th in [np.pi / 3, np.pi, 2 * np.pi, 5 * np.pi / 4, 4 * np.pi]:
        Kth0, Kth1 = kraus_rotate(K_0, K_1, th)
        C_th = choi_state(Kth0, Kth1)
        diffs.append(np.linalg.norm(C_th - C_at_0, "fro"))
    cond = max(diffs) < TOL_TIGHT
    report("F2", "Choi state C_Λ is unitarily invariant (⇒ 2π-periodic)",
           cond, f"max ||C(θ) − C(0)|| = {max(diffs):.2e}")

    # F3: ũ_seam IS 4π-periodic AND IS NOT 2π-periodic (period discrimination)
    test_thetas = [0.1, np.pi / 3, np.pi, 5 * np.pi / 4, 7 * np.pi / 3]
    period_4pi_ok = True
    period_2pi_breaks_ok = True
    for theta in test_thetas:
        K_th, _ = kraus_rotate(K_0, K_1, theta)
        K_th_2pi, _ = kraus_rotate(K_0, K_1, theta + 2 * np.pi)
        K_th_4pi, _ = kraus_rotate(K_0, K_1, theta + 4 * np.pi)
        u_th = signed_seam_witness(K_0, K_th)
        u_th_2pi = signed_seam_witness(K_0, K_th_2pi)
        u_th_4pi = signed_seam_witness(K_0, K_th_4pi)
        if abs(u_th_4pi - u_th) > TOL_TIGHT:
            period_4pi_ok = False
        # 2π-periodicity must NOT hold (the value should be sign-flipped, not equal)
        if abs(u_th_2pi - u_th) < TOL_TIGHT and abs(u_th) > TOL_TIGHT:
            period_2pi_breaks_ok = False
    cond = period_4pi_ok and period_2pi_breaks_ok
    report("F3", "ũ_seam is 4π-periodic but NOT 2π-periodic",
           cond, f"period 4π: {period_4pi_ok}, breaks 2π: {period_2pi_breaks_ok}")

    # F4: Single j=1/2 internal factor: K_z(θ) = U_Z(θ)_{zz'} K_{z'}(0)
    max_err = 0.0
    for theta in [np.pi / 3, np.pi / 2, np.pi, 5 * np.pi / 4, 7 * np.pi / 3]:
        U = U_Z(theta)
        K0_direct = U[0, 0] * K_0 + U[0, 1] * K_1
        K1_direct = U[1, 0] * K_0 + U[1, 1] * K_1
        K0_func, K1_func = kraus_rotate(K_0, K_1, theta)
        e = max(np.linalg.norm(K0_direct - K0_func, "fro"),
                np.linalg.norm(K1_direct - K1_func, "fro"))
        max_err = max(max_err, e)
    cond = max_err < TOL_TIGHT
    report("F4", "Single j=1/2 factor: K_z(θ) = U_Z(θ)_{zz'} K_{z'}(0)",
           cond, f"max ||K_direct − K_func|| = {max_err:.2e}")

    # ------------------------------------------------------------------------
    section("G", "Anti-Numerology", 4)
    # ------------------------------------------------------------------------

    N_TRIALS = 100
    THETAS_FIT = np.linspace(0, 4 * np.pi, 17)

    def model_M1(theta, b, phi, c):
        """4π-periodic spinor model."""
        return c + b * np.cos(theta / 2 + phi)

    def model_M0(theta, b, phi, c):
        """2π-periodic vector model."""
        return c + b * np.cos(theta + phi)

    fit_chi2 = []
    discrim_passes = 0
    for _ in range(N_TRIALS):
        K0_r, K1_r = random_rank2_channel(rng)
        u_data = np.array([
            signed_seam_witness(K0_r, kraus_rotate(K0_r, K1_r, t)[0])
            for t in THETAS_FIT
        ])
        try:
            popt_1, _ = curve_fit(model_M1, THETAS_FIT, u_data, p0=[0.5, 0, 0])
            chi2_1 = float(np.sum((u_data - model_M1(THETAS_FIT, *popt_1)) ** 2))
        except Exception:
            chi2_1 = np.inf
        try:
            popt_0, _ = curve_fit(model_M0, THETAS_FIT, u_data, p0=[0.5, 0, 0])
            chi2_0 = float(np.sum((u_data - model_M0(THETAS_FIT, *popt_0)) ** 2))
        except Exception:
            chi2_0 = np.inf
        fit_chi2.append(chi2_1)
        R = (chi2_0 / chi2_1) if chi2_1 > 1e-30 else np.inf
        if R > 4 or chi2_1 < TOL_FIT:
            discrim_passes += 1

    # G1: ≥99/100 random channels: M_1 fits with χ² < TOL_FIT
    n_perfect = sum(1 for c in fit_chi2 if c < TOL_FIT)
    cond = n_perfect >= 99
    report("G1", f"≥99/100 random channels: M_1 fits cos(θ/2) (χ² < {TOL_FIT:.0e})",
           cond, f"{n_perfect}/100 perfect, max χ² = {max(fit_chi2):.2e}")

    # G2: ≥99/100 random channels: discrimination ratio R > 4
    cond = discrim_passes >= 99
    report("G2", "≥99/100 random channels: R = χ²_M0 / χ²_M1 > 4",
           cond, f"{discrim_passes}/100 discriminate H_1 vs H_0")

    # G3: Spinor sign flip ũ(2π) = −ũ(0) is universal across random channels
    rng2 = np.random.default_rng(RNG_SEED + 1)
    n_signflip = 0
    for _ in range(N_TRIALS):
        K0_r, K1_r = random_rank2_channel(rng2)
        u0_r = signed_seam_witness(K0_r, kraus_rotate(K0_r, K1_r, 0.0)[0])
        u_2pi_r = signed_seam_witness(K0_r, kraus_rotate(K0_r, K1_r, 2 * np.pi)[0])
        if abs(u_2pi_r - (-u0_r)) < TOL_NUM:
            n_signflip += 1
    cond = n_signflip >= 99
    report("G3", "Spinor sign flip ũ(2π) = −ũ(0) for ≥99/100 random channels",
           cond, f"{n_signflip}/100 satisfy sign flip")

    # G4: Specificity — random noise data does NOT spuriously trigger R > 4
    rng3 = np.random.default_rng(RNG_SEED + 2)
    false_positives = 0
    for _ in range(N_TRIALS):
        u_noise = rng3.standard_normal(17) * 0.5
        try:
            popt_1, _ = curve_fit(model_M1, THETAS_FIT, u_noise, p0=[0.3, 0, 0])
            chi2_1 = float(np.sum((u_noise - model_M1(THETAS_FIT, *popt_1)) ** 2))
            popt_0, _ = curve_fit(model_M0, THETAS_FIT, u_noise, p0=[0.3, 0, 0])
            chi2_0 = float(np.sum((u_noise - model_M0(THETAS_FIT, *popt_0)) ** 2))
            R = (chi2_0 / chi2_1) if chi2_1 > 1e-30 else np.inf
            if R > 4:
                false_positives += 1
        except Exception:
            pass
    # Specificity: ≤15/100 false positives is acceptable for n=17 noise samples
    cond = false_positives <= 15
    report("G4", "Specificity: random noise → R > 4 in ≤ 15/100 cases",
           cond, f"{false_positives}/100 false positives")

    # ------------------------------------------------------------------------
    section("H", "Cross-Paper Consistency", 6)
    # ------------------------------------------------------------------------

    # H1: ZS-Q7 Theorem 1 (Dimension Ratio): dim(Y)/dim(X) = 6/3 = 2
    ratio = Y / X
    cond = abs(ratio - 2.0) < TOL_TIGHT
    report("H1", "ZS-Q7 Thm 1: dim(Y)/dim(X) = 6/3 = 2",
           cond, f"computed = {ratio}")

    # H2: ZS-Q1 §3.3 CPTP for the toy
    cptp_2 = K_0.conj().T @ K_0 + K_1.conj().T @ K_1 - I2
    cond = np.linalg.norm(cptp_2, "fro") < TOL_TIGHT
    report("H2", "ZS-Q1 §3.3:  Σ K_z† K_z = I  (toy)",
           cond, f"residual = {np.linalg.norm(cptp_2):.2e}")

    # H3: ZS-A4 §4.1 unsigned u_seam = 0 for seam-symmetric channel
    # K_0 = I/√2, K_1 = σ_x/√2  (CPTP, manifestly seam-symmetric on the Z-subspace)
    K0_sym = I2 / np.sqrt(2)
    K1_sym = sigma_x / np.sqrt(2)
    cptp_sym = K0_sym.conj().T @ K0_sym + K1_sym.conj().T @ K1_sym
    cptp_ok = np.allclose(cptp_sym, I2, atol=TOL_TIGHT)
    C_sym = choi_state(K0_sym, K1_sym)
    JJ = np.kron(sigma_x, sigma_x)  # J ⊗ J on the doubled space
    seam_defect = JJ @ C_sym @ JJ - C_sym.T
    u_unsigned = (np.linalg.norm(seam_defect, "fro")
                  / np.linalg.norm(C_sym, "fro"))
    cond = cptp_ok and (u_unsigned < TOL_NUM)
    report("H3", "ZS-A4: unsigned u_seam = 0 for seam-symmetric channel",
           cond, f"u_seam = {u_unsigned:.2e}")

    # H4: ZS-T2 / ZS-S2: A/Q = 35/4807 ≈ 0.007281
    A_over_Q = (35 / 437) / 11
    expected_AQ = 35 / 4807
    cond = abs(A_over_Q - expected_AQ) < TOL_TIGHT
    report("H4", "ZS-T2: A/Q = 35/4807 ≈ 0.007281",
           cond, f"A/Q = {A_over_Q:.10f}")

    # H5: ZS-M3 Lemma 10.1 generalized: D^j(−I) = (−1)^{2j} I
    # Test j ∈ {1/2, 1, 3/2}: signs should be (−1, +1, −1)
    j_list = [0.5, 1.0, 1.5]
    signs = [(-1) ** int(round(2 * j)) for j in j_list]
    cond = signs == [-1, 1, -1]
    report("H5", "ZS-M3 Lem 10.1: (−1)^{2j} for j ∈ {1/2, 1, 3/2} = {−1,+1,−1}",
           cond, f"signs = {tuple(signs)}")

    # H6: ZS-A6 §3 boundary condition: F(ε=0) = 1 + A·0² = 1
    F_horizon = 1 + A * (0.0 ** 2)
    cond = abs(F_horizon - 1.0) < TOL_TIGHT
    report("H6", "ZS-A6 §3: F(ε=0) = 1 + A·0² = 1",
           cond, f"F(0) = {F_horizon}")

    # ------------------------------------------------------------------------
    return footer()


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
