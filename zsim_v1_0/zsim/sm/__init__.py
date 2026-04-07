"""Z-Sim v1.0 — Standard Model Predictions from Polyhedral Geometry.

This package derives Standard Model parameters from A = 35/437
and the 11-dimensional register (Z,X,Y) = (2,3,6).

Modules:
    gauge_couplings  — α_s, sin²θ_W, α₂, β-coefficients, α_EM NLO
    ewsb             — Higgs VEV, top mass prediction, λ(UV)=0
    icosahedral      — A₅ representation engine (60 rotations, 5 irreps),
                       §9.5 lepton-channel character lift, TI golden-ratio
                       spectral quantization (April 2026 update)
    yukawa           — Yukawa tensor, fermion mass ratios, CKM angles
    neutrino         — Type-I seesaw, HNL mass, BBN safety
    qcd_spectral     — ZS-S7 Λ_QCD, glueball mass, b_0, n_f
                       (April 2026, 55-paper release)
    m0_lattice       — Schur complement on TI for α_EM NLO (X-side T1-2)
    report           — Unified pull table and SM prediction summary

Source papers: ZS-S1 (gauge), ZS-S4 (EWSB), ZS-M8 (α_EM),
               ZS-M9 (McKay), ZS-M10/M11 (Yukawa/CKM), ZS-S2 (neutrino),
               ZS-S7 (QCD spectral, April 2026)

April 2026 updates (first + second batch):
    ZS-M11 §9.5.4: Singlet ν_R Yukawa Vanishing (PROVEN)
    ZS-M11 §9.5.5: Lepton-Channel Character Lift (PROVEN)
    ZS-M11 §9.5.6: ρ₂-Sector Golden-Ratio Spectral Quantization (COMPUTED)
    ZS-S2  §8.1:   F-S2-IO3 closure → ε_lepton(LO) = κ² = A/Q (DERIVED at LO)
    ZS-S7  v1.0:   Λ_QCD = 264 MeV, m(0⁺⁺) = 1.791 GeV, b_0 = 23/3, n_f = 5
    Book   §G.2:   T1-3 entry, X↔Y reciprocal duality registration
"""

__version__ = "1.0.0"

