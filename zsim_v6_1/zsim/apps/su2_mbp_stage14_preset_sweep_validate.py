from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage14 import run_stage14_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-14 preset-sweep stability validation for Z-Sim v4.5.')
    p.add_argument('--reference-stage13-summary', default='outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json')
    p.add_argument('--default-broad-shape-grid', default='1,1,1;2,1,1;2,2,1;2,2,2;3,2,1;3,2,2;3,3,1')
    p.add_argument('--expanded-broad-shape-grid', default='1,1,1;2,1,1;2,2,1;2,2,2;3,2,1;3,2,2;3,3,1;4,2,1;4,3,1')
    p.add_argument('--larger-shape-sweep-grid', default='1,1,1;2,1,1;2,2,1;2,2,2;3,2,1;3,2,2;3,3,1;4,2,1;4,3,1;4,2,2;4,3,2;4,4,1')
    p.add_argument('--lightweight-shape-grid', default='1,1,1;2,1,1;2,2,1')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage14_preset_sweep_validate')
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


def run_su2_mbp_stage14_preset_sweep_validate(
    *,
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
    default_broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1)),
    expanded_broad_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1), (4, 2, 1), (4, 3, 1)),
    larger_shape_sweep_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1), (2, 2, 2), (3, 2, 1), (3, 2, 2), (3, 3, 1), (4, 2, 1), (4, 3, 1), (4, 2, 2), (4, 3, 2), (4, 4, 1)),
    lightweight_shape_grid: Sequence[tuple[int, int, int]] = ((1, 1, 1), (2, 1, 1), (2, 2, 1)),
    output_dir: str | Path = 'outputs/su2_mbp_stage14_preset_sweep_validate',
) -> dict[str, object]:
    summary, payload = run_stage14_pipeline(
        reference_stage13_summary=reference_stage13_summary,
        default_broad_shape_grid=default_broad_shape_grid,
        expanded_broad_shape_grid=expanded_broad_shape_grid,
        larger_shape_sweep_grid=larger_shape_sweep_grid,
        lightweight_shape_grid=lightweight_shape_grid,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage14_sweep_rows.csv', [r.to_dict() for r in summary.sweep_rows])
    write_csv_rows(out_dir / 'stage14_stability_rows.csv', [r.to_dict() for r in summary.stability_rows])
    write_json(out_dir / 'stage14_summary.json', payload)
    return {
        'success': True,
        'reference_stage13_summary': str(reference_stage13_summary),
        'default_broad_shape_grid': tuple(default_broad_shape_grid),
        'expanded_broad_shape_grid': tuple(expanded_broad_shape_grid),
        'larger_shape_sweep_grid': tuple(larger_shape_sweep_grid),
        'lightweight_shape_grid': tuple(lightweight_shape_grid),
        'selected_shape': summary.selected_shape,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'selected_source_label': summary.selected_source_label,
        'num_sweep_rows': len(summary.sweep_rows),
        'num_stability_rows': len(summary.stability_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage14_sweep_rows.csv', 'stage14_stability_rows.csv', 'stage14_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage14_preset_sweep_validate(
            reference_stage13_summary=args.reference_stage13_summary,
            default_broad_shape_grid=_parse_shape_grid(args.default_broad_shape_grid),
            expanded_broad_shape_grid=_parse_shape_grid(args.expanded_broad_shape_grid),
            larger_shape_sweep_grid=_parse_shape_grid(args.larger_shape_sweep_grid),
            lightweight_shape_grid=_parse_shape_grid(args.lightweight_shape_grid),
            output_dir=args.output_dir,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v4.5 stage-14 preset-sweep stability validation failed.', exc)
    return print_cli_summary('Z-Sim v4.5 stage-14 preset-sweep stability validation complete.', summary, ordered_keys=('success', 'reference_stage13_summary', 'default_broad_shape_grid', 'expanded_broad_shape_grid', 'larger_shape_sweep_grid', 'lightweight_shape_grid', 'selected_shape', 'selected_sign_method', 'selected_scheme', 'selected_source_label', 'num_sweep_rows', 'num_stability_rows', 'output_dir'))


if __name__ == '__main__':
    raise SystemExit(main())
