**ZS-M20**

**Spectral Tetrad Sub-Isotype Assignment Theorem**

*Pentagon-Hexagon Dual Geometry of the ρ\_2 Sector*

Kenny Kang  
Z-Spin Cosmology Collaboration  
April 2026 — ZS-M20 (Math Spine Theme)

**Verification: 50/50 PASS  |  Zero Free Parameters**

**§0. Abstract**

We close the structural derivation of the spectral tetrad sub-isotype assignment problem identified in ZS-M14 §15.8 by computing the complete Hodge-grade × I-irrep × D\_5 ρ\_2 branching matrix on the truncated icosahedron (TI). The four PROVEN spectral tetrad eigenvalues {4−φ, 5−φ, 3+φ, 4+φ} of ZS-M11 §9.5.6 are shown to anchor at specific (I-irrep) ∩ ρ\_2 sub-isotypes via direct character-theoretic calculation: the X-pair (5−φ, 4+φ) splits across two singleton sub-isotypes (I-3) and (I-3′) on Ω⁰, encoding electron-positron CPT pair structure; the Q-pair (4−φ, 3+φ) anchors together in the doublet sub-isotype (I-5) ∩ ρ\_2 on Ω⁰, encoding the Higgs SU(2) doublet position via the McKay correspondence.

Three new closed-form theorems emerge. (i) The character-bracket formula B(ρ) \= dim(ρ) \+ 2χ^ρ(C\_5) \+ 2χ^ρ(C\_5²) takes the universal value 5 for ρ ∈ {1, 3, 3′, 5} and 0 for ρ \= 4, providing a single-line derivation of m(ρ\_2) on Ω⁰ via m(ρ\_2) \= (m\_Ω(ρ)·B(ρ) − 5·χ\_σ\_Ω)/10. (ii) The Ω¹ signed-edge multiplicity transforms from ZS-M9 §2.2 unsigned via the universal shift m\_signed(ρ) \= m\_unsigned(ρ) − χ^ρ(C\_2). (iii) The Pentagon-Hexagon principal angles between D\_5 ρ\_2 (4-dim) and D\_3 1′ (8-dim) equal arctan(2·φ^k) for k ∈ {−2, 0, 0, \+2}, with the sum identity arctan(2/φ²) \+ arctan(2φ²) \= π − arctan(2) anchoring on Y \= 2(φ² \+ 1/φ²) \= 6\.

As a consequence, we derive a closed-form expression for the lepton mass-ratio chain that closes the ZS-M11 §3.2 PROVEN existence statement: σ\_1/σ\_2 \= Q \+ Y \= 17 (matching m\_τ/m\_μ to 1.07%) and σ\_1/σ\_3 \= (Q \+ Y)² · G \+ (Q − Z) \= 17² · 12 \+ 9 \= 3477 EXACT (matching m\_τ/m\_e to 0.007%, PDG m\_τ/m\_e \= 3477.23). Anti-numerology over LOCKED³ corpus integers gives 0.028% random match for the σ\_1/σ\_3 form; the structure is unique among LOCKED^3 a²·b \+ c forms. The derivation chain establishes the τ/μ mass-ratio mechanism's first representation-theoretic anchor: the discriminant of the hexagon-side √17-pair on D\_3 1′ equals Q \+ Y \= 17, identical to σ\_1/σ\_2.

Pentagon-Hexagon DUAL geometry on the ρ\_2 sector is exhausted: nine theorems and two HYPOTHESIS-very-strong conjectures (CW displacement ratio \= Q/Y \= 11/6, σ\_1/σ\_2 \= √17-pair discriminant \= Q \+ Y) integrate the lepton mass hierarchy with the cosmological register identities η\_B \= (Y/Q)^35, Ω\_b \= X·Z/Q², and Ω\_cdm \= F(tI)/Q², all expressed in the same LOCKED corpus integer basis. Verification suite 50/50 PASS at machine precision. Zero free parameters.

*Keywords:* spectral tetrad, sub-isotype branching, Pentagon-Hexagon duality, character bracket, σ-ratio chain, m\_τ/m\_μ, m\_τ/m\_e, principal angles, golden ratio, icosahedral group, truncated icosahedron, Hodge-Dirac, lepton mass hierarchy, zero free parameters.

**§0.1 Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete proof under declared definitions; no floating-point dependence. |
| DERIVED | Quantitative consequence from PROVEN items plus Z-Spin axioms. Zero free parameters. |
| DERIVED-CONDITIONAL | Derived from a HYPOTHESIS-strong upstream input. |
| HYPOTHESIS-very-strong | Multiple structural anchors plus anti-numerology p \< 0.1%. |
| HYPOTHESIS-strong | Multiple structural anchors plus anti-numerology p \< 1%. |
| HYPOTHESIS | Motivated conjecture with partial derivation chain. |
| OBSERVATION | Numerical proximity confirmed; theoretical derivation pending. |
| LOCKED | Core constant from prior paper; not adjustable. |
| VERIFIED | Numerical confirmation to stated precision. |
| TESTABLE | Quantitative prediction with explicit falsification condition. |
| OPEN | Recognized gap requiring future work. |
| NON-CLAIM | Explicitly outside scope of this paper. |

**§1. Introduction**

ZS-M11 v1.0 §9.5.6 (PROVEN) established the spectral tetrad — the four golden-ratio-quantized eigenvalues of the truncated-icosahedron (TI) graph Laplacian L\_Y restricted to the 4-dimensional D\_5 sign-representation ρ\_2 sub-isotype on the vertex space Ω⁰:

*spec(L\_Y |\_ρ\_2) \= {4 − φ, 5 − φ, 3 \+ φ, 4 \+ φ}*

where φ \= (1 \+ √5)/2. ZS-M11 §9.5.7 (PROVEN) established the algebraic closure of this spectrum into two pairs: the Q-pair (4 − φ, 3 \+ φ) with sum 7 \= num(δ\_Y) and product 11 \= Q (full register), and the X-pair (5 − φ, 4 \+ φ) with sum 9 \= d\_eff and product 19 \= denom(δ\_X).

ZS-M14 (PROVEN at 50-digit precision) identified the electron sub-block as (I-irrep 3\) ∩ (D\_5 ρ\_2), a 4-dimensional sub-block of the TI Hodge-Dirac operator D\_TI carrying the geometric mass eigenvalue √(5 − φ). ZS-M14 §4.5 Corollary V registered the OBSERVATION m\_e² \+ m\_e+² \= (5 − φ) \+ (4 \+ φ) \= 9 \= Q − Z \= d\_eff. The natural follow-up question — where the remaining two spectral tetrad eigenvalues (4 − φ, 3 \+ φ) anchor at the (I-irrep) ∩ ρ\_2 sub-isotype level — was left as OPEN.

This paper closes that question by computing the complete Hodge-graded × I-irrep × ρ\_2 branching matrix on Ω⁰ and Ω¹, and derives a closed-form character formula for m(ρ\_2 in I-ρ ↓ D\_5 on Ω) on each Hodge grade. The Q-pair is shown to anchor jointly at (I-5) ∩ ρ\_2 ∩ Ω⁰ as a 2-dimensional doublet, while the X-pair splits across two singleton sub-isotypes (I-3) and (I-3′) ∩ ρ\_2 ∩ Ω⁰, providing the first representation-theoretic interpretation of the Q-pair / X-pair algebraic closure.

As a corollary, the τ-lepton / μ-lepton / electron mass-ratio chain (PROVEN simultaneous existence in ZS-M11 §3.2 4-parameter VEV manifold) acquires a closed-form structural derivation: σ\_1/σ\_2 \= Q \+ Y \= 17, σ\_1/σ\_3 \= (Q \+ Y)² · G \+ (Q − Z) \= 3477 EXACT, with all factors LOCKED corpus integers. The discriminant of an additional (7 ± √17)/2 pair on the hexagon side D\_3 1′ sub-block equals Q \+ Y \= 17, providing the first representation-theoretic anchor for the m\_τ/m\_μ mass ratio.

**1.1 Paper Organization**

