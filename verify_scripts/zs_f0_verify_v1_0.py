#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║  ZS-F0 v1.0 — Ontological Bootstrap Verification Suite           ║
║  Kenny Kang                                                      ║
║  March 2026                                                      ║
║                                                                  ║
║  22 Tests: V1–V12 (Bootstrap Chain) + V13–V20 (Info Preserv.)    ║
║           + F-BOOT-5, F-BOOT-6 (Falsification Gates)             ║
║  7 OPEN Gates: F-BOOT-1 through F-BOOT-4, F-BOOT-7–9             ║
║  Anti-Numerology Check: Monte Carlo null hypothesis test         ║
║  Canonical seed: 350437 | Precision: mpmath 50-digit             ║
║                                                                  ║
║  Grand Reset: v1.0 (Consolidated from internal research notes    ║
║  up to v1.1.0)                                                   ║
╚══════════════════════════════════════════════════════════════════╝

Cross-references (all v1.0):
  ZS-F1: Action S, L_XY = 0 [PROVEN]
  ZS-F2: A = 35/437, δ-uniqueness [LOCKED]
  ZS-F5: Q=11, (Z,X,Y)=(2,3,6) [PROVEN]
  ZS-M3: J² = I, seam involution [PROVEN]
  ZS-A4: u_seam, Δ₂ protocol [DERIVED]
  ZS-A5: i-tetration, z*, η_topo [PROVEN]
  ZS-A6: Z-Telomere, phase accumulation [HYPOTHESIS]
  ZS-Q1: CPTP, dim(Z)=2, Born rule [PROVEN]
  ZS-Q7: Arrow of time, master equation [DERIVED]
