"""Locked structural constants for Z-Sim v6.1 (was v3.1).

v6.1 changes (2026-03-21):
  - OMEGA_M_BARE switched from slot counting (39/121) to face counting (38/121)
  - OMEGA_M_EFF: 0.2984 → 0.2908
  - OMEGA_M_BARE_SLOT retained for historical reference
  - No changes to CMB pipeline (already uses face counting CDM = 32/121)

Constants are organized in three strict tiers:

  TIER 0 — LOCKED STRUCTURAL: Exact values from geometry/number theory.
      These are mathematical identities. Changing any of them breaks
      the framework at the axiomatic level.
      Examples: A = 35/437, (Z,X,Y) = (2,3,6), delta_X = 5/19

  TIER 1 — EXACT DERIVED: Computed from Tier 0 by standard operations
      (exp, sqrt, division). No approximation involved.
      Examples: G_eff/G = 1/(1+A) = 437/472, H0_ratio = exp(A)

  TIER 2 — BENCHMARK PREDICTIONS: Approximate or phenomenological values
      that depend on slow-roll expansions, leading-order formulas, or
      definitions that may differ between bare/effective contexts.
      These are reference numbers for comparison, NOT authoritative inputs.
      Examples: n_s ~ 1-2/60, r ~ 0.0089

Runtime solver tolerances and engineering knobs must NOT be defined here.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Final, Tuple


@dataclass(frozen=True, slots=True)
class LockedConstant:
    """Immutable container for a theory-side constant."""
    name: str
    value: float
    exact: str
    note: str


# =====================================================================
# TIER 0 -- LOCKED STRUCTURAL (mathematical identities, zero freedom)
# =====================================================================

A_NUMERATOR: Final[int] = 35
A_DENOMINATOR: Final[int] = 437
A_FRACTION: Final[Fraction] = Fraction(A_NUMERATOR, A_DENOMINATOR)
A_LOCKED: Final[float] = float(A_FRACTION)

DIM_X: Final[int] = 3
DIM_Z: Final[int] = 2
DIM_Y: Final[int] = 6
Q_TOTAL: Final[int] = DIM_X + DIM_Z + DIM_Y
SECTOR_DIMS: Final[Tuple[int, int, int]] = (DIM_X, DIM_Z, DIM_Y)
SECTOR_NAMES: Final[Tuple[str, str, str]] = ("X", "Z", "Y")
G_MUB: Final[int] = Q_TOTAL + 1  # = 12 MUB(Q) [ZS-F5, PROVEN]

# Polyhedral invariants [ZS-F2, ZS-S1, PROVEN]
DELTA_X: Final[float] = 5.0 / 19.0
DELTA_Y: Final[float] = 7.0 / 23.0

# i-tetration fixed point z* = W0(-ln i)/(-ln i) [ZS-M1, PROVEN]
X_STAR: Final[float] = 0.4382829367270321
Z_STAR_IM: Final[float] = 0.3605924718713855
Z_STAR_MOD_SQ: Final[float] = X_STAR**2 + Z_STAR_IM**2

# Scalar field potential coupling [ZS-F1 S4.4]
LAMBDA_POTENTIAL: Final[float] = 1.79

# Tier 0 assertions
assert abs(DELTA_X * DELTA_Y - A_LOCKED) < 1e-15, "A != dX*dY"
assert Q_TOTAL == 11, "Q != 11"
assert DIM_X + DIM_Z + DIM_Y == Q_TOTAL, "Z+X+Y != Q"


# =====================================================================
# TIER 1 -- EXACT DERIVED (computed from Tier 0, no approximation)
# =====================================================================

KAPPA: Final[float] = math.sqrt(A_LOCKED / Q_TOTAL)
G_EFF_RATIO: Final[float] = 1.0 / (1.0 + A_LOCKED)       # 437/472
H0_RATIO: Final[float] = math.exp(A_LOCKED)                # exp(A)
H_ZS_OVER_H_GR: Final[float] = 1.0 / math.sqrt(1.0 + A_LOCKED)
M_EPSILON_OVER_MP: Final[float] = math.sqrt(LAMBDA_POTENTIAL)
TAU_D_OVER_TAU_PENROSE: Final[float] = 1.0 / A_LOCKED

# Sector counting — DERIVED from (Z,X,Y) = (2,3,6), Q=11
# v6.1: OMEGA_M_BARE/EFF now use face counting (38/121) as PRIMARY.
#        Slot counting (39/121) retained as _SLOT for historical reference.
OMEGA_M_BARE_SLOT: Final[float] = 39.0 / 121.0          # X(Z+Q)/Q^2 [DERIVED, slot — HISTORICAL]
OMEGA_M_BARE: Final[float] = 38.0 / 121.0               # face counting: F(cube)+F(trunc.icosa.)/Q^2 [v6.1, ZS-A5 v2.2.0]
OMEGA_M_EFF: Final[float] = OMEGA_M_BARE * G_EFF_RATIO  # 38/(121(1+A)) = 0.2908 [v6.1: was 0.2984]
OMEGA_B_BARE: Final[float] = 6.0 / 121.0                # XZ/Q^2 [ZS-A5]
OMEGA_B_EFF: Final[float] = OMEGA_B_BARE * G_EFF_RATIO
OMEGA_CDM_SLOT: Final[float] = 33.0 / 121.0             # X·Q/Q^2 = 33/121 [DERIVED, slot counting]
OMEGA_CDM_SLOT_EFF: Final[float] = OMEGA_CDM_SLOT * G_EFF_RATIO
ETA_B: Final[float] = (6.0 / 11.0) ** 35                # [ZS-M5]

assert abs(OMEGA_M_BARE - 38.0 / 121.0) < 1e-15, "OMEGA_M_BARE must be 38/121 (face counting)"
assert abs(OMEGA_M_EFF - 38.0 / (121.0 * (1.0 + A_LOCKED))) < 1e-15


# =====================================================================
# TIER 1c -- FACE COUNTING (Platonic solid faces)
#   STATUS: OBSERVATION (Cobaya-validated 2026-03-18, Δχ² = 3.9)
#   Requires theoretical derivation before upgrade to DERIVED.
# =====================================================================
#
# DISCOVERY (2026-03-18):
#   Planck ω_cdm h² = 0.1200 implies Ω_cdm = 32/121 exactly.
#   32 = F(truncated icosahedron) = F(dodecahedron) + F(icosahedron)
#      = 12 pentagonal faces + 20 hexagonal faces
#
#   In Z-Spin, the truncated icosahedron is the Y-sector mediation
#   polyhedron (ZS-F2): it mediates between dodecahedron ↔ icosahedron,
#   just as the truncated octahedron mediates cube ↔ octahedron
#   in the X-sector.
#
#   Physical interpretation:
#     Baryons (6):  cube faces → X-sector visible matter
#     CDM (32):     truncated icosahedron faces → Z-sector entanglement
#                   boundary tension projected onto X-sector as gravity
#     Dark energy (83): remaining background slots → expansion
#
#   Anti-numerology verification:
#     - n/121 scan: only n=32 within 1σ (1/120 = 0.8%)
#     - 500K random fractions: 0.0% better than 32/121
#     - 32 is NOT arbitrary: it is F(truncated icosahedron),
#       a mathematical theorem (Euler formula V-E+F=2)
#
#   Cobaya plik_lite results (H₀=67.36, n_s=0.9674):
#     Ω_cdm = 33/121 (slot) → Δχ² = 226  FAIL
#     Ω_cdm = 32/121 (face) → Δχ² = 3.9  PASS
#
# Polyhedral face counts (Platonic solids):
F_TETRAHEDRON: Final[int] = 4                               # Z-sector (self-dual)
F_CUBE: Final[int] = 6                                      # X-sector
F_OCTAHEDRON: Final[int] = 8                                # X-sector (dual of cube)
F_DODECAHEDRON: Final[int] = 12                             # Y-sector
F_ICOSAHEDRON: Final[int] = 20                              # Y-sector (dual of dodec.)
F_TRUNCATED_ICOSAHEDRON: Final[int] = F_DODECAHEDRON + F_ICOSAHEDRON  # = 32

# Face-counted matter fractions [OBSERVATION — pending derivation]
OMEGA_B_FACE: Final[float] = float(F_CUBE) / float(Q_TOTAL**2)       # 6/121
OMEGA_CDM_FACE: Final[float] = float(F_TRUNCATED_ICOSAHEDRON) / float(Q_TOTAL**2)  # 32/121
OMEGA_M_FACE: Final[float] = OMEGA_B_FACE + OMEGA_CDM_FACE           # 38/121
OMEGA_LAMBDA_FACE: Final[float] = 1.0 - OMEGA_M_FACE                 # 83/121

# Consistency checks
assert OMEGA_B_FACE == OMEGA_B_BARE, "baryon face count must equal slot count"
assert F_TRUNCATED_ICOSAHEDRON == 32, "truncated icosahedron has 32 faces"
assert abs(OMEGA_M_FACE - 38.0 / 121.0) < 1e-15

# Backward compat: CDM bare/eff now point to FACE values for CMB pipeline
OMEGA_CDM_BARE: Final[float] = OMEGA_CDM_FACE                # 32/121 [OBSERVATION]
OMEGA_CDM_EFF: Final[float] = OMEGA_CDM_FACE * G_EFF_RATIO   # 32/(121(1+A))


# =====================================================================
# TIER 1b -- CMB PARAMETER MAPPING (Cobaya Tier-0.9, 2026-03-18)
# =====================================================================
#
# Uses FACE counting (Tier 1c) for matter fractions.
# H₀_CMB = 67.36 (Planck, unchanged by Z-Spin).
# H₀_local = exp(A) × H₀_CMB = 72.98 (SH0ES: 73.04 ± 1.04, 0.06σ).
#
# Baryon ω_b: bare (particle count, no G_eff)
# CDM ω_cdm: bare face count (32/121 × h², no G_eff needed — face
#            counting already gives the physical projection)
#
# Cobaya validation (Planck plik_lite TTTEEE):
#   38/121 face counting → Δχ² = 3.9  (PASS, best result)
#   39/121 slot counting → Δχ² = 226  (FAIL)
#
CMB_H0: Final[float] = 67.36                               # km/s/Mpc [Planck 2018]
CMB_H: Final[float] = CMB_H0 / 100.0                       # dimensionless h
CMB_OMBH2: Final[float] = OMEGA_B_FACE * CMB_H**2           # 6/121 × h² = 0.02250
CMB_OMCH2: Final[float] = OMEGA_CDM_FACE * CMB_H**2         # 32/121 × h² = 0.12000
CMB_NS: Final[float] = 0.9674                               # Paper 18 canonical inflation
CMB_H0_LOCAL: Final[float] = CMB_H0 * H0_RATIO             # exp(A) × 67.36 = 72.98

# Cobaya validation results (2026-03-18)
TIER09_DCHI2_FACE: Final[float] = 3.9                       # 38/121 face counting
TIER09_DCHI2_SLOT: Final[float] = 226.0                     # 39/121 slot counting
TIER09_DCHI2_MCMC: Final[float] = 8.4                       # Path C MCMC


# =====================================================================
# TIER 2 -- BENCHMARK PREDICTIONS (approximate / leading-order)
# WARNING: reference numbers, NOT authoritative simulation inputs.
# =====================================================================

BENCH_NS_60: Final[float] = 1.0 - 2.0 / 60.0    # leading-order Starobinsky
BENCH_NS_55: Final[float] = 1.0 - 2.0 / 55.0
BENCH_R_TENSOR: Final[float] = 0.0089             # book Chapter 9 table

PLANCK_OMEGA_M: Final[float] = 0.3153
PLANCK_H0: Final[float] = 67.36
PLANCK_SIGMA8: Final[float] = 0.8111
PLANCK_NS: Final[float] = 0.9649


# =====================================================================
# Registry + utilities
# =====================================================================

LOCKED_CONSTANTS: Final[dict[str, LockedConstant]] = {
    "A": LockedConstant(name="A", value=A_LOCKED,
        exact=f"{A_NUMERATOR}/{A_DENOMINATOR}", note="Tier 0"),
    "DIM_X": LockedConstant(name="DIM_X", value=float(DIM_X),
        exact=str(DIM_X), note="Tier 0"),
    "DIM_Z": LockedConstant(name="DIM_Z", value=float(DIM_Z),
        exact=str(DIM_Z), note="Tier 0"),
    "DIM_Y": LockedConstant(name="DIM_Y", value=float(DIM_Y),
        exact=str(DIM_Y), note="Tier 0"),
    "Q_TOTAL": LockedConstant(name="Q_TOTAL", value=float(Q_TOTAL),
        exact=str(Q_TOTAL), note="Tier 0"),
}

def get_sector_dims() -> dict[str, int]:
    """Return sector dimensions as a new mapping."""
    return {"X": DIM_X, "Z": DIM_Z, "Y": DIM_Y}

# Backward compatibility aliases (v3.0 names -> v3.1 names)
N_S_60 = BENCH_NS_60
N_S_55 = BENCH_NS_55
R_TENSOR = BENCH_R_TENSOR
OMEGA_B = OMEGA_B_BARE
TIER09_DCHI2 = TIER09_DCHI2_FACE   # best result uses face counting

__all__ = [
    "LockedConstant", "A_NUMERATOR", "A_DENOMINATOR", "A_FRACTION", "A_LOCKED",
    "DIM_X", "DIM_Z", "DIM_Y", "Q_TOTAL", "G_MUB",
    "SECTOR_DIMS", "SECTOR_NAMES", "LOCKED_CONSTANTS", "get_sector_dims",
    "DELTA_X", "DELTA_Y", "X_STAR", "Z_STAR_IM", "Z_STAR_MOD_SQ",
    "LAMBDA_POTENTIAL",
    "KAPPA", "G_EFF_RATIO", "H0_RATIO", "H_ZS_OVER_H_GR",
    "M_EPSILON_OVER_MP", "TAU_D_OVER_TAU_PENROSE",
    # Slot counting (DERIVED, Tier 1) — historical
    "OMEGA_M_BARE", "OMEGA_M_BARE_SLOT", "OMEGA_M_EFF", "OMEGA_B_BARE", "OMEGA_B_EFF",
    "OMEGA_CDM_SLOT", "OMEGA_CDM_SLOT_EFF", "ETA_B",
    # Face counting (OBSERVATION, Tier 1c) — Cobaya-validated
    "F_TETRAHEDRON", "F_CUBE", "F_OCTAHEDRON", "F_DODECAHEDRON",
    "F_ICOSAHEDRON", "F_TRUNCATED_ICOSAHEDRON",
    "OMEGA_B_FACE", "OMEGA_CDM_FACE", "OMEGA_M_FACE", "OMEGA_LAMBDA_FACE",
    "OMEGA_CDM_BARE", "OMEGA_CDM_EFF",
    # CMB pipeline
    "CMB_H0", "CMB_H", "CMB_OMBH2", "CMB_OMCH2", "CMB_NS", "CMB_H0_LOCAL",
    "TIER09_DCHI2", "TIER09_DCHI2_FACE", "TIER09_DCHI2_SLOT", "TIER09_DCHI2_MCMC",
    # Benchmarks
    "BENCH_NS_60", "BENCH_NS_55", "BENCH_R_TENSOR",
    "PLANCK_OMEGA_M", "PLANCK_H0", "PLANCK_SIGMA8", "PLANCK_NS",
    "N_S_60", "N_S_55", "R_TENSOR", "OMEGA_B",
]
