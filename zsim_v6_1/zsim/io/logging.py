"""Run metadata helpers for Z-Sim v3.1."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from zsim.core import Status, ZSimConfig
from zsim.solver import IntegrationResult


def default_epistemic_labels() -> dict[str, str]:
    return {
        'model.partition': Status.PROVEN.value,
        'model.zero_xy': Status.PROVEN.value,
        'model.rank2_xy': Status.PROVEN.value,
        'closure.phase': Status.TRANSLATED.value,
        'closure.phase_source': Status.TRANSLATED.value,
        'closure.mediation': Status.TRANSLATED.value,
        'closure.background': Status.TRANSLATED.value,
        'closure.epsilon': Status.TRANSLATED.value,
        'observables.proxies': Status.HYPOTHESIS.value,
    }


def build_run_metadata(config: ZSimConfig, result: IntegrationResult) -> dict[str, Any]:
    return {
        'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'config': config.to_dict(),
        'closure_modes': config.closure.mode_summary(),
        'solver_method': result.method,
        'success': bool(result.success),
        'message': result.message,
        'step_count': int(result.step_count),
        'event_count': len(result.events),
        'initial_N': float(result.states[0].N),
        'final_N': float(result.final_state.N),
        'epistemic_labels': default_epistemic_labels(),
        'generated_outputs': [],
    }


__all__ = ['build_run_metadata', 'default_epistemic_labels']
