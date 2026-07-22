**ZS-S25**  
**The Projected Cubic Jacobi Tensor and the Isotypic Single-Exchange Kernel on the Z-Spin Carrier**

An Equivariant Selection Theorem for the so(3) Cubic Kinematic Algebra, with Quartic Rigidity and the Two Intertwiner Gates that Separate It from a Double Copy

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Date:** July 2026  
**Theme / Paper code:** Standard Model — **ZS-S25 v2.1**  
**Role of this paper:** G0 audit and dimensional redirection, plus three equivariant rigidity theorems. It is **not** a completed gauge–gravity double copy.  
**Corpus inputs not used in the principal theorems:** the geometric impedance **A** \= 35/437 and the register **Q** \= 11 are LOCKED corpus constants and appear in Table 2.1 for completeness. **Neither enters Theorems S25.1–S25.9 or Propositions S25.3a and S25.6.** They are recorded here so that no reader mistakes them for inputs to the results.  
**Parents:** ZS-S14 (master action); ZS-S17 v2.2 (two-T₁ active space); ZS-S18 v1.6 (factorised cubic vertex; quartic non-square); ZS-S21 v1.x (carrier census); ZS-S23 v1.3 (action-to-Hessian universality); ZS-S24 v1.9 (finite-carrier gap, reflection-positive slab family)  
**Companion:** zs\_s25\_verify\_v2\_1.py (1063 lines, Python 3, NumPy \+ SciPy only, no imported data files)

**Verification ledger: 78/78 executed | 78 PASS | 0 FAIL.** Resolved by kind: **34 numerical reconstruction (R) \+ 28 analytical confirmation (A) \= 62 proof-bearing**; **8 control (X) \+ 5 locked-input drift (L) \+ 3 declaration (D) \= 16 non-proof-bearing**, the X count having risen because four v1.7 checks were demoted to historical diagnostics in v1.9. The distinction is enforced in Appendix D and no aggregate is quoted without it.

**Zero free parameters.** **A** \= 35/437, **Q** \= 11, dim **Z** \= 2, λ₁ \= 1.2428416164, λ\_h \= 7.5210904061 all LOCKED, none re-fitted. Two pre-registered anti-numerology controls, both FAIL-TO-REJECT, one now by exact enumeration (p \= 1/18) rather than sampling. SHA256(companion) \= 982b19cb069007a12476d6675e1028b2239d1ee30c65a0825689faf1e86653c6.

# **§0.1 Corrections Notice — what was withdrawn, and which numbers are reproducible**

This paper has been through seven external review rounds. Three of them forced retractions, and one forced a retraction of a retraction. §0.1 states the current position once, and every later section is consistent with it.

**The central correction (v1.8, confirmed and sharpened in v1.9).** ZS-S17 forms the alternating cup product as a **cyclic average over the basepoints** of each face. ZS-S25 from v1.0 through v1.8 used a **fixed-basepoint** product instead. These are different bilinear maps. Under the cyclic product the two-T₁ active space closes **exactly**, at 3.6 × 10⁻¹³ % leakage (check C54/C63). **ZS-S17 was correct throughout; the error was ZS-S25’s.** The v1.5 claim that "nothing closes" and the v1.7 claim that the discrepancy was "one product read two ways" are both **withdrawn**.

**New in v1.9: the fixed-basepoint numbers were never reproducible constants.** The v1.6 reviewer ran the v1.8 companion and obtained 62.95 % where the paper printed 62.25 %, and similar small disagreements throughout. v1.9 traces this (check C62): fixed-basepoint leakage on the two-T₁ space ranges over **45.21 % – 71.94 %** across the six basepoint conventions, so any single quoted value depends on which vertex of each face an implementation happens to select. **Every fixed-basepoint figure quoted in v1.0–v1.8 is convention-dependent, and v1.9 replaces them all with ranges.** The cyclic-product figures are convention-independent by construction, which is exactly why ZS-S17’s number reproduces and ZS-S25’s did not.

**Also new in v1.9: Jacobi residuals are renormalised.** v1.5–v1.8 normalised them with the max-norm, which is not invariant under orthogonal changes of eigenbasis and varies by a factor of about 2.5 (check C65). v1.9 reports Frobenius-normalised residuals, which are invariant. The 6-dimensional figure becomes **0.0675**, superseding the 0.059 printed in v1.8.

**The decisive structural fact (check C64).** No unprojected space is both product-closed and a Lie algebra:

**Table 0.1.** Closure and Jacobi under the **cyclic** product. All figures convention-independent.

| candidate space | dim | image closure | strict Jacobi (Frobenius) |
| ----- | ----- | ----- | ----- |
| λ₁ \= 1.2428416164, T₁ | 3 | **fails**, 26.72 % leakage | holds after projection, 4 × 10⁻¹⁷ |
| λ\_h \= 7.5210904061, T₁ | 3 | **fails**, 12.34 % leakage | holds after projection, 1 × 10⁻¹⁶ |
| **both T₁ copies — the ZS-S17 active space** | **6** | **holds**, 3.6 × 10⁻¹³ % | **fails**, 0.0675 |

So closure and the Jacobi identity are properties of **different** objects: the 6-dimensional space is closed but not Lie, and each 3-dimensional channel is Lie only after projection, where it is not closed. Theorem S25.2 is renamed in §3 to reflect this, and the phrase "kinematic-Jacobi closure" is not used of a single space anywhere in v1.9.

**Standing withdrawals from earlier rounds, listed once.** Corollary S25.7a (selection-irrelevance) — withdrawn in v1.5, gate F-S25.10 OPEN. Theorem S25.8’s off-shell colour–kinematics title — withdrawn in v1.5, demoted to Proposition, gate F-S25.12 OPEN. Corollary S25.9a (K is the BCJ quartic) — demoted in v1.5 to Hypothesis S25.H2, gate F-S25.20. Theorem S25.11’s "gravitational closure", "Λ \= 0 forced", "114 counted degrees of freedom" and the universal 1/|G\_full| rule — all withdrawn in v1.8; the general law is G₃m \= χ/4N.

**The recurring fault, and the gate aimed at it.** Five times the running text has outrun the ledger: the v1.1 violation of F-S25.8; the v1.1 normalisation explanation of control C14; the v1.2 I\_h multiplicity statement; the v1.0 suppression of a failing closure check, which is the direct cause of four versions of misdirected theorem-building; and the v1.0–v1.8 quotation of convention-dependent numbers as if they were constants. Gate **F-S25.16** covers all five. Every one was caught by review, none by the ledger.

# **Contents**

| § | Section | Principal result | Status |
| ----- | ----- | ----- | ----- |
| 1 | Introduction | what v2.1 establishes and deliberately does not establish | — |
| 2 | Locked inputs and the dimension of the carrier | **Theorem S25.1** — the carrier is three-dimensional | PROVEN |
| 3 | §3.3 states both separately | **Theorem S25.2** (3-dim projection, Lie, not closed) and **Prop. S25.2a** (6-dim closed, not Lie); **Theorem S25.7** selection census |  |
| 4 | The kernel, the isotypes, and the two intertwiner gates | **Theorems S25.3, S25.4**; **Prop. S25.8**; **Thm S25.9**; **Prop. S25.3a**; **Hyp. S25.H0–H2** | PROVEN / HYPOTHESIS |
| 5 | The unique dimensionless monomial | **Theorem S25.5** — \[G g²\] \= M^{6−2D} | PROVEN |
| 6 | Branch selection; cone geometry; F-S25.19 resolved | **Prop. S25.6**; **Thm S25.11a** cone geometry, **Prop. S25.11b** conditional mass reading; **§6.5** product mismatch resolved | DERIVED-COND. / **PROVEN** / **RESOLVED** |
| 7 | Zero free parameters and anti-numerology | two controls, both fail to reject | CONTROL |
| 8 | Cross-paper dependency and collision audit | no upstream result perturbed | AUDIT |
| 9 | Confrontation with observation | consistency by non-interference | — |
| 10 | Falsification gates | F-S25.1 – F-S25.22 | — |
| 11 | Non-claims | NC-S25.1 – NC-S25.17 | — |
| 12 | Conclusion | — | — |
| 13 | Record of revision | v1.0 → … → v2.1, one row per version | — |

# **§0. Abstract**

**The audit.** ZS-S17 to ZS-S24 built the chain geometry → gauge action → physical operator → strictly positive spectral gap on the finite Z-Spin carrier K\_TI × a\_tℤ. The natural successor programme proposed to convert that Yang–Mills operator into a gravitational one by colour–kinematics duality and the double copy, and pre-registered seven closure gates including the requirement that the linearised physical space contain exactly two transverse-traceless graviton degrees of freedom. This paper audits that programme before executing it, and finds three of its seven gates mis-specified. It is a **G0 audit and redirection paper**: it constructs no gravitational action and derives no unconditional gravitational coupling, obtaining only the conditional dimensionless product G₃m \= 1/120 of §6.4.

**Theorem S25.1 (the carrier is three-dimensional).** K\_TI is the 2-skeleton of a convex polyhedron and carries no 3-cells, so K\_TI × a\_tℤ is a three-dimensional cell complex and the ZS-S24 SU(3) transfer operator is a (2+1)-dimensional lattice gauge theory. In D \= 3 a gauge field carries D − 2 \= 1 physical polarisation per colour and a massless Einstein graviton carries D(D − 3)/2 \= 0 local degrees of freedom. The two-graviton gate is therefore not merely open but unsatisfiable on this carrier. This is a redirection, not a no-go. **\[PROVEN\]**

**Theorem S25.2 (Projected Cubic Jacobi Tensor).** Let R ≅ T₁ or T₂ be an irreducible admissible isotype of the carrier, dim R \= 3, and let B\_cyc be the cyclic basepoint-averaged cochain vertex. Define the **projected** self-channel tensor T\_R \= Alt(P\_R B\_cyc|\_{Λ²R}). Since Λ³(ℝ³) is one-dimensional, T\_R \= c\_R ε, whose structure constants are those of so(3); the Jacobi identity therefore holds identically and off-shell **for T\_R**. The companion rebuilds the carrier from exact coordinates and recovers **c₁ \= 0.3515993958** to ten digits at all six basepoints, independently of ZS-S18, with Frobenius Jacobi residual below 2 × 10⁻¹⁶ on both T₁ channels (checks C36, C57, C64). **\[PROVEN — for the projected tensor only.\]**

**Proposition S25.2a (Six-Dimensional Image Closure).** Under the same cyclic product the six-dimensional space W₆ \= T₁(λ₁) ⊕ T₁(λ\_h) is **product-closed**, B\_cyc(W₆, W₆) ⊆ W₆ to 3.6 × 10⁻¹³ % leakage — this is the closure ZS-S17 reports. **But the induced six-dimensional bracket is not a Lie algebra:** its Frobenius Jacobi residual is **0.067484**, not zero (checks C54, C63, C64). **\[Image closure PROVEN; Lie structure on W₆ REFUTED.\]**

**The two statements concern different objects, and v2.1 keeps them apart.** Theorem S25.2 is about the three-dimensional **projection**, which is Lie but whose raw channel is not closed — the low and high T₁ channels leak 26.72 % and 12.34 % respectively. Proposition S25.2a is about the six-dimensional **raw image**, which is closed but not Lie. **No unprojected space has been shown to be both.** Earlier versions of this paper wrote "the cubic kinematic Lie algebra of the two-T₁ active space", which silently merged the two; that phrasing is withdrawn, and the theorem is renamed accordingly.

**What neither statement establishes.** Neither is full off-shell colour–kinematics duality of the ZS-S14 action, which additionally requires kinetic/propagator compatibility, a BRST-complete treatment including ghosts, and a Jacobi-compatible quartic — the last of which ZS-S18 §4.4 reports is **not** the square of the cup curvature. Nor is it established that the exact {κ\_p}-weighted ZS-S14 Hessian selects either W₆ or any T₁ isotype. **\[DERIVED-CONDITIONAL for identification with the action-selected physical sector, gate F-S25.10; full off-shell CK duality OPEN, gate F-S25.12.\]**

**Theorem S25.3 and Proposition S25.3a (the single-exchange kernel).** Substituting the colour tensor by a second kinematic tensor gives the symmetric algebraic kernel K \= c₁²(δ\_ab δ\_cd − δ\_ad δ\_bc) on T₁ ⊗ T₁, with spectrum exactly **\+2c₁² on A (dim 1), \+c₁² on T₁ (dim 3), −c₁² on H (dim 5\)** and vanishing trace. Proposition S25.3a strengthens this: for **every** internal contraction metric η, tr K^η \= 0, so K^η is indefinite unless identically zero; and the map η ↦ K^η is injective, since contracting back with two Levi-Civita tensors gives ε\_{acp} ε\_{bdq} K^η\_{(ab),(cd)} \= 4c₁² η\_{pq}. Hence K^η is indefinite for every admissible η; numerically the inertia never has fewer than four negative directions over all eight sign patterns and 40 000 random η. The "wrong pairing" resolution is therefore closed analytically. **This does not establish a ghost.** K is an algebraic single-exchange kernel, not a gravitational Hessian, not a gauge-fixed kinetic operator, not a Hamiltonian, and not a propagator residue. The correct statement is: **K is indefinite as an algebraic single-exchange kernel; ghost status is UNDECIDED.** **\[PROVEN for the algebra; ghost status UNDECIDED, gate F-S25.6\]**

**Theorem S25.4 (A₅ isotypic tensor decomposition) and the two intertwiner gates.** Under I ≅ A₅, T₁ ⊗ T₁ \= A ⊕ T₁ ⊕ H \= 1 ⊕ 3 ⊕ 5, with Sym²(T₁) \= A ⊕ H and Λ²(T₁) \= T₁, the three summands carrying **ambient SO(3) tensor type** trace-scalar, antisymmetric/pseudovector and symmetric-traceless respectively. That is the whole of what is PROVEN. **Two distinct bridges, not one, separate it from a double-copy field dictionary**, and v1.2 registers both. **Hypothesis S25.H0 (kinematic-index intertwiner):** there exists 𝒥 : T₁^carrier → V\_kin compatible with the kinetic pairing, the gauge transformation and the BRST differential, under which — and only under which — the reading A ↔ φ, T₁ ↔ B\_{μν}, H ↔ h\_{μν} is licensed. The indices are of different provenance: T₁ labels internal truncated-icosahedron modes, whereas the μ, ν of A\_μ ⊗ A\_ν are spacetime or kinematic vector indices. **Hypothesis S25.H1 (Z-bias/dilaton intertwiner):** one step further, φ\_DC \= 𝓘(Φ) identifies the composite scalar with the corpus field Φ of ZS-F1. **\[Theorem S25.4 PROVEN; S25.H0 HYPOTHESIS-weak, gate F-S25.15; S25.H1 DERIVED-CONDITIONAL on S25.H0 plus an explicit field map, gate F-S25.13\]**

**Theorem S25.5 (the unique dimensionless monomial).** \[G\_D\] \= M^{2−D} and \[g²\] \= M^{4−D}, so \[G\_D g²\] \= M^{6−2D}, which vanishes if and only if D \= 3\. **The four-dimensional no-go against deriving G\_N stands unaltered.** What becomes admissible at D \= 3 is only the relative combination: G₃g² is the unique algebraically independent dimensionless **monomial in G₃ and g² alone**. Adjoining the lattice spacings a and a\_t, a Chern–Simons level, or any mass generates further dimensionless ratios, and no uniqueness is claimed for those. No value is computed. **\[PROVEN as stated\]**

**Proposition S25.6 (minimal Chern–Simons branch selection).** Within the minimal two-derivative Einstein/dilaton branch and its parity-odd Chern–Simons deformation, a propagating single-helicity graviton occurs in the Chern–Simons branch and not in the parity-even one. **No universal "if and only if" is asserted**: New Massive Gravity is parity-even, curvature-squared, and propagates a unitary massive spin-2 at linear order, so a parity-odd term is not a necessary condition for a propagating three-dimensional graviton in general. The corpus's PROVEN parity-odd structure — the Regge deficit as a T-odd scalar, K\_bwd ≠ K\_fwd†, φ\_CP \= 19.06°, α \= π/10 — is a candidate Chern–Simons source. **\[DERIVED-CONDITIONAL, gate F-S25.4\]**

**Theorem S25.7 (equivariant selection) — new in v1.4, and the principal result of this version.** A non-vanishing I-equivariant totally antisymmetric cubic vertex Λ²R → R exists **if and only if** R ≅ T₁ or R ≅ T₂. Both are three-dimensional with dim Hom\_I(Λ²R, R) \= 1, so the vertex is forced to be c ε with so(3) structure constants; and dim Hom\_I(Sym²R, R) \= 0 on both. On any single irreducible admissible isotype the projected antisymmetric self-map is therefore unique up to scale. Confirmed against the real face Laplacian, which supplies **four** admissible channels rather than the two the corpus records, all four carrying a projected T \= cε exactly, with the two T₂ structure constants \+0.0071641984 and \+0.0015865494 computed here for the first time. **The v1.4 corollary that this makes the selection of the active space irrelevant is WITHDRAWN in v1.5**: the carrier contains each admissible isotype twice, equivariance does not constrain the multiplicity-space product enough to force Jacobi, and — decisively — **no unprojected candidate space is simultaneously product-closed and a strict Lie algebra** (§0.1). **\[PROVEN as an irreducible self-channel census; gate F-S25.10 OPEN\]**

**Theorem S25.8 (off-shell colour–kinematics on the active space) — new in v1.4.** In the Batalin–Vilkovisky formulation, manifest off-shell colour–kinematics duality follows from a factorisation 𝒜 ⊗ 𝔤 with 𝒜 a differential graded **commutative** algebra \[8, 25\]. The cellular cochain algebra of K\_TI is associative but **not** graded-commutative: the obstruction a ∪ b \+ b ∪ a has basepoint-independent norm up to 0.2682844991 and, for a \= b, a non-trivial class in H²(K\_TI; ℝ) with ⟨\[K\_TI\], a∪a \+ a∪a⟩ \= −0.6092155, so it is not even exact. **But its projection onto any irreducible admissible isotype vanishes identically**, by Hom\_I(Sym²R, R) \= 0\. **The v1.4 promotion of this to off-shell colour–kinematics duality on the active space is WITHDRAWN**: vanishing of one projected symmetric channel is one component of one of nine requirements, and the closure requirement holds only partially — the six-dimensional space closes under the cyclic product but its bracket is not Lie. The result is retained, demoted to **Proposition S25.8**, as the single negative structural fact it is. **\[PROVEN as stated; F-S25.12 OPEN\]**

**Theorem S25.9 (quartic rigidity) and the resolution of the ghost gate — new in v1.4.** dim Hom\_I(T₁^⊗4, A) \= 3 \= dim Hom\_{SO(3)}(3^⊗4, 1): the icosahedral group admits no quartic invariant on the active space beyond the three SO(3) δδ pairings, so every quartic contact term is a point in one known three-dimensional space, and the ZS-S18 §4.4 mismatch is a **position in that space rather than an obstruction of unknown type**. K \= c₁²(δδ − δδ) lies in that space with coordinates (+1, 0, −1)·c₁², which is PROVEN. **The v1.4 identification of K as the BCJ quartic is demoted in v1.5 to Hypothesis S25.H2**, since membership of an invariant tensor in an invariant space does not establish a dynamical role, and the accompanying claim that the quartic gate reduces to two ratios is withdrawn until the three coordinates of the ZS-S18 Wilson quartic are computed. The ghost reading of K remains withdrawn, but on the weaker and secure ground that **K is an algebraic kernel and not a kinetic operator**, which was already true from §4.1 and needs no quartic identification. **\[Theorem PROVEN; S25.H2 OPEN, gate F-S25.20; F-S25.6 re-specified\]**

**What this paper does not do.** It does not integrate the exact ZS-S14 slab action, does not compute {κ\_p}, does not close F-S24.18, does not construct a gravitational action or constraint algebra, does not establish a ghost-free physical Hilbert space, does not compute G₃g², and claims no four-dimensional observational consequence. It constructs no gravitational action and derives no unconditional gravitational coupling; it obtains only the conditional dimensionless product G₃m \= 1/120, with G₃ and m not separately determined. Two pre-registered anti-numerology controls on Q \= dim **Z** \+ (dim **X**)² both fail to reject (p \= 0.400; p \= 1/18 exactly); the identity is shown to be structurally forced by dim **X** \= 3 and therefore carries no evidential weight.

# **Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** / **PROVEN at level L** | Exact theorem, verified to machine precision where numerical. "At level L" means proved only for the structure named by L; outside L nothing is asserted. |
| **DERIVED** / **DERIVED-CONDITIONAL** | Follows from PROVEN inputs with no new fitted parameter; \-CONDITIONAL names the remaining unsupplied input. |
| **HYPOTHESIS-strong / \-weak** | Conjecture; \-strong has passed a pre-registered anti-numerology control, \-weak has not. |
| **OPEN** / **UNDECIDED** | OPEN: a well-posed question this paper does not answer. UNDECIDED: a question on which the computation performed is genuinely uninformative. |
| **CLOSED-NEGATIVE** | Settled, and the route as posed fails. |
| **WITHDRAWN / DEMOTED / RETRACTED** | Previously claimed here; removed or lowered in status with the reason stated. v1.5 withdrew three v1.4 promotions. |
| **NON-CLAIM** / **OBSERVATION** / **DECLARATION** | Respectively: outside scope, recorded to prevent overclaim; a reproducible pattern with no derivation chain; an axiom-level choice, never counted as proof. |
| **Ledger kinds** | **R** numerical reconstruction (could have failed) · **A** analytical confirmation · **X** control · **L** locked-input drift · **D** declaration. **Only R and A carry proof weight.** |

