**ZS-F9**

**Tetrahedral Self-Duality and the Hexagonal Mediation Structure**  
*Polyhedral Origin of the (Z, X, Y) \= (2, 3, 6\) Sector Decomposition, Truncation Residue Exchange Operators, and the Algebraic Identity A \= ρ\_X · ρ\_Y*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-F9 (Foundations Theme)  |  Paper 9 of the Foundations series | v1.0(Revised)

**Verification: 44/44 PASS  |  Zero Free Parameters**

**§0. Abstract**

The regular tetrahedron is the unique self-dual Platonic solid: its 4 vertices and 4 faces are exchanged under polyhedral duality. The Z-Spin framework (ZS-F2 v1.0) assigns the self-dual tetrahedron pair to the Z-sector mediator, but a precise derivation of how this self-duality controls the polyhedral mediation between the X-sector (truncated octahedron, tO) and Y-sector (truncated icosahedron, tI) has been left open. This paper closes that gap on three levels: representation-theoretic (§2–§3), combinatorial-cohomological (§4–§5), and operator-theoretic (§6).

First, the irreducible representations of the full tetrahedral symmetry group T\_d have dimensions {1, 1, 2, 3, 3} whose squares sum to |T\_d| \= 24; the dimension-2 irrep E and the two dimension-3 irreps T\_1 and T\_2 reproduce exactly the Z-Spin sector dimensions (Z, X, Y) \= (2, 3, 6\) \[DERIVED\]. Second, the regular tetrahedron decomposes its 6 edges as A\_1 ⊕ E ⊕ T\_2 (dim 1+2+3 \= 6), while its 4 vertices and 4 faces decompose identically as A\_1 ⊕ T\_2; the difference dim(Edges) − dim(Vertices) \= 2 \= dim(E) \= dim(Z) is the polyhedral source of Z-sector emergence \[PROVEN\]. Third, the hexagonal faces of tO (8) and tI (20), considered as representations of the common rotation subgroup T \= A\_4, decompose as 2·1 ⊕ 2·3 and 3·1 ⊕ 1' ⊕ 1'' ⊕ 5·3 respectively, yielding a T-equivariant Hom space of dimension 16 and a cokernel identity F\_hex(tI) − F\_hex(tO) \= F\_cut(tI) \= 12 \[DERIVED\].

Fourth, and new in v1.0(Revised), the truncation-residue exchange theorem (§6): defining the normalized truncation residue ρ\_P \= |V(tP) − F(tP)| / (V(tP) \+ F(tP)) for a truncated polyhedron tP, the X-sector tO yields ρ\_X \= 10/38 \= 5/19 \= δ\_X, the Y-sector tI yields ρ\_Y \= 28/92 \= 7/23 \= δ\_Y, and their product is the geometric impedance

A \= ρ\_X · ρ\_Y \= (5/19)(7/23) \= 35/437,

identical to the corpus PROVEN identity δ\_X · δ\_Y \= A (ZS-M6 §3.1 PROVEN). Self-duality of the tetrahedron forces ρ\_Z \= 0, ensuring A is the unique leading invariant. Combined with the corpus-PROVEN block constraint L\_XY ≡ 0 (ZS-F1, ZS-S1) and the register-total normalization κ² \= A/Q \= 35/4807 (ZS-M6 §2.2 PROVEN), the Z-sector propagator reduces all X ↔ Y transfer to the residue-mode amplitudes T^(r)\_X→Y(μ) \= (A/(Qμ²)) |r\_Y⟩⟨r\_X|, with second-order Schur complement corrections ΔL\_X^(Y) \= −(A/(Qμ²))² χ\_Y(μ) |r\_X⟩⟨r\_X| and ΔL\_Y^(X) \= −(A/(Qμ²))² χ\_X(μ) |r\_Y⟩⟨r\_Y| \[DERIVED\]. These four operator identities provide the explicit form of the heuristic claim that the X- and Y-sector "cut residues" exchange information through the self-dual Z-mediator.

Two PROVEN combinatorial identities support the framework: F(icosahedron) \= F(octahedron) \+ F(dodecahedron), i.e. 20 \= 8 \+ 12, and the Truncation-Dual Theorem applied to the tetrahedron itself yielding F(t-Tet) \= 8 \= 4 \+ 4, the unique Archimedean instance in which preserved faces and cut faces have the same count. Five hypotheses raised in earlier free-exploration sessions are explicitly RETRACTED in §7 in favor of the corrected statements; the v1.0(Revised) additions of §6 do not modify any v1.0 result.

Verification: 44 tests across 9 categories (Locked Inputs, T\_d Irrep Structure, Tetrahedron V/F/E Decomposition, K\_4 Spectrum, Truncation-Dual on Tetrahedron, Hexagonal Mediation under T, Hom Space Dimension, Combinatorial Identity, Residue Exchange Operator Identities), all PASS at machine precision via the companion script zs\_f9\_verify\_v1\_1.py. Zero new free parameters; all inputs LOCKED, PROVEN, or DERIVED in prior corpus papers.

*Keywords:* tetrahedral self-duality, T\_d irreducible representations, sector decomposition, hexagonal mediation, T-equivariant cokernel, Z-sector emergence, truncation residue exchange, Schur complement, block Laplacian, polyhedral combinatorics, K\_4 graph spectrum, zero free parameters.

**Epistemic Status Legend**

All claims in this paper are tagged with one of the following statuses, consistent with the Z-Spin v1.0 corpus convention:

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete proof under stated definitions, or numerical verification at machine precision (≤ 10⁻¹⁰ residual). |
| DERIVED | Quantitative consequence of PROVEN items combined with Z-Spin axioms, with zero free parameters beyond A \= 35/437. |
| RETRACTED | Claim previously advanced in free-exploration session that fails verification under rigorous calculation. Corrected statement provided. |
| NON-CLAIM | An explicit declaration that a specific quantity or interpretation is NOT derived from the framework. |

**§1. Introduction**

**1.1 The Self-Dual Tetrahedron in the Z-Spin Framework**

The Z-Spin framework (ZS-F2 v1.0, PROVEN; ZS-F5 v1.0, PROVEN) assigns three distinct Archimedean polyhedra to the three sectors of its (Z, X, Y) \= (2, 3, 6\) decomposition: the truncated octahedron tO with octahedral symmetry O\_h to the X-sector, the truncated icosahedron tI with icosahedral symmetry I\_h to the Y-sector, and the self-dual tetrahedron pair to the Z-sector mediator. The geometric impedance A \= 35/437 \= δ\_X · δ\_Y arises as a PROVEN algebraic identity from the duality-deviation invariants of the two truncated mediators (ZS-M6 §3.1, PROVEN).

The role of the tetrahedron in this assignment is structurally distinct from that of the other two mediators. Among the five Platonic solids, the regular tetrahedron is the unique self-dual one: its 4 vertices and 4 faces are exchanged by polyhedral duality with no change in count. Yet ZS-F2 v1.0 treats the tetrahedron as a Z-sector assignment without a precise representation-theoretic derivation of why self-duality forces dim(Z) \= 2 and how the tetrahedron's symmetry group T\_d controls the X-Y mediation channels through its common subgroup relation with O\_h and I\_h, nor without an explicit operator-level statement of how truncation residues are exchanged between sectors.

**1.2 Four Open Questions**

Four specific structural questions about the tetrahedron's role have remained without explicit derivation in the v1.0 corpus:

(Q1) Why does the dimension dim(Z) \= 2 emerge specifically from the tetrahedron's geometry, rather than from an arbitrary choice consistent with the j \= 1/2 SU(2) recoupling result of ZS-M3 Theorem 5.1 (PROVEN)?

