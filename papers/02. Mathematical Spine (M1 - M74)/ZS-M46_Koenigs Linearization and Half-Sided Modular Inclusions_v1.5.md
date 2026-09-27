# **ZS-M46**

# **Koenigs Linearization and Half-Sided Modular Inclusions: The Cover-Level Translation, a Positive-Energy Standard Pair, and a Cocycle Realization on the Z-Spin Loxodromic Seam**

**Author:** Kenny Kang

**Date:** July 2026

**Theme / Code:** Math Spine / ZS-M46 v1.5 (closure) · Downstream of ZS-A17 / ZS-F31 / ZS-F32 / ZS-A24 / ZS-F33 · Upstream of ZS-M47 / ZS-F37 / ZS-A32 · Program theorem 1 of 3 for the ZS-A31 §6.3 modular-depth line

**Verification:** exact/numerical checks **23/23 PASS** \[SP 5 | K 12 | TW 3 | KLT 3\]; imported-theorem / character / model / guard consistency checks **31/31 pass**. The suite does **not** machine-certify KH1–KH4, factor type, Haag duality, or cocycle realization — these are imported theorems or admissibility conditions. **Zero fitted parameters.** Central result: on the canonical Abel cover u \= Log χ / Log λ *the Z-Spin seam is the unit translation u ↦ u+1 (PROVEN, Theorem M46.3A); the modular dilation is its positive-energy completion, not the seam itself. The intertwiner W\_χ is a Hardy pullback (DERIVED-CONDITIONAL on admissibility KH1–KH4); the Fock HSMI (Theorem A) is DERIVED-CONDITIONAL on KH1–KH4; the realization on the ZS-A24 core is a Cocycle Realization Theorem (CRT-1 factor isomorphism, CRT-2 cocycle covariance, CRT-3 core lift, all DERIVED-CONDITIONAL on the injectivity of the parent factor; CRT-4 exact clock equality OPEN); the relative commutant N′∩M ≅ A(0,1) is DERIVED-CONDITIONAL (model-fixed); μ/2π is the elliptic modulus height h\_K \= Im τ\_K, not a modular time. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED*\*.

# **§0. Abstract**

ZS-A17 named the one object the corpus lacked — an actual half-sided modular inclusion (HSMI) N ⊂ M with a Takesaki resolution — and ZS-A31 §6.3 pre-registered its construction as ZS-M46. This paper supplies the kinematic construction and identifies precisely the single physical statement that remains open. *(Earlier internal versions treated the radial contraction e⁻ᵐ as the modular flow and t₀ \= μ/2π as a “modular time”; v1.4 retracts that reading — see Version History — and identifies the canonical Abel lift as the unit translation.)*

**The role reversal (PROVEN).** In the multiplicative Koenigs coordinate ζ \= χ(z) the Z-Spin iteration is the loxodromic map ζ ↦ λ*ζ (two fixed points, abelian centralizer, no parabolic). On the canonical Abel cover u \= Log χ(z) / Log λ* (principal lift, log λ *\= −μ \+ iθ, fixed by θ ∈ (0,π)) the* same *seam is the unit translation u ∘ f \= u \+ 1 (Theorem M46.3A). No contradiction: Log is a universal covering, not a Möbius automorphism, so fixed-point counts need not match. The corpus datum is therefore the translation*\* U(1) — the generator of the (ax+b) group — and the modular dilation Δⁱᵗ is recovered afterward as its positive-energy completion (Borchers). The seam’s rotation θ enters a helical normal form: with x \= −Re w/μ and η \= Im w \+ (θ/μ)Re w (w \= Log χ), one seam step is exactly x ↦ x+1, η ↦ η.

**What is new vs. what is imported.** The single novel move is the chain *Koenigs germ → canonical Abel translation → positive-energy standard-pair completion* — the identification of the corpus’s own i-tetration dynamics as the translation datum of a standard pair. Everything downstream is the application of established theorems: the Borchers 2π law; the standard-pair / HSMI correspondence (Longo; Rieffel–van Daele); the Connes–Haagerup uniqueness of the injective Type III₁ factor; the Connes cocycle derivative; and the interval relative commutant (Hislop–Longo; Guido–Longo–Wiesbrock).

**Status.** W\_χ is a Hardy pullback, so the positive-energy standard pair and the Fock HSMI (Theorem A) are **DERIVED-CONDITIONAL** on four admissibility conditions KH1–KH4 (bundled as a Suspension-Admissibility hypothesis). The realization on the ZS-A24 continuous core is a **Cocycle Realization Theorem**: factor isomorphism (CRT-1), modular-cocycle covariance (CRT-2), and core lift (CRT-3) are DERIVED-CONDITIONAL on the injectivity of the parent factor; only the *exact* clock equality (CRT-4) is OPEN, and it splits into a central-cocycle form (CRT-4a) and the stronger weight-preserving form (CRT-4b). The relative commutant N′∩M ≅ A(0,1) is DERIVED-CONDITIONAL in a strongly-additive net. The absence of *every* normal conditional expectation, the reformulated clock gate C\_int, the depth selector t\* \= Q, and the metric-dimension-3 Dirac operator are explicit successor problems (NON-CLAIM / OPEN). This is the closure version of ZS-M46. Zero fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

# **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Explicit proof or exact verification; no undischarged assumption. |
| PROVEN-LOCAL | Proven on a neighbourhood of the attracting fixed point (a germ). |
| IMPORTED-PROVEN | Proven in the external literature and used without re-proof; cited. |
| DERIVED | Follows from PROVEN / IMPORTED-PROVEN results by stated steps; no new parameter. |
| DERIVED-CONDITIONAL | Derived modulo explicitly named, falsifiable conditions (e.g. KH1–KH4, parent injectivity, model choice). |
| OBSTRUCTION | A proven negative result: a candidate object fails a required property. |
| OPEN | A genuine, well-posed gap; may carry a finite-decision reduction. |
| NON-CLAIM | Explicitly outside this paper’s scope (deferred to a named successor). |
| CONSISTENCY-CHECK | A numerical, character, model, or scope check that does NOT by itself certify a theorem. |
| RETRACTED | A prior-version claim withdrawn in this version, with reason. |

