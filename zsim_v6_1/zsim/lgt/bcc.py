from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class BCCLattice:
    positions: Array
    edges: tuple[tuple[int, int], ...]
    site_types: tuple[str, ...]
    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def num_sites(self) -> int:
        return int(self.positions.shape[0])

    @property
    def num_edges(self) -> int:
        return len(self.edges)

    def adjacency_matrix(self) -> Array:
        adj = np.zeros((self.num_sites, self.num_sites), dtype=float)
        for i, j in self.edges:
            adj[i, j] = 1.0
            adj[j, i] = 1.0
        return adj


def build_bcc_supercell(nx: int = 1, ny: int = 1, nz: int = 1) -> BCCLattice:
    positions: list[tuple[float, float, float]] = []
    site_types: list[str] = []
    corner_index: dict[tuple[int, int, int], int] = {}
    center_index: dict[tuple[int, int, int], int] = {}
    for i in range(nx + 1):
        for j in range(ny + 1):
            for k in range(nz + 1):
                corner_index[(i, j, k)] = len(positions)
                positions.append((float(i), float(j), float(k)))
                site_types.append('corner')
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                center_index[(i, j, k)] = len(positions)
                positions.append((i + 0.5, j + 0.5, k + 0.5))
                site_types.append('center')
    edges: set[tuple[int, int]] = set()
    for i in range(nx):
        for j in range(ny):
            for k in range(nz):
                c = center_index[(i, j, k)]
                for di in (0, 1):
                    for dj in (0, 1):
                        for dk in (0, 1):
                            v = corner_index[(i + di, j + dj, k + dk)]
                            edges.add((c, v) if c < v else (v, c))
    metadata = {
        'shape': (nx, ny, nz),
        'description': 'open BCC supercell scaffold',
        'corner_index': corner_index,
        'center_index': center_index,
    }
    return BCCLattice(np.asarray(positions, dtype=float), tuple(sorted(edges)), tuple(site_types), metadata)