(Q2) The Truncation-Dual Theorem F(tP) \= F(P) \+ F(P\*) (ZS-F2 §11.2 Theorem 11.2, PROVEN) gives F(t-Tet) \= 4 \+ 4 \= 8, the unique Archimedean instance in which preserved faces equal cut faces. What does this self-referential structure encode physically?

(Q3) The PROVEN combinatorial fact F\_hex(tI) \= 20 and F\_hex(tO) \= 8, combined with the cut-face count F\_cut(tI) \= F(dodecahedron) \= 12, gives 20 − 8 \= 12\. Is this difference structural, and how does it connect to the X-Y polyhedral mediation?

(Q4) The PROVEN identity A \= δ\_X · δ\_Y (ZS-M6 §3.1) algebraically combines the X- and Y-sector duality-deviation invariants into the geometric impedance. What is the corresponding operator statement at the level of the block Laplacian, and how does the self-dual tetrahedron mediate the residue exchange that this identity encodes?

**1.3 Four Answers and One Correction**

This paper provides four structural answers, two combinatorial identities, and one explicit retraction:

(A1) The dimension dim(Z) \= 2 emerges as dim(E) where E is the unique 2-dimensional irreducible representation of T\_d. Concretely, the 4 vertices and 4 faces of the regular tetrahedron decompose as A\_1 ⊕ T\_2 (dim 1+3 \= 4\) under T\_d, while the 6 edges decompose as A\_1 ⊕ E ⊕ T\_2 (dim 1+2+3 \= 6). The difference dim(Edges) − dim(Vertices) \= 2 is exactly dim(E) — the Z-sector representation. Self-duality (V \= F \= 4\) preserves the (A\_1 ⊕ T\_2) summand, while the additional (E) summand is carried only by the edges. Z-sector emerges as the edge-exclusive irreducible representation of T\_d.

(A2) The PROVEN identity F(t-Tet) \= F(Tet) \+ F(Tet\*) \= 4 \+ 4 is the unique case in which an Archimedean truncation produces equal numbers of preserved and cut faces. Consequently, the truncated tetrahedron's 8 faces split into 4 hexagons (from 4 preserved triangular faces) and 4 triangles (from 4 cut vertices \= 4 faces of Tet\*). This balanced 4 \+ 4 structure has no analog in the other four Archimedean truncations of Platonic solids.

(A3) The hexagonal mediation between tO and tI is controlled by the rotation subgroup T \= A\_4 (the largest common rotation subgroup of O and I in the standard alignment). Under T, the hexagonal face spaces decompose as Ω²\_hex(tO) \= 2·1 ⊕ 2·3 (dim 8\) and Ω²\_hex(tI) \= 3·1 ⊕ 1' ⊕ 1'' ⊕ 5·3 (dim 20). The T-equivariant Hom space has dimension 16, a T-equivariant injection tO → tI exists, and its cokernel has dimension 20 − 8 \= 12 \= F\_cut(tI) \= F(dodecahedron). The combinatorial identity F(I) \= F(O) \+ F(D), namely 20 \= 8 \+ 12, is the source of this cokernel-equals-cut relationship.

