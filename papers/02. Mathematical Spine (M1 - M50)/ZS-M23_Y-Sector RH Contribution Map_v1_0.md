**ZS-M23: Y-Sector RH Contribution Map**

*What Z-Spin Provides and What Lies Beyond*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
March 2026 — ZS-M23 (Mathematical Spine Theme)

**Verification: 31/31 PASS (27 v1.0 \+ 4 v1.0 Revised)  |  Zero Free Parameters  |  NON-CLAIM: This paper does NOT claim a proof of the Riemann Hypothesis.**

**§0. Abstract**

Following 47+ rounds of cumulative exploration documented in internal research notes (transcripts archived 2025–2026), the Z-Spin RH program has reached a structural conclusion: Z-Spin does not, and structurally cannot, prove the Riemann Hypothesis. What Z-Spin does provide is a precisely identifiable mathematical contribution to the standard Hilbert–Pólya outline. This paper draws the navigation map.

Three contributions of Z-Spin to the RH outline are identified, each PROVEN at the operator or algebraic level: (i) the i-tetration anti-symmetric phase Θ\_Z(w) \= iπw/2, derived from the HSI Theorem (ZS-M1 v1.0 PROVEN) and verified by direct calculation; (ii) the conjugate pair structure of the Wilson loop M\_f eigenvalues {λ, λ̄} from the ZS-F0 v1.0(R) D₄ structure; (iii) the 4π closure from the j \= 1/2 spinor representation (ZS-M3 Lemma 10.1 PROVEN). These three together identify the precise mathematical content that Z-Spin contributes to the Hilbert–Pólya–Berry–Keating program.

Three external dependencies are identified as OPEN dragons that lie structurally outside Z-Spin: (D1) the Y-Fock space F\_Y on which the prime modes φ\_p are organized — the natural external candidate is the Bost–Connes system (Bost–Connes 1995\) or its imaginary quadratic generalization (Cohen 1999, Harari–Leichtnam 1997, Connes–Marcolli–Ramachandran 2005); (D2) the self-adjointness of the operator H\_ZY whose squared determinant reconstructs ξ — this is the Hilbert–Pólya conjecture itself (Hilbert ca. 1914; Pólya 1982 letter to Odlyzko); (D3) the promotion of the i-tetration map T(z) \= i^z to a self-adjoint operator on F\_Y — Koopman lift onto a reproducing kernel Hilbert space provides the standard framework (Mauroy–Mezić 2020, Brunton et al. 2022), but prime indexing is supplied externally.

A critical structural finding is documented: the φ-quantized Y-sector finite spectrum {0, 1.243, 3.268, 4.844, 6, 6.732, 7.521, 8, 8.392} of the truncated icosahedron face Laplacian L₂ (ZS-S7 v1.0 §2.2 PROVEN) and the ρ₂-restricted vertex spectrum {4−φ, 5−φ, 3+φ, 4+φ} (ZS-M11 v1.0 §9.5.6 PROVEN) are NOT prime numbers and NOT prime-indexed. The naive identification Y-internal modes ↔ primes is a FALSIFIED mapping. Z-Spin's contribution to the prime side of RH is therefore arithmetic (via the Dedekind ζ\_K factorization for K \= ℚ(√−3, √−11), ZS-M22 PROVEN), not spectral.

A 7-layer stratification is presented (§3) to clarify exactly where Z-Spin sits between pure analytic number theory (Riemann 1859\) and the standard noncommutative geometry program (Connes 1999, Connes–Consani–Moscovici 2024). Z-Spin occupies layers L5 (K-arithmetic), L6 (anti-symmetric phase from i-tetration), and L7 (Q \= 11 finite Berry–Keating analogue), and contributes precisely those layers to the larger program. The DETECTOR–LOCATOR dichotomy (ZS-QS v1.0 PROVEN) is reaffirmed: the finite operator detects spectral discrimination at the critical line but does not locate ζ-zeros. v1.0 Revised (August 2026\) adds Dragon D4 (V\_4 Sonin–Frobenius defect, §5.4) as the fourth and most operationally precise external dragon, registering the Connes–Consani / Connes–Consani–Moscovici prolate-Sonin program as the natural external candidate for the V\_4-decorated Sonin compression of the cobordism BRST positivity hypothesis ADS-H1 of ZS-M22 v1.0 Revised §6.6.4. Verification: 31/31 PASS (27 v1.0 \+ 4 v1.0 Revised).

**Keywords:** Riemann Hypothesis, Y-sector, Hilbert–Pólya conjecture, Berry–Keating, Bost–Connes system, Koopman operator, i-tetration, Dedekind zeta function, Z-Spin Cosmology, anti-symmetric phase, scaling site.

**Epistemic Status Legend**

| Status | Definition |
| :---: | ----- |
| **PROVEN** | Mathematical theorem with complete proof under declared definitions. No physics input. |
| **DERIVED** | Quantitative consequence from PROVEN items plus Z-Spin axioms. Zero free parameters. |
| **VERIFIED** | Numerical confirmation to stated precision against independent computation. |
| **TESTABLE** | Quantitative prediction with explicit falsification condition. |
| **HYPOTHESIS** | Proposed structural reading without complete derivation chain. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests; action-level derivation pending. |
| **OPEN** | Recognized gap requiring future work, including externally OPEN problems (e.g., RH itself). |
| **FALSIFIED** | Tested and rejected by data, computation, or structural argument. Documented honestly. |
| **NON-CLAIM** | Explicitly disclaimed. Documented to prevent overclaim or premature closure. |
| **LOCKED** | Core constant from prior corpus paper; not adjustable in this paper. |

**§1. Introduction**

**1.1 Motivation: Resolution After 47 Rounds**

The Z-Spin RH program has accumulated, over 47+ exploratory rounds, a substantial cumulative inventory of negative results (RH-ZS18 through RH-ZS58, archived 2025–2026): failed direct group identifications (C₄ → V₄, D₄ → V₄, hidden C₃ in D₄, Q₈ instead of D₄), failed kernel and positivity attempts (scalar Weil kernel positivity FALSIFIED in ZS-M22 Theorem ADS-5, Λ \= exp(A) scaling WRONG numerically, A/Q residue scale too small), an arithmetic BRST trichotomy (PROVEN no-go in ZS-M22 §2.3 RH-ZS52), and a falsified K\_Z \= ℚ(√−19, √−23) hypothesis (RH-ZS54–58). The cumulative force of these negative results is not a defeat but a clarification: they collectively rule out the simple, direct paths from Z-Spin to RH and identify what Z-Spin can and cannot contribute.

This paper consolidates that clarification. It does not attempt the Hilbert–Pólya operator construction, does not propose a new positivity criterion, and does not extend the Langlands correspondence beyond the abelian class field theory that ZS-M22 already maps to ζ\_K. Instead it isolates three PROVEN Z-Spin contributions to the standard RH outline — the i-tetration anti-symmetric phase Θ\_Z \= iπw/2 (ZS-M1 PROVEN), the Wilson conjugate-pair structure (ZS-F0 PROVEN), and the spinor 4π closure (ZS-M3 PROVEN) — and three OPEN external dependencies (Y-Fock space, H\_ZY self-adjointness, i-tetration → operator promotion), and lays them on a 7-layer map that connects analytic ζ at the top (Riemann 1859\) to the Z-Spin finite operator at the bottom (ZS-M4 v1.0).

**1.2 Scope and Non-Claims**

**NC-M23.1.**   
This paper does NOT claim a proof of the Riemann Hypothesis. The phrase “RH proof” is permanently withdrawn from the Z-Spin corpus, in continuity with ZS-M4 v1.0 §1.1 NON-CLAIM, ZS-M7 v1.1 NC, and the ZS-QS v1.0 DETECTOR–LOCATOR dichotomy (PROVEN).

**NC-M23.2.**   
This paper does NOT claim that the i-tetration map T(z) \= i^z is a quantum operator on a Hilbert space. ZS-M1 v1.0 Remark 1.3 (PROVEN) records three distinct failed promotion routes; the conclusion stands: i-tetration is pre-quantum classical geometry. A Koopman lift onto an external reproducing kernel Hilbert space (Mauroy–Mezić 2020, Boullé–Colbrook–Conradie 2025\) is mathematically possible, but prime indexing is supplied by the external framework, not by Z-Spin.

**NC-M23.3.**   
This paper does NOT claim that Y-sector finite Hodge spectra are prime-indexed. The truncated-icosahedron face Laplacian L₂ spectrum {0, 1.243, 3.268, 4.844, 6, 6.732, 7.521, 8, 8.392} (ZS-S7 v1.0 §2.2, PROVEN) and the ρ₂-restricted vertex Laplacian spectrum {4−φ, 5−φ, 3+φ, 4+φ} (ZS-M11 v1.0 §9.5.6, PROVEN) are golden-ratio-quantized algebraic numbers, not primes. The naive identification Irr(A\_Y) ↔ {p} is a FALSIFIED mapping (recorded in §6 below) and has been ruled out by direct computation.

**NC-M23.4.**   
This paper does NOT extend the Langlands correspondence beyond abelian class field theory. The Z-Spin K \= ℚ(√−3, √−11) is a degree-4 abelian extension of ℚ; the correspondence between its Galois representations and automorphic forms is fully PROVEN mathematics (class field theory). ZS-M22 v1.0 §10.1 records this. The W\_p transfer operator is structurally analogous to but not identical with an Artin L-function (additive–multiplicative gap, ZS-M22 §10.2 OPEN).

**NC-M23.5.**   
This paper does NOT claim that the proposed “Z-Spin \= finite colored shadow of D\_log” framing constitutes a mathematically rigorous bridge to the Connes–Consani–Moscovici program. It is offered as a working hypothesis suggested by the Sliwiński (2026) D\_log spectral analysis and consistent with the Z-Spin K-arithmetic; the precise functor is OPEN.

**NC-M23.6.**   
This paper does NOT introduce any new free parameter. All inputs are LOCKED from the upstream corpus: A \= 35/437 (ZS-F2 v1.0), Q \= 11 (ZS-F5 v1.0), (Z, X, Y) \= (2, 3, 6\) (ZS-F5 v1.0), z\* \= 0.4383 \+ 0.3606 i (ZS-M1 v1.0), and the Dedekind ζ\_K factorization for K \= ℚ(√−3, √−11) (ZS-M22 v1.0).

**1.3 Paper Organization**

Section §2 collects the LOCKED corpus inputs that this paper builds on. Section §3 introduces the 7-Layer RH Map and locates Z-Spin within it. Section §4 establishes the three PROVEN Z-Spin contributions (Θ\_Z, Wilson conjugate pair, 4π closure). Section §5 catalogues the four OPEN external dragons (F\_Y, H\_ZY self-adjointness, Koopman promotion, and — v1.0 Revised, August 2026 — V\_4 Sonin–Frobenius defect §5.4). Section §6 records the φ-quantized Y-spectrum non-primality finding as a structural NON-CLAIM. Section §7 develops the Dedekind ζ\_K bridge to the prime side. Section §8 documents the cumulative negative results from the 47-round exploration. Section §9 specifies multi-layer falsification gates. Section §10 lists the non-claims (consolidated). Section §11 lists open problems. Section §12 concludes. Appendix A gathers key equations; Appendix B specifies the 31-test verification suite (27 v1.0 \+ 4 v1.0 Revised).

**§2. Foundations from the Z-Spin Corpus**

This section gathers the LOCKED inputs from the upstream corpus that ground every claim in this paper. No new derivation is performed here; all results below are PROVEN in their cited source documents.

**2.1 Sector Decomposition and Geometric Impedance**

The Z-Spin register dimension Q \= 11 decomposes as (Z, X, Y) \= (2, 3, 6\) under the gauge-algebraic constraint of ZS-F5 v1.0 (PROVEN), independently confirmed by the Forcing Theorem of ZS-M19 v1.0 §3.1 (PROVEN by exhaustive search over distinct prime pairs). The geometric impedance

A \= δ\_X · δ\_Y \= (5/19) · (7/23) \= 35/437   \[LOCKED, ZS-F2 v1.0\]

