"""Phase / holonomy helpers for Z-Sim v1.0.

This module provides the minimal phase-layer contract needed by the reduced
engine:

- a bounded routing gate ``phase_gate(phi_z, mode)``
- translated phase-source hooks ``phase_source_argument(state, source_mode)``
- a translated v0.1 phase evolution closure ``dphi_dN(state, config)``
- optional phase wrapping for stable downstream use

Important
---------
The concrete evolution closure implemented here is a **TRANSLATED** software
choice for v0.1. It is not presented as a final or unique derivation of the
full Z-sector phase dynamics.
"""

from __future__ import annotations

import math

from zsim.core import ConfigValidationError, ZSimConfig, ZSimState

_TWO_PI = 2.0 * math.pi


def wrap_phase(phi_z: float) -> float:
    wrapped = (float(phi_z) + math.pi) % _TWO_PI - math.pi
    return -math.pi if math.isclose(wrapped, math.pi) else wrapped


def phase_gate(phi_z: float, mode: str = "bounded_sine") -> float:
    """Compute the phase gate Π_Z(φ_Z).

    Modes:
      bounded_sine  — sin(φ)           [HYPOTHESIS, v0.1 default]
      bounded_tanh  — tanh(φ)          [HYPOTHESIS]
      constant      — 1.0              [diagnostic]
      spinor_sin2   — sin²(φ/2)        [DERIVED: SU(2) j=1/2 Wigner d-matrix,
                                         ZS-M3 Thm 5.1, Lemma 10.1]
    """
    phi = float(phi_z)
    if mode == "bounded_sine":
        return math.sin(phi)
    if mode == "bounded_tanh":
        return math.tanh(phi)
    if mode == "constant":
        return 1.0
    if mode == "spinor_sin2":
        # Transition probability |d^{1/2}_{-,+}(φ)|² = sin²(φ/2)
        # Source: ZS-M3 §2 Theorem 5.1 (j=1/2 uniqueness, PROVEN)
        s = math.sin(phi / 2.0)
        return s * s
    raise ConfigValidationError(f"Unsupported phase mode: {mode!r}.")


def phase_source_argument(state: ZSimState, source_mode: str = "full_state") -> float:
    if source_mode == "full_state":
        return state.phi_z + state.epsilon + state.rho_z + (state.J_xz - state.J_zy)
    if source_mode == "currents_only":
        return state.J_xz - state.J_zy
    if source_mode == "epsilon_mediator":
        return state.epsilon + state.rho_z
    if source_mode == "phase_feedback_only":
        return state.phi_z
    raise ConfigValidationError(f"Unsupported phase source mode: {source_mode!r}.")


def dphi_dN(state: ZSimState, config: ZSimConfig) -> float:
    mode = config.closure.phase_mode
    arg = phase_source_argument(state, config.closure.phase_source_mode)
    if mode == "constant":
        return 0.0
    if mode == "bounded_sine":
        return math.sin(arg)
    if mode == "bounded_tanh":
        return math.tanh(arg)
    if mode == "spinor_sin2":
        # Phase evolution under SU(2) j=1/2 holonomy
        # dφ/dN = sin²(arg/2) — bounded in [0,1], monotone accumulation
        s = math.sin(arg / 2.0)
        return s * s
    raise ConfigValidationError(f"Unsupported phase mode: {mode!r}.")


__all__ = ["wrap_phase", "phase_gate", "phase_source_argument", "dphi_dN"]
