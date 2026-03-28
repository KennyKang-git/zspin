
from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage17_live_stress_validate import run_su2_mbp_stage17_live_stress_validate


def test_stage17_app_writes_outputs(tmp_path: Path) -> None:
    result = run_su2_mbp_stage17_live_stress_validate(output_dir=tmp_path)
    assert result['success'] is True
    assert (tmp_path / 'stage17_stress_rows.csv').exists()
    summary_path = tmp_path / 'stage17_summary.json'
    assert summary_path.exists()
    payload = json.loads(summary_path.read_text(encoding='utf-8'))
    assert payload['gates']['G-STRESS-LEDGER-RUN'] is True
