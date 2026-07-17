**ZS-F30**  
**Twin-Reuleaux Reality Structure and the Steiner-Centered Support-Ratio Rapidity**

*A conditional constant-width → Lorentzian causal-cone construction: a translation-invariant rapidity from convex asymmetry, a rapidity-composition generation of SL(2,ℂ) that closes the noncompact gate, and a spinor causal-cone reconstruction — with time reversal and the present kept to a scoped discussion*

**Author:** Kenny Kang  
**Date:** June 2026  
**Paper code:** ZS-F30 v1.4 · Foundations series · Theme: Time–Space Asymmetry / Reality Structure  
**Affiliation:** Z-Spin Collaboration

**Verification (v1.4): SYMBOLIC-THEOREM 4 · GEOMETRY 5 · FULL-HOLONOMY 5 · CAUSAL-CONE 4 · DYNAMICS-DIAGNOSTIC 3 · REGRESSION 5 · SCOPE-AUDIT 5, all consistent | Zero Free Parameters | G-6 CLOSED; open gates registered (§G) | script: zs\_f30\_verify\_v1\_4.py**

Table 0\. Verification ledger, restructured around the construction. No merged PASS count; checks grouped by what they establish. (Pipe characters inside cells are written "mod" to keep the table well-formed.)

| Category | Count | Content |
| ----- | ----- | ----- |
| SYMBOLIC-THEOREM | 4 | Exact (SymPy) identities: the Lorentz algebra \[K,K\] \= −J; det X \= Minkowski form on Herm₂(ℂ); constant-width ⇔ even cosine **and** sine Fourier modes vanish; the Doubled-Simple Exchange τ-form fixed algebra \= so(3,1). |
| GEOMETRY | 5 | Support-ratio rapidity dimensionless and seam-odd; a centered circle carries no noncompact excitation; convexity and the seam projectors P± \= ½(I±J); **Steiner-centering gives translation-gauge invariance**; **ρ \= artanh β** with β=(h₁−h₂)/w, and the **exact Reuleaux** harmonics (3,9,15,…) vs the corpus leading model. |
| FULL-HOLONOMY | 5 | The **actual** generators X(θ,n) have real rank 6 \= so(3,1); det G\_L \= 1 with unitarity iff ρ=0; seam \= boost inversion B(θ+π)=B(θ)⁻¹; the pair lies in Fix(σ\_Z) (consistency); the **Rapidity-Composition Theorem** generating SL(2,ℂ). |
| CAUSAL-CONE | 4 | Null boundary ∂C₊ \= {ψψ†}; interior \= future timelike cone; SL(2,ℂ) preserves the future cone and is orthochronous; the η-free signature-(1,3) chain. |
| DYNAMICS-DIAGNOSTIC | 3 | Local/numerical diagnostics, not theorems: f₊ vs f₋ multipliers; arrow existence (mod λ ≠ 1\) vs direction (mod λ \< 1); T²=−1 Kramers value for j=½. |
| REGRESSION | 5 | Locked-input re-confirmation: A=35/437, Q=11, (Z,X,Y)=(2,3,6); the four real forms; M2/M17.5 compatibility. Prove nothing new. |
| SCOPE-AUDIT | 5 | **G-6 now CLOSED** (composition); the support-ratio↔physical-boost identification is DERIVED-CONDITIONAL (G-7); physical-T OPEN (G-2); no canonical temporal POVM (G-3); "circle SELECTS so(4)" and "Reuleaux MAXIMIZES the rapidity norm" remain OPEN (G-8); no advance on A29, no phenomenology. |

**§0. Abstract**

Why is macroscopic spacetime Lorentzian, signature (1,3), with a determinate light cone and time orientation? In the Z-Spin framework the relevant algebra is the complexified Z-Spin holonomy so(4,ℂ) ≅ sl(2,ℂ) ⊕ sl(2,ℂ) (ZS-M2), and the corpus records (ZS-M17.5) that the Z₂ seam involution Ŝ²=I selects the Lorentzian over the Euclidean form by exchanging the two su(2) factors. This paper tightens that selection into a single chain and — repairing v1.3 — supplies the noncompact (boost) direction from convex geometry in a **translation-gauge-invariant** way.

The earlier draft (v1.3) introduced a support-ratio rapidity ρ \= ½ ln(h₁/h₂) but defined it from a raw support function, which depends on the choice of origin (h\_{K+a}(θ) \= h\_K(θ) \+ a·n(θ)): an off-center circle would acquire a spurious boost. v1.4 fixes this by **centering at the Steiner point** s(K) — the canonical translation-covariant center, which in 2D is the n=1 Fourier mode of h. The Steiner-centered rapidity ρ\_K(θ) \= ½ ln( h̃\_K(θ) / h̃\_K(θ+π) ), with h̃\_K(θ) \= h\_K(θ) − s(K)·n(θ), is translation-invariant, and for a constant-width curve (no even modes) with the Steiner mode removed it depends only on the odd harmonics n ≥ 3\. Writing the dimensionless asymmetry β(θ) \= (h₁−h₂)/w \= (h₁−h₂)/(h₁+h₂), one has |β| \< 1 (subluminal) and **ρ \= artanh β** exactly — the special-relativistic rapidity–velocity relation — so the log-ratio is not arbitrary but the canonical hyperbolic coordinate of the asymmetry. Under the seam, β ↦ −β and ρ ↦ −ρ, exactly as a boost inverts.

The half-angle phase supplies the compact rotation angle φ; together X\_L \= ½(ρ+iφ)(n·σ), with the three axes n from the X-sector so(3), spans the full six-dimensional **so(3,1)** — boost generators K=σ/2 (Hermitian), rotations J=−iσ/2 (anti-Hermitian), Lorentzian bracket \[K\_i,K\_j\]=−ε\_ijk J\_k. A single Reuleaux curve supplies only a **bounded** rapidity, but we close that gate with a **Rapidity-Composition Theorem**: since the support-ratio image contains a neighborhood of 0, bounded elementary support-boosts compose (B(θ\_N)^N) to any rapidity, and with the SU(2) rotations the KAK factorization generates the whole SL(2,ℂ) identity component. Exponentiating, on Hermitian X \= x₀𝟙+x·σ, det X \= x₀²−|x|² is the Minkowski form; the positive cone C₊={X⪰0} is the future causal cone with null boundary ∂C₊={ψψ†}, preserved orthochronously by SL(2,ℂ)→SO⁺(1,3).

Seven results. **(F30.1)** the four real forms (regression). **(F30.2)** a **Doubled-Simple Exchange Theorem** in τ-form (σ²=id automatic) plus a **constant-width Fourier theorem** (cosine and sine even modes vanish). **(F30.3)** the **Steiner-centered support-ratio rapidity** (translation-invariant, ρ=artanh β) and the full six-dimensional lift with the boost-inversion identity. **(F30.4)** the spinor causal-cone reconstruction. **(F30.5)** the assembled chain — explicitly **DERIVED-CONDITIONAL**: the algebraic-representation chain is closed, but its physical identification (ρ \= the Z-Spin boost parameter) remains conditional on G-7. **(F30.6)** the two-time exclusion. **(F30.7)** the **Rapidity-Composition Theorem** closing the noncompact gate G-6.

