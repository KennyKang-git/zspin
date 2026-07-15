**ZS-F34**

# **The Six-Dimensional Charge Unit of the Z-Spin Three-Form**

### 

### *The Icosahedral Bivector Selection of the Baryon Module and the Finite-Symmetry Susceptibility-Rank Theorem, with the Single-Mode Reduction of the Dark-Energy Susceptibility in the Exact-A₅ Branch*

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Date:** June 2026 (v1.8, **terminal**: final-clean typesetting \+ N\_eff precision \+ signature/multiplicity-line caveats)  
**Paper code:** ZS-F34 · v1.8 · Theme: Foundations / UV Charge-Unit Reduction / Companion to ZS-F33

**Verification:** 23/23 (zs\_f34\_verify\_v1\_1.py) \+ 32/32 gate-decomposition-v5 (zs\_f34\_verify\_v1\_8.py) PASS (arithmetic, counterexample, and model-instantiation checks — **not** a closure certificate). **This is the terminal version of ZS-F34.** Two general theorems are placed at the front, lifting the result from a conditional internal coefficient to a statement of independent interest. (A) **Icosahedral Bivector Selection (F34.BIV):** the exterior square of the standard four-dimensional A₅-module is Λ²(**4**) \= **3** ⊕ **3′** (a textbook character identity, GC27); it is the six-dimensional *irreducible* of S₅ (GC28); the two triplets are the Hodge **self-dual** and **anti-self-dual** sectors, and an orientation-reversing odd permutation in S₅ commutes/anticommutes with the Hodge star so as to *swap* them (GC29). This **geometrizes** the outer automorphism σ of v1.6: 3 ↔ 3′ *is* self-dual ↔ anti-self-dual under orientation reversal. Conditional on identifying the corpus rank-6 Y/baryon carrier with Λ²(V₄), the module **3 ⊕ 3′** is selected — the mathematics is DERIVED-CONDITIONAL, while the physical identity of the orientation-reversing symmetry remains OPEN. (B) **Finite-Symmetry Susceptibility-Rank Theorem (F34.SR):** for a finite group G acting unitarily on a flux space V, a G-equivariant kinetic operator Z \> 0, and a source c ∈ V^G, the susceptibility is χ \= (1/4π²) c†(Z|\_{V^G})⁻¹ c, so the *effective mode count is dim V^G, not the full flux rank* (GC30). The single-mode dark-energy result (dim V^G \= 1\) and the m×m block case are its corollaries; the "factor 83" was never the right multiplicity for an invariant source. **A residual v1.6 error is fixed:** the single-mode susceptibility is χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) with ν\_s² \= v\_sᵀv\_s (lattice norm) and G\_s \= sᵀG s (Hessian norm), since v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s already — v1.6 divided by G\_s twice (GC23/GC32). The 83-dimensional flux/source realization reduces to **five one-dimensional objects** {P\_s, G\_s, ν\_s, (U\_s, V\_s) \= 1, Q\_s}; the independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates remain, and the actual P\_b, I\_s, e₆ are deferred to ZS-F35/ZS-F36. **v1.8 (this version)** is an eighth-review final-clean pass: it simplifies math spacing, sharpens F34.SR to N\_eff \= dim S\_src ≤ dim V^G (equality when admissible sources span V^G), adds the Euclidean-vs-Lorentzian **signature caveat** to F34.BIV (its ⋆² \= \+1 real split is identified with the Lorentzian Λ²(ℝ^{1,3}) only via complexification/an explicit intertwiner, part of the carrier bridge), and records that F34.BIV selects the *representation type* 3 ⊕ 3′ while the actual baryon projector P\_b retains a residual ℂP³ **multiplicity-line freedom** (→ ZS-F35). No new theorems or closures are added. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

---

# §0. Abstract

This is the companion paper promised by ZS-F33 §9.5, revised after external review. ZS-F33 reduced the absolute cosmological vacuum scale to a single dimensionful susceptibility through ρ\_Λ,Z \= ½ **χ₋** ω², and registered the *Charge-Unit Obstruction*: flux integrality fixes the flux number but not the dimensionful unit χ₋ \= e₋²/(4π²Z₋). F33.8D recorded a route to χ₋ under a rank-2 internal-cycle ansatz Y₆ \= M₄ × Σ₂ and deferred its establishment to this paper.

**What is established.** The uplift is **internal-fibre, not Kaluza–Klein**: the "6" is the representation dimension dim Λ²(ℝ^{1,3}) \= 6, and a 6D *spacetime* metric is **not licensed** (ZS-A17; asserting one triggers the F33-G8D retraction). A **degree-counting argument** (§2) shows the 4D odd three-form A₃⁻ (field strength F₄⁻, a 4-form) descends from a parent five-form C₅ (six-form strength G₆ \= dC₅) by wrapping the **unique** 2-cycle (b₂ \= 1); a 6-form needs a carrier of dimension **≥ 6**, and M₄ × Σ₂ (dim 4 \+ dim **Z** \= 6 \= **Y**) *saturates* this, so it is the **minimal** carrier — the product of the *existing* 4D base and the *existing* Z-sector Koenigs torus Σ₂ \= E\_λ\*, a six-dimensional pseudo-Riemannian **total space** (four noncompact spacetime dimensions \+ a compact 2D internal fibre), **not** six observable spacetime dimensions. A **parent-action wrapped-brane reduction** of C₅ \= A₃⁻ ∧ ω₂ gives the 4D kinetic matrix Z\_{ij} \= (1/g₆²)∫\_Σ₂ ω₂^i ∧ ⋆₂ω₂^j and the susceptibility in its **general quadratic form** in the theta-coupling vector **c**\_θ

$$\\chi\_- \= \\frac{1}{4\\pi^2} \\mathbf{c}*\\theta^{\\mathsf T} Z^{-1}\\mathbf{c}*\\theta.$$

**What v1.7 adds (terminal version).** v1.6 corrected an A₅ trichotomy and proposed an outer-automorphism selection; a seventh review found one real formula error (fixed below) and recommended terminating F34. A deep exploration then showed that the result's value is raised most not by closing another gate but by stating two general theorems. v1.7 does both.

- **Icosahedral Bivector Selection (F34.BIV, new — geometrizes v1.6's σ).** The standard four-dimensional A₅-module V₄ (the sum-zero subspace of the S₅ permutation representation) has exterior square Λ²(V₄) \= **3 ⊕ 3′** — an elementary character computation (χ\_{Λ²4} \= (6,−2,0,1,1) \= χ\_3 \+ χ\_3′, GC27). Over S₅ this is the six-dimensional *irreducible* (GC28), so the two A₅-triplets cannot be S₅-separated: an odd permutation mixes them. Geometrically, in an oriented 4-dimensional metric space Λ²(V₄) \= Λ²₊ ⊕ Λ²₋ (self-dual ⊕ anti-self-dual, each 3-dimensional); A₅ ⊂ SO(V₄) commutes with the Hodge star and preserves each, while an orientation-reversing odd permutation anticommutes with it and **swaps Λ²₊ ↔ Λ²₋** (GC29). This is exactly v1.6's outer automorphism, now *realized* rather than posited: **3 ↔ 3′ is self-dual ↔ anti-self-dual under orientation reversal**. The same 3 ⊕ 3′ is the known decomposition of the six-dimensional crystallographic icosahedral representation (T₁ ⊕ T₂, IMPORTED-PROVEN), an independent cross-check. Conditional on identifying the corpus rank-6 Y/baryon carrier with Λ²(V₄), the module **3 ⊕ 3′** is selected with no extra representation choice. The mathematics is DERIVED-CONDITIONAL; the physical identity of the orientation-reversing symmetry stays OPEN (split from v1.6's single HYPOTHESIS-strong tag into F34.OUT-Math and G-Outer-Physical).  
- **Finite-Symmetry Susceptibility-Rank Theorem (F34.SR, new — the external-value statement).** Let a finite group G act unitarily on a flux space V, let Z \> 0 be G-equivariant, and let the source c ∈ V^G. Then Z⁻¹ is G-equivariant, it preserves V \= V^G ⊕ (V^G)^⊥, and since c ∈ V^G,

$$\\chi \= \\frac{1}{4\\pi^2}\\mathbf c^{\\dagger}\\big(Z|*{V^G}\\big)^{-1}\\mathbf c,\\qquad N*{\\rm eff} \= \\dim V^G\\ \\ (\\neq \\dim V).$$

The *effective mode count is the invariant-source rank, not the full flux rank* (GC30). Three corollaries: dim V^G \= 0 ⟹ c \= 0; dim V^G \= 1 ⟹ exact single mode; dim V^G \= m \> 1 ⟹ an m×m invariant-block susceptibility. This is a statement about any finite-symmetry multi-four-form theory (Bousso–Polchinski-type included): the naive "N fluxes ⟹ susceptibility ∝ N" is generally false. In F34 the baryon/CDM-equivariant single-singlet branch has dim H\_Λ^{A₅} \= 1, so N\_eff \= 1 and full 83-dimensional centrality is *not needed* — the old question "why are 83 kinetic eigenvalues equal?" is replaced by "what is the one-dimensional invariant-source response?".

**One real error fixed.** v1.6 wrote χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) **and** defined ν\_s² \= v\_sᵀG⁻¹v\_s, which double-divides by G\_s (v\_sᵀG⁻¹v\_s already equals ν\_s²/G\_s). v1.7 separates the **lattice norm** ν\_s² \= v\_sᵀv\_s \= ⟨v\_s, v\_s⟩₀ from the **Hessian norm** G\_s \= sᵀG s (s the unit singlet), so that q\_s := v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s and

$$\\chi\_-^{(s)} \= \\frac{Z\_{\\rm match}g\_{\\rm reg}^2}{4\\pi^2V\_\\Sigma}e\_6^2\\frac{\\nu\_s^2}{G\_s} \= \\frac{g\_{\\rm reg}^2e\_6^2}{4\\pi^2V\_\\Sigma}I\_s,\\qquad I\_s := Z\_{\\rm match}v\_s^{\\mathsf T} G^{-1} v\_s,$$

introducing the **Singlet Response Invariant** I\_s, one basis-independent number bundling Z\_match, the singlet Hessian, and the primitive-source normalization (GC23, GC32, robust over many A₅-invariant metrics).

**Net.** The robust object is the master quadratic form χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² ĉ\_θᵀG⁻¹ĉ\_θ; F34.SR fixes its effective rank at dim V^G, F34.BIV selects the rank-6 carrier, and the exact-A₅ branch reduces to I\_s plus the independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates. The number 0.091847 · e₆² (ρ\_Λ,Z \= 0.234402 · e₆²) is the path-(c) aligned-central value only; single-mode is **one of three branches**, not generic. **The actual P\_b, I\_s, and e₆ are deferred to ZS-F35; F34 terminates here.** The contribution is a *reduction*, not a closure. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

---

# Epistemic Status Legend

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN / IMPORTED-PROVEN | Complete proof, here or in cited peer-reviewed work. |
| DERIVED | Follows from Z-Spin structure \+ standard mathematics; no fitted parameter. |
| DERIVED-CONDITIONAL | Derived conditional on a stated, not-yet-closed hypothesis. |
| HYPOTHESIS-strong | Multiple independent structural anchors and a documented promotion path, but a load-bearing identification still OPEN. |
| COMPUTED-UNDER-NORMALIZATION | A definite number, but only after an undetermined normalization is fixed by hand. |
| BENCHMARK-COROLLARY | A value that holds under an explicit, declared set of normalizations. |
| NO-GO / CLOSED-NEGATIVE | A registered impossibility, or a route resolved in the negative (scope stated). |
| METRIC-IDENTIFICATION-CONDITION | A definite value, conditional on identifying the physical metric with a canonical candidate. |
| MINIMALITY-CONDITIONAL | A structure derived as the minimal one of its kind, unique only under a no-extra-structure principle. |
| REDUCED | A gate shown to reduce to an upstream gate, inheriting that gate's (still-open) status rather than closing independently. |
| OPEN-GATE / SUB-GATE | A named, load-bearing gap the paper deliberately does **not** close (a sub-gate is one component of a decomposed gate). |
| RETRACTED | A claim withdrawn in a later version, with the reason recorded. |
| LOCKED | Core constant fixed upstream; immutable downstream. |

---

# Claim Ledger (17 entries: 6 results incl. two new general theorems, the A₅-path theorems, the F34.OUT split into Math \+ Physical, the metric/flux theorems one retracted, and the torsion-No-Go retraction)

| Tag | Result | Status |
| ----- | ----- | ----- |
| **F34.BIV** | **Icosahedral Bivector Selection:** Λ²(V₄) \= **3 ⊕ 3′** for the standard 4-dim A₅-module V₄ (character, GC27); it is the 6-dim irreducible of S₅ (GC28); the triplets are Hodge self-dual/anti-self-dual, swapped by an orientation-reversing odd permutation (GC29). Conditional on identifying the corpus rank-6 Y/baryon carrier with Λ²(V₄), the *representation type* 3 ⊕ 3′ is selected (the actual projector P\_b keeps a residual ℂP³ multiplicity-line freedom → F35); Euclidean ⋆²=+1 vs Lorentzian carrier via complexification (signature caveat) | PROVEN (math) / DERIVED-CONDITIONAL (carrier) |
| **F34.SR** | **Finite-Symmetry Susceptibility-Rank Theorem:** for G-equivariant Z \> 0 and source c ∈ V^G, χ \= (1/4π²) c†(Z|\_{V^G})⁻¹ c, so N\_eff \= dim V^G ≠ dim V (GC30). Corollaries: dim V^G \= 0 ⟹ c \= 0; \= 1 ⟹ single mode; \= m ⟹ m×m block | PROVEN (general) |
| **F34.1** | Internal-fibre Y₆ \= M₄ × Σ₂: a 6-form needs dim ≥ 6, so M₄ × Σ₂ (4 \+ dim **Z** \= 6\) is the **minimal** carrier (6-dim total space, not a 6D spacetime) | DERIVED (minimal) / MINIMALITY-CONDITIONAL (unique) |
| **F34.2** | Parent-action wrapped-brane reduction ⇒ Z\_{ij}, and χ₋ \= (1/4π²) **ĉ**\_θ^T Z⁻¹ **ĉ**\_θ · e₆² (theta-coupling, distinct from Q\_source) | DERIVED-CONDITIONAL (anomaly gates) |
| **F34.M1** | λ\*-*invariance alone* fixes τ but **not** the Kähler area (c\_Σ free) | NO-GO (PROVEN) |
| **F34.M2** | v1.2 "Koenigs coordinate forces c\_Σ \= 1" | **RETRACTED** (non sequitur) |
| **F34.M3** | **Principal-polarization candidate metric:** Θ\_Z (c₁ \= 1\) ⇒ representative Area \= 1, V\_Σ \= 1 | METRIC-IDENTIFICATION-CONDITION |
| **F34.4** | g\_reg² \= 6**A**/**Q** \= 210/4807 (ZS-M6); EFT match Z\_match (in the **denominator** of Z, numerator of χ₋) | DERIVED-CONDITIONAL (matching) |
| **F34.4-NG** | v1.0 "even-dim Ray–Singer torsion" No-Go | **RETRACTED** (category error) |
| **F34.M4** | **G-Flux decomposition:** diagonality **DERIVED-COND**; **centrality OPEN** (needed only in path c); A₅ commutant M₄⊕M₄⊕M₆⊕M₇ (**dim 117**); 121 \= integral-lattice embedding (full index OPEN) | DECOMPOSED (centrality OPEN) |
| **F34.A5-1** | End(V₁₁) \= 3·1⊕6·3⊕6·3′⊕8·4⊕10·5, {baryon+DE} \= End−CDM \= 1·1⊕4·3⊕4·3′⊕6·4⊕8·5 (one singlet) | DERIVED (chars) / CONDITIONAL (baryon OPEN) |
| **F34.SEL** | **Singlet-selection (conditional on P\_b, P\_c orthogonal A₅-equivariant projectors):** a nonzero A₅-invariant θ-coupling exists **iff baryon ≠ 1⊕5**; singlet-free candidates {2·3, 3⊕3′, 2·3′} — A₅ alone does **not** uniquely pick 3⊕3′ | DERIVED-CONDITIONAL (excludes 1⊕5) |
| **F34.OUT-Math** | σ ∈ Out(A₅) swaps 3 ↔ 3′, fixes 1,4,5; only **3⊕3′** is σ-stable among singlet-free candidates ⇒ A₅ \+ σ-stability \+ no-baryon-singlet **uniquely** select 3⊕3′ (realized geometrically by F34.BIV) | DERIVED-CONDITIONAL |
| **G-Outer-Physical** | Identifying σ with a physical Z-Spin symmetry (seam orientation reversal / J\_Z parity / register automorphism / CPT exchange) | **OPEN** |
| **F34.A5-2** | **Single-mode reduction (path a):** if DE keeps the singlet **and** \[K, R(g)\] \= 0, χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) with ν\_s² \= v\_sᵀv\_s, G\_s \= sᵀG s, so q\_s \= v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s; **factor 83 replaced**. Bundled as I\_s := Z\_match v\_sᵀG⁻¹v\_s. If A₅ broken, Schur complement | DERIVED-CONDITIONAL (exact-A₅ \+ kinetic A₅); I\_s value OPEN |
| **F34.6** | Master χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² **ĉ**\_θ^T G⁻¹ **ĉ**\_θ; value 0.091847·e₆² only in path (c) at {V\_Σ=1, G=I, **ĉ**\_θ=uniform, Z\_match=1} | CANDIDATE (path c, aligned) |
| **F34.8** | Robust: the master quadratic form with N\_eff \= dim V^G (F34.SR); exact-A₅ branch reduces to I\_s \+ independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆); dimensionful residual e₆ | OPEN (terminus; P\_b, I\_s, e₆ → ZS-F35) |

The thermal-history material (formerly F34.7) is moved to the Outlook (§10), as it does not feed the charge-unit reduction.

---

# §1. Introduction

ZS-F32 proved that the absolute vacuum scale reduces to a single odd-sector susceptibility through ρ\_Λ,Z \= ½ χ₋ ω², ω \= arg λ\* \= 2.2592495540. ZS-F33 then showed *why* (**A**, **Q**) plus topology cannot finish: the energy spacing E\_k(θ) \= (e₋²/2Z₋)(k \+ θ/2π)² depends on the **dimensionful unit** χ₋ \= e₋²/(4π²Z₋), which flux integrality does not constrain (the *Charge-Unit Obstruction*, F33.8). F33.8D sketched the route — Y₆ \= M₄ × Σ₂, C₅ \= A₃⁻ ∧ ω₂ — and named ZS-F34 as the paper that would establish it.

The first release (v1.0) claimed that three of the four unknowns {V\_Σ, g₆, N, e₆} close, leaving e₆ as the sole residual. Seven successive external reviews progressively dismantled the over-claims. v1.1 reframed the result as three named gates. v1.2 claimed to close two; **v1.3 retracted both** (the Koenigs argument is a non sequitur; the flux coefficient hid a 121-fold ambiguity). **v1.4** corrected the centrality and carrier errors and introduced an A₅ analysis. **v1.5** corrected that analysis (Schur is four *multiplicity matrices*, commutant 117, not four scalars; the 83-decomposition is baryon-conditional; Z\_match was inverted) and computed a source trichotomy instead of a No-Go. **v1.6** corrected three v1.5 over-reaches (singlet-selection only *excludes* baryon \= 1 ⊕ 5; the single-mode reduction needs the *kinetic* operator A₅-invariant; the singlet *normalization* ν\_s is not fixed by A₅) and proposed an outer-automorphism selection plus a single-mode reduction. **v1.7 (this terminal version) fixes one real formula error and places two general theorems at the front:** the **Icosahedral Bivector Selection Theorem** (F34.BIV: Λ²V₄ \= 3 ⊕ 3′, which *geometrizes* v1.6's outer automorphism as the Hodge self-dual ↔ anti-self-dual swap under orientation reversal) and the **Finite-Symmetry Susceptibility-Rank Theorem** (F34.SR: for a G-equivariant kinetic operator and a source in V^G, the effective mode count is dim V^G, not the full flux rank — a statement of independent mathematical-physics interest). The one error fixed is the ν\_s²/G\_s double-counting in the single-mode susceptibility. The robust deliverable is the master quadratic form, with every unresolved gate located in an explicit factor; the residual computations (P\_b, the Singlet Response Invariant I\_s, and e₆) are deferred to ZS-F35.

Dependencies: ZS-F33 (obstruction, F33.8D route, the Koenigs-torus complex structure and theta-line c₁ \= 1), ZS-F32 (½χ₋ω²), ZS-M1 (z\*, λ\*), ZS-F5/F18 ((Z,X,Y) \= (2,3,6)), ZS-M6 (κ\_reg² \= **A**/**Q**, Dimensional Coupling Norm Theorem), ZS-M11/S1 (the A₅ \= icosahedral-rotation representation theory of the truncated-icosahedron Hodge complex), ZS-S4 (C\_M^sp, kept distinct), ZS-A17 (Spin–Metric No-Go), ZS-A24 (the type-II₁ corner and the continuous-trace face projectors), ZS-A28 (the rank/energy separation and the lattice no-go), ZS-A29/A30 (the rank-83 kinematic precursor and one-quantum-per-face). External: Bousso–Polchinski, Brown–Teitelboim, Ray–Singer, Milnor, Quillen/Mumford, Appell–Humbert.

