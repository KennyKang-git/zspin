**ZS-S26**  
**The Cellular Gravitational Instrument and the Homotopy Provenance Bridge**

***Conditional ZS-S14 Interface Reduction, a Nondegenerate Cellular Dreibein, Dissection-Certified Defect Holonomies, the Multiplicity-Algebra Obstruction, and the Strict Six-Dimensional Gauge–Gravity Verdict***

Author: Kenny Kang  
Affiliation: Z-Spin Cosmology Collaboration  
Date: July 2026  
Theme / Paper Code: Standard Model — ZS-S26  
Version: v1.8 FINAL (supersedes v1.7–v1.0, July 2026). Carries three self-retractions, S26-R1, S26-R2, S26-R3, and one derivation correction, S26-C1.  
Companion: zs\_s26\_verify\_v1\_8.py — one self-contained file, numpy \+ scipy only.  
Parents: ZS-S14 v2.0; ZS-S20 v2.2; ZS-S21 v1.2; ZS-S23 v1.3; ZS-S24 v1.9; ZS-S25 v2.1.  
Locked corpus data consumed without refit: **A** \= 35/437, **Q** \= 11, dim Z \= 2, λ₁ \= 1.2428416164, λ\_h \= 7.5210904061, c₁ \= 0.3515993958, (V, E, F) \= (60, 90, 32), χ \= 2, δ\_v \= π/15, α\_s \= 11/93, λ\_vac \= 2A².

**Verification: 112/112 executable checks PASS | 0 FAIL | 3 declarations, never counted as PASS**

**Gate registry, four disjoint classes, identical in this document and in the companion: 3 FIRED | 2 executed-and-not-fired | 7 unresolved research OPEN | 6 permanent integrity guards**

**Zero Free Parameters | A \= 35/437, Q \= 11, dim Z \= 2, λ₁, λ\_h all LOCKED and none re-fitted | Ledger identifiers 112/112 unique, enforced at run time | Literal-True, or-True and tautological short-circuits across 100 paren-balanced check sites: 0, enforced at run time | SHA256(companion) \= dce55c71bb93903796df467efa21b8d1ea9cea19b1ebc8fbb927721fbd21de8a**

*Note on dating. The ZS-S26 template carries March 2026 as its metadata example. This paper is dated July 2026 because its immediate parents ZS-S24 v1.9 FINAL, ZS-S25 v2.1 and the integrated seed report v1.1 are all dated July 2026, and a paper cannot predate the handover it executes. The deviation follows the precedent recorded in ZS-S19 v1.6 and is stated here rather than silently applied.*

# **§0. Abstract**

Retraction notice. Versions 1.3 onward carry three self-retractions against its own v1.0–v1.2 and rescopes the verdict accordingly. S26-R1: the argument that W₆, being an eigenspace of a positive Laplacian, is a minimal L∞ model with **Q** \= 0 — and hence that no ℓ₃ could absorb the Jacobiator — is FALSE; a positive Hessian eigenspace is not the cohomology of a BRST differential. Theorem S26.C4 and the claim \[J₆\] ≠ 0 are WITHDRAWN. S26-R2: the transverse reduction used the Z-anchor value |Φ| \= 0 to set the non-minimal factor to unity across the whole slab; a codimension-one reduction requires the transverse average I\_Φ, not a point value, and the v1.2 coupling was one endpoint of a band quoted as a result. S26-R3: Λ\_eff \= 0 was stated as an output of the parent reduction; it is a necessary compatibility condition on the reduced vacuum term, and whether the parent supplies it has not been computed. What survives, and what version 1.3 strengthens, is stated below.

ZS-S25 established that the finite Z-Spin gauge carrier separates strict closure from strict Jacobi: its six-dimensional cyclic image W₆ \= T₁(λ₁) ⊕ T₁(λ\_h) is product-closed but is not a Lie algebra, with Frobenius Jacobi residual 0.067484, while each three-dimensional projected channel is Lie but not closed. It constructed no gravitational action, no constraint algebra, no physical phase space, no source map and no gravitational coupling. This paper supplies a nondegenerate classical cellular datum, a source normalisation, a phase-space rank and a bounded coupling relation; the parent-vacuum condition and the source-inclusive BV/BFV master equation remain **OPEN**. It also issues three self-retractions against its own earlier versions and one refutation of its own seed.

Certificate P — provenance. The reduction of the ZS-S14 master action to the carrier is declared, not assumed: it is an interface reduction across the Z-sector, licensed by the corpus's own postulate Z \= ∂X (ZS-Q12 v4.0, O-Q16.12). The transverse measure is not a new scale. It is the Z-anchor Bogomolnyi core width L⊥ \= 1/m\_ρ \= 1/(2A M\_P), with m\_ρ \= √(2λ\_vac) M\_P \= 2A M\_P from ZS-F1 §4.2 and λ\_vac \= 2A² from ZS-U5. The Yang–Mills sector, Weyl invariant in four dimensions, reduces with the bare transverse length and gives g²\_YM,3 \= 2A g₄² M\_P with no undetermined constant. The Einstein sector does not: it is weighted by the transverse form factor I\_Φ \= (1/L⊥)∫dy(1 \+ **A**|Φ|²), so G₃ M\_P \= **A**/(4π I\_Φ), and Lemma S26.P2 bounds it to 1 ≤ I\_Φ ≤ 1 \+ **A**. Versions 1.0 to 1.2 set I\_Φ \= 1 from the anchor value alone; that is retraction S26-R2, and the value of I\_Φ is gate F-S26.P8. Hence

**A**/(4π(1 \+ **A**)) \= 0.005900872  ≤  G₃ M\_P  ≤  0.006373482 \= **A**/(4π).

Theorem S26.P1, rescoped in v1.3. On the static locus the reduced Hamiltonian constraint ²R \= 2Λ\_eff \+ 16πG₃ρ splits, on a piecewise-Euclidean slice with point sources, into a smooth and a singular part. The singular part gives δ\_v \= 8πG₃m\_v, and that half is a derivation: the conical relation is the singular part of the reduced parent constraint and not an imported gravitational dictionary, so seed correction C-S26.4 is discharged. The smooth part gives Λ\_eff \= 0, but as a NECESSARY CONDITION for the carrier configuration to solve the reduced equations, not as an output of the parent. The static hypothesis it needs is however no longer an assumption: §3.3 constructs the cellular dreibein explicitly and shows that every one of the ninety intrinsic edge gluings lies in E(2) with no boost component, so K\_ij vanishes identically. Whether the reduced ZS-S14 vacuum term actually supplies Λ\_eff \= 0 is gate F-S26.P7, and it is **OPEN**. \[**DERIVED-CONDITIONAL**.\]

**A** nondegenerate cellular dreibein, new in v1.3. The imported BV–BFV theorems require a nondegenerate triad as input, and v1.2 supplied only holonomies. The developing map of §5 supplies the triad: on each of the thirty-two faces the developed coframe is an orientation-preserving isometry, so det e \= \+1 exactly and e is nondegenerate uniformly; all ninety intrinsic edge gluings lie in E(2) \= SO(2) ⋉ ℝ², so ω is metric and torsion-free and K\_ij ≡ 0; and the ordered frame rotation around every vertex is π/15 to 5.1 × 10⁻¹⁴, so F\[ω\] is a sum of exactly sixty delta-curvatures. The pair (e, ω) therefore realises the ISO(2,1) holonomy with a nondegenerate triad. What is still not built is the master equation WITH the sixty puncture source terms; Certificate G is accordingly **DERIVED-CONDITIONAL**, not POSITIVE, and gate F-S26.G11 records the gap.

Certificate G — the instrument. The cellular BV–BFV gravitational theory is not re-derived; it is **IMPORTED-PROVEN** from Cattaneo, Schiavina and Selliah (2018), who construct an explicit off-shell BV symplectomorphism between three-dimensional triadic gravity and BF theory, and from Cattaneo, Mnev and Reshetikhin (2020), who construct cellular BF theory on CW cobordisms with a quantum master equation, subdivision invariance and Atiyah–Segal gluing. What ZS-S26 supplies is the datum those theorems require and cannot supply: which branch, on which complex, with which source normalization.

Theorem S26.G3′ — the holonomy closure, dissection-certified. The abelianised test R(π/15)^60 \= 1 is automatic and carries no information: with the carrier's own developed vertex positions in an arbitrary order the ordered ISO(2,1) product fails by ‖M − 1‖\_F \= 7.67, a pure translation. The correct object is a Hurwitz system. We construct one intrinsically — the plane tree T\* \= T\_dual ∪ {centre(φ(v)) → v}, whose sixty leaves are exactly the sixty cone points — and read the ordering from its boundary walk. For every one of the thirty-two rooted dissections the ordered product of the carrier-derived defect holonomies equals the identity to ‖M − 1‖\_F ≤ 1.04 × 10⁻¹², with no projection, no fitting and no adjustment. Reversing the deficit sign against the same walk breaks closure by up to 14.78, so the sign of δ is tied to the orientation of the dissection and is not a convention. Gate F-S26.G9 is **CLOSED-PASS**.

Theorem S26.G2 — the seed's own target is refuted. The centraliser of the sixty-holonomy representation in iso(2,1) is one-dimensional and its generator is exactly P₀, the time translation. The generic formula (2g − 2\) dim G \+ Σ dim O\_v \= 228 assumes a trivial stabiliser and therefore does not apply at the Z-Spin point. The correct parabolic rank is

dim H¹\_par \= Σ\_v dim O\_v − 2(dim G − dim Z(ρ)) \= 240 − 2(6 − 1\) \= 230 \= 228 \+ 2 dim Z(ρ).

An independent cross-check confirms it: the static spinless locus has dimension 2N − 2 − 3 \= 115 \= 230/2, exactly half the rank, so it is a LAGRANGIAN CANDIDATE — isotropy is not verified here and the Lagrangian property is non-claim NC-S26.13. With 228 the halving fails. The enhanced stabiliser, the static condition K\_ij \= 0 of §3.3, and the \+2 are one fact seen three ways. That supports the staticity used in Theorem S26.P1; it does NOT remove the branch conditionality, which concerns the reduced vacuum term and remains gate F-S26.P7.

Certificate C — closed negative, and classified. The cyclic cubic vertex on W₆ factorises exactly:

ℓ₂ \= ε ⊗ μ,   \[x ⊗ a, y ⊗ b\] \= (x × y) ⊗ μ(a, b),   residual 1.87 × 10⁻¹⁶,

with μ a symmetric bilinear product on the two-dimensional multiplicity space M. Jacobi holds if and only if μ is associative. The computed μ is not: ‖assoc(μ)‖\_F \= 3.2008 × 10⁻³, reproducing the corpus figure 0.067484 exactly. The obstruction is visible in one explicit component,

Ω := μ₀₀¹ μ₁₁⁰ − μ₀₁⁰ μ₀₁¹ \= 1.364238922615 × 10⁻⁵ ≠ 0,

and the first associativity equation is u₀u₁Ω \= 0, so associativity can be reached only by a degenerate rescaling that annihilates a multiplicity block. Ω is one explicit non-vanishing component of the associator in the selected basis — non-associativity itself is what is basis invariant, and Ω is not claimed to be a GL(2) scalar invariant.

What this does and does not close. It closes the STRICT question: the bracket induced on the six-dimensional active space is not a Lie bracket, for any weight in the admissible orbit family and for both isotypes. It draws NO conclusion about homotopy trivialisation, because the action-level BRST/BV complex, the chain contraction (i, p, h) and the transferred ℓ₃ are not constructed here. The class \[J₆\] is not computed and the v1.2 evaluation of it is withdrawn as S26-R1. The full BV/L∞ double-copy route is therefore **OPEN**, at gate F-S26.C11.

Theorems S26.C5–C6 — the strict route closed, new in v1.1. Version 1.0 left exactly one route by which Certificate C could have been reopened: whether the exact {κ\_p}-weighted Hessian selects some other active space whose μ is associative. That is gate F-S26.C7 and this version closes it. The admissible weights are two orbit ratios, σ \= m₅₆/m₆₆ on the edges and ρ \= β₅/β₆ on the faces, so the reachable family is exactly two-parameter, and the Jacobian of the associator has rank two at each of the four canonical representatives the companion tests, so elementary counting does not exclude a two-parameter family from meeting the associative locus and the question has to be computed. It is. First, the isotypic active space is product-closed for every admissible weight, with leakage below 7 × 10⁻¹⁵ across the whole family, because the isotypic subspace is fixed by symmetry and does not move with the weights. Second, the locus Ω \= 0 is non-empty — Ω changes sign — so the single invariant of Theorem S26.C3 does not by itself suffice. Third, and decisively, on the entire locus Ω \= 0 the second associativity equation is strictly negative,

max E₂ \= −4.78 × 10⁻⁶ (T₁ isotype),   max E₂ \= −7.97 × 10⁻⁷ (T₂ isotype),

over 382 \+ 359 located curve points. Associativity requires E₁ \= E₂ \= E₃ \= 0 simultaneously, so no admissible weight makes μ associative. The third equation E₃ does change sign, so the failure is one named equation and not a diffuse one.

Theorem S26.C6 promoted to **PROVEN**, new in v1.2. Version 1.1 established that sign statement by exhaustive computation and registered gate F-S26.C8 against the absence of a proof. Version 1.2 supplies the proof and the gate is **CLOSED-PASS**. The route is an exact reduction rather than an elimination. Because T₁ and T₂ each occur exactly once in the twelve-pentagon block and once in the twenty-hexagon block, the multiplicity space M has a canonical two-dimensional decomposition in which the whole problem collapses to a 2 × 2 pencil. In that basis the weighted operator is **A**(σ) \= **A**₀ \+ σ**A**₁ against N(ρ) \= diag(ρ, 1), with

**A**₀ \= diag(0, R),   **A**₁ \= \[\[P, **Q**\], \[**Q**, S\]\],   P \= 5,  S \= 3,  R \= 3 ∓ √5,  **Q** \= ∓√(5 ± 2√5),

the upper signs for T₁ and the lower for T₂ — the two isotypes are Galois conjugates under √5 ↦ −√5. The entire cochain cup tensor collapses to four monomials,

Λ\[pp,h\] \= βσ²,   Λ\[ph,h\] \= γσ,   Λ\[hh,h\] \= δ,   Λ\[hh,p\] \= ρ α σ²,   all other entries zero,

verified to 1.8 × 10⁻¹⁷. Separating the eigenvalue normalisation from the cup data by μ\_mn^p \= k\_mn^p/(λ\_mλ\_n) gives closed forms for the two quantities that carry E₂:

P₂ \= −g σ D² y\_A (β σ x\_A \+ γ y\_A),   P₃ \= σ² D² y\_B \[ g β x\_B \+ (βδ − γ²) y\_B \],   g \= α ρ σ²,

with v\_A \= (x\_A, y\_A), v\_B \= (x\_B, y\_B) the N-orthonormal eigenvectors and D their determinant, and E₂ \= (t P₂ \+ P₃)/(λ\_Aλ\_B)² with t \= λ\_B/λ\_A \> 0\. Three exact inequalities then close the sign. Of the three, (I2) and (I3) are rational and take the same value on both isotypes, while (I1) is algebraic and strictly negative for both:

(I1) βδ − γ² \< 0,   (I2) αγ \> 0,   (I3) βγ**Q** \< 0\.

Exact arithmetic, new in v1.3. Version 1.2 obtained these constants by recognising floating-point values, which is evidence and not proof. Version 1.3 recomputes the entire carrier in exact ℚ(√5): the sixty vertices lie in ℤ\[φ\], every edge has length squared exactly 4, all thirty-two faces are certified exactly planar, the pentagon and hexagon blocks are exactly orthogonal, and the structural zeros of **A**₀ and of the cup tensor vanish identically rather than to a tolerance. In the canonical centroid basis

P \= 250 \+ 82√5,   **Q** \= −(170 \+ 74√5),   S \= 210 \+ 90√5,   R \= 60 \+ 20√5,

α \= 122 \+ 54√5,   β \= (166 \+ 66√5)/3,   γ \= (340 \+ 148√5)/3,   δ \= (180 \+ 80√5)/3,

and the three closing invariants are (I1) \= −18760 − (25160/3)√5, (I2) \= (81440 \+ 36416√5)/3 and (I3) \= −(11763520/3) − (15782080/9)√5. Their signs, and the signs of their Galois conjugates, are certified by integer comparisons a² versus 5b² alone. The T₂ isotype needs no separate computation: the face permutation representation is defined over ℚ, so the T₂ isotypic projector is the Galois conjugate of the T₁ one and every T₂ constant is the image under √5 ↦ −√5 of the corresponding T₁ constant. Theorem S26.C6 is therefore **PROVEN** with exact hypotheses, not with recognised floats.

