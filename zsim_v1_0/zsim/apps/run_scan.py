"""CLI for lightweight batch parameter scans in Z-Sim v1.0."""

from __future__ import annotations

import argparse
import itertools
from dataclasses import replace
from pathlib import Path
from typing import Any, Iterable, Sequence

import matplotlib.pyplot as plt

from zsim.core import (
    ClosureConfig,
    ConfigLoadError,
    ConfigValidationError,
    InitialConfig,
    IntegrationError,
    ZSimConfig,
)
from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io import (
    ensure_output_dir,
    persist_integrated_run,
    write_csv_rows,
    write_json,
)
from zsim.observables import H_like, compile_observables
from zsim.solver import integrate

_DEFAULT_PARAMS = ('gamma_xz', 'gamma_zy')
_DEFAULT_FACTORS = (0.0, 1.0, 2.0)

_PARAM_LOCATIONS: dict[str, tuple[str, str]] = {
    'wx': ('closure', 'wx'),
    'wz': ('closure', 'wz'),
    'wy': ('closure', 'wy'),
    'gamma_xz': ('closure', 'gamma_xz'),
    'gamma_zy': ('closure', 'gamma_zy'),
    'alpha_xz': ('closure', 'alpha_xz'),
    'alpha_zy': ('closure', 'alpha_zy'),
    'phase_mode': ('closure', 'phase_mode'),
    'epsilon_potential': ('closure', 'epsilon_potential'),
    'N0': ('initial', 'N0'),
    'a0': ('initial', 'a0'),
    'h0': ('initial', 'h0'),
    'epsilon0': ('initial', 'epsilon0'),
    'pi_epsilon0': ('initial', 'pi_epsilon0'),
    'rho_x0': ('initial', 'rho_x0'),
    'rho_z0': ('initial', 'rho_z0'),
    'rho_y0': ('initial', 'rho_y0'),
    'phi_z0': ('initial', 'phi_z0'),
    'sigma_struct0': ('initial', 'sigma_struct0'),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run lightweight Z-Sim parameter scans.')
    parser.add_argument('--config', default='configs/base.yaml', help='Path to YAML config file.')
    parser.add_argument('--output-dir', default='outputs/run_scan', help='Directory for scan artifacts.')
    parser.add_argument('--vary', nargs='*', default=list(_DEFAULT_PARAMS), help='Parameters to scan (defaults: gamma_xz gamma_zy).')
    parser.add_argument('--factors', default='0.0,1.0,2.0', help='Comma-separated multiplicative factors applied to each varied parameter.')
    parser.add_argument('--absolute-values', default=None, help='Optional comma-separated absolute values to use instead of factors.')
    parser.add_argument('--no-plots', action='store_true', help='Disable PNG plot generation for the scan run.')
    parser.add_argument('--N-end', dest='N_end', type=float, default=None, help='Optional override for solver.N_end.')
    return parser


def _parse_float_list(text: str | None, *, name: str) -> tuple[float, ...]:
    if text is None:
        return ()
    items = [item.strip() for item in text.split(',') if item.strip()]
    if not items:
        raise ConfigValidationError(f'{name} must define at least one numeric value.')
    try:
        return tuple(float(item) for item in items)
    except ValueError as exc:
        raise ConfigValidationError(f'{name} must be a comma-separated list of numeric values.') from exc


def _normalize_params(params: Iterable[str]) -> tuple[str, ...]:
    normalized: list[str] = []
    for raw in params:
        name = raw.strip()
        if not name:
            continue
        if name.startswith('closure.') or name.startswith('initial.'):
            _, _, short = name.partition('.')
            name = short
        if name not in _PARAM_LOCATIONS:
            raise ConfigValidationError(f'Unsupported scan parameter: {raw!r}.')
        normalized.append(name)
    if not normalized:
        raise ConfigValidationError('At least one valid scan parameter must be provided.')
    return tuple(normalized)


def _parameter_base_value(config: ZSimConfig, parameter: str) -> float:
    section_name, attr_name = _PARAM_LOCATIONS[parameter]
    section = getattr(config, section_name)
    value = getattr(section, attr_name)
    if isinstance(value, (int, float)):
        return float(value)
    raise ConfigValidationError(f'Scan parameter {parameter!r} is not numeric and cannot be scanned with factors.')


def _replace_parameter(config: ZSimConfig, parameter: str, value: float) -> ZSimConfig:
    section_name, attr_name = _PARAM_LOCATIONS[parameter]
    if section_name == 'closure':
        closure = replace(config.closure, **{attr_name: float(value)}).validate()
        return replace(config, closure=closure).validate()
    if section_name == 'initial':
        initial = replace(config.initial, **{attr_name: float(value)}).validate()
        return replace(config, initial=initial).validate()
    raise ConfigValidationError(f'Unsupported parameter section: {section_name!r}.')


def _build_case_configs(config: ZSimConfig, vary: Sequence[str], *, factors: Sequence[float] = _DEFAULT_FACTORS, absolute_values: Sequence[float] | None = None) -> list[tuple[str, ZSimConfig, dict[str, float]]]:
    params = _normalize_params(vary)
    if absolute_values is not None and factors:
        value_grid = [tuple(float(v) for v in absolute_values)] * len(params)
    else:
        value_grid = []
        factor_tuple = tuple(float(v) for v in factors)
        for param in params:
            base = _parameter_base_value(config, param)
            value_grid.append(tuple(base * factor for factor in factor_tuple))

    cases: list[tuple[str, ZSimConfig, dict[str, float]]] = []
    for index, values in enumerate(itertools.product(*value_grid)):
        case_name = f'case_{index:03d}'
        cfg = config
        assignments: dict[str, float] = {}
        for param, value in zip(params, values, strict=True):
            cfg = _replace_parameter(cfg, param, value)
            assignments[param] = float(value)
        cases.append((case_name, cfg, assignments))
    return cases


def _scan_metric_row(case_name: str, assignments: dict[str, float], config: ZSimConfig, *, success: bool, message: str, step_count: int | None = None, final_state: Any | None = None) -> dict[str, Any]:
    row: dict[str, Any] = {
        'case': case_name,
        'success': bool(success),
        'message': message,
        'step_count': int(step_count or 0),
    }
    for key, value in assignments.items():
        row[f'param:{key}'] = float(value)
    if final_state is None:
        row.update({
            'final_N': None,
            'final_h_like': None,
            'final_sigma_struct': None,
            'final_sector_asymmetry': None,
            'final_mediation_efficiency': None,
            'final_phase_gate_value': None,
            'final_w_eff': None,
        })
        return row

    obs = compile_observables(final_state, config)
    row.update({
        'final_N': float(final_state.N),
        'final_h_like': float(H_like(final_state)),
        'final_sigma_struct': float(final_state.sigma_struct),
        'final_sector_asymmetry': float(obs['sector_asymmetry']),
        'final_mediation_efficiency': float(obs['mediation_efficiency']),
        'final_phase_gate_value': float(obs['phase_gate_value']),
        'final_w_eff': float(obs['w_eff']),
    })
    return row


def _write_scan_plots(output_dir: Path, rows: Sequence[dict[str, Any]], *, vary: Sequence[str]) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    numeric_rows = [row for row in rows if row.get('success')]
    if not numeric_rows:
        return []

    case_ids = list(range(len(numeric_rows)))
    paths: list[Path] = []

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(case_ids, [float(row['final_sigma_struct']) for row in numeric_rows], marker='o')
    ax.set_xlabel('successful case index')
    ax.set_ylabel('final_sigma_struct')
    ax.set_title('Scan final sigma_struct')
    path = output_dir / 'scan_final_sigma_struct.png'
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    paths.append(path)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(case_ids, [float(row['final_h_like']) for row in numeric_rows], marker='o')
    ax.set_xlabel('successful case index')
    ax.set_ylabel('final_h_like')
    ax.set_title('Scan final H-like')
    path = output_dir / 'scan_final_h_like.png'
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    paths.append(path)

    if vary:
        first_param = vary[0]
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot([float(row[f'param:{first_param}']) for row in numeric_rows], [float(row['final_mediation_efficiency']) for row in numeric_rows], marker='o')
        ax.set_xlabel(first_param)
        ax.set_ylabel('final_mediation_efficiency')
        ax.set_title(f'Scan mediation efficiency vs {first_param}')
        path = output_dir / f'scan_mediation_vs_{first_param}.png'
        fig.tight_layout()
        fig.savefig(path, dpi=150)
        plt.close(fig)
        paths.append(path)

    return paths


def run_scan(config_path: str | Path, output_dir: str | Path, *, vary: Sequence[str] | None = None, factors: Sequence[float] | None = None, absolute_values: Sequence[float] | None = None, make_plots_override: bool | None = None, N_end: float | None = None) -> dict[str, Any]:
    config = ZSimConfig.from_yaml(config_path)
    vary_params = _normalize_params(vary or _DEFAULT_PARAMS)
    factor_values = tuple(_DEFAULT_FACTORS if factors is None else tuple(float(v) for v in factors))
    if absolute_values is not None:
        absolute_values = tuple(float(v) for v in absolute_values)

    out_dir = ensure_output_dir(output_dir)
    generated: list[str] = []
    summary_rows: list[dict[str, Any]] = []
    scenario_index: list[dict[str, Any]] = []

    cases = _build_case_configs(config, vary_params, factors=factor_values, absolute_values=absolute_values)

    success_count = 0
    for case_name, case_config, assignments in cases:
        case_dir = ensure_output_dir(out_dir / case_name)
        case_generated: list[str] = []
        try:
            result = integrate(case_config, N_end=N_end)
            artifacts = persist_integrated_run(
                case_dir,
                case_config,
                result,
                relative_to=out_dir,
                include_diagnostics=False,
                include_plots=False,
                metadata_extra={'scan_assignments': dict(assignments)},
            )
            case_generated.extend(artifacts.generated_outputs)
            generated.extend(case_generated)
            summary_rows.append(_scan_metric_row(case_name, assignments, case_config, success=result.success, message=result.message, step_count=result.step_count, final_state=result.final_state))
            if result.success:
                success_count += 1
            scenario_index.append({
                'case': case_name,
                'path': case_name,
                'assignments': dict(assignments),
                'success': bool(result.success),
                'message': result.message,
            })
        except (ConfigValidationError, IntegrationError) as exc:
            error_payload = {
                'case': case_name,
                'assignments': dict(assignments),
                'success': False,
                'message': str(exc),
            }
            case_generated.append(str(write_json(case_dir / 'run_metadata.json', error_payload).relative_to(out_dir)))
            generated.extend(case_generated)
            summary_rows.append(_scan_metric_row(case_name, assignments, case_config, success=False, message=str(exc)))
            scenario_index.append({
                'case': case_name,
                'path': case_name,
                'assignments': dict(assignments),
                'success': False,
                'message': str(exc),
            })

    generated.append(str(write_csv_rows(out_dir / 'scan_metrics.csv', summary_rows).name))

    summary_payload = {
        'vary': list(vary_params),
        'factor_values': list(factor_values),
        'absolute_values': None if absolute_values is None else list(absolute_values),
        'case_count': len(cases),
        'success_count': success_count,
        'failure_count': len(cases) - success_count,
        'scenarios': scenario_index,
        'generated_outputs': [],
    }
    generated.append(str(write_json(out_dir / 'scan_summary.json', summary_payload).name))

    plot_enabled = config.outputs.make_plots if make_plots_override is None else bool(make_plots_override)
    if plot_enabled:
        plot_paths = _write_scan_plots(out_dir, summary_rows, vary=vary_params)
        generated.extend(path.name for path in plot_paths)

    summary_payload['generated_outputs'] = list(generated)
    write_json(out_dir / 'scan_summary.json', summary_payload)

    return {
        'success': success_count == len(cases),
        'message': 'Parameter scan completed.',
        'output_dir': str(out_dir),
        'generated_outputs': tuple(generated),
        'case_count': len(cases),
        'success_count': success_count,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        factors = _parse_float_list(args.factors, name='--factors')
        absolute_values = _parse_float_list(args.absolute_values, name='--absolute-values') if args.absolute_values is not None else None
        summary = run_scan(
            args.config,
            args.output_dir,
            vary=args.vary,
            factors=factors,
            absolute_values=absolute_values,
            make_plots_override=not args.no_plots,
            N_end=args.N_end,
        )
    except (ConfigLoadError, ConfigValidationError, IntegrationError) as exc:
        return print_cli_failure('Z-Sim scan run failed.', exc)

    return print_cli_summary(
        'Z-Sim scan run complete.',
        summary,
        ordered_keys=('success', 'message', 'output_dir', 'case_count', 'success_count'),
    )


__all__ = [
    'build_parser',
    'run_scan',
    'main',
    '_build_case_configs',
    '_normalize_params',
    '_parse_float_list',
]


if __name__ == '__main__':
    raise SystemExit(main())
