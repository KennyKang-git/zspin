"""Sector metadata helpers for Z-Sim v3.1.

These helpers keep the X/Z/Y partition available as a first-class software
object. The module is intentionally small: it exposes fixed dimensions,
lightweight ratio helpers, and an explicit answer to whether a direct X↔Y edge
is allowed in v0.1.
"""

from __future__ import annotations

from zsim.core import DIM_X, DIM_Y, DIM_Z, get_sector_dims


VALID_SECTORS = ("X", "Z", "Y")


def get_sector_order() -> tuple[str, str, str]:
    """Return canonical sector order used across structural kernels."""
    return VALID_SECTORS


def canonical_sector_order() -> tuple[str, str, str]:
    """Backward-compatible alias for the canonical X-Z-Y order."""
    return get_sector_order()



def sector_ratio(src: str, dst: str) -> float:
    """Return dim(src) / dim(dst) for known sectors."""
    dims = get_sector_dims()
    if src not in dims or dst not in dims:
        raise KeyError(f"Unknown sector pair: {src!r}, {dst!r}")
    return dims[src] / dims[dst]



def is_direct_xy_allowed() -> bool:
    """Direct X↔Y coupling is forbidden in Z-Sim v3.1."""
    return False


__all__ = [
    "VALID_SECTORS",
    "get_sector_order",
    "canonical_sector_order",
    "get_sector_dims",
    "sector_ratio",
    "is_direct_xy_allowed",
    "DIM_X",
    "DIM_Z",
    "DIM_Y",
]
