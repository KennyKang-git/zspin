from __future__ import annotations

from dataclasses import asdict, dataclass
import random

from zsim.lgt.backgrounds import scrambled_caloron_links
from zsim.lgt.bcc import BCCLattice
from zsim.lgt.mbp import MBPResult, extract_mbp_bilinear
from zsim.lgt.su2_links import identity_links, random_su2_links


@dataclass(frozen=True)
class NegativeControlSummary:
    label: str
    mu2_formula_proxy: float
    gamma_consistency_gap: float
    sigma_min: float
    active_sites: int
    fermion_scheme: str

    def to_dict(self) -> dict[str, float | int | str]:
        return asdict(self)


def _random_support_mode(seed: int) -> str:
    return random.Random(seed).choice(['center', 'corner', 'positive_x', 'negative_x'])


def run_negative_controls(lattice: BCCLattice, base_links, *, amplitude: float, yt: float, nc: float, mass: float, reg_epsilon: float, cutoff: float, fd_step: float, seed: int, fermion_scheme: str = 'reduced2', kappa: float = 1.0, wilson_r: float = 1.0) -> dict[str, dict[str, float | int | str]]:
    controls: dict[str, MBPResult] = {}
    common = dict(fermion_scheme=fermion_scheme, yt=yt, nc=nc, mass=mass, kappa=kappa, wilson_r=wilson_r, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step)
    controls['identity_vector'] = extract_mbp_bilinear(lattice, identity_links(lattice.edges), projector_mode='center', chirality_mode='vector', **common)
    controls['haar_left'] = extract_mbp_bilinear(lattice, random_su2_links(lattice.edges, seed=seed), projector_mode='center', chirality_mode='left', **common)
    controls['scrambled_projector'] = extract_mbp_bilinear(lattice, base_links, projector_mode=_random_support_mode(seed + 17), chirality_mode='left', **common)
    controls['scrambled_caloron'] = extract_mbp_bilinear(lattice, scrambled_caloron_links(lattice.edges, lattice.positions, amplitude, seed=seed + 31), projector_mode='center', chirality_mode='left', **common)
    return {label: NegativeControlSummary(label, result.mu2_formula_proxy, result.gamma_consistency_gap, result.sigma_min, result.active_sites, result.fermion_scheme).to_dict() for label, result in controls.items()}
