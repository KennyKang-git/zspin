from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt.bcc import BCCLattice
from zsim.lgt.fermion import wilson_spinor_operator
from zsim.lgt.pairing import NearZeroPairingSummary, analyze_near_zero_pairs_from_singular_values
from zsim.lgt.spinor import wilson_gamma5_matrix

Array = np.ndarray


@dataclass(frozen=True)
class OverlapModeSummary:
    rho: float
    m0: float
    sign_epsilon: float
    pairing: NearZeroPairingSummary
    chiral_abs_mean: float
    chiral_signed_sum: float
    gw_residual: float
    hermitian_kernel_min: float
    hermitian_kernel_next: float
    score: float

    def to_dict(self) -> dict[str, float | dict[str, object]]:
        return {
            'rho': self.rho,
            'm0': self.m0,
            'sign_epsilon': self.sign_epsilon,
            'pairing': self.pairing.to_dict(),
            'chiral_abs_mean': self.chiral_abs_mean,
            'chiral_signed_sum': self.chiral_signed_sum,
            'gw_residual': self.gw_residual,
            'hermitian_kernel_min': self.hermitian_kernel_min,
            'hermitian_kernel_next': self.hermitian_kernel_next,
            'score': self.score,
        }


def hermitian_wilson_kernel(
    lattice: BCCLattice,
    links: dict[tuple[int, int], Array],
    *,
    mass: float = 0.15,
    kappa: float = 0.6,
    r: float = 1.0,
    m0: float = 1.20,
) -> Array:
    d_w = wilson_spinor_operator(lattice, links, mass=mass, kappa=kappa, r=r)
    g5 = wilson_gamma5_matrix(lattice)
    return g5 @ (d_w - float(m0) * np.eye(d_w.shape[0], dtype=np.complex128))


def smooth_matrix_sign_hermitian(hmat: Array, *, sign_epsilon: float = 1e-5) -> Array:
    evals, evecs = np.linalg.eigh(hmat)
    smooth = evals / np.sqrt(evals * evals + float(sign_epsilon) ** 2)
    return (evecs * smooth) @ evecs.conj().T


def overlap_dirac_operator(
    lattice: BCCLattice,
    links: dict[tuple[int, int], Array],
    *,
    mass: float = 0.15,
    kappa: float = 0.6,
    r: float = 1.0,
    m0: float = 1.20,
    rho: float = 1.0,
    sign_epsilon: float = 1e-5,
) -> tuple[Array, Array]:
    g5 = wilson_gamma5_matrix(lattice)
    hmat = hermitian_wilson_kernel(lattice, links, mass=mass, kappa=kappa, r=r, m0=m0)
    sign_h = smooth_matrix_sign_hermitian(hmat, sign_epsilon=sign_epsilon)
    d_ov = float(rho) * (np.eye(hmat.shape[0], dtype=np.complex128) + g5 @ sign_h)
    return d_ov, hmat


def evaluate_overlap_background(
    lattice: BCCLattice,
    links: dict[tuple[int, int], Array],
    *,
    mass: float = 0.15,
    kappa: float = 0.6,
    r: float = 1.0,
    m0: float = 1.20,
    rho: float = 1.0,
    sign_epsilon: float = 1e-5,
    pair_count: int = 2,
    sample_size: int = 8,
) -> OverlapModeSummary:
    d_ov, hmat = overlap_dirac_operator(
        lattice,
        links,
        mass=mass,
        kappa=kappa,
        r=r,
        m0=m0,
        rho=rho,
        sign_epsilon=sign_epsilon,
    )
    g5 = wilson_gamma5_matrix(lattice)
    singular = np.linalg.svd(d_ov, compute_uv=False)
    pairing = analyze_near_zero_pairs_from_singular_values(singular, pair_count=pair_count, sample_size=sample_size)
    herm = d_ov.conj().T @ d_ov
    evals, evecs = np.linalg.eigh(herm)
    idx = np.argsort(np.real_if_close(evals))[: max(2 * pair_count, 2)]
    chiralities = []
    for col in idx:
        vec = evecs[:, col]
        num = np.vdot(vec, g5 @ vec)
        den = np.vdot(vec, vec)
        chiralities.append(float(np.real_if_close(num / den)))
    abs_mean = float(np.mean(np.abs(chiralities))) if chiralities else 0.0
    signed_sum = float(np.sum(chiralities)) if chiralities else 0.0
    lhs = d_ov @ g5 + g5 @ d_ov
    rhs = (1.0 / max(float(rho), 1e-12)) * (d_ov @ g5 @ d_ov)
    gw_residual = float(np.linalg.norm(lhs - rhs) / (np.linalg.norm(lhs) + 1e-12))
    h_eigs = np.sort(np.abs(np.linalg.eigvalsh(hmat)))
    hk_min = float(h_eigs[0]) if h_eigs.size else 0.0
    hk_next = float(h_eigs[1]) if h_eigs.size > 1 else hk_min
    score = float(pairing.score * (1.0 + abs_mean) / (1.0 + gw_residual))
    return OverlapModeSummary(
        rho=float(rho),
        m0=float(m0),
        sign_epsilon=float(sign_epsilon),
        pairing=pairing,
        chiral_abs_mean=abs_mean,
        chiral_signed_sum=signed_sum,
        gw_residual=gw_residual,
        hermitian_kernel_min=hk_min,
        hermitian_kernel_next=hk_next,
        score=score,
    )