**Notation (corrected in v1.1).** Two distinct constants are never written with the same symbol again:

$$\\kappa\_\\lambda := \-\\ln|\\lambda^\*| \= 0.1148346250\\quad(\\text{loxodromic decrement}),\\qquad \\kappa\_{\\rm reg}^2 := \\frac{\\mathbf{A}}{\\mathbf{Q}} \= \\frac{35}{4807}\\quad(\\text{register normalization}).$$

These differ numerically (6κ\_λ² \= 0.0791 ≠ 6**A**/**Q** \= 0.0437), and v1.0's shared symbol "κ" is a genuine source of confusion now removed. The gauge coupling is g\_reg² \= 6κ\_reg², and the torus area uses κ\_λ.

---

# §2. The Internal-Fibre Uplift (F34.1)

## 2.1 The "6" is a representation dimension

By F33.3A′, equating the complex-doubling count 2(d−1) with the bivector count d(d−1)/2 gives d \= 4, X \= 3, **Y \= 6 \= dim Λ²(ℝ^{1,3}) \= dim 𝔰𝔬(1,3)** \[**AC3**, PROVEN\]. This is the dimension of the Y-sector *field representation*, not a count of spacetime directions. (This distinction is used again, decisively, in §5.2.)

## 2.2 Why Kaluza–Klein is not licensed, and the internal-fibre route is forced

A Kaluza–Klein uplift would require an *independent* 6D spacetime metric. The present corpus does not license one: ZS-A17 Theorem F proves the spatial metric is **not reconstructible** from **A** or the spin structure, and ZS-F31 carries the spacetime metric as an imported datum. The corpus is explicit that asserting a 6D *spacetime* from the representation "6" is a **retraction trigger** (F33-G8D). We therefore read the "6" as the **internal-fibre product**

$$Y\_6 \= M\_4 \\times \\Sigma\_2,\\qquad M\_4 \= \\text{(existing 4D base)},\\quad \\Sigma\_2 \= \\text{(existing Z-sector 2-cycle)} ,$$

a product of structures the corpus *already* has — never a new 6D spacetime.

Two facts make Σ₂ forced. **(i)** The bivector 2-form must integrate over a 2-cycle; the *only* 2-cycle is the Z-sector Koenigs torus E\_λ\* (dim **Z** \= 2, b₂ \= 1; F33.2B PROVEN), so Σ₂ ≡ E\_λ\*. **(ii)** Consistency with F32: F32 places F₄⁻ \= dA₃⁻ in 4D, and wrapping C₅ \= A₃⁻ ∧ ω₂ on Σ₂ reproduces exactly that A₃⁻ (§3).

## 2.3 The degree-counting derivation: M₄ × Σ₂ as the *minimal* carrier (corrected in v1.4)

The factorization is strongly constrained by form degree, though — as a fourth review noted — it yields a *minimal* carrier, not a uniquely forced one. Start from what cosmology fixes: the odd sector is the 4D three-form A₃⁻ with field strength F₄⁻ \= dA₃⁻, a **4-form** (Kaloper–Sorbo; F32). Demand that A₃⁻ descend from a single parent gauge form by wrapping an internal harmonic form ω\_k on the internal cycle, G\_parent \= F₄⁻ ∧ ω\_k. Then:

- the internal cycle is the unique 2-cycle Σ₂ (b₂ \= 1), whose unique harmonic generator is a **2-form**, so k \= 2;  
- the parent field strength has degree 4 \+ k \= **6** (a 6-form G₆ \= dC₅), so the parent potential C₅ is a **5-form**;  
- a 6-form needs a carrier of dimension **≥ 6**. The product of the 4D base with the 2-cycle, dim(M₄ × Σ₂) \= 4 \+ dim **Z** \= 6, **saturates** this bound, so M₄ × Σ₂ is the **minimal** such carrier.

What the degree count proves is therefore *minimality*, not uniqueness: a carrier of dimension \> 6 with unused directions is not excluded by form degree alone. Uniqueness requires an added principle — **Minimal-Carrier** (no unused extra dimensions) or **Corpus-Completeness** (Σ₂ is the only internal cycle the corpus supplies). Under either, M₄ × Σ₂ is selected \[**GC15**\].

Two cautions, both from review. First, the kinetic term ∫\_{M₄×Σ₂} G₆ ∧ ⋆₆ G₆ genuinely uses a six-dimensional product metric and Hodge star, so the precise statement is: **M₄ × Σ₂ is a six-dimensional pseudo-Riemannian total space with four noncompact spacetime dimensions and a compact two-dimensional internal fibre** — *not* a claim of six observable spacetime dimensions (F33-G8D). Second, the field-representation count dim Λ²ℝ^{1,3} \= 6 and the carrier dimension 4 \+ dim **Z** \= 6 coincide, as do the corpus's bivector route C(4,2) \= 6 and sector-product route dim **X** × dim **Z** \= 3 × 2 \= 6; but these are *distinct arithmetic operations*, and their agreement is an internal-consistency indicator, **not** a proof of "not numerology." The four routes reconfirm the Y representation dimension; they do not by themselves single out M₄ × Σ₂ as the unique physical carrier.

**Theorem F34.1 \[DERIVED minimal / MINIMALITY-CONDITIONAL unique\].** Producing the 4D odd three-form A₃⁻ by wrapping the unique internal 2-cycle forces a five-form C₅ whose 6-form strength needs a carrier of dim ≥ 6; M₄ × Σ₂ (4 \+ dim **Z** \= 6 \= **Y**) is the minimal carrier, and is *the* carrier under a no-extra-dimension / corpus-completeness principle. It is a 6-dim total space, not a 6D spacetime. **Gate G-A1:** identifying Σ₂ with a non-corpus 2-cycle, asserting a 6D spacetime metric, or claiming uniqueness without the minimality principle, voids this (F33-G8D).

---

# §3. The Parent-Action Wrapped-Brane Reduction (F34.2)

v1.0 began directly from a 4D membrane term and the single normalization Z₋ \= V\_Σ/g₆². Review correctly noted that this skips the 6D→4D reduction and the anomaly bookkeeping that F33.8D required. v1.1 supplies the parent action and the reduction, and exposes the general (matrix) structure.

## 3.1 The parent action

We start in 6D with a five-form sector and wrapped 4-branes (5D worldvolume W₃ × Σ₂):

$$S\_6 \= \-\\tfrac{1}{2}\\int\_{M\_4\\times\\Sigma\_2} Z\_{IJ} G\_6^I\\wedge\\star\_6 G\_6^J \+ \\sum\_a e\_a^{(6)}\\int\_{W\_3^{(a)}\\times\\Sigma\_2} C\_5^a ,\\qquad G\_6^I \= dC\_5^I .$$

## 3.2 Harmonic expansion and the reduced data

Expanding each C₅^I on a basis {ω₂^i} of H²(Σ₂) — for the geometric torus b₂ \= 1, so a *single* ω₂ (the multiplicity question is deferred to §5) — with the theta-line cohomology normalization ∫\_Σ₂ ω₂ \= 1 (c₁ \= 1, F33.2B Computation Θ):

$$C\_5^I \= \\sum\_i A\_3^{(i)}(x)\\wedge\\omega\_2^i(y),\\qquad G\_6^I \= \\sum\_i F\_4^{(i)}(x)\\wedge\\omega\_2^i(y),$$

the kinetic term and the wrapped-brane term reduce, factorizing base and fibre, to

$$Z\_{ij}^{(4)} \= \\int\_{\\Sigma\_2} Z\_{IJ} \\omega\_2^i\\wedge\\star\_2\\omega\_2^j \= \\frac{1}{g\_6^2}\\int\_{\\Sigma\_2}\\omega\_2^i\\wedge\\star\_2\\omega\_2^j,\\qquad e\_i^{(4)} \= e\_i^{(6)}\\int\_{\\Sigma\_2}\\omega\_2^i \= e\_i^{(6)},\\qquad T\_{\\rm mem}^{(4)} \= T\_{\\rm 4\\text{-}brane}^{(6)}\\cdot\\mathrm{Area}(\\Sigma\_2) .$$

So the 4D membrane charge **e\_mem \= e₆^(6)** (with the unit-normalized ω₂), and its tension is the 6D 4-brane tension times the cycle area. The compact-3-form energy of F33 follows, with the kinetic normalization now a **matrix** Z\_{ij}, giving

$$\\chi\_- \= \\frac{1}{4\\pi^2} \\mathbf{c}*\\theta^{\\mathsf T} Z^{-1}\\mathbf{c}*\\theta$$

which reduces to the F33.8D scalar χ₋ \= e\_mem²/(4π²Z) only in the one-flux (b₂ \= 1\) case.

## 3.3 Anomaly gates

F33.8D required the wrapped sector to be anomaly-free. The reduction is therefore conditional on:

**Theorem F34.2 \[DERIVED-CONDITIONAL on the anomaly gates\].** χ₋ \= (1/4π²) **c**\_θ^T Z⁻¹ **c**\_θ, with (Z\_{ij}, e\_mem, T\_mem) as above. **Gate G-A2 (anomaly):** the charge lattice is unimodular; the membrane tadpole cancels; the global (mod-2) anomaly vanishes; orientation reversal acts as the J\_Z-odd parity; membrane nucleation changes the flux by exactly one unit. Any failure voids the reduction. *None of these is verified here* — they are the executable content of F33.8D's "anomaly-free wrapped sector."

---

# §4. The Metric Gate: No-Go (F34.M1), the Retracted Koenigs Argument (F34.M2), and the Principal-Polarization Metric (F34.M3, F34.3)

## 4.1 F34.M1: λ\*-invariance alone does not fix the Kähler area

**Theorem F34.M1 (Metric-Normalization Obstruction) \[NO-GO, PROVEN\].** λ\*-*invariance alone* fixes the *complex structure* of E\_λ\* (τ \= (ω \+ iκ\_λ)/2π, Im τ \> 0; F33.2B, DERIVED) but **not** the Kähler *area*. *Proof.* For any constant c\_Σ \> 0 the metric g\_{c\_Σ} \= c\_Σ²|d log w|² is invariant under w ↦ λ\*w (a constant rescaling commutes with the discrete action), with Area \= c\_Σ² · 2π κ\_λ \[**AC11**\]. So invariance leaves a one-parameter family.

The corpus theta-line normalization **c₁ \= 1** (∫\_Σ₂ ω₂ \= 1; F33.2B Computation Θ) is metric-*independent* and does not fix the area either \[**AC10**\] — *as a number*. Its role is deeper than v1.1/v1.2 used: it fixes the **degree** of the polarization (§4.3).

## 4.2 Retraction of the v1.2 Koenigs argument (F34.M2)

v1.2 argued (theorem F34.M2) that the Koenigs linearizing coordinate forces c\_Σ \= 1, because c\_Σ²|d log w|² supposedly corresponds to the power coordinate w^{c\_Σ} (whose multiplier λ\*^{c\_Σ} ≠ λ\* fails to linearize). External review correctly identified this as a **non sequitur**:

**F34.M2 \[RETRACTED\].** Choosing the Riemannian metric g\_{c\_Σ} \= c\_Σ²|d log w|² on the *same* Koenigs coordinate w is **not** the same operation as changing coordinates to w^{c\_Σ}. For any c\_Σ \> 0 the metric g\_{c\_Σ} is defined on the unchanged coordinate and remains invariant under w ↦ λ\*w. Koenigs' theorem fixes the linearizing coordinate up to a nonzero constant — the *conformal* structure — but the overall *Kähler scale* of the metric placed on that coordinate is a separate datum it does not determine. This confirms only that λ\*^{c\_Σ} ≠ λ\*, which is irrelevant to whether c\_Σ²|d log w|² is admissible. The Koenigs route is therefore withdrawn.

So after F34.M1 alone, V\_Σ reverts to **COMPUTED-UNDER-NORMALIZATION** — pending an *independent* metric-selection principle.

## 4.3 F34.M3: the principal polarization of the theta line fixes the scale (G-Metric)

That principle is the **polarization** the corpus already carries. F33.2B established the degree-1 theta line Θ\_Z with **c₁(Θ\_Z) \= 1** ("fibre flux," ∫\_Z curv \= 1), kept strictly separate from the flat Wilson line (c₁ \= 0). By the **Appell–Humbert theorem**, line bundles on the complex torus E\_τ \= ℂ/(ℤ \+ τℤ) are classified by a Hermitian form H with Im H(Λ, Λ) ⊆ ℤ; a **degree-1 positive** such bundle is a **principal polarization**, with

$$H(z,w) \= \\frac{z \\bar w}{\\operatorname{Im}\\tau},\\qquad |c\_1| \= |\\operatorname{Im}H(1,\\tau)| \= 1.$$

Its Kähler metric and form are ds²\_Θ \= |dz|²/Im τ and ω\_Θ \= (1/Im τ) dx ∧ dy, and the key point is that the **area equals the degree**:

$$\\operatorname{Area}(E\_\\tau) \= \\int\_{E\_\\tau}\\omega\_\\Theta \= c\_1 \= 1.$$

This is a **topological** equality — the area is the first Chern number, not a free Kähler modulus — which is exactly the datum the Koenigs argument lacked. (In the u \= log w coordinate the same metric reads ds²\_Θ \= |du|²/(2π κ\_λ); its conformal factor 1/(2π κ\_λ) \= 1.385949 is *numerically* the v1.2 "V\_Σ", but the invariant area is 1.) For the unit-class 2-form ω₂ the Hodge norm on this representative is therefore

$$V\_\\Sigma \= \\int\_{\\Sigma\_2}\\omega\_2\\wedge\\star\_2\\omega\_2 \= \\frac{1}{\\operatorname{Area}} \= 1.$$

*Convention.* We use ω\_Θ with ∫ω\_Θ \= c₁ in the normalization c₁ \= \[Im H\] (equivalently c₁ \= \[i F/2π\] for the Chern connection F); the corpus theta-line statement ∫\_Z curv \= 1 (F33.2B) is in the same normalization, so no 2π ambiguity enters between "fibre flux \= 1" and "Area \= 1."

v1.4 separates **three** distinct claims that v1.3 ran together:

1. the principal-polarization **class** is integral of degree 1 — **IMPORTED-PROVEN** (Appell–Humbert \+ F33.2B's c₁ \= 1);  
2. the chosen translation-invariant **representative** has normalized area 1, so V\_Σ \= 1 — **DERIVED** (a computation on that representative);  
3. that this representative is the **physical kinetic Hodge metric** — a **METRIC-IDENTIFICATION-CONDITION**, not a theorem.

**Theorem F34.M3 (Principal-Polarization Candidate Metric) \[METRIC-IDENTIFICATION-CONDITION\].** On the polarization representative of the degree-1 theta line Θ\_Z, Area \= c₁ \= 1 and V\_Σ \= 1\. The polarization class (degree 1\) is imported-proven and its representative area is derived; identifying it with the physical Hodge metric is the residual postulate. This is a **candidate normalization** of the metric scale, not a closure.

**Anti-numerology.** V\_Σ \= 1 is the statement Area \= c₁ \= 1 on the representative; the v1.2 near-miss to 2 ln 2 (which lived in the *conformal factor* 1.385949) is irrelevant to V\_Σ and is **dropped**.

**F34.3 \[DERIVED on the representative / identification-conditional\].** V\_Σ \= 1 on the principal-polarization representative (F34.M3). **Gate G-Metric:** reduced to the metric-identification condition — the polarization representative is the canonical candidate, but its identification with the physical metric is a postulate. The coefficient consequence (§7) is the *only* metric-dependence of χ₋.

---

# §5. The Coupling and the Retraction of the Torsion No-Go (F34.4, F34.4-NG)

## 5.1 The register coupling, and the missing matching

ZS-M6's **Dimensional Coupling Norm Theorem** (Peter–Weyl \+ rank-1 β₀, PROVEN) gives the *finite-register* block-Laplacian coupling

$$g\_{\\rm reg}^2 \= \\dim(Y)\\cdot\\kappa\_{\\rm reg}^2 \= 6\\cdot\\frac{\\mathbf{A}}{\\mathbf{Q}} \= \\frac{210}{4807} \= 0.04368629\\qquad\[\\textbf{AC16}\].$$

But — as review noted — that the *register* coupling equals the *continuum five-form* kinetic coefficient in S₆ is a **separate matching proposition**. It requires a quadratic-response identity

$$\\left.\\frac{\\delta^2\\Gamma\_{\\rm register}}{\\delta C\_5 \\delta C\_5}\\right|*{p\\to 0} \= \\frac{1}{g*{6,\\rm EFT}^2} \\Delta\_5,\\qquad g\_{6,\\rm EFT}^2 \= Z\_{\\rm match}\\cdot g\_{\\rm reg}^2,$$

with the wave-function renormalization Z\_match proved equal to 1\. This is **not done here**.

**F34.4 \[DERIVED-CONDITIONAL on the register→EFT matching\].** g\_reg² \= 6**A**/**Q** is the ZS-M6 register coupling; g\_{6,EFT}² \= Z\_match · g\_reg². **Gate G-Charge(matching):** Z\_match is OPEN; absent its proof, the continuum coupling is named g\_reg, not g₆.

A separate object must not be conflated: **C\_M^sp \= 11 ln 2 \+ ln 3 \= 8.7232** (ZS-S4) is the **Higgs-VEV** flat-direction determinant, *not* the gauge coupling \[**AC17**\].

## 5.2 Retraction of the even-dimensional torsion No-Go

v1.0 ruled out a "full-Y Ray–Singer torsion" source for the coupling/scale by asserting that the Y-sector is even-dimensional and even-dimensional analytic torsion vanishes. **This is retracted as a category error.**

1. The "6" of §2.1 is a **representation** dimension (dim Λ²(ℝ^{1,3})), not the dimension of the manifold on which a torsion is defined. The torsion-relevant geometry in the corpus is the BCC T³ quotient CW complex, not a 6-manifold.  
2. Ray–Singer triviality is usually invoked for the full **unitary** de Rham complex. The corpus quantity is **not** that: F33's ln 4 is a **seam-parity-restricted determinant functional**, the determinant of the Laplacian restricted to the ℤ₂-odd (seam-parity) sub-complex. The sign representation {±1} is itself orthogonal/unitary, so calling the bundle "non-unitary" is imprecise; the correct point is that the *restricted* complex is not the full de Rham complex, so the standard even-dimensional Hodge-duality cancellation does not apply to it. Concretely, F33.2B Computation ET finds this **2D T² seam-parity-restricted torsion to be ln 4 ≠ 0** \[**AC14**\] — even-dimensionality does *not* trivialize the restricted functional (and equivariant even-dimensional torsion has its own vanishing theorems, so "even ⇒ zero" was never the right lemma).  
3. The spectral route to the *scale* is nonetheless closed-negative, but by the **F33.5/A28 involution-independent lattice no-go**: the achievable seam-parity-restricted log-determinants lie in {a ln 2 \+ b ln 3 : a, b ∈ ℤ≥0}, and the back-solved target 8.190 is not in that lattice \[**AC15**\].

**F34.4-NG \[RETRACTED → restated\].** The even-dimensional-vanishing argument is withdrawn. The correct statements are: (i) the corpus's **seam-parity-restricted determinant torsion** (F33's terminology, retained here) is non-zero, ln 4 (AC14) — the issue is the restriction of the complex, not a failure of unitarity; (ii) the spectral route to the χ₋ *scale* is CLOSED-NEGATIVE by the lattice no-go (AC15), consistent with ZS-A28 keeping the absolute scale OPEN.