# **§1. Introduction**

## **§1.1 What ZS-S17 to ZS-S24 delivered, and the question they did not ask**

The Standard-Model line of the Z-Spin corpus reached a well-defined terminus at ZS-S24 v1.9. On the finite carrier K\_TI × a\_tℤ with G \= SU(3), the operator H\_g \= g²L \+ g^{−2}V has compact resolvent, a positivity-improving heat semigroup, a unique strictly positive and hence gauge-invariant ground state, and a strictly positive physical gap for every g \> 0 (Theorem S24.2). Reflection positivity is not imported but constructed: the symmetric slab family T\_a \= e^{−aV/2} e^{−aL} e^{−aV/2} \= S\*S realises hypothesis (R2⁺) from the corpus's own kinetic operator and potential, and converges to L \+ V by symmetric Trotter (Theorem S24.14). One identification remains, gate F-S24.18: whether integrating the exact ZS-S14 slab action returns a member of that canonical family.

The natural next step, and the one an internal exploration memo recommended, is to ask whether this Yang–Mills operator is the single copy of a gravitational operator. That is the right question. The memo then pre-registered seven closure gates, of which three — the requirement of exactly two transverse-traceless graviton modes, the previously specified 3+1-dimensional Friedmann reduction, and the recovery of a Newtonian 1/r potential — silently assumed a four-dimensional carrier. (A 2+1-dimensional Hamiltonian/Friedmann constraint is itself perfectly well-posed; see §2.3.)

It is not. The one question ZS-S17 to ZS-S24 never asked of themselves is how many dimensions their own carrier has. ZS-S21 answered it in passing — check T052 records that dim K\_TI \= 2 and that the product complex therefore admits exactly two classes of 2-cell and no third — but the consequence was never carried into the gravitational programme. ZS-S24 is already consistent with the finding, since it declares the Clay 3+1D Yang–Mills mass gap a **NON-CLAIM** under gate F-S24.1. The corpus knew its carrier was not four-dimensional; it had not yet drawn the gravitational conclusion.

## **§1.2 What v2.1 establishes, and what it deliberately does not**

This paper is deliberately narrow, and each revision has narrowed it further at places where the interpretation ran ahead of the computation. It establishes six statements, three of which are theorems of elementary but load-bearing content, one of which is an independent numerical reproduction of a corpus value to ten digits, one of which is a new closure result obtained during revision, and two of which are reported against interest.

First, the carrier is three-dimensional, and the memo's degree-of-freedom gate is unsatisfiable as posed (§2). Second, the **projected** three-dimensional cubic tensor is forced to be c\_Rε and satisfies the so(3) Jacobi identity off-shell, while the six-dimensional two-T₁ image separately closes without being a Lie algebra (Thm S25.2 and Prop. S25.2a) — not full colour–kinematics duality (§3). Third, the single-exchange kernel has spectrum exactly (+2, \+1, −1)·c₁², vanishing trace, and — new in v1.1 — vanishing trace for **every** internal contraction metric, so its indefiniteness cannot be removed by re-choosing the pairing; the ghost question nevertheless remains undecided because K is not a kinetic operator (§4). Fourth, the isotypic content of T₁ ⊗ T₁ is the scalar–antisymmetric–symmetric triple **as internal A₅ isotypes**, and reading it as double-copy fields requires an intertwiner 𝒥 from the internal mode index to a spacetime index that no corpus paper supplies (§4.5–§4.7). Fifth, the four-dimensional no-go stands and only the relative monomial G₃g² becomes dimensionally admissible at D \= 3 (§5). Sixth, within the minimal two-derivative branch the appearance of a propagating gravitational mode is a parity choice, with no universal converse (§6).

**The honest summary of the paper's standing.** What is closed is: the three-dimensional carrier census, the projected three-dimensional Jacobi tensor together with the distinct six-dimensional image-closure result, and the isotypic spectrum of the algebraic single-exchange kernel. What is open is: the exact ZS-S14 slab integration, full off-shell CK/BV completion, the gravitational action and its constraints, a ghost-free physical Hilbert space, G₃g², and any four-dimensional emergence. This is a G0 audit paper. Its value lies in redefining the research problem as (2+1)-dimensional before further work is spent on a four-dimensional target that the carrier cannot support.

## **§1.3 Relation to the external literature**

Colour–kinematics duality and the double copy \[1–3\] are established at tree level and conjectural at loop level; the obstruction to an off-shell Lagrangian formulation is a BV\_∞^□ structure governed by the wave operator \[5\], and genuine off-shell constructions implement the duality across the whole Batalin–Vilkovisky complex including ghosts and antifields \[6–9\], with the quartic sector completed separately \[14\]. §4.8 lists which of those nine ingredients the Z-Spin carrier supplies (one) and shows that product closure is partial and insufficient: it holds on the six-dimensional space, while strict Jacobi does not.

On the gravity side, three-dimensional Einstein gravity is a Chern–Simons theory with no local degrees of freedom \[10\]; topologically massive gravity carries one massive graviton \[11\]; New Massive Gravity is parity-even and also carries one \[24\], which is why §6 is a Proposition with a restricted domain rather than a Theorem with a converse. The double copy of topologically massive Yang–Mills is topologically massive gravity to five points \[12, 13\]. **Most directly relevant to §6.4**, a point mass in 2+1 dimensions produces a conical deficit and no field \[26, 27\] — the result Theorem S25.11 applies to the carrier.

**What would be new externally.** A reflection-positive finite cellular Yang–Mills carrier whose projected cubic vertex is rigidly so(3) by an equivariance census, together with a measured separation between image closure and the Jacobi identity — the six-dimensional active space closes but is not Lie, each three-dimensional channel is Lie only after projection — and a conditional zero-fit-parameter cone-surface / point-particle correspondence on the same carrier. **\[NON-CLAIM NC-S25.1: no exhaustive novelty search has been performed.\]**

# **§2. Locked Inputs and the Dimension of the Carrier**

## **§2.1 Locked inputs**

**Table 2.1.** Locked inputs. Every entry is imported; none is re-derived or re-fitted in this paper.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| Geometric impedance **A** | 35/437 \= 0.0800915332 | ZS-F2 | LOCKED |
| Register **Q** | 11 \= 2 \+ 3 \+ 6 | ZS-F5 | LOCKED |
| dim(**Z**), dim(**X**), dim(**Y**) | 2, 3, 6 | ZS-F5 | LOCKED |
| K\_TI census (V, E, F) | (60, 90, 32), χ \= 2 | ZS-S21 T010–T020 | PROVEN |
| Spectral gap λ₁ | 1.2428416164 (3-fold, T₁) | ZS-S7 / ZS-S21 | LOCKED |
| Second T₁ eigenvalue λ\_h | 7.5210904061 (3-fold) | ZS-S17 / ZS-S18 | LOCKED |
| Alternating-vertex closure | dim Hom\_I(T₁⊗T₁, T₁) \= 1; c\_{rst} ε-proportional | ZS-S17 v2.2 §1 | PROVEN |
| Factorised cubic vertex | H₃ \= (μg/2) Σ f^{abc} q q q T\_{rαβ}, T totally antisymmetric | ZS-S18 v1.6 Thm S18.9 | PROVEN |
| Quartic is **not** the cubic square | ratio spans −0.083 to \+0.389, sign change included | ZS-S18 v1.6 §4.4 | PROVEN |
| Parity dictionary | A → 0⁺⁺, H → 2⁺⁺ | ZS-S18 v1.6 Thm S18.8 | PROVEN |
| Finite-carrier gap | Δ\_phys ∈ (0, ∞) for all g \> 0, all a \> 0 | ZS-S24 v1.9 Thm S24.9/S24.14 | PROVEN |
| Regge T-odd scalar phase | K\_bwd ≠ K\_fwd†, ‖·‖ \= 0.4032; φ\_CP \= 19.06° | ZS-S6 §4 | PROVEN |
| Frame mismatch angle | α \= δ\_X − δ\_Y \= π/6 − π/15 \= π/10 | ZS-S6 §G.2 | PROVEN |

No quantity is introduced in this paper that is not either an element of Table 2.1, a consequence of it, or standard mathematics. The parameter audit is §7.1. Note that the ninth row is new to v1.1: the non-squareness of the quartic was cited in v1.0 only in passing, and is promoted here to a locked input because Theorem S25.2's restricted status depends on it.

## **§2.2 Theorem S25.1 — the carrier is three-dimensional**

**Theorem S25.1.** K\_TI is the 2-skeleton of a convex polyhedron with (V, E, F) \= (60, 90, 32\) and χ \= 2\. It contains no 3-cells. Hence K\_TI × a\_tℤ is a three-dimensional cell complex, and the ZS-S24 gauge theory on it is a (2+1)-dimensional lattice gauge theory.

**Proof.** The companion rebuilds K\_TI from the exact vertex coordinates — the even permutations of (0, ±1, ±3φ), (±1, ±(2+φ), ±2φ) and (±φ, ±2, ±(2φ+1)) with φ the golden ratio — with no imported data file. It finds 60 vertices, 90 edges at the common minimal separation, and 32 faces obtained by merging coplanar convex-hull simplices, split as 12 pentagons and 20 hexagons; χ \= 60 − 90 \+ 32 \= 2 (checks C1–C4, kind R). A 2-skeleton has no cells of dimension 3, so the top cell of K\_TI × a\_tℤ is a temporal prism of dimension 3 (check C5, kind D). This is the fact ZS-S21 records at check T052.

**\[STATUS: PROVEN — C1–C4 (R), C5 (D). This restates an existing corpus check; the novelty is not the fact but its use.\]**

## **§2.3 Corollary S25.1a — the degree-of-freedom census**

In D spacetime dimensions a massless gauge field carries D − 2 physical polarisations per colour and a massless Einstein graviton carries D(D − 3)/2 local degrees of freedom. At D \= 3 these are 1 and 0; at D \= 4 they are 2 and 2\.

**Table 2.2.** Degree-of-freedom census (checks C22, C23, kind A). The D \= 4 row is the value the exploration memo assumed; the D \= 3 row is what the carrier supplies.

| D | gauge, per colour | massless Einstein graviton | topologically massive graviton |
| ----- | ----- | ----- | ----- |
| **3** | **1** | **0** | **1** |
| 4 | 2 | 2 | — |
| 5 | 3 | 5 | — |

**Corollary S25.1a.** The pre-registered gate requiring exactly two transverse-traceless graviton degrees of freedom in the linearised physical space of the double copy is **unsatisfiable** on the Z-Spin carrier, for the same reason that it is unsatisfiable for any three-dimensional theory.

**A correction to the v1.2 statement of the other two gates.** v1.2 wrote that "the gates asking for a Friedmann constraint and a Newtonian 1/r potential are not well-posed", as though the Friedmann constraint were itself a four-dimensional notion. **It is not, and the phrasing is withdrawn.** Friedmann–Robertson–Walker cosmology and its Hamiltonian constraint are defined in any spacetime dimension, and a (2+1)-dimensional Hamiltonian/Friedmann constraint is perfectly well-posed. The correct statement is:

The previously proposed 3+1-dimensional Friedmann gate and Newtonian 1/r gate are mis-specified on this carrier. A genuinely 2+1-dimensional Hamiltonian/Friedmann constraint remains well-posed, while the Newtonian potential must be replaced by its two-spatial-dimensional analogue.

In two spatial dimensions the Poisson equation gives a logarithmic rather than an inverse-power potential, and in pure (2+1)-dimensional Einstein gravity the exterior of a source is locally flat with a conical deficit rather than carrying any Newtonian field at all. Which of these is the right target depends on the branch selected in §6, and this paper does not choose. The practical effect of the correction is to sharpen rather than to remove the successor gates: ZS-S26 should ask for a **2+1-dimensional** Hamiltonian constraint and the **two-dimensional** potential analogue, not abandon either.

**\[STATUS: CLOSED-NEGATIVE for the gate as posed; PROVEN for the counting. This is a redirection, not a no-go for the double copy — §4 and §6 supply the correct targets.\]**

**A firewall that must not be dropped.** Two distinct counts appear throughout and must never be conflated. The first is the count of spacetime degrees of freedom, which is 1 at D \= 3\. The second is the count of internal polyhedral polarisation labels, which is 3 for T₁ and 9 for T₁ ⊗ T₁. They multiply; they do not compete. Gate **F-S25.8** fires on any downstream Z-Spin paper that reads the 9 of §4 as a spacetime degree-of-freedom count.

# **§3. Theorem S25.2 — The Projected Cubic Jacobi Tensor**

**A note on the change of name.** In v1.0 this section was headed "Cellular Colour–Kinematics Duality". That title claimed more than the argument delivers, and it is withdrawn. What follows is proved at the level of the cubic vertex restricted to the active space; the additional structures that a full off-shell colour–kinematics duality of the ZS-S14 action would require are enumerated in §3.5 and registered as gate F-S25.12. **\[DEMOTED in v1.1.\]**

## **§3.1 The two ingredients, both already PROVEN upstream**

**Ingredient one (ZS-S17 v2.2, PROVEN).** The Yang–Mills-relevant alternating cochain vertex maps T₁(λ₁) ⊕ T₁(λ\_h) into itself with zero leakage over all four input pairs; with the copies aligned by the icosahedral intertwiner under the signed face action, all eight coefficient blocks c\_{rst} are exactly ε-proportional, confirming dim Hom\_I(T₁ ⊗ T₁, T₁) \= 1\. The closure is a property of the alternating vertex specifically: the full non-antisymmetrised bilinear leaks.

**Ingredient two (ZS-S18 v1.6 Theorem S18.9, PROVEN).** Since f^{abc} is totally antisymmetric, total symmetry of the combined multi-index forces the mode tensor to be totally antisymmetric, and the physical cubic Hamiltonian is

H₃ \= (μg/2) Σ f^{abc} q^a\_r q^b\_α q^c\_β T\_{rαβ},   T totally antisymmetric (residual exactly 0),

with no family-dependent factors and retained magnitude c₁ \= 0.3515993958, relative leakage 1.4 × 10⁻¹⁵ at every one of the six basepoints. Neither paper drew the double-copy consequence.

## **§3.2 The dimension argument**

**Lemma S25.2a.** Let W be a three-dimensional real inner-product space and T ∈ W\* ⊗ W\* ⊗ W\* totally antisymmetric. Then dim Λ³(W) \= C(3,3) \= 1, so in any orthonormal basis T \= c ε for a single scalar c. **\[PROVEN\]**

**Lemma S25.2b.** The structure constants ε\_{abc} satisfy ε\_{abe}ε\_{ecd} \+ ε\_{bce}ε\_{ead} \+ ε\_{cae}ε\_{ebd} \= 0, being the structure constants of so(3) ≅ su(2). Verified to exactly zero (check C15, kind A). **\[PROVEN\]**

## **§3.3 Statement and proof — two separate results**

Earlier versions stated a single theorem "on the two-T₁ active space" and then used dim W \= 3 in its proof, silently merging a six-dimensional space with a three-dimensional projection. v2.1 states the two results separately, each with its own proof and its own status.

**Theorem S25.2 (Projected Cubic Jacobi Tensor).** Let R ≅ T₁ or T₂ be a three-dimensional irreducible isotype of the carrier, let B\_cyc be the cyclic basepoint-averaged cochain vertex, let P\_R be the orthogonal projector onto R, and define the projected self-channel tensor

**T\_R \= Alt( P\_R B\_cyc |\_{Λ²R} ).**

Then T\_R \= c\_R ε, and consequently the Jacobi identity **n\_s \+ n\_t \+ n\_u \= 0** holds identically and off-shell **for T\_R**.

**Proof.** ZS-S18 Theorem S18.9 gives the factorisation of the physical cubic vertex into a totally antisymmetric colour tensor times a totally antisymmetric mode tensor, so only the totally antisymmetrised part of the vertex survives; that part is T\_R by definition. Since dim R \= 3 and Λ³(ℝ³) is one-dimensional, Lemma S25.2a forces T\_R \= c\_R ε. Lemma S25.2b gives the Jacobi identity for ε, hence for T\_R up to the overall factor c\_R², hence for numerators built by contracting T\_R with external polarisations. The companion reconstructs c₁ \= 0.3515993958 to ten digits at all six basepoints and finds Frobenius Jacobi residual below 2 × 10⁻¹⁶ on both T₁ channels (checks C36, C57, C64).

**Scope, stated explicitly.** This is a statement about the **projected** tensor. It does **not** assert that R is closed under B\_cyc; in fact neither T₁ channel is — the low channel leaks 26.72 % and the high channel 12.34 % of the product out of itself (check C64). **\[PROVEN for T\_R only.\]**

**Proposition S25.2a (Six-Dimensional Image Closure).** Let W₆ \= T₁(λ₁) ⊕ T₁(λ\_h) be the two-T₁ active space of ZS-S17. Under the cyclic product,

**B\_cyc(W₆, W₆) ⊆ W₆ ,   leakage 3.60 × 10⁻¹³ % ,   but   J(B\_cyc|\_{W₆}) ≠ 0 ,   ‖J‖\_F / ‖B‖²\_F \= 0.067484 .**

**Proof.** Direct computation in the companion (checks C54, C63, C64): the residual ‖(1 − P\_{W₆}) B\_cyc(W₆, W₆)‖ / ‖B\_cyc(W₆, W₆)‖ is at machine zero, so the image closes; the Frobenius-normalised Jacobiator of the induced six-dimensional bracket is 0.067484, which is not zero and is basis-invariant.

**W₆ is therefore product-closed but is not a Lie algebra.** This is the closure ZS-S17 reports, and it is genuine; what it is not is a Lie structure. **\[Image closure PROVEN; Lie structure on W₆ REFUTED.\]**

**The two results together.** Theorem S25.2 concerns a three-dimensional projection that is Lie but not closed; Proposition S25.2a concerns a six-dimensional raw image that is closed but not Lie. **No unprojected space has been shown to be both.** Any statement of the form "the cubic kinematic Lie algebra of the active space" merges them and is not used in this paper.

**\[STATUS: Theorem S25.2 PROVEN for the projected tensor — from ZS-S18 Thm S18.9 PROVEN via Lemmas S25.2a–b PROVEN; verification C11–C16, C36, C57, C64. Proposition S25.2a PROVEN for image closure, REFUTED for Lie structure; verification C54, C63, C64.\]**

## **§3.4 Independent numerical confirmation**

The companion does not import c₁. It rebuilds K\_TI from coordinates, forms the unweighted face Laplacian Δ₂ \= B₂ᵀB₂, extracts the two three-fold eigenspaces at the LOCKED values λ₁ and λ\_h, builds the gap edge potentials a \= B₂u/λ, evaluates the alternating cup product face by face, totally antisymmetrises, and contracts with ε. It obtains

**c₁ \= 0.3515993958,   c₁² \= 0.1236221352,**

agreeing with ZS-S18 Theorem S18.9 to all ten quoted digits (check C11, kind R), with T \= c₁ ε at relative residual exactly 0 (C13) and kinematic Jacobi residual exactly 0 (C16). The spectrum of Δ₂ is in Appendix A.

## **§3.5 The precise gap between Theorem S25.2 and off-shell colour–kinematics duality**

This subsection is new in v1.1 and is the most important correction it carries. Theorem S25.2 is a statement about one tensor on one subspace. A claim of off-shell colour–kinematics duality for the ZS-S14 action would require, in addition, all four of the following.

**Table 3.1.** Ingredients of a full off-shell colour–kinematics duality, and their status on the Z-Spin carrier.

| Ingredient | Required for off-shell CK | Status on the Z-Spin carrier |
| ----- | ----- | ----- |
| **Cubic factorisation with Jacobi** | yes | **supplied** — Theorem S25.2, PROVEN at cubic active-space level |
| **Kinetic pairing / propagator compatibility** | yes — numerators must be compatible with the inverse of the quadratic form | **not supplied** — no compatibility statement between c₁ε and the ZS-S24 quadratic operator has been proved |
| **Gauge fixing and a BRST/BV complex including ghosts** | yes — off-shell CK is a statement about the full complex \[6–9\] | **not supplied** — no BRST complex for the carrier exists in the corpus |
| **Jacobi-compatible quartic / contact completion** | yes \[14\] | **not supplied** — ZS-S18 §4.4 proves the Wilson quartic is not the square of the cup curvature. §4.9 shows the quartic invariant space is three-dimensional, which locates the question but does not answer it; Hypothesis S25.H2 and gate F-S25.20 |