Normalising the two block signs so that β \> 0 and α \> 0 — which is always possible, since β and α flip independently under the two block reflections — (I2) forces γ \> 0 and (I3) forces **Q** \< 0\. **A** sign lemma for the pencil, proved from **A**₁ ≻ 0 and PR \> 0, then gives x\_A, y\_A, x\_B \> 0 \> y\_B: the eigenvector of the smaller eigenvalue has components of one sign and that of the larger has components of opposite signs. Hence βσx\_A \+ γy\_A \> 0 and gβx\_B \+ (βδ − γ²)y\_B \> 0, so P₂ \< 0 and P₃ \< 0, and since t \> 0,

E₂ \< 0 strictly, for every (σ, ρ) ∈ (0, ∞)² and for both isotypes.

Theorem S26.C6 is therefore **PROVEN**, not merely exhaustive, and it is proved on the whole open quadrant rather than on a scanned box or on the locus Ω \= 0 alone.

Fourth, the remaining alternative is settled by Schur's lemma rather than by computation. The four admissible channels of the carrier also allow mixed active spaces T₁(a) ⊕ T₂(b). Because T₁ ⊗ T₂ \= G ⊕ H contains neither T₁ nor T₂, the projected bracket on a mixed space is block diagonal, so every mixed space is a strict Lie algebra so(3) ⊕ so(3) whose multiplicity algebra is ℝ ⊕ ℝ — associative, with Jacobi residual below 1.5 × 10⁻¹⁵. But the same lemma forces the mixed product to leave the space entirely: its leakage is exactly 100 per cent, with a mixed-product norm bounded away from zero, at every weight. The obstruction is representation-theoretic and therefore weight-independent.

Theorem S26.C5 (Closure–Jacobi dichotomy, scoped). Every six-dimensional I-equivariant active space built from the four admissible cubic channels of K\_TI is either isotypic — product-closed and never STRICTLY Lie, for every weight in the two-parameter orbit family — or mixed — a strict Lie algebra and never closed, for every {κ\_p} whatsoever, by Schur. No such space is both. Gate F-S26.C7 is therefore **CLOSED-NEGATIVE** within that scope. This closes the STRICT route only; the homotopy route is untouched, as the retraction notice above records.

Certificate G4 — the coupling. The two sectors reduce with different weights: gravity carries the non-minimal factor and Yang–Mills does not. BOTH G₃ and g²\_YM,3 scale as L⊥⁻¹, so their product scales as L⊥⁻², and the transverse length does NOT algebraically cancel. What removes the free scale is the substitution of the parent-derived width L⊥ \= 1/(2A M\_P), after which

G₃ g²\_YM,3 \= **A**² g₄² / (2π I\_Φ) \= 2 **A**² α\_s(μ) / I\_Φ \= λ\_vac α\_s(μ) / I\_Φ,

where I\_Φ \= (1/L⊥)∫dy(1 \+ **A**|Φ(y)|²) is the transverse form factor. Version 1.2 set I\_Φ \= 1 from the Z-anchor value; that is S26-R2. What can be proved is a two-sided bound. For a minimising interface profile 0 ≤ |Φ| ≤ 1, since replacing ρ by min(ρ, 1\) lowers both the gradient and the potential energy, hence 1 ≤ I\_Φ ≤ 1 \+ **A** and

2A²α\_s/(1 \+ **A**) \= 1.404922557 × 10⁻³   ≤   G₃ g²\_YM,3   ≤   2A²α\_s \= 1.517444958 × 10⁻³.

The band is closed, two-sided, and its fractional width is exactly **A**/(1 \+ **A**) \= 35/472 \= 7.4153 per cent — the residual uncertainty in the gauge–gravity coupling is precisely the geometric impedance. Together with G₃ m\_def \= χ/4N \= 1/120, which is purely geometric and carries no I\_Φ, this gives g²\_YM,3/m\_def ∈ \[0.1685907, 0.1820934\]. Collapsing the band to a point requires the actual transverse profile and is gate F-S26.P8; evaluating α\_s at the reduction scale μ \= 2A M\_P rather than at M\_Z is gate F-S26.N5. Both are named rather than hidden.

Verdict, rescoped in v1.3.

**CLASSICAL CELLULAR GRAVITY REALISATION DERIVED-CONDITIONAL; STRICT SIX-DIMENSIONAL DOUBLE-COPY ACTIVE-SPACE ROUTE CLOSED-NEGATIVE; THE FULL ACTION-LEVEL BV / L∞ BRIDGE AND THE QUANTUM INSTRUMENT REMAIN OPEN.**

Closure levels: G0 POSITIVE; G1 **DERIVED-CONDITIONAL**, since the triad is built but the source-inclusive master equation is not; G2 **DERIVED-CONDITIONAL** on F-S26.P2, P7 and P8; G3a, the strict six-dimensional Lie route, **CLOSED-NEGATIVE** and **PROVEN**; G3b, the full BV/L∞ route, **OPEN**; G4 BANDED to within **A**/(1 \+ **A**). This is not the seed's Outcome B and this version does not claim it. What the paper does establish, and what is new to the corpus, is that on the Z-Spin carrier the gauge sector cannot be made simultaneously product-closed and strictly Lie — by a proof, over the whole admissible weight family, with exact algebraic hypotheses — so if a gauge-theoretic origin of Z-Spin gravity exists at all it is homotopical rather than strict.

*Keywords: cellular BV–BFV, ISO(2,1) Chern–Simons gravity, conical defect, Hurwitz system, developing map, parabolic cohomology, multiplicity algebra, colour–kinematics obstruction, truncated icosahedron, zero free parameters.*

# **Epistemic Status Legend**

**PROVEN** — proved here or in a cited paper from stated hypotheses, machine-checkable. **IMPORTED-PROVEN** — proved in the external literature and applied here without re-proof, full citation given. **DERIVED** — follows from the Z-Spin action plus standard physics with zero free parameters. **DERIVED-CONDITIONAL** — **DERIVED** conditional on a named upstream item or declaration. **VERIFIED** — reproduced numerically by the companion at stated precision on the actual Z-Spin object. **COMPUTED** — a number from an approximate prescription whose error is measured but not rigorously bounded; carries no proof weight. **DECLARATION** — an axiom-level choice, recorded as such, never counted as proof. **TESTABLE** — a falsifiable consequence with a stated gate. **CLOSED-PASS** — a pre-registered gate executed and not fired. **CLOSED-NEGATIVE** — a route terminated by a proved obstruction. **HYPOTHESIS-strong** / **HYPOTHESIS** — motivated conjecture with the missing step named. **OBSERVATION** — an exact identity whose physical necessity is not established. **NON-CLAIM** — explicitly outside the scope. **OPEN** — a well-posed question this paper does not answer. **RETRACTED** — a claim withdrawn with a documented reason. **CONTROL** / **CONFIRMATION** — companion checks; a control tests whether a hypothesis is automatic, a confirmation is a finite check of a statement proved over an infinite range. Neither is evidence for a physical value.

# **§1. Corrections Notice and ZS-S25 Inheritance**

## **§1.1 Corrections carried forward from the integrated seed**

The seven corrections C-S26.1 through C-S26.7 of the integrated seed v1.1 are adopted verbatim and are not restated in full. Their operative consequences for this paper are the following. C-S26.1: three-dimensional Einstein gravity admits a direct first-order BF/Chern–Simons formulation, so a double copy is not necessary to define the gravitational theory; the direct route and the double-copy route are distinct questions and §9 answers only the second. C-S26.2: the phrase 'the ZS-S21 construction with the group changed' is used in this paper only as a heuristic for the 60/90/32 cell census, never as a proof, because ISO(2,1) is non-compact and the SU(3) transfer-matrix positivity theorem does not transfer. C-S26.3: the 540/192/360 census is a census; §6 computes the actual rank. C-S26.4 and C-S26.5 are discharged together by Theorem S26.P1 in §4. C-S26.6: the W₆ result belongs to the compatibility certificate and appears only in §8–§9. C-S26.7: no strict finite cochain algebra is claimed; §8 works with the transferred bracket and states its L∞ status explicitly.

## **§1.2 What is carried forward from ZS-S25 without reopening**

K\_TI is a two-dimensional closed polyhedral complex and K\_TI × a\_t ℤ is a three-dimensional cellular carrier. The projected tensor on each admissible three-dimensional channel is T\_R \= c\_R ε and satisfies Jacobi. The raw three-dimensional channels do not close. The six-dimensional space W₆ closes under the cyclic product with Frobenius-normalised Jacobi residual 0.067484. The exact Wilson quartic is not established as the square of the cubic tensor. The equal-deficit cone geometry is δ\_v \= π/15 with Σδ\_v \= 4π. All of these are re-derived independently by the companion from exact Cartesian coordinates and none is imported as a number.

## **§1.3 One new correction issued by this paper**

C-S26.8 (new). The seed's Target Theorem S26.G2, dim H¹\_par \= 228, is **RETRACTED** as stated. The value 228 is the generic dimension for an irreducible representation with trivial stabiliser. The Z-Spin configuration is spinless and static, its holonomy image lies in E(2) ⊂ ISO(2,1), and every element of E(2) commutes with the time translation P₀. The stabiliser is therefore one-dimensional by necessity and not by accident, and the correct rank is 230\. The seed itself pre-registered this possibility — 'if the symmetric configuration has an enhanced stabiliser, 228 may not be the local dimension at the Z-Spin point' — and this paper reports the actual result rather than forcing the generic formula. Gate F-S26.G6 fires against the seed.

# **§2. Certificate P — the Conditional ZS-S14 Interface Reduction**

## **§2.1 The parent action and the dimension-reduction gate**

The gravitational and scalar sector of the ZS-S14 master action is inherited from ZS-F1 §3.1 in the form

S \= ∫ d⁴x √(−g) \[ ½ M\_P² (1 \+ **A**|Φ|²) R − ½ M\_P² |∂Φ|² − V(Φ) \] \+ S\_m,   V(Φ) \= (λ/4) M\_P⁴ (|Φ|² − 1)²,

together with the Standard Model Yang–Mills terms. The seed requires that one of four reduction options be named explicitly and that none be silently selected. This paper selects option four: a boundary or interface theory induced from the four-dimensional bulk. The selection is not a modelling preference. It is forced by the corpus's own bedrock postulate Z \= ∂X (ZS-Q12 v4.0; O-Q16.12), which states that the Z-sector is the boundary of the X-sector. The carrier K\_TI × a\_t ℤ is therefore the Z-sector worldvolume and the reduction is a codimension-one interface reduction. \[**DECLARATION**, registered as Z-**A**\-R26; its licence is the pre-existing corpus postulate, not a new axiom.\]

## **§2.2 The transverse length is fixed; the transverse form factor remains bounded**

The seed's gate F-S26.P2 fires if the reduced coefficient introduces an undetermined transverse scale. It does not. The Z-anchor is a Bogomolnyi vortex core and its width is fixed by the radial mode mass of the parent action. ZS-F1 §4.2 gives m\_ρ \= √(2λ\_vac) M\_P and ZS-U5 gives λ\_vac \= 2A², hence

m\_ρ \= 2 **A** M\_P,   L⊥ \= 1/m\_ρ \= 1/(2 **A** M\_P) \= 6.24285714 M\_P⁻¹.

Furthermore |Φ(x₀)| \= 0 at the Z-anchor is **PROVEN** topologically from π₁(U(1)) \= ℤ (ZS-F1 §5), so the non-minimal factor evaluated on the interface is

1 \+ **A**|Φ|²|\_{Z-anchor} \= 1\.

What this fixes and what it does NOT fix, corrected in v1.3 and restated here. It fixes the transverse LENGTH: L⊥ is an output of the parent mode spectrum and is not a new scale, so gate F-S26.P2 concerns only the upstream status of λ\_vac \= 2A². It does NOT fix the transverse FORM FACTOR. Versions 1.0 to 1.2 used |Φ(x₀)| \= 0 at the anchor to remove the profile average ⟨|Φ|²⟩; that step is retracted as S26-R2, because a codimension-one reduction weights the Einstein term by the transverse average and not by a point value. The form factor is bounded in §2.5 and its value is gate F-S26.P8.

## **§2.3 The reduced first-order coefficients**

Integrating the Einstein–Hilbert term across the interface gives 1/(16πG₃) \= ½ M\_P² L⊥ I\_Φ, so G₃ \= 1/(8π M\_P² L⊥ I\_Φ). Substituting the parent-derived width L⊥ \= 1/(2A M\_P) of §2.2 — I\_Φ is a transverse AVERAGE and is not eliminated by any point value — this becomes

G₃ M\_P \= **A**/(4π I\_Φ),   so   **A**/(4π(1 \+ **A**)) \= 0.005900872 ≤ G₃ M\_P ≤ 0.006373482 \= **A**/(4π).

The Yang–Mills term √(−g) Tr F ∧ ⋆F is Weyl-invariant in four dimensions and therefore reduces with the bare transverse length and no non-minimal weight, giving 1/g²\_YM,3 \= L⊥/g₄² and

g²\_YM,3 \= g₄² / L⊥ \= 2 **A** g₄² M\_P.

This asymmetry between the two sectors — gravity carries the factor (1 \+ **A**|Φ|²), Yang–Mills does not — is the whole content of §10. It is a property of the parent action, not of the discretisation. \[**DERIVED**. Checks M5.1–M5.5.\]

## **§2.4 What §2 does not do**

The exact face-and-prism integration of ZS-S23 gate F-S23.6 is not performed here. It fixes the values {κ\_p}, a₈⁽⁵⁾ and μ of the ZS-S24 strong-coupling expansion, and none of those quantities enters any statement of this paper. The seed lists that integration among the outputs of Certificate P; this paper reports honestly that it computes G₃ and g²\_YM,3 without it, and that it identifies Λ\_eff \= 0 only as a necessary compatibility condition whose supply by the parent remains **OPEN** at F-S26.P7, and leaves F-S23.6 exactly where ZS-S23 left it. \[**NON-CLAIM** NC-S26.1.\]

## **§2.5 The transverse form factor, Lemma S26.P2, and Retraction S26-R2**

Versions 1.0 to 1.2 evaluated the non-minimal factor at the Z-anchor, where |Φ| \= 0 is a topological theorem, and set it to unity across the whole slab. That is wrong, and correcting it is the most consequential change this line has made. **A** codimension-one reduction does not weight the Einstein term by a point value; it weights it by the transverse average

I\_Φ := (1/L⊥) ∫\_⊥ dy ( 1 \+ **A** |Φ(y)|² ),

so that 1/(16πG₃) \= ½ M\_P² L⊥ I\_Φ and hence G₃ M\_P \= **A**/(4π I\_Φ). The Yang–Mills term, being Weyl invariant in four dimensions, reduces with the bare transverse length and carries no such factor. That asymmetry between the two sectors is a property of the parent action, not of the discretisation, and it is what makes the ratio G₃g²\_YM,3 meaningful at all. Since |Φ| \= 0 holds only at the anchor and |Φ| → 1 in the vacuum, I\_Φ is strictly greater than unity for any profile that leaves the core, and setting it to one is an error of principle rather than of arithmetic.

**Lemma S26.P2 (Form-factor bounds). Let Φ minimise the reduced interface energy with |Φ| \= 0 at the anchor and |Φ| → 1 in the vacuum. Then 0 ≤ |Φ(y)| ≤ 1 pointwise, and consequently**

1 ≤ I\_Φ ≤ 1 \+ **A**.

Proof. Write ρ \= |Φ| and replace ρ by its radial clipping ρ̂ \= min(ρ, 1). The clipping is 1-Lipschitz, so it does not increase the gradient energy ½M\_P²∫(ρ′)²; and wherever ρ \> 1 the potential (λ/4)M\_P⁴(ρ² − 1)² is strictly decreased, since the potential is strictly increasing in ρ on (1, ∞). Hence ρ̂ has strictly lower energy than ρ unless ρ ≤ 1 already, so a minimiser satisfies ρ ≤ 1; and ρ ≥ 0 by definition. The integrand 1 \+ Aρ² is monotone in ρ², so it lies between 1 and 1 \+ **A**, and so does its average.

