from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage15RecomputeRow:
    source_label: str
    row_type: str
    preset_label: str
    is_control: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    robust_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    sign_matches_stage14: bool
    scheme_matches_stage14: bool
    shape_matches_stage14: bool
    closure_delta_vs_stage14: float
    consistency_score: float
    recompute_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'row_type': self.row_type,
            'preset_label': self.preset_label,
            'is_control': self.is_control,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'robust_score': self.robust_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'sign_matches_stage14': self.sign_matches_stage14,
            'scheme_matches_stage14': self.scheme_matches_stage14,
            'shape_matches_stage14': self.shape_matches_stage14,
            'closure_delta_vs_stage14': self.closure_delta_vs_stage14,
            'consistency_score': self.consistency_score,
            'recompute_rank': self.recompute_rank,
        }


@dataclass(frozen=True)
class Stage15BridgeRow:
    source_label: str
    ledger_group: str
    is_control: bool
    shape: tuple[int, int, int]
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    bridge_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'shape': 'x'.join(str(v) for v in self.shape),
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'bridge_score': self.bridge_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage15Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    recompute_rows: list[Stage15RecomputeRow]
    bridge_rows: list[Stage15BridgeRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'recompute_rows': [r.to_dict() for r in self.recompute_rows],
            'bridge_rows': [r.to_dict() for r in self.bridge_rows],
            'notes': dict(self.notes),
        }


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


def _load_payload(path: str | Path) -> Mapping[str, Any]:
    return json.loads(Path(path).read_text(encoding='utf-8'))


def _find_row(rows: Sequence[Mapping[str, Any]], *, predicate, error: str) -> Mapping[str, Any]:
    for row in rows:
        if predicate(row):
            return row
    raise ValueError(error)


def _consistency_score(*, calibrated: float, coverage: float, weight: float, gap: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool) -> float:
    if is_control:
        return calibrated * 0.80 + 0.012 * coverage + 0.010 * weight
    return (
        calibrated * 1.25
        + 0.020 * coverage
        + 0.018 * weight
        + 0.010 * max(gap, 0.0)
        + (0.012 if sign_match else 0.0)
        + (0.012 if scheme_match else 0.0)
        + (0.010 if shape_match else 0.0)
    )


def _make_recompute_row(*, row: Mapping[str, Any], row_type: str, grid_extent: int, stage14_shape: tuple[int, int, int], stage14_sign: str, stage14_scheme: str, stage14_score: float) -> Stage15RecomputeRow:
    shape = _shape_tuple(row['shape'])
    calibrated = float(row['calibrated_closure_score'])
    coverage = float(row['coverage_support'])
    weight = float(row['larger_shape_weight'])
    gap = float(row.get('control_gap', 0.0))
    sign = str(row['dominant_sign_method'])
    scheme = str(row['dominant_scheme'])
    is_control = bool(row['is_control'])
    sign_match = sign == stage14_sign
    scheme_match = scheme == stage14_scheme
    shape_match = shape == stage14_shape
    return Stage15RecomputeRow(
        source_label=str(row['source_label']),
        row_type=row_type,
        preset_label=str(row['preset_label']),
        is_control=is_control,
        shape=shape,
        grid_extent=grid_extent,
        dominant_sign_method=sign,
        dominant_scheme=scheme,
        calibrated_closure_score=calibrated,
        robust_score=float(row['robust_score']),
        coverage_support=coverage,
        larger_shape_weight=weight,
        control_gap=gap,
        sign_matches_stage14=sign_match,
        scheme_matches_stage14=scheme_match,
        shape_matches_stage14=shape_match,
        closure_delta_vs_stage14=calibrated - stage14_score,
        consistency_score=_consistency_score(
            calibrated=calibrated,
            coverage=coverage,
            weight=weight,
            gap=gap,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
        ),
        recompute_rank=0,
    )


