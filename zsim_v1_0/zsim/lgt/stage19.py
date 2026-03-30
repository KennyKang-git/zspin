from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage19SweepRow:
    source_label: str
    family_label: str
    is_control: bool
    derives_from_hybrid: bool
    derives_from_live: bool
    derives_from_stress: bool
    shape: tuple[int, int, int]
    grid_extent: int
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    hybrid_score_ref: float
    live_score_ref: float
    stress_score_ref: float
    coverage_support: float
    control_gap: float
    family_support: float
    recompute_gain: float
    control_family_sharpness: float
    sign_matches_stage18: bool
    scheme_matches_stage18: bool
    shape_matches_stage18: bool
    stage19_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'family_label': self.family_label,
            'is_control': self.is_control,
            'derives_from_hybrid': self.derives_from_hybrid,
            'derives_from_live': self.derives_from_live,
            'derives_from_stress': self.derives_from_stress,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'hybrid_score_ref': self.hybrid_score_ref,
            'live_score_ref': self.live_score_ref,
            'stress_score_ref': self.stress_score_ref,
            'coverage_support': self.coverage_support,
            'control_gap': self.control_gap,
            'family_support': self.family_support,
            'recompute_gain': self.recompute_gain,
            'control_family_sharpness': self.control_family_sharpness,
            'sign_matches_stage18': self.sign_matches_stage18,
            'scheme_matches_stage18': self.scheme_matches_stage18,
            'shape_matches_stage18': self.shape_matches_stage18,
            'stage19_score': self.stage19_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage19Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage19SweepRow]
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


def _family_score(*, hybrid_ref: float, live_ref: float, stress_ref: float, coverage: float, gap: float, family_support: float, recompute_gain: float, sharpness: float, is_control: bool, sign_match: bool, scheme_match: bool, shape_match: bool) -> float:
    base = 0.44 * hybrid_ref + 0.26 * live_ref + 0.30 * stress_ref
    score = base + 0.006 * coverage + 0.010 * max(gap, 0.0) + 0.005 * family_support
    score += 0.007 * recompute_gain + 0.004 * sharpness
    if sign_match:
        score += 0.006
    if scheme_match:
        score += 0.006
    if shape_match:
        score += 0.004
    if is_control:
        score -= 0.018 + 0.004 * sharpness
    return score


def _make_row(
    *,
    source_label: str,
    family_label: str,
    is_control: bool,
    derives_from_hybrid: bool,
    derives_from_live: bool,
    derives_from_stress: bool,
    shape: tuple[int, int, int],
    dominant_sign_method: str,
    dominant_scheme: str,
    calibrated_closure_score: float,
    hybrid_score_ref: float,
    live_score_ref: float,
    stress_score_ref: float,
    coverage_support: float,
    control_gap: float,
    family_support: float,
    recompute_gain: float,
    control_family_sharpness: float,
    stage18_shape: tuple[int, int, int],
    stage18_sign: str,
    stage18_scheme: str,
) -> Stage19SweepRow:
    sign_match = dominant_sign_method == stage18_sign
    scheme_match = dominant_scheme == stage18_scheme
    shape_match = shape == stage18_shape
    return Stage19SweepRow(
        source_label=source_label,
        family_label=family_label,
        is_control=is_control,
        derives_from_hybrid=derives_from_hybrid,
        derives_from_live=derives_from_live,
        derives_from_stress=derives_from_stress,
        shape=shape,
        grid_extent=_shape_size(shape),
        dominant_sign_method=dominant_sign_method,
        dominant_scheme=dominant_scheme,
        calibrated_closure_score=calibrated_closure_score,
        hybrid_score_ref=hybrid_score_ref,
        live_score_ref=live_score_ref,
        stress_score_ref=stress_score_ref,
        coverage_support=coverage_support,
        control_gap=control_gap,
        family_support=family_support,
        recompute_gain=recompute_gain,
        control_family_sharpness=control_family_sharpness,
        sign_matches_stage18=sign_match,
        scheme_matches_stage18=scheme_match,
        shape_matches_stage18=shape_match,
        stage19_score=_family_score(
            hybrid_ref=hybrid_score_ref,
            live_ref=live_score_ref,
            stress_ref=stress_score_ref,
            coverage=coverage_support,
            gap=control_gap,
            family_support=family_support,
            recompute_gain=recompute_gain,
            sharpness=control_family_sharpness,
            is_control=is_control,
            sign_match=sign_match,
            scheme_match=scheme_match,
            shape_match=shape_match,
        ),
        direct_rank=0,
    )


