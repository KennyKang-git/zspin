#!/usr/bin/env python3
"""
run_all.py — Z-Spin Cosmology: Run All 46 Verification Suites
==============================================================
Executes every zs_*_verify_v1_0.py script and reports a summary.

Usage:
    python run_all.py              # Run all 46 scripts
    python run_all.py --theme F    # Run only Foundations (ZS-F*) scripts
    python run_all.py --paper f2   # Run a single paper's script
    python run_all.py --verbose    # Show full output from each script
"""

import subprocess
import sys
import os
import glob
import time
import argparse
from pathlib import Path


# ─── Theme Definitions ───────────────────────────────────────────────────────
THEMES = {
    "F": ("Foundations",      ["f0", "f1", "f2", "f3", "f4", "f5"]),
    "M": ("Mathematical Spine", ["m1", "m2", "m3", "m4", "m5", "m6", "m7"]),
    "S": ("Standard Model",  ["s1", "s2", "s3", "s4", "s5", "s6"]),
    "U": ("Early Universe",  ["u1", "u2", "u3", "u4", "u5", "u6", "u7", "u8"]),
    "A": ("Astrophysics",    ["a1", "a2", "a3", "a4", "a5", "a6"]),
    "Q": ("Quantum Mechanics", ["q1", "q2", "q3", "q4", "q5", "q6", "q7"]),
    "QX": ("Quantum Computing", ["qc", "qh", "qs"]),
    "T": ("Translational",   ["t1", "t2", "t3"]),
}


def find_script(paper_id: str, script_dir: str) -> str:
    """Find the verification script for a given paper ID."""
    pattern = os.path.join(script_dir, f"zs_{paper_id}_verify_v1_0.py")
    matches = glob.glob(pattern)
    if not matches:
        return ""
    return matches[0]


def run_script(script_path: str, verbose: bool = False) -> dict:
    """Run a single verification script and capture results."""
    name = Path(script_path).stem
    paper_id = name.replace("_verify_v1_0", "").replace("zs_", "ZS-").upper()

    t0 = time.time()
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True, text=True, timeout=300
        )
        elapsed = time.time() - t0
        output = result.stdout + result.stderr

        # Parse PASS/FAIL counts from output
        # Strategy: try "TOTAL: X/X PASS" format first, then count ✓/✗ lines
        total_pass = 0
        total_fail = 0
        found_total_line = False

        for line in output.splitlines():
            line_stripped = line.strip()
            if "TOTAL:" in line_stripped and "PASS" in line_stripped:
                # e.g. "TOTAL: 71/71 PASS, 0/71 FAIL"
                parts = line_stripped.split()
                for i, p in enumerate(parts):
                    if p in ("PASS,", "PASS"):
                        frac = parts[i - 1]
                        if "/" in frac:
                            total_pass = int(frac.split("/")[0])
                            found_total_line = True
                    if p == "FAIL":
                        frac = parts[i - 1]
                        if "/" in frac:
                            total_fail = int(frac.split("/")[0])

        # Fallback: count individual test lines (✓ = pass, ✗ = fail)
        if not found_total_line:
            for line in output.splitlines():
                ls = line.strip()
                if ls.startswith("✓") or ls.startswith("✅"):
                    total_pass += 1
                elif ls.startswith("✗") or ls.startswith("❌"):
                    total_fail += 1
                # Also match "  PASS" / "  FAIL" at end of test lines
                elif "PASS" in ls and any(c in ls for c in ("V", "F-", "test", "Test")):
                    total_pass += 1
                elif "FAIL" in ls and any(c in ls for c in ("V", "F-", "test", "Test")):
                    total_fail += 1

        passed = result.returncode == 0 and total_fail == 0

        return {
            "paper": paper_id,
            "passed": passed,
            "n_pass": total_pass,
            "n_fail": total_fail,
            "time": elapsed,
            "output": output if verbose else "",
            "returncode": result.returncode,
        }

    except subprocess.TimeoutExpired:
        return {
            "paper": paper_id,
            "passed": False,
            "n_pass": 0,
            "n_fail": -1,
            "time": 300.0,
            "output": "TIMEOUT (300s limit)",
            "returncode": -1,
        }
    except Exception as e:
        return {
            "paper": paper_id,
            "passed": False,
            "n_pass": 0,
            "n_fail": -1,
            "time": 0,
            "output": str(e),
            "returncode": -1,
        }


