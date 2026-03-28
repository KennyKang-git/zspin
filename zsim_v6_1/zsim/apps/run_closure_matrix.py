"""CLI for categorical closure-mode experiments in Z-Sim v3.1."""

from __future__ import annotations

import argparse
import itertools
from pathlib import Path
from typing import Any, Iterable, Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.core import ConfigLoadError, ConfigValidationError, IntegrationError, ZSimConfig
from zsim.io import ensure_output_dir, persist_integrated_run, write_csv_rows, write_json
from zsim.observables import H_like, compile_observables
from zsim.solver import integrate

_DEFAULT_PHASE_SOURCE = ('full_state', 'currents_only', 'epsilon_mediator')
_DEFAULT_MEDIATION = ('raw_contrast', 'normalized_contrast')
_DEFAULT_EPSILON_SOURCE = ('gate_current_difference', 'current_difference', 'zero')
_DEFAULT_H_CLOSURE = ('sqrt_sum', 'sqrt_sum_plus_epsilon')


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run categorical closure-mode experiments for Z-Sim.')
    parser.add_argument('--config', default='configs/base.yaml', help='Path to YAML config file.')
    parser.add_argument('--output-dir', default='outputs/closure_matrix', help='Directory for closure experiment artifacts.')
    parser.add_argument('--phase-source-modes', default=','.join(_DEFAULT_PHASE_SOURCE), help='Comma-separated phase source modes.')
    parser.add_argument('--mediation-modes', default=','.join(_DEFAULT_MEDIATION), help='Comma-separated mediation modes.')
    parser.add_argument('--epsilon-source-modes', default=','.join(_DEFAULT_EPSILON_SOURCE), help='Comma-separated epsilon source modes.')
    parser.add_argument('--h-closure-modes', default=','.join(_DEFAULT_H_CLOSURE), help='Comma-separated H-like closure modes.')
    parser.add_argument('--limit', type=int, default=None, help='Optional cap on number of mode combinations to run.')
    parser.add_argument('--no-plots', action='store_true', help='Disable per-case plot generation.')
    parser.add_argument('--N-end', dest='N_end', type=float, default=None, help='Optional override for solver.N_end.')
    return parser


def _parse_modes(text: str | Iterable[str], *, name: str) -> tuple[str, ...]:
    if isinstance(text, str):
        raw_items = text.split(',')
    else:
        raw_items = list(text)
    modes = tuple(item.strip() for item in raw_items if str(item).strip())
    if not modes:
        raise ConfigValidationError(f'{name} must define at least one mode.')
    return modes


def _case_row(case_name: str, mode_map: dict[str, str], config: ZSimConfig, *, success: bool, message: str, step_count: int, final_state: Any | None) -> dict[str, Any]:
    row: dict[str, Any] = {
        'case': case_name,
        'success': bool(success),
        'message': message,
        'step_count': int(step_count),
        'phase_source_mode': mode_map['phase_source_mode'],
        'mediation_mode': mode_map['mediation_mode'],
        'epsilon_source_mode': mode_map['epsilon_source_mode'],
        'h_closure_mode': mode_map['h_closure_mode'],
    }
    if final_state is None:
        row.update({
            'final_N': None,
            'final_h_like': None,
            'final_sigma_struct': None,
            'final_phase_gate_value': None,
            'final_mediation_efficiency': None,
        })
        return row

    obs = compile_observables(final_state, config)
    row.update({
        'final_N': float(final_state.N),
        'final_h_like': float(H_like(final_state)),
        'final_sigma_struct': float(final_state.sigma_struct),
        'final_phase_gate_value': float(obs['phase_gate_value']),
        'final_mediation_efficiency': float(obs['mediation_efficiency']),
    })
    return row


