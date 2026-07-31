# **ZS-S21**

# **The Instrument Construction: Closing the Cellular Transfer-Matrix / Hodge-Measure Sub-Bridge of Z-Spin Yang–Mills**

*Formerly titled “Closing the Z-Spin Yang–Mills Bridge by Transfer Matrix” (v1.0, v1.1). The title is scope-corrected in v1.2 so that the qualifier travels with the citation rather than being lost with a subtitle.*

Author: Kenny Kang  
Affiliation: Z-Spin Cosmology Collaboration  
Date: July 2026  
Theme / Paper Code: Standard Model — ZS-S21  
Version: v1.2 TERMINAL — supersedes v1.1 (July 2026\) and v1.0 (March 2026\)

**Verification: 88/88 PASS | 1 PROXY | 24 DECL | 0 FAIL | Zero continuous dimensionless parameters under (H-W) ∧ (Z-A0) ∧ (Z-A1); two ratios σ and ρ survive without (Z-A1) | A \= 35/437, Q \= 11, dim Z \= 2, λ₁ \= 1.2428416164 — all LOCKED, none re-fitted**

# **§0.0 Scope Declaration**

**Read this before the abstract.** In this paper the phrase “Yang–Mills bridge” denotes the **cellular transfer-matrix / Hodge-measure sub-bridge** only, namely the chain  
ZS-S14 group-valued cellular action  →  transfer matrix  →  diagonal Hodge measure  →  dimensionless quadratic spectrum .  
It does NOT denote closure of the full non-perturbative SU(3) glueball phenomenology. Specifically, and by the accounting ZS-S18 itself set out, the following remain outside the closure claimed here: the exact Wilson quartic; the non-Abelian Gauss–Coulomb–Faddeev–Popov reduction; the full 31-mode non-perturbative Lanczos spectrum; the absolute glueball interaction coefficient; and the running-coupling and continuum scheme-matching programme. Every O(g²) statement of ZS-S17 to ZS-S20 remains DERIVED-PERT-COND at λ\_t ≈ 5.54 and is not improved here. What the transfer-matrix construction does supply is a non-perturbative definition of the instrument, which is a different and narrower thing.

# **§0.1 Abstract**

ZS-S20 established, over ten review cycles, that no condition formulated inside the quadratic cellular action can select the Hodge measure (M₁, M₂) that the reduction of the ZS-S14 SU(3) Yang–Mills action onto the truncated-icosahedron complex K\_TI requires. That result is correct and is imported here without modification. This paper acts on its diagnosis rather than on its conclusion: in lattice gauge theory the quadratic Hamiltonian is not a datum to be selected but an output of the transfer matrix, constructed from a group-valued action. ZS-S21 performs that construction.

Theorem S21.1. Under (H-W) — that the cellular reduction is a Wilson-type group-valued plaquette action with compact link variables and nearest-neighbour coupling in time — the temporal plaquettes on K\_TI × a\_tℤ stand in exact bijection with the 90 edges and the spatial plaquettes with the 32 faces, and no third class of 2-cell exists because dim K\_TI \= 2\. Consequently M₁ and M₂ are diagonal in the edge and face bases, and they are diagonal for every weight assignment, not merely for the uniform one. Gate F-S20.5, the non-diagonal I\_h-equivariant family that ZS-S20 left as its one genuine remaining mathematical risk, is thereby SUPERSEDED-BY-CONSTRUCTION: there is no family to search.

Lemma S21.2 and Corollary S21.2a. All 90 edges of an Archimedean solid are congruent, so all 90 temporal plaquettes e × a\_t are congruent as primal cells and are all quadrilaterals. No weight built from the plaquette’s own primal geometry can separate the two edge orbits; that much is PROVEN and unconditional. Weight uniformity itself is not. The (5,6) and (6,6) orbits have different ambient stars, so the metric-free function ψ\_e({deg f : f ⊃ e}) and every dual measure do separate them. The companion computes the circumcentric dual-length ratio and obtains 0.8973272361 intrinsically and 0.9105929973 chordally — the second reproducing the ZS-S20 Table 17.1 flat-cone value independently — and confirms that the transfer matrix returns diag(β\_e) for orbit-dependent temporal weights exactly as it returns diag(β\_f) for orbit-dependent spatial ones. Version 1.1’s claim that σ \= 1 is unconditional is therefore RETRACTED (Retraction S21-R3): σ \= 1 is DERIVED-CONDITIONAL, on exactly the same footing as ρ \= 1\.

Reported against interest, twice. First, the seed hypothesis that the Wilson action carries a single spatial coupling by construction is refuted for non-regular complexes: the standard random-lattice gauge action of Christ, Friedberg and Lee weights each plaquette by the ratio of its dual measure to its own, and on K\_TI the 12 pentagons and 20 hexagons are not congruent (A₆/A₅ \= 1.5100902868). Second — and this is the correction that produces v1.1 — the inference made in v1.0, that a metric-free carrier alone forces β₅ \= β₆, is INVALID. The family β\_f \= β\_s ψ(n\_f) is metric-free and realises every ρ \> 0\. That is the ψ(n\_f) obstruction which ZS-S19 v1.3 discovered and retracted, recurring one level up. Version 1.0's Corollary S21.2 is retracted (Retraction S21-R2) and replaced.

The axiom structure is therefore as follows. (Z-A0), Metric-Free Carrier, removes every dual-measure and area branch. (Z-A1), the Orbit-Blind Plaquette Reduction Postulate — expanded in v1.2 to cover BOTH anisotropy classes — removes every ambient-combinatorial branch, temporal and spatial alike. Only together do they give β\_e \= β\_t for all 90 edges and β\_f \= β\_s for all 32 faces, hence M₁ \= m·I₉₀, M₂ \= β·I₃₂, σ \= ρ \= 1 and Δ₂ \= r·B₂B₂ᵀ with r \= β\_s/(β\_t a\_t²). (Z-A1) is the ZS-S19 counting axiom R\_C restated at the level of the group-valued action and extended to the temporal class. What the transfer matrix contributes is precise and limited: it PROVES diagonality and it PROPAGATES orbit weights. It does not select them, in either class, and §6.3 reports that as a negative result of the construction rather than burying it.

The surviving branches are separated observably and non-uniformly, and the discriminator is branch-robust. In the counting branch the third-lowest excitation has multiplicity 3 and isotype T₂u; in the spatial-only Christ–Friedberg–Lee branch and in the full metric branch alike it has multiplicity 4 and isotype G\_u. The scale-free ratio ω(T₂u,1)/ω(T₁u,1) is 1.9742883436 in the counting branch against 2.2042305068 and 2.2154919435 in the two metric branches, separations of 11.65 % and 12.21 %, whereas the ratio to the lowest H\_g separates by only 0.53 %. Gate F-S21.8 is defined on the former, not the latter, and it therefore discriminates orbit-blind from orbit-sensitive weighting rather than merely one metric from another.

A further correction concerns the observable itself. The transfer-matrix Hamiltonian is a system of coupled harmonic oscillators, so normal-mode energies obey ω\_k \= √(r λ\_k) and the falsifiable table is the table of √(λ\_k/λ₁), not of λ\_k/λ₁. This is verified end-to-end by exact diagonalisation of the compact U(1) Kogut–Susskind Hamiltonian on a finite model complex carrying the same two-face-orbit / two-edge-orbit pathology as K\_TI.

Nine errata are reported and corrected in §11 — five in the standing corpus and four against earlier versions of this paper — the most consequential of the corpus ones being that Ω²(K\_TI) does not contain all ten I\_h irreducible representations, it contains six, and that the level λ \= 8 of multiplicity five is not an H irrep but an accidental degeneracy A\_g ⊕ G\_g which splits for every ρ ≠ 1\.

The verdict is stated in §15. The cellular transfer-matrix / Hodge-measure sub-bridge is CLOSED at DERIVED-CONDITIONAL on three explicitly named statements — (H-W), (Z-A0), (Z-A1) — none of which is a fitted number. No continuous dimensionless parameter survives the stated postulate; two survive without it; one dimensionful scale is calibrated. It is not closed at unconditional DERIVED, and we do not say that it is. This is the terminal release of the S-line on this question.

# **§0.2 Hypothesis Register**

Exactly three statements carry the closure. None is a free parameter; each is falsifiable and each has its own gate.

Table 0.1. The three named hypotheses of ZS-S21 v1.2, what each buys, and its gate. (Z-A1) was expanded in v1.2 to cover the temporal class after Retraction S21-R3.

| Tag | Statement | Used by | Gate |
| ----- | ----- | ----- | ----- |
| (H-W) | The cellular reduction of ZS-S14 onto K\_TI × a\_tℤ is a Wilson-type group-valued plaquette action: compact link variables, one holonomy term per 2-cell, nearest-neighbour coupling in time. ZS-S14 does not prove this; ZS-S19 §4.11 pre-registered it as one of three candidate reduction routes. It is a hypothesis and is named as one. | Thm S21.1, Thm S21.2, everything downstream | F-S21.11 |
| (Z-A0) | Metric-Free Carrier. K\_TI enters the reduction with incidence data (B₁, B₂) and the I\_h action only. No area, length, dual volume or embedding is supplied. | removes β\_f ∝ 1/A\_f and β\_e ∝ |⋆e|/|e|, i.e. every metric branch, temporal and spatial | F-S21.7 |
| (Z-A1) | Orbit-Blind Plaquette Reduction Postulate (EXPANDED in v1.2). Within each anisotropy class the character-kernel coefficient is independent of every ambient combinatorial orbit and of every dual-cell datum: β\_e \= β\_t for all 90 edges and β\_f \= β\_s for all 32 faces. In particular it is independent of the edge-star type (5,6)/(6,6), of the face degree 5/6, of the face and edge orbits, and of any functions ψ\_e, ψ\_f of those data. | removes β\_e \= β\_t ψ\_e({deg f : f ⊃ e}) and β\_f \= β\_s ψ(n\_f); together with (Z-A0) gives σ \= ρ \= 1 | F-S21.10 |

**On the honest cost of (Z-A1).** It is not derivable inside the reduction, and §15.4 says so in one sentence. It is the same choice ZS-S19 named R\_C, moved from the quadratic action to the group-valued one and extended from the spatial class to both. What has changed is its status in the search space: in ZS-S19 it was one prescription among a continuum of live alternatives on an object with 181 undetermined diagonal directions; after Theorem S21.1 the whole non-diagonal question is empty, and what remains is two numbers, σ and ρ, on which exactly two families compete — the ambient-combinatorial family, removed by (Z-A1), and the dual-measure family, removed by (Z-A0). (Z-A1) is therefore the **last** remaining choice rather than one of many, and it is the choice on which the whole S-line now turns. It buys two numbers, not one.

# **§0.3 Outcome Registry and Revision History**

Outcomes A to D were pre-registered in v1.0 before the §4–§6 computations were executed. Outcomes A′, A″ and A‴ are post-review corrective classifications and are NOT pre-registered; they are recorded here so that the revision history is legible rather than hidden in a version note.

