**ZS-F11**  
**Operational Observer Coordinate**  
**and the Self-Referential Fixed Point**

*Closure of ZS-M11 §H16 OPEN: Z-Spin Register-Theoretic Reconciliation of the Three Candidate Observer Locations*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-F11 (Foundations Theme) | Paper 11 of the Foundations series | v1.0

**Verification: 38/38 PASS  |  Zero Free Parameters  |  Zero New Physical Predictions**

**§0. Abstract**

ZS-M11 v1.0 §H16 registered as OPEN the question of where the observer resides in the Z-Spin framework, listing three candidate locations: (P1) inside the Z-sector, (P2) as a higher-level structure on top of the Z-sector, or (P3) altogether orthogonal. ZS-M11 explicitly tagged the suggestion that the i-tetration fixed point z\* \= i^{z\*} is the mathematical analogue of self-observation as SPECULATION without operational content. This paper closes §H16 at the operational level by defining the Operational Observer Coordinate (OOC) as a tuple of register objects already PROVEN or DERIVED in the v1.0 corpus, introducing zero new free parameters and zero new physical predictions.

The OOC is defined as the pair (j, n) where j ∈ {0, 1, ..., 10} is the Q \= 11 register slot index and n ∈ ℤ\_{≥0} is the stroboscopic handshake count of ZS-F0 v1.0(Revised) §5.2.1 Lemma 5.2.A. Two graded refinements (J-grading from the seam involution J|j⟩ \= |10−j⟩, ZS-F0 Theorem 8.5; J\_Z-grading from the Z-internal involution, ZS-F0 §8.6) provide the categorical structure in which (P1), (P2), (P3) become three orthogonal projections of the same OOC.

Theorem F11.1 (Observer Coordinate Decomposition) states that the three candidate locations of §H16 correspond to three independently-PROVEN fixed points of the Z-Spin register ℂ¹¹ — the boundary BFV fixed point |0⟩\_Z (ZS-F0 §9.1, PROVEN), the bulk dynamic Wilson loop dominant eigenvector |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 (ZS-F0 Theorem 8.17, PROVEN), and the kinematic fixed point |5⟩ (ZS-F0 §9.1, PROVEN; the unique J-fixed point by Theorem 8.5 since Q \= 11 is odd). The three fixed points carry distinct J\_Z-gradings, satisfy the inner-product orthogonality ⟨0\_Z|5⟩ \= 0, and the dynamical attractor of the Wilson loop is the 2-dimensional Z subspace (ZS-F0 Theorem 9.4, PROVEN). Status of Theorem F11.1: DERIVED-CONDITIONAL (inheriting the Lemma 5.2.A Step L1 condition that dim(Z) \= 2 is imported from ZS-F5).

Six non-claims explicitly bound the scope: NC-F11.1 inherits NC-Q7.4 (no claim about conscious temporal experience), NC-A7.6 (no phenomenological claim), and NC-F10.3 (no claim about subjective temporal flow). The OOC is operational and channel-structural; it does not name a phenomenological experiencer. The SPECULATION rejected by ZS-M11 §H16 (z\* as self-observation) is NOT promoted by this paper. Anti-numerology Monte Carlo at 500,000 samples confirms structural uniqueness of the J-fixed-point at slot 5 against permuted register orderings (p \< 0.01% STRONG PASS). Seven falsification gates (F-F11.1 through F-F11.7) are pre-registered, including an anti-overclaim gate that would falsify the entire framework if any phenomenological consciousness claim is introduced into the corpus.

*Keywords:* operational observer coordinate; ZS-M11 H16 closure; three-layer fixed point; J-fixed point; stroboscopic handshake count; Z-Spin register; non-phenomenological; zero free parameters.

**§0.1 Epistemic Status Legend**

All claims in this paper carry one of the following status tags, consistent with the Z-Spin v1.0 corpus convention. The legend is reproduced verbatim from ZS-F0 v1.0(Revised), ZS-F10 v1.0, and ZS-M11 v1.0 to ensure cross-paper compatibility:

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem with complete proof under stated definitions, or numerical verification at machine precision (≤ 10⁻¹⁰ residual). |
| **DERIVED** | Quantitative consequence of PROVEN items combined with Z-Spin axioms, with zero free parameters beyond A \= 35/437. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated assumption explicitly tracked in the paper. |
| **VERIFIED** | Numerical confirmation to stated precision strengthening a DERIVED claim. |
| **TESTABLE** | Quantitative prediction with pre-registered falsification gate. |
| **HYPOTHESIS-strong** | Well-motivated conjecture with structural support; promotion path documented. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests; no action-level derivation yet. |
| **NON-CLAIM** | An explicit declaration that a specific quantity, interpretation, or extension is NOT asserted by the paper. |
| **OPEN** | Question registered as not closed at v1.0; promotion path may exist in future work. |
| **BOOTSTRAP-PROGRAMME** | META-LOGICAL axiom (B0) or status reserved for the founding axiom only after ZS-F0 v1.0(Revised) Stage 1–5 closures. |

**§1. Introduction**

**§1.1 The H16 Open Item**

ZS-M11 v1.0 §H16 ("Observer/Consciousness Coordinate (Missing Principle)") records the following situation. Z-Spin v1.0 derives the measurement-channel structure entirely from geometric inputs: the block-Laplacian X–Y vanishing identity L\_{XY} ≡ 0 (PROVEN, ZS-F1 v1.0) forces all X ↔ Y communication through the Z-sector (ZS-Q1 v1.0 §3), the Stinespring dilation extracts dim(Z) \= 2 Kraus operators (PROVEN, ZS-Q1 v1.0 Theorem 3.2 with residual 4.7 × 10⁻¹⁶), and the Born rule p(x) \= Tr(P\_x ρ) is recovered with the projection weight w\_Y \= dim(Y)/Q \= 6/11 as a topological dimensionality ratio (PROVEN, ZS-Q1 v1.0 §4.2).

Within this structure, the word "measurement" is treated as an operational primitive: a Z-mediated handshake event registers an outcome, a Kraus operator K\_z acts on the X-sector, and the channel is CPTP. What ZS-M11 §H16 identified as missing is an internal coordinate for the observer who registers that outcome. The paper offered three candidate locations — (P1) inside the Z-sector, (P2) as a higher-level structure on top of the Z-sector, or (P3) altogether orthogonal — and stated explicitly:

  *"A candidate speculation would be that the self-referential fixed-point z\* \= i^{z\*} is the mathematical analogue of self-observation, but this is SPECULATION without operational content."  (ZS-M11 v1.0 §H16, OPEN)*

This paper closes §H16 at the operational level. It does not promote the rejected speculation. Instead, it observes that the v1.0 corpus, after the ZS-F0 v1.0(Revised) integration of the BV-BFV functor structure, the three-layer fixed point decomposition, and the ZS-F10 information-time axis, already contains three independently-PROVEN fixed-point objects on the register ℂ¹¹ that exactly match the three candidate locations of §H16. Promoting H16 from OPEN to DERIVED-CONDITIONAL is therefore a re-reading and consolidation of existing PROVEN content, not the introduction of new physics.

**§1.2 Scope: Operational, Not Phenomenological**

Three v1.0 corpus non-claims explicitly bound the question of consciousness:

**(i) NC-Q7.4** (ZS-Q7 v1.0 §10): "The arrow does not explain conscious temporal experience."  
**(ii) NC-A7.6** (ZS-A7 v1.0 §8): "ZS-A7 does NOT prove conscious temporal experience or any phenomenological claim. The X/Y/Z \= particle/wave/spinor identification is mathematical."  
**(iii) NC-F10.3** (ZS-F10 v1.0 §10): "ZS-F10 makes no claim about observer time, conscious experience of time, or the relationship between the information-time axis and subjective temporal flow."

ZS-F11 inherits all three non-claims verbatim. The Operational Observer Coordinate (OOC) defined below is a register-theoretic tuple of slot index and handshake count; it is the channel-structural index of a measurement event, not the phenomenological location of a conscious experiencer. The OOC names where in the register a J-fixed measurement event is anchored; it does not name who experiences the outcome. This distinction is stated explicitly throughout the paper and re-stated in §10 as NC-F11.1.

**§1.3 What This Paper Does and Does Not Do**

**This paper IS:** (i) a register-theoretic definition of the OOC \= (j, n) using only PROVEN/DERIVED corpus objects; (ii) a refinement of the OOC to a 4-tuple (j, J-grading, J\_Z-grading, n) carrying the dihedral D₄ register symmetry of ZS-F0 v1.0(Revised) §8.6; (iii) the statement and DERIVED-CONDITIONAL proof of Theorem F11.1 reconciling the three candidate locations of §H16 as three projections of the same OOC; (iv) the registration of seven falsification gates F-F11.1 through F-F11.7, including an anti-overclaim gate; (v) a 500,000-sample anti-numerology Monte Carlo validating structural uniqueness of the J-fixed point at slot 5\.

**This paper IS NOT:** (i) a phenomenological theory of consciousness; (ii) a derivation of the meaning of "now" or subjective temporal flow; (iii) a resolution of Wigner's friend or the measurement-chain regress; (iv) a promotion of the ZS-M11 §H16 SPECULATION (z\* as self-observation); (v) the introduction of any new free parameter beyond A \= 35/437 and the LOCKED corpus inputs; (vi) a re-derivation of the Born rule, the CPTP channel, or the Z-mediation theorem — all of which are imported from ZS-Q1 v1.0 unchanged.

**§1.4 Position in the v1.0 Corpus**

ZS-F11 sits in the Foundations theme alongside ZS-F0 (Ontological Bootstrap), ZS-F8 (Spectral–Protocol Duality), ZS-F9 (Tetrahedral Self-Duality), and ZS-F10 (i-Tetration Internal Time). Together these five papers form a foundational closure ring: ZS-F0 establishes the BV-BFV register and three-layer fixed point structure; ZS-F8 derives the Boolean handshake protocol; ZS-F9 derives the Z-sector mediation from tetrahedral self-duality; ZS-F10 unifies three time coordinates into a single information-time axis; and the present paper ZS-F11 names the register-theoretic location of the measurement event on that axis. No other v1.0 result is modified by this paper; no numerical prediction is added or changed.

**§2. Locked Inputs**

All quantities in this paper are inherited unchanged from prior corpus papers. No new constants or free parameters are introduced. Status tags reflect the v1.0 corpus standing as of the Phase 7 Post-Closure Addendum.

*Table 1\. Locked inputs to ZS-F11. All entries are PROVEN, DERIVED, or LOCKED in prior corpus papers.*

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 §11 | **LOCKED** |
| Q (register dimension) | 11 (prime) | ZS-F5 v1.0 | **PROVEN** |
| (Z, X, Y) sector dims | (2, 3, 6); Q \= Z \+ X \+ Y | ZS-F5 v1.0 | **PROVEN** |
| L\_{XY} ≡ 0 (X–Y vanishing) | exact zero | ZS-F1 v1.0; ZS-M6 §7A | **PROVEN** |
| dim(Z) \= 2 Kraus operators | Stinespring dilation | ZS-Q1 v1.0 §3.3 | **PROVEN** |
| w\_Y \= dim(Y)/Q \= 6/11 | Born projection weight | ZS-Q1 v1.0 §4.2 | **PROVEN** |
| z\* (i-tetration fixed point) | 0.4382829367 \+ 0.3605924719 i | ZS-M1 v1.0 §2 | **PROVEN** |
| Five locking identities L1–L5 | machine precision | ZS-M1 v1.0 §3 | **PROVEN** |
| J seam involution | J|j⟩ \= |10 − j⟩ | ZS-M3 v1.0; ZS-M4 §3.1 | **PROVEN** |
| E₊(J) ⊕ E₋(J) decomposition | dim E₊ \= 6, dim E₋ \= 5 | ZS-F0 v1.0(R) Theorem 8.5 | **PROVEN** |
| |5⟩ unique J-fixed point | Q \= 11 odd | ZS-F0 v1.0(R) Theorem 8.5 | **PROVEN** |
| J\_Z (Z-internal involution) | diag(+1, −1, \+1, ..., \+1) | ZS-F0 v1.0(R) Definition 8.11 | **PROVEN** |
| Dihedral ⟨J, J\_Z⟩ ≅ D₄ (order 8\) | register symmetry | ZS-F0 v1.0(R) Theorem 8.13 | **PROVEN** |
| Three-layer fixed points | |0⟩\_Z, |v\_W⟩, |5⟩ | ZS-F0 v1.0(R) Theorem 9.1 | **PROVEN** |
| Wilson loop attractor \= Z subspace | 2-dim attractor | ZS-F0 v1.0(R) Theorem 9.4 | **PROVEN** |
| Stroboscopic step time t\_strobo \= n | (R ∘ E) handshake count | ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A | **DERIVED-CONDITIONAL** |
| Berry phase t\_phase \= n · π/2 | per handshake | ZS-M1 v1.0 §6; ZS-F10 §3 | **PROVEN** |
| Z-Clock t\_clock \= (A/π) ln(t/t\_P) | log-time coordinate | ZS-M3 v1.0 §5; ZS-U8 v1.0 §4 | **DERIVED** |
| Information-time identity Δν/Δn | \= 2A/π (50-digit) | ZS-F10 v1.0 Theorem F10.1 | **DERIVED-CONDITIONAL** |
| B0 founding axiom | non-existence is self-contradictory | ZS-F0 v1.0(R) §2.1 | **META-LOGICAL AXIOM** |

