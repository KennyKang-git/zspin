from __future__ import annotations

from zsim.lgt.stage25 import run_stage25_pipeline


def test_stage25_pipeline_runs() -> None:
    summary, payload = run_stage25_pipeline()
    assert len(summary.sweep_rows) >= 9
    assert payload['gates']['G-STAGE25-RUN'] is True
    assert payload['gates']['G-STAGE25-SELECTED-OVER-CONTROL'] is True
    assert payload['gates']['G-STAGE25-DIRECT-LEDGER'] is True
