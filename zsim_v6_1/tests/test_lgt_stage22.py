from __future__ import annotations

from zsim.lgt.stage22 import run_stage22_pipeline


def test_stage22_pipeline_runs() -> None:
    summary, payload = run_stage22_pipeline()
    assert len(summary.sweep_rows) >= 6
    assert payload['gates']['G-STAGE22-RUN'] is True
    assert payload['gates']['G-STAGE22-RECOMPUTE-SNAPSHOT-AVAILABLE'] is True
    assert payload['gates']['G-STAGE22-SELECTED-OVER-CONTROL'] is True
