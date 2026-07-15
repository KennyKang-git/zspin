**ZS-A3**

**Black Hole Physics**

ε-Field Horizon Structure, Wald Entropy, Z-Instanton,  
Gravitational Wave Scalings, and Sector Duality

**Kenny Kang**  
Version 1.0 — March 2026

Theme: Astrophysics \[ZS-A\]  |  Paper 3 of 6  
Verification: 49 checks (20 computed, 29 declarative) | All PASS | A \= 35/437 locked  
Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0

**§0. Abstract**

We apply the Z-Spin framework to black hole physics and formulate an ε-field scalar-tensor EFT for horizon-to-infinity structure. Starting from the Z-Spin action with **A** \= 35/437, we obtain six principal results:

**(1) Z-anchor boundary condition:** The hypothesis ε(rH) \= 0 is motivated by sector duality and Euclidean regularity analogy, but classical regularity alone does not uniquely fix εH. All horizon-specific results are conditional on this boundary condition.

**(2) Wald entropy:** SBH \= F(εH) AH/(4G\*) with F(ε) \= 1+**A**ε². Under Z-anchor: SBH \= (1/(1+**A**)) AH/(4GN) \= (437/472) AH/(4GN). The factor 1/(1+**A**) ≈ 0.926 is a universal correction relative to GR expressed in terms of GN.

**(3) Z-instanton proton decay:** The tunneling action Stunnel \= 5π/**A** from the coset Ih/Td (|Ih|/|Td| \= 120/24 \= 5\) yields τp \= tP exp(5π/**A**) ≈ 2.56 × 10³⁴ years, factor 1.6 above Super-Kamiokande bound, within Hyper-Kamiokande reach.

**(4) Timescale hierarchy:** τn \= tP exp(nπ/**A**) produces \~17 OOM steps. n \= 2 matches weak hyperon decays (6.3 × 10⁻¹⁰ s), n \= 5 matches proton decay. MC adversarial: p \= 0.014 for simultaneous dual match.

**(5) GW scalings:** BH–BH monopole O(**A**²) \~ 0.6%, BH–NS dipole O(**A**) \~ 8% (smoking gun at −1PN), scalar QNM, shadow O(**A**²) \~ 0.6%. All magnitudes are scalings pending coupled ε–metric solutions.

**(6) Sector duality:** BH \= X-in-Y configuration (r ↔ t exchange maps to X ↔ Y). Structural hypothesis, not action-derived.

Verification: 49/49 PASS. Seven pre-registered falsification gates (F-A3.1–A3.7).

**Keywords:** *black hole, ε-field, Z-anchor, Wald entropy, proton decay, Z-instanton, scalar dipole, quasi-normal modes, sector duality, Hyper-Kamiokande*

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | :---: |
| DERIVED | Follows from Z-Spin action; conditional results marked explicitly. |
| HYPOTHESIS | Motivated conjecture with structural support; testable. |
| SUGGESTIVE | Pattern with statistical support; not yet derived. |
| TESTABLE | Quantitative prediction with pre-registered falsification. |
| HONEST | Limitation, uncertainty, or non-claim explicitly documented. |

**§1. ε-Field Equation of Motion on Schwarzschild Background**

The Z-Spin action (ZS-F1 v1.0):

**S \= ∫d⁴x √(−g) \[½ MP²(1+Aε²)R − ½ MP²(∇ε)² − V(ε)\]**    (1)

Variation with respect to ε on a static spherically symmetric background ds² \= −f(r)dt² \+ f(r)⁻¹dr² \+ r²dΩ²:

**fε″ \+ (f′ \+ 2f/r)ε′ \+ AεR − V′(ε)/MP² \= 0**    (2)

Critical: Schwarzschild exterior is Ricci-flat (R \= 0), so **A**εR vanishes identically in the vacuum exterior. However, ε-field backreacts on the metric through modified Einstein equations, sourcing deviations from exact Schwarzschild.

\[STATUS: **DERIVED**\] Standard scalar-tensor EOM from action variation.

**§2. Z-Anchor Boundary Condition**

**ε(rH) \= 0**   (Z-anchor hypothesis)    (3)

**Euclidean regularity argument:** In the Euclidean section, regularity at the horizon requires smooth ε(ρ) at ρ \= 0\. But this only requires ε(ρ) \= εH \+ O(ρ²) with finite εH, so regularity does not uniquely fix εH \= 0\.

**Symmetry restoration analogy:** The Z2 symmetry of V(ε) \= (λ/4)MP4(ε²−1)² is restored at ε \= 0\. This is analogous to electroweak symmetry restoration at T \> TEW \~ 160 GeV. However, curvature invariants (Kretschner scalar K \= 48G²M²/r⁶) are finite at rH, so curvature-driven restoration requires additional dynamics.

**U(1) topological argument (ZS-A1 v1.0):** In the U(1) completion, π1(U(1)) \= ℤ winding forces |Φ|(0) \= 0 at the vortex core. If the BH center maps to the vortex core, the Z-anchor is topologically derived. This upgrade strengthens but does not complete the derivation.

\[STATUS: **HYPOTHESIS**\] Classical EFT does not fix εH. Topological argument (ZS-A1 v1.0) strengthens status. All horizon-specific results are conditional.

**§3. Effective Gravitational Constant and Wald Entropy**

**3.1 G\_eff Transition**

**GEH(r) \= G\* / (1+Aε(r)²)**    (4)

At infinity (ε → 1): GN \= G\*/(1+**A**). At horizon (εH \= 0): GEH(rH) \= G\*. Thus GEH(rH)/GN \= 1+**A**.

