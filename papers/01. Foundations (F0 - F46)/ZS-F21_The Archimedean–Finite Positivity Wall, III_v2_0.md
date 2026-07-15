**ZS-F21**

**The Archimedean–Finite Positivity Wall, III: The Commutant-Gate Insufficiency Theorem, External Boundary-Selector Imports, and the V₄-Decorated Sonin–Frobenius Construction over the Connes–Katsnelson Prolate Realization**

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Date:** March 2026  
**Theme / Paper Code:** Foundations \[ZS-F\] | ZS-F21 | v2.0

**Verification: 34/34 PASS | Zero Free Parameters | Theorem C3.0 proved (analytic \+ 200/200 empirical) | Four external imports (Connes 1998, Katsnelson 2016, Connes–Moscovici 2022, Ramis–Richard-Jung–Thomann 2025\) | Six anti-numerology controls (five rejected candidates withdrawn) | Lemma M31.0 Non-Separability obstruction certified.**

**§0. Abstract**

This paper completes a thirteen-stage deep exploration of D4c — the central open gate of the Z-Spin archimedean–finite positivity programme — by isolating what can be closed honestly and what remains genuinely open. The contribution divides into four parts. (i) Theorem C3.0 (Commutant-Gate Insufficiency, PROVEN here): if A \= Π\_λ Π\_F Π\_λ is the Slepian concentration operator, then every Borel functional f(A) is self-adjoint and lies in the commutant of A; consequently hermiticity and Slepian-commutation cannot uniquely select the Connes–Katsnelson prolate realization W\_{λ,sa}. (ii) External imports T4–T5: the explicit boundary condition lim\_{q→±λ}(q²−λ²)∂\_qξ(q) \= 0 (Connes 1998 Lemma 6), the Fourier-commuting uniqueness (Katsnelson 2016), the discrete two-sided unbounded spectrum (Connes–Moscovici 2022), and — settling a 2022 CCM conjecture — the negativity of all non-classical eigenvalues plus the imaginary-axis characterization (Ramis–Richard-Jung–Thomann 2025\) are imported as a single block. (iii) V₄-decoration (T6d): the ramified channels χ₋₃, χ₋₁₁, χ₃₃ are not represented by rescaled prolate parameters Λ\_χ \= Λ√(q\_χ) (withdrawn as fitted) but by Burnol conductor blocks C\_χ \= Σ\_{p|q\_χ} e\_p(χ)·log p \= log q\_χ on the common Connes–Katsnelson Sonin space. This decoration is canonical (an identity of integer factorization) and matches Tate’s analytic conductor (q\_χ/π)^{(s+a\_χ)/2}. (iv) Diagnosis of the direct-sum closure (T7): a pure channelwise direct sum Q^{def} \= Σ\_χ Tr(D\_χ† D\_χ) is trivially PSD but cannot equal the actual V₄-decorated Weil form, since the corpus Probe-W2 data show each non-trivial channel is individually indefinite (χ₋₃: 6/12, χ₋₁₁: 9/12, χ₃₃: 7/12 negative grids) — and pure direct sums violate Lemma M31.0 (Non-Separability, PROVEN). The improved replacement T7′ retains the Reading-C Π\_Z-sandwich while absorbing the Burnol decoration into the channelwise test factor γ\_χ(s). No claim of full Weil positivity or RH/GRH is asserted at any stage. Verification: 34/34 PASS, six pre-registered anti-numerology controls.

*Keywords: Connes–Katsnelson prolate realization, Sonin space, commutant gate, Slepian concentration operator, Connes 1998 boundary condition, Ramis–Richard-Jung–Thomann 2025, Burnol conductor operator, Tate analytic conductor, V₄ character decoration, Reading-C non-separability, Lemma M31.0, anti-numerology*

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Theorem with complete proof verifiable here (analytic \+ machine-witness). |
| **IMPORTED-PROVEN** | External theorem with full reference; used without re-derivation. |
| **DERIVED** | Follows from LOCKED \+ IMPORTED inputs by an identity or definition. |
| **DERIVED-CONDITIONAL** | Follows once the listed imports are in force. |
| **LOCKED** | Constant or structural datum carried in from prior corpus papers. |
| **DEFINITIONAL** | A choice of name or notation that creates no new content. |
| **NON-CLAIM (NC)** | Explicit statement of what is not asserted. |
| **OPEN** | Recognized gap whose closure object is precisely identified. |
| **WITHDRAWN** | Candidate identity that anti-numerology has retired. |
| **REJECTED** | A candidate identity refuted by a controlled test. |