Table 0.2. Outcome registry. A–D are pre-registered (v1.0); A′, A″, A‴ are post-review corrective classifications added after the fact and are labelled as such.

| Outcome | Registration | Trigger | Consequence | Realised |
| ----- | ----- | ----- | ----- | ----- |
| A — clean closure | Steps 1–3 give M₁ \= m·I and M₂ \= β·I with no orbit dependence and no prescription choice | Bridge CLOSED at DERIVED | NO |  |
| A′ — closure on one axiom | post hoc (v1.0) | M diagonal and M₁ uniform unconditionally; M₂ uniformity from a metric-free axiom alone | Bridge CLOSED on one axiom | NO — invalid; Retraction S21-R2 |
| A″ — closure on a named triple, M₁ unconditional | post hoc (v1.1) | M diagonal and M₁ uniform under (H-W) alone; only M₂ needs the axioms | Sub-bridge CLOSED with one conditional ratio | NO — the ambient star separates the edge orbits; Retraction S21-R3 |
| A‴ — closure on a named triple, both ratios conditional | post hoc (v1.2) | M diagonal under (H-W); σ and ρ both uniform only under (Z-A0) ∧ expanded (Z-A1) | Sub-bridge CLOSED at DERIVED-CONDITIONAL on (H-W) ∧ (Z-A0) ∧ (Z-A1). The construction proves diagonality and propagates, rather than selects, orbit weights in both classes. No continuous dimensionless parameter survives the postulate; two survive without it. | YES |
| B — anisotropy branch | PRE-REGISTERED (v1.0) | β\_t ≠ β\_s in a way not absorbable into a\_t | Closed with one extra measurable dimensionless number | NO — ξ is absorbed into r |
| C — orbit dependence forced | PRE-REGISTERED (v1.0) | The transfer matrix genuinely produces orbit-dependent m\_e or β\_f | §4 falsified; the Wilson prescription is incompatible with K\_TI | NO — but the correct reading is that the transfer matrix is AGNOSTIC in BOTH classes: it neither produces nor removes orbit dependence, it propagates it (checks T064, T065) |
| D — reflection positivity fails | PRE-REGISTERED (v1.0) | T not self-adjoint or not positive on the non-bipartite complex | Hard fork | CANNOT FIRE — removed; see §7.3 |

# **§0.4 Epistemic Status Legend**

Table 0.3. Epistemic status legend used throughout ZS-S21.

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Mathematical theorem or exact arithmetic identity, verified to machine precision or symbolically. |
| IMPORTED-PROVEN | Standard result of the external literature, cited and used but not re-proved here. |
| DERIVED | Quantitative consequence of PROVEN items plus the Z-Spin axioms already LOCKED. No new postulate. |
| DERIVED-CONDITIONAL | DERIVED given one explicitly named additional axiom, stated in the body and registered as a gate. |
| DERIVED-PERT-COND | DERIVED within perturbation theory, whose control is not established at λ\_t ≈ 5.54. |
| VERIFIED | Numerical confirmation on the actual Z-Spin object by an executable check in the companion. |
| TESTABLE | A number the framework predicts that an external measurement can contradict. |
| HYPOTHESIS | Structural pattern without a completed derivation chain from the action. |
| OBSERVATION | Numerical proximity, anti-numerology tested, with no action-level derivation. Carries no evidential weight. |
| OPEN | Recognised gap requiring future work. |
| SUPERSEDED-BY-CONSTRUCTION | A gate that has become moot because the object it constrained is no longer selected but manufactured. |
| NON-CLAIM | Quantity explicitly NOT derived; honest acknowledgement of a framework limitation. |
| RETRACTED | A statement previously asserted in this corpus and withdrawn, with the withdrawal recorded. |

# **§1. Why ZS-S20 Could Not Close It**

ZS-S20 is imported here in full and nothing in it is retracted. Its substance is a set of negative theorems whose joint content is a non-identifiability result. \[STATUS: PROVEN\]

Table 1.1. The ZS-S20 non-identifiability core, imported without modification.

| Result | Content |
| ----- | ----- |
| Thm S20.O | D\_M \= d \+ M⁻¹dᵀM is M-self-adjoint for every positive M. Hermiticity selects nothing. Fires gate F-S20.8. |
| Thm S20.N-a | Every positive-definite matrix is already a Gram matrix. The metric is free data. |
| Thm S20.T1 | The transfer free-energy Hessian returns the M that was put in, exactly, for every positive M. |
| Thm S20.R | \[M, D\_K\] \= 0 ⟺ M \= m·I, certified by integer union-find and GF(2³¹−1) arithmetic, rank 181/182. |
| Thm S20.E | (H-UA) is equivalent to its own conclusion. This is the test every new hypothesis must pass. |
| Meta-obs. §19.2 | A fixed-point condition built solely from the action admits the action as a solution, and constrains M only if over-determined. |

Together these say: no condition formulated inside the quadratic action can select M. ZS-S20 then spent ten versions proposing such conditions anyway, and each proposal was found equivalent to its own conclusion. The failure was not one of ingenuity. It was that the question was malformed.

# **§2. The Diagnosis: M Is an Output, Not a Datum**

In lattice gauge theory the quadratic Hamiltonian is never postulated alongside the action. Kogut and Susskind derived it from Wilson's action \[1\]; Creutz gave the transfer-matrix construction that performs the derivation \[4\]; Lüscher proved that the resulting transfer operator is self-adjoint and strictly positive, so that its logarithm exists and the Hamiltonian has real spectrum \[2\]; Osterwalder and Seiler supplied the reflection positivity that is the hypothesis of Lüscher's theorem \[3\]. In that chain the measure is read off from the action; it is never selected.

ZS-S20 never built a transfer matrix. It took the quadratic action as given and searched for a condition on M. ZS-S20's own gate F-S20.14 named the way out: a non-quadratic or coarse-graining step. The transfer matrix is exactly such a step — the input is a group-valued, non-quadratic Wilson action and the output is a quadratic Hamiltonian. This paper closes F-S20.14. \[STATUS: DERIVED\]

Two things must be said at once. First, the construction requires an input that ZS-S14 does not itself supply: that the reduction be of Wilson type, with compact link variables and one holonomy per 2-cell. ZS-S19 §4.11 pre-registered three candidate reduction routes — counting, Whitney/Galerkin, and mass-lumped circumcentric DEC — and did not select among them. We therefore name the assumption (H-W) rather than pass it off as a definition, and register gate F-S21.11 against it. Second, performing the construction does not by itself dispose of the measure question. It relocates it. Where ZS-S20 asked which M, ZS-S21 must ask with what weights the plaquette terms enter on a complex whose cells are not all congruent. §6 shows that this relocation is a real and large gain — every alternative but two is eliminated by construction — and also that it is not, by itself, a closure.

# **§3. K\_TI × a\_tℤ and the Anisotropic Wilson Action**

## **3.1 The complex**

K\_TI is rebuilt from first principles in the companion, from the standard coordinates of the truncated icosahedron, with no imported data file. The census is metric-free. \[STATUS: PROVEN — checks T010–T020\]

Table 3.1. The complex K\_TI. All entries are computed, not quoted.

| Object | Count | I\_h orbits | Check |
| ----- | ----- | ----- | ----- |
| vertices | 60 | 1 — vertex-transitive | T010 |
| edges | 90 | 2 — 60 of type (5,6), 30 of type (6,6) | T019 |
| faces | 32 | 2 — 12 pentagons, 20 hexagons | T020 |
| χ \= V − E \+ F | 2 | — | T011 |
| |Aut(K\_TI)| | 120 \= |I\_h| | — | T040 |
| rank B₁ (exact) | 59 | — | T014 |
| rank B₂ (coexact) | 31 | — | T015 |
| harmonic | 0 — H¹(K\_TI) \= 0 | — | T016 |

The chain complex is exact: B₂B₁ᵀ \= 0 to machine zero (max |B₂B₁ᵀ| \= 0.0, check T013), and the metric-free Hodge census is 90 \= 59 \+ 31 \+ 0\.

## **3.2 The 2-cells of K\_TI × a\_tℤ**

Put the theory on K\_TI × a\_tℤ in temporal gauge. Because K\_TI carries no 3-cells, the 2-cells of the product complex fall into exactly two classes, and no third class exists. \[STATUS: PROVEN — checks T050–T052\]

Table 3.2. Plaquette census on K\_TI × a\_tℤ, per time slab.

| Plaquette class | Geometric content | Count | Coupling |
| ----- | ----- | ----- | ----- |
| temporal | (edge e) × (one time step) | 90 — one per edge, bijection verified (T051) | β\_t |
| spatial | face f | 32 — one per face | β\_s (pentagons), β\_s (hexagons); see §6 |
| any other | — | 0 — dim K\_TI \= 2, no 3-cells (T052) | — |

The anisotropic Wilson action is  
S \= β\_s Σ\_f \[1 − (1/N) Re Tr U\_f\] \+ β\_t Σ\_e \[1 − (1/N) Re Tr( V\_e(t+a\_t) V\_e(t)† )\] ,   (3.1)  
with U\_f the holonomy around face f and V\_e the spatial link on edge e.

## **3.3 (H-TR) is a unit choice, not a hypothesis**

ZS-S20 carried Tr Δ₂ \= 2E as a hypothesis (H-TR). It is not one. With M₁ \= diag(m\_e) and M₂ \= diag(β\_f), Tr Δ₂ \= Σ\_f β\_f n\_f / m, so for every shape ratio ρ there is exactly one positive scale r that satisfies it. The companion solves it symbolically at ρ \= 0.8, 1.0, 1.3, obtaining r \= 1.0714285714, 1.0000000000, 0.9090909091 (check T090), and at ρ \= 1 it returns r \= 1, which is the a\_TI \= 1 convention (check T091). (H-TR) fixes units and constrains no shape. ZS-S21 therefore inherits one hypothesis where ZS-S20 had two, and adopts Tr Δ₂ \= 2E throughout as the single stated normalisation convention. \[STATUS: PROVEN\]

# **§4. Theorem S21.1 — The Transfer Matrix Produces a Diagonal M**

## **4.1 The construction**

Work in temporal gauge. The transfer operator is T \= A K A with A \= exp(−½ β\_s Σ\_f \[1 − (1/N)Re Tr U\_f\]) diagonal in the link representation and K the temporal kernel, which factorises over edges because each temporal plaquette involves exactly one edge variable at two adjacent times. For U(1) the construction is exact and Gaussian. Expanding the kernel in characters,  
⟨n|K|n′⟩ \= δ\_{nn′} Π\_e I\_{n\_e}(β\_t)/I\_0(β\_t) ,   −log\[I\_n(β\_t)/I\_0(β\_t)\] \= n²/(2β\_t) \+ O(β\_t⁻²) ,   (4.1)  
and taking H \= −lim\_{a\_t→0}(1/a\_t) log T gives the Kogut–Susskind form  
H \= (1/2) Σ\_e E\_eᵀ M₁⁻¹ E\_e \+ (1/2) Σ\_f Φ\_f M₂ Φ\_f \+ O(Φ⁴) ,   M₁ \= β\_t a\_t , M₂ \= β\_s/a\_t ,   (4.2)  
with Φ \= B₂θ. The extension to SU(2) is by character expansion, using the heat-kernel semigroup already VERIFIED in the corpus to 2.8 × 10⁻¹⁷; the extension to SU(3) is representation-theoretic and leaves the incidence structure untouched (§7).

