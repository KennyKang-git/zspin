**ZS-U8**

**Cyclic Holonomy and Z₂ Vacuum Transition**  
**in Z-Spin Cosmology**

Kenny Kang

**Version 1.0** — March 2026  
Theme: Early Universe \[ZS-U\] | Paper 8 of 8

**Verification: 60/60 PASS | Zero New Fit Parameters**

**§0. Abstract**

This paper establishes the complete cyclic cosmological scenario in Z-Spin Cosmology: the Z₂-degenerate vacuum structure mandating identical inflation in both ε \= \+1 and ε \= −1 sectors, the D₃ holonomy group determining the Z₂ transition action S\_Z₂ \= 6π/A, and the ε-field dynamics governing the transition mechanism.

The core result is a pre-registered, parameter-free timescale hierarchy: τ₅ \= t\_P × exp(5π/A) ≈ 2.56×10³⁴ yr (proton-decay epoch, n=5 from |I\_h/T\_d|) and τ₆ \= t\_P × exp(6π/A) ≈ 2.78×10⁵¹ yr (Z₂ holonomy transition, n=6 from |Stab\_{T\_d}(v)| \= |D₃|). The mirror universe sector (ε \= −1) is proven observationally identical to the current sector: V\_E(−ε) ≡ V\_E(+ε) is an exact algebraic identity.

The decisive near-term test is the tensor-to-scalar ratio: r \= 0.00890, which is 2.7× the Starobinsky prediction and distinguishable at \~6σ by LiteBIRD (early 2030s).

**Keywords:** cyclic cosmology, Z₂ vacuum transition, Coleman-de Luccia, D₃ holonomy, Regge calculus, mirror cosmology, tensor-to-scalar ratio, Z-Spin cosmology

**§0.1 Epistemic Status Legend**

| Status | Definition |
| :---: | ----- |
| PROVEN | Exact mathematical result, verified analytically or to machine precision. |
| DERIVED | Follows from locked inputs (A \= 35/437) with no free parameters. |
| DERIVED-CONDITIONAL | Follows from locked inputs conditional on a stated hypothesis. |
| HYPOTHESIS | Well-motivated conjecture with specified falsification condition. |
| VERIFIED | Numerical computation confirms analytical claim to stated precision. |
| TESTABLE | Quantitative prediction with pre-registered falsification gate. |
| NON-CLAIM | Explicitly excluded claim; paper scope boundary. |

**§1. Introduction**

Z-Spin Cosmology is built on a single geometric constant **A \= 35/437**, derived from the polyhedral impedance between the Z-sector (dim 2), X-sector (dim 3), and Y-sector (dim 6\) of the Q \= 11 slot register (ZS-F2 v1.0). The scalar-tensor action:

*S\[g, Φ\] \= ∫d⁴x √(−g) \[½M²\_P(1 \+ A|Φ|²)R − ½M²\_P|∂Φ|² − V(Φ)\] \+ S\_m     (1)*

with V(Φ) \= (λ\_vac/4)M⁴\_P(|Φ|² − 1)², λ\_vac \= 2A² (ZS-U5 v1.0 §8), possesses a Z₂-symmetric double-well potential: V\_E(+1) \= V\_E(−1) \= 0 exactly \[PROVEN\]. This paper addresses three questions: (Q1) Why is standard CdL tunneling forbidden? (Q2) What group-theoretic structure gives S\_Z₂ \= 6π/A? (Q3) What stabilizes ε \= \+1 between τ₅ and τ₆?

**§2. Z₂-Degenerate Vacuum and Coleman-de Luccia Analysis**

**2.1 Locked Inputs**

**Table 1\. Locked constants.**

| Constant | Value | Source |
| ----- | :---: | ----- |
| A | 35/437 \= 0.080092 | ZS-F2 v1.0 \[LOCKED\] |
| λ\_vac | 2A² \= 0.012829 | ZS-U5 v1.0 §8 \[DERIVED-COND\] |
| K(ε) | (1+Aε²)⁻¹ \+ 6A²ε²(1+Aε²)⁻² | ZS-F1 v1.0 §3 \[DERIVED\] |
| V\_E(ε) | (λ\_vac/4)(ε²−1)² / (1+Aε²)² | ZS-F1 v1.0 §3 \[DERIVED\] |

**2.2 V\_E Symmetry: Exact Z₂ Identity \[PROVEN\]**

**Claim:** V\_E(−ε) ≡ V\_E(+ε) for all ε ∈ ℝ. Proof: V\_E(ε) \= (λ\_vac/4)(ε²−1)²/(1+Aε²)². Both (ε²−1)² and (1+Aε²)² depend only on ε² (even functions). Therefore V\_E(−ε) \= V\_E(+ε) exactly. □ Corollaries: (C1) V\_E(+1) \= V\_E(−1) \= 0 exactly. (C2) V\_E(0) \= λ\_vac/4 \= A²/2 \> 0 (barrier). (C3) All CMB observables are Z₂-symmetric.

*\[STATUS: PROVEN\] Algebraic identity.*

**2.3 Coleman-de Luccia: S → ∞ \[PROVEN\]**

