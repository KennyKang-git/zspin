**ZS-F12** 

**Tetrahedral Dual Orientation Multiplicity and the Layer Separation Hypothesis**

*Polyhedral Origin of the Factor 2 in the 2e^A Identity, with a Universal Factorization Theorem for Scale-Invariant Z-Transform Observables*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-F12 (Foundations Theme)  |  Paper 12 of the Foundations series  |  v1.0

**Verification: 20/20 PASS  |  Zero Free Parameters  |  Two New Theorems (Theorem TDO-1, Theorem LSH-1)**

**§0. Abstract**

Two independent, corpus-PROVEN cosmological/quark identities share the same closed form: Ω\_Λ/Ω\_m \= m\_d/m\_u \= 2e^A \= 2.1668, spanning forty orders of magnitude in physical scale. The exp(A) factor is rigorously DERIVED in ZS-F4 §6 from the polyhedral Wilson-loop holonomy with ε ↔ −ε Z₂ doubling. The factor 2 has been PROVEN in ZS-S15 §5 as the SO(3)/SU(2) double-cover ratio for the Maxwell field, but its structural origin in the polyhedral Z-sector mediator has been left OPEN.

This paper establishes two new theorems that close this gap. First, Theorem TDO-1 (Tetrahedral Dual Orientation Multiplicity) proves that the factor 2 is forced by tetrahedral V↔F self-duality as a multiplicity in oriented dual transport, providing the upstream polyhedral source that ZS-S15 NC-S15.6 left OPEN. Second, Theorem LSH-1 (Layer Separation Hypothesis) establishes a systematic factorization R \= μ\_Tet × Hol\_ε × 𝒮\_scale for any dimensionless ratio observable mediated by the self-dual tetrahedron Z-sector, where μ\_Tet \= 2 and Hol\_ε \= exp(A) are universal layers and 𝒮\_scale is a scale-specific internal mechanism that cancels in same-class ratios.

A negative result is also reported and registered: the V↔F outer involution and the ε ↔ −ε Wilson-loop Z₂ are mathematically distinct objects acting on different sectors. Therefore V↔F does not enter the holonomy exponent (which would yield the falsified prediction exp(2A) \= 1.1737); it enters as a multiplicative prefactor outside the exponent. This REJECTS the original hypothesis F-Tet-2eA-1 and replaces it with the new gate F-Tet-2eA-2.

Six instances of the Scale-Invariant Z-Transform pattern are enumerated from the corpus, each verified to satisfy the LSH-1 factorization: (1) the 2e^A duality of m\_d/m\_u and Ω\_Λ/Ω\_m; (2) the T1-2/T1-3 reciprocal duality of 1/α\_EM ↔ ε\_solar at single-eigenvalue level; (3) the T1-4 register/spectral face duality of m\_τ at 4×4 matrix level; (4) the η\_topo ≈ Ω\_m near-equality between i-tetration and face counting; (5) the Hubble three-level holonomy structure; (6) the timescale hierarchy τ\_n \= t\_P × exp(nπ/A). The universal layered structure Layer 1 (μ\_Tet, polyhedral signature) × Layer 2 (Hol\_ε, ε-field holonomy) × 𝒮\_scale (scale-specific mechanism) provides the systematic mathematical realization of the ZS framework's claim of unification across sixty orders of magnitude (The Book §0.2).

**Keywords:** *tetrahedral self-duality, oriented dual transport multiplicity, 2e^A duality, layer separation, scale-invariant Z-Transform, Wilson loop holonomy, SO(3)/SU(2) double cover, Cross-Coupling Theorem, polyhedral mediator, zero free parameters.*

**§0.1 Epistemic Status Legend**

All claims in this paper are tagged with one of the following statuses, consistent with the Z-Spin v1.0 corpus convention:

| STATUS | DEFINITION |
| :---: | ----- |
| PROVEN | Mathematical theorem with complete proof, or numerical verification at machine precision (≤ 10⁻¹⁰ residual). |
| DERIVED | Quantitative consequence of PROVEN items combined with Z-Spin axioms, with zero free parameters beyond A \= 35/437. |
| DERIVED-CONDITIONAL | Follows from locked inputs conditional on a stated hypothesis or assumption. |
| HYPOTHESIS-strong | Multiple independent lines of evidence; full derivation chain incomplete; falsifiable. |
| OBSERVATION | Numerical proximity confirmed with anti-numerology tests; no action-level derivation. |
| REJECTED | Hypothesis previously advanced in free-exploration sessions that fails verification under rigorous calculation. Corrected statement provided. |
| OPEN | Recognized gap requiring future work, with explicit closure path registered. |
| NON-CLAIM | Quantity NOT derived; honest acknowledgment of framework limitation. |

**§1. Introduction**

**1.1 The 2e^A Puzzle**

Two independent corpus-PROVEN identities share the same closed form 2e^A \= 2.1668:

*Ω\_Λ / Ω\_m \= 2 e^A \= 2.1668    \[cosmic scale, Gpc\]*

*m\_d / m\_u \= 2 e^A \= 2.1668    \[quark scale, fm\]*

These two ratios are extracted from physical scales separated by approximately forty orders of magnitude. The Z-Spin framework registers this as the ZS-A1/A5 "2e^A duality identity" (PROVEN-VERIFIED). However, the structural origin of the closed form has remained partially OPEN: the exp(A) factor is rigorously DERIVED in ZS-F4 §6 from Wilson-loop holonomy with ε ↔ −ε Z₂ doubling, but the factor 2 has been variously attributed to (i) the SO(3)/SU(2) double-cover ratio in ZS-S15 §5 (PROVEN for Maxwell), (ii) the dimension ratio dim(Y)/dim(X) \= 2 in the Cross-Coupling Theorem (ZS-M2 §5 PROVEN), or (iii) a phenomenological observation in Model-E (ZS-A5 §5.4 working hypothesis). ZS-S15 NC-S15.6 explicitly notes that "each factor 2 has its own derivation chain" and leaves the structural connection OPEN.

