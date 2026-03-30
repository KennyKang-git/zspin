from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.bcc import BCCLattice, build_bcc_supercell
from zsim.lgt.stage8 import run_stage8_pipeline
from zsim.lgt.stage9 import stage9_sharpened_controls
from zsim.lgt.stage10 import _evaluate_source, _shape_gain


@dataclass(frozen=True)
class Stage11ShapeRow:
    shape: tuple[int, int, int]
    num_sites: int
    num_edges: int
    dominant_sign_method: str
    dominant_scheme: str
    stress_mean_score: float
    stress_std_score: float
    robust_shape_score: float
    larger_shape_weight: float
    sign_method_consistency: float
    scheme_consistency: float
    stress_pass_fraction: float

    def to_dict(self) -> dict[str, object]:
        return {
            'shape': 'x'.join(str(v) for v in self.shape),
            'num_sites': self.num_sites,
            'num_edges': self.num_edges,
            'dominant_sign_method': self.dominant_sign_method,
            'dominant_scheme': self.dominant_scheme,
            'stress_mean_score': self.stress_mean_score,
            'stress_std_score': self.stress_std_score,
            'robust_shape_score': self.robust_shape_score,
            'larger_shape_weight': self.larger_shape_weight,
            'sign_method_consistency': self.sign_method_consistency,
            'scheme_consistency': self.scheme_consistency,
            'stress_pass_fraction': self.stress_pass_fraction,
        }


@dataclass(frozen=True)
class Stage11StressRow:
    source_label: str
    is_control: bool
    dominant_sign_method: str
    dominant_scheme: str
    stress_mean_score: float
    stress_std_score: float
    robust_score: float
    worst_score: float
    sign_method_consistency: float
    scheme_consistency: float
    stress_pass_fraction: float
    robust_margin_vs_selected: float

    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage11Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    shape_rows: list[Stage11ShapeRow]
    stress_rows: list[Stage11StressRow]
    sign_epsilon_grid: tuple[float, ...]
    fd_scale_grid: tuple[float, ...]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'shape_rows': [r.to_dict() for r in self.shape_rows],
            'stress_rows': [r.to_dict() for r in self.stress_rows],
            'sign_epsilon_grid': list(self.sign_epsilon_grid),
            'fd_scale_grid': list(self.fd_scale_grid),
            'notes': dict(self.notes),
        }


def _dominant_label(labels: Sequence[str]) -> tuple[str, float]:
    counter = Counter(str(x) for x in labels)
    if not counter:
        raise ValueError('empty label sequence')
    label, count = counter.most_common(1)[0]
    return label, float(count / max(len(labels), 1))




def _score_tolerance(*values: float) -> float:
    scale = max((abs(float(v)) for v in values), default=0.0)
    return float(max(1e-37, 1e-3 * scale))


def _score_geq(a: float, b: float) -> bool:
    return float(a) >= float(b) - _score_tolerance(a, b)
def _larger_shape_weight(shape: tuple[int, int, int], num_sites: int) -> float:
    gain = float(np.log1p(_shape_gain(shape)))
    site_weight = float(1.0 + 0.05 * np.log1p(max(num_sites, 1)))
    isotropy_bonus = float(1.0 / (1.0 + 0.15 * (max(shape) - min(shape))))
    return gain * site_weight * isotropy_bonus


