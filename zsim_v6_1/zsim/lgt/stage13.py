from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from zsim.lgt.stage11 import _score_geq
from zsim.lgt.stage12 import Stage12CalibrationRow, Stage12CoverageRow, Stage12Summary, run_stage12_pipeline


@dataclass(frozen=True)
class Stage13PresetRow:
    preset_label: str
    shape: tuple[int, int, int]
    num_sites: int
    num_edges: int
    selected_sign_method: str
    selected_scheme: str
    normalized_coverage_score: float
    coverage_support: float
    larger_shape_weight: float
    calibrated_closure_score: float
    robust_score: float
    control_gap: float
    coverage_rank: int
    calibration_rank: int
    preset_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'preset_label': self.preset_label,
            'shape': 'x'.join(str(v) for v in self.shape),
            'num_sites': self.num_sites,
            'num_edges': self.num_edges,
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'normalized_coverage_score': self.normalized_coverage_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'calibrated_closure_score': self.calibrated_closure_score,
            'robust_score': self.robust_score,
            'control_gap': self.control_gap,
            'coverage_rank': self.coverage_rank,
            'calibration_rank': self.calibration_rank,
            'preset_rank': self.preset_rank,
        }


@dataclass(frozen=True)
class Stage13ComparisonRow:
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
    scheme_matches_broad: bool
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
            'scheme_matches_broad': self.scheme_matches_broad,
            'direct_rank': self.direct_rank,
        }


@dataclass(frozen=True)
class Stage13Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    selected_source_label: str
    preset_rows: list[Stage13PresetRow]
    comparison_rows: list[Stage13ComparisonRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_source_label': self.selected_source_label,
            'preset_rows': [r.to_dict() for r in self.preset_rows],
            'comparison_rows': [r.to_dict() for r in self.comparison_rows],
            'notes': dict(self.notes),
        }


def _coverage_map(summary: Stage12Summary) -> dict[tuple[int, int, int], Stage12CoverageRow]:
    return {tuple(row.shape): row for row in summary.coverage_rows}


def _selected_calibration(summary: Stage12Summary) -> Stage12CalibrationRow:
    row = next((r for r in summary.calibration_rows if r.source_label == 'selected_background'), None)
    if row is None:
        raise ValueError('selected_background calibration row not found')
    return row


def _top_control(summary: Stage12Summary) -> Stage12CalibrationRow:
    row = next((r for r in summary.calibration_rows if r.is_control), None)
    if row is None:
        raise ValueError('control calibration row not found')
    return row


def _shape_size(shape: tuple[int, int, int]) -> int:
    nx, ny, nz = shape
    return int(nx * ny * nz)


def _preset_row(preset_label: str, summary: Stage12Summary) -> Stage13PresetRow:
    coverage_row = _coverage_map(summary)[tuple(summary.selected_shape)]
    selected_row = _selected_calibration(summary)
    top_control = _top_control(summary)
    shape = tuple(int(v) for v in summary.selected_shape)
    return Stage13PresetRow(
        preset_label=preset_label,
        shape=shape,
        num_sites=coverage_row.num_sites,
        num_edges=coverage_row.num_edges,
        selected_sign_method=summary.selected_sign_method,
        selected_scheme=summary.selected_scheme,
        normalized_coverage_score=coverage_row.normalized_coverage_score,
        coverage_support=coverage_row.coverage_support,
        larger_shape_weight=coverage_row.larger_shape_weight,
        calibrated_closure_score=selected_row.calibrated_closure_score,
        robust_score=selected_row.robust_score,
        control_gap=selected_row.calibrated_closure_score - top_control.calibrated_closure_score,
        coverage_rank=coverage_row.coverage_rank,
        calibration_rank=selected_row.calibration_rank,
        preset_rank=0,
    )


def _rank_preset_rows(rows: Sequence[Stage13PresetRow]) -> list[Stage13PresetRow]:
    sorted_rows = sorted(
        rows,
        key=lambda r: (
            r.calibrated_closure_score,
            r.coverage_support,
            r.larger_shape_weight,
            _shape_size(r.shape),
            r.preset_label == 'default_broad',
        ),
        reverse=True,
    )
    ranked: list[Stage13PresetRow] = []
    for idx, row in enumerate(sorted_rows, start=1):
        ranked.append(Stage13PresetRow(
            preset_label=row.preset_label,
            shape=row.shape,
            num_sites=row.num_sites,
            num_edges=row.num_edges,
            selected_sign_method=row.selected_sign_method,
            selected_scheme=row.selected_scheme,
            normalized_coverage_score=row.normalized_coverage_score,
            coverage_support=row.coverage_support,
            larger_shape_weight=row.larger_shape_weight,
            calibrated_closure_score=row.calibrated_closure_score,
            robust_score=row.robust_score,
            control_gap=row.control_gap,
            coverage_rank=row.coverage_rank,
            calibration_rank=row.calibration_rank,
            preset_rank=idx,
        ))
    return ranked


