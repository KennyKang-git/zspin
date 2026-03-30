import math

import pytest

from zsim.core import LabeledValue, Status, ZSimConfig, ZSimState
from zsim.validation import (
    KillSwitchReport,
    emit_run_report,
    ks_direct_xy_path,
    ks_epistemic_overclaim,
    ks_nonphysical_state,
    ks_partition_collapse,
    ks_rank_overflow,
    partition_signature,
    run_kill_switches,
    validate_config,
    validate_initial_state,
)


@pytest.fixture()
def base_config() -> ZSimConfig:
    return ZSimConfig.from_yaml("configs/base.yaml")


@pytest.fixture()
def base_state() -> ZSimState:
    return ZSimState(
        N=-2.0,
        a=math.exp(-2.0),
        h=1.0,
        epsilon=1.0,
        pi_epsilon=0.0,
        rho_x=0.30,
        rho_z=0.02,
        rho_y=0.68,
        J_xz=0.0,
        J_zy=0.0,
        phi_z=0.1,
        sigma_struct=0.0,
    )


def test_validate_config_and_initial_state_nominal(base_config: ZSimConfig, base_state: ZSimState) -> None:
    assert validate_config(base_config) is base_config
    assert validate_initial_state(base_state, base_config) is base_state


def test_partition_signature_matches_locked_dims(base_config: ZSimConfig) -> None:
    assert partition_signature(base_config) == (3, 2, 6)


def test_ks_direct_xy_path_passes_for_nominal_config(base_config: ZSimConfig) -> None:
    assert ks_direct_xy_path(base_config) is None


def test_ks_rank_overflow_passes_for_nominal_state(base_config: ZSimConfig, base_state: ZSimState) -> None:
    assert ks_rank_overflow(base_state, base_config) is None


def test_ks_partition_collapse_passes_for_nominal_config(base_config: ZSimConfig) -> None:
    assert ks_partition_collapse(base_config) is None


def test_ks_nonphysical_state_triggers_on_negative_density(base_state: ZSimState) -> None:
    trigger = ks_nonphysical_state(base_state.replace(rho_x=-0.1))
    assert trigger is not None
    assert trigger.code == "KS-4"


def test_ks_epistemic_overclaim_triggers_for_stronger_public_claim() -> None:
    labels = {
        "phase_closure": LabeledValue(
            name="phase_closure",
            value="bounded_sine",
            status=Status.TRANSLATED,
            rationale="v0.1 engineering closure",
        )
    }
    claims = {"phase_closure": Status.PROVEN}
    trigger = ks_epistemic_overclaim(claims, labels)
    assert trigger is not None
    assert trigger.code == "KS-5"


def test_run_kill_switches_returns_ok_report_for_nominal_inputs(base_config: ZSimConfig, base_state: ZSimState) -> None:
    report = run_kill_switches(base_state, base_config)
    assert isinstance(report, KillSwitchReport)
    assert report.ok is True
    assert report.triggers == ()


def test_run_kill_switches_collects_nonphysical_and_epistemic_triggers(base_config: ZSimConfig, base_state: ZSimState) -> None:
    labels = {
        "epsilon_potential": LabeledValue(
            name="epsilon_potential",
            value="quartic",
            status=Status.TRANSLATED,
            rationale="reduced v0.1 closure",
        )
    }
    claims = {"epsilon_potential": Status.PROVEN}
    report = run_kill_switches(base_state.replace(rho_y=-1.0), base_config, claims=claims, labels=labels)
    codes = {trigger.code for trigger in report.triggers}
    assert report.ok is False
    assert {"KS-4", "KS-5"}.issubset(codes)


def test_emit_run_report_is_serializable(base_config: ZSimConfig, base_state: ZSimState) -> None:
    report = run_kill_switches(base_state, base_config)
    payload = emit_run_report(report)
    assert payload["ok"] is True
    assert payload["triggers"] == []
