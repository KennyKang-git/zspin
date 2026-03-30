from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_stage5_spinor_validate import run_su2_mbp_stage5_spinor_validate


def test_stage5_app_writes_outputs(tmp_path: Path) -> None:
    summary = run_su2_mbp_stage5_spinor_validate(output_dir=tmp_path, amplitudes=(0.5,), separations=(0.75,), widths=(0.6,), seam_biases=(0.15,), mass=0.15, kappa=0.6, reg_epsilon=1e-4, cutoff=1e-6, fd_step=5e-4)
    assert summary['success'] is True
    payload = json.loads((tmp_path / 'stage5_spinor_summary.json').read_text(encoding='utf-8'))
    assert payload['fermion_scheme'] == 'wilson4'
    assert 'G-TRACE-FD' in payload['gates']
