from __future__ import annotations

from zsim.lgt.stage10 import run_stage10_pipeline


def test_stage10_pipeline_runs() -> None:
    summary, payload = run_stage10_pipeline(
        shape_grid=((1, 1, 1), (2, 1, 1)),
        scan_schemes=('staggered2', 'wilson4'),
        compare_schemes=('reduced2', 'wilson4'),
        sign_methods=('smooth', 'tanh', 'rational', 'arctan', 'pade11'),
        amplitudes=(0.4, 0.7),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10, 0.20),
        mass=0.10,
        kappa=0.5,
        reg_epsilon=1e-4,
        cutoff=1e-6,
        fd_step=5e-4,
        sign_epsilon=1e-4,
    )
    assert len(summary.shape_rows) == 2
    assert len(summary.comparison_rows) >= 7
    assert summary.comparison_rows[0].source_label == 'selected_background'
    assert payload['gates']['G-DIRECT-COMPARISON-LEDGER'] is True
    assert payload['gates']['G-TIGHTER-SIGN-CALIBRATION'] is True