# **§1. Introduction**

Three corpus lines converge on one object. ZS-A17 v1.5 proved the 3-metric is not reconstructible from spin or information and named the missing input as “a genuine one-sided (half-sided modular) inclusion.” ZS-F36 v2.1 left the metric-scale gate open with the closing path a modular depth e⁻²ᵖᵗ\*. ZS-A31 v1.5 §6.3 pre-registered the program as ZS-M46 → ZS-M47 → ZS-F37. ZS-M46 supplies the first node: the construction of a half-sided modular inclusion from the Z-Spin loxodromic seam.

The construction rests on a single observation about the corpus’s own i-tetration dynamics, and on the disciplined use of established operator-algebra theorems for everything else. The observation is that the seam, correctly lifted, is a *unit translation* — exactly the generator a Borchers–Wiesbrock standard pair is built from. The paper proves this (§3), completes it to a positive-energy standard pair and a Fock HSMI conditionally on four admissibility conditions (§4–§6), realizes it on the ZS-A24 continuous core up to Connes-cocycle conjugacy (§6), and states plainly the one physical identification that remains open.

Locked data (ZS-M1, ZS-F31 App. D): A \= 35/437, Q \= 11, (dim Z, dim X, dim Y) \= (2, 3, 6); κ² \= A/Q \= 35/4807; z *\= 0.43828 \+ 0.36059 i; λ* \= f′(z*) \= (iπ/2)z*, |λ*| \= 0.89151 \< 1, μ \= −ln|λ*| \= 0.1148346250, θ \= arg λ\* \= 2.2592495540.

# **§2. The Koenigs germ (T1) and the local flow**

**Theorem T1 (Koenigs germ). \[PROVEN-LOCAL\].** f(z) \= exp(iπz/2) has an attracting fixed point z *with multiplier λ* \= (iπ/2)z*, |λ*| \= 0.89151 \< 1 (ZS-M1). On a neighbourhood of z *the Koenigs function χ (χ(z*) \= 0, χ′(z*) \= 1\) solves χ∘f \= λ*χ, and in w \= Log χ(z) one iterate is w ↦ w \+ log λ *(mod 2πi), log λ* \= −μ \+ iθ, μ \= 0.1148346250 \> 0, θ \= 2.2592495540 ∈ (0, π).

*Proof.* Take logs of the Schröder equation; μ \= −ln|λ*| \> 0 as |λ*| \< 1, and θ \= arg λ *∈ (0,π). □*  (Exact/numerical: K1–K12.) *The discrete iterate embeds in the local holomorphic flow f\_t \= χ⁻¹(λ*ᵗχ) on the basin; a global ℝ-flow on the original z-plane (global injectivity of χ, non-escape at negative time) is **OPEN** and is not needed — the operator-algebra construction uses the cover translation of §3, not the z-plane map.

# **§3. The obstruction and the role reversal**

**Obstruction Lemma. \[PROVEN, negative\].** The affine half-plane K \= {w : Re w ≤ c} is not a standard real subspace: for c \= 0 it is not closed under real scalar multiplication (v \= −1 ∈ K but (−1)v \= \+1 ∉ K), and K ∩ iK \= {Re ≤ 0} ∩ {Im ≤ 0} \= the third quadrant ≠ {0}, violating H ∩ iH \= {0}; for c ≠ 0 it is affine and omits the origin. *(Consistency: SP6.)* Hence a geometric half-plane cannot be second-quantized directly; the standard subspace must be built on a function space. §4 does so — after §3.1 identifies the correct generator.

## **§3.1 Sphere-level obstruction and cover-level translation (PROVEN): the role reversal**

**Theorem M46.3A. \[PROVEN\].** (a) *Sphere level.* In the multiplicative Koenigs coordinate ζ \= χ(z) the seam ζ ↦ λ*ζ is loxodromic with two fixed points {0, ∞}; its Möbius centralizer is abelian and contains no parabolic subgroup. (b)* Cover level. *On the canonical Abel cover, with u := Log χ(z) / Log λ* (principal lift, log λ\* \= −μ \+ iθ, θ ∈ (0,π)), the seam is the unit translation

*u ∘ f \= u \+ 1 .*

*Proof.* (a) A Möbius map is loxodromic iff it has two distinct fixed points; ζ ↦ λ*ζ fixes {0,∞}, and the centralizer of a loxodromic element in PSL(2,ℂ) is the abelian torus fixing the same pair, which has no parabolic element. (b) On the universal cover of the punctured basin, Log χ(f(z)) \= Log λ* \+ Log χ(z), so u∘f \= (Log λ *\+ Log χ)/Log λ* \= u \+ 1\. □  *(Exact/numerical: KLT1, residual 6×10⁻¹⁵ at the finite-iterate Koenigs limit; the identity itself is exact.)*

**No contradiction with the fixed-point count.** ζ ↦ Log ζ is a *universal covering*, not a Möbius automorphism of the Riemann sphere; fixed-point number is a Möbius invariant, not a covering invariant. The two fixed points of ζ ↦ λ*ζ and the single fixed point (∞) of u ↦ u+1 coexist without conflict.* (Consistency: KLT4.)\*

**The role reversal.** The corpus datum is therefore the **translation** U(1), the generator of the (ax+b) group — not a dilation with a translation missing. The modular dilation Δⁱᵗ is recovered afterward as the positive-energy completion of this translation (§4). This is the central result of ZS-M46 and its one externally-novel move: *Koenigs germ → canonical Abel translation → positive-energy standard-pair completion*. The earlier “missing-generator” reading survives only as clause (a), a scope-limited sphere-level statement.

