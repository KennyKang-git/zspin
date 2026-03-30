"""Step-level event helpers for Z-Sim v1.0.

These are not full ``solve_ivp`` root-finding events. Instead, they are simple
post-step checks used by the segmented integrator. This keeps the v0.1 control
flow explicit and makes later kill-switch integration straightforward.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Iterable

from zsim.core import ZSimConfig, ZSimState


@dataclass(frozen=True, slots=True)
class StepEvent:
    """A discrete event detected during segmented integration."""

    name: str
    N: float
    message: str
    terminal: bool = True


def event_negative_density(state: ZSimState) -> StepEvent | None:
    negatives = [name for name in ("rho_x", "rho_z", "rho_y") if getattr(state, name) < 0.0]
    if not negatives:
        return None
    return StepEvent(
        name="negative_density",
        N=float(state.N),
        message=f"Negative density encountered in {negatives}.",
        terminal=True,
    )


def event_nonfinite_state(state: ZSimState) -> StepEvent | None:
    bad = [field for field in state.VECTOR_FIELDS if not isfinite(getattr(state, field))]
    if not bad:
        return None
    return StepEvent(
        name="nonfinite_state",
        N=float(state.N),
        message=f"Non-finite values encountered in {bad}.",
        terminal=True,
    )


def event_partition_violation(config: ZSimConfig) -> StepEvent | None:
    if config.model.enforce_zero_xy and config.model.enforce_rank2_xy:
        return None
    return StepEvent(
        name="partition_violation",
        N=float(config.initial.N0),
        message="Structural config violates v0.1 partition constraints.",
        terminal=True,
    )


def collect_step_events(state: ZSimState, config: ZSimConfig) -> list[StepEvent]:
    events: list[StepEvent] = []
    cfg_event = event_partition_violation(config)
    if cfg_event is not None:
        events.append(cfg_event)
    for fn in (event_nonfinite_state, event_negative_density):
        evt = fn(state)
        if evt is not None:
            events.append(evt)
    return events


def has_terminal_event(events: Iterable[StepEvent]) -> bool:
    return any(evt.terminal for evt in events)


__all__ = [
    "StepEvent",
    "collect_step_events",
    "event_negative_density",
    "event_nonfinite_state",
    "event_partition_violation",
    "has_terminal_event",
]