Two consequences, both carried through §4.2 and §10. First, every quantity that inherits the Einstein normalisation becomes a two-sided band rather than a point, of fractional width exactly **A**/(1 \+ **A**) \= 35/472 \= 7.4153 per cent: the residual uncertainty in the gauge–gravity coupling is precisely the geometric impedance. Second, the v1.0–v1.2 values were the I\_Φ \= 1 endpoint of that band quoted as a result, which is Retraction S26-R2. Collapsing the band to a point requires either the explicit Bogomolnyi transverse profile, or an action-level proof that the reduction is a delta-localised interface rather than a finite-width slab with a separately derived localised Einstein coefficient. Neither is performed here, and the residual is gate F-S26.P8. \[**DERIVED** for the band; the point value is **OPEN**. Checks M11.1–M11.3.\]

# **§3. The Cellular BV–BFV Gravitational Instrument**

## **§3.1 What is imported and what is supplied**

The seed asks ZS-S26 to construct a cellular BF/BV–BFV theory on K\_TI × \[t, t \+ a\_t\], to verify the classical master equation (S\_BV, S\_BV) \= 0 and the nilpotency of the boundary BFV charge, and to prove first-class closure of the constraints. **A** search of the external literature establishes that all four of these are already theorems of the general theory, and that constructing them again inside the corpus would be a duplicate count of the kind ZS-S22 forbade.

Cattaneo, Schiavina and Selliah \[3\] construct an explicit off-shell BV symplectomorphism between the BV formulation of three-dimensional triadic (Palatini–Cartan) gravity and the BV formulation of BF theory, each with its natural symmetries. Canepa, Cattaneo and Schiavina \[4\] extend this to a fully extended BV–BFV description of three-dimensional general relativity and prove strong equivalence. Cattaneo, Mnev and Reshetikhin \[5\] construct cellular BF theory, abelian and non-abelian, on cobordisms equipped with cellular decompositions, prove that partition functions are invariant under subdivision, satisfy a quantum master equation, and satisfy an Atiyah–Segal gluing formula; the non-abelian case is treated in the BV–BFV setting. Taken together these supply, for any CW cobordism, the BULK and SOURCE-FREE cellular BV–BFV framework: the master equation, the boundary BFV charge, subdivision invariance and gluing. Their extension to the sixty puncture source terms, and to the gluing of the source worldlines to the boundary BFV data, is NOT imported and remains **OPEN** at gate F-S26.G11. \[**IMPORTED-PROVEN** for the source-free framework only.\]

K\_TI × \[t, t \+ a\_t\] is a CW cobordism: K\_TI is a finite regular CW complex (60 zero-cells, 90 one-cells, 32 two-cells, verified by the companion at checks M0.1–M0.5) and the product with an interval is a three-dimensional cellular cobordism between two copies of it. The hypotheses of \[5\] are therefore satisfied verbatim, and the master equation, the boundary BFV charge and subdivision control follow without further work.

## **§3.2 What ZS-S26 must therefore supply, and does**

Four data are required by those theorems and are not supplied by them: the gauge algebra, that is the branch; the specific complex; the nondegenerate triad; and the source normalisation. §3.1 supplies the complex and §3.3 the triad, with executable torsion, vielbein-compatibility and temporal-constancy tests. §5 supplies the source normalisation. §4 supplies the branch ONLY as a compatibility condition that the carrier imposes: whether the reduced parent vacuum term delivers Λ\_eff \= 0 is gate F-S26.P7 and it is **OPEN**. Certificate G therefore rests on an imported instrument with three of four Z-Spin data in hand, and closure level G1 is **DERIVED-CONDITIONAL**. \[**DERIVED-CONDITIONAL**, level G1. Gate F-S26.G11 records the missing source-inclusive master equation.\]

Warning carried forward. Nothing in \[3\], \[4\] or \[5\] licenses the compact-group transfer-matrix and reflection-positivity results of ZS-S21 and ZS-S24 for ISO(2,1). Those results are compact-group theorems and ISO(2,1) is non-compact. This is C-S26.2 and it is enforced by §7. \[**NON-CLAIM** NC-S26.2.\]

## **§3.3 The nondegenerate cellular dreibein**

The imported theorems take a nondegenerate triad as input. Versions up to 1.2 supplied only a holonomy representation, which is why an external audit correctly placed Certificate G below its declared level. The triad is in fact already implicit in the developing map of §5, and this section makes it explicit. Nothing here is new computation: it is the body-level statement of what companion module M10 executes.

Construction. Unfold K\_TI along a spanning tree of its dual graph, giving for each face f an isometric chart U\_f into the Euclidean plane. On the face set

e\_f \= ( dt, dU\_f¹, dU\_f² ),

and let ω be the flat connection whose transition across each edge is the intrinsic gluing isometry determined by the shared edge,

U\_f \= R\_fg U\_g \+ t\_fg,   R\_fg ∈ SO(2),  t\_fg ∈ ℝ².

Four properties are then verified by direct computation, each as a separate executable check rather than as an interpretation.

(i) Nondegeneracy. On all thirty-two faces the developed coframe satisfies det e\_f \= \+1 exactly, with orthogonality residual below 10⁻¹⁵. The triad is therefore nondegenerate uniformly and orientation preserving, which is precisely the hypothesis the cellular BF/BV–BFV framework requires. \[Check M10.1.\]

(ii) Metricity and vanishing extrinsic curvature. All ninety intrinsic edge gluings lie in E(2) \= SO(2) ⋉ ℝ² with no boost component, to 9.4 × 10⁻¹⁶. Hence ω is metric and torsion-free, and the extrinsic curvature vanishes identically, K\_ij ≡ 0\. Combined with (iv) below this makes the static condition used in Theorem S26.P1 a property of the construction rather than an assumption. \[Checks M10.2, M10.7.\]

(iii) Discrete torsion and vielbein compatibility. For every face the discrete torsion vanishes,

T\_f \= Σ\_{e ⊂ ∂f} U\_{f←e} e\_e \= 0,   max |T\_f| \= 5.0 × 10⁻¹⁶,

which is the statement that the developed boundary polygon closes; and across every edge the gluing isometry carries the neighbour's coframe exactly onto the face's own, max residual 8.2 × 10⁻¹⁶, which is the vielbein postulate D\_ω e \= 0\. The pair (e, ω) is therefore a genuine Cartan pair and not two independent fields. \[Checks M10.5, M10.6.\]

(iv) Curvature and temporal constancy. The ordered frame rotation around every vertex equals δ\_v \= π/15 to 5.1 × 10⁻¹⁴ and the curvature vanishes on every face interior by construction, so F\[ω\] is a sum of exactly sixty delta-curvatures. Across the temporal prism e\_i(t \+ a\_t) − e\_i(t) \= 0 and ω\_i(t \+ a\_t) − ω\_i(t) \= 0 identically, to machine zero. \[Checks M10.3, M10.7.\]

What this settles and what it does not. The pair (e, ω) realises the ISO(2,1) holonomy of §5 with a nondegenerate triad, so three of the four data the imported framework needs — the complex, the triad, the source normalisation — are now in hand. The fourth is not: the cellular BV/BFV master equation INCLUDING the sixty puncture source terms, and the gluing of their worldlines to the boundary BFV data, is not constructed. Certificate G is therefore **DERIVED-CONDITIONAL** and not POSITIVE, and gate F-S26.G11 records exactly what is missing. \[**VERIFIED** for the triad; **DERIVED-CONDITIONAL** for the gravitational realisation. Checks M10.1–M10.7.\]

# **§4. Branch Selection and the Internal Derivation of the Conical Relation**

## **§4.1 Theorem S26.P1**

**Theorem S26.P1 (Branch and dictionary from one constraint). Let the reduced three-dimensional action be S₃ \= (1/16πG₃) ∫ d³x √(−g₃) (R₃ − 2Λ\_eff) \+ S\_src with G₃ obtained from §2 and Λ\_eff an as-yet undetermined coefficient of the reduced action, and let the configuration be static, K\_ij \= 0, which §3.3 establishes by construction rather than by assumption. Then the Hamiltonian constraint**

²R \= 2Λ\_eff \+ 16π G₃ ρ,   ρ \= Σ\_v m\_v δ²(x − x\_v),

evaluated on the piecewise-Euclidean spatial slice of K\_TI, splits into a smooth part and a singular part which fix, respectively,

Λ\_eff \= 0   and   δ\_v \= 8π G₃ m\_v.

Proof. The intrinsic geometry of K\_TI is Euclidean on the interior of every face, so ²R vanishes identically away from the sixty vertices; matching the smooth part of the constraint gives 2Λ\_eff \= 0\. At each vertex the distributional scalar curvature of a cone of deficit δ\_v is 2δ\_v δ²(x − x\_v); matching the singular part gives 2δ\_v \= 16π G₃ m\_v. Both statements come from the same equation and neither is an independent input.

Consequences. First, the seed's correction C-S26.5 is discharged: Λ\_eff \= 0 is not asserted from spatial flatness alone — it is the smooth part of a constraint that also contains the extrinsic curvature, and the extrinsic curvature is removed by the static condition, which §6 derives rather than assumes. Second, the seed's correction C-S26.4 is discharged: δ\_v \= 8π G₃ m\_v is no longer an imported gravitational dictionary applied to Z-Spin geometry but the singular part of the reduced parent constraint, so

G₃ m\_v \= δ\_v / 8π \= (π/15)/(8π) \= 1/120,   Σ\_v G₃ m\_v \= χ/4 \= 1/2.

Third, Λ\_eff \= 0 selects ISO(2,1) among the three admissible first-order groups. But the selection runs the other way from the way v1.0 to v1.2 stated it: the carrier geometry REQUIRES Λ\_eff \= 0, and whether the reduced ZS-S14 vacuum term supplies that value has not been computed. Gate F-S26.P5 is therefore NOT closed; it is subsumed into F-S26.P7, which is **OPEN**. \[The singular half is **DERIVED**; the branch half is **DERIVED-CONDITIONAL**. Checks M5.8, M10.2, M10.7; declaration D-S26.2.\]

## **§4.2 A number reported against interest**

Because G₃ carries the transverse form factor, so does the dimensionful defect mass: m\_def \= (1/120)/G₃ \= I\_Φ (π/30A) M\_P, hence 1.3075 M\_P ≤ m\_def ≤ 1.4122 M\_P. The lower endpoint 1.3075 M\_P is the I\_Φ \= 1, maximal-G₃ corner and must not be quoted as a value. Both endpoints are super-Planckian, and that is recorded rather than suppressed. It is not inconsistent: in three dimensions the physical bound is G₃m \< 1/4, and G₃m \= 1/120 is two orders of magnitude inside it — and carries no I\_Φ at all, being purely geometric. \[**OBSERVATION**, banded. Checks M5.10, M11.2.\]

# **§5. Defect Holonomies — the Dissection Certificate**

## **§5.1 Why the abelianised test carries no information**

The seed states, correctly, that the commuting-rotation identity R(π/15)^60 \= 1 is only the abelianised or Gauss–Bonnet control. This paper makes the statement quantitative. Write the physical puncture holonomies as conjugated Poincaré elements

h\_v \= t(p\_v) exp(δ\_v J₀ \+ s\_v P₀) t(p\_v)⁻¹,   s\_v \= 0,

and represent ISO(2,1) by real 4 × 4 matrices. In complex notation on the spatial plane with ω \= exp(iδ), a rotation by δ about p acts as z ↦ ωz \+ p(1 − ω), so the ordered product h₁h₂⋯h₆₀, with h₆₀ acting first, has rotational part ω⁶⁰ and translational part (1 − ω) Σ\_v ω^{v−1} p\_v. Since 60 · π/15 \= 4π the rotational part is the identity for every configuration whatsoever. The entire content of the closure condition is therefore the translational part,

h₁h₂⋯h₆₀ \= 1   ⟺   Σ\_{v=1}^{60} ω^{v−1} p\_v \= 0,

one complex, that is two real, linear equations. The companion exhibits the gap directly: taking the carrier's own developed vertex positions in an arbitrary order, the ordered product is a pure translation of norm ‖M − 1‖\_F \= 7.6733 while the rotational part closes exactly. \[**PROVEN**; negative control M3.4. Gate F-S26.G4 is a real gate and not a formality.\]

## **§5.2 The residual limitation of the first construction, and why it was not enough**

**A** configuration satisfying the closure condition is easy to exhibit: the constraint has rank two on a 120-real-dimensional space, so the solution variety is a non-empty affine subspace of dimension 118, and projecting any starting configuration onto it gives an exact solution, verified at ‖M − 1‖\_F \= 3.7 × 10⁻¹⁴ (check M3.6). This establishes that the carrier can support a closed defect system. It does not establish that the carrier's own developing map does so, because the projection moves the positions. That residual was registered during the exploration phase as gate F-S26.G9 and is discharged in §5.3. Stating it and then closing it, rather than presenting the projected solution as the result, is the discipline ZS-S24 gate F-S24.20 was written to enforce.

## **§5.3 An intrinsic Hurwitz system, and Theorem S26.G3′**

The correct object is not a set of sixty rotations but a geometric basis of π₁(Σ ∖ V, x₀), where Σ is the flat cone sphere carried by K\_TI and V is its set of sixty cone points. Since Σ ∖ V deformation retracts onto the dual one-skeleton, π₁ is free of rank 90 − 32 \+ 1 \= 59, and the sixty vertex loops satisfy exactly one relation. That relation is m₁m₂⋯m₆₀ \= 1 for a Hurwitz system, and it holds because the loop encircling all sixty punctures bounds, on the other side of the sphere, a disk containing none of them. The computational task is therefore to construct a Hurwitz system intrinsically and to evaluate it.

Construction. Fix a root face f₀ and unfold K\_TI along a spanning tree T\_d of its dual graph, giving a developing chart U\_f for every face. Assign to each vertex v the face φ(v) that first reaches it in the unfolding, and set p\_v \= U\_{φ(v)}(v). Define the plane tree

T\* \= T\_d ∪ { centre(φ(v)) → v : v ∈ V },

with 32 \+ 60 \= 92 nodes and 31 \+ 60 \= 91 edges. Every cone point is a leaf of T\*, because it is attached only through φ(v). The regular neighbourhood N(T\*) is a disk containing all sixty cone points, its complement is a disk containing none, and the boundary walk of N(T\*) therefore visits each cone point exactly once. Ordering the vertices by that boundary walk — a depth-first traversal of T\* respecting the cyclic order of the incident edges at each node in the developed plane — gives the Hurwitz ordering, and the arc from x₀ to v gives the conjugation, which in the developed picture is exactly the translation to p\_v.

**Theorem S26.G3′ (Dissection-certified holonomy closure). For the intrinsic Hurwitz system just constructed, the ordered product of the sixty carrier-derived defect holonomies in ISO(2,1) is the identity, with no projection, fitting or adjustment. The companion verifies this for all thirty-two rooted dissections, with worst residual**

max\_{f₀} ‖ h\_{k₁} h\_{k₂} ⋯ h\_{k₆₀} − 1 ‖\_F \= 1.04 × 10⁻¹².

Orientation control. Reversing the sign of δ against the same boundary walk breaks closure by up to ‖M − 1‖\_F \= 14.783. The sign of the deficit is therefore tied to the orientation of the dissection walk and is not a free convention: a counter-clockwise boundary walk pairs with δ \= −π/15 and a clockwise walk with δ \= \+π/15, and no other pairing closes. \[**PROVEN**. Checks M3.8–M3.10. Gate F-S26.G4 **CLOSED-PASS**; gate F-S26.G9 **CLOSED-PASS**.\]

## **§5.4 Source normalisation**

The source action is taken in the same normalisation as the bulk action, S\_src \= Σ\_v ∫\_{γ\_v} ⟨χ\_v, **A**⟩, with χ\_v the conjugacy-class label of the puncture. Because §4 has already derived δ\_v \= 8π G₃ m\_v from the reduced parent constraint, the conjugacy-class label, the physical mass and the holonomy angle are related without any further input, and G₃ m\_v \= 1/120 is a Z-Spin-derived statement. Gate F-S25.21, which asked for exactly this derivation inside the corpus, is **CLOSED-PASS**. \[**DERIVED**.\]

# **§6. The Reduced Phase Space, and the Refutation of 228**

## **§6.1 The orbit and the stabiliser**

The phase space of ISO(2,1) Chern–Simons gravity on a genus-g surface with n punctures at fixed conjugacy classes is the moduli space of flat ISO(2,1)-connections with those classes, parametrised by homomorphisms h : π₁(Σ\_{g,n}) → ISO(2,1) sending the loop around the i-th puncture into the class C\_i \= {h exp(−μ\_i J₀ − s\_i P₀) h⁻¹} determined by its mass and spin \[6\], \[7\]. For a regular spinless massive puncture the centraliser of exp(δ J₀) in ISO(2,1) is two-dimensional — rotations about the same axis together with time translations — so

