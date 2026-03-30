"""Z-Sim v1.0 — Electroweak Symmetry Breaking from Polyhedral Geometry.

Canonical source: ZS-S4 v6.3.0 (Factorized Determinant Theorem)

Higgs VEV derivation chain:
    1. d_eff = X + Y = Q − Z = 9                    [PROVEN, three routes]
    2. γ_CW = (V+F)_X / d_eff = 38/9                [DERIVED]
    3. C_M^sp = Q·ln(Z) + ln(X) = 8.7232            [DERIVED, from ZS-Q3 spectrum]
    4. v = M_P × exp(−γ_CW × C_M^sp) = 245.93 GeV  [DERIVED, 0.12% from 246.22]

Path B top mass prediction:
    5. λ(Λ_comp) = 0                                 [PROVEN]
    6. SM RG running → m_t = 171.5 ± 0.5 GeV        [TESTABLE, FCC-ee ~2040]
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Final

from zsim.core.constants import (
    A_LOCKED, Q_TOTAL, DIM_X, DIM_Y, DIM_Z, G_MUB,
    VF_TO, D_EFF, GAMMA_CW, C_M_SPECTRAL,
    M_PLANCK_GEV, HIGGS_VEV, HIGGS_VEV_EXPONENT,
    TOP_MASS_PRED, HIGGS_MASS_HYPO,
    PDG_HIGGS_VEV, PDG_HIGGS_MASS, PDG_TOP_MASS, PDG_TOP_MASS_ERR,
)


@dataclass(frozen=True)
class EWSBPrediction:
    """A single EWSB prediction with provenance."""
    name: str
    symbol: str
    z_spin_value: float
    z_spin_exact: str
    observed_value: float
    observed_error: float
    deviation_pct: float
    status: str
    source_paper: str

    def to_dict(self) -> dict[str, object]:
        return self.__dict__.copy()


def derivation_chain_higgs_vev() -> tuple[str, ...]:
    """Return the complete derivation chain for the Higgs VEV."""
    return (
        f"d_eff = X + Y = {DIM_X} + {DIM_Y} = {D_EFF} [PROVEN, three independent routes: KK/Heat/Instanton]",
        f"γ_CW = (V+F)_X / d_eff = {VF_TO}/{D_EFF} = 38/9 = {GAMMA_CW:.4f} [DERIVED]",
        f"C_M^sp = Q·ln(Z) + ln(X) = {Q_TOTAL}·ln({DIM_Z}) + ln({DIM_X}) = {C_M_SPECTRAL:.4f} [DERIVED]",
        f"  (from ZS-Q3 Hodge coexact spectrum: λ=8(×3)={{Z³}}, λ=12(×1)={{Z²X}})",
        f"Exponent = −γ_CW × C_M^sp = −{GAMMA_CW:.4f} × {C_M_SPECTRAL:.4f} = {HIGGS_VEV_EXPONENT:.3f}",
        f"v = M_P × exp(exponent) = {M_PLANCK_GEV:.3e} × exp({HIGGS_VEV_EXPONENT:.3f}) = {HIGGS_VEV:.2f} GeV",
        f"Observed: {PDG_HIGGS_VEV} GeV, deviation = {abs(HIGGS_VEV - PDG_HIGGS_VEV)/PDG_HIGGS_VEV*100:.2f}%",
    )


def derivation_chain_top_mass() -> tuple[str, ...]:
    """Return the derivation chain for the top quark mass prediction."""
    return (
        "λ(Λ_comp) = 0 [PROVEN, ZS-S4 §6.10: conformal symmetry at UV scale]",
        "SM RG running (2-loop) from λ=0 at M_P scale",
        f"m_t^pred = {TOP_MASS_PRED} ± 0.5 GeV [TESTABLE]",
        f"PDG 2024: m_t = {PDG_TOP_MASS} ± {PDG_TOP_MASS_ERR} GeV",
        f"Gap = {PDG_TOP_MASS - TOP_MASS_PRED:.2f} GeV decomposed as:",
        "  UV scale offset ~ 2.7 GeV + m_t uncertainty ~ 1.4 GeV",
        "Decisive test: FCC-ee (~2040), Δm_t < 50 MeV",
    )


def compute_all_ewsb_predictions() -> list[EWSBPrediction]:
    """Compute all EWSB predictions."""
    return [
        EWSBPrediction(
            name="Higgs VEV",
            symbol="v",
            z_spin_value=HIGGS_VEV,
            z_spin_exact="M_P × 2^{-418/9} × 3^{-38/9}",
            observed_value=PDG_HIGGS_VEV,
            observed_error=0.01,  # sub-percent known
            deviation_pct=abs(HIGGS_VEV - PDG_HIGGS_VEV) / PDG_HIGGS_VEV * 100,
            status="DERIVED",
            source_paper="ZS-S4 v6.3.0 §6.12",
        ),
        EWSBPrediction(
            name="Top quark mass (Path B)",
            symbol="m_t",
            z_spin_value=TOP_MASS_PRED,
            z_spin_exact="λ(Λ)=0 + SM RG",
            observed_value=PDG_TOP_MASS,
            observed_error=PDG_TOP_MASS_ERR,
            deviation_pct=abs(TOP_MASS_PRED - PDG_TOP_MASS) / PDG_TOP_MASS * 100,
            status="TESTABLE",
            source_paper="ZS-S4 v6.3.0 §6.10",
        ),
        EWSBPrediction(
            name="Higgs mass (hypothesis)",
            symbol="m_H",
            z_spin_value=HIGGS_MASS_HYPO,
            z_spin_exact="v/Z × √(1+A/Z)",
            observed_value=PDG_HIGGS_MASS,
            observed_error=0.17,
            deviation_pct=abs(HIGGS_MASS_HYPO - PDG_HIGGS_MASS) / PDG_HIGGS_MASS * 100,
            status="HYPOTHESIS",
            source_paper="ZS-S4 v6.3.0 §6.12",
        ),
    ]


def spectral_topological_duality() -> dict[str, object]:
    """Document the Spectral-Topological Duality (ZS-S4 §6.12).

    Two independent routes to the Higgs VEV:
        §6.11 MBP  = Reidemeister torsion (S_cl = 35π/3)  [topological]
        §6.12 SVev = Ray-Singer torsion (C_M^sp)           [spectral]
    The difference δ = −1.20 matches the estimated c₁ ≈ −1.0 1-loop correction.
    """
    s_cl = 35.0 * math.pi / 3.0
    ln_v_spectral = HIGGS_VEV_EXPONENT + math.log(M_PLANCK_GEV)
    ln_v_topological = math.log(M_PLANCK_GEV) - s_cl  # approximate

    return {
        "spectral_route": {
            "method": "Ray-Singer torsion (C_M^sp)",
            "exponent": HIGGS_VEV_EXPONENT,
            "v_GeV": HIGGS_VEV,
        },
        "topological_route": {
            "method": "Reidemeister torsion (S_cl = 35π/3)",
            "S_cl": s_cl,
        },
        "duality_gap_delta": -1.20,
        "c1_loop_estimate": -1.0,
    }


def print_ewsb_summary() -> None:
    """Print formatted EWSB prediction summary."""
    preds = compute_all_ewsb_predictions()
    print("=" * 72)
    print("  Z-Spin EWSB Predictions (ZS-S4 v6.3.0)")
    print("  Factorized Determinant Theorem | Zero free parameters")
    print("=" * 72)
    for p in preds:
        print(f"\n  {p.name} [{p.status}]")
        print(f"    Z-Spin:   {p.symbol} = {p.z_spin_exact}")
        print(f"              = {p.z_spin_value:.2f} GeV")
        print(f"    Observed: {p.observed_value} ± {p.observed_error} GeV")
        print(f"    Deviation: {p.deviation_pct:.2f}%")
        print(f"    Source:   {p.source_paper}")
    print("=" * 72)
