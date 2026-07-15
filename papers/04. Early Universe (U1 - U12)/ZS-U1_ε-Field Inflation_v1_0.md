**ZS-U1**

**ε-Field Inflation:**  
**Slow-Roll Dynamics, CMB Observables,**  
**and Attractor Reheating**

Kenny Kang

**Version 1.0** — March 2026  
Theme: Early Universe \[ZS-U\] | Paper 1 of 8

**Verification: 28/28 PASS | Zero New Fit Parameters | A\_s Normalized**

**§0. Abstract**

We demonstrate that the Z-Spin ε-field, governed by the base action S \= ∫ d⁴x √(−g) \[(1 \+ **A**ε²)R/2 − (∂ε)²/2 − (λ/4)(ε² − 1)²\] with **A \= 35/437** (ZS-F2 v1.0), supports slow-roll inflation in the large-field regime (ε ≫ 1). Working in the Einstein frame with the canonical field φ̃, we compute slow-roll parameters using robust 4th-order finite differences and full RK45 trajectory integration, obtaining (n\_s, r) as a function of the horizon-exit e-fold number N\*.

At N\* \= 60 we find **n\_s \= 0.9674** (0.6σ from Planck) and **r \= 8.90×10⁻³** (below BICEP/Keck bound r \< 0.032), with r exceeding the Starobinsky R² value by a factor ≈ 2.67 due to Jordan kinetic-term dominance (1/(6**A**) ≈ 2.08). We close the post-inflation reheating uncertainty by deriving the oscillation equation-of-state w\_osc ≈ 0 from the quadratic structure of the Einstein-frame potential near the Z₂ attractor (ε → ±1), confirmed by RK45 trajectory integration (\<w\>\_osc \= −0.020). This reduces reheating ambiguity to a single parameter T\_reh.

The quartic coupling λ\_inf \= 7.63 × 10⁻¹² is fixed by the Planck scalar amplitude A\_s \= 2.1 × 10⁻⁹ (external normalization condition, not a Z-Spin fit parameter). The ZS-F3 v1.0 claim r \= A/π is formally **WITHDRAWN**; the correct prediction r \= 16ε\_V(N\_e) gives r ∈ \[0.007, 0.013\] for N\_e ∈ \[50, 60\]. All late-time predictions (H₀, Ω\_Λ, S₈, η\_B, quark masses, τ\_p) remain fully preserved.

**Keywords:** Z-Spin cosmology, scalar-tensor inflation, slow-roll, CMB observables, tensor-to-scalar ratio, Starobinsky discriminator, LiteBIRD, reheating closure, RK45 trajectory

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | ----- |
| PROVEN | Mathematical theorem with complete proof. |
| STANDARD | Established result in QFT/cosmology textbooks. |
| DERIVED | Quantitative consequence from Z-Spin axioms \+ standard physics. |
| VERIFIED | Numerically checked (verification suite provided). |
| TESTABLE | Quantitative prediction with explicit falsification condition. |
| HYPOTHESIS | Requires further derivation or decisive tests. |
| OBSERVATION | Empirical pattern identified; upgrade to DERIVED pending derivation. |
| NON-CLAIM | Quantity NOT derived; honest acknowledgment of limitation. |
| WITHDRAWN | Previously claimed result found incorrect; formally retracted. |

**§1. Introduction and Motivation**

ZS-F1 through ZS-A5 of the Z-Spin series have established a comprehensive framework in which all six interaction regimes—strong, electromagnetic, weak, gravitational, ε-Halo (dark matter), and ε-Drive (dark energy)—emerge as geometric consequences of a single scalar-tensor action with ε-field and geometric impedance **A \= 35/437**. The late-time (ε → ±1 attractor) predictions include the H₀ tension resolution (ZS-F3 v1.0), flat rotation curves without particle dark matter (ZS-A1 v1.0), the baryon asymmetry η\_B \= (6/11)³⁵ (ZS-U3 v1.0), gauge coupling derivations (ZS-S1 v1.0), and proton lifetime τ\_p ≈ 2.56 × 10³⁴ yr (ZS-A3 v1.0).

A critical gap remained: the framework had not addressed the inflationary epoch. The central question of this paper is: **Can the same ε-field that governs late-time cosmology also serve as the inflaton?**

