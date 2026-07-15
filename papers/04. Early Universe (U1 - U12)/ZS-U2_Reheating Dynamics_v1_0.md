**ZS-U2**

**Reheating Dynamics:**  
**Dual-Channel Decay, Three-Timescale Hierarchy,**  
**Gravitational Wave Spectrum, and ε-SM Coupling**

Kenny Kang

**Version 1.0** — March 2026  
Theme: Early Universe \[ZS-U\] | Paper 2 of 8

**Verification: 24/24 PASS | Zero New U2 Fit Parameters | A\_s Normalized**

**§0. Abstract**

We derive the reheating dynamics of the Z-Spin ε-field from the base action of ZS-F1 v1.0, introducing **no new fit parameters** beyond A \= 35/437 and the Planck normalization A\_s. The ε-field couples to Standard Model particles through the conformal factor Ω² \= 1 \+ **A**ε², generating an effective coupling y\_eff \= **A**/(1+**A**) \= 35/472 ≈ 0.074. The three-timescale hierarchy T\_osc (4.7 t\_P) ≪ t\_decay (1,912 t\_P) ≪ t\_Hubble (267,410 t\_P) implies dual-channel reheating: \~406 coherent oscillations during which perturbative conformal decay and parametric resonance operate simultaneously.

The conformal decay rate Γ \= y\_eff² m³\_eff/(8π M²\_P), independently derived from the Z-Spin action, yields Γ/H\_end ≈ 140 ≫ 1 (instant reheating). The reheating temperature **T\_reh \= (30 ρ\_end/(π² g\_\*))^{1/4} ≈ 2.55 × 10¹⁵ GeV** follows from the instant reheating limit, where ρ\_end \= 1.5 λ\_inf V\_E(ε\_end) M⁴\_P includes the kinetic correction. The decay branching ratios predict 85% gluons, 7% W-bosons, and 8% B-bosons via the SM trace anomaly.

We compute the gravitational wave spectrum from three sources: the inflationary tensor background (Ω\_GW h² ≈ 5 × 10⁻¹⁸, detectable by LiteBIRD at \~9σ and DECIGO at 500× sensitivity), parametric resonance GW (peak at \~12.6 THz, unobservable), and thermal plasma GW (peak at \~67 MHz, unobservable). ZS-U2 sharpens the ZS-U1 v1.0 prediction r \= 0.0089 by eliminating the reheating-temperature uncertainty band. r\_ZS/r\_Starobinsky \= 2.63, enabling LiteBIRD to distinguish Z-Spin from Starobinsky at 6σ.

**Keywords:** reheating, trace anomaly, parametric resonance, gravitational waves, LiteBIRD, DECIGO, branching ratios, conformal coupling, instant reheating

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | ----- |
| PROVEN | Exact mathematical identity/theorem under declared definitions. |
| STANDARD | Established result in QFT/cosmology textbooks. |
| DERIVED | Quantitative consequence from Z-Spin axioms \+ standard physics. |
| VERIFIED | Numerically checked (verification suite provided). |
| TESTABLE | Quantitative prediction with explicit falsification condition. |
| HYPOTHESIS | Structural pattern without completed derivation chain. |
| OBSERVATION | Empirical pattern identified; upgrade to DERIVED pending derivation. |
| NON-CLAIM | Quantity NOT derived; honest acknowledgment of limitation. |
| WITHDRAWN | Previously claimed result found incorrect; formally retracted. |

**§1. Introduction and Motivation**

The Z-Spin action S \= ∫ d⁴x √(−g) \[½(1+**A**ε²)R − ½(∇ε)² − V(ε)\] predicts inflation (ZS-U1 v1.0), but the post-inflationary universe must thermalize. ZS-U2 derives the complete reheating process from this action, introducing zero new fit parameters beyond A \= 35/437, the A\_s normalization, and standard SM gauge couplings.

The conformal factor Ω² \= 1 \+ **A**ε² is the sole bridge between the ε-field and Standard Model matter. Through the trace anomaly of the SM energy-momentum tensor, this coupling generates decay channels to all gauge bosons. The single geometric parameter **A \= 35/437** determines the coupling strength, decay rate, branching ratios, reheating temperature, and gravitational wave spectrum.

**§2. Conformal Coupling to the Standard Model**

In the Einstein frame, the ε-field acquires an effective coupling to SM fields through the conformal transformation. The effective Yukawa-like coupling is:

*y\_eff \= A/(1+A) \= 35/472 ≈ 0.0742     (1)*

