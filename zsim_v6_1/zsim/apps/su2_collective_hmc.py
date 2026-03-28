"""CLI for reduced collective-coordinate HMC in Z-Sim v3.4."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.fermion import fermion_effective_action_proxy, gauge_covariant_hopping_matrix
from zsim.lgt.hmc import reduced_collective_hmc
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.observables import link_observables
from zsim.lgt.valley import collective_valley_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run reduced collective-coordinate HMC for Z-Sim v3.4.')
    parser.add_argument('--shape', default='2,2,2')
    parser.add_argument('--output-dir', default='outputs/su2_collective_hmc')
    parser.add_argument('--initial', type=float, default=0.0)
    parser.add_argument('--steps', type=int, default=48)
    parser.add_argument('--step-size', type=float, default=0.12)
    parser.add_argument('--leapfrog-steps', type=int, default=6)
    parser.add_argument('--seed', type=int, default=350437)
    return parser


def _parse_shape(text: str) -> tuple[int, int, int]:
    vals = [int(item.strip()) for item in text.split(',') if item.strip()]
    if len(vals) != 3:
        raise ValueError('shape must be nx,ny,nz')
    return tuple(vals)  # type: ignore[return-value]


def run_su2_collective_hmc(*, shape: tuple[int, int, int] = (2, 2, 2), output_dir: str | Path = 'outputs/su2_collective_hmc', initial: float = 0.0, steps: int = 48, step_size: float = 0.12, leapfrog_steps: int = 6, seed: int = 350437) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)

    def potential(amplitude: float) -> float:
        links = collective_valley_links(lattice.edges, lattice.positions, amplitude)
        hopping = gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, links)
        obs = link_observables(links, plaquettes)
        return 0.5 * amplitude * amplitude + obs['wilson_action_proxy'] + 0.05 * fermion_effective_action_proxy(hopping)

    chain = reduced_collective_hmc(initial, potential=potential, steps=steps, step_size=step_size, leapfrog_steps=leapfrog_steps, seed=seed)
    rows = [{'step': idx, 'amplitude': amp, 'potential': potential(amp)} for idx, amp in enumerate(chain.samples)]
    final_links = collective_valley_links(lattice.edges, lattice.positions, chain.samples[-1] if chain.samples else initial)
    final_obs = link_observables(final_links, plaquettes)
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'collective_hmc_chain.csv', rows)
    write_json(out_dir / 'collective_hmc_summary.json', {
        'shape': list(shape),
        'num_sites': lattice.num_sites,
        'num_edges': lattice.num_edges,
        'num_plaquettes': len(plaquettes),
        'accept_rate': chain.accept_rate,
        'potential_mean': chain.potential_mean,
        'final_amplitude': chain.samples[-1] if chain.samples else float(initial),
        'final_observables': final_obs,
    })
    return {'success': True, 'shape': shape, 'plaquettes': len(plaquettes), 'accept_rate': chain.accept_rate, 'output_dir': str(out_dir), 'generated_outputs': ['collective_hmc_chain.csv', 'collective_hmc_summary.json']}


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_collective_hmc(shape=_parse_shape(args.shape), output_dir=args.output_dir, initial=args.initial, steps=args.steps, step_size=args.step_size, leapfrog_steps=args.leapfrog_steps, seed=args.seed)
    except Exception as exc:
        return print_cli_failure('Z-Sim v3.4 collective HMC failed.', exc)
    return print_cli_summary('Z-Sim v3.4 collective HMC complete.', summary, ordered_keys=('success', 'shape', 'plaquettes', 'accept_rate', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
