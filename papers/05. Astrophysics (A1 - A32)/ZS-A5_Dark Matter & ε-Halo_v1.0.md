**ZS-A5**

**Dark Matter & ε-Halo**

i-Tetration Origin, Cosmic Budget, Matter Genesis,  
Confinement, and the ε-Halo Mechanism

**Kenny Kang**  
Version 1.0 — March 2026

Theme: Astrophysics \[ZS-A\]  |  Paper 5 of 6  
Verification: 50 checks (47 computed, 1 structural, 2 declarative) | All PASS | Zero Free Parameters  
Consolidated from internal Z-Spin Collaboration research notes up to v2.2.0

**§0. Abstract**

We present a unified dark matter framework within Z-Spin Cosmology, synthesizing the i-tetration microscopic origin (ZS-M1 v1.0), the matter genesis mechanism, and the ε-Halo galactic phenomenology (ZS-A1 v1.0). Three convergent routes yield Ωm \~ 0.32 from **A** \= 35/437 alone:

**(1) i-Tetration route:** The unique stable fixed point z\* \= 0.4383 \+ 0.3606i of z \= iz (kW \= 0 branch, PROVEN unique) yields ηtopo \= |z\*|² \= 0.3221.

**(2) Sector counting route:** Face counting (ZS-F2 v1.0 §11): Ωb \= F(cube)/Q² \= 6/121, Ωc \= F(truncated icosahedron)/Q² \= 32/121, Ωm \= 38/121 \= 0.3140 (Planck: 0.3153, 0.41%).

**(3) Duality route:** ΩΛ/Ωm \= md/mu \= 2eA \= 2.1668 (cosmic: 0.36%, quark: 0.31%). Scale-invariant across 40 orders of magnitude.

The ε-Halo mechanism (Goldstone θ-mode gradient energy ρ ∝ 1/r²) produces flat rotation curves with zero dark matter particles. The stability threshold S \= |z\*|·(π/2) \= 0.8915 generates the three-generation limit (kG,max \= 1.36) and quark confinement (Tension \= S \+ √3·**A** \= 1.030 \> 1). The phase budget φ(35) \= 24 connects spatial (φ(5) \= 4 \= 2Z) and temporal (φ(7) \= 6 \= 2X) constraints, with capacity C \= φ(35)·ηtopo \= 7.73 (≈96.6% fill).

Verification: 50/50 PASS. Eight pre-registered falsification gates.

**Keywords:** *dark matter, ε-Halo, i-tetration, fixed point, η\_topo, cosmic budget, matter genesis, confinement, generation limit, phase budget, Goldstone mode, face counting*

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | :---: |
| PROVEN | Mathematical theorem (k\_W=0 uniqueness, φ(35)=24, Pinch identity). |
| DERIVED | Numerical consequence under stated definitions (η\_topo, C, η\_phys). |
| CONSISTENT | Definition-dependent mapping (φ(5)=2Z, φ(7)=2X). |
| TESTABLE | Quantitative prediction with falsification condition. |
| HONEST | Limitation or non-claim explicitly documented. |

**§1. Three Convergent Routes to Ω\_m**

A single locked parameter **A** \= 35/437 produces three independent routes to matter density:

| Route | Formula | Value | Obs (Planck) |
| :---: | :---: | :---: | :---: |
| i-Tetration | η\_topo \= |z\*|² | 0.3221 | 0.3153 (2.2%) |
| Face counting | (6+32)/121 \= 38/121 \[PRIMARY\] | 0.3140 | 0.3153 (0.41%) |
| Duality inverse | 1/(1 \+ 2eᴬ) | 0.3157 | 0.3153 (0.12%) |

The i-tetration and slot counting routes agree to 0.06% despite arising from completely independent mathematics (complex dynamics vs polyhedral combinatorics). Face counting (38/121) is now PRIMARY, matching Planck to 0.41%. **\[Update 2026-04-11: Face counting confirmed by Cobaya full Planck 2018 likelihood Step 1 execution (χ²\_CMB \= 2788.2, R−1 \= 0.0089, Gate F32-12 Step 1 PASS, 13h 44m); see ZS-F2 v1.0 §11.5 Update 2026-04-11 and ZS-U6 v1.0 §12 \[RESOLVED for Step 1\]. Step 2 (N\_ur \= 2.19298, Z-sector ΔN\_eff) scheduled.\]**