## **4.2 Statement and proof**

**Theorem S21.1 (Instrument Construction and Diagonality).** Assume (H-W): the cellular reduction of the ZS-S14 SU(3) Yang–Mills action onto K\_TI × a\_tℤ is the anisotropic Wilson action (3.1), with a possibly cell-dependent weight on each 2-cell. Let T be the Osterwalder–Seiler / Lüscher transfer matrix and H \= −lim\_{a\_t→0}(1/a\_t) log T. Then M₁ and M₂ are diagonal in the edge and face bases respectively, with M₁ \= diag(β\_e a\_t) and M₂ \= diag(β\_f/a\_t), for EVERY weight assignment {β\_e}, {β\_f}. No off-diagonal entry can be generated. Consequently  
Δ₂ \= M₂^{1/2} B₂ M₁⁻¹ B₂ᵀ M₂^{1/2} ,    r \= β\_s/(β\_t a\_t²) .   (4.3)  
**\[STATUS: DERIVED under (H-W) — checks T060–T064\]**

Proof. The temporal term of (3.1) is a sum over the 90 temporal plaquettes, and by the bijection of Table 3.2 each such plaquette contains exactly one edge variable. Its Hessian with respect to the link differences is therefore supported on the diagonal. The companion computes this Hessian as a literal 90 × 90 matrix by fourth-order finite differencing on the actual K\_TI edge set and finds max |H\_t − β\_t I₉₀| \= 1.41 × 10⁻⁷ with the off-diagonal part vanishing identically (checks T060, T061). The spatial term is a sum over the 32 faces, and its Hessian with respect to θ is computed as a literal 90 × 90 matrix and found equal to β\_s B₂ᵀB₂ with max deviation 1.49 × 10⁻⁷ (check T062), with no edge–edge coupling outside the incidence pattern of B₂ᵀB₂ (check T063). The same computation repeated with deliberately orbit-dependent weights β₅ \= 1.3, β₆ \= 0.8 returns B₂ᵀ diag(β\_f) B₂ to 1.74 × 10⁻⁷ (check T064), so diagonality is a property of the incidence structure and not of the uniform branch. Hence in the face basis M₂ is diagonal for every weight assignment. ∎

**Corollary S21.1a.** Gate F-S20.5 — the non-diagonal I\_h-equivariant family, which ZS-S20 left as its one genuine remaining mathematical risk — is **SUPERSEDED-BY-CONSTRUCTION**. The transfer matrix does not select from a family; it produces one M, and that M is diagonal. There is nothing to search. The undetermined directions collapse from order 6 × 10³ for general symmetric positive M, and from 181 for the diagonal family after removal of the overall scale, to the four orbit weights (m₅₆, m₆₆, β₅, β₆), that is three ratios.

# **§5. Temporal-Plaquette Congruence Is Unconditional; Weight Uniformity Is Conditional**

Version 1.1 of this paper claimed more for this section than the computation supports, and the claim is retracted here before it is used. The correct statement is a PROVEN lemma about primal geometry followed by a DERIVED-CONDITIONAL corollary about weights.

## **5.1 Lemma S21.2 — primal congruence**

**Lemma S21.2 (Primal Temporal-Plaquette Congruence).** Assume (H-W). The 90 temporal plaquettes of K\_TI × a\_tℤ are congruent as primal cells and are all quadrilaterals with the same side data. Consequently no weight built solely from the plaquette's own primal geometry or its own combinatorial type can distinguish the (5,6) edge orbit from the (6,6) edge orbit.  
**\[STATUS: PROVEN — checks T053, T054, T074\]**

Proof. A temporal plaquette is the product cell e × a\_t. Its primal geometry is fixed by the pair (|e|, a\_t). The truncated icosahedron is Archimedean, so the companion computes all 90 edge lengths directly from the vertex coordinates and finds a spread of 1.12 × 10⁻⁹, with the two orbit means differing by 8.9 × 10⁻¹⁰ (checks T053, T074). Since a\_t is common, all 90 primal cells are congruent. They are also combinatorially indistinguishable as cells: every temporal plaquette is a quadrilateral, so a degree function ψ(n\_p) evaluated on the plaquette itself is constant across all 90\. ∎

## **5.2 The temporal ambient-star obstruction — reported against interest (iii)**

Lemma S21.2 does not give σ \= 1, and version 1.1's assertion that it does is the third self-retraction of this paper. The reason is exact and is the same reason ρ was not fixed by (Z-A0) alone.

**Retraction S21-R3 (v1.2, against v1.1).** Version 1.1 titled this section “Edge-Orbit Uniformity Is Unconditional” and stated Theorem S21.2 as holding “for every intrinsic weight prescription — metric-induced, area-based, dual-measure-based or counting alike”. That is too strong on both counts. Theorem S21.1 explicitly writes M₁ \= diag(β\_e a\_t), so (H-W) permits a different coefficient on each temporal plaquette; and the two edge orbits, though of equal primal length, have **different ambient stars**: a (5,6) edge borders a pentagon and a hexagon, a (6,6) edge borders two hexagons. Hence the metric-free assignment β\_e \= β\_t·ψ\_e({deg f : f ⊃ e}) realises every σ \> 0, and every dual measure separates the orbits outright. Version 1.1's §5 heading, its unconditional status tag, and the phrase “requires no axiom” are RETRACTED.

The obstruction is made executable rather than left as an argument. First, the transfer matrix propagates temporal orbit dependence exactly as it propagates spatial orbit dependence: with β₅₆ \= 1.3 and β₆₆ \= 0.8 the companion computes the literal 90 × 90 temporal Hessian and obtains diag(β\_e), with the two orbit entries at 1.300000 and 0.800000 and maximum deviation 1.08 × 10⁻⁷ (check T065). Second, the dual measures are computed and are unequal:

Table 5.1. Primal and dual measures of the two edge orbits. The primal lengths coincide; every dual measure does not. All entries computed on the regular K\_TI, unit edge.

| Quantity | (5,6) orbit, 60 edges | (6,6) orbit, 30 edges | ratio | check |
| ----- | ----- | ----- | ----- | ----- |
| primal length |e| | 1.0000000000 | 1.0000000000 | 1.0000000000 | T053, T074 |
| intrinsic dual |⋆e| \= a₅ \+ a₆ vs 2a₆ | 1.5542163640 | 1.7320508076 | 0.8973272361 | T075 |
| chordal circumcentric dual | 1.4733704195 | 1.6180339887 | 0.9105929973 | T075, T076 |

The second row's ratio 0.9105929973 is precisely the flat-cone value m₅₆/m₆₆ recorded in ZS-S20 Table 17.1, here reproduced independently from a rebuilt complex and an independently constructed dual (check T076). That agreement is a strong consistency test of both computations, and it also settles what ZS-S20 §17.1a left open: the anchoring value 1.2550451434 and the flat-cone value 0.9105929973 are not a contradiction to be resolved by declaring one of them wrong about the Z-sector. They are two points in a one-parameter family that the transfer matrix does not narrow.

Third, the family is live: the companion evaluates σ ∈ {0.8, 0.9, 1.0, 1.15, 1.3} and obtains five distinct λ₁ spanning 1.0600 to 1.4381 (check T077). σ is a genuine continuous freedom under (H-W) alone.

## **5.3 Corollary S21.2a — electric-orbit uniformity, conditionally**

**Corollary S21.2a (Electric-Orbit Uniformity).** Under (H-W) ∧ (Z-A0) ∧ (Z-A1) as stated in §6.4 — that is, once the dual-measure family and the ambient-combinatorial family are both excluded — β\_e \= β\_t for all 90 edges, hence M₁ \= m·I₉₀ and σ \= m₅₆/m₆₆ \= 1\.  
**\[STATUS: DERIVED-CONDITIONAL on (H-W) ∧ (Z-A0) ∧ (Z-A1) — checks T060, T061, T071\]**

Table 5.2. The electric orbit ratio σ and the resulting spectral gap, in the (H-TR) convention. Only the last row is compatible with the LOCKED λ₁, and it is the value the orbit-blind postulate selects.

| σ \= m₅₆/m₆₆ | Origin | λ₁ | Status |
| ----- | ----- | ----- | ----- |
| 1.2550451434 | (H-UA), ZS-S20 §17.1a | 1.0820156095 | one point of the family; not derived |
| 0.9105929973 | chordal circumcentric dual — excluded by (Z-A0) | 1.3197876963 | metric branch |
| 0.8973272361 | intrinsic polyhedral dual — excluded by (Z-A0) | see §6.5 Table 6.2 | metric branch |
| 1.0000000000 | orbit-blind counting — selected by (Z-A1) | 1.2428416164 (LOCKED) | DERIVED-CONDITIONAL |

That the postulated σ \= 1 returns the independently LOCKED λ₁ remains a non-trivial consistency check rather than a fit: λ₁ was locked in ZS-S7 and ZS-S17 before the transfer-matrix construction existed, and no quantity in §5 was tuned to reproduce it. It is not, however, evidence for (Z-A1), and §13 declines to use it as such.

# **§6. The Residual: Two Ratios σ and ρ, and the Two Axioms That Fix Them**

## **6.1 Reported against interest (i) — the seed's single-β\_s claim is refuted**

The ZS-S21 seed asserted that the Wilson action carries one β\_s and one β\_t by construction, and that orbit-dependent couplings are a generalisation of the Wilson action rather than the Wilson action. For a hypercubic lattice this is correct. For a complex whose 2-cells are not congruent it is false, and the standard literature says so. The random-lattice gauge action of Christ, Friedberg and Lee \[5, 6\] weights each plaquette by the ratio of its dual measure to its own measure,  
S\_g \= (β/6) Σ\_Λ (Ã\_Λ / 2A\_Λ) \[1 − (1/3) Re Tr U\_Λ\] ,   (6.1)  
so that gauge fields are loosely constrained on large cells and tightly constrained on small ones. On an irregular lattice this is the Wilson action, not a generalisation of it. The reason a single β suffices on ℤ⁴ is not that the prescription forbids weights but that all plaquettes there are congruent, so all weights coincide. On K\_TI the 12 pentagons and 20 hexagons are not congruent: A₆/A₅ \= 1.5100902868 exactly (check T055). A single β\_s is therefore a prescription. \[STATUS: the seed claim is RETRACTED — Retraction S21-R1\]

## **6.2 Reported against interest (ii) — the ψ(n\_f) obstruction, and Retraction S21-R2**

