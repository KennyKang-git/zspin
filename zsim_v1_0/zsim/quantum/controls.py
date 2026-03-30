from __future__ import annotations

import random
from typing import Iterable

import numpy as np

Array = np.ndarray


def adjacency_from_edges(num_vertices: int, edges: Iterable[tuple[int, int]]) -> Array:
    adj = np.zeros((num_vertices, num_vertices), dtype=float)
    for i, j in edges:
        adj[i, j] = 1.0
        adj[j, i] = 1.0
    return adj


def random_cubic_graph(num_vertices: int, *, seed: int | None = None, max_tries: int = 256) -> tuple[tuple[int, int], ...]:
    if num_vertices % 2 != 0 or num_vertices < 4:
        raise ValueError('num_vertices must be even and >= 4')
    rng = random.Random(seed)
    stubs = [v for v in range(num_vertices) for _ in range(3)]
    for _ in range(max_tries):
        rng.shuffle(stubs)
        edges: set[tuple[int, int]] = set()
        ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b:
                ok = False
                break
            edge = (a, b) if a < b else (b, a)
            if edge in edges:
                ok = False
                break
            edges.add(edge)
        if ok:
            return tuple(sorted(edges))
    raise RuntimeError('failed to generate simple cubic graph')
