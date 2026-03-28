from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.su2_mbp_extract import run_su2_mbp_extract


def test_run_su2_mbp_extract(tmp_path: Path) -> None:
    summary = run_su2_mbp_extract(
        shape=(2, 2, 2),
        output_dir=tmp_path / 'mbp',
        background='collective',
        amplitudes=(-0.25, 0.0, 0.25),
        projector_mode='center',
        reg_epsilon=1e-3,
        cutoff=1e-6,
        fd_step=1e-3,
    )
    assert summary['success'] is True
    out = Path(summary['output_dir'])
    assert (out / 'mbp_extract_scan.csv').exists()
    payload = json.loads((out / 'mbp_extract_summary.json').read_text())
    assert payload['num_rows'] == 3
    assert payload['notes']['status'] == 'surrogate'


def test_run_su2_mbp_extract_wilson4(tmp_path: Path) -> None:
    summary = run_su2_mbp_extract(
        shape=(2, 2, 2),
        output_dir=tmp_path / 'mbp_wilson4',
        background='collective',
        amplitudes=(0.0,),
        projector_mode='center',
        fermion_scheme='wilson4',
        reg_epsilon=1e-3,
        cutoff=1e-6,
        fd_step=1e-3,
    )
    assert summary['success'] is True
    assert summary['fermion_scheme'] == 'wilson4'
    out = Path(summary['output_dir'])
    payload = json.loads((out / 'mbp_extract_summary.json').read_text())
    assert payload['fermion_scheme'] == 'wilson4'
    assert payload['best_consistency_row']['fermion_scheme'] == 'wilson4'


def test_run_su2_mbp_extract_wilson_r_chirality_ledger(tmp_path: Path) -> None:
    summary = run_su2_mbp_extract(
        shape=(2, 2, 2),
        output_dir=tmp_path / 'mbp_wilson4_sweep',
        background='collective',
        amplitudes=(0.0,),
        projector_mode='center',
        fermion_scheme='wilson4',
        wilson_r=1.0,
        wilson_r_grid=(0.5, 1.0),
        chirality_compare=('vector', 'left', 'right'),
        reg_epsilon=1e-3,
        cutoff=1e-6,
        fd_step=1e-3,
    )
    assert summary['success'] is True
    out = Path(summary['output_dir'])
    payload = json.loads((out / 'mbp_extract_summary.json').read_text())
    assert payload['wilson_r_grid'] == [0.5, 1.0]
    assert payload['chirality_compare'] == ['vector', 'left', 'right']
    assert 'wilson_r_chirality_ledger_summary' in payload
    assert (out / 'mbp_extract_wilson_r_chirality_scan.csv').exists()
    assert (out / 'mbp_extract_wilson_r_chirality_ledger.csv').exists()
