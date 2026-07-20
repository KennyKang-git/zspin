**ZS-S11**

**Standard Model Anomaly Cancellation as Polyhedral Sector Identities**

A V-E-F Reformulation of the Five Anomaly Conditions in Z-Spin Cosmology

Kenny Kang  
April 2026 — ZS-S11 (Standard Model Theme)  
Version 1.0 — April 2026

**Verification: 30/30 PASS | Zero Free Parameters | Anti-numerology MC 500k**

**§0. Abstract**

The Standard Model (SM) gauge anomaly cancellation conditions A1–A5 (the five anomaly-freedom requirements derived from triangle diagrams and the discrete Witten anomaly) are automatically satisfied by the Trinity Braiding hypercharges Y\_Q \= \+1/6, Y\_u \= \+2/3, Y\_d \= −1/3, Y\_L \= −1/2, Y\_e \= −1, Y\_νR \= 0 of ZS-U9 v1.0 §7 (PROVEN at integer arithmetic). This paper reformulates that PROVEN cancellation in the Z-Spin (X, Z) sector language, where (X, Z) \= (3, 2\) is locked by ZS-F5 (Cayley-Hamilton recoupling, PROVEN) and ZS-M3 Theorem 5.1 (j \= 1/2 uniqueness, PROVEN).

Three structural results are established. (T1) The A2 (\[SU(2)\]² × U(1)\_Y) anomaly reduces to the linear sector identity X − Z \= 1; A3 reduces to A2/X (algebraically redundant under the sector identification). (T2) The A4 (\[U(1)\_Y\]³) cubic anomaly factorizes as A4(X, Z) \= (X − Z)(X \+ Z)(X \+ Z − 5)/(X·Z)², revealing three structural factors with distinct meaning. (T3) The joint A2 ∧ A4 conditions uniquely select (X, Z) \= (3, 2\) among the 45 positive integer partitions of Q \= 11, matching ZS-F5 PROVEN values exactly.

The five SM anomaly conditions thus collapse to four structural identity groups: SU(5) Linear (A2/A3/A5), SU(5) Cubic (A4), A₅ Real Representation (A1, conditional on Gap G2), and Z₂ Seam Topology (Witten, conditional on Gap G2). The (X \+ Z − 5\) factor of A4 admits two independent PROVEN derivations: from ZS-F5 (X \+ Z \= Q − Y \= 11 − 6 \= 5\) and from McKay Z₅ → Â₄ → SU(5) (ZS-M9 §5, PROVEN).

This paper does not derive new physical predictions, does not close Gap G2 (ZS-M9 Table 2 HYPOTHESIS strong remains open; closure is the subject of forthcoming ZS-M15), and does not introduce free parameters. Its contribution is the structural reformulation that clarifies how SM anomaly freedom is encoded in Z-Spin's polyhedral geometry. Verification: 30/30 PASS. Anti-numerology Monte Carlo with three baskets (independent (X, Z) sampling, Q \= 11 partition restriction, Q → ∞ asymptotic), all confirming the structural significance of the joint A2 ∧ A4 selection.

**Keywords:** Standard Model, anomaly cancellation, polyhedral geometry, McKay correspondence, SU(5) Cartan, sector decomposition, V-E-F reformulation, Z-Spin Cosmology, zero free parameters

**§0.1 Epistemic Status Legend**

**Table 0.1. Epistemic Status Legend (standard Z-Spin convention).**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; complete proof under declared definitions. |
| **DERIVED** | Follows from Z-Spin action plus PROVEN inputs. Zero free parameters beyond A. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated upstream assumption. |
| **VERIFIED** | Numerically confirmed against observational data or independent computation. |
| **TESTABLE** | Well-defined prediction awaiting experimental data. |
| **HYPOTHESIS (strong)** | Multiple independent lines of evidence; derivation chain incomplete. |
| **HYPOTHESIS** | Physically motivated conjecture; derivation chain incomplete. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests. |
| **OPEN** | Recognized gap requiring future work. |
| **NON-CLAIM** | Explicitly not asserted; documented to prevent overclaim. |
| **RETRACTED** | Previously claimed, now withdrawn with documented reason. |

**§1. Introduction**

**§1.1 The Five SM Anomaly Conditions and Z-Spin's Logical Inversion**

In the Standard Model (Weinberg, QFT vol. II; Peskin–Schroeder §20), the five gauge anomaly cancellation conditions — A1 \[SU(3)\]³ color, A2 \[SU(2)\]² × U(1)\_Y, A3 \[SU(3)\]² × U(1)\_Y, A4 \[U(1)\_Y\]³ cubic, A5 mixed gauge-gravitational, plus the discrete Witten SU(2)⁴ anomaly (π₄(SU(2)) \= ℤ₂) — are typically used as constraints to determine the hypercharge spectrum (Y\_Q, Y\_L, Y\_u, Y\_d, Y\_e). The standard derivation chain runs from anomaly freedom to charge assignments.

Z-Spin Cosmology inverts this logical direction. The Hypercharge Trinity Braiding Theorem (ZS-U9 v1.0 §6, DERIVED conditional on Gap G2) derives all SM hypercharges from three PROVEN ingredients (Compact Phase Integer Lattice, Yukawa Gauge-Lift, McKay SU(5) Cartan) plus the Neutral-Higgs Hypercharge Fixing (Theorem T3, DERIVED). The five anomaly conditions are then automatically satisfied as direct arithmetic consequences (ZS-U9 §7 PROVEN at integer precision).

This paper takes that PROVEN cancellation and asks a sharper question: what does the cancellation mean structurally in Z-Spin's polyhedral sector language? The (X, Y, Z) \= (3, 6, 2\) decomposition with Q \= 11 is locked by independent axioms (ZS-F5 Cayley-Hamilton recoupling PROVEN; ZS-M3 Theorem 5.1 j \= 1/2 intertwiner uniqueness PROVEN). Reformulating the five anomaly conditions in this sector language reveals four structural identity groups, two novel polynomial identities (Theorems 3.1 and 3.3), and a joint-uniqueness theorem (Theorem 4.1) that selects (X, Z) \= (3, 2\) among the 45 positive integer partitions of Q \= 11\.

**§1.2 What This Paper Is and Is Not**

This paper IS: (i) a structural reformulation of the ZS-U9 §7 PROVEN result in (X, Z) sector language; (ii) a presentation of new algebraic identities (A4 cubic factorization, A3-A2 redundancy, joint partition uniqueness); (iii) a four-group classification framework for the SM anomaly conditions in Z-Spin terms.

This paper IS NOT: (i) a derivation of new physical predictions (all numerical predictions remain in upstream papers ZS-S1, ZS-S2, ZS-U9, etc.); (ii) a closure of Gap G2 (ZS-M9 Table 2 HYPOTHESIS strong remains open; the closure plan is laid out in ZS-U9 §8.2 and is the subject of forthcoming ZS-M15 via Route (b) exhaustive falsification); (iii) an introduction of new free parameters (all inputs are LOCKED from prior papers, with A \= 35/437 the sole geometric input).

**§1.3 Locked Inputs**

**Table 1.1. All inputs locked from prior papers. No new free parameters introduced.**

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 | **LOCKED** |
| Q (register dimension) | 11 | ZS-F5 v1.0 | **PROVEN** |
| (Z, X, Y) sector dims | (2, 3, 6\) | ZS-F5, ZS-M3 v1.0 | **PROVEN** |
| dim(Z) \= 2 (j \= 1/2) | 2 | ZS-M3 Theorem 5.1 | **PROVEN** |
| SU(5) Cartan Y | diag(−1/3,−1/3,−1/3,+1/2,+1/2) | ZS-U9 Theorem 5.1 | **PROVEN** |
| Trinity Y values | Y\_Q=+1/6, Y\_L=−1/2, Y\_u=+2/3, Y\_d=−1/3, Y\_e=−1 | ZS-U9 §6 | **DERIVED** |
| McKay Z₅ → Â₄ → SU(5) | full chain | ZS-M9 §5 | **PROVEN** |
| 8\_adj(SU(3)) \= 3 ⊕ 5 | under A₅ ⊂ SU(3) | ZS-F0 §4.3 | **PROVEN** |
| 5/5 anomaly arithmetic | all PASS | ZS-U9 §7 | **PROVEN** |
| |I\_h/T\_d| \= 5 | 120/24 \= 5 | ZS-M9 §10 Table 7 | **PROVEN** |

**§1.4 Outline**

§2 establishes the (X, Z) sector Cartan reformulation as the technical foundation. §3 systematically reformulates each of the five SM anomaly conditions in sector language, with subsections §3.1 (Witten), §3.2 (A1), §3.3 (A2), §3.4 (A3), §3.5 (A4 — the principal novel result), and §3.6 (A5). §4 presents the joint uniqueness theorem and the four-group classification. §5 registers ten falsification gates. §6 reports the three-basket anti-numerology Monte Carlo (500k samples each). §7 enumerates eight non-claims to prevent overreach. §8 concludes and identifies future work, with explicit forward reference to ZS-M15 (Gap G2 closure).

**§2. The (X, Z) Sector Cartan Reformulation**

**§2.1 SU(5) Cartan in Sector Coordinates**

ZS-U9 Theorem 5.1 (PROVEN) establishes that the U(1)\_Y hypercharge generator embedded in su(5) takes the block-diagonal form Y \= diag(a, a, a, b, b), acting on the SU(5) fundamental representation 5 \= (3, 1, −1/3) ⊕ (1, 2, \+1/2) under the Georgi–Glashow branching SU(5) → SU(3)\_C × SU(2)\_L × U(1)\_Y.

Under the Z-Spin sector identification — namely, that the three color-block diagonal entries correspond to the X-sector (dim X \= 3\) and the two weak-block diagonal entries correspond to the Z-sector (dim Z \= 2\) — we adopt the parametrization:

a \= −1/X,    b \= \+1/Z

For Z-Spin's locked values (X, Z) \= (3, 2), this gives a \= −1/3, b \= \+1/2, reproducing the Trinity-derived Cartan Y \= diag(−1/3, −1/3, −1/3, \+1/2, \+1/2) of ZS-U9 §6 (DERIVED) without modification.

**§2.2 Traceless Condition as Sector Balance**

The su(5) traceless condition Tr(Y) \= 0 (standard Lie algebra fact) becomes, under the sector identification, the balance equation:

Tr(Y) \= X · a \+ Z · b \= X · (−1/X) \+ Z · (+1/Z) \= −1 \+ 1 \= 0

The cancellation is automatic: each sector contributes −1 or \+1 to the trace, regardless of the specific (X, Z) values, as long as a \= −1/X and b \= \+1/Z. This reformulation is algebraically equivalent to the standard SU(5) traceless 3a \+ 2b \= 0 (ZS-U9 Theorem 5.1 PROVEN), but expressed in sector language.

**§2.3 Lemma 2.1 (Sector Cartan Identification)**

**Lemma 2.1 (Sector Cartan Identification).** Under the Z-Spin sector identification a \= −1/X, b \= \+1/Z applied to Y \= diag(a, a, a, b, b) acting on the SU(5) fundamental representation 5 \= (3, 1, −1/3) ⊕ (1, 2, \+1/2), the standard SM physical hypercharges arise as natural combinations of (a, b):

**Table 2.1. SM hypercharges from sector parameters at (X, Z) \= (3, 2).**

| SM Particle | Sector formula | Value | Trinity reference |
| ----- | ----- | ----- | ----- |
| Y\_Q (Q\_L, in 10\) | a \+ b \= −1/X \+ 1/Z | \+1/6 | ZS-U9 Y\_Q \= \+1/6 ✓ |
| Y\_u (u\_R, in 10\) | −2a \= \+2/X | \+2/3 | ZS-U9 Y\_u \= \+2/3 ✓ |
| Y\_d (d\_R, in 5̄) | −a (after conj.) | −1/3 | ZS-U9 Y\_d \= −1/3 ✓ |
| Y\_L (L\_L, in 5̄) | −b \= −1/Z | −1/2 | ZS-U9 Y\_L \= −1/2 ✓ |
| Y\_e (e\_R, in 10\) | \+2b \= \+2/Z \= \+1 | \+1 (anti-particle conv.) | Y\_e^{phys} \= −1 ✓ |
| Y\_νR (in 1\) | 0 | 0 | ZS-U9 Y\_νR \= 0 ✓ |

**\[STATUS: DERIVED\]** from ZS-U9 Theorem 5.1 PROVEN \+ sector identification a \= −1/X, b \= \+1/Z. The lemma is a re-expression, not a new derivation: it confirms that the sector parametrization is consistent with the Trinity Braiding output.

**§3. The Five Anomaly Conditions in (X, Z) Language**

Each subsection §3.1–§3.6 follows a uniform four-step structure: (i) statement of the SM arithmetic from ZS-U9 §7 PROVEN; (ii) reformulation in (X, Z) sector language; (iii) identification of the underlying structural identity; (iv) status declaration including Gap G2 dependency where applicable.

**§3.1 Witten SU(2)⁴ Anomaly \[DERIVED-CONDITIONAL\]**

The discrete Witten anomaly π₄(SU(2)) \= ℤ₂ requires that the total number of LH SU(2)\_L doublets per generation be even. SM has 4: three quark doublets Q\_L (one per color) plus one lepton doublet L\_L. Three structural ingredients enter the V-E-F reduction:

**(i) \[PROVEN\]** D₃ ⊂ I\_h provides the SU(2)\_L doublet structure via the standard 2-dimensional representation of S₃ ≅ D₃ (ZS-M9 Table 3 PROVEN: irrep 3 → 1' ⊕ 2 under D₃; the 2-dim component is the SU(2)\_L doublet).

**(ii) \[PROVEN\]** The color count \= 3 is forced by three independent routes: (R1) ZS-F5 PROVEN gives X \= 3 from Cayley-Hamilton \+ j \= 1/2 recoupling; (R2) ZS-M9 Theorem 6.1 PROVEN gives 3 colors from 2 Z₅ charges via SU(3) fundamental; (R3) ZS-F0 §4.3 PROVEN gives 3 \= unique 3-dim real irrep of A₅ ⊂ SO(3) ⊂ SU(3).

**(iii) \[HYPOTHESIS strong, Gap G2\]** The specific identification of I-irrep 3 with LH fermions including L\_L (ZS-M9 Table 2). This component enables the lepton-doublet count \= 1 per generation but requires the Gap G2 assignment.

Under (iii), the LH SU(2) doublet content per generation decomposes as 3 (color quark doublets via Theorem 6.1) \+ 1 (lepton doublet via Table 2\) \= 4, which is even (Witten condition satisfied). The arithmetic 3 \+ 1 \= 4 is consistent with V-E-F structure but is not itself a V-E-F structural identity: the lepton-doublet count \= 1 requires the Table 2 assignment.

**\[STATUS: DERIVED-CONDITIONAL\]** on Gap G2 (ZS-M9 Table 2). When Gap G2 is upgraded to PROVEN (forthcoming ZS-M15 via Route (b) exhaustive falsification), the Witten cancellation will upgrade to DERIVED automatically.

**§3.2 \[SU(3)\]³ Color Anomaly (A1) \[DERIVED-CONDITIONAL\]**

The A1 \[SU(3)\]³ anomaly cancels because SM fermions transform vector-like under SU(3)\_c: each LH quark Q\_L (in fundamental 3\) is paired with a RH conjugate u\_R^c \+ d\_R^c (in 3̄), giving Tr(T^a {T^b, T^c})\_LH \= Tr(T^a {T^b, T^c})\_RH automatically (ZS-U9 §7 PROVEN, vector-like).

In Z-Spin V-E-F language, this vector-like cancellation has a concrete geometric origin. The adjoint of SU(3) decomposes under A₅ ⊂ SU(3) as 8\_adj \= 3 ⊕ 5 (ZS-F0 §4.3 PROVEN; verified by character inner product χ\_adj(g) \= χ\_3(g)² − 1 \= χ\_3(g) \+ χ\_5(g) at all five conjugacy classes of A₅). Since 3 is a real representation of A₅ (A₅ ⊂ SO(3) acts faithfully on ℝ³), the conjugate 3̄ equals 3 as A₅-representations. The two ZS-M9 Table 2 fermion irreps I-3 and I-3' both have dimension 3, satisfying dim(I-3) \= dim(I-3') and providing the matching multiplicities required for vector-like cancellation.

**\[STATUS: DERIVED-CONDITIONAL\]** on Gap G2. The dim equality dim(I-3) \= dim(I-3') \= 3 is a PROVEN consequence of A₅ representation theory; the assignment of these I-irreps to LH/RH fermions remains HYPOTHESIS strong (Table 2). Status upgrade follows ZS-M15.

**§3.3 \[SU(2)\]² × U(1)\_Y Anomaly (A2) — ★ Core Sector Identity \[DERIVED\]**

ZS-U9 §7 PROVEN gives the SM arithmetic:

A2 \= 6 · (1/6) \+ 2 · (−1/2) \= 1 − 1 \= 0

Reformulating in (X, Z) sector language: the sum of LH hypercharges weighted by SU(2) doublet content takes the form

Σ\_LH Y \= X · Z · Y\_Q \+ Z · Y\_L

where the prefactor X · Z counts the X-color × Z-doublet components of Q\_L (= 3 × 2 \= 6 components) and Z counts the SU(2)\_L components of L\_L (= 2 components). Substituting Y\_Q \= a \+ b \= −1/X \+ 1/Z and Y\_L \= −b \= −1/Z from Lemma 2.1:

Σ\_LH Y \= X · Z · (−1/X \+ 1/Z) \+ Z · (−1/Z) \= (−Z \+ X) − 1 \= X − Z − 1

**Theorem 3.1 (A2 Sector Identity, DERIVED).** Under the Z-Spin sector identification of Lemma 2.1, the A2 anomaly satisfies A2 \= X − Z − 1\. Therefore A2 \= 0 if and only if X − Z \= 1\.

For Z-Spin's locked (X, Z) \= (3, 2): X − Z \= 3 − 2 \= 1 ✓. The cancellation is verified at integer arithmetic without further computation.

**\[STATUS: DERIVED\]** within the sector identification. Gap G2 independent. The reformulation makes manifest that A2 cancellation is equivalent to the linear sector asymmetry X − Z \= 1\. Note that this does not assert that X − Z \= 1 causally produces the SM lepton family count \= 1; it is a numerical identity.

**§3.4 \[SU(3)\]² × U(1)\_Y Anomaly (A3) \[DERIVED, Redundant with A2\]**

ZS-U9 §7 PROVEN gives the SM arithmetic per color:

A3 \= 2 · Y\_Q − (Y\_u \+ Y\_d) \= 2 · (1/6) − \[(2/3) \+ (−1/3)\] \= 1/3 − 1/3 \= 0

Reformulating in (X, Z) sector language: Σ\_LH^{quark} Y \= Z · Y\_Q (sum over Z \= 2 SU(2) components per color) and Σ\_RH^{quark} Y \= Y\_u \+ Y\_d. Substituting Y\_Q \= −1/X \+ 1/Z, Y\_u \= \+2/X, Y\_d \= −1/X (consistent with Lemma 2.1):

Σ\_LH^{quark} Y \= Z · (−1/X \+ 1/Z) \= −Z/X \+ 1 \= (X − Z)/X

Σ\_RH^{quark} Y \= (2/X) \+ (−1/X) \= 1/X

A3 \= (X − Z)/X − 1/X \= (X − Z − 1)/X \= A2/X

**Theorem 3.2 (A3-A2 Redundancy, DERIVED).** Under the sector identification, A3 \= A2/X. For X ≠ 0, A3 \= 0 if and only if A2 \= 0\. Therefore A3 provides no new constraint on (X, Z) beyond A2.

**\[STATUS: DERIVED\]** Gap G2 independent. The A3-A2 redundancy under SU(5) embedding is a known consequence of standard SU(5) representation theory (Weinberg, vol. II); the Z-Spin contribution is the explicit (X, Z) form A3 \= A2/X.

**§3.5 \[U(1)\_Y\]³ Cubic Anomaly (A4) — ★★ Novel Factorization \[DERIVED\]**

ZS-U9 §7 PROVEN gives the SM arithmetic at integer precision:

Σ\_LH Y³ \= 6 · (1/6)³ \+ 2 · (−1/2)³ \= 1/36 − 1/4 \= −2/9

Σ\_RH Y³ \= 3 · (2/3)³ \+ 3 · (−1/3)³ \+ (−1)³ \+ 0³ \= 24/27 − 3/27 − 1 \= −2/9

A4 \= (−2/9) − (−2/9) \= 0

In the "all LH" convention (using charge conjugates for RH fields, with Y³ being odd under Y → −Y), A4 equals Tr(Y³) over the full SU(5) matter content 5̄ \+ 10 \+ 1 of one generation, which vanishes by the cubic invariant of the SU(5) Cartan.

Reformulating in (X, Z) sector language using Y \= diag(a, a, a, b, b) on 5 with a \= −1/X, b \= \+1/Z, and applying Tr(Y³) over 5̄ \+ 10 \+ 1 with the SU(5) branching multiplicities:

Tr(Y³)|\_{5̄} \= −(X · a³ \+ Z · b³) \= −(−1/X² \+ 1/Z²) \= 1/X² − 1/Z²

Tr(Y³)|\_{10} \= X · Z · (a \+ b)³ \+ 4X(X−1) · a³ \+ 4Z(Z−1) · b³

Combining over the common denominator (X · Z)² and simplifying yields a polynomial in (X, Z) which, by SymPy verification at machine precision, factors algebraically:

**Theorem 3.3 (A4 Cubic Factorization, DERIVED).** Under the sector identification of Lemma 2.1, the \[U(1)\_Y\]³ cubic anomaly admits the factored form

A4(X, Z) \= (X − Z) · (X \+ Z) · (X \+ Z − 5\) / (X · Z)²

valid for all positive integer (X, Z). At (X, Z) \= (3, 2): A4 \= 1 · 5 · 0 / 36 \= 0, with the (X \+ Z − 5\) factor vanishing.

**Three structural factors.** The numerator (X − Z)(X \+ Z)(X \+ Z − 5\) decomposes into three polynomial factors with distinct meanings: (X − Z) is the sector asymmetry factor (vanishing iff X \= Z); (X \+ Z) is always strictly positive for physical sector dimensions; (X \+ Z − 5\) is the SU(5) fundamental dimension factor — see Theorem 3.4 below for the dual derivation.

**Theorem 3.4 (Dual Derivation of X \+ Z \= 5, DERIVED).** The factor (X \+ Z − 5\) of Theorem 3.3 admits two independent PROVEN derivations:

**Route A (Polyhedral):** From ZS-F5 PROVEN sector decomposition Q \= X \+ Y \+ Z \= 11 with Y \= 6, we obtain X \+ Z \= Q − Y \= 11 − 6 \= 5\.

**Route B (Gauge-theoretic):** From ZS-M9 §5 PROVEN McKay chain Z₅ ⊂ SU(2) → 5-cycle \= Â₄ extended Dynkin → SU(5) Lie algebra (after removing the affine node), the SU(5) fundamental representation has dimension 5, and the Cartan Y \= diag(a, a, a, b, b) splits into 3 color slots \+ 2 weak slots \= X \+ Z \= 5\.

Both routes are established independently in the Z-Spin corpus and arrive at the same value 5 via distinct mechanisms (polyhedral sector counting vs. McKay node counting). The numerical equality is therefore not coincidence but reflects a deeper structural alignment between Z-Spin's polyhedral foundation and the SU(5) Lie-algebraic embedding (ZS-M9 §10 Coset Structure Table 7 PROVEN provides additional related identities including |I\_h/T\_d| \= 5).

**\[STATUS: DERIVED\]** Gap G2 independent. The factorization is a Sympy-verified algebraic identity at machine precision. The dual derivation of (X \+ Z − 5\) via two independent PROVEN routes elevates this from algebraic coincidence to structural theorem.

**§3.6 Mixed Gauge-Gravitational Anomaly (A5) \[DERIVED\]**

ZS-U9 §7 PROVEN: A5 \= Σ\_LH Y − Σ\_RH Y \= 0, equivalently Tr(Y) \= 0 over the full SM fermion content. In the "all LH" convention this is automatic from the SU(5) Cartan traceless condition.

In (X, Z) sector language, A5 reduces to the same balance equation as in §2.2:

A5 ↔ Tr(Y) \= X · a \+ Z · b \= −1 \+ 1 \= 0

Multiple equivalent derivation routes exist for A5 \= 0: (Route α, 1-step) Y ∈ su(5) ⟹ Tr(Y) \= 0 (standard Lie algebra); (Route β, 2-step) sector identification (a, b) \= (−1/X, \+1/Z) ⟹ X · a \+ Z · b \= 0 (the present formulation); (Route γ, 4-step) McKay shortcut Z₅ → Â₄ → SU(5) → traceless (skipping topological prelude); (Route δ) Yukawa neutrality at every Yukawa vertex (ZS-U9 §4 Theorem 4.1 PROVEN). The traditional 7-step narrative chain S² → I\_h → A₅ → Z₅ → McKay → SU(5) → Tr(Y) \= 0 is one consistent path among multiple equivalent routes; it is not the unique proof.

**\[STATUS: DERIVED\]** via multiple equivalent routes. Gap G2 indirect (the assignment of which I-irreps carry which Y values requires Table 2, but the traceless cancellation itself is automatic once the SU(5) Cartan structure is in place).

**§4. Joint Uniqueness Theorem**

**§4.1 Theorem 4.1 (Joint A2 ∧ A4 Partition Uniqueness)**

**Theorem 4.1 (Joint Uniqueness, DERIVED).** Among the 45 positive integer partitions (X, Y, Z) of Q \= 11 with all three parts ≥ 1, exactly one partition satisfies both the A2 sector identity (X − Z \= 1, Theorem 3.1) and the A4 cubic identity in non-degenerate form (X \+ Z \= 5, the third factor of Theorem 3.3, excluding the degenerate X \= Z branch). That unique partition is

(X, Y, Z) \= (3, 6, 2\)

which matches the ZS-F5 PROVEN sector values exactly.

**Proof.** By direct enumeration: the 45 partitions are listed in Appendix B. The 4 partitions satisfying A2 (X − Z \= 1\) are {(2, 8, 1), (3, 6, 2), (4, 4, 3), (5, 2, 4)}. The 4 partitions satisfying A4 in non-degenerate form (X \+ Z \= 5, X ≠ Z) are {(1, 6, 4), (2, 6, 3), (3, 6, 2), (4, 6, 1)}. The intersection has cardinality 1: {(3, 6, 2)}. The linear system X − Z \= 1, X \+ Z \= 5 has the unique solution (X, Z) \= (3, 2\) by elementary algebra (2X \= 6, 2Z \= 4). □

**§4.2 Structural Significance**

Theorem 4.1 establishes that the joint A2 ∧ A4 conditions function as a powerful internal consistency check between Z-Spin's polyhedral axioms and the SM anomaly structure. The partition (3, 6, 2\) is forced by ZS-F5 PROVEN (Cayley-Hamilton recoupling) and ZS-M3 Theorem 5.1 PROVEN (j \= 1/2 uniqueness) before any anomaly analysis is performed; it is also the unique partition selected by the joint A2 ∧ A4 system. The convergence is not a derivation — Z-Spin does not pick (3, 6, 2\) by anomaly minimization — but a structural alignment that confirms the Trinity Braiding Theorem's automatic 5/5 anomaly cancellation (ZS-U9 §7 PROVEN) at the level of partition selectivity.

**§4.3 The Four Structural Identity Groups**

Combining the results of §3, the five SM anomaly conditions plus Witten reduce in Z-Spin sector language to four structural identity groups:

**Table 4.1. Four structural identity groups for SM anomaly cancellation in Z-Spin language.**

| Group | Sector identity | Anomalies | Gap G2 | ZS-S11 § |
| ----- | ----- | ----- | ----- | ----- |
| **SU(5) Linear** | X − Z \= 1 (or X·a \+ Z·b \= 0\) | A2, A3, A5 | independent | §3.3, §3.4, §3.6 |
| **SU(5) Cubic** | (X \+ Z − 5\) factor | A4 | independent | §3.5 |
| **A₅ Real Rep** | 8\_adj \= 3 ⊕ 5; dim(3) \= dim(3') | A1 | dependent | §3.2 |
| **Z₂ Seam Topology** | dim(Z) \= 2; D₃ doublet | Witten | partial dep. | §3.1 |

This four-group classification is the principal organizational contribution of ZS-S11. The standard SM literature treats the five anomaly conditions as separate constraints; the present reformulation reveals that they descend from at most four distinct structural identities in Z-Spin's polyhedral V-E-F language. Two of the four groups (SU(5) Linear and SU(5) Cubic, jointly covering A2/A3/A4/A5) are Gap G2 independent and yield the joint uniqueness of Theorem 4.1; the remaining two (A₅ Real Rep for A1, Z₂ Seam Topology for Witten) require the ZS-M9 Table 2 assignment (HYPOTHESIS strong) and thus carry Gap G2 dependency.

**§5. Falsification Gates**

Ten falsification gates are pre-registered for ZS-S11. All gates currently PASS at the verification level; experimental gates are in the upstream ZS-U9 / ZS-S2 / ZS-S1 papers.

**Table 5.1. Pre-registered falsification gates for ZS-S11 v1.0.**

| Gate | Condition (FAIL means) | Type | Status |
| ----- | ----- | ----- | ----- |
| **F-S11.1** | A4(X, Z) does not factor as (X−Z)(X+Z)(X+Z−5)/(XZ)² | Mathematical | **PASS (Sympy)** |
| **F-S11.2** | Joint A2 ∧ A4 has more than 1 solution in partitions of Q=11 | Mathematical | **PASS (= 1\)** |
| **F-S11.3** | Joint solution from F-S11.2 differs from ZS-F5 PROVEN (3, 6, 2\) | Cross-paper | **PASS** |
| **F-S11.4** | A4 sector identity contradicts ZS-U9 §7 arithmetic | Cross-paper | **PASS** |
| **F-S11.5** | Sector Cartan a \= −1/X, b \= \+1/Z fails to reproduce Trinity Y values | Internal | **PASS** |
| **F-S11.6** | Route A and Route B give different values for X \+ Z (Theorem 3.4) | Cross-paper | **PASS (both \= 5\)** |
| **F-S11.7** | Joint A2 ∧ A4 partition probability \> 50% at Q \= 11 | Anti-numerology | **PASS (1/45 \= 2.2%)** |
| **F-S11.8** | ZS-M9 Table 7 cosets fail |G/H| identities (e.g., |I\_h/T\_d| ≠ 5\) | Cross-paper | **PASS (all 6 OK)** |
| **F-S11.9** | A3 \= A2/X redundancy fails to match ZS-U9 §7 A3 arithmetic | Internal | **PASS** |
| **F-S11.10** | MC selectivity P(A2 ∧ A4) deviates from theoretical 1/100 by \> 5σ at N \= 500k | Anti-numerology | **PASS (0.0100 vs 0.01)** |

**§6. Anti-Numerology Monte Carlo**

**§6.1 Three-Basket Design**

The anti-numerology assessment uses three independent baskets, each with N \= 500,000 samples, to test the partition selectivity of (X, Z) \= (3, 2\) under joint A2 ∧ A4 constraints from different angles.

**Table 6.1. Three-basket Monte Carlo results (N \= 500,000 per basket).**

| Basket | Sampling space | P(A2) | P(A4) | P(A2 ∧ A4) |
| ----- | ----- | ----- | ----- | ----- |
| **Basket 1** | (X, Z) ∈ \[1, 10\]² independent | 0.0904 | 0.0397 | 0.0100 |
| **Basket 2** | Q \= 11 partition restriction | 4/45 \= 0.0889 | 9/45 \= 0.2000 | 1/45 \= 0.0222 |
| **Basket 3** | Q → ∞ asymptotic (numerical) | \~ 2/Q | \~ 2/Q | \~ 2/Q² |

**§6.2 Selectivity Assessment**

At Z-Spin's locked Q \= 11, the joint A2 ∧ A4 selectivity is P(both | Q \= 11\) \= 1/45 ≈ 2.2%. This passes the standard 5% anti-numerology threshold but does not pass a stricter 1% threshold. The asymptotic behavior P(both | Q) \~ 2/Q² confirms genuine selectivity — at Q \= 100 the probability drops to \~ 2 × 10⁻⁴, indicating that the joint constraint is not trivially satisfiable for arbitrary register sizes.

**§6.3 The Crucial Caveat — Forcing vs. Discovery**

The 1/45 partition selectivity is not the relevant measure of Z-Spin's anti-numerology strength. Z-Spin's (X, Y, Z) \= (3, 6, 2\) is forced by independent axioms (ZS-F5 PROVEN, ZS-M3 Theorem 5.1 PROVEN) before any anomaly conditions are checked. The anomaly cancellation is therefore a consistency check, not a probabilistic discovery.

The proper anti-numerology question is whether a different polyhedral framework could give a different (X, Y, Z). The answer is no: ZS-F5 \+ ZS-M3 uniquely select (2, 3, 6). The genuine strength of the anti-numerology argument therefore comes from cross-verification across multiple independent identities — A2 (linear sector asymmetry) \+ A4 (cubic SU(5) Cartan) \+ ZS-F5 (recoupling) \+ ZS-M3 (j \= 1/2) — all converging on the same (X, Z) \= (3, 2). Each constraint is established from different axioms; their joint consistency at the unique partition (3, 6, 2\) is the meaningful structural strength.

**§7. Non-Claims (Overreach Prevention)**

Eight non-claims are explicitly registered to prevent overreach in interpreting ZS-S11's results.

**NC-S11.1: Does NOT derive Y values.**  
ZS-S11 inherits SM hypercharges Y\_Q \= \+1/6 etc. from ZS-U9 Trinity Braiding (DERIVED). It does not provide an independent first-principles derivation of these values.

**NC-S11.2: Does NOT close Gap G2.**  
ZS-M9 Table 2 (LH/RH ↔ I-irrep 3/3' etc.) remains HYPOTHESIS strong. The §3.1 Witten and §3.2 A1 reductions in ZS-S11 require Table 2 for full V-E-F reduction; they do not upgrade Table 2's epistemic status. Closure is the subject of forthcoming ZS-M15 (Falsification-Based Upgrade of ZS-M9 Table 2 via Route (b) of ZS-U9 §8.2).

**NC-S11.3: Does NOT claim (X \+ Z − 5\) is causal for SU(5).**  
The factor (X \+ Z − 5\) in Theorem 3.3 admits dual PROVEN derivation (Theorem 3.4), but the SU(5) Lie algebra structure (specifically rank 4, fundamental dim 5\) precedes the Z-Spin (X, Z) sector identification. The numerical alignment X \+ Z \= 5 \= dim(SU(5) fund) is structurally meaningful but not causal.

**NC-S11.4: Does NOT claim Witten Route C closes Gap G2.**  
The 3 \+ 1 \= 4 doublet decomposition is partially V-E-F reducible (color \= 3 PROVEN by three independent routes) but the lepton family count \= 1 per generation depends on the ZS-M9 Table 2 assignment (Gap G2). Closing Witten via V-E-F requires upgrading Table 2 first (deferred to ZS-M15).

**NC-S11.5: Does NOT claim the 7-step A5 chain is unique.**  
Multiple equivalent routes derive Tr(Y) \= 0 (Routes α 1-step, β 2-step, γ 4-step, δ Yukawa neutrality). The traditional narrative chain S² → I\_h → A₅ → Z₅ → McKay → SU(5) → Tr(Y) \= 0 is one consistent path among several; it is not the unique proof. ZS-S11 does not assert this chain's necessity.

**NC-S11.6: Does NOT claim X − Z \= 1 causes the SM lepton family count.**  
The numerical coincidence X − Z \= 1 \= (number of LH lepton families per generation) is a consistency match, not a causal derivation. Z-Spin does not derive lepton family count from sector asymmetry.

**NC-S11.7: Does NOT introduce new free parameters.**  
All ZS-S11 inputs (A \= 35/437, Q \= 11, X, Y, Z, McKay structure, SU(5) Cartan, Trinity Y values) are LOCKED from prior papers. ZS-S11 contains zero new free parameters.

**NC-S11.8: Does NOT predict new physical observables.**  
ZS-S11 is a structural reformulation of an already PROVEN result (ZS-U9 §7 anomaly cancellation). All numerical predictions remain in upstream papers (ZS-S1 gauge couplings, ZS-S2 neutrino masses, ZS-U9 hypercharges, etc.).

**§8. Conclusion**

**§8.1 Three Achievements**

ZS-S11 v1.0 establishes three new structural results within the Z-Spin Cosmology framework, all built on the PROVEN foundation of ZS-U9 §7 (5/5 SM anomaly cancellation at integer arithmetic):

(i) A4 Cubic Factorization (Theorem 3.3): The \[U(1)\_Y\]³ cubic anomaly admits the algebraic factorization A4(X, Z) \= (X − Z)(X \+ Z)(X \+ Z − 5)/(X·Z)² in Z-Spin sector language, with three structural factors carrying distinct meanings.

(ii) Joint Partition Uniqueness (Theorem 4.1): The joint A2 ∧ A4 conditions select (X, Y, Z) \= (3, 6, 2\) uniquely among the 45 positive integer partitions of Q \= 11, matching the ZS-F5 PROVEN sector values exactly.

(iii) Four-Group Classification (Table 4.1): The five SM anomaly conditions plus the discrete Witten anomaly reduce in Z-Spin V-E-F language to four structural identity groups — SU(5) Linear (A2/A3/A5), SU(5) Cubic (A4), A₅ Real Representation (A1), and Z₂ Seam Topology (Witten) — clarifying the structural origin of anomaly cancellation in Z-Spin's polyhedral foundation.

**§8.2 What This Means and What It Does Not Mean**

ZS-S11 demonstrates that SM anomaly freedom, already established in ZS-U9 §7, can be re-expressed in Z-Spin sector language with significantly cleaner algebraic structure. The reformulation reveals a powerful consistency between SM anomaly axioms and Z-Spin's polyhedral axioms (ZS-F5, ZS-M3): both independently select (X, Y, Z) \= (3, 6, 2\) as the unique solution. This is a structural alignment, not a new derivation. ZS-S11 does not claim that Z-Spin predicts anomaly cancellation a priori; the prediction is provided by the ZS-U9 Trinity Braiding Theorem (DERIVED conditional on Gap G2).

**§8.3 Future Work**

Two principal directions for future work follow from ZS-S11's findings:

**(a) ZS-M15 (Falsification-Based Upgrade of ZS-M9 Table 2).** Following Route (b) of ZS-U9 §8.2's Gap G2 closure plan, an exhaustive falsification of alternative I-irrep ↔ SM field assignments can extend the existing five lines of evidence (chirality Δ, A₄ content, D₅ content, gauge dimension saturation PROVEN at ZS-M9 §3.2, branching rules) to a sixth line via systematic alternative elimination. Combined with ZS-M11 §9.5.2 Uniqueness Corollary PROVEN (ν\_R ↔ irrep 1 is the unique Yukawa-vanishing assignment), this can plausibly upgrade ZS-M9 Table 2 from HYPOTHESIS strong to DERIVED-CONDITIONAL. Full PROVEN status requires complementary action-level potential minimization (Route (a)), deferred to subsequent work.

**(b) Generalization to higher SU(N).** The (X − Z)(X \+ Z)(X \+ Z − 5\) factorization of A4 raises the question of whether analogous cubic factorizations exist for hypothetical SU(N) extensions with N \> 5\. Such generalizations would be structural (not predictive) and would clarify whether the (X \+ Z − 5\) factor is uniquely tied to SU(5) or has broader applicability.

**(c) Strengthening Witten Route C.** Once Gap G2 closure (via ZS-M15 or successor) provides the I-irrep 3 ⊗ gauge sector tensor product structure for LH fermions, the 3 \+ 1 \= 4 doublet decomposition of Witten anomaly cancellation may admit a fully V-E-F reducible derivation. This is contingent on Gap G2 closure and is not addressed in ZS-S11.

**§9. Acknowledgements & Code Availability**

Code Availability: The ZS-S11 verification suite (zs\_s11\_verify\_v1\_0.py, 30/30 PASS) is publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts. The script reproduces all six categories of tests: anomaly arithmetic (Category A), sector identity theorems (Category B), A4 cubic factorization (Category C), joint uniqueness theorem (Category D), cross-paper consistency (Category E), and anti-numerology Monte Carlo (Category F).

Acknowledgements: This paper was developed through five rounds of progressive falsification with self-correction (Q1 dual derivation of X \+ Z \= 5, Q2 parallel-gauge-universe analysis of A4 zeros, Q3 critical examination of Witten Route C revealing partial V-E-F reducibility, Q4 evaluation of A5 7-step chain as contingent narrative, Q5 honest assessment of anti-numerology selectivity scaling). The author acknowledges multi-AI collaborative review (Claude, Anthropic) for the (X, Z) sector reformulation methodology and for the systematic identification and correction of overreach claims throughout the development process. All physical interpretations and final claims are the sole responsibility of the author.

**§10. Appendix A: Sympy Verification of A4 Factorization**

The algebraic identity A4(X, Z) \= (X − Z)(X \+ Z)(X \+ Z − 5)/(X · Z)² of Theorem 3.3 is verified by symbolic computation. The numerator polynomial:

N(X, Z) \= (5 − 4X) · Z² \+ (4Z − 5\) · X² \+ (X − Z)³

is obtained by substituting a \= −1/X, b \= \+1/Z into Tr(Y³)|\_{5̄ \+ 10 \+ 1}, multiplying through by (X · Z)², and collecting terms. SymPy's factor() function returns:

N(X, Z) \= (X − Z)(X \+ Z)(X \+ Z − 5\)

verified at machine precision. Brute-force enumeration in \[1, 6\]² with X ≠ Z yields zeros at {(1, 4), (2, 3), (3, 2), (4, 1)}, all sharing the X \+ Z \= 5 factor. The complete verification script zs\_s11\_verify\_v1\_0.py executes Categories A through F (30 total tests) and exits with code 0 (success) when all tests PASS.

**§11. Appendix B: Q \= 11 Partition Enumeration**

All 45 positive integer partitions (X, Y, Z) of Q \= 11 with X, Y, Z ≥ 1, with A2 (X − Z \= 1\) and A4 (X \+ Z \= 5 or X \= Z) satisfaction marked.

**Table B.1. Complete partition enumeration (45 partitions).**

| (X, Y, Z) | X − Z | X \+ Z | A2 ? | A4 ? |
| :---: | :---: | :---: | :---: | :---: |
| (1, 9, 1\) | 0 | 2 |  | ✓ |
| (1, 8, 2\) | \-1 | 3 |  |  |
| (1, 7, 3\) | \-2 | 4 |  |  |
| (1, 6, 4\) | \-3 | 5 |  | ✓ |
| (1, 5, 5\) | \-4 | 6 |  |  |
| (1, 4, 6\) | \-5 | 7 |  |  |
| (1, 3, 7\) | \-6 | 8 |  |  |
| (1, 2, 8\) | \-7 | 9 |  |  |
| (1, 1, 9\) | \-8 | 10 |  |  |
| (2, 8, 1\) | 1 | 3 | ✓ |  |
| (2, 7, 2\) | 0 | 4 |  | ✓ |
| (2, 6, 3\) | \-1 | 5 |  | ✓ |
| (2, 5, 4\) | \-2 | 6 |  |  |
| (2, 4, 5\) | \-3 | 7 |  |  |
| (2, 3, 6\) | \-4 | 8 |  |  |
| (2, 2, 7\) | \-5 | 9 |  |  |
| (2, 1, 8\) | \-6 | 10 |  |  |
| (3, 7, 1\) | 2 | 4 |  |  |
| (3, 6, 2\) | 1 | 5 | ✓ | ✓ |
| (3, 5, 3\) | 0 | 6 |  | ✓ |
| (3, 4, 4\) | \-1 | 7 |  |  |
| (3, 3, 5\) | \-2 | 8 |  |  |
| (3, 2, 6\) | \-3 | 9 |  |  |
| (3, 1, 7\) | \-4 | 10 |  |  |
| (4, 6, 1\) | 3 | 5 |  | ✓ |
| (4, 5, 2\) | 2 | 6 |  |  |
| (4, 4, 3\) | 1 | 7 | ✓ |  |
| (4, 3, 4\) | 0 | 8 |  | ✓ |
| (4, 2, 5\) | \-1 | 9 |  |  |
| (4, 1, 6\) | \-2 | 10 |  |  |
| (5, 5, 1\) | 4 | 6 |  |  |
| (5, 4, 2\) | 3 | 7 |  |  |
| (5, 3, 3\) | 2 | 8 |  |  |
| (5, 2, 4\) | 1 | 9 | ✓ |  |
| (5, 1, 5\) | 0 | 10 |  | ✓ |
| (6, 4, 1\) | 5 | 7 |  |  |
| (6, 3, 2\) | 4 | 8 |  |  |
| (6, 2, 3\) | 3 | 9 |  |  |
| (6, 1, 4\) | 2 | 10 |  |  |
| (7, 3, 1\) | 6 | 8 |  |  |
| (7, 2, 2\) | 5 | 9 |  |  |
| (7, 1, 3\) | 4 | 10 |  |  |
| (8, 2, 1\) | 7 | 9 |  |  |
| (8, 1, 2\) | 6 | 10 |  |  |
| (9, 1, 1\) | 8 | 10 |  |  |

Counts: A2 satisfied by 4 partitions; A4 satisfied by 9 partitions (4 with X \+ Z \= 5 and 5 with X \= Z degenerate); joint A2 ∧ A4 satisfied uniquely by (3, 6, 2).

**§12. Appendix C: Cross-Paper Consistency Audit**

ZS-S11 inherits inputs from five upstream papers. All cross-references are explicit and verified.

**Table C.1. Cross-paper consistency audit for ZS-S11 v1.0.**

| Paper | Inherited result | Status | Used in ZS-S11 |
| ----- | ----- | ----- | ----- |
| ZS-F5 v1.0 | Q \= 11; (Z, X, Y) \= (2, 3, 6); j \= 1/2 recoupling | **PROVEN** | §1.3, §2.1, §4.1 |
| ZS-M3 v1.0 | Theorem 5.1: dim(Inv) \= 2 \= Z (j \= 1/2 unique) | **PROVEN** | §1.3, §3.1 |
| ZS-F0 v1.0 | §4.3: 8\_adj(SU(3)) \= 3 ⊕ 5 under A₅ | **PROVEN** | §3.1, §3.2 |
| ZS-M9 v1.0 | §5 McKay Z₅→Â₄→SU(5); §3.2 dim(3⊗4) \= 12; §10 cosets | **PROVEN** | §3.5, §4.3, Theorem 3.4 |
| ZS-U9 v1.0 | §5.1 Cartan Y; §6 Trinity Y values; §7 5/5 anomaly PASS | **PROVEN/DERIVED** | §1.1, §2.1, §3.3–§3.6 |

**§13. References**

\[1\] K. Kang, "Z-Spin Cosmology Foundations," ZS-F5 v1.0 (2026). \[Q \= 11 sector decomposition\]  
\[2\] K. Kang, "Regge–Holonomy, Immirzi & Z-Telomere," ZS-M3 v1.0 (2026). \[j \= 1/2 uniqueness Theorem 5.1\]  
\[3\] K. Kang, "Polyhedral Hodge Decomposition," ZS-F0 v1.0 (2026). \[§4.3: 8\_adj \= 3 ⊕ 5 under A₅\]  
\[4\] K. Kang, "McKay Bridge: Z₅ → SU(5) → Standard Model," ZS-M9 v1.0 (2026). \[Tables 2, 3, 4, 7\]  
\[5\] K. Kang, "Yukawa Tensor Uniqueness," ZS-M10 v1.0 (2026).  
\[6\] K. Kang, "Yukawa Mass Spectrum," ZS-M11 v1.0 (2026). \[§9.5.2 Uniqueness Corollary\]  
\[7\] K. Kang, "Hypercharge Trinity," ZS-U9 v1.0 (2026). \[§5.1 Cartan, §6 Trinity, §7 5/5 anomaly, §8.2 Gap G2\]  
\[8\] K. Kang, "Spectral-to-β Bridge," ZS-S1 v1.0 (2026).  
\[9\] K. Kang, "Geometric Impedance A \= 35/437," ZS-F2 v1.0 (2026).  
\[10\] S. Weinberg, The Quantum Theory of Fields, Vol. II: Modern Applications (Cambridge University Press, 1996), Chapter 22\.  
\[11\] M. E. Peskin and D. V. Schroeder, An Introduction to Quantum Field Theory (Westview Press, 1995), §20.  
\[12\] E. Witten, "An SU(2) Anomaly," Phys. Lett. B 117, 324 (1982).  
\[13\] H. Georgi and S. L. Glashow, "Unity of All Elementary Particle Forces," Phys. Rev. Lett. 32, 438 (1974).  
\[14\] J. McKay, "Graphs, Singularities, and Finite Groups," Proc. Symp. Pure Math. 37, 183 (1980).  
\[15\] P. Langacker, "Grand Unified Theories and Proton Decay," Phys. Rep. 72, 185 (1981).  
\[16\] P. H. Frampton, S. L. Glashow, and T. Yanagida, "Cosmological Sign of Neutrino CP Violation," Phys. Lett. B 548, 119 (2002).

**§14. Version History**

**v1.0 (April 2026):** Initial public release. Establishes Theorem 3.1 (A2 sector identity X − Z \= 1), Theorem 3.2 (A3 \= A2/X redundancy), Theorem 3.3 (A4 cubic factorization (X − Z)(X \+ Z)(X \+ Z − 5)/(X · Z)²), Theorem 3.4 (dual derivation of X \+ Z \= 5), Theorem 4.1 (joint A2 ∧ A4 partition uniqueness selecting (3, 6, 2\) among 45 partitions of Q \= 11). Four-group structural classification of SM anomaly conditions in Z-Spin sector language. Verification: 30/30 PASS (Categories A–F). Anti-numerology Monte Carlo with three baskets (independent (X, Z), Q \= 11 partition, Q → ∞ asymptotic). Eight non-claims registered. Ten falsification gates pre-registered. Forward reference to ZS-M15 (Gap G2 closure via Route (b) exhaustive falsification). Consolidated from internal Z-Spin Collaboration research notes including five rounds of progressive self-correction (Q1–Q5 exploration, March–April 2026).  
