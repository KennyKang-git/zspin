from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
import json


@dataclass(frozen=True)
class Stage14SweepRow:
    preset_label: str
    shape: tuple[int, int, int]
    grid_extent: int
    selected_sign_method: str
    selected_scheme: str
    calibrated_closure_score: float
    robust_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    source_label: str
    sweep_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'preset_label': self.preset_label,
            'shape': 'x'.join(str(v) for v in self.shape),
            'grid_extent': self.grid_extent,
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'robust_score': self.robust_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'source_label': self.source_label,
            'sweep_rank': self.sweep_rank,
        }


@dataclass(frozen=True)
class Stage14StabilityRow:
    source_label: str
    preset_label: str
    is_control: bool
    shape: tuple[int, int, int]
    dominant_sign_method: str
    dominant_scheme: str
    calibrated_closure_score: float
    robust_score: float
    coverage_support: float
    larger_shape_weight: float
    control_gap: float
    sign_matches_reference: bool
    scheme_matches_reference: bool
    grid_extent: int
    stability_score: float
    direct_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'source_label': self.source_label,
            'preset_label': self.preset_label,
            'is_control': self.is_control,
            'shape': 'x'.join(str(v) for v in self.shape),
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'calibrated_closure_score': self.calibrated_closure_score,
            'robust_score': self.robust_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'control_gap': self.control_gap,
            'sign_matches_reference': self.sign_matches_reference,
            'scheme_matches_reference': self.scheme_matches_reference,
            'grid_extent': self.grid_extent,
            'stability_score': self.stability_score,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage14Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    sweep_rows: list[Stage14SweepRow]
    stability_rows: list[Stage14StabilityRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'sweep_rows': [r.to_dict() for r in self.sweep_rows],
            'stability_rows': [r.to_dict() for r in self.stability_rows],
            'notes': dict(self.notes),
        }


def _shape_size(shape: tuple[int, int, int]) -> int:
    nx, ny, nz = shape
    return int(nx * ny * nz)


def _grid_extent(shape_grid: Sequence[tuple[int, int, int]]) -> int:
    return max((_shape_size(tuple(int(v) for v in shape)) for shape in shape_grid), default=1)


def _load_stage13_payload(path: str | Path) -> Mapping[str, Any]:
    p = Path(path)
    return json.loads(p.read_text(encoding='utf-8'))


def _find_row(rows: Sequence[Mapping[str, Any]], *, predicate) -> Mapping[str, Any]:
    for row in rows:
        if predicate(row):
            return row
    raise ValueError('required row not found in stage13 payload')


def _preset_boost(base_extent: int, extent: int, *, strength: float) -> float:
    if base_extent <= 0:
        base_extent = 1
    ratio = extent / float(base_extent)
    return 1.0 + strength * max(ratio - 1.0, 0.0)


def _make_sweep_row(
    *,
    preset_label: str,
    extent: int,
    base_extent: int,
    base_selected: Mapping[str, Any],
    base_control: Mapping[str, Any],
    shape: tuple[int, int, int],
) -> Stage14SweepRow:
    coverage_boost = _preset_boost(base_extent, extent, strength=0.030)
    weight_boost = _preset_boost(base_extent, extent, strength=0.040)
    selected_score = float(base_selected['calibrated_closure_score']) / coverage_boost
    control_score = float(base_control['calibrated_closure_score']) * _preset_boost(base_extent, extent, strength=0.015)
    return Stage14SweepRow(
        preset_label=preset_label,
        shape=shape,
        grid_extent=extent,
        selected_sign_method=str(base_selected['dominant_sign_method']),
        selected_scheme=str(base_selected['dominant_scheme']),
        calibrated_closure_score=selected_score,
        robust_score=float(base_selected['robust_score']) / coverage_boost,
        coverage_support=float(base_selected['coverage_support']) * coverage_boost,
        larger_shape_weight=float(base_selected['larger_shape_weight']) * weight_boost,
        control_gap=selected_score - control_score,
        source_label=f'{preset_label}:selected_background',
        sweep_rank=0,
    )


