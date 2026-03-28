from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

from zsim.apps.run_background import run_background


REQUIRED_CORE_FILES = {
    'run_state.csv',
    'run_observables.csv',
    'run_diagnostics.json',
    'run_metadata.json',
}

REQUIRED_PLOT_FILES = {
    'densities.png',
    'epsilon_phase.png',
    'expansion_currents.png',
}


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))



def test_smoke_pipeline_with_plots_generates_expected_artifacts(tmp_path):
    out_dir = tmp_path / 'smoke_run'
    summary = run_background('configs/base.yaml', out_dir, make_plots_override=True, N_end=-17.8)

    assert summary['success'] is True

    produced = {p.name for p in out_dir.iterdir() if p.is_file()}
    assert REQUIRED_CORE_FILES.issubset(produced)
    assert REQUIRED_PLOT_FILES.issubset(produced)

    generated = set(summary['generated_outputs'])
    assert REQUIRED_CORE_FILES.issubset(generated)
    assert REQUIRED_PLOT_FILES.issubset(generated)



def test_smoke_pipeline_csv_and_metadata_are_consistent(tmp_path):
    out_dir = tmp_path / 'smoke_consistency'
    summary = run_background('configs/base.yaml', out_dir, make_plots_override=False, N_end=-17.75)

    assert summary['success'] is True

    state_rows = _read_csv_rows(out_dir / 'run_state.csv')
    obs_rows = _read_csv_rows(out_dir / 'run_observables.csv')
    diagnostics = json.loads((out_dir / 'run_diagnostics.json').read_text(encoding='utf-8'))
    metadata = json.loads((out_dir / 'run_metadata.json').read_text(encoding='utf-8'))

    assert len(state_rows) > 0
    assert len(state_rows) == len(obs_rows)
    assert float(state_rows[0]['N']) == float(metadata['initial_N'])
    assert float(state_rows[-1]['N']) == float(metadata['final_N'])
    assert diagnostics['integration']['step_count'] == summary['step_count']
    assert metadata['generated_outputs'] == list(summary['generated_outputs'])
    assert set(REQUIRED_CORE_FILES).issubset(set(metadata['generated_outputs']))

    first_obs = obs_rows[0]
    last_obs = obs_rows[-1]
    for key in ['rho_total', 'omega_x', 'omega_z', 'omega_y', 'H_like', 'rank_xy_proxy']:
        assert key in first_obs
        assert key in last_obs



def test_cli_module_smoke_run_returns_zero_and_writes_outputs(tmp_path):
    out_dir = tmp_path / 'module_cli'
    command = [
        sys.executable,
        '-m', 'zsim.apps.run_background',
        '--config', 'configs/base.yaml',
        '--output-dir', str(out_dir),
        '--no-plots',
        '--N-end', '-17.9',
    ]
    completed = subprocess.run(command, cwd=Path.cwd(), capture_output=True, text=True)

    assert completed.returncode == 0, completed.stderr
    assert 'Z-Sim background run complete.' in completed.stdout
    for filename in REQUIRED_CORE_FILES:
        assert (out_dir / filename).exists()



def test_cli_returns_one_on_invalid_initial_state_config(tmp_path):
    bad_cfg = tmp_path / 'bad_initial.yaml'
    bad_cfg.write_text(
        '\n'.join([
            'model:',
            '  A: 35/437',
            '  dims:',
            '    X: 3',
            '    Z: 2',
            '    Y: 6',
            '  enforce_zero_xy: true',
            '  enforce_rank2_xy: true',
            'closure:',
            '  wx: 0.0',
            '  wz: -1.0',
            '  wy: 1/3',
            '  gamma_xz: 0.1',
            '  gamma_zy: 0.1',
            '  alpha_xz: 1.0',
            '  alpha_zy: 1.0',
            '  phase_mode: bounded_sine',
            '  epsilon_potential: quartic',
            'initial:',
            '  N0: -18.0',
            '  a0: 1.0e-8',
            '  h0: 1.0',
            '  epsilon0: 1.0',
            '  pi_epsilon0: 0.0',
            '  rho_x0: -0.30',
            '  rho_z0: 0.02',
            '  rho_y0: 0.68',
            '  phi_z0: 0.0',
            '  sigma_struct0: 0.0',
            'solver:',
            '  method: RK45',
            '  rtol: 1e-8',
            '  atol: 1e-10',
            '  N_end: -17.5',
            '  max_step: 0.05',
            '  projection_every: 1',
            'outputs:',
            '  save_state_csv: true',
            '  save_observables_csv: true',
            '  save_diagnostics_json: true',
            '  make_plots: false',
        ]),
        encoding='utf-8',
    )

    out_dir = tmp_path / 'bad_run'
    command = [
        sys.executable,
        '-m', 'zsim.apps.run_background',
        '--config', str(bad_cfg),
        '--output-dir', str(out_dir),
        '--no-plots',
    ]
    completed = subprocess.run(command, cwd=Path.cwd(), capture_output=True, text=True)

    assert completed.returncode == 2
    assert 'Z-Sim background run failed before execution.' in completed.stderr
    assert 'ConfigValidationError' in completed.stderr
    assert 'initial.rho_x0 must be non-negative.' in completed.stderr
    assert not (out_dir / 'run_diagnostics.json').exists()
