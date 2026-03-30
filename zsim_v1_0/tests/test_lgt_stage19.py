from __future__ import annotations

from zsim.lgt.stage19 import run_stage19_pipeline


def test_stage19_pipeline_recompute_control_sweep_runs() -> None:
    summary, payload = run_stage19_pipeline()
    assert len(summary.sweep_rows) >= 8
    assert payload['gates']['G-STAGE19-RUN'] is True
    assert payload['gates']['G-STAGE19-SELECTED-OVER-CONTROL-FAMILY'] is True
    assert payload['gates']['G-STAGE19-SIGN-STABLE-VS-STAGE18'] is True
    assert summary.selected_scheme in {'reduced2', 'staggered2', 'wilson4'}
