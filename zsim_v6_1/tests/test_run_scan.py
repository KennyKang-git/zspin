from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.run_scan import _build_case_configs, _normalize_params, _parse_float_list, main, run_scan
from zsim.core import ZSimConfig


def _base_config_path() -> Path:
    return Path(__file__).resolve().parents[1] / 'configs' / 'base.yaml'


def test_normalize_params_accepts_short_and_prefixed_names() -> None:
    assert _normalize_params(['gamma_xz', 'closure.gamma_zy']) == ('gamma_xz', 'gamma_zy')


def test_build_case_configs_cartesian_product_size() -> None:
    config = ZSimConfig.from_yaml(_base_config_path())
    cases = _build_case_configs(config, ('gamma_xz',), factors=(0.0, 1.0, 2.0))
    assert len(cases) == 3
    assert cases[0][2]['gamma_xz'] == 0.0
    assert cases[1][2]['gamma_xz'] == config.closure.gamma_xz


def test_parse_float_list_parses_csv() -> None:
    assert _parse_float_list('0.0, 1.0,2.5', name='--factors') == (0.0, 1.0, 2.5)


def test_run_scan_generates_summary_and_case_outputs(tmp_path: Path) -> None:
    summary = run_scan(
        _base_config_path(),
        tmp_path,
        vary=('gamma_xz',),
        factors=(0.0, 1.0),
        make_plots_override=False,
        N_end=-17.8,
    )
    assert summary['case_count'] == 2
    assert (tmp_path / 'scan_metrics.csv').exists()
    assert (tmp_path / 'scan_summary.json').exists()
    assert (tmp_path / 'case_000' / 'run_state.csv').exists()
    assert (tmp_path / 'case_001' / 'run_observables.csv').exists()


def test_run_scan_summary_lists_cases(tmp_path: Path) -> None:
    run_scan(
        _base_config_path(),
        tmp_path,
        vary=('gamma_xz',),
        factors=(0.0, 1.0),
        make_plots_override=False,
        N_end=-17.8,
    )
    payload = json.loads((tmp_path / 'scan_summary.json').read_text(encoding='utf-8'))
    assert payload['vary'] == ['gamma_xz']
    assert payload['case_count'] == 2
    assert payload['scenarios'][0]['path'] == 'case_000'


def test_run_scan_cli_entrypoint(tmp_path: Path) -> None:
    rc = main([
        '--config', str(_base_config_path()),
        '--output-dir', str(tmp_path),
        '--vary', 'gamma_xz',
        '--factors', '0.0,1.0',
        '--no-plots',
        '--N-end', '-17.8',
    ])
    assert rc == 0
    assert (tmp_path / 'scan_metrics.csv').exists()
