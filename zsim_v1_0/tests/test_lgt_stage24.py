from __future__ import annotations

from zsim.lgt.stage24 import run_stage24_pipeline


def test_stage24_pipeline_runs() -> None:
    summary, payload = run_stage24_pipeline()
    assert len(summary.sweep_rows) >= 7
    assert payload['gates']['G-STAGE24-RUN'] is True
    assert payload['gates']['G-STAGE24-SELECTED-OVER-CONTROL'] is True
    assert payload['gates']['G-STAGE24-DIRECT-LEDGER'] is True
