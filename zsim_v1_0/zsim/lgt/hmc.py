from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
import math

import numpy as np


@dataclass(frozen=True)
class ReducedChainResult:
    samples: tuple[float, ...]
    accept_rate: float
    potential_mean: float


def _finite_difference_gradient(potential: Callable[[float], float], x: float, eps: float = 1.0e-5) -> float:
    return (potential(x + eps) - potential(x - eps)) / (2.0 * eps)


def reduced_collective_hmc(
    initial: float,
    *,
    potential: Callable[[float], float],
    gradient: Callable[[float], float] | None = None,
    steps: int,
    step_size: float = 0.12,
    leapfrog_steps: int = 6,
    seed: int | None = None,
) -> ReducedChainResult:
    rng = np.random.default_rng(seed)
    grad = gradient if gradient is not None else (lambda x: _finite_difference_gradient(potential, x))
    x = float(initial)
    samples: list[float] = []
    accepted = 0
    potentials: list[float] = []
    for _ in range(steps):
        p0 = float(rng.normal())
        x_prop = x
        p = p0 - 0.5 * step_size * grad(x_prop)
        for lf in range(leapfrog_steps):
            x_prop += step_size * p
            if lf != leapfrog_steps - 1:
                p -= step_size * grad(x_prop)
        p -= 0.5 * step_size * grad(x_prop)
        p = -p
        current_H = potential(x) + 0.5 * p0 * p0
        prop_H = potential(x_prop) + 0.5 * p * p
        if math.log(float(rng.random())) < min(0.0, current_H - prop_H):
            x = x_prop
            accepted += 1
        samples.append(x)
        potentials.append(potential(x))
    return ReducedChainResult(samples=tuple(samples), accept_rate=accepted / max(steps, 1), potential_mean=float(np.mean(potentials) if potentials else potential(x)))
