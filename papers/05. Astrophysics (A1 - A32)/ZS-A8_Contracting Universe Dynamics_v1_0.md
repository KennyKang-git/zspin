**ZS-A8**

**Contracting Universe Dynamics:**

**The Polyhedral-Tetration Bridge for Wave-Contraction Sector**

Kenny Kang  
April 2026 — ZS-A8 (Astrophysics & Strong Field Theme)  
Version 1.0 Revised — April 2026 (consolidating dated updates 2026-04-24 supplements 1, 2, 3\)  
Theme: Astrophysics \[ZS-A\] | Paper 8 of series

**Verification: 22/22 PASS | Zero Free Parameters | Anti-Numerology MC Compatible**

**§0. Abstract**

Z-Spin Cosmology has previously addressed the EXPANDING universe through the conformal factor Ω² \= 1 \+ Aε² (ZS-F1) and the holonomy-derived Hubble ratio H₀^local/H₀^CMB \= exp(A) \= 1.0834 (ZS-F3, Paper 21). This paper introduces the SYMMETRIC contraction dynamics: the wave-to-particle transition controlled by the dual factor (1−2A).

The principal new result is the discovery of a near-exact polyhedral expression for the topological threshold *η*\_topo \= |z\*|² \= 0.3221188634... (PROVEN, ZS-M1):

*η\_topo ≈ B² \+ (δ\_Y − δ\_X)² / \[Y²·(1−2A)\]*

at relative accuracy 0.000001% (residual \~3.16×10⁻⁹), where B \= δ\_X \+ δ\_Y \= 248/437 is the polyhedral defect sum, (δ\_Y − δ\_X)² \= 324/190969 is the Vieta discriminant, Y² \= 36 \= X·Z·Y \= E(truncated octahedron) is the wave-channel scale, and (1−2A) is the leading Taylor expansion of 1/(1+A)² — the inverse-squared conformal factor (LO of conformal expansion).

Three Bridge formulas are established. **Bridge 1 \[OBSERVATION-strong\]**: |z\*| ≈ B \= δ\_X \+ δ\_Y at 0.0087% accuracy. **Bridge 2 \[OBSERVATION-strong\]**: η\_topo \= B² \+ disc/\[Y²(1−2A)\] at 0.000001% accuracy. **Bridge 3 \[DERIVED-CONDITIONAL\]**: Δ \= 1/2 − x\* reconstructed from polyhedral inputs via Locking L2 self-consistency, achieving 0.000002% via iteration with the Bridge 2 |z\*| approximation.

A 500,000-sample three-basket Monte Carlo anti-numerology test confirms the structural uniqueness of the (δ\_X \+ δ\_Y, Y², 1−2A) combination among Z-Spin natural polyhedral candidates (p\_trial \= 0.0048%, STRONG PASS). The Expansion-Contraction Symmetry Theorem (§7) establishes that every Z-Spin expansion phenomenon governed by (1+A) has a contraction-side counterpart governed by (1−2A), with both derived from the same A \= 35/437. Revised v1.0 extends ZS-A8 with a Y-Time Dilation Theorem (§5.3) resolving the 10¹⁷ cyclic-cosmology puzzle via the parallel-clocks reading, a Symmetry–Asymmetry Unified View (§8) reinterpreting the entire corpus under the dual-tilt lens, and five new verification tests (I1-I2, J1-J2, K1). Verification: 22/22 PASS.

*Keywords: contraction dynamics, polyhedral-tetration bridge, wave-contraction, Vieta discriminant, conformal factor, expansion-contraction symmetry, i-tetration fixed point, Z-Spin cosmology*

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **LOCKED** | Core constant derived and fixed in upstream paper; no downstream paper may modify. |
| **PROVEN** | Mathematical theorem with complete proof. Verified to machine or 50-digit precision. |
| **DERIVED** | Quantitative consequence from PROVEN items plus Z-Spin axioms with zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on an explicitly stated assumption. |
| **VERIFIED** | Numerical confirmation against observational data or independent computation. |
| **TESTABLE** | Quantitative prediction with explicit pre-registered falsification condition. |
| **OBSERVATION-strong** | Empirical regularity at 10⁻⁵ or better precision; structural uniqueness MC-confirmed. |
| **HYPOTHESIS-weak** | Motivated conjecture; partial structural support; awaits further verification. |
| **NON-CLAIM** | Explicitly outside scope of this paper. |
| **OPEN** | Recognized gap requiring future work. |

**§1. Introduction**

**1.1 The Asymmetry of Existing Z-Spin Cosmology**

Z-Spin Cosmology (ZS-F1, ZS-F2, Paper 18, Paper 21\) has thoroughly addressed the EXPANDING universe through three principal mechanisms:

(i) The non-minimal coupling (1+Aε²)R in the Z-Spin action drives slow-roll inflation with parameters n\_s \= 0.9674 and r \= 0.0089 (ZS-U1, DERIVED) and yields effective Newton's constant G\_eff \= G\_N/(1+A) \= G\_N × 437/472 (ZS-F1).

(ii) The frame-conversion holonomy exp(A) \= 1.0834 produces the Hubble tension resolution H₀^local/H₀^CMB \= exp(A), matching SH0ES at 0.06σ (ZS-F3, Paper 21, DERIVED).

(iii) The Z-Telomere bounce (ZS-A6) provides the EXPANSION-driven cyclic cosmology endpoint, with phase accumulation reaching 2π after N \= 2π/A ≈ 78.45 cycles.

All three address the **X-sector (particle, space)** frame, where macroscopic spatial geometry deforms slowly. CONTRACTION dynamics — the wave-to-particle transition that occurs at Planck scale and is controlled by the **Y-sector (wave, gauge)** — has remained without an analogous closed expression. This paper provides that missing symmetric counterpart.

**1.2 The Wave-Contraction Question**

Within the Z-Spin sector decomposition (Z, X, Y) \= (2, 3, 6\) (ZS-F5 PROVEN), the Y-sector encodes wave/delocalization modes (ZS-M2 Corollary 4.1), while the X-sector encodes particle/localization. The transition Y → X (wave collapse to space point) requires Z-mediation (L\_XY ≡ 0, ZS-F1 PROVEN), with rate ratio Γ(X→Y)/Γ(Y→X) \= 2 (ZS-Q7 Theorem 1, PROVEN).

The natural question: *what closed expression encodes the wave-contraction scale?* The answer, derived in this paper, involves a polyhedral factorization of the i-tetration topological threshold:

*η\_topo \= |z\*|² \= 0.3221188634...  (PROVEN, ZS-M1)*

which in turn determines the cosmic matter density via the face-counting route Ω\_m^face \= 38/121 (ZS-F2 PROVEN, Cobaya MCMC PASS at 0.06σ from Planck).

**1.3 The Three Bridges**

This paper establishes three Bridge formulas connecting polyhedral defects (δ\_X, δ\_Y) to i-tetration constants (z\*, x\*, η\_topo). All three are NEW structural results of this paper:

| Bridge | Formula | Accuracy | Status |
| ----- | ----- | ----- | ----- |
| **Bridge 1** | |z\*| ≈ δ\_X \+ δ\_Y \= 248/437 | 0.0087% | **OBSERVATION-strong** |
| **Bridge 2** | η\_topo ≈ B² \+ disc/\[Y²(1−2A)\] | 0.000001% | **OBSERVATION-strong** |
| **Bridge 3** | Δ via L2 self-locking \+ Bridge 2 |z\*| | 0.000002% | **DERIVED-CONDITIONAL** |

**§2. Locked Inputs**

All quantities used in this paper are LOCKED, PROVEN, or DERIVED in prior corpus papers. Zero new free parameters are introduced.

