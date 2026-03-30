from __future__ import annotations

import numpy as np

from zsim.lgt.su2_links import project_to_su2, random_su2_links

Array = np.ndarray
_SIGMA1 = np.asarray([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
_SIGMA2 = np.asarray([[0.0, -1j], [1j, 0.0]], dtype=np.complex128)
_SIGMA3 = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
_PAULI = (_SIGMA1, _SIGMA2, _SIGMA3)


def _su2_from_vector(vec: Array) -> Array:
    theta = float(np.linalg.norm(vec))
    if theta < 1e-12:
        return np.eye(2, dtype=np.complex128)
    axis = vec / theta
    sigma = axis[0] * _SIGMA1 + axis[1] * _SIGMA2 + axis[2] * _SIGMA3
    return project_to_su2(np.cos(theta) * np.eye(2, dtype=np.complex128) + 1j * np.sin(theta) * sigma)


def caloron_pair_links(
    edges: tuple[tuple[int, int], ...],
    positions: Array,
    amplitude: float,
    *,
    separation: float = 0.75,
    width: float = 0.55,
    seam_bias: float = 0.15,
) -> dict[tuple[int, int], Array]:
    """Build a smooth instanton/anti-instanton surrogate on the reduced lattice.

    This is not a continuum caloron solution. It is a structured non-Abelian background
    with two separated lumps of opposite sign and a seam-like z-bias, designed to move
    the reduced MBP extractor away from the almost-pure-gauge collective toy model.
    """
    center = np.mean(positions, axis=0)
    c_i = center + np.asarray([0.5 * separation, 0.0, 0.0])
    c_a = center - np.asarray([0.5 * separation, 0.0, 0.0])
    denom = max(float(width) ** 2, 1e-8)
    links: dict[tuple[int, int], Array] = {}
    for edge in edges:
        i, j = edge
        midpoint = 0.5 * (positions[i] + positions[j])
        r_i = midpoint - c_i
        r_a = midpoint - c_a
        w_i = np.exp(-float(np.dot(r_i, r_i)) / denom)
        w_a = np.exp(-float(np.dot(r_a, r_a)) / denom)
        # Non-Abelian orientation: x and y from the two lumps, z from the seam.
        vec = float(amplitude) * np.asarray([
            w_i - w_a,
            (r_i[1] * w_i) - (r_a[1] * w_a),
            seam_bias * np.sign(midpoint[0] - center[0]) * (w_i + w_a),
        ], dtype=float)
        links[edge] = _su2_from_vector(vec)
    return links


def scrambled_caloron_links(
    edges: tuple[tuple[int, int], ...],
    positions: Array,
    amplitude: float,
    *,
    seed: int | None = None,
) -> dict[tuple[int, int], Array]:
    """Negative control: destroy geometric coherence while keeping rough scale."""
    base = caloron_pair_links(edges, positions, amplitude)
    rng = np.random.default_rng(seed)
    keys = list(base)
    mats = [base[k] for k in keys]
    rng.shuffle(mats)
    return {k: project_to_su2(mats[idx] + 0.15 * random_su2_links((k,), seed=None)[k]) for idx, k in enumerate(keys)}
