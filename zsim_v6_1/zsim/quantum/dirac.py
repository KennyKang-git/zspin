from __future__ import annotations

import numpy as np

Array = np.ndarray


def hodge_dirac(B1: Array, B2: Array) -> Array:
    nv, ne = B1.shape
    _, nf = B2.shape
    return np.block([
        [np.zeros((nv, nv)), B1, np.zeros((nv, nf))],
        [B1.T, np.zeros((ne, ne)), B2],
        [np.zeros((nf, nv)), B2.T, np.zeros((nf, nf))],
    ])