Version 1.0 of this paper stated a single axiom, that K\_TI enters metric-free, and inferred ρ \= 1 from it on the ground that without a metric the weight cannot depend on area. The first half of that reasoning is sound; the inference is not, and it is retracted here.

**Retraction S21-R2.** The inference “no metric ⟹ β₅ \= β₆” is INVALID. Incidence data alone determine the degree of every face, n\_f \= 5 for pentagons and 6 for hexagons, so the assignment  
β\_f \= β\_s · ψ(n\_f) ,   ρ \= ψ(5)/ψ(6)  
is completely metric-free and realises every positive ρ. A single SU(3) gauge coupling does not help: one coupling β\_s and a dimensionless cellular quadrature weight w\_f coexist without contradiction in S\_s \= β\_s Σ\_f w\_f \[1 − (1/3)Re Tr U\_f\]. This is not a new objection. It is precisely the obstruction that ZS-S19 v1.3 discovered when it withdrew its claim to have derived the counting measure from the metric-free regulator axiom (R) alone, and registered the need for the strictly stronger counting-trace axiom R\_C. The obstruction has recurred one level up, at the group-valued action instead of the quadratic one. Version 1.0's Corollary S21.2, and the sentence in its §15.3 asserting that no continuous freedom survives under a single ontological axiom, are RETRACTED.

The companion makes the obstruction executable rather than rhetorical: five metric-free ψ prescriptions are evaluated and return five distinct values of ρ and five distinct λ₁, spanning −4.2 % to \+0.3 % (checks T086, T087). Version 1.0's own §15.3 in fact conceded the point in passing — that nothing internal to a metric-free complex distinguishes the counting weight from another function of the combinatorial cell type — while its §6.3 asserted the opposite. That internal inconsistency is what v1.1 removes.

## **6.3 What the transfer matrix does and does not decide**

It is worth stating the division of labour exactly, because it is the substance of the paper.

Table 6.1. What the transfer-matrix construction settles, and what it propagates.

| Question | Settled by the construction? | Result |
| ----- | ----- | ----- |
| Is M off-diagonal? | YES — settled | No. Diagonal for every weight assignment (Thm S21.1, checks T060–T064). F-S20.5 has no content. |
| Is M₁ orbit-dependent? | NO — propagated | The transfer matrix returns M₁ \= diag(β\_e a\_t) and reproduces orbit-dependent temporal weights faithfully (check T065). Primal congruence is unconditional (Lemma S21.2); weight uniformity is not. |
| Is M₂ orbit-dependent? | NO — propagated | The transfer matrix returns M₂ \= diag(β\_f/a\_t) and reproduces orbit-dependent spatial weights faithfully (check T064). It neither creates nor removes face-orbit dependence. |
| What is the overall scale r? | NO — dimensional transmutation | r \= β\_s/(β\_t a\_t²), calibrated from one measurement (§15.2). |

**So the honest statement is a negative result about the construction, and we state it as one:** the transfer matrix is agnostic about both σ and ρ. It proves diagonality and it propagates weights; it selects nothing. Gate F-S21.12 is registered against any later claim to the contrary. What the construction does contribute is the elimination of everything else — the non-diagonal family, the primal-geometry family, and the whole apparatus of conditions ZS-S20 searched — reducing a problem bounded at order 6 × 10³ undetermined directions, and at 181 in the diagonal family, to exactly two numbers.

Combining Theorem S21.1 with the (H-TR) unit fixing of §3.3, write M₁ \= m·M̂₁(σ) with M̂₁(σ) \= diag(σ on the 60 edges of type (5,6), 1 on the 30 of type (6,6)), and M₂ \= β·M̂₂(ρ) with M̂₂(ρ) \= diag(ρ on the 12 pentagons, 1 on the 20 hexagons). Then  
Δ₂(σ, ρ, r) \= r · M̂₂(ρ)^{1/2} B₂ M̂₁(σ)⁻¹ B₂ᵀ M̂₂(ρ)^{1/2} ,    r \= β/m \= β\_s/(β\_t a\_t²) ,   (6.2)  
with the dimensionless shape carried entirely by the pair (σ, ρ) and the single dimensionful scale carried entirely by r, in which a\_t appears exactly once. The convention (H-TR), Tr Δ₂ \= 2E \= 180, fixes r for each (σ, ρ); at σ \= ρ \= 1 it returns r \= 1, the a\_TI \= 1 convention (checks T090, T091).

## **6.4 The two axioms**

Two families survive §6.3 in each anisotropy class, and they are disjoint. The dual-measure family — β\_f ∝ 1/A\_f on faces, β\_e ∝ |⋆e|/|e| on edges — requires a metric. The ambient-combinatorial family — β\_f \= β\_s ψ(n\_f) on faces, β\_e \= β\_t ψ\_e({deg f : f ⊃ e}) on edges — requires none. Each needs its own axiom to remove, and each axiom must apply to both classes.

**Axiom Z-A0 (Metric-Free Carrier).** In the cellular reduction of ZS-S14, K\_TI enters as a metric-free I\_h-equivariant cell complex. Its only structure is the incidence data (B₁, B₂) and the I\_h action. No area, length, dual volume, dual edge or embedding is available to the reduction. **\[Kills the dual-measure family in both classes.\]**

**Axiom Z-A1 (Orbit-Blind Plaquette Reduction Postulate, expanded in v1.2).** Within each anisotropy class the character-kernel coefficient that the ZS-S14 reduction attaches to a 2-cell is independent of every ambient combinatorial orbit and of every dual-cell datum. Explicitly β\_e \= β\_t for all 90 edges and β\_f \= β\_s for all 32 faces, so that it depends on neither the edge-star type (5,6)/(6,6), nor the face degree 5/6, nor the face or edge orbit, nor any functions ψ\_e, ψ\_f of those data. Equivalently S \= β\_s Σ\_{f∈F} \[1 − (1/3) Re Tr U\_f\] \+ β\_t Σ\_{e∈E} \[1 − (1/3) Re Tr(V\_e(t+a\_t)V\_e(t)†)\]. **\[Kills the ambient-combinatorial family in both classes.\]**

**Corollary S21.2b (Face-Orbit Uniformity).** Under (H-W) ∧ (Z-A0) ∧ (Z-A1), β₅ \= β₆ \= β\_s, hence M₂ \= β·I₃₂ and ρ \= 1\. Together with Corollary S21.2a this gives M₁ \= m·I₉₀, M₂ \= β·I₃₂, σ \= ρ \= 1 and Δ₂ \= r·B₂B₂ᵀ with r \= β\_s/(β\_t a\_t²). **\[STATUS: DERIVED-CONDITIONAL on (H-W) ∧ (Z-A0) ∧ (Z-A1)\]**

Three remarks, in the order a sceptical reader will want them.

**(i) Does (Z-A1) pass the ZS-S20 Theorem S20.E test?** Yes. Its solution set is not {M uniform}: (Z-A1) is a statement about which functional form the reduction takes, and its negation is informative rather than vacuous — negating (Z-A0) yields the definite alternative ρ \= 1.5100902868, and negating (Z-A1) yields the definite one-parameter ψ-family. A hypothesis whose negation produces a computable rival theory is not a restatement of its own conclusion. Theorem S20.T1 does not apply, because that theorem concerns conditions imposed on a given quadratic form, whereas here the quadratic form is the output.

**(ii) Is (Z-A1) anything more than ZS-S19's R\_C?** Not in content. It is R\_C, moved from the quadratic action to the group-valued one. What has changed is its position: in ZS-S19 the counting measure was one live prescription among many, competing with degree bias, equal-cell refinement, heat-kernel area weighting and the circumcentric DEC star, and ZS-S19 could not order them. After Theorem S21.1 the DEC/Whitney branch is gone (M is diagonal by construction, and the mass-lumped star is not what the transfer matrix returns), after Theorem S21.2 the electric ambiguity is gone, and after (Z-A0) the area branch is gone. (Z-A1) is what is left. We claim a reduction of the search space, not a derivation of the axiom, and we mark the difference.

**(iii) What does the axiom cost?** A reader who rejects (Z-A0) obtains a different but equally parameter-free theory, falsifiable now by §6.5. A reader who rejects (Z-A1) obtains a two-parameter family (σ, ρ), which no single measurement can falsify. That asymmetry is the honest terminus of the S-line, and §15.4 states it in one sentence.

## **6.5 The branches are separated observably, and non-uniformly**

Version 1.0 wrote that the branches differ by 0.91 % in every energy. That is wrong and was corrected in v1.1. The lowest gap does move by −0.9125 % in ω, but the shift is strongly mode-dependent, because ρ ≠ 1 splits the accidental A\_g ⊕ G\_g degeneracy at λ \= 8 and reorders the spectrum. Version 1.2 adds the third branch, in which σ is also metric-induced, and the companion computes all three with full I\_h isotype resolution (checks T088, T089, T092–T096).

Table 6.2. Isotype-resolved spectra of the three surviving branches, in the (H-TR) convention. Each is parameter-free once the branch is chosen. The counting branch has eight nonzero levels; both metric branches have nine, because the accidental degeneracy at λ \= 8 splits. The full metric branch uses σ \= 0.8973272361 and ρ \= 1.5100902868.

| k | counting (σ \= ρ \= 1\) | mult | iso | spatial-only CFL (σ \= 1\) | mult | iso | full metric | mult | iso |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | 1.2428416164 | 3 | T₁u | 1.2202641716 | 3 | T₁u | 1.2069213135 | 3 | T₁u |
| 2 | 3.2679491924 | 5 | H\_g | 3.2426532809 | 5 | H\_g | 3.2021584823 | 5 | H\_g |
| 3 | 4.8443660283 | 3 | T₂u | 5.1280732201 | 4 | G\_u | 5.0114038007 | 4 | G\_u |
| 4 | 6.0000000000 | 4 | G\_u | 5.9288147079 | 3 | T₂u | 5.9240580690 | 3 | T₂u |
| 5 | 6.7320508076 | 5 | H\_g | 6.8374309601 | 4 | G\_g | 6.5914753301 | 4 | G\_g |
| 6 | 7.5210904061 | 3 | T₁u | 7.4839523690 | 5 | H\_g | 7.5015797384 | 3 | T₂u |
| 7 | 8.0000000000 | 5 | A\_g ⊕ G\_g | 7.5635898643 | 3 | T₂u | 7.6668698858 | 5 | H\_g |
| 8 | 8.3917019492 | 3 | T₂u | 8.4499002960 | 3 | T₁u | 8.6855691448 | 3 | T₁u |
| 9 | — | — | — | 9.0172479099 | 1 | A\_g | 9.2889568387 | 1 | A\_g |

Table 6.3. Isotype-matched branch shifts in the physical energy ω \= √(rλ). The shift is not uniform and its sign is not constant.

