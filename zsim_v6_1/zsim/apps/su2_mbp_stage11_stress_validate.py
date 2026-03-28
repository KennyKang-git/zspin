from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage11 import run_stage11_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run stage-11 stress-ledger validation for Z-Sim v4.2.')
    p.add_argument('--shape-grid', default='1,1,1;2,1,1;2,2,1;2,2,2;3,2,1')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage11_stress_validate')
    p.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    p.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='left')
    p.add_argument('--scan-schemes', default='staggered2,wilson4')
    p.add_argument('--compare-schemes', default='reduced2,staggered2,wilson4')
    p.add_argument('--sign-methods', default='smooth,tanh,rational,arctan,pade11')
    p.add_argument('--amplitudes', default='0.35,0.55,0.75')
    p.add_argument('--separations', default='0.55,0.75,0.95')
    p.add_argument('--widths', default='0.45,0.65')
    p.add_argument('--seam-biases', default='0.10,0.18,0.26')
    p.add_argument('--sign-epsilon-grid', default='5e-6,1e-5,2e-5')
    p.add_argument('--fd-scale-grid', default='0.5,1.0,2.0')
    p.add_argument('--pair-count', type=int, default=2)
    p.add_argument('--sample-size', type=int, default=8)
    p.add_argument('--yt', type=float, default=1.0)
    p.add_argument('--nc', type=float, default=3.0)
    p.add_argument('--mass', type=float, default=0.15)
    p.add_argument('--kappa', type=float, default=0.6)
    p.add_argument('--wilson-r', type=float, default=1.0)
    p.add_argument('--reg-epsilon', type=float, default=1e-4)
    p.add_argument('--cutoff', type=float, default=1e-6)
    p.add_argument('--fd-step', type=float, default=5e-4)
    p.add_argument('--overlap-m0', type=float, default=1.20)
    p.add_argument('--overlap-rho', type=float, default=1.0)
    return p


def _parse_shape_grid(text: str) -> tuple[tuple[int, int, int], ...]:
    shapes = []
    for block in text.split(';'):
        vals = [int(item.strip()) for item in block.split(',') if item.strip()]
        if not vals:
            continue
        if len(vals) != 3:
            raise ValueError('each shape in shape-grid must be nx,ny,nz')
        shapes.append(tuple(vals))
    if not shapes:
        raise ValueError('at least one shape is required')
    return tuple(shapes)


def _parse_floats(text: str) -> tuple[float, ...]:
    vals = [item.strip() for item in text.split(',') if item.strip()]
    if not vals:
        raise ValueError('at least one numeric value is required')
    return tuple(float(v) for v in vals)


def _parse_list(text: str) -> tuple[str, ...]:
    vals = tuple(item.strip() for item in text.split(',') if item.strip())
    if not vals:
        raise ValueError('at least one value is required')
    return vals


def run_su2_mbp_stage11_stress_validate(
    *,
    shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1)),
    output_dir: str | Path = 'outputs/su2_mbp_stage11_stress_validate',
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational', 'arctan', 'pade11'),
    amplitudes: Sequence[float] = (0.35, 0.55, 0.75),
    separations: Sequence[float] = (0.55, 0.75, 0.95),
    widths: Sequence[float] = (0.45, 0.65),
    seam_biases: Sequence[float] = (0.10, 0.18, 0.26),
    sign_epsilon_grid: Sequence[float] = (5e-6, 1e-5, 2e-5),
    fd_scale_grid: Sequence[float] = (0.5, 1.0, 2.0),
    pair_count: int = 2,
    sample_size: int = 8,
    yt: float = 1.0,
    nc: float = 3.0,
    mass: float = 0.15,
    kappa: float = 0.6,
    wilson_r: float = 1.0,
    reg_epsilon: float = 1e-4,
    cutoff: float = 1e-6,
    fd_step: float = 5e-4,
    overlap_m0: float = 1.20,
    overlap_rho: float = 1.0,
) -> dict[str, object]:
    summary, payload = run_stage11_pipeline(
        shape_grid=shape_grid,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        scan_schemes=scan_schemes,
        compare_schemes=compare_schemes,
        sign_methods=sign_methods,
        amplitudes=amplitudes,
        separations=separations,
        widths=widths,
        seam_biases=seam_biases,
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        pair_count=pair_count,
        sample_size=sample_size,
        yt=yt,
        nc=nc,
        mass=mass,
        kappa=kappa,
        wilson_r=wilson_r,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        overlap_m0=overlap_m0,
        overlap_rho=overlap_rho,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage11_shape_rows.csv', [r.to_dict() for r in summary.shape_rows])
    write_csv_rows(out_dir / 'stage11_stress_rows.csv', [r.to_dict() for r in summary.stress_rows])
    write_json(out_dir / 'stage11_summary.json', payload)
    return {
        'success': True,
        'shape_grid': tuple(shape_grid),
        'selected_shape': summary.selected_shape,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'num_shape_rows': len(summary.shape_rows),
        'num_stress_rows': len(summary.stress_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage11_shape_rows.csv', 'stage11_stress_rows.csv', 'stage11_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage11_stress_validate(
            shape_grid=_parse_shape_grid(args.shape_grid),
            output_dir=args.output_dir,
            projector_mode=args.projector_mode,
            chirality_mode=args.chirality_mode,
            scan_schemes=_parse_list(args.scan_schemes),
            compare_schemes=_parse_list(args.compare_schemes),
            sign_methods=_parse_list(args.sign_methods),
            amplitudes=_parse_floats(args.amplitudes),
            separations=_parse_floats(args.separations),
            widths=_parse_floats(args.widths),
            seam_biases=_parse_floats(args.seam_biases),
            sign_epsilon_grid=_parse_floats(args.sign_epsilon_grid),
            fd_scale_grid=_parse_floats(args.fd_scale_grid),
            pair_count=args.pair_count,
            sample_size=args.sample_size,
            yt=args.yt,
            nc=args.nc,
            mass=args.mass,
            kappa=args.kappa,
            wilson_r=args.wilson_r,
            reg_epsilon=args.reg_epsilon,
            cutoff=args.cutoff,
            fd_step=args.fd_step,
            overlap_m0=args.overlap_m0,
            overlap_rho=args.overlap_rho,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v4.2 stage-11 stress-ledger validation failed.', exc)
    return print_cli_summary('Z-Sim v4.2 stage-11 stress-ledger validation complete.', summary, ordered_keys=('success', 'shape_grid', 'selected_shape', 'selected_sign_method', 'selected_scheme', 'num_shape_rows', 'num_stress_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
