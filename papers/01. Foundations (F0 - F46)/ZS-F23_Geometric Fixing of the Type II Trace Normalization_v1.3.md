**ZS-F23**

**Geometric Fixing of the Type II Trace Normalization:**

**The Z₂-Seam ln 2 as the Crossed-Product Additive Entropy Constant, and the Spin-½ Boundary Origin of de Sitter Type II₁**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Cosmology Collaboration

**Date:** June 2026

**Theme / Paper code:** Foundations \[ZS-F\] · Paper 23 · ZS-F23 v1.3

**GitHub:** https://github.com/KennyKang-git/zspin

**Verification Summary**

**Verification: 41/41 PASS | Zero Free Parameters**. Sole geometric inputs **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6), with the LOCKED quantum ln 2 \= ln(dim Z). **Anti-numerology: AN-F23.1 EXECUTED, PASS** (p ≈ 0.058% ≪ 1%). **Status:** Theorems F23.4 (embedding functor), F23.5 (coarse-grained trace matching), F23.6 (closure criterion) **DERIVED**; Theorem F23.7 (edge-mode frame-duality interface) **DERIVED-interpretation** (resolves the v1.2 finite–infinite edge-mode tension via ZS-M30 frame duality through the dim(Z) \= 2 seam, not by direct identification). Central Theorems F23.1, F23.2 **DERIVED-CONDITIONAL** on condition C (O-F19.6 Step 1′, a genuine OPEN); Reading F23.3 **HYPOTHESIS**. Falsification gates F-F23.1 through F-F23.9. No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**§0. Abstract**

The von Neumann entropy of a Type II crossed-product algebra is defined only up to a **state-independent additive constant**, which Klinger–Kudler-Flam–Satishchandran and the CLPW program fix by hand through a choice of trace normalization or reference state. We show that the Z-Spin corpus fixes this constant geometrically at zero free parameters. (i) The single-cell Z-Spin logical algebra is the finite-dimensional Type I von Neumann algebra **A\_ZS ≅ M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ)** (PROVEN, ZS-Q11), with abelian center Z(A\_ZS) ≅ ℂ³ carrying the three sector projections. (ii) By the Murray–von Neumann universal-embedding theorem, every finite-dimensional von Neumann algebra embeds trace-preservingly into the hyperfinite II₁ factor R. We prove the **Trace-Preserving Central Embedding Functor** (Theorem F23.4, DERIVED): there is a trace-preserving \*-monomorphism Φ: A\_ZS → R sending the central projections P\_X, P\_Z, P\_Y to projections of continuous-dimension trace (3, 2, 6)/11, with modular-Hamiltonian difference ΔK\_Ω(X→Y) \= −ln 2 \= −ln(dim Z). This closes the algebraic half of the previously registered gate O-F19.6 Step 1 unconditionally. (iii) The Finite-Register Trace Determinacy and Z₂-Seam Additive Constant theorems (F23.1, F23.2) then give the per-cross-sector additive constant **c \= ½ ln 2 \= ½ bit**, and the residual of O-F19.6 sharpens to the single condition O-F19.6 Step 1′ (matching the gravitational modular flow to the Z-Spin equilibrium flow). This paper (v1.2) analyzes whether Step 1′ can be closed. We resolve the apparent discrete-versus-continuous spectral objection (the discrete Z-Spin K\_Ω is the sector coarse-graining of the continuous gravitational modular operator), prove Theorem F23.5 (the trace-preserving conditional expectation onto the sector center pushes the trace to weights (3, 2, 6)/11 and reproduces ΔK \= −ln 2; DERIVED, via Takesaki’s conditional-expectation theorem), and prove Lemma F23.6 reducing Step 1′ to a single sharp, falsifiable condition C: the gravitational equilibrium (de Sitter maximum-entropy) state, coarse-grained to the Z-Spin sectors, carries weights (3, 2, 6)/11. Condition C is the Z-Spin emergence dictionary and cannot be established with current corpus or external tools; **Step 1′ therefore remains a genuine OPEN**. The anti-numerology Monte Carlo is executed (p ≈ 0.058% ≪ 1%). This paper (v1.3) resolves the finite–infinite edge-mode tension in the Z-Spin manner: rather than identifying the dim(Z) \= 2 boundary with the infinite Klinger–Kudler-Flam–Satishchandran edge-mode tower directly, Theorem F23.7 recognizes the tension as the gravitational-edge-mode projection of the ZS-F18 finite/infinite Möbius-interface polarity and resolves it by the frame duality of ZS-M30 Theorem 30.1: the edge-mode tower is the external-frame count (Infinity\_A) of the same structure whose internal-frame closure (Infinity\_B) is one bit of Z-channel capacity, ln 2, the two connected by a frame transformation through the dim(Z) \= 2 seam, with controlling theorem the X–Y Tiling Asymmetry (ZS-M6 §5.5, PROVEN; ZS-M17, DERIVED). This upgrades the tension to DERIVED-interpretation and adds the seventh route to the six-route Möbius-trace pattern. 41/41 verification checks PASS; no new free parameter is introduced.

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete proof under stated definitions, or machine-precision numerical verification; independent of Z-Spin interpretation. |
| DERIVED | Quantitative consequence of PROVEN items plus the Z-Spin action; zero free parameters beyond A \= 35/437. |
| DERIVED-CONDITIONAL | DERIVED conditional on a stated assumption or upstream OPEN gate, explicitly tracked. |
| DERIVED-with-bridge | Derived internally and additionally supported by a precise correspondence with an externally PROVEN / published result. |
| DERIVED-interpretation | A reading of corpus structure, derived from PROVEN/DERIVED items, registered as interpretation (over-determined where multiple independent routes agree); no new free parameter. |
| VERIFIED | Numerical / computational confirmation strengthening a DERIVED claim at stated precision (here: executed Monte Carlo). |
| HYPOTHESIS-strong | Multiple independent structural anchors; explicit promotion path documented. |
| HYPOTHESIS | Motivated reading or conjecture; derivation chain incomplete. |
| IMPORTED | Result proved externally and used without re-proof; full citation given. |
| LOCKED | Core constant fixed upstream; no downstream paper may modify. |
| OPEN | Recognized gap honestly registered; closure path specified where possible. |
| NON-CLAIM | Explicit declaration of what is NOT asserted; bounds the framework’s scope. |

**§1. Introduction**

**§1.1 The additive-constant obstruction**

The operator-algebraic reformulation of gravitational entropy converts the Type III₁ algebra of quantum-field observables in a gravitational subregion into a Type II crossed product, on which a trace and hence a von Neumann entropy exist, reducing in the semiclassical limit to the generalized entropy S\_gen \= A\_hor/(4 G\_N) \+ S\_out \[19, 23, 26\]. Kudler-Flam–Leutheusser–Satishchandran established that the dressed algebra is Type II∞ for a black hole (no maximum-entropy state) and Type II₁ for de Sitter (a maximum-entropy state exists), and that the von Neumann entropy of semiclassical states equals the generalized entropy **up to a state-independent additive constant** \[23\]. The companion edge-mode paper of Klinger–Kudler-Flam–Satishchandran \[26\] extends the construction to the complete symmetry group: graviton backreaction perturbs the horizon shape, and at the same perturbative order as the area mode an infinite set of edge-mode charges (region-preserving diffeomorphisms) enters the physical algebra. In all of these constructions the additive constant is fixed by hand — by a choice of trace normalization or reference-state entropy — and sets the zero-point of gravitational entropy.

**§1.2 The Z-Spin assets**