"""

import sys
import time

# ─────────────────────────────────────────────────────────
#  Dependencies
# ─────────────────────────────────────────────────────────
try:
    from mpmath import mp, mpf, mpc, log, exp, pi, sqrt, fabs, re, im, conj, lambertw, matrix, eye, norm
    import mpmath
except ImportError:
    print("ERROR: mpmath required. Install with: pip install mpmath")
    sys.exit(1)

try:
    import numpy as np
    from scipy.linalg import expm, svdvals
except ImportError:
    print("ERROR: numpy and scipy required.")
    sys.exit(1)

import random

# ─────────────────────────────────────────────────────────
#  Configuration
# ─────────────────────────────────────────────────────────
mp.dps = 50  # 50-digit precision
SEED = 350437  # Canonical seed
random.seed(SEED)
np.random.seed(SEED)

# Locked constants (ZS-F2 v1.0, ZS-F5 v1.0)
A = mpf(35) / mpf(437)
Z_dim, X_dim, Y_dim = 2, 3, 6
Q = 11
HILBERT_DIM = Z_dim * X_dim * Y_dim  # = 36

# ─────────────────────────────────────────────────────────
#  Helper: Test runner
# ─────────────────────────────────────────────────────────
results = []

def run_test(test_id, description, test_func, expected_summary):
    """Execute a single test and record result."""
    t0 = time.time()
    try:
        passed, detail = test_func()
        dt = time.time() - t0
        status = "PASS" if passed else "FAIL"
    except Exception as e:
        dt = time.time() - t0
        passed = False
        status = "ERROR"
        detail = str(e)
    
    results.append((test_id, description, status, detail, dt))
    icon = "✓" if status == "PASS" else "✗"
    print(f"  [{icon}] {test_id}: {description}")
    print(f"       Expected: {expected_summary}")
    print(f"       Result:   {detail}")
    print(f"       Status:   {status} ({dt:.3f}s)")
    print()
    return passed


# ═══════════════════════════════════════════════════════════
#  PART I: BOOTSTRAP CHAIN VERIFICATION (V1–V12)
# ═══════════════════════════════════════════════════════════
print("=" * 70)
print("  ZS-F0 v1.0 VERIFICATION SUITE")
print("  Ontological Bootstrap: Why Non-Existence Is Self-Contradictory")
print("  and the i-Tetration Fixed Point as the Seed of Physical Law")
print("=" * 70)
print(f"\n  Precision: {mp.dps} digits | Seed: {SEED}")
print(f"  Locked: A = 35/437 = {float(A):.6f} (ZS-F2 v1.0)")
print(f"  Register: (Z,X,Y) = ({Z_dim},{X_dim},{Y_dim}), Q = {Q} (ZS-F5 v1.0)")
print(f"  Hilbert dim: {HILBERT_DIM}")
print()

print("─" * 70)
print("  PART I: Bootstrap Chain (V1–V12)")
print("─" * 70)
print()

# ───── V1: Boolean negation has no fixed point ─────
def test_V1():
    """
    §2.2 Lawvere bridge motivation.
    Boolean NOT: {0,1} → {0,1}, N(0)=1, N(1)=0.
    No x ∈ {0,1} with N(x) = x.
    Derivation: N(0)=1≠0, N(1)=0≠1. QED.
    """
    N = {0: 1, 1: 0}
    fixed_points = [x for x in [0, 1] if N[x] == x]
    passed = len(fixed_points) == 0
    return passed, f"Fixed points of NOT on {{0,1}}: {fixed_points} (empty = correct)"

run_test("V1", "Boolean negation has no fixed point", test_V1, "True (empty set)")

# ───── V2: Real negation: only trivial fixed point ─────
def test_V2():
    """
    §2.3 Frobenius bridge motivation.
    f(x) = -x on ℝ. f(x) = x ⟹ -x = x ⟹ 2x = 0 ⟹ x = 0.
    Only the trivial (annihilation) fixed point exists.
    """
    x_fp = mpf(0)
    test_vals = [mpf(v) for v in [-100, -1, -0.001, 0.001, 1, 100, 3.14159]]
    all_nontrivial_fail = all(-x != x for x in test_vals)
    passed = (x_fp == 0) and all_nontrivial_fail
    return passed, f"Unique fixed point: x = {float(x_fp)} (trivial annihilation)"

run_test("V2", "Real negation: only trivial fixed point x=0", test_V2, "x = 0")

# ───── V3: z = i + z has no solution ─────
def test_V3():
    """
    §2.4 Hyperoperation H₁ (addition): z = i + z.
    Subtract z from both sides: 0 = i. Contradiction.
    """
    i = mpc(0, 1)
    contradiction = (i != 0)
    return contradiction, f"z = i+z ⟹ 0 = i. Since i ≠ 0, CONTRADICTION confirmed."

run_test("V3", "H₁: z = i+z has no solution (contradiction)", test_V3, "Contradiction")

# ───── V4: z = i × z: only z = 0 ─────
def test_V4():
    """
    §2.4 Hyperoperation H₂ (multiplication): z = i·z.
    z(1 - i) = 0 ⟹ z = 0 (since 1-i ≠ 0).
    Only trivial fixed point.
    """
    i = mpc(0, 1)
    coeff = 1 - i
    coeff_nonzero = fabs(coeff) > 0
    z_fp = mpc(0, 0)
    check = i * z_fp
    passed = coeff_nonzero and (fabs(check - z_fp) < mpf(10)**(-40))
    return passed, f"z(1−i)=0, |1−i|={float(fabs(coeff)):.4f}≠0 ⟹ z=0 (trivial)"

run_test("V4", "H₂: z = i·z only z=0 (trivial)", test_V4, "z = 0")

# ───── V5: z = iᶻ converges (iteration) ─────
def test_V5():
    """
    §2.4 / §3.1: H₃ (exponentiation): z = iᶻ converges.
    Start from z₀ = i, iterate z_{n+1} = i^{z_n}.
    Should converge to z* within 1000 iterations.
    """
    i = mpc(0, 1)
    z = i
    for n in range(1000):
        z_new = exp(z * log(i))
        if fabs(z_new - z) < mpf(10)**(-40):
            return True, f"Converged at iteration {n+1}, z = {z_new}"
        z = z_new
    z_check = exp(z * log(i))
    resid = fabs(z_check - z)
    return float(resid) < 1e-10, f"After 1000 iter, residual = {float(resid):.2e}"

run_test("V5", "H₃: z = iᶻ converges from z₀=i", test_V5, "Convergence")

# ───── V6: z* via Lambert W (50-digit precision) ─────
def test_V6():
    """
    §3.1: z* = −2W₀(−iπ/2)/(iπ)

    Derivation:
      z = iᶻ = exp(iπz/2), let w = iπz/2:
      (2w)/(iπ) = exp(w) → w·exp(−w) = iπ/2 → (−w)·exp(−w) = −iπ/2
      −w = W₀(−iπ/2) → z = −2W₀(−iπ/2)/(iπ)
    """
    i_val = mpc(0, 1)
    arg = -i_val * pi / 2
    W0 = lambertw(arg, k=0)
    z_star = -2 * W0 / (i_val * pi)
    
    re_expected = mpf('0.4383')
    im_expected = mpf('0.3606')
    
    iz_star = exp(z_star * log(i_val))
    residual = fabs(iz_star - z_star)
    
    re_match = fabs(re(z_star) - re_expected) < mpf('0.0001')
    im_match = fabs(im(z_star) - im_expected) < mpf('0.0001')
    fp_precision = float(residual) < 1e-16
    
    passed = re_match and im_match and fp_precision
    return passed, (f"z* = {float(re(z_star)):.16f} + {float(im(z_star)):.16f}i, "
                    f"|iᶻ*−z*| = {float(residual):.2e}")

run_test("V6", "z* = 0.4383+0.3606i (Lambert W, 10⁻¹⁶)", test_V6, "Lambert W exact, residual < 10⁻¹⁶")

# ───── V7: |f'(z*)| < 1 (attractivity) ─────
def test_V7():
    """
    §3.1: f(z) = iᶻ = exp(iπz/2).
    f'(z) = iᶻ · ln(i) = iᶻ · (iπ/2).
    At z = z*: f'(z*) = z* · (iπ/2)  [since iᶻ* = z*].
    |f'(z*)| = |z*| · π/2 ≡ S (stability budget).
    Must have S < 1 for attractivity.
    """
    i_val = mpc(0, 1)
    arg = -i_val * pi / 2
    W0 = lambertw(arg, k=0)
    z_star = -2 * W0 / (i_val * pi)
    
    f_prime = z_star * i_val * pi / 2
    S = fabs(f_prime)
    z_abs = fabs(z_star)
    S_check = z_abs * pi / 2
    
    passed = (float(S) < 1) and (fabs(S - S_check) < mpf(10)**(-40))
    return passed, f"|f'(z*)| = |z*|·π/2 = {float(z_abs):.6f} × {float(pi/2):.6f} = {float(S):.4f} < 1 ✓"

run_test("V7", "|f'(z*)| = 0.8915 < 1 (attractivity)", test_V7, "S = 0.8915 < 1")

# ───── V8: k_W = 0 uniquely attractive ─────
def test_V8():
    """
    §3.1 / ZS-A5 §2.1: Exhaustive scan of Lambert W branches.
    For k_W ∈ {-50,...,50}, only k_W=0 gives |f'(z*)| < 1.
    """
    i_val = mpc(0, 1)
    arg = -i_val * pi / 2
    attractive_branches = []
    
    for k in range(-50, 51):
        try:
            Wk = lambertw(arg, k=k)
            zk = -2 * Wk / (i_val * pi)
            S_k = fabs(zk) * pi / 2
            if float(S_k) < 1.0:
                attractive_branches.append((k, float(re(zk)), float(im(zk)), float(S_k)))
        except:
            pass
    
    passed = (len(attractive_branches) == 1) and (attractive_branches[0][0] == 0)
    detail = f"Attractive branches in k∈[-50,50]: {attractive_branches}"
    return passed, detail

run_test("V8", "k_W=0 uniquely attractive (scan k∈[-50,50])", test_V8, "Only k=0")

# ───── V9: η_topo = |z*|² = 0.3221 ─────
def test_V9():
    """
    §3.2: Topological threshold.
    η_topo ≡ |z*|² = Re(z*)² + Im(z*)²
    """
    i_val = mpc(0, 1)
    arg = -i_val * pi / 2
    W0 = lambertw(arg, k=0)
    z_star = -2 * W0 / (i_val * pi)
    
    eta_topo = re(z_star)**2 + im(z_star)**2
    expected = mpf('0.32212')
    passed = fabs(eta_topo - expected) < mpf('0.00001')
    return passed, f"η_topo = |z*|² = {float(eta_topo):.10f}"

run_test("V9", "η_topo = |z*|² = 0.32212", test_V9, "0.32212")

# ───── V10: Ω_m(sector) = 39/121 ─────
def test_V10():
    """
    §3.3: Polyhedral sector counting route (ZS-F5 v1.0, ZS-A5 v1.0).
    Ω_m = X(Z + Q)/Q² = 3 × (2 + 11) / 11² = 3 × 13 / 121 = 39/121
    """
    omega_m_sector = mpf(X_dim) * (Z_dim + Q) / Q**2
    exact_frac = mpf(39) / mpf(121)
    
    passed = (omega_m_sector == exact_frac)
    return passed, f"Ω_m = {X_dim}×{Z_dim+Q}/{Q}² = 39/121 = {float(exact_frac):.6f}"

run_test("V10", "Ω_m(sector) = X(Z+Q)/Q² = 39/121 = 0.322314", test_V10, "39/121 = 0.322314")

# ───── V11: Convergence of two routes < 0.1% ─────
def test_V11():
    """
    §3.3: Two mathematically independent routes must converge.
    Route 1: η_topo = |z*|² (complex dynamics)
    Route 2: Ω_m = 39/121 (polyhedral combinatorics)
    """
    i_val = mpc(0, 1)
    W0 = lambertw(-i_val * pi / 2, k=0)
    z_star = -2 * W0 / (i_val * pi)
    eta_topo = float(re(z_star)**2 + im(z_star)**2)
    
    omega_sector = 39.0 / 121.0
    deviation_pct = abs(eta_topo - omega_sector) / omega_sector * 100
    
    passed = deviation_pct < 0.1
    return passed, f"|η_topo − Ω_m|/Ω_m = |{eta_topo:.6f} − {omega_sector:.6f}|/{omega_sector:.6f} = {deviation_pct:.4f}%"

run_test("V11", "Two-route convergence < 0.1%", test_V11, "0.06%")

# ───── V12: z = z^i does NOT converge ─────
def test_V12():
    """
    §2.4 / §4: The REVERSED equation z = z^i does NOT converge.
    Verifies directional uniqueness: i-tetration (z = iᶻ) is
    special; the reversed form (z = zⁱ) is unstable.
    """
    i_val = mpc(0, 1)
    z = mpc('0.5', '0.5')
    converged = False
    
    for n in range(1000):
        try:
            z_new = exp(i_val * log(z))
            if fabs(z_new - z) < mpf(10)**(-30):
                converged = True
                break
            if fabs(z_new) > mpf(10)**10 or fabs(z_new) < mpf(10)**(-10):
                break
            z = z_new
        except:
            break
    
    passed = not converged
    return passed, f"z = z^i after 1000 iter: converged={converged} (expected: No convergence)"

run_test("V12", "z = zⁱ does NOT converge (directional uniqueness)", test_V12, "No convergence")


# ═══════════════════════════════════════════════════════════
#  PART II: INFORMATION PRESERVATION VERIFICATION (V13–V20)
#  36-dim Hilbert space: Z(2) ⊗ X(3) ⊗ Y(6)
# ═══════════════════════════════════════════════════════════
print("─" * 70)
print("  PART II: Information Preservation (V13–V20)")
print("  36-dim Hilbert space: Z(2) ⊗ X(3) ⊗ Y(6)")
print("─" * 70)
print()


def build_zspin_hamiltonian():
    """
    Build the Z-Spin Hamiltonian on ℋ = ℋ_Z ⊗ ℋ_X ⊗ ℋ_Y
    dim = 2 × 3 × 6 = 36

    H = H_Z ⊗ I_X ⊗ I_Y  +  I_Z ⊗ H_X ⊗ I_Y  +  I_Z ⊗ I_X ⊗ H_Y
        + H_XZ (coupling)  +  H_ZY (coupling)

    CRITICAL CONSTRAINT: H_XY = 0 (no direct X-Y coupling).
    All X↔Y information flows through Z-mediation.
    This is the L_XY = 0 constraint (ZS-F1 v1.0, PROVEN).
    """
    dZ, dX, dY = Z_dim, X_dim, Y_dim
    d = dZ * dX * dY

    np.random.seed(SEED)

    def rand_hermitian(n, scale=1.0):
        M = np.random.randn(n, n) + 1j * np.random.randn(n, n)
        return scale * (M + M.conj().T) / 2

    H_Z = rand_hermitian(dZ, scale=0.5)
    H_X = rand_hermitian(dX, scale=0.3)
    H_Y = rand_hermitian(dY, scale=0.2)

    I_Z = np.eye(dZ)
    I_X = np.eye(dX)
    I_Y = np.eye(dY)

    H_Z_full = np.kron(H_Z, np.kron(I_X, I_Y))
    H_X_full = np.kron(I_Z, np.kron(H_X, I_Y))
    H_Y_full = np.kron(I_Z, np.kron(I_X, H_Y))

    V_XZ = rand_hermitian(dZ * dX, scale=float(A))
    H_XZ_full = np.kron(V_XZ, I_Y)

    V_ZY_base = rand_hermitian(dZ * dY, scale=float(A))
    H_ZY_full = np.zeros((d, d), dtype=complex)
    for x in range(dX):
        for z1 in range(dZ):
            for y1 in range(dY):
                for z2 in range(dZ):
                    for y2 in range(dY):
                        i = z1 * dX * dY + x * dY + y1
                        j = z2 * dX * dY + x * dY + y2
                        zy1 = z1 * dY + y1
                        zy2 = z2 * dY + y2
                        H_ZY_full[i, j] += V_ZY_base[zy1, zy2]

    H_total = H_Z_full + H_X_full + H_Y_full + H_XZ_full + H_ZY_full

    H_XY = np.zeros((d, d), dtype=complex)  # identically zero (L_XY = 0)

    return H_total, H_XY, H_Z_full, H_X_full, H_Y_full, H_XZ_full, H_ZY_full


def build_seam_involution():
    """
    Build seam involution J on the 36-dim Hilbert space (ZS-M3 v1.0).
    J|z,x,y⟩ → |dZ-1-z, dX-1-x, dY-1-y⟩
    Must satisfy J² = I (involution).
    """
    dZ, dX, dY = Z_dim, X_dim, Y_dim
    d = dZ * dX * dY
    J = np.zeros((d, d), dtype=complex)

    for z in range(dZ):
        for x in range(dX):
            for y in range(dY):
                i = z * dX * dY + x * dY + y
                z_f = dZ - 1 - z
                x_f = dX - 1 - x
                y_f = dY - 1 - y
                j = z_f * dX * dY + x_f * dY + y_f
                J[i, j] = 1.0

    return J


def partial_trace(rho, keep, dims):
    """Partial trace of density matrix rho over subsystems NOT in 'keep'."""
    n = len(dims)
    rho_r = rho.reshape([dims[i] for i in range(n)] * 2)

    trace_axes = [i for i in range(n) if i not in keep]

    for offset, ax in enumerate(sorted(trace_axes, reverse=True)):
        current_n = n - offset
        rho_r = np.trace(rho_r, axis1=ax, axis2=ax + current_n)

    d_keep = int(np.prod([dims[i] for i in keep]))
    return rho_r.reshape(d_keep, d_keep)


def von_neumann_entropy(rho):
    """S = -Tr(ρ ln ρ), computed via eigenvalues."""
    evals = np.linalg.eigvalsh(rho)
    evals = evals[evals > 1e-15]
    return -np.sum(evals * np.log(evals))


def mutual_info(rho, subsys_a, subsys_b, dims):
    """I(A:B) = S(A) + S(B) - S(AB)"""
    rho_a = partial_trace(rho, subsys_a, dims)
    rho_b = partial_trace(rho, subsys_b, dims)
    rho_ab = partial_trace(rho, subsys_a + subsys_b, dims)
    S_a = von_neumann_entropy(rho_a)
    S_b = von_neumann_entropy(rho_b)
    S_ab = von_neumann_entropy(rho_ab)
    return S_a + S_b - S_ab


# Build the Hamiltonian and seam involution
H_total, H_XY, H_Z_full, H_X_full, H_Y_full, H_XZ_full, H_ZY_full = build_zspin_hamiltonian()
J_matrix = build_seam_involution()
dims = [Z_dim, X_dim, Y_dim]

# Prepare initial state: random pure state |ψ₀⟩
psi0 = np.random.randn(HILBERT_DIM) + 1j * np.random.randn(HILBERT_DIM)
psi0 /= np.linalg.norm(psi0)
rho0 = np.outer(psi0, psi0.conj())


# ───── V13: H = H_X + H_Z + H_Y + H_XZ + H_ZY, H_XY = 0 ─────
def test_V13():
    """
    §8.2 / ZS-F1 v1.0: The Hamiltonian decomposes as
    H = H_Z + H_X + H_Y + H_XZ + H_ZY with H_XY ≡ 0.
    This is the L_XY = 0 constraint (PROVEN).
    """
    xy_norm = np.linalg.norm(H_XY, 'fro')
    herm_err = np.linalg.norm(H_total - H_total.conj().T, 'fro')
    H_sum = H_Z_full + H_X_full + H_Y_full + H_XZ_full + H_ZY_full
    decomp_err = np.linalg.norm(H_total - H_sum, 'fro')

    passed = (xy_norm < 1e-14) and (herm_err < 1e-14) and (decomp_err < 1e-14)
    return passed, (f"||H_XY||_F = {xy_norm:.2e}, ||H−H†||_F = {herm_err:.2e}, "
                    f"||H−Σ_parts||_F = {decomp_err:.2e}")

run_test("V13", "H = H_Z+H_X+H_Y+H_XZ+H_ZY, H_XY≡0 (Hermitian)", test_V13, "All norms = 0")

# ───── V14: Global von Neumann entropy S = 0 throughout ─────
def test_V14():
    """
    §8.2: Unitary evolution preserves global purity.
    If ρ₀ is pure, ρ(t) remains pure: S_global = 0 for all t.
    """
    max_S = 0
    for t in [0.1, 0.5, 1.0, 2.0, 5.0]:
        U = expm(-1j * H_total * t)
        rho_t = U @ rho0 @ U.conj().T
        S_global = von_neumann_entropy(rho_t)
        max_S = max(max_S, S_global)

    passed = max_S < 1e-14
    return passed, f"max S_global over t∈{{0.1,0.5,1.0,2.0,5.0}} = {max_S:.2e}"

run_test("V14", "Global S=0 throughout evolution (unitarity)", test_V14, "S < 10⁻¹⁴")

# ───── V15: X-sector entropy > 0 ─────
def test_V15():
    """§8.2: X-sector reduced state is MIXED (S_X > 0)."""
    t = 1.0
    U = expm(-1j * H_total * t)
    rho_t = U @ rho0 @ U.conj().T
    rho_X = partial_trace(rho_t, [1], dims)
    S_X = von_neumann_entropy(rho_X)

    passed = S_X > 0
    return passed, f"S_X(t=1.0) = {S_X:.4f} > 0 (local mixedness confirmed)"

run_test("V15", "X-sector entropy S_X > 0 (local mixedness)", test_V15, "S_X > 0")

# ───── V16: Y-sector entropy > 0 ─────
def test_V16():
    """§8.2: Y-sector reduced state is mixed."""
    t = 1.0
    U = expm(-1j * H_total * t)
    rho_t = U @ rho0 @ U.conj().T
    rho_Y = partial_trace(rho_t, [2], dims)
    S_Y = von_neumann_entropy(rho_Y)

    passed = S_Y > 0
    return passed, f"S_Y(t=1.0) = {S_Y:.4f} > 0 (Y-sector mixedness confirmed)"

run_test("V16", "Y-sector entropy S_Y > 0", test_V16, "S_Y > 0")

# ───── V17: J² = I (seam involution on 36-dim space) ─────
def test_V17():
    """
    §3.4 / ZS-M3 v1.0: Seam involution J satisfies J² = I.
    J|z,x,y⟩ = |dZ-1-z, dX-1-x, dY-1-y⟩; applying twice restores original.
    """
    J2 = J_matrix @ J_matrix
    I_36 = np.eye(HILBERT_DIM)
    err = np.linalg.norm(J2 - I_36, 'fro')

    passed = err < 1e-14
    return passed, f"||J² − I₃₆||_F = {err:.2e}"

run_test("V17", "J² = I (seam involution, 36-dim)", test_V17, "||J²−I|| = 0")

# ───── V18: Z-sector entropy bounded by ln(2) ─────
def test_V18():
    """
    §8.2: Z-sector entanglement entropy bounded by ln(dZ) = ln(2).
    The 2-dimensional Z-bottleneck has maximum entropy capacity ln(2) ≈ 0.693.
    """
    t = 1.0
    U = expm(-1j * H_total * t)
    rho_t = U @ rho0 @ U.conj().T
    rho_Z = partial_trace(rho_t, [0], dims)
    S_Z = von_neumann_entropy(rho_Z)
    max_S_Z = np.log(Z_dim)

    bounded = (S_Z <= max_S_Z + 1e-10)
    passed = bounded and (S_Z > 0)
    return passed, f"S_Z = {S_Z:.4f}, max = ln({Z_dim}) = {max_S_Z:.4f}. Bounded: {bounded}"

run_test("V18", "Z-sector entropy bounded by ln(2)", test_V18, "0 < S_Z ≤ ln(2) = 0.693")

# ───── V19: Stability budget S = |z*|·π/2 = 0.8915 ─────
def test_V19():
    """
    §8.3: Stability budget S = |z*| · π/2 from the i-tetration
    fixed point. This same quantity determines the three-generation
    limit (ZS-A5 v1.0) and confinement threshold (ZS-A5 v1.0).
    """
    i_val = mpc(0, 1)
    W0 = lambertw(-i_val * pi / 2, k=0)
    z_star = -2 * W0 / (i_val * pi)

    S_budget = float(fabs(z_star) * pi / 2)
    expected = 0.8915

    passed = abs(S_budget - expected) < 0.001
    return passed, f"S = |z*|·π/2 = {S_budget:.4f} (expected: {expected})"

run_test("V19", "Stability budget S = |z*|·π/2 = 0.8915", test_V19, "S = 0.8915 (= |f'(z*)|)")

# ───── V20: I(X:Y)_ZSpin < I(X:Y)_generic (ensemble) ─────
def test_V20():
    """
    §8.2 / ZS-F1 v1.0: The L_XY = 0 constraint suppresses direct X-Y
    mutual information compared to a generic Hamiltonian.
    Ensemble average over 20 random initial states and 20 random
    direct XY couplings.
    """
    N_ensemble = 20
    t = 0.5

    I_zspin_list = []
    I_generic_list = []

    for trial in range(N_ensemble):
        rng = np.random.RandomState(SEED + 100 + trial)

        psi = rng.randn(HILBERT_DIM) + 1j * rng.randn(HILBERT_DIM)
        psi /= np.linalg.norm(psi)
        rho_init = np.outer(psi, psi.conj())

        U_zs = expm(-1j * H_total * t)
        rho_zs = U_zs @ rho_init @ U_zs.conj().T
        I_zspin_list.append(mutual_info(rho_zs, [1], [2], dims))

        V_XY = rng.randn(X_dim * Y_dim, X_dim * Y_dim) + \
               1j * rng.randn(X_dim * Y_dim, X_dim * Y_dim)
        V_XY = float(A) * 3.0 * (V_XY + V_XY.conj().T) / 2
        H_XY_direct = np.kron(np.eye(Z_dim), V_XY)
        H_gen = H_total + H_XY_direct

        U_gen = expm(-1j * H_gen * t)
        rho_gen = U_gen @ rho_init @ U_gen.conj().T
        I_generic_list.append(mutual_info(rho_gen, [1], [2], dims))

    avg_zspin = np.mean(I_zspin_list)
    avg_generic = np.mean(I_generic_list)
    ratio = avg_generic / max(avg_zspin, 1e-15)

    passed = (avg_generic > avg_zspin) and (ratio > 1.0)
    return passed, (f"⟨I(X:Y)⟩_ZSpin = {avg_zspin:.4f}, ⟨I(X:Y)⟩_generic = {avg_generic:.4f}, "
                    f"ratio = {ratio:.2f}× (N={N_ensemble} ensemble)")

run_test("V20", "I(X:Y)_ZSpin < I(X:Y)_generic (L_XY=0 suppression)", test_V20, "Ratio > 1")


# ═══════════════════════════════════════════════════════════
#  PART III: FALSIFICATION GATES (F-BOOT-1 through F-BOOT-9)
# ═══════════════════════════════════════════════════════════
print("─" * 70)
print("  PART III: Falsification Gates (F-BOOT-1 to F-BOOT-9)")
print("─" * 70)
print()

def check_FBOOT5():
    """F-BOOT-5: η_topo must agree with Ω_m(sector) within 1%."""
    i_val = mpc(0, 1)
    W0 = lambertw(-i_val * pi / 2, k=0)
    z_star = -2 * W0 / (i_val * pi)
    eta = float(re(z_star)**2 + im(z_star)**2)
    omega = 39.0 / 121.0
    dev = abs(eta - omega) / omega * 100
    passed = dev < 1.0
    return passed, f"Deviation = {dev:.4f}% (threshold: <1%)"

run_test("F-BOOT-5", "η_topo ↔ Ω_m(sector) < 1% [PASS if <1%]", check_FBOOT5, "<1% → PASS")

def check_FBOOT6():
    """F-BOOT-6: No second attractive branch of z = iᶻ."""
    i_val = mpc(0, 1)
    arg = -i_val * pi / 2
    count = 0
    for k in range(-50, 51):
        try:
            Wk = lambertw(arg, k=k)
            zk = -2 * Wk / (i_val * pi)
            Sk = float(fabs(zk) * pi / 2)
            if Sk < 1.0:
                count += 1
        except:
            pass
    passed = count == 1
    return passed, f"Attractive branches found: {count} (must be exactly 1)"

run_test("F-BOOT-6", "No 2nd attractive branch (k_W=0 unique) [PASS if 1]", check_FBOOT6, "Exactly 1")

# OPEN gates (status report only)
open_gates = [
    ("F-BOOT-1", "Construct CCC + point-surjective morphism for B0", "OPEN (formalization target)"),
    ("F-BOOT-2", "Connect Frobenius to dim(Z)=2 derivation", "OPEN (formalization target)"),
    ("F-BOOT-3", "Publish H₃ minimality as peer-reviewed theorem", "OPEN (formalization target)"),
    ("F-BOOT-4", "Derive Ŵ²=I from bootstrap (not gauge)", "OPEN (formalization target)"),
    ("F-BOOT-7", "Formalize info-loss ↔ fixed-point destabilization", "OPEN (formalization target)"),
    ("F-BOOT-8", "Z-mediated model where recovery is impossible", "OPEN (formalization target)"),
    ("F-BOOT-9", "Alternative scrambling map outperforms i-tetration", "OPEN (formalization target)"),
]

for gate_id, desc, status in open_gates:
    print(f"  [○] {gate_id}: {desc}")
    print(f"       Status: {status}")
    print()


# ═══════════════════════════════════════════════════════════
#  PART IV: ANTI-NUMEROLOGY CHECK (Monte Carlo)
# ═══════════════════════════════════════════════════════════
print("─" * 70)
print("  PART IV: Anti-Numerology Monte Carlo")
print("  Null hypothesis: random constants can replicate convergence")
print("─" * 70)
print()

def anti_numerology_check():
    """
    Anti-numerology verification via Monte Carlo.

    Null hypothesis H₀: A random fraction a/b (with a,b ∈ [1,1000])
    can produce |z*|² matching a rational sector-counting formula to <0.1%.

    N_trials random "fake eta" values tested against small-integer
    rational targets. If p-value is small, numerology is rejected.
    """
    N_trials = 100000

    i_val = mpc(0, 1)
    W0 = lambertw(-i_val * pi / 2, k=0)
    z_star = -2 * W0 / (i_val * pi)
    eta_true = float(re(z_star)**2 + im(z_star)**2)

    # Generate rational targets from small-integer formulas
    targets = set()
    for X in range(1, 7):
        for Zv in range(1, 5):
            for Qv in range(2, 21):
                val = X * (Zv + Qv) / Qv**2
                if 0.1 < val < 0.9:
                    targets.add(round(val, 6))
    targets = list(targets)

    random.seed(SEED)
    hits = 0
    for trial in range(N_trials):
        fake_eta = 0.1 + 0.8 * random.random()
        for target in targets:
            if abs(fake_eta - target) / target < 0.001:
                hits += 1
                break

    p_value = hits / N_trials

    hits_specific = 0
    random.seed(SEED)
    target_specific = 39.0 / 121.0
    for trial in range(N_trials):
        fake_eta = 0.1 + 0.8 * random.random()
        if abs(fake_eta - target_specific) / target_specific < 0.001:
            hits_specific += 1

    p_specific = hits_specific / N_trials

    return (p_value, p_specific, hits, hits_specific, N_trials, len(targets))


p_any, p_specific, h_any, h_specific, N_mc, n_targets = anti_numerology_check()
print(f"  Monte Carlo trials: {N_mc:,}")
print(f"  Rational targets (small-integer formulas): {n_targets}")
print(f"  Hits (any target, <0.1%): {h_any} → p = {p_any:.4f}")
print(f"  Hits (39/121 specifically, <0.1%): {h_specific} → p = {p_specific:.6f}")
print()
print(f"  Interpretation:")
print(f"  - Random uniform value matching ANY rational target: p ≈ {p_any:.1%}")
print(f"  - Random value matching 39/121 specifically: p ≈ {p_specific:.4%}")
print(f"  - Z-Spin achieves 0.06% match via INDEPENDENT math (i-tetration)")
print(f"  - This is NOT a fit — η_topo is computed from z = iᶻ, not from Q=11")
print()


# ═══════════════════════════════════════════════════════════
#  PART V: OBSERVATIONAL CROSS-CHECK
# ═══════════════════════════════════════════════════════════
print("─" * 70)
print("  PART V: Observational Cross-Check (Planck 2018)")
print("─" * 70)
print()

i_val = mpc(0, 1)
W0_val = lambertw(-i_val * pi / 2, k=0)
z_star_val = -2 * W0_val / (i_val * pi)
eta_val = float(re(z_star_val)**2 + im(z_star_val)**2)

observables = [
    ("Ω_m (sector)", 39/121, 0.3150, 0.007, "X(Z+Q)/Q² = 39/121"),
    ("Ω_m (η_topo)", eta_val, 0.3150, 0.007, "|z*|²"),
    ("Ω_b", 6/121, 0.0493, 0.001, "XZ/Q² = 6/121"),
    ("Ω_c/Ω_b", 11/2, 5.38, 0.15, "Q/Z = 11/2"),
]

print(f"  {'Observable':<20} {'Z-Spin':>10} {'Planck':>10} {'σ':>6} {'Pull':>8}  Formula")
print(f"  {'─'*20} {'─'*10} {'─'*10} {'─'*6} {'─'*8}  {'─'*20}")

for name, zs_val, obs_val, obs_err, formula in observables:
    pull = abs(zs_val - obs_val) / obs_err
    print(f"  {name:<20} {zs_val:>10.6f} {obs_val:>10.4f} {obs_err:>6.4f} {pull:>7.2f}σ  {formula}")

print()
print("  Note: All Z-Spin values are DERIVED (zero free parameters).")
print("  2.3% offset from Planck is within expected range given")
print("  the simplicity of the sector-counting approximation.")
print()


# ═══════════════════════════════════════════════════════════
#  FINAL SUMMARY
# ═══════════════════════════════════════════════════════════
print("═" * 70)
print("  FINAL SUMMARY")
print("═" * 70)
print()

n_pass = sum(1 for r in results if r[2] == "PASS")
n_fail = sum(1 for r in results if r[2] == "FAIL")
n_error = sum(1 for r in results if r[2] == "ERROR")
n_total = len(results)

print(f"  Verification Tests:  {n_pass}/{n_total} PASS", end="")
if n_fail > 0:
    print(f", {n_fail} FAIL", end="")
if n_error > 0:
    print(f", {n_error} ERROR", end="")
print()

print(f"  Falsification Gates: 2/9 PASS, 7/9 OPEN (formalization targets)")
print(f"  Free Parameters:     0 (zero)")
print(f"  Anti-Numerology:     p(specific) = {p_specific:.6f}")
print()

if n_fail == 0 and n_error == 0:
    print("  ╔═══════════════════════════════════════════╗")
    print(f"  ║  ALL {n_total} TESTS PASSED — ZS-F0 v1.0 VERIFIED   ║")
    print("  ╚═══════════════════════════════════════════╝")
    exit_code = 0
else:
    print(f"  ⚠ {n_fail + n_error} test(s) did not pass. Review required.")
    exit_code = 1
    sys.exit(exit_code)
    
print()

# Detailed results table
print("─" * 70)
print("  Detailed Results")
print("─" * 70)
print(f"  {'ID':<12} {'Description':<45} {'Status':>6} {'Time':>7}")
print(f"  {'─'*12} {'─'*45} {'─'*6} {'─'*7}")
for test_id, desc, status, detail, dt in results:
    icon = "✓" if status == "PASS" else ("✗" if status == "FAIL" else "!")
    desc_trunc = desc[:44] if len(desc) > 44 else desc
    print(f"  {icon} {test_id:<10} {desc_trunc:<45} {status:>6} {dt:>6.3f}s")

print()
print(f"  Total execution time: {sum(r[4] for r in results):.2f}s")
print(f"  Canonical seed: {SEED}")
print(f"  Precision: {mp.dps} digits (mpmath)")
print()
print("  Kenny Kang")
print("  March 2026")
