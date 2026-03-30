from __future__ import annotations

from zsim.lgt.stage23 import run_stage23_pipeline


def test_stage23_pipeline_runs() -> None:
    summary, payload = run_stage23_pipeline()
    assert len(summary.sweep_rows) >= 6
    assert payload['gates']['G-STAGE23-RUN'] is True
    assert payload['gates']['G-STAGE23-SELECTED-OVER-CONTROL'] is True
    assert payload['gates']['G-STAGE23-DIRECT-HYBRID-LEDGER'] is True