This is NOT a free parameter; it is algebraically determined by **A \= 35/437** (ZS-F2 v1.0).

*\[STATUS: DERIVED\] y\_eff from base action conformal factor. No new parameters.*

**§3. Three-Timescale Hierarchy**

Three characteristic timescales govern the post-inflationary dynamics:

**Table 1\. Three-timescale hierarchy.**

| Timescale | Expression | Value | Physical meaning |
| :---: | :---: | :---: | ----- |
| T\_osc | 2π/(m\_eff M\_P) | 4.7 t\_P | One ε-oscillation period |
| t\_decay | 8π M²\_P/(y²\_eff m³\_eff) | 1,912 t\_P | Conformal decay time |
| t\_Hubble | 1/H\_end | 267,410 t\_P | Expansion timescale |

The hierarchy T\_osc ≪ t\_decay ≪ t\_Hubble implies that the ε-field executes approximately **N\_osc ≈ 406** coherent oscillations before decaying, while the Hubble friction acts only at the longest timescale.

*Γ/H ≈ 140 ≫ 1 → instant reheating*

*\[STATUS: DERIVED \+ VERIFIED\] All timescales independently derived from A, m\_eff, λ\_inf.*

**§4. Decay Branching Ratios**

The ε-field decays to SM gauge bosons through the conformal trace anomaly. The partial width to each gauge sector is proportional to |b₀|² N\_i α²\_i, where b₀ is the 1-loop β-function coefficient:

**Table 2\. Decay branching ratios from trace-anomaly coupling.**

| Channel | b₀ (full SM) | N\_gauge | α(M\_P) | BR | Sector |
| :---: | :---: | :---: | :---: | :---: | :---: |
| ε → gg (gluons) | 7 | 8 | 0.0198 | 85.0% | SU(3) |
| ε → WW | 19/6 | 3 | 0.0206 | 7.1% | SU(2) |
| ε → BB | −41/6 | 1 | 0.0175 | 7.9% | U(1) |

*\[STATUS: DERIVED\] Standard SM trace-anomaly with Z-Spin conformal coupling.*

**§5. Reheating Temperature and Dual-Channel Dynamics**

The conformal decay rate is independently derived from the Z-Spin action:

*Γ\_pert \= y²\_eff m³\_eff / (8π M²\_P)     (2)*

where m\_eff \= √(m²\_eff\_norm) × M\_P and m²\_eff\_norm \= d²V\_E/dφ̃²|\_{ε=1} ≈ 1.79 is computed from the Einstein-frame potential (ZS-U1 v1.0). This yields Γ/H\_end ≈ 140 ≫ 1, placing the system firmly in the instant reheating regime.

In the instant reheating limit (Γ ≫ H), the reheating temperature is determined by the energy density at inflation end, not by the standard perturbative formula T \~ √(ΓM\_P):

*T\_reh \= (30 ρ\_end / (π² g\_\*))^{1/4} ≈ 2.55 × 10¹⁵ GeV     (3)*

where ρ\_end \= 1.5 × λ\_inf × V\_E(ε\_end) × M⁴\_P includes the kinetic correction factor 1.5. This is well above the leptogenesis threshold (\>10⁹ GeV, ZS-S5 v1.0) and below the GUT scale (\~2×10¹⁶ GeV). Dual-channel reheating operates: perturbative conformal decay dominates globally, while parametric resonance (q \= y\_eff ≈ 0.074, narrow regime) provides additional early-time energy transfer for approximately 35 oscillations.

*Note: The standard perturbative formula T \= (90/(π²g\_\*))^{1/4} √(ΓM\_P) yields \~3×10¹⁶ GeV, which overestimates by \~12× because it assumes a matter-dominated reheating phase. In the instant regime (Γ/H \= 140), the ρ\_end formula (Eq. 3\) is the physically correct expression.*

*\[STATUS: DERIVED\] T\_reh from ρ\_end. All inputs independently computed from A \= 35/437.*

**§6. Gravitational Wave Spectrum from Reheating**

**6.1 Source Classification**

**Table 3\. GW source classification.**

| GW Source | Peak Ω\_GW h² | Peak frequency (today) | Detectable? |
| ----- | :---: | :---: | :---: |
| Inflationary tensor (ZS-U1 v1.0) | 5.1 × 10⁻¹⁸ | Flat (10⁻¹⁸–67.5 MHz) | ✓ YES |
| Preheating parametric res. | \~7 × 10⁻¹⁸ | \~12.6 THz | ✗ NO |
| Thermal plasma | \~2 × 10⁻¹³ | \~67 MHz | ✗ NO |