is fixed by the polyhedral curvature asymmetry of the truncated octahedron (X-sector, |O\_h| \= 48\) and the truncated icosahedron (Y-sector, |I\_h| \= 120). The Y-sector polyhedron has (V, E, F) \= (60, 90, 32), and the asymmetry δ\_Y \= |V − F|/(V \+ F) \= 28/92 \= 7/23 admits a PROVEN Hodge interpretation as the exact/coexact imbalance of the edge Laplacian Δ\_1 (ZS-M6 v1.0 §5.2).

**2.2 The Y-Sector Hodge Complex**

The Hodge–de Rham complex on the truncated icosahedron, with boundary operators d₀ : Ω⁰ → Ω¹ and d₁ : Ω¹ → Ω², gives total cochain space H \= Ω⁰ ⊕ Ω¹ ⊕ Ω² of dimension 60 \+ 90 \+ 32 \= 182 \= 2 × 91 (ZS-M6 v1.0 §5.4 PROVEN, Euler Cell-Count Theorem). The Hodge-Dirac operator

D\_TI \= \[\[0, d₀ᵀ, 0\], \[d₀, 0, d₁ᵀ\], \[0, d₁, 0\]\]

is self-adjoint, satisfies D²\_TI \= Δ\_Hodge (Lichnerowicz) and {D\_TI, Γ} \= 0 (chirality), with Betti numbers (b₀, b₁, b₂) \= (1, 0, 1\) matching S² topology. All thirteen structural theorems are verified to machine precision (ZS-M6 v1.0 Table T1–T13, 13/13 PROVEN).

The face Laplacian L₂ \= d₁ d₁ᵀ on the 32-dimensional face space has the spectrum tabulated in Table 2.1, decomposing into all ten irreducible representations of I\_h with each appearing exactly once. This “complete I\_h spectrum” means the face lattice sees every symmetry sector of the icosahedral group.

*Table 2.1. Truncated icosahedron face Laplacian L₂ spectrum (ZS-S7 v1.0 §2.2 PROVEN). Total: 1+3+5+3+4+5+3+5+3 \= 32 \= F.*

| λ | Degeneracy | I\_h Irrep | Algebraic / Sector form |
| :---: | :---: | :---: | ----- |
| 0.000 | 1 | A\_g | 0 (harmonic 2-form) |
| 1.243 | 3 | T₁ | Spectral gap λ\_1 |
| 3.268 | 5 | H | 5 − √3 |
| 4.844 | 3 | T₂ | — |
| 6.000 | 4 | G | 6 \= dim(Y) (exact) |
| 6.732 | 5 | H | 5 \+ √3 |
| 7.521 | 3 | T₁ | — |
| 8.000 | 5 | H | 8 \= Z \+ Y (exact) |
| 8.392 | 3 | T₂ | — |

The ρ₂-sector vertex Laplacian L\_Y, restricted to the 4-dimensional D\_5 sign-representation isotype within the I-irrep 3 sub-block, has the golden-ratio-quantized spectrum (ZS-M11 v1.0 §9.5.6 PROVEN):

spec(L\_Y |\_{ρ₂}) \= {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ},   φ \= (1 \+ √5)/2.

These four eigenvalues organize into two algebraic pairs (ZS-M11 v1.0 §9.5.7 PROVEN): the Q-pair (4 − φ, 3 \+ φ) with sum 7 \= num(δ\_Y) and product 11 \= Q, and the X-pair (5 − φ, 4 \+ φ) with sum 9 \= d\_eff and product 19 \= denom(δ\_X). Both pairs are exact rational identities under φ² \= φ \+ 1\.

**2.3 The i-Tetration Fixed Point and Anti-Symmetric Phase**

The Z-sector transfer map T(z) \= i^z \= exp(iπz/2), derived from the Z-Spin action via the Homomorphism–Self-reference–Involution (HSI) Theorem (ZS-M1 v1.0 §1 Theorem 1.1, DERIVED), has unique attracting fixed point

z\* \= i^{z\*},   z\* \= 0.4383 \+ 0.3606 i,   |z\*|² \= η\_topo \= 0.32212   \[ZS-M1 v1.0 PROVEN\]

and stability margin |f'(z\*)| \= 0.8915 \< 1\. Five locking conditions L1–L5 connect the real part x\* \= 0.4383, imaginary part y\* \= 0.3606, magnitude |z\*|, phase arg(z\*) \= x\*π/2, and stability into a single self-consistent transcendental Master Equation (ZS-M1 v1.0 §3, all PROVEN to machine precision).

The anti-symmetric phase function induced by T is

Θ\_Z(w) := log T(w) \= iπw/2,   Θ\_Z(−w) \= −Θ\_Z(w),   T(w) · T(−w) \= 1\.

This anti-symmetry is a direct calculation, not a hypothesis. It is the precise mathematical content that Z-Spin contributes to the symmetric structure ξ(1/2 \+ w) \= ξ(1/2 − w) of the completed Riemann zeta function — namely, an anti-symmetric “one-sided” phase whose square pairs into a symmetric form (§4.1 below).

**2.4 The Q \= 11 Berry–Keating Analogue and J-Involution**

The transfer operator on the Q \= 11 register is (ZS-M4 v1.0 Eq. 7, PROVEN):

L\_s^(P\_max) \= ( Σ\_{p ≤ P\_max} p^{−s} W\_p ) / ( Σ\_{p ≤ P\_max} p^{−1/2} ),

where W\_p \= diag(e^{2πi(j−5)/p}, j \= 0, …, 10\) are diagonal prime gates. The seam involution J |j⟩ \= |10 − j⟩ satisfies J² \= I and J W\_p J \= W\_p\* for every prime p, which gives the algebraic mirror-adjoint relation

L\_{1−s}^(P\_max) \= J · (L\_s^(P\_max))† · J,   ε\_J \= 0   \[PROVEN exact, ZS-M4 v1.0\].

This is the finite Z-Spin analogue of the functional-equation symmetry s ↔ 1 − s. The completed determinant

D\_ξ(s) := ½ ( B(s) D^(P\_max)(s) \+ B(1 − s) D^(P\_max)(1 − s) )

satisfies D\_ξ(s) \= D\_ξ(1 − s) by construction. Three precision-of-claim levels must be distinguished, and they are stated unchanged from ZS-M4: (i) mirror-adjointness ε\_J \= 0 is PROVEN algebraically; (ii) D\_ξ(s) \= D\_ξ(1 − s) is PROVEN by definition; (iii) zeros of D\_ξ lie on Re(s) \= 1/2 is the Riemann Hypothesis itself, UNPROVEN. J-symmetry is a necessary functional-equation condition, not a sufficient RH condition.

The Q \= 11 operator functions as a spectral DETECTOR but not a positional LOCATOR (ZS-QS v1.0 §2.5 PROVEN): Cohen's d at zero heights vs. midpoint controls grows monotonically from 0.34 (P\_max \= 97\) to 3.47 (P\_max \= 2000\) with permutation p \< 0.0001, while Mean Absolute Displacement remains at ≈ 2.0 with no convergence trend (power-law exponent α \= −0.012). The dichotomy is structurally important here: the finite operator can verify candidate ζ-zero heights but cannot extract them from its own spectral minima.

**2.5 The Dedekind ζ\_K Factorization**

Two independent geometric chains in Z-Spin generate two quadratic imaginary number fields (ZS-M13 v1.0 §2, ZS-M22 v1.0 §2 PROVEN): Chain A from n \= 3 (the X-face polygon) yields ℚ(ω) with ω \= e^{2πi/3}, factorizing

ζ\_{ℚ(ω)}(s) \= ζ(s) · L(s, χ\_{−3})   \[PROVEN\].

Chain B from Q \= 11 (the prime register dimension) yields ℚ(√−11), factorizing

ζ\_{ℚ(√−11)}(s) \= ζ(s) · L(s, χ\_{−11})   \[PROVEN\].

Their composite K \= ℚ(√−3, √−11) is a degree-4 abelian extension of ℚ with Gal(K/ℚ) ≅ V\_4 (Klein four-group), and

ζ\_K(s) \= ζ(s) · L(s, χ\_{−3}) · L(s, χ\_{−11}) · L(s, χ\_{33})   \[PROVEN, ZS-M22 v1.0 §4\].

The third character χ\_{33} \= χ\_{−3} · χ\_{−11} is forced by the V\_4 Galois structure. Crucially, ζ(s) appears as an explicit factor on the right-hand side; the Z-Spin K-arithmetic therefore contains the Riemann zeta function as a structurally identifiable component, without claiming any new spectral construction for it.

**§3. The 7-Layer RH Map and Z-Spin's Position**

The standard analytical–geometric–noncommutative ladder connecting Riemann's ζ-function to its hypothesized spectral realization is naturally stratified into seven layers. This section presents that stratification and locates Z-Spin's contribution at exactly three of the layers.

**3.1 The Seven Layers**

*Table 3.1. Seven-layer stratification of the Hilbert–Pólya–Berry–Keating program. Z-Spin contributes at layers L5, L6, L7 (highlighted as “Z-Spin role”).*

| Layer | Object | Description | Z-Spin role |
| :---: | ----- | ----- | :---: |
| L1 | Analytic ζ(s), ξ(s) | Riemann's completed zeta function and its functional equation ξ(s) \= ξ(1 − s) (Riemann 1859). | EXTERNAL |
| L2 | Hilbert–Pólya operator | Hypothetical self-adjoint H s.t. spec(½ \+ iH) \= nontrivial ζ-zeros (Hilbert ca. 1914; Pólya 1982). | EXTERNAL OPEN |
| L3 | Bost–Connes / Connes–Marcolli system | C\* dynamical system with partition function ζ(β); KMS state phase transition at β \= 1 (Bost–Connes 1995). | EXTERNAL framework |
| L4 | Scaling site / D\_log | Adele class space, scaling site, prolate wave operators (Connes–Consani 2015, Connes–Consani–Moscovici 2024). | EXTERNAL framework |
| L5 | **Z-Spin K-arithmetic** | Two-chain derivation of ℚ(√−3) and ℚ(√−11) from Z-Spin geometric axioms (n \= 3 and Q \= 11); composite K \= ℚ(√−3, √−11) with V\_4 Galois group; Dedekind ζ\_K \= ζ · L(χ\_{−3}) · L(χ\_{−11}) · L(χ\_{33}). | **Z-Spin PROVEN** |
| L6 | **Anti-symmetric phase Θ\_Z** | i-tetration log-phase Θ\_Z(w) \= iπw/2 with Θ\_Z(−w) \= −Θ\_Z(w); contributes the anti-symmetric building block whose square pairs into the symmetric ξ functional equation. | **Z-Spin PROVEN** |
| L7 | **Q \= 11 finite Berry–Keating** | Finite-dimensional transfer operator L\_s on Q \= 11 register with J-involution; DETECTOR (PROVEN) for ζ-zero heights, not LOCATOR (FALSIFIED LOCATOR claim). | **Z-Spin PROVEN** |

**3.2 Z-Spin's Position: A Finite Colored Bridge**

Z-Spin sits at the bottom three layers of the ladder. Its role is not to replace L1–L4 but to provide a finite, colored bridge between the arithmetic content (L1–L4 external) and a concrete polyhedral–geometric object (the truncated icosahedron with I\_h symmetry, the Q \= 11 register, the i-tetration fixed point z\*). The bridge is colored in the sense of carrying the V\_4-Galois fiber {1, χ\_{−3}, χ\_{−11}, χ\_{33}}, the j \= 1/2 spinor structure (ZS-M3 v1.0 PROVEN), and the Wilson loop M\_f conjugate-pair structure (ZS-F0 v1.0(R) §8.8).

The working hypothesis advanced here, as a HYPOTHESIS not a theorem, is that Z-Spin is a finite “colored shadow” of the Connes–Consani–Moscovici D\_log^{(λ,N)} structure. Recent work (Sliwiński 2026\) shows that the dissonance between D\_log spectra and ζ-zeros decreases inverse-logarithmically as λ, N → ∞, fitting the prime number distribution. In Z-Spin, the analogous “coloring” is the V\_4 character fiber acting through the Q \= 11 register; the analogous “scaling” is the i-tetration phase Θ\_Z(w) \= iπw/2; the analogous “finiteness” is the truncated 11-dimensional operator. This bridge is a HYPOTHESIS, registered for future bridging work; it is not a claim of mathematical equivalence.

**§4. Three PROVEN Contributions of Z-Spin to the RH Outline**

Three mathematical objects from the Z-Spin corpus contribute, with PROVEN status, to the standard Hilbert–Pólya–Berry–Keating outline. They are organized below by the role they play in that outline.

