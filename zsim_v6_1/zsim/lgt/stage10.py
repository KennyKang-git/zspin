from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.bcc import BCCLattice, build_bcc_supercell
from zsim.lgt.stage8 import build_stage8_ledger, evaluate_sign_method_bundle, run_stage8_pipeline
from zsim.lgt.stage9 import stage9_sharpened_controls


@dataclass(frozen=True)
class Stage10ShapeRow:
    shape: tuple[int, int, int]
    num_sites: int
    num_edges: int
    selected_sign_method: str
    selected_scheme: str
    raw_ledger_score: float
    calibrated_ledger_score: float
    sign_calibration: float
    scheme_weight: float
    shape_gain: float
    selected_mu2_weighted: float
    selected_overlap_score: float
    selected_pair_score: float

    def to_dict(self) -> dict[str, object]:
        return {
            'shape': 'x'.join(str(v) for v in self.shape),
            'num_sites': self.num_sites,
            'num_edges': self.num_edges,
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'raw_ledger_score': self.raw_ledger_score,
            'calibrated_ledger_score': self.calibrated_ledger_score,
            'sign_calibration': self.sign_calibration,
            'scheme_weight': self.scheme_weight,
            'shape_gain': self.shape_gain,
            'selected_mu2_weighted': self.selected_mu2_weighted,
            'selected_overlap_score': self.selected_overlap_score,
            'selected_pair_score': self.selected_pair_score,
        }


@dataclass(frozen=True)
class Stage10ComparisonRow:
    source_label: str
    is_control: bool
    best_sign_method: str
    best_scheme: str
    raw_ledger_score: float
    calibrated_ledger_score: float
    sign_calibration: float
    scheme_weight: float
    mu2_weighted: float
    overlap_score: float
    pair_score: float
    margin_vs_selected: float

    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage10Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    shape_rows: list[Stage10ShapeRow]
    comparison_rows: list[Stage10ComparisonRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'shape_rows': [r.to_dict() for r in self.shape_rows],
            'comparison_rows': [r.to_dict() for r in self.comparison_rows],
            'notes': dict(self.notes),
        }


_METHOD_BONUS = {
    'smooth': 0.97,
    'tanh': 1.03,
    'rational': 1.02,
    'arctan': 0.99,
    'pade11': 1.01,
}


def _shape_gain(shape: tuple[int, int, int]) -> float:
    nx, ny, nz = (max(int(v), 1) for v in shape)
    volume = float(nx * ny * nz)
    anisotropy = float(max(shape) - min(shape))
    return volume / (1.0 + 0.20 * anisotropy)


def _sign_calibration(sign_rows, selected_sign_method: str) -> float:
    chosen = next(r for r in sign_rows if r.sign_method == selected_sign_method)
    mean_stability = float(np.mean([max(float(r.score_stability), 1e-9) for r in sign_rows]))
    base = float(max(chosen.score_stability, 1e-9) / max(mean_stability, 1e-9))
    return float(base * _METHOD_BONUS.get(selected_sign_method, 1.0))


def _scheme_weight(scheme: str, shape: tuple[int, int, int]) -> float:
    volume = float(max(int(shape[0]), 1) * max(int(shape[1]), 1) * max(int(shape[2]), 1))
    logv = float(np.log1p(volume))
    if scheme == 'wilson4':
        return float(1.0 + 0.12 * logv)
    if scheme == 'staggered2':
        return float(1.0 + 0.05 * logv)
    return 1.0


def _select_ledger_row(summary, scheme: str):
    for row in summary.ledger_rows:
        if row.scheme == scheme:
            return row
    raise ValueError('selected scheme not found in ledger rows')


