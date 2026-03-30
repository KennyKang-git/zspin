"""Serialization helpers for Z-Sim v1.0."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from zsim.core import ZSimConfig, ZSimState
from zsim.observables import compile_observables


def ensure_output_dir(path: str | Path) -> Path:
    """Create and return an output directory."""
    output_dir = Path(path)
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def states_to_rows(states: Sequence[ZSimState]) -> list[dict[str, float]]:
    """Convert a state trajectory into CSV-friendly rows."""
    return [state.to_dict() for state in states]



def observables_to_rows(states: Sequence[ZSimState], config: ZSimConfig) -> list[dict[str, float]]:
    """Compile observables for each state in a trajectory."""
    rows: list[dict[str, float]] = []
    for state in states:
        row = {"N": float(state.N), "a": float(state.a)}
        row.update(compile_observables(state, config))
        rows.append(row)
    return rows



def write_csv_rows(path: str | Path, rows: Sequence[Mapping[str, Any]]) -> Path:
    """Write homogeneous mapping rows to CSV."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        out_path.write_text('', encoding='utf-8')
        return out_path
    fieldnames = list(rows[0].keys())
    with out_path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(dict(row))
    return out_path



def write_json(path: str | Path, payload: Mapping[str, Any]) -> Path:
    """Write a JSON payload with stable formatting."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding='utf-8')
    return out_path



def write_state_csv(path: str | Path, states: Sequence[ZSimState]) -> Path:
    return write_csv_rows(path, states_to_rows(states))



def write_observables_csv(path: str | Path, states: Sequence[ZSimState], config: ZSimConfig) -> Path:
    return write_csv_rows(path, observables_to_rows(states, config))


__all__ = [
    'ensure_output_dir',
    'observables_to_rows',
    'states_to_rows',
    'write_csv_rows',
    'write_json',
    'write_observables_csv',
    'write_state_csv',
]