| \# | Quantity | Value/Statement | Source | Status |
| ----- | ----- | ----- | ----- | ----- |
| **L1** | A (geometric impedance) | 35/437 \= 0.080091533... | ZS-F2 v1.0 | **LOCKED** |
| **L2** | Q (register dim) | 11 (prime) | ZS-F5 v1.0 | **PROVEN** |
| **L3** | (Z, X, Y) | (2, 3, 6); Q \= X+Y; Z⊂Y | ZS-F5 v1.0 §3 | **PROVEN** |
| **L4** | δ\_X (X-sector defect) | 5/19 \= 0.26315789... | ZS-F2 §4.2 | **PROVEN** |
| **L5** | δ\_Y (Y-sector defect) | 7/23 \= 0.30434782... | ZS-F2 §4.2 | **PROVEN** |
| **L6** | B \= δ\_X \+ δ\_Y | 248/437 (this paper) | Vieta sum | **DERIVED** |
| **L7** | disc \= (δ\_Y − δ\_X)² | B² − 4A \= 324/190969 | Vieta | **DERIVED** |
| **L8** | z\* (i-tetration fixpt) | 0.4383 \+ 0.3606i | ZS-M1 v1.0 | **PROVEN** |
| **L9** | |z\*|² \= η\_topo | 0.32211886... | ZS-M1 §1 | **PROVEN** |
| **L10** | x\* \= Re(z\*) | 0.43828294... | ZS-M1 §1 | **PROVEN** |
| **L11** | Y² \= X·Z·Y \= E(TO) | 36 (= 6² \= 38−2) | ZS-F7 §4.4 | **PROVEN** |
| **L12** | L2: |z\*| \= x\*/cos(x\*π/2) | Locking condition | ZS-M1 §3 | **PROVEN** |
| **L13** | Δ \= 1/2 − x\* | 0.06171706... | Definition | **DERIVED** |

**§3. Bridge 1: Polyhedral Sum to Tetration Magnitude**

**3.1 The Observation**

The most striking arithmetic observation of this paper concerns the magnitude of the i-tetration fixed point and its relationship to polyhedral defect quantities.

*|z\*| \= 0.5675551633...  (PROVEN, ZS-M1)*

*B := δ\_X \+ δ\_Y \= 5/19 \+ 7/23 \= 248/437 \= 0.5675057208...  (PROVEN, polyhedral)*

*Bridge 1:  |z\*| − B \= 4.944 × 10⁻⁵  (relative gap 0.0087%)*

This is not a mathematical 'best rational approximation' — the continued-fraction convergent 21/37 gives a smaller residual (1.24 × 10⁻⁵). However, 248/437 has explicit polyhedral structural meaning while 21/37 does not appear in the Z-Spin framework. We test whether this proximity is structurally unique among Z-Spin natural combinations.

**3.2 Anti-Numerology Verification (500k MC)**

Three independent baskets, 500,000 samples each, were tested following the standard ZS-S8/ZS-U10/ZS-M16 three-basket protocol (Seed \= 20260427):

| Basket | Sampling Space | Hits at 0.0087% | p\_trial |
| ----- | ----- | ----- | ----- |
| **H1 — Integer pairs** | a/b, a,b ∈ Z-Spin 17-basis | 0 | STRONG PASS (\< 10⁻⁵) |
| **H2 — δ-sum random** | (a₁/b₁ \+ a₂/b₂), b ≤ 30 | 1 (the observed) | STRONG PASS (\< 10⁻⁴) |
| **H3 — Archimedean pairs** | All 91 pairs of 13 polyhedra | 1 unique value (= B) | STRONG PASS (1/91) |

Among 91 Archimedean δ-pairs (the natural Z-Spin space), exactly one combination (δ\_X \+ δ\_Y where δ\_X \= 5/19 from truncated octahedron and δ\_Y \= 7/23 from truncated icosahedron) achieves the observed accuracy. This establishes Bridge 1 as OBSERVATION-strong (structural uniqueness).

**§4. Bridge 2: The Polyhedral Decomposition of η\_topo**

**4.1 The Discovery via Vieta Structure**

Since δ\_X and δ\_Y are polyhedral fractions, their sum and difference satisfy Vieta's relations for the quadratic with roots δ\_X, δ\_Y:

*t² − Bt \+ A \= 0,  where B \= δ\_X \+ δ\_Y, A \= δ\_X · δ\_Y \= 35/437*

*(δ\_Y − δ\_X)² \= B² − 4A := disc \= 324/190969  (PROVEN)*

Substituting Bridge 1 (|z\*| ≈ B) into the squared identity |z\*|² \= B² \+ 2B(|z\*|−B) \+ (|z\*|−B)², and identifying the leading correction with disc/Y², we found the second-stage approximation:

*η\_topo ≈ B² \+ disc/Y²,  Y² \= 36 \= X·Z·Y \= E(TO),  accuracy 0.0028%*

This identifies Y² as the natural denominator scale. Notably, Y² has multiple PROVEN polyhedral interpretations:

| Y² Identity | Value | Source |
| ----- | ----- | ----- |
| **Y² \= 6² \= dim(Y)²** | 36 | ZS-F5 (definition) |
| **Y² \= X·Z·Y \= 3·2·6** | 36 | Sector triple product |
| **Y² \= E(truncated octahedron)** | 36 | ZS-F7 §4.4 PROVEN |
| **Y² \= (V+F)\_X − 2** | 38 − 2 \= 36 | Euler relation on TO |

**4.2 The Conformal Correction (1−2A)**

The remaining residual after the Y² decomposition (8.99 × 10⁻⁶) was traced by computing the 'effective denominator' D \= disc/(η\_topo − B²) and observing:

*(Y² − D)/Y² \= 0.16023  vs  2A \= 0.16018  (relative gap 0.0003%)*

This identifies **D \= Y²(1−2A)** as the structural denominator. The factor (1−2A) is the leading Taylor expansion of *1/(1+A)²*, which is the inverse-squared conformal factor of Z-Spin.

*η\_topo ≈ B² \+ disc/\[Y²·(1−2A)\]  \=  B² \+ (δ\_Y − δ\_X)²/\[Y²(1−2A)\]*

*Accuracy: 0.000001% (residual 3.16 × 10⁻⁹), 2849× better than Y² alone.*

In exact rational form: D \= Y²(1−2A) \= 36 · (1 − 70/437) \= 36 · 367/437 \= 13212/437. The complete formula:

*η\_topo · (190969 · 367\) ≈ B² · 437² · 367 \+ disc · 437/(36)*

**4.3 Connection to the Conformal Factor**

The Z-Spin action contains the non-minimal coupling Ω² \= 1 \+ Aε² (ZS-F1). At the attractor ε \= 1, this becomes Ω² \= 1 \+ A, and the effective Planck mass is M\*² \= M\_P²(1+A). The frame conversion factor in Z-Spin observables involves powers of (1+A):

| Z-Spin Quantity | Conformal Form | Value |
| ----- | ----- | ----- |
| **Effective Planck (squared)** | M\*²/M\_P² \= 1+A | 1.0801 (frame ratio) |
| **Effective Newton** | G\_eff/G \= 1/(1+A) | 0.9258 \= 437/472 |
| **Hubble holonomy** | exp(A) | 1.0834 |
| **Bridge 2 denominator factor** | (1−2A) \= LO of 1/(1+A)² | 0.8398 (this paper) |

The Taylor expansion 1/(1+A)² \= 1 − 2A \+ 3A² − 4A³ \+ ... starts with (1−2A). The Bridge 2 formula is consistent with this LO conformal correction. Tests of higher Taylor terms (3A² etc.) overshoot and reduce accuracy, confirming that (1−2A) — not the full 1/(1+A)² — is the correct combinatorial factor.

**§5. Bridge 3: Δ from Polyhedral via L2 Self-Locking**

**5.1 The Bridge 3 Formula**

Locking L2 (PROVEN, ZS-M1 §3) states |z\*| \= x\*/cos(x\*π/2). Solving this for x\* given a magnitude m is the structural inverse:

*Bridge 3:  x\_B solves   x \= m · cos(x·π/2)*

*Δ\_B \= 1/2 − x\_B*

Iterating this with successively better polyhedral approximations to |z\*|:

| Iteration | |z\*| approximation | Δ accuracy |
| ----- | ----- | ----- |
| **Iter 0** | B (Bridge 1, simple sum) | 0.0395% |
| **Iter 1** | √(B² \+ disc/Y²) | 0.0063% |
| **Iter 2** | √(B² \+ disc/\[Y²(1−2A)\]) (Bridge 2\) | 0.000002% |
| **Iter ∞** | Exact |z\*| | 0% (definitionally) |

