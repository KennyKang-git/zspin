"""Density-side observables for Z-Sim v1.0.

These functions expose stable, low-cost quantities that can be computed directly
from a reduced state. They are intended to be the first layer of the observable
compiler: simple, transparent, and structure-preserving.
"""

from __future__ import annotations

from dataclasses import dataclass

from zsim.core import ZSimState


@dataclass(frozen=True, slots=True)
class DensityObservables:
    """Native density observables compiled from a single state."""

    rho_total: float
    omega_x: float
    omega_z: float
    omega_y: float
    sector_asymmetry: float

    def to_dict(self) -> dict[str, float]:
        return {
            "rho_total": float(self.rho_total),
            "omega_x": float(self.omega_x),
            "omega_z": float(self.omega_z),
            "omega_y": float(self.omega_y),
            "sector_asymmetry": float(self.sector_asymmetry),
        }



def sector_asymmetry(state: ZSimState) -> float:
    """Return a simple X-Y contrast proxy.

    v0.1 uses a normalized absolute X/Y imbalance:

        |rho_x - rho_y| / rho_total

    This is a translated diagnostic, not a final physical claim.
    """

    if state.rho_total == 0.0:
        return 0.0
    return abs(state.rho_x - state.rho_y) / state.rho_total



def compute_density_observables(state: ZSimState) -> DensityObservables:
    """Compile native density observables from the reduced state."""

    return DensityObservables(
        rho_total=state.rho_total,
        omega_x=state.omega_x,
        omega_z=state.omega_z,
        omega_y=state.omega_y,
        sector_asymmetry=sector_asymmetry(state),
    )


__all__ = ["DensityObservables", "compute_density_observables", "sector_asymmetry"]
