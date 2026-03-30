"""SU(2) group and Lie algebra operations.

Parameterisation: U = a₀I + i(a₁σ₁ + a₂σ₂ + a₃σ₃), |a|² = 1.
Lie algebra: X = i(x₁σ₁ + x₂σ₂ + x₃σ₃)/2  (traceless anti-Hermitian).
"""
from __future__ import annotations

import numpy as np

Array = np.ndarray

SIGMA1 = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
SIGMA2 = np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
SIGMA3 = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
I2 = np.eye(2, dtype=np.complex128)
SIGMAS = (SIGMA1, SIGMA2, SIGMA3)


def random_su2(*, rng: np.random.Generator | None = None) -> Array:
    """Haar-uniform random SU(2) element via quaternion sampling."""
    gen = rng or np.random.default_rng()
    q = gen.normal(size=4)
    q /= np.linalg.norm(q)
    a, b, c, d = q
    return np.asarray(
        [[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]],
        dtype=np.complex128,
    )


def project_su2(M: Array) -> Array:
    """Project 2×2 matrix to SU(2) via polar decomposition."""
    u, s, vh = np.linalg.svd(M)
    W = u @ vh
    return (W / np.sqrt(np.linalg.det(W))).astype(np.complex128)


def su2_exp(X: Array) -> Array:
    """Exponential map: traceless anti-Hermitian 2×2 → SU(2).

    X must be traceless anti-Hermitian: X = iθ(n̂·σ)/2.
    exp(X) = cos(θ/2)I + sin(θ/2)(n̂·σ) where θ = 2|Im eigenvalue|.
    """
    # Extract θ from eigenvalues of X
    eigvals = np.linalg.eigvalsh(1j * X)  # Hermitian → real eigenvalues
    theta = float(np.max(np.abs(eigvals)))
    if theta < 1e-15:
        return I2.copy()
    return np.cos(theta) * I2 + (np.sin(theta) / theta) * X


def su2_log(U: Array) -> Array:
    """Logarithm: SU(2) → traceless anti-Hermitian 2×2.

    Returns X such that exp(X) = U, with X traceless anti-Hermitian.
    """
    tr = float(np.real(np.trace(U)))
    cos_theta = np.clip(tr / 2.0, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    if abs(theta) < 1e-14:
        return np.zeros((2, 2), dtype=np.complex128)
    return (theta / np.sin(theta)) * (U - cos_theta * I2)


def traceless_antihermitian(M: Array) -> Array:
    """Project to traceless anti-Hermitian part: (M - M†)/2 - Tr(M - M†)/(2N) I."""
    ah = 0.5 * (M - M.conj().T)
    return ah - (np.trace(ah) / 2.0) * I2


def plaquette_force(U: Array, staple_sum: Array) -> Array:
    """Compute the traceless anti-Hermitian force from link U and its staple sum.

    F = TA[U · Σ†]  where TA = traceless anti-Hermitian projection.
    This is proportional to ∂S_W/∂U.
    """
    Z = U @ staple_sum.conj().T
    return traceless_antihermitian(Z)


def su2_distance(U: Array, V: Array) -> float:
    """Geodesic distance on SU(2) ≅ S³: d(U,V) = arccos(|Tr(U†V)|/2)."""
    tr = float(np.abs(np.trace(U.conj().T @ V))) / 2.0
    return float(np.arccos(np.clip(tr, -1.0, 1.0)))
