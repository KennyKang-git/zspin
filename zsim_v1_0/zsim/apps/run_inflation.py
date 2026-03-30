#!/usr/bin/env python3
"""
Z-Sim v1.0 — Inflation Analysis Runner
Full canonical-field slow-roll computation.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from zsim.core.constants import A_LOCKED
from zsim.kernel.inflation_canonical import (
    compute_full_inflation, make_inflation_plots, slow_roll_canonical
)


def main(output_dir="zsim_inflation"):
    print("=" * 70)
    print("  Z-Sim v1.0 — Full Canonical-Field Inflation Analysis")
    print(f"  A = 35/437 = {A_LOCKED:.10f}")
    print("  Method: Canonical field φ with K(ε) kinetic metric")
    print("=" * 70)

    N_star_values = [45, 50, 55, 58, 60, 62, 65, 70]
    results = compute_full_inflation(N_star_values)

    print(f"\n{'N*':>5} {'n_s':>10} {'r':>12} {'ε_V':>12} {'η_V':>12} {'ε_field':>10}")
    print("-" * 65)
    for r in results:
        print(f"{r['N_star']:5d} {r['n_s']:10.6f} {r['r']:12.6f} "
              f"{r['eps_V']:12.6e} {r['eta_V']:12.6e} {r['epsilon_field']:10.4f}")

    # Planck comparison
    print(f"\n{'='*65}")
    print("PLANCK 2018 COMPARISON")
    print(f"{'='*65}")
    planck_ns = 0.9649
    planck_ns_err = 0.0042
    bk18_r_upper = 0.036

    for r in results:
        if r['N_star'] in [55, 60]:
            pull_ns = (r['n_s'] - planck_ns) / planck_ns_err
            r_status = "PASS" if r['r'] < bk18_r_upper else "FAIL"
            print(f"  N*={r['N_star']}: n_s={r['n_s']:.6f} (pull={pull_ns:+.2f}σ), "
                  f"r={r['r']:.6f} ({r_status} vs BK18<0.036)")

    # LiteBIRD prediction
    print(f"\n  LiteBIRD target sensitivity: σ(r) ≈ 0.001")
    r_60 = [r for r in results if r['N_star'] == 60][0]
    print(f"  Z-Spin r = {r_60['r']:.6f} → {r_60['r']/0.001:.1f}σ detection by LiteBIRD")
    print(f"  Boyle-Finn-Turok competitor: r = 0 → Z-Spin vs BFT distinguishable at >{r_60['r']/0.001:.0f}σ")

    os.makedirs(output_dir, exist_ok=True)
    make_inflation_plots(results, output_dir)

    print(f"\n  Results saved to {output_dir}/")
    return results


if __name__ == "__main__":
    main()
