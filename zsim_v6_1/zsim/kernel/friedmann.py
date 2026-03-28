"""Z-Sim v3.0 — Modified Friedmann Equation [CRITICAL]

Source: ZS-F1 §3, Paper 22 §2.1, Paper 24 §5.1
Status: DERIVED from the Z-Spin action

THE SINGLE MOST IMPORTANT MODULE IN Z-SIM.
Without (1+Aε²), this is not a Z-Spin simulator.

The full modified Friedmann equation from the Z-Spin scalar-tensor action:

    S = ∫d⁴x √(−g) [(1 + Aε²)R/2 − (∂ε)²/2 − (λ/4)(ε² − 1)²]

Variation → modified Friedmann:

    3 H² F(ε) = ρ_total + ½(dε/dt)² + V(ε) − 6AHε(dε/dt)

where F(ε) = 1 + Aε² is the non-minimal coupling function.
"""

from __future__ import annotations

import math
from dataclasses import replace

from zsim.core import A_LOCKED, ZSimConfig, ZSimState
from zsim.core.constants import LAMBDA_POTENTIAL
from zsim.core.exceptions import StateValidationError

from .epsilon import epsilon_potential


# ─── Non-minimal coupling functions ──────────────────────────────────

def F_epsilon(epsilon: float, A: float = A_LOCKED) -> float:
    """Non-minimal coupling function F(ε) = 1 + Aε².

    [STATUS: PROVEN — direct from action ZS-F1]
    """
    return 1.0 + A * epsilon * epsilon


def G_eff_over_G(epsilon: float, A: float = A_LOCKED) -> float:
    """Effective Newton constant ratio: G_eff/G = 1/F(ε) = 1/(1+Aε²).

    At attractor ε=1: G_eff = G/(1+A) = 437/472 G.
    [STATUS: DERIVED — ZS-F1, ZS-A2]
    """
    return 1.0 / F_epsilon(epsilon, A)


# ─── Potential functions ─────────────────────────────────────────────

def V_epsilon(epsilon: float, lam: float = LAMBDA_POTENTIAL) -> float:
    """Quartic potential V(ε) = (λ/4)(ε² − 1)².

    [STATUS: DERIVED — ZS-F1 §4]
    """
    return 0.25 * lam * (epsilon * epsilon - 1.0) ** 2


def dV_depsilon(epsilon: float, lam: float = LAMBDA_POTENTIAL) -> float:
    """dV/dε = λ ε (ε² − 1).

    [STATUS: DERIVED — ZS-F1 §4]
    """
    return lam * epsilon * (epsilon * epsilon - 1.0)


# ─── Modified Friedmann equation ─────────────────────────────────────

def friedmann_h_squared(state: ZSimState, config: ZSimConfig) -> float:
    """Modified Friedmann equation from the Z-Spin action.

    In e-fold time N = ln(a), with π_ε = dε/dN:

        H² [3 F(ε) - ½π_ε² + 6Aε π_ε] = ρ_total + V(ε)

    Source: ZS-F1 §3 variation of action.
    [STATUS: DERIVED]
    """
    A = config.model.A
    eps = state.epsilon
    pi_e = state.pi_epsilon
    lam = config.closure.lam

    F_e = F_epsilon(eps, A)
    V_e = V_epsilon(eps, lam)
    rho_tot = state.rho_total

    # Effective coefficient of H² on LHS
    coeff_h2 = 3.0 * F_e - 0.5 * pi_e * pi_e + 6.0 * A * eps * pi_e

    if coeff_h2 <= 0:
        return 0.0  # Will be caught by KS-4

    return (rho_tot + V_e) / coeff_h2


def friedmann_h(state: ZSimState, config: ZSimConfig) -> float:
    """Compute H from the full modified Friedmann equation.

    Returns h = H/H_ref (dimensionless).
    Uses the complete non-minimal coupling F(ε) = 1 + Aε².
    """
    h_sq = friedmann_h_squared(state, config)
    if h_sq < 0:
        return 0.0
    return math.sqrt(h_sq)


# ─── Non-minimal coupling verification (KS-6) ───────────────────────

class MissingNonMinimalCoupling(StateValidationError):
    """Raised when the non-minimal coupling F(ε) = 1+Aε² is absent."""
    pass


def verify_non_minimal_coupling(config: ZSimConfig) -> None:
    """KS-6: Verify that the Friedmann equation includes (1+Aε²).

    Correct test: compute h² with real A vs A→0 at SAME ε.
    At ε=1, π_ε=0, V(1)=0:
        h²(A)   = ρ / [3(1+A)]
        h²(A=0) = ρ / 3
    Ratio = 1/(1+A) exactly.
    """
    state = ZSimState(
        N=0, a=1, h=1, epsilon=1.0, pi_epsilon=0,
        rho_x=0.3, rho_z=0.02, rho_y=0.68,
        J_xz=0, J_zy=0, phi_z=0, sigma_struct=0,
    )

    h2_real = friedmann_h_squared(state, config)

    # Create config with A=0 using immutable replace
    model_zero = replace(config.model, A=0.0)
    cfg_zero = replace(config, model=model_zero)
    h2_zero = friedmann_h_squared(state, cfg_zero)

    if h2_zero > 0 and h2_real > 0:
        ratio = h2_real / h2_zero
        expected = 1.0 / (1.0 + config.model.A)  # = 437/472
        if abs(ratio - expected) > 0.001:
            raise MissingNonMinimalCoupling(
                f"KS-6: h²(A={config.model.A:.6f})/h²(A=0) = {ratio:.6f}, "
                f"expected {expected:.6f}. Non-minimal coupling missing."
            )
    elif h2_real <= 0:
        raise MissingNonMinimalCoupling("KS-6: h² ≤ 0 — Friedmann equation broken.")


__all__ = [
    "F_epsilon",
    "G_eff_over_G",
    "V_epsilon",
    "dV_depsilon",
    "friedmann_h_squared",
    "friedmann_h",
    "MissingNonMinimalCoupling",
    "verify_non_minimal_coupling",
]