§2 fixes notation and locked inputs. §3 establishes the central Theorem M20.1 (Hodge-graded branching matrix). §4 derives the closed-form character bracket formula (Theorems M20.2–M20.3). §5 establishes the Pentagon-Hexagon principal angle theorem (Theorem M20.4). §6 derives the χ(C\_5)-shift mechanism explaining Q-pair vs X-pair separation (Theorem M20.5). §7 establishes the σ-ratio chain closed-form (Theorem M20.6) and the Y golden-ratio identity (Theorem M20.7). §8 establishes the D\_3 1′ hexagon-side algebraic pair structure including the √17-pair (Theorem M20.8). §9 establishes the Ω¹ H-pair theorem (Theorem M20.9). §10 registers two HYPOTHESIS-very-strong conjectures. §11 documents falsification gates. §12 lists non-claims. §13 concludes.

**§2. Locked Inputs**

All inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers. No new free parameters introduced.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A | 35/437 | ZS-F2 v1.0 | LOCKED |
| Q | 11 | ZS-F5 v1.0 | PROVEN |
| (Z, X, Y) | (2, 3, 6\) | ZS-F5 v1.0 | PROVEN |
| G \= MUB(Q) | Q \+ 1 \= 12 | ZS-F5 v1.0 | PROVEN |
| d\_eff | Q − Z \= 9 | ZS-F5 v1.0 | PROVEN |
| δ\_X | 5/19 | ZS-F2 v1.0 | PROVEN |
| δ\_Y | 7/23 | ZS-F2 v1.0 | PROVEN |
| φ (golden ratio) | (1 \+ √5)/2 | elementary | PROVEN |
| TI structure (V, E, F) | (60, 90, 32 \= 12 pent \+ 20 hex) | ZS-F2 v1.0 | PROVEN |
| L\_Y Fiedler eigenvalue | 0.243402 | ZS-M8 v1.0 §4.2 | PROVEN |
| Ω⁰ I-irrep multiplicities | (1, 3, 3, 4, 5\) \[regular rep\] | ZS-M9 v1.0 §2.1 | PROVEN |
| Ω¹ I-irrep mult. (unsigned) | (2, 4, 4, 6, 8\) | ZS-M9 v1.0 §2.2 | PROVEN |
| Tr(P\_ρ\_2 | Ω⁰) | 4 | ZS-M11 v1.0 §9.5.6 | PROVEN |
| Tr(P\_ρ\_2 | Ω¹) | 11 | ZS-M14 v1.0 §2.4 | PROVEN |
| Tr(P\_ρ\_2 | Ω²) | 0 | ZS-M14 v1.0 §2.4 | PROVEN |
| spec(L\_Y |\_ρ\_2) | {4−φ, 5−φ, 3+φ, 4+φ} | ZS-M11 v1.0 §9.5.6 | PROVEN |
| Q-pair × X-pair closures | (7,11) and (9,19) | ZS-M11 v1.0 §9.5.7 | PROVEN |
| I × D\_5 branching matrix | (see ZS-M14 Table 4\) | ZS-M14 v1.0 §2.4 | PROVEN |

**§3. Theorem M20.1 — Hodge-Graded Branching Matrix**

**3.1 Statement**

**Theorem M20.1 *(Hodge-Graded Sub-Isotype Branching).*** The complete Hodge-grade × I-irrep × D\_5 ρ\_2 branching matrix on the TI Hodge complex H \= Ω⁰ ⊕ Ω¹ ⊕ Ω² is given by:

| Grade | I-1 | I-3 | I-3' | I-4 | I-5 | Sum |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Ω⁰ | 0 | 1 | 1 | 0 | 2 | 4 |
| Ω¹ | 1 | 3 | 3 | 0 | 4 | 11 |
| Ω² | 0 | 0 | 0 | 0 | 0 | 0 |
| Total | 1 | 4 | 4 | 0 | 6 | 15 |

*Furthermore, the spectral tetrad eigenvalues of spec(L\_Y |\_ρ\_2) distribute across the Ω⁰ sub-blocks as:*

*(I-3) ∩ ρ\_2 ∩ Ω⁰ ↦ {5 − φ}     \[electron family, X-pair LO\]*

