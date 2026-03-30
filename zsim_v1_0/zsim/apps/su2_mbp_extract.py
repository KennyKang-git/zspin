"""CLI for reduced MBP bilinear extraction in Z-Sim v1.0.

This app also supports Wilson-r sweeps and chirality comparison ledgers for
research calibration runs.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.bcc import build_bcc_supercell
from zsim.lgt.flow import cooling_trajectory
from zsim.lgt.loops import enumerate_bcc_rhombic_plaquettes
from zsim.lgt.mbp import extract_mbp_bilinear, mbp_prefactor
from zsim.lgt.su2_links import identity_links, random_su2_links
from zsim.lgt.valley import collective_valley_links


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Extract reduced MBP bilinear coefficients for Z-Sim v1.0.')
    parser.add_argument('--shape', default='2,2,2')
    parser.add_argument('--output-dir', default='outputs/su2_mbp_extract')
    parser.add_argument('--background', choices=('collective', 'cooled_random', 'identity'), default='collective')
    parser.add_argument('--amplitudes', default='-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75')
    parser.add_argument('--projector-mode', choices=('center', 'corner', 'positive_x', 'negative_x', 'all'), default='center')
    parser.add_argument('--chirality-mode', choices=('left', 'right', 'vector'), default='vector')
    parser.add_argument('--fermion-scheme', choices=('reduced2', 'staggered2', 'wilson4'), default='reduced2')
    parser.add_argument('--yt', type=float, default=1.0)
    parser.add_argument('--nc', type=float, default=3.0)
    parser.add_argument('--mass', type=float, default=0.0)
    parser.add_argument('--reg-epsilon', type=float, default=1e-6)
    parser.add_argument('--cutoff', type=float, default=1e-8)
    parser.add_argument('--fd-step', type=float, default=1e-3)
    parser.add_argument('--wilson-r', type=float, default=1.0)
    parser.add_argument('--wilson-r-grid', default='')
    parser.add_argument('--chirality-compare', default='')
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


def _parse_optional_floats(text: str) -> tuple[float, ...]:
    vals = [item.strip() for item in text.split(',') if item.strip()]
    return tuple(float(v) for v in vals)


def _parse_optional_strings(text: str) -> tuple[str, ...]:
    vals = [item.strip() for item in text.split(',') if item.strip()]
    return tuple(vals)


def _sign_match(trace_value: float, fd_value: float) -> bool:
    if abs(trace_value) <= 1e-15 or abs(fd_value) <= 1e-15:
        return True
    return (trace_value > 0.0) == (fd_value > 0.0)


def _recommendation_score(gap: float, sign_match: bool) -> float:
    return float(gap + (0.25 if not sign_match else 0.0))


def _build_links(background: str, lattice, amplitude: float, *, seed: int, cooling_steps: int, alpha: float):
    if background == 'collective':
        return collective_valley_links(lattice.edges, lattice.positions, amplitude)
    if background == 'identity':
        return identity_links(lattice.edges)
    base = random_su2_links(lattice.edges, seed=seed + int(round(1000.0 * amplitude)))
    plaquettes = enumerate_bcc_rhombic_plaquettes(lattice)
    cooled = cooling_trajectory(base, cooling_steps, plaquettes, alpha=alpha)
    return cooled[-1]


def _run_single_extract(*, lattice, background: str, amplitude: float, projector_mode: str, chirality_mode: str, fermion_scheme: str, yt: float, nc: float, mass: float, reg_epsilon: float, cutoff: float, fd_step: float, wilson_r: float, seed: int, cooling_steps: int, alpha: float) -> dict[str, object]:
    links = _build_links(background, lattice, float(amplitude), seed=seed, cooling_steps=cooling_steps, alpha=alpha)
    result = extract_mbp_bilinear(
        lattice,
        links,
        projector_mode=projector_mode,
        chirality_mode=chirality_mode,
        fermion_scheme=fermion_scheme,
        yt=yt,
        nc=nc,
        mass=mass,
        reg_epsilon=reg_epsilon,
        cutoff=cutoff,
        fd_step=fd_step,
        wilson_r=wilson_r,
    )
    row = {'amplitude': float(amplitude), **result.to_dict()}
    row['wilson_r'] = float(wilson_r)
    row['prefactor_exp_minus_2S'] = mbp_prefactor()
    row['mu2_with_prefactor'] = float(row['mu2_formula_proxy']) * float(row['prefactor_exp_minus_2S'])
    row['gamma_sign_match'] = _sign_match(float(row['gamma_h2_trace']), float(row['gamma_h2_fd']))
    row['recommendation_score'] = _recommendation_score(float(row['gamma_consistency_gap']), bool(row['gamma_sign_match']))
    return row


def _build_wilson_r_chirality_ledger(rows: Sequence[dict[str, object]]) -> tuple[list[dict[str, object]], dict[str, object]]:
    grouped: dict[tuple[str, float], list[dict[str, object]]] = {}
    for row in rows:
        key = (str(row['chirality_mode']), float(row['wilson_r']))
        grouped.setdefault(key, []).append(row)
    ledger: list[dict[str, object]] = []
    for (chirality_mode, wilson_r), subset in grouped.items():
        best_gap = min(subset, key=lambda item: abs(float(item['gamma_consistency_gap'])))
        strongest_mu2 = max(subset, key=lambda item: abs(float(item['mu2_formula_proxy'])))
        ledger.append({
            'chirality_mode': chirality_mode,
            'wilson_r': float(wilson_r),
            'num_rows': len(subset),
            'best_amplitude': float(best_gap['amplitude']),
            'gamma_consistency_gap': float(best_gap['gamma_consistency_gap']),
            'gamma_h2_trace': float(best_gap['gamma_h2_trace']),
            'gamma_h2_fd': float(best_gap['gamma_h2_fd']),
            'gamma_sign_match': bool(best_gap['gamma_sign_match']),
            'recommendation_score': float(best_gap['recommendation_score']),
            'mu2_formula_proxy': float(best_gap['mu2_formula_proxy']),
            'largest_mu2_amplitude': float(strongest_mu2['amplitude']),
            'largest_mu2_formula_proxy': float(strongest_mu2['mu2_formula_proxy']),
            'sigma_min': float(best_gap['sigma_min']),
            'sigma_next': float(best_gap['sigma_next']),
            'masked_modes': int(best_gap['masked_modes']),
        })
    ledger.sort(key=lambda item: (not bool(item['gamma_sign_match']), float(item['recommendation_score']), -abs(float(item['mu2_formula_proxy']))))
    recommended = ledger[0] if ledger else {}
    summary = {
        'num_combinations': len(ledger),
        'recommended_combination': recommended,
        'all_sign_matching': all(bool(item['gamma_sign_match']) for item in ledger) if ledger else False,
        'best_gap': float(recommended.get('gamma_consistency_gap', 0.0)) if recommended else None,
    }
    return ledger, summary


def run_su2_mbp_extract(*, shape: tuple[int, int, int] = (2, 2, 2), output_dir: str | Path = 'outputs/su2_mbp_extract', background: str = 'collective', amplitudes: Sequence[float] = (-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75), projector_mode: str = 'center', chirality_mode: str = 'vector', fermion_scheme: str = 'reduced2', yt: float = 1.0, nc: float = 3.0, mass: float = 0.0, reg_epsilon: float = 1e-6, cutoff: float = 1e-8, fd_step: float = 1e-3, wilson_r: float = 1.0, wilson_r_grid: Sequence[float] | None = None, chirality_compare: Sequence[str] | None = None, seed: int = 350437, cooling_steps: int = 10, alpha: float = 0.15) -> dict[str, object]:
    lattice = build_bcc_supercell(*shape)
    rows: list[dict[str, object]] = []
    for amplitude in amplitudes:
        rows.append(_run_single_extract(lattice=lattice, background=background, amplitude=float(amplitude), projector_mode=projector_mode, chirality_mode=chirality_mode, fermion_scheme=fermion_scheme, yt=yt, nc=nc, mass=mass, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step, wilson_r=wilson_r, seed=seed, cooling_steps=cooling_steps, alpha=alpha))

    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'mbp_extract_scan.csv', rows)
    best_gap = min(rows, key=lambda row: abs(float(row['gamma_consistency_gap'])))
    strongest_mu2 = max(rows, key=lambda row: abs(float(row['mu2_formula_proxy'])))

    generated_outputs = ['mbp_extract_scan.csv', 'mbp_extract_summary.json']
    payload: dict[str, object] = {
        'shape': list(shape),
        'background': background,
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'fermion_scheme': fermion_scheme,
        'num_rows': len(rows),
        'best_consistency_row': best_gap,
        'largest_mu2_row': strongest_mu2,
        'prefactor_exp_minus_2S': mbp_prefactor(),
        'notes': {
            'stage': 'reduced operator extractor',
            'status': 'surrogate',
            'non_claim': 'not a full caloron or production-lattice computation',
        },
    }

    if wilson_r_grid or chirality_compare:
        r_values = tuple(float(v) for v in (wilson_r_grid or (wilson_r,)))
        chirality_modes = tuple(str(v) for v in (chirality_compare or (chirality_mode,)))
        sweep_rows: list[dict[str, object]] = []
        for current_r in r_values:
            for current_chirality in chirality_modes:
                for amplitude in amplitudes:
                    sweep_rows.append(_run_single_extract(lattice=lattice, background=background, amplitude=float(amplitude), projector_mode=projector_mode, chirality_mode=current_chirality, fermion_scheme=fermion_scheme, yt=yt, nc=nc, mass=mass, reg_epsilon=reg_epsilon, cutoff=cutoff, fd_step=fd_step, wilson_r=float(current_r), seed=seed, cooling_steps=cooling_steps, alpha=alpha))
        write_csv_rows(out_dir / 'mbp_extract_wilson_r_chirality_scan.csv', sweep_rows)
        ledger, ledger_summary = _build_wilson_r_chirality_ledger(sweep_rows)
        write_csv_rows(out_dir / 'mbp_extract_wilson_r_chirality_ledger.csv', ledger)
        payload['wilson_r_grid'] = list(r_values)
        payload['chirality_compare'] = list(chirality_modes)
        payload['wilson_r_chirality_ledger_summary'] = ledger_summary
        generated_outputs.extend(['mbp_extract_wilson_r_chirality_scan.csv', 'mbp_extract_wilson_r_chirality_ledger.csv'])

    write_json(out_dir / 'mbp_extract_summary.json', payload)
    return {
        'success': True,
        'shape': shape,
        'background': background,
        'projector_mode': projector_mode,
        'chirality_mode': chirality_mode,
        'fermion_scheme': fermion_scheme,
        'wilson_r': float(wilson_r),
        'wilson_r_grid': list(wilson_r_grid) if wilson_r_grid else [],
        'chirality_compare': list(chirality_compare) if chirality_compare else [],
        'num_rows': len(rows),
        'output_dir': str(out_dir),
        'generated_outputs': generated_outputs,
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_extract(
            shape=_parse_shape(args.shape),
            output_dir=args.output_dir,
            background=args.background,
            amplitudes=_parse_amplitudes(args.amplitudes),
            projector_mode=args.projector_mode,
            chirality_mode=args.chirality_mode,
            fermion_scheme=args.fermion_scheme,
            yt=args.yt,
            nc=args.nc,
            mass=args.mass,
            reg_epsilon=args.reg_epsilon,
            cutoff=args.cutoff,
            fd_step=args.fd_step,
            wilson_r=args.wilson_r,
            wilson_r_grid=_parse_optional_floats(args.wilson_r_grid),
            chirality_compare=_parse_optional_strings(args.chirality_compare),
            seed=args.seed,
            cooling_steps=args.cooling_steps,
            alpha=args.alpha,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 MBP extraction failed.', exc)
    return print_cli_summary('Z-Sim v1.0 MBP extraction complete.', summary, ordered_keys=('success', 'shape', 'background', 'projector_mode', 'chirality_mode', 'fermion_scheme', 'wilson_r', 'num_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
