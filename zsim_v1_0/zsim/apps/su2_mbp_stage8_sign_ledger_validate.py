from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.stage8 import run_stage8_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run stage-8 sign-ledger validation for Z-Sim v1.0.')
    p.add_argument('--shape', default='2,2,2')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage8_sign_ledger_validate')
    p.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    p.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='left')
    p.add_argument('--scan-schemes', default='staggered2,wilson4')
    p.add_argument('--compare-schemes', default='reduced2,staggered2,wilson4')
    p.add_argument('--sign-methods', default='smooth,tanh,rational')
    p.add_argument('--amplitudes', default='0.35,0.55,0.75')
    p.add_argument('--separations', default='0.55,0.75,0.95')
    p.add_argument('--widths', default='0.45,0.65')
    p.add_argument('--seam-biases', default='0.10,0.18,0.26')
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
    p.add_argument('--sign-epsilon', type=float, default=1e-5)
    return p


def _parse_shape(text: str) -> tuple[int, int, int]:
    vals = [int(item.strip()) for item in text.split(',') if item.strip()]
    if len(vals) != 3:
        raise ValueError('shape must be nx,ny,nz')
    return tuple(vals)


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


def run_su2_mbp_stage8_sign_ledger_validate(
    *,
    shape: tuple[int, int, int] = (2, 2, 2),
    output_dir: str | Path = 'outputs/su2_mbp_stage8_sign_ledger_validate',
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational'),
    amplitudes: Sequence[float] = (0.35, 0.55, 0.75),
    separations: Sequence[float] = (0.55, 0.75, 0.95),
    widths: Sequence[float] = (0.45, 0.65),
    seam_biases: Sequence[float] = (0.10, 0.18, 0.26),
    pair_count: int = 2,
    sample_size: int = 8,
    yt: float = 1.0,
    nc: float = 3.0,
    mass: float = 0.15,
    kappa: float = 0.6,
    wilson_r: float = 1.0,
    reg_epsilon: float = 1.0e-4,
    cutoff: float = 1.0e-6,
    fd_step: float = 5.0e-4,
    overlap_m0: float = 1.20,
    overlap_rho: float = 1.0,
    sign_epsilon: float = 1.0e-5,
) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    summary, _best_links, payload = run_stage8_pipeline(
        lattice,
        amplitude_grid=amplitudes,
        separation_grid=separations,
        width_grid=widths,
        seam_bias_grid=seam_biases,
        scan_schemes=scan_schemes,
        compare_schemes=compare_schemes,
        sign_methods=sign_methods,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
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
        sign_epsilon=sign_epsilon,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage8_sign_rows.csv', [r.to_dict() for r in summary.sign_rows])
    write_csv_rows(out_dir / 'stage8_ledger_rows.csv', [r.to_dict() for r in summary.ledger_rows])
    write_json(out_dir / 'stage8_summary.json', {
        'shape': list(shape),
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'scan_schemes': list(scan_schemes),
        'compare_schemes': list(compare_schemes),
        'sign_methods': list(sign_methods),
        **payload,
    })
    return {
        'success': True,
        'shape': shape,
        'scan_schemes': tuple(scan_schemes),
        'compare_schemes': tuple(compare_schemes),
        'sign_methods': tuple(sign_methods),
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'num_sign_rows': len(summary.sign_rows),
        'num_ledger_rows': len(summary.ledger_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage8_sign_rows.csv', 'stage8_ledger_rows.csv', 'stage8_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage8_sign_ledger_validate(
            shape=_parse_shape(args.shape),
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
            sign_epsilon=args.sign_epsilon,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 stage-8 sign-ledger validation failed.', exc)
    return print_cli_summary('Z-Sim v1.0 stage-8 sign-ledger validation complete.', summary, ordered_keys=('success', 'shape', 'scan_schemes', 'compare_schemes', 'sign_methods', 'selected_sign_method', 'selected_scheme', 'num_sign_rows', 'num_ledger_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
