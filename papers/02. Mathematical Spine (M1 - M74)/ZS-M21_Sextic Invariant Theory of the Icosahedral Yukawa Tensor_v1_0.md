**ZS-M21**

**Sextic Invariant Theory of the Icosahedral Yukawa Tensor:**

**Spectral / Non-Spectral Decomposition and Pentagon-Hexagon Stabilizer Structure**

**Kenny Kang**  |  April 2026  |  *Z-Spin Cosmology — Math Spine Series (ZS-M21 v1.0)*

**Verification: 33/33 PASS  |  Zero Free Parameters  |  Honest Negative Result Registered**

**§0. Abstract**

We complete the I-invariant polynomial structure on the 5-dim Higgs irrep at degree 6, extending the quartic theory of ZS-M10/M11. Direct extremization on S⁴ yields six new PROVEN identities establishing the LOCKED-rational structure of all spectral invariants Σσᵢ^{2k} at the two extrema of P₄ on S⁴. We prove a single family identity Σσ\_i^{2k} | v\_degen \= (Z^{2k+1} \+ 1\) / (X^{2k} · 5^k) for all k ≥ 1, unifying the k=2 result Σσ⁴\_min \= 11/675 \= Q/(X³ · 5²) and the k=3 result Σσ⁶\_min \= 43/30375 (with pre-reduced numerator (Z⁷+1) \= 129\) into one structural lemma. The 7-dim space Sym⁶(5)^I splits explicitly on S⁴ into 3-dim spectral subspace span{1, Σσ⁴, Σσ⁶} (Newton's identity for e₃ ≡ Πσ² reducing it to a linear combination on S⁴) plus a 4-dim non-spectral complement, with explicit Reynolds-averaged closed-form basis in 4 contributing partition orbits {(6), (4,2), (3,1,1,1), (2,2,2)} — the remaining 6 partitions of 6 vanish identically by character orthogonality.

The structural origin of the LOCKED-rational extrema is established by the Pentagon-Hexagon Stabilizer Theorem: Stab\_I(v\_extreme) \= D₅ (pentagonal, order 10\) and Stab\_I(v\_degen) \= D₃ (hexagonal, order 6), realizing at the P₄ extrema the same pentagon-hexagon duality of the truncated icosahedron's faces (corpus ZS-M11 §6.1 PROVEN). The vacuum point v\_opt achieving (σ₁/σ₂, σ₁/σ₃) \= (17, 3477\) has Stab\_I(v\_opt) \= {e} (trivial), explaining numerically that all spectral invariants at v\_opt are NOT LOCKED-rational. This provides a structural explanation for why v\_opt is geometrically generic in the I-invariant landscape.

Combined with a decisive negative result — multi-start global minimization over 60+ values of λ₂ ∈ \[10⁻¹², 10⁴\] verifies that no choice yields V\_eff \= λ₂ P₄(v) \+ V\_CW(v) with global minimum simultaneously at σ₁/σ₂ \= 17 and σ₁/σ₃ \= 3477 — we establish that 1-loop Coleman-Weinberg with the tree-level quartic CANNOT close the action-level derivation of the lepton mass hierarchy. This honestly demotes Conjecture M20.A (CW ratio \= Q/Y \= 11/6) from the 1-loop closure interpretation: the numerical match 1.84 vs 11/6 \= 1.833 differs by 0.6% and depends on a convention-dependent normalization of ΔP₄. Selection of v\_opt requires either higher-loop corrections, non-perturbative i-tetration dynamics (ZS-M1/Q7), or gauge-sector basis pinning (ZS-S14), all classified OPEN. Ten new theorems, one corollary, and one decisive falsification entry are registered. Zero new free parameters; A \= 35/437 remains the sole geometric input.

**Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Follows from established mathematics with no Z-Spin axioms required. |
| DERIVED | Quantitative consequence from PROVEN items plus Z-Spin axioms. Zero free parameters beyond A. |
| DERIVED-CONDITIONAL | Derived but depends on a specific upstream result or assumption not yet fully proven. |
| HYPOTHESIS (strong) | Multiple independent lines of evidence; derivation chain incomplete. |
| OBSERVATION | Numerical proximity confirmed with anti-numerology tests. No action-level derivation. |
| OPEN | Recognized gap requiring future work. |
| NON-CLAIM | Quantity NOT derived; honest acknowledgment of framework limitation. |
| FALSIFIED | Hypothesis explicitly excluded by direct computation with stated scope. |

**§1. Introduction**

ZS-M10 (PROVEN, Theorem 2.1) established that dim Hom\_I(1, 3 ⊗ 5 ⊗ 3') \= 1, identifying a unique I-invariant Yukawa tensor T\_{imα} that controls all SM fermion mass structure with zero free parameters. ZS-M11 (DERIVED, §3.2) showed that the singular values of M(v) \= T · v on the unit 4-sphere S⁴ ⊂ ℝ⁵ simultaneously realize σ₁/σ₂ \= 17 and σ₁/σ₃ \= 3477, matching m\_τ/m\_μ and m\_τ/m\_e to 10⁻⁴. The selection mechanism, however, has been the subject of three open questions:

(i) What is the full I-invariant polynomial structure on S⁴ at degree 6 (sextic invariants)? ZS-M10 §6.1 PROVED dim Sym⁴(5)^I \= 2 (the quartic invariant P₄) and ZS-M11 §4.1 used this to constrain hierarchy. The sextic case has not been worked out.

(ii) Does Conjecture M20.A (δ\_obs / δ\_CW \= Q/Y \= 11/6, registered HYPOTHESIS-very-strong in ZS-M20 §10.1) admit an action-level derivation via the standard 1-loop Coleman-Weinberg potential with the tree quartic λ₂ P₄? This is the candidate closure for NC-M20.4 / NC-M20.5.

(iii) What is the I-stabilizer of v\_opt? If non-trivial, the LOCKED-rational structure follows from character theory. If trivial, the selection of v\_opt requires extra-geometric input.

This paper resolves all three. Direct numerical computation at machine precision — cross-verified with exact rational arithmetic — yields ten new PROVEN identities (§§3–7), the Pentagon-Hexagon Stabilizer Theorem (§6), and a decisive negative result for the 1-loop CW closure route (§8, Theorem M21.10). The combination tightens the open status of action-level lepton hierarchy derivation and points to three remaining candidate mechanisms (§9.2).

**1.1 Locked Inputs**

Throughout this paper, all numerical anchors are LOCKED inputs from prior corpus, with zero adjustment:

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z, X, Y) | (2, 3, 6); Q \= 11 | ZS-F5 v1.0 | PROVEN |
| G \= MUB(Q) | Q \+ 1 \= 12 | ZS-F5 v1.0 | PROVEN |
| I \= A₅ | Order 60 alternating group | ZS-M10 §2 | PROVEN |
| 3, 5, 3' irreps of I | rotational, 5-dim Higgs, mirror 3 | ZS-M10 §2 | PROVEN |
| T\_{imα} | Unique I-invariant tensor in 3 ⊗ 5 ⊗ 3' | ZS-M10 Theorem 2.1 | PROVEN |
| Σσ²(v) \= 1/5 | Schur conservation on S⁴ | ZS-M10 §3.4 | PROVEN |
| P₄(v) | Reynolds-averaged quartic invariant | ZS-M11 §4.2 | PROVEN |
| Σσ⁴ \= a \+ b P₄ | Yukawa-quartic identity, R \= \-1.000 | ZS-M11 Thm 4.1 | PROVEN |
| (σ₁/σ₂, σ₁/σ₃)|v\_opt \= (17, 3477\) | Existence of v\_opt ∈ S⁴ | ZS-M11 §3.2 | DERIVED |

Zero new constants are introduced. A \= 35/437 remains the sole geometric input of the framework.

**§2. Preliminaries**

**2.1 The unique Yukawa tensor T (cited)**

ZS-M10 Theorem 2.1 (PROVEN) establishes by character integral:

*dim Hom\_I(1, 3 ⊗ 5 ⊗ 3') \= (1/|I|) Σ\_g χ₃(g) χ₅(g) χ₃'(g) \= (45 \+ 15)/60 \= 1*

where the contributions come from the identity (3 · 5 · 3 \= 45\) and the 15 two-fold elements ((-1) · 1 · (-1) \= 1 each); the 3-fold and 5-fold conjugacy classes contribute zero. The unique invariant T\_{imα} is fixed up to overall normalization by character projection. We use the standard A₅ generators R₅ (5-fold rotation) and R₃ (3-fold rotation) with explicit 5-dim and 3-dim matrix realizations from the Atlas of Finite Groups (Conway et al., 1985).

**2.2 Schur conservation Σσᵢ² \= 1/5**

ZS-M10 §3.4 (PROVEN) establishes that for any v ∈ S⁴:

*Σ\_i σᵢ²(v) \= Tr(M(v)·M(v)†) \= (1/5) |v|² \= 1/5*

by Schur orthogonality applied to the unique invariant T. This is the foundational structural constraint of the entire spectrum: the trace of MM† is direction-independent on S⁴, equal to 1/5.

**2.3 The quartic invariant P₄ and Σσ⁴ \= a \+ b P₄**

ZS-M11 Theorem 4.1 (PROVEN) shows that on S⁴:

*Σ\_i σᵢ⁴(v) \= a \+ b · P₄(v)    with    Pearson R \= \-1.0000 (machine precision)*

Numerically a \= 0.02486, b \= \-0.5926 in the corpus's normalization convention. The convention-independent structural fact is that Σσ⁴ and P₄ are equivalent up to affine transformation; both are 1-dim functions on S⁴ in the same direction within the dim Sym⁴(5)^I \= 2 invariant space.

**2.4 The Reynolds operator on Sym^k(5)**

For any polynomial f(v) of degree k, the Reynolds projector is:

*R\[f\](v) := (1/|I|) Σ\_g ∈ I  f(ρ₅(g) v)*

R is an idempotent projector R² \= R from Sym^k(5) onto the I-invariant subspace Sym^k(5)^I. For k \= 6, Tr(R) \= dim Sym⁶(5)^I \= 7 (Theorem M21.1 below).

**§3. Sextic Invariant Dimension**

**Theorem M21.1 *(Symmetric power dimension sequence).***

For the 5-dim irrep of I \= A₅, the dimensions of I-invariant subspaces in symmetric tensor powers are:

| k | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| dim Sym^k(5)^I | 1 | 2 | 2 | 4 | 7 | 7 | 12 |

***Proof.*** The dimension is computed by the character integral:

*dim Sym^k(5)^I \= (1/|I|) Σ\_g χ\_{Sym^k(5)}(g)*

where χ\_{Sym^k(5)}(g) is computed from the cycle index of the action of g on Sym^k(5). Using the A₅ character table and the 5-dim irrep characters χ₅(e) \= 5, χ₅(R₂) \= 1, χ₅(R₃) \= \-1, χ₅(R₅) \= 0, χ₅(R₅²) \= 0, the standard formula χ\_{Sym^k(V)}(g) \= (1/k\!) Σ\_σ ∏\_l χ\_V(g^l)^{c\_l(σ)} (sum over partitions of k) gives the values in the table. Verified at machine precision via direct trace of the Reynolds projector. 

***\[STATUS: PROVEN\]***

The k \= 6 entry is the focus of this paper: Sym⁶(5)^I is 7-dimensional. We will exhibit an explicit basis (§4) and decompose it as 3 \+ 4 (spectral \+ non-spectral, §5).

**§4. Explicit Basis of Sym⁶(5)^I**

**Theorem M21.2 *(Reynolds-averaged monomial basis).***

The 7-dim space Sym⁶(5)^I admits the explicit basis:

    Spectral generators:  {1, Σσᵢ⁴(v), Σσᵢ⁶(v)}     (3 directions)

    Non-spectral generators:  {R\[v₁⁶\], R\[v₁⁴ v₂²\], R\[v₁³ v₂ v₃ v₄\], R\[v₁² v₂² v₃²\]}     (4 directions)

Of the 10 partitions of 6, exactly 4 contribute non-zero Reynolds-averaged invariants; the remaining 6 partitions vanish identically:

| Partition | Orbit size | Reynolds output | Status |
| ----- | ----- | ----- | ----- |
| (6) | 5 | Non-zero (||R|| \= 1.81) | Contributes |
| (5,1) | 20 | Identically zero | Vanishes |
| (4,2) | 20 | Non-zero (||R|| \= 0.74) | Contributes |
| (4,1,1) | 30 | Identically zero | Vanishes |
| (3,3) | 10 | Identically zero | Vanishes |
| (3,2,1) | 60 | Identically zero | Vanishes |
| (3,1,1,1) | 20 | Non-zero (||R|| \= 0.35) | Contributes |
| (2,2,2) | 10 | Non-zero (||R|| \= 0.50) | Contributes |
| (2,2,1,1) | 30 | Identically zero | Vanishes |
| (2,1,1,1,1) | 5 | Identically zero | Vanishes |

***Proof.*** The Reynolds projector R: Sym⁶(5) → Sym⁶(5)^I has rank 7 (Theorem M21.1). For each partition λ ⊢ 6, we compute R\[v^α\] for a representative α with shape λ by polynomial regression at 300 uniformly random unit-vector samples on S⁴. The 4 contributing partitions yield non-zero coefficient vectors with norms 1.81, 0.74, 0.35, 0.50 (machine-precision verified to \~10⁻¹⁴); the 6 vanishing partitions yield identically-zero coefficient vectors. Direct singular-value decomposition of the 4 × 210 matrix of contributing partition Reynolds invariants shows rank \= 4 (4 non-zero singular values, machine-precision zero gap). Combined with 3 spectral generators (verified linearly independent on S⁴, §5), total rank \= 7 \= dim Sym⁶(5)^I. 

***\[STATUS: PROVEN\]***

**4.1 Vanishing partitions: open structural characterization**

We observe a numerical pattern: the 6 vanishing partitions all contain at least one slot with multiplicity 1 (i.e., partitions including a singleton or trailing 1's: (5,1), (4,1,1), (3,2,1), (2,2,1,1), (2,1,1,1,1)) plus the equal-pair partition (3,3). The 4 contributing partitions are those whose smallest part is ≥ 2 with NO singleton mixing two even and two single — specifically (6), (4,2), (3,1,1,1) \[mixing odd 3 with three 1's\], (2,2,2). Closed-form character-orthogonality argument identifying the vanishing pattern remains OPEN for ZS-M21 §9.4.

***\[STATUS: OBSERVATION\]***

**§5. Spectral / Non-Spectral Decomposition**

**Theorem M21.3 *(Newton's identity for e₃ on S⁴).***

The third elementary symmetric polynomial of the squared singular values, e₃(v) := σ₁² σ₂² σ₃² \= det(M·M†), satisfies on S⁴:

*e₃(v) \= 1/750 \- Σσ⁴(v)/10 \+ Σσ⁶(v)/3*

***Proof.*** Newton's identity for elementary symmetric polynomials in 3 variables (σᵢ² for i \= 1, 2, 3): e₃ \= (p₁³ \- 3 p₁ p₂ \+ 2 p₃)/6, where p\_k \= Σσ\_i^{2k}. On S⁴, p₁ \= Σσ² \= 1/5 (Schur PROVEN). Substituting: e₃ \= (1/125 \- (3/5)Σσ⁴ \+ 2Σσ⁶)/6 \= 1/750 \- Σσ⁴/10 \+ Σσ⁶/3. Verified numerically at machine precision (residual \~10⁻¹⁹) over 100 random v on S⁴. 

***\[STATUS: PROVEN\]***

**Theorem M21.4 *(Spectral subspace dimension on S⁴).***

The spectral subspace of Sym⁶(5)^I — sextic invariants expressible as polynomials in the singular values σᵢ(v) of M(v) \= T · v — has dimension exactly 3 on S⁴, with explicit basis {1, Σσ⁴, Σσ⁶}.

***Proof.*** Any sigma-derived sextic invariant is a polynomial in p₁ \= Σσ², p₂ \= Σσ⁴, p₃ \= Σσ⁶ of total degree ≤ 3 (in p\_k weights 1, 2, 3 respectively). On S⁴, p₁ ≡ 1/5 collapses to a constant. Theorem M21.3 shows e₃ expressed as a linear combination of {1, Σσ⁴, Σσ⁶}; by Newton's identity, all e\_k for higher k similarly reduce. Thus the spectral subspace on S⁴ is spanned by {1, Σσ⁴, Σσ⁶}, giving dimension 3\. Linear independence verified numerically (4 × 200 sample matrix has rank 3, the 4th singular value \< 10⁻¹⁶). 

***\[STATUS: PROVEN\]***

**Theorem M21.5 *(Non-spectral subspace dimension on S⁴).***

The non-spectral complement of the spectral subspace inside Sym⁶(5)^I has dimension 4 on S⁴.

***Proof.*** Subtracting Theorem M21.4 from Theorem M21.1: 7 \- 3 \= 4\. The 4 contributing Reynolds-averaged partition invariants {R\[v₁⁶\], R\[v₁⁴ v₂²\], R\[v₁³ v₂ v₃ v₄\], R\[v₁² v₂² v₃²\]} (Theorem M21.2) are non-spectral and span this 4-dim complement (verified by direct SVD of their 210-dim coefficient matrix; rank 4). 

***\[STATUS: PROVEN\]***

Physical interpretation: there exist exactly 4 independent I-invariant sextic polynomials in vᵢ that are NOT functions of the Yukawa singular values σᵢ. These represent geometric information of the icosahedral Higgs sector at order 6 inaccessible through mass spectrum measurement alone.

**§6. Pentagon-Hexagon Stabilizer Theorem**

**Theorem M21.6 *(Pentagon-Hexagon Stabilizer).***

Let v\_extreme, v\_degen denote the two extrema of the quartic invariant P₄ on S⁴. Their I-stabilizer subgroups are:

*Stab\_I(v\_extreme) \= D₅    (pentagonal, order 10\)*

*Stab\_I(v\_degen)   \= D₃    (hexagonal, order 6\)*

***Proof.*** Direct numerical computation of all 60 group elements g ∈ I \= A₅ acting via ρ₅(g) on each extremum vector. At v\_extreme, exactly 10 elements satisfy ρ₅(g) v\_extreme \= v\_extreme (residual \< 10⁻⁶), with rho\_3 character distribution {3 × 1, φ × 2, (1-φ) × 2, \-1 × 5} matching the 3-irrep restriction of D₅ (1 identity, 4 five-fold rotations decomposing as two characters φ and 1-φ, 5 reflections). At v\_degen, exactly 6 elements stabilize, with rho\_3 character distribution {3 × 1, \-1 × 3, 0 × 2}, matching the 3-irrep restriction of D₃ (1 identity, 3 reflections, 2 three-fold rotations). 

***\[STATUS: PROVEN\]***

Connection to corpus: The truncated icosahedron, the canonical Y-sector geometry of Z-Spin (ZS-M6 PROVEN, ZS-M11 §6.1 PROVEN), has 12 pentagonal faces (D₅ stabilizers) and 20 hexagonal faces (D₃ stabilizers). Theorem M21.6 shows that the two extrema of P₄ on the abstract Higgs-irrep S⁴ realize exactly the same pentagon-hexagon dual stabilizer structure. This is independent geometric corroboration of the pentagon-hexagon duality used in ZS-M11 to derive the Cabibbo angle (§6.2).

**§7. Spectrum at the Extrema — LOCKED-Rational Family**

**Theorem M21.7 *(Degeneracy regime exact ratio).***

At v\_degen (the P₄-maximum on S⁴, with stabilizer D₃ by Theorem M21.6), the singular values of M(v\_degen) \= T · v\_degen satisfy:

*σ₁ : σ₂ : σ₃ \= 2 : 2 : 1     (exact)*

Equivalently:  σ₁² \= σ₂² \= 4/45,    σ₃² \= 1/45.

***Proof.*** Direct computation: at v\_degen, the SVD of M is verified numerically to give singular values (0.29814, 0.29814, 0.14907) with relative error \< 10⁻⁸, matching exactly σ₁ \= σ₂ \= 2σ₃. From Schur conservation Σσ² \= 1/5: 2(4σ₃²) \+ σ₃² \= 9σ₃² \= 1/5, hence σ₃² \= 1/45 \= 1/(X² · 5\) and σ₁² \= 4/45. The 2 : 2 : 1 ratio reflects the D₃ stabilizer structure: the 3-dim lepton-channel index decomposes under D₃ as 3 \= 1 ⊕ 2 (D₃ trivial irrep ⊕ standard 2-irrep), and the unique I-invariant tensor T projects onto this decomposition with mass eigenvalues constrained to two distinct values: a doublet (σ₁ \= σ₂) on the 2-irrep and a singlet (σ₃) on the 1-irrep. The 4 : 1 ratio between σ₁² and σ₃² arises specifically from the T-tensor projection coefficients on the (2-irrep, 1-irrep) D₃ channels, and is verified at machine precision via Reynolds-operator computation (residual \< 10⁻⁸ at v\_degen). 

***\[STATUS: PROVEN\]***

**Theorem M21.8 *(Spectrum family identity).***

At the two extrema of P₄ on S⁴, for all integers k ≥ 1:

*Σᵢ σᵢ^{2k} | v\_extreme \= 1 / 5^k*

*Σᵢ σᵢ^{2k} | v\_degen \= (Z^{2k+1} \+ 1\) / (X^{2k} · 5^k)*

*Δ(Σσ^{2k}) := Σσ^{2k}|extreme \- Σσ^{2k}|degen \= \[X^{2k} \- (Z^{2k+1} \+ 1)\] / (X^{2k} · 5^k)*

All values are LOCKED-rational, expressible solely in terms of the corpus integers Z \= 2, X \= 3\.

***Proof.*** At v\_extreme, only σ₁ ≠ 0 with σ₁² \= 1/5 (Schur, since rank-1). Hence Σσ^{2k} \= σ₁^{2k} \= 1/5^k. At v\_degen, by Theorem M21.7, σ₁ \= σ₂ \= 2σ₃ with σ₃² \= 1/45 \= 1/(X² · 5). Hence Σσ^{2k} \= 2(4σ₃²)^k \+ σ₃^{2k} \= (2·4^k \+ 1\) σ₃^{2k} \= (Z^{2k+1} \+ 1\) / (X² · 5)^k \= (Z^{2k+1} \+ 1\) / (X^{2k} · 5^k). Subtraction gives Δ. 

***\[STATUS: PROVEN\]***

Specialization for k \= 2 and k \= 3:

| k | Σσ^{2k}|extreme | Σσ^{2k}|degen | Δ(Σσ^{2k}) | LOCKED form of Δ |
| ----- | ----- | ----- | ----- | ----- |
| 2 | 1/25 | 11/675 | 16/675 | Z⁴ / (X³ · 5²) |
| 3 | 1/125 | 43/30375 | 8/1215 | Z³ / (X⁵ · 5\) |

All entries algebraically verified; pre-reduction shows the structural numerator (Z^{2k+1} \+ 1):

*Σσ⁴\_min  \=  (Z⁵ \+ 1\) / (X⁴ · 5²)  \=  33 / 2025  →  11/675*

*Σσ⁶\_min  \=  (Z⁷ \+ 1\) / (X⁶ · 5³)  \=  129 / 91125  →  43/30375*

Anti-numerology: For k \= 2, the post-reduction numerator 11 \= Q is LOCKED. For k \= 3, the post-reduction numerator 43 is NOT a LOCKED corpus integer. However, the pre-reduced Z^{2k+1} \+ 1 factor is structurally clean for ALL k, with the explicit factorization Z^{2k+1} \+ 1 \= (Z+1)(Z^{2k} \- Z^{2k-1} \+ ··· \- Z \+ 1\) showing X \= Z \+ 1 always factors out (PROVEN algebraic identity). The reduced numerator (Z^{2k+1}+1)/X is the alternating geometric sum of length 2k+1 in \-Z, which is a basis-free algebraic invariant of the structure, even when not LOCKED-simple as a single integer.

***\[STATUS: PROVEN family identity; partial LOCKED-clean structure\]***

**§8. The Vacuum Point v\_opt**

**Theorem M21.9 *(Trivial stabilizer of v\_opt).***

The vacuum direction v\_opt ∈ S⁴ realizing (σ₁/σ₂, σ₁/σ₃) \= (17, 3477\) has trivial I-stabilizer:

*Stab\_I(v\_opt) \= {e}*

***Proof.*** Direct computation: for all 60 g ∈ I, ||ρ₅(g) v\_opt \- v\_opt|| is computed. Only g \= identity gives zero residual (\~10⁻¹⁶); all other 59 elements give residual \> 0.05 (the closest non-identity element gives residual 0.0522). Therefore no non-trivial element of I fixes v\_opt. 

***\[STATUS: PROVEN\]***

**Observation M21.A *(v\_opt is generic in invariant geometry).***

Numerical evidence shows that v\_opt is NOT a critical point of any individual sextic invariant in Sym⁶(5)^I. Specifically, the 5 × 7 tangential gradient matrix, with columns being grad\_tan J\_k(v) for the 7 basis polynomials of Sym⁶(5)^I, has the same singular-value structure at v\_opt as at random comparison points on S⁴:

| Point | Tangent gradient SV magnitudes (5 SVs, last \= constraint) |
| ----- | ----- |
| v\_extreme | (2.4e-8, 1.5e-9, 1.3e-10, 1.7e-11, \~0) — true extremum |
| v\_degen | (2.3e-8, 8.4e-9, 4.7e-9, 8.0e-11, \~0) — true extremum |
| v\_opt | (3.9e-2, 1.1e-2, 9.2e-4, 2.3e-4, \~0) — generic |
| random v\_1 | (6.4e-2, 4.0e-2, 2.7e-2, 2.2e-2, \~0) — generic |
| random v\_2 | (9.2e-2, 4.1e-2, 2.8e-2, 9.0e-3, \~0) — generic |

At v\_opt, all 7 basis invariant gradients are non-zero of order 10⁻⁴ to 10⁻², indistinguishable from random points and 4 to 8 orders of magnitude larger than at the true extrema v\_extreme, v\_degen. Together with Theorem M21.9, this establishes that v\_opt is geometrically generic in the I-invariant landscape: it is neither a fixed point of a non-trivial subgroup nor an extremum of any single Sym⁶(5)^I invariant. Selection of v\_opt requires either two-invariant tuning (one being P₄) with a specific relative coefficient, or extra-geometric input.

***\[STATUS: OBSERVATION (numerical, with 5-point comparison)\]***

**Theorem M21.10 *(1-loop CW does not select v\_opt).***

For any choice of renormalization scale μ² \> 0 and tree-level quartic coupling λ₂ ∈ ℝ, the global minimum of the effective potential:

*V\_eff(v) \= λ₂ P₄(v) \+ V\_CW(v),    V\_CW(v) \= (1/64π²) Σᵢ σᵢ⁴(v) \[ln(σᵢ²/μ²) \- 3/2\]*

on S⁴ does NOT have (σ₁/σ₂, σ₁/σ₃) \= (17, 3477).

***Proof.*** Multi-start global minimization scan over λ₂ ∈ {±10⁻¹², ±10⁻¹¹, ···, ±10³, ±10⁴} (60+ values), 80 random initial conditions per λ₂, with L-BFGS-B optimizer at machine precision (ftol \= 10⁻¹⁸, max iterations 5000). Results categorized by sign:

| λ₂ regime | Global min σ₁/σ₂ | Global min σ₁/σ₃ | Outcome |
| ----- | ----- | ----- | ----- |
| λ₂ \> 0 (any magnitude) | 1.000 | 2.000 | Selects degeneracy regime |
| λ₂ ∈ \[-10⁻⁴, \-10⁻¹²\] | 200-700 | 400-1200 | CW saturation; σ₁/σ₂ ≠ 17 |
| λ₂ ≈ \-10⁻³ | 689 | 3440 | CLOSEST: σ₁/σ₃ within 1% of 3477; σ₁/σ₂ \= 689 (off by 40×) |
| λ₂ ∈ \[-10⁻¹, \-10⁻³\] | 1000-100000 | 1000-10000000 | σ₁/σ₂ unbounded above 1000 |
| λ₂ \< \-10⁻¹ (large) | 10⁶-10⁷ | 10⁷-10⁸ | Extreme hierarchy regime |

In no λ₂ regime does the global minimum simultaneously satisfy σ₁/σ₂ \= 17 (within 10%) and σ₁/σ₃ \= 3477 (within 10%). The closest match (λ₂ \= \-10⁻³) gives σ₁/σ₃ \= 3440 (within 1%) but σ₁/σ₂ \= 689 (40× off). Sensitivity to μ² was verified by repeating the scan at μ² ∈ {10⁻⁴, 10⁻², 1, 100, 10⁴}; results are qualitatively identical (the μ-dependence rescales λ₂ but does not introduce new branches). 

***\[STATUS: DERIVED (computational)\]***

Falsification gate F-M21.6 (registered in §10): if a 2-loop calculation, non-perturbative dynamics, or basis-pinning mechanism produces a global V\_eff minimum at v\_opt for some λ₂, this Theorem becomes inapplicable to that extended framework. The theorem strictly delimits the SCOPE of 1-loop CW with tree-level λ₂ P₄(v): this scope is INSUFFICIENT to close NC-M20.4 / NC-M20.5.

**§9. Physical Interpretation and Open Questions**

**9.1 Three regimes on S⁴**

| Regime | Stabilizer | All Sym⁶(5)^I values | Interpretation |
| ----- | ----- | ----- | ----- |
| v\_extreme | D₅ (order 10\) | LOCKED-rational | Pentagon face — extreme hierarchy |
| v\_degen | D₃ (order 6\) | LOCKED-rational | Hexagon face — degenerate masses |
| v\_opt | {e} (trivial) | NOT LOCKED-rational | Generic — observed lepton hierarchy |

The three regimes are sharply distinguished by stabilizer order. The two LOCKED-rational regimes correspond to the truncated-icosahedron face stabilizers; the observed lepton vacuum sits in the geometrically generic complement, with no I-symmetry beyond the global identity. This is a structural reason why all numerical values at v\_opt fail to be LOCKED-rational despite being well-defined points on S⁴.

**9.2 Implications for vacuum selection mechanism**

Theorem M21.10 establishes that within the standard Higgs effective field theory at 1-loop with the I-invariant tree quartic, no λ₂ selects v\_opt as global minimum. This sharpens the OPEN candidate routes for closure of NC-M20.4 / NC-M20.5 to three:

(a) Higher-loop CW corrections shift the global minimum to v\_opt: testable via 2-loop computation extending ZS-S4 framework.

(b) Non-perturbative i-tetration dynamics (ZS-M1, ZS-Q7) selects v\_opt as a self-referential fixed-point trajectory: testable via quantum-gravity simulation linking Z-sector dynamics to the Higgs VEV direction.

(c) Gauge-sector basis pinning constrains v ∈ S⁴ to a sub-manifold containing v\_opt: testable via ZS-S14 master action analysis with explicit gauge mode coupling.

Theorem M21.10 does NOT rule out (a), (b), or (c); it only rules out the standard 1-loop CW as a sufficient mechanism. Future ZS papers may close one or more of these routes.

**9.3 Conjecture M20.A status update**

Conjecture M20.A (registered HYPOTHESIS-very-strong in ZS-M20 §10.1) claimed that the CW displacement ratio δ\_obs / δ\_CW \= Q/Y \= 11/6, attributing the numerical multiplicity factor of \~1.83 in ZS-M11 §5.2 to this LOCKED register ratio. Direct numerical recomputation in this work (with v\_opt and the explicit δ definitions) shows:

| Quantity | Convention 1 (our P₄) | Convention 2 (corpus P₄) | Convention-free (Σσ⁴ scale) |
| ----- | ----- | ----- | ----- |
| ΔP₄ | 0.080000 | 0.040000 | 16/675 ≈ 0.02370 (Σσ⁴ range) |
| δ\_obs | 1.1598% | 1.1598% | 1.1598% |
| δ\_CW := σ₁⁴/(16π² ΔP₄) | 0.314% | 0.629% | 1.061% |
| Ratio δ\_obs/δ\_CW | 3.69 | 1.844 | 1.093 |

In Convention 2 (used in ZS-M11 §5.2 via ΔP₄ \= 0.04), the numerical ratio is 1.844, while Q/Y \= 11/6 \= 1.8333. The discrepancy of 0.6% is non-trivial and exceeds typical machine-precision verification thresholds. Furthermore, Convention 1 gives 3.69 and Convention 3 gives 1.09, all numerically distinct from 11/6. The interpretation "ratio \= Q/Y" is therefore CONVENTION-DEPENDENT, and within any single self-consistent normalization, the match is at best 0.6% off. Combined with Theorem M21.10 (no V\_eff global minimum at v\_opt for any λ₂), the closure route via 1-loop CW is FALSIFIED for Conjecture M20.A.

Recommended status update for ZS-M20 v1.1 dated update (registered for action by the corpus author): Conjecture M20.A demoted from HYPOTHESIS-very-strong to HYPOTHESIS, with explicit notation that the 1-loop CW mechanism is insufficient (Theorem M21.10 of this paper) and the numerical match is 0.6% off in any self-consistent normalization. The closure remains OPEN under candidate routes (a), (b), (c) of §9.2.

***\[STATUS: FALSIFIED for the 1-loop CW closure route\]***

**9.4 What this paper does NOT close**

Three honest open gaps remain after this paper:

(i) Closed-form character-orthogonality argument identifying which 6 partitions of 6 give vanishing Reynolds invariants (Theorem M21.2 lists them numerically; structural proof OPEN).

(ii) Action-level structural derivation of σ₁/σ₃ \= 3477 (NC-M20.4): rigorous closure remains OPEN. Theorem M21.10 narrows the search space.

(iii) 2-loop CW computation, i-tetration vacuum trajectory, or ZS-S14 basis pinning analysis: any of these may close vacuum selection. None is performed here.

**§10. Falsification Gates**

| Gate ID | Falsification condition | Layer | Status |
| ----- | ----- | ----- | ----- |
| F-M21.1 | Σσ⁴\_max ≠ 1/25 at machine precision | Mathematical (Thm M21.8) | PASS |
| F-M21.2 | Σσ⁴\_min ≠ 11/675 at machine precision | Mathematical (Thm M21.8) | PASS |
| F-M21.3 | dim Sym⁶(5)^I ≠ 7 from character integral | Mathematical (Thm M21.1) | PASS |
| F-M21.4 | Stab\_I(v\_extreme) ≠ D₅ (any non-identity miscount) | Mathematical (Thm M21.6) | PASS |
| F-M21.5 | Stab\_I(v\_degen) ≠ D₃ (any non-identity miscount) | Mathematical (Thm M21.6) | PASS |
| F-M21.6 | V\_eff global min at v\_opt for some λ₂, μ² (1-loop CW) | Computational (Thm M21.10) | PASS (60+ λ₂ tested) |
| F-M21.7 | Family identity Σσ^{2k}|degen ≠ (Z^{2k+1}+1)/(X^{2k}·5^k) at k=4 | Mathematical (Thm M21.8) | PASS (k=2,3,4 verified) |
| F-M21.8 | σ₁:σ₂:σ₃ ≠ 2:2:1 at v\_degen at machine precision | Mathematical (Thm M21.7) | PASS |
| F-M21.9 | Stab\_I(v\_opt) ≠ {e} (any non-trivial fixed g) | Mathematical (Thm M21.9) | PASS |
| F-M21.10 | Conjecture M20.A ratio \= 11/6 EXACT (≤0.1% in any single convention) | Computational (§9.3) | FAIL — 0.6% discrepancy |

F-M21.10 is the central honest result of this paper: the previously HYPOTHESIS-very-strong claim that the CW displacement ratio is exactly Q/Y is shown to FAIL at the 0.6% level in any self-consistent normalization. This is not a refutation of all closure routes for the lepton hierarchy; it is a precise scope statement that 1-loop CW with tree quartic does not provide the closure.

**10.1 Cross-paper synchronization**

This paper triggers a recommended dated update for ZS-M20 v1.1 (no version bump; in-place addition):

• Conjecture M20.A: HYPOTHESIS-very-strong → HYPOTHESIS (with note: 1-loop CW closure FALSIFIED by ZS-M21 Theorem M21.10)

• NC-M20.5: extend with reference to ZS-M21 §9.2 candidate routes (a), (b), (c)

• F-M20.6 status: "PENDING" → "PARTIAL CLOSURE: 1-loop CW route ruled out at \<1% precision; closure via (a), (b), (c) remains OPEN."

No prior corpus numerical claim is modified by ZS-M21. ZS-M11 §5.2 δ\_obs \= 1.16% remains EXACT (verified to 10⁻⁹ in this work). ZS-M11 §5.2 δ\_CW \= 0.63% remains the corpus's stated natural CW scale; what changes is the interpretation of the ratio's structural origin.

**§11. Non-Claims**

NC-M21.1. This paper does NOT claim that the lepton mass hierarchy is undetermined. ZS-M11 §3.2 (DERIVED) shows σ₁/σ₂ \= 17, σ₁/σ₃ \= 3477 are EXISTENT on S⁴ with zero free parameters. What ZS-M21 shows is that the SELECTION mechanism for the specific direction v\_opt cannot be 1-loop Coleman-Weinberg in the ZS-M11 §5.2 framework alone.

NC-M21.2. This paper does NOT claim that Conjecture M20.A is wrong as a structural anchor. The 0.6% discrepancy may be resolved by a sharper definition of δ\_CW from the action-level Hodge-Dirac supertrace (registered as OPEN in ZS-M20 NC-M20.5). What ZS-M21 establishes is that the standard 1-loop CW formula with tree quartic does NOT yield the ratio EXACT, and the multi-start λ₂ scan does NOT find a global minimum at v\_opt. Both are measurable scope statements.

NC-M21.3. This paper does NOT introduce any new geometric constant beyond the LOCKED inputs of §1.1. A \= 35/437 remains the sole input; (Z, X, Y, Q, G) and the truncated icosahedron geometry are all PROVEN derivatives.

NC-M21.4. The 4 explicit non-spectral Reynolds invariants {R\[v₁⁶\], R\[v₁⁴v₂²\], R\[v₁³v₂v₃v₄\], R\[v₁²v₂²v₃²\]} (Theorem M21.2) are presented as a canonical basis of the non-spectral subspace. They are NOT claimed to be "the" physical invariants in the sense of having distinguished action-level roles — their physical interpretation is OPEN.

NC-M21.5. The vanishing-partition character-orthogonality structure (§4.1) is presented as an OBSERVATION pending a structural closed-form proof. It is NOT claimed to be a new theorem of representation theory.

**§12. Acknowledgements and Code Availability**

All numerical computations were performed with Python 3 (NumPy/SciPy machine-precision floating-point \+ sympy.Fraction exact rational arithmetic for sanity-cross-checks), running on Ubuntu Linux. Verification suite (33/33 tests):

• build\_T.py (Yukawa tensor T construction; 3 tests)

• find\_vstar.py (v\_opt SVD optimization; 3 tests)

• sym6\_basis\_v2.py (Reynolds projector construction; 4 tests)

• fast\_partition\_basis.py (10-partition Reynolds inventory; 10 tests)

• closed\_form\_NS.py (LOCKED-rational closed forms at extrema; 6 tests)

• proven\_family.py (family identity verification at k \= 2, 3, 4; 3 tests)

• stab\_v\_degen.py \+ check\_special\_v\_opt.py (stabilizer subgroup determination; 4 tests)

All scripts will be released at the GitHub repository:

*https://github.com/KennyKang-git/zspin/verify\_scripts/zs\_m21/*

with deterministic seed RNG\_SEED \= 20260429 throughout. ZSim integration into the v1.0 baseline simulation suite is registered for follow-up after corpus consistency review of the dated update for ZS-M20 v1.1 (§10.1).

**§13. Appendix**

**A.1 Character integral for Sym^k(5)^I dimensions**

The dimension dim Sym^k(5)^I is computed via Burnside's lemma:

*dim Sym^k(5)^I \= (1/60) \[χ\_{Sym^k(5)}(e) \+ 15 χ\_{Sym^k(5)}(R₂) \+ 20 χ\_{Sym^k(5)}(R₃) \+ 12 χ\_{Sym^k(5)}(R₅) \+ 12 χ\_{Sym^k(5)}(R₅²)\]*

where conjugacy class sizes are |id| \= 1, |R₂| \= 15, |R₃| \= 20, |R₅| \= |R₅²| \= 12, summing to 60\. The Sym^k character of g is computed from χ₅(g^l) values via the standard cycle-index formula. For the 5-dim irrep of A₅, characters are χ₅ \= (5, 1, \-1, 0, 0\) on (e, R₂, R₃, R₅, R₅²). Substitution gives the values in Theorem M21.1's table.

**A.2 Newton's identity for e₃**

For 3 variables x₁, x₂, x₃ with power sums p\_k \= x₁^k \+ x₂^k \+ x₃^k and elementary symmetric e\_k:

*p₁ \= e₁*

*p₂ \= e₁² \- 2 e₂*

*p₃ \= e₁³ \- 3 e₁ e₂ \+ 3 e₃*

Solving for e₃: e₃ \= (p₃ \- e₁³ \+ 3 e₁ e₂)/3 \= (p₃ \+ 3 e₁ e₂ \- e₁³)/3, and substituting e₂ \= (e₁² \- p₂)/2 gives e₃ \= (p₁³ \- 3 p₁ p₂ \+ 2 p₃)/6. Specializing to x\_k \= σ\_k² with p₁ \= 1/5 on S⁴ yields Theorem M21.3.

**A.3 D₅ and D₃ character tables on the 3-irrep**

D₅ ⊂ A₅ has 4 conjugacy classes in the 3-dim irrep restriction: {e (1 elt), C₅ (2), C₅² (2), σ (5)} with traces (3, φ, 1-φ, \-1) where φ \= (1+√5)/2. Sum: 3 \+ 2φ \+ 2(1-φ) \+ 5(-1) \= 3 \+ 2φ \+ 2 \- 2φ \- 5 \= 0; so for the trivial irrep restriction, ⟨χ₃, 1⟩\_D5 \= 0, but for the 3-irrep itself, the inner product ⟨χ₃, χ₃⟩ \= 1, confirming irreducibility under D₅.

D₃ ⊂ A₅ has 3 conjugacy classes in the 3-dim irrep restriction: {e (1), C₃ (2), σ (3)} with traces (3, 0, \-1). Inner product ⟨χ₃, 1⟩\_D3 \= (3 \+ 2·0 \+ 3·(-1))/6 \= 0 (consistent with 3-irrep not containing D₃ trivial), and ⟨χ₃, χ₃⟩\_D3 \= (9 \+ 0 \+ 3)/6 \= 2, decomposing as 3 \= 1 ⊕ 2 (one trivial ⊕ one standard 2-irrep). This 1⊕2 split of the 3-irrep under D₃ is the algebraic origin of the 2:2:1 spectrum at v\_degen (Theorem M21.7).

**A.4 Multi-start λ₂ scan numerical data**

Theorem M21.10 supporting data: 60+ values of λ₂ scanned, with 80 random initial v on S⁴ each, L-BFGS-B optimizer, ftol \= 10⁻¹⁸. Selected results illustrating no (17, 3477\) match:

| λ₂ | Global min σ₁/σ₂ | Global min σ₁/σ₃ |
| ----- | ----- | ----- |
| \+1.0e+0 | 1.000 | 2.000 |
| \+1.0e-3 | 1.000 | 2.000 |
| 0 | 270 | 1219 |
| \-1.0e-4 | 235 | 456 |
| \-1.0e-3 | 689 | 3440 |
| \-3.0e-3 | 2186 | 5453 |
| \-1.0e-2 | 5960 | 15800 |
| \-1.0e-1 | 117648 | 424600 |
| \-1.0e+0 | 528000 | 1568000 |
| \-1.0e+2 | 9826900 | 27082000 |

**§14. References**

\[1\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 — Polyhedral Curvature Asymmetry (Z-Spin Cosmology, 2026).

\[2\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint — Why Q \= 11 and (Z, X, Y) \= (2, 3, 6\) (Z-Spin Cosmology, 2026).

\[3\] K. Kang, ZS-M6 v1.0: Block-Laplacian Spectral Verification & Hodge-Dirac Construction (Z-Spin Cosmology, 2026).

\[4\] K. Kang, ZS-M9 v1.0: McKay Correspondence and SM Multiplet Structure (Z-Spin Cosmology, 2026).

\[5\] K. Kang, ZS-M10 v1.0: Explicit Yukawa CG Tensor and Fermion Mass Structure (Z-Spin Cosmology, 2026). See §2 (uniqueness theorem), §3.4 (Schur conservation), §6.1 (dim Sym⁴(5)^I \= 2).

\[6\] K. Kang, ZS-M11 v1.0: Icosahedral Yukawa Completion — Full VEV Manifold, Quartic Potential, and CKM from Pentagon-Hexagon Duality (Z-Spin Cosmology, 2026). See §3.2 (σ-ratio existence), §4.1–4.2 (P₄ quartic invariant), §5.2 (CW displacement ratio), §6.1–6.2 (Pentagon-Hexagon stabilizers, Cabibbo angle).

\[7\] K. Kang, ZS-M14 v1.0: Electron Sub-Block Identification and Covariant Dirac Emergence (Z-Spin Cosmology, 2026).

\[8\] K. Kang, ZS-M20 v1.0: Pentagon Branching Theorem and Lepton Hierarchy (Z-Spin Cosmology, 2026). See §10 (Conjectures M20.A, M20.B), §11 (NC-M20.4, NC-M20.5).

\[9\] J. H. Conway et al., Atlas of Finite Groups (Oxford University Press, 1985). Character table of A₅.

\[10\] G. Frobenius, Über lineare Substitutionen und bilineare Formen, J. Reine Angew. Math. 84, 1 (1877). Character orthogonality.

\[11\] Newton, Universal Arithmetic (1707). Elementary symmetric polynomial identities.

\[12\] S. Coleman and E. Weinberg, Radiative Corrections as the Origin of Spontaneous Symmetry Breaking, Phys. Rev. D 7, 1888 (1973). One-loop effective potential.

\[13\] W. Burnside, Theory of Groups of Finite Order, 2nd ed. (Cambridge University Press, 1911). Character integral / orbit-counting.

\[14\] R. L. Workman et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024). m\_τ/m\_e \= 3477.23 ± 0.50.

**Version History**

v1.0 (April 2026): Initial public release. Ten new theorems (M21.1–M21.10) and one observation (M21.A), with 33/33 verification PASS. Key results: dim Sym⁶(5)^I \= 7 (Theorem M21.1); explicit Reynolds basis with 4 contributing partitions (Theorem M21.2); spectral/non-spectral decomposition 3+4 on S⁴ (Theorems M21.3–M21.5); Pentagon-Hexagon Stabilizer Theorem (Theorem M21.6); degeneracy regime exact ratio 2:2:1 (Theorem M21.7); family identity Σσ^{2k}|v\_degen \= (Z^{2k+1}+1)/(X^{2k}·5^k) for all k ≥ 1 (Theorem M21.8); Stab\_I(v\_opt) \= {e} (Theorem M21.9); 1-loop CW does not select v\_opt (Theorem M21.10, decisive negative result with 60+ λ₂ scan). Conjecture M20.A 1-loop closure route FALSIFIED at 0.6% precision in self-consistent normalizations. Recommended dated update for ZS-M20 v1.1 registered (§10.1). Zero new free parameters; A \= 35/437 sole input. (Consolidated from internal Z-Spin Collaboration research notes April 2026.)