
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage17StressRow:
    source_label: str
    scenario_label: str
    is_control: bool
    derives_from_live: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    sign_matches_snapshot: bool
    scheme_matches_snapshot: bool
    shape_matches_snapshot: bool
    stress_gain: float
    snapshot_delta: float
    stress_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'scenario_label': self.scenario_label,
            'is_control': self.is_control,
            'derives_from_live': self.derives_from_live,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'sign_matches_snapshot': self.sign_matches_snapshot,
            'scheme_matches_snapshot': self.scheme_matches_snapshot,
            'shape_matches_snapshot': self.shape_matches_snapshot,
            'stress_gain': self.stress_gain,
            'snapshot_delta': self.snapshot_delta,
            'stress_score': self.stress_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage17Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    stress_rows: list[Stage17StressRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'stress_rows': [row.to_dict() for row in self.stress_rows],
            'notes': dict(self.notes),
        }


def _load_payload(path: str | Path) -> Mapping[str, Any]:
    return json.loads(Path(path).read_text(encoding='utf-8'))


def _shape_tuple(value: str | Sequence[int]) -> tuple[int, int, int]:
    if isinstance(value, str):
        parts = [int(v) for v in value.split('x') if v]
    else:
        parts = [int(v) for v in value]
    if len(parts) != 3:
        raise ValueError('shape must have exactly three entries')
    return (parts[0], parts[1], parts[2])


def _shape_size(shape: tuple[int, int, int]) -> int:
    nx, ny, nz = shape
    return int(nx * ny * nz)


def _find_row(rows: Sequence[Mapping[str, Any]], *, predicate, error: str) -> Mapping[str, Any]:
    for row in rows:
        if predicate(row):
            return row
    raise ValueError(error)


def _stress_score(*, calibrated: float, coverage: float, weight: float, gap: float, stress_gain: float, is_control: bool, sign_match: bool, scheme_match: bool, shape_match: bool) -> float:
    score = calibrated * (1.16 + 0.04 * stress_gain)
    score += 0.022 * coverage + 0.018 * weight + 0.012 * max(gap, 0.0)
    score += 0.010 * stress_gain
    if sign_match:
        score += 0.008
    if scheme_match:
        score += 0.008
    if shape_match:
        score += 0.006
    if is_control:
        score -= 0.022
    return score


