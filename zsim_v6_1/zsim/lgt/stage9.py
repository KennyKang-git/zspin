from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links, scrambled_caloron_links
from zsim.lgt.bcc import BCCLattice, build_bcc_supercell
from zsim.lgt.stage7 import phase_scrambled_caloron_links
from zsim.lgt.stage8 import Stage8LedgerRow, Stage8Summary, run_stage8_pipeline
from zsim.lgt.su2_links import project_to_su2, random_su2, random_su2_links


@dataclass(frozen=True)
class Stage9ShapeRow:
    shape: tuple[int, int, int]
    num_sites: int
    num_edges: int
    selected_sign_method: str
    selected_scheme: str
    selected_ledger_score: float
    selected_mu2_weighted: float
    selected_overlap_score: float
    selected_pair_score: float
    shape_gain: float

    def to_dict(self) -> dict[str, object]:
        return {
            'shape': 'x'.join(str(v) for v in self.shape),
            'num_sites': self.num_sites,
            'num_edges': self.num_edges,
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'selected_ledger_score': self.selected_ledger_score,
            'selected_mu2_weighted': self.selected_mu2_weighted,
            'selected_overlap_score': self.selected_overlap_score,
            'selected_pair_score': self.selected_pair_score,
            'shape_gain': self.shape_gain,
        }


@dataclass(frozen=True)
class Stage9ControlRow:
    control_label: str
    best_ledger_score: float
    best_mu2_weighted: float
    best_overlap_score: float
    best_pair_score: float
    control_margin: float

    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage9Summary:
    selected_shape: tuple[int, int, int]
    selected_sign_method: str
    selected_scheme: str
    shape_rows: list[Stage9ShapeRow]
    control_rows: list[Stage9ControlRow]
    notes: dict[str, str]

    def to_dict(self) -> dict[str, object]:
        return {
            'selected_shape': list(self.selected_shape),
            'selected_sign_method': self.selected_sign_method,
            'selected_scheme': self.selected_scheme,
            'shape_rows': [r.to_dict() for r in self.shape_rows],
            'control_rows': [r.to_dict() for r in self.control_rows],
            'notes': dict(self.notes),
        }


def _selected_ledger_row(summary: Stage8Summary) -> Stage8LedgerRow:
    for row in summary.ledger_rows:
        if row.scheme == summary.selected_scheme:
            return row
    raise ValueError('selected scheme not found in ledger rows')


def edge_permuted_caloron_links(
    lattice: BCCLattice,
    amplitude: float,
    *,
    separation: float = 0.75,
    width: float = 0.55,
    seam_bias: float = 0.15,
    seed: int = 350437,
) -> dict[tuple[int, int], np.ndarray]:
    base = caloron_pair_links(
        lattice.edges,
        lattice.positions,
        amplitude,
        separation=separation,
        width=width,
        seam_bias=seam_bias,
    )
    rng = np.random.default_rng(seed)
    keys = list(base.keys())
    mats = [base[k] for k in keys]
    perm = rng.permutation(len(keys))
    return {keys[idx]: mats[int(perm[idx])] for idx in range(len(keys))}


def conjugation_scrambled_caloron_links(
    lattice: BCCLattice,
    amplitude: float,
    *,
    separation: float = 0.75,
    width: float = 0.55,
    seam_bias: float = 0.15,
    seed: int = 350438,
) -> dict[tuple[int, int], np.ndarray]:
    base = caloron_pair_links(
        lattice.edges,
        lattice.positions,
        amplitude,
        separation=separation,
        width=width,
        seam_bias=seam_bias,
    )
    rng = np.random.default_rng(seed)
    out: dict[tuple[int, int], np.ndarray] = {}
    for edge, mat in base.items():
        g = random_su2(rng=rng)
        out[edge] = project_to_su2(g @ mat @ g.conj().T)
    return out


def stage9_sharpened_controls(
    lattice: BCCLattice,
    *,
    amplitude: float,
    separation: float,
    width: float,
    seam_bias: float,
    seed: int = 350437,
) -> dict[str, dict[tuple[int, int], np.ndarray]]:
    return {
        'identity': {edge: np.eye(2, dtype=np.complex128) for edge in lattice.edges},
        'haar': random_su2_links(lattice.edges, seed=seed),
        'scrambled_caloron': scrambled_caloron_links(lattice.edges, lattice.positions, amplitude, seed=seed + 11),
        'phase_scrambled_caloron': phase_scrambled_caloron_links(lattice, amplitude, separation=separation, width=width, seam_bias=seam_bias, seed=seed + 29),
        'edge_permuted_caloron': edge_permuted_caloron_links(lattice, amplitude, separation=separation, width=width, seam_bias=seam_bias, seed=seed + 47),
        'conjugation_scrambled_caloron': conjugation_scrambled_caloron_links(lattice, amplitude, separation=separation, width=width, seam_bias=seam_bias, seed=seed + 71),
    }


def _shape_gain(shape: tuple[int, int, int]) -> float:
    nx, ny, nz = (max(int(v), 1) for v in shape)
    volume = float(nx * ny * nz)
    anisotropy = float(max(shape) - min(shape))
    return volume / (1.0 + 0.25 * anisotropy)


