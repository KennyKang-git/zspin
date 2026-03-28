"""Tests for the modified Friedmann equation module (kernel/friedmann.py).

This is the SINGLE MOST IMPORTANT physics test in Z-Sim.
Without F(ε) = 1 + Aε², this is not a Z-Spin simulator.

Source: ZS-F1 §3, Paper 22 §2.1, Paper 24 §5.1
"""
import math
import pytest

from zsim.core import A_LOCKED, ZSimConfig, ZSimState
from zsim.core.constants import G_EFF_RATIO, LAMBDA_POTENTIAL
from zsim.kernel.friedmann import (
    F_epsilon,
    G_eff_over_G,
    MissingNonMinimalCoupling,
    V_epsilon,
    dV_depsilon,
    friedmann_h,
    friedmann_h_squared,
    verify_non_minimal_coupling,
)


# ─── Helpers ─────────────────────────────────────────────────────────

def _default_config() -> ZSimConfig:
    return ZSimConfig.from_yaml("configs/base.yaml")


def _attractor_state() -> ZSimState:
    """State at the attractor ε=1, π_ε=0 where V(1)=0."""
    return ZSimState(
        N=0, a=1, h=1, epsilon=1.0, pi_epsilon=0,
        rho_x=0.3, rho_z=0.02, rho_y=0.68,
        J_xz=0, J_zy=0, phi_z=0, sigma_struct=0,
    )


# ─── F(ε) = 1 + Aε² ─────────────────────────────────────────────────

class TestNonMinimalCoupling:
    def test_F_at_zero(self):
        assert F_epsilon(0.0) == 1.0

    def test_F_at_one(self):
        expected = 1.0 + A_LOCKED
        assert abs(F_epsilon(1.0) - expected) < 1e-15

    def test_F_at_large_epsilon(self):
        """F(ε) grows quadratically."""
        eps = 10.0
        expected = 1.0 + A_LOCKED * 100.0
        assert abs(F_epsilon(eps) - expected) < 1e-12

    def test_F_is_always_positive(self):
        for eps in [0.0, 0.1, 1.0, 5.0, 100.0]:
            assert F_epsilon(eps) > 0

    def test_G_eff_at_attractor(self):
        """G_eff/G = 1/(1+A) = 437/472 at ε=1."""
        ratio = G_eff_over_G(1.0)
        assert abs(ratio - G_EFF_RATIO) < 1e-12
        assert abs(ratio - 437.0 / 472.0) < 1e-12

    def test_G_eff_at_zero(self):
        assert G_eff_over_G(0.0) == 1.0


# ─── V(ε) = (λ/4)(ε²−1)² ────────────────────────────────────────────

class TestPotential:
    def test_V_at_attractor(self):
        """V(1) = 0 — the attractor is at the minimum."""
        assert V_epsilon(1.0) == 0.0

    def test_V_at_origin(self):
        """V(0) = λ/4."""
        expected = LAMBDA_POTENTIAL / 4.0
        assert abs(V_epsilon(0.0) - expected) < 1e-12

    def test_V_symmetric(self):
        """V(ε) = V(−ε) by construction (depends on ε²)."""
        for eps in [0.5, 1.5, 3.0]:
            assert abs(V_epsilon(eps) - V_epsilon(-eps)) < 1e-14

    def test_dV_at_attractor(self):
        """dV/dε = 0 at ε = ±1 (minima) and ε = 0 (maximum)."""
        assert abs(dV_depsilon(1.0)) < 1e-14
        assert abs(dV_depsilon(-1.0)) < 1e-14
        assert abs(dV_depsilon(0.0)) < 1e-14


# ─── Modified Friedmann Equation ─────────────────────────────────────

class TestFriedmannEquation:
    def test_h_squared_positive_at_attractor(self):
        """h² > 0 at the attractor with positive energy density."""
        cfg = _default_config()
        state = _attractor_state()
        h2 = friedmann_h_squared(state, cfg)
        assert h2 > 0

    def test_h_squared_includes_non_minimal_coupling(self):
        """h²(A) / h²(A=0) = 1/(1+A) at ε=1, π_ε=0."""
        from dataclasses import replace

        cfg = _default_config()
        state = _attractor_state()

        h2_real = friedmann_h_squared(state, cfg)

        model_zero = replace(cfg.model, A=0.0)
        cfg_zero = replace(cfg, model=model_zero)
        h2_zero = friedmann_h_squared(state, cfg_zero)

        ratio = h2_real / h2_zero
        expected = 1.0 / (1.0 + A_LOCKED)
        assert abs(ratio - expected) < 1e-6

    def test_friedmann_h_returns_sqrt(self):
        cfg = _default_config()
        state = _attractor_state()
        h = friedmann_h(state, cfg)
        h2 = friedmann_h_squared(state, cfg)
        assert abs(h - math.sqrt(h2)) < 1e-14

    def test_h_squared_at_zero_epsilon(self):
        """At ε=0, F(0)=1, V(0)=λ/4. Friedmann equation still works."""
        cfg = _default_config()
        state = _attractor_state()
        state = state.replace(epsilon=0.0)
        h2 = friedmann_h_squared(state, cfg)
        # Should be (ρ_tot + λ/4) / 3
        rho_tot = state.rho_total
        expected = (rho_tot + LAMBDA_POTENTIAL / 4.0) / 3.0
        assert abs(h2 - expected) < 1e-10


# ─── KS-6: Non-minimal coupling verification ─────────────────────────

class TestKS6:
    def test_verify_passes_for_nominal_config(self):
        cfg = _default_config()
        verify_non_minimal_coupling(cfg)  # should not raise

    def test_verify_runs_via_kill_switches(self):
        """KS-6 is integrated into the kill-switch framework."""
        from zsim.validation.kill_switches import ks_non_minimal_coupling
        cfg = _default_config()
        trigger = ks_non_minimal_coupling(cfg)
        assert trigger is None  # no trigger = PASS
