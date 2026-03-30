"""Overlap Dirac operator on periodic BCC T³.

Architecture improvement #3: Exact overlap Dirac operator replacing
the plain Wilson operator.

The Neuberger overlap operator:
  D_ov = ρ (I + γ₅ sign(H_W))

where H_W = γ₅(D_W − ρ) is the Hermitian Wilson operator and
sign(H_W) is the matrix sign function.

Key properties:
  - Satisfies the Ginsparg-Wilson relation: {γ₅, D_ov} = (1/ρ) D_ov γ₅ D_ov
  - Exact chiral symmetry on the lattice
  - Index theorem: n₊ − n₋ = Q_top (exact, not approximate)
  - The I-Ī background produces exactly 2 exact zero modes (one from I, one from Ī)

Implementation:
  For small matrices: full eigendecomposition of H_W, replace eigenvalues
  by their signs.
  For production (N > ~5000): Zolotarev rational approximation or
  Chebyshev polynomial (noted but not yet implemented).

This is Phase 3 of the MBP protocol: compute the overlap Dirac spectrum
in the I-Ī background.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt2.dirac_wilson import WilsonDirac
from zsim.lgt2.gauge_field import GaugeField

Array = np.ndarray


@dataclass(frozen=True)
class OverlapSpectrum:
    """Spectrum of the overlap Dirac operator."""
    eigenvalues: Array          # complex eigenvalues of D_ov
    zero_modes: int             # number of exact zero modes (|λ| < threshold)
    n_plus: int                 # positive chirality zero modes
    n_minus: int                # negative chirality zero modes
    topological_charge: int     # Q = n₊ − n₋ (index theorem)
    near_zero_threshold: float  # threshold used for counting
    condition_number: float     # condition number of H_W
    hw_eigenvalues: Array       # eigenvalues of H_W (for diagnostics)


class OverlapDirac:
    """Neuberger overlap Dirac operator.

    D_ov = ρ (I + γ₅ · sign(H_W))

    where H_W = γ₅(D_W − ρ·I) and sign(H_W) is computed via full
    eigendecomposition for research lattice sizes.

    Parameters
    ----------
    gf : GaugeField
        Gauge field configuration.
    rho : float
        Negative mass parameter. Must satisfy 0 < ρ < 2r_W where
        r_W is the Wilson parameter. Typical: ρ = 1.0 for r_W = 1.0,
        ρ = 0.4 for r_W = 0.5.
    wilson_r : float
        Wilson parameter for the kernel operator.
    mass : float
        Bare fermion mass (usually 0 for the overlap).
    kappa : float
        Hopping parameter for the kernel.
    near_zero_threshold : float
        Threshold below which eigenvalues are considered "zero modes".
    """

    def __init__(self, gf: GaugeField, *, rho: float = 1.0,
                 wilson_r: float = 1.0, mass: float = 0.0,
                 kappa: float = 1.0, near_zero_threshold: float = 1e-10):
        self.gf = gf
        self.rho = rho
        self.wilson_r = wilson_r
        self.mass = mass
        self.kappa = kappa
        self.near_zero_threshold = near_zero_threshold

        # Construct kernel
        self._wilson = WilsonDirac(
            gf, mass=mass, wilson_r=wilson_r, kappa=kappa
        )
        self._hw: Array | None = None
        self._sign_hw: Array | None = None
        self._d_ov: Array | None = None

    @property
    def dim(self) -> int:
        return self._wilson.dim

    def hermitian_wilson(self) -> Array:
        """H_W = γ₅(D_W − ρ·I)."""
        if self._hw is None:
            self._hw = self._wilson.hermitian_wilson(rho=self.rho)
        return self._hw

    def sign_hw(self) -> Array:
        """Matrix sign function of H_W via eigendecomposition.

        sign(H_W) = V · diag(sign(λ_i)) · V†

        For H_W Hermitian, eigenvalues are real and V is unitary.
        """
        if self._sign_hw is not None:
            return self._sign_hw

        hw = self.hermitian_wilson()
        eigenvalues, eigenvectors = np.linalg.eigh(hw)

        # sign function: sign(0) = 0 to preserve zero modes
        signs = np.sign(eigenvalues)

        # Reconstruct sign(H_W)
        self._sign_hw = (eigenvectors * signs) @ eigenvectors.conj().T
        return self._sign_hw

    def matrix(self) -> Array:
        """Overlap Dirac operator: D_ov = ρ(I + γ₅ · sign(H_W))."""
        if self._d_ov is not None:
            return self._d_ov

        G5 = self._wilson.gamma5_matrix()
        I_full = np.eye(self.dim, dtype=np.complex128)
        self._d_ov = self.rho * (I_full + G5 @ self.sign_hw())
        return self._d_ov

    def spectrum(self) -> OverlapSpectrum:
        """Compute the full overlap Dirac spectrum.

        Returns eigenvalues, zero mode count, and topological charge
        via the index theorem.
        """
        D = self.matrix()
        eigenvalues = np.linalg.eigvals(D)

        # Sort by magnitude
        order = np.argsort(np.abs(eigenvalues))
        eigenvalues = eigenvalues[order]

        # Count zero modes
        zero_mask = np.abs(eigenvalues) < self.near_zero_threshold
        n_zero = int(np.sum(zero_mask))

        # Chirality of zero modes: for exact zero mode ψ, γ₅ψ = ±ψ
        G5 = self._wilson.gamma5_matrix()
        n_plus, n_minus = 0, 0

        if n_zero > 0:
            # Get zero-mode eigenvectors
            _, evecs = np.linalg.eig(D)
            zero_vecs = evecs[:, order[:n_zero]]
            for k in range(n_zero):
                v = zero_vecs[:, k]
                chirality = float(np.real(v.conj() @ G5 @ v))
                if chirality > 0.5:
                    n_plus += 1
                elif chirality < -0.5:
                    n_minus += 1

        # H_W eigenvalues for diagnostics
        hw_evals = np.linalg.eigvalsh(self.hermitian_wilson())
        cond = float(np.max(np.abs(hw_evals))) / max(float(np.min(np.abs(hw_evals))), 1e-30)

        return OverlapSpectrum(
            eigenvalues=eigenvalues,
            zero_modes=n_zero,
            n_plus=n_plus,
            n_minus=n_minus,
            topological_charge=n_plus - n_minus,
            near_zero_threshold=self.near_zero_threshold,
            condition_number=cond,
            hw_eigenvalues=hw_evals,
        )

    def singular_values(self) -> Array:
        """Singular values of D_ov, sorted ascending."""
        D = self.matrix()
        return np.sort(np.linalg.svd(D, compute_uv=False))

    def verify_ginsparg_wilson(self) -> float:
        """Check Ginsparg-Wilson relation: {γ₅, D_ov} = (1/ρ) D_ov γ₅ D_ov.

        Returns the Frobenius norm of the residual (should be ≈ 0).
        """
        D = self.matrix()
        G5 = self._wilson.gamma5_matrix()
        lhs = G5 @ D + D @ G5
        rhs = (1.0 / self.rho) * D @ G5 @ D
        return float(np.linalg.norm(lhs - rhs))

    def det_ratio(self, gf_ref: GaugeField) -> float:
        """Ratio of overlap determinants: det(D_ov[U]) / det(D_ov[U_ref]).

        Used for the fermion determinant in the MBP bilinear extraction.
        """
        D_current = self.matrix()
        ov_ref = OverlapDirac(
            gf_ref, rho=self.rho, wilson_r=self.wilson_r,
            mass=self.mass, kappa=self.kappa,
        )
        D_ref = ov_ref.matrix()

        # Use log-det for numerical stability
        sign_c, logdet_c = np.linalg.slogdet(D_current)
        sign_r, logdet_r = np.linalg.slogdet(D_ref)
        return float(np.real(sign_c / sign_r * np.exp(logdet_c - logdet_r)))