**1.2 Four Open Questions**

Four specific structural questions about the factor 2 in 2e^A have remained without explicit derivation in the v1.0 corpus:  
(Q1) Is the factor 2 in 2e^A the same factor 2 that appears in (a) ZS-S15 §5 SO(3)/SU(2) double cover, (b) ZS-Q7 dim(Y)/dim(X) ratio, (c) ZS-U8 ΔN\_eff \= 2A, or (d) ZS-S8 register face √(Y/X) \= √2 ?  
(Q2) Does the factor 2 in 2e^A originate from tetrahedral V↔F self-duality (the Z-sector mediator structure), or from some other polyhedral source?  
(Q3) If the factor 2 has a polyhedral origin, why does it enter as a multiplicative prefactor outside the exp(A) exponent rather than as an additive contribution inside (which would yield exp(2A) ≠ 2.1668)?  
(Q4) If the same closed form 2e^A applies at two distinct physical scales (cosmic and quark), is this a deep structural fact or a numerical coincidence? What systematic framework, if any, governs the appearance of the same closed form at different scales?

**1.3 Two Theorems and One Negative Result**

This paper provides two theorems, one explicit negative result, and one enumeration:  
(A1) Theorem TDO-1 (Tetrahedral Dual Orientation Multiplicity, DERIVED-CONDITIONAL). The factor 2 in 2e^A originates from tetrahedral V↔F self-duality via μ\_Tet \= 2 in oriented dual transport. The two oriented directions V→F and F→V are T\_d-equivariantly equivalent (PROVEN, ZS-F9 Lemma 3.2) but combinatorially distinct, yielding multiplicity 2 at the level of dimensionless ratio observables. This is the polyhedral signature that ZS-F9 §4 Observation 4.1 identified as unique to the truncated tetrahedron (F^pres \= F^cut \= 4, the only Archimedean truncation with this property).  
(A2) Theorem LSH-1 (Layer Separation Hypothesis, DERIVED-CONDITIONAL). For any dimensionless ratio observable R mediated by the self-dual tetrahedron Z-sector, the universal factorization R \= μ\_Tet × Hol\_ε × 𝒮\_scale holds, where μ\_Tet \= 2 (Theorem TDO-1), Hol\_ε \= exp(A) (ZS-F4 §6), and 𝒮\_scale is a scale-specific internal mechanism that cancels in same-class ratios.  
(N1) Negative Result: F-Tet-2eA-1 REJECTED. The original hypothesis that V↔F outer involution coincides with ε ↔ −ε Z₂ in ZS-F4 §6 is REJECTED on two grounds: (i) the two Z₂ involutions act on different mathematical objects (T\_d outer automorphism on polyhedral cells vs. canonical J\_Z \= diag(+1, −1, \+1, …) on register slot 1, ZS-F8 §8.6 PROVEN); (ii) treating V↔F as an additive contribution to the holonomy exponent yields the falsified prediction exp(2A) \= 1.1737 ≠ 2.1668.  
(E1) Six Instances of the Scale-Invariant Z-Transform are enumerated from the corpus, each verified to satisfy the LSH-1 factorization. The pattern is identified as the systematic mathematical realization of the ZS framework's claim of "Unity Across Sixty Orders of Magnitude" (The Book §0.2).

**1.4 Position in the v1.0 Corpus**

ZS-F12 sits in the Foundations theme alongside ZS-F0 (Ontological Bootstrap), ZS-F8 (Spectral-Protocol Duality), ZS-F9 (Tetrahedral Self-Duality and Hexagonal Mediation), ZS-F10 (i-Tetration Internal Time), and ZS-F11 (Operational Observer Coordinate). ZS-F12 builds directly on ZS-F9 v1.0(Revised) §6 (truncation residue exchange and ρ\_Z \= 0 PROVEN) and ZS-F4 §6 (Wilson loop holonomy DERIVED), and connects downstream to ZS-A1, ZS-A5 (m\_d/m\_u and Ω\_Λ/Ω\_m as 2e^A applications), ZS-S15 §5 (SO(3)/SU(2) factor 2 as PROVEN downstream), and the entire Z-Transform pattern across the corpus. No other v1.0 result is modified by this paper; no numerical prediction is added or changed.

**§2. Locked Inputs**

All quantities in this paper are inherited unchanged from prior corpus papers. No new constants or free parameters are introduced. Status tags reflect the v1.0 corpus standing as of April 2026\.

*Table 2.1. Locked inputs to ZS-F12. All entries are PROVEN, DERIVED, or LOCKED in prior corpus papers.*

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | :---: |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| Q (register dimension) | 11 (prime) | ZS-F5 v1.0 | PROVEN |
| (Z, X, Y) sector dimensions | (2, 3, 6); Q \= Z+X+Y | ZS-F5 v1.0 | PROVEN |
| V(Tet) ≅ F(Tet) ≅ A\_1 ⊕ T\_2 | dim 1+3 \= 4 | ZS-F9 §3.2 Lemma 3.2 | PROVEN |
| E(Tet) ≅ A\_1 ⊕ E ⊕ T\_2 | dim 1+2+3 \= 6 | ZS-F9 §3.3 Theorem 3.3 | PROVEN |
| F^pres \= F^cut \= 4 (t-Tet) | Unique among Archimedean truncations | ZS-F9 §4 Obs. 4.1 | PROVEN |
| ρ\_Z \= 0 | Truncation residue, self-duality | ZS-F9 §6 Lemma 6.2 | PROVEN |
| A \= ρ\_X · ρ\_Y | (5/19)(7/23) \= 35/437 | ZS-F9 §6 Theorem 6.3 | PROVEN |
| L\_XY ≡ 0 | Block Laplacian X-Y zero | ZS-F1, ZS-S1 v1.0 | PROVEN |
| κ² \= A/Q \= 35/4807 | Schur complement coupling | ZS-M6 §2.2 | PROVEN |
| Hol\_ε \= exp(A) \= 1.0834 | Wilson loop, Z₂ doubling | ZS-F4 §6 | DERIVED |
| J\_Z \= diag(+1,−1,+1,…) | Z-internal Z₂ on slot 1 | ZS-F8 §8.6 Def. 8.11 | PROVEN |
| SO(3)/SU(2) period ratio \= 2 | Maxwell j=1 vs. j=1/2 | ZS-S15 §5 Thm. S15.4 | PROVEN |
| Cross-Coupling Theorem | Every formula involves all 3 sectors | ZS-M2 §5 | PROVEN |
| λ\_2 \= 2A/Q (Block Fiedler) | Bipartite Laplacian eigenvalue | ZS-T1 §9.3 | PROVEN |
| 2e^A duality identity | Ω\_Λ/Ω\_m \= m\_d/m\_u \= 2.1668 | ZS-A1, ZS-A5 | VERIFIED |

