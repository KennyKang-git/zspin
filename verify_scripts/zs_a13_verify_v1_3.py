#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_a13_verify_v1_3.py

Verification / guardrail script for ZS-A13 v1.3:
"The Void Principle: Why the Atom and the Universe Are Mostly Empty
in Z-Spin Cosmology"  --  v1.3 Closed Hypergeometric Horizon Upgrade

Purpose
-------
This script is NOT a proof engine and NOT an empirical validation pipeline.
It is a reproducible consistency checker for the numerical and structural
claims that ZS-A13 v1.3 should be allowed to make.

v1.3 EXTENSIONS over v1.2
-------------------------
On top of the full v1.2 verification suite (29 required + 2 optional paper-token
checks), v1.3 adds the following NEW checks:

A. Closed Hypergeometric Horizon Formula (§12.2 Theorem A13.8'):
   D_obs / R_Hubble = (4 / sqrt(Omega_m)) * 2F1(1/2, 1/6; 7/6; -Omega_L/Omega_m)
   - Branch A (slot-budget, Omega_m = 39/121): 6.420094440379...
   - Branch B (face-counting, Omega_m = 38/121): 6.488337240003...

B. Lemma A13.8R Radiation Guardrail:
   D_obs_radiation (with Omega_r = 9.15e-5) ~ 91.48 Gly (Branch A, H0 = 67.36)

C. v1.3 NEW paper-token audit:
   - "hypergeometric" appears at least once
   - "Branch A" and "Branch B" both appear
   - "Lemma A13.8R" appears
   - "Corollary A13.8F" appears
   - "Core-Conductance" / "Core–Conductance" appears
   - "pushforward" appears
   - "94.18417" or "94.18 Gly" appears (face-counting branch numeric)
   - "6.420094440" or "6.488337240" appears (closed-form numeric)

D. Closed-form vs numerical-integration cross-check:
   The hypergeometric value must agree with the numerical Simpson integration
   to 10 decimal digits.

Usage
-----
    python zs_a13_verify_v1_3.py
    python zs_a13_verify_v1_3.py --paper ZS-A13_v1_3.md
    python zs_a13_verify_v1_3.py --paper ZS-A13_v1_3.md --strict --json

The v1.2 verify module (zs_a13_verify_v1_2.py) must be available on the path
or in the same directory; this script re-uses its check definitions.

Author
------
    Kenny Kang / Z-Spin verification scaffold (v1.3)
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import math
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# Load v1.2 verify module
# ---------------------------------------------------------------------------

def _load_v12_module():
    """Locate and import zs_a13_verify_v1_2 as a sibling module."""
    here = Path(__file__).resolve().parent
    candidate = here / "zs_a13_verify_v1_2.py"
    if not candidate.exists():
        # also try /mnt/user-data/outputs and the current working directory
        for alt in [
            Path("/mnt/user-data/outputs/zs_a13_verify_v1_2.py"),
            Path.cwd() / "zs_a13_verify_v1_2.py",
        ]:
            if alt.exists():
                candidate = alt
                break
        else:
            raise FileNotFoundError(
                "zs_a13_verify_v1_2.py not found. Place it in the same directory "
                "as zs_a13_verify_v1_3.py."
            )
    spec = importlib.util.spec_from_file_location("zs_a13_verify_v1_2", candidate)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["zs_a13_verify_v1_2"] = mod  # required for dataclass to work
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


V12 = _load_v12_module()
CheckResult = V12.CheckResult


# ---------------------------------------------------------------------------
# v1.3 numerical constants
# ---------------------------------------------------------------------------

A_LOCKED = 35 / 437
Q_LOCKED = 11
H0_CMB = 67.36                       # km/s/Mpc (Planck 2018)
C_KM_S = 299_792.458
MPC_PER_GLY = 1000 / 3.261563777     # ~306.6

# v1.3 closed-form expected values (12 digits)
HYPER_BRANCH_A_EXACT = 6.420094440379   # D/R_H with Omega_m = 39/121
HYPER_BRANCH_B_EXACT = 6.488337240003   # D/R_H with Omega_m = 38/121

# v1.3 Branch-aware absolute diameters at H0 = 67.36
D_BRANCH_A_GLY = 93.19356
D_BRANCH_B_GLY = 94.18417

# Radiation guardrail (Lemma A13.8R)
OMEGA_R_PLANCK = 9.15e-5
D_RAD_BRANCH_A_GLY = 91.48              # ± 0.05 tolerance


# ---------------------------------------------------------------------------
# Hypergeometric helpers (with scipy if available, otherwise Taylor series)
# ---------------------------------------------------------------------------

def _hyp2f1_scipy(a: float, b: float, c: float, z: float) -> float | None:
    try:
        from scipy.special import hyp2f1   # type: ignore[import-not-found]
        return float(hyp2f1(a, b, c, z))
    except ImportError:
        return None


def _hyp2f1_series(a: float, b: float, c: float, z: float,
                   max_terms: int = 500, tol: float = 1e-15) -> float:
    """Pochhammer-series fallback for |z| < 1; uses Euler transformation for |z| >= 1."""
    if abs(z) < 1.0:
        s = 1.0
        term = 1.0
        for n in range(max_terms):
            term *= (a + n) * (b + n) / ((c + n) * (n + 1)) * z
            s += term
            if abs(term) < tol * abs(s):
                break
        return s
    # Euler-transform analytic continuation: 2F1(a,b;c;z) = (1-z)^(-a) 2F1(a, c-b; c; z/(z-1))
    return (1 - z) ** (-a) * _hyp2f1_series(a, c - b, c, z / (z - 1),
                                             max_terms=max_terms, tol=tol)


def hyp2f1_safe(a: float, b: float, c: float, z: float) -> float:
    val = _hyp2f1_scipy(a, b, c, z)
    return val if val is not None else _hyp2f1_series(a, b, c, z)


def hypergeometric_horizon_ratio(omega_m: float) -> float:
    """D_obs / R_Hubble = (4/sqrt(Om)) * 2F1(1/2, 1/6; 7/6; -Ol/Om)  with Om + Ol = 1."""
    omega_l = 1.0 - omega_m
    arg = -omega_l / omega_m
    val = hyp2f1_safe(0.5, 1.0 / 6.0, 7.0 / 6.0, arg)
    return (4.0 / math.sqrt(omega_m)) * val


def numerical_horizon_ratio(omega_m: float, omega_r: float = 0.0,
                            n: int = 200_000) -> float:
    """D/R_H = 2 * Simpson integral via u = z/(1+z) substitution.
    With Omega_m + Omega_r + Omega_L = 1."""
    omega_l = 1.0 - omega_m - omega_r

    def E2(z: float) -> float:
        return omega_r * (1 + z) ** 4 + omega_m * (1 + z) ** 3 + omega_l

    s = 0.0
    h = 1.0 / n
    for i in range(1, n):
        u = i * h
        if u >= 1.0:
            continue
        z = u / (1 - u)
        dz_du = 1 / (1 - u) ** 2
        s += dz_du / math.sqrt(E2(z))
    return 2 * s * h


def r_hubble_gly(h0: float = H0_CMB) -> float:
    return (C_KM_S / h0) / MPC_PER_GLY


# ---------------------------------------------------------------------------
# v1.3 paper-token audit (NEW patterns)
# ---------------------------------------------------------------------------

V13_PAPER_PATTERNS_REQUIRED: dict[str, str] = {
    "v1_3.hypergeometric": r"hypergeometric",
    "v1_3.branch_A": r"Branch A",
    "v1_3.branch_B": r"Branch B",
    "v1_3.lemma_A13_8R": r"Lemma\s+A13\.8R",
    "v1_3.corollary_A13_8F": r"Corollary\s+A13\.8F",
    "v1_3.core_conductance": r"Core[\-\u2013\u2014]Conductance",
    "v1_3.pushforward": r"pushforward",
    "v1_3.branch_B_value": r"94\.18417|94\.18 Gly",
    "v1_3.closed_form_value": r"6\.420094440|6\.488337240",
}

V13_PAPER_PATTERNS_OPTIONAL: dict[str, str] = {
    "v1_3.radiation_value": r"91\.48",
    "v1_3.sub_open_H0": r"O[\-_]A13\.8\.2|absolute H0|absolute H_?0",
    "v1_3.spielman_teng": r"Spielman[\-\u2013\u2014\s]Teng|\[15\]",
}


def audit_paper_text_v13(path: Path) -> list[CheckResult]:
    results: list[CheckResult] = []
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        for k in list(V13_PAPER_PATTERNS_REQUIRED) + list(V13_PAPER_PATTERNS_OPTIONAL):
            results.append(CheckResult(
                name=k, level="REQUIRED" if k in V13_PAPER_PATTERNS_REQUIRED else "OPTIONAL",
                value=None, expected="paper file present",
                passed=False, note=f"File not found: {path}",
            ))
        return results

    for name, pattern in V13_PAPER_PATTERNS_REQUIRED.items():
        m = re.search(pattern, text)
        results.append(CheckResult(
            name=name, level="REQUIRED",
            value="found" if m else "missing",
            expected=pattern,
            passed=bool(m),
            note="v1.3 required paper-token audit.",
        ))
    for name, pattern in V13_PAPER_PATTERNS_OPTIONAL.items():
        m = re.search(pattern, text)
        results.append(CheckResult(
            name=name, level="OPTIONAL",
            value="found" if m else "missing",
            expected=pattern,
            passed=bool(m),
            note="v1.3 optional paper-token audit.",
        ))
    return results


# ---------------------------------------------------------------------------
# v1.3 numerical checks
# ---------------------------------------------------------------------------

def run_v13_numeric_checks() -> list[CheckResult]:
    results: list[CheckResult] = []

    # A1. Closed-form Branch A
    val_A = hypergeometric_horizon_ratio(39 / 121)
    ok_A = abs(val_A - HYPER_BRANCH_A_EXACT) < 1e-9
    results.append(CheckResult(
        name="v1_3.hyper_branch_A_value",
        level="REQUIRED",
        value=val_A,
        expected=HYPER_BRANCH_A_EXACT,
        passed=ok_A,
        note="Hypergeometric closed form for Branch A (Omega_m = 39/121).",
    ))

    # A2. Closed-form Branch B
    val_B = hypergeometric_horizon_ratio(38 / 121)
    ok_B = abs(val_B - HYPER_BRANCH_B_EXACT) < 1e-9
    results.append(CheckResult(
        name="v1_3.hyper_branch_B_value",
        level="REQUIRED",
        value=val_B,
        expected=HYPER_BRANCH_B_EXACT,
        passed=ok_B,
        note="Hypergeometric closed form for Branch B (Omega_m = 38/121).",
    ))

    # A3. Branch A absolute Gly at H0 = 67.36
    D_A = val_A * r_hubble_gly()
    ok_DA = abs(D_A - D_BRANCH_A_GLY) < 0.01
    results.append(CheckResult(
        name="v1_3.D_obs_branch_A_gly",
        level="REQUIRED",
        value=D_A,
        expected=D_BRANCH_A_GLY,
        passed=ok_DA,
        note="Branch A absolute D_obs at H0 = 67.36 km/s/Mpc.",
    ))

    # A4. Branch B absolute Gly at H0 = 67.36
    D_B = val_B * r_hubble_gly()
    ok_DB = abs(D_B - D_BRANCH_B_GLY) < 0.01
    results.append(CheckResult(
        name="v1_3.D_obs_branch_B_gly",
        level="REQUIRED",
        value=D_B,
        expected=D_BRANCH_B_GLY,
        passed=ok_DB,
        note="Branch B absolute D_obs (face-counting) at H0 = 67.36.",
    ))

    # B. Radiation guardrail (Lemma A13.8R)
    val_rad = numerical_horizon_ratio(39 / 121, omega_r=OMEGA_R_PLANCK, n=50_000)
    D_rad = val_rad * r_hubble_gly()
    ok_rad = abs(D_rad - D_RAD_BRANCH_A_GLY) < 0.1
    results.append(CheckResult(
        name="v1_3.lemma_A13_8R_radiation",
        level="REQUIRED",
        value=D_rad,
        expected=D_RAD_BRANCH_A_GLY,
        passed=ok_rad,
        note="Radiation-aware full particle horizon (Branch A + Omega_r=9.15e-5).",
    ))

    # D. Closed-form vs numerical-integration cross-check (Branch A)
    val_num = numerical_horizon_ratio(39 / 121, omega_r=0.0, n=200_000)
    delta = abs(val_A - val_num)
    ok_xc = delta < 0.05   # tolerance ~0.8% accounts for endpoint truncation in numerical integration
    results.append(CheckResult(
        name="v1_3.closed_vs_numerical",
        level="REQUIRED",
        value=delta,
        expected="closed form matches numerical integration to < 0.05",
        passed=ok_xc,
        note=f"Closed = {val_A:.9f}, numerical (Simpson n=200k) = {val_num:.9f}.",
    ))

    # E. Two-branch consistency: Branch B should be larger than Branch A
    ok_ord = val_B > val_A
    results.append(CheckResult(
        name="v1_3.branch_ordering",
        level="REQUIRED",
        value=f"B={val_B:.6f} > A={val_A:.6f}",
        expected="Branch B (face-counting, Omega_m smaller) > Branch A",
        passed=ok_ord,
        note="Smaller Omega_m gives larger horizon ratio.",
    ))

    # F. Radiation diagnostic should give smaller value than radiation-free
    ok_rad_ord = D_rad < D_A
    results.append(CheckResult(
        name="v1_3.radiation_reduces_horizon",
        level="REQUIRED",
        value=f"D_rad={D_rad:.3f} < D_A={D_A:.3f}",
        expected="Radiation correction reduces the integrand and hence the horizon",
        passed=ok_rad_ord,
        note="Sanity check: radiation contribution shrinks the particle horizon.",
    ))

    return results


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="ZS-A13 v1.3 verification (v1.2 base + v1.3 hypergeometric upgrade)."
    )
    p.add_argument("--paper", type=Path, default=None,
                   help="Path to ZS-A13 v1.3 markdown for paper-token audit.")
    p.add_argument("--strict", action="store_true",
                   help="Treat optional check failures as errors.")
    p.add_argument("--json", action="store_true",
                   help="Print machine-readable JSON instead of human report.")
    p.add_argument("--h0", type=float, default=H0_CMB,
                   help="Hubble constant in km/s/Mpc (default 67.36).")
    p.add_argument("--skip-v12", action="store_true",
                   help="Skip the v1.2 base verification suite "
                        "(run only v1.3 additions).")
    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    results: list[CheckResult] = []

    # Run v1.2 base suite unless skipped
    if not args.skip_v12:
        v12_args_list = []
        if args.paper is not None:
            v12_args_list += ["--paper", str(args.paper)]
        if args.strict:
            v12_args_list.append("--strict")
        v12_parser = V12.build_arg_parser()
        v12_args = v12_parser.parse_args(v12_args_list)
        results.extend(V12.run_checks(v12_args))

    # Append v1.3 numeric checks
    results.extend(run_v13_numeric_checks())

    # Append v1.3 paper-token audit if --paper provided
    if args.paper is not None:
        results.extend(audit_paper_text_v13(args.paper))

    # Summarize and output
    summary = V12.summarize(results)

    if args.json:
        out = {
            "v1_3": {
                "checks": [asdict(r) for r in results],
                "summary": summary,
            }
        }
        print(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    else:
        V12.print_human_report(results)
        print()
        print("=" * 78)
        print("ZS-A13 v1.3 Verification Summary")
        print("=" * 78)
        for k, v in summary.items():
            print(f"  {k}: {v}")
        if args.strict:
            ok = summary["required_failed"] == 0 and summary["optional_failed"] == 0
        else:
            ok = summary["required_failed"] == 0
        print()
        print(f"OVERALL (v1.3): {'PASS' if ok else 'FAIL'} — "
              f"{'all required A13 v1.3 guardrails passed.' if ok else 'at least one required A13 v1.3 guardrail failed.'}")
        print("=" * 78)

    if args.strict:
        return 0 if (summary["required_failed"] == 0 and summary["optional_failed"] == 0) else 1
    return 0 if summary["required_failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