The fourth row is the sharpest. The corpus has already computed the quantity that would have to cooperate, and it does not cooperate in the naive way. Any future claim of full off-shell CK duality on this carrier must confront ZS-S18 §4.4 directly rather than around it.

**\[STATUS: full off-shell colour–kinematics duality of the ZS-S14 action is OPEN, gate F-S25.12. NON-CLAIM NC-S25.10.\]**

## **§3.6 What is nontrivial and what is forced — reported against interest**

It would be an overclaim to present the Jacobi identity as a discovery. Once the surviving mode tensor is known to be totally antisymmetric on a three-dimensional space, Lemma S25.2a makes T ∝ ε and the Jacobi identity is automatic. The whole of the nontrivial content sits in the two upstream facts: that the alternating vertex **closes** on the two-T₁ space at all, and that the physical vertex is the totally antisymmetrised one. The first is a computed property of the truncated icosahedron and could have failed; the second follows from the total antisymmetry of f^{abc} and could not.

The honest statement of Theorem S25.2 is therefore: **the projected cubic Jacobi identity on the Z-Spin carrier is a corollary of the three-dimensionality of the declared active space, not an independent dynamical property of the action.**

**Status of the {κ\_p} question, told once.** v1.1 claimed Theorem S25.2 is independent of {κ\_p}; v1.2 withdrew that as unproven; v1.4 claimed to prove it via Corollary S25.7a; **v1.5 withdrew that too; v1.8 and v1.9 then corrected v1.5 itself.** The correct position, from §0.1: under the cyclic product of ZS-S17 the six-dimensional two-T₁ space **does** close (3.6 × 10⁻¹³ %), but its bracket fails Jacobi (0.0675); each three-dimensional channel satisfies Jacobi only after projection, where it is not closed (26.72 %, 12.34 %). The current position is:

Once a three-dimensional **closed** active space W and a totally antisymmetric T ∈ Λ³W\* are supplied, the implication T \= cε ⇒ Jacobi is coefficient-independent. Whether the exact {κ\_p}-weighted Hessian selects a space that is simultaneously closed and Lie is unproven, and Table 0.1 shows the unweighted operator supplies no such space. **PROVEN** for the projected tensor T\_R; the existence of an unprojected three-dimensional space that is simultaneously closed and Lie is **not established**. **DERIVED-CONDITIONAL** for any identification with a physical, action-selected sector. **Gate F-S25.10 is OPEN.**

**\[CORRECTION-IN-ADVANCE, S25-C1: any downstream paper quoting Theorem S25.2 as evidence for the ZS-S14 action specifically is quoting it wrongly. It is evidence about the active space.\]**

## **§3.7 Controls and further items reported against interest**

**Control C14 (kind X).** The non-antisymmetrised bilinear built from the same potentials leaks entirely out of the six-mode space, confirming that closure is a property of the alternating vertex and not of general bilinears. **v1.1 attributed the difference from ZS-S17's 29.5 % to normalisation. That explanation is wrong and is withdrawn:** a leakage fraction is a ratio, invariant under a ↦ sa and b ↦ tb, so no choice of overall normalisation can move it. The correct statement is that **the two controls use different non-alternating bilinear definitions, not merely different normalisations**, and the two figures are therefore not numerically comparable. Only the qualitative content — that closure is not automatic — transfers.

**Reported against interest, C11b.** At the normalisation of this paper the λ\_h channel gives c\_h² \= 0.0025500303, matching **neither** the ZS-S17 raw cup projection 0.0095045494 **nor** the ZS-S18 polarised value 0.0012658090. The three numbers refer to three different objects and the map between them is a convention that has not been written down anywhere in the corpus. Registered as gate **F-S25.7**. The one thing the discrepancy does establish is that the independent value lies below the ZS-S17 raw projection, confirming the **direction** of the ZS-S18 v1.5 correction that a projection is not a coupling (C11c). Nothing in Theorems S25.1–S25.5 or Proposition S25.6 depends on c\_h.

**Reported against interest, C7b, and upgraded in v1.2 by C7c.** The unweighted face Laplacian has 9 distinct eigenvalues, not 10, with multiplicities (1, 3, 5, 3, 4, 5, 3, 5, 3\) summing to 32, so statements of the form "each eigenvalue carries one irrep" are false as written. v1.1 asserted, on upstream authority, that two I\_h isotypes merge; it did not compute which. **v1.2 computes them.** The companion now reconstructs the 60 proper rotations of the icosahedral group directly from the vertex set, induces the signed action on the 32 oriented faces, and decomposes every eigenspace by character orthogonality, with the parity label supplied by the orientation-reversing inversion. The results are Tables A.1 and A.2. λ₁ and λ\_h are **both** T₁ and both parity-even, confirming the corpus assignment independently, and the single accidental degeneracy at 8.0000000000 is precisely **A\_u ⊕ G\_u**. **v1.3 additionally computes the complete I\_h content by character orthogonality over all 120 group elements**, obtaining 2A\_u ⊕ 2T₁\_g ⊕ 2T₂\_g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u — six distinct I\_h types, not ten. The statement in v1.2 that the ten I\_h irreducibles each appear once is withdrawn; see Appendix A, where the correction, its independent cross-check against the unsigned representation, and the reason the v1.2 ledger failed to catch it are all recorded.

# **§3.8 Theorem S25.7 — The Irreducible Self-Channel Selection Theorem**

v1.1 claimed that Theorem S25.2 is independent of {κ\_p}; v1.2 withdrew that claim as unproven and restored gate F-S25.10 to OPEN. Both were right about the argument then available. v1.4 supplies the argument that was missing, and the conclusion is stronger than the one v1.1 asserted without proof.

The question F-S25.10 poses is: which three-dimensional active space does the exact {κ\_p}-weighted Hessian select, and does the vertex close on it? The answer given here does not compute {κ\_p}. It shows that **the question does not need to be answered**, because every admissible answer gives the same conclusion.

**Theorem S25.7 (Irreducible Self-Channel Selection).** Let R be an irreducible real representation of the icosahedral group I ≅ A₅. Then a non-vanishing I-equivariant totally antisymmetric cubic vertex Λ²R → R exists **if and only if** R ≅ T₁ or R ≅ T₂. In both admissible cases:

(i) dim R \= 3;  (ii) dim Hom\_I(Λ²R, R) \= 1, so the vertex is forced to be T \= c ε and the kinematic Jacobi identity holds;  (iii) dim Hom\_I(Sym²R, R) \= 0, so the symmetric part of the vertex vanishes identically in the output channel.

**Table 3.2.** The full equivariant vertex census for I (checks C31–C33, kind A). Only the two three-dimensional irreducibles admit a cubic vertex at all, and on both the symmetric channel is empty.

| R | dim | Λ²R | dim Hom\_I(Λ²R, R) | Sym²R | dim Hom\_I(Sym²R, R) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| A | 1 | 0 | **0** | A | 1 |
| **T₁** | **3** | **T₁** | **1** | A ⊕ H | **0** |
| **T₂** | **3** | **T₂** | **1** | A ⊕ H | **0** |
| G | 4 | T₁ ⊕ T₂ | **0** | A ⊕ G ⊕ H | 1 |
| H | 5 | T₁ ⊕ T₂ ⊕ G | **0** | A ⊕ G ⊕ 2H | 2 |

**Proof.** Character orthogonality on the five classes of I, evaluated in the companion. For R \= A the exterior square vanishes. For R \= G and R \= H the exterior square contains no copy of R itself, so every equivariant antisymmetric vertex on those isotypes is identically zero. For R \= T₁ and R \= T₂ the exterior square is R with multiplicity one, so the vertex space is one-dimensional and Lemma S25.2a applies verbatim. Clause (iii) is the statement that Sym²(T₁) \= Sym²(T₂) \= A ⊕ H contains no three-dimensional summand.

**Corollary S25.7a of v1.4 is WITHDRAWN.** v1.4 concluded from Theorem S25.7 that whatever active space an I-equivariant operator selects, the conclusion of Theorem S25.2 follows, so the selection question posed by F-S25.10 need not be answered. **That inference does not hold, for two independent reasons, both identified in review of v1.4 and both confirmed numerically in v1.5.**

**Reason one: the carrier contains each admissible isotype twice.** The face representation contains 2T₁ and 2T₂ (Table A.2). An I-equivariant operator may act by an arbitrary matrix on the two-dimensional multiplicity space of an isotype, so the space it selects need not be a single isolated copy. For W \= T₁ ⊗ M with dim M \= 2, the general equivariant antisymmetric bracket is \[x ⊗ a, y ⊗ b\] \= (x × y) ⊗ μ(a, b) with μ a **symmetric** bilinear map on M. Equivariance constrains the form of μ and nothing else; the full Jacobi identity imposes further conditions on μ that equivariance does not supply. **I-equivariance does not imply an active-space Jacobi identity.**

**Reason two: no space is both closed and Lie.** Checks C34 and C40 measure the **self-projection** of the vertex, never whether (1 − P\_W) B(W, W) vanishes. Table 0.1 measures it under the correct (cyclic) product: the six-dimensional two-T₁ space closes, but its bracket is not Lie; the three-dimensional channels are Lie after projection but leak 26.72 % and 12.34 %. The hypothesis of Theorem S25.2 — a **closed three-dimensional** active space — is met by no eigenspace of this operator.

**Direct confirmation (checks C42, C64).** Under the fixed-basepoint product the raw bracket satisfies Jacobi on no channel. Under the cyclic product the six-dimensional bracket has Frobenius Jacobi residual 0.0675 — small but not zero — while the projected three-dimensional brackets are exact to 10⁻¹⁷. The Lie structure lives in the projection, not in any raw subspace.

**Gate F-S25.10 is restored to OPEN.** New gate F-S25.17, introduced in v1.4 to carry the residual of a closure that has now evaporated, is retained but demoted to a sub-question of F-S25.10 rather than its replacement.

**What Theorem S25.7 does and does not give.** It is a complete census of the **irreducible self-channels**: it says which isotypes can carry a non-vanishing equivariant antisymmetric cubic self-map at all, and that where one exists it is unique up to scale and equals c ε. That is a genuine rigidity statement about the **projected** vertex. It says nothing about closure, nothing about multiplicity spaces, and nothing about whether the projected object is the physical one. The physical layer of Theorem S25.2 remains **DERIVED-CONDITIONAL on F-S23.6**, exactly as v1.2 and v1.3 had it.

**\[STATUS: Theorem S25.7 PROVEN as an irreducible self-channel census — C31–C33 (A), C34 and C40 (R), where C34 and C40 are read strictly as self-projection measurements. Corollary S25.7a WITHDRAWN in v1.5. Gate F-S25.10 OPEN. NON-CLAIM NC-S25.14.\]**

## **§3.9 Confirmation on the real operator, and two channels the corpus had not recorded**

Theorem S25.7 is a character computation. The companion tests it against the actual face Laplacian by evaluating the totally antisymmetrised cochain vertex on every one of the nine eigenspaces (check C34, kind R). The prediction is confirmed exactly: the vertex is non-zero on the two T₁ eigenspaces and the two T₂ eigenspaces, and vanishes to between 10⁻¹⁴ and 10⁻¹⁵ on the A, G and H eigenspaces and on the reducible A\_u ⊕ G\_u space at eigenvalue 8\.

**This exposes something the corpus had not recorded.** ZS-S17 and ZS-S18 work with a two-T₁ active space. But the carrier supplies **four** admissible channels, not two: the T₂ eigenspaces at 4.8443660283 and 8.3917019492 carry a non-vanishing antisymmetric cubic vertex on exactly the same footing. On all four the vertex is exactly c ε (check C40, kind R):

**Table 3.3.** All four admissible cubic channels of the carrier, with potentials normalised as a \= B₂u/λ. The first row is the corpus value; the other three are computed here for the first time.

| eigenvalue | isotype | structure constant c | relative residual of T − cε | status in the corpus |
| ----- | ----- | ----- | ----- | ----- |
| **1.2428416164** | **T₁** | **\+0.3515993958** | 0.0e+00 | ZS-S18 Thm S18.9 |
| 4.8443660283 | T₂ | \+0.0071641984 | 0.0e+00 | **not previously recorded** |
| 7.5210904061 | T₁ | \+0.0038869096 | 1.1e−16 | **not previously recorded at this normalisation** |
| 8.3917019492 | T₂ | \+0.0015865494 | 1.4e−16 | **not previously recorded** |

Two consequences follow, and the second is uncomfortable. First, the so(3) kinematic algebra is not a property of the corpus gap in particular: it is **the only structure an I-equivariant operator can produce at all**, on any of its channels. Second, the corpus's restriction to the two T₁ copies is a **choice**, not a derivation, and no ZS-S17/S18 argument excludes the T₂ channels. Whether the exact Hessian populates them is exactly the content of F-S25.10 as now reformulated. **\[NEW OBSERVATION; registered as gate F-S25.18.\]**

**Basepoint independence, verified (check C36, kind R).** The structure constant of the leading channel is the same to machine precision at all six basepoints of the cochain vertex, c₁ \= 0.3515993958 at every one, with T \= c₁ε at relative residual ≤ 3 × 10⁻¹⁶. This confirms the ZS-S17 basepoint claim independently and removes the last discretionary element from the leading number.

# **§4. The Single-Exchange Kernel, Its Spectrum, and What It Does Not Decide**

## **§4.1 The substitution and the object it produces**

The double copy replaces the colour factor of each cubic graph by a second kinematic numerator, c\_i n\_i → n\_i ñ\_i. On the Z-Spin active space both numerators are built from T \= c₁ ε, so the copy carries two T₁ indices and lives on the nine-dimensional space T₁ ⊗ T₁. Contracting two vertices over one internal index gives

**K\_{(ab),(cd)} \= Σ\_e T\_{ace} T\_{bde} \= c₁² ( δ\_{ab} δ\_{cd} − δ\_{ad} δ\_{bc} ),**

equivalently (K M)\_{ab} \= c₁² ( δ\_{ab} tr M − M\_{ba} ) on 3 × 3 matrices M.

**What K is, stated before any spectrum is quoted.** K is an **algebraic single-exchange kernel**: the contraction of two cubic tensors over one internal index. It is **not** a gravitational Hessian, **not** a gauge-fixed quadratic kinetic operator, **not** a physical Hilbert-space Hamiltonian, and **not** the residue of a propagator at a physical pole. Every statement in §4.2 and §4.3 is a statement about this algebraic object and nothing else. **\[Gate F-S25.14 fires on any reading of K as a kinetic operator.\]**

## **§4.2 Theorem S25.3 — the spectrum**

**Theorem S25.3.** K is symmetric, traceless, and has exactly three eigenvalues, one on each isotype of T₁ ⊗ T₁.

**Table 4.1.** Spectrum of the algebraic single-exchange kernel (checks C17a–C17d, kind A). Numerical column uses c₁² \= 0.1236221352. The field-content column is a representation-theoretic label, not an identification with any corpus field.

| isotype | dim | representation type | eigenvalue | numerical value |
| ----- | ----- | ----- | ----- | ----- |
| **A** | 1 | scalar | **\+2 c₁²** | \+0.2472442703 |
| **T₁** | 3 | antisymmetric tensor | **\+1 c₁²** | \+0.1236221352 |
| **H** | 5 | symmetric traceless tensor | **−1 c₁²** | −0.1236221352 |

**Proof.** Symmetry is immediate. On the antisymmetric subspace tr M \= 0 and Mᵀ \= −M, so KM \= \+c₁²M. On the symmetric traceless subspace tr M \= 0 and Mᵀ \= M, so KM \= −c₁²M. On the trace subspace M \= (t/3)·1, giving KM \= 2c₁²M. The trace is 2·1 \+ 1·3 \+ (−1)·5 \= 0\. Confirmed to machine zero. **\[PROVEN\]**

## **§4.3 Proposition S25.3a — the indefiniteness is metric-independent (new in v1.1)**

One resolution proposed in v1.0 §4.3 was that the Euclidean identity contraction δ\_{ef} is the wrong pairing and that a different internal contraction metric restores positivity on H. That resolution can now be closed analytically.

**Proposition S25.3a.** Let η be any symmetric bilinear form on the internal index and define K^η\_{(ab),(cd)} \= Σ\_{ef} T\_{ace} T\_{bdf} η^{ef}. Writing η \= Σ\_k λ\_k v\_k v\_kᵀ gives

K^η \= c₁² Σ\_k λ\_k A^{(k)} ⊗ A^{(k)},   A^{(k)} \= \[v\_k\]\_× ,

where each A^{(k)} is antisymmetric and therefore traceless. Hence

**tr K^η \= c₁² Σ\_k λ\_k ( tr A^{(k)} )² \= 0   for every η.**

A traceless symmetric operator is either identically zero or indefinite. It remains to show that K^η \= 0 forces η \= 0\. v1.1 asserted this without proof; the one line is supplied here. Contracting back with two Levi-Civita tensors,

**ε\_{acp} ε\_{bdq} K^η\_{(ab),(cd)} \= 4 c₁² η\_{pq},**

so the map η ↦ K^η is injective and K^η \= 0 implies η \= 0\. Hence **K^η is indefinite for every admissible internal contraction metric.** (Verified to machine zero, check C17g, kind A.)

**Numerical confirmation (check C17e, kind R; C17f, kind A).** Over all eight sign patterns η \= diag(±1, ±1, ±1) the inertia (n₋, n₀, n₊) is (5,0,4) or (4,0,5); over 40 000 random η, symmetric and positive-definite alike, the number of negative directions never falls below 4, and max |tr K^η| \= 0 to machine precision.

**\[STATUS: PROVEN. Escape route (i) of v1.0 §4.3 is CLOSED.\]**

## **§4.4 What the indefiniteness does and does not establish**

It is essential not to over-read Proposition S25.3a. The correct statement is:

**K is indefinite as an algebraic single-exchange kernel; ghost status is UNDECIDED.**

A ghost is a wrong-sign residue at a physical pole of a gauge-fixed propagator, or equivalently a negative-norm state in the physical Hilbert space. Establishing one requires a kinetic operator, a gauge fixing, and a physical state space, none of which this paper constructs. The negative eigenvalue on H is a property of a tensor contraction and carries no unitarity content by itself.

With route (i) closed, two live routes remain and this paper selects neither. (ii) K is simply not the object whose sign matters, and the gravitational kinetic operator on the carrier — once constructed — has a different sign structure; this is the reviewer's reading and it is the most likely one. (iii) The substitution is incomplete and the quartic contributes at the same order, which ZS-S18 §4.4 makes a live possibility since the Wilson quartic is not the square of the cup curvature.

A third remark, offered as context and not as a resolution: the indefiniteness of the Euclidean gravitational action in its conformal sector \[21\] is a genuine and well-understood feature of gravity, so indefiniteness appearing somewhere in a gravitational construction is not by itself an alarm.

**\[STATUS: ghost status UNDECIDED, gate F-S25.6. No positivity, ghost-freedom or unitarity is claimed or denied. NON-CLAIM NC-S25.2.\]**

## **§4.5 Theorem S25.4 — the isotypic dictionary**

**Theorem S25.4.** Under the rotational icosahedral group I ≅ A₅,

T₁ ⊗ T₁ \= A ⊕ T₁ ⊕ H \= 1 ⊕ 3 ⊕ 5,   Sym²(T₁) \= A ⊕ H \= 6,   Λ²(T₁) \= T₁ \= 3\.

**Proof.** Character orthogonality on the five classes {E, 12C₅, 12C₅², 20C₃, 15C₂} with χ\_{T₁} \= (3, φ, 1−φ, 0, −1) and the symmetrised characters (χ(g)² ± χ(g²))/2 (checks C18–C20, kind A). The rank of the image of the alternating vertex is independently found to be 3, matching dim Λ² (check C21, kind R). **\[PROVEN\]**

**What is PROVEN, stated exactly.** The three summands carry the following **ambient SO(3) tensor types**: A is of trace-scalar type, T₁ is of antisymmetric or pseudovector type, and H is of symmetric-traceless type. That is the entire content of Theorem S25.4. The type labels are statements about how each summand transforms under the ambient rotation group acting on the **internal** polyhedral index, and nothing more. ZS-S18 Theorem S18.8 independently assigns A → 0⁺⁺ and H → 2⁺⁺, and that assignment is retained unaltered.

**What is NOT proven, and what v1.1 got wrong.** v1.1 §4.5 wrote that matching against the standard double-copy content A\_μ ⊗ A\_ν \= h\_{μν} ⊕ B\_{μν} ⊕ φ "gives the representation dictionary", and then treated that dictionary as PROVEN. **It is not, and the claim is withdrawn.** The two sides carry indices of different provenance. On the left, T₁ labels internal vibrational modes of the truncated icosahedron: it is a label on the carrier’s geometry. On the right, μ and ν are spacetime or kinematic vector indices, and the off-shell double-copy literature constructs that decomposition on the Lorentz index of the gauge field within the full BRST/BV field complex \[6–9\]. Equating a three-dimensional internal isotype with a three-dimensional spacetime index space because both happen to be three-dimensional is precisely the inference this paper’s own gate **F-S25.8** was written to forbid. v1.1 violated its own firewall, and the reviewer of v1.1 caught it. The Z-Spin Book issues the same warning independently, that identifying the internal rotation-algebra 3 with the metric or spacetime dimension 3 is a category error.

