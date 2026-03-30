import json
from pathlib import Path

from zsim.apps.quantum_topology import run_quantum_topology


def test_quantum_topology_app(tmp_path: Path):
    summary = run_quantum_topology(geometry='ti', output_dir=tmp_path)
    assert summary['success'] is True
    payload = json.loads((tmp_path / 'topology_summary.json').read_text(encoding='utf-8'))
    assert payload['counts'] == {'V': 60, 'E': 90, 'F': 32}
