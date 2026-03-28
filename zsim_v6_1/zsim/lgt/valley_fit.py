from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

from zsim.lgt.backgrounds import caloron_pair_links
from zsim.lgt.bcc import BCCLattice
from zsim.lgt.fermion import gauge_covariant_hopping_matrix, smallest_singular_values
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.wilson import plaquette_observables


@dataclass(frozen=True)
class ValleyFitResult:
    amplitude: float
    separation: float
    width: float
    seam_bias: float
    score: float
    avg_plaquette: float
    wilson_action_proxy: float
    sigma_min: float
    sigma_next: float

    def to_dict(self) -> dict[str, float]:
        return {
            'amplitude': self.amplitude,
            'separation': self.separation,
            'width': self.width,
            'seam_bias': self.seam_bias,
            'score': self.score,
            'avg_plaquette': self.avg_plaquette,
            'wilson_action_proxy': self.wilson_action_proxy,
            'sigma_min': self.sigma_min,
            'sigma_next': self.sigma_next,
        }


def fit_caloron_valley_family(
    lattice: BCCLattice,
    *,
    amplitude_grid: Sequence[float],
    separation_grid: Sequence[float],
    width_grid: Sequence[float],
    seam_bias_grid: Sequence[float] = (0.15,),
    mass: float = 0.0,
) -> tuple[ValleyFitResult, dict[tuple[int, int], np.ndarray], list[ValleyFitResult]]:
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    best: ValleyFitResult | None = None
    best_links: dict[tuple[int, int], np.ndarray] | None = None
    rows: list[ValleyFitResult] = []
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
                    obs = plaquette_observables(links, plaquettes)
                    d0 = gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, links, mass=mass)
                    sigma = smallest_singular_values(d0, k=2)
                    sigma_min = sigma[0] if sigma else 0.0
                    sigma_next = sigma[1] if len(sigma) > 1 else sigma_min
                    action = float(obs['wilson_action_proxy'])
                    avg_plaq = float(obs['avg_plaquette'])
                    score = action / (sigma_min + 1.0e-6) + 0.15 * (1.0 - avg_plaq)
                    row = ValleyFitResult(float(amplitude), float(separation), float(width), float(seam_bias), float(score), avg_plaq, action, float(sigma_min), float(sigma_next))
                    rows.append(row)
                    if best is None or row.score > best.score:
                        best = row
                        best_links = links
    if best is None or best_links is None:
        raise ValueError('empty parameter grids supplied to fit_caloron_valley_family')
    return best, best_links, rows