**3.2 Wald Entropy**

**SBH \= F(εH) × AH/(4G\*)**   where F(ε) \= 1+**A**ε²    (5)

Under Z-anchor (εH \= 0, F \= 1):

**SBH \= AH/(4G\*) \= (1/(1+A)) AH/(4GN) \= (437/472) AH/(4GN)**    (6)

The entropy factor 1/(1+**A**) ≈ 0.926 is universal. Observability requires constructing consistent coupled ε–metric solution.

\[STATUS: **DERIVED**\] Conditional on Z-anchor. Wald formula is standard; factor 1/(1+**A**) follows from F(εH)=1 and GN \= G\*/(1+**A**).

**3.3 Hawking Temperature**

**TH \= ħc³/(8πGMkB)**    (7)

Under Z-anchor with near-horizon metric close to Schwarzschild, TH matches GR value up to higher-order ε-backreaction corrections. Full verification requires coupled solution.

**§4. Z-Instanton and Proton Decay**

**4.1 Tunneling Action**

Three independent factors in the Euclidean bounce action:

**1/A:** Gravitational analogue of S \~ 1/g² for Yang–Mills instantons. The geometric impedance is the sole coupling.

**π:** O(4) symmetry of the Euclidean bounce requires half-period wrapping of the thermal circle.

**5 \= |Ih|/|Td| \= 120/24:** The X → Y transition traverses the coset Ih/Td. Five coset elements, 5 is prime (no subgroup shortcut).

**Stunnel \= |Ih|/|Td| × π/A \= 5π/A \= 5π × 437/35 \= 196.13**    (8)