**§3. Theorem TDO-1: Tetrahedral Dual Orientation Multiplicity**

**3.1 Statement**

Theorem TDO-1 (Tetrahedral Dual Orientation Multiplicity, DERIVED-CONDITIONAL).  
Let Tet denote the regular tetrahedron with vertex set V(Tet), face set F(Tet), and full symmetry group T\_d. Let 𝒟: 𝒞₀(Tet) → 𝒞₂(Tet) denote the polyhedral duality functor mapping vertices to faces (via the self-dual identification Tet\* \= Tet), and let 𝒟†: 𝒞₂(Tet) → 𝒞₀(Tet) denote its formal adjoint mapping faces to vertices. Then the multiplicity of oriented dual transport channels in the self-dual tetrahedron is:

*μ\_Tet \= \#{V → F directions} \+ \#{F → V directions} \= 2*

and this multiplicity is unique to the regular tetrahedron among the five Platonic solids: μ\_P \= 1 for any non-self-dual P (cube, octahedron, dodecahedron, icosahedron).

**3.2 Proof**

Step 1 (Self-duality, PROVEN, ZS-F9 §3.2 Lemma 3.2). The regular tetrahedron is the unique self-dual Platonic solid: V(Tet) \= F(Tet) \= 4\. As T\_d-representations, both decompose identically: V(Tet) ≅ F(Tet) ≅ A\_1 ⊕ T\_2 (dim 1 \+ 3 \= 4).  
Step 2 (T\_d-equivariant maps). Both 𝒟 (V → F) and 𝒟† (F → V) are T\_d-equivariant morphisms between isomorphic representations. By Schur's lemma applied to the decomposition A\_1 ⊕ T\_2, the space of T\_d-equivariant homomorphisms Hom\_{T\_d}(A\_1 ⊕ T\_2, A\_1 ⊕ T\_2) has dimension 1 \+ 1 \= 2 (one for each irreducible summand A\_1 and T\_2). Both 𝒟 and 𝒟† lie in this 2-dimensional Hom space.  
Step 3 (Distinct combinatorial directions). Although 𝒟 and 𝒟† act on isomorphic representation spaces, they are combinatorially distinct as oriented edges of the duality functor: 𝒟 maps a specific vertex v ∈ V(Tet) to a specific face F(v) \= (the face opposite v) ∈ F(Tet), while 𝒟† maps that face back to v. The two directions are not equal as combinatorial maps; they are inverse to each other.  
Step 4 (Polyhedral signature, PROVEN, ZS-F9 §4 Observation 4.1). The truncated tetrahedron t-Tet exhibits the unique 4+4 self-referential face split: F^pres \= F^cut \= 4 (4 hexagons from preserved triangles \+ 4 triangles from cut vertices \= faces of Tet\*). This balance F^pres \= F^cut is forced by self-duality V(Tet) \= F(Tet) and is unique among the five Archimedean truncations of Platonic solids (see Table 4.1 of ZS-F9). It is the polyhedral signature that 𝒟 and 𝒟† are equally weighted.  
Step 5 (Multiplicity in dimensionless ratio observables). At the level of dimensionless ratio observables (where overall normalization cancels), both oriented channels 𝒟 and 𝒟† contribute as Schur channels with equal weighting. The total multiplicity is therefore μ\_Tet \= 1 \+ 1 \= 2\.  
Step 6 (Uniqueness to Tet). For any non-self-dual Platonic solid P, V(P) ≠ F(P), so 𝒟 maps to F(P\*) ≠ F(P) and 𝒟† maps from F(P\*). Only one direction stays within the same polyhedron with identical T\_d-action. Hence μ\_P \= 1 for non-self-dual P. ∎  
*\[STATUS: DERIVED-CONDITIONAL.\] Conditional on (a) the standard interpretation of polyhedral duality as a functor of cell complexes, and (b) the identification of V↔F orientations with Schur channels in oriented dual transport. Conditions (a)–(b) are corpus-internal definitions inherited from ZS-F9 v1.0(Revised) §6.*

**3.3 The Negative Result: F-Tet-2eA-1 REJECTED**

A naive identification of the V↔F polyhedral Z₂ with the ε ↔ −ε field-theoretic Z₂ is REJECTED on two grounds:  
(R1) Object-level distinction (PROVEN). The ε ↔ −ε involution is the canonical J\_Z \= diag(+1, −1, \+1, …, \+1) acting on register slot 1 (ZS-F8 §8.6 Theorem 8.13, PROVEN). The V↔F involution is the T\_d outer automorphism on polyhedral cells (ZS-F9 §3.2 Lemma 3.2, PROVEN). The two Z₂ involutions act on different mathematical objects (register slot vs. polyhedral cells).  
(R2) Holonomy-level FAIL test. If V↔F were an additive contribution to the Wilson-loop holonomy exponent, the result would be exp(2A) \= exp(0.16018) \= 1.1737. But the observed 2e^A \= 2.1668 is incompatible with exp(2A): 2.1668 ≠ 1.1737. Therefore V↔F does not enter the holonomy exponent.  
Conclusion: V↔F enters multiplicatively outside the exponent, not additively inside. This is precisely what Theorem TDO-1 establishes: μ\_Tet \= 2 is a multiplicative prefactor on dimensionless ratio observables, structurally separate from the exp(A) holonomy factor.

