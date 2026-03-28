"""CLI for reproducible baseline comparisons in Z-Sim v3.1."""

from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path
from typing import Any, Sequence

import matplotlib.pyplot as plt

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.core import ConfigLoadError, ConfigValidationError, IntegrationError, ZSimConfig, ZSimState
from zsim.io import (
    ensure_output_dir,
    persist_integrated_run,
    write_csv_rows,
    write_json,
    write_observables_csv,
    write_state_csv,
)
from zsim.observables import H_like, compile_observables
from zsim.solver import integrate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run reproducible Z-Sim baseline comparisons.')
    parser.add_argument('--config', default='configs/base.yaml', help='Path to YAML config file.')
    parser.add_argument('--output-dir', default='outputs/compare_baselines', help='Directory for comparison artifacts.')
    parser.add_argument('--no-plots', action='store_true', help='Disable PNG plot generation for this comparison run.')
    parser.add_argument('--N-end', dest='N_end', type=float, default=None, help='Optional override for solver.N_end.')
    return parser


def _config_with_mediation(config: ZSimConfig, *, enabled: bool) -> ZSimConfig:
    closure = replace(
        config.closure,
        gamma_xz=config.closure.gamma_xz if enabled else 0.0,
        gamma_zy=config.closure.gamma_zy if enabled else 0.0,
    )
    return replace(config, closure=closure)


def _config_with_phase_mode(config: ZSimConfig, phase_mode: str) -> ZSimConfig:
    closure = replace(config.closure, phase_mode=phase_mode)
    return replace(config, closure=closure)


def _mock_global_average_state(state: ZSimState) -> ZSimState:
    mean_rho = state.rho_total / 3.0
    mean_current = 0.5 * (state.J_xz + state.J_zy)
    return state.replace(
        rho_x=mean_rho,
        rho_z=mean_rho,
        rho_y=mean_rho,
        J_xz=mean_current,
        J_zy=mean_current,
    ).validate(require_nonnegative_densities=True)


def _scenario_metrics(name: str, states: tuple[ZSimState, ...], config: ZSimConfig, *, success: bool = True, message: str = 'OK') -> dict[str, Any]:
    final_state = states[-1]
    obs = compile_observables(final_state, config)
    return {
        'scenario': name,
        'success': bool(success),
        'message': message,
        'final_N': float(final_state.N),
        'step_count': len(states) - 1,
        'final_h_like': float(H_like(final_state)),
        'final_sigma_struct': float(final_state.sigma_struct),
        'final_phi_z': float(final_state.phi_z),
        'final_J_xz': float(final_state.J_xz),
        'final_J_zy': float(final_state.J_zy),
        'final_rho_x': float(final_state.rho_x),
        'final_rho_z': float(final_state.rho_z),
        'final_rho_y': float(final_state.rho_y),
        'final_rho_total': float(final_state.rho_total),
        'final_sector_asymmetry': float(obs['sector_asymmetry']),
        'final_mediation_efficiency': float(obs['mediation_efficiency']),
        'final_phase_gate_value': float(obs['phase_gate_value']),
        'final_w_eff': float(obs['w_eff']),
    }


def _add_reference_deltas(rows: list[dict[str, Any]], *, reference_name: str = 'reference') -> list[dict[str, Any]]:
    reference = next(row for row in rows if row['scenario'] == reference_name)
    numeric_keys = [
        'final_h_like', 'final_sigma_struct', 'final_phi_z', 'final_J_xz', 'final_J_zy',
        'final_rho_x', 'final_rho_z', 'final_rho_y', 'final_rho_total',
        'final_sector_asymmetry', 'final_mediation_efficiency', 'final_phase_gate_value', 'final_w_eff',
    ]
    augmented: list[dict[str, Any]] = []
    for row in rows:
        enriched = dict(row)
        for key in numeric_keys:
            enriched[f'delta_vs_{reference_name}:{key}'] = float(row[key]) - float(reference[key])
        augmented.append(enriched)
    return augmented


def _write_comparison_plots(output_dir: Path, trajectories: dict[str, tuple[ZSimState, ...]]) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    fig, ax = plt.subplots(figsize=(6, 4))
    for name, states in trajectories.items():
        ax.plot([s.N for s in states], [s.rho_total for s in states], label=name)
    ax.set_xlabel('N')
    ax.set_ylabel('rho_total')
    ax.set_title('Total density comparison')
    ax.legend()
    path = output_dir / 'compare_rho_total.png'
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    paths.append(path)

    fig, ax = plt.subplots(figsize=(6, 4))
    for name, states in trajectories.items():
        ax.plot([s.N for s in states], [s.sigma_struct for s in states], label=name)
    ax.set_xlabel('N')
    ax.set_ylabel('sigma_struct')
    ax.set_title('Structural arrow comparison')
    ax.legend()
    path = output_dir / 'compare_sigma_struct.png'
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    paths.append(path)

    fig, ax = plt.subplots(figsize=(6, 4))
    for name, states in trajectories.items():
        ax.plot([s.N for s in states], [s.phi_z for s in states], label=name)
    ax.set_xlabel('N')
    ax.set_ylabel('phi_z')
    ax.set_title('Phase comparison')
    ax.legend()
    path = output_dir / 'compare_phi_z.png'
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    paths.append(path)

    return paths


