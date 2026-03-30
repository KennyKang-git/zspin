
from __future__ import annotations

from zsim.lgt.stage17 import run_stage17_pipeline


def test_stage17_pipeline_live_stress_runs() -> None:
    summary, payload = run_stage17_pipeline()
    assert len(summary.stress_rows) >= 7
    assert payload['gates']['G-STRESS-LEDGER-RUN'] is True
    assert payload['gates']['G-STRESS-SELECTED-OVER-STRESS-CONTROL'] is True
    assert payload['gates']['G-STRESS-SELECTED-OVER-LIVE-CONTROL'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
