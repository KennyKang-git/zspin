from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from zsim.lgt.bcc import BCCLattice
from zsim.lgt.chirality import chirality_projector as reduced_chirality_projector
from zsim.lgt.fermion import gauge_covariant_hopping_matrix, staggered_color_operator, wilson_spinor_operator
from zsim.lgt.spinor import wilson_chirality_projector

Array = np.ndarray
ProjectorMode = Literal['center', 'corner', 'positive_x', 'negative_x', 'all']
FermionScheme = Literal['reduced2', 'staggered2', 'wilson4']


@dataclass(frozen=True)
class MBPResult:
    projector_mode: str
    chirality_mode: str
    fermion_scheme: str
    active_sites: int
    masked_modes: int
    y_norm: float
    reg_epsilon: float
    cutoff: float
    diag_term: float
    cross_term_half: float
    mbp_bracket: float
    mu2_formula_proxy: float
    gamma_h2_trace: float
    gamma_h2_fd: float
    gamma_consistency_gap: float
    sigma_min: float
    sigma_next: float
    k0_min_mode: float

    def to_dict(self) -> dict[str, float | int | str]:
        return self.__dict__.copy()


def _projector_mask(lattice: BCCLattice, mode: ProjectorMode) -> Array:
    site_types = np.asarray(lattice.site_types)
    positions = np.asarray(lattice.positions, dtype=float)
    if mode == 'center':
        return site_types == 'center'
    if mode == 'corner':
        return site_types == 'corner'
    if mode == 'positive_x':
        return positions[:, 0] >= float(np.mean(positions[:, 0]))
    if mode == 'negative_x':
        return positions[:, 0] < float(np.mean(positions[:, 0]))
    if mode == 'all':
        return np.ones(lattice.num_sites, dtype=bool)
    raise ValueError(f'unknown projector mode: {mode}')


def _site_internal_dim(fermion_scheme: FermionScheme) -> int:
    return 8 if fermion_scheme == 'wilson4' else 2


def _chirality_projector(lattice: BCCLattice, fermion_scheme: FermionScheme, chirality_mode: str) -> Array:
    return wilson_chirality_projector(lattice, chirality_mode) if fermion_scheme == 'wilson4' else reduced_chirality_projector(lattice, chirality_mode)


def build_yukawa_projector(lattice: BCCLattice, projector_mode: ProjectorMode = 'center', *, yt: float = 1.0, chirality_mode: str = 'vector', fermion_scheme: FermionScheme = 'reduced2') -> Array:
    mask = _projector_mask(lattice, projector_mode)
    internal_dim = _site_internal_dim(fermion_scheme)
    proj = np.kron(np.diag(mask.astype(float)), np.eye(internal_dim, dtype=np.complex128))
    x = np.asarray(lattice.positions, dtype=float)[:, 0]
    seam = np.sign(x - float(np.mean(x)))
    if chirality_mode == 'left':
        site_weights = 1.10 + 0.15 * seam
    elif chirality_mode == 'right':
        site_weights = 0.90 - 0.15 * seam
    else:
        site_weights = np.ones(lattice.num_sites, dtype=float)
    weight = np.kron(np.diag(site_weights), np.eye(internal_dim, dtype=np.complex128))
    return (float(yt) / np.sqrt(2.0)) * (proj @ weight @ _chirality_projector(lattice, fermion_scheme, chirality_mode))


def _d0_from_links(lattice: BCCLattice, links: dict[tuple[int, int], Array], *, fermion_scheme: FermionScheme, mass: float, kappa: float, wilson_r: float) -> Array:
    if fermion_scheme == 'reduced2':
        return gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, links, mass=mass, kappa=kappa)
    if fermion_scheme == 'staggered2':
        return staggered_color_operator(lattice, links, mass=mass, kappa=kappa)
    if fermion_scheme == 'wilson4':
        return wilson_spinor_operator(lattice, links, mass=mass, kappa=kappa, r=wilson_r)
    raise ValueError(f'unknown fermion scheme: {fermion_scheme}')