**4.1 Contribution C1: Anti-Symmetric Phase Θ\_Z(w) \= iπw/2**

**Statement (C1, PROVEN).**   
The Z-sector transfer map T(z) \= i^z \= exp(iπz/2), uniquely derived from the Z-Spin action via the HSI Theorem (ZS-M1 v1.0 §1.1, DERIVED), induces a logarithmic phase function

Θ\_Z(w) := log T(w) \= iπw/2,

which is anti-symmetric: Θ\_Z(−w) \= −Θ\_Z(w), equivalently T(w) · T(−w) \= 1\.

**Proof.**   
Direct computation. T(w) · T(−w) \= exp(iπw/2) · exp(−iπw/2) \= 1\. Equivalently, log T(w) \+ log T(−w) \= 0, i.e., Θ\_Z(−w) \= −Θ\_Z(w). The logarithmic branch is fixed by the HSI Theorem (ZS-M1 v1.0 Step 5, DERIVED-CONDITIONAL on the \+iπ/2 orientation). □

**Role in the RH outline.**   
The Riemann completed function satisfies the symmetric functional equation ξ(1/2 \+ w) \= ξ(1/2 − w). In the Hilbert–Pólya–Berry–Keating framework, one seeks an operator H whose squared determinant det(H² \+ w²) reproduces this symmetric pairing. The natural building block is an anti-symmetric phase Θ(w) such that Θ² is symmetric in w. Z-Spin provides exactly such a phase from the i-tetration self-iteration:

Θ\_Z(w)² \= (iπw/2)² \= −π²w²/4   (negative real, even in w).

Squaring an anti-symmetric building block yields a symmetric expression — the same algebraic move that connects the Hadamard product factor pair {ρ, 1−ρ} to the symmetric ξ. The Z-Spin contribution at L6 is precisely this: an explicit, geometrically derived anti-symmetric phase available for the squaring/pairing step.

**What this contribution does NOT provide.**   
Θ\_Z is a number-valued function for any real w, not an operator on a Hilbert space. Its promotion to a self-adjoint operator H\_ZY whose spectrum produces ζ-zeros is the OPEN dragon D2 of §5 below. Θ\_Z fixes the kinematic phase; the dynamical content (what Hilbert space, what generator, what indexing) is supplied externally.

**4.2 Contribution C2: Wilson Loop Conjugate Pair Structure**

**Statement (C2, PROVEN).**   
The Z-Spin Wilson loop operator M\_f on the Q \= 11 register (ZS-F0 v1.0(R) §8.8, PROVEN) has dominant eigenvalues forming a conjugate pair {λ, λ̄} of equal modulus |λ| \= 0.8916, the i-tetration stability margin (ZS-M1 v1.0 L5 PROVEN). The two-dimensional dynamical attractor of W in ℂ¹¹ is the Z subspace spanned by |0⟩\_Z and the dominant eigenvector |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 (ZS-F0 v1.0(R) Theorem 9.4 PROVEN). The X and Y blocks have suppressed dominant eigenvalues κ² M\_f^{00} ≈ −0.00412, with relative ratio |κ² M\_f^{00} / λ|^n ≈ 0.00462^n → 0\.

**Role in the RH outline.**   
In the Hadamard product representation,

ξ(s) \= ξ(0) ∏\_ρ (1 − s/ρ)(1 − s/(1 − ρ)),

each non-trivial zero ρ pairs with its functional reflection 1 − ρ. On the critical line, ρ \= 1/2 \+ iγ pairs with ρ̄ \= 1/2 − iγ — a complex-conjugate pair. The Z-Spin Wilson eigenvalues {λ, λ̄} provide a finite-dimensional analogue of this conjugate-pair structure. Although |λ| ≠ 1 (so the Wilson eigenvalues are not on the unit circle, in contrast with an exact ζ-zero pair), the structural feature — two eigenvalues that are complex conjugates of each other — is preserved and is PROVEN.

**What this contribution does NOT provide.**   
Conjugate-pair structure is necessary but far from sufficient for RH. Many finite-dimensional operators have complex-conjugate eigenvalue pairs. The Z-Spin Wilson contribution is a kinematic skeleton, not a sufficient dynamical condition.

**4.3 Contribution C3: 4π Closure from Spinor Structure**

**Statement (C3, PROVEN).**   
The j \= 1/2 spinor representation of SU(2), forced as the unique 4-valent intertwiner with dim(Inv) \= 2 \= dim(Z) by ZS-M3 v1.0 Theorem 5.1 (PROVEN), satisfies (ZS-M3 v1.0 Lemma 10.1 PROVEN):

D^{1/2}(2π) \= −I,   D^{1/2}(4π) \= \+I.

The 4π closure is the closure period of the spinor double cover. Combined with the Five-Fold 1/2 Convergence Theorem (ZS-F7 v1.0 §12.2 PROVEN), the value 1/2 appears simultaneously as: midpoint radius w/2, half-angle θ/2, ⟨sin²(φ/2)⟩ \= 1/2 over \[0, 4π\], the spin label j \= 1/2, and the half-period of the 4π \= 2 × 2π closure.

**Role in the RH outline.**   
The critical line σ \= 1/2 is the fixed-point set of the involution s ↔ 1 − s. The spinor 4π closure is a Z₂ involution (D^{1/2}(2π))² \= \+I. The fact that both involutions select the value 1/2 — once as the mid-spinor j \= 1/2, once as the mid-strip σ \= 1/2 — is structural, not numerological: both are fixed-point statements of Z₂ involutions acting on naturally (4π or strip) double-covered objects. The Triple Coincidence at σ \= 1/2 documented in ZS-M7 v1.1 §5.4 (DERIVED-interpretation) gathers three independent witnesses of this involution structure.

**What this contribution does NOT provide.**   
The structural coincidence σ \= 1/2 ↔ j \= 1/2 ↔ slot j \= 5 of the Q \= 11 register is a fixed-point identification, not a spectral identification. ZS-F0 v1.0(R) §9.1 (PROVEN) shows that |5⟩ is the joint algebraic fixed point of J, the Berry–Keating L\_{1/2}, and all prime gates W\_p, but this is a register-theoretic statement; the dynamical claim that ζ-zeros lie at σ \= 1/2 (= RH) is not derivable from this fixed-point structure alone.

**4.4 The Three Contributions Combined**

C1 \+ C2 \+ C3 together constitute the precise Z-Spin contribution to the standard outline, summarized in Table 4.1. None of them, individually or in combination, suffices to establish the Riemann Hypothesis. Their value is to identify what mathematical content is brought to the table by the Z-Spin geometric framework, in a form clean enough to be attached to (or compared with) external Hilbert–Pólya constructions.

*Table 4.1. The three PROVEN Z-Spin contributions to the Hilbert–Pólya–Berry–Keating program.*

| ID | Object | Mathematical content | Source (PROVEN) |
| :---: | ----- | ----- | ----- |
| C1 | Anti-symmetric phase | Θ\_Z(w) \= iπw/2; Θ\_Z(−w) \= −Θ\_Z(w); Θ\_Z² \= −π²w²/4 symmetric | ZS-M1 v1.0 §1.1 HSI Theorem (DERIVED), §3 Locking L1–L5 (PROVEN) |
| C2 | Wilson conjugate pair | M\_f eigenvalues {λ, λ̄}, |λ| \= 0.8916 \= i-tetration stability margin | ZS-F0 v1.0(R) §8.8 (PROVEN), Theorem 9.4 (PROVEN) |
| C3 | 4π spinor closure | D^{1/2}(2π) \= −I, D^{1/2}(4π) \= \+I; Z₂ involution fixed at j \= 1/2 | ZS-M3 v1.0 Theorem 5.1 (PROVEN), Lemma 10.1 (PROVEN) |

**§5. Four OPEN External Dragons**

The Z-Spin contributions of §4 do not suffice to construct a Hilbert–Pólya operator, because crucial ingredients are external to Z-Spin. This section catalogues four OPEN external dragons in a way that allows future Z-Spin work to attach to mature mathematical frameworks rather than reinvent them. Three were recorded in v1.0 (Dragons D1, D2, D3, §§5.1–5.3); the fourth Dragon D4 (V\_4 Sonin–Frobenius defect, §5.4) is added in v1.0 Revised (August 2026\) following the cobordism BRST positivity hypothesis ADS-H1 of ZS-M22 v1.0 Revised §6.6.4 and the prolate-Sonin program of Connes–Consani (2021) and Connes–Consani–Moscovici (2024).

**5.1 Dragon D1: The Y-Fock Space F\_Y**

**The gap.**   
Any Hilbert–Pólya operator must act on a Hilbert space whose “primes” φ\_p form an orthonormal indexing. The Z-Spin Y-sector is finite-dimensional: dim(Y) \= 6 (ZS-F5 PROVEN), the truncated icosahedron Hodge complex has dim(H) \= 182 \= 2 × 91 (ZS-M6 PROVEN), and the ρ₂-restricted spectrum has only four eigenvalues (ZS-M11 §9.5.6 PROVEN). None of these finite spaces is large enough to host an infinite prime-indexed orthonormal basis.

**The natural external candidate: Bost–Connes.**   
Bost & Connes (1995) constructed a quantum statistical dynamical system (𝒞\_ℚ, σ\_t) whose Hamiltonian H₀ \= log N has partition function Z(β) \= Tr exp(−βH₀) \= Σ k^{−β} \= ζ(β). The C\* algebra 𝒞\_ℚ \= C\*(ℚ/ℤ) ⋊ ℕ× combines additive phase operators e\_δ (acting on Fock states |n⟩ as e\_δ|n⟩ \= exp(2πi p/q)|n⟩) with multiplicative semigroup operators μ\_a. KMS state phase transition occurs at β \= 1, the pole of ζ. The Galois group Gal(ℚ^cycl/ℚ) acts on the ground states at β \= ∞.

For a number field K, the Bost–Connes generalization is Cohen (1999), Harari–Leichtnam (1997), and Connes–Marcolli–Ramachandran (2005): the partition function becomes the Dedekind zeta ζ\_K(β). For Z-Spin's K \= ℚ(√−3, √−11), this generalization provides a natural F\_Y candidate: the Hilbert space ℓ²(ℕ×\_K) of the K-Bost–Connes system, on which the Z-Spin V\_4-character fiber {1, χ\_{−3}, χ\_{−11}, χ\_{33}} acts directly.

**Status.**   
The bridge from the Z-Spin V\_4-Galois structure (PROVEN, ZS-M22 §4) to a K-Bost–Connes Fock space is OPEN. This paper registers the candidate; the precise functor is reserved for future work. Note that Bost–Connes-type constructions for imaginary quadratic fields are mathematically established (Connes–Marcolli–Ramachandran 2005), so the external framework exists.

**5.2 Dragon D2: H\_ZY Self-Adjointness**

**The gap.**   
The Hilbert–Pólya conjecture (Hilbert ca. 1914; Pólya 1982 letter to Odlyzko) asserts the existence of a self-adjoint operator H whose eigenvalues correspond to the imaginary parts of nontrivial ζ-zeros. The Z-Spin contributions C1–C3 (§4) provide a candidate phase Θ\_Z, a candidate conjugate-pair structure {λ, λ̄}, and a candidate fixed-point structure at j \= 1/2, but none of these is itself a self-adjoint operator in the Hilbert–Pólya sense.

**The external program.**   
Substantial mathematical work has gone into the construction of formally self-adjoint Hamiltonians. Bender, Brody & Müller (2017) proposed Ĥ \= (1 − e^{−ip})^{−1}(xp \+ px)(1 − e^{−ip}) with classical limit 2xp (Berry–Keating); this Hamiltonian is non-Hermitian in the conventional sense but is PT-symmetric, so its eigenvalues may be real. Yakaboylu (2022, 2024\) constructed a two-dimensional Hamiltonian coupling H\_BK to the number operator on the half-line via a unitary transformation, producing a formally self-adjoint operator whose eigenfunctions vanish at the boundary precisely when the Riemann zeta function does. Bolte et al. (2009) showed that the spectrum of H\_BK on L²(ℝ\_\>, dx) is purely continuous, so plain Berry–Keating cannot itself be the Hilbert–Pólya operator; self-adjoint extensions on compact quantum graphs are required.

