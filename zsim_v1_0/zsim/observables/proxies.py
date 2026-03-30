"""Structural diagnostics and external-comparison proxies for Z-Sim v1.0."""

from __future__ import annotations

from dataclasses import dataclass

from zsim.core import A_LOCKED, ZSimConfig, ZSimState
from zsim.kernel import effective_rank_xy, phase_gate

from .densities import compute_density_observables
from .entropy import compute_entropy_observables
from .expansion import compute_expansion_observables


@dataclass(frozen=True, slots=True)
class StructuralDiagnostics:
    """Diagnostics that expose reduced structural behavior."""

    rank_xy_proxy: float
    mediation_efficiency: float
    phase_gate_value: float
    sigma_struct: float
    sector_asymmetry: float

    def to_dict(self) -> dict[str, float]:
        return {
            "rank_xy_proxy": float(self.rank_xy_proxy),
            "mediation_efficiency": float(self.mediation_efficiency),
            "phase_gate_value": float(self.phase_gate_value),
            "sigma_struct": float(self.sigma_struct),
            "sector_asymmetry": float(self.sector_asymmetry),
        }


@dataclass(frozen=True, slots=True)
class ExternalProxies:
    """Clearly labeled proxy outputs for coarse external comparison."""

    delta_neff_proxy: float
    bbn_support_proxy: float
    ewsb_support_proxy: float
    decoherence_proxy: float

    def to_dict(self) -> dict[str, float]:
        return {
            "delta_neff_proxy": float(self.delta_neff_proxy),
            "bbn_support_proxy": float(self.bbn_support_proxy),
            "ewsb_support_proxy": float(self.ewsb_support_proxy),
            "decoherence_proxy": float(self.decoherence_proxy),
        }



def mediation_efficiency(state: ZSimState) -> float:
    """Return a bounded current-to-budget transmission proxy."""

    scale = state.rho_total + abs(state.J_xz) + abs(state.J_zy)
    if scale == 0.0:
        return 0.0
    return (abs(state.J_xz) + abs(state.J_zy)) / scale



def compute_structural_diagnostics(state: ZSimState, config: ZSimConfig) -> StructuralDiagnostics:
    """Compile structural diagnostics from the current reduced state."""

    density = compute_density_observables(state)
    return StructuralDiagnostics(
        rank_xy_proxy=float(effective_rank_xy(state, config)),
        mediation_efficiency=mediation_efficiency(state),
        phase_gate_value=float(phase_gate(state.phi_z, config.closure.phase_mode)),
        sigma_struct=float(state.sigma_struct),
        sector_asymmetry=float(density.sector_asymmetry),
    )



def compute_external_proxies(state: ZSimState, config: ZSimConfig) -> ExternalProxies:
    """Compile optional proxy outputs.

    These outputs are intentionally coarse and explicitly labeled as proxies.
    They should never be surfaced as precision observables in v0.1.
    """

    density = compute_density_observables(state)
    entropy = compute_entropy_observables(state)
    gate = float(phase_gate(state.phi_z, config.closure.phase_mode))
    med = mediation_efficiency(state)

    delta_neff = density.omega_y
    bbn_support = max(0.0, 1.0 - density.sector_asymmetry)
    ewsb_support = abs(state.epsilon) * abs(gate) * A_LOCKED / (1.0 + abs(state.pi_epsilon))
    decoherence = med * (1.0 - entropy.phase_lock_index)
    return ExternalProxies(
        delta_neff_proxy=float(delta_neff),
        bbn_support_proxy=float(bbn_support),
        ewsb_support_proxy=float(ewsb_support),
        decoherence_proxy=float(decoherence),
    )



def compile_observables(state: ZSimState, config: ZSimConfig) -> dict[str, float]:
    """Compile the full v0.1 observable payload into a flat mapping."""

    payload: dict[str, float] = {}
    for bundle in (
        compute_density_observables(state),
        compute_expansion_observables(state, config),
        compute_entropy_observables(state),
        compute_structural_diagnostics(state, config),
        compute_external_proxies(state, config),
    ):
        payload.update(bundle.to_dict())
    return payload


__all__ = [
    "ExternalProxies",
    "StructuralDiagnostics",
    "compile_observables",
    "compute_external_proxies",
    "compute_structural_diagnostics",
    "mediation_efficiency",
]