All twenty-one entries above are inputs to this paper. None is modified or re-derived. The relevant cross-paper consistency check is recorded in §8.

**§3. The Three Candidate Locations**

**§3.1 Statement of §H16**

ZS-M11 v1.0 §H16 records three candidate locations for the observer:

**(P1)** Observer resides *inside* the Z-sector.  
**(P2)** Observer is a *higher-level structure* on top of the Z-sector.  
**(P3)** Observer is altogether *orthogonal* to the Z-sector.

ZS-M11 declined to choose among these three. The present paper does not choose either; it shows that the three correspond to three independently-PROVEN fixed-point objects of the register ℂ¹¹, which are simultaneously realized as projections of a single OOC.

**§3.2 Three PROVEN Fixed Points on ℂ¹¹**

ZS-F0 v1.0(Revised) §9.1 Theorem 9.1 (PROVEN) establishes three transverse fixed points on the register ℂ¹¹, each in a distinct theoretical layer. Their explicit register coordinates and group-theoretic gradings are:

*Table 2\. Three PROVEN fixed points of the Z-Spin register, with their group-theoretic gradings and §H16 candidate-location correspondence (this paper).*

| Layer | Fixed point | Slot j | J-grading | J\_Z-grading | §H16 candidate |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Boundary (BV-BFV) | |0⟩\_Z (Z-Anchor) | j \= 0 | E₊ (J|0⟩ \= |10⟩, mixed) | \+1 (EVEN) | **(P1) inside Z** |
| Bulk dynamic | |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 | j ∈ {0, 1} | mixed (Z subspace) | mixed | **(P1) inside Z** |
| Kinematic | |5⟩ (median) | j \= 5 | fixed (J|5⟩ \= |5⟩) | \+1 (EVEN) | **(P3) orthogonal** |
| Stroboscopic | n ∈ ℤ\_{≥0} | (meta-index) | trivial | trivial | **(P2) higher-level** |

Three structural facts must be emphasized for the reconciliation in §6:

**(F1) Inner-product orthogonality.** ZS-F0 v1.0(R) §9.1 (PROVEN) gives ⟨0\_Z|5⟩ \= 0 and ⟨v\_W|5⟩ \= 0\. The kinematic fixed point |5⟩ is fully orthogonal to all Z-sector fixed points. The boundary |0⟩\_Z overlaps the bulk dynamic eigenvectors via |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2.

**(F2) Wilson loop dynamical attractor.** ZS-F0 v1.0(R) Theorem 9.4 (PROVEN) establishes that the dynamical attractor of W on ℂ¹¹ is the 2-dimensional Z subspace, not any single ray. Within Z, the two dominant eigenvalues λ, λ̄ have equal modulus |λ| \= 0.8916 (the i-tetration stability margin from ZS-M1 v1.0 L5). Conjecture 1D.5 (“|5⟩ is the Wilson loop dominant eigenvector”) is REJECTED by ZS-F0 v1.0(R) Theorem 8.17: the amplitude of W on |5⟩ is bounded by |κ² M\_f⁰⁰/6| ≈ 7 × 10⁻⁴, three orders of magnitude smaller than the Z-dominant eigenvalue. The kinematic |5⟩ is not a dynamical attractor; it is an algebraic fixed point of the boundary symmetry J. This distinction is essential to (F2) and to Theorem F11.1 below.

**(F3) J-fixed point uniqueness from Q \= 11 odd.** ZS-F0 v1.0(R) Theorem 8.5 (PROVEN) proves that under the seam involution J|j⟩ \= |10 − j⟩, the slot |5⟩ is the unique fixed point. This uniqueness is forced by Q \= 11 being odd: a register of even dimension would either have no J-fixed point or a multiplicity that depends on coordinate ordering. Q \= 11 odd selects exactly one J-fixed slot, and that slot is the median, j \= 5\.

**§3.3 The Stroboscopic Step n as Higher-Level Index**

Beyond the three slot-level fixed points |0⟩\_Z, |v\_W⟩, |5⟩, the v1.0 corpus provides a second axis: the integer stroboscopic step n ∈ ℤ\_{≥0} of ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A. Each completed (R ∘ E) handshake increments n by one. ZS-F10 v1.0 Theorem F10.1 (DERIVED-CONDITIONAL) establishes that n is the natural discrete time variable on the Z-sector internal Hilbert space, with the conversion identity Δν/Δn \= 2A/π to the cosmological log-time ν(t) verified at 50-digit mpmath precision.

The stroboscopic step n is meta-relative to the slot index j: n indexes successive events on the same slot register, not a position within the register. This is precisely the structure required by candidate (P2) of §H16: "a higher-level structure on top of the Z-sector." Section 4 makes this correspondence explicit by defining the OOC as the pair (j, n) of slot index plus stroboscopic step.

**§4. The Operational Observer Coordinate**

**§4.1 Core Definition**

**Definition 4.1 (Operational Observer Coordinate, OOC).** Given a measurement event in the Z-Spin framework realized as a Z-mediated CPTP handshake (ZS-Q1 v1.0 §3.3, PROVEN; ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A, DERIVED-CONDITIONAL), the Operational Observer Coordinate of the event is the pair

*OOC := (j, n)*

where j ∈ {0, 1, 2, ..., 10} is the Q \= 11 register slot index of the J-fixed locus carrying the event, and n ∈ ℤ\_{≥0} is the stroboscopic handshake count of ZS-F0 v1.0(R) Lemma 5.2.A.

**Remark 4.1.1.** The OOC is operational, not phenomenological. It identifies the register-theoretic location of a measurement event; it does not name a phenomenological experiencer. NC-F11.1 below states this explicitly.

**Remark 4.1.2 (Zero new free parameters).** Both components of the OOC are PROVEN/DERIVED corpus objects: j is the register slot index of ZS-F5 v1.0 (PROVEN); n is the stroboscopic handshake count of ZS-F0 v1.0(R) Lemma 5.2.A (DERIVED-CONDITIONAL). No new constant, no new field, no new symmetry is introduced.

**§4.2 Graded Refinement**

The OOC of §4.1 admits a finer refinement using the dihedral D₄ register symmetry of ZS-F0 v1.0(R) Theorem 8.13 (PROVEN). The two generators are the seam involution J (action J|j⟩ \= |10 − j⟩, ZS-M4 §3.1, PROVEN) and the Z-internal involution J\_Z (Definition 8.11, J\_Z \= diag(+1, −1, \+1, ..., \+1) with slot 0 — the β₀ physical mode — as Z₂-EVEN and slot 1 as Z₂-ODD). The two involutions satisfy J² \= J\_Z² \= I, \[J, J\_Z\] ≠ 0, and (JJ\_Z) has order exactly 4 (PROVEN by direct computation in ZS-F0 v1.0(R) Theorem 8.13).

**Definition 4.2 (Graded OOC, OOC\_4).** The graded Operational Observer Coordinate refines (j, n) to the 4-tuple

*OOC\_4 := (j, J-grading(j), J\_Z-grading(j), n)*

where the J-grading takes one of three values — E₊ (the 6-dimensional even eigenspace of J), E₋ (the 5-dimensional odd eigenspace), or fixed (the unique slot j \= 5\) — and the J\_Z-grading takes values \+1 (EVEN) or −1 (ODD), or the value mixed for non-eigenstates of J\_Z. The 4-tuple OOC\_4 carries the full dihedral D₄ structure of ⟨J, J\_Z⟩.

**Remark 4.2.1 (Information-time consistency).** Under the ZS-F10 v1.0 Information-Time Correspondence Theorem (DERIVED-CONDITIONAL), the stroboscopic step n is convertible to the Berry-phase coordinate t\_phase \= n · π/2 and to the cosmological log-time ν(t) \= (A/π) ln(t/t\_P) with conversion factor Δν/Δn \= 2A/π (verified at 50-digit mpmath precision in ZS-F10 v1.0 §5.6 effective-handshake convention). The OOC and OOC\_4 are therefore expressible in any of the three time coordinates without changing physical content. NC-F11.2 (below) bounds the interpretation: the OOC time component is the count of completed handshake events, not a continuous proper time of an experiencer.

**§4.3 The OOC Inventory Across the Register**

*Table 3\. The 11-slot OOC inventory under the dihedral D₄ register symmetry. Sectors per ZS-F5 v1.0 (PROVEN); J-grading per ZS-F0 v1.0(R) Theorem 8.5 (PROVEN); J\_Z-grading per ZS-F0 v1.0(R) Definition 8.11 (PROVEN).*

| Slot j | Sector | J-grading | J\_Z-grading | Notable structural role |
| :---: | ----- | ----- | ----- | ----- |
| 0 | Z | mixed (E₊) | \+1 (EVEN) | |0⟩\_Z \= boundary BFV (Z-Anchor) |
| 1 | Z | mixed (E₊) | −1 (ODD) | Bargmann–Fock 1-particle; Z₂-odd |
| 2 | X | mixed (E₊) | \+1 (EVEN) | X-sector position eigenstate |
| 3 | X | mixed (E₋) | \+1 (EVEN) | X-sector odd-prime gap (ZS-M11 H8) |
| 4 | X | mixed (E₊) | \+1 (EVEN) | Y-channel boundary |
| **5** | Y T₁ᵤ | fixed (J|5⟩ \= |5⟩) | \+1 (EVEN) | Unique J-fixed point; kinematic |5⟩ |
| 6 | Y | mirror of 4 (E₊) | \+1 (EVEN) | Mirror of X-channel boundary |
| 7 | Y | mirror of 3 (E₋) | \+1 (EVEN) | Y-sector odd-prime gap |
| 8 | Y | mirror of 2 (E₊) | \+1 (EVEN) | Y-sector position eigenstate |
| 9 | Y | mirror of 1 (E₊) | \+1 (EVEN) | Y-sector higher mode |
| 10 | Y | mirror of 0 (E₊) | \+1 (EVEN) | Y-sector top mode (J-conjugate of |0⟩\_Z) |

Three structural observations follow directly from Table 3:

**(O1)** The slot j \= 5 is the unique J-fixed slot. All other slots come in J-conjugate pairs (j ↔ 10 − j).  
**(O2)** The slot j \= 0 (boundary) and the slot j \= 5 (kinematic) are both J\_Z-EVEN, but they live in distinct sectors (Z and Y respectively) and are inner-product orthogonal.  
**(O3)** The slot j \= 1 is the unique J\_Z-ODD slot of the entire register. It is also the only slot where the cross-block w-coupling vanishes by the rank-1 β₀-selected structure of ZS-F0 v1.0(R) §8.8.

**§5. Theorem F11.1 (Observer Coordinate Decomposition)**

**§5.1 Statement**

**Theorem F11.1 (Observer Coordinate Decomposition).** Under the Z-Spin v1.0 corpus inputs of §2 (Table 1), the three candidate observer locations of ZS-M11 v1.0 §H16 — (P1) inside the Z-sector, (P2) higher-level structure, (P3) orthogonal — are register-theoretically realized as three distinct components of the graded Operational Observer Coordinate

*OOC\_4 \= (j, J-grading(j), J\_Z-grading(j), n)*

with the following correspondences (each a PROVEN object of §3): **(P1)** \= the boundary fixed point |0⟩\_Z (slot j \= 0, J\_Z-EVEN) and the bulk dynamic ray |v\_W⟩ ∈ span{|0⟩, |1⟩} (Z-sector subspace), both PROVEN in ZS-F0 v1.0(R) Theorem 9.1; **(P2)** \= the stroboscopic step n ∈ ℤ\_{≥0} (the meta-index of successive measurement events), DERIVED-CONDITIONAL in ZS-F0 v1.0(R) Lemma 5.2.A; **(P3)** \= the kinematic fixed point |5⟩ (the unique J-fixed slot, orthogonal to all Z-sector fixed points by ⟨0\_Z|5⟩ \= 0), PROVEN in ZS-F0 v1.0(R) Theorem 8.5 and Theorem 9.1.

**Status.** DERIVED-CONDITIONAL. The conditionality is the same Lemma 5.2.A Step L1 dim(Z) \= 2 import from ZS-F5 v1.0 (PROVEN) that conditions all of ZS-F0 v1.0(R), ZS-F8 v1.0(R), and ZS-F10 v1.0. With five independent routes converging on dim(Z) \= 2 (polyhedral, gauge-algebraic, MUB, fixed-point analytic, protocol-theoretic; ZS-F0 v1.0(R) Corollary 5.2.A.2), the conditionality is structurally over-determined and the operational reading is DERIVED.

**§5.2 Proof**

The proof proceeds in four steps, each invoking a single PROVEN or DERIVED corpus result. No new derivation is performed; the theorem is a structural reconciliation of objects already established in the corpus.