**§1. Position Relative to ZS-F21 v1.2**

ZS-F21 v1.2 reduced the archimedean–finite wall to two precise objects: the Positive-Square Criterion (F21.9, PROVEN both directions — Q\_W,S ≥ 0 if and only if Q\_W,S admits the representation ‖Π\_S(H\_∞ \+ iH\_fin,S)Π\_S f‖² \+ R\_S(f) with R\_S ≥ 0\) and the Commutator-Coverage Obstruction (F21.10, PROVEN negative — the third-axis commutator does not canonically select B). The criterion located the actual closure gate at the Connes–Consani–Moscovici (CCM) compressed-scaling representation; the obstruction rejected the F18-style commutator shortcut. This paper supplies the next layer: an honest evaluation of the boundary-selector route to that representation, with all external machinery now identified and imported by name, and with the Z-Spin contribution kept where it belongs — in the channel decoration, not in re-discovering archimedean theorems.

**§2. Locked Inputs**

*Table 2.1. LOCKED constants and structural data (carried in from prior corpus).*

| Symbol | Definition | Source / status |
| ----- | ----- | ----- |
| **A; (Z,X,Y); Q** | 35/437; (2,3,6); 11 | ZS-F2; ZS-F5 — LOCKED |
| **K** | ℚ(√−3, √−11) | ZS-M28 — LOCKED |
| **V₄** | {1, χ₋₃, χ₋₁₁, χ₃₃} | ZS-M28 — LOCKED |
| **q\_χ** | {1, 3, 11, 33} | ZS-M28 — LOCKED (conductor) |
| **a\_χ** | {0, 1, 1, 0} | ZS-M28 — LOCKED (parity) |
| **J\_Z, Π\_Z** | I₁₁ − 2|1⟩⟨1|; ½(I \+ J\_Z) | ZS-M31 — PROVEN structure |
| **W\_S(g)** | Z-mediator Reading-C bilinear form | ZS-M31 — PROVEN |

**§3. Theorem C3.0: Commutant-Gate Insufficiency**

Let Π\_λ denote multiplication by 1\_{\[−λ,λ\]} on L²(ℝ) and Π\_F \= F Π\_λ F⁻¹ the Fourier-conjugate band projection. The Slepian concentration operator is A := Π\_λ Π\_F Π\_λ, bounded self-adjoint with 0 ≤ A ≤ I.  
**Theorem C3.0 (PROVEN). For every real-valued bounded Borel function f on spec(A), the operator W \= f(A) is self-adjoint, lies in the von Neumann algebra W\*(A), and commutes with every operator in the commutant of A. In particular it satisfies the standard hermiticity gate (SA-1) and the Slepian-commutation gate (\[W, A\] \= 0). The family {f(A) : f real Borel} is infinite-dimensional. Consequently SA-1 together with Slepian-commutation cannot uniquely select the Connes–Katsnelson realization W\_{λ,sa}^{CK} among self-adjoint operators on L²(ℝ).**  
Proof. The spectral theorem gives W \= f(A) \= ∫ f(t) dE\_A(t), where E\_A is the projection-valued spectral measure of A. Real-valued f makes W self-adjoint; the functional calculus is a \*-algebra homomorphism, so W ∈ W\*(A) and commutes with the commutant {A}′. The cardinality of {f(A) : f real Borel} is that of the real Borel functions on the (uncountable) spectrum, which is infinite. Hence no finite list of commutation conditions inside W\*(A) selects a unique member.  
Empirical witness. Two hundred random real polynomials of degree 7 in A were generated under the pre-registered seed 20260528\. All two hundred satisfied the hermiticity and Slepian-commutation gates within 10⁻¹⁰. The selection of W\_{λ,sa}^{CK} therefore requires a constraint outside W\*(A) — namely, the boundary domain at q \= ±λ.  
Remark. Theorem C3.0 corrects a class of attempted closures in earlier exploration cycles where Slepian-based proxies appeared to satisfy the gates designed to detect W\_{λ,sa}^{CK}. The gates were necessary but, by Theorem C3.0, vacuously degenerate: any spectral-calculus operator on the same commutant passes them. The selector for W\_{λ,sa}^{CK} is the boundary condition (⋆) at the turning points q \= ±λ, which lives outside the commutant.

**§4. External Imports T4–T5: the Connes–Katsnelson Realization**