Standard CdL action: S\_CdL \= 27π²σ⁴ / (2ΔV³). Here ΔV \= V\_E(+1) − V\_E(−1) \= 0 exactly. Therefore S\_Coleman → ∞. Tunneling probability P \= exp(−∞) \= 0\. CdL mechanism strictly forbidden.

*\[STATUS: PROVEN\] ΔV \= 0 is exact (C1).*

**2.4 Hawking-Moss Action \[DERIVED\]**

S\_HM ≈ 5.7×10¹²³ (from locked constants). S\_HM ≫ S\_Z₂ \= 6π/A ≈ 235\. The Hawking-Moss tunneling via the hilltop (ε \= 0\) requires an exponentially suppressed probability P \= exp(−S\_HM) ≈ exp(−5.7×10¹²³), which is effectively zero. The Z-Telomere mechanism, with its much smaller action S\_Z₂ ≈ 235, is the only physically viable route for the Z₂ vacuum transition.

**§3. Z-Telomere Extension: S\_Z₂ \= 6π/A via D₃ Holonomy**

**3.0a P6 Primitive Locality Theorem \[PROVEN\]**

**Theorem P6\*:** Primitive Regge cells admit only diagonal involutions (P=I), yielding κ=4 uniquely. The group-theoretic core is verified: 10/10 involutions of SU(2) rank-4 representation, κ\_ladder census {0:1, 4:3, 6:6} confirmed. For primitive cells with P6 bridge (κ ≤ r \= 4): exactly 3 diagonal involutions with κ\_disrupted \= 4 are selected, giving I\_cell \= κ/r \= 4/4 \= 1\.

Non-self-folding lattice caveat: The theorem assumes the Regge lattice is primitive (non-self-folding). For Kelvin/BCC lattices, the primitive locality assumption may fail — this is registered as gate FU8-P6.4.

*\[STATUS: PROVEN\] Group-theoretic core verified (10/10 involutions). κ=4 uniquely selected by P6 bridge.*

**3.1 Lemma 8.1 Review (ZS-U5 v1.0 §5, n=5)**

From ZS-U5 v1.0 Lemma 8.1 \[DERIVED\]: δφ\_cell \= A × I\_cell, with I\_cell \= κ\_disrupted/r \= 4/4 \= 1\. The X→Y sector transition: S₅ \= |I\_h/T\_d cosets| × π/A \= 5 × π/A \= 5π/A ≈ 196.13, where |I\_h/T\_d| \= 120/24 \= 5 (orbit counting via orbit-stabilizer theorem).

**3.2 Lemma 8.2: Z₂ Holonomy Action (n=6) \[DERIVED\]**

The Z₂ transition (ε: \+1 → −1) is an intra-sector topological phase reversal. The relevant group object is the vertex stabilizer of T\_d:

*S\_Z₂ \= |Stab\_{T\_d}(v)| × π/A \= 6π/A ≈ 235.35     (2)*

**4-step proof:** Step 1: Z₂ reversal is intra-Z-sector → stabilizer order governs. Step 2: Orbit-stabilizer theorem: |T\_d| \= |Orb(v)| × |Stab(v)| \= 4 × 6 \= 24\. Therefore |Stab\_{T\_d}(v)| \= 6\. The stabilizer Stab\_{T\_d}(v) ≅ D₃ \= C₃ ⋊ Z₂. Step 3: Each D₃ element contributes one Regge cell with δφ\_cell \= A. Total: S\_Z₂ \= 6×(π/A). Step 4: Three independent convergent paths: G1: Stab\_{I\_h}(face) \= 120/20 \= 6 \[PROVEN\]; G2: Stab\_{T\_d}(vtx) \= 24/4 \= 6 \[PROVEN\]; G3: dim(Y) \= 6 \[LOCKED\].

**3.2a Chamber-Cell Correspondence Lemma \[DERIVED\]**

**Theorem (Minimal Unwinding on Punctured Vertex-Link):** Let v be the frozen vacuum vertex. The Z-anchor punctures the center of lk(v). Then the minimum winding-1 path on lk(v)× has combinatorial length ℓ\_min \= 6\.

**Proof (6 steps):** 

**Step 1 (Vertex-link identification):** The regular tetrahedron has 4 vertices. The link of any vertex v is the opposite face, a triangle: lk(v) ≅ Δ². \[PROVEN: standard polyhedral geometry\]

**Step 2 (Barycentric subdivision):** sd(Δ²) partitions the triangle into (dim+1)\! \= 3\! \= 6 chambers. Each chamber is a flag (vertex ⊂ edge ⊂ face), i.e., a pair (v\_i, e\_ij) where v\_i ∈ e\_ij. Explicit count: 3 vertices × 2 incident edges \= 6 flags. \[PROVEN: combinatorial identity\]

**Step 3 (D₃ equivariance):** D₃ ≅ Stab\_{T\_d}(v) acts on the 6 chambers by permuting (v\_i, e\_ij) → (σ(v\_i), σ(e\_ij)). The action is simply transitive: |orbit| \= 6, |stab(c₀)| \= 1\. Therefore all 6 chambers are geometrically equivalent — each wall crossing carries the same instanton action π/A. \[PROVEN: explicit computation\]

