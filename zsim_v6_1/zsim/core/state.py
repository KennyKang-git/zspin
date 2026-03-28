"""State model for Z-Sim v3.1.

This module defines the canonical reduced-order state vector used throughout the
engine. The state object is intentionally small, explicit, and serialization-
friendly so that solver, observables, and validation layers can share one common
contract.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, replace as dc_replace
from math import isfinite
from typing import Any, ClassVar

import numpy as np

from .exceptions import StateSerializationError, StateValidationError

STATE_VECTOR_FIELDS: tuple[str, ...] = (
    "N",
    "a",
    "h",
    "epsilon",
    "pi_epsilon",
    "rho_x",
    "rho_z",
    "rho_y",
    "J_xz",
    "J_zy",
    "phi_z",
    "sigma_struct",
)


@dataclass(frozen=True, slots=True)
class ZSimState:
    """Canonical state vector for Z-Sim v3.1.

    Notes
    -----
    - The state is frozen to prevent accidental in-place mutation across solver
      boundaries. Explicit replacement is encouraged instead.
    - Both ``N`` and ``a`` are retained because v0.1 treats them as part of the
      public state contract, even though they are related by definition in many
      runs.
    """

    VECTOR_FIELDS: ClassVar[tuple[str, ...]] = STATE_VECTOR_FIELDS

    N: float
    a: float
    h: float
    epsilon: float
    pi_epsilon: float
    rho_x: float
    rho_z: float
    rho_y: float
    J_xz: float
    J_zy: float
    phi_z: float
    sigma_struct: float

    @property
    def rho_total(self) -> float:
        """Total sector density."""
        return self.rho_x + self.rho_z + self.rho_y

    @property
    def omega_x(self) -> float:
        """X-sector density fraction."""
        return self._safe_fraction(self.rho_x, self.rho_total)

    @property
    def omega_z(self) -> float:
        """Z-sector density fraction."""
        return self._safe_fraction(self.rho_z, self.rho_total)

    @property
    def omega_y(self) -> float:
        """Y-sector density fraction."""
        return self._safe_fraction(self.rho_y, self.rho_total)

    @property
    def ordered_values(self) -> tuple[float, ...]:
        """State values in canonical vector order."""
        return tuple(getattr(self, field) for field in self.VECTOR_FIELDS)

    def to_dict(self) -> dict[str, float]:
        """Serialize the state to a plain dictionary in canonical field order."""
        return {field: float(value) for field, value in asdict(self).items()}

    def to_array(self, *, dtype: Any = float) -> np.ndarray:
        """Serialize the state to a 1D NumPy array in canonical field order."""
        return np.asarray(self.ordered_values, dtype=dtype)

    def replace(self, **changes: float) -> "ZSimState":
        """Return a new state with selected fields updated."""
        unknown = sorted(set(changes) - set(self.VECTOR_FIELDS))
        if unknown:
            raise StateSerializationError(f"Unknown state field(s) in replace(): {unknown}")
        return dc_replace(self, **changes)

    def validate(
        self,
        *,
        require_nonnegative_densities: bool = True,
        require_positive_scale_factor: bool = True,
    ) -> "ZSimState":
        """Validate structural and numerical state invariants.

        Returns
        -------
        ZSimState
            Returns ``self`` to allow fluent usage.
        """
        nonfinite = [field for field in self.VECTOR_FIELDS if not isfinite(getattr(self, field))]
        if nonfinite:
            raise StateValidationError(f"Non-finite state field(s): {nonfinite}")

        if require_positive_scale_factor and self.a <= 0.0:
            raise StateValidationError("Scale factor 'a' must be strictly positive.")

        if require_nonnegative_densities:
            negative = [name for name in ("rho_x", "rho_z", "rho_y") if getattr(self, name) < 0.0]
            if negative:
                raise StateValidationError(f"Density field(s) must be non-negative: {negative}")

        return self

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> "ZSimState":
        """Construct a state from a mapping.

        Extra keys are rejected to keep the state contract explicit.
        """
        expected = set(cls.VECTOR_FIELDS)
        provided = set(payload)
        missing = sorted(expected - provided)
        extra = sorted(provided - expected)

        if missing or extra:
            msg_parts = []
            if missing:
                msg_parts.append(f"missing keys={missing}")
            if extra:
                msg_parts.append(f"extra keys={extra}")
            raise StateSerializationError("Invalid state mapping: " + "; ".join(msg_parts))

        try:
            return cls(**{field: float(payload[field]) for field in cls.VECTOR_FIELDS})
        except (TypeError, ValueError) as exc:
            raise StateSerializationError(f"Failed to build state from mapping: {exc}") from exc

    @classmethod
    def from_array(cls, values: Any) -> "ZSimState":
        """Construct a state from an ordered array-like object."""
        array = np.asarray(values, dtype=float)
        if array.ndim != 1:
            raise StateSerializationError("State array must be 1-dimensional.")
        if array.size != len(cls.VECTOR_FIELDS):
            raise StateSerializationError(
                f"State array length mismatch: expected {len(cls.VECTOR_FIELDS)}, got {array.size}."
            )
        return cls(**dict(zip(cls.VECTOR_FIELDS, array.tolist(), strict=True)))

    @staticmethod
    def _safe_fraction(numerator: float, denominator: float) -> float:
        if denominator == 0.0:
            raise StateValidationError("Cannot compute density fraction when rho_total is zero.")
        return numerator / denominator