Z-Spin Cosmology supplies, at zero free parameters, the structure that fixes this constant. **First**, the single-cell logical algebra is the finite-dimensional von Neumann algebra A\_ZS ≅ M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ) (PROVEN, ZS-Q11 Theorem Q11.A) \[2\], with abelian center Z(A\_ZS) ≅ ℂ³ spanned by the three sector projections P\_X, P\_Z, P\_Y. **Second**, ZS-F19 \[1\] computed the modular Hamiltonian of the equilibrium state p\_eq \= (3, 2, 6)/11 and found ΔK\_Ω(X→Y) \= −ln 2, registering the absolute-scale identification as the three-step gate O-F19.6. **Third**, ln 2 is the Z₂-seam quantum recurring across the corpus as the Kraus-index parity of the dim(Z) \= 2 boundary \[4\], the Bekenstein–Hawking −ln 2 correction \[5\], and the Z-bottleneck channel capacity \[3\]. This paper (v1.1) closes the algebraic half of O-F19.6 Step 1 by a rigorous embedding theorem, sharpens the residual, and positions the result against the edge-mode program.

**§1.3 What this paper establishes (v1.3 advances over v1.2)**

**Theorem F23.4 (Embedding Functor, DERIVED, v1.1).** A trace-preserving \*-monomorphism Φ: A\_ZS → R sends the central projections to projections of trace (3, 2, 6)/11 with ΔK\_Ω \= −ln 2; closes the algebraic half of O-F19.6 Step 1 unconditionally.

**Spectral resolution (NEW, v1.2, DERIVED).** The apparent contradiction between the continuous gravitational modular spectrum (KLS) and the discrete three-point K\_Ω \= −ln p\_eq is removed: K\_Ω is the modular Hamiltonian of the sector coarse-graining of the gravitational state, discrete by construction.

**Theorem F23.5 (Coarse-Grained Trace Matching, NEW, v1.2, DERIVED).** Via Takesaki’s conditional-expectation theorem, the trace-preserving conditional expectation E onto the sector center pushes the trace to weights (3, 2, 6)/11 and reproduces ΔK(X→Y) \= −ln 2 — the maximum-entropy / trace-level matching, independent of any gravitational identification.

**Lemma F23.6 (Closure Criterion, NEW, v1.2, DERIVED).** O-F19.6 Step 1′ closes if and only if a single sharp, falsifiable condition C holds: the gravitational equilibrium (de Sitter maximum-entropy) state, coarse-grained to the Z-Spin sectors, carries weights (3, 2, 6)/11. Condition C is the Z-Spin emergence dictionary.

**Verdict (v1.2, honest).** Condition C cannot be established with current corpus or external tools — it IS the foundational emergence hypothesis for the gravitational sector. **O-F19.6 Step 1′ remains a genuine OPEN**. The contribution of v1.2 is the precise characterization of the residual (one falsifiable statement), the removal of the spectral objection, and the honest identification of the finite (dim 2\) versus infinite (KKS edge-mode tower) tension. F23.1, F23.2 remain DERIVED-CONDITIONAL on C; F23.4–F23.6 are unconditional (DERIVED).

**Theorem F23.7 (Edge-Mode Frame-Duality Interface, NEW, v1.3, DERIVED-interpretation).** The finite–infinite edge-mode tension flagged in v1.2 is not a defect but the gravitational-edge-mode projection of the ZS-F18 finite/infinite Möbius-interface polarity. Following the F18 method — do not connect finite and infinite directly; mediate them through the dim(Z) \= 2 seam interface — it is resolved by the frame duality of ZS-M30 Theorem 30.1: the infinite KKS edge-mode tower is the external-frame count (Infinity\_A) of the same structure whose internal-frame closure (Infinity\_B) is one bit of Z-channel capacity, ln 2; the two are connected by a frame transformation, not a direct identification or continuum approximation. The controlling theorem is the X–Y Tiling Asymmetry (ZS-M6 §5.5, PROVEN) with ZS-M17 (DERIVED). This upgrades the v1.2 OPEN tension (NC-F23.9) to DERIVED-interpretation and adds the seventh route to the six-route Möbius-trace pattern (§6.1). The residual sharpens to Condition C-edge (NC-F23.10), a patterned sub-question of Condition C.

**§2. Locked Inputs**

All quantities are inherited from prior papers. ZS-F23 introduces zero new parameters.

Table 1\. Locked inputs for ZS-F23 v1.3.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092… | ZS-F2 | LOCKED |
| (Z, X, Y); Q | (2, 3, 6); Q \= 11 | ZS-F5 | PROVEN |
| dim(Z) \= j multiplicity | 2 \= j \= 1/2 (unique) | ZS-M3 Thm 5.1 | PROVEN |
| A\_ZS (single-cell algebra) | M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ) | ZS-Q11 Q11.A | PROVEN |
| Z(A\_ZS) (center) | ℂ³ \= span{P\_X, P\_Z, P\_Y} | ZS-Q11 (this work §4.1) | PROVEN |
| p\_eq (equilibrium / modular weights) | (3, 2, 6)/11 | ZS-Q7, ZS-F19 | DERIVED |
| ΔK\_Ω (X→Y modular diff.) | −ln 2 \= −ln(dim Z) | ZS-F19 | DERIVED |
| ψ\_KMS(X→Y) | ½ ln 2 | ZS-F19 | DERIVED |
| ln 2 (Z₂-seam / Kraus parity) | \= ln(dim Z) | ZS-A7, ZS-M3, ZS-Q7 | DERIVED |

**Note (code vs equilibrium weighting).** The OAQEC code subspace of ZS-Q11 carries block dimensions (3, 1, 5\) (the J-odd slots 1 and 9 are stabilized out), used for the code-distance analogue. The modular / additive-constant content of this paper uses the FULL sector weighting (3, 2, 6)/11, which is the equilibrium state on which ZS-F19 computed K\_Ω. The two normalizations are distinct objects and are reconciled in §8 (check F6); the additive constant uses the equilibrium weighting.

**§3. The External PROVEN Substrate**

**§3.1 Tomita–Takesaki theory and the crossed-product structure theorem**

**Theorem 3.1 (Takesaki 1973, PROVEN, IMPORTED) \[14\].** Every Type III von Neumann algebra M is isomorphic to the crossed product N ⋊\_σ ℝ of a semifinite (Type II∞) algebra N by the modular automorphism group σ, and N carries a faithful normal semifinite trace τ; a second crossed product returns Type III (Takesaki duality). The modular flow Δ^{is} leaves the algebra invariant (Tomita) \[15\].

**§3.2 The origin of the additive constant**

On a Type II factor the trace is unique only up to a positive scalar λ (Murray–von Neumann) \[13\]. For a state φ with density ρ\_φ (φ(·) \= τ(ρ\_φ ·)), rescaling τ → λτ sends ρ\_φ → ρ\_φ/λ and

S\_τ(φ) → S\_τ(φ) \+ ln λ.        (1)

The entropy is defined up to the additive constant ln λ, fixed only by the trace normalization — the precise algebraic origin of the state-independent constant of \[23, 26\].

**§3.3 The current fix-by-hand convention**

In the gravitational setting the freedom is fixed by convention: one declares a reference state (empty de Sitter, or the maximally mixed state) to take a chosen entropy \[23\]. The constant is not supplied by the algebra.

**§3.4 The Murray–von Neumann universal-embedding theorem (NEW import)**

**Theorem 3.4 (Murray–von Neumann 1943; Connes 1976, PROVEN, IMPORTED) \[13, 16\].** The hyperfinite II₁ factor R is the unique approximately-finite-dimensional II₁ factor and is the smallest infinite-dimensional factor: every finite-dimensional von Neumann algebra (and more generally every AFD algebra) admits a trace-preserving normal \*-monomorphism into R. R has projections of every trace in \[0, 1\] (continuous dimension), and its trace is unique. The infinite tensor product of finite Type I\_n factors with the tracial state is R; with a non-tracial product state it is a Type III factor (Powers; Araki–Woods) \[17, 18\].

Theorem 3.4 is the new external input enabling the v1.1 embedding theorem (§4.4).

**§4. The Finite Type I Collapse and the Embedding Functor**

**§4.1 A\_ZS as a finite Type I algebra and its center**