**Step 4 (Hexagonal dual graph):** Two chambers are adjacent iff they share a codimension-1 wall (differ in exactly one flag element). The chamber-dual adjacency graph is the cycle graph C₆: every chamber has exactly 2 neighbors, forming a hexagon. The 6 walls alternate between 3 vertex-swaps (order-2) and 3 edge-swaps (order-3). \[PROVEN: explicit adjacency computation\]

**Step 5 (Topological constraint):** The Z-anchor defect punctures the center of lk(v), creating π₁(lk(v)×) ≅ ℤ. The generator of π₁ is the boundary cycle of the hexagon C₆. Any winding-1 closed path must traverse this generator at least once. Since the generator has length 6 in C₆: ℓ\_min ≥ 6\. \[PROVEN: standard algebraic topology\]

**Step 6 (Existence \+ minimality):** The hexagonal boundary itself is a winding-1 path of length exactly 6: ℓ\_min ≤ 6\. Combining with Step 5: ℓ\_min \= 6\. No shortcut exists because C₆ has no chords (each chamber has exactly 2 neighbors) and girth(C₆) \= 6\. □

**Corollary:** S\_Z₂ \= ℓ\_min × S\_step \= 6 × (π/A) \= 6π/A ≈ 235.35. The number 6 is forced by the vertex-link of a tetrahedron being a triangle (3\! \= 6 chambers). Anti-numerology: octahedral vertex-link (square) gives 8; icosahedral (pentagon) gives 10\.

*\[STATUS: DERIVED\] ℓ\_min \= 6 is PROVEN (girth of C₆). Step cost π/A is DERIVED.*

**3.3 Unified Formula**

S₅ \= |I\_h/T\_d cosets| × π/A (orbit). S₆ \= |Stab\_{T\_d}(v)| × π/A (stabilizer). S₆ \= S₅ \+ π/A (step continuity).

*\[STATUS: DERIVED\] π/A step structure from orbit-stabilizer duality.*

**§4. Timescale Hierarchy**

*All Z-Spin cosmological timescales: τ\_n \= t\_P × exp(nπ/A),  n ∈ ℤ₊,  t\_P \= 1.708×10⁻⁵¹ yr.*

**Table 2\. Timescale hierarchy.**

| n | Group Origin | τ\_n (yr) | Physical Scale |
| :---: | ----- | :---: | :---: |
| 2 | |O\_h/T\_d| \= Z \= 2 | \~6.3×10⁻¹⁰ s | Weak baryon decays ★ |
| 5 | |I\_h/T\_d cosets| \= 5 | 2.56×10³⁴ yr | Proton decay ★ |
| 6 | |Stab\_{T\_d}(v)| \= 6 | 2.78×10⁵¹ yr | Z₂ holonomy (NEW) ★ |

Step size: π/A ≈ 39.225 ≈ 17 orders of magnitude per n. No free parameters.

*\[STATUS: DERIVED\] All three timescales from A \= 35/437 alone.*

**§4.1 Parallel Reading of the Timescale Hierarchy \[v1.0 dated update 2026-04-24\]**

**Motivation.** Table 2 of §4 lists τ₂, τ₅, τ₆ in a single X-clock reference frame. A naive sequential reading of this list interprets the ratio τₙ₊₁/τₙ \= exp(π/A) ≈ 1.08 × 10¹⁷ as a “waiting interval”: the universe would wait 10¹⁷ τ₅-units between proton decay (τ₅) and Z₂ holonomy (τ₆). This produces a visible “cosmic inefficiency” puzzle. ZS-A8 v1.0 Revised §5.3 (Theorem 5.3.1, HYPOTHESIS-strong) resolves this puzzle by a parallel-clock reading. This subsection imports that resolution into ZS-U8 without changing any numerical value in Table 2\.

**Y-Time Dilation Theorem (ZS-A8 §5.3 Theorem 5.3.1, HYPOTHESIS-strong).** The X-clock observation of any Y-sector completion event is dilated by a factor exp(π/A) per added Y-dimension relative to the Y-sector proper-time measurement of the same event:

τ₆ / τ₅ \= exp(π/A)     (4.1.1)

where τ₅ is the X-sector baryon-completion lifecycle in X-clock proper time and τ₆ is the X-clock observation of the Y-sector Z₂ holonomy completion. The dilation factor decomposes exactly as

exp(π/A) \= exp( (2π/A) × (1/2) ) \= exp( N₍₂π₎ × ⟨sin²(φ/2)⟩ )     (4.1.2)

where N₍₂π₎ \= 2π/A ≈ 78.45 is the Z-Telomere completion cycle count (PROVEN, ZS-U5 v1.0 §5.2 Lemma 8.1, DERIVED-under-P6), and ⟨sin²(φ/2)⟩ \= (1/4π) ∫₀⁴π sin²(φ/2) dφ \= 1/2 is the time-average of the SU(2) spinor phase gate over the 4π period (PROVEN, ZS-M3 v1.0 §10.3, ZS-T2 v1.0 §5.5).

**Physical content of the parallel reading.** The X-sector baryon-completion lifecycle (τ₅) and the Y-sector wave-contraction lifecycle (Z₂ holonomy completion) are SIMULTANEOUS in their respective sectoral proper times, not sequential. Each sector completes its own proper-time τ₅ at matched duration. The factor exp(π/A) ≈ 10¹⁷ appearing in Table 2 as the ratio τ₆/τ₅ is the Y-sector’s time-dilation as seen by the X-clock observer, analogous to the cosmological inflation factor of ∼60 e-folds in the X-sector. Under this reading, the sequential-waiting interpretation of the hierarchy is replaced by a dual-clock observation picture: no waiting, only two frames measuring the same sectoral completion event.

