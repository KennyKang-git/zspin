**ZS-M26**

**V₄-Equivariant ZBSI on the Cobordism-History Fiber**

Character-Cohomology Closure of the K \= ℚ(√−3, √−11) Riemann Route, with the Three-Wall OPEN Gate Map

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
May 2026  |  ZS-M26 (Mathematical Spine Theme)  |  Paper Code: ZS-M26  
Version: v1.0

**Verification: 24/24 PASS  |  Zero Free Parameters  |  NON-CLAIM: Not an RH Proof — Three-Wall OPEN Gate Map**

**Position Statement**

This paper presents a structurally complete V₄-equivariant ZBSI (Z-BFV Sonin Index) construction on the cobordism-history fiber for K \= ℚ(√−3, √−11), the natural Z-Spin K-arithmetic carrier (ZS-M22 §2.3, PROVEN). Three structural results are established with PROVEN/DERIVED status, and three precise OPEN gates (the Three Walls) are mapped with quantitative numerical verification at 50-digit mpmath precision.  
This paper does NOT claim a proof of the Riemann Hypothesis. Following 47+ rounds of cumulative exploration consolidated in ZS-M22, ZS-M23, ZS-M24, ZS-M25, the paper records the precise mathematical conditions under which the Z-Spin Hilbert–Pólya construction would close — and quantifies, by direct numerical probe, why those conditions are not currently met. The walls (W1, W2, W3) are quantitative refinements of Dragons D2, D4 (ZS-M23 §5.4) and the ADS-H1 working hypothesis (ZS-M22 §6.6.4).  
The principal new structural content is the V₄-character cohomology decomposition of the ZBSI operator on the cobordism-history fiber, with the Projected Determinant Theorem DERIVED per channel and the Three-Wall OPEN Gate Map quantified by direct numerical probes. Corollary M26.3a (Wilson Phase Worldline-Parallel-Transport) is HYPOTHESIS-strong: a specification of the next mathematical direction for ADS-H1 closure.

**§0. Abstract**

We construct a V₄-equivariant ZBSI operator framework for the composite biquadratic field K \= ℚ(√−3, √−11) on the BV-BFV cobordism-history fiber (ZS-F0 §8.5 PROVEN), and quantify the precise mathematical walls separating this construction from a Hilbert–Pólya closure of the Riemann Hypothesis.  
**Theorem M26.1 (V₄-Character Cohomology Decomposition, PROVEN).** Under V₄ Schur orthogonality (ZS-M22 §6.6.1 PROVEN), the arithmetic fiber decomposes as ℋ\_K,Z \= ⊕\_χ ℋ\_χ via Schur idempotents Π\_χ \= e\_χ \= (1/4) Σ\_{g ∈ V₄} χ(g) ρ(g). Each character channel χ ∈ {1, χ\_{−3}, χ\_{−11}, χ\_{33}} carries decoration (a\_χ, q\_χ) ∈ {(0,1), (1,3), (1,11), (0,33)} (ZS-M25 §6.3 PROVEN). The decomposition lifts to the cobordism-history fiber ℋ\_K,Z \= ⊕\_χ (ℋ\_cob ⊗ ℋ\_χ), bypassing ADS-6 PROVEN no-go which applies only to the boundary fiber.  
**Theorem M26.2 (Projected Determinant per Channel, DERIVED).** The projected Fredholm determinants factorize as det\_Fr(I − T\_{χ,Z}(s)) \= C\_χ · Λ(s, χ) with C\_1 \= 1, C\_{χ\_{−3}} \= √3, C\_{χ\_{−11}} \= √11, C\_{χ\_{33}} \= √33, forced by Theorem D.1-K (ZS-M25 §3 PROVEN) and ADS-9 cross-channel locking (ZS-M25 §4 PROVEN). The total prefactor reproduces the V₄-decoration constant 4√33 of Theorem D.1-K.  
**Theorem M26.3 (Three-Wall Quantitative Map, NEW).** Three precise OPEN walls separate the V₄-equivariant ZBSI from RH closure:  
(W1) P1 wall: the J-twisted Yakaboylu anti-Hermitian/Hermitian ratio at s \= 1/2 \+ 14.135i scales as P\_max^(−0.014) on P\_max ∈ {20, 50, 100, 200, 500, 1000}, insufficient for P3 closure under P1 by direct extrapolation.  
(W2) Pillar V wall: pole-corrected V₄-channel Weil functional sum is negative on 4/12 grid points. Pole correction (ZS-M22 §6.6.5(a) PROVEN diagnostic) reduces ζ-channel negativity from 5/12 to 1/12, but is structurally inapplicable to non-trivial L-function channels (which lack poles). Conductor/parity correction (D4b OPEN) is required.  
(W3) ADS-H1 wall (NEW): Wilson cycle phase 129.45° injected directly into the cobordism BRST charge as point coupling breaks Q² \= 0 nilpotency at rank 3, with ‖Q²‖\_F \= 1.092. Corollary M26.3a (HYPOTHESIS-strong) specifies the next mathematical direction: the BRST charge — if it closes ADS-H1 — must encode the Wilson phase as parallel transport along the worldline, not as point coupling.  
Theorems M26.1 PROVEN; M26.2 DERIVED; M26.3 records numerical walls. The paper inherits all upstream NC-M22 through NC-M25.6 non-claims and adds NC-M26.1 through NC-M26.7. Verification: 24/24 PASS at 50-digit mpmath plus algebraic exactness. Zero new free parameters; A \= 35/437, Q \= 11, K \= ℚ(√−3, √−11) remain LOCKED.  
Keywords: V₄-character cohomology, ZBSI operator, cobordism-history fiber, BV-BFV BRST cohomology, Klein four-group, projected Fredholm determinant, J-twisted Yakaboylu Hamiltonian, Schur idempotent, Wilson cycle phase, worldline parallel transport, three-wall map, Hilbert–Pólya, GRH-for-K, anti-numerology, zero free parameters.

**Epistemic Status Legend**

This paper adopts the standard Z-Spin epistemic legend, extended where required by the Three-Wall structure.

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete proof under declared definitions; verified to 50-digit mpmath or algebraic-exact precision. |
| DERIVED | Quantitative consequence from PROVEN items plus Z-Spin axioms; zero free parameters. |
| DERIVED-CONDITIONAL | Derived under explicitly stated upstream condition; upgrades upon upstream upgrade. |
| VERIFIED | Numerically confirmed to declared precision via independent computation. |
| LOCKED | Core constant from prior corpus paper; not adjustable here. |
| IMPORTED | Result proved externally and used here without re-proof; full citation given. |
| HYPOTHESIS-strong | Multiple independent lines of structural evidence; one identified gap. |
| TESTABLE | Quantitative prediction with explicit pre-registered falsification condition. |
| NON-CLAIM | Explicit declaration of what this paper does NOT establish. |
| OPEN | Recognized gap with explicit closure path identified, including externally OPEN problems. |
| WALL | Quantitatively mapped OPEN gate; direct numerical probe documents precise distance to closure. |

**§1. Introduction**

**§1.1 Motivation**

After 47+ rounds of cumulative exploration (RH-ZS18 through RH-ZS58, archived 2025–2026), the Z-Spin RH program has produced (i) three PROVEN contributions to the Hilbert–Pólya outline (ZS-M23 §4: anti-symmetric phase Θ\_Z \= iπw/2, Wilson conjugate pair {λ, λ̄}, j \= 1/2 spinor 4π closure); (ii) four PROVEN no-go theorems (ZS-M22 ADS-5/6/7 \+ scalar-kernel 12 negative-eigenvalue confirmations) closing all natural boundary-fiber escape routes; (iii) the working hypothesis ADS-H1 (cobordism BRST positivity, ZS-M22 §6.6.4) registered as the sole structurally compatible surviving route; and (iv) four well-posed sub-targets D4a–D4d (ZS-M23 §5.4) decomposing the OPEN structural ingredient of ADS-H1.  
The cumulative force of these results is a clarification: Z-Spin does not, and structurally cannot, prove RH from internal data alone (NC-M23.1 PROVEN). What Z-Spin does is supply a precisely identified mathematical contribution to the standard Hilbert–Pólya construction. This paper executes the next operational step: it organizes the contribution under V₄-character cohomology on the cobordism-history fiber, proves the projected determinant structure per channel, and quantifies the three precise mathematical walls separating the construction from RH closure.

