"""CLI for reduced SU(2) BCC scans in Z-Sim v1.0."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.fermion import fermion_effective_action_proxy, gauge_covariant_hopping_matrix, smallest_singular_values
from zsim.lgt.flow import cooling_trajectory
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.observables import link_observables
from zsim.lgt.su2_links import identity_links, random_su2_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run reduced SU(2) BCC scans for Z-Sim v1.0.')
    parser.add_argument('--shape', default='2,2,2')
    parser.add_argument('--output-dir', default='outputs/su2_bcc_scan')
    parser.add_argument('--seed', type=int, default=350437)
    parser.add_argument('--cooling-steps', type=int, default=8)
    parser.add_argument('--alpha', type=float, default=0.15)
    parser.add_argument('--identity', action='store_true')
    return parser


def _parse_shape(text: str) -> tuple[int, int, int]:
    vals = [int(item.strip()) for item in text.split(',') if item.strip()]
    if len(vals) != 3:
        raise ValueError('shape must be nx,ny,nz')
    return tuple(vals)  # type: ignore[return-value]


def run_su2_bcc_scan(*, shape: tuple[int, int, int] = (2, 2, 2), output_dir: str | Path = 'outputs/su2_bcc_scan', seed: int = 350437, cooling_steps: int = 8, alpha: float = 0.15, use_identity: bool = False) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    links = identity_links(lattice.edges) if use_identity else random_su2_links(lattice.edges, seed=seed)
    trajectory = cooling_trajectory(links, cooling_steps, plaquettes, alpha=alpha)
    rows = []
    for step, state in enumerate(trajectory):
        obs = link_observables(state, plaquettes)
        hopping = gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, state)
        rows.append({
            'step': step,
            **obs,
            'smallest_sigma_0': smallest_singular_values(hopping, k=1)[0],
            'gamma_f_proxy': fermion_effective_action_proxy(hopping),
        })
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'cooling_scan.csv', rows)
    write_json(out_dir / 'bcc_summary.json', {
        'shape': list(shape),
        'num_sites': lattice.num_sites,
        'num_edges': lattice.num_edges,
        'num_plaquettes': len(plaquettes),
        'site_types': {'corner': lattice.site_types.count('corner'), 'center': lattice.site_types.count('center')},
        'final_observables': rows[-1],
    })
    return {'success': True, 'shape': shape, 'plaquettes': len(plaquettes), 'output_dir': str(out_dir), 'generated_outputs': ['cooling_scan.csv', 'bcc_summary.json']}


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_bcc_scan(shape=_parse_shape(args.shape), output_dir=args.output_dir, seed=args.seed, cooling_steps=args.cooling_steps, alpha=args.alpha, use_identity=args.identity)
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 SU(2) BCC scan failed.', exc)
    return print_cli_summary('Z-Sim v1.0 SU(2) BCC scan complete.', summary, ordered_keys=('success', 'shape', 'plaquettes', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