**Structural support for the “6 \= dim(Y)” convergence (§3.2 Lemma 8.2 revisited).** §3.2 registered three convergent group-theoretic paths to the coefficient 6 in S\_Z₂ \= 6π/A: (G1) |Stab\_(I\_h)(face)| \= 120/20 \= 6, (G2) |Stab\_(T\_d)(vtx)| \= 24/4 \= 6, (G3) dim(Y) \= 6 (LOCKED). Under the sequential reading these were three independent coincidences. Under the Y-Time Dilation reading they are three group-theoretic angles on a single physical phenomenon: the dim(Y) coefficient IS the exponent of time-dilation per Y-completion, and the stabilizer structure IS the information-processing count of one Y-sector lifecycle.

**Epistemic status.** Inputs N₍₂π₎ \= 2π/A and ⟨sin²(φ/2)⟩ \= 1/2 are PROVEN. Their product N₍₂π₎ × ⟨phase⟩ \= π/A is DERIVED. The information-time correspondence that maps phase-information to exponentiated time-dilation is HYPOTHESIS-strong and is inherited directly from ZS-A8 §5.3 with no modification. The parallel reading is a REINTERPRETATION of the existing ZS-U8 results; it does not introduce any new parameter, field, or axiom, and it does not change any numerical value in §4 Table 2, §5 CMB predictions, §6.3 ODE results, or §7 Table 5\. The sequential reading is preserved as a valid single-frame description and the parallel reading is added as a dual-frame description. Both readings are consistent with the same equation τₙ \= t\_P × exp(nπ/A).

**Relation to NC2.** §8 NC2 (“τ₆ not experimentally testable”) is retained without modification. The parallel reading reinterprets the meaning of τ₆ in the X-clock frame but does not promote it to an observable: the Y-sector completion that τ₆ encodes lies entirely outside the X-observer’s causal reach.

**\[STATUS: HYPOTHESIS-strong\]** Parallel reading imported from ZS-A8 §5.3 Theorem 5.3.1. No numerical result changed.

**\[Dated Update 2026-04-26 — ZS-F10 Closure: Parallel Reading Promotion to DERIVED-CONDITIONAL strong\]**