def k_matrices_from_links(lattice: BCCLattice, links: dict[tuple[int, int], Array], *, projector_mode: ProjectorMode = 'center', yt: float = 1.0, chirality_mode: str = 'vector', fermion_scheme: FermionScheme = 'reduced2', mass: float = 0.0, kappa: float = 1.0, wilson_r: float = 1.0, reg_epsilon: float = 1e-6) -> tuple[Array, Array, Array, Array, Array]:
    d0 = _d0_from_links(lattice, links, fermion_scheme=fermion_scheme, mass=mass, kappa=kappa, wilson_r=wilson_r)
    y = build_yukawa_projector(lattice, projector_mode, yt=yt, chirality_mode=chirality_mode, fermion_scheme=fermion_scheme)
    k0 = d0.conj().T @ d0 + float(reg_epsilon) * np.eye(d0.shape[0], dtype=np.complex128)
    k1 = d0.conj().T @ y + y.conj().T @ d0
    k2 = y.conj().T @ y
    return d0, y, k0, k1, k2


def masked_inverse_from_k0(k0: Array, *, cutoff: float = 1e-8) -> tuple[Array, Array, Array]:
    evals, evecs = np.linalg.eigh(k0)
    mask = evals > float(cutoff)
    if not np.any(mask):
        raise ValueError('no eigenmodes survived the prime cutoff')
    kept = evals[mask]
    vecs = evecs[:, mask]
    inv_prime = (vecs / kept) @ vecs.conj().T
    return inv_prime, kept, mask


def gamma_from_k(k: Array, *, cutoff: float = 1e-8, nc: float = 3.0) -> float:
    kept = np.linalg.eigvalsh(k)
    kept = kept[kept > float(cutoff)]
    if kept.size == 0:
        raise ValueError('no eigenvalues survived the prime cutoff in gamma evaluation')
    return float(-(float(nc) / 2.0) * np.sum(np.log(np.real_if_close(kept))))


def finite_difference_gamma_h2(k0: Array, k1: Array, k2: Array, *, fd_step: float = 1e-3, cutoff: float = 1e-8, nc: float = 3.0) -> float:
    h = float(fd_step)
    g0 = gamma_from_k(k0, cutoff=cutoff, nc=nc)
    gp = gamma_from_k(k0 + h * k1 + h * h * k2, cutoff=cutoff, nc=nc)
    gm = gamma_from_k(k0 - h * k1 + h * h * k2, cutoff=cutoff, nc=nc)
    return float((gp - 2.0 * g0 + gm) / (2.0 * h * h))


def extract_mbp_bilinear(lattice: BCCLattice, links: dict[tuple[int, int], Array], *, projector_mode: ProjectorMode = 'center', chirality_mode: str = 'vector', fermion_scheme: FermionScheme = 'reduced2', yt: float = 1.0, nc: float = 3.0, mass: float = 0.0, kappa: float = 1.0, wilson_r: float = 1.0, reg_epsilon: float = 1e-6, cutoff: float = 1e-8, fd_step: float = 1e-3) -> MBPResult:
    d0, y, k0, k1, k2 = k_matrices_from_links(lattice, links, projector_mode=projector_mode, yt=yt, chirality_mode=chirality_mode, fermion_scheme=fermion_scheme, mass=mass, kappa=kappa, wilson_r=wilson_r, reg_epsilon=reg_epsilon)
    k0_inv, kept, _ = masked_inverse_from_k0(k0, cutoff=cutoff)
    diag_term = float(np.real(np.trace(k0_inv @ k2)))
    cross_half = 0.5 * float(np.real(np.trace(k0_inv @ k1 @ k0_inv @ k1)))
    mbp_bracket = diag_term - cross_half
    gamma_h2_trace = float(-(float(nc) / 2.0) * mbp_bracket)
    gamma_h2_fd = finite_difference_gamma_h2(k0, k1, k2, fd_step=fd_step, cutoff=cutoff, nc=nc)
    svals = np.sort(np.linalg.svd(d0, compute_uv=False))
    sigma_min = float(np.real_if_close(svals[0])) if svals.size else 0.0
    sigma_next = float(np.real_if_close(svals[1])) if svals.size > 1 else sigma_min
    return MBPResult(str(projector_mode), str(chirality_mode), str(fermion_scheme), int(np.count_nonzero(_projector_mask(lattice, projector_mode))), int(kept.size), float(np.linalg.norm(y)), float(reg_epsilon), float(cutoff), diag_term, cross_half, float(mbp_bracket), float(nc) * float(mbp_bracket), gamma_h2_trace, gamma_h2_fd, float(abs(gamma_h2_trace - gamma_h2_fd)), sigma_min, sigma_next, float(np.min(kept)))


def mbp_prefactor(s_cl: float = 35.0 * np.pi / 3.0) -> float:
    return float(np.exp(-2.0 * float(s_cl)))