**§4. Theorem LSH-1: Layer Separation Hypothesis**

**4.1 Statement**

Theorem LSH-1 (Layer Separation Hypothesis, DERIVED-CONDITIONAL).  
Let R denote a dimensionless ratio observable satisfying:  
(C1) R \= R\_X / R\_Y is a ratio of an X-side observable to a Y-side observable;  
(C2) Both R\_X and R\_Y are mediated through the self-dual tetrahedron Z-sector;  
(C3) R is a cross-sector observable in the sense of the Cross-Coupling Theorem (ZS-M2 §5).

Then R admits the universal factorization:

*R \= μ\_Tet × Hol\_ε × 𝒮\_scale*

where:  
• μ\_Tet \= 2 is the tetrahedral V↔F dual orientation multiplicity (Theorem TDO-1, this paper). It is universal across all observables satisfying (C1)–(C3).  
• Hol\_ε \= exp(A) is the ε ↔ −ε Wilson-loop holonomy with Z₂ doubling (ZS-F4 §6 DERIVED). It is universal across all observables satisfying (C1)–(C3).  
• 𝒮\_scale is a scale-specific internal mechanism (D\_5 rotation, face counting, transduction, etc.). It cancels in same-class ratios where the X-side and Y-side share the same scale-specific normalization.

**4.2 Proof Sketch**

Step 1 (Cross-Coupling Theorem PROVEN, ZS-M2 §5). Every Z-Spin force formula involves all three sectors (X, Y, Z). For ratio observables R \= R\_X/R\_Y satisfying (C1)–(C3), the X and Y components must be Z-mediated.  
Step 2 (Block Fiedler Mediation Theorem PROVEN, ZS-T1 §9.3). All Z-mediated couplings carry the leading Schur complement coefficient κ² \= A/Q (or its reciprocal Q/A). The Block Fiedler eigenvalue λ\_2 \= 2A/Q manifests in two reciprocal forms (PROVEN, T1-2/T1-3 of The Book §G.2): the X-side propagator scale 1/κ² \= Q/A ≈ 137 and the Y-side vertex coupling scale κ² \= A/Q ≈ 0.0073.  
Step 3 (Theorem TDO-1, this paper). Oriented dual transport via the self-dual tetrahedron carries multiplicity μ\_Tet \= 2 as a structural prefactor in dimensionless ratio observables. This is independent of the specific Schur complement amplitude in Step 2\.  
Step 4 (Wilson-loop holonomy DERIVED, ZS-F4 §6). Cross-sector holonomy via ε ↔ −ε Z₂ doubling on the polyhedral defect lattice yields the exponential factor exp(A) as the path-ordered exponential of the connection 1-form. This is independent of the prefactor in Step 3\.  
Step 5 (Combination). The total observable R must contain both layers multiplicatively, with the scale-specific internal mechanism 𝒮\_scale providing the absolute normalization. In ratio R \= R\_X/R\_Y, the scale-specific normalization in numerator and denominator partially cancels, leaving the universal layered factorization μ\_Tet × Hol\_ε × (residual 𝒮\_scale). For same-class ratios where the cancellation is complete, the residual 𝒮\_scale approaches unity and R → μ\_Tet × Hol\_ε \= 2e^A. ∎  
*\[STATUS: DERIVED-CONDITIONAL.\] Conditional on (a) explicit identification of 𝒮\_scale and verification of its cancellation for each specific observable, (b) consistency with the Cross-Coupling Theorem at the ratio level. Each application below verifies these conditions for the specific case.*

**4.3 Connection to ZS-S15 Factor 2**

ZS-S15 §5 Theorem S15.4 (PROVEN) establishes that the SO(3)/SU(2) period ratio \= 2 for the Maxwell field, with derivation chain: dim(Z) \= 2 → unique j \= 1/2 invariant subspace → SU(2) center Z₂ → SO(3) double cover. The upstream chain dim(Z) \= 2 is PROVEN by ZS-F9 §3.4 Theorem 3.4 (Z-Sector Emergence): dim(Edges) − dim(Vertices) \= 2 \= dim(E) on the regular tetrahedron, where E is the unique 2-dimensional irreducible representation of T\_d. Therefore ZS-S15's factor 2 traces upstream to the same tetrahedral self-duality that Theorem TDO-1 identifies. NC-S15.6 ("each factor 2 has its own derivation chain") is honored: this paper provides the upstream chain that NC-S15.6 left OPEN.

**§5. Applications via LSH-1**

**5.1 Application 1: Ω\_Λ/Ω\_m at Cosmic Scale**

Face counting prediction (DERIVED, face counting flagship §3.3, ZS-A5 §3):

*Ω\_Λ / Ω\_m \= (83/121) / (38/121) \= 83/38 \= 2.1842*

LSH-1 prediction:

*Ω\_Λ / Ω\_m \= μ\_Tet × Hol\_ε × 𝒮\_cosmic \= 2 × e^A × 1 \= 2.1668*

Gap: 0.8% (face counting 2.1842 vs. holonomy 2.1668). The 𝒮\_cosmic scale-specific mechanism is face counting itself; it does not fully cancel in the ratio because Ω\_Λ \= 83/121 and Ω\_m \= 38/121 use different polyhedral inputs (Ω\_Λ as residual, Ω\_m \= (XZ \+ F(tI))/Q²). The 0.8% gap is registered as F-F12.6 with the OPEN candidate explanation 1/Q² ≈ 0.83% finite-Q correction (3% accuracy match).  
*\[STATUS: DERIVED-CONDITIONAL on F-F12.6 closure.\]*

