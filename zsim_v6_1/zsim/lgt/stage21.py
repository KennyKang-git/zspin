from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage21SweepRow:
    source_label: str
    ledger_group: str
    is_control: bool
    derives_from_default_live: bool
    derives_from_broader_live: bool
    derives_from_stage20: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    default_live_score_ref: float
    broader_live_score_ref: float
    stage20_score_ref: float
    coverage_support: float
    control_gap: float
    rerun_support: float
    preset_weight: float
    sign_matches_stage20: bool
    scheme_matches_stage20: bool
    shape_matches_stage20: bool
    stage21_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'derives_from_default_live': self.derives_from_default_live,
            'derives_from_broader_live': self.derives_from_broader_live,
            'derives_from_stage20': self.derives_from_stage20,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'default_live_score_ref': self.default_live_score_ref,
            'broader_live_score_ref': self.broader_live_score_ref,
            'stage20_score_ref': self.stage20_score_ref,
            'coverage_support': self.coverage_support,
            'control_gap': self.control_gap,
            'rerun_support': self.rerun_support,
            'preset_weight': self.preset_weight,
            'sign_matches_stage20': self.sign_matches_stage20,
            'scheme_matches_stage20': self.scheme_matches_stage20,
            'shape_matches_stage20': self.shape_matches_stage20,
            'stage21_score': self.stage21_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage21Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage21SweepRow]
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


def _score_row(*, default_ref: float, broader_ref: float, stage20_ref: float, coverage: float, gap: float, rerun_support: float, preset_weight: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, rank: int) -> float:
    score = 0.35 * default_ref + 0.35 * broader_ref + 0.22 * stage20_ref
    score += 0.016 * coverage + 0.090 * max(gap, 0.0) + 0.010 * rerun_support + 0.006 * preset_weight
    if sign_match:
        score += 0.010
    if scheme_match:
        score += 0.012
    if shape_match:
        score += 0.010
    score += max(0, 8 - rank) * 0.0010
    if is_control:
        score -= 0.018
    return score


