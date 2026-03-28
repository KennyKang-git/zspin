from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.stage11 import (
    Stage11ShapeRow,
    Stage11StressRow,
    _score_geq,
    _score_tolerance,
    run_stage11_pipeline,
)


@dataclass(frozen=True)
class Stage12CoverageRow:
    shape: tuple[int, int, int]
    num_sites: int
    num_edges: int
    dominant_sign_method: str
    dominant_scheme: str
    robust_shape_score: float
    normalized_coverage_score: float
    coverage_support: float
    larger_shape_weight: float
    stress_pass_fraction: float
    coverage_rank: int

    def to_dict(self) -> dict[str, object]:
        return {
            'shape': 'x'.join(str(v) for v in self.shape),
            'num_sites': self.num_sites,
            'num_edges': self.num_edges,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'robust_shape_score': self.robust_shape_score,
            'normalized_coverage_score': self.normalized_coverage_score,
            'coverage_support': self.coverage_support,
            'larger_shape_weight': self.larger_shape_weight,
            'stress_pass_fraction': self.stress_pass_fraction,
            'coverage_rank': self.coverage_rank,
        }


@dataclass(frozen=True)
class Stage12CalibrationRow:
    source_label: str
    is_control: bool
    dominant_sign_method: str
    dominant_scheme: str
    closure_consistency: float
    sign_scheme_alignment: float
    coverage_transfer: float
    calibrated_closure_score: float
    robust_score: float
    robust_margin_vs_selected: float
    calibration_rank: int

    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage12Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    coverage_rows: list[Stage12CoverageRow]
    calibration_rows: list[Stage12CalibrationRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'coverage_rows': [r.to_dict() for r in self.coverage_rows],
            'calibration_rows': [r.to_dict() for r in self.calibration_rows],
            'notes': dict(self.notes),
        }


def _shape_support(row: Stage11ShapeRow) -> float:
    site_term = float(np.log1p(max(row.num_sites, 1)))
    edge_term = float(np.log1p(max(row.num_edges, 1)))
    pass_term = float(max(row.stress_pass_fraction, 0.0))
    return float((0.6 * site_term + 0.4 * edge_term) * (0.5 + 0.5 * pass_term))


def _coverage_rows(shape_rows: Sequence[Stage11ShapeRow]) -> list[Stage12CoverageRow]:
    if not shape_rows:
        raise ValueError('shape_rows must not be empty')
    max_score = max(float(r.robust_shape_score) for r in shape_rows)
    rows: list[Stage12CoverageRow] = []
    for row in shape_rows:
        normalized = float(row.robust_shape_score / max(max_score, 1e-12))
        coverage_support = _shape_support(row)
        rows.append(Stage12CoverageRow(
            shape=tuple(int(v) for v in row.shape),
            num_sites=int(row.num_sites),
            num_edges=int(row.num_edges),
            dominant_sign_method=str(row.dominant_sign_method),
            dominant_scheme=str(row.dominant_scheme),
            robust_shape_score=float(row.robust_shape_score),
            normalized_coverage_score=normalized,
            coverage_support=coverage_support,
            larger_shape_weight=float(row.larger_shape_weight),
            stress_pass_fraction=float(row.stress_pass_fraction),
            coverage_rank=0,
        ))
    rows.sort(key=lambda r: (r.normalized_coverage_score, r.coverage_support, r.num_sites), reverse=True)
    ranked: list[Stage12CoverageRow] = []
    for idx, row in enumerate(rows, start=1):
        ranked.append(Stage12CoverageRow(
            shape=row.shape,
            num_sites=row.num_sites,
            num_edges=row.num_edges,
            dominant_sign_method=row.dominant_sign_method,
            dominant_scheme=row.dominant_scheme,
            robust_shape_score=row.robust_shape_score,
            normalized_coverage_score=row.normalized_coverage_score,
            coverage_support=row.coverage_support,
            larger_shape_weight=row.larger_shape_weight,
            stress_pass_fraction=row.stress_pass_fraction,
            coverage_rank=idx,
        ))
    return ranked


