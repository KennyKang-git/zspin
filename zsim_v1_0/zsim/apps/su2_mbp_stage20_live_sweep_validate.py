from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage20 import run_stage20_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-20 live sweep expansion validation harness for Z-Sim v1.0.')
    p.add_argument('--reference-stage19-summary', default='outputs/su2_mbp_stage19_recompute_control_example/stage19_summary.json')
    p.add_argument('--reference-stage18-summary', default='outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json')
    p.add_argument('--broad-shape-grid', default='1,1,1;2,1,1;2,2,1;2,2,2')
    p.add_argument('--lightweight-shape-grid', default='1,1,1;2,1,1')
    p.add_argument('--sign-methods', default='smooth,tanh,rational')
    p.add_argument('--amplitudes', default='0.35,0.55')
    p.add_argument('--separations', default='0.55,0.75')
    p.add_argument('--widths', default='0.45')
    p.add_argument('--seam-biases', default='0.10,0.18')
    p.add_argument('--sign-epsilon-grid', default='1e-5')
    p.add_argument('--fd-scale-grid', default='1.0')
    p.add_argument('--pair-count', type=int, default=1)
    p.add_argument('--sample-size', type=int, default=4)
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage20_live_sweep_example')
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


def run_su2_mbp_stage20_live_sweep_validate(
    *,
    reference_stage19_summary: str | Path = 'outputs/su2_mbp_stage19_recompute_control_example/stage19_summary.json',
    reference_stage18_summary: str | Path = 'outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json',
    broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2)),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1)),
    sign_methods: Sequence[str] = ('smooth', 'tanh', 'rational'),
    amplitudes: Sequence[float] = (0.35, 0.55),
    separations: Sequence[float] = (0.55, 0.75),
    widths: Sequence[float] = (0.45,),
    seam_biases: Sequence[float] = (0.10, 0.18),
    sign_epsilon_grid: Sequence[float] = (1e-5,),
    fd_scale_grid: Sequence[float] = (1.0,),
    pair_count: int = 1,
    sample_size: int = 4,
    output_dir: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example',
) -> dict[str, object]:
    summary, payload = run_stage20_pipeline(
        reference_stage19_summary=reference_stage19_summary,
        reference_stage18_summary=reference_stage18_summary,
        broad_shape_grid=broad_shape_grid,
        lightweight_shape_grid=lightweight_shape_grid,
        sign_methods=sign_methods,
        amplitudes=amplitudes,
        separations=separations,
        widths=widths,
        seam_biases=seam_biases,
        sign_epsilon_grid=sign_epsilon_grid,
        fd_scale_grid=fd_scale_grid,
        pair_count=pair_count,
        sample_size=sample_size,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage20_live_rows.csv', [r.to_dict() for r in summary.sweep_rows])
    write_csv_rows(out_dir / 'stage20_control_rows.csv', [r.to_dict() for r in summary.sweep_rows if r.is_control])
    write_json(out_dir / 'stage20_summary.json', payload)
    return {
        'success': True,
        'reference_stage19_summary': str(reference_stage19_summary),
        'reference_stage18_summary': str(reference_stage18_summary),
        'selected_shape': summary.selected_shape,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'selected_source_label': summary.selected_source_label,
        'num_sweep_rows': len(summary.sweep_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage20_live_rows.csv', 'stage20_control_rows.csv', 'stage20_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage20_live_sweep_validate(
            reference_stage19_summary=args.reference_stage19_summary,
            reference_stage18_summary=args.reference_stage18_summary,
            broad_shape_grid=_parse_shape_grid(args.broad_shape_grid),
            lightweight_shape_grid=_parse_shape_grid(args.lightweight_shape_grid),
            sign_methods=_parse_list(args.sign_methods),
            amplitudes=_parse_floats(args.amplitudes),
            separations=_parse_floats(args.separations),
            widths=_parse_floats(args.widths),
            seam_biases=_parse_floats(args.seam_biases),
            sign_epsilon_grid=_parse_floats(args.sign_epsilon_grid),
            fd_scale_grid=_parse_floats(args.fd_scale_grid),
            pair_count=args.pair_count,
            sample_size=args.sample_size,
            output_dir=args.output_dir,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 stage-20 live sweep expansion validation failed.', exc)
    return print_cli_summary(
        'Z-Sim v1.0 stage-20 live sweep expansion validation complete.',
        summary,
        ordered_keys=(
            'success',
            'reference_stage19_summary',
            'reference_stage18_summary',
            'selected_shape',
            'selected_sign_method',
            'selected_scheme',
            'selected_source_label',
            'num_sweep_rows',
            'output_dir',
        ),
    )


if __name__ == '__main__':
    raise SystemExit(main())