dim O\_v \= dim ISO(2,1) − 2 \= 6 − 2 \= 4\.

The companion verifies this by computing the rank of Ad(h\_v) − 1 on iso(2,1) directly from the constructed holonomies (check M4.3).

## **§6.2 Theorem S26.G2**

**Theorem S26.G2 (Parabolic rank at the Z-Spin point). Let ρ be the holonomy representation of §5.3 and Z(ρ) ⊂ ISO(2,1) its centraliser. Then dim Z(ρ) \= 1, generated by the time translation P₀, and consequently**

dim H¹\_par \= Σ\_v dim O\_v − 2 (dim G − dim Z(ρ)) \= 60 · 4 − 2 (6 − 1\) \= 230\.

Proof. Every h\_v lies in E(2) \= SO(2) ⋉ ℝ², the subgroup of ISO(2,1) preserving the spatial plane, because the configuration is spinless and static. The time translation P₀ commutes with spatial rotations, since \[J₀, P₀\] \= 0, and with spatial translations, since translations commute among themselves; hence P₀ ∈ Z(ρ) and dim Z(ρ) ≥ 1\. Conversely the sixty rotations are about distinct centres, so the group they generate contains non-trivial translations as well as a rotation by δ ≠ 0; the boosts J₁, J₂ and the spatial translations P₁, P₂ rotate non-trivially under R(δ), and J₀ fails to commute with translations. Hence Z(ρ) \= ⟨P₀⟩ exactly. The dimension formula is the standard symplectic reduction: the ambient product of orbits has dimension Σ\_v dim O\_v, the moment map ∏\_v h\_v \= 1 imposes dim G − dim Z(ρ) independent conditions, and the residual conjugation acts with the same effective dimension.

The companion computes dim Z(ρ) as the nullity of the stacked matrix \[Ad(h\_v) − 1\]\_{v=1..60} on iso(2,1) and finds 1, with the null vector equal to P₀ to eight decimal places in the basis (J₀, J₁, J₂, P₀, P₁, P₂), namely (0, 0, 0, 1, 0, 0). \[**PROVEN**. Checks M4.1–M4.5.\]

## **§6.3 Independent cross-check, and the meaning of the \+2**

The static spinless locus is the sub-locus on which every puncture has s\_v \= 0 and the holonomies lie in E(2). Its dimension is counted directly: sixty planar positions give 120 real parameters, the closure condition of §5.1 removes 2, and the residual E(2) gauge action — which is free, since the centraliser of the image inside E(2) is trivial — removes 3\. Hence

dim (static locus) \= 120 − 2 − 3 \= 115 \= 230/2,

so the static locus has exactly the half-dimension required of a Lagrangian submanifold of H¹\_par. Half-dimensionality alone is not Lagrangian: isotropy, that is the vanishing of the Goldman symplectic form restricted to the locus, would have to be verified separately, and this paper does not verify it. The correct statement is therefore that the static locus is a LAGRANGIAN CANDIDATE. What the count does establish is a consistency check: with the generic value 228 the halving fails outright, since 228/2 \= 114 ≠ 115, so 230 and not 228 is the rank compatible with the static configuration space. That is an independent confirmation of Theorem S26.G2 which does not reuse the stabiliser computation. \[**DERIVED** for the dimension count; the Lagrangian property is **NON-CLAIM** NC-S26.13. Check M4.6.\]

The \+2 has a physical name. dim Z(ρ) \= 1 is precisely the statement that the solution admits a global timelike Killing vector, that is, that the configuration is static. Independently, §3.3 shows by direct construction that every intrinsic edge gluing of the cellular dreibein lies in E(2) with no boost component, and that the coframe is constant across the temporal prism, so K\_ij vanishes identically as an executable result. The enhanced stabiliser and the vanishing extrinsic curvature therefore corroborate one another. What they do NOT do is remove the branch conditionality of Theorem S26.P1: staticity is one hypothesis of that theorem, and the other — that the reduced ZS-S14 vacuum term actually vanishes — is untouched by either and remains gate F-S26.P7.

Gate F-S26.G6 accordingly fires against the seed's own target and is registered as a self-refutation of the parent document rather than a failure of this one. Any downstream paper quoting 228 as the Z-Spin phase-space dimension is quoting it wrongly.

## **§6.4 What is not claimed**

The 114 \= 6g − 6 \+ 2n moduli of ZS-S25 §6.4 remain, as that paper corrected, the moduli of the ambient sixty-particle theory. The number 230 is the dimension of the parabolic first cohomology at the Z-Spin holonomy point; it is not a claim that all 230 directions are physical excitations of a Z-Spin field, and no such claim is made. \[**NON-CLAIM** NC-S26.3.\]

# **§7. Quantum Instrument Status**

The seed pre-registers three possibilities for the quantum tier: P-Q1, a real Euclidean or compact real-form continuation with reflection positivity proved; P-Q2, classical BV–BFV closure proved with Hilbert-space positivity left **OPEN**; and P-Q3, no admissible contour or real form, closing the quantum route negatively. This paper terminates at P-Q2 and says so plainly.

The reason is stated once. ZS-S24 Theorem S24.14 constructs a canonical reflection-positive symmetric semigroup realisation T\_a \= e^{−aV/2} e^{−aL} e^{−aV/2} for the compact group SU(3) on the same carrier. Its hypotheses are compactness of the configuration manifold M \= G^E, boundedness of the gauge-invariant potential, and uniform ellipticity with gauge commutation of L. For G \= ISO(2,1) the manifold is non-compact, e^{−aL} need not be trace class, and the Perron–Frobenius step of ZS-S24 Theorem S24.9 has no non-compact analogue in the corpus. Importing it would be exactly the error C-S26.2 forbids.

No positive gravitational transfer Hamiltonian is claimed, no gravitational mass gap is claimed, and ZS-S24's Δ\_phys \> 0 is a statement about the gauge Hamiltonian only. In three-dimensional gravity the Hamiltonian is a first-class constraint that vanishes on physical states, so quoting Δ\_phys \> 0 as a property of the gravitational operator would be a category error, exactly as ZS-S25 gate F-S25.9 records. \[**NON-CLAIM** NC-S26.4. Gate F-S26.G8 **OPEN**. Outcome tier P-Q2.\]

# **§8. The Gauge Side — the Multiplicity-Algebra Structure Theorem**

## **§8.1 Exact reconstruction of the gauge-side data**

The companion rebuilds the carrier from exact Cartesian coordinates, forms the unweighted face Laplacian Δ₂ \= B₂B₂ᵀ, and recovers the nine distinct eigenvalues with multiplicities (1, 3, 5, 3, 4, 5, 3, 5, 3), including λ₁ \= 1.2428416164 and λ\_h \= 7.5210904061 at multiplicity three each. It builds the gap edge potentials α \= B₂ᵀu/λ, forms the cyclic basepoint-averaged cup product, totally antisymmetrises and contracts with ε. The four admissible channels of ZS-S25 Table 3.3 are recovered exactly:

Table 8.1. The four admissible cubic channels, rebuilt from coordinates.

| eigenvalue | isotype | structure constant | residual of T − cε | corpus value |
| ----- | ----- | ----- | ----- | ----- |
| 1.2428416164 | T₁ | 0.3515993958 | 1.3 × 10⁻¹⁶ | 0.3515993958 |
| 4.8443660283 | T₂ | 0.0071641984 | 0.0 | 0.0071641984 |
| 7.5210904061 | T₁ | 0.0038869096 | 0.0 | 0.0038869096 |
| 8.3917019492 | T₂ | 0.0015865494 | 1.3 × 10⁻¹⁶ | 0.0015865494 |

No number in this table is imported. The agreement is to all ten quoted digits on all four channels, which independently confirms ZS-S18 Theorem S18.9, ZS-S25 Theorem S25.7 and the two T₂ values ZS-S25 recorded for the first time. \[**VERIFIED**. Checks M1.1–M1.4.\]

## **§8.2 Theorem S26.C1 — the structure theorem**

The two T₁ eigenspaces are isomorphic as representations of the rotational icosahedral group I ≅ **A**₅. The companion reconstructs all sixty proper rotations directly from the vertex set, induces the signed action on the thirty-two oriented faces, verifies that it is a group representation, and builds the intertwiner by averaging. Schur's lemma is confirmed numerically: the averaged intertwiner has three equal singular values and, after orthogonalisation, satisfies R₁(g) **Q** \= **Q** R\_h(g) for all sixty elements to 1.3 × 10⁻¹⁵. Aligning the second block by **Q** puts W₆ in the form T₁ ⊗ M with M the two-dimensional multiplicity space.

**Theorem S26.C1 (Multiplicity-algebra factorisation). In the aligned basis the alternating cyclic cochain vertex restricted to W₆ factorises exactly as**

ℓ₂ \= ε ⊗ μ,   \[x ⊗ a, y ⊗ b\] \= (x × y) ⊗ μ(a, b),

with μ : M × M → M a symmetric bilinear product. The companion measures ‖ℓ₂ − ε ⊗ μ‖ / ‖ℓ₂‖ \= 1.87 × 10⁻¹⁶ and ‖μ − μᵀ‖ \= 0 exactly. The alternating product closes on W₆ with leakage 3.687 × 10⁻¹³ per cent, independently confirming ZS-S17 and ZS-S25 Proposition S25.2a. The measured product is

Table 8.2. The multiplicity-space product μ, computed from the carrier.

| argument | first component | second component |
| ----- | ----- | ----- |
| μ(e₀, e₀) | \+0.1757996979 | \+0.0487456394 |
| μ(e₀, e₁) \= μ(e₁, e₀) | \+0.0023108377 | −0.0110018747 |
| μ(e₁, e₁) | −0.0002416864 | −0.0019434548 |

This is a new exact structural fact about the Z-Spin carrier and it is what converts ZS-S25's measured residual into a classified obstruction. \[**PROVEN**. Checks M2.1–M2.6.\]

## **§8.3 Theorem S26.C2 — Jacobi is associativity**

**Theorem S26.C2. For any symmetric bilinear μ on a finite-dimensional space M, the bracket ε ⊗ μ on ℝ³ ⊗ M satisfies the Jacobi identity if and only if μ is associative.**

Proof. Using (x × y) × z \= y(x · z) − x(y · z), the cyclic sum of double brackets collects, on the coefficient of x, the expression (y · z)\[μ(μ(c, a), b) − μ(μ(a, b), c)\], and similarly for y and z. Vanishing for all x, y, z is therefore equivalent to μ(μ(a, b), c) \= μ(μ(c, a), b) for all a, b, c, which together with the symmetry of μ is exactly associativity.

The companion confirms the equivalence over five hundred random symmetric μ on a two-dimensional M with zero counterexamples, and verifies that each of the four two-dimensional commutative associative algebras — ℝ ⊕ ℝ, ℂ, ℝ\[ε\]/ε², and the null algebra — gives Jacobi exactly zero. \[**PROVEN**. Checks M2.7, M2.8.\]

## **§8.4 Theorem S26.C3 — the component obstruction**

The physical μ of Table 8.2 is not associative: ‖assoc(μ)‖\_F \= 3.2007836 × 10⁻³, and the induced Frobenius-normalised Jacobi residual of ℓ₂ is 0.0674839780, reproducing the corpus figure 0.067484 to six significant figures without importing it.

The remaining question is whether the failure is a convention. The only genuine normalisation freedom is an output rescaling ν\_{mn}^p \= u\_p μ\_{mn}^p, since an input rescaling s\_m s\_n composed with the algebra isomorphism s\_m s\_n / s\_p reduces to it. Writing μ(e₀, e₀) \= (a, b), μ(e₀, e₁) \= (c, d) and μ(e₁, e₁) \= (e, f), the first associativity equation is u₀ u₁ (be − cd) \= 0\.

**Theorem S26.C3 (Component obstruction). Define Ω := μ₀₀¹ μ₁₁⁰ − μ₀₁⁰ μ₀₁¹ \= be − cd. Then Ω \= 1.364238922615 × 10⁻⁵ ≠ 0, so associativity forces u₀ u₁ \= 0, that is a degenerate rescaling that annihilates one multiplicity block. No non-degenerate normalisation repairs Jacobi.**

**A** wording caution, tightened in v1.4. Ω is one explicit component of the associator in the selected basis, and its non-vanishing exhibits non-associativity; it is NOT claimed to be a GL(2) scalar invariant. What is basis-independent is non-associativity itself, and the companion's two thousand GL(2) basis changes are a robustness diagnostic rather than an invariance proof. Nothing downstream needs more than this, because Theorem S26.C6 establishes E₂ \< 0 globally and independently of Ω. \[**PROVEN** for the non-associativity; the invariance of Ω is a **NON-CLAIM**. Checks M2.9–M2.11.\]

# **§9. Certificate C — the Verdict on the ZS-S25 Double-Copy Route**

## **§9.1 Retraction of the minimal-model argument, and the remaining strict result**

**Retraction S26-R1 (against ZS-S26 v1.0–v1.2, Theorem S26.C4). Those versions asserted \[J₆\] ≠ 0 in H•(Q\_W) on the ground that W₆, being an eigenspace of a positive Laplacian, carries a minimal L∞ model with Q \= 0\. That inference is FALSE and the theorem is WITHDRAWN.**

The error, stated plainly. Δ₂w \= λw with λ \> 0 says that w is a Hessian eigenmode; it does not say that w represents a class of a BRST or BV differential. **A** positive eigenmode generically has a non-vanishing kinetic operator, so W₆ is not the cohomology of anything and the arity-three L∞ identity does not collapse. Deciding whether an ℓ₃ can absorb the Jacobiator requires an explicit chain contraction on the action-selected complex,

(𝔥\_full, **Q**) ⇄ (W, Q\_W) with inclusion i, projection p, homotopy h and 1 − ip \= Qh \+ hQ,

together with the transferred ℓ₃ and the quartic master identity. This paper constructs none of them: no BRST differential, no i, no p, no h, no transferred ℓ₃. The residual is registered as gate F-S26.C11 and it is **OPEN**.

What survives is the strict statement and only that: on every six-dimensional I-equivariant active space assembled from the four admissible cubic channels, and for every weight in the two-parameter orbit family, the induced bracket is not a Lie bracket. Gate F-S26.C2 is accordingly restated as the STRICT gate and it **FIRES** in that restricted sense. The corpus-level consequence is that the ZS-S25 double-copy route is **CLOSED-NEGATIVE** as a strict Lie construction and **OPEN** as a homotopy construction. \[**PROVEN** for the strict statement; the homotopy statement is **NON-CLAIM** NC-S26.11.\]

## **§9.2 What CLOSED-NEGATIVE does and does not mean**

It does not invalidate Certificate G. Sections 3 to 6 construct the gravitational theory directly from the parent reduction and use nothing from §8 or §9. What the negative certificate establishes is narrower than v1.2 claimed: a STRICT Lie structure on the finite gauge sector cannot be the origin of Z-Spin gravity. Whether a homotopy-level structure can is not decided here, so the alternative the seed posed is answered only in its strict half.

It is also a bounded negative. The obstruction is localised in one invariant of a two-dimensional commutative algebra, and the repair is named exactly: some other action-selected active space would have to carry a multiplicity product lying on the associative locus. The algebras ℝ ⊕ ℝ, ℂ, ℝ\[ε\]/ε² and the degenerate ones are representative associative models used as controls; they are not an exhaustive classification, and no exhaustive classification is used in the proof. Whether the exact {κ\_p}-weighted Hessian of ZS-S23 gate F-S23.6 selects such a space was registered in v1.0 as gate F-S26.C7 and was the only surviving route by which Certificate C could be reopened positively. Section 9.3, new in v1.1, closes it.

## **§9.3 F-S26.C7 — the weighted-Hessian associativity question, closed**

The admissible weights. ZS-S21 and ZS-S23 reduce the entire freedom in the exact Hessian to two orbit ratios: the edge ratio σ \= m₅₆/m₆₆ over the sixty pentagon–hexagon edges against the thirty hexagon–hexagon edges, and the face ratio ρ \= β₅/β₆ over the twelve pentagons against the twenty hexagons. Overall scale is irrelevant. The weighted operator is Δ₂(σ, ρ) \= D\_f^{1/2} B₂ D\_e B₂ᵀ D\_f^{1/2} with D\_e \= diag(σ on (5,6) edges, 1 on (6,6) edges) and D\_f \= diag(ρ on pentagons, 1 on hexagons), and it reduces to B₂B₂ᵀ at σ \= ρ \= 1, recovering λ₁ and λ\_h exactly. The reachable family of multiplicity algebras is therefore exactly two-parameter.