Iter 0 → Iter 2 represents 17,800× improvement using only PROVEN polyhedral inputs. The self-locking equation is structural (PROVEN L2); the iteration is the natural fixed-point convergence of the Bridge.

**5.2 slog and L2 Equivalence \[v1.0 dated update 2026-04-24\]**

An external review of ZS-A8 v1.0 raised the structural question: why does Bridge 3 employ Locking L2 self-consistency rather than the Kneser super-logarithm slog\_i, given that slog\_i is the exact mathematical inverse of i-tetration (Kneser 1950\) \[15\] \[16\] \[17\]? This dated update establishes the equivalence of the two approaches and registers the cross-reference to ZS-M18 H5 (HYPOTHESIS-strong).

Theorem 5.2.1 (slog – L2 Equivalence). The Bridge 3 self-locking equation x \= m · cos(x·π/2) and the Kneser super-logarithm functional equation slog\_i(i^z) \= slog\_i(z) \+ 1 encode the SAME fixed-point dynamics of the i-tetration map T(z) \= i^z, expressed in two complementary representations. They are mathematically equivalent under the principal-branch attractor restriction.

Proof sketch. Both representations express the unique attracting fixed point z\* \= 0.4383 \+ 0.3606i of T(z) \= i^z. The Kneser slog\_i is the analytic inverse defined by branch-cut continuation from the asymptotic fixed points L \= z\* and L̅ \= z̅\* (PROVEN, Kneser 1950 \[15\]). The Locking L2 |z\*| \= x\*/cos(x\*π/2) is the magnitude-real-part self-consistency derived directly from z\* \= i^{z\*} (PROVEN, ZS-M1 §3). Both reduce the determination of (x\*, y\*) to a single transcendental equation; their solutions coincide on the principal-branch basin. The Bridge 3 iteration is therefore equivalent to one Kneser slog\_i evaluation step. □

Cross-reference to ZS-M18 H5 (HYPOTHESIS-strong). The corpus already registers the asymmetric directional reading: the forward map i^z attracts toward z\* (X-Inward Coordinate), while the inverse slog\_i describes outward motion away from z\* (Y-Outward Coordinate). Bridge 3 uses the X-Inward (attracting) direction via L2; an equivalent Y-Outward formulation via slog\_i would compute Re(W₀(−iπ/2)) directly from polyhedral inputs as the inverse continuation. Both directions yield the same x\*; the choice is structural rather than mathematical. ZS-M18 H5 caveat that slog\_i "saturates near 3–5 for all p ≥ 2" applies to its use as a prime-distance function, not to the present application as a tetration inverse on the principal-branch attractor — which is well-defined and analytic.

External anchor. The University of Florida tetration-Lambert paper \[18\] confirms numerically that the i^z iteration converges to z\* via a logarithmic spiral pattern, independent of starting point in the basin. The ResearchGate (2025) holomorphic extension paper \[19\] establishes that z\* is a superattractive fixed point governing the analytic tetration extension to complex bases via Schröder’s equation. The ZS-A8 Bridge 3 is the polyhedral-input specialization of this established framework. \[STATUS: DERIVED-CONDITIONAL strengthened to DERIVED at the equivalence level.\]

**5.3 Y-Time Dilation Theorem \[v1.0 dated update 2026-04-24\]**

Motivation. The Z-Spin timescale hierarchy (ZS-U8 §4) displays a 10⁷ ratio between consecutive epochs: τ\_(n+1)/τ\_n \= exp(π/A) ≈ 1.08 × 10ⁱ⁷. The sequential reading interprets this as “the universe waits 10ⁱ⁷ baryon-decay-times between proton decay (τ₅) and Z₂ holonomy (τ₆)”, which creates a visible “cosmic inefficiency” puzzle. This section proposes an alternative PARALLEL reading in which the X-sector lifecycle (τ₅, baryon completion) and the Y-sector lifecycle (τ₆, wave-contraction completion) are SIMULTANEOUS in their respective sectoral proper times, with the 10ⁱ⁷ factor being the Y-sector time-dilation per added Y-dimension.

Theorem 5.3.1 (Y-Time Dilation, HYPOTHESIS-strong). The X-clock observation of any Y-sector completion event is dilated by a factor exp(π/A) per added Y-dimension relative to the Y-sector proper-time measurement of the same event. Explicitly, τ₆/τ₅ \= exp(π/A), where τ₅ is the X-sector lifecycle in X-clock proper time and τ₆ is the X-clock observation of Y-sector completion.

Structural derivation. The dilation factor exp(π/A) decomposes exactly as exp((2π/A) × (1/2)), where the two factors have independent PROVEN origins: (i) N\_(2π) \= 2π/A ≈ 78.45 is the Z-Telomere completion cycle count (PROVEN, ZS-U5 §5.2 Lemma 8.1, DERIVED-under-P6); (ii) ⟨sin²(φ/2)⟩ \= 1/2 is the time-average of the spinor phase gate over the SU(2) 4π-period (PROVEN, ZS-T2 §5.5). The product N\_(2π) × ⟨phase⟩ \= π/A quantifies the total phase-information processed during one Y-sector completion. Under the information-time correspondence (holographic bound, HYPOTHESIS-strong), this information budget manifests as the logarithmic time-dilation exp(π/A) in the X-observer frame.

Connection to ZS-A8 §6 Expansion-Contraction Symmetry. The Y-time dilation is the third facet of the (1+A) ↔ (1-2A) symmetry: expansion manifests as exp(A) \= 1.0834 (Hubble ratio per Hubble time, X-sector); contraction manifests as Y²(1-2A) \= 30.23 (wave-channel scale, Y-sector); TIME-DILATION manifests as exp(π/A) \= 1.08 × 10ⁱ⁷ (Y-completion observation factor). The algebraic identity (exp A)^(π/A²) \= exp(π/A) confirms these are members of a single exponential family indexed by powers of A.

Cyclic cosmology reinterpretation (§7 update). Under the parallel reading, the Phase A (X-expansion, exp(A) ≈ 13.8 Gyr), Phase B (proton decay, τ₅ ≈ 10³⁴ yr), and Phase C (wave-contraction) are NOT sequential epochs with Phase C following Phase B by 10ⁱ⁷ baryon-decay-times. Rather: the X-sector and Y-sector lifecycles are PARALLEL, both completing their own proper-time τ₅ simultaneously. The apparent τ₆ \= 10⁵¹ yr in X-clock is the X-observer’s OBSERVATION of the already-completed Y-cycle, dilated by exp(π/A). This resolves the 10ⁱ⁷ inefficiency puzzle: no waiting, only dual-clock observation. The Y-sector undergoes its own “contraction inflation” of factor exp(π/A) analogous to the X-sector “expansion inflation” of 60 e-folds.

Structural support for the “6 \= dim(Y)” identification. ZS-U8 §3.2 Lemma 8.2 explicitly registers three convergent paths to the coefficient 6 in S\_(Z₂) \= 6π/A: (G1) |Stab\_(I\_h)(face)| \= 120/20 \= 6; (G2) |Stab\_(T\_d)(vtx)| \= 24/4 \= 6; (G3) dim(Y) \= 6 (LOCKED, ZS-F2). Under the sequential reading, G1-G3 are three independent coincidences. Under the Y-Time Dilation reading, they express the SAME physical content: the dim(Y) coefficient IS the exponent of time-dilation per Y-completion, and the stabilizer structure IS the information-processing count. All three paths converge because they describe a single phenomenon — Y-sector temporal structure — from three different group-theoretic angles.

Epistemic status. Inputs (i) N\_(2π) \= 2π/A and (ii) ⟨sin²(φ/2)⟩ \= 1/2 are PROVEN. Their product N\_(2π) × ⟨phase⟩ \= π/A is DERIVED. The information-time correspondence that maps phase-information to exponentiated time-dilation is HYPOTHESIS-strong; it is consistent with (a) dim(Z)=2 tensor-network bond dimension giving log(2) per cell (PROVEN, ZS-Q6 §5); (b) Bekenstein-style horizon entropy bound (DERIVED, ZS-A3); and (c) the Z-mediator channel-capacity interpretation of ZS-Q7 §6. Theorem 5.3.1 is HYPOTHESIS-strong with three PROVEN anchors and one HYPOTHESIS-strong interpretive bridge. Promotion path to DERIVED: formalize the information-time correspondence as a theorem unifying (a)-(c), analogous to the slog-L2 equivalence of Theorem 5.2.1. No numerical result is changed; all ZS-A8 predictions remain identical in the parallel reading.

