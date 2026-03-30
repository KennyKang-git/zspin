from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.common import print_cli_summary
from zsim.core import ZSimConfig
from zsim.io import build_integration_diagnostics, persist_integrated_run
from zsim.solver import integrate


def test_persist_integrated_run_writes_standard_artifacts(tmp_path: Path) -> None:
    config = ZSimConfig.from_yaml('configs/base.yaml')
    result = integrate(config, N_end=-17.8)

    artifacts = persist_integrated_run(
        tmp_path / 'run',
        config,
        result,
        include_diagnostics=True,
        make_plots_override=False,
        metadata_extra={'test_tag': 'stage20'},
    )

    assert (tmp_path / 'run' / 'run_state.csv').exists()
    assert (tmp_path / 'run' / 'run_observables.csv').exists()
    assert (tmp_path / 'run' / 'run_diagnostics.json').exists()
    assert (tmp_path / 'run' / 'run_metadata.json').exists()
    assert 'run_metadata.json' in artifacts.generated_outputs
    payload = json.loads((tmp_path / 'run' / 'run_metadata.json').read_text(encoding='utf-8'))
    assert payload['test_tag'] == 'stage20'


def test_build_integration_diagnostics_matches_result_shape() -> None:
    config = ZSimConfig.from_yaml('configs/base.yaml')
    result = integrate(config, N_end=-17.8)
    diagnostics = build_integration_diagnostics(result, config)
    assert diagnostics['integration']['step_count'] == result.step_count
    assert diagnostics['integration']['events'] == []


def test_print_cli_summary_success_code(capsys) -> None:
    code = print_cli_summary('Header', {'success': True, 'message': 'ok', 'generated_outputs': ('a', 'b')}, ordered_keys=('success', 'message'))
    captured = capsys.readouterr()
    assert code == 0
    assert 'Header' in captured.out
    assert 'generated_outputs:' in captured.out
