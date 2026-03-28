from __future__ import annotations

from pathlib import Path

from zsim.apps.su2_mbp_stage15_recompute_validate import run_su2_mbp_stage15_recompute_validate


def test_stage15_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage15_recompute_validate(
        reference_stage14_summary=Path('outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json'),
        reference_stage13_summary=Path('outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json'),
        output_dir=tmp_path,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage15_recompute_rows.csv').exists()
    assert (tmp_path / 'stage15_bridge_rows.csv').exists()
    assert (tmp_path / 'stage15_summary.json').exists()
