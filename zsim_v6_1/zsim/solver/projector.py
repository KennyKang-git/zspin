"""State projection helpers for Z-Sim v3.1.

Projection is intentionally conservative in v0.1. It does not alter the
sector topology or inject new dynamics; it only applies small numerical hygiene
operations that make the reduced ODE loop more robust.
"""

from __future__ import annotations

from zsim.core import ZSimConfig, ZSimState
from zsim.kernel import wrap_phase


DENSITY_FLOOR = 0.0
SCALE_FACTOR_FLOOR = 1e-30


def project_state(state: ZSimState, config: ZSimConfig) -> ZSimState:
    """Return a numerically sanitized state.

    v0.1 projection rules:
    - clamp sector densities to ``>= 0``;
    - clamp the scale factor away from zero;
    - wrap ``phi_z`` into ``[-pi, pi)``;
    - leave the X-Z-Y partition and current topology untouched.
    """
    del config
    return state.replace(
        a=max(float(state.a), SCALE_FACTOR_FLOOR),
        rho_x=max(float(state.rho_x), DENSITY_FLOOR),
        rho_z=max(float(state.rho_z), DENSITY_FLOOR),
        rho_y=max(float(state.rho_y), DENSITY_FLOOR),
        phi_z=wrap_phase(float(state.phi_z)),
    )


__all__ = ["DENSITY_FLOOR", "SCALE_FACTOR_FLOOR", "project_state"]