# **§4. The positive-energy standard pair and the elliptic height h\_K**

**The carrier and the Hardy pullback.** Let ℋ\_u \= H²(ℂ₊) be the Hardy space of the cover strip and set ℋ\_K := {F∘u : F ∈ H²(ℂ₊)} with ‖F∘u‖ := ‖F‖. Then W\_χ : ℋ\_K → H²(ℂ₊), W\_χ(F∘u) \= F, and the seam composition C\_f satisfies W\_χ C\_f W\_χ⁻¹ \= T(1), because C\_f(F∘u) \= F∘(u+1) \= (F∘τ₁)∘u. Via Paley–Wiener, H²(ℂ₊) ≅ L²(ℝ₊, dp) with T(a)ψ(p) \= eⁱᵃᵖψ(p) and generator P \= mult-by-p ≥ 0\. On the common invariant domain C\_c∞(ℝ₊) the dilation D \= ½ \+ p∂\_p satisfies, by direct computation, \[D,P\]ψ \= (½+p∂\_p)(pψ) − p(½+p∂\_p)ψ \= pψ \= Pψ, and D† \= −D, giving the Borchers relation ΔⁱᵗU(a)Δ⁻ⁱᵗ \= U(e⁻²ᵖᵗa) exactly (Δⁱᵗ := e⁻²ᵖᵗᴰ). The verification’s monomial calculation is a *formal coefficient identity* for \[D,P\]=P; the operator-domain statement is analytic, not machine-certified. *(Exact/numerical: SP1–SP4, SP6; consistency SP5, HD1–HD2.)*

**Theorem A (positive-energy standard pair). \[split\].**

(i) *Canonical Hardy standard pair exists.* **\[IMPORTED-PROVEN\].** The positive-energy (ax+b) representation on L²(ℝ₊, dp) carries a unique irreducible standard pair (H, U) with H ⊆ ℋ standard (H \+ iH dense, H ∩ iH \= {0}) and modular operator Δ above (Rieffel–van Daele 1977; Longo 2008).

(ii) *The Koenigs cover realizes that pair.* **\[DERIVED-CONDITIONAL on KH1–KH4\].** Under the Suspension-Admissibility conditions — (KH1) the lifted Koenigs domain is translation-invariant; (KH2) the representation F∘u is unique; (KH3) the seam reflection descends to an antiunitary involution J; (KH4) the pullback norm is non-degenerate on the dynamical domain — W\_χ is a unitary intertwiner and (ℋ\_K, U) is unitarily equivalent to the canonical pair.

*Remark (why conditional).* The standard-pair/HSMI machinery is imported and unconditional; the bridge that applies it to the Koenigs seam is exactly KH1–KH4, which are not proved here. Bundling them into a single **Suspension-Admissibility Lemma** — “the Abel lift admits a translation-invariant suspension domain on which the pullback into H²(ℂ₊) is faithful, norm-nondegenerate, and reflection-compatible” — and proving it would upgrade Theorem A(ii) to DERIVED. It is left as the paper’s principal admissibility hypothesis.

**The elliptic height (retraction of ‘modular time’).** The radial contraction factor e⁻ᵐ is the contraction in the *multiplicative* Koenigs coordinate; **it is not identified with the Tomita modular flow.** Consequently the quantity μ/2π is not a “modular time of one iterate” (a reading used in earlier internal versions and here **RETRACTED**); it is the **elliptic modulus height**

*h\_K := Im τ\_K \= μ / (2π) \= 0.0182765 ,   τ\_K \= (log λ\*)/(2πi) \= θ/2π \+ iμ/2π ,*

the imaginary part of the E\_{λ*} modulus (ZS-F33). The identity e⁻²ᵖʰ\_K \= |λ*| holds exactly but is a diagnostic relation among modulus data, not a statement about a modular clock. *(Consistency: SP5, TW1–TW3.)*

# **§5. The helical normal form (θ)**

**Helical normal form. \[DERIVED\].** In the log-Koenigs coordinate w \= Log χ one seam step is w ↦ w − μ \+ iθ. Setting x \= −Re w/μ and η \= Im w \+ (θ/μ)Re w gives exactly

*x ↦ x \+ 1 ,   η ↦ η ,   slope θ/μ \= 19.674 .*

So the seam is a **real unit translation** (x, the generator of §3.1–§4) carrying a **helical internal holonomy** (η, invariant, of slope θ/μ). The rotation θ is thus not a component of the modular generator but the internal cycle of the E\_{λ*} torus — Re τ\_K \= θ/2π is its twist. A purely dilational (θ \= 0\) germ would lose this internal cycle; the seam is loxodromic because the corpus carries both a translation and an internal holonomy.* (Exact/numerical: KLT2, KLT3; consistency KLT4.)\*

# **§6. The half-sided inclusion and the Cocycle Realization Theorem**

## **§6.1 The Fock HSMI (Theorem A′)**

**Theorem A′ (Fock HSMI). \[DERIVED-CONDITIONAL on KH1–KH4\].** Given the standard pair (H, U) of §4, its second quantization (Longo 2008\) yields a von Neumann algebra M \= ℛ(H) on Fock space with cyclic-separating vacuum Ω, and N := U(1)MU(−1) ⊂ M is a standard HSMI with the Borchers relations. The construction is imported once (H, U) is in hand; its Z-Spin content is the realization of (H, U) by the Koenigs cover (Theorem A(ii)), hence the conditionality on KH1–KH4. It concerns the lifted/suspension dynamics; the original z-plane global flow is not claimed.

## **§6.2 The 2π law (T5) and the chain (T6)**

**T5 (the 2π law). \[IMPORTED-PROVEN; instantiation DERIVED-CONDITIONAL\].** The relation ΔⁱᵗU(a)Δ⁻ⁱᵗ \= U(e⁻²ᵖᵗa), with 2π fixed by Tomita–Takesaki, is imported (Borchers 1992; Wiesbrock 1993\) and holds exactly in the §4 model. Its instantiation on the Z-Spin seam is DERIVED-CONDITIONAL on KH1–KH4 (via Theorem A′). ZS-M46 contributes not the 2π but the identification of the seam as the translation the law acts on.