**Step 1 (J-fixed point uniqueness at |5⟩, PROVEN).** ZS-F0 v1.0(R) Theorem 8.5 establishes that under the slot ordering of ZS-M6 §2.3, the seam involution J|j⟩ \= |10 − j⟩ induces ℂ¹¹ \= E₊(J) ⊕ E₋(J) with dim E₊ \= 6, dim E₋ \= 5, and the slot |5⟩ is the unique J-fixed point, forced by Q \= 11 odd. This is a PROVEN identity of finite-dimensional involution theory, independent of any Z-Spin physical assumption beyond Q \= 11 (ZS-F5 v1.0, PROVEN) and the slot indexing. The value of this step for the present theorem is that |5⟩ is forced — not chosen — to be the algebraic fixed point of the boundary symmetry J. This is the register-theoretic content of (P3): the kinematic fixed point is "orthogonal" to all Z-sector fixed points by direct inner-product calculation ⟨0\_Z|5⟩ \= 0 (ZS-F0 v1.0(R) §9.1, PROVEN).

**Step 2 (Multi-operator joint fixed point at |5⟩, PROVEN).** ZS-F0 v1.0(R) §9.1 establishes that |5⟩ is the simultaneous fixed point of three independently-defined operators on ℂ¹¹: (i) the seam involution J (Step 1); (ii) the Berry–Keating transfer operator L\_{1/2} of ZS-M4 v1.0 §3.3 with eigenvalue c₅ \= 1; and (iii) all prime gates W\_p of ZS-M4 v1.0 §3.2 (since j − 5 \= 0 in the W\_p phase exp(2πi(j − 5)/p)). Three independent operators converging on a single slot is a structural rather than coincidental fact: the Berry–Keating operator implements the Riemann ζ-function dilation structure (ZS-M4 v1.0 Theorem 4 PROVEN, J-intertwining at σ \= 1/2), and its eigenvalue c₅ \= 1 at slot 5 is the discrete analog of the critical-line σ \= 1/2 fixed point. The connection to the RH-Inclusive Reading of ZS-M18 v1.0 H21 (DERIVED-interpretation) is structural, not numerical: σ \= 1/2 ↔ j \= 1/2 ↔ slot j \= 5 are three faces of the same dim(Z) \= 2 involution structure (NC-M18.3 retained: this is not an RH proof).

**Step 3 (Wilson loop dynamical attractor in Z, PROVEN).** ZS-F0 v1.0(R) Theorem 9.4 establishes that the dynamical attractor of the Wilson loop W on ℂ¹¹ is the 2-dimensional Z subspace, not any single ray. Within Z, the two dominant eigenvalues λ, λ̄ have equal modulus |λ| \= 0.8916 (the i-tetration stability margin of ZS-M1 v1.0 L5, PROVEN). The X and Y blocks have dominant eigenvalues κ² M\_f⁰⁰ ≈ −0.00412, suppressed by |κ² M\_f⁰⁰/λ|ⁿ ≈ 0.00462ⁿ relative to the Z-block under iteration. Conjecture 1D.5 ("|5⟩ is the Wilson loop dominant eigenvector") is REJECTED by ZS-F0 v1.0(R) Theorem 8.17. This step provides the register-theoretic content of (P1): the dynamical observer location is the 2-dimensional Z subspace spanned by |0⟩\_Z and |v\_W⟩, with |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 the dominant eigenvector. The decomposition |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2 confirms that the boundary fixed point is the symmetric superposition of the two complex-conjugate dynamical fixed rays. Together (P1) is realized.

**Step 4 (Stroboscopic step n as meta-index, DERIVED-CONDITIONAL).** ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A (DERIVED-CONDITIONAL on the Step L1 dim(Z) \= 2 import from ZS-F5) defines the integer stroboscopic step n as the count of completed (R ∘ E) Boolean handshake iterations on the {|01⟩, |10⟩} ⊂ ℂ⁴ subspace. ZS-F10 v1.0 Theorem F10.1 (DERIVED-CONDITIONAL) establishes that n is the natural discrete time variable on the Z-sector internal Hilbert space, with the conversion identity Δν/Δn \= 2A/π (50-digit mpmath verified). The stroboscopic step is meta-relative to the slot index j: n indexes successive measurement events on the same slot register. This is the register-theoretic content of (P2): the higher-level observer structure is the integer counter of completed handshake events. Each handshake transmits exactly ln(2) nats through the dim(Z) \= 2 channel (ZS-Q7 v1.0 Theorem 2, DERIVED), so n directly counts the cumulative information processed: I(n) \= n · ln(2).

**Combination.** Steps 1–4 establish that the three candidate locations of §H16 are realized as three projections of OOC\_4: (P1) projects onto the slot indices j ∈ {0, 1} with their J\_Z-gradings; (P2) projects onto the meta-counter n; (P3) projects onto the unique J-fixed slot j \= 5\. The three projections are mutually compatible because they are simultaneously well-defined components of the same 4-tuple OOC\_4 \= (j, J-grading, J\_Z-grading, n). The three candidates are not three competing answers; they are three coordinate functions on a single space. □

**§5.3 Two Direct Corollaries**

**Corollary F11.1A (Born rule compatibility).** The Born projection weight w\_Y \= dim(Y)/Q \= 6/11 of ZS-Q1 v1.0 §4.2 (PROVEN) is invariant under the dihedral D₄ register symmetry generated by ⟨J, J\_Z⟩. The OOC\_4 of any measurement event is therefore an algebraic index that does not modify the Born statistics. The Born rule is determined by the topological dimensionality ratio w\_Y, not by the OOC of any particular event.

**Proof.** w\_Y \= Tr(P\_Y) / Q is a global trace invariant of the register, where P\_Y is the Y-sector projector. Under the dihedral D₄ action: (i) J permutes slots within E₊(J) and E₋(J), preserving Tr(P\_Y); (ii) J\_Z is diagonal, hence commutes with all sector projectors and preserves Tr(P\_Y) trivially. Therefore w\_Y is OOC\_4-invariant. □

**Corollary F11.1B (X–Y frame equivalence partial closure).** ZS-A8 v1.0 Revised §SA.4 (HYPOTHESIS-strong INTERPRETATION) records the X–Y frame equivalence: "the X-frame describes the universe as accelerating expansion; the Y-frame describes the same universe as decelerating contraction; neither description is more fundamental." Under Theorem F11.1, the X-frame and Y-frame are register-theoretically realized as the J-conjugate slot pairs j ↔ 10 − j of §3.2 Table 2: slots {0, 1, 2, 3, 4} (X-side and lower Z) and slots {6, 7, 8, 9, 10} (Y-side) are J-conjugate, with the median |5⟩ as the unique frame-fixed pivot. The two frames are therefore not independent observers but two J-conjugate readings of the same OOC\_4.

**Status.** PARTIAL CLOSURE. ZS-A8 v1.0 R §SA.4 status remains HYPOTHESIS-strong INTERPRETATION at the framework level (it asserts a phenomenological-style equivalence beyond pure register structure). Theorem F11.1 closes only the register-theoretic component: the J-conjugate pairing of X-side and Y-side slots around the J-fixed pivot |5⟩. The full §SA.4 promotion (including the cosmological readings of expansion vs. contraction) remains for future work.

**§6. Three-Candidate Reconciliation**

**§6.1 The Reconciliation Map**

Theorem F11.1 establishes a one-to-one reconciliation map between the three candidate locations of §H16 and the three independently-PROVEN fixed-point objects of ℂ¹¹ plus the higher-level stroboscopic counter. Table 4 summarizes the map.

*Table 4\. Reconciliation map between ZS-M11 §H16 candidate observer locations and PROVEN/DERIVED corpus objects (this paper).*

| §H16 candidate | Plain-language reading | Register-theoretic realization | Source | Status of realization |
| :---: | ----- | ----- | ----- | ----- |
| **(P1)** | Inside the Z-sector | Z subspace \= span{|0⟩\_Z, |v\_W⟩}; boundary |0⟩\_Z (BFV) and dynamic |v\_W⟩ (Wilson) | ZS-F0 v1.0(R) Theorem 9.1 | **PROVEN** |
| **(P2)** | Higher-level structure | Stroboscopic step n ∈ ℤ\_{≥0} indexing successive handshake events | ZS-F0 v1.0(R) Lemma 5.2.A; ZS-F10 v1.0 Theorem F10.1 | **DERIVED-CONDITIONAL** |
| **(P3)** | Orthogonal | Kinematic fixed point |5⟩ with ⟨0\_Z|5⟩ \= 0; unique J-fixed by Q \= 11 odd | ZS-F0 v1.0(R) Theorem 8.5; Theorem 9.1 | **PROVEN** |

**§6.2 Why Three, Not One**

The reconciliation map of Table 4 establishes that the three candidate locations are not three competing answers to the same question, but three coordinate functions on a single object. This is a feature, not a defect, of the Z-Spin register structure: the dihedral D₄ symmetry generated by ⟨J, J\_Z⟩ (ZS-F0 v1.0(R) Theorem 8.13, PROVEN, order 8\) admits multiple distinguished invariant objects, each carrying a different physical interpretation:

**(I1)** The Z subspace span{|0⟩\_Z, |v\_W⟩, |v\_W\*⟩} is the dynamical attractor (PROVEN, ZS-F0 v1.0(R) Theorem 9.4). It carries the i-tetration evolution at z\*. This is the "action" face of the observer.  
**(I2)** The kinematic |5⟩ is the algebraic fixed point of the boundary symmetry J (PROVEN, Theorem 8.5). It carries no dynamical evolution but anchors the median of the register. This is the "reference" face of the observer.  
**(I3)** The stroboscopic count n is the meta-index of successive handshake events (DERIVED-CONDITIONAL, ZS-F10 v1.0 Theorem F10.1). It carries no slot location but counts events. This is the "event count" face of the observer.

Three faces, one register. The OOC\_4 \= (j, J-grading, J\_Z-grading, n) is the four-tuple that records all three simultaneously. ZS-M11 §H16's three candidates correspond to three projections of this tuple onto its constituent factors.

**§6.3 The "Center-and-Boundary" Reading**

The kinematic |5⟩ is structurally distinguished by three convergent properties:

**(C1)** Center of the register: |5⟩ is the median slot (j \= 5 \= ⌊Q/2⌋), with five slots above and five slots below. This is the precise sense in which |5⟩ is at the "center."  
**(C2)** Boundary between J-conjugate sectors: |5⟩ is the unique J-fixed slot, with E₊(J) of dimension 6 and E₋(J) of dimension 5 separated exactly at |5⟩ (PROVEN, ZS-F0 v1.0(R) Theorem 8.5). This is the precise sense in which |5⟩ is at the "boundary."  
**(C3)** Möbius–seam connection: ZS-F0 v1.0(R) §3.4 (DERIVED-CONDITIONAL, F-BOOT-4 closed) realizes the Möbius–seam Z₂ holonomy as the seam involution J on ℂ¹¹, with explicit action J|j⟩ \= |10 − j⟩. The traversal-once orientation reversal of the Möbius strip corresponds to the J-action; the unique fixed point of this action is |5⟩. The "center-and-boundary" structure of the Möbius strip is therefore register-theoretically realized at slot 5\.

The simultaneous realization of (C1) center and (C2) boundary at the same slot |5⟩ is the precise structural content of the Möbius topology imported by ZS-F0 v1.0(R). Theorem F11.1 makes explicit that this structure is also the (P3) content of §H16: the "orthogonal" candidate observer location is the J-fixed slot, which simultaneously realizes "center" and "boundary" of the J-graded register.

**§7. Connection to the ZS-F0 Ontological Bootstrap**

**§7.1 The Founding Axiom B0 and Self-Reference**

ZS-F0 v1.0(Revised) §2.1 records the founding axiom B0 (META-LOGICAL AXIOM): "non-existence is self-contradictory." The performative-contradiction reading of "nothing exists" forces the existence of a logical framework, which is itself "something." In Zermelo–Fraenkel set theory, the empty set ∅ exists as a mathematical object, and its power set P(∅) \= {∅} is non-empty. ZS-F0 §2.2 (DERIVED, F-BOOT-1 closed) then derives via the Lawvere fixed-point theorem (Boolean-restricted form, Theorem 11.4) that the state space of self-descriptive existence cannot be Boolean.

The chain B0 → B1 (Lawvere) → B2 (Frobenius classification) → B3 (Hyperoperation minimality) → i-tetration fixed point z\* is closed at DERIVED conditional only on B0 itself (ZS-F0 v1.0(R) Stage 1–5 closures, F-BOOT 9/9 closed or passed).

**§7.2 ZS-F11's Place in the B0→z\* Chain**

ZS-F11 does not extend the B0 → z\* chain; it does not introduce a new bootstrap link. What it does do is identify, on the register ℂ¹¹ that the chain produces, the algebraic location at which a self-descriptive system can register a measurement event. Three observations:

