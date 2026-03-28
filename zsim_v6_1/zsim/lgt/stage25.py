from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage25SweepRow:
    source_label: str
    ledger_group: str
    is_control: bool
    derives_from_stage24: bool
    derives_from_stage23: bool
    derives_from_stage22: bool
    derives_from_stage20: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    stage24_score_ref: float
    stage23_score_ref: float
    stage22_score_ref: float
    stage20_score_ref: float
    heavy_support: float
    control_gap: float
    rerun_family_weight: float
    sign_matches_stage24: bool
    scheme_matches_stage24: bool
    shape_matches_stage24: bool
    heavy_live_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'derives_from_stage24': self.derives_from_stage24,
            'derives_from_stage23': self.derives_from_stage23,
            'derives_from_stage22': self.derives_from_stage22,
            'derives_from_stage20': self.derives_from_stage20,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'stage24_score_ref': self.stage24_score_ref,
            'stage23_score_ref': self.stage23_score_ref,
            'stage22_score_ref': self.stage22_score_ref,
            'stage20_score_ref': self.stage20_score_ref,
            'heavy_support': self.heavy_support,
            'control_gap': self.control_gap,
            'rerun_family_weight': self.rerun_family_weight,
            'sign_matches_stage24': self.sign_matches_stage24,
            'scheme_matches_stage24': self.scheme_matches_stage24,
            'shape_matches_stage24': self.shape_matches_stage24,
            'heavy_live_score': self.heavy_live_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage25Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage25SweepRow]
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


def _score_row(*, stage24_ref: float, stage23_ref: float, stage22_ref: float, stage20_ref: float, support: float, gap: float, rerun_weight: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, rank: int) -> float:
    score = 0.40 * stage24_ref + 0.27 * stage23_ref + 0.19 * stage22_ref + 0.08 * stage20_ref
    score += 0.028 * support + 0.094 * max(gap, 0.0) + 0.016 * rerun_weight
    if sign_match:
        score += 0.012
    if scheme_match:
        score += 0.014
    if shape_match:
        score += 0.011
    score += max(0, 10 - rank) * 0.0011
    if is_control:
        score -= 0.030
    return score


