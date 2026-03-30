"""Tests for the Z-Sim typed configuration layer."""

from __future__ import annotations

from pathlib import Path

import pytest

from zsim.core.config import (
    ClosureConfig,
    ConfigLoadError,
    ConfigValidationError,
    InitialConfig,
    ModelConfig,
    SolverConfig,
    ZSimConfig,
)
from zsim.core.constants import A_LOCKED
from zsim.core.state import ZSimState


REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_CONFIG = REPO_ROOT / "configs" / "base.yaml"


def test_model_config_accepts_locked_values() -> None:
    cfg = ModelConfig.from_mapping(
        {
            "A": "35/437",
            "dims": {"X": 3, "Z": 2, "Y": 6},
            "enforce_zero_xy": True,
            "enforce_rank2_xy": True,
        }
    )
    assert cfg.A == pytest.approx(A_LOCKED)
    assert cfg.dims == {"X": 3, "Z": 2, "Y": 6}


def test_model_config_rejects_mismatched_locked_a() -> None:
    with pytest.raises(ConfigValidationError):
        ModelConfig.from_mapping(
            {
                "A": "36/437",
                "dims": {"X": 3, "Z": 2, "Y": 6},
                "enforce_zero_xy": True,
                "enforce_rank2_xy": True,
            }
        )


def test_model_config_rejects_mismatched_dims() -> None:
    with pytest.raises(ConfigValidationError):
        ModelConfig.from_mapping(
            {
                "A": "35/437",
                "dims": {"X": 3, "Z": 3, "Y": 5},
                "enforce_zero_xy": True,
                "enforce_rank2_xy": True,
            }
        )


def test_closure_config_supplies_defaults() -> None:
    cfg = ClosureConfig.from_mapping({"wy": "1/3"})
    assert cfg.wy == pytest.approx(1.0 / 3.0)
    assert cfg.phase_mode == "bounded_sine"
    assert cfg.epsilon_potential == "quartic"


def test_solver_config_rejects_invalid_method() -> None:
    with pytest.raises(ConfigValidationError):
        SolverConfig.from_mapping({"method": "EULER"})


def test_initial_config_to_state() -> None:
    state = InitialConfig.from_mapping({}).to_state()
    assert isinstance(state, ZSimState)
    assert state.rho_total == pytest.approx(1.0)
    assert state.J_xz == 0.0
    assert state.J_zy == 0.0


def test_zsim_config_loads_base_yaml() -> None:
    cfg = ZSimConfig.from_yaml(BASE_CONFIG)
    assert cfg.model.A == pytest.approx(A_LOCKED)
    assert cfg.closure.phase_mode == "bounded_sine"
    assert cfg.solver.method == "RK45"
    assert cfg.make_initial_state().rho_total == pytest.approx(1.0)


def test_zsim_config_from_mapping_requires_model_section() -> None:
    with pytest.raises(ConfigValidationError):
        ZSimConfig.from_mapping({"closure": {"wx": 0.0}})


def test_from_yaml_missing_file_raises() -> None:
    with pytest.raises(ConfigLoadError):
        ZSimConfig.from_yaml(REPO_ROOT / "configs" / "missing.yaml")