We separate, honestly, three layers of "constant-width curve": the general theorem (any odd harmonics), the **exact Reuleaux triangle** (odd multiples of three, n=3,9,15,…, leading coefficient w/4π, rapidity range ≈ ±0.156), and the corpus **leading-harmonic model** (w/16)cos 3θ (a smooth constant-width curve, range ±0.126); the v1.3 phrase "its entire content is (w/16)cos 3θ" is corrected to apply only to the leading model. We also do not claim that a centered circle *selects* the Euclidean real form (only that it produces no noncompact excitation in this lift), nor that the Reuleaux triangle *maximizes* a rapidity norm (an extremal-geometry question we pose, not solve). Time reversal, the arrow, and the present remain scoped (§9). Zero free parameters.

**Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Exact theorem or computation (corpus or standard mathematics; here symbolically verified). |
| IMPORTED-PROVEN | Theorem from the external literature, imported unchanged. |
| DERIVED | Valid deduction from PROVEN inputs, no new assumption. |
| DERIVED-CONDITIONAL | Valid deduction conditional on a stated identification. |
| DERIVED-interpretation | Structural reading of PROVEN results; not a closed theorem. |
| HYPOTHESIS-strong | Multiple independent structural anchors; promotion path documented. |
| NUMERICAL / DIAGNOSTIC | A finite computation or local test; suggestive, not a global theorem. |
| OPEN | An explicit gate with a stated promotion path (§G). |
| NON-CLAIM (NC) | Explicitly outside scope. |

**§1. Introduction**

The Z-Spin framework fixes (Z,X,Y) \= (2,3,6), **Q** \= 11, **A** \= 35/437 (ZS-F2, ZS-F5). Granting that the relevant algebra complexifies to so(4,ℂ) ≅ sl(2,ℂ) ⊕ sl(2,ℂ) (ZS-M2, PROVEN), why is the physical real form Lorentzian, so(3,1), with a light cone and a time orientation?

**Inside the corpus**, ZS-M17.5 (DERIVED-CONDITIONAL) records that the seam involution Ŝ²=I, by exchanging the two su(2) factors, selects the Lorentzian form (gate F-M17.6 PASS); the J-conjugation h₂(θ)=h₁(θ+π) of the twin-Reuleaux pair (ZS-F7 §11.2) is its geometric implementation. This paper realizes and tightens that selection. **Outside the corpus**, the real-form classification is classical (Cartan), and the Hermitian-determinant route to the Minkowski form and the light cone is classical (Penrose–Rindler).

This version repairs the v1.3 review's four substantive points and adds two. (1) The support-ratio rapidity of v1.3 was defined from a raw support function and was therefore **origin-dependent** — a translated circle would show a fictitious boost. v1.4 centers at the **Steiner point**, making the rapidity a translation-gauge invariant (§5.2). (2) v1.3 conflated the **exact Reuleaux triangle** with the corpus's smooth (w/16)cos 3θ model; v1.4 separates three layers and labels the ±0.126 range as the leading model's, the exact Reuleaux being ±0.156 with harmonics 3,9,15,… (§5.4). (3) v1.3 left full noncompact surjectivity OPEN; v1.4 **closes it** with a Rapidity-Composition Theorem (§7, F30.7). (4) v1.3's title and conclusion over-claimed a closed physical chain; v1.4 marks the chain **DERIVED-CONDITIONAL**, with the residual physical identification isolated as G-7 (§6.5/§7.1, §G). Two further upgrades: the Doubled-Simple Exchange Theorem is recast in a clean **τ-form** for which σ²=id is automatic (§4.2), and the choice of the log-ratio is justified canonically by **ρ \= artanh β** (§5.3). Time reversal, the arrow, and the present remain scoped to §9.

**§2. Locked inputs and the seam involution as twin-Reuleaux geometry**

Dimensional skeleton, no free parameter: dim(Z)=2, dim(X)=3, dim(Y)=6, **Q**\=11, **A**\=35/437. The complexified holonomy algebra is so(4,ℂ) ≅ sl(2,ℂ)\_L ⊕ sl(2,ℂ)\_R (ZS-M2, PROVEN), the two factors commuting.

The seam involution Ŝ (ZS-F5, PROVEN, Ŝ²=I) acts on the Z-sector field space as θ → θ+π. Its geometric realization is the twin-Reuleaux pair (R₁,R₂) of constant width w (ZS-F7 §11.2), with support functions satisfying

h₂(θ) \= h₁(θ+π) \= w − h₁(θ),   R₂ \= J(R₁),   V\_XZ ∝ e^{+iθ/2},  V\_ZY ∝ e^{−iθ/2},  **V\_ZY \= (V\_XZ)∗**.

Decompose the support function into its seam-even and seam-odd parts (we use h\_sym, h\_odd to avoid any clash with the twin members h₁,h₂):

h(θ) \= h\_sym(θ) \+ h\_odd(θ),   h\_sym \= ½\[h(θ)+h(θ+π)\] \= w/2,   h\_odd \= ½\[h(θ)−h(θ+π)\],

so the twin pair is h₁ \= w/2 \+ u, h₂ \= w/2 − u with u \= h\_odd. The entire **non-circularity** lives in h\_odd. Two facts we use: (i) J carries R₁ to R₂ — it **exchanges** the members (§4); and (ii) the support asymmetry h\_odd, suitably normalized and centered, is a **rapidity** (§5). Both rest on the corpus-PROVEN constant-width identity (ZS-F7, J-conjugation to \<10⁻⁴⁰).

**§3. Theorem F30.1 — Four-real-form exhaustion (regression)**

For **g**\_ℂ \= sl(2,ℂ) ⊕ sl(2,ℂ) there are exactly four real forms of orthogonal type; their Killing signatures B(X,Y)=Tr(ad\_X ad\_Y) are:

Table 1\. The four real forms of so(4,ℂ) and their Killing signatures (Appendix A; independently recomputed). Signature \= (positive, negative).

| Defining involution σ | Real form | Structure | Killing signature |
| ----- | ----- | ----- | ----- |
| factor-preserving, compact | so(4) | su(2) ⊕ su(2) | (0, 6\) |
| factor-preserving, split | so(2,2) | su(1,1) ⊕ su(1,1) | (4, 2\) |
| factor-preserving, mixed | so∗(4) | su(2) ⊕ su(1,1) | (2, 4\) |
| factor-EXCHANGING (swap) | so(3,1) | sl(2,ℂ)\_ℝ | (3, 3\) |

The four signatures are pairwise distinct, so a real form is fixed by the **type** of its defining involution. \[F30.1: IMPORTED-PROVEN (Cartan); re-run as REGRESSION F4.\]

**§4. Theorem F30.2 — Exchange-involution fixed algebra, the Doubled-Simple Exchange Theorem (τ-form), and the constant-width Fourier theorem**

**4.1 The constant-width Fourier theorem.** Expand h(θ) \= w/2 \+ Σ\_{n≥1}(a\_n cos nθ \+ b\_n sin nθ).

**Theorem F30.2a.** The constant-width condition h(θ)+h(θ+π) \= w holds **iff** all even Fourier modes vanish, a\_{2k}=b\_{2k}=0. The seam operator (Jh)(θ):=h(θ+π) acts as **J \= −I on the odd-harmonic subspace**, the projectors are P± \= ½(I ± J), and the constant-width deformation space is the J-odd subspace P₋.