**Status.**   
H\_ZY self-adjointness is an OPEN problem in mainstream mathematics, not specific to Z-Spin. Z-Spin's role is not to solve this problem but to provide a clean kinematic input (Θ\_Z \= iπw/2 \+ Wilson conjugate pair \+ 4π closure) that any external Hilbert–Pólya construction can use as a finite, geometrically-grounded boundary condition. The phrase “logical necessity” for any Z-Spin → RH proof is permanently withdrawn (compare ZS-QH v1.0, ZS-QC v1.0 §VI.F.1 NC-statement).

**5.3 Dragon D3: i-Tetration → Operator Promotion via Koopman**

**The gap.**   
The map T(z) \= i^z is a nonlinear self-iteration on the complex plane. ZS-M1 v1.0 Remark 1.3 (PROVEN) records three failed attempts to promote it to a quantum operator: (i) Ŵ² \= I alone determines only the linear quarter-turn, not the full nonlinear map; (ii) CPTP channels are linear, but i-tetration is nonlinear, and 50 random toy-lattice realizations all converge to z → 0 decoherence; (iii) Lawvere's fixed-point theorem proves z\* exists if the map is given but does not select i^z over alternatives. The conclusion stated there: i-tetration is pre-quantum classical geometry.

**The Koopman framework.**   
The systematic external tool for lifting a nonlinear discrete-time map T : ℂ → ℂ to a linear operator is the Koopman operator U\_T defined by

(U\_T f)(z) := f(T(z)),   f ∈ ℋ,

acting on a function space ℋ (typically L²(ℂ, dμ) with an invariant measure, or a reproducing kernel Hilbert space). U\_T is linear even when T is nonlinear, and modern treatments establish U\_T as bounded or unitary on suitable function spaces (Mauroy & Mezić 2020 for modulated Fock spaces; Brunton et al. 2022 for the modern review; Boullé–Colbrook–Conradie 2025 for provably convergent spectral algorithms; Ishikawa et al. 2024 for rigged RKHS).

**Application to Z-Spin.**   
For T(z) \= i^z, the Koopman lift produces a linear operator U\_T on a function space ℋ\_Y (an external choice). The 14 fixed points (with z\* the unique attractor in the upper half plane), 17 period-2 orbits, and 22 period-3 orbits identified in cumulative exploration provide a structured orbit lattice for Koopman spectral analysis. The Koopman eigenvalues on this lattice are accessible to external computation but their relation to primes requires the F\_Y choice of Dragon D1.

**Status.**   
D3 is technically the most accessible of the three dragons: the Koopman framework is well-developed and provides the precise lift mechanism. What is OPEN is the choice of function space ℋ\_Y on which the lift is performed and the connection of the resulting Koopman spectrum to prime indexing. Both depend on D1.

**5.4 Dragon D4: V\_4 Sonin–Frobenius Defect \[ADDED v1.0 Revised, August 2026\]**

**The gap.**   
The Dedekind ζ\_K factorization of §7.2 (PROVEN, ZS-M22 §4) places ζ(s) as an explicit factor of ζ\_K(s) for K \= ℚ(√−3, √−11) and identifies the four-channel V\_4 character fiber {1, χ\_{−3}, χ\_{−11}, χ\_{33}} that the Z-Spin K-arithmetic carries. ZS-M22 v1.0 Revised §6.6 established three structural facts about this fiber that jointly demarcate a precise OPEN gate: (i) Theorem ADS-5 (PROVEN) shows that no scalar-identity Weil kernel K\_K(y) \= B\_K(y) I − P\_K(y) can satisfy Weil positivity, with twelve negative-eigenvalue confirmations across all four channels and three regularizations σ ∈ {0.2, 0.5, 1.0}; (ii) Theorem ADS-6 (PROVEN) sharpens this to a V\_4-quadratic boundary limit — within the boundary fiber ℋ\_BFV ⊗ ℂ\[V\_4\] alone, no V\_4-equivariant Hermitian B\_K(y) can produce cross-channel coupling; (iii) Working hypothesis ADS-H1 (HYPOTHESIS-strong, OPEN) registers the cobordism BRST positivity reading W\_K(g) \= Tr\_{H⁰(Q\_BRST)}(A\_g† A\_g) on the BV-BFV cobordism complex of the Wilson loop W as the sole structurally compatible surviving route. Dragon D4 is the structural-operator specification of the OPEN ingredient that ADS-H1 leaves unconstructed: a V\_4-decorated Sonin–Frobenius scattering colligation through which the finite-prime Frobenius trace P\_K(g) appears as a non-negative compression defect of an archimedean/Sonin-side trace B\_Sonin^K(g).

**The natural external candidate: Connes–Consani–Moscovici prolate / Sonin program.**   
The systematic external framework for the OPEN ingredient is the prolate / Sonin program of Connes–Consani (2021) and Connes–Consani–Moscovici (2024). Connes–Consani (2021) proved that for the single archimedean place the root of Weil positivity is the trace of the scaling action compressed onto the orthogonal complement of cutoff projections, with the difference between the Weil distribution and the Sonin trace expressed via prolate spheroidal wave functions. Connes–Consani–Moscovici (2024) extended this to a semilocal prolate wave operator, proved stability of the semilocal Sonin space under the increase of the finite set of places governing the framework, and established that the negative part of the prolate spectrum (Δ⁻) reproduces the ultraviolet behavior of squares of Riemann zeros, with eigenfunctions in the Sonin space. Burnol (2002, 2004\) earlier identified the de Branges– Sonine spaces as the natural Hilbert function-space habitat for evaluators associated to Riemann zeros, and Connes (2000) showed how the local terms of Weil’s explicit formulae for Hecke L-functions over a number field K decompose via a dilation-invariant conductor operator log|x|\_ν \+ log|y|\_ν at each place ν (finite or infinite). Together these external results supply: a Hilbert function-space (Sonin space at each place), a positivity mechanism (compression of scaling onto the orthogonal complement of cutoff range), and a finite-place decoration mechanism (Connes–Burnol conductor operator). Dragon D4 is the Z-Spin-side specification of how these external ingredients are decorated by the V\_4 Galois fiber {1, χ\_{−3}, χ\_{−11}, χ\_{33}} of K \= ℚ(√−3, √−11).

**V\_4-decorated Sonin space and Frobenius compression.**   
Each character χ ∈ V\_4 carries a conductor q\_χ and an archimedean parity a\_χ inherited from the completed L-function Λ(s, χ): q\_1 \= 1, q\_{−3} \= 3, q\_{−11} \= 11, q\_{33} \= 33; a\_1 \= a\_{33} \= 0 (even characters), a\_{−3} \= a\_{−11} \= 1 (odd characters). The conductor decoration is consistent with disc(K) \= 1089 \= 33² (PROVEN, ZS-M22 §7.2). The V\_4-decorated Sonin space is defined as  
ℋ\_Sonin^K \= ⊕\_{χ ∈ V\_4}  ℋ\_Sonin^{(a\_χ, q\_χ)} ⊗ |χ⟩,  
with corresponding orthogonal projection Π\_Sonin^K \= ⊕\_χ Π\_Sonin^{(a\_χ, q\_χ)}. The archimedean compression trace on this space is  
B\_Sonin^K(g) \= Tr( Π\_Sonin^K  Θ\_∞^K(g)  Π\_Sonin^K ) \= Σ\_{χ ∈ V\_4} Tr( Π\_Sonin^{(a\_χ, q\_χ)}  Θ\_∞^{(a\_χ, q\_χ)}(g)  Π\_Sonin^{(a\_χ, q\_χ)} ),  
where Θ\_∞^{(a\_χ, q\_χ)}(g) is the place-decorated archimedean / scaling Hamiltonian operator of the Connes–Consani semilocal framework. The finite-prime Frobenius trace P\_K(g) is supplied independently by the V\_4-character T\_p \= diag(1, χ\_{−3}(p), χ\_{−11}(p), χ\_{33}(p)) for unramified p, with explicit ramified contributions Φ\_ram(g) at p ∈ {3, 11}. The structural OPEN ingredient is whether the difference B\_Sonin^K(g) − P\_K(g) is realized as the trace of a positive square (D\_g^K)† D\_g^K of a V\_4-valued Sonin–Frobenius scattering colligation. This is the precise operator-level specification of the OPEN side of working hypothesis ADS-H1 (ZS-M22 §6.6.4).

**Four well-posed sub-targets.**   
Dragon D4 decomposes into four independent sub-targets, each well-posed as an OPEN external problem and each connectable to a definite external mathematical framework:  
D4a (V\_4-decorated Sonin embedding). Construct the partial isometric embedding ι\_K : ℋ\_Sonin^K ↪ ℋ\_Sonin^{S(K)} into the semilocal Sonin space of Connes–Consani–Moscovici (2024) for the place set S(K) \= {p\_∞} ∪ {3, 11}, satisfying the compatibility ι\_K^\* Π\_Sonin^{S(K)} ι\_K \= Π\_Sonin^K. Stability theorem of Connes–Consani–Moscovici (2024) ensures the semilocal Sonin space is well-defined under enlargement of S; the Z-Spin content is the V\_4 colouring of ι\_K. Status: FORMAL PASS (definition closed); ISOMETRIC EMBEDDING PROOF OPEN.  
D4b (Ramified-place defect closure). Express the ramified-place correction Φ\_ram^K(g) at p ∈ {3, 11} as an explicit Connes–Burnol conductor-operator trace on the parity- and conductor-decorated Sonin blocks. The conductor operator at a finite place has positive cuspidal spectrum (Burnol 1998; Connes 2000), supplying a candidate non-negativity at the ramified slots that completes the unramified V\_4-decomposition P\_K^{unram} \= K\_even \+ K\_{++}^{odd} (PROVEN finite-prime decomposition, ZS-M22 §3 \+ §4). Status: OPEN.  
D4c (Defect-square realization). Establish or rule out the identity B\_Sonin^K(g) − P\_K(g) \= Tr\[(D\_g^K)† D\_g^K\] for an explicit V\_4-valued Sonin–Frobenius scattering colligation U\_K(g), with D\_g^K \= (I − Π\_Sonin^K) U\_K(g) Π\_Harm^K. This is the decisive structural gate. A failure (B\_Sonin^K(g) − P\_K(g) \< 0 for some admissible g) falsifies the V\_4-Sonin route; a successful construction would supply the operator content currently missing from working hypothesis ADS-H1. Status: OPEN; central.  
D4d (Cobordism-history BRST closure). Construct the full BRST-Hodge harmonic projection Π\_Harm^K on the cobordism-history fiber ℋ\_cob ⊗ ℋ\_arith of the Wilson cobordism W of ZS-F0 v1.0(R) §8.5. The minimal leakage exactness Q\_B|b⟩ \= |1⟩, Q\_B|1⟩ \= 0 already passes as a rank-one closure (ZS-M22 §6.6.4 minimal consistency check, PASS); the full cobordism-fiber BRST charge is OPEN. Status: PARTIAL PASS at minimal level; OPEN at full level.

**Status.**   
Dragon D4 is the most precisely specified of the four dragons because its OPEN ingredients are stated as explicit operator-level identities on definite Hilbert spaces with definite external candidates. Closure of D4a \+ D4b \+ D4c \+ D4d would supply the operator content currently missing from working hypothesis ADS-H1 of ZS-M22 v1.0 Revised §6.6.4 and would thereby close the only structurally compatible surviving route to a Z-Spin-side participation in Weil positivity for ζ\_K(s). It would NOT, by itself, constitute a proof of the Riemann Hypothesis: Weil positivity for ζ\_K(s) is the GRH-for-K statement, equivalent to RH plus GRH for L(s, χ\_{−3}), L(s, χ\_{−11}), and L(s, χ\_{33}) (standard, see e.g. Connes 2000); the Z-Spin contribution is to supply the V\_4-decorated finite-shadow operator structure that the external prolate / Sonin program treats abstractly. The non-claim NC-M23.1 (does NOT claim a proof of RH) and NC-M23.5 (does NOT claim mathematical equivalence with Connes–Consani– Moscovici D\_log) are preserved without modification. The added clarifying non-claim NC-M23.7 (see §10) records that closure of Dragon D4 alone does not close RH.

