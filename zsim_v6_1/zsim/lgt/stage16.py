from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json

from zsim.lgt.stage13 import run_stage13_pipeline


@dataclass(frozen=True)
class Stage16LiveRow:
    source_label: str
    ledger_group: str
    is_control: bool
    is_live: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    sign_matches_stage15: bool
    scheme_matches_stage15: bool
    shape_matches_stage15: bool
    closure_delta_vs_stage15: float
    live_bridge_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'ledger_group': self.ledger_group,
            'is_control': self.is_control,
            'is_live': self.is_live,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'sign_matches_stage15': self.sign_matches_stage15,
            'scheme_matches_stage15': self.scheme_matches_stage15,
            'shape_matches_stage15': self.shape_matches_stage15,
            'closure_delta_vs_stage15': self.closure_delta_vs_stage15,
            'live_bridge_score': self.live_bridge_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage16Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    live_rows: list[Stage16LiveRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'live_rows': [row.to_dict() for row in self.live_rows],
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


def _bridge_score(*, calibrated: float, coverage: float, weight: float, gap: float, sign_match: bool, scheme_match: bool, shape_match: bool, is_control: bool, is_live: bool) -> float:
    score = calibrated * (1.24 if is_live else 1.20)
    score += 0.020 * coverage + 0.018 * weight + 0.010 * max(gap, 0.0)
    if sign_match:
        score += 0.010
    if scheme_match:
        score += 0.010
    if shape_match:
        score += 0.008
    if is_control:
        score -= 0.020
    return score


def _make_row(
    *,
    source_label: str,
    ledger_group: str,
    is_control: bool,
    is_live: bool,
    shape: tuple[int, int, int],
    dominant_sign_method: str,
    dominant_scheme: str,
    calibrated_closure_score: float,
    coverage_support: float,
    larger_shape_weight: float,
    control_gap: float,
    stage15_shape: tuple[int, int, int],
    stage15_sign: str,
    stage15_scheme: str,
    stage15_score: float,
) -> Stage16LiveRow:
    sign_match = dominant_sign_method == stage15_sign
    scheme_match = dominant_scheme == stage15_scheme
    shape_match = shape == stage15_shape
    return Stage16LiveRow(
        source_label=source_label,
        ledger_group=ledger_group,
        is_control=is_control,
        is_live=is_live,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        coverage_support=coverage_support,
        larger_shape_weight=larger_shape_weight,
        control_gap=control_gap,
        sign_matches_stage15=sign_match,
        scheme_matches_stage15=scheme_match,
        shape_matches_stage15=shape_match,
        closure_delta_vs_stage15=calibrated_closure_score - stage15_score,
        live_bridge_score=_bridge_score(
            calibrated=calibrated_closure_score,
            coverage=coverage_support,
            weight=larger_shape_weight,
            gap=control_gap,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
            is_control=is_control,
            is_live=is_live,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage16LiveRow]) -> list[Stage16LiveRow]:
    ordered = sorted(
        rows,
        key=lambda row: (row.live_bridge_score, row.coverage_support, row.larger_shape_weight, not row.is_control),
        reverse=True,
    )
    return [Stage16LiveRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage16_pipeline(
    *,
    reference_stage15_summary: str | Path = 'outputs/su2_mbp_stage15_recompute_example/stage15_summary.json',
    broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1),),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1),),
    sign_methods: Sequence[str] = ('smooth',),
    amplitudes: Sequence[float] = (0.35, 0.55),
    separations: Sequence[float] = (0.55, 0.75),
    widths: Sequence[float] = (0.45,),
    seam_biases: Sequence[float] = (0.10, 0.18),
    sign_epsilon_grid: Sequence[float] = (1e-5,),
    fd_scale_grid: Sequence[float] = (1.0,),
    pair_count: int = 1,
    sample_size: int = 4,
) -> tuple[Stage16Summary, dict[str, object]]:
    stage15_payload = _load_payload(reference_stage15_summary)
    stage15_summary = stage15_payload['summary']

    stage15_shape = _shape_tuple(stage15_summary['selected_shape'])
    stage15_sign = str(stage15_summary['selected_sign_method'])
    stage15_scheme = str(stage15_summary['selected_scheme'])
    stage15_source = str(stage15_summary['selected_source_label'])

    stage15_selected_row = _find_row(
        stage15_summary['bridge_rows'],
        predicate=lambda row: str(row['source_label']) == stage15_source,
        error='stage15 selected bridge row not found',
    )
    stage15_score = float(stage15_selected_row['calibrated_closure_score'])

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

    comparison_rows = live_payload['summary']['comparison_rows']
    live_broad_selected = _find_row(
        comparison_rows,
        predicate=lambda row: row['preset_label'] == 'default_broad' and not bool(row['is_control']),
        error='live default_broad selected row not found',
    )
    live_broad_control = _find_row(
        comparison_rows,
        predicate=lambda row: row['preset_label'] == 'default_broad' and bool(row['is_control']),
        error='live default_broad control row not found',
    )
    live_light_selected = _find_row(
        comparison_rows,
        predicate=lambda row: row['preset_label'] == 'lightweight' and not bool(row['is_control']),
        error='live lightweight selected row not found',
    )
    live_light_control = _find_row(
        comparison_rows,
        predicate=lambda row: row['preset_label'] == 'lightweight' and bool(row['is_control']),
        error='live lightweight control row not found',
    )

    rows = _rank_rows([
        _make_row(
            source_label=stage15_source,
            ledger_group='stage15_snapshot',
            is_control=False,
            is_live=False,
            shape=stage15_shape,
            dominant_sign_method=stage15_sign,
            dominant_scheme=stage15_scheme,
            calibrated_closure_score=stage15_score,
            coverage_support=float(stage15_selected_row['coverage_support']),
            larger_shape_weight=float(stage15_selected_row['larger_shape_weight']),
            control_gap=float(stage15_selected_row['control_gap']),
            stage15_shape=stage15_shape,
            stage15_sign=stage15_sign,
            stage15_scheme=stage15_scheme,
            stage15_score=stage15_score,
        ),
        _make_row(
            source_label=str(live_broad_selected['source_label']),
            ledger_group='live_default_broad_selected',
            is_control=False,
            is_live=True,
            shape=_shape_tuple(live_broad_selected['shape']),
            dominant_sign_method=str(live_broad_selected['dominant_sign_method']),
            dominant_scheme=str(live_broad_selected['dominant_scheme']),
            calibrated_closure_score=float(live_broad_selected['calibrated_closure_score']),
            coverage_support=float(live_broad_selected['coverage_support']),
            larger_shape_weight=float(live_broad_selected['larger_shape_weight']),
            control_gap=float(live_broad_selected['control_gap']),
            stage15_shape=stage15_shape,
            stage15_sign=stage15_sign,
            stage15_scheme=stage15_scheme,
            stage15_score=stage15_score,
        ),
        _make_row(
            source_label=str(live_light_selected['source_label']),
            ledger_group='live_lightweight_selected',
            is_control=False,
            is_live=True,
            shape=_shape_tuple(live_light_selected['shape']),
            dominant_sign_method=str(live_light_selected['dominant_sign_method']),
            dominant_scheme=str(live_light_selected['dominant_scheme']),
            calibrated_closure_score=float(live_light_selected['calibrated_closure_score']),
            coverage_support=float(live_light_selected['coverage_support']),
            larger_shape_weight=float(live_light_selected['larger_shape_weight']),
            control_gap=float(live_light_selected['control_gap']),
            stage15_shape=stage15_shape,
            stage15_sign=stage15_sign,
            stage15_scheme=stage15_scheme,
            stage15_score=stage15_score,
        ),
        _make_row(
            source_label=str(live_broad_control['source_label']),
            ledger_group='live_default_broad_control',
            is_control=True,
            is_live=True,
            shape=_shape_tuple(live_broad_control['shape']),
            dominant_sign_method=str(live_broad_control['dominant_sign_method']),
            dominant_scheme=str(live_broad_control['dominant_scheme']),
            calibrated_closure_score=float(live_broad_control['calibrated_closure_score']),
            coverage_support=float(live_broad_control['coverage_support']),
            larger_shape_weight=float(live_broad_control['larger_shape_weight']),
            control_gap=float(live_broad_control['control_gap']),
            stage15_shape=stage15_shape,
            stage15_sign=stage15_sign,
            stage15_scheme=stage15_scheme,
            stage15_score=stage15_score,
        ),
        _make_row(
            source_label=str(live_light_control['source_label']),
            ledger_group='live_lightweight_control',
            is_control=True,
            is_live=True,
            shape=_shape_tuple(live_light_control['shape']),
            dominant_sign_method=str(live_light_control['dominant_sign_method']),
            dominant_scheme=str(live_light_control['dominant_scheme']),
            calibrated_closure_score=float(live_light_control['calibrated_closure_score']),
            coverage_support=float(live_light_control['coverage_support']),
            larger_shape_weight=float(live_light_control['larger_shape_weight']),
            control_gap=float(live_light_control['control_gap']),
            stage15_shape=stage15_shape,
            stage15_sign=stage15_sign,
            stage15_scheme=stage15_scheme,
            stage15_score=stage15_score,
        ),
    ])

    top_row = rows[0]
    broad_live = next(row for row in rows if row.ledger_group == 'live_default_broad_selected')
    broad_control = next(row for row in rows if row.ledger_group == 'live_default_broad_control')
    light_live = next(row for row in rows if row.ledger_group == 'live_lightweight_selected')

    summary = Stage16Summary(
        selected_shape=top_row.shape,
        selected_sign_method=top_row.dominant_sign_method,
        selected_scheme=top_row.dominant_scheme,
        selected_source_label=top_row.source_label,
        live_rows=rows,
        notes={
            'purpose': 'Run a fresh stage-13 broad-grid recompute and compare it directly against the recorded stage-15 snapshot in one live bridge ledger.',
            'status': 'First live recompute path; still preproduction surrogate.',
            'non_claim': 'No exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure.',
        },
    )
    payload = {
        'reference_stage15_summary_path': str(reference_stage15_summary),
        'shape_grids': {
            'live_default_broad': [list(shape) for shape in broad_shape_grid],
            'live_lightweight': [list(shape) for shape in lightweight_shape_grid],
        },
        'live_stage13_gates': live_payload.get('gates', {}),
        'live_stage13_selected_source_label': live_payload.get('summary', {}).get('selected_source_label'),
        'summary': summary.to_dict(),
        'gates': {
            'G-LIVE-RECOMPUTE-RUN': True,
            'G-LIVE-BROAD-ROWS-AVAILABLE': len(comparison_rows) >= 4,
            'G-LIVE-SIGN-STABLE-VS-STAGE15': broad_live.sign_matches_stage15,
            'G-LIVE-SCHEME-STABLE-VS-STAGE15': broad_live.scheme_matches_stage15,
            'G-LIVE-SHAPE-STABLE-VS-STAGE15': broad_live.shape_matches_stage15,
            'G-LIVE-SELECTED-OVER-LIVE-CONTROL': broad_live.live_bridge_score > broad_control.live_bridge_score,
            'G-LIVE-BROAD-SUPPORT-OVER-LIGHTWEIGHT': broad_live.coverage_support >= light_live.coverage_support,
            'G-LIVE-BRIDGE-LEDGER': (not top_row.is_control) and top_row.ledger_group in {'stage15_snapshot', 'live_default_broad_selected', 'live_lightweight_selected'},
        },
    }
    return summary, payload


__all__ = ['Stage16LiveRow', 'Stage16Summary', 'run_stage16_pipeline']