ZS-F10 v1.0 (i-Tetration Internal Time, Foundations Theme, April 2026\) closes the information-time correspondence promotion path of ZS-A8 §SA.7 by establishing the Information-Time Correspondence Theorem F10.1, which formalizes the bridge linking phase-information to exponentiated time-dilation as a derived identity. Consequently, the Parallel Reading of §4.1 above — which inherits its status directly from ZS-A8 §5.3 Theorem 5.3.1 — inherits the corresponding status promotion.  
**Status update.** The Parallel Reading of §4.1 (Y-Time Dilation Theorem 5.3.1 inherited from ZS-A8 §5.3) is hereby promoted from HYPOTHESIS-strong to **DERIVED-CONDITIONAL strong**, tracking the ZS-A8 §5.3 dated update of 2026-04-26 (separate document). The conditionality is the same dim(Z) \= 2 import from ZS-F5 v1.0 (PROVEN) that conditions the entire ZS-F10 framework; with five independent routes converging on dim(Z) \= 2 (polyhedral, gauge-algebraic, MUB, fixed-point analytic, protocol-theoretic; ZS-F0 v1.0(Revised) Corollary 5.2.A.2), the conditionality is structurally over-determined. The operational reading is DERIVED.  
**Structural decomposition unchanged.** Equations (4.1.1) τ₆/τ₅ \= exp(π/A) and (4.1.2) exp(π/A) \= exp((2π/A) × (1/2)) \= exp(N₍₂π₎ × ⟨sin²(φ/2)⟩) of §4.1 above remain identical at the numerical level. The phase-effective handshake count interpretation introduced by ZS-F10 §6 Theorem F10.2 now provides the corrected single-step proof (no separate “time-averaging” reduction needed): n\_φ ≡ N₍₂π₎ × ⟨sin²(φ/2)⟩ \= π/A, hence Δν per Y-cycle \= (A/π) × n\_φ \= 1, which directly gives Δlog(τ) \= π/A per Y-cycle, hence τ₆/τ₅ \= exp(π/A). The arithmetic factor-of-2 correction noted in ZS-F10 §6.2 Phase 2 (Eq. 6.4′ replacing v1.0 Eq. 6.4) does not affect any ZS-U8 result.  
**Verification (50-digit mpmath, ZS-F10 Phase 2 audit).** (i) N₍₂π₎ \= 2π/A \= 78.450056549642265440467151913893... PASS. (ii) N₍₂π₎ × ⟨sin²(φ/2)⟩ \= π/A \= 39.225028274821132720... PASS. (iii) exp(π/A) \= exp(N₍₂π₎ × ⟨phase⟩) at machine zero residual (|residual| \&lt; 10⁻⁴⁰) PASS. (iv) Δν per Y-cycle \= 1.0 with |residual| \&lt; 10⁻⁵⁰ PASS. All four checks correspond to ZS-F10 audit script zs\_f10\_pr\_audit\_v1\_0.py items C1, F-F10.7, and the (6.4′)-(6.5′) corrected proof chain.  
**No numerical prediction is changed.** The 60/60 verification suite of ZS-U8 v1.0 is unchanged. The §4 Table 2 timescale hierarchy (τ₂ ≈ 6.3×10⁻¹⁰ s weak baryon decays, τ₅ ≈ 2.56×10³⁴ yr proton decay, τ₆ ≈ 2.78×10⁵¹ yr Z₂ holonomy), the §5 CMB predictions (n\_s \= 0.9676, r \= 0.00890, mirror cosmology Z₂ symmetry), the §6.3 ODE results (f\_crit \= 1.0002), the §7 baryon asymmetry η\_B \= (6/11)³⁵, and the §8 NC2 (“τ₆ not experimentally testable”) all remain identical. The two readings — SEQUENTIAL X-clock reading (preserved) and PARALLEL dual-clock reading (this section, now DERIVED-CONDITIONAL strong) — are mutually consistent with the same equation τₙ \= t\_P × exp(nπ/A).  
**Cross-reference addendum.** This dated update adds ZS-F10 v1.0 (April 2026\) as an upstream closure source. The §4.1 reference entries \[16\] ZS-A8 v1.0 Revised and \[17\] ZS-T2 v1.0 (introduced in the 2026-04-24 dated update) are supplemented by \[18\] ZS-F10 v1.0 in cross-reference dependency tracking; the References list itself is preserved verbatim in this dated update per the no-deletion rule (the reference will be added to the References list at the next ZS-U8 cumulative revision).  
**Supplementary §4.1 status note.** The §4.1 closing line “\[STATUS: HYPOTHESIS-strong\] Parallel reading imported from ZS-A8 §5.3 Theorem 5.3.1. No numerical result changed.” should be read with the supplementary annotation: “promoted to DERIVED-CONDITIONAL strong (operationally DERIVED) per ZS-F10 v1.0 Theorem F10.2 closure of ZS-A8 §SA.7 promotion path”. The Conclusion ③-parallel note in §3.3 (the parenthetical “See §4.1 and ZS-A8 v1.0 Revised §5.3 Theorem 5.3.1 (HYPOTHESIS-strong)”) inherits the same status promotion through this dated update.  
**No-deletion compliance.** All §4.1 text is preserved verbatim. This dated update is additive only. External label remains v1.0 (no version bump per ZS-A8 v1.0 Revised precedent and ZS-F10 v1.0 Phase 2 dated update precedent). Word count strictly increased per the no-deletion rule. The Phase 1 dated update of 2026-04-24 (Parallel Reading import from ZS-A8) is preserved unchanged. Source for closure: ZS-A8 v1.0 §5.3 dated update of 2026-04-26 (status promotion to DERIVED-CONDITIONAL strong); ZS-F10 v1.0 §6.3 Phase 2 (peer review closure). **\[STATUS: DERIVED-CONDITIONAL strong, inherited\]**

**§5. Mirror Cosmology: Z₂ Symmetry Proof**

Since V\_E(−ε) ≡ V\_E(+ε) \[PROVEN, §2.2\], every inflationary observable is identical in both sectors. Mirror trajectory: max|ε₊(t) \+ ε₋(t)| \= 0.0000 (machine precision).

*\[STATUS: PROVEN\] Z₂ symmetry is algebraic, not approximate.*

**5.1 CMB Predictions (Z₂-Symmetric)**

**Table 3\. CMB predictions.**

| Observable | Value | Planck 2018 | Pull | Status |
| :---: | :---: | :---: | :---: | :---: |
| n\_s (N=60) | 0.9676 | 0.9649 ± 0.0042 | 0.6σ | PASS |
| n\_s (N=55) | 0.9636 | — | 0.3σ | PASS |
| r | 0.00890 | \< 0.032 (BK18+Planck) | — | PASS |
| r / r\_Staro | 2.671× | — | — | DERIVED |
| N\* (e-folds) | 59.5 | \[55, 65\] | — | PASS |

**Tensor-to-scalar discriminator:** r\_ZS \= 0.00890 vs r\_Staro ≈ 0.00333 for N\* \= 60\. r\_ZS / r\_Staro \= 2.671 → \~6σ discrimination at LiteBIRD (early 2030s) → Gate FU8-2.

**5.2 Baryogenesis (Mirror \= Primary)**

From ZS-U3 v1.0: η\_B \= (6/11)^35 \= 6.117×10⁻¹⁰. By Z₂ symmetry, both sectors generate identical baryon asymmetry. The exponent 35 \= A\_numerator is a structural identity (ZS-M3 v1.0).

*\[STATUS: PROVEN (Z₂) \+ DERIVED (η\_B value)\]*

**§6. ε-Field Dynamics After τ₅**

**6.1 Phase A: de Sitter Stability \[DERIVED\]**

Post-τ₅: H\_dS ≈ 1.18×10⁻⁶¹ M\_P. Effective mass at ε \= \+1: m\_eff \= √(λ\_vac/K(1)) ≈ 0.116 M\_P. Ratio: m\_eff/H\_dS ≈ 1.04×10⁶⁰ ≫ 1\. The ε \= \+1 attractor is super-stable throughout the τ₅ → τ₆ epoch.

