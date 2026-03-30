"""Gauge field configuration and Wilson plaquette action on periodic BCC T³.

The Wilson action on the BCC lattice:
  S_W[U] = β Σ_P (1 - ½ Re Tr(U_P))
where β = 4/g₀² and U_P is the ordered product of link variables around
plaquette P.  On BCC, plaquettes are rhombic 4-cycles C₁-V₁-C₂-V₂.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt2.lattice import PeriodicBCCLattice, Loop
from zsim.lgt2.su2 import (
    I2, random_su2, project_su2, traceless_antihermitian
)

Array = np.ndarray


@dataclass
class GaugeField:
    """SU(2) gauge field configuration on a periodic BCC lattice.

    Attributes
    ----------
    lattice : PeriodicBCCLattice
        The underlying lattice.
    links : dict[tuple[int,int], Array]
        Maps each oriented edge (i,j) with i<j to a 2×2 SU(2) matrix.
        For transport j→i, use U†.
    beta : float
        Bare coupling β = 4/g₀².  Sets the lattice spacing implicitly.
    """

    lattice: PeriodicBCCLattice
    links: dict[tuple[int, int], Array]
    beta: float = 2.3  # typical SU(2) coupling

    @classmethod
    def identity(cls, lattice: PeriodicBCCLattice, beta: float = 2.3) -> "GaugeField":
        """Trivial vacuum configuration U=I on all links."""
        links = {e: I2.copy() for e in lattice.edges}
        return cls(lattice=lattice, links=links, beta=beta)

    @classmethod
    def random(cls, lattice: PeriodicBCCLattice, beta: float = 2.3,
               *, seed: int = 350437) -> "GaugeField":
        """Hot-start: Haar-random SU(2) on every link."""
        rng = np.random.default_rng(seed)
        links = {e: random_su2(rng=rng) for e in lattice.edges}
        return cls(lattice=lattice, links=links, beta=beta)

    @classmethod
    def cold_perturbed(cls, lattice: PeriodicBCCLattice, beta: float = 2.3,
                       *, epsilon: float = 0.1, seed: int = 350437) -> "GaugeField":
        """Near-vacuum configuration: U = exp(ε·X) with small random X."""
        rng = np.random.default_rng(seed)
        links = {}
        for e in lattice.edges:
            X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
            X = traceless_antihermitian(X)
            X *= epsilon / max(np.linalg.norm(X), 1e-15)
            from zsim.lgt2.su2 import su2_exp
            links[e] = su2_exp(X)
        return cls(lattice=lattice, links=links, beta=beta)

    def copy(self) -> "GaugeField":
        """Deep copy of the gauge field."""
        return GaugeField(
            lattice=self.lattice,
            links={e: U.copy() for e, U in self.links.items()},
            beta=self.beta,
        )

    def oriented_link(self, i: int, j: int) -> Array:
        """Return U_{i→j}, using hermitian conjugate if stored as (j,i)."""
        key = (min(i, j), max(i, j))
        U = self.links[key]
        return U if i < j else U.conj().T


def loop_holonomy(gf: GaugeField, loop: Loop) -> Array:
    """Compute the ordered product of links around a loop."""
    acc = I2.copy()
    n = len(loop)
    for idx in range(n):
        acc = acc @ gf.oriented_link(loop[idx], loop[(idx + 1) % n])
    return acc


def plaquette_trace(gf: GaugeField, loop: Loop) -> float:
    """½ Re Tr(U_P) for a single plaquette."""
    return float(np.real(np.trace(loop_holonomy(gf, loop)))) / 2.0


def wilson_action(gf: GaugeField) -> float:
    """Wilson plaquette action: S_W = β Σ_P (1 - ½ Re Tr(U_P))."""
    total = 0.0
    for p in gf.lattice.plaquettes:
        total += 1.0 - plaquette_trace(gf, p)
    return gf.beta * total


def avg_plaquette(gf: GaugeField) -> float:
    """<½ Re Tr(U_P)> averaged over all plaquettes."""
    if not gf.lattice.plaquettes:
        return 1.0
    return float(np.mean([plaquette_trace(gf, p) for p in gf.lattice.plaquettes]))


def staple_sum(gf: GaugeField, edge: tuple[int, int]) -> Array:
    """Sum of staples around a given edge.

    For edge (u,v), the staple through plaquette P = (u, v, ...) is
    the ordered product of the other 3 links in P, oriented to close
    the loop ending at u.
    """
    u, v = edge
    total = np.zeros((2, 2), dtype=np.complex128)
    count = 0
    for loop in gf.lattice.plaquettes:
        n = len(loop)
        for idx in range(n):
            a, b = loop[idx], loop[(idx + 1) % n]
            if (a == u and b == v) or (a == v and b == u):
                # Build the staple: the rest of the loop
                if a == u and b == v:
                    acc = I2.copy()
                    cursor = v
                    for step in range(1, n):
                        nxt = loop[(idx + 1 + step) % n]
                        acc = acc @ gf.oriented_link(cursor, nxt)
                        cursor = nxt
                    total += acc
                else:  # a == v, b == u → reverse orientation
                    acc = I2.copy()
                    cursor = u
                    for step in range(1, n):
                        nxt = loop[(idx + 1 + step) % n]
                        acc = acc @ gf.oriented_link(cursor, nxt)
                        cursor = nxt
                    total += acc.conj().T
                count += 1
                break
    return total


def all_staple_sums(gf: GaugeField) -> dict[tuple[int, int], Array]:
    """Compute staple sums for all edges."""
    return {edge: staple_sum(gf, edge) for edge in gf.lattice.edges}


def topological_charge_clover(gf: GaugeField) -> float:
    """Lattice topological charge via clover (plaquette-based) estimator.

    For SU(2) in 3D, this is the Chern-Simons-like winding number.
    Q = (1/8π²) Σ_P Tr(F_P) where F_P = Im(U_P).
    On the BCC lattice this is a rough estimator; gradient flow
    improves it dramatically.
    """
    total = 0.0
    for p in gf.lattice.plaquettes:
        hol = loop_holonomy(gf, p)
        # F ≈ (U_P - U_P†)/(2i) = Im(U_P)
        F = (hol - hol.conj().T) / 2j
        total += float(np.real(np.trace(F)))
    return total / (8.0 * np.pi**2)
