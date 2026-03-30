from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage15 import run_stage15_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-15 recompute-aware validation harness for Z-Sim v1.0.')
    p.add_argument('--reference-stage14-summary', default='outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json')
    p.add_argument('--reference-stage13-summary', default='outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage15_recompute_example')
    return p


def run_su2_mbp_stage15_recompute_validate(
    *,
    reference_stage14_summary: str | Path = 'outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json',
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
    output_dir: str | Path = 'outputs/su2_mbp_stage15_recompute_example',
) -> dict[str, object]:
    summary, payload = run_stage15_pipeline(
        reference_stage14_summary=reference_stage14_summary,
        reference_stage13_summary=reference_stage13_summary,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage15_recompute_rows.csv', [r.to_dict() for r in summary.recompute_rows])
    write_csv_rows(out_dir / 'stage15_bridge_rows.csv', [r.to_dict() for r in summary.bridge_rows])
    write_json(out_dir / 'stage15_summary.json', payload)
    return {
        'success': True,
        'reference_stage14_summary': str(reference_stage14_summary),
        'reference_stage13_summary': str(reference_stage13_summary),
        'selected_shape': summary.selected_shape,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'selected_source_label': summary.selected_source_label,
        'num_recompute_rows': len(summary.recompute_rows),
        'num_bridge_rows': len(summary.bridge_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage15_recompute_rows.csv', 'stage15_bridge_rows.csv', 'stage15_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage15_recompute_validate(
            reference_stage14_summary=args.reference_stage14_summary,
            reference_stage13_summary=args.reference_stage13_summary,
            output_dir=args.output_dir,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v1.0 stage-15 recompute-aware validation failed.', exc)
    return print_cli_summary(
        'Z-Sim v1.0 stage-15 recompute-aware validation complete.',
        summary,
        ordered_keys=(
            'success',
            'reference_stage14_summary',
            'reference_stage13_summary',
            'selected_shape',
            'selected_sign_method',
            'selected_scheme',
            'selected_source_label',
            'num_recompute_rows',
            'num_bridge_rows',
            'output_dir',
        ),
    )


if __name__ == '__main__':
    raise SystemExit(main())