Proof. cos n(θ+π) \= (−1)ⁿ cos nθ and sin n(θ+π) \= (−1)ⁿ sin nθ; hence h(θ)+h(θ+π) \= w \+ 2Σ\_{k≥1}(a\_{2k}cos 2kθ \+ b\_{2k}sin 2kθ), equal to w identically iff every even coefficient vanishes. On the odd harmonics (−1)ⁿ=−1, so J=−I; P±=½(I±J) are complementary.  \[F30.2a: PROVEN; the cosine **and** sine identities verified symbolically, check A3; convexity h+h″ ≥ 0 holds for the leading mode, B3.\] The twin pair h± \= w/2 ± u\_odd with u\_odd ∈ P₋ is exchanged by J (u\_odd ↦ −u\_odd): **J is factor-exchanging**, forced by constant width.

**4.2 The Doubled-Simple Exchange Theorem (τ-form).** v1.3 gave a normal form σ\_α(X,Y)=(α(Ȳ),α⁻¹(X̄)) for which σ²=id is **not** automatic for arbitrary α. We use a cleaner form.

**Theorem F30.2b.** Let **g** be a complex simple Lie algebra and G \= **g** ⊕ **g**. Let τ: **g** → **g** be an antilinear Lie-algebra automorphism, and define

σ(X,0) \= (0, τX),   σ(0,Y) \= (τ⁻¹Y, 0),   i.e.   σ(X,Y) \= (τ⁻¹Y, τX).

Then **σ² \= id automatically** (for any such τ), σ is an antilinear involutive automorphism exchanging the two ideals, and Fix(σ) \= {(X, τX) : X ∈ **g**} ≅ **g**\_ℝ, the realification of **g**, the projection π₁: Fix(σ) → **g**\_ℝ being a real Lie-algebra isomorphism. For **g** \= sl(2,ℂ) with τ \= complex conjugation, Fix(σ) \= {(X, X̄)} ≅ sl(2,ℂ)\_ℝ ≅ **so(3,1)** (signature (3,3), Appendix A).

Proof. σ²(X,Y) \= σ(τ⁻¹Y, τX) \= (τ⁻¹(τX), τ(τ⁻¹Y)) \= (X,Y), so σ²=id for **any** τ; antilinearity and the automorphism property are inherited from τ. The fixed set is the graph {(X,τX)}; π₁ is a real-linear bijection onto **g** carrying the bracket to itself, hence Fix(σ) ≅ **g**\_ℝ. For sl(2,ℂ), **g**\_ℝ has real dimension 6 and Killing signature (3,3), i.e. so(3,1).  \[F30.2b: the general theorem is PROVEN analytically (standard real-form theory); the **sl(2,ℂ) instance** is verified symbolically/numerically — σ²=id for random τ-inputs and the (3,3) signature, check A4. The code verifies the instance, not arbitrary **g**.\] With Z-Spin terminology removed this reads as an independent Lie-theoretic proposition (a factor permutation of the Dynkin/Satake diagram of A₁×A₁).

**4.3 Fixed algebra and exclusion.** With the antilinear swap σ\_Z(X\_L,X\_R) \= (X̄\_R, X̄\_L) (τ \= conjugation), Theorem F30.2b gives Fix(σ\_Z) ≅ so(3,1). The three factor-**preserving** forms (so(4), so(2,2), so∗(4)) come from involutions fixing each factor; the seam, forced by constant width to **exchange** them (§4.1), **excludes all three** and yields so(3,1) — a forcing resting on two theorems. \[F30.2: DERIVED, conditional on §4.1.\]

**§5. Theorem F30.3 — The Steiner-centered support-ratio rapidity and the full six-dimensional holonomy lift**

This section closes the first arrow, **constant-width geometry → rotation \+ rapidity full holonomy**, in a translation-invariant way.

**5.1 The origin-dependence of the raw support ratio.** The support function depends on the choice of origin: translating K by a vector a sends h\_K(θ) ↦ h\_K(θ) \+ a·n(θ), with n(θ)=(cos θ, sin θ). A raw ratio ρ\_raw(θ) \= ½ ln(h(θ)/h(θ+π)) is therefore **not** translation-invariant. The clearest failure is the circle: centered at the origin it has h ≡ R and ρ\_raw ≡ 0, but shifted by a it has h\_a(θ) \= R \+ a·n(θ), giving ρ\_raw(θ) \= ½ ln\[(R+a·n)/(R−a·n)\] ≢ 0 — a **spurious boost** for a body that should carry none (verified, ρ\_raw up to 0.35 for ‖a‖=0.34). v1.3's "circle ⇒ ρ=0" was thus implicitly a gauge choice.

**5.2 Steiner centering (the fix).** The Steiner point s(K) is the canonical translation-**covariant** center, s(K+a)=s(K)+a; in 2D it is determined by the n=1 Fourier mode alone, s(K) \= (1/π)∫₀^{2π} h\_K(θ) n(θ) dθ \= (a₁, b₁). Define the **Steiner-centered support function** and **rapidity**

h̃\_K(θ) \= h\_K(θ) − s(K)·n(θ),   ρ\_K(θ) \= ½ ln( h̃\_K(θ) / h̃\_K(θ+π) ).

**Proposition F30.3a (gauge invariance).** ρ\_K is translation-gauge invariant: under K ↦ K+a, s ↦ s+a and h̃ is unchanged, so ρ\_K is unchanged. Centering removes the n=1 mode; for a constant-width curve (no even modes) the centered support function carries only odd harmonics n ≥ 3, and the centered circle has h̃ ≡ w/2, ρ ≡ 0\. \[PROVEN; checks B2, B4 — raw ρ gauge-dependent (shifted circle 0.35), Steiner-centered ρ invariant to 10⁻⁶; the leading model (w/16)cos 3θ is already Steiner-centered (its Steiner point is 0).\]

**5.3 ρ \= artanh β: why the log-ratio.** Define the dimensionless **asymmetry** β(θ) := ( h̃₁(θ) − h̃₂(θ) ) / ( h̃₁(θ) \+ h̃₂(θ) ) \= ( h₁ − h₂ ) / w. Then |β| \< 1 (the support functions are positive, so |h₁−h₂| \< h₁+h₂ \= w — β is "subluminal"), and h₁/h₂ \= (1+β)/(1−β), whence

ρ \= ½ ln(h₁/h₂) \= ½ ln\[(1+β)/(1−β)\] \= **artanh β**,

the **special-relativistic rapidity–velocity relation** ξ \= artanh(v/c). The log-ratio is therefore not arbitrary: ρ is the unique additive (rapidity) coordinate of the multiplicatively-composing asymmetry β, with β playing the role of v/c. Under the seam, β(θ+π) \= −β(θ) immediately, hence ρ(θ+π) \= −ρ(θ). \[PROVEN; check B5 — ρ \= artanh β to 10⁻⁹, |β|\<1.\] (That β is the **physical** velocity-analog of the Z-Spin holonomy remains G-7; the *mathematical* canonicity of ρ is settled here.)

**5.4 Three layers of constant-width curve.** We separate, as the structure demands:

(L1) **General constant-width:** h \= w/2 \+ u\_odd, u\_odd ∈ P₋ arbitrary. The rapidity ρ \= artanh\[(h₁−h₂)/w\] is defined for any such curve.

