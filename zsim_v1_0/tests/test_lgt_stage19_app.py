from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage19_recompute_control_validate import run_su2_mbp_stage19_recompute_control_validate


def test_stage19_app_writes_outputs(tmp_path: Path) -> None:
    result = run_su2_mbp_stage19_recompute_control_validate(output_dir=tmp_path)
    assert result['success'] is True
    assert (tmp_path / 'stage19_sweep_rows.csv').exists()
    assert (tmp_path / 'stage19_control_family_rows.csv').exists()
    summary_path = tmp_path / 'stage19_summary.json'
    assert summary_path.exists()
    payload = json.loads(summary_path.read_text(encoding='utf-8'))
    assert payload['gates']['G-STAGE19-RUN'] is True