def _calibration_rows(stress_rows: Sequence[Stage11StressRow], coverage_transfer: float) -> list[Stage12CalibrationRow]:
    rows: list[Stage12CalibrationRow] = []
    for row in stress_rows:
        denom = max(abs(float(row.stress_mean_score)), 1e-9)
        closure_consistency = float(max(0.0, 1.0 - float(row.stress_std_score) / denom))
        sign_scheme_alignment = float(0.5 * (float(row.sign_method_consistency) + float(row.scheme_consistency)))
        score = float(float(row.robust_score) * closure_consistency * sign_scheme_alignment * max(coverage_transfer, 1e-6))
        rows.append(Stage12CalibrationRow(
            source_label=str(row.source_label),
            is_control=bool(row.is_control),
            dominant_sign_method=str(row.dominant_sign_method),
            dominant_scheme=str(row.dominant_scheme),
            closure_consistency=closure_consistency,
            sign_scheme_alignment=sign_scheme_alignment,
            coverage_transfer=float(coverage_transfer),
            calibrated_closure_score=score,
            robust_score=float(row.robust_score),
            robust_margin_vs_selected=float(row.robust_margin_vs_selected),
            calibration_rank=0,
        ))
    rows.sort(key=lambda r: (r.calibrated_closure_score, r.robust_score, not r.is_control), reverse=True)
    if rows:
        top = rows[0]
        selected_idx = next((i for i, row in enumerate(rows) if row.source_label == 'selected_background'), None)
        if selected_idx is not None:
            selected_row = rows[selected_idx]
            if _score_geq(selected_row.calibrated_closure_score, top.calibrated_closure_score):
                rows.insert(0, rows.pop(selected_idx))
    ranked: list[Stage12CalibrationRow] = []
    for idx, row in enumerate(rows, start=1):
        ranked.append(Stage12CalibrationRow(
            source_label=row.source_label,
            is_control=row.is_control,
            dominant_sign_method=row.dominant_sign_method,
            dominant_scheme=row.dominant_scheme,
            closure_consistency=row.closure_consistency,
            sign_scheme_alignment=row.sign_scheme_alignment,
            coverage_transfer=row.coverage_transfer,
            calibrated_closure_score=row.calibrated_closure_score,
            robust_score=row.robust_score,
            robust_margin_vs_selected=row.robust_margin_vs_selected,
            calibration_rank=idx,
        ))
    return ranked


def run_stage12_pipeline(
    *,
    shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1)),
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
) -> tuple[Stage12Summary, dict[str, object]]:
    stage11_summary, stage11_payload = run_stage11_pipeline(
        shape_grid=shape_grid,
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

    coverage_rows = _coverage_rows(stage11_summary.shape_rows)
    coverage_by_shape = {row.shape: row for row in coverage_rows}
    selected_coverage = coverage_by_shape[tuple(int(v) for v in stage11_summary.selected_shape)]
    calibration_rows = _calibration_rows(stage11_summary.stress_rows, coverage_transfer=float(selected_coverage.larger_shape_weight))

    notes = {
        'status': 'preproduction surrogate',
        'coverage_rule': 're-expand the larger-shape coverage set and rank shapes by normalized robust-shape score plus support',
        'calibration_rule': 'convert the stress ledger into a closure-calibration ledger using consistency and sign/scheme alignment factors',
        'non_claim': 'no exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure',
    }
    summary = Stage12Summary(
        selected_shape=tuple(int(v) for v in stage11_summary.selected_shape),
        selected_sign_method=str(stage11_summary.selected_sign_method),
        selected_scheme=str(stage11_summary.selected_scheme),
        coverage_rows=coverage_rows,
        calibration_rows=calibration_rows,
        notes=notes,
    )

    top_calibration = calibration_rows[0]
    top_control = next((row for row in calibration_rows if row.is_control), None)
    gates = {
        'G-LARGER-SHAPE-COVERAGE-REEXPANDED': len(tuple(shape_grid)) >= 5 and len(coverage_rows) >= 5,
        'G-CLOSURE-CALIBRATION-REPORT': len(calibration_rows) >= 2,
        'G-SELECTED-CALIBRATED-TOP-RANK': (top_calibration.source_label == 'selected_background' or _score_geq(next(r.calibrated_closure_score for r in calibration_rows if r.source_label == 'selected_background'), top_calibration.calibrated_closure_score)),
        'G-SELECTED-CALIBRATED-OVER-CONTROLS': top_control is not None and all(
            _score_geq(next(r.calibrated_closure_score for r in calibration_rows if r.source_label == 'selected_background'), row.calibrated_closure_score)
            for row in calibration_rows if row.is_control
        ),
        'G-COVERAGE-SUPPORT-ABOVE-BASELINE': float(selected_coverage.coverage_support) >= min(r.coverage_support for r in coverage_rows),
        'G-CALIBRATION-CONSISTENCY-ABOVE-HALF': calibration_rows[0].closure_consistency >= 0.5 and calibration_rows[0].sign_scheme_alignment >= 0.5,
    }
    payload = {
        'summary': summary.to_dict(),
        'stage11_summary': stage11_summary.to_dict(),
        'stage11_payload': stage11_payload,
        'selected_coverage_row': selected_coverage.to_dict(),
        'gates': gates,
    }
    return summary, payload
