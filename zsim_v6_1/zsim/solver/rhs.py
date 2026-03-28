"""Reduced RHS assembly for Z-Sim v3.1.

This module glues together the v0.1 kernel pieces into the single contract that
an ODE solver expects:

    state vector -> derivative vector

Design notes
------------
- The integration variable is ``N = ln(a)``.
- ``J_xz``, ``J_zy``, and ``h`` are treated as closure-tracked state fields.
  Their derivatives relax the stored state toward the values implied by the
  reduced structural kernel.
- No direct X↔Y term is introduced anywhere in this assembly layer.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.core import ZSimConfig, ZSimState
from zsim.kernel import (
    compute_background_derivatives,
    compute_currents,
    dphi_dN,
    epsilon_rhs,
    friedmann_like_h,
)


@dataclass(frozen=True, slots=True)
class RHSDerivatives:
    """Typed derivative bundle in canonical state order."""

    dN_dN: float
    da_dN: float
    dh_dN: float
    depsilon_dN: float
    dpi_epsilon_dN: float
    drho_x_dN: float
    drho_z_dN: float
    drho_y_dN: float
    dJ_xz_dN: float
    dJ_zy_dN: float
    dphi_z_dN: float
    dsigma_struct_dN: float

    def to_array(self, *, dtype: type[float] = float) -> np.ndarray:
        return np.asarray(
            [
                self.dN_dN,
                self.da_dN,
                self.dh_dN,
                self.depsilon_dN,
                self.dpi_epsilon_dN,
                self.drho_x_dN,
                self.drho_z_dN,
                self.drho_y_dN,
                self.dJ_xz_dN,
                self.dJ_zy_dN,
                self.dphi_z_dN,
                self.dsigma_struct_dN,
            ],
            dtype=dtype,
        )


def state_from_ode_vector(N: float, y: np.ndarray | list[float], config: ZSimConfig) -> ZSimState:
    """Reconstruct a :class:`ZSimState` from solver inputs.

    The external ODE integrator controls the independent variable ``N``.
    We therefore always overwrite the state's stored ``N`` field with the value
    provided by the solver call, regardless of what is inside ``y``.
    """
    del config  # reserved for future reconstruction policies
    state = ZSimState.from_array(y)
    return state.replace(N=float(N))


def close_state(state: ZSimState, config: ZSimConfig) -> ZSimState:
    """Return a closure-consistent helper state.

    The returned state has currents and H-like value replaced by the values
    implied by the reduced v0.1 kernel. The original input state is not
    modified.
    """
    target_J_xz, target_J_zy = compute_currents(state, config)
    closed = state.replace(J_xz=target_J_xz, J_zy=target_J_zy)
    target_h = friedmann_like_h(closed, config)
    return closed.replace(h=target_h)


def sigma_struct_source(closed_state: ZSimState, config: ZSimConfig) -> float:
    """Return the reduced structural-arrow source term.

    v0.1 keeps this intentionally small and monotone:

    ``d sigma_struct / dN = |J_xz| + |J_zy|``

    This is a translated engineering diagnostic, not a final microscopic claim.
    """
    del config
    return abs(closed_state.J_xz) + abs(closed_state.J_zy)


def evaluate_rhs(state: ZSimState, config: ZSimConfig) -> RHSDerivatives:
    """Evaluate the reduced ODE right-hand side for a validated state."""
    state.validate()

    closed = close_state(state, config)
    background = compute_background_derivatives(closed, config)
    eps = epsilon_rhs(closed, config)

    target_J_xz = closed.J_xz
    target_J_zy = closed.J_zy
    target_h = closed.h

    return RHSDerivatives(
        dN_dN=1.0,
        da_dN=state.a,
        dh_dN=target_h - state.h,
        depsilon_dN=eps.depsilon_dN,
        dpi_epsilon_dN=eps.dpi_epsilon_dN,
        drho_x_dN=background.drho_x_dN,
        drho_z_dN=background.drho_z_dN,
        drho_y_dN=background.drho_y_dN,
        dJ_xz_dN=target_J_xz - state.J_xz,
        dJ_zy_dN=target_J_zy - state.J_zy,
        dphi_z_dN=dphi_dN(closed, config),
        dsigma_struct_dN=sigma_struct_source(closed, config),
    )


def rhs(N: float, y: np.ndarray | list[float], config: ZSimConfig) -> np.ndarray:
    """Assemble the solver-ready derivative vector.

    Parameters
    ----------
    N:
        Current value of the independent variable ``ln(a)``.
    y:
        Current state vector in canonical order.
    config:
        Validated runtime configuration.
    """
    state = state_from_ode_vector(N, y, config)
    return evaluate_rhs(state, config).to_array(dtype=float)


__all__ = [
    "RHSDerivatives",
    "close_state",
    "evaluate_rhs",
    "rhs",
    "sigma_struct_source",
    "state_from_ode_vector",
]
