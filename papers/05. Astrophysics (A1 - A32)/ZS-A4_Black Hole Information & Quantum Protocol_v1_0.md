**ZS-A4**

**Black Hole Information & Quantum Protocol**

Seam Witness, Decoupling Proxy, Q=11 Register,  
Lattice Gauge Simulation, and Statistical Decision Framework

**Kenny Kang**  
Version 1.0 — March 2026

Theme: Astrophysics \[ZS-A\]  |  Paper 4 of 6  
Verification: 54 checks (47 computed, 2 honest, 5 declarative) | All PASS | Zero Free Parameters  
Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0

**§0. Abstract**

We define measurable, device-level diagnostics of information preservation in Z-Spin black-hole microtheory by mapping the ε-horizon (ZS-A3 v1.0) to an operational near-horizon membrane and re-expressing the seam gate J as a channel-level antiunitary conjugation constraint. Two co-primary observables are preregistered:

**(E1) Seam witness useam(Λ)** measuring conjugation defect on the Choi state: useam \= ||(J⊗J)CΛ(J⊗J) − CΛT||F / ||CΛ||F. Under the seam constraint, useam \= 0 exactly.

**(E2) Decoupling proxy Δ2** bounding information-flow recoverability: Δ2 \= Tr(ρ²RB′) − (1/dR)Tr(ρ²B′). Both estimated via hardware-friendly classical-shadow routines.

The statistical decision procedure is preregistered at clinical-trial rigour: ROPE/TOST equivalence gate (self-contained, zero external dependencies), Holm–Bonferroni co-primary control, five negative controls (NC1–NC5 including NC4 leakage gate), and five outcome levels (PASS\_FULL, PASS\_MINIMAL, FAIL\_EQUIVALENT, FAIL\_UNDERPOWERED, INVALID\_PROTOCOL). The decision framework is designed as a CLI pipeline (JSON→JSON); the current release provides the verify stage.

The Q \= 11 register (ZS-F5 v1.0) provides MUB(Q) \= Q+1 \= 12 \= G (PROVEN) and Q²−1 \= 120 \= |Ih| (structural identity). Lattice gauge simulation on the truncated octahedron (72 qubits, feasible on current hardware) tests whether Z-Spin geometry produces faster β-function convergence.

Verification: 54/54 PASS. Seven falsification gates (F-A4.1–A4.7).

**Keywords:** *black hole information, seam gate, Choi state, classical shadows, TOST, Q=11 qudit, MUB, lattice gauge, truncated octahedron, falsification*

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | :---: |
| PROVEN | Mathematical theorem (J²=I, MUB(Q)=Q+1, Δ₂ bound). |
| DERIVED | Follows from action \+ prior papers; conditional where noted. |
| HYPOTHESIS | Motivated conjecture (horizon seam); testable. |
| TESTABLE | Quantitative prediction with pre-registered falsification. |
| HONEST | Limitation explicitly documented (toy vs hardware caveat). |

**§1. Inputs from Prior Papers**

No new assumptions are introduced. All quantities are locked from prior papers:

| Quantity | Value | Source |
| :---: | :---: | :---: |
| A | 35/437 \= 0.080092 | ZS-F2 v1.0 |
| (Z, X, Y) | (2, 3, 6); Q=11, G=12 | ZS-F5 v1.0 |
| z\* | 0.4383 \+ 0.3606i | ZS-F3 v1.0 |
| |f′(z\*)| | 0.891514 | ZS-F3 v1.0 L5 |
| J|j⟩ \= |10−j⟩ | Q=11 seam involution | ZS-M3 v1.0 |
| ε-horizon, Wald entropy | S\_BH \= F(ε\_H)A\_H/(4G\_\*) | ZS-A3 v1.0 |

U(1) completion (ZS-F1 v1.0): Φ(x) \= |Φ|e{iθ}, vacuum manifold S¹ implies π1(S¹) \= ℤ. Nontrivial winding forces |Φ| → 0 at vortex cores, providing a conditional upgrade path for the Z-anchor: within the n≠0 winding sector, |Φ|→0 is DERIVED (see ZS-A6 v1.0 Theorem A). The physical realization depends on whether the BH exterior carries nontrivial winding (Q≠0), which remains HYPOTHESIS pending NR confirmation (ZS-A3 v1.0).

