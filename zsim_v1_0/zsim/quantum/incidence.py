from __future__ import annotations

import numpy as np

from zsim.quantum.geometry import PolyhedralComplex

Array = np.ndarray


def boundary_matrices(complex_: PolyhedralComplex) -> tuple[Array, Array]:
    num_vertices = complex_.V
    num_edges = complex_.E
    num_faces = complex_.F
    B1 = np.zeros((num_vertices, num_edges), dtype=float)
    edge_to_idx = {edge: idx for idx, edge in enumerate(complex_.edges)}
    for idx, (u, v) in enumerate(complex_.edges):
        B1[u, idx] = -1.0
        B1[v, idx] = 1.0
    B2 = np.zeros((num_edges, num_faces), dtype=float)
    for face_idx, face in enumerate(complex_.faces):
        for i in range(len(face)):
            a = int(face[i])
            b = int(face[(i + 1) % len(face)])
            key = (a, b) if a < b else (b, a)
            sign = 1.0 if key == (a, b) else -1.0
            B2[edge_to_idx[key], face_idx] += sign
    return B1, B2


def assert_boundary_nilpotency(B1: Array, B2: Array, *, atol: float = 1e-10) -> None:
    product = B1 @ B2
    if not np.allclose(product, 0.0, atol=atol):
        raise ValueError(f'Boundary nilpotency failed: max={np.max(np.abs(product))}')
