from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage4_validate import run_su2_mbp_stage4_validate


def test_run_su2_mbp_stage4_validate(tmp_path: Path) -> None:
    summary = run_su2_mbp_stage4_validate(
        shape=(2, 2, 2),
        output_dir=tmp_path / 'stage4',
        background='caloron',
        amplitudes=(-0.4, 0.0, 0.4),
        projector_mode='center',
        chirality_mode='left',
        reg_epsilon=1e-3,
        cutoff=1e-6,
        fd_step=1e-3,
        seed=11,
    )
    assert summary['success'] is True
    out = Path(summary['output_dir'])
    assert (out / 'mbp_stage4_scan.csv').exists()
    payload = json.loads((out / 'mbp_stage4_summary.json').read_text())
    assert payload['num_rows'] == 3
    assert payload['notes']['status'] == 'preproduction-surrogate'
    assert 'negative_controls' in payload
