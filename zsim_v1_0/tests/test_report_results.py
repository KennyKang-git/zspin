from __future__ import annotations

import json
from pathlib import Path

from zsim.apps.compare_baselines import compare_baselines
from zsim.apps.report_results import main as report_main, report_results
from zsim.apps.run_background import run_background
from zsim.apps.run_scan import run_scan
from zsim.io import build_report_payload, detect_result_type, render_markdown_report


def test_report_background(tmp_path: Path) -> None:
    run_dir = tmp_path / 'background'
    run_background('configs/quickstart.yaml', run_dir, make_plots_override=False)

    summary = report_results(run_dir)
    assert summary['success'] is True
    report_dir = run_dir / 'report'
    assert (report_dir / 'report.md').exists()
    payload = json.loads((report_dir / 'report.json').read_text(encoding='utf-8'))
    assert payload['report_type'] == 'background'
    assert detect_result_type(run_dir) == 'background'


def test_report_comparison(tmp_path: Path) -> None:
    compare_dir = tmp_path / 'compare'
    compare_baselines('configs/quickstart.yaml', compare_dir, make_plots_override=False)
    payload = build_report_payload(compare_dir)
    assert payload['report_type'] == 'comparison'
    text = render_markdown_report(payload)
    assert 'Scenario table' in text
    assert report_main(['--source-dir', str(compare_dir), '--output-dir', str(compare_dir / 'report')]) == 0


def test_report_scan(tmp_path: Path) -> None:
    scan_dir = tmp_path / 'scan'
    run_scan('configs/quickstart.yaml', scan_dir, vary=('gamma_xz',), factors=(0.0, 1.0), make_plots_override=False)
    payload = build_report_payload(scan_dir)
    assert payload['report_type'] == 'scan'
    assert payload['case_count'] == 2
    assert 'Case table' in render_markdown_report(payload)


def test_report_main_fails_for_unknown_dir(tmp_path: Path) -> None:
    empty_dir = tmp_path / 'empty'
    empty_dir.mkdir()
    assert report_main(['--source-dir', str(empty_dir), '--output-dir', str(empty_dir / 'report')]) == 2


def test_report_background_contains_interpretation(tmp_path: Path) -> None:
    run_dir = tmp_path / 'background2'
    run_background('configs/quickstart.yaml', run_dir, make_plots_override=False)
    payload = build_report_payload(run_dir)
    text = render_markdown_report(payload)
    assert 'Interpretation' in text
    assert payload['interpretation']


def test_report_index_for_parent_directory(tmp_path: Path) -> None:
    root = tmp_path / 'root'
    run_background('configs/quickstart.yaml', root / 'background', make_plots_override=False)
    compare_baselines('configs/quickstart.yaml', root / 'compare', make_plots_override=False)
    assert report_main(['--source-dir', str(root), '--output-dir', str(root / 'index_report'), '--index']) == 0
    index_json = json.loads((root / 'index_report' / 'index.json').read_text(encoding='utf-8'))
    assert index_json['report_type'] == 'index'
    assert index_json['entry_count'] >= 2
    names = {entry['name'] for entry in index_json['entries']}
    assert 'background' in names
    assert 'compare' in names