def _comparison_rows(
    broad_summary: Stage12Summary,
    light_summary: Stage12Summary,
) -> list[Stage13ComparisonRow]:
    broad_preset = _preset_row('default_broad', broad_summary)
    light_preset = _preset_row('lightweight', light_summary)
    broad_control = _top_control(broad_summary)
    light_control = _top_control(light_summary)
    rows = [
        Stage13ComparisonRow(
            source_label='default_broad:selected_background',
            preset_label='default_broad',
            is_control=False,
            shape=broad_preset.shape,
            dominant_sign_method=broad_summary.selected_sign_method,
            dominant_scheme=broad_summary.selected_scheme,
            calibrated_closure_score=broad_preset.calibrated_closure_score,
            robust_score=broad_preset.robust_score,
            coverage_support=broad_preset.coverage_support,
            larger_shape_weight=broad_preset.larger_shape_weight,
            control_gap=broad_preset.control_gap,
            scheme_matches_broad=True,
            direct_rank=0,
        ),
        Stage13ComparisonRow(
            source_label='lightweight:selected_background',
            preset_label='lightweight',
            is_control=False,
            shape=light_preset.shape,
            dominant_sign_method=light_summary.selected_sign_method,
            dominant_scheme=light_summary.selected_scheme,
            calibrated_closure_score=light_preset.calibrated_closure_score,
            robust_score=light_preset.robust_score,
            coverage_support=light_preset.coverage_support,
            larger_shape_weight=light_preset.larger_shape_weight,
            control_gap=light_preset.control_gap,
            scheme_matches_broad=(
                light_summary.selected_sign_method == broad_summary.selected_sign_method
                and light_summary.selected_scheme == broad_summary.selected_scheme
            ),
            direct_rank=0,
        ),
        Stage13ComparisonRow(
            source_label=f'default_broad:{broad_control.source_label}',
            preset_label='default_broad',
            is_control=True,
            shape=broad_preset.shape,
            dominant_sign_method=broad_control.dominant_sign_method,
            dominant_scheme=broad_control.dominant_scheme,
            calibrated_closure_score=broad_control.calibrated_closure_score,
            robust_score=broad_control.robust_score,
            coverage_support=broad_preset.coverage_support,
            larger_shape_weight=broad_preset.larger_shape_weight,
            control_gap=0.0,
            scheme_matches_broad=(
                broad_control.dominant_sign_method == broad_summary.selected_sign_method
                and broad_control.dominant_scheme == broad_summary.selected_scheme
            ),
            direct_rank=0,
        ),
        Stage13ComparisonRow(
            source_label=f'lightweight:{light_control.source_label}',
            preset_label='lightweight',
            is_control=True,
            shape=light_preset.shape,
            dominant_sign_method=light_control.dominant_sign_method,
            dominant_scheme=light_control.dominant_scheme,
            calibrated_closure_score=light_control.calibrated_closure_score,
            robust_score=light_control.robust_score,
            coverage_support=light_preset.coverage_support,
            larger_shape_weight=light_preset.larger_shape_weight,
            control_gap=0.0,
            scheme_matches_broad=(
                light_control.dominant_sign_method == broad_summary.selected_sign_method
                and light_control.dominant_scheme == broad_summary.selected_scheme
            ),
            direct_rank=0,
        ),
    ]
    rows.sort(
        key=lambda r: (
            r.calibrated_closure_score,
            r.coverage_support,
            r.larger_shape_weight,
            (not r.is_control),
            r.preset_label == 'default_broad',
        ),
        reverse=True,
    )
    ranked: list[Stage13ComparisonRow] = []
    for idx, row in enumerate(rows, start=1):
        ranked.append(Stage13ComparisonRow(
            source_label=row.source_label,
            preset_label=row.preset_label,
            is_control=row.is_control,
            shape=row.shape,
            dominant_sign_method=row.dominant_sign_method,
            dominant_scheme=row.dominant_scheme,
            calibrated_closure_score=row.calibrated_closure_score,
            robust_score=row.robust_score,
            coverage_support=row.coverage_support,
            larger_shape_weight=row.larger_shape_weight,
            control_gap=row.control_gap,
            scheme_matches_broad=row.scheme_matches_broad,
            direct_rank=idx,
        ))
    return ranked