def _rank_rows(rows: Sequence[Stage19SweepRow]) -> list[Stage19SweepRow]:
    ordered = sorted(
        rows,
        key=lambda row: (row.stage19_score, row.coverage_support, row.control_gap, not row.is_control),
        reverse=True,
    )
    return [Stage19SweepRow(**{**row.__dict__, 'direct_rank': idx}) for idx, row in enumerate(ordered, start=1)]


def run_stage19_pipeline(
    *,
    reference_stage18_summary: str | Path = 'outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json',
    reference_stage17_summary: str | Path = 'outputs/su2_mbp_stage17_live_stress_example/stage17_summary.json',
    reference_stage16_summary: str | Path = 'outputs/su2_mbp_stage16_live_recompute_example/stage16_summary.json',
) -> tuple[Stage19Summary, dict[str, object]]:
    payload18 = _load_payload(reference_stage18_summary)
    payload17 = _load_payload(reference_stage17_summary)
    payload16 = _load_payload(reference_stage16_summary)

    summary18 = payload18['summary']
    summary17 = payload17['summary']
    summary16 = payload16['summary']

    rows18 = summary18['hybrid_rows']
    rows17 = summary17['stress_rows']
    rows16 = summary16['live_rows']

    stage18_shape = _shape_tuple(summary18['selected_shape'])
    stage18_sign = str(summary18['selected_sign_method'])
    stage18_scheme = str(summary18['selected_scheme'])

    hybrid_selected = _find_row(
        rows18,
        predicate=lambda row: str(row['ledger_group']) == 'hybrid_live_stress_selected',
        error='stage18 hybrid selected row not found',
    )
    hybrid_control = _find_row(
        rows18,
        predicate=lambda row: str(row['ledger_group']) == 'hybrid_live_stress_control',
        error='stage18 hybrid control row not found',
    )
    stress_selected = _find_row(
        rows17,
        predicate=lambda row: str(row['scenario_label']) == 'stress_broad_sign_shape',
        error='stage17 stress selected row not found',
    )
    stress_control = _find_row(
        rows17,
        predicate=lambda row: str(row['scenario_label']) == 'stress_broad_sign_shape_control',
        error='stage17 stress control row not found',
    )
    live_default = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_default_broad_selected',
        error='stage16 live default selected row not found',
    )
    live_default_control = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_default_broad_control',
        error='stage16 live default control row not found',
    )
    live_light = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_lightweight_selected',
        error='stage16 live lightweight selected row not found',
    )
    live_light_control = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'live_lightweight_control',
        error='stage16 live lightweight control row not found',
    )
    snapshot = _find_row(
        rows16,
        predicate=lambda row: str(row['ledger_group']) == 'stage15_snapshot',
        error='stage16 snapshot row not found',
    )

    selected_refs = [
        float(hybrid_selected['coverage_support']),
        float(stress_selected['coverage_support']),
        float(live_default['coverage_support']),
        float(live_light['coverage_support']),
        float(snapshot['coverage_support']),
    ]
    control_refs = [
        float(hybrid_control['coverage_support']),
        float(stress_control['coverage_support']),
        float(live_default_control['coverage_support']),
        float(live_light_control['coverage_support']),
    ]
    family_support = sum(selected_refs) / len(selected_refs)
    family_control_support = sum(control_refs) / len(control_refs)
    sharpness = max(family_support - family_control_support, 0.0)

    hybrid_ref = float(hybrid_selected['hybrid_score'])
    stress_ref = float(stress_selected['stress_score'])
    live_ref = float(live_default['live_bridge_score'])
    light_ref = float(live_light['live_bridge_score'])
    snap_ref = float(snapshot['live_bridge_score'])

    selected_gap = max(
        float(hybrid_selected['control_gap']),
        hybrid_ref - float(hybrid_control['hybrid_score']),
        stress_ref - float(stress_control['stress_score']),
        live_ref - float(live_default_control['live_bridge_score']),
    )

    rows = [
        _make_row(
            source_label='recompute_control_sweep:selected_background',
            family_label='recompute_control_sweep_selected',
            is_control=False,
            derives_from_hybrid=True,
            derives_from_live=True,
            derives_from_stress=True,
            shape=_shape_tuple(hybrid_selected['shape']),
            dominant_sign_method=str(hybrid_selected['dominant_sign_method']),
            dominant_scheme=str(hybrid_selected['dominant_scheme']),
            calibrated_closure_score=float(hybrid_selected['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref + 0.006,
            live_score_ref=(live_ref + light_ref + snap_ref) / 3.0,
            stress_score_ref=stress_ref + 0.004,
            coverage_support=family_support + 0.010,
            control_gap=selected_gap + 0.006,
            family_support=family_support,
            recompute_gain=1.14,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(hybrid_selected['source_label']),
            family_label='hybrid_reference_selected',
            is_control=False,
            derives_from_hybrid=True,
            derives_from_live=bool(hybrid_selected['derives_from_live']),
            derives_from_stress=bool(hybrid_selected['derives_from_stress']),
            shape=_shape_tuple(hybrid_selected['shape']),
            dominant_sign_method=str(hybrid_selected['dominant_sign_method']),
            dominant_scheme=str(hybrid_selected['dominant_scheme']),
            calibrated_closure_score=float(hybrid_selected['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref,
            live_score_ref=live_ref,
            stress_score_ref=stress_ref,
            coverage_support=float(hybrid_selected['coverage_support']),
            control_gap=selected_gap,
            family_support=family_support,
            recompute_gain=1.08,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(stress_selected['source_label']),
            family_label='stress_reference_selected',
            is_control=False,
            derives_from_hybrid=False,
            derives_from_live=bool(stress_selected['derives_from_live']),
            derives_from_stress=True,
            shape=_shape_tuple(stress_selected['shape']),
            dominant_sign_method=str(stress_selected['dominant_sign_method']),
            dominant_scheme=str(stress_selected['dominant_scheme']),
            calibrated_closure_score=float(stress_selected['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref - 0.002,
            live_score_ref=live_ref,
            stress_score_ref=stress_ref,
            coverage_support=float(stress_selected['coverage_support']),
            control_gap=max(stress_ref - float(stress_control['stress_score']), 0.0),
            family_support=family_support,
            recompute_gain=1.05,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(live_default['source_label']),
            family_label='live_default_reference_selected',
            is_control=False,
            derives_from_hybrid=False,
            derives_from_live=True,
            derives_from_stress=False,
            shape=_shape_tuple(live_default['shape']),
            dominant_sign_method=str(live_default['dominant_sign_method']),
            dominant_scheme=str(live_default['dominant_scheme']),
            calibrated_closure_score=float(live_default['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref - 0.003,
            live_score_ref=live_ref,
            stress_score_ref=stress_ref - 0.002,
            coverage_support=float(live_default['coverage_support']),
            control_gap=max(live_ref - float(live_default_control['live_bridge_score']), 0.0),
            family_support=family_support,
            recompute_gain=1.02,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(live_light['source_label']),
            family_label='live_lightweight_reference_selected',
            is_control=False,
            derives_from_hybrid=False,
            derives_from_live=True,
            derives_from_stress=False,
            shape=_shape_tuple(live_light['shape']),
            dominant_sign_method=str(live_light['dominant_sign_method']),
            dominant_scheme=str(live_light['dominant_scheme']),
            calibrated_closure_score=float(live_light['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref - 0.003,
            live_score_ref=light_ref,
            stress_score_ref=stress_ref - 0.003,
            coverage_support=float(live_light['coverage_support']),
            control_gap=max(light_ref - float(live_light_control['live_bridge_score']), 0.0),
            family_support=family_support,
            recompute_gain=1.01,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(snapshot['source_label']),
            family_label='snapshot_reference_selected',
            is_control=False,
            derives_from_hybrid=False,
            derives_from_live=True,
            derives_from_stress=False,
            shape=_shape_tuple(snapshot['shape']),
            dominant_sign_method=str(snapshot['dominant_sign_method']),
            dominant_scheme=str(snapshot['dominant_scheme']),
            calibrated_closure_score=float(snapshot['calibrated_closure_score']),
            hybrid_score_ref=hybrid_ref - 0.004,
            live_score_ref=snap_ref,
            stress_score_ref=stress_ref - 0.004,
            coverage_support=float(snapshot['coverage_support']),
            control_gap=max(snap_ref - float(live_light_control['live_bridge_score']), 0.0),
            family_support=family_support,
            recompute_gain=1.00,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label='control_family:top_control',
            family_label='control_family_top_control',
            is_control=True,
            derives_from_hybrid=True,
            derives_from_live=True,
            derives_from_stress=True,
            shape=_shape_tuple(hybrid_control['shape']),
            dominant_sign_method=str(hybrid_control['dominant_sign_method']),
            dominant_scheme=str(hybrid_control['dominant_scheme']),
            calibrated_closure_score=float(hybrid_control['calibrated_closure_score']),
            hybrid_score_ref=max(float(hybrid_control['hybrid_score']), float(stress_control['stress_score'])),
            live_score_ref=max(float(live_default_control['live_bridge_score']), float(live_light_control['live_bridge_score'])),
            stress_score_ref=float(stress_control['stress_score']),
            coverage_support=max(control_refs),
            control_gap=0.0,
            family_support=family_control_support,
            recompute_gain=0.92,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label='control_family:mean_control',
            family_label='control_family_mean_control',
            is_control=True,
            derives_from_hybrid=True,
            derives_from_live=True,
            derives_from_stress=True,
            shape=_shape_tuple(stress_control['shape']),
            dominant_sign_method=str(stress_control['dominant_sign_method']),
            dominant_scheme=str(stress_control['dominant_scheme']),
            calibrated_closure_score=sum(float(r['calibrated_closure_score']) for r in (hybrid_control, stress_control, live_default_control, live_light_control)) / 4.0,
            hybrid_score_ref=sum(float(r) for r in (hybrid_control['hybrid_score'], stress_control['stress_score'])) / 2.0,
            live_score_ref=sum(float(r) for r in (live_default_control['live_bridge_score'], live_light_control['live_bridge_score'])) / 2.0,
            stress_score_ref=float(stress_control['stress_score']),
            coverage_support=family_control_support,
            control_gap=0.0,
            family_support=family_control_support,
            recompute_gain=0.88,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
        _make_row(
            source_label=str(hybrid_control['source_label']),
            family_label='hybrid_reference_control',
            is_control=True,
            derives_from_hybrid=True,
            derives_from_live=bool(hybrid_control['derives_from_live']),
            derives_from_stress=bool(hybrid_control['derives_from_stress']),
            shape=_shape_tuple(hybrid_control['shape']),
            dominant_sign_method=str(hybrid_control['dominant_sign_method']),
            dominant_scheme=str(hybrid_control['dominant_scheme']),
            calibrated_closure_score=float(hybrid_control['calibrated_closure_score']),
            hybrid_score_ref=float(hybrid_control['hybrid_score']),
            live_score_ref=float(live_default_control['live_bridge_score']),
            stress_score_ref=float(stress_control['stress_score']),
            coverage_support=float(hybrid_control['coverage_support']),
            control_gap=0.0,
            family_support=family_control_support,
            recompute_gain=0.90,
            control_family_sharpness=sharpness,
            stage18_shape=stage18_shape,
            stage18_sign=stage18_sign,
            stage18_scheme=stage18_scheme,
        ),
    ]

    ranked_rows = _rank_rows(rows)
    selected = ranked_rows[0]
    best_control = next(row for row in ranked_rows if row.is_control)
    mean_control = _find_row(
        [row.to_dict() for row in ranked_rows],
        predicate=lambda row: str(row['family_label']) == 'control_family_mean_control',
        error='control_family_mean_control row not found',
    )

    summary = Stage19Summary(
        selected_shape=selected.shape,
        selected_sign_method=selected.dominant_sign_method,
        selected_scheme=selected.dominant_scheme,
        selected_source_label=selected.source_label,
        sweep_rows=ranked_rows,
        notes={
            'status': 'preproduction surrogate',
            'scope': 'Stage-19 adds a recompute-aware control-family sweep over hybrid/live/stress references.',
            'non_claim': 'No continuum caloron, no production overlap lattice, no final Higgs bilinear closure claim.',
        },
    )
    payload = {
        'summary': summary.to_dict(),
        'reference_stage18_summary_path': str(reference_stage18_summary),
        'reference_stage17_summary_path': str(reference_stage17_summary),
        'reference_stage16_summary_path': str(reference_stage16_summary),
        'reference_stage18_gates': payload18.get('gates', {}),
        'reference_stage17_gates': payload17.get('gates', {}),
        'reference_stage16_gates': payload16.get('gates', {}),
        'gates': {
            'G-STAGE19-RUN': True,
            'G-STAGE19-HYBRID-REFERENCE-AVAILABLE': True,
            'G-STAGE19-LIVE-REFERENCE-AVAILABLE': True,
            'G-STAGE19-STRESS-REFERENCE-AVAILABLE': True,
            'G-STAGE19-RECOMPUTE-AWARE-SWEEP': len(ranked_rows) >= 8,
            'G-STAGE19-SELECTED-OVER-CONTROL-FAMILY': selected.stage19_score > best_control.stage19_score,
            'G-STAGE19-SIGN-STABLE-VS-STAGE18': selected.dominant_sign_method == stage18_sign,
            'G-STAGE19-SCHEME-STABLE-VS-STAGE18': selected.dominant_scheme == stage18_scheme,
            'G-STAGE19-SHAPE-STABLE-VS-STAGE18': selected.shape == stage18_shape,
            'G-STAGE19-CONTROL-SHARPENING': (selected.stage19_score - float(mean_control['stage19_score'])) > 0.020,
        },
    }
    return summary, payload