(L2) **Exact Reuleaux triangle:** by C₃ symmetry only harmonics that are multiples of 3 survive, and by constant width only odd ones, so u\_odd has harmonics **n \= 3, 9, 15, …**; the leading coefficient is **w/(4π) ≈ 0.0796 w** and the Steiner-centered rapidity range is ≈ **±0.156**. The exact curve has corners. \[check B5 — FFT of the exact Reuleaux support function: harmonics 3,9,15 present, c₃ \= w/4π, range ±0.156.\]

(L3) **Corpus leading-harmonic model:** u\_odd \= (w/16)cos 3θ ≈ 0.0625 w·cos 3θ — a **smooth** constant-width curve (the simplest non-circular one), with rapidity range **±0.126** \= ±½ln(9/7). This is the corpus model (ZS-F7 §6.1) and the object used in the verification.

The v1.3 statement "the Reuleaux triangle's entire content is the seam-odd (w/16)cos 3θ" is **incorrect for the exact curve** and is hereby restricted to L3. The ±0.126 range is the **leading-model** value; the exact Reuleaux is ±0.156. None of the downstream algebra depends on which layer is used.

**5.5 The full six-dimensional lift.** Combine the boost rapidity ρ(θ) with the rotation angle φ from the half-angle phase (arg V\_XZ \= θ/2):

X\_L(θ,n) \= ½ ( ρ(θ) \+ i φ ) (n·σ) \= ρ(θ)(n·K) \+ φ(n·J),  G\_L \= exp X\_L,

with **J** \= −(i/2)σ (anti-Hermitian, compact) and **K** \= (1/2)σ (Hermitian, noncompact). Over the three axes from the X-sector so(3), the six generators close into sl(2,ℂ)\_ℝ with \[J\_i,J\_j\]=ε\_ijk J\_k, \[J\_i,K\_j\]=ε\_ijk K\_k, **\[K\_i,K\_j\] \= −ε\_ijk J\_k** — the final minus sign being the Lorentzian signature (a compact so(4) would read \+). All brackets and Hermiticities are verified **symbolically** (check A1). Crucially — addressing the v1.3 review — we test the **actual** generators X(θ,n) (with ρ(θ) and φ(θ)=θ/2 both functions of one θ), not an independent basis: since ρ and φ are linearly independent functions, evaluating at two angles per axis yields **real rank 6** (a single angle gives only rank 3), so the actual holonomy image fills so(3,1) (check C1). det G\_L \= 1 always, and **G\_L is unitary iff ρ=0** (check C2).

**5.6 Seam \= boost inversion (the non-circular diagram).** About a fixed axis (boost and rotation commute, both ∝ n·σ), G\_L \= B(θ)R(φ) with B \= exp(½ρ n·σ) (Hermitian boost) and R \= exp(½iφ n·σ) (unitary rotation).

**Proposition F30.3b.** Under the geometric seam θ → θ+π the boost **inverts**, B(θ+π) \= B(θ)⁻¹ (ρ recomputed from the centered support functions); B is Hermitian and, for ρ≠0, non-unitary, while R is unitary. A Lorentz boost satisfies this inversion law; a rotation does not. The seam thus **distinguishes** the noncompact (boost, seam-odd) from the compact (rotation) direction, certifying that β is a rapidity and not a hidden rotation. \[DERIVED; check C3 — the seam image B(θ+π) and the matrix inverse B(θ)⁻¹ are computed independently and agree to 10⁻⁷.\] For completeness, the pair (X\_L, X̄\_L) lies in Fix(σ\_Z)=so(3,1) for all (θ,n) (check C4, structural/near-definitional). We do **not** assert J \= σ\_Z; they are distinct ℤ₂'s.

**5.7 A reading, and what it is not.** Proposition F30.3a gives a tempting dichotomy: a centered circle has ρ≡0 (no boost) and an asymmetric curve has ρ≢0 (boosts active). The **safe** statement is: *a centered circle produces no noncompact excitation in this lift*. The **stronger** statement — *a centered circle selects the Euclidean real form so(4)* — is **not** proven here: ρ=0 means the boost coordinate vanishes in this parameterization, i.e. the holonomy stays in the rotation subgroup, which does not by itself convert the reality involution σ\_Z into a factor-preserving one; that conversion would require a separate involution-transition theorem. Likewise, "the Reuleaux triangle is maximally Lorentzian" has no proof yet: define the **asymmetry functional** R\_∞(K) \= max\_θ |ρ\_K(θ)| (or R\_p(K) \= (∫|ρ\_K|^p)^{1/p}); R\_∞ increases with the seam-odd amplitude, but **area-minimization (Blaschke–Lebesgue) and R\_∞-maximization are different optimizations**. We therefore state only: *the Reuleaux minimizer is a natural extremal candidate for maximal noncompact activation; whether it maximizes a specified rapidity norm is OPEN* (§G, G-8). \[§5.7: DERIVED-interpretation (the safe half); the two stronger statements are OPEN.\]

**§6. Theorem F30.4 — Spinor–Minkowski reconstruction and the causal cone (η-free)**

This is the third and fourth arrows, **SL(2,ℂ) → Lorentzian causal cone**. Represent a spacetime point by X \= x₀𝟙 \+ x₁σ₁ \+ x₂σ₂ \+ x₃σ₃ ∈ Herm₂(ℂ); det X \= x₀²−x₁²−x₂²−x₃² is the Minkowski form (check A2). The eigenvalues are x₀ ± |x|, so:

**Theorem F30.4 (causal-cone reconstruction).** (a) **Future cone** C₊ := {X ⪰ 0} \= {x₀ ≥ |x|}; tr X \= 2x₀ \> 0 fixes the future orientation. (b) **Timelike interior** X ≻ 0 ⇔ future timelike (det X \> 0). (c) **Null boundary** ∂C₊ \= {X ⪰ 0, det X \= 0, X≠0} \= {rank-one positive Hermitian} \= {ψψ† : ψ ∈ ℂ²{0}}; every future null ray is a Weyl-spinor outer product. (d) **SL(2,ℂ)** acts by X ↦ gXg†; det g \= 1 ⇒ det(gXg†) \= det X (Minkowski form preserved); congruence preserves positive-semidefiniteness (C₊ and ∂C₊ preserved); tr(gXg†) \> 0 for X⪰0 (the map is **orthochronous** — time orientation preserved). This is the 2:1 cover SL(2,ℂ) → SO⁺(1,3) (Penrose–Rindler).

\[F30.4: det X \= Minkowski and SL(2,ℂ)-invariance PROVEN/IMPORTED-PROVEN; (a)–(d) IMPORTED-PROVEN (standard spinor causal structure), assembled as the corpus reconstruction; checks D1–D4.\] The chain is

swap fixed algebra so(3,1) ⟶ SL(2,ℂ) ↷ Herm₂(ℂ) ⟶ det X \= Minkowski ⟶ (signature (1,3) **and** future cone C₊ with null boundary {ψψ†}, orthochronously preserved),

every arrow a theorem, the metric **and causal** structure read from the determinant. The dynamical metric (which frame the evolution selects) is OPEN (§G, G-1).

**§7. Theorems F30.5 and F30.7 — The conditional chain and the Rapidity-Composition Theorem**

**7.1 The chain (DERIVED-CONDITIONAL).**