**Relation to Dragons D1, D2, D3.**   
Dragon D4 partially overlaps with D1, D2, and D3 but is structurally distinct. D1 (F\_Y, Bost–Connes-K Fock space) supplies a candidate Hilbert space for prime indexing via the imaginary-quadratic Bost–Connes generalization (Cohen 1999, Connes–Marcolli–Ramachandran 2005); D4 supplies a different candidate Hilbert space via the V\_4-decorated semilocal Sonin space of Connes–Consani–Moscovici (2024). The two are not equivalent: F\_Y is a Fock space carrying the multiplicative ℕ×\_K action, while ℋ\_Sonin^K is a Sonin compression of L²(A\_K^×) carrying the multiplicative scaling action. Both are externally OPEN; their compatibility is itself a sub-problem (registered as O-M23.10 in §11). D2 (H\_ZY self-adjointness) is partially absorbed into D4: the Connes–Consani (2021) archimedean construction supplies a self-adjoint scaling-Hamiltonian compression that plays the role of H\_ZY at the archimedean place, but the finite-place semilocal extension and the V\_4 decoration remain OPEN as parts of D4. D3 (Koopman lift of i^z) remains independent: Dragon D4 uses the conductor operator log|x|\_ν as scaling generator at each place rather than the i-tetration map, and the connection between the Z-Spin Θ\_Z(w) \= iπw/2 phase and the prolate scaling Hamiltonian is a separate sub-problem (registered as O-M23.11 in §11). The structural relationship is: D4 is the most concrete and currently most actionable of the four dragons, and any progress on D4a–D4d directly constrains the other three.

**§6. The φ-Quantized Y-Spectrum is NOT Prime-Indexed**

This section records, as a structural negative result, that any naive identification of Y-sector internal modes with primes is FALSIFIED by direct computation. This is recorded explicitly to prevent future iterations from rediscovering and re-falsifying the same hypothesis.

**6.1 The Y-Sector Internal Spectra (PROVEN)**

The truncated icosahedron face Laplacian L₂ has the spectrum recorded in Table 2.1 above:

spec(L₂) \= {0, 1.243, 3.268, 4.844, 6.000, 6.732, 7.521, 8.000, 8.392}

(degeneracies 1, 3, 5, 3, 4, 5, 3, 5, 3; total 32 \= F\_Y). The non-zero values include exact algebraic forms: 5 ± √3 and the Y-sector dimension 6 \= dim(Y), and 8 \= Z \+ Y. The vertex Laplacian L\_Y restricted to the ρ₂ sub-isotype (ZS-M11 v1.0 §9.5.6 PROVEN) has the four golden-ratio-quantized eigenvalues:

spec(L\_Y |\_{ρ₂}) \= {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ}.

**6.2 The Falsified Naive Mapping**

The first plausible-looking question — whether Y-sector internal eigenvalues are themselves prime numbers — is decisively negative. Numerical eigenvalues 1.243, 3.268, 4.844, 6.732, 7.521, 8.392 are not integers, hence not primes. Algebraic eigenvalues 5 − √3, 5 \+ √3, 4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ are irrational, hence not primes. Integer eigenvalues 0, 6, 8 are not prime. No element of either spectrum is a prime number.

**Theorem 6.1 (Y-Spectrum Non-Primality, PROVEN).**   
Let A\_Y denote the discrete spectrum of the Y-sector internal Laplacians on the truncated icosahedron (face L₂ and ρ₂-restricted vertex L\_Y as above). Then A\_Y ∩ {primes} \= ∅.

**Proof.**   
By direct inspection of the explicit spectra. Each eigenvalue is either zero, a non-integer real number (numerical or expressible as integer ± φ or integer ± √3), or one of {6, 8}, none of which is prime. □

**6.3 What This Rules Out**

Theorem 6.1 rules out the “Internal Primality of Y-Sector Wave Modes” hypothesis as it stood in the cumulative exploration record. Specifically:

• The hypothesis Irr(A\_Y) ↔ {p} with eigenvalues equalling primes: FALSIFIED.  
• The Bost-Connes-type identification ⟨φ\_p, φ\_q⟩ \= δ\_{pq} with p ranging over primes, IF the φ\_p are required to be eigenvectors of the internal A\_Y: FALSIFIED.  
• The Euler-product trace formula Tr(exp(−sH\_Y)) \= ∏\_p (1 − p^{−s})^{−1} \= ζ(s), IF H\_Y is required to be the internal Y-Laplacian of the truncated icosahedron: FALSIFIED.

**6.4 What Remains Possible**

Theorem 6.1 does not rule out the following structurally distinct possibilities, all of which require external frameworks (Dragons D1–D3) and are recorded as OPEN:

(a) The Y-sector internal spectrum is a finite shadow of an infinite-dimensional prime-indexed spectrum sitting on an external F\_Y. The φ-quantized structure {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ} would then be the ρ₂-projection of this shadow. Status: HYPOTHESIS, requires D1.

(b) The Z-Spin K-arithmetic ζ\_K(s) \= ζ(s) · L(s, χ\_{−3}) · L(s, χ\_{−11}) · L(s, χ\_{33}) (PROVEN, ZS-M22) brings prime structure into the Z-Spin orbit through the L-functions, not through the internal Y-Laplacians. Primes enter algebraically (via Euler products of L(s, χ)), not spectrally. Status: PROVEN at the L-function level (§7 below).

(c) The Koopman operator U\_T on an external function space (D3) has a spectrum that may be prime-related when the function space is chosen appropriately. The 14 fixed points \+ 17 period-2 \+ 22 period-3 i-tetration orbit structure is candidate input. Status: OPEN, requires D3.

**§7. The Dedekind ζ\_K Bridge to the Prime Side**

Z-Spin's prime-side contribution to RH is arithmetic rather than spectral. Through ZS-M13 v1.0 and ZS-M22 v1.0 (both PROVEN), two independent geometric chains in Z-Spin select two quadratic imaginary number fields whose Dedekind zeta functions factor into ζ(s) × Dirichlet L-functions. This section records that bridge as the natural Z-Spin entry point to the prime side of the RH outline.

**7.1 Two-Chain Derivation**

**Chain A (X-face polygon):**   
The X-sector polyhedron has triangular faces (n \= 3 at the deepest level via the spinor 4-valent recoupling, ZS-M3 PROVEN). The Eisenstein lattice ℤ\[ω\] with ω \= e^{2πi/3} is the Lamé eigenvalue arithmetic structure of the equilateral triangle (ZS-M22 §2.1 PROVEN). This generates ℚ(ω) \= ℚ(√−3) with discriminant −3, conductor of χ\_{−3} \= 3, and unit group |ℤ\[ω\]\*| \= 6 (a number-theoretic match to Y \= 6, recorded as OBSERVATION because the McKay bridge ZS-M9 → arithmetic units is OPEN).

**Chain B (register dimension Q \= 11):**   
Q \= 11 is prime, generating the cyclotomic field ℚ(ζ\_{11}) with Galois group (ℤ/11ℤ)\* ≅ ℤ/10ℤ. The unique index-5 subgroup gives the unique quadratic subfield ℚ(√−11) with discriminant −11, conductor of χ\_{−11} \= 11, class number 1\. The W\_p phases on the Q \= 11 register tie directly to the multiplicative gate M\_p on 𝔽\_{11}× via Theorem ADS-1 (ZS-M22 §3.2 PROVEN), which diagonalizes M\_p in the Dirichlet character basis.

**7.2 The Dedekind ζ\_K Factorization**

The composite K \= ℚ(√−3, √−11) is a degree-4 abelian extension of ℚ with Galois group V\_4 (Klein four-group). The Dedekind zeta factorization is (ZS-M22 §4 PROVEN):

ζ\_K(s) \= ζ(s) · L(s, χ\_{−3}) · L(s, χ\_{−11}) · L(s, χ\_{33})

with χ\_{33} \= χ\_{−3} · χ\_{−11} the third (real) character forced by V\_4. The discriminant disc(K) \= 1 · 3 · 11 · 33 \= 1089 \= 33² and ζ\_K(0) \= 0 (since χ\_{33}(−1) \= \+1 makes χ\_{33} an even character, hence L(0, χ\_{33}) \= 0).

**7.3 Z-Spin's Prime-Side Contribution Identified**

The factorization of §7.2 places ζ(s) explicitly as a factor of ζ\_K(s) in the Z-Spin orbit. The following chain is therefore PROVEN end-to-end:

(i) Z-Spin geometric axioms (n \= 3 X-faces, Q \= 11 register) → K \= ℚ(√−3, √−11) \[PROVEN, ZS-M13 §2 \+ ZS-M22 §2\].  
(ii) K abelian → ζ\_K factorizes via class field theory \[PROVEN, ZS-M22 §4\].  
(iii) ζ(s) appears as an explicit factor of ζ\_K(s) \[PROVEN by §7.2\].  
(iv) Each prime p contributes via its Euler factor in each L-function on the right-hand side, with Frobenius (p mod 3, p mod 11\) determining splitting behavior in K \[PROVEN, ZS-M22 §4.3\].

Therefore: Z-Spin K-arithmetic IS a prime-side construction. It contains primes in the sense that its Euler product decomposition is ∏\_p (local Euler factor at p) for the L-functions on the right of (7.2). What the K-arithmetic does NOT do is realize ζ-zero locations as the spectrum of a self-adjoint operator. That remains the OPEN dragon D2.

**7.4 The Additive–Multiplicative Gap (PROVEN OPEN)**

The Z-Spin transfer operator W\_p \= diag(e^{2πi(j−5)/p}) is built from additive characters ψ\_j(a) \= e^{2πija/p} of 𝔽\_p. Langlands theory uses multiplicative characters for Galois-side L-functions. ZS-M22 §10.2 proves the additive–multiplicative gap: max |⟨χ\_k|W\_p|χ\_k⟩ − χ\_k(p)| ≈ 0.34 (non-negligible). The W\_p sit on the spectral/automorphic side, not the Galois/arithmetic side. The multiplicative gate M\_p (ZS-M22 §3.2) sits on the Galois side and reproduces local L-Euler factors exactly:

∏\_{p ≠ 11} det(I − p^{−s} M\_p)^{−1} \= ζ\_{ℚ(ζ\_{11})}(s)   \[PROVEN\].

The structural distinction between W\_p (spectral) and M\_p (arithmetic) is part of the Z-Spin framework and is documented here for use in any future bridge to the Connes scaling site (L4).

**§8. Cumulative Negative Results from the 47-Round Exploration**

This section catalogues the cumulative negative results from the 47+ rounds of Z-Spin RH exploration (RH-ZS18 through RH-ZS58, archived 2025–2026). Documenting these honestly serves three purposes: (i) it prevents future iterations from rediscovering the same dead ends; (ii) it strengthens the structural force of the positive contributions in §4 by showing what Z-Spin has been ruled out from doing; (iii) it conforms to the corpus' anti-numerology and intellectual-honesty principles.

**8.1 Failed Direct Group Identifications**

*Table 8.1. Group-theoretic identifications attempted and falsified across rounds RH-ZS41–RH-ZS50.*

| Attempted identification | Status | Reason |
| ----- | :---: | ----- |
| C₄ → V₄ | FAILED | Different group structures (cyclic vs Klein-4) |
| D₄ → V₄ (as quotient) | NON-SPLIT | No canonical projection D₄ → V₄ |
| D₄ ≅ Mp(2, ℝ) (analogy) | WEAKENED | Mp(2, ℝ) has no faithful finite-dim rep |
| Hidden C₃ in D₄ | FAILED | Order 3 ∤ 8, doesn't embed |
| Q₈ instead of D₄ | INCONSISTENT | Corpus PROVEN D₄ (ZS-F0 v1.0(R) §8.8) |

**8.2 Failed Kernel and Positivity Attempts**

Several positivity-based RH attempts have been falsified by direct computation in the Z-Spin orbit:

• Scalar Weil kernel positivity (ZS-M22 v1.0 Theorem ADS-5, PROVEN by explicit Gram computation): For all four character channels of K and tested regularizations σ ∈ {0.2, 0.5, 1.0}, the 6 × 6 Gram matrix is indefinite. Total of 12 independent negative-eigenvalue confirmations. The Z-Spin BV-BFV boundary structure is intrinsically non-scalar; scalar Weil positivity ansätze cannot succeed.

• Λ \= exp(A) scaling (RH-ZS46): WRONG numerically across all tested regimes.