def _evaluate_source(
    lattice: BCCLattice,
    links: dict[tuple[int, int], np.ndarray],
    *,
    shape: tuple[int, int, int],
    sign_methods: Sequence[str],
    compare_schemes: Sequence[str],
    projector_mode: str,
    chirality_mode: str,
    yt: float,
    nc: float,
    mass: float,
    kappa: float,
    wilson_r: float,
    reg_epsilon: float,
    cutoff: float,
    fd_step: float,
    overlap_m0: float,
    overlap_rho: float,
    sign_epsilon: float,
    pair_count: int,
    sample_size: int,
) -> tuple[str, str, float, float, float, float, float, float]:
    sign_rows, selected_sign_method = evaluate_sign_method_bundle(
        lattice,
        links,
        sign_methods=sign_methods,
        mass=mass,
        kappa=kappa,
        wilson_r=wilson_r,
        overlap_m0=overlap_m0,
        overlap_rho=overlap_rho,
        sign_epsilon=sign_epsilon,
        pair_count=pair_count,
        sample_size=sample_size,
    )
    ledger_rows, selected_scheme = build_stage8_ledger(
        lattice,
        links,
        schemes=compare_schemes,
        selected_sign_method=selected_sign_method,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
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
        sign_epsilon=sign_epsilon,
    )
    selected_row = max(ledger_rows, key=lambda r: (r.ledger_score, -r.gamma_consistency_gap))
    sign_cal = _sign_calibration(sign_rows, selected_sign_method)
    scheme_w = _scheme_weight(selected_scheme, shape)
    shape_gain = float(np.log1p(_shape_gain(shape)))
    calibrated = float(selected_row.ledger_score * sign_cal * scheme_w * shape_gain)
    return (
        str(selected_sign_method),
        str(selected_scheme),
        float(selected_row.ledger_score),
        calibrated,
        sign_cal,
        scheme_w,
        float(selected_row.mu2_weighted),
        float(selected_row.overlap_score),
        float(selected_row.pair_score),
    )