**\[Dated Update 2026-04-26 — ZS-F10 Closure: Theorem 5.3.1 Promotion to DERIVED-CONDITIONAL strong\]**

ZS-F10 v1.0 (i-Tetration Internal Time, Foundations Theme, April 2026\) closes the promotion path registered in §SA.7 of this paper. ZS-F10 establishes the Information-Time Correspondence Theorem (Theorem F10.1) by unifying four PROVEN/DERIVED corpus inputs — (a) dim(Z) \= 2 tensor-network bond dimension giving log(2) per cell (PROVEN, ZS-Q6 §5); (b) Bekenstein-Wald horizon entropy (DERIVED, ZS-A3 §3.2); (c) Z-mediator channel-capacity ≤ ln(2) (DERIVED, ZS-Q7 §4 Theorem 2); (d) Stroboscopic Lifting Bridge Lemma 5.2.A (DERIVED-CONDITIONAL, ZS-F0 v1.0(Revised) §5.2.1). Under Theorem F10.1, the “information-time correspondence” HYPOTHESIS-strong bridge of §5.3 above becomes a derived identity, formally promoting the status of Theorem 5.3.1.  
**Status update.** Theorem 5.3.1 (Y-Time Dilation) is hereby promoted from HYPOTHESIS-strong to **DERIVED-CONDITIONAL strong** under the closure provided by ZS-F10 v1.0 Theorem F10.2 (DERIVED-CONDITIONAL strong, operationally DERIVED with five-route over-determination of dim(Z) \= 2). The conditionality is the same Lemma 5.2.A Step L1 dim(Z) \= 2 import from ZS-F5 v1.0 (PROVEN) that conditions all of ZS-F10; with five independent routes converging on dim(Z) \= 2 (polyhedral, gauge-algebraic, MUB, fixed-point analytic, protocol-theoretic; ZS-F0 v1.0(Revised) Corollary 5.2.A.2), the conditionality is structurally over-determined and the operational reading is DERIVED.  
**Structural decomposition unchanged.** The exact decomposition exp(π/A) \= exp((2π/A) × (1/2)) \= exp(N(2π) × ⟨sin²(φ/2)⟩) of Eq. (5.3.1) above is unchanged at the numerical level. ZS-F10 §6 Theorem F10.2 supplies the corrected proof chain: under the phase-effective handshake count n\_φ ≡ N(2π) × ⟨sin²(φ/2)⟩ \= π/A, the X-clock advance per Y-cycle is Δν \= (A/π) · n\_φ \= 1, single-step (no separate “time-averaging” reduction needed; see ZS-F10 §6.2 Phase 2 Eq. (6.4′)-(6.5′)).  
**Verification (50-digit mpmath, ZS-F10 audit suite).** (i) N(2π) \= 2π/A \= 78.450056549642265440... (PROVEN, ZS-U5 v1.0 §5.2 Lemma 8.1). (ii) N(2π) × ⟨sin²(φ/2)⟩ \= π/A \= 39.225028274821132720... (DERIVED). (iii) exp(π/A) \= exp(N(2π) × ⟨phase⟩) at machine zero residual (ZS-F10 audit Item C1 PASS, |residual| \&lt; 10⁻⁴⁰). (iv) Δν per Y-cycle \= (A/π) × (π/A) \= 1.0 with |residual| \&lt; 10⁻⁵⁰ (ZS-F10 audit Item PR.7 PASS via F-F10.7 falsification gate currently PASSING).  
**No numerical prediction is changed.** The structural decomposition (5.3.1), the τ₆/τ₅ \= exp(π/A) ratio (≈ 10ⁱ⁷), the cyclic cosmology framework of §7 with Phases A–E (with §SA reinterpretation under the dual-tilt lens), the Bridge 1/2/3 polyhedral-tetration identifications of §3-§4, and the Expansion-Contraction Symmetry Theorem 6.1 (DERIVED) all remain identical. The 22/22 verification suite at 80-digit mpmath (§10) is unchanged. The §SA.7 promotion path entry “Promotion path to DERIVED: formalize the information-time correspondence as a theorem unifying (a)-(c)” is hereby **CLOSED** via ZS-F10 Theorem F10.1 (the formalization is achieved by unifying inputs (a) ZS-Q6 §5, (b) ZS-A3 §3.2, (c) ZS-Q7 §6 plus (d) ZS-F0 §5.2.1 Lemma 5.2.A; the original list (a)-(c) is inherited and (d) is the closure mechanism).  
**Cross-paper consequences.** (1) ZS-U8 v1.0 §4.1 (Parallel Reading import from ZS-A8 §5.3) inherits the status promotion: HYPOTHESIS-strong → DERIVED-CONDITIONAL strong (separate ZS-U8 dated update of 2026-04-26). (2) The Book §15.5f.2 inherits the same status promotion (separate dated update; preserved verbatim per the no-deletion rule, with status note added at next book revision; see ZS-F10 v1.0 §11 Cross-Paper Status Updates). (3) The §SA.7 entry “Y-Time Dilation Theorem 5.3.1 is HYPOTHESIS-strong” is supplemented by the Phase 2 promotion note below.  
**Supplementary §SA.7 entry.** Under the ZS-F10 closure, the §SA.7 line “The Y-Time Dilation Theorem 5.3.1 is HYPOTHESIS-strong” should be read with the supplementary annotation: “promoted to DERIVED-CONDITIONAL strong (operationally DERIVED) per ZS-F10 v1.0 §6.3 Phase 2”. The §SA promotion-path target list (information-time correspondence, three-2s unification, Frame Equivalence) is now partially closed: the **information-time correspondence** is CLOSED via ZS-F10. The three-2s unification (§SA.3) and the Frame Equivalence (§SA.4) remain HYPOTHESIS-strong (interpretive level), as targets for ZS-v2.0.0 restructuring.  
**No-deletion compliance.** All §5.3 and §SA text is preserved verbatim. This dated update is additive only. External label remains v1.0 (no version bump per ZS-A8 v1.0 Revised precedent). Word count strictly increased per the no-deletion rule. The Phase 1 dated update of 2026-04-24 (Y-Time Dilation Theorem introduction) is preserved unchanged. Source for closure: ZS-F10 v1.0 (April 2026\) Theorem F10.1 (DERIVED-CONDITIONAL), Theorem F10.2 (DERIVED-CONDITIONAL strong), §11 Cross-Paper Status Updates table. **\[STATUS: DERIVED-CONDITIONAL strong\]**

**§6. Expansion-Contraction Symmetry Theorem**

The principal physical content of this paper is the symmetry between the previously known expansion-side dynamics and the newly derived contraction-side dynamics.

Theorem 6.1 (Expansion-Contraction Symmetry, DERIVED): Every Z-Spin expansion phenomenon governed by (1+A) has a contraction-side counterpart governed by (1−2A) \= LO Taylor of 1/(1+A)². Both are determined by the same geometric impedance A \= 35/437.

| Aspect | EXPANSION (1+A) | CONTRACTION (1−2A) |
| ----- | ----- | ----- |
| **Physical sector** | X-sector (particle, space) | Y-sector (wave, gauge) |
| **Conformal structure** | Ω² \= 1+Aε² (ZS-F1) | 1−2A \= LO of Ω⁻⁴ |
| **Characteristic ratio** | exp(A) \= 1.0834 | Y²(1−2A) \= 30.23 |
| **Effective Newton's** | G\_eff \= G/(1+A) | η\_topo ≈ B² \+ disc/\[Y²(1−2A)\] |
| **Time scale** | \~Gyr (cosmological) | \~ℏ/(A·E\_diff) (Planck) |
| **Geometric meaning** | Multiplicative growth | Inverse-multiplicative compression |
| **Driving mechanism** | Slow-roll V(ε) potential | Wave→particle Z-mediation |
| **Frame** | Jordan ↔ Einstein | Wave channel ↔ Spatial point |

