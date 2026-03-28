import math

import pytest

from zsim.core import ZSimConfig, ZSimState, ConfigValidationError
from zsim.kernel import compute_J_xz, compute_J_zy, compute_currents, dphi_dN, phase_gate, wrap_phase


@pytest.fixture()
def base_state() -> ZSimState:
    return ZSimState(
        N=-5.0,
        a=math.exp(-5.0),
        h=1.0,
        epsilon=1.0,
        pi_epsilon=0.0,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.1,
        J_zy=0.05,
        phi_z=0.3,
        sigma_struct=0.0,
    )


@pytest.fixture()
def base_config() -> ZSimConfig:
    return ZSimConfig.from_yaml("configs/base.yaml")


@pytest.mark.parametrize(
    ("mode", "phi_z", "expected"),
    [
        ("bounded_sine", 0.0, 0.0),
        ("bounded_sine", math.pi / 2.0, 1.0),
        ("bounded_tanh", 0.0, 0.0),
        ("constant", 123.456, 1.0),
    ],
)
def test_phase_gate_modes(mode: str, phi_z: float, expected: float) -> None:
    value = phase_gate(phi_z, mode=mode)
    assert value == pytest.approx(expected)


@pytest.mark.parametrize("phi_z", [-100.0, -1.0, 0.0, 1.0, 100.0])
def test_phase_gate_dynamic_modes_are_bounded(phi_z: float) -> None:
    for mode in ("bounded_sine", "bounded_tanh"):
        value = phase_gate(phi_z, mode=mode)
        assert -1.0 <= value <= 1.0



def test_phase_gate_rejects_unknown_mode() -> None:
    with pytest.raises(ConfigValidationError):
        phase_gate(0.0, mode="mystery")


@pytest.mark.parametrize("raw", [-10 * math.pi, -3.4, 0.0, 3.2, 9 * math.pi])
def test_wrap_phase_maps_into_half_open_interval(raw: float) -> None:
    wrapped = wrap_phase(raw)
    assert -math.pi <= wrapped < math.pi



