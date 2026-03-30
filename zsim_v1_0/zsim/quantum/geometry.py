from __future__ import annotations

from dataclasses import dataclass, field
from math import atan2, sqrt
from typing import Iterable

import numpy as np
from scipy.spatial import ConvexHull

Array = np.ndarray


@dataclass(frozen=True)
class PolyhedralComplex:
    name: str
    vertices: Array
    edges: tuple[tuple[int, int], ...]
    faces: tuple[tuple[int, ...], ...]
    metadata: dict[str, object] = field(default_factory=dict)

    @property
    def V(self) -> int:
        return int(self.vertices.shape[0])

    @property
    def E(self) -> int:
        return len(self.edges)

    @property
    def F(self) -> int:
        return len(self.faces)

    def adjacency_matrix(self) -> Array:
        adj = np.zeros((self.V, self.V), dtype=float)
        for i, j in self.edges:
            adj[i, j] = 1.0
            adj[j, i] = 1.0
        return adj

    def degree_sequence(self) -> Array:
        return self.adjacency_matrix().sum(axis=1)


_TOL = 1e-8


def _unique_rows(points: Array, *, tol: float = 1e-8) -> Array:
    rounded = np.round(points / tol).astype(np.int64)
    _, idx = np.unique(rounded, axis=0, return_index=True)
    return points[np.sort(idx)]


def _normalize(vec: Array) -> Array:
    return vec / np.linalg.norm(vec)


def _plane_key(normal: Array, offset: float, *, tol: float = 1e-8) -> tuple[int, int, int, int]:
    n = np.asarray(normal, dtype=float)
    d = float(offset)
    if tuple(n) < tuple(-n):
        n = -n
        d = -d
    vals = np.round(np.concatenate([n, [d]]) / tol).astype(int)
    return tuple(int(v) for v in vals)


def _order_face_vertices(points: Array, vertex_ids: Iterable[int], normal: Array) -> tuple[int, ...]:
    ids = list(dict.fromkeys(int(v) for v in vertex_ids))
    pts = points[ids]
    centroid = pts.mean(axis=0)
    normal = _normalize(np.asarray(normal, dtype=float))
    ref = pts[0] - centroid
    ref = ref - np.dot(ref, normal) * normal
    if np.linalg.norm(ref) < _TOL:
        ref = pts[1] - centroid
        ref = ref - np.dot(ref, normal) * normal
    ref = _normalize(ref)
    tangent = _normalize(np.cross(normal, ref))
    angles = []
    for idx, p in zip(ids, pts, strict=True):
        rel = p - centroid
        x = float(np.dot(rel, ref))
        y = float(np.dot(rel, tangent))
        angles.append((atan2(y, x), idx))
    angles.sort()
    return tuple(idx for _, idx in angles)


def convex_polyhedron_faces(points: Array) -> tuple[tuple[int, ...], ...]:
    hull = ConvexHull(points)
    groups: dict[tuple[int, int, int, int], dict[str, object]] = {}
    for simplex, equation in zip(hull.simplices, hull.equations, strict=True):
        normal = np.asarray(equation[:-1], dtype=float)
        offset = float(equation[-1])
        key = _plane_key(normal, offset)
        groups.setdefault(key, {'normal': normal, 'offset': offset})
    faces = []
    for entry in groups.values():
        normal = np.asarray(entry['normal'], dtype=float)
        offset = float(entry['offset'])
        ids = [i for i, dist in enumerate(points @ normal + offset) if abs(float(dist)) < 5e-7]
        faces.append(_order_face_vertices(points, ids, normal))
    return tuple(sorted(set(faces), key=lambda face: (len(face), face)))


def edges_from_faces(faces: Iterable[tuple[int, ...]]) -> tuple[tuple[int, int], ...]:
    edges: set[tuple[int, int]] = set()
    for face in faces:
        m = len(face)
        for i in range(m):
            a = int(face[i])
            b = int(face[(i + 1) % m])
            edges.add((a, b) if a < b else (b, a))
    return tuple(sorted(edges))