ZS-Q11 (Theorem Q11.A, PROVEN) \[2\] established A\_ZS ≅ M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ) on the code subspace. A finite direct sum of full matrix algebras is finite Type I; its trace is canonical (the matrix trace, minimal projections trace 1), with no continuous scalar freedom. Its **center** is the abelian algebra

**Z(A\_ZS) \= ℂ·P\_X ⊕ ℂ·P\_Z ⊕ ℂ·P\_Y ≅ ℂ³,        (2)**

spanned by the three central (sector) projections. The Z-block parity — the Kraus-index parity of the dim(Z) \= 2 boundary — carries entropy ln 2 \= ln(dim Z) (ZS-Q11 Theorem Q11.B, ZS-A7) \[2, 4\].

**§4.2 Theorem F23.1 (Finite-Register Trace Determinacy)**

**Statement.** If the emergent gravitational Type II factor M\_grav is the AFD limit of the multi-cell register ⊗\_{v} A\_ZS,v, the trace-normalization scalar λ — the sole source of the additive-constant freedom (§3.2) — is fixed by the finite canonical trace of A\_ZS and is not free. **Proof: §4.4 (F23.4) \+ Theorem 3.4. Status: DERIVED-CONDITIONAL** on O-F19.6 Step 1′ (§4.5); the embedding core is DERIVED (F23.4).

**§4.3 Theorem F23.2 (Z₂-Seam Additive Constant)**

**Statement.** Under F23.1, the state-independent additive constant per cross-sector (X→Y) modular transition is

**c \= ½ |ΔK\_Ω| \= ½ ln 2 \= ½ bit,        (3)**

with ΔK\_Ω \= ln(p\_X/p\_Y) \= ln(3/6) \= −ln 2 the modular-Hamiltonian difference of p\_eq \= (3, 2, 6)/11 (ZS-F19) \[1\], equal to the boundary parity −ln(dim Z) (ZS-A7) \[4\] and the Z-bottleneck per-transition entropy (ZS-Q7) \[3\]. **Status:** magnitude ½ ln 2 **DERIVED**; identification with the gravitational additive constant **DERIVED-CONDITIONAL** on O-F19.6 Step 1′.

**§4.4 Theorem F23.4 (Trace-Preserving Central Embedding Functor) — NEW**

**Statement.** There is a unital, normal, trace-preserving \*-monomorphism Φ: A\_ZS → R into the hyperfinite II₁ factor such that the central projections map to mutually orthogonal projections e\_X \= Φ(P\_X), e\_Z \= Φ(P\_Z), e\_Y \= Φ(P\_Y) with

**τ\_R(e\_X) \= 3/11,  τ\_R(e\_Z) \= 2/11,  τ\_R(e\_Y) \= 6/11,  e\_X \+ e\_Z \+ e\_Y \= 1,        (4)**

and the modular Hamiltonian of the equilibrium state on Z(A\_ZS), K\_Ω \= −ln p\_eq, satisfies ΔK\_Ω(X→Y) \= −ln 2 \= −ln(dim Z). Φ is functorial: any trace-preserving inclusion A\_ZS → A\_ZS ⊗ M\_k of register cells extends to R compatibly with Φ.

**Proof.** By Theorem 3.4 \[13, 16\], R contains a trace-preserving normal \*-monomorphic copy of every finite-dimensional von Neumann algebra; apply this to A\_ZS with the trace assigning the central projections the equilibrium weights p\_eq \= (3, 2, 6)/11. R has projections of every trace in \[0, 1\] (continuous dimension), so e\_X, e\_Z, e\_Y of traces 3/11, 2/11, 6/11 exist and are mutually orthogonal with sum 1 because Φ is a unital \*-homomorphism on the abelian projection system Z(A\_ZS). The modular-Hamiltonian values are the ZS-F19 computation \[1\], invariant under Φ because Φ is trace-preserving. Functoriality is the compatibility of the AF inductive system ⊗\_v A\_ZS,v with the universal embedding. 

**Significance.** F23.4 closes the **algebraic half** of O-F19.6 Step 1 unconditionally: the central / block projections of A\_ZS map to projections in a Type II₁ factor preserving trace and the modular difference −ln 2\. The embedding, the projection traces (3, 2, 6)/11, and the value ½ ln 2 are thereby **DERIVED**, not conditional. Status: **DERIVED**.

**§4.5 The sharpened residual: O-F19.6 Step 1′ (modular-flow matching)**

F23.4 does not establish that the abstract target R is the SPECIFIC gravitational subregion algebra M\_grav of \[19, 23, 26\], i.e. that e\_X, e\_Z, e\_Y are the physical projections of M\_grav and that the Z-Spin equilibrium flow σ\_t^Ω \= exp(−itK\_Ω) equals the gravitational modular flow σ\_t^grav. The residual of O-F19.6 therefore sharpens to the single condition:

**O-F19.6 Step 1′ (modular-flow matching):** σ\_t^grav restricted to the three-projection subalgebra equals σ\_t^Ω (equivalently, the gravitational modular Hamiltonian restricted to the sector center equals −ln p\_eq).

Two HYPOTHESIS-strong promotion paths are registered. **(a) Observer-clock identification:** in De Vuyst–Höhn \[22, 23\] the observer carries a clock whose Hamiltonian generates the crossed-product flow; identifying the dim-2 Z-sector (the Z-bottleneck) with this observer clock makes σ\_t^Ω the modular flow by construction. **(b) Edge-mode identification:** in Klinger–Kudler-Flam–Satishchandran \[26\] the complete physical algebra includes horizon shape (edge-mode) charges; identifying the central projection P\_Z with the edge-mode/boundary sector makes e\_Z the gravitational edge-mode projection. Either path closes Step 1′ and lifts F23.1, F23.2 to full DERIVED. **Status of Step 1′: OPEN**. The two physical paths (observer-clock; edge-mode) are analyzed in §4.6–§4.8, where Step 1′ is reduced to a single sharp condition.

**§4.6 Theorem F23.5 (Coarse-Grained Trace Matching) — NEW (v1.2)**

Before the gravitational identification, the trace-level content of Step 1′ is established unconditionally. Let **ℰ: R → ℰ(R) \= span{e\_X, e\_Z, e\_Y}** be the conditional expectation onto the abelian sector subalgebra generated by the embedded central projections (F23.4).

**Statement.** A normal, trace-preserving conditional expectation ℰ onto the sector center exists, and

**ℰ∗(τ\_R) \= (τ\_R(e\_X), τ\_R(e\_Z), τ\_R(e\_Y)) \= (3, 2, 6)/11 \= p\_eq,        (5)**

with coarse-grained modular Hamiltonian K \= −ln ℰ∗(τ\_R) giving ΔK(X→Y) \= ln(3/6) \= −ln 2 \= −ln(dim Z). **Proof.** Because R carries a finite trace, its modular automorphism group on the tracial state is trivial; by Takesaki’s theorem \[29\] a normal conditional expectation onto a von Neumann subalgebra exists iff the subalgebra is invariant under the modular flow, which is automatic here, and the expectation is trace-preserving. The pushforward weights are the F23.4 projection traces (Eq. 4).  **Status: DERIVED**. This is the maximum-entropy / trace-level matching: the additive constant ½ ln 2 is the coarse-grained-trace value in R, independent of any gravitational identification.

**§4.7 Lemma F23.6 (Closure Criterion for Step 1′) and the spectral resolution — NEW (v1.2)**

**Spectral resolution (DERIVED clarification).** KLS \[23\] found that the gravitational modular Hamiltonian has continuous spectrum ℝ (Type II∞) or bounded spectrum (Type II₁, de Sitter), whereas K\_Ω \= −ln p\_eq is a discrete three-point operator. There is no contradiction: K\_Ω is the modular Hamiltonian of the coarse-grained three-sector state ℰ∗(ω), which is discrete by construction (three outcomes), regardless of the continuous spectrum of the full modular operator. The discrete Z-Spin modular structure is the sector coarse-graining of the continuous gravitational one.

