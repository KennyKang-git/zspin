"""Tests for v3.0 derived constants, derived.yaml config, and structural assertions.

Source: ZS-F1, ZS-F2, ZS-U1, ZS-M5, ZS-S1
Anti-numerology discipline: every number requires a derivation chain.
"""
import math
import pytest

from zsim.core.constants import (
    A_LOCKED,
    A_FRACTION,
    DELTA_X,
    DELTA_Y,
    DIM_X,
    DIM_Y,
    DIM_Z,
    ETA_B,
    G_EFF_RATIO,
    G_MUB,
    H0_RATIO,
    H_ZS_OVER_H_GR,
    KAPPA,
    LAMBDA_POTENTIAL,
    M_EPSILON_OVER_MP,
    N_S_55,
    N_S_60,
    OMEGA_B,
    OMEGA_M_EFF,
    Q_TOTAL,
    R_TENSOR,
    TAU_D_OVER_TAU_PENROSE,
    X_STAR,
    Z_STAR_IM,
    Z_STAR_MOD_SQ,
)
from zsim.core.config import ZSimConfig


# ─── Structural Constants ────────────────────────────────────────────

class TestStructuralConstants:
    def test_A_is_exact_fraction(self):
        """A = 35/437 exactly (IEEE 754 bit-identical)."""
        assert A_LOCKED == 35 / 437
        assert A_FRACTION.numerator == 35
        assert A_FRACTION.denominator == 437

    def test_partition(self):
        assert (DIM_X, DIM_Z, DIM_Y) == (3, 2, 6)
        assert Q_TOTAL == 11
        assert DIM_X + DIM_Z + DIM_Y == Q_TOTAL

    def test_G_MUB(self):
        """G = Q + 1 = 12 MUBs [ZS-F5]."""
        assert G_MUB == 12

    def test_A_equals_delta_product(self):
        """A = δ_X · δ_Y (polyhedral invariant factorization)."""
        assert abs(DELTA_X * DELTA_Y - A_LOCKED) < 1e-15

    def test_delta_X(self):
        """δ_X = 5/19 (truncated octahedron)."""
        assert abs(DELTA_X - 5.0 / 19.0) < 1e-15

    def test_delta_Y(self):
        """δ_Y = 7/23 (truncated icosahedron)."""
        assert abs(DELTA_Y - 7.0 / 23.0) < 1e-15


# ─── Derived Constants ────────────────────────────────────────────────

class TestDerivedConstants:
    def test_kappa(self):
        assert abs(KAPPA - math.sqrt(A_LOCKED / Q_TOTAL)) < 1e-15

    def test_G_eff_ratio(self):
        assert abs(G_EFF_RATIO - 437.0 / 472.0) < 1e-12

    def test_H0_ratio(self):
        assert abs(H0_RATIO - math.exp(A_LOCKED)) < 1e-12

    def test_H_ZS_over_H_GR(self):
        assert abs(H_ZS_OVER_H_GR - 1.0 / math.sqrt(1.0 + A_LOCKED)) < 1e-12

    def test_lambda_potential(self):
        assert LAMBDA_POTENTIAL == 1.79

    def test_m_epsilon(self):
        assert abs(M_EPSILON_OVER_MP - math.sqrt(1.79)) < 1e-12

    def test_tau_d(self):
        assert abs(TAU_D_OVER_TAU_PENROSE - 1.0 / A_LOCKED) < 1e-12


# ─── Cosmological Predictions ─────────────────────────────────────────

class TestPredictions:
    def test_omega_m_eff(self):
        """Omega_m^eff = 38/(121(1+A)) = 0.2908 (face counting, v6.1; was 39/121)."""
        expected = 38.0 / (121.0 * (1.0 + A_LOCKED))
        assert abs(OMEGA_M_EFF - expected) < 1e-12

    def test_omega_m_bare(self):
        """Omega_m^bare = 38/121 = 0.3140 (face counting, v6.1; was 39/121)."""
        from zsim.core.constants import OMEGA_M_BARE
        assert abs(OMEGA_M_BARE - 38.0 / 121.0) < 1e-12

    def test_omega_b(self):
        assert abs(OMEGA_B - 6.0 / 121.0) < 1e-12

    def test_eta_B(self):
        """η_B = (6/11)^35 — baryon asymmetry [ZS-M5]."""
        expected = (6.0 / 11.0) ** 35
        assert abs(ETA_B - expected) < 1e-20

    def test_n_s_values(self):
        assert abs(N_S_60 - (1.0 - 2.0 / 60.0)) < 1e-12
        assert abs(N_S_55 - (1.0 - 2.0 / 55.0)) < 1e-12

    def test_r_tensor(self):
        assert R_TENSOR == 0.0089


# ─── i-Tetration Fixed Point ──────────────────────────────────────────

