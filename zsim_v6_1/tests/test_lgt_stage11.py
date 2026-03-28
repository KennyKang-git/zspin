from __future__ import annotations

from zsim.lgt.stage11 import run_stage11_pipeline


def test_stage11_pipeline_runs() -> None:
    summary, payload = run_stage11_pipeline(
        shape_grid=((1, 1, 1), (2, 1, 1)),
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
    assert len(summary.shape_rows) == 2
    assert len(summary.stress_rows) >= 7
    assert summary.stress_rows[0].source_label == 'selected_background'
    assert payload['gates']['G-CLOSURE-LEDGER-STRESS-TEST'] is True
    assert payload['gates']['G-SELECTED-ROBUST-OVER-CONTROLS'] is True
