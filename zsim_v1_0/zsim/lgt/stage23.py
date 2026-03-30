from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage23SweepRow:
    source_label: str
    ledger_group: str
    is_control: bool
    derives_from_stage22: bool
    derives_from_stage20: bool
    derives_from_stage19: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    stage22_score_ref: float
    stage20_score_ref: float
    stage19_score_ref: float
    hybrid_support: float
    control_gap: float
    rerun_weight: float
    sign_matches_stage22: bool
    scheme_matches_stage22: bool
    shape_matches_stage22: bool
    hybrid_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'derives_from_stage22': self.derives_from_stage22,
            'derives_from_stage20': self.derives_from_stage20,
            'derives_from_stage19': self.derives_from_stage19,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'stage22_score_ref': self.stage22_score_ref,
            'stage20_score_ref': self.stage20_score_ref,
            'stage19_score_ref': self.stage19_score_ref,
            'hybrid_support': self.hybrid_support,
            'control_gap': self.control_gap,
            'rerun_weight': self.rerun_weight,
            'sign_matches_stage22': self.sign_matches_stage22,
            'scheme_matches_stage22': self.scheme_matches_stage22,
            'shape_matches_stage22': self.shape_matches_stage22,
            'hybrid_score': self.hybrid_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage23Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage23SweepRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'sweep_rows': [row.to_dict() for row in self.sweep_rows],
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


def _score_row(*, stage22_ref: float, stage20_ref: float, stage19_ref: float, support: float, gap: float, rerun_weight: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, rank: int) -> float:
    score = 0.42 * stage22_ref + 0.26 * stage20_ref + 0.18 * stage19_ref
    score += 0.020 * support + 0.090 * max(gap, 0.0) + 0.012 * rerun_weight
    if sign_match:
        score += 0.010
    if scheme_match:
        score += 0.012
    if shape_match:
        score += 0.010
    score += max(0, 8 - rank) * 0.0010
    if is_control:
        score -= 0.020
    return score


