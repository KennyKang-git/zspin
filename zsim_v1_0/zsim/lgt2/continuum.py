"""Continuum extrapolation framework for lattice observables.

Architecture improvement #4: Systematic a→0 extrapolation.

On the lattice, physical observables receive corrections in powers of
the lattice spacing a:
  O(a) = O_continuum + c₁ a + c₂ a² + ...    (naive/staggered)
  O(a) = O_continuum + c₂ a² + c₄ a⁴ + ...   (Wilson, O(a) improved)

The continuum limit is extracted by:
  1. Computing O(a) at multiple lattice spacings (= multiple β values)
  2. Fitting to the expected functional form
  3. Extrapolating to a = 0

For the Wilson fermion action (used in the overlap kernel):
  - Leading lattice artifacts are O(a²)
  - With improvement (Sheikholeslami-Wohlert): O(a) artifacts removed
  - The overlap operator has automatic O(a) improvement

The lattice spacing a(β) is determined by:
  - The Sommer scale r₀: r₀²F(r₀) = 1.65
  - Or the gradient flow scale t₀: t₀²<E(t₀)> = 0.3
  - Or matching to the string tension: σa² = known function of β
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

import numpy as np

Array = np.ndarray


@dataclass(frozen=True)
class ExtrapolationPoint:
    """A single measurement at a given lattice spacing."""
    beta: float           # bare coupling β = 4/g₀²
    lattice_spacing: float  # a in physical units
    shape: tuple[int, int, int]
    observable: float     # measured value
    observable_error: float  # statistical error
    label: str = ""       # e.g. "gamma_h2_trace"


@dataclass(frozen=True)
class ExtrapolationResult:
    """Result of continuum extrapolation."""
    continuum_value: float
    continuum_error: float
    chi2_per_dof: float
    coefficients: tuple[float, ...]  # (O_cont, c₂, c₄, ...)
    fit_order: int         # highest power of a included
    n_points: int
    a_values: tuple[float, ...]
    measured_values: tuple[float, ...]
    fitted_values: tuple[float, ...]
    label: str


def lattice_spacing_from_beta(beta: float, *,
                               r0_physical: float = 0.5,
                               method: str = "two_loop") -> float:
    """Estimate lattice spacing a(β) for SU(2) using perturbation theory.

    Two-loop asymptotic scaling for SU(2):
      a/r₀ = (b₀ g²)^{-b₁/(2b₀²)} exp(-1/(2b₀g²))
    where g² = 4/β, b₀ = 11/(12π²), b₁ = 17/(24π⁴) for SU(2).

    Parameters
    ----------
    beta : float
        Bare coupling β = 4/g₀².
    r0_physical : float
        Physical value of the Sommer scale r₀ (in fm or GeV⁻¹).
    method : str
        "two_loop" or "one_loop".

    Returns
    -------
    float
        Lattice spacing a in the same units as r0_physical.
    """
    g2 = 4.0 / beta
    # SU(2) beta-function coefficients
    b0 = 11.0 / (12.0 * np.pi**2)
    b1 = 17.0 / (24.0 * np.pi**4)

    if method == "one_loop":
        a_over_r0 = np.exp(-1.0 / (2.0 * b0 * g2))
    else:  # two_loop
        a_over_r0 = (b0 * g2) ** (-b1 / (2 * b0**2)) * np.exp(-1.0 / (2 * b0 * g2))

    return float(r0_physical * a_over_r0)


def extrapolate_to_continuum(
    points: Sequence[ExtrapolationPoint],
    *,
    max_order: int = 2,
    scaling_power: int = 2,
) -> ExtrapolationResult:
    """Extrapolate lattice observable to the continuum limit.

    Fits O(a) = O_cont + Σ_{k=1}^{max_order} c_k × a^{k×scaling_power}

    For Wilson/overlap fermions, scaling_power=2 (O(a²) artifacts).

    Parameters
    ----------
    points : Sequence[ExtrapolationPoint]
        Measurements at different lattice spacings.
    max_order : int
        Highest order in the polynomial fit.
    scaling_power : int
        Leading power of a in the lattice artifact.

    Returns
    -------
    ExtrapolationResult
    """
    n = len(points)
    if n < 2:
        # Can't extrapolate with < 2 points
        p = points[0]
        return ExtrapolationResult(
            continuum_value=p.observable,
            continuum_error=p.observable_error,
            chi2_per_dof=0.0,
            coefficients=(p.observable,),
            fit_order=0,
            n_points=1,
            a_values=(p.lattice_spacing,),
            measured_values=(p.observable,),
            fitted_values=(p.observable,),
            label=p.label,
        )

    # Sort by lattice spacing (finest first)
    sorted_pts = sorted(points, key=lambda p: p.lattice_spacing)

    a_vals = np.array([p.lattice_spacing for p in sorted_pts])
    y_vals = np.array([p.observable for p in sorted_pts])
    y_errs = np.array([max(p.observable_error, 1e-15) for p in sorted_pts])

    # Determine fit order (can't exceed n_points - 1)
    order = min(max_order, n - 1)

    # Design matrix: [1, a^p, a^{2p}, ...]
    powers = [k * scaling_power for k in range(order + 1)]
    powers[0] = 0  # constant term
    A = np.column_stack([a_vals**p for p in powers])
    W = np.diag(1.0 / y_errs**2)

    # Weighted least squares: (A^T W A) c = A^T W y
    AW = A.T @ W
    coeffs = np.linalg.lstsq(AW @ A, AW @ y_vals, rcond=None)[0]

    # Fitted values and chi²
    y_fit = A @ coeffs
    residuals = (y_vals - y_fit) / y_errs
    dof = max(n - len(coeffs), 1)
    chi2_dof = float(np.sum(residuals**2)) / dof

    # Error on continuum value from covariance
    cov = np.linalg.inv(AW @ A)
    cont_err = float(np.sqrt(cov[0, 0]))

    return ExtrapolationResult(
        continuum_value=float(coeffs[0]),
        continuum_error=cont_err,
        chi2_per_dof=chi2_dof,
        coefficients=tuple(float(c) for c in coeffs),
        fit_order=order,
        n_points=n,
        a_values=tuple(float(a) for a in a_vals),
        measured_values=tuple(float(y) for y in y_vals),
        fitted_values=tuple(float(y) for y in y_fit),
        label=sorted_pts[0].label,
    )


class ContinuumExtrapolator:
    """Manages multi-β runs and continuum extrapolation.

    Usage:
        ext = ContinuumExtrapolator()
        for beta in [2.0, 2.3, 2.5, 2.7]:
            a = lattice_spacing_from_beta(beta)
            result = run_mbp2_pipeline(shape=(4,4,4), lattice_spacing=a, beta=beta)
            ext.add_point("gamma_h2_trace", beta, a, (4,4,4),
                         result.gamma_h2_trace, 0.01)
        continuum = ext.extrapolate("gamma_h2_trace")
    """

    def __init__(self):
        self._points: dict[str, list[ExtrapolationPoint]] = {}

    def add_point(self, label: str, beta: float, a: float,
                  shape: tuple[int, int, int],
                  value: float, error: float = 0.0) -> None:
        if label not in self._points:
            self._points[label] = []
        self._points[label].append(
            ExtrapolationPoint(beta=beta, lattice_spacing=a,
                              shape=shape, observable=value,
                              observable_error=error, label=label)
        )

    def extrapolate(self, label: str, **kwargs) -> ExtrapolationResult:
        if label not in self._points:
            raise KeyError(f"No data for observable '{label}'")
        return extrapolate_to_continuum(self._points[label], **kwargs)

    def all_labels(self) -> list[str]:
        return list(self._points.keys())

    def summary(self) -> dict[str, ExtrapolationResult]:
        return {label: self.extrapolate(label) for label in self._points}
