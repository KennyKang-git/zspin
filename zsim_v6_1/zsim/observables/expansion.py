"""Expansion-side observables for Z-Sim v3.1."""

from __future__ import annotations

from dataclasses import dataclass

from zsim.core import ZSimConfig, ZSimState


@dataclass(frozen=True, slots=True)
class ExpansionObservables:
    """Reduced expansion observables compiled from a single state."""

    H_like: float
    w_eff: float

    def to_dict(self) -> dict[str, float]:
        return {"H_like": float(self.H_like), "w_eff": float(self.w_eff)}



def effective_w(state: ZSimState, config: ZSimConfig) -> float:
    """Return a reduced effective equation-of-state parameter.

    The v0.1 closure uses a density-weighted average of the closure-side sector
    equation-of-state parameters.
    """

    rho_total = state.rho_total
    if rho_total == 0.0:
        return 0.0
    c = config.closure
    weighted = c.wx * state.rho_x + c.wz * state.rho_z + c.wy * state.rho_y
    return weighted / rho_total



def H_like(state: ZSimState) -> float:
    """Return the reduced Hubble-like observable.

    v0.1 exposes the state's tracked `h` directly rather than attempting a more
    elaborate background reconstruction.
    """

    return float(state.h)



def compute_expansion_observables(state: ZSimState, config: ZSimConfig) -> ExpansionObservables:
    """Compile reduced expansion observables from the state and closure."""

    return ExpansionObservables(H_like=H_like(state), w_eff=effective_w(state, config))


__all__ = ["ExpansionObservables", "H_like", "effective_w", "compute_expansion_observables"]
