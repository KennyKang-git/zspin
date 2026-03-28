"""Entropy and coherence-flavored diagnostics for Z-Sim v3.1."""

from __future__ import annotations

from dataclasses import dataclass
from math import cos, log

from zsim.core import ZSimState


@dataclass(frozen=True, slots=True)
class EntropyObservables:
    """Entropy-side diagnostics compiled from a single state."""

    sigma_struct: float
    shannon_sector_entropy: float
    phase_lock_index: float

    def to_dict(self) -> dict[str, float]:
        return {
            "sigma_struct": float(self.sigma_struct),
            "shannon_sector_entropy": float(self.shannon_sector_entropy),
            "phase_lock_index": float(self.phase_lock_index),
        }



def shannon_sector_entropy(state: ZSimState) -> float:
    """Compute Shannon entropy over the normalized sector weights."""

    weights = [state.omega_x, state.omega_z, state.omega_y]
    entropy = 0.0
    for p in weights:
        if p > 0.0:
            entropy -= p * log(p)
    return entropy



def phase_lock_index(state: ZSimState) -> float:
    """Bounded phase-lock proxy in [0, 1].

    Defined as (1 + cos(phi_z)) / 2 so that perfect alignment at phi_z = 0 maps
    to 1 and anti-alignment at phi_z = pi maps to 0.
    """

    return 0.5 * (1.0 + cos(state.phi_z))



def compute_entropy_observables(state: ZSimState) -> EntropyObservables:
    """Compile entropy/coherence diagnostics from the state."""

    return EntropyObservables(
        sigma_struct=float(state.sigma_struct),
        shannon_sector_entropy=shannon_sector_entropy(state),
        phase_lock_index=phase_lock_index(state),
    )


__all__ = [
    "EntropyObservables",
    "compute_entropy_observables",
    "phase_lock_index",
    "shannon_sector_entropy",
]