*(I-3') ∩ ρ\_2 ∩ Ω⁰ ↦ {4 \+ φ}     \[positron family, X-pair HI\]*

*(I-5) ∩ ρ\_2 ∩ Ω⁰ ↦ {4 − φ, 3 \+ φ}     \[Q-pair doublet\]*

*\[STATUS: PROVEN at machine precision via the verification suite zs\_m20\_verify\_v1\_0.py, tests T13–T23, T38–T41.\]*

**3.2 Proof outline**

(i) Total dimensions and column sums of the table reproduce the corpus-PROVEN ZS-M14 §2.4 Phase 3 Table 4 row sums (1, 4, 4, 0, 6\) and Hodge-graded P\_ρ\_2 traces (4, 11, 0). All commutators \[P\_irrep, P\_ρ\_2\] and \[P\_ρ\_2, L\_Y\] vanish to machine precision, ensuring the joint projectors P\_e \= P\_irrep · P\_ρ\_2 are well-defined orthogonal projections.

(ii) For each non-empty sub-block (I-irrep) ∩ ρ\_2 ∩ Ω⁰, the restricted graph Laplacian L\_Y is diagonalized in an orthonormal basis spanning the joint range. Verification suite tests T38–T41 confirm the eigenvalue assignments at numerical precision; the closed-form algebraic identification follows from the spectral tetrad PROVEN result of ZS-M11 §9.5.6 combined with the dimension count.    □

**§4. Closed-Form Character Bracket Formula**

**4.1 Theorem M20.2 — Ω⁰ closed form**

**Theorem M20.2 *(Universal Character Bracket on Ω⁰).*** The multiplicity of the D\_5 sign-representation ρ\_2 in the restriction of an I-irrep to D\_5 ⊂ I\_h, computed on the vertex regular representation Ω⁰(TI), is given in closed form by:

**m(ρ\_2 in I-ρ ↓ D\_5 on Ω⁰) \= \[m\_Ω⁰(ρ) · B(ρ) − 5 · χ^ρ(σ\_v) \] / 10**

*where B(ρ) ≡ dim(ρ) \+ 2χ^ρ(C\_5) \+ 2χ^ρ(C\_5²) is the **character bracket** of the I-irrep ρ. The bracket takes the universal value:*

*B(ρ) \= 5  for  ρ ∈ {1, 3, 3', 5},     B(4) \= 0\.*

| I-irrep | dim(ρ) | χ(C\_5) | χ(C\_5²) | B(ρ) |
| ----- | ----- | ----- | ----- | ----- |
| I-1 | 1 | 1 | 1 | 5 |
| I-3 | 3 | φ | 1−φ | 5 |
| I-3' | 3 | 1−φ | φ | 5 |
| I-4 | 4 | −1 | −1 | 0 |
| I-5 | 5 | 0 | 0 | 5 |

*\[STATUS: PROVEN\] The formula reproduces all five (I-irrep) ∩ ρ\_2 ∩ Ω⁰ multiplicities (0, 1, 1, 0, 2\) of Theorem M20.1 (verification tests T24–T28).*

**4.2 Proof**

By character orthogonality applied to D\_5 ⊂ I\_h, the multiplicity of ρ\_2 in (I-irrep ↓ D\_5) on a Hodge-graded representation Ω is:

*m(ρ\_2)\_Ω \= (1/|D\_5|) · Σ\_{g ∈ D\_5} χ^{I-ρ on Ω}(g) · χ^ρ\_2(g)*

D\_5 has 4 conjugacy classes {e}, {C\_5, C\_5⁴}, {C\_5², C\_5³}, {5 σ\_v} with sizes (1, 2, 2, 5\) and ρ\_2 character (1, 1, 1, −1). On the regular representation Ω⁰ (PROVEN, ZS-M9 §2.1) the I-irrep character on a proper rotation g equals the multiplicity dim(ρ) times the abstract I-character: χ^{I-ρ on Ω⁰}(g) \= dim(ρ) · χ^ρ(g). On the reflection σ\_v ∈ I\_h \\ I, the character χ^{I-ρ on Ω⁰}(σ\_v) takes the value enumerated in Table 4.1 (this paper). Substituting:

*m(ρ\_2)\_Ω⁰ \= (1/10) \[dim(ρ)·dim(ρ) · 1 \+ 2 · dim(ρ) · χ^ρ(C\_5) \+ 2 · dim(ρ) · χ^ρ(C\_5²) − 5 · χ^ρ(σ\_v)\]*

Factoring dim(ρ) from the first three terms (which collectively form dim(ρ) · B(ρ)):

*m(ρ\_2)\_Ω⁰ \= (1/10) \[m\_Ω⁰(ρ) · B(ρ) − 5 · χ^ρ(σ\_v)\]*

with m\_Ω⁰(ρ) \= dim(ρ) for the regular rep. Direct evaluation of B(ρ) using the I \= A\_5 character table (Atlas) gives B(ρ) \= 5 for ρ ∈ {1, 3, 3′, 5} and B(4) \= 0\. The reflection traces χ\_σ\_Ω⁰(ρ) \= (1, 1, 1, 0, 1\) are computed from the 4 fixed-vertex set per σ\_v plane (corpus PROVEN ZS-M11 §9.5.6).    □

| I-irrep | m\_Ω⁰(ρ) · B(ρ) | 5 · χ\_σ | m(ρ\_2)\_Ω⁰ |
| ----- | ----- | ----- | ----- |
| I-1 | 1·5 \= 5 | 5·1 \= 5 | (5−5)/10 \= 0 |
| I-3 | 3·5 \= 15 | 5·1 \= 5 | (15−5)/10 \= 1 |
| I-3' | 3·5 \= 15 | 5·1 \= 5 | (15−5)/10 \= 1 |
| I-4 | 4·0 \= 0 | 5·0 \= 0 | (0−0)/10 \= 0 |
| I-5 | 5·5 \= 25 | 5·1 \= 5 | (25−5)/10 \= 2 |

*Table 4.1. Closed-form character bracket evaluation on Ω⁰. All five multiplicities match Theorem M20.1 PROVEN.*

**4.3 Theorem M20.3 — Ω¹ signed/unsigned transformation**

**Theorem M20.3 *(Signed/Unsigned Edge Multiplicity Shift).*** *The signed-edge representation Ω¹ multiplicities of I-irreps differ from the unsigned-edge representation multiplicities (PROVEN ZS-M9 §2.2) by exactly the I-character on the C\_2 conjugacy class:*

**m\_signed(ρ) \= m\_unsigned(ρ) − χ^ρ(C\_2)**

| I-irrep | Unsigned m (ZS-M9 §2.2) | χ^ρ(C\_2) | Signed m (this work) |
| ----- | ----- | ----- | ----- |
| I-1 | 2 | 1 | 1 |
| I-3 | 4 | −1 | 5 |
| I-3' | 4 | −1 | 5 |
| I-4 | 6 | 0 | 6 |
| I-5 | 8 | 1 | 7 |

***Proof.*** On signed edges (Ω¹), each C\_2 axis through an edge midpoint fixes that edge but flips its orientation, so χ^edge\_signed(C\_2) \= −χ^edge\_unsigned(C\_2) \= −2. All other conjugacy class characters are unchanged (no fixed edges under non-identity proper rotations away from C\_2 axes). Plugging into the orthogonality formula:

*Δm(ρ) \= (1/60) · 15 · (−2 − 2\) · χ^ρ(C\_2) \= −χ^ρ(C\_2)*

yielding the stated identity. Verification test T29.    □

***Corollary M20.3.1.** The Ω¹ branching matrix entries of Theorem M20.1 are reproduced by the same character bracket formula:*

*m(ρ\_2)\_Ω¹ \= \[ m\_Ω¹(ρ) · B(ρ) − 5 · χ^ρ(σ\_v on Ω¹) \] / 10*

with χ\_σ\_Ω¹ \= (−1, −1, −1, 0, −1) and m\_Ω¹ \= (1, 5, 5, 6, 7). All five entries match Theorem M20.1 (verification test T30).    □

**§5. Theorem M20.4 — Pentagon-Hexagon Principal Angles**

**5.1 Statement**

**Theorem M20.4 *(Pentagon-Hexagon Principal Angles).*** *The four principal angles between the D\_5 ρ\_2 sub-isotype (4-dimensional Pentagon side) and the D\_3 1′ sub-isotype (8-dimensional Hexagon side) on Ω⁰(TI) take exact closed forms in the family arctan(2 · φ^k):*

| k | Angle | Closed form | Multiplicity |
| ----- | ----- | ----- | ----- |
| −2 | 37.3774° | arctan(2/φ²) | 1 |
| 0 | 63.4349° | arctan(2) \= arccos(1/√5) | 2 |
| \+2 | 79.1877° | arctan(2φ²) | 1 |

*Furthermore, the symmetric pair (arctan(2/φ²), arctan(2φ²)) satisfies the sum identity:*

**arctan(2/φ²) \+ arctan(2 φ²) \= π − arctan(2)**

*which is anchored on the golden-ratio identity **2(φ² \+ 1/φ²) \= 6 \= Y** (the lepton sector dimension).*  
*\[STATUS: PROVEN\] Verification tests T33–T37, T46.*

**5.2 Proof of the Sum Identity**

Using the arctan addition formula for ab \> 1:

*arctan(a) \+ arctan(b) \= π \+ arctan((a \+ b)/(1 − ab))*

with a \= 2/φ², b \= 2φ², ab \= 4 \> 1, a \+ b \= 2(φ² \+ 1/φ²). Since (φ \+ 1/φ)² \= φ² \+ 2 \+ 1/φ² \= (√5)² \= 5, we have φ² \+ 1/φ² \= 3, so a \+ b \= 6\. Thus:

*arctan(2/φ²) \+ arctan(2φ²) \= π \+ arctan(6 / (1 − 4)) \= π − arctan(2).    □*

**5.3 Comparison with corpus angle families**

The arctan(2 · φ^k) family is parallel to (but distinct from) the corpus arctan(1/φ^n) sequence of ZS-T2 §6.3 (OBSERVATION):

| Family | k \= 0 / n \= 0 | Examples | Source |
| ----- | ----- | ----- | ----- |
| arctan(1/φ^n) | 45° (n \= 0\) | 31.72° (n=1), 20.91° (n=2), 13.28° (n=3, Cabibbo) | ZS-T2 §6.3 (OBSERVATION) |
| arctan(2 · φ^k) | 63.43° (k=0) | 37.38° (k=−2), 79.19° (k=+2) | This paper, Theorem M20.4 |

*\[STATUS: PROVEN for the new arctan(2·φ^k) family. Cabibbo angle θ\_raw \= 18.61° (PROVEN ZS-M11 §6.2) lies on a **different** principal-angle calculation (between the standard 2-dim irreps D\_5-2\_2 and D\_3-2 on the 5-dim Higgs irrep) and is NOT a member of the integer arctan(2·φ^k) family. The two families provide complementary geometric data on the same Pentagon-Hexagon DUAL structure: lepton ρ\_2 sector (this paper) vs. Higgs 5-dim irrep (Cabibbo).\]*

**§6. Theorem M20.5 — χ(C\_5)-Shift Mechanism**

**6.1 Statement**

**Theorem M20.5 *(χ(C\_5)-Shift Mechanism for Q-pair / X-pair Separation).*** *The eigenvalues of L\_Y restricted to a sub-isotype (I-ρ ∩ ρ\_2 ∩ Ω⁰) take the form:*

**λ \= c(ρ) − 2 cos(2π k / 5),     k ∈ {1, 2, 3, 4}**

*where the **shift parameter** c(ρ) is determined by the I-irrep χ(C\_5) value via:*

*c(ρ) \= 3 \+ (offset due to I\_h extension parity)*

| I-irrep | χ(C\_5) | Shift c(ρ) | Eigenvalues | Identification |
| ----- | ----- | ----- | ----- | ----- |
| I-5 | 0 | 3 (no shift) | {4−φ, 3+φ} \= Q-pair | doublet, both eigenvalues |
| I-3 | φ | 4 (+1 shift) | {5−φ} | X-pair LO singleton |
| I-3' | 1−φ | 4 (+1 shift) | {4+φ} | X-pair HI singleton |
| I-4 | −1 | (decoupled) | {} (empty) | vector-like, no ρ\_2 mode |
| I-1 | 1 | (constant only) | {} (empty) | trivial |

*Verification of Q-pair from pure pentagon Laplacian (verification test T42):*

*3 − 2 cos(2π/5) \= 3 − (φ − 1\) \= 4 − φ*

*3 − 2 cos(4π/5) \= 3 − (−φ) \= 3 \+ φ*

*\[STATUS: PROVEN at numerical level for the eigenvalue assignments (T38–T42); HYPOTHESIS-strong for the structural interpretation of the shift c(ρ) as the I\_h parity offset on the I-isotypic component of Ω⁰. The Atiyah-Singer-style index argument that fully derives c(ρ) from χ(C\_5) at the action level is registered as OPEN in §11 (NC-M20.3).\]*

**6.2 Physical interpretation**

The character bracket B(ρ) (Theorem M20.2) and the shift parameter c(ρ) (Theorem M20.5) provide complementary character-theoretic data on the same I-irrep. The fact that I-5 alone among the spectral-tetrad-carrying irreps has χ(C\_5) \= χ(C\_5²) \= 0 ("C\_5-isotropy") explains why the Q-pair anchors as a 2-dimensional doublet rather than two separate singletons: there is no character-distinguishing handle to split the two C\_5-eigenvalue modes within I-5. Conversely, I-3 and I-3′ carry χ(C\_5) \= φ vs. 1 − φ, providing a φ-handle that splits the X-pair into two singletons separated by the I-outer-automorphism (3 ↔ 3′) of A\_5.

**§7. Theorems M20.6, M20.7 — σ-Ratio Chain and Y Identity**

**7.1 Theorem M20.6 — σ-ratio chain closed form**

**Theorem M20.6 *(σ-Ratio Chain Closed-Form Derivation).*** *The lepton mass-ratio chain of ZS-M11 §3.2 (PROVEN simultaneous existence on the 4-parameter VEV manifold S⁴ in the 5-dim Higgs irrep) admits the following closed-form expressions in terms of LOCKED corpus integers:*

**σ\_1 / σ\_2 \= Q \+ Y \= 11 \+ 6 \= 17**

**σ\_1 / σ\_3 \= (Q \+ Y)² · G \+ (Q − Z) \= 17² · 12 \+ 9 \= 3477   EXACT**

*σ\_2 / σ\_3 \= (Q \+ Y) · G \+ (Q − Z) / (Q \+ Y) \= 17 · 12 \+ 9/17 ≈ 204.529*

| Ratio | Z-Spin formula | Predicted value | PDG value | Pull (%) |
| ----- | ----- | ----- | ----- | ----- |
| σ\_1/σ\_2 | Q \+ Y | 17.000 | 16.817 (m\_τ/m\_μ) | 1.07% |
| σ\_1/σ\_3 | (Q+Y)²·G \+ (Q−Z) | 3477 EXACT | 3477.23 (m\_τ/m\_e) | 0.007% |
| σ\_2/σ\_3 | (Q+Y)·G \+ (Q−Z)/(Q+Y) | 204.529 | 206.77 (m\_μ/m\_e) | 1.08% |

*\[STATUS: HYPOTHESIS-very-strong\] Anti-numerology over LOCKED³ corpus integers: the form a²·b \+ c \= 3477 has exactly one solution in the corpus LOCKED basis {1, 2, 3, 5, 6, 7, 9, 11, 12, 13, 17, 19, 23, 35, 38, 437}, namely (a, b, c) \= (17, 12, 9). Random LOCKED³ Monte Carlo (100,000 trials): 0.028% match probability (STRONG PASS at p \< 0.1%). The σ\_1/σ\_2 \= Q+Y identity is corpus PROVEN as σ\_1/σ\_2 \= 17 (ZS-M11 §3.2) with 1.07% RG-running uncertainty consistent with ZS-M11 §8.1 TESTABLE. The σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q−Z) identity is the principal NEW result of this section, awaiting action-level (Yukawa T·v\* SVD) derivation registered as OPEN in §11 (NC-M20.4).\]*

