import json
from pathlib import Path

from zsim.apps.su2_bcc_scan import run_su2_bcc_scan
from zsim.apps.su2_collective_hmc import run_su2_collective_hmc
from zsim.apps.su2_valley_probe import run_su2_valley_probe


def test_su2_bcc_scan_app(tmp_path: Path):
    out_dir = tmp_path / 'scan'
    summary = run_su2_bcc_scan(output_dir=out_dir, use_identity=True, cooling_steps=2)
    assert summary['success'] is True
    payload = json.loads((out_dir / 'bcc_summary.json').read_text(encoding='utf-8'))
    assert payload['num_sites'] == 35
    assert payload['num_plaquettes'] == 48


def test_su2_valley_probe_app(tmp_path: Path):
    out_dir = tmp_path / 'probe'
    summary = run_su2_valley_probe(output_dir=out_dir)
    assert summary['success'] is True
    payload = json.loads((out_dir / 'valley_probe_summary.json').read_text(encoding='utf-8'))
    assert payload['num_edges'] == 64
    assert 'kappa2_proxy' in payload['even_quartic_fit']


def test_su2_collective_hmc_app(tmp_path: Path):
    out_dir = tmp_path / 'hmc'
    summary = run_su2_collective_hmc(output_dir=out_dir, steps=8)
    assert summary['success'] is True
    payload = json.loads((out_dir / 'collective_hmc_summary.json').read_text(encoding='utf-8'))
    assert 0.0 <= payload['accept_rate'] <= 1.0
