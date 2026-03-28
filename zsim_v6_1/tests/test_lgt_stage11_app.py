from __future__ import annotations

from zsim.apps.su2_mbp_stage11_stress_validate import run_su2_mbp_stage11_stress_validate


def test_stage11_app_outputs(tmp_path) -> None:
    summary = run_su2_mbp_stage11_stress_validate(
        shape_grid=((1, 1, 1), (2, 1, 1)),
        output_dir=tmp_path,
        compare_schemes=('reduced2', 'wilson4'),
        sign_methods=('smooth', 'tanh'),
        amplitudes=(0.4,),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10,),
        sign_epsilon_grid=(5e-5, 1e-4),
        fd_scale_grid=(1.0,),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
    )
    assert summary['success'] is True
    assert (tmp_path / 'stage11_shape_rows.csv').exists()
    assert (tmp_path / 'stage11_stress_rows.csv').exists()
    assert (tmp_path / 'stage11_summary.json').exists()
