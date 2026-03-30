from __future__ import annotations

from zsim.lgt.stage26 import run_stage26_pipeline


def test_stage26_pipeline_runs() -> None:
    summary, payload = run_stage26_pipeline(
        shape_grid=((2, 2, 2), (3, 2, 2)),
        background='identity',
        fermion_scheme='reduced2',
        amplitudes=(0.0,),
        adaptive_chirality_modes=('left', 'right'),
        adaptive_wilson_r_grid=(0.5,),
    )
    assert len(summary.shape_rows) == 2
    assert payload['gates']['G-STAGE26-RUN'] is True
    assert payload['gates']['G-ADAPTIVE-LEDGER'] is True
    assert payload['gates']['G-ADAPTIVE-WINNER-DEFINED'] is True