class TestITetration:
    def test_z_star_mod_sq(self):
        expected = X_STAR ** 2 + Z_STAR_IM ** 2
        assert abs(Z_STAR_MOD_SQ - expected) < 1e-15

    def test_z_star_values_reasonable(self):
        """z* ≈ 0.438 + 0.361i (W(−ln i)/(−ln i))."""
        assert 0.43 < X_STAR < 0.44
        assert 0.35 < Z_STAR_IM < 0.37


# ─── Derived YAML Config ─────────────────────────────────────────────

class TestDerivedConfig:
    def test_derived_yaml_loads(self):
        cfg = ZSimConfig.from_yaml("configs/derived.yaml")
        assert cfg.model.A == 35 / 437

    def test_derived_closure_params(self):
        cfg = ZSimConfig.from_yaml("configs/derived.yaml")
        # gamma_xz = 2A/Q [DERIVED]
        expected_gamma_xz = 2 * A_LOCKED / Q_TOTAL
        assert abs(cfg.closure.gamma_xz - expected_gamma_xz) < 1e-5
        # gamma_zy = 6A/Q [DERIVED]
        expected_gamma_zy = 6 * A_LOCKED / Q_TOTAL
        assert abs(cfg.closure.gamma_zy - expected_gamma_zy) < 1e-5
        # alpha_xz = dim(X)/dim(Z) = 3/2 [DERIVED]
        assert cfg.closure.alpha_xz == 1.5
        # alpha_zy = dim(Z)/dim(Y) = 1/3 [DERIVED]
        assert abs(cfg.closure.alpha_zy - 1.0 / 3.0) < 1e-5

    def test_derived_initial_equipartition(self):
        cfg = ZSimConfig.from_yaml("configs/derived.yaml")
        assert abs(cfg.initial.rho_x0 - 3.0 / 11.0) < 1e-5
        assert abs(cfg.initial.rho_z0 - 2.0 / 11.0) < 1e-5
        assert abs(cfg.initial.rho_y0 - 6.0 / 11.0) < 1e-5
        # Sum = 1
        total = cfg.initial.rho_x0 + cfg.initial.rho_z0 + cfg.initial.rho_y0
        assert abs(total - 1.0) < 1e-10

    def test_derived_phase_mode_spinor(self):
        cfg = ZSimConfig.from_yaml("configs/derived.yaml")
        assert cfg.closure.phase_mode == "spinor_sin2"

    def test_derived_lam(self):
        cfg = ZSimConfig.from_yaml("configs/derived.yaml")
        assert cfg.closure.lam == 1.79

    def test_spinor_sin2_phase_gate(self):
        """sin²(φ/2) — SU(2) j=1/2 Wigner d-matrix transition probability."""
        from zsim.kernel.phase import phase_gate
        import math

        assert phase_gate(0.0, "spinor_sin2") == 0.0
        assert abs(phase_gate(math.pi, "spinor_sin2") - 1.0) < 1e-12
        assert abs(phase_gate(math.pi / 2, "spinor_sin2") - 0.5) < 1e-12
        for phi in [0.1, 0.5, 1.0, 2.0, 5.0, -1.0, -3.0]:
            val = phase_gate(phi, "spinor_sin2")
            assert 0.0 <= val <= 1.0


# ─── Tier System Tests (v3.1 Fix #4) ─────────────────────────────────

class TestConstantTiers:
    """Verify the 3-tier constant hierarchy is correctly structured."""

    def test_omega_m_bare_vs_eff_distinction(self):
        """OMEGA_M_BARE != OMEGA_M_EFF — this was the v3.0 bug. v6.1: face counting."""
        from zsim.core.constants import OMEGA_M_BARE, OMEGA_M_EFF
        assert abs(OMEGA_M_BARE - 38.0 / 121.0) < 1e-12
        assert abs(OMEGA_M_EFF - 38.0 / (121.0 * (1.0 + A_LOCKED))) < 1e-12
        assert OMEGA_M_BARE != OMEGA_M_EFF
        # v1.0 face counting value
        assert abs(OMEGA_M_EFF - 0.290762) < 1e-4

    def test_omega_b_bare_vs_eff(self):
        from zsim.core.constants import OMEGA_B_BARE, OMEGA_B_EFF, G_EFF_RATIO
        assert abs(OMEGA_B_EFF - OMEGA_B_BARE * G_EFF_RATIO) < 1e-15

    def test_bench_predictions_are_approximate(self):
        """Tier 2 benchmarks are leading-order approximations."""
        from zsim.core.constants import BENCH_NS_60, BENCH_R_TENSOR
        # These are reference values, not exact
        assert abs(BENCH_NS_60 - 0.9667) < 0.001
        assert BENCH_R_TENSOR == 0.0089

    def test_planck_reference_values(self):
        from zsim.core.constants import PLANCK_OMEGA_M, PLANCK_H0, PLANCK_NS
        assert abs(PLANCK_OMEGA_M - 0.3153) < 0.001
        assert abs(PLANCK_H0 - 67.36) < 0.1
        assert abs(PLANCK_NS - 0.9649) < 0.001
