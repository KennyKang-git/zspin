"""Common execution pipeline helpers for Z-Sim run artifacts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping

from zsim.core import ZSimConfig
from zsim.io.logging import build_run_metadata
from zsim.io.plots import write_basic_plots
from zsim.io.serialize import ensure_output_dir, write_json, write_observables_csv, write_state_csv
from zsim.solver import IntegrationResult
from zsim.validation import emit_run_report, run_kill_switches


@dataclass(frozen=True)
class PersistedRunArtifacts:
    output_dir: Path
    generated_outputs: tuple[str, ...]
    metadata: dict[str, Any]
    diagnostics: dict[str, Any] | None = None


def _display_name(path: Path, *, relative_to: Path | None = None) -> str:
    if relative_to is None:
        return path.name
    return str(path.relative_to(relative_to))


def serialize_step_events(result: IntegrationResult) -> list[dict[str, Any]]:
    return [
        {
            'name': event.name,
            'N': event.N,
            'message': event.message,
            'terminal': event.terminal,
        }
        for event in result.events
    ]


def build_integration_diagnostics(result: IntegrationResult, config: ZSimConfig) -> dict[str, Any]:
    final_report = emit_run_report(run_kill_switches(result.final_state, config))
    return {
        'integration': {
            'success': result.success,
            'message': result.message,
            'method': result.method,
            'step_count': result.step_count,
            'N_values': list(result.N_values),
            'events': serialize_step_events(result),
        },
        'kill_switches_final': final_report,
    }


def resolve_plot_enabled(config: ZSimConfig, override: bool | None = None) -> bool:
    return config.outputs.make_plots if override is None else bool(override)


def persist_integrated_run(
    output_dir: str | Path,
    config: ZSimConfig,
    result: IntegrationResult,
    *,
    relative_to: str | Path | None = None,
    include_diagnostics: bool = False,
    include_plots: bool = True,
    make_plots_override: bool | None = None,
    metadata_extra: Mapping[str, Any] | None = None,
) -> PersistedRunArtifacts:
    out_dir = ensure_output_dir(output_dir)
    relative_root = None if relative_to is None else Path(relative_to)
    generated: list[str] = []

    state_path = write_state_csv(out_dir / 'run_state.csv', result.states)
    generated.append(_display_name(state_path, relative_to=relative_root))

    observable_path = write_observables_csv(out_dir / 'run_observables.csv', result.states, config)
    generated.append(_display_name(observable_path, relative_to=relative_root))

    diagnostics_payload: dict[str, Any] | None = None
    if include_diagnostics:
        diagnostics_payload = build_integration_diagnostics(result, config)
        diagnostics_path = write_json(out_dir / 'run_diagnostics.json', diagnostics_payload)
        generated.append(_display_name(diagnostics_path, relative_to=relative_root))

    metadata = build_run_metadata(config, result)
    if metadata_extra:
        metadata.update(dict(metadata_extra))

    if include_plots and resolve_plot_enabled(config, make_plots_override):
        plot_paths = write_basic_plots(out_dir, list(result.states), config)
        generated.extend(_display_name(path, relative_to=relative_root) for path in plot_paths)

    metadata['generated_outputs'] = list(generated) + [_display_name(out_dir / 'run_metadata.json', relative_to=relative_root)]
    metadata_path = write_json(out_dir / 'run_metadata.json', metadata)
    generated.append(_display_name(metadata_path, relative_to=relative_root))

    return PersistedRunArtifacts(
        output_dir=out_dir,
        generated_outputs=tuple(generated),
        metadata=metadata,
        diagnostics=diagnostics_payload,
    )


__all__ = [
    'PersistedRunArtifacts',
    'build_integration_diagnostics',
    'persist_integrated_run',
    'resolve_plot_enabled',
    'serialize_step_events',
]