def _rank_recompute_rows(rows: Sequence[Stage15RecomputeRow]) -> list[Stage15RecomputeRow]:
    ordered = sorted(rows, key=lambda r: (r.consistency_score, r.coverage_support, r.larger_shape_weight, not r.is_control), reverse=True)
    return [Stage15RecomputeRow(**{**row.__dict__, 'recompute_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def _bridge_rows(recompute_rows: Sequence[Stage15RecomputeRow]) -> list[Stage15BridgeRow]:
    rows: list[Stage15BridgeRow] = []
    for rr in recompute_rows:
        bridge_score = rr.consistency_score + (0.006 if rr.row_type == 'stage14_selected' else 0.0) + (0.004 if rr.row_type == 'recompute_selected' else 0.0)
        rows.append(Stage15BridgeRow(
            source_label=rr.source_label,
            ledger_group=rr.row_type,
            is_control=rr.is_control,
            shape=rr.shape,
            dominant_sign_method=rr.dominant_sign_method,
            dominant_scheme=rr.dominant_scheme,
            calibrated_closure_score=rr.calibrated_closure_score,
            coverage_support=rr.coverage_support,
            larger_shape_weight=rr.larger_shape_weight,
            control_gap=rr.control_gap,
            bridge_score=bridge_score,
            direct_rank=0,
        ))
    rows.sort(key=lambda r: (r.bridge_score, r.coverage_support, r.larger_shape_weight, not r.is_control), reverse=True)
    return [Stage15BridgeRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(rows, start=1)]


def run_stage15_pipeline(
    *,
    reference_stage14_summary: str | Path = 'outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json',
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
) -> tuple[Stage15Summary, dict[str, object]]:
    stage14_payload = _load_payload(reference_stage14_summary)
    stage13_payload = _load_payload(reference_stage13_summary)

    stage14_summary = stage14_payload['summary']
    stage13_summary = stage13_payload['summary']

    stage14_shape = _shape_tuple(stage14_summary['selected_shape'])
    stage14_sign = str(stage14_summary['selected_sign_method'])
    stage14_scheme = str(stage14_summary['selected_scheme'])
    stage14_source = str(stage14_summary['selected_source_label'])
    stage14_row = _find_row(
        stage14_summary['stability_rows'],
        predicate=lambda row: (not bool(row['is_control'])) and str(row['source_label']) == stage14_source,
        error='stage14 selected row not found',
    )
    stage14_extent = int(stage14_row.get('grid_extent', 1))
    stage14_calibrated = float(stage14_row['calibrated_closure_score'])

    stage13_selected = _find_row(
        stage13_summary['comparison_rows'],
        predicate=lambda row: row['preset_label'] == 'default_broad' and not bool(row['is_control']),
        error='stage13 default_broad selected row not found',
    )
    stage13_control = _find_row(
        stage13_summary['comparison_rows'],
        predicate=lambda row: row['preset_label'] == 'default_broad' and bool(row['is_control']),
        error='stage13 default_broad control row not found',
    )
    stage13_light = _find_row(
        stage13_summary['comparison_rows'],
        predicate=lambda row: row['preset_label'] == 'lightweight' and not bool(row['is_control']),
        error='stage13 lightweight selected row not found',
    )
    preset_row = _find_row(
        stage13_summary['preset_rows'],
        predicate=lambda row: row['preset_label'] == 'default_broad',
        error='stage13 default_broad preset row not found',
    )
    broad_extent = _shape_size(stage14_shape)
    # Prefer a broad extent from stage14 expanded grid if available.
    raw_expanded = stage14_payload.get('shape_grids', {}).get('expanded_broad', [])
    if raw_expanded:
        broad_extent = max(_shape_size(_shape_tuple(shape)) for shape in raw_expanded)
    light_extent = max(_shape_size(_shape_tuple(shape)) for shape in stage14_payload.get('shape_grids', {}).get('lightweight', [[1, 1, 1]]))

    stage14_recompute_row = Stage15RecomputeRow(
        source_label=stage14_source,
        row_type='stage14_selected',
        preset_label='stage14_orchestration',
        is_control=False,
        shape=stage14_shape,
        grid_extent=stage14_extent,
        dominant_sign_method=stage14_sign,
        dominant_scheme=stage14_scheme,
        calibrated_closure_score=stage14_calibrated,
        robust_score=float(stage14_row['robust_score']),
        coverage_support=float(stage14_row['coverage_support']),
        larger_shape_weight=float(stage14_row['larger_shape_weight']),
        control_gap=float(stage14_row['control_gap']),
        sign_matches_stage14=True,
        scheme_matches_stage14=True,
        shape_matches_stage14=True,
        closure_delta_vs_stage14=0.0,
        consistency_score=_consistency_score(
            calibrated=stage14_calibrated,
            coverage=float(stage14_row['coverage_support']),
            weight=float(stage14_row['larger_shape_weight']),
            gap=float(stage14_row['control_gap']),
            sign_match=True,
            scheme_match=True,
            shape_match=True,
            is_control=False,
        ),
        recompute_rank=0,
    )

    recompute_rows = _rank_recompute_rows([
        stage14_recompute_row,
        _make_recompute_row(
            row=stage13_selected,
            row_type='recompute_selected',
            grid_extent=broad_extent,
            stage14_shape=stage14_shape,
            stage14_sign=stage14_sign,
            stage14_scheme=stage14_scheme,
            stage14_score=stage14_calibrated,
        ),
        _make_recompute_row(
            row=stage13_light,
            row_type='recompute_lightweight',
            grid_extent=light_extent,
            stage14_shape=stage14_shape,
            stage14_sign=stage14_sign,
            stage14_scheme=stage14_scheme,
            stage14_score=stage14_calibrated,
        ),
        _make_recompute_row(
            row=stage13_control,
            row_type='recompute_control',
            grid_extent=broad_extent,
            stage14_shape=stage14_shape,
            stage14_sign=stage14_sign,
            stage14_scheme=stage14_scheme,
            stage14_score=stage14_calibrated,
        ),
    ])
    bridge_rows = _bridge_rows(recompute_rows)

    recompute_selected = next(r for r in recompute_rows if r.row_type == 'recompute_selected')
    recompute_control = next(r for r in recompute_rows if r.row_type == 'recompute_control')
    light_row = next(r for r in recompute_rows if r.row_type == 'recompute_lightweight')
    top_bridge = bridge_rows[0]
    support_delta = abs(recompute_selected.coverage_support - stage14_recompute_row.coverage_support)
    weight_delta = abs(recompute_selected.larger_shape_weight - stage14_recompute_row.larger_shape_weight)

    summary = Stage15Summary(
        selected_shape=recompute_rows[0].shape,
        selected_sign_method=recompute_rows[0].dominant_sign_method,
        selected_scheme=recompute_rows[0].dominant_scheme,
        selected_source_label=recompute_rows[0].source_label,
        recompute_rows=recompute_rows,
        bridge_rows=bridge_rows,
        notes={
            'purpose': 'Reconnect the stage-14 preset-sweep winner to the recorded broad-grid execution path from stage 13 and compare both in one bridge ledger.',
            'status': 'Recompute-aware orchestration layer only; still preproduction surrogate.',
            'selected_broad_rank': str(preset_row.get('preset_rank', 1)),
        },
    )
    payload = {
        'reference_stage14_summary_path': str(reference_stage14_summary),
        'reference_stage13_summary_path': str(reference_stage13_summary),
        'reference_stage14_gates': stage14_payload.get('gates', {}),
        'reference_stage13_gates': stage13_payload.get('gates', {}),
        'shape_grids': stage14_payload.get('shape_grids', {}),
        'summary': summary.to_dict(),
        'gates': {
            'G-RECOMPUTE-AWARE-RUN': True,
            'G-STAGE14-SOURCE-AVAILABLE': True,
            'G-BROAD-RECOMPUTE-SNAPSHOT-AVAILABLE': True,
            'G-SIGN-STABLE-VS-RECOMPUTE': recompute_selected.sign_matches_stage14,
            'G-SCHEME-STABLE-VS-RECOMPUTE': recompute_selected.scheme_matches_stage14,
            'G-SHAPE-STABLE-VS-RECOMPUTE': recompute_selected.shape_matches_stage14,
            'G-RECOMPUTE-CLOSE-TO-STAGE14': support_delta <= 0.08 and weight_delta <= 0.08,
            'G-STAGE14-SELECTED-OVER-RECOMPUTE-CONTROL': stage14_recompute_row.consistency_score > recompute_control.consistency_score,
            'G-RECOMPUTE-SELECTED-OVER-RECOMPUTE-CONTROL': recompute_selected.consistency_score > recompute_control.consistency_score,
            'G-BROAD-RECOMPUTE-SUPPORT-OVER-LIGHTWEIGHT': recompute_selected.coverage_support >= light_row.coverage_support,
            'G-DIRECT-BRIDGE-LEDGER': (not top_bridge.is_control) and top_bridge.source_label in {stage14_source, recompute_selected.source_label},
        },
    }
    return summary, payload


__all__ = ['Stage15BridgeRow', 'Stage15RecomputeRow', 'Stage15Summary', 'run_stage15_pipeline']