def _base_polyhedron(name: str) -> PolyhedralComplex:
    if name == 'icosahedron':
        phi = (1.0 + sqrt(5.0)) / 2.0
        raw = []
        for x in (-1.0, 1.0):
            for y in (-phi, phi):
                raw.extend([(0.0, x, y), (y, 0.0, x), (x, y, 0.0)])
        vertices = _unique_rows(np.asarray(raw, dtype=float))
    elif name == 'octahedron':
        vertices = np.asarray([
            (1.0, 0.0, 0.0), (-1.0, 0.0, 0.0),
            (0.0, 1.0, 0.0), (0.0, -1.0, 0.0),
            (0.0, 0.0, 1.0), (0.0, 0.0, -1.0),
        ], dtype=float)
    else:
        raise ValueError(f'Unsupported base polyhedron: {name}')
    faces = convex_polyhedron_faces(vertices)
    edges = edges_from_faces(faces)
    return PolyhedralComplex(name=name, vertices=vertices, edges=edges, faces=faces)


def _cyclic_neighbors_around_vertex(base: PolyhedralComplex, vertex: int) -> tuple[int, ...]:
    neighbors = set()
    adjacency: dict[int, set[int]] = {}
    for face in base.faces:
        if vertex not in face:
            continue
        idx = face.index(vertex)
        prev_n = int(face[(idx - 1) % len(face)])
        next_n = int(face[(idx + 1) % len(face)])
        neighbors.update([prev_n, next_n])
        adjacency.setdefault(prev_n, set()).add(next_n)
        adjacency.setdefault(next_n, set()).add(prev_n)
    start = min(neighbors)
    order = [start]
    prev = None
    current = start
    while True:
        options = sorted(adjacency[current] - ({prev} if prev is not None else set()))
        if not options:
            break
        nxt = options[0]
        if nxt == start or nxt in order:
            break
        order.append(nxt)
        prev, current = current, nxt
        if len(order) == len(neighbors):
            break
    if len(order) != len(neighbors):
        order.extend(sorted(neighbors - set(order)))
    return tuple(order)


def truncate_polyhedron(base: PolyhedralComplex, *, fraction: float = 1.0 / 3.0, name: str | None = None) -> PolyhedralComplex:
    lookup: dict[tuple[int, int], int] = {}
    oriented_vertices: list[Array] = []
    for i, j in base.edges:
        lookup[(i, j)] = len(oriented_vertices)
        oriented_vertices.append((1.0 - fraction) * base.vertices[i] + fraction * base.vertices[j])
        lookup[(j, i)] = len(oriented_vertices)
        oriented_vertices.append((1.0 - fraction) * base.vertices[j] + fraction * base.vertices[i])
    vertices = np.asarray(oriented_vertices, dtype=float)

    faces: list[tuple[int, ...]] = []
    for i in range(base.V):
        cycle = _cyclic_neighbors_around_vertex(base, i)
        faces.append(tuple(lookup[(i, j)] for j in cycle))

    for face in base.faces:
        expanded: list[int] = []
        for i in range(len(face)):
            a = int(face[i])
            b = int(face[(i + 1) % len(face)])
            expanded.extend([lookup[(a, b)], lookup[(b, a)]])
        faces.append(tuple(expanded))

    edges = edges_from_faces(faces)
    return PolyhedralComplex(
        name=name or f'truncated_{base.name}',
        vertices=vertices,
        edges=edges,
        faces=tuple(sorted(faces, key=lambda f: (len(f), f))),
        metadata={'base_polyhedron': base.name, 'truncation_fraction': fraction},
    )


def build_truncated_icosahedron() -> PolyhedralComplex:
    return truncate_polyhedron(_base_polyhedron('icosahedron'), name='truncated_icosahedron')


def build_truncated_octahedron() -> PolyhedralComplex:
    return truncate_polyhedron(_base_polyhedron('octahedron'), name='truncated_octahedron')
