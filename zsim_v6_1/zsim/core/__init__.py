"""Core package exports for Z-Sim v3.1."""

from .constants import (
    # Tier 0 -- Locked Structural
    A_DENOMINATOR, A_FRACTION, A_LOCKED, A_NUMERATOR,
    DIM_X, DIM_Y, DIM_Z, Q_TOTAL, G_MUB,
    SECTOR_DIMS, SECTOR_NAMES, LOCKED_CONSTANTS, get_sector_dims,
    DELTA_X, DELTA_Y, X_STAR, Z_STAR_IM, Z_STAR_MOD_SQ,
    LAMBDA_POTENTIAL,
    # Tier 1 -- Exact Derived
    KAPPA, G_EFF_RATIO, H0_RATIO, H_ZS_OVER_H_GR,
    M_EPSILON_OVER_MP, TAU_D_OVER_TAU_PENROSE,
    OMEGA_M_BARE, OMEGA_M_EFF, OMEGA_B_BARE, OMEGA_B_EFF, ETA_B,
    # Tier 2 -- Benchmark Predictions
    BENCH_NS_60, BENCH_NS_55, BENCH_R_TENSOR,
    PLANCK_OMEGA_M, PLANCK_H0, PLANCK_SIGMA8, PLANCK_NS,
    # Backward compat
    N_S_60, N_S_55, R_TENSOR, OMEGA_B,
)
from .exceptions import (
    ConfigLoadError,
    ConfigValidationError,
    IntegrationError,
    StateSerializationError,
    StateValidationError,
    ZSimError,
)
from .state import STATE_VECTOR_FIELDS, ZSimState

from .config import (
    ClosureConfig,
    InitialConfig,
    ModelConfig,
    OutputConfig,
    SolverConfig,
    ZSimConfig,
)

from .labels import (
    EpistemicOverclaimError,
    LabeledValue,
    Status,
    UnknownStatusError,
    assert_status_not_overclaimed,
    ensure_minimum_status,
    status_rank,
)

__all__ = [
    "A_NUMERATOR", "A_DENOMINATOR", "A_FRACTION", "A_LOCKED",
    "DIM_X", "DIM_Z", "DIM_Y", "Q_TOTAL", "G_MUB",
    "SECTOR_DIMS", "SECTOR_NAMES", "LOCKED_CONSTANTS", "get_sector_dims",
    "DELTA_X", "DELTA_Y", "X_STAR", "Z_STAR_IM", "Z_STAR_MOD_SQ",
    "LAMBDA_POTENTIAL",
    "KAPPA", "G_EFF_RATIO", "H0_RATIO", "H_ZS_OVER_H_GR",
    "M_EPSILON_OVER_MP", "TAU_D_OVER_TAU_PENROSE",
    "OMEGA_M_BARE", "OMEGA_M_EFF", "OMEGA_B_BARE", "OMEGA_B_EFF", "ETA_B",
    "BENCH_NS_60", "BENCH_NS_55", "BENCH_R_TENSOR",
    "PLANCK_OMEGA_M", "PLANCK_H0", "PLANCK_SIGMA8", "PLANCK_NS",
    "N_S_60", "N_S_55", "R_TENSOR", "OMEGA_B",
    "Status", "LabeledValue", "EpistemicOverclaimError", "UnknownStatusError",
    "status_rank", "assert_status_not_overclaimed", "ensure_minimum_status",
    "ZSimError", "StateValidationError", "StateSerializationError",
    "ConfigLoadError", "ConfigValidationError", "IntegrationError",
    "STATE_VECTOR_FIELDS", "ZSimState",
    "ClosureConfig", "InitialConfig", "ModelConfig", "OutputConfig",
    "SolverConfig", "ZSimConfig",
]
