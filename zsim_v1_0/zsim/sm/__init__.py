"""Z-Sim v1.0 — Standard Model Predictions from Polyhedral Geometry.

This package derives Standard Model parameters from A = 35/437
and the 11-dimensional register (Z,X,Y) = (2,3,6).

Modules:
    gauge_couplings  — α_s, sin²θ_W, α₂, β-coefficients, α_EM NLO
    ewsb             — Higgs VEV, top mass prediction, λ(UV)=0
    icosahedral      — A₅ representation engine (60 rotations, 5 irreps)
    yukawa           — Yukawa tensor, fermion mass ratios, CKM angles
    neutrino         — Type-I seesaw, HNL mass, BBN safety
    report           — Unified pull table and SM prediction summary

Source papers: ZS-S1 (gauge), ZS-S4 (EWSB), ZS-M8 (α_EM),
               ZS-M9 (McKay), ZS-M10/M11 (Yukawa/CKM), ZS-S2 (neutrino)
"""

__version__ = "1.0.0"