def test_dphi_dN_uses_zero_for_constant_mode(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    assert dphi_dN(base_state, config) == pytest.approx(0.0)


@pytest.mark.parametrize("mode", ["bounded_sine", "bounded_tanh"])
def test_dphi_dN_dynamic_modes_are_bounded(mode: str, base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode(mode)
    value = dphi_dN(base_state, config)
    assert -1.0 <= value <= 1.0



def test_dphi_dN_changes_when_currents_change(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("bounded_tanh")
    value_1 = dphi_dN(base_state, config)
    shifted = base_state.replace(J_xz=0.4, J_zy=0.0)
    value_2 = dphi_dN(shifted, config)
    assert value_1 != pytest.approx(value_2)


@pytest.mark.parametrize("mode", ["bounded_sine", "bounded_tanh", "constant"])
def test_compute_currents_matches_individual_components(
    mode: str, base_state: ZSimState, base_config: ZSimConfig
) -> None:
    config = base_config.replace_phase_mode(mode)
    j_xz, j_zy = compute_currents(base_state, config)
    assert j_xz == pytest.approx(compute_J_xz(base_state, config))
    assert j_zy == pytest.approx(compute_J_zy(base_state, config))



def test_mediation_currents_follow_default_closure(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    expected_xz = config.closure.gamma_xz * (base_state.rho_x - config.closure.alpha_xz * base_state.rho_z)
    expected_zy = config.closure.gamma_zy * (base_state.rho_z - config.closure.alpha_zy * base_state.rho_y)
    assert compute_J_xz(base_state, config) == pytest.approx(expected_xz)
    assert compute_J_zy(base_state, config) == pytest.approx(expected_zy)



def test_mediation_currents_vanish_when_gate_is_zero(base_state: ZSimState, base_config: ZSimConfig) -> None:
    state = base_state.replace(phi_z=0.0)
    config = base_config.replace_phase_mode("bounded_sine")
    j_xz, j_zy = compute_currents(state, config)
    assert j_xz == pytest.approx(0.0)
    assert j_zy == pytest.approx(0.0)



def test_mediation_currents_change_sign_with_sector_contrast(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    positive = base_state.replace(rho_x=1.0, rho_z=0.1, rho_y=0.0)
    negative = base_state.replace(rho_x=0.0, rho_z=1.0, rho_y=2.0)
    assert compute_J_xz(positive, config) > 0.0
    assert compute_J_xz(negative, config) < 0.0
    assert compute_J_zy(positive, config) > 0.0
    assert compute_J_zy(negative, config) < 0.0



def test_kernel_exports_no_direct_j_xy_symbol() -> None:
    import zsim.kernel as kernel

    assert not hasattr(kernel, "compute_J_xy")
    assert not hasattr(kernel, "J_xy")


from zsim.kernel import BackgroundDerivatives, compute_background_derivatives, drho_x_dN, drho_y_dN, drho_z_dN, friedmann_like_h


def test_background_derivatives_follow_default_closure(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    j_xz, j_zy = compute_currents(base_state, config)
    state = base_state.replace(J_xz=j_xz, J_zy=j_zy)

    expected_x = -3.0 * (1.0 + config.closure.wx) * state.rho_x - state.J_xz
    expected_z = -3.0 * (1.0 + config.closure.wz) * state.rho_z + state.J_xz - state.J_zy
    expected_y = -3.0 * (1.0 + config.closure.wy) * state.rho_y + state.J_zy

    assert drho_x_dN(state, config) == pytest.approx(expected_x)
    assert drho_z_dN(state, config) == pytest.approx(expected_z)
    assert drho_y_dN(state, config) == pytest.approx(expected_y)



def test_compute_background_derivatives_returns_dataclass(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    j_xz, j_zy = compute_currents(base_state, config)
    state = base_state.replace(J_xz=j_xz, J_zy=j_zy)
    result = compute_background_derivatives(state, config)
    assert isinstance(result, BackgroundDerivatives)
    assert result.drho_x_dN == pytest.approx(drho_x_dN(state, config))
    assert result.drho_z_dN == pytest.approx(drho_z_dN(state, config))
    assert result.drho_y_dN == pytest.approx(drho_y_dN(state, config))



def test_friedmann_like_h_matches_sqrt_total_density(base_state: ZSimState, base_config: ZSimConfig) -> None:
    state = base_state.replace(rho_x=0.25, rho_z=0.25, rho_y=0.50)
    assert friedmann_like_h(state, base_config) == pytest.approx(1.0)



def test_friedmann_like_h_tracks_changed_sector_budget(base_state: ZSimState, base_config: ZSimConfig) -> None:
    state = base_state.replace(rho_x=0.16, rho_z=0.09, rho_y=0.00)
    assert friedmann_like_h(state, base_config) == pytest.approx(0.5)



def test_kernel_exports_background_symbols() -> None:
    import zsim.kernel as kernel

    assert hasattr(kernel, "drho_x_dN")
    assert hasattr(kernel, "drho_z_dN")
    assert hasattr(kernel, "drho_y_dN")
    assert hasattr(kernel, "friedmann_like_h")

from zsim.kernel import (
    EpsilonDerivatives,
    compute_epsilon_source,
    depsilon_dN,
    dpi_epsilon_dN,
    dV_depsilon,
    epsilon_potential,
    epsilon_rhs,
)


def test_quartic_epsilon_potential_has_minimum_at_one(base_config: ZSimConfig) -> None:
    assert epsilon_potential(1.0, base_config) == pytest.approx(0.0)
    assert dV_depsilon(1.0, base_config) == pytest.approx(0.0)



def test_quadratic_epsilon_potential_matches_expected_form(base_config: ZSimConfig) -> None:
    config = ZSimConfig(
        model=base_config.model,
        closure=base_config.closure.__class__(
            wx=base_config.closure.wx,
            wz=base_config.closure.wz,
            wy=base_config.closure.wy,
            gamma_xz=base_config.closure.gamma_xz,
            gamma_zy=base_config.closure.gamma_zy,
            alpha_xz=base_config.closure.alpha_xz,
            alpha_zy=base_config.closure.alpha_zy,
            phase_mode=base_config.closure.phase_mode,
            epsilon_potential="quadratic",
        ),
        initial=base_config.initial,
        solver=base_config.solver,
        outputs=base_config.outputs,
    )
    assert epsilon_potential(2.0, config) == pytest.approx(2.0)
    assert dV_depsilon(2.0, config) == pytest.approx(2.0)



def test_flat_test_potential_is_identically_zero(base_config: ZSimConfig) -> None:
    config = ZSimConfig(
        model=base_config.model,
        closure=base_config.closure.__class__(
            wx=base_config.closure.wx,
            wz=base_config.closure.wz,
            wy=base_config.closure.wy,
            gamma_xz=base_config.closure.gamma_xz,
            gamma_zy=base_config.closure.gamma_zy,
            alpha_xz=base_config.closure.alpha_xz,
            alpha_zy=base_config.closure.alpha_zy,
            phase_mode=base_config.closure.phase_mode,
            epsilon_potential="flat_test",
        ),
        initial=base_config.initial,
        solver=base_config.solver,
        outputs=base_config.outputs,
    )
    assert epsilon_potential(-99.0, config) == pytest.approx(0.0)
    assert dV_depsilon(-99.0, config) == pytest.approx(0.0)



def test_compute_epsilon_source_uses_phase_gate_and_current_difference(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    state = base_state.replace(J_xz=0.25, J_zy=0.10)
    assert compute_epsilon_source(state, config) == pytest.approx(0.15)



def test_compute_epsilon_source_vanishes_when_sine_gate_is_zero(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("bounded_sine")
    state = base_state.replace(phi_z=0.0, J_xz=10.0, J_zy=-5.0)
    assert compute_epsilon_source(state, config) == pytest.approx(0.0)



def test_depsilon_dN_equals_pi_epsilon(base_state: ZSimState, base_config: ZSimConfig) -> None:
    state = base_state.replace(pi_epsilon=0.375)
    assert depsilon_dN(state, base_config) == pytest.approx(0.375)



def test_dpi_epsilon_dN_matches_reduced_closure(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    state = base_state.replace(h=2.0, epsilon=1.5, pi_epsilon=0.2, J_xz=0.3, J_zy=0.1)
    expected = -(3.0 + abs(state.h)) * state.pi_epsilon - dV_depsilon(state.epsilon, config) / (state.h * state.h) + (state.J_xz - state.J_zy)
    assert dpi_epsilon_dN(state, config) == pytest.approx(expected)



def test_epsilon_rhs_returns_dataclass_bundle(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    state = base_state.replace(J_xz=0.2, J_zy=0.05)
    result = epsilon_rhs(state, config)
    assert isinstance(result, EpsilonDerivatives)
    assert result.depsilon_dN == pytest.approx(depsilon_dN(state, config))
    assert result.dpi_epsilon_dN == pytest.approx(dpi_epsilon_dN(state, config))



def test_kernel_exports_epsilon_symbols() -> None:
    import zsim.kernel as kernel

    assert hasattr(kernel, "epsilon_potential")
    assert hasattr(kernel, "dV_depsilon")
    assert hasattr(kernel, "epsilon_rhs")