**A correction to the v1.2 auxiliary argument.** v1.2 argued additionally that since D \= 3 gives one physical polarisation per colour while T₁ is three-dimensional, "they cannot be the same object". **That argument confuses two layers and is withdrawn.** The off-shell Lorentz vector space in D \= 3 is itself three-dimensional; the count of one is the \*gauge-reduced\* physical polarisation, obtained after gauge fixing, and the μ, ν of A\_μ ⊗ A\_ν are off-shell vector indices. So the dimensions do not in fact disagree at the level where 𝒥 would act.

The correct statement is weaker and is the one v1.3 adopts: the off-shell Lorentz vector space in D \= 3 is three-dimensional, while its gauge-reduced physical polarisation space is one-dimensional; the carrier mode space T₁ is also three-dimensional, but **dimension matching alone supplies no intertwiner**. A valid 𝒥 must act at the off-shell vector and BRST level and descend consistently to the one-dimensional physical quotient after gauge reduction. The numerical coincidence dim T₁ \= dim V\_Lorentz \= 3 neither establishes S25.H0 nor obstructs it; it is the reason the question is worth asking and not the reason it is settled.

## **§4.6 Hypothesis S25.H0 — the kinematic-index intertwiner (new in v1.2)**

**Hypothesis S25.H0 (Kinematic-Index Intertwiner).** There exists a map

**𝒥 : T₁^{carrier} ⟶ V\_{kin/spacetime}**

from the internal icosahedral mode space to the kinematic or spacetime index space of the copy, which is compatible with (i) the kinetic pairing, (ii) the gauge transformation, and (iii) the BRST differential. **Under S25.H0, and only under it, the isotypes of Theorem S25.4 may be read as double-copy fields:**

A ↔ φ (dilaton),   T₁ ↔ B\_{μν} (two-form),   H ↔ h\_{μν} (graviton).

**Why it is a hypothesis and not a corollary.** No such 𝒥 is exhibited in the corpus. Its existence is not implied by the isotypic decomposition, which is a statement about the internal index alone. It is constrained rather than supported by Theorem S25.1: 𝒥 must be defined on the three-dimensional off-shell vector and BRST complex and descend consistently to its one-dimensional gauge-reduced physical quotient. And it must intertwine three separate structures, any one of which could obstruct it.

**\[STATUS: HYPOTHESIS-weak. Gate F-S25.15. NON-CLAIM NC-S25.12.\]**

**The two bridges are distinct and must not be conflated.** ZS-S25 now registers two separate and consecutive intertwiner gates, and neither is supplied:

| Bridge | Map | From | To | Gate | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **First** | **𝒥** | T₁ internal carrier mode index | spacetime / kinematic index of the copy | F-S25.15 | HYPOTHESIS-weak |
| **Second** | **𝓘** | φ\_DC, the composite scalar of the copy | Φ, the Z-bias field of ZS-F1 | F-S25.13 | DERIVED-CONDITIONAL on the first |

v1.1 recognised only the second. The first is logically prior: without 𝒥 there is no "dilaton of the copy" for 𝓘 to map Φ onto, so **S25.H1 is now conditional on S25.H0** as well as on its own field map.

## **§4.7 Hypothesis S25.H1 — the Z-bias/dilaton identification**

**What v1.0 claimed.** v1.0 §4.4 carried a Corollary S25.4a asserting that the Z-bias field Φ of ZS-F1 **is** the dilaton of the double copy, on the grounds that the copy contains exactly one scalar and the Z-sector carries exactly one scalar. **That inference is invalid and the corollary is withdrawn.** Uniqueness of a scalar on each side of a correspondence does not identify the two scalars. The copy's scalar is a composite built from T₁ ⊗ T₁; Φ is an independent field appearing in the ZS-F1 action. They are objects of different provenance.

**Hypothesis S25.H1.** There exists an action-level intertwiner φ\_DC \= 𝓘(Φ) identifying the composite scalar of the double copy with the Z-bias field, under which the kinetic terms, the couplings, the parity assignment and the equations of motion of the two fields agree.

**What would be required to promote it.** An explicit map 𝓘 exhibited at the level of the action, not the spectrum; agreement of the two kinetic normalisations; agreement of the coupling of φ\_DC to the H sector with the coupling of Φ to the corpus metric sector; and consistency of the equations of motion. None of these is supplied here.

**\[STATUS: DERIVED-CONDITIONAL on Hypothesis S25.H0** and **on an explicit field map; in the absence of both, HYPOTHESIS-weak. Gate F-S25.13. NON-CLAIM NC-S25.11.\]**

**A consistency remark, unchanged in force but not upgraded.** The corpus's Horndeski analysis of the ZS-F1 action finds G₅ \= 0 structurally, hence c\_T \= c and compatibility with GW170817; G₄ \= ½M\_P²(1 \+ **A**ε²); no gravitational slip, η \= 1; and μ \= Σ \= 1/(1 \+ **A**) \= 0.9258. That is a conformal scalar–tensor theory: a graviton and a scalar, with no antisymmetric tensor — the field content of a double copy whose two-form has been dualised away or is absent, which in D \= 3 it is, since a two-form in three dimensions carries no propagating degrees of freedom. Two independent corpus routes arrive at the same **field content**. This is an OBSERVATION about counting and is explicitly **not** evidence for the identification of Hypothesis S25.H1, since matching multiplicities is exactly the inference that §4.6 has just rejected.

## **§4.8 Proposition S25.8 — Vanishing of the projected symmetric self-channel**

Gate F-S25.12 records that a full off-shell colour–kinematics duality needs, beyond the cubic Jacobi identity, a kinetic pairing, a BRST/BV complex and a compatible quartic. v1.4 supplies the structural criterion those requirements are usually phrased through, and evaluates it.

In the Batalin–Vilkovisky formulation, a gauge theory manifestly satisfies off-shell colour–kinematics duality when its field complex **factorises** as 𝒜 ⊗ 𝔤 with 𝔤 the colour Lie algebra and 𝒜 a differential graded **commutative** algebra \[8, 25\]; Chern–Simons theory, BF theory and two-dimensional Yang–Mills are the standard examples, and the BV double copy is then 𝒜 ⊗ 𝒜̃. For a cellular gauge theory the candidate 𝒜 is the cochain algebra of the carrier with the cup product. Associativity holds; graded commutativity is the question.

**Proposition S25.8.** The cellular cochain algebra of K\_TI is **not** graded-commutative. For degree-one cochains a, b the symmetric combination a ∪ b \+ b ∪ a is generically non-zero, with basepoint-independent norm; on the gap potentials its largest value is 0.2682844991, and for a \= b it carries a **non-trivial class in H²(K\_TI; ℝ) ≅ ℝ**, with ⟨\[K\_TI\], a ∪ a \+ a ∪ a⟩ \= −0.6092155, so the obstruction is not even exact. **However, its projection onto any irreducible admissible isotype R vanishes identically**, and does so because Hom\_I(Sym²R, R) \= 0 rather than by accident.

**Proof.** The non-commutativity is computed directly (check C35, kind R; C39, kind R). The vanishing on W is Hom\_I(Sym²W, W) \= 0 from Table 3.2: the symmetric square of an admissible isotype is A ⊕ H, which contains no copy of W, so by Schur's lemma every equivariant symmetric vertex with output in W is zero. The companion confirms the projection at 1.2 × 10⁻¹⁵.

**What v1.4 claimed, and why it is withdrawn.** v1.4 titled this result "off-shell colour–kinematics duality holds exactly on the active space" and reclassified gate F-S25.12 as CLOSED-POSITIVE there. **That promotion is withdrawn.** Vanishing of one projected symmetric channel is one component of one requirement. A Batalin–Vilkovisky off-shell colour–kinematics construction \[8, 25\] requires all of the following, and the Z-Spin carrier is known to supply only the first:

| Requirement | Status on the carrier |
| ----- | ----- |
| Hom\_I(Sym²R, R) \= 0 on the admissible isotypes | **supplied** — Proposition S25.8 |
| a full graded vector space A⁰ ⊕ A¹ ⊕ A² ⊕ …, not a space of degree-one modes | not supplied — the active space is a set of degree-one modes |
| closure of the space under the product | **partial** — the 6-dim two-T₁ space closes under the cyclic product (3.6 × 10⁻¹³ %), but its bracket fails Jacobi (0.0675); no 3-dim channel is closed |
| graded associativity of the projected product P\_W(P\_W(a∪b)∪c) \= P\_W(a∪P\_W(b∪c)) | not tested anywhere in the companion |
| a differential, and the derivation property for it | not supplied |
| a non-degenerate integration/pairing | not supplied |
| a gauge-fixing operator with the second-order (BV) property | not supplied |
| a BV complex including ghosts and antifields | not supplied |
| higher C∞ / BV∞ multilinear maps and generalised Jacobi identities | not supplied |

The third row is the sharpest: the six-dimensional space is a subalgebra but not a Lie algebra, and the three-dimensional channels are Lie only as projections, so no single space carries both properties at once and no graded or BV structure is being claimed on any of them. **Gate F-S25.12 is restored to OPEN in full.** What Proposition S25.8 contributes is a single negative structural fact, honestly worth having and no more: the symmetric self-channel is empty by Schur's lemma, so whatever obstruction eventually blocks off-shell CK duality on this carrier, it will not be that one.

**\[STATUS: Proposition S25.8 PROVEN as stated — C33 (A), C35 and C39 (R). The v1.4 title and the CLOSED-POSITIVE reclassification are WITHDRAWN. Gate F-S25.12 OPEN. NON-CLAIM NC-S25.15.\]**

## **§4.9 Theorem S25.9 — Quartic rigidity, and what the kernel K actually is**

The sharpest clause of F-S25.12 is the quartic: ZS-S18 §4.4 proves that the Wilson quartic is **not** the square of the cup curvature, with the ratio spanning −0.083 to \+0.389 including a sign change. v1.0 to v1.3 recorded that as an obstruction of unknown type. It is not of unknown type.

**Theorem S25.9 (Quartic Rigidity).** dim Hom\_I(T₁^⊗4, A) \= 3, and the same holds for T₂. This equals dim Hom\_{SO(3)}(3^⊗4, 1\) \= 3, the span of the three pairings δ\_{ab}δ\_{cd}, δ\_{ac}δ\_{bd}, δ\_{ad}δ\_{bc}. **The icosahedral group therefore admits no quartic invariant on an admissible active space beyond those already permitted by the full rotation group.** Every quartic contact term on the active space, whatever the weighting {κ\_p}, is a point in that same three-dimensional space.

**Proof.** Character orthogonality: ⟨χ\_{T₁}⁴, χ\_A⟩ \= (1/60)\[81 \+ 12φ⁴ \+ 12(1−φ)⁴ \+ 0 \+ 15\] \= 3, with φ⁴ \= 3φ \+ 2\. Verified in the companion (check C37, kind A).

**What check C38 actually establishes.** K \= c₁²(δ\_{ab}δ\_{cd} − δ\_{ad}δ\_{bc}) lies in the three-dimensional invariant space with coordinates (+1, 0, −1)·c₁². That is a membership statement about an invariant tensor, and it is PROVEN.

**Hypothesis S25.H2 (formerly Corollary S25.9a, demoted in v1.5).** K is the quartic contact term that BCJ compatibility requires. **This does not follow from C38**, which only checks that an invariant tensor lies in an invariant space. Establishing it would require: the three coordinates of the actual ZS-S18 Wilson quartic, which have never been computed; the propagator structure that separates cubic exchange from contact terms; the generalised gauge transformations; the quartic L∞/C∞ identity; BRST invariance; action-level locality; and the BCJ-compatible redistribution. None is supplied here, and the external quartic double-copy constructions do not identify the quartic with the square of the cubic tensor either — they build trilinear homotopy maps and generalised identities explicitly \[14\].

**Also withdrawn: the "two ratios" claim.** v1.4 wrote that the ZS-S18 quartic mismatch reduces to fixing two ratios in a known three-space. Until the three coordinates of the Wilson quartic are computed, that sentence asserts a reduction that has not been performed. **\[STATUS: HYPOTHESIS S25.H2, OPEN. Gate F-S25.20.\]**

**Corollary S25.9b (the ghost gate, resolved).** Gates F-S25.6 and F-S25.14 have carried the question of what the indefiniteness of K means since v1.0, and v1.3 left it UNDECIDED with three candidate readings, of which route (i) was closed analytically by Proposition S25.3a. the correct and sufficient statement does not require Theorem S25.9 at all. **K is an algebraic single-exchange kernel — a contraction of two cubic tensors over one internal index. It is not a kinetic operator, not a Hessian, not a Hamiltonian and not a propagator residue, and a ghost is a property of exactly those objects. No ghost can be inferred from the sign of K, whatever K turns out to be.** That was already true from the v1.3 definition in §4.1 and needs no further input.

**What v1.4 added and v1.5 removes.** v1.4 supported this conclusion by asserting that K \*is\* the Yang–Mills seagull, whose f^{abe}f^{cde} colour structure produces the same indefinite tensor. That analogy remains suggestive and is retained as motivation for Hypothesis S25.H2, but it is not established, so it cannot be load-bearing. The ghost conclusion stands on the weaker and secure ground instead.

This resolves the ghost question in the only direction the computation licenses: **there is no ghost implied by the indefiniteness of K, because K is not the object whose sign carries unitarity information.** It does not establish that the eventual gravitational operator is ghost-free — no such operator is constructed here — and F-S25.6 is therefore not closed but **re-specified**: it now asks about a kinetic operator that does not yet exist, rather than about a kernel that has been misassigned.

**\[STATUS: Theorem S25.9 (quartic invariant space is 3-dimensional) PROVEN — C37 (A). C38 confirms K lies in it — PROVEN as a membership statement. The identification of K as the BCJ quartic is** Hypothesis S25.H2, OPEN **(gate F-S25.20), not a corollary. Corollary S25.9b (no ghost follows from K, since K is not a kinetic operator) DERIVED and independent of S25.H2. Gate F-S25.6 RE-SPECIFIED.\]**

# **§5. Theorem S25.5 — The Unique Dimensionless Monomial in G₃ and g²**

The exploration memo correctly warns against attempting to derive Newton's constant from dimensionless corpus data: **A**, **Q** and z\* are dimensionless while \[G\_N\] \= M^{−2}, so no combination of them can produce G\_N without an additional dimensionful datum. The argument is sound, and **v1.1 states plainly that it remains sound.** What follows does not repair it.

**Theorem S25.5.** With S\_EH \= (1/16πG\_D) ∫ d^Dx √(−g) R and S\_YM \= −(1/4g²) ∫ d^Dx F², the mass dimensions are \[G\_D\] \= M^{2−D} and \[g²\] \= M^{4−D}, so

**\[ G\_D g² \] \= M^{6 − 2D},   which vanishes if and only if D \= 3\.**

**Proof.** \[R\] \= M², \[d^Dx\] \= M^{−D}, so \[1/G\_D\] \= M^{D−2}. \[F²\] \= M⁴, so \[1/g²\] \= M^{D−4}. Add exponents. Verified over D \= 2…7 (check C24, kind A). **\[PROVEN\]**

**Table 5.1.** Mass dimension of the product G\_D g² (check C24).

| D | 2 | \*\*3\*\* | 4 | 5 | 6 | 7 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| \[G\_D g²\] | M² | **M⁰** | M⁻² | M⁻⁴ | M⁻⁶ | M⁻⁸ |

## **§5.1 The scope of the uniqueness claim (restricted in v1.1)**

**Corollary S25.5a, as restricted.** On the three-dimensional Z-Spin carrier, **G₃g² is the unique algebraically independent dimensionless monomial constructible from G₃ and g² alone.** It is therefore dimensionally admissible to ask whether

G₃ g² \= f( **A**, **Q**, λ₁ )

with f a function of LOCKED dimensionless data and no new fitted parameter. No value is computed.

**What the restriction excludes.** v1.0 wrote "exactly one dimensionless gravitational coupling" without qualification. That is too strong. The carrier supplies the lattice spacings a and a\_t, so g²a and G₃/a are separately dimensionless; a Chern–Simons level is dimensionless by construction; and any mass scale generates further ratios. The uniqueness statement holds **only** within the two-symbol algebra generated by G₃ and g², and no uniqueness whatever is claimed once further scales are adjoined.

**And what it does not license.** The four-dimensional no-go stands: G\_N in D \= 4 remains outside reach for exactly the reason the memo gives. What becomes admissible at D \= 3 is only the **relative** combination. Any downstream attempt to promote G₃g² to G\_N without a metric-side datum is rejected on sight by gate **F-S25.5**.

**\[STATUS: Theorem S25.5 PROVEN; Corollary S25.5a PROVEN as restricted; the existence of a zero-free-parameter expression for G₃g² is OPEN and is not asserted. NON-CLAIM NC-S25.3.\]**

# **§6. Proposition S25.6 — Minimal Chern–Simons Branch Selection**

**A note on the change of status.** v1.0 stated this as a Theorem with an "if and only if": that a propagating three-dimensional graviton arises **precisely when** the action contains a parity-odd Chern–Simons term. **The converse is false in general and is withdrawn.** New Massive Gravity \[24\] is parity-even, curvature-squared, and propagates a unitary massive spin-2 at linear order. A parity-odd term is therefore sufficient within the minimal branch but not necessary in general. **\[DEMOTED in v1.1.\]**

## **§6.1 The restricted dichotomy**

In D \= 3 a gauge field carries one physical polarisation per colour, so the double-copy state count is 1 ⊗ 1 \= 1\. Massless Einstein gravity in three dimensions is topological, with no local degrees of freedom and an equivalent Chern–Simons description \[10\]. The single copied state therefore cannot be a massless Einstein graviton; parity-even and within the two-derivative branch, it is a scalar. If instead the gauge theory carries a parity-odd Chern–Simons term, it becomes topologically massive Yang–Mills with one physical mode, whose double copy is topologically massive gravity with one massive graviton \[11–13\].

**Proposition S25.6 (Minimal Chern–Simons Branch Selection).** Within the minimal two-derivative Einstein/dilaton branch and its parity-odd Chern–Simons deformation, a propagating single-helicity graviton occurs in the Chern–Simons branch and not in the parity-even branch, where the propagating content is the scalar alone and the gravitational sector is topological — constraints without dynamics.

**Domain of validity, stated explicitly.** The Proposition is a statement about that two-member family only. It says nothing about higher-derivative three-dimensional gravities, and in particular it is **not** contradicted by, and does not contradict, New Massive Gravity and its relatives, which lie outside the family and do propagate a massive spin-2 without any parity-odd term \[24\].

**\[STATUS: DERIVED-CONDITIONAL — from Theorem S25.1 (PROVEN) together with \[10–13\], within the stated domain. The universal converse is NOT claimed.\]**

## **§6.2 The corpus already owns a parity-odd structure**

Whether the Chern–Simons branch is realised is a question about the ZS-S14 Lagrangian, not about the double copy. ZS-S6 proves that the Regge deficit angle is a T-odd scalar, that the backward kernel therefore satisfies K\_bwd ≠ K\_fwd† with ‖K\_bwd − K\_fwd†‖ \= 0.4032, and that the resulting CP-violating phase is φ\_CP \= 19.06°; the frame mismatch angle α \= π/10 is derived from first principles as π/6 − π/15. ZS-M32 lifts the same structure to amplitude level and derives the operator-level phase quantum π/5. A parity-odd, orientation-sensitive phase is the structure a Chern–Simons term supplies. This is a candidate, not an identification; establishing it requires extracting a parity-odd term from ZS-S14 explicitly and matching its coefficient to a level. Gate **F-S25.4**.

**\[NON-CLAIM NC-S25.4: no graviton mass is computed, and no relation between φ\_CP and a Chern–Simons level is asserted.\]**

## **§6.3 A firewall between two Hamiltonians**

ZS-S24 proves Δ\_phys \> 0 for the gauge Hamiltonian on the carrier. Three-dimensional gravity requires the Hamiltonian to vanish on physical states as a first-class constraint. These are not in conflict, but the resolution must be stated because the objects are easy to confuse. The double copy is a map on numerators; it does **not** preserve the spectrum, and it changes the operator class from "self-adjoint Hamiltonian with a gap" to "first-class constraint". Quoting Δ\_phys \> 0 as a property of the gravitational operator would be a category error. **\[Gate F-S25.9.\]**

## **§6.4 Theorem S25.11a–c — Cone geometry and its conditional point-particle reading**

Every gravitational statement in §§4–6 has been conditional. This section adds one **unconditional** geometric fact and one **conditional** gravitational reading of it, by a route that uses **none** of the machinery the §0.1 withdrawals touched. It needs Theorem S25.1, the Gauss–Bonnet theorem, and the standard (2+1)-dimensional dictionary between conical defects and point masses \[26, 27\]. It does not need active-space closure, colour–kinematics duality, the kernel K, Hypotheses S25.H0–H2, the value of {κ\_p}, or either of **A** and **Q** (check C49).

**The observation the corpus had not used.** K\_TI is not a smooth sphere. It is a **flat** polyhedron: every face is planar, so the intrinsic geometry is Euclidean everywhere except at the 60 vertices, where the angles sum to 348° rather than 360°. All of the curvature of the spatial slice sits in 60 identical conical defects of deficit exactly π/15, and Gauss–Bonnet fixes their sum at 2πχ \= 4π (check C45, kind R; this is the corpus's own check C30, now used rather than merely recorded).

In (2+1)-dimensional gravity a point mass produces a conical deficit δ \= 8πG₃m and nothing else: there is no local field, and the exterior geometry is flat \[26, 27\]. Applying the dictionary to the carrier gives the whole gravitational content immediately.

**A note on scope, forced by the v1.6 review.** v1.6 stated a single "Theorem S25.11 — Gravitational Closure" that identified cone geometry, a static point-particle solution, Λ \= 0, the full phase space and a gravitational-bridge closure all at once. The review was right that this over-reached: the companion checks the angle deficits, the Gauss–Bonnet sum, a dictionary substitution and a moduli formula, and none of an Einstein/Regge action, lapse and shift, extrinsic curvature, the Hamiltonian and momentum constraints, particle worldlines, Lorentz holonomies or time evolution. v1.8 therefore splits the result into what is proven, what is conditional and what is an observation, and withdraws the word "closure."

**Theorem S25.11a (Equal-Deficit Cone Geometry).** The spatial slice of K\_TI is a piecewise-Euclidean cone surface carrying 60 identical conical defects of deficit δ \= π/15, with Σδ \= 4π \= 2πχ(S²). **\[PROVEN — C45.\]**

**Proposition S25.11b (Conditional Point-Particle Reading).** Under the static product ansatz K\_{ij} \= 0 and the Λ \= 0 Deser–Jackiw–'t Hooft point-particle branch, each defect corresponds to

**G₃ m \= δ/8π \= 1/2N \= 1/120 ,   Σ G₃ m \= χ/4 \= 1/2 .**

**\[DERIVED-CONDITIONAL** on the static ansatz and the Λ \= 0 branch, and on the imported dictionary \[26, 27\], gate F-S25.21.**\]**

**On Λ \= 0, corrected.** v1.6 wrote that Λ \= 0 is \*forced\* because the polyhedron is flat away from its vertices. The reviewer correctly noted that spatial flatness does not force Λ \= 0: the Hamiltonian constraint ²R \+ K² − K\_{ij}K^{ij} \= 2Λ \+ 16πG₃ρ involves the extrinsic curvature K\_{ij}, and ²R \= 0 permits Λ ≠ 0 compensated by K\_{ij}. **Λ \= 0 is a branch choice, not a consequence**, and is the branch in which the static point-particle dictionary of S25.11b holds. Status: **DERIVED-CONDITIONAL / OPEN**, not forced.

**On the 114 moduli, corrected.** The count 6g − 6 \+ 2n \= 114 (and 2 × 114 \= 228 for the phase space) is the dimension of the Teichmüller/moduli space of a 60-punctured sphere — the configuration space of the **whole** 60-particle theory in which the punctures may move. K\_TI is one highly symmetric point in that space: vertex positions, edge lengths, icosahedral symmetry and all deficits are fixed. Calling 114 "the carrier's degrees of freedom" would require showing that all 114 deformation directions preserve incidence and the deficit constraints and are physical rather than gauge — none of which is done. Status: **114 is the candidate moduli dimension of the ambient 60-particle theory; the carrier itself sits at a symmetric locus. \[OBSERVATION, not a carrier DOF count.\]**

**Table 6.1.** Cone geometry and its conditional gravitational reading (checks C45–C49). The status column is part of the table: only the first two rows are unconditional.

| quantity | value | status |
| ----- | ----- | ----- |
| deficit per vertex | π/15 \= 12.0000000000° | **PROVEN** (S25.11a) |
| total deficit | Σδ \= 4π \= 2πχ | **PROVEN** (S25.11a) |
| local graviton DOF | 0 | **PROVEN** — D(D − 3)/2 at D \= 3 |
| **G₃ m per defect** | **1/120** | **DERIVED-CONDITIONAL** (S25.11b): static K\_{ij} \= 0, Λ \= 0 branch, imported dictionary \[26, 27\] |
| total mass | Σ G₃m \= χ/4 \= 1/2 | DERIVED-CONDITIONAL, as above |
| cosmological constant | Λ \= 0 | **ASSUMED branch, not derived** — spatial flatness does not force it |
| ambient puncture moduli | 114 | **OBSERVATION** — moduli of the 60-puncture theory, not of the fixed carrier |
| carrier physical DOF | not derived | **OPEN** |
| unconditional geometric law | δ \= 2πχ/N | **PROVEN** |
| conditional mass law | G₃m \= χ/4N | **DERIVED-CONDITIONAL** on the point-particle dictionary; 1/|G\_full| only when the rotation stabiliser is trivial |

**Observation S25.11c (Symmetry Rewriting), corrected.** Conditional on the point-particle dictionary, the mass formula is **G₃m \= χ/4N**; the unconditional geometric formula is **δ \= 2πχ/N**, fixed by the polyhedron and the Euler characteristic alone. v1.6 further claimed G₃m \= 1/|full point group| for any vertex-transitive carrier; the reviewer correctly noted this is false in general. By orbit–stabiliser N \= |G\_rot|/|Stab(v)|, so G₃m \= χ|Stab(v)|/4|G\_rot|, and the clean form 1/2N \= 1/|G\_full| holds **only** when the rotation stabiliser is trivial — which is true for the truncated icosahedron (N \= 60 \= |I|) and the truncated octahedron (N \= 24 \= |O|) but fails, for example, for the cube (N \= 8 ≠ |O| \= 24). Status: **G₃m \= χ/4N is the law; G₃m \= 1/|G\_full| is a corollary for these two carriers only. \[OBSERVATION.\]**

**What is unconditional, and what is not.** Unconditional: the equal-deficit cone geometry (S25.11a), i.e. δ \= 2πχ/N. Conditional: the mass law G₃m \= χ/4N, the point-particle mass identification (S25.11b, on the static Λ \= 0 branch and the imported dictionary), the value Λ \= 0, and the reading of 114 as physical degrees of freedom. **Withdrawn: the words "gravitational sector closed", "complete zero-parameter description of gravity", and "Λ \= 0 forced."** This is a conditional cone-surface / point-particle **correspondence**, not a closure. An actual gravitational closure still requires a successor paper to construct the Regge–Einstein action, the constraints, the extrinsic curvature, the holonomies and the time evolution — exactly as NC-S25.6 says this paper does not.

**What is not closed, stated immediately.** Three things. (i) The dictionary δ \= 8πG₃m is imported, not derived here; deriving it inside the corpus is the content of gate F-S25.21. (ii) G₃m being dimensionless means **no mass and no Newton constant is separately determined** — only their product, exactly as Theorem S25.5 requires, and NC-S25.3 continues to forbid promoting anything here to G\_N. (iii) The relation between this sector and the gauge sector runs through G₃g², which remains uncomputed; since G₃m \= 1/120 is now known, computing g²/m would deliver G₃g², and that is gate F-S25.22 and the single most valuable remaining calculation in the line.

**Anti-numerology, pre-registered.** The number 1/120 is 1/|I\_h|, and |I\_h| \= 120 is also 5\!. No relation between 1/120 and **A** \= 35/437, **Q** \= 11, λ₁ or c₁ is asserted, sought, or used anywhere in this paper. The derivation is δ/8π with δ fixed by Gauss–Bonnet, and it would return 1/48 on a different carrier; a quantity that changes when the carrier changes is not a numerological coincidence about 120\.

**\[STATUS: S25.11a PROVEN (C45); S25.11b DERIVED-CONDITIONAL (C46, gate F-S25.21); S25.11c OBSERVATION (C47); Λ \= 0 and the 114-DOF reading DERIVED-CONDITIONAL/OBSERVATION. Independence of the geometry from A, Q and the double copy audited at C49. The v1.6 word "closure" is withdrawn.\]**

## **§6.5 Resolution of F-S25.19 — two different products, and a correction to v1.7**

**v1.7 got this wrong, and the v1.6 reviewer identified how.** v1.7 §6.5 claimed the 62 % leakage and ZS-S17's zero leakage were two \*readings\* of one product — an image statement versus a Hom-space statement. That is false. They are two **different products**, and v1.8 retracts the v1.7 resolution and replaces it.

**The actual difference.** ZS-S17 forms the alternating cup product as a **cyclic average over basepoints** of each face — the mean of the ordered product over all n cyclic starting points of an n-gon. Every version of ZS-S25 from v1.0 through v1.7 used a **fixed-basepoint** product instead. These are genuinely different bilinear maps, and the difference is exactly the mixed-symmetry, basepoint-dependent part that §3.7 had already measured varying from 15 % to 56 %. **Note the second row: the fixed-basepoint leakage is not a single number at all** — it ranges over 45.21 – 71.94 % across the six basepoint conventions (check C62), which is why no value quoted in v1.0–v1.8 was reproducible.

**Table 6.2.** Leakage of the two products out of the 2×T₁ active space (checks C54–C57).

| product | used by | 6-dim leakage | 6-dim Jacobi (Frobenius) | 3-dim projected Jacobi | c₁ |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **cyclic basepoint-average** | **ZS-S17** | **3.60 × 10⁻¹³ % (zero)** | **0.067484** | \< 2 × 10⁻¹⁶ | 0.3515993958 |
| fixed basepoint | ZS-S25 v1.0–v1.8 | 45.21 – 71.94 % (convention-dependent) | convention-dependent | — | 0.3515993958 |

**ZS-S17 is correct, and the fault was entirely ZS-S25's.** With the cyclic product the 2×T₁ image closes to machine zero — closure is a real property, not a definitional artefact — and the projected bracket is an exact so(3) structure (Frobenius Jacobi residual below 2 × 10⁻¹⁶ on both channels). Both products give the identical c₁ \= 0.3515993958, which is why that invariant was never in dispute. **No wording correction is owed upstream** (this reverses the v1.7 §6.5 verdict); ZS-S17's zero-leakage statement is literally true at its own product.

**What this does to the v1.5 retraction.** §0.1 and v1.5 reported that \*no active space closes\*, at 56–97 % leakage. That was computed with the fixed-basepoint product and is therefore a statement about the **wrong** bracket. Under the cyclic product the two-T₁ space **does** close. This does not automatically restore Corollary S25.7a — the multiplicity-space and selection questions of §3.8 are untouched, and the full 6-dim cyclic bracket has Frobenius Jacobi residual **0.067484**, not zero (checks C58, C64, reported against interest), so the clean Lie structure lives in the 3-dimensional projection rather than on the whole active space. But the blunt claim "nothing closes" is withdrawn: **the ZS-S17 active space closes exactly under the ZS-S17 product**, and ZS-S25 spent seven versions testing the wrong one.

**\[STATUS: F-S25.19 RE-RESOLVED in ZS-S17's favour — C54–C57, C59 (R/A). The v1.7 §6.5 resolution is RETRACTED. The v1.5 "nothing closes" claim is corrected to "nothing closes under the fixed-basepoint product; the active space closes under the cyclic product." Gate F-S25.19 CLOSED.\]**

# **§7. Zero Free Parameters and Anti-Numerology**

## **§7.1 Parameter audit**

Every quantity appearing in Theorems S25.1–S25.5 and Proposition S25.6 is either an element of Table 2.1, a consequence of the carrier geometry, or standard mathematics. The single computed number, c₁ \= 0.3515993958, is not fitted: it is an eigenvector contraction determined entirely by the vertex coordinates of the truncated icosahedron, and it reproduces an existing corpus value to ten digits. The dimensional argument of §5 uses no constants at all. The eigenvalues (+2, \+1, −1) are rational and forced by representation theory. Proposition S25.3a introduces no constant.

**Table 7.1.** Parameter audit. "Introduced" means: appears in this paper's results and is not derivable from a LOCKED input or standard mathematics.

| Quantity | Origin | Fitted? | Introduced? |
| ----- | ----- | ----- | ----- |
| **A** \= 35/437 | ZS-F2, LOCKED | no | no |
| **Q** \= 11 | ZS-F5, LOCKED | no | no |
| λ₁, λ\_h | carrier spectrum, LOCKED | no | no |
| c₁ \= 0.3515993958 | computed from coordinates | no | no |
| (+2, \+1, −1) | representation theory | no | no |
| 6 − 2D | dimensional analysis | no | no |
| **any other** | — | — | **none** |

## **§7.2 Pre-registered anti-numerology controls**

One arithmetic identity appears in §4 and must be policed rather than celebrated. Since Λ²(T₁) \= T₁ has dimension 3 \= dim **X** and Sym²(T₁) \= A ⊕ H has dimension 6 \= dim **Y**,

**Q \= dim Z \+ dim X \+ dim Y \= dim Z \+ ( dim X )² \= 2 \+ 9 \= 11\.**

Two controls were pre-registered before evaluation, with the acceptance threshold fixed at p ≤ 0.05.

**Control A (irrep control, exhaustive).** Among the five irreducible representations of I, how many R satisfy (dim Sym²R, dim Λ²R) \= (6, 3)? Result: two of five, namely T₁ and T₂. **p \= 0.400.** Does not clear 5 %.

**Control B (integer control, exact enumeration — changed in v1.1).** v1.0 estimated this by 200 000 Monte Carlo draws and obtained p ≈ 0.0551. The quantity is finite and needs no sampling. Over the 36 pairs (dim **Z**, dim **X**) ∈ {1,…,6}², the equation dim **Z** \+ dim **X** \+ Sym²(dim **X**) \= 11 has exactly two solutions, (2, 3\) and (6, 2), so

**p \= 2/36 \= 1/18 ≈ 0.05556   (exact; no seed, no sampling error).**

Does not clear 5 %. The exact value replaces the estimate in the ledger.

**The stronger finding is structural, and it is negative.** For any three-dimensional representation of any subgroup of SO(3), Λ² has dimension 3 and Sym² has dimension 6 automatically. The identity is therefore not a coincidence that survived a test; it is **forced** by dim **X** \= 3 and could not have come out otherwise. A forced identity carries no surprise and therefore no evidential weight (check C26, kind X).

**\[STATUS: HYPOTHESIS-weak, with the additional and more important annotation that the identity is structurally forced. NON-CLAIM NC-S25.5.\]**

# **§8. Cross-Paper Dependency and Version-Collision Audit**

**Table 8.1.** Dependency and collision audit. "Perturbed?" asks whether ZS-S25 changes the value, status or hypotheses of the upstream object.

| Consumed object | Source | Consumed by | Perturbed? |
| ----- | ----- | ----- | ----- |
| λ₁ \= 1.2428416164 | ZS-S7 / ZS-S21 | ZS-S7 (Λ\_QCD, m(0⁺⁺)), ZS-S17, ZS-S18, ZS-S24 | no — read only, value reproduced |
| ε-proportionality of c\_{rst} | ZS-S17 v2.2 | §3 | no — re-derived, not modified |
| Thm S18.9 factorisation, c₁ | ZS-S18 v1.6 | §3 | no — reproduced to 10 digits |
| Quartic ≠ cubic square | ZS-S18 v1.6 §4.4 | §3.5, §4.4 | no — now load-bearing for the restricted status of Thm S25.2 |
| A → 0⁺⁺, H → 2⁺⁺ | ZS-S18 v1.6 Thm S18.8 | §4.5 | no — reinterpreted, not altered |
| Z-bias field Φ | ZS-F1 | §4.6 | no — v1.1 explicitly does **not** identify Φ with the copy's scalar |
| Δ\_phys \> 0 | ZS-S24 v1.9 | §6.3 (firewalled) | no — explicitly not transported |
| {κ\_p} | ZS-S23, OPEN F-S23.6 | §3.6 | no — but v1.2 **withdraws** the v1.1 independence claim; the physical layer of Thm S25.2 is now conditional on F-S23.6 and F-S25.10 is restored to OPEN |
| Regge T-odd phase, φ\_CP | ZS-S6 | §6.2 | no — candidate role only |
| z\*, i-tetration fixed point | ZS-M1 | not consumed | no |
| log m \= h\_top(T\_m) | ZS-F47 | not consumed | no — deferred, see §11 |

**One live tension, reported.** ZS-M17 result M17.7 records a Wightman-QFT reconstruction of the Z-Spin lattice theory to a Lorentz-invariant continuum QFT, and M17.1 a continuum convergence ‖H\_a − H\_∞‖ \= O((a/ℓ\_P)²). If the object being reconstructed is K\_TI × a\_tℤ, Theorem S25.1 says the continuum limit is three-dimensional and the reconstruction cannot be to a four-dimensional theory. If instead the object is the BCC or Γ\_X ⊗ Γ\_Y tiling that M17.6 also names, there is no tension. The corpus does not currently state which. Registered as gate **F-S25.1**; this paper takes no position.

**No retraction of any upstream result is required by this paper.** Within ZS-S25 itself, v1.1 demotes two v1.0 claims (Theorem S25.2's title and scope; Corollary S25.4a → Hypothesis S25.H1), restricts one (Corollary S25.5a), converts one Theorem to a Proposition with a restricted domain (S25.6), tightens the language of one result throughout (§4), and reclassifies the verification ledger. Full record in §13.

# **§9. Confrontation with Observation**

This paper makes no four-dimensional prediction and therefore cannot be confirmed or refuted by four-dimensional data. What it can and must do is establish that it does not collide with data the corpus already respects.

**Table 9.1.** Consistency by non-interference. No entry is a prediction of ZS-S25.

| Observable | External value | ZS-S25 exposure | Verdict |
| ----- | ----- | ----- | ----- |
| Λ\_QCD | 260 ± 20 MeV (quenched lattice) | uses λ₁ read-only; ZS-S7 chain untouched | no interference |
| m(0⁺⁺) glueball | 1.73 ± 0.05 GeV | A → 0⁺⁺ label reinterpreted, value unchanged | no interference |
| α\_s(M\_Z) | 0.1180 ± 0.0009 (PDG \[19\]) | not consumed | no interference |
| c\_T/c − 1 | |·| \< 3 × 10⁻¹⁵ (GW170817 \[18\]) | §4.6 remark is a counting observation only | no interference |
| Ω\_m, S₈, H₀ | Planck 2018 \[17\] | not consumed; §5 forbids promoting G₃g² to G\_N | no interference |
| G\_N | 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻² | explicitly out of reach, gate F-S25.5 | no claim |

The one statement with observational flavour is negative: **if** a future Z-Spin paper derives a gravitational coupling from the carrier, Theorem S25.5 fixes what kind of number it can be. It cannot be G\_N in SI units without a metric-side datum, and it can be G₃g² without one.

# **§10. Falsification Gates**

Gates are layered by the kind of failure they represent. A mathematical gate fires on a proof error and is immediately decisive. A consistency gate fires on a collision inside the corpus and requires a revision. A scope gate fires on a misuse downstream. An observational gate fires on external data. Three gates are new in v1.1 (F-S25.12, F-S25.13, F-S25.14) and correspond to the three demotions.

**Table 10.1.** Pre-registered falsification gates for ZS-S25 v2.1.

| ID | Layer | Condition that fires the gate | Status |
| ----- | ----- | ----- | ----- |
| **F-S25.1** | Consistency | If ZS-M17's Wightman reconstruction is shown to concern K\_TI × a\_tℤ itself, then M17.7 and Theorem S25.1 cannot both stand. | OPEN |
| **F-S25.2** | Scope | If the finite so(3) cubic kinematic algebra of §3 is quoted as the spacetime kinematic algebra of Yang–Mills, the citation is rejected on sight. | STANDING |
| **F-S25.3** | Mathematical | If the corpus **Y**\-sector is shown to carry I-isotypes other than A ⊕ H, the Sym²(**X**) reading of §7.2 collapses. | OPEN |
| **F-S25.4** | Mathematical | If the ZS-S14 Lagrangian is shown to contain no parity-odd term, Proposition S25.6 selects the parity-even branch and the minimal carrier double copy has no propagating graviton. | OPEN |
| **F-S25.5** | Scope | If any Z-Spin paper promotes G₃g² to G\_N without an independent dimensionful datum, that inference is rejected on sight. | STANDING |
| **F-S25.6** (re-specified) | Mathematical | K is an algebraic kernel, not a kinetic operator, so no ghost follows from its sign — independent of whether K is the BCJ quartic (Hyp. S25.H2, open). The gate now asks only about the eventual gauge-fixed kinetic operator, which does not yet exist: if one is constructed and its spin-2 residue is negative at a physical pole, the route is CLOSED-NEGATIVE. | OPEN, re-specified |
| **F-S25.7** | Consistency | If no convention map is found relating this paper's c\_h² \= 0.0025500303, ZS-S17's 0.0095045494 and ZS-S18's 0.0012658090, the λ\_h channel normalisation is undefined corpus-wide. | OPEN |
| **F-S25.8** | Scope | If the 9 of T₁ ⊗ T₁ is read as a spacetime degree-of-freedom count anywhere downstream, the reading is rejected on sight. | STANDING |
| **F-S25.9** | Scope | If the ZS-S24 gap Δ\_phys is transported across the double copy and quoted as a gravitational gap, the transport is rejected on sight. | STANDING |
| **F-S25.10** (reopened in v1.5) | Mathematical | If the exact {κ\_p}-weighted Hessian is shown not to select a **closed** active space, the physical layer of Theorem S25.2 fails. v1.1 asserted closure of this gate without proof; v1.2 withdrew it; v1.4 claimed to prove it via Corollary S25.7a; **v1.5 withdrew that too, and v1.9 restates the reason: no candidate space is simultaneously product-closed and a strict Lie algebra (Table 0.1).** | **OPEN** |
| **F-S25.17** (demoted in v1.5) | Mathematical | Retained as a sub-question of F-S25.10 rather than its replacement: if the exact weighting is not I-equivariant, Theorem S25.7's census does not apply to it at all. | OPEN |
| **F-S25.18** (new) | Consistency | The carrier admits four cubic channels (two T₁ and two T₂), not the two the corpus records. If ZS-S17/S18 are shown to have excluded the T₂ channels by an argument rather than by choice, that argument must be located; if not, any result depending on the two-T₁ restriction is conditional on it. | OPEN |
| **F-S25.11** | Code | If the companion writes any file, requires any external asset, or reproduces a retracted value, the verification is void. | PASS |
| **F-S25.12** (fully reopened in v1.5) | Scope / Mathematical | Nine requirements are listed in §4.8; the carrier supplies one, and no single unprojected space is both product-closed and Lie, so full off-shell CK remains OPEN. Citing Theorem S25.2 or Proposition S25.8 as off-shell CK duality, on the active space or anywhere else, is rejected on sight. | **OPEN** |
| **F-S25.19** (resolved in v1.8, confirmed v1.9) | Consistency | **Product mismatch, not a corpus conflict.** ZS-S17 uses a cyclic basepoint-average product; ZS-S25 v1.0–v1.8 used a fixed-basepoint product. Under the cyclic product the two-T₁ space closes exactly (3.6 × 10⁻¹³ %), so ZS-S17 is correct and no upstream correction is owed. The v1.7 "one product, two readings" resolution is retracted. v1.9 adds that the fixed-basepoint figures were never reproducible constants (range 45–72 %, check C62). | **RESOLVED** |
| **F-S25.21** (new) | Mathematical | If the dictionary δ \= 8πG₃m is shown not to apply to a Regge carrier with 60 simultaneous defects — for instance because the defects interact at the order that matters — Proposition S25.11b's mass identification fails. The cone geometry and the D \= 3 local graviton count survive; the Λ \= 0 branch remains an independent assumption either way. | OPEN |
| **F-S25.22** (partially resolved in v1.8) | Mathematical | **Reduction proved (C60):** G₃g² \= (g²/m)·(G₃m) \= (g²/m)/120 exactly, so G₃m \= 1/120 converts any determination of the single dimensionless ratio g²/m directly into G₃g². **Honest negative (C61):** ZS-S24's H\_g \= g²L \+ g⁻²V has a gap for all g \> 0, so the corpus locks no value of g². Moreover the normalisation map between the finite-carrier coupling of ZS-S24 and the dimensionful (2+1) Yang–Mills g²\_YM — which requires the lattice spacing a, the time step a\_t and the kinetic normalisation to be restored — has never been established. The correct statement is therefore: **once that normalisation map is supplied, the bridge reduces algebraically to g²\_YM/m.** Until then G₃g² is not reduced to one unknown but to one unknown plus a missing dictionary. | OPEN — one dimensionless ratio plus one missing normalisation dictionary |
| **F-S25.20** (new) | Mathematical | If the three invariant-space coordinates of the ZS-S18 Wilson quartic are computed and do not admit a BCJ-compatible redistribution consistent with K, Hypothesis S25.H2 is CLOSED-NEGATIVE. | OPEN |
| **F-S25.13** (new) | Scope | If Hypothesis S25.H1 is cited as a derivation that Φ is the dilaton, rather than as a hypothesis awaiting an action-level intertwiner, the citation is rejected on sight. | STANDING |
| **F-S25.14** | Scope | If the kernel K of §4 is read as a gravitational Hessian, a gauge-fixed kinetic operator, a Hamiltonian, or a propagator residue, the reading is rejected on sight. | STANDING |
| **F-S25.15** (new) | Scope / Mathematical | If the isotypes of Theorem S25.4 are read as double-copy spacetime fields without exhibiting an intertwiner 𝒥 : T₁^carrier → V\_kin compatible with the kinetic pairing, the gauge transformation and the BRST differential, the reading is rejected on sight. This gate is the general form of F-S25.8, which ZS-S25 v1.1 itself violated. | STANDING / OPEN |
| **F-S25.16** (extended again in v1.5) | Consistency | If any Z-Spin paper, **or its companion code output**, states a result its own scope gates forbid, asserts in prose something no executed check examined, **or removes, replaces or weakens a check that failed**, that result is suspended pending audit. Four instances are on record within ZS-S25: v1.1 §4.5 against F-S25.8; the v1.1 normalisation explanation of C14; the v1.2 I\_h multiplicity statement; and — the worst — the v1.0 suppression of a failing closure check, which is the direct cause of the v1.5 retractions. All four were caught by review, none by the ledger. | STANDING |

# **§11. Non-Claims**

| ID | Not claimed by this paper |
| ----- | ----- |
| NC-S25.1 | No exhaustive novelty search has been performed. |
| NC-S25.2 | No positivity, ghost-freedom or unitarity of any gravitational operator. K is indefinite as an algebraic kernel; since it is not a kinetic operator, no ghost follows either way. |
| NC-S25.3 | No value of G₃g². **Theorem S25.11 gives G₃m, not G₃ and not m separately**, and the four-dimensional no-go against G\_N is not repaired. |
| NC-S25.4 | No graviton mass; no relation between φ\_CP, α \= π/10 and a Chern–Simons level. |
| NC-S25.5 | Q \= 11 is not derived or supported; §7.2 shows the identity is structurally forced and evidentially empty. |
| NC-S25.6 | No constraint algebra, discrete Bianchi identity, lapse–shift decomposition, extrinsic curvature or Regge–Einstein operator is constructed. §6.4 gives cone geometry (PROVEN) and a conditional point-particle reading only, **not** a gravitational closure. |
| NC-S25.7 | Gate F-S24.18 is not closed, {κ\_p} is not computed, the ZS-S14 slab action is not integrated. |
| NC-S25.8 | No cosmological statement. The ZS-F47 gaps A, B, C are untouched. |
| NC-S25.9 | The Clay Yang–Mills mass gap remains outside scope, as in ZS-S24 under F-S24.1. |
| NC-S25.10 | Full off-shell colour–kinematics duality of the ZS-S14 action is not claimed. Theorem S25.2 concerns only the projected cubic Jacobi tensor; it proves neither raw three-dimensional closure nor a six-dimensional Lie structure. |
| NC-S25.11 | Φ is not claimed to be the dilaton of a double copy; that is Hypothesis S25.H1, which now also awaits S25.H0. |
| NC-S25.12 | The isotypes A, T₁, H are not claimed to be dilaton, two-form and graviton. That reading requires Hypothesis S25.H0. No internal carrier index is identified with a spacetime index. |
| NC-S25.13 | Theorem S25.2 is not claimed to be independent of {κ\_p} at the physical level. (Reaffirmed after the v1.4 lapse.) |
| NC-S25.14 | No space is claimed to be **both** product-closed and a strict Lie algebra. Under the cyclic product the 6-dim two-T₁ space is closed but not Lie (residual 0.0675); the 3-dim channels are Lie only after projection and are not closed (26.72 %, 12.34 %). |
| NC-S25.15 | No off-shell colour–kinematics duality is claimed anywhere. Proposition S25.8 establishes one negative structural fact. |
| NC-S25.16 | K is not claimed to be the BCJ quartic; that is Hypothesis S25.H2. |
| **NC-S25.17** | **New in v1.6.** Theorem S25.11 does not derive the dictionary δ \= 8πG₃m, which is imported \[26, 27\]; does not determine G₃ or m separately; and asserts no relation between 1/120 and **A**, **Q**, λ₁ or c₁. |

# **§12. Conclusion**

The Z-Spin Standard-Model line asked whether its Yang–Mills operator is the single copy of a gravitational one. This paper answers a prior question that had gone unasked: on what kind of spacetime does that operator live? The answer, already recorded in the corpus's own check T052 and never used, is three dimensions. Everything else follows.

In three dimensions the double copy is not the search for two transverse-traceless graviton polarisations; within the minimal two-derivative family it is a parity choice between a propagating scalar with a topological gravity sector and a single massive graviton. In three dimensions the dimensional obstruction lifts far enough to admit one relative combination, G₃g², while leaving the four-dimensional no-go against G\_N exactly where it was. And in three dimensions the cubic kinematic tensor of the carrier is forced to be c₁ε, so the cubic kinematic Jacobi identity is a theorem rather than a hypothesis. The scope of that independence must be stated carefully, and v1.3 states it as follows: the abstract implication T ∈ Λ³W\* ⇒ T \= cε ⇒ Jacobi is independent of the missing integration **once the declared active space W is fixed**; whether that integration selects and preserves this W remains OPEN under F-S25.10.

**What is closed and what is not.** Closed: the three-dimensional carrier census; the **projected** three-dimensional self-channel tensor T \= c₁ε and its Jacobi identity (Thm S25.2); separately, the **six-dimensional cyclic image closure** (Prop. S25.2a), which is not a Lie structure; the A₅ isotypic decomposition, including the full I\_h content of every eigenspace; the isotypic spectrum of the algebraic single-exchange kernel; and the metric-independence of the kernel's indefiniteness, with its injectivity step supplied. Not closed: the exact ZS-S14 slab integration; whether the {κ\_p}-weighted Hessian selects the active space the theorem is stated on; full off-shell CK/BV completion including kinetic pairing, ghosts and a compatible quartic; the kinematic-index intertwiner 𝒥; the Z-bias field map 𝓘; the gravitational action and its constraint algebra; a ghost-free physical Hilbert space; G₃g²; and any four-dimensional emergence. **ZS-S25 is a G0 audit and redirection paper, not a completed gauge–gravity double copy, and should be cited as such.**

**What v1.4 attempted and v1.5 corrects.** v1.4 added three rigidity theorems and promoted all three past what they support. The census of irreducible self-channels survives, and with it the discovery of two T₂ channels the corpus had not recorded. The promotions do not. Behind all of them lay a hypothesis no version had ever tested — that the active space is closed under the vertex — and when v1.5 finally tested it the answer appeared to be 56 % to 97 % leakage on every candidate. **Those figures were computed with the fixed-basepoint product and are convention-dependent historical diagnostics, not current results**; under the correct cyclic product the six-dimensional space closes (§6.5).

Among the irreducible representations of I, exactly T₁ and T₂ admit a non-vanishing equivariant antisymmetric cubic self-map, and where one exists it is unique up to scale and equals c ε. The carrier realises four such channels. **The projected vertex is therefore rigid. Whether the projection is the physics is exactly what remains open — though §6.5 now shows the ZS-S17 active space does close under the correct (cyclic) product, which reopens in ZS-S17’s favour a question v1.5 had closed negatively.**

**And one geometric result is now unconditional.** §6.4 establishes that the spatial slice of the carrier is a flat cone surface with 60 identical defects of deficit π/15 (Theorem S25.11a, PROVEN). Under a static, Λ \= 0 point-particle reading (Proposition S25.11b, DERIVED-CONDITIONAL) each defect carries G₃m \= 1/120. v1.8 withdraws the v1.6 word "closure": Λ \= 0 is a branch choice not a consequence, the 114 moduli belong to the ambient 60-particle theory rather than to the fixed carrier, and no action, constraint algebra or time evolution is constructed. What remains genuinely closed is the geometry; the gravitational **reading** is conditional, and an actual gravitational closure is a successor paper. On the bridge to the gauge sector, v1.8 proves the reduction G₃g² \= (g²/m)/120 (gate F-S25.22) but reports the honest negative that g² is a free coupling in ZS-S24, so G₃g² reduces to the single unknown g²/m rather than closing. **The two items a successor should carry are that computation and the Regge–Einstein construction — one successor, not two.**

**The product mismatch is now resolved (§6.5).** ZS-S17 uses the **cyclic basepoint-averaged** product, under which the six-dimensional two-T₁ image closes to machine precision. ZS-S25 v1.0–v1.8 used a **fixed-basepoint** product whose leakage is convention-dependent, ranging over 45.21 – 71.94 %. The two maps share the invariant projected coefficient c₁ \= 0.3515993958 but differ away from that projection. **ZS-S17 requires no correction; the error was in ZS-S25.** The earlier v1.7 reading — that the two were one product read two ways, and that a wording correction was owed upstream — is withdrawn. **F-S25.19 is CLOSED.** The two gates that now carry the most value are F-S25.22 (compute g²/m, which delivers G₃g² since G₃m \= 1/120 is fixed) and F-S25.21 (derive the 2+1 mass dictionary inside the corpus).

**The two gaps that matter most are both intertwiners, and neither is numerical.** Between the internal icosahedral mode index and any spacetime index stands 𝒥, and between the composite scalar of the copy and the corpus field Φ stands 𝓘. Everything this paper computes lives strictly on the internal side of 𝒥. That is a narrower claim than v1.1 made, and it is the accurate one.

Three results are reported against interest and are the ones a reviewer should weigh most heavily. The single-exchange kernel is indefinite, and Proposition S25.3a shows no choice of internal contraction metric can change that — though this establishes an algebraic fact and **not** a ghost, since K is not a kinetic operator. The λ\_h channel amplitude computed here agrees with neither of the two values the corpus already carries for it. And the arithmetic identity Q \= dim **Z** \+ (dim **X**)², which looks like a discovery, is structurally forced and carries no evidential weight at all.

The single most valuable next computation is unchanged and is now triply motivated: integrate ∫√(−g) Tr(F ∧ ⋆F) explicitly over the 32 faces and 90 temporal prisms of K\_TI × a\_tℤ. Its output {κ\_p} decides gate F-S24.18; the presence or absence of a parity-odd term in the same integral decides, via Proposition S25.6, whether the minimal carrier double copy has a graviton at all; and the quartic sector of the same integral is the first of the three missing ingredients of gate F-S25.12. That is the content of a successor paper ZS-S26.

# **§13. Record of Revision**

Ten versions, seven external review rounds, every point integrated and none declined. No numerical output of any companion version has ever been found to be wrong; every correction has been to a statement \*about\* a correct computation, or — once, and worst — to a failing check that was removed instead of reported. That pattern is the reason gate F-S25.16 is aimed at this paper itself.

**Table 13.1.** One row per version. "Blocking" counts the points without which the reviewer refused closure.

| version | points (blocking) | principal demotions | principal additions |
| ----- | ----- | ----- | ----- |
| v1.0 | — | — | Thms S25.1–S25.6; 11 gates; 9 non-claims. c₁ \= 0.3515993958 reproduced to 10 digits |
| v1.1 | 6 (4) | Thm S25.2 → cubic active-space level only, F-S25.12; Cor. S25.4a → **Hyp. S25.H1**; Thm S25.6 → **Prop.**, "iff" withdrawn (New Massive Gravity); ghost language → UNDECIDED; §5 restricted to a monomial | **Prop. S25.3a**: tr K^η \= 0 for every η, so the indefiniteness is metric-independent. Kind-resolved ledger; exact enumeration p \= 1/18 |
| v1.2 | 8 (2) | Thm S25.4 restricted to A₅ isotypes; field reading moved behind new **Hyp. S25.H0** (𝒥); the {κ\_p}-independence claim withdrawn, **F-S25.10 reopened**; ref. \[8\] reattributed | Injectivity ε ε K^η \= 4c₁²η closes Prop. S25.3a. F-S25.14–16 |
| v1.3 | 6 (1) | Appendix A's "ten I\_h irreducibles once each" **withdrawn**; the D \= 3 polarisation argument for S25.H0 withdrawn; 3+1 Friedmann phrasing corrected | Full I\_h content by character orthogonality over 120 elements: 2A\_u ⊕ 2T₁\_g ⊕ 2T₂\_g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u; degeneracy at 8 named A\_u ⊕ G\_u |
| v1.4 | 5 (0) | five editorial patches; **A** and **Q** recorded as inputs to no theorem | **Thm S25.7** self-channel census; four channels found, not two, with two new T₂ structure constants; **Thm S25.9** quartic rigidity; basepoint independence of c₁ |
| v1.5 | 13 (3) | **Cor. S25.7a withdrawn**, F-S25.10 reopened; Thm S25.8 → **Prop.**, F-S25.12 reopened; Cor. S25.9a → **Hyp. S25.H2** | Ran the closure test no version had run, and reported large leakage on every candidate space. **Both the product and the reproducibility of the numbers were wrong — corrected in v1.8 and v1.9.** |
| **v1.6** | — | paper compressed; §13 collapsed to this table | Thm S25.11 asserted "gravitational sector closed" (G₃m \= 1/120, Λ \= 0, 114 DOF). **Over-read; corrected in v1.8.** New gates F-S25.21, F-S25.22 |
| v1.7 | — (review not received) | — | F-S25.19 "resolved" as one product read two ways. **This was wrong (see v1.8).** |
| **v1.9** | 9 (3) | consistency-only release; **all fixed-basepoint figures replaced by ranges** (they are convention-dependent, 45–72 %); Jacobi residuals renormalised to Frobenius (0.059 → **0.0675**); C50–C53 demoted to historical diagnostics (kind X); C41, C47–C49, C61 rescoped; Thm S25.2 renamed \*Projected Cubic Jacobi Tensor\*; §0.1, Abstract, §1.2–1.3, §3.6, §3.8, §4.8, NC-S25.14, F-S25.19, Table 6.1, Contents all propagated | **C62–C65:** the fixed-basepoint numbers were never reproducible constants; the cyclic ones are. **C64 separates closure from Jacobi:** the 6-dim two-T₁ space is closed (3.6 × 10⁻¹³ %) but not Lie (0.0675); the 3-dim channels are Lie after projection (10⁻¹⁷) but leak 26.72 % and 12.34 %. No unprojected space is both |
| **v1.8** | 13 (3) | **Thm S25.11 → S25.11a (PROVEN) \+ Prop. S25.11b (COND.) \+ Obs. S25.11c**; "gravitational closure", "Λ \= 0 forced", "114 DOF", "1/|G\_full| universal" all withdrawn; **v1.7 §6.5 retracted**; six companion PASS strings corrected; internal-state conflicts fixed | **F-S25.19 RE-resolved correctly**: ZS-S17 uses the cyclic basepoint-average product, which closes the 2×T₁ space to zero (C54); ZS-S25 used a fixed-basepoint product (62 %); the v1.5 "nothing closes" is corrected. **F-S25.22 reduction** G₃g² \= (g²/m)/120 proved, with the honest negative that g² is unlocked |

**The recurring fault, named once.** Four times the running text outran the ledger: v1.1 §4.5 against the paper's own gate F-S25.8; the v1.1 normalisation explanation of control C14; the v1.2 I\_h multiplicity statement; and — the worst, because it is not a misdescription but a deletion — a closure check written during v1.0 development that **failed at 26 % leakage and was replaced rather than reported**. Four versions of theorem-building then rested on the hypothesis it would have refuted. Gate F-S25.16 now covers removal or weakening of a failing check, and all four instances are named in it. All four were caught by review; none by the ledger.

# **Acknowledgements and Code Availability**

This paper was consolidated from internal Z-Spin Collaboration deep-exploration notes of July 2026, which were themselves an audit of an internal successor-topic recommendation. That recommendation proposed a seven-gate programme; three of its gates are shown here to be mis-specified, and a fourth is re-specified in v1.3. The paper has since passed through seven rounds of external review, every round recorded in §13. The author records that Proposition S25.3a exists only because a review forced a re-examination of §4.3; that the complete I\_h decomposition exists only because a review found the prose contradicting the companion; and that the correct identification of the ZS-S17 cyclic product — which reversed this paper's own v1.5 retraction — came from a reviewer, not from the author. Errors that remain are the author's.

Developed with the assistance of AI tools for symbolic checking, numerical verification and drafting; the author assumes full responsibility for all scientific content.

The companion **zs\_s25\_verify\_v2\_1.py** (1063 lines, Python 3, NumPy and SciPy only) rebuilds K\_TI from exact vertex coordinates with no imported data file; computes the edge and face incidence and the Euler characteristic by exhaustive enumeration; diagonalises the unweighted face Laplacian and reports its full multiplicity structure including the accidental degeneracy; constructs the gap edge potentials and evaluates the alternating cup product face by face; totally antisymmetrises and verifies T \= c₁ε and the cubic kinematic Jacobi identity to machine zero; runs the non-antisymmetrised bilinear as a negative control; builds the single-exchange kernel and verifies its symmetry, isotypic spectrum, tracelessness and indefiniteness; **scans all eight sign patterns and 40 000 random internal contraction metrics to confirm Proposition S25.3a**; reconstructs the 60 proper rotations of I from the vertex set and computes the **complete I\_h content of both the signed 2-cochain and the unsigned face permutation representations**, cross-checking them by the relation signed \= unsigned ⊗ A\_u; verifies the I ≅ A₅ character decomposition against the numerically computed rank of the vertex image; tabulates the degree-of-freedom and mass-dimension censuses; and executes the two pre-registered anti-numerology controls, the second now by exact enumeration. It emits results between BEGIN\_ZS\_S25\_RESULTS and END\_ZS\_S25\_RESULTS, writes no files, and exits non-zero on any FAIL.

**Ledger: 78 checks executed, 78 PASS, 0 FAIL — 34 R \+ 28 A \= 62 proof-bearing; 8 X \+ 5 L \+ 3 D \= 16 non-proof-bearing.** SHA256 \= 982b19cb069007a12476d6675e1028b2239d1ee30c65a0825689faf1e86653c6.

# **Appendix**

## **Appendix A — The carrier and its face Laplacian**

Even permutations of (0, ±1, ±3φ), (±1, ±(2+φ), ±2φ) and (±φ, ±2, ±(2φ+1)) with φ \= (1+√5)/2 give 60 vertices; the 90 edges are the pairs at the common minimal separation, which at these coordinates is exactly 2; the 32 faces are obtained by merging coplanar convex-hull simplices and split 12 pentagons and 20 hexagons; χ \= 2\. With B₂ the signed edge–face incidence matrix and unit weights, Δ₂ \= B₂ᵀB₂ is the 32 × 32 face Laplacian.

**Table A.1.** Spectrum of Δ₂ on K\_TI. Nine distinct eigenvalues, multiplicities summing to 32\.

| eigenvalue | multiplicity | note |
| ----- | ----- | ----- |
| 0.0000000000 | 1 | harmonic top-form; dim H²(K\_TI; ℝ) \= 1\. (H¹(K\_TI) \= 0 holds separately and is not what this kernel measures.) |
| **1.2428416164** | **3** | **λ₁, the T₁ gap — LOCKED** |
| 3.2679491924 | 5 | \= 5 − √3 |
| 4.8443660283 | 3 |  |
| 6.0000000000 | 4 |  |
| 6.7320508076 | 5 | \= 5 \+ √3 |
| **7.5210904061** | **3** | **λ\_h, the second T₁ — LOCKED** |
| 8.0000000000 | 5 | accidental degeneracy: two I\_h isotypes merge here |
| 8.3917019492 | 3 |  |

**Table A.2.** I\_h isotype decomposition of every eigenspace of Δ₂, reconstructed in the companion (check C7c, kind R) from the 60 proper rotations of I acting on the 32 oriented faces, with parity from the orientation-reversing inversion.

| eigenvalue | mult | I isotype | parity | note |
| ----- | ----- | ----- | ----- | ----- |
| 0.000000000 | 1 | A | u | harmonic top-form; H²(K\_TI; ℝ) ≅ ℝ |
| **1.242841616** | **3** | **T₁** | **g** | **λ₁ — LOCKED** |
| 3.267949192 | 5 | H | u | \= 5 − √3 |
| 4.844366028 | 3 | T₂ | g |  |
| 6.000000000 | 4 | G | g |  |
| 6.732050808 | 5 | H | u | \= 5 \+ √3 |
| **7.521090406** | **3** | **T₁** | **g** | **λ\_h — LOCKED; confirms the corpus T₁ assignment** |
| **8.000000000** | **5** | **A ⊕ G** | **u** | **the single accidental degeneracy: A\_u ⊕ G\_u** |
| 8.391701949 | 3 | T₂ | g |  |

**A correction, and a retraction of the v1.2 statement of this table.** v1.2 read Table A.2 as saying that "each of the five I-irreducible representations appears exactly twice, once even and once odd, so the representation contains each of the ten I\_h irreducible representations exactly once." **That sentence contradicts the companion’s own output and is withdrawn.** Summing the table gives A twice with parity u both times, T₁ twice with parity g both times, T₂ twice with parity g both times, H twice with parity u both times, and G once g and once u. v1.3 therefore computes the full I\_h content directly, by character orthogonality over all 120 elements of I\_h rather than by inspecting parities eigenspace by eigenspace (check C7d, kind R):

**signed 2-cochain representation \= 2A\_u ⊕ 2T₁\_g ⊕ 2T₂\_g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u   (dim 32).**

So the representation on which Δ₂ acts contains **six distinct I\_h types**, not the ten I\_h irreducibles once each. It has ten irreducible constituents counted with multiplicity — 2 \+ 2 \+ 2 \+ 1 \+ 1 \+ 2 \= 10 — and that is the likely origin of the erroneous statement, which confused a count of constituents with a count of distinct types. The accidental degeneracy at eigenvalue 8.0000000000 is specifically **A\_u ⊕ G\_u**.

**An independent consistency check on the correction (check C7e, kind A).** The companion also decomposes the \*unsigned\* face permutation representation, obtaining

unsigned face permutation representation \= 2A\_g ⊕ 2T₁\_u ⊕ 2T₂\_u ⊕ G\_g ⊕ G\_u ⊕ 2H\_g   (dim 32).

The signed representation differs from the unsigned one exactly by tensoring with the odd one-dimensional representation A\_u, since rotations act identically on the two while the inversion differs by the orientation sign. That predicts a g ↔ u swap on every constituent, leaving the self-conjugate pair G\_g ⊕ G\_u fixed. The two computed decompositions satisfy that relation exactly, which is a check on both. **Neither** representation contains the ten I\_h irreducibles once each, so the error was not a confusion between the two representations; it was simply wrong.

**What survives unaltered.** Both λ₁ and λ\_h carry T₁ and both are parity-even, which is exactly what the two-T₁ active space of ZS-S17 requires; that agreement is reconstructed here rather than imported, and nothing in Theorems S25.1–S25.5, Proposition S25.3a or Proposition S25.6 depended on the withdrawn sentence.

**Why 43/43 PASS did not catch this.** The v1.2 check C7c tested only that there are 60 proper rotations, that λ₁ and λ\_h are both T₁, and that the degeneracy at 8 merges A with G. It did not test the parity of each eigenspace or the full multiplicity multiset, so the prose could assert something the check never examined. v1.3 adds C7d, which compares the complete I\_h multiset against an explicit expected value, and C7e, which cross-checks it against the unsigned representation. This is the third occasion on which a statement in the running text outran what the companion actually verified — the first being the v1.1 violation of gate F-S25.8, the second the v1.1 normalisation explanation for control C14 — and gate **F-S25.16** is extended in v1.3 to cover it.

## **Appendix B — The kernel and Proposition S25.3a in closed form**

With T \= c₁ ε on ℝ³, contracting two vertices over one internal index with the identity gives

K\_{(ab),(cd)} \= c₁² Σ\_e ε\_{ace} ε\_{bde} \= c₁² ( δ\_{ab} δ\_{cd} − δ\_{ad} δ\_{cb} ),

so (K M)\_{ab} \= c₁² ( δ\_{ab} tr M − (Mᵀ)\_{ab} ), with eigenvalues 2c₁², \+c₁², −c₁² on the trace, antisymmetric and symmetric-traceless subspaces, multiplicities 1, 3, 5, and vanishing trace.

For a general internal contraction metric η, write η \= Σ\_k λ\_k v\_k v\_kᵀ. Since Σ\_e ε\_{ace} v\_e \= (\[v\]\_×)\_{ac},

K^η\_{(ab),(cd)} \= c₁² Σ\_k λ\_k (\[v\_k\]\_×)\_{ac} (\[v\_k\]\_×)\_{bd},   i.e.   K^η \= c₁² Σ\_k λ\_k A^{(k)} ⊗ A^{(k)}

with A^{(k)} \= \[v\_k\]\_× antisymmetric. Taking the trace of the 9 × 9 operator, tr(A ⊗ A) \= (tr A)² \= 0 for antisymmetric A, so tr K^η \= 0 identically in η.

**Injectivity of η ↦ K^η (supplied in v1.2).** Contracting K^η back against two Levi-Civita tensors and using ε\_{acp} ε\_{ace′} \= 2 δ\_{pe′} twice,

**ε\_{acp} ε\_{bdq} K^η\_{(ab),(cd)} \= c₁² ( ε\_{acp} ε\_{ace} ) ( ε\_{bdq} ε\_{bdf} ) η^{ef} \= 4 c₁² η\_{pq}.**

Hence K^η \= 0 forces η \= 0, and the map is injective. Verified to machine zero (check C17g). Combining: a traceless symmetric operator is zero or indefinite, and K^η vanishes only for η \= 0, so **the indefiniteness of the single-exchange kernel cannot be removed by any choice of internal contraction metric.** The numerical scan (C17e) finds the inertia never has fewer than four negative directions over all eight sign patterns and 40 000 random η.

This closes escape route (i) of §4.4 and **narrows** the remaining resolutions to (ii) K is not the operator whose sign matters, and (iii) the quartic completion contributes at the same order. It does **not** establish a ghost.

## **Appendix C — Anti-numerology protocol**

Both controls of §7.2 were specified before evaluation, with the acceptance threshold fixed at p ≤ 0.05. Control A is exhaustive over the five irreducible representations of I. Control B is, in v1.1, exhaustive over the 36 pairs (dim **Z**, dim **X**) ∈ {1,…,6}²; the v1.0 Monte Carlo with 200 000 draws and seed 20260721 gave 0.0551 and is superseded by the exact value 1/18 ≈ 0.05556. Neither control clears the threshold, and the pre-registered consequence — that the identity Q \= dim **Z** \+ (dim **X**)² is registered at HYPOTHESIS-weak and is not used to support any other claim — is applied. The additional structural finding, that the identity is forced for any three-dimensional representation of any subgroup of SO(3), was not pre-registered; it is reported as an OBSERVATION and it strengthens the negative verdict.

## **Appendix D — Verification ledger, resolved by kind**

**R** numerical reconstruction — a computation from the carrier coordinates that could have returned a different answer. **A** analytical confirmation — a finite check of a statement proved in the text. **X** control — a test of whether a hypothesis is automatic. **L** locked-input drift check — confirms an imported constant has not drifted. **D** declaration — records a definition. **Only R and A carry proof weight.**

**Table D.1.** Ledger by category. The aggregate "78/78" must not be quoted without this resolution.

| Category | Checks | Kind | Count |
| ----- | ----- | ----- | ----- |
| Carrier reconstruction and census | C1–C4 | R | 4 |
| Dimension of the product complex | C5 | D | 1 |
| Face Laplacian, kernel dimension counted, multiplicities | C6, C7, C7b | R | 3 |
| **I\_h isotype decomposition, all eigenspaces** | **C7c** | **R** | **1** |
| **Full I\_h content of the 2-cochain rep (new)** | **C7d** | **R** | **1** |
| **signed \= unsigned (x) A\_u consistency (new)** | **C7e** | **A** | **1** |
| Locked eigenvalues present and 3-fold | C8, C9 | L | 2 |
| Six-mode active space | C10 | D | 1 |
| c₁ reproduction and λ\_h convention gap | C11, C11b, C12 | R | 3 |
| ε-proportionality and correction direction | C11c, C13 | A | 2 |
| Negative control, non-alternating bilinear | C14 | X | 1 |
| Jacobi for ε | C15 | A | 1 |
| Kinematic Jacobi for the computed vertex | C16 | R | 1 |
| Off-shell statement | C17 | D | 1 |
| Kernel symmetry, spectrum, trace, indefiniteness | C17a–C17d | A | 4 |
| Contraction-metric inertia scan | C17e | R | 1 |
| tr K^η \= 0 for every η | C17f | A | 1 |
| **Injectivity ε ε K^η \= 4c₁²η (new)** | **C17g** | **A** | **1** |
| Character decomposition of T₁ ⊗ T₁ | C18–C20 | A | 3 |
| Rank of the alternating vertex image | C21 | R | 1 |
| Degree-of-freedom census | C22, C23 | A | 2 |
| Mass-dimension census | C24 | A | 1 |
| Anti-numerology controls (C27 now exact) | C25–C27 | X | 3 |
| Locked-input drift | C28–C30 | L | 3 |
| **Equivariant selection theorem (new)** | **C31–C34, C40** | **A \+ R** | **5** |
| **Graded commutativity and its H² class (new)** | **C35, C39** | **R** | **2** |
| **Basepoint independence of c₁ (new)** | **C36** | **R** | **1** |
| **Quartic rigidity (new)** | **C37, C38** | **A** | **2** |
| **Closure audit: leakage, Jacobi, basepoint (new)** | **C41–C44** | **R** | **4** |
| **Gravitational closure** | **C45–C49** | **R \+ A** | **5** |
| F-S25.19 (v1.7) — **demoted to historical diagnostics in v1.9** | C50–C53 | **X** | 4 |
| **F-S25.19 re-resolved: cyclic product (new)** | **C54–C59** | **R \+ A** | **6** |
| **F-S25.22 reduction (new)** | **C60, C61** | **A** | **2** |
| **Reproducibility audit (new)** | **C62–C65** | **R \+ A** | **4** |
| **Total** | **—** | **R 34 · A 28 · X 8 · L 5 · D 3** | **78 executed, 78 PASS, 0 FAIL** |
| **Proof-bearing** | **R \+ A** | **—** | **62** |
| **Non-proof-bearing** | **X \+ L \+ D** | **—** | **16** |

# **References**

## **Internal (Z-Spin Collaboration)**

\[Z1\]  K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[LOCKED.\]  
\[Z2\]  K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (2026). \[PROVEN: (Z, X, Y) \= (2, 3, 6).\]  
\[Z3\]  K. Kang, "The Z-Spin Action and U(1) Completion," ZS-F1 v1.0 (2026). \[Z-bias field Φ; Z-anchor.\]  
\[Z4\]  K. Kang, "Z-Transit CP Violation: Non-Abelian Holonomy and the lcm(5,7) Selection Rule," ZS-S6 v1.0 and v1.0(Revised) (2026). §4.1, §G.2. \[PROVEN: Regge T-odd scalar; α \= π/10.\]  
\[Z5\]  K. Kang, "The Spinor Mass Gap," ZS-S7 v1.0.0 (2026). §3, §5, §6.  
\[Z6\]  K. Kang, "The ZS-S14 Master Action," ZS-S14 v2.0 (2026). §3, §4.  
\[Z7\]  K. Kang, "The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex," ZS-S17 v2.2 FINAL (2026). §1. \[PROVEN: two-T₁ closure, ε-proportionality.\]  
\[Z8\]  K. Kang, "The Symmetric Two-Body Sector of the Z-Spin Master Action," ZS-S18 v1.6 FINAL (2026). Lemma S18.A, Theorems S18.4, S18.8, S18.9; §4.4. \[PROVEN: factorised cubic vertex, c₁ \= 0.3515993958, parity dictionary, quartic ≠ cubic square.\]  
\[Z9\]  K. Kang, ZS-S21 (2026). §3.1–3.2, checks T010–T020, T050–T052. \[PROVEN: carrier census; dim K\_TI \= 2.\]  
\[Z10\]  K. Kang, "Action-to-Hessian Bridge," ZS-S23 v1.3 (2026). §5.1–5.3, Theorem S23.4, Lemma S23.5, Theorem S23.6; gate F-S23.6.  
\[Z11\]  K. Kang, "Finite-Carrier Action-to-Gap Closure under the Canonical Holonomy Reduction," ZS-S24 v1.9 FINAL (2026). Theorems S24.2, S24.9, S24.12, S24.14; gates F-S24.1, F-S24.18.  
\[Z12\]  K. Kang, "Regge-Holonomy, Immirzi and Z-Telomere," ZS-M3 v1.0 (2026). Theorem 5.1, Lemma 10.1.  
\[Z13\]  K. Kang, ZS-M17 (2026). Results M17.1, M17.3, M17.6, M17.7. \[Cited for gate F-S25.1.\]  
\[Z14\]  K. Kang, ZS-M32 v1.0 (2026). §4. \[Operator-level phase quantum π/5.\]  
\[Z15\]  K. Kang, ZS-F47 v1.6 (2026). §6.1–6.4. \[Cited only to record that its gaps are untouched.\]  
\[Z16\]  K. Kang (ed.), The Book of Z-Spin Cosmology — Light Edition, v12.1 (2026).

## **External**

\[1\]  Z. Bern, J. J. M. Carrasco and H. Johansson, "New relations for gauge-theory amplitudes," Phys. Rev. D 78, 085011 (2008), arXiv:0805.3993.  
\[2\]  Z. Bern, J. J. M. Carrasco and H. Johansson, "Perturbative quantum gravity as a double copy of gauge theory," Phys. Rev. Lett. 105, 061602 (2010), arXiv:1004.0476.  
\[3\]  H. Kawai, D. C. Lewellen and S.-H. H. Tye, "A relation between tree amplitudes of closed and open strings," Nucl. Phys. B 269, 1 (1986).  
\[4\]  R. Monteiro and D. O'Connell, "The kinematic algebra from the self-dual sector," JHEP 07, 007 (2011), arXiv:1105.2565.  
\[5\]  M. Reiterer, "A homotopy BV algebra for Yang-Mills and color-kinematics," arXiv:1912.03110.  
\[6\]  L. Borsten, B. Jurčo, H. Kim, T. Macrelli, C. Saemann and M. Wolf, "Becchi-Rouet-Stora-Tyutin-Lagrangian double copy of Yang-Mills theory," Phys. Rev. Lett. 126, 191601 (2021), arXiv:2007.13803.  
\[7\]  L. Borsten, B. Jurčo, H. Kim, T. Macrelli, C. Saemann and M. Wolf, "Colour-kinematics duality, double copy, and homotopy algebras," PoS ICHEP2022, 426 (2022), arXiv:2211.16405.  
\[8\]  M. Ben-Shahar, F. Bonechi and M. Zabzine, "Off-shell double copy theories in BV," Commun. Math. Phys. 407, 107 (2026), doi:10.1007/s00220-026-05609-1, arXiv:2506.09869. \[**Authorship corrected in v1.2**; v1.0 and v1.1 misattributed this work to Borsten et al.\]  
\[9\]  R. J. Szabo and G. Trojani, "Homotopy double copy of noncommutative gauge theories," Symmetry 15, no. 8, 1543 (2023), arXiv:2306.12175.  
\[10\]  E. Witten, "(2+1)-dimensional gravity as an exactly soluble system," Nucl. Phys. B 311, 46 (1988).  
\[11\]  S. Deser, R. Jackiw and S. Templeton, "Topologically massive gauge theories," Ann. Phys. (N.Y.) 140, 372 (1982).  
\[12\]  M. Carrillo González, A. Momeni and J. Rumbutis, "Massive double copy in three spacetime dimensions," JHEP 08, 116 (2021), arXiv:2107.00611.  
\[13\]  N. Moynihan, "Scattering amplitudes and the double copy in topologically massive theories," arXiv:2006.15957.  
\[14\]  R. Bonezzi, C. Chiaffrino, F. Diaz-Jaramillo and O. Hohm, "Gauge invariant double copy of Yang-Mills theory: the quartic theory," Phys. Rev. D 107, 126015 (2023), arXiv:2212.04513.  
\[15\]  K. Osterwalder and E. Seiler, "Gauge field theories on a lattice," Ann. Phys. (N.Y.) 110, 440 (1978).  
\[16\]  M. Lüscher, "Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories," Commun. Math. Phys. 54, 283 (1977).  
\[17\]  Planck Collaboration (N. Aghanim et al.), "Planck 2018 results. VI. Cosmological parameters," Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.  
\[18\]  LIGO Scientific and Virgo Collaborations, "GW170817: observation of gravitational waves from a binary neutron star inspiral," Phys. Rev. Lett. 119, 161101 (2017).  
\[19\]  S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024).  
\[20\]  M. Reed and B. Simon, Methods of Modern Mathematical Physics IV: Analysis of Operators (Academic Press, New York, 1978).  
\[21\]  G. W. Gibbons, S. W. Hawking and M. J. Perry, "Path integrals and the indefiniteness of the gravitational action," Nucl. Phys. B 138, 141 (1978).  
\[22\]  T. Regge, "General relativity without coordinates," Nuovo Cimento 19, 558 (1961).  
\[23\]  H. Whitney, Geometric Integration Theory (Princeton University Press, Princeton, 1957).  
\[24\]  E. A. Bergshoeff, O. Hohm and P. K. Townsend, "Massive gravity in three dimensions," Phys. Rev. Lett. 102, 201301 (2009), arXiv:0901.1766.  
\[25\]  M. Ben-Shahar, F. Bonechi and M. Zabzine, "Off-shell color-kinematics duality from codifferentials," arXiv:2409.11484.  
\[26\]  S. Deser, R. Jackiw and G. 't Hooft, "Three-dimensional Einstein gravity: dynamics of flat space," Ann. Phys. (N.Y.) 152, 220 (1984).  
\[27\]  S. Deser and R. Jackiw, "Three-dimensional cosmological gravity: dynamics of constant curvature," Ann. Phys. (N.Y.) 153, 405 (1984).

# **Version History**

**v1.0 (July 2026): initial public release.** Consolidated from internal Z-Spin Collaboration deep-exploration notes up to The Book of Z-Spin Cosmology v12.1. Established Theorem S25.1 (the carrier is three-dimensional), Corollary S25.1a (the two-graviton gate is unsatisfiable as posed), Theorem S25.2 (then titled "cellular colour–kinematics duality"), Theorem S25.3 (the exchange kernel, spectrum (+2, \+1, −1)c₁², traceless and indefinite), Theorem S25.4 and Corollary S25.4a, Theorem S25.5, and Theorem S25.6 (then stated with a universal "if and only if"). Registered eleven gates and nine non-claims. Verification 37/37 PASS.

**v1.1 (July 2026): revision following external review; four blocking corrections and two further corrections, all integrated.** No numerical result of v1.0 was found to be in error; every change is to interpretation, scope, status or presentation. Full disposition table in §13.

**Demotions.** (i) Theorem S25.2 is renamed **the Projected Cubic Jacobi Tensor** and its status restricted to **PROVEN at cubic active-space level**; the claim of full off-shell colour–kinematics duality of the ZS-S14 action is withdrawn and registered as gate F-S25.12, with the four missing ingredients — kinetic pairing, BRST/BV complex with ghosts, Jacobi-compatible quartic (obstructed by ZS-S18 §4.4), and a full CK representation — tabulated in §3.5. The paper title is changed accordingly. (ii) Corollary S25.4a is withdrawn and replaced by **Hypothesis S25.H1**, DERIVED-CONDITIONAL on an explicit action-level intertwiner φ\_DC \= 𝓘(Φ); the representation dictionary is retained as PROVEN. (iii) Theorem S25.6 is demoted to **Proposition S25.6, Minimal Chern–Simons Branch Selection**, with the universal converse withdrawn because New Massive Gravity \[24\] is parity-even and propagates a massive spin-2. (iv) Corollary S25.5a is restricted to the unique algebraically independent dimensionless **monomial in G₃ and g² alone**, and the paper now states that the four-dimensional no-go against G\_N **stands**.

**Tightening.** The kernel K of §4 is defined as an **algebraic single-exchange kernel** before any spectrum is quoted, and the formulation **"K is indefinite as an algebraic kernel; ghost status is UNDECIDED"** replaces every looser phrasing in the Abstract, §4, the Conclusion and this history. UNDECIDED is added to the Epistemic Status Legend as distinct from OPEN. Three new gates F-S25.12, F-S25.13, F-S25.14 and two new non-claims NC-S25.10, NC-S25.11.

**New result obtained during revision.** **Proposition S25.3a:** for every internal contraction metric η, tr K^η \= 0, hence K^η is indefinite unless identically zero. This closes analytically the "wrong pairing" resolution offered in v1.0 §4.3, and thereby narrows the remaining resolutions to the two the reviewer identified. Confirmed numerically over all eight sign patterns and 40 000 random η (checks C17e, C17f).

**Ledger.** Reclassified by kind and reported only in resolved form: **39 executed, 39 PASS, 0 FAIL \= 13 R \+ 14 A (27 proof-bearing) \+ 4 X \+ 5 L \+ 3 D (12 non-proof-bearing).** Control B is now an exact enumeration, p \= 2/36 \= 1/18, replacing the v1.0 Monte Carlo estimate 0.0551.

**v1.2 (July 2026): second revision; two blocking corrections and five further corrections, all integrated.** Full disposition in §13.2. **Demotions:** (i) Theorem S25.4 is restricted to the A₅ isotypic decomposition with ambient SO(3) tensor-type labels, and the double-copy field reading is moved behind new **Hypothesis S25.H0**, the kinematic-index intertwiner 𝒥 : T₁^carrier → V\_kin, HYPOTHESIS-weak, gate F-S25.15, NC-S25.12; S25.H1 becomes conditional on S25.H0 as well. v1.1 §4.5 is recorded as having violated the paper's own gate F-S25.8, and new gate F-S25.16 is registered against that failure mode. (ii) The §3.6 claim that Theorem S25.2 is independent of {κ\_p} is **withdrawn**; the theorem is now two-layered, PROVEN for the abstract cubic algebra on the declared active space and DERIVED-CONDITIONAL for its identification with the action-selected physical space, and **gate F-S25.10 is restored to OPEN**, NC-S25.13. **Corrections:** Proposition S25.3a's injectivity step is proved via ε\_{acp} ε\_{bdq} K^η \= 4c₁² η\_{pq} (new check C17g); reference \[8\] is reattributed to Ben-Shahar, Bonechi and Zabzine, CMP 407, 107 (2026), with \[25\] added; the Abstract now says ghost status **UNDECIDED**, matching the body; the v1.1 explanation of the C14 control discrepancy as a normalisation effect is withdrawn as wrong, since a leakage fraction is scale-invariant. **Upgrade:** C6 now counts the kernel dimension, and C7b is not downgraded but **upgraded** — the companion reconstructs the 60 rotations of I and decomposes every eigenspace, confirming λ₁ and λ\_h are both T₁ and naming the accidental degeneracy at 8.0000000000 as **A ⊕ G** (Table A.2). Title changed to remove "Double Copy". **Ledger: 41 executed, 41 PASS, 0 FAIL \= 14 R \+ 15 A (29 proof-bearing) \+ 4 X \+ 5 L \+ 3 D (12 non-proof-bearing).**

**v1.3 (July 2026): third revision; one blocking correction and five further corrections, all integrated. Consistency and correction release; no new physical claim.** Full disposition in §13.3. **Blocking correction:** the v1.2 Appendix A statement that the 32-dimensional face representation contains each of the ten I\_h irreducibles once is **withdrawn** as contradicting the companion’s own output. The complete content, computed by character orthogonality over all 120 elements of I\_h, is **2A\_u ⊕ 2T₁\_g ⊕ 2T₂\_g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u** — six distinct I\_h types, ten irreducible constituents with multiplicity — and the accidental degeneracy at 8.0000000000 is **A\_u ⊕ G\_u**. New checks C7d and C7e test the full multiset and cross-check it against the unsigned face permutation representation through the exact relation signed \= unsigned ⊗ A\_u. **Further corrections:** the v1.2 auxiliary argument for S25.H0 from the one-dimensional polarisation count is withdrawn, since the off-shell Lorentz vector space in D \= 3 is itself three-dimensional and the reduction to one occurs only after gauge fixing; Corollary S25.1a is re-specified so that a 2+1-dimensional Hamiltonian/Friedmann constraint is recognised as well-posed while only its 3+1-dimensional form is mis-specified; the companion’s output labels are stripped of dilaton, two-form, graviton and spin-2 language in compliance with F-S25.15 and NC-S25.12, and its docstring and C17 status line are aligned with the paper; the Conclusion’s independence sentence is restricted to the declared active space; and the Contents gate and non-claim ranges, the §1.2 label, the review-point counts and the Δ₂ kernel cohomology label are corrected. Gate **F-S25.16 is extended** to cover companion output and prose that outruns an executed check, with all three internal instances placed on record. **Ledger: 43 executed, 43 PASS, 0 FAIL \= 15 R \+ 16 A (31 proof-bearing) \+ 4 X \+ 5 L \+ 3 D (12 non-proof-bearing).**

**v1.4 (July 2026): fourth revision. Five editorial patches from the v1.3 review, plus three new theorems responding to that review’s substantive scores.** Full disposition in §13.4. **New results:** **Theorem S25.7 (equivariant selection)** — a non-vanishing I-equivariant totally antisymmetric cubic vertex exists on exactly the isotypes T₁ and T₂, both of dimension 3, both with dim Hom\_I(Λ²R, R) \= 1 and dim Hom\_I(Sym²R, R) \= 0; hence no weighting {κ\_p} respecting icosahedral symmetry can yield structure constants other than so(3)’s, and **gate F-S25.10 is closed conditional on equivariance alone**, with new gate F-S25.17 for the residual. **Theorem S25.8** — the cellular cochain algebra is not graded-commutative, with the obstruction carrying a non-trivial H²(K\_TI; ℝ) class, yet its projection onto any admissible active space vanishes identically, so the Batalin–Vilkovisky factorisation criterion for off-shell colour–kinematics duality holds exactly on the active space; **F-S25.12 reclassified CLOSED-POSITIVE on the active space**. **Theorem S25.9** — the quartic sector is SO(3)-rigid, dim Hom\_I(T₁^⊗4, A) \= 3, and K \= c₁²(δδ − δδ) is the BCJ quartic; **Corollary S25.9b withdraws the ghost reading of K as a category error and re-specifies F-S25.6**. **New findings against the corpus:** the carrier admits **four** cubic channels, not two, the T₂ pair carrying structure constants \+0.0071641984 and \+0.0015865494 (new gate F-S25.18); and c₁ \= 0.3515993958 is confirmed basepoint-independent at all six basepoints. **A and Q are explicitly recorded in the metadata as inputs that do not enter any theorem of this paper.** **Ledger: 53 executed, 53 PASS, 0 FAIL \= 20 R \+ 21 A (41 proof-bearing) \+ 4 X \+ 5 L \+ 3 D.**

**v1.5 (July 2026): fifth revision. RETRACTION RELEASE.** Thirteen review points, three blocking, all integrated; see §0.1 and §13.5. **Withdrawn:** Corollary S25.7a (selection-irrelevance) in full, gate F-S25.10 reopened; the v1.4 title and CLOSED-POSITIVE status of Theorem S25.8, demoted to Proposition S25.8, gate F-S25.12 fully reopened; Corollary S25.9a demoted to Hypothesis S25.H2 with gate F-S25.20, and the "two ratios" reduction withdrawn. Corollary S25.9b narrowed to ground already secure in v1.3. **New and decisive:** the closure test that no version had run — ‖(1 − P\_W)B(W,W)‖/‖B(W,W)‖ — gave large leakage on all four channels and on the ZS-S17 two-T₁ space (check C41). **Both the product and the reproducibility of these figures were wrong; corrected in v1.8 and v1.9**; the raw bracket fails Jacobi on every channel with residuals 0.47–1.38 (C42); and the mechanism is that only the totally antisymmetric part c₁ is basepoint-independent while the mixed part varies 15–56 % with basepoint (C43). **This contradicts ZS-S17's zero-leakage claim (check C44, gate F-S25.19)** at the same definition that reproduces c₁ \= 0.3515993958 to ten digits. Recorded against interest: the v1.0 suppression of a failing closure check is the direct cause of the retractions, and gate F-S25.16 is extended to cover removal of failing checks. **Retained unaffected:** the self-channel census, the four-channel discovery, the two new T₂ structure constants, the I\_h decomposition, quartic rigidity, the kernel spectrum, Proposition S25.3a, and the D \= 3 redirection. **Ledger: 57 executed, 57 PASS, 0 FAIL \= 24 R \+ 21 A (45 proof-bearing) \+ 4 X \+ 5 L \+ 3 D.**

**v1.6 (July 2026): sixth revision. Gravitational closure, and compression.** **New: Theorem S25.11** closes the gravitational sector of the carrier outright. K\_TI is a flat polyhedral 2-sphere whose curvature sits entirely in 60 identical conical defects of deficit π/15; under the standard (2+1) dictionary \[26, 27\] each carries **G₃m \= δ/8π \= 1/2N \= 1/120 \= 1/|I\_h|** exactly, the total saturates Gauss–Bonnet at ΣG₃m \= χ/4 \= 1/2, **Λ \= 0 is forced**, and the sector has **0 local and 114 global degrees of freedom** with a 228-dimensional reduced phase space. Zero free parameters; the same formula gives 1/48 \= 1/|O\_h| on the truncated-octahedron carrier, so the rule is G₃m \= 1/|point group| and not a fitted number. **The route is independent of every v1.5 retraction** (check C49): it uses Theorem S25.1, Gauss–Bonnet and the external dictionary, and none of active-space closure, colour–kinematics, K, S25.H0–H2, {κ\_p}, **A** or **Q**. New gates F-S25.21 (derive the dictionary internally) and F-S25.22 (compute g²/m, which now delivers G₃g², the highest-value remaining calculation); NC-S25.17. **Compression:** §13 collapsed from five subsections to one table, §11 to a table, the legend and §1.3 condensed, and the {κ\_p} narrative told once instead of three times. **Ledger: 62 executed, 62 PASS, 0 FAIL \= 26 R \+ 24 A (50 proof-bearing) \+ 4 X \+ 5 L \+ 3 D.**

**v1.7 (July 2026): seventh revision. F-S25.19 resolved (incorrectly; see v1.8).** With no v1.6 review received, v1.7 acts on the highest-value open gate. **§6.5 resolves F-S25.19**: the ZS-S17 zero-leakage claim and this paper’s 62 % leakage denote different objects — the well-definedness of the projected structure tensor c\_{rst} (a Hom-space statement, dim Hom\_I(Λ²W, W) \= 1, consistent) versus the leakage of the raw cup image out of the active space (a subalgebra statement, real). Both image readings, input- and output-projected, give 62.25 %; the projected tensor captures 61 % of the norm and is well-defined; 28.4 % of the cup image is non-exact in C², which is the mechanism (checks C50–C53). The shared invariant c₁ \= 0.3515993958 is identical to ten digits, so no downstream number moves; the glueball chain consumes c₁ and c\_{rst}, not the raw image. The gate is closed as a definitional divergence, with one wording correction owed to ZS-S17. **Ledger: 66 executed, 66 PASS, 0 FAIL \= 29 R \+ 25 A (54 proof-bearing) \+ 4 X \+ 5 L \+ 3 D.**

**v1.8 (July 2026): eighth revision. Integrates the v1.6 review (thirteen points, three blocking) and corrects v1.7.** **Blocking corrections:** (1) Theorem S25.11 "gravitational closure" is split into **S25.11a** (equal-deficit cone geometry, PROVEN), **Proposition S25.11b** (point-particle reading G₃m \= 1/120, DERIVED-CONDITIONAL on the static Λ \= 0 branch and the imported dictionary) and **Observation S25.11c** (symmetry rewriting); the words "closure", "Λ \= 0 forced", "114 fully-counted DOF" and the universal 1/|G\_full| rule are withdrawn, and the general law is corrected to G₃m \= χ/4N. (2) The v1.7 §6.5 resolution of F-S25.19 is **retracted**: ZS-S17 uses a cyclic basepoint-average product and ZS-S25 a fixed-basepoint product — two different maps, not two readings — and the cyclic product closes the 2×T₁ space to 3.6×10⁻¹³ % (C54–C57), so ZS-S17 is correct and the v1.5 "nothing closes" retraction is itself corrected. (3) Six overclaiming companion PASS strings (C32, C35, C38, C40, C43, C44) are rewritten to state only what is tested. **Parallel result on F-S25.22:** the reduction G₃g² \= (g²/m)/120 is proved (C60), with the honest negative that ZS-S24 locks no g², so G₃g² reduces to one unknown rather than closing (C61). Internal-state conflicts from the review’s §7 table are reconciled. **Ledger: 74 executed, 74 PASS, 0 FAIL \= 34 R \+ 28 A (62 proof-bearing) \+ 4 X \+ 5 L \+ 3 D.**

**v1.9 (July 2026): ninth revision. CONSISTENCY-ONLY RELEASE — no new physics.** Nine review points, three blocking, all integrated. **(1) Reproducibility defect fixed.** The reviewer ran the v1.8 companion and obtained different numbers (62.95 % vs 62.25 %, and similar). v1.9 traces this to the fixed-basepoint convention: leakage on the two-T₁ space ranges over **45.21–71.94 %** across the six basepoints (check C62), so no single value was ever reproducible. All such figures are replaced by ranges. Jacobi residuals are renormalised from the basis-dependent max-norm to the invariant Frobenius norm (check C65); the six-dimensional value becomes **0.0675**, superseding 0.059. **(2) Global state propagation.** Every surviving v1.5/v1.7 sentence is replaced: §0.1 rewritten, Abstract and §1.2–1.3 novelty claims, §3.6, §3.8, §4.8 requirement table, NC-S25.14, the F-S25.19 gate row, Table 6.1, the Contents ranges and revision range. **(3) Theorem S25.2 renamed** \*The Projected Cubic Jacobi Tensor\*, because check C64 shows closure and the Jacobi identity hold on **different** objects: the six-dimensional two-T₁ space is product-closed but not Lie, each three-dimensional channel is Lie only after projection and leaks 26.72 % and 12.34 %. **(4) Companion messages rescoped:** C41 restricted to the fixed-basepoint product, C47 corrected to G₃m \= χ/4N with 1/|G\_full| a two-carrier corollary, C48 restated as an ambient-moduli observation, C49 stripped of "closure", C61 stripped of the self-dual sentence and given the missing normalisation caveat, and C50–C53 demoted from proof-bearing to historical diagnostics (kind X). **Ledger: 78 executed, 78 PASS, 0 FAIL \= 34 R \+ 28 A (62 proof-bearing) \+ 8 X \+ 5 L \+ 3 D.**

**v2.0 (July 2026): final consistency release. No new physics.** Nine review points, four blocking, all integrated. **(1) Theorem S25.2 is split** into **Theorem S25.2** (Projected Cubic Jacobi Tensor — the three-dimensional projection, Lie, Frobenius residual \< 2 × 10⁻¹⁶) and **Proposition S25.2a** (Six-Dimensional Image Closure — W₆ closed to 3.6 × 10⁻¹³ % but **not** a Lie algebra, residual 0.067484). Earlier phrasing merged the two and is withdrawn. **(2) §6.5 and Table 6.2 synchronised** to the v1.9 companion: the fixed-basepoint leakage is given as the range 45.21 – 71.94 % rather than a single value, the six-dimensional Jacobi residual as the Frobenius 0.067484 rather than 0.059, and the projected residual as \< 2 × 10⁻¹⁶. **(3) G₃m \= χ/4N reclassified DERIVED-CONDITIONAL** throughout; the unconditional geometric law is δ \= 2πχ/N alone. Companion C46 now reads "zero fitted parameters within the static Λ \= 0 point-particle branch" and C47 separates the unconditional deficit law from the conditional mass law. **(4) Residual strings cleared:** Abstract (both the gravitational-number sentence and the S25.7 summary), §1.2, §1.3, gates F-S25.12, F-S25.21 and the F-S25.22 status cell, NC-S25.10, the cover ledger, the §13 aggregate count, the Version History ordering, and the companion docstring, section header, duplicate KIND entry, C17 and C57. **Ledger unchanged: 78 executed, 78 PASS, 0 FAIL \= 34 R \+ 28 A (62 proof-bearing) \+ 8 X \+ 5 L \+ 3 D (16 non-proof-bearing).**

**v2.1 (July 2026): final error-correction release. No new research.** Two blocking defects and five residual strings from the v2.0 review, all corrected; no check, number or status changed. **(1) §3.3 rewritten.** v2.0 separated Theorem S25.2 and Proposition S25.2a in the Abstract but left the main-body statement in its old form — asserting the result "on the two-T₁ active space" and then using dim W \= 3 in the proof, which merged a six-dimensional space with a three-dimensional projection, and omitting Proposition S25.2a from §3 entirely. §3.3 now states both results separately, each with its own proof and status: **Theorem S25.2** for T\_R \= Alt(P\_R B\_cyc|\_{Λ²R}) \= c\_R ε, PROVEN for the projection only and explicitly not asserting closure of R; **Proposition S25.2a** for B\_cyc(W₆, W₆) ⊆ W₆ at 3.60 × 10⁻¹³ % with ‖J‖\_F/‖B‖²\_F \= 0.067484, PROVEN for image closure and REFUTED for Lie structure. **(2) §12 Conclusion rewritten.** It still repeated the v1.7 reading — that the two leakage figures were one product read two ways and that a wording correction was owed to ZS-S17 — which v1.8 withdrew. It now states the product mismatch, that ZS-S17 requires no correction, and that the error was ZS-S25’s. **(3) Residual strings:** the cover ledger’s trailing "= 12 non-proof-bearing" clause deleted; §1.2’s two "cubic kinematic Lie algebra" summaries replaced; §3.6’s status line restricted to the projected tensor; Observation S25.11c’s opening sentence made conditional; and the Conclusion’s recital of the 56–97 % figures marked as convention-dependent historical diagnostics. **Ledger unchanged: 78 executed, 78 PASS, 0 FAIL \= 34 R \+ 28 A (62 proof-bearing) \+ 8 X \+ 5 L \+ 3 D (16 non-proof-bearing); companion identical to v2.0 apart from its version string.**

**Presentation.** Page numbers and a short contents table added. Role restated in the metadata: **ZS-S25 is a G0 audit and dimensional redirection paper, not a completed gauge–gravity double copy.** Zero free parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2), λ₁ and λ\_h LOCKED and none re-fitted. Companion zs\_s25\_verify\_v2\_1.py, 1063 lines, SHA256 982b19cb069007a12476d6675e1028b2239d1ee30c65a0825689faf1e86653c6.