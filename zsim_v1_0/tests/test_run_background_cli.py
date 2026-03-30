from pathlib import Path

from zsim.apps.run_background import main, run_background
from zsim.core import ZSimConfig


def test_run_background_function_writes_core_outputs(tmp_path):
    config_path = Path('configs/base.yaml')
    out_dir = tmp_path / 'run'
    summary = run_background(config_path, out_dir, make_plots_override=False, N_end=-17.8)

    assert summary['success'] is True
    assert (out_dir / 'run_state.csv').exists()
    assert (out_dir / 'run_observables.csv').exists()
    assert (out_dir / 'run_diagnostics.json').exists()
    assert (out_dir / 'run_metadata.json').exists()
    assert 'run_state.csv' in summary['generated_outputs']


def test_run_background_cli_main_returns_zero(tmp_path):
    exit_code = main([
        '--config', 'configs/base.yaml',
        '--output-dir', str(tmp_path / 'cli_run'),
        '--no-plots',
        '--N-end', '-17.85',
    ])
    assert exit_code == 0
    assert (tmp_path / 'cli_run' / 'run_state.csv').exists()
