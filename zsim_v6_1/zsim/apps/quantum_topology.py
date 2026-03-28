"""CLI for exact polyhedral spectral calculations in Z-Sim v3.2."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

import numpy as np

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.quantum.dirac import hodge_dirac
from zsim.quantum.effective import heat_kernel_trace, regularized_logdet, spectral_action_moments
from zsim.quantum.geometry import build_truncated_icosahedron, build_truncated_octahedron
from zsim.quantum.hodge import hodge_laplacians
from zsim.quantum.incidence import assert_boundary_nilpotency, boundary_matrices
from zsim.quantum.spectrum import eigensystem, spectral_summary

_BUILDERS = {'ti': build_truncated_icosahedron, 'to': build_truncated_octahedron}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run exact Z-Sim v3.2 quantum topology calculations.')
    parser.add_argument('--geometry', choices=sorted(_BUILDERS), default='ti')
    parser.add_argument('--output-dir', default='outputs/quantum_topology')
    parser.add_argument('--heat-times', default='0.1,1.0,10.0')
    return parser


def _parse_heat_times(text: str) -> tuple[float, ...]:
    vals = [item.strip() for item in text.split(',') if item.strip()]
    return tuple(float(item) for item in vals) if vals else (1.0,)


def run_quantum_topology(*, geometry: str = 'ti', output_dir: str | Path = 'outputs/quantum_topology', heat_times: Sequence[float] = (0.1, 1.0, 10.0)) -> dict[str, object]:
    complex_ = _BUILDERS[geometry]()
    B1, B2 = boundary_matrices(complex_)
    assert_boundary_nilpotency(B1, B2)
    L0, L1, L2 = hodge_laplacians(B1, B2)
    D = hodge_dirac(B1, B2)
    adjacency_values, _ = eigensystem(complex_.adjacency_matrix())
    dirac_values, _ = eigensystem(D)
    out_dir = ensure_output_dir(output_dir)
    write_json(out_dir / 'topology_summary.json', {
        'geometry': complex_.name,
        'counts': {'V': complex_.V, 'E': complex_.E, 'F': complex_.F},
        'degree_min': float(np.min(complex_.degree_sequence())),
        'degree_max': float(np.max(complex_.degree_sequence())),
        'boundary_shapes': {'B1': list(B1.shape), 'B2': list(B2.shape)},
        'laplacian_shapes': {'L0': list(L0.shape), 'L1': list(L1.shape), 'L2': list(L2.shape)},
        'adjacency': spectral_summary(adjacency_values),
        'dirac': spectral_summary(dirac_values),
        'dirac_logdet_mu2_1e-6': regularized_logdet(dirac_values, mu2=1e-6),
        'dirac_moments': spectral_action_moments(dirac_values),
        'heat_kernel': {str(float(t)): heat_kernel_trace(dirac_values, float(t)) for t in heat_times},
    })
    write_csv_rows(out_dir / 'dirac_spectrum.csv', [{'index': i, 'eigenvalue': float(v)} for i, v in enumerate(dirac_values)])
    return {'success': True, 'geometry': complex_.name, 'output_dir': str(out_dir), 'counts': f'V={complex_.V}, E={complex_.E}, F={complex_.F}', 'generated_outputs': ['topology_summary.json', 'dirac_spectrum.csv']}


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_quantum_topology(geometry=args.geometry, output_dir=args.output_dir, heat_times=_parse_heat_times(args.heat_times))
    except Exception as exc:
        return print_cli_failure('Z-Sim v3.2 quantum topology run failed.', exc)
    return print_cli_summary('Z-Sim v3.2 quantum topology run complete.', summary, ordered_keys=('success', 'geometry', 'counts', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
