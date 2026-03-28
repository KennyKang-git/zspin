"""Epistemic validation helpers for Z-Sim v3.1."""

from __future__ import annotations

from typing import Mapping

from zsim.core import LabeledValue, Status, assert_status_not_overclaimed



def validate_labeled_value(value: LabeledValue, claimed: Status | None = None) -> LabeledValue:
    """Validate one labeled value and optional surfaced claim strength."""
    if claimed is not None:
        assert_status_not_overclaimed(value.status, claimed, name=value.name)
    return value



def validate_claim_map(values: Mapping[str, LabeledValue], claims: Mapping[str, Status]) -> None:
    """Validate a map of public claims against stored labels."""
    for name, claimed in claims.items():
        if name not in values:
            continue
        assert_status_not_overclaimed(values[name].status, claimed, name=name)


__all__ = ["validate_claim_map", "validate_labeled_value"]
