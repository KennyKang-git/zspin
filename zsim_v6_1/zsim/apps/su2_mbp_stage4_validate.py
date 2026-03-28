"""CLI for stage-4 chiral/caloron MBP validation in Z-Sim v3.5."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.backgrounds import caloron_pair_links
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.controls import run_negative_controls
from zsim.lgt.flow import cooling_trajectory
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear, mbp_prefactor
from zsim.lgt.su2_links import identity_links, random_su2_links
from zsim.lgt.valley import collective_valley_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Run stage-4 chiral/caloron MBP validation for Z-Sim v3.5.')
    parser.add_argument('--shape', default='2,2,2')
    parser.add_argument('--output-dir', default='outputs/su2_mbp_stage4_validate')
    parser.add_argument('--background', choices=('caloron', 'collective', 'cooled_random', 'identity'), default='caloron')
    parser.add_argument('--amplitudes', default='-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75')
    parser.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    parser.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='left')
    parser.add_argument('--yt', type=float, default=1.0)
    parser.add_argument('--nc', type=float, default=3.0)
    parser.add_argument('--mass', type=float, default=0.0)
    parser.add_argument('--reg-epsilon', type=float, default=1e-6)
    parser.add_argument('--cutoff', type=float, default=1e-8)
    parser.add_argument('--fd-step', type=float, default=1e-3)
    parser.add_argument('--seed', type=int, default=350437)
    parser.add_argument('--cooling-steps', type=int, default=10)
    parser.add_argument('--alpha', type=float, default=0.15)
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


def _build_links(background: str, lattice, amplitude: float, *, seed: int, cooling_steps: int, alpha: float):
    if background == 'caloron':
        return caloron_pair_links(lattice.edges, lattice.positions, amplitude)
    if background == 'collective':
        return collective_valley_links(lattice.edges, lattice.positions, amplitude)
    if background == 'identity':
        return identity_links(lattice.edges)
    base = random_su2_links(lattice.edges, seed=seed + int(round(1000.0 * amplitude)))
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    cooled = cooling_trajectory(base, cooling_steps, plaquettes, alpha=alpha)
    return cooled[-1]


def run_su2_mbp_stage4_validate(*, shape: tuple[int, int, int] = (2, 2, 2), output_dir: str | Path = 'outputs/su2_mbp_stage4_validate', background: str = 'caloron', amplitudes: Sequence[float] = (-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75), projector_mode: str = 'center', chirality_mode: str = 'left', yt: float = 1.0, nc: float = 3.0, mass: float = 0.0, reg_epsilon: float = 1e-6, cutoff: float = 1e-8, fd_step: float = 1e-3, seed: int = 350437, cooling_steps: int = 10, alpha: float = 0.15) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    rows = []
    cached = {}
    for amplitude in amplitudes:
        links = _build_links(background, lattice, float(amplitude), seed=seed, cooling_steps=cooling_steps, alpha=alpha)
        cached[float(amplitude)] = links
        result = extract_mbp_bilinear(lattice, links, projector_mode=projector_mode, chirality_mode=chirality_mode, yt=yt, nc=nc, mass=mass, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step)
        row = {'amplitude': float(amplitude), **result.to_dict()}
        row['prefactor_exp_minus_2S'] = mbp_prefactor()
        row['mu2_with_prefactor'] = float(row['mu2_formula_proxy']) * float(row['prefactor_exp_minus_2S'])
        rows.append(row)
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'mbp_stage4_scan.csv', rows)
    best_gap = min(rows, key=lambda row: abs(float(row['gamma_consistency_gap'])))
    strongest = max(rows, key=lambda row: abs(float(row['mu2_formula_proxy'])))
    base_amp = float(strongest['amplitude'])
    controls = run_negative_controls(
        lattice,
        cached[base_amp],
        amplitude=base_amp,
        yt=yt,
        nc=nc,
        mass=mass,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        seed=seed,
    )
    partner_mode = 'right' if chirality_mode == 'left' else 'left'
    partner = extract_mbp_bilinear(
        lattice,
        cached[base_amp],
        projector_mode=projector_mode,
        chirality_mode=partner_mode,
        yt=yt,
        nc=nc,
        mass=mass,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
    )
    gates = {
        'G-CONSISTENCY': float(best_gap['gamma_consistency_gap']) < 5.0e-2,
        'G-CHIRAL-SPLIT': abs(float(strongest['mu2_formula_proxy']) - float(partner.mu2_formula_proxy)) > 1.0e-6,
        'G-CONTROL-SEPARATION': abs(float(strongest['mu2_formula_proxy']) - float(controls['scrambled_caloron']['mu2_formula_proxy'])) > 1.0e-6,
    }
    write_json(out_dir / 'mbp_stage4_summary.json', {
        'shape': list(shape),
        'background': background,
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'num_rows': len(rows),
        'best_consistency_row': best_gap,
        'largest_mu2_row': strongest,
        'negative_controls': controls,
        'partner_chirality_row': partner.to_dict(),
        'gates': gates,
        'prefactor_exp_minus_2S': mbp_prefactor(),
        'notes': {
            'stage': 'chiral-caloron preproduction surrogate',
            'status': 'preproduction-surrogate',
            'non_claim': 'not a continuum caloron or production-scale lattice result',
        },
    })
    return {
        'success': True,
        'shape': shape,
        'background': background,
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'num_rows': len(rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['mbp_stage4_scan.csv', 'mbp_stage4_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage4_validate(
            shape=_parse_shape(args.shape),
            output_dir=args.output_dir,
            background=args.background,
            amplitudes=_parse_amplitudes(args.amplitudes),
            projector_mode=args.projector_mode,
            chirality_mode=args.chirality_mode,
            yt=args.yt,
            nc=args.nc,
            mass=args.mass,
            reg_epsilon=args.reg_epsilon,
            cutoff=args.cutoff,
            fd_step=args.fd_step,
            seed=args.seed,
            cooling_steps=args.cooling_steps,
            alpha=args.alpha,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v3.5 stage-4 MBP validation failed.', exc)
    return print_cli_summary('Z-Sim v3.5 stage-4 MBP validation complete.', summary, ordered_keys=('success', 'shape', 'background', 'projector_mode', 'chirality_mode', 'num_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