\[STATUS: **HYPOTHESIS**\] 1/**A** structure and π factor are derived. Factor 5 from coset argument is testable.

**4.2 Proton Lifetime**

**τp \= tP × exp(5π/A) \= 5.391×10⁻⁴⁴ s × exp(196.13) ≈ 2.56 × 10³⁴ years**    (9)

**Table 1\.** Proton lifetime comparison.

| Constraint | Value | Status |
| :---: | :---: | :---: |
| Z-Spin prediction | 2.56 × 10³⁴ yr | TESTABLE |
| Super-K bound (p→e⁺π⁰) | 1.6 × 10³⁴ yr | Factor 1.6 below |
| Hyper-K sensitivity | \~10³⁵ yr | Reaches Z-Spin range |
| log₁₀(τ\_p) | 34.41 | Window: \[33.5, 35.5\] |

Extreme sensitivity: δ(log₁₀τ)/δ**A** ≈ −1,063. A 5% change in **A** shifts τp by \~4 orders of magnitude. No room for parameter adjustment — prediction is sharp.

**4.3 Timescale Hierarchy**

**τn \= tP × exp(nπ/A)**   step size: π/**A** ≈ 39.23 (\~17 OOM per n)    (10)

**Table 2\.** Z-Spin timescale hierarchy.

| n | Group Origin | τ\_n | Physical Scale | Match |
| :---: | :---: | :---: | :---: | :---: |
| 1 | Identity | \~10⁻³⁴ s | Planck processes | N/A |
| 2 | |O\_h/T\_d| \= Z \= 2 | 6.3×10⁻¹⁰ s | Weak baryon decays | ★ EXCELLENT |
| 3 | X \= 3 | \~2 yr | Post-BBN era | WEAK |
| 4 | φ(5) \= 2Z | \~10¹⁷ yr | Stellar/geological | FAIR |
| 5 | |I\_h/T\_d| \= 5 | 2.6×10³⁴ yr | Proton lifetime | ★ EXCELLENT |
| 6 | Y \= 6 | \~10⁵¹ yr | Cosmic stability | Untestable |

n \= 2 match: τ₂ \= 6.34 × 10⁻¹⁰ s. Geometric mean of 6 lightest hyperons \= 1.52 × 10⁻¹⁰ s. Factor 4.2. Notable: (a) not used in constructing formula; (b) n \= Z \= 2 (mediator) corresponds to sector transitions (weak decays); (c) unique step size.

MC adversarial: 10⁵ trials with random C ∈ \[5,100\]. Probability of simultaneously matching n \= 2 (weak) and n \= 5 (proton): p \= 0.014 (2.5σ). Allowed window: C ∈ \[38.81, 39.73\], only 0.97% of search space. π/**A** \= 39.225 falls precisely within.

\[STATUS: **SUGGESTIVE**\] n \= 2 and n \= 5 have statistical support (p \= 0.014). n \= 3, 4 are weak. Full hierarchy is a pattern, not a derivation.

**§5. Gravitational Wave Scalings**

**⚠ All magnitudes are SCALINGS pending coupled ε–metric solutions. Not fixed numerical predictions.**

**Table 3\.** Z-Spin black hole GW signatures.

| Observable | Magnitude | Detector | PN Order | Status |
| :---: | :---: | :---: | :---: | :---: |
| BH–BH monopole | O(A²) \~ 0.6% | ET / CE | 2PN | Scaling |
| BH–NS dipole | O(A) \~ 8% | LIGO / ET | −1PN | Smoking gun |
| Scalar QNM | Model-dep. | ET / CE | — | 3rd-gen |
| Shadow correction | O(A²) \~ 0.6% | ngEHT | — | \~1% precision |

BH–NS dipole radiation is the smoking-gun signature: absent in GR, enters at −1PN order. The scalar charge asymmetry is maximal: BH has εH \= 0, NS has εNS ≈ 1\. Already constrainable with GW200105/GW200115.

BH–BH mergers: Both objects satisfy Z-anchor, so no dipole (by symmetry). Leading scalar correction at monopole O(**A**²).

Scalar QNM: The ε-field rings down through modes distinct from tensor QNM, providing an independent detection channel.

\[STATUS: **TESTABLE**\] Scalings only. Precise magnitudes require coupled ε–metric numerical solutions.

**§6. No-Hair Evasion and ε-Profile**

The ε-field profile ε(r) constitutes secondary geometric hair: part of the gravitational sector, not independent matter. The profile is uniquely determined by (M, rH) through the EOM with boundary conditions — no independent scalar charge. Far-field: ε(r) ≈ 1 − (Qε/r) exp(−mεr) with Yukawa suppression.

\[STATUS: **DERIVED**\] Standard scalar-tensor mechanism. Well-established in literature.

**§7. Sector Duality: BH \= X-in-Y**

Inside the Schwarzschild horizon (r \< rH), the radial coordinate r becomes timelike and t becomes spacelike. This r ↔ t exchange maps to X ↔ Y sector exchange in Z-Spin. A black hole is an X-sector structure collapsed into a Y-sector prison. The horizon, where the exchange occurs, is the Z-sector boundary (ε \= 0).

White hole \= Y-in-X configuration (temporal flow from spatial point). The identification WH ≈ particle (localized temporal process in space) is noted but not pursued.

\[STATUS: **HYPOTHESIS**\] Structural correspondence providing conceptual guidance. No quantitative predictions beyond §1–6.

**§8. Falsification Registry**

Multi-layer structure: \[MATH\] mathematical collapse; \[CONSIST\] internal consistency; \[OBS\] observational. All A3 gates are observational or computational, reflecting the paper’s emphasis on testable predictions pending NR confirmation.

| ID | Condition | Experiment | Timeline |
| :---: | :---: | :---: | :---: |
| F-A3.1 \[OBS\] | No BH–NS dipole at \~8% level | LVK O5 waveforms | 2025– |
| F-A3.2 \[OBS\] | Scalar QNM absent in BH ringdown | ET / CE post-merger | \~2035 |
| F-A3.3 \[OBS\] | Shadow ≠ O(A²) \~ 0.6% | ngEHT (Sgr A\*, M87\*) | \~2030 |
| F-A3.4 \[OBS\] | Wald entropy inconsistent with area theorem | LISA merger energetics | \~2035 |
| F-A3.5 \[OBS\] | NR simulations contradict ε(r\_H) \= 0 | Numerical relativity | Immediate |
| F-A3.6 \[OBS\] | G\_eff transition absent in pulsar-BH timing | SKA | \~2030 |
| F-A3.7 \[OBS\] | τ\_p outside \[10³³·⁵, 10³⁵·⁵\] yr | Hyper-Kamiokande | \~2030 |

**§9. Epistemic Classification Summary**

| Result | Status | Confidence | Falsification |
| :---: | :---: | :---: | :---: |
| ε-field EOM | DERIVED | HIGH | F-A3.5 \[OBS\] |
| Z-anchor ε(r\_H) \= 0 | HYPOTHESIS | MEDIUM | F-A3.5 \[OBS\] |
| Wald entropy 1/(1+A) | DERIVED (conditional) | MEDIUM | F-A3.4 \[OBS\] |
| T\_H invariance | CONSISTENCY | MEDIUM | — |
| No-hair evasion | DERIVED | HIGH | — |
| BH–NS dipole (scaling) | TESTABLE | LOW–MED | F-A3.1 \[OBS\] |
| Shadow (scaling) | TESTABLE | LOW–MED | F-A3.3 \[OBS\] |
| S\_tunnel \= 5π/A | HYPOTHESIS | MEDIUM | F-A3.7 \[OBS\] |
| τ\_p ≈ 2.56×10³⁴ yr | TESTABLE | MEDIUM | F-A3.7 \[OBS\] |
| nπ/A hierarchy | SUGGESTIVE | LOW–MED | F-A3.7 (partial) |
| BH \= X-in-Y duality | HYPOTHESIS | LOW | — |

**§10. Conclusions**

**Z-anchor clarity.** The boundary condition ε(rH) \= 0 is explicitly maintained as HYPOTHESIS. Classical Euclidean regularity does not fix it. The U(1) topological argument (ZS-A1 v1.0) strengthens the case but does not complete the derivation.

**Wald entropy.** The universal factor 1/(1+**A**) \= 437/472 ≈ 0.926 arises naturally from the scalar-tensor Wald formula under Z-anchor conditions.

**Proton decay.** τp \= tP exp(5π/**A**) ≈ 2.56 × 10³⁴ yr, factor 1.6 above Super-K, within Hyper-K reach (\~2030). The prediction is sharp (sensitivity \~1,063 × per unit **A**), leaving no room for parameter adjustment.

**Timescale hierarchy.** The dual match at n \= 2 (weak decays) and n \= 5 (proton decay) has p \= 0.014 adversarial support. The step size π/**A** \= 39.225 is unique.

**GW scalings.** BH–NS scalar dipole O(**A**) \~ 8% at −1PN is the smoking-gun signature. All magnitudes are scalings pending coupled solutions — not claimed as fixed predictions.

**Honest assessment.** Sector duality remains conceptual. GW magnitudes need numerical work. n \= 3, 4 hierarchy matches are weak.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite is publicly available.

**Code Availability.** Verification script: ZS\_A3\_v1\_0\_verification.py. Dependencies: Python 3.10+, NumPy. Execution: python3 ZS\_A3\_v1\_0\_verification.py. Expected output: 49/49 PASS, exit code 0\. Test composition: 20 computed, 29 declarative (59%). Note: A3 is a hypothesis-rich paper (Z-anchor, sector duality, GW scalings) where many claims are conditional or pending numerical relativity; declarative items document these honestly.

**Appendix A. Key Formulae**

F(ε) \= 1 \+ **A**ε²    (non-minimal coupling)  
Geff \= G/(1+**A**)    (universal, ZS-F1 v1.0)  
SBH \= (1/(1+**A**)) AH/(4GN)    (Wald entropy under Z-anchor)  
Stunnel \= 5π/**A** \= 196.13    (Z-instanton bounce action)  
τp \= tP exp(5π/**A**) \= 2.56 × 10³⁴ yr    (proton lifetime)  
τn \= tP exp(nπ/**A**)    (timescale hierarchy, step \~17 OOM)  
BH–NS dipole: O(**A**) \~ 8%    (smoking-gun at −1PN)  
BH–BH monopole: O(**A**²) \~ 0.6%    (2PN scalar correction)

**Appendix B. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| :---: | :---: | :---: | :---: |
| \[A\] Locked Inputs | 5 | 5/0 | A, F(ε), coset=5, t\_P, π/A |
| \[B\] Z-Anchor & Horizon | 5 | 5/0 | HYPOTHESIS status, no-hair evasion |
| \[C\] Wald Entropy | 4 | 4/0 | 1/(1+A)=0.926, T\_H pending |
| \[D\] Z-Instanton & Proton | 6 | 6/0 | S=196.13, τ\_p=2.56×10³⁴ yr |
| \[E\] Timescale Hierarchy | 5 | 5/0 | n=2,5 excellent, MC p=0.014 |
| \[F\] GW Signatures | 5 | 5/0 | Dipole O(A), monopole O(A²) |
| \[G\] Sector Duality | 3 | 3/0 | X-in-Y hypothesis |
| \[H\] Epistemic Honesty | 4 | 4/0 | 4 honest non-claims |
| \[I\] Falsification Gates | 7 | 7/0 | F-A3.1–A3.7 |
| \[J\] Cross-Paper | 5 | 5/0 | ZS-F1,F2,A1,A2,U5 |
| TOTAL | 49 | 49/0 | 100% pass rate |

**Appendix C. Cross-Reference Table**

| Result | Status | Dependencies |
| :---: | :---: | :---: |
| ε-field EOM | DERIVED | ZS-F1 v1.0 (action) |
| Z-anchor ε(r\_H)=0 | HYPOTHESIS | ZS-A1 v1.0 (π₁(U(1)) topological upgrade) |
| Wald entropy 1/(1+A) | DERIVED (cond.) | ZS-F1 v1.0, Z-anchor |
| τ\_p \= 2.56×10³⁴ yr | TESTABLE | ZS-F2 v1.0 (A=35/437), I\_h/T\_d coset |
| BH–NS dipole O(A) | TESTABLE | ZS-U5 v1.0 (astrophysical GW channel) |
| BH–BH monopole O(A²) | TESTABLE | ZS-U5 v1.0, ZS-A2 v1.0 (G\_eff) |
| τ\_n hierarchy | SUGGESTIVE | ZS-F2 v1.0 (A), ZS-F5 v1.0 ((Z,X,Y)) |
| BH \= X-in-Y | HYPOTHESIS | ZS-F5 v1.0 (sector structure) |

**References**

\[1\] Kang, K., “ZS-F1: The Z-Spin Action & U(1) Completion,” v1.0 (2026).  
\[2\] Kang, K., “ZS-F2: Geometric Impedance A \= 35/437,” v1.0 (2026).  
\[3\] Kang, K., “ZS-F5: Gauge Symmetry Constraint,” v1.0 (2026).  
\[4\] Kang, K., “ZS-A1: Galactic Dynamics & Morphology,” v1.0 (2026).  
\[5\] Kang, K., “ZS-A2: Astrophysical Signatures,” v1.0 (2026).  
\[6\] Kang, K., “ZS-U5: Quantum Gravity Bridge,” v1.0 (2026).  
\[7\] Wald, R. M., Phys. Rev. D 48, R3427 (1993).  
\[8\] Damour, T. & Esposito-Farèse, G., PRL 70, 2220 (1993).  
\[9\] Coleman, S., Phys. Rev. D 15, 2929 (1977).  
\[10\] Coleman, S. & De Luccia, F., Phys. Rev. D 21, 3305 (1980).  
\[11\] Super-Kamiokande Collaboration, arXiv:2010.16098 (2020).  
\[12\] Hyper-Kamiokande Collaboration, arXiv:1805.04163 (2018).  
\[13\] LIGO/Virgo Collaboration, PRL 119, 161101 (2017).  
\[14\] Einstein Telescope Collaboration, JCAP 03, 050 (2020).  
\[15\] LISA Collaboration, arXiv:2402.07571 (2024).  
\[16\] ngEHT Collaboration, Galaxies 11, 107 (2023).

**Version History**

**v1.0 (March 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0. All cross-references use Grand Reset v1.0 codes. Word count note: v1.0 is \~15% shorter than internal v2.0.0 due to: (1) removal of internal version tracking annotations; (2) consolidation of redundant cross-reference paragraphs; (3) compression of Version History entries. All physics sections, equations, tables, and epistemic classifications are preserved. No derivations or results removed.