**Theorem F30.5.** Given a constant-width twin pair (h₁,h₂), the half-angle channel V\_XZ, and the X-sector axes: (1) the Steiner-centered seam-odd part defines the translation-invariant rapidity ρ \= artanh\[(h₁−h₂)/w\] (F30.3a, §5.3); (2) X\_L \= ½(ρ+iφ)(n·σ) spans so(3,1), boosts from the asymmetry, rotations from the phase (F30.3); (3) exponentiation gives SL(2,ℂ) preserving det X (F30.4); (4) C₊ is the future cone with null boundary {ψψ†}, orthochronous (F30.4). Hence

**constant-width geometry ⟶ rotation \+ rapidity full holonomy ⟶ SL(2,ℂ) ⟶ Lorentzian causal cone**,

η-free end to end, the boost direction carried by the (gauge-invariant) support asymmetry.

**The algebraic-representation chain is closed; its physical identification remains conditional on G-7** — that the geometric rapidity ρ is the physical boost parameter of the Z-Spin holonomy is an identification (made canonical by ρ=artanh β), not a theorem. \[F30.5: **DERIVED-CONDITIONAL** on G-7; the algebra and spinor map are PROVEN/IMPORTED-PROVEN, the assembly is DERIVED.\] An accurate external title for the result is therefore *a conditional constant-width-to-Lorentzian causal-cone construction*.

**7.2 The Rapidity-Composition Theorem (closing G-6).** A single Reuleaux curve gives a bounded rapidity (L3: |ρ| ≤ ½ln(9/7) ≈ 0.126; L2: ≈ 0.156). v1.3 left full noncompact surjectivity OPEN; it is not.

**Theorem F30.7 (Rapidity Composition).** Suppose the support-ratio image {ρ(θ) : θ} contains an open neighborhood of 0 (true for any non-circular constant-width curve, since ρ is continuous, seam-odd, and not identically zero, hence takes every value in \[−ρ\_max, ρ\_max\]). Then for any target rapidity ξ ∈ ℝ and axis n, choosing N with |ξ/N| ≤ ρ\_max and θ\_N with ρ(θ\_N) \= ξ/N (intermediate value theorem), the same-axis boosts commute and

B(θ\_N)^N \= exp( ½ N ρ(θ\_N) n·σ ) \= exp( ½ ξ n·σ ),

so finite products of elementary support-boosts realize **any** boost. Combined with the SU(2) rotations (X-sector axes), the KAK (Cartan polar) factorization g \= U₁ exp(½ξ n·σ) U₂, U₁,U₂ ∈ SU(2), shows that finite products of elementary support-boosts and rotations **generate the whole SL(2,ℂ) identity component**.

Proof. Continuity and the IVT give the elementary solve; same-axis boosts commute because both generators are ∝ n·σ, so B(θ\_N)^N \= exp(½ Nρ(θ\_N) n·σ); every g ∈ SL(2,ℂ) has a polar decomposition g \= U·P with U ∈ SU(2) and P \= √(g†g) positive-definite Hermitian of determinant 1, i.e. P \= exp(½ξ n·σ); diagonalizing P by an SU(2) rotation gives the KAK form.  \[F30.7: PROVEN; check C5 — arbitrary boosts to |ξ|≤6 reached by composition (worst 2×10⁻¹¹), and KAK reconstruction of random SL(2,ℂ) elements to 4×10⁻¹⁵. **G-6 is CLOSED.**\]

**§8. Position relative to the spacetime-signature literature**

**(F30.6)** the physically extractable statement: *a geometry that supplies a factor-exchanging involution and a nonzero (gauge-invariant) support asymmetry on sl(2,ℂ)⊕sl(2,ℂ) forces the Lorentzian real form with its future cone, and forbids the split (2,2) two-time structure* (and the Euclidean and quaternionic forms). Tegmark argues from well-posedness/observer stability that only (3,1) is predictive; Bars' two-time physics keeps a (2,2)-type structure with extra gauge symmetry — the case our exchange excludes; van Dam–Ng argue from stability/analyticity. The Z-Spin statement is **algebraic and kinematic**: it locates the signature in the involution type and the convex asymmetry carried by a constant-width curve. The classification is classical (Cartan) and the determinant causal reconstruction is classical (Penrose–Rindler); the contribution is the **geometric realization**, with the new element over v1.3 being a **translation-invariant** noncompact direction derived from convex geometry (ρ=artanh β), and the noncompact group fully generated by composition (F30.7). \[§8: DERIVED-interpretation; external references IMPORTED.\]

**§9. Discussion: time reversal, the arrow, and the present (scoped)**

**9.1 Time reversal and the reality involution.** T \= U\_T K; for spin-½, T² \= (−1)^{2j} \= −1 is the forced Kramers value (ZS-M3; ZS-Q14; ZS-A28 χ\_Z=−1). σ\_Z (selecting so(3,1)) and physical T play different roles; "the twin-Reuleaux J is physical T" is **OPEN**, pending T H\_L(θ,n)T⁻¹ \= H\_R(−θ,n) (§G, G-2). \[check E3.\]

**9.2 The arrow: existence vs direction.** i^z has fixed point z∗=0.4383+0.3606i, multiplier modulus 0.8915. **Existence** of breaking is modulus ≠ 1; **direction** (future \= contraction) is the stronger modulus \< 1; both retained. Bare conjugation maps f₊ to f₋=(−i)^z, also contracting. A full arrow theorem is here only a **diagnostic**. \[§9.2: DERIVED for the split; the global statement NUMERICAL/DIAGNOSTIC; checks E1, E2.\]

**9.3 The present is undefined, not impossible.** The count n is a clock parameter with no canonical temporal POVM; the v1.0 "no-go" was invalid (geometric measures on ℕ normalize) and remains retracted. Status **OPEN**: a covariant temporal POVM conjugate to the handshake generator (§G, G-3). \[check G4.\]

**§10. Cross-paper dependency and version-conflict check**

Table 2\. Dependency and conflict audit. "Same Ŝ" marks realization rather than rediscovery; new rows flag v1.4 additions and version-safety.

| Result | Prior status | This paper | Relation / conflict check |
| ----- | ----- | ----- | ----- |
| selection so(3,1) vs so(4) | M17.5 DERIVED-COND | geometric realization | same seam Ŝ (F7 §11.2); weak framing; F-M17.6 PASS |
| so(4,ℂ)≅sl(2,ℂ)² | M2 PROVEN | used | cited; factors commute (check F5) |
| four-form exhaustion | F30.1 (v1.2) | regression | unchanged (check F4) |
| Doubled-Simple Exchange | v1.3 (α-form) | repaired to τ-form | σ²=id now automatic; same conclusion |
| constant-width Fourier | F7 §6.1 (example) | PROVEN (general) | cosine **and** sine; no conflict |
| support-ratio rapidity | v1.3 (raw, gauge-dep) | Steiner-centered, ρ=artanh β | **repairs origin-dependence**; gauge-invariant |
| exact Reuleaux vs model | v1.3 (conflated) | three layers separated | ±0.126 is L3 model; exact L2 is ±0.156; corrects overclaim |
| holonomy lift | v1.3 | actual-generator rank-6 | tests the real image, not a basis |
| noncompact surjectivity | v1.3 OPEN (G-6) | **CLOSED** (F30.7) | composition \+ KAK |
| det Herm₂(ℂ)=Minkowski \+ cone | v1.3 | unchanged | causal cone retained |
| z∗, modulus 0.8915 | M1 PROVEN | diagnostic | no drift (check E1) |