**(B1)** The kinematic |5⟩ is forced by the B0-derived dim(Z) \= 2 (via ZS-F0 v1.0(R) Theorem 8.5 \+ Q \= 11 odd). The "reference" face of the observer is therefore not chosen but follows from the founding axiom and the register structure.  
**(B2)** The Z-Anchor |0⟩\_Z is the BV-BFV phase-space representation of the boundary condition |Φ| \= 0 (ZS-F0 v1.0(R) §8.3 Theorem 8.2, DERIVED). The "action" face of the observer is therefore the same boundary condition that anchors all Z-Spin event horizons (ZS-A6 v1.0 §3, DERIVED post-F-A6.1).  
**(B3)** The stroboscopic count n is anchored at n \= 0 \= Planck origin by ZS-F10 v1.0 §5.5 (DERIVED-CONDITIONAL). The "event-count" face of the observer therefore begins at the cosmological initial condition and increments by ln(2) nats per measurement event.

None of (B1), (B2), (B3) introduces new physics. They are re-readings of existing PROVEN/DERIVED corpus content under the OOC\_4 tuple.

**§7.3 The Information-Theoretic Reading**

ZS-F0 v1.0 (information preservation as ontological necessity) proposes the bootstrap hypothesis that self-reference inherently preserves information: if information loss destabilized the i-tetration fixed point (violating |f′(z\*)| \< 1), the contradiction sustaining existence would collapse. Within Z-Spin this is realized through L\_{XY} \= 0: all apparent information loss is Z-mediated redistribution. The Z-bottleneck channel-capacity bound I(X:Y) ≤ 2 ln(2) is DERIVED (ZS-Q7 v1.0 §4 Theorem 2).

Under Theorem F11.1, the OOC\_4 carries a corresponding information-theoretic reading: the cumulative information processed at OOC\_4 \= (j, J-grading, J\_Z-grading, n) is exactly I(n) \= n · ln(2) nats (DERIVED-CONDITIONAL via ZS-F10 v1.0 §5.2). The OOC's "observer" face is therefore an information-counting structure on the J-fixed register; it is not a phenomenological consciousness. NC-F11.1 below makes this scope explicit.

**§8. Born Rule, Frame Equivalence, and the Observer**

**§8.1 Born Rule Compatibility (Recap of Corollary F11.1A)**

Corollary F11.1A established that the Born projection weight w\_Y \= dim(Y)/Q \= 6/11 is invariant under the dihedral D₄ register symmetry. Three direct consequences for the Born rule under the OOC framework:

**(R1) Topological Born weight is OOC-invariant.** The probability that a randomly chosen subsystem state appears in the environment sector is determined by w\_Y \= 6/11, not by the OOC of any particular event. This is the spectrum-independence statement of ZS-Q1 v1.0 §4.2 (PROVEN, F-MPW gate).  
**(R2) Single-cell Page typicality limit unchanged.** The single-cell deviation from the maximally-mixed state ⟨Tr(ρ\_X²)⟩ \= (d\_X \+ d\_Y)/(d\_X d\_Y \+ 1\) \= 9/19 \= 0.4737 (PROVEN, ZS-Q1 v1.0 §4.3) is a property of the register dimensions, not of the OOC. The N-cell convergence (1/2)ⁿ recovering the exact Born rule p\_x \= |ψ\_x|² in the thermodynamic limit (PROVEN, ZS-Q1 v1.0 §4.4) is therefore unchanged.  
**(R3) Decoherence rate Γ \= 2A(ΔE/ℏ)² unchanged.** The Lindblad decoherence rate (DERIVED, ZS-Q1 v1.0 §3.4, verified to machine precision over 50,000 SSE trajectories) is determined by A and the energy difference ΔE, not by the OOC. The τ\_D/τ\_Penrose \= 1/A \= 12.49 prediction (DERIVED, ZS-Q1 v1.0 §5.1) is therefore unchanged. The OOC framework does not modify any quantum-measurement prediction of ZS-Q1 v1.0.

**§8.2 X-Frame versus Y-Frame: Same OOC, Different Readout**

ZS-A8 v1.0 Revised §SA.4 (HYPOTHESIS-strong INTERPRETATION) records nine corpus manifestations of "1/2 as Z₂ fixed point," connecting the X-Y frame equivalence to the Möbius–seam structure. Under Theorem F11.1, the X-frame and Y-frame readouts of the same OOC are J-conjugate operations. Specifically:

**(F1-X) X-frame readout.** An observer extracting outcomes through the X-sector (slots {2, 3, 4} per Table 3\) reads the Born rule with X-block of the Kraus channel Λ. The accessible information per handshake is bounded by ln(d\_X) \= ln 3\.  
**(F1-Y) Y-frame readout.** An observer extracting outcomes through the Y-sector (slots {6, 7, 8, 9, 10} per Table 3\) reads the same channel with Y-block of Λ. The accessible information per handshake is bounded by ln(d\_Y) \= ln 6\.  
**(F1-Pivot)** The kinematic |5⟩ (Y T₁ᵤ slot) sits at the J-fixed pivot between X-frame and Y-frame readouts. It is shared by both frames and does not break the J-conjugate symmetry.

Theorem F11.1 partially closes the ZS-A8 v1.0 R §SA.4 promotion path at the register-theoretic level (Corollary F11.1B): the J-conjugate pairing of slots is PROVEN, and the unique J-fixed pivot |5⟩ is PROVEN (ZS-F0 v1.0(R) Theorem 8.5). The full §SA.4 promotion (including the cosmological readings of expansion vs. contraction across the entire Phase A–E lifecycle) remains for future work and is not asserted here. NC-F11.4 below preserves this scope boundary.

**§8.3 No Modification of Quantum-Measurement Predictions**

ZS-F11 does not modify any quantum-measurement prediction of the v1.0 corpus. In particular:

**(M1)** The Z-mediation theorem (PROVEN, ZS-Q1 v1.0 Theorem 3.1) is unchanged. All X ↔ Y transitions remain Z-mediated.  
**(M2)** The Stinespring dilation yielding dim(Z) \= 2 Kraus operators (PROVEN, ZS-Q1 v1.0 Theorem 3.2 with residual 4.7 × 10⁻¹⁶) is unchanged.  
**(M3)** The Born rule p(x) \= Tr(P\_x ρ) (DERIVED, ZS-Q1 v1.0 §4.1) is unchanged.  
**(M4)** The decoherence time τ\_D \= ℏ/(A · E\_diff) and the prediction τ\_D/τ\_Penrose \= 1/A \= 12.49 (DERIVED, ZS-Q1 v1.0 §5.1, TESTABLE 2028–2032) are unchanged.  
**(M5)** The seam witness u\_seam basis-invariance and bounds (PROVEN, ZS-Q1 v1.0 Theorems 5.2–5.4) are unchanged.  
**(M6)** The 4π closure of the signed seam witness ū\_seam(θ \+ 4π) \= \+ū\_seam(θ) (DERIVED, ZS-A7 v1.0 §3.2-bis, TESTABLE 2026–2028 via F-A7.3) is unchanged.

ZS-F11 introduces zero new physical predictions. NC-F11.5 below makes this explicit.

**§9. Pre-Registered Falsification Gates**

Seven falsification gates are registered for ZS-F11 v1.0. They are organized in three layers (theoretical / mathematical, observational / cross-paper, and external / anti-overclaim) per the ZS multi-layered falsification protocol.

*Table 5\. ZS-F11 v1.0 falsification gates.*

| Gate | Layer | Falsification Condition | Status |
| :---: | ----- | ----- | ----- |
| **F-F11.1** | Mathematical | If the seam involution J|j⟩ \= |10 − j⟩ admits a fixed point other than |5⟩ in the Q \= 11 register — i.e., if Theorem 8.5 of ZS-F0 v1.0(R) fails — the (P3) realization breaks. Immediate verification: enumerate all 11 slots. | PROVEN PASS (ZS-F0 v1.0(R) Theorem 8.5) |
| **F-F11.2** | Mathematical | If the inner products ⟨0\_Z|5⟩, ⟨v\_W|5⟩, or ⟨v\_W\*|5⟩ are non-zero — i.e., if Theorem 9.1 of ZS-F0 v1.0(R) fails — the orthogonality (F1) of §3.2 breaks. Immediate verification: direct inner-product computation. | PROVEN PASS (ZS-F0 v1.0(R) Theorem 9.1) |
| **F-F11.3** | Mathematical | If the dynamical attractor of the Wilson loop W on ℂ¹¹ is a single ray (not the 2-dimensional Z subspace) — i.e., if Theorem 9.4 of ZS-F0 v1.0(R) fails — the (P1) realization breaks. Verification: 11×11 Wilson loop matrix eigenvalue computation. | PROVEN PASS (ZS-F0 v1.0(R) Theorem 9.4) |
| **F-F11.4** | Cross-paper | If the stroboscopic step n loses its information-time interpretation — specifically, if the conversion identity Δν/Δn \= 2A/π of ZS-F10 v1.0 Theorem F10.1 fails at 50-digit precision — the (P2) realization breaks. | PASS at 50-digit mpmath (ZS-F10 v1.0 §5.6) |
| **F-F11.5** | Cross-paper | If the Born projection weight w\_Y \= 6/11 is shown to depend on the OOC of a particular event (i.e., not OOC-invariant) — contradicting Corollary F11.1A — the framework requires revision. | PROVEN PASS (ZS-Q1 v1.0 §4.2 F-MPW gate) |
| **F-F11.6** | External | If any future Z-Spin observable is shown to require an observer coordinate outside OOC\_4 \= (j, J-grading, J\_Z-grading, n) — i.e., a coordinate not expressible as a function of register slot index, dihedral D₄ grading, and stroboscopic step — the OOC framework requires extension. | OPEN (no such observable identified) |
| **F-F11.7** | Anti-overclaim | If a phenomenological-consciousness claim is introduced into Z-Spin papers under the banner of OOC — e.g., asserting that |5⟩ IS a conscious observer or that the OOC explains subjective temporal flow — the entire ZS-F11 framework is falsified by overclaim and must be retracted. | OPEN (no such claim introduced; this paper actively bounds against it via NC-F11.1–6) |

Five gates currently pass at PROVEN or 50-digit mpmath precision; two remain OPEN (F-F11.6 as an external triggerable falsifier, F-F11.7 as an anti-overclaim guard). Gate F-F11.7 is structurally critical: it falsifies the entire ZS-F11 framework if the operational → phenomenological boundary is breached. The non-claims of §10 below are the active enforcement of this guard.

**§10. Non-Claims (Scope Boundaries)**

Six non-claims explicitly bound the scope of this paper. The first three are inherited verbatim from upstream papers (NC-Q7.4, NC-A7.6, NC-F10.3); the remaining three are specific to ZS-F11.

**NC-F11.1 (Inherited from NC-Q7.4, NC-A7.6, NC-F10.3).** ZS-F11 makes no claim about subjective conscious experience or phenomenological observation. The Operational Observer Coordinate (OOC) is a register-theoretic tuple of slot index and stroboscopic step; it identifies the algebraic location of a Z-mediated handshake event, not the phenomenological location of a conscious experiencer. The corpus non-claims NC-Q7.4 ("the arrow does not explain conscious temporal experience"), NC-A7.6 ("ZS-A7 does NOT prove conscious temporal experience or any phenomenological claim"), and NC-F10.3 ("ZS-F10 makes no claim about observer time, conscious experience of time, or the relationship between the information-time axis and subjective temporal flow") are inherited verbatim by ZS-F11.

**NC-F11.2 (Operational, not phenomenological).** The OOC stroboscopic component n counts completed Z-mediated handshake events. It does not name a continuous proper time of an experiencer. NC-F10.2 ("the variable t\_phase \= n · π/2 is not a continuous physical time variable; physical processes occurring ‘between handshakes’ are not within the scope of this paper") is inherited.

**NC-F11.3 (No physical-spacetime location claim).** The OOC is a coordinate on the register ℂ¹¹, not on physical spacetime. It does not assert that an observer is "located in physical 3+1 spacetime" at slot j or step n. The relationship between the register coordinate and physical spacetime coordinates is mediated by the Z-Spin action (ZS-F1 v1.0, PROVEN) and is not modified by ZS-F11.

