from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage19 import run_stage19_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-19 recompute-aware control sweep validation harness for Z-Sim v5.0.')
    p.add_argument('--reference-stage18-summary', default='outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json')
    p.add_argument('--reference-stage17-summary', default='outputs/su2_mbp_stage17_live_stress_example/stage17_summary.json')
    p.add_argument('--reference-stage16-summary', default='outputs/su2_mbp_stage16_live_recompute_example/stage16_summary.json')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage19_recompute_control_example')
    return p


def run_su2_mbp_stage19_recompute_control_validate(
    *,
    reference_stage18_summary: str | Path = 'outputs/su2_mbp_stage18_hybrid_live_stress_example/stage18_summary.json',
    reference_stage17_summary: str | Path = 'outputs/su2_mbp_stage17_live_stress_example/stage17_summary.json',
    reference_stage16_summary: str | Path = 'outputs/su2_mbp_stage16_live_recompute_example/stage16_summary.json',
    output_dir: str | Path = 'outputs/su2_mbp_stage19_recompute_control_example',
) -> dict[str, object]:
    summary, payload = run_stage19_pipeline(
        reference_stage18_summary=reference_stage18_summary,
        reference_stage17_summary=reference_stage17_summary,
        reference_stage16_summary=reference_stage16_summary,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage19_sweep_rows.csv', [r.to_dict() for r in summary.sweep_rows])
    write_csv_rows(out_dir / 'stage19_control_family_rows.csv', [r.to_dict() for r in summary.sweep_rows if r.is_control])
    write_json(out_dir / 'stage19_summary.json', payload)
    return {
        'success': True,
        'reference_stage18_summary': str(reference_stage18_summary),
        'reference_stage17_summary': str(reference_stage17_summary),
        'reference_stage16_summary': str(reference_stage16_summary),
        'selected_shape': summary.selected_shape,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'selected_source_label': summary.selected_source_label,
        'num_sweep_rows': len(summary.sweep_rows),
        'output_dir': str(out_dir),
        'generated_outputs': ['stage19_sweep_rows.csv', 'stage19_control_family_rows.csv', 'stage19_summary.json'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    try:
        summary = run_su2_mbp_stage19_recompute_control_validate(
            reference_stage18_summary=args.reference_stage18_summary,
            reference_stage17_summary=args.reference_stage17_summary,
            reference_stage16_summary=args.reference_stage16_summary,
            output_dir=args.output_dir,
        )
    except Exception as exc:
        return print_cli_failure('Z-Sim v5.0 stage-19 recompute-aware control sweep validation failed.', exc)
    return print_cli_summary(
        'Z-Sim v5.0 stage-19 recompute-aware control sweep validation complete.',
        summary,
        ordered_keys=(
            'success',
            'reference_stage18_summary',
            'reference_stage17_summary',
            'reference_stage16_summary',
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