*\[STATUS: DERIVED\] All from independently computed inputs (A, r, T\_reh).*

**6.2 Inflationary Tensor Background**

*Ω\_GW^{inf} h² \= (P\_t/24) × Ω\_rad h² × ⟨T²⟩ × R(g\_\*) ≈ 5.1 × 10⁻¹⁸     (4)*

High-frequency cutoff: f\_max ≈ 67.5 MHz. Because reheating is instant (Γ/H \= 140), there is no suppression of high-frequency modes below f\_max.

**r\_ZS/r\_Starobinsky \= 0.0089/0.00339 \= 2.63.** LiteBIRD (σ\_r ≈ 0.001) can distinguish Z-Spin from Starobinsky at **6σ** significance. CMB-S4 (σ\_r ≈ 5×10⁻⁴) provides complementary confirmation.

*\[STATUS: DERIVED \+ TESTABLE\] Parameter-free from ZS-U1 v1.0 \+ ZS-U2.*

**6.3 Preheating GW (Unobservable)**

f\_peak ≈ 12.6 THz (mid-infrared λ \~ 24 μm). No GW detector operates at this frequency. This is a NON-RESULT honestly reported.

**6.4 Thermal Plasma GW (Unobservable)**

f\_peak^{th} ≈ 67 MHz. The thermal plasma GW peak falls in an unobservable gap between LIGO (10–100 Hz) and no planned detector.

**§7. ε-Higgs Effective Field Theory**

At the Z₂ attractor (ε₂ \= cos(arg z\*) ≈ 0.8066), the Higgs potential rescales as V\_H^{E} \= V\_H/(1+A)² ≈ 0.857 V\_H. This is shape-invariant: the VEV v \= 246 GeV is independent of the overall potential scale.

Radiative portal coupling: ξ\_eff \~ A²/(16π²) ≈ 4×10⁻⁵ (negligible). Thermal decoupling: T\_reh/m\_ε ≈ 7.8 × 10⁻⁴ → Boltzmann suppression.

*\[STATUS: DERIVED\] Higgs parameters (m\_H, v) are NON-CLAIM (§9).*

**§8. Falsification Conditions**

**Table 4\. Falsification conditions for ZS-U2.**

| ID | Condition | Timeline | Detector |
| :---: | ----- | :---: | :---: |
| FU2-1 | r ≠ 0.0089 ± 0.002 | \~2032 | LiteBIRD |
| FU2-2 | BR deviates from SM trace anomaly by \>3σ | \~2040 | Collider \+ BBN |
| FU2-GW1 | Ω\_GW h² at 0.1 Hz differs from 5×10⁻¹⁸ by \>3× | \~2040s | DECIGO |
| FU2-GW2 | Preheating GW detected at f \< 10⁶ Hz | \~2040s | Any GW detector |

**§9. Non-Claims (Honest Limitations)**

**NC1:** Higgs mass m\_H \= 125.25 GeV is NOT derived from A. NON-CLAIM.

**NC2:** Higgs VEV v \= 246 GeV is NOT derived from A. NON-CLAIM.

**NC3:** Reheating GW detectability at f \> 10⁶ Hz is a NON-RESULT.

**NC4:** Sector interpretation (I\_h ↔ oscillation, O\_h ↔ lattice) is HYPOTHESIS.

**§10. Discussion and Conclusions**

ZS-U2 establishes the complete reheating dynamics of Z-Spin Cosmology from **A \= 35/437** with no new U2 fit parameters. The conformal decay rate Γ \= y²\_eff m³\_eff/(8π M²\_P) is independently derived, giving Γ/H \= 140 (instant reheating). The reheating temperature T\_reh \= 2.55 × 10¹⁵ GeV follows from the ρ\_end-based instant reheating formula. The sole detectable primordial GW is the inflationary tensor background, measurable by LiteBIRD (\~9σ), CMB-S4 (\~18σ), and DECIGO (500×). Reheating GW are honestly assessed as unobservable. r\_ZS/r\_Starobinsky \= 2.63 provides a decisive discriminator.

**§11. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite (Python/NumPy/SciPy, with fully independent derivation chain) is publicly available.

**Appendix A. Verification Suite Summary**