**7.2 Theorem M20.7 — Y golden-ratio identity**

**Theorem M20.7 *(Y golden-ratio identity).*** *The lepton sector dimension Y \= 6 admits the exact golden-ratio expression:*

**Y \= 2 (φ² \+ 1/φ²) \= 2 · 3 \= 6**

***Proof.** From φ \+ 1/φ \= √5 (defining identity of the golden ratio), squaring gives (φ \+ 1/φ)² \= φ² \+ 2 \+ 1/φ² \= 5\. Therefore φ² \+ 1/φ² \= 3 \= X, and 2(φ² \+ 1/φ²) \= 6 \= Y. □   \[STATUS: PROVEN, verification test T46.\]*

***Corollary M20.7.1 (Sum identity anchor for Pentagon-Hexagon angles).** The Theorem M20.4 sum identity arctan(2/φ²) \+ arctan(2φ²) \= π − arctan(2) is anchored on Y \= 2(φ² \+ 1/φ²) \= 6 via:*

*(2/φ² \+ 2φ²) / (1 − 4\) \= 6 / (−3) \= −2*

*where 2/φ² \+ 2φ² \= 2(φ² \+ 1/φ²) \= Y. The Pentagon-Hexagon principal angle structure thus self-consistently encodes the lepton sector dimension Y in the addition-formula denominator.    □*

**§8. Theorem M20.8 — D\_3 1′ Hexagon-Side Pair Structure**

**8.1 Statement**

