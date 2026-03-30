from __future__ import annotations

from zsim.lgt.stage16 import run_stage16_pipeline


def test_stage16_pipeline_live_recompute_runs() -> None:
    summary, payload = run_stage16_pipeline(
        broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        lightweight_shape_grid=((1, 1, 1),),
        sign_methods=('smooth', 'tanh'),
    )
    assert len(summary.live_rows) >= 5
    assert payload['gates']['G-LIVE-RECOMPUTE-RUN'] is True
    assert payload['gates']['G-LIVE-BROAD-ROWS-AVAILABLE'] is True
    assert payload['gates']['G-LIVE-SELECTED-OVER-LIVE-CONTROL'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
