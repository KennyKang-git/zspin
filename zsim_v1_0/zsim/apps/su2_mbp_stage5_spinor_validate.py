from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.controls import run_negative_controls
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear, mbp_prefactor
from zsim.lgt.valley_fit import fit_caloron_valley_family
from zsim.lgt.wilson import plaquette_observables


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run stage-5 Wilson/staggered spinor MBP validation for Z-Sim v1.0.')
    p.add_argument('--shape', default='2,2,2')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage5_spinor_validate')
    p.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    p.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='left')
    p.add_argument('--fermion-scheme', choices=('wilson4', 'staggered2', 'reduced2'), default='wilson4')
    p.add_argument('--amplitudes', default='0.25,0.5,0.75,1.0')
    p.add_argument('--separations', default='0.55,0.75,0.95')
    p.add_argument('--widths', default='0.45,0.60,0.80')
    p.add_argument('--seam-biases', default='0.10,0.15,0.25')
    p.add_argument('--yt', type=float, default=1.0)
    p.add_argument('--nc', type=float, default=3.0)
    p.add_argument('--mass', type=float, default=0.15)
    p.add_argument('--kappa', type=float, default=0.6)
    p.add_argument('--wilson-r', type=float, default=1.0)
    p.add_argument('--reg-epsilon', type=float, default=1e-4)
    p.add_argument('--cutoff', type=float, default=1e-6)
    p.add_argument('--fd-step', type=float, default=5e-4)
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


def run_su2_mbp_stage5_spinor_validate(*, shape: tuple[int, int, int] = (2, 2, 2), output_dir: str | Path = 'outputs/su2_mbp_stage5_spinor_validate', projector_mode: str = 'center', chirality_mode: str = 'left', fermion_scheme: str = 'wilson4', amplitudes: Sequence[float] = (0.25, 0.5, 0.75, 1.0), separations: Sequence[float] = (0.55, 0.75, 0.95), widths: Sequence[float] = (0.45, 0.60, 0.80), seam_biases: Sequence[float] = (0.10, 0.15, 0.25), yt: float = 1.0, nc: float = 3.0, mass: float = 0.15, kappa: float = 0.6, wilson_r: float = 1.0, reg_epsilon: float = 1e-4, cutoff: float = 1e-6, fd_step: float = 5e-4, seed: int = 350437) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    best, best_links, fit_rows = fit_caloron_valley_family(lattice, amplitude_grid=amplitudes, separation_grid=separations, width_grid=widths, seam_bias_grid=seam_biases, mass=mass)
    main = extract_mbp_bilinear(lattice, best_links, projector_mode=projector_mode, chirality_mode=chirality_mode, fermion_scheme=fermion_scheme, yt=yt, nc=nc, mass=mass, kappa=kappa, wilson_r=wilson_r, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step)
    partner = extract_mbp_bilinear(lattice, best_links, projector_mode=projector_mode, chirality_mode='right' if chirality_mode == 'left' else 'left', fermion_scheme=fermion_scheme, yt=yt, nc=nc, mass=mass, kappa=kappa, wilson_r=wilson_r, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step)
    staggered_ref = extract_mbp_bilinear(lattice, best_links, projector_mode=projector_mode, chirality_mode=chirality_mode, fermion_scheme='staggered2', yt=yt, nc=nc, mass=mass, kappa=kappa, wilson_r=wilson_r, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step)
    controls = run_negative_controls(lattice, best_links, amplitude=best.amplitude, yt=yt, nc=nc, mass=mass, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step, seed=seed, fermion_scheme=fermion_scheme, kappa=kappa, wilson_r=wilson_r)
    plaq = plaquette_observables(best_links, enumerate_bcc_rhombic_plaquettes(lattice))
    gates = {
        'G-TRACE-FD': float(main.gamma_consistency_gap) < 1.0e-1,
        'G-CHIRAL-SPLIT': abs(float(main.mu2_formula_proxy) - float(partner.mu2_formula_proxy)) > 1.0e-6,
        'G-SCHEME-DIFFERENCE': abs(float(main.mu2_formula_proxy) - float(staggered_ref.mu2_formula_proxy)) > 1.0e-6,
        'G-FIT-LOCALIZATION': float(best.score) > 0.0,
        'G-CONTROL-SEPARATION': abs(float(main.mu2_formula_proxy) - float(controls['scrambled_caloron']['mu2_formula_proxy'])) > 1.0e-6,
    }
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage5_valley_fit_grid.csv', [row.to_dict() for row in fit_rows])
    write_csv_rows(out_dir / 'stage5_mbp_rows.csv', [main.to_dict(), partner.to_dict(), staggered_ref.to_dict()])
    write_json(out_dir / 'stage5_spinor_summary.json', {
        'shape': list(shape), 'projector_mode': projector_mode, 'chirality_mode': chirality_mode, 'fermion_scheme': fermion_scheme,
        'fit_best': best.to_dict(), 'main_row': main.to_dict(), 'partner_chirality_row': partner.to_dict(), 'staggered_reference_row': staggered_ref.to_dict(),
        'negative_controls': controls, 'plaquette_observables': plaq, 'prefactor_exp_minus_2S': mbp_prefactor(), 'mu2_with_prefactor': main.mu2_formula_proxy * mbp_prefactor(),
        'gates': gates,
        'notes': {'stage': 'spinor-block valley-fit preproduction surrogate', 'status': 'preproduction-surrogate', 'non_claim': 'not a continuum caloron, not a production-scale lattice, not final EWSB closure'},
    })
    return {'success': True, 'shape': shape, 'projector_mode': projector_mode, 'chirality_mode': chirality_mode, 'fermion_scheme': fermion_scheme, 'num_fit_rows': len(fit_rows), 'output_dir': str(out_dir), 'generated_outputs': ['stage5_valley_fit_grid.csv', 'stage5_mbp_rows.csv', 'stage5_spinor_summary.json']}


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage5_spinor_validate(shape=_parse_shape(args.shape), output_dir=args.output_dir, projector_mode=args.projector_mode, chirality_mode=args.chirality_mode, fermion_scheme=args.fermion_scheme, amplitudes=_parse_floats(args.amplitudes), separations=_parse_floats(args.separations), widths=_parse_floats(args.widths), seam_biases=_parse_floats(args.seam_biases), yt=args.yt, nc=args.nc, mass=args.mass, kappa=args.kappa, wilson_r=args.wilson_r, reg_epsilon=args.reg_epsilon, cutoff=args.cutoff, fd_step=args.fd_step, seed=args.seed)
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 stage-5 spinor/valley validation failed.', exc)
    return print_cli_summary('Z-Sim v1.0 stage-5 spinor/valley validation complete.', summary, ordered_keys=('success', 'shape', 'projector_mode', 'chirality_mode', 'fermion_scheme', 'num_fit_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