| Lowest level of isotype | counting λ | CFL λ | Δλ | Δω |
| ----- | ----- | ----- | ----- | ----- |
| T₁u | 1.24284162 | 1.22026417 | −1.8166 % | −0.9125 % |
| H\_g | 3.26794919 | 3.24265328 | −0.7741 % | −0.3878 % |
| T₂u | 4.84436603 | 5.92881471 | \+22.3858 % | \+10.6281 % |
| G\_u | 6.00000000 | 5.12807322 | −14.5321 % | −7.5512 % |
| G\_g | 8.00000000 | 6.83743096 | −14.5321 % | −7.5512 % |
| A\_g | 8.00000000 | 9.01724791 | \+12.7156 % | \+6.1676 % |

**The sharpest discriminator is qualitative and needs no precision.** In the counting branch the third-lowest excitation has multiplicity 3 and isotype T₂u; in BOTH metric branches it has multiplicity 4 and isotype G\_u (checks T089, T095). A determination of the degeneracy of the third excited state, without any absolute scale and without percent-level accuracy, decides between orbit-blind and orbit-sensitive weighting — not merely between one metric and another.

Two scale-free numerical discriminators follow, and it matters which is used:  
D₁ \= ω(T₂u,1)/ω(T₁u,1) :   counting 1.9742883436   vs   spatial CFL 2.2042305068 (+11.65 %)   vs   full metric 2.2154919435 (+12.21 %)  
D₂ \= ω(H\_g,1)/ω(T₁u,1) :   counting 1.6215477963   vs   CFL 1.6301340807   —   separation only \+0.53 %  
Gate F-S21.8 is therefore defined on D₁ with the decision threshold at the branch midpoint 2.0892594252, and NOT on D₂, which version 1.0 mistakenly used and which separates the branches by less than the systematic uncertainty of any realistic determination. Because both metric branches lie on the same side of the threshold, the gate is branch-robust: it tests the postulate, not a particular metric. \[STATUS: TESTABLE — checks T092, T093, T095, T096\]

One further disclosure. ZS-S20 Table 19.2 quotes λ₁ \= 1.2492508718, a shift of \+0.5157 %, for the heat-kernel branch, without stating its normalisation convention. In the (H-TR) convention adopted here — the convention that returns the LOCKED λ₁ exactly at ρ \= 1 — the heat-kernel branch gives 1.2202641716, a shift of −1.8166 %. We do not adopt either number silently. The discrepancy is registered as erratum-candidate E-5 in §11 and does not enter the closure argument, which requires only that the branches be separated and that the separation be measurable.

# **§7. SU(2), SU(3), and Reflection Positivity**

## **7.1 SU(2) by character expansion**

The heat-kernel semigroup K\_{t₁} ∗ K\_{t₂} \= K\_{t₁+t₂} is exact and non-perturbative, and is VERIFIED in the ZS-S20 companion to 4.3 × 10⁻¹⁴ for U(1) and 2.8 × 10⁻¹⁷ for SU(2). The temporal kernel of §4.1 is replaced by Σ\_j d\_j χ\_j(V′V†) c\_j(β\_t) with c\_j \> 0, and the electric operator becomes the Casimir. Nothing in the incidence structure changes. \[STATUS: IMPORTED-PROVEN \+ VERIFIED\]

## **7.2 SU(3)**

The step from SU(2) to SU(3) is representation-theoretic. The plaquette census, the temporal-plaquette bijection, the diagonality of the Hessians and the congruence argument of §5 are all statements about the complex and are unaffected by the gauge group. The Kogut–Susskind Hamiltonian is that of \[1\] with the colour Casimir on edges and the SU(3) magnetic term on faces; the construction is Creutz's \[4\] performed on K\_TI instead of ℤ³. We do not re-prove it. \[STATUS: IMPORTED-PROVEN, applied\]

## **7.3 Reflection positivity — the seed's Outcome D cannot fire**

The seed pre-registered an outcome in which reflection positivity fails on the non-bipartite complex K\_TI. That outcome cannot fire, and we remove it. Osterwalder–Seiler reflection positivity for a Wilson-type action is a statement about reflection in a time-slice: T \= A K A with A positive and diagonal in the link representation and K the temporal kernel, whose positivity is equivalent to the positivity of its character coefficients. For U(1) these are I\_n(β\_t) \> 0 for all n; for the heat-kernel action they are exp(−t C₂(j)) \> 0 for every irreducible representation. The companion checks both (T104, T105). No property of the spatial complex — bipartiteness, vertex-transitivity, orbit structure — enters anywhere in the argument. \[STATUS: DERIVED; gate F-S21.4 removed\]

A genuine strengthening follows. The construction of T is non-perturbative. Every O(g²) statement of ZS-S17 to ZS-S20 remains DERIVED-PERT-COND at λ\_t ≈ 5.54, but Theorems S21.1 and S21.2 do not inherit that limitation.

# **§8. Gauss Law and the Census 59 \+ 31**

The Gauss law of the constructed theory is (B₁E)\_v \= 0 with unit coefficients. Its rank is 59, so the physical edge count is 90 − 59 \= 31 \= rank B₂ᵀ, and there are no harmonic edge modes since H¹(K\_TI) \= 0 (checks T100–T102). The magnetic term is gauge invariant because B₁B₂ᵀ \= 0 to machine zero (check T103). The census that ZS-S18 predicted would survive in every outcome does survive, and it survives here as an output of the construction rather than as an input to it. \[STATUS: PROVEN\]

# **§9. The Dimensionless Spectrum — and What the Observable Actually Is**

## **9.1 The exact spectral algebra, carried forward**

Corollary S20.Q is reproduced symbolically in the companion from the independently rebuilt complex (check T030):  
χ\_{B₂B₂ᵀ}(λ) \= λ · (λ−6)⁴ · (λ−8)⁵ · (λ²−10λ+22)⁵ · (λ⁴ − 22λ³ \+ 166λ² − 480λ \+ 380)³  
The quartic p(λ) is irreducible over ℚ (check T031); λ₁ \= 1.2428416164 and λ\_h \= 7.5210904061 are both roots of it (checks T032, T033), so both are algebraic integers of degree 4; the four roots sum to 22 by Vieta (check T034); and λ² − 10λ \+ 22 has roots 5 ± √3 with multiplicity 5 (check T035). Tr B₂B₂ᵀ \= 180 \= 2E (check T036). \[STATUS: PROVEN\]

## **9.2 The observable is ω \= √(rλ), not λ**

The Hamiltonian (4.2) is a system of coupled harmonic oscillators with mass matrix M₁ and stiffness B₂ᵀM₂B₂. Its normal-mode frequencies are the square roots of the eigenvalues of M₁⁻¹B₂ᵀM₂B₂, so  
ω\_k \= √( r λ\_k ) ,    ω\_k/ω₁ \= √( λ\_k/λ₁ ) .   (9.1)  
The falsifiable table is therefore the table of square roots. This is not a convention: it is verified end-to-end in §10.2 by exact diagonalisation. Any prior statement of the ratio table as λ\_k/λ₁ describes eigenvalues of Δ₂, not excitation energies. \[STATUS: DERIVED — check T162\]

Table 9.1. The complete dimensionless spectrum of the constructed theory in the counting branch, i.e. under (H-W) ∧ (Z-A0) ∧ (Z-A1). No continuous dimensionless freedom. The third column is the eigenvalue ratio; the fourth is the physical energy ratio and is the falsifiable prediction. The isotype column corrects erratum E-1.

| λ\_k | mult | I\_h isotype | λ\_k/λ₁ | ω\_k/ω₁ \= √(λ\_k/λ₁) |
| ----- | ----- | ----- | ----- | ----- |
| 1.2428416164 | 3 | T\_1u | 1.0000000000 | 1.0000000000 |
| 3.2679491924 | 5 | H\_g | 2.6294172558 | 1.6215477963 |
| 4.8443660283 | 3 | T\_2u | 3.8978144635 | 1.9742883436 |
| 6.0000000000 | 4 | G\_u | 4.8276465165 | 2.1971905963 |
| 6.7320508076 | 5 | H\_g | 5.4166602716 | 2.3273719668 |
| 7.5210904061 | 3 | T\_1u | 6.0515276498 | 2.4599852946 |
| 8.0000000000 | 5 | A\_g ⊕ G\_g | 6.4368620220 | 2.5370971645 |
| 8.3917019492 | 3 | T\_2u | 6.7520284470 | 2.5984665568 |

The multiplicities sum to 31, the physical transverse count, and with the harmonic mode they sum to 32 (checks T160, T038). The table is invariant under the scale r (check T163). \[STATUS: TESTABLE\]

# **§10. Verification**

## **10.1 What counts as evidence**

Every claim about M is an executable check on the actual 90- and 32-dimensional objects. The companion carries three check kinds: check (an assertion on a computed number from the Z-Spin object), proxy (a generic theorem verified on a surrogate, never counted as a verification of the Z-Spin object), and decl (a registry statement with no numerical content). Following the ZS-S20 v2.2 retraction, the suite performs a static analysis of its own source with Python's ast module and asserts that no check-kind assertion is a literal constant (check T190). The suite emits its own SHA256.

## **10.2 The end-to-end diagonalisation**

Theorems S21.1 and S21.2 are structural, and structural claims verified only on the object they describe risk circularity. We therefore diagonalise the compact U(1) transfer-matrix Hamiltonian exactly on a model complex chosen to carry the same pathology as K\_TI — two face orbits and two edge orbits — namely the triangular prism, with V \= 6, E \= 9, F \= 5 (two triangles and three squares), six edges of type (3,4) and three of type (4,4) (check T120). The Hamiltonian is built in the gauge-invariant flux basis with the exact U(1) kinetic kernel −log\[I\_n(β\_t)/I\_0(β\_t)\], no harmonic approximation, and diagonalised by Lanczos.

Table 10.1. Exact diagonalisation of the compact U(1) Kogut–Susskind Hamiltonian on the two-orbit model complex, against ω\_k \= √(λ\_k β\_s/β\_t) of the uniform measure. β\_s \= 1\.

| β\_t | charge cutoff | Hilbert dim | E\_k/ω\_k (uniform) | E₂/E₁ |
| ----- | ----- | ----- | ----- | ----- |
| 25 | 5 | 14 641 | 0.97905, 0.96619, 0.96971, 0.98766 | 1.27404 |
| 50 | 6 | 28 561 | 0.99037, 0.97790, 0.98079, 1.00584 | 1.27474 |
| 100 | 7 | 50 625 | 1.00445, 0.98942, 0.99210, 1.03267 | 1.27167 |

The agreement with the uniform measure is better than 4 % throughout, the residual being the O(1/β) anharmonic correction of the compact theory (checks T130–T132), and the predicted E₂/E₁ is 1.29099 for the uniform measure against 1.11803 for ψ \= 1/n\_f and 1.37437 for ψ \= n\_f, with an observed mean of 1.27348 (checks T140, T141).

**What this proxy shows, and what it does not.** It shows that the transfer-matrix construction propagates the weight it is given and manufactures no face-size dependence of its own, and that excitation ratios are in principle sharp enough to discriminate weight prescriptions in a controlled finite model. It does NOT select (Z-A1) for K\_TI, and it does not extend to SU(3): the model is a weak-coupling compact U(1) theory on a nine-edge complex, it is not the Z-Spin object, and only two rival prescriptions were compared. It is registered as PROXY P150 and is not counted as a verification of K\_TI.