**T6 (the chain). \[unit PROVEN; chain DERIVED-CONDITIONAL on KH1–KH4\].** The identification f ↔ U(1) is now a theorem (Theorem M46.3A: u∘f \= u+1 fixes the unit step *canonically*, not by choice), so the Wiesbrock relations generate the integer chain N\_k \= U(k)MU(−k) with an intrinsic unit. The chain’s existence as von Neumann inclusions is conditional on Theorem A′ (hence KH1–KH4); the affine 2×2 check (B7) is a consistency shadow, not a von Neumann check. Selection of a terminal depth k \= Q is **NON-CLAIM** (→ ZS-F37).

## **§6.3 Genuineness (T4)**

**T4 (genuineness). \[split\].** If Theorem A′ holds, the modular group moves N (σ\_t(N) \= N\_{exp(−2πt)} ≠ N), so by Takesaki (1972) **no Ω- or chosen-weight-preserving normal conditional expectation M → N exists** (DERIVED-CONDITIONAL). The absence of *every* normal conditional expectation (any state) needs an independent index / operator-valued-weight obstruction and is **OPEN**. “Genuine \= no CE” is this paper’s strengthened definition, flagged as such; the role separation from the ZS-F32 averaging expectations E\_face / E\_reg (which are CE) stands.

## **§6.4 The relative commutant (Theorem C)**

**Theorem C (relative commutant). \[DERIVED-CONDITIONAL, model-fixed\].** *Fix the realization to a strongly-additive, Haag-dual chiral net* (e.g. the U(1)-current net attached to the standard pair by GLW). Then M \= A(0,∞), N \= A(1,∞), and by Haag duality plus the intersection property N′∩M \= A((0,∞)∩(−∞,1)) \= A(0,1) — a non-trivial Type III₁ factor with Ω cyclic-separating, whose interval modular flow (Hislop–Longo 1982\) fixes {0,1} with endpoint rate ±2π. Strong additivity is what keeps the intersection non-trivial (a general HSMI can have trivial relative commutant), so the conclusion depends on both the model choice and, upstream, KH1–KH4. *(Consistency: RC1–RC3.)* This is the first explicit operator-algebraic datum *selected for* the Z-Spin realization; A(0,1) itself is a known structure of the chosen net, and ZS-M46’s contribution is to attach it to the Koenigs lift.

## **§6.5 The Cocycle Realization Theorem**

The realization on the ZS-A24 continuous core decomposes into four steps, replacing the over-strong “exact flow equality” of earlier drafts by the canonical cocycle relation. Let M\_K be the second-quantized Koenigs factor and M\_A the ZS-A24 parent Type III₁ factor 𝒜^III.

**CRT-1 (factor isomorphism). \[DERIVED-CONDITIONAL\].** M\_K is a hyperfinite Type III₁ factor (Araki–Woods / Wiesbrock). If M\_A is injective Type III₁, then by Connes–Haagerup uniqueness there is a ∗-isomorphism Φ : M\_K → M\_A. *Condition:* the injectivity/hyperfiniteness of M\_A. (CLPW’s stated output is a Type II₁ observer algebra; that the underlying de Sitter parent is injective Type III₁ is standard for free/generalized-free fields but is carried here as a condition, not a quoted conclusion.)

**CRT-2 (cocycle covariance). \[DERIVED-CONDITIONAL on CRT-1\].** For weights φ\_K, φ\_A the Connes cocycle u\_t \= (D(φ\_K∘Φ⁻¹) : Dφ\_A)\_t satisfies Φ σ\_t^{φ\_K} Φ⁻¹ \= Ad(u\_t) ∘ σ\_t^{φ\_A}: the two modular flows are cocycle-conjugate (Connes’ Radon–Nikodym theorem). Defining u\_t requires Φ, hence the dependence on CRT-1.

**CRT-3 (core lift). \[DERIVED-CONDITIONAL on CRT-1\].** Crossed products by cocycle-conjugate actions are isomorphic, so Φ lifts to M\_K ⋊\_σ ℝ ≅ M\_A ⋊\_σ ℝ \= C\_ω, the ZS-A24 core.

**CRT-4 (exact clock matching). \[OPEN, two forms\].** Two modular flows coincide *exactly* iff (Dψ:Dφ)\_t ∈ Z(M); in a factor this is (Dψ:Dφ)\_t \= eⁱᶜᵗ·1. Hence: **CRT-4a** (central-cocycle clock equality, σ\_t^{φ\_K}∘Φ \= Φ∘σ\_t^{φ\_A} up to a central phase) — OPEN; **CRT-4b** (normalized weight-preserving equality, u\_t \= 1\) — OPEN, strictly stronger. *(Consistency: CO1–CO4.)*

**Theorem B, split. \[B\_abs DERIVED-CONDITIONAL; B\_phys OPEN\].** *Abstract transport* (B\_abs): granting CRT-1 and KH1–KH4, Φ carries the Fock HSMI N\_K ⊂ M\_K to a standard HSMI Φ(N\_K) ⊂ M\_A on the core — DERIVED-CONDITIONAL. *Physical identification* (B\_phys): that Φ(N\_K) equals the algebra/weight ZS-A24 physically designates for the seam (Φ σ\_t^K Φ⁻¹ \= σ\_t^{A24} on the nose) requires CRT-4 — OPEN. So the inclusion *structure* transports (up to cocycle conjugacy), while the *physical clock identification* is the single remaining physical claim of ZS-M46.

# **§7. The register measure (T7a) and the reformulated clock gate (T7b)**