24 tests across 6 categories: independent derivations (5), timescale hierarchy (4), reheating dynamics (4), branching ratios (4), GW spectrum (5), cross-paper consistency (2). All quantities independently computed from A \= 35/437 — no hardcoded intermediate values. 100% pass rate.

**Appendix B. T\_reh Formula Selection**

In the instant reheating regime (Γ/H ≈ 140 ≫ 1), the ρ\_end-based formula T\_reh \= (30ρ\_end/(π²g\_\*))^{1/4} is the physically correct expression. The standard perturbative formula T \~ (90/(π²g\_\*))^{1/4} √(ΓM\_P) assumes a matter-dominated reheating phase (Γ ≪ H) and overestimates T\_reh by \~12× in the instant regime. The verification suite explicitly tests this distinction (test C4).

**Appendix C. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| ----- | :---: | :---: | ----- |
| \[A\] Independent Derivations | 5 | 5/0 | y\_eff, m²\_eff, H\_end, Γ/H=140, T\_reh |
| \[B\] Timescale Hierarchy | 4 | 4/0 | T\_osc=4.7, t\_decay=1912, t\_Hub=267410 t\_P |
| \[C\] Reheating Dynamics | 4 | 4/0 | T\_reh bounds, q\<1, formula consistency |
| \[D\] Branching Ratios | 4 | 4/0 | BR(gg)=85%, sum=100% |
| \[E\] GW Spectrum | 5 | 5/0 | Ω\_GW=5.1×10⁻¹⁸, r\_ratio=2.63 |
| \[F\] Cross-Paper | 2 | 2/0 | A×437=35 exact, derivation chain |

**TOTAL: 24/24 PASS — 100% pass rate**

**Cross-Reference Table**

| Result | Status | Dependencies |
| ----- | :---: | ----- |
| y\_eff \= A/(1+A) \= 35/472 | DERIVED | ZS-F1 v1.0 (base action), ZS-F2 v1.0 (A) |
| Γ \= y²m³/(8πM²), Γ/H=140 | DERIVED+VERIFIED | ZS-U1 v1.0 (m\_eff, ε\_end), independent computation |
| T\_reh \= 2.55×10¹⁵ GeV | DERIVED | ρ\_end instant reheating (Γ/H≫1) |
| BR(gg/WW/BB) \= 85/7/8% | DERIVED | SM trace anomaly \+ ZS-S1 v1.0 |
| Ω\_GW h² \= 5.1×10⁻¹⁸ | DERIVED+TESTABLE | ZS-U1 v1.0 (r=0.0089) |
| r\_ZS/r\_Staro \= 2.63 | DERIVED | N\_\* \= 59.5 (ZS-U1 v1.0) |
| Reheating GW unobservable | NON-CLAIM | f\_peak \= 12.6 THz |

**References**

\[1\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026).

\[2\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026).

\[3\] K. Kang, "ε-Field Inflation," ZS-U1 v1.0 (2026).

\[4\] K. Kang, "Gauge Coupling Unification," ZS-S1 v1.0 (2026).

\[5\] K. Kang, "Resonant Leptogenesis Framework," ZS-S5 v1.0 (2026).

\[6\] K. Kang, "Z-Sim Forward Simulator," ZS-T3 v1.0 (2026).

\[7\] Kofman, L., Linde, A., & Starobinsky, A.A., Phys. Rev. D 56, 3258 (1997).

\[8\] Fujii, Y. & Maeda, K., The Scalar-Tensor Theory of Gravitation, Cambridge (2003).

\[9\] Tristram, M. et al., Phys. Rev. D 105, 083524 (2022). r \< 0.032.

\[10\] LiteBIRD Collaboration, PTEP 2023, 042F01 (2023). δr ≈ 0.001, launch \~JFY2032.

\[11\] CMB-S4 Collaboration, ApJ 926, 54 (2022). σ(r) ≈ 5×10⁻⁴.

\[12\] Kawamura, S. et al., CQG 28, 094011 (2011). DECIGO.

\[13\] Planck Collaboration, A\&A 641, A10 (2020).

**Version History**

**v1.0 (March 2026):** Initial public release. Reheating dynamics with independently derived T\_reh from ρ\_end formula (Eq. 3), conformal decay rate Γ (Eq. 2), branching ratios, GW spectrum, ε-Higgs EFT, dual-channel dynamics, T\_reh formula selection (Appendix B). All intermediate values independently computed — no hardcoded quantities. 24/24 tests across 6 categories. (Consolidated from internal Z-Spin Collaboration research notes up to v2.2.0)  
