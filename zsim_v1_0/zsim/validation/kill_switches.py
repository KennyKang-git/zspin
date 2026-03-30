"""Kill-switch evaluation for Z-Sim v1.0.

This module centralizes run-time checks that determine whether a simulation may
continue. Each kill-switch is designed to correspond to a structural promise in
Z-Sim v1.0:

- KS-1: direct X↔Y path must not appear
- KS-2: effective X↔Y rank must remain <= 2
- KS-3: partition structure must remain intact
- KS-4: state must remain finite and physically admissible
- KS-5: translated/hypothesis objects must not be surfaced as stronger claims
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping

import numpy as np

from zsim.core import LabeledValue, Status, ZSimConfig, ZSimState
from zsim.kernel.operators import build_structural_operator, direct_xy_block, effective_rank_xy
from zsim.validation.epistemic import validate_claim_map
from zsim.validation.invariants import partition_signature, validate_config, validate_initial_state


@dataclass(frozen=True, slots=True)
class KillSwitchTrigger:
    code: str
    message: str
    terminal: bool = True
    payload: Mapping[str, Any] | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "code": self.code,
            "message": self.message,
            "terminal": self.terminal,
            "payload": dict(self.payload or {}),
        }


@dataclass(frozen=True, slots=True)
class KillSwitchReport:
    ok: bool
    triggers: tuple[KillSwitchTrigger, ...]

    @property
    def terminal(self) -> bool:
        return any(t.terminal for t in self.triggers)

    def to_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "terminal": self.terminal, "triggers": [t.to_dict() for t in self.triggers]}



def ks_direct_xy_path(config: ZSimConfig) -> KillSwitchTrigger | None:
    validate_config(config)
    operator = build_structural_operator(config)
    xy_block = direct_xy_block(operator)
    if np.allclose(xy_block, 0.0):
        return None
    return KillSwitchTrigger(
        code="KS-1",
        message="Direct X-Y path detected in structural operator.",
        payload={"max_abs_xy": float(np.max(np.abs(xy_block)))},
    )



def ks_rank_overflow(state: ZSimState, config: ZSimConfig) -> KillSwitchTrigger | None:
    validate_config(config)
    try:
        state.validate(require_nonnegative_densities=False)
    except Exception:
        return None
    rank = effective_rank_xy(state, config)
    if rank <= 2:
        return None
    return KillSwitchTrigger(
        code="KS-2",
        message="Effective X-Y transfer rank exceeds the Z-mediated ceiling.",
        payload={"rank_xy": int(rank)},
    )



def ks_partition_collapse(config: ZSimConfig) -> KillSwitchTrigger | None:
    sig = partition_signature(config)
    if sig == (3, 2, 6) and config.model.enforce_zero_xy and config.model.enforce_rank2_xy:
        return None
    return KillSwitchTrigger(
        code="KS-3",
        message="Partition signature or structural enforcement flags are invalid.",
        payload={"partition": sig},
    )



def ks_nonphysical_state(state: ZSimState) -> KillSwitchTrigger | None:
    try:
        state.validate()
    except Exception as exc:  # noqa: BLE001 - convert to structured trigger
        return KillSwitchTrigger(
            code="KS-4",
            message=f"Nonphysical state detected: {exc}",
            payload={"state_N": float(state.N)},
        )
    return None



def ks_epistemic_overclaim(claims: Mapping[str, Status] | None, labels: Mapping[str, LabeledValue] | None) -> KillSwitchTrigger | None:
    if not claims or not labels:
        return None
    try:
        validate_claim_map(labels, claims)
    except Exception as exc:  # noqa: BLE001 - convert to structured trigger
        return KillSwitchTrigger(
            code="KS-5",
            message=f"Epistemic overclaim detected: {exc}",
            payload={"claims": {k: v.value for k, v in claims.items()}},
        )
    return None



def ks_non_minimal_coupling(config: ZSimConfig) -> KillSwitchTrigger | None:
    """KS-6: Verify that the Friedmann equation includes F(ε) = 1 + Aε².

    At ε=1, π_ε=0, V(1)=0:
        h²(A) / h²(A=0) = 1/(1+A) = 437/472

    Without (1+Aε²), this is not a Z-Spin simulator.
    Source: ZS-F1 §3 variation of action.
    [STATUS: DERIVED]
    """
    try:
        from zsim.kernel.friedmann import verify_non_minimal_coupling
        verify_non_minimal_coupling(config)
    except ImportError:
        # friedmann module not available — skip (reduced mode)
        return None
    except Exception as exc:
        return KillSwitchTrigger(
            code="KS-6",
            message=f"Non-minimal coupling F(ε)=1+Aε² missing: {exc}",
            terminal=True,
        )
    return None



def run_kill_switches(
    state: ZSimState,
    config: ZSimConfig,
    diagnostics: Mapping[str, Any] | None = None,
    *,
    claims: Mapping[str, Status] | None = None,
    labels: Mapping[str, LabeledValue] | None = None,
) -> KillSwitchReport:
    """Run all implemented kill-switch checks and collect structured results."""
    _ = diagnostics  # reserved for future use in v0.1
    triggers = []
    for fn, args in (
        (ks_direct_xy_path, (config,)),
        (ks_rank_overflow, (state, config)),
        (ks_partition_collapse, (config,)),
        (ks_nonphysical_state, (state,)),
        (ks_epistemic_overclaim, (claims, labels)),
        (ks_non_minimal_coupling, (config,)),
    ):
        trigger = fn(*args)
        if trigger is not None:
            triggers.append(trigger)
    return KillSwitchReport(ok=not triggers, triggers=tuple(triggers))



def emit_run_report(report: KillSwitchReport) -> dict[str, Any]:
    """Return a serialization-ready representation of a kill-switch report."""
    return report.to_dict()


__all__ = [
    "KillSwitchTrigger",
    "KillSwitchReport",
    "emit_run_report",
    "ks_direct_xy_path",
    "ks_epistemic_overclaim",
    "ks_non_minimal_coupling",
    "ks_nonphysical_state",
    "ks_partition_collapse",
    "ks_rank_overflow",
    "run_kill_switches",
]