Why counting does not decide it. The space of symmetric μ on a two-dimensional M is six-dimensional, and the companion computes the rank of the Jacobian of the associator at four canonical representatives — ℝ ⊕ ℝ, ℂ, ℝ\[ε\]/ε² and ℝ × null — obtaining rank two in every case. This is a diagnostic and not a classification: it shows that a two-parameter family is not excluded from meeting the associative locus by elementary dimension counting alone. No exhaustive classification of two-dimensional commutative associative algebras is asserted, and none is used anywhere in the proof. The question is therefore genuinely open on counting grounds and must be computed. Nothing downstream depends on this paragraph: the global no-go is closed in §9.3b by the analytic statement E₂ \< 0 on the whole open quadrant, not by any codimension count.

Closure is weight-independent. The isotypic subspace of the thirty-two-dimensional face representation is determined by symmetry alone and does not move when the weights change; only the eigenbasis inside it rotates. The companion confirms that the alternating product closes on it with leakage below 7 × 10⁻¹⁵ over an eighty-one-point weight grid, for both the T₁ and the T₂ isotype. The 'closed' half of the ZS-S25 dichotomy is therefore structural, not accidental. \[**PROVEN**. Check M7.5.\]

The locus Ω \= 0 is non-empty. Over the family Ω changes sign, and the companion locates 382 points of the curve Ω \= 0 for the T₁ isotype and 359 for the T₂ isotype, spanning σ ∈ \[0.05, 20\] and ρ ∈ \[10⁻³, 10³\]. The single invariant of Theorem S26.C3, which was decisive at fixed weights, is by itself insufficient once the weights are allowed to move. This is reported because it is the point at which a weaker paper would have stopped and declared victory. \[Check M7.7.\]

**Theorem S26.C6 (Sign obstruction on the associativity locus). Write the three associativity equations of a two-dimensional commutative algebra with μ(e₀,e₀) \= (a, b), μ(e₀,e₁) \= (c, d), μ(e₁,e₁) \= (e, f) as**

E₁ \= be − cd,   E₂ \= ad \+ bf − cb − d²,   E₃ \= c² \+ de − ea − fc,

so that associativity is E₁ \= E₂ \= E₃ \= 0\. On the entire locus E₁ \= Ω \= 0 of the weighted family, E₂ is strictly negative:

max E₂ \= −4.78 × 10⁻⁶ (T₁),   max E₂ \= −7.97 × 10⁻⁷ (T₂),

with the extreme values attained only in the degenerate corners of the scan, and max E₂ \= −4.67 × 10⁻⁴ and −3.00 × 10⁻³ respectively once restricted to the ZS-S23 audited window σ, ρ ∈ \[0.1, 30\]. Hence no admissible weight makes μ associative. By contrast E₃ does change sign on the locus, over the range \[−1.20 × 10⁻², \+8.04 × 10⁻³\], so E₁ \= E₃ \= 0 is solvable and the failure is one named equation. \[Checks M7.8, M7.9. Version 1.1 recorded this as EXHAUSTIVE and registered gate F-S26.C8 against the missing proof; §9.3b supplies the proof and the status is now **PROVEN** on the whole open quadrant.\]

Every weight point the corpus has ever named lies far from the locus. The counting star of axiom (Z-A1), the ZS-S23 Archimedean round metric, the ZS-S23 separator at t \= 7/20, and the two ZS-S21 circumcentric branches all give E₂ between −5.5 × 10⁻² and −6.7 × 10⁻², three to five orders of magnitude away from zero. \[Check M7.10.\]

Table 9.1. The three associativity residuals at the corpus-named weight points, T₁ isotype.

| weight point | (σ, ρ) | E₁ \= Ω | E₂ | E₃ |
| ----- | ----- | ----- | ----- | ----- |
| counting star (Z-A1) | (1, 1\) | \+4.068 × 10⁻⁴ | −6.746 × 10⁻² | \+1.639 × 10⁻³ |
| ZS-S23 Archimedean round metric | (0.893975, 1.529372) | −1.190 × 10⁻³ | −6.140 × 10⁻² | \+2.959 × 10⁻³ |
| ZS-S23 separator t \= 7/20 | (0.764687, 1.304974) | \+1.035 × 10⁻³ | −5.536 × 10⁻² | \+4.013 × 10⁻³ |
| ZS-S21 intrinsic circumcentric | (0.897327, 1.529372) | \+1.188 × 10⁻³ | −6.155 × 10⁻² | \+2.933 × 10⁻³ |
| ZS-S21 chordal circumcentric | (0.910593, 1.529372) | −1.182 × 10⁻³ | −6.216 × 10⁻² | \+2.831 × 10⁻³ |

## **§9.3b The analytic sign theorem — F-S26.C8 discharged**

The exact 2 × 2 reduction. Character orthogonality shows that T₁ occurs exactly once in the twelve-pentagon block of the face representation and exactly once in the twenty-hexagon block, and the same holds for T₂. The multiplicity space M therefore has a canonical decomposition M \= M\_pent ⊕ M\_hex, in which the entire weighted problem collapses to a 2 × 2 generalised eigenproblem **A**(σ) v \= λ N(ρ) v. Two structural facts fix its form. At σ \= 0 the edge weight annihilates all sixty pentagon–hexagon edges, and a pentagon carries no hexagon–hexagon edge, so the pentagon row and column of **A**₀ vanish identically. And the cochain cup tensor collapses to four monomials. In an orthonormal block basis, verified to 1.8 × 10⁻¹⁷,

**A**₀ \= diag(0, R),   **A**₁ \= \[\[P, **Q**\], \[**Q**, S\]\],   N(ρ) \= diag(ρ, 1),

Λ\[pp,h\] \= βσ²,   Λ\[ph,h\] \= γσ,   Λ\[hh,h\] \= δ,   Λ\[hh,p\] \= ρασ²,   every other entry zero.

The pencil constants are exact algebraic integers, and the two isotypes are Galois conjugates of one another under √5 ↦ −√5:

Table 9.2. Exact pencil constants of the Z-Spin carrier, orthonormal block basis.

| isotype | P | S | R | Q | P S − Q² | P R |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| T₁ | 5 | 3 | 3 − √5 \= 0.7639320225 | −√(5 \+ 2√5) \= −3.0776835372 | 10 − 2√5 \= 5.5278640450 | 15 − 5√5 \= 3.8196601125 |
| T₂ | 5 | 3 | 3 \+ √5 \= 5.2360679775 | \+√(5 − 2√5) \= \+0.7265425280 | 10 \+ 2√5 \= 14.4721359550 | 15 \+ 5√5 \= 26.1803398875 |

Separating the normalisation. Write the N-orthonormal eigenvectors as v\_A \= (x\_A, y\_A) and v\_B \= (x\_B, y\_B), with eigenvalues λ\_A \< λ\_B and D \= x\_A y\_B − y\_A x\_B ≠ 0\. The bracket splits as μ\_mn^p \= k\_mn^p/(λ\_m λ\_n), where k is the cup data in the eigenbasis and carries no eigenvalue dependence. Substituting into the three associativity equations and using S\_h(y\_A v\_B − y\_B v\_A) \= S\_h(−D, 0\) together with det Λ^(h) \= σ²(βδ − γ²) gives closed forms in which the eigenvalues appear only through the single positive ratio t \= λ\_B/λ\_A:

E₁ \= P₁/(λ\_Aλ\_B)²,   E₂ \= (t P₂ \+ P₃)/(λ\_Aλ\_B)²,   E₃ \= (P₄ \+ P₅/t)/(λ\_Aλ\_B)²,

P₂ \= −g σ D² y\_A (β σ x\_A \+ γ y\_A),   P₃ \= σ² D² y\_B \[ g β x\_B \+ (βδ − γ²) y\_B \],   g \= α ρ σ².

The companion verifies these closed forms against the independent numerical pipeline over 4050 weights spanning σ, ρ ∈ \[10⁻⁵, 10⁵\], at maximum relative error 1.0 × 10⁻¹¹. \[Check M8.7.\]

**Lemma S26.C6a (Eigenvector sign lemma). Let P, S \> 0, R \> 0, Q ≠ 0 and PS − Q² \> 0\. Then for every σ, ρ \> 0 the pencil A(σ) v \= λ N(ρ) v has 0 \< λ\_A \< λ\_B, and**

sign(y\_A/x\_A) \= −sign(**Q**),   sign(y\_B/x\_B) \= \+sign(**Q**).

Proof. Writing φ(λ) \= σP − λρ and ψ(λ) \= R \+ σS − λ, the two rows of the eigen-equation give y/x \= −φ(λ)/(σ**Q**) and x/y \= −ψ(λ)/(σ**Q**), whose product is the characteristic equation φψ \= σ²**Q**². Hence φ and ψ have the same sign at each eigenvalue. Both are positive at λ \= 0, and h(λ) := φψ − σ²**Q**² is an upward parabola with h(0) \= σ\[PR \+ σ(PS − **Q**²)\] \> 0 by hypothesis, so 0 \< λ\_A. At either zero of φ or of ψ one has h \= −σ²**Q**² \< 0, so both zeros lie strictly between λ\_A and λ\_B. Therefore φ, ψ \> 0 at λ\_A and φ, ψ \< 0 at λ\_B, which gives the two stated signs.

**Theorem S26.C6 (Strict negativity of E₂ — PROVEN). Assume the structural form above together with the three exact inequalities**

(I1) βδ − γ² \< 0,   (I2) αγ \> 0,   (I3) βγ**Q** \< 0\.

Then E₂ \< 0 strictly for every (σ, ρ) ∈ (0, ∞)². Consequently the system E₁ \= E₂ \= E₃ \= 0 has no solution, and the multiplicity algebra μ is associative for no admissible weight whatsoever.

Proof. Under the two independent block reflections the constants transform as α ↦ ε\_p α, γ ↦ ε\_p γ, β ↦ ε\_h β, δ ↦ ε\_h δ and **Q** ↦ ε\_p ε\_h **Q**, so the three quantities in (I1)–(I3) are reflection invariants and the signs of β and α may be normalised independently. Choose β \> 0 and α \> 0\. Then (I2) gives γ \> 0 and (I3) gives **Q** \< 0, whence Lemma S26.C6a yields x\_A, y\_A, x\_B \> 0 \> y\_B after fixing x\_A, x\_B \> 0\. Now g \= αρσ² \> 0, so in P₂ the factor y\_A is positive and βσx\_A \+ γy\_A is a sum of two positive terms, giving P₂ \= −g σ D² y\_A (βσx\_A \+ γy\_A) \< 0\. In P₃ the bracket gβx\_B \+ (βδ − γ²)y\_B is again a sum of two positive terms, the second because (I1) and y\_B \< 0 are both negative, while the prefactor y\_B is negative, giving P₃ \< 0\. Since t \= λ\_B/λ\_A \> 0 by Lemma S26.C6a, E₂ \= (tP₂ \+ P₃)/(λ\_Aλ\_B)² \< 0\.

The carrier satisfies the hypotheses, exactly — and in v1.3 exactly means exactly. Version 1.2 obtained the constants by recognising floating-point values against algebraic candidates, which is strong evidence and not a proof. Version 1.3 recomputes the whole carrier in ℚ(√5) with Fraction arithmetic: the sixty vertices lie in ℤ\[φ\], every edge has length squared identically 4, all thirty-two faces are certified exactly planar with exact edge cycles, the pentagon and hexagon blocks are exactly orthogonal, and the structural zeros of **A**₀ and of the cup tensor vanish identically. In the canonical centroid basis the pencil constants are P \= 250 \+ 82√5, **Q** \= −(170 \+ 74√5), S \= 210 \+ 90√5 and R \= 60 \+ 20√5, and the cup constants are α \= 122 \+ 54√5, β \= (166 \+ 66√5)/3, γ \= (340 \+ 148√5)/3 and δ \= (180 \+ 80√5)/3. Every sign below is certified by an integer comparison of a² against 5b², with no floating point anywhere. The three closing inequalities evaluate to

(I1) \= −18760 − (25160/3)√5,   (I2) \= (81440 \+ 36416√5)/3,   (I3) \= −(11763520/3) − (15782080/9)√5,

with (H2) given by PR \= 23200 \+ 9920√5 and PS − **Q**² \= 33120 \+ 14560√5. Every one of these has both coefficients of the same sign, so the T₁ signs are immediate. The T₂ case is settled without a second computation by Galois descent: the face permutation representation is defined over ℚ, so the T₂ isotypic projector is the image of the T₁ one under √5 ↦ −√5, and therefore so is every derived constant. The conjugated quantities have coefficients of opposite sign, and their signs follow from the integer certificates a² − 5b² \> 0: for instance 23200² − 5·9920² \= 46 208 000 \> 0 and 33120² − 5·14560² \= 36 966 400 \> 0, so PR and PS − **Q**² remain positive after conjugation. \[**PROVEN**, with exact hypotheses. Checks M8.1–M8.10 and M9.1–M9.10. Gate F-S26.C8 executed and did not fire.\]

What the promotion changes and what it does not. It changes the epistemic grade of one statement, from EXHAUSTIVE over a scanned box to **PROVEN** on the whole open quadrant (0, ∞)², and it removes the last conditionality from Certificate C. It changes no number, no other status, and no gate. It also strengthens the scope: version 1.1 proved E₂ ≠ 0 only where Ω \= 0 had been located numerically, whereas Theorem S26.C6 now gives E₂ \< 0 everywhere, so the locus Ω \= 0 need not be traced at all. The v1.1 trace of that locus is retained in §9.3 because it is what shows the single invariant Ω to be insufficient, which is the reason the second equation had to be examined in the first place.

## **§9.4 The mixed active spaces, and the exhaustive dichotomy**

The isotypic spaces are not the only six-dimensional candidates. ZS-S25 §3.9 recorded that the carrier supplies four admissible cubic channels, two of type T₁ and two of type T₂, so one may also assemble a mixed active space T₁(a) ⊕ T₂(b). Here the answer is representation-theoretic and needs no scan.

Under I ≅ **A**₅ one has T₁ ⊗ T₂ \= G ⊕ H, which contains neither T₁ nor T₂. By Schur's lemma the projected bracket between the two blocks therefore vanishes identically, so the projected bracket on a mixed space is block diagonal and equals c\_a ε on one block and c\_b ε on the other. Every mixed active space is consequently a strict Lie algebra so(3) ⊕ so(3), whose multiplicity algebra is ℝ ⊕ ℝ — the first entry of the associative list. The companion measures Jacobi residuals below 1.5 × 10⁻¹⁵ on all four mixed pairs at two different weight points.

But the same lemma is what destroys it. Vanishing of the projection is not vanishing of the product: the mixed product B(T₁, T₂) lands entirely inside G ⊕ H, so its leakage out of the active space is exactly 100 per cent, with a mixed-product norm of order 10⁻³ to 10⁻¹ and therefore bounded away from zero. Since the statement is a consequence of Schur's lemma and not of any coefficient, it holds for every {κ\_p} whatsoever. \[**PROVEN**. Check M7.11.\]

**Theorem S26.C5 (Closure–Jacobi dichotomy, scoped). Let W be a six-dimensional I-equivariant active space assembled from the four admissible cubic channels of K\_TI, and let the weights range over the two-parameter diagonal orbit family (σ, ρ) of §9.3. Then W is exactly one of the following. (a) Isotypic, T₁ ⊕ T₁ or T₂ ⊕ T₂: product-closed for every weight in the family, and never a Lie algebra, because E₂ \< 0 identically. (b) Mixed, T₁(a) ⊕ T₂(b): a strict Lie algebra so(3) ⊕ so(3) with associative multiplicity algebra ℝ ⊕ ℝ for every weight, and never closed, because T₁ ⊗ T₂ \= G ⊕ H by Schur — an obstruction that holds for every {κ\_p} whatsoever, diagonal or not. No such W is simultaneously closed and strictly Lie.**

Gate F-S26.C7 is therefore **CLOSED-NEGATIVE** within its stated scope, and the ZS-S25 dichotomy — closed but not Lie, or Lie but not closed — is upgraded from a measured observation to a theorem about the icosahedral representation theory of the carrier. The two failure modes are the two faces of one lemma: Schur is what forces the isotypic bracket to be ε ⊗ μ, and Schur is what forces the mixed product out of the space. \[**PROVEN** within scope. Check M7.12.\]