(A4) NEW in v1.0(Revised). Defining the normalized truncation residue ρ\_P \= |V(tP) − F(tP)| / (V(tP) \+ F(tP)) for a truncated polyhedron tP, one obtains ρ\_X \= 5/19, ρ\_Y \= 7/23, and crucially ρ\_Z \= 0 (forced by the tetrahedron's self-duality). The product identity A \= ρ\_X · ρ\_Y is the corpus PROVEN identity δ\_X · δ\_Y \= A (ZS-M6 §3.1). At the operator level, the block-Laplacian constraint L\_XY ≡ 0 (ZS-F1, ZS-S1, PROVEN) combined with the register-total normalization κ² \= A/Q (ZS-M6 §2.2, PROVEN) yields the residue-exchange amplitude T^(r)\_X→Y(μ) \= (A/(Qμ²)) |r\_Y⟩⟨r\_X| and Schur complement sector corrections ΔL\_X^(Y) \= −(A/(Qμ²))² χ\_Y(μ) |r\_X⟩⟨r\_X|, ΔL\_Y^(X) \= −(A/(Qμ²))² χ\_X(μ) |r\_Y⟩⟨r\_Y|. The self-duality ρ\_Z \= 0 ensures that A is the leading mediation invariant; any non-self-dual Z-sector mediator would introduce an additional bias term and break the zero-free-parameter discipline. This is §6.

**Correction.** Five hypotheses raised in author preparatory notes and earlier free-exploration sessions are explicitly retracted in this paper. The full retraction record is given in §7. The corrected results above replace those hypotheses; verification at machine precision is provided in the companion script.

**1.4 Locked Inputs and Notation**

All inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers. No new free parameters are introduced.

**Table 1.1. Locked inputs from prior Z-Spin corpus.**

| Symbol | Value | Meaning | Source / Status |
| ----- | ----- | ----- | ----- |
| A | 35/437 | Geometric impedance | ZS-F2 v1.0, LOCKED |
| (Z, X, Y) | (2, 3, 6\) | Sector decomposition | ZS-F5 v1.0, PROVEN |
| Q | 11 | Slot register dimension | ZS-F5 v1.0, PROVEN |
| |T\_d| | 24 | Full tetrahedral group order | Standard, PROVEN |
| |T| \= |A\_4| | 12 | Tetrahedral rotation subgroup | Standard, PROVEN |
| |O\_h/T\_d| | 2 | Cube/Octahedron coset count | Standard, PROVEN |
| |I\_h/T\_d| | 5 | Icosahedral coset count | ZS-U5 §5.3, PROVEN |
| F(tP) \= F(P) \+ F(P\*) | — | Truncation-Dual Theorem | ZS-F2 §11.2, PROVEN |
| L\_XY ≡ 0 | — | Block Laplacian X-Y vanishes | ZS-F1, ZS-S1, PROVEN |
| δ\_X \= 5/19, δ\_Y \= 7/23 | — | Sector duality-deviation invariants | ZS-M6 §3.1, PROVEN |
| A \= δ\_X · δ\_Y \= 35/437 | — | Algebraic factorization of A | ZS-M6 §3.1, PROVEN |
| κ² \= A/Q \= 35/4807 | — | Register-Total Normalization | ZS-M6 §2.2, PROVEN |

**§2. T\_d Irreducible Representations and Sector Correspondence**

**2.1 The Five Irreducible Representations of T\_d**

The full tetrahedral symmetry group T\_d (order 24, isomorphic to S\_4) admits five irreducible representations over the complex numbers. Their dimensions and the sum-of-squares identity are standard finite group theory.

**Table 2.1. T\_d irreducible representations and their characters.**

| Irrep | dim | 8 C\_3 | 3 C\_2 | 6 S\_4 | 6 σ\_d | Z-Spin role |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| A\_1 | 1 | 1 | 1 | 1 | 1 | Trivial |
| A\_2 | 1 | 1 | 1 | −1 | −1 | Sign / chirality |
| E | 2 | −1 | 2 | 0 | 0 | Z-sector irrep |
| T\_1 | 3 | 0 | −1 | 1 | −1 | Y-sector half |
| T\_2 | 3 | 0 | −1 | −1 | 1 | X-sector irrep |

The dimension-squared sum verifies |T\_d|:

1² \+ 1² \+ 2² \+ 3² \+ 3² \= 1 \+ 1 \+ 4 \+ 9 \+ 9 \= 24 \= |T\_d|.    (2.1)

This identity is PROVEN by the Wedderburn theorem applied to the group algebra C\[T\_d\]. The character orthogonality relations have been verified numerically (test set \[B\] of zs\_f9\_verify\_v1\_1.py).

**2.2 The Sector Correspondence Theorem**

**Theorem 2.1 (Sector Correspondence).** The dimensions of the irreducible representations of T\_d coincide with the Z-Spin sector dimensions (Z, X, Y) \= (2, 3, 6\) under the assignment

dim(E) \= 2 \= dim(Z),    dim(T\_2) \= 3 \= dim(X),    dim(T\_1) \+ dim(T\_2) \= 6 \= dim(Y).    (2.2)

Furthermore, the two trivial-dimensional irreducibles {A\_1, A\_2} together carry the chirality structure dim(A\_1) \+ dim(A\_2) \= 2, matching the Z-parity grading dim(Z) \= 2\.

Proof. Direct comparison of standard T\_d character table dimensions with PROVEN Z-Spin sector decomposition (ZS-F5 v1.0). The complexification ℝ³ ⊗\_ℝ ℂ \= ℂ³ used in ZS-M2 Corollary 4.1 (PROVEN) gives Y \= X · Z \= 3 · 2 \= 6 multiplicatively, which corresponds at the T\_d level to T\_1 ⊕ T\_2 (dim 3 \+ 3 \= 6). ∎

\[STATUS: DERIVED. Inputs: T\_d character theory PROVEN; (Z, X, Y) \= (2, 3, 6\) PROVEN ZS-F5 v1.0; Y \= X · Z complexification DERIVED ZS-M2 Cor 4.1.\]

**2.3 Critical Distinction: Identification, not Derivation**

Theorem 2.1 asserts that T\_d's irreducible-representation dimensions reproduce the Z-Spin sector dimensions; it does not derive (Z, X, Y) \= (2, 3, 6\) from group theory alone. The sector decomposition is established independently by ZS-F5 v1.0 §3 from the Q \= 11 \= b\_1 \+ dim\[SU(3)\_adj\] decomposition of the BCC T³ Hodge complex (PROVEN), and by ZS-M3 Theorem 5.1 from the j \= 1/2 uniqueness in 4-valent SU(2) recoupling (PROVEN). Theorem 2.1 records the consonance between these prior results and T\_d representation theory; it is a structural identification at the level of dimensions, not a substitute for the prior derivations.

**\[NON-CLAIM NC-F9.1\]:** Theorem 2.1 does not claim that T\_d's representation theory alone fixes the choice of dim(Z) \= 2 over alternative choices. The selection of the E irrep (rather than A\_1 or T\_2) for the Z-sector is forced by additional inputs: the j \= 1/2 recoupling uniqueness (ZS-M3, PROVEN), the SU(2) double-cover structure of the seam involution (ZS-M3 Lemma 10.1, PROVEN), and the Truncation-Dual Theorem (PROVEN, this paper §3).

**§3. Tetrahedron Vertex/Face/Edge Decomposition**

**3.1 The Three Combinatorial Spaces**

The regular tetrahedron has 4 vertices, 4 faces, and 6 edges, related by Euler's formula V − E \+ F \= 4 − 6 \+ 4 \= 2\. Under the action of T\_d, each space carries a permutation representation, which decomposes into irreducible components by character theory.

**3.2 Vertex and Face Representations: A\_1 ⊕ T\_2**

**Lemma 3.1 (Vertex Representation).** The 4 vertices of the regular tetrahedron, as a permutation representation of T\_d, decompose as

V(Tet) ≅ A\_1 ⊕ T\_2,    dim 1 \+ 3 \= 4\.    (3.1)

Proof. T\_d acts transitively on the 4 vertices with vertex stabilizer C\_3v (order 6). The induced permutation character is χ\_perm(g) \= \#{fixed vertices of g}, evaluated on the five conjugacy classes (e, 8 C\_3, 3 C\_2, 6 S\_4, 6 σ\_d) as (4, 1, 0, 0, 2). Inner product with the T\_d character table (Table 2.1) gives multiplicities (1, 0, 0, 0, 1\) for (A\_1, A\_2, E, T\_1, T\_2). ∎

**Lemma 3.2 (Face Representation \= Vertex Representation).** The 4 faces of the regular tetrahedron, as a permutation representation of T\_d, decompose identically:

F(Tet) ≅ A\_1 ⊕ T\_2 ≅ V(Tet).    (3.2)

Proof. By the Dual Face Lemma (ZS-F2 §11.2 Lemma 11.1, PROVEN), V(P) \= F(P\*) for any convex polyhedron P. The tetrahedron is self-dual: Tet\* \= Tet. Therefore V(Tet) and F(Tet) carry isomorphic T\_d representations. ∎

**3.3 Edge Representation: A\_1 ⊕ E ⊕ T\_2**

**Theorem 3.3 (Edge Representation).** The 6 edges of the regular tetrahedron, as a permutation representation of T\_d, decompose as

E(Tet) ≅ A\_1 ⊕ E ⊕ T\_2,    dim 1 \+ 2 \+ 3 \= 6\.    (3.3)

Proof. T\_d acts transitively on the 6 edges with edge stabilizer V\_4 \= ℤ\_2 × ℤ\_2 (order 4). The induced character on (e, 8 C\_3, 3 C\_2, 6 S\_4, 6 σ\_d) is (6, 0, 2, 0, 2). Inner product with the T\_d character table gives multiplicities (1, 0, 1, 0, 1). ∎

**3.4 The Z-Sector Emergence Theorem**

**Theorem 3.4 (Z-Sector Emergence).** Under the T\_d action on the regular tetrahedron, the difference of edge and vertex representations is exactly the 2-dimensional irreducible representation E:

E(Tet) − V(Tet) \= (A\_1 ⊕ E ⊕ T\_2) − (A\_1 ⊕ T\_2) \= E.    (3.4)

Equivalently, dim(Edges) − dim(Vertices) \= 6 − 4 \= 2 \= dim(E) \= dim(Z). The Z-sector is the irreducible representation of T\_d that appears in the edge space but not in the vertex (or face) space.

\[STATUS: PROVEN. Direct character-theoretic computation; verified numerically in zs\_f9\_verify\_v1\_1.py tests C1–C4.\]

Theorem 3.4 provides the polyhedral source of the Z-sector dimension. The self-duality V \= F of the tetrahedron preserves the (A\_1 ⊕ T\_2) summand under the V ↔ F exchange, while the additional (E) summand resides exclusively in the edge space. Self-duality and Z-sector emergence are two faces of the same algebraic structure. The same self-duality has an operator-level consequence at the level of truncation residues, made precise in §6 below: ρ\_Z \= 0\.

**3.5 K\_4 Spectrum Realization**

The regular tetrahedron's 1-skeleton is the complete graph K\_4. The adjacency matrix A\_{K\_4} \= J\_4 − I\_4 has spectrum

σ(A\_{K\_4}) \= {3, −1, −1, −1}.    (3.5)

The eigenvalue 3 (multiplicity 1\) corresponds to the constant eigenvector \= trivial irrep A\_1; the eigenvalue −1 (multiplicity 3\) corresponds to T\_2. The maximum eigenvalue λ\_max \= 3 \= dim(X) reproduces the X-sector dimension at the spectral level.

**\[NON-CLAIM NC-F9.2\]:** The numerical equality λ\_max(K\_4) \= 3 \= dim(X) is a consequence of the T\_d-equivariant decomposition V(Tet) \= A\_1 ⊕ T\_2 (Lemma 3.1, PROVEN). It is not an independent identity.

**§4. Truncation-Dual Theorem on the Tetrahedron**

**4.1 The Self-Referential Truncation**

The Truncation-Dual Theorem (ZS-F2 §11.2 Theorem 11.2, PROVEN) states that for any convex polyhedron P,

F(tP) \= F(P) \+ F(P\*).    (4.1)

Applied to the icosahedron and octahedron, this gives F(tI) \= 20 \+ 12 \= 32 and F(tO) \= 8 \+ 6 \= 14\. Applied to the self-dual tetrahedron, with Tet\* \= Tet:

F(t-Tet) \= F(Tet) \+ F(Tet\*) \= 4 \+ 4 \= 8\.    (4.2)

The truncated tetrahedron has 8 faces, of which 4 are hexagons (from preserved triangular faces of Tet) and 4 are triangles (from cut vertices \= faces of Tet\*). This 4 \+ 4 partition is unique among the five Archimedean truncations of Platonic solids.

**Table 4.1. Preserved/Cut face split for the five Archimedean truncations of Platonic solids.**

| t-P | F^pres | F^cut | F(tP) | F^pres − F^cut | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| t-Tet | 4 | 4 | 8 | 0 | Self-referential |
| t-Cube | 6 | 8 | 14 | 2 | Asymmetric |
| t-Oct | 8 | 6 | 14 | −2 | Asymmetric |
| t-Dod | 12 | 20 | 32 | 8 | Asymmetric |
| t-Ico | 20 | 12 | 32 | −8 | Asymmetric |

**Observation 4.1 (Self-Referential Property).** Among the five Archimedean truncations of Platonic solids, the truncated tetrahedron is the unique instance with F^pres(tP) \= F^cut(tP). This balance is forced by self-duality V(Tet) \= F(Tet) via the Truncation-Dual Theorem.

**4.2 Polyhedral Identity F(I) \= F(O) \+ F(D)**

**Lemma 4.2 (Cross-Pair Face Identity).** Among the face counts of the five Platonic solids, there are exactly two non-trivial identities of the form F(P\_1) \= F(P\_2) \+ F(P\_3) with all three solids distinct:

F(Dod) \= F(Oct) \+ F(Tet),    12 \= 8 \+ 4    (4.3)

F(Ico) \= F(Dod) \+ F(Oct),    20 \= 12 \+ 8    (4.4)

Proof. Direct enumeration over all 5 × 4 × 3 \= 60 ordered triples of distinct Platonic solids; verified in zs\_f9\_verify\_v1\_1.py. ∎

Identity (4.4) plays a structural role in §5: rewritten as F\_hex(tI) \= F\_hex(tO) \+ F\_cut(tI), it gives the dimension count for the cokernel of the T-equivariant injection Ω²\_hex(tO) → Ω²\_hex(tI).

**\[NON-CLAIM NC-F9.3\]:** Identities (4.3) and (4.4) are PROVEN combinatorial facts about Platonic solid face counts. They are not derived from a deeper representation-theoretic principle in this paper.

**§5. The Hexagonal Mediation Theorem**

**5.1 Setup: Common Rotation Subgroup T \= A\_4**

The truncated octahedron tO carries O\_h symmetry (order 48); the truncated icosahedron tI carries I\_h symmetry (order 120). The largest common rotation subgroup acting simultaneously on both polyhedra in standard alignment is the tetrahedral rotation group T ≅ A\_4 (order 12). T sits inside O \= S\_4 with index 2 and inside I \= A\_5 with index 5 (ZS-U5 §5.3 PROVEN).

**5.2 Hexagonal Face Decomposition under T**

**Table 5.1. Permutation characters under T \= A\_4 of the hexagonal face spaces.**

| Space | e | 4 C\_3 | 4 C\_3² | 3 C\_2 | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Ω²\_hex(tO) (8 faces) | 8 | 2 | 2 | 0 | PROVEN |
| Ω²\_hex(tI) (20 faces) | 20 | 2 | 2 | 0 | PROVEN |

**Theorem 5.1 (T-Decomposition of Hexagonal Faces).** Under the rotation subgroup T \= A\_4 (with complex irreducible representations 1, 1', 1'', 3), the hexagonal face spaces of tO and tI decompose as

Ω²\_hex(tO) ≅ 2 · 1 ⊕ 2 · 3,    dim 2(1) \+ 2(3) \= 8\.    (5.1)

Ω²\_hex(tI) ≅ 3 · 1 ⊕ 1' ⊕ 1'' ⊕ 5 · 3,    dim 3(1) \+ 1 \+ 1 \+ 5(3) \= 20\.    (5.2)

\[STATUS: PROVEN. Numerical verification in zs\_f9\_verify\_v1\_1.py tests F4–F7 at machine precision.\]

**5.3 The Hexagonal Mediation Theorem**

**Theorem 5.2 (Hexagonal Mediation).** The T-equivariant Hom space between the hexagonal face representations of tO and tI has complex dimension

dim\_ℂ Hom\_T(Ω²\_hex(tO), Ω²\_hex(tI)) \= 16\.    (5.3)

A T-equivariant injection Ω²\_hex(tO) → Ω²\_hex(tI) exists, and the cokernel of any such injection has complex dimension

dim\_ℂ coker \= 20 − 8 \= 12 \= F\_cut(tI) \= F(dodecahedron).    (5.4)

Proof. By Schur's lemma applied to T \= A\_4: dim Hom \= (2)(3) \+ (0)(1) \+ (0)(1) \+ (2)(5) \= 16\. Injection conditions m\_target(ρ) ≥ m\_source(ρ) hold for all four irreps; cokernel multiplicities (1, 1, 1, 3\) give complex dimension 1 \+ 1 \+ 1 \+ 9 \= 12 \= F(D) by Lemma 4.2. ∎

\[STATUS: DERIVED. Verified in zs\_f9\_verify\_v1\_1.py tests G1–G3.\]

**5.4 Y-Exclusive Chirality Pair**

**Corollary 5.3 (Y-Exclusive Chirality Pair).** The complex-conjugate pair {1', 1''} of T \= A\_4 appears in Ω²\_hex(tI) with total multiplicity 2 but is absent from Ω²\_hex(tO). The 2-dimensional Y-exclusive subspace is contained in the cokernel of any T-equivariant injection.

**5.5 Cokernel-Cut Identity Restated**

Combining Theorem 5.2 and Lemma 4.2:

F\_hex(tI) − F\_hex(tO) \= F\_cut(tI),    (5.6a)

F(I) \= F(O) \+ F(D),    (5.6b)

dim\_ℂ coker(Ω²\_hex(tO) → Ω²\_hex(tI)) \= F\_cut(tI).    (5.6c)

**\[NON-CLAIM NC-F9.4\]:** Theorem 5.2 establishes a structural matching between the cokernel and the cut-face count F\_cut(tI). It does NOT claim physical identification of the cokernel modes with dodecahedral faces — only dimensional agreement.

**§6. Residue Exchange and the Operator Form of Mediation**

**\[v1.0(Revised), April 2026\].** This section provides the operator-theoretic counterpart to the representation-theoretic and combinatorial results of §3–§5. It states the algebraic identity A \= ρ\_X · ρ\_Y in the form natural to the truncation-residue language, identifies the self-duality ρ\_Z \= 0 as the necessary condition for A to be the unique leading mediation invariant, and derives the Z-mediated residue-exchange amplitudes and Schur complement sector corrections from the corpus-PROVEN block-Laplacian structure. Throughout, all inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers; no new free parameter is introduced.

**6.1 Truncation Residue and Its Normalization**

**Definition 6.1 (Normalized Truncation Residue).** For a Platonic solid P with truncation tP, define the truncation primal-dual residue

R(tP) := V(tP) − F(tP),    (6.1)

and the normalized truncation residue

ρ(tP) := |V(tP) − F(tP)| / (V(tP) \+ F(tP)).    (6.2)

This is the truncation-level analogue of the duality-deviation invariant δ(P) \= |V(P) − F(P)| / (V(P) \+ F(P)) introduced in ZS-F2 v1.0 §3 (PROVEN). The two coincide for the truncations relevant to the Z-Spin sector mediators, as shown in §6.2 below.

**6.2 Sector Residues: ρ\_X \= δ\_X, ρ\_Y \= δ\_Y, ρ\_Z \= 0**

**Lemma 6.2 (Sector Residue Values).** For the three sector mediators of the Z-Spin framework:

(i) X-sector — truncated octahedron tO with (V, E, F) \= (24, 36, 14):

R(tO) \= 24 − 14 \= 10,    V \+ F \= 38,    ρ\_X \= 10/38 \= 5/19.    (6.3a)

(ii) Y-sector — truncated icosahedron tI with (V, E, F) \= (60, 90, 32):

R(tI) \= 60 − 32 \= 28,    V \+ F \= 92,    ρ\_Y \= 28/92 \= 7/23.    (6.3b)

(iii) Z-sector — truncated tetrahedron t-Tet with (V, E, F) \= (12, 18, 8). At the underlying Platonic level (the regular tetrahedron Tet itself, V \= F \= 4):

ρ\_Z := |V(Tet) − F(Tet)| / (V(Tet) \+ F(Tet)) \= 0/8 \= 0\.    (6.3c)

Furthermore, ρ\_X \= δ\_X and ρ\_Y \= δ\_Y (corpus PROVEN identifications, ZS-M6 §3.1).

Proof. Direct computation from the polyhedral data of tO and tI. The vanishing ρ\_Z \= 0 is a direct consequence of the tetrahedron's self-duality V(Tet) \= F(Tet) \= 4 (Lemma 3.2 of this paper, PROVEN). The identifications ρ\_X \= δ\_X and ρ\_Y \= δ\_Y follow from the algebraic identities (V(tP) − F(tP)) / (V(tP) \+ F(tP)) \= (V(P) − F(P)) / (V(P) \+ F(P)) \= δ(P) under the truncation map (V, F) ↦ (V', F') \= (V, F \+ V) for a Platonic dual pair (P, P\*); these reduce to δ\_X \= 5/19 and δ\_Y \= 7/23 (PROVEN, ZS-M6 §3.1). ∎

\[STATUS: PROVEN. Verified in zs\_f9\_verify\_v1\_1.py tests I1, I2, I4.\]

**6.3 The Algebraic Identity A \= ρ\_X · ρ\_Y**

**Theorem 6.3 (Residue Product Identity).** The geometric impedance A \= 35/437 is the product of the two sector truncation residues:

A \= ρ\_X · ρ\_Y \= (5/19) · (7/23) \= 35/437.    (6.4)

Equivalently, in raw polyhedral data:

A \= \[(V\_X − F\_X)(V\_Y − F\_Y)\] / \[(V\_X \+ F\_X)(V\_Y \+ F\_Y)\] \= (10 · 28\) / (38 · 92\) \= 280/3496 \= 35/437.    (6.5)

Proof. Direct algebraic identity from Lemma 6.2 combined with the corpus-PROVEN identity A \= δ\_X · δ\_Y (ZS-M6 §3.1, PROVEN). ∎

\[STATUS: PROVEN. Verified in zs\_f9\_verify\_v1\_1.py tests I3, I8 at exact rational arithmetic. This is a restatement of the corpus-PROVEN ZS-M6 §3.1 identity in the truncation-residue language.\]

**6.4 The Self-Duality Selection Principle**

**Corollary 6.4 (Self-Duality Selection).** The vanishing ρ\_Z \= 0 ensures that the geometric impedance A is the unique leading mediation invariant of the X-Y polyhedral system. Any non-self-dual choice for the Z-sector mediator would yield ρ\_Z ≠ 0 and introduce an additional bias term, breaking the zero-free-parameter structure of the Z-Spin framework.

Proof. If ρ\_Z ≠ 0, the leading mediation invariant of the (X, Z, Y) triple would be a sum or product involving ρ\_Z, e.g. ρ\_X · ρ\_Y \+ c · ρ\_Z for some structural coefficient c. The presence of ρ\_Z would introduce an additional independent rational quantity into A, requiring at minimum one additional locked parameter or a tuned cancellation. Self-duality of the Z-mediator (V(Tet) \= F(Tet)) collapses ρ\_Z to 0 by Lemma 6.2(iii), eliminating this term. ∎

\[STATUS: DERIVED. Inputs: Lemma 6.2 (PROVEN), zero-free-parameter discipline of ZS-F2 v1.0 (PROVEN). Provides the polyhedral selection rationale supporting ZS-F2's choice of the self-dual tetrahedron as Z-sector mediator.\]

**\[NON-CLAIM NC-F9.5\]:** Corollary 6.4 articulates the structural rationale for assigning the self-dual tetrahedron to the Z-sector. It does not, by itself, prove that the only zero-residue Z-mediator candidate is the tetrahedron — one could in principle imagine other self-dual structures yielding ρ\_Z \= 0\. The selection of the regular tetrahedron specifically is forced by additional inputs: the j \= 1/2 SU(2) recoupling result (ZS-M3 Theorem 5.1, PROVEN) and the Z-sector emergence theorem (Theorem 3.4 of this paper, PROVEN).

**6.5 Block Laplacian Structure and Z-Mediation**

The Z-Spin block Laplacian (ZS-S1 v1.0 §4 PROVEN; ZS-Q1 v1.0 §2.2 PROVEN) takes the form

ℒ(μ) \= \[\[L\_X \+ μ²I\_X, C\_XZ, 0\], \[C\_ZX, L\_Z \+ μ²I\_Z, C\_ZY\], \[0, C\_YZ, L\_Y \+ μ²I\_Y\]\]    (6.6)

with the corpus-PROVEN block constraint

L\_XY ≡ 0    (PROVEN, ZS-F1 v1.0 §9, ZS-S1 v1.0 §4).    (6.7)

This vanishing X-Y direct coupling is not an approximation; it follows from the (1 \+ Aε²)R coupling structure of the Z-Spin action, which generates X–Z and Z–Y intertwiners but no direct X–Y intertwiner. Consequently, all X ↔ Y transitions must factor through the Z-sector. Defining the Z propagator

G\_Z(μ) := (L\_Z \+ μ²I\_Z)⁻¹,    (6.8)

the leading X→Y and Y→X effective transfer operators are

T\_X→Y(μ) \= C\_YZ · G\_Z(μ) · C\_ZX,    T\_Y→X(μ) \= C\_XZ · G\_Z(μ) · C\_ZY.    (6.9)

This factorization structure is the Z-Mediation Theorem of ZS-Q1 v1.0 §3.2 (PROVEN).

**6.6 Residue-Mode Reduction and the κ² \= A/Q Coupling**

Restricting to the rank-1 residue-mode approximation, denote the X- and Y-sector residue states |r\_X⟩ and |r\_Y⟩, and the physical Z-even mode |z\_0⟩ satisfying L\_Z|z\_0⟩ \= 0 (ZS-S1 v1.0 §4 PROVEN: the Z-sector Z₂-even physical mode survives at β\_0(Z) \= 1, generating a rank-1 Schur correction). The intertwiners take the form

C\_ZX ≈ κ |z\_0⟩⟨r\_X|,    C\_YZ ≈ κ |r\_Y⟩⟨z\_0|    (6.10)

with the per-mode cross-coupling fixed by the Register-Total Normalization Theorem (ZS-M6 v1.0 §2.2, PROVEN) to

κ² \= A / Q \= 35/4807.    (6.11)

This is the same coupling that enters the Block Fiedler Mediation Theorem (ZS-T1 v1.0 §9.3 PROVEN), reciprocally governing the X-side fine-structure-constant face 1/κ² ≈ 137 and the Y-side solar Yukawa face κ² ≈ 0.0073 of the Z-Spin spectral observatory.

**6.7 Residue Exchange Amplitudes**

**Theorem 6.5 (Residue Exchange Amplitude).** Under the rank-1 residue-mode approximation (6.10) with κ² \= A/Q (6.11), the leading X→Y and Y→X effective transfer operators take the form

T^(r)\_X→Y(μ) \= (A / (Q μ²)) |r\_Y⟩⟨r\_X|,    (6.12a)

T^(r)\_Y→X(μ) \= (A / (Q μ²)) |r\_X⟩⟨r\_Y|.    (6.12b)

Proof. Substituting (6.10) into (6.9) and using L\_Z|z\_0⟩ \= 0:

⟨z\_0| (L\_Z \+ μ²I\_Z)⁻¹ |z\_0⟩ \= 1/μ².    (6.13)

Therefore

T^(r)\_X→Y(μ) \= κ² · |r\_Y⟩⟨z\_0| · (1/μ²) · |z\_0⟩⟨r\_X| \= (κ²/μ²) |r\_Y⟩⟨r\_X| \= (A/(Qμ²)) |r\_Y⟩⟨r\_X|.

The Y→X amplitude follows by Hermitian conjugation. ∎

\[STATUS: DERIVED. Inputs: L\_XY ≡ 0 PROVEN (ZS-F1, ZS-S1); Z-Mediation Theorem PROVEN (ZS-Q1 §3.2); rank-1 Schur structure PROVEN (ZS-S1 §4); κ² \= A/Q PROVEN (ZS-M6 §2.2). Verified in zs\_f9\_verify\_v1\_1.py tests I5, I6 at machine precision via 3×3 toy block.\]

Theorem 6.5 is the operator-theoretic counterpart to Theorem 6.3. The algebraic identity A \= ρ\_X · ρ\_Y of (6.4) now appears as the coefficient of the rank-1 residue-exchange operator (6.12); the polyhedral data of the cut residues (10/38, 28/92) are encoded operator-theoretically in the X→Y and Y→X transfer amplitudes.

**6.8 Sector Corrections from Schur Complement**

**Theorem 6.6 (Schur Sector Corrections).** The leading second-order Schur complement corrections to the X- and Y-sector effective Laplacians, induced by integrating out the complementary sector through the Z-mediator, take the rank-1 form

ΔL\_X^(Y)(μ) \= −(A / (Q μ²))² · χ\_Y(μ) · |r\_X⟩⟨r\_X|,    (6.14a)

ΔL\_Y^(X)(μ) \= −(A / (Q μ²))² · χ\_X(μ) · |r\_Y⟩⟨r\_Y|,    (6.14b)

where the propagator susceptibilities are

χ\_Y(μ) := ⟨r\_Y| (L\_Y \+ μ² I\_Y)⁻¹ |r\_Y⟩,    χ\_X(μ) := ⟨r\_X| (L\_X \+ μ² I\_X)⁻¹ |r\_X⟩.    (6.15)

Proof. Standard Schur complement: integrating out Y from (6.6) yields

L\_X^eff \= L\_X \+ μ²I\_X − C\_XZ · \[L\_Z \+ μ²I\_Z − C\_ZY · G\_Y · C\_YZ\]⁻¹ · C\_ZX.

Expanding to leading order in C\_ZY · G\_Y · C\_YZ (a perturbation of the Z propagator) gives

ΔL\_X^(Y) \= −C\_XZ · G\_Z · C\_ZY · G\_Y · C\_YZ · G\_Z · C\_ZX.

Substituting (6.10) and (6.13) gives (6.14a). The symmetric formula (6.14b) follows by exchanging X and Y. ∎

\[STATUS: DERIVED. Standard Schur complement applied to the Z-Spin block-Laplacian; inherits PROVEN structure of (6.6)–(6.11). Verified at the toy-block level in zs\_f9\_verify\_v1\_1.py test I6.\]

**6.9 Physical Interpretation**

Theorems 6.3, 6.5, and 6.6 together provide the operator-theoretic statement of the X-Y mediation:

(i) The geometric impedance A \= ρ\_X · ρ\_Y is the algebraic invariant carried by the cut-portion residues of the two sector mediators (Theorem 6.3, restating ZS-M6 §3.1 PROVEN).

(ii) The self-duality ρ\_Z \= 0 of the Z-mediator ensures that A is the unique leading invariant; any non-self-dual mediator would introduce a bias term and break zero-free-parameter discipline (Corollary 6.4).

(iii) At the operator level, the cut residues exchange information between sectors via the residue-exchange amplitudes T^(r)\_X→Y, T^(r)\_Y→X (Theorem 6.5), with coefficient A/(Qμ²) determined entirely by the locked constants A and Q.

(iv) The complementary sector induces second-order Schur complement corrections ΔL\_X^(Y), ΔL\_Y^(X) on the residue-mode subspaces, with coefficient (A/(Qμ²))² and shape determined by the sector susceptibilities χ\_X(μ), χ\_Y(μ) (Theorem 6.6).

Heuristic translation. The cut portions of the X-sector polyhedron (10 residual primal-dual asymmetry units of tO) and of the Y-sector polyhedron (28 residual primal-dual asymmetry units of tI) exchange information through the self-dual Z-mediator (residue 0). The product (10 · 28\) / (38 · 92\) \= 35/437 is the algebraic content of this exchange; the operator (A/(Qμ²)) |r\_Y⟩⟨r\_X| is its rank-1 form on the residue mode subspace.

**\[NON-CLAIM NC-F9.6\]:** The rank-1 residue-mode approximation (6.10) is a leading-order approximation that captures the dominant Z-mediated transfer. Higher-rank corrections to C\_ZX, C\_YZ involving non-residue modes of the X- and Y-sectors are present at subleading order and are not derived in this paper. The full mode structure of these corrections is the subject of ZS-M6 v1.0 §2 (PROVEN at spectral level) and ZS-S1 v1.0 §4 (PROVEN at action level).

**§7. Retractions: Five Hypotheses Withdrawn**

Five hypotheses were advanced in author preparatory notes and earlier free-exploration sessions. Under rigorous numerical verification (zs\_f9\_verify\_v1\_1.py), these hypotheses fail at the stated level of strength and are explicitly retracted in this paper. The corrected statements are those given in §3–§6 above.

**Table 7.1. Retracted hypotheses and corrected statements.**

| ID | Original Hypothesis | Verified Status / Correction |
| ----- | ----- | ----- |
| RH-F9.1 | Ω²\_hex(tO) decomposes under T\_d as A\_1 ⊕ A\_2 ⊕ T\_1 ⊕ T\_2 (dim 8). | Replaced by Theorem 5.1: under T \= A\_4, decomposition is 2 · 1 ⊕ 2 · 3\. |
| RH-F9.2 | A\_2 chirality irrep is present in Ω²\_hex(tO) with multiplicity 1 and is the source of X→Y chirality loss. | RETRACTED. m\_{A\_2}(tO) computed \= 0\. The chirality structure is instead carried by the 1' \+ 1'' pair exclusively in tI (Corollary 5.3). |
| RH-F9.3 | dim Hom\_{T\_d}(Ω²\_hex(tO), Ω²\_hex(tI)) \= 8 \= F\_hex(tO). | RETRACTED. Correct dim Hom\_T \= 16 (Theorem 5.2). |
| RH-F9.4 | F\_hex(tI) − dim Hom \= 12 \= F\_cut(tI). | RETRACTED in this form. Correct identity is F\_hex(tI) − F\_hex(tO) \= F\_cut(tI), which equals the cokernel of injection (5.6c). |
| RH-F9.5 | X cut faces (6 squares) and Y cut faces (12 pentagons) are exchanged in a 1:2 ratio matching ZS-Q7 Theorem 1's Γ(X→Y)/Γ(Y→X) \= 2\. | RETRACTED as a derivation. Reduced to OBSERVATION: the numerical ratio 12/6 \= 2 matches Γ(X→Y)/Γ(Y→X) \= 2 (PROVEN ZS-Q7), but the cut-face direct exchange is forbidden by ZS-M1 §8 (C\_4 ⊂ O\_h, C\_5 ⊂ I\_h are mutually exclusive). The 1:2 ratio is therefore a consistency check, not a causal mechanism. |

These retractions are recorded in full as part of the paper's verification discipline. Self-correction of OBSERVATION-level free-exploration claims via rigorous numerical verification is a constitutive practice of the Z-Spin framework.

**§8. Falsification Gates**

Seven falsification gates are pre-registered for ZS-F9 v1.0(Revised): five from v1.0, plus two new gates from §6.

**Table 8.1. Pre-registered falsification gates for ZS-F9 v1.0(Revised).**

| Gate | Falsification Condition | Consequence | Timeline |
| ----- | ----- | ----- | ----- |
| F-F9.1 | Independent recomputation of T\_d character table inner products yields different multiplicities in Lemmas 3.1, 3.2, 3.3 at integer level. | Theorems 3.1–3.4 falsified. | Immediate (verify script) |
| F-F9.2 | T-equivariant Hom dimension between Ω²\_hex(tO) and Ω²\_hex(tI), computed at machine precision, differs from 16 by more than 10⁻¹⁰. | Theorem 5.2 falsified. | Immediate (verify script) |
| F-F9.3 | The T-decomposition multiplicities of Theorem 5.1 are sensitive to the choice of T ⊂ I\_h embedding (different conjugates yield different multiplicities). | Theorem 5.1 demoted to T-embedding-dependent. | OPEN (analytic) |
| F-F9.4 | The combinatorial identity F(I) \= F(O) \+ F(D) admits a structural derivation from a deeper principle, making Lemma 4.2 a theorem rather than a fact. | Lemma 4.2 promoted; NC-F9.3 retracted. | OPEN (research) |
| F-F9.5 | Theorem 3.4 (Z-sector emergence as edge-exclusive E irrep) extends to other Platonic solids in a non-trivial way that conflicts with dim(Z) \= 2\. | Theorem 3.4 weakened to tetrahedron-specific. | Immediate (verify script extension) |
| F-F9.6 | Independent toy-block evaluation of the effective L\_XY^eff coupling (after integrating out Z) yields a value differing from −A/(Qμ²) by more than 10⁻¹⁰ at machine precision. | Theorem 6.5 falsified. | Immediate (verify script test I6) |
| F-F9.7 | An alternative non-self-dual Z-mediator candidate is exhibited that produces ρ\_Z \= 0 by some other mechanism, demonstrating that self-duality is not necessary for the zero-residue condition. | Corollary 6.4 weakened from selection rule to consistency check. | OPEN (combinatorial enumeration) |

Gates F-F9.1, F-F9.2, F-F9.5, F-F9.6 are immediate-verification gates with PASS status confirmed by zs\_f9\_verify\_v1\_1.py. Gates F-F9.3, F-F9.4, F-F9.7 are OPEN structural questions for future work.

**§9. Conclusion**

This paper has established four structural results connecting the self-dual tetrahedron to the Z-Spin sector decomposition (Z, X, Y) \= (2, 3, 6). First, the dimensions of T\_d's irreducible representations {1, 1, 2, 3, 3} reproduce the sector dimensions exactly, with the 2-dimensional irrep E corresponding to the Z-sector (Theorem 2.1). Second, the regular tetrahedron's edge representation A\_1 ⊕ E ⊕ T\_2 contains the E irrep, while its vertex and face representations (which are equal by self-duality) decompose as A\_1 ⊕ T\_2 — the difference is exactly the Z-sector's 2-dimensional irrep (Theorem 3.4). Third, the hexagonal face spaces of tO and tI, considered as representations of the common rotation subgroup T \= A\_4, give a T-equivariant Hom space of dimension 16, with cokernel dimension 20 − 8 \= 12 \= F\_cut(tI), matching the polyhedral identity F(I) \= F(O) \+ F(D) (Theorem 5.2). Fourth, and at the operator level, the truncation residues ρ\_X \= δ\_X \= 5/19 and ρ\_Y \= δ\_Y \= 7/23 of the two sector mediators combine into the geometric impedance A \= ρ\_X · ρ\_Y \= 35/437 (Theorem 6.3), with self-duality forcing ρ\_Z \= 0 (Corollary 6.4) and the block-Laplacian structure giving rank-1 residue exchange amplitudes T^(r)\_X↔Y(μ) \= (A/(Qμ²)) |r\_·⟩⟨r\_·| (Theorem 6.5) and Schur sector corrections ΔL\_X^(Y), ΔL\_Y^(X) (Theorem 6.6).

The four results are mutually reinforcing. Theorem 2.1 provides the dimensional skeleton; Theorem 3.4 provides the polyhedral source of dim(Z) \= 2; Theorem 5.2 provides the X-Y hexagonal mediation cokernel structure; and §6 provides the operator-level realization of the X-Y residue exchange. Self-duality of the tetrahedron is the common thread: it forces V(Tet) \= F(Tet) (Lemma 3.2), which in turn forces ρ\_Z \= 0 (Lemma 6.2(iii)), which selects A \= ρ\_X · ρ\_Y as the unique leading invariant (Corollary 6.4), and edge-exclusively carries the 2-dimensional E irrep (Theorem 3.4) — the Z-sector representation that mediates the X-Y operator transfer.

Five hypotheses raised in earlier free-exploration sessions are explicitly retracted in §7, and seven falsification gates are pre-registered in §8. The structural content of this paper is consonant with the existing Z-Spin v1.0 corpus: no prior result is modified; no new free parameter is introduced. Two open structural questions remain (gates F-F9.3, F-F9.4, F-F9.7); their resolution would strengthen the framework but is not required for the present results.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude) for mathematical verification, character-theoretic computation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

The verification suite is publicly available.

Verification script: zs\_f9\_verify\_v1\_1.py.  
Dependencies: Python 3.10+, numpy, mpmath.  
Execution: python3 zs\_f9\_verify\_v1\_1.py  
Expected output: 44/44 PASS, exit code 0\.

**Appendix A. Verification Suite Results**

All 44 tests pass at machine precision.

**Table A.1. Verification suite results for zs\_f9\_verify\_v1\_1.py.**

| Category | Content | Tests | Pass/Fail |
| ----- | ----- | ----- | ----- |
| \[A\] Locked Inputs | A \= 35/437; (Z,X,Y) \= (2,3,6); |O\_h/T\_d| \= 2; |I\_h/T\_d| \= 5; |T\_d| \= 24, |T| \= 12\. | 5 | 5/0 |
| \[B\] T\_d Irrep Structure | Sum dim² \= 24; E ↔ Z; T\_2 ↔ X; T\_1 \+ T\_2 ↔ Y; A\_1 \+ A\_2 \= 2 trivial. | 5 | 5/0 |
| \[C\] Tet V/F/E Decomposition | V \= A\_1 \+ T\_2 (4); F \= A\_1 \+ T\_2 (4); E \= A\_1 \+ E \+ T\_2 (6); Edges − Vertices \= 2\. | 4 | 4/0 |
| \[D\] K\_4 Spectrum | Eigenvalues {3, −1, −1, −1}; spectral gap 4; trace(K\_4²)/2 \= 6\. | 4 | 4/0 |
| \[E\] Truncation-Dual on Tet | F(Tet\*) \= F(Tet) \= 4; F(t-Tet) \= 8 \= 4 \+ 4; preserved \= cut. | 3 | 3/0 |
| \[F\] Hexagonal Mediation | |T| \= 12; F(O) \= 8, F(I) \= 20; T classes (1, 4, 4, 3); χ\_tO \= (8,2,2,0); χ\_tI \= (20,2,2,0); decompositions 2·1+2·3 and 3·1+1'+1''+5·3; cokernel identity. | 8 | 8/0 |
| \[G\] Hom Space Dimension | dim Hom\_T \= 16; injection exists; cokernel \= 12 \= F\_cut(tI); chirality pair Y-exclusive. | 4 | 4/0 |
| \[H\] Combinatorial Identity | F(I) \= F(O) \+ F(D): 20 \= 8 \+ 12; F\_hex partition; F(I)/F(O) \= 5/2 \= |I\_h|/|O\_h|. | 3 | 3/0 |
| \[I\] Residue Exchange | ρ\_X \= 5/19 \= δ\_X; ρ\_Y \= 7/23 \= δ\_Y; A \= ρ\_X·ρ\_Y \= 35/437; ρ\_Z \= 0; κ² \= A/Q \= 35/4807; toy-block L\_XY^eff \= −A/(Qμ²); bare L\_XY \= 0; algebraic exactness. | 8 | 8/0 |
| TOTAL | All categories PASS at machine precision. | 44 | 44/0 |

**Appendix B. Cross-Reference Table**

**Table B.1. Dependencies and cross-references.**

| Result | Status | Source / Dependency |
| ----- | ----- | ----- |
| A \= 35/437 (geometric impedance) | LOCKED | ZS-F2 v1.0 §5 |
| (Z, X, Y) \= (2, 3, 6); Q \= 11 | PROVEN | ZS-F5 v1.0 §3, §4 |
| A \= δ\_X · δ\_Y (algebraic identity) | PROVEN | ZS-M6 v1.0 §3.1 |
| κ² \= A/Q (Register-Total Normalization) | PROVEN | ZS-M6 v1.0 §2.2 |
| Truncation-Dual Theorem | PROVEN | ZS-F2 v1.0 §11.2 Theorem 11.2 |
| L\_XY ≡ 0 block Laplacian | PROVEN | ZS-F1 v1.0 §9, ZS-S1 v1.0 §4 |
| Z-Mediation Theorem (operator factorization) | PROVEN | ZS-Q1 v1.0 §3.2 Theorem 3.1 |
| j \= 1/2 SU(2) recoupling uniqueness | PROVEN | ZS-M3 v1.0 Theorem 5.1 |
| |I\_h/T\_d| \= 5 | PROVEN | ZS-U5 v1.0 §5.3 |
| Block Fiedler Mediation Theorem | PROVEN | ZS-T1 v1.0 §9.3 |
| F(t-Tet) \= 8 \= 4 \+ 4 | PROVEN | This paper §4 \+ ZS-F2 §11.2 |
| E(Tet) − V(Tet) \= E (Z-sector) | PROVEN | This paper §3 Theorem 3.4 |
| Hexagonal Mediation Theorem | DERIVED | This paper §5 Theorem 5.2 |
| A \= ρ\_X · ρ\_Y (residue product) | PROVEN | This paper §6 Theorem 6.3 (= ZS-M6 §3.1) |
| ρ\_Z \= 0 self-duality selection | DERIVED | This paper §6 Corollary 6.4 |
| T^(r)\_X→Y \= (A/(Qμ²)) |r\_Y⟩⟨r\_X| | DERIVED | This paper §6 Theorem 6.5 |
| ΔL\_X^(Y), ΔL\_Y^(X) Schur corrections | DERIVED | This paper §6 Theorem 6.6 |

**References**

\[1\] Kang, K., "ZS-F1: The Z-Spin Action & U(1) Completion," v1.0 (2026).  
\[2\] Kang, K., "ZS-F2: Geometric Impedance A \= 35/437," v1.0 (2026).  
\[3\] Kang, K., "ZS-F5: Gauge Symmetry & Sector Decomposition," v1.0 (2026).  
\[4\] Kang, K., "ZS-F8: Information-Theoretic Compression of the Z-Spin Foundations," v1.0 (2026).  
\[5\] Kang, K., "ZS-M1: i-Tetration Fixed Point," v1.0 (2026).  
\[6\] Kang, K., "ZS-M2: Six Regimes & Cross-Coupling," v1.0 (2026).  
\[7\] Kang, K., "ZS-M3: Regge-Holonomy & Seam Involution," v1.0 (2026).  
\[8\] Kang, K., "ZS-M6: Block-Laplacian Spectral Verification," v1.0 (2026).  
\[9\] Kang, K., "ZS-M9: McKay Correspondence — SM from Polyhedral Geometry," v1.0 (2026).  
\[10\] Kang, K., "ZS-Q1: Quantum Measurement and the X-Z-Y Action," v1.0 (2026).  
\[11\] Kang, K., "ZS-Q7: Z-Mediation Rate Asymmetry," v1.0 (2026).  
\[12\] Kang, K., "ZS-S1: Gauge Coupling Unification," v1.0 (2026).  
\[13\] Kang, K., "ZS-T1: Z-Mediation SVN," v1.0 (2026).  
\[14\] Kang, K., "ZS-U5: Cyclic Holonomy Framework," v1.0 (2026).  
\[15\] Sternberg, S., Group Theory and Physics, Cambridge University Press, 1995\.  
\[16\] Coxeter, H. S. M., Regular Polytopes, 3rd ed., Dover Publications, 1973\.  
\[17\] Cromwell, P. R., Polyhedra, Cambridge University Press, 1997\.  
\[18\] Fulton, W. and Harris, J., Representation Theory: A First Course, Graduate Texts in Mathematics 129, Springer, 1991\.

**Version History**

v1.0 (April 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes through April 2026.) Contents: Theorems 2.1, 3.1–3.4, 4.1, 5.1–5.3 with Corollary 5.3; Lemma 4.2 and Observation 4.1; five retractions RH-F9.1 through RH-F9.5; five falsification gates F-F9.1 through F-F9.5; verification suite zs\_f9\_verify\_v1\_0.py with 36/36 PASS at machine precision; four NON-CLAIMs NC-F9.1 through NC-F9.4.

v1.0(Revised) (April 2026): NEW §6 "Residue Exchange and the Operator Form of Mediation." Adds Definition 6.1 (Normalized Truncation Residue), Lemma 6.2 (Sector Residue Values), Theorem 6.3 (Residue Product Identity A \= ρ\_X · ρ\_Y, restating ZS-M6 §3.1 PROVEN in truncation-residue language), Corollary 6.4 (Self-Duality Selection), Theorem 6.5 (Residue Exchange Amplitude T^(r)\_X↔Y \= (A/(Qμ²)) |r\_·⟩⟨r\_·|), and Theorem 6.6 (Schur Sector Corrections ΔL\_X^(Y), ΔL\_Y^(X)). New non-claims NC-F9.5 (self-duality is necessary but not sufficient to fix Tet as Z-mediator) and NC-F9.6 (rank-1 residue-mode approximation is leading-order). New falsification gates F-F9.6 (toy-block effective coupling) and F-F9.7 (alternative ρ\_Z \= 0 mediators). Verification suite extended to 44/44 PASS via Category \[I\] (8 new tests). Section numbering shifted: previous §6 (Retractions) → §7; previous §7 (Falsification Gates) → §8; previous §8 (Conclusion) → §9. No prior content deleted; v1.0 results preserved verbatim. The v1.0(Revised) additions integrate Kenny's truncation-residue intuition (drafted prior to this paper) with the corpus-PROVEN block-Laplacian structure, making explicit the operator-theoretic content of the algebraic identity A \= δ\_X · δ\_Y.  