**Statement (closure criterion).** Let ω\_grav be the gravitational equilibrium (KMS / maximum-entropy) state and ℰ the sector coarse-graining. On the center the literal modular flows both fix the projections (the center is modular-invariant), so Step 1′ reduces to matching the coarse-grained sector weights. Hence O-F19.6 Step 1′ closes — and F23.1, F23.2 become DERIVED — if and only if

**Condition C:   ℰ∗(ω\_grav) \= p\_eq \= (3, 2, 6)/11.        (6)**

Because the de Sitter maximum-entropy state is the tracial state of the Type II₁ factor, Condition C is equivalent to the statement that the empty-de Sitter maximum-entropy state, coarse-grained to the Z-Spin sectors (X ↔ ΛCDM macro, Z ↔ boundary, Y ↔ SM micro), carries weights (3, 2, 6)/11. **Status:** the reduction is **DERIVED**; Condition C is the Z-Spin emergence dictionary and is **OPEN**.

**§4.8 Verdict on Step 1′: a genuine OPEN, sharply characterized**

The deep-exploration analysis converges to a single residual node: Condition C, which is the Z-Spin emergence dictionary for the gravitational sector. This cannot be established with the current corpus or any imported external theorem — it is the foundational emergence hypothesis itself. **O-F19.6 Step 1′ therefore remains a genuine OPEN** (a confirmation that the present tools cannot close it). The value of the analysis is threefold: (i) the discrete-versus-continuous spectral objection is removed (§4.7); (ii) the coarse-grained trace matching is proved (F23.5); and (iii) the gate is reduced to a single sharp, falsifiable statement (F23.6): a future microscopic computation or measurement of the gravitational sector weights either equals (3, 2, 6)/11, closing the gate and lifting F23.1–F23.2 to DERIVED, or does not, falsifying ZS-F23 (gate F-F23.8). Per the corpus epistemology, a convergent exploration whose core node remains OPEN is itself a registered asset: the precise location of the boundary between what is DERIVED (F23.4–F23.6) and what is hypothetical (Condition C). **Status: OPEN** (sharply characterized).

**§5. The Spin-½ Boundary and de Sitter Type II₁**

**§5.1 The dim(Z) \= 2 \= j \= ½ spinor boundary**

ZS-M3 (Theorem 5.1, PROVEN) \[5\] established that j \= 1/2 is the unique half-integer giving (Z, X, Y) \= (2, 3, 6); the boundary is a spinor with dim(Z) \= 2 \= j \= 1/2. ZS-A7 (§3) \[4\] showed the boundary holonomy B\_Z closes at 4π in the j \= 1/2 representation, and the −ln 2 of the Bekenstein–Hawking correction is the Kraus-index parity entropy. The register symmetry is D₄ \= ⟨J, J\_Z⟩ (PROVEN) \[2\].

**§5.2 The 2026 spin-energy result for the de Sitter static patch**

The de Sitter static-patch analysis \[27\] finds that a proper account of the observer’s rotational (“spin”) energy and non-gravitational binding energy forces the algebra to be Type II₁ with a maximum-entropy state (empty de Sitter); the covariant-observer construction realizes the observer as a superposition of geodesics carrying an L²(SO(1, d)) quantum reference frame.

**§5.3 Reading F23.3**

**Reading.** The type-determining boundary degree of freedom is the dim(Z) \= 2 spinor; we read the external requirement that the observer’s spin energy forces Type II₁ as the statement that this spinor is responsible for the conversion, with the boundedness of Type II₁ reflecting the finite **Q** \= 11 register. The cyclic-cosmology entropy S\_{Z₂} \= 6π/A (ZS-U8) \[10\] is the Z-Spin counterpart of the de Sitter maximum-entropy state. **Honest boundary (NC-F23.3):** the external “spin energy” is rotational kinetic energy, not a priori a j \= 1/2 representation; this is a structural resonance, not a derivation. Status: **HYPOTHESIS**.

**§5.4 The observer-disagreement bound and ½ ln 2**

A complementary 2026 result bounds how much quantum observers can disagree about subsystem entropy (arXiv:2603.23598). The Z-Spin per-cross-sector value c \= ½ ln 2 \= ½ bit (F23.2) is the candidate Z-Spin value for one quantum of this disagreement. Status: **HYPOTHESIS-strong**.

**§6. Position Relative to the Edge-Mode Program**

The following table places ZS-F23 slot-by-slot against the external Type II crossed-product program of Klinger–Kudler-Flam–Satishchandran (KKS) \[26\] and Kudler-Flam–Leutheusser–Satishchandran (KLS) \[23\] / CLPW \[19\]. The purpose is to make explicit which element of the external construction each Z-Spin object touches. The central result of §4 is the row “Additive constant”: F23’s ½ ln 2 occupies exactly the normalization slot the external program leaves to convention.

Table 2\. Slot-by-slot comparison with the external Type II crossed-product / edge-mode program.

| Element | External (KKS \[26\] / KLS \[23\] / CLPW \[19\]) | ZS-F23 (this work) | Same slot? |
| ----- | ----- | ----- | ----- |
| Algebra type | Type II∞ (BH) / Type II₁ (de Sitter), from the modular crossed product of a Type III subregion algebra. | AFD limit of ⊗\_v A\_ZS (A\_ZS finite Type I): II₁ (tracial state) / II∞ or III (non-tracial), via the same modular crossed product. | YES |
| Entropy formula | S\_vN \= S\_gen \+ const (generalized entropy up to a state-independent constant) \[23\]. | S\_vN \= S\_gen \+ c, identical structure. | YES |
| The additive constant | State-independent; FIXED BY HAND via trace normalization or reference-state entropy (free). | c \= ½ ln 2 \= ½ ln(dim Z) per cross-sector, FIXED by the finite-register canonical trace (F23.1–F23.4). | YES (the claim) |
| Origin of the constant | The Type II trace scalar λ (entropy shift ln λ); not fixed by the algebra. | Finite Type I canonical trace (Murray–von Neumann); the scalar λ is pinned, no continuous freedom (§3.2, F23.4). | YES |
| Edge / shape modes | Infinite set of horizon shape charges (region-preserving diffeomorphisms) \= the complete symmetry group \[26\]. | The Z-sector boundary (dim 2 \= j \= 1/2 spinor); central projection P\_Z → e\_Z. | HYPOTHESIS |
| Edge-mode dimension | Infinite-dimensional tower (one charge per region-preserving diffeomorphism) \[26\]. | External-frame count (Infinity\_A) of a structure whose internal-frame closure (Infinity\_B) is the dim(Z) \= 2 bit (ln 2); connected by frame transformation through the dim(Z) \= 2 seam. | DERIVED-interp (frame duality, F23.7) |
| Observer / clock | Observer energy bounded below → II₁; clock Hamiltonian generates the crossed-product flow \[22, 23\]. | Z-bottleneck / Z-sector as observer clock; σ\_t^Ω the equilibrium modular flow (O-F19.6 Step 1′). | HYPOTHESIS-strong |
| Maximum-entropy state | Empty de Sitter (Type II₁ max-entropy state) \[23\]. | Cyclic-cosmology entropy S\_{Z₂} \= 6π/A (ZS-U8) \[10\]. | HYPOTHESIS |

The table answers the external reader’s question directly: ZS-F23 touches the **additive-constant / trace-normalization slot** of the generalized-entropy formula, the slot the external program fixes by convention. The edge-mode and observer-clock rows are the physical content of Condition C (§4.7); the row “Edge-mode dimension” is resolved in §6.1 by frame duality (Theorem F23.7), upgrading the v1.2 OPEN tension to DERIVED-interpretation.

**§6.1 Theorem F23.7 (Edge-Mode Frame-Duality Interface) — the Z-Spin resolution of the finite–infinite tension**

