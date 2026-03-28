"""Invariant and preflight checks for Z-Sim v3.1."""

from __future__ import annotations

import numpy as np

from zsim.core import DIM_X, DIM_Y, DIM_Z, Q_TOTAL, ConfigValidationError, ZSimConfig, ZSimState
from zsim.kernel.operators import build_structural_operator, direct_xy_block



def validate_config(config: ZSimConfig) -> ZSimConfig:
    """Validate structural config assumptions used by v0.1 validation.

    This complements ``config.validate()`` with explicit partition checks tied to
    kill-switch semantics.
    """
    config.validate()
    dims = config.model.dims
    if dims != {"X": DIM_X, "Z": DIM_Z, "Y": DIM_Y}:
        raise ConfigValidationError(f"Unexpected sector dims: {dims!r}")
    if sum(dims.values()) != Q_TOTAL:
        raise ConfigValidationError("Sector dimensions do not sum to Q_TOTAL.")
    if not config.model.enforce_zero_xy:
        raise ConfigValidationError("v0.1 requires enforce_zero_xy = true.")
    if not config.model.enforce_rank2_xy:
        raise ConfigValidationError("v0.1 requires enforce_rank2_xy = true.")
    return config



def validate_initial_state(state: ZSimState, config: ZSimConfig) -> ZSimState:
    """Validate initial state and structural operator compatibility."""
    validate_config(config)
    state.validate()
    operator = build_structural_operator(config)
    if operator.shape != (Q_TOTAL, Q_TOTAL):
        raise ConfigValidationError(f"Structural operator must be {Q_TOTAL}x{Q_TOTAL}.")
    xy = direct_xy_block(operator)
    if not np.allclose(xy, 0.0):
        raise ConfigValidationError("Structural operator has a nonzero direct X-Y block.")
    return state



def partition_signature(config: ZSimConfig) -> tuple[int, int, int]:
    """Return the canonical partition signature encoded by the config."""
    dims = config.model.dims
    return (dims["X"], dims["Z"], dims["Y"])


__all__ = [
    "partition_signature",
    "validate_config",
    "validate_initial_state",
]
