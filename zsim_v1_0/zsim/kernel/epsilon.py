"""Reduced order-parameter dynamics for Z-Sim v1.0.

This module provides a deliberately lightweight epsilon-sector closure. The
functions here are engineering translations for the v0.1 simulator rather than
claims of a unique final microscopic dynamics.
"""

from __future__ import annotations

from dataclasses import dataclass

from zsim.core import ConfigValidationError, ZSimConfig, ZSimState

from .phase import phase_gate

_H2_FLOOR = 1.0e-12


@dataclass(frozen=True, slots=True)
class EpsilonDerivatives:
    depsilon_dN: float
    dpi_epsilon_dN: float


def epsilon_potential(epsilon: float, config: ZSimConfig) -> float:
    mode = config.closure.epsilon_potential
    if mode == "quartic":
        return 0.25 * (epsilon * epsilon - 1.0) ** 2
    if mode == "quadratic":
        return 0.5 * epsilon * epsilon
    if mode == "flat_test":
        return 0.0
    raise ConfigValidationError(f"Unsupported closure.epsilon_potential: {mode!r}.")


def dV_depsilon(epsilon: float, config: ZSimConfig) -> float:
    mode = config.closure.epsilon_potential
    if mode == "quartic":
        return epsilon * (epsilon * epsilon - 1.0)
    if mode == "quadratic":
        return epsilon
    if mode == "flat_test":
        return 0.0
    raise ConfigValidationError(f"Unsupported closure.epsilon_potential: {mode!r}.")


def compute_epsilon_source(state: ZSimState, config: ZSimConfig) -> float:
    delta = state.J_xz - state.J_zy
    gate = phase_gate(state.phi_z, mode=config.closure.phase_mode)
    mode = config.closure.epsilon_source_mode
    if mode == "gate_current_difference":
        return gate * delta
    if mode == "current_difference":
        return delta
    if mode == "gate_abs_difference":
        return gate * abs(delta)
    if mode == "zero":
        return 0.0
    raise ConfigValidationError(f"Unsupported closure.epsilon_source_mode: {mode!r}.")


def depsilon_dN(state: ZSimState, config: ZSimConfig) -> float:
    _ = config
    return state.pi_epsilon


def dpi_epsilon_dN(state: ZSimState, config: ZSimConfig) -> float:
    h2 = max(state.h * state.h, _H2_FLOOR)
    friction = 3.0 + abs(state.h)
    restoring = dV_depsilon(state.epsilon, config) / h2
    source = compute_epsilon_source(state, config)
    return -friction * state.pi_epsilon - restoring + source


def epsilon_rhs(state: ZSimState, config: ZSimConfig) -> EpsilonDerivatives:
    return EpsilonDerivatives(
        depsilon_dN=depsilon_dN(state, config),
        dpi_epsilon_dN=dpi_epsilon_dN(state, config),
    )


__all__ = [
    "EpsilonDerivatives",
    "compute_epsilon_source",
    "depsilon_dN",
    "dpi_epsilon_dN",
    "epsilon_potential",
    "dV_depsilon",
    "epsilon_rhs",
]
