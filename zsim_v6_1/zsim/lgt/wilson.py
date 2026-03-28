from __future__ import annotations

from collections import defaultdict

import numpy as np

from zsim.lgt.loops import Loop

Array = np.ndarray


def oriented_link_matrix(links: dict[tuple[int, int], Array], start: int, stop: int) -> Array:
    if (start, stop) in links:
        return links[(start, stop)]
    if (stop, start) in links:
        return links[(stop, start)].conj().T
    raise KeyError(f'missing link for oriented edge {(start, stop)}')


def loop_holonomy(links: dict[tuple[int, int], Array], loop: Loop) -> Array:
    acc = np.eye(2, dtype=np.complex128)
    n = len(loop)
    for i in range(n):
        acc = acc @ oriented_link_matrix(links, loop[i], loop[(i + 1) % n])
    return acc


def loop_half_trace(links: dict[tuple[int, int], Array], loop: Loop) -> float:
    return float(np.real(np.trace(loop_holonomy(links, loop))) / 2.0)


def plaquette_observables(links: dict[tuple[int, int], Array], plaquettes: tuple[Loop, ...]) -> dict[str, float]:
    if not plaquettes:
        return {
            'num_plaquettes': 0.0,
            'avg_plaquette': 1.0,
            'min_plaquette': 1.0,
            'max_plaquette': 1.0,
            'wilson_action_proxy': 0.0,
        }
    vals = [loop_half_trace(links, loop) for loop in plaquettes]
    return {
        'num_plaquettes': float(len(vals)),
        'avg_plaquette': float(np.mean(vals)),
        'min_plaquette': float(np.min(vals)),
        'max_plaquette': float(np.max(vals)),
        'wilson_action_proxy': float(sum(1.0 - v for v in vals)),
    }


def _edge_staple_from_loop(links: dict[tuple[int, int], Array], loop: Loop, u: int, v: int) -> Array | None:
    n = len(loop)
    for i in range(n):
        a = loop[i]
        b = loop[(i + 1) % n]
        if a == u and b == v:
            acc = np.eye(2, dtype=np.complex128)
            cursor = b
            for step in range(1, n):
                nxt = loop[(i + 1 + step) % n]
                acc = acc @ oriented_link_matrix(links, cursor, nxt)
                cursor = nxt
            return acc
        if a == v and b == u:
            acc = np.eye(2, dtype=np.complex128)
            cursor = u
            for step in range(1, n):
                nxt = loop[(i + 1 + step) % n]
                acc = acc @ oriented_link_matrix(links, cursor, nxt)
                cursor = nxt
            return acc.conj().T
    return None


def staple_sums(links: dict[tuple[int, int], Array], plaquettes: tuple[Loop, ...]) -> dict[tuple[int, int], Array]:
    edge_to_loops: dict[tuple[int, int], list[Loop]] = defaultdict(list)
    for loop in plaquettes:
        n = len(loop)
        for i in range(n):
            a = loop[i]
            b = loop[(i + 1) % n]
            key = (a, b) if a < b else (b, a)
            edge_to_loops[key].append(loop)
    staples: dict[tuple[int, int], Array] = {}
    for edge in links:
        u, v = edge
        acc = np.zeros((2, 2), dtype=np.complex128)
        count = 0
        for loop in edge_to_loops.get(edge, []):
            staple = _edge_staple_from_loop(links, loop, u, v)
            if staple is not None:
                acc += staple
                count += 1
        staples[edge] = acc / count if count else np.eye(2, dtype=np.complex128)
    return staples
