"""CLI entry point for one Z-Sim background run."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.core import ConfigLoadError, ConfigValidationError, IntegrationError, ZSimConfig
from zsim.io import ensure_output_dir, persist_integrated_run
from zsim.solver import integrate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run a Z-Sim v1.0 background evolution.')
    parser.add_argument('--config', default='configs/base.yaml', help='Path to YAML config file.')
    parser.add_argument('--output-dir', default='outputs/run_background', help='Directory for run artifacts.')
    parser.add_argument('--no-plots', action='store_true', help='Disable PNG plot generation for this run.')
    parser.add_argument('--N-end', dest='N_end', type=float, default=None, help='Optional override for solver.N_end.')
    return parser


def run_background(config_path: str | Path, output_dir: str | Path, *, make_plots_override: bool | None = None, N_end: float | None = None) -> dict[str, object]:
    config = ZSimConfig.from_yaml(config_path)
    result = integrate(config, N_end=N_end)
    out_dir = ensure_output_dir(output_dir)
    artifacts = persist_integrated_run(
        out_dir,
        config,
        result,
        include_diagnostics=True,
        make_plots_override=make_plots_override,
    )
    return {
        'success': result.success,
        'message': result.message,
        'output_dir': str(artifacts.output_dir),
        'generated_outputs': artifacts.generated_outputs,
        'step_count': result.step_count,
        'final_N': float(result.final_state.N),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_background(
            args.config,
            args.output_dir,
            make_plots_override=not args.no_plots,
            N_end=args.N_end,
        )
    except (ConfigLoadError, ConfigValidationError, IntegrationError) as exc:
        return print_cli_failure('Z-Sim background run failed before execution.', exc)

    return print_cli_summary(
        'Z-Sim background run complete.',
        summary,
        ordered_keys=('success', 'message', 'output_dir', 'step_count', 'final_N'),
    )


if __name__ == '__main__':
    raise SystemExit(main())