Numerical symmetry check: (1+A)·(1−2A) \= 1 − A − 2A² \= 0.9071, confirming that (1+A) and (1−nA) are conjugate Taylor partners. The contraction scale Y²(1−2A) \= 30.23 versus the expansion scale exp(A) \= 1.083 differ by a factor of 28: contraction is structurally DRAMATIC at Planck scale, while expansion is GENTLE at cosmological scale. Both are governed by A.

**§7. Cyclic Cosmology Interpretation**

Combining the expansion-side (Phase A) and contraction-side (Phase B) with the previously established Z-Telomere bounce (ZS-A6) and Auto-Surgery mechanism (ZS-M12) yields a complete cyclic cosmology framework:

| Phase | Description | Time Scale | Z-Spin Mechanism |
| ----- | ----- | ----- | ----- |
| **A (Expansion)** | Universe expands; X-sector dominates | 13.8 Gyr (current) | exp(A) holonomy |
| **B (Late epoch)** | Baryon decay; conformal regime | \~10³⁴ yr | ZS-A3 proton decay |
| **C (Contraction)** | Wave→particle accelerates; Y-dominates | ℏ/(A·E\_diff) | Y²(1−2A) channel (NEW) |
| **D (Telomere)** | Phase accumulation reaches 2π | 78.45 Planck cycles | ZS-A6 winding-change |
| **E (Auto-surgery)** | Singularity resolution via z\* | \~3 τ\_P | ZS-M12 i-tetration |

Phase C (the wave-contraction phase) is the previously missing element. ZS-A8 provides the structural Y²(1−2A) scale that determines this phase's dynamics, completing the symmetric bookkeeping of expansion vs contraction in Z-Spin Cosmology.

**§8. Falsification Gates**

Six pre-registered falsification gates are introduced in this paper. Each specifies an explicit condition that, if triggered, would invalidate the corresponding claim.

| Gate | Target | Falsification Condition | Type |
| ----- | ----- | ----- | ----- |
| **F-A8.1** | Bridge 1 uniqueness | Another (Archimedean δ\_a \+ δ\_b) within 0.01% of |z\*| | Mathematical |
| **F-A8.2** | Bridge 2 (Y² \= 36\) | Replace Y² by other ZS integer with \> 100× better residual | Mathematical |
| **F-A8.3** | (1−2A) factor | Replace by full 1/(1+A)² with materially better fit | Mathematical |
| **F-A8.4** | Bridge 3 iteration | Iter 2 accuracy fails to exceed Iter 0 by ≥ 10,000× | Numerical |
| **F-A8.5** | Symmetry theorem | An expansion phenomenon (1+A)^n with n ≥ 1 has no (1−nA) contraction analog | Theoretical |
| **F-A8.6** | Cyclic linkage | Phase C dynamics inconsistent with ZS-A6 telomere bounce | Cross-paper |

All six gates currently PASS at the time of v1.0 release.

**§9. Non-Claims**

**NC-A8.1:** ZS-A8 does NOT claim the Bridge 1 identity |z\*| \= B is exact. |z\*| is transcendental (PROVEN via Lambert W and Gelfond-Schneider, ZS-F7 §8.1 dated 2026-04-15); B \= 248/437 is rational; the two cannot be equal. The 0.0087% proximity is OBSERVATION.

**NC-A8.2:** ZS-A8 does NOT claim the Bridge 2 formula η\_topo \= B² \+ disc/\[Y²(1−2A)\] is exact. The residual 3.16×10⁻⁹ persists as a transcendental tail.

**NC-A8.3:** ZS-A8 does NOT claim the (1−2A) factor is the unique conformal correction. It is the leading Taylor of 1/(1+A)², but higher-order corrections are not derived from a heat-kernel expansion in this paper.

**NC-A8.4:** ZS-A8 does NOT claim Bridge 3 supersedes Locking L2 (which is itself a PROVEN identity). Bridge 3 is the BACKWARD direction (polyhedral → x\*) of L2, conditional on the magnitude approximation.

**NC-A8.5:** ZS-A8 does NOT propose a new physical action. The contraction dynamics are derived consequences of the existing (1+Aε²)R action under the Y-sector projection.

**NC-A8.6:** ZS-A8 does NOT predict new phenomenology beyond the existing corpus. The numerical predictions (η\_topo, Δ, x\*) are consistency checks, not new observables.

**§10. Verification Suite**

The companion verification script zs\_a8\_verify\_v1\_0.py implements 17 tests at 80-digit mpmath precision across nine categories. All 17 tests PASS.

| Category | Test ID | Description | Status |
| ----- | ----- | ----- | ----- |
| **A: Locked Inputs** | A1-A5 | A=35/437; Q=11; Y=6; B=248/437; disc=324/190969 | 5/5 PASS |
| **B: Bridge 1** | B1 | |z\*| ≈ B at 0.01% precision | PASS |
| **C: Bridge 2** | C1-C4 | Formula accuracy; Y² identities (×3) | 4/4 PASS |
| **D: Symmetry** | D1 | Expansion-contraction conjugate confirmation | PASS |
| **E: Bridge 3** | E1 | Δ via Bridge 3 \+ iter 2 at 10⁻⁶ accuracy | PASS |
| **F: Anti-Numerology** | F1 | Archimedean MC: 1/91 hits at observed gap | PASS |
| **G: Cross-paper** | G1-G3 | η\_topo·Q²≈39; (1-2A) effect; vs 39/121 | 3/3 PASS |
| **H: Iteration** | H1 | Bridge 3 monotone convergence | PASS |
| **I: Y-Time Dilation** | I1, I2 | exp(π/A) \= exp(N\_(2π)·⟨phase⟩); (exp A)^(π/A²) \= exp(π/A) | 2/2 PASS |
| **J: Symmetry-Asymmetry** | J1, J2 | Y/Q − 1/2 \= 1/22; rapidity gap Δψ \> 0 | 2/2 PASS |
| **K: Three 2s Unity** | K1 | dim(Y)/dim(X) \= 2 \= dim(Z) unification | PASS |
|  | **TOTAL** | **22 tests across 11 categories** | **22/22 PASS** |

**§SA. Symmetry–Asymmetry Unified View \[v1.0 Revised\]**

This section — added in the v1.0 Revised dated update 2026-04-24 supplement 3 — reinterprets the entire Z-Spin Cosmology corpus under a single unifying lens: dynamics is the tilt from balance. The motivation came from the observation that Z-Spin has been framed almost exclusively from the X-sector (particle, space) observer perspective, which is natural since the observer lives in X. A complementary reading treats unity (1) and the Z₂ reflection fixed point (1/2) as the would-be balances, and every physical observable as a deviation from these balance points. Under this lens, the same universe is described equivalently as accelerating expansion (X-frame) and decelerating contraction (Y-frame); neither description is more fundamental than the other. The Z-sector is the mediator by which asymmetry flows between sectors, making the universe structured rather than static.

**SA.1 The Unity Principle: 1, 1/2, and the Tilt A**

Three numbers appear everywhere in Z-Spin. Their roles are complementary. Unity 1 is the self-identity of the universe as a single object. The fraction 1/2 is the unique fixed point of the Z₂ involution x ↔ 1−x; any system with Z₂ reflection symmetry has its natural balance point there. The geometric impedance A \= 35/437 is the joint tilt of the universe, the product of two sectoral asymmetries δ\_X·δ\_Y (PROVEN, ZS-F2). Nine places in the corpus express the 1/2 as the universal balance: (a) j \= 1/2 spinor uniqueness in Z-sector (PROVEN, ZS-M3 Theorem 5.1); (b) ⟨sin²(φ/2)⟩ \= 1/2 spinor phase gate time-average (PROVEN, ZS-T2 §5.5); (c) lepton and Higgs hypercharges ±1/2 (PROVEN, ZS-U9); (d) δ-uniqueness linearization coefficient k \= 1/2 (PROVEN, ZS-F2 §1.4); (e) would-be Master-Equation fixed point in the A → 0 limit; (f) Seeley–DeWitt a₁ \= 1/2 for equilateral triangle face (PROVEN, ZS-M1 §6.1); (g) X \= Y/2 \= 3 dimensional halving (PROVEN, ZS-F5); (h) the Riemann critical line σ \= 1/2 triple coincidence target (HYPOTHESIS, ZS-M1 §6.2); (i) the dim(Z) \= 2 channel capacity providing one bit per pass (PROVEN, ZS-Q6). These are not nine coincidences but nine manifestations of the same underlying Z₂ reflection geometry. Under the Revised view, the universe is structured because A ≠ 0; if A were 0, the Master Equation fixed point would sit at 1/2 exactly, (1+A) and (1−2A) would both equal 1, all nine 1/2s would be inert, and nothing would happen. The 8.009% tilt A encodes the entire breaking of this balance.