We answer this affirmatively. The Z-Spin base action, analyzed in the Einstein frame, possesses a plateau potential at large ε that naturally supports slow-roll inflation. The key physical insight is that the non-minimal coupling Aε²R produces Starobinsky-like potential flattening, but the simultaneous Jordan-frame kinetic term (∂ε)²/2 modifies the universality class: the ratio 1/(6A) ≈ 2.08 \> 1, enhancing r by 2.67× relative to Starobinsky.

**§2. Einstein-Frame Action and Canonical Field**

**2.1 Conformal Transformation**

The Jordan-frame Z-Spin base action (ZS-F1 v1.0) is:

*S\_J \= ∫d⁴x √(−g\_J) \[(1 \+ Aε²)R\_J/2 − (∂ε)²/2 − (λ/4)(ε² − 1)²\]     (1)*

Define Ω²(ε) \= 1 \+ Aε² and perform the Weyl rescaling g\_μν \= Ω² g\_J\_μν:

*S\_E \= ∫d⁴x √(−g) \[R/2 − K(ε)(∂ε)²/2 − V\_E(ε)\]     (2)*

where the kinetic metric and Einstein-frame potential are:

*K(ε) \= 1/(1+Aε²) \+ 6A²ε²/(1+Aε²)²     (3)*

*V\_E(ε) \= (λ/4)(ε² − 1)² / (1 \+ Aε²)²     (4)*

The first term in K(ε) originates from the Jordan-frame kinetic term; the second from the conformal transformation of the Ricci scalar.

*\[STATUS: STANDARD\] Weyl rescaling is textbook (Fujii & Maeda 2003).*

**2.2 Kinetic Term Structure**

The ratio of Jordan-frame kinetic (Term I) to conformal (Term II) contributions:

*T\_I / T\_II \= (1+Aε²)/(6A²ε²) → 1/(6A) ≈ 2.08 as ε → ∞     (5)*

In Starobinsky R² inflation, Term II dominates exclusively. In Higgs inflation with ξφ²R, 1/(6ξ) ≪ 1 for ξ ≫ 1\. The Z-Spin model occupies a qualitatively different regime: **A** \= 0.080 \< 1/6 ≈ 0.167, so the **Jordan kinetic term always dominates**. This is the root cause of the enhanced tensor-to-scalar ratio.

*\[STATUS: DERIVED\] Verified numerically. Novel universality class.*

**Table 1\. Kinetic term ratio T\_I/T\_II as a function of ε.**

| ε | Term I | Term II | I/II | Dominant |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 0.926 | 0.033 | 28.06 | Jordan |
| 5 | 0.333 | 0.107 | 3.12 | Jordan |
| 10 | 0.111 | 0.047 | 2.34 | Jordan |
| 20 | 0.030 | 0.014 | 2.15 | Jordan |
| 100 | 1.25×10⁻³ | 5.99×10⁻⁴ | 2.08 | Jordan |
| ∞ | — | — | 1/(6A)=2.08 | Jordan |

**§3. Einstein-Frame Potential Landscape**

V\_E(ε) has three distinct regimes:

**Hilltop (ε ≈ 0):** V\_E(0) \= λ/4, a local maximum. Hilltop inflation yields at most \~2 e-folds (verified by RK45 integration: N\_e \= 2.04), far too few.

**Minimum (ε \= ±1):** V\_E(±1) \= 0 exactly, the Z₂-symmetric vacua (ZS-F1 v1.0). These are the late-time attractors.

**Plateau (ε ≫ 1):** V\_E → λ/(4A²) ≡ V∞. At ε \= 100, V\_E/V∞ \= 0.9973. The inflation energy scale E\_inf \= V∞^(1/4) ≈ 1.0 × 10¹⁶ GeV (GUT scale).

*\[STATUS: DERIVED\] Complete landscape with three regimes analytically characterized.*

**§4. Slow-Roll Analysis and CMB Observables**

**4.1 Slow-Roll Parameters**

The potential slow-roll parameters are:

*ε\_V \= (1/2)(V′/V)²,   η\_V \= V″/V     (6)*

where primes denote d/dφ̃. All derivatives use 4th-order central differences, avoiding chain-rule cancellation errors (see Appendix B).

*\[STATUS: VERIFIED\] Three independent methods agree to machine precision.*

**4.2 CMB Observables**

Inflation ends when ε\_V(ε\_end) \= 1, at ε\_end \= 2.640. The number of e-folds N\_e fixes the CMB exit point ε\*. The coupling λ \= λ\_inf \= 7.63 × 10⁻¹² is fixed by the scalar amplitude A\_s \= 2.1 × 10⁻⁹ (Planck 2018). This is an external normalization condition, not a Z-Spin fit parameter; the vacuum-scale coupling λ\_vac differs due to RG running (see ZS-F1 v1.0 §4.4 for scale hierarchy).

