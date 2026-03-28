from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage26_shape_adaptive_validate import run_su2_mbp_stage26_shape_adaptive_validate


def test_stage26_app_writes_outputs(tmp_path: Path) -> None:
    result = run_su2_mbp_stage26_shape_adaptive_validate(
        shape_grid=((2, 2, 2), (3, 2, 2)),
        background='identity',
        fermion_scheme='reduced2',
        amplitudes=(0.0,),
        adaptive_chirality_modes=('left', 'right'),
        adaptive_wilson_r_grid=(0.5,),
        output_dir=tmp_path,
    )
    assert result['success'] is True
    assert (tmp_path / 'stage26_shape_rows.csv').exists()
    assert (tmp_path / 'stage26_adaptive_rows.csv').exists()
    summary_path = tmp_path / 'stage26_summary.json'
    assert summary_path.exists()
    payload = json.loads(summary_path.read_text(encoding='utf-8'))
    assert payload['gates']['G-STAGE26-RUN'] is True