**§2. Black-Hole Horizon as Z-Anchor Membrane**

The Z-anchor is an operational near-horizon membrane whose reduced state is Z2\-symmetric. In U(1) language, |Φ| is suppressed on the membrane layer while θ (Goldstone mode) fluctuates.

**DERIVED:** Nontrivial U(1) winding around contractible Euclidean time circle forces |Φ| \= 0\.

**HYPOTHESIS (H-Λ):** The effective horizon channel Λ satisfies an antiunitary seam-conjugation constraint. The falsifiable content is the smallness of useam relative to matched GR+EFT controls.

**§3. Wald Entropy Normalization**

**SBH \= F(εH) × AH/(4G\*)**   with F(ε) \= 1+**A**ε²    (1)

**SZS \= \[1/(1+A)\] × SGR**    (2)

**ΔS/SGR \= A/(1+A) ≈ 7.4%**   (not tunable — fixed by **A** \= 35/437)    (3)

\[STATUS: **DERIVED**\] Conditional on Z-anchor. Factor A/(1+**A**) is locked.

**§4. Co-Primary Measurable Endpoints**

| Observable | Definition | Estimator | Role |
| :---: | :---: | :---: | :---: |
| u\_seam (E1) | ||(J⊗J)C\_Λ(J⊗J)−C\_Λ^T||\_F/||C\_Λ||\_F | Shadow Pauli overlaps | CO-PRIMARY: seam |
| Δ₂ (E2) | Tr(ρ²\_{RB'})−(1/d\_R)Tr(ρ²\_{B'}) | Purity via shadows | CO-PRIMARY: decoupling |
| u\_chan | (1/(d²−1))Tr(T^T T) | Randomized benchmarking | SECONDARY: unitarity |

**4.1 Seam Witness u\_seam (E1)**

Stinespring dilation: Λ(ρ) \= TrE\[U(ρ⊗σH)U†\], with seam constraint (J⊗I)U(J⊗I) \= U\*. Then:

**(J⊗J) CΛ (J⊗J) \= CΛ**T **⇒ useam \= 0**    (4)

\[STATUS: **DERIVED**\] Choi identity from Stinespring seam constraint. PROVEN bound for Δ2.

**4.2 Decoupling Proxy Δ₂ (E2)**

**δdecouple ≤ √(dR dB′) √Δ2**   (PROVEN)    (5)

Shadow-estimable from purities alone. Mandatory debiasing: μ̂² \= (mX̄² − 1)/(m−1).

**§5. Q \= 11 Register Implementation**

**5.1 MUB–Gauge Identity**

**MUB(Q) \= Q+1 \= 12 \= G**   (PROVEN for prime Q \= 11\)    (6)

Connects Z-Spin slot register Q \= 11 with gauge algebra dimension G \= 12 through a number-theoretic theorem.

**5.2 Tomographic–Symmetry Identity**

**Q² − 1 \= 120 \= |Ih|**   (STRUCTURAL)    (7)

**5.3 Implementation Tracks**

| Track | Register | Qubits | Hardware |
| :---: | :---: | :---: | :---: |
| A: native qudit | Q \= 11 directly | 11 levels | Trapped-ion qudits |
| B: 4-qubit | d \= 16 (embed 11\) | 4 qubits | IBM / Google |
|  | Leakage: states 11–15 | NC4 monitors | p\_leak \< 0.01 |

**§6. Negative Controls (NC1–NC5)**

| ID | Action | Expected | Purpose |
| :---: | :---: | :---: | :---: |
| NC1 | Replace J by random involution R | u\_R \= O(1) | Specificity |
| NC2 | Phase-scramble perturbation | u\_seam → O(1) | Sensitivity |
| NC3 | Shuffle Pauli pairing | Signal disappears | Estimator sanity |
| NC4 | Inject leakage (Track B) | p\_leak \> 1% ⇒ INVALID | Leakage gate |
| NC5 | Measurement schedule mismatch | Signal disappears | Schedule confound |

NC4: Code-subspace projector Pcode \= Σj=010 |j⟩⟨j|, rank-11 on ℂ¹⁶. Leakage: pleak \= 1 − Tr(Pcode ρ Pcode). If pleak \> 0.01, run is INVALID\_PROTOCOL.

