from __future__ import annotations

from zsim.lgt.stage12 import run_stage12_pipeline


def test_stage12_pipeline_runs() -> None:
    summary, payload = run_stage12_pipeline(
        shape_grid=((1, 1, 1),),
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
    assert len(summary.coverage_rows) == 1
    assert len(summary.calibration_rows) >= 2
    assert summary.calibration_rows[0].source_label == 'selected_background'
    assert payload['gates']['G-CLOSURE-CALIBRATION-REPORT'] is True
    assert payload['gates']['G-SELECTED-CALIBRATED-TOP-RANK'] is True
    assert payload['gates']['G-SELECTED-CALIBRATED-OVER-CONTROLS'] is True
