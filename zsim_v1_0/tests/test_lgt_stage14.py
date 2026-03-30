from __future__ import annotations

from pathlib import Path

from zsim.lgt.stage14 import run_stage14_pipeline


def test_stage14_pipeline_runs() -> None:
    summary, payload = run_stage14_pipeline(
        reference_stage13_summary=Path('outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json'),
        default_broad_shape_grid=((1, 1, 1), (2, 1, 1)),
        expanded_broad_shape_grid=((1, 1, 1), (2, 1, 1), (2, 2, 1)),
        larger_shape_sweep_grid=((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2)),
        lightweight_shape_grid=((1, 1, 1),),
    )
    assert len(summary.sweep_rows) == 3
    assert len(summary.stability_rows) == 6
    assert payload['gates']['G-PRESET-SWEEP-RUN'] is True
    assert payload['gates']['G-LARGER-SHAPE-PRESET-EXPANDED'] is True
    assert payload['gates']['G-DIRECT-LEDGER-STABILITY-STRESS'] is True
    assert payload['gates']['G-SIGN-STABLE-ACROSS-SWEEPS'] is True
    assert payload['gates']['G-SCHEME-STABLE-ACROSS-SWEEPS'] is True
