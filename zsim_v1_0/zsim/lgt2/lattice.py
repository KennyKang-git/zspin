"""Periodic BCC lattice on T³.

Architecture improvement #1: Periodic boundary conditions replace open boundary.

A BCC unit cell has 2 sites: corner at (i,j,k) and center at (i+½,j+½,k+½).
With periodic BC on Nx×Ny×Nz cells:
  - Corner sites: Nx·Ny·Nz (indices wrap modulo N)
  - Center sites: Nx·Ny·Nz
  - Total: 2·Nx·Ny·Nz
  - Edges per cell: 8 (center ↔ 8 corner neighbours)
  - Total edges: 8·Nx·Ny·Nz (every edge counted once)

Plaquettes are 4-cycles: C₁-V₁-C₂-V₂ (two centers sharing two corner
neighbours in adjacent cells, wrapping at boundaries).

The lattice spacing *a* is an explicit parameter (improvement #4).
Physical distances scale with a; the continuum limit is a → 0.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import numpy as np

Array = np.ndarray
Loop = tuple[int, ...]


@dataclass(frozen=True)
class PeriodicBCCLattice:
    """BCC lattice on T³ with periodic boundary conditions."""

    nx: int
    ny: int
    nz: int
    a: float  # lattice spacing in physical units

    positions: Array  # (num_sites, 3) coordinates
    site_types: tuple[str, ...]  # 'corner' or 'center'
    edges: tuple[tuple[int, int], ...]  # sorted (i < j) unique edges
    plaquettes: tuple[Loop, ...]  # 4-site rhombic plaquettes

    # Indexing maps
    corner_index: dict[tuple[int, int, int], int] = field(repr=False)
    center_index: dict[tuple[int, int, int], int] = field(repr=False)

    @property
    def num_sites(self) -> int:
        return 2 * self.nx * self.ny * self.nz

    @property
    def num_edges(self) -> int:
        return len(self.edges)

    @property
    def num_plaquettes(self) -> int:
        return len(self.plaquettes)

    @property
    def shape(self) -> tuple[int, int, int]:
        return (self.nx, self.ny, self.nz)

    @property
    def volume_cells(self) -> int:
        return self.nx * self.ny * self.nz

    @property
    def physical_volume(self) -> float:
        """Physical volume = (a·Nx)(a·Ny)(a·Nz)."""
        return (self.a ** 3) * self.volume_cells

    def adjacency_matrix(self) -> Array:
        n = self.num_sites
        adj = np.zeros((n, n), dtype=float)
        for i, j in self.edges:
            adj[i, j] = 1.0
            adj[j, i] = 1.0
        return adj


def build_periodic_bcc(
    nx: int = 4, ny: int = 4, nz: int = 4, *, a: float = 1.0
) -> PeriodicBCCLattice:
    """Construct a BCC lattice on T³ with periodic boundary conditions.

    Parameters
    ----------
    nx, ny, nz : int
        Number of unit cells in each direction. Minimum 2 for PBC.
    a : float
        Lattice spacing in physical units.

    Returns
    -------
    PeriodicBCCLattice
        Fully constructed lattice with edges and plaquettes.
    """
    if nx < 2 or ny < 2 or nz < 2:
        raise ValueError(f"PBC requires shape >= (2,2,2), got ({nx},{ny},{nz})")

    # ---- Sites ----
    positions: list[tuple[float, float, float]] = []
    site_types: list[str] = []
    corner_index: dict[tuple[int, int, int], int] = {}
    center_index: dict[tuple[int, int, int], int] = {}

    # Corners: one per cell (periodic → no extra boundary layer)
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                corner_index[(i, j, k)] = len(positions)
                positions.append((a * i, a * j, a * k))
                site_types.append("corner")

    # Centers: one per cell
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                center_index[(i, j, k)] = len(positions)
                positions.append((a * (i + 0.5), a * (j + 0.5), a * (k + 0.5)))
                site_types.append("center")

    # ---- Edges (center ↔ 8 corner neighbours, with PBC wrapping) ----
    edges_set: set[tuple[int, int]] = set()
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                c = center_index[(i, j, k)]
                for di in (0, 1):
                    for dj in (0, 1):
                        for dk in (0, 1):
                            ci = (i + di) % nx
                            cj = (j + dj) % ny
                            ck = (k + dk) % nz
                            v = corner_index[(ci, cj, ck)]
                            edge = (min(c, v), max(c, v))
                            edges_set.add(edge)

    edges = tuple(sorted(edges_set))

    # ---- Rhombic plaquettes with PBC wrapping ----
    plaquettes = _enumerate_periodic_plaquettes(
        nx, ny, nz, corner_index, center_index
    )

    return PeriodicBCCLattice(
        nx=nx, ny=ny, nz=nz, a=a,
        positions=np.asarray(positions, dtype=float),
        site_types=tuple(site_types),
        edges=edges,
        plaquettes=plaquettes,
        corner_index=corner_index,
        center_index=center_index,
    )


def _enumerate_periodic_plaquettes(
    nx: int, ny: int, nz: int,
    corner_index: dict[tuple[int, int, int], int],
    center_index: dict[tuple[int, int, int], int],
) -> tuple[Loop, ...]:
    """Enumerate all rhombic 4-plaquettes on the periodic BCC lattice.

    A plaquette is a 4-cycle: center₁ → corner₁ → center₂ → corner₂.
    Two adjacent centers (differing by 1 cell in one direction) share
    4 pairs of common corner neighbours; each pair defines a plaquette.
    With PBC, adjacency wraps around boundaries.
    """
    loops: list[Loop] = []

    # x-direction plaquettes
    for i in range(nx):
        i2 = (i + 1) % nx
        for j in range(ny):
            for k in range(nz):
                left = center_index[(i, j, k)]
                right = center_index[(i2, j, k)]
                for dj in (0, 1):
                    for dk in (0, 1):
                        c1 = corner_index[((i + 1) % nx, (j + dj) % ny, (k + dk) % nz)]
                        c2 = corner_index[((i + 1) % nx, (j + 1 - dj) % ny, (k + 1 - dk) % nz)]
                        loops.append((left, c1, right, c2))

    # y-direction plaquettes
    for i in range(nx):
        for j in range(ny):
            j2 = (j + 1) % ny
            for k in range(nz):
                left = center_index[(i, j, k)]
                right = center_index[(i, j2, k)]
                for di in (0, 1):
                    for dk in (0, 1):
                        c1 = corner_index[((i + di) % nx, (j + 1) % ny, (k + dk) % nz)]
                        c2 = corner_index[((i + 1 - di) % nx, (j + 1) % ny, (k + 1 - dk) % nz)]
                        loops.append((left, c1, right, c2))

    # z-direction plaquettes
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                k2 = (k + 1) % nz
                left = center_index[(i, j, k)]
                right = center_index[(i, j, k2)]
                for di in (0, 1):
                    for dj in (0, 1):
                        c1 = corner_index[((i + di) % nx, (j + dj) % ny, (k + 1) % nz)]
                        c2 = corner_index[((i + 1 - di) % nx, (j + 1 - dj) % ny, (k + 1) % nz)]
                        loops.append((left, c1, right, c2))

    return tuple(loops)


def plaquette_incidence(lattice: PeriodicBCCLattice) -> dict[tuple[int, int], tuple[int, ...]]:
    """Map each edge to the indices of plaquettes containing it."""
    from collections import defaultdict
    inc: dict[tuple[int, int], list[int]] = defaultdict(list)
    for p_idx, loop in enumerate(lattice.plaquettes):
        n = len(loop)
        for i in range(n):
            a, b = loop[i], loop[(i + 1) % n]
            key = (min(a, b), max(a, b))
            inc[key].append(p_idx)
    return {k: tuple(v) for k, v in inc.items()}
