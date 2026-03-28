from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage20_live_sweep_validate import run_su2_mbp_stage20_live_sweep_validate


def test_stage20_app_writes_outputs(tmp_path: Path) -> None:
    result = run_su2_mbp_stage20_live_sweep_validate(
        broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        lightweight_shape_grid=((1, 1, 1),),
        sign_methods=('smooth', 'tanh'),
        amplitudes=(0.35,),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10,),
        sign_epsilon_grid=(1e-5,),
        fd_scale_grid=(1.0,),
        pair_count=1,
        sample_size=2,
        output_dir=tmp_path,
    )
    assert result['success'] is True
    assert (tmp_path / 'stage20_live_rows.csv').exists()
    assert (tmp_path / 'stage20_control_rows.csv').exists()
    summary_path = tmp_path / 'stage20_summary.json'
    assert summary_path.exists()
    payload = json.loads(summary_path.read_text(encoding='utf-8'))
    assert payload['gates']['G-STAGE20-RUN'] is True