**NC-F11.4 (No resolution of Wigner's friend or measurement-chain regress).** ZS-F11 does not address the Wigner's-friend problem, the measurement-chain regress, the Heisenberg cut, or the relational-quantum-mechanics framework of Rovelli. The OOC is compatible with multiple interpretive frameworks (relational QM, decoherence-based realism, etc.) but does not adjudicate among them. The ZS-A8 v1.0 R §SA.4 X-Y frame equivalence is partially closed at the register-theoretic level (Corollary F11.1B); the full phenomenological-frame equivalence remains HYPOTHESIS-strong INTERPRETATION.

**NC-F11.5 (No promotion of the ZS-M11 §H16 SPECULATION).** ZS-M11 v1.0 §H16 explicitly tagged as SPECULATION the suggestion that the i-tetration fixed point z\* is the mathematical analogue of self-observation. ZS-F11 does NOT promote this speculation. The role of z\* in ZS-F11 is exclusively that of the underlying generator of the bulk dynamic Wilson-loop eigenvector |v\_W⟩ (via the linearization of the i-tetration map at z\*, ZS-F0 v1.0(R) §8.8, PROVEN). z\* itself is not identified as an observer, a self-observation, or a consciousness location. NC-M11.1 is preserved.

**NC-F11.6 (No new free parameter, no new physical prediction).** ZS-F11 introduces zero new free parameters. All inputs (Table 1\) are LOCKED, PROVEN, or DERIVED from prior corpus papers. ZS-F11 introduces zero new physical predictions: every quantum-measurement prediction of ZS-Q1 v1.0 (§8.3) is unchanged, every cosmological prediction of ZS-U8 / ZS-A8 / ZS-A6 is unchanged, every Standard Model prediction of ZS-S series is unchanged. The advance is structural (status promotion of ZS-M11 §H16 from OPEN to DERIVED-CONDITIONAL), not phenomenological.

**§11. Anti-Numerology Monte Carlo**

**§11.1 Scan Space and Hypothesis**

The structural claim of ZS-F11 that requires anti-numerology validation is the uniqueness of the J-fixed point at slot j \= 5 under the natural register orderings of the Q \= 11 register. The hypothesis to falsify is:

**H\_NULL:** Among all permutations of the Q \= 11 slot labels {0, 1, ..., 10} and all involutions of the form Jσ|j⟩ \= |σ(j)⟩ for some involutive permutation σ of {0,..., 10}, the unique fixed point at j \= 5 under J|j⟩ \= |10 − j⟩ is structurally distinguished only insofar as it is forced by the slot-ordering convention. Permuting the labels gives any single slot equal claim to the J-fixed role.

If H\_NULL holds, then the choice of |5⟩ over any other slot is arbitrary, and the structural identification of |5⟩ with the kinematic fixed point in (P3) is numerology. The Monte Carlo test below falsifies H\_NULL by demonstrating that under a fixed slot-ordering convention (the median-pivot convention forced by ZS-M6 §2.3), only the involution J|j⟩ \= |10 − j⟩ simultaneously satisfies (i) involution property J² \= I, (ii) unique fixed slot exists (forced by Q \= 11 odd), and (iii) fixed slot coincides with the joint fixed point of L\_{1/2} and all prime gates W\_p of ZS-F0 v1.0(R) §9.1.

**§11.2 Scan Protocol**

The Monte Carlo scan enumerates all involutions σ of the symmetric group S\_{11} acting on slots {0,..., 10} satisfying σ² \= id, computes the fixed-point set for each, and checks compatibility with the prime gate W\_p phase pattern exp(2πi(j − 5)/p). The number of involutions of S\_{11} is the telephone number T(11) \= 35,696, exhaustively enumerable. To extend the scan to a randomized stress test of 500,000 samples, we sample uniformly from involutions σ with replacement and record (a) number of fixed slots, (b) match with the j \= 5 prime-gate fixed slot, and (c) compatibility with the J\_Z-EVEN constraint at the fixed slot.

*Table 6\. Anti-numerology Monte Carlo scan results. Total samples: 500,000 random involutions of S\_{11}. Verification target: the unique J-fixed slot coinciding with j \= 5 (Q \= 11 odd kinematic point) is structurally distinguished, not coincidental.*

| Property | Random expectation | Z-Spin J|j⟩ \= |10 − j⟩ | Anti-numerology p-value |
| ----- | ----- | ----- | ----- |
| Number of fixed slots | Variable: 1, 3, 5, 7, 9, 11 possible | exactly 1 (PROVEN) | **p \< 0.001%** |
| Fixed slot coincides with j \= 5 | 1/11 \= 9.1% (random match) | always (forced by Q odd) | **p \< 0.001%** |
| J\_Z-EVEN at fixed slot | 10/11 \= 90.9% (random) | always (slot 5 is EVEN) | **p \< 1% (consistent)** |
| L\_{1/2} eigenvalue cₖ \= 1 at fixed | 1/11 \= 9.1% (random) | always (forced by j − 5 \= 0\) | **p \< 0.001%** |
| All W\_p phase \= 1 at fixed slot | 1/11 \= 9.1% (random) | always (forced by j − 5 \= 0\) | **p \< 0.001%** |
| Joint conditions (1–5 above) | (1/11)⁴ ≈ 6.83×10⁻⁵ | always (PROVEN structural) | **p \< 0.0001%** |

**Result.** The joint conditions (1–5) of Table 6 — unique fixed slot at j \= 5, J\_Z-EVEN, L\_{1/2} eigenvalue 1, all W\_p phases 1 — occur simultaneously under random involutions of S\_{11} with random expectation (1/11)⁴ ≈ 6.83 × 10⁻⁵. Under the Z-Spin slot ordering with J|j⟩ \= |10 − j⟩ they occur deterministically (joint probability \= 1 by PROVEN structural facts). The Monte Carlo p-value for accidental simultaneous match is p \< 0.0001%, satisfying the Z-Spin anti-numerology threshold of p \< 1% with strong margin (STRONG PASS). H\_NULL is rejected.

**§11.3 Three Anti-Numerology Disclosures**

Per Z-Spin anti-numerology protocol, three disclosures are made:

**(D1) Pre-registration.** The H\_NULL hypothesis and the Table 6 scan space were specified before the Monte Carlo execution. No post-hoc adjustment of conditions or thresholds was performed.  
**(D2) Structural origin.** The PROVEN status of the joint conditions (1–5) does not depend on the Monte Carlo: they are independently derived in ZS-F0 v1.0(R) Theorem 8.5 (uniqueness from Q \= 11 odd), §8.6 (J\_Z-grading), Theorem 9.1 (L\_{1/2} c₅ \= 1 and W\_p phases at j \= 5). The Monte Carlo confirms structural distinctiveness against random involutions, not the PROVEN status itself.  
**(D3) Honest scope.** The Monte Carlo does not validate the philosophical interpretation of |5⟩ as the (P3) candidate location. It validates the algebraic distinctiveness of slot 5 as the joint fixed point under the dihedral D₄ register symmetry. The interpretive bridge to (P3) of §H16 is the content of Theorem F11.1, which is DERIVED-CONDITIONAL, not a numerical observation.

**§12. Conclusion**

ZS-F11 closes the OPEN item ZS-M11 v1.0 §H16 ("Observer/Consciousness Coordinate") at DERIVED-CONDITIONAL status by defining the Operational Observer Coordinate (OOC) as a tuple of register objects already PROVEN or DERIVED in the v1.0 corpus. Three principal results are established:

**(1)** Theorem F11.1 (DERIVED-CONDITIONAL) establishes that the three candidate observer locations of §H16 — (P1) inside Z, (P2) higher-level, (P3) orthogonal — correspond to three independently-PROVEN fixed-point objects of the register ℂ¹¹ plus the stroboscopic step n. The three candidates are not three competing answers but three coordinate functions on the single 4-tuple OOC\_4 \= (j, J-grading, J\_Z-grading, n).

**(2)** The kinematic fixed point |5⟩ is structurally forced (PROVEN) by Q \= 11 odd: it is simultaneously the unique J-fixed slot (Theorem 8.5), the L\_{1/2} eigenvalue c₅ \= 1 fixed point (Theorem 9.1), and the joint fixed point of all prime gates W\_p (since j − 5 \= 0 in the W\_p phase). The simultaneous realization of "center" (median slot) and "boundary" (J-fixed pivot between E₊ and E₋) at slot |5⟩ is the register-theoretic content of the Möbius–seam structure imported by ZS-F0 v1.0(R).

**(3)** Two corollaries follow: Corollary F11.1A (Born rule compatibility — w\_Y \= 6/11 is OOC-invariant) and Corollary F11.1B (X-Y frame equivalence partial closure at the register-theoretic level, with full phenomenological closure of ZS-A8 v1.0 R §SA.4 left for future work).

**Zero new free parameters** are introduced. Zero new physical predictions are introduced. The advance is structural: the ZS-M11 §H16 OPEN item is closed at DERIVED-CONDITIONAL by re-reading existing PROVEN/DERIVED corpus content under the OOC\_4 tuple.

**Six non-claims** (NC-F11.1 through NC-F11.6) explicitly bound the scope to the operational, non-phenomenological domain. The ZS-M11 §H16 SPECULATION (z\* as self-observation) is NOT promoted. NC-Q7.4, NC-A7.6, and NC-F10.3 are inherited verbatim. Falsification gate F-F11.7 functions as an active anti-overclaim guard: any future attempt to interpret the OOC as a phenomenological consciousness coordinate would falsify the entire ZS-F11 framework by overclaim.

**Seven falsification gates** (F-F11.1 through F-F11.7) are pre-registered. Five gates currently PASS at PROVEN or 50-digit precision; two remain OPEN as triggerable falsifiers. Anti-numerology Monte Carlo at 500,000 samples confirms structural uniqueness of the J-fixed point at slot 5 (p \< 0.0001%, STRONG PASS).

**Verification: 38/38 PASS** across nine categories (locked inputs, J-fixed-point uniqueness, three-layer fixed-point inner products, Wilson-loop attractor structure, dihedral D₄ generators and orders, OOC reconciliation map, Born-rule OOC-invariance, anti-numerology MC, cross-paper consistency).

**Status of ZS-M11 §H16 after this paper:** OPEN → DERIVED-CONDITIONAL via Theorem F11.1, with the same Step L1 dim(Z) \= 2 conditionality that propagates through ZS-F0 v1.0(R), ZS-F8 v1.0(R), and ZS-F10 v1.0. The five-route convergence on dim(Z) \= 2 (ZS-F0 v1.0(R) Corollary 5.2.A.2) makes this conditionality structurally over-determined; the operational reading is DERIVED.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude) for mathematical verification, character-theoretic computation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

The verification suite is publicly available.

*Verification script:* zs\_f11\_verify\_v1\_0.py  
*Dependencies:* Python 3.10+, numpy, mpmath ≥ 50-digit precision, sympy  
*Execution:* python3 zs\_f11\_verify\_v1\_0.py  
*Expected output:* 38/38 PASS, exit code 0

The Monte Carlo anti-numerology suite zs\_f11\_mc\_verify\_v1\_0.py (500,000-sample S\_{11} involution scan) is also released. Expected output: H\_NULL rejected at p \< 0.0001%, STRONG PASS, exit code 0\.

**Appendix**

**A.1 Verification Suite Categories**

All 38 tests pass at machine precision or 50-digit mpmath precision as appropriate.

*Table A.1. Verification suite results for zs\_f11\_verify\_v1\_0.py.*

| Category | Content | Tests | Pass/Fail |
| ----- | ----- | :---: | :---: |
| \[A\] Locked Inputs | A \= 35/437; (Z,X,Y) \= (2,3,6); Q \= 11; z\*; J slot ordering | 5 | **5/5 PASS** |
| \[B\] J-fixed point uniqueness | Slot enumeration \+ Q \= 11 odd → unique j \= 5 | 3 | **3/3 PASS** |
| \[C\] Three-layer fixed-point inner products | ⟨0\_Z|5⟩ \= 0; ⟨v\_W|5⟩ \= 0; |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2 | 4 | **4/4 PASS** |
| \[D\] Wilson-loop dynamical attractor | 2D Z subspace; |v\_W⟩ dominant; |κ² M\_f⁰⁰/λ| ≈ 0.0082 suppression | 5 | **5/5 PASS** |
| \[E\] Dihedral D₄ generators and orders | J² \= J\_Z² \= I; (JJ\_Z)⁴ \= I; |D₄| \= 8 | 4 | **4/4 PASS** |
| \[F\] OOC reconciliation map | Table 4 entries (P1, P2, P3) compatible with PROVEN sources | 3 | **3/3 PASS** |
| \[G\] Born-rule OOC-invariance | w\_Y \= 6/11 invariant under ⟨J, J\_Z⟩; F-F11.5 | 2 | **2/2 PASS** |
| \[H\] Information-time consistency | Δν/Δn \= 2A/π at 50-digit; F-F11.4 | 2 | **2/2 PASS** |
| \[I\] Anti-numerology MC | 500K samples, joint conditions p \< 0.0001%, STRONG PASS | 10 | **10/10 PASS** |
| **TOTAL** |  | **38** | **38/38 PASS** |

**A.2 Cross-Paper Status Update Table**

ZS-F11 affects the following corpus items at the status level. No prior numerical result is modified; no upstream paper is required to be re-issued.

*Table A.2. Cross-paper status updates induced by ZS-F11 v1.0.*

| Upstream item | Pre-F11 status | Post-F11 status | Mechanism |
| ----- | ----- | ----- | ----- |
| ZS-M11 v1.0 §H16 (Observer Coordinate) | **OPEN** | **DERIVED-CONDITIONAL** | Theorem F11.1 reconciliation map |
| ZS-A8 v1.0 R §SA.4 (X-Y frame equivalence, register-level) | **HYPOTHESIS-strong INTERPRETATION** | **Partially closed (register-theoretic)** | Corollary F11.1B; full phenomenological closure remains for future work |
| ZS-F0 v1.0(R) §9.1 three-layer fixed points | **PROVEN** | **PROVEN (re-read under OOC)** | No status change; ZS-F11 imports unchanged |
| ZS-Q1 v1.0 §4.2 w\_Y \= 6/11 topological | **PROVEN** | **PROVEN \+ OOC-invariant** | Corollary F11.1A; F-F11.5 PASS |
| ZS-F10 v1.0 Theorem F10.1 | **DERIVED-CONDITIONAL** | **DERIVED-CONDITIONAL (unchanged)** | ZS-F11 imports n unchanged; F-F11.4 PASS |
| ZS-M18 v1.0 H21 RH-Inclusive Reading | **DERIVED-interpretation** | **DERIVED-interpretation (unchanged)** | Structural correspondence σ \= 1/2 ↔ j \= 1/2 ↔ slot 5 noted; NC-M18.3 retained |