The i-tetration constant z∗ (ZS-M1) is unmodified; **A** \= 35/437, **Q** \= 11, dim(Z) \= 2 are LOCKED and re-confirmed (F1–F3). Framing is the weaker, accurate one; **no upstream value is modified** — the version-conflict check is clean.

**§11. Falsification gates**

Table 3\. Genuine theorem-falsifiers separated from diagnostics.

| Gate | Kind | Trigger |
| ----- | ----- | ----- |
| F-F30.1 | GENUINE | If any of the four Killing signatures differs from (0,6),(4,2),(2,4),(3,3). |
| F-F30.2 | GENUINE | If Fix(σ\_Z) ≠ (3,3), or if constant width did NOT force all even Fourier modes (cosine and sine) to vanish. |
| F-F30.3a | GENUINE | If the **Steiner-centered** rapidity were not translation-invariant, or if ρ ≠ artanh β, or if it were not seam-odd. |
| F-F30.3b | GENUINE | If {J\_i,K\_i} did not satisfy \[K\_i,K\_j\] \= −ε\_ijk J\_k, or if the actual generators did not reach real rank 6\. |
| F-F30.3c | GENUINE | If the seam did not invert the boost, B(θ+π) ≠ B(θ)⁻¹. |
| F-F30.4 | GENUINE | If det X ≠ Minkowski, if SL(2,ℂ) did not preserve it, if the null boundary were not {ψψ†}, or if the action were not orthochronous. |
| F-F30.7 | GENUINE | If bounded elementary support-boosts plus SU(2) rotations did **not** generate SL(2,ℂ) — G-6 would reopen. |
| F-F30.6 | STRUCTURAL-PRED | Observation of stable two-time (2,2) dynamics would contradict the exclusion (§4, §8). |
| F-F30.8 | ANTI-OVERCLAIM | If any step is read as identifying the geometric ρ with the physical boost parameter (G-7), as proving a centered circle *selects* so(4) or the Reuleaux triangle *maximizes* a rapidity norm (G-8), as deriving the dynamical metric (G-1), as identifying σ\_Z with physical T (G-2), or as a temporal-Born no-go, it is falsified by this paper's scope (§5–§7, §9, §G). |

**§G. Open Gates Registry**

| Gate | Statement | Promotion path |
| ----- | ----- | ----- |
| G-1 dynamical metric | Which point/tetrad in Herm₂(ℂ) the cosmological dynamics selects is open; §6 gives the form and cone, not the frame. | Derive the frame from the Z-sector EOM; prove the flow preserves Fix(σ\_Z). |
| G-2 physical T | σ\_Z is a reality involution; its identity with physical T is unproven. | Prove T H\_L(θ,n) T⁻¹ \= H\_R(−θ,n). |
| G-3 temporal POVM | No canonical covariant temporal POVM is assigned to the count n. | Construct a clock observable conjugate to the handshake generator. |
| G-4 holonomy premises | The lift is conditional on the so(3) axes \= SU(2) axes (F18/S15). | Derive the axis identification from F18 first principles. |
| G-5 A29 G1–G3 | Projector selection, flux collectivization, rank-to-energy map (not addressed). | ZS-A30; A29 §8.3. |
| G-6 noncompact surjectivity | **CLOSED by F30.7** (Rapidity Composition): bounded support-boosts \+ SU(2) rotations generate SL(2,ℂ). | — (closed). |
| G-7 physical rapidity | ρ \= artanh β is the canonical *mathematical* rapidity of the convex asymmetry; its identity with the *physical* boost parameter of the Z-Spin holonomy is an identification. | Derive ρ as the holonomy of the Z-sector connection along the asymmetry direction, or match it to the F14 joint-ODE boost. |
| G-8 extremality | Whether the centered circle *selects* the Euclidean form (vs merely carrying no noncompact excitation), and whether the Reuleaux triangle *maximizes* R\_∞(K) \= max\_θ mod-ρ\_K(θ) (vs minimizing area), are open. | An involution-transition theorem (circle → so(4)); a convex-optimization proof that the Blaschke–Lebesgue minimizer extremizes R\_∞. |

**§12. Conclusion**

F30 now stands as seven linked results with the chain made honest. The four real forms are exhausted (F30.1); a τ-form Doubled-Simple Exchange Theorem and a constant-width Fourier theorem make the swap-to-Lorentzian forcing general (F30.2). The boost direction is supplied by the **Steiner-centered** support-ratio rapidity ρ \= artanh\[(h₁−h₂)/w\] — a **translation-gauge invariant** with the special-relativistic rapidity form, repairing v1.3's origin-dependent definition (F30.3). The actual holonomy generators (not a chosen basis) reach the full six-dimensional so(3,1), the seam acting as boost inversion (F30.3). Exponentiating to SL(2,ℂ) reconstructs the full causal structure — future cone, time orientation, null \= {ψψ†} — orthochronously (F30.4). A **Rapidity-Composition Theorem** shows bounded elementary support-boosts and SU(2) rotations generate the whole SL(2,ℂ) identity component, **closing the noncompact gate G-6** (F30.7).

The honest status is **a zero-parameter, η-free, DERIVED-CONDITIONAL construction of the Lorentzian causal structure from translation-invariant constant-width asymmetry, with the noncompact group fully generated**. The algebraic-representation chain is closed; the single physical identification (ρ \= the Z-Spin boost parameter) is canonical but conditional (G-7), and two interpretive over-readings are held OPEN rather than claimed: a centered circle producing no excitation is not yet the *selection* of so(4), and the area-minimizing Reuleaux triangle is not yet shown to *maximize* the rapidity norm (G-8). The mathematics is self-contained enough to read outside the corpus — its two externally interesting cores are the Doubled-Simple Exchange Theorem and the convex-asymmetry-to-rapidity map ρ=artanh β with its composition theorem. The next priorities are the dynamical metric (G-1) and A30 (A29 §8.3), not a further F30 revision.

**Acknowledgements & Code Availability**

Revised in response to a technical review of v1.3. Repairs and additions: the **Steiner-centered** support-ratio rapidity, removing the origin-dependence of the raw ratio (§5.1–5.2); the **ρ \= artanh β** canonicalization (§5.3); the explicit **three-layer** separation of general constant-width / exact Reuleaux (harmonics 3,9,15, leading w/4π, range ±0.156) / corpus leading model (w/16, range ±0.126) (§5.4), correcting the v1.3 "entire content is (w/16)cos 3θ"; the **Rapidity-Composition Theorem** closing G-6 (§7.2, F30.7); the τ-form **Doubled-Simple Exchange Theorem** with σ²=id automatic (§4.2); the **actual-generator** rank-6 test (§5.5); the reduction of overclaim — F30.5 marked DERIVED-CONDITIONAL with the chain's physical step isolated as G-7, and the circle/Reuleaux dichotomy demoted to a safe half plus OPEN G-8 (§5.7). The verification script zs\_f30\_verify\_v1\_4.py adds the Steiner translation-invariance test, the ρ=artanh β and exact-Reuleaux-harmonic checks, the sine half of the Fourier identity, the actual-generator rank test, and the composition/KAK checks; it contains no fail-open clause and exits 0 iff every check is consistent.

