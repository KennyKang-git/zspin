from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage26 import run_stage26_pipeline


def _parse_shapes(text: str) -> tuple[tuple[int, int, int], ...]:
    shapes = []
    for chunk in text.split(';'):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = [int(v.strip()) for v in chunk.split(',') if v.strip()]
        if len(parts) != 3:
            raise ValueError('each shape must be nx,ny,nz')
        shapes.append((parts[0], parts[1], parts[2]))
    if not shapes:
        raise ValueError('at least one shape is required')
    return tuple(shapes)


def _parse_floats(text: str) -> tuple[float, ...]:
    vals = [float(v.strip()) for v in text.split(',') if v.strip()]
    if not vals:
        raise ValueError('at least one float value is required')
    return tuple(vals)


def _parse_strings(text: str) -> tuple[str, ...]:
    vals = [v.strip() for v in text.split(',') if v.strip()]
    if not vals:
        raise ValueError('at least one string value is required')
    return tuple(vals)


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-26 shape-adaptive MBP validation harness for Z-Sim v5.7.')
    p.add_argument('--reference-stage25-summary', default='outputs/su2_mbp_stage25_heavier_live_hybrid_example/stage25_summary.json')
    p.add_argument('--shape-grid', default='4,4,4;6,4,4;6,6,4;8,6,4;8,8,4;8,10,4')
    p.add_argument('--background', choices=('collective', 'cooled_random', 'identity'), default='cooled_random')
    p.add_argument('--amplitudes', default='-0.75,-0.5,-0.25,0.0,0.25,0.5,0.75')
    p.add_argument('--fermion-scheme', choices=('reduced2', 'staggered2', 'wilson4'), default='wilson4')
    p.add_argument('--fixed-chirality-mode', choices=('left', 'right', 'vector'), default='left')
    p.add_argument('--fixed-wilson-r', type=float, default=0.5)
    p.add_argument('--adaptive-chirality-modes', default='left,right,vector')
    p.add_argument('--adaptive-wilson-r-grid', default='0.25,0.5,0.75,1.0,1.25')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage26_shape_adaptive_example')
    return p


def run_su2_mbp_stage26_shape_adaptive_validate(
    *,
    reference_stage25_summary: str | Path = 'outputs/su2_mbp_stage25_heavier_live_hybrid_example/stage25_summary.json',
    shape_grid: Sequence[tuple[int, int, int]] = ((4, 4, 4), (6, 4, 4), (6, 6, 4), (8, 6, 4), (8, 8, 4), (8, 10, 4)),
    background: str = 'cooled_random',
    amplitudes: Sequence[float] = (-0.75, -0.5, -0.25, 0.0, 0.25, 0.5, 0.75),
    fermion_scheme: str = 'wilson4',
    fixed_chirality_mode: str = 'left',
    fixed_wilson_r: float = 0.5,
    adaptive_chirality_modes: Sequence[str] = ('left', 'right', 'vector'),
    adaptive_wilson_r_grid: Sequence[float] = (0.25, 0.5, 0.75, 1.0, 1.25),
    output_dir: str | Path = 'outputs/su2_mbp_stage26_shape_adaptive_example',
) -> dict[str, object]:
    summary, payload = run_stage26_pipeline(
        reference_stage25_summary=reference_stage25_summary,
        shape_grid=shape_grid,
        background=background,
        amplitudes=amplitudes,
        fermion_scheme=fermion_scheme,
        fixed_chirality_mode=fixed_chirality_mode,
        fixed_wilson_r=fixed_wilson_r,
        adaptive_chirality_modes=adaptive_chirality_modes,
        adaptive_wilson_r_grid=adaptive_wilson_r_grid,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage26_shape_rows.csv', [row.to_dict() for row in summary.shape_rows])
    write_csv_rows(out_dir / 'stage26_adaptive_rows.csv', [row.to_dict() for row in summary.shape_rows if row.winner_mode == 'shape_adaptive_winner'])
    write_json(out_dir / 'stage26_summary.json', payload)
    return {
        'success': True,
        'selected_source_label': summary.selected_source_label,
        'selected_shape': list(summary.selected_shape),
        'selected_scheme': summary.selected_scheme,
        'selected_chirality_mode': summary.selected_chirality_mode,
        'selected_wilson_r': summary.selected_wilson_r,
        'selected_sign_match': summary.selected_sign_match,
        'output_dir': str(out_dir),
        'gates': payload['gates'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = run_su2_mbp_stage26_shape_adaptive_validate(
            reference_stage25_summary=args.reference_stage25_summary,
            shape_grid=_parse_shapes(args.shape_grid),
            background=args.background,
            amplitudes=_parse_floats(args.amplitudes),
            fermion_scheme=args.fermion_scheme,
            fixed_chirality_mode=args.fixed_chirality_mode,
            fixed_wilson_r=args.fixed_wilson_r,
            adaptive_chirality_modes=_parse_strings(args.adaptive_chirality_modes),
            adaptive_wilson_r_grid=_parse_floats(args.adaptive_wilson_r_grid),
            output_dir=args.output_dir,
        )
    except Exception as exc:  # pragma: no cover
        print_cli_failure('su2_mbp_stage26_shape_adaptive_validate', exc)
        return 1
    print_cli_summary('su2_mbp_stage26_shape_adaptive_validate', result)
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