**§4.1 IMP-T4 (Connes 1998 Lemma 6; explicit boundary matching)**

Let W\_λ denote the formal prolate differential expression W\_λ \= −(d/dq)\[(λ² − q²)(d/dq)\] \+ (2πλ q)². Connes (1998, Collège de France) introduced a self-adjoint extension W\_{λ,sa} on L²(ℝ) by imposing at q \= ±λ the condition

**(⋆)  lim\_{q→±λ} (q² − λ²) ∂\_q ξ(q) \= 0\.**

In the local Frobenius basis (y\_I, y\_II) at ±λ, with y\_II carrying the logarithm (the indicial equation is r² \= 0, a double root, so the second solution is logarithmic), the condition (⋆) is equivalent (Ramis–Richard-Jung–Thomann 2025, Lemma 1\) to the vanishing of the y\_II-coefficient. Equivalently, the local solution is bounded at ±λ.  
Status: IMPORTED-PROVEN. References: Connes (1998), Collège de France, Lemma 6 / \[8\] condition \[17\]; Ramis–Richard-Jung–Thomann (2025), Comptes Rendus Math. 363:1065, Lemma 1\.

**§4.2 IMP-T4b (Katsnelson 2016; Fourier-commuting uniqueness)**

Among all self-adjoint extensions of the restriction W\_{λ,min} to (−λ,λ), there is a UNIQUE self-adjoint extension that commutes with the Fourier transform F. It is the restriction of W\_{λ,sa} to that interval. Status: IMPORTED-PROVEN. Reference: V. Katsnelson, in Indefinite Inner Product Spaces, Schur Analysis, and Differential Equations (2016).

**§4.3 IMP-T5 (Connes–Moscovici 2022; spectrum)**

The operator W\_{λ,sa} is self-adjoint, commutes with F, Π\_λ, and Π\_F; its spectrum is discrete and unbounded on both sides; classical (positive) eigenvalues are double; non-classical eigenvalues are simple. Status: IMPORTED-PROVEN. Reference: A. Connes, H. Moscovici, PNAS 119 (2022); arXiv:2112.05500.

**§4.4 IMP-T5b (Ramis–Richard-Jung–Thomann 2025; negativity \+ imaginary-axis characterization)**

Settling the 2022 Connes–Moscovici conjecture: all non-classical eigenvalues of W\_{λ,sa} are NEGATIVE. Their eigenfunctions are identically zero on (−λ, λ), and both they and their Fourier transforms vanish there; in particular they lie in the Sonin space. The non-classical eigenfunctions are exactly the eigenfunctions of W\_λ which are bounded on the imaginary axis iℝ (the “naive” eigenvalues on iℝ). For λ \= √2, the ultraviolet behavior of these negative eigenvalues reproduces the squares of the shifted zeros of the Riemann zeta function. Status: IMPORTED-PROVEN (NEW). Reference: J.-P. Ramis, F. Richard-Jung, J. Thomann, Comptes Rendus Math. 363 (2025) 1065–1081; doi:10.5802/crmath.780, Theorem 3 \+ Corollary 15\.

**§5. T6d: V₄-Decoration via Burnol Conductor Blocks**

The corpus locks the V₄ channel data (§2). An earlier exploration introduced the convention Λ\_χ \= Λ·√(q\_χ), placing the conductor on the prolate parameter axis; the anti-numerology audit retired this convention (cf. §8). The correct decoration places the conductor on the FINITE-PLACE axis, leaving the archimedean parameter Λ untouched.

**§5.1 Conductor block C\_χ \= log q\_χ**

For each χ ∈ V₄, with conductor factorization q\_χ \= ∏\_p p^{e\_p(χ)}, define the channel conductor block

**C\_χ \= Σ\_{p | q\_χ} e\_p(χ) · log p \= log q\_χ.**

*Table 5.1. V₄ conductor blocks; identity of integer factorization.*

| χ | q\_χ | Σ e\_p log p | log q\_χ |
| ----- | ----- | ----- | ----- |
| **1** | 1 | 0 | 0 |
| **χ₋₃** | 3 | 1·log 3 | log 3 ≈ 1.0986 |
| **χ₋₁₁** | 11 | 1·log 11 | log 11 ≈ 2.3979 |
| **χ₃₃** | 33 | 1·log 3 \+ 1·log 11 | log 33 ≈ 3.4965 |