def _stress_profile(
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
    sign_epsilon_grid: Sequence[float],
    fd_scale_grid: Sequence[float],
    overlap_m0: float,
    overlap_rho: float,
    pair_count: int,
    sample_size: int,
) -> dict[str, float | str]:
    scores: list[float] = []
    sign_labels: list[str] = []
    scheme_labels: list[str] = []
    mu2_values: list[float] = []
    overlap_values: list[float] = []
    pair_values: list[float] = []
    for sign_epsilon in sign_epsilon_grid:
        for fd_scale in fd_scale_grid:
            best_sign, best_scheme, raw, calibrated, sign_cal, scheme_w, mu2, overlap, pair = _evaluate_source(
                lattice,
                links,
                shape=shape,
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
                fd_step=float(fd_step * fd_scale),
                overlap_m0=overlap_m0,
                overlap_rho=overlap_rho,
                sign_epsilon=float(sign_epsilon),
                pair_count=pair_count,
                sample_size=sample_size,
            )
            del raw, sign_cal, scheme_w
            scores.append(float(calibrated))
            sign_labels.append(str(best_sign))
            scheme_labels.append(str(best_scheme))
            mu2_values.append(float(mu2))
            overlap_values.append(float(overlap))
            pair_values.append(float(pair))
    dominant_sign_method, sign_consistency = _dominant_label(sign_labels)
    dominant_scheme, scheme_consistency = _dominant_label(scheme_labels)
    scores_arr = np.asarray(scores, dtype=float)
    robust_score = float(np.mean(scores_arr) - np.std(scores_arr))
    return {
        'dominant_sign_method': dominant_sign_method,
        'dominant_scheme': dominant_scheme,
        'stress_mean_score': float(np.mean(scores_arr)),
        'stress_std_score': float(np.std(scores_arr)),
        'robust_score': robust_score,
        'worst_score': float(np.min(scores_arr)),
        'sign_method_consistency': float(sign_consistency),
        'scheme_consistency': float(scheme_consistency),
        'stress_pass_fraction': float(np.mean(scores_arr > 0.0)),
        'mu2_mean': float(np.mean(mu2_values)),
        'overlap_mean': float(np.mean(overlap_values)),
        'pair_mean': float(np.mean(pair_values)),
    }