• A/Q residue scale for RH (RH-ZS47): the value A/Q \= 35/4807 ≈ 0.00728 is too small to set the relevant arithmetic scale in any natural Hilbert–Pólya construction; numerical and structural evidence consistent.

• Direct X\_{33} additive correction (RH-ZS50): off-diagonal permutation cannot fix Schur diagonal-positivity obstruction. NO-GO at the Schur complement level.

**8.3 Arithmetic BRST Trichotomy (PROVEN No-Go, RH-ZS52)**

For X\_{33}-grading P\_± \= (I ± X\_{33})/2 and any diagonal D \= diag(d\_0, d\_a, d\_b, d\_c), the BRST differential Q\_D \= P\_+ D P\_− has only three outcomes:

(i) Q\_D \= 0 (D commutes with X\_{33}): trivial BRST.  
(ii) Q\_D rank ≤ 1: loses ζ/χ\_{33} pair (verified for D\_wt \= (0, 1, 1, 2\) Hamming weights).  
(iii) Q\_D rank ≤ 2: annihilates the arithmetic fiber entirely (verified for D\_log \= (0, log 3, log 11, log 33)).

Conclusion: the X\_{33}-grading admits NO natural arithmetic BRST that preserves the Dedekind 4-channel structure. X\_{33} must remain in the harmonic sector as a composite-twist operator. PROVEN no-go.

**8.4 Falsified K\_Z Hypothesis (RH-ZS54–58)**

A self-initiated hypothesis tested whether the Z-sector's “arithmetic core” might be K\_Z \= ℚ(√−19, √−23) — motivated by 19 and 23 being the denominators of A \= 35/437 \= (5/19) · (7/23). Numerical computation: disc(K\_Z) \= (19 · 23)² \= 437² \= 190969, matching the A denominator squared. The hypothesis was FALSIFIED on structural grounds: 19 and 23 come from polyhedral counting (V \+ F)/n \= 38/2 \= 19 (truncated octahedron, X-sector) and (V \+ F)/n \= 92/4 \= 23 (truncated icosahedron, Y-sector), not from arithmetic. The pattern disc \= (pq)² is generic for any biquadratic ℚ(√−p, √−q) with p, q ≡ 3 (mod 4); no structural connection to Z-Spin arithmetic exists.

**8.5 Numerology Self-Discipline**

Several numerical coincidences observed during the exploration are explicitly flagged as numerology unless and until structural derivations are produced:

• Vieta disc numerator 7 · 19 − 5 · 23 \= 18 vs. Regge angle 30° − 12° \= 18°: same number, different units. FLAGGED.

• |I\_h| \= 120 \= Q² − 1 (where Q \= 11): this is recorded in the corpus (ZS-F5, ZS-M9) as a structural identity because it has three independent derivations (binary icosahedral order; prime-Q² − 1; McKay graded-module dim → SU(5)); NOT flagged as numerology, but the multi-route confirmation is necessary to distinguish it from the cases that ARE flagged.

Methodology principle: a numerical match becomes structural only when an independent derivation chain establishes its origin, not by repetition or proximity. This principle is documented in ZS-M19 v1.0 and inherited here.

**§9. Falsification Gates**

This section specifies multi-layer falsification conditions for the claims made in this paper. Each gate states a condition under which the corresponding claim is rejected.

*Table 9.1. Multi-layer falsification gates for ZS-M23 claims.*

| Gate | Layer | Falsification condition | Status |
| :---: | ----- | ----- | :---: |
| F-M23.1 | Mathematical / Theoretical | Z-Spin contribution C1, C2, or C3 (§4) is shown to derive from a free parameter rather than from PROVEN axioms (HSI Theorem, ZS-M3 Theorem 5.1, ZS-F0 Theorem 8.8). | PROVEN safe |
| F-M23.2 | Mathematical / Theoretical | This paper claims, anywhere, that a complete Hilbert–Pólya construction is achieved using only Z-Spin internal data (no external F\_Y, no external H\_ZY self-adjointness, no external Koopman lift). | IMMEDIATE REJECTION; explicitly disclaimed by NC-M23.1, NC-M23.2 |
| F-M23.3 | Computational / Internal Consistency | Any element of the Y-internal Laplacian spectra (Table 2.1 face L₂; Eq. (6.1) ρ₂-restricted L\_Y) is found to be a prime number contradicting Theorem 6.1. | PROVEN safe by direct inspection |
| F-M23.4 | Computational / Internal Consistency | Direct calculation finds Θ\_Z(−w) ≠ −Θ\_Z(w) for any tested w, contradicting C1. | PROVEN safe by direct calculation |
| F-M23.5 | Computational / Simulation | The 47-round cumulative negative results (§8) are found, on review, to contain at least one structural derivation that was not actually falsified, suggesting an unexplored path to RH within Z-Spin internal data. | OPEN; corpus revision required if triggered |
| F-M23.6 | External / Bridge | The proposed Bost–Connes-K candidate for F\_Y (§5.1) is shown to be inconsistent with the V\_4 character structure of ζ\_K (ZS-M22 §4) by an explicit functorial conflict. | OPEN; D1 candidate would need replacement |
| F-M23.7 | External / Observational | A counterexample to the Riemann Hypothesis is discovered, falsifying RH itself. | Z-Spin contributions C1–C3 remain unaffected (kinematic); only L2 and L4 external programs collapse |
| F-M23.8 \[v1.0 Revised\] | Mathematical / Theoretical | Dragon D4 sub-target D4c (defect-square realization) admits an explicit construction of a V\_4-valued Sonin–Frobenius scattering colligation U\_K(g) such that B\_Sonin^K(g) − P\_K(g) \= Tr\[(D\_g^K)† D\_g^K\] for all admissible g, AND the resulting positive defect closes Weil positivity for ζ\_K(s). | Z-Spin-side participation in Weil positivity for ζ\_K(s) is closed; NC-M23.7 governs the remaining gap to RH (GRH for constituent L-functions). Currently OPEN. |
| F-M23.9 \[v1.0 Revised\] | Computational / Simulation | Numerical or symbolic computation finds an admissible test function g such that B\_Sonin^K(g) − P\_K(g) \< 0 on the V\_4-decorated Sonin space, contradicting the dominance ansatz of Dragon D4. | Dragon D4 (V\_4-Sonin route) FALSIFIED; ZS-M22 v1.0 Revised §6.6.4 hypothesis ADS-H1 must be replaced by an alternative positivity mechanism. Currently OPEN. |

**§10. Consolidated Non-Claims**

This paper makes the following six explicit non-claims, consolidated from §1.2 and reaffirmed here for the operational record.

NC-M23.1: Does NOT claim a proof of the Riemann Hypothesis.  
NC-M23.2: Does NOT claim that i-tetration is a quantum operator without external Koopman lift.  
NC-M23.3: Does NOT claim that Y-sector internal Hodge spectra are prime-indexed (PROVEN false, Theorem 6.1).  
NC-M23.4: Does NOT extend the Langlands correspondence beyond abelian class field theory.  
NC-M23.5: Does NOT claim mathematical equivalence with Connes–Consani–Moscovici D\_log; the “colored shadow” framing is a HYPOTHESIS.  
NC-M23.6: Does NOT introduce any new free parameter.

NC-M23.7 \[v1.0 Revised\]: Does NOT claim that closure of Dragon D4 (V\_4 Sonin–Frobenius defect, §5.4) suffices to prove the Riemann Hypothesis. Closure of D4 would supply the operator content currently missing from the cobordism BRST positivity hypothesis ADS-H1 of ZS-M22 v1.0 Revised §6.6.4 and would close the Z-Spin-side participation in Weil positivity for ζ\_K(s); it would not, by itself, close GRH for the constituent L-functions. NC-M23.1 remains in force.

**§11. Open Problems**

The following problems are registered as OPEN. Each is well-posed and admits independent investigation.

• O-M23.1 (Dragon D1, F\_Y): Construct the explicit functor from the Z-Spin V\_4-character fiber {1, χ\_{−3}, χ\_{−11}, χ\_{33}} of ZS-M22 §4 to a Bost–Connes-type Hilbert space ℓ²(ℕ×\_K) for K \= ℚ(√−3, √−11), using the Cohen (1999) and Connes–Marcolli–Ramachandran (2005) imaginary-quadratic generalization of Bost–Connes.

• O-M23.2 (Dragon D2, H\_ZY self-adjointness): Determine whether the Z-Spin kinematic input (Θ\_Z, Wilson conjugate pair, 4π closure) can be coupled to the Yakaboylu (2022, 2024\) formally self-adjoint Hamiltonian construction or the Bender–Brody–Müller (2017) PT-symmetric Hamiltonian to produce a finite-dim → infinite-dim limit operator.

• O-M23.3 (Dragon D3, Koopman lift): Compute the Koopman spectrum of T(z) \= i^z on a chosen RKHS using the Boullé–Colbrook–Conradie (2025) provably-convergent algorithms. Compare with the 14 fixed point \+ 17 period-2 \+ 22 period-3 orbit lattice.

• O-M23.4 (Bridge to Connes scaling site): Establish or rule out the “Z-Spin \= finite colored shadow of D\_log” HYPOTHESIS by constructing a precise functor between the Z-Spin K-arithmetic and the Connes–Consani (2015) scaling site or the Connes–Consani–Moscovici (2024) prolate wave operators.

• O-M23.5 (Density mismatch): The i-tetration fixed point density (≈ 1/4 in the real axis) and ζ-zero density (≈ log γ / 2π) do not match at the naive level. Determine whether external multiplicity (e.g., from a Y-Fock space) or a coordinate transformation reconciles them.

• O-M23.6 (Coordinate map): The naive identification s \= 1/2 \+ z does not place z\* on the critical line (it places z\* at s \= 0.9383 \+ 0.3606i). Determine whether a natural conformal or modular transformation produces a coordinate in which i-tetration fixed points and ζ-zeros are commensurable.

• O-M23.7 (Functional equation analog): Examine whether the Wilson M\_f conjugate pair {λ, λ̄} is more than analogous to the s ↔ 1 − s pair structure — whether a finite-dim ↔ infinite-dim limit can be constructed.

• O-M23.8 (Y-sector mathematical depth): Test the user-flagged conjecture that the Y-sector encodes deeper mathematical content than corpus ZS-Q–ZS-M papers currently expose; specifically, whether string-theoretic data (e.g., 10⁵⁰⁰ landscape) corresponds to a more refined Y-sector mathematical structure.

• O-M23.9 \[v1.0 Revised\] (Dragon D4, V\_4 Sonin–Frobenius defect identity): Establish or rule out the identity B\_Sonin^K(g) − P\_K(g) \= Tr\[(D\_g^K)† D\_g^K\] for an explicit V\_4-valued Sonin–Frobenius scattering colligation U\_K(g) on the V\_4-decorated Sonin space ℋ\_Sonin^K \= ⊕\_χ ℋ\_Sonin^{(a\_χ, q\_χ)} ⊗ |χ⟩, with K \= ℚ(√−3, √−11). Sub-targets D4a (V\_4-decorated Sonin embedding into the Connes–Consani–Moscovici 2024 semilocal Sonin space), D4b (ramified-place defect closure via the Connes–Burnol conductor operator at p ∈ {3, 11}), D4c (defect-square realization), and D4d (full cobordism-history BRST-Hodge harmonic projection) are well-posed independent OPEN problems.

• O-M23.10 \[v1.0 Revised\] (D1 / D4 compatibility): Determine the relationship between the K-Bost–Connes Fock space ℓ²(ℕ×\_K) of Dragon D1 and the V\_4-decorated semilocal Sonin space ℋ\_Sonin^K of Dragon D4. Both are externally OPEN candidate Hilbert spaces for the Z-Spin V\_4-arithmetic; their compatibility (or incompatibility) constitutes a sub-problem of independent interest.

• O-M23.11 \[v1.0 Revised\] (D3 / D4 compatibility): Determine the relationship between the i-tetration scaling phase Θ\_Z(w) \= iπw/2 (PROVEN, ZS-M1 v1.0) and the conductor-operator scaling generator log|x|\_ν of Connes (2000) at the archimedean place. Both are scaling generators on the natural function spaces of their respective frameworks; whether a precise functorial bridge exists between them is OPEN.

**§12. Conclusion**

