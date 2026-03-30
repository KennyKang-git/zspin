"""Background sector evolution helpers for Z-Sim v1.0.

This module implements the minimal reduced background closure for the X/Z/Y
sector budgets. The design goal is structural fidelity, not precision
cosmology.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from zsim.core import StateValidationError, ZSimConfig, ZSimState

from .epsilon import epsilon_potential


@dataclass(frozen=True, slots=True)
class BackgroundDerivatives:
    drho_x_dN: float
    drho_z_dN: float
    drho_y_dN: float


def drho_x_dN(state: ZSimState, config: ZSimConfig) -> float:
    state.validate()
    return float(-3.0 * (1.0 + config.closure.wx) * state.rho_x - state.J_xz)


def drho_z_dN(state: ZSimState, config: ZSimConfig) -> float:
    state.validate()
    return float(-3.0 * (1.0 + config.closure.wz) * state.rho_z + state.J_xz - state.J_zy)


def drho_y_dN(state: ZSimState, config: ZSimConfig) -> float:
    state.validate()
    return float(-3.0 * (1.0 + config.closure.wy) * state.rho_y + state.J_zy)


def compute_background_derivatives(state: ZSimState, config: ZSimConfig) -> BackgroundDerivatives:
    return BackgroundDerivatives(
        drho_x_dN=drho_x_dN(state, config),
        drho_z_dN=drho_z_dN(state, config),
        drho_y_dN=drho_y_dN(state, config),
    )


def friedmann_like_h(state: ZSimState, config: ZSimConfig) -> float:
    state.validate()
    total = state.rho_total
    if total < 0.0:
        raise StateValidationError("rho_total must be non-negative for the reduced Friedmann closure.")
    mode = config.closure.h_closure_mode
    if mode == "sqrt_sum":
        return float(math.sqrt(total))
    if mode == "sqrt_sum_plus_epsilon":
        epsilon_energy = 0.5 * state.pi_epsilon * state.pi_epsilon + epsilon_potential(state.epsilon, config)
        return float(math.sqrt(max(total + epsilon_energy, 0.0)))
    if mode == "friedmann_full":
        from .friedmann import friedmann_h
        return friedmann_h(state, config)
    raise StateValidationError(f"Unsupported h closure mode: {mode!r}.")


__all__ = [
    "BackgroundDerivatives",
    "drho_x_dN",
    "drho_z_dN",
    "drho_y_dN",
    "compute_background_derivatives",
    "friedmann_like_h",
]