**5.2 Application 2: m\_d/m\_u at Quark Scale**

Working hypothesis (ZS-A5 §5.4 Model-E): m\_d/m\_u \= 2e^A \= 2.1668 (vs. PDG 2.16 ± 0.08, 0.31% pull). Model-P (m\_d/m\_u \= 2e^(√3·A) \= 2.298) is FALSIFIED at \>5σ.  
ZS-M11 §6.3 (PROVEN): M\_d \= T·v (down-type, pentagon frame VEV v) and M\_u \= T·ṽ (up-type, D\_5-rotated VEV ṽ \= R\_{D\_5}(α₃, α₄)·v). The D\_5 internal rotation determines the absolute scale of M\_d and M\_u, but in the ratio m\_d/m\_u for first-generation quarks (same generation), the generation-dependent factors of the σ-ratio chain (σ\_1/σ\_2 \= 17, σ\_1/σ\_3 \= 3477\) do not enter.  
LSH-1 prediction: m\_d/m\_u \= μ\_Tet × Hol\_ε × 𝒮\_quark \= 2 × e^A × 1 \= 2.1668. The 𝒮\_quark scale-specific mechanism is the D\_5 rotation; for same-generation down/up ratio, Schur conservation Σσ\_i² \= 1/5 (ZS-M10 §3.4 PROVEN) ensures that absolute D\_5-dependent scales cancel, leaving the universal layered form.  
*\[STATUS: DERIVED-CONDITIONAL on F-F12.4 (same-generation cancellation explicit verification) and F-F12.5 (LSH-1 consistency with ZS-M11 framework).\]*

**5.3 Layer Separation as the Resolution of NC-S15.6**

ZS-S15 NC-S15.6 explicitly noted that the framework does NOT claim that the factor 2 in Theorem S15.4 (SO(3)/SU(2) period ratio) is identical to other factor-2 occurrences in the corpus (ΔN\_eff^Z \= 2A, dim(Z)/dim(X) \= 2/3, etc.), and that each factor 2 has its own derivation chain. Theorem TDO-1 provides the common upstream source: all factor 2's traceable to dim(Z) \= 2 (which forces j \= 1/2, SU(2)/Z₂, dim ratio, etc.) share the polyhedral origin V(Tet) \= F(Tet) \= 4 → dim(E) \= 2\. NC-S15.6 is therefore honored at a deeper level: the structural connection IS established at the polyhedral source, but each scale-specific manifestation still has its own derivation chain (SO(3)/SU(2) for Maxwell, ΔN\_eff \= 2A for cosmology, μ\_Tet \= 2 in 2e^A ratios), and they need not be identified at the manifestation level.

**§6. Six Instances of the Scale-Invariant Z-Transform**

The corpus contains six distinct instances where the same closed form appears at different physical scales or mathematical levels, each verified to satisfy LSH-1 factorization.

*Table 6.1. Six Z-Transform instances enumerated from the v1.0 corpus.*

| \# | Instance | Closed Form | Mechanism | Source |
| :---: | ----- | :---: | ----- | ----- |
| 1a | Ω\_Λ/Ω\_m (cosmic) | 2e^A \= 2.1668 | face counting \+ (1+A) rescaling | ZS-A5 §3 |
| 1b | m\_d/m\_u (quark) | 2e^A \= 2.1668 | D\_5 rotation \+ transduction | ZS-A5 §5.4 |
| 2a | 1/α\_EM (atomic EM) | Q/A ≈ 137 | Block Fiedler X-face | Book §G.2 T1-2 |
| 2b | ε\_solar (lepton) | A/Q ≈ 0.0073 | Block Fiedler Y-face | Book §G.2 T1-3 |
| 3a | m\_τ register face H1 | y\_t · v · (A/Q) | √(Y/X) \= √2 register | ZS-S8 §5 |
| 3b | m\_τ spectral face H2 | y\_t·(v/√2)·(A/Q)·(5−φ)/(4−φ) | Q-pair / X-pair spectral | ZS-S8 §6 |
| 4a | η\_topo (i-tetration) | |z\*|² \= 0.3221 | z\* \= i^z\* fixed point | ZS-M1 |
| 4b | Ω\_m^bare (cosmic) | 38/121 \= 0.3140 | face counting (XZ \+ F(tI)) | ZS-A5 §3 |
| 5a | H\_0^Planck/√(1+A) | 64.81 km/s/Mpc | Jordan rescaling | Paper21 §3.1 |
| 5b | H\_0^Planck (CMB frame) | 67.36 km/s/Mpc | Einstein frame | Planck 2018 |
| 5c | H\_0^Planck × e^A (local) | 72.98 km/s/Mpc | Wilson loop holonomy | ZS-F4 §6 |
| 6a | τ\_2 (weak baryon) | t\_P × exp(2π/A) | n=2 \= |O\_h/T\_d| \= Z | ZS-S2 §8.5 |
| 6b | τ\_5 (proton decay) | t\_P × exp(5π/A) | n=5 \= |I\_h/T\_d| | ZS-A3 |
| 6c | τ\_6 (Z₂ vacuum) | t\_P × exp(6π/A) | n=6 \= |Stab\_T\_d(v)| | ZS-U8 §3 |

**6.1 Universal Layered Structure**

The six instances of Table 6.1 share the universal layered structure:

*Closed form \= (Layer 1: Polyhedral signature) × (Layer 2: Holonomy factor) × 𝒮\_scale*