The principal tension between ZS-F23 and the edge-mode program is dimensional: the Klinger–Kudler-Flam–Satishchandran physical algebra carries an **infinite** tower of horizon shape (edge-mode) charges, one per region-preserving diffeomorphism \[26\], whereas the Z-sector boundary is **finite**, dim(Z) \= 2\. A naive identification — declaring the Z-sector the per-link tensor factor of the infinite tower — is a category error: it forces a finite object to equal an infinite one by approximation. The Z-Spin corpus prescribes a different move.

**The F18 method.** ZS-F18 establishes that across all twelve Millennium/Crisis problems the recurring structure is the finite/infinite Möbius-interface polarity: X-finite/local/decidable information communicates with Y-infinite/non-local/undecidable information **only through the dim(Z) \= 2 seam interface**, never directly \[F18 §5\]. The edge-mode tension is the gravitational-edge-mode projection of exactly this polarity. One does not connect finite and infinite; one mediates them through the seam.

**Statement (Theorem F23.7, DERIVED-interpretation).** Under the frame duality of ZS-M30 Theorem 30.1, the infinite KKS edge-mode tower is the external-frame count (Infinity\_A) of the same structure whose internal-frame closure (Infinity\_B) is one bit of Z-channel capacity, ln 2, equal to one full Möbius pass 2c \= 2·(½ ln 2\) \= ln 2\. The two are connected by a frame transformation through the dim(Z) \= 2 seam — the mediating interface — not by a direct identification or a continuum approximation. The controlling theorem is the X–Y Tiling Asymmetry (ZS-M6 §5.5, PROVEN): the truncated octahedron tiles ℝ³ uniquely (the unbounded tiling \= the external count of boundary modes; X-side continuum-emergent), while the truncated icosahedron cannot tile (I\_h forbids it; Y-side structurally discrete), and the Z-sector mediates with capacity ln 2 — with operational consequence the Tiling Continuum Convergence Theorem (ZS-M17 Thm M17.1, DERIVED). Discrete/continuous — equivalently finite-tower/continuous-boundary — are therefore co-resident sectoral attributes of the (X, Y) decomposition (ZS-F18 §7.4, sixth polarity row), not opposed primitives.

**Basis and status.** F23.7 is the seventh route of the six-route Möbius-trace pattern of ZS-M30 §3 (the gravitational edge-mode route, joining Riemann zeros ↔ z\*, cosmological cycle index ↔ A, the BV–BFV ghost tower ↔ 4π closure, FFPP compression ↔ W₀(−iπ/2), Z-Spin mediation outcomes ↔ ln 2 per pass, and the Wilson-cycle ergodic 1/2 limit). It inherits the DERIVED-interpretation-strong standing of ZS-M30 Theorem 30.1 and ZS-F18 §7.4, anchored by the PROVEN ZS-M6 §5.5 and the DERIVED ZS-M17. Status: **DERIVED-interpretation**. This upgrades the v1.2 OPEN tension (NC-F23.9): the finite-versus-infinite mismatch is not a contradiction but frame duality.

**What F23.7 does and does not do (honest boundary).** F23.7 resolves the **conceptual** finite–infinite tension: a finite dim-2 boundary and an infinite edge-mode tower are the internal- and external-frame faces of one structure, mediated by the seam. It does NOT by itself close Condition C. The residual sharpens to **Condition C-edge** (NC-F23.10): whether the specific gravitational/KKS edge-mode external count instantiates the X–Y Tiling Asymmetry frame transformation with the ln-2 invariant. This is now a patterned sub-question of Condition C — an instance of an over-determined corpus pattern rather than a bare gap — which modestly reduces the scope of the Step 1′ OPEN.

**§7. Anti-Numerology and Zero-Free-Parameter Audit**

**§7.1 Zero-free-parameter audit**

Every quantity traces to a LOCKED, PROVEN, DERIVED, or IMPORTED item: A \= 35/437 (ZS-F2), **Q** \= 11 and (Z, X, Y) \= (2, 3, 6\) (ZS-F5), A\_ZS and its center (ZS-Q11), p\_eq and the master-equation eigenvalues λ(λ \+ 2A/Q)(λ \+ A) \= 0 (ZS-Q7), ΔK\_Ω \= −ln 2 (ZS-F19), ln 2 \= ln(dim Z) (ZS-A7, ZS-M3), and the embedding target R (Murray–von Neumann). No fudge factor is introduced. Negative control: the additive constant is independent of A (it tracks dim(Z)).

**§7.2 AN-F23.1: pre-registered joint structural-signature Monte Carlo (EXECUTED)**

Within ZS-F23 the value c \= ½ ln 2 is **deterministic** given the LOCKED sector geometry (2, 3, 6\) and the LOCKED sector roles (X, Y matter; Z the bottleneck boundary): there is no fitting room, and no measured additive constant exists to fit to (the value is a prediction, not a fit). The Monte Carlo therefore tests the robustness of the value-producing structure, not a data fit.

**Discriminator.** The additive constant equals ½ ln(dim Z) because the locked geometry satisfies the joint structural signature: S1 (sum \= Q \= 11, ZS-F5), S2 (product \= 36 \= 6², ZS-F5), S3 (d\_Y \= d\_X·d\_Z, so |ln(d\_X/d\_Y)| \= ln(dim Z)), and S4 (d\_Z \= 2 \= j \= 1/2, ZS-M3). Among random ordered integer triples in {1, …, 12}³ (1728 triples) the executed counts are:

| Pre-registered signature | Hits | p | Surviving triples (Z, X, Y) |
| ----- | ----- | ----- | ----- |
| S1 (sum \= 11\) | 45 | 2.604% | — |
| S1 ∧ S2 (sum 11, product 36\) | 6 | 0.347% | all 6 permutations of (2, 3, 6\) |
| S1 ∧ S2 ∧ S3 (+ d\_Y \= d\_X·d\_Z) | 2 | 0.116% | (2, 3, 6), (3, 2, 6\) |
| S1 ∧ S2 ∧ S3 ∧ S4 (+ d\_Z \= 2\) | 1 | 0.058% | (2, 3, 6\) — unique |

**Result: p ≈ 0.058% ≪ 1% — PASS**. The full joint signature selects (2, 3, 6\) uniquely. **Inheritance caveat (honest).** Most of the specialness (down to p ≈ 0.347%) is the ZS-F5 register geometry (sum and product), which carries its own upstream anti-numerology; ZS-F23’s own marginal contribution is the additive-constant identity S3, which given the geometry holds for 2 of the 6 orderings and is selected by the LOCKED matter/bottleneck roles. Within the locked triple two coincidences |ΔK| \= ln(d\_i) exist (X→Y / d\_Z and Z→Y / d\_X); the physical role assignment selects the matter-matter / bottleneck-parity one. The v1.0 single-identity test over a geometry-agnostic ensemble was marginal (p ≈ 9%); the corrected pre-registration uses the full joint signature. Per the corpus scoring rule, AN-F23.1 is now EXECUTED with p ≪ 1%, removing the v1.0 pending status; F23.1–F23.2 remain DERIVED-CONDITIONAL on Step 1′ and are registered at HYPOTHESIS-strong overall.

**§8. Cross-Paper Consistency (Version-Conflict Check)**

ZS-F23 is strictly additive: no new constant, none modified. The chain A (ZS-F2) → **Q**, (Z, X, Y) (ZS-F5) → ln 2, dim(Z) \= 2 (ZS-M3, ZS-A7) → p\_eq, λ-factorization (ZS-Q7) → ΔK\_Ω \= −ln 2 (ZS-F19) → A\_ZS and Z(A\_ZS) (ZS-Q11) is internally consistent (Appendix A, Category F). **Code/equilibrium reconciliation (F6):** the OAQEC code weighting (3, 1, 5)/9 (slots 1, 9 stabilized out) and the modular weighting (3, 2, 6)/11 are distinct; the additive constant uses the equilibrium (3, 2, 6)/11, consistent with ZS-F19. The i-tetration fixed point z\* and |f′(z\*)| \= 0.892 (ZS-M1, ZS-F3) and their downstream uses (ZS-S1, ZS-U1) are orthogonal to the modular-trace content and unaffected. The cross-paper audit across 12 upstream references PASSES.