## **10.3 Summary**

88/88 executable checks PASS, 1 proxy, 24 declarative statements, 0 FAIL, and the suite exits non-zero on any failure. No ledger number moves. A \= 35/437, Q \= 11, dim Z \= 2, λ₁ \= 1.2428416164 and λ\_h \= 7.5210904061 are all LOCKED and none is re-fitted. The seven checks added in v1.1 were T064, T086, T087, T088, T089, T092, T093. The eight added in v1.2 are T065 (temporal propagation of orbit dependence), T075 and T076 (the ambient-star obstruction and the independent reproduction of the ZS-S20 flat-cone ratio), T077 (the σ-family is live), T094 to T096 (the full metric branch and the robustness of the discriminator), and T106 (the SU(3) Casimir, replacing a description that previously overstated a SU(2)-only computation).

# **§11. Errata in the Standing Corpus**

Nine errors are reported, with their computational evidence. Five are in the standing corpus and were found while executing §§3–9. Four are errors of earlier versions of this paper — three of v1.0 and one of v1.1 — found in external review and corrected here. The corpus does not distinguish between the two kinds in how it records them, and it should not: an error is more instructive when it is one of your own.

Table 11.1. Errata reported by ZS-S21. E-1 to E-5 are in the standing corpus and were reported in v1.0; E-6 to E-8 are v1.1 corrections to v1.0; E-9 is a v1.2 correction to v1.1.

| ID | Location | Erroneous statement | Correction | Check |
| ----- | ----- | ----- | ----- | ----- |
| E-1a | ZS-S7 §2.2; Math-Spine Table 2.1 | The 32-dimensional face representation decomposes into all ten irreducible representations of I\_h, each appearing exactly once, so the face lattice sees every symmetry sector. | Ω²(K\_TI) \= 2A\_g ⊕ 2T\_1u ⊕ 2T\_2u ⊕ 2H\_g ⊕ G\_g ⊕ G\_u. Exactly six irreps occur; A\_u, T\_1g, T\_2g and H\_u do not occur at all. The multiplicities are 2,2,2,2,1,1 and not 1 × ten. | T041, T042 |
| E-1b | ZS-S7 §2.2 spectrum table | λ \= 8.000, multiplicity 5, is the H irrep. | λ \= 8 is A\_g ⊕ G\_g, an accidental degeneracy of two inequivalent irreps. The second A\_g eigenvector is 20·1\_pent − 12·1\_hex with exact residual 0.0. It splits for every ρ ≠ 1\. | T043, T046, T082 |
| E-1c | ZS-S7 §2.2 spectrum table | λ \= 6.000, multiplicity 4, labelled G. | The isotype is G\_u specifically; the G\_g copy sits at λ \= 8\. | T044 |
| E-2 | ZS-S21 seed §1.3 | The dimensionless ratio table (seven entries, multiplicities summing to 28). | One level is missing: λ \= 8.3917019492, multiplicity 3, ratio 6.7520284470 (T\_2u). With it the multiplicities sum to 31, and with the harmonic mode to 32\. | T160, T161 |
| E-3 | ZS-S21 seed, item 3 | The Wilson action carries one β\_s by construction; orbit-dependent couplings are a generalisation of the Wilson action, not the Wilson action. | False for complexes whose 2-cells are not congruent. The standard random-lattice action \[5,6\] weights each plaquette by the ratio of dual to own measure. On K\_TI, A₆/A₅ \= 1.5100902868. Uniform β\_s is a prescription, and §6.3 states the axiom that licenses it. | T055 |
| E-4 | ZS-S21 seed §1.3; ZS-S20 §1.3 | The ratio table λ\_k/λ₁ is the physical prediction. | The eigenvalue ratios are correct as eigenvalue ratios, but the excitation energies of the constructed Hamiltonian are ω\_k \= √(rλ\_k). The falsifiable table is the fourth column of Table 9.1. | T162, T130–T132 |
| E-9 | ZS-S21 v1.1 §5, title and status tag | Theorem S21.2: σ \= 1 holds unconditionally, for every intrinsic weight prescription — metric-induced, area-based, dual-measure-based or counting alike — and requires no axiom. | Too strong on both counts. The primal congruence is unconditional (Lemma S21.2), but the (5,6) and (6,6) orbits have different ambient stars, so ψ\_e({deg f : f ⊃ e}) and every dual measure separate them; the computed dual ratios are 0.8973272361 and 0.9105929973. σ \= 1 is DERIVED-CONDITIONAL on the expanded (Z-A1). Retraction S21-R3. | T065, T075, T076, T077, D078 |
| E-6 | ZS-S21 v1.0 §6.3, §15.3 | A metric-free carrier alone forces β₅ \= β₆, so one ontological axiom closes the bridge and no continuous freedom survives. | INVALID. β\_f \= β\_s ψ(n\_f) is metric-free and realises every ρ \> 0 — the ZS-S19 v1.3 obstruction recurring. Two axioms are required: (Z-A0) metric-free and (Z-A1) orbit-blind. Retraction S21-R2. | T086, T087, D087 |
| E-7 | ZS-S21 v1.0 §6.3 | The CFL and counting branches differ by 0.91 % in every energy. | Only the lowest gap differs by 0.9125 %. The shift is mode-dependent and changes sign: the lowest T₂u moves by \+10.6281 %, the lowest G\_u by −7.5512 %, and the accidental A\_g ⊕ G\_g degeneracy splits, giving nine levels instead of eight. | T088, T089 |
| E-8 | ZS-S21 v1.0 §14 / companion G212 | Gate F-S21.8 defined on the lowest T₁u : H\_g ratio, with mutually inconsistent tolerances quoted in the body (0.91 %) and in the code (0.26 %). | That ratio separates the branches by only 0.53 % and is useless as a gate. F-S21.8 is redefined on D₁ \= ω(T₂u,1)/ω(T₁u,1), which separates by 11.65 %, with the threshold at the midpoint 2.0892594252; and on the degeneracy of the third excitation, 3 versus 4\. | T089, T092, T093 |
| E-5 | ZS-S20 Table 19.2 | Heat-kernel branch: λ₁ \= 1.2492508718, a shift of \+0.5157 %. | Not reproducible without a stated normalisation. In the (H-TR) convention Tr Δ₂ \= 2E, which returns the LOCKED λ₁ exactly at ρ \= 1, the heat-kernel branch gives 1.2202641716, a shift of −1.8166 %. Registered as ERRATUM-CANDIDATE pending disclosure of the ZS-S20 convention. | T083–T085, D086 |

Additionally, ZS-S20 §17.1a's inference that the anchoring and geometric routes are inequivalent so that one must be wrong about the Z-sector is superseded rather than corrected: Theorem S21.2 shows that the transfer matrix returns a third value, σ \= 1, and that neither of the two compared values is the reduction's output.

# **§12. Non-Circularity: the Three ZS-S20 Tests Applied Before Writing**

Table 12.1. The self-tests ZS-S20 built against itself, applied to Theorem S21.1, Theorem S21.2 and Corollary S21.2.

| Test | Thm S21.1 (H-W) | Lemma S21.2 (H-W) | Cor S21.2a, S21.2b (Z-A0 ∧ Z-A1) |
| ----- | ----- | ----- | ----- |
| S20.E — is the hypothesis equivalent to its conclusion? | No. The hypothesis is a statement about the functional form of a group-valued action; M is computed from it. | No hypothesis at all beyond the incidence structure and Archimedean congruence, both PROVEN. | No. Z-A's negation yields a definite alternative, ρ \= 1.5100902868, not vacuity. |
| S20.T1 — is it linear in the action, returning its input? | Does not apply. The quadratic form is the output; the input is not quadratic. | Does not apply. | Does not apply. |
| v1.7 — is r carried explicitly and never set to 1 silently? | Yes, r \= β\_s/(β\_t a\_t²) appears in (4.3). | Yes; §5 concerns M₁ only and carries no scale. | Yes; (6.2) separates the shape (σ, ρ) from the scale r, with a\_t appearing exactly once, and §3.3 fixes r by a stated convention rather than by fiat. |

And the structural difference from every failed ZS-S20 route: those routes took the quadratic action as given and searched for a condition selecting M. This route never has a free M to select in the sense they meant, because the off-diagonal question is empty. It does still have two numbers to postulate, and §6.4 postulates them in the open. That is precisely the non-quadratic step gate F-S20.14 demanded, and it is also the limit of what that step can deliver.

# **§13. Anti-Numerology**

The closure argument contains no numerical coincidence. Every step in §§3–6 is an incidence count, a congruence, or a Hessian evaluated on the actual complex (check T172). Nothing is asserted on the strength of a numerical proximity.

The one standing coincidence in the neighbourhood, 22 \= 2Q for the Vieta sum of the quartic roots, is NOT upgraded. A uniform null over admissible integer root-sums returns p \= 0.0229 with 200 000 draws, seed 20260320 (check T170), which is far above any evidential threshold this corpus uses. No connecting theorem is constructed here and the quantity plays no role whatever in the closure argument. \[STATUS: OBSERVATION\]

The accidental degeneracy A\_g ⊕ G\_g at λ \= 8, and the exact values 6 \= dim Y and 8 \= dim Z \+ dim Y that the corpus records at σ \= ρ \= 1, are likewise NOT used as evidence for the orbit-blind postulate. They are consequences of it, not arguments for it, and treating them as arguments would be exactly the failure mode ZS-S20 was corrected for. The same denial applies, and is repeated here because it is tempting, to the fact that σ \= ρ \= 1 returns the LOCKED λ₁ \= 1.2428416164: that is a consistency check between two independent computations, and it is not evidence that (Z-A1) is true, because λ₁ was itself computed in ZS-S7 under the counting prescription. \[STATUS: OBSERVATION; explicitly denied evidential force\]

# **§14. Gate Registry and Retraction Register**

Table 14.1. Falsification gate registry after ZS-S21 v1.1. Layers: M \= mathematical/theoretical collapse (immediate rejection); S \= simulation/consistency collapse (revision required); O \= observational collapse (external data).