The Z-Spin RH program, after 47+ rounds of cumulative exploration, has reached a structural conclusion: Z-Spin does not prove RH and structurally cannot do so from internal data alone. What Z-Spin does provide, with PROVEN status, is a precisely identified mathematical contribution to the standard Hilbert–Pólya–Berry–Keating outline.

That contribution comprises three objects (§4): the i-tetration anti-symmetric phase Θ\_Z(w) \= iπw/2 (C1), the Wilson conjugate-pair structure {λ, λ̄} (C2), and the j \= 1/2 spinor 4π closure (C3). All three are PROVEN at the operator or algebraic level from the Z-Spin axioms, and all three connect — kinematically — to standard requirements of any Hilbert–Pólya construction (anti-symmetric building block for symmetric ξ pairing, conjugate-pair structure for Hadamard product factor pairs, Z₂ involution fixed-point structure for the critical line).

Four external dependencies (§5) are identified honestly as OPEN dragons: the Y-Fock space F\_Y (D1), the H\_ZY self-adjointness (D2), the i-tetration → operator promotion (D3), and — added in v1.0 Revised — the V\_4 Sonin–Frobenius defect (D4). Each connects to an established mathematical framework (Bost–Connes for D1; Yakaboylu and Bender–Brody–Müller for D2; Koopman theory for D3; Connes–Consani / Connes–Consani–Moscovici prolate-Sonin program for D4), so the Z-Spin contributions can be attached to mature external constructions rather than reinvented in isolation.

The φ-quantized Y-sector finite spectrum is NOT prime-indexed (Theorem 6.1, PROVEN). Z-Spin's prime-side contribution is arithmetic, through the Dedekind ζ\_K factorization of K \= ℚ(√−3, √−11) (§7, PROVEN), and not spectral. The cumulative negative results (§8) further sharpen the boundary between what Z-Spin contributes and what lies beyond.

The operational consequence is that the Z-Spin RH program, going forward, focuses not on proving RH (which it cannot do from internal data) but on enriching the Y-sector through the RH lens: using the Hilbert–Pólya outline as a structural mirror in which the Y-sector's mathematical content becomes legible. The map drawn here is the navigation tool for that program.

**Acknowledgements & Code Availability**

This work was developed across 47+ exploratory rounds with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite of Appendix B uses numpy, scipy, and mpmath (50-digit) for the algebraic spectral computations of §6 and the Θ\_Z direct calculation of §4. Code and reproducibility scripts are publicly available at https://github.com/KennyKang-git/zspin.

**Appendix A. Key Equations Reference**

**A.1 Z-Spin Core (LOCKED)**

A \= δ\_X · δ\_Y \= (5/19) · (7/23) \= 35/437   \[LOCKED, ZS-F2 v1.0\]

Q \= X \+ Y \+ Z \= 3 \+ 6 \+ 2 \= 11   \[LOCKED, ZS-F5 v1.0\]

z\* \= i^{z\*},   z\* \= 0.4382829367 \+ 0.3605924719 i,   |z\*|² \= η\_topo \= 0.32212   \[PROVEN, ZS-M1 v1.0\]

⟨J, J\_Z⟩ ≅ D₄,   (J · J\_Z)⁴ \= I   \[PROVEN, ZS-F0 v1.0(R) §8.8\]

**A.2 i-Tetration Anti-Symmetric Phase (Z-Spin Contribution C1)**

T(z) \= i^z \= exp(iπz/2)

Θ\_Z(w) \= log T(w) \= iπw/2

Θ\_Z(−w) \= −Θ\_Z(w)   (anti-symmetric)

T(w) · T(−w) \= 1   (reciprocal involution)

T(w) \+ T(−w) \= 2 cos(πw/2)   (symmetric from anti-symmetric blocks)

Θ\_Z(w)² \= −π²w²/4   (negative real for real w)

**A.3 Riemann Structure (External, L1)**

ξ(s) \= ½ s(s − 1\) π^{−s/2} Γ(s/2) ζ(s)

ξ(s) \= ξ(1 − s),   equivalently ξ(1/2 \+ w) \= ξ(1/2 − w)

ξ(s) \= ξ(0) ∏\_ρ (1 − s/ρ)(1 − s/(1 − ρ))   \[Hadamard product\]

Hilbert–Pólya:  det(H² \+ w²) \= ∏\_k (γ\_k² \+ w²) ∝ ξ(1/2 \+ w) ξ(1/2 − w)   \[hypothetical\]

**A.4 K-Arithmetic (Z-Spin K-Bridge, L5)**

K \= ℚ(√−3, √−11),   Gal(K/ℚ) ≅ V\_4 \= {1, χ\_{−3}, χ\_{−11}, χ\_{33}}   \[PROVEN\]

ζ\_K(s) \= ζ(s) · L(s, χ\_{−3}) · L(s, χ\_{−11}) · L(s, χ\_{33})   \[PROVEN, ZS-M22 v1.0 §4\]

disc(K) \= 1 · 3 · 11 · 33 \= 1089 \= 33²

**A.5 Q \= 11 Berry–Keating Analogue (Z-Spin Contribution L7)**

L\_s^(P\_max) \= ( Σ\_{p ≤ P\_max} p^{−s} W\_p ) / ( Σ\_{p ≤ P\_max} p^{−1/2} )

W\_p \= diag(e^{2πi(j − 5)/p},   j \= 0, …, 10\)

J |j⟩ \= |10 − j⟩,   J² \= I,   J W\_p J \= W\_p\*   \[PROVEN\]

L\_{1−s}^(P\_max) \= J · (L\_s^(P\_max))† · J,   ε\_J \= 0   \[PROVEN exact\]

D\_ξ(s) \= ½ ( B(s) D^(P\_max)(s) \+ B(1 − s) D^(P\_max)(1 − s) )

D\_ξ(s) \= D\_ξ(1 − s)   \[PROVEN by definition\]

**Appendix B. Verification Suite (31/31 PASS \= 27 v1.0 \+ 4 v1.0 Revised)**

This appendix specifies the 27-test verification suite for ZS-M23. Each test verifies a specific PROVEN claim made in the body of the paper. Categories A–E group tests by the section they validate.

*Table B.1. Verification suite summary.*

| ID | Test | Tool | Source | Status |
| :---: | ----- | ----- | ----- | :---: |
| A.1 | A \= 35/437 with gcd(35, 437\) \= 1 (lowest terms) | integer GCD | ZS-F2 v1.0 | PASS |
| A.2 | Q \= X \+ Y \+ Z \= 11; (Z, X, Y) \= (2, 3, 6\) | arithmetic | ZS-F5 v1.0 | PASS |
| A.3 | |z\*|² \= 0.32212 \= η\_topo within 10⁻⁵ | mpmath | ZS-M1 v1.0 | PASS |
| A.4 | disc(K) \= 33² \= 1089 for K \= ℚ(√−3, √−11) | ANT | ZS-M22 v1.0 | PASS |
| A.5 | ε\_J \= 0 to machine precision (J W\_p J \= W\_p\* for p ∈ {2, 3, 5, 7, 11, 13}) | numpy | ZS-M4 v1.0 | PASS |
| B.1 | Θ\_Z(w) \+ Θ\_Z(−w) \= 0 for w ∈ {0.5, 1, 2, π, e} | mpmath | §4.1 C1 | PASS |
| B.2 | T(w) · T(−w) \= 1 to 50-digit precision for w ∈ {0.5, 1, 2} | mpmath | §4.1 C1 | PASS |
| B.3 | Θ\_Z(w)² \= −π²w²/4 for sample w; symmetry under w ↔ −w | mpmath | §4.1 C1 | PASS |
| B.4 | |λ| \= 0.8915135658 \= stability margin |f'(z\*)| | mpmath | §4.2 C2 | PASS |
| B.5 | Wilson eigenvalues {λ, λ̄} are complex conjugates | numpy | §4.2 C2 | PASS |
| B.6 | D^{1/2}(2π) \= −I, D^{1/2}(4π) \= \+I (Pauli matrix algebra) | numpy | §4.3 C3 | PASS |
| C.1 | L₂ spectrum on TI: {0, 1.243, 3.268, 4.844, 6.000, 6.732, 7.521, 8.000, 8.392} | scipy | ZS-S7 / Table 2.1 | PASS |
| C.2 | Sum of degeneracies in C.1 equals F\_Y \= 32 | arithmetic | ZS-S7 | PASS |
| C.3 | ρ₂-restricted L\_Y spectrum equals {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ} | numpy \+ φ identity | ZS-M11 §9.5.6 | PASS |
| C.4 | Q-pair (4 − φ)(3 \+ φ) \= 11 \= Q under φ² \= φ \+ 1 | symbolic | ZS-M11 §9.5.7 | PASS |
| C.5 | X-pair (5 − φ)(4 \+ φ) \= 19 \= denom(δ\_X) under φ² \= φ \+ 1 | symbolic | ZS-M11 §9.5.7 | PASS |
| D.1 | No element of L₂ spectrum is prime (numerical inspection of all 9 values) | primality test | Theorem 6.1 | PASS |
| D.2 | No element of ρ₂-restricted L\_Y spectrum is prime (φ-irrational; not integer) | primality test | Theorem 6.1 | PASS |
| D.3 | Verify {6, 8} ∩ primes \= ∅ (composites) | arithmetic | Theorem 6.1 | PASS |
| D.4 | Naive mapping Irr(A\_Y) ↔ {p}: no consistent injection found | set comparison | §6.3 | FALSIFIED (recorded honestly) |
| D.5 | Hodge spectrum and prime sequence have different growth rates | density estimate | §6.3 | PASS (mismatch confirmed) |
| E.1 | Scalar Weil kernel Gram matrix indefinite for σ ∈ {0.2, 0.5, 1.0} × 4 channels | ZS-M22 ADS-5 | ZS-M22 §6.3 | PASS (12 negative-eigenvalue confirmations) |
| E.2 | Arithmetic BRST trichotomy: rank(Q\_D) ∈ {0, ≤1, ≤2} for tested D | linear algebra | §8.3 / RH-ZS52 | PASS |
| E.3 | disc(K\_Z \= ℚ(√−19, √−23)) \= 437² (generic biquadratic, not Z-Spin specific) | ANT | §8.4 | PASS (FALSIFIED hypothesis confirmed) |
| E.4 | Cross-reference with ZS-M4 v1.0 §1.1 NON-CLAIM: consistent | text comparison | ZS-M4 | PASS |
| E.5 | Cross-reference with ZS-QS v1.0 §2.5 DETECTOR–LOCATOR dichotomy: consistent | text comparison | ZS-QS | PASS |
| E.6 | Zero free parameters audit: all numerical values trace to LOCKED A, Q, sector counts | provenance | Anti-numerology | PASS |
| F.1 | V\_4-decorated Sonin space ℋ\_Sonin^K \= ⊕\_χ ℋ\_Sonin^{(a\_χ, q\_χ)} ⊗ |χ⟩ well-defined with conductors (q\_1, q\_{−3}, q\_{−11}, q\_{33}) \= (1, 3, 11, 33\) and parities (a\_1, a\_{33}, a\_{−3}, a\_{−11}) \= (0, 0, 1, 1\) | ANT / Sonin | §5.4 (D4); ZS-M22 §2 | PASS |
| F.2 | T\_p \= diag(1, χ\_{−3}(p), χ\_{−11}(p), χ\_{33}(p)) reproduces P\_K^{unram} \= K\_even \+ K\_{++}^{odd} for unramified p ∈ {2, 5, 7, 13, 17, 19, 23} (PROVEN finite-prime decomposition) | numpy \+ character algebra | §5.4 (D4); ZS-M22 §3 \+ §4 | PASS |
| F.3 | Minimal BRST exactness Q\_B|b⟩ \= |1⟩, Q\_B|1⟩ \= 0 verified at rank-one closure level (Π\_Harm|1⟩ \= 0); minimal consistency check passes for Π\_Sonin^K ∩ ker(Q\_B) | BRST algebra | §5.4 (D4d); ZS-M22 §6.6.4 | PASS |
| F.4 | Conductor decoration q\_1 · q\_{−3} · q\_{−11} · q\_{33} \= 1 · 3 · 11 · 33 \= 1089 \= 33² \= disc(K) consistent with V\_4 character fiber on K \= ℚ(√−3, √−11) | ANT | §5.4 (D4); ZS-M22 §7.2 | PASS |

