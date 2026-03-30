from __future__ import annotations

import numpy as np

Array = np.ndarray


def eigensystem(matrix: Array, *, hermitian: bool = True) -> tuple[Array, Array]:
    values, vectors = np.linalg.eigh(matrix) if hermitian else np.linalg.eig(matrix)
    order = np.argsort(values)
    return values[order], vectors[:, order]


def spectral_summary(values: Array, *, tol: float = 1e-8) -> dict[str, object]:
    real_vals = np.real_if_close(values)
    rounded = np.round(real_vals / tol) * tol
    unique, counts = np.unique(rounded, return_counts=True)
    return {
        'dimension': int(values.shape[0]),
        'trace': float(np.real_if_close(np.sum(values))),
        'min': float(np.min(real_vals)),
        'max': float(np.max(real_vals)),
        'zero_mode_count': int(np.sum(np.abs(real_vals) < tol)),
        'degeneracies': [
            {'eigenvalue': float(val), 'count': int(count)}
            for val, count in zip(unique, counts, strict=True)
        ],
    }
