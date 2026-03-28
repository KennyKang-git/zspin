"""Z-mediated current closures for Z-Sim v3.1.

This module implements the minimal mediation contract for the reduced engine:

- X -> Z current ``J_xz``
- Z -> Y current ``J_zy``
- no direct X -> Y current constructor
- pluggable translated mediation modes for closure experiments

Important
---------
The concrete current laws implemented here are **TRANSLATED** v0.1 closures.
They are intended to preserve the structural rule that all X↔Y exchange is
mediated through Z. They are not claimed to be the unique or final microscopic
form of the full theory.
"""

from __future__ import annotations

import math
from typing import Tuple

from zsim.core import ConfigValidationError, ZSimConfig, ZSimState

from .phase import phase_gate

_EPS = 1.0e-12


def mediation_contrast(left: float, right: float, mode: str = "raw_contrast") -> float:
    delta = float(left) - float(right)
    if mode == "raw_contrast":
        return delta
    if mode == "normalized_contrast":
        return delta / (abs(left) + abs(right) + _EPS)
    if mode == "tanh_contrast":
        return math.tanh(delta)
    raise ConfigValidationError(f"Unsupported mediation mode: {mode!r}.")


def compute_J_xz(state: ZSimState, config: ZSimConfig) -> float:
    gate = phase_gate(state.phi_z, mode=config.closure.phase_mode)
    contrast = mediation_contrast(
        state.rho_x,
        config.closure.alpha_xz * state.rho_z,
        mode=config.closure.mediation_mode,
    )
    return float(config.closure.gamma_xz * gate * contrast)


def compute_J_zy(state: ZSimState, config: ZSimConfig) -> float:
    gate = phase_gate(state.phi_z, mode=config.closure.phase_mode)
    contrast = mediation_contrast(
        state.rho_z,
        config.closure.alpha_zy * state.rho_y,
        mode=config.closure.mediation_mode,
    )
    return float(config.closure.gamma_zy * gate * contrast)


def compute_currents(state: ZSimState, config: ZSimConfig) -> Tuple[float, float]:
    return compute_J_xz(state, config), compute_J_zy(state, config)


__all__ = ["mediation_contrast", "compute_J_xz", "compute_J_zy", "compute_currents"]