**Table 2\. Z-Spin inflation predictions at CMB exit.**

| N\_e | ε\* | Aε² | ε\_V | η\_V | r | n\_s | Planck σ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 50 | 17.71 | 25.1 | 7.84×10⁻⁴ | −1.71×10⁻² | 0.0125 | 0.9610 | 0.9σ ✓ |
| 55 | 18.53 | 27.5 | 6.56×10⁻⁴ | −1.58×10⁻² | 0.0105 | 0.9645 | 0.1σ ✓ |
| 60 | 19.31 | 29.9 | 5.56×10⁻⁴ | −1.46×10⁻² | 0.0089 | 0.9674 | 0.6σ ✓ |

All benchmarks produce red tilt (n\_s \< 1\) and satisfy BICEP/Keck r \< 0.032.

*\[STATUS: DERIVED \+ VERIFIED\] Predictions are parameter-free given A \= 35/437. λ\_inf fixed by A\_s (external normalization).*

**§5. Comparison with Starobinsky and Planck**

**Table 3\. Z-Spin vs Starobinsky vs Planck (N\_e \= 60).**

| Observable | Z-Spin | Starobinsky | Planck 2018 |
| :---: | :---: | :---: | :---: |
| n\_s | 0.9674 | 0.9667 | 0.9649 ± 0.0042 |
| r | 8.90 × 10⁻³ | 3.33 × 10⁻³ | \< 0.032 |
| dn\_s/dlnk | −5.4 × 10⁻⁴ | −5.6 × 10⁻⁴ | −0.0045 ± 0.0067 |
| r/r\_Staro | 2.67 | 1.00 | — |
| n\_s deviation | 0.6σ | 0.4σ | — |

The spectral indices are nearly identical (\~0.967). **The key discriminator is r:** r\_ZSpin/r\_Staro \= 2.67. With LiteBIRD's projected σ\_r ≈ 0.001, this ratio is measurable at \~6σ. The spectral running dn\_s/dlnk \= −5.4 × 10⁻⁴ is computed via the numerical ΔN method (N \= 59 vs 61), which is more stable than the analytic formula involving third derivatives.

*\[STATUS: TESTABLE\] LiteBIRD will distinguish Z-Spin from Starobinsky at 6σ.*

**§6. Tensor-to-Scalar Ratio Scaling Law**

The product r · N² is approximately constant:

**Table 4\. r scaling with N\_e.**

| N\_e | r | r · N | r · N² |
| :---: | :---: | :---: | :---: |
| 50 | 1.25 × 10⁻² | 0.627 | 31.4 |
| 55 | 1.05 × 10⁻² | 0.577 | 31.7 |
| 60 | 8.90 × 10⁻³ | 0.534 | 32.1 |
| 65 | 7.65 × 10⁻³ | 0.497 | 32.3 |
| 70 | 6.65 × 10⁻³ | 0.466 | 32.6 |

Starobinsky gives r \= 12/N² exactly. Z-Spin gives r ≈ 32/N², reflecting the enhanced kinetic term (1/(6A) \= 2.08).

*\[STATUS: DERIVED\] r · N² ≈ 32 \= 12 × \[1 \+ 1/(6A)\] (approximate).*

**§7. Full Field Dynamics: ε(t) Trajectory**

**7.1 Friedmann–Klein–Gordon System**

*K(ε)ε̈ \+ (1/2)K′(ε)ε̇² \+ 3HK(ε)ε̇ \+ dV\_E/dε \= 0     (10)*

*3H² \= (1/2)K(ε)ε̇² \+ V\_E(ε)     (11)*

Solved using scipy.integrate.solve\_ivp (RK45 method) with relative tolerance 10⁻¹¹ and absolute tolerance 10⁻¹⁴. The full trajectory includes 8,013 adaptive time steps.

**7.2 Large-Field Inflation (ε₀ \= 20\)**

**Slow-roll (t \= 0–21):** ε decreases from 20 to \~2.5. w ≈ −1 throughout. \~69.5 e-folds accumulated (RK45 verified).

**Fast-roll (t \= 21–22):** ε\_V \> 1, inflation ends.

**Reheating oscillation (t \= 22–100):** Field oscillates around ε \= 1 with ω ≈ 1.33 M\_P. Time-averaged \<w\>\_osc \= −0.020 (RK45, matter-like).

