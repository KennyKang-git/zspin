from __future__ import annotations

import numpy as np

Array = np.ndarray


def hodge_laplacians(B1: Array, B2: Array) -> tuple[Array, Array, Array]:
    return B1 @ B1.T, B1.T @ B1 + B2 @ B2.T, B2.T @ B2
