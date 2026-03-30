import math

from zsim.core import ZSimConfig
from zsim.observables import (
    H_like,
    compile_observables,
    compute_density_observables,
    compute_entropy_observables,
    compute_expansion_observables,
    compute_external_proxies,
    compute_structural_diagnostics,
    effective_w,
    mediation_efficiency,
    phase_lock_index,
    sector_asymmetry,
    shannon_sector_entropy,
)


def _state():
    cfg = ZSimConfig.from_yaml("configs/base.yaml")
    state = cfg.make_initial_state().replace(J_xz=0.2, J_zy=0.1, sigma_struct=0.7)
    return cfg, state


def test_density_observables_match_state_fractions():
    cfg, state = _state()
    obs = compute_density_observables(state)
    assert math.isclose(obs.rho_total, 1.0)
    assert math.isclose(obs.omega_x, 0.30)
    assert math.isclose(obs.omega_z, 0.02)
    assert math.isclose(obs.omega_y, 0.68)
    assert math.isclose(obs.sector_asymmetry, abs(0.30 - 0.68))


def test_effective_w_matches_density_weighted_closure():
    cfg, state = _state()
    expected = cfg.closure.wx * 0.30 + cfg.closure.wz * 0.02 + cfg.closure.wy * 0.68
    assert math.isclose(effective_w(state, cfg), expected)
    assert math.isclose(H_like(state), state.h)


def test_entropy_observables_are_bounded_and_consistent():
    _, state = _state()
    entropy = compute_entropy_observables(state)
    assert math.isclose(entropy.sigma_struct, 0.7)
    assert math.isclose(entropy.phase_lock_index, 1.0)
    assert entropy.shannon_sector_entropy > 0.0
    assert math.isclose(phase_lock_index(state), 1.0)
    assert math.isclose(shannon_sector_entropy(state), entropy.shannon_sector_entropy)


def test_structural_diagnostics_include_rank_and_gate():
    cfg, state = _state()
    diag = compute_structural_diagnostics(state, cfg)
    assert diag.rank_xy_proxy <= 2.0
    assert 0.0 <= diag.mediation_efficiency <= 1.0
    assert math.isclose(diag.phase_gate_value, 0.0)
    assert math.isclose(diag.sigma_struct, 0.7)
    assert math.isclose(diag.sector_asymmetry, sector_asymmetry(state))


def test_external_proxies_are_explicitly_proxy_like():
    cfg, state = _state()
    proxy = compute_external_proxies(state, cfg)
    assert 0.0 <= proxy.delta_neff_proxy <= 1.0
    assert 0.0 <= proxy.bbn_support_proxy <= 1.0
    assert proxy.ewsb_support_proxy == 0.0  # phase gate is zero at phi_z = 0 in bounded_sine mode
    assert 0.0 <= proxy.decoherence_proxy <= 1.0


def test_compile_observables_returns_flat_payload():
    cfg, state = _state()
    payload = compile_observables(state, cfg)
    for key in (
        "rho_total",
        "omega_x",
        "omega_z",
        "omega_y",
        "H_like",
        "w_eff",
        "sigma_struct",
        "phase_lock_index",
        "rank_xy_proxy",
        "mediation_efficiency",
        "delta_neff_proxy",
        "bbn_support_proxy",
        "ewsb_support_proxy",
        "decoherence_proxy",
    ):
        assert key in payload


def test_mediation_efficiency_zero_when_budget_and_currents_zero():
    cfg = ZSimConfig.from_yaml("configs/base.yaml")
    state = cfg.make_initial_state().replace(rho_x=0.0, rho_z=0.0, rho_y=0.0, J_xz=0.0, J_zy=0.0)
    assert mediation_efficiency(state) == 0.0


def test_expansion_bundle_to_dict_is_serializable():
    cfg, state = _state()
    bundle = compute_expansion_observables(state, cfg)
    assert bundle.to_dict() == {"H_like": state.h, "w_eff": effective_w(state, cfg)}