def run_stage11_pipeline(
    *,
    shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1)),
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
) -> tuple[Stage11Summary, dict[str, object]]:
    shape_rows: list[Stage11ShapeRow] = []
    shape_payloads: dict[str, object] = {}
    best_objective = -np.inf
    best_shape: tuple[int, int, int] | None = None
    best_lattice: BCCLattice | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    best_stage8 = None

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
            sign_epsilon=float(sign_epsilon_grid[len(sign_epsilon_grid)//2]),
        )
        stress = _stress_profile(
            lattice,
            links,
            shape=tuple(int(v) for v in shape),
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
            sign_epsilon_grid=sign_epsilon_grid,
            fd_scale_grid=fd_scale_grid,
            overlap_m0=overlap_m0,
            overlap_rho=overlap_rho,
            pair_count=pair_count,
            sample_size=sample_size,
        )
        weight = _larger_shape_weight(tuple(int(v) for v in shape), lattice.num_sites)
        robust_shape_score = float(stress['robust_score'] * weight)
        row = Stage11ShapeRow(
            shape=tuple(int(v) for v in shape),
            num_sites=lattice.num_sites,
            num_edges=lattice.num_edges,
            dominant_sign_method=str(stress['dominant_sign_method']),
            dominant_scheme=str(stress['dominant_scheme']),
            stress_mean_score=float(stress['stress_mean_score']),
            stress_std_score=float(stress['stress_std_score']),
            robust_shape_score=robust_shape_score,
            larger_shape_weight=float(weight),
            sign_method_consistency=float(stress['sign_method_consistency']),
            scheme_consistency=float(stress['scheme_consistency']),
            stress_pass_fraction=float(stress['stress_pass_fraction']),
        )
        shape_rows.append(row)
        shape_key = 'x'.join(str(v) for v in shape)
        shape_payloads[shape_key] = {
            'stage8': summary8.to_dict(),
            'payload': payload8,
            'stress_profile': stress,
        }
        if robust_shape_score > best_objective:
            best_objective = robust_shape_score
            best_shape = tuple(int(v) for v in shape)
            best_lattice = lattice
            best_links = links
            best_stage8 = summary8

    if best_shape is None or best_lattice is None or best_links is None or best_stage8 is None:
        raise RuntimeError('stage-11 failed to select a stressed shape/background')

    selected_stress = _stress_profile(
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
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        overlap_m0=overlap_m0,
        overlap_rho=overlap_rho,
        pair_count=pair_count,
        sample_size=sample_size,
    )
    stress_rows: list[Stage11StressRow] = [
        Stage11StressRow(
            source_label='selected_background',
            is_control=False,
            dominant_sign_method=str(selected_stress['dominant_sign_method']),
            dominant_scheme=str(selected_stress['dominant_scheme']),
            stress_mean_score=float(selected_stress['stress_mean_score']),
            stress_std_score=float(selected_stress['stress_std_score']),
            robust_score=float(selected_stress['robust_score']),
            worst_score=float(selected_stress['worst_score']),
            sign_method_consistency=float(selected_stress['sign_method_consistency']),
            scheme_consistency=float(selected_stress['scheme_consistency']),
            stress_pass_fraction=float(selected_stress['stress_pass_fraction']),
            robust_margin_vs_selected=0.0,
        )
    ]
    selected_robust = float(selected_stress['robust_score'])

    best_candidate = best_stage8.best_stage7
    controls = stage9_sharpened_controls(
        best_lattice,
        amplitude=float(best_candidate.amplitude),
        separation=float(best_candidate.separation),
        width=float(best_candidate.width),
        seam_bias=float(best_candidate.seam_bias),
    )
    control_profiles: dict[str, object] = {}
    for label, links in controls.items():
        stress = _stress_profile(
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
            sign_epsilon_grid=sign_epsilon_grid,
            fd_scale_grid=fd_scale_grid,
            overlap_m0=overlap_m0,
            overlap_rho=overlap_rho,
            pair_count=pair_count,
            sample_size=sample_size,
        )
        margin = float(selected_robust - float(stress['robust_score']))
        stress_rows.append(Stage11StressRow(
            source_label=str(label),
            is_control=True,
            dominant_sign_method=str(stress['dominant_sign_method']),
            dominant_scheme=str(stress['dominant_scheme']),
            stress_mean_score=float(stress['stress_mean_score']),
            stress_std_score=float(stress['stress_std_score']),
            robust_score=float(stress['robust_score']),
            worst_score=float(stress['worst_score']),
            sign_method_consistency=float(stress['sign_method_consistency']),
            scheme_consistency=float(stress['scheme_consistency']),
            stress_pass_fraction=float(stress['stress_pass_fraction']),
            robust_margin_vs_selected=margin,
        ))
        control_profiles[str(label)] = stress

    notes = {
        'status': 'preproduction surrogate',
        'shape_rule': 'select the shape/background family with the best stress-robust score over a broader larger-shape grid',
        'stress_rule': 'stress each source over sign-epsilon and finite-difference scale grids, then compare robust mean-minus-std scores',
        'non_claim': 'no exact continuum caloron, no production overlap lattice, no final Higgs bilinear closure',
    }
    summary = Stage11Summary(
        selected_shape=best_shape,
        selected_sign_method=str(selected_stress['dominant_sign_method']),
        selected_scheme=str(selected_stress['dominant_scheme']),
        shape_rows=shape_rows,
        stress_rows=stress_rows,
        sign_epsilon_grid=tuple(float(v) for v in sign_epsilon_grid),
        fd_scale_grid=tuple(float(v) for v in fd_scale_grid),
        notes=notes,
    )
    control_rows = [r for r in stress_rows if r.is_control]
    gates = {
        'G-BROADER-LARGER-SHAPE-GRID': len(tuple(shape_grid)) >= 4,
        'G-STRICTER-SIGN-KERNEL-DIAGNOSTICS': len(tuple(sign_epsilon_grid)) >= 3 and len(tuple(fd_scale_grid)) >= 2,
        'G-CLOSURE-LEDGER-STRESS-TEST': any(r.is_control for r in stress_rows),
        'G-SELECTED-ROBUST-OVER-CONTROLS': all(_score_geq(selected_robust, r.robust_score) for r in control_rows),
        'G-SCHEME-CONSISTENCY-ABOVE-HALF': float(selected_stress['scheme_consistency']) >= 0.5,
        'G-SIGN-CONSISTENCY-ABOVE-HALF': float(selected_stress['sign_method_consistency']) >= 0.5,
    }
    payload = {
        'summary': summary.to_dict(),
        'shape_payloads': shape_payloads,
        'selected_stress_profile': selected_stress,
        'control_stress_profiles': control_profiles,
        'gates': gates,
    }
    return summary, payload
