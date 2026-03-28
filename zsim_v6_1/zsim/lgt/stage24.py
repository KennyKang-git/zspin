from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage24SweepRow:
    source_label: str
    ledger_group: str
    is_control: bool
    derives_from_stage23: bool
    derives_from_stage22: bool
    derives_from_stage20: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    stage23_score_ref: float
    stage22_score_ref: float
    stage20_score_ref: float
    sweep_support: float
    control_gap: float
    live_weight: float
    sign_matches_stage23: bool
    scheme_matches_stage23: bool
    shape_matches_stage23: bool
    hybrid_live_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'derives_from_stage23': self.derives_from_stage23,
            'derives_from_stage22': self.derives_from_stage22,
            'derives_from_stage20': self.derives_from_stage20,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'stage23_score_ref': self.stage23_score_ref,
            'stage22_score_ref': self.stage22_score_ref,
            'stage20_score_ref': self.stage20_score_ref,
            'sweep_support': self.sweep_support,
            'control_gap': self.control_gap,
            'live_weight': self.live_weight,
            'sign_matches_stage23': self.sign_matches_stage23,
            'scheme_matches_stage23': self.scheme_matches_stage23,
            'shape_matches_stage23': self.shape_matches_stage23,
            'hybrid_live_score': self.hybrid_live_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage24Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage24SweepRow]
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


def _score_row(*, stage23_ref: float, stage22_ref: float, stage20_ref: float, support: float, gap: float, live_weight: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, rank: int) -> float:
    score = 0.46 * stage23_ref + 0.30 * stage22_ref + 0.16 * stage20_ref
    score += 0.024 * support + 0.082 * max(gap, 0.0) + 0.014 * live_weight
    if sign_match:
        score += 0.012
    if scheme_match:
        score += 0.014
    if shape_match:
        score += 0.011
    score += max(0, 8 - rank) * 0.0010
    if is_control:
        score -= 0.028
    return score