The equality C\_χ \= log q\_χ is the logarithm of the multiplicative factorization q\_χ \= ∏\_p p^{e\_p(χ)}; it is an identity of integer arithmetic, not a fit. It matches the conductor exponent in Tate’s analytic completion Λ(s, χ) \= (q\_χ/π)^{(s+a\_χ)/2} Γ((s+a\_χ)/2) L(s, χ), of which (1/2)·log(q\_χ/π) is the s-derivative coefficient. Status: DERIVED (identity).

**§5.2 Direct-sum decoration on the common CK/Sonin space**

Let S\_{CK} denote the imported Connes–Katsnelson Sonin subspace of L²(ℝ) (= span of non-classical eigenfunctions, all with negative eigenvalues by IMP-T5b). Define the V₄-decorated channel space

**ℋ\_{CK}^{V₄} := S\_{CK} ⊗ ℂ\[V₄\],**

and the finite-place conductor operator H\_{ram}^{V₄} := ⊕\_{χ∈V₄} C\_χ · I\_{S\_{CK}} ⊗ |χ⟩⟨χ|. The boundary condition (⋆) at q \= ±λ applies componentwise on ℂ\[V₄\] (it constrains the q-dependence, and the q-axis is shared across channels). Status: DERIVED, conditional on IMP-T4 \+ the locked V₄ data.  
**Theorem T6d (V₄-Decorated Burnol–Sonin Channel Closure, DERIVED). The triple (S\_{CK}, ℂ\[V₄\], H\_{ram}^{V₄}) is canonical: every datum is either imported (S\_{CK}, the Sonin projection, the (⋆) condition) or locked (ℂ\[V₄\], q\_χ, a\_χ), and C\_χ \= log q\_χ is an identity. No new free parameter is introduced.**  
This closes T6d. It does NOT close T7 (cf. §6), and it does not assert full Weil positivity (cf. §9 NC list).

**§6. T7: Direct-Sum Conflation and the Π\_Z-Sandwich Replacement T7′**

The natural next step would write a V₄-decorated colligation D \= ⊕\_χ (I − Π\_{CK,χ}) U\_{g,χ} Π\_{Harm,χ} and observe Q^{def}(g) := Tr(D† D) \= Σ\_χ Tr(D\_χ† D\_χ) ≥ 0 by Hilbert–Schmidt positivity. This identity is correct as an operator statement — but it does NOT equal the actual V₄-decorated Weil form.

**§6.1 Why pure direct-sum conflates two objects**

The corpus PROVEN per-channel Probe-W2 data (ZS-M22, ZS-M28) show that each non-trivial channel’s actual Weil contribution is INDEFINITE on the standard (a, t) grid:

*Table 6.1. Per-channel sign counts on the 12-point (a, t) grid (corpus Probe W2, PROVEN).*

| Channel | Negative grids | Status |
| ----- | ----- | ----- |
| **χ₋₃** | 6 / 12 | individually indefinite |
| **χ₋₁₁** | 9 / 12 | individually indefinite |
| **χ₃₃** | 7 / 12 | individually indefinite |

A pure direct sum Σ\_χ Tr(D\_χ† D\_χ) is a sum of PSD terms, hence ≥ 0\. The actual per-channel Weil contribution is INDEFINITE. The two cannot be equal except in degenerate cases. Therefore

**Q^{def}(g) \= Σ\_χ Tr(D\_χ† D\_χ)  ≠  Q\_{W,V₄}(g)**

as quadratic forms on test functions.

**§6.2 Lemma M31.0 obstruction**

ZS-M31 Lemma M31.0 (Non-Separability, PROVEN, 18/18) states that the Reading-C Weil bilinear form admits no decomposition W(g) \= F\_X(g) \+ F\_Y(g) \+ F\_Z(g) into separately X-, Y-, Z-dependent terms. A pure channelwise direct sum is, by definition, a separable decomposition over V₄. The direct-sum form therefore violates Lemma M31.0 as a candidate identity for the actual Weil form. The direct-sum object Q^{def} is a well-defined PSD operator-trace; it is simply not the Weil form.

**§6.3 Improvement T7′: Π\_Z-sandwich V₄-decoration**

The Z-Spin Reading C (ZS-M31, PROVEN) supplies the correct cross-coupling. Its V₄-decorated analogue retains the Π\_Z sandwich while absorbing the Burnol decoration into the channelwise test factor:

**W\_{X,Y,Z}^{V₄}(g) \= Σ\_χ γ\_χ(g) ⟨ g\_X^χ, (Π\_Z ⊗ I\_χ) (B\_Y^χ − P\_Y^χ) (Π\_Z ⊗ I\_χ) g\_X^χ ⟩,**

