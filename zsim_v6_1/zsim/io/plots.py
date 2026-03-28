"""Simple plot writers for Z-Sim v3.1 output trajectories."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt

from zsim.core import ZSimConfig, ZSimState
from zsim.observables import H_like


def write_basic_plots(output_dir: str | Path, states: list[ZSimState], config: ZSimConfig) -> list[Path]:
    """Write a small default plot set for one background run."""
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    N = [state.N for state in states]
    paths: list[Path] = []

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(N, [state.rho_x for state in states], label='rho_x')
    ax.plot(N, [state.rho_z for state in states], label='rho_z')
    ax.plot(N, [state.rho_y for state in states], label='rho_y')
    ax.set_xlabel('N')
    ax.set_ylabel('density')
    ax.set_title('Sector densities')
    ax.legend()
    density_path = out_dir / 'densities.png'
    fig.tight_layout()
    fig.savefig(density_path, dpi=150)
    plt.close(fig)
    paths.append(density_path)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(N, [state.epsilon for state in states], label='epsilon')
    ax.plot(N, [state.phi_z for state in states], label='phi_z')
    ax.set_xlabel('N')
    ax.set_ylabel('value')
    ax.set_title('Order parameter and phase')
    ax.legend()
    phase_path = out_dir / 'epsilon_phase.png'
    fig.tight_layout()
    fig.savefig(phase_path, dpi=150)
    plt.close(fig)
    paths.append(phase_path)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(N, [H_like(state) for state in states], label='H_like')
    ax.plot(N, [state.J_xz for state in states], label='J_xz')
    ax.plot(N, [state.J_zy for state in states], label='J_zy')
    ax.set_xlabel('N')
    ax.set_ylabel('value')
    ax.set_title('Expansion and currents')
    ax.legend()
    current_path = out_dir / 'expansion_currents.png'
    fig.tight_layout()
    fig.savefig(current_path, dpi=150)
    plt.close(fig)
    paths.append(current_path)

    return paths


__all__ = ['write_basic_plots']
