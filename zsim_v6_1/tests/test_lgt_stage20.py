from __future__ import annotations

from zsim.lgt.stage20 import run_stage20_pipeline


def test_stage20_pipeline_live_sweep_runs() -> None:
    summary, payload = run_stage20_pipeline(
        broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        lightweight_shape_grid=((1, 1, 1),),
        sign_methods=('smooth', 'tanh'),
        amplitudes=(0.35,),
        separations=(0.55,),
        widths=(0.45,),
        seam_biases=(0.10,),
        sign_epsilon_grid=(1e-5,),
        fd_scale_grid=(1.0,),
        pair_count=1,
        sample_size=2,
    )
    assert len(summary.sweep_rows) >= 6
    assert payload['gates']['G-STAGE20-RUN'] is True
    assert payload['gates']['G-STAGE20-LIVE-SELECTED-BACKGROUND-FOUND'] is True
    assert payload['gates']['G-STAGE20-SELECTED-OVER-LIVE-CONTROL'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
