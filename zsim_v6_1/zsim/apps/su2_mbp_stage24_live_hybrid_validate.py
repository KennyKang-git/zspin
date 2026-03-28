from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage24 import run_stage24_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-24 live-hybrid sweep validation harness for Z-Sim v5.5.')
    p.add_argument('--reference-stage23-summary', default='outputs/su2_mbp_stage23_hybrid_recompute_example/stage23_summary.json')
    p.add_argument('--reference-stage22-summary', default='outputs/su2_mbp_stage22_recompute_bridge_example/stage22_summary.json')
    p.add_argument('--reference-stage20-summary', default='outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage24_live_hybrid_example')
    return p


def run_su2_mbp_stage24_live_hybrid_validate(
    *,
    reference_stage23_summary: str | Path = 'outputs/su2_mbp_stage23_hybrid_recompute_example/stage23_summary.json',
    reference_stage22_summary: str | Path = 'outputs/su2_mbp_stage22_recompute_bridge_example/stage22_summary.json',
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
    output_dir: str | Path = 'outputs/su2_mbp_stage24_live_hybrid_example',
) -> dict[str, object]:
    summary, payload = run_stage24_pipeline(
        reference_stage23_summary=reference_stage23_summary,
        reference_stage22_summary=reference_stage22_summary,
        reference_stage20_summary=reference_stage20_summary,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage24_live_rows.csv', [row.to_dict() for row in summary.sweep_rows])
    write_csv_rows(out_dir / 'stage24_control_rows.csv', [row.to_dict() for row in summary.sweep_rows if row.is_control])
    write_json(out_dir / 'stage24_summary.json', payload)
    return {
        'success': True,
        'selected_source_label': summary.selected_source_label,
        'selected_sign_method': summary.selected_sign_method,
        'selected_scheme': summary.selected_scheme,
        'selected_shape': list(summary.selected_shape),
        'output_dir': str(out_dir),
        'gates': payload['gates'],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = run_su2_mbp_stage24_live_hybrid_validate(
            reference_stage23_summary=args.reference_stage23_summary,
            reference_stage22_summary=args.reference_stage22_summary,
            reference_stage20_summary=args.reference_stage20_summary,
            output_dir=args.output_dir,
        )
    except Exception as exc:  # pragma: no cover
        print_cli_failure('su2_mbp_stage24_live_hybrid_validate', exc)
        return 1
    print_cli_summary('su2_mbp_stage24_live_hybrid_validate', result)
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
