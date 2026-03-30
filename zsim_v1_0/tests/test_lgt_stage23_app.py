from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage23_hybrid_recompute_validate import run_su2_mbp_stage23_hybrid_recompute_validate


def test_stage23_app_writes_outputs(tmp_path: Path) -> None:
    result = run_su2_mbp_stage23_hybrid_recompute_validate(output_dir=tmp_path)
    assert result['success'] is True
    assert (tmp_path / 'stage23_hybrid_rows.csv').exists()
    assert (tmp_path / 'stage23_control_rows.csv').exists()
    summary_path = tmp_path / 'stage23_summary.json'
    assert summary_path.exists()
    payload = json.loads(summary_path.read_text(encoding='utf-8'))
    assert payload['gates']['G-STAGE23-RUN'] is True