*\[STATUS: DERIVED\] Heavy-field regime: oscillations 10⁶⁰× faster than Hubble.*

**6.2 Phase B: Z-Telomere Phase Drift \[HYPOTHESIS\]**

Z-Telomere drift (ZS-U5 v1.0 Lemma 8.1): δφ \= A rad/cycle. D₃ threshold at Φ\_total \= |D₃| × A \= 6A. Time: τ₆ \= t\_P × exp(S\_Z₂) \= t\_P × exp(6π/A) ≈ 2.78×10⁵¹ yr.

*\[STATUS: HYPOTHESIS\] Physical scenario pending full dynamical verification.*

**6.3 Phase C: Z₂ Transition \[DERIVED+VERIFIED\]**

Kinetic energy threshold: ε̇\_min \= √(2V\_E(0)/K(1)) ≈ 8.179×10⁻² M\_P. Numerical ODE integration confirms the transition dynamics:

**Table 4\. ODE transition results.**

| Factor | Outcome | Physical Meaning |
| :---: | :---: | :---: |
| 0.9 (sub) | Bounce at ε\_min≈0.305, returns to ε≈+1 | Insufficient energy |
| f\_crit \= 1.0002 | Transition exactly triggered | Near-degenerate phase transition |
| 1.1 (super) | ε \= 0 at t≈16, ε \= −1 at t≈34 M\_P⁻¹ | Full mirror rolldown |

The critical factor f\_crit ≈ 1.000 means the transition requires essentially exactly ε̇\_min. This is consistent with the near-degenerate vacuum picture: V\_E(+1) \= V\_E(−1) \= 0 exactly, so the transition is symmetric and requires only the minimum energy to cross the barrier at ε \= 0\. The instability rate μ \= 0.1177 M\_P means the rolldown to ε \= −1 completes in \~10⁻⁴³ s once the barrier is crossed.

*\[STATUS: VERIFIED\] f\_crit ≈ 1.000. Instability rate μ \= 0.1177 M\_P.*

**§7. Pre-Registered Falsification Gates**

**Table 5\. Falsification gates.**

| ID | Condition | Timeline | Status |
| :---: | ----- | :---: | :---: |
| FU8-1 | τ\_p ≠ 2.56×10³⁴ yr at \>3σ (Hyper-K) | 2030+ | TESTABLE |
| FU8-2 | r ≠ 0.00890 at \>3σ (LiteBIRD tensor) | early 2030s | TESTABLE ★ |
| FU8-3 | |Stab\_{T\_d}(v)| ≠ 6 by group theory | Immediate | SUPRA-FALSIFIABLE |
| FU8-4 | Mirror n\_s' ≠ n\_s (V\_E non-even) | Theory | SUPRA-FALSIFIABLE |
| FU8-5 | f\_crit ≫ 1 (large excess energy) | Numerics | REFUTED: 1.0002 |
| FU8-6 | S\_Z₂ group-theory inconsistency | Theory | RESOLVED (§3.2a) |

**FU8-2 is the critical near-term test.** r \= 0.00890 \= 2.671 × r\_Staro is distinguishable at \~6σ by LiteBIRD (target δr \~ 0.001). A null detection (r \< 0.005 at \>3σ) falsifies the Z-Spin inflationary sector.

**Additional P6 gates:** FU8-P6.4: Kelvin/BCC lattice self-folding (primitive locality fails), STATUS: SUPRA-FALSIFIABLE. FU8-P6.5: Alternative definition of 'primitive' gives κ ≠ 4, STATUS: OPEN. FU8-P6.6: Non-primitive cells dominate holonomy integral, STATUS: OPEN.

**§8. Cross-Paper Consistency**

**Table 6\. Cross-paper dependencies.**

| This paper § | Uses | From paper | Status |
| ----- | :---: | ----- | :---: |
| §2 (V\_E) | λ\_vac \= 2A² | ZS-U5 v1.0 §8 | DERIVED-COND |
| §2 (CdL) | V\_E(±1) \= 0 | ZS-F1 v1.0 §3 | PROVEN |
| §3 (Lemma 8.2) | δφ \= A (Lemma 8.1) | ZS-U5 v1.0 §5.2 | DERIVED |
| §3 (Lemma 8.2) | |T\_d|=24, |I\_h|=120 | ZS-F2 v1.0 | LOCKED |
| §4 (τ₅) | S₅ \= 5π/A | ZS-A3 v1.0 §4 | HYPOTHESIS |
| §5 (inflation) | n\_s, r | ZS-U1 v1.0 §4 | DERIVED |
| §5 (η\_B) | η\_B \= (6/11)^35 | ZS-U3 v1.0 §2 | DERIVED |
| §6 (m\_eff) | K(ε) | ZS-F1 v1.0 §3 | DERIVED |

**Non-Claims:** NC1: No observable properties of mirror universe. NC2: τ₆ not experimentally testable. NC3: No new Big Bang with different physics. NC4: Proton decay τ₅ belongs to ZS-A3 v1.0.

**§9. Epistemic Summary**

