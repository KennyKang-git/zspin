"""Epistemic labels and overclaim guards for Z-Sim v3.1.

The project needs an explicit way to distinguish theory-fixed objects from
engineering translations and optional hypotheses. This module provides a small,
portable labeling layer that downstream modules can attach to values, closures,
and run metadata.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Final, Mapping


class Status(str, Enum):
    """Allowed epistemic statuses for Z-Sim objects."""

    PROVEN = "PROVEN"
    DERIVED = "DERIVED"
    TRANSLATED = "TRANSLATED"
    HYPOTHESIS = "HYPOTHESIS"
    NON_CLAIM = "NON-CLAIM"


_STATUS_RANK: Final[dict[Status, int]] = {
    Status.PROVEN: 5,
    Status.DERIVED: 4,
    Status.TRANSLATED: 3,
    Status.HYPOTHESIS: 2,
    Status.NON_CLAIM: 1,
}


@dataclass(frozen=True, slots=True)
class LabeledValue:
    """Value annotated with epistemic provenance.

    Attributes:
        name: Logical identifier used in logs or reports.
        value: The underlying value.
        status: Epistemic label.
        rationale: Brief explanation of why the label was chosen.
        metadata: Optional structured metadata for serialization.
    """

    name: str
    value: Any
    status: Status
    rationale: str
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to a JSON-serializable dictionary where possible."""

        return {
            "name": self.name,
            "value": self.value,
            "status": self.status.value,
            "rationale": self.rationale,
            "metadata": dict(self.metadata),
        }


class EpistemicOverclaimError(ValueError):
    """Raised when a weaker status is promoted beyond its allowed strength."""


class UnknownStatusError(ValueError):
    """Raised when a non-Status object is used in validation."""


def status_rank(status: Status) -> int:
    """Return monotonic strength ordering for a status.

    Higher means epistemically stronger.
    """

    if not isinstance(status, Status):
        raise UnknownStatusError(f"Expected Status, received: {status!r}")
    return _STATUS_RANK[status]


def assert_status_not_overclaimed(actual: Status, claimed: Status, *, name: str = "object") -> None:
    """Reject claims that are stronger than the object's assigned status.

    Example:
        A TRANSLATED closure cannot be surfaced as PROVEN.
    """

    if status_rank(claimed) > status_rank(actual):
        raise EpistemicOverclaimError(
            f"{name} is labeled {actual.value}, but was claimed as {claimed.value}."
        )


def ensure_minimum_status(actual: Status, minimum: Status, *, name: str = "object") -> None:
    """Require that a status is at least as strong as a minimum threshold."""

    if status_rank(actual) < status_rank(minimum):
        raise EpistemicOverclaimError(
            f"{name} has status {actual.value}, which is below required minimum {minimum.value}."
        )


__all__ = [
    "Status",
    "LabeledValue",
    "EpistemicOverclaimError",
    "UnknownStatusError",
    "status_rank",
    "assert_status_not_overclaimed",
    "ensure_minimum_status",
]
