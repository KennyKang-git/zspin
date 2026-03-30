from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(cmd: list[str]) -> int:
    return subprocess.run(cmd, cwd=REPO_ROOT).returncode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run Z-Sim quickstart scenarios.")
    parser.add_argument("mode", choices=["background", "compare", "scan", "closure-matrix", "report"], help="Quickstart scenario to run.")
    args = parser.parse_args(argv)

    python = sys.executable
    config = "configs/derived.yaml"

    if args.mode == "background":
        return _run([python, "-m", "zsim.apps.run_background", "--config", config, "--output-dir", "outputs/quickstart_background", "--no-plots"])
    if args.mode == "compare":
        return _run([python, "-m", "zsim.apps.compare_baselines", "--config", config, "--output-dir", "outputs/quickstart_compare", "--no-plots"])
    if args.mode == "scan":
        return _run([python, "-m", "zsim.apps.run_scan", "--config", config, "--output-dir", "outputs/quickstart_scan", "--vary", "gamma_xz", "gamma_zy", "--factors", "0.0,1.0", "--no-plots"])
    if args.mode == "closure-matrix":
        return _run([python, "-m", "zsim.apps.run_closure_matrix", "--config", config, "--output-dir", "outputs/quickstart_closure_matrix", "--phase-source-modes", "full_state,currents_only", "--mediation-modes", "raw_contrast", "--epsilon-source-modes", "zero", "--h-closure-modes", "sqrt_sum", "--N-end", "-17.8", "--no-plots"])
    return _run([python, "-m", "zsim.apps.report_results", "--source-dir", "outputs/quickstart_background", "--output-dir", "outputs/quickstart_background/report"])


if __name__ == "__main__":
    raise SystemExit(main())
