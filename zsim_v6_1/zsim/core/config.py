"""Typed configuration loader and validator for Z-Sim v3.1.

This module turns YAML or dictionary input into a validated, explicit runtime
configuration. It keeps theory-side locked constants separate from translated
engineering defaults, and provides a single place where structural constraints
such as A and sector dimensions are checked.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping

import yaml

from .constants import A_FRACTION, A_LOCKED, Q_TOTAL, get_sector_dims
from .exceptions import ConfigLoadError, ConfigValidationError
from .state import ZSimState


def _ensure_mapping(value: Any, *, name: str) -> Mapping[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, Mapping):
        raise ConfigValidationError(f"Section '{name}' must be a mapping, got {type(value).__name__}.")
    return value


def _parse_float(value: Any, *, name: str) -> float:
    if isinstance(value, bool):
        raise ConfigValidationError(f"Field '{name}' must be numeric, not bool.")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ConfigValidationError(f"Field '{name}' cannot be empty.")
        if "/" in text:
            try:
                return float(Fraction(text))
            except (ValueError, ZeroDivisionError) as exc:
                raise ConfigValidationError(f"Field '{name}' has invalid fraction '{value}'.") from exc
        try:
            return float(text)
        except ValueError as exc:
            raise ConfigValidationError(f"Field '{name}' has invalid numeric value '{value}'.") from exc
    raise ConfigValidationError(f"Field '{name}' must be numeric, got {type(value).__name__}.")


def _parse_int(value: Any, *, name: str) -> int:
    if isinstance(value, bool):
        raise ConfigValidationError(f"Field '{name}' must be an integer, not bool.")
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        text = value.strip()
        if text.isdigit() or (text.startswith("-") and text[1:].isdigit()):
            return int(text)
    raise ConfigValidationError(f"Field '{name}' must be an integer, got {value!r}.")


def _parse_bool(value: Any, *, name: str) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        text = value.strip().lower()
        if text in {"true", "yes", "1", "on"}:
            return True
        if text in {"false", "no", "0", "off"}:
            return False
    raise ConfigValidationError(f"Field '{name}' must be a boolean, got {value!r}.")


def _parse_string(value: Any, *, name: str) -> str:
    text = str(value).strip()
    if not text:
        raise ConfigValidationError(f"Field '{name}' must be a non-empty string.")
    return text


@dataclass(frozen=True, slots=True)
class ModelConfig:
    A: float = A_LOCKED
    dims: dict[str, int] = field(default_factory=get_sector_dims)
    enforce_zero_xy: bool = True
    enforce_rank2_xy: bool = True

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any]) -> "ModelConfig":
        data = _ensure_mapping(payload, name="model")
        if "A" not in data:
            raise ConfigValidationError("Section 'model' must define locked constant 'A'.")
        if "dims" not in data:
            raise ConfigValidationError("Section 'model' must define sector dimensions 'dims'.")

        dims_map = _ensure_mapping(data["dims"], name="model.dims")
        dims: dict[str, int] = {}
        for key in ("X", "Z", "Y"):
            if key not in dims_map:
                raise ConfigValidationError(f"Section 'model.dims' is missing '{key}'.")
            dims[key] = _parse_int(dims_map[key], name=f"model.dims.{key}")

        obj = cls(
            A=_parse_float(data["A"], name="model.A"),
            dims=dims,
            enforce_zero_xy=_parse_bool(data.get("enforce_zero_xy", True), name="model.enforce_zero_xy"),
            enforce_rank2_xy=_parse_bool(data.get("enforce_rank2_xy", True), name="model.enforce_rank2_xy"),
        )
        obj.validate()
        return obj

    def validate(self) -> "ModelConfig":
        if self.A != A_LOCKED:
            raise ConfigValidationError(
                f"model.A must equal locked A={A_FRACTION.numerator}/{A_FRACTION.denominator}, got {self.A}."
            )
        expected_dims = get_sector_dims()
        if self.dims != expected_dims:
            raise ConfigValidationError(f"model.dims must equal locked dimensions {expected_dims}, got {self.dims}.")
        if sum(self.dims.values()) != Q_TOTAL:
            raise ConfigValidationError(f"Sector dimensions must sum to Q_TOTAL={Q_TOTAL}.")
        if not self.enforce_zero_xy:
            raise ConfigValidationError("v0.1 requires model.enforce_zero_xy = true.")
        if not self.enforce_rank2_xy:
            raise ConfigValidationError("v0.1 requires model.enforce_rank2_xy = true.")
        return self


@dataclass(frozen=True, slots=True)
class ClosureConfig:
    wx: float = 0.0
    wz: float = -1.0
    wy: float = 1.0 / 3.0
    gamma_xz: float = 0.1
    gamma_zy: float = 0.1
    alpha_xz: float = 1.0
    alpha_zy: float = 1.0
    phase_mode: str = "bounded_sine"
    epsilon_potential: str = "quartic"
    lam: float = 1.79  # λ in V(ε) = (λ/4)(ε²−1)² [DERIVED, ZS-F1 §4.4]
    phase_source_mode: str = "full_state"
    mediation_mode: str = "raw_contrast"
    epsilon_source_mode: str = "gate_current_difference"
    h_closure_mode: str = "sqrt_sum"

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any] | None) -> "ClosureConfig":
        data = _ensure_mapping(payload, name="closure")
        obj = cls(
            wx=_parse_float(data.get("wx", 0.0), name="closure.wx"),
            wz=_parse_float(data.get("wz", -1.0), name="closure.wz"),
            wy=_parse_float(data.get("wy", 1.0 / 3.0), name="closure.wy"),
            gamma_xz=_parse_float(data.get("gamma_xz", 0.1), name="closure.gamma_xz"),
            gamma_zy=_parse_float(data.get("gamma_zy", 0.1), name="closure.gamma_zy"),
            alpha_xz=_parse_float(data.get("alpha_xz", 1.0), name="closure.alpha_xz"),
            alpha_zy=_parse_float(data.get("alpha_zy", 1.0), name="closure.alpha_zy"),
            phase_mode=_parse_string(data.get("phase_mode", "bounded_sine"), name="closure.phase_mode"),
            epsilon_potential=_parse_string(data.get("epsilon_potential", "quartic"), name="closure.epsilon_potential"),
            lam=_parse_float(data.get("lam", 1.79), name="closure.lam"),
            phase_source_mode=_parse_string(data.get("phase_source_mode", "full_state"), name="closure.phase_source_mode"),
            mediation_mode=_parse_string(data.get("mediation_mode", "raw_contrast"), name="closure.mediation_mode"),
            epsilon_source_mode=_parse_string(data.get("epsilon_source_mode", "gate_current_difference"), name="closure.epsilon_source_mode"),
            h_closure_mode=_parse_string(data.get("h_closure_mode", "sqrt_sum"), name="closure.h_closure_mode"),
        )
        obj.validate()
        return obj

    def validate(self) -> "ClosureConfig":
        if self.phase_mode not in {"bounded_sine", "bounded_tanh", "constant", "spinor_sin2"}:
            raise ConfigValidationError(f"Unsupported closure.phase_mode: {self.phase_mode!r}.")
        if self.epsilon_potential not in {"quartic", "quadratic", "flat_test"}:
            raise ConfigValidationError(f"Unsupported closure.epsilon_potential: {self.epsilon_potential!r}.")
        if self.phase_source_mode not in {"full_state", "currents_only", "epsilon_mediator", "phase_feedback_only"}:
            raise ConfigValidationError(f"Unsupported closure.phase_source_mode: {self.phase_source_mode!r}.")
        if self.mediation_mode not in {"raw_contrast", "normalized_contrast", "tanh_contrast"}:
            raise ConfigValidationError(f"Unsupported closure.mediation_mode: {self.mediation_mode!r}.")
        if self.epsilon_source_mode not in {"gate_current_difference", "current_difference", "gate_abs_difference", "zero"}:
            raise ConfigValidationError(f"Unsupported closure.epsilon_source_mode: {self.epsilon_source_mode!r}.")
        if self.h_closure_mode not in {"sqrt_sum", "sqrt_sum_plus_epsilon", "friedmann_full"}:
            raise ConfigValidationError(f"Unsupported closure.h_closure_mode: {self.h_closure_mode!r}.")
        if self.lam < 0.0:
            raise ConfigValidationError(f"closure.lam must be non-negative, got {self.lam}.")
        for name in ("gamma_xz", "gamma_zy", "alpha_xz", "alpha_zy"):
            if getattr(self, name) < 0.0:
                raise ConfigValidationError(f"closure.{name} must be non-negative.")
        return self

    def mode_summary(self) -> dict[str, str]:
        return {
            "phase_mode": self.phase_mode,
            "phase_source_mode": self.phase_source_mode,
            "mediation_mode": self.mediation_mode,
            "epsilon_source_mode": self.epsilon_source_mode,
            "h_closure_mode": self.h_closure_mode,
            "epsilon_potential": self.epsilon_potential,
        }


@dataclass(frozen=True, slots=True)
class InitialConfig:
    N0: float = -18.0
    a0: float = 1.522997974e-8
    h0: float = 1.0
    epsilon0: float = 1.0
    pi_epsilon0: float = 0.0
    rho_x0: float = 0.30
    rho_z0: float = 0.02
    rho_y0: float = 0.68
    phi_z0: float = 0.0
    sigma_struct0: float = 0.0

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any] | None) -> "InitialConfig":
        data = _ensure_mapping(payload, name="initial")
        obj = cls(
            N0=_parse_float(data.get("N0", -18.0), name="initial.N0"),
            a0=_parse_float(data.get("a0", 1.522997974e-8), name="initial.a0"),
            h0=_parse_float(data.get("h0", 1.0), name="initial.h0"),
            epsilon0=_parse_float(data.get("epsilon0", 1.0), name="initial.epsilon0"),
            pi_epsilon0=_parse_float(data.get("pi_epsilon0", 0.0), name="initial.pi_epsilon0"),
            rho_x0=_parse_float(data.get("rho_x0", 0.30), name="initial.rho_x0"),
            rho_z0=_parse_float(data.get("rho_z0", 0.02), name="initial.rho_z0"),
            rho_y0=_parse_float(data.get("rho_y0", 0.68), name="initial.rho_y0"),
            phi_z0=_parse_float(data.get("phi_z0", 0.0), name="initial.phi_z0"),
            sigma_struct0=_parse_float(data.get("sigma_struct0", 0.0), name="initial.sigma_struct0"),
        )
        obj.validate()
        return obj

    def validate(self) -> "InitialConfig":
        if self.a0 <= 0.0:
            raise ConfigValidationError("initial.a0 must be strictly positive.")
        for name in ("rho_x0", "rho_z0", "rho_y0"):
            if getattr(self, name) < 0.0:
                raise ConfigValidationError(f"initial.{name} must be non-negative.")
        return self

    def to_state(self) -> ZSimState:
        return ZSimState(
            N=self.N0,
            a=self.a0,
            h=self.h0,
            epsilon=self.epsilon0,
            pi_epsilon=self.pi_epsilon0,
            rho_x=self.rho_x0,
            rho_z=self.rho_z0,
            rho_y=self.rho_y0,
            J_xz=0.0,
            J_zy=0.0,
            phi_z=self.phi_z0,
            sigma_struct=self.sigma_struct0,
        ).validate()


@dataclass(frozen=True, slots=True)
class SolverConfig:
    method: str = "RK45"
    rtol: float = 1e-8
    atol: float = 1e-10
    N_end: float = 5.0
    max_step: float = 0.05
    projection_every: int = 1

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any] | None) -> "SolverConfig":
        data = _ensure_mapping(payload, name="solver")
        obj = cls(
            method=str(data.get("method", "RK45")),
            rtol=_parse_float(data.get("rtol", 1e-8), name="solver.rtol"),
            atol=_parse_float(data.get("atol", 1e-10), name="solver.atol"),
            N_end=_parse_float(data.get("N_end", 5.0), name="solver.N_end"),
            max_step=_parse_float(data.get("max_step", 0.05), name="solver.max_step"),
            projection_every=_parse_int(data.get("projection_every", 1), name="solver.projection_every"),
        )
        obj.validate()
        return obj

    def validate(self) -> "SolverConfig":
        if self.method not in {"RK45", "BDF"}:
            raise ConfigValidationError(f"Unsupported solver.method: {self.method!r}.")
        if self.rtol <= 0.0 or self.atol <= 0.0:
            raise ConfigValidationError("solver.rtol and solver.atol must be strictly positive.")
        if self.max_step <= 0.0:
            raise ConfigValidationError("solver.max_step must be strictly positive.")
        if self.projection_every < 1:
            raise ConfigValidationError("solver.projection_every must be >= 1.")
        return self


@dataclass(frozen=True, slots=True)
class OutputConfig:
    save_state_csv: bool = True
    save_observables_csv: bool = True
    save_diagnostics_json: bool = True
    make_plots: bool = True

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any] | None) -> "OutputConfig":
        data = _ensure_mapping(payload, name="outputs")
        return cls(
            save_state_csv=_parse_bool(data.get("save_state_csv", True), name="outputs.save_state_csv"),
            save_observables_csv=_parse_bool(data.get("save_observables_csv", True), name="outputs.save_observables_csv"),
            save_diagnostics_json=_parse_bool(data.get("save_diagnostics_json", True), name="outputs.save_diagnostics_json"),
            make_plots=_parse_bool(data.get("make_plots", True), name="outputs.make_plots"),
        )


@dataclass(frozen=True, slots=True)
class ZSimConfig:
    model: ModelConfig
    closure: ClosureConfig = field(default_factory=ClosureConfig)
    initial: InitialConfig = field(default_factory=InitialConfig)
    solver: SolverConfig = field(default_factory=SolverConfig)
    outputs: OutputConfig = field(default_factory=OutputConfig)

    @classmethod
    def from_mapping(cls, payload: Mapping[str, Any]) -> "ZSimConfig":
        root = _ensure_mapping(payload, name="root")
        if "model" not in root:
            raise ConfigValidationError("Configuration must define top-level 'model' section.")

        obj = cls(
            model=ModelConfig.from_mapping(root.get("model")),
            closure=ClosureConfig.from_mapping(root.get("closure")),
            initial=InitialConfig.from_mapping(root.get("initial")),
            solver=SolverConfig.from_mapping(root.get("solver")),
            outputs=OutputConfig.from_mapping(root.get("outputs")),
        )
        obj.validate()
        return obj

    @classmethod
    def from_yaml(cls, path: str | Path) -> "ZSimConfig":
        config_path = Path(path)
        if not config_path.exists():
            raise ConfigLoadError(f"Configuration file does not exist: {config_path}")
        try:
            raw = yaml.safe_load(config_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            raise ConfigLoadError(f"Failed to parse YAML config: {config_path}") from exc
        except OSError as exc:
            raise ConfigLoadError(f"Failed to read config file: {config_path}") from exc

        if raw is None:
            raise ConfigLoadError(f"Configuration file is empty: {config_path}")
        return cls.from_mapping(raw)

    def validate(self) -> "ZSimConfig":
        self.model.validate()
        self.closure.validate()
        self.initial.validate()
        self.solver.validate()
        self.outputs
        return self

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def make_initial_state(self) -> ZSimState:
        return self.initial.to_state()

    def replace_closure(self, **updates: Any) -> "ZSimConfig":
        closure = replace(self.closure, **updates).validate()
        return replace(self, closure=closure).validate()

    def replace_phase_mode(self, phase_mode: str) -> "ZSimConfig":
        return self.replace_closure(phase_mode=phase_mode)


__all__ = [
    "ConfigLoadError",
    "ConfigValidationError",
    "ModelConfig",
    "ClosureConfig",
    "InitialConfig",
    "SolverConfig",
    "OutputConfig",
    "ZSimConfig",
]
