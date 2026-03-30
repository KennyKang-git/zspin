"""Solver package exports for Z-Sim v1.0."""

from .events import (
    StepEvent,
    collect_step_events,
    event_negative_density,
    event_nonfinite_state,
    event_partition_violation,
    has_terminal_event,
)
from .integrator import IntegrationResult, integrate
from .projector import DENSITY_FLOOR, SCALE_FACTOR_FLOOR, project_state
from .rhs import RHSDerivatives, close_state, evaluate_rhs, rhs, sigma_struct_source, state_from_ode_vector

__all__ = [
    "DENSITY_FLOOR",
    "IntegrationResult",
    "RHSDerivatives",
    "SCALE_FACTOR_FLOOR",
    "StepEvent",
    "close_state",
    "collect_step_events",
    "event_negative_density",
    "event_nonfinite_state",
    "event_partition_violation",
    "evaluate_rhs",
    "has_terminal_event",
    "integrate",
    "project_state",
    "rhs",
    "sigma_struct_source",
    "state_from_ode_vector",
]