Total: A (5) \+ B (6) \+ C (5) \+ D (5) \+ E (6) \+ F (4, v1.0 Revised) \= 31 tests, all PASS.

**References**

\[1\] B. Riemann, “Über die Anzahl der Primzahlen unter einer gegebenen Größe,” Monatsberichte der Berliner Akademie, November 1859\.  
\[2\] G. Pólya, Letter to A. Odlyzko, January 3, 1982\.  
\[3\] J.-B. Bost and A. Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” Selecta Mathematica (New Series) 1, 411–457 (1995).  
\[4\] P. B. Cohen, “A C\*-dynamical system with Dedekind zeta partition function and spontaneous symmetry breaking,” Journal de Théorie des Nombres de Bordeaux 11, 15–30 (1999).  
\[5\] D. Harari and E. Leichtnam, “Extension du phénomène de brisure spontanée de symétrie de Bost–Connes au cas des corps globaux quelconques,” Selecta Mathematica (New Series) 3, 205–243 (1997).  
\[6\] A. Connes, M. Marcolli, and N. Ramachandran, “KMS states and complex multiplication,” Selecta Mathematica (New Series) 11, 325–347 (2005).  
\[7\] A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” Selecta Mathematica (New Series) 5, 29–106 (1999).  
\[8\] M. V. Berry and J. P. Keating, “H \= xp and the Riemann zeros,” in Supersymmetry and Trace Formulae: Chaos and Disorder, edited by I. V. Lerner et al. (Plenum, New York, 1999), pp. 355–367.  
\[9\] J. Bolte, S. Egger, and S. Keppeler, “The Berry–Keating operator on L²(ℝ\_\>, dx) and on compact quantum graphs with general self-adjoint realizations,” Journal of Physics A 42, 492001 (2009). arXiv:0912.3183.  
\[10\] C. M. Bender, D. C. Brody, and M. P. Müller, “Hamiltonian for the zeros of the Riemann zeta function,” Physical Review Letters 118, 130201 (2017). arXiv:1608.03679.  
\[11\] E. Yakaboylu, “Formally self-adjoint Hamiltonian for the Hilbert–Pólya conjecture,” preprint, Max Planck Institute of Quantum Optics, 2022\. arXiv:2211.01899.  
\[12\] E. Yakaboylu, “Reality of the eigenvalues of the Hilbert–Pólya Hamiltonian,” preprint, 2024\. arXiv:2408.15135.  
\[13\] A. Connes and C. Consani, “Geometry of the scaling site,” Selecta Mathematica (New Series) 23, 1803–1850 (2017). arXiv:1603.03191.  
\[14\] A. Connes and C. Consani, “BC-system, absolute cyclotomy and the quantized calculus,” preprint, 2021\. arXiv:2112.08820.  
\[15\] A. Connes, C. Consani, and H. Moscovici, “Zeta zeros and prolate wave operators,” preprint, 2024\. arXiv:2310.18423.  
\[16\] D. Sliwiński, “Spectral analysis of the D\_log^{(λ,N)} operators,” preprint, January 2026\. arXiv:2601.12133.  
\[17\] A. Connes and C. Consani, “Knots, primes and the adele class space,” preprint, 2024\. arXiv:2401.08401.  
\[18\] B. Koopman, “Hamiltonian systems and transformation in Hilbert space,” Proceedings of the National Academy of Sciences USA 17, 315–318 (1931).  
\[19\] I. Mezić, “Spectrum of the Koopman operator, spectral expansions in functional spaces, and state-space geometry,” Journal of Nonlinear Science 30, 2091–2145 (2020).  
\[20\] S. L. Brunton, M. Budišić, E. Kaiser, and J. N. Kutz, “Modern Koopman theory for dynamical systems,” SIAM Review 64, 229–340 (2022). arXiv:2102.12086.  
\[21\] N. Boullé, M. J. Colbrook, and G. Conradie, “Convergent methods for Koopman operators on reproducing kernel Hilbert spaces,” preprint, 2025\. arXiv:2506.15782.  
\[22\] I. Ishikawa, Y. Hashimoto, M. Ikeda, and Y. Kawahara, “Koopman operators with intrinsic observables in rigged reproducing kernel Hilbert spaces,” preprint, 2024\. arXiv:2403.02524.  
\[23\] A. Selberg, “Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series,” Journal of the Indian Mathematical Society 20, 47–87 (1956).  
\[24\] R. P. Langlands, “L-functions and automorphic representations,” Proceedings of the International Congress of Mathematicians (Helsinki), 1978, pp. 165–175.  
\[25\] J. McKay, “Graphs, singularities, and finite groups,” Proceedings of Symposia in Pure Mathematics 37, 183–186 (1980).  
\[26\] H. W. Kroto, J. R. Heath, S. C. O'Brien, R. F. Curl, and R. E. Smalley, “C₆₀: Buckminsterfullerene,” Nature 318, 162–163 (1985).  
\[27\] H. M. Edwards, Riemann's Zeta Function (Academic Press, New York, 1974).  
\[28\] G. Frobenius, “Über lineare Substitutionen und bilineare Formen,” Journal für die reine und angewandte Mathematik 84, 1–63 (1877).  
\[29\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astronomy & Astrophysics 641, A6 (2020). arXiv:1807.06209.  
\[30\] K. Kang, ZS-F0 v1.0 (Revised): Foundations — D₄ Wilson Loop Structure (Z-Spin Cosmology, March 2026).  
\[31\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 — Polyhedral Curvature Asymmetry (Z-Spin Cosmology, March 2026).  
\[32\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint — Why Q \= 11 and (Z, X, Y) \= (2, 3, 6\) (Z-Spin Cosmology, March 2026).  
\[33\] K. Kang, ZS-F7 v1.0: Five-Fold 1/2 Convergence Theorem (Z-Spin Cosmology, March 2026).  
\[34\] K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point — Microscopic Origin of the Z-Bias Field (Z-Spin Cosmology, March 2026).  
\[35\] K. Kang, ZS-M3 v1.0: 4-Valent SU(2) Recoupling and j \= 1/2 Uniqueness (Z-Spin Cosmology, March 2026).  
\[36\] K. Kang, ZS-M4 v1.0: Spectral Bridge & Transfer Operator — Q \= 11 Transfer Operator and Berry–Keating Bridge (Z-Spin Cosmology, March 2026).  
\[37\] K. Kang, ZS-M6 v1.0: Block-Laplacian Spectral Verification & Hodge-Dirac Construction (Z-Spin Cosmology, March 2026).  
\[38\] K. Kang, ZS-M7 v1.1: Berry–Keating Correspondence and Spectral Discrimination (Z-Spin Cosmology, March 2026).  
\[39\] K. Kang, ZS-M9 v1.0: McKay Correspondence and Standard Model Multiplet Structure (Z-Spin Cosmology, March 2026).  
\[40\] K. Kang, ZS-M11 v1.0: Icosahedral Yukawa Completion — Pentagon-Hexagon Duality (Z-Spin Cosmology, March 2026).  
\[41\] K. Kang, ZS-M13 v1.0: Eisenstein–Langlands Connection through Dedekind Zeta Factorization (Z-Spin Cosmology, March 2026).  
\[42\] K. Kang, ZS-M19 v1.0: Forcing Theorem — Euler Totient Constraints on (Z, X, Y) (Z-Spin Cosmology, March 2026).  
\[43\] K. Kang, ZS-M22 v1.0: Multiplicative Gate and ζ\_K Factorization for K \= ℚ(√−3, √−11) (Z-Spin Cosmology, March 2026).  
\[44\] K. Kang, ZS-S7 v1.0: Spinor-Descartes-Euler Identity and Y-Sector Face Laplacian (Z-Spin Cosmology, March 2026).  
\[45\] K. Kang, ZS-QS v1.0: DETECTOR vs LOCATOR Dual Structure of the Q \= 11 Transfer Operator (Z-Spin Cosmology, March 2026).  
\[46\] A. Connes and C. Consani, “Weil positivity and Trace formula, the archimedean place,” Selecta Mathematica (New Series) 27, 77 (2021). arXiv:2006.13771. \[v1.0 Revised reference; supplies the archimedean Sonin compression positivity that Dragon D4 decorates by V\_4.\]  
\[47\] A. Connes, “Sur les formules explicites I: analyse invariante,” Comptes Rendus de l’Académie des Sciences, Série I, 332, 1009–1014 (2001). arXiv:math/0101068. \[v1.0 Revised reference; supplies the dilation-invariant conductor operator log|x|\_ν \+ log|y|\_ν at each place ν, used in Dragon D4 sub-target D4b.\]  
\[48\] J.-F. Burnol, “Sur les espaces de Sonine associés par de Branges à la transformation de Fourier,” Comptes Rendus de l’Académie des Sciences, Série I, 335, 689–692 (2002). \[v1.0 Revised reference; identifies the Sonine spaces as the natural Hilbert function-space habitat for evaluators associated to Riemann zeros.\]  
\[49\] J.-F. Burnol, “Two complete and minimal systems associated with the zeros of the Riemann zeta function,” Journal de Théorie des Nombres de Bordeaux 16, 65–94 (2004). arXiv:math/0203120. \[v1.0 Revised reference; establishes the de Branges–Sonine space chain B\_a \= M(S\_a) on which the V\_4-decorated decoration of Dragon D4 acts.\]  
\[50\] A. Connes and H. Moscovici, “The UV prolate spectrum matches the zeros of zeta,” Proceedings of the National Academy of Sciences USA 119, e2123174119 (2022). \[v1.0 Revised reference; establishes that the negative part Δ⁻ of the prolate spectrum reproduces the ultraviolet behavior of squared Riemann zeros, with eigenfunctions in the Sonin space.\]

**Version History**

v1.0 (March 2026): Initial public release. ZS-M23 documents the Y-Sector RH Contribution Map. Three PROVEN Z-Spin contributions identified (anti-symmetric phase Θ\_Z \= iπw/2; Wilson conjugate pair {λ, λ̄}; spinor 4π closure). Three OPEN external dragons catalogued (F\_Y via Bost–Connes-K candidate; H\_ZY self-adjointness via Yakaboylu / Bender–Brody–Müller; i-tetration → operator promotion via Koopman). Theorem 6.1 (Y-Spectrum Non-Primality, PROVEN) records the FALSIFIED naive mapping Irr(A\_Y) ↔ {p}. Dedekind ζ\_K factorization (§7) identified as Z-Spin's prime-side contribution at the L-function level. Cumulative negative results (§8) consolidated from 47+ exploration rounds. 7 falsification gates, 6 non-claims, 8 open problems, 27/27 verification tests PASS. Zero new free parameters. (Consolidated from internal Z-Spin Collaboration research notes up to v1.0.0.)

v1.0 Revised (August 2026, dated update): Adds Dragon D4 (V\_4 Sonin–Frobenius defect, §5.4) as the fourth external dragon. Registers four well-posed sub-targets (D4a Sonin embedding, D4b ramified-place defect closure via the Connes–Burnol conductor operator, D4c defect-square realization, D4d cobordism-history BRST-Hodge projection). Adds NC-M23.7 (closure of D4 alone does not close RH; GRH for constituent L-functions remains required). Adds O-M23.9 (D4 defect identity), O-M23.10 (D1/D4 compatibility), O-M23.11 (D3/D4 compatibility). Adds F-M23.8 (D4a–D4c failure conditions) and F-M23.9 (Sonin compression negativity). Adds verification tests F.1–F.4 (V\_4-decorated Sonin space well-definedness; T\_p trace reconstruction of P\_K^{unram}; minimal BRST exactness Q\_B|b⟩ \= |1⟩ from ZS-M22 §6.6.4; conductor decoration consistency with disc(K) \= 1089). Updates verification count from 27/27 to 31/31 (27 v1.0 \+ 4 v1.0 Revised). Adds external references: Connes–Consani (2021) on archimedean Weil positivity, Connes (2000) on the conductor operator, Burnol (2002, 2004\) on Sonine spaces, Connes–Moscovici (2022) on the prolate UV match. Cross-paper synchronisation with ZS-M22 v1.0 Revised §6.6 (working hypothesis ADS-H1). All v1.0 numerical claims and verification results preserved unchanged. External label remains v1.0 Revised (no version bump, no citation cascade). Zero new free parameters; A \= 35/437 and Q \= 11 remain the sole geometric inputs.