All negative controls must PASS before interpretive claims. A single NC failure ⇒ INVALID\_PROTOCOL.

**§7. Preregistered Statistical Decision Procedure**

**7.1 Protocol Validity Gate**

Before any test: (a) bin QC; (b) NC1–NC5 all pass; (c) compile-matching contract (Δdepth \= 0, Δn2q \= 0, identical edge multiset, same schedule, calibration ±24h). Any failure ⇒ INVALID\_PROTOCOL.

**7.2 ROPE/TOST Equivalence Failure**

**TOST: both one-sided t-tests reject at αtost \= 0.05 within δrope \= 0.25 × sdpooled(E1)**    (8)

Self-contained t-CDF via Lanczos Γ-approximation and Lentz continued-fraction for regularized incomplete beta Ix(a,b). Zero external dependencies. TOST can never be skipped. Welch–Satterthwaite degrees of freedom throughout.

**7.3 Discovery Gate: Holm–Bonferroni**

E1 and E2 tested jointly (m \= 2). Reject H(1) if p(1) \< α/2 \= 0.005; then reject H(2) if p(2) \< α \= 0.01. Minimum effect size d ≥ 1.0.

**7.4 Outcome Levels**

| Outcome | Condition |
| :---: | :---: |
| PASS\_FULL | E1+E2 both Holm \+ d\_target; not TOST-equivalent; all QC/NC pass |
| PASS\_MINIMAL | E1 passes; E2 does not; all QC/NC pass |
| FAIL\_EQUIVALENT | TOST: E1 equivalent within ROPE |
| FAIL\_UNDERPOWERED | Neither TOST nor Holm rejects |
| INVALID\_PROTOCOL | Any QC, NC (incl. NC4), or matching gate fails |

**7.5 CLI Decision Pipeline**

**verify:** Run verification suite → JSON report. **decide:** Load JSON decision input → compute bin QC, stratified permutation, TOST, Holm, Cohen’s d → machine-generated JSON report. **template:** Export decision input schema. No narrative-only tuning permitted. Note: The current release provides the verify stage (ZS\_A4\_v1\_0\_verification.py). The decide and template stages are specified but not yet implemented; their implementation is registered as a pre-hardware deliverable.

**§8. Lattice Gauge Quantum Simulation**

**Prediction P1:** SU(2) lattice gauge on truncated octahedron converges faster to continuum β-function a2 \= 19/6 than on generic Archimedean lattices of comparable size (≥2σ).

| Lattice | V | E | F | (V+F)/G | Match a₂? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| Truncated octahedron | 24 | 36 | 14 | 19/6 \= 3.167 | ★ EXACT |
| Cuboctahedron | 12 | 24 | 14 | 26/12 \= 2.167 | ✗ |
| Rhombicuboctahedron | 24 | 48 | 26 | 50/12 \= 4.167 | ✗ |
| Snub cube | 24 | 60 | 38 | 62/12 \= 5.167 | ✗ |

Resource: SU(2), j=1/2 truncation: 36 links × 2 qubits \= 72 qubits. Feasible on IBM Eagle (127q) in 2025–2026.

\[STATUS: **TESTABLE**\] Unique geometric match. Current-hardware feasible. P1 is pre-registered.

**§9. Falsification Registry**

Multi-layer structure: \[OBS\] observational/experimental gates. All A4 gates are experimental (hardware runs, NC tests). Mathematical consistency (J²=I, MUB theorem) verified in computation suite.

| ID | Condition | Experiment | Timeline |
| :---: | :---: | :---: | :---: |
| F-A4.1 \[OBS\] | FAIL\_EQUIVALENT on E1 under ROPE/TOST | First hardware run | PRIMARY |
| F-A4.2 \[OBS\] | NC1 fails (random involution gives u≈0) | Same batch | BLOCKING |
| F-A4.3 \[OBS\] | NC3 fails (shuffle doesn’t destroy signal) | Same batch | BLOCKING |
| F-A4.4 \[OBS\] | NC4: p\_leak \> 1% in 4-qubit embedding | Same batch | BLOCKING |
| F-A4.5 \[OBS\] | Wald ΔS/S ≠ A/(1+A) within 3σ | EHT \+ future | OPEN |
| F-A4.6 \[OBS\] | Seam J incompatible with Q=11 qudit HW | Hardware impl. | OPEN |
| F-A4.7 \[OBS\] | NC5: schedule mismatch reproduces signal | Same batch | BLOCKING |