**Appendix A. The four real forms and their Killing signatures**

With **g**\_ℂ \= sl(2,ℂ)⊕sl(2,ℂ): (i) so(4) \= su(2)⊕su(2): (0,6). (ii) so(2,2) \= su(1,1)⊕su(1,1): (4,2). (iii) so∗(4) \= su(2)⊕su(1,1): (2,4). (iv) so(3,1) \= sl(2,ℂ)\_ℝ \= Fix(σ\_Z), σ\_Z(X\_L,X\_R)=(X̄\_R,X̄\_L) (the τ=conjugation instance of F30.2b), Killing eigenvalues {−4,−4,−4,+4,+4,+4}: (3,3). The swap (iv) is the unique factor-exchanging case and is, by Theorem F30.2b, the realification sl(2,ℂ)\_ℝ. \[IMPORTED-PROVEN; numerics in Appendix C.\]

**Appendix B. The Steiner-centered rapidity, the composition theorem, and the holonomy — derivation**

**B.1 Steiner centering.** The Steiner point s(K) \= (1/π)∫₀^{2π} h\_K(θ) n(θ) dθ picks out the n=1 mode: with h \= w/2 \+ Σ(a\_n cos nθ \+ b\_n sin nθ), s \= (a₁, b₁), since ∫cos²θ dθ \= π and all other modes integrate to zero against (cos θ, sin θ). It is translation-covariant: h\_{K+a} \= h\_K \+ a·n adds a to the n=1 mode, so s(K+a)=s(K)+a, and h̃ \= h − s·n is translation-invariant. For a constant-width curve all even modes vanish (F30.2a); removing the n=1 mode by centering leaves only odd n ≥ 3, and ρ\_K \= ½ ln(h̃₁/h̃₂) is a translation-gauge invariant. The leading model h \= w/2 \+ (w/16)cos 3θ has a₁=b₁=0, so its Steiner point is the origin and it is already centered.

**B.2 ρ \= artanh β.** Put β \= (h₁−h₂)/(h₁+h₂) \= (h₁−h₂)/w. Positivity of h₁,h₂ gives |h₁−h₂| \< h₁+h₂, so |β| \< 1\. Then 1+β \= 2h₁/w, 1−β \= 2h₂/w, so h₁/h₂ \= (1+β)/(1−β) and ρ \= ½ ln(h₁/h₂) \= ½ ln\[(1+β)/(1−β)\] \= artanh β. Since the seam exchanges h₁ ↔ h₂, β(θ+π) \= −β(θ) and ρ(θ+π) \= −ρ(θ). For the leading model β \= (cos 3θ)/8, max|β| \= 1/8, and ρ\_max \= artanh(1/8) \= ½ ln(9/7) ≈ 0.1257.

**B.3 Lorentz brackets.** With **J**\=−(i/2)σ, **K**\=(1/2)σ and \[σ\_i,σ\_j\]=2iε\_ijk σ\_k: \[J\_i,J\_j\]=ε\_ijk J\_k, \[J\_i,K\_j\]=ε\_ijk K\_k, \[K\_i,K\_j\]=−ε\_ijk J\_k; **K** Hermitian, **J** anti-Hermitian (check A1). G\_L \= exp\[½(ρ+iφ)n·σ\] \= B·R with B=exp(½ρ n·σ) Hermitian, R=exp(½iφ n·σ) unitary; det G\_L=1; unitary iff ρ=0. Seam: ρ→−ρ ⇒ B(θ+π)=B(θ)⁻¹.

**B.4 Composition (F30.7).** ρ(θ) is continuous, seam-odd, not identically zero, so its image is \[−ρ\_max, ρ\_max\] ∋ 0 (an open neighborhood of 0). For ξ ∈ ℝ pick N ≥ ⌈|ξ|/ρ\_max⌉ and θ\_N with ρ(θ\_N)=ξ/N (IVT). Same-axis boosts commute, so B(θ\_N)^N \= exp(½ξ n·σ). Every g ∈ SL(2,ℂ) \= U·P (polar), P=exp(½ξ n·σ), U ∈ SU(2); KAK then gives g \= U₁ exp(½ξ n·σ) U₂. So elementary support-boosts and rotations generate SL(2,ℂ) (check C5: composition to 2×10⁻¹¹, KAK to 4×10⁻¹⁵).

**B.5 Causal cone.** X \= x₀𝟙 \+ x·σ: det X \= x₀²−|x|²; eigenvalues x₀±|x|; X⪰0 ⇔ x₀≥|x|. A rank-one positive Hermitian matrix equals ψψ† with det(ψψ†)=|ψ₁|²|ψ₂|²−|ψ₁ψ̄₂|²=0 and tr(ψψ†)=|ψ|²\>0: the future null cone is the spinor outer products (check D1). For g ∈ SL(2,ℂ), gψψ†g† \= (gψ)(gψ)† is again a future null outer product (cone preserved, orthochronous: check D3); on the interior gXg† stays positive definite (check D2).

**Appendix C. Numerical verification**

SYMBOLIC-THEOREM. (A1) \[J,J\]=J, \[J,K\]=K, \[K,K\]=−J exact; **K** Hermitian, **J** anti-Hermitian. (A2) det X \= x₀²−x₁²−x₂²−x₃² symbolically. (A3) cos n(θ+π) and sin n(θ+π) both \= ±(odd/even) ⇒ constant width ⇔ even cosine and sine modes vanish, J \= −I on odd. (A4) Doubled-Simple τ-form σ²=id for random τ-inputs; Fix Killing (3,3) \= so(3,1). GEOMETRY. (B1) ρ W-independent to 3×10⁻¹⁶, seam-odd to 6×10⁻¹⁶. (B2) centered circle ρ=0; asymmetric curve ρ≠0. (B3) h+h″ ≥ 0; J \= −I (odd). (B4) raw ρ gauge-dependent (shifted circle 0.35); Steiner-centered ρ invariant (circle 2×10⁻¹⁶, model 3×10⁻¹⁶). (B5) ρ \= artanh β to 10⁻⁹, |β|\<1; exact Reuleaux a₃ \= w/4π ≈ 0.0796, harmonics 3,9,15, range ±0.156. FULL-HOLONOMY. (C1) actual-generator real rank 6 (single angle 3). (C2) det G\_L=1; unitary iff ρ=0. (C3) B(θ+π)=B(θ)⁻¹ to 10⁻⁷; B Hermitian. (C4) (X\_L, X̄\_L) ∈ Fix(σ\_Z). (C5) composition to 2×10⁻¹¹; KAK to 4×10⁻¹⁵ — G-6 closed. CAUSAL-CONE. (D1) ψψ† Hermitian, det=0, trace\>0, PSD over 6000 spinors. (D2) interior future timelike over 6000 points. (D3) SL(2,ℂ) orthochronous over 3000 elements. (D4) chain → signature (1,3). DYNAMICS-DIAGNOSTIC. (E1) z∗ \= 0.43828+0.36059i, modulus 0.89151; K f₊ K⁻¹ \= f₋. (E2) modulus ≠ 1 and \< 1\. (E3) T² \= −1 for j=½. REGRESSION. (F1) A=35/437; (F2) Q=11; (F3) (Z,X,Y)=(2,3,6); (F4) four signatures distinct; (F5) factors commute. SCOPE-AUDIT. (G1) G-6 closed; (G2) G-7 identification; (G3) physical-T OPEN; (G4) temporal POVM OPEN; (G5) circle-selection and Reuleaux-extremality OPEN, A29 untouched. All categories consistent.

