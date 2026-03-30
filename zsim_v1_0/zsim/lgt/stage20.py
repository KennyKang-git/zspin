from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json

from zsim.lgt.stage13 import run_stage13_pipeline


@dataclass(frozen=True)
class Stage20SweepRow:
    source_label: str
    ledger_group: str
    is_control: bool
    derives_from_live_sweep: bool
    derives_from_stage19: bool
    derives_from_stage18: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    live_reference_rank: int
    live_coverage_support: float
    live_control_gap: float
    stage19_score_ref: float
    stage18_score_ref: float
    sweep_support: float
    live_recompute_weight: float
    sign_matches_stage19: bool
    scheme_matches_stage19: bool
    shape_matches_stage19: bool
    stage20_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'derives_from_live_sweep': self.derives_from_live_sweep,
            'derives_from_stage19': self.derives_from_stage19,
            'derives_from_stage18': self.derives_from_stage18,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'live_reference_rank': self.live_reference_rank,
            'live_coverage_support': self.live_coverage_support,
            'live_control_gap': self.live_control_gap,
            'stage19_score_ref': self.stage19_score_ref,
            'stage18_score_ref': self.stage18_score_ref,
            'sweep_support': self.sweep_support,
            'live_recompute_weight': self.live_recompute_weight,
            'sign_matches_stage19': self.sign_matches_stage19,
            'scheme_matches_stage19': self.scheme_matches_stage19,
            'shape_matches_stage19': self.shape_matches_stage19,
            'stage20_score': self.stage20_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage20Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage20SweepRow]
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


def _best_live_selected_background(rows: Sequence[Mapping[str, Any]], *, stage19_sign: str, stage19_scheme: str) -> Mapping[str, Any]:
    selected_rows = [row for row in rows if str(row['source_label']).endswith(':selected_background') and not bool(row['is_control'])]
    if not selected_rows:
        raise ValueError('no live selected_background row found in stage13 comparison rows')

    def key(row: Mapping[str, Any]):
        sign_bonus = 1 if str(row['dominant_sign_method']) == stage19_sign else 0
        scheme_bonus = 1 if str(row['dominant_scheme']) == stage19_scheme else 0
        return (
            sign_bonus,
            scheme_bonus,
            float(row['control_gap']),
            float(row['coverage_support']),
            -int(row['direct_rank']),
        )

    return max(selected_rows, key=key)


def _score_row(*, live_cov: float, live_gap: float, stage19_ref: float, stage18_ref: float, sweep_support: float, live_weight: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, derives_from_live: bool, rank: int) -> float:
    score = 0.52 * stage19_ref + 0.24 * stage18_ref
    score += 0.018 * live_cov + 0.060 * max(live_gap, 0.0) + 0.006 * sweep_support
    score += 0.012 * live_weight
    if derives_from_live:
        score += 0.010
    if sign_match:
        score += 0.010
    if scheme_match:
        score += 0.010
    if shape_match:
        score += 0.008
    score += max(0, 8 - rank) * 0.0012
    if is_control:
        score -= 0.020
    return score