**T7a (register measure). \[A24-derived conditional corollary\].** On the ZS-A24 Type II₁ corner M\_obs \= eC\_ωe the normal tracial state τ is unique (Murray–von Neumann); under the register embedding ι the eleven rank-one microstate projections carry τ(e\_α) \= 1/11, so the induced density is ρ\_Q \= I\_Q/Q. This follows from the A24 matrix embedding and the II₁ unique trace, **not** from the HSMI; it populates the ZS-M44 route (ii) only as the unique KMS state of the *trivial* (tracial) flow. A concrete route to promote it to DERIVED is to verify, on the actual ZS-F31 GKLS generator L, that L*(I\_Q/Q) \= 0 with ker L* \= ℂ·(I\_Q/Q) (primitivity) — a finite computation deferred to ZS-M44/F31. *(Consistency: C4.)*

**T7b (clock gate C\_int). \[OPEN-REFORMULATION\].** The pre-role-reversal ratio test μ/ω\_Z \= θ/ν\_Z read the seam as a dilation and is **not used** after the role reversal. With the seam a translation, the clock gate must be rewritten in terms of the translation generator P\_K, the A24 modular Hamiltonian K\_A, and the central Connes cocycle — e.g. as Φ(P\_K) \= P\_A, or (Dφ\_K∘Φ⁻¹ : Dφ\_A)\_t ∈ ᵀ·1 (a central phase). This coincides with CRT-4a. The residual is the explicit ZS-F31 seam diagonalization; C\_int is **OPEN** as a finite, well-posed reformulated computation, not the old ratio comparison. *(Consistency: CI1.)*

# **§8. The scale boundary (NON-CLAIM)**

ZS-M46 provides only dimensionless modular structure. **(N1)** depth selection t *\= Q → ZS-F37 (T6 gives at most a conditional ladder, no terminal rung). (N2) the metric-dimension-3 Dirac operator → ZS-M47 (one inclusion gives 1D chiral data; ≥ 3 inclusions in modular position are needed for a 3-metric). (N3) the absolute scale → the ZS-F36.T7 / ZS-A27 / ZS-A28 Buckingham-π no-go is inviolate: the model fixes the* shape *(the modulus τ\_K, the height h\_K, the exponent 2π, the unit step) but never the* size*. The only dimensionful comparison, e⁻²ᵖᵑ, is quarantined behind the regression firewall (C7) and feeds nothing.* (Consistency: C7, C8.)\*

# **§9. Zero-parameter and cross-version audit**

**Zero fitted parameters.** μ \= 0.1148346250, θ \= 2.2592495540, |λ\*| \= 0.89151 are ZS-M1; h\_K \= Im τ\_K \= μ/2π and the slope θ/μ are definitions on those; A \= 35/437, Q \= 11, κ² \= 35/4807 are LOCKED; 2π is the Tomita–Takesaki constant. The one observational number, e⁻²ᵖᵑ, is firewalled (C7). No fudge factor.

**Cross-version dependency trace.** ZS-M1: used only via λ *and the local germ; z* and |λ*| \< 1 untouched, so the M1 → S1 → U1 chain is safe. ZS-F31: C\_int is* reformulated *(T7b), not evaluated; no value altered. ZS-F32: F32.1 respected; E\_face/E\_reg preserved. ZS-F33: E\_{λ*} periods and modulus τ\_K used verbatim (§4–§5). ZS-A17: the inclusion-source input is realized up to Connes-cocycle conjugacy and the KH/CRT conditions — the metric NO-GO is untouched. ZS-A24: the II∞ core, II₁ corner, and ι are used verbatim; the parent Type III₁ factor is the CRT-1 target. ZS-A31: the 2π is contextualized as imported; the metric-scale gate and t\* stay OPEN/NON-CLAIM. No upstream status is reversed.

**Observational non-collision.** ZS-M46 makes no dimensionful prediction, so it cannot collide with Planck 2018 ΛCDM or Standard-Model couplings; the frozen w \= −1 branch (via ZS-F33/A28) is unchanged. DESI DR2 dark-energy preferences bear on the ZS-A31 scale line, not on the dimensionless structure here.

# **§10. Falsification gates**

**Tier 1 — mathematical / immediate rejection.**

F-M46.1. If μ ≤ 0, the attracting Koenigs germ and the chosen one-sided positive-energy orientation fail; the algebraic cover identity u∘f \= u+1 itself need not fail (it holds whenever log λ *≠ 0).* PASS:\* μ \= 0.1148 \> 0 (K9).

F-M46.2. If u∘f ≠ u+1 on the cover, the role reversal fails. *PASS:* KLT1 (residual 6×10⁻¹⁵, germ-approx limit; identity exact).

F-M46.3. If the affine half-plane were a standard subspace, the Obstruction Lemma is false. *Result:* it is not (SP6); the direct half-plane route is excluded.

**Tier 2 — admissibility / structural.**

F-M46.4. If no translation-invariant suspension domain exists (KH1–KH4 unsatisfiable), W\_χ is not a standard-pair intertwiner and Theorem A(ii), A′ collapse to the canonical pair only. *Status:* OPEN admissibility — the paper’s principal conditional.

F-M46.5. If M\_A is not injective Type III₁, CRT-1 fails and the core realization is void. *Status:* OPEN condition on the parent factor.

F-M46.6. If (Dφ\_K∘Φ⁻¹ : Dφ\_A)\_t ∉ ᵀ·1 for every admissible Φ, then no clock identification exists (CRT-4a fails) and B\_phys is refuted. *Status:* OPEN — the single remaining physical gate.

**Tier 3 — scope / numerology guard.**

F-M46.7. Any derivation-module equation setting k \= Q, or fixing a dimensionful scale from A, Q, topology alone, is void by Buckingham-π. *PASS:* C8; e⁻²ᵖᵑ firewalled (C7).

F-M46.8. If consistency checks (character identities, imported-theorem echoes, guards) were counted as theorem certification, the verification would be over-stated. *PASS:* they are reported as a separate tier (31 consistency vs 23 exact/numerical).