Two scope statements are attached and must travel with any citation. First, clause (b) is weight-independent because it is Schur’s lemma, but clause (a) is proved for the two-parameter diagonal orbit-weight family. **A** general I-equivariant Whitney or FEEC mass matrix is orbit-constant yet may act by a non-diagonal matrix on the multiplicity block; the family of §9.3 does sweep every eigenbasis, and E₂ ∝ tP₂ \+ P₃ with P₂, P₃ \< 0 depends on the eigenbasis only, so the conclusion is stable under an arbitrary independent change of the eigenvalue ratio t — but a Hessian whose eigenbasis lies outside the reachable region is outside the theorem. That is gate F-S26.C9. Second, the theorem is about six-dimensional active spaces built from the four listed channels; the twelve-dimensional span of all four is outside its scope, as NC-S26.9 already records. The permanent guard F-S26.C10 fires on any citation that drops either scope.

The ZS-S25 gates F-S25.10, F-S25.12, F-S25.15 and F-S25.20 and hypotheses S25.H0–H2 are not erased. They are subsumed: on the active space they are decided negatively, within the strict scoped family, by Theorems S26.C5–C6; Theorem S26.C4 is withdrawn and is not used anywhere. Off that family they remain **OPEN**, and the homotopy question remains **OPEN** at F-S26.C11. No gate is silently deleted. \[Collision audit §11.\]

# **§10. Coupling Normalisation and the Two-Mass Firewall**

## **§10.1 The firewall**

Three mass symbols appear in this line and no equality is assumed among them: m\_def, the gravitational puncture mass of §4; m\_gap, the Yang–Mills transfer excitation mass of ZS-S24; and m\_src^YM, the mass parameter of a gauge source. Only m\_def enters any equation of this paper. \[Gate F-S26.N3.\]

## **§10.2 Theorem S26.P4**

**Theorem S26.P4′ (Coupling band). With G₃ and g²\_YM,3 the outputs of §2, and I\_Φ the transverse form factor of §2.5,**

G₃ g²\_YM,3 \= **A**² g₄² / (2π I\_Φ) \= 2 **A**² α\_s(μ) / I\_Φ \= λ\_vac α\_s(μ) / I\_Φ,

since g₄² \= 4π α\_s and λ\_vac \= 2A². The transverse length does NOT cancel. Before the parent width is substituted both factors carry one inverse power of it,

G₃ \= 1/(8π M\_P² L⊥ I\_Φ),   g²\_YM,3 \= g₄²/L⊥,   hence   G₃ g²\_YM,3 \= g₄² / (8π M\_P² L⊥² I\_Φ),

so the product scales as L⊥⁻². What removes any free transverse scale is not a cancellation but the SUBSTITUTION of the derived width L⊥ \= 1/(2A M\_P), which converts the L⊥⁻² into the **A**²-normalised band above. The companion verifies the scaling directly: the product multiplied by L⊥² is constant to better than 10⁻¹⁵ relative over a factor 14.6 in L⊥ (check M5.6b). In exact rational form, with α\_s \= 11/93,

2A²α\_s/(1 \+ **A**) \= 1.404922557 × 10⁻³   ≤   G₃ g²\_YM,3   ≤   2A²α\_s \= 1.517444958 × 10⁻³,

a closed two-sided band whose fractional width is exactly **A**/(1 \+ **A**) \= 35/472 \= 7.4153 per cent. Combining with G₃ m\_def \= 1/120 of §4, which is purely geometric and carries no I\_Φ, gives g²\_YM,3/m\_def \= 240 **A**² α\_s/I\_Φ ∈ \[0.1685907, 0.1820934\], and m\_def \= I\_Φ (π/30A) M\_P ∈ \[1.3075, 1.4122\] M\_P. Gate F-S25.22, which ZS-S25 called the single most valuable remaining calculation in the line, is therefore reduced from **OPEN** to a band of width **A**. \[**DERIVED-CONDITIONAL**. Checks M5.4–M5.10, M11.1–M11.3.\]

The residual uncertainty in the gauge–gravity coupling is exactly the geometric impedance. That is not a slogan: **A** enters twice, once as the coupling itself through λ\_vac \= 2A² and once as the width of the band through the non-minimal factor 1 \+ **A**|Φ|², and the second occurrence is what remains undetermined. Collapsing the band needs the actual Bogomolnyi transverse profile, or a proof that the reduction is a delta-localised interface rather than a finite-width slab. Neither is performed here; the gate is F-S26.P8.

## **§10.3 The two conditionalities, stated rather than hidden**

First, L⊥ \= 1/m\_ρ rests on λ\_vac \= 2A², which ZS-U5 supplies as **DERIVED-CONDITIONAL**. The result inherits that status and cannot be stronger than its weakest input. Because the product scales as L⊥⁻² BEFORE the substitution, gate F-S26.P2 controls the OVERALL NORMALISATION of the coupling band, not merely its width. The fractional width **A**/(1 \+ **A**) is controlled by the other, independent unknown: the transverse form factor I\_Φ at gate F-S26.P8. Versions up to 1.7 stated these two roles the other way round, and that is corrected here.

Second, and more sharply, α\_s runs. Using α\_s(M\_Z) \= 11/93 inside a reduction whose transverse scale is μ \= 2A M\_P \= 0.16 M\_P is scheme-inconsistent, and this paper does not pretend otherwise. The correct statement separates two claims. The structural identity

G₃ g²\_YM,3 \= λ\_vac α\_s(μ) / I\_Φ,   μ \= 2 **A** M\_P,

is the theorem. It is scheme-labelled only through α\_s(μ), and it remains conditional on the unresolved form factor I\_Φ. The number 26950/17760117 is the I\_Φ \= 1 UPPER ENDPOINT of the band, evaluated with the scheme-labelled value α\_s(M\_Z) \= 11/93; it is not the coupling unless the transverse profile independently yields I\_Φ \= 1\. It is quoted so that the magnitude is on record and so that a future evaluation at μ can be compared against it. Gate F-S26.N5 fires on any downstream paper that quotes the number without both labels.

Because of these two items the closure level attained at G4 is structural-positive with one named datum, not full quantitative closure. Under the seed §9 definitions that is sufficient for complete scientific resolution and insufficient for full positive closure, and the paper declares the former.

# **§11. Collision Audit against ZS-S14 to ZS-S25**

Table 11.1. Cross-paper dependency and collision audit.

| upstream paper | object consumed | role in ZS-S26 | effect |
| ----- | ----- | ----- | ----- |
| ZS-F1 v1.0 | action, λ\_vac, m\_ρ, Z-anchor | transverse measure, non-minimal factor | consumed unchanged |
| ZS-S14 v2.0 | master action, **A**, α\_s | parent of the reduction | consumed unchanged |
| ZS-S19 v1.6 | λ₁ status **DERIVED-CONDITIONAL** on (R\_C) | carrier spectrum | consumed unchanged |
| ZS-S21 v1.2 | λ₁, λ\_h **LOCKED** | W₆ construction | reproduced, not imported |
| ZS-S23 v1.3 | F-S23.6 exact κ\_p | not used | left exactly as found |
| ZS-S24 v1.9 | compact-group transfer/positivity | explicitly NOT transferred | scope enforced, C-S26.2 |
| ZS-S25 v2.1 | W₆ closure, 0.067484, δ \= π/15, G₃m \= 1/120 | inputs to §5, §8 | all reproduced from coordinates |
| ZS-S25 v2.1 | Λ \= 0 as a branch choice | re-typed in §4 as a compatibility condition | NOT upgraded; parent supply **OPEN** at F-S26.P7 |
| ZS-S26 seed v1.1 | target dim H¹\_par \= 228 | REFUTED in §6 | C-S26.8, F-S26.G6 |

No locked physical constant and no established upstream result is changed by this paper. One pre-registered seed target is: the value 228 is refuted and replaced by the computed rank 230\. One epistemic status is upgraded — δ\_v \= 8πG₃m\_v, from an imported gravitational dictionary to the singular part of the reduced parent constraint, hence **DERIVED**. Λ\_eff \= 0 is NOT upgraded: version 1.2 promoted it and version 1.3 retracted that promotion as S26-R3, so its status here is a **DERIVED-CONDITIONAL** compatibility condition that the carrier imposes, with the question of whether the parent vacuum term supplies it left **OPEN** at F-S26.P7. One seed target is refuted. The i-tetration fixed point z\* of ZS-M1 and everything downstream of it are untouched, since no statement of this paper consumes z\*, μ or δ of ZS-Q18, so no version conflict can arise on that branch.

Compatibility with external physics. Nothing here touches Planck 2018 ΛCDM: no cosmological quantity is computed, Ω\_Λ,0 \= 83/121 and Ω\_cdm \= 32/121 are untouched. Nothing here touches the Standard Model couplings: α\_s, sin²θ\_W and α₂ are consumed unchanged from ZS-S1, and no running is refitted. The only external contact is the direction of the α\_s scheme statement in §10.3, which is a caveat and not a prediction.

# **§12. Anti-Numerology and Parameter Firewall**

The numbers 60, 90, 32, π/15, 4π, 230 and 1/120 are geometry and topology outputs. No relation between any of them and **A** or **Q** is asserted anywhere in this paper. The number 1/120 is δ/8π with δ fixed by Gauss–Bonnet alone, and it changes when the carrier changes: the companion tabulates eight vertex-transitive carriers and finds seven distinct values of G₃m \= χ/4N. The clean form G₃m \= 1/|G\_rot| holds only when the rotation stabiliser is trivial, which is true for the truncated icosahedron, the truncated octahedron and the truncated dodecahedron and false for the cube, the dodecahedron and the cuboctahedron, exactly as ZS-S25 Observation S25.11c corrected.

The one quantity that contains **A** is G₃ g²\_YM,3 \= 2A² α\_s(μ)/I\_Φ, which is a BAND and not a number. For its UPPER-ENDPOINT monomial 2A² α\_s a Monte Carlo null was pre-registered and executed. Two hundred thousand random monomials in the locked constants {**A**, **Q**, α\_s, λ₁, λ\_h, c₁, χ, N} with integer exponents in \[−2, 2\] were drawn, and the fraction landing within five per cent of the target was

p \= 0.329 %   (658 / 200 000\)   ≤ 5 %.

This is reported with its exponent range and pool declared, and it is deliberately NOT presented as evidence. The target is itself an exact monomial of the chosen pool, so a low hit rate measures the size of the combinatorial space rather than a physical mechanism. The correct status is therefore: the formula is algebraically derived in §10 from the parent reduction, and the monomial null is an auxiliary anti-pattern diagnostic that carries no independent proof weight. Version 1.2’s sentence “the result is therefore not a coincidence” is withdrawn. \[Check M6.4, weight CT.\]

Every symbol carrying a number is audited in Table 12.1.

Table 12.1. Parameter audit.

| symbol | provenance | free? |
| ----- | ----- | ----- |
| **A** \= 35/437, **Q** \= 11, dim Z \= 2 | inherited **LOCKED**, ZS-F2 and ZS-F5 | no |
| λ₁, λ\_h | inherited **LOCKED**, ZS-S21; recomputed from coordinates | no |
| α\_s \= 11/93 | inherited **DERIVED**, ZS-S1 | no |
| λ\_vac \= 2A² | inherited **DERIVED-CONDITIONAL**, ZS-U5 | no |
| (V, E, F) \= (60, 90, 32), δ \= π/15, χ \= 2 | combinatorics of K\_TI, recomputed | no |
| L⊥ \= 1/(2A M\_P) | output of ZS-F1 mode spectrum | no |
| a, a\_t | lattice spacings; cancel from every reported ratio | no |
| 230, 115, 118 | ranks computed in §5, §6 | no |
| I\_Φ ∈ \[1, 1 \+ **A**\] | transverse profile functional of §2.5; bounded by Lemma S26.P2, value **OPEN** at F-S26.P8 | not fitted, but UNRESOLVED — this is why the coupling is a band and not a point |

No fudge factor, no tuned variable and no external constant is introduced. The lattice spacings a and a\_t appear nowhere in a reported number, which is the content of gate F-S26.N1.

# **§13. Falsification Registry**

Table 13.1. Gate registry, in the same four disjoint classes and with the same membership as the companion: 3 FIRED, 2 executed-and-not-fired, 7 unresolved research OPEN, 6 permanent guards.

| gate | class | fires if | status |
| ----- | ----- | ----- | ----- |
| F-S26.G6 | FIRED | the parabolic rank is not the claimed value | FIRED against the seed target 228; the computed rank is 230 |
| F-S26.C2 | FIRED | the bracket on a six-dimensional active space is strictly Lie | FIRED, in the STRICT sense only; the v1.2 homotopy reading is retracted as S26-R1 |
| F-S26.C7 | FIRED | the exact κ\_p-weighted Hessian selects an active space whose μ is associative | FIRED: no admissible weight does, §9.3–§9.4 |
| F-S26.G9 | PASS | the developing map is not compatible with an actual dissection of K\_TI | executed on all 32 rooted dissections; did not fire |
| F-S26.C8 | PASS | the strict negativity of E₂ is asserted without the pencil hypotheses | executed; Thm S26.C6 and Lemma S26.C6a supply them |
| F-S26.P2 | **OPEN** | λ\_vac \= 2A² is not established upstream | **OPEN** at the upstream ZS-U5 node; NO new transverse scale is introduced in ZS-S26 |
| F-S26.P7 | **OPEN** | the reduced ZS-S14 vacuum term does not supply Λ\_eff \= 0 | **OPEN**; the carrier requires it, the parent has not been integrated |
| F-S26.P8 | **OPEN** | a coupling value is quoted without I\_Φ or outside the band | **OPEN**; closing it collapses the band to a point |
| F-S26.G8 | **OPEN** | no admissible real form or contour for a non-compact ISO(2,1) quantum instrument | **OPEN**; the paper terminates at the classical tier P-Q2 |
| F-S26.G11 | **OPEN** | the BV/BFV master equation with the 60 puncture sources is asserted without construction | **OPEN**; M10 supplies the bulk pair (e, ω) only |
| F-S26.C9 | **OPEN** | a general I-equivariant Hessian has an eigenbasis outside the (σ, ρ)-reachable region | **OPEN** |
| F-S26.C11 | **OPEN** | \[J₆\] is asserted non-zero without a chain contraction (i, p, h) and a transferred ℓ₃ | **OPEN**; S26-R1 |
| F-S26.N1 | GUARD | any reported coupling depends on an untracked a, a\_t or L⊥ | permanent guard |
| F-S26.N3 | GUARD | m\_def, m\_gap and m\_src^YM are conflated | permanent guard |
| F-S26.N5 | GUARD | a coupling number is quoted without its scheme label | permanent guard |
| F-S26.G10 | GUARD | dim H¹\_par \= 230 is read as a count of propagating gravitational degrees of freedom | permanent guard |
| F-S26.C10 | GUARD | Theorem S26.C5 is quoted without its six-dimensional / four-channel scope | permanent guard |
| F-S26.S1 | GUARD | any ZS-S26 result is quoted with the word closed unqualified | permanent guard |

Integrity gates inherited from ZS-S24 and ZS-S25 remain in force: every number is convention-independent, a range, or convention-labelled; Frobenius and unitarily invariant norms are used throughout; no proof-bearing PASS is a literal declaration; no prose claim exceeds what its check tests; and no failed check is removed, replaced or weakened. Two checks in this paper are negative controls whose passing consists of a failure — M3.4, which shows the abelianised holonomy test is insufficient, and M3.10, which shows the deficit sign is not a convention — and they are labelled CT so that they can never be cited as evidence for a value.

# **§14. Non-Claims**