**Table 7\. Epistemic status of all results.**

| Result | Status | Source § |
| ----- | :---: | ----- |
| V\_E(±1) \= 0, V\_E(−ε) ≡ V\_E(+ε) | PROVEN | §2.2 algebraic |
| S\_Coleman → ∞ (ΔV \= 0\) | PROVEN | §2.3 |
| S\_HM ≈ 5.7×10¹²³ | DERIVED | §2.4 |
| |Stab\_{T\_d}(v)| \= 6 \= |D₃| | PROVEN | §3.2 group theory |
| S\_Z₂ \= 6π/A, ℓ\_min \= 6 | DERIVED | §3.0a+§3.2+§3.2a |
| τ₅ \= 2.56×10³⁴ yr | HYPOTHESIS | ZS-A3 v1.0 |
| τ₆ \= 2.78×10⁵¹ yr | DERIVED | §4 |
| n\_s=0.9676, r=0.00890 (mirror=primary) | PROVEN+VERIFIED | §5 |
| f\_crit ≈ 1.000 | DERIVED+VERIFIED | §6.3 |

**§10. Conclusion**

**① Vacuum structure (§2):** V\_E(+1) \= V\_E(−1) \= 0, CdL forbidden, Z-Telomere is the only viable mechanism.

**② Timescale hierarchy (§3–4):** τ₅ \= t\_P × exp(5π/A) ≈ 2.56×10³⁴ yr (proton decay). τ₆ \= t\_P × exp(6π/A) ≈ 2.78×10⁵¹ yr (Z₂ holonomy). Step continuity: S₆ \= S₅ \+ π/A.

**③ Mirror cosmology (§5):** V\_E(−ε) ≡ V\_E(+ε) algebraically → identical n\_s, r, η\_B in both sectors.

**④ Post-τ₅ dynamics (§6):** m\_eff/H\_dS \~ 10⁶⁰ ensures ε \= \+1 is pinned. Transition triggered near-exactly at ε̇\_min (f\_crit \= 1.0002).

**Decisive test:** r \= 0.00890 \= 2.671 × r\_Starobinsky → \~6σ discrimination at LiteBIRD (early 2030s) \[Gate FU8-2\].

**Parallel reading note \[v1.0 dated update 2026-04-24\]:** The sequential X-clock reading “τ₅ (proton decay) → τ₆ (Z₂ holonomy)” in item ③ above is supplemented (not replaced) by the parallel-clock reading of §4.1: X-sector and Y-sector lifecycles are SIMULTANEOUS in their respective sectoral proper times, and τ₆/τ₅ \= exp(π/A) ≈ 10¹⁷ is the Y-sector time-dilation as seen by the X-clock observer. Both readings are consistent with τₙ \= t\_P × exp(nπ/A). Step continuity S₆ \= S₅ \+ π/A describes the group-theoretic cost increment in coset units, not a temporal waiting interval. See §4.1 and ZS-A8 v1.0 Revised §5.3 Theorem 5.3.1 (HYPOTHESIS-strong).

**Epistemic honesty:** Lemma 8.2 (S\_Z₂ \= 6π/A) is DERIVED as of v1.0: Theorem P6\* (§3.0a) closes the P6 bridge via primitive locality, and the Chamber-Cell Correspondence Lemma (§3.2a) proves ℓ\_min \= 6 from vertex-link topology. This paper does NOT claim that the mirror universe is currently observable, that ε \= −1 physics differs from ε \= \+1 physics, or that τ₆ is experimentally accessible. These are long-timescale structural consequences, not near-term predictions. All inputs locked from ZS-F1–ZS-U5 v1.0. Zero new free parameters.

**§11. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite (Python/NumPy/SciPy, including ODE transition solver) is publicly available.

**Appendix A. Verification Suite Results**

| Category | Tests | Pass/Fail | Key Result |
| ----- | :---: | :---: | ----- |
| \[A\] Locked Inputs | 5 | 5/0 | A, λ\_vac, t\_P, groups |
| \[B\] V\_E Symmetry | 6 | 6/0 | Z₂ identity, V(±1)=0, barrier |
| \[C\] CdL Analysis | 4 | 4/0 | ΔV=0, S→∞, S\_HM ≫ S\_Z₂ |
| \[D\] Group Theory | 6 | 6/0 | |T\_d|, |I\_h|, |D₃|=6, 3 paths |
| \[E\] Timescale Hierarchy | 4 | 4/0 | τ₅, τ₆, step π/A |
| \[F\] Mirror Cosmology | 10 | 10/0 | n\_s, r, η\_B, Z₂ trajectory |
| \[G\] ε-EOM After τ₅ | 8 | 8/0 | m/H, f\_crit, transition ODE |
| \[H\] Chamber Geometry | 10 | 10/0 | lk(v), sd, C₆, D₃ equivariance |
| \[I\] Cross-Paper | 7 | 7/0 | ZS-U5, ZS-A3, ZS-U1, ZS-U3 |

**TOTAL: 60/60 PASS — 100% pass rate**

**Cross-Reference Table**

