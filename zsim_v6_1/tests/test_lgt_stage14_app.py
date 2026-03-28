from __future__ import annotations

from pathlib import Path

from zsim.apps.su2_mbp_stage14_preset_sweep_validate import run_su2_mbp_stage14_preset_sweep_validate


def test_stage14_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage14_preset_sweep_validate(
        reference_stage13_summary=Path('outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json'),
        default_broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        expanded_broad_shape_grid=((1, 1, 1), (2, 1, 1), (2, 2, 1)),
        larger_shape_sweep_grid=((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2)),
        lightweight_shape_grid=((1, 1, 1),),
        output_dir=tmp_path,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage14_sweep_rows.csv').exists()
    assert (tmp_path / 'stage14_stability_rows.csv').exists()
    assert (tmp_path / 'stage14_summary.json').exists()