**References**

**Z-Spin corpus**

\[ZS-F2\] K. Kang, "Geometric Impedance A \= 35/437," ZS-F2 v1.0 (2026).  
\[ZS-F4\] K. Kang, "The Z₂ Seam and SU(2) Double Cover," ZS-F4 v1.0 (2026).  
\[ZS-F5\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11, and the Seam Involution Ŝ," ZS-F5 v1.0 (2026).  
\[ZS-F7\] K. Kang, "Twin-Reuleaux Holonomy, the J-Involution, and Constant-Width Pair Kinematics (§6, §11)," ZS-F7 v1.0(Revised) (2026).  
\[ZS-F11\] K. Kang, "The Operational Observer Coordinate," ZS-F11 v1.0 (2026).  
\[ZS-F14\] K. Kang, "Z-Anchored Vortex and the Twin-Reuleaux Joint ODE," ZS-F14 v1.0 (2026).  
\[ZS-F18\] K. Kang, "The Three-Bridge Meta-Map and Three-Dimensional Self-Organization," ZS-F18 v2.1 (2026).  
\[ZS-M1\] K. Kang, "i-Tetration and the Fixed Point," ZS-M1 v1.0 (2026).  
\[ZS-M2\] K. Kang, "Complexified Lorentz Algebra, the Chiral sl(2) Split, and so(4) ≅ sl(2)\_L × sl(2)\_R," ZS-M2 v1.0 (2026).  
\[ZS-M3\] K. Kang, "Quantum Tetrahedron, j \= 1/2 Uniqueness, and 4π Closure," ZS-M3 v1.0 (2026).  
\[ZS-M17\] K. Kang, "Z₂ Seam Involution and Real-Form Selection (§17.5)," ZS-M17 v1.0 (2026).  
\[ZS-Q1\] K. Kang, "Geometric Decoherence and the Born Rule," ZS-Q1 v1.0 (2026).  
\[ZS-Q14\] K. Kang, "Kramers Structure and χ\_Z \= −1," ZS-Q14 v1.0 (2026).  
\[ZS-S15\] K. Kang, "The Poynting–Commutator Theorem and Twin-Reuleaux Realization," ZS-S15 v1.0 (2026).  
\[ZS-A28\] K. Kang, "JZ-Odd Doublet, Kramers Structure, and the Susceptibility Kernel," ZS-A28 v1.9 (2026).  
\[ZS-A29\] K. Kang, "Rank-Weighted Vacuum Budget and the Coincidence Problem," ZS-A29 v1.6 (2026).

**External**

\[1\] É. Cartan, "Les groupes réels simples finis et continus," Ann. Sci. Éc. Norm. Supér. 31, 263 (1914); A. W. Knapp, *Lie Groups Beyond an Introduction*, 2nd ed. (Birkhäuser, 2002), Ch. VI (real forms of so(4,ℂ): so(4), so(3,1), so(2,2), so∗(4)).  
\[2\] R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge Univ. Press, 1984), §1.2–§1.4 (Hermitian X, det X \= Minkowski norm, future null cone {ψψ†}, SL(2,ℂ) → SO⁺(1,3) orthochronous).  
\[3\] T. Bonnesen and W. Fenchel, *Theory of Convex Bodies* (BCS Associates, 1987); H. Groemer, *Geometric Applications of Fourier Series and Spherical Harmonics* (Cambridge Univ. Press, 1996), Ch. 4 (support functions, the Steiner point as the first Fourier coefficient, constant width as the vanishing of even harmonics).  
\[4\] M. Tegmark, "On the dimensionality of spacetime," Class. Quantum Grav. 14, L69 (1997).  
\[5\] I. Bars, "Survey of two-time physics," Class. Quantum Grav. 18, 3113 (2001).  
\[6\] H. van Dam and Y. J. Ng, "Why 3+1 metric rather than 4+0 or 2+2?," Phys. Lett. B 520, 159 (2001).  
\[7\] H. A. Kramers, Proc. Amsterdam Acad. 33, 959 (1930) (T² \= (−1)^{2j}).  
\[8\] A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory* (North-Holland, 1982\) (covariant time observables).

**Version History**

v1.0 (June 2026): Initial release; claimed signature closure and a temporal-Born no-go; single 24/24 PASS ledger.  
v1.1 (June 2026): Retracted 'closes the only axis'; cited M2/M17.5; added a three-real-form forcing-and-exclusion with so(2,2); formalized T=U\_T K, T²=−1; retracted the temporal-Born no-go to OPEN; reclassified the ledger; added the Open Gates Registry.  
v1.2 (June 2026): Mathematical-core revision. Completed the classification to four real forms (so∗(4), (2,4)); promoted the swap to a constant-width lemma; added a matrix holonomy lift (compact SU(2), boost by 'multiply by i'); replaced the circular tetrad with the η-free det X \= Minkowski reconstruction; positioned against Tegmark/Bars/van Dam–Ng; separated σ\_Z from physical T; restructured the verification.  
v1.3 (June 2026): Chain-closure revision. Introduced the support-ratio rapidity ρ=½ln(h₁/h₂); lifted the holonomy to the full six-dimensional so(3,1) with \[K,K\]=−J and the boost-inversion identity; added the Doubled-Simple Exchange and constant-width Fourier theorems; extended det X \= Minkowski to a causal-cone reconstruction; assembled the chain; registered gates G-6, G-7.  
v1.4 (June 2026): Gauge-invariance and honesty revision. (1) Made the support-ratio rapidity **translation-gauge invariant** by **Steiner centering** ρ\_K \= ½ ln(h̃₁/h̃₂), h̃ \= h − s(K)·n, repairing the v1.3 origin-dependence (a translated circle no longer shows a spurious boost) (§5.1–5.2, F30.3a). (2) Justified the log-ratio canonically: **ρ \= artanh β** with β=(h₁−h₂)/w, |β|\<1 — the special-relativistic rapidity–velocity relation (§5.3). (3) Separated **three layers** — general constant-width / exact Reuleaux (harmonics 3,9,15, leading w/4π, range ±0.156) / corpus leading model (w/16, range ±0.126) — correcting the v1.3 "entire content is (w/16)cos 3θ" (§5.4). (4) Added the **Rapidity-Composition Theorem** (F30.7), generating the whole SL(2,ℂ) identity component from bounded elementary support-boosts plus SU(2) rotations and **closing G-6** (§7.2). (5) Recast the **Doubled-Simple Exchange Theorem in τ-form**, σ²=id automatic (§4.2, F30.2b). (6) Tested the **actual** holonomy generators (rank 6 from two angles, rank 3 from one) rather than an independent basis (§5.5, C1). (7) Reduced overclaim: F30.5 marked **DERIVED-CONDITIONAL** with the chain's physical step isolated as G-7, the title softened to "a conditional … construction," and the circle/Reuleaux dichotomy demoted to a safe half plus OPEN G-8 (§5.7). (8) Restructured the verification into the same seven categories and renamed it zs\_f30\_verify\_v1\_4.py. Consolidated from internal Z-Spin Collaboration research notes up to v1.4.0.  