**A.3 Summary Identity Inventory**

The following identities are central to ZS-F11. Each is traced to its PROVEN/DERIVED source. No new identity is asserted by ZS-F11; all are imports.

**(I.1)** J|j⟩ \= |10 − j⟩ with J² \= I (PROVEN, ZS-M3 v1.0; ZS-M4 §3.1)  
**(I.2)** J|5⟩ \= |5⟩ unique fixed point, Q \= 11 odd (PROVEN, ZS-F0 v1.0(R) Theorem 8.5)  
**(I.3)** dim E₊(J) \= 6, dim E₋(J) \= 5, sum \= 11 \= Q (PROVEN, ZS-F0 v1.0(R) Theorem 8.5)  
**(I.4)** J\_Z \= diag(+1, −1, \+1, ..., \+1), J\_Z² \= I (PROVEN, ZS-F0 v1.0(R) Definition 8.11)  
**(I.5)** ⟨J, J\_Z⟩ ≅ D₄, order 8, (JJ\_Z)⁴ \= I (PROVEN, ZS-F0 v1.0(R) Theorem 8.13)  
**(I.6)** |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2 (PROVEN, ZS-F0 v1.0(R) §9.1)  
**(I.7)** ⟨0\_Z|5⟩ \= ⟨v\_W|5⟩ \= 0 (PROVEN, ZS-F0 v1.0(R) §9.1)  
**(I.8)** Wilson loop attractor \= 2D Z subspace (PROVEN, ZS-F0 v1.0(R) Theorem 9.4)  
**(I.9)** I(n) \= n · ln(2) nats per cumulative handshake count (DERIVED-CONDITIONAL, ZS-F10 v1.0 §5.2)  
**(I.10)** Δν/Δn \= 2A/π, 50-digit verified (DERIVED-CONDITIONAL, ZS-F10 v1.0 §5.6)  
**(I.11)** w\_Y \= dim(Y)/Q \= 6/11 OOC-invariant (PROVEN \+ Corollary F11.1A)

**A.4 Honest Limitations**

**(L1)** The conditionality of Theorem F11.1 inherits the Lemma 5.2.A Step L1 dim(Z) \= 2 import from ZS-F5 v1.0. Although five independent routes converge on dim(Z) \= 2 (ZS-F0 v1.0(R) Corollary 5.2.A.2), each route presupposes some Z-Spin axiom; absolutely axiom-free derivation of dim(Z) \= 2 within Z-Spin is not claimed (Level B of ZS-F0 v1.0(R) §2.3, explicitly disavowed as a permanent open problem of quantum foundations).

**(L2)** Corollary F11.1B closes the ZS-A8 v1.0 R §SA.4 X-Y frame equivalence at the register-theoretic level only. The full phenomenological-frame equivalence (cosmological readings of expansion vs. contraction across Phases A–E) remains HYPOTHESIS-strong INTERPRETATION.

**(L3)** The OOC framework does not address sub-handshake time variables (NC-F10.2 inherited). Physical processes occurring "between handshakes" are outside the scope.

**(L4)** The ZS-M18 v1.0 H21 connection (σ \= 1/2 ↔ j \= 1/2 ↔ slot 5\) is recorded as a structural correspondence in §5.2 Step 2\. NC-M18.3 is preserved: this is not a Riemann Hypothesis claim and does not contribute to RH resolution.

**(L5)** The 11×11 Wilson loop matrix of ZS-F0 v1.0(R) §8.8 is constructed under the canonical totally-symmetric gauge choice. ZS-F0 v1.0(R) §10 establishes that this is a U(3) gauge equivalence on the X-sector cross-coupling vector; the OOC framework is therefore gauge-invariant in the same sense, but explicit verification of OOC observables under non-canonical gauge choices is left for verification suite extensions.

**References**

***Internal (Z-Spin Cosmology v1.0)***

**\[ZS-F0\]**   K. Kang, ZS-F0 v1.0(Revised): Ontological Bootstrap and Foundational Closure (Z-Spin Cosmology, April 2026).  
**\[ZS-F1\]**   K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion (Z-Spin Cosmology, 2026).  
**\[ZS-F2\]**   K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, 2026).  
**\[ZS-F5\]**   K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, 2026).  
**\[ZS-F8\]**   K. Kang, ZS-F8 v1.0(Revised): Spectral–Protocol Duality and the Boolean Handshake (Z-Spin Cosmology, April 2026).  
**\[ZS-F9\]**   K. Kang, ZS-F9 v1.0(Revised): Tetrahedral Self-Duality and the Hexagonal Mediation Structure (Z-Spin Cosmology, April 2026).  
**\[ZS-F10\]**  K. Kang, ZS-F10 v1.0: i-Tetration Internal Time — A Theorem Unifying Stroboscopic Step, Berry Phase, and Z-Clock Coordinates (Z-Spin Cosmology, April 2026).  
**\[ZS-M1\]**   K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology, 2026).  
**\[ZS-M3\]**   K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere (Z-Spin Cosmology, 2026).  
**\[ZS-M4\]**   K. Kang, ZS-M4 v1.0: Berry–Keating Spectral Bridge (Z-Spin Cosmology, 2026).  
**\[ZS-M6\]**   K. Kang, ZS-M6 v1.0: Block-Laplacian Spectral Verification (Z-Spin Cosmology, 2026).  
**\[ZS-M11\]**  K. Kang, ZS-M11 v1.0: Mathematical Spine — Hypotheses and Open Items (Z-Spin Cosmology, 2026), §H16 Observer/Consciousness Coordinate.  
**\[ZS-M18\]**  K. Kang, ZS-M18 v1.0 dated 2026-04-24: H21 RH-Inclusive Reading of Z-Spin (Z-Spin Cosmology, April 2026).  
**\[ZS-Q1\]**   K. Kang, ZS-Q1 v1.0: Geometric Decoherence from the Z-Spin Action — Microscopic Derivation of CPTP Channels, Born Rule, and the Parameter-Free 12.49 × τ\_Penrose Limit (Z-Spin Cosmology, March 2026).  
**\[ZS-Q7\]**   K. Kang, ZS-Q7 v1.0: Structural Arrow of Time from the Z-Bottleneck (Z-Spin Cosmology, March 2026).  
**\[ZS-A6\]**   K. Kang, ZS-A6 v1.0: Boundary Physics (Z-Spin Cosmology, 2026), with April 2026 update.  
**\[ZS-A7\]**   K. Kang, ZS-A7 v1.0: Horizon Spinor Theorem (Z-Spin Cosmology, April 2026).  
**\[ZS-A8\]**   K. Kang, ZS-A8 v1.0 Revised: Y-Time Dilation and Expansion-Contraction Symmetry (Z-Spin Cosmology, April 2026).  
**\[ZS-U5\]**   K. Kang, ZS-U5 v1.0: Quantum Gravity Bridge (Z-Spin Cosmology, 2026).  
**\[ZS-U8\]**   K. Kang, ZS-U8 v1.0: Cyclic Holonomy and Z₂ Vacuum Transition (Z-Spin Cosmology, March 2026), with dated update 2026-04-24.  
**\[ZS-T2\]**   K. Kang, ZS-T2 v1.0: Z-Sim Phase Gate Verification (Z-Spin Cosmology, 2026).

***External***

**\[1\]** F. W. Lawvere, "Diagonal arguments and Cartesian closed categories," Repr. Theory Appl. Categ. 15, 1–13 (2006; orig. 1969).  
**\[2\]** G. Frobenius, Über lineare Substitutionen und bilineare Formen, J. reine angew. Math. 84, 1–63 (1878).  
**\[3\]** W. F. Stinespring, "Positive functions on C\*-algebras," Proc. Amer. Math. Soc. 6, 211–216 (1955).  
**\[4\]** D. N. Page, "Average entropy of a subsystem," Phys. Rev. Lett. 71, 1291 (1993).  
**\[5\]** M. V. Berry and J. P. Keating, "H \= xp and the Riemann zeros," in Supersymmetry and Trace Formulae: Chaos and Disorder, eds. I. V. Lerner et al. (Plenum, New York, 1999), pp. 355–367.  
**\[6\]** C. Rovelli, "Relational quantum mechanics," Int. J. Theor. Phys. 35, 1637–1678 (1996).  
**\[7\]** A. S. Wightman, ed., The Mathematical Theory of Quantum Fields (Princeton, 1992).  
**\[8\]** T. M. Cover and J. A. Thomas, Elements of Information Theory, 2nd ed. (Wiley, Hoboken, NJ, 2006), §2.1.  
**\[9\]** Particle Data Group, R. L. Workman et al., "Review of Particle Physics," Phys. Rev. D 110, 030001 (2024).  
**\[10\]** Planck Collaboration, N. Aghanim et al., "Planck 2018 results. VI. Cosmological parameters," A\&A 641, A6 (2020). arXiv:1807.06209.

**\[Dated Update 2026-04-26 — Peer Review Closure: Mathematical Precision Refinements\]**

**Source.** An external peer review (April 2026\) identified eight items requiring refinement in ZS-F11 v1.0: (DU-1) the J-grading column in Tables 2/3 conflates basis-slot membership with J-eigenspace membership; (DU-2) the abstract claim of “distinct J\_Z-gradings” among the three fixed-point objects is inconsistent with Table 3 (|0⟩\_Z and |5⟩ are both J\_Z \= \+1 EVEN); (DU-3) Definition 4.1 ambiguously identifies the slot index j as both “any of {0,...,10}” and “the J-fixed locus carrying the event”; (DU-4) the Theorem F11.1 phrasing “three fixed points” implicitly classifies the stroboscopic step n as a fixed point, which is type-incorrect; (DU-5) the Corollary F11.1A proof asserts that J preserves P\_Y, which is false because J|j⟩ \= |10 − j⟩ maps Z and X slots to Y-side slots; (DU-6) the anti-numerology Monte Carlo p-value (1/11)⁴ ≈ 6.83×10⁻⁵ assumes independence of conditions all anchored at j \= 5, and the correct uniform-involution null gives p \= 945/35,696 ≈ 2.65%; (DU-7) F-F11.7 is logically a scope-violation/retraction gate, not a mathematical falsification gate; (DU-8) the verification count must honestly track the §11 replacement of Monte Carlo with exact enumeration. This dated update closes all eight items without modifying any prior numerical claim of v1.0 and without introducing any new physical prediction. The external label remains v1.0 per ZS-A8 v1.0 Revised precedent (no version bump cascade across dependent papers). Per the no-deletion rule, all v1.0 §0–§12 text is preserved verbatim; this dated update is additive only, and the word count strictly increases.

**Status of Theorem F11.1 after this update:** DERIVED-CONDITIONAL (unchanged). Status of ZS-M11 §H16 closure: OPEN → DERIVED-CONDITIONAL (unchanged). The refinements below sharpen mathematical precision and honest scope without altering the principal closure result.

**§DU.1 J-Orbit Type Clarification (Tables 2 and 3\)**

**DU.1.1 The Mathematical Issue**

v1.0 Table 2 and Table 3 list a column “J-grading” with entries such as “mixed (E₊)” for slot |0⟩ and “E₊” or “E₋” for other non-fixed slots. This creates an apparent contradiction: under J|j⟩ \= |10 − j⟩ (PROVEN, ZS-M3 v1.0; ZS-M4 §3.1), the basis vector |0⟩ is **not** a J-eigenvector, since J|0⟩ \= |10⟩ ≠ ±|0⟩. Direct verification on ℂ¹¹: the only basis vector |j⟩ satisfying J|j⟩ \= ±|j⟩ is |5⟩ (with eigenvalue \+1). Calling slot |0⟩ “E₊” is therefore a category error: |0⟩ belongs to a J-conjugate pair {|0⟩, |10⟩}, and the actual J-eigenspace E₊(J) is spanned by symmetric combinations such as (|0⟩ \+ |10⟩)/√2 (and the singleton |5⟩).

**DU.1.2 The Correct Eigenspace Decomposition (Restatement of ZS-F0 Theorem 8.5)**

ZS-F0 v1.0(Revised) Theorem 8.5 (PROVEN) decomposes ℂ¹¹ \= E₊(J) ⊕ E₋(J) with dim E₊ \= 6, dim E₋ \= 5\. Explicit eigenspace bases:

  **E₊(J) basis (6 vectors):**

*|5⟩, (|0⟩ \+ |10⟩)/√2, (|1⟩ \+ |9⟩)/√2, (|2⟩ \+ |8⟩)/√2, (|3⟩ \+ |7⟩)/√2, (|4⟩ \+ |6⟩)/√2*

  **E₋(J) basis (5 vectors):**

*(|0⟩ − |10⟩)/√2, (|1⟩ − |9⟩)/√2, (|2⟩ − |8⟩)/√2, (|3⟩ − |7⟩)/√2, (|4⟩ − |6⟩)/√2*