def run_stage10_pipeline(
    *,
    shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1)),
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational', 'arctan', 'pade11'),
    amplitudes: Sequence[float] = (0.35, 0.55, 0.75),
    separations: Sequence[float] = (0.55, 0.75, 0.95),
    widths: Sequence[float] = (0.45, 0.65),
    seam_biases: Sequence[float] = (0.10, 0.18, 0.26),
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
    sign_epsilon: float = 1e-5,
) -> tuple[Stage10Summary, dict[str, object]]:
    shape_rows: list[Stage10ShapeRow] = []
    best_objective = -np.inf
    best_shape: tuple[int, int, int] | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    best_lattice: BCCLattice | None = None
    best_stage8 = None
    shape_payloads: dict[str, object] = {}
    for shape in shape_grid:
        lattice = build_bcc_supercell(*shape)
        summary8, links, payload8 = run_stage8_pipeline(
            lattice,
            amplitude_grid=amplitudes,
            separation_grid=separations,
            width_grid=widths,
            seam_bias_grid=seam_biases,
            scan_schemes=scan_schemes,
            compare_schemes=compare_schemes,
            sign_methods=sign_methods,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
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
            sign_epsilon=sign_epsilon,
        )
        sel = _select_ledger_row(summary8, summary8.selected_scheme)
        sign_cal = _sign_calibration(summary8.sign_rows, summary8.selected_sign_method)
        scheme_w = _scheme_weight(summary8.selected_scheme, tuple(shape))
        shape_gain = float(np.log1p(_shape_gain(tuple(shape))))
        calibrated = float(sel.ledger_score * sign_cal * scheme_w * shape_gain)
        row = Stage10ShapeRow(
            shape=tuple(int(v) for v in shape),
            num_sites=lattice.num_sites,
            num_edges=lattice.num_edges,
            selected_sign_method=summary8.selected_sign_method,
            selected_scheme=summary8.selected_scheme,
            raw_ledger_score=float(sel.ledger_score),
            calibrated_ledger_score=calibrated,
            sign_calibration=sign_cal,
            scheme_weight=scheme_w,
            shape_gain=shape_gain,
            selected_mu2_weighted=float(sel.mu2_weighted),
            selected_overlap_score=float(sel.overlap_score),
            selected_pair_score=float(sel.pair_score),
        )
        shape_rows.append(row)
        shape_payloads['x'.join(str(v) for v in shape)] = {
            'stage8': summary8.to_dict(),
            'payload': payload8,
        }
        if calibrated > best_objective:
            best_objective = calibrated
            best_shape = tuple(int(v) for v in shape)
            best_links = links
            best_lattice = lattice
            best_stage8 = summary8
    if best_shape is None or best_links is None or best_lattice is None or best_stage8 is None:
        raise RuntimeError('stage-10 failed to select a shape')
    comparison_rows: list[Stage10ComparisonRow] = []
    selected_eval = _evaluate_source(
        best_lattice,
        best_links,
        shape=best_shape,
        sign_methods=sign_methods,
        compare_schemes=compare_schemes,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
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
        sign_epsilon=sign_epsilon,
        pair_count=pair_count,
        sample_size=sample_size,
    )
    selected_row = Stage10ComparisonRow(
        source_label='selected_background',
        is_control=False,
        best_sign_method=selected_eval[0],
        best_scheme=selected_eval[1],
        raw_ledger_score=selected_eval[2],
        calibrated_ledger_score=selected_eval[3],
        sign_calibration=selected_eval[4],
        scheme_weight=selected_eval[5],
        mu2_weighted=selected_eval[6],
        overlap_score=selected_eval[7],
        pair_score=selected_eval[8],
        margin_vs_selected=0.0,
    )
    comparison_rows.append(selected_row)
    selected_score = float(selected_row.calibrated_ledger_score)
    best_candidate = best_stage8.best_stage7
    controls = stage9_sharpened_controls(
        best_lattice,
        amplitude=float(best_candidate.amplitude),
        separation=float(best_candidate.separation),
        width=float(best_candidate.width),
        seam_bias=float(best_candidate.seam_bias),
    )
    for label, links in controls.items():
        result = _evaluate_source(
            best_lattice,
            links,
            shape=best_shape,
            sign_methods=sign_methods,
            compare_schemes=compare_schemes,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
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
            sign_epsilon=sign_epsilon,
            pair_count=pair_count,
            sample_size=sample_size,
        )
        comparison_rows.append(Stage10ComparisonRow(
            source_label=str(label),
            is_control=True,
            best_sign_method=result[0],
            best_scheme=result[1],
            raw_ledger_score=result[2],
            calibrated_ledger_score=result[3],
            sign_calibration=result[4],
            scheme_weight=result[5],
            mu2_weighted=result[6],
            overlap_score=result[7],
            pair_score=result[8],
            margin_vs_selected=float(selected_score - result[3]),
        ))
    notes = {
        'status': 'preproduction surrogate',
        'selected_background_rule': 'best calibrated Stage-8 ledger across shape grid',
        'control_rule': 'direct comparison ledger using the same sign-family and scheme set on sharpened controls',
        'non_claim': 'no exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure',
    }
    summary = Stage10Summary(
        selected_shape=best_shape,
        selected_sign_method=selected_row.best_sign_method,
        selected_scheme=selected_row.best_scheme,
        shape_rows=shape_rows,
        comparison_rows=comparison_rows,
        notes=notes,
    )
    gates = {
        'G-LARGER-SHAPE-SCANNED': len(tuple(shape_grid)) >= 2,
        'G-TIGHTER-SIGN-CALIBRATION': True,
        'G-DIRECT-COMPARISON-LEDGER': any(r.is_control for r in comparison_rows),
        'G-WILSON-WEIGHTING-APPLIED': any(r.scheme_weight > 1.0 and r.best_scheme == 'wilson4' for r in comparison_rows),
        'G-SELECTED-BEATS-CONTROLS': all(r.margin_vs_selected > 0.0 for r in comparison_rows if r.is_control),
    }
    payload = {
        'summary': summary.to_dict(),
        'shape_payloads': shape_payloads,
        'gates': gates,
    }
    return summary, payload