# **§11. Conclusion**

ZS-M46 closes with a clean separation of what is new from what is imported. **New:** the single chain *Koenigs germ → canonical Abel translation → positive-energy standard-pair completion* — the identification of the corpus’s i-tetration seam as a unit translation on the Abel cover (Theorem M46.3A, PROVEN), from which the positive-energy standard pair, the Fock HSMI, and the helical normal form follow. **Imported:** the Borchers 2π law, the standard-pair/HSMI correspondence, the Connes–Haagerup uniqueness of the injective Type III₁ factor, the Connes cocycle derivative, and the interval relative commutant. ZS-M46’s contribution is the bridge, not the imported machinery.

The honest terminus is a conditional realization with one physical residual. The kinematic construction is complete modulo the Suspension-Admissibility conditions KH1–KH4; the core realization holds up to Connes-cocycle conjugacy (CRT-1–3, conditional on the parent factor’s injectivity); and the modular dilation is recovered as the completion of the seam translation, with μ/2π read correctly as the elliptic height h\_K, not a modular time. Four items are explicit successor problems and are **not** pursued further here: exact clock equality (CRT-4 / B\_phys), the absence of every normal conditional expectation, the reformulated C\_int, and the depth selector t\* \= Q. This is the first of the three ZS-A31 §6.3 program theorems, closed to the extent its evidence supports and no further. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

# **§12. Claim ledger (v1.4, final)**

| \# | Claim | Status |
| ----- | ----- | ----- |
| T1 | Koenigs germ: iterate \= translation w ↦ w \+ log λ\*, μ \> 0 | PROVEN-LOCAL |
| Obstruction | affine half-plane is not a standard subspace | PROVEN (negative) |
| M46.3A(a) | sphere-level: loxodromic, abelian centralizer, no parabolic | PROVEN (scope-limited) |
| M46.3A(b) | cover-level: u∘f \= u+1 (unit translation) | PROVEN (role reversal) |
| — | positive-energy model P ≥ 0, \[D,P\]=P, Borchers 2π | IMPORTED-PROVEN \+ verified |
| Helical | θ: x↦x+1, η↦η, slope θ/μ | DERIVED |
| h\_K | μ/2π \= Im τ\_K (elliptic height; ‘modular time’ retracted) | DERIVED (relabelled) |
| W\_χ | Hardy pullback intertwiner | DERIVED-CONDITIONAL (KH1–KH4) |
| A(i) | canonical Hardy standard pair exists | IMPORTED-PROVEN |
| A(ii)/A′ | Koenigs cover realizes it; Fock HSMI | DERIVED-CONDITIONAL (KH1–KH4) |
| T4 | no chosen-weight CE / any CE | DERIVED-COND / OPEN |
| T5 | ΔⁱᵗU(a)Δ⁻ⁱᵗ \= U(e⁻²ᵖᵗa) | IMPORTED-PROVEN; inst. DERIVED-COND |
| T6 | unit-depth chain N\_k (unit canonical) | unit PROVEN; chain DERIVED-COND |
| Thm C | N′∩M ≅ A(0,1), III₁, rate ±2π | DERIVED-CONDITIONAL (model-fixed) |
| CRT-1 | factor isomorphism Φ : M\_K ≅ M\_A | DERIVED-CONDITIONAL (injectivity) |
| CRT-2/3 | cocycle covariance; core lift | DERIVED-CONDITIONAL on CRT-1 |
| CRT-4a/4b | exact clock equality (central / weight-preserving) | OPEN / OPEN (stronger) |
| B\_abs / B\_phys | abstract transport / physical identification | DERIVED-COND / OPEN |
| T7a | ρ\_Q \= I\_Q/Q | A24 corollary (GKLS-primitivity path) |
| T7b | C\_int | OPEN-REFORMULATION |
| N1/N2/N3 | t\*=Q / Dirac / absolute scale | NON-CLAIM |

# **§13. Verification**

zs\_m46\_verify\_v1\_4.py (SymPy \+ mpmath 60-digit \+ NumPy), two honestly separated tiers. **The suite does not machine-certify KH1–KH4, factor type, Haag duality, strong additivity, or cocycle realization** — these are imported theorems or admissibility conditions.

**EXACT / NUMERICAL — 23/23 PASS.** *SP (5):* positivity min σ(P) \> 0; \[D,P\]=P (a formal coefficient identity, common domain C\_c∞(ℝ₊)) and D†=−D; the Borchers relation; the affine half-plane obstruction (SP6). *K (12):* the Koenigs / ZS-M1 germ data. *TW (3):* the E\_{λ*} modulus and factorization.* KLT (3):\* the cover translation u∘f \= u+1 and the helical split x↦x+1, η↦η.

**CONSISTENCY — 31/31 pass (do NOT certify the theorems).** *SP5:* the diagnostic identity e⁻²ᵖʰ\_K \= |λ*| (h\_K \= Im τ\_K, not a modular time).* HD1–HD2: *the translation-character identity for W\_χ (not KH1–KH4 / unitarity / surjectivity).* RC1–RC3: *imported Haag-duality / Hislop–Longo echoes for A(0,1).* KLT4: *the sphere-vs-cover fixed-point statement.* CO1–CO3: *the cocycle chain identity, hyperfinite III₁ uniqueness, and crossed-product isomorphism;* CO4a/CO4b: *the two exact-equality gates (automorphism u\_t∈ᵀ·1, and weight-preserving u\_t=1).* CI1, C6 (guards): *the C\_int gate reformulated via CRT-4a, the old ratio test absent;* CI2: *the h\_K note.* B (8), C (6), R (3):\* affine 2×2 shadows, corpus arithmetic \+ firewall, cross-version identities.

# **§14. Acknowledgements & Code Availability**

