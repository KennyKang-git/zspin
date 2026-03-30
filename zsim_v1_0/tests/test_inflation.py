"""Tests for the inflation modules (kernel/inflation.py, inflation_canonical.py).

Source: ZS-U1 §2, Paper 24 Appendix A, Paper 18 §2.1
Predictions: n_s ≈ 0.9667 (N*=60), r ≈ 0.0089
"""
import math
import pytest

from zsim.core.constants import A_LOCKED, LAMBDA_POTENTIAL, R_TENSOR, N_S_60
from zsim.kernel.inflation import (
    V_einstein,
    dV_einstein_deps,
    K_einstein,
    slow_roll_epsilon1,
    compute_inflation_observables,
)


# ─── Einstein-Frame Potential V_E(ε) ─────────────────────────────────

class TestEinsteinPotential:
    def test_V_E_at_attractor(self):
        """V_E(1) = 0 — same minimum as Jordan frame."""
        assert abs(V_einstein(1.0)) < 1e-15

    def test_V_E_positive_away_from_attractor(self):
        for eps in [0.5, 2.0, 5.0, 10.0]:
            assert V_einstein(eps) > 0

    def test_V_E_plateau_for_large_epsilon(self):
        """V_E → λ/(4A²) as ε → ∞ (Starobinsky-like plateau)."""
        eps_large = 100.0
        V = V_einstein(eps_large)
        plateau = LAMBDA_POTENTIAL / (4.0 * A_LOCKED ** 2)
        # Should approach but not exactly equal
        assert abs(V / plateau - 1.0) < 0.01

    def test_dV_E_at_attractor(self):
        """dV_E/dε = 0 at ε=1 (minimum)."""
        assert abs(dV_einstein_deps(1.0)) < 1e-10


# ─── Kinetic Metric K(ε) ─────────────────────────────────────────────

class TestKineticMetric:
    def test_K_positive(self):
        for eps in [0.01, 0.5, 1.0, 5.0, 50.0]:
            assert K_einstein(eps) > 0

    def test_K_at_attractor(self):
        """K(1) = 1/(1+A) + 6A²/(1+A)²."""
        F = 1.0 + A_LOCKED
        expected = 1.0 / F + 6.0 * A_LOCKED ** 2 / (F ** 2)
        assert abs(K_einstein(1.0) - expected) < 1e-12


# ─── Slow-Roll Parameters ────────────────────────────────────────────

class TestSlowRoll:
    def test_slow_roll_small_at_large_epsilon(self):
        """Slow-roll ε₁ ≪ 1 on the plateau (large ε)."""
        assert slow_roll_epsilon1(20.0) < 0.01

    def test_slow_roll_grows_near_end_of_inflation(self):
        """ε₁ increases as ε approaches the attractor."""
        eps_far = 20.0
        eps_near = 3.0
        assert slow_roll_epsilon1(eps_near) > slow_roll_epsilon1(eps_far)


# ─── Inflation Observables ────────────────────────────────────────────

class TestInflationObservables:
    def test_n_s_at_N60(self):
        """n_s ≈ 1 − 2/60 = 0.9667 for N*=60."""
        result = compute_inflation_observables(N_star=60.0)
        assert abs(result["n_s"] - N_S_60) < 0.002

    def test_r_at_N60(self):
        """Analytical r = 12/N^2 * (1+A)/(1+6A) for the leading-order formula.
        Full canonical-field gives r ~ 0.0089 (see test_v3_derived.py).
        """
        result = compute_inflation_observables(N_star=60.0)
        expected = 12.0 / 3600.0 * (1.0 + A_LOCKED) / (1.0 + 6.0 * A_LOCKED)
        assert abs(result["r"] - expected) < 1e-4

    def test_canonical_ns_monotonic(self):
        """n_s must be monotonically increasing with N* (physical requirement)."""
        from zsim.kernel.inflation_canonical import compute_full_inflation
        results = compute_full_inflation(N_star_values=list(range(45, 75)))
        ns_values = [r["n_s"] for r in results]
        for i in range(1, len(ns_values)):
            assert ns_values[i] > ns_values[i-1], \
                f"n_s not monotonic: N*={44+i} ({ns_values[i-1]:.6f}) -> N*={45+i} ({ns_values[i]:.6f})"

    def test_canonical_r_monotonic_decreasing(self):
        """r must be monotonically decreasing with N*."""
        from zsim.kernel.inflation_canonical import compute_full_inflation
        results = compute_full_inflation(N_star_values=list(range(45, 75)))
        r_values = [r["r"] for r in results]
        for i in range(1, len(r_values)):
            assert r_values[i] < r_values[i-1], \
                f"r not monotonic: N*={44+i} ({r_values[i-1]:.6f}) -> N*={45+i} ({r_values[i]:.6f})"

    def test_canonical_ns60_matches_book(self):
        """Canonical n_s at N*=60 should match book Chapter 9: 0.9674."""
        from zsim.kernel.inflation_canonical import compute_full_inflation
        results = compute_full_inflation(N_star_values=[60])
        ns60 = results[0]["n_s"]
        assert abs(ns60 - 0.9674) < 0.001, f"n_s(60) = {ns60:.4f}, expected ~0.9674"

    def test_canonical_r60_matches_book(self):
        """Canonical r at N*=60 should match book Chapter 9: 0.0089."""
        from zsim.kernel.inflation_canonical import compute_full_inflation
        results = compute_full_inflation(N_star_values=[60])
        r60 = results[0]["r"]
        assert abs(r60 - 0.0089) < 0.001, f"r(60) = {r60:.6f}, expected ~0.0089"

    def test_r_below_BK18_bound(self):
        """r < 0.036 (BICEP/Keck 2018 upper limit)."""
        result = compute_inflation_observables(N_star=60.0)
        assert result["r"] < 0.036

    def test_n_s_in_Planck_range(self):
        """n_s within Planck 2018 2σ range [0.955, 0.975]."""
        result = compute_inflation_observables(N_star=60.0)
        assert 0.955 < result["n_s"] < 0.975

    def test_A_correction_factor(self):
        """The Z-Spin correction factor (1+A)/(1+6A) is computed."""
        result = compute_inflation_observables(N_star=60.0)
        expected_correction = (1.0 + A_LOCKED) / (1.0 + 6.0 * A_LOCKED)
        assert abs(result["A_correction_factor"] - expected_correction) < 1e-6