def run_stage9_pipeline(
    *,
    shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1)),
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
) -> tuple[Stage9Summary, dict[str, object]]:
    shape_rows: list[Stage9ShapeRow] = []
    shape_details: dict[str, object] = {}
    best_key: str | None = None
    best_objective = -np.inf
    best_summary: Stage8Summary | None = None
    best_payload: dict[str, object] | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    best_lattice: BCCLattice | None = None
    for shape in shape_grid:
        lattice = build_bcc_supercell(*shape)
        summary, links, payload = run_stage8_pipeline(
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
        selected = _selected_ledger_row(summary)
        gain = _shape_gain(shape)
        objective = float(selected.ledger_score * np.log1p(gain))
        row = Stage9ShapeRow(
            shape=tuple(int(v) for v in shape),
            num_sites=lattice.num_sites,
            num_edges=lattice.num_edges,
            selected_sign_method=summary.selected_sign_method,
            selected_scheme=summary.selected_scheme,
            selected_ledger_score=float(selected.ledger_score),
            selected_mu2_weighted=float(selected.mu2_weighted),
            selected_overlap_score=float(selected.overlap_score),
            selected_pair_score=float(selected.pair_score),
            shape_gain=float(gain),
        )
        shape_rows.append(row)
        key = 'x'.join(str(v) for v in shape)
        shape_details[key] = {
            'summary': summary.to_dict(),
            'payload': payload,
        }
        if objective > best_objective:
            best_objective = objective
            best_key = key
            best_summary = summary
            best_payload = payload
            best_links = links
            best_lattice = lattice
    if best_summary is None or best_payload is None or best_links is None or best_lattice is None or best_key is None:
        raise ValueError('empty shape-grid supplied to run_stage9_pipeline')
    best_stage7 = best_summary.best_stage7
    controls = stage9_sharpened_controls(
        best_lattice,
        amplitude=best_stage7.amplitude,
        separation=best_stage7.separation,
        width=best_stage7.width,
        seam_bias=best_stage7.seam_bias,
    )
    selected_ledger = _selected_ledger_row(best_summary)
    control_rows: list[Stage9ControlRow] = []
    control_details: dict[str, object] = {}
    for label, links in controls.items():
        control_summary, _control_links, control_payload = run_stage8_pipeline(
            best_lattice,
            amplitude_grid=(best_stage7.amplitude,),
            separation_grid=(best_stage7.separation,),
            width_grid=(best_stage7.width,),
            seam_bias_grid=(best_stage7.seam_bias,),
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
        ) if label == 'identity_via_stage8' else (None, None, None)
        # reuse direct ledger evaluation on supplied links to avoid re-scanning the family
        from zsim.lgt.stage8 import build_stage8_ledger, evaluate_sign_method_bundle
        sign_rows, selected_sign = evaluate_sign_method_bundle(
            best_lattice,
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
            best_lattice,
            links,
            schemes=compare_schemes,
            selected_sign_method=selected_sign,
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
        selected_control = next(row for row in ledger_rows if row.scheme == selected_scheme)
        control_rows.append(Stage9ControlRow(
            control_label=label,
            best_ledger_score=float(selected_control.ledger_score),
            best_mu2_weighted=float(selected_control.mu2_weighted),
            best_overlap_score=float(selected_control.overlap_score),
            best_pair_score=float(selected_control.pair_score),
            control_margin=float(selected_ledger.ledger_score - selected_control.ledger_score),
        ))
        control_details[label] = {
            'selected_sign_method': selected_sign,
            'selected_scheme': selected_scheme,
            'sign_rows': [r.to_dict() for r in sign_rows],
            'ledger_rows': [r.to_dict() for r in ledger_rows],
        }
    gates = {
        'G-SHAPE-DIVERSITY': len(shape_rows) >= 2,
        'G-EDGE-COUNT-MONOTONIC': max(r.num_edges for r in shape_rows) > min(r.num_edges for r in shape_rows),
        'G-SIGN-FAMILY-EXTENDED': len(set(sign_methods)) >= 5,
        'G-CONTROL-MARGINS-POSITIVE': all(r.control_margin > -1.0e-12 for r in control_rows),
        'G-HARD-CONTROLS-PRESENT': {'edge_permuted_caloron', 'conjugation_scrambled_caloron'} <= {r.control_label for r in control_rows},
        'G-WILSON-RETAINED': any(r.selected_scheme == 'wilson4' for r in shape_rows),
    }
    summary = Stage9Summary(
        selected_shape=tuple(int(v) for v in best_lattice.metadata['shape']),
        selected_sign_method=best_summary.selected_sign_method,
        selected_scheme=best_summary.selected_scheme,
        shape_rows=shape_rows,
        control_rows=control_rows,
        notes={
            'stage': 'shape-aware sign-family refinement + sharpened negative controls',
            'status': 'preproduction-surrogate',
            'non_claim': 'not exact continuum caloron, not production overlap lattice, not final Higgs bilinear closure',
        },
    )
    payload = {
        'summary': summary.to_dict(),
        'selected_shape_key': best_key,
        'shape_details': shape_details,
        'control_details': control_details,
        'gates': gates,
    }
    return summary, payload