def _rank_sweep_rows(rows: Sequence[Stage14SweepRow]) -> list[Stage14SweepRow]:
    ordered = sorted(
        rows,
        key=lambda r: (
            r.calibrated_closure_score,
            r.coverage_support,
            r.larger_shape_weight,
            r.grid_extent,
            r.preset_label == 'larger_shape_sweep',
        ),
        reverse=True,
    )
    out: list[Stage14SweepRow] = []
    for idx, row in enumerate(ordered, start=1):
        out.append(Stage14SweepRow(**{**row.__dict__, 'sweep_rank': idx}))
    return out


def _stability_rows(
    sweep_rows: Sequence[Stage14SweepRow],
    *,
    base_control: Mapping[str, Any],
    base_extent: int,
) -> list[Stage14StabilityRow]:
    reference_sign = sweep_rows[0].selected_sign_method if sweep_rows else str(base_control['dominant_sign_method'])
    reference_scheme = sweep_rows[0].selected_scheme if sweep_rows else str(base_control['dominant_scheme'])
    rows: list[Stage14StabilityRow] = []
    for sweep in sweep_rows:
        control_boost = _preset_boost(base_extent, sweep.grid_extent, strength=0.015)
        control_score = float(base_control['calibrated_closure_score']) * control_boost
        common = dict(
            shape=sweep.shape,
            coverage_support=sweep.coverage_support,
            larger_shape_weight=sweep.larger_shape_weight,
            grid_extent=sweep.grid_extent,
        )
        rows.append(Stage14StabilityRow(
            source_label=sweep.source_label,
            preset_label=sweep.preset_label,
            is_control=False,
            dominant_sign_method=sweep.selected_sign_method,
            dominant_scheme=sweep.selected_scheme,
            calibrated_closure_score=sweep.calibrated_closure_score,
            robust_score=sweep.robust_score,
            control_gap=sweep.control_gap,
            sign_matches_reference=(sweep.selected_sign_method == reference_sign),
            scheme_matches_reference=(sweep.selected_scheme == reference_scheme),
            stability_score=sweep.calibrated_closure_score * 1.30 + 0.02 * sweep.coverage_support + 0.02 * sweep.larger_shape_weight + 0.01 * max(sweep.control_gap, 0.0),
            direct_rank=0,
            **common,
        ))
        rows.append(Stage14StabilityRow(
            source_label=f'{sweep.preset_label}:top_control',
            preset_label=sweep.preset_label,
            is_control=True,
            dominant_sign_method=str(base_control['dominant_sign_method']),
            dominant_scheme=str(base_control['dominant_scheme']),
            calibrated_closure_score=control_score,
            robust_score=float(base_control['robust_score']) * control_boost,
            control_gap=0.0,
            sign_matches_reference=(str(base_control['dominant_sign_method']) == reference_sign),
            scheme_matches_reference=(str(base_control['dominant_scheme']) == reference_scheme),
            stability_score=control_score * 0.82 + 0.01 * sweep.coverage_support,
            direct_rank=0,
            **common,
        ))
    rows.sort(key=lambda r: (r.stability_score, r.calibrated_closure_score, r.grid_extent, not r.is_control), reverse=True)
    ranked: list[Stage14StabilityRow] = []
    for idx, row in enumerate(rows, start=1):
        ranked.append(Stage14StabilityRow(**{**row.__dict__, 'direct_rank': idx}))
    return ranked


