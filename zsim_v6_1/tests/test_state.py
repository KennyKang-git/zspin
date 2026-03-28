"""Tests for the canonical Z-Sim state model."""

from __future__ import annotations

import numpy as np
import pytest

from zsim.core.exceptions import StateSerializationError, StateValidationError
from zsim.core.state import STATE_VECTOR_FIELDS, ZSimState


@pytest.fixture()
def nominal_state() -> ZSimState:
    return ZSimState(
        N=-18.0,
        a=1.522997974e-8,
        h=1.0,
        epsilon=1.0,
        pi_epsilon=0.0,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.0,
        J_zy=0.0,
        phi_z=0.0,
        sigma_struct=0.0,
    )


def test_state_field_order_is_stable() -> None:
    assert STATE_VECTOR_FIELDS == (
        "N",
        "a",
        "h",
        "epsilon",
        "pi_epsilon",
        "rho_x",
        "rho_z",
        "rho_y",
        "J_xz",
        "J_zy",
        "phi_z",
        "sigma_struct",
    )


def test_state_to_dict_roundtrip(nominal_state: ZSimState) -> None:
    restored = ZSimState.from_dict(nominal_state.to_dict())
    assert restored == nominal_state


def test_state_to_array_roundtrip(nominal_state: ZSimState) -> None:
    arr = nominal_state.to_array()
    assert isinstance(arr, np.ndarray)
    assert arr.shape == (len(STATE_VECTOR_FIELDS),)
    restored = ZSimState.from_array(arr)
    assert restored == nominal_state


def test_state_replace_returns_new_instance(nominal_state: ZSimState) -> None:
    changed = nominal_state.replace(phi_z=0.25, J_xz=0.1)
    assert changed is not nominal_state
    assert changed.phi_z == pytest.approx(0.25)
    assert changed.J_xz == pytest.approx(0.1)
    assert nominal_state.phi_z == pytest.approx(0.0)
    assert nominal_state.J_xz == pytest.approx(0.0)


def test_state_density_fractions(nominal_state: ZSimState) -> None:
    assert nominal_state.rho_total == pytest.approx(1.0)
    assert nominal_state.omega_x == pytest.approx(0.30)
    assert nominal_state.omega_z == pytest.approx(0.02)
    assert nominal_state.omega_y == pytest.approx(0.68)


def test_validate_rejects_negative_density(nominal_state: ZSimState) -> None:
    bad = nominal_state.replace(rho_z=-1e-6)
    with pytest.raises(StateValidationError):
        bad.validate()


def test_validate_rejects_nonfinite_value(nominal_state: ZSimState) -> None:
    bad = nominal_state.replace(h=float("nan"))
    with pytest.raises(StateValidationError):
        bad.validate()


def test_from_dict_rejects_missing_or_extra_keys(nominal_state: ZSimState) -> None:
    payload = nominal_state.to_dict()
    payload.pop("phi_z")
    with pytest.raises(StateSerializationError):
        ZSimState.from_dict(payload)

    payload2 = nominal_state.to_dict()
    payload2["unexpected"] = 123.0
    with pytest.raises(StateSerializationError):
        ZSimState.from_dict(payload2)


def test_from_array_rejects_wrong_length() -> None:
    with pytest.raises(StateSerializationError):
        ZSimState.from_array(np.zeros(len(STATE_VECTOR_FIELDS) - 1))
