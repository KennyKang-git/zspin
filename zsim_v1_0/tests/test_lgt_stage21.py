from __future__ import annotations

from zsim.lgt.stage21 import run_stage21_pipeline


def test_stage21_pipeline_runs() -> None:
    summary, payload = run_stage21_pipeline()
    assert len(summary.sweep_rows) >= 6
    assert payload['gates']['G-STAGE21-RUN'] is True
    assert payload['gates']['G-STAGE21-SELECTED-OVER-CONTROL'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
