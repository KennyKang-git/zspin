"""Segmented ODE integrator for Z-Sim v1.0.

The v0.1 engine uses a small, explicit segmented loop around ``scipy``'s
``solve_ivp`` so that projection and diagnostic hooks can be applied after every
accepted segment. This is intentionally more transparent than a single opaque
integrator call.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp

from zsim.core import IntegrationError, ZSimConfig, ZSimState
from zsim.solver.events import StepEvent, collect_step_events, has_terminal_event
from zsim.solver.projector import project_state
from zsim.solver.rhs import rhs
from zsim.validation import run_kill_switches


@dataclass(frozen=True, slots=True)
class IntegrationResult:
    """Container for a completed or failed segmented integration run."""

    success: bool
    message: str
    method: str
    states: tuple[ZSimState, ...]
    N_values: tuple[float, ...]
    events: tuple[StepEvent, ...]
    step_count: int

    @property
    def final_state(self) -> ZSimState:
        return self.states[-1]

    @property
    def trajectory(self) -> np.ndarray:
        return np.vstack([state.to_array() for state in self.states])


def _single_segment(state: ZSimState, next_N: float, config: ZSimConfig) -> ZSimState:
    if next_N <= state.N:
        raise IntegrationError("next_N must be strictly greater than the current state.N")

    solution = solve_ivp(
        fun=lambda N, y: rhs(N, y, config),
        t_span=(float(state.N), float(next_N)),
        y0=state.to_array(),
        method=config.solver.method,
        rtol=config.solver.rtol,
        atol=config.solver.atol,
        max_step=config.solver.max_step,
        t_eval=[float(next_N)],
    )

    if not solution.success or solution.y.size == 0:
        raise IntegrationError(solution.message or "Segment integration failed.")

    return ZSimState.from_array(solution.y[:, -1]).replace(N=float(solution.t[-1]))


def integrate(config: ZSimConfig, initial_state: ZSimState | None = None, *, N_end: float | None = None) -> IntegrationResult:
    """Run the reduced segmented integration loop.

    Parameters
    ----------
    config:
        Validated runtime configuration.
    initial_state:
        Optional override for the initial state. Defaults to
        ``config.make_initial_state()``.
    N_end:
        Optional override for the terminal e-fold value.
    """
    state = initial_state or config.make_initial_state()

    raw_initial_report = run_kill_switches(state, config)
    if raw_initial_report.triggers:
        init_events = [
            StepEvent(name=t.code.lower(), N=float(state.N), message=t.message, terminal=t.terminal)
            for t in raw_initial_report.triggers
        ]
        return IntegrationResult(
            success=False,
            message=init_events[0].message,
            method=config.solver.method,
            states=(state,),
            N_values=(float(state.N),),
            events=tuple(init_events),
            step_count=0,
        )

    state = project_state(state, config).validate()

    target_N = float(config.solver.N_end if N_end is None else N_end)
    if target_N < state.N:
        raise IntegrationError("Target N_end must be >= initial state.N.")

    states: list[ZSimState] = [state]
    N_values: list[float] = [float(state.N)]
    events: list[StepEvent] = []
    step_count = 0

    initial_events = collect_step_events(state, config)
    initial_report = run_kill_switches(state, config)
    if initial_report.triggers:
        initial_events.extend(
            StepEvent(name=t.code.lower(), N=float(state.N), message=t.message, terminal=t.terminal)
            for t in initial_report.triggers
        )
    if initial_events:
        events.extend(initial_events)
        if has_terminal_event(initial_events):
            return IntegrationResult(
                success=False,
                message=initial_events[0].message,
                method=config.solver.method,
                states=tuple(states),
                N_values=tuple(N_values),
                events=tuple(events),
                step_count=step_count,
            )

    while state.N < target_N - 1e-15:
        next_N = min(state.N + config.solver.max_step, target_N)
        raw_state = _single_segment(state, next_N, config)
        step_count += 1

        step_events = collect_step_events(raw_state, config)
        step_report = run_kill_switches(raw_state, config)
        if step_report.triggers:
            step_events.extend(
                StepEvent(name=t.code.lower(), N=float(raw_state.N), message=t.message, terminal=t.terminal)
                for t in step_report.triggers
            )
        if step_events:
            events.extend(step_events)
            if has_terminal_event(step_events):
                states.append(raw_state)
                N_values.append(float(raw_state.N))
                return IntegrationResult(
                    success=False,
                    message=step_events[0].message,
                    method=config.solver.method,
                    states=tuple(states),
                    N_values=tuple(N_values),
                    events=tuple(events),
                    step_count=step_count,
                )

        if step_count % config.solver.projection_every == 0:
            state = project_state(raw_state, config).validate()
        else:
            state = raw_state.validate(require_nonnegative_densities=False)

        states.append(state)
        N_values.append(float(state.N))

    return IntegrationResult(
        success=True,
        message="Integration completed successfully.",
        method=config.solver.method,
        states=tuple(states),
        N_values=tuple(N_values),
        events=tuple(events),
        step_count=step_count,
    )


__all__ = ["IntegrationResult", "integrate"]
