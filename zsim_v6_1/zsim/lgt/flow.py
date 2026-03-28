from __future__ import annotations

import numpy as np

from zsim.lgt.loops import Loop
from zsim.lgt.su2_links import project_to_su2
from zsim.lgt.wilson import staple_sums

Array = np.ndarray


def cooling_step(links: dict[tuple[int, int], Array], plaquettes: tuple[Loop, ...] = (), *, alpha: float = 0.15) -> dict[tuple[int, int], Array]:
    if not plaquettes:
        ident = np.eye(2, dtype=np.complex128)
        return {edge: project_to_su2((1.0 - alpha) * U + alpha * ident) for edge, U in links.items()}
    staples = staple_sums(links, tuple(plaquettes))
    updated = {}
    for edge, U in links.items():
        suggestion = staples[edge]
        updated[edge] = project_to_su2((1.0 - alpha) * U + alpha * suggestion)
    return updated


def cooling_trajectory(links: dict[tuple[int, int], Array], steps: int, plaquettes: tuple[Loop, ...] = (), *, alpha: float = 0.15) -> list[dict[tuple[int, int], Array]]:
    states = [links]
    current = links
    for _ in range(steps):
        current = cooling_step(current, tuple(plaquettes), alpha=alpha)
        states.append(current)
    return states