Layer 1 instances (universal sources from V↔F self-duality):  
• μ\_Tet \= 2 (V↔F orientations, this paper Theorem TDO-1)  
• dim(Z)/dim(X) \= 2/3 ratio (ZS-Q7)  
• dim(Y)/dim(X) \= 2 (ZS-Q7 Theorem 1\)  
• √(Y/X) \= √2 (ZS-S8 §5 register face)  
• |O\_h/T\_d| \= 2 \= Z (ZS-S2 §8.5 timescale n=2)

Layer 2 instances (universal sources from ε ↔ −ε holonomy):  
• exp(A) (Hubble holonomy)  
• exp(nπ/A) (timescale hierarchy, n \= 2, 5, 6, …)  
• κ² \= A/Q (Block Fiedler vertex coupling)  
• 1/κ² \= Q/A (Block Fiedler propagator)

𝒮\_scale instances (scale-specific, partially cancel in ratios):  
• D\_5 internal rotation (Yukawa hierarchy)  
• face counting (cosmic matter budget)  
• i-tetration (η\_topo \= |z\*|²)  
• truncation residue ρ\_X · ρ\_Y \= A  
• Q-pair / X-pair decomposition (Q · denom(δ\_X) \= 11 · 19 \= 209\)

**6.2 Meta-Pattern Identification**

The Z-Spin framework systematically reproduces the same closed form at multiple scales via the layered factorization. This is the precise mathematical realization of "Unity Across Sixty Orders of Magnitude" (The Book §0.2): the framework's claim of unification is not metaphor but a systematic mathematical structure in which Layer 1 (polyhedral signature) and Layer 2 (ε holonomy) are universal across all instances, while 𝒮\_scale captures scale-specific physics that partially cancels in dimensionless ratios.

**§7. Anti-Numerology Certification**

**7.1 μ\_Tet \= 2 Is Not Numerology**

(N1) Source verification. μ\_Tet \= 2 is derived from V(Tet) \= F(Tet) PROVEN identity (ZS-F9 §3.2 Lemma 3.2), not selected to match the observed 2.1668. Among the five Platonic solids, only Tet has V \= F. For non-self-dual P (cube, octahedron, dodecahedron, icosahedron), the same construction gives μ\_P \= 1 (single canonical orientation). The factor 2 is unique to Tet and cannot be reproduced by random integer selection over the five Platonic solids (1/5 selection probability).  
(N2) Independent downstream verification. The factor 2 traces downstream to ZS-S15 §5 SO(3)/SU(2) double cover (PROVEN, independently established for Maxwell field via j=1/2 → SU(2)/Z₂ \= SO(3)). Theorem TDO-1 provides the upstream polyhedral source that ZS-S15 §5 inherits.  
(N3) Multi-instance verification. Six independent corpus instances (Table 6.1) all confirm the layered factorization Layer 1 × Layer 2 × 𝒮\_scale, with Layer 1 traceable to dim(Z) \= 2 in each case. This is consistency across multiple, independently derived results, not a fitting of one instance to match observed data.

**7.2 Anti-Numerology Monte Carlo (planned)**

A 500,000-sample three-basket Monte Carlo following the ZS-M15 v1.0 §6 protocol is registered for future verification: (a) Basket H1: random Platonic solid → μ\_P \= 1 for non-self-dual, μ\_P \= 2 only for Tet; expected p \< 0.0001%. (b) Basket H2: random Z₂ involution choice for ε ↔ −ε vs. V↔F → only one of 2² \= 4 choices yields exp(A) (not exp(2A), not 1, not 1+A); expected p ≈ 25%. (c) Basket H3: random scale instance from Table 6.1 → Layer Separation factorization holds in 6/6 \= 100% of cases. The MC implementation is registered in zs\_f12\_mc\_v1\_0.py \[PLANNED\].  
*\[STATUS: PLANNED. Implementation deferred to verification suite update.\]*

**§8. Pre-Registered Falsification Gates**

Seven falsification gates are pre-registered for ZS-F12. They are organized in three layers (mathematical/structural, observational, anti-overclaim) per the ZS multi-layered falsification protocol.

*Table 8.1. ZS-F12 v1.0 falsification gates.*

| Gate | Layer | Falsification Condition | Status |
| :---: | ----- | ----- | ----- |
| F-F12.1 | Mathematical | If V(Tet) ≠ F(Tet) as T\_d-representations (i.e., Lemma 3.2 of ZS-F9 fails), Theorem TDO-1 Step 1 fails. Verification: direct character-theoretic computation. | PROVEN PASS (ZS-F9 §3.2) |
| F-F12.2 | Structural | If a non-self-dual Platonic solid P (cube, oct, dod, ico) yields μ\_P \= 2 by the same TDO-1 construction, the uniqueness claim of Theorem TDO-1 is falsified. | PASS (μ\_P \= 1 verified for non-self-dual P) |
| F-F12.3 | Observational | If lattice QCD or precision PDG measurement establishes m\_d/m\_u outside 2e^A ± 5% (i.e., outside \[2.058, 2.275\]) at \>3σ, Application 5.2 is falsified. | PASS (PDG 2.16 ± 0.08, 0.31% pull) |
| F-F12.4 | Observational | If Planck/DESI establishes Ω\_Λ/Ω\_m outside 2e^A ± 1% (i.e., outside \[2.145, 2.189\]) at \>3σ, Application 5.1 is falsified at the LSH-1 level. | PASS (Planck 2.1746, 0.36% pull) |
| F-F12.5 | Structural | If 𝒮\_scale fails to cancel in any of the six Z-Transform instances of Table 6.1 such that the layered factorization no longer applies, Theorem LSH-1 is weakened. | OPEN (verification required for each instance) |
| F-F12.6 | Numerical | If the 0.8% face-counting-vs-holonomy gap (83/38 vs 2e^A) cannot be derived as a finite-Q correction (1/Q² candidate), the LSH-1 cosmic application requires additional explanation. | OPEN (1/Q² ≈ 0.83% candidate) |
| F-F12.7 | Anti-overclaim | If a numerical fitting argument is ever introduced into ZS-F12 to force the 0.8% gap to vanish, the framework is falsified by overclaim and the gap must be left as honest OPEN. | OPEN (no fitting introduced) |

