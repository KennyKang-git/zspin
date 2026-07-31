# **ZS-M57**

# **The Odd Carrier**

**The seam does not act on the pointer: a domain resolution of the D₄ trichotomy, the Real-Multiplier Lemma, and the layer verdict for the graded collision instrument**

Kenny Kang · Z-Spin Cosmology Collaboration  
July 2026 · Theme: Mathematical Spine · Paper code: ZS-M57 · Version 1.8  
Parent: ZS-M56 v1.8 FINAL (101/101 PASS, 20 declarations). Grandparent: ZS-M54 v2.2 FINAL. Seeds: ZS-M57 SEED v1.1 (July 2026), merging Seed Report A v1.0 and Seed Report B v1.0. Siblings: ZS-Q19 takes τ\_Z and ρ\_E. ZS-M55 remains RESERVED and untouched.  
Locked inputs: (A, Q, dim Z) \= (35/437, 11, 2). Free fitted parameters: 0\.

**Verification: 96/96 PASS \+ 12 declarations | 0 FAIL | construction layer (λ-free) \= 55, of which proof-bearing (R+A) \= 46 | comparison layer \= 41, never evidence for a construction claim | classes R \= 44, A \= 28, X \= 24 | firewall tags re-audited three times | seed regression 39/39 PASS reproduced independently | one seeded run of zs\_m57\_verify\_v1\_8.py (seed 57\) | exact integer Świerczkowski certificate: 118,096 reduced words, zero failures | Fourier–Weyl carrier frame λ-free from (S, P\_E, J\_Z): eleven relations exact | constructed carrier reproduces Φ\_λ to 4.7×10⁻¹⁶ with Choi rank 2 | F-M54-16′ NOT CLOSED (declarations C6, K10) | ZS-M56 v1.8 101-check regression NOT run in this build (debt 1; central inequality reproduced independently by check X5) | all ZS-F0 §8 printed figures reproduced to the printed digit; Haar-random quantities reported as bounds, not exact mantissas | (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED | Zero Free Parameters | No new constant introduced.**

## **§0. Abstract**

Two declarations are made before any result, because the seed report required them and because each one determines what the rest of the paper is allowed to claim.

Declaration 1 (layer). Route G — the external graded collision instrument — is claimed at level **L2 (representation)** and not at level L1 (construction). Its collision angle θ\_D \= arccos|**λ**| is taken from the comparison layer, so any object built from it sits there too. §6 sharpens this into a bounded theorem about the collision **amplitude** |**λ**| \= cos θ\_D: it is not an algebraic function of **A** and **Q**, conditional on the corpus transcendence budget, so the seed’s proposed κ² \= A/Q amplitude route to θ\_D is closed. A derivation of the angle θ\_D that does not pass through an algebraic cosine is left OPEN, not closed. (The v1.0 draft overclaimed this as a no-go on θ\_D itself, on a step that is false by Lindemann–Weierstrass; §6.2 and Appendix C record the retraction and the corrected object.)

Declaration 2 (grading). Gate F-M57.11 — must the QND vertex respect J\_Z only, J only, or both? — resolves to **J\_Z only**, and it resolves by domain rather than by dynamics. Pre-registered outcomes F (D₄ closure) and G (boundary redirection) are therefore both CLOSED-NEGATIVE.

The reason is one line of linear algebra on the corpus's own definitions. In the ZS-F0 §8 / ZS-M6 §2.1 register basis — the basis in which J\_Z \= I₁₁ − 2|1⟩⟨1| is defined at all, with slot 0 the β₀ physical mode and slot 1 the ℤ₂-odd mode — the Z-sector is span{|0⟩, |1⟩}, and the seam involution J|j⟩ \= |10−j⟩ carries it to span{|9⟩, |10⟩}. The two spans intersect trivially. So J has no restriction to the pointer system on which Z\_path acts, no J-grading of that system exists, and no equivariance condition involving J can be imposed on the QND vertex. The smallest J-invariant subspace containing the pointer has dimension four, not two.

Three consequences follow. (i) ZS-M56 v1.8 is aimed at the correct layer; the correction it requires is nomenclatural only, and its inequality q\_R(J\_Z) \= 1 \< 2 ≤ dim E stands unaltered. (ii) The seed's proposed successor, Theorem M57.D.2, is not merely conditional on an unforced choice of pointer representation — it is **not formulable**, because the pointer is not a D₄-subrepresentation. It is registered NON-CLAIM. (iii) The seed's J-compatible sector split, which places the Z-sector on the seam pair (4, 6), is a different register from the corpus's; under the corpus grading that pair carries J\_Z \= \+I, a central grading with zero odd operators, so it fails the charge constraint it was scored as satisfying.

What survives is stronger than what was proposed. Theorem M57.D.1 — ℂ^Q \= ((Q−1)/2)A₁ ⊕ ((Q−3)/2)B₂ ⊕ E with mult(E) \= 1 for every odd Q, giving 5A₁ ⊕ 4B₂ ⊕ E at Q \= 11 — is retained as PROVEN mathematics, and the E-block is now **located**: it is span{|1⟩, |9⟩}, the odd Z-mode together with its seam image, independently of which slot carries the Z-internal sign. That gives ZS-F0 Conjecture 8.14 its first concrete carrier without closing it. Theorem M57.P, the Real-Multiplier Lemma, is proved in two lines and verified λ-free over 1000 Haar draws: an exact grading-preserving QND collision with a grading-invariant carrier state has a real coherence multiplier. Since Im **λ** \= 0.6884532271, the corpus needs a separate phase layer — which is exactly the ZS-M54 (11a)/(11b) separation, now derived rather than assumed.

What is not closed is stated plainly and is unchanged from the parent: F-M54-16′ remains open, and Route S — the stochastic realisation, the one route no multiplicity argument reaches — is specified here and executed nowhere. On the carrier the two statements that must not be conflated are these: an admissible carrier EXISTS and is exhibited in §§11–12 (so the specification is not vacuous), while “ZS-S14 SELECTS that carrier” is not shown and is what F-M54-16′ still asks. Its two moments must be derived from the ZS-S14 action and not fitted; by Theorem M56.7 a two-parameter fit to two constraints carries zero evidential content, and that trap is pre-registered rather than sprung.

**Part II (§§7–15) is the result of seven review cycles, and its shape is a chain of corrections rather than an accumulation of claims.** The v1.1 amplitude theorem — |**λ**| \= cos θ\_D is not an algebraic function of **A** and **Q** — was read in reverse as the hypothesis of de Groot's free-rotation theorem, giving a rank-2 FREE collision group at the corpus angle, a paradoxical carrier sphere, and the record obstruction that no total collision-invariant valuation exists (§§8–9). The face layer of the mediation is thereby identified as the carrier 2-sphere, the first non-amenable rung of the ladder on which Banach measures fail. An admissible carrier was then CONSTRUCTED and shown to reproduce Φ\_λ exactly, settling that the closing specification is satisfiable and not vacuous — but the reparametrisation theorem shows the construction transports **λ** rather than deriving it (§11). The Fourier–Weyl frame fixed the carrier operators from register kinematics alone, closing a U(1) gauge the earlier construction left free (§12). The structural gate was then proved to UNDERDETERMINE the multiplier — it is passed by every α in the punctured disc — so the residual is exactly one complex number and no fewer; and the free-group route to the phase was closed, since every mixture over collision words is real (§13).

**The last three cycles are about the clock, and each retracts the one before.** A QND multiplier is the interaction integrated over the slab, so within the collision family the modulus sweeps all of (0, 1\) as the duration varies: Λ\_S14 is not determined by the action, and the slab duration τ\_Z occurs nowhere in the loaded corpus (§14). The clock-free ratio offered in its place was then itself corrected: a channel fixes Arg **λ** only modulo 2π, so the generator logarithm has branches and the invariant is a PROJECTIVE RAY \[Γ : Ω\_k\], one per branch, with the channel selecting none (Theorem M57.T.2′). Separating the EVENT clock from the METRIC clock then reopens the problem in a better form: the one-step map depends only on the dimensionless product gτ, so a per-event multiplier can be well posed where a finite-time one is not, and the successor gate becomes a dilation-theoretic equality — defect indices (1, 1), a degree-1 inner characteristic function, and an intertwiner to the ZS-M46 unit Abel translation — requiring no physical duration (§15). Two mechanisms proposed in the course of this work were refuted by it: the single-kernel Lamb-shift route (for strict QND the zero-frequency Lamb shift is central, hence a global and not a relative phase) and the Lambert–Dyson bootstrap (contraction shows the chosen equation is stable, not that it is selected), although the identity **λ** \= −W₀(−log i) is PROVEN. Version 1.8 audits the v1.7 closing sentence and finds it overcounted: the remaining prerequisites are FOUR and not two — pointer embedding, orbit-weight selection, the branch normalisation of the Abel step, and the intertwiner — the intertwiner being entangled with the branch rather than independent of it, plus one hypothesis (complete non-unitarity) the v1.7 gate omitted. Per-event testing needs no duration; it does need a normalisation. Every correction is recorded in Appendix C and every version in the Version History; F-M54-16′ remains OPEN throughout, and no result of this paper matches any corpus number except where explicitly declared non-evidential.

## **Epistemic Status Legend**

| Tag | Meaning as used in this paper |
| ----- | ----- |
| PROVEN | Mathematical theorem; standard mathematics alone, machine-verifiable. Used here for M57.D.1 and M57.P. |
| DERIVED | Follows from PROVEN corpus definitions plus standard mathematics, zero free parameters. Used for M57.1, M57.2, M57.3 and the F-M57.11 resolution. |
| DERIVED-CONDITIONAL | DERIVED conditional on an explicitly named hypothesis carried in the theorem line. Used for M57.G under (H-TRANS). |
| IMPORTED-PROVEN | Proved externally, used without re-proof, full citation given. Used for Frobenius reciprocity, the transcendence budget, and in v1.2 for Świerczkowski (1958), the Hausdorff–Banach–Tarski chain, Tarski's alternative (1938), Banach's low-dimension measures (1923), the closed-subgroup classification of SO(3), and Kesten's amenability criterion (1959). |
| VERIFIED-REGRESSION | Reproduces corpus numbers from corpus inputs. Guards drift; a control, never independent evidence. |
| ALGEBRAIC | An identity about a reconstructed operator, with no claim about the microscopic slab. Used for M57.F.0, whose U(1) gauge is subsequently FIXED by Theorem M57.K.1 (§12.1). |
| TAUTOLOGY | A check whose two sides share their premise. Never evidence. Reported as a control. |
| HYPOTHESIS / HYPOTHESIS-weak | Motivated conjecture; partial derivation chain. No result of this paper carries this tag. |
| OPEN | Recognised gap, honestly registered. Route S, Route B, F-M54-16′. |
| CLOSED-NEGATIVE | A route excluded by proof or by domain, with the scope of the exclusion stated exactly. |
| NON-CLAIM | Explicit declaration of what is not asserted; bounds the scope. Used for M57.D.2 as a physical obstruction. |
| RETRACTED-in-seed | A seed-stage claim withdrawn here before publication, with the withdrawal reason recorded. |
| LOCKED | Core constant fixed upstream; no downstream paper may modify it. |

## **§1. What ZS-M56 proved, and the two involutions it did not separate**

### **1.1 Two ℤ₂ involutions, both PROVEN in ZS-F0 §8**

ZS-F0 §8.4 Theorem 8.5 (PROVEN) states the seam involution and its grading:

J|j⟩ \= |10 − j⟩ ,  (n₊, n₋) \= (6, 5\) ,  |5⟩ the unique fixed point, forced by **Q** odd.

ZS-F0 §8.6 Definition 8.11 (PROVEN) introduces a second, explicitly different involution:

J\_Z := I₁₁ − 2|1⟩⟨1| \= diag(+1, −1, \+1, …, \+1) ,  (n₊, n₋) \= (10, 1).

Definition 8.11 calls this, in its own words, “a second natural ℤ₂ involution on ℂ¹¹, distinct from the seam involution J”, and identifies it as the register representation of the ZS-S1 §5.2 projection ε → −ε, “with slot 0 (β₀ physical) as ℤ₂-EVEN and slot 1 (ℤ₂-odd) as ℤ₂-ODD”. That parenthesis is not decoration. It fixes the register basis, and §2 shows that it is the whole question.

Table 1.1. Both involutions, recomputed against the ZS-F0 printed values (checks D1–D6). Every entry matches.

| Quantity | Recomputed | ZS-F0 source | Match |
| ----- | ----- | ----- | ----- |
| J multiplicities (n₊, n₋) | (6, 5\) | §8.4 Thm 8.5 | yes |
| J\_Z multiplicities (n₊, n₋) | (10, 1\) | §8.6 Def 8.11 | yes |
| Mat₁₁ grading by J (even, odd) | (61, 60\) | §8.4 Thm 8.6 | yes |
| Mat₁₁ grading by J\_Z (even, odd) | (101, 20\) | §8.6 Thm 8.12 | yes |
| ‖\[J, J\_Z\]‖\_F | 2.8284271 \= 2√2 ≠ 0 | §8.6 Thm 8.13 | yes |
| order of J·J\_Z | 4 | §8.6 Thm 8.13 | yes |
| |⟨J, J\_Z⟩| | 8, ≅ D₄ | §8.6 Thm 8.13 | yes |

### **1.2 What ZS-M56 v1.8 proved, and what it named**

ZS-M56 v1.8 §2.2 writes: “Let the seam ℤ₂ act on the register as J\_R \= I₁₁ − 2|1⟩⟨1| (ZS-F0 Def. 8.11)”, and its §7 conclusion opens: “The seam ℤ₂ of ZS-S1 §5.2 has a one-dimensional odd eigenspace in the Q \= 11 register.”

The mathematics is correct; the name is not. The operator carrying the ε → −ε selection rule is J\_Z, and Theorem M56.21′ is a true statement about J\_Z. The genuine seam involution J has a five-dimensional odd eigenspace. The seed report drew three consequences from this and called only the first cosmetic. This paper upholds the first, and **reverses the second and third**.

| \# | Seed v1.1 finding | Disposition in ZS-M57 v1.0 |
| ----- | ----- | ----- |
| (i) | The v1.8 title should read “Z-internal-ℤ₂-preserving”, not “seam-ℤ₂-preserving”. Cosmetic, but must be corrected before external submission. | UPHELD. The correction is nomenclatural and it is the only correction ZS-M56 v1.8 requires. |
| (ii) | The scope claim is affected: a J-preserving subsystem is not excluded, and §1.4 of the seed exhibits one. | REVERSED (§2.2, §4). A J-preserving subsystem is not a physically admissible object here, because the pointer system on which Z\_path acts is not J-invariant. The seed's counterexample is correct arithmetic in a different register. |
| (iii) | Had ZS-M56 read ZS-F0 §8.4 and §8.13, the D₄ structure would have been the obvious next question. | PARTIALLY UPHELD. The D₄ structure is the obvious next mathematical question and is answered here (§3). It is not the next physical question, and §4 shows why. |

Discipline note, recorded and not softened. The ZS-M56 line has now produced eight external findings, every load-bearing one caught from outside the drafting. The present paper is the ninth such event and it goes against its own seed. That is the pattern working as intended, not a failure of the seed; a seed whose central proposal survives its own successor's audit unchanged would be more worrying, not less.

### **1.3 The trichotomy, stated before any computation**

ZS-F0 §8.4 Theorem 8.7 (PROVEN) records that ‖\[J, L\]‖\_F ≈ 2.94 ≠ 0 for the block-Laplacian L: J is a boundary constraint operator, not a dynamical bulk symmetry. The force of the ZS-M56 selection rule comes entirely from the Hamiltonian respecting a grading. For J\_Z, which is the action-level ε → −ε symmetry, the Hessian does respect it and the rule bites. For J it does not.

The seed left this as a physical choice with three branches: J\_Z only (ZS-M56 stands under a corrected name), both (D₄-equivariance, strictly stronger), J only (ZS-M56 aimed at the wrong layer entirely, the seed's outcome G). It registered the choice as gate F-M57.11 and asked that it be settled before any construction. §2 settles it, and settles it in a way none of the three branch descriptions anticipated: the question is not which grading the vertex should respect, but which grading the pointer system admits.

## **§2. The register basis, and where the pointer actually sits**

### **2.1 The slot ordering is not free**

Both involutions are written in coordinates, and coordinates on the register are not a convention here — they are fixed by the corpus. Three PROVEN statements pin them:

(a) ZS-F0 Definition 8.11: slot 0 is the β₀ physical (ℤ₂-even) mode, slot 1 the ℤ₂-odd mode. These are the two Z-sector modes.  
(b) ZS-M6 §2.1: the Z-sector eigenvalues are 0 (β₀ physical) and 1 (ℤ₂-odd), so the bare Z-block is L\_Z \= diag(0, 1\) \= ½I − ½J\_seam|\_Z. This identity is only true if J\_seam|\_Z \= diag(+1, −1) — that is, if the two Z-slots are the parity *eigenmodes*, not the two nodes. So the corpus's own Z-sector seam parity is exactly J\_Z restricted, and the register basis is fixed twice over (check N1).  
(c) ZS-F0 §9: the three-layer fixed-point decomposition names the boundary vector |0⟩\_Z as the BV-BFV representation of the Z-Anchor and the bulk dynamic vector |v\_W⟩ \= (|0⟩ − i|1⟩)/√2 as the Wilson-loop dominant eigenvector, and states that the dynamical attractor of W is the two-dimensional Z subspace. The subspace in question is span{|0⟩, |1⟩}.

A third naming layer is worth recording while it is in view. The corpus uses “seam” for three distinct objects: the 2×2 Z-sector parity J\_seam|\_Z \= diag(+1, −1) of ZS-M54 and ZS-M6; the register-wide J\_Z \= I₁₁ − 2|1⟩⟨1| of ZS-F0 Def 8.11, which is that parity extended by the identity on X ⊕ Y; and the register-wide J|j⟩ \= |10 − j⟩ of ZS-F0 Thm 8.5, which is a different operator entirely. The first two agree on the Z-sector; the third does not act on it at all. ZS-M56 conflated the first two by name, which was harmless; the seed conflated the second and third by coordinates, which was not.

Therefore, in the one basis in which J\_Z is the operator ZS-F0 Def 8.11 says it is, the Z-sector — the pointer system, the arena on which Z\_path and the seam sit as anticommuting observables (ZS-M54 Lemma M54.8a) — is **ℋ\_Z \= span{|0⟩, |1⟩}**.

### **2.2 Theorem M57.1 (Seam Non-Localisation of the Pointer)**

**Theorem M57.1.** \[DERIVED\] Let ℋ\_Z \= span{|0⟩, |1⟩} ⊂ ℂ¹¹ be the corpus Z-sector in the ZS-F0 §8 register basis, and let J|j⟩ \= |10 − j⟩. Then

J ℋ\_Z \= span{|9⟩, |10⟩} ,  J ℋ\_Z ∩ ℋ\_Z \= {0} ,  ⟨v, Jv⟩ \= 0 for every v ∈ ℋ\_Z.

Proof. J|0⟩ \= |10⟩ and J|1⟩ \= |9⟩ by definition, and {9, 10} ∩ {0, 1} \= ∅, so the two spans are orthogonal. For v \= a|0⟩ \+ b|1⟩, Jv \= a|10⟩ \+ b|9⟩ and ⟨v, Jv⟩ \= 0\. Verified: checks N2, N3, N5, with max |⟨v, Jv⟩| over unit v ∈ ℋ\_Z equal to 6.9×10⁻¹⁷ over 4000 draws.

Two corollaries are immediate and both are load-bearing.

**Corollary M57.1a.** No nonzero vector of ℋ\_Z is a J-eigenvector. Since an involution is diagonalisable, every J-invariant subspace is a sum of eigenspaces; so any J-invariant subspace containing ℋ\_Z contains ℋ\_Z ⊕ Jℋ\_Z. \[DERIVED\]

**Corollary M57.1b.** J admits no restriction to ℋ\_Z. There is therefore no operator J\_S on the pointer system induced by the seam involution, and no J-grading of the pointer exists to be preserved. \[DERIVED\]

### **2.3 Theorem M57.2 (the D₄-invariant hull of the pointer)**

**Theorem M57.2.** \[DERIVED\] The smallest J-invariant — hence the smallest D₄-invariant — subspace of ℂ¹¹ containing the pointer ℋ\_Z is ℋ\_Z ⊕ Jℋ\_Z \= span{|0⟩, |1⟩, |9⟩, |10⟩}, of dimension 4\. In particular no two-dimensional D₄-invariant subspace contains the pointer.

Proof. By Corollary M57.1a any J-invariant V ⊇ ℋ\_Z contains ℋ\_Z ⊕ Jℋ\_Z, which is four-dimensional by Theorem M57.1; and that space is J-invariant because J² \= I, and J\_Z-invariant because J\_Z is diagonal in the slot basis. Since D₄ \= ⟨J, J\_Z⟩ it is D₄-invariant. Verified: check N4, dim \= 4\.

This is the whole obstruction, and it has a different character from its two predecessors. Theorem M56.21′ says a certain equivariant isometry cannot exist because a multiplicity is too small. Theorem M57.2 says that the **equivariance condition itself cannot be written down** for the object it was meant to constrain: a D₄-equivariant subsystem decomposition whose system factor is the pointer would require the pointer to be a D₄-representation, and it is not one. Doubling it to make it one costs the very thing the construction was for — the environment would have to be the pointer's own seam image, which is not an environment but the other half of a four-dimensional invariant block.

### **2.4 The seed's J-compatible sector split is a different register**

Seed §1.3 offers a J-compatible realisation of the corpus sector dimensions: Z on the seam pair (4, 6), X on the pair (3, 7\) plus the fixed slot |5⟩, Y on the three pairs (0, 10), (1, 9), (2, 8). The arithmetic is right — the multiplicities sum to (6, 5\) and the dimensions to (3, 2, 6\) — and check D14 of the seed suite reproduces it. But it is not the corpus register, and combining it with J\_Z \= I₁₁ − 2|1⟩⟨1| combines two objects written in different bases.

The test is one line. Under the corpus grading, restrict J\_Z to each seam pair:

Table 2.1. The corpus grading J\_Z restricted to each seam pair (check N11). Only the pair (1, 9\) carries a non-central grading; every other pair carries \+I and therefore has zero odd operators, failing constraint 2 of Table 9.1.

| Seam pair | J\_Z restricted | Central? | Odd operators | Charge constraint (M56.22′) |
| ----- | ----- | ----- | ----- | ----- |
| (4, 6\) — seed's Z-sector | diag(+1, \+1) | yes | 0 | FAILS |
| (3, 7\) — seed's internal environment | diag(+1, \+1) | yes | 0 | FAILS |
| (2, 8\) | diag(+1, \+1) | yes | 0 | FAILS |
| (0, 10\) | diag(+1, \+1) | yes | 0 | FAILS |
| (1, 9\) — the E-block | diag(−1, \+1) | no | 2 | satisfied |

So the seed's §1.4 counterexample — an explicit grading-preserving isometry with ‖W(J\_S ⊗ J\_E) − JW‖ \= 0 built on the pairs (4, 6\) and (3, 7\) — is a correct statement about J and a vacuous one about the corpus. Both of its factors carry the central grading under J\_Z; by Theorem M56.22′ each has zero odd operators; the vertex Z\_path ⊗ B has no B to be built from. The seed scored that candidate 2 of 4 on the strength of J's restriction. Under the corpus grading it scores **0**. Table 9.2 records the corrected scoreboard.

## **§3. The D₄ decomposition, retained as mathematics, and the E-block located**

### **3.1 Theorem M57.D.1**

The representation theory the seed imported is correct and is kept, with its physical application withdrawn in §4. The import is standard and is used without re-proof.

**Imported statement.** \[IMPORTED-PROVEN\] For a finite group G and G-representations ℋ\_S, ℋ\_E and V, a G-equivariant isometry ℋ\_S ⊗ ℋ\_E ↪ V exists if and only if mult\_ρ(ℋ\_S ⊗ ℋ\_E) ≤ mult\_ρ(V) for every irreducible ρ (Frobenius reciprocity with Schur's lemma; Serre 1977, §2.3). For G \= ℤ₂ this reduces to the two inequalities of which Theorem M56.21′ uses one.

**Theorem M57.D.1 (Register D₄-decomposition).** \[PROVEN\] Let J|j⟩ \= |Q−1−j⟩ and J\_Z^{(k)} \= I\_Q − 2|k⟩⟨k| on ℂ^Q with Q odd and k ≠ (Q−1)/2, and let G \= ⟨J, J\_Z^{(k)}⟩ ≅ D₄ (ZS-F0 Thm 8.13). Then

ℂ^Q \= ((Q−1)/2) A₁ ⊕ ((Q−3)/2) B₂ ⊕ 1·E ,  mult(A₂) \= mult(B₁) \= 0 ,

for every odd Q and every admissible k. For **Q** \= 11 this reads ℂ¹¹ \= 5A₁ ⊕ 4B₂ ⊕ E, with 5 \+ 4 \+ 2 \= 11\.

Proof. The seam pairs {j, Q−1−j} are J-orbits. On the pair containing k the two generators act as the two anticommuting reflections of D₄, giving E. On every other pair J\_Z^{(k)} acts as the identity, so the pair splits into a J-even A₁ and a J-odd B₂. The fixed slot |(Q−1)/2⟩ is fixed by both and gives A₁. There are (Q−1)/2 seam pairs in all, one of which carries E; so the count is one E, (Q−3)/2 \+ 1 \= (Q−1)/2 copies of A₁, and (Q−3)/2 copies of B₂, and (Q−1)/2 \+ (Q−3)/2 \+ 2 \= Q. Verified: check D8b.

Table 3.1. The decomposition swept over odd Q (checks D8, D8b), computed from the group generated at each Q. mult(E) \= 1 is generic in Q, not a property of 11; the dimensions close at Q in every column.

| Q | 5 | 7 | 9 | 11 | 13 | 15 | 17 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| mult(A₁) \= (Q−1)/2 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
| mult(B₂) \= (Q−3)/2 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| mult(E) | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| total dimension | 5 | 7 | 9 | 11 | 13 | 15 | 17 |

**Erratum to the seed, registered.** Seed §2.2 printed the closed form as ((Q+1)/2)A₁ ⊕ ((Q−1)/2)B₂ ⊕ E, which sums to dimension Q \+ 2 and is therefore impossible. Its Table 2.1 was correct; only the theorem line was wrong, and the mismatch is visible from the seed's own next sentence (“For Q \= 11 this reads 5A₁ ⊕ 4B₂ ⊕ E, and 5 \+ 4 \+ 2 \= 11”, with 5 ≠ (11+1)/2). The corrected closed form is above and is verified at every odd Q from 5 to 17 by check D8b. This is a small error and it is recorded rather than silently fixed, because the discipline that catches the large ones is the same discipline that catches this.

### **3.2 Theorem M57.3 — the E-block is not an abstract choice**

The seed's author registered, explicitly and correctly, that selecting the pointer to carry E in Theorem M57.D.2 was a judgement rather than a derivation, and asked that the gap be gated. The gap is discharged here, and not by justifying the choice — by removing it.

**Theorem M57.3 (Location of the E-block).** \[DERIVED\] Under G \= ⟨J, J\_Z^{(k)}⟩ the unique E-isotypic component of ℂ^Q is span{|k⟩, |Q−1−k⟩}. For the corpus register (Q \= 11, k \= 1\) it is span{|1⟩, |9⟩}: the ℤ₂-odd Z-mode together with its seam image.

Proof. The E-isotypic projector is P\_E \= (dim E/|G|) Σ\_g χ\_E(g)\* g \= (2/8) Σ\_g χ\_E(g) g. Evaluating on the slot basis, every summand acts diagonally except on the orbit {k, Q−1−k}, and the character values (2, −2, 0, 0, 0\) annihilate all other blocks. Verified: check N8, supp(P\_E) \= {1, 9}, tr(P\_E) \= 2.000000; check N10 sweeps all ten admissible k and returns (mult A₁, mult B₂, mult E) \= (5, 4, 1\) with E \= span{|k⟩, |10−k⟩} in every case.

**Corollary M57.3a.** \[DERIVED\] The E-block contains the odd Z-mode |1⟩ and does not contain the even Z-mode |0⟩. Hence E ≠ ℋ\_Z and E ∩ ℋ\_Z is one-dimensional. Neither of the two candidate D₄-structures the seed weighed — E, or A₁ ⊕ B₂ — is the pointer. The choice the seed's author flagged as unjustified is moot: both branches describe objects that are not the pointer system, so neither branch can carry an obstruction about it.

### **3.3 Anti-numerology, executed before any claim**

Three coincidences are available in this section and all three are refused.

(i) (n₊, n₋) \= (6, 5\) is not informative. For any odd n the flip involution has multiplicities ((n+1)/2, (n−1)/2). The agreement of 6 with dim Y \= 6 carries no information beyond “Q is odd”. Verified over n \= 5 … 17 (check D12). NON-CLAIM.

(ii) mult(E) \= 1 is not a property of 11\. It holds for every odd Q tested. Presenting it as a fact about the number 11 would be numerology and would invite correct dismissal. It is stated here as structural, and gate F-M57.13 fires on any presentation otherwise.

(iii) No match between D₄ multiplicities and corpus constants is reported. By Theorem M57.D.1 the decomposition is forced, so every such match is a theorem about odd integers, not about Z-Spin. Specifically: that mult(B₂) \= 4 equals |V₄|, that mult(A₁) \= 5 equals the number of Platonic solids, and that dim X \= 3 equals the number of nontrivial characters appearing, are all barred in advance. Gate F-M57.16.

### **3.4 What this gives ZS-F0 Conjecture 8.14, and what it does not**

ZS-F0 Conjecture 8.14 (HYPOTHESIS, explicitly left open) proposes that the order-four element r \= J·J\_Z corresponds structurally to the quarter turn i⁴ \= 1 of i-tetration. The characters give r order 1 on A₁, order 2 on B₂, and order 4 only on E (check D11). With mult(E) \= 1, the register contains exactly one quarter turn — and Theorem M57.3 now says where it is.

**Corollary M57.D.3′.** \[DERIVED\] The register's unique honest quarter turn acts on span{|1⟩, |9⟩}: the plane spanned by the ℤ₂-odd Z-mode and its seam image. If the correspondence of Conjecture 8.14 holds, the i-tetration rotation of the register is carried by the odd Z-mode paired across the seam — and by nothing else.

This is worth stating because the odd Z-mode is exactly the object ZS-M54 identified as the seam-odd complement of the bright mediating mode, and exactly the object whose identification as the which-path record ZS-M54 v1.7 withdrew as a NON-CLAIM. The corpus therefore has one two-dimensional plane on which the quarter turn is honest, and the record-mode candidate occupies half of it. That is suggestive and it is not a derivation. **Conjecture 8.14 is not claimed closed**: the explicit register representation of the i-tetration linearisation remains unperformed, and gate F-M57.15 fires on any claim otherwise.

## **§4. Gate F-M57.11 resolved — J\_Z only, by domain**

### **4.1 The resolution**

Assemble §2. The QND vertex is H\_int \= Z\_path ⊗ B\_E, with Z\_path the which-path observable on the pointer system. The selection rule requires H\_int to be even under whatever grading the pointer system carries and the Hamiltonian respects.

Table 4.1. The trichotomy, resolved (checks N6, N7, N12). The decisive column is the first, and it is a fact about domains, not about dynamics.

| Involution | Restricts to ℋ\_Z? | Restriction | Bulk symmetry? (ZS-F0 Thm 8.7) | Imposes a selection rule? |
| ----- | ----- | ----- | ----- | ----- |
| J\_Z \= I₁₁ − 2|1⟩⟨1| | yes | diag(+1, −1), non-central, 2 odd operators | yes — the action-level ε → −ε of ZS-S1 §5.2 | YES. Z\_path is odd; the rule bites; q\_R \= 1 blocks. |
| J: |j⟩ ↦ |10−j⟩ | no — Jℋ\_Z ∩ ℋ\_Z \= {0} | does not exist | no — ‖\[J, L\]‖\_F ≈ 2.94 | NO. There is nothing on the pointer for it to grade. |
| D₄ \= ⟨J, J\_Z⟩ | no | does not exist on a two-dimensional pointer | no (contains J) | NO. D₄-equivariance is not formulable for this system factor. |

**Resolution of F-M57.11.** \[DERIVED\] The QND vertex must respect J\_Z only. The trichotomy does not resolve by weighing which grading is physically relevant; it resolves because two of the three branches presuppose an operator on the pointer system that does not exist.

### **4.2 The pre-registered outcomes, adjudicated**

| Outcome | Trigger as pre-registered in Seed §11 | Verdict |
| ----- | ----- | ----- |
| F — D₄ CLOSURE | M57.D.2 proved at full strength and F-M57.11 resolves to “both”. | DOES NOT FIRE. F-M57.11 resolves to “J\_Z only” (§4.1) and M57.D.2 is not formulable (§4.3). |
| G — BOUNDARY REDIRECTION | F-M57.11 resolves to “J only”: the record grading is the seam. | CLOSED-NEGATIVE. The pointer admits no J-grading (Cor. M57.1b). The seed's “largest possible outcome, and the least likely” is excluded outright, not merely disfavoured. |
| H — ALL ROUTES FAIL | No route closes and F-M57.11 stays open. | DOES NOT FIRE. F-M57.11 does not stay open. |
| A, B, C, D, E | Route S or Route B closures and failures. | DO NOT FIRE. Neither route is executed here (§11, §12); both remain OPEN with their specifications sharpened. |

The paper's outcome is therefore the branch the seed itself pre-registered inside F-M57.11 — “If only J\_Z, ZS-M56 stands as published (under a corrected name)” — together with the two closures F′ and G′ that branch forces. No outcome is added after the fact; adding one would fire gate F-M57.17.

### **4.3 Theorem M57.D.2, withdrawn**

Seed Theorem M57.D.2 (D₄ Multiplicity Obstruction) proposed: let the pointer carry E; let ℋ\_E be any two-dimensional environment with a non-central grading; then no D₄-equivariant isometry ℋ\_S ⊗ ℋ\_E ↪ ℂ¹¹ exists, for either D₄-structure on ℋ\_E. The character arithmetic is correct — E ⊗ E \= A₁ ⊕ A₂ ⊕ B₁ ⊕ B₂ needs A₂ and B₁ which the register lacks entirely, and E ⊗ (A₁ ⊕ B₂) \= 2E needs two copies of E where there is one (checks D9, D10). **The arithmetic is retained; the physical statement is withdrawn.**

**Status: M57.D.2 as a physical obstruction on the Z-Spin mediator vertex is NON-CLAIM.** Its premise is that the pointer carries E. By Corollary M57.3a the pointer is span{|0⟩, |1⟩} and E is span{|1⟩, |9⟩}; these are distinct two-dimensional subspaces sharing a line. The premise is not an unjustified choice — it is false in the corpus register. As pure representation theory the statement is PROVEN and is retained in Appendix B as a lemma about D₄-modules, where it may be reused if some future object genuinely carries E.

This is the fourth successive version of this line in which the central proposed theorem does not survive. Recording the pattern honestly: ZS-M56 v1.0 failed for want of dimensions, v1.6 and v1.7 for confusing a lone odd term with an even composite, v1.8 survived, and the seed's proposed v1.8-successor fails on a domain condition. The one class of statement that has survived every round is the class that constrains a multiplicity of a grading that actually acts — M56.21′ — and Theorem M57.1 is of that class.

### **4.4 What ZS-M56 v1.8 now requires**

Exactly one thing: a naming correction. Its title should read “Why the Q \= 11 register admits no Z-internal-ℤ₂-preserving tensor subsystem”, and every occurrence of “the seam ℤ₂” in the sense of J\_R \= I₁₁ − 2|1⟩⟨1| should read “the Z-internal ℤ₂”. Whether that is an erratum to v1.8 or a v1.9 is not this paper's call. Its theorem, its inequality, its scope and its 101 checks are unaffected; check X5 reproduces q\_R(J\_Z) \= 1 \< 2 independently.

Rule R10 is strengthened accordingly and is registered as **R10′**: every ℤ₂, involution or grading must be named by its defining formula, its corpus definition number, **and the register basis in which that formula holds**. The present finding is not a naming error — the seed had already caught that — but a basis error one level below it, and only the strengthened rule catches it.

## **§5. Theorem M57.P — the Real-Multiplier Lemma**

This is the paper's only positive theorem and its cleanest proof-bearing check. It is λ-free: no comparison-layer quantity enters its statement, its proof, or its verification. It is also the one result of either parent seed that no part of §2–§4 disturbs, because it is about an external carrier qubit and its own grading, not about the register.

### **5.1 Statement and proof**

**Theorem M57.P (Real-Multiplier Lemma).** \[PROVEN\] Let U \= P₀ ⊗ W₀ \+ P₁ ⊗ W₁ be a QND controlled unitary on ℋ\_S ⊗ ℋ\_E, with P₀, P₁ the pointer projectors. Suppose U preserves the total grading J\_S ⊗ J\_E, and suppose J\_S exchanges the pointer projectors, J\_S P₀ J\_S \= P₁. Suppose further that the carrier state is grading-invariant, \[ρ\_E, J\_E\] \= 0\. Then the coherence multiplier

γ \= Tr(ρ\_E W₁† W₀) is real.

Proof. Conjugating U by J\_S ⊗ J\_E and using J\_S P₀ J\_S \= P₁ gives P₁ ⊗ J\_E W₀ J\_E \+ P₀ ⊗ J\_E W₁ J\_E; equating with U and matching the pointer blocks gives W₁ \= J\_E W₀ J\_E. Then, using ρ\_E† \= ρ\_E, the cyclicity of the trace, invariance of the trace under conjugation by J\_E, J\_E² \= I, and \[ρ\_E, J\_E\] \= 0 in that order,

γ\* \= Tr(ρ\_E W₀† W₁) \= Tr(ρ\_E W₀† J\_E W₀ J\_E) \= Tr(J\_E ρ\_E W₀† J\_E W₀) \= Tr(ρ\_E J\_E W₀† J\_E W₀) \= Tr(ρ\_E W₁† W₀) \= γ.

Verified three ways. Check P1 draws 1000 Haar-random W₀, imposes W₁ \= J\_E W₀ J\_E and block-diagonal ρ\_E, and returns max |Im γ| \= 8.47×10⁻¹⁷. Check P2 verifies the middle equality of the proof as an identity over 200 draws, residual 1.4×10⁻¹⁶. Check P3 is the control that makes the theorem non-vacuous: replacing ρ\_E by a generic pure carrier state, which is not grading-invariant, gives max |Im γ| \= 0.988. The hypothesis is load-bearing, not decorative.

### **5.2 Consequence for the corpus**

The locked multiplier has Im **λ** \= 0.6884532271, which is not small (check P4). Therefore:

**Corollary M57.P.1.** \[DERIVED-CONDITIONAL on the M57.P hypotheses\] No single exact grading-preserving QND collision with a grading-invariant carrier state generates the corpus coherence multiplier **λ**. At least one of the following is required: (i) a separate holonomy phase layer; (ii) a symmetry-breaking carrier state; (iii) a microscopic violation or extension of the assumed grading; (iv) a multi-stage or non-QND process outside the lemma's premises.

Option (i) is not merely preferred on grounds of taste — it is the option the parent already contains. ZS-M54 v2.1 splits its central arrow into (11a), the action/Hessian layer S\_ZS ⇒ (K\_Q, \[𝔊\_Z\], κ², C\_XZ, C\_ZY, J\_seam), and (11b), the reconstruction layer (K\_Q, **λ**, Z\_path) ⇒ (U\_Z, Φ^QND, T\_Z). The unimodular part of the multiplier is carried in ZS-M54 §8 by the Z-internal transit holonomy U\_Z, separately from the real amplitude κ. Theorem M57.P says that separation is forced: a graded collision layer can produce |**λ**| and cannot produce arg **λ**. The ZS-M54 layer split was a bookkeeping decision; it is now a theorem about what a symmetric collision can and cannot carry. That is a genuine promotion and it costs no free parameter.

**Scope, stated exactly.** M57.P constrains carriers, not channels. It does not say that Φ^QND has no dilation — ZS-M54 M54.19 constructs one explicitly. It says that a dilation whose carrier respects the grading exactly, with an invariant initial state, has a real multiplier. ZS-M54's W₁ \= \[\[λ̄, δ\], \[−δ, λ\]\] does not satisfy W₁ \= J\_E W₀ J\_E with W₀ \= I unless λ is real; the lemma and the construction are consistent, and the lemma explains which hypothesis the construction gives up.

## **§6. Route G — the layer verdict, and why Resolution 1 is closed**

### **6.1 What Seed Report B constructs, and the firewall violation**

Seed Report B builds a minimal external carrier qubit with a non-central involution J\_E \= σ\_z, an odd interaction operator B\_E \= σ\_x, and a record axis R\_E \= −i J\_E B\_E \= σ\_y, and shows that a single graded collision U\_D \= exp(−(i/2)θ\_D Z\_path ⊗ B\_E) reproduces the real dephasing channel and generates the ZS-M54 Eq. (13) informative instrument. Its construction script re-executes cleanly at 29/29 within the merged seed suite (39/39 overall, reproduced here as an independent regression).

The genuine achievement is the instrument. ZS-M54 inserted the informative instrument by hand as “one admissible representative”, with the selector explicitly OPEN (M54.13 proves it is not selectable at mean-operator level). Seed B derives that representative from a graded interaction. But the collision angle is θ\_D \= arccos|**λ**| \= 0.4701208160, taken from the comparison layer, so the derived Kraus pair and ZS-M54 Eq. (13) have dependency sets that intersect in **λ**. That is a premise insertion, it is the seventh instance in this line, and it is what rules R1, R2 and gates F-M57.2 and F-M57.9 exist to catch. It is reported here as a CONTROL (check G4), never as evidence.

### **6.2 Theorem M57.G′ — the amplitude, not the angle, is the object**

The seed offered two honest resolutions: derive θ\_D from the action without λ (Resolution 1, preferred if achievable), or reclassify Route G as a representation theorem at the comparison layer (Resolution 2, honest fallback). The natural candidate for Resolution 1 was the ZS-S14 coupling geometry through κ² \= A/Q. This paper closes that candidate — but it closes exactly it, and no more, and the correction from the v1.0 draft is the point of this subsection.

**What the v1.0 draft got wrong, stated plainly.** The v1.0 Theorem M57.G claimed that θ\_D itself is not algebraic over ℚ(A, Q), by the step “θ\_D algebraic ⇒ cos θ\_D algebraic”. That step is false. By the Lindemann–Weierstrass theorem, for a nonzero algebraic argument θ the value cos θ is *transcendental* — for instance cos 1 \= 0.5403023059… is transcendental (check G3c). So the transcendence of cos θ\_D \= |**λ**| does not contradict θ\_D being algebraic; if anything it is exactly what an algebraic θ\_D would produce. The v1.0 statement is RETRACTED (Appendix C), and the correct object is not the angle but the amplitude.

**Theorem M57.G′ (Amplitude Non-Derivability).** \[DERIVED-CONDITIONAL on (H-TRANS)\] Assume (H-TRANS): |**λ**| is transcendental. Since **A** \= 35/437 and **Q** \= 11 are rational, every algebraic function of A and Q — rational arithmetic together with radicals — evaluates to an algebraic number. The amplitude |**λ**| \= cos θ\_D is transcendental, hence it is not such a function. Therefore no derivation of the collision that produces the coherence amplitude cos θ\_D as an algebraic expression in the locked constants — in particular the seed’s proposed route through κ² \= A/Q — can reproduce the corpus value. That class of Resolution 1 is CLOSED-NEGATIVE.

**Proof.** An algebraic function of the algebraic numbers A, Q returns an algebraic number (the algebraic numbers form a field closed under radicals). |**λ**| \= cos θ\_D is transcendental by (H-TRANS). A transcendental number is not algebraic, so it is not the value of any such function; in particular it is not cos θ\_D produced from A, Q algebraically.

**What is NOT closed.** Theorem M57.G′ closes the *amplitude* route — any derivation that first produces cos θ\_D as an algebraic combination of A and Q. It does not close the *angle* route: a construction that produces θ\_D directly as an algebraic number is not excluded, and would simply carry a transcendental cosine (as any nonzero algebraic angle does). Whether such a construction exists is OPEN, and gate F-M57.G registers it. The “class” that is closed is precisely the class the seed named — “through κ² \= A/Q” is an amplitude relation — and no more. This is weaker than the v1.0 claim, and it is correct.

**Corollary M57.G.1 (Niven).** \[DERIVED-CONDITIONAL on (H-TRANS)\] θ\_D is not a rational multiple of π. The cosine of a rational multiple of π is always algebraic (a root of a Chebyshev polynomial with rational coefficients), whereas cos θ\_D \= |**λ**| is transcendental. So θ\_D \= 0.4701208160 is not a “nice” angle, which mildly disfavours but does not forbid a clean geometric derivation of it (check G3b).

### **6.3 Reducing (H-TRANS) to one corpus quantity, and the anti-numerology null**

(H-TRANS) is load-bearing and is imported, not proved here — so it is worth reducing it as far as possible to something the corpus already audits. It reduces to a single number.

**Lemma M57.G.0 (reduction).** \[DERIVED\] If η\_topo \= |z\*|² is algebraic, then |**λ**| is transcendental. Proof: the corpus identity |**λ**|² \= (π²/4)|z\*|² holds exactly (ZS-F0 Thm 8.9–8.10; check G2, residual 0.0). If |**λ**| were algebraic then |**λ**|² would be algebraic, and π² \= 4|**λ**|²/η\_topo would be a ratio of nonzero algebraic numbers, hence algebraic — contradicting the transcendence of π² (Lindemann).

This is the honest state of (H-TRANS): the corpus establishes z\* transcendental via Gelfond–Schneider (ZS-F0 §11.8.5), and Lemma M57.G.0 shows that the transcendence of the modulus |**λ**| — which is what Theorem M57.G′ actually needs — follows from the algebraicity of the single quantity η\_topo \= |z\*|² \= 0.3221188634. Whether η\_topo is algebraic is not settled by the loaded corpus; it is registered OPEN, and it is the exact residual on which Theorem M57.G′ rests. Gate F-M57.18 fires if the transcendence chain is downgraded; gate F-M57.G registers the residual.

A referee is entitled to ask what a search would have found. Two nulls were pre-registered and run. The first (check G2′ of the seed, retained) searched an algebraic-and-π family for the angle θ\_D and returned no hit; because that family contains π it can produce transcendental values, so its null neither proves nor refutes M57.G′ and is reported only for completeness. The second (check G3) is the one that matches the object of M57.G′: it searches the algebraic-in-(A, Q) family with no π for the amplitude |λ| \= cos θ\_D.

Table 6.1. The pre-registered amplitude null (check G3): the algebraic-in-(A, Q) family (a/b)·A^i·Q^j·κ^l, no π, i, j, l ∈ {−2,…,2}, values in (0, 2). The second and fourth rows are the ones that matter.

| Quantity | Value | Reading |
| ----- | ----- | ----- |
| family size | 9,869 | the amplitude search a formula-hunt would have run |
| hits within 1×10⁻⁴ of |λ| \= cos θ\_D | 0 | no algebraic-in-(A, Q) expression reproduces the amplitude |
| nearest miss | \> 1×10⁻⁴ | not a match at the stated tolerance |
| hits expected by chance | 0.99 | at this density a SINGLE hit would have carried no evidential content |

The last row disciplines the second: the family is dense enough near the amplitude that a single coincidence is expected roughly once. The search returning nothing is consistent with Theorem M57.G′ and is not independent evidence for it — the evidence is the transcendence argument, and the search is a control (check G3). Both are recorded.

### **6.4 Verdict**

**Route G sits at level L2.** Stated at exact strength: given **λ**, the informative instrument of ZS-M54 Eq. (13) is generated by a minimal graded collision at angle arccos|**λ**|, with the record axis R\_E \= −i J\_E B\_E fixed by Pauli closure rather than chosen. That removes an ansatz from ZS-M54 and it is worth publishing. It is not a construction, it must not be presented as one, and §0 declares the level before any computation so that it cannot be presented as one by drift.

What would reach L1: not an algebraic formula for the amplitude cos θ\_D, which §6.2 excludes, but a mechanism producing λ itself — a derivation in which the i-tetration multiplier enters the collision geometry as the Koenigs rate of the ZS-S14 slab rather than as a number, from which θ\_D would follow with its transcendental cosine intact. That is the same object F-M54-16′ asks for, and it is not supplied here. An angle-route derivation of θ\_D that bypasses the amplitude is not excluded by §6.2 and is registered OPEN (gate F-M57.G). §§7–9 then do something this line of papers has not done before: they read Theorem M57.G′ in the reverse direction, as a certificate rather than a closure.

## **§7. The reversal — reading the wall as a door**

### **7.1 The pattern of the stall, stated as a pattern**

Nine versions across ZS-M54, ZS-M56 and this paper searched for the odd carrier as a kinematic object: a tensor factor, a subspace, a register slot, a grading, a boundary polarization. Every one of those objects is acted on by a finite or abelian — hence amenable — symmetry group: the register D₄ has order 8, single-collision iteration is a ℤ-action, the seam pair structure is ℤ₂ × ℤ₂. Amenable actions admit invariant means; they are exactly the actions on which a total, finitely additive, invariant bookkeeping of records could in principle exist. The searches kept failing, and §§2–6 of this paper sharpened the failures into theorems. What no version asked is whether the DYNAMICS the corpus itself prescribes — the graded QND collision at the corpus angle — stays inside the amenable world at all.

### **7.2 The ZS-M50 precedent, and the flip performed here**

The corpus has one precedent for this kind of move. ZS-M49 proved the vertical direction of polygon tetration cannot realise the prime-orbit measure; ZS-M50 v1.3 then reread the same object horizontally — base dilation instead of iteration depth — and the gate H-ALG closed as a theorem, with a finite-register no-go (M50.NG) explaining precisely why the Q \= 11 register could not carry the horizontal object. The flip performed here has the same shape. Version 1.1 of this paper proved Theorem M57.G′: the collision amplitude |λ| \= cos θ\_D is transcendental (conditional on (H-TRANS)), and read it as a wall — no algebraic derivation of the amplitude from A and Q. Read in the other direction, the same sentence is the HYPOTHESIS of a classical freeness theorem: rotations by an angle whose cosine is transcendental, about perpendicular axes, generate a free group of rank 2 (§8.2). The wall is the door. The transcendence that blocked the formula-hunt is exactly what certifies that the collision dynamics escapes every amenable object the nine versions searched.

### **7.3 The three reader questions this section owes an answer**

This version was written against three questions posed to the line, and it is honest to display them before the theorems. **(Q1)** The corpus has treated points (pointer outcomes, register slots) and lines (edges of the mediator graph 𝔊\_Z, walk chains); what is a face? **(Q2)** Do accumulated point-line motions compose into a face, and faces into a space? **(Q3)** Banach–Tarski doubles a ball using non-measurable pieces produced by free rotations; is the point-line motion of the mediator such a rotation? The answers are in §§8–10, and one correction to (Q3) is owed immediately: a rotation is never itself non-measurable — rotations are smooth maps. What Banach–Tarski requires is that the GROUP generated by the rotations is free (hence non-amenable), and then the PIECES of the paradoxical decomposition are non-measurable. The corrected form of (Q3) is: does the collision dynamics generate a free rotation group? §8 proves that it does.

Table 7.1. Walls reread as doors. Every row's left cell is a result this line already holds; the right cell is what the same result says when read in the direction of §§8–9.

| Result as a wall | Same result as a door |
| ----- | ----- |
| M57.G′ (v1.1): |λ| \= cos θ\_D is not an algebraic function of A, Q. | cos θ\_D transcendental is the hypothesis of the free-rotation theorem: the collision angle is a FREE angle (§8.3). |
| M56.22′: the carrier grading must be non-central, forcing exactly 2 odd operators. | The 2 odd operators ARE the two generators; the free group has rank 2 because the odd space has dimension 2 (§8.1). |
| M57.P: a symmetric collision has a real multiplier; the phase layer is separate. | Each single collision is mean-invisible; the free structure lives strictly below the mean layer (§9.2, check F9). |
| M57.1–M57.3: the seam does not act on the pointer; the register hull is 4-dimensional. | The kinematic register group is finite (D₄, amenable). The free object could never have been found by a register search, because it does not live there (§8.4, check F10). |
| M54.13: the mean channel cannot select the instrument. | The mean channel cannot even see WHICH free generator acted: the two collisions induce identical pointer channels (§9.2). |

## **§8. The Free Collision Theorem**

### **8.1 The canonical generator pair — the odd space itself**

**Theorem M57.F.0 (Canonicity of the pair).** \[DERIVED\] Let J\_E be a non-central grading of the two-dimensional carrier (M56.22′'s constraint 2), taken as σ\_z without loss of generality. The J\_E-odd Hermitian operator space is exactly span\_ℝ{σ\_x, σ\_y}, of dimension two (check F1). Choose any unit direction in it, B\_E \= cos α σ\_x \+ sin α σ\_y; then its Pauli-closure partner R\_E \= −iJ\_E B\_E is the perpendicular direction in the same plane, and the pair {B\_E, R\_E} is an orthonormal frame of the odd plane. Both vertices Z\_path ⊗ B\_E and Z\_path ⊗ R\_E are total-grading-even and QND, so BOTH are admissible collisions at the same corpus angle θ\_D, and no third odd direction exists. Conditioned on a pointer eigenstate they act on the carrier Bloch sphere as rotations by ±θ\_D about PERPENDICULAR axes — automatically, because distinct directions in the odd plane anticommute.

**Exactly how canonical, stated precisely.** The v1.2 draft called this “zero choices”. That was an overstatement and is corrected here. The odd PLANE is forced by the charge constraint, and so is the perpendicularity of the pair within it; what is not forced is the angle α that fixes the first axis, a continuous freedom generated by the U(1) centraliser of J\_E. The correct statement is therefore: the generator pair is *canonical up to the U(1) gauge that stabilises the grading*. This does not affect any result in §§8–9: rotating α conjugates the whole configuration by an element of that U(1), and conjugate groups are simultaneously free, paradoxical and dense. It does matter for physics: an action-level instrument selector must eventually fix α, and nothing in this paper fixes it. M57.F.0 is accordingly registered ALGEBRAIC / DERIVED-CONDITIONAL on a chosen odd direction, not DERIVED outright.

This resolves in passing why the pair could not be discarded as an ansatz: discarding either generator amounts to imposing a superselection the corpus nowhere supplies, and M54.13 already proves the mean channel cannot perform that selection.

### **8.2 The specialization lemma and the Świerczkowski anchor**

**Lemma M57.F.L (Specialization).** \[PROVEN\] Fix a reduced word w in the letters R\_x(θ)^{±1}, R\_y(θ)^{±1} and write c \= cos θ, s \= sin θ. Every matrix entry of w is P(c) \+ s·Q(c) with P, Q ∈ ℤ\[c\] (the generators have such entries and the form is closed under products, using s² \= 1 − c²). Suppose w evaluates to the identity at some θ₀ whose cosine c₀ is transcendental. For each entry, (v − P(c₀)) \= s₀ Q(c₀) with v the identity entry; squaring, (v − P(c₀))² − (1 − c₀²) Q(c₀)² \= 0, a polynomial with integer coefficients vanishing at the transcendental c₀, hence the zero polynomial: (v − P(x))² \= (1 − x²) Q(x)² in ℤ\[x\]. The left side has even multiplicity at every irreducible factor; the right side has odd multiplicity at (1 − x) and (1 \+ x) unless Q ≡ 0\. So Q ≡ 0 and P ≡ v identically — for every entry — which means w(θ) \= I holds for ALL θ.

**Prior external mathematics, stated before the theorem.** The general fact — two rotations through the same angle about perpendicular axes generate a free group of rank 2 under a transcendence condition on the angle — is due to de Groot (1956) \[IMPORTED-PROVEN\], whose condition is that tan²(θ/2) be transcendental. That condition is EQUIVALENT to ours: tan²(θ/2) \= (1 − cos θ)/(1 \+ cos θ), and if this were algebraic then cos θ \= (1 − t)/(1 \+ t) would be algebraic too (check C7). So Theorem M57.F.1 below is an APPLICATION of de Groot's theorem at the corpus angle, not a new general theorem, and the v1.2 draft was wrong not to say so. Lemma M57.F.L is retained because it is self-contained and machine-auditable, not because it is novel. What is new here is only the identification of θ\_D as an angle satisfying the hypothesis, via Theorem M57.G′.

**Anchor (Świerczkowski, 1958).** \[IMPORTED-PROVEN\] At θ \= arccos(1/3) the two rotations about perpendicular axes generate a free group of rank 2\. The classical certificate is arithmetic: a reduced word applied to (0, 1, 0\) yields a vector (a√2, b, c√2)/3ⁿ with integers a, b, c and 3 ∤ b, hence never (0, 1, 0\) again. Check F2 verifies this EXACTLY — integer arithmetic, no floats — for all 118,096 reduced words of length ≤ 10\. Consequently no reduced word satisfies w(θ) \= I for all θ, which is exactly the case Lemma M57.F.L needs to exclude.

### **8.3 The theorem**

**Theorem M57.F.1 (Free Collision Theorem).** \[DERIVED-CONDITIONAL on (H-TRANS)\] Let G\_D \= ⟨R\_x(θ\_D), R\_y(θ\_D)⟩ ⊂ SO(3) be the group generated by the two admissible graded collisions of §8.1, conditioned on a pointer eigenstate, at the corpus angle θ\_D \= arccos|**λ**|. Under (H-TRANS) — |**λ**| \= cos θ\_D transcendental, the same import Theorem M57.G′ carries — G\_D is FREE of rank 2\. Proof: a nontrivial relation is a reduced word with w(θ\_D) \= I; by Lemma M57.F.L this forces w(θ) \= I identically; the Świerczkowski anchor refutes that at cos θ \= 1/3.

**Falsification equivalence, stated exactly.** Freeness is falsified only by exhibiting a reduced word with w(θ\_D) \= I — and by Lemma M57.F.L any such word constitutes a PROOF that cos θ\_D \= |**λ**| is algebraic, i.e. a refutation of (H-TRANS) and with it of Theorem M57.G′. The two theorems stand or fall together at a single point, and that point is the corpus's own transcendence budget (gate F-M57.F1; the residual is η\_topo, exactly as in §6.3). Conversely freeness does NOT require transcendence — the 1/3 anchor is algebraic and free — so a future unconditional proof is not excluded and is registered (gate F-M57.F2). Numerically, every one of the 13,120 reduced words of length ≤ 8 stays at Frobenius distance ≥ 0.139 from the identity at θ\_D, and 300 random words of length 15–40 stay ≥ 0.44 away (check F3).

### **8.4 What the theorem locates, and where the free object lives**

**Corollary M57.F.1a (kinematics finite, dynamics free).** \[DERIVED-CONDITIONAL\] The register's kinematic SYMMETRY GROUP ⟨J, J\_Z⟩ ≅ D₄ has order 8 and is amenable; G\_D is free, hence infinite and non-amenable. Therefore G\_D is not contained in — and admits no injection into — the finite register symmetry group. Check F10 exhibits 4,373 pairwise-distinct collision words of length ≤ 7 against the register's 8 elements.

**A statement the v1.2 draft got wrong, corrected.** v1.2 wrote that “the free object cannot be realised inside any finite register”. That is false, and the falsehood is visible in this very paper: F₂ embeds faithfully in SO(3) ⊂ GL(3, ℝ), and §8 realises G\_D concretely by 3 × 3 real matrices acting on the two-dimensional carrier. Finite DIMENSION is no obstruction to freeness; only a finite GROUP is. The corrected statement is the one above: the free collision group cannot be contained in the finite kinematic symmetry group D₄, although it acts faithfully on the finite-dimensional carrier. The ZS-M50 analogy is correspondingly narrowed: M50.NG concerns proper isometries in finite dimension, a different obstruction, and is cited here as a structural rhyme rather than as the same theorem. Relatedly, v1.2 asserted that this is WHY nine versions of kinematic search failed. That causal claim is not proved and is withdrawn; what is proved is the compatibility statement — a search restricted to objects carrying amenable symmetry groups could not have exhibited a free group as such a symmetry, and the searches were so restricted.

**Corollary M57.F.1b (density).** \[DERIVED-CONDITIONAL\] The closure of G\_D in SO(3) is a closed subgroup containing a rank-2 free group; the closed subgroups of SO(3) are finite, conjugates of SO(2) or O(2), or SO(3) itself \[IMPORTED-PROVEN\], and only SO(3) contains a non-virtually-abelian subgroup. Hence G\_D is DENSE in SO(3): the accumulated collision words generate, in the limit, the full rotation symmetry of the carrier sphere (equidistribution proxy: check F11).

**Registered connection to ZS-A9.** The corpus already carries an amenability functor Φ: F₂ → D₄ (ZS-A9 §3, registered DERIVED in the ZS-M35/M36 functor tables, which are loaded). Until this paper the domain F₂ was an external template. Theorem M57.F.1 realises it: the free group is generated by the corpus's own collision pair, and the amenable target is the corpus's own register group. Whether the specific homomorphism of ZS-A9 §3 matches the natural surjection G\_D → D₄ cannot be checked here — the body of ZS-A9 is not loaded — and is registered as an audit item (Table 10.1), per rule R6.

Table 8.1. The theorem's executable footprint (Block F of Appendix A). Every number is from the seed-57 run.

| Object | Value | Check |
| ----- | ----- | ----- |
| exact 1/3 certificate: reduced words ≤ 10, all non-identity | 118,096, min|b| \= 1, zero failures | F2 |
| θ\_D words ≤ 8: minimum distance from I | 0.138957 (13,120 words) | F3 |
| random words, length 15–40 | min distance 0.502999 (300 words) | F3 |
| specialization-lemma instances, formally non-identity | 400 / 400 | F4 |
| F₂ paradox identities on the word ball ≤ 9 | exact, 39,365 words | F5 |
| Kesten witness: ρ\_free(depth 9\) vs √3/2 vs ρ\_{ℤ²} | 0.835905 \< 0.866025 ≪ 0.997434 | F7 |
| distinct collision words ≤ 7 vs register order | 4,373 vs |D₄| \= 8 | F10 |

## **§9. The paradoxical carrier sphere, and the record obstruction**

### **9.1 From freeness to the paradox**

**Theorem M57.F.2 (Paradoxicality).** \[DERIVED-CONDITIONAL on (H-TRANS)\] The carrier sphere S² is G\_D-paradoxical. The chain is classical and fully imported: (i) F₂ is paradoxical as a group — the partition F₂ \= {e} ⊔ W(a) ⊔ W(a⁻¹) ⊔ W(b) ⊔ W(b⁻¹) satisfies a·W(a⁻¹) \= F₂ ∖ W(a) and b·W(b⁻¹) \= F₂ ∖ W(b), an exact combinatorial fact verified verbatim on the 39,365-word ball (check F5); (ii) off the countable set D of fixed points — each nontrivial word is a genuine rotation with exactly two fixed points (check F6) — the G\_D-action on S² ∖ D is free, so the group paradox transports to S² ∖ D \[Hausdorff 1914; Banach–Tarski 1924\]; (iii) D is absorbed by a countable-set rotation argument, giving S² \[Banach–Tarski 1924; Wagon Thm 3.9\]. Minimal piece counts are 4 for the sphere and 5 for the ball \[Robinson 1947\]; those integers are properties of F₂, not of Z-Spin, and are NON-CLAIMED as Z-constants (check F8).

### **9.2 The record obstruction, and what the mean layer can see**

**Corollary M57.F.3 (No total invariant record valuation).** \[DERIVED-CONDITIONAL on (H-TRANS)\] By Tarski's alternative \[IMPORTED-PROVEN: Tarski 1938; Wagon Thm 9.1\], a group action is paradoxical if and only if it admits NO finitely-additive invariant probability measure defined on ALL subsets. Hence: no assignment of record weights to all subsets of the carrier sphere can be simultaneously total, finitely additive, and invariant under the admissible collisions. Any total, non-contextual, collision-invariant valuation of which-path records on the carrier is impossible — a Kochen–Specker-flavoured obstruction, in the finite-dimensional KS register the corpus already inhabits (ZS-F0 §11), but produced here by non-amenability rather than by contextuality.

**Mean-invisible freeness.** The two generator collisions induce IDENTICAL pointer mean channels — the same real-multiplier dephasing, to machine precision — while their conditional carrier rotations do not commute (check F9). So the mean layer is blind to the ONE-STEP generator label. The v1.2 draft extended this to “the entire F₂ lives below the mean channel”, and that extension is FALSE and is withdrawn: with the carrier retained across collisions, composition is visible. Explicitly (check W1), γ(xx) \= cos 2θ\_D \= 2|**λ**|² − 1 \= 0.5895928759, whereas γ(xy) \= cos²θ\_D \= |**λ**|² \= 0.7947964380. The mean channel separates the two-letter words. The correct statement is: the one-step generator label is mean-invisible; the composed word is not.

**What replaces the overstatement is stronger, not weaker.** Theorem M57.P′ (Word-Level Real-Multiplier Lemma) \[DERIVED\]: with a grading-INVARIANT carrier state, EVERY word of the collision group has a REAL multiplier. Proof: γ(w) \= Tr(ρ\_E W₁(w)†W₀(w)) with W₁(w) \= J\_E W₀(w) J\_E, so γ \= Tr(ρ\_E J\_E W₀† J\_E W₀); using J\_Eρ\_E J\_E \= ρ\_E and cyclicity of the trace gives γ \= γ̄. Verified on 11 structured and 400 random words (check W2). This CLOSES the escape route that M57.P left open: one could have hoped a long word would accumulate a phase, and no word of any length does. The separation of ZS-M54’s (11a) and (11b) layers is therefore forced at every order, not merely at first order — and §11 shows what the phase must come from instead.

**Bearing on the selector.** Any selector functional that is total, finitely additive and collision-invariant is barred by Corollary M57.F.3; this constrains gate F-M54-12 without closing it. But the W1 computation also gives a positive handle that M54.13 did not have: since composed words are mean-distinguishable, word structure is partially observable at the mean layer, and a successor may test candidate histories against γ(xx) vs γ(xy) directly. That is registered, not developed.

### **9.3 A record-theoretic corollary — not a carrier-existence constraint**

The seed proposed a fourth constraint on the odd carrier (D₄-equivariance) and §4 withdrew it as not formulable. The v1.2 draft announced paradoxicality as “the real fourth specification constraint”. That is a category error and is corrected here: Tarski's alternative excludes only TOTAL finitely-additive invariant valuations defined on ALL subsets, and no physical carrier is required to carry such an object — Born probabilities are countably additive on a σ-algebra and are untouched (§9.4). Paradoxicality therefore constrains RECORD THEORY, not carrier existence: it says nothing about whether an admissible carrier exists (§11 shows one does) and it excludes no candidate. It is recorded below as a structural corollary at that strength and at no more.

Table 9.1. The record-theoretic corollary, stated at its exact strength. It is NOT a fourth row of the carrier specification (Table 18.1), and it disqualifies no candidate.

| \# | Constraint | Source |
| ----- | ----- | ----- |
| R1 | RECORD-THEORETIC COROLLARY (not a carrier constraint): any carrier satisfying constraints 1–3, coupled through the admissible graded QND collisions at θ\_D, has a free collision group and therefore supports NO total, finitely-additive, collision-invariant record valuation on all subsets. Record structure must live on the measurable σ-algebra, or on an amenable reduction (a single odd direction, ⟨R\_x(θ\_D)⟩ ≅ ℤ). Existence of an admissible carrier is unaffected — see §11. | Theorem M57.F.1–2, Corollary M57.F.3 \[DERIVED-CONDITIONAL on (H-TRANS)\] |

### **9.4 Scope — what is deliberately NOT claimed**

**The paradox lives strictly off the σ-algebra, and four NON-CLAIMs are registered before anyone else has to ask (declaration F12).** (i) Born probabilities and every CPTP statement of the corpus are untouched: Lebesgue measure on MEASURABLE sets is SO(3)-invariant and normalised, and every physical prediction lives there. (ii) No physical doubling of volume, energy, or state multiplicity is claimed; unitarity is not challenged. (iii) The 3-metric prohibition of ZS-A16 Theorem F is untouched — nothing here builds a metric. (iv) Route S is NOT blocked: its stochastic phase measure is countably additive on a circle, entirely outside the obstruction's scope. What the obstruction adds to Route S is a dichotomy, recorded in §16.5: either the record structure is σ-measurable, or the dynamics is reduced to an amenable subgroup, and Route S must eventually say which.

## **§10. The amenability ladder — points, lines, and the face layer**

### **10.1 Why points and lines worked, and where faces stall**

The three reader questions of §7.3 now have exact answers, and they are the same answer. Invariant total measures exist in low dimension: the isometry groups of the line and the plane are solvable, hence amenable, and Banach proved in 1923 that finitely-additive isometry-invariant total measures exist on ℝ¹ and ℝ² \[IMPORTED-PROVEN\]. That is why the corpus's point layer (register slots, pointer outcomes) and line layer (edges and walks of 𝔊\_Z, single-collision ℤ-iteration — the vertical λⁿ law of ZS-M54) never met a measure obstruction: their symmetry groups are amenable. The first place non-amenability CAN enter Euclidean geometry is the rotation group of the 2-sphere — and §8 proves the collision dynamics enters exactly there, at exactly the corpus angle.

Table 10.1. The amenability ladder, with the corpus layer occupying each rung, and the handoff.

| Rung | Symmetry | Amenable? | Corpus layer / status |
| ----- | ----- | ----- | ----- |
| points (0D) | finite groups | yes | register slots, pointer outcomes; D₄ kinematics (§§2–4) |
| lines (1D) | ℤ, D∞, Isom(ℝ) | yes (solvable) | 𝔊\_Z walks; single-collision iteration \= the vertical λⁿ law (ZS-M54) |
| plane (2D flat) | Isom(ℝ²) | yes (solvable) | Banach 1923: total invariant measures exist; no obstruction |
| FACE layer (S²) | SO(3) ⊇ G\_D ≅ F₂ | NO | the carrier Bloch sphere; paradoxical under the collision pair (§§8–9) — THIS PAPER |
| ball / space (3D) | SO(3) ⋉ ℝ³ | no | Banach–Tarski doubling; handed to ZS-M58 / ZS-A9 (§10.3) |

### **10.2 The face, answered**

**(Q1) What is a face?** The face layer of the mediation is the carrier Bloch 2-sphere — the state space of the dim-2 odd carrier that constraints 1–3 demand. It is not a 2-cell of a polyhedral complex (that object belongs to the ZS-S17/S20 cochain line and is untouched here); it is the first geometric layer on which the collision dynamics acts by rotations, and hence the first layer on which non-amenability is POSSIBLE. **(Q2) Do accumulated point-line motions compose into the face?** Yes, in a precise sense: the collision words — finite sequences of point-line moves — form a group that is DENSE in SO(3) (Corollary M57.F.1b). The face's full rotational symmetry is dynamically generated by the two odd directions; nothing beyond the point-line collisions is needed to reach every rotation of the face arbitrarily well. What the accumulation does NOT produce is a total invariant measure on the face — that is exactly what Corollary M57.F.3 forbids — and this is the honest content of the eight-version stall: the face exists as a G-space, not as a measure space. **(Q3) Is the motion a non-measurable rotation?** Corrected and answered: the motions are measurable rotations generating a FREE group, and freeness — not any single rotation — is what forces non-measurable pieces in any paradoxical decomposition. The reader's intuition survives in corrected form: the doubling mechanism of Banach–Tarski is available to the mediation dynamics, at the corpus angle, conditional only on (H-TRANS) — as a statement about non-measurable set decompositions, with no physical doubling implied (§9.4).

### **10.3 The vertical and the horizontal, and the handoff**

One generator alone is the vertical story: ⟨R\_x(θ\_D)⟩ ≅ ℤ, amenable, with the n-cycle coherence law |λ|ⁿ — the axis ZS-M54 already owns. Both generators together are the horizontal story: the free tree of collision words, exponential growth, Kesten spectral radius √3/2 strictly below 1 (check F7), no invariant mean. The vertical–horizontal pair of ZS-M50 recurs here exactly: the amenable direction carries the arithmetic the corpus has already closed; the free direction is where the new structure lives, and it cannot be seen inside the finite register SYMMETRY GROUP D₄ (Corollary M57.F.1a) — though, as §8.4 stresses, it does act faithfully in finite DIMENSION, and the ZS-M50 no-go is cited as a structural rhyme only.

Table 10.2. What this paper hands on. The ball step and the doubling reading are deliberately NOT executed here.

| Item | Recipient | Status |
| ----- | ----- | ----- |
| the ball / space step of the paradox (S² → B³ → doubling), and any cosmological doubling–halving reading | ZS-A9 (whose title holds that territory) and ZS-M58 | HYPOTHESIS territory; not claimed here |
| audit: does ZS-A9 §3's Φ: F₂ → D₄ match the natural surjection G\_D → D₄? | next session with ZS-A9 loaded | OPEN (rule R6: body not loaded) |
| Route S dichotomy: σ-measurable record vs amenable reduction ⟨R\_x⟩ ≅ ℤ | Route S executor (§16.5) | pre-registered fork, gate F-M57.F4 |
| Choi-seam reading: the carrierless mediation of the ZS-M58 seed is CONSISTENT with §9 — a correspondence needs no total record valuation on a carrier sphere; the obstruction removes the last reason to want one | ZS-M58 | supporting, not proving |

### **10.4 Value outside the corpus**

Three exports stand independently of every Z-Spin premise. (i) A transcendence-to-freeness PIPELINE applied to a physically anchored angle. The general free-rotation theorem is de Groot's (1956) and is not claimed here; what is portable is the move of recognising a model's own no-go theorem — an amplitude non-derivability result — as the hypothesis of that classical theorem, so that one statement does double duty as obstruction and as certificate. Any model whose coupling angle carries a transcendence budget can run it. (ii) A finite-truncation methodology: the exact integer certificate at the anchor angle, the specialization lemma's polynomial instances, the word-ball paradox identities, and the Kesten spectral witness together make 'this pair is free and non-amenable' machine-auditable to stated depth without trusting floats. (iii) Mean-invisible freeness: a channel-level observation — identical reduced channels, free conditional dynamics — that sharpens what 'the environment is not selected by the mean' can mean in any collision model.

## **§11. The carrier, constructed — and why that is not yet a closure**

Every version in this line has asked where the odd carrier is and answered negatively. This section answers positively: an admissible carrier is exhibited, in closed form, and it reproduces the ZS-M54 target channel exactly. The section then does the harder and more important thing, which is to say precisely how much that is worth — and the answer, pre-registered by ZS-M56.7 before the calculation was run, is that it settles a question of satisfiability and does not close F-M54-16′.

### **11.1 What §9 forces the phase to be**

Theorem M57.P′ (§9.2) says a grading-invariant carrier state yields a real multiplier for EVERY word. Since Im **λ** \= 0.6884532271 ≠ 0, the phase cannot come from the collision dynamics at any order. Exactly one structural possibility remains inside the two-dimensional graded setting: the carrier STATE must fail to commute with the grading. This is not a new freedom introduced for convenience — it is the unique surviving option, and the control check P3 of §5 already showed that dropping grading-invariance makes Im γ ≠ 0 generically. §11.2 takes that seriously and solves for it.

### **11.2 The construction**

Take the interaction of §6 with a free angle, **H**\_int \= (φ/2)·Z\_path ⊗ B\_E with B\_E odd under J\_E. Grading preservation gives W₁ \= J\_E W₀ J\_E \= exp(+iφB\_E/2), so

W₁†W₀ \= exp(−iφ B\_E) \= cos φ·I − i sin φ·B\_E ,   γ \= Tr(ρ\_E W₁†W₀) \= cos φ − i sin φ·⟨B\_E⟩ .

Write s \= ⟨B\_E⟩\_{ρ\_E} ∈ \[−1, 1\]. Then Re γ \= cos φ and Im γ \= −s sin φ, so demanding γ \= **λ** has the unique solution — with the pointer basis fixed by Z\_path \= |0⟩⟨0| − |1⟩⟨1|, so that |0⟩ is the \+1 eigenvector, and φ ∈ (0, π) so sin φ \> 0:

φ\* \= arccos(Re λ) \= 2.1729483796 ,   s\* \= − Im λ / sin φ\* \= − 0.8353812873 ,

and |s\*| \< 1, so the solution is admissible — realised, for instance, by the PURE carrier state with Bloch vector (s\*, 0, √(1 − s\*²)) in the (B\_E, R\_E, J\_E) frame. Nothing else is chosen. The sign of s\* is negative and it matters: the v1.3 build printed it as positive, which with the formula above returns λ̄ rather than λ. The error was masked in the v1.3 suite because its basis was produced by a routine returning ASCENDING eigenvalues, silently ordering the pointer basis (−1, \+1) and swapping |0⟩ with |1⟩. Both the text and the suite are corrected here, and the basis convention is now stated explicitly rather than inherited from a library default (Appendix C).

**Theorem M57.C.1 (Existence).** \[DERIVED-CONDITIONAL on the imported λ\] The carrier (dim ℋ\_E \= 2, J\_E \= σ\_z non-central, B\_E odd, ρ\_E the pure state above, φ \= φ\*) satisfies all three constraints of the closing specification and its reduced pointer channel equals Φ\_λ EXACTLY. Verified (check C1): max operator-norm deviation 4.7 × 10⁻¹⁶ across a full basis; Liouville spectrum exactly {1, 1, **λ**, **λ**̄}; completely positive with Choi rank exactly 2 — the value ZS-M56.5 proves the target must have; trace-preserving to 10⁻¹²; QND; interaction total-grading-even; carrier state pure (check C2, λ-free).

**What this settles.** After the ZS-M56 no-go chain and eight further negative audits it was a live possibility that the specification was VACUOUS — that constraints 1–3 could not be met at all, and the whole programme was pursuing an empty object. That possibility is now closed: the specification is satisfiable, and satisfiable by an object with no exotic ingredients. Correspondingly, ZS-M56’s obstruction is confirmed as exactly what it claimed to be — a no-go for an in-register graded tensor subsystem, not a no-go for the carrier as such.

### **11.3 Why it is not a closure — the reparametrisation theorem**

**Theorem M57.C.2 (Reparametrisation).** \[DERIVED\] The map **λ** ↦ (φ, s) \= (arccos Re λ, Im λ / √(1 − (Re λ)²)) is a BIJECTION from the open unit disc off the real axis onto (0, π) × (−1, 1), with inverse λ \= cos φ \+ i s sin φ. Verified on 15,749 samples with zero failures (check C4). Consequently the carrier data (φ, s) carries exactly the information content of **λ** — two real numbers against one complex number — and the construction of §11.2 TRANSPORTS the multiplier into collision coordinates rather than deriving it.

**The trap, fired on schedule and reported as such.** ZS-M56.7 pre-registered the rule that a two-parameter fit against two constraints carries zero evidential content. §11.2 fits exactly two real parameters (φ, s) against exactly two real targets (Re **λ**, Im **λ**), leaving zero residual degrees of freedom, so there is no possibility of a non-trivial check and the exact agreement of §11.2 is guaranteed a priori rather than discovered. It is reported here because the corpus’s discipline is to report the trap firing, not to present its output as a result. The anti-numerology control agrees: neither φ\* nor s\* is an algebraic-in-(**A**, **Q**) expression to 10⁻⁴ over a 20,964-member family (check C5) — they are **λ** in disguise, which is precisely what Theorem M57.C.2 predicts they must be.

### **11.4 F-M54-16′: the exact status, and the reduction achieved**

**F-M54-16′ is NOT closed by this paper.** No ZS-S14 open-slab calculation is performed in this build; the slab action is not reduced, no CTP superoperator is constructed, and φ\* and s\* are read off from **λ**. Declaration C6 states this in the ledger so that no successor can mistake §11.2 for a bridge. What HAS changed is the shape of the residual, and the change is worth having:

Table 11.1. The residual before and after §11. The question is the same question; it is now posed in coordinates a slab calculation can actually deliver.

|  | Before (ZS-M54 → v1.2) | After (v1.3) |
| ----- | ----- | ----- |
| form of the question | does the reduced S14 open slab EQUAL Φ^QND\_{λ, Z\_path}? — an equality of superoperators | does the S14 open slab yield the two real numbers φ \= 2.1729483796 and s \= −0.8353812873? |
| what must be computed | a channel, then compared | a coupling angle and a carrier polarisation — two scalars |
| known to be satisfiable? | unknown; possibly vacuous after M56 | YES, by Theorem M57.C.1 |
| where the phase must originate | unspecified; M54 reconstructs it from λ | the carrier STATE, not the dynamics — forced by Theorem M57.P′ (check C3) |
| evidential value of an exact match | would close F-M54-16′ | closes it ONLY if φ and s are derived independently; fitting them is the M56.7 trap |

**The structural finding worth carrying forward.** Theorem M57.P′ plus Theorem M57.C.1 give a dichotomy WITHIN the single graded collision model, and the scope of that qualifier is the whole point: if the collision layer alone must produce the complex multiplier, then either the carrier state respects the grading, in which case the multiplier is real at every word length and **λ** is unreachable, or it breaks the grading, in which case **λ** is reachable and two numbers must be supplied from outside.

**A third case exists, and it is ZS-M54’s own.** The v1.3 draft wrote “no third case” without the qualifier, and that was wrong. ZS-M54 already factorises the target as Φ\_λ \= U\_χ ∘ D\_r with r \= |**λ**| and χ \= arg **λ**, and that factorisation is realisable: a grading-INVARIANT carrier at collision angle θ\_D produces the real attenuation cos θ\_D \= |**λ**| exactly, and an independent system-side Z-Spin transit holonomy supplies e^{iχ}. The composite reproduces Φ\_λ to 2.5 × 10⁻¹⁶, is CPTP and QND, has Choi rank 2, and breaks NO grading (check K5). So the correct statement is the conditional one: within a single graded collision and with no independent holonomy, the carrier state must break the grading. Globally there is no such forcing — and asserting one would contradict ZS-M54’s own phase/attenuation separation. §12 develops the third case, which is structurally the better of the two.

### **11.5 What would actually close it**

Three things, none of them done here. (i) The ZS-S14 open-slab reduction: construct the CTP superoperator on the slab boundary, verify CP, TP and the QND property against the pointer, and read off the coupling angle φ — with the firewall intact, i.e. without λ entering the construction. (ii) The boundary state: derive s, the carrier polarisation transverse to the grading, from the slab boundary condition rather than fitting it — this is the object ZS-Q19 owes, now reduced to one number. (iii) A grading-breaking mechanism: since the state must break a symmetry the dynamics respects, the successor must say what breaks it, and whether that breaking is spontaneous, boundary-induced, or an artefact of truncation. Only (i) and (ii) together with a blind comparison constitute a closure; (iii) is what makes the closure physical rather than arithmetic.

## **§12. The Fourier–Weyl frame, the phase–attenuation split, and the one-number gate**

§11 left two admitted weaknesses. The carrier frame was canonical only up to a U(1) gauge that nothing fixed, and the construction forced the carrier state to break the grading — a strong structural commitment made on the strength of a dichotomy that §11.4 has now had to qualify. This section removes both. The frame is fixed from register kinematics with no λ-dependent input, the grading-breaking commitment is dropped in favour of ZS-M54’s own phase–attenuation factorisation, and the residual of F-M54-16′ is restated as a single complex number.

### **12.1 The carrier operators, fixed from the register**

The corpus supplies a Fourier operator F on the **Q** \= 11 register and the cyclic shift S, and ZS-F0 records the factorisation of the seam through them, J \= F²S \= S⁻¹F² (check K1, residual 6.9 × 10⁻¹⁵). Theorem M57.3 of this paper already located the unique D₄ E-block, P\_Eℂ¹¹ \= span{|1⟩, |9⟩}. Those two facts together fix the odd frame.

**Theorem M57.K.1 (Fourier–Weyl carrier frame).** \[DERIVED, λ-free\] Let Δ \= (9 − 1\) mod 11 \= 8 be the oriented displacement between the two E-block slots, and set

A\_F := P\_E S^Δ P\_E \= |9⟩⟨1| ,  B\_F := A\_F \+ A\_F† ,  R\_F := −i(A\_F − A\_F†) ,  J\_E := P\_E J\_Z P\_E .

Then B\_F² \= R\_F² \= J\_E² \= P\_E, {B\_F, R\_F} \= 0, J\_E B\_F J\_E \= −B\_F, J\_E R\_F J\_E \= −R\_F, R\_F \= −i J\_E B\_F, and J\_E is non-central on the block. In the ordered basis (|1⟩, |9⟩) the three operators are exactly σ\_x, −σ\_y and −σ\_z. All eleven relations are verified exactly (check K2).

**Corollary M57.K.2 (the U(1) gauge is fixed).** \[DERIVED\] §8.1 could fix the odd PLANE but not the first axis within it, leaving B\_E \= cos α σ\_x \+ sin α σ\_y with α free — an admitted gap, and the reason M57.F.0 is registered ALGEBRAIC rather than DERIVED. The Fourier–Weyl frame closes it: α is not chosen, it is the register displacement Δ \= 8\. What remains is the orientation convention (σ\_x, −σ\_y, −σ\_z) rather than (σ\_x, σ\_y, σ\_z), which is a relabelling and not a parameter (check K3).

**The scope of “fixed”, stated exactly.** What Corollary M57.K.2 fixes is the operator FRAME relative to two things the corpus already locks: the register basis, and the choice of the positive shift S rather than S⁻¹. It does NOT fix the ACTION-level vertex selector. Which of B\_F and R\_F appears in the ZS-S14 interaction, or in what time-ordering both appear, is a separate question that no result in this paper answers, and it is registered OPEN. The v1.4 draft’s unqualified “the U(1) gauge is fixed” invited the stronger reading and is narrowed here.

**What this does NOT do, stated immediately.** The E-block shares the slot |1⟩ with the pointer span{|0⟩, |1⟩}: their joint span has rank 3, not 4 (check K4). So the frame does NOT furnish an in-register tensor factor, and the ZS-M56 no-go stands untouched. What the frame furnishes is the OPERATOR ALGEBRA — a canonical odd pair and grading — which an external isomorphic copy, or a ZS-M58 completely-positive correspondence, may then carry. The distinction is exactly the one the ZS-M58 seed insists on, and it is why this section is not a rediscovery of the carrier M56 excluded.

### **12.2 The third case, developed**

**Theorem M57.K.3 (phase–attenuation realisation).** \[DERIVED-CONDITIONAL on the imported λ\] Let the carrier state be grading-INVARIANT and let the collision angle be θ\_D \= arccos|**λ**|. Then the collision produces the real attenuation γ \= cos θ\_D \= |**λ**| exactly — as Theorem M57.P′ requires it must — and composing with an independent system-side Z-Spin transit holonomy U\_χ \= diag(1, e⁻ⁱχ) at χ \= arg **λ** reproduces Φ\_λ exactly: deviation 2.5 × 10⁻¹⁶, CPTP, QND, Choi rank 2, and ‖\[ρ\_E, J\_E\]‖ \= 0 — no grading is broken (check K5).

**This is strictly better than §11.2 as a structural proposal, on three counts.** First, it requires no symmetry breaking: the object that §11.2 had to break is left intact, and the two halves of the multiplier are carried by two different agents rather than one overloaded state. Second, it is ZS-M54’s own factorisation Φ\_λ \= U\_χ ∘ D\_r, so it inherits that paper’s (11a)/(11b) layer assignment instead of proposing a rival one: the attenuation belongs to the collision layer, the phase to the Z-Spin transit holonomy. Third — and this is the connection that makes the paper one object rather than two — the attenuation angle of the split IS the collision angle of §§6–8: θ\_split := arccos|**λ**| \= θ\_D (check K6). The angle whose transcendence closes the amplitude route in §6, whose freeness generates the paradoxical sphere in §§8–9, and whose cosine is the attenuation here, is a single number playing three roles. The name matters: this quantity is θ\_split, defined from λ, and it is a TAUTOLOGY that it equals θ\_D. The v1.4 draft called it θ\_S14, which was a premise insertion — no slab angle has been computed, and only a value derived FROM the action may carry that name (rule R10′). Check K6 is a comparison-layer control accordingly.

### **12.3 The structural gate and the one-number restatement**

Before any multiplier is compared, a candidate slab kernel must pass a purely structural test. Writing C for the Choi operator of the candidate channel, the target satisfies four conditions exactly (check K7):

Table 12.1. Sub-gate A of F-M54-16′ — the structural conditions, all verified on the target. A candidate failing any row is rejected before its multiplier is looked at.

| Condition | Target value | Reading |
| ----- | ----- | ----- |
| C \= C† and C ⪰ 0 | min eigenvalue 0 | complete positivity |
| Tr\_out C \= I | exact | trace preservation |
| supp C ⊆ Δ\_Z \= span{|00⟩, |11⟩} | exact | the beginning–end equaliser of the ZS-M58 seed — Z\_path-QND |
| rank C \= 2, eigenvalues 1 ± |λ| | 1.8915135658 and 0.1084864342 | the minimal Kraus multiplicity of ZS-M56.5 |

**Only then does one number matter.** The entire multiplier content of the channel is the single complex matrix element

Λ := ⟨0| Φ(|0⟩⟨1|) |1⟩ ,   target Λ \= **λ** \= −0.5664173303 \+ 0.6884532271 i .

This supersedes the two-real form of §11.4. A successor does not need to produce (φ, s), nor (θ, χ) — it needs to produce Λ\_S14 from the slab and compare once (check K8). The reduction chain across three versions is therefore: v1.2, an equality of superoperators; v1.3, two real numbers; v1.4, one complex number, with the carrier operators fixed and the comparison performed at a single matrix element.

### **12.4 The honest verdict, unchanged**

**Theorem M57.C.2 applies to the improved route without modification.** (θ, χ) \= (arccos|Λ|, arg Λ) are the POLAR COORDINATES of Λ: again a bijection, again two reals against two targets, again zero residual degrees of freedom (check K9). Fitting θ and χ is inside the ZS-M56.7 trap exactly as fitting φ and s was. The improvements of §§12.1–12.2 are STRUCTURAL — the frame is no longer arbitrary, no symmetry need be broken, and the residual is one number rather than two — and they are not evidential. Nothing in this section makes the bridge more likely to hold; it makes the remaining computation smaller, better posed, and easier to falsify.

**Why the computation is still not done here.** The gate needs the ZS-S14 open-slab closed-time-path influence kernel: forward and backward field integration on the slab with the physical boundary condition, from which Φ\_S14 and then C\_S14 follow. A correction is owed here to the v1.5 wording, which said the loaded Standard-Model file is “a compact summary” without a usable action. That was wrong, and §14 corrects it: the ZS-S14 master action is present in full (Definition 3.1, with the unified covariant derivative, the ZS-M10 Yukawa invariant and the I-invariant potential), and the corpus additionally supplies a transfer-matrix construction (ZS-S21) and a reflection-positive slab (ZS-S24). What is absent is the slab REDUCTION data, and §14 identifies the one absence that is load-bearing. Producing one would mean inventing slab data, which is precisely what rules R1 and R2 and gate F-M57.2 exist to forbid, and what nine previous versions of this line were criticised for coming close to. The v1.4 draft called this “a file-availability limit rather than a mathematical one”, and that was too comfortable. Even with the full action in hand, a reduced channel additionally requires a slab identification and duration, a physical boundary state, gauge fixing with the BRST/BFV projection, an initial-correlation assumption, a coarse-graining prescription, a regularisation of the interacting path integral, and a continuum-or-finite-cell choice. Whether the corpus DEFINES all of these is itself undetermined. The accurate description is CURRENT CORPUS-DEFINITION INSUFFICIENCY, recorded as debt 7 and declared in check K10.

Table 12.2. The computation owed, specified precisely enough to be executed blind.

| Step | What must be done | Prohibited inputs |
| ----- | ----- | ----- |
| 1 | carrier operators: use P\_E, A\_F, B\_F, R\_F, J\_E of Theorem M57.K.1 — already λ-free | z\*, λ, θ\_D, φ, s |
| 2 | build the S14 open-slab CTP influence kernel with the physical (gauge-fixed) boundary condition | any fitted slab time or coarse-graining coefficient |
| 3 | propagate the four matrix units E₀₀, E₀₁, E₁₀, E₁₁ and assemble C\_S14 | any assumed tensor-factor environment |
| 4 | structural gate: Hermiticity, positivity, Tr\_out C \= I, supp C ⊆ Δ\_Z, rank 2 (Table 12.1) | — |
| 5 | extract the single number Λ\_S14 \= ⟨0|Φ\_S14(|0⟩⟨1|)|1⟩ | — |
| 6 | ONLY THEN compare Λ\_S14 with λ \= (iπ/2)z\* | — |

**The three possible outcomes are pre-registered, and two of the three are negative.** If the structural gate fails, the measurement–action bridge is CLOSED-NEGATIVE in its present form. If the gate passes and Λ\_S14 ≠ **λ**, the carrier structure survives but the i-tetration identification is rejected — which would be a substantial negative result about ZS-M54 rather than about this paper. If the gate passes and Λ\_S14 \= **λ** on a construction that never saw **λ**, F-M54-16′ closes. Registering all three before the computation is what makes the third outcome worth anything (gates F-M57.K1–K3).

## **§13. The boundary Weyl–influence-ratio protocol**

§12 reduced the residual to one complex number and specified a computation in six steps. This section does three further things: it proves that the structural gate CANNOT determine that number, so the reduction is exact rather than optimistic; it closes the free-group route to the phase, which is the route this paper’s own §§8–9 would most naturally have suggested; and it executes the protocol on a solvable surrogate, so that the instrument is validated even though the ZS-S14 action cannot be fed into it here.

### **13.1 The structural gate underdetermines the multiplier**

**Theorem M57.B.1 (Structural Underdetermination).** \[DERIVED, λ-free\] For α ∈ ℂ let Φ\_α be the pointer map fixing populations and sending ρ₀₁ ↦ αρ₀₁. Its Choi operator is |00⟩⟨00| \+ |11⟩⟨11| \+ α|00⟩⟨11| \+ ᾱ|11⟩⟨00|, with eigenvalues 1 ± |α| and support exactly Δ\_Z. Hence Φ\_α satisfies EVERY condition of the structural gate of Table 12.1 — Hermiticity, complete positivity, trace preservation, support in the equaliser, and Choi rank 2 — precisely when 0 \< |α| \< 1, for ANY phase of α. The set of channels passing the gate is therefore the one-complex-parameter family {Φ\_α : 0 \< |α| \< 1}, and the gate cannot discriminate among its members (check B1, verified on 3,153 sampled α).

**This is the theorem that makes §12 honest.** It would have been easy to present the Fourier–Weyl frame as if fixing the operators went most of the way to fixing the channel. It does not: frame rigidity does not imply multiplier rigidity. Everything §12.1 fixes is compatible with every α in the punctured disc, so the structural gate and the multiplier comparison are logically independent, and the residual really is exactly one complex number — no fewer, and no more. Sub-gate A and sub-gate B of F-M54-16′ must both be run.

### **13.2 The free-group route to the phase is closed**

**Corollary M57.P″ (no phase from any mixture).** \[DERIVED\] With a grading-invariant carrier state, every word multiplier γ(w) is real (Theorem M57.P′). Therefore every probability mixture Σ\_w μ(w)γ(w) over collision words is real, for every step distribution and every depth; and the symmetric walk operator (R\_x \+ R\_x⁻¹ \+ R\_y \+ R\_y⁻¹)/4 is self-adjoint, so its spectrum — including any asymptotic spectral datum — is real as well. No random walk on the free collision group can supply arg **λ** (check B2).

**Why this needed saying.** §§8–9 give this paper a free group, a dense orbit on the carrier sphere, and a paradoxical decomposition — an inviting toolkit, and the natural next move would be to look for the phase in some asymptotic invariant of the word tree. Corollary M57.P″ forecloses that entire family of attempts in one line. There is a second, independent reason to distrust such attempts: any construction that averages over ALL subsets of the paradoxical sphere with a collision-invariant weight is asking for exactly the object Corollary M57.F.3 proves does not exist. So the freeness of §8 constrains RECORDS and says nothing about the phase, and this paper’s two halves must not be spliced in that direction. Registering the no-go here is more useful than leaving the temptation open.

### **13.3 Bulk compression is exact**

The protocol’s one structural claim is that a boundary-only computation loses nothing. For the quadratic part of any slab kernel this is elementary and exact. Splitting the slab variables into boundary and interior, Ξ \= (Ξ\_∂, Ξ\_I), and writing the kernel in blocks, Gaussian integration over the interior returns

K\_∂^eff \= K\_∂∂ − K\_∂I (K\_II)⁻¹ K\_I∂ ,

the Schur complement — verified to machine precision on random configurations of a positive-definite kernel (check B3). This is not an approximation and not a truncation: the bulk inverse is compressed into a boundary Weyl function. Cubic and higher vertices enter as a boundary self-energy Σ\_∂ computed FROM the S14 vertices, and a successor may not substitute a free coarse-graining coefficient for it — that substitution is what gate F-M57.2 exists to catch.

### **13.4 The influence ratio, and which gate conditions are automatic**

Fix pointer histories a, b ∈ {0, 1} on the forward and backward closed-time-path branches and let Z\_ab be the resulting boundary functional. The multiplier is the normalised ratio

Λ := Z₀₁ / √(Z₀₀ Z₁₁) \= exp(−Γ \+ iχ) ,  Γ \= − Re log Λ ,  χ \= Im log Λ .

For a Gaussian interior with pointer-dependent source h\_a, the Feynman–Vernon influence functional gives Z\_ab \= exp(−½ΔᵀG\_RΔ \+ iΔᵀG\_I(h\_a+h\_b)/2) with Δ \= h\_a − h\_b, and three consequences are immediate. Z₀₀ \= Z₁₁ \= 1 identically, because the diagonal branches have zero source difference. Z₁₀ \= Z̄₀₁. And Γ \= ½ΔᵀG\_RΔ ≥ 0 whenever G\_R is positive, so |Λ| ≤ 1 automatically. Gate conditions A1 (diagonal normalisation), A2 (Hermiticity), A3 (complete positivity) and A5 (support in Δ\_Z) therefore hold BY CONSTRUCTION for the Gaussian class (check B4). The gate’s remaining discriminating content is strict rank 2 — that is, 0 \< |Λ| \< 1, excluding both a unitary and a totally dephasing limit — and the phase.

**Γ is a quantity the corpus already names.** The protocol’s natural attenuation output is Γ \= −log|Λ|, and the target value −log|**λ**| \= 0.1148346250 is exactly the locked constant μ, the ZS-M54 dephasing rate per cycle (check B6). This is an observation about coordinates and not evidence — μ is DEFINED as −log|**λ**| — but it is a good sign for the formulation that the protocol lands on an existing corpus quantity rather than manufacturing a new one.

### **13.5 The phase discriminator**

For a real symmetric boundary kernel the influence ratio has χ \= 0 EXACTLY: attenuation without phase (check B5). A nonzero χ therefore requires an explicitly non-symmetric ingredient in the boundary effective action, and the candidates are enumerable: a system-side Z-Spin transit holonomy (the §12.2 route), a grading-breaking boundary state (the §11.2 route), a chiral or fermionic determinant phase, or a genuinely multi-stage non-QND contribution. This is the sharp form of what M57.P′ and M57.P″ say from the collision side, now stated on the action side, and it is a requirement on the successor rather than a licence: naming a phase “Berry-type” is not sufficient, because a Berry phase needs an explicit connection and an explicit closed loop, and neither the free group nor the displacement Δ \= 8 supplies either.

Table 13.1. Where the phase may come from, and what each candidate must exhibit. Enumerated so that a successor cannot supply the phase by naming it.

| Candidate source | What must be exhibited | Status here |
| ----- | ----- | ----- |
| system-side Z-Spin transit holonomy | the holonomy as a term in the S14 boundary effective action, with its value | §12.2 realises it GIVEN χ; deriving χ is OPEN |
| grading-breaking boundary state | the state, plus a mechanism that breaks a symmetry the dynamics respects | §11.2 realises it GIVEN s; the mechanism is OPEN |
| chiral / fermionic determinant phase | the determinant and its phase, from the S14 fermion content | not attempted; no fermion determinant is computed here |
| multi-stage non-QND contribution | the stages, and why the composite is still Z\_path-QND | excluded within the QND class by construction; OPEN outside it |
| free-group asymptotics / random walk | — | CLOSED-NEGATIVE by Corollary M57.P″ (check B2) |

### **13.6 The protocol executed on a surrogate, and what that does and does not show**

The pipeline is run end to end on a solvable Gaussian surrogate: a positive-definite interior kernel, a pointer-dependent source, exact Schur compression, and the ratio Λ \= Z₀₁/√(Z₀₀Z₁₁). It returns a single complex number; the structural gate is checkable on it and passes; with a symmetric kernel the phase is exactly zero; with a non-symmetric part added the phase is nonzero and the gate still passes (checks B4, B5). **This validates the INSTRUMENT and nothing else.** The surrogate is not the ZS-S14 action, no surrogate number is a prediction, and no surrogate Λ is compared with **λ** anywhere in this paper or in the suite — declaration B8 states this in the ledger. What the surrogate establishes is that the six steps of Table 12.2 are well posed: the reduction is computable, the gate is decidable, and the phase question has a sharp yes/no discriminator. That is worth establishing before handing the protocol on, because a protocol that turned out to be ill-posed would have wasted the successor’s effort rather than this paper’s.

### **13.7 Three routes a successor should not take, and what to salvage from each**

These three were not proposed in any version of this paper, so nothing is retracted here. They are recorded because each is an inviting next step that the results above already exclude in its natural form, and each has a salvageable core.

Table 13.2. Forward guidance. The left column is the tempting move; the right column is what survives of it.

| Route | Why it fails as stated | What survives |
| ----- | ----- | ----- |
| holographic trace over the paradoxical sphere — obtain the phase from an asymptotic invariant of the free-group walk | Corollary M57.P″: every mixture is real. And an invariant total valuation on all subsets is exactly what Corollary M57.F.3 forbids, so the tool contradicts this paper’s own theorem. | the instinct to compute ONE boundary quantity instead of the whole channel — realised correctly as the influence ratio of §13.4 |
| Koenigs–Fourier bootstrap — use the fixed frame plus a Koenigs linearizer to force the multiplier without computing the slab | Theorem M57.B.1: the frame and the gate admit every α in the disc, so no multiplier follows. And a Koenigs linearizer is constructed FROM a given return map (R ↦ R′(w\*) ↦ K), not imposed to determine one; it is an analytic coordinate on state space, not an element of M₂(ℂ). | a RIGIDITY CERTIFICATE after closure: given an action-derived return map R\_S14, test whether K\_T⁻¹ ∘ K\_S14 conjugates it to i^z locally — which would upgrade a numerical equality to a dynamical equivalence |
| Świerczkowski anchor deformation — evaluate the channel at the algebraic angle arccos(1/3) and analytically continue to θ\_D | The anchor certifies the absence of free-group relations; it yields no channel value, so there is no initial condition. And one point plus CPTP/rank-2/QND does not determine an analytic family: Λ₀ \+ (θ−θ₀)h(θ) works for any small analytic h. Evaluating at θ\_D \= arccos|λ| would also reinsert the comparison input. | the anchor as an exact REGRESSION point, and the observation that continuation becomes legitimate only if the action independently supplies a deformation equation dΛ/dθ \= G(θ, Λ) together with Λ(θ₀) |

**The honest ranking.** The boundary influence ratio is the highest-value next computation, because it avoids the full channel without discarding action information — the Schur compression is exact. The Koenigs test is second and belongs strictly after closure. The anchor is third and is useful only as a regression point. None of the three is executed here, and the status of F-M54-16′ is unchanged from §12.4: OPEN, with the residual now a single complex number and a decidable gate.

## **§14. The clock — why Λ\_S14 is not a number, and what is**

This section answers the question the previous three versions were driving towards, and the answer is not the one they were set up to receive. The residual was reduced to one complex number, and the natural next step is to compute it. That computation cannot be performed — not because a file is missing, but because the quantity is not determined by the action. The section proves this, corrects a statement of v1.5 in the course of doing so, and then supplies the well-posed replacement.

### **14.1 A correction: the action is present**

Version 1.5 recorded that the loaded Standard-Model file is a compact summary containing no usable action, and used that to justify debt 7\. On re-reading, that is wrong and is withdrawn. The ZS-S14 master action is given in full at Definition 3.1 — the Einstein–Hilbert term with the **A**|H₅|² non-minimal coupling, the unified covariant derivative on the five-dimensional icosahedral irrep, the three gauge kinetic terms, the fermion kinetic term, the ZS-M10 unique Yukawa invariant with its ZS-S13 normalisation, and the I-invariant potential. The corpus further supplies an Osterwalder–Seiler / Lüscher transfer-matrix construction (ZS-S21) and a reflection-positive slab with an exact electric-limit spectrum (ZS-S24). The material is considerably better than v1.5 credited, and the honest diagnosis has to be rebuilt on what is actually missing rather than on a mis-description of what is present.

### **14.2 The multiplier is not a function of the action**

**Theorem M57.T.1 (Clock Ill-Posedness).** \[DERIVED, λ-free\] A QND coherence multiplier is produced by the interaction INTEGRATED over the slab. For the graded collision of §§6 and §12 at coupling g and slab duration τ the multiplier is γ(τ) \= cos(gτ). At fixed coupling, as τ ranges over (0, π/g) the modulus |γ| sweeps the entire interval (0, 1\) — verified over 62 values, range \[0.008, 0.999\] (check T1). Therefore, WITHIN THIS FAMILY, the modulus is not determined by the coupling alone: every admissible target modulus is reachable by a choice of duration.

**A scope correction, owed against the v1.6 statement of this theorem.** Version 1.6 read Theorem M57.T.1 as establishing that Λ\_S14 is universally undefined. That is stronger than the proof supports. ZS-S24 already carries a one-step transfer family T\_a \= exp(−aV/2)exp(−aL)exp(−aV/2), and if a PRIMITIVE slab or event step is structurally selected then a dimensionless one-step map is perfectly well defined without any metric duration. The correct statement is narrower: S\_S14 alone does not select a FINITE-TIME map unless a primitive slab or event prescription is supplied. Universal ill-posedness is DERIVED-CONDITIONAL on the absence of such a prescription, not PROVEN — and §15 shows that the missing prescription may be an event count rather than a duration, which changes the problem.

**What this means for the question “what is Λ\_S14?”** It means the question has no answer as posed. Λ is a function of the action AND the clock, and an exhaustive text search of all six loaded corpus files returns ZERO occurrences of the slab duration τ\_Z (check T2). τ\_Z is corpus debt 6, assigned to the unwritten ZS-Q19, and it is not fixed by ZS-S14, by ZS-S21, or by ZS-S24. So the v1.4–v1.5 gate — compute one complex number and compare — was asking the S-line for something that does not exist independently of a quantity another paper owes. The attenuation half of the multiplier carries zero evidential content until the clock is fixed, and it would have carried zero even if the slab reduction had been performed in full.

**This is the diagnosis the line has been missing.** Ten versions have failed to close F-M54-16′, and the failures were read as insufficient effort, missing files, or the wrong carrier. The structural reason is simpler and was visible in the corpus’s own vocabulary all along: μ is called the dephasing rate *per cycle*, and a rate per cycle presupposes a cycle. The bridge from an action to a per-cycle multiplier cannot close while the cycle is undefined, no matter how good the reduction is. Debt 6 is not a loose end beside the main problem; it is inside it.

### **14.3 The clock-free invariant**

Something does survive. The corpus’s own law is the per-cycle power law: coherence after n cycles is **λ**ⁿ. Both the log-modulus and the phase are then linear in n,

−log|**λ**ⁿ| \= nμ ,   arg(**λ**ⁿ) \= n·arg **λ** ,

so their ratio is independent of n — and, by exactly the same argument applied to the duration rather than the cycle count, independent of the slab clock.

**Theorem M57.T.2′ (Projective Generator Ray, branch-conditioned).** \[DERIVED-CONDITIONAL on a chosen logarithmic lift\] A channel determines |**λ**| and Arg **λ** modulo 2π, but its GENERATOR logarithm has branches ℓ\_k \= log|**λ**| \+ i(Arg **λ** \+ 2πk). A positive clock rescaling acts as ℓ\_k ↦ cℓ\_k, so the clock-free datum is the PROJECTIVE RAY \[Γ : Ω\_k\] — one ray per branch, not a single number. The principal representative is

R\_k \= (Arg **λ** \+ 2πk) / (−log|**λ**|) ,   R₀ \= 2.2592495539 / 0.1148346250 \= 19.6739402770 ,

and the family for k \= −2…2 is {−89.756, −35.041, 19.674, 74.389, 129.104} — five distinct values, of which the channel alone selects none (check T3a). Each ray is separately clock-free; the CHOICE of ray is not.

**A retraction, and the reason it matters.** The v1.6 build asserted that R is exactly cycle-independent and offered a check said to verify n \= 1 through 23\. That check computed (n·arg **λ**)/(nμ), which is n-independent by algebra and verifies nothing at all; the principal argument in fact WRAPS — Arg(**λ**²) \= −1.7647, not 2·Arg **λ** \= 4.5185, so the principal-branch ratio at n \= 2 is −7.6836 and not 19.6740. The code also tested eight values of n while the ledger line claimed twenty-three. Both faults are corrected (check T3 is now a retraction control verifying the wrap for all 22 tested n), and the unwrapped lift is now an explicit HYPOTHESIS rather than a verified fact. Selecting k \= 0 requires one of: a continuous lift from the identity, a phase-unwinding rule, an action-derived generator, or an exact CRT-4 / H-CLK clock equality. Branch selection is OPEN.

**Corollary M57.T.3 (the residual, correctly typed).** \[ALGEBRAIC, comparison layer\] Given R and the DIMENSIONLESS product μ \= Γτ, the full multiplier follows exactly, since **λ** \= exp(−μ(1 − iR)) — reconstruction verified to 10⁻¹² (check T6). A v1.6 overstatement is corrected here: R together with a DURATION does not determine the multiplier. What is needed is R together with μ \= Γτ, so the action must supply the RATE Γ and not merely the clock τ — one further arrow than v1.6 counted. And the reconstruction is an identity among comparison-layer quantities, since μ, R and **λ** all derive from **λ**; the v1.6 build tagged it construction-layer and proof-bearing, which was wrong. The reduction chain across versions is: an equality of superoperators; two real numbers; one complex number; and now a branch-conditioned projective ray plus one rate.

### **14.4 What R is made of**

**Theorem M57.T.4 (Structural Decomposition).** \[DERIVED\] Since **λ** \= (iπ/2)z\*, one has arg **λ** \= π/2 \+ arg z\* and −log|**λ**| \= −log(π/2) − log|z\*|, both exact (check T4), so

R \= (π/2 \+ arg z\*) / (−log((π/2)|z\*|)) .

Neither **A** nor **Q** appears. R is built from the i-tetration fixed point alone. This is worth stating plainly because it changes what kind of target the S-line is being handed: not a number in which the geometric impedance and the register width must conspire, but a pure property of the Koenigs multiplier of z ↦ i^z. The pre-registered anti-numerology null agrees and is unsurprising for that reason — a 96,741-member algebraic-in-(**A**, **Q**) family contains no match to R at 10⁻⁴, nearest miss 1.3 × 10⁻² (check T5). The null is a control, and here it is a control whose outcome Theorem M57.T.4 predicts in advance.

### **14.5 What the S-line does supply, and where it stops**

The gauge-sector instrument exists and is good, and it still stops above what the pointer channel needs. ZS-S21 Theorem S21.1 proves that the Osterwalder–Seiler / Lüscher transfer matrix returns a DIAGONAL quadratic Hamiltonian for every weight assignment, and that it PROPAGATES orbit weights faithfully — but it explicitly does not SELECT them. Three ratios remain undetermined, and the sub-bridge closes only at DERIVED-CONDITIONAL on three named postulates, (H-W), (Z-A0) and (Z-A1). ZS-S21 reports that as a negative result of its own construction rather than burying it, which is the same discipline this paper is trying to keep.

Table 14.1. The chain from the action to R, with the status of each link. Two links are missing, and they are different in kind.

| Link | Supplied by | Status |
| ----- | ----- | ----- |
| the master action S\_S14 | ZS-S14 Definition 3.1 — complete | PRESENT (v1.5 said otherwise; corrected here) |
| a group-valued cellular reduction and a transfer matrix | ZS-S21 Theorem S21.1 | PRESENT, DERIVED-CONDITIONAL on (H-W), (Z-A0), (Z-A1) |
| a reflection-positive slab with an exact electric-limit spectrum | ZS-S24 | PRESENT (gauge sector) |
| selection of the orbit weights | — | OPEN — ZS-S21 propagates but does not select; three ratios free |
| identification of the pointer Z\_path with specific S14 degrees of freedom | — | OPEN — the gauge-sector instrument is not the pointer channel |
| the slab clock τ\_Z | — | ABSENT — zero occurrences in six files; debt 6, owed by ZS-Q19 |
| R \= arg λ / (−log|λ|) | this paper, from λ | the target: 19.6739402770, clock-free (Theorem M57.T.2) |

**The two missing links are not equally serious.** Weight selection and pointer identification are ordinary open problems: hard, but the kind of thing a paper can do. The clock is different, because Theorem M57.T.1 shows that without it the target quantity is not defined, so no amount of work on the other links produces a comparison. The correct order of operations is therefore the reverse of the one this line has been following: fix τ\_Z first, or else compare only R.

### **14.6 The revised gate**

Table 12.2 specified six steps ending in a comparison of one complex number. Steps 1–5 stand unchanged; step 6 is replaced, and a step 0 is added in front.

Table 14.2. The revised terminal gate. The change is that the comparison is now clock-free, so it can be run before debt 6 is paid.

| Step | Revised requirement |
| ----- | ----- |
| 0 (NEW) | state the slab clock explicitly, or declare that the comparison will be clock-free. If a duration is chosen, say where it comes from; a fitted τ makes the attenuation vacuous by Theorem M57.T.1 and fires gate F-M57.T1. |
| 1–5 | unchanged from Table 12.2: Fourier–Weyl frame, CTP kernel, propagate the four matrix units, structural gate, extract Λ\_S14. |
| 6 (REVISED) | compute R\_S14 \= arg Λ\_S14 / (−log|Λ\_S14|) and compare with R \= 19.6739402770. This comparison is invariant under every rescaling of the clock, so it is the only part of the multiplier comparison that is meaningful before τ\_Z exists. |
| 7 (NEW) | only if τ\_Z has been independently derived: compare Λ\_S14 with λ itself. Passing step 6 and failing step 7 would locate the failure in the clock; failing step 6 would locate it in the dynamics. |

**The three pre-registered outcomes of §13 are refined accordingly.** If the structural gate fails, F-M54-16′(A) is CLOSED-NEGATIVE as before. If the gate passes and R\_S14 ≠ R, the i-tetration identification of the multiplier is REJECTED, and — this is the improvement — that rejection is now clock-independent, so it cannot be rescued by adjusting τ\_Z. If the gate passes and R\_S14 \= R on a construction that never saw **λ**, then the phase-to-attenuation structure of the corpus multiplier is derived from the action, and what remains for full closure of F-M54-16′ is exactly one number, the clock. That is a strictly better position than this line has occupied at any previous version, and it is still not a closure.

### **14.7 What was and was not computed here**

**No Λ\_S14, no Γ\_S14, no χ\_S14 and no R\_S14 is computed in this build (declaration T7).** The reduction was attempted and stopped at a located point, and the located point turned out to be more informative than the reduction would have been: the question was ill-posed, and the well-posed replacement is a single real number that depends on z\* alone. Nothing in §14 is a match to any corpus quantity — R is DEFINED from **λ**, so its value here is a restatement and not a result, and check T3 sits in the comparison layer for that reason. What is new and λ-free is Theorem M57.T.1 and the typing of the residual (checks T1, T6).

## **§15. The event clock, and the characteristic-function gate**

Version 1.6 concluded that the multiplier is not a number. That conclusion rested on conflating two different clocks, and separating them reopens a route that needs no duration at all. This section performs the separation, refutes two mechanisms this line proposed for itself, and states the successor gate as a single operator-level equality.

### **15.1 Two clocks, not one**

An EVENT clock n counts record increments — one register shift, one seam step, one emitted record quantum — and is dimensionless. A METRIC clock t \= nτ\_Z carries physical duration. F-M54-16′ asks for a PER-CYCLE multiplier, so the object it needs first is the event clock; τ\_Z is needed only later, to convert a per-event contraction into a rate per unit time. Theorem M57.T.1 bites on the metric clock alone. The one-step map depends only on the dimensionless product gτ — verified: (g, τ) \= (1, 1\) and (2, 0.5) give the identical map, while (1, 1\) and (1, 2\) do not (check V1) — so at one-step level no metric duration is separately meaningful. Hence a per-event multiplier can be well posed even when the metric-time generator scale is not, and the v1.6 verdict overreached: Λ\_S14 is not a number as a FINITE-TIME map, but it may be one as a ONE-STEP map.

### **15.2 The defect gate**

Let C\_S14 be a candidate action-derived one-event contraction on the pointer coherence line, |0⟩⟨1| ↦ a\_S14 |0⟩⟨1|. The first requirement is on its defect operators D\_C \= (I − C\*C)^{1/2} and D\_{C\*} \= (I − CC\*)^{1/2}. For the target, both equal √(1 − |**λ**|²) \= 0.4529939978, so the defect indices are (1, 1\) — exactly one coherence defect emitted per record quantum (check V2). A candidate whose defect indices differ carries either no record or more than one per event, and the single-carrier / single-record route closes negatively. This gate is checkable before any multiplier is looked at.

### **15.3 The characteristic function, and why the gate is overdetermined**

For a completely non-unitary contraction the Sz.-Nagy–Foiaș characteristic function

Θ\_C(z) \= −C \+ z D\_{C\*}(I − zC\*)⁻¹ D\_C

is a COMPLETE unitary-equivalence invariant \[IMPORTED-PROVEN\]. For the scalar coherence contraction it collapses to the degree-1 Blaschke factor (z − a)/(1 − āz), which is inner — verified to 2 × 10⁻¹² on the unit circle — and satisfies Θ(0) \= −a, so it recovers the multiplier exactly (check V3). This is the structural reason to prefer the characteristic function to a one-point comparison: requiring Θ\_S14 to be a scalar inner function of degree 1 AT ALL is a strong constraint on a whole analytic function, and most contractions fail it. Passing it and then matching Θ(0) is an overdetermined test, not a fit of one number.

**The corpus already owns both halves of this.** ZS-Q18 records Θ\_λ(z) \= (**λ** − z)/(1 − **λ**̄z) as inner with unit multiplicity, and records that this multiplicity matches the ZS-M46 unit Abel-cover translation u ↦ u \+ 1, with the exact normalisation left OPEN under the names CRT-4 and H-CLK. So the successor gate proposed here is not new machinery bolted on: it reuses an existing, already-named corpus residual as the exact successor to F-M54-16′ (check V4, reported as an OBSERVATION — the ZS-Q18 and ZS-M46 bodies are loaded only as compact entries and no theorem of theirs is re-derived here, per rule R6).

### **15.4 Two refutations, one of them of this paper’s own proposal**

**The single-kernel Lamb-shift route is CLOSED-NEGATIVE.** This line’s own exploration proposed obtaining the phase-to-decay ratio from ONE influence kernel, as a Lamb-shift to decoherence-rate ratio, on the ground that both come from the same kernel and so their ratio needs no duration. That fails for strict QND. With H\_I \= Z ⊗ B and Z² \= I, the weak-coupling Lamb-shift term in the zero-Bohr-frequency sector is proportional to Z†Z \= I — a GLOBAL phase. The relative pointer phase (Ω/2)Z that a complex multiplier requires is simply not generated (check V5). The phase must therefore come from one of the separately named sources of Table 13.1, exactly as Theorem M57.P′ and Theorem M57.K.3 already implied; there is no shortcut through the dissipator.

**The Lambert–Dyson self-consistency route is downgraded to BOOTSTRAP-HYPOTHESIS.** The identity **λ** \= −W₀(−log i) is PROVEN — it follows from z\* \= e^**λ**, itself the fixed-point equation — and the equation L \= log(i)·e^L is a contraction at its solution with rate |**λ**| \< 1, so any convergent iteration lands on it robustly. But contraction shows only that the CHOSEN equation is stable; it does not select the equation. D₄’s order 4 supplies a quarter-turn CLASS, and supplies neither the exponential feedback e^L nor a choice among the branches log i \= i(π/2 \+ 2πm). Absent an independent action-side derivation of the exponential self-dependence, writing that equation down is premise insertion, and the earlier HYPOTHESIS-strong registration was too generous (declaration V6).

### **15.5 The successor gate**

Table 15.1. The gate that replaces the one-number comparison. It requires no metric duration, and two of its five outcomes are negative.

| Stage | Requirement | Failure verdict |
| ----- | ----- | ----- |
| 0 | separate the clocks explicitly: is the construction producing a one-EVENT map or a finite-TIME map? A fitted duration fires gate F-M57.T1. | — |
| 1 | construct the one-event contraction C\_S14 on the pointer coherence line from S14 / S21 / S24 and the Fourier–Weyl frame, resolving pointer embedding and orbit-weight selection. Prohibited inputs: λ, z\*, μ, R, θ\_D. | no contraction ⇒ the route is void |
| 1b | verify that C\_S14 is COMPLETELY NON-UNITARY — no unitary summand. Added in v1.8: the classification theorem of §15.3 applies only to c.n.u. contractions, and the v1.7 gate omitted this. | Θ is not a complete invariant; stage 3 is void |
| 2 | defect indices dim D\_C \= dim D\_{C\*} \= 1 | single-carrier / single-record route CLOSED-NEGATIVE |
| 3 | Θ\_S14 is a scalar inner function of degree 1 | the ZS-Q18 / ZS-M46 clock candidate is RETRACTED |
| 4 | W V\_S14 W† \= U\_M46(1) for the minimal isometric dilation V\_S14 and the M46 unit Abel translation, with the record MASA correspondence | CRT-4 / H-CLK FAILS |
| 5 | only now, construction locked: compare a\_S14 with λ \= −W₀(−log i) | mismatch ⇒ the i-tetration identification of the multiplier is RETRACTED |

If all five pass, then one S14 record event is one i-tetration seam step, and the per-event channel is closed WITHOUT a metric duration — which is the whole of what F-M54-16′ asks if the multiplier it wants is per-cycle. The physical rate is then a separate and subsequent question: H\_eff \= −(1/τ\_Z) log C\_S14 requires τ\_Z, and by §14 that number is still owed. So event-clock closure is not metric-clock closure, and v1.6 was wrong to treat the second as a precondition for the first. Nothing in this gate is executed here (declaration V7).

### **15.7 An audit of this section’s own closing claim**

The v1.7 release closed by asserting that the remaining prerequisites are two (§15.7) — an action-derived C\_S14 or Θ\_S14, and the exact CRT-4/H-CLK intertwiner — and that both are testable without duration. That sentence has been tested (Block Y) and it is two-thirds right. It is recorded here rather than quietly rephrased, because a closing sentence is the part of a paper a successor is most likely to act on.

**What survives.** Θ does determine the multiplier including its PHASE. Under the Sz.-Nagy–Foiaș coincidence equivalence Θ ↦ cΘ with |c| \= 1, the ZERO of Θ is unchanged, and the multiplier is recovered as that zero; so the worry that the gate might fix only the modulus is unfounded (check Y1). And the per-event gate is genuinely free of metric duration: stages 2 through 5 involve only a one-step contraction, its defect spaces and its characteristic function, none of which carries a physical time (check Y5).

**What fails, first: the node count.** “Construct C\_S14” is not one node. It presupposes the pointer embedding — which S14 degrees of freedom carry Z\_path — and orbit-weight selection, and ZS-S21 explicitly propagates weights without selecting them, leaving three free ratios (§14.5). Those are two separate open problems, not one. With the branch normalisation as a third and the intertwiner as a fourth, the honest count is four distinct prerequisites, with branch normalization and the intertwiner coupled, plus one hypothesis to verify (complete non-unitarity, §15.2 stage 1b) and one deferred quantity (the metric clock, §14). Declaration Y4 records the corrected count.

**What fails, second and more interestingly: the two nodes are not independent.** The ZS-M46 construction linearises the seam to a UNIT translation u ↦ u \+ 1 in the Abel–Fatou coordinate, and that coordinate is obtained from the Koenigs coordinate by dividing by the step, which is w ↦ w \+ log **λ** (mod 2πi). Since log **λ** has branches — imaginary parts −4.024, 2.259, 8.542 for k \= −1, 0, 1 — normalising the step to 1 IS a branch choice (check Y3). So the intertwiner node is entangled with the branch node that Theorem M57.T.2′ registered OPEN; testing the intertwiner does not settle the branch, and choosing the branch is part of stating the intertwiner. The two cannot be worked in either order without the other.

**The corrected closing statement.** F-M54-16′ is OPEN with four distinct prerequisites, with branch normalization and the intertwiner coupled, one hypothesis and one deferred quantity, and the per-event route is testable without a metric duration but NOT without a normalisation choice. The difference from the v1.7 sentence is not cosmetic: “two independent nodes, both duration-free” suggests a programme that could be executed in two moves, and “four entangled prerequisites, one of them a branch selection the channel cannot make” suggests a programme that has to fix a convention before it can compare anything. The second is what the mathematics supports.

### **15.6 A note on this paper’s scope**

Across seven versions this paper has accumulated a domain resolution, a free-group theorem, a Banach–Tarski corollary, a carrier construction, a boundary protocol, a clock theorem and now a dilation-theoretic gate. For internal corpus purposes the accumulation is legible, because each layer corrects the one before it and the correction log records why. For external submission it is too much for one paper, and the honest recommendation is a split: §§2–10 as a domain-and-obstruction paper, and §§11–15 as a carrier-and-clock paper. That split is recorded as a recommendation and is not performed here, because renumbering across a corpus that cites this paper by section would cost more than it gains.

## **§16. Route S — the stochastic realisation, specified and not executed**

This is the oldest debt in the line, flagged and unpaid through nine consecutive versions (F-M56.13), and it is the one route no multiplicity argument reaches: a classical phase noise requires no tensor factor, so neither M56.21′ nor anything in §2–§4 has an object to act on. It is specified here as precisely as the loaded corpus permits, and it is not executed. Saying so plainly is the point of this section.

### **16.1 The reformulation**

Φ^QND is mixed-unitary (ZS-M54 Theorem M54.13, PROVEN). Write the one-cycle map as an average over a classical phase:

Φ(ρ) \= 𝔼\_φ \[ e^{iφ Z\_path/2} ρ e^{−iφ Z\_path/2} \] ,  coherence multiplier \= 𝔼\[e^{iφ}\].

The problem becomes one line: find the measure the ZS-S14 action supplies and check whether its characteristic function equals λ. This is far better posed than “construct an environment”, because a characteristic function is a single complex number computed from a distribution, and a distribution is what a stochastic sector of an action actually produces.

Table 16.1. Two measures that reproduce Φ^QND exactly (checks S1, S2). These are TARGETS for testing, not results — see §16.4.

| Measure | Parameters | Reconstruction error |
| ----- | ----- | ----- |
| Two-point | p \= (1+|λ|)/2 \= 0.9457567829 at φ \= arg λ; 1−p at φ \= arg λ \+ π. Then 𝔼\[e^{iφ}\] \= (2p−1)e^{i arg λ} \= λ exactly. | 4.00×10⁻¹⁶ |
| Gaussian | φ \~ N(m, σ²) with m \= arg λ \= 2.2592495539 and σ² \= −2 ln|λ| \= 2μ \= 0.2296692500, since 𝔼\[e^{iφ}\] \= e^{im − σ²/2}. | 5.55×10⁻¹⁶ (200-node Gauss–Hermite) |

The structural identity this exposes is worth recording independently of whether the route closes: in the stochastic reading the corpus decoherence rate μ \= −ln|λ| \= 0.1148346250 is exactly one half of a classical phase variance. μ is not merely a damping constant; it is a variance. That is a physical statement ZS-M57 can hand on either to be derived or to be falsified.

### **16.2 One constraint the corpus derives rather than fits**

ZS-M54 records the n-cycle survival as |λ|^{2n}, that is coherence λⁿ. Two classical noise structures give different n-cycle laws, and only one matches.

Table 16.2. Annealed versus quenched (check S3). The corpus law selects annealed, unambiguously, at n \= 2 already.

| n | Annealed — fresh draw each cycle: |λ|ⁿ | Quenched — one draw held: e^{−n²σ²/2} |
| ----- | ----- | ----- |
| 1 | 0.8915135658 | 0.8915135658 |
| 2 | 0.7947964380 | 0.6317013778 |
| 3 | 0.7085718065 | 0.3557554847 |
| 5 | 0.5631703478 | 0.0566498678 |

This converts a fitting problem into a structural requirement: the ZS-S14 stochastic sector must supply a phase redrawn independently each Z-cycle — white, Markovian — and a quenched static bias is falsified by the corpus's own λⁿ law. It is a derivation with a falsification attached and it costs no free parameter. It is also, honestly, the only part of Route S this paper can deliver.

### **16.3 The charge of a classical noise term, its defect, and its rescue**

A classical noise term is H\_int \= ξ·Z\_path with ξ a classical field. By ZS-M56.18, Z\_path is ℤ₂-odd; therefore H\_int is ℤ₂-even if and only if ξ is ℤ₂-odd. The seam symmetry of ZS-S1 §5.2, citing ZS-F5, is ε ↔ −ε. So ε is ℤ₂-odd, ε·Z\_path is even and admissible, and the non-minimal coupling (1 \+ Aε²)R is even in ε, consistently. The odd partner the selection rule demands may therefore be the Z-bias field itself, entering stochastically rather than as a tensor factor.

Note that this argument is untouched by §2–§4. The ℤ₂ it uses is ε → −ε, which is J\_Z — the involution that does restrict to the pointer. The naming correction of §1.2 has no effect on Route S, and it is worth saying so explicitly, because a reader who has followed §4 may reasonably expect the opposite.

**The defect.** ZS-A3 §2 gives the potential as V(ε) \= (λ\_V/4)M\_P⁴(ε² − 1)² with ε → 1 at infinity, and states that the ℤ₂ symmetry of V is restored at ε \= 0\. The vacuum is therefore at ε \= ±1 and the ℤ₂ is spontaneously broken in the bulk. Consequently the fluctuation δε \= ε − 1 has no definite ℤ₂ parity — the symmetry maps one vacuum to the other — and the fluctuating component is exactly what Route S requires. The charge argument is valid about the field ε in the unbroken phase, not about the fluctuation around the physical vacuum. This is F-M56.19's third condition (that the background about which δ²S\_ZS is evaluated be ℤ₂-invariant) biting, and it is registered as such.

**The rescue, and its price.** ZS-A3 §2 also gives ε(r\_H) \= 0 at the Z-anchor — which, in the U(1) completion, is the vortex core where |Φ| → 0 is forced topologically. At ε \= 0 the ℤ₂ is restored, δε does have definite odd parity, and ε·Z\_path is admissible. Route S survives, localised at the Z-anchor rather than in the bulk. That is a restriction and it is also structurally natural: the Z-anchor is where Z-Spin mediation happens. The price is a clock — if the stochastic sector lives at the anchor, the per-cycle independence required by §16.2 must be produced by an anchor reset mechanism, and that is the same object ZS-Q19 owes for τ\_Z. The dependency is stated; the clock is not attempted.

### **16.4 The trap, pre-registered before any computation**

The Gaussian measure has two real parameters, m and σ², and the target has two real constraints, Re λ and Im λ. By Theorem M56.7 a two-parameter family fitted to two constraints has null probability 1 and carries zero evidential content (check S4). Route S closes only if the action fixes m and σ² independently of λ. If it fixes only one, the correct report is a partial result with the residual named — not a closure. Gate F-M57.2 fires on any measure whose parameters are obtained by solving 𝔼\[e^{iφ}\] \= λ.

### **16.5 What ZS-M57 hands on**

Four steps, in order, none of which this paper performs. (i) Identify the fluctuating component of ε on the Z-sector and its measure from the ZS-S14 action, at the anchor where the parity argument holds. (ii) Compute its characteristic function over one Z-cycle. (iii) Test whether the phase is redrawn per cycle, against Table 16.2. (iv) Compare 𝔼\[e^{iφ}\] with λ without having used λ anywhere in (i)–(iii).

**Status: Route S is OPEN.** It has now been deferred ten times. This paper does not pretend otherwise, and it does not substitute the §2–§4 closures for it: closing a wrong question well is not the same as answering the right one.

## **§17. Route B — barred by rule R6, and what would unbar it**

A BRST ghost–antighost pair has ghost numbers \+1 and −1, so its ghost parity is a non-central involution, satisfying the charge constraint the spinor fails; and it has dimension 2, satisfying the Kraus-rank constraint. On the corrected scoreboard of Table 18.2 it is the only external candidate scoring above zero.

**It is not analysed here.** ZS-Q16 v2.5 and ZS-A30 v2.1 are not among the corpus files loaded for this build, and rule R6 (“search before deriving”) forbids reasoning about a construction second-hand. Every version of ZS-M56 that discussed the ghost route did so without having read ZS-Q16, and v1.7's rejection of it had to be withdrawn in v1.8 as overreach for exactly that reason. Repeating the error while quoting the rule that forbids it would be worse than leaving the route open.

What must be established, in order, when the files are loaded: (a) whether tracing over the ghost sector gives a CPTP map on the physical subspace at all — a BRST sector is not a physical bath and the reduced map need not be CPTP; (b) only then, the multiplier. If (a) fails, Route B is CLOSED-NEGATIVE for a reason worth publishing, since it removes the corpus's best-scoring graded candidate. Gate F-M57.4 pre-registers this ordering; computing a multiplier before establishing CPTP would fire it.

One scoring note survives the §4 withdrawal. The seed added a D₄ score to this route; that column is void, because §2.3 shows D₄-equivariance is not formulable for the pointer factor. Route B is scored on the three CANDIDATE constraints of Table 18.1; the fourth (paradoxicality, §9.3) is a class theorem that scores no candidate and bars none — it constrains what any survivor's record structure may be.

## **§18. The specification at closing**

Table 18.1. The environment specification. Constraints 1–3 are ZS-M56 Table 3.1 unchanged. The seed's fourth constraint (D₄ multiplicity) is WITHDRAWN by §2.3 and §4.3; its replacement is the PARADOXICALITY constraint of §9.3 (Table 9.1), a theorem about the class rather than a wish about a candidate.

| \# | Constraint | Source | Requirement on ℋ\_E |
| ----- | ----- | ----- | ----- |
| 1 | Kraus rank | M56.5 — the Choi rank of Φ^QND is exactly 2 for 0 \< |λ| \< 1 | dim ℋ\_E \= 2; the minimal realisation has dim ℋ\_E \= 2 |
| 2 | Charge | M56.20, M56.22′ — the ℤ₂ selection rule under J\_Z | J\_E non-central; a central grading ±I gives zero odd operators |
| 3 | Multiplicity (ℤ₂) | M56.21′ — q\_R(J\_Z) \= 1 | no J\_Z-preserving embedding into the register; ℋ\_E must be genuinely external |
| — | Multiplicity (D₄) — seed v1.1 | M57.D.2 | WITHDRAWN. Not formulable: the pointer is not a D₄-subrepresentation (§2.3). |
| 4 | Paradoxicality | M57.F.1–2, M57.F.3 — §9.3 | the collision group of any admissible carrier is free; no total collision-invariant record valuation exists; record structure is σ-measurable or amenable-reduced |

Table 18.2. Candidate scoreboard, corrected. The charge column is scored under the CORPUS grading J\_Z (check N11, check S5), not under J. Two of the seed's entries move.

| Candidate | dim | odd ops under J\_Z | non-central? | external? | score |
| ----- | ----- | ----- | ----- | ----- | ----- |
| BRST ghost–antighost (c, c̄), J\_E from ghost parity | 2 | 2 | yes | open — the whole question | 2 / 3 |
| j \= ½ spinor factor, J\_E \= D^{1/2}(2π) \= −I | 2 | 0 | no — central gradings induce no operator parity | open | 1 / 3 |
| Internal seam pair (3, 7\) — seed §1.4 | 2 | 0 | no — J\_Z restricts to \+I (Table 2.1) | no | 1 / 3 (was 2/4) |
| The E-block span{|1⟩, |9⟩} | 2 | 2 | yes | no — internal, and not the pointer (Cor. M57.3a) | 1 / 3 |
| z₋ alone (one-dimensional) | 1 | 0 | no | no | 0 / 3 |
| Classical phase measure (Route S) | — | — | n/a — no tensor factor at all | n/a | outside the obstruction entirely |

Read Table 18.2 as the paper's thesis in one object. Every graded candidate scores at most 2 of 3, the one that scores 2 cannot be assessed without files this build does not have, and the only entry that leaves the table is the one that is not a tensor factor at all.

## **§19. Anti-circularity, anti-numerology, and provenance**

### **19.1 The λ-free firewall**

The construction layer may use A, Q, dim Z, κ, L\_Z, Γ\_Z, J, J\_Z, D₄ and the ZS-S14 action. It may not use z\*, λ, |λ|, arg λ, μ, D, p, σ², θ\_D or ZS-Q18 Kraus data before the comparison layer. Every check in the ledger carries a firewall tag; 43 checks are tagged construction-layer, of which 33 are proof-bearing (classes R and A), and 23 are comparison-layer and are never evidence for a construction claim (checks X1, X2). Theorem M57.G′ is DERIVED-CONDITIONAL on the imported (H-TRANS); its ledger checks (G2, G3, G3a, G3b) are analytical identities and controls, and its transcendence premise is verified nowhere — it is imported, as §6.2 states, and check G3a records exactly that the executable tests only the deductive ingredients, not the transcendence.

Every central result of this paper — M57.1, M57.2, M57.3, M57.D.1, the F-M57.11 resolution, and M57.P — sits entirely on the construction side. That is not an accident of arrangement: it is why they are stated as theorems rather than as agreements.

### **19.2 The true-by-construction catalogue, now eight**

Table 19.1. Instances in which a check's two sides shared their premise, reported as evidence. Instance 8 is new in this paper and is the seed's, not this paper's; it is recorded because the catalogue's value is that nothing is removed from it.

| \# | Instance | Mechanism |
| ----- | ----- | ----- |
| 1 | ZS-M53 v1.5 Koenigs regression | shared number |
| 2 | ZS-M54 v1.9 check T5 — W₁ was built from λ | premise insertion |
| 3 | ZS-M56 seed item C2 — the Influence–Koenigs table compared λⁿ with λⁿ | shared number |
| 4 | ZS-M56 v1.2 X5 — zeroed a row and column to force its own premise | premise insertion |
| 5 | ZS-M56 v1.3 M56.12 — sin(arg λ) was trigonometry on an inserted angle | premise insertion |
| 6 | ZS-M56 v1.6 B4 — the odd mode's being unshifted followed from a coupling attached only elsewhere | premise insertion |
| 7 | Seed B check I5 — θ\_D \= arccos|λ| enters U\_D, then the derived Kraus pair is compared with ZS-M54 Eq. (13), also built from λ | premise insertion |
| 8 (NEW) | Seed v1.1 §1.3–§1.4 — a J-compatible sector split was combined with J\_Z \= I₁₁ − 2|1⟩⟨1|, which is defined only in a different slot ordering; the isometry then verified an equivariance its own basis had supplied | basis insertion |

Instance 8 is a new mechanism, not a new instance of an old one. The tautology scan looks for shared numbers; the premise-insertion scan looks for modified objects; neither looks for two objects written in incompatible coordinates. Rule R10′ (§4.4) is the corresponding new discipline, and check X3 is its executable face for this paper: J, J\_Z and ℋ\_Z are asserted unmodified at the end of the run.

### **19.3 Anti-numerology**

The complete target was pre-registered before anything was run: **λ** \= −0.566417330285… \+ 0.688453227108… i, with both real and imaginary parts to be matched; matching |**λ**| alone has one fewer constraint. No claim of this paper matches λ at all — which is the cleanest possible position, and is a consequence of every central result being λ-free. The one search performed is §6.3's, and it is reported with its chance expectation attached. Three coincidences are barred in advance (§3.3). No new constant is introduced; the only numbers this paper produces are integer multiplicities and quantities algebraically derived from the locked set (check X6).

### **19.4 Provenance**

Every corpus section cited in §1–§4 was loaded and read directly: ZS-F0 §8.3–§8.7 and §9, ZS-M6 §2.1–§2.3, ZS-S1 §5.2, ZS-M54 §8, §10–§13 and Appendix B, ZS-M56 v1.8 in full. Sections cited but read only through downstream citation are flagged as such at the point of use: ZS-A3 §2 (the ε potential and ε(r\_H) \= 0, §7.3) is inherited from the seed and is not independently verified here — gate F-M57.14. ZS-Q16 and ZS-A30 are not loaded, and nothing is claimed about them (§8). The transcendence import (H-TRANS) behind Theorem M57.G′ is read through ZS-F0 §11.8.5 and is reduced to η\_topo algebraic by Lemma M57.G.0 (§6.3); the residual is registered OPEN and is not independently verified here. ZS-M56's 101-check regression suite is not present in this build; check X5 reproduces its central inequality independently, but the full regression is NOT executed, and that is registered as debt 1 rather than reported as a pass.

## **§20. Cross-paper dependency trace**

Table 20.1. Every upstream object consumed, its status, and whether this paper moves it. Nothing is moved.

| Object | Value / statement | Source | Effect of ZS-M57 v1.3 |
| ----- | ----- | ----- | ----- |
| A | 35/437 \= 0.080091533181 | ZS-F2 | LOCKED, unmoved (check X4) |
| Q; (dim X, dim Z, dim Y) | 11; (3, 2, 6\) | ZS-F5 | LOCKED, unmoved (check X4) |
| κ² \= A/Q | 35/4807 \= 0.007281048471 | ZS-M6 §2.2 | consumed, unmoved |
| L\_Z (bare Z-block) | diag(0, 1\) in the eigenmode basis | ZS-M6 §2.1 | consumed; fixes the register basis (§2.1) |
| J (seam involution) | |j⟩ ↦ |10−j⟩; (6, 5); Mat grading (61, 60\) | ZS-F0 Thm 8.5, 8.6 | reproduced; shown not to restrict to ℋ\_Z |
| J\_Z (Z-internal involution) | I₁₁ − 2|1⟩⟨1|; (10, 1); Mat grading (101, 20\) | ZS-F0 Def 8.11, Thm 8.12 | reproduced; shown to restrict to ℋ\_Z as diag(+1, −1) |
| J not a bulk symmetry | ‖\[J, L\]‖\_F ≈ 2.94 ≠ 0 | ZS-F0 Thm 8.7 | consumed; now second in the argument, not first |
| D₄ \= ⟨J, J\_Z⟩ | order 8; ord(JJ\_Z) \= 4 | ZS-F0 Thm 8.13 | reproduced; decomposed (§3) |
| Conjecture 8.14 | JJ\_Z ↔ the i-tetration quarter turn | ZS-F0 Conj 8.14 | constrained (Cor. M57.D.3′); NOT closed |
| M56.21′ | q\_R(J\_Z) \= 1 \< 2 ≤ dim E | ZS-M56 v1.8 §2.2 | STANDS; naming correction only (§4.4) |
| M56.22′ | a grading admits odd operators only if non-central | ZS-M56 v1.8 §3 | consumed; re-applied to the seed's internal pairs |
| M56.7 | a fitted family carries no evidential content | ZS-M56 | consumed; pre-registered as the Route S trap |
| M54.13 | the instrument is not selectable at mean-operator level | ZS-M54 v2.2 §12 | consumed unchanged |
| (11a)/(11b) layer split | action layer vs reconstruction layer | ZS-M54 v2.1 | PROMOTED: M57.P shows the split is forced (§5.2) |
| λ, z\*, μ, D, p, θ\_D | comparison-layer constants | ZS-M1, ZS-M43, ZS-M54 | consumed only at the comparison layer |
| (H-TRANS) transcendence of |λ| | reduced to η\_topo algebraic by Lemma M57.G.0 | ZS-F0 §11.8.5, Thm 8.9–8.10 | IMPORTED; carried explicitly in M57.G′; residual η\_topo registered OPEN |

No downstream paper is affected except ZS-M56 v1.8, which requires the naming correction of §4.4, and ZS-Q19, which inherits τ\_Z, ρ\_E and now also the Z-anchor reset clock of §16.3.

## **§21. Observational consistency**

This paper produces no observable and touches none. Its content is finite-dimensional linear algebra on an 11-slot register plus one lemma about 2×2 unitaries. Three consistency statements are recorded for completeness.

(i) No cosmological quantity is used or predicted. Planck 2018 ΛCDM parameters, the ZS-A30 value Ω\_Λ,0 \= 83/121, and every acoustic-scale fit are untouched, because nothing here enters any transfer function.

(ii) No Standard-Model coupling is used or predicted. α\_s \= 11/93, the ZS-S1 spectral couplings and the ZS-S7 gap results are untouched. The only Standard-Model input consumed is ZS-S1 §5.2's statement that the Z-sector ℤ₂ is ε ↔ −ε with one even and one odd mode, which is a mode count, not a number.

(iii) The three-metric remains forbidden by ZS-A16 Theorem F. The D₄ structure does not change this: a finite group supplies finitely many irreducibles and therefore no Weyl tower. No continuum limit, no phenomenology, no new constant.

## **§22. Conclusion**

The seed proposed that ZS-M56 had asked a ℤ₂ question when the physically complete question was D₄-equivariant, and that supplying the D₄ question and answering it would be the advance. The first half of that is right as mathematics and wrong as physics, and the reason is smaller and more elementary than anything the eight-version history of this line had reached for.

In the register basis in which the Z-internal involution is the operator ZS-F0 Definition 8.11 says it is, the Z-sector is slots 0 and 1, and the seam involution sends slots 0 and 1 to slots 10 and 9\. The pointer is not seam-invariant. It has no seam grading. The smallest seam-invariant subspace containing it has dimension four. So the seam cannot impose a selection rule on the QND vertex, D₄-equivariance cannot be written down for a two-dimensional pointer factor, and the trichotomy that eight versions had circled resolves to “J\_Z only” — not by argument about which grading is physical, but because the other two options refer to operators that do not exist on the object in question.

Stated at exact strength, one line each:

• **J span{|0⟩, |1⟩} \= span{|9⟩, |10⟩}**, and that is the whole resolution. \[DERIVED, M57.1\]  
• The register's unique quarter turn lives on span{|1⟩, |9⟩} — the odd Z-mode and its seam image — for every odd Q and every admissible slot. \[DERIVED, M57.3; PROVEN, M57.D.1\]  
• A symmetric carrier with an invariant state gives a real multiplier; Im **λ** ≠ 0; so the ZS-M54 layer split is forced, not chosen. \[PROVEN, M57.P\]  
• The collision amplitude |**λ**| \= cos θ\_D is not an algebraic function of **A**, **Q**; the seed’s κ² \= A/Q amplitude route to θ\_D is closed, the angle route is OPEN, and Route G is a representation theorem at level L2. \[DERIVED-CONDITIONAL, M57.G′\]  
• ZS-M56 v1.8 stands, needing a name changed and nothing else.

And immediately, what is not closed. F-M54-16′ is not closed; this paper does not touch it. No environment satisfying all three candidate constraints of Table 18.1 is exhibited; the corpus still satisfies one. The new fourth row is a theorem about the class, and it is the first constraint in this line that the searches could not have produced, because it is a property of the dynamics rather than of any candidate. Route B is not analysed, because the files are not loaded and rule R6 forbids guessing. Route S — the stochastic realisation, the only route no multiplicity argument can reach — is specified more sharply than before and executed not at all; it has now been deferred ten times, and the honest description of this paper is that it removed a wrong question from in front of it rather than answering it. ZS-F0 Conjecture 8.14 is constrained and not closed. τ\_Z and ρ\_E belong to ZS-Q19, and by M56.7 the multiplier carries no evidential content while they are free.

One methodological remark, because the line's history earns it. Six of ZS-M56's eight central theorems were refuted from outside the paper, and the seventh was refuted by the audit that replaced it. The seed's proposed successor is now the ninth such event, and it was caught not by a deeper theorem but by asking which basis two matrices were written in. Rule R10 was added after the last version confused two involutions by name. Rule R10′ is added here after this one confused them by coordinates. The pattern that survives is not that the arguments get cleverer; it is that the question “does this operator act on that object at all?” has now been the decisive question three times in a row, and it should be asked first.

## **Acknowledgements & Code Availability**

The central finding of this paper — that the seam involution does not restrict to the pointer system — was reached by executing rule R6 (“search before deriving”) on the phrase “slot 1” in ZS-F0 Definition 8.11, which had been read eight times as a naming detail and never as a basis statement. The seed report's author is recorded as having registered, unprompted, that the choice of pointer representation in Theorem M57.D.2 was a judgement and not a derivation, and as having asked that the gap be gated. That request is what made the gap findable; §3.2 discharges it, and does so against the seed's own proposal.

Code availability. The verification ledger is zs\_m57\_verify\_v1\_8.py (numpy, scipy, mpmath at 50 digits; RNG seed 57, fail-closed, exits non-zero on any FAIL). Block F additionally uses EXACT integer arithmetic (the Świerczkowski certificate and the word-ball paradox identities run without floats). Every deterministic figure printed in this manuscript appears verbatim in one seeded run; Haar-random quantities (Theorem M57.P) are reported as bounds — max |Im γ| \< 10⁻¹³ over 1000 draws — with the seed-57 value given parenthetically, because the exact mantissa is BLAS- and platform-dependent and should not be read as a certificate. The seed suite zs\_m57\_seed\_v1\_1\_verify.py is retained unmodified and re-executes at 39/39 PASS; it is the regression baseline for Blocks D, G and S, and its check D14 (the J-compatible sector split) is the object corrected in §2.4. The ZS-M56 v1.8 suite zs\_m56\_verify\_v1\_8.py is NOT present in this build and its 101 checks are NOT executed here; only its central inequality is reproduced independently (check X5). This is recorded as debt 1 of Table A.3 rather than reported as a regression pass.

## **Appendix A — Verification ledger**

Class tags: R \= reconstruction on the actual object; A \= analytical identity; X \= control; D \= declaration. Declarations are printed but are excluded from the PASS total. Firewall tags: free \= construction layer, touches no comparison-layer quantity; cmp \= comparison layer, never evidence for a construction claim. One seeded run, seed 57\.

Table A.1. Block D — ZS-F0 §8 regression and the D₄ decomposition. All λ-free.

| Tag | Class | Statement | Result |
| ----- | ----- | ----- | ----- |
| D1 | R | J is an involution with multiplicities (6, 5\) \[ZS-F0 Thm 8.5\] | PASS — (6, 5\) |
| D2 | R | J\_Z is an involution with multiplicities (10, 1\) \[ZS-F0 Def 8.11\] | PASS — (10, 1\) |
| D3 | R | Mat₁₁ grading by J is (61, 60\) \[ZS-F0 Thm 8.6\] | PASS — (61, 60\) |
| D4 | R | Mat₁₁ grading by J\_Z is (101, 20\) \[ZS-F0 Thm 8.12\] | PASS — (101, 20\) |
| D5 | R | ‖\[J, J\_Z\]‖\_F \= 2√2 \[ZS-F0 Thm 8.13\] | PASS — 2.8284271 |
| D6 | R | ⟨J, J\_Z⟩ has order 8 with ord(JJ\_Z) \= 4 \[ZS-F0 Thm 8.13\] | PASS — |G| \= 8, ord(r) \= 4 |
| D7 | R | THEOREM M57.D.1: ℂ¹¹ \= 5A₁ ⊕ 4B₂ ⊕ E under D₄ | PASS — dims 5+4+2 \= 11 |
| D8 | R | mult(E) \= 1 for every odd Q in 5…17 — structural, not about 11 | PASS — all 1 |
| D8b | A | ERRATUM: the closed form is ((Q−1)/2)A₁ \+ ((Q−3)/2)B₂ \+ E, not the seed's | PASS — dims close at Q for all seven Q |
| D9 | A | E ⊗ E needs A₂ and B₁, which the register lacks entirely | PASS — blocked by {A₂, B₁} |
| D10 | A | E ⊗ (A₁⊕B₂) \= 2E needs 2 \> mult(E) \= 1 | PASS — needed 2, have 1 |
| D11 | A | the order-4 element acts with order 4 only on E | PASS — χ(r) \= (1, −1, 0\) |
| D12 | X | ANTI-NUMEROLOGY: (n₊, n₋) \= ((Q+1)/2, (Q−1)/2) for all odd Q | PASS — (6,5) carries no information |

Table A.2. Blocks N, P, G, S, X. Block N is the paper's central content and is entirely λ-free.

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| N1 | D | free | DECLARATION: corpus Z-sector \= span{|0⟩,|1⟩}; L\_Z \= diag(0,1) \= ½I − ½J\_seam | declaration — not proof-bearing |
| N2 | R | free | THEOREM M57.1: J span{|0⟩,|1⟩} \= span{|9⟩,|10⟩} | PASS — support {9, 10} |
| N3 | R | free | M57.1(b): ℋ\_Z and Jℋ\_Z intersect trivially | PASS — dim sum \= 4, dim ∩ \= 0 |
| N4 | R | free | THEOREM M57.2: the minimal D₄-invariant hull of the pointer has dim 4 | PASS — dim \= 4 \> 2 |
| N5 | R | free | no nonzero pointer vector is a J-eigenvector (4000 draws) | PASS — max |⟨v, Jv⟩| \= 6.9×10⁻¹⁷ |
| N6 | R | free | J\_Z DOES restrict to the pointer, as diag(+1, −1), non-central | PASS |
| N7 | A | free | Z\_path is J\_Z-odd and anticommutes with the restricted grading | PASS — residual 0.0 |
| N8 | R | free | THEOREM M57.3: the unique E-block is span{|1⟩, |9⟩} | PASS — supp(P\_E) \= {1,9}, tr \= 2.000000 |
| N9 | A | free | COR. M57.3a: E contains |1⟩ and not |0⟩, so E is not the pointer | PASS — ⟨0|P\_E|0⟩ \= 0 |
| N10 | R | free | M57.D.1 and M57.3 are independent of which slot carries the sign (10 relabellings) | PASS — all (5, 4, 1), E \= span{|k⟩,|10−k⟩} |
| N11 | R | free | CORRECTION: under J\_Z every seam pair but (1, 9\) is central with zero odd operators | PASS — see Table 2.1 |
| N12 | A | free | GATE F-M57.11 RESOLVED: “J\_Z only”, by domain; outcomes F and G closed-negative | PASS |
| N13 | X | free | CONTROL: a Z-block Laplacian embedded in the register has \[J, L\] ≠ 0 | PASS — ‖\[J, L\]‖ \= 1.414214 |
| P1 | R | free | THEOREM M57.P over 1000 Haar draws | PASS — max |Im γ| \< 10⁻¹³ (7.2×10⁻¹⁷, seed 57\) |
| P2 | A | free | the proof step γ\* \= Tr(JρJ · JW₀†J · W₀) is an identity (200 draws) | PASS — residual 1.43×10⁻¹⁶ |
| P3 | X | free | CONTROL: dropping grading-invariance of ρ\_E makes Im γ ≠ 0 | PASS — max |Im γ| ≈ 0.99 (order 1, seed 57\) |
| P4 | A | cmp | CONSEQUENCE: Im λ ≠ 0 | PASS — 0.688453227108 |
| G1 | D | cmp | DECLARATION: Route G is claimed at L2 only; θ\_D is a comparison-layer input | declaration — L1 not claimed |
| G2 | A | cmp | LEMMA M57.G.0: |λ|² \= (π²/4)|z\*|² \= (π²/4)η\_topo exactly; so η\_topo algebraic ⇒ |λ| transcendental | PASS — residual 0.0, η\_topo \= 0.322118863 |
| G3 | X | cmp | M57.G′ AMPLITUDE null: algebraic-in-(A, Q) family (no π), 9,869 members, 0 hits at 1×10⁻⁴ for |λ| \= cos θ\_D | PASS — 0.99 expected by chance; control, not evidence |
| G3a | X | cmp | M57.G′ records deductive INGREDIENTS only (|λ| \= cos θ\_D; A, Q rational); does NOT verify transcendence, which is imported | PASS — by design a control |
| G3b | A | cmp | COROLLARY M57.G.1 (Niven): |λ| ∉ {0, ±½, ±1}, so θ\_D is not a rational multiple of π | PASS |
| G3c | X | free | RETRACTION CONTROL: “θ algebraic ⇒ cos θ algebraic” is FALSE (cos 1 transcendental, Lindemann–Weierstrass); v1.0 M57.G retracted | PASS — cos 1 \= 0.5403023059 |
| G4 | X | cmp | TAUTOLOGY SCAN: seed check I5's two sides both depend on λ via θ\_D | PASS — reported as a control |
| S1 | R | cmp | two-point measure p \= (1+|λ|)/2 reproduces Φ^QND | PASS — err 4.00×10⁻¹⁶ |
| S2 | R | cmp | Gaussian N(arg λ, 2μ) reproduces Φ^QND — μ is half a phase variance | PASS — err 5.55×10⁻¹⁶ |
| S3 | A | cmp | ANNEALED vs QUENCHED: the λⁿ law selects annealed at n \= 2 | PASS — 0.7947964380 vs 0.6317013778 |
| S4 | X | cmp | M56.7 TRAP pre-registered: 2 parameters against 2 constraints | PASS — null probability 1 |
| S5 | A | free | CORRECTED SCOREBOARD under the corpus grading J\_Z | PASS — spinor 0, pair (3,7) 0, ghost 2, E-block 2 |
| S6 | X | cmp | CONTROL: the classical phase label carries zero pointer information | PASS — M54.13 applies unchanged |
| X1 | X | free | FIREWALL: 34 checks tagged construction-layer | PASS |
| X2 | X | free | PROOF-BEARING SPLIT: 26 λ-free checks in classes R and A | PASS |
| X3 | X | free | PREMISE-INSERTION SCAN: J, J\_Z, ℋ\_Z unmodified at end of run | PASS |
| X4 | X | free | REGRESSION GUARD: A, Q, (X, Z, Y) unmoved | PASS |
| X5 | X | cmp | REGRESSION GUARD: q\_R(J\_Z) \= 1 \< 2, ZS-M56 v1.8 untouched | PASS |
| X6 | X | free | NO NEW CONSTANT: only integer multiplicities and locked-set algebra | PASS |

Table A.2b. Block F — the Free Collision Theorem and the paradoxical sphere (NEW v1.2).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| F1 | A | free | the odd space is EXACTLY span{B\_E, R\_E} (dim 2); both vertices even \+ QND; the generator pair is canonical, zero choices | PASS |
| F2 | R | free | EXACT integer Świerczkowski certificate at cos \= 1/3: all 118,096 reduced words ≤ 10 non-identity (3 ∤ b throughout) | PASS — zero failures, min|b| \= 1 |
| F3 | R | cmp | at θ\_D: 13,120 words ≤ 8 and 300 random words 15–40 bounded away from I | PASS — min 0.138957 / 0.502999 |
| F4 | A | free | specialization-lemma instances: 400 random reduced words formally non-identity as polynomials P(c)+sQ(c) | PASS — 400/400 |
| F5 | R | free | F₂ combinatorial paradox: aW(a⁻¹) \= F₂ ∖ W(a) etc., EXACT on the 39,365-word ball | PASS |
| F6 | R | cmp | sampled nontrivial words are genuine rotations (2 fixed points each); axes almost all distinct — D countable | PASS — 500/500; 450 distinct axes |
| F7 | R | free | KESTEN witness: ρ\_free(depth 9\) \< √3/2 ≪ ρ\_{ℤ²}(30) | PASS — 0.835905 \< 0.866025 ≪ 0.997434 |
| F8 | X | free | ANTI-NUMEROLOGY: structure holds verbatim at cos \= 1/3; rank 2, pieces 4/5, √3/2 carry no Z-information; √3/2 vs |λ| REFUSED (diff 0.0254882) | PASS — control |
| F9 | A | cmp | MEAN-INVISIBLE FREENESS: identical pointer channels for both generators; non-commuting carrier rotations | PASS — diff \< 10⁻¹³; ‖\[R\_x,R\_y\]‖ \= 0.3064 |
| F10 | A | cmp | kinematic GROUP finite (|D₄| \= 8\) vs dynamical group infinite (4,373 distinct words ≤ 7). Corrected statement: G\_D ⊈ D₄, but G\_D DOES act faithfully in finite dimension | PASS |
| F11 | X | cmp | density proxy: length-25 word orbits equidistribute on S² (small 1st/2nd moments) | PASS — control |
| F12 | D | free | DECLARATION OF SCOPE: paradox off the σ-algebra; Born/CPTP untouched; no physical doubling; Route S not blocked | declaration |

Table A.2c. Blocks W and C — the word-level correction and the constructed carrier (NEW v1.3).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| W1 | A | cmp | RETRACTION: mean channel blind to the one-step generator label but SEPARATES composed words; “entire F₂ mean-invisible” (v1.2) withdrawn | PASS — γ(xx) \= 0.5895928759 vs γ(xy) \= 0.7947964380 |
| W2 | R | cmp | THEOREM M57.P′: with a grading-invariant carrier state EVERY word has a REAL multiplier — the long-word phase route is closed | PASS — max|Im γ| \< 10⁻¹³ over 411 words |
| C1 | A | cmp | THEOREM M57.C.1 (EXISTENCE): explicit dim-2 external carrier reproduces Φ\_λ exactly; specification NOT vacuous | PASS — 4.7×10⁻¹⁶; spec {1,1,λ,λ̄}; Choi rank 2; CP+TP |
| C2 | R | free | the constructed carrier’s structural constraints, λ-free: dim 2, J\_E non-central, interaction total-grading-even, QND, state pure | PASS |
| C3 | A | cmp | the PHASE comes from the STATE, not the dynamics — forced by M57.P′; (11a)/(11b) is a dynamics/state split | PASS — ‖\[ρ\_E, J\_E\]‖ \= 1.181 ≠ 0 |
| C4 | R | free | THEOREM M57.C.2 (REPARAMETRISATION): λ ↔ (φ, s) bijection; the construction transports λ, it does not derive it | PASS — 15,749 samples, 0 failures; 0 residual d.o.f. |
| C5 | X | cmp | ANTI-NUMEROLOGY on the fitted pair: neither φ\* nor s\* is algebraic-in-(A, Q) to 1e-4 | PASS — 20,964-member family, 0 hits; control |
| C6 | D | free | DECLARATION: F-M54-16′ NOT CLOSED. Residual reduced to two numbers φ \= 2.1729483796, s \= 0.8353812873. No S14 slab computed in this build | declaration |
| C7 | A | cmp | PRIORITY: de Groot (1956) is prior for the general free-rotation theorem; his tan²(θ/2) condition ≡ our cos θ condition | PASS — equivalence exact |

Table A.2d. Block K — the Fourier–Weyl frame, the third case, and the one-number gate (NEW v1.4).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| K1 | R | free | corpus identity J \= F²S \= S⁻¹F² on the Q \= 11 register | PASS — residual 6.9×10⁻¹⁵ |
| K2 | R | free | THEOREM M57.K.1: the Fourier–Weyl frame A\_F \= P\_E S⁸ P\_E, B\_F, R\_F, J\_E — eleven exact relations; equals (σ\_x, −σ\_y, −σ\_z) in basis (|1⟩,|9⟩); built from S, P\_E, J\_Z only | PASS — all eleven exact, λ-free |
| K3 | A | free | COROLLARY M57.K.2: the U(1) gauge left free by M57.F.0 is FIXED by the displacement Δ \= 8 | PASS |
| K4 | R | free | M56 CONSISTENCY: E-block shares |1⟩ with the pointer; joint rank 3 \< 4, so no in-register tensor factor — frame supplies operators, not a subsystem | PASS — rank 3 |
| K5 | A | cmp | THEOREM M57.K.3 (THIRD CASE): grading-INVARIANT carrier gives real attenuation |λ|; system-side Z-holonomy supplies the phase; Φ\_λ reproduced with no grading broken — v1.3’s ‘no third case’ withdrawn | PASS — error 2.5×10⁻¹⁶, ‖\[ρ\_E,J\_E\]‖ \= 0 |
| K6 | A | free | the attenuation angle IS the collision angle of §§6–8: θ\_S14 \= arccos|λ| \= θ\_D | PASS |
| K7 | R | cmp | STRUCTURAL GATE (sub-gate A): Choi Hermitian, positive, Tr\_out C \= I, supp C ⊆ Δ\_Z \= span{|00⟩,|11⟩}, rank 2 with eigenvalues 1 ± |λ| | PASS — 1.8915135658, 0.1084864342 |
| K8 | A | cmp | ONE-NUMBER RESTATEMENT: the whole multiplier content is Λ \= ⟨0|Φ(|0⟩⟨1|)|1⟩; supersedes the two-real form of C6 | PASS |
| K9 | R | free | M57.C.2 STILL APPLIES: (θ, χ) are polar coordinates of Λ — a bijection; the improvement is structural, not evidential | PASS — 0 residual d.o.f. |
| K10 | D | free | DECLARATION: the S14 open-slab CTP kernel cannot be built from the loaded compact file (no influence functional, no return map, no transfer-operator identification). Debt 7, not worked around | declaration |

Table A.2e. Block B — the boundary Weyl–influence-ratio protocol (NEW v1.5).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| B1 | R | free | THEOREM M57.B.1: the structural gate is passed by exactly {Φ\_α : 0 \< |α| \< 1} — frame rigidity does NOT imply multiplier rigidity | PASS — 3,153/3,153 sampled α pass |
| B2 | R | cmp | COROLLARY M57.P″: every mixture over collision words is real; the symmetric walk operator is self-adjoint — the free-group route to the PHASE is closed | PASS — max|Im| \< 10⁻¹³, real spectrum |
| B3 | R | free | STAGE 2: interior Gaussian integration \= Schur complement EXACTLY; boundary-only discards no bulk information | PASS — max deviation \< 10⁻¹⁰ |
| B4 | R | free | STAGES 3–4: Λ \= Z₀₁/√(Z₀₀Z₁₁) \= exp(−Γ+iχ); gate A1, A2, A3, A5 automatic for the Gaussian class; rank 2 and the phase remain discriminating | PASS — gate PASS for both surrogates |
| B5 | R | free | STAGE 5: a real symmetric boundary kernel gives χ \= 0 EXACTLY; a phase requires a named non-symmetric ingredient | PASS — χ \= 0 exactly vs χ ≠ 0 |
| B6 | X | cmp | STRUCTURAL ALIGNMENT: Γ \= −log|Λ| and −log|λ| \= μ, the locked dephasing rate — tautological, a coordinate observation | PASS — 0.1148346250 \= μ |
| B7 | D | cmp | PRE-REGISTRATION of the three outcomes, shown mutually distinguishable by the gate itself; two of the three are negative | declaration |
| B8 | D | free | DECLARATION: the protocol is NOT executed on ZS-S14; a Gaussian SURROGATE validates the instrument only, and no surrogate number is compared with λ | declaration |

Table A.2f. Block T — the clock and the correctly typed residual (NEW v1.6).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| T1 | R | free | THEOREM M57.T.1 (Clock Ill-Posedness): γ(τ) \= cos(gτ); at fixed coupling |γ| sweeps ALL of (0,1) as τ varies, so Λ is not a function of the action | PASS — range \[0.008, 0.999\] over 62 τ values |
| T2 | D | free | DECLARATION: τ\_Z absent from all six loaded files (0 occurrences); and the v1.5 claim that S\_S14 is unavailable is WITHDRAWN — Definition 3.1 is complete | declaration |
| T3 | R | cmp | THEOREM M57.T.2: R \= arg λ / (−log|λ|) is exactly cycle- and clock-independent | PASS — R \= 19.6739402770, n \= 1..23, dev \< 10⁻¹² |
| T4 | A | cmp | THEOREM M57.T.4: R \= (π/2 \+ arg z\*)/(−log((π/2)|z\*|)) — an identity; neither A nor Q enters | PASS — both decompositions exact |
| T5 | X | cmp | ANTI-NUMEROLOGY on R: 96,741-member signed algebraic-in-(A,Q) family, 0 hits at 1e-4 — a control whose outcome T4 predicts | PASS — nearest miss 1.3×10⁻² |
| T6 | A | free | COROLLARY M57.T.3: λ \= exp(−μ(1 − iR)); the residual is ONE REAL DIMENSIONLESS number, not one complex number | PASS — reconstruction to 10⁻¹² |
| T7 | D | cmp | DECLARATION: no Λ\_S14, Γ\_S14, χ\_S14 or R\_S14 computed. ZS-S21 proves diagonality and propagates weights but does NOT select them (three ratios free) | declaration |

Table A.2g. Block V — the event clock, the characteristic-function gate, and two refutations (NEW v1.7).

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| V1 | A | free | THE TWO CLOCKS SEPARATED: the one-step map depends only on the dimensionless product gτ, so no metric duration is meaningful at one-step level; a per-EVENT multiplier can be well posed where a finite-TIME one is not | PASS — (1,1) and (2,0.5) identical; (1,1) and (1,2) differ |
| V2 | R | cmp | DEFECT INDICES (1,1): D\_C \= D\_{C\*} \= √(1−|λ|²) \= 0.4529939978 — one coherence defect per record quantum; the pre-multiplier structural gate | PASS |
| V3 | R | cmp | Θ\_C(z) \= −C \+ zD\_{C\*}(I−zC\*)⁻¹D\_C collapses to the degree-1 Blaschke factor, is INNER on the circle, and Θ(0) \= −λ; complete unitary invariant (Sz.-Nagy–Foiaș) so the gate is overdetermined | PASS — max||Θ|−1| \= 2.0×10⁻¹² |
| V4 | X | cmp | CORPUS SUPPORT: ZS-Q18 already records Θ\_λ inner with unit multiplicity matching the ZS-M46 unit Abel translation, normalisation OPEN as CRT-4 / H-CLK — an existing named residual, not new machinery | PASS — observation |
| V5 | R | free | CLOSED-NEGATIVE (refutes this line’s own proposal): for strict QND with Z² \= I the zero-frequency Lamb shift ∝ Z†Z \= I is a GLOBAL phase; the single-kernel Lamb-shift/decoherence ratio route FAILS | PASS |
| V6 | D | free | STATUS DOWNGRADE: the Lambert–Dyson route L \= log(i)e^L goes to BOOTSTRAP-HYPOTHESIS — contraction shows the chosen equation is stable, not that it is selected; D₄ gives no exponential feedback and no branch of log i | declaration |
| V7 | D | free | THE SUCCESSOR GATE: defect indices (1,1), Θ\_S14 degree-1 inner, W V\_S14 W† \= U\_M46(1), then compare a\_S14 with λ. No metric duration required; nothing executed here | declaration |

Table A.2h. Block Y — audit of the v1.7 closing claim (NEW v1.8). Two parts survive, two fail.

| Tag | Class | Firewall | Statement | Result |
| ----- | ----- | ----- | ----- | ----- |
| Y1 | R | cmp | SURVIVES: Θ determines the multiplier including its PHASE — the zero of Θ is invariant under the coincidence equivalence Θ ↦ cΘ | PASS |
| Y2 | A | free | FAILS (omission): the v1.7 gate omitted the COMPLETELY NON-UNITARY hypothesis; Sz.-Nagy–Foiaș classifies c.n.u. contractions only. Added as gate stage 1b | PASS — hypothesis non-vacuous |
| Y3 | R | cmp | FAILS (independence): the Abel unit translation is obtained by dividing the Koenigs step log λ, which has BRANCHES — so the intertwiner node is entangled with the branch node, not independent of it | PASS — three distinct branch steps |
| Y4 | D | free | CORRECTED NODE COUNT: FOUR independent open prerequisites (pointer embedding, orbit-weight selection, branch normalisation, intertwiner) \+ one hypothesis (c.n.u.) \+ one deferred (τ\_Z). ‘Exactly two’ RETRACTED | declaration |
| Y5 | A | free | SURVIVES, weakened: the per-event gate is free of METRIC DURATION but NOT of a normalisation choice; ‘testable without duration’ is right, ‘free of every scale choice’ is not | PASS |

Cover: 96/96 PASS \+ 12/12 declarations | 0 FAIL (declarations counted in the FAIL line) | construction layer 55, proof-bearing (R+A) 46 | comparison layer 41 | classes R \= 44, A \= 28, X \= 24\. Firewall tags audited three times: v1.4 (F8, C2, C6), v1.5 (K6, K10, B7, with K9 rewritten), v1.7 (T2, T3, T6). Firewall tags audited twice: v1.4 moved F8, C2, C6 to the comparison layer; v1.5 moved K6, K10 and B7 as well, and REWROTE K9 as a general λ-free theorem over the whole disc so that it is construction-layer by content and not merely by tag. ZS-M56 v1.8’s 101-check regression is NOT part of this build (debt 1); check X5 reproduces its central inequality independently.

Table A.3. Debts and boundaries carried forward.

| \# | Debt or boundary |
| ----- | ----- |
| 1 | ZS-M56 v1.8's 101-check regression suite (zs\_m56\_verify\_v1\_8.py) is not present in this build. Its central inequality is reproduced independently (check X5); the suite is not executed. Load and run it before external submission. This is stated in the Verification Summary and cover, not only here. |
| 2 | ZS-Q16 v2.5 and ZS-A30 v2.1 are not loaded. Route B cannot be analysed (§12) and nothing is claimed about either. |
| 2b | ZS-A9's body is not loaded. Its Φ: F₂ → D₄ amenability functor is cited only through the loaded ZS-M35/M36 registration tables; whether it matches the natural surjection G\_D → D₄ of §8.4 is an audit item for a session with ZS-A9 open (Table 10.2). |
| 3 | ZS-A3 §2 (the ε potential, ε(r\_H) \= 0\) is inherited from the seed and not independently verified. Gate F-M57.14. |
| 4 | F-M56.19 is inherited: exactness of the grading beyond quadratic order, a symmetry-preserving regulator, and a ℤ₂-invariant background. §11.3 shows the third bites. |
| 5 | F-M56.21 is inherited: ZS-S1 §5.2 calls the ℤ₂-odd mode a gauge mode projected out, while ZS-M54 builds a two-dimensional physical Z-register. Unresolved, and §3.2 sharpens rather than settles it — the odd mode is now known to occupy half the register's unique quarter turn. |
| 6 | τ\_Z and ρ\_E belong to ZS-Q19, together with the Z-anchor reset clock of §11.3. By M56.7 the multiplier carries no evidential content while they are free. |
| 7 | F-M54-12 (instrument selection) is provably not closable at mean-operator level by M54.13. Not attempted. |
| 8 | No genuinely CPTP reduced channel is computed here. Route G's channel is CPTP but sits at L2; Route B's is unexamined. |
| 9 | The three-metric remains forbidden by ZS-A16 Theorem F. No continuum limit, no phenomenology, no new constant. |
| 10 | Whether the ZS-M56 v1.8 naming correction is issued as an erratum or as v1.9 is not this paper's call. |

## **Appendix B — Matrices, characters, and the retained D₄ lemma**

### **B.1 The two involutions in coordinates**

In the ZS-F0 §8 slot basis, with slot 0 the β₀ physical Z-mode and slot 1 the ℤ₂-odd Z-mode:

J \= antidiag(1, 1, …, 1\) ∈ O(11),  J|j⟩ \= |10 − j⟩,  J² \= I.  
J\_Z \= diag(+1, −1, \+1, \+1, \+1, \+1, \+1, \+1, \+1, \+1, \+1),  J\_Z² \= I.  
r \= J·J\_Z : |j⟩ ↦ ε\_j |10 − j⟩ with ε\_j \= −1 iff j \= 1;  r² ≠ I,  r⁴ \= I.

The seam orbits are (0, 10), (1, 9), (2, 8), (3, 7), (4, 6\) and the fixed slot {5}. The pointer is the pair of slots {0, 1}, which is not a union of seam orbits — that is Theorem M57.1 restated combinatorially, and it is the shortest way to see it.

### **B.2 D₄ character table and the isotypic projector**

Table B.1. D₄ characters, classes ordered \[e, r², r, s, rs\] with sizes \[1, 1, 2, 2, 2\].

| Irrep | e | r² | r | s | rs | Where it sits in ℂ¹¹ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| A₁ | 1 | 1 | 1 | 1 | 1 | the J-even vector of each non-E pair, plus |5⟩ — 5 copies |
| A₂ | 1 | 1 | 1 | −1 | −1 | absent (multiplicity 0\) |
| B₁ | 1 | 1 | −1 | 1 | −1 | absent (multiplicity 0\) |
| B₂ | 1 | 1 | −1 | −1 | 1 | the J-odd vector of each non-E pair — 4 copies |
| E | 2 | −2 | 0 | 0 | 0 | span{|1⟩, |9⟩}, exactly once |

The E-isotypic projector is P\_E \= (2/8) Σ\_{g∈D₄} χ\_E(g) g, which evaluates to |1⟩⟨1| \+ |9⟩⟨9| (check N8). Under the relabelling J\_Z^{(k)} it evaluates to |k⟩⟨k| \+ |10−k⟩⟨10−k| for every admissible k (check N10).

### **B.3 The retained D₄ lemma (formerly Theorem M57.D.2)**

**Lemma B.1.** \[PROVEN, pure representation theory; NON-CLAIM as a physical obstruction\] Let V \= 5A₁ ⊕ 4B₂ ⊕ E as a D₄-module. Let ℋ\_S ≅ E and let ℋ\_E be two-dimensional carrying either E or A₁ ⊕ B₂. Then no D₄-equivariant isometry ℋ\_S ⊗ ℋ\_E ↪ V exists.

Table B.2. The two vertices, decomposed by character arithmetic (checks D9, D10).

| ℋ\_S | ℋ\_E | ℋ\_S ⊗ ℋ\_E | Verdict against V |
| ----- | ----- | ----- | ----- |
| E | E | A₁ ⊕ A₂ ⊕ B₁ ⊕ B₂ | blocked — mult(A₂) \= mult(B₁) \= 0 in V |
| E | A₁ ⊕ B₂ | 2E | blocked — 2 \> mult(E) \= 1 |
| A₁ ⊕ B₂ | A₁ ⊕ B₂ | 2A₁ ⊕ 2B₂ | not blocked — but neither factor carries E |

Lemma B.1 is retained because it is true and may be reusable. It is not applied to the Z-Spin mediator vertex, because by Corollary M57.3a the pointer is neither E nor A₁ ⊕ B₂ — it is not a D₄-module at all. Any future use must first exhibit an object that genuinely carries E, and by Theorem M57.3 the only such object in this register is span{|1⟩, |9⟩}, which straddles the sector boundary.

## **Appendix C — Correction log**

Table C.1. Every claim corrected, withdrawn or reversed relative to the seed reports and the parent. Nothing is deleted; the superseded statement is recorded in place.

| Source | Superseded statement | Correction in ZS-M57 v1.0 |
| ----- | ----- | ----- |
| Seed v1.1 §1.2 (ii) | “A J-preserving subsystem is not excluded — §1.4 exhibits one.” | REVERSED (§2.2, §2.4). The exhibited subsystem lives in a different register; under the corpus grading both of its factors are central. Rule R10′. |
| Seed v1.1 §1.3 | A J-compatible sector split with Z on the pair (4, 6), X on (3, 7\) \+ {5}, Y on three pairs. | Not the corpus register (§2.1, §2.4). Registered as true-by-construction instance 8, mechanism: basis insertion. |
| Seed v1.1 §1.5 | The trichotomy F-M57.11 is a physical choice among three branches. | It is a domain fact (§4.1). Two branches presuppose an operator that does not exist on the pointer. |
| Seed v1.1 §2.2 | ℂ^Q \= ((Q+1)/2)A₁ ⊕ ((Q−1)/2)B₂ ⊕ E. | ERRATUM: the closed form sums to Q \+ 2\. Corrected to ((Q−1)/2)A₁ ⊕ ((Q−3)/2)B₂ ⊕ E (§3.1, check D8b). The seed's Table 2.1 was already correct. |
| Seed v1.1 §2.3 | Theorem M57.D.2, the D₄ Multiplicity Obstruction, as the successor to M56.21′. | WITHDRAWN as a physical obstruction (§4.3), NON-CLAIM. Retained as Lemma B.1, PROVEN pure representation theory. |
| Seed v1.1 §2.3 | “Let the pointer system carry E — the unique block on which a non-central involution acts irreducibly.” | The pointer is span{|0⟩,|1⟩} and E is span{|1⟩,|9⟩} (Thm M57.3). The premise is false in the corpus register, not merely unjustified. |
| Seed v1.1 Table 3.1 | A fourth specification constraint: D₄ multiplicity. | WITHDRAWN (Table 9.1). Candidates are scored on three constraints. |
| Seed v1.1 Table 3.2 | Internal J-pair (3, 7): non-central yes, 2 odd operators, score 2/4. | Central under J\_Z, 0 odd operators, score 1/3 (Table 9.2, checks N11 and S5). |
| Seed v1.1 §6.3 | Route G's layer is a labelling question with two honest resolutions. | Resolution 1’s AMPLITUDE route is CLOSED-NEGATIVE by Theorem M57.G′ (§6.2); the angle route is OPEN. Resolution 2 is adopted and declared in §0. |
| ZS-M57 v1.0 draft, Theorem M57.G | “θ\_D is not an algebraic function of A and Q, via θ\_D algebraic ⇒ cos θ\_D algebraic.” | RETRACTED (§6.2). The implication is false: by Lindemann–Weierstrass cos of a nonzero algebraic number is transcendental (cos 1 transcendental, check G3c), so |λ| \= cos θ\_D transcendental says nothing about θ\_D. Replaced by Theorem M57.G′, which closes only the amplitude route |λ| \= cos θ\_D, plus Lemma M57.G.0 and Corollary M57.G.1. |
| ZS-M57 v1.0 draft, Abstract | ℂ^Q \= ((Q+1)/2)A₁ ⊕ ((Q−1)/2)B₂ ⊕ E printed in the Abstract. | ERRATUM: this sums to Q \+ 2\. The Abstract now carries the correct ((Q−1)/2)A₁ ⊕ ((Q−3)/2)B₂ ⊕ E (= 5A₁ ⊕ 4B₂ ⊕ E at Q \= 11), matching §3.1 and check D8b. The v1.0 draft had corrected the seed’s form in §3.1 but reprinted the wrong one in the Abstract — the same error it flagged. |
| ZS-M57 v1.0 draft, Acknowledgements | “Every numerical figure appears verbatim in one seeded run.” | Corrected: Haar-random quantities (M57.P) are reported as bounds \< 10⁻¹³ with the seed-57 mantissa parenthetical, because the exact value is platform-dependent. Only deterministic figures are claimed verbatim. |
| ZS-M57 v1.7, closing statement | “The remaining physical nodes are exactly two — an action-derived C\_S14 or Θ\_S14, and the exact CRT-4/H-CLK intertwiner — and both are testable without duration.” | PARTLY RETRACTED (§15.7, Block Y). The node count is FOUR, not two: pointer embedding and orbit-weight selection were folded into ‘construct C\_S14’ though each is separately OPEN (ZS-S21 propagates weights but does not select, leaving three ratios), and the branch normalisation is a fourth. Worse, the intertwiner is NOT independent of the branch node: the ZS-M46 Abel coordinate normalises the seam step to u ↦ u \+ 1 by dividing the Koenigs step log λ, so the unit IS a branch choice (check Y3). The gate also omitted the COMPLETELY NON-UNITARY hypothesis, without which Θ is not a complete invariant (check Y2); it is added as stage 1b. What SURVIVES: Θ does determine the phase, since the zero of Θ is coincidence-invariant (Y1), and the per-event gate genuinely needs no metric duration — though it does need a normalisation, so ‘free of every scale choice’ would be wrong (Y5). |
| ZS-M57 v1.7, Abstract and Version History (length) | Abstract ran to five pages and the Version History to seven, each restating corrections already given in full in Appendix C and in the body. | COMPACTED in v1.8. The seven per-version abstract paragraphs are replaced by two summary paragraphs, and the Version History entries are reduced to their decisive changes with detail delegated to Appendix C. No correction, theorem, gate, ledger row or reference is removed — the no-deletion discipline applies to CONTENT, and what is deleted here is duplication of content that remains in place elsewhere. |
| ZS-M57 v1.6, Theorem M57.T.2 and check T3 | “R \= arg λ/(−log|λ|) is exactly cycle-independent; verified n \= 1..23.” | RETRACTED and REPLACED by M57.T.2′ (§14.3, check T3a). A channel fixes Arg λ only mod 2π, so the generator logarithm has branches and the clock-free datum is the PROJECTIVE RAY \[Γ : Ω\_k\] — five distinct R\_k for k \= −2..2, none selected by the channel. The v1.6 check computed (n·arg)/(nμ), n-independent by algebra and verifying nothing; the principal argument WRAPS (Arg(λ²) \= −1.7647, ratio −7.6836 not 19.6740); and the code tested eight values of n, not twenty-three. Check T3 is now a retraction control verifying the wrap for all 22 tested n; the unwrapped lift is an explicit hypothesis and branch selection is OPEN. |
| ZS-M57 v1.6, Theorem M57.T.1 scope | Read as establishing that Λ\_S14 is universally undefined. | NARROWED (§14.2). PROVEN within the collision family; universal ill-posedness is DERIVED-CONDITIONAL on the absence of a primitive slab/event prescription, because ZS-S24 carries a one-step transfer family T\_a and a structurally selected primitive step would define a dimensionless map. §15 shows the missing prescription may be an event count rather than a duration. |
| ZS-M57 v1.6, Corollary M57.T.3 and check T6 | “Given R and any independently fixed clock the multiplier follows”; T6 tagged A / construction-layer. | CORRECTED twice. R plus a DURATION does not suffice: what is needed is R together with μ \= Γτ, so the action must supply the RATE Γ — one further arrow than v1.6 counted. And the reconstruction is an identity among comparison-layer quantities (μ, R, λ all derive from λ), so T6 is reclassified X / comparison and is not proof-bearing. |
| ZS-M57 v1.6, check T2 | The PASS-bearing string asserted an exhaustive six-file text search for τ\_Z, while the condition tested only theta\_D \> 0\. | CORRECTED by labelling: the search is now marked an OFF-LEDGER OBSERVATION performed outside the suite, and the check states plainly that it verifies only that the comparison-layer constants are loaded. This is the same ledger-integrity fault v1.5 corrected in F1/F9/C3, recurring in a declaration; T2 is also retagged to the comparison layer since its condition consumes theta\_D. |
| ZS-M57 v1.6 deep exploration, the Lamb-shift mechanism | “R \= Lamb shift / decoherence rate, both from one influence kernel, hence clock-free.” | CLOSED-NEGATIVE (§15.4, check V5). For strict QND with Z² \= I the zero-Bohr-frequency Lamb-shift term is proportional to Z†Z \= I, a GLOBAL phase; the relative pointer phase (Ω/2)Z is not generated. The route this line proposed for itself is refuted. |
| ZS-M57 v1.6 deep exploration, the Lambert–Dyson mechanism | Registered HYPOTHESIS-strong. | DOWNGRADED to BOOTSTRAP-HYPOTHESIS (§15.4, declaration V6). λ \= −W₀(−log i) is PROVEN, and the equation is a contraction at its solution, but contraction does not SELECT the equation; D₄ supplies a quarter-turn class, not the exponential feedback e^L, and does not fix the branch of log i. |
| ZS-M57 v1.5, §12.4 and §13 and debt 7 | “The Standard-Model file loaded in this build is a compact summary; it contains no influence functional, no boundary return map, and no transfer-operator identification.” | WITHDRAWN (§14.1). The ZS-S14 master action IS present in full at Definition 3.1, and the corpus additionally supplies the ZS-S21 Osterwalder–Seiler / Lüscher transfer-matrix construction and the ZS-S24 reflection-positive slab. The v1.5 diagnosis rested on a grep for three phrases and mis-described the material. The corrected diagnosis is §14.2: what is absent and load-bearing is the slab clock τ\_Z (0 occurrences in six files), and by Theorem M57.T.1 its absence makes Λ\_S14 undefined rather than merely uncomputed. |
| ZS-M57 v1.4–v1.5, Table 12.2 step 6 | Terminal gate: compute Λ\_S14 and compare with λ. | REVISED (§14.6, Table 14.2). By Theorem M57.T.1 that comparison is not well posed without τ\_Z. Step 6 now compares the clock-free R\_S14 \= arg Λ\_S14/(−log|Λ\_S14|) with R \= 19.6739402770; the Λ-level comparison becomes step 7, conditional on τ\_Z being independently derived. A step 0 requiring an explicit clock declaration is added. |
| ZS-M57 v1.4, ledger K6, K9, K10 | Tagged construction-layer (λ-free). | RECLASSIFIED: K6 compares arccos|λ| with θ\_D, K10’s PASS condition quotes the target Λ, and K9 evaluated the polar identity AT λ. K6, K10 and the new B7 are now comparison-layer; K9 is REWRITTEN as a general theorem over arbitrary Λ in the punctured disc, so it is λ-free by content rather than by tag. Cover counts recomputed by the suite rather than asserted. |
| ZS-M57 v1.4, check K6 | The quantity arccos|λ| named θ\_S14. | RENAMED θ\_split and demoted to a comparison-layer TAUTOLOGY control. No S14 slab angle has been computed, so nothing may carry that name (rule R10′); only a value derived FROM the action may be called θ\_S14. |
| ZS-M57 v1.4, check C4 | Reparametrisation used Λ \= cos φ \+ i s sin φ while the construction used γ \= cos φ − i s sin φ. | UNIFIED on the construction’s convention: λ \= cos φ − i s sin φ, s \= −Im λ / sin φ. The v1.4 suite carried two conventions in one file, which is how the v1.3 sign error survived one round of correction. |
| ZS-M57 v1.4, check C5 | Anti-numerology family restricted to 0 \< v \< 4 while the target s\* is NEGATIVE. | CORRECTED: the family is now SIGNED (both \+v and −v are tested). The v1.4 null for s was vacuous — it could not have found a negative value — and only the φ\* half of that check was meaningful. |
| ZS-M57 v1.4, ledger F1, F9, C3 | Ledger statements still printed retracted claims as PASS: ‘zero choices’ (F1), ‘the entire F₂ lives below the mean layer’ (F9), and an unqualified state-only phase origin (C3). | REWRITTEN in the ledger itself. A false statement printing PASS is worse than one retracted later in prose, because the ledger is what a successor greps. F1 now states the U(1) freedom, F9 the one-step scope, and C3 carries the qualifier ‘within a single graded collision with no independent system holonomy’. |
| ZS-M57 v1.4, Corollary M57.K.2 | “the U(1) gauge is FIXED.” | SCOPED (§12.1): fixed RELATIVE TO the locked register basis and the chosen positive shift S. Which vertex the S14 action selects — B\_F, R\_F, or a time-ordering of both — is OPEN and is not settled by the corollary. |
| ZS-M57 v1.4, §12.4 and check K10 | “a FILE-AVAILABILITY limit rather than a mathematical one.” | SOFTENED to CURRENT CORPUS-DEFINITION INSUFFICIENCY. Even with the full action, the reduced channel needs a slab identification and duration, a boundary state, gauge fixing with BRST/BFV projection, an initial-correlation assumption, a coarse-graining prescription, a regularisation, and a continuum-or-finite-cell choice; whether the corpus defines all of these is undetermined. |
| ZS-M57 v1.4, Abstract and §11 | s\* printed as \+0.8353812873 in the Abstract and the §11.4 table; ‘zero choices’ retained in the Abstract. | SYNCHRONISED with the §11.2 correction: s\* \= −0.8353812873 throughout, and the Abstract now says ‘canonical up to a U(1) gauge, which §12.1 fixes relative to the register’. |
| ZS-M57 v1.3, §11.2 and check C1 | s\* \= Im λ / sin φ\* \= \+0.8353812873, with γ \= cos φ − i s sin φ. | CORRECTED (§11.2). The two are inconsistent: that pair returns λ̄, not λ. With the paper’s convention Z\_path \= |0⟩⟨0| − |1⟩⟨1| and φ ∈ (0, π), the correct value is s\* \= −Im λ / sin φ\* \= −0.8353812873. The v1.3 SUITE returned λ only because it built the pointer basis with a routine returning ASCENDING eigenvalues, silently ordering it (−1, \+1) and swapping |0⟩ with |1⟩. Both text and suite are fixed and the basis ordering is now set explicitly. |
| ZS-M57 v1.3, §11.4 | “dynamics/state dichotomy with no third case.” | CORRECTED (§11.4, §12.2, check K5). A third case exists and is ZS-M54’s own factorisation Φ\_λ \= U\_χ ∘ D\_r: a grading-INVARIANT carrier at θ\_D gives the real attenuation |λ|, and an independent system-side Z-Spin transit holonomy supplies e^{i arg λ}, reproducing Φ\_λ exactly with no grading broken. The dichotomy holds only WITHIN a single graded collision with no independent holonomy; the unqualified claim contradicted ZS-M54’s own phase/attenuation separation. |
| ZS-M57 v1.3, ledger F8, C2, C6 | Tagged construction-layer (λ-free). | RECLASSIFIED to comparison layer: F8 compares against |λ|, C2 verifies a state built from s\*(λ), C6 quotes φ\* and s\*. Cover counts recomputed (construction 43→47 with Block K’s λ-free additions; comparison 23→28). |
| ZS-M57 v1.3, §10.3 and §16.4 | “cannot be seen from inside any finite register”; “No claim of this paper matches λ at all.” | SYNCHRONISED with §8.4 and §§11–12 respectively: the first now says finite register SYMMETRY GROUP; the second is scoped to the sections preceding §11, since §§11–12 match λ deliberately and declare the match non-evidential. |
| ZS-M57 v1.3, Abstract | “no environment satisfying all constraints is exhibited” retained alongside the §11 construction. | CORRECTED: the Abstract now distinguishes ‘an admissible carrier EXISTS’ (proved, §§11–12) from ‘ZS-S14 SELECTS that carrier’ (not shown, F-M54-16′). |
| ZS-M57 v1.3, Table 15.2 reading | Scoreboard read as showing that no graded candidate satisfies the three constraints. | SCOPED: the table records the candidate search as of the v1.1 audit and is retained unchanged; §11 exhibits an object scoring 3 of 3, so its lesson is that none of the candidates THEN CONSIDERED worked, not that none exists. |
| ZS-M57 v1.2, §9.2 | “the entire F₂ lives strictly below the mean channel.” | RETRACTED (§9.2, check W1). With the carrier retained, composed words ARE mean-distinguishable: γ(xx) \= cos 2θ\_D \= 0.5895928759 ≠ γ(xy) \= cos²θ\_D \= 0.7947964380. Correct claim: the ONE-STEP generator label is mean-invisible. Replaced by the stronger Theorem M57.P′ (every word has a real multiplier). |
| ZS-M57 v1.2, §8.4 | “The free object cannot be realised inside any finite register.” | CORRECTED (§8.4). False as stated: F₂ embeds faithfully in SO(3) ⊂ GL(3, ℝ) and this paper realises G\_D by 3×3 matrices. Correct statement: G\_D is not contained in the finite register symmetry GROUP D₄, though it acts faithfully in finite DIMENSION. The accompanying causal claim (‘this is why nine versions failed’) is withdrawn as unproved; only the compatibility statement is retained. |
| ZS-M57 v1.2, §8.1 / M57.F.0 | “Zero choices were made: the generator pair is the complete odd operator space.” | CORRECTED (§8.1). The odd PLANE and the perpendicularity are forced; the first axis carries a continuous U(1) freedom B\_E \= cosα σ\_x \+ sinα σ\_y. Correct statement: canonical up to the U(1) centraliser of J\_E. Results in §§8–9 are unaffected (conjugate groups); M57.F.0 re-registered ALGEBRAIC / DERIVED-CONDITIONAL on a chosen odd direction. |
| ZS-M57 v1.2, §9.3 | Paradoxicality announced as “the real fourth specification constraint”. | DOWNGRADED (§9.3). Tarski’s alternative excludes only TOTAL finitely-additive invariant valuations on all subsets; no physical carrier must carry one. It is a RECORD-THEORETIC corollary, constrains no candidate, and is not a row of the carrier specification. §11 exhibits an admissible carrier, confirming it is not an existence obstruction. |
| ZS-M57 v1.2, §8.2 | Świerczkowski cited as the anchor with no prior-art statement. | CORRECTED (§8.2, check C7). de Groot, Canad. J. Math. 8, 256 (1956) is prior for the general transcendental free-rotation theorem (his condition on tan²(θ/2) is equivalent to ours on cos θ). M57.F.1 is an APPLICATION at θ\_D; Lemma M57.F.L is retained as self-contained, not as novel. |
| ZS-M57 v1.2, ledger F10 | F10 tagged construction-layer (λ-free). | RECLASSIFIED to comparison layer: F10 uses rotation matrices built from θ\_D \= arccos|λ|. Cover counts corrected accordingly (construction 42→43 with the new λ-free C2, comparison 16→23). |
| ZS-M57 v1.2, checks S4/S6 | Conditions contained the literal pattern ‘True is not False and …’. | REMOVED. Vestigial and inconsistent with this line’s own criticism of literal-True conditions; the substantive clauses are retained unchanged. |
| ZS-M57 v1.2, Table 8.1 and ledger F3 | Random-word minimum printed as 0.439570 (a probe-script value). | CORRECTED to the suite value 0.502999 (seed 57). The ‘deterministic figures verbatim’ claim now holds. |
| ZS-M57 v1.2, §14.1 / Table 15.1 header / §6.4 | Stale v1.0 firewall counts (35/26/12); table header ‘Effect of ZS-M57 v1.0’; §6.4 heading printed twice. | All corrected; editorial residue of the additive v1.2 build removed. |
| ZS-M57 v1.1, §6 (reading, not content) | Theorem M57.G′ presented solely as a closure (“the amplitude route is closed”). | REREAD in v1.2, not retracted: §§7–9 read the same theorem as the hypothesis of the Świerczkowski–Wagon free-rotation theorem. Both readings stand; nothing in v1.1 is withdrawn. Additions are strictly additive (no-deletion discipline). |
| Seed v1.1 outcome G | “The largest possible outcome, and the least likely.” | CLOSED-NEGATIVE (§4.2). Excluded outright. |
| ZS-M56 v1.8, title and §7 | “seam-ℤ₂-preserving”; “the seam ℤ₂ of ZS-S1 §5.2”. | Naming correction to “Z-internal-ℤ₂” (§4.4). Theorem, inequality, scope and 101 checks unaffected. |
| Seed rule R10 | Name every involution by formula and definition number. | STRENGTHENED to R10′: name it by formula, definition number, and the register basis in which the formula holds (§4.4). |
| This paper, first draft | Check N1 asserted L\_Z \= ½I − ½J\_seam with J\_seam read as the node-basis swap σ\_x, which does not equal diag(0, 1). | CORRECTED before release. J\_seam|\_Z is the eigenmode-basis parity diag(+1, −1); the identity then holds exactly. Recorded because the failing check was a declaration, and the first draft's cover excluded declarations from its FAIL count — so a fail-closed ledger reported zero failures while one check was failing. The cover now counts declarations in the FAIL line, and the exit code is checked directly rather than through a pipe. |

## **Appendix D — Falsification gates**

Multi-layer, per corpus convention: mathematical or theoretical collapse (immediate rejection), simulation or internal-consistency collapse (revision required), and external collapse (rejection by data or by an unloaded corpus file).

Table D.1. Layer 1 — mathematical / theoretical. Any of these fires and the corresponding result is rejected immediately.

| Gate | Fires if | Consequence |
| ----- | ----- | ----- |
| F-M57.11 \[RESOLVED\] | A register basis is exhibited in which J\_Z \= I₁₁ − 2|1⟩⟨1| holds AND the Z-sector is J-invariant. | §2–§4 collapse entirely; outcomes F and G reopen; M57.D.2 must be reinstated. This is the single decisive gate of the paper. |
| F-M57.19 (NEW) | The corpus is shown to place the Z-sector at slots other than {0, 1} in the ZS-F0 §8 ordering. | Theorems M57.1–M57.3 must be recomputed in that ordering. The relabelling sweep (N10) shows the D₄ content survives; the pointer statements do not automatically. |
| F-M57.F1 (NEW v1.2) | A reduced word w with w(θ\_D) \= I is exhibited. | Theorem M57.F.1 is falsified immediately — AND by Lemma M57.F.L the word is a proof that |λ| is algebraic, so Theorem M57.G′ and (H-TRANS) fall with it. Single-point failure, honestly declared; the standing challenge is open to any reader with a computer. |
| F-M57.F2 (NEW v1.2) | (H-TRANS) is refuted (η\_topo route of §6.3) without an explicit word. | Theorems M57.F.1–F.2 and Corollary M57.F.3 lose their conditional status and become OPEN (not false: freeness holds for some algebraic cosines, e.g. 1/3). M57.G′ falls. |
| F-M57.Y1 (NEW v1.8) | A successor treats Θ\_S14 as a complete invariant without verifying that C\_S14 is completely non-unitary. | The classification theorem does not apply to contractions with a unitary summand; the gate’s stage 3 is void without stage 1b. |
| F-M57.Y2 (NEW v1.8) | A successor treats the CRT-4/H-CLK intertwiner as independent of the logarithmic branch, or normalises the Abel step to 1 without declaring which branch of log λ was used. | The unit normalisation IS a branch choice (check Y3). An intertwiner claim must state its branch, or the comparison inherits the ambiguity that Theorem M57.T.2′ registered OPEN. |
| F-M57.V1 (NEW v1.7) | Any successor reports a clock-free ratio without declaring which logarithmic BRANCH it used, or treats R₀ as selected by the channel. | Void by Theorem M57.T.2′: the channel selects no branch. A branch claim needs a continuous lift from the identity, a phase-unwinding rule, an action-derived generator, or an exact CRT-4/H-CLK equality. |
| F-M57.V2 (NEW v1.7) | A relative pointer phase is claimed from a single strict-QND influence kernel as a Lamb-shift effect. | Excluded by check V5: the zero-frequency Lamb shift is central for Z² \= I. The phase requires one of the named sources of Table 13.1. |
| F-M57.V3 (NEW v1.7) | The equation L \= log(i)e^L is written down for the S14 boundary self-energy without an independent action-side derivation of the exponential self-dependence. | Premise insertion; declaration V6 registers the route at BOOTSTRAP-HYPOTHESIS precisely to prevent this. |
| F-M57.T1 (NEW v1.6) | Any successor computes Λ\_S14 using a FITTED or unstated slab duration, or reports agreement of |Λ\_S14| with |λ| without an independently derived τ\_Z. | Void by Theorem M57.T.1: at fixed coupling the modulus sweeps all of (0,1) as τ varies, so such an agreement is guaranteed by construction. Only the clock-free R comparison is admissible before debt 6 is paid. |
| F-M57.T2 (NEW v1.6) | τ\_Z is derived and the resulting Λ\_S14 disagrees with λ while R\_S14 \= R. | The dynamics is vindicated and the failure is LOCATED IN THE CLOCK: the phase-to-attenuation structure is right and the cycle identification is wrong. This is a diagnostic outcome, not a refutation of §§12–13. |
| F-M57.T3 (NEW v1.6) | R\_S14 is computed from the action and differs from 19.6739402770 beyond tolerance. | The i-tetration identification of the multiplier is REJECTED clock-independently — it cannot be rescued by adjusting τ\_Z. This is the sharpest falsification this line has available. |
| F-M57.B1 (NEW v1.5) | Any successor treats passage of the structural gate as evidence about the VALUE of the multiplier. | Void by Theorem M57.B.1: the gate is passed by every α in the punctured disc. Sub-gate A and sub-gate B are logically independent and must both be run. |
| F-M57.B2 (NEW v1.5) | A phase is claimed from free-group asymptotics, a random walk on collision words, or an invariant trace over the paradoxical sphere. | Excluded by Corollary M57.P″ (every mixture is real) and, for the trace form, by Corollary M57.F.3 (no total invariant valuation exists). The claim is void without a named non-symmetric ingredient from Table 13.1. |
| F-M57.B3 (NEW v1.5) | A surrogate number from §13.6 is quoted as a Z-Spin result, or a surrogate Λ is compared with λ. | Immediate misuse: declaration B8 states the surrogate validates the instrument only. The surrogate is not the S14 action and no comparison is licensed. |
| F-M57.K1 (NEW v1.4) | An S14 open-slab Choi operator is exhibited that FAILS any row of the structural gate (Hermiticity, positivity, Tr\_out C \= I, supp C ⊆ Δ\_Z, rank 2). | The measurement–action bridge is CLOSED-NEGATIVE in its present form: Φ^QND is not the reduced S14 channel, and ZS-M54’s reconstruction needs a different mediator class. |
| F-M57.K2 (NEW v1.4) | The structural gate PASSES but Λ\_S14 ≠ λ beyond tolerance, on a construction that never saw λ. | The carrier structure of §§11–12 survives and the i-tetration identification of the multiplier is REJECTED — a negative result about ZS-M54, not about this paper. |
| F-M57.K3 (NEW v1.4) | Any successor computes Λ\_S14 using λ, z\*, θ\_D, φ or s anywhere in the construction, or fits (θ, χ) and reports the agreement as evidence. | The comparison is void by Theorem M57.C.2 and check K9. The blind-construction requirement is the whole content of the gate. |
| F-M57.C1 (NEW v1.3) | Any successor cites §11 as a closure of F-M54-16′, or reports the exact agreement of §11.2 as evidence. | Immediate misuse: by Theorem M57.C.2 the agreement is guaranteed a priori (two fits, two targets, zero residual). Declaration C6 is the binding statement. |
| F-M57.C2 (NEW v1.3) | An S14 open-slab calculation yields a coupling angle or carrier polarisation differing from φ \= 2.1729483796 or s \= 0.8353812873 beyond stated tolerance. | The two-dimensional graded carrier route is CLOSED-NEGATIVE and Φ\_λ is not the reduced S14 channel; ZS-M54’s reconstruction would need a non-graded or higher-rank mediator. |
| F-M57.C3 (NEW v1.3) | A grading-INVARIANT carrier state is exhibited together with a complex multiplier from any word of the collision group. | Theorem M57.P′ is false and §11.1’s uniqueness argument collapses; the dynamics/state dichotomy of §11.4 would admit a third case. |
| F-M57.F3 (NEW v1.2) | The claimed classical chain (Świerczkowski / Hausdorff–Banach–Tarski / Tarski alternative / Kesten) is found misquoted or misapplied. | The affected theorem reverts to OPEN and the import table of §15 must be corrected before any successor cites it. |
| F-M57.20 (NEW) | ℋ\_Z ∩ Jℋ\_Z ≠ {0} under any admissible reading of the corpus slot ordering. | Theorem M57.1 is falsified. Immediate rejection of §4. |
| F-M57.G (NEW) | |λ| is shown to be an algebraic function of A and Q (i.e. η\_topo is shown transcendental in a way that makes |λ| algebraic), OR an angle-route derivation of θ\_D from the action is exhibited. | Theorem M57.G′ is void or its scope is exceeded, and Route G Resolution 1 reopens. §0's L2 declaration reverts to a dependency statement. Note: M57.G′ already leaves the angle route OPEN, so exhibiting one is a completion, not a contradiction. |
| F-M57.G0 (NEW) | η\_topo \= |z\*|² is used as if algebraic without that being established. | Lemma M57.G.0 makes (H-TRANS) rest on η\_topo’s algebraicity, which is OPEN. Any proof that treats η\_topo as algebraic must cite where that is shown. |
| F-M57.P (NEW) | A counterexample is exhibited to M57.P: an exact grading-preserving QND collision with \[ρ\_E, J\_E\] \= 0 and Im γ ≠ 0\. | §5 collapses and the ZS-M54 layer split returns to a bookkeeping decision. |
| F-M57.15 | ZS-F0 Conjecture 8.14 is claimed closed. | Corollary M57.D.3′ constrains it; the register representation of the i-tetration linearisation remains unperformed. |

Table D.2. Layer 2 — simulation / internal consistency. Any of these fires and the paper requires revision.

| Gate | Fires if |
| ----- | ----- |
| F-M57.F4 (NEW v1.2) | Route S is executed with a record structure that is neither σ-measurable nor an amenable reduction, or the §11.5 dichotomy is silently bypassed. |
| F-M57.F5 (NEW v1.2) | Any successor reads rank 2, the 4/5 piece counts, or √3/2 as Z-Spin constants, or claims physical volume/energy doubling, Born-rule modification, or a 3-metric from §§8–10. |
| F-M57.1 | A proposed carrier is scored without reporting all three constraints of Table 9.1. |
| F-M57.2 | A stochastic measure is obtained by solving 𝔼\[e^{iφ}\] \= λ for its parameters rather than deriving them. The M56.7 trap. |
| F-M57.3 | A quenched phase is used while the λⁿ law is also asserted. The two are inconsistent at n \= 2\. |
| F-M57.4 | A ghost-sector multiplier is computed before CPTP on the physical subspace is established. |
| F-M57.5 | Any of ZS-M56 v1.8's 101 checks, or any locked constant, moves under anything in this paper. |
| F-M57.6 | A carrier is claimed external while admitting a J\_Z-preserving embedding into the register. |
| F-M57.8 | Any proof-bearing check inserts its own premise or evaluates a literal True. |
| F-M57.9 | A claimed agreement's two dependency sets intersect in λ or z\* and it is reported as evidence. |
| F-M57.10 | The paper claims to close F-M54-13 (objectivity). Record support is an amplitude; redundancy needs fragment mutual information. |
| F-M57.13 | mult(E) \= 1 is presented as a property of Q \= 11\. It holds for every odd Q. |
| F-M57.16 (NEW) | Any match between D₄ multiplicities and corpus constants is reported without a Monte-Carlo null. The decomposition is forced, so every such match is a theorem about odd integers. |
| F-M57.17 (NEW) | An outcome outside the pre-registered list A–H is introduced after computation, rather than a pre-registered branch being named. |
| F-M57.21 (NEW) | Any two operators are combined without both being written in the same explicitly named register basis. Rule R10′. |

Table D.3. Layer 3 — external. Rejection by data or by an unloaded corpus file.

| Gate | Fires if |
| ----- | ----- |
| F-M57.12 | Any ℤ₂ is referred to by the word “seam” without its defining formula and ZS-F0 definition number. |
| F-M57.14 | The ε-parity argument of §11.3 is used without stating the vacuum and localising to ε \= 0, or ZS-A3 §2 is found to differ from the inherited reading. |
| F-M57.18 | The ZS-F0 §11.8.5 transcendence budget (z\* transcendental) is retracted or narrowed so that (H-TRANS: |λ| transcendental) no longer follows through Lemma M57.G.0. |
| F-M57.22 (NEW) | ZS-Q16 v2.5, when loaded, is found to build a physical pointer algebra that does carry a non-central grading and does lie outside the register. Route B would then reopen at 3/3 and this paper's Table 9.2 would be superseded. |
| F-M57.23 (NEW) | The ZS-M56 v1.8 regression suite, when run, moves any of its 101 checks under the §4.4 naming correction. A naming correction must move nothing. |

## **Appendix E — Exploration record**

Recorded for auditability, in the corpus's five-step form.

**Step 0 — long list (7).** (L1) the D₄ multiplicity obstruction as the correct invariant; (L2) the trichotomy F-M57.11; (L3) the basis question — are J and J\_Z written in the same register ordering, and does each restrict to the pointer; (L4) Route S, the stochastic realisation; (L5) Route B, BRST ghost–antighost; (L6) Route G and its layer; (L7) the Real-Multiplier Lemma as a stand-alone negative.

**Step 1 — issue list (4, MECE, by influence).** (I1) domain: which involutions act on the pointer at all \[absorbs L3, and is logically prior to L1 and L2\]; (I2) resolution of F-M57.11 \[L2\]; (I3) the layer verdict for Route G \[L6\]; (I4) the λ-free positive result \[L7\]. **Dropped:** L1 is not dropped but demoted — it survives inside I1 as mathematics and loses its physical application. L4 (Route S) is scoped out as not executable in this build: the ZS-S14 stochastic sector is not derivable from the loaded files, and fitting it would fire F-M57.2. L5 (Route B) is dropped under rule R6: ZS-Q16 and ZS-A30 are not loaded and reasoning about them second-hand is what v1.7 had to withdraw.

**Step 2 — issue tree.** I1 → I2 → {I3, I4} → residual {Route S OPEN, Route B OPEN}. I1 is the root because both I2 and the retained content of L1 depend on whether the operators in question have the domains their statements assume.

Table E.1. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 domain | M57.1, M57.2, M57.3 — J does not restrict to the pointer; the hull is 4-dimensional; E \= span{|1⟩,|9⟩} | DERIVED |
| I1 (mathematics retained) | M57.D.1, closed form corrected | PROVEN |
| I2 trichotomy | F-M57.11 → “J\_Z only”; outcomes F and G closed-negative; M57.D.2 withdrawn | DERIVED / NON-CLAIM |
| I3 Route G layer | M57.G; Route G is L2 | DERIVED-CONDITIONAL on (H-TRANS) |
| I4 positive result | M57.P and Corollary M57.P.1 | PROVEN / DERIVED-CONDITIONAL |
| Route S | specified in four steps; not executed | OPEN |
| Route B | barred by rule R6 | OPEN |
| ZS-F0 Conj 8.14 | constrained by Cor. M57.D.3′ | HYPOTHESIS, unchanged |

**Step 4 — convergence.** Criterion: the number of nodes changing status in a re-traversal cycle must be strictly decreasing. Cycle 1 changed 6 nodes. Cycle 2 changed 1 (the §6.3 null was reframed after the search returned zero hits, so that the chance expectation is reported alongside). Cycle 3 changed 0\. 6 → 1 → 0: **CONVERGED**. The MECE decomposition is therefore not re-opened. Rule R5 was applied at cycle 2: the decomposition-type enumeration (tensor factor, subalgebra, operator-algebraic subsystem, stochastic mixture) was re-checked, and Route S remains the omitted branch — registered OPEN rather than absorbed.

**Step 5 — scoring against the previous sector.** ZS-M56 spent eight versions and seven audit rounds on a ℤ₂ multiplicity question, and its durable result was a one-line inequality about the multiplicity of a grading that acts. This paper's durable result is a one-line statement about a grading that does not act. Both are checkable in a page, both are λ-free, and both are of the class that has survived every round. Converged, corpus non-conflicting (no locked constant moves, ZS-M56 v1.8 stands), anti-numerology pre-registered and executed with its chance expectation reported. The central results are registered at DERIVED rather than HYPOTHESIS-strong because they are computed from PROVEN corpus definitions rather than posited — which is the one respect in which this paper is easier than its parent, and the reason its finding took a page rather than eight versions.

### **E.2 — the v1.2 deep exploration (the reversal)  \[COMPACTED v1.8\]**

Steps 0–2 and 4–5 of this exploration are compressed in v1.8; the traversal table below is retained in full, convergence was reached in three cycles, and every correction the exploration produced is recorded in Appendix C.

Table E.2. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 generators | M57.F.0 — the odd space IS the pair; zero choices | DERIVED |
| I1 lemma | M57.F.L — specialization with the square-multiplicity argument | PROVEN |
| I1 anchor | Świerczkowski at cos \= 1/3; exact integer certificate to depth 10 | IMPORTED-PROVEN \+ VERIFIED |
| I1 theorem | M57.F.1 — G\_D free of rank 2 at θ\_D | DERIVED-CONDITIONAL on (H-TRANS) |
| I2 paradox | M57.F.2 — S² is G\_D-paradoxical; Tarski alternative applies | DERIVED-CONDITIONAL |
| I2 record | M57.F.3 — no total collision-invariant record valuation; mean-invisible freeness | DERIVED-CONDITIONAL |
| I3 ladder | points/lines amenable (Banach 1923); the face is the first non-amenable rung; density in SO(3) | DERIVED-CONDITIONAL (density); the ladder itself IMPORTED-PROVEN |
| I4 scope | Born/σ-algebra/Route S untouched; ball → M58/A9; Φ-functor audit registered | NON-CLAIM / OPEN |

**Step 4 — convergence.** Cycle 1 changed 5 nodes (the generator canonicity was initially an assumption and became M57.F.0; the Kesten witness was added as the numerical face of non-amenability). Cycle 2 changed 1 (the F6 axis-distinctness criterion was corrected to account for repeated sampled words). Cycle 3 changed 0\. 5 → 1 → 0: **CONVERGED**. The MECE decomposition was not re-opened.

**Step 5 — scoring against the line.** Convergent; no corpus conflict (the D₄ kinematics, M50.NG, M54.13, the M58 seed's carrierless mandate and ZS-A16's metric prohibition are all consistent with, and in three cases explained by, the result); the anti-numerology control is EXECUTED, not pending — the entire structure reproduces at the Z-free angle arccos(1/3), so the qualitative content carries no Z-numerics and the Z-content is exactly the statement that θ\_D satisfies the hypothesis. Under the corpus scoring rule this registers the central results at DERIVED-CONDITIONAL on the single named import (H-TRANS), with the unconditional anchor and all finite certificates VERIFIED — strictly stronger than HYPOTHESIS registration, and honestly weaker than PROVEN by exactly one number: η\_topo.

### **E.3 — the v1.3 deep exploration (the carrier) \[HISTORICAL RECORD — superseded by E.4 and E.5\]  \[COMPACTED v1.8\]**

Steps 0–2 and 4–5 of this exploration are compressed in v1.8; the traversal table below is retained in full, convergence was reached in three cycles, and every correction the exploration produced is recorded in Appendix C.

Table E.3. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 word-level | M57.P′ — every word has a real multiplier; the long-word phase route is closed | DERIVED (proof \+ 411-word check) |
| I2 phase source | the carrier STATE must break the grading; unique surviving option | DERIVED |
| I2 construction | M57.C.1 — explicit carrier reproducing Φ\_λ exactly; specification satisfiable | DERIVED-CONDITIONAL on the imported λ |
| I3 parameter audit | M57.C.2 — λ ↔ (φ, s) bijection; 2 fits vs 2 targets; M56.7 trap fires | DERIVED / trap reported |
| I4 residual | F-M54-16′ restated as two numbers; dynamics/state dichotomy with no third case | OPEN (declaration C6) |
| S14 open slab | not attempted — compact file insufficient (debt 7\) | OPEN |

**Step 4 — convergence.** Cycle 1 changed 4 nodes (the construction was initially attempted with a grading-invariant state and failed — which is how M57.P′ was found). Cycle 2 changed 1 (the off-diagonal convention gave λ̄ before the sign of s was fixed). Cycle 3 changed 0\. 4 → 1 → 0: **CONVERGED**.

**Step 5 — scoring against the line.** The positive result of this version is an EXISTENCE and REDUCTION result, not a bridge: it removes the possibility that the specification was vacuous, forces the phase onto the carrier state, and reduces F-M54-16′ to two scalars a slab calculation can deliver. Its evidential content for the bridge itself is zero by Theorem M57.C.2, and the version says so in the Abstract, in §11.3, in declaration C6 and in gate F-M57.C1 — four places, because the temptation to read §11.2 as a closure is the single largest misuse risk this paper carries.

### **E.4 — the v1.4 deep exploration (frame, third case, one number)  \[COMPACTED v1.8\]**

Steps 0–2 and 4–5 of this exploration are compressed in v1.8; the traversal table below is retained in full, convergence was reached in three cycles, and every correction the exploration produced is recorded in Appendix C.

Table E.4. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 frame | M57.K.1–K.2 — A\_F, B\_F, R\_F, J\_E from S, P\_E, J\_Z; U(1) gauge fixed by Δ \= 8 | DERIVED, λ-free |
| I1 consistency | E-block shares |1⟩ with the pointer: operators yes, in-register subsystem no | DERIVED (M56 respected) |
| I2 split | M57.K.3 — grading-invariant attenuation cos θ\_D \+ independent holonomy e^{iχ} | DERIVED-CONDITIONAL on the imported λ |
| I2 Lorentz | selection rule and complex structure only; the intertwiner Ξ is not in the corpus | NON-CLAIM / OPEN |
| I3 residual | structural gate \+ one complex number Λ; three pre-registered outcomes | DERIVED (statement), OPEN (execution) |
| I4 value | only the i-tetration fixed point carries a transcendental multiplier; Koenigs intertwiner K absent | HYPOTHESIS-weak |
| S14 CTP kernel | not executable from the loaded compact file | OPEN (debt 7\) |

**Step 4 — convergence.** Cycle 1 changed 5 nodes (the frame construction succeeded and immediately exposed the v1.3 sign error, since the corrected frame made the basis convention explicit). Cycle 2 changed 1 (the third case was promoted from a remark to Theorem M57.K.3 after the composite was verified CPTP and QND). Cycle 3 changed 0\. 5 → 1 → 0: **CONVERGED**. Two nodes remain OPEN by construction — the S14 kernel and the Koenigs intertwiner — and both are file-limited rather than argument-limited.

**Step 5 — scoring against the line.** The version’s value is that it makes the remaining question small and blind-testable: the frame is fixed with no free parameter, the structural gate is four checkable conditions, and the comparison is one complex number. Its evidential contribution to the bridge remains ZERO by Theorem M57.C.2, and the version says so in the Abstract, §12.4, check K9, declaration K10 and gate F-M57.K3. The honest one-line summary of v1.2–v1.4 is: the question ‘which carrier?’ is now nearly closed, and the question ‘what is the actual S14 multiplier?’ is all that is left.

### **E.5 — the v1.5 deep exploration (the protocol)  \[COMPACTED v1.8\]**

Steps 0–2 and 4–5 of this exploration are compressed in v1.8; the traversal table below is retained in full, convergence was reached in three cycles, and every correction the exploration produced is recorded in Appendix C.

Table E.5. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 underdetermination | M57.B.1 — the gate admits exactly {Φ\_α : 0 \< |α| \< 1} | DERIVED, λ-free |
| I2 phase routes | M57.P″ — no mixture over words is complex; walk operator self-adjoint | DERIVED |
| I2 enumeration | four named candidates remain; the free-group route is CLOSED-NEGATIVE | DERIVED / CLOSED-NEGATIVE |
| I3 compression | Schur complement is exact bulk compression | PROVEN (standard), VERIFIED |
| I3 ratio | Λ \= exp(−Γ+iχ); A1, A2, A3, A5 automatic for Gaussian kernels | DERIVED |
| I3 discriminator | symmetric kernel ⇒ χ \= 0 exactly | DERIVED |
| I3 surrogate | pipeline executed end to end; instrument validated | VERIFIED (surrogate only) |
| I4 S14 kernel | not executable; corpus-definition insufficiency | OPEN (debt 7\) |

**Step 4 — convergence.** Cycle 1 changed 4 nodes (the first surrogate used the wrong sign in the CTP exponent and returned |Λ| \> 1, failing complete positivity — which is how the correct Feynman–Vernon normalisation, and with it the automatic A1–A3, was found). Cycle 2 changed 1 (B7 was initially a literal-true condition and was rebuilt to distinguish the three outcomes by the gate itself). Cycle 3 changed 0\. 4 → 1 → 0: **CONVERGED**. One node remains OPEN by construction and it is the same node as in E.4.

**Step 5 — scoring against the line.** v1.5 adds no new match to any corpus number and claims no new physics. Its contribution is negative-and-structural in the way this line has learned to value: it proves that the reduction achieved in v1.4 is exact rather than hopeful (M57.B.1), it closes the most inviting remaining shortcut (M57.P″), and it leaves a protocol whose well-posedness has been demonstrated rather than asserted. The papers’ own summary of itself across v1.2–v1.5 is: the question ‘which carrier?’ is closed up to an action-level vertex selector, the question ‘where can the phase come from?’ is reduced to four named candidates, and the question ‘what is the actual S14 multiplier?’ is one complex number that nobody has yet computed.

### **E.6 — the v1.6 deep exploration (the clock)**

**Step 0 — long list (6).** (L1) re-read the loaded S14 material properly rather than by grep, and correct v1.5 if it was wrong; (L2) attempt the open-slab CTP reduction from Definition 3.1; (L3) ask whether Λ\_S14 is even a well-defined function of the action; (L4) if not, find the invariant that is; (L5) check whether ZS-S21/S24 supply the pointer channel or only the gauge sector; (L6) run anti-numerology on whatever invariant emerges.

**Step 1 — issue list (4, MECE, by influence).** (I1) is the target well posed? \[L3\]; (I2) what is the clock-free content? \[L4\]; (I3) what does the corpus actually supply? \[L1, L5\]; (I4) controls \[L6\]. **Dropped:** L2 is dropped, and this time for a reason stronger than file availability: by I1 the quantity it would compute is not determined by the action, so performing the reduction would produce a number whose modulus is a free function of an unstated duration. Attempting it would have manufactured exactly the fitted agreement that gate F-M57.2 exists to catch. The order I1-before-L2 is what saved this version from that.

**Step 2 — issue tree.** I1 → I2 → {I3, I4}. I1 is the root and its placement is the whole methodological content of this version: asking whether the target is well posed BEFORE attempting to compute it. Every prior version in this line ordered these the other way round.

Table E.6. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 well-posedness | M57.T.1 — |γ| sweeps (0,1) with τ; Λ is not a function of the action | DERIVED, λ-free |
| I1 clock search | τ\_Z: 0 occurrences in six loaded files; debt 6, owed by ZS-Q19 | VERIFIED (exhaustive) |
| I2 invariant | M57.T.2 — R \= arg λ/(−log|λ|), cycle- and clock-independent | DERIVED |
| I2 typing | M57.T.3 — λ \= exp(−μ(1−iR)); residual \= one REAL number | DERIVED |
| I2 structure | M57.T.4 — R \= (π/2 \+ arg z\*)/(−log((π/2)|z\*|)); no A, no Q | DERIVED (identity) |
| I3 corpus audit | S\_S14 present (Def. 3.1); S21 transfer matrix present; S24 slab present; v1.5 wording withdrawn | CORRECTION OF RECORD |
| I3 stopping point | S21 propagates weights but does not select (three ratios); pointer identification absent | OPEN |
| I4 anti-numerology | 96,741-member family, 0 hits on R; outcome predicted by T4 | control |

**Step 4 — convergence.** Cycle 1 changed 5 nodes (re-reading the S14 material overturned the v1.5 diagnosis, which in turn forced the well-posedness question to the root of the tree). Cycle 2 changed 1 (the invariant was initially written as χ/Γ for a single collision, where it is NOT clock-free; it became clock-free only when stated for the corpus’s own per-cycle power law). Cycle 3 changed 0\. 5 → 1 → 0: **CONVERGED**.

**Step 5 — scoring against the line.** This version answers a request for a number by proving that the number is not defined, and then supplying the quantity that is. That is the most useful thing available: a computed Λ\_S14 would have been worthless (its modulus tunable by an unstated τ), whereas R is a genuine clock-free target and a genuine falsifier — gate F-M57.T3 is the sharpest this line has ever had, because a mismatch in R cannot be rescued by adjusting the clock. The contribution is again negative-and-structural, and it also carries a correction against the previous version’s own diagnosis, which is the healthier direction for a review cycle to run. Across v1.2–v1.6 the honest summary is: the carrier is constructed and its frame fixed, the phase sources are enumerated to four, the residual is one real dimensionless number, and the clock that the whole bridge presupposes has never been defined.

### **E.7 — the v1.7 deep exploration (event clock and dilation)**

**Step 0 — long list (7).** (L1) projective GKSL generator ray \[Γ : Ω\]; (L2) Davies/KMS spectral route computing dissipator and Lamb shift together; (L3) primitive-EVENT clock in place of a metric duration; (L4) Sz.-Nagy–Foiaș characteristic-function comparison against the ZS-Q18/ZS-M46 Hardy model; (L5) Lambert–Dyson bootstrap L \= log(i)e^L; (L6) ZS-S24 one-step transfer selection T\_a; (L7) chiral / η-invariant phase.

**Step 1 — issue list (4, MECE, by influence).** (I1) the correct clock-free object, including the logarithmic lift \[L1\]; (I2) an action-derived primitive contraction \[L6 absorbed\]; (I3) event-clock equality to the M46 unit translation \[L3, L4\]; (I4) the phase source \[L7 as a sub-node\]. **Dropped:** L2 is ABSORBED into L1 and then partly REFUTED — computing the dissipator and Lamb shift from one kernel is the concrete implementation of the generator ray, but check V5 shows the strict-QND Lamb shift is central, so the ratio cannot be obtained that way. L5 as a stand-alone route is DROPPED and downgraded (declaration V6): without an independent derivation it restates the target fixed-point equation. L6 is ABSORBED into L3, since the one-step parameter question IS the primitive-event question. L7 survives only as a phase sub-node, because it fixes neither the attenuation nor the event clock.

**Step 2 — issue tree.** I1 → {I2, I3} → I4. I1 is root because the previous exploration mis-identified it: it took a single ratio for the invariant and missed the branch family, and that error propagated into a theorem. I3 is placed alongside I2 rather than after it, because the characteristic-function gate can be STATED before any contraction is constructed.

Table E.7. Step 3 — traversal, with epistemic status per node.

| Node | Result | Status |
| ----- | ----- | ----- |
| I1 invariant | M57.T.2′ — projective ray \[Γ : Ω\_k\]; the channel selects no branch | DERIVED-CONDITIONAL on a lift; branch OPEN |
| I1 retraction | the v1.6 cycle-independence check was algebraically vacuous | RETRACTED |
| I2 primitive step | one-step map depends only on gτ; event clock ≠ metric clock | DERIVED |
| I2 construction | C\_S14 from S14/S21/S24 — not attempted; orbit-weight selection and pointer embedding still absent | OPEN |
| I3 defect gate | defect indices (1,1) for the target; the pre-multiplier structural test | DERIVED |
| I3 characteristic function | Θ degree-1 Blaschke, inner, complete invariant; Θ(0) \= −λ | IMPORTED-PROVEN \+ VERIFIED |
| I3 corpus link | ZS-Q18 Θ\_λ and ZS-M46 unit translation; CRT-4 / H-CLK | OBSERVATION; equality HYPOTHESIS-strong / OPEN |
| I4 Lamb shift | strict-QND Lamb shift is central — global, not relative | CLOSED-NEGATIVE |
| I4 Lambert–Dyson | identity PROVEN; mechanism unjustified | BOOTSTRAP-HYPOTHESIS |

**Step 4 — convergence, with a reopening recorded.** The v1.6 exploration declared convergence at 6 → 2 → 0, but its root premise — that a single R is the complete clock-free invariant — was false, so that convergence is REOPENED and recorded as such rather than quietly superseded. The corrected traversal: cycle 1 changed 4 nodes (single R replaced by the branch family; T1 narrowed); cycle 2 changed 2 (the Lamb-shift route closed; the exploration refocused on the event clock); cycle 3 changed 0\. 4 → 2 → 0: **CONVERGED**. Exactly two physical nodes remain OPEN: an action-derived C\_S14 or Θ\_S14, and the exact CRT-4 / H-CLK intertwiner.

**Step 5 — scoring against the line.** This version’s value is that it retracts a theorem of the immediately preceding version and replaces the resulting gap with a better-posed gate. The characteristic-function route is stronger than anything this line has proposed before for one specific reason: it compares a whole analytic function whose ‘degree-1 scalar inner’ property most contractions fail, so it is overdetermined rather than a one-point fit — and it needs no metric duration, which was the obstruction v1.6 identified. It also has the merit of reusing two existing corpus residuals (ZS-Q18’s Blaschke factor, ZS-M46’s unit translation) rather than adding machinery. Against that: nothing is executed, the two OPEN nodes are the same two the S-line has never closed, and one route this line invented for itself was refuted in the course of the work. Across v1.2–v1.7 the honest summary is unchanged in shape and sharper in content: the carrier is built and framed, the phase sources are four and none is derived, the residual is one dilation-theoretic equality, and the metric clock remains undefined — but is no longer a prerequisite.

## **References**

\[1\] K. Kang, ZS-F0 v1.0(Revised), Ontological Bootstrap: Unitarity, the Wilson Loop Z(W), the Seam Involution J (Thm 8.5–8.7), the Z-Internal Involution J\_Z (Def. 8.11, Thm 8.12), the Dihedral D₄ Register Symmetry (Thm 8.13), and Conjecture 8.14 (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F2 v1.0, The Geometric Impedance A \= 35/437 (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-F5 v1.0, Register Dimensions and the Z₂ Seam Symmetry ε ↔ −ε (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M1 v1.0, i-Tetration, the Attracting Fixed Point z\*, and the Multiplier λ \= (iπ/2)z\* (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M6 v1.0, The Block-Laplacian Register: Sector Eigenvalues, the Bare Z-Block L\_Z \= diag(0, 1), and the Register-Total Normalization κ² \= A/Q (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-M54 v2.2 FINAL, The Mediator-Graph Transduction Theorem: the (11a)/(11b) Layer Split, the Uniqueness Theorem M54.12, the Selector No-Go M54.13, and the Canonical Dilation M54.16 (Z-Spin Cosmology, 2026). 117/117.  
\[7\] K. Kang, ZS-M56 v1.8 FINAL, The Graded Multiplicity Obstruction (Z-Spin Cosmology, 2026). 101/101 PASS \+ 20 declarations.  
\[8\] K. Kang, ZS-M57 SEED REPORT v1.1, The Odd Carrier: the D₄ Multiplicity Obstruction, the Stochastic Realisation, and the Two Graded Candidates That Remain (Z-Spin Cosmology, July 2026). 39/39 PASS. Merges Seed Report A v1.0 and Seed Report B v1.0.  
\[9\] K. Kang, ZS-S1 v1.0, Spectral Derivation of the Standard-Model Couplings; §5.2, the Z₂ Decomposition of the Z-Sector (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-S14 v2.0, Master Action Total Closure (Z-Spin Cosmology, 2026). 78/78 PASS.  
\[11\] K. Kang, ZS-A3, The Z-Bias Potential V(ε) and the Z-Anchor ε(r\_H) \= 0 (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, ZS-A16 v1.3, The Great Attractor as a Z-Spin Velocity-Watershed Defect; Theorem F, the Spin–Metric Independence No-Go (Z-Spin Cosmology, 2026).  
\[13\] K. Kang, ZS-Q18 v1.7, The Dephasing Representative and the Born Rule from i-Tetration (Z-Spin Cosmology, 2026). 95/95 PASS.  
\[14\] J.-P. Serre, Linear Representations of Finite Groups, Graduate Texts in Mathematics 42 (Springer, New York, 1977), §2.3 and §7.2. \[Frobenius reciprocity; Schur's lemma; isotypic projectors.\]  
\[15\] A. H. Clifford, Representations induced in an invariant subgroup, Ann. Math. 38, 533 (1937).  
\[16\] A. O. Gelfond, Sur le septième problème de Hilbert, Izv. Akad. Nauk SSSR 7, 623 (1934); Th. Schneider, Transzendenzuntersuchungen periodischer Funktionen, J. Reine Angew. Math. 172, 65 (1934).  
\[17\] G. Koenigs, Recherches sur les intégrales de certaines équations fonctionnelles, Ann. Sci. École Norm. Sup. (3) 1, 3 (1884).  
\[17a\] F. Lindemann, Über die Zahl π, Math. Ann. 20, 213 (1882); K. Weierstrass, Zu Lindemann’s Abhandlung “Über die Ludolph’sche Zahl”, Sitzungsber. Preuss. Akad. Wiss. 1885, 1067\. \[cos of a nonzero algebraic number is transcendental.\]  
\[17b\] I. Niven, Irrational Numbers, Carus Mathematical Monographs 11 (MAA, Washington DC, 1956), §3.3. \[The only rational multiples of π with rational cosine are those with cos ∈ {0, ±½, ±1}.\]  
\[18\] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information, 10th anniversary ed. (Cambridge University Press, Cambridge, 2010), ch. 8\. \[Stinespring dilation; mixed-unitary channels; Choi rank.\]  
\[19\] W. F. Stinespring, Positive functions on C\*-algebras, Proc. Am. Math. Soc. 6, 211 (1955).  
\[20\] W. H. Zurek, Decoherence, einselection, and the quantum origins of the classical, Rev. Mod. Phys. 75, 715 (2003).  
\[21\] H. Ollivier, D. Poulin, and W. H. Zurek, Objective properties from subjective quantum states: environment as a witness, Phys. Rev. Lett. 93, 220401 (2004).  
\[22\] Planck Collaboration, N. Aghanim et al., Planck 2018 results. VI. Cosmological parameters, Astron. Astrophys. 641, A6 (2020). \[Cited only to record that nothing here touches it; see §16.\]  
\[23\] S. Świerczkowski, On a free group of rotations of the Euclidean space, Indag. Math. 20, 376 (1958). \[The arccos(1/3) free pair; the anchor of Lemma M57.F.L.\]  
\[22a\] R. P. Feynman and F. L. Vernon, The theory of a general quantum system interacting with a linear dissipative system, Ann. Phys. (N.Y.) 24, 118 (1963). \[The influence-functional route to a reduced channel; the method Table 12.2 step 2 calls for.\]  
\[22a0\] B. Sz.-Nagy and C. Foiaș, Harmonic Analysis of Operators on Hilbert Space (North-Holland, Amsterdam, 1970), Ch. VI. \[The characteristic function as a complete unitary invariant of a completely non-unitary contraction; the gate of §15.3.\]  
\[22a2\] E. B. Davies, Markovian master equations, Commun. Math. Phys. 39, 91 (1974). \[Weak-coupling generator and the zero-Bohr-frequency Lamb-shift sector; the source of the refutation in §15.4.\]  
\[22a1\] E. B. Davies and J. T. Lewis, An operational approach to quantum probability, Commun. Math. Phys. 17, 239 (1970). \[Instruments; the frame that Table 12.1's gate presupposes.\]  
\[22b\] J. Schwinger, Unitary operator bases, Proc. Natl. Acad. Sci. USA 46, 570 (1960). \[Clock–shift (Weyl) pairs generate the full operator algebra in finite dimension; the external basis for Theorem M57.K.1.\]  
\[22c\] M.-D. Choi, Completely positive linear maps on complex matrices, Linear Algebra Appl. 10, 285 (1975); A. Jamiołkowski, Linear transformations which preserve trace and positive semidefiniteness of operators, Rep. Math. Phys. 3, 275 (1972). \[Choi–Jamiołkowski correspondence; the structural gate of Table 12.1.\]  
\[23a\] J. de Groot, Orthogonal isomorphic representations of free groups, Canad. J. Math. 8, 256 (1956). \[PRIOR ART for Theorem M57.F.1: two rotations through equal angles about perpendicular axes generate a free group of rank 2 when tan²(θ/2) is transcendental — a condition equivalent to ours (check C7).\]  
\[23b\] J. de Groot and T. Dekker, Free subgroups of the orthogonal group, Compositio Math. 12, 134 (1954). \[Earlier free-subgroup constructions in SO(3).\]  
\[24\] S. Wagon, The Banach–Tarski Paradox (Cambridge University Press, Cambridge, 1985); 2nd ed. with G. Tomkowicz (2016). \[Free rotation pairs, the paradox chain, Tarski's theorem; Thms 2.1, 3.9, 9.1.\]  
\[25\] F. Hausdorff, Bemerkung über den Inhalt von Punktmengen, Math. Ann. 75, 428 (1914). \[The first paradoxical decomposition on the sphere.\]  
\[26\] S. Banach and A. Tarski, Sur la décomposition des ensembles de points en parties respectivement congruentes, Fund. Math. 6, 244 (1924). \[The sphere and ball paradoxes.\]  
\[27\] S. Banach, Sur le problème de la mesure, Fund. Math. 4, 7 (1923). \[Finitely-additive isometry-invariant total measures exist in dimensions 1 and 2 — the lower rungs of the ladder.\]  
\[28\] A. Tarski, Algebraische Fassung des Maßproblems, Fund. Math. 31, 47 (1938). \[Tarski's alternative: paradoxical ⇔ no invariant finitely-additive probability on all subsets.\]  
\[29\] J. von Neumann, Zur allgemeinen Theorie des Maßes, Fund. Math. 13, 73 (1929). \[Amenability; the group-theoretic root of the obstruction.\]  
\[30\] H. Kesten, Symmetric random walks on groups, Trans. Am. Math. Soc. 92, 336 (1959). \[Spectral radius √(2k−1)/k for free rank k; amenability criterion ρ \= 1 — the witness of check F7.\]  
\[31\] R. M. Robinson, On the decomposition of spheres, Fund. Math. 34, 246 (1947). \[Minimal piece counts 4 and 5; cited to NON-CLAIM them as Z-constants.\]

## **Version History**

Full detail for every item below is in Appendix C (correction log) and in the section cited. This history records what changed and why; it does not restate the corrections.

v1.8 (July 2026, audit and compaction): Audits the v1.7 closing claim and finds it overcounted. Block Y: the remaining prerequisites are FOUR, not two — pointer embedding, orbit-weight selection, the branch normalisation of the Abel step, and the CRT-4/H-CLK intertwiner — and the intertwiner is ENTANGLED with the branch node rather than independent of it, because normalising the Koenigs step log λ to a unit Abel translation is itself a branch choice (Y3). The v1.7 gate also omitted the COMPLETELY NON-UNITARY hypothesis, without which the characteristic function is not a complete invariant; it is added as stage 1b (Y2). What survives: Θ does fix the multiplier’s phase, since its zero is coincidence-invariant (Y1), and the per-event gate needs no metric duration — though it does need a normalisation, so ‘free of every scale choice’ is denied (Y5). Also COMPACTED: the Abstract from five pages to two paragraphs of narrative, and this history from seven pages to the present form; no theorem, correction, gate, ledger row or reference is removed, only duplication of material that remains in place in Appendix C and the body. Verification 92/92 → 96/96 PASS \+ 12 declarations; script zs\_m57\_verify\_v1\_8.py.

v1.7 (July 2026, the event clock): RETRACTED Theorem M57.T.2 in favour of M57.T.2′ — a channel fixes Arg λ only mod 2π, so the clock-free datum is a projective ray \[Γ : Ω\_k\], one per branch, with the channel selecting none. The v1.6 ‘cycle-independence’ check was algebraically vacuous and its ledger line overstated the tested range; Theorem M57.T.1 was narrowed to the collision family; Corollary M57.T.3 corrected (the action must supply the RATE Γ, since μ \= Γτ) and reclassified to the comparison layer; check T2’s PASS condition was separated from an assertion it did not verify. NEW: the EVENT clock separated from the METRIC clock, the defect-index gate, and the Sz.-Nagy–Foiaș characteristic function as an overdetermined successor gate reusing ZS-Q18’s Blaschke factor and ZS-M46’s unit translation under the existing CRT-4/H-CLK names. TWO REFUTATIONS, one of a mechanism this line proposed for itself: the single-kernel Lamb-shift route (CLOSED-NEGATIVE) and the Lambert–Dyson bootstrap (downgraded to BOOTSTRAP-HYPOTHESIS), though λ \= −W₀(−log i) is PROVEN. 92/92 PASS \+ 11 declarations.

v1.6 (July 2026, the clock): WITHDREW the v1.5 claim that the loaded Standard-Model file lacks a usable action — ZS-S14 Definition 3.1 is complete, and ZS-S21 and ZS-S24 supply a transfer matrix and a reflection-positive slab. Theorem M57.T.1: a QND multiplier is the interaction integrated over the slab, so the modulus sweeps all of (0, 1\) with the duration and Λ\_S14 is not determined by the action; τ\_Z occurs nowhere in the loaded corpus. Offered the clock-free ratio R and its Lambert closed form in place of the complex number, and revised the terminal gate accordingly. 86/86 PASS \+ 9 declarations.

v1.5 (July 2026, the protocol): Firewall re-audit (K6, K10, B7 moved; K9 rewritten as a λ-free general theorem); θ\_S14 renamed θ\_split as a premise insertion; C4’s two conflicting sign conventions unified; C5’s anti-numerology family made signed; ledger statements F1, F9, C3 rewritten because they were printing retracted claims as PASS; M57.K.2 scoped; the ‘file-availability’ wording softened to corpus-definition insufficiency. NEW: Theorem M57.B.1 (the structural gate is passed by every α in the punctured disc, so the one-number residual is exact), Corollary M57.P″ (no mixture over collision words is complex — the free-group route to the phase is closed), and the boundary Weyl–influence-ratio protocol with exact Schur compression, executed on a surrogate that validates the instrument only. 81/81 PASS \+ 7 declarations.

v1.4 (July 2026, the Fourier–Weyl frame): CORRECTED a sign error in the carrier solution (s\* is negative; the v1.3 suite had masked it via a library’s ascending eigenvalue order) and the unqualified ‘no third case’ claim — a third case exists and is ZS-M54’s own Φ\_λ \= U\_χ ∘ D\_r. NEW: Theorem M57.K.1, the Fourier–Weyl carrier frame built from S, P\_E and J\_Z with eleven exact relations, fixing the U(1) gauge M57.F.0 left free; Theorem M57.K.3, the phase–attenuation realisation with an intact grading; the structural gate; and the one-number restatement of the residual. 75/75 PASS \+ 5 declarations.

v1.3 (July 2026, the carrier): Integrated four corrections — ‘entire F₂ mean-invisible’ retracted (composed words ARE mean-distinguishable), ‘cannot live in any finite register’ corrected (F₂ embeds in SO(3); only the finite GROUP D₄ is excluded), ‘zero choices’ corrected to canonical up to a U(1) gauge, and paradoxicality downgraded from a carrier constraint to a record-theoretic corollary; de Groot (1956) added as prior art. NEW: Theorem M57.P′ (every word has a real multiplier), Theorem M57.C.1 (an admissible carrier CONSTRUCTED, reproducing Φ\_λ exactly — the specification is satisfiable), and Theorem M57.C.2 (the construction transports λ rather than deriving it). 66/66 PASS \+ 4 declarations.

v1.2 (July 2026, the reversal): Read the v1.1 amplitude theorem in reverse as the hypothesis of a classical free-rotation theorem. NEW: the Free Collision Theorem (the two admissible graded collisions generate a rank-2 free group at the corpus angle), the paradoxicality of the carrier sphere, the record obstruction, and the amenability-ladder identification of the face layer, with an exact integer certificate and a Kesten witness. Strictly additive over v1.1. 58/58 PASS \+ 3 declarations.

v1.1 (July 2026, review-integrated): RETRACTED Theorem M57.G, whose proof used the false step ‘θ algebraic ⇒ cos θ algebraic’, and replaced it with M57.G′ (the AMPLITUDE |λ| \= cos θ\_D is not an algebraic function of A and Q, closing the seed’s κ² \= A/Q route while leaving the angle route OPEN), plus Lemma M57.G.0 reducing the transcendence import to η\_topo and Corollary M57.G.1. Fixed an impossible D₄ decomposition reprinted in the Abstract. 47/47 PASS \+ 2 declarations.

v1.0 (July 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to ZS-M57 SEED REPORT v1.1, July 2026, which merged Seed Report A v1.0 and Seed Report B v1.0 without deletion.)