from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_quickstart_config_exists():
    path = REPO_ROOT / 'configs' / 'quickstart.yaml'
    assert path.exists()
    text = path.read_text(encoding='utf-8')
    assert 'N_end: -17.8' in text
    assert 'make_plots: false' in text


def test_quickstart_script_help():
    result = subprocess.run([sys.executable, 'scripts/quickstart.py', '--help'], cwd=REPO_ROOT, capture_output=True, text=True)
    assert result.returncode == 0
    assert 'background' in result.stdout
    assert 'compare' in result.stdout
    assert 'scan' in result.stdout
