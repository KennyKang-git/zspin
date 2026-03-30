from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links
from zsim.lgt.bcc import BCCLattice
from zsim.lgt.mbp import MBPResult, extract_mbp_bilinear, mbp_prefactor
from zsim.lgt.overlap import evaluate_overlap_background_with_method
from zsim.lgt.stage7 import Stage7Candidate, scan_stage7_valley_family, stage7_overlap_controls


@dataclass(frozen=True)
class Stage8SignRow:
    sign_method: str
    overlap_score: float
    chiral_abs_mean: float
    gw_residual: float
    pair_score: float
    score_stability: float

    def to_dict(self) -> dict[str, float | str]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage8LedgerRow:
    scheme: str
    sign_method: str
    mu2_formula_proxy: float
    gamma_h2_trace: float
    gamma_h2_fd: float
    gamma_consistency_gap: float
    overlap_score: float
    chiral_abs_mean: float
    gw_residual: float
    pair_score: float
    prefactor_exp_minus_2S: float
    mu2_weighted: float
    ledger_score: float

    def to_dict(self) -> dict[str, float | str]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage8Summary:
    best_stage7: Stage7Candidate
    sign_rows: list[Stage8SignRow]
    ledger_rows: list[Stage8LedgerRow]
    selected_sign_method: str
    selected_scheme: str
    prefactor_exp_minus_2S: float

    def to_dict(self) -> dict[str, object]:
        return {
            'best_stage7': self.best_stage7.to_dict(),
            'sign_rows': [r.to_dict() for r in self.sign_rows],
            'ledger_rows': [r.to_dict() for r in self.ledger_rows],
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'prefactor_exp_minus_2S': self.prefactor_exp_minus_2S,
        }


def _sign_weight(summary) -> float:
    return float(summary.score * (1.0 + summary.chiral_abs_mean) / (1.0 + summary.gw_residual))


def evaluate_sign_method_bundle(
    lattice: BCCLattice,
    links: dict[tuple[int, int], np.ndarray],
    *,
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational'),
    mass: float = 0.15,
    kappa: float = 0.6,
    wilson_r: float = 1.0,
    overlap_m0: float = 1.20,
    overlap_rho: float = 1.0,
    sign_epsilon: float = 1e-5,
    pair_count: int = 2,
    sample_size: int = 8,
) -> tuple[list[Stage8SignRow], str]:
    rows: list[Stage8SignRow] = []
    for method in sign_methods:
        summary = evaluate_overlap_background_with_method(
            lattice,
            links,
            mass=mass,
            kappa=kappa,
            r=wilson_r,
            m0=overlap_m0,
            rho=overlap_rho,
            sign_epsilon=sign_epsilon,
            pair_count=pair_count,
            sample_size=sample_size,
            sign_method=method,
        )
        stability = float(summary.score / (1.0 + summary.gw_residual))
        rows.append(Stage8SignRow(
            sign_method=method,
            overlap_score=float(summary.score),
            chiral_abs_mean=float(summary.chiral_abs_mean),
            gw_residual=float(summary.gw_residual),
            pair_score=float(summary.pairing.score),
            score_stability=stability,
        ))
    best = max(rows, key=lambda r: (r.score_stability, r.overlap_score, r.chiral_abs_mean))
    return rows, str(best.sign_method)