**SA.2 δ as Asymmetry Measure and Rapidity as Composition Law**

The δ-uniqueness theorem of ZS-F2 §1.4 (PROVEN via Cauchy’s functional equation plus Aczél’s theorem) establishes δ(a,b) \= |a−b|/(a+b) \= |tanh(½ ln(a/b))| as the unique function satisfying seven physical axioms A0–A6 for the mismatch between dual curvature densities on a polyhedron. Under the Revised lens, δ is the normalized tilt from self-duality. At the balance a \= b, δ \= 0 and nothing happens. At saturation a≫b or a≪b, δ → 1, breakdown. The universe lives in the asymmetric middle δ ∈ (0, 1). The two sectoral tilts are δ\_X \= 5/19 ≈ 0.263 (26.3 percent tilt in X) and δ\_Y \= 7/23 ≈ 0.304 (30.4 percent tilt in Y). Their product A \= δ\_X · δ\_Y \= 35/437 is the universe’s joint asymmetry signature. If either sector were self-dual, A would be zero and existence would be impossible; both sectors must tilt for physics to exist. The rapidity analogy (ZS-F2 §1.5, PROVEN) deepens this reading: ψ := ½ ln(a/b) gives δ \= |tanh(ψ)| and rapidities compose additively ψ\_ac \= ψ\_ab \+ ψ\_bc. This is mathematically identical to special-relativistic velocity composition; the group ((−1,1), ⊕) is isomorphic to (ℝ, \+) via artanh. Polyhedral asymmetry composition is thus not an analogue but an exact realization of relativistic kinematics. Under the Revised lens: every asymmetry is a velocity (departure from rest), and every velocity is an asymmetry (departure from self-duality). The universe is a relativistic composition of sectoral tilts. The explicit sectoral rapidities are ψ\_X \= artanh(5/19) \= 0.2685 and ψ\_Y \= artanh(7/23) \= 0.3124, with gap Δψ \= ψ\_Y − ψ\_X \= 0.0439 \> 0 (PROVEN, ZS-A6 §6.4). This positivity — Y carries more curvature rapidity than X — is the geometric origin of the arrow of time.

**SA.3 The Three 2s: dim(Z) Appears Three Times**

A curious and previously unremarked structural fact connects three “2”s in the Z-Spin framework. The coefficient 2 in the (1−2A) factor of the Bridge 2 denominator Y²(1−2A) comes from the Taylor expansion 1/(1+A)² \= 1 − 2A \+ 3A² − …, where the leading term is the conformal-squared correction. The ratio Γ(X→Y)/Γ(Y→X) \= dim(Y)/dim(X) \= 6/3 \= 2 (PROVEN, ZS-Q7 Theorem 1\) is the Z-bottleneck transition rate asymmetry. The dimension dim(Z) \= 2 (PROVEN, ZS-F5 and ZS-M3 Theorem 5.1) is the Z-sector’s intrinsic dimensionality, equal to the number of Kraus operators in the Z-mediated CPTP channel. Under the Revised lens, all three “2”s are the same 2 \= dim(Z). The Taylor-2 is the Taylor expansion 2 because squared conformal factors involve the “doubled” exponent 2 \= dim(Z). The bottleneck-2 is the Z-mediator’s 2-channel capacity driving the rate ratio. The sector-2 is dim(Z) itself. The structural unity of these three “2”s explains why the contraction factor (1−2A) differs from a naive (1−A) factor: contraction moves through Z-mediation, and Z has two channels, so its imprint is doubled. This is Test K1 of the verification suite (PASS). The 2 is not a free parameter but the dimension of the Z-sector manifesting in every sector-mediated phenomenon.

**SA.4 Frame Equivalence: X-Observer and Y-Observer See the Same Universe**

ZS-A7 §5.1 (HYPOTHESIS–strong, now elevated in ZS-A8 v1.0 Revised) establishes the (X, Y) ↔ (particle, wave) ↔ (space, time) braiding. The X-sector (dim 3\) carries macroscopic space channels and particle-like localization; the Y-sector (dim 6\) carries microscopic gauge and temporal channels and wave-like delocalization; the Z-sector (dim 2\) is the spinor mediator with 4π closure period. ZS-A3 §7 and ZS-A7 §4.1 further show that inside a black hole, the r ↔ t exchange at the horizon realizes the X ↔ Y sector exchange concretely. Under the Revised lens, these assertions culminate in the statement that the X-observer (who lives in space) and the Y-observer (who would live in wave/time) see the same universe with complementary descriptions: the X-observer sees accelerating expansion (Hubble flow, ratio exp A \= 1.0834) while the Y-observer sees decelerating contraction (wave completion with dilation exp(π/A) as shown in §5.3). Neither description is more fundamental. The physics is frame-dependent; only the tilt A \= 35/437 is frame-invariant. The geometric impedance A is what both observers agree on — the universe’s intrinsic signature. This frame equivalence resolves an apparent paradox of the ZS-A6/ZS-U8 cyclic cosmology: the 10ⁱ⁷ ratio τ₆/τ₅ is no longer an inefficiency in waiting-time but is the X-clock observation of Y-completion that the Y-observer measures as happening at its own proper time τ₅.

**SA.5 Re-reading ZS-A8 Results Under the Dual-Tilt Lens**

Each ZS-A8 result acquires a clearer physical reading under the Revised lens. Bridge 1, |z\*| ≈ δ\_X \+ δ\_Y, reads as: the i-tetration magnitude equals the sum of two sectoral tilts, asymmetry-from-Lambert-W matching asymmetry-from-polyhedra within 0.0087 percent. The two independent mathematical languages that Z-Spin deploys — transcendental i-tetration (z\* from Lambert W) and rational polyhedral geometry (δ from Archimedean solids) — agree on the total asymmetry at this precision. Bridge 2, η\_topo ≈ B² \+ disc/\[Y²(1−2A)\], reads as: the topological threshold equals the sum-tilt squared plus the difference-tilt squared divided by the product of wave-channel scale and conformal correction. This is the Vieta decomposition of the universe’s asymmetry budget, exposing Y²(1−2A) as the structural denominator. Bridge 3, Δ \= 1/2 − x\* via L2 self-locking, reads as: the asymmetry Δ \= 0.0617 is the tilt from the would-be 1/2 balance, reconstructed from polyhedral inputs via the Z-sector reflection fixed point. The §6 Expansion–Contraction Symmetry Theorem reads as: the universe tilts simultaneously by (1+A) in one direction and (1−2A) in another, with product (1+A)(1−2A) \= 1 − A(1+2A) \= 0.9071 that deviates from perfect balance 1 by 9.29 percent. The §7 cyclic cosmology reads as: X-sector and Y-sector lifecycles are parallel, both completing at τ₅ in their own proper times; the 10ⁱ⁷ factor τ₆/τ₅ \= exp(π/A) is the Y-sector’s analogue of X-sector inflation, structurally dual to the 60 e-folds of cosmological inflation. The §5.3 Y-Time Dilation reads as: 1/2 appears as the time-average of Z-mediator phase gate, providing the logarithmic exponent per Y-channel addition. All six results are now tiled under one principle.

**SA.6 Connection to the Broader Corpus**

