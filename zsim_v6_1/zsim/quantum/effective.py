from __future__ import annotations

import numpy as np

Array = np.ndarray


def regularized_logdet(values: Array, *, mu2: float = 1e-6) -> float:
    shifted = np.real_if_close(values) ** 2 + float(mu2)
    return float(np.sum(np.log(shifted)))


def heat_kernel_trace(values: Array, t: float) -> float:
    vals = np.real_if_close(values)
    return float(np.sum(np.exp(-float(t) * vals)))


def spectral_action_moments(values: Array) -> dict[str, float]:
    vals = np.real_if_close(values)
    return {
        'moment_1_abs': float(np.sum(np.abs(vals))),
        'moment_2': float(np.sum(vals ** 2)),
        'moment_4': float(np.sum(vals ** 4)),
    }
