from __future__ import annotations

import math

import pytest

from zsim.core import ConfigValidationError, ZSimConfig, ZSimState
from zsim.kernel import compute_J_xz, compute_epsilon_source, dphi_dN, friedmann_like_h, mediation_contrast, phase_source_argument


@pytest.fixture()
def base_config() -> ZSimConfig:
    return ZSimConfig.from_yaml('configs/base.yaml')


@pytest.fixture()
def base_state() -> ZSimState:
    return ZSimState(
        N=-5.0,
        a=math.exp(-5.0),
        h=1.0,
        epsilon=1.2,
        pi_epsilon=0.4,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.2,
        J_zy=0.05,
        phi_z=0.3,
        sigma_struct=0.0,
    )


def test_closure_config_exposes_new_mode_defaults(base_config: ZSimConfig) -> None:
    assert base_config.closure.phase_source_mode == 'full_state'
    assert base_config.closure.mediation_mode == 'raw_contrast'
    assert base_config.closure.epsilon_source_mode == 'gate_current_difference'
    assert base_config.closure.h_closure_mode == 'sqrt_sum'


def test_replace_closure_updates_selected_modes(base_config: ZSimConfig) -> None:
    updated = base_config.replace_closure(phase_source_mode='currents_only', mediation_mode='normalized_contrast')
    assert updated.closure.phase_source_mode == 'currents_only'
    assert updated.closure.mediation_mode == 'normalized_contrast'


def test_phase_source_argument_modes_change_value(base_state: ZSimState) -> None:
    full_value = phase_source_argument(base_state, 'full_state')
    current_value = phase_source_argument(base_state, 'currents_only')
    epsilon_value = phase_source_argument(base_state, 'epsilon_mediator')
    assert full_value != pytest.approx(current_value)
    assert epsilon_value == pytest.approx(base_state.epsilon + base_state.rho_z)


def test_phase_source_argument_rejects_unknown_mode(base_state: ZSimState) -> None:
    with pytest.raises(ConfigValidationError):
        phase_source_argument(base_state, 'mystery')


def test_mediation_contrast_modes_are_distinct() -> None:
    raw = mediation_contrast(2.0, 1.0, 'raw_contrast')
    normalized = mediation_contrast(2.0, 1.0, 'normalized_contrast')
    tanh_value = mediation_contrast(2.0, 1.0, 'tanh_contrast')
    assert raw == pytest.approx(1.0)
    assert normalized == pytest.approx(1.0 / 3.0)
    assert 0.0 < tanh_value < 1.0


def test_dphi_dN_responds_to_phase_source_mode(base_config: ZSimConfig, base_state: ZSimState) -> None:
    full_cfg = base_config.replace_closure(phase_mode='bounded_tanh', phase_source_mode='full_state')
    current_cfg = base_config.replace_closure(phase_mode='bounded_tanh', phase_source_mode='currents_only')
    assert dphi_dN(base_state, full_cfg) != pytest.approx(dphi_dN(base_state, current_cfg))


def test_compute_J_xz_responds_to_mediation_mode(base_config: ZSimConfig, base_state: ZSimState) -> None:
    raw_cfg = base_config.replace_closure(phase_mode='constant', mediation_mode='raw_contrast')
    norm_cfg = base_config.replace_closure(phase_mode='constant', mediation_mode='normalized_contrast')
    assert compute_J_xz(base_state, raw_cfg) != pytest.approx(compute_J_xz(base_state, norm_cfg))


def test_compute_epsilon_source_modes(base_config: ZSimConfig, base_state: ZSimState) -> None:
    zero_cfg = base_config.replace_closure(epsilon_source_mode='zero')
    current_cfg = base_config.replace_closure(phase_mode='constant', epsilon_source_mode='current_difference')
    assert compute_epsilon_source(base_state, zero_cfg) == pytest.approx(0.0)
    assert compute_epsilon_source(base_state, current_cfg) == pytest.approx(base_state.J_xz - base_state.J_zy)


def test_friedmann_like_h_plus_epsilon_exceeds_sqrt_sum(base_config: ZSimConfig, base_state: ZSimState) -> None:
    base = friedmann_like_h(base_state, base_config.replace_closure(h_closure_mode='sqrt_sum'))
    enriched = friedmann_like_h(base_state, base_config.replace_closure(h_closure_mode='sqrt_sum_plus_epsilon'))
    assert enriched >= base
