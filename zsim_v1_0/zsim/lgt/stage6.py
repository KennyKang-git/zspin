from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links, scrambled_caloron_links
from zsim.lgt.bcc import BCCLattice
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear, k_matrices_from_links
from zsim.lgt.pairing import NearZeroPairingSummary, analyze_near_zero_pairs_from_matrix
from zsim.lgt.su2_links import identity_links, random_su2_links
from zsim.lgt.wilson import plaquette_observables


@dataclass(frozen=True)
class SchemeBundleRow:
    scheme: str
    mu2_formula_proxy: float
    gamma_consistency_gap: float
    sigma_min: float
    sigma_next: float
    pair_score: float
    pair_mean: float
    pair_gap_mean: float
    bulk_mean: float
    bulk_gap: float

    def to_dict(self) -> dict[str, float | str]:
        return self.__dict__.copy()


@dataclass(frozen=True)
class Stage6Candidate:
    amplitude: float
    separation: float
    width: float
    seam_bias: float
    objective: float
    pair_score_mean: float
    scheme_spread: float
    gamma_gap_max: float
    avg_plaquette: float
    wilson_action_proxy: float

    def to_dict(self) -> dict[str, float]:
        return self.__dict__.copy()


def evaluate_scheme_bundle(
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
) -> tuple[list[SchemeBundleRow], dict[str, float | bool]]:
    rows: list[SchemeBundleRow] = []
    for scheme in schemes:
        result = extract_mbp_bilinear(
            lattice,
            links,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
            fermion_scheme=str(scheme),
            yt=yt,
            nc=nc,
            mass=mass,
            kappa=kappa,
            wilson_r=wilson_r,
            reg_epsilon=reg_epsilon,
            cutoff=cutoff,
            fd_step=fd_step,
        )
        d0, *_ = k_matrices_from_links(
            lattice,
            links,
            projector_mode=projector_mode,
            chirality_mode=chirality_mode,
            fermion_scheme=str(scheme),
            mass=mass,
            kappa=kappa,
            wilson_r=wilson_r,
            reg_epsilon=reg_epsilon,
        )
        # Pairing is assessed on the background-sensitive part of D0 rather than on the trivial mass floor.
        d0_pair = d0 - float(mass) * np.eye(d0.shape[0], dtype=np.complex128)
        pairing = analyze_near_zero_pairs_from_matrix(d0_pair, pair_count=pair_count, sample_size=sample_size)
        rows.append(
            SchemeBundleRow(
                scheme=str(scheme),
                mu2_formula_proxy=float(result.mu2_formula_proxy),
                gamma_consistency_gap=float(result.gamma_consistency_gap),
                sigma_min=float(result.sigma_min),
                sigma_next=float(result.sigma_next),
                pair_score=float(pairing.score),
                pair_mean=float(pairing.pair_mean),
                pair_gap_mean=float(pairing.pair_gap_mean),
                bulk_mean=float(pairing.bulk_mean),
                bulk_gap=float(pairing.bulk_gap),
            )
        )
    mu2_vals = np.asarray([row.mu2_formula_proxy for row in rows], dtype=float)
    pair_vals = np.asarray([row.pair_score for row in rows], dtype=float)
    gamma_vals = np.asarray([row.gamma_consistency_gap for row in rows], dtype=float)
    nz_signs = np.sign(mu2_vals[np.abs(mu2_vals) > 1.0e-10])
    harness = {
        'scheme_count': int(len(rows)),
        'sign_consistent': bool(len(set(nz_signs.tolist())) <= 1),
        'scheme_spread': float(np.std(mu2_vals) / (np.mean(np.abs(mu2_vals)) + 1.0e-12)),
        'pair_score_mean': float(np.mean(pair_vals)),
        'pair_score_min': float(np.min(pair_vals)),
        'pair_score_std': float(np.std(pair_vals)),
        'gamma_gap_max': float(np.max(gamma_vals)),
        'gamma_gap_mean': float(np.mean(gamma_vals)),
    }
    return rows, harness


def scan_stage6_valley_family(
    lattice: BCCLattice,
    *,
    amplitude_grid: Sequence[float],
    separation_grid: Sequence[float],
    width_grid: Sequence[float],
    seam_bias_grid: Sequence[float],
    scan_schemes: Sequence[str] = ('reduced2', 'staggered2'),
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
) -> tuple[Stage6Candidate, dict[tuple[int, int], np.ndarray], list[Stage6Candidate]]:
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    best: Stage6Candidate | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    rows: list[Stage6Candidate] = []
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
                    scheme_rows, harness = evaluate_scheme_bundle(
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
                    )
                    obs = plaquette_observables(links, plaquettes)
                    objective = float(harness['pair_score_mean']) * (1.0 + float(obs['avg_plaquette'])) / (1.0 + float(harness['scheme_spread']) + float(harness['gamma_gap_max']))
                    row = Stage6Candidate(
                        amplitude=float(amplitude),
                        separation=float(separation),
                        width=float(width),
                        seam_bias=float(seam_bias),
                        objective=objective,
                        pair_score_mean=float(harness['pair_score_mean']),
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
        raise ValueError('empty grids supplied to scan_stage6_valley_family')
    return best, best_links, rows


def stage6_pairing_controls(
    lattice: BCCLattice,
    *,
    amplitude: float,
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
    seed: int = 350437,
) -> dict[str, dict[str, object]]:
    controls = {
        'identity': identity_links(lattice.edges),
        'haar': random_su2_links(lattice.edges, seed=seed),
        'scrambled_caloron': scrambled_caloron_links(lattice.edges, lattice.positions, amplitude, seed=seed + 11),
    }
    out: dict[str, dict[str, object]] = {}
    for label, links in controls.items():
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
        out[label] = {
            'rows': [row.to_dict() for row in rows],
            'harness': harness,
        }
    return out