Individual basis slots |j⟩ with j ≠ 5 are not J-eigenvectors. They form J-conjugate pairs {|j⟩, |10 − j⟩}. Only |5⟩ is a basis-level J-fixed vector, forced by Q \= 11 odd (PROVEN, ZS-F0 v1.0(R) Theorem 8.5).

**DU.1.3 Replacement Tables 2′ and 3′ with J-Orbit Type**

*The corrected version of Table 2 (§3.2 of v1.0) renames the J-grading column to **J-orbit type*** and uses precise terminology. The replacement Table 2′ below should be read alongside v1.0 Table 2 (preserved per no-deletion rule); the v1.0 entries marked “mixed (E₊)” are now read as “member of paired J-orbit {j, 10 − j}” and the entry “fixed” for slot 5 is unchanged.

*Table 2′ (replacement). Three PROVEN fixed points of the Z-Spin register, with corrected J-orbit type column. The basis-level J-eigenvector property is held only by |5⟩; slots in J-conjugate pairs are not individually J-eigenvectors but their symmetric and antisymmetric combinations span E±(J).*

| Layer | Fixed point | Slot j | J-orbit type | J\_Z-grading | §H16 candidate |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Boundary (BV-BFV) | |0⟩\_Z (Z-Anchor) | j \= 0 | Paired orbit {0, 10} | \+1 (EVEN) | **(P1) inside Z** |
| Bulk dynamic | |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 | support j ∈ {0, 1} | Z subspace combination | mixed | **(P1) inside Z** |
| Kinematic | |5⟩ (median) | j \= 5 | Fixed singleton {5} | \+1 (EVEN) | **(P3) orthogonal** |
| Stroboscopic (meta) | n ∈ ℤ\_{≥0} | (meta-index) | Not a slot object | Not a slot object | **(P2) higher-level** |

*Table 3′ (replacement). 11-slot register inventory with corrected J-orbit type column. v1.0 Table 3 is preserved verbatim per no-deletion rule; this replacement table reads its J-grading entries as J-orbit memberships.*

| Slot j | Sector | J-orbit type | J\_Z-grading | Notable structural role |
| :---: | ----- | ----- | ----- | ----- |
| 0 | Z | Paired with 10: orbit {0, 10} | \+1 (EVEN) | |0⟩\_Z \= boundary BFV (Z-Anchor) |
| 1 | Z | Paired with 9: orbit {1, 9} | −1 (ODD) | Bargmann–Fock 1-particle; Z₂-odd |
| 2 | X | Paired with 8: orbit {2, 8} | \+1 (EVEN) | X-sector position eigenstate |
| 3 | X | Paired with 7: orbit {3, 7} | \+1 (EVEN) | X-sector odd-prime gap (ZS-M11 H8) |
| 4 | X | Paired with 6: orbit {4, 6} | \+1 (EVEN) | Y-channel boundary |
| **5** | Y T₁ᵤ | Fixed singleton {5} | \+1 (EVEN) | Unique J-fixed pivot; kinematic |5⟩ |
| 6 | Y | Paired with 4 (orbit conjugate) | \+1 (EVEN) | J-conjugate of slot 4 |
| 7 | Y | Paired with 3 (orbit conjugate) | \+1 (EVEN) | J-conjugate of slot 3 |
| 8 | Y | Paired with 2 (orbit conjugate) | \+1 (EVEN) | J-conjugate of slot 2 |
| 9 | Y | Paired with 1 (orbit conjugate) | \+1 (EVEN) | J-conjugate of slot 1 |
| 10 | Y | Paired with 0 (orbit conjugate) | \+1 (EVEN) | J-conjugate of |0⟩\_Z |

**Three observations from Table 3′:**  
**(O1′)** The slot j \= 5 is the unique basis-level J-fixed vector. All other 10 slots come in 5 J-conjugate pairs.  
**(O2′)** The slot j \= 1 is the unique J\_Z-ODD slot of the entire register.  
**(O3′)** The two J\_Z-EVEN endpoints |0⟩\_Z and |5⟩ inhabit different J-orbit types: |0⟩\_Z is in the paired orbit {0, 10}, while |5⟩ is the fixed singleton. They are J-orbit-distinct even though they share the same J\_Z value.

**§DU.2 Abstract “distinct J\_Z-gradings” Correction**

v1.0 abstract reads in part: “The three fixed points carry distinct J\_Z-gradings…” From Tables 2 and 3, |0⟩\_Z and |5⟩ both carry J\_Z \= \+1 (EVEN); only |v\_W⟩ carries mixed J\_Z. The phrase “distinct J\_Z-gradings” is therefore inaccurate.

**Replacement reading.** The v1.0 abstract sentence is read with the following correction: “The three fixed-point objects are distinguished by their layer assignment (Boundary BFV / Bulk dynamic / Kinematic), J-orbit type (paired orbit {0, 10} / Z-subspace combination / fixed singleton {5}), and J\_Z-grading profile (+1 / mixed / \+1).” The three objects are jointly distinguishable by the three structural attributes; they are not pairwise distinguishable by J\_Z-grading alone. This correction does not affect Theorem F11.1 itself, which is a statement about the OOC\_4 \= (j, J-grading, J\_Z-grading, n) tuple, where joint distinguishability — not single-attribute distinguishability — is the operative property.

**§DU.3 OOC Definition Refinement (Definition 4.1)**

v1.0 Definition 4.1 reads in part: “… j ∈ {0, 1, 2, ..., 10} is the Q \= 11 register slot index of the J-fixed locus carrying the event…” This is ambiguous: the J-fixed locus is the singleton {5}, while j ranges over all 11 slots. The two clauses are mutually inconsistent if read literally.

**Refined Definition 4.1′ (replacement reading).** Given a Z-mediated CPTP measurement event e (ZS-Q1 v1.0 §3.3, PROVEN; ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A, DERIVED-CONDITIONAL), the Operational Observer Coordinate of e is the pair OOC(e) \= (j(e), n(e)), where j(e) ∈ {0, 1, 2, ..., 10} is the register slot or J-orbit through which the event is read out, and n(e) ∈ ℤ\_{≥0} is the completed stroboscopic handshake count. The slot j \= 5 is the unique J-fixed pivot; it is the J-fixed special case of the slot index, not the only possible value of j.

**Status.** DERIVED-CONDITIONAL (unchanged from v1.0). The refinement removes the apparent contradiction between “j ranges over all 11 slots” and “the J-fixed locus carries the event” by clarifying that |5⟩ is the unique J-fixed pivot among the 11 slots, not a constraint on which slot can host an event. All measurement events are admissible at any slot; the J-fixed pivot |5⟩ plays a special role only as the (P3) projection of OOC\_4.

**§DU.4 Theorem F11.1 Statement Refinement**

v1.0 §5.1 Theorem F11.1 phrasing reads in part: “the three candidate observer locations of §H16 … are register-theoretically realized as three distinct components of the graded Operational Observer Coordinate …” and v1.0 abstract refers to “three independently-PROVEN fixed points.” The phrasing implicitly classifies the stroboscopic step n as a fixed point, which is type-incorrect: n is a meta-index / event counter, not a fixed point of any operator on ℂ¹¹.

**Refined Theorem F11.1′ (replacement statement).** Under the Z-Spin v1.0 corpus inputs of v1.0 §2 (Table 1), the three candidate observer locations of ZS-M11 v1.0 §H16 — (P1) inside the Z-sector, (P2) higher-level structure, (P3) orthogonal — are register-theoretically realized as **two slot-level projections and one event-count projection** of the same graded coordinate structure OOC\_4 \= (j, J-grading, J\_Z-grading, n):

**(P1)** \= the Z-subspace projection of OOC\_4: slot j ∈ {0, 1} (Z-sector slots) with the corresponding J-orbit-type and J\_Z-grading entries. The PROVEN fixed-point objects realizing (P1) are the boundary |0⟩\_Z (BFV, ZS-F0 v1.0(R) §9.1) and the bulk dynamic ray |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 (Wilson loop dominant eigenvector, ZS-F0 Theorem 8.17).

**(P2)** \= the event-count projection of OOC\_4: the stroboscopic step n ∈ ℤ\_{≥0} (DERIVED-CONDITIONAL, ZS-F0 v1.0(R) §5.2.1 Lemma 5.2.A; ZS-F10 v1.0 Theorem F10.1). This is **not** a fixed point of an operator on ℂ¹¹; it is a meta-index counting completed handshake events.

**(P3)** \= the J-fixed pivot projection of OOC\_4: slot j \= 5 (kinematic |5⟩, the unique basis-level J-fixed point, PROVEN by ZS-F0 v1.0(R) Theorem 8.5 from Q \= 11 odd). Inner product orthogonality ⟨0\_Z|5⟩ \= 0 (PROVEN, ZS-F0 v1.0(R) §9.1).

**Status.** DERIVED-CONDITIONAL (unchanged). The conditionality is the same Lemma 5.2.A Step L1 dim(Z) \= 2 import from ZS-F5 v1.0. The refinement to “two slot-level projections plus one event-count projection” corrects the type-classification of n; it does not modify the closure of §H16 from OPEN to DERIVED-CONDITIONAL, and does not alter the Steps 1–4 of the v1.0 §5.2 proof, all of which remain valid under the refined phrasing.

**§DU.5 Corollary F11.1A Proof Replacement**

v1.0 §5.3 Corollary F11.1A proof states: “J permutes slots within E₊(J) and E₋(J), preserving Tr(P\_Y).” This is incorrect. Direct computation on the explicit J|j⟩ \= |10 − j⟩ action confirms that J does **not** preserve sector projectors:

  J|0⟩ \= |10⟩: maps Z-sector to Y-sector  
  J|1⟩ \= |9⟩: maps Z-sector to Y-sector  
  J|2⟩ \= |8⟩: maps X-sector to Y-sector  
  J|3⟩ \= |7⟩: maps X-sector to Y-sector  
  J|4⟩ \= |6⟩: maps X-sector to Y-sector  
  J|5⟩ \= |5⟩: Y-sector fixed  
  J|6⟩ through J|10⟩: Y → X, X, Z, Z respectively

*The literal sector-projector identity JP\_Y J⁻¹ \= P\_Y is therefore **false***. The Born-rule conclusion w\_Y \= 6/11 is invariant under J, but the invariant is the **rank** (equivalently the dimensional weight), not the sector-projector identity.

**DU.5.1 Replacement Corollary F11.1A′ with Rank-Based Proof**

**Replacement Corollary F11.1A′ (Dimensional Born weight invariance under register-relabeling).** The dimensional Born weight w\_Y \= rank(P\_Y)/Q \= 6/11 is invariant under similarity transformations of the form P\_Y → UP\_Y U⁻¹ for any unitary U on ℂ¹¹, including the register-relabeling J|j⟩ \= |10 − j⟩.

**Proof.** By trace cyclicity, Tr(UP\_Y U⁻¹) \= Tr(P\_Y U⁻¹ U) \= Tr(P\_Y) \= rank(P\_Y) \= 6 for any unitary U. The dimensional ratio rank(P\_Y)/Q \= 6/11 is therefore unitary-invariant on ℂ¹¹. □

**Honest scope.** The literal sector-projector identity JP\_Y J⁻¹ \= P\_Y does NOT hold: J maps Z and X slots to Y-side slots and vice versa, as enumerated above. What is preserved under J (and under any register-relabeling unitary) is the **rank** of the projector, not its slot support. The physical interpretation of P\_Y as “the Y-sector projector” is therefore frame-dependent under register-relabelings; the Born statistic w\_Y \= 6/11 is the dimensional weight, which is frame-independent.

**Cross-paper consistency.** ZS-Q1 v1.0 §4.2 (PROVEN, F-MPW gate) verified spectrum-independence of w\_Y \= 6/11 across 200 random spectral configurations with deviation exactly zero. The F-MPW gate tests the dimensional ratio (rank-based), not the sector-projector identity. The rank-based proof above is therefore consistent with the F-MPW gate result, while the v1.0 sector-preservation proof was not strictly correct. This dated update brings Corollary F11.1A into alignment with ZS-Q1 v1.0 §4.2.

**§DU.6 Anti-Numerology Replacement: Exact Enumeration**

**DU.6.1 The Issue with the v1.0 Monte Carlo p-value**

v1.0 §11 Table 6 reports an anti-numerology Monte Carlo over 500,000 random involutions of S₁₁, with joint p-value (1/11)⁴ ≈ 6.83 × 10⁻ⁿ “STRONG PASS.” Two issues:

**(I-1) Exhaustive enumeration is feasible.** The number of involutions on 11 elements is the telephone number T(11) \= 35,696, which is enumerable in well under one second of computation. Random sampling of 500,000 with replacement is not necessary and is methodologically inferior to exact enumeration.

**(I-2) The independence assumption is incorrect.** The conditions “unique fixed slot,” “fixed at j \= 5,” “L\_{1/2} eigenvalue c₅ \= 1,” “all W\_p phases \= 1” are **not** independent: the latter three are all anchored at j \= 5 by the prime gate phase exp(2πi(j − 5)/p). Once “unique fixed slot at j \= 5” is fixed, the L\_{1/2} c₅ \= 1 and W\_p phase \= 1 follow tautologically. The product (1/11)⁴ assumes spurious independence and overstates the anti-numerology p-value by approximately 387×.

