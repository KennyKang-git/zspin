from __future__ import annotations

from zsim.apps.su2_mbp_stage13_broad_compare_validate import run_su2_mbp_stage13_broad_compare_validate


def test_stage13_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage13_broad_compare_validate(
        broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        lightweight_shape_grid=((1, 1, 1),),
        output_dir=tmp_path,
        compare_schemes=('reduced2', 'wilson4'),
        sign_methods=('smooth',),
        amplitudes=(0.4,),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10,),
        sign_epsilon_grid=(1e-4,),
        fd_scale_grid=(1.0,),
        pair_count=1,
        sample_size=2,
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage13_preset_rows.csv').exists()
    assert (tmp_path / 'stage13_comparison_rows.csv').exists()
    assert (tmp_path / 'stage13_summary.json').exists()