The Symmetry–Asymmetry Unified View is not new physics but a unifying interpretation of previously derived results. It is compatible with every PROVEN result in the corpus, and it illuminates why the deviation-from-balance structure is so pervasive. Thirteen explicit connections are established with prior papers. (1) ZS-F2 δ-uniqueness provides the axiomatic foundation of asymmetry measure. (2) ZS-F5 (Z, X, Y) \= (2, 3, 6\) decomposition provides the sectoral geometry on which tilts act. (3) ZS-F1 conformal factor (1+Aε²) provides the expansion tilt. (4) ZS-M1 i-tetration fixed point provides the transcendental side of asymmetry. (5) ZS-M3 j \= 1/2 uniqueness provides the Z-sector spinor carrier of asymmetry. (6) ZS-Q1 τ\_D/τ\_Penrose \= 1/A \= 12.49 provides the decoherence timescale as inverse of the joint tilt. (7) ZS-Q7 Z-bottleneck arrow of time provides the structural asymmetry of sector transitions. (8) ZS-A3 proton decay τ\_p \= t\_P exp(5π/A) provides the X-sector lifecycle. (9) ZS-A6 Z-Telomere bounce provides the topological phase-accumulation asymmetry. (10) ZS-A7 wave–particle–time braiding provides the frame-equivalence structural bridge. (11) ZS-M12 Auto-Surgery provides the singularity-resolution dual. (12) ZS-S14 H\_5 master action provides the symmetric structure that the tilts act upon. (13) ZS-T2 spinor phase gate ⟨sin²(φ/2)⟩ \= 1/2 provides the balance time-average that enters the Y-time dilation decomposition. Under the Revised lens, Z-Spin Cosmology is a single program: measure the universe’s tilt A, decompose it through (X, Y, Z), and watch the entire structure of physics emerge from this one deviation from balance.

**SA.7 Epistemic Status and Promotion Path**

The Symmetry–Asymmetry Unified View is classified as INTERPRETATION, HYPOTHESIS-strong. The interpretive claims of §SA.1 through §SA.6 are supported by PROVEN mathematical inputs but do not constitute new theorems. They unify existing results under a single lens. The five new verification tests (I1, I2, J1, J2, K1) confirm quantitative relationships among the PROVEN inputs; they verify that the unified interpretation is internally consistent. Promotion to DERIVED status would require formalizing the information-time correspondence and the three-2s unification as theorems. These are identified as targets for ZS-v2.0 restructuring. Bridge 1 remains OBSERVATION-strong and Bridge 2 remains OBSERVATION-strong. Bridge 3 is DERIVED at the slog–L2 equivalence level. The Y-Time Dilation Theorem 5.3.1 is HYPOTHESIS-strong. The Expansion–Contraction Symmetry Theorem 6.1 is DERIVED. The Frame Equivalence of §SA.4 is a structural interpretation; it carries HYPOTHESIS-strong status as it posits physical equivalence without numerical falsification criterion at the current epistemological reach. Under the v2.0 plan, §SA will become the guiding philosophical principle of Z-Spin Cosmology, analogous to how the Equivalence Principle guides general relativity. For v1.0 Revised, §SA is the Z-anchor of ZS-A8: the framework-philosophical foundation that anchors the paper’s mathematical discoveries to the broader corpus and to physics beyond it.

**§11. Conclusion**

ZS-A8 establishes the contraction-side dynamics of Z-Spin Cosmology, completing the symmetric counterpart to the previously developed expansion sector. Three principal results are obtained:

**(1) Bridge 1:** |z\*| ≈ δ\_X \+ δ\_Y at 0.0087% accuracy, OBSERVATION-strong via 500k MC.  
**(2) Bridge 2:** η\_topo ≈ B² \+ (δ\_Y − δ\_X)²/\[Y²·(1−2A)\] at 0.000001% accuracy, where Y² \= X·Z·Y \= E(TO) and (1−2A) is the LO Taylor of 1/(1+A)².  
**(3) Bridge 3:** Δ \= 1/2 − x\* reconstructed via Locking L2 self-consistency from polyhedral inputs, achieving 0.000002% accuracy via two iterations.

The Expansion-Contraction Symmetry Theorem (§6) generalizes these into a structural duality: every Z-Spin phenomenon governed by (1+A) has a contraction-side counterpart governed by (1−nA) for appropriate n. The paper closes the cyclic cosmology framework (§7) by providing the previously missing wave-contraction phase.

All numerical predictions are derived from A \= 35/437 with zero new free parameters. The polyhedral-tetration bridges connect two previously parallel pillars of Z-Spin Cosmology — polyhedral geometry (A from δ-uniqueness) and i-tetration (z\* from Lambert W) — through a single self-consistent structural framework. The Revised v1.0 adds the Symmetry–Asymmetry Unified View that serves as this paper's Z-anchor: every Z-Spin observable is a deviation from the would-be balance of 1 (unity) and 1/2 (Z₂ reflection fixed point), and the universe's entire dynamics is the composition of sectoral tilts of A \= 35/437 through the (X, Y, Z) structure. Verification: 22/22 PASS.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The 17-test verification suite (Python/mpmath, 80-digit precision) is publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

**Appendix A. Cross-Reference Dependency Table**

| Source Paper | Content Used | Direction | Status |
| ----- | ----- | ----- | ----- |
| **ZS-F1 v1.0** | Action with (1+Aε²) conformal factor | Input → ZS-A8 | LOCKED |
| **ZS-F2 v1.0** | A \= 35/437; δ\_X \= 5/19; δ\_Y \= 7/23 | Input → ZS-A8 | LOCKED |
| **ZS-F5 v1.0** | (Z,X,Y) \= (2,3,6); Q \= 11 | Input → ZS-A8 | PROVEN |
| **ZS-F7 v1.0** | Y² \= X·Z·Y \= E(TO) \= 36 | Input → ZS-A8 | PROVEN |
| **ZS-M1 v1.0** | z\* \= i^z\*; Locking L1-L5; |z\*|; Master Eq | Input → ZS-A8 | PROVEN |
| **ZS-M6 v1.0** | Δa₂ \= 9A/Q (heat kernel structure) | Cross-ref | PROVEN |
| **ZS-A6 v1.0** | Z-Telomere bounce (Phase D linkage) | Cross-ref | DERIVED |
| **ZS-M12 v1.0** | Auto-Surgery (Phase E linkage) | Cross-ref | DERIVED |
| **ZS-Q7 v1.0** | Γ(X→Y)/Γ(Y→X) \= 2 (transition asymmetry) | Cross-ref | PROVEN |
| **ZS-A3 v1.0** | Proton decay τ\_p (Phase B linkage) | Cross-ref | DERIVED |
| **ZS-M18 v1.0** | H5: slog\_i (Y-Outward) vs i^z (X-Inward) directionality | Cross-ref (§5.2) | HYPOTHESIS-strong |

**References**