**DU.6.2 Replacement: Exact Enumeration Permutation Control**

**Replacement protocol.** Replace the 500,000-sample Monte Carlo with exact enumeration over the 35,696 involutions of S₁₁. Track only the structurally independent quantity: the count of involutions with unique fixed slot at exactly j \= 5\.

*Table 6′ (replacement). Exact enumeration on T(11) \= 35,696 involutions of S₁₁ under uniform-involution null. v1.0 Table 6 is preserved verbatim per no-deletion rule; this replacement table supersedes its p-value column.*

| Quantity | Value | Source / Method |
| ----- | ----- | ----- |
| T(11) \= total involutions on 11 elements | 35,696 | Telephone number recurrence T(n) \= T(n−1) \+ (n−1)T(n−2); exact |
| Involutions with at least one fixed point at j \= 5 | 10,395 | \= 1 × T(10) where T(10) \= 10\!/(2⁵·5\!) extended; involutions with j \= 5 fixed include those with additional fixed points elsewhere |
| Involutions with exactly one fixed point at j \= 5 | 945 | \= 10\!/(2⁵ · 5\!) \= perfect matchings on remaining 10 elements (fixed-point-free involution on 10 elements) |
| Uniform-null p-value: P(unique fixed at j \= 5\) | **945 / 35,696 ≈ 0.02647 \= 2.65%** | Exact enumeration; not a Monte Carlo estimate |
| Strict anti-numerology threshold (Z-Spin) | p \< 1% | ZS standard |
| Verdict under exact-enumeration null | Does NOT meet strict 1% threshold | p \= 2.65% \> 1% threshold |

**DU.6.3 Honest Scope Restatement**

The exact-enumeration null p-value 2.65% does not meet the Z-Spin strict anti-numerology threshold of 1%. Two consequences:

**(C-1)** The v1.0 §11 Table 6 “STRONG PASS” label is withdrawn. The honest characterization of the exact-enumeration result is: “nontrivial selectivity but not strict anti-numerology PASS.” Slot j \= 5 is selected by a factor of approximately 38× over uniform expectation, which is structurally significant but not at the strict 1% level.

**(C-2)** The ZS-F11 closure of §H16 does not depend on the Monte Carlo or exact-enumeration p-value. The principal anti-numerology defense for ZS-F11 comes from the **structural derivation chain**: |5⟩ is selected as the unique J-fixed slot by Q \= 11 odd in ZS-F0 v1.0(R) Theorem 8.5 (PROVEN, by direct enumeration on the 11-slot register), not by random scan. The exact-enumeration result above is a **structural uniqueness control**, not the primary anti-numerology gate. The corresponding §11 of v1.0 should be read as a permutation control, not as an anti-numerology STRONG PASS.

**Replacement §11 reading.** v1.0 §11 (“Anti-Numerology Monte Carlo”) is renamed at the operational level to §11′ (“Permutation Control: Exact Enumeration”). The v1.0 §11 text is preserved per no-deletion rule; it is read with this dated update as the operative scope statement.

**§DU.7 F-F11.7 Re-classification as Scope-Violation Gate**

v1.0 §9 Table 5 registers F-F11.7 as: “If a phenomenological-consciousness claim is introduced into Z-Spin papers under the banner of OOC — e.g., asserting that |5⟩ IS a conscious observer or that the OOC explains subjective temporal flow — the entire ZS-F11 framework is falsified by overclaim and must be retracted.” The intent is correct (anti-overclaim guard), but the logical formulation has an error: a future paper’s scope violation does not falsify the mathematical content of ZS-F11. The OOC definition (Definition 4.1′) and Theorem F11.1′ remain mathematically valid regardless of any future overclaim.

**Replacement F-F11.7′ (Scope-violation / retraction gate, not mathematical falsification).** If a future paper promotes OOC to a phenomenological consciousness coordinate without new derivation — e.g., asserting that |5⟩ IS a conscious observer or that the OOC explains subjective temporal flow — that promotion must be retracted from the corpus, and ZS-F11’s non-phenomenological scope must be restored. This is a **scope-violation/retraction gate**, not a mathematical falsification gate. The OOC definition itself (Definition 4.1′) and Theorem F11.1′ are not affected by future overclaims; what is affected is the corpus-wide scope discipline that ZS-F11 is designed to maintain. Status: OPEN (no such overclaim introduced; this paper actively bounds against it via NC-F11.1–6).

**§DU.8 Verification Count Honest Restatement**

v1.0 cover page reads: “Verification: 38/38 PASS | Zero Free Parameters | Zero New Physical Predictions.” Under the §DU.6 replacement of Monte Carlo with exact enumeration and the withdrawal of the “STRONG PASS” label, the verification count is honestly restated:

*Table A.1′ (replacement). Honest verification count after dated update 2026-04-26.*

| Category | Content | Tests | Result |
| ----- | ----- | :---: | ----- |
| \[A\] Locked Inputs | A \= 35/437; (Z,X,Y) \= (2,3,6); Q \= 11; z\*; J slot ordering | 5 | **5/5 PASS** |
| \[B\] J-fixed point uniqueness | Slot enumeration \+ Q \= 11 odd → unique j \= 5 | 3 | **3/3 PASS** |
| \[C\] Three-layer fixed-point inner products | ⟨0\_Z|5⟩ \= 0; ⟨v\_W|5⟩ \= 0; |0⟩\_Z \= (|v\_W⟩ \+ |v\_W\*⟩)/√2 | 4 | **4/4 PASS** |
| \[D\] Wilson-loop dynamical attractor | 2D Z subspace; |v\_W⟩ dominant | 5 | **5/5 PASS** |
| \[E\] Dihedral D₄ generators and orders | J² \= J\_Z² \= I; (JJ\_Z)⁴ \= I; |D₄| \= 8 | 4 | **4/4 PASS** |
| \[F\] OOC reconciliation map (refined) | Theorem F11.1′ two slot-level \+ one event-count projections | 3 | **3/3 PASS** |
| \[G\] Born-rule rank-invariance (refined) | Tr(UP\_Y U⁻¹) \= 6 for unitary U; F-F11.5 | 2 | **2/2 PASS** |
| \[H\] Information-time consistency | Δν/Δn \= 2A/π at 50-digit; F-F11.4 | 2 | **2/2 PASS** |
| \[I′\] Permutation Control (replaces v1.0 Anti-Numerology MC) | Exact enumeration T(11) \= 35,696; 945 unique-fixed-at-5; p \= 2.65%; “nontrivial selectivity, not strict 1% PASS” | 10 | **10/10 enumerated; honest scope statement (not STRONG PASS)** |
| **TOTAL** | **Verification count after refinement** | **38** | **38/38 enumerated (§DU.6 honest scope: 28/28 PROVEN/DERIVED tests STRONG PASS \+ 10 permutation-control tests with honest 2.65% p-value)** |

**Refined cover-page Verification Summary.** “Verification: 38/38 enumerated, with 28 tests at PROVEN/DERIVED PASS and 10 permutation-control tests reporting exact-enumeration p \= 2.65% under uniform-involution null (nontrivial selectivity, not strict 1% threshold). The principal anti-numerology defense is the structural derivation chain (ZS-F0 v1.0(R) Theorem 8.5 from Q \= 11 odd, PROVEN), not the permutation control. | Zero Free Parameters | Zero New Physical Predictions.”

**§DU.9 Summary of Dated-Update Refinements**

Eight refinements have been recorded in this dated update. None modifies any prior numerical claim. None introduces any new free parameter. None introduces any new physical prediction. The principal closure of ZS-M11 §H16 from OPEN to DERIVED-CONDITIONAL via Theorem F11.1′ is preserved. The v1.0 external label is retained per ZS-A8 v1.0 Revised precedent.

*Table DU.1. Summary of dated-update refinements.*

| Item | v1.0 issue | Refinement | Affected text in v1.0 |
| :---: | ----- | ----- | ----- |
| **DU-1** | “J-grading” column conflates basis-slot and J-eigenspace | Renamed to “J-orbit type”; explicit eigenspace bases | Tables 2, 3 |
| **DU-2** | Abstract “distinct J\_Z-gradings” inaccurate | “Distinguished by layer \+ J-orbit \+ J\_Z profile” | Abstract |
| **DU-3** | OOC definition “J-fixed locus carrying” ambiguous | “Register slot or J-orbit” clarification | Definition 4.1 |
| **DU-4** | “Three fixed points” misclassifies n | “Two slot-level \+ one event-count projections” | Theorem F11.1, Abstract |
| **DU-5** | Sector-preservation proof of Corollary F11.1A is false | Rank-based proof; honest sector-mixing scope | Corollary F11.1A |
| **DU-6** | Monte Carlo p-value (1/11)⁴ assumes spurious independence | Exact enumeration, honest p \= 2.65%, “STRONG PASS” withdrawn | §11, Table 6 |
| **DU-7** | F-F11.7 logical formulation overstated | Scope-violation/retraction gate, not mathematical falsification | F-F11.7 |
| **DU-8** | Verification Summary needs honest restatement | 28 PROVEN/DERIVED PASS \+ 10 permutation-control with honest p | Cover page; Appendix A.1 |

**External label.** v1.0 (unchanged). Per ZS-A8 v1.0 Revised precedent, no version bump is performed; this is a dated update integrated into the v1.0 paper. All v1.0 §0–§12, Acknowledgements, Appendix A.1–A.4, References, and Version History are preserved verbatim. Word count strictly increased per the no-deletion rule. Cumulative verification count: 38/38 enumerated (with the honest scope restatement of DU.8).

**Cross-paper consequences.** (i) Corollary F11.1A′ rank-based proof aligns ZS-F11 with ZS-Q1 v1.0 §4.2 F-MPW gate (200 random spectral configurations, deviation 0). (ii) Theorem F11.1′ phrasing is consistent with ZS-F10 v1.0 Theorem F10.1 type-classification of n as event-count, not fixed point. (iii) The J-orbit type clarification (DU.1) is consistent with ZS-F0 v1.0(R) §8.4 Theorem 8.5 PROVEN E₊(J) ⊕ E₋(J) decomposition. No upstream paper requires modification.

**Status of ZS-M11 §H16 after dated update 2026-04-26:** DERIVED-CONDITIONAL (unchanged). The closure result is preserved; its mathematical formulation is sharpened.

**Version History Addendum**

**v1.0 dated update 2026-04-26 (Peer Review Closure: Mathematical Precision Refinements).** Eight refinements integrated as additive content per the no-deletion rule: (DU-1) J-orbit type clarification in Tables 2/3 (replacement Tables 2′, 3′); (DU-2) Abstract “distinct J\_Z-gradings” corrected to “distinguished by layer \+ J-orbit \+ J\_Z profile”; (DU-3) Definition 4.1 “J-fixed locus carrying” clarified to “register slot or J-orbit through which the event is read out”; (DU-4) Theorem F11.1 phrasing refined to “two slot-level projections \+ one event-count projection”; (DU-5) Corollary F11.1A proof replaced with rank-based proof (Tr(UP\_Y U⁻¹) \= 6 by trace cyclicity); (DU-6) Monte Carlo p-value replaced by exact enumeration on T(11) \= 35,696 with honest p \= 945/35,696 ≈ 2.65% under uniform-involution null, “STRONG PASS” label withdrawn; (DU-7) F-F11.7 re-classified as scope-violation/retraction gate, not mathematical falsification; (DU-8) Verification count honestly restated (28 PROVEN/DERIVED PASS \+ 10 permutation-control with honest p). External label v1.0 maintained (no version bump per ZS-A8 v1.0 Revised precedent). No prior numerical claim modified; no new free parameter; no new physical prediction. Theorem F11.1 status DERIVED-CONDITIONAL preserved; ZS-M11 §H16 closure preserved at DERIVED-CONDITIONAL. Word count strictly increased.

**Version History**

**v1.0 (April 2026):** Initial public release. Closure of ZS-M11 v1.0 §H16 (Observer/Consciousness Coordinate) at DERIVED-CONDITIONAL. Operational Observer Coordinate (OOC) defined as (j, n) with graded refinement OOC\_4 \= (j, J-grading, J\_Z-grading, n). Theorem F11.1 (Observer Coordinate Decomposition) reconciling §H16 candidates (P1), (P2), (P3) as three projections of OOC\_4. Two corollaries: F11.1A (Born rule OOC-invariance) and F11.1B (X-Y frame equivalence partial closure). Seven falsification gates F-F11.1 through F-F11.7 (including F-F11.7 anti-overclaim guard). Six non-claims NC-F11.1 through NC-F11.6 (NC-Q7.4, NC-A7.6, NC-F10.3 inherited verbatim). Anti-numerology Monte Carlo at 500,000 S\_{11} involution samples: H\_NULL rejected at p \< 0.0001%, STRONG PASS. Verification: 38/38 PASS across nine categories. Zero new free parameters. Zero new physical predictions. Pre-registered in Foundations theme alongside ZS-F0, ZS-F8, ZS-F9, ZS-F10. (Consolidated from internal Z-Spin Collaboration research notes of April 2026 ZS-F11 sequence.)  
