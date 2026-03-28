from __future__ import annotations

from pathlib import Path

from zsim.lgt.stage15 import run_stage15_pipeline


def test_stage15_pipeline_runs() -> None:
    summary, payload = run_stage15_pipeline(
        reference_stage14_summary=Path('outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json'),
        reference_stage13_summary=Path('outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json'),
    )
    assert len(summary.recompute_rows) == 4
    assert len(summary.bridge_rows) == 4
    assert payload['gates']['G-RECOMPUTE-AWARE-RUN'] is True
    assert payload['gates']['G-STAGE14-SOURCE-AVAILABLE'] is True
    assert payload['gates']['G-BROAD-RECOMPUTE-SNAPSHOT-AVAILABLE'] is True
    assert payload['gates']['G-SIGN-STABLE-VS-RECOMPUTE'] is True
    assert payload['gates']['G-SCHEME-STABLE-VS-RECOMPUTE'] is True
    assert payload['gates']['G-DIRECT-BRIDGE-LEDGER'] is True
