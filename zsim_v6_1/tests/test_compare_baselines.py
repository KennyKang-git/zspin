from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.compare_baselines import compare_baselines, main


def _base_config_path() -> Path:
    return Path(__file__).resolve().parents[1] / 'configs' / 'base.yaml'


def test_compare_baselines_generates_core_outputs(tmp_path: Path) -> None:
    summary = compare_baselines(_base_config_path(), tmp_path, make_plots_override=False, N_end=-17.8)
    assert summary['success'] is True
    assert (tmp_path / 'comparison_summary.json').exists()
    assert (tmp_path / 'comparison_metrics.csv').exists()
    assert (tmp_path / 'reference' / 'run_state.csv').exists()
    assert (tmp_path / 'mediation_off' / 'run_observables.csv').exists()
    assert (tmp_path / 'phase_constant' / 'run_metadata.json').exists()
    assert (tmp_path / 'global_mean_mock' / 'run_state.csv').exists()


def test_compare_baselines_summary_lists_expected_modes(tmp_path: Path) -> None:
    compare_baselines(_base_config_path(), tmp_path, make_plots_override=False, N_end=-17.8)
    payload = json.loads((tmp_path / 'comparison_summary.json').read_text(encoding='utf-8'))
    assert 'mediation_on vs mediation_off' in payload['comparisons']
    assert 'phase_dynamic vs phase_constant' in payload['comparisons']
    assert 'partition_aware vs global_mean_mock' in payload['comparisons']
    assert payload['scenarios']['reference']['path'] == 'reference'


def test_compare_baselines_cli_entrypoint(tmp_path: Path) -> None:
    rc = main([
        '--config', str(_base_config_path()),
        '--output-dir', str(tmp_path),
        '--no-plots',
        '--N-end', '-17.8',
    ])
    assert rc == 0
    assert (tmp_path / 'comparison_metrics.csv').exists()
