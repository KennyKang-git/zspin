from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt.bcc import BCCLattice

Array = np.ndarray

_SIGMA1 = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
_SIGMA2 = np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
_SIGMA3 = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
_I2 = np.eye(2, dtype=np.complex128)


@dataclass(frozen=True)
class EuclideanGammaSet:
    gamma1: Array
    gamma2: Array
    gamma3: Array
    gamma4: Array
    gamma5: Array

    @property
    def all(self) -> tuple[Array, Array, Array, Array]:
        return (self.gamma1, self.gamma2, self.gamma3, self.gamma4)


def euclidean_gamma_set() -> EuclideanGammaSet:
    gamma1 = np.block([[np.zeros((2, 2), dtype=np.complex128), -1j * _SIGMA1], [1j * _SIGMA1, np.zeros((2, 2), dtype=np.complex128)]])
    gamma2 = np.block([[np.zeros((2, 2), dtype=np.complex128), -1j * _SIGMA2], [1j * _SIGMA2, np.zeros((2, 2), dtype=np.complex128)]])
    gamma3 = np.block([[np.zeros((2, 2), dtype=np.complex128), -1j * _SIGMA3], [1j * _SIGMA3, np.zeros((2, 2), dtype=np.complex128)]])
    gamma4 = np.block([[np.zeros((2, 2), dtype=np.complex128), _I2], [_I2, np.zeros((2, 2), dtype=np.complex128)]])
    gamma5 = np.block([[_I2, np.zeros((2, 2), dtype=np.complex128)], [np.zeros((2, 2), dtype=np.complex128), -_I2]])
    return EuclideanGammaSet(gamma1=gamma1, gamma2=gamma2, gamma3=gamma3, gamma4=gamma4, gamma5=gamma5)


def directional_gamma(displacement: Array) -> Array:
    disp = np.asarray(displacement, dtype=float)
    spatial = disp[:3]
    norm = float(np.linalg.norm(spatial))
    if norm < 1e-12:
        return np.zeros((4, 4), dtype=np.complex128)
    nx, ny, nz = spatial / norm
    gs = euclidean_gamma_set()
    return nx * gs.gamma1 + ny * gs.gamma2 + nz * gs.gamma3


def staggered_phase_for_edge(lattice: BCCLattice, start: int, stop: int) -> float:
    coords = np.asarray(lattice.positions, dtype=float)
    origin = np.rint(2.0 * coords[start]).astype(int)
    delta = np.rint(2.0 * (coords[stop] - coords[start])).astype(int)
    axis = int(np.argmax(np.abs(delta[:3])))
    if axis == 0:
        return 1.0
    if axis == 1:
        return float((-1) ** origin[0])
    return float((-1) ** (origin[0] + origin[1]))


def wilson_gamma5_matrix(lattice: BCCLattice) -> Array:
    g5 = euclidean_gamma_set().gamma5
    block = np.kron(np.eye(2, dtype=np.complex128), g5)
    dim_site = 8
    total = lattice.num_sites * dim_site
    out = np.zeros((total, total), dtype=np.complex128)
    for site in range(lattice.num_sites):
        sl = slice(dim_site * site, dim_site * (site + 1))
        out[sl, sl] = block
    return out


def wilson_chirality_projector(lattice: BCCLattice, mode: str = 'vector') -> Array:
    g5 = wilson_gamma5_matrix(lattice)
    ident = np.eye(g5.shape[0], dtype=np.complex128)
    mode = str(mode)
    if mode == 'left':
        return 0.5 * (ident - g5)
    if mode == 'right':
        return 0.5 * (ident + g5)
    if mode in {'vector', 'both', 'all'}:
        return ident
    if mode == 'axial':
        return g5.copy()
    raise ValueError(f'unknown chirality mode: {mode}')
