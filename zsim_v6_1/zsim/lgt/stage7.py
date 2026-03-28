from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links, scrambled_caloron_links
from zsim.lgt.bcc import BCCLattice
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear
from zsim.lgt.overlap import OverlapModeSummary, evaluate_overlap_background
from zsim.lgt.stage6 import SchemeBundleRow, evaluate_scheme_bundle
from zsim.lgt.su2_links import identity_links, random_su2_links, project_to_su2
from zsim.lgt.wilson import plaquette_observables


@dataclass(frozen=True)
class Stage7Candidate:
    amplitude: float
    separation: float
    width: float
    seam_bias: float
    objective: float
    pair_score_mean: float
    overlap_score: float
    overlap_chiral_abs_mean: float
    gw_residual: float
    scheme_spread: float
    gamma_gap_max: float
    avg_plaquette: float
    wilson_action_proxy: float

    def to_dict(self) -> dict[str, float]:
        return self.__dict__.copy()


def phase_scrambled_caloron_links(
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
    out: dict[tuple[int, int], np.ndarray] = {}
    for edge, mat in base.items():
        theta = rng.uniform(-np.pi, np.pi)
        rot = np.asarray([[np.exp(1j * theta), 0.0], [0.0, np.exp(-1j * theta)]], dtype=np.complex128)
        out[edge] = project_to_su2(rot @ mat)
    return out


def evaluate_stage7_bundle(
    lattice: BCCLattice,
    links: dict[tuple[int, int], np.ndarray],
    *,
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
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
) -> tuple[list[SchemeBundleRow], dict[str, float | bool], OverlapModeSummary]:
    rows, harness = evaluate_scheme_bundle(
        lattice,
        links,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        schemes=schemes,
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
    )
    overlap = evaluate_overlap_background(
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
    )
    harness = dict(harness)
    harness.update(
        {
            'overlap_score': float(overlap.score),
            'overlap_chiral_abs_mean': float(overlap.chiral_abs_mean),
            'overlap_gw_residual': float(overlap.gw_residual),
            'overlap_pair_score': float(overlap.pairing.score),
        }
    )
    return rows, harness, overlap


def scan_stage7_valley_family(
    lattice: BCCLattice,
    *,
    amplitude_grid: Sequence[float],
    separation_grid: Sequence[float],
    width_grid: Sequence[float],
    seam_bias_grid: Sequence[float],
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
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
) -> tuple[Stage7Candidate, dict[tuple[int, int], np.ndarray], list[Stage7Candidate]]:
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    best: Stage7Candidate | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    rows: list[Stage7Candidate] = []
    for amplitude in amplitude_grid:
        for separation in separation_grid:
            for width in width_grid:
                for seam_bias in seam_bias_grid:
                    links = caloron_pair_links(
                        lattice.edges,
                        lattice.positions,
                        float(amplitude),
                        separation=float(separation),
                        width=float(width),
                        seam_bias=float(seam_bias),
                    )
                    scheme_rows, harness, overlap = evaluate_stage7_bundle(
                        lattice,
                        links,
                        projector_mode=projector_mode,
                        chirality_mode=chirality_mode,
                        schemes=scan_schemes,
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
                    obs = plaquette_observables(links, plaquettes)
                    _ = scheme_rows
                    objective = float(harness['pair_score_mean']) * (1.0 + float(overlap.score)) * (1.0 + float(obs['avg_plaquette']))
                    objective /= 1.0 + float(harness['scheme_spread']) + float(harness['gamma_gap_max']) + float(overlap.gw_residual)
                    row = Stage7Candidate(
                        amplitude=float(amplitude),
                        separation=float(separation),
                        width=float(width),
                        seam_bias=float(seam_bias),
                        objective=float(objective),
                        pair_score_mean=float(harness['pair_score_mean']),
                        overlap_score=float(overlap.score),
                        overlap_chiral_abs_mean=float(overlap.chiral_abs_mean),
                        gw_residual=float(overlap.gw_residual),
                        scheme_spread=float(harness['scheme_spread']),
                        gamma_gap_max=float(harness['gamma_gap_max']),
                        avg_plaquette=float(obs['avg_plaquette']),
                        wilson_action_proxy=float(obs['wilson_action_proxy']),
                    )
                    rows.append(row)
                    if best is None or row.objective > best.objective:
                        best = row
                        best_links = links
    if best is None or best_links is None:
        raise ValueError('empty grids supplied to scan_stage7_valley_family')
    return best, best_links, rows


def stage7_overlap_controls(
    lattice: BCCLattice,
    *,
    amplitude: float,
    separation: float = 0.75,
    width: float = 0.55,
    seam_bias: float = 0.15,
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
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
    seed: int = 350437,
) -> dict[str, dict[str, object]]:
    controls = {
        'identity': identity_links(lattice.edges),
        'haar': random_su2_links(lattice.edges, seed=seed),
        'scrambled_caloron': scrambled_caloron_links(lattice.edges, lattice.positions, amplitude, seed=seed + 11),
        'phase_scrambled_caloron': phase_scrambled_caloron_links(lattice, amplitude, separation=separation, width=width, seam_bias=seam_bias, seed=seed + 29),
    }
    out: dict[str, dict[str, object]] = {}
    for label, links in controls.items():
        rows, harness, overlap = evaluate_stage7_bundle(
            lattice,
            links,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
            schemes=schemes,
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
        out[label] = {
            'rows': [row.to_dict() for row in rows],
            'harness': harness,
            'overlap': overlap.to_dict(),
        }
    return out