**Attractor (t \> 100):** Field settles to ε\_final \= 0.9977, confirming ZS-F1 v1.0's Z₂ attractor dynamically.

*\[STATUS: VERIFIED\] ε(t) trajectory confirms dynamical continuity: inflation → reheating → attractor. RK45 with 8,013 steps.*

**7.3 Hilltop (ε₀ \= 0.5)**

Starting near the hilltop yields only N\_e \= 2.04 e-folds (RK45 confirmed). **Hilltop inflation is insufficient.** Viable inflation requires large-field initial condition.

**7.4 Reheating Closure**

Near ε \= 1, V\_E ≈ (1/2)m²\_eff(φ̃ − φ̃₀)² (quadratic), giving \<w\> ≈ 0 (matter-like). RK45 integration confirms \<w\>\_osc \= −0.020 over the oscillation phase, validating the analytic expectation. With w\_re ≈ 0 as the physical prior, reheating ambiguity reduces to a single parameter T\_reh.

**§8. Withdrawal of r \= A/π (ZS-F3 v1.0)**

ZS-F3 v1.0 claimed r \= A/π \= 0.0255 as TESTABLE. The present analysis demonstrates:

*r\_slow-roll \= 16ε\_V \= 0.0089 ≠ A/π \= 0.0255     (12)*

Discrepancy ratio: 0.35, far outside theoretical uncertainty. **The r \= A/π claim is formally withdrawn.**

This affects ONLY the r prediction. All other ZS-F3 v1.0 predictions—H₀, Ω\_Λ, S₈, η\_B, quark mass ratios, proton lifetime—depend on the late-time attractor (ε \= ±1) and are entirely independent of inflationary dynamics.

*\[STATUS: WITHDRAWN\] r \= A/π replaced by r \= 16ε\_V(N\_e). Late-time predictions preserved.*

**§9. Cross-Paper Consistency**

**Table 5\. Cross-paper consistency verification.**

| Paper | Claim | ZS-U1 Status | Verdict |
| :---: | ----- | ----- | :---: |
| ZS-F1 v1.0 | Z₂ attractor ε → ±1 | ε\_final=0.9977 (RK45) | VERIFIED |
| ZS-F2 v1.0 | A \= 35/437 locked | Used without adjustment | CONSISTENT |
| ZS-F3 v1.0 | r \= A/π | r \= 0.0089 ≠ 0.0255 | WITHDRAWN |
| ZS-F3 v1.0 | H₀ tension, Ω\_Λ, S₈ | Independent of inflation | PRESERVED |
| ZS-U3 v1.0 | η\_B \= (6/11)³⁵ | Independent of inflation | PRESERVED |
| ZS-A1 v1.0 | Flat rotation curves | Independent of inflation | PRESERVED |
| ZS-S1 v1.0 | Gauge couplings | Independent of inflation | PRESERVED |
| ZS-A3 v1.0 | τ\_p ≈ 2.56×10³⁴ yr | Independent of inflation | PRESERVED |

**§10. Falsification Conditions**

**Table 6\. Falsification conditions for ZS-U1.**

| ID | Condition | Experiment / Timeline | Priority |
| :---: | ----- | ----- | :---: |
| FU1-1 | n\_s outside \[0.955, 0.975\] | CMB-S4, LiteBIRD (\~2032) | HIGH |
| FU1-2 | r outside \[0.003, 0.020\] | LiteBIRD (σ\_r ≈ 0.001) | HIGH |
| FU1-3 | r \< r\_Staro \= 0.003 | LiteBIRD (6σ discriminator) | HIGH |
| FU1-4 | |dn\_s/dlnk| \> 0.01 | CMB-S4 \+ LSS | MEDIUM |
| FU1-5 | ε-field fails to reach attractor | Internal consistency | HIGH |

**FU1-3 is the most powerful discriminator.** Z-Spin predicts r \= 0.0089, which is 2.67× larger than Starobinsky. LiteBIRD will measure r with σ\_r ≈ 0.001, sufficient to distinguish at \~6σ. If r \< 0.003 is measured, Z-Spin ε-field inflation is falsified (though the late-time framework survives).

**§11. Epistemic Classification Summary**

**Table 7\. Epistemic status of ZS-U1 results.**