where γ\_χ(s) \= (q\_χ/π)^{(s+a\_χ)/2} Γ((s+a\_χ)/2) is Tate’s channel-decorated factor (the conductor enters here, NOT in Λ) and I\_χ \= |χ⟩⟨χ|. The Π\_Z sandwich is unchanged from corpus Reading C; the V₄ sum runs outside the sandwich, so cross-channel coupling via Π\_Z survives.  
Properties of T7′ (DERIVED-CONDITIONAL on imports \+ Reading C): (a) Π\_Z sandwich preserves Cross-Coupling (ZS-M2); (b) channelwise γ\_χ absorbs the Burnol decoration without changing Λ; (c) Z₂-parity selection (ZS-M31 Theorem M31.4) operates inside each channel; (d) the form is NOT automatically PSD — positivity would be the actual Weil-positivity claim, which is registered OPEN.  
**Theorem T7′ (V₄-Decorated Reading-C Construction, DERIVED-CONDITIONAL). The form W\_{X,Y,Z}^{V₄}(g) above is well-defined on the locked Z-Spin Hilbert spaces, satisfies the corpus-PROVEN obstructions Lemma M31.0 (Non-Separability), ZS-M2 (Cross-Coupling), and Theorem M31.4 (Z₂-parity selection), and reduces in the trivial channel (χ \= 1\) to the standard Reading-C bilinear form W\_S(g). The improvement is structural, not numerical: T7′ does not assert positivity.**

**§7. The Closure Gate, Updated**

*Table 7.1. Status of the closure gate after the present exploration.*

| Object | Status | Reference |
| ----- | ----- | ----- |
| **M\_CK explicit (q²−λ²)∂\_qξ \= 0** | IMPORTED-PROVEN | Connes 1998; Ramis–RJ–T 2025 |
| **F-commuting uniqueness** | IMPORTED-PROVEN | Katsnelson 2016 |
| **W\_{λ,sa} spectrum (discrete, 2-sided)** | IMPORTED-PROVEN | Connes–Moscovici 2022 |
| **Negativity of non-classical eigenvalues; Sonin membership** | IMPORTED-PROVEN (NEW) | Ramis–RJ–T 2025 |
| **Theorem C3.0 (commutant-gate insufficiency)** | PROVEN (this paper) | §3 |
| **Λ\_χ \= Λ√(q\_χ) rescaling** | WITHDRAWN | §8 |
| **V₄ direct-sum H\_{ram}^{V₄} \= ⊕\_χ C\_χ · I** | DERIVED | §5; Burnol IMPORT |
| **Pure direct-sum Q^{def} \= Q\_{W,V₄}** | REJECTED | §6 (Lemma M31.0) |
| **T7′ Π\_Z-sandwich V₄ Reading C** | DERIVED-CONDITIONAL | §6.3 |
| **Semilocal Sonin stability (S\_N → ∞)** | IMPORTED | CCM 2024 |
| **Full Weil positivity** | OPEN / NC | §9 |

**§8. Anti-Numerology Controls (Negative Results)**

Pre-registered controls (seed 20260528). Five candidate identities were tested across the thirteen-stage exploration and retired; they carry no claim status.

| Candidate | Why it fails | Status |
| ----- | ----- | ----- |
| **B\_F18 \= B\_eig (commutator selects E\_−)** | K full-rank ⇒ coverage vacuous; null model 2000/2000 | REJECTED (ZS-F21 v1.2) |
| **B\_Sonin−P\_K ≥ 0 by naive scale dominance** | B\_Sonin \~ 100× P\_K (normalization artifact) | REJECTED |
| **tanh(n \+ 0.3) defect colligation** | offset is a fitted free parameter | REJECTED |
| **Sonin space from Jacobi-truncation prolate** | min eig → −∞, \#neg → ∞ with truncation | REJECTED (artifact) |
| **Λ\_χ \= Λ·√(q\_χ) per-channel prolate** | conductor belongs to s-axis (Tate), not Λ-axis | WITHDRAWN (this paper, §5) |
| **Pure direct-sum Q^{def} \= Q\_{W,V₄}** | violates Lemma M31.0; per-channel data indefinite | REJECTED (this paper, §6) |

Across the cycles, the recurring failure mode is a normalization/rank/offset/truncation artifact producing an apparently clean match that null controls retire. The mature programme now flags scale dominance, full-rank coverage, fitted offsets, and conductor-on-the-wrong-axis as first-line suspects whenever a clean positivity match appears.