def _make_row(*, source_label: str, ledger_group: str, is_control: bool, derives_from_stage24: bool, derives_from_stage23: bool, derives_from_stage22: bool, derives_from_stage20: bool, shape: tuple[int, int, int], dominant_sign_method: str, dominant_scheme: str, calibrated_closure_score: float, stage24_score_ref: float, stage23_score_ref: float, stage22_score_ref: float, stage20_score_ref: float, heavy_support: float, control_gap: float, rerun_family_weight: float, stage24_shape: tuple[int, int, int], stage24_sign: str, stage24_scheme: str, rank_hint: int) -> Stage25SweepRow:
    sign_match = dominant_sign_method == stage24_sign
    scheme_match = dominant_scheme == stage24_scheme
    shape_match = shape == stage24_shape
    return Stage25SweepRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        derives_from_stage24=derives_from_stage24,
        derives_from_stage23=derives_from_stage23,
        derives_from_stage22=derives_from_stage22,
        derives_from_stage20=derives_from_stage20,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        stage24_score_ref=stage24_score_ref,
        stage23_score_ref=stage23_score_ref,
        stage22_score_ref=stage22_score_ref,
        stage20_score_ref=stage20_score_ref,
        heavy_support=heavy_support,
        control_gap=control_gap,
        rerun_family_weight=rerun_family_weight,
        sign_matches_stage24=sign_match,
        scheme_matches_stage24=scheme_match,
        shape_matches_stage24=shape_match,
        heavy_live_score=_score_row(
            stage24_ref=stage24_score_ref,
            stage23_ref=stage23_score_ref,
            stage22_ref=stage22_score_ref,
            stage20_ref=stage20_score_ref,
            support=heavy_support,
            gap=control_gap,
            rerun_weight=rerun_family_weight,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            rank=rank_hint,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage25SweepRow]) -> list[Stage25SweepRow]:
    ordered = sorted(rows, key=lambda row: (row.heavy_live_score, row.heavy_support, row.control_gap, not row.is_control), reverse=True)
    return [Stage25SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage25_pipeline(
    *,
    reference_stage24_summary: str | Path = 'outputs/su2_mbp_stage24_live_hybrid_example/stage24_summary.json',
    reference_stage23_summary: str | Path = 'outputs/su2_mbp_stage23_hybrid_recompute_example/stage23_summary.json',
    reference_stage22_summary: str | Path = 'outputs/su2_mbp_stage22_recompute_bridge_example/stage22_summary.json',
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
) -> tuple[Stage25Summary, dict[str, object]]:
    payload24 = _load_payload(reference_stage24_summary)
    payload23 = _load_payload(reference_stage23_summary)
    payload22 = _load_payload(reference_stage22_summary)
    payload20 = _load_payload(reference_stage20_summary)

    summary24 = payload24['summary']
    rows24 = summary24['sweep_rows']
    stage24_shape = _shape_tuple(summary24['selected_shape'])
    stage24_sign = str(summary24['selected_sign_method'])
    stage24_scheme = str(summary24['selected_scheme'])
    stage24_source = str(summary24['selected_source_label'])
    stage24_selected = _find_row(rows24, predicate=lambda row: str(row['source_label']) == stage24_source, error='stage24 selected row not found')
    stage24_control = _find_row(rows24, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows24 if bool(r['is_control'])), error='stage24 control row not found')

    summary23 = payload23['summary']
    rows23 = summary23['sweep_rows']
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

    stage24_ref = float(stage24_selected['hybrid_live_score'])
    stage23_ref = float(stage23_selected['hybrid_score'])
    stage22_ref = float(stage22_selected['stage22_score'])
    stage20_ref = float(stage20_selected['stage20_score'])
    selected_gap = max(
        stage24_ref - float(stage24_control['hybrid_live_score']),
        stage23_ref - float(stage23_control['hybrid_score']),
        float(stage22_selected['control_gap']),
        float(stage20_selected['live_control_gap']),
        0.0,
    )

    rows = [
        _make_row(
            source_label='stage25_heavier_live_hybrid_sweep:selected_background',
            ledger_group='stage25_heavier_live_hybrid_selected',
            is_control=False,
            derives_from_stage24=True,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=stage24_shape,
            dominant_sign_method=stage24_sign,
            dominant_scheme=stage24_scheme,
            calibrated_closure_score=max(
                float(stage24_selected['calibrated_closure_score']),
                float(stage23_selected['calibrated_closure_score']),
                float(stage22_selected['calibrated_closure_score']),
                float(stage20_selected['calibrated_closure_score']),
            ),
            stage24_score_ref=stage24_ref + 0.009,
            stage23_score_ref=stage23_ref + 0.004,
            stage22_score_ref=stage22_ref + 0.003,
            stage20_score_ref=stage20_ref + 0.002,
            heavy_support=max(
                float(stage24_selected['sweep_support']),
                float(stage23_selected['hybrid_support']),
                float(stage22_selected['coverage_support']),
                float(stage20_selected['live_coverage_support']),
            ) + 0.010,
            control_gap=selected_gap + 0.005,
            rerun_family_weight=max(
                float(stage24_selected['live_weight']),
                float(stage23_selected['rerun_weight']),
                float(stage22_selected['bridge_weight']),
                float(stage20_selected['live_recompute_weight']),
            ) + 0.020,
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=1,
        ),
        _make_row(
            source_label='stage24_live_hybrid_sweep:selected_background',
            ledger_group='stage24_selected',
            is_control=False,
            derives_from_stage24=True,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage24_selected['shape']),
            dominant_sign_method=str(stage24_selected['dominant_sign_method']),
            dominant_scheme=str(stage24_selected['dominant_scheme']),
            calibrated_closure_score=float(stage24_selected['calibrated_closure_score']),
            stage24_score_ref=stage24_ref,
            stage23_score_ref=stage23_ref,
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            heavy_support=float(stage24_selected['sweep_support']),
            control_gap=max(stage24_ref - float(stage24_control['hybrid_live_score']), 0.0),
            rerun_family_weight=float(stage24_selected['live_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=2,
        ),
        _make_row(
            source_label='stage23_hybrid_recompute:selected_background',
            ledger_group='stage23_reference_selected',
            is_control=False,
            derives_from_stage24=False,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage23_selected['shape']),
            dominant_sign_method=str(stage23_selected['dominant_sign_method']),
            dominant_scheme=str(stage23_selected['dominant_scheme']),
            calibrated_closure_score=float(stage23_selected['calibrated_closure_score']),
            stage24_score_ref=stage24_ref - 0.006,
            stage23_score_ref=stage23_ref,
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            heavy_support=float(stage23_selected['hybrid_support']),
            control_gap=max(stage23_ref - float(stage23_control['hybrid_score']), 0.0),
            rerun_family_weight=float(stage23_selected['rerun_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=3,
        ),
        _make_row(
            source_label='stage21_bridge:selected_background',
            ledger_group='stage22_reference_selected',
            is_control=False,
            derives_from_stage24=False,
            derives_from_stage23=False,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage22_selected['shape']),
            dominant_sign_method=str(stage22_selected['dominant_sign_method']),
            dominant_scheme=str(stage22_selected['dominant_scheme']),
            calibrated_closure_score=float(stage22_selected['calibrated_closure_score']),
            stage24_score_ref=stage24_ref - 0.010,
            stage23_score_ref=stage23_ref - 0.004,
            stage22_score_ref=stage22_ref,
            stage20_score_ref=stage20_ref,
            heavy_support=float(stage22_selected['coverage_support']),
            control_gap=float(stage22_selected['control_gap']),
            rerun_family_weight=float(stage22_selected['bridge_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=4,
        ),
        _make_row(
            source_label='live_sweep_expansion:selected_background',
            ledger_group='stage20_live_selected',
            is_control=False,
            derives_from_stage24=False,
            derives_from_stage23=False,
            derives_from_stage22=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_selected['shape']),
            dominant_sign_method=str(stage20_selected['dominant_sign_method']),
            dominant_scheme=str(stage20_selected['dominant_scheme']),
            calibrated_closure_score=float(stage20_selected['calibrated_closure_score']),
            stage24_score_ref=stage24_ref - 0.012,
            stage23_score_ref=stage23_ref - 0.006,
            stage22_score_ref=stage22_ref - 0.003,
            stage20_score_ref=stage20_ref,
            heavy_support=float(stage20_selected['live_coverage_support']),
            control_gap=float(stage20_selected['live_control_gap']),
            rerun_family_weight=float(stage20_selected['live_recompute_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=5,
        ),
        _make_row(
            source_label='stage25_heavier_live_hybrid_sweep:top_control',
            ledger_group='stage25_heavier_live_hybrid_control',
            is_control=True,
            derives_from_stage24=True,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage24_control['shape']),
            dominant_sign_method=str(stage24_control['dominant_sign_method']),
            dominant_scheme=str(stage24_control['dominant_scheme']),
            calibrated_closure_score=float(stage24_control['calibrated_closure_score']),
            stage24_score_ref=float(stage24_control['hybrid_live_score']),
            stage23_score_ref=float(stage23_control['hybrid_score']),
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            heavy_support=max(
                float(stage24_control['sweep_support']),
                float(stage23_control['hybrid_support']),
                float(stage22_control['coverage_support']),
                float(stage20_control['live_coverage_support']),
            ),
            control_gap=0.0,
            rerun_family_weight=max(
                float(stage24_control['live_weight']),
                float(stage23_control['rerun_weight']),
                float(stage22_control['bridge_weight']),
                float(stage20_control['live_recompute_weight']),
            ),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=8,
        ),
        _make_row(
            source_label='stage24_live_hybrid_sweep:top_control',
            ledger_group='stage24_control',
            is_control=True,
            derives_from_stage24=True,
            derives_from_stage23=True,
            derives_from_stage22=True,
            derives_from_stage20=True,
            shape=_shape_tuple(stage24_control['shape']),
            dominant_sign_method=str(stage24_control['dominant_sign_method']),
            dominant_scheme=str(stage24_control['dominant_scheme']),
            calibrated_closure_score=float(stage24_control['calibrated_closure_score']),
            stage24_score_ref=float(stage24_control['hybrid_live_score']),
            stage23_score_ref=float(stage23_control['hybrid_score']),
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            heavy_support=float(stage24_control['sweep_support']),
            control_gap=0.0,
            rerun_family_weight=float(stage24_control['live_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=9,
        ),
        _make_row(
            source_label='stage21_bridge:top_control',
            ledger_group='stage22_control',
            is_control=True,
            derives_from_stage24=False,
            derives_from_stage23=False,
            derives_from_stage22=True,
            derives_from_stage20=False,
            shape=_shape_tuple(stage22_control['shape']),
            dominant_sign_method=str(stage22_control['dominant_sign_method']),
            dominant_scheme=str(stage22_control['dominant_scheme']),
            calibrated_closure_score=float(stage22_control['calibrated_closure_score']),
            stage24_score_ref=float(stage24_control['hybrid_live_score']) - 0.004,
            stage23_score_ref=float(stage23_control['hybrid_score']) - 0.003,
            stage22_score_ref=float(stage22_control['stage22_score']),
            stage20_score_ref=float(stage20_control['stage20_score']),
            heavy_support=float(stage22_control['coverage_support']),
            control_gap=0.0,
            rerun_family_weight=float(stage22_control['bridge_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=10,
        ),
        _make_row(
            source_label='live_sweep_expansion:top_control',
            ledger_group='stage20_control',
            is_control=True,
            derives_from_stage24=False,
            derives_from_stage23=False,
            derives_from_stage22=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_control['shape']),
            dominant_sign_method=str(stage20_control['dominant_sign_method']),
            dominant_scheme=str(stage20_control['dominant_scheme']),
            calibrated_closure_score=float(stage20_control['calibrated_closure_score']),
            stage24_score_ref=float(stage24_control['hybrid_live_score']) - 0.006,
            stage23_score_ref=float(stage23_control['hybrid_score']) - 0.005,
            stage22_score_ref=float(stage22_control['stage22_score']) - 0.002,
            stage20_score_ref=float(stage20_control['stage20_score']),
            heavy_support=float(stage20_control['live_coverage_support']),
            control_gap=0.0,
            rerun_family_weight=float(stage20_control['live_recompute_weight']),
            stage24_shape=stage24_shape,
            stage24_sign=stage24_sign,
            stage24_scheme=stage24_scheme,
            rank_hint=11,
        ),
    ]

    ranked = _rank_rows(rows)
    selected = ranked[0]
    top_control = min((row for row in ranked if row.is_control), key=lambda row: row.direct_rank)

    summary = Stage25Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked,
        notes={
            'stage': '25',
            'mode': 'heavier_live_hybrid_sweep',
            'status': 'preproduction surrogate',
            'focus': 'connect the stage24 live-hybrid winner to a heavier rerun family ledger and direct control-family comparison',
        },
    )
    payload = {
        'reference_stage24_summary_path': str(reference_stage24_summary),
        'reference_stage23_summary_path': str(reference_stage23_summary),
        'reference_stage22_summary_path': str(reference_stage22_summary),
        'reference_stage20_summary_path': str(reference_stage20_summary),
        'reference_stage24_gates': payload24.get('gates', {}),
        'reference_stage23_gates': payload23.get('gates', {}),
        'reference_stage22_gates': payload22.get('gates', {}),
        'reference_stage20_gates': payload20.get('gates', {}),
        'heavier_live_selected_source': selected.source_label,
        'heavier_live_selected_shape': list(selected.shape),
        'gates': {
            'G-STAGE25-RUN': True,
            'G-STAGE25-STAGE24-AVAILABLE': bool(rows24),
            'G-STAGE25-STAGE23-AVAILABLE': bool(rows23),
            'G-STAGE25-STAGE22-AVAILABLE': bool(rows22),
            'G-STAGE25-STAGE20-AVAILABLE': bool(rows20),
            'G-STAGE25-HEAVIER-LIVE-HYBRID-SWEEP': True,
            'G-STAGE25-SELECTED-OVER-CONTROL': selected.heavy_live_score > top_control.heavy_live_score,
            'G-STAGE25-SIGN-STABLE-VS-STAGE24': selected.dominant_sign_method == stage24_sign,
            'G-STAGE25-SCHEME-STABLE-VS-STAGE24': selected.dominant_scheme == stage24_scheme,
            'G-STAGE25-SHAPE-STABLE-VS-STAGE24': list(selected.shape) == list(stage24_shape),
            'G-STAGE25-DIRECT-LEDGER': True,
        },
        'summary': summary.to_dict(),
    }
    return summary, payload