def _smooth_sign_values(evals: Array, sign_epsilon: float, method: str = 'smooth') -> Array:
    x = np.asarray(evals, dtype=float)
    eps = float(max(sign_epsilon, 1.0e-12))
    if method == 'smooth':
        vals = x / np.sqrt(x * x + eps * eps)
    elif method == 'tanh':
        vals = np.tanh(x / eps)
    elif method == 'rational':
        vals = x * (x * x + 3.0 * eps * eps) / (np.power(x * x + eps * eps, 1.5) + 1.0e-18)
    elif method == 'arctan':
        vals = (2.0 / np.pi) * np.arctan(x / eps)
    elif method == 'pade11':
        y = x / eps
        vals = y / (1.0 + np.abs(y))
    else:
        raise ValueError(f'unknown sign-method: {method}')
    return np.clip(vals, -1.0, 1.0)


def matrix_sign_hermitian_method(hmat: Array, *, sign_epsilon: float = 1.0e-5, method: str = 'smooth') -> Array:
    evals, evecs = np.linalg.eigh(hmat)
    signed = _smooth_sign_values(np.real_if_close(evals), sign_epsilon=sign_epsilon, method=method)
    return (evecs * signed) @ evecs.conj().T


def overlap_dirac_operator_with_method(
    lattice: BCCLattice,
    links: dict[tuple[int, int], Array],
    *,
    mass: float = 0.15,
    kappa: float = 0.6,
    r: float = 1.0,
    m0: float = 1.20,
    rho: float = 1.0,
    sign_epsilon: float = 1.0e-5,
    sign_method: str = 'smooth',
) -> tuple[Array, Array]:
    g5 = wilson_gamma5_matrix(lattice)
    hmat = hermitian_wilson_kernel(lattice, links, mass=mass, kappa=kappa, r=r, m0=m0)
    sign_h = matrix_sign_hermitian_method(hmat, sign_epsilon=sign_epsilon, method=sign_method)
    d_ov = float(rho) * (np.eye(hmat.shape[0], dtype=np.complex128) + g5 @ sign_h)
    return d_ov, hmat


def evaluate_overlap_background_with_method(
    lattice: BCCLattice,
    links: dict[tuple[int, int], Array],
    *,
    mass: float = 0.15,
    kappa: float = 0.6,
    r: float = 1.0,
    m0: float = 1.20,
    rho: float = 1.0,
    sign_epsilon: float = 1.0e-5,
    pair_count: int = 2,
    sample_size: int = 8,
    sign_method: str = 'smooth',
) -> OverlapModeSummary:
    d_ov, hmat = overlap_dirac_operator_with_method(
        lattice,
        links,
        mass=mass,
        kappa=kappa,
        r=r,
        m0=m0,
        rho=rho,
        sign_epsilon=sign_epsilon,
        sign_method=sign_method,
    )
    g5 = wilson_gamma5_matrix(lattice)
    singular = np.linalg.svd(d_ov, compute_uv=False)
    pairing = analyze_near_zero_pairs_from_singular_values(singular, pair_count=pair_count, sample_size=sample_size)
    herm = d_ov.conj().T @ d_ov
    evals, evecs = np.linalg.eigh(herm)
    idx = np.argsort(np.real_if_close(evals))[: max(2 * pair_count, 2)]
    chiralities = []
    for col in idx:
        vec = evecs[:, col]
        num = np.vdot(vec, g5 @ vec)
        den = np.vdot(vec, vec)
        chiralities.append(float(np.real_if_close(num / den)))
    abs_mean = float(np.mean(np.abs(chiralities))) if chiralities else 0.0
    signed_sum = float(np.sum(chiralities)) if chiralities else 0.0
    lhs = d_ov @ g5 + g5 @ d_ov
    rhs = (1.0 / max(float(rho), 1.0e-12)) * (d_ov @ g5 @ d_ov)
    gw_residual = float(np.linalg.norm(lhs - rhs) / (np.linalg.norm(lhs) + 1.0e-12))
    h_eigs = np.sort(np.abs(np.linalg.eigvalsh(hmat)))
    hk_min = float(h_eigs[0]) if h_eigs.size else 0.0
    hk_next = float(h_eigs[1]) if h_eigs.size > 1 else hk_min
    score = float(pairing.score * (1.0 + abs_mean) / (1.0 + gw_residual))
    return OverlapModeSummary(
        rho=float(rho),
        m0=float(m0),
        sign_epsilon=float(sign_epsilon),
        pairing=pairing,
        chiral_abs_mean=abs_mean,
        chiral_signed_sum=signed_sum,
        gw_residual=gw_residual,
        hermitian_kernel_min=hk_min,
        hermitian_kernel_next=hk_next,
        score=score,
    )
