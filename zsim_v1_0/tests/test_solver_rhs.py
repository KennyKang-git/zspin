import math

import numpy as np
import pytest

from zsim.core import ZSimConfig, ZSimState, STATE_VECTOR_FIELDS
from zsim.kernel import compute_currents, friedmann_like_h
from zsim.solver import RHSDerivatives, close_state, evaluate_rhs, rhs, sigma_struct_source, state_from_ode_vector


@pytest.fixture()
def base_config() -> ZSimConfig:
    return ZSimConfig.from_yaml("configs/base.yaml")


@pytest.fixture()
def base_state() -> ZSimState:
    return ZSimState(
        N=-5.0,
        a=math.exp(-5.0),
        h=0.8,
        epsilon=1.0,
        pi_epsilon=0.1,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.0,
        J_zy=0.0,
        phi_z=0.3,
        sigma_struct=0.0,
    )


def test_state_from_ode_vector_overrides_N(base_state: ZSimState, base_config: ZSimConfig) -> None:
    array = base_state.to_array()
    rebuilt = state_from_ode_vector(-2.0, array, base_config)
    assert rebuilt.N == pytest.approx(-2.0)
    assert rebuilt.a == pytest.approx(base_state.a)



def test_close_state_inserts_kernel_currents_and_h(base_state: ZSimState, base_config: ZSimConfig) -> None:
    closed = close_state(base_state, base_config.replace_phase_mode("constant"))
    j_xz, j_zy = compute_currents(base_state, base_config.replace_phase_mode("constant"))
    assert closed.J_xz == pytest.approx(j_xz)
    assert closed.J_zy == pytest.approx(j_zy)
    assert closed.h == pytest.approx(friedmann_like_h(closed, base_config))



def test_sigma_struct_source_is_nonnegative(base_state: ZSimState, base_config: ZSimConfig) -> None:
    closed = close_state(base_state, base_config.replace_phase_mode("constant"))
    assert sigma_struct_source(closed, base_config) >= 0.0



def test_evaluate_rhs_returns_typed_bundle(base_state: ZSimState, base_config: ZSimConfig) -> None:
    result = evaluate_rhs(base_state, base_config.replace_phase_mode("constant"))
    assert isinstance(result, RHSDerivatives)
    assert result.dN_dN == pytest.approx(1.0)
    assert result.da_dN == pytest.approx(base_state.a)



def test_evaluate_rhs_relaxes_h_and_currents_toward_closed_values(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    closed = close_state(base_state, config)
    derivs = evaluate_rhs(base_state, config)
    assert derivs.dh_dN == pytest.approx(closed.h - base_state.h)
    assert derivs.dJ_xz_dN == pytest.approx(closed.J_xz - base_state.J_xz)
    assert derivs.dJ_zy_dN == pytest.approx(closed.J_zy - base_state.J_zy)



def test_rhs_returns_canonical_length_vector(base_state: ZSimState, base_config: ZSimConfig) -> None:
    vector = rhs(base_state.N, base_state.to_array(), base_config.replace_phase_mode("constant"))
    assert isinstance(vector, np.ndarray)
    assert vector.shape == (len(STATE_VECTOR_FIELDS),)



def test_rhs_background_entries_match_closed_state_background(base_state: ZSimState, base_config: ZSimConfig) -> None:
    config = base_config.replace_phase_mode("constant")
    derivs = evaluate_rhs(base_state, config)
    closed = close_state(base_state, config)
    j_xz, j_zy = closed.J_xz, closed.J_zy
    expected_x = -3.0 * (1.0 + config.closure.wx) * closed.rho_x - j_xz
    expected_z = -3.0 * (1.0 + config.closure.wz) * closed.rho_z + j_xz - j_zy
    expected_y = -3.0 * (1.0 + config.closure.wy) * closed.rho_y + j_zy
    assert derivs.drho_x_dN == pytest.approx(expected_x)
    assert derivs.drho_z_dN == pytest.approx(expected_z)
    assert derivs.drho_y_dN == pytest.approx(expected_y)



def test_rhs_array_order_matches_state_contract(base_state: ZSimState, base_config: ZSimConfig) -> None:
    arr = rhs(base_state.N, base_state.to_array(), base_config.replace_phase_mode("constant"))
    assert arr[0] == pytest.approx(1.0)
    assert arr[1] == pytest.approx(base_state.a)