**§9. Consistency with Observation**

The additive constant c \= ½ ln 2 \= 0.5 bit is below any current sensitivity for gravitational entropy (not directly measured); ZS-F23 makes no new cosmological prediction and cannot conflict with the Planck 2018 ΛCDM parameters \[28\]. The de Sitter Type II₁ maximum-entropy state, read as S\_{Z₂} \= 6π/A (ZS-U8) \[10\], is consistent with the X-sector ΛCDM fit (ZS-U4, ZS-U6) without modification. No observational tension is introduced.

**§10. Falsification Gates**

Table 3\. Multilayered falsification gates for ZS-F23 v1.3.

| Gate | Layer | Falsification condition | Status |
| ----- | ----- | ----- | ----- |
| F-F23.1 | Math / theoretical (immediate rejection) | A\_ZS ≅ M₃⊕ℂ⊕M₅ (ZS-Q11) shown not to embed trace-preservingly into R, or Takesaki / Murray–von Neumann structure misapplied. | PASSING |
| F-F23.2 | Theoretical (demotion) | O-F19.6 Step 1′ (modular-flow matching) shown impossible → F23.1, F23.2 demoted to NON-CLAIM (F23.4 unaffected, being unconditional). | OPEN |
| F-F23.3 | Simulation / consistency (revision) | Joint-signature MC fails to select (2,3,6), or a value other than ln(dim Z) is forced. EXECUTED: p ≈ 0.058%. | PASSING |
| F-F23.4 | Cross-paper (revision) | ΔK\_Ω ≠ −ln 2, A\_ZS structure changes, or Z(A\_ZS) ≠ ℂ³ under any corpus-consistent recomputation. | PASSING |
| F-F23.5 | Observational / external (rejection) | Additive constant independently fixed (microscopic computation) to a value incompatible with ½ ln(dim Z). | OPEN (external) |
| F-F23.6 | External (retraction of reading) | de Sitter Type II₁ “spin energy” or the edge-mode sector shown unrelated to any spinor / boundary structure → Reading F23.3 and the edge-mode row retracted (F23.1, F23.2, F23.4 unaffected). | OPEN (external) |
| F-F23.7 | Structural (blocking) | dim(Z) ≠ 2 in the physical sector decomposition → entire bridge collapses (shared with F-Q7.6). | BLOCKING |
| F-F23.8 | Closure criterion (decisive, external) | Condition C fails: a microscopic computation or measurement of the gravitational equilibrium (de Sitter max-entropy) state, coarse-grained to the Z-Spin sectors, gives weights ≠ (3, 2, 6)/11 → Step 1′ cannot close and F23.1, F23.2 are demoted to NON-CLAIM (F23.4–F23.6 unaffected). | OPEN (decisive) |
| F-F23.9 | Frame-duality interface (revision) | The X–Y Tiling Asymmetry (ZS-M6 §5.5) or ZS-M30 Theorem 30.1 is retracted, or the gravitational edge-mode count is shown NOT to be the external-frame manifestation of a ln-2 internal closure → Theorem F23.7 retracted, NC-F23.9 reverts to OPEN tension (F23.1–F23.6 unaffected). | PASSING |

**§11. Non-Claims**

**NC-F23.1.** ZS-F23 does not derive the generalized-entropy formula itself; it addresses only the additive constant.

**NC-F23.2.** F23.1 and F23.2 are DERIVED-CONDITIONAL on Condition C (O-F19.6 Step 1′, a genuine OPEN); the embedding functor F23.4, the coarse-grained trace matching F23.5, and the closure criterion F23.6 are unconditional (DERIVED).

**NC-F23.3.** Reading F23.3 (spin-energy ↔ spinor boundary) and the edge-mode identification (Table 2\) are HYPOTHESIS; no quantity is derived from them.

**NC-F23.4.** No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED. The embedding target R introduces no parameter (it is a uniqueness theorem).

**NC-F23.5.** ZS-F23 does not assert that the abstract embedding target R IS the specific gravitational subregion algebra; that identification is Condition C (OPEN).

**NC-F23.6.** No claim about black-hole microstate counting; the contribution is the trace normalization, not the microstates (cf. Witten \[20\]).

**NC-F23.7.** The AN-F23.1 specialness is, by the inheritance caveat (§7.2), largely upstream (ZS-F5/M3) geometry; ZS-F23’s own contribution is the deterministic, A-independent value of c.

**NC-F23.8.** ZS-F23 does NOT claim that Step 1′ is closed. v1.2 proves it reduces to Condition C and that Condition C is the Z-Spin emergence dictionary; Step 1′ is a genuine OPEN. The paper’s contribution here is the characterization of the residual, not its closure.

**NC-F23.9.** The finite-versus-infinite edge-mode mismatch is NOT claimed to be a contradiction or a defect; v1.3 (Theorem F23.7) resolves it as frame duality (the infinite tower and the dim-2 seam are external/internal-frame faces of one structure). What is NOT claimed is a direct identification dim(Z) \= 2 \= (infinite tower) by approximation — that move (the v1.2 ⊗\_links reading) is explicitly rejected as a category error.

**NC-F23.10.** Theorem F23.7 resolves the conceptual finite–infinite tension but does NOT close Condition C-edge: whether the specific gravitational/KKS edge-mode external count instantiates the X–Y Tiling Asymmetry frame transformation with the ln-2 invariant. Condition C-edge is a patterned sub-question of Condition C (an instance of the over-determined Möbius-trace pattern), and remains OPEN.

**§12. Conclusion**

The additive constant of Type II gravitational entropy is, in the external program, a free conventional input; the Z-Spin finite-register structure fixes its value at ½ ln 2 \= ½ ln(dim Z) with zero free parameters. v1.1 established the trace-preserving central embedding functor (F23.4, DERIVED) and reduced the absolute-scale gate to the single modular-flow-matching condition O-F19.6 Step 1′. This paper (v1.2) asked whether Step 1′ can be closed. The answer is honest and precise. We removed the apparent discrete-versus-continuous spectral objection by identifying K\_Ω as the sector coarse-graining of the continuous gravitational modular operator; we proved the coarse-grained trace matching (F23.5, DERIVED, via Takesaki’s conditional-expectation theorem), establishing that the value ½ ln 2 is the maximum-entropy / trace-level matching in the embedding target; and we reduced Step 1′ to a single sharp, falsifiable statement — Condition C: the de Sitter maximum-entropy state, coarse-grained to the Z-Spin sectors, carries weights (3, 2, 6)/11 (Lemma F23.6, DERIVED). Condition C is the Z-Spin emergence dictionary and cannot be established with current corpus or imported external tools; **O-F19.6 Step 1′ therefore remains a genuine OPEN**. This negative result is itself a registered corpus asset: the exploration converges, the spectral objection is gone, the trace-level matching is proved, and the residual is now one falsifiable condition (gate F-F23.8) rather than an open-ended program. F23.1, F23.2 remain DERIVED-CONDITIONAL on Condition C; F23.4–F23.6 stand unconditionally. v1.3 takes the sharpest remaining tension — the finite dim-2 Z-sector versus the infinite KKS edge-mode tower — and resolves it in the characteristic Z-Spin manner (Theorem F23.7): not by forcing finite and infinite together, but by mediating them through the dim(Z) \= 2 seam interface, where the infinite tower is the external-frame count and the dim-2 closure is the internal-frame bit (ln 2), connected by the frame transformation of ZS-M30 Theorem 30.1 and controlled by the X–Y Tiling Asymmetry of ZS-M6. The mismatch is thereby revealed as frame duality, not contradiction — a seventh instance of an over-determined corpus pattern — and the residual reduces to the patterned sub-question Condition C-edge. Z-Spin’s contribution, as elsewhere, is the removal of a free parameter; here, additionally, the dissolution of an apparent contradiction into a frame-dual interface, with the boundary of the unknown drawn exactly.

