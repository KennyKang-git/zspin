from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io.serialize import ensure_output_dir, write_csv_rows, write_json
from zsim.lgt.stage21 import run_stage21_pipeline


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description='Run the stage-21 broader-default live bridge validation harness for Z-Sim v5.2.')
    p.add_argument('--reference-stage20-summary', default='outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json')
    p.add_argument('--reference-stage13-summary', default='outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json')
    p.add_argument('--reference-stage14-summary', default='outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json')
    p.add_argument('--output-dir', default='outputs/su2_mbp_stage21_default_live_example')
    return p


def run_su2_mbp_stage21_default_live_validate(
    *,
    reference_stage20_summary: str | Path = 'outputs/su2_mbp_stage20_live_sweep_example/stage20_summary.json',
    reference_stage13_summary: str | Path = 'outputs/su2_mbp_stage13_broad_compare_example/stage13_summary.json',
    reference_stage14_summary: str | Path = 'outputs/su2_mbp_stage14_preset_sweep_example/stage14_summary.json',
    output_dir: str | Path = 'outputs/su2_mbp_stage21_default_live_example',
) -> dict[str, object]:
    summary, payload = run_stage21_pipeline(
        reference_stage20_summary=reference_stage20_summary,
        reference_stage13_summary=reference_stage13_summary,
        reference_stage14_summary=reference_stage14_summary,
    )
    out_dir = ensure_output_dir(output_dir)
    write_csv_rows(out_dir / 'stage21_live_rows.csv', [row.to_dict() for row in summary.sweep_rows])
    write_csv_rows(out_dir / 'stage21_control_rows.csv', [row.to_dict() for row in summary.sweep_rows if row.is_control])
    write_json(out_dir / 'stage21_summary.json', payload)
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
        result = run_su2_mbp_stage21_default_live_validate(
            reference_stage20_summary=args.reference_stage20_summary,
            reference_stage13_summary=args.reference_stage13_summary,
            reference_stage14_summary=args.reference_stage14_summary,
            output_dir=args.output_dir,
        )
    except Exception as exc:  # pragma: no cover
        print_cli_failure('su2_mbp_stage21_default_live_validate', exc)
        return 1
    print_cli_summary('su2_mbp_stage21_default_live_validate', result)
    return 0


if __name__ == '__main__':  # pragma: no cover
    raise SystemExit(main())