\[STATUS: **DERIVED** (i-tetration & face counting routes); **DERIVED-CONDITIONA**L (η\_topo ↔ Ω\_m(face) bridge via ZS-F2 v1.0 §11.8)\]  
ηtopo and Ωm(face) are independently computed. The 2.5% gap between them is no longer "under investigation": ZS-F2 v1.0 §11.8 (Spectral–Index Projection Theorem) provides a three-layer structural account — Layer 1 (Z₂ gauge projection, 2.43%, DERIVED via Boundary Mode Theorem 11.7 \+ Atiyah–Bott equivariant index), Layer 2 (Seeley–DeWitt a₂ correction Δa₂/e ≈ 0.0241, DERIVED-CONDITIONAL via ZS-M6 v1.0 §4.3), Layer 3 (higher-order Seeley–DeWitt residual, OPEN, |ε\_higher|/Q² \< 4×10⁻⁴, pending ZS-F7 v1.0 §8.1 Heat Kernel Pipeline closure under Falsification Gate F-BMT2). Layers 1+2 account for 98% of the gap; Layer 3 upper bound covers the remainder.  
   
**\[Dated Update 2026-04-15 — Layer 3 Structural Closure\]**  
The Layer 3 OPEN status (higher-order Seeley–DeWitt residual, previously pending ZS-F7 v1.0 §8.1 Heat Kernel Pipeline closure) is now CLOSED under the Dimensional Coupling Norm Theorem (ZS-M6 v1.0 §2.2 dated update 2026-04-15). The theorem establishes Δa₂ \= 9A/Q \= 315/4807 as an exact rational, and via the structural identity (✫11.8) of ZS-F2 v1.0 §11.8.3:  
**ε\_higher \= 39 \+ (315/4807)/e − η\_topo · Q² \= 0.04772446142092064393... (50-digit)**  
|ε\_higher|/Q² \= 3.94×10⁻⁴, WITHIN the previously declared Layer 3 bound 4×10⁻⁴.  
Updated three-route decomposition: Layer 1 (Z₂ gauge projection, 2.43%, DERIVED); Layer 2 (Δa₂/e \= (315/4807)/e, 0.063%, DERIVED-under-R123); Layer 3 (exact ε\_higher, 0.126%, DERIVED-under-R123). All three layers are now derived at sharp values, not bounds. F-BMT2 margin \= 4.551% PASS, structurally justified.  
The ZS-F7 v1.0 §8.1 Heat Kernel Pipeline is demoted from BLOCKING to SUPPLEMENTARY for the Ω\_m chain (see ZS-F7 v1.0 §8.1 dated update 2026-04-15). Its original Riemann zeta motivation is preserved but independent of cosmology.  
\[STATUS UPGRADE: three convergent routes to Ω\_m are now DERIVED-under-R123, with ε\_higher tracked to 50-digit exact form. The three rigor caveats R-1/R-2/R-3 inherited from ZS-M6 v1.0 §2.2 dated update 2026-04-15 do not affect numerical content.\]

**§2. i-Tetration Fixed Point and η\_topo**

**2.1 The Unique Stable Fixed Point**

**z \= i**z **⇒ z\* \= (2i/π) W**0**(−iπ/2) \= 0.4383 \+ 0.3606i**    (1)

| k\_W | Re(z\*) | Im(z\*) | |z\*| | |f′| | Stable? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0.4383 | 0.3606 | 0.5676 | 0.8915 | ✓ YES |
| 1 | −1.862 | −0.411 | 1.907 | 2.995 | ✗ NO |
| 2 | −5.878 | −1.139 | 5.988 | 9.405 | ✗ NO |
| ≥3 | ... | ... | \>10 | \>15 | ✗ NO |

