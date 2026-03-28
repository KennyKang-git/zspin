from __future__ import annotations

import numpy as np

from zsim.lgt.bcc import BCCLattice
from zsim.lgt.spinor import directional_gamma, staggered_phase_for_edge

Array = np.ndarray


def gauge_covariant_hopping_matrix(num_sites: int, edges: list[tuple[int, int]] | tuple[tuple[int, int], ...], links: dict[tuple[int, int], Array], *, mass: float = 0.0, kappa: float = 1.0) -> Array:
    dim = 2 * num_sites
    mat = np.zeros((dim, dim), dtype=np.complex128)
    for site in range(num_sites):
        sl = slice(2 * site, 2 * site + 2)
        mat[sl, sl] = mass * np.eye(2)
    for edge in edges:
        i, j = edge
        U = links[edge] if edge in links else links[(j, i)]
        si = slice(2 * i, 2 * i + 2)
        sj = slice(2 * j, 2 * j + 2)
        mat[si, sj] += kappa * U
        mat[sj, si] += kappa * U.conj().T
    return mat


def staggered_color_operator(lattice: BCCLattice, links: dict[tuple[int, int], Array], *, mass: float = 0.0, kappa: float = 1.0) -> Array:
    dim = 2 * lattice.num_sites
    out = np.zeros((dim, dim), dtype=np.complex128)
    for site in range(lattice.num_sites):
        sl = slice(2 * site, 2 * site + 2)
        out[sl, sl] = mass * np.eye(2, dtype=np.complex128)
    for i, j in lattice.edges:
        U = links[(i, j)] if (i, j) in links else links[(j, i)]
        phase = staggered_phase_for_edge(lattice, i, j)
        si = slice(2 * i, 2 * i + 2)
        sj = slice(2 * j, 2 * j + 2)
        out[si, sj] += 0.5 * kappa * phase * U
        out[sj, si] -= 0.5 * kappa * phase * U.conj().T
    return out


def wilson_spinor_operator(lattice: BCCLattice, links: dict[tuple[int, int], Array], *, mass: float = 0.0, kappa: float = 1.0, r: float = 1.0) -> Array:
    dim_site = 8
    total = lattice.num_sites * dim_site
    out = np.zeros((total, total), dtype=np.complex128)
    ident4 = np.eye(4, dtype=np.complex128)
    ident8 = np.eye(dim_site, dtype=np.complex128)
    for site in range(lattice.num_sites):
        sl = slice(dim_site * site, dim_site * (site + 1))
        out[sl, sl] = mass * ident8
    for i, j in lattice.edges:
        diff = np.asarray(lattice.positions[j] - lattice.positions[i], dtype=float)
        gamma_dir = directional_gamma(diff)
        spin_fwd = r * ident4 - 1j * gamma_dir
        spin_bwd = r * ident4 + 1j * gamma_dir
        U = links[(i, j)] if (i, j) in links else links[(j, i)]
        si = slice(dim_site * i, dim_site * (i + 1))
        sj = slice(dim_site * j, dim_site * (j + 1))
        out[si, sj] += -float(kappa) * np.kron(U, spin_fwd)
        out[sj, si] += -float(kappa) * np.kron(U.conj().T, spin_bwd)
    return out


def smallest_singular_values(matrix: Array, k: int = 8) -> list[float]:
    values = np.linalg.svd(matrix, compute_uv=False)
    values = np.sort(np.real_if_close(values))
    return [float(v) for v in values[:k]]


def fermion_effective_action_proxy(matrix: Array, *, mu2: float = 1.0e-6) -> float:
    singular = np.linalg.svd(matrix, compute_uv=False)
    shifted = np.real_if_close(singular * singular + mu2)
    return float(0.5 * np.sum(np.log(shifted)))