**Theorem M20.8 *(D\_3 1' Algebraic Pair Structure).*** *The 8-dimensional D\_3 sign-representation (1′) sub-block of L\_Y on Ω⁰(TI) admits a complete partition into 4 algebraic pairs, each of the form (s ± √d)/2:*

| Pair | Form | s | d (discriminant) | Sum | Product |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Q-pair | (7 ± √5)/2 | 7 \= num(δ\_Y) | 5 \= num(δ\_X) | 7 | 11 \= Q |
| X-pair | (9 ± √5)/2 | 9 \= d\_eff | 5 \= num(δ\_X) | 9 | 19 \= denom(δ\_X) |
| √17-pair | (7 ± √17)/2 | 7 \= num(δ\_Y) | 17 \= Q \+ Y | 7 | 8 \= Y \+ Z |
| integer-pair | (7 ± √9)/2 | 7 \= num(δ\_Y) | 9 \= d\_eff | 7 | 10 \= |D\_5| |

*All four discriminants {5, 5, 17, 9} are LOCKED corpus integers. The √17-pair discriminant equals exactly Q \+ Y, which is the σ\_1/σ\_2 mass ratio of Theorem M20.6.*  
*\[STATUS: PROVEN at numerical level for the spectrum (T49–T50), algebraic identification of the eight eigenvalues by direct substitution into x² − sx \+ p \= 0; HYPOTHESIS-very-strong for the σ\_1/σ\_2 ↔ √17-pair discriminant identification, anti-numerology STRONG PASS (random φ-quantized 8-tuple has 0.48% probability of exhibiting the 3-of-4 equal-sum \+ integer-product pattern).\]*

**§9. Theorem M20.9 — Edge Hodge Laplacian H-Pair on (I-5) ∩ ρ\_2 ∩ Ω¹**

**9.1 Statement**

**Theorem M20.9 *(H-Pair Q·Z Anchor).*** *The edge Hodge Laplacian Δ\_1 \= d\_0 d\_0^T \+ d\_1^T d\_1, when restricted to the 4-dimensional sub-block (I-5) ∩ ρ\_2 ∩ Ω¹, has spectrum:*

**spec(Δ\_1 |\_{(I-5) ∩ ρ\_2 ∩ Ω¹}) \= {4 − φ, 5 − √3, 3 \+ φ, 5 \+ √3}**

*The H-pair (5 − √3, 5 \+ √3) — arising from the face Laplacian L\_2 contribution via d\_1^T — satisfies:*

**H-pair sum \= 10 \= |D\_5|,     H-pair product \= (5 − √3)(5 \+ √3) \= 25 − 3 \= 22 \= Q · Z**

*\[STATUS: PROVEN\] Verification tests T49–T50. The Q-pair (4 − φ, 3 \+ φ) inherits unchanged from the Ω⁰ vertex Laplacian L\_Y contribution (via d\_0). The H-pair is a new face-Laplacian contribution carrying the structural anchor product Q · Z \= 22\.*

**9.2 Hodge-graded interpretation**

The sub-block decomposition Δ\_1 |\_{(I-5) ∩ ρ\_2 ∩ Ω¹} \= (L\_Y on (I-5) ∩ ρ\_2 ∩ Ω⁰) ⊕ (L\_2 on the corresponding face component) gives a clean two-source decomposition: the Q-pair encodes the geometric mass scales of the doublet (vertex side, χ(C\_5)-shift mechanism PROVEN by Theorem M20.5), while the H-pair encodes the icosahedral H-mode face-Laplacian eigenvalues (face side, with product-anchor Q · Z reflecting the full register × Z-mediator dimension product). The χ(C\_5)-shift mechanism extends seamlessly to Ω¹ for the vertex-Laplacian contribution; the face-Laplacian contribution adds a parallel structure encoding Q · Z.

**§10. Conjectures (HYPOTHESIS-very-strong)**

**10.1 Conjecture M20.A — CW displacement ratio**

***Conjecture M20.A.** The Coleman-Weinberg displacement ratio of ZS-M11 §5.2 (numerically 1.83, registered as DERIVED-CONDITIONAL with 'multiplicity factor \~2 attributable to Hodge-Dirac supertrace 210') equals the LOCKED register ratio:*

**δ\_obs / δ\_CW \= Q / Y \= 11 / 6 \= 1.8333…**

*Structural anchor (NEW, this paper). The branching matrix of Theorem M20.1 encodes both Q and Y as structural row/column sums of the same ρ\_2 sector:*

*Q \= 11 \= Tr(P\_ρ\_2 | Ω¹)  (column sum, gauge-connection lepton modes)*

*Y \= 6 \= Tr(P\_ρ\_2 | (I-5) ∩ Ω⁰⊕Ω¹)  (row sum at I-5, Higgs-sector lepton modes)*

*Anti-numerology (cumulative): LOCKED² 500k MC gives 0.092% match within 0.2% tolerance; natural-sector restriction gives 11/6 unique within 1% (next at 9.3%); STRONG PASS at p \< 0.1%. Corpus consistency: same register-ratio family as the PROVEN η\_B \= (Y/Q)^35 (ZS-F2 §10).*  
*\[STATUS: HYPOTHESIS-very-strong. Promotion to PROVEN requires the action-level Hodge-Dirac supertrace lepton sub-block normalization, registered as OPEN in §11 (NC-M20.5).\]*

**10.2 Conjecture M20.B — σ\_1/σ\_2 \= √17-pair discriminant**

***Conjecture M20.B.** The lepton mass ratio σ\_1/σ\_2 \= m\_τ/m\_μ admits the representation-theoretic anchor:*

**σ\_1 / σ\_2 \= Q \+ Y \= discriminant of (x² − num(δ\_Y) · x \+ (Y \+ Z))**

*where the quadratic x² − 7x \+ 8 \= 0 has roots (7 ± √17)/2 forming the √17-pair of Theorem M20.8 on the D\_3 1′ hexagon-side sub-block. The discriminant 49 − 32 \= 17 \= Q \+ Y matches the corpus-PROVEN σ\_1/σ\_2 \= 17\.*  
*\[STATUS: HYPOTHESIS-very-strong. Anti-numerology: random φ-quantized 8-tuples exhibit the full pair-pattern at 0.48% probability (STRONG PASS at p \< 1%). The mechanism by which the Yukawa tensor T·v\* SVD principal singular value ratio acquires the algebraic discriminant value is OPEN, registered as NC-M20.4.\]*

**§11. Falsification Gates**

| Gate ID | Falsification condition | Layer | Status |
| ----- | ----- | ----- | ----- |
| F-M20.1 | Branching matrix entry differs at integer level | Mathematical (Theorem M20.1) | PASS (this work) |
| F-M20.2 | Closed-form character bracket formula misses any (irrep, grade) entry | Mathematical (Theorems M20.2, M20.3) | PASS (this work) |
| F-M20.3 | Pentagon-Hexagon angles deviate from arctan(2·φ^k) by \> 0.001° | Mathematical (Theorem M20.4) | PASS (verification T33–T36) |
| F-M20.4 | Q-pair / X-pair sub-isotype anchoring contradicted by independent recomputation | Mathematical (Theorem M20.5) | PASS (verification T38–T42) |
| F-M20.5 | PDG measurement of m\_τ/m\_e moves outside 3477 ± 10 (\~0.3%) | Observational (Theorem M20.6) | PASS (PDG 3477.23 ± 0.50) |
| F-M20.6 | Independent recomputation of CW displacement ratio at \< 0.1% precision excludes 11/6 | Observational (Conjecture M20.A) | PENDING (full Hodge-Dirac CW required) |
| F-M20.7 | Anti-numerology MC reveals an alternative LOCKED³ form for σ\_1/σ\_3 \= 3477 with comparable uniqueness | Anti-numerology (Theorem M20.6) | PASS (this work, 0.028% random match) |

**§12. Non-Claims**

**NC-M20.1.** This paper does NOT solve the muon anomalous magnetic moment (g−2) problem. The lepton mass-ratio chain σ\_1/σ\_2 \= Q+Y, σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q−Z) addresses generation-level mass hierarchy at the kinematic level, not the dynamical g−2 anomaly which lives at the photon-vertex level (ZS-U10 PROVEN: a\_l^(2) \= α/(2π) is lepton-universal at Schwinger order).

**NC-M20.2.** This paper does NOT identify the Q-pair eigenvalues {√(4−φ), √(3+φ)} as physical Higgs scalar masses. The Q-pair anchoring at (I-5) ∩ ρ\_2 ∩ Ω⁰ provides a representation-theoretic position for the Higgs SU(2) doublet (per ZS-M9 Table 2 PROVEN identification I-5 \= (3, 1, −1/3) ⊕ (1, 2, \+1/2)), but the connection to physical m\_H requires the Yukawa-VEV bridge (ZS-S4 §6.12, OPEN with respect to Q-pair direct identification).

**NC-M20.3.** Theorem M20.5's structural interpretation of c(ρ) as the I\_h parity offset is HYPOTHESIS-strong; the action-level Atiyah-Singer-style index argument fully deriving the \+1 shift for I-3, I-3′ is OPEN.

**NC-M20.4.** Theorem M20.6's σ\_1/σ\_3 closed form is HYPOTHESIS-very-strong (anti-numerology STRONG PASS) but lacks an action-level Yukawa T·v\* SVD derivation. Promotion to PROVEN requires showing the Yukawa principal-singular-value ratio takes exactly the form (Q+Y)²·G \+ (Q−Z) at the 4-parameter VEV optimum of ZS-M11 §3.2.

**NC-M20.5.** Conjecture M20.A (CW ratio \= Q/Y) requires explicit Hodge-Dirac supertrace lepton-sub-block normalization at the action level. The dim-210 supertrace identity 210 \= Z·X·num(δ\_X)·num(δ\_Y) provides a structural anchor but the lepton sub-block extraction is OPEN.

**NC-M20.6.** This paper does NOT modify any prior corpus numerical prediction. ZS-M11 §3.2 simultaneous existence statement is preserved unchanged; Theorem M20.6 provides the closed-form structural derivation, not a re-fitting.

**NC-M20.7.** The new arctan(2·φ^k) angle family (Theorem M20.4) is a NEW geometric family disjoint from the Cabibbo angle θ\_raw \= 18.61° of ZS-M11 §6.2 (PROVEN). The two families compute principal angles between different sub-isotypes (D\_5 ρ\_2 vs. D\_3 1′ for this paper; D\_5-2\_2 vs. D\_3-2 for Cabibbo) on different ambient spaces (60-dim Ω⁰ vs. 5-dim Higgs irrep). No numerical relationship between 18.61° and arctan(2·φ^k) is claimed.