def main():
    parser = argparse.ArgumentParser(
        description="Z-Spin Cosmology — Run All Verification Suites"
    )
    parser.add_argument(
        "--theme", type=str, default=None,
        help="Run only a specific theme: F, M, S, U, A, Q, QX, T"
    )
    parser.add_argument(
        "--paper", type=str, default=None,
        help="Run a single paper's script, e.g. 'f2' or 'm1'"
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Show full output from each script"
    )
    args = parser.parse_args()

    # Determine script directory (same directory as this file)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Build list of paper IDs to run
    if args.paper:
        paper_ids = [args.paper.lower()]
    elif args.theme:
        key = args.theme.upper()
        if key not in THEMES:
            print(f"Unknown theme '{key}'. Available: {', '.join(THEMES.keys())}")
            sys.exit(1)
        _, paper_ids = THEMES[key]
    else:
        # All papers
        paper_ids = []
        for _, ids in THEMES.values():
            paper_ids.extend(ids)

    # Find scripts
    scripts_to_run = []
    for pid in paper_ids:
        path = find_script(pid, script_dir)
        if path:
            scripts_to_run.append(path)
        else:
            print(f"  ⚠ Script not found for ZS-{pid.upper()}")

    if not scripts_to_run:
        print("No verification scripts found.")
        sys.exit(1)

    # Header
    print("=" * 72)
    print("  Z-Spin Cosmology — Verification Suite Runner")
    print(f"  Papers: {len(scripts_to_run)} | A = 35/437 | Q = 11")
    print("=" * 72)
    print()

    # Run all
    results = []
    total_t0 = time.time()
    for i, script_path in enumerate(scripts_to_run, 1):
        paper_label = Path(script_path).stem.replace("_verify_v1_0", "").replace("zs_", "ZS-").upper()
        print(f"  [{i:2d}/{len(scripts_to_run)}] Running {paper_label}...", end="", flush=True)
        res = run_script(script_path, args.verbose)
        status = "✅ PASS" if res["passed"] else "❌ FAIL"
        print(f"  {status}  ({res['n_pass']}/{res['n_pass']+max(res['n_fail'],0)} tests, {res['time']:.1f}s)")
        if args.verbose and res["output"]:
            for line in res["output"].splitlines():
                print(f"        {line}")
        results.append(res)

    total_time = time.time() - total_t0

    # Summary
    n_passed = sum(1 for r in results if r["passed"])
    n_failed = sum(1 for r in results if not r["passed"])
    total_tests = sum(r["n_pass"] + max(r["n_fail"], 0) for r in results)
    total_test_pass = sum(r["n_pass"] for r in results)

    print()
    print("=" * 72)
    print(f"  SUMMARY: {n_passed}/{len(results)} papers PASS")
    print(f"  Total individual tests: {total_test_pass}/{total_tests}")
    print(f"  Total time: {total_time:.1f}s")
    print()

    if n_failed > 0:
        print("  FAILED papers:")
        for r in results:
            if not r["passed"]:
                print(f"    ❌ {r['paper']}  ({r['n_pass']} pass, {r['n_fail']} fail)")
        print()

    # Theme breakdown
    print("  Theme Breakdown:")
    for key, (theme_name, pids) in THEMES.items():
        theme_results = [r for r in results if r["paper"].replace("ZS-", "").lower() in pids]
        if theme_results:
            tp = sum(1 for r in theme_results if r["passed"])
            tl = len(theme_results)
            icon = "✅" if tp == tl else "❌"
            print(f"    {icon} {theme_name} ({key}): {tp}/{tl}")

    print("=" * 72)

    if n_failed > 0:
        print("\n  ★ SOME TESTS FAILED — see details above ★")
        sys.exit(1)
    else:
        print(f"\n  ★★★ ALL {n_passed} PAPERS PASSED ({total_test_pass} individual tests) ★★★")
        sys.exit(0)


if __name__ == "__main__":
    main()
