"""Structural operators for Z-Sim v1.0.

The engine does not use a full dense field operator. Instead, it keeps a small
block-structured surrogate consistent with the X-Z-Y partition:

    [ L_XX  C_XZ   0  ]
    [ C_ZX  L_ZZ  C_ZY]
    [  0    C_YZ  L_YY]

The direct X-Y block is identically zero. A reduced transfer proxy is also
provided so validation can check the effective X↔Y rank ceiling.
"""

from __future__ import annotations

import numpy as np

from zsim.core import A_LOCKED, DIM_X, DIM_Y, DIM_Z, ZSimConfig, ZSimState


_DEF_LX = 1.0 + A_LOCKED
_DEF_LZ = 1.0
_DEF_LY = 1.0 - A_LOCKED / 2.0



def build_structural_operator(config: ZSimConfig) -> np.ndarray:
    """Build a small dense structural surrogate with explicit block form."""
    q = DIM_X + DIM_Z + DIM_Y
    op = np.zeros((q, q), dtype=float)

    # Diagonal self blocks.
    op[:DIM_X, :DIM_X] = np.eye(DIM_X) * _DEF_LX
    op[DIM_X:DIM_X + DIM_Z, DIM_X:DIM_X + DIM_Z] = np.eye(DIM_Z) * _DEF_LZ
    op[DIM_X + DIM_Z:, DIM_X + DIM_Z:] = np.eye(DIM_Y) * _DEF_LY

    # Symmetric X↔Z couplings.
    c_xz = np.array(
        [
            [config.closure.gamma_xz, 0.0],
            [0.0, config.closure.gamma_xz],
            [config.closure.gamma_xz / 2.0, config.closure.gamma_xz / 2.0],
        ],
        dtype=float,
    )
    op[:DIM_X, DIM_X:DIM_X + DIM_Z] = c_xz
    op[DIM_X:DIM_X + DIM_Z, :DIM_X] = c_xz.T

    # Symmetric Z↔Y couplings.
    c_zy = np.array(
        [
            [config.closure.gamma_zy, 0.0, config.closure.gamma_zy / 2.0, 0.0, config.closure.gamma_zy / 2.0, 0.0],
            [0.0, config.closure.gamma_zy, 0.0, config.closure.gamma_zy / 2.0, 0.0, config.closure.gamma_zy / 2.0],
        ],
        dtype=float,
    )
    op[DIM_X:DIM_X + DIM_Z, DIM_X + DIM_Z:] = c_zy
    op[DIM_X + DIM_Z:, DIM_X:DIM_X + DIM_Z] = c_zy.T

    # Direct X↔Y block intentionally left at zero.
    return op



def build_transfer_proxy(state: ZSimState, config: ZSimConfig) -> np.ndarray:
    """Build an effective X↔Y transfer proxy factorized through Z.

    The proxy is constructed as an outer-product sum over the two Z channels,
    which guarantees rank <= DIM_Z unless modified illegally.
    """
    gate = 1.0 if config.closure.phase_mode == "constant" else np.tanh(state.phi_z)

    vx = np.array(
        [
            [state.rho_x, 0.0],
            [0.0, state.rho_z + 1.0],
            [0.5 * (state.rho_x + state.rho_z), 0.5 * gate],
        ],
        dtype=float,
    )
    vy = np.array(
        [
            [state.rho_z + 1.0, 0.0],
            [0.0, state.rho_y + 1.0],
            [0.5 * (state.rho_z + state.rho_y), 0.0],
            [0.0, 0.5 * (state.rho_z + state.rho_y)],
            [state.J_xz - state.J_zy, 0.0],
            [0.0, gate],
        ],
        dtype=float,
    )
    scale = np.diag([config.closure.gamma_xz, config.closure.gamma_zy])
    return vx @ scale @ vy.T



def effective_rank_xy(state: ZSimState, config: ZSimConfig, *, tol: float = 1e-10) -> int:
    """Return numerical matrix rank of the reduced X↔Y transfer proxy."""
    proxy = build_transfer_proxy(state, config)
    return int(np.linalg.matrix_rank(proxy, tol=tol))



def direct_xy_block(operator: np.ndarray) -> np.ndarray:
    """Extract the direct X↔Y block from a structural operator."""
    return operator[:DIM_X, DIM_X + DIM_Z:]


__all__ = [
    "build_structural_operator",
    "build_transfer_proxy",
    "effective_rank_xy",
    "direct_xy_block",
]