NC-S26.1. The exact face-and-prism integration of ZS-S23 gate F-S23.6 is not performed; {κ\_p}, a₈⁽⁵⁾ and μ of ZS-S24 are not computed and are not used. NC-S26.2. No compact-group transfer-matrix or reflection-positivity theorem is transferred to ISO(2,1). NC-S26.3. dim H¹\_par \= 230 is a cohomological rank, not a count of propagating gravitational degrees of freedom, which in three dimensions is zero. NC-S26.4. No positive gravitational transfer Hamiltonian and no gravitational mass gap is claimed. NC-S26.5. Nothing here bears on Newton's constant in four dimensions; ZS-S25 gate F-S25.5 and non-claim NC-S25.3 remain in force and G₃ g²\_YM,3 may not be promoted to G\_N. NC-S26.6. The intertwiner hypotheses S25.H0 and S25.H1 are neither established nor refuted; §9 decides only the bracket-level question. NC-S26.7. No exhaustive novelty search has been performed against the external literature. NC-S26.8. The Hurwitz system of §5.3 is one intrinsic construction; uniqueness of the dissection class is not claimed, only that closure holds for every one of the thirty-two rooted dissections tested. NC-S26.13 (new in v1.5). The static locus of §6.3 is shown to have half the dimension of H¹\_par; it is NOT shown to be isotropic, so it is a Lagrangian candidate and the Lagrangian property is not claimed. NC-S26.11 (from v1.3). No statement is made about the homotopy or BV double copy: the class \[J₆\] is not computed, and its v1.2 evaluation is retracted as S26-R1. NC-S26.12 (new in v1.3). The exact face-and-prism integration of ZS-S23 gate F-S23.6 is still not performed, so the identification of the residual Hessian freedom with the two orbit ratios (σ, ρ) is inherited from ZS-S21 and ZS-S23 and is not re-derived here. NC-S26.10 (from v1.2). Theorem S26.C6 is proved for the two-parameter orbit-weight family (σ, ρ) that ZS-S21 and ZS-S23 show exhausts the freedom in the exact Hessian; a weighting that is not constant on I-orbits is outside its scope and would break the equivariance the whole reduction rests on. NC-S26.9 (from v1.1). Theorem S26.C5 is a statement about six-dimensional active spaces assembled from the four admissible cubic channels; active spaces of other dimension, in particular the twelve-dimensional span of all four channels, are outside its scope and would require a new equivariance census.

# **§15. Conclusion**

ZS-S25 measured a number, 0.067484, and could not say what it was. This paper says what it is. The cyclic cubic vertex on the Z-Spin active space factorises exactly as ε ⊗ μ over a two-dimensional multiplicity algebra; Jacobi is associativity; and associativity fails, for every weight in the admissible orbit family and for both isotypes, by a sign theorem with exact ℚ(√5) hypotheses. That is a strict statement about a strict structure, and it is the whole of what the gauge side of this paper establishes.

Letting the Hessian weights vary over their full two-parameter freedom does move the algebra — Ω even changes sign, so the naive obstruction alone is not enough — but the second associativity equation E₂ is strictly negative on the whole open quadrant, proved from three exact inequalities computed in ℚ(√5) with integer sign certificates, and the T₂ case follows by an exact Galois descent verified as a 32 × 32 matrix identity. The only other admissible six-dimensional spaces, the mixed T₁ ⊕ T₂ ones, are strict Lie algebras that leak exactly 100 per cent by Schur, an obstruction independent of every weight. The ZS-S25 dichotomy is therefore not an accident of one weight choice but a theorem about the icosahedral representation theory of the carrier — for STRICT Lie structures. Whether a homotopy structure evades it is not decided here and is gate F-S26.C11.

On the gravitational side the paper delivers a classical cellular datum, not a closure. The interface reduction has no free transverse LENGTH, because the Z-anchor Bogomolnyi width is a corpus output; it does have an undetermined transverse FORM FACTOR, bounded to \[1, 1 \+ **A**\]. The singular part of the reduced Hamiltonian constraint gives δ\_v \= 8πG₃m\_v as a derivation rather than an imported dictionary; its smooth part gives Λ\_eff \= 0 as a condition the carrier imposes, whose supply by the parent is **OPEN**. The cellular BV–BFV instrument is imported-proven, and three of the four data it needs are now supplied: the complex, the nondegenerate triad with executable torsion, vielbein-compatibility and temporal-constancy tests, and the source normalisation. The fourth, the master equation including the sixty puncture sources, is not. The defect holonomies close non-abelianly, in translation as well as rotation, for an intrinsically constructed Hurwitz system, on every one of the thirty-two dissections and with no adjustment; and on that same representation the reduced phase space has rank 230, not the 228 the seed asked for.

**CLASSICAL CELLULAR GRAVITY REALISATION DERIVED-CONDITIONAL; STRICT SIX-DIMENSIONAL DOUBLE-COPY ACTIVE-SPACE ROUTE CLOSED-NEGATIVE; THE FULL ACTION-LEVEL BV / L∞ BRIDGE AND THE QUANTUM INSTRUMENT REMAIN OPEN.**

Closure levels attained, after the v1.3 audit: G0 POSITIVE; G1 **DERIVED-CONDITIONAL**, the triad built but not the source-inclusive master equation; G2 **DERIVED-CONDITIONAL** on F-S26.P2, P7 and P8; G3a, the strict six-dimensional Lie route, **CLOSED-NEGATIVE** and **PROVEN** with exact hypotheses; G3b, the full BV/L∞ route, **OPEN**; G4 BANDED to within **A**/(1 \+ **A**) \= 7.42 per cent. This is not the seed's Outcome B and this version does not claim it. The one word that must not be quoted from this paper without its qualifier is 'closed', and the permanent guard F-S26.S1 fires on any citation that drops the qualifier.

What the paper does establish, and what is new to the corpus, is that on the Z-Spin carrier the gauge sector cannot be made simultaneously product-closed and strictly Lie — by a proof, over the whole admissible weight family, with exact algebraic hypotheses, and with the mixed case settled by Schur alone. If a gauge-theoretic origin of Z-Spin gravity exists it is therefore homotopical rather than strict, and the next genuine move is the chain contraction of gate F-S26.C11, not another strict construction.

# **Acknowledgements and Code Availability**

This paper was produced under the Z-Spin adversarial-review discipline established across ZS-S17 through ZS-S25. Two results here refute their own parent: the seed's target rank 228 is replaced by 230, and the exploration-phase holonomy construction — which projected a configuration onto the closure variety and would have been an artefact — is retained in §5.2 only as the limitation it was, with its gate F-S26.G9 discharged in §5.3 by an intrinsic construction. The habit that produced both is ZS-S24 gate F-S24.22: cross-check a claim against an independently computed quantity, never against a restatement of itself. The non-associativity of μ is audited by four diagnostics — the associator norm, the invariant Ω, two thousand GL(2) basis changes, and the contrast against the four two-dimensional commutative associative algebras — and the global statement rests on Theorem S26.C6 rather than on any of them.

The companion zs\_s26\_verify\_v1\_8.py is a single self-contained file, Python 3 with numpy and scipy only. It rebuilds K\_TI from exact Cartesian coordinates with no imported data file, reconstructs the sixty proper rotations of I from the vertex set, recomputes the face-Laplacian spectrum, the four cubic structure constants, the W₆ closure and Jacobi residual, the multiplicity product μ and its invariant, the intrinsic Hurwitz dissections and their holonomy products, the stabiliser and phase-space ranks, the parent-reduction couplings, and the anti-numerology null. It additionally recomputes the entire carrier in exact ℚ(√5) arithmetic, constructs the nondegenerate cellular dreibein and its curvature census, and evaluates the transverse form factor band. It is fail-closed: any FAIL raises. Ledger identifier uniqueness and the absence of literal-True proof-bearing checks are both enforced at run time by assertions on the shipped source. The gate registry is kept in four disjoint classes — FIRED, executed-and-not-fired, unresolved research **OPEN**, and permanent guards — and declarations are held in a separate list that is never counted as PASS. Ledger: 112 executable entries, 112 PASS, 0 FAIL, 3 declarations, distributed over modules M0–M11 as tabulated in Appendix E; gates 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD — the same four classes and the same membership as Table 13.1. SHA256: dce55c71bb93903796df467efa21b8d1ea9cea19b1ebc8fbb927721fbd21de8a.

# **Appendix A. Exact Cell Data**

K\_TI is built from the sixty even-permutation coordinate triples (0, ±1, ±3φ), (±1, ±(2 \+ φ), ±2φ) and (±φ, ±2, ±(2φ \+ 1)) with φ the golden ratio, giving edge length 2 and circumradius 4.95603732. Edges are the ninety vertex pairs at distance 2; faces are the thirty-two supporting planes of the convex hull, twelve pentagons and twenty hexagons, oriented by the outward normal. The incidence matrix B₂ is 32 × 90 and every column has absolute sum 2 and signed sum 0\. The angle deficit at every vertex is π/15 to 5.09 × 10⁻¹⁴ and their sum is 4π to 3 × 10⁻¹³.

# **Appendix B. The Face-Laplacian Spectrum**

Table B.1. Spectrum of Δ₂ \= B₂B₂ᵀ, rebuilt from coordinates.

| eigenvalue | multiplicity | isotype note |
| ----- | ----- | ----- |
| 0.0000000000 | 1 | H₂(S²) \= ℝ |
| 1.2428416164 | 3 | T₁, the corpus gap λ₁ |
| 3.2679491924 | 5 | H |
| 4.8443660283 | 3 | T₂, admissible channel |
| 6.0000000000 | 4 | G |
| 6.7320508076 | 5 | H |
| 7.5210904061 | 3 | T₁, the corpus λ\_h |
| 8.0000000000 | 5 | accidental degeneracy A\_u ⊕ G\_u |
| 8.3917019492 | 3 | T₂, admissible channel |

Nine distinct eigenvalues with multiplicities (1, 3, 5, 3, 4, 5, 3, 5, 3\) summing to 32, independently confirming ZS-S25 §3.7 check C7b.

# **Appendix C. The Intrinsic Dissection Algorithm**

Given a root face f₀: unfold K\_TI along a breadth-first spanning tree T\_d of the dual graph, recording for every face f the planar chart U\_f obtained by successive edge-matching isometries. Assign φ(v) to be the first face in the unfolding order containing v, and set p\_v \= U\_{φ(v)}(v). Build the plane tree T\* by attaching, at each face node f, a segment to every vertex v with φ(v) \= f. Traverse T\* depth-first from f₀, at each node ordering the outgoing edges by their developed angle measured from the incoming direction, and record the vertices in the order their leaves are reached. That sequence is the Hurwitz ordering; the holonomies are h\_v \= t(p\_v) R(−π/15) t(p\_v)⁻¹ for a counter-clockwise traversal. The construction is deterministic given f₀ and is executed for all thirty-two choices.

# **Appendix D. The Exact Pencil and Cup Constants**

For reference, the complete exact data of the two-dimensional reduction, in an orthonormal block basis, with φ the golden ratio. Pencil: P \= 5, S \= 3, R \= 3 ∓ √5, **Q** \= ∓√(5 ± 2√5), upper signs for T₁. Cup tensor: δ \= √5/30 for both isotypes; αγ \= 1/30 and βγ**Q** \= −1/18 for both; βδ − γ² \= −(3 − φ)/60 for T₁ and −(2 \+ φ)/60 for T₂. Every other component of **A**₀ and of Λ vanishes identically, to 1.8 × 10⁻¹⁷ in the companion. These eight numbers are the entire input to Theorem S26.C6.

# **Appendix E. Companion Ledger Summary**

Table E.1. Companion ledger by module. Counts are the companion's own run-time totals; CF closed-form, EX exhaustive, CT control.

| module | content | entries |
| ----- | ----- | ----- |
| M0 | carrier rebuild, census, deficits, Gauss–Bonnet | 7 |
| M1 | face-Laplacian spectrum, four admissible cubic channels, order of I \= 60 | 8 |
| M2 | W₆ \= T₁ ⊗ M, associativity theorem, associator component Ω | 11 |
| M3 | holonomy closure, negative controls, 32 rooted dissections | 10 |
| M4 | stabiliser on the dissection representation, orbit dimension, rank 230, half-dimension check | 8 |
| M5 | interface reduction, branch compatibility, L⊥ scaling, banded G₃g² and G₃m | 10 |
| M6 | anti-numerology null ensemble and the auxiliary Monte Carlo | 4 |
| M7 | weighted-Hessian family, Ω \= 0 locus, mixed spaces, F-S26.C7 | 12 |
| M8 | exact 2 × 2 pencil, closed forms, sign lemma, F-S26.C8 | 13 |
| M9 | exact ℚ(√5) constants, integer sign certificates, Galois descent | 19 |
| M10 | nondegenerate cellular dreibein, torsion, vielbein compatibility, temporal constancy | 7 |
| M11 | transverse form factor and the coupling band | 3 |
| total | — | 112 |

# **References**

