"""Common CLI helpers for Z-Sim apps."""

from __future__ import annotations

import sys
from typing import Any, Mapping, Sequence


def print_cli_failure(header: str, exc: BaseException) -> int:
    print(header, file=sys.stderr)
    print(f'{exc.__class__.__name__}: {exc}', file=sys.stderr)
    return 2


def print_cli_summary(header: str, summary: Mapping[str, Any], *, ordered_keys: Sequence[str] = (), list_keys: Sequence[str] = ('generated_outputs',)) -> int:
    print(header)
    seen: set[str] = set()
    for key in ordered_keys:
        if key in summary:
            print(f'{key}: {summary[key]}')
            seen.add(key)
    for key, value in summary.items():
        if key in seen or key in list_keys:
            continue
        print(f'{key}: {value}')
    for key in list_keys:
        if key in summary:
            print(f'{key}:')
            for item in summary[key]:
                print(f'  - {item}')
    success_value = summary.get('success', True)
    return 0 if bool(success_value) else 1


__all__ = ['print_cli_failure', 'print_cli_summary']
