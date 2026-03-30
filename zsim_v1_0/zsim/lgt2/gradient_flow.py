"""Wilson gradient flow on periodic BCC T³.

Architecture improvement #2: Continuous-time Wilson gradient flow replacing
discrete cooling steps.

The flow equation (Lüscher, JHEP 2010):
  ∂_t V_μ(x,t) = −g₀² {∂_{x,μ} S_W[V]} V_μ(x,t)

In terms of the force:
  Z_μ = V_μ · Σ_μ†   (link times conjugate staple sum)
  X_μ = TA(Z_μ)       (traceless anti-Hermitian projection)
  V̇_μ = X_μ · V_μ     (flow equation)

Integration via 3rd-order Runge-Kutta (Lüscher 2010, eq. 3.9):
  W₀ = V(t)
  W₁ = exp(¼ε X(W₀)) · W₀
  W₂ = exp(8/9 ε X(W₁) − 17/36 ε X(W₀)) · W₁
  V(t+ε) = exp(¾ε X(W₂) − 8/9 ε X(W₁) + 17/36 ε X(W₀)) · W₂

The flow time t has dimension [length²]; at flow time t, the gauge field
is smeared over a radius r ≈ √(8t).

Observable: E(t) = −½ Tr(G_μν G_μν) where G is the clover field strength.
The quantity t²<E(t)> defines the reference scale t₀ via t₀²<E(t₀)> = 0.3.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from zsim.lgt2.gauge_field import GaugeField, all_staple_sums, avg_plaquette, wilson_action
from zsim.lgt2.su2 import su2_exp, traceless_antihermitian, project_su2

Array = np.ndarray


@dataclass
class FlowState:
    """State of the gauge field at a given flow time."""
    flow_time: float
    gauge_field: GaugeField
    action_density: float
    avg_plaq: float
    energy_density: float  # t²<E(t)>


def _compute_forces(gf: GaugeField) -> dict[tuple[int, int], Array]:
    """Compute X_μ = TA(V_μ · Σ_μ†) for all links."""
    staples = all_staple_sums(gf)
    forces = {}
    for edge, U in gf.links.items():
        sigma = staples[edge]
        Z = U @ sigma.conj().T
        forces[edge] = traceless_antihermitian(Z)
    return forces


def _apply_exponential(
    gf: GaugeField, forces: dict[tuple[int, int], Array], coeff: float
) -> dict[tuple[int, int], Array]:
    """Compute exp(coeff · X_edge) · U_edge for all edges."""
    new_links = {}
    for edge, U in gf.links.items():
        X = forces.get(edge, np.zeros((2, 2), dtype=np.complex128))
        new_links[edge] = project_su2(su2_exp(coeff * X) @ U)
    return new_links


def rk3_step(gf: GaugeField, epsilon: float) -> GaugeField:
    """Single Lüscher RK3 gradient flow step.

    Parameters
    ----------
    gf : GaugeField
        Current gauge field configuration.
    epsilon : float
        Flow time step Δt.

    Returns
    -------
    GaugeField
        Updated configuration at t + ε.
    """
    # Stage 0: W₀ = V(t), compute X₀
    X0 = _compute_forces(gf)

    # Stage 1: W₁ = exp(ε/4 · X₀) · W₀
    links1 = _apply_exponential(gf, X0, epsilon / 4.0)
    gf1 = GaugeField(lattice=gf.lattice, links=links1, beta=gf.beta)
    X1 = _compute_forces(gf1)

    # Stage 2: W₂ = exp(8ε/9 · X₁ − 17ε/36 · X₀) · W₁
    combined_12 = {}
    for edge in gf.lattice.edges:
        combined_12[edge] = (8.0 / 9.0) * epsilon * X1[edge] - (17.0 / 36.0) * epsilon * X0[edge]
    links2 = {}
    for edge, U in links1.items():
        links2[edge] = project_su2(su2_exp(combined_12[edge]) @ U)
    gf2 = GaugeField(lattice=gf.lattice, links=links2, beta=gf.beta)
    X2 = _compute_forces(gf2)

    # Final: V(t+ε) = exp(¾ε X₂ − 8ε/9 X₁ + 17ε/36 X₀) · W₂
    final_exp = {}
    for edge in gf.lattice.edges:
        final_exp[edge] = (
            (3.0 / 4.0) * epsilon * X2[edge]
            - (8.0 / 9.0) * epsilon * X1[edge]
            + (17.0 / 36.0) * epsilon * X0[edge]
        )
    final_links = {}
    for edge, U in links2.items():
        final_links[edge] = project_su2(su2_exp(final_exp[edge]) @ U)

    return GaugeField(lattice=gf.lattice, links=final_links, beta=gf.beta)


def energy_density(gf: GaugeField) -> float:
    """Gauge energy density: E = (β/V) Σ_P (1 - ½ Re Tr(U_P)).

    This is proportional to <Tr(F²)> on the lattice.
    """
    S = wilson_action(gf)
    V = gf.lattice.volume_cells
    return S / max(V, 1)


class WilsonGradientFlow:
    """Wilson gradient flow integrator.

    Implements the 5-phase MBP protocol step 2:
    Cool/gradient-flow to the caloron constituent sector.

    The flow smooths UV fluctuations while preserving IR topology.
    The flow time t₀ (defined by t₀²<E(t₀)> = 0.3) sets a physical
    reference scale independent of the bare coupling.
    """

    def __init__(self, epsilon: float = 0.01, max_steps: int = 1000,
                 target_t0_condition: float = 0.3):
        """
        Parameters
        ----------
        epsilon : float
            Flow time step size.
        max_steps : int
            Maximum number of flow steps.
        target_t0_condition : float
            Target value for t²<E(t)> that defines t₀.
        """
        self.epsilon = epsilon
        self.max_steps = max_steps
        self.target_t0_condition = target_t0_condition

    def flow(self, gf: GaugeField, *, n_steps: int | None = None,
             record_every: int = 1) -> list[FlowState]:
        """Run the gradient flow.

        Parameters
        ----------
        gf : GaugeField
            Initial configuration.
        n_steps : int, optional
            Number of steps (defaults to max_steps).
        record_every : int
            Record state every N steps.

        Returns
        -------
        list[FlowState]
            Recorded flow states.
        """
        steps = n_steps or self.max_steps
        current = gf.copy()
        t = 0.0
        trajectory: list[FlowState] = []

        # Record initial state
        E = energy_density(current)
        trajectory.append(FlowState(
            flow_time=t,
            gauge_field=current.copy(),
            action_density=wilson_action(current) / max(current.lattice.volume_cells, 1),
            avg_plaq=avg_plaquette(current),
            energy_density=t * t * E,
        ))

        for step in range(1, steps + 1):
            current = rk3_step(current, self.epsilon)
            t += self.epsilon

            if step % record_every == 0:
                E = energy_density(current)
                trajectory.append(FlowState(
                    flow_time=t,
                    gauge_field=current.copy(),
                    action_density=wilson_action(current) / max(current.lattice.volume_cells, 1),
                    avg_plaq=avg_plaquette(current),
                    energy_density=t * t * E,
                ))

        return trajectory

    def flow_to_scale(self, gf: GaugeField) -> tuple[GaugeField, float, list[FlowState]]:
        """Flow until t²<E(t)> crosses the t₀ condition.

        Returns
        -------
        tuple
            (flowed_config, t0, trajectory)
        """
        trajectory = self.flow(gf, record_every=1)
        t0 = 0.0
        best_gf = gf

        for i in range(1, len(trajectory)):
            prev = trajectory[i - 1]
            curr = trajectory[i]
            if curr.energy_density >= self.target_t0_condition >= prev.energy_density:
                # Linear interpolation for t₀
                if abs(curr.energy_density - prev.energy_density) > 1e-15:
                    frac = (self.target_t0_condition - prev.energy_density) / (
                        curr.energy_density - prev.energy_density
                    )
                    t0 = prev.flow_time + frac * (curr.flow_time - prev.flow_time)
                else:
                    t0 = curr.flow_time
                best_gf = curr.gauge_field
                break
            if curr.energy_density <= self.target_t0_condition:
                t0 = curr.flow_time
                best_gf = curr.gauge_field

        return best_gf, t0, trajectory
