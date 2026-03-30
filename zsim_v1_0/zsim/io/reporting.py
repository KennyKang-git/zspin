"""Result reporting helpers for Z-Sim v1.0."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Iterable, Mapping


def _read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding='utf-8'))


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open('r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        return [dict(row) for row in reader]


def detect_result_type(source_dir: str | Path) -> str:
    source = Path(source_dir)
    if (source / 'scan_summary.json').exists() and (source / 'scan_metrics.csv').exists():
        return 'scan'
    if (source / 'comparison_summary.json').exists() and (source / 'comparison_metrics.csv').exists():
        return 'comparison'
    if (source / 'run_metadata.json').exists() and (source / 'run_observables.csv').exists():
        return 'background'
    raise FileNotFoundError(f'Could not detect a supported Z-Sim result type in: {source}')


def _float_or_none(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    text = str(value).strip()
    if not text or text.lower() == 'none':
        return None
    return float(text)


def _format_scalar(value: Any, digits: int = 6) -> str:
    if value is None:
        return 'None'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return f'{value:.{digits}g}'
    return str(value)


def _markdown_table(columns: list[str], rows: Iterable[Mapping[str, Any]]) -> list[str]:
    header = '| ' + ' | '.join(columns) + ' |'
    divider = '| ' + ' | '.join('---' for _ in columns) + ' |'
    lines = [header, divider]
    for row in rows:
        lines.append('| ' + ' | '.join(_format_scalar(row.get(col)) for col in columns) + ' |')
    return lines


def _safe_delta_text(value: float | None, label: str) -> str:
    if value is None:
        return f'{label} unavailable.'
    if abs(value) < 1e-12:
        return f'{label} is effectively zero.'
    direction = 'increases' if value > 0 else 'decreases'
    return f'{label} {direction} by {_format_scalar(abs(value))}.'


def _background_interpretation(payload: Mapping[str, Any]) -> list[str]:
    lines: list[str] = []
    med = _float_or_none(payload.get('final_mediation_efficiency'))
    asym = _float_or_none(payload.get('final_sector_asymmetry'))
    sigma = _float_or_none(payload.get('final_sigma_struct'))
    success = bool(payload.get('success', False))

    if success:
        lines.append('Run completed successfully without a terminal failure.')
    else:
        lines.append('Run did not complete successfully; treat final observables as diagnostic only.')

    if med is not None:
        if med < 1e-6:
            lines.append('Mediator flow is effectively dormant at the final step.')
        elif med < 0.05:
            lines.append('Mediator flow remains active but weak at the final step.')
        else:
            lines.append('Mediator flow is materially active at the final step.')

    if asym is not None:
        if asym < 0.1:
            lines.append('Sector budgets remain relatively balanced in the reduced state.')
        elif asym < 0.3:
            lines.append('Sector budgets show moderate contrast across X/Z/Y.')
        else:
            lines.append('Sector budgets remain strongly partitioned across X/Z/Y.')

    if sigma is not None:
        if sigma <= 0.0:
            lines.append('Structural-arrow accumulation is negligible.')
        else:
            lines.append('Structural-arrow accumulation is monotone-positive over the run.')
    return lines


def _comparison_interpretation(payload: Mapping[str, Any]) -> list[str]:
    lines = [
        _safe_delta_text(_float_or_none(payload.get('mediation_off_delta_h_like')), 'Turning mediation off'),
        _safe_delta_text(_float_or_none(payload.get('phase_constant_delta_phi_z')), 'Freezing phase evolution'),
        _safe_delta_text(
            _float_or_none(payload.get('global_mean_delta_sector_asymmetry')),
            'Replacing partition-aware evolution with the global-mean mock',
        ),
    ]
    return lines


def _scan_interpretation(payload: Mapping[str, Any]) -> list[str]:
    success_count = int(payload.get('success_count', 0))
    failure_count = int(payload.get('failure_count', 0))
    min_h = _float_or_none(payload.get('final_h_like_min'))
    max_h = _float_or_none(payload.get('final_h_like_max'))
    lines: list[str] = []
    if failure_count == 0:
        lines.append('All scanned cases completed successfully.')
    else:
        lines.append(f'{failure_count} scanned case(s) failed or terminated early.')
    if min_h is not None and max_h is not None:
        span = max_h - min_h
        if span < 1e-6:
            lines.append('Final H_like is effectively invariant across the scanned cases.')
        else:
            lines.append(f'Final H_like spans {_format_scalar(span)} across successful cases.')
    if success_count > 0:
        lines.append(f'Successful case count: {success_count}.')
    return lines


def _background_report(source: Path) -> dict[str, Any]:
    metadata = _read_json(source / 'run_metadata.json')
    diagnostics = _read_json(source / 'run_diagnostics.json') if (source / 'run_diagnostics.json').exists() else {}
    observables = _read_csv_rows(source / 'run_observables.csv')
    final_obs = observables[-1] if observables else {}
    payload = {
        'report_type': 'background',
        'source_dir': str(source),
        'success': bool(metadata.get('success', False)),
        'message': metadata.get('message', ''),
        'step_count': int(metadata.get('step_count', 0)),
        'initial_N': _float_or_none(metadata.get('initial_N')),
        'final_N': _float_or_none(metadata.get('final_N')),
        'final_h_like': _float_or_none(final_obs.get('H_like')),
        'final_w_eff': _float_or_none(final_obs.get('w_eff')),
        'final_sigma_struct': _float_or_none(final_obs.get('sigma_struct')),
        'final_sector_asymmetry': _float_or_none(final_obs.get('sector_asymmetry')),
        'final_mediation_efficiency': _float_or_none(final_obs.get('mediation_efficiency')),
        'event_count': int(metadata.get('event_count', 0)),
        'kill_switches': diagnostics.get('kill_switches_final', {}),
        'generated_outputs': list(metadata.get('generated_outputs', [])),
    }
    payload['interpretation'] = _background_interpretation(payload)
    return payload


def _comparison_report(source: Path) -> dict[str, Any]:
    summary = _read_json(source / 'comparison_summary.json')
    metrics = _read_csv_rows(source / 'comparison_metrics.csv')
    scenarios = {row['scenario']: row for row in metrics}
    ref = scenarios.get('reference', {})
    med_off = scenarios.get('mediation_off', {})
    phase_const = scenarios.get('phase_constant', {})
    global_mock = scenarios.get('global_mean_mock', {})
    payload = {
        'report_type': 'comparison',
        'source_dir': str(source),
        'scenario_count': int(summary.get('scenario_count', len(metrics))),
        'generated_outputs': list(summary.get('generated_outputs', [])),
        'reference_final_h_like': _float_or_none(ref.get('final_h_like')),
        'mediation_off_delta_h_like': _float_or_none(med_off.get('delta_vs_reference:final_h_like')),
        'phase_constant_delta_phi_z': _float_or_none(phase_const.get('delta_vs_reference:final_phi_z')),
        'global_mean_delta_sector_asymmetry': _float_or_none(global_mock.get('delta_vs_reference:final_sector_asymmetry')),
        'scenarios': metrics,
    }
    payload['interpretation'] = _comparison_interpretation(payload)
    return payload


def _scan_report(source: Path) -> dict[str, Any]:
    summary = _read_json(source / 'scan_summary.json')
    metrics = _read_csv_rows(source / 'scan_metrics.csv')
    successful = [row for row in metrics if str(row.get('success', '')).lower() == 'true']
    h_values = [_float_or_none(row.get('final_h_like')) for row in successful]
    h_values = [value for value in h_values if value is not None]
    payload = {
        'report_type': 'scan',
        'source_dir': str(source),
        'case_count': int(summary.get('case_count', len(metrics))),
        'success_count': int(summary.get('success_count', len(successful))),
        'failure_count': int(summary.get('failure_count', len(metrics) - len(successful))),
        'vary': list(summary.get('vary', [])),
        'factor_values': list(summary.get('factor_values', [])),
        'final_h_like_min': min(h_values) if h_values else None,
        'final_h_like_max': max(h_values) if h_values else None,
        'generated_outputs': list(summary.get('generated_outputs', [])),
        'cases': metrics,
    }
    payload['interpretation'] = _scan_interpretation(payload)
    return payload


def _candidate_dirs(source: Path, recursive: bool = True) -> list[Path]:
    iterator = source.rglob('*') if recursive else source.iterdir()
    dirs = [path for path in iterator if path.is_dir()]
    return sorted(dirs)


def build_directory_index(source_dir: str | Path, recursive: bool = True) -> dict[str, Any]:
    source = Path(source_dir)
    entries: list[dict[str, Any]] = []
    for path in _candidate_dirs(source, recursive=recursive):
        try:
            payload = build_report_payload(path)
        except FileNotFoundError:
            continue
        entries.append(
            {
                'name': path.name,
                'path': str(path),
                'report_type': payload['report_type'],
                'success': payload.get('success', True),
                'final_h_like': payload.get('final_h_like', payload.get('reference_final_h_like')),
                'generated_outputs': len(payload.get('generated_outputs', [])),
            }
        )
    if not entries:
        raise FileNotFoundError(f'Could not find any reportable Z-Sim result directories under: {source}')
    type_counts: dict[str, int] = {}
    for entry in entries:
        key = str(entry['report_type'])
        type_counts[key] = type_counts.get(key, 0) + 1
    return {
        'report_type': 'index',
        'source_dir': str(source),
        'entry_count': len(entries),
        'type_counts': type_counts,
        'entries': entries,
    }


def build_report_payload(source_dir: str | Path) -> dict[str, Any]:
    source = Path(source_dir)
    result_type = detect_result_type(source)
    if result_type == 'background':
        return _background_report(source)
    if result_type == 'comparison':
        return _comparison_report(source)
    if result_type == 'scan':
        return _scan_report(source)
    raise RuntimeError(f'Unsupported result type: {result_type}')


def render_markdown_report(payload: Mapping[str, Any]) -> str:
    report_type = str(payload['report_type'])
    lines: list[str] = [f'# Z-Sim {report_type.title()} Report', '']
    lines.append(f"- Source: `{payload['source_dir']}`")
    lines.append(f"- Type: `{report_type}`")
    if 'generated_outputs' in payload:
        lines.append(f"- Generated outputs tracked: {len(payload['generated_outputs'])}")
    lines.append('')

    if report_type == 'background':
        lines.extend([
            '## Summary',
            '',
            *_markdown_table(
                ['field', 'value'],
                [
                    {'field': 'success', 'value': payload['success']},
                    {'field': 'message', 'value': payload['message']},
                    {'field': 'step_count', 'value': payload['step_count']},
                    {'field': 'final_N', 'value': payload['final_N']},
                    {'field': 'final_H_like', 'value': payload['final_h_like']},
                    {'field': 'final_w_eff', 'value': payload['final_w_eff']},
                    {'field': 'final_sigma_struct', 'value': payload['final_sigma_struct']},
                    {'field': 'final_sector_asymmetry', 'value': payload['final_sector_asymmetry']},
                    {'field': 'final_mediation_efficiency', 'value': payload['final_mediation_efficiency']},
                ],
            ),
            '',
            '## Interpretation',
            '',
        ])
        lines.extend([f'- {line}' for line in payload.get('interpretation', [])])
        lines.extend([
            '',
            '## Kill-switch snapshot',
            '',
            '```json',
            json.dumps(payload.get('kill_switches', {}), indent=2, sort_keys=True),
            '```',
        ])
        return '\n'.join(lines) + '\n'

    if report_type == 'comparison':
        lines.extend([
            '## Summary',
            '',
            *_markdown_table(
                ['field', 'value'],
                [
                    {'field': 'scenario_count', 'value': payload['scenario_count']},
                    {'field': 'reference_final_h_like', 'value': payload['reference_final_h_like']},
                    {'field': 'mediation_off_delta_h_like', 'value': payload['mediation_off_delta_h_like']},
                    {'field': 'phase_constant_delta_phi_z', 'value': payload['phase_constant_delta_phi_z']},
                    {'field': 'global_mean_delta_sector_asymmetry', 'value': payload['global_mean_delta_sector_asymmetry']},
                ],
            ),
            '',
            '## Interpretation',
            '',
        ])
        lines.extend([f'- {line}' for line in payload.get('interpretation', [])])
        lines.extend([
            '',
            '## Scenario table',
            '',
            *_markdown_table(
                ['scenario', 'success', 'final_h_like', 'final_sigma_struct', 'final_sector_asymmetry'],
                payload['scenarios'],
            ),
        ])
        return '\n'.join(lines) + '\n'

    if report_type == 'scan':
        lines.extend([
            '## Summary',
            '',
            *_markdown_table(
                ['field', 'value'],
                [
                    {'field': 'case_count', 'value': payload['case_count']},
                    {'field': 'success_count', 'value': payload['success_count']},
                    {'field': 'failure_count', 'value': payload['failure_count']},
                    {'field': 'vary', 'value': ', '.join(payload['vary'])},
                    {'field': 'factor_values', 'value': ', '.join(str(v) for v in payload['factor_values'])},
                    {'field': 'final_h_like_min', 'value': payload['final_h_like_min']},
                    {'field': 'final_h_like_max', 'value': payload['final_h_like_max']},
                ],
            ),
            '',
            '## Interpretation',
            '',
        ])
        lines.extend([f'- {line}' for line in payload.get('interpretation', [])])
        lines.extend([
            '',
            '## Case table',
            '',
            *_markdown_table(
                ['case', 'success', 'final_h_like', 'final_sigma_struct', 'final_mediation_efficiency'],
                payload['cases'],
            ),
        ])
        return '\n'.join(lines) + '\n'

    if report_type == 'index':
        lines.extend([
            '## Summary',
            '',
            *_markdown_table(
                ['field', 'value'],
                [
                    {'field': 'entry_count', 'value': payload['entry_count']},
                    {'field': 'type_counts', 'value': ', '.join(f'{k}:{v}' for k, v in sorted(payload['type_counts'].items()))},
                ],
            ),
            '',
            '## Entry table',
            '',
            *_markdown_table(['name', 'report_type', 'success', 'final_h_like', 'path'], payload['entries']),
        ])
        return '\n'.join(lines) + '\n'

    raise RuntimeError(f'Unsupported report payload type: {report_type}')


__all__ = [
    'build_directory_index',
    'build_report_payload',
    'detect_result_type',
    'render_markdown_report',
]