| Gate | Condition that fires it | Layer | Status |
| ----- | ----- | ----- | ----- |
| F-S20.5 | An independent cellular reduction returns a non-diagonal M₁ or M₂. | M | SUPERSEDED-BY-CONSTRUCTION (T060–T064); diagonality holds for every weight |
| F-S20.14 | No non-quadratic or coarse-graining step exists. | M | CLOSED by Theorem S21.1 |
| F-S20.15a–d | register-lift and normalisation gates | S | SUPERSEDED-BY-CONSTRUCTION — M is no longer selected |
| F-S18.16b / F-S19.6b | action-level determination of M | M | REDUCED by construction from a continuum of directions to the two ratios σ and ρ, fixed only by (Z-A0) ∧ (Z-A1) |
| F-S19.3 | a\_TI and the g\_S14 ↔ g\_MS-bar scheme relation | O | REFRAMED as scale setting; see §15.2 |
| F-S21.1 | The temporal-plaquette ↔ edge bijection fails. | M | Does not fire (T051) |
| F-S21.2 | The U(1) transfer matrix produces an off-diagonal M. | M | Does not fire (T061, T064, T065) |
| F-S21.3 | The SU(3) character expansion introduces face-orbit dependence at O(g⁰). | M | Does not fire under (Z-A1); the construction is agnostic and propagates whatever weight it is given |
| F-S21.12 (NEW in v1.2) | The transfer matrix is shown to SELECT rather than merely propagate an orbit weight, in either anisotropy class. | M | Does not fire; it propagates (T064, T065). Registered so that no later paper can attribute a selection to the construction. |
| F-S21.4 | Lüscher positivity fails on K\_TI. | M | CANNOT FIRE — removed; see §7.3 |
| F-S21.5 | The Gauss census is not 59 \+ 31 in the constructed theory. | S | Does not fire (T100–T102) |
| F-S21.6 | Any dimensionless ratio in Table 9.1 moves. | M | Does not fire (T030–T038, T160–T163) |
| F-S21.7 | Axiom (Z-A0) is contradicted: ZS-S14 is shown to supply K\_TI with a metric, an area or a dual measure. | M | OPEN |
| F-S21.8 (REDEFINED v1.1, BRANCH-ROBUST v1.2) | The third-lowest excitation is found to have multiplicity 4 with isotype G\_u rather than multiplicity 3 with isotype T₂u; or the scale-free ratio D₁ \= ω(T₂u,1)/ω(T₁u,1) is found above the branch midpoint 2.0892594252. | O | OPEN — both metric branches lie on the same side of the threshold (T095, T096), so the gate tests orbit-blind against orbit-sensitive weighting, not one metric against another |
| F-S21.9 | Erratum E-1a is shown to be wrong, i.e. Ω²(K\_TI) does contain A\_u, T₁g, T₂g or H\_u. | M | Does not fire (T041, T042) |
| F-S21.10 (NEW in v1.1) | Axiom (Z-A1) is contradicted: the ZS-S14 reduction is shown to weight 2-cells by a combinatorial function ψ(n\_f). | M | OPEN — this is ZS-S19's R\_C axiom restated at the group-valued level, and it is the single load-bearing choice of the S-line |
| F-S21.11 (NEW in v1.1) | (H-W) is contradicted: the ZS-S14 cellular reduction is shown not to be of Wilson type — non-compact link variables, more than one holonomy per 2-cell, or coupling beyond nearest neighbour in time. | M | OPEN — Theorems S21.1 and S21.2 both rest on (H-W) |

Retraction register. ZS-S21 inherits the ten ZS-S20 retractions (v1.0 R\_C-equivalence-as-demotion; v1.2 scalar heat kernel read as a Yang–Mills one-loop result; v1.3 unit systems presented as physical exclusion; v1.4 the F-S20.11 scale error; v1.5 an over-strong meta-theorem; v1.6 a retracted metric smuggled back; v1.7 a headline not following from its own conditions; v1.8/v1.9 an off-diagonal conductance read as β₅/β₆; v2.1 a 729-point grid called exhaustive; v2.2 a literal True passing as an executable check) and adds three of its own.

**Retraction S21-R1 (v1.0).** The ZS-S21 seed's central structural claim — that the Wilson action carries one β\_s by construction, with no selection principle invoked — is RETRACTED before use. It is true on congruent-cell lattices and false on K\_TI. The paper that would have been written from the seed as given would have committed a new instance of the ZS-S20 failure mode: a proxy, the hypercubic Wilson action, verified and reported as the target, the Wilson action on an Archimedean complex.

**Retraction S21-R2 (v1.1, against v1.0 of this paper).** Version 1.0's Corollary S21.2, which inferred ρ \= 1 from the metric-free axiom together with the single-coupling statement, is RETRACTED. The inference is invalid because β\_f \= β\_s ψ(n\_f) is metric-free. With it are retracted v1.0's headline that one ontological axiom closes the bridge; v1.0 §6.3's assertion that the branches differ by 0.91 % in every energy; and v1.0's definition of gate F-S21.8. The shape of this error is worth naming, because it is the eleventh instance of the same shape: a necessary condition (no metric) verified and reported as a sufficient one (uniform weight). The corpus has now made this error in ZS-S19 v1.3, in six of ZS-S20's ten cycles, and once here.

# **§15. Conclusion — Is the Sub-Bridge Closed?**

## **15.1 What was shown**

The measure was never a free datum in the sense ZS-S20 assumed. In lattice gauge theory the quadratic Hamiltonian is constructed from a group-valued action by the transfer matrix, and ZS-S21 performs that construction on K\_TI × a\_tℤ. Three things follow that ZS-S20 could not obtain. First, M is diagonal, necessarily and for every weight assignment, so the non-diagonal family is not a gap but an empty set and F-S20.5 has no content. Second, the 90 temporal plaquettes are congruent as primal cells and all quadrilaterals, so no primal-geometry weight can act on the electric orbits; that is unconditional. Third, the residual is not a continuum of undetermined directions across 90 and 32 dimensions, nor the 181 of the diagonal family, but the two dimensionless ratios σ and ρ, on which exactly two candidate families survive — the dual-measure family and the ambient-combinatorial family.

## **15.2 What is predicted and what is calibrated**

Given the branch, every dimensionless quantity of the cellular theory is fixed with no continuous freedom: the isotype-resolved spectrum of Table 9.1 and every ratio built from it. One dimensionful number, r \= β\_s/(β\_t a\_t²), sets the overall scale and is fixed by one measurement. This is scale calibration in a dimensionally transmuted Yang–Mills theory, and the distinction is worth keeping: dimensional transmutation is the renormalisation-group phenomenon by which a dimensionful Λ arises from a dimensionless coupling, whereas fixing r from one observable is the lattice scale-setting step that follows it. Neither is an unfilled gap; every lattice QCD calculation ever published performs the second. Accordingly Λ\_QCD \= 264.1 MeV is relabelled from prediction to calibration. Its epistemic status is demoted; its value does not move. \[STATUS: DERIVED-CONDITIONAL — the structure; the value is a CALIBRATION\]

## **15.3 The verdict, stated symmetrically**

Over-claiming and under-claiming are the same failure, a mismatch between what was shown and what was written. Versions 1.0 and 1.1 of this paper each erred on the first side, in the same way and one section apart. Both halves are therefore said here, and neither is softened.

**ZS-S21 terminal verdict. The cellular transfer-matrix / Hodge-measure sub-bridge is CLOSED at DERIVED-CONDITIONAL on (H-W), (Z-A0), and an orbit-blind plaquette-reduction postulate (Z-A1) applying to both temporal and spatial plaquettes. The transfer matrix PROVES diagonality but PROPAGATES, rather than selects, orbit weights. No continuous dimensionless parameter survives the stated postulate; two survive without it. One overall Yang–Mills scale is calibrated. Full non-perturbative SU(3) glueball dynamics is outside this closure claim.**

What that verdict does NOT license, spelled out so that no later paper can borrow it: it does not license calling the Yang–Mills bridge closed without the qualifier of §0.0, which is now carried in the title; it does not improve the perturbative control of ZS-S17 to ZS-S20 at λ\_t ≈ 5.54; it does not supply the exact Wilson quartic, the non-Abelian Gauss–Coulomb–Faddeev–Popov reduction, the 31-mode non-perturbative Lanczos spectrum, the absolute glueball interaction coefficient, or the continuum scheme matching; it does not attribute the selection of any orbit weight to the transfer matrix, in either class (gate F-S21.12); and it does not make (Z-A1) a theorem.

What it does license, equally plainly: refusing to call this a derivation because one dimensionful scale remains would be wrong, not humble; and re-opening F-S20.5 after §4 has emptied it would be a new error, not caution.

## **15.4 The one sentence on what remains impossible**

After the construction, no further internal calculation selects the remaining orbit weights; their removal requires the explicitly named orbit-blind postulate. Nothing internal to a metric-free cell complex can distinguish the counting weight from any other function of the ambient combinatorial type, in either anisotropy class, so (Z-A1) cannot be derived from within the reduction — it can only be stated, tested against gate F-S21.10, or discriminated experimentally through gate F-S21.8, whose sharpest form is the degeneracy of the third excitation, 3 versus 4, and which is robust across both metric branches.

ZS-S21 v1.2 is the terminal release of the S-line on this question. There is no further reduction to perform: after Theorem S21.1 and Lemma S21.2 what remains is not a calculation but a postulate with a gate on it, and postulates are not shortened by restatement. A further S-paper restating (Z-A1) in new language would be the thirteenth instance of a pattern this corpus has now recorded twelve times — ten in ZS-S20, and twice here. The next genuine move is external: fire F-S21.8, or exhibit the ZS-S14 reduction explicitly enough to decide (H-W) and (Z-A1) from the action itself.

# **Acknowledgements and Code Availability**

This paper was consolidated from Z-Spin Collaboration research notes and from the ten external review cycles of ZS-S20 v1.0–v2.2, whose discipline it inherits. The companion verification suite is zs\_s21\_verify\_v1\_2.py. It rebuilds K\_TI from vertex coordinates with no imported data file, emits its results between the delimiters BEGIN\_ZS\_S21\_RESULTS and END\_ZS\_S21\_RESULTS, prints its own SHA256, and exits non-zero on any FAIL. Environment: Python 3.12.3+, numpy 2.4+, scipy 1.17+, sympy 1.14+, mpmath 1.3.0. Deterministic seed 20260320\. Setting the environment variable ZS\_S21\_FAST=1 runs a reduced version of the §10.2 diagonalisation. No runtime claim is made; runtime is environment-dependent.

# **Appendix A. Verification Ledger**

Fail-closed ledger. Each check-kind entry asserts on a number computed inside the suite. Kinds: C \= check (executable on the Z-Spin object or on the §10.2 model complex), P \= proxy, D \= declarative. The suite exits non-zero on any FAIL.

Table A1. Verification ledger, ZS-S21 v1.2. 88/88 executable checks PASS, 1 proxy, 24 declarative, 0 FAIL.