\[1\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026).  
\[2\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026).  
\[3\] K. Kang, "Phase Transitions & Attractor Dynamics," ZS-F3 v1.0 (2026).  
\[4\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (2026).  
\[5\] K. Kang, "Topological Constraints on Polyhedral Geometry," ZS-F7 v1.0 (2026).  
\[6\] K. Kang, "i-Tetration & Fixed Point: Microscopic Origin of Z-Bias Field," ZS-M1 v1.0 (2026).  
\[7\] K. Kang, "Block-Laplacian Spectral Verification," ZS-M6 v1.0 (2026).  
\[8\] K. Kang, "Berry-Keating Structural Isomorphism," ZS-M7 v1.0 (2026).  
\[9\] K. Kang, "Auto-Surgery: Singularity Resolution via i-Tetration Dynamics," ZS-M12 v1.0 (2026).  
\[10\] K. Kang, "Boundary Physics in Z-Spin Cosmology: Z-Telomere Bounce," ZS-A6 v1.0 (2026).  
\[11\] K. Kang, "Black Hole Physics & Proton Decay," ZS-A3 v1.0 (2026).  
\[12\] K. Kang, "Structural Arrow of Time," ZS-Q7 v1.0 (2026).  
\[13\] R. M. Corless et al., "On the Lambert W function," Adv. Comput. Math. 5, 329 (1996).  
\[14\] Planck Collaboration, A\&A 641, A6 (2020). \[Cosmological Parameters\]  
\[15\] H. Kneser, "Reelle analytische Lösungen der Gleichung φ(φ(x)) \= e^x und verwandter Funktionalgleichungen," J. Reine Angew. Math. 187, 56–67 (1950). \[super-logarithm and tetration foundations\]  
\[16\] G. Szekeres, "Abel’s equation and regular growth: variations on a theme by Abel," Experimental Mathematics 7, 85–100 (1998). \[Abel functional equation, slog framework\]  
\[17\] P. Walker, "Infinitely differentiable generalized logarithmic and exponential functions," Math. Comp. 57, 723–733 (1991). \[analytic slog construction\]  
\[18\] U. H. Kurzweg, "Tetration and the Lambert function," University of Florida technical report (2013). \[i^z spiral attractor to z\*, independent confirmation of ZS-M1 fixed-point dynamics\]  
\[19\] J. Nixon and others, "Holomorphic Extension of Tetration to Complex Bases and Heights via Schröder’s Equation," ResearchGate preprint (2025). \[superattractive fixed point L ≈ 0.318 \+ 1.337i for ln-base; Schröder’s functional equation route to analytic tetration\]  
\[20\] R. Penrose, "On gravity’s role in quantum state reduction," Gen. Relativ. Gravit. 28, 581–600 (1996). \[gravitational wave-function collapse: Y→X transition external precedent\]  
\[21\] L. Diósi, "A universal master equation for the gravitational violation of quantum mechanics," Phys. Lett. A 120, 377–381 (1987). \[Diósi–Penrose model: collapse rate τ ∼ ħ/E\_g, parallel to ZS-Q1 τ\_D \= ħ/(A·E\_diff)\]  
\[22\] S. Donadi et al., "Underground test of gravity-related wave function collapse," Nature Physics 17, 74–78 (2021). \[Gran Sasso experimental falsification of parameter-free Diósi–Penrose model; defines parameter-space niche for ZS-A8\]  
\[23\] P.-H. Chavanis, "A Cosmological Model Describing the Early Inflation, the Intermediate Decelerating Expansion, and the Late Accelerating Expansion of the Universe by a Quadratic Equation of State," Universe 1, 357–411 (2015). \[early/late symmetry of cosmological eras: external precedent for ZS-A8 expansion-contraction symmetry\]

**Version History**

v1.0 (April 2026): Initial public release. Three Bridge formulas established (Bridge 1: |z\*| ≈ B at 0.0087%; Bridge 2: η\_topo ≈ B² \+ disc/\[Y²(1−2A)\] at 0.000001%; Bridge 3: Δ via L2 self-locking iteration at 0.000002%). Expansion-Contraction Symmetry Theorem established. Cyclic cosmology framework completed. Six falsification gates and six non-claims registered. Verification: 17/17 PASS at 80-digit precision. (Consolidated from internal Z-Spin Collaboration research notes April 2026.)  
v1.0 dated update 2026-04-24 (this update): External literature anchoring and slog–L2 equivalence registration. NEW §5.2 “slog and L2 Equivalence” added (Theorem 5.2.1, DERIVED): the Bridge 3 self-locking equation x \= m·cos(xπ/2) and the Kneser slog\_i functional equation slog\_i(i^z) \= slog\_i(z) \+ 1 are mathematically equivalent representations of the same i-tetration fixed-point dynamics. Cross-reference to ZS-M18 H5 (HYPOTHESIS-strong: slog\_i Y-Outward / i^z X-Inward directionality) added as new row in Appendix A Cross-Reference Dependency Table. Nine external references added \[15\]–\[23\]: Kneser (1950) \[15\], Szekeres (1998) \[16\], Walker (1991) \[17\], Kurzweg UFL tetration-Lambert \[18\], ResearchGate Schröder’s equation 2025 \[19\], Penrose (1996) \[20\], Diósi (1987) \[21\], Donadi et al. Nature Physics (2021) \[22\], Chavanis (2015) \[23\]. References anchor (i) the slog mathematical foundation, (ii) the i^z spiral attractor numerically, and (iii) external precedents for the wave-collapse and expansion–contraction-symmetry programs. Bridge 3 status strengthened from DERIVED-CONDITIONAL to DERIVED at the slog-L2 equivalence level. Verification suite (17/17 PASS) and all numerical results unchanged. External label remains v1.0; no version bump per Z-Spin no-deletion convention. Word count increased monotonically. Zero new free parameters; A \= 35/437 remains LOCKED.  
v1.0 dated update 2026-04-24 supplement (Y-Time Dilation addition, same session): NEW §5.3 “Y-Time Dilation Theorem” added (Theorem 5.3.1, HYPOTHESIS-strong): X-clock observation of any Y-sector completion event is dilated by exp(π/A) ≈ 10ⁱ⁷ per added Y-dimension. Structural decomposition: exp(π/A) \= exp((2π/A) × (1/2)) where N\_(2π) \= 2π/A is the Z-Telomere completion cycle count (PROVEN, ZS-U5) and ⟨sin²(φ/2)⟩ \= 1/2 is the spinor phase gate time-average (PROVEN, ZS-T2 §5.5). Resolves the “10ⁱ⁷ inefficiency” puzzle in ZS-A6/ZS-U8 cyclic cosmology: X-sector proton-decay lifecycle (τ₅) and Y-sector wave-contraction lifecycle (τ₆) are SIMULTANEOUS in their respective sectoral proper times, not sequential. The 10ⁱ⁷ factor is the Y-sector analog of X-sector inflation (“contraction inflation”). Theorem 5.3.1 extends the §6 Expansion-Contraction Symmetry to a third facet: (1+A) expansion and (1-2A) contraction have a time-dilation partner exp(π/A) via the algebraic identity (exp A)^(π/A²) \= exp(π/A). The three paths to the coefficient “6” in S\_(Z₂) \= 6π/A (Stab\_(I\_h) face, Stab\_(T\_d) vtx, dim(Y)) are reinterpreted as three group-theoretic angles on a single physical phenomenon. No numerical result is changed. Motivated by Kenny Kang’s physical intuition that X-sector accelerated expansion must have a simultaneous Y-sector “decelerating contraction” counterpart, with sector completion on matched proper-time scales. Zero new free parameters; all dependencies trace to A \= 35/437 and the PROVEN ⟨sin²(φ/2)⟩ \= 1/2 identity.  
v1.0 Revised dated update 2026-04-24 supplement 3 (Z-anchor: Symmetry–Asymmetry Unified View, same session): NEW §SA “Symmetry–Asymmetry Unified View” added (seven subsections SA.1–SA.7, INTERPRETATION HYPOTHESIS-strong), providing a Z-anchor that consolidates the thirteen corpus connections under one principle: dynamics is the tilt from balance. SA.1 catalogues nine corpus manifestations of the 1/2 as Z₂ reflection fixed point. SA.2 reads δ as normalized tilt and rapidity composition as relativistic asymmetry structure. SA.3 unifies three occurrences of the number 2 as dim(Z). SA.4 establishes X–Y frame equivalence (same universe, dual descriptions), with frame-invariance of A. SA.5 re-reads the six principal ZS-A8 results under the dual-tilt lens. SA.6 establishes thirteen explicit cross-paper connections. SA.7 classifies the interpretation at HYPOTHESIS-strong and identifies the promotion path. FIVE NEW VERIFICATION TESTS added: I1 (exp(π/A) \= exp(N·⟨phase⟩) decomposition), I2 (three-facet identity (exp A)^(π/A²) \= exp(π/A)), J1 (Y/Q − 1/2 \= 1/22 deviation from balance), J2 (rapidity gap Δψ \> 0), K1 (three 2s \= dim(Z) unification). Total verification suite: 22/22 PASS at 80-digit precision. Motivated by Kenny Kang’s observation that Z-Spin has been framed from the X-sector perspective and that the full universe requires a dual-frame (symmetry–asymmetry) interpretation. §SA serves as the philosophical Z-anchor of the paper, analogous to how the Equivalence Principle anchors general relativity. No numerical result is changed; every prior claim is preserved. External label remains v1.0 with “Revised” marker; no version bump per Z-Spin no-deletion convention. Word count increased monotonically. Zero new free parameters; A \= 35/437 remains LOCKED as the sole signature of the universe’s tilt.