def run_closure_matrix(
    config_path: str | Path,
    output_dir: str | Path,
    *,
    phase_source_modes: Sequence[str] | str = _DEFAULT_PHASE_SOURCE,
    mediation_modes: Sequence[str] | str = _DEFAULT_MEDIATION,
    epsilon_source_modes: Sequence[str] | str = _DEFAULT_EPSILON_SOURCE,
    h_closure_modes: Sequence[str] | str = _DEFAULT_H_CLOSURE,
    limit: int | None = None,
    make_plots_override: bool | None = None,
    N_end: float | None = None,
) -> dict[str, Any]:
    config = ZSimConfig.from_yaml(config_path)
    phase_source_modes = _parse_modes(phase_source_modes, name='phase_source_modes')
    mediation_modes = _parse_modes(mediation_modes, name='mediation_modes')
    epsilon_source_modes = _parse_modes(epsilon_source_modes, name='epsilon_source_modes')
    h_closure_modes = _parse_modes(h_closure_modes, name='h_closure_modes')
    out_dir = ensure_output_dir(output_dir)

    generated: list[str] = []
    metrics_rows: list[dict[str, Any]] = []
    scenario_index: list[dict[str, Any]] = []
    success_count = 0

    products = itertools.product(phase_source_modes, mediation_modes, epsilon_source_modes, h_closure_modes)
    if limit is not None:
        if limit < 1:
            raise ConfigValidationError('limit must be >= 1 when provided.')
        products = itertools.islice(products, limit)

    for index, (phase_source_mode, mediation_mode, epsilon_source_mode, h_closure_mode) in enumerate(products):
        case_name = f'closure_case_{index:03d}'
        mode_map = {
            'phase_source_mode': phase_source_mode,
            'mediation_mode': mediation_mode,
            'epsilon_source_mode': epsilon_source_mode,
            'h_closure_mode': h_closure_mode,
        }
        case_config = config.replace_closure(**mode_map)
        case_dir = ensure_output_dir(out_dir / case_name)
        result = integrate(case_config, N_end=N_end)
        artifacts = persist_integrated_run(
            case_dir,
            case_config,
            result,
            relative_to=out_dir,
            include_diagnostics=False,
            include_plots=False,
            make_plots_override=make_plots_override,
            metadata_extra={'closure_experiment': dict(mode_map)},
        )
        generated.extend(artifacts.generated_outputs)
        if result.success:
            success_count += 1
        metrics_rows.append(_case_row(case_name, mode_map, case_config, success=result.success, message=result.message, step_count=result.step_count, final_state=result.final_state))
        scenario_index.append({
            'case': case_name,
            'path': case_name,
            'closure_modes': dict(mode_map),
            'success': bool(result.success),
        })

    metrics_path = write_csv_rows(out_dir / 'closure_matrix_metrics.csv', metrics_rows)
    generated.append(metrics_path.name)

    summary = {
        'success': True,
        'message': 'closure matrix complete',
        'output_dir': str(out_dir),
        'case_count': len(metrics_rows),
        'success_count': success_count,
        'failure_count': len(metrics_rows) - success_count,
        'phase_source_modes': list(phase_source_modes),
        'mediation_modes': list(mediation_modes),
        'epsilon_source_modes': list(epsilon_source_modes),
        'h_closure_modes': list(h_closure_modes),
        'scenarios': scenario_index,
        'generated_outputs': sorted(set(generated + ['closure_matrix_summary.json'])),
    }
    summary_path = write_json(out_dir / 'closure_matrix_summary.json', summary)
    generated.append(summary_path.name)
    summary['generated_outputs'] = sorted(set(generated))
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_closure_matrix(
            args.config,
            args.output_dir,
            phase_source_modes=args.phase_source_modes,
            mediation_modes=args.mediation_modes,
            epsilon_source_modes=args.epsilon_source_modes,
            h_closure_modes=args.h_closure_modes,
            limit=args.limit,
            make_plots_override=not args.no_plots,
            N_end=args.N_end,
        )
    except (ConfigLoadError, ConfigValidationError, IntegrationError) as exc:
        return print_cli_failure('Z-Sim closure matrix failed.', exc)

    return print_cli_summary(
        'Z-Sim closure matrix complete.',
        summary,
        ordered_keys=('success', 'message', 'output_dir', 'case_count', 'success_count', 'failure_count'),
    )


if __name__ == '__main__':
    raise SystemExit(main())