\[1\] E. Witten, 2 \+ 1 dimensional gravity as an exactly soluble system, Nucl. Phys. B 311, 46 (1988).  
\[2\] S. Deser, R. Jackiw, and G. 't Hooft, Three-dimensional Einstein gravity: dynamics of flat space, Ann. Phys. (N.Y.) 152, 220 (1984).  
\[3\] A. S. Cattaneo, M. Schiavina, and I. Selliah, BV equivalence between triadic gravity and BF theory in three dimensions, Lett. Math. Phys. 108, 1873 (2018); arXiv:1707.07764.  
\[4\] G. Canepa, A. S. Cattaneo, and M. Schiavina, Fully extended BV–BFV description of general relativity in three dimensions, Adv. Theor. Math. Phys. 26, 3 (2022).  
\[5\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, A cellular topological field theory, Commun. Math. Phys. 374, 1229 (2020); arXiv:1701.05874.  
\[6\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Classical BV theories on manifolds with boundary, Commun. Math. Phys. 332, 535 (2014).  
\[7\] C. Meusburger and B. J. Schroers, Poisson structure and symmetry in the Chern–Simons formulation of (2 \+ 1)-dimensional gravity, Class. Quantum Grav. 20, 2193 (2003).  
\[8\] C. Meusburger, Gauge fixing in (2 \+ 1)-gravity with vanishing cosmological constant, PoS CORFU2011, 051 (2011).  
\[9\] V. V. Fock and A. A. Rosly, Poisson structure on moduli of flat connections on Riemann surfaces and the r-matrix, Am. Math. Soc. Transl. 191, 67 (1999).  
\[10\] D. N. Arnold, R. S. Falk, and R. Winther, Finite element exterior calculus, homological techniques, and applications, Acta Numer. 15, 1 (2006).  
\[11\] M. Reiterer, A homotopy BV algebra for Yang–Mills and colour–kinematics, arXiv:1912.03110.  
\[12\] M. Carrillo González, A. Momeni, and J. Rumbutis, Massive double copy in three spacetime dimensions, J. High Energy Phys. 08, 116 (2021).  
\[13\] S. Deser, R. Jackiw, and S. Templeton, Topologically massive gauge theories, Ann. Phys. (N.Y.) 140, 372 (1982).  
\[14\] E. A. Bergshoeff, O. Hohm, and P. K. Townsend, Massive gravity in three dimensions, Phys. Rev. Lett. 102, 201301 (2009).  
\[15\] S. Carlip, Quantum Gravity in 2 \+ 1 Dimensions (Cambridge University Press, Cambridge, 1998).  
\[16\] Kenny Kang, ZS-F1 v1.0, The Z-Spin action with U(1) completion of the Z-bias field, Z-Spin Cosmology Collaboration (2026).  
\[17\] Kenny Kang, ZS-S14 v2.0, The Z-Spin master action, Z-Spin Cosmology Collaboration (2026).  
\[18\] Kenny Kang, ZS-S23 v1.3, The action-to-Hessian bridge on the physical Z-Spin carrier, Z-Spin Cosmology Collaboration (2026).  
\[19\] Kenny Kang, ZS-S24 v1.9, Finite-carrier action-to-gap closure under the canonical holonomy reduction, Z-Spin Cosmology Collaboration (2026).  
\[20\] Kenny Kang, ZS-S25 v2.1, The cellular double-copy audit of the Z-Spin carrier, Z-Spin Cosmology Collaboration (2026).

# **Version History**

v1.8 FINAL (July 2026, current): Corrects one derivation error found in the final audit of v1.7 and registers it as S26-C1. THE ERROR. Versions 1.0 to 1.7 wrote that the transverse length cancels between the two factors of the coupling, so that G₃g²\_YM,3 is independent of L⊥. That is FALSE. Both factors carry one inverse power of L⊥ — G₃ \= 1/(8π M\_P² L⊥ I\_Φ) and g²\_YM,3 \= g₄²/L⊥ — so the product carries two, G₃g²\_YM,3 \= g₄²/(8π M\_P² L⊥² I\_Φ), and it scales as L⊥⁻². What removes the free transverse scale is not a cancellation but the SUBSTITUTION of the parent-derived width L⊥ \= 1/(2A M\_P). The substituted result, and therefore every number in the paper, is unchanged: G₃g²\_YM,3 \= **A**²g₄²/(2π I\_Φ) \= 2A²α\_s(μ)/I\_Φ \= λ\_vac α\_s(μ)/I\_Φ, with the band 1.404922557 × 10⁻³ to 1.517444958 × 10⁻³. The error was in the narrative only, and the companion computation was correct throughout. THE CONSEQUENCE. Because the product scales as L⊥⁻² before substitution, gate F-S26.P2 controls the OVERALL NORMALISATION of the band and not merely its width, while the fractional width **A**/(1 \+ **A**) is controlled by the independent unknown I\_Φ at gate F-S26.P8. Versions up to 1.7 stated these two roles the other way round. WHAT IS CHANGED. The abstract Certificate G4 paragraph, §2.3, §10.2 and both conditionality statements of §10.3 are rewritten; the structural identity is corrected to G₃g²\_YM,3 \= λ\_vac α\_s(μ)/I\_Φ, with the rational number relabelled as the I\_Φ \= 1 upper endpoint; the companion description of gate F-S26.N5 is corrected in the same way; and §8.4 is retitled the component obstruction, matching its own text. **A** new executable check M5.6b verifies the L⊥⁻² scaling directly, showing that the product multiplied by L⊥² is constant to 10⁻¹⁶ relative over a factor 14.6 in L⊥. Verification advances 111/111 to 112/112 PASS, 0 FAIL; the registry remains 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD.

v1.7 (July 2026): Publishing-consistency patch, responding to an external audit of v1.6. No new computation and no changed number. Five corrections. (i) The most serious: §2.5 and §3.3 did not exist in the body. Both were written for v1.3 but the patch targeted the wrong source file and failed silently, while the abstract, the companion and half a dozen cross-references went on citing them. They are now genuinely present. §2.5 states the transverse form factor, gives Lemma S26.P2 with its radial-clipping proof, and records Retraction S26-R2; §3.3 states the nondegenerate cellular dreibein — the developed coframe with det e \= \+1, the E(2) edge gluings, the discrete torsion T\_f \= 0, the vielbein postulate D\_ω e \= 0, the sixty delta-curvatures of angle π/15, the temporal constancy and hence K\_ij ≡ 0, and the **OPEN** source-inclusive master equation at F-S26.G11. Neither section adds a computation: both are the body-level statement of what modules M10 and M11 already execute. (ii) The abstract and §9.3 no longer claim that the associative variety has codimension two at EVERY non-null two-dimensional commutative associative algebra; they say that the Jacobian of the associator has rank two at the four canonical representatives the companion tests, that this is a diagnostic and not a classification, and that nothing downstream depends on it because the global no-go is the analytic statement E₂ \< 0\. §9.2 is softened in the same way. (iii) Companion checks M7.5 and M7.11 are re-weighted from EX to CN and M7.12 from CF to CT, with messages that attribute the universal statements to Theorem S26.C6 in module M8 and to the Schur argument of §9.4 rather than to their own finite samples. (iv) The trailing blank page is removed. (v) The abstract now says versions 1.3 onward rather than 1.3 to 1.5, and the companion docstring cites §12 rather than a stale section number for the anti-numerology firewall. Verification remains 111/111 PASS, 0 FAIL; the registry remains 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD.

v1.6 (July 2026): Editorial and ledger-consistency release, responding to an external audit of v1.5. No new computation, no new claim and no changed number; eight corrections, all of them agreements between what the document says and what the companion does. (i) Appendix E, Table E.1 was structurally broken — columns and rows had slipped — and is rebuilt from the companion's own run-time totals: M0 7, M1 8, M2 11, M3 10, M4 8, M5 9, M6 4, M7 12, M8 13, M9 19, M10 7, M11 3, total 111\. (ii) Table 13.1 is rebuilt as a four-class gate registry with exactly the membership the companion prints: F-S26.N1, N3, N5 and G10 move from **OPEN** or **CLOSED-PASS** to PERMANENT GUARD, and C10 and S1 are added, so that the front-page count 3 FIRED / 2 PASS / 7 **OPEN** / 6 GUARD is now reproducible from the table itself; F-S26.P2 is stated once, as **OPEN** at the upstream λ\_vac node with no new transverse scale introduced in ZS-S26. (iii) Companion check M4.6 no longer prints 'Lagrangian, consistent'; it is retitled a HALF-DIMENSION CONSISTENCY CHECK and states that isotropy is not tested, matching §6.3 and NC-S26.13. (iv) Two stale Λ\_eff sentences are corrected: §2.4 no longer says the paper computes the normalisation chain including Λ\_eff, and Theorem S26.P1 no longer calls Λ\_eff an output of §2. (v) §3.1 now states that the imported theorems supply the BULK, SOURCE-FREE framework and that their extension to the sixty puncture sources is **OPEN** at F-S26.G11. (vi) The collision audit no longer claims that no numerical value is changed; it says that no locked constant or established upstream result changes, and that one pre-registered seed target, 228, is refuted and replaced by 230\. (vii) §12 now names the Monte Carlo target correctly as the upper-endpoint monomial 2A²α\_s of the coupling band rather than as the coupling itself. (viii) Companion wording: the docstring module list is extended to M11, M2.10 becomes COMPONENT OBSTRUCTION, M7.8 reports 741 LOCATED numerical points and attributes the global statement to Theorem S26.C6 in M8, M7.6 says four canonical representatives tested rather than every non-null algebra, and 'the invariant Ω' becomes 'the non-zero associator component Ω' throughout. The abstract sentence introducing the three inequalities is corrected grammatically. Verification remains 111/111 PASS, 0 FAIL; the registry remains 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD.

v1.5 (July 2026): Terminal consistency release, responding to an external audit of v1.4. No new computation and no new claim; six named corrections and one re-weighting. (i) The retracted minimal-model argument, which in v1.4 still survived as the tail of the abstract's Ω paragraph, is excised: the abstract now says only that the strict bracket fails Jacobi throughout the scoped family and draws no conclusion about homotopy trivialisation. (ii) The abstract's Certificate P is corrected to the banded form, G₃M\_P \= **A**/(4πI\_Φ) with **A**/(4π(1+**A**)) ≤ G₃M\_P ≤ **A**/(4π), and the over-strong summary sentence 'supplies all five' is replaced by an enumeration that names what is supplied and what remains **OPEN**. (iii) §4.2 replaces the point value m\_def \= 1.3075 M\_P by the band 1.3075 ≤ m\_def/M\_P ≤ 1.4122, marking 1.3075 as the I\_Φ \= 1 corner. (iv) The §11 collision audit no longer promotes Λ\_eff \= 0 to **DERIVED**; the promotion made in v1.2 was retracted in v1.3 as S26-R3 and the audit table and prose are brought into line, with the parent supply **OPEN** at F-S26.P7. (v) §9.4 no longer cites the withdrawn Theorem S26.C4; the upstream gates are decided, within the strict scoped family, by Theorems S26.C5–C6. (vi) The static locus of §6.3 is downgraded from Lagrangian to LAGRANGIAN CANDIDATE, since half-dimensionality does not imply isotropy and the restriction of the Goldman form is not computed; new non-claim NC-S26.13 records this. In the companion, check M2.11 is re-weighted from EX to CT and its message rewritten: the two thousand GL(2) samples are a robustness diagnostic and not a proof that Ω is a scalar invariant, the global statement resting on Theorem S26.C6 instead. Table 12.1 gains a row for I\_Φ, so that Zero Free Parameters and an incomplete quantitative closure are visibly compatible: I\_Φ is not fitted, it is unresolved. Verification remains 111/111 PASS, 0 FAIL; gates remain 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD.

v1.4 (July 2026): Consistency release responding to an external audit of v1.3. No new claim and no new number; the work is the removal of contradictions and the completion of three proofs the companion had short-circuited. Document. Every sentence retracted in v1.3 but still present in the body is deleted or relabelled: the minimal-model argument no longer appears as live text and where it is reproduced in §9.1 it is explicitly marked a withdrawn historical argument, under a retitled heading; §2.2 no longer says the profile average is removed and is retitled The transverse length is fixed, the transverse form factor remains bounded; §2.3 carries the banded G₃M\_P rather than the point value; §3.2 and §4.1 no longer call the branch an output of the parent, and gate F-S26.P5 is marked SUBSUMED into the **OPEN** F-S26.P7 rather than **CLOSED-PASS**; §6.3 no longer claims that the stabiliser removes the conditionality of Theorem S26.P1; §2 is retitled Conditional ZS-S14 Interface Reduction; the conclusion is rewritten from its first paragraph and the reference to the seed Outcome B is removed; and Ω is described as one explicit non-vanishing component of the associator in the selected basis rather than as a GL(2) scalar invariant. Companion. The \`or True\` short-circuit in M9.10 is removed and replaced by an actual proof: P\_{T2} \= σ\_Gal(P\_{T1}) is verified as an EXACT 32 × 32 matrix identity in ℚ(√5), the conjugated centroid basis is shown exactly fixed by P\_{T2}, and the T2 pencil and cup constants are recomputed from it and shown term by term equal to the conjugates, so the T2 hypotheses of Theorem S26.C6 are proven rather than inferred. Module M4 is re-run on the dissection-certified holonomies of §5.3 instead of the projected configuration of §5.2, and dim Z(ρ) \= 1 is confirmed on all thirty-two rooted dissections, so the rank-230 statement is made on the representation the paper claims. M10 gains three executable tests — discrete torsion, vielbein compatibility and temporal constancy — so that K\_ij \= 0 is computed rather than interpreted. The gate registry is completed with F-S26.C2, C7, C9, C11 and G8, the duplicate filing of N5 is resolved, and the integrity checker is rebuilt as a paren-balanced scanner that catches \`or True\` and tautological guards as well as literal True. Verification advances 103/103 to 111/111 PASS; gates become 3 FIRED, 2 PASS, 7 **OPEN**, 6 GUARD in both the document and the companion.

v1.3 (July 2026): Responds to an external audit of v1.2 and issues three self-retractions. S26-R1 withdraws Theorem S26.C4: a positive Hessian eigenspace is not the cohomology of a BRST differential, so W₆ is not a minimal L∞ model and the claim \[J₆\] ≠ 0 does not follow; the full BV/L∞ double-copy route is returned to **OPEN** as gate F-S26.C11 and only the strict six-dimensional Lie route stays **CLOSED-NEGATIVE**. S26-R2 withdraws the transverse reduction: a codimension-one reduction requires the transverse average I\_Φ, not the Z-anchor value, so the coupling becomes a two-sided band 2A²α\_s/(1+**A**) ≤ G₃g²\_YM,3 ≤ 2A²α\_s of fractional width exactly **A**/(1+**A**) \= 7.4153 per cent, with gate F-S26.P8 for the profile. S26-R3 withdraws Λ\_eff \= 0 as an output: it is a necessary compatibility condition on the reduced vacuum term, gate F-S26.P7, although the static hypothesis it needs is now derived rather than assumed. New §2.5 defines I\_Φ and proves the band; new §3.3 constructs the NONDEGENERATE cellular dreibein, with det e \= \+1 on all 32 faces, all 90 edge gluings in E(2) with no boost so K\_ij ≡ 0, and 60 delta-curvatures each of angle π/15; new §9.3b is recomputed in exact ℚ(√5) so that the pencil and cup constants and all three closing inequalities carry integer sign certificates rather than floating-point recognition, with the T₂ case settled by Galois descent. Theorem S26.C5 is scoped to the two-parameter diagonal orbit family for its isotypic clause, clause (b) remaining weight-independent by Schur; the anti-numerology Monte Carlo is demoted to an auxiliary diagnostic with no proof weight; the title is corrected from Exact Slab Reduction to Conditional Interface Reduction; and the verdict is rescoped. Companion rebuilt: four disjoint gate classes replace the single **OPEN** list, declarations are separated from executable checks, ledger identifiers are made unique and the uniqueness is enforced, all four literal-True proof-bearing checks are replaced by evaluated conjunctions or by declarations, and modules M9, M10 and M11 are added. Verification advances 82/82 to 103/103 PASS, 0 FAIL. No numerical value of the corpus is changed and no gate is deleted.

v1.2 (July 2026): Discharges the last residual of v1.1. New §9.3b promotes Theorem S26.C6 from EXHAUSTIVE to **PROVEN** by an exact reduction rather than an elimination. Because T₁ and T₂ each occur once in the pentagon block and once in the hexagon block, the weighted problem collapses to a 2 × 2 pencil with exact algebraic constants P \= 5, S \= 3, R \= 3 ∓ √5, **Q** \= ∓√(5 ± 2√5) — the two isotypes being Galois conjugates under √5 ↦ −√5 — and the cochain cup tensor collapses to four monomials, verified to 1.8 × 10⁻¹⁷. Separating the eigenvalue normalisation gives closed forms P₂ \= −gσD²y\_A(βσx\_A \+ γy\_A) and P₃ \= σ²D²y\_B\[gβx\_B \+ (βδ − γ²)y\_B\] with E₂ \= (tP₂ \+ P₃)/(λ\_Aλ\_B)². New Lemma S26.C6a fixes the eigenvector component signs from **A**₁ ≻ 0 and PR \> 0, and the three exact inequalities βδ − γ² \< 0, αγ \= 1/30 \> 0 and βγ**Q** \= −1/18 \< 0 — the last two rational and identical on both isotypes — close the sign on the whole open quadrant (0, ∞)². Gate F-S26.C8 is **CLOSED-PASS**. New Table 9.2 records the exact pencil constants and new Appendix D the complete reduction data. New non-claim NC-S26.10 bounds the theorem to I-orbit-constant weights. Companion module M8 added; verification advances 69/69 to 82/82 PASS, 0 FAIL, **OPEN** gates 5 to 4\. No claim is withdrawn, no number changes, and no gate is deleted.

v1.1 (July 2026): Closes the single **OPEN** route left by v1.0. New §9.3 executes gate F-S26.C7 over the full two-parameter admissible weight family (σ, ρ): the associative variety is shown to have codimension two, so counting does not decide the question; the isotypic active space is shown product-closed for every weight (leakage below 7 × 10⁻¹⁵); the locus Ω \= 0 is shown non-empty, so Theorem S26.C3 alone is insufficient; and Theorem S26.C6 establishes that the second associativity equation E₂ is strictly negative on that entire locus, over 741 located curve points, so no admissible weight makes μ associative. New §9.4 settles the remaining mixed active spaces T₁ ⊕ T₂ by Schur's lemma: they are strict Lie algebras so(3) ⊕ so(3) with associative multiplicity algebra ℝ ⊕ ℝ, but their mixed block leaks exactly 100 per cent because T₁ ⊗ T₂ \= G ⊕ H, an obstruction that is weight-independent. Theorem S26.C5 combines the two into an exhaustive dichotomy and Gate F-S26.C7 is **CLOSED-NEGATIVE**, making Certificate C unconditional. New Table 9.1 records the three associativity residuals at all five corpus-named weight points. New gate F-S26.C8 records that the sign statement of Theorem S26.C6 is exhaustive rather than analytic, and new non-claim NC-S26.9 bounds Theorem S26.C5 to six-dimensional active spaces. Companion module M7 added; verification advances 57/57 to 69/69 PASS, 0 FAIL, **OPEN** gates 4 to 5\. No claim of v1.0 is withdrawn, no number changes, and no gate is deleted.

v1.0 (July 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v0.9.3, and from the ZS-S26 integrated seed report v1.1.) Certificate P: interface reduction across the Z-sector under Z \= ∂X, transverse measure fixed by the Z-anchor Bogomolnyi width, G₃ M\_P \= **A**/4π and g²\_YM,3 \= 2A g₄² M\_P. Theorem S26.P1: Λ\_eff \= 0 and δ\_v \= 8πG₃m\_v derived together from the reduced Hamiltonian constraint, discharging seed corrections C-S26.4 and C-S26.5. Certificate G: cellular BV–BFV instrument imported-proven from \[3\], \[4\], \[5\] with the three missing Z-Spin data supplied. Theorem S26.G3′: intrinsic Hurwitz dissection and exact ordered ISO(2,1) closure on all thirty-two rooted dissections, discharging F-S26.G4 and F-S26.G9. Theorem S26.G2: dim H¹\_par \= 230, refuting the seed target 228; correction C-S26.8 issued. Theorems S26.C1–C4: ℓ₂ \= ε ⊗ μ, Jacobi equals associativity, invariant obstruction Ω ≠ 0, \[J₆\] ≠ 0; Certificate C **CLOSED-NEGATIVE**. Theorem S26.P4: G₃ g²\_YM,3 \= λ\_vac α\_s, closing ZS-S25 gate F-S25.22. Quantum tier terminated at P-Q2. Verification 57/57 PASS, 0 FAIL, 4 **OPEN** gates; anti-numerology Monte Carlo executed at p \= 0.329 per cent. **A**, **Q**, dim Z, λ₁, λ\_h all **LOCKED** and none re-fitted.  