**§9. Non-Claims**

NC-F21.1. No proof of full Weil positivity, of the Connes–Consani archimedean positivity beyond the imported theorems, or of RH/GRH is asserted here.  
NC-F21.2. The pure direct-sum closure Q^{def} \= Σ\_χ Tr(D\_χ† D\_χ) is a well-defined PSD operator-trace but is explicitly NOT identified with the actual V₄-decorated Weil form (§6).  
NC-F21.3. The improvement T7′ (Π\_Z-sandwich V₄ Reading C) is a structural construction; no positivity claim is attached to it.  
NC-F21.4. Λ\_χ \= Λ√(q\_χ) is permanently withdrawn and carries no claim status.  
NC-F21.5. Equivalence between the Z-Spin V₄-Sonin–Frobenius construction and the Connes–Consani–Moscovici program is NOT asserted (cf. corpus NC-M23.5). Only finite colored-shadow correspondences are made; functoriality between Z-Spin K-arithmetic and CCM scaling-site remains the corpus-OPEN problem O-M23.11.

**§10. Falsification Gates**

| Gate | Condition (falsifies if TRUE) | Status |
| ----- | ----- | ----- |
| **F-F21.1** | A spectral-calculus operator f(A) selects W\_{λ,sa}^{CK} uniquely | PASS (Theorem C3.0) |
| **F-F21.2** | C\_χ ≠ log q\_χ for some χ ∈ V₄ | PASS (4/4, identity) |
| **F-F21.3** | Pure direct sum Q^{def} reproduces an indefinite channel sign | PASS (REJECTED, §6.1) |
| **F-F21.4** | Λ\_χ \= Λ√(q\_χ) appears in any external Tate-conductor formula | PASS (no such formula; WITHDRAWN) |
| **F-F21.5** | T7′ form admits a separable decomposition F\_X+F\_Y+F\_Z | PASS (Π\_Z sandwich blocks it; Lemma M31.0) |

**§11. Conclusion**

Across thirteen exploration cycles, six independent attacks on the D4c defect-square gate converged without closing it: each route was retired by an anti-numerology control or by a Z-Spin obstruction (Lemma M31.0). The cumulative residue is now precisely located. (1) Theorem C3.0 explains why intrinsic Slepian-based selectors cannot work: the commutant W\*(A) is too rich. (2) The Connes 1998 boundary condition (q²−λ²)∂\_qξ \= 0, the Katsnelson Fourier-commuting uniqueness, the Connes–Moscovici 2022 spectrum, and — settling a 2022 conjecture — the Ramis–Richard-Jung–Thomann 2025 negativity-and-imaginary-axis theorem furnish the external archimedean side as a single black box. (3) The Burnol conductor block C\_χ \= log q\_χ supplies the finite-place V₄ decoration as an identity of integer factorization, without disturbing the archimedean parameter Λ. (4) The natural direct-sum closure Q^{def} \= Σ\_χ Tr(D\_χ† D\_χ) is a trivially PSD object that does NOT equal the actual V₄-decorated Weil form; Lemma M31.0 forbids the identification. The improvement T7′ (Π\_Z-sandwich V₄ Reading C) absorbs the Burnol decoration into Tate’s channel factor γ\_χ(s) while preserving the corpus-PROVEN cross-coupling structure; it is a structural construction with no positivity claim. Full Weil positivity remains OPEN. The Z-Spin contribution after thirteen cycles is the new Theorem C3.0, the explicit map of which external archimedean theorems close T4–T5b, the canonical Burnol decoration of T6d, and the diagnosis-and-replacement T7 → T7′ that brings the channelwise structure into agreement with the corpus-PROVEN non-separability obstruction.

**Acknowledgements and Code Availability**

This paper consolidates a thirteen-stage deep exploration (March 2026\) examining the D4c defect-square gate of the Z-Spin archimedean–finite positivity programme. The author thanks the AI collaborator (Anthropic Claude) for the exploration, the diagnosis of normalization and convention artifacts, the null-model anti-numerology controls, and manuscript drafting. The author assumes full responsibility for all scientific content and status assignments.  
Code availability: zs\_F21\_verify\_v2\_0.py (34/34 PASS; Theorem C3.0 analytic \+ 200-sample empirical witness; C\_χ \= log q\_χ identity at 4/4 channels; pure direct-sum / Lemma M31.0 obstruction; six anti-numerology controls; seed 20260528). Dependencies: Python 3.10+, numpy, scipy, mpmath ≥ 1.3.0, sympy.