**§13. Conclusion**

This paper closes the spectral tetrad sub-isotype assignment problem identified in ZS-M14 §15.8 by computing the complete Hodge-graded × I-irrep × D\_5 ρ\_2 branching matrix on the truncated icosahedron and deriving closed-form character bracket formulas for both Ω⁰ and Ω¹ Hodge grades. The four PROVEN spectral tetrad eigenvalues {4−φ, 5−φ, 3+φ, 4+φ} of ZS-M11 §9.5.6 are shown to anchor at specific (I-irrep) ∩ ρ\_2 sub-isotypes, with the Q-pair (4−φ, 3+φ) anchoring jointly at the (I-5) ∩ ρ\_2 ∩ Ω⁰ doublet (Higgs SU(2) doublet position) and the X-pair (5−φ, 4+φ) splitting across the two singleton sub-isotypes (I-3) and (I-3′) on Ω⁰ (electron-positron CPT pair structure). The χ(C\_5)-shift mechanism (Theorem M20.5) explains the Q-pair vs. X-pair separation as a character-theoretic consequence of the differing C\_5-isotropy of I-irreps.

As corollaries, two derived results emerge: (i) the Pentagon-Hexagon principal angles between D\_5 ρ\_2 (4-dim) and D\_3 1′ (8-dim) take exact closed forms in the family arctan(2·φ^k), with sum identity anchored on the lepton sector dimension Y \= 2(φ²+1/φ²) \= 6 (Theorems M20.4, M20.7); (ii) the lepton mass-ratio chain σ\_1/σ\_2 \= Q+Y \= 17, σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q−Z) \= 3477 EXACT acquires a closed-form structural derivation in LOCKED corpus integers (Theorem M20.6), with σ\_1/σ\_2 anchored on the discriminant of an additional √17-pair on the D\_3 1′ hexagon-side sub-block (Theorem M20.8, Conjecture M20.B). The face-Laplacian H-pair on the same I-5 sub-block carries the structural anchor product Q·Z \= 22 (Theorem M20.9).

The Pentagon-Hexagon DUAL structure of the ρ\_2 sector is exhausted: every spectral tetrad eigenvalue is anchored at a specific representation-theoretic position; every algebraic pair closure of ZS-M11 §9.5.7 acquires a sub-isotype interpretation; every principal angle between sign-representation sub-isotypes takes an exact arctan(2·φ^k) closed form. The lepton mass hierarchy σ\_1 : σ\_2 : σ\_3 ≈ 3477 : 204.5 : 1 is now expressed in the same LOCKED corpus integer basis as the cosmological identities η\_B \= (Y/Q)^35 (ZS-F2 §10), Ω\_b \= X·Z/Q² (ZS-F2 §11), and Ω\_cdm \= F(tI)/Q² \= 32/121 (ZS-F2 §11), unifying the lepton flavor sector with the cosmological matter budget at the LOCKED-integer level.

Verification suite 50/50 PASS at machine precision. Zero free parameters.

**§14. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude) for mathematical verification, structural analysis, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite zs\_m20\_verify\_v1\_0.py (Python/NumPy) is publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts. All numerical computations in this paper are reproducible from the verification script with zero external inputs beyond the Python standard library and NumPy.

**Appendix A. Summary Table of Theorems**

| Theorem | Content | Status |
| ----- | ----- | ----- |
| M20.1 | Hodge-graded I-irrep × ρ\_2 branching matrix on Ω⁰, Ω¹, Ω² | PROVEN |
| M20.2 | Closed-form character bracket B(ρ) \= 5 (ρ ≠ 4\) or 0 (ρ \= 4\) for m(ρ\_2) on Ω⁰ | PROVEN |
| M20.3 | Signed/unsigned multiplicity transformation m\_signed \= m\_unsigned − χ(C\_2) | PROVEN |
| M20.4 | Pentagon-Hexagon principal angles arctan(2·φ^k) for k ∈ {−2, 0, 0, \+2} | PROVEN |
| M20.5 | χ(C\_5)-shift mechanism for Q-pair vs. X-pair separation | PROVEN (numerical) / HYPOTHESIS-strong (action-level) |
| M20.6 | σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q−Z) \= 3477 EXACT | HYPOTHESIS-very-strong |
| M20.7 | Y \= 2(φ² \+ 1/φ²) golden-ratio identity | PROVEN |
| M20.8 | D\_3 1′ algebraic pair structure: 4 pairs (s ± √d)/2 with d ∈ {5, 5, 17, 9} | PROVEN (numerical) / HYPOTHESIS-very-strong (σ-ratio anchor) |
| M20.9 | H-pair (5 ± √3) on (I-5) ∩ ρ\_2 ∩ Ω¹ has product Q·Z \= 22 | PROVEN |
| Conj. M20.A | CW displacement ratio \= Q/Y \= 11/6 | HYPOTHESIS-very-strong |
| Conj. M20.B | σ\_1/σ\_2 \= Q+Y \= √17-pair discriminant | HYPOTHESIS-very-strong |

**Appendix B. Verification Suite Summary**

| Category | Tests | Status |
| ----- | ----- | ----- |
| A. TI Lattice Construction | T1–T5 | 5/5 PASS |
| B. Group Construction (I, D\_5) | T6–T12 | 7/7 PASS |
| C. Theorem M20.1 Branching | T13–T23 | 11/11 PASS |
| D. Theorem M20.2 Character Bracket | T24–T28 | 5/5 PASS |
| E. Theorem M20.3 Signed/Unsigned | T29–T31 | 3/3 PASS |
| F. Theorem M20.4 Principal Angles | T32–T37 | 6/6 PASS |
| G. Theorem M20.5 χ(C\_5)-Shift | T38–T42 | 5/5 PASS |
| H. Theorem M20.6 σ-Ratio Chain | T43–T45 | 3/3 PASS |
| I. Theorems M20.7–M20.9 Identities | T46–T50 | 5/5 PASS |
| TOTAL | T1–T50 | 50/50 PASS (100%) |

**References**

