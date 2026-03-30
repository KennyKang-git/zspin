from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.mbp import mbp_prefactor
from zsim.lgt.stage7 import evaluate_stage7_bundle, scan_stage7_valley_family, stage7_overlap_controls


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run stage-7 overlap-aware MBP validation for Z-Sim v1.0.')
    p.add_argument('--shape', default='2,2,2')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage7_overlap_validate')
    p.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    p.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='left')
    p.add_argument('--scan-schemes', default='staggered2,wilson4')
    p.add_argument('--compare-schemes', default='reduced2,staggered2,wilson4')
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
    p.add_argument('--seed', type=int, default=350437)
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


def _parse_schemes(text: str) -> tuple[str, ...]:
    vals = tuple(item.strip() for item in text.split(',') if item.strip())
    if not vals:
        raise ValueError('at least one fermion scheme is required')
    return vals


def run_su2_mbp_stage7_overlap_validate(
    *,
    shape: tuple[int, int, int] = (2, 2, 2),
    output_dir: str | Path = 'outputs/su2_mbp_stage7_overlap_validate',
    projector_mode: str = 'center',
    chirality_mode: str = 'left',
    scan_schemes: Sequence[str] = ('staggered2', 'wilson4'),
    compare_schemes: Sequence[str] = ('reduced2', 'staggered2', 'wilson4'),
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
    reg_epsilon: float = 1e-4,
    cutoff: float = 1e-6,
    fd_step: float = 5e-4,
    overlap_m0: float = 1.20,
    overlap_rho: float = 1.0,
    sign_epsilon: float = 1e-5,
    seed: int = 350437,
) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    best, best_links, scan_rows = scan_stage7_valley_family(
        lattice,
        amplitude_grid=amplitudes,
        separation_grid=separations,
        width_grid=widths,
        seam_bias_grid=seam_biases,
        scan_schemes=scan_schemes,
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
    scheme_rows, harness, overlap = evaluate_stage7_bundle(
        lattice,
        best_links,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        schemes=compare_schemes,
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
    controls = stage7_overlap_controls(
        lattice,
        amplitude=best.amplitude,
        separation=best.separation,
        width=best.width,
        seam_bias=best.seam_bias,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        schemes=compare_schemes,
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
        seed=seed,
    )
    best_objective = float(best.objective)
    median_objective = float(sorted(row.objective for row in scan_rows)[len(scan_rows) // 2])
    identity_overlap = float(controls['identity']['overlap']['score'])
    identity_chiral = float(controls['identity']['overlap']['chiral_abs_mean'])
    phase_scrambled_overlap = float(controls['phase_scrambled_caloron']['overlap']['score'])
    gates = {
        'G-OVERLAP-LOCALIZATION': best_objective > median_objective,
        'G-OVERLAP-CHIRALITY': float(overlap.chiral_abs_mean) > 0.01,
        'G-OVERLAP-VS-IDENTITY': (float(overlap.chiral_abs_mean) > identity_chiral) or (float(overlap.score) > identity_overlap),
        'G-PHASE-SCRAMBLE-DISTINCT': abs(float(overlap.score) - phase_scrambled_overlap) > 1.0e-8,
        'G-WILSON-PRESENT': 'wilson4' in set(compare_schemes),
        'G-FD-CONSISTENCY': float(harness['gamma_gap_max']) < 2.5e-1,
        'G-SCAN-COVERAGE': len(scan_rows) == len(amplitudes) * len(separations) * len(widths) * len(seam_biases),
    }
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage7_scan_rows.csv', [row.to_dict() for row in scan_rows])
    write_csv_rows(out_dir / 'stage7_scheme_rows.csv', [row.to_dict() for row in scheme_rows])
    write_json(out_dir / 'stage7_overlap_summary.json', {
        'shape': list(shape),
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'scan_schemes': list(scan_schemes),
        'compare_schemes': list(compare_schemes),
        'best_candidate': best.to_dict(),
        'scheme_rows': [row.to_dict() for row in scheme_rows],
        'scheme_harness': harness,
        'overlap': overlap.to_dict(),
        'controls': controls,
        'prefactor_exp_minus_2S': mbp_prefactor(),
        'mu2_with_prefactor_by_scheme': {row.scheme: row.mu2_formula_proxy * mbp_prefactor() for row in scheme_rows},
        'gates': gates,
        'notes': {
            'stage': 'overlap-aware valley family + Wilson-weighted comparison harness',
            'status': 'preproduction-surrogate',
            'non_claim': 'not an exact overlap implementation on a production 8^3 lattice, not a continuum caloron, not final Higgs bilinear closure',
        },
    })
    return {
        'success': True,
        'shape': shape,
        'scan_schemes': tuple(scan_schemes),
        'compare_schemes': tuple(compare_schemes),
        'num_scan_rows': len(scan_rows),
        'num_scheme_rows': len(scheme_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage7_scan_rows.csv', 'stage7_scheme_rows.csv', 'stage7_overlap_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage7_overlap_validate(
            shape=_parse_shape(args.shape),
            output_dir=args.output_dir,
            projector_mode=args.projector_mode,
            chirality_mode=args.chirality_mode,
            scan_schemes=_parse_schemes(args.scan_schemes),
            compare_schemes=_parse_schemes(args.compare_schemes),
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
            seed=args.seed,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 stage-7 overlap validation failed.', exc)
    return print_cli_summary('Z-Sim v1.0 stage-7 overlap validation complete.', summary, ordered_keys=('success', 'shape', 'scan_schemes', 'compare_schemes', 'num_scan_rows', 'num_scheme_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