**Appendix A — Frobenius Structure at q \= ±λ**

Near q \= λ write q \= λ \+ ε. To leading order, λ² − q² \= −2λε \+ O(ε²). The ODE −(d/dq)\[(λ²−q²)(d/dq)ψ\] \+ (2πλ q)²ψ \= χψ becomes, in ε,

**(d/dε)\[2λε·(dψ/dε)\] \+ (2πλ²)² ψ \+ O(ε) \= χ ψ.**

Try ψ \~ εʳ; then (d/dε)\[2λε·r·εʳ⁻¹\] \= 2λ r² εʳ⁻¹, so the indicial polynomial is 2λ r² \= 0, giving the double root r \= 0\. The two linearly independent local solutions therefore behave as ψ₁(ε) \= const \+ O(ε log ε) and ψ₂(ε) \= log|ε| \+ O(ε log ε). Imposing (⋆), lim\_{q→±λ} (q²−λ²) ∂\_q ξ \= 0, projects out the ψ₂ component. The boundary trace map (Γ₀, Γ₁) reads off the constant part and the log-coefficient respectively. By symmetry q → −q the analysis at q \= −λ is identical. Together with the L² deficiency at q \= ±∞, the deficiency indices of W\_{λ,min} are (4, 4); the self-adjoint extensions form a U(4) family in the Naimark/Krein sense. The Connes–Katsnelson realization is the unique point in U(4) selected by the Fourier-commutation constraint (IMP-T4b).

**Appendix B — Identity of Integer Factorization**

For any positive integer n with prime factorization n \= ∏\_p p^{e\_p}, taking the logarithm gives log n \= Σ\_p e\_p · log p, an identity in characteristic zero. Applied to n \= q\_χ and exponents e\_p(χ) recorded in the conductor factorization, this yields C\_χ \= log q\_χ. The identity is purely arithmetic, with no analytic or operator-theoretic content; it cannot be “fit” or “withdrawn”. Its appearance in Tate’s analytic conductor (q\_χ/π)^{(s+a\_χ)/2} as a s-derivative coefficient is what makes the same expression simultaneously the natural Burnol conductor block.

**Appendix C — Why the Pure Direct-Sum Closure Is Vacuous in This Sense**

For any bounded operator D on a Hilbert space, Tr(D† D) \= ‖D‖²\_{HS} ≥ 0 by definition; equality holds iff D \= 0\. When D \= ⊕\_χ D\_χ is block-diagonal, Tr(D† D) \= Σ\_χ Tr(D\_χ† D\_χ), a sum of non-negative reals. Identifying this with a quadratic form Q(g) that depends on a test function g delivers a PSD form by construction. This says nothing about whether Q matches any particular target functional. In the present case the target — the V₄-decorated Weil form Q\_{W,V₄} — has corpus-PROVEN per-channel indefiniteness (Table 6.1) and corpus-PROVEN non-separable structure (Lemma M31.0). A PSD block-diagonal trace can equal neither: the first because the actual channels are individually signed, the second because separation is forbidden. The construction is internally consistent as an operator object and PSD by construction; it simply names a different object than the one D4c demands.

**References**

\[1\] A. Connes, “Formules explicites, formules de trace et réalisation spectrale des zéros de la fonction zêta,” Cours au Collège de France (1998), Annu. Collège de France 95, 115–122. \[Lemma 6: explicit boundary condition (q²−λ²)∂\_qξ \= 0.\]

\[2\] V. Katsnelson, “Self-adjoint boundary conditions for the prolate spheroid differential operator,” in Indefinite Inner Product Spaces, Schur Analysis, and Differential Equations (D. Alpay, ed.), Birkhäuser (2016). \[Fourier-commuting uniqueness.\]

\[3\] A. Connes, H. Moscovici, “The UV prolate spectrum matches the zeros of zeta,” Proc. Natl. Acad. Sci. USA 119 (22) e2123174119 (2022); arXiv:2112.05500. \[W\_{λ,sa} spectrum, Sonin compression.\]

\[4\] J.-P. Ramis, F. Richard-Jung, J. Thomann, “New eigenfunctions for the negative part of the Connes–Moscovici prolate spectrum,” Comptes Rendus Math. 363, 1065–1081 (2025); doi:10.5802/crmath.780. \[Settling the CCM 2022 conjecture: all non-classical eigenvalues are negative; imaginary-axis characterization.\]