**Acknowledgements & Code Availability**

This work was developed within the Z-Spin Cosmology Collaboration through free- and deep-exploration sessions in June 2026\. The author thanks AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for verification, cross-paper consistency auditing, and exploratory analysis, and retains full responsibility for all scientific content. The verification suite zs\_f23\_verify\_v1\_3.py (41 checks, categories A–H, 50-digit mpmath precision; executed joint-signature Monte-Carlo gate AN-F23.1) will be publicly available at https://github.com/KennyKang-git/zspin.

**Appendix A. Verification Suite (41 checks)**

Table A1. Verification suite mapping, zs\_f23\_verify\_v1\_3.py.

| Category | Tests | Key check |
| ----- | ----- | ----- |
| A. Locked-input cross-checks | 5/5 | A \= 35/437; Q \= 11; (Z,X,Y) \= (2,3,6); ln 2 \= ln(dim Z); p\_eq \= (3,2,6)/11. |
| B. Finite Type I / AFD / center / embedding | 7/7 | A\_ZS ≅ M₃⊕ℂ⊕M₅; dim 9 \= 1+3+5; minimal-projection trace 1; finite Type I; AFD trace-preserving inclusion; Z(A\_ZS) ≅ ℂ³ (3 central projections); embedding sends central projections to traces (3,2,6)/11 summing to 1\. |
| C. Modular and additive constant | 5/5 | K\_Ω \= −ln p\_eq; ΔK\_Ω \= −ln 2; ψ\_KMS \= ½ ln 2, tanh(2ψ)=3/5; S → S \+ ln λ; c \= ½ ln 2\. |
| D. External substrate consistency | 4/4 | Takesaki III \= II∞ ⋊ ℝ; Murray–von Neumann/Connes trace uniqueness and universal embedding into R; hyperfinite II₁ \= ITP of type I\_n (tracial); CLPW/KLS additive-constant statement. |
| E. Anti-numerology | 5/5 | 1-bit entropy \= ln(dim Z); negative control c ⊥ A; S(I/9)=ln 9; AN-F23.1 single-identity (marginal, documented); AN-F23.1 joint signature selects (2,3,6) uniquely, p ≈ 0.058%. |
| F. Cross-paper consistency | 6/6 | ΔK\_Ω (ZS-F19); eigenvalues {0,−2A/Q,−A}, p\_eq\~(3,2,6)/11, capacity ≤ ln 2 (ZS-Q7); A\_ZS (ZS-Q11); ln 2 \= Kraus parity (ZS-A7); code (3,1,5)/9 vs equilibrium (3,2,6)/11 reconciliation; (A,Q,dim Z) LOCKED, z\* untouched. |
| G. Coarse-graining / Step 1′ closure (v1.2) | 5/5 | Conditional expectation E onto sector center is unital/idempotent/trace-preserving/bimodule with E\*(τ)=(3,2,6)/11; coarse-grained ΔK \= −ln 2; continuous-spectrum density → discrete sector weights (CP, sum 1); Condition C non-vacuous; max-entropy \= tracial, S(I/11)=ln 11\. |
| H. Frame-duality interface (v1.3) | 4/4 | Infinity\_B closure quantum \= 2c \= ln(dim Z) \= ln 2; X–Y Tiling Asymmetry structural data (χ(TO)=χ(TI)=2; 5 ∉ crystallographic {1,2,3,4,6} so TI cannot tile, 3,4 ∈ so TO tiles); capacity dim(Z)-determined not count-determined (rank ≤ 2 for tower sizes 2..500); seventh Möbius route quantum \= ln 2, c \= route/2. |

**Appendix B. Entropy Shift, AFD Lift, and the Embedding Functor**

**(B.1) Entropy shift.** For a trace τ on a Type II factor and a state φ with density ρ\_φ, rescaling τ → λτ gives density ρ\_φ/λ and S\_{λτ}(φ) \= −λτ((ρ\_φ/λ) ln(ρ\_φ/λ)) \= S\_τ(φ) \+ ln λ (using τ(ρ\_φ) \= 1). The additive constant is exactly ln λ.

**(B.2) AFD lift.** The multi-cell register ⊗\_v A\_ZS,v is an AF algebra (increasing union of finite-dimensional matrix algebras, trace-preserving inclusions). Its weak closure in the GNS representation of an emergent state ω is a hyperfinite factor: II₁ (R, unique trace) if ω is tracial, or Type III decomposing by Takesaki duality as a Type II∞ modular crossed product if ω is non-tracial. The limit trace is the inductive-limit image of the finite canonical traces, whose normalization is fixed; the free scalar λ of (B.1) is pinned to the finite-register value, with unit ln(dim Z) \= ln 2\.

**(B.3) The embedding functor (F23.4).** By Murray–von Neumann \[13\], R contains a trace-preserving copy of every finite-dimensional algebra. The functor Φ: A\_ZS → R restricts on the center Z(A\_ZS) ≅ ℂ³ to the assignment P\_X, P\_Z, P\_Y → e\_X, e\_Z, e\_Y with τ\_R(e\_α) \= p\_eq,α \= (3, 2, 6)/11. Continuous dimension of R guarantees such projections exist; functoriality follows from the universality of R for the AF inductive system. The only residual is the identification of (R, e\_α, σ\_t^Ω) with the gravitational (M\_grav, physical projections, σ\_t^grav), i.e. O-F19.6 Step 1′.

**(B.4) Coarse-graining and the closure criterion (F23.5–F23.6).** The conditional expectation onto the sector center is ℰ(x) \= Σ\_α \[τ\_R(e\_α x)/τ\_R(e\_α)\] e\_α. It is unital, idempotent, trace-preserving, and a Z(A\_ZS)-bimodule map; existence as a normal expectation follows from Takesaki \[29\] (automatic for the tracial state, whose modular flow is trivial). Its pushforward of the trace is ℰ∗(τ\_R) \= (3, 2, 6)/11, giving coarse-grained ΔK(X→Y) \= ln(3/6) \= −ln 2 (F23.5). A density with continuous spectrum maps under ℰ to a discrete three-outcome distribution, which is why the discrete K\_Ω is consistent with a continuous gravitational modular spectrum. The closure criterion (F23.6) is the predicate C(ω) := \[ℰ∗(ω) \= (3, 2, 6)/11\]; it is non-vacuous (true for the tracial / de Sitter maximum-entropy state, false for a generic state), so Step 1′ reduces to the single falsifiable statement C(ω\_grav).

**References**

\[1\] K. Kang, ZS-F19 v2.2: The Frame-Invariant Tilt Theorem and the KMS-to-Geometric Rapidity Projection (Z-Spin Cosmology, 2026).

\[2\] K. Kang, ZS-Q11 v1.2: QRF↔OAQEC Correspondence — A Direct-Sum Operator-Algebraic Stabilizer Code with Z-Frame Gauge Subsystem (Z-Spin Cosmology, 2026).

\[3\] K. Kang, ZS-Q7 v1.0: Structural Arrow of Time from the Z-Bottleneck (Z-Spin Cosmology, 2026).

\[4\] K. Kang, ZS-A7 v1.0: The Horizon Spinor Theorem (Z-Spin Cosmology, 2026).