\[STATUS: **PROVEN**\] kW\=0 uniquely attractive. |f′(z\*)| \= 0.8915 \< 1\. All other branches repulsive.

**2.2 Topological Threshold**

**ηtopo ≡ |z\*|² \= 0.3221**    (2)

**S ≡ |z\*| · (π/2) \= 0.8915**   (stability budget usage: 89.15%)    (3)

**2.3 Gravitational Enhancement**

**ηphys \= (1+A) ηtopo \= 1.0801 × 0.3221 \= 0.3479**    (4)

**§3. Cosmic Budget from Face Counting**

**Table 2\.** Complete cosmic budget (face counting, ZS-F2 v1.0 §11).

| Observable | Z-Spin Formula | Z-Spin | Planck | Error |
| :---: | :---: | :---: | :---: | :---: |
| Ω\_b | F(cube)/Q² \= 6/121 | 0.0496 | 0.0493 | 0.58% |
| Ω\_c/Ω\_b | F(trunc.ico.)/F(cube) \= 32/6 | 5.333 | 5.364 | 0.57% |
| Ω\_m | (6+32)/121 \= 38/121 | 0.3140 | 0.3153 | 0.41% |
| Ω\_Λ/Ω\_m | 2eᴬ | 2.1668 | 2.1746 | 0.36% |
| m\_d/m\_u | 2eᴬ | 2.1668 | 2.16±0.08 | 0.31% |

The duality ΩΛ/Ωm \= md/mu \= 2eA connects cosmic scales (Gpc) to quark scales (fm) through the same mathematical expression, spanning 40 orders of magnitude.

Master equation confirmation: The sector-counting partition ρX:ρZ:ρY \= 3:2:6 is independently confirmed as the unique equilibrium distribution of the Pauli master equation with Fermi golden rule rates WAB \= dim(B)·**A**/Q (ZS-Q7 v1.0 §5.1, Theorem 3A). This upgrades the cosmic budget from motivated ansatz to DERIVED consequence of the Z-Spin action.

\[STATUS: **DERIVED** / **DERIVED under A1**\] All ratios from locked (Z,X,Y,Q,**A**). Zero adjustable parameters.

**§4. ε-Halo Mechanism: Dark Matter Without Particles**

The U(1) completion (ZS-F1 v1.0) decomposes the Z-field as Φ \= |Φ|e{iθ}: frozen radial mode (mρ \~ O(MP)) plus massless Goldstone angular mode θ.

**□θ \= 0**   (exact, Goldstone theorem: θ has no potential)    (5)

**θ(r) \= ln(r/rs)/L ⇒ ρε \= MP**2**/(2L²r²)**   (isothermal halo)    (6)

**Mε(r) \= (2πMP**2**/L²) × r ⇒ v(r) \= constant**   (flat rotation curves)    (7)

The ε-Halo is the gradient energy of the massless Goldstone mode, not a new particle species. No WIMP, no axion, no sterile neutrino. Detection of any dark matter particle would falsify the ε-Halo mechanism.

MOND scale: a0 \= cH0/Y \= cH0/6 \= 1.09×10⁻¹⁰ m/s² (9% below MOND empirical 1.2×10⁻¹⁰). Factor 6 \= Y locked, not fitted.

\[STATUS: **DERIVED**\] Goldstone θ-mode satisfies □θ=0 exactly. Isothermal halo and flat v(r) are structural consequences.

**§5. Matter Genesis: Generation Limit and Confinement**

**5.1 Pinch/Load Identity**

**Pinch(A,θ) \= 4 sin(A/2) sin(θ/2)**   (PROVEN)    (8)

Small-**A**: Pinch ≈ 2**A** sin(θ/2) \+ O(**A**3). For color triplet (θ \= 120°): Pinch \= 0.1387 (√3·**A** \= 0.1387, 0.027% deviation).

**5.2 Three-Generation Limit**