**§10. Epistemic Classification Summary**

| Result | Status | Confidence | Falsification |
| :---: | :---: | :---: | :---: |
| J²=I, dim(E+)=6, dim(E-)=5 | PROVEN | HIGH | — |
| (J⊗J)C\_Λ(J⊗J)=C\_Λ^T | DERIVED | HIGH | F-A4.1 \[OBS\] |
| Δ₂ bounds δ\_decouple | PROVEN | HIGH | — |
| Wald: ΔS/S=7.4% | DERIVED (cond.) | MED | F-A4.5 \[OBS\] |
| u\_seam distinguishes ZS/CTL | HYPOTHESIS | LOW–MED | F-A4.1,2,3 |
| Horizon satisfies seam | HYPOTHESIS | LOW | F-A4.1 \[OBS\] |
| MUB(Q)=Q+1=12=G | PROVEN | HIGH | — |
| Lattice convergence P1 | TESTABLE | MED | 2025–2026 HW |

**§11. Removed Claims and Honest Assessment**

**Removed from v1.0.0:** (1) Iseam/Ifull \> 1 (direct sum ≠ tensor product). (2) Negative entropy (projector bug FIX-A). (3) Entropy oscillation \= unitarity (replaced by uchan \+ Δ2).

**Toy vs Hardware caveat:** Verification suite uses idealized toy generators producing Cohen’s d \~ 28\. This confirms pipeline self-consistency but does NOT predict hardware effect sizes. Decoherence and gate errors will reduce ZS–CTL separation. The protocol handles this via attenuation factor α and the FAIL\_EQUIVALENT outcome.

\[STATUS: **HONEST**\] Toy PASS \= ‘protocol works as designed’, NOT ‘experiment has already succeeded.’

**§12. Conclusions**

**Co-primary endpoints.** useam (seam symmetry) and Δ2 (decoupling) provide complementary diagnostics of information preservation, both estimable via classical shadows on near-term quantum hardware.

**Clinical-trial rigour.** ROPE/TOST equivalence gate, Holm–Bonferroni co-primary control, five negative controls, and five outcome levels ensure that positive results are not artifacts of protocol design. The CLI pipeline (verify stage implemented; decide/template stages pending) is designed to produce machine-generated decisions with zero narrative tuning.

**Q \= 11 register.** MUB(Q) \= G \= 12 (PROVEN theorem) and Q²−1 \= |Ih| \= 120 (structural identity) connect quantum information to Z-Spin group theory. Implementation on trapped-ion qudits (Track A) or 4-qubit embeddings (Track B) with NC4 leakage monitoring.

**Lattice gauge simulation.** Prediction P1 (truncated octahedron convergence) is uniquely testable on 72-qubit hardware available in 2025–2026. Among Archimedean solids, only the truncated octahedron gives (V+F)/G \= a2(SM).

**Honest limitations.** Horizon seam hypothesis has LOW confidence. Toy effect sizes do not predict hardware results. Three v1.0.0 overclaims were removed. All structural identities in Appendix A are clearly separated from the falsifiable protocol.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

**Code Availability.** Verification script: ZS\_A4\_v1\_0\_verification.py. Dependencies: Python 3.10+, NumPy. Execution: python3 ZS\_A4\_v1\_0\_verification.py. Expected output: 54/54 PASS, exit code 0\. Test composition: 47 computational, 2 honest-assessment, 5 declarative (9%).

**Appendix A. Key Formulae**

J|j⟩ \= |Q−1−j⟩ \= |10−j⟩    (seam gate on Q=11)  
dim(E\+) \= Y \= 6,  dim(E−) \= Q−Y \= 5  
useam \= ||(J⊗J)CΛ(J⊗J) − CΛT||F / ||CΛ||F  
ΔS/SGR \= A/(1+A) \= 7.42%  
MUB(Q) \= Q+1 \= 12 \= G    (Wootters-Fields, prime Q)  
Q²−1 \= 120 \= |Ih|    (tomographic-symmetry identity)  
(V+F)/G \= 38/12 \= 19/6 \= a2(SM)    (truncated octahedron)