| Result | Status | Dependencies |
| ----- | :---: | ----- |
| V\_E(−ε) ≡ V\_E(+ε) | PROVEN | ZS-F1 v1.0 action structure |
| S\_CdL → ∞ | PROVEN | §2.2 \+ §2.3 |
| S\_Z₂ \= 6π/A ≈ 235.35 | DERIVED | ZS-U5 v1.0 \+ §3.2a |
| τ₆ \= 2.78×10⁵¹ yr | DERIVED | §4 from S\_Z₂ |
| Mirror n\_s, r, η\_B | PROVEN | §5 Z₂ algebraic |
| f\_crit \= 1.0002 | VERIFIED | §6.3 ODE integration |
| r / r\_Staro \= 2.671 | DERIVED | ZS-U1 v1.0 §4 |

**References**

\[1\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026).  
\[2\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026).  
\[3\] K. Kang, "ε-Field Inflation," ZS-U1 v1.0 (2026).  
\[4\] K. Kang, "Baryon Asymmetry," ZS-U3 v1.0 (2026).  
\[5\] K. Kang, "Quantum Gravity Bridge," ZS-U5 v1.0 (2026).  
\[6\] K. Kang, "Black Hole Physics," ZS-A3 v1.0 (2026).  
\[7\] K. Kang, "Regge-Holonomy, Immirzi & Z-Telomere," ZS-M3 v1.0 (2026).  
\[8\] Planck Collaboration, A\&A 641, A6 (2020).  
\[9\] Tristram, M. et al., Phys. Rev. D 105, 083524 (2022). r \< 0.032.  
\[10\] Coleman, S. & de Luccia, F., Phys. Rev. D 21, 3305 (1980).  
\[11\] Hawking, S.W. & Moss, I.G., Phys. Lett. B 110, 35 (1982).  
\[12\] Regge, T., Nuovo Cimento 19, 558 (1961).  
\[13\] Starobinsky, A.A., Phys. Lett. B 91, 99 (1980).  
\[14\] Hyper-Kamiokande Collaboration, arXiv:1805.04163 (2018).  
\[15\] LiteBIRD Collaboration, PTEP 2023, 042F01 (2023).

**Version History**

**v1.0 (March 2026):** Initial public release. Z₂-degenerate vacuum (PROVEN), CdL forbidden (PROVEN), D₃ holonomy S\_Z₂ \= 6π/A (DERIVED), Chamber-Cell Correspondence Lemma ℓ\_min \= 6 (PROVEN), timescale hierarchy τ₅/τ₆ (DERIVED), mirror cosmology Z₂ proof (PROVEN), ε-field dynamics f\_crit \= 1.0002 (VERIFIED), P6 Primitive Locality Theorem κ=4 (PROVEN). 6 falsification gates (FU8-1–FU8-6). 60/60 tests. (Consolidated from internal research notes up to v1.2.0)

**v1.0 dated update 2026-04-24 (Parallel Reading import from ZS-A8):** NEW §4.1 “Parallel Reading of the Timescale Hierarchy” added, importing the Y-Time Dilation Theorem (ZS-A8 v1.0 Revised §5.3 Theorem 5.3.1, HYPOTHESIS-strong). Under the parallel-clock reading, X-sector baryon-completion lifecycle (τ₅) and Y-sector wave-contraction lifecycle (Z₂ holonomy completion) are SIMULTANEOUS in their respective sectoral proper times, not sequential. The ratio τ₆/τ₅ \= exp(π/A) ≈ 10¹⁷ is reinterpreted as the Y-sector time-dilation as seen by the X-clock observer, not a waiting interval. Structural decomposition exp(π/A) \= exp((2π/A) × (1/2)) where N₍₂π₎ \= 2π/A is the Z-Telomere completion cycle count (PROVEN, ZS-U5 v1.0 §5.2 Lemma 8.1) and ⟨sin²(φ/2)⟩ \= 1/2 is the SU(2) spinor phase gate time-average (PROVEN, ZS-M3 v1.0 §10.3, ZS-T2 v1.0 §5.5). The three convergent paths to coefficient 6 in S\_Z₂ \= 6π/A (§3.2: Stab\_(I\_h) face, Stab\_(T\_d) vtx, dim(Y)) are reinterpreted as three group-theoretic angles on a single physical phenomenon — Y-sector temporal structure. NEW Conclusion ③-parallel note added. NEW reference entries \[16\] ZS-A8 v1.0 Revised and \[17\] ZS-T2 v1.0 listed in cross-reference dependencies (References list itself untouched in this update). NO numerical result changed: §4 Table 2, §5 CMB predictions (n\_s, r, η\_B), §6.3 ODE results (f\_crit \= 1.0002), §7 falsification gates, and the 60/60 verification suite all remain identical. NO new free parameter introduced. NO existing text deleted. Sequential reading is preserved; parallel reading is added as a second, dual-frame description of the same equation τₙ \= t\_P × exp(nπ/A). §8 NC2 (“τ₆ not experimentally testable”) retained. Motivated by the physical intuition (ZS-A8 §5.3) that X-sector accelerated expansion must have a simultaneous Y-sector wave-contraction counterpart completing at matched sectoral proper-time scale. Parallel reading status: HYPOTHESIS-strong (inherited from ZS-A8 §5.3). Word count strictly increased (no-deletion rule preserved). Patch author: Kenny Kang; XML edit by Claude (Anthropic) per Kenny’s direction.  