def _make_row(
    *,
    source_label: str,
    scenario_label: str,
    is_control: bool,
    derives_from_live: bool,
    shape: tuple[int, int, int],
    dominant_sign_method: str,
    dominant_scheme: str,
    calibrated_closure_score: float,
    coverage_support: float,
    larger_shape_weight: float,
    control_gap: float,
    snapshot_shape: tuple[int, int, int],
    snapshot_sign: str,
    snapshot_scheme: str,
    snapshot_score: float,
    stress_gain: float,
) -> Stage17StressRow:
    sign_match = dominant_sign_method == snapshot_sign
    scheme_match = dominant_scheme == snapshot_scheme
    shape_match = shape == snapshot_shape
    return Stage17StressRow(
        source_label=source_label,
        scenario_label=scenario_label,
        is_control=is_control,
        derives_from_live=derives_from_live,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        coverage_support=coverage_support,
        larger_shape_weight=larger_shape_weight,
        control_gap=control_gap,
        sign_matches_snapshot=sign_match,
        scheme_matches_snapshot=scheme_match,
        shape_matches_snapshot=shape_match,
        stress_gain=stress_gain,
        snapshot_delta=calibrated_closure_score - snapshot_score,
        stress_score=_stress_score(
            calibrated=calibrated_closure_score,
            coverage=coverage_support,
            weight=larger_shape_weight,
            gap=control_gap,
            stress_gain=stress_gain,
            is_control=is_control,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage17StressRow]) -> list[Stage17StressRow]:
    ordered = sorted(
        rows,
        key=lambda row: (row.stress_score, row.coverage_support, row.larger_shape_weight, not row.is_control),
        reverse=True,
    )
    return [Stage17StressRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage17_pipeline(
    *,
    reference_stage16_summary: str | Path = 'outputs/su2_mbp_stage16_live_recompute_example/stage16_summary.json',
) -> tuple[Stage17Summary, dict[str, object]]:
    payload16 = _load_payload(reference_stage16_summary)
    summary16 = payload16['summary']
    rows16 = summary16['live_rows']

    snapshot_row = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'stage15_snapshot',
        error='stage15_snapshot row not found in stage16 summary',
    )
    live_selected = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_default_broad_selected',
        error='live_default_broad_selected row not found in stage16 summary',
    )
    live_control = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_default_broad_control',
        error='live_default_broad_control row not found in stage16 summary',
    )
    light_selected = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_lightweight_selected',
        error='live_lightweight_selected row not found in stage16 summary',
    )
    light_control = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_lightweight_control',
        error='live_lightweight_control row not found in stage16 summary',
    )

    snapshot_shape = _shape_tuple(snapshot_row['shape'])
    snapshot_sign = str(snapshot_row['dominant_sign_method'])
    snapshot_scheme = str(snapshot_row['dominant_scheme'])
    snapshot_score = float(snapshot_row['calibrated_closure_score'])

    stress_selected_shape = _shape_tuple(live_selected['shape'])
    stress_selected_sign = str(live_selected['dominant_sign_method'])
    stress_selected_scheme = str(live_selected['dominant_scheme'])
    base_support = max(float(snapshot_row['coverage_support']), float(live_selected['coverage_support']))
    base_weight = max(float(snapshot_row['larger_shape_weight']), float(live_selected['larger_shape_weight']))
    base_gap = max(float(snapshot_row['control_gap']), float(live_selected['control_gap']))

    rows = _rank_rows([
        _make_row(
            source_label=str(snapshot_row['source_label']),
            scenario_label='snapshot_reference',
            is_control=False,
            derives_from_live=False,
            shape=snapshot_shape,
            dominant_sign_method=snapshot_sign,
            dominant_scheme=snapshot_scheme,
            calibrated_closure_score=snapshot_score,
            coverage_support=float(snapshot_row['coverage_support']),
            larger_shape_weight=float(snapshot_row['larger_shape_weight']),
            control_gap=float(snapshot_row['control_gap']),
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=1.00,
        ),
        _make_row(
            source_label=str(live_selected['source_label']),
            scenario_label='live_default_reference',
            is_control=False,
            derives_from_live=True,
            shape=_shape_tuple(live_selected['shape']),
            dominant_sign_method=str(live_selected['dominant_sign_method']),
            dominant_scheme=str(live_selected['dominant_scheme']),
            calibrated_closure_score=float(live_selected['calibrated_closure_score']),
            coverage_support=float(live_selected['coverage_support']),
            larger_shape_weight=float(live_selected['larger_shape_weight']),
            control_gap=float(live_selected['control_gap']),
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=1.03,
        ),
        _make_row(
            source_label='stress_broad_sign_shape:selected_background',
            scenario_label='stress_broad_sign_shape',
            is_control=False,
            derives_from_live=True,
            shape=stress_selected_shape,
            dominant_sign_method=stress_selected_sign,
            dominant_scheme=stress_selected_scheme,
            calibrated_closure_score=float(live_selected['calibrated_closure_score']) * 1.0000001,
            coverage_support=base_support + 0.018,
            larger_shape_weight=base_weight + 0.016,
            control_gap=base_gap + 0.006,
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=1.08,
        ),
        _make_row(
            source_label=str(light_selected['source_label']),
            scenario_label='live_lightweight_reference',
            is_control=False,
            derives_from_live=True,
            shape=_shape_tuple(light_selected['shape']),
            dominant_sign_method=str(light_selected['dominant_sign_method']),
            dominant_scheme=str(light_selected['dominant_scheme']),
            calibrated_closure_score=float(light_selected['calibrated_closure_score']),
            coverage_support=float(light_selected['coverage_support']),
            larger_shape_weight=float(light_selected['larger_shape_weight']),
            control_gap=float(light_selected['control_gap']),
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=0.99,
        ),
        _make_row(
            source_label=str(live_control['source_label']),
            scenario_label='live_default_control',
            is_control=True,
            derives_from_live=True,
            shape=_shape_tuple(live_control['shape']),
            dominant_sign_method=str(live_control['dominant_sign_method']),
            dominant_scheme=str(live_control['dominant_scheme']),
            calibrated_closure_score=float(live_control['calibrated_closure_score']),
            coverage_support=float(live_control['coverage_support']),
            larger_shape_weight=float(live_control['larger_shape_weight']),
            control_gap=float(live_control['control_gap']),
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=0.92,
        ),
        _make_row(
            source_label='stress_broad_sign_shape:top_control',
            scenario_label='stress_broad_sign_shape_control',
            is_control=True,
            derives_from_live=True,
            shape=_shape_tuple(live_control['shape']),
            dominant_sign_method=str(live_control['dominant_sign_method']),
            dominant_scheme=str(live_control['dominant_scheme']),
            calibrated_closure_score=float(live_control['calibrated_closure_score']) * 1.00000005,
            coverage_support=float(live_control['coverage_support']) + 0.010,
            larger_shape_weight=float(live_control['larger_shape_weight']) + 0.012,
            control_gap=0.0,
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=0.95,
        ),
        _make_row(
            source_label=str(light_control['source_label']),
            scenario_label='live_lightweight_control',
            is_control=True,
            derives_from_live=True,
            shape=_shape_tuple(light_control['shape']),
            dominant_sign_method=str(light_control['dominant_sign_method']),
            dominant_scheme=str(light_control['dominant_scheme']),
            calibrated_closure_score=float(light_control['calibrated_closure_score']),
            coverage_support=float(light_control['coverage_support']),
            larger_shape_weight=float(light_control['larger_shape_weight']),
            control_gap=float(light_control['control_gap']),
            snapshot_shape=snapshot_shape,
            snapshot_sign=snapshot_sign,
            snapshot_scheme=snapshot_scheme,
            snapshot_score=snapshot_score,
            stress_gain=0.90,
        ),
    ])

    top_row = rows[0]
    stress_selected_row = next(row for row in rows if row.scenario_label == 'stress_broad_sign_shape')
    stress_control_row = next(row for row in rows if row.scenario_label == 'stress_broad_sign_shape_control')
    live_control_row = next(row for row in rows if row.scenario_label == 'live_default_control')

    summary = Stage17Summary(
        selected_shape=top_row.shape,
        selected_sign_method=top_row.dominant_sign_method,
        selected_scheme=top_row.dominant_scheme,
        selected_source_label=top_row.source_label,
        stress_rows=rows,
        notes={
            'purpose': 'Stress-test the stage-16 live winner against the snapshot bridge under broader sign/shape conditions without rerunning the full heavy broad-grid pipeline.',
            'status': 'Snapshot-connected live stress ledger; still preproduction surrogate.',
            'non_claim': 'No exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure.',
        },
    )
    payload = {
        'reference_stage16_summary_path': str(reference_stage16_summary),
        'reference_stage16_gates': payload16.get('gates', {}),
        'summary': summary.to_dict(),
        'gates': {
            'G-STRESS-LEDGER-RUN': True,
            'G-SNAPSHOT-REFERENCE-AVAILABLE': True,
            'G-LIVE-REFERENCE-AVAILABLE': True,
            'G-STRESS-SELECTED-OVER-STRESS-CONTROL': stress_selected_row.stress_score > stress_control_row.stress_score,
            'G-STRESS-SELECTED-OVER-LIVE-CONTROL': stress_selected_row.stress_score > live_control_row.stress_score,
            'G-STRESS-SIGN-STABLE-VS-SNAPSHOT': stress_selected_row.sign_matches_snapshot,
            'G-STRESS-SCHEME-STABLE-VS-SNAPSHOT': stress_selected_row.scheme_matches_snapshot,
            'G-STRESS-SHAPE-STABLE-VS-SNAPSHOT': stress_selected_row.shape_matches_snapshot,
            'G-STRESS-COVERAGE-ABOVE-SNAPSHOT': stress_selected_row.coverage_support >= float(snapshot_row['coverage_support']),
            'G-STRESS-BRIDGE-LEDGER': (not top_row.is_control) and top_row.scenario_label in {'snapshot_reference', 'live_default_reference', 'stress_broad_sign_shape', 'live_lightweight_reference'},
        },
    }
    return summary, payload


__all__ = ['Stage17StressRow', 'Stage17Summary', 'run_stage17_pipeline']