\[5\] A. Connes, C. Consani, “Weil positivity and trace formula — the archimedean place,” Selecta Math. (N.S.) 27, 77 (2021); arXiv:2006.13771.

\[6\] A. Connes, C. Consani, H. Moscovici, “Semilocal Sonin space stability,” Ann. Funct. Anal. 15:87 (2024); arXiv:2310.18423.

\[7\] J. F. Burnol, “Sur les espaces de Sonine associés par de Branges à la transformation de Fourier,” C. R. Acad. Sci. Paris Ser. I 335, 689–692 (2002).

\[8\] J. F. Burnol, “The explicit formula and the conductor operator,” arXiv:math/9902080 (1999).

\[9\] J. Tate, “Fourier analysis in number fields and Hecke’s zeta-functions,” in Algebraic Number Theory (J. W. S. Cassels, A. Fröhlich, eds.), Academic Press (1967). \[Analytic conductor (q\_χ/π)^{s/2}.\]

\[10\] D. Slepian, H. Pollak, “Prolate spheroidal wave functions, Fourier analysis and uncertainty I,” Bell Syst. Tech. J. 40, 43–63 (1961). \[Concentration operator A \= Π\_λ Π\_F Π\_λ.\]

\[11\] M. Reed, B. Simon, Methods of Modern Mathematical Physics, Vols. I–II, Academic Press (1972, 1975). \[Spectral theorem, von Neumann–Naimark–Krein self-adjoint extension theory.\]

\[12\] R. Bhatia, Matrix Analysis, Springer GTM 169 (1997). \[Inertia, principal angles.\]

\[13\] Z-Spin Collaboration (K. Kang), ZS-F21 v1.2 — Positive-Square Criterion and Commutator-Coverage Obstruction.

\[14\] Z-Spin Collaboration (K. Kang), ZS-M22 v1.0 — ADS-5, §6.4–6.6 (Probe W2 per-channel data; matrix-valued B\_K requirement).

\[15\] Z-Spin Collaboration (K. Kang), ZS-M23 v1.0 — Dragon D4 (D4a, D4b, D4c, D4d); NC-M23.5, NC-M23.7; O-M23.9, O-M23.11.

\[16\] Z-Spin Collaboration (K. Kang), ZS-M28 v1.0 — Locked V₄ channel data; Probe W2 PROVEN diagnostic; Baseline-4 V₄ trace-remainder.

\[17\] Z-Spin Collaboration (K. Kang), ZS-M31 v1.0 — Reading C Π\_Z-sandwich bilinear form; Lemma M31.0 Non-Separability (18/18); Theorem M31.2 (NEG localization); Theorem M31.4 (Z₂-parity selection).

\[18\] Z-Spin Collaboration (K. Kang), ZS-M33 v1.0 — Path γ-revised colligation; Theorem M33.4 TARGET-SIMULATION.

**Version History**

v1.0 (March 2026, as ZS-F21 v1.0): closure-type asymmetry; sector–place direction; Mellin frame-duality of the operator-form wall. 18/18 PASS.  
v1.1 (March 2026, as ZS-F21 v1.1): positivity wall closed in the obstruction sense — inertia invariance (F21.5), scalar/diagonal no-go (F21.6), minimal matrix-rank obstruction (F21.7), finite semilocal exact inertia (F21.8). 22/22 PASS.  
v1.2 (March 2026, as ZS-F21 v1.2): Positive-Square Criterion (F21.9, PROVEN both directions); Commutator-Coverage Obstruction (F21.10, PROVEN negative, null-model 2000 samples); commutator shortcut REJECTED. 26/26 PASS.  
v2.0 (March 2026, as ZS-F21 v2.0): Theorem C3.0 (Commutant-Gate Insufficiency, PROVEN this paper, analytic \+ 200/200 empirical); external imports T4–T5 (Connes 1998 \+ Katsnelson 2016 \+ CM 2022 \+ Ramis–RJ–T 2025 NEW PROVEN); T6d Burnol conductor decoration C\_χ \= log q\_χ DERIVED; T7 pure direct-sum REJECTED via Lemma M31.0; T7′ Π\_Z-sandwich V₄ Reading C DERIVED-CONDITIONAL; Λ\_χ \= Λ√(q\_χ) WITHDRAWN; full Weil positivity OPEN / NC. 34/34 PASS, six anti-numerology controls.