from __future__ import annotations

from collections import defaultdict

from zsim.lgt.bcc import BCCLattice

Loop = tuple[int, ...]


def enumerate_bcc_rhombic_plaquettes(lattice: BCCLattice) -> tuple[Loop, ...]:
    shape = lattice.metadata.get('shape')
    if not isinstance(shape, tuple) or len(shape) != 3:
        raise ValueError('BCC lattice metadata missing shape information')
    nx, ny, nz = shape
    corner_index = lattice.metadata.get('corner_index')
    center_index = lattice.metadata.get('center_index')
    if not isinstance(corner_index, dict) or not isinstance(center_index, dict):
        raise ValueError('BCC lattice metadata missing index maps')
    loops: list[Loop] = []

    def add_x_loops() -> None:
        for i in range(nx - 1):
            for j in range(ny):
                for k in range(nz):
                    left = center_index[(i, j, k)]
                    right = center_index[(i + 1, j, k)]
                    for dj in (0, 1):
                        for dk in (0, 1):
                            c1 = corner_index[(i + 1, j + dj, k + dk)]
                            c2 = corner_index[(i + 1, j + 1 - dj, k + 1 - dk)]
                            loops.append((left, c1, right, c2))

    def add_y_loops() -> None:
        for i in range(nx):
            for j in range(ny - 1):
                for k in range(nz):
                    left = center_index[(i, j, k)]
                    right = center_index[(i, j + 1, k)]
                    for di in (0, 1):
                        for dk in (0, 1):
                            c1 = corner_index[(i + di, j + 1, k + dk)]
                            c2 = corner_index[(i + 1 - di, j + 1, k + 1 - dk)]
                            loops.append((left, c1, right, c2))

    def add_z_loops() -> None:
        for i in range(nx):
            for j in range(ny):
                for k in range(nz - 1):
                    left = center_index[(i, j, k)]
                    right = center_index[(i, j, k + 1)]
                    for di in (0, 1):
                        for dj in (0, 1):
                            c1 = corner_index[(i + di, j + dj, k + 1)]
                            c2 = corner_index[(i + 1 - di, j + 1 - dj, k + 1)]
                            loops.append((left, c1, right, c2))

    add_x_loops()
    add_y_loops()
    add_z_loops()
    return tuple(loops)


def plaquette_incidence(plaquettes: tuple[Loop, ...]) -> dict[tuple[int, int], tuple[int, ...]]:
    incidence: dict[tuple[int, int], list[int]] = defaultdict(list)
    for p_index, loop in enumerate(plaquettes):
        n = len(loop)
        for i in range(n):
            a = loop[i]
            b = loop[(i + 1) % n]
            key = (a, b) if a < b else (b, a)
            incidence[key].append(p_index)
    return {key: tuple(indices) for key, indices in incidence.items()}
