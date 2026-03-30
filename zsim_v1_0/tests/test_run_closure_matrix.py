from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.run_closure_matrix import main, run_closure_matrix


def test_run_closure_matrix_writes_summary_and_metrics(tmp_path: Path) -> None:
    output_dir = tmp_path / 'closure_matrix'
    summary = run_closure_matrix(
        'configs/quickstart.yaml',
        output_dir,
        phase_source_modes=('full_state', 'currents_only'),
        mediation_modes=('raw_contrast',),
        epsilon_source_modes=('zero',),
        h_closure_modes=('sqrt_sum',),
        N_end=-17.8,
    )
    assert summary['case_count'] == 2
    assert (output_dir / 'closure_matrix_summary.json').exists()
    assert (output_dir / 'closure_matrix_metrics.csv').exists()

    payload = json.loads((output_dir / 'closure_matrix_summary.json').read_text(encoding='utf-8'))
    assert payload['case_count'] == 2
    assert payload['phase_source_modes'] == ['full_state', 'currents_only']


def test_closure_matrix_cli_runs(tmp_path: Path) -> None:
    output_dir = tmp_path / 'closure_matrix_cli'
    exit_code = main([
        '--config', 'configs/quickstart.yaml',
        '--output-dir', str(output_dir),
        '--phase-source-modes', 'full_state,currents_only',
        '--mediation-modes', 'raw_contrast',
        '--epsilon-source-modes', 'zero',
        '--h-closure-modes', 'sqrt_sum',
        '--N-end', '-17.8',
        '--no-plots',
    ])
    assert exit_code == 0
    assert (output_dir / 'closure_matrix_summary.json').exists()