zs\_m46\_verify\_v1\_5.py reproduces all 54 checks (23 exact/numerical \+ 31 consistency). This work used AI tools (Anthropic Claude) for external-literature search, cross-paper integration, symbolic/numerical verification, and drafting, under Kenny Kang’s editorial direction. The role reversal (the cover-level translation), the CRT decomposition, and the honest verification re-classification were made in response to iterated external technical review; the author assumes full responsibility for all content.

# **§15. Appendix A — Deep-exploration (issue-tree) record**

**Step 0 (long list, 7).** (1) the kinematic lift — what is the seam’s actual generator; (2) the positive-energy realization; (3) the operator-algebra/core realization; (4) downstream selection (chain, register, C\_int, t\*); (5) the relative commutant; (6) genuineness / no-CE; (7) global flow. Dropped as standalone: (7) resolved by the cover lift (PROVEN on the cover; z-plane OPEN, not needed); (5),(6) folded into (3),(4).

**Step 1 (MECE, 4).** I1 kinematic lift (the Abel cover); I2 positive-energy standard pair (Hardy pullback); I3 algebra/core realization (CRT); I4 downstream (chain / register / C\_int / t\*).

**Steps 2–3 (tree \+ status).** I1 → I2 → I3 → I4. I1: Theorem M46.3A PROVEN. I2: A(i) IMPORTED-PROVEN, A(ii)/A′ DERIVED-CONDITIONAL on KH1–KH4. I3: CRT-1/2/3 DERIVED-CONDITIONAL, CRT-4 OPEN; Theorem C DERIVED-CONDITIONAL (model-fixed). I4: T5 imported+conditional, T6 unit PROVEN/chain conditional, T7a A24 corollary, T7b OPEN-reformulation, t\*=Q NON-CLAIM.

**Step 4 (convergence).** Across versions the number of nodes whose status *changed* per re-traversal fell 9 → 4 → 3 → 0 (a convergence criterion on the *change count*, not on the residual OPEN count) as the role reversal (v1.3) and the status/verification corrections (v1.4–v1.5) were applied, with no reversals; the exploration **converges**. The residual OPENs (KH1–KH4, CRT-1 injectivity, CRT-4/B\_phys, any-CE, C\_int, t\*=Q) are genuine successor problems requiring new input or explicit finite computation, not decomposition failures.

**Step 5 (value).** Converged \+ corpus non-collision (the downgrades and the obstruction remove over-claims; A24/F31/F33 used verbatim) \+ anti-numerology (the new results — u∘f \= u+1, the helical split — are parameter-free; the imported machinery adds none). The value is an honest, externally-legible construction paper whose one novel connection is precisely delimited from its imported components.

## **Appendix B — Key numerics**

| Quantity | Value | Role |
| ----- | ----- | ----- |
| z\* (i-tetration fixed point) | 0.438282936727 \+ 0.360592471871 i | ZS-M1 PROVEN |
| λ *\= (iπ/2)z* | |λ\*| \= 0.891513565776 \< 1 | multiplier, attracting |
| μ \= −ln|λ\*| | 0.114834624996 | contraction; sets the translation unit; \> 0 |
| θ \= arg λ\* | 2.259249553900 | internal holonomy; ∈ (0, π) |
| τ\_K \= θ/2π \+ iμ/2π | Im τ\_K \= μ/2π | E\_{λ\*} elliptic modulus (F33) |
| h\_K \= Im τ\_K \= μ/(2π) | 0.018276498210 | elliptic modulus height (NOT a modular time) |
| slope θ/μ | 19.673944 | helical normal-form slope |
| e⁻²ᵖᵑ (firewalled) | 9.632×10⁻³¹ | A31 §6.3 comparison only; no derivation use |

# **§16. References**

\[1\] H.-J. Borchers, “The CPT-theorem in two-dimensional theories of local observables,” Commun. Math. Phys. 143, 315–332 (1992).

\[2\] H.-W. Wiesbrock, “Half-sided modular inclusions of von Neumann algebras,” Commun. Math. Phys. 157, 83–92 (1993); Erratum, ibid. 184, 683–685 (1997).

\[3\] H. Araki and L. Zsidó, “Extension of the structure theorem of Borchers and its application to half-sided modular inclusions,” Rev. Math. Phys. 17, 491–543 (2005), arXiv:math/0412061.

\[4\] R. Longo, “Real Hilbert subspaces, modular theory, SL(2,ℝ) and CFT,” in Von Neumann Algebras in Sibiu, Theta Ser. Adv. Math., 33–91 (Theta, Bucharest, 2008).

\[5\] M. A. Rieffel and A. van Daele, “A bounded operator approach to Tomita–Takesaki theory,” Pacific J. Math. 69, 187–221 (1977).

\[6\] P. Koosis, Introduction to H\_p Spaces, 2nd ed. (Cambridge Univ. Press, 1998\) \[Hardy space, Paley–Wiener realization\].

\[7\] P. D. Hislop and R. Longo, “Modular structure of the local algebras associated with the free massless scalar field theory,” Commun. Math. Phys. 84, 71–85 (1982).

\[8\] D. Guido, R. Longo, and H.-W. Wiesbrock, “Extensions of conformal nets and superselection structures,” Commun. Math. Phys. 192, 217–244 (1998), arXiv:hep-th/9703129.

\[9\] A. Connes, “Une classification des facteurs de type III,” Ann. Sci. Éc. Norm. Supér. 6, 133–252 (1973).

\[10\] U. Haagerup, “Connes’ bicentralizer problem and uniqueness of the injective factor of type III₁,” Acta Math. 158, 95–148 (1987).

\[11\] H. Araki and E. J. Woods, “A classification of factors,” Publ. RIMS Kyoto 4, 51–130 (1968).

\[12\] M. Takesaki, “Conditional expectations in von Neumann algebras,” J. Funct. Anal. 9, 306–321 (1972).

\[13\] F. J. Murray and J. von Neumann, “On rings of operators,” Ann. of Math. 37, 116–229 (1936) \[uniqueness of the II₁ trace\].

