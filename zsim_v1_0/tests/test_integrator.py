import math

import numpy as np
import pytest

from zsim.core import IntegrationError, ZSimConfig, ZSimState
from zsim.solver import (
    IntegrationResult,
    StepEvent,
    collect_step_events,
    event_negative_density,
    event_nonfinite_state,
    integrate,
    project_state,
)


@pytest.fixture()
def base_config() -> ZSimConfig:
    return ZSimConfig.from_yaml("configs/base.yaml")


@pytest.fixture()
def base_state() -> ZSimState:
    return ZSimState(
        N=-2.0,
        a=math.exp(-2.0),
        h=1.0,
        epsilon=1.0,
        pi_epsilon=0.0,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.0,
        J_zy=0.0,
        phi_z=4.5,
        sigma_struct=0.0,
    )


def test_project_state_wraps_phase_and_clamps_densities(base_config: ZSimConfig, base_state: ZSimState) -> None:
    dirty = base_state.replace(phi_z=4.5, rho_x=-1.0, rho_z=-0.5)
    projected = project_state(dirty, base_config)
    assert -math.pi <= projected.phi_z < math.pi
    assert projected.rho_x == pytest.approx(0.0)
    assert projected.rho_z == pytest.approx(0.0)



def test_event_helpers_detect_negative_and_nonfinite_state(base_state: ZSimState) -> None:
    neg_event = event_negative_density(base_state.replace(rho_y=-0.1))
    assert isinstance(neg_event, StepEvent)
    assert neg_event is not None and neg_event.name == "negative_density"

    bad_event = event_nonfinite_state(base_state.replace(h=float("nan")))
    assert isinstance(bad_event, StepEvent)
    assert bad_event is not None and bad_event.name == "nonfinite_state"



def test_collect_step_events_empty_for_nominal_state(base_config: ZSimConfig, base_state: ZSimState) -> None:
    assert collect_step_events(base_state, base_config) == []



def test_integrate_returns_result_object(base_config: ZSimConfig) -> None:
    result = integrate(base_config, N_end=base_config.initial.N0 + 0.1)
    assert isinstance(result, IntegrationResult)
    assert result.success is True
    assert result.step_count >= 1
    assert result.final_state.N == pytest.approx(base_config.initial.N0 + 0.1)
    assert len(result.states) == result.step_count + 1
    assert result.trajectory.shape[1] == len(result.final_state.VECTOR_FIELDS)



def test_integrate_monotone_N_values(base_config: ZSimConfig) -> None:
    result = integrate(base_config, N_end=base_config.initial.N0 + 0.15)
    assert all(b >= a for a, b in zip(result.N_values, result.N_values[1:]))
    assert result.N_values[0] == pytest.approx(base_config.initial.N0)
    assert result.N_values[-1] == pytest.approx(base_config.initial.N0 + 0.15)



def test_integrate_with_custom_initial_state(base_config: ZSimConfig, base_state: ZSimState) -> None:
    result = integrate(base_config, initial_state=base_state, N_end=base_state.N + 0.1)
    assert result.success is True
    assert result.N_values[0] == pytest.approx(base_state.N)
    assert result.final_state.N == pytest.approx(base_state.N + 0.1)



def test_integrate_rejects_reverse_time(base_config: ZSimConfig) -> None:
    with pytest.raises(IntegrationError):
        integrate(base_config, N_end=base_config.initial.N0 - 0.1)


def test_integrate_stops_on_kill_switch_nonphysical_initial_state(base_config: ZSimConfig, base_state: ZSimState) -> None:
    bad_state = base_state.replace(rho_x=-0.1)
    result = integrate(base_config, initial_state=bad_state, N_end=bad_state.N + 0.1)
    assert result.success is False
    assert any(evt.name == "ks-4" for evt in result.events)
