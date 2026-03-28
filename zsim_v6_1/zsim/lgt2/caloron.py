"""Caloron constituent / BPS monopole backgrounds on periodic BCC T³.

Architecture improvement #5: Physics-motivated instanton backgrounds
replacing random configurations.

For the 3D BCC lattice, the relevant classical solutions are:
  - BPS monopole: the 3D magnetic monopole in SU(2)
  - Instanton-anti-instanton (I-Ī) molecular configuration

The BPS monopole in the hedgehog gauge:
  A_i^a(x) = ε_{aij} x̂_j f(r) / r

where f(r) = 1 − vr/sinh(vr) for a monopole with Higgs VEV v.
At large r, A ~ monopole; at r=0, regular.

For the I-Ī molecular background, we superpose two BPS profiles
centred at x₁ and x₂ with opposite charges. The separation R = |x₁−x₂|
controls the "molecular" nature. The valley parameter ζ interpolates
between isolated instantons (ζ→∞) and the vacuum (ζ→0).

The continuum gauge field is discretised onto BCC links by path-ordered
exponentials along edges:
  U_{xy} = P exp(−ig ∫_x^y A_μ dx^μ) ≈ exp(−ig A_μ(x̄) Δx^μ)
where x̄ = (x+y)/2 is the edge midpoint.

This is Phase 2 of the MBP protocol: generate the caloron constituent
background for subsequent Dirac spectrum computation.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt2.lattice import PeriodicBCCLattice
from zsim.lgt2.gauge_field import GaugeField
from zsim.lgt2.su2 import I2, SIGMAS, su2_exp, project_su2

Array = np.ndarray


@dataclass(frozen=True)
class CaloronParams:
    """Parameters for the I-Ī molecular caloron background."""
    center1: tuple[float, float, float]  # instanton center
    center2: tuple[float, float, float]  # anti-instanton center
    rho_inst: float = 0.5                # instanton size parameter
    coupling_g: float = 1.0              # gauge coupling for discretisation
    topological_charge_target: int = 0   # ν=0 for I-Ī


def _levi_civita_3(a: int, i: int, j: int) -> float:
    """3D Levi-Civita symbol ε_{aij}."""
    perm = (a, i, j)
    if perm in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
        return 1.0
    if perm in ((2, 1, 0), (1, 0, 2), (0, 2, 1)):
        return -1.0
    return 0.0


def _bps_profile(r: float, rho: float) -> float:
    """BPS monopole profile function: f(r) = 1 − r/(ρ·sinh(r/ρ)).

    At r=0: f→0 (regular core).
    At r→∞: f→1 (Coulomb tail).
    """
    if r < 1e-15:
        return 0.0
    x = r / max(rho, 1e-15)
    if x > 500:
        return 1.0
    return 1.0 - x / np.sinh(x)


def _bps_gauge_field(x: Array, center: Array, rho: float, charge: int = 1) -> Array:
    """Compute the BPS monopole gauge field A_i at point x.

    A_i = (charge/2) ε_{aij} x̂_j f(r) σ_a / r

    Returns a 3-vector of 2×2 su(2) matrices: [A_1, A_2, A_3].
    """
    dx = x - center
    r = float(np.linalg.norm(dx))

    if r < 1e-15:
        return [np.zeros((2, 2), dtype=np.complex128) for _ in range(3)]

    x_hat = dx / r
    f = _bps_profile(r, rho)
    A = []

    for i in range(3):
        Ai = np.zeros((2, 2), dtype=np.complex128)
        for a in range(3):
            coeff = 0.0
            for j in range(3):
                coeff += _levi_civita_3(a, i, j) * x_hat[j]
            Ai += charge * 0.5 * f * coeff * SIGMAS[a] / r
        A.append(Ai)
    return A


def _molecular_gauge_field(x: Array, params: CaloronParams) -> list[Array]:
    """I-Ī molecular gauge field: superposition of instanton + anti-instanton.

    A_i^{I-Ī}(x) = A_i^I(x; x₁, +1) + A_i^Ī(x; x₂, −1)

    The superposition is valid in the dilute instanton gas approximation
    when |x₁ − x₂| >> ρ.
    """
    c1 = np.asarray(params.center1, dtype=float)
    c2 = np.asarray(params.center2, dtype=float)
    A_I = _bps_gauge_field(x, c1, params.rho_inst, charge=+1)
    A_Ibar = _bps_gauge_field(x, c2, params.rho_inst, charge=-1)
    return [A_I[i] + A_Ibar[i] for i in range(3)]


def _discretise_link(
    lattice: PeriodicBCCLattice,
    gauge_field_func,
    i: int, j: int,
    coupling_g: float,
) -> Array:
    """Discretise continuum gauge field onto a lattice link.

    U_{ij} ≈ exp(−ig A_μ(x̄) Δx^μ)

    where x̄ = midpoint, Δx = x_j − x_i.
    For periodic BC, we use the minimal image convention for the
    displacement vector.
    """
    xi = lattice.positions[i]
    xj = lattice.positions[j]

    # Minimal image displacement for periodic BC
    dx = xj - xi
    L = np.array([lattice.a * lattice.nx,
                   lattice.a * lattice.ny,
                   lattice.a * lattice.nz])
    dx = dx - L * np.round(dx / L)  # minimal image

    midpoint = xi + 0.5 * dx
    A_mid = gauge_field_func(midpoint)

    # Lie algebra element: −ig Σ_μ A_μ Δx^μ
    exponent = np.zeros((2, 2), dtype=np.complex128)
    for mu in range(3):
        exponent += -1j * coupling_g * A_mid[mu] * dx[mu]

    return project_su2(su2_exp(exponent))


class CaloronBackground:
    """Generator for I-Ī molecular caloron backgrounds on periodic BCC.

    Implements the MBP protocol Phase 2: create a gauge field in the
    caloron constituent sector (net ν=0).

    Usage:
        params = CaloronParams(center1=..., center2=..., rho_inst=0.5)
        cal = CaloronBackground(lattice, params)
        gf = cal.generate()
    """

    def __init__(self, lattice: PeriodicBCCLattice, params: CaloronParams):
        self.lattice = lattice
        self.params = params

    def generate(self, *, beta: float = 2.3) -> GaugeField:
        """Generate the discretised I-Ī gauge field configuration."""
        def gauge_func(x):
            return _molecular_gauge_field(x, self.params)

        links = {}
        for (i, j) in self.lattice.edges:
            links[(i, j)] = _discretise_link(
                self.lattice, gauge_func, i, j,
                self.params.coupling_g,
            )
        return GaugeField(lattice=self.lattice, links=links, beta=beta)

    def classical_action(self) -> float:
        """Analytical classical action of the I-Ī molecular configuration.

        For widely separated I-Ī pair:
          S_{I-Ī} ≈ 2 × S_cl = 2 × (8π²/g²)

        In Z-Spin: S_cl = 35π/3 (from I_h/T_d coset, DERIVED).
        """
        return 2.0 * 35.0 * np.pi / 3.0

    @classmethod
    def symmetric_pair(cls, lattice: PeriodicBCCLattice, *,
                       separation_fraction: float = 0.4,
                       rho_inst: float = 0.5,
                       coupling_g: float = 1.0) -> "CaloronBackground":
        """Create a symmetric I-Ī pair centred on the lattice.

        The instanton and anti-instanton are placed symmetrically
        along the x-axis at ±(separation/2) from the lattice centre.

        Parameters
        ----------
        separation_fraction : float
            Fraction of Lx for the I-Ī separation (0 < frac < 1).
        """
        Lx = lattice.a * lattice.nx
        Ly = lattice.a * lattice.ny
        Lz = lattice.a * lattice.nz

        cx, cy, cz = Lx / 2, Ly / 2, Lz / 2
        dx = separation_fraction * Lx / 2

        params = CaloronParams(
            center1=(cx - dx, cy, cz),
            center2=(cx + dx, cy, cz),
            rho_inst=rho_inst,
            coupling_g=coupling_g,
        )
        return cls(lattice, params)

    @classmethod
    def single_monopole(cls, lattice: PeriodicBCCLattice, *,
                        rho_inst: float = 0.5,
                        coupling_g: float = 1.0) -> "CaloronBackground":
        """Single BPS monopole at the lattice centre (Q=1).

        Useful for validation: the overlap Dirac operator should
        produce exactly 1 zero mode.
        """
        Lx = lattice.a * lattice.nx
        Ly = lattice.a * lattice.ny
        Lz = lattice.a * lattice.nz
        cx, cy, cz = Lx / 2, Ly / 2, Lz / 2

        # Place a single monopole (instanton) at centre,
        # anti-instanton very far away (effectively absent)
        params = CaloronParams(
            center1=(cx, cy, cz),
            center2=(cx + 100 * Lx, cy, cz),  # effectively absent
            rho_inst=rho_inst,
            coupling_g=coupling_g,
        )
        return cls(lattice, params)