---

# §6. The Flux Multiplicity (F34.5)

This is the deepest of v1.0's overclaims, and v1.1 demotes it to an explicit open gate.

## 6.1 b₂ \= 1 gives one flux; "83" is a trace, not a flux count

The geometric cycle has **b₂(Σ₂) \= 1** \[**AC18**\], so §3 yields a **single** harmonic ω₂ and a single 4D four-form. The dark-energy "83" is *not* 83 two-cycles. In ZS-A24 the dark-energy sector is the projector P\_Λ in the **type-II₁ corner** M\_obs, carrying the **continuous trace** τ(P\_Λ) \= 83/121; since 121 \> Q \= 11, these are *not* integer projection ranks in M₁₁ — they are continuous-trace weights \[**AC19**, **AC20**\]. So 83 is a **trace**, not a count of independent fluxes.

## 6.2 ZS-A29 is a kinematic precursor, not a proof

v1.0 wrote "ZS-A29 proves that this rank-83 flux vector is free." This **misstates A29**, which treats the rank-83 occupation only as a *Bousso–Polchinski-type kinematic precursor* and keeps **OPEN**: the G2 flux collectivization, whether the rank-83 occupation is a genuine independent flux vector, and the rank-to-energy identification. v1.1 carries these at A29's actual status.

## 6.3 The G-Flux decomposition: the theta-coupling quadratic form and its sub-gates (F34.M4)

v1.2 claimed to *settle* the realization of 83 as a flux coefficient; v1.3–v1.4 decomposed it but mislabelled the A₅ structure. v1.5 corrects the representation theory and states the robust object as the **theta-coupling quadratic form**, with the dimensionful charge factored out (c\_θ \= e₆ ĉ\_θ, \[ĉ\_θ\] \= 1, \[e₆\] \= E²) and Z\_match in its correct place:

$$\\chi\_- \= \\frac{1}{4\\pi^2} \\mathbf{c}*\\theta^{\\mathsf T} Z^{-1}\\mathbf{c}*\\theta \= \\frac{Z\_{\\rm match} g\_{\\rm reg}^2}{4\\pi^2 V\_\\Sigma} e\_6^2 \\hat{\\mathbf c}*\\theta^{\\mathsf T} G^{-1}\\hat{\\mathbf c}*\\theta,\\qquad Z\_{ab} \= \\frac{V\_\\Sigma}{Z\_{\\rm match} g\_{\\rm reg}^2} G\_{ab},\\quad G\_{ab} \= \\tau(q\_a K q\_b).$$

(Defining g²\_{6,EFT} \= Z\_match g²\_reg puts Z\_match in the **denominator** of Z, so χ₋ scales as \+Z\_match; v1.4 had this inverted \[**GC12**\].) Here **ĉ**\_θ is the dimensionless **theta-coupling direction**, distinct from the membrane charge-lattice map Q\_source (whose Smith-normal-form rank sets Path A/B); identifying them at rank 83 silently assumes equal θ-coupling ⇔ equal membrane charge.

**(a) Coefficient-module monodromy.** A flat rank-83 coefficient bundle carries commuting monodromies U\_Λ, V\_Λ ∈ U(83); the massless count is r\_flux \= dim(ker(U\_Λ − I) ∩ ker(V\_Λ − I)), which for commuting unitaries equals the coinvariant dimension dim E/((U\_Λ−I)E \+ (V\_Λ−I)E) (lemma; verified both ways). The cases **r\_flux \= 83 (trivial), 82 (one phase), 0 (generic)** \[**GC14**\] make the *trivial* bundle a **load-bearing assumption**: motivated by the face algebra being a constant channel over Σ₂, but to be DERIVED one must compute ρ\_Λ(γ₁ \= 2πi), ρ\_Λ(γ₂ \= log λ\*) on the actual face module.

**(b) The 121 is an integral charge-lattice embedding (corrected in v1.4).** v1.3 called the factor 121 a "basis ambiguity." That is wrong: a *genuine* basis change S sends Z → S⁻ᵀZS⁻¹ and **c**\_θ → S⁻ᵀ**c**\_θ, leaving **c**\_θᵀZ⁻¹**c**\_θ **invariant** \[**GC13**\]. The factor 121 instead arises from re-declaring the **unit charge \= 1** in two *different integral lattices* — the idempotent lattice (τ(q\_a) \= 1/121) versus the orthonormal-τ lattice (q̂\_a \= √121 q\_a) — i.e. it is an **integral charge-lattice embedding** ambiguity (two exhibited embeddings differ by 121; full index OPEN). The basis-independent quantity is q\_min² \= min\_{v∈Λ} vᵀG⁻¹v. Fixing it is exactly the **finite-to-core lift F-A24.9**, now sharpened to a *trace-preserving integral charge-lattice intertwiner* ι\_Λ : (ℤ⁸³, Q\_fin) → (M\_obs, τ) with ⟨ι e\_a, ι e\_b⟩\_τ \= G\_ab and ι(Λ\_fin) \= Λ\_core — stronger than a Hilbert-space isometry, and **OPEN**.

**(c) Kinetic centrality is OPEN, and A₅ alone does not close it (Schur corrected in v1.5).** Centrality is the condition

$$P\_\\Lambda K P\_\\Lambda \= k\_\\Lambda P\_\\Lambda .$$

Uniform trace does *not* give it: with q\_a \= |a⟩⟨a|, τ(q\_a K q\_b) \= (1/121) K\_{aa} δ\_{ab}, so orthogonality gives only **diagonality**; the counterexample K \= diag(1, …, 83\) has equal face traces yet all-different Z\_{aa} (a one-line consequence). v1.4 then claimed the corpus A₅ symmetry makes an invariant K "block-scalar with ≥4 distinct eigenvalues." **This misapplies Schur's lemma.** Because each irrep occurs with multiplicity, the dark-energy module is (for the illustrative baryon 6 \= **1** ⊕ **5**)

