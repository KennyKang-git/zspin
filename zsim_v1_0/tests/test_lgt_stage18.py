from __future__ import annotations

from zsim.lgt.stage18 import run_stage18_pipeline


def test_stage18_pipeline_hybrid_live_stress_runs() -> None:
    summary, payload = run_stage18_pipeline()
    assert len(summary.hybrid_rows) >= 8
    assert payload['gates']['G-HYBRID-LIVE-STRESS-RUN'] is True
    assert payload['gates']['G-HYBRID-SELECTED-OVER-HYBRID-CONTROL'] is True
    assert payload['gates']['G-HYBRID-SELECTED-OVER-LIVE-CONTROL'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
