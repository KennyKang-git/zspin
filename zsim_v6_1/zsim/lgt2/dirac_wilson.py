"""Wilson-Dirac operator on periodic BCC T³.

The Wilson fermion operator on a general graph:
  D_W = (m + 4r/a) δ_{xy} − (1/2a) Σ_μ [(r−γ_μ)U_μ(x)δ_{x+μ,y}
                                          + (r+γ_μ)U_μ†(y)δ_{x−μ,y}]

On the BCC lattice, "directions" are the 8 center↔corner edges.
We use 4-component spinors (Euclidean 4D γ-matrices) to preserve
chiral structure needed for the overlap construction.

Site Hilbert space: C² (color) ⊗ C⁴ (spinor) = C⁸ per site.
Total dimension: 8 × N_sites.
"""
from __future__ import annotations

import numpy as np

from zsim.lgt2.lattice import PeriodicBCCLattice
from zsim.lgt2.gauge_field import GaugeField

Array = np.ndarray

# Euclidean gamma matrices (chiral basis)
_I2 = np.eye(2, dtype=np.complex128)
_Z2 = np.zeros((2, 2), dtype=np.complex128)
_S1 = np.asarray([[0, 1], [1, 0]], dtype=np.complex128)
_S2 = np.asarray([[0, -1j], [1j, 0]], dtype=np.complex128)
_S3 = np.asarray([[1, 0], [0, -1]], dtype=np.complex128)

GAMMA1 = np.block([[_Z2, -1j * _S1], [1j * _S1, _Z2]])
GAMMA2 = np.block([[_Z2, -1j * _S2], [1j * _S2, _Z2]])
GAMMA3 = np.block([[_Z2, -1j * _S3], [1j * _S3, _Z2]])
GAMMA4 = np.block([[_Z2, _I2], [_I2, _Z2]])
GAMMA5 = np.block([[_I2, _Z2], [_Z2, -_I2]])

GAMMAS_SPATIAL = (GAMMA1, GAMMA2, GAMMA3)
I4 = np.eye(4, dtype=np.complex128)


def directional_gamma(displacement: Array) -> Array:
    """Compute γ · n̂ for a given spatial displacement vector.

    For BCC edges, the displacement is one of the 8 body diagonals:
    (±½, ±½, ±½) × a.  The directional gamma is n̂·γ = Σᵢ nᵢ γᵢ.
    """
    d = np.asarray(displacement, dtype=float)
    norm = float(np.linalg.norm(d))
    if norm < 1e-15:
        return np.zeros((4, 4), dtype=np.complex128)
    n = d / norm
    return sum(float(n[i]) * GAMMAS_SPATIAL[i] for i in range(3))


class WilsonDirac:
    """Wilson-Dirac operator on the periodic BCC lattice.

    D_W[U] = Σ_{edges (x,y)} [−κ (r·I₄ − iγ·n̂_{xy}) ⊗ U_{xy} δ_{xy}
                                −κ (r·I₄ + iγ·n̂_{xy}) ⊗ U†_{xy} δ_{yx}]
             + m·I  (on diagonal)

    where κ = 1/(2ma + 8r) in the standard normalisation, but here we
    keep (m, r, κ) as independent parameters for flexibility.

    Parameters
    ----------
    gf : GaugeField
        Gauge field configuration.
    mass : float
        Bare fermion mass parameter.
    wilson_r : float
        Wilson parameter (r=1 standard, r=0.5 explored in v5.x).
    kappa : float
        Hopping parameter.
    """

    def __init__(self, gf: GaugeField, *, mass: float = 0.0,
                 wilson_r: float = 1.0, kappa: float = 1.0):
        self.gf = gf
        self.mass = mass
        self.wilson_r = wilson_r
        self.kappa = kappa
        self._matrix: Array | None = None

    @property
    def dim(self) -> int:
        """Total Hilbert space dimension: 8 × N_sites."""
        return 8 * self.gf.lattice.num_sites

    def _site_slice(self, site: int) -> slice:
        return slice(8 * site, 8 * (site + 1))

    def matrix(self) -> Array:
        """Construct the full Wilson-Dirac matrix.

        Returns (dim × dim) complex matrix.
        """
        if self._matrix is not None:
            return self._matrix

        N = self.dim
        D = np.zeros((N, N), dtype=np.complex128)
        lattice = self.gf.lattice
        I8 = np.eye(8, dtype=np.complex128)

        # Mass term: m · I on each site
        for site in range(lattice.num_sites):
            sl = self._site_slice(site)
            D[sl, sl] = self.mass * I8

        # Hopping terms
        # For periodic BC: use minimal image convention for displacement
        L = np.array([
            lattice.a * lattice.nx,
            lattice.a * lattice.ny,
            lattice.a * lattice.nz,
        ])
        for i, j in lattice.edges:
            # Minimal image displacement from i to j
            disp = lattice.positions[j] - lattice.positions[i]
            disp = disp - L * np.round(disp / L)
            gamma_dir = directional_gamma(disp)

            U_ij = self.gf.oriented_link(i, j)

            # Forward: site i → site j
            # Standard Wilson convention: (r − γ·n̂) with NO imaginary unit.
            # This ensures γ₅-Hermiticity: γ₅ D_W γ₅ = D_W†, which is
            # the foundational property for the overlap construction.
            spin_fwd = self.wilson_r * I4 - gamma_dir   # (r − γ·n̂)
            hopping_fwd = np.kron(U_ij, spin_fwd)  # color ⊗ spinor

            # Backward: site j → site i
            spin_bwd = self.wilson_r * I4 + gamma_dir   # (r + γ·n̂)
            hopping_bwd = np.kron(U_ij.conj().T, spin_bwd)

            si, sj = self._site_slice(i), self._site_slice(j)
            D[si, sj] += -self.kappa * hopping_fwd
            D[sj, si] += -self.kappa * hopping_bwd

        self._matrix = D
        return D

    def gamma5_matrix(self) -> Array:
        """Block-diagonal γ₅ matrix: I₂ (color) ⊗ γ₅ (spinor) per site."""
        N = self.dim
        G5 = np.zeros((N, N), dtype=np.complex128)
        g5_block = np.kron(_I2, GAMMA5)  # 8×8
        for site in range(self.gf.lattice.num_sites):
            sl = self._site_slice(site)
            G5[sl, sl] = g5_block
        return G5

    def hermitian_wilson(self, *, rho: float = 1.0) -> Array:
        """Hermitian Wilson operator: H_W = γ₅(D_W − ρ).

        This is the kernel for the overlap Dirac operator.
        The parameter ρ ∈ (0, 2r) controls the negative-mass shift.
        """
        D = self.matrix()
        G5 = self.gamma5_matrix()
        return G5 @ (D - rho * np.eye(self.dim, dtype=np.complex128))

    def eigenvalues(self) -> Array:
        """Eigenvalues of D_W (not Hermitian in general)."""
        return np.linalg.eigvals(self.matrix())

    def singular_values(self) -> Array:
        """Singular values of D_W, sorted ascending."""
        return np.sort(np.linalg.svd(self.matrix(), compute_uv=False))

    def chirality_projector(self, mode: str = "vector") -> Array:
        """Chirality projector: P_L = (I−γ₅)/2, P_R = (I+γ₅)/2."""
        G5 = self.gamma5_matrix()
        I_full = np.eye(self.dim, dtype=np.complex128)
        if mode == "left":
            return 0.5 * (I_full - G5)
        elif mode == "right":
            return 0.5 * (I_full + G5)
        elif mode in ("vector", "both"):
            return I_full
        raise ValueError(f"unknown chirality mode: {mode}")