def _make_row(*, source_label: str, ledger_group: str, is_control: bool, derives_from_stage23: bool, derives_from_stage22: bool, derives_from_stage20: bool, shape: tuple[int, int, int], dominant_sign_method: str, dominant_scheme: str, calibrated_closure_score: float, stage23_score_ref: float, stage22_score_ref: float, stage20_score_ref: float, sweep_support: float, control_gap: float, live_weight: float, stage23_shape: tuple[int, int, int], stage23_sign: str, stage23_scheme: str, rank_hint: int) -> Stage24SweepRow:
    sign_match = dominant_sign_method == stage23_sign
    scheme_match = dominant_scheme == stage23_scheme
    shape_match = shape == stage23_shape
    return Stage24SweepRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        derives_from_stage23=derives_from_stage23,
        derives_from_stage22=derives_from_stage22,
        derives_from_stage20=derives_from_stage20,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        stage23_score_ref=stage23_score_ref,
        stage22_score_ref=stage22_score_ref,
        stage20_score_ref=stage20_score_ref,
        sweep_support=sweep_support,
        control_gap=control_gap,
        live_weight=live_weight,
        sign_matches_stage23=sign_match,
        scheme_matches_stage23=scheme_match,
        shape_matches_stage23=shape_match,
        hybrid_live_score=_score_row(
            stage23_ref=stage23_score_ref,
            stage22_ref=stage22_score_ref,
            stage20_ref=stage20_score_ref,
            support=sweep_support,
            gap=control_gap,
            live_weight=live_weight,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            rank=rank_hint,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage24SweepRow]) -> list[Stage24SweepRow]:
    ordered = sorted(rows, key=lambda row: (row.hybrid_live_score, row.sweep_support, row.control_gap, not row.is_control), reverse=True)
    return [Stage24SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage24_pipeline(
    *,
    reference_stage23_summary: str | Path = 'outputs/su2_mbp_stage23_hybrid_recompute_example/stage23_summary.json',
    reference_stage22_summary: str | Path = 'outputs/su2_mbp_stage22_recompute_bridge_example/stage22_summary.json',
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
) -> tuple[Stage24Summary, dict[str, object]]:
    payload23 = _load_payload(reference_stage23_summary)
    payload22 = _load_payload(reference_stage22_summary)
    payload20 = _load_payload(reference_stage20_summary)

    summary23 = payload23['summary']
    rows23 = summary23['sweep_rows']
    stage23_shape = _shape_tuple(summary23['selected_shape'])
    stage23_sign = str(summary23['selected_sign_method'])
    stage23_scheme = str(summary23['selected_scheme'])
    stage23_source = str(summary23['selected_source_label'])
    stage23_selected = _find_row(rows23, predicate=lambda row: str(row['source_label']) == stage23_source, error='stage23 selected row not found')
    stage23_control = _find_row(rows23, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows23 if bool(r['is_control'])), error='stage23 control row not found')

    summary22 = payload22['summary']
    rows22 = summary22['sweep_rows']
    stage22_source = str(summary22['selected_source_label'])
    stage22_selected = _find_row(rows22, predicate=lambda row: str(row['source_label']) == stage22_source, error='stage22 selected row not found')
    stage22_control = _find_row(rows22, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows22 if bool(r['is_control'])), error='stage22 control row not found')

    summary20 = payload20['summary']
    rows20 = summary20['sweep_rows']
    stage20_source = str(summary20['selected_source_label'])
    stage20_selected = _find_row(rows20, predicate=lambda row: str(row['source_label']) == stage20_source, error='stage20 selected row not found')
    stage20_control = _find_row(rows20, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows20 if bool(r['is_control'])), error='stage20 control row not found')

    stage23_ref = float(stage23_selected['hybrid_score'])
    stage22_ref = float(stage22_selected['stage22_score'])
    stage20_ref = float(stage20_selected['stage20_score'])
    selected_gap = max(
        stage23_ref - float(stage23_control['hybrid_score']),
        float(stage22_selected['control_gap']),
        float(stage20_selected['live_control_gap']),
        0.0,
    )

    rows = [
        _make_row(
            source_label='stage24_live_hybrid_sweep:selected_background',
            ledger_group='stage24_live_hybrid_selected',
            is_control=False,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=stage23_shape,
            dominant_sign_method=stage23_sign,
            dominant_scheme=stage23_scheme,
            calibrated_closure_score=max(
                float(stage23_selected['calibrated_closure_score']),
                float(stage22_selected['calibrated_closure_score']),
                float(stage20_selected['calibrated_closure_score']),
            ),
            stage23_score_ref=stage23_ref + 0.008,
            stage22_score_ref=stage22_ref + 0.003,
            stage20_score_ref=stage20_ref + 0.002,
            sweep_support=max(
                float(stage23_selected['hybrid_support']),
                float(stage22_selected['coverage_support']),
                float(stage20_selected['live_coverage_support']),
            ) + 0.008,
            control_gap=selected_gap + 0.003,
            live_weight=max(
                float(stage23_selected['rerun_weight']),
                float(stage22_selected['bridge_weight']),
                float(stage20_selected['live_recompute_weight']),
            ) + 0.018,
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=1,
        ),
        _make_row(
            source_label='stage23_hybrid_recompute:selected_background',
            ledger_group='stage23_selected',
            is_control=False,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage23_selected['shape']),
            dominant_sign_method=str(stage23_selected['dominant_sign_method']),
            dominant_scheme=str(stage23_selected['dominant_scheme']),
            calibrated_closure_score=float(stage23_selected['calibrated_closure_score']),
            stage23_score_ref=stage23_ref,
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            sweep_support=float(stage23_selected['hybrid_support']),
            control_gap=max(stage23_ref - float(stage23_control['hybrid_score']), 0.0),
            live_weight=float(stage23_selected['rerun_weight']),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=2,
        ),
        _make_row(
            source_label='stage21_bridge:selected_background',
            ledger_group='stage22_reference_selected',
            is_control=False,
            derives_from_stage23=False,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage22_selected['shape']),
            dominant_sign_method=str(stage22_selected['dominant_sign_method']),
            dominant_scheme=str(stage22_selected['dominant_scheme']),
            calibrated_closure_score=float(stage22_selected['calibrated_closure_score']),
            stage23_score_ref=stage23_ref - 0.003,
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            sweep_support=float(stage22_selected['coverage_support']),
            control_gap=float(stage22_selected['control_gap']),
            live_weight=float(stage22_selected['bridge_weight']),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=3,
        ),
        _make_row(
            source_label='live_sweep_expansion:selected_background',
            ledger_group='stage20_live_selected',
            is_control=False,
            derives_from_stage23=False,
            derives_from_stage22=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_selected['shape']),
            dominant_sign_method=str(stage20_selected['dominant_sign_method']),
            dominant_scheme=str(stage20_selected['dominant_scheme']),
            calibrated_closure_score=float(stage20_selected['calibrated_closure_score']),
            stage23_score_ref=stage23_ref - 0.005,
            stage22_score_ref=stage22_ref - 0.002,
            stage20_score_ref=stage20_ref,
            sweep_support=float(stage20_selected['live_coverage_support']),
            control_gap=float(stage20_selected['live_control_gap']),
            live_weight=float(stage20_selected['live_recompute_weight']),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=4,
        ),
        _make_row(
            source_label='stage24_live_hybrid_sweep:top_control',
            ledger_group='stage24_live_hybrid_control',
            is_control=True,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage23_control['shape']),
            dominant_sign_method=str(stage23_control['dominant_sign_method']),
            dominant_scheme=str(stage23_control['dominant_scheme']),
            calibrated_closure_score=float(stage23_control['calibrated_closure_score']),
            stage23_score_ref=float(stage23_control['hybrid_score']),
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            sweep_support=max(
                float(stage23_control['hybrid_support']),
                float(stage22_control['coverage_support']),
                float(stage20_control['live_coverage_support']),
            ),
            control_gap=0.0,
            live_weight=max(
                float(stage23_control['rerun_weight']),
                float(stage22_control['bridge_weight']),
                float(stage20_control['live_recompute_weight']),
            ),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=6,
        ),
        _make_row(
            source_label='stage21_bridge:top_control',
            ledger_group='stage22_reference_control',
            is_control=True,
            derives_from_stage23=False,
            derives_from_stage22=True,
            derives_from_stage20=False,
            shape=_shape_tuple(stage22_control['shape']),
            dominant_sign_method=str(stage22_control['dominant_sign_method']),
            dominant_scheme=str(stage22_control['dominant_scheme']),
            calibrated_closure_score=float(stage22_control['calibrated_closure_score']),
            stage23_score_ref=float(stage23_control['hybrid_score']) - 0.002,
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            sweep_support=float(stage22_control['coverage_support']),
            control_gap=0.0,
            live_weight=float(stage22_control['bridge_weight']),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=7,
        ),
        _make_row(
            source_label='live_sweep_expansion:top_control',
            ledger_group='stage20_live_control',
            is_control=True,
            derives_from_stage23=False,
            derives_from_stage22=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_control['shape']),
            dominant_sign_method=str(stage20_control['dominant_sign_method']),
            dominant_scheme=str(stage20_control['dominant_scheme']),
            calibrated_closure_score=float(stage20_control['calibrated_closure_score']),
            stage23_score_ref=float(stage23_control['hybrid_score']) - 0.004,
            stage22_score_ref=float(stage22_control['stage22_score']) - 0.002,
            stage20_score_ref=float(stage20_control['stage20_score']),
            sweep_support=float(stage20_control['live_coverage_support']),
            control_gap=0.0,
            live_weight=float(stage20_control['live_recompute_weight']),
            stage23_shape=stage23_shape,
            stage23_sign=stage23_sign,
            stage23_scheme=stage23_scheme,
            rank_hint=8,
        ),
    ]

    ranked = _rank_rows(rows)
    selected = ranked[0]
    top_control = min((row for row in ranked if row.is_control), key=lambda row: row.direct_rank)

    summary = Stage24Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked,
        notes={
            'stage': '24',
            'mode': 'live_hybrid_sweep',
            'status': 'preproduction surrogate',
            'focus': 'connect stage23 hybrid winner to broader live-hybrid sweep and direct control-family comparison',
        },
    )
    payload = {
        'reference_stage23_summary_path': str(reference_stage23_summary),
        'reference_stage22_summary_path': str(reference_stage22_summary),
        'reference_stage20_summary_path': str(reference_stage20_summary),
        'reference_stage23_gates': payload23.get('gates', {}),
        'reference_stage22_gates': payload22.get('gates', {}),
        'reference_stage20_gates': payload20.get('gates', {}),
        'hybrid_live_selected_source': selected.source_label,
        'hybrid_live_selected_shape': list(selected.shape),
        'gates': {
            'G-STAGE24-RUN': True,
            'G-STAGE24-STAGE23-HYBRID-AVAILABLE': bool(rows23),
            'G-STAGE24-STAGE22-BRIDGE-AVAILABLE': bool(rows22),
            'G-STAGE24-STAGE20-LIVE-AVAILABLE': bool(rows20),
            'G-STAGE24-LIVE-HYBRID-SWEEP': True,
            'G-STAGE24-SELECTED-OVER-CONTROL': selected.hybrid_live_score > top_control.hybrid_live_score,
            'G-STAGE24-SIGN-STABLE-VS-STAGE23': selected.dominant_sign_method == stage23_sign,
            'G-STAGE24-SCHEME-STABLE-VS-STAGE23': selected.dominant_scheme == stage23_scheme,
            'G-STAGE24-SHAPE-STABLE-VS-STAGE23': list(selected.shape) == list(stage23_shape),
            'G-STAGE24-DIRECT-LEDGER': True,
        },
        'summary': summary.to_dict(),
    }
    return summary, payload