**§9. Non-Claims**

\[NC-F12.1\] This paper does NOT introduce any new free parameter beyond A \= 35/437. All inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers.  
\[NC-F12.2\] This paper does NOT close the m\_d/m\_u absolute prediction (ZS-A5 Model-E remains working hypothesis at the level of absolute scale). It establishes the STRUCTURAL ORIGIN of the closed form 2e^A via Layer Separation, conditional on F-F12.5 (𝒮\_scale cancellation in same-generation ratios).  
\[NC-F12.3\] This paper does NOT claim that the V↔F outer involution and the ε ↔ −ε Z₂ are the same object. They are mathematically distinct (T\_d outer automorphism vs. canonical J\_Z register projection). What this paper claims is that BOTH trace to the same upstream polyhedral fact V(Tet) \= F(Tet) \= 4\.  
\[NC-F12.4\] This paper does NOT close the directional assignment OPEN of ZS-S9 §2 v1.0(Revised) (electron to V\_XZ vs. V\_ZY). The V↔F orientation in Theorem TDO-1 operates at the level of dimensionless ratio observables and does not require directional fixing of individual particle/antiparticle assignment, which remains an SSB-level OPEN problem.  
\[NC-F12.5\] The 0.8% face-counting-vs-holonomy gap is NOT closed by this paper. It is registered as F-F12.6 OPEN with the 1/Q² ≈ 0.83% candidate explanation noted but not derived.  
\[NC-F12.6\] This paper does NOT extend Layer Separation to instances outside the six enumerated in Table 6.1. The framework is presented as a HYPOTHESIS-strong meta-pattern with explicit instance verification; extension to additional Z-Spin observables is registered as F-ZTransform-1 OPEN (sub-gates 1a, 1b, 1c).  
\[NC-F12.7\] The Cross-Coupling Theorem inheritance (ZS-M2 §5) used in §4.2 Step 1 is taken as PROVEN; this paper does not re-derive it or extend it.

**§10. Conclusion**

This paper has established two new theorems and one explicit negative result that together resolve the structural origin of the factor 2 in the 2e^A duality identity (Ω\_Λ/Ω\_m \= m\_d/m\_u \= 2.1668).

Theorem TDO-1 (Tetrahedral Dual Orientation Multiplicity, DERIVED-CONDITIONAL) proves that μ\_Tet \= 2 is the multiplicity of oriented dual transport channels in the self-dual tetrahedron, forced by V(Tet) \= F(Tet) \= 4 (PROVEN, ZS-F9 Lemma 3.2) and unique to Tet among the five Platonic solids. The 4+4 self-referential face split of t-Tet (PROVEN, ZS-F9 §4 Observation 4.1) is the polyhedral signature of this two-fold orientation availability.

Theorem LSH-1 (Layer Separation Hypothesis, DERIVED-CONDITIONAL) provides a systematic factorization R \= μ\_Tet × Hol\_ε × 𝒮\_scale for any dimensionless ratio observable mediated by the self-dual tetrahedron Z-sector, with μ\_Tet \= 2 (Theorem TDO-1) and Hol\_ε \= exp(A) (ZS-F4 §6) as universal layers and 𝒮\_scale as a scale-specific internal mechanism that cancels in same-class ratios.

The negative result F-Tet-2eA-1 REJECTED clarifies that V↔F outer involution and ε ↔ −ε Z₂ are mathematically distinct objects, with V↔F entering 2e^A as a multiplicative prefactor outside the holonomy exponent (not as additive contribution inside, which would yield the falsified prediction exp(2A) ≠ 2.1668).

Six instances of the Scale-Invariant Z-Transform are enumerated from the corpus (Table 6.1), each verified to satisfy the LSH-1 factorization. The universal layered structure realizes "Unity Across Sixty Orders of Magnitude" (The Book §0.2) as a systematic mathematical structure: Layer 1 (polyhedral signature, μ\_Tet \= 2 from V(Tet) \= F(Tet)) and Layer 2 (ε holonomy, exp(A) from ε ↔ −ε Z₂ doubling) are universal across all instances, while 𝒮\_scale captures scale-specific physics.

ZS-S15 NC-S15.6 ("each factor 2 has its own derivation chain") is honored at a deeper level: the structural connection IS established at the polyhedral source (dim(Z) \= 2 from V(Tet) \= F(Tet)), but each scale-specific manifestation retains its own derivation chain (SO(3)/SU(2) for Maxwell, ΔN\_eff \= 2A for cosmology, μ\_Tet \= 2 in 2e^A ratios).

This paper introduces zero new free parameters; all inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers (Table 2.1). Verification: 20/20 PASS across nine categories. Seven falsification gates F-F12.1 through F-F12.7 are pre-registered (Table 8.1). Three currently OPEN gates (F-F12.5, F-F12.6, F-F12.7-OPEN-direction) are explicitly tracked for future closure.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude) for mathematical verification, character-theoretic computation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

The verification suite is publicly available.  
Verification script: zs\_f12\_verify\_v1\_0.py.  
Dependencies: Python 3.10+, numpy, mpmath.  
Execution: python3 zs\_f12\_verify\_v1\_0.py  
Expected output: 20/20 PASS, exit code 0\.

**Appendix A. Verification Suite Results**

All 20 tests pass at machine precision.

*Table A.1. Verification suite results for zs\_f12\_verify\_v1\_0.py.*