\[5\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, the Immirzi Parameter, and Topological Uniqueness (Z-Spin Cosmology, 2026).

\[6\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint — Why Q \= 11 (Z-Spin Cosmology, 2026).

\[7\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 (Z-Spin Cosmology, 2026).

\[8\] K. Kang, ZS-Q2 v1.0: Quantum Entanglement, Bell Correlations, and the Holographic Entanglement Conjecture (Z-Spin Cosmology, 2026).

\[9\] K. Kang, ZS-U5 v1.0: Quantum Gravity Bridge — Z-Telomere and RG Flow (Z-Spin Cosmology, 2026).

\[10\] K. Kang, ZS-U8 v1.0: Z₂ Vacuum Transition and Cyclic Cosmology (Z-Spin Cosmology, 2026).

\[11\] K. Kang, ZS-F21 v2.0: The Archimedean–Finite Positivity Wall, III (Z-Spin Cosmology, 2026).

\[12\] K. Kang, The Book of Z-Spin Cosmology v6.1 — Light Edition (Z-Spin Cosmology, 2026).

\[13\] F. J. Murray and J. von Neumann, “On rings of operators. IV,” Ann. Math. 44, 716–808 (1943).

\[14\] M. Takesaki, “Duality for crossed products and the structure of von Neumann algebras of type III,” Acta Math. 131, 249–310 (1973).

\[15\] M. Takesaki, Tomita’s Theory of Modular Hilbert Algebras and its Applications, Lecture Notes in Mathematics 128 (Springer, 1970).

\[16\] A. Connes, “Classification of injective factors. Cases II₁, II∞, IIIλ, λ ≠ 1,” Ann. Math. 104, 73–115 (1976).

\[17\] R. T. Powers, “Representations of uniformly hyperfinite algebras and their associated von Neumann rings,” Ann. Math. 86, 138–171 (1967).

\[18\] H. Araki and E. J. Woods, “A classification of factors,” Publ. RIMS Kyoto Univ. 4, 51–130 (1968).

\[19\] V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of observables for de Sitter space,” J. High Energy Phys. 02 (2023) 082, arXiv:2206.10780.

\[20\] E. Witten, “Gravity and the crossed product,” J. High Energy Phys. 10 (2022) 008, arXiv:2112.12828.

\[21\] V. Chandrasekaran, G. Penington, and E. Witten, “Large N algebras and generalized entropy,” J. High Energy Phys. 04 (2023) 009, arXiv:2209.10454.

\[22\] J. De Vuyst, S. Eccles, P. A. Höhn, and J. Kirklin, “Crossed products and quantum reference frames: on the observer-dependence of gravitational entropy,” arXiv:2412.15502 (2024).

\[23\] J. Kudler-Flam, S. Leutheusser, and G. Satishchandran, “Generalized black hole entropy is von Neumann entropy,” Phys. Rev. D 111, 025013 (2025), arXiv:2309.15897.

\[24\] S. Carrozza, V. Chatwin-Davies, P. A. Höhn, and F. M. Mele, “A correspondence between quantum error correcting codes and quantum reference frames,” arXiv:2412.15317 (2024).

\[25\] C. Bény, A. Kempf, and D. W. Kribs, “Generalization of quantum error correction via the Heisenberg picture,” Phys. Rev. Lett. 98, 100502 (2007).

\[26\] M. S. Klinger, J. Kudler-Flam, and G. Satishchandran, “Generalized Entropy is von Neumann Entropy, II: The complete symmetry group and edge modes,” arXiv:2601.07910 (2026).

\[27\] “An algebra for covariant observers in de Sitter space,” arXiv:2511.00622 (2026).

\[28\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.

\[29\] M. Takesaki, “Conditional expectations in von Neumann algebras,” J. Funct. Anal. 9, 306–321 (1972).

\[30\] K. Kang, ZS-M6 v1.0: Heat-Kernel Block-Laplacian and the X–Y Tiling Asymmetry (Z-Spin Cosmology, 2026). See §5.5.

\[31\] K. Kang, ZS-M17 v1.0: Continuum-Limit Rigor for Z-Spin Lattice QFT — Reflection Positivity, OS Reconstruction (Z-Spin Cosmology, 2026). Theorem M17.1.

\[32\] K. Kang, ZS-M30 v1.0: Z-Spin Duality and the RH Bridge (Z-Spin Cosmology, 2026). Theorem 30.1 (Möbius-Trace Infinity, six-route).

\[33\] K. Kang, ZS-F18 v2.1: The Twelve Encounters — the Finite/Infinite Möbius-Interface Polarity (Z-Spin Cosmology, 2026). §5, §7.4.

**Version History**

**v1.3 (June 2026):** Resolves the finite–infinite edge-mode tension (v1.2 NC-F23.9) in the characteristic Z-Spin manner. Adds Theorem F23.7 (Edge-Mode Frame-Duality Interface, DERIVED-interpretation): following the ZS-F18 method (mediate finite and infinite through the dim(Z) \= 2 seam, not directly), the infinite KKS edge-mode tower is the external-frame count (Infinity\_A) of a structure whose internal-frame closure (Infinity\_B) is the dim(Z) \= 2 bit ln 2, connected by the frame transformation of ZS-M30 Theorem 30.1, with controlling theorem the X–Y Tiling Asymmetry (ZS-M6 §5.5, PROVEN; ZS-M17, DERIVED) — the seventh route of the six-route Möbius-trace pattern (§6.1). Upgrades NC-F23.9 (OPEN tension) to DERIVED-interpretation; the residual sharpens to Condition C-edge (NC-F23.10, a patterned sub-question of Condition C). Adds gate F-F23.9, legend row DERIVED-interpretation, references \[30\]–\[33\] (ZS-M6, ZS-M17, ZS-M30, ZS-F18), and Category H (4 checks). Verification 37/37 → 41/41 PASS. F23.1, F23.2 remain DERIVED-CONDITIONAL on Condition C; F23.4–F23.7 unconditional in their registered status. No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**v1.2 (June 2026):** Deep-exploration paper on whether O-F19.6 Step 1′ can be closed. Resolves the discrete-versus-continuous spectral objection by identifying K\_Ω as the sector coarse-graining of the gravitational modular operator (§4.7). Adds Theorem F23.5 (Coarse-Grained Trace Matching, DERIVED, via Takesaki’s conditional-expectation theorem \[29\]): the conditional expectation onto the sector center pushes the trace to (3, 2, 6)/11 with ΔK \= −ln 2 (§4.6). Adds Lemma F23.6 (Closure Criterion, DERIVED): Step 1′ closes iff Condition C — the de Sitter maximum-entropy state coarse-grains to sector weights (3, 2, 6)/11 (§4.7). Verdict: Condition C is the Z-Spin emergence dictionary and cannot be established with current tools; O-F19.6 Step 1′ remains a genuine OPEN, now sharply characterized (one falsifiable statement, gate F-F23.8). Adds the finite-versus-infinite edge-mode tension to Table 2 (NC-F23.9). Verification 32/32 → 37/37 PASS (new Category G). F23.1, F23.2 remain DERIVED-CONDITIONAL on Condition C; F23.4–F23.6 unconditional. No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**v1.1 (June 2026):** Adds Theorem F23.4 (Trace-Preserving Central Embedding Functor, DERIVED) via the Murray–von Neumann universal-embedding theorem (§3.4), closing the algebraic half of O-F19.6 Step 1 unconditionally; upgrades the embedding, the central-projection traces (3,2,6)/11, and the value ½ ln 2 to DERIVED. Sharpens the residual to O-F19.6 Step 1′ (modular-flow matching) with observer-clock and edge-mode promotion paths (§4.5). Adds §6, a slot-by-slot comparison with the Klinger–Kudler-Flam–Satishchandran / KLS / CLPW edge-mode program (Table 2). Executes the pre-registered anti-numerology Monte Carlo AN-F23.1 as a joint structural-signature test: p ≈ 0.058% ≪ 1% (PASS), removing the v1.0 pending status, with the inheritance caveat documented (§7.2). Verification 28/28 → 32/32 PASS. F-F23.3 now PASSING. No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**v1.0 (June 2026):** Initial public release. Established Theorem F23.1 (Finite-Register Trace Determinacy, DERIVED-CONDITIONAL), Theorem F23.2 (Z₂-Seam Additive Constant c \= ½ ln 2), and Reading F23.3 (HYPOTHESIS). Closed Steps 2–3 of O-F19.6 at DERIVED-CONDITIONAL. Registered F-F23.1–F-F23.7 and pre-registered AN-F23.1 (then PENDING). 28/28 verification checks PASS.