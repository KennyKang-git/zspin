#!/usr/bin/env python3
"""Z-Sim v3.1 — Tier-0.9 Cobaya Verification Matrix.

Run this in WSL with cobaya_env activated to test all parameter
combinations against Planck plik_lite.

This script tests 4 configurations and reports Dchi2 vs Planck LCDM.
Paper 32 criterion: Dchi2 < 10 = PASS.

Usage (in WSL):
    source ~/cobaya_env/bin/activate
    cd /mnt/c/Users/LG/zsim_v3.1
    python cobaya_f32/verify_tier09.py --packages-path ~/packages
"""
import subprocess
import sys
import os
import tempfile
import json

CONFIGS = {
    "Planck_LCDM": {
        "H0": 67.36, "ombh2": 0.02237, "omch2": 0.1200,
        "ns": 0.9649, "As": 2.1e-9, "tau": 0.054,
        "label": "Planck LCDM (6-param best-fit)"
    },
    "ZSpin_bare_b_eff_cdm_h6736": {
        "H0": 67.36, "ombh2": 0.02250, "omch2": 0.11457,
        "ns": 0.9674, "As": 2.1e-9, "tau": 0.054,
        "label": "Z-Spin self-consistent (bare b, eff cdm, h=0.6736)"
    },
    "ZSpin_bare_b_bare_cdm_h6736": {
        "H0": 67.36, "ombh2": 0.02250, "omch2": 0.12375,
        "ns": 0.9674, "As": 2.1e-9, "tau": 0.054,
        "label": "Z-Spin all-bare (bare b, bare cdm, h=0.6736)"
    },
    "ZSpin_pathC_validated": {
        "H0": 67.36, "ombh2": 0.02250, "omch2": 0.120740,
        "ns": 0.9674, "As": 2.1e-9, "tau": 0.054,
        "label": "Z-Spin Path C (Cobaya-validated 2026-03-18)"
    },
}


YAML_TEMPLATE = """
likelihood:
  planck_2018_highl_plik.TTTEEE_lite:

theory:
  camb:

params:
  H0: {H0}
  ombh2: {ombh2}
  omch2: {omch2}
  ns: {ns}
  As: {As}
  tau: {tau}
  A_planck: 1.0

sampler:
  evaluate:

output: {output}
"""


def run_cobaya(config, name, packages_path):
    """Run cobaya-run with evaluate sampler and return chi2."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, name)
        yaml_content = YAML_TEMPLATE.format(output=output, **config)
        yaml_path = os.path.join(tmpdir, f"{name}.yaml")

        with open(yaml_path, 'w') as f:
            f.write(yaml_content)

        cmd = ["cobaya-run", yaml_path]
        if packages_path:
            cmd += ["--packages-path", packages_path]

        result = subprocess.run(cmd, capture_output=True, text=True)

        # Parse chi2 from output
        for line in result.stdout.split('\n'):
            if 'chi2_planck_2018_highl_plik.TTTEEE_lite' in line:
                chi2 = float(line.split('=')[1].strip())
                return chi2

        # Fallback: try parsing the chain file
        chain_file = f"{output}.1.txt"
        if os.path.exists(chain_file):
            with open(chain_file) as f:
                lines = f.readlines()
                if len(lines) > 1:
                    # Last column should be plik chi2
                    vals = lines[-1].strip().split()
                    return float(vals[-1])

    return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--packages-path", default=os.path.expanduser("~/packages"))
    args = parser.parse_args()

    print("=" * 70)
    print("  Z-Sim v3.1 — Tier-0.9 Verification Matrix")
    print("  Testing against Planck 2018 plik_lite TTTEEE")
    print("=" * 70)

    results = {}
    for name, config in CONFIGS.items():
        label = config.pop("label")
        print(f"\n  Running: {label}...")
        chi2 = run_cobaya(config, name, args.packages_path)
        config["label"] = label  # restore
        results[name] = {"chi2": chi2, "label": label}
        if chi2 is not None:
            print(f"    chi2 = {chi2:.2f}")
        else:
            print(f"    FAILED to get chi2")

    # Report
    ref_chi2 = results.get("Planck_LCDM", {}).get("chi2")
    if ref_chi2 is None:
        print("\n  ERROR: Planck LCDM reference failed!")
        return 1

    print("\n" + "=" * 70)
    print("  RESULTS")
    print("=" * 70)
    print(f"\n  {'Config':<45s} {'chi2':>8s} {'Dchi2':>8s} {'Verdict':>8s}")
    print(f"  {'-'*70}")

    for name, r in results.items():
        chi2 = r["chi2"]
        if chi2 is not None:
            dchi2 = chi2 - ref_chi2
            verdict = "PASS" if dchi2 < 10 else ("MARGIN" if dchi2 < 25 else "FAIL")
            print(f"  {r['label']:<45s} {chi2:>8.1f} {dchi2:>+8.1f} {verdict:>8s}")
        else:
            print(f"  {r['label']:<45s} {'N/A':>8s}")

    print(f"\n  Reference: Planck LCDM chi2 = {ref_chi2:.2f}")
    print(f"  Criterion: Dchi2 < 10 = PASS (Paper 32)")
    print("=" * 70)

    return 0


if __name__ == "__main__":
    sys.exit(main())