**Appendix B. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| :---: | :---: | :---: | :---: |
| \[A\] Locked Inputs | 6 | 6/0 | A, Q=11, G=12, z\*, |f′|, ΔS/S |
| \[B\] Seam Gate J | 5 | 5/0 | J²=I, dim(E±), W\_p compatible |
| \[C\] Co-Primary Endpoints | 5 | 5/0 | u\_seam, Δ₂, Choi identity |
| \[D\] Q=11 Register & MUB | 4 | 4/0 | MUB=12=G, Q²-1=120=|I\_h| |
| \[E\] Negative Controls | 5 | 5/0 | NC1–NC5 all verified |
| \[F\] Statistical Decision | 6 | 6/0 | TOST, Holm, 5 outcomes, CLI |
| \[G\] Wald Entropy | 3 | 3/0 | ΔS/S=7.42% locked |
| \[H\] Lattice Gauge | 4 | 4/0 | 19/6=a₂, 72 qubits feasible |
| \[I\] Epistemic Honesty | 4 | 4/0 | Toy caveat, 3 removed claims |
| \[J\] Falsification Gates | 7 | 7/0 | F-A4.1–A4.7 |
| \[K\] Cross-Paper | 5 | 5/0 | ZS-F1,F2,F5,A3,M3 |
| TOTAL | 54 | 54/0 | 100% pass rate |

**Appendix C. Cross-Reference Table**

| Result | Status | Dependencies |
| :---: | :---: | :---: |
| Seam gate J, dim(E±) | PROVEN | ZS-F5 v1.0 (Q=11, Y=6), ZS-M3 v1.0 |
| Choi identity u\_seam=0 | DERIVED | Stinespring \+ seam constraint |
| Δ₂ bound | PROVEN | Standard quantum info theory |
| Wald ΔS/S=7.42% | DERIVED (cond.) | ZS-A3 v1.0, ZS-F2 v1.0 (A=35/437) |
| MUB(Q)=G=12 | PROVEN | Number theory (prime Q) |
| Q²−1=|I\_h|=120 | STRUCTURAL | ZS-F5 v1.0, group theory |
| Lattice convergence P1 | TESTABLE | ZS-F5 v1.0 (polyhedra), ZS-S1 v1.0 |
| TOST/Holm framework | STANDARD | Clinical trial methodology |

**References**

\[1\] Kang, K., “ZS-F1: The Z-Spin Action & U(1) Completion,” v1.0 (2026).  
\[2\] Kang, K., “ZS-F2: Geometric Impedance A \= 35/437,” v1.0 (2026).  
\[3\] Kang, K., “ZS-F5: Gauge Symmetry Constraint,” v1.0 (2026).  
\[4\] Kang, K., “ZS-A3: Black Hole Physics,” v1.0 (2026).  
\[5\] Kang, K., “ZS-M3: Regge-Holonomy, Immirzi & Z-Telomere,” v1.0 (2026).  
\[6\] Wald, R. M., Phys. Rev. D 48, R3427 (1993).  
\[7\] Hayden, P. & Preskill, J., JHEP 09, 120 (2007).  
\[8\] Huang, H.-Y. et al., Nat. Phys. 16, 1050 (2020).  
\[9\] Elben, A. et al., Rev. Mod. Phys. 95, 025003 (2023).  
\[10\] Lakens, D., Equivalence Tests, Routledge (2017).  
\[11\] Holm, S., Scand. J. Statist. 6, 65 (1979).  
\[12\] Wootters, W. K. & Fields, B. D., Ann. Phys. 191, 363 (1989).  
\[13\] Planck Collaboration, A\&A 641, A6 (2020).  
\[14\] Kim, Y. et al., Nature 618, 500 (2023). IBM Eagle 127-qubit utility.

**Version History**

**v1.0 (March 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0 (Paper 25 v2.2.0 \+ Paper 14 v2.0.0). All cross-references use Grand Reset v1.0 codes. Verification suite rebuilt with 47/54 computational tests (9% declarative, down from 80%). Verification: 54/54 PASS.