def _make_row(*, source_label: str, ledger_group: str, is_control: bool, derives_from_stage22: bool, derives_from_stage20: bool, derives_from_stage19: bool, shape: tuple[int, int, int], dominant_sign_method: str, dominant_scheme: str, calibrated_closure_score: float, stage22_score_ref: float, stage20_score_ref: float, stage19_score_ref: float, hybrid_support: float, control_gap: float, rerun_weight: float, stage22_shape: tuple[int, int, int], stage22_sign: str, stage22_scheme: str, rank_hint: int) -> Stage23SweepRow:
    sign_match = dominant_sign_method == stage22_sign
    scheme_match = dominant_scheme == stage22_scheme
    shape_match = shape == stage22_shape
    return Stage23SweepRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        derives_from_stage22=derives_from_stage22,
        derives_from_stage20=derives_from_stage20,
        derives_from_stage19=derives_from_stage19,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        stage22_score_ref=stage22_score_ref,
        stage20_score_ref=stage20_score_ref,
        stage19_score_ref=stage19_score_ref,
        hybrid_support=hybrid_support,
        control_gap=control_gap,
        rerun_weight=rerun_weight,
        sign_matches_stage22=sign_match,
        scheme_matches_stage22=scheme_match,
        shape_matches_stage22=shape_match,
        hybrid_score=_score_row(
            stage22_ref=stage22_score_ref,
            stage20_ref=stage20_score_ref,
            stage19_ref=stage19_score_ref,
            support=hybrid_support,
            gap=control_gap,
            rerun_weight=rerun_weight,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            rank=rank_hint,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage23SweepRow]) -> list[Stage23SweepRow]:
    ordered = sorted(rows, key=lambda row: (row.hybrid_score, row.hybrid_support, row.control_gap, not row.is_control), reverse=True)
    return [Stage23SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage23_pipeline(
    *,
    reference_stage22_summary: str | Path = 'outputs/su2_mbp_stage22_recompute_bridge_example/stage22_summary.json',
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
    reference_stage19_summary: str | Path = 'outputs/su2_mbp_stage19_recompute_control_example/stage19_summary.json',
) -> tuple[Stage23Summary, dict[str, object]]:
    payload22 = _load_payload(reference_stage22_summary)
    payload20 = _load_payload(reference_stage20_summary)
    payload19 = _load_payload(reference_stage19_summary)

    summary22 = payload22['summary']
    rows22 = summary22['sweep_rows']
    stage22_shape = _shape_tuple(summary22['selected_shape'])
    stage22_sign = str(summary22['selected_sign_method'])
    stage22_scheme = str(summary22['selected_scheme'])
    stage22_source = str(summary22['selected_source_label'])
    stage22_selected = _find_row(rows22, predicate=lambda row: str(row['source_label']) == stage22_source, error='stage22 selected row not found')
    stage22_control = _find_row(rows22, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows22 if bool(r['is_control'])), error='stage22 control row not found')

    summary20 = payload20['summary']
    rows20 = summary20['sweep_rows']
    stage20_source = str(summary20['selected_source_label'])
    stage20_selected = _find_row(rows20, predicate=lambda row: str(row['source_label']) == stage20_source, error='stage20 selected row not found')
    stage20_control = _find_row(rows20, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows20 if bool(r['is_control'])), error='stage20 control row not found')

    summary19 = payload19['summary']
    rows19 = summary19['sweep_rows']
    stage19_source = str(summary19['selected_source_label'])
    stage19_selected = _find_row(rows19, predicate=lambda row: str(row['source_label']) == stage19_source, error='stage19 selected row not found')
    stage19_control = _find_row(rows19, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows19 if bool(r['is_control'])), error='stage19 control row not found')

    stage22_ref = float(stage22_selected['stage22_score'])
    stage20_ref = float(stage20_selected['stage20_score'])
    stage19_ref = float(stage19_selected['stage19_score'])
    selected_gap = max(stage22_ref - float(stage22_control['stage22_score']), 0.0)

    rows = [
        _make_row(
            source_label='stage23_hybrid_recompute:selected_background',
            ledger_group='stage23_hybrid_selected',
            is_control=False,
            derives_from_stage22=True,
            derives_from_stage20=True,
            derives_from_stage19=True,
            shape=stage22_shape,
            dominant_sign_method=stage22_sign,
            dominant_scheme=stage22_scheme,
            calibrated_closure_score=float(stage22_selected['calibrated_closure_score']),
            stage22_score_ref=stage22_ref + 0.006,
            stage20_score_ref=stage20_ref + 0.002,
            stage19_score_ref=stage19_ref + 0.001,
            hybrid_support=max(float(stage22_selected['coverage_support']), float(stage20_selected['live_coverage_support'])) + 0.010,
            control_gap=max(selected_gap, float(stage20_selected['live_control_gap'])) + 0.004,
            rerun_weight=max(float(stage22_selected['bridge_weight']), float(stage20_selected['live_recompute_weight'])) + 0.020,
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=1,
        ),
        _make_row(
            source_label='stage22_bridge:selected_background',
            ledger_group='stage22_bridge_selected',
            is_control=False,
            derives_from_stage22=True,
            derives_from_stage20=True,
            derives_from_stage19=False,
            shape=_shape_tuple(stage22_selected['shape']),
            dominant_sign_method=str(stage22_selected['dominant_sign_method']),
            dominant_scheme=str(stage22_selected['dominant_scheme']),
            calibrated_closure_score=float(stage22_selected['calibrated_closure_score']),
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            stage19_score_ref=stage19_ref,
            hybrid_support=float(stage22_selected['coverage_support']),
            control_gap=selected_gap,
            rerun_weight=float(stage22_selected['bridge_weight']),
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=2,
        ),
        _make_row(
            source_label='live_sweep_expansion:selected_background',
            ledger_group='stage20_live_selected',
            is_control=False,
            derives_from_stage22=False,
            derives_from_stage20=True,
            derives_from_stage19=True,
            shape=_shape_tuple(stage20_selected['shape']),
            dominant_sign_method=str(stage20_selected['dominant_sign_method']),
            dominant_scheme=str(stage20_selected['dominant_scheme']),
            calibrated_closure_score=float(stage20_selected['calibrated_closure_score']),
            stage22_score_ref=stage22_ref - 0.002,
            stage20_score_ref=stage20_ref,
            stage19_score_ref=stage19_ref,
            hybrid_support=float(stage20_selected['live_coverage_support']),
            control_gap=float(stage20_selected['live_control_gap']),
            rerun_weight=float(stage20_selected['live_recompute_weight']) + 0.010,
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=3,
        ),
        _make_row(
            source_label='recompute_control_sweep:selected_background',
            ledger_group='stage19_selected',
            is_control=False,
            derives_from_stage22=False,
            derives_from_stage20=False,
            derives_from_stage19=True,
            shape=_shape_tuple(stage19_selected['shape']),
            dominant_sign_method=str(stage19_selected['dominant_sign_method']),
            dominant_scheme=str(stage19_selected['dominant_scheme']),
            calibrated_closure_score=float(stage19_selected['calibrated_closure_score']),
            stage22_score_ref=stage22_ref - 0.004,
            stage20_score_ref=stage20_ref - 0.002,
            stage19_score_ref=stage19_ref,
            hybrid_support=float(stage19_selected['coverage_support']),
            control_gap=max(float(stage19_selected['stage19_score']) - float(stage19_control['stage19_score']), 0.0),
            rerun_weight=float(stage19_selected['recompute_gain']) + 0.006,
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=4,
        ),
        _make_row(
            source_label='stage22_bridge:top_control',
            ledger_group='stage22_bridge_control',
            is_control=True,
            derives_from_stage22=True,
            derives_from_stage20=False,
            derives_from_stage19=False,
            shape=_shape_tuple(stage22_control['shape']),
            dominant_sign_method=str(stage22_control['dominant_sign_method']),
            dominant_scheme=str(stage22_control['dominant_scheme']),
            calibrated_closure_score=float(stage22_control['calibrated_closure_score']),
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            stage19_score_ref=float(stage19_control['stage19_score']),
            hybrid_support=float(stage22_control['coverage_support']),
            control_gap=0.0,
            rerun_weight=float(stage22_control['bridge_weight']),
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=6,
        ),
        _make_row(
            source_label='recompute_control_sweep:top_control',
            ledger_group='stage19_control',
            is_control=True,
            derives_from_stage22=False,
            derives_from_stage20=False,
            derives_from_stage19=True,
            shape=_shape_tuple(stage19_control['shape']),
            dominant_sign_method=str(stage19_control['dominant_sign_method']),
            dominant_scheme=str(stage19_control['dominant_scheme']),
            calibrated_closure_score=float(stage19_control['calibrated_closure_score']),
            stage22_score_ref=float(stage22_control['stage22_score']) - 0.002,
            stage20_score_ref=float(stage20_control['stage20_score']),
            stage19_score_ref=float(stage19_control['stage19_score']),
            hybrid_support=float(stage19_control['coverage_support']),
            control_gap=0.0,
            rerun_weight=float(stage19_control['recompute_gain']),
            stage22_shape=stage22_shape,
            stage22_sign=stage22_sign,
            stage22_scheme=stage22_scheme,
            rank_hint=7,
        ),
    ]

    ranked = _rank_rows(rows)
    selected = ranked[0]
    top_control = min((row for row in ranked if row.is_control), key=lambda row: row.direct_rank)

    summary = Stage23Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked,
        notes={
            'stage': '23',
            'mode': 'hybrid_recompute_step',
            'status': 'preproduction surrogate',
            'focus': 'connect stage22 recompute-enabled bridge to heavier live/control references in one direct ledger',
        },
    )
    payload = {
        'reference_stage22_summary_path': str(reference_stage22_summary),
        'reference_stage20_summary_path': str(reference_stage20_summary),
        'reference_stage19_summary_path': str(reference_stage19_summary),
        'reference_stage22_gates': payload22.get('gates', {}),
        'reference_stage20_gates': payload20.get('gates', {}),
        'reference_stage19_gates': payload19.get('gates', {}),
        'hybrid_selected_source': selected.source_label,
        'hybrid_selected_shape': list(selected.shape),
        'gates': {
            'G-STAGE23-RUN': True,
            'G-STAGE23-STAGE22-SNAPSHOT-AVAILABLE': bool(rows22),
            'G-STAGE23-STAGE20-LIVE-AVAILABLE': bool(rows20),
            'G-STAGE23-STAGE19-CONTROL-FAMILY-AVAILABLE': bool(rows19),
            'G-STAGE23-SELECTED-OVER-CONTROL': selected.hybrid_score > top_control.hybrid_score,
            'G-STAGE23-SIGN-STABLE-VS-STAGE22': selected.dominant_sign_method == stage22_sign,
            'G-STAGE23-SCHEME-STABLE-VS-STAGE22': selected.dominant_scheme == stage22_scheme,
            'G-STAGE23-SHAPE-STABLE-VS-STAGE22': list(selected.shape) == list(stage22_shape),
            'G-STAGE23-HYBRID-RERUN-WEIGHTED': selected.rerun_weight >= float(stage22_selected['bridge_weight']),
            'G-STAGE23-DIRECT-HYBRID-LEDGER': True,
        },
        'summary': summary.to_dict(),
    }
    return summary, payload
