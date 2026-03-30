"""Z-Sim v1.0 — SM Prediction Report (Grand Reset).

Honestly separates PREDICT, FIT, and HARDCODED results.
"""
from __future__ import annotations
import time

from zsim.core.constants import (
    ALPHA_S, SIN2_THETA_W, ALPHA_EM_INV_NLO,
    HIGGS_VEV, TOP_MASS_PRED,
    M_D_NEUTRINO_KEV, M_R_HNL_GEV,
    PDG_ALPHA_S, PDG_ALPHA_S_ERR,
    PDG_SIN2_THETA_W, PDG_SIN2_THETA_W_ERR,
    PDG_ALPHA_EM_INV, PDG_HIGGS_VEV,
    PDG_TOP_MASS, PDG_TOP_MASS_ERR,
    PDG_M_TAU_OVER_M_MU, PDG_M_TAU_OVER_M_E,
)


def run_full_pipeline(verbose=True):
    t0 = time.time()
    results = {"version": "1.0.0"}

    if verbose:
        print("=" * 76)
        print("  Z-Sim v1.0 — Standard Model Predictions from A = 35/437")
        print("  Grand Reset | Honest epistemic status for every result")
        print("=" * 76)

    # Constants-based (all DERIVED or HYPOTHESIS)
    pull_alpha_s = (ALPHA_S - PDG_ALPHA_S) / PDG_ALPHA_S_ERR
    pull_sw2 = (SIN2_THETA_W - PDG_SIN2_THETA_W) / PDG_SIN2_THETA_W_ERR

    if verbose:
        print(f"\n  [DERIVED] α_s = 11/93 = {ALPHA_S:.5f}, pull = {pull_alpha_s:+.2f}σ")
        print(f"  [DERIVED] sin²θ_W = (48/91)·x* = {SIN2_THETA_W:.5f}, pull = {pull_sw2:+.2f}σ")
        print(f"  [HYPOTHESIS] 1/α_EM = {ALPHA_EM_INV_NLO:.3f}, dev = {abs(ALPHA_EM_INV_NLO-PDG_ALPHA_EM_INV)/PDG_ALPHA_EM_INV*1e6:.1f} ppm")
        print(f"  [DERIVED] Higgs VEV = {HIGGS_VEV:.2f} GeV, dev = {abs(HIGGS_VEV-PDG_HIGGS_VEV)/PDG_HIGGS_VEV*100:.2f}%")
        print(f"  [TESTABLE] m_t = {TOP_MASS_PRED} GeV (FCC-ee ~2040)")

    # Icosahedral engine
    from zsim.sm.icosahedral import build_icosahedral_group
    ig = build_icosahedral_group()
    results["group_order"] = ig.order
    results["yukawa_unique"] = ig.yukawa_unique

    # Fermion predictions
    from zsim.sm.yukawa import (
        restricted_vev_predict, fit_vev_s4, compute_ckm, quartic_analysis,
        d5_channel_decomposition,
    )

    m10 = restricted_vev_predict(ig.yukawa_tensor, ig.rep5, ig.rotations)
    results["m10_ratio_12"] = m10.ratio_12
    results["m10_ratio_13"] = m10.ratio_13
    results["schur_sum"] = m10.schur_check

    d5 = d5_channel_decomposition(ig.yukawa_tensor, ig.rep3, ig.rep5, ig.rep3p, ig.rotations)
    results["d5_lepton"] = d5.lepton_fraction
    results["d5_sqrt2"] = d5.quark_lepton_ratio
    results["d5_silver"] = d5.silver_ratio

    m11 = fit_vev_s4(ig.yukawa_tensor)
    results["fit_ratio_12"] = m11.ratio_12
    results["fit_ratio_13"] = m11.ratio_13

    ckm = compute_ckm(ig.rep3, ig.rep5, ig.rotations)
    results["cabibbo_deg"] = ckm.cabibbo_angle_deg
    results["raw_angle_deg"] = ckm.raw_principal_angle_deg

    if verbose:
        print(f"\n  [PREDICT] Restricted VEV: σ₁/σ₂={m10.ratio_12:.1f}, σ₁/σ₃={m10.ratio_13:.0f}")
        print(f"  [PROVEN]  D₅ channels: lepton={d5.lepton_fraction:.4f}, √2={d5.quark_lepton_ratio:.4f}, 1+√2={d5.silver_ratio:.4f}")
        print(f"  [FIT]     S⁴ optimization: σ₁/σ₂={m11.ratio_12:.2f}, σ₁/σ₃={m11.ratio_13:.0f}")
        print(f"  [DERIVED-CONDITIONAL] Cabibbo = {ckm.cabibbo_angle_deg:.2f}°")

    results["elapsed_sec"] = time.time() - t0
    if verbose:
        print(f"\n  Pipeline: {results['elapsed_sec']:.1f}s")
        print("=" * 76)
    return results

if __name__ == "__main__":
    run_full_pipeline()