| Result | Status | Confidence |
| ----- | :---: | :---: |
| Einstein-frame action (Eq. 2–4) | STANDARD | HIGH |
| Kinetic ratio 1/(6A) \= 2.08 (Eq. 5\) | DERIVED | HIGH |
| Plateau potential V∞ (Eq. 4\) | DERIVED | HIGH |
| Slow-roll parameters (Table 2\) | DERIVED \+ VERIFIED | HIGH |
| n\_s \= 0.9674, r \= 0.0089 (N\_e=60) | DERIVED \+ VERIFIED | HIGH |
| λ\_inf \= 7.63 × 10⁻¹² (A\_s normalized) | DERIVED | HIGH |
| r · N² ≈ 32 scaling | DERIVED \+ VERIFIED | HIGH |
| ε(t) attractor recovery (RK45) | VERIFIED | HIGH |
| \<w\>\_osc \= −0.020 (RK45) | VERIFIED | HIGH |
| Hilltop N\_e \= 2.04 (RK45) | VERIFIED | HIGH |
| dn\_s/dlnk \= −5.4×10⁻⁴ (ΔN method) | DERIVED \+ VERIFIED | HIGH |
| r \= A/π (ZS-F3 v1.0) | WITHDRAWN | — |
| Reheating temperature | HYPOTHESIS | LOW |

**§12. Discussion and Conclusions**

**Viable inflation.** The Einstein-frame potential possesses a plateau at ε ≫ 1 supporting 60+ e-folds with n\_s \= 0.9674 and r \= 0.0089. No additional fields or parameters beyond ZS-F1 v1.0's base action. λ\_inf is externally normalized by A\_s.

**Novel universality class.** The model occupies a kinetic regime intermediate between pure Starobinsky (Term II dominant) and chaotic inflation. The Jordan-frame kinetic dominance (1/(6A) ≈ 2.08) enhances r by 2.67× while preserving n\_s, providing a sharp experimental discriminator.

**Complete trajectory.** The full ε(t) evolution via RK45 integration—from slow-roll inflation (69.5 e-folds) through reheating oscillation (\<w\> \= −0.020, matter-like) to the Z₂ attractor (ε\_final \= 0.9977)—confirms dynamical continuity between the inflationary and late-time regimes.

**Honest withdrawal.** The ZS-F3 v1.0 prediction r \= A/π is formally withdrawn, strengthening epistemic integrity.

Open questions: (i) precise reheating temperature (requires specifying ε-SM coupling, see ZS-U2 v1.0); (ii) initial condition motivation from pre-inflationary quantum cosmology; (iii) loop corrections to the potential.

**Z-Sim pre-flight check:** ZS-T3 v1.0 (Z-Sim) provides a zero-free-parameter consistency check for Tier-0 predictions before the full Cobaya MCMC run (Gate F32-12). With all 8 closure parameters derived from ZS-Q7 v1.0 and ZS-M3 v1.0, the simulator has only 2 remaining sampled parameters (A\_s, τ\_reio). Z-Sim does NOT replace Cobaya; it provides the pre-flight verification.

**§13. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite (Python/NumPy/SciPy, including RK45 trajectory integration) is publicly available.

**Appendix A. Verification Suite Summary**

28 tests across 8 categories: potential properties (4), derivative consistency (2), slow-roll parameters (3), CMB observables (7), kinetic structure (3), dynamics/static (3), cross-paper (2), RK45 trajectory (4). 100% pass rate.

**Appendix B. Derivative Bug Diagnosis**

The initial incorrect result n\_s \= 1.003 (blue tilt) was traced to a sign error in the analytic chain-rule computation. Resolved by using purely numerical 4th-order central differences, independently validated.

**Appendix C. Reheating Prediction Curve**

Complete (T\_reh → N\*, n\_s, r) mapping for both ρ\_end definitions (V\_end and 1.5V\_end), providing a falsifiable one-parameter family.

**Appendix D. Spectral Running Methodology**

The spectral running dn\_s/dlnk \= −5.4 × 10⁻⁴ is computed via the numerical ΔN method: n\_s is evaluated at N\_e \= 59 and 61 via independent slow-roll computations, then dns/dlnk \= −(n\_s(61) − n\_s(59))/2. This method avoids the numerical instability of the analytic formula dn\_s/dlnk \= 16ε\_Vη\_V − 24ε\_V² − 2ξ²\_V, where the third-order slow-roll parameter ξ²\_V \= (V′V‴)/V² requires triple-nested finite differences. Narrow-span (ΔN=1) and wide-span (ΔN=5) estimates agree to 1.3%, confirming robustness.