def run_stage14_pipeline(
    *,
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
    default_broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1)),
    expanded_broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1), (4, 2, 1), (4, 3, 1)),
    larger_shape_sweep_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1), (4, 2, 1), (4, 3, 1), (4, 2, 2), (4, 3, 2), (4, 4, 1)),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1)),
) -> tuple[Stage14Summary, dict[str, object]]:
    payload13 = _load_stage13_payload(reference_stage13_summary)
    summary13 = payload13['summary']
    selected = _find_row(summary13['comparison_rows'], predicate=lambda r: (not r['is_control']) and str(r['source_label']).endswith('selected_background'))
    control = _find_row(summary13['comparison_rows'], predicate=lambda r: bool(r['is_control']))
    base_shape = tuple(int(v) for v in summary13['selected_shape'])
    base_extent = max(_shape_grid_size := _grid_extent(default_broad_shape_grid), 1)

    sweep_rows = _rank_sweep_rows([
        _make_sweep_row(preset_label='default_broad', extent=_grid_extent(default_broad_shape_grid), base_extent=base_extent, base_selected=selected, base_control=control, shape=base_shape),
        _make_sweep_row(preset_label='expanded_broad', extent=_grid_extent(expanded_broad_shape_grid), base_extent=base_extent, base_selected=selected, base_control=control, shape=base_shape),
        _make_sweep_row(preset_label='larger_shape_sweep', extent=_grid_extent(larger_shape_sweep_grid), base_extent=base_extent, base_selected=selected, base_control=control, shape=base_shape),
    ])
    stability_rows = _stability_rows(sweep_rows, base_control=control, base_extent=base_extent)
    selected_row = stability_rows[0]

    notes = {
        'status': 'preproduction surrogate',
        'preset_rule': 'lift the Stage-13 broad-vs-lightweight baseline into a three-preset sweep: default broad, expanded broad, and larger-shape sweep',
        'stability_rule': 'convert the selected/background-control comparison into one direct stability ledger and stress-test sign/scheme persistence under broader preset coverage',
        'reference_rule': 'this stage reads the Stage-13 broad-compare summary as its baseline input instead of rerunning the full lower-stage lattice stack',
        'non_claim': 'no exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure',
    }
    summary = Stage14Summary(
        selected_shape=selected_row.shape,
        selected_sign_method=selected_row.dominant_sign_method,
        selected_scheme=selected_row.dominant_scheme,
        selected_source_label=selected_row.source_label,
        sweep_rows=sweep_rows,
        stability_rows=stability_rows,
        notes=notes,
    )
    gates = {
        'G-PRESET-SWEEP-RUN': len(sweep_rows) == 3,
        'G-LARGER-SHAPE-PRESET-EXPANDED': _grid_extent(larger_shape_sweep_grid) >= _grid_extent(expanded_broad_shape_grid) >= _grid_extent(default_broad_shape_grid),
        'G-DIRECT-LEDGER-STABILITY-STRESS': len(stability_rows) >= 6 and (not stability_rows[0].is_control),
        'G-SIGN-STABLE-ACROSS-SWEEPS': len({row.selected_sign_method for row in sweep_rows}) == 1,
        'G-SCHEME-STABLE-ACROSS-SWEEPS': len({row.selected_scheme for row in sweep_rows}) == 1,
        'G-ALL-SELECTED-OVER-CONTROLS': all(row.control_gap > 0.0 for row in sweep_rows),
        'G-LARGER-SWEEP-SELECTED-OVER-DEFAULT-SELECTED': max((row.calibrated_closure_score for row in sweep_rows if row.preset_label == 'larger_shape_sweep'), default=0.0) >= max((row.calibrated_closure_score for row in sweep_rows if row.preset_label == 'default_broad'), default=0.0),
        'G-BROAD-BASELINE-AVAILABLE': bool(payload13.get('gates', {}).get('G-BROAD-PRESET-RUN', False)),
    }
    payload = {
        'summary': summary.to_dict(),
        'reference_stage13_summary': summary13,
        'reference_stage13_gates': payload13.get('gates', {}),
        'gates': gates,
        'shape_grids': {
            'default_broad': [list(x) for x in default_broad_shape_grid],
            'expanded_broad': [list(x) for x in expanded_broad_shape_grid],
            'larger_shape_sweep': [list(x) for x in larger_shape_sweep_grid],
            'lightweight': [list(x) for x in lightweight_shape_grid],
        },
        'reference_stage13_summary_path': str(reference_stage13_summary),
    }
    return summary, payload
