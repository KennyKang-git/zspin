from __future__ import annotations

import numpy as np

from zsim.lgt.su2_links import project_to_su2

Array = np.ndarray
_SIGMA3 = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)


def collective_valley_links(edges: tuple[tuple[int, int], ...], positions: Array, amplitude: float) -> dict[tuple[int, int], Array]:
    midpoint_x = float(np.mean(positions[:, 0]))
    links = {}
    for edge in edges:
        i, j = edge
        sign = 1.0 if 0.5 * (positions[i, 0] + positions[j, 0]) >= midpoint_x else -1.0
        theta = float(amplitude) * sign
        U = np.cos(theta) * np.eye(2) + 1j * np.sin(theta) * _SIGMA3
        links[edge] = project_to_su2(U)
    return links


def fit_even_quartic_bilinear_proxy(amplitudes: Array, values: Array) -> dict[str, float]:
    amps = np.asarray(amplitudes, dtype=float)
    vals = np.asarray(values, dtype=float)
    design = np.column_stack([np.ones_like(amps), amps * amps, amps ** 4])
    coeffs, *_ = np.linalg.lstsq(design, vals, rcond=None)
    c0, c2, c4 = coeffs
    return {'c0': float(c0), 'kappa2_proxy': float(c2), 'c4': float(c4)}