def build_stage8_ledger(
    lattice: BCCLattice,
    links: dict[tuple[int, int], np.ndarray],
    *,
    schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    selected_sign_method: str = 'smooth',
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
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
) -> tuple[list[Stage8LedgerRow], str]:
    overlap = evaluate_overlap_background_with_method(
        lattice,
        links,
        mass=mass,
        kappa=kappa,
        r=wilson_r,
        m0=overlap_m0,
        rho=overlap_rho,
        sign_epsilon=sign_epsilon,
        pair_count=2,
        sample_size=8,
        sign_method=selected_sign_method,
    )
    pref = mbp_prefactor()
    rows: list[Stage8LedgerRow] = []
    for scheme in schemes:
        mbp = extract_mbp_bilinear(
            lattice,
            links,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
            fermion_scheme=scheme,
            yt=yt,
            nc=nc,
            mass=mass,
            kappa=kappa,
            wilson_r=wilson_r,
            reg_epsilon=reg_epsilon,
            cutoff=cutoff,
            fd_step=fd_step,
        )
        mu2_weighted = float(mbp.mu2_formula_proxy * pref)
        ledger_score = float(mu2_weighted * (1.0 + _sign_weight(overlap)) / (1.0 + mbp.gamma_consistency_gap))
        rows.append(Stage8LedgerRow(
            scheme=str(scheme),
            sign_method=selected_sign_method,
            mu2_formula_proxy=float(mbp.mu2_formula_proxy),
            gamma_h2_trace=float(mbp.gamma_h2_trace),
            gamma_h2_fd=float(mbp.gamma_h2_fd),
            gamma_consistency_gap=float(mbp.gamma_consistency_gap),
            overlap_score=float(overlap.score),
            chiral_abs_mean=float(overlap.chiral_abs_mean),
            gw_residual=float(overlap.gw_residual),
            pair_score=float(overlap.pairing.score),
            prefactor_exp_minus_2S=float(pref),
            mu2_weighted=mu2_weighted,
            ledger_score=ledger_score,
        ))
    best = max(rows, key=lambda r: (r.ledger_score, -r.gamma_consistency_gap))
    return rows, str(best.scheme)


def run_stage8_pipeline(
    lattice: BCCLattice,
    *,
    amplitude_grid: Sequence[float] = (0.35, 0.55, 0.75),
    separation_grid: Sequence[float] = (0.55, 0.75, 0.95),
    width_grid: Sequence[float] = (0.45, 0.65),
    seam_bias_grid: Sequence[float] = (0.10, 0.18, 0.26),
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational'),
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
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
) -> tuple[Stage8Summary, dict[tuple[int, int], np.ndarray], dict[str, object]]:
    best_stage7, best_links, _ = scan_stage7_valley_family(
        lattice,
        amplitude_grid=amplitude_grid,
        separation_grid=separation_grid,
        width_grid=width_grid,
        seam_bias_grid=seam_bias_grid,
        scan_schemes=scan_schemes,
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
    sign_rows, selected_sign_method = evaluate_sign_method_bundle(
        lattice,
        best_links,
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
        best_links,
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
    controls = stage7_overlap_controls(
        lattice,
        amplitude=best_stage7.amplitude,
        separation=best_stage7.separation,
        width=best_stage7.width,
        seam_bias=best_stage7.seam_bias,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        schemes=compare_schemes,
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
    summary = Stage8Summary(
        best_stage7=best_stage7,
        sign_rows=sign_rows,
        ledger_rows=ledger_rows,
        selected_sign_method=selected_sign_method,
        selected_scheme=selected_scheme,
        prefactor_exp_minus_2S=mbp_prefactor(),
    )
    sign_map = {r.sign_method: r for r in sign_rows}
    ledger_map = {r.scheme: r for r in ledger_rows}
    gates = {
        'G-SIGN-METHOD-DIVERSITY': len({r.sign_method for r in sign_rows}) >= 3,
        'G-SIGN-SEPARATION': max(r.score_stability for r in sign_rows) - min(r.score_stability for r in sign_rows) >= 1.0e-8,
        'G-LEDGER-NONTRIVIAL': abs(max(r.ledger_score for r in ledger_rows) - min(r.ledger_score for r in ledger_rows)) >= 1.0e-18,
        'G-WILSON-IN-LEDGER': 'wilson4' in ledger_map,
        'G-SELECTED-SIGN-PRESENT': selected_sign_method in sign_map,
        'G-SELECTED-SCHEME-PRESENT': selected_scheme in ledger_map,
        'G-PREFACTOR-POSITIVE': float(summary.prefactor_exp_minus_2S) > 0.0,
    }
    payload = {
        'summary': summary.to_dict(),
        'controls': controls,
        'gates': gates,
        'notes': {
            'stage': 'controlled sign-function comparison + overlap-to-MBP ledger bridge',
            'status': 'preproduction-surrogate',
            'non_claim': 'not exact overlap on production lattice, not continuum caloron, not final Higgs bilinear closure',
        },
    }
    return summary, best_links, payload