| Block | IDs | Kind | Content |
| ----- | ----- | ----- | ----- |
| S1 | T001–T003, D004–D005 | C, D | LOCKED constants; hypothesis register (H-W), (Z-A0), (Z-A1); scope declaration |
| S2 | T010–T020 | C | K\_TI reconstruction, chain complex, ranks, census, orbits, δ\_Y \= 7/23 |
| S3 | T030–T038 | C | exact characteristic polynomial, irreducibility, roots, Vieta, trace, multiplicities |
| S4 | T040–T046 | C | |Aut| \= 120, I\_h isotypic decomposition, errata E-1a/E-1b/E-1c |
| S5 | T050–T055 | C | K\_TI × a\_tℤ cell census, temporal bijection, edge congruence, A₆/A₅ |
| S6 | T060–T065 | C | Theorem S21.1: 90 × 90 Hessians, diagonality, and diagonality under orbit-dependent weights in BOTH classes — spatial β₅ \= 1.3, β₆ \= 0.8 and temporal β₅₆ \= 1.3, β₆₆ \= 0.8 |
| S7 | T070–T077, D078 | C, D | Lemma S21.2 (primal congruence), the ambient-star obstruction, the two dual-measure ratios, the live σ-family, Retraction S21-R3 |
| S8 | T080–T096, D086–D087 | C, D | ρ-family, Lemma S20.A1, ψ(n\_f) obstruction, Retraction S21-R2, isotype-resolved branch tables for all three branches, ordering discriminator, D₁ and D₂, branch robustness |
| S9 | T090–T091 | C | (H-TR) is a unit choice |
| S10 | T100–T106, D110 | C, D | Gauss law, census 59 \+ 31, U(1) and SU(2) kernel positivity, SU(3) Casimir C₂(p,q) on a 12 × 12 grid, removal of Outcome D |
| S11 | T120–T141, P150 | C, P | end-to-end compact U(1) diagonalisation on the two-orbit model complex |
| S12 | T160–T163 | C | the ratio table, erratum E-2, erratum E-4, scale invariance |
| S13 | T170–T172, D171 | C, D | anti-numerology on 22 \= 2Q; no coincidence in the closure argument |
| S14 | G200–G215 | D | gate registry, including F-S21.10, F-S21.11 and F-S21.12 |
| S15 | T190 | C | anti-regression static analysis: no check is a literal constant |

# **Appendix B. The Weighted Face Laplacian**

With M₁ \= diag(m\_e) and M₂ \= diag(β\_f) the generalised eigenproblem is M₁⁻¹B₂ᵀM₂B₂ a \= λ a, equivalently Δ₂ \= M₂^{1/2}B₂M₁⁻¹B₂ᵀM₂^{1/2} on 2-cochains. Ordering faces as 12 pentagons then 20 hexagons, and writing x \= r/σ, y \= rρ/σ, z \= r with C the pentagon–hexagon incidence block and A₆₆ the hexagon–hexagon one,  
Δ₂ \= \[\[ 5y·I₁₂ , √(xy)·C \] , \[ √(xy)·Cᵀ , (3x+3z)·I₂₀ \+ z·A₆₆ \]\]  
A₆₆ and CᵀC commute. The kernel sector gives the two linear levels λ\_A \= 3x \+ 3z and λ\_B \= 3x \+ 5z, each of multiplicity 4 and free of y; the (15, −3) block has identically zero determinant, so its eigenvalues are 0 and 5y \+ 3x, the unique nonzero multiplicity-one level. With σ \= 1 by Theorem S21.2 this reads r(3Y+3), r(3Y+5) and rY(5X+3) with X \= ρ, Y \= 1\. This is Lemma S20.A1, imported and re-verified (checks T080, T081). The A\_g isotype is spanned by 1 and by 20·1\_pent − 12·1\_hex; the latter is an exact eigenvector at λ \= 5ρ \+ 3, which equals 8 if and only if ρ \= 1, and it is the coincidence of that level with the ρ-independent G\_g level at 8 that produces the apparent multiplicity 5 recorded in the corpus tables (erratum E-1b).

# **References**

\[1\] J. Kogut and L. Susskind, “Hamiltonian formulation of Wilson’s lattice gauge theories,” Phys. Rev. D 11, 395 (1975).  
\[2\] M. Lüscher, “Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories,” Commun. Math. Phys. 54, 283 (1977).  
\[3\] K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” Ann. Phys. (N.Y.) 110, 440 (1978).  
\[4\] M. Creutz, “Gauge fixing, the transfer matrix, and confinement on a lattice,” Phys. Rev. D 15, 1128 (1977).  
\[5\] N. H. Christ, R. Friedberg and T. D. Lee, “Gauge theory on a random lattice,” Nucl. Phys. B 210, 310 (1982).  
\[6\] N. H. Christ, R. Friedberg and T. D. Lee, “Weights of links and plaquettes in a random lattice,” Nucl. Phys. B 210 \[FS6\], 337 (1982).  
\[7\] K. G. Wilson, “Confinement of quarks,” Phys. Rev. D 10, 2445 (1974).  
\[8\] I. Montvay and G. Münster, Quantum Fields on a Lattice (Cambridge University Press, Cambridge, 1994), ch. 3\.  
\[9\] M. Creutz, Quarks, Gluons and Lattices (Cambridge University Press, Cambridge, 1983).  
\[10\] A. A. Migdal, “Recursion equations in gauge field theories,” Sov. Phys. JETP 42, 413 (1975).  
\[11\] E. Witten, “On quantum gauge theories in two dimensions,” Commun. Math. Phys. 141, 153 (1991).  
\[12\] B. K. Driver, “YM₂: continuum expectations, lattice convergence, and lassos,” Commun. Math. Phys. 123, 575 (1989).  
\[13\] T. Lévy, “Yang–Mills measure on compact surfaces,” Mem. Amer. Math. Soc. 166, no. 790 (2003).  
\[14\] D. N. Arnold, R. S. Falk and R. Winther, “Finite element exterior calculus, homological techniques, and applications,” Acta Numerica 15, 1 (2006).  
\[15\] A. N. Hirani, Discrete Exterior Calculus, Ph.D. thesis, California Institute of Technology (2003).  
\[16\] T. Regge, “General relativity without coordinates,” Nuovo Cimento 19, 558 (1961).  
\[17\] J. M. Drouffe and K. J. M. Moriarty, “Gauge theories on a simplicial lattice,” Nucl. Phys. B 220, 253 (1983).  
\[18\] C. J. Morningstar and M. J. Peardon, “The glueball spectrum from an anisotropic lattice study,” Phys. Rev. D 60, 034509 (1999), arXiv:hep-lat/9901004.  
\[19\] A. Athenodorou and M. Teper, “The glueball spectrum of SU(3) gauge theory in 3+1 dimensions,” JHEP 11, 172 (2020), arXiv:2007.06422.  
\[20\] K. Kang, Geometric Impedance A \= 35/437, ZS-F2 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[21\] K. Kang, Gauge Symmetry Constraint: Why Q \= 11, ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[22\] K. Kang, The Spinor Mass Gap, ZS-S7 v1.0 (Z-Spin Cosmology Collaboration, April 2026).  
\[23\] K. Kang, Master Action Total Closure, ZS-S14 v2.0 (Z-Spin Cosmology Collaboration, May 2026).  
\[24\] K. Kang, The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex, ZS-S17 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026).  
\[25\] K. Kang, The Normalization-Ambiguity Theorem and the Regge-Moduli Exclusion, ZS-S19 (Z-Spin Cosmology Collaboration, 2026).  
\[26\] K. Kang, Non-Identifiability of the Hodge Measure, ZS-S20 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026).  
\[27\] K. Kang, The Hodge–Dirac Complex of the Truncated Icosahedron, ZS-M6 v1.0 (Z-Spin Cosmology Collaboration, 2026).

# **Version History**

v1.2 TERMINAL (July 2026, current): Closing revision in response to the v1.1 external review; no new physics and no ledger number moves. The substantive correction is that v1.1's Theorem S21.2 was too strong: σ \= 1 does NOT follow from (H-W) alone. The two edge orbits have equal primal length but different ambient stars, so the metric-free function ψ\_e({deg f : f ⊃ e}) and every dual measure separate them; the companion computes the circumcentric dual-length ratios 0.8973272361 (intrinsic) and 0.9105929973 (chordal), the latter independently reproducing the ZS-S20 Table 17.1 flat-cone value. Retraction S21-R3 is issued; §5 is split into Lemma S21.2 (PROVEN, primal congruence) and Corollary S21.2a (DERIVED-CONDITIONAL, weight uniformity); and axiom (Z-A1) is expanded from the spatial class to both anisotropy classes and renamed the Orbit-Blind Plaquette Reduction Postulate. The residual is accordingly two ratios σ and ρ, not one. Check T065 is added, showing that the transfer matrix propagates temporal orbit dependence exactly as it propagates spatial; gate F-S21.12 is registered so that no later paper can attribute a selection to the construction. The full metric branch (σ and ρ both metric-induced, λ₁ \= 1.2069213135) is computed and added to Table 6.2, and gate F-S21.8 is shown to be branch-robust: both metric branches place the third excitation at multiplicity 4 (G\_u) against 3 (T₂u) for the counting branch, and D₁ separates by 11.65 % and 12.21 %. The main title is scope-corrected so that the sub-bridge qualifier travels with the citation rather than living in a subtitle. Table 0.2 is relabelled an Outcome Registry, with A′, A″ and A‴ marked as post-review corrective classifications rather than pre-registrations. §15.2 distinguishes scale calibration from dimensional transmutation. §15.1's claim that nothing continuous remains after the theorems is corrected. Check T074's description is narrowed to what its assertion actually tests, and T105 is split so that the SU(3) Casimir C₂(p,q) \= (p² \+ q² \+ pq \+ 3p \+ 3q)/3 is computed rather than described (new T106). Erratum E-9 is added. 88/88 executable checks PASS, 1 proxy, 24 declarative, 0 FAIL. A, Q, dim Z, λ₁, λ\_h all LOCKED.

v1.1 (July 2026): Split the single axiom of v1.0 into (Z-A0) Metric-Free Carrier and (Z-A1) Orbit-Blind Wilson Reduction Postulate after Retraction S21-R2, the invalid inference that a metric-free carrier alone forces β₅ \= β₆; named the Wilson-type reduction as the hypothesis (H-W) and registered F-S21.11 against it; added the Scope Declaration limiting the closure claim to the cellular transfer-matrix / Hodge-measure sub-bridge; corrected v1.0's uniform-0.91 % claim to the mode-dependent shift table; redefined gate F-S21.8 on D₁; rewrote (6.2) to separate shape from scale; added check T064; restated the §10.2 prism computation as a proxy that does not select (Z-A1); corrected the date to July 2026\. Errata E-6, E-7, E-8. 80/80 checks PASS. Superseded by v1.2 in its §5, its axiom (Z-A1), its parameter count, its title, and its Table 0.2 labelling.

v1.0 (March 2026): Initial release. Constructed the Osterwalder–Seiler / Lüscher transfer matrix on K\_TI × a\_tℤ; proved Theorem S21.1 (M diagonal, F-S20.5 superseded by construction); refuted the seed's single-β\_s claim for non-congruent cells against Christ–Friedberg–Lee (Retraction S21-R1); corrected the observable from λ\_k/λ₁ to √(λ\_k/λ₁); reported errata E-1a, E-1b, E-1c, E-2, E-3, E-4 and erratum-candidate E-5; relabelled Λ\_QCD as a calibration without changing its value. Superseded by v1.1 and v1.2. 73/73 checks PASS.