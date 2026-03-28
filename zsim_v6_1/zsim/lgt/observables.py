from __future__ import annotations

import numpy as np

from zsim.lgt.loops import Loop
from zsim.lgt.wilson import plaquette_observables

Array = np.ndarray


def link_observables(links: dict[tuple[int, int], Array], plaquettes: tuple[Loop, ...] = ()) -> dict[str, float]:
    traces = [float(np.real(np.trace(U)) / 2.0) for U in links.values()]
    defects = [float(np.linalg.norm(U.conj().T @ U - np.eye(2))) for U in links.values()]
    payload = {
        'avg_half_trace': float(np.mean(traces) if traces else 1.0),
        'max_unitarity_defect': float(np.max(defects) if defects else 0.0),
        'link_action_proxy': float(sum(1.0 - t for t in traces)),
    }
    payload.update(plaquette_observables(links, tuple(plaquettes)))
    return payload
