"""Locked structural constants for Z-Sim v1.0.

v1.0 changes (2026-03-21):
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
# v1.0: OMEGA_M_BARE/EFF now use face counting (38/121) as PRIMARY.
#        Slot counting (39/121) retained as _SLOT for historical reference.
OMEGA_M_BARE_SLOT: Final[float] = 39.0 / 121.0          # X(Z+Q)/Q^2 [DERIVED, slot — HISTORICAL]
OMEGA_M_BARE: Final[float] = 38.0 / 121.0               # face counting: F(cube)+F(trunc.icosa.)/Q^2 [v1.0, ZS-A5 v2.2.0]
OMEGA_M_EFF: Final[float] = OMEGA_M_BARE * G_EFF_RATIO  # 38/(121(1+A)) = 0.2908 [v1.0: was 0.2984]
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

# ── Archimedean solid invariants (V, E, F) [PROVEN, Euler V-E+F=2] ──
# Truncated Octahedron (TO) — X-sector mediation polyhedron [ZS-F2, ZS-S1]
V_TO: Final[int] = 24                                       # vertices
E_TO: Final[int] = 36                                       # edges
F_TO: Final[int] = 14                                       # faces (8 hex + 6 sq)
VF_TO: Final[int] = V_TO + F_TO                             # = 38 [Mode-Count Collapse]
VEF_TO: Final[int] = V_TO + E_TO + F_TO                    # = 74

# Truncated Icosahedron (TI) — Y-sector mediation polyhedron [ZS-F2, ZS-S1]
V_TI: Final[int] = 60                                       # vertices
E_TI: Final[int] = 90                                       # edges
F_TI: Final[int] = 32                                       # faces (12 pent + 20 hex)
VF_TI: Final[int] = V_TI + F_TI                             # = 92 [Mode-Count Collapse]
VEF_TI: Final[int] = V_TI + E_TI + F_TI                    # = 182

# Symmetry group orders [PROVEN]
ORDER_O_H: Final[int] = 48                                  # |O_h| = full octahedral
ORDER_I: Final[int] = 60                                    # |I| = icosahedral rotation ≅ A₅
ORDER_I_H: Final[int] = 120                                 # |I_h| = full icosahedral

# Z-sector Schur complement: zeroth Betti number [ZS-S1 §5, PROVEN]
BETA0_Z: Final[int] = 1                                     # β₀(Z) = connected component mode

# Euler formula consistency assertions
assert V_TO - E_TO + F_TO == 2, "TO Euler formula fails"
assert V_TI - E_TI + F_TI == 2, "TI Euler formula fails"
assert VF_TO == 38, "TO V+F != 38"
assert VF_TI == 92, "TI V+F != 92"
assert ORDER_I == V_TI, "|I| must equal V(TI) = 60"

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
# TIER 1d -- STANDARD MODEL GAUGE COUPLINGS (v1.0, ZS-S1/M8/M9)
#   All derived from polyhedral invariants + i-tetration fixed point.
#   Zero free parameters beyond A = 35/437.
# =====================================================================

# ── Gauge coupling building blocks [PROVEN] ──
N_EFF_Y: Final[int] = VF_TI + BETA0_Z                      # 92 + 1 = 93 [Schur complement]
HALF_VEF_TI: Final[int] = VEF_TI // 2                      # 182/2 = 91 [Z₂ reduction]
TWICE_V_TO: Final[int] = 2 * V_TO                           # 2 × 24 = 48 = |O_h|

# ── Strong coupling α_s [ZS-S1 §8.1, DERIVED] ──
# α_s = Q / [(V+F)_Y + β₀(Z)] = 11/93
ALPHA_S_FRAC: Final[Fraction] = Fraction(Q_TOTAL, N_EFF_Y)  # 11/93
ALPHA_S: Final[float] = float(ALPHA_S_FRAC)                 # 0.11828
# PDG 2024: α_s(M_Z) = 0.1180 ± 0.0009, pull = +0.31σ

# ── Weinberg angle sin²θ_W [ZS-S1 §8.2, DERIVED] ──
# sin²θ_W = (2V_X / ((V+E+F)_Y/2)) × x* = (48/91) × x*
R_GEOM: Final[float] = float(TWICE_V_TO) / float(HALF_VEF_TI)  # 48/91
SIN2_THETA_W: Final[float] = R_GEOM * X_STAR                    # 0.23118
# PDG 2024: sin²θ_W(M_Z) = 0.23122 ± 0.00003, pull = −1.26σ

# ── Electromagnetic coupling α₂ [ZS-S1 §8.3, DERIVED] ──
# α₂ = Y / (5 × (V+F)_X) = 6/190 = 3/95
ALPHA_2_FRAC: Final[Fraction] = Fraction(DIM_Y, 5 * VF_TO)  # 6/190 = 3/95
ALPHA_2: Final[float] = float(ALPHA_2_FRAC)                  # 0.031579
# Factor 5 = |I_h|/|O_h| = 120/24 [PROVEN, two independent routes]

# ── β-function coefficients [ZS-S1 §7, PROVEN] ──
# a₂ = (V+F)_X / G = 38/12 = 19/6 [SU(2)]
# a₃ = (V+F)_Y / G = 92/12 = 23/3 [SU(3)]
BETA_COEFF_SU2_FRAC: Final[Fraction] = Fraction(VF_TO, G_MUB)   # 19/6
BETA_COEFF_SU3_FRAC: Final[Fraction] = Fraction(VF_TI, G_MUB)   # 23/3
BETA_COEFF_SU2: Final[float] = float(BETA_COEFF_SU2_FRAC)
BETA_COEFF_SU3: Final[float] = float(BETA_COEFF_SU3_FRAC)
BETA_SLOPE_RATIO: Final[float] = BETA_COEFF_SU3 / BETA_COEFF_SU2  # 46/19

# ── Fine structure constant α_EM NLO [ZS-M8 §3, HYPOTHESIS (strong)] ──
# κ² = A/Q = 35/4807, c₄ = |V−F|_Y / [(V+F)_Y − β₀(Z)] = 28/91 = 4/13
KAPPA_SQ: Final[float] = A_LOCKED / Q_TOTAL                          # 35/4807
C4_NLO_FRAC: Final[Fraction] = Fraction(abs(V_TI - F_TI),
                                         VF_TI - BETA0_Z)            # 28/91 = 4/13
C4_NLO: Final[float] = float(C4_NLO_FRAC)                           # 0.30769
ALPHA_EM_NLO: Final[float] = KAPPA_SQ + C4_NLO * KAPPA_SQ**2        # ≈ 1/137.036
ALPHA_EM_INV_NLO: Final[float] = 1.0 / ALPHA_EM_NLO                 # 137.036
# CODATA 2022: 1/α = 137.035999, deviation = 1.07 ppm

# SM gauge coupling assertions
assert abs(ALPHA_S - 11.0 / 93.0) < 1e-15, "α_s != 11/93"
assert abs(R_GEOM - 48.0 / 91.0) < 1e-15, "R_geom != 48/91"
assert TWICE_V_TO == ORDER_O_H, "2V_X must equal |O_h|"
assert C4_NLO_FRAC == Fraction(4, 13), "c₄ != 4/13"
assert BETA_COEFF_SU2_FRAC == Fraction(19, 6), "a₂ != 19/6"
assert BETA_COEFF_SU3_FRAC == Fraction(23, 3), "a₃ != 23/3"


# =====================================================================
# TIER 1e -- ELECTROWEAK SYMMETRY BREAKING (v1.0, ZS-S4 v6.3.0)
#   Higgs VEV from Factorized Determinant Theorem.
#   Zero free parameters.
# =====================================================================

# ── Effective compact dimension [PROVEN, three independent routes] ──
D_EFF: Final[int] = DIM_X + DIM_Y                           # Q − Z = 9

# ── Coleman-Weinberg exponent [ZS-S4 §6.12, DERIVED] ──
# γ_CW = (V+F)_X / d_eff = 38/9
GAMMA_CW_FRAC: Final[Fraction] = Fraction(VF_TO, D_EFF)     # 38/9
GAMMA_CW: Final[float] = float(GAMMA_CW_FRAC)               # 4.2222...

# ── Y-sector spectral cost [ZS-S4 §6.12, DERIVED] ──
# C_M^sp = ln(Z^Q × X) = Q·ln(Z) + ln(X)
# From ZS-Q3 PROVEN spectrum: λ=8(×3), λ=12(×1); 8=Z³, 12=Z²X
C_M_SPECTRAL: Final[float] = Q_TOTAL * math.log(DIM_Z) + math.log(DIM_X)  # 8.7232

# ── Higgs VEV [ZS-S4 v6.3.0, DERIVED] ──
# v = M_P × exp(−γ_CW × C_M^sp)
# = M_P × 2^{−418/9} × 3^{−38/9}
M_PLANCK_GEV: Final[float] = 2.435e18                       # reduced Planck mass [GeV]
HIGGS_VEV_EXPONENT: Final[float] = -GAMMA_CW * C_M_SPECTRAL # −36.853
HIGGS_VEV: Final[float] = M_PLANCK_GEV * math.exp(HIGGS_VEV_EXPONENT)  # 245.93 GeV
# Observed: 246.22 GeV, deviation = 0.12%

# ── Top quark mass prediction [ZS-S4 §6.10, TESTABLE] ──
# Path B: λ(Λ_comp) = 0 + SM RG → m_t = 171.5 ± 0.5 GeV
TOP_MASS_PRED: Final[float] = 171.5                          # GeV [TESTABLE, FCC-ee ~2040]
# PDG 2024: m_t = 172.57 ± 0.29 GeV

# ── Higgs mass hypothesis [HYPOTHESIS] ──
# m_H = v/Z × √(1+A/Z)
HIGGS_MASS_HYPO: Final[float] = HIGGS_VEV / DIM_Z * math.sqrt(1.0 + A_LOCKED / DIM_Z)
# ≈ 125.9 GeV  (observed 125.25 ± 0.17 GeV)

# EWSB assertions
assert D_EFF == 9, "d_eff != 9"
assert GAMMA_CW_FRAC == Fraction(38, 9), "γ_CW != 38/9"
assert abs(HIGGS_VEV - 245.93) < 0.1, f"Higgs VEV too far: {HIGGS_VEV:.2f}"


# =====================================================================
# TIER 1f -- NEUTRINO SECTOR (v1.0, ZS-S2 v1.0)
#   Type-I seesaw from geometric Dirac mass.
#   Zero free parameters.
# =====================================================================

# ── Dirac mass [ZS-S2, DERIVED] ──
M_ELECTRON_KEV: Final[float] = 510.999                      # keV [CODATA]
M_D_NEUTRINO_KEV: Final[float] = M_ELECTRON_KEV * A_LOCKED  # m_e × A = 40.93 keV

# ── Heavy neutral lepton [ZS-S2, DERIVED] ──
# Lightest neutrino mass ~ 0.05 eV (normal ordering)
M_NU_LIGHTEST_EV: Final[float] = 0.05                       # eV [NuFIT, approximate]
M_R_HNL_GEV: Final[float] = (M_D_NEUTRINO_KEV * 1e-6)**2 / (M_NU_LIGHTEST_EV * 1e-9)  # ≈ 33.5 GeV

# ── Seesaw mixing [ZS-S2, DERIVED] ──
THETA_SQ_SEESAW: Final[float] = (M_D_NEUTRINO_KEV * 1e-6)**2 / (M_R_HNL_GEV)**2  # ≈ 1.49e-12

# ── Baryon asymmetry [ZS-M5, DERIVED] ──
# η_B = (6/11)^35 = (X·Z/Q)^A_num
ETA_B_EXACT: Final[float] = (float(DIM_X * DIM_Z) / float(Q_TOTAL))**A_NUMERATOR


# =====================================================================
# TIER 1g -- AUTO-SURGERY & SINGULARITY RESOLUTION (v1.0, ZS-M12 v1.0)
#   Flow dynamics from Z-sector transfer map T(z) = iz.
#   Topological cap resolves curvature singularity.
#   Zero free parameters.
# =====================================================================

# ── Topological cap [ZS-M12 §5, DERIVED] ──
# Ω² = 1 + A·η_topo where η_topo = |z*|²
OMEGA_CAP_SQ: Final[float] = 1.0 + A_LOCKED * Z_STAR_MOD_SQ  # = 1.0258

# ── Flow attractor [ZS-M12 §3, DERIVED] ──
# Half-life of z* damped spiral (in Planck time units)
FLOW_HALF_LIFE_TP: Final[float] = 0.44

# ── Centrifugal barrier [ZS-M12 §9, DERIVED-CONDITIONAL] ──
# ε_min ≈ 30.7 ≫ ε_sr = 2.64 (prevents field from reaching ε=0 at bounce)
# Contingent on V1 (Planck-bulk matching, OPEN)
EPSILON_MIN_BARRIER: Final[float] = 30.7

# ── Critical temperature [ZS-M12 §8, DERIVED] ──
# T_c ≈ T_reh ≈ 2.48×10¹⁵ GeV (cyclic self-consistency with ZS-U2)
T_C_SYMMETRY_GEV: Final[float] = 2.48e15


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

# PDG 2024 reference values for SM parameters
PDG_ALPHA_S: Final[float] = 0.1180                # ± 0.0009 [MS-bar, M_Z]
PDG_ALPHA_S_ERR: Final[float] = 0.0009
PDG_SIN2_THETA_W: Final[float] = 0.23122          # ± 0.00003 [MS-bar, M_Z]
PDG_SIN2_THETA_W_ERR: Final[float] = 0.00003
PDG_ALPHA_EM_INV: Final[float] = 137.035999        # CODATA 2022
PDG_HIGGS_VEV: Final[float] = 246.22              # GeV
PDG_HIGGS_MASS: Final[float] = 125.25             # ± 0.17 GeV
PDG_TOP_MASS: Final[float] = 172.57               # ± 0.29 GeV
PDG_TOP_MASS_ERR: Final[float] = 0.29
PDG_M_TAU_OVER_M_MU: Final[float] = 16.817        # mτ/mμ
PDG_M_TAU_OVER_M_E: Final[float] = 3477.2         # mτ/me
PDG_CABIBBO_DEG: Final[float] = 13.04             # degrees


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

# Backward compatibility aliases (legacy names → v1.0 names)
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
    # Archimedean solid invariants (Tier 0, v1.0)
    "V_TO", "E_TO", "F_TO", "VF_TO", "VEF_TO",
    "V_TI", "E_TI", "F_TI", "VF_TI", "VEF_TI",
    "ORDER_O_H", "ORDER_I", "ORDER_I_H", "BETA0_Z",
    # SM gauge couplings (Tier 1d, v1.0)
    "N_EFF_Y", "HALF_VEF_TI", "TWICE_V_TO",
    "ALPHA_S_FRAC", "ALPHA_S",
    "R_GEOM", "SIN2_THETA_W",
    "ALPHA_2_FRAC", "ALPHA_2",
    "BETA_COEFF_SU2_FRAC", "BETA_COEFF_SU3_FRAC",
    "BETA_COEFF_SU2", "BETA_COEFF_SU3", "BETA_SLOPE_RATIO",
    "KAPPA_SQ", "C4_NLO_FRAC", "C4_NLO", "ALPHA_EM_NLO", "ALPHA_EM_INV_NLO",
    # EWSB (Tier 1e, v1.0)
    "D_EFF", "GAMMA_CW_FRAC", "GAMMA_CW", "C_M_SPECTRAL",
    "M_PLANCK_GEV", "HIGGS_VEV_EXPONENT", "HIGGS_VEV",
    "TOP_MASS_PRED", "HIGGS_MASS_HYPO",
    # Neutrino sector (Tier 1f, v1.0)
    "M_ELECTRON_KEV", "M_D_NEUTRINO_KEV", "M_R_HNL_GEV",
    "THETA_SQ_SEESAW", "ETA_B_EXACT",
    # Auto-Surgery (Tier 1g, v1.0, ZS-M12)
    "OMEGA_CAP_SQ", "FLOW_HALF_LIFE_TP", "EPSILON_MIN_BARRIER", "T_C_SYMMETRY_GEV",
    # CMB pipeline
    "CMB_H0", "CMB_H", "CMB_OMBH2", "CMB_OMCH2", "CMB_NS", "CMB_H0_LOCAL",
    "TIER09_DCHI2", "TIER09_DCHI2_FACE", "TIER09_DCHI2_SLOT", "TIER09_DCHI2_MCMC",
    # Benchmarks & PDG references
    "BENCH_NS_60", "BENCH_NS_55", "BENCH_R_TENSOR",
    "PLANCK_OMEGA_M", "PLANCK_H0", "PLANCK_SIGMA8", "PLANCK_NS",
    "PDG_ALPHA_S", "PDG_ALPHA_S_ERR", "PDG_SIN2_THETA_W", "PDG_SIN2_THETA_W_ERR",
    "PDG_ALPHA_EM_INV", "PDG_HIGGS_VEV", "PDG_HIGGS_MASS",
    "PDG_TOP_MASS", "PDG_TOP_MASS_ERR",
    "PDG_M_TAU_OVER_M_MU", "PDG_M_TAU_OVER_M_E", "PDG_CABIBBO_DEG",
    "N_S_60", "N_S_55", "R_TENSOR", "OMEGA_B",
]