def compare_baselines(config_path: str | Path, output_dir: str | Path, *, make_plots_override: bool | None = None, N_end: float | None = None) -> dict[str, Any]:
    config = ZSimConfig.from_yaml(config_path)
    out_dir = ensure_output_dir(output_dir)
    generated: list[str] = []

    reference_result = integrate(config, N_end=N_end)
    mediation_off_config = _config_with_mediation(config, enabled=False)
    mediation_off_result = integrate(mediation_off_config, N_end=N_end)
    phase_constant_config = _config_with_phase_mode(config, 'constant')
    phase_constant_result = integrate(phase_constant_config, N_end=N_end)

    reference_states = tuple(reference_result.states)
    global_mean_states = tuple(_mock_global_average_state(state) for state in reference_states)

    scenarios: dict[str, dict[str, Any]] = {
        'reference': {'config': config, 'result': reference_result, 'states': reference_states, 'metadata_extra': {'comparison_scenario': 'reference'}},
        'mediation_off': {'config': mediation_off_config, 'result': mediation_off_result, 'states': tuple(mediation_off_result.states), 'metadata_extra': {'comparison_scenario': 'mediation_off'}},
        'phase_constant': {'config': phase_constant_config, 'result': phase_constant_result, 'states': tuple(phase_constant_result.states), 'metadata_extra': {'comparison_scenario': 'phase_constant'}},
    }

    for name, payload in scenarios.items():
        artifacts = persist_integrated_run(
            out_dir / name,
            payload['config'],
            payload['result'],
            relative_to=out_dir,
            include_diagnostics=False,
            include_plots=False,
            metadata_extra=payload['metadata_extra'],
        )
        generated.extend(artifacts.generated_outputs)

    mock_dir = ensure_output_dir(out_dir / 'global_mean_mock')
    generated.append(str(write_state_csv(mock_dir / 'run_state.csv', global_mean_states).relative_to(out_dir)))
    generated.append(str(write_observables_csv(mock_dir / 'run_observables.csv', global_mean_states, config).relative_to(out_dir)))
    mock_metadata = {
        'success': True,
        'message': 'Mock global-average projection from reference trajectory.',
        'epistemic_labels': {'comparison.global_mean_mock': 'TRANSLATED'},
        'comparison_scenario': 'global_mean_mock',
        'generated_outputs': [
            'global_mean_mock/run_state.csv',
            'global_mean_mock/run_observables.csv',
            'global_mean_mock/run_metadata.json',
        ],
    }
    generated.append(str(write_json(mock_dir / 'run_metadata.json', mock_metadata).relative_to(out_dir)))

    metric_rows = [
        _scenario_metrics('reference', reference_states, config, success=reference_result.success, message=reference_result.message),
        _scenario_metrics('mediation_off', tuple(mediation_off_result.states), mediation_off_config, success=mediation_off_result.success, message=mediation_off_result.message),
        _scenario_metrics('phase_constant', tuple(phase_constant_result.states), phase_constant_config, success=phase_constant_result.success, message=phase_constant_result.message),
        _scenario_metrics('global_mean_mock', global_mean_states, config, success=True, message='Mock global-average projection from reference trajectory.'),
    ]
    metric_rows = _add_reference_deltas(metric_rows)
    generated.append(str(write_csv_rows(out_dir / 'comparison_metrics.csv', metric_rows).name))

    summary_payload = {
        'reference': {
            'config_identity': 'partition_aware + mediation_on + phase_dynamic',
            'success': reference_result.success,
            'message': reference_result.message,
        },
        'comparisons': [
            'mediation_on vs mediation_off',
            'phase_dynamic vs phase_constant',
            'partition_aware vs global_mean_mock',
        ],
        'scenarios': {
            'reference': {'path': 'reference', 'description': 'Reference run reused for mediation_on, phase_dynamic, and partition_aware.'},
            'mediation_off': {'path': 'mediation_off', 'description': 'Both Z-mediated current amplitudes set to zero.'},
            'phase_constant': {'path': 'phase_constant', 'description': 'phase_mode forced to constant so dphi/dN = 0.'},
            'global_mean_mock': {'path': 'global_mean_mock', 'description': 'Post-processed mock baseline with rho_x = rho_z = rho_y = rho_total/3 on the reference trajectory.'},
        },
        'generated_outputs': [],
    }
    generated.append(str(write_json(out_dir / 'comparison_summary.json', summary_payload).name))

    plot_enabled = config.outputs.make_plots if make_plots_override is None else bool(make_plots_override)
    if plot_enabled:
        plot_paths = _write_comparison_plots(out_dir, {
            'reference': reference_states,
            'mediation_off': tuple(mediation_off_result.states),
            'phase_constant': tuple(phase_constant_result.states),
            'global_mean_mock': global_mean_states,
        })
        generated.extend(path.name for path in plot_paths)

    summary_payload['generated_outputs'] = list(generated)
    write_json(out_dir / 'comparison_summary.json', summary_payload)

    return {
        'success': bool(reference_result.success and mediation_off_result.success and phase_constant_result.success),
        'message': 'Baseline comparisons completed.',
        'output_dir': str(out_dir),
        'generated_outputs': tuple(generated),
        'scenario_count': len(scenarios) + 1,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        summary = compare_baselines(
            args.config,
            args.output_dir,
            make_plots_override=not args.no_plots,
            N_end=args.N_end,
        )
    except (ConfigLoadError, ConfigValidationError, IntegrationError) as exc:
        return print_cli_failure('Z-Sim baseline comparison failed.', exc)

    return print_cli_summary(
        'Z-Sim baseline comparisons complete.',
        summary,
        ordered_keys=('success', 'message', 'output_dir', 'scenario_count'),
    )


if __name__ == '__main__':
    raise SystemExit(main())