$$H\_\\Lambda \= (\\mathbf{3}\\otimes\\mathbb{C}^4)\\oplus(\\mathbf{3'}\\otimes\\mathbb{C}^4)\\oplus(\\mathbf{4}\\otimes\\mathbb{C}^6)\\oplus(\\mathbf{5}\\otimes\\mathbb{C}^7),$$

and an A₅-invariant K is **not** four scalars but four **multiplicity matrices**,

$$K \= \\big(I\_3\\otimes K\_3\\big)\\oplus\\big(I\_{3'}\\otimes K\_{3'}\\big)\\oplus\\big(I\_4\\otimes K\_4\\big)\\oplus\\big(I\_5\\otimes K\_5\\big),\\qquad K\_3,K\_{3'}\\in M\_4,\\ K\_4\\in M\_6,\\ K\_5\\in M\_7 .$$

The commutant has complex dimension 4² \+ 4² \+ 6² \+ 7² \= **117** \[**GC7**\], so a Hermitian K carries up to 4 \+ 4 \+ 6 \+ 7 \= **21** eigenvalues (and could, by coincidence, have as few as one — so "≥4 distinct" is also false). An explicit A₅-invariant but non-central example is K \= I₃ ⊗ diag(1, 2, 3, 4\) on one sector \[**GC8**\]. The general A₅-invariant susceptibility is therefore

$$\\chi\_- \= \\frac{1}{4\\pi^2}\\sum\_{\\rho\\in{3,3',4,5}} \\mathbf{c}*\\rho^{\\dagger}\\big(I*{d\_\\rho}\\otimes K\_\\rho^{-1}\\big)\\mathbf{c}\_\\rho\\qquad\[\\textbf{GC9}\],$$

and the simple factor 83 requires *three* things at once — K\_ρ \= k I for all ρ (scalarity), the same k across ρ (centrality), and the source alignment ‖c\_ρ‖² ∝ d\_ρ m\_ρ. **Status: kinetic DIAGONALITY DERIVED-CONDITIONAL; kinetic CENTRALITY OPEN; A₅ alone is insufficient (commutant 117 \> 1).**

**(c′) The baryon embedding, the singlet, and the outer-automorphism selection (refined in v1.6).** v1.5 observed that {baryon \+ dark energy} \= End(V₁₁) − F\_TI \= **1·1 ⊕ 4·3 ⊕ 4·3′ ⊕ 6·4 ⊕ 8·5** \[**GC3**\] carries exactly one singlet, and that a nonzero A₅-invariant source needs dark energy to keep it. v1.6 makes this precise on two points a sixth review raised, then strengthens it.

First, the statement only makes representation-theoretic sense if **P\_b and P\_c are mutually orthogonal A₅-equivariant projectors** (\[P\_b, R(g)\] \= \[P\_c, R(g)\] \= 0); then P\_Λ \= I − P\_b − P\_c is A₅-invariant and the "location" of the singlet is well-defined. If P\_b is not A₅-equivariant, the singlet has no definite location and one is already in the symmetry-broken branch (c).

Second, the selection does **not** uniquely pick 3 ⊕ 3′. Enumerating the rank-6 A₅-submodules of {baryon \+ DE} exhaustively \[**GC17**, **GC18**\]:

| baryon 6 | dark energy (83) | singlet in DE | invariant ĉ\_θ |
| ----- | ----- | :---: | :---: |
| **1** ⊕ **5** | 4·3 ⊕ 4·3′ ⊕ 6·4 ⊕ 7·5 | 0 \[**GC4**\] | none |
| **2·3** | 1·1 ⊕ 2·3 ⊕ 4·3′ ⊕ 6·4 ⊕ 8·5 | 1 | unique up to scale |
| **3** ⊕ **3′** | 1·1 ⊕ 3·3 ⊕ 3·3′ ⊕ 6·4 ⊕ 8·5 | 1 \[**GC5**\] | unique up to scale |
| **2·3′** | 1·1 ⊕ 4·3 ⊕ 2·3′ ⊕ 6·4 ⊕ 8·5 | 1 | unique up to scale |

**Theorem F34.SEL (Singlet-Selection) \[DERIVED-CONDITIONAL\].** Conditional on P\_b, P\_c being mutually orthogonal A₅-equivariant projectors, a nonzero A₅-invariant linear theta-coupling exists **iff** the dark-energy module retains the single available singlet — i.e. iff baryon ≠ **1** ⊕ **5**. This *excludes* 1 ⊕ 5 but leaves three singlet-free candidates {2·3, 3 ⊕ 3′, 2·3′}; A₅ alone does **not** select 3 ⊕ 3′.

The extra structure that *does* select 3 ⊕ 3′ is the outer automorphism, and v1.7 **realizes it geometrically** rather than positing it. A₅ has Out(A₅) ≅ ℤ₂, generated by σ (an odd permutation of the five points); σ exchanges the two 5-cycle classes, so on irreps **σ: 3 ↔ 3′, with 1, 4, 5 fixed** \[**GC19a**\], and among the singlet-free candidates 2·3 ↔ 2·3′ while **3 ⊕ 3′ is σ-stable** \[**GC19b**\]. The geometric content is the exterior square of the standard 4-dimensional module.

**Theorem F34.BIV (Icosahedral Bivector Selection).** Let V₄ be the standard real four-dimensional A₅-module (the sum-zero subspace of the S₅ permutation representation on ℝ⁵). Then $$\\Lambda^2 V\_4 \\cong \\mathbf 3 \\oplus \\mathbf 3',$$ a textbook character identity (χ\_{Λ²4} \= ½\[χ₄(g)² − χ₄(g²)\] \= (6, −2, 0, 1, 1\) \= χ₃ \+ χ₃′, **GC27**). Over S₅ this is the six-dimensional *irreducible* (norm 1, **GC28**), so no S₅-equivariant splitting of the two triplets exists. In an oriented 4-dimensional **Euclidean** metric space (signature \++++, ⋆² \= \+1 on real 2-forms) Λ²V₄ \= Λ²₊ ⊕ Λ²₋ (self-dual ⊕ anti-self-dual, each 3-dimensional); A₅ ⊂ SO(V₄) commutes with the Hodge star and **preserves each triplet**, while an orientation-reversing odd permutation (det \= −1) anticommutes with the Hodge star and **swaps Λ²₊ ↔ Λ²₋**, i.e. **3 ↔ 3′** \[**GC29**\]. Thus 3 ↔ 3′ *is* self-dual ↔ anti-self-dual under orientation reversal. The same 3 ⊕ 3′ is the standard decomposition of the six-dimensional crystallographic icosahedral representation T₁ ⊕ T₂ (IMPORTED-PROVEN), an independent cross-check. **Status: PROVEN (representation theory).**

*Signature caveat (v1.8).* F34.BIV is formulated on the **Euclidean** standard A₅-module V₄, where ⋆² \= \+1 gives a *real* self-dual/anti-self-dual split. The corpus carrier Y \= dim Λ²(ℝ^{1,3}) is a **Lorentzian** bivector space, where on real 2-forms ⋆² \= −1 and the self-dual/anti-self-dual decomposition appears only after complexification (as the ±i eigenspaces of ⋆). The identification of V₄'s exterior square with the Lorentzian bivector carrier therefore requires complexification or an explicit signature-changing intertwiner, and remains part of the (DERIVED-CONDITIONAL) carrier bridge — not a real-orthogonal identity.

This converts v1.6's F34.OUT into two claims of *different* status, which v1.7 keeps separate:

**F34.OUT-Math \[DERIVED-CONDITIONAL\].** Conditional on identifying the corpus rank-6 Y/baryon carrier with Λ²V₄, the module **3 ⊕ 3′** is selected with no additional representation assignment: it is the unique σ-stable singlet-free rank-6 A₅-module, and σ is realized as the orientation-reversing (Hodge ±-swapping) symmetry of F34.BIV. (The coincidence 6 \= dim **X** × dim **Z** \= 3 × 2 plays no role in the proof.) **Scope (v1.8):** F34.BIV selects the *representation type* 3 ⊕ 3′; it does **not** by itself fix the actual baryon projector P\_b. Inside {baryon \+ dark energy} \= **1** ⊕ (3 ⊗ ℂ⁴) ⊕ (3′ ⊗ ℂ⁴) ⊕ (4 ⊗ ℂ⁶) ⊕ (5 ⊗ ℂ⁸), choosing a 3 ⊕ 3′ submodule means choosing one line in each multiplicity space ℂ⁴, i.e. P\_b \= I₃ ⊗ |u⟩⟨u| ⊕ I₃′ ⊗ |u′⟩⟨u′| with \[u\] ∈ ℂP³; σ-stability forces u′ \= S\_σ u but a residual ℂP³ multiplicity-line freedom remains. Fixing P\_b is a *dynamical* question (a parent-Hessian spectral selection), deferred to ZS-F35 (§10).

**G-Outer-Physical \[OPEN\].** Whether the orientation-reversing σ is a *physical* Z-Spin symmetry — seam-orientation reversal, J\_Z parity, a register automorphism, or a CPT-related exchange — is open. F34.BIV makes σ geometric (a Hodge involution), which sharpens but does not close this identification.

The carrier bridge is the more honest framing of the earlier "Y \= bivector module": the corpus already uses Y \= 6 \= dim Λ²(ℝ^{1,3}), and F34.BIV says the *internal* rank-6 module is likewise an exterior square — of the icosahedral V₄.

Three source-symmetry paths then follow \[**GC10**, **ID1**\]:

- **(a) dark energy keeps the singlet, K is A₅-invariant.** Then \[K, R(g)\] \= 0 forces the singlet block to decouple, P\_s K (I − P\_s) \= 0 \[**GC21**\], and an A₅-invariant source couples only to the **1-dimensional** invariant subspace. The susceptibility is a **single mode** (see §7), and the factor 83 is *replaced*. (If K breaks A₅, even a singlet source mixes via the Schur complement \[**GC22**\], (Z⁻¹)\_ss \= 1/(Z\_ss − B D⁻¹ B†) ≠ 1/Z\_ss — so the kinetic A₅-invariance is a genuine extra hypothesis.)  
- **(b) dark energy has no singlet** (baryon \= 1 ⊕ 5). An exact-A₅ linear source must vanish; a nonzero source needs explicit/spontaneous A₅ breaking or a spurion ĉ\_θ \= I(s).  
- **(c) A₅ is broken in the source sector.** Then ĉ\_θ is a spurion and the factor 83 returns *only* with the alignment ‖c\_ρ‖² ∝ d\_ρ m\_ρ together with full centrality. **The central number 0.091847 lives entirely in path (c).**

So the honest content is a *trichotomy*; single-mode (a) is **one branch, not generic**, since the singlet's location is open. Determining the branch requires constructing the actual baryon/CDM projectors and the vacuum character (§10).

**(d) The theta-coupling direction** is resolved by (c′): in path (a) ĉ\_θ is the singlet (fixed up to scale, *not* uniform in the face basis); the uniform ĉ\_θ \= (1, …, 1\) belongs to path (c). A single θ-mode does **not** imply rank Q\_source \= 1 — the susceptibility direction ĉ\_θ and the membrane charge-lattice map Q\_source stay distinct, so Path A/B is still set by rank Q\_source.

**(e) Path A vs Path B.** Set by the Smith normal form of Q\_source ∈ M\_{N×r\_flux}(ℤ): rank r\_flux → Path A, rank 1 → Path B, intermediate → partial; elementary divisors d\_i \= 1 → primitive. The v1.2 claim that orthogonality excludes Path B is **withdrawn**. Status: **Path selection OPEN.**

## 6.4 Honest status: decomposed, not closed

**F34.M4 \[DECOMPOSITION; centrality OPEN; A₅ paths computed\].** The flux coefficient decomposes into {monodromy (a), charge-lattice embedding (b), kinetic centrality (c), A₅ source paths (c′), Path selection (e)}. Only kinetic *diagonality* is derived; **centrality is OPEN and A₅ alone cannot close it** — the commutant is M₄ ⊕ M₄ ⊕ M₆ ⊕ M₇ (dim 117), permitting up to 21 eigenvalues, not four scalars. The source structure resolves into a **trichotomy** (F34.SEL): (a) single-mode if dark energy keeps the lone singlet *and* K is A₅-invariant; (b) zero unless A₅ is broken, if it does not; (c) the factor-83 form only under A₅-breaking with source alignment. The baryon module is selected uniquely to 3 ⊕ 3′ only with the outer automorphism (F34.OUT). The 121 is an integral-lattice embedding (two embeddings differ by 121; full index OPEN), and Path A/B awaits the Smith normal form of Q\_source. **Gate G-Flux: DECOMPOSED; the central factor-83 candidate lives only in path (c); path (a) admits the single-mode closure of §10.**

The Bousso–Polchinski *gap* (dense discretuum) remains a separate, still-open question (the shell density of Λ(**n**) \= Λ\_bare \+ ½ **n**^T Q **n** needs Q fixed and counted; §10); the susceptibility does not require it.

---

# §7. The Susceptibility: the Finite-Symmetry Rank Theorem (F34.SR, F34.6)

The single most transferable statement in this paper is that the source-coupled susceptibility of a multi-four-form theory is controlled not by the number of fluxes but by the dimension of the invariant subspace the source lives in.

**Theorem F34.SR (Finite-Symmetry Susceptibility-Rank) \[PROVEN\].** Let a finite group G act unitarily on a finite-dimensional flux space V, let Z \> 0 be G-equivariant (R(g)†ZR(g) \= Z for all g), and let the source satisfy c ∈ V^G (R(g)c \= c). Then Z⁻¹ is G-equivariant and preserves the orthogonal decomposition V \= V^G ⊕ (V^G)^⊥, so the off-block part of Z⁻¹ annihilates c and $$\\chi \= \\frac{1}{4\\pi^2}\\mathbf c^{\\dagger} Z^{-1}\\mathbf c \= \\frac{1}{4\\pi^2}\\mathbf c^{\\dagger}\\big(Z|*{V^G}\\big)^{-1}\\mathbf c,\\qquad N*{\\rm eff} \= \\dim V^G.$$ The effective mode count is the **invariant-source rank dim V^G, not the full flux rank dim V** \[**GC30**\]. More precisely, if the admissible sources occupy a subspace S\_src ⊆ V^G, the response is confined to V^G and the maximal invariant-source rank is N\_eff \= dim S\_src ≤ dim V^G, with equality when the admissible sources span V^G. Corollaries: **(i)** dim V^G \= 0 ⟹ c \= 0 (no invariant source); **(ii)** dim V^G \= 1 ⟹ an exact **single-mode** susceptibility; **(iii)** dim V^G \= m \> 1 ⟹ an m×m invariant-block susceptibility c†(Z|\_{V^G})⁻¹c. (In F34's exact-A₅ branch dim V^{A₅} \= 1, so S\_src \= V^{A₅} and N\_eff \= 1 regardless.)

The proof is one line of representation theory (a G-equivariant operator preserves isotypic components, and V^G is the trivial-isotypic one), but the consequence is not folklore in the flux-landscape setting: the common heuristic "N fluxes contribute N modes to the vacuum susceptibility" is **false** whenever the source respects a symmetry — only the invariant directions respond. Changing the kinetic eigenvalues on (V^G)^⊥ leaves χ untouched \[**GC31**\]. In F34 this is exactly why the "factor 83" was never the right multiplicity for an A₅-invariant source.

**Application to F34.** With the master normalization (c\_θ \= e₆ ĉ\_θ, \[ĉ\_θ\] \= 1, \[e₆\] \= E²),

$$\\chi\_- \= \\frac{1}{4\\pi^2}\\mathbf{c}*\\theta^{\\mathsf T} Z^{-1}\\mathbf{c}*\\theta \= \\frac{Z\_{\\rm match}g\_{\\rm reg}^2}{4\\pi^2V\_\\Sigma}e\_6^2\\hat{\\mathbf c}*\\theta^{\\mathsf T} G^{-1}\\hat{\\mathbf c}*\\theta,\\qquad Z \= \\frac{V\_\\Sigma}{Z\_{\\rm match}g\_{\\rm reg}^2}G,\\quad G\_{ab} \= \\tau(q\_a K q\_b),$$

with Z\_match in the **denominator** of Z, hence the **numerator** of χ₋ \[**GC12**\]. In the baryon/CDM-equivariant single-singlet branch, dim H\_Λ^{A₅} \= 1, so by F34.SR N\_eff \= 1 and the susceptibility is single-mode — *without* proving full 83-dimensional centrality. Which number χ₋ yields depends on the A₅ source path of §6.3(c′):

- **Path (a) — dark energy keeps the singlet, K is A₅-invariant (dim V^G \= 1).** A₅ fixes the singlet *direction* s but not its *magnitude*. Writing the primitive integral source as v\_s \= ν\_s s, with the **lattice norm** ν\_s² := v\_sᵀv\_s \= ⟨v\_s, v\_s⟩₀ and the **Hessian norm** G\_s := sᵀG s, the full quadratic form is q\_s := v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s (since for A₅-invariant G the singlet is an eigenvector, G⁻¹s \= G\_s⁻¹s), so

$$\\chi\_-^{(s)} \= \\frac{Z\_{\\rm match}g\_{\\rm reg}^2}{4\\pi^2V\_\\Sigma}e\_6^2\\frac{\\nu\_s^2}{G\_s}  \=  \\frac{Z\_{\\rm match}g\_{\\rm reg}^2}{4\\pi^2V\_\\Sigma}e\_6^2q\_s\\qquad\[\\textbf{GC23}, \\textbf{GC32}\].$$

(**v1.7 fix:** v1.6 wrote ν\_s² \= v\_sᵀG⁻¹v\_s *and* divided by G\_s, double-counting the kinetic norm; the corrected reading separates the lattice norm ν\_s² \= v\_sᵀv\_s from G\_s \= sᵀG s.) There is no factor 83 — but the integral-lattice (121 / F-A24.9) problem **persists as the single number ν\_s**. It is convenient to bundle the three remaining single-mode unknowns into one basis-independent **Singlet Response Invariant**

$$\\boxed{I\_s := Z\_{\\rm match}v\_s^{\\mathsf T} G^{-1} v\_s}\\qquad\\Longrightarrow\\qquad \\chi\_-^{(s)} \= \\frac{g\_{\\rm reg}^2e\_6^2}{4\\pi^2V\_\\Sigma}I\_s,$$

which folds together register-to-EFT matching (Z\_match), the singlet Hessian norm (G\_s), and the primitive-source lattice normalization (ν\_s). **What F34 asks of an external calculator is therefore not the full 83×83 matrix but a single zero-momentum singlet-response residue I\_s** (definition basis-independent: DERIVED; value: OPEN, → ZS-F35). (If K breaks A₅, even this is corrected by the Schur complement (Z⁻¹)\_ss \= 1/(Z\_ss − B D⁻¹ B†) \[**GC22**\].)

- **Path (b) — no singlet (dim V^G \= 0).** An exact-A₅ source vanishes; a nonzero source needs breaking or a spurion.  
- **Path (c) — A₅ broken, fully aligned and central.** Only here does the factor 83 appear. Setting V\_Σ \= 1, G \= I (central), ĉ\_θ \= (1, …, 1), Z\_match \= 1,

$$\\chi\_- \= \\frac{83 g\_{\\rm reg}^2}{4\\pi^2} e\_6^2 \= 0.091847\\cdot e\_6^2\\qquad\[\\textbf{GC11}\],\\qquad \\rho\_{\\Lambda,Z} \= \\tfrac12\\chi\_-\\omega^2 \= 0.234402\\cdot e\_6^2\\qquad\[\\textbf{GC16}\].$$

(The v1.3 value ρ \= 0.234426 was an arithmetic slip; 0.09184669 × ω²/2 \= 0.09184669 × 2.5521043 \= **0.23440234**.) The shift from the v1.2 number 0.066270 to 0.091847 is the metric correction V\_Σ : 1.385949 → 1 (a factor 2π κ\_λ \= 0.7215).

**F34.6 \[CANDIDATE — path (c), aligned\].** χ₋ \= 0.091847 · e₆² (with Z\_match \= 1\) is the value of the master form **only** in path (c) at the fully aligned central point {V\_Σ \= 1; G \= I (central — A₅ alone does not give this, commutant 117); ĉ\_θ \= (1, …, 1\) with the alignment ‖c\_ρ‖² ∝ d\_ρ m\_ρ; orthonormal-τ lattice (F-A24.9); Z\_match \= 1; anomaly-free}. In the exact-A₅ single-mode branch (a) the susceptibility is instead (Z\_match g\_reg²/4π² V\_Σ) e₆² q\_s \= (g\_reg² e₆²/4π² V\_Σ) I\_s, controlled by the single invariant I\_s, with **no** factor 83\. The only basis-independent statement is the master form itself.

**Corollary F34.SR-Branch (Symmetry-Branch Ratio).** At fixed {V\_Σ, Z\_match, e₆}, the two branches differ by a *structural* factor, not a normalization: $$\\frac{\\chi\_{83}^{(c,\\rm aligned)}}{\\chi\_{\\rm singlet}^{(a)}} \= \\frac{83}{q\_s}.$$ At the benchmark q\_s \= 1 the ratio is exactly **83**. Matching the same observed vacuum density in the single-mode branch instead of the aligned-83 branch raises the characteristic charge scale by 83^{1/4}: where path (c) reports e₆ ≈ (3.219 meV)², path (a) at q\_s \= 1 reports √e₆ ≈ 9.72 meV. This is **not** a prediction; it is a conditional discriminator that an independent determination of e₆ (ZS-F35) would resolve. **Status: DERIVED-CONDITIONAL / REPORTED.**

---

# §8. The Residual: One Dimensionful Charge Behind a Conditional List (F34.8)

The cleanest way to record the residual is to write the master form and label which gate sits in each factor (the under-labels are given in prose to avoid fragile markup):

$$\\chi\_- \= \\frac{1}{4\\pi^2} \\mathbf{c}*\\theta^{\\mathsf T} Z^{-1}\\mathbf{c}*\\theta,\\qquad Z \= \\frac{V\_\\Sigma}{Z\_{\\rm match} g\_{\\rm reg}^2} G,\\qquad G\_{ab} \= \\tau(q\_a K q\_b),\\qquad \\mathbf{c}*\\theta \= e\_6 \\hat{\\mathbf c}*\\theta .$$

The factor V\_Σ carries G-Metric; the prefactor Z\_match/g\_reg² carries G-Charge; the matrix G \= τ(q\_a K q\_b) carries the G-Flux sub-gates (a) monodromy, (b) charge-lattice embedding, and (c) centrality; the direction ĉ\_θ carries the G-Flux source paths (c′); and rank Q\_source carries the Path-A/B sub-gate (e).

| Gate | Factor it controls | v1.7 status |
| ----- | ----- | ----- |
| **G-Metric** | V\_Σ | **Candidate normalization** V\_Σ \= 1 (principal-polarization representative; F34.M3). Koenigs RETRACTED. METRIC-IDENTIFICATION-CONDITION. |
| **G-Flux (a)** | monodromy r\_flux | Trivial bundle (r \= 83\) a load-bearing assumption (toy holonomy only). |
| **G-Flux (b)** | charge-lattice embedding | Two exhibited embeddings differ by 121; full index OPEN → F-A24.9. |
| **G-Flux (c)** | G \= τ(q\_a K q\_b) | Diagonality DERIVED; **centrality OPEN**; A₅ commutant **117** (M₄⊕M₄⊕M₆⊕M₇), not four scalars. |
| **G-Flux (c′)** | ĉ\_θ (source) | **Trichotomy** (F34.SEL): (a) single-mode singlet, (b) zero unless A₅ broken, (c) factor 83 under alignment. |
| **G-Flux (e)** | rank Q\_source | Path A/B OPEN (Smith normal form). |
| **G-Charge** | Z\_match, e₆ | Z\_match (denominator of Z) OPEN; **e₆** the sole *dimensionful* OPEN (F33-G12). |

The dimensionful content does reduce to the **single charge e₆**, but only *behind* this list. Were the list discharged in path (c) at the aligned central point and e₆ fixed, reproducing ρ\_Λ,obs ≈ (2.24 meV)⁴ would require **e₆ ≈ (3.219 meV)²** \[REPORTED, not a claim; firewall F34-G5\].

**F34.8 \[OPEN — the honest terminus\].** The robust result is the master form χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² ĉ\_θᵀ G⁻¹ ĉ\_θ. The dimensionful residual is e₆, but the dimensionless coefficient is conditional on the factor map above, of which only the metric *class* (c₁ \= 1), kinetic *diagonality*, and the *representation-theoretic structure* (the singlet count, the commutant 117, the outer-automorphism σ-stability of 3 ⊕ 3′) are settled — kinetic *centrality*, the singlet's location, the charge-lattice embedding (now ν\_s in the single-mode branch), Path selection, anomaly cancellation, and Z\_match are not. "Sole remaining dimensionful OPEN \= e₆" may be written **only after** the list is discharged; v1.7 does not claim it. The contribution is the **bivector selection** of the baryon module (F34.BIV), the **finite-symmetry susceptibility-rank theorem** (F34.SR, N\_eff \= dim V^G), and the **single-mode reduction** — by F34.SR the 83-dimensional flux/source realization reduces to the five one-dimensional objects {P\_s, G\_s, ν\_s, (U\_s, V\_s) \= 1, Q\_s}, while the **independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates remain**. This is a *reduction*, not a closure; the actual P\_b, I\_s, e₆ are deferred to ZS-F35.

---

# §9. Falsification Gates

| Gate | Layer | Condition that voids the result |
| ----- | ----- | ----- |
| **G-A1** | Mathematical | Σ₂ ≠ E\_λ\*, or a 6D spacetime metric is asserted that the corpus does not supply. |
| **G-A2** | Theoretical | Any anomaly gate fails (lattice non-unimodular, tadpole/global-anomaly non-cancelling, nucleation ≠ one unit). |
| **G-Metric** | Mathematical | V\_Σ claimed *derived* (it is a metric-identification candidate); or the Koenigs argument re-used (RETRACTED); or V\_Σ \= 2 ln 2 claimed. |
| **G-Flux** | Mathematical | Kinetic *centrality* claimed from uniform trace or from A₅ alone (commutant is 117, not ℂI); an A₅-invariant K called "block-scalar" or "≥4 distinct eigenvalues" (it is four multiplicity matrices, ≤ 21 eigenvalues); the factor 83 used without specifying path (c) \+ alignment; or 0.091847 called derived. |
| **G-Source** | Mathematical | A nonzero A₅-invariant linear ĉ\_θ asserted when dark energy has no singlet; the single-mode result (path a) stated without the kinetic A₅-invariance hypothesis (\[K, R(g)\] \= 0\) or with 1/Z\_ss in place of the Schur complement when A₅ is broken; or the single-mode ν\_s normalization dropped (with ν\_s² \= v\_sᵀv\_s and G\_s \= sᵀG s, **not** ν\_s² \= v\_sᵀG⁻¹v\_s, which double-divides — the v1.6 error); or the singlet holonomy written U\_s \= V\_s rather than the correct gate U\_s \= V\_s \= **1** (U\_s \= V\_s \= −1 is also equal yet kills the invariant singlet). |
| **G-Outer-Math** | Mathematical | Λ²V₄ ≠ 3 ⊕ 3′ asserted (it is a character identity, GC27); the Hodge ±-swap under odd permutations denied (GC29); or baryon \= 3 ⊕ 3′ asserted as *uniquely selected* without the σ-stability hypothesis (A₅ alone leaves {2·3, 3 ⊕ 3′, 2·3′}). |
| **G-Outer-Physical** | Theoretical | F34.OUT-Math (a DERIVED-CONDITIONAL representation statement) presented as a physical derivation — the identification of the orientation-reversing σ with a Z-Spin symmetry is OPEN; or "favours 3 ⊕ 3′" justified by 6 \= 3 × 2 alone. |
| **G-SuscRank** | Mathematical | the susceptibility's effective mode count equated with the full flux rank dim V rather than dim V^G (F34.SR, GC30); or the m \> 1 invariant block reduced to a scalar without computing Z|\_{V^G}. |
| **G-Generic** | Consistency | The single-mode branch (a) called "generic" — the singlet's location (baryon vs DE) is open, so no branch is generic. |
| **G-Carrier** | Mathematical | M₄ × Σ₂ claimed the *unique* carrier without a minimality/completeness principle (degree counting gives dim ≥ 6 only); or six observable spacetime dimensions asserted. |
| **G-Charge** | Meta / matching | g₆ used as the continuum coupling without Z\_match; Z\_match placed in the numerator of Z; e₆ back-solved from observed ρ\_Λ. |
| **G-Torsion** | Mathematical | An even-dimensional-vanishing argument is re-used (category error); or the scale claimed from a determinant lying outside {a ln2 \+ b ln3}. |
| **G-Sym** | Consistency | ω\_KV (= √2) conflated with arg λ\* (= 2.2592). |

Layering: **G-A1, G-Flux, G-Torsion** are theoretical-collapse gates; **G-A2, G-Metric, G-Sym** are consistency/computation gates; **G-Charge** is the meta / anti-numerology gate.

---

# §10. Outlook

**Thermal history (moved from v1.0 §F34.7).** The dynamical evolution of ρ\_Λ is the Klinkhamer–Volovik q-theory with c\_KV \= 1/8 and the freeze-out kernel ρ̇\_V \= −Γ\_Y(ρ\_V − ρ\_V,0), where Γ\_Y is the **Y-sector thermal** correlator (the SM plasma thermalizes), *not* the Z-Goldstone — so the apparent ZS-M43 No-Thermal-Transport conflict does not arise (M43 retires only the unitary Z-Goldstone η/s). This is a *consequence* of the framework, not an input to the charge-unit reduction, and is recorded here as context.

**A pre-registered programme to close the gates.**

1. **G-Metric (metric identification):** derive the internal Hodge metric as the parent-action kinetic Hessian δ²S\_parent \= ∫\_Σ₂ δω₂ ∧ ⋆\_{g\_Hess} δω₂ and check g\_Hess \= g\_Θ \= |dz|²/Im τ (Area \= 1). Equality lifts F34.M3 to DERIVED; proportionality g\_Hess \= α g\_Θ exposes α as a new normalization gate.  
2. **Baryon embedding \+ outer automorphism (decides the branch).** Construct the actual projectors, not the decomposition: build P\_c (CDM), P\_b (baryon), P\_Λ \= I − P\_b − P\_c on V₁₁ ⊗ V₁₁\* (e.g. via the central projectors P\_ρ \= (d\_ρ/60) Σ\_g χ\_ρ(g)‾ R(g) plus matrix-unit projectors within each isotypic block), verify P\_i² \= P\_i \= P\_i†, P\_b P\_c \= 0, \[P\_b, R(g)\] \= \[P\_c, R(g)\] \= 0, and read the multiplicities from χ\_Λ(g) \= Tr(P\_Λ R(g)). This decides the singlet's location (F34.SEL). F34.BIV already realizes the selecting symmetry geometrically (the Hodge ±-swap of Λ²V₄, GC29); what remains (G-Outer-Physical) is to identify that orientation-reversing involution with a *physical* Z-Spin symmetry and prove σ P\_b σ⁻¹ \= P\_b — the candidates to test are seam-orientation reversal, J\_Z parity, a register automorphism, and a CPT-related exchange; success upgrades G-Outer-Physical from OPEN to DERIVED, completing the bridge to F34.BIV.  
3. **Single-mode reduction of path (a) — the efficient route.** If step 2 leaves the singlet in dark energy and K is A₅-invariant, the susceptibility is the single mode of §7 and, by F34.SR, the **83-dimensional flux/source realization** reduces to **five one-dimensional objects** — no 83-dimensional centrality required (the **independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates still remain**): (i) the rank-1 singlet projector P\_s \= (1/60) Σ\_g R\_Λ(g); (ii) the singlet Hessian norm G\_s \= τ(P\_s K\_Hess P\_s)/τ(P\_s) from the parent Hessian projected to the singlet (needing only \[P\_s, K\_Hess\] \= 0 and G\_s \> 0, not full centrality); (iii) the primitive integral singlet v\_s \= (Σ\_g R(g) v)/gcd, with lattice norm ν\_s² \= v\_sᵀv\_s and quadratic form q\_s \= v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s (the single-mode version of the 121 / F-A24.9 problem) — bundled with Z\_match into I\_s; (iv) the singlet holonomy (U\_s, V\_s) \= (P\_s U\_Λ P\_s, P\_s V\_Λ P\_s), requiring the gate **U\_s \= V\_s \= 1** (r\_singlet \= 1, not r\_flux \= 83; U\_s \= V\_s \= −1 is equal yet kills the singlet); (v) the singlet nucleation Q\_s \= Q\_source P\_s, whose Smith normal form d\_s decides primitive one-unit nucleation. Full 83-dimensional centrality (the double-commutant test below) and the factor 83 are needed **only in path (c)**. A key simplification, to be proved in ZS-F35, decouples this route from step 2: since {baryon \+ dark energy} carries **exactly one** singlet and any singlet-free A₅-equivariant baryon projector satisfies P\_s P\_b \= 0 (hence P\_s P\_Λ \= P\_s), the unique dark-energy singlet projector P\_s — and therefore I\_s — is **independent of the residual ℂP³ multiplicity-line choice** in P\_b (a *Baryon-Embedding Independence* statement). I\_s can thus be computed without first closing P\_b. **These computations are deferred to ZS-F35** (see below); F34 terminates with the reduction in place.  
4. **Path (c) only — full centrality.** Since the A₅ commutant is 117-dimensional, A₅ alone cannot centralize K; either enlarge the symmetry to G\_Λ \= Aut(A\_face, P\_b, P\_c, τ, Q\_source) and test End\_{G\_Λ}(H\_Λ) \= ℂI (a double-commutant test, strictly stronger than A₅-invariance), or compute the full parent-Hessian K\_{ab}, restrict to P\_Λ, extract the multiplicity matrices K\_ρ, and measure Δ\_cent \= ‖P\_Λ K P\_Λ − k̄ P\_Λ‖\_F / ‖P\_Λ K P\_Λ‖\_F (centrality iff Δ\_cent \= 0; isotypic-scalar gives the four-block χ₋ \= (1/4π²) Σ\_ρ k\_ρ⁻¹‖c\_ρ‖²; generic keeps the full matrix form).  
5. **G-Carrier:** state and justify a Minimal-Carrier / Corpus-Completeness principle to upgrade M₄ × Σ₂ from minimal to unique.  
6. **The two follow-on papers (pre-registered split).** The residual quantities have *different logical characters* — P\_b is a representation/projector-selection problem, I\_s is a dimensionless zero-momentum matching problem, and e₆ is a dimensionful UV-charge problem that (per F33's Charge-Unit Obstruction) cannot be derived without a new dimensionful input — so they are split across two papers rather than forced into one. **ZS-F35** (*The Universal Exact-A₅ Singlet Lift*) closes the dimensionless and lattice content: it proves the **Multiplicity-Line No-Go** (A₅ \+ σ fix the type 3 ⊕ 3′ but leave a ℂP³ projector family), the **Baryon-Embedding Independence Theorem** (P\_s P\_b \= 0, P\_s P\_Λ \= P\_s), a direct **physical singlet stiffness** Z\_s^{phys} := δ²Γ\_EFT/δF\_s δF\_s|\_{p=0} \= V\_Σ G\_s/(Z\_match g\_reg²) bundling {V\_Σ, Z\_match, G\_s} into one EFT coefficient so that χ₋^{(s)} \= e\_s²/(4π² Z\_s^{phys}) with e\_s \= e₆ ν\_s, the **primitive singlet lift** (ν\_s, U\_s \= V\_s \= 1, d\_s \= gcd(Q\_source v\_s)), and an optional parent-Hessian spectral selection of the actual P\_b (with the action-level justification that the *minimal* Hessian mode is the baryon, not a value-fitted eigenvector); it may also include an **Approximate-Symmetry Stability Theorem** showing the single mode is *second*\-order stable under weak kinetic A₅-breaking, (Z⁻¹)\_ss \= 1/(Z\_s − ε² B D⁻¹ B†) ⟹ δχ\_s/χ\_s \= O(ε²). **ZS-F36** (*The Primitive Membrane Charge and the Absolute Z-Spin Vacuum Scale*) then closes the sole dimensionful unknown e₆ from a *pre-registered* UV completion — either an explicit wrapped-brane charge e₆ \= μ₄ (with flux quantization, tadpole/global-anomaly cancellation) or dimensional transmutation e₆ \= c\_e Λ₋² from a specified odd gauge group G₋ (matter content, b₋, M\_UV, and c\_e all fixed *before* computing, to avoid numerology). Only after F36 may the absolute scale be claimed.

---

# §11. Conclusion

ZS-F34 has been through seven external reviews, each catching the previous version's over-claim. v1.1 named three gates; v1.2 claimed to close two; v1.3 retracted those; v1.4 corrected the centrality and carrier errors; v1.5 corrected the A₅ representation theory and computed a source trichotomy; v1.6 split off the outer-automorphism selection and the single-mode reduction; **v1.7 (this terminal version) fixes one real formula error and places two general theorems at the front.** The version-by-version growth was not endless polishing but the steady addition of load-bearing claims, each bringing a new verification target; v1.7 adds the last two and stops.

**Two general theorems.** (i) **F34.BIV (Icosahedral Bivector Selection).** The exterior square of the standard 4-dimensional A₅-module is Λ²V₄ \= **3 ⊕ 3′** (character, PROVEN); it is the 6-dimensional S₅-irreducible, and the two triplets are the Hodge self-dual / anti-self-dual sectors, *swapped* by an orientation-reversing odd permutation. This **realizes** v1.6's outer automorphism geometrically — 3 ↔ 3′ is self-dual ↔ anti-self-dual under orientation reversal — and is cross-checked by the known T₁ ⊕ T₂ decomposition of the 6-dimensional crystallographic icosahedral representation. Conditional on identifying the corpus rank-6 Y/baryon carrier with Λ²V₄, the module 3 ⊕ 3′ is selected (F34.OUT-Math, DERIVED-CONDITIONAL); the physical identity of the orientation-reversing symmetry stays OPEN (G-Outer-Physical). (ii) **F34.SR (Finite-Symmetry Susceptibility-Rank).** For a G-equivariant kinetic operator and a source in V^G, χ \= (1/4π²) c†(Z|\_{V^G})⁻¹c, so the effective mode count is dim V^G, not the full flux rank. The single-mode dark-energy result and the m×m block case are corollaries; the "factor 83" was never the right multiplicity for an invariant source. This is a statement about any finite-symmetry multi-four-form theory, valid outside Z-Spin.

**One error fixed.** The single-mode susceptibility is χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) with ν\_s² \= v\_sᵀv\_s (lattice norm) and G\_s \= sᵀG s (Hessian norm), since q\_s \= v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s already; v1.6 divided by G\_s twice. The three single-mode unknowns bundle into one basis-independent **Singlet Response Invariant** I\_s \= Z\_match v\_sᵀG⁻¹v\_s.

**The terminus.** The robust deliverable is the master form χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² ĉ\_θᵀ G⁻¹ ĉ\_θ; F34.SR fixes its effective rank at dim V^G, F34.BIV selects the rank-6 carrier, and the exact-A₅ branch reduces to I\_s plus the **independent** G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates. Single-mode is **one of three branches**, not generic — the singlet's location is open. The actual P\_b, I\_s, and e₆ are deferred to **ZS-F35** (*The Exact-A₅ Singlet Lift and the Primitive Dark-Energy Charge*). The honest contribution of v1.7 is the reframing of F34 from a conditional internal coefficient into a *symmetry-reduction theory of multi-top-form vacuum susceptibility* — neither a forced closure nor a No-Go, consistent with the corpus's standing caution that internal iteration converges to honesty, not to closure. **F34 terminates here.** (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

---

# Acknowledgements & Code Availability

Seven external reviews have shaped this paper. v1.1 reframed v1.0's over-claims as three gates; v1.2 claimed to close two; v1.3 retracted that (Koenigs non sequitur; hidden 121); v1.4 corrected the centrality and carrier errors and introduced an A₅ analysis; v1.5 corrected that analysis (Schur is four *multiplicity matrices*, commutant 117, not four scalars; the 83-decomposition is baryon-conditional; Z\_match was inverted) and computed a source trichotomy instead of a No-Go; v1.6 corrected three v1.5 over-reaches (singlet-selection only *excludes* 1 ⊕ 5 and needs A₅-equivariant projectors; the single-mode reduction needs the kinetic operator A₅-invariant; the singlet normalization ν\_s is not fixed by A₅) and proposed an outer-automorphism selection plus a single-mode reduction. A **seventh** review found one real formula error — the ν\_s²/G\_s double-counting (v\_sᵀG⁻¹v\_s already equals ν\_s²/G\_s) — fixed here, and recommended terminating F34; a parallel deep exploration showed the result's value is raised most by stating two general theorems rather than closing another gate. v1.7 does both. The two theorems are: the **Icosahedral Bivector Selection Theorem** (F34.BIV — Λ²V₄ \= 3 ⊕ 3′, the two triplets being the Hodge self-dual/anti-self-dual sectors swapped by an orientation-reversing odd permutation, which *geometrizes* the outer automorphism; the carrier identification is DERIVED-CONDITIONAL and the physical σ stays OPEN), and the **Finite-Symmetry Susceptibility-Rank Theorem** (F34.SR — for G-equivariant Z \> 0 and source c ∈ V^G, χ \= (1/4π²) c†(Z|\_{V^G})⁻¹c, so N\_eff \= dim V^G, not the full flux rank; valid for any finite-symmetry multi-four-form theory). The single-mode unknowns are bundled into the basis-independent Singlet Response Invariant I\_s \= Z\_match v\_sᵀG⁻¹v\_s. Two suites accompany the paper: zs\_f34\_verify\_v1\_1.py (23/23, arithmetic and the v1.1 regressions) and zs\_f34\_verify\_v1\_8.py (32/32, GATE-DECOMPOSITION-v5 — arithmetic, counterexample, and model-instantiation checks, **not** a closure certificate), which keeps the v5 checks (rank-6 enumeration and singlet counts, the character-level outer automorphism, the explicit A₅ 5-point representation, the Schur-complement mixing, and — now corrected — the single-mode normalization with ν\_s² \= v\_sᵀv\_s and G\_s \= sᵀG s) and adds GC27–GC32: the Λ²(4) \= 3 ⊕ 3′ exterior-square character (GC27), its irreducibility as the 6-dim S₅ rep (GC28), the even-commutes/odd-anticommutes Hodge-star check that realizes σ (GC29), the F34.SR invariant-block reduction at dim V^G \= 2 (GC30), the invariance of the single mode under non-singlet kinetic changes (GC31), and the robust ν\_s²/G\_s factorization over many A₅-invariant metrics (GC32). **This is the terminal version of ZS-F34; the residual computations are deferred to ZS-F35.** This work used Anthropic's Claude; the author assumes responsibility, including for errors caught only on later review.

---

# Appendix A. Numerical Regressions (v1.1)

All from zs\_f34\_verify\_v1\_1.py, mpmath 50-digit, locked inputs and standard constants only. (Tags **AC** are this suite; tags **GC** cited in §2.3/§4.3/§6.3/§7 are the gate-decomposition suite zs\_f34\_verify\_v1\_8.py, 32/32 — arithmetic, counterexample, and model-instantiation checks.)

| Tag | Quantity | Value |
| ----- | ----- | ----- |
| AC4 | z\* \= i^{z\*} | 0.4382829367 \+ 0.3605924719 i |
| AC5 | |λ\*| (|λ\*|² \= 0.794796) | 0.8915135658 |
| AC6 | **κ\_λ** \= −ln|λ\*| (loxodromic) | 0.1148346250 |
| AC7 | ω \= arg λ\* | 2.2592495539 |
| AC9 | Koenigs τ \= (ω \+ i κ\_λ)/2π | 0.35957 \+ 0.018276 i |
| AC10 | theta-line c₁ \= ∫ω₂ \= 1 (metric-independent) | 1 |
| AC11 | **F34.M1**: V\_Σ(c\_Σ=2) \= V\_Σ(1)/4 (area not fixed) | 0.346487 \= 1.385949/4 |
| AC12 | V\_Σ|\_{c\_Σ=1} \= 1/(2π κ\_λ) | 1.385949 |
| AC13 | anti-numerology vs 2 ln 2 \= 1.386294 | rel 0.000249 (distinct) |
| AC14 | **correction**: 2D even seam-odd torsion ln T | ln 4 \= 1.386 (≠ 0\) |
| AC15 | lattice no-go: 8.190 ∈ {a ln2 \+ b ln3}? | None (closed-negative) |
| AC16 | g\_reg² \= 6**A**/**Q** \= 210/4807 (κ\_reg²) | 0.04368629 |
| AC17 | C\_M^sp \= 11 ln2 \+ ln3 (Higgs VEV, ≠ g₆) | 8.7232313 |
| AC19 | Ω\_Λ \= τ(P\_Λ) \= 83/121 (continuous trace; 83 \> 11\) | 0.68595 |
| AC21 | general **c**\_θ^T Z⁻¹ **c**\_θ \= 83 (diagonal-equal only) | 83 |
| AC22 | **superseded** χ₋/e₆² \= 83 g\_reg² κ\_λ/(2π) \[v1.1 Koenigs area 2π κ\_λ\] | 0.066270 |
| AC23 | ρ\_Λ,Z / χ₋ \= ω²/2 | 2.5521043 |

*AC22 is the v1.1 regression value, computed with the retracted Koenigs area 2π κ\_λ (V\_Σ \= 1.385949). The v1.3 metric is the principal polarization (Area \= 1, V\_Σ \= 1), giving χ₋/e₆² \= 83 g\_reg²/(4π²) \= **0.091847** (gate check GC11); the two differ by the factor 2π κ\_λ \= 0.7215.*

**REPORTED (excluded):** e₆ for ρ\_obs ≈ (3.219 meV)² (principal-polarization coefficient; the v1.1-table value used (3.49 meV)²).

---

# Appendix B. Cross-Version Consistency Audit (v1.7)

| Upstream object | Used as | v1.1 verdict |
| ----- | ----- | ----- |
| ZS-F32 ρ\_Λ,Z \= ½χ₋ω² | §7 link | PASS (AC8, AC23) |
| ZS-F33.2B Koenigs τ, theta-line c₁ \= 1 | §3, §4 (metric-independent normalization) | PASS (AC9, AC10) |
| ZS-F33.2B Computation ET (2D seam-odd torsion ln 4\) | §5 (retracts even-dim No-Go) | PASS (AC14) |
| ZS-F33.5 / A28 lattice no-go | §5 (closes scale route) | PASS (AC15) |
| ZS-M6 g\_Γ² \= dim·κ\_reg² | §5 (register coupling) | PASS, matching OPEN (AC16, OG2) |
| ZS-S4 C\_M^sp | §5 (kept distinct) | PASS (AC17) |
| ZS-A17 Spin–Metric No-Go | §2 (KK not licensed) | PASS (softened wording) |
| ZS-A24 II₁ corner, τ(P\_Λ) \= 83/121 | §6 (83 is a trace) | PASS (AC19) |
| ZS-A29 rank-83 kinematic precursor | §6 (G2 OPEN) | corrected: v1.0 "proves free" RETRACTED |
| ZS-A30 one-quantum-per-face | §6 (n\_i \= 1\) | DERIVED-CONDITIONAL (carried) |
| ZS-M43 No-Thermal-Transport | §10 (Γ\_Y on Y, not Z) | PASS (context only) |

No upstream result is overturned; v1.0's three overclaims (unique metric, A29 "proves," even-dim No-Go) are corrected to match upstream status.

---

# References

\[1\] R. Bousso and J. Polchinski, *Quantization of four-form fluxes and dynamical neutralization of the cosmological constant*, JHEP **06**, 006 (2000), arXiv:hep-th/0004134.  
\[2\] J. D. Brown and C. Teitelboim, Nucl. Phys. B **297**, 787 (1988); Phys. Lett. B **195**, 177 (1987).  
\[3\] D. B. Ray and I. M. Singer, *R-torsion and the Laplacian on Riemannian manifolds*, Adv. Math. **7**, 145 (1971) (triviality for closed even-dimensional **unitary** complexes).  
\[4\] J. Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton Univ. Press, 2006\) — Koenigs linearization; ℂ\*/⟨λ\*⟩ as an Ecalle–Koenigs / elliptic curve.  
\[5\] D. Quillen, Funct. Anal. Appl. **19**, 31 (1985) (determinant line, theta line bundle, c₁ \= 1); D. Mumford, *Tata Lectures on Theta I* (Birkhäuser, 1983\) (theta divisor, degree 1); J.-M. Bismut, H. Gillet, and C. Soulé, Commun. Math. Phys. **115**, 49 & 79 (1988) (Quillen metric).  
\[6\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Commun. Math. Phys. **332**, 535 (2014), arXiv:1201.0290 (BV–BFV state-sum).  
\[7\] F. R. Klinkhamer and G. E. Volovik, Phys. Rev. D **80**, 083001 (2009), arXiv:0905.1919; Phys. Rev. D **77**, 085015 (2008), arXiv:0711.3170.  
\[8\] Planck Collaboration, N. Aghanim *et al.*, Astron. Astrophys. **641**, A6 (2020), arXiv:1807.06209.

\[ZS-F32\] K. Kang, *The Continuous-Core Operator Closure and the ½χ₋ω² Reduction of B3*, ZS-F32 (Z-Spin Cosmology Collaboration, 2026).  
\[ZS-F33\] K. Kang, *The Conditional UV Reduction of the Z-Spin Odd Three-Form … and the Charge-Unit Obstruction*, ZS-F33 v1.8 (2026).  
\[ZS-M1\] K. Kang, *i-Tetration, the Fixed Point z\*, and the Leaky Wilson Loop*, ZS-M1 (2026).  
\[ZS-M6\] K. Kang, *Block-Laplacian Spectral Verification; the Dimensional Coupling Norm Theorem*, ZS-M6 (2026).  
\[ZS-S4\] K. Kang, *Y-Sector Spectral VEV: the Factorized Determinant Theorem*, ZS-S4 (2026).  
\[ZS-A17\] K. Kang, *Macro-Holonomy and Spin-Structure Selection: the Spin–Metric Independence No-Go*, ZS-A17 (2026).  
\[ZS-A24\] K. Kang, *Dimension-Weighted Mediator Semigroups and Their Spin-Graded Continuous-Core Lift*, ZS-A24 (2026).  
\[ZS-A28\] K. Kang, *The Odd Spectral Invariant: the Rank/Energy Separation and the Lattice No-Go (absolute scale OPEN)*, ZS-A28 (2026).  
\[ZS-A29\] K. Kang, *Dust and Vacuum from Measure/Form Actions*, ZS-A29 (2026).  
\[ZS-A30\] K. Kang, *The Coincidence Wall and Its Classified Escapes (one quantum per face; the (6, 32, 83\) partition)*, ZS-A30 (2026).  
\[ZS-M43\] K. Kang, *The Z-Goldstone Is a Coherent Superfluid (the No-Thermal-Transport Lemma)*, ZS-M43 (2026).  
\[ZS-F5\] K. Kang, *Gauge Symmetry Constraint: Q \= 11, (Z, X, Y) \= (2, 3, 6\)*, ZS-F5 (2026).  
\[ZS-F18\] K. Kang, *The Five-Axiom Meta-Structure and the Sector Decomposition*, ZS-F18 (2026).

---

# Version History

**v1.8 (June 2026\) — TERMINAL (final-clean):** **Eighth-review pre-publication pass — no new theorems.** An eighth review confirmed the v1.7 content is terminal (32/32) and flagged only publication-clean items, all applied here. **(typesetting)** the \\;=\\; thick-space artifacts are simplified to plain \= (they rendered as ;=; in some viewers); the source LaTeX for Z|\_{V^G}, N\_{\\rm eff}, \\hat{\\mathbf c}\_\\theta etc. was already correct (the \*\-for-\_ seen in rendering is a markdown-renderer effect, not a source bug). **(F34.SR precision)** N\_eff is sharpened to N\_eff \= dim S\_src ≤ dim V^G for an admissible source space S\_src ⊆ V^G, with equality when the admissible sources span V^G (in F34's exact-A₅ branch dim V^{A₅} \= 1, so the conclusion is unchanged). **(F34.BIV signature caveat)** F34.BIV is Euclidean (⋆² \= \+1, a real self-dual/anti-self-dual split); the corpus carrier Λ²(ℝ^{1,3}) is Lorentzian (⋆² \= −1 on real 2-forms, ±i eigenspaces after complexification), so the identification needs complexification or an explicit signature-changing intertwiner — added as part of the carrier bridge, not a real-orthogonal identity. **(F34.BIV scope)** recorded that F34.BIV selects the *representation type* 3 ⊕ 3′, while the actual baryon projector P\_b retains a residual ℂP³ multiplicity-line freedom; fixing P\_b is a dynamical (parent-Hessian) question deferred to ZS-F35. **(Outlook sharpened)** §10 now splits the follow-on work into **ZS-F35** (dimensionless/lattice: Multiplicity-Line No-Go, Baryon-Embedding Independence P\_s P\_b \= 0 so I\_s is independent of the multiplicity line, physical singlet stiffness Z\_s^{phys}, primitive singlet lift, optional approximate-symmetry O(ε²) stability) and **ZS-F36** (the sole dimensionful e₆ from a pre-registered UV completion). **(script)** zs\_f34\_verify\_v1\_8.py docstring updated to v1.8/GATE-DECOMPOSITION-v5 and the OG3 note changed from "CLOSURE PROGRAMME"/"U\_s \= V\_s" to "REDUCTION"/"(U\_s, V\_s) \= 1"; the 32/32 verification is unchanged. F34 remains terminal.

**v1.7 (June 2026\) — TERMINAL:** **Seventh-review fix \+ two general theorems.** A seventh review found **one real formula error** and recommended terminating F34; a parallel deep exploration showed the value is raised most by stating two general theorems. **(error fixed)** the single-mode susceptibility is χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) with **ν\_s² \= v\_sᵀv\_s** (lattice norm) and **G\_s \= sᵀG s** (Hessian norm), since q\_s \= v\_sᵀG⁻¹v\_s \= ν\_s²/G\_s already — v1.6 wrongly set ν\_s² \= v\_sᵀG⁻¹v\_s and divided by G\_s again (double-count); GC23 rebuilt on an A₅-invariant SPD metric, GC32 verifies the factorization over many such metrics. **(F34.BIV — new general theorem)** Λ²(standard 4-dim A₅-module) \= **3 ⊕ 3′** (character, GC27); it is the 6-dim S₅-irreducible (GC28); the two triplets are the Hodge self-dual/anti-self-dual sectors, and even permutations commute with the Hodge star (preserve them) while orientation-reversing odd permutations anticommute (swap 3 ↔ 3′) (GC29) — this **geometrizes** v1.6's outer automorphism. Cross-checked by the T₁ ⊕ T₂ decomposition of the 6-dim crystallographic icosahedral representation. Math PROVEN; carrier identification DERIVED-CONDITIONAL. **(F34.SR — new general theorem)** for G-equivariant Z \> 0 and source c ∈ V^G, χ \= (1/4π²) c†(Z|\_{V^G})⁻¹c, so **N\_eff \= dim V^G**, not the full flux rank (GC30, GC31); corollaries dim V^G \= 0/1/m. Valid for any finite-symmetry multi-four-form theory; the "factor 83" was never the right multiplicity for an invariant source. **(F34.OUT split)** v1.6's single HYPOTHESIS-strong tag is separated into **F34.OUT-Math** (σ-stable selection, DERIVED-CONDITIONAL) and **G-Outer-Physical** (σ \= physical Z-Spin symmetry, OPEN); HYPOTHESIS-strong added to the legend. **(I\_s)** the single-mode unknowns bundle into the basis-independent **Singlet Response Invariant** I\_s \= Z\_match v\_sᵀG⁻¹v\_s, χ₋ \= (g\_reg² e₆²/4π² V\_Σ) I\_s. **(branch ratio)** χ\_83/χ\_singlet \= 83/q\_s (= 83 at q\_s \= 1), a conditional discriminator. **(wording)** "single-mode closure" → "single-mode reduction"; "the entire dark-energy coefficient reduces to five objects" → "the 83-dimensional flux/source realization reduces to five 1-dim objects {P\_s, G\_s, ν\_s, (U\_s, V\_s) \= 1, Q\_s}; the independent G-Metric (V\_Σ) and G-Charge (Z\_match, e₆) gates remain"; the singlet-holonomy gate sharpened from U\_s \= V\_s to **U\_s \= V\_s \= 1**. **(scope)** the residual computations (P\_b, I\_s, e₆) are deferred to **ZS-F35**; no new closure theorem is added. Added zs\_f34\_verify\_v1\_8.py (32/32). Honest framing: the contribution is a **symmetry-reduction theory of multi-top-form vacuum susceptibility** — a *reduction*, not a closure. **F34 terminates here.**

**v1.6 (June 2026):** **Sixth-review correction: outer-automorphism selection \+ single-mode reduction** (v1.6 called this "single-mode closure"; renamed "reduction" in v1.7). A sixth review found three places where v1.5 over-reached, all corrected, plus two new results. **(F34.SEL — selection not unique)** v1.5 said singlet-selection "favours 3 ⊕ 3′." The singlet-free rank-6 A₅-modules are **{2·3, 3 ⊕ 3′, 2·3′}** (DE singlet counts 0,1,1,1 for {1⊕5, 2·3, 3⊕3′, 2·3′}; GC17, GC18), so F34.SEL only **excludes 1 ⊕ 5** and additionally requires P\_b, P\_c to be mutually orthogonal **A₅-equivariant** projectors (else the singlet has no representation-theoretic location and one is already in path c). **(F34.OUT — new, outer-automorphism selection)** σ ∈ Out(A₅) ≅ ℤ₂ (odd permutation) swaps the two 5-cycle classes, hence **σ: 3 ↔ 3′, fixing 1, 4, 5** (GC19a); among the singlet-free candidates 2·3 ↔ 2·3′ while only **3 ⊕ 3′ is σ-stable** (GC19b), so A₅ \+ σ \+ no-baryon-singlet **uniquely** select baryon \= 3 ⊕ 3′. HYPOTHESIS-strong, pending identification of σ with a physical symmetry (seam orientation / J\_Z parity / register automorphism / CPT exchange). **(F34.A5-2 — single-mode made precise)** the single-mode χ₋ \= e₆²/(4π² Z\_s) holds only when DE keeps the singlet **and** \[K, R(g)\] \= 0 (singlet decouples, P\_s K (I−P\_s) \= 0, GC21); if A₅ is broken a singlet source mixes via the **Schur complement** (Z⁻¹)\_ss \= 1/(Z\_ss − B D⁻¹ B†) (GC22). The singlet **direction** is fixed but its **normalization ν\_s is not**, so the susceptibility is χ₋ \= (Z\_match g\_reg²/4π² V\_Σ) e₆² (ν\_s²/G\_s) with ν\_s² \= v\_sᵀ G⁻¹ v\_s *(this definition double-counts G\_s and is corrected in v1.7: ν\_s² \= v\_sᵀv\_s, G\_s \= sᵀG s)* — the 121/F-A24.9 problem persists in the single-mode branch as the one number ν\_s (GC23). **(single-mode closure, new)** path (a) reduces the 83-dim seven-gate problem to **five 1-dim objects** {P\_s, G\_s, ν\_s, U\_s \= V\_s, Q\_s}; full 83-centrality and the factor 83 are needed only in path (c) (GC24, OG3). **(wording)** "generically single-mode" → "single-mode branch (one of three)"; "Z\_match in the denominator" sharpened to "denominator of Z, numerator of χ₋." **(LaTeX)** set-brace escaping in Σ\_{ρ∈{3,3′,4,5}}, thin-space and bold-in-math artifacts cleaned. Added zs\_f34\_gates\_v5\_verify.py (26/26). Honest framing: the contribution is the **outer-automorphism selection** of the baryon module and the **single-mode closure reduction** — neither a forced closure nor a No-Go.

**v1.5 (June 2026):** **Fifth-review correction: A₅ representation theory \+ Z\_match; source paths computed (not a No-Go)** (the "favours 3 ⊕ 3′" wording and the single-mode conditions later refined in v1.6). **(F34.M4(c) — Schur corrected)** an A₅-invariant K \= ⊕\_ρ (I\_{d\_ρ} ⊗ K\_ρ) has **multiplicity matrices** K₃,K₃′ ∈ M₄, K₄ ∈ M₆, K₅ ∈ M₇; commutant **dim 117**, up to **21** eigenvalues (GC7, GC8) — correcting v1.4's "block-scalar, ≥4 eigenvalues." **(F34.A5-1 — 83 conditional)** 83 \= 4·3 ⊕ 4·3′ ⊕ 6·4 ⊕ 7·5 holds only for the illustrative baryon 6 \= 1⊕5; End(V₁₁), F\_TI character-computed (GC2, GC3). **(F34.SEL, F34.A5-2 — source paths)** a nonzero A₅-invariant θ-coupling exists iff DE keeps the lone singlet; trichotomy (a) single-mode / (b) spurion / (c) factor-83 under alignment; 0.091847 lives in path (c). **(F34.6 — Z\_match corrected)** Z \= (V\_Σ/Z\_match g\_reg²) G, Z\_match in the denominator (v1.4 had it inverted); c\_θ \= e₆ ĉ\_θ. **(F34.M4(b))** "up to 121" removed (full index OPEN). Added zs\_f34\_gates\_v4\_verify.py (16/16).

**v1.4 (June 2026):** **Fourth-review correction: kinetic centrality OPEN \+ carrier minimality** (the A₅ Schur claim and the 83-decomposition later corrected in v1.5). **(F34.M4(c) — centrality OPEN)** v1.3 wrongly claimed kinetic centrality follows from the uniform face trace. It does not: with q\_a \= |a⟩⟨a|, τ(q\_a K q\_b) \= (1/121)K\_{aa}δ\_{ab}, so orthogonality gives only **diagonality**; the counterexample K \= diag(1, …, 83\) has equal face traces but unequal Z\_{aa}. *Note: v1.4 then over-simplified the A₅ structure to "block-scalar, ≥4 eigenvalues" and treated 83 \= 4·3⊕4·3′⊕6·4⊕7·5 as fixed; v1.5 corrects both (commutant 117; baryon-conditional).* **(F34.1 — minimal carrier)** form-degree counting gives only D\_parent ≥ 6, so M₄ × Σ₂ (4 \+ dim **Z** \= 6\) is the **minimal** carrier, unique only under a Minimal-Carrier / Corpus-Completeness principle; the "not a 6D spacetime" wording is sharpened to "a six-dimensional pseudo-Riemannian total space with four noncompact spacetime dimensions and a compact 2D internal fibre." **(F34.M4(b) — 121 \= integral lattice embedding)** recast from "basis ambiguity": a genuine basis change leaves the quadratic form invariant (computed), so the factor 121 is an integral charge-lattice embedding choice, and F-A24.9 is sharpened to a *trace-preserving integral charge-lattice intertwiner*. **(c\_θ vs Q\_source)** separated. **(F34.M3 — wording)** "closure" → "candidate normalization"; the three levels separated; c₁ \= \[iF/2π\] convention stated. **(arithmetic)** ρ\_Λ,Z corrected 0.234426 → **0.234402**. **(LaTeX/docs)** parent-action spacing fixed; brace artifacts removed; References A24/A29/A30 synced. Added zs\_f34\_gates\_v3\_verify.py (11/11).

**v1.3 (June 2026):** **Third-review correction: principal polarization \+ sub-gate decomposition** (centrality claim and carrier uniqueness later corrected in v1.4). **(F34.M2 RETRACTED)** the v1.2 Koenigs argument is withdrawn as a non sequitur. **(F34.M3, new)** the metric scale is fixed by the **principal polarization** of F33's degree-1 theta line Θ\_Z (Area \= c₁ \= 1 ⇒ V\_Σ \= 1); coefficient **0.066270 → 0.091847**. **(F34.M4, new)** G-Flux decomposed into sub-gates {monodromy, 121-normalization, kinetic centrality, equal charge, Path A}; the v1.2 closure claims withdrawn. **(F34.1)** Y6 given a degree-counting derivation. **(F34.4-NG)** "non-unitary" corrected to "seam-parity-restricted determinant torsion." Added zs\_f34\_gates\_v2\_verify.py (10/10). *Note: v1.3 still wrongly marked kinetic centrality "established" and the carrier "forced"; both corrected in v1.4.*

**v1.2 (June 2026):** Gate-closure update (now partly superseded by v1.3). Claimed G-Metric CLOSED via a Koenigs-canonical metric (F34.M2 — **retracted in v1.3**) and G-Flux REDUCED to ZS-A24/A30, with χ₋ \= 0.066270 · Z\_match · e₆² as DERIVED-CONDITIONAL. The third review found the Koenigs argument a non sequitur and a 121-fold normalization ambiguity in the flux coefficient; see the v1.3 entry. Added zs\_f34\_gates\_verify.py (10/10).

**v1.1 (June 2026):** **Major revision integrating an external peer review (MAJOR REVISION verdict).** Substantive changes: **(notation)** separated the overloaded symbol κ into κ\_λ \= −ln|λ\*| (loxodromic decrement) and κ\_reg² \= **A**/**Q** (register), with g\_reg² \= 6κ\_reg²; **(F34.M1, new NO-GO)** proved that λ\*-invariance fixes the torus complex structure but not the Kähler area (c\_Σ free), so V\_Σ \= 1.385949 is COMPUTED-UNDER-NORMALIZATION (c\_Σ \= 1), not derived, and the corpus theta-line c₁ \= 1 is a metric-independent cohomology condition; **(F34.2, new)** added the parent-action wrapped-brane reduction giving Z\_{ij}, e\_mem \= e₆^(6)∫ω₂, T\_mem^(4) \= T\_4-brane Area(Σ₂), the general susceptibility χ₋ \= (1/4π²) **c**\_θ^T Z⁻¹ **c**\_θ, and the anomaly gates (G-A2); **(F34.4)** demoted the coupling to the register value g\_reg² \= 6**A**/**Q** pending a register→EFT matching Z\_match (OPEN); **(F34.4-NG, RETRACTED)** withdrew the even-dimensional Ray–Singer No-Go as a category error; **(F34.5, demoted to OPEN-GATE)** corrected the b₂ \= 1 → 83 overclaim (83 is the ZS-A24 continuous trace τ(P\_Λ), not 83 fluxes), gave the two Realization paths, and withdrew the "BP gap solved" claim; **(F34.6)** recast χ₋ \= 0.066270 e₆² as a BENCHMARK-COROLLARY; **(F34.8)** recast the residual as a finite UV matching problem; **(structure)** moved the thermal history to the Outlook; softened "KK forbidden" to "KK not licensed". Verification reframed: 23/23 checks PASS, explicitly **not** a certificate of physical closure (zs\_f34\_verify\_v1\_1.py).

**v1.0 (June 2026):** Initial public release (superseded). Established the F33.8D ansatz and computed the Charge-Unit reduction, but overclaimed in three places (unique cylinder metric; rank-83 as 83 independent fluxes; register coupling as the continuum coupling) and contained a Ray–Singer dimension category error — all corrected in v1.1.

(**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.  
