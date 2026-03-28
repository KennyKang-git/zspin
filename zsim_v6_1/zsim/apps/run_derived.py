"""Z-Sim v3.1 — Run with DERIVED closures (zero free parameters).

All 8 closure parameters are DERIVED from the Z-Spin action:
  7 from ZS-Q7 S5.1 (Pauli master equation)
  1 from ZS-M3 Thm 5.1 (SU(2) j=1/2 spinor gate)
"""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from zsim.apps.common import print_cli_failure, print_cli_summary
from zsim.core import ConfigLoadError, ConfigValidationError, IntegrationError, ZSimConfig
from zsim.core.constants import A_LOCKED, DIM_X, DIM_Z, DIM_Y, Q_TOTAL
from zsim.io import ensure_output_dir, persist_integrated_run
from zsim.solver import integrate
from zsim.validation.kill_switches import run_kill_switches


def run_derived(config_path: str | Path = "configs/derived.yaml",
                output_dir: str | Path = "outputs/derived_run",
                *, make_plots_override: bool | None = None,
                N_end: float | None = None) -> dict[str, object]:
    """Run background evolution with theory-derived closures."""

    print("=" * 70)
    print("  Z-Sim v3.1 — DERIVED Closures (Zero Free Parameters)")
    print("=" * 70)

    cfg = ZSimConfig.from_yaml(config_path)

    # Verify derived values match theory
    A, Q = A_LOCKED, Q_TOTAL
    X, Z, Y = DIM_X, DIM_Z, DIM_Y
    checks = [
        ("gamma_xz", cfg.closure.gamma_xz, 2*A/Q),
        ("gamma_zy", cfg.closure.gamma_zy, 6*A/Q),
        ("alpha_xz", cfg.closure.alpha_xz, X/Z),
        ("alpha_zy", cfg.closure.alpha_zy, Z/Y),
    ]
    print("\n  Derived closure verification:")
    for name, actual, expected in checks:
        ok = abs(actual - expected) < 1e-4
        print(f"    {name:12s} = {actual:.6f} ({'OK' if ok else 'MISMATCH'})")
    print(f"    phase_mode  = {cfg.closure.phase_mode}")
    print(f"    lam         = {cfg.closure.lam}")

    # Run integration
    result = integrate(cfg, N_end=N_end)

    # Save outputs using the standard pipeline
    out_dir = ensure_output_dir(output_dir)
    artifacts = persist_integrated_run(
        out_dir, cfg, result,
        include_diagnostics=True,
        make_plots_override=make_plots_override,
    )

    # Convergence report
    final = result.final_state
    print(f"\n  Convergence:")
    print(f"    epsilon    = {final.epsilon:.8f} (|delta|={abs(final.epsilon-1):.2e})")
    print(f"    rho_total  = {final.rho_total:.6e}")
    if final.rho_total > 0:
        print(f"    Z-fraction = {final.rho_z / final.rho_total:.4f}")

    ks = run_kill_switches(final, cfg)
    print(f"    Kill-switches: {'ALL PASS (6/6)' if ks.ok else 'TRIGGERED'}")

    return {
        "success": result.success,
        "message": result.message,
        "output_dir": str(artifacts.output_dir),
        "generated_outputs": artifacts.generated_outputs,
        "step_count": result.step_count,
        "final_N": float(final.N),
        "final_epsilon": float(final.epsilon),
        "kill_switches_ok": ks.ok,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Z-Sim v3.1: run with theory-derived closures (zero free parameters).")
    parser.add_argument("--config", default="configs/derived.yaml")
    parser.add_argument("--output-dir", default="outputs/derived_run")
    parser.add_argument("--no-plots", action="store_true")
    parser.add_argument("--N-end", type=float, default=None)
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        summary = run_derived(
            args.config, args.output_dir,
            make_plots_override=not args.no_plots,
            N_end=args.N_end,
        )
    except (ConfigLoadError, ConfigValidationError, IntegrationError) as exc:
        return print_cli_failure("Z-Sim derived run failed.", exc)

    return print_cli_summary("Z-Sim derived run complete.", summary,
        ordered_keys=("success", "message", "output_dir", "step_count",
                      "final_N", "final_epsilon", "kill_switches_ok"))


if __name__ == "__main__":
    raise SystemExit(main())