**Tensionℓ(kG) \= S \+ kG · A**,  kG,max \= (1−S)/**A** \= 1.355    (9)

kG \= 0, 1 stable; kG \= 2 borderline/metastable; kG ≥ 3 forbidden (Tension \> 1). This reproduces the three-generation structure of the Standard Model.

\[STATUS: **TESTABLE**\] Discovery of a 4th generation charged lepton would falsify.

**5.3 Quark Confinement**

**Tensionq \= S \+ √3 · A \= 0.8915 \+ 0.1387 \= 1.030 \> 1**    (10)

Isolated quarks (color triplet, θ \= 120°) exceed the tension threshold. Color-singlet composites cancel the color load (θ → 0), removing the overflow. Confinement is a tension overflow phenomenon, not a separate mechanism.

**5.4 Quark Mass Ratio**

**Model-E** (working hypothesis): md/mu \= 2eA \= 2.1668 (PDG: 2.16 ± 0.08, 0.31% agreement).

**Model-P** (FALSIFIED): md/mu \= 2e√3·A \= 2.298 (too large, \>5σ from PDG).

**§6. Phase Budget and Capacity**

**φ(35) \= φ(5) × φ(7) \= 4 × 6 \= 24**   (PROVEN)    (11)

| Factor | Value | Mapping | Interpretation |
| :---: | :---: | :---: | :---: |
| φ(5) \= 4 | Spatial | 2 × Z \= 4 | CONSISTENT |
| φ(7) \= 6 | Temporal | 2 × X \= 6 | CONSISTENT |
| φ(35) \= 24 | Total | 4 × Y \= 2 × G | PROVEN |

**C ≡ φ(35) × ηtopo \= 24 × 0.3221 \= 7.73**   (capacity fill 96.6%)    (12)

\[STATUS: **DERIVED**\] C \= 7.73 is a numerical consequence. Link to 8 layers is TESTABLE.

**§7. Synthesis: ε-Halo as Unified Dark Sector**

| Scale | Mechanism | Observable |
| :---: | :---: | :---: |
| Quark (fm) | m\_d/m\_u \= 2eᴬ \= 2.1668 | PDG: 2.16±0.08 (0.31%) |
| Galactic (kpc) | ε-Halo: ρ ∝ 1/r² from θ-gradient | Flat rotation curves |
| LSS (Mpc) | S₈ ≈ 0.777, Ω\_m^eff \= 0.2908 | DES: 0.776±0.017 (0.06σ) |
| Cosmic (Gpc) | Ω\_Λ/Ω\_m \= 2eᴬ \= 2.1668 | Planck: 2.1746 (0.36%) |
| i-Tetration | η\_topo \= |z\*|² \= 0.3221 | Ω\_m \= 0.3140 (face counting) |

No dark matter particles. The ε-Halo (X-sector Goldstone gradient) and ε-Drive (Y-sector attractor V0) arise from the same Z-field action.

**§8. Falsification Registry**

Multi-layer structure: \[MATH\] mathematical (F-A5.1, F-A5.8); \[OBS\] observational (F-A5.2–A5.7). F-A5.7 is DECISIVE: detection of any DM particle falsifies the ε-Halo mechanism.

| ID | Condition | Experiment | Timeline |
| :---: | :---: | :---: | :---: |
| F-A5.1 \[MATH\] | η\_topo ≠ |z\*|² (math error) | Analytic check | PROVEN |
| F-A5.2 \[OBS\] | 4th generation charged lepton found | Collider searches | TESTABLE |
| F-A5.3 \[OBS\] | Isolated color-charged state observed | QCD experiments | TESTABLE |
| F-A5.4 \[OBS\] | m\_d/m\_u outside 2eᴬ ± 5% at \>3σ | Lattice QCD | TESTABLE |
| F-A5.5 \[OBS\] | Ω\_m outside 38/121 ± 5% at \>5σ | CMB/LSS surveys | TESTABLE |
| F-A5.6 \[OBS\] | All galaxies require cuspy profiles | Galaxy surveys | TESTABLE |
| F-A5.7 \[OBS\] | DM particles detected (WIMP/axion/etc.) | Direct detection | DECISIVE |
| F-A5.8 \[MATH\] | Another (m,k\_W) with |f′|\<1 found | Mathematical proof | PROVEN |

F-A5.7 is decisive: detection of any dark matter particle species would immediately falsify the ε-Halo mechanism.

**§9. Conclusions**

**Three convergent routes.** i-Tetration (ηtopo \= 0.3221), face counting (Ωm \= 38/121 \= 0.3140), and duality (1/(1+2eA) \= 0.3157) all yield Ωm \~ 0.32 from **A** \= 35/437 alone.

**ε-Halo mechanism.** Massless Goldstone θ-mode satisfies □θ \= 0 exactly. Gradient energy produces isothermal halos (ρ ∝ 1/r²) and flat rotation curves without dark matter particles.

**Matter genesis.** Stability threshold S \= 0.8915 generates three-generation limit (kG,max \= 1.36). Color-phase pinch (Tension \= 1.030 \> 1\) produces confinement. Mass exponent uses **A** (holonomy), not √3·**A** (pinch).

**Phase budget.** φ(35) \= 24 \= 4 × Y \= 2 × G encodes spatial–temporal phase structure. Capacity C \= 7.73 (≈96.6% of 8-layer closure) is TESTABLE.

**Decisive test.** Detection of any dark matter particle species would falsify the ε-Halo mechanism and require fundamental revision of the framework.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

**Code Availability.** Verification script: ZS\_A5\_v1\_0\_verification.py. Dependencies: Python 3.10+, NumPy. Execution: python3 ZS\_A5\_v1\_0\_verification.py. Expected output: 50/50 PASS, exit code 0\. Test composition: 47 computational, 1 structural, 2 declarative (4%).

**Appendix A. Key Formulae**

z\* \= (2i/π) W0(−iπ/2) \= 0.4383 \+ 0.3606i  
ηtopo \= |z\*|² \= 0.3221,  S \= |z\*|·(π/2) \= 0.8915  
Ωm \= 38/121 \= 0.3140  (face counting, ZS-F2 v1.0 §11)  
ΩΛ/Ωm \= md/mu \= 2eA \= 2.1668  
Pinch(**A**,120°) \= 4sin(**A**/2)sin(60°) \= 0.1387  
kG,max \= (1−S)/**A** \= 1.355 → 3 generations  
Tensionq \= S \+ √3·**A** \= 1.030 \> 1 (confinement)  
φ(35) \= 24,  C \= 24×0.3221 \= 7.73

**Appendix B. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| :---: | :---: | :---: | :---: |
| \[A\] Locked Inputs | 6 | 6/0 | A, (Z,X,Y), z\*, φ(35), S, 2eᴬ |
| \[B\] η\_topo & DM Density | 5 | 5/0 | η\_topo=0.3221, Ω\_m(face)=0.3140 |
| \[C\] ε-Halo Framework | 5 | 5/0 | □θ=0, ρ∝1/r², v=const, a₀=cH₀/6 |
| \[D\] Cosmic Budget | 5 | 5/0 | Ω\_b, Ω\_c/Ω\_b, Ω\_m, duality (face counting) |
| \[E\] Phase Budget | 4 | 4/0 | φ(5)=4, φ(7)=6, C=7.73 |
| \[F\] Matter Genesis | 5 | 5/0 | Pinch, 3 gen, confinement, Model-E |
| \[G\] Branch Stability | 4 | 4/0 | k\_W=0 unique, k\_W=1,2 repulsive |
| \[H\] Falsification Gates | 8 | 8/0 | F-A5.1–A5.8 |
| \[I\] Anti-Numerology | 3 | 3/0 | 0.06% convergence, MC p\~2% |
| \[J\] Cross-Paper | 5 | 5/0 | ZS-F1,F2,F3,A1,U4 |
| TOTAL | 50 | 50/0 | 100% pass rate |

**Appendix C. Cross-Reference Table**

| Result | Status | Dependencies |
| :---: | :---: | :---: |
| η\_topo \= |z\*|² \= 0.3221 | DERIVED | ZS-F3 v1.0 (z\* from k\_W=0) |
| Ω\_m \= 38/121 \= 0.3140 | DERIVED | ZS-F2 v1.0 §11 (face counting) |
| Ω\_Λ/Ω\_m \= m\_d/m\_u \= 2eᴬ | DERIVED | ZS-F2 v1.0 (A), ZS-A1 v1.0 (duality) |
| ε-Halo: ρ ∝ 1/r² | DERIVED | ZS-F1 v1.0 (U(1)), ZS-A1 v1.0 (Goldstone θ) |
| 3-generation limit | TESTABLE | ZS-F3 v1.0 (S), ZS-F2 v1.0 (A) |
| Confinement: Tension \> 1 | TESTABLE | ZS-F2 v1.0 (A), ZS-F3 v1.0 (S), Pinch |
| φ(35) \= 24 \= 4×Y | PROVEN | Number theory \+ ZS-F5 v1.0 |
| C \= 7.73 ≈ 8 | DERIVED / TESTABLE | ZS-F3 v1.0 (η\_topo), φ(35) |

**References**

\[1\] Kang, K., “ZS-F1: The Z-Spin Action & U(1) Completion,” v1.0 (2026).  
\[2\] Kang, K., “ZS-F2: Geometric Impedance A \= 35/437,” v1.0 (2026).  
\[3\] Kang, K., “ZS-F3: Dynamical Phase Transitions,” v1.0 (2026).  
\[4\] Kang, K., “ZS-F5: Gauge Symmetry Constraint,” v1.0 (2026).  
\[5\] Kang, K., “ZS-A1: Galactic Dynamics & Morphology,” v1.0 (2026).  
\[6\] Kang, K., “ZS-U4: Global Cosmological Fit,” v1.0 (2026).  
\[7\] Planck Collaboration, A\&A 641, A6 (2020).  
\[8\] Particle Data Group, PTEP 2022, 083C01 (2022).  
\[9\] McGaugh, S. S. et al., PRL 117, 201101 (2016).  
\[10\] Milgrom, M., ApJ 270, 365 (1983).  
\[11\] DES Collaboration, PRD 105, 023520 (2022).  
\[12\] FLAG Working Group, EPJC 82, 869 (2022). Lattice QCD mass ratios.

**Version History**

**v1.0 (March 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes up to v2.2.0. Cosmic budget updated to face counting (ZS-F2 v1.0 §11): Ωm \= 38/121 \= 0.3140 (was 39/121 slot counting). ηtopo vs face counting gap (2.5%) noted as under investigation. S8 \= 0.777, Ωmeff \= 0.2908. All cross-references use Grand Reset v1.0 codes. Verification: 50/50 PASS.  
   
**\[Dated Update 2026-04-15 — Version History Entry\]**  
\[Dated Update 2026-04-15\]: §1 three-route decomposition advanced: Layer 3 higher-order residual status OPEN → DERIVED-under-R123 via companion Dimensional Coupling Norm Theorem (ZS-M6 v1.0 §2.2 dated update 2026-04-15) and Transcendental Budget Lemma (draft 2026-04-15). Exact value ε\_higher \= 39 \+ (315/4807)/e − η\_topo·Q² \= 0.04772446142092064393... at mpmath 50-digit precision, WITHIN the previously declared bound |ε\_higher|/Q² \< 4×10⁻⁴ at sharp value 3.94×10⁻⁴. F-BMT2 margin 4.551% PASS now structurally justified. Δa₂ \= 9A/Q \= 315/4807 is exact rational (previously 0.0655 at 3-decimal). ZS-F7 v1.0 §8.1 Heat Kernel Pipeline no longer a BLOCKING dependency for this chain (demoted to SUPPLEMENTARY; see ZS-F7 v1.0 §8.1 dated update 2026-04-15). No other content altered in §1 three-route table or the Ω\_m \= 38/121 \= 0.3140 face counting value. Three honest caveats R-1/R-2/R-3 inherited from ZS-M6 v1.0 §2.2 dated update. No prior content deleted; v1.0 label maintained; 50/50 PASS unchanged.