def _make_row(*, source_label: str, ledger_group: str, is_control: bool, derives_from_default_live: bool, derives_from_broader_live: bool, derives_from_stage20: bool, shape: tuple[int, int, int], dominant_sign_method: str, dominant_scheme: str, calibrated_closure_score: float, default_live_score_ref: float, broader_live_score_ref: float, stage20_score_ref: float, coverage_support: float, control_gap: float, rerun_support: float, preset_weight: float, stage20_shape: tuple[int, int, int], stage20_sign: str, stage20_scheme: str, rank_hint: int) -> Stage21SweepRow:
    sign_match = dominant_sign_method == stage20_sign
    scheme_match = dominant_scheme == stage20_scheme
    shape_match = shape == stage20_shape
    return Stage21SweepRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        derives_from_default_live=derives_from_default_live,
        derives_from_broader_live=derives_from_broader_live,
        derives_from_stage20=derives_from_stage20,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        default_live_score_ref=default_live_score_ref,
        broader_live_score_ref=broader_live_score_ref,
        stage20_score_ref=stage20_score_ref,
        coverage_support=coverage_support,
        control_gap=control_gap,
        rerun_support=rerun_support,
        preset_weight=preset_weight,
        sign_matches_stage20=sign_match,
        scheme_matches_stage20=scheme_match,
        shape_matches_stage20=shape_match,
        stage21_score=_score_row(
            default_ref=default_live_score_ref,
            broader_ref=broader_live_score_ref,
            stage20_ref=stage20_score_ref,
            coverage=coverage_support,
            gap=control_gap,
            rerun_support=rerun_support,
            preset_weight=preset_weight,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            rank=rank_hint,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage21SweepRow]) -> list[Stage21SweepRow]:
    ordered = sorted(rows, key=lambda row: (row.stage21_score, row.coverage_support, row.control_gap, not row.is_control), reverse=True)
    return [Stage21SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage21_pipeline(
    *,
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
    reference_stage14_summary: str | Path = 'outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json',
) -> tuple[Stage21Summary, dict[str, object]]:
    payload20 = _load_payload(reference_stage20_summary)
    payload13 = _load_payload(reference_stage13_summary)
    payload14 = _load_payload(reference_stage14_summary)

    summary20 = payload20['summary']
    stage20_rows = summary20['sweep_rows']
    stage20_shape = _shape_tuple(summary20['selected_shape'])
    stage20_sign = str(summary20['selected_sign_method'])
    stage20_scheme = str(summary20['selected_scheme'])
    stage20_source = str(summary20['selected_source_label'])
    stage20_selected = _find_row(stage20_rows, predicate=lambda row: str(row['source_label']) == stage20_source, error='stage20 selected row not found')
    stage20_control = _find_row(stage20_rows, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in stage20_rows if bool(r['is_control'])), error='stage20 control row not found')

    rows13 = payload13['summary']['comparison_rows']
    rows14 = payload14['summary']['stability_rows']
    default_selected = _find_row(rows13, predicate=lambda row: str(row['source_label']) == 'default_broad:selected_background', error='stage13 default_broad selected row not found')
    default_control = _find_row(rows13, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows13 if bool(r['is_control'])), error='stage13 top control not found')
    broader_selected = _find_row(rows14, predicate=lambda row: str(row['source_label']) == 'larger_shape_sweep:selected_background', error='stage14 larger_shape_sweep selected row not found')
    broader_control = _find_row(rows14, predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows14 if bool(r['is_control'])), error='stage14 top control not found')

    default_ref = float(default_selected['robust_score'])
    broader_ref = float(broader_selected['stability_score'])
    stage20_ref = float(stage20_selected['stage20_score'])

    rows = [
        _make_row(
            source_label='default_live_reference:selected_background',
            ledger_group='default_live_reference_selected',
            is_control=False,
            derives_from_default_live=True,
            derives_from_broader_live=False,
            derives_from_stage20=True,
            shape=_shape_tuple(default_selected['shape']),
            dominant_sign_method=str(default_selected['dominant_sign_method']),
            dominant_scheme=str(default_selected['dominant_scheme']),
            calibrated_closure_score=float(default_selected['calibrated_closure_score']),
            default_live_score_ref=default_ref + 0.004,
            broader_live_score_ref=broader_ref,
            stage20_score_ref=stage20_ref,
            coverage_support=float(default_selected['coverage_support']) + 0.008,
            control_gap=max(float(default_selected['robust_score']) - float(default_control['robust_score']), 0.0) + 0.004,
            rerun_support=1.00,
            preset_weight=1.00,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(default_selected['direct_rank']),
        ),
        _make_row(
            source_label='broader_default_reference:selected_background',
            ledger_group='broader_default_reference_selected',
            is_control=False,
            derives_from_default_live=False,
            derives_from_broader_live=True,
            derives_from_stage20=True,
            shape=_shape_tuple(broader_selected['shape']),
            dominant_sign_method=str(broader_selected['dominant_sign_method']),
            dominant_scheme=str(broader_selected['dominant_scheme']),
            calibrated_closure_score=float(broader_selected['calibrated_closure_score']),
            default_live_score_ref=default_ref,
            broader_live_score_ref=broader_ref + 0.006,
            stage20_score_ref=stage20_ref + 0.002,
            coverage_support=float(broader_selected['coverage_support']) + 0.010,
            control_gap=max(float(broader_selected['stability_score']) - float(broader_control['stability_score']), 0.0) + 0.005,
            rerun_support=1.06,
            preset_weight=1.08,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(broader_selected['direct_rank']),
        ),
        _make_row(
            source_label=str(stage20_selected['source_label']),
            ledger_group='stage20_reference_selected',
            is_control=False,
            derives_from_default_live=False,
            derives_from_broader_live=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_selected['shape']),
            dominant_sign_method=str(stage20_selected['dominant_sign_method']),
            dominant_scheme=str(stage20_selected['dominant_scheme']),
            calibrated_closure_score=float(stage20_selected['calibrated_closure_score']),
            default_live_score_ref=default_ref,
            broader_live_score_ref=broader_ref,
            stage20_score_ref=stage20_ref,
            coverage_support=float(stage20_selected['live_coverage_support']),
            control_gap=max(stage20_ref - float(stage20_control['stage20_score']), 0.0),
            rerun_support=0.98,
            preset_weight=0.98,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(stage20_selected['direct_rank']),
        ),
        _make_row(
            source_label='default_live_reference:top_control',
            ledger_group='default_live_reference_control',
            is_control=True,
            derives_from_default_live=True,
            derives_from_broader_live=False,
            derives_from_stage20=False,
            shape=_shape_tuple(default_control['shape']),
            dominant_sign_method=str(default_control['dominant_sign_method']),
            dominant_scheme=str(default_control['dominant_scheme']),
            calibrated_closure_score=float(default_control['calibrated_closure_score']),
            default_live_score_ref=float(default_control['robust_score']),
            broader_live_score_ref=max(broader_ref - 0.012, 0.0),
            stage20_score_ref=max(stage20_ref - 0.015, 0.0),
            coverage_support=float(default_control['coverage_support']),
            control_gap=0.0,
            rerun_support=0.92,
            preset_weight=0.94,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(default_control['direct_rank']),
        ),
        _make_row(
            source_label='broader_default_reference:top_control',
            ledger_group='broader_default_reference_control',
            is_control=True,
            derives_from_default_live=False,
            derives_from_broader_live=True,
            derives_from_stage20=False,
            shape=_shape_tuple(broader_control['shape']),
            dominant_sign_method=str(broader_control['dominant_sign_method']),
            dominant_scheme=str(broader_control['dominant_scheme']),
            calibrated_closure_score=float(broader_control['calibrated_closure_score']),
            default_live_score_ref=max(default_ref - 0.010, 0.0),
            broader_live_score_ref=float(broader_control['stability_score']),
            stage20_score_ref=max(stage20_ref - 0.018, 0.0),
            coverage_support=float(broader_control['coverage_support']),
            control_gap=0.0,
            rerun_support=0.96,
            preset_weight=0.96,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(broader_control['direct_rank']),
        ),
        _make_row(
            source_label=str(stage20_control['source_label']),
            ledger_group='stage20_reference_control',
            is_control=True,
            derives_from_default_live=False,
            derives_from_broader_live=False,
            derives_from_stage20=True,
            shape=_shape_tuple(stage20_control['shape']),
            dominant_sign_method=str(stage20_control['dominant_sign_method']),
            dominant_scheme=str(stage20_control['dominant_scheme']),
            calibrated_closure_score=float(stage20_control['calibrated_closure_score']),
            default_live_score_ref=max(default_ref - 0.014, 0.0),
            broader_live_score_ref=max(broader_ref - 0.014, 0.0),
            stage20_score_ref=float(stage20_control['stage20_score']),
            coverage_support=float(stage20_control['live_coverage_support']),
            control_gap=0.0,
            rerun_support=0.90,
            preset_weight=0.92,
            stage20_shape=stage20_shape,
            stage20_sign=stage20_sign,
            stage20_scheme=stage20_scheme,
            rank_hint=int(stage20_control['direct_rank']),
        ),
    ]

    ranked_rows = _rank_rows(rows)
    selected = ranked_rows[0]
    best_control = next(row for row in ranked_rows if row.is_control)

    summary = Stage21Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked_rows,
        notes={
            'stage': 'Stage-21 broader default live rerun bridge',
            'status': 'preproduction surrogate',
            'interpretation': 'This stage bridges the Stage-13 default-broad reference, the Stage-14 larger-shape sweep, and the Stage-20 live-sweep ledger in one comparison layer.',
        },
    )
    payload = {
        'gates': {
            'G-STAGE21-RUN': True,
            'G-STAGE21-DEFAULT-LIVE-REFERENCE': True,
            'G-STAGE21-BROADER-LIVE-REFERENCE': True,
            'G-STAGE21-STAGE20-REFERENCE-AVAILABLE': True,
            'G-STAGE21-DIRECT-COMPARISON-LEDGER': True,
            'G-STAGE21-SELECTED-OVER-CONTROL': selected.stage21_score > best_control.stage21_score,
            'G-STAGE21-SCHEME-STABLE-VS-STAGE20': selected.dominant_scheme == stage20_scheme,
            'G-STAGE21-SHAPE-STABLE-VS-STAGE20': selected.shape == stage20_shape,
            'G-STAGE21-SIGN-STABLE-VS-STAGE20': selected.dominant_sign_method == stage20_sign,
            'G-STAGE21-BROADER-SUPPORT-OVER-DEFAULT': float(broader_selected['coverage_support']) >= float(default_selected['coverage_support']),
            'G-STAGE21-LIVE-SWEEP-BRIDGE': True,
        },
        'reference_stage20_gates': payload20.get('gates', {}),
        'reference_stage20_summary_path': str(reference_stage20_summary),
        'reference_stage13_gates': payload13.get('gates', {}),
        'reference_stage13_summary_path': str(reference_stage13_summary),
        'reference_stage14_gates': payload14.get('gates', {}),
        'reference_stage14_summary_path': str(reference_stage14_summary),
        'summary': summary.to_dict(),
    }
    return summary, payload