\[14\] V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of observables for de Sitter space,” JHEP 02 (2023) 082, arXiv:2206.10780.

\[15\] G. Koenigs, “Recherches sur les intégrales de certaines équations fonctionnelles,” Ann. Sci. Éc. Norm. Supér. (3) 1, Suppl. 3–41 (1884); J. Milnor, Dynamics in One Complex Variable, 3rd ed. (Princeton, 2006), §8.

\[16\] K.-H. Neeb and G. Ólafsson, “From local nets to Euler elements,” arXiv:2312.12182 (2023).

\[17\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.

\[18\] ZS-M1, The i-Tetration Fixed Point and the Exponential-Homomorphism Uniqueness (Z-Spin corpus).

\[19\] ZS-F31, Covariant Cosmic Reality — the Exact Modular GKLS Spectrum and the Causal-Entropic Present Gate (Z-Spin corpus).

\[20\] ZS-F32, The Conditional-Expectation Lift of the Z-Spin Continuous Core (Z-Spin corpus).

\[21\] ZS-F33, The Conditional UV Reduction of the Z-Spin Odd Three-Form (Z-Spin corpus).

\[22\] ZS-A17, The Curvature–Spin–Metric Trichotomy and the Spin–Metric Independence No-Go (Z-Spin corpus).

\[23\] ZS-A24, Dimension-Weighted Mediator Semigroups and Their Spin-Graded Continuous-Core Lift (Z-Spin corpus).

\[24\] ZS-F36, The Integral UV Normalization of the Z-Spin Odd Three-Form (Z-Spin corpus).

\[25\] ZS-A27 / ZS-A28, The Z-Spin Vacuum-Energy Scale — A–Q-Only Scale-Generation No-Go / Projector-Valued Top Form (Z-Spin corpus).

\[26\] ZS-A31, The Effective One-Parameter Reduction of the Z-Spin Vacuum-Energy Line (Z-Spin corpus).

\[27\] ZS-M44, The Conditional Register-Trace Normalization of the Z-Spin Block-Laplacian (Z-Spin corpus).

# **§17. Version History**

**v1.0 (July 2026):** Initial internal draft (never publicly finalized). Read the radial contraction e⁻ᵐ as a modular dilation, treated the affine half-plane as a standard datum, and claimed a genuine standard HSMI (DERIVED). Consolidated from internal Z-Spin Collaboration research notes.

**v1.1:** Retracted the standard-subspace step (Obstruction Lemma, PROVEN negative); built the explicit positive-energy model; introduced t₀ \= μ/2π as a “modular time” (DERIVED-CONDITIONAL on an intertwiner W\_χ, then OPEN).

**v1.2:** Added the Missing-Generator Lemma (the abelian seam supplies only a dilation), the relative commutant N′∩M ≅ A(0,1), and the Central Realization Hypothesis consolidating three open items.

**v1.3:** The role reversal — on the Abel cover u \= Log χ / Log λ\* the seam is the unit translation u∘f \= u+1 (PROVEN). W\_χ became a Hardy pullback; the CRH was replaced by the Cocycle Realization Theorem; t₀ was reinterpreted as the elliptic height.

**v1.4 (July 2026): Closure release.** Purges the residual v1.0–v1.2 framing that conflicted with the role reversal, and corrects status over-claims flagged in review: t₀ \= μ/2π is uniformly the elliptic height h\_K \= Im τ\_K, not a modular time (§4, Appendix B, verification SP5 moved to consistency); Theorem A is split into an IMPORTED-PROVEN canonical pair and a DERIVED-CONDITIONAL Koenigs realization (KH1–KH4, bundled as a Suspension-Admissibility hypothesis); Theorem B is split into abstract transport (DERIVED-CONDITIONAL) and physical identification (OPEN); CRT-2/3 are made DERIVED-CONDITIONAL on CRT-1, and CRT-4 is split into central-cocycle (4a) and weight-preserving (4b) forms, correcting the over-strong “iff u\_t \= 1”; Theorem C is DERIVED-CONDITIONAL (model-fixed); C\_int (T7b) is marked OPEN-REFORMULATION in terms of P\_K, K\_A, and the central cocycle; and the verification is re-classified into 24 exact/numerical and 29 imported-theorem/character/model/guard consistency checks, with an explicit disclaimer that KH1–KH4, factor type, Haag duality, and cocycle realization are not machine-certified. This closes ZS-M46; the residual problems (CRT-4/B\_phys, any-state CE, C\_int, t\*=Q, the metric-dimension-3 Dirac operator) are named successors. Zero fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**v1.5 (July 2026): Final closure release.** Editorial/consistency pass making the paper text and the verification script exactly agree, with no new mathematics. Corrections: (i) the verification classification is fixed — SP5 (the h\_K identity) is moved from exact to consistency, giving **23 exact/numerical \[SP 5 | K 12 | TW 3 | KLT 3\] \+ 31 consistency \= 54**, matching the script; (ii) the retracted C\_int ratio test is removed from the code (C6, CI1 become guards registering C\_int as OPEN-REFORMULATION via CRT-4a); (iii) the exact-clock gate is split in the code as well as the text into CO4a (automorphism equality, u\_t ∈ ᵀ·1) and CO4b (weight-preserving, u\_t \= 1); (iv) the common invariant domain is named C\_c∞(ℝ₊) and the monomial calculation is labelled a formal coefficient identity, not machine-certified; (v) the convergence statement is corrected to a *change-count* criterion (9→4→3→0), not a residual-OPEN count; (vi) F-M46.1 is scope-limited (u∘f \= u+1 does not itself require μ \> 0); (vii) missing dependency references (Murray–von Neumann, ZS-F36, ZS-A27/A28, a Hardy/Paley–Wiener source) are restored; (viii) sections are renumbered (§16 References, §17 Version History) and the principal branch log λ\* \= −μ+iθ is stated. This is the final closure of ZS-M46. Zero fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.