from __future__ import annotations

from zsim.lgt.stage13 import run_stage13_pipeline


def test_stage13_pipeline_runs() -> None:
    summary, payload = run_stage13_pipeline(
        broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        lightweight_shape_grid=((1, 1, 1),),
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
    assert len(summary.preset_rows) == 2
    assert len(summary.comparison_rows) >= 4
    assert payload['gates']['G-BROAD-PRESET-RUN'] is True
    assert payload['gates']['G-DIRECT-COMPARISON-LEDGER'] is True
    assert payload['gates']['G-BROAD-SCHEME-STABLE-VS-LIGHTWEIGHT'] is True
    assert payload['gates']['G-BROAD-SELECTED-OVER-BROAD-CONTROL'] is True
    assert payload['gates']['G-LIGHTWEIGHT-SELECTED-OVER-LIGHTWEIGHT-CONTROL'] is True
