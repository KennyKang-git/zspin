"""Integration test for run_derived.py (v3.1 Fix #2).

Verifies that the DERIVED closure runner works end-to-end
with the current v3.1 IO/validation API.
"""
import json
import os
import pytest
from pathlib import Path


def test_run_derived_succeeds(tmp_path):
    """run_derived produces expected outputs with derived.yaml."""
    from zsim.apps.run_derived import run_derived

    result = run_derived(
        config_path="configs/derived.yaml",
        output_dir=str(tmp_path / "derived_out"),
        make_plots_override=False,
        N_end=-15.0,  # short run for speed
    )
    assert result["success"] is True
    assert result["kill_switches_ok"] is True
    assert result["step_count"] > 0
    assert abs(result["final_epsilon"] - 1.0) < 0.01

    # Check output files exist
    out = tmp_path / "derived_out"
    assert (out / "run_state.csv").exists()
    assert (out / "run_observables.csv").exists()
    assert (out / "run_metadata.json").exists()


def test_run_derived_cli(tmp_path):
    """run_derived works as CLI module."""
    from zsim.apps.run_derived import main
    ret = main([
        "--config", "configs/derived.yaml",
        "--output-dir", str(tmp_path / "cli_out"),
        "--no-plots",
        "--N-end", "-15.0",
    ])
    assert ret == 0


def test_run_derived_closure_verification():
    """Derived closures match theoretical values."""
    from zsim.core.config import ZSimConfig
    from zsim.core.constants import A_LOCKED, DIM_X, DIM_Z, DIM_Y, Q_TOTAL

    cfg = ZSimConfig.from_yaml("configs/derived.yaml")
    A, Q = A_LOCKED, Q_TOTAL
    X, Z, Y = DIM_X, DIM_Z, DIM_Y

    assert abs(cfg.closure.gamma_xz - 2*A/Q) < 1e-5
    assert abs(cfg.closure.gamma_zy - 6*A/Q) < 1e-5
    assert abs(cfg.closure.alpha_xz - X/Z) < 1e-5
    assert abs(cfg.closure.alpha_zy - Z/Y) < 1e-5
    assert cfg.closure.phase_mode == "spinor_sin2"
    assert cfg.closure.lam == 1.79

    # Equipartition ICs
    total = cfg.initial.rho_x0 + cfg.initial.rho_z0 + cfg.initial.rho_y0
    assert abs(total - 1.0) < 1e-10
    assert abs(cfg.initial.rho_x0 - X/Q) < 1e-5
    assert abs(cfg.initial.rho_z0 - Z/Q) < 1e-5
    assert abs(cfg.initial.rho_y0 - Y/Q) < 1e-5