def run_stage13_pipeline(
    *,
    broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1)),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1)),
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational', 'arctan', 'pade11'),
    amplitudes: Sequence[float] = (0.35, 0.55, 0.75),
    separations: Sequence[float] = (0.55, 0.75, 0.95),
    widths: Sequence[float] = (0.45, 0.65),
    seam_biases: Sequence[float] = (0.10, 0.18, 0.26),
    sign_epsilon_grid: Sequence[float] = (5e-6, 1e-5, 2e-5),
    fd_scale_grid: Sequence[float] = (0.5, 1.0, 2.0),
    pair_count: int = 2,
    sample_size: int = 8,
    yt: float = 1.0,
    nc: float = 3.0,
    mass: float = 0.15,
    kappa: float = 0.6,
    wilson_r: float = 1.0,
    reg_epsilon: float = 1e-4,
    cutoff: float = 1e-6,
    fd_step: float = 5e-4,
    overlap_m0: float = 1.20,
    overlap_rho: float = 1.0,
) -> tuple[Stage13Summary, dict[str, object]]:
    broad_summary, broad_payload = run_stage12_pipeline(
        shape_grid=broad_shape_grid,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        scan_schemes=scan_schemes,
        compare_schemes=compare_schemes,
        sign_methods=sign_methods,
        amplitudes=amplitudes,
        separations=separations,
        widths=widths,
        seam_biases=seam_biases,
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        pair_count=pair_count,
        sample_size=sample_size,
        yt=yt,
        nc=nc,
        mass=mass,
        kappa=kappa,
        wilson_r=wilson_r,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        overlap_m0=overlap_m0,
        overlap_rho=overlap_rho,
    )
    light_summary, light_payload = run_stage12_pipeline(
        shape_grid=lightweight_shape_grid,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        scan_schemes=scan_schemes,
        compare_schemes=compare_schemes,
        sign_methods=sign_methods,
        amplitudes=amplitudes,
        separations=separations,
        widths=widths,
        seam_biases=seam_biases,
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        pair_count=pair_count,
        sample_size=sample_size,
        yt=yt,
        nc=nc,
        mass=mass,
        kappa=kappa,
        wilson_r=wilson_r,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        overlap_m0=overlap_m0,
        overlap_rho=overlap_rho,
    )

    preset_rows = _rank_preset_rows([
        _preset_row('default_broad', broad_summary),
        _preset_row('lightweight', light_summary),
    ])
    comparison_rows = _comparison_rows(broad_summary, light_summary)
    selected_row = comparison_rows[0]

    notes = {
        'status': 'preproduction surrogate',
        'preset_rule': 'run stage-12 twice: once with the default broad shape preset and once with the lightweight preset',
        'comparison_rule': 'compare the selected backgrounds and the top controls from each preset in one direct ledger',
        'non_claim': 'no exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure',
    }
    summary = Stage13Summary(
        selected_shape=selected_row.shape,
        selected_sign_method=selected_row.dominant_sign_method,
        selected_scheme=selected_row.dominant_scheme,
        selected_source_label=selected_row.source_label,
        preset_rows=preset_rows,
        comparison_rows=comparison_rows,
        notes=notes,
    )

    broad_preset = next(r for r in preset_rows if r.preset_label == 'default_broad')
    light_preset = next(r for r in preset_rows if r.preset_label == 'lightweight')
    gates = {
        'G-BROAD-PRESET-RUN': len(tuple(broad_shape_grid)) >= len(tuple(lightweight_shape_grid)) and len(broad_summary.coverage_rows) >= len(light_summary.coverage_rows),
        'G-DIRECT-COMPARISON-LEDGER': len(comparison_rows) >= 4,
        'G-BROAD-COVERAGE-SUPPORT-OVER-LIGHTWEIGHT': broad_preset.coverage_support >= light_preset.coverage_support,
        'G-BROAD-TOP-RANK-OR-TIE': broad_preset.calibrated_closure_score >= (light_preset.calibrated_closure_score - 1e-40),
        'G-BROAD-SCHEME-STABLE-VS-LIGHTWEIGHT': (
            broad_preset.selected_sign_method == light_preset.selected_sign_method
            and broad_preset.selected_scheme == light_preset.selected_scheme
        ),
        'G-BROAD-SELECTED-OVER-BROAD-CONTROL': _score_geq(broad_preset.calibrated_closure_score, broad_preset.calibrated_closure_score - broad_preset.control_gap),
        'G-LIGHTWEIGHT-SELECTED-OVER-LIGHTWEIGHT-CONTROL': _score_geq(light_preset.calibrated_closure_score, light_preset.calibrated_closure_score - light_preset.control_gap),
    }
    payload = {
        'summary': summary.to_dict(),
        'broad_summary': broad_summary.to_dict(),
        'broad_payload': broad_payload,
        'lightweight_summary': light_summary.to_dict(),
        'lightweight_payload': light_payload,
        'gates': gates,
    }
    return summary, payload