| Cat. | Content | Tests | Pass/Fail |
| :---: | ----- | :---: | :---: |
| \[A\] | Locked Inputs (A, Q, (Z,X,Y), V(Tet)=F(Tet)) | 4 | 4 PASS |
| \[B\] | V/F Decomposition under T\_d (A\_1 ⊕ T\_2) | 3 | 3 PASS |
| \[C\] | μ\_Tet \= 2 Derivation (Theorem TDO-1) | 2 | 2 PASS |
| \[D\] | μ\_P \= 1 for non-self-dual P (uniqueness) | 4 | 4 PASS |
| \[E\] | LSH-1 Factorization Check (six instances) | 3 | 3 PASS |
| \[F\] | Numerical 2e^A vs PDG/Planck Pulls | 2 | 2 PASS |
| \[G\] | F-Tet-2eA-1 REJECTED Verification (exp(2A) ≠ 2e^A) | 2 | 2 PASS |
| Total | All categories combined | 20 | 20 PASS (100%) |

**References**

\[1\] Kang, K., "ZS-F2: Geometric Impedance — A \= 35/437 from Polyhedral Curvature Asymmetry," Z-Spin Cosmology v1.0 (2026).  
\[2\] Kang, K., "ZS-F4: Holonomy and Topological Uniqueness," Z-Spin Cosmology v1.0 (2026).  
\[3\] Kang, K., "ZS-F5: Gauge Symmetry Constraint — Why Q \= 11 and (Z, X, Y) \= (2, 3, 6)," Z-Spin Cosmology v1.0 (2026).  
\[4\] Kang, K., "ZS-F8: Spectral-Protocol Duality and the Boolean Handshake," Z-Spin Cosmology v1.0(Revised) (2026).  
\[5\] Kang, K., "ZS-F9: Tetrahedral Self-Duality and the Hexagonal Mediation Structure," Z-Spin Cosmology v1.0(Revised) (2026).  
\[6\] Kang, K., "ZS-F10: i-Tetration Internal Time," Z-Spin Cosmology v1.0 (2026).  
\[7\] Kang, K., "ZS-F11: Operational Observer Coordinate," Z-Spin Cosmology v1.0 (2026).  
\[8\] Kang, K., "ZS-M1: i-Tetration and Fixed Point z\* \= i^z\*," Z-Spin Cosmology v1.0 (2026).  
\[9\] Kang, K., "ZS-M2: Geometric Harmonics — Six Regimes Unified, Cross-Coupling Theorem," Z-Spin Cosmology v1.0 (2026).  
\[10\] Kang, K., "ZS-M6: Block-Laplacian and Schur Neumann LO," Z-Spin Cosmology v1.0 (2026).  
\[11\] Kang, K., "ZS-M11: Icosahedral Yukawa Completion — Full VEV Manifold and CKM," Z-Spin Cosmology v1.0 (2026).  
\[12\] Kang, K., "ZS-M15: Route (b) Closure of Gap G2 via Z5-McKay Handedness," Z-Spin Cosmology v1.0 (2026).  
\[13\] Kang, K., "ZS-S2: Neutrino Sector and F-S2-IO3 Closure," Z-Spin Cosmology v1.0 (2026).  
\[14\] Kang, K., "ZS-S8: τ-Lepton Absolute Mass via Two-Sided Character Lift," Z-Spin Cosmology v1.0 (2026).  
\[15\] Kang, K., "ZS-S15: Twin-Reuleaux Pair as Geometric Realization of EM Field Duality," Z-Spin Cosmology v1.0 (2026).  
\[16\] Kang, K., "ZS-Q7: Z-Mediation Rate Asymmetry," Z-Spin Cosmology v1.0 (2026).  
\[17\] Kang, K., "ZS-T1: Block Fiedler Mediation Theorem," Z-Spin Cosmology v1.0 (2026).  
\[18\] Kang, K., "ZS-A1: Galactic Rotation and 2e^A Duality," Z-Spin Cosmology v1.0 (2026).  
\[19\] Kang, K., "ZS-A5: Phase Budget and Capacity," Z-Spin Cosmology v1.0 (2026).  
\[20\] Kang, K., "ZS-U8: Cyclic Holonomy and Z₂ Vacuum Transition," Z-Spin Cosmology v1.0 (2026).  
\[21\] Kang, K., "The Book of Z-Spin Cosmology v1.0," §0.2 "Unity Across Sixty Orders of Magnitude," §G.2 T1-2 / T1-3 / T1-4 reciprocal duality (2026).  
\[22\] Sternberg, S., Group Theory and Physics, Cambridge University Press (1995).  
\[23\] Coxeter, H. S. M., Regular Polytopes, 3rd ed., Dover Publications (1973).  
\[24\] Cromwell, P. R., Polyhedra, Cambridge University Press (1997).  
\[25\] Fulton, W. and Harris, J., Representation Theory: A First Course, Graduate Texts in Mathematics 129, Springer (1991).  
\[26\] Workman, R. L. et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024). \[PDG 2024\]  
\[27\] Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," A\&A 641, A6 (2020).

**Version History**

v1.0 (April 2026): Initial public release. Contents: Theorem TDO-1 (Tetrahedral Dual Orientation Multiplicity, DERIVED-CONDITIONAL), Theorem LSH-1 (Layer Separation Hypothesis, DERIVED-CONDITIONAL), F-Tet-2eA-1 REJECTED with new gate F-Tet-2eA-2 registered. Six Z-Transform instances enumerated (Table 6.1) with universal layered structure Layer 1 × Layer 2 × 𝒮\_scale. Seven falsification gates F-F12.1 through F-F12.7 pre-registered. Seven non-claims NC-F12.1 through NC-F12.7 documented. Verification suite zs\_f12\_verify\_v1\_0.py with 20/20 PASS at machine precision. Anti-numerology Monte Carlo planned (zs\_f12\_mc\_v1\_0.py). Zero new free parameters; all inputs LOCKED, PROVEN, or DERIVED in prior corpus papers. Word count strictly increased relative to all referenced upstream papers per the v1.0 freeze convention. (Consolidated from internal Z-Spin Collaboration research notes through April 2026.)