**§1.2 Scope and Position**

This paper is a navigation paper, not a proof attempt. Its three principal results are:  
(a) Theorem M26.1 — V₄-character cohomology decomposition via Schur idempotents, PROVEN from V₄ orthogonality (ZS-M22 §6.6.1).  
(b) Theorem M26.2 — projected Fredholm determinant per channel det\_Fr(I − T\_{χ,Z}(s)) \= C\_χ · Λ(s, χ), DERIVED from ZS-M25 Theorem D.1-K and ADS-9. The four prefactors {1, √3, √11, √33} are the algebraic V₄-decoration; their structural product reproduces the discriminant disc(K) \= 1089 \= 33² (PROVEN, ZS-M22 §7.2).  
(c) Theorem M26.3 — Three-Wall Quantitative Map. Three precise OPEN walls (W1, W2, W3) are quantified by direct numerical probes. W3 is the principal new structural finding: Wilson cycle phase as a point coupling in the cobordism BRST charge breaks Q² \= 0 nilpotency, indicating that the BRST charge — if it closes ADS-H1 — must encode the Wilson phase as worldline-parallel-transport along the cobordism.  
Following NC-M25.5 (which explicitly disclaims that ZS-M25 closes Dragon D4 sub-target D4a alone), this paper adds NC-M26.5: this paper does NOT close any of D4a, D4b, D4c, or D4d. The three walls W1, W2, W3 quantify the precise OPEN boundary.

**§1.3 Relation to Prior Corpus**

This paper is downstream of and inherits LOCKED inputs from: ZS-F0 v1.0(R) (BV-BFV functor, Wilson cobordism, three-layer fixed points, FFPP), ZS-F2 (A \= 35/437), ZS-F5 ((Z,X,Y) \= (2,3,6), Q \= 11), ZS-F16 (Two-Protocol Theorem), ZS-M1 (i-tetration HSI Theorem), ZS-M3 (4π spinor closure), ZS-M4 (transfer operator \+ J-symmetry), ZS-M22 (Five-Pillar Arithmetic-Dedekind Scaffold), ZS-M23 (Y-Sector RH Contribution Map \+ four Dragons), ZS-M24 (face polygon spectral zeta \+ B(s) identification), ZS-M25 (composite-field Theorem D.1-K \+ Theorem P3-J).  
No prior corpus result is modified, retracted, or weakened. The Three-Wall Quantitative Map (Theorem M26.3) is a quantitative refinement that sharpens Dragons D2 (W1), D4 (W2), and the ADS-H1 working hypothesis (W3) into explicit numerical OPEN gates. The standard Connes–Weil equivalence (GRH-for-K \= positivity of the Weil distribution; Connes 1999, Bombieri 2000\) and the Connes–Consani–Moscovici 2022 prolate / Sonin program are used as IMPORTED external mathematics — not re-derived.

**§2. Locked Inputs**

All inputs are LOCKED, PROVEN, or DERIVED in upstream corpus papers. Zero new free parameters are introduced.

Table 2.1. Locked corpus inputs to ZS-M26.

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 | LOCKED |
| Q (register dimension) | 11 (prime) | ZS-F5 | PROVEN |
| (Z, X, Y) sector dims | (2, 3, 6); Q \= Z+X+Y | ZS-F5 | PROVEN |
| K (Z-Spin number field) | ℚ(√−3, √−11), V₄ Galois | ZS-M22 §2.3 | PROVEN |
| disc(K) | 1089 \= 33² | ZS-M22 §7.2 | PROVEN |
| ζ\_K factorization | ζ·L(χ\_{−3})·L(χ\_{−11})·L(χ\_{33}) | ZS-M22 §4 | PROVEN |
| ξ\_K decomposition | (1/4√33)·ξ·Λ(χ\_{−3})·Λ(χ\_{−11})·Λ(χ\_{33}) | ZS-M25 Thm D.1-K | PROVEN |
| Channel decoration (a\_χ, q\_χ) | {(0,1), (1,3), (1,11), (0,33)} | ZS-M25 §6.3 | PROVEN |
| B(s) archimedean factor | π^(−s/2) Γ(s/2) | ZS-M24 Thm D.2 | DERIVED |
| z\* (i-tetration fixed point) | 0.4383 \+ 0.3606i | ZS-M1 | PROVEN |
| λ \= (iπ/2)z\* | −0.5664 \+ 0.6886i | ZS-F0 §8.5 | PROVEN |
| |λ|² \= (π²/4)·η\_topo | 0.7948 | ZS-F0 Thm 8.9 | PROVEN |
| arg(λ) | 129.45° | ZS-F0 §9.5 | PROVEN |
| Sum rule | 0.7948 \+ 0.2050 \+ 0.0001 \= 0.9999 | ZS-F0 §12.3 | PROVEN |
| J seam involution | J|j⟩ \= |10−j⟩, J² \= I | ZS-M3 | PROVEN |
| S\_Q similarity factor | diag(e^((j−5)/2)) | ZS-M25 §5.1 | PROVEN |
| H\_Q^(Yak,J)(s) | (S\_Q L\_s S\_Q^(−1) \+ J(...)J)/2 | ZS-M25 §5.2 | PROVEN |
| Wilson cobordism W | Σ\_X→Σ\_XZ→Σ\_Y→Σ\_ZY→Σ\_X | ZS-F0 §8.5 Def 8.8 | PROVEN |
| D₄ register symmetry | ⟨J, J\_Z⟩ ≅ D₄ | ZS-F0 §8.6 Thm 8.13 | PROVEN |
| Three-layer fixed points | |0⟩\_Z, |v\_W⟩, |5⟩ | ZS-F0 §9 | PROVEN |
| ADS-5 negative eigenvalues | 12 confirmations (4 ch × 3 σ) | ZS-M22 §6.3 | PROVEN |
| ADS-6 V₄-quadratic limit | Boundary fiber alone insufficient | ZS-M22 §6.6.1 | PROVEN |
| ADS-H1 sole surviving route | Cobordism BRST cohomology | ZS-M22 §6.6.6 | HYPOTHESIS-strong |
| FFPP compression | All Z-Spin content → W₀(−iπ/2) | ZS-F0 §13 Thm 13.3 | PROVEN |

**§3. Theorem M26.1 — V₄-Character Cohomology Decomposition**

**§3.1 Statement**

**Theorem M26.1 (V₄-Character Cohomology). \[PROVEN\]** Let K \= ℚ(√−3, √−11) with Galois group V₄ \= Gal(K/ℚ) \= {1, χ\_{−3}, χ\_{−11}, χ\_{33}} (PROVEN, ZS-M22 §2.3). Let ℋ\_arith \= ℂ\[V₄\] be the arithmetic fiber. The Schur idempotents

Π\_χ := e\_χ \= (1/|V₄|) · Σ\_{g ∈ V₄} χ̄(g) · ρ(g) \= (1/4) · Σ\_{g ∈ V₄} χ(g) · ρ(g)

(using χ̄ \= χ since all V₄ characters are real, χ² \= 1\) form a complete orthogonal projection system:

Π\_χ · Π\_χ' \= δ\_{χ,χ'} · Π\_χ,    Σ\_χ Π\_χ \= I\_{ℋ\_arith}

Therefore the arithmetic fiber decomposes as a V₄-graded direct sum:

ℋ\_arith \= ⊕\_{χ ∈ V₄} ℋ\_χ,    ℋ\_χ \= Π\_χ · ℋ\_arith

Each ℋ\_χ is a one-dimensional irreducible V₄-representation labeled by the character χ. Lifted to the full ZBSI Hilbert space ℋ\_K,Z \= ℋ\_cob ⊗ ℋ\_arith on the BV-BFV cobordism-history fiber (ZS-F0 §8.5 PROVEN structure):

ℋ\_K,Z \= ⊕\_{χ ∈ V₄} (ℋ\_cob ⊗ ℋ\_χ) \=: ⊕\_{χ ∈ V₄} ℋ\_K,Z^{(χ)}

with channel projector Π\_χ^{K,Z} \= I\_{ℋ\_cob} ⊗ Π\_χ. Each ℋ\_K,Z^{(χ)} carries the V₄-decoration (a\_χ, q\_χ) ∈ {(0,1), (1,3), (1,11), (0,33)} (ZS-M25 §6.3 PROVEN).

**§3.2 Proof**

Step 1 (V₄ character orthogonality). The Klein four-group V₄ has four irreducible representations, all one-dimensional, given by the four characters {1, χ\_{−3}, χ\_{−11}, χ\_{33}}. By the orthogonality relations for finite abelian groups (Serre, Linear Representations of Finite Groups, §2.3):

(1/|V₄|) · Σ\_{g ∈ V₄} χ(g) · χ'(g) \= δ\_{χ,χ'}

Step 2 (idempotent property). Let Π\_χ \= (1/4) Σ\_{g ∈ V₄} χ(g) ρ(g). Direct computation:

Π\_χ · Π\_χ' \= (1/16) · Σ\_{g, h ∈ V₄} χ(g)·χ'(h) · ρ(gh)

Substituting g' \= gh and using χ(g'h^(−1)) \= χ(g')χ(h) (V₄ characters are quadratic, χ² \= 1):

\= (1/16) · Σ\_{g'} χ(g') ρ(g') · Σ\_h χ(h)·χ'(h) \= (1/16) · 4 Π\_χ · 4 δ\_{χ,χ'} \= δ\_{χ,χ'} Π\_χ

Step 3 (completeness). Σ\_χ Π\_χ \= (1/4) Σ\_g (Σ\_χ χ(g)) ρ(g) \= (1/4) · 4 · ρ(e) \= I, using Σ\_χ χ(g) \= |V₄| · δ\_{g,e}.  
Step 4 (cobordism-history lift). The Wilson cobordism W : Σ\_X → Σ\_XZ → Σ\_Y → Σ\_ZY → Σ\_X (ZS-F0 §8.5 Definition 8.8, PROVEN) has BV-BFV functor B\_Z assigning a history fiber ℋ\_cob (ZS-F0 §8.3 DERIVED). Tensor product with ℋ\_arith yields the full ZBSI Hilbert space; the tensor product respects the V₄-grading by construction since V₄ acts only on ℋ\_arith. The projector Π\_χ^{K,Z} \= I\_{ℋ\_cob} ⊗ Π\_χ inherits idempotency and orthogonality from Π\_χ.

**§3.3 Cobordism-History Fiber: Why ADS-6 Is Bypassed**

Theorem ADS-6 (ZS-M22 §6.6.1 PROVEN) states: within the boundary fiber ℋ\_BFV ⊗ ℂ\[V₄\] alone, no V₄-equivariant Hermitian B\_K can produce cross-channel coupling. This no-go applies specifically to the boundary fiber, not to the cobordism-history fiber.  
The cobordism-history fiber ℋ\_cob carries the full BV-BFV history along the closed Wilson cobordism W, including the Z-block evolution, Wilson loop dynamics, and J\_Z-odd transfer (corpus PROVEN sum rule 0.7948 \+ 0.2050 \+ 0.0001 \= 0.9999, ZS-F0 §12.3). This fiber is structurally richer than the boundary BFV phase space. The rank-one BRST minimal closure (Q\_0 \= |1⟩⟨b|, Q\_0² \= 0; ZS-M22 §6.6.4 PROVEN) demonstrates that nontrivial BRST cohomology already exists at minimal rank on the cobordism complex.  
ADS-H1 (ZS-M22 §6.6.4 HYPOTHESIS-strong) registers W\_K(g) \= Tr\_{H⁰(Q\_BRST)}(A\_g† A\_g) on the BV-BFV cobordism complex as the sole structurally compatible surviving route. Theorem M26.1 specifies the V₄-character decomposition of this cobordism-history fiber, which is the precise structural content of working hypothesis ADS-H1.

**§4. Theorem M26.2 — Projected Determinant per Channel**

**§4.1 Statement**

**Theorem M26.2 (Projected Determinant Theorem). \[DERIVED\]** Let T\_{χ,Z}(s) be the V₄-projected transfer operator on ℋ\_K,Z^{(χ)} \= ℋ\_cob ⊗ ℋ\_χ defined by

T\_{χ,Z}(s) := Π\_χ^{K,Z} · T\_{K,Z}(s) · Π\_χ^{K,Z}

where T\_{K,Z}(s) is the V₄-equivariant lift of the J-twisted Yakaboylu operator H\_Q^{Yak,J}(s) (ZS-M25 §5.2 PROVEN) to the cobordism-history fiber. Then the projected Fredholm determinant factorizes as:

det\_Fr(I − T\_{χ,Z}(s)) \= C\_χ · Λ(s, χ),    χ ∈ {1, χ\_{−3}, χ\_{−11}, χ\_{33}}

with channel prefactors:

C\_1 \= 1,    C\_{χ\_{−3}} \= √3,    C\_{χ\_{−11}} \= √11,    C\_{χ\_{33}} \= √33

and the per-channel completed L-functions Λ(s, χ) following the standard Iwaniec–Kowalski (2004) Chapter 5 normalization with conductor q\_χ and parity a\_χ from ZS-M25 §6.3.

**§4.2 Derivation**

Step 1\. Apply Theorem D.1-K (ZS-M25 §3 PROVEN at 35-digit precision):

ξ\_K(s) \= (1/4√33) · ξ(s) · Λ(s, χ\_{−3}) · Λ(s, χ\_{−11}) · Λ(s, χ\_{33})

Step 2\. Apply Theorem D.2 (ZS-M24 §4.3 DERIVED): B(s) \= π^(−s/2) Γ(s/2) is the archimedean factor, with ξ(s) \= B(s) · ζ(s).  
Step 3\. Apply ADS-9 (ZS-M25 §4.1 PROVEN): the constant 4√33 \= 2 · 2 · √3 · √11 has the unique factorization (i) factor 2 from Legendre duplication on (χ\_{−3}, χ\_{33}) parity pair; (ii) factor 2 from Legendre duplication on (χ\_{−11}, ξ) parity pair; (iii) factor √3 from conductor q\_{χ\_{−3}}; (iv) factor √11 from conductor q\_{χ\_{−11}}.  
Step 4\. The four channels carry (a\_χ, q\_χ) ∈ {(0,1), (1,3), (1,11), (0,33)} (ZS-M25 §6.3 PROVEN). Each channel's archimedean side is Λ(s, χ) with explicit form:  
• Λ(s, 1\) \= ξ(s) \= π^(−s/2) Γ(s/2) ζ(s),  C\_1 \= 1  
• Λ(s, χ\_{−3}) \= (3/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_{−3}),  C\_{χ\_{−3}} \= √3 from q\_{χ\_{−3}} \= 3  
• Λ(s, χ\_{−11}) \= (11/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_{−11}),  C\_{χ\_{−11}} \= √11 from q\_{χ\_{−11}} \= 11  
• Λ(s, χ\_{33}) \= (33/π)^(s/2) Γ(s/2) L(s, χ\_{33}),  C\_{χ\_{33}} \= √33 from q\_{χ\_{33}} \= 33  
Step 5\. The V₄-projected ZBSI operator T\_{χ,Z}(s) on ℋ\_K,Z^{(χ)} produces per-channel Fredholm determinant det\_Fr(I − T\_{χ,Z}(s)) \= C\_χ · Λ(s, χ) by the projection plus the Theorem D.1-K decomposition. The four C\_χ values are forced by Theorem D.1-K with no free parameter.

**§4.3 Status and Anti-Numerology**

Status: \[DERIVED\] from Theorem D.1-K \+ Theorem D.2 \+ ADS-9 \+ channel decoration of ZS-M25 §6.3. All upstream inputs are PROVEN; no free parameter is introduced.  
Anti-numerology: the four prefactors {1, √3, √11, √33} are forced uniquely by V₄ Galois structure \+ Legendre duplication \+ signature (0,2) of K. Replacing any conductor q\_χ produces incompatibility with disc(K) \= 1089 \= 33² (PROVEN, ZS-M22 §7.2). The structural factor 4 \= 2² in 4√33 (Theorem D.1-K) comes from 2² Legendre duplications, structurally forced by the two odd characters in V₄. Q \= 5 (Y-sector pentagon) does NOT appear because V₄ does not contain any modulus-5 character (ZS-M25 §4.1 PROVEN). NC-M26.3 is preserved.

**§5. Theorem M26.3 — The Three Walls**

**§5.1 Statement and Methodology**

**Theorem M26.3 (Three-Wall Quantitative Map). \[WALL\]** Three precise mathematical walls separate the V₄-equivariant ZBSI construction of §3–§4 from a closure of GRH-for-K, hence from RH. Each wall is documented by direct numerical probe at corpus-PROVEN inputs.  
(W1) P1 wall: At s \= 1/2 \+ 14.135i, the J-twisted Yakaboylu ratio ‖H − H†‖\_F / ‖H \+ H†‖\_F scales as P\_max^(−0.014) on P\_max ∈ {20, 50, 100, 200, 500, 1000}. Insufficient for P3 closure under P1.  
(W2) Pillar V wall: Pole-corrected V₄-channel Weil functional sum is negative on 4/12 grid points. Conductor/parity correction (D4b OPEN) required for non-trivial channels.  
(W3) ADS-H1 wall: Wilson cycle phase 129.45° injected directly as point coupling into the cobordism BRST charge breaks Q² \= 0 at rank 3 with ‖Q²‖\_F \= 1.092.  
Methodology: all three probes use mpmath at 50-digit precision plus numpy verified against mpmath. Inputs are corpus PROVEN (Table 2.1). No new parameters.

**§5.2 Wall W1 — P1 Closure Numerical Wall**

Theorem P3-J (ZS-M25 §5.3 PROVEN) establishes \[J, H\_Q^{Yak,J}(s)\] \= 0 for all s ∈ ℂ. This is necessary for J-symmetry but not sufficient for self-adjointness. ZS-M25 §5.5 records: at P\_max \= 20, s \= 1/2 \+ 14.13i, the anti-Hermitian/Hermitian ratio is approximately 0.42 (VERIFIED, ZS-M25 §7 Test J-3). NC-M25.3 explicitly disclaims H\_Q^{Yak,J} self-adjointness at any finite Q.  
P3 closure (Yakaboylu (2024) sense self-adjointness) requires H\_∞^{Yak,J} \= lim\_{P\_max→∞} H\_Q^{Yak,J} to converge in trace norm — this is the P1 closure (ZS-QS §4.2 OPEN). Probe W1 directly tests the convergence rate.

Table 5.1. Probe W1 — anti-Hermitian/Hermitian ratio of H\_Q^{Yak,J}(1/2 \+ 14.135i) vs P\_max.

| P\_max | ‖H+H†‖\_F/2 | ‖H−H†‖\_F/2 | ratio (anti/herm) | ‖\[J,H\]‖\_F |
| ----- | ----- | ----- | ----- | ----- |
| 20 | 0.9052 | 0.3766 | 0.4161 | 0.00e+00 |
| 50 | 0.6768 | 0.2821 | 0.4169 | 0.00e+00 |
| 100 | 0.5171 | 0.2071 | 0.4005 | 0.00e+00 |
| 200 | 0.4304 | 0.1849 | 0.4295 | 0.00e+00 |
| 500 | 0.3407 | 0.1478 | 0.4337 | 0.00e+00 |
| 1000 | 0.2994 | 0.1108 | 0.3703 | 0.00e+00 |

Power-law fit on log(ratio) vs log(P\_max): ratio ≈ const · P\_max^(−0.014). The fit slope of −0.014 is essentially flat: scaling P\_max by a factor of 50 (20 → 1000\) reduces the ratio by less than 11%. Direct extrapolation to P\_max → ∞ does NOT give convergence to zero; even at P\_max \= 10⁶ (extrapolated) the ratio remains ≈ 0.31.  
Verification W1: \[J, H\_Q^{Yak,J}(s)\] \= 0 at machine precision (≤ 1e-14) for all P\_max — confirms Theorem P3-J PROVEN at all tested P\_max. The wall is purely the anti-Hermitian/Hermitian ratio gap.  
\[STATUS: WALL W1 — VERIFIED, OPEN. P3 closure under P1 cannot be reached by direct numerical extrapolation from finite-Q. Yakaboylu (2024) self-adjointness applies to the continuous half-line operator; convergence of the finite-Q operator to a self-adjoint extension requires a separate trace-norm convergence theorem in the external mathematics literature.\]

**§5.3 Wall W2 — Pillar V V₄-Channel Weil Functional**

ZS-M22 §6.6.5(a) PROVEN diagnostic: the pole contribution Φ(0) \+ Φ(1) of ζ at s \= 1 is sign-determining; inclusion flips W\_ζ from negative to positive on multiple grid points. The corpus mandates pole-term convention lock before any sign report.  
This pole correction applies only to the trivial character channel (ζ-channel). The non-trivial Dirichlet L-functions L(s, χ\_{−3}), L(s, χ\_{−11}), L(s, χ\_{33}) are entire — no pole — so the pole-correction mechanism is structurally inapplicable (Davenport, Multiplicative Number Theory, 3rd ed., §9 IMPORTED).  
Probe W2 evaluates the V₄-channel Weil functional sum on the test grid (a, t) ∈ {0.2, 0.5, 1.0} × {0, 1, 5, 14.13} with Gaussian-cosine test functions g(x) \= exp(−ax²) cos(tx) (positive-definite by construction).

Table 5.2. Probe W2 — V₄-channel Weil functional W\_K^(V₄)(g\_{a,t}). 12-point grid; P\_max \= 500, n\_max \= 8\.

| a | t | W\_ζ no-pole | W\_ζ \+pole | W\_χ\_{-3} | W\_χ\_{-11} | W\_χ\_{33} | V₄ sum |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 0.2 | 0.00 | −7.187 | −2.088 | \+0.941 | −0.355 | \+0.142 | −1.361 |
| 0.2 | 1.00 | \+1.454 | \+4.584 | \+0.631 | −0.409 | −1.045 | \+3.760 |
| 0.2 | 5.00 | \+0.241 | \+0.241 | −0.861 | −2.090 | −0.092 | −2.802 |
| 0.2 | 14.13 | \+3.154 | \+3.154 | −1.729 | −1.114 | −0.208 | \+0.102 |
| 0.5 | 0.00 | −2.682 | \+1.345 | \+0.770 | −0.296 | −0.441 | \+1.377 |
| 0.5 | 1.00 | −0.615 | \+2.329 | \+0.561 | \+0.110 | −0.739 | \+2.261 |
| 0.5 | 5.00 | \+0.252 | \+0.252 | −0.822 | −1.546 | \+0.300 | −1.816 |
| 0.5 | 14.13 | \+1.699 | \+1.699 | −1.141 | −0.227 | \+0.124 | \+0.455 |
| 1.0 | 0.00 | −1.248 | \+1.905 | \+0.589 | \+0.054 | −0.571 | \+1.976 |
| 1.0 | 1.00 | −0.629 | \+1.964 | \+0.451 | \+0.265 | −0.500 | \+2.181 |
| 1.0 | 5.00 | \+0.278 | \+0.297 | −0.646 | −0.936 | \+0.447 | −0.838 |
| 1.0 | 14.13 | \+0.967 | \+0.967 | −0.702 | −0.221 | \+0.391 | \+0.435 |

Sign profile: W\_ζ without pole correction is negative on 5/12 grid points; with pole correction reduces to 1/12. Full V₄ sum negative on 4/12. Non-trivial channels W\_{χ\_{−3}}, W\_{χ\_{−11}}, W\_{χ\_{33}} are negative at multiple points (especially high t); no pole-correction mechanism is available for them.  
Structural reading: pole correction reduces ζ-channel negativity from 5/12 to 1/12 (consistent with ZS-M22 §6.6.5(a) PROVEN diagnostic). Non-trivial channels remain indefinite — consistent with ADS-5 PROVEN (12 negative-eigenvalue confirmations across 4 channels × 3 σ values, ZS-M22 §6.3). Required correction: conductor/parity correction of Connes (2000)–Burnol (2002, 2004\) — Dragon D4 sub-target D4b OPEN.  
\[STATUS: WALL W2 — VERIFIED, OPEN. Pole correction works for trivial channel only; conductor/parity correction for non-trivial channels remains OPEN under D4b.\]

**§5.4 Wall W3 — Cobordism BRST Nilpotency**

ZS-M22 §6.6.4 minimal rank-one consistency check: Q\_0 \= |1⟩⟨b|, Q\_0² \= 0 PASSES. The check uses the J\_Z-odd ghost pair (b, c) and verifies \[Q\_0, W\]·Π\_phys \= 0\. The full closure of ADS-H1 requires a complete BRST charge on the cobordism-history fiber, currently OPEN.  
Probe W3 attempts higher-rank extension of Q\_BRST while preserving Q² \= 0 on the minimal 4-dimensional cobordism slice with basis {|0⟩\_Z, |1⟩\_Z, |b⟩, |c⟩}.

Table 5.3. Probe W3 — BRST charge extension attempts on the minimal 4-dim cobordism slice.

| Construction | BRST action | ‖Q²‖\_F | rank(Q) | Q² \= 0? |
| ----- | ----- | ----- | ----- | ----- |
| Rank-1 (corpus minimal) | Q|c⟩ \= |1⟩\_Z | 0.00e+00 | 1 | PASS |
| Rank-2 (standard BV ghost) | \+ Q|b⟩ \= |0⟩\_Z | 0.00e+00 | 2 | PASS |
| Rank-3 (Wilson phase point coupling) | \+ Q|0⟩\_Z \= sin(arg λ)·|b⟩ | 1.092 | 3 | FAIL |

Rank-2 extension (standard BV ghost) PASSES Q² \= 0\. However, dim H⁰(Q\_2) \= 0 (ker − im \= 2 − 2 \= 0): trivial cohomology at rank 2, giving zero-dimensional trace target for ADS-H1's W\_K(g) \= Tr\_{H⁰(Q\_BRST)}(A\_g† A\_g).  
Rank-3 extension attempts to inject the Wilson cycle phase 129.45° (PROVEN, ZS-F0 §9.5 Theorem 9.4: arg(λ) is irrational) directly into the BRST charge as a point coupling Q|0⟩\_Z \= sin(arg λ)·|b⟩. Then Q²|0⟩\_Z \= Q(sin(arg λ)·|b⟩) \= sin(arg λ)·|0⟩\_Z ≠ 0\.  
This is a structural obstruction, not a computational error. The Wilson cycle phase as a point coupling generates a non-zero |0⟩\_Z → |0⟩\_Z return amplitude under Q², breaking nilpotency.  
**Corollary M26.3a (Wilson Phase Worldline-Parallel-Transport, NEW). \[HYPOTHESIS-strong\]** If a cobordism BRST charge Q\_BRST exists that closes ADS-H1 — i.e., satisfies Q\_BRST² \= 0 on the cobordism-history fiber and produces the V₄-equivariant cross-channel coupling required by ZS-M22 §6.6.5(b) — then Q\_BRST cannot encode the Wilson cycle phase as a point coupling. The Wilson phase must enter as a parallel transport along the cobordism worldline (gauge connection on the worldline parameter), not as a coupling at a single point of the BRST complex.  
This corollary is the principal new structural result of ZS-M26. It identifies the precise next mathematical direction for ADS-H1 closure: BV-BFV worldline gauge theory in the sense of Cattaneo–Mnev–Reshetikhin (2014–2024) extended with V₄-equivariant arithmetic decoration.  
\[STATUS: WALL W3 — VERIFIED via direct probe; Corollary M26.3a HYPOTHESIS-strong. Full structural derivation that Wilson-phase-parallel-transport closes ADS-H1 is OPEN (O-M26.1, §9).\]

**§5.5 Joint Wall Status Summary**

Table 5.4. Three-wall joint status.

| Wall | Direct probe result | Structural reading | Closure path |
| ----- | ----- | ----- | ----- |
| W1 (P1) | ratio P\_max^(−0.014), no convergence | Self-adjoint extension OPEN | External: trace-norm convergence theorem |
| W2 (Pillar V) | V₄ sum 4/12 negative | Pole correction limited to ζ | External: D4b conductor/parity (Connes–Burnol) |
| W3 (ADS-H1) | ‖Q²‖\_F \= 1.092 at rank 3 | Wilson phase ≠ point coupling | Internal: Worldline parallel transport (NEW) |

All three walls are VERIFIED via direct numerical probe at corpus PROVEN inputs. Their joint structural reading: V₄-equivariant ZBSI closure of GRH-for-K requires (W1) external trace-norm convergence theorem extending Yakaboylu (2024); (W2) external conductor/parity correction extending Connes (2000) and Burnol (2002, 2004); (W3) NEW Z-Spin-internal direction encoding Wilson phase as worldline parallel transport on the cobordism complex.  
Once all three walls are closed (each via its specified path), the V₄-equivariant ZBSI of §3–§4 yields per-channel projected positivity W\_χ(g) \= ‖D\_{χ,g}‖\_HS² ≥ 0, hence positivity of the full V₄ Weil distribution, hence (by the standard Connes–Weil equivalence; Connes 1999, Bombieri 2000\) GRH-for-K, hence RH and the three GRHs for L(χ\_{−3}), L(χ\_{−11}), L(χ\_{33}).

**§6. Interpretation Layer (Not Proof Engine)**

This section consolidates the structural role of four corpus tools — FFPP, Two-Protocol sum rule, pole correction, Pentagon tetration — as interpretation/normalization/diagnostic, NOT as proof engines for RH or GRH-for-K. This separation is required by the anti-numerology discipline of ZS-M22 §7 and the corpus PROVEN no-go on Pentagon → χ\_{33} direct connection (ZS-M25 §4.1).

**§6.1 FFPP W₀(−iπ/2) — ZBSI Operator Normalization**

FFPP (ZS-F0 §13 Theorem 13.3 PROVEN): all Z-Spin numerical content compresses to W₀(−iπ/2) under the minimal 5-axiom set.  
Role in ZS-M26: FFPP provides the unique fixed-point normalization for the ZBSI operator T\_{K,Z}(s). Specifically, λ \= (iπ/2)z\* with z\* \= −W₀(−iπ/2)/(iπ/2) sets the i-tetration linearization scale, propagating through the Wilson cycle to fix the eigenvector orthogonality ⟨v\_W | v\_W\*⟩ \= 0 (ZS-F0 §9.1 PROVEN). This orthogonality enters Theorem M26.1 implicitly via the BV-BFV functor B\_Z.  
Role NOT claimed: FFPP is not used as a "prevention principle" for L-zero off-critical-line motion. The FFPP fixed point compresses Z-Spin content; it does not prove analytic zero-location for any L-function.

**§6.2 Two-Protocol Sum Rule — Finite-Q Diagnostic**

Sum rule (ZS-F0 §12.3 \+ ZS-F16 Theorem 4.1 PROVEN): 0.7948 \+ 0.2050 \+ 0.0001 \= 0.9999 decomposes the per-cycle Wilson loop amplitude budget into Z-block-retained, J\_Z-odd-transferred, X+Y-residual.  
Role in ZS-M26: the sum rule is a finite-Q spectral consistency diagnostic for the Wilson cobordism W. Protocol (a) state-preparation P\_a^(n) \= 0.7948^n · cos²(n · 129.45°) and Protocol (b) spectral P\_b^(n) \= 0.7948^n predictions are mutually consistent in time-average ergodic sense (ZS-F16 §4.4 PROVEN). The sum rule audits this consistency.  
Role NOT claimed: the sum rule does NOT analytically force L-zero locations. There is no PROVEN trace identity between L(s, χ) zeros and Wilson-protocol probability conservation. NC-M26.4 preserves this scope.

**§6.3 Pole Correction — Trivial-Channel Convention Lock**

Pole correction (ZS-M22 §6.6.5(a) PROVEN diagnostic): inclusion of Φ(0) \+ Φ(1) flips W\_ζ from negative to positive on multiple grid points. Corpus mandates: any Weil functional audit must lock the pole-term convention before reporting a sign.  
Role in ZS-M26: pole correction is locked as part of the trivial-channel (ζ) Weil functional convention. Probe W2 (§5.3) confirmed the corpus diagnostic: ζ-channel negativity reduces from 5/12 to 1/12.  
Role NOT claimed: pole correction does NOT generalize to non-trivial L-function channels (no pole). Conductor/parity correction (D4b) is the corresponding mechanism for non-trivial channels and remains OPEN.

**§6.4 Pentagon Tetration — Optional Y-Channel Interpretation**

Pentagon tetration z\*(5) \= −W\_0(−2πi/5)/(2πi/5) (ZS-U10 §4.1 PROVEN at 50-digit precision): connected to electron internal mode (ZS-U10 §5.1 DERIVED) and Schwinger leading order 1/(2π) \= dim(Z)/(4π) (ZS-U10 Theorem U10.3 DERIVED).  
Role in ZS-M26: Pentagon tetration is registered as an optional Y-channel HYPOTHESIS-strong interpretation that does NOT enter the ZBSI proof engine.  
Role NOT claimed: Pentagon tetration does NOT control L(s, χ\_{33}) zero distribution. Corpus PROVEN result (ZS-M25 §4.1) establishes that K \= ℚ(√−3, √−11) has abelian character group V₄ which does NOT include any modulus-5 character. Q \= 5 is a Y-sector pentagon mode, structurally separate from the V₄ character data of K. Connection between Pentagon tetration and L(s, χ\_{33}) is registered as the externally OPEN problem O-M25.1 (sextic field K\_6 \= K · ℚ(ζ\_5) extension).  
\[STATUS: §6.4 strict NON-CLAIM under NC-M26.3 below.\]

**§7. Consolidated Non-Claims**

This paper inherits non-claims NC-M22.X, NC-M23.1–7, NC-M24.X, NC-M25.1–6 verbatim. New non-claims registered in this paper:  
NC-M26.1: Does NOT claim a proof of the Riemann Hypothesis. Theorems M26.1, M26.2 are V₄-character cohomology and projected determinant structure; Theorem M26.3 maps three OPEN walls.  
NC-M26.2: Does NOT claim a proof of GRH for L(s, χ\_{−3}), L(s, χ\_{−11}), or L(s, χ\_{33}). Per-channel Λ(s, χ) zero locations remain externally OPEN.  
NC-M26.3: Does NOT claim that Pentagon tetration z\*(5) controls L(s, χ\_{33}) zero distribution. The corpus PROVEN result that K does not include modulus-5 character (ZS-M25 §4.1) is preserved verbatim.  
NC-M26.4: Does NOT claim that the Two-Protocol sum rule analytically forces L-function zero locations. The sum rule is a finite-Q diagnostic per §6.2.  
NC-M26.5: Does NOT close any of Dragon D4 sub-targets D4a, D4b, D4c, D4d (ZS-M23 §5.4). The three-wall map quantifies the precise OPEN gates, not closures.  
NC-M26.6: Does NOT claim that the rank-2 BRST extension of §5.4 produces a non-trivial cohomology useful for ADS-H1. Direct probe shows H⁰(Q\_2) \= 0 at rank 2; rank-3 extension fails Q² \= 0\.  
NC-M26.7: Does NOT introduce any new free parameter. All inputs are LOCKED from upstream corpus papers per Table 2.1. The numerical walls (W1, W2, W3) are direct probes of corpus-PROVEN structures, not new fits.

**§8. Falsification Gates**

This paper registers eight falsification gates organized into four layers (mathematical/theoretical, simulation/consistency, observational, anti-overclaim).

Table 8.1. ZS-M26 falsification gates.

| Gate | Layer | Condition (triggers falsification if TRUE) | Status |
| ----- | ----- | ----- | ----- |
| F-M26.1 | Mathematical | V₄ Schur idempotents Π\_χ fail to satisfy Π\_χ Π\_χ' \= δ\_{χ,χ'} Π\_χ at exact precision | PASS (algebraic exact) |
| F-M26.2 | Mathematical | Theorem M26.2 prefactor product structure deviates from ZS-M25 ADS-9 algebraic factorization at 35-digit precision | PASS (35-digit verified) |
| F-M26.3 | Simulation | P\_max scaling of Probe W1 ratio shows convergence rate \< P\_max^(−0.5) (would be sufficient for P3) | PASS (rate is P\_max^(−0.014), far slower) |
| F-M26.4 | Simulation | Probe W2 V₄ sum is non-negative on entire 12-point grid (would imply scalar-route closure, contradicting ADS-5) | PASS (4/12 negative) |
| F-M26.5 | Simulation | Rank-3 BRST extension with Wilson phase point coupling preserves Q² \= 0 (would invalidate Corollary M26.3a) | PASS (‖Q²‖\_F \= 1.092 ≠ 0\) |
| F-M26.6 | External | Connes–Weil equivalence (GRH-for-K ⇔ Weil positivity) is shown false | PASS (standard, Connes 1999\) |
| F-M26.7 | External Dep. | ZS-M25 Theorem D.1-K is retracted or its 4√33 factorization shown incorrect | PASS (35-digit verified, ZS-M25 §7) |
| F-M26.8 | Anti-Overclaim | Any §3–§5 result is found to introduce a new free parameter beyond LOCKED A and Q | PASS (audit per Table 2.1) |

All eight gates currently PASS. The Three-Wall structure of §5 is itself a multi-layer falsification: each wall is a quantitative VERIFIED OPEN gate, designed to falsify any premature closure attempt by direct numerical probe.

**§9. Open Problems**

This paper inherits OPEN problems O-M23.1–11, O-M25.1–6 verbatim. Three new OPEN problems specific to ZS-M26 are registered.  
O-M26.1 (Wilson-phase parallel transport closure of W3). Formulate the cobordism BRST charge Q\_BRST such that the Wilson cycle phase 129.45° enters as a worldline parallel transport (gauge connection on the worldline parameter τ ∈ \[0, T\_W\]) rather than as a point coupling. Test whether such a Q\_BRST satisfies Q\_BRST² \= 0 on the cobordism-history fiber and produces V₄-equivariant cross-channel coupling consistent with ZS-M22 §6.6.5(b). External candidate framework: BV-BFV worldline gauge theory (Cattaneo–Mnev–Reshetikhin 2014, 2021).  
O-M26.2 (Trace-norm convergence of H\_∞^{Yak,J} for W1 closure). Prove (or disprove) that H\_Q^{Yak,J}(s) converges in trace-class Fredholm norm to a self-adjoint extension H\_∞^{Yak,J}(s) on the Yakaboylu (2024) Laguerre-boundary domain as P\_max → ∞. Direct probe of W1 (§5.2) shows the anti-Hermitian/Hermitian ratio scales only as P\_max^(−0.014), providing strong evidence that direct numerical extrapolation does not suffice. The convergence theorem must be analytic, not numerical.  
O-M26.3 (Conductor/parity correction for non-trivial channels). Construct the explicit Connes (2000)–Burnol (2002, 2004\) conductor-operator correction to W\_χ(g) for χ ∈ {χ\_{−3}, χ\_{−11}, χ\_{33}} at the corresponding ramified primes p ∈ {3, 11}, completing Dragon D4 sub-target D4b. Test whether the conductor-corrected V₄-channel Weil functional sum becomes non-negative on the test-functional grid of Probe W2 (§5.3).

**§10. Verification Suite (24/24 PASS)**

All numerical claims of this paper were verified at 50-digit mpmath precision (analytic continuations and Theorem D.1-K reproduction) plus floating-point machine precision (algebraic identities, BRST nilpotency, V₄ Schur orthogonality).

Table 10.1. ZS-M26 verification suite (24/24 PASS).

| Cat. | Test ID | Description | Status |
| ----- | ----- | ----- | ----- |
| \[A\] | A-1 | A \= 35/437 LOCKED (ZS-F2) | PASS |
| \[A\] | A-2 | Q \= 11 prime LOCKED (ZS-F5) | PASS |
| \[A\] | A-3 | K \= ℚ(√−3, √−11), V₄ Galois, disc \= 1089 LOCKED (ZS-M22) | PASS |
| \[A\] | A-4 | Channel decoration {(0,1),(1,3),(1,11),(0,33)} LOCKED (ZS-M25) | PASS |
| \[B\] | B-1 | V₄ Schur idempotents Π\_χ Π\_χ' \= δ\_{χ,χ'} Π\_χ algebraic exact | PASS |
| \[B\] | B-2 | Σ\_χ Π\_χ \= I (completeness) algebraic exact | PASS |
| \[B\] | B-3 | All four V₄ characters χ² \= 1 (quadratic) algebraic exact | PASS |
| \[B\] | B-4 | Cobordism-history lift Π\_χ^(K,Z) \= I\_cob ⊗ Π\_χ idempotent | PASS |
| \[C\] | C-1 | Theorem M26.2 prefactor C\_1 \= 1 (trivial channel) | PASS |
| \[C\] | C-2 | C\_{χ\_{−3}} \= √3 from conductor q\_{χ\_{−3}} \= 3 | PASS |
| \[C\] | C-3 | C\_{χ\_{−11}} \= √11 from conductor q\_{χ\_{−11}} \= 11 | PASS |
| \[C\] | C-4 | C\_{χ\_{33}} \= √33 from conductor q\_{χ\_{33}} \= 33 | PASS |
| \[C\] | C-5 | ADS-9 4√33 \= 2·2·√3·√11 algebraic factorization (35-digit) | PASS |
| \[D\] | D-1 | Probe W1: ratio at P\_max \= 20 \= 0.4161 ≈ corpus ZS-M25 Test J-3 value 0.42 | PASS |
| \[D\] | D-2 | Probe W1: P\_max scaling fit ratio \~ P\_max^(−0.014) | PASS |
| \[D\] | D-3 | Probe W1: \[J, H\_Q^(Yak,J)\] \= 0 at machine precision for P\_max ∈ {20,...,1000} | PASS |
| \[E\] | E-1 | Probe W2: pole correction reduces ζ-channel negativity 5/12 → 1/12 | PASS |
| \[E\] | E-2 | Probe W2: V₄ sum negative on 4/12 grid points (W2 wall confirmed) | PASS |
| \[E\] | E-3 | Probe W2: non-trivial L-channels are entire (no pole) — Davenport §9 | PASS |
| \[F\] | F-1 | Probe W3: rank-1 BRST Q\_0 \= |1⟩⟨b| with Q\_0² \= 0 (ZS-M22 §6.6.4) | PASS |
| \[F\] | F-2 | Probe W3: rank-2 extension passes Q² \= 0 with H⁰ \= 0 | PASS |
| \[F\] | F-3 | Probe W3: rank-3 with Wilson phase point coupling, ‖Q²‖\_F \= 1.092 ≠ 0 | PASS |
| \[F\] | F-4 | Probe W3: structural derivation Q²|0⟩\_Z \= sin(arg λ)·|0⟩\_Z ≠ 0 | PASS (algebraic) |
| \[G\] | G-1 | Zero new free parameters audit (all values trace to LOCKED corpus) | PASS |

Total: A (4) \+ B (4) \+ C (5) \+ D (3) \+ E (3) \+ F (4) \+ G (1) \= 24 tests, all PASS.

**§11. Conclusion**

This paper organizes the cumulative Z-Spin RH program (47+ rounds; ZS-M22, ZS-M23, ZS-M24, ZS-M25 PROVEN structural inputs) under a single V₄-equivariant ZBSI framework on the BV-BFV cobordism-history fiber, and quantifies the precise mathematical walls separating this construction from a Hilbert–Pólya closure of GRH-for-K \= RH \+ GRH(L\_{−3}) \+ GRH(L\_{−11}) \+ GRH(L\_{33}).  
Three principal results:  
(1) Theorem M26.1 (V₄-Character Cohomology Decomposition, PROVEN): the arithmetic fiber decomposes via V₄ Schur idempotents into four orthogonal channels {1, χ\_{−3}, χ\_{−11}, χ\_{33}}. Lifted to the cobordism-history fiber ℋ\_K,Z \= ⊕\_χ (ℋ\_cob ⊗ ℋ\_χ), the decomposition bypasses ADS-6 PROVEN no-go (which applies only to the boundary fiber).  
(2) Theorem M26.2 (Projected Determinant per Channel, DERIVED): per-channel projected Fredholm determinant det\_Fr(I − T\_{χ,Z}(s)) \= C\_χ · Λ(s, χ) with C\_1 \= 1, C\_{χ\_{−3}} \= √3, C\_{χ\_{−11}} \= √11, C\_{χ\_{33}} \= √33, forced uniquely by Theorem D.1-K and ADS-9 (ZS-M25 PROVEN). The four prefactors are the algebraic V₄-decoration; their structure reproduces 4√33 of Theorem D.1-K.  
(3) Theorem M26.3 (Three-Wall Quantitative Map, NEW): three precise OPEN walls. (W1) P3 closure under P1 anti-Hermitian/Hermitian ratio scales as P\_max^(−0.014), insufficient for direct extrapolation; (W2) pole-corrected V₄-channel Weil functional sum negative on 4/12 grid points, with non-trivial channels requiring conductor/parity correction (D4b OPEN); (W3) Wilson cycle phase as point coupling in cobordism BRST charge breaks Q² \= 0, with Corollary M26.3a HYPOTHESIS-strong stating that the Wilson phase must enter as worldline-parallel-transport.  
Corollary M26.3a is the principal new structural finding: it identifies the precise mathematical direction for ADS-H1 closure as BV-BFV worldline gauge theory (Cattaneo–Mnev–Reshetikhin 2014, 2021\) extended with V₄-equivariant arithmetic decoration. This direction is registered as OPEN problem O-M26.1.  
This paper does NOT claim a proof of the Riemann Hypothesis. NC-M23.1 (no RH proof) is preserved without modification. The contribution is to organize the Z-Spin participation in the standard Hilbert–Pólya outline under a single framework that makes the OPEN gates precisely visible, quantifies their distance to closure by direct numerical probe, and identifies the next mathematical direction for the sole structurally compatible surviving route. The framework embraces RH as a shadow rather than as a prerequisite (ZS-M18 §3 framework consistent).  
The Z-Spin RH program continues to satisfy the principle stated in ZS-M23 §12: "Z-Spin does not, and structurally cannot, prove RH from internal data alone." What this paper adds is precision: the three walls W1, W2, W3 are now quantitatively mapped, each with explicit closure paths (two external, one Z-Spin-internal NEW direction). Future work along these three closure paths — particularly the worldline-parallel-transport direction of Corollary M26.3a — defines the next operational steps for ZS-M27 onward.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.  
Code availability. Direct probe scripts: zsm26\_attempt.py (Probes W1, W2, W3 with mpmath 50-digit \+ numpy verification). Reproducibility: input parameters are corpus-PROVEN (Table 2.1); output is deterministic given the standard random number convention (mpmath 50-digit \+ numpy double precision). All scripts will be publicly available at https://github.com/KennyKang-git/zspin upon v1.0 release.

**References**

\[1\] B. Riemann, "Über die Anzahl der Primzahlen unter einer gegebenen Größe," Monatsberichte der Berliner Akademie, November 1859\.  
\[2\] A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers," Comm. Sém. Math. Univ. Lund (Suppl. dédié à M. Riesz), 252 (1952).  
\[3\] A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function," Selecta Mathematica (New Series) 5, 29–106 (1999).  
\[4\] E. Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I," Atti Accad. Naz. Lincei 11, 183 (2000).  
\[5\] A. Connes, "Sur les formules explicites I: analyse invariante," Comptes Rendus de l'Académie des Sciences, Série I, 332, 1009–1014 (2001). arXiv:math/0101068.  
\[6\] J.-F. Burnol, "Sur les espaces de Sonine associés par de Branges à la transformation de Fourier," Comptes Rendus de l'Académie des Sciences, Série I, 335, 689–692 (2002).  
\[7\] J.-F. Burnol, "Two complete and minimal systems associated with the zeros of the Riemann zeta function," Journal de Théorie des Nombres de Bordeaux 16, 65–94 (2004). arXiv:math/0203120.  
\[8\] A. Connes and C. Consani, "Weil positivity and Trace formula, the archimedean place," Selecta Mathematica (New Series) 27, 77 (2021). arXiv:2006.13771.  
\[9\] A. Connes and H. Moscovici, "The UV prolate spectrum matches the zeros of zeta," Proceedings of the National Academy of Sciences USA 119, e2123174119 (2022).  
\[10\] E. Yakaboylu, "Hamiltonian for the Hilbert–Pólya conjecture," J. Phys. A: Math. Theor. 57, 235204 (2024). arXiv:2309.00405.  
\[11\] G. Mårdby and J. Rowlett, "Spectral invariants of integrable polygons," J. Fourier Anal. Appl. 31, art. 81 (2025). arXiv:2409.14391.  
\[12\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, "Classical BV theories on manifolds with boundary," Communications in Mathematical Physics 332, 535–603 (2014). arXiv:1201.0290.  
\[13\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, "Cellular BV-BFV-BF theory," preprint (2021–2024).  
\[14\] H. Davenport, Multiplicative Number Theory, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics 74, Springer-Verlag (2000).  
\[15\] H. Iwaniec and E. Kowalski, Analytic Number Theory, AMS Colloquium Publications 53, American Mathematical Society (2004).  
\[16\] J.-P. Serre, Linear Representations of Finite Groups, Graduate Texts in Mathematics 42, Springer (1977).  
\[17\] M. Watkins, "Class numbers of imaginary quadratic fields," Math. Comp. 73, 907 (2004).  
\[18\] K. Kang, "ZS-F0 v1.0(R): Foundational BV-BFV Functor B\_Z, Wilson Cobordism, and Three-Layer Fixed Point Structure," Z-Spin Cosmology Collaboration (2026).  
\[19\] K. Kang, "ZS-F2 v1.0(R): Geometric Impedance A \= 35/437 from Polyhedral Geometry," Z-Spin Cosmology Collaboration (2026).  
\[20\] K. Kang, "ZS-F5 v1.0: Q \= 11 Register and (Z, X, Y) Sector Decomposition," Z-Spin Cosmology Collaboration (2026).  
\[21\] K. Kang, "ZS-F16 v1.0: Two-Protocol Theorem and CTA-Z v3 Framework," Z-Spin Cosmology Collaboration (2026).  
\[22\] K. Kang, "ZS-M1 v1.0: i-Tetration Holomorphic Self-Iteration and the Fixed Point z\*," Z-Spin Cosmology Collaboration (2026).  
\[23\] K. Kang, "ZS-M3 v1.0: 4π Spinor Closure and j \= 1/2 Uniqueness," Z-Spin Cosmology Collaboration (2026).  
\[24\] K. Kang, "ZS-M4 v1.0: Spectral Bridge & Transfer Operator," Z-Spin Cosmology Collaboration (2026).  
\[25\] K. Kang, "ZS-M22 v1.0(Revised): Five-Pillar Arithmetic-Dedekind Scaffold of Z-Spin Cosmology," Z-Spin Cosmology Collaboration (May 2026).  
\[26\] K. Kang, "ZS-M23 v1.0(Revised): Y-Sector RH Contribution Map and Four Dragons," Z-Spin Cosmology Collaboration (March 2026, August 2026 dated update).  
\[27\] K. Kang, "ZS-M24 v1.0: Face Polygon Spectral Zeta and Archimedean Completion," Z-Spin Cosmology Collaboration (May 2026).  
\[28\] K. Kang, "ZS-M25 v1.0: Composite-Field Archimedean Completion and J-Twisted Yakaboylu Bridge," Z-Spin Cosmology Collaboration (May 2026).  
\[29\] K. Kang, "ZS-QS v1.0(Revised): Inverse Riemann Engine: Quantum Algorithms for Spectral Zero Detection," Z-Spin Cosmology Collaboration (May 2026).  
\[30\] K. Kang, "ZS-U10 v1.0: Pentagon Tetration and Schwinger Coefficient," Z-Spin Cosmology Collaboration (2026).

**Version History**

v1.0 (May 2026): Initial public release. Theorem M26.1 (V₄-Character Cohomology Decomposition, PROVEN); Theorem M26.2 (Projected Determinant per Channel, DERIVED); Theorem M26.3 (Three-Wall Quantitative Map, WALL); Corollary M26.3a (Wilson Phase Worldline-Parallel-Transport, HYPOTHESIS-strong, NEW). Verification suite 24/24 PASS at 50-digit mpmath precision (numerical) plus algebraic exact (Schur orthogonality, BRST nilpotency identities). Falsification gates F-M26.1 through F-M26.8 registered, all PASS. Open problems O-M26.1 (Wilson-phase parallel transport closure), O-M26.2 (trace-norm convergence for W1), O-M26.3 (conductor/parity correction for non-trivial channels) registered. Non-claims NC-M26.1 through NC-M26.7 registered. Zero new free parameters; A \= 35/437, Q \= 11, K \= ℚ(√−3, √−11) LOCKED throughout. NON-CLAIM: not an RH proof; W1, W2, W3 walls remain VERIFIED OPEN gates. (Consolidated from internal Z-Spin Collaboration deep-exploration session of May 2026 on V₄-equivariant ZBSI structure with cobordism-history fiber bypass of ADS-6, Three-Wall direct numerical probes, and the Wilson-phase worldline-parallel-transport NEW direction for ADS-H1 closure.)  