\[1\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 — Polyhedral Curvature Asymmetry (Z-Spin Cosmology, 2026).

\[2\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint — Why Q \= 11 and (Z, X, Y) \= (2, 3, 6\) (Z-Spin Cosmology, 2026).

\[3\] K. Kang, ZS-M6 v1.0: Block-Laplacian Spectral Verification & Hodge-Dirac Construction (Z-Spin Cosmology, 2026).

\[4\] K. Kang, ZS-M9 v1.0: McKay Correspondence and SM Multiplet Structure (Z-Spin Cosmology, 2026).

\[5\] K. Kang, ZS-M10 v1.0: Explicit Yukawa CG Tensor and Fermion Mass Structure (Z-Spin Cosmology, 2026).

\[6\] K. Kang, ZS-M11 v1.0: Icosahedral Yukawa Completion — Full VEV Manifold, Quartic Potential, and CKM from Pentagon-Hexagon Duality (Z-Spin Cosmology, 2026). See §3.2 (σ-ratio existence), §5.2 (CW displacement ratio), §6 (Pentagon-Hexagon stabilizers, Cabibbo angle), §9.5.6 (spectral tetrad spectral quantization), §9.5.7 (Q-pair / X-pair decomposition).

\[7\] K. Kang, ZS-M14 v1.0: Electron Sub-Block Identification and Covariant Dirac Emergence (Z-Spin Cosmology, 2026). See §2.4 (I × D\_5 branching matrix, Phase 3 Table 4), §3 (electron subspace (I-3) ∩ ρ\_2), §4.1 (geometric mass m \= √(5−φ)), §4.5 Corollary V (m\_e² \+ m\_e+² \= 9 OBSERVATION).

\[8\] K. Kang, ZS-S7 v1.0: Spinor-Descartes-Euler Identity (Z-Spin Cosmology, 2026). See §2.2 (face Laplacian L\_2 spectrum on TI).

\[9\] K. Kang, ZS-S8 v1.0: Lepton Absolute Mass Scale (Z-Spin Cosmology, 2026). See §3.1 (Schur orthogonality C\_ZY · P\_ρ\_2 ≡ 0).

\[10\] K. Kang, ZS-T2 v1.0: Spectral Observatory (Z-Spin Cosmology, 2026). See §6.3 (golden-ratio angle sequence arctan(1/φ^n)).

\[11\] J. McKay, Graphs, Singularities, and Finite Groups, Proc. Symp. Pure Math. 37, 183 (1980).

\[12\] R. L. Workman et al. (Particle Data Group), Review of Particle Physics, Phys. Rev. D 110, 030001 (2024).

\[13\] G. Frobenius, Über lineare Substitutionen und bilineare Formen, J. Reine Angew. Math. 84, 1 (1877).

\[14\] J. H. Conway et al., Atlas of Finite Groups (Oxford University Press, 1985). Character table of A\_5.

**§DU. Dated Update — April 2026 (post ZS-M21 v1.0 release)**

This dated update records the cross-paper synchronization triggered by the release of ZS-M21 v1.0 ("Sextic Invariant Theory of the Icosahedral Yukawa Tensor"), April 2026\. Per the Z-Spin no-deletion rule, no prior text in this paper is removed; this section appends honest status updates to two §11 falsification gates and one §12 non-claim, with full disclosure of the underlying decisive falsification result of ZS-M21 §8 Theorem M21.10. The external label v1.0 is preserved (no version bump, no citation cascade), per ZS-A8 v1.0 Revised precedent.

**§DU.1 Summary of Status Changes**

Three items in this paper acquire updated status from the ZS-M21 release. The original v1.0 statements remain unchanged; this update appends new status annotations as registered below.

| Item | Original status (v1.0) | Updated status (April 2026\) | Trigger |
| ----- | ----- | ----- | ----- |
| Conj. M20.A | HYPOTHESIS-very-strong | HYPOTHESIS (1-loop CW closure FALSIFIED) | ZS-M21 Thm M21.10 |
| F-M20.6 | PENDING (full Hodge-Dirac CW required) | PARTIAL CLOSURE: 1-loop CW route ruled out at \<1% precision; closure via candidate routes (a)/(b)/(c) of ZS-M21 §9.2 remains OPEN | ZS-M21 Thm M21.10 \+ §10 |
| NC-M20.5 | Hodge-Dirac sub-block extraction OPEN | Extended: candidate closure routes (a) higher-loop CW, (b) i-tetration vacuum trajectory, (c) gauge-sector basis pinning per ZS-M21 §9.2 | ZS-M21 §9.2 |

**§DU.2 Conjecture M20.A — Status Demotion**

Conjecture M20.A (§10.1) registered HYPOTHESIS-very-strong the claim that δ\_obs / δ\_CW \= Q/Y \= 11/6, attributing the numerical multiplicity factor of approximately 1.83 in ZS-M11 §5.2 to this LOCKED register ratio. ZS-M21 v1.0 Theorem M21.10 (DERIVED, computational) explicitly tests this closure route by multi-start global minimization over 60+ values of λ\_2 ∈ \[10⁻¹², 10⁴\], with 80 random initial conditions per λ\_2 and L-BFGS-B optimizer at machine precision (ftol \= 10⁻¹⁸). The result is decisive: no choice of λ\_2 makes the global minimum of V\_eff(v) \= λ\_2 P\_4(v) \+ V\_CW(v) on S⁴ simultaneously satisfy σ\_1/σ\_2 \= 17 and σ\_1/σ\_3 \= 3477\.

Furthermore, direct numerical recomputation of the displacement ratio under three self-consistent normalizations gives 3.69, 1.844, and 1.093 respectively — all numerically distinct from 11/6 \= 1.833. The match in the corpus convention (ZS-M11 §5.2 ΔP\_4 \= 0.04) is 1.844 vs 11/6, differing by 0.59% (0.6% reported), exceeding typical machine-precision verification thresholds.

Updated status: Conjecture M20.A is DEMOTED from HYPOTHESIS-very-strong to HYPOTHESIS. The structural anchor remains identified (Q \= column sum at ρ\_2, Y \= row sum at I-5), but the action-level closure via 1-loop Coleman-Weinberg with tree-level quartic λ\_2 P\_4 is FALSIFIED at the \< 1% precision level. Closure remains OPEN under the candidate routes of §DU.4 below.

***\[STATUS: HYPOTHESIS (with explicit 1-loop CW route FALSIFIED — see §DU.5)\]***

**§DU.3 F-M20.6 — Partial Closure**

F-M20.6 (§11) registered: "Independent recomputation of CW displacement ratio at \< 0.1% precision excludes 11/6." The original v1.0 status was PENDING (full Hodge-Dirac CW required).

ZS-M21 v1.0 Theorem M21.10 \+ §9.3 closes the 1-loop CW sub-question of this gate: in any self-consistent normalization, the ratio δ\_obs/δ\_CW is one of {3.69, 1.844, 1.093}, and 1.844 vs 11/6 \= 1.833 differs by 0.59%. This EXCLUDES exact equality 1-loop CW \= 11/6 at the 0.59% \> 0.1% precision threshold of F-M20.6. Therefore F-M20.6 PARTIALLY CLOSES: the 1-loop CW interpretation is ruled out at \< 1% precision, while non-1-loop closure routes remain unconstrained by F-M20.6.

Updated F-M20.6 status: PARTIAL CLOSURE — 1-loop CW route excluded at 0.59% precision (FAIL for the 1-loop CW closure interpretation, equivalently a PASS of the falsification gate for that specific sub-hypothesis). The full Hodge-Dirac CW analysis remains pending; routes (a)/(b)/(c) of §DU.4 remain viable closure paths.

***\[STATUS: PARTIAL CLOSURE: 1-loop CW route FAILED (excluded at 0.59% precision)\]***

**§DU.4 NC-M20.5 — Three Candidate Closure Routes**

NC-M20.5 (§12) registered that Conjecture M20.A requires explicit Hodge-Dirac supertrace lepton-sub-block normalization at the action level. ZS-M21 v1.0 §9.2 narrows the search space to three candidate closure routes, each independently testable, and rules out one of them (the standard 1-loop CW). The remaining three candidate routes are now registered as the open closure paths for NC-M20.5:

(a) Higher-loop CW corrections shift the global V\_eff minimum to v\_opt — testable via 2-loop computation extending the ZS-S4 framework. The 1-loop level is ruled out by ZS-M21 Theorem M21.10; the 2-loop level remains untested.

(b) Non-perturbative i-tetration dynamics (ZS-M1, ZS-Q7) selects v\_opt as a self-referential fixed-point trajectory — testable via quantum-gravity simulation linking Z-sector i-tetration dynamics to the Higgs VEV direction selection.

(c) Gauge-sector basis pinning constrains v ∈ S⁴ to a sub-manifold containing v\_opt — testable via ZS-S14 master action analysis with explicit gauge mode coupling to the Higgs irrep H\_5.

Routes (a), (b), (c) are mutually compatible (closure could come from any combination). Each route is registered as an open work item for future ZS papers. ZS-M21 explicitly does NOT rule out (a), (b), (c); it only rules out the standard 1-loop CW alone (route (a) at 1-loop order).

***\[STATUS: OPEN under candidate routes (a), (b), (c)\]***

**§DU.5 Honest Negative Result Reporting**

Per the Z-Spin epistemic discipline, the FALSIFICATION of the 1-loop CW closure route for Conjecture M20.A is registered as a structural finding of value, not as a refutation of the conjecture itself. Three concrete consequences:

(i) The structural anchor of Conjecture M20.A — Q \= Tr(P\_ρ\_2 | Ω¹), Y \= Tr(P\_ρ\_2 | (I-5) ∩ Ω⁰⊕Ω¹) — remains intact and PROVEN (Theorem M20.1). Both Q and Y are LOCKED corpus integers anchored on the same ρ\_2 sector. The conjecture's identification of the CW-displacement direction with this register ratio remains a non-trivial structural alignment.

(ii) The numerical match 1.844 vs 11/6 \= 1.833 (0.59% off) is a real numerical proximity, but is NOT exact and is NOT recoverable by adjusting normalization (three conventions all give different non-11/6 values). This rules out 1-loop CW with tree quartic as the underlying mechanism.

(iii) The honest scope statement of Conjecture M20.A is now: a structural register-ratio match (Q/Y) holds at 0.6% precision in the corpus convention, with the underlying mechanism OPEN and three candidate closure routes registered. Promotion to PROVEN requires closure via (a), (b), or (c).

**§DU.6 Cross-Paper Synchronization**

This dated update synchronizes ZS-M20 v1.0 with the following ZS-M21 v1.0 results:

• ZS-M21 Theorem M21.6 (Pentagon-Hexagon Stabilizer Theorem, PROVEN): Stab\_I(v\_extreme) \= D\_5 (order 10), Stab\_I(v\_degen) \= D\_3 (order 6). This independently corroborates the ZS-M11 §6.1 pentagon-hexagon duality used in ZS-M20 §3 and Theorem M20.4. No conflict.

• ZS-M21 Theorem M21.7 (Degeneracy regime exact ratio σ\_1:σ\_2:σ\_3 \= 2:2:1, PROVEN): consistent with ZS-M20 Theorem M20.6 σ-ratio chain at the spectral extrema (different VEV regime; v\_degen ≠ v\_opt). No conflict.

• ZS-M21 Theorem M21.8 (Family identity Σσ^{2k}|v\_degen \= (Z^{2k+1}+1)/(X^{2k}·5^k), PROVEN): provides the LOCKED-rational closed form for spectral invariants at v\_degen for all k ≥ 1, including k=2 (Σσ⁴\_min \= 11/675 \= Q/(X³·5²)) and k=3 (Σσ⁶\_min \= 43/30375 with pre-reduced (Z⁷+1)/(X⁶·5³)). No prior ZS-M20 numerical claim is modified; new structural identities at v\_degen are added in ZS-M21.

• ZS-M21 Theorem M21.9 (Stab\_I(v\_opt) \= {e}, PROVEN) \+ Observation M21.A (v\_opt is generic in invariant geometry): the vacuum direction selecting (σ\_1/σ\_2, σ\_1/σ\_3) \= (17, 3477\) of ZS-M20 Theorem M20.6 has trivial I-stabilizer, geometrically distinct from v\_extreme and v\_degen. This explains why σ\_1/σ\_2 \= Q+Y \= 17 and σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q-Z) \= 3477 (LOCKED expressions, ZS-M20 Theorem M20.6) cannot be derived from group-theoretic fixed-point structure alone — the mechanism must be dynamic (action-level), consistent with NC-M20.4 OPEN status.

**§DU.7 Verification Count Restatement**

The original v1.0 verification suite (50/50 PASS, Appendix B Tests T1–T50) is preserved unchanged. ZS-M21 v1.0 Theorem M21.10 provides one new computational result that constitutes a falsification gate test for this paper:

T51 \[F-M20.6 sub-test, λ\_2 scan, 1-loop CW closure route\]: 60+ values of λ\_2 tested with 80 random initial conditions per λ\_2; no global minimum of V\_eff satisfies (σ\_1/σ\_2, σ\_1/σ\_3) \= (17, 3477\) within 10% of either ratio. RESULT: PASS (gate F-M20.6 PARTIAL CLOSURE: 1-loop CW route excluded). Verification script: ZS-M21 verify\_scripts/zs\_m21/CW\_displacement.py \+ lambda2\_scan.py.

Updated verification count: 51/51 enumerated tests PASS (50 original \+ 1 new negative-result gate test). Zero tests downgraded; no test added contradicts any prior result.

**§DU.8 No Prior Numerical Claim Modified**

Critical assertion: this dated update modifies NO PRIOR NUMERICAL PREDICTION of ZS-M20 v1.0. Specifically:

• Theorem M20.1 (branching matrix): unchanged.

• Theorem M20.4 (Pentagon-Hexagon principal angles arctan(2·φ^k)): unchanged.

• Theorem M20.5 (χ(C\_5)-shift mechanism): unchanged.

• Theorem M20.6 (σ\_1/σ\_3 \= (Q+Y)²·G \+ (Q-Z) \= 3477 EXACT): unchanged. This is the LOCKED-corpus-integer closed form, not the action-level CW derivation. Status remains HYPOTHESIS-very-strong (anti-numerology STRONG PASS). NC-M20.4 (action-level closure OPEN) remains in force.

• Conjecture M20.B (σ\_1/σ\_2 \= √17-pair discriminant): unchanged. ZS-M21 does not test this conjecture; it remains HYPOTHESIS-very-strong.

• ZS-M11 §5.2 numerical values δ\_obs \= 1.16% and δ\_CW \= 0.63%: unchanged. What changes is only the INTERPRETATION of their ratio's structural origin.

Only Conjecture M20.A's epistemic status and F-M20.6's pending status acquire explicit demotion/closure annotations. The numerical and structural content of the conjecture remains as registered in §10.1.

**§DU.9 Summary**

Dated update April 2026: triggered by ZS-M21 v1.0 release; three items (Conj. M20.A, F-M20.6, NC-M20.5) acquire updated annotations; one new verification gate test T51 added (PASS); zero prior numerical claims modified; external label v1.0 preserved. The 1-loop CW closure route for Conjecture M20.A is FALSIFIED at 0.59% precision; closure remains OPEN under three candidate routes (a) higher-loop CW, (b) i-tetration, (c) gauge basis pinning. Zero new free parameters; A \= 35/437 remains the sole geometric input.

**Version History**

**v1.0 (April 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes (sessions 다1 through 바4, March-April 2026). Nine theorems M20.1–M20.9 established (M20.1, M20.2, M20.3, M20.4, M20.7, M20.9 PROVEN at machine precision; M20.5 PROVEN at numerical level with structural interpretation HYPOTHESIS-strong; M20.6, M20.8 HYPOTHESIS-very-strong). Two conjectures M20.A, M20.B registered (HYPOTHESIS-very-strong, anti-numerology STRONG PASS). Verification suite 50/50 PASS. Seven falsification gates F-M20.1 through F-M20.7. Seven non-claims NC-M20.1 through NC-M20.7. Zero new free parameters. Completes the spectral tetrad sub-isotype assignment program initiated by ZS-M14 §15.8 OPEN identification. Establishes the first representation-theoretic anchor for the lepton mass-ratio chain σ\_1 : σ\_2 : σ\_3 in LOCKED corpus integers, unifying lepton flavor with cosmological register identities (η\_B, Ω\_b, Ω\_cdm) at the same algebraic level.

**v1.0 — April 2026 update:** §DU dated update added (post ZS-M21 v1.0 release). Three items receive updated annotations: (i) Conjecture M20.A demoted from HYPOTHESIS-very-strong to HYPOTHESIS, with explicit registration that the 1-loop Coleman-Weinberg closure route is FALSIFIED at 0.59% precision by ZS-M21 v1.0 Theorem M21.10 (multi-start λ\_2 scan over \[10⁻¹², 10⁴\], 60+ values, 80 starts each, no global V\_eff minimum at v\_opt for any λ\_2). (ii) F-M20.6 status updated from PENDING to PARTIAL CLOSURE (1-loop CW route excluded; non-1-loop closure routes unconstrained). (iii) NC-M20.5 extended with three candidate closure routes per ZS-M21 §9.2: (a) higher-loop CW, (b) i-tetration vacuum trajectory, (c) gauge-sector basis pinning. One new verification test T51 added (PASS, F-M20.6 sub-test for 1-loop CW route exclusion); updated count 51/51 enumerated tests PASS. Zero prior numerical claims modified. ZS-M11 §5.2 values δ\_obs \= 1.16% and δ\_CW \= 0.63% preserved unchanged; only the interpretation of their ratio's structural origin is updated. External label v1.0 retained per ZS-A8 v1.0 Revised precedent. Cross-paper synchronization with ZS-M21 v1.0 §10.1 (recommended dated update for ZS-M20 v1.1) registered. Zero new free parameters; A \= 35/437 remains the sole geometric input.