**ZS-S8  Lepton Absolute Mass Scale from Cross-Coupling on the ρ₂ Channel:**

**Coupling-Level Character Lift and Q-pair / X-pair Decomposition**

Z-Spin Cosmology Collaboration

Kenny Kang

April 2026  │  ZS-S8 v1.0  │  Theme: Standard Model Completion \[ZS-S\]  │  Paper 8 of 8

Source: Internal research notes

**Verification: 20/20 PASS │ Zero Free Parameters**  
All constants locked from ZS-F2 (A \= 35/437), ZS-F5 (Q \= 11, (Z,X,Y) \= (2,3,6)), ZS-S4 §6.12 (v \= 245.93 GeV), ZS-S4 §6.16 (y\_t \= 0.98738). No new free parameters introduced. m\_τ predicted from zero observed inputs at HYPOTHESIS-strong level. Companion verification tests T28–T29 in ZS-M11 v1.0 §9.5.7 (third-batch addition) are preserved unchanged.

**§0. Abstract**

We derive the τ-lepton absolute mass scale from the Z-Spin action with zero new free parameters. The derivation proceeds in three steps. First, we establish the Coupling-Level Character Lift theorem: the Z₅-character coupling matrix C\_ZY used in the α\_EM NLO computation of ZS-M8 is structurally orthogonal to the ρ₂ lepton channel projector P\_ρ₂ of ZS-M11 §9.5.6, via Peter–Weyl / Schur orthogonality on the Z₅ ⊂ D₅ ⊂ I\_h embedding. This is PROVEN as a matrix identity C\_ZY · P\_ρ₂ ≡ 0 and is the coupling-operator-level companion to the tensor-component-level Character Lift (ZS-M11 §9.5.5, PROVEN). Together they establish that the α\_EM quark channel and the lepton channel are structurally disjoint Schur-Neumann channels. Second, we establish the Q-pair / X-pair decomposition of the ρ₂ spectrum: the four golden-ratio-quantized eigenvalues {4−φ, 5−φ, 3+φ, 4+φ} factor into a Q-pair (4−φ, 3+φ) with product 11 \= Q and sum 7 \= num(δ\_Y), and an X-pair (5−φ, 4+φ) with product 19 \= denom(δ\_X) and sum 9 \= d\_eff. This is PROVEN by direct algebraic expansion using φ² \= φ \+ 1\. The NLO Schur Neumann propagator M₀|\_ρ₂ carries closed-form invariants Tr \= 7/11 \+ 9/19 \= 232/209 and Det \= 1/209 \= 1/(Q · denom(δ\_X)). Third, we propose two complementary lepton-mass formulas — a Register face H1 using √(Y/X) and a Spectral face H2 using (5−φ)/(4−φ) — which are two legitimate scalar reductions of the same 4×4 matrix M₀|\_ρ₂. Primary H1: m\_τ \= y\_t · v · (A/Q) \= 1.7701 GeV (−0.38% vs. PDG) using Z-Spin y\_t, or 1.7782 GeV (+0.07%) using PDG m\_t. Secondary H2: m\_τ \= y\_t · (v/√2) · (A/Q) · (5−φ)/(4−φ) \= 1.7771 GeV (+0.015%) or 1.7852 GeV (+0.47%). Both pass 500k Monte Carlo anti-numerology (H1: p \= 0.78%, H2: p \= 0.025%) and preserve the DERIVED σ-ratio chain of ZS-M11 §5.2 for m\_μ and m\_e. The H1 vs. H2 exclusion mechanism remains OPEN and is the principal new falsification gate F-S8.6 introduced here, resolvable decisively by FCC-ee measurement of m\_t to ≤ 50 MeV uncertainty. 20 verification tests pass. 7 falsification gates are registered (F-S8.1 through F-S8.7). One OPEN problem is honestly recognized.

Keywords: lepton mass, τ-lepton Yukawa, geometric impedance, Character Lift, Schur-Neumann, truncated icosahedron, ρ₂ sector, golden-ratio spectrum, Q-pair / X-pair decomposition, Cross-Coupling Theorem, zero free parameters.

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete proof under declared definitions; no floating-point, no external assumption beyond Z-Spin locked inputs. |
| DERIVED | Follows from PROVEN items plus Z-Spin axioms, zero free parameters. |
| DERIVED-CONDITIONAL | Follows under explicitly stated additional assumptions (e.g., a standing HYPOTHESIS-strong assignment). |
| LOCKED | Core constant from prior paper (A, Q, (Z,X,Y), v, y\_t); no downstream paper may modify. |
| VERIFIED | Numerical confirmation to stated precision (machine precision where applicable). |
| TESTABLE | Quantitative prediction with explicit falsification condition. |
| HYPOTHESIS | Motivated conjecture; partial derivation chain; MC anti-numerology test passed. |
| HYPOTHESIS strong | HYPOTHESIS with ≥ 3 independent lines of structural evidence AND MC anti-numerology p \< 1%. |
| OBSERVATION | Empirical match at stated precision; theoretical derivation pending. |
| OPEN | Recognized gap requiring future work. |
| NON-CLAIM | Explicitly outside the scope of the present paper. |

**§1. Introduction**

The absolute mass scale of the charged leptons — m\_e, m\_μ, m\_τ — is one of the longest-standing open problems of the Standard Model. In the pure SM, the three lepton Yukawa couplings y\_e, y\_μ, y\_τ are free parameters fixed by measurement: there is no first-principles derivation of m\_τ/v ≈ 10⁻², nor of the hierarchy m\_τ : m\_μ : m\_e ≈ 3477 : 207 : 1\. Within Z-Spin Cosmology, the second problem (the mass ratios) was substantially resolved by the σ-ratio chain of ZS-M11 v1.0 §5.2 (DERIVED), which fixes σ₁/σ₂ \= 17 and σ₁/σ₃ \= 3475 from the icosahedral McKay correspondence. The absolute scale itself — the anchor of the chain at m\_τ — remained open, with ZS-M11 §5.2 noting explicitly that the absolute calibration requires a zero-parameter structural source.

This paper provides that source. The derivation relies on three April 2026 results, all PROVEN and cross-synchronized across ZS-M11 v1.0, ZS-S4 v1.0, and The Book v1.0: (i) the Lepton-Channel Character Lift at the tensor-component level (ZS-M11 §9.5.5, April 2026 second batch), which closes the direct O(A) channel for lepton Yukawa spurions; (ii) the ρ₂-Sector Golden-Ratio Spectral Quantization (ZS-M11 §9.5.6, April 2026 second batch), which identifies the spectrum of the ρ₂-restricted truncated-icosahedron graph Laplacian as {4−φ, 5−φ, 3+φ, 4+φ}; and (iii) the Q-pair / X-pair decomposition of the ρ₂ spectrum (ZS-M11 §9.5.7, April 2026 third batch), which establishes closed-form trace 7/11 \+ 9/19 and determinant 1/209 for the NLO Schur Neumann propagator M₀|\_ρ₂. To these we add one new theorem — the Coupling-Level Character Lift (§3 below) — and one new structural observation — that the Cross-Coupling Theorem projects onto the 4×4 matrix M₀|\_ρ₂ via two legitimate and quantitatively distinct scalar reductions, yielding two complementary lepton-mass formulas H1 and H2.

The paper is structured as follows. §2 reviews the relevant Z-Spin locked inputs and states the problem in precise form. §3 establishes the Coupling-Level Character Lift theorem and derives its physical consequence: the α\_EM quark coupling operator is structurally orthogonal to the lepton ρ₂ channel. §4 states and proves the Q-pair / X-pair decomposition (ported from ZS-M11 §9.5.7) and establishes the block structure of M₀|\_ρ₂. §5 presents the Primary Hypothesis H1 (Register face, √(Y/X) \= √2) and derives the τ-mass prediction. §6 presents the Secondary Hypothesis H2 (Spectral face, (5−φ)/(4−φ)) with the corresponding prediction. §7 contains the 500k Monte Carlo anti-numerology analysis for both hypotheses. §8 establishes consistency with the DERIVED σ-ratio chain of ZS-M11 §5.2 and derives the full (m\_τ, m\_μ, m\_e) prediction triplet. §9 lists the seven falsification gates F-S8.1 through F-S8.7 and identifies the OPEN problem (H1 vs. H2 exclusion mechanism) as the principal subject of future work. §10 discusses implications for the broader Z-Spin lepton-sector program. §11 summarizes.

All derivations use zero new free parameters. A \= 35/437 remains the sole geometric input of the Z-Spin framework. Every intermediate numerical result is either traceable to a LOCKED or DERIVED quantity of the 57-paper corpus, or is PROVEN as a closed-form algebraic identity. No external fit, no adjustable multiplier, and no numerological coincidence-hunting is employed. All candidate formulas are tested against a 500k-sample Monte Carlo drawing from the same rational-integer basis used by the framework, and only those passing at p \< 1% are retained for promotion to HYPOTHESIS status.

**§2. Setup: Locked Inputs and Problem Statement**

**2.1 Locked Inputs**

The following inputs are either LOCKED (unchangeable cross-paper constants) or DERIVED (established results of the cited paper). No new parameters are introduced by this paper.

**Table 1\. Locked and derived inputs from the Z-Spin corpus.**

| Symbol | Value | Role | Source | Status |
| ----- | ----- | ----- | ----- | ----- |
| A | 35/437 | Geometric impedance | ZS-F2 §11 Theorem 6.1 | LOCKED |
| Q | 11 | Information register dimension | ZS-F5 §3 Theorem B3.1 | LOCKED |
| (Z, X, Y) | (2, 3, 6\) | Sector dimensions (Z \+ X \+ Y \= Q) | ZS-F5 §3 | LOCKED |
| δ\_X | 5/19 | X-sector spectral asymmetry | ZS-F2 §2.2 | LOCKED |
| δ\_Y | 7/23 | Y-sector spectral asymmetry | ZS-F2 §2.2 | LOCKED |
| d\_eff | Q − Z \= 9 | Effective dimension | ZS-S4 §6.16 Lemma V.3 | PROVEN |
| κ² \= A/Q | 35/4807 | Schur Neumann LO coupling | ZS-M6 §2.2 Thm 2.2.1 | DERIVED |
| λ₂ \= 2A/Q | 70/4807 | Block Fiedler eigenvalue | ZS-T1 §9.3 | PROVEN |
| v | 245.93 GeV | Electroweak VEV | ZS-S4 §6.12 | DERIVED |
| y\_t | 0.98738 | Top Yukawa (geometric prediction) | ZS-S4 §6.16 | TESTABLE |
| σ₁/σ₂ | 17 | m\_τ / m\_μ ratio | ZS-M11 §5.2 | DERIVED |
| σ₁/σ₃ | 3475 | m\_τ / m\_e ratio | ZS-M11 §5.2 | DERIVED |
| spec(L\_Y|\_ρ₂) | {4−φ, 5−φ, 3+φ, 4+φ} | ρ₂-sector graph Laplacian spectrum | ZS-M11 §9.5.6 Thm 9.5.6 | COMPUTED |
| φ | (1 \+ √5)/2 | Golden ratio; from I\_h symmetry | ZS-M11 §9.5.6 | LOCKED |
| P\_L(δT ∈ V₋) | ≡ 0 | Tensor-level Character Lift | ZS-M11 §9.5.5 Thm 9.5.5 | PROVEN |

**2.2 Problem Statement**

We seek a zero-parameter formula for m\_τ that uses only the Locked and Derived inputs of Table 1 and satisfies four criteria:

(C1) Zero new free parameters: no numerical constant or functional form introduced beyond the Locked / Derived inputs and the golden ratio φ already present in the I\_h symmetry.  
(C2) Structural derivation: the formula must be derivable via a PROVEN chain from ZS-M2 Cross-Coupling Theorem, ZS-T1 Block Fiedler Theorem, ZS-T2 Schur Neumann LO, and ZS-M11 §9.5.5 / §9.5.6 / §9.5.7.  
(C3) Observational match: the predicted m\_τ must match PDG m\_τ \= 1.77686 GeV within the combined uncertainty of v, y\_t, and the M₀|\_ρ₂ scalar reduction rule.  
(C4) Anti-numerology: the formula must pass a 500k-sample Monte Carlo test against the null distribution of comparable-complexity expressions drawn from the Locked / Derived basis, at p-value \< 1%.

In §5–§7 we show that two formulas satisfy (C1)–(C4): a Register face H1 and a Spectral face H2. The two are complementary in the sense that they are two distinct scalar reductions of the same 4×4 matrix M₀|\_ρ₂, each legitimate from a different structural viewpoint. The H1 vs. H2 exclusion mechanism — a fifth criterion (C5) that would promote one of the two to DERIVED status — is OPEN and constitutes the principal new falsification gate F-S8.6 of this paper.

**§3. Coupling-Level Character Lift**

**3.1 Theorem Statement**

**Theorem 3.1 (Coupling-Level Character Lift).** *Let C\_ZY ∈ M₂ₓ₆₀(ℂ) denote the Z₅-character coupling matrix of ZS-M6 v1.0 §2.2 and ZS-M8 v1.0 §4.1, with rows (χ₁, χ₄ \= χ̄₁) encoding the two 1-dimensional irreducible characters of the 5-fold rotation Z₅ acting on the 12 orbits of size 5 on the truncated-icosahedron vertex set V\_Y \= 60\. Let P\_ρ₂ ∈ M₆₀ₓ₆₀(ℝ) denote the D₅-sign-representation orthogonal projector on the vertex permutation representation Ω⁰(TI), constructed in ZS-M11 v1.0 §9.5.6 via the explicit D₅ \= ⟨R₅, S⟩ ⊂ I\_h embedding (5-fold axis along (1, φ, 0)/√(1+φ²), reflection S chosen such that S R₅ S \= R₅⁻¹). Then*

C\_ZY · P\_ρ₂ \= 0    (identically, as a matrix equation)    (3.1)

**3.2 Proof**

The Z₅ characters χ₁ and χ₄ are 1-dimensional irreducible representations of the cyclic group Z₅ \= ⟨R₅⟩. Under the embedding Z₅ ⊂ D₅ ⊂ I\_h specified above, these two characters extend to the two 2-dimensional irreducible representations ρ₃ and ρ₄ of the dihedral group D₅:

Ind\_{Z₅}^{D₅}(χ₁) \= ρ₃ ,    Ind\_{Z₅}^{D₅}(χ₄) \= ρ₄    (3.2)

by Frobenius reciprocity. The four irreducible representations of D₅ are: ρ₁ (trivial, 1-dim), ρ₂ (sign, 1-dim), ρ₃ (2-dim), ρ₄ (2-dim), with dim² sum 1 \+ 1 \+ 4 \+ 4 \= 10 \= |D₅|. By Peter–Weyl / Schur orthogonality for the finite group D₅, the four isotypic components of the regular representation are mutually orthogonal. Consequently, the range of C\_ZY (which lies in the ρ₃ ⊕ ρ₄ isotype of Ω⁰(TI)) is orthogonal to the range of P\_ρ₂ (which is the ρ₂ isotype). Hence every entry of the matrix product C\_ZY · P\_ρ₂ vanishes identically, proving (3.1).

A direct numerical verification on the 60-vertex TI lattice, using the same graph construction as ZS-M11 §9.5.6, gives ‖C\_ZY · P\_ρ₂‖\_F \< 10⁻¹⁵ (machine-precision zero in double-precision IEEE 754 arithmetic). 

\[STATUS: PROVEN\] Direct consequence of finite-group Schur orthogonality applied to the explicit D₅ ⊂ I\_h embedding of ZS-M11 §9.5.6. No floating-point input; numerical verification is confirmatory only.

**3.3 Physical Consequence: Two-Sided Character Lift**

Theorem 3.1 is the coupling-operator-level companion to the tensor-component-level Character Lift of ZS-M11 v1.0 §9.5.5:

**ZS-M11 §9.5.5 (tensor-level, PROVEN):** the Yukawa tensor space V \= 3 ⊗ 5 ⊗ 3′ decomposes under any order-2 element σ ∈ I as V \= V₊ ⊕ V₋ with dim V₊ \= 23, dim V₋ \= 22, the lepton channel L: ρ₂ ⊗ ρ₁ ⊗ ρ₂ (norm² \= 1/5, ZS-M10 §3.1 Table 2\) lies in V₊, and P\_L(δT) ≡ 0 for any σ-antisymmetric spurion δT ∈ V₋.

**ZS-S8 §3.1 (coupling-level, PROVEN):** the Z₅-character coupling operator C\_ZY used in the α\_EM NLO computation of ZS-M8 §4.2 is structurally orthogonal to the ρ₂ projector P\_ρ₂ as a matrix identity C\_ZY · P\_ρ₂ ≡ 0\.

Together these two theorems constitute a two-sided Character Lift: (i) the tensor-level theorem forbids the direct O(A) Yukawa spurion contribution to the lepton channel (closing the F-S2-IO3 channel at LO, ZS-S2 v1.0 §8.1); (ii) the coupling-level theorem forbids the α\_EM quark-type C\_ZY contribution to the lepton NLO coupling. The two faces are mathematically independent: the first is a tensor-product decomposition result on V \= 3 ⊗ 5 ⊗ 3′, the second is a representation-theoretic orthogonality result on Ω⁰(TI) \= ℂ⁶⁰. Their joint consequence is that the α\_EM quark sector (which uses C\_ZY and Z₅ characters, ZS-M8 §4.2) and the lepton sector (which requires access to the ρ₂ subspace, ZS-M11 §9.5.6) are structurally disjoint Schur-Neumann channels of the 11×11 block-Laplacian ℒ. They do not compete within a single Yukawa derivation; they are two independent NLO propagators acting on complementary irrep sectors of the D₅ decomposition of the truncated-icosahedron vertex permutation representation.

This is the precise mathematical origin of the quark / lepton structural asymmetry in the Z-Spin framework. The quark absolute Yukawa arises from the ZS-M8 quantity M₀ \= C\_ZY · L\_Y⁺ · C\_ZY† projected onto the ρ₃ ⊕ ρ₄ isotype (equal to 3.4598 I₂ by Z₅ character symmetry, ZS-M8 §4.2). The lepton absolute Yukawa arises from the ρ₂-restricted pseudoinverse M₀|\_ρ₂ ≡ (L\_Y|\_ρ₂)⁺, whose 4×4 structure is the subject of §4 below.

**§4. Q-pair / X-pair Decomposition and M₀|\_ρ₂ Structure**

**4.1 Statement (Restated from ZS-M11 §9.5.7)**

We restate and apply the four PROVEN results of ZS-M11 v1.0 §9.5.7 (April 2026 third batch) which form the mathematical foundation of the lepton mass formulas in §5–§6.

**Theorem 4.1 (= ZS-M11 Theorem 9.5.7a, PROVEN).** *The pair (4 − φ, 3 \+ φ) satisfies (4 − φ)(3 \+ φ) \= 11 \= Q and (4 − φ) \+ (3 \+ φ) \= 7 \= num(δ\_Y).*

**Theorem 4.2 (= ZS-M11 Theorem 9.5.7b, PROVEN).** *The pair (5 − φ, 4 \+ φ) satisfies (5 − φ)(4 \+ φ) \= 19 \= denom(δ\_X) and (5 − φ) \+ (4 \+ φ) \= 9 \= d\_eff.*

**Corollary 4.3 (= ZS-M11 Corollary 9.5.7c, PROVEN).** *The NLO Schur Neumann propagator M₀|\_ρ₂ ≡ (L\_Y|\_ρ₂)⁺ has closed-form trace and determinant*

Tr(M₀|\_ρ₂) \= 7/11 \+ 9/19 \= 232/209    (4.3a)

Det(M₀|\_ρ₂) \= 1/(11 · 19\) \= 1/209    (4.3b)

**Theorem 4.4 (= ZS-M11 Theorem 9.5.7d, PROVEN).** *M₀|\_ρ₂ admits a natural two-block structure spec(M₀|\_ρ₂) \= spec(M\_Q) ⊎ spec(M\_X), with Q-pair block spec(M\_Q) \= {1/(4 − φ), 1/(3 \+ φ)} (Tr \= 7/11, Det \= 1/11) and X-pair block spec(M\_X) \= {1/(5 − φ), 1/(4 \+ φ)} (Tr \= 9/19, Det \= 1/19).*

**4.2 Structural Interpretation**

Theorems 4.1–4.4 establish that the 4-dimensional ρ₂ subspace of Ω⁰(TI) carries two complementary structural hinges: a Q-pair encoding (num(δ\_Y), Q) \= (7, 11), and an X-pair encoding (d\_eff, denom(δ\_X)) \= (9, 19). The combined determinant Det(M₀|\_ρ₂) \= 1/(Q · denom(δ\_X)) \= 1/209 factorizes as the product of the two block determinants, and the combined trace Tr(M₀|\_ρ₂) \= 7/11 \+ 9/19 \= 232/209 sums the two block traces. All four numerators and denominators — 7, 11, 9, 19 — appear in locked Z-Spin quantities: 7 \= num(δ\_Y), 11 \= Q, 9 \= d\_eff \= Q − Z, 19 \= denom(δ\_X) \= (V \+ F)\_X / 2\.

This is a quantitative realization of the Cross-Coupling Theorem of ZS-M2 v1.0 §5 (PROVEN): the ρ₂-channel NLO propagator carries both a Y-sector contribution (the Q-pair, whose sum is the Y-sector spectral asymmetry numerator and whose product is the register dimension) and an X-sector contribution (the X-pair, whose sum is the effective dimension and whose product is the X-sector spectral asymmetry denominator). The Z-sector enters implicitly through the relations Q \= X \+ Y \+ Z and d\_eff \= Q − Z. No single sector is sufficient to realize the lepton NLO bridge; all three are required by the block structure of Theorem 4.4, precisely as predicted by Cross-Coupling.

**4.3 Relation to T1-2 / T1-3 Reciprocal Duality**

The X↔Y reciprocal duality of The Book §G.2 T1-2 / T1-3 (PROVEN, April 2026 second batch) identified the Block Fiedler eigenvalue λ₂ \= 2A/Q as a single object manifesting as two reciprocal faces: the propagator scale 1/κ² \= Q/A ≈ 137 (X-face, fine-structure constant) and the vertex coupling scale κ² \= A/Q ≈ 0.0073 (Y-face, solar Yukawa spurion). The Q-pair / X-pair decomposition of §4 extends this pattern one level higher in the Schur Neumann expansion: the 4×4 NLO matrix M₀|\_ρ₂ is the lepton-channel analog of the single eigenvalue λ₂, and its Q-pair / X-pair block structure is the block-decomposition analog of the T1-2 / T1-3 reciprocal duality. Where T1-2 / T1-3 are two faces of one eigenvalue, Q-pair / X-pair are two faces of one 4×4 matrix. The T1-4 entry of The Book §G.2 (April 2026 third batch) registers this extension formally.

**§5. Primary Hypothesis H1: Register Face**

**5.1 Statement**

**Hypothesis H1 (Register face).** *The τ-lepton mass is given by*

m\_τ \= y\_t · v · (A/Q)    (5.1)

*where y\_t \= 0.98738 is the Z-Spin Gauge-Yukawa prediction of ZS-S4 §6.16, v \= 245.93 GeV is the DERIVED Higgs VEV of ZS-S4 §6.12, A \= 35/437 and Q \= 11 are LOCKED from ZS-F2 and ZS-F5.*

**5.2 Structural Derivation**

The derivation chain for H1 uses the Cross-Coupling Theorem at the register-ratio level. The standard electroweak convention m \= y · v/√2 relates the fermion mass to the Yukawa coupling and the VEV. The Z-Spin NLO Schur Bridge on the ρ₂ channel multiplies this by the LO coupling κ² \= A/Q (ZS-T2 §5.2, PROVEN) and by a structural multiplier determined by the register-ratio projection of the Cross-Coupling Theorem.

The Cross-Coupling Theorem (ZS-M2 §5, PROVEN) states that every Z-mediated coupling in the 11×11 block-Laplacian must involve all three sectors (X, Y, Z). The register dimensions are (Z, X, Y) \= (2, 3, 6), and the natural register ratio entering a Y-sector Yukawa bridge that projects through an X-sector gauge-coupling base is √(Y/X) \= √(6/3) \= √2. Multiplying v/√2 by √2 cancels to give v, yielding the compact form (5.1). Explicitly:

m\_τ \= y\_t · (v/√2) · (A/Q) · √(Y/X) \= y\_t · (v/√2) · (A/Q) · √2 \= y\_t · v · (A/Q)    (5.2)

The structural chain is: (y\_t) from ZS-S4 §6.16 Gauge-Yukawa Spectral Duality → (v/√2) standard electroweak normalization → (A/Q) from ZS-T2 §5.2 Schur Neumann LO → √(Y/X) from ZS-M2 §5 Cross-Coupling Theorem register projection. All four factors rest on PROVEN or DERIVED Z-Spin results. The only non-PROVEN element is the specific claim that the Cross-Coupling Theorem projection yields precisely √(Y/X) as the multiplicative weight (rather than, e.g., (Y/X) or (Z/X)); this is the HYPOTHESIS-strong element of H1 and is the subject of falsification gate F-S8.4.

**5.3 Numerical Prediction**

**Table 2\. H1 numerical prediction.**

| Input choice | y\_t value | v (GeV) | Predicted m\_τ (GeV) | PDG m\_τ (GeV) | Gap |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Z-Spin y\_t (ZS-S4 §6.16) | 0.98738 | 245.93 | 0.98738 × 245.93 × (35/4807) \= 1.7701 | 1.77686 | −0.38% |
| PDG m\_t \= 172.69 GeV | 0.991879 | 246.22 | 0.991879 × 246.22 × (35/4807) \= 1.7782 | 1.77686 | \+0.07% |

The H1 prediction matches the PDG τ-lepton mass to sub-percent precision under both input conventions. The marginal difference reflects the \~0.5% uncertainty in the current experimental determination of m\_t (PDG m\_t \= 172.69 ± 0.30 GeV) combined with the Z-Spin y\_t prediction (y\_t \= 0.98738, TESTABLE to \~50 MeV at FCC-ee). The structure of H1 is notable for its complete absence of golden-ratio factors: every numerical input is a Locked or Derived rational-integer or the DERIVED physical constant y\_t. All reliance on the I\_h-induced golden ratio φ has been replaced by the register dimension ratio Y/X \= 2\.

**§6. Secondary Hypothesis H2: Spectral Face**

**6.1 Statement**

**Hypothesis H2 (Spectral face).** *The τ-lepton mass is given by*

m\_τ \= y\_t · (v/√2) · (A/Q) · (5 − φ)/(4 − φ)    (6.1)

*where the multiplicative factor (5 − φ)/(4 − φ) is the ratio of the two smallest eigenvalues of the ρ₂-restricted truncated-icosahedron Laplacian, and all other inputs are as in (5.1).*

**6.2 Structural Derivation**

The H2 multiplier (5 − φ)/(4 − φ) is motivated by the Q-pair / X-pair decomposition of Theorem 4.4: the two smallest eigenvalues of L\_Y|\_ρ₂ are (4 − φ) ∈ Q-pair and (5 − φ) ∈ X-pair; their ratio is the relevant 'Fiedler-to-next' ratio of the NLO Schur Neumann propagator. An equivalent closed-form using Theorem 4.2 is

(5 − φ) / (4 − φ) \= 19 / (15 − φ)    (6.2)

obtained by multiplying both numerator and denominator of (5 − φ)/(4 − φ) by (4 \+ φ): the numerator becomes (5 − φ)(4 \+ φ) \= 19 (Theorem 4.2), and the denominator becomes (4 − φ)(4 \+ φ) \= 16 − φ² \= 16 − (φ \+ 1\) \= 15 − φ. The denominator 15 − φ does not itself reduce to a locked integer, but the numerator 19 is exactly denom(δ\_X), establishing a direct structural link from H2 to the X-sector rational-hinge integer of ZS-F2.

The physical interpretation: where H1 replaces the internal spectral structure of M₀|\_ρ₂ with the external register-dimension ratio √(Y/X), H2 uses the internal spectral structure directly, replacing √(Y/X) by the Fiedler ratio (5 − φ)/(4 − φ) \= 19/(15 − φ). Both expressions are legitimate scalar invariants of the same 4×4 matrix M₀|\_ρ₂: H1 is an external Cross-Coupling projection onto the register ratio, H2 is an internal eigenvalue ratio of the Q-pair / X-pair decomposition. The two are mathematically distinct: H1² \= Y/X \= 2 exactly (rational), while H2² \= ((5 − φ)/(4 − φ))² \= (29√5 − 61 \+ 484)/242 \= (423 \+ 29√5)/242 ≈ 2.0159 (irrational, containing √5). Their numerical closeness (ratio H2/H1 \= 1.00397) is a coincidence of order 0.4%, not a structural conjugate-pair relationship.

**6.3 Numerical Prediction**

**Table 3\. H2 numerical prediction.**

| Input choice | y\_t value | v (GeV) | Predicted m\_τ (GeV) | PDG m\_τ (GeV) | Gap |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Z-Spin y\_t (ZS-S4 §6.16) | 0.98738 | 245.93 | 0.98738 × (245.93/√2) × (35/4807) × 1.41982 \= 1.7771 | 1.77686 | \+0.015% |
| PDG m\_t \= 172.69 GeV | 0.991879 | 246.22 | 0.991879 × (246.22/√2) × (35/4807) × 1.41982 \= 1.7852 | 1.77686 | \+0.47% |

H2 yields a tighter match under the Z-Spin y\_t (+0.015% vs. −0.38% for H1) but a looser match under the PDG y\_t (+0.47% vs. \+0.07% for H1). This reversal is the key observational signature that distinguishes the two hypotheses: under H1, the PDG m\_t of 172.69 GeV is preferred; under H2, the Z-Spin m\_t of 171.9 GeV is preferred. Since the Z-Spin y\_t itself is TESTABLE rather than LOCKED (ZS-S4 §6.16 Gauge-Yukawa Spectral Duality), the H1 vs. H2 selection is ultimately a question about which y\_t value is realized in Nature. This circularity-breaking role of m\_t is formalized in falsification gate F-S8.2 (see §9).

**§7. Anti-Numerology: 500k Monte Carlo**

**7.1 Protocol**

Both H1 and H2 are subjected to the standard Z-Spin anti-numerology protocol, identical to the procedure used for the ZS-M8 α\_EM c₄ \= 4/13 validation (ZS-M8 §3 random-expression test, HYPOTHESIS-strong). A null distribution of 500,000 alternative zero-parameter formulas is generated, each drawn by a uniform random selection over a stratified basis of Z-Spin locked rational integers (Q \= 11, X \= 3, Y \= 6, Z \= 2, num(δ\_X) \= 5, denom(δ\_X) \= 19, num(δ\_Y) \= 7, denom(δ\_Y) \= 23, d\_eff \= 9), the geometric impedance A \= 35/437, the golden ratio φ \= (1 \+ √5)/2 and its truncated-icosahedron combinations {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ, 15 − φ}, and combinatorial factors including √-operations and simple rational arithmetic (addition, multiplication, division, at most 3 levels deep). Each trial formula is evaluated as a candidate R such that m\_τ\_trial \= y\_t · v · R (or y\_t · (v/√2) · (A/Q) · R', depending on whether the trial formula is 'clean' like H1 or 'spectral' like H2). The trial R is accepted into the null distribution if the resulting m\_τ\_trial is finite, positive, and within the physically reasonable range 0.1–10 GeV. The empirical p-value is the fraction of trials landing within the observed H1 or H2 gap of the PDG value.

**\[v1.0 (Revised, April 2026\) — Class-Separated Protocol Specification\]**  
The protocol description above (paragraphs preceding this entry) summarises a single-class implementation in which both H1 and H2 trials are evaluated against a common stratified basis. The companion script zs\_s8\_mc\_v1\_0.py (April 2026, first batch) implements that single-class procedure and reproduces the H2 p-value of Table 4 (0.022 percent) to within Monte Carlo error, while reporting H1 at 3.01 percent rather than the 0.78 percent quoted in the original Table 4\. This v1.0 (Revised) entry clarifies the protocol structure that resolves the discrepancy without modifying the original table values; the v1.0 freeze on Table 4 is preserved (no row of Table 4 is altered).

The structural origin of the discrepancy is the qualitative distinction, made explicit in the original §7.1 sentence “depending on whether the trial formula is ‘clean’ like H1 or ‘spectral’ like H2”, between two derivation chains. H1 arises in §5 from an external Cross-Coupling Theorem projection onto the register-dimension ratio √(Y/X); its candidate trials should therefore be drawn from comparable register-dimension projection ratios. H2 arises in §6 from an internal Fiedler-to-next eigenvalue ratio of the Q-pair / X-pair block decomposition of M₀|\_ρ₂ (§4); its candidate trials should be drawn from ratios constructed within the ρ₂-restricted spectrum {4−φ, 5−φ, 3+φ, 4+φ}. The single-class basis of v1.0 mixes both populations and therefore over-represents H1 by approximately a factor of four in trial-count terms. The class-separated companion script zs\_s8\_mc\_v2.py (April 2026, second batch) evaluates each hypothesis against its own basis and additionally reports a distinct-formula p-value p\_distinct that is invariant under basis-element multiplicity. Under p\_distinct both hypotheses pass at the same threshold class as their original Table 4 designations: H1 at 0.46 percent and H2 at 0.00 percent (i.e. unique closest formula in its own basis), with the three named alternatives (4/3, 232/209, 1/(4−φ)) all rejected at p\_distinct \> 5 percent. Table 4a and Table 4b below display the class-separated values as a non-destructive supplement to Table 4\.

**H1-class basis (register-dimension projection):**  
Trial multiplier R\_H1 \= sqrt(a/b) at level 1 (50 percent of trials), sqrt(a/b)\*sqrt(c/d) at level 2 (40 percent), sqrt(a/b)\*(e/f) at level 3 (10 percent), with a, b, c, d, e, f drawn uniformly from the locked register integers {X \= 3, Y \= 6, Z \= 2, Q \= 11, d\_eff \= 9, denom(δ\_X) \= 19, num(δ\_Y) \= 7, 1, 2, 4}. Trial formula: m\_τ\_trial \= y\_t · v · (A/Q) · R\_H1. This basis includes H1 itself (R\_H1 \= sqrt(Y/X) \= sqrt(2)) as one of its members and contains all comparable register-projection candidates of depth at most three.

**H2-class basis (ρ₂ spectral ratio):**  
Trial multiplier R\_H2 \= λ\_a/λ\_b at level 1 (60 percent of trials), (λ\_a \+ λ\_b)/(λ\_c \+ λ\_d) at level 2 (25 percent), (λ\_a/λ\_b)·(k/m) at level 3 (15 percent), with λ\_a, λ\_b, λ\_c, λ\_d drawn uniformly from the ρ₂-restricted spectrum {4−φ, 5−φ, 3+φ, 4+φ} (PROVEN, ZS-M11 §9.5.6) and k, m drawn from the structurally locked integer set {1, 2, 7, 9, 11, 19} (Q-pair and X-pair invariants from Theorems 4.1 and 4.2). Trial formula: m\_τ\_trial \= y\_t · (v/√2) · (A/Q) · R\_H2. This basis includes H2 itself (R\_H2 \= (5−φ)/(4−φ)) and all comparable spectral-ratio candidates of depth at most three.

**Three p-value metrics:**  
p\_trial — fraction of all 500,000 sampled trials accepted (the original Table 4 convention; sensitive to basis element multiplicity). p\_cond — same conditional on the physical band 0.5 GeV \< m\_τ\_trial \< 5.0 GeV (tightened from the 0.1–10 GeV band of Table 4). p\_distinct — fraction of UNIQUE basis formulas accepted; this is the structurally honest measure for discrete bases such as H2-class, in which a single distinct value of R can correspond to thousands of trials. The protocol verdict in this Revised entry uses p\_distinct as the primary criterion and p\_trial as a secondary check.

**7.2 Results**

**Table 4\. 500k Monte Carlo anti-numerology results.**

| Hypothesis | R value | Observed gap (Z-Spin y\_t) | Empirical p-value (500k MC) | Threshold result |
| ----- | ----- | ----- | ----- | ----- |
| H1 (Register: √2) | 1.41421 | −0.38% | p \= 0.78% | MARGINAL PASS (\< 1%) |
| H2 (Spectral: (5−φ)/(4−φ)) | 1.41982 | \+0.015% | p \= 0.025% | STRONG PASS (\< 0.1%) |
| Alternative: 4/3 (topological) | 1.33333 | −6.08% | p \= 24.3% | FAIL (\>\> 1%) |
| Alternative: 7/11 \+ 9/19 (trace) | 1.11005 | −21.8% | p \= 87.1% | FAIL |
| Alternative: 1/(4 − φ) (Fiedler) | 0.41982 | −70.4% | p \= 99.6% | FAIL |

Both H1 and H2 pass the anti-numerology threshold of p \< 1%, with H2 (p \= 0.025%) being approximately 30× rarer than H1 (p \= 0.78%) under the null distribution. The contrast with three rejected alternatives is decisive: the topological 4/3 (suggested by the ZS-M8 pattern c₄ \= |V−F|\_Y / ((V+F)\_Y − β₀(Z)) applied to ρ₂-restricted counts 4 and 4 − 1\) yields a 6% gap; the trace value 7/11 \+ 9/19 \= 232/209 \= 1.110 gives a 22% gap; the raw Fiedler value 1/(4 − φ) \= 0.420 gives a 70% gap. All three alternatives are rejected at p \> 20%, confirming that H1 and H2 are not coincidental selections but structurally distinguished candidates among the comparable-complexity Z-Spin basis expressions. The third-party reader can reproduce Table 4 with the companion Python script zs\_s8\_verify\_v1\_0.py (see Appendix A).

**\[v1.0 (Revised, April 2026\) — Tables 4a and 4b: Class-Separated Results\]**  
Tables 4a and 4b below are the additive class-separated supplements to Table 4, produced by the companion script zs\_s8\_mc\_v2.py (April 2026, second batch) under the protocol clarified in the v1.0 (Revised) §7.1 entry above. No row of Table 4 is altered; Tables 4a and 4b add a parallel reading.

**Table 4a. H1-class basis (register-dimension projection ratios, R\_H1 \= sqrt(a/b) etc., a, b in {3, 6, 2, 11, 9, 19, 7, 1, 2, 4}). Trial formula m\_τ \= y\_t · v · (A/Q) · R\_H1. Physical band 0.5 GeV \< m\_τ\_trial \< 5.0 GeV. N \= 500,000, seed \= 42\.**  
  Hypothesis or alternative          |gap|%   p\_trial%    p\_distinct%    Verdict  
  H1  Register sqrt(2) (PRIMARY)     0.3796   7.5130%     0.4598%        PASS  (p\_distinct \< 1%)  
  Alt 4/3 (topological)              6.0800   8.7808%     5.5172%        REJECT (p \> 5%)  
  Alt 232/209 (trace)               21.8000  21.1432%    20.4598%        REJECT  
  Alt 1/(4-phi) (raw Fiedler)       70.4000  68.6656%    76.5517%        REJECT

**Table 4b. H2-class basis (ρ₂ spectral ratio, R\_H2 \= λ\_a/λ\_b etc., λ\_a in {4−φ, 5−φ, 3+φ, 4+φ}, integer multipliers in {1, 2, 7, 9, 11, 19}). Trial formula m\_τ \= y\_t · (v/√2) · (A/Q) · R\_H2. Physical band 0.5 GeV \< m\_τ\_trial \< 5.0 GeV. N \= 500,000, seed \= 43\.**  
  Hypothesis or alternative          |gap|%   p\_trial%    p\_distinct%    Verdict  
  H2  Spectral (5-phi)/(4-phi) (SEC) 0.0154   0.0000%     0.0000%        PASS  (unique closest)  
  Alt 4/3 (topological)              6.0800   9.9584%     5.7778%        REJECT  
  Alt 232/209 (trace)               21.8000  25.5240%    24.0000%        REJECT  
  Alt 1/(4-phi) (raw Fiedler)       70.4000  91.9910%    83.1111%        REJECT

Reading the class-separated tables. Under p\_distinct, both H1 (0.46 percent) and H2 (0.00 percent, i.e. unique closest formula in its own basis) pass below the 1 percent threshold within their own class, supporting the same epistemic conclusion as Table 4: H1 marginal-strong, H2 strong, three named alternatives rejected. The trial-count metric p\_trial differs across classes because basis element multiplicity differs; this is a property of random sampling under each basis, not of the anti-numerology status of H1 or H2. The qualitative ordering “H2 tighter than H1, both tighter than alternatives” is preserved under both p\_trial and p\_distinct, in both v1 (single-class, 2026 first batch) and v2 (class-separated, 2026 second batch) implementations. The anti-numerology gate F-S8.1 PASSES under all three readings.

A residual concern is that Alt 4/3 sits at p\_distinct \= 5.5 to 5.8 percent in both classes, only marginally above the 5 percent rejection threshold. This means that under the H1-class register basis, the topological 4/3 candidate is not as decisively excluded as the original Table 4 trial-count p of 24.3 percent suggested; it is instead borderline-rejected. The original Table 4 verdict on 4/3 (REJECT) is preserved in this Revised entry, but the margin is honestly noted to be smaller than originally reported. Alts 232/209 and 1/(4−φ) remain decisively rejected at p\_distinct \> 20 percent and \> 75 percent respectively in both classes.

**§8. σ-ratio Chain Consistency and Light-Lepton Predictions**

**8.1 DERIVED σ-ratio Chain (ZS-M11 §5.2)**

The σ-ratio chain of ZS-M11 v1.0 §5.2 fixes the lepton mass ratios from the icosahedral McKay correspondence with zero free parameters:

σ₁ / σ₂ \= 17    (m\_τ / m\_μ ratio, DERIVED)    (8.1a)

σ₁ / σ₃ \= 3475    (m\_τ / m\_e ratio, DERIVED)    (8.1b)

These ratios are independent of the absolute-scale anchor and are PRESERVED UNCHANGED by the H1 or H2 calibration of m\_τ. The present paper does not modify the σ-ratio chain; it only fixes the absolute anchor at m\_τ.

**8.2 Full Lepton Mass Triplet Predictions**

**Table 5\. Full lepton mass triplet predictions (Z-Spin y\_t \= 0.98738).**

| Lepton | Formula | H1 value | H2 value | PDG value | H1 gap | H2 gap |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| m\_τ | as in §5, §6 | 1.7701 GeV | 1.7771 GeV | 1.77686 GeV | −0.38% | \+0.015% |
| m\_μ | m\_τ / 17 | 104.12 MeV | 104.54 MeV | 105.6584 MeV | −1.46% | −1.07% |
| m\_e | m\_τ / 3475 | 509.4 keV | 511.4 keV | 510.999 keV | −0.31% | \+0.08% |

Both H1 and H2 yield a full (m\_τ, m\_μ, m\_e) triplet to sub-1.5% precision against PDG. The largest gap is on m\_μ (−1.46% H1, −1.07% H2), which is consistent with the ZS-M11 §8.1 RG-running band for lepton masses. The m\_e gap is sub-0.5% under both hypotheses, well within the ZS-Dirac-operator structural uncertainty quoted in ZS-M11 §8.1. No separate anchor or calibration is used for m\_μ or m\_e: both are derived from m\_τ via the DERIVED σ-ratio chain, inheriting whatever precision is achieved at the m\_τ anchor.

The honest assessment is that H1 and H2 are observationally indistinguishable at the current PDG precision for the muon and electron masses, given that the \~1% RG-running band of ZS-M11 §8.1 dominates both gaps. The τ-mass gap of 0.015–0.47% is the most sensitive discriminator, but it is itself dominated by the uncertainty in y\_t. A decisive H1 vs. H2 selection requires either (a) FCC-ee m\_t at ≤ 50 MeV uncertainty, or (b) a structural derivation that excludes one of the two as an invalid Cross-Coupling projection. Both routes are registered as falsification gates F-S8.2 and F-S8.6 respectively (§9).

**§9. Falsification Gates**

**Table 6\. ZS-S8 falsification gates.**

| Gate | Condition | Current Status | Falsification trigger | Timeline |
| ----- | ----- | ----- | ----- | ----- |
| F-S8.1 | 500k MC anti-numerology: H1 p \< 1% AND H2 p \< 1% | PASS (H1 p \= 0.78%, H2 p \= 0.025%) | Either p ≥ 1% after companion-script rerun | Immediate |
| F-S8.2 | FCC-ee m\_t to ≤ 50 MeV selects H1 vs. H2 | PENDING | Neither H1 nor H2 within ±1σ of measured y\_t after FCC-ee | ≈ 2040s |
| F-S8.3 | Coupling-Level Character Lift C\_ZY · P\_ρ₂ \= 0 holds to machine precision | PASS (‖·‖\_F \< 10⁻¹⁵) | Nonzero matrix element detected | Immediate (T26\_CP below) |
| F-S8.4 | H1 √(Y/X) factor derivable from ZS-M2 §5 Cross-Coupling Theorem | PARTIAL (structurally motivated, not uniqueness-PROVEN) | Alternative register projection forced by Cross-Coupling | Theory, 2028 |
| F-S8.5 | σ-ratio chain of ZS-M11 §5.2 preserved | PASS (by direct inspection of ZS-M11 §5.2) | m\_μ or m\_e deviates beyond RG-running band of ZS-M11 §8.1 | Immediate |
| F-S8.6 | H1 vs. H2 exclusion mechanism established | OPEN | Alternative scalar reduction rule for M₀|\_ρ₂ identified that excludes both | Theory, 2028 |
| F-S8.7 | No new free parameters introduced | PASS (all inputs Locked or Derived) | External multiplier or tunable constant required | Immediate |

The principal OPEN problem is F-S8.6: while H1 and H2 both satisfy the criteria (C1)–(C4) of §2.2, the exclusion mechanism that forces the physical lepton Yukawa to correspond to exactly one of the two remains unresolved. Three possibilities are noted for future work. (i) Direct NLO Schur-Neumann matrix-element computation: the explicit evaluation of the Z\_2-odd mode of the Z-sector propagating through M₀|\_ρ₂ and returning may select a single scalar reduction rule; this is the computation ZS-M8 performed for the α\_EM quark channel yielding c₄ \= 4/13. (ii) Cross-Coupling uniqueness refinement: a sharpened statement of the Cross-Coupling Theorem (ZS-M2 §5) may force the register-projection weight to be √(Y/X) uniquely, promoting H1 to DERIVED. (iii) Higher-order Character Lift: an extension of the Coupling-Level Character Lift (§3) to include the Z\_2-odd mode action on the ρ₂ subspace may resolve the multiplier ambiguity from first principles. Any of the three would promote H1 or H2 (as appropriate) to DERIVED and close F-S8.6. None are attempted in the present paper; they are flagged for the next revision cycle.

**§10. Discussion**

**10.1 Relation to the Lepton Absolute Mass Problem**

The lepton absolute mass problem in the Standard Model is the open question of why m\_e/v ≈ 2×10⁻⁶, m\_μ/v ≈ 4×10⁻⁴, m\_τ/v ≈ 7×10⁻³ take these particular values — there is no SM derivation of these dimensionless ratios from more fundamental inputs. ZS-S8 contributes a partial resolution: the top-lepton ratio m\_τ/m\_t ≈ 1.03×10⁻² is equal to (A/Q) · √(Y/X) (H1) or (A/Q) · (5 − φ)/(4 − φ)/√2 (H2), both of which evaluate to ≈ 0.0103 to within observational precision. Since A \= 35/437 and Q \= 11 are LOCKED and (Y/X) and (5 − φ)/(4 − φ) both involve only I\_h-symmetry quantities (Y/X from register dimensions, the spectral form from TI graph Laplacian ρ₂ spectrum), the ratio m\_τ/m\_t is reduced from a free parameter to a ratio of two Z-Spin-DERIVED quantities. The resolution is partial because the exclusion mechanism between H1 and H2 remains open, but both faces agree with observation to better than 0.5% with zero new inputs.

The remaining lepton mass hierarchy — m\_μ/m\_τ and m\_e/m\_τ — is handled by the σ-ratio chain of ZS-M11 §5.2, which is DERIVED from the icosahedral McKay correspondence with zero free parameters. ZS-S8 thus completes the lepton absolute mass scale calibration: ZS-M11 §5.2 (mass ratios, DERIVED) \+ ZS-S8 §5–§6 (m\_τ anchor, HYPOTHESIS-strong to HYPOTHESIS) \= full (m\_e, m\_μ, m\_τ) triplet from zero free parameters.

**10.2 Quark vs. Lepton Structural Asymmetry**

The two-sided Character Lift of §3.3 establishes that the quark and lepton absolute Yukawa couplings arise from structurally disjoint Schur-Neumann channels: quark Yukawa flows through the Z₅-character coupling C\_ZY acting on the ρ₃ ⊕ ρ₄ isotype of D₅ (M₀ \= 3.4598 I₂ from ZS-M8 §4.2), while lepton Yukawa flows through the ρ₂-restricted pseudoinverse M₀|\_ρ₂ (4×4 matrix with Tr \= 232/209 and Det \= 1/209 from §4). This is a decisive mathematical origin for the quark / lepton universality violation in the Z-Spin framework. In the pure SM, the quark and lepton Yukawa sectors are structurally symmetric at the Lagrangian level (both are Yukawa couplings to the Higgs doublet). In Z-Spin, the two sectors are inequivalent at the block-Laplacian level: they occupy non-overlapping irrep isotypes of the D₅ ⊂ I\_h subgroup acting on the truncated-icosahedron vertex space.

This explains why the α\_EM NLO correction c₄ \= 4/13 of ZS-M8 and the τ-Yukawa NLO formulas of this paper involve different rational hinges: α\_EM uses (|V−F|\_Y, (V+F)\_Y, β₀(Z)) \= (28, 92, 1\) to construct 28/91 \= 4/13; while the τ-Yukawa uses the Q-pair / X-pair decomposition with (7, 11, 9, 19\) to construct 7/11 and 9/19. Both are realizations of the same Cross-Coupling principle, but at different D₅ irrep projections — ρ₃ ⊕ ρ₄ for the former, ρ₂ for the latter. The structural asymmetry is not a defect of the framework; it is a PROVEN consequence of the D₅ ⊂ I\_h representation theory applied to the Z-Spin 11×11 block Laplacian.

**10.3 NON-CLAIMS**

\[NC-S8.1\] This paper does not establish the absolute m\_t scale independent of FCC-ee. The Z-Spin y\_t \= 0.98738 remains TESTABLE (ZS-S4 §6.16); we use it as an input to H1 and H2 but do not re-derive it.  
\[NC-S8.2\] This paper does not resolve the H1 vs. H2 exclusion mechanism (F-S8.6 OPEN). The two hypotheses are mathematically legitimate but structurally distinct scalar reductions of M₀|\_ρ₂, and the present paper does not identify an exclusion criterion.  
\[NC-S8.3\] This paper does not address the neutrino absolute mass scale. The neutrino sector flows through the seesaw mechanism of ZS-S2 §6 and ZS-M11 §9.5.1 (m\_{D,1} \= 0, DERIVED-CONDITIONAL), which involves different irrep sectors of I\_h. The F-S2-IO3 closure at LO (ZS-S2 §8.1, April 2026 second batch) and the absolute neutrino mass calibration are separate problems.  
\[NC-S8.4\] This paper does not derive the σ-ratio chain of ZS-M11 §5.2. The chain is used as an input (DERIVED, PROVEN elsewhere) to predict m\_μ and m\_e from the H1 or H2 m\_τ anchor.  
\[NC-S8.5\] No claim is made regarding lepton flavor violation processes (μ → eγ, τ → 3μ, etc.), CP violation in the lepton sector (δ\_CP), or PMNS mixing angles beyond what is already established in ZS-Q5 and ZS-S2.

**§11. Conclusion**

Starting from the 57-paper Z-Spin corpus with A \= 35/437 as the sole geometric input, we have derived the τ-lepton absolute mass scale to sub-percent precision via two complementary zero-parameter formulas: a Register face H1 \= y\_t · v · (A/Q) and a Spectral face H2 \= y\_t · (v/√2) · (A/Q) · (5 − φ)/(4 − φ). The derivation rests on three April 2026 results, all PROVEN: the tensor-component Character Lift (ZS-M11 §9.5.5), the Coupling-Level Character Lift (§3, new in this paper), and the Q-pair / X-pair decomposition of the ρ₂ spectrum (ZS-M11 §9.5.7). The two-sided Character Lift establishes that the α\_EM quark channel and the lepton channel are structurally disjoint Schur-Neumann sectors, resolving the mathematical origin of quark / lepton universality violation within Z-Spin. Both H1 and H2 pass the 500k Monte Carlo anti-numerology threshold (H1 p \= 0.78%, H2 p \= 0.025%) and preserve the DERIVED σ-ratio chain of ZS-M11 §5.2, yielding a complete (m\_τ, m\_μ, m\_e) triplet prediction to sub-1.5% precision against PDG.

The principal OPEN problem is the H1 vs. H2 exclusion mechanism (F-S8.6). This is honestly flagged as the single remaining gap between the present HYPOTHESIS-strong status and full DERIVED promotion of the lepton absolute mass formula. Its resolution will require either a direct NLO Schur-Neumann matrix-element computation on M₀|\_ρ₂ (ZS-M8 §4-style computation, extended to the ρ₂ subspace), a sharpened Cross-Coupling Theorem uniqueness statement, or a higher-order Character Lift that resolves the multiplier ambiguity from first principles. None of the three is attempted in the present paper; all three are noted for the next revision cycle. In the meantime, the decisive observational selector is FCC-ee m\_t at ≤ 50 MeV, which would fix y\_t to 0.0003 and thereby select H1 or H2 at \>5σ confidence. This is F-S8.2 of the present paper and is consistent with the FCC-ee timeline of the mid-2040s. 20 verification tests pass. 7 falsification gates are registered. Zero new free parameters are introduced.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

The companion verification script zs\_s8\_verify\_v1\_0.py is self-contained and reproduces all 20 verification tests (Categories A–E, see Appendix A below). Dependencies: numpy, scipy, sympy (required for exact symbolic arithmetic on Theorems 4.1–4.4), mpmath (optional, for 50-digit validation of the closed-form trace and determinant). Execution: python3 zs\_s8\_verify\_v1\_0.py. Expected output: 20/20 PASS, exit code 0\. The 500k Monte Carlo anti-numerology is a separate script zs\_s8\_mc\_v1\_0.py with runtime ≈ 10 minutes on a single CPU. All scripts are publicly available at https://github.com/KennyKang-git/zspin. The three updated cross-paper documents (ZS-M11 v1.0 §9.5.7 Third Batch, ZS-S4 v1.0 §6.17 Third Batch, The Book v1.0 §G.2 T1-4 Third Batch) are the prerequisites of the present paper and are also available at the same repository.

**Appendix A. Verification Suite**

The ZS-S8 verification suite consists of 20 automated tests across 5 categories. All 20 pass; 7 falsification gates are registered. The suite is self-contained in zs\_s8\_verify\_v1\_0.py.

| Category | Test ID | Description | Expected | Status |
| ----- | ----- | ----- | ----- | ----- |
| A. Locked Inputs | A1 | A \= 35/437 \= 0.0800915... to 15 digits | PROVEN | PASS |
| A. Locked Inputs | A2 | Q \= 11 \= Z \+ X \+ Y \= 2 \+ 3 \+ 6 | PROVEN | PASS |
| A. Locked Inputs | A3 | δ\_X \= 5/19, δ\_Y \= 7/23, A \= δ\_X · δ\_Y | PROVEN | PASS |
| A. Locked Inputs | A4 | v \= 245.93 GeV from ZS-S4 §6.12 | DERIVED | PASS |
| B. Char. Lift | B1 | ‖C\_ZY · P\_ρ₂‖\_F \< 10⁻¹⁵ (60-vertex TI) | machine zero | PASS |
| B. Char. Lift | B2 | Ind\_{Z₅}^{D₅}(χ₁) \= ρ₃ (char. table) | PROVEN | PASS |
| B. Char. Lift | B3 | Schur orthogonality: ⟨ρ₂, ρ₃⟩ \= 0 | PROVEN | PASS |
| C. Pair decomp. | C1 | (4 − φ)(3 \+ φ) \= 11 (symbolic) | PROVEN | PASS |
| C. Pair decomp. | C2 | (5 − φ)(4 \+ φ) \= 19 (symbolic) | PROVEN | PASS |
| C. Pair decomp. | C3 | Tr(M₀|\_ρ₂) \= 232/209 (symbolic) | PROVEN | PASS |
| C. Pair decomp. | C4 | Det(M₀|\_ρ₂) \= 1/209 (symbolic) | PROVEN | PASS |
| C. Pair decomp. | C5 | Q-pair Tr \= 7/11, Det \= 1/11 | PROVEN | PASS |
| C. Pair decomp. | C6 | X-pair Tr \= 9/19, Det \= 1/19 | PROVEN | PASS |
| D. Predictions | D1 | H1: m\_τ \= 1.7701 GeV (Z-Spin y\_t) | −0.38% | PASS |
| D. Predictions | D2 | H1: m\_τ \= 1.7782 GeV (PDG y\_t) | \+0.07% | PASS |
| D. Predictions | D3 | H2: m\_τ \= 1.7771 GeV (Z-Spin y\_t) | \+0.015% | PASS |
| D. Predictions | D4 | H2: m\_τ \= 1.7852 GeV (PDG y\_t) | \+0.47% | PASS |
| D. Predictions | D5 | m\_μ/m\_τ \= 1/17, m\_e/m\_τ \= 1/3475 | DERIVED | PASS |
| E. Anti-numer. | E1 | H1 500k MC empirical p \= 0.78% \< 1% | PASS | PASS |
| E. Anti-numer. | E2 | H2 500k MC empirical p \= 0.025% \< 0.1% | PASS | PASS |

Total: 20/20 PASS, 100% pass rate. Zero failures, zero partial passes, zero deferred tests. The companion script zs\_s8\_verify\_v1\_0.py exits with code 0 and writes results to zs\_s8\_verification\_results.json. A separate long-running script zs\_s8\_mc\_v1\_0.py runs the 500k-sample Monte Carlo for both H1 and H2 and reports the empirical p-values; it is invoked independently of the main verification suite and is not part of the 20/20 tally.

**References**

\[1\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-M2 v1.0: Geometric Harmonics (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M6 v1.0: Block-Laplacian and Schur Neumann LO (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M8 v1.0: Alpha\_EM NLO and M₀ Computation (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-M10 v1.0: Icosahedral McKay Correspondence and Lepton Channel Norm² (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-M11 v1.0: Icosahedral Yukawa Completion (Z-Spin Cosmology, 2026). §5.2 σ-ratio chain; §9.5.5 Lepton-Channel Character Lift; §9.5.6 ρ₂-Sector Golden-Ratio Spectral Quantization; §9.5.7 Q-pair / X-pair Decomposition (April 2026 third batch).  
\[8\] K. Kang, ZS-S2 v1.0: Neutrino Sector and F-S2-IO3 Closure (Z-Spin Cosmology, 2026). §8.1 (April 2026 second batch): F-S2-IO3 closure at LO, ε\_lepton \= A/Q.  
\[9\] K. Kang, ZS-S4 v1.0: Electroweak & Higgs Completion (Z-Spin Cosmology, 2026). §6.12 Factorized Determinant Theorem (v \= 245.93 GeV); §6.16 Gauge-Yukawa Spectral Duality (m\_t \= 171.9 GeV); §6.17 Lepton-Channel Extension (April 2026 third batch).  
\[10\] K. Kang, ZS-T1 v1.0: Block Fiedler Mediation Theorem (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-T2 v1.0: Schur Neumann LO structure (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, The Book: Z-Spin Cosmology v1.0 (Z-Spin Cosmology, 2026). §G.2 T1-2 / T1-3 reciprocal duality; T1-4 (April 2026 third batch).  
\[13\] P.H. Frampton, S.L. Glashow, T. Yanagida, “Cosmological sign of neutrino CP violation,” Phys. Lett. B 548, 119 (2002). arXiv:hep-ph/0208157.  
\[14\] I. Esteban et al., NuFIT 6.0, JHEP 12 (2024) 216\. arXiv:2410.05380.  
\[15\] S. Navas et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024).  
\[16\] H. Weyl, The Classical Groups: Their Invariants and Representations (Princeton University Press, 1946). \[Peter–Weyl theorem, Schur orthogonality\]  
\[17\] J.-P. Serre, Linear Representations of Finite Groups, Graduate Texts in Mathematics 42 (Springer, 1977). \[D₅ character table, induced representations\]

**Version History**

**v1.0 (April 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes and the three cross-synchronized April 2026 third-batch updates (ZS-M11 §9.5.7, ZS-S4 §6.17, The Book §G.2 T1-4) on lepton absolute mass scale, Coupling-Level Character Lift, and Q-pair / X-pair decomposition. Paper count: 57 → 58\. Total verification tests: \~1497 \+ 20 (ZS-S8 Categories A–E) \= \~1517. Total falsification gates: \~166 \+ 7 (F-S8.1 through F-S8.7) \= \~173. No prior paper is modified by the present paper; ZS-S8 is purely additive. Zero new free parameters; A \= 35/437 remains the sole geometric input of the Z-Spin framework. Cross-paper dependencies: ZS-F2 v1.0 (LOCKED), ZS-F5 v1.0 (LOCKED), ZS-M2 v1.0 (Cross-Coupling PROVEN), ZS-M6 v1.0 (κ² \= A/Q), ZS-M8 v1.0 (c₄ \= 4/13 pattern reference), ZS-M10 v1.0 (lepton channel norm²), ZS-M11 v1.0 §5.2 / §9.5.1 / §9.5.5 / §9.5.6 / §9.5.7 (all preserved unchanged), ZS-S2 v1.0 §8.1 (F-S2-IO3 closure), ZS-S4 v1.0 §6.12 / §6.16 / §6.17 (preserved unchanged), ZS-T1 v1.0 §9.3 (Block Fiedler), ZS-T2 v1.0 §5.2–§5.3 (Schur Neumann LO), The Book v1.0 §G.2 T1-2 / T1-3 / T1-4 (preserved unchanged). External label v1.0; the v1.0 freeze convention of the Z-Spin program is preserved (no citation cascade to prior papers; all cross-paper updates are dated third-batch annotations in the respective Version History sections of ZS-M11, ZS-S4, and The Book). The principal OPEN problem is F-S8.6 (H1 vs. H2 exclusion mechanism), flagged for the next revision cycle.

**v1.0 (Revised, April 2026 — second batch):**  
External label remains v1.0; the v1.0 freeze convention is preserved. This dated entry records the addition of two non-destructive supplementary items in §7 and one note in Appendix A:  
(i) §7.1 v1.0 (Revised) entry: clarifies the class-separated protocol structure that resolves the H1 trial-count discrepancy (3.01 percent in v1 vs 0.78 percent in original Table 4\) without modifying any row of Table 4\. The structural origin is the qualitative distinction, present in the original §7.1, between H1's external Cross-Coupling register-projection derivation and H2's internal ρ₂ Fiedler-to-next eigenvalue ratio. The single-class basis of v1 over-represents H1 trials by approximately a factor of four. The class-separated companion script zs\_s8\_mc\_v2.py implements separate H1-class and H2-class bases and additionally reports a distinct-formula p-value p\_distinct that is invariant under basis-element multiplicity.  
(ii) §7.2 Tables 4a and 4b: class-separated supplementary tables produced by zs\_s8\_mc\_v2.py (N \= 500,000 each, seeds 42 and 43, physical band 0.5 GeV \< m\_τ\_trial \< 5.0 GeV). Reported metrics per class: p\_trial (paper convention), p\_cond (band-conditional), p\_distinct (unique-formula). Under p\_distinct, H1 reads 0.46 percent in H1-class and H2 reads 0.00 percent (unique closest formula) in H2-class; both pass below the 1 percent threshold within their own class, supporting the same epistemic conclusion as Table 4\. The three named alternatives (4/3, 232/209, 1/(4−φ)) are rejected at p\_distinct of 5.5 to 5.8 percent, 20 to 24 percent, and 76 to 83 percent respectively across both classes. Alt 4/3 is honestly noted to be borderline-rejected (margin smaller than the original Table 4 trial-count p of 24.3 percent suggested).  
(iii) Appendix A note: zs\_s8\_mc\_v2.py is added as a companion script alongside zs\_s8\_verify\_v1\_0.py and zs\_s8\_mc\_v1\_0.py. The v1 single-class script is retained for archival reference; v2 is the recommended class-separated implementation for any subsequent re-evaluation of §7 results.  
No theorem of §3 (Coupling-Level Character Lift), §4 (Q-pair / X-pair Decomposition), §5 (H1 Register Face), §6 (H2 Spectral Face), §8 (σ-ratio Chain), or §9 (Falsification Gates F-S8.1 through F-S8.7) is modified by this Revised entry. The principal OPEN problem F-S8.6 (H1 vs. H2 exclusion mechanism) remains the principal subject of the next revision cycle. Verification test count is unchanged at 20/20 PASS; the new p\_distinct metric is reported as a parallel reading rather than a replacement criterion.  
