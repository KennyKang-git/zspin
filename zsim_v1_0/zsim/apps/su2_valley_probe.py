"""CLI for reduced collective-coordinate valley probes in Z-Sim v1.0."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import numpy as np

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.fermion import fermion_effective_action_proxy, gauge_covariant_hopping_matrix, smallest_singular_values
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.observables import link_observables
from zsim.lgt.valley import collective_valley_links, fit_even_quartic_bilinear_proxy


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Probe reduced collective-coordinate valleys in Z-Sim v1.0.')
    parser.add_argument('--shape', default='2,2,2')
    parser.add_argument('--amplitudes', default='-1.0,-0.5,-0.25,0.0,0.25,0.5,1.0')
    parser.add_argument('--output-dir', default='outputs/su2_valley_probe')
    return parser


def _parse_shape(text: str) -> tuple[int, int, int]:
    vals = [int(item.strip()) for item in text.split(',') if item.strip()]
    if len(vals) != 3:
        raise ValueError('shape must be nx,ny,nz')
    return tuple(vals)  # type: ignore[return-value]


def _parse_amplitudes(text: str) -> tuple[float, ...]:
    vals = [item.strip() for item in text.split(',') if item.strip()]
    if not vals:
        raise ValueError('at least one amplitude is required')
    return tuple(float(v) for v in vals)


def run_su2_valley_probe(*, shape: tuple[int, int, int] = (2, 2, 2), amplitudes: Sequence[float] = (-1.0, -0.5, -0.25, 0.0, 0.25, 0.5, 1.0), output_dir: str | Path = 'outputs/su2_valley_probe') -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    rows = []
    gamma_vals = []
    amps = []
    for amplitude in amplitudes:
        links = collective_valley_links(lattice.edges, lattice.positions, amplitude)
        hopping = gauge_covariant_hopping_matrix(lattice.num_sites, lattice.edges, links)
        gamma = fermion_effective_action_proxy(hopping)
        rows.append({
            'amplitude': float(amplitude),
            **link_observables(links, plaquettes),
            'sigma_min': smallest_singular_values(hopping, k=1)[0],
            'gamma_f_proxy': gamma,
        })
        amps.append(float(amplitude))
        gamma_vals.append(float(gamma))
    fit = fit_even_quartic_bilinear_proxy(np.asarray(amps, dtype=float), np.asarray(gamma_vals, dtype=float))
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'valley_probe.csv', rows)
    write_json(out_dir / 'valley_probe_summary.json', {
        'shape': list(shape),
        'num_sites': lattice.num_sites,
        'num_edges': lattice.num_edges,
        'num_plaquettes': len(plaquettes),
        'argmin_gamma': min(rows, key=lambda row: row['gamma_f_proxy']),
        'even_quartic_fit': fit,
    })
    return {'success': True, 'shape': shape, 'plaquettes': len(plaquettes), 'output_dir': str(out_dir), 'generated_outputs': ['valley_probe.csv', 'valley_probe_summary.json']}


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_valley_probe(shape=_parse_shape(args.shape), amplitudes=_parse_amplitudes(args.amplitudes), output_dir=args.output_dir)
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 SU(2) valley probe failed.', exc)
    return print_cli_summary('Z-Sim v1.0 SU(2) valley probe complete.', summary, ordered_keys=('success', 'shape', 'plaquettes', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
