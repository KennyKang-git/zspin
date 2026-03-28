from __future__ import annotations

from collections import deque

import numpy as np

from zsim.lgt.bcc import BCCLattice

Array = np.ndarray


def bipartite_chirality_signs(lattice: BCCLattice) -> Array:
    """Return ±1 signs for the bipartite BCC scaffold.

    The reduced BCC supercell used in Z-Sim is bipartite. We use the graph coloring
    as a surrogate chirality/parity label so that a chiral projector can distinguish
    the two sublattices without introducing extra fermion species.
    """
    adj = [[] for _ in range(lattice.num_sites)]
    for i, j in lattice.edges:
        adj[i].append(j)
        adj[j].append(i)
    colors = np.zeros(lattice.num_sites, dtype=int)
    seen = np.zeros(lattice.num_sites, dtype=bool)
    for root in range(lattice.num_sites):
        if seen[root]:
            continue
        seen[root] = True
        colors[root] = 1
        dq: deque[int] = deque([root])
        while dq:
            node = dq.popleft()
            for nxt in adj[node]:
                if not seen[nxt]:
                    seen[nxt] = True
                    colors[nxt] = -colors[node]
                    dq.append(nxt)
                elif colors[nxt] == colors[node]:
                    raise ValueError('BCC scaffold unexpectedly lost bipartite structure')
    return colors.astype(float)


def gamma5_matrix(lattice: BCCLattice) -> Array:
    """Reduced gamma_5 surrogate with site-parity weighting.

    Each site carries a 2x2 internal block. Within the block we use sigma_3, and the
    site-level bipartite sign flips the handedness between sublattices.
    """
    signs = bipartite_chirality_signs(lattice)
    sigma3 = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    g5 = np.zeros((2 * lattice.num_sites, 2 * lattice.num_sites), dtype=np.complex128)
    for site, sign in enumerate(signs):
        sl = slice(2 * site, 2 * site + 2)
        g5[sl, sl] = float(sign) * sigma3
    return g5


def chirality_projector(lattice: BCCLattice, chirality_mode: str = 'vector') -> Array:
    g5 = gamma5_matrix(lattice)
    ident = np.eye(g5.shape[0], dtype=np.complex128)
    mode = str(chirality_mode)
    if mode == 'left':
        return 0.5 * (ident - g5)
    if mode == 'right':
        return 0.5 * (ident + g5)
    if mode in {'vector', 'both', 'all'}:
        return ident
    if mode == 'axial':
        return g5.copy()
    raise ValueError(f'unknown chirality mode: {chirality_mode}')
