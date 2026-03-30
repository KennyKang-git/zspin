"""Kernel exports for Z-Sim v1.0."""

from .background import BackgroundDerivatives, compute_background_derivatives, drho_x_dN, drho_y_dN, drho_z_dN, friedmann_like_h
from .epsilon import EpsilonDerivatives, compute_epsilon_source, depsilon_dN, dpi_epsilon_dN, dV_depsilon, epsilon_potential, epsilon_rhs
from .friedmann import (
    F_epsilon, G_eff_over_G, V_epsilon, dV_depsilon as dV_depsilon_friedmann,
    friedmann_h_squared, friedmann_h, MissingNonMinimalCoupling, verify_non_minimal_coupling,
)
from .inflation import V_einstein, dV_einstein_deps, K_einstein, slow_roll_epsilon1, compute_inflation_observables
from .mediation import compute_J_xz, compute_J_zy, compute_currents, mediation_contrast
from .operators import build_structural_operator, build_transfer_proxy, direct_xy_block, effective_rank_xy
from .phase import dphi_dN, phase_gate, phase_source_argument, wrap_phase
from .sectors import canonical_sector_order, get_sector_dims, is_direct_xy_allowed, sector_ratio

__all__ = [
    'BackgroundDerivatives',
    'compute_background_derivatives',
    'drho_x_dN',
    'drho_y_dN',
    'drho_z_dN',
    'friedmann_like_h',
    'EpsilonDerivatives',
    'compute_epsilon_source',
    'depsilon_dN',
    'dpi_epsilon_dN',
    'dV_depsilon',
    'epsilon_potential',
    'epsilon_rhs',
    # Friedmann (v3.0 — from Z-Spin action)
    'F_epsilon',
    'G_eff_over_G',
    'V_epsilon',
    'friedmann_h_squared',
    'friedmann_h',
    'MissingNonMinimalCoupling',
    'verify_non_minimal_coupling',
    # Inflation (v3.0 — Einstein-frame)
    'V_einstein',
    'dV_einstein_deps',
    'K_einstein',
    'slow_roll_epsilon1',
    'compute_inflation_observables',
    # Mediation
    'compute_J_xz',
    'compute_J_zy',
    'compute_currents',
    'mediation_contrast',
    'build_structural_operator',
    'build_transfer_proxy',
    'direct_xy_block',
    'effective_rank_xy',
    'dphi_dN',
    'phase_gate',
    'phase_source_argument',
    'wrap_phase',
    'canonical_sector_order',
    'get_sector_dims',
    'is_direct_xy_allowed',
    'sector_ratio',
]
