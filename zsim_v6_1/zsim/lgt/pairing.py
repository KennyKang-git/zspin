from __future__ import annotations

from dataclasses import dataclass
import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class NearZeroPairingSummary:
    pair_count: int
    sample_size: int
    sigma_values: tuple[float, ...]
    pair_mean: float
    pair_gap_mean: float
    bulk_mean: float
    bulk_gap: float
    normalized_gap: float
    score: float

    def to_dict(self) -> dict[str, float | int | list[float]]:
        return {
            'pair_count': self.pair_count,
            'sample_size': self.sample_size,
            'sigma_values': list(self.sigma_values),
            'pair_mean': self.pair_mean,
            'pair_gap_mean': self.pair_gap_mean,
            'bulk_mean': self.bulk_mean,
            'bulk_gap': self.bulk_gap,
            'normalized_gap': self.normalized_gap,
            'score': self.score,
        }


def analyze_near_zero_pairs_from_singular_values(values: Array, *, pair_count: int = 2, sample_size: int = 8) -> NearZeroPairingSummary:
    vals = np.sort(np.real_if_close(np.asarray(values, dtype=float)))
    if vals.size == 0:
        raise ValueError('empty singular-value array')
    m = min(int(sample_size), vals.size)
    sigma = vals[:m]
    usable = min(2 * int(pair_count), (sigma.size // 2) * 2)
    if usable == 0:
        raise ValueError('not enough singular values for pairing analysis')
    sigma = sigma[:usable]
    pairs = sigma.reshape(-1, 2)
    pair_means = np.mean(pairs, axis=1)
    pair_gaps = np.abs(pairs[:, 1] - pairs[:, 0])
    bulk = vals[usable:min(vals.size, usable + max(2, int(sample_size) - usable))]
    bulk_mean = float(np.mean(bulk)) if bulk.size else float(np.max(pair_means))
    pair_mean = float(np.mean(pair_means))
    pair_gap_mean = float(np.mean(pair_gaps))
    bulk_gap = float(max(0.0, bulk_mean - pair_mean))
    normalized_gap = float(pair_gap_mean / (pair_mean + 1.0e-12))
    score = float((bulk_gap / (pair_mean + 1.0e-12)) / (1.0 + normalized_gap))
    return NearZeroPairingSummary(
        pair_count=int(pairs.shape[0]),
        sample_size=int(vals.size),
        sigma_values=tuple(float(v) for v in sigma.tolist()),
        pair_mean=pair_mean,
        pair_gap_mean=pair_gap_mean,
        bulk_mean=bulk_mean,
        bulk_gap=bulk_gap,
        normalized_gap=normalized_gap,
        score=score,
    )


def analyze_near_zero_pairs_from_matrix(matrix: Array, *, pair_count: int = 2, sample_size: int = 8) -> NearZeroPairingSummary:
    singular = np.linalg.svd(matrix, compute_uv=False)
    return analyze_near_zero_pairs_from_singular_values(singular, pair_count=pair_count, sample_size=sample_size)