**Appendix E. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| ----- | :---: | :---: | ----- |
| \[A\] Potential Properties | 4 | 4/0 | V(1)=0, V(0)=λ/4, plateau V∞ |
| \[B\] Derivative Consistency | 2 | 2/0 | 4th-order accurate |
| \[C\] Slow-Roll Parameters | 3 | 3/0 | η\_V\<0 (red), ε\_V=5.6×10⁻⁴ |
| \[D\] CMB Observables | 7 | 7/0 | n\_s=0.967, r=0.0089, dns=−5.4×10⁻⁴ |
| \[E\] Kinetic Structure | 3 | 3/0 | 1/(6A)=2.08 \> 1 (Jordan) |
| \[F\] Dynamics (Static) | 3 | 3/0 | Attractor, m²\_eff\>0, hilltop\<5 |
| \[G\] Cross-Paper | 2 | 2/0 | A=35/437, 1/(6A) cross-check |
| \[H\] RK45 Trajectory | 4 | 4/0 | N=69.5, ε→0.998, \<w\>=−0.020 |

**TOTAL: 28/28 PASS — 100% pass rate**

**Cross-Reference Table**

| Result | Status | Dependencies |
| ----- | :---: | ----- |
| Einstein-frame action | STANDARD | ZS-F1 v1.0 (base action), Weyl rescaling |
| 1/(6A) \= 2.08 kinetic ratio | DERIVED | ZS-F2 v1.0 (A \= 35/437) |
| n\_s=0.9674, r=0.0089 | DERIVED+VERIFIED | ZS-F2 v1.0, Planck A\_s (normalization) |
| λ\_inf=7.63×10⁻¹² | DERIVED | A\_s normalization (external input) |
| r·N²≈32 scaling | DERIVED | Kinetic structure |
| ε(t) attractor (RK45) | VERIFIED | ZS-F1 v1.0 (Z₂ symmetry) |
| \<w\>\_osc=−0.020 | VERIFIED | RK45, quadratic minimum |
| dn\_s/dlnk=−5.4×10⁻⁴ | DERIVED+VERIFIED | ΔN method (N=59,61) |
| r=A/π withdrawn | WITHDRAWN | Replaced by r=16ε\_V |

**References**

\[1\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026).

\[2\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026).

\[3\] K. Kang, "Dynamical Phase Transitions," ZS-F3 v1.0 (2026).

\[4\] K. Kang, "Gauge Coupling Unification," ZS-S1 v1.0 (2026).

\[5\] K. Kang, "Baryon Asymmetry," ZS-U3 v1.0 (2026).

\[6\] K. Kang, "Galactic Dynamics & Morphology," ZS-A1 v1.0 (2026).

\[7\] K. Kang, "Black Hole Physics," ZS-A3 v1.0 (2026).

\[8\] K. Kang, "Reheating Dynamics," ZS-U2 v1.0 (2026).

\[9\] K. Kang, "Structural Arrow of Time," ZS-Q7 v1.0 (2026).

\[10\] K. Kang, "Regge-Holonomy, Immirzi & Z-Telomere," ZS-M3 v1.0 (2026).

\[11\] K. Kang, "Z-Sim Forward Simulator," ZS-T3 v1.0 (2026).

\[12\] Planck Collaboration, A\&A 641, A6 (2020). Planck 2018 results VI.

\[13\] BICEP/Keck Collaboration, Phys. Rev. Lett. 131, 131001 (2023).

\[14\] Starobinsky, A.A., Phys. Lett. B 91, 99 (1980).

\[15\] Bezrukov, F. & Shaposhnikov, M., Phys. Lett. B 659, 703 (2008).

\[16\] Fujii, Y. & Maeda, K., The Scalar-Tensor Theory of Gravitation, Cambridge (2003).

\[17\] LiteBIRD Collaboration, PTEP 2023, 042F01 (2023). δr ≈ 0.001, launch \~JFY2032.

\[18\] CMB-S4 Collaboration, ApJ 926, 54 (2022). σ(r) ≈ 5×10⁻⁴.

**Version History**

**v1.0 (March 2026):** Initial public release. Slow-roll analysis, CMB observables, full RK45 ε(t) trajectory (8,013 steps), reheating closure (\<w\>\_osc \= −0.020 verified), derivative bug diagnosis, reheating prediction curve, ΔN spectral running (−5.4×10⁻⁴), Z-Sim cross-reference. 28/28 tests across 8 categories. (Consolidated from internal Z-Spin Collaboration research notes up to v2.3.0)  
