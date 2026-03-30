from __future__ import annotations

from typing import Iterable

import numpy as np

Array = np.ndarray


def random_su2(*, rng: np.random.Generator | None = None) -> Array:
    gen = np.random.default_rng() if rng is None else rng
    q = gen.normal(size=4)
    q = q / np.linalg.norm(q)
    a, b, c, d = q
    return np.asarray([[a + 1j * b, c + 1j * d], [-c + 1j * d, a - 1j * b]], dtype=np.complex128)


def identity_links(edges: Iterable[tuple[int, int]]) -> dict[tuple[int, int], Array]:
    ident = np.eye(2, dtype=np.complex128)
    return {tuple(edge): ident.copy() for edge in edges}


def random_su2_links(edges: Iterable[tuple[int, int]], *, seed: int | None = None) -> dict[tuple[int, int], Array]:
    rng = np.random.default_rng(seed)
    return {tuple(edge): random_su2(rng=rng) for edge in edges}


def project_to_su2(matrix: Array) -> Array:
    u, _, vh = np.linalg.svd(matrix)
    candidate = u @ vh
    return (candidate / np.sqrt(np.linalg.det(candidate))).astype(np.complex128)
