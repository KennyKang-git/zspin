"""CLI for summarizing Z-Sim output directories into readable reports."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.io import (
    build_directory_index,
    build_report_payload,
    ensure_output_dir,
    write_json,
    render_markdown_report,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Generate a human-readable report from an existing Z-Sim output directory.')
    parser.add_argument('--source-dir', required=True, help='Existing Z-Sim output directory to summarize.')
    parser.add_argument('--output-dir', default=None, help='Directory for report artifacts. Defaults to <source-dir>/report.')
    parser.add_argument(
        '--index',
        action='store_true',
        help='Build an index report over reportable child directories instead of summarizing a single run directory.',
    )
    return parser


def report_results(source_dir: str | Path, output_dir: str | Path | None = None, *, index: bool = False) -> dict[str, object]:
    source = Path(source_dir)
    out_dir = ensure_output_dir(output_dir or (source / 'report'))
    payload = build_directory_index(source) if index else build_report_payload(source)
    markdown = render_markdown_report(payload)
    md_name = 'index.md' if payload['report_type'] == 'index' else 'report.md'
    json_name = 'index.json' if payload['report_type'] == 'index' else 'report.json'
    md_path = out_dir / md_name
    json_path = out_dir / json_name
    md_path.write_text(markdown, encoding='utf-8')
    write_json(json_path, payload)
    return {
        'success': True,
        'report_type': payload['report_type'],
        'source_dir': str(source),
        'output_dir': str(out_dir),
        'generated_outputs': (md_name, json_name),
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        summary = report_results(args.source_dir, args.output_dir, index=bool(args.index))
    except FileNotFoundError as exc:
        return print_cli_failure('Z-Sim report generation failed.', exc)

    return print_cli_summary(
        'Z-Sim report generation complete.',
        summary,
        ordered_keys=('success', 'report_type', 'source_dir', 'output_dir'),
    )


if __name__ == '__main__':
    raise SystemExit(main())