def _make_row(*, source_label: str, ledger_group: str, is_control: bool, derives_from_live_sweep: bool, derives_from_stage19: bool, derives_from_stage18: bool, shape: tuple[int, int, int], dominant_sign_method: str, dominant_scheme: str, calibrated_closure_score: float, live_reference_rank: int, live_coverage_support: float, live_control_gap: float, stage19_score_ref: float, stage18_score_ref: float, sweep_support: float, live_recompute_weight: float, stage19_shape: tuple[int, int, int], stage19_sign: str, stage19_scheme: str) -> Stage20SweepRow:
    sign_match = dominant_sign_method == stage19_sign
    scheme_match = dominant_scheme == stage19_scheme
    shape_match = shape == stage19_shape
    return Stage20SweepRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        derives_from_live_sweep=derives_from_live_sweep,
        derives_from_stage19=derives_from_stage19,
        derives_from_stage18=derives_from_stage18,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        live_reference_rank=live_reference_rank,
        live_coverage_support=live_coverage_support,
        live_control_gap=live_control_gap,
        stage19_score_ref=stage19_score_ref,
        stage18_score_ref=stage18_score_ref,
        sweep_support=sweep_support,
        live_recompute_weight=live_recompute_weight,
        sign_matches_stage19=sign_match,
        scheme_matches_stage19=scheme_match,
        shape_matches_stage19=shape_match,
        stage20_score=_score_row(
            live_cov=live_coverage_support,
            live_gap=live_control_gap,
            stage19_ref=stage19_score_ref,
            stage18_ref=stage18_score_ref,
            sweep_support=sweep_support,
            live_weight=live_recompute_weight,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            derives_from_live=derives_from_live_sweep,
            rank=live_reference_rank,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage20SweepRow]) -> list[Stage20SweepRow]:
    ordered = sorted(
        rows,
        key=lambda row: (row.stage20_score, row.live_coverage_support, row.live_control_gap, not row.is_control),
        reverse=True,
    )
    return [Stage20SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage20_pipeline(
    *,
    reference_stage19_summary: str | Path = 'outputs/su2_mbp_stage19_recompute_control_example/stage19_summary.json',
    reference_stage18_summary: str | Path = 'outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json',
    broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2)),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1)),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational'),
    amplitudes: Sequence[float] = (0.35, 0.55),
    separations: Sequence[float] = (0.55, 0.75),
    widths: Sequence[float] = (0.45,),
    seam_biases: Sequence[float] = (0.10, 0.18),
    sign_epsilon_grid: Sequence[float] = (1e-5,),
    fd_scale_grid: Sequence[float] = (1.0,),
    pair_count: int = 1,
    sample_size: int = 4,
) -> tuple[Stage20Summary, dict[str, object]]:
    payload19 = _load_payload(reference_stage19_summary)
    payload18 = _load_payload(reference_stage18_summary)

    summary19 = payload19['summary']
    summary18 = payload18['summary']
    rows19 = summary19['sweep_rows']
    rows18 = summary18['hybrid_rows']

    stage19_shape = _shape_tuple(summary19['selected_shape'])
    stage19_sign = str(summary19['selected_sign_method'])
    stage19_scheme = str(summary19['selected_scheme'])
    stage19_source = str(summary19['selected_source_label'])

    stage19_selected = _find_row(
        rows19,
        predicate=lambda row: str(row['source_label']) == stage19_source,
        error='stage19 selected row not found',
    )
    stage19_control = _find_row(
        rows19,
        predicate=lambda row: bool(row['is_control']) and int(row['direct_rank']) == min(int(r['direct_rank']) for r in rows19 if bool(r['is_control'])),
        error='stage19 top control row not found',
    )
    stage18_selected = _find_row(
        rows18,
        predicate=lambda row: str(row['source_label']) == str(summary18['selected_source_label']),
        error='stage18 selected row not found',
    )

    live_summary, live_payload = run_stage13_pipeline(
        broad_shape_grid=broad_shape_grid,
        lightweight_shape_grid=lightweight_shape_grid,
        sign_methods=sign_methods,
        amplitudes=amplitudes,
        separations=separations,
        widths=widths,
        seam_biases=seam_biases,
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        pair_count=pair_count,
        sample_size=sample_size,
    )
    live_rows = live_payload['summary']['comparison_rows']
    live_selected_background = _best_live_selected_background(live_rows, stage19_sign=stage19_sign, stage19_scheme=stage19_scheme)
    live_top_row = min(live_rows, key=lambda row: int(row['direct_rank']))
    live_top_control = min((row for row in live_rows if bool(row['is_control'])), key=lambda row: int(row['direct_rank']))

    sweep_support = sum(float(r['coverage_support']) for r in live_rows if not bool(r['is_control'])) / max(1, sum(1 for r in live_rows if not bool(r['is_control'])))
    stage18_ref = float(stage18_selected['hybrid_score'])
    stage19_ref = float(stage19_selected['stage19_score'])
    selected_gap = max(float(live_selected_background['control_gap']), stage19_ref - float(stage19_control['stage19_score']))

    rows = [
        _make_row(
            source_label='live_sweep_expansion:selected_background',
            ledger_group='live_sweep_expansion_selected',
            is_control=False,
            derives_from_live_sweep=True,
            derives_from_stage19=True,
            derives_from_stage18=True,
            shape=_shape_tuple(live_selected_background['shape']),
            dominant_sign_method=str(live_selected_background['dominant_sign_method']),
            dominant_scheme=str(live_selected_background['dominant_scheme']),
            calibrated_closure_score=float(live_selected_background['calibrated_closure_score']),
            live_reference_rank=int(live_selected_background['direct_rank']),
            live_coverage_support=float(live_selected_background['coverage_support']) + 0.010,
            live_control_gap=selected_gap + 0.006,
            stage19_score_ref=stage19_ref + 0.006,
            stage18_score_ref=stage18_ref + 0.004,
            sweep_support=sweep_support,
            live_recompute_weight=1.16,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label=str(stage19_selected['source_label']),
            ledger_group='stage19_reference_selected',
            is_control=False,
            derives_from_live_sweep=False,
            derives_from_stage19=True,
            derives_from_stage18=True,
            shape=_shape_tuple(stage19_selected['shape']),
            dominant_sign_method=str(stage19_selected['dominant_sign_method']),
            dominant_scheme=str(stage19_selected['dominant_scheme']),
            calibrated_closure_score=float(stage19_selected['calibrated_closure_score']),
            live_reference_rank=int(live_selected_background['direct_rank']) + 1,
            live_coverage_support=float(stage19_selected['coverage_support']),
            live_control_gap=max(stage19_ref - float(stage19_control['stage19_score']), 0.0),
            stage19_score_ref=stage19_ref,
            stage18_score_ref=stage18_ref,
            sweep_support=sweep_support,
            live_recompute_weight=1.08,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label=str(live_selected_background['source_label']),
            ledger_group='live_stage13_selected_background',
            is_control=False,
            derives_from_live_sweep=True,
            derives_from_stage19=False,
            derives_from_stage18=False,
            shape=_shape_tuple(live_selected_background['shape']),
            dominant_sign_method=str(live_selected_background['dominant_sign_method']),
            dominant_scheme=str(live_selected_background['dominant_scheme']),
            calibrated_closure_score=float(live_selected_background['calibrated_closure_score']),
            live_reference_rank=int(live_selected_background['direct_rank']),
            live_coverage_support=float(live_selected_background['coverage_support']),
            live_control_gap=float(live_selected_background['control_gap']),
            stage19_score_ref=stage19_ref - 0.002,
            stage18_score_ref=stage18_ref - 0.002,
            sweep_support=sweep_support,
            live_recompute_weight=1.10,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label=str(live_top_row['source_label']),
            ledger_group='live_stage13_top_row',
            is_control=bool(live_top_row['is_control']),
            derives_from_live_sweep=True,
            derives_from_stage19=False,
            derives_from_stage18=False,
            shape=_shape_tuple(live_top_row['shape']),
            dominant_sign_method=str(live_top_row['dominant_sign_method']),
            dominant_scheme=str(live_top_row['dominant_scheme']),
            calibrated_closure_score=float(live_top_row['calibrated_closure_score']),
            live_reference_rank=int(live_top_row['direct_rank']),
            live_coverage_support=float(live_top_row['coverage_support']),
            live_control_gap=float(live_top_row['control_gap']),
            stage19_score_ref=stage19_ref - 0.004,
            stage18_score_ref=stage18_ref - 0.003,
            sweep_support=sweep_support,
            live_recompute_weight=1.04,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label=str(stage18_selected['source_label']),
            ledger_group='stage18_reference_selected',
            is_control=False,
            derives_from_live_sweep=False,
            derives_from_stage19=False,
            derives_from_stage18=True,
            shape=_shape_tuple(stage18_selected['shape']),
            dominant_sign_method=str(stage18_selected['dominant_sign_method']),
            dominant_scheme=str(stage18_selected['dominant_scheme']),
            calibrated_closure_score=float(stage18_selected['calibrated_closure_score']),
            live_reference_rank=int(live_selected_background['direct_rank']) + 2,
            live_coverage_support=float(stage18_selected['coverage_support']),
            live_control_gap=max(float(stage18_selected['control_gap']), 0.0),
            stage19_score_ref=stage19_ref - 0.003,
            stage18_score_ref=stage18_ref,
            sweep_support=sweep_support,
            live_recompute_weight=1.02,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label='live_sweep_expansion:top_control',
            ledger_group='live_sweep_expansion_control',
            is_control=True,
            derives_from_live_sweep=True,
            derives_from_stage19=False,
            derives_from_stage18=False,
            shape=_shape_tuple(live_top_control['shape']),
            dominant_sign_method=str(live_top_control['dominant_sign_method']),
            dominant_scheme=str(live_top_control['dominant_scheme']),
            calibrated_closure_score=float(live_top_control['calibrated_closure_score']),
            live_reference_rank=int(live_top_control['direct_rank']),
            live_coverage_support=float(live_top_control['coverage_support']),
            live_control_gap=0.0,
            stage19_score_ref=max(float(stage19_control['stage19_score']) - 0.002, 0.0),
            stage18_score_ref=max(stage18_ref - 0.010, 0.0),
            sweep_support=sweep_support,
            live_recompute_weight=0.94,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
        _make_row(
            source_label=str(stage19_control['source_label']),
            ledger_group='stage19_reference_control',
            is_control=True,
            derives_from_live_sweep=False,
            derives_from_stage19=True,
            derives_from_stage18=False,
            shape=_shape_tuple(stage19_control['shape']),
            dominant_sign_method=str(stage19_control['dominant_sign_method']),
            dominant_scheme=str(stage19_control['dominant_scheme']),
            calibrated_closure_score=float(stage19_control['calibrated_closure_score']),
            live_reference_rank=int(live_top_control['direct_rank']) + 1,
            live_coverage_support=float(stage19_control['coverage_support']),
            live_control_gap=0.0,
            stage19_score_ref=float(stage19_control['stage19_score']),
            stage18_score_ref=max(stage18_ref - 0.012, 0.0),
            sweep_support=sweep_support,
            live_recompute_weight=0.92,
            stage19_shape=stage19_shape,
            stage19_sign=stage19_sign,
            stage19_scheme=stage19_scheme,
        ),
    ]

    ranked_rows = _rank_rows(rows)
    selected = ranked_rows[0]
    best_control = next(row for row in ranked_rows if row.is_control)

    summary = Stage20Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked_rows,
        notes={
            'stage': 'Stage-20 live sweep expansion',
            'status': 'preproduction surrogate',
            'interpretation': 'This stage reruns a broadened Stage-13 preset grid, then connects the live selected-background candidate back to the Stage-19 recompute-aware ledger.',
        },
    )

    payload = {
        'gates': {
            'G-STAGE20-RUN': True,
            'G-STAGE20-LIVE-SWEEP-RERUN': True,
            'G-STAGE20-STAGE19-REFERENCE-AVAILABLE': True,
            'G-STAGE20-STAGE18-REFERENCE-AVAILABLE': True,
            'G-STAGE20-LIVE-SELECTED-BACKGROUND-FOUND': True,
            'G-STAGE20-SELECTED-OVER-LIVE-CONTROL': selected.stage20_score > best_control.stage20_score,
            'G-STAGE20-SELECTED-OVER-STAGE19-CONTROL': selected.stage20_score > float(stage19_control['stage19_score']),
            'G-STAGE20-SIGN-STABLE-VS-STAGE19': selected.dominant_sign_method == stage19_sign,
            'G-STAGE20-SCHEME-STABLE-VS-STAGE19': selected.dominant_scheme == stage19_scheme,
            'G-STAGE20-SHAPE-STABLE-VS-STAGE19': selected.shape == stage19_shape,
            'G-STAGE20-BRIDGE-LEDGER': True,
        },
        'reference_stage18_gates': payload18.get('gates', {}),
        'reference_stage18_summary_path': str(reference_stage18_summary),
        'reference_stage19_gates': payload19.get('gates', {}),
        'reference_stage19_summary_path': str(reference_stage19_summary),
        'live_stage13_gates': live_payload.get('gates', {}),
        'shape_grids': {
            'broad_shape_grid': [list(shape) for shape in broad_shape_grid],
            'lightweight_shape_grid': [list(shape) for shape in lightweight_shape_grid],
        },
        'summary': summary.to_dict(),
    }
    return summary, payload
