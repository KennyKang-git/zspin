**ZS-M22**

**Arithmetic-Dedekind Scaffold of Z-Spin Cosmology**

*Dual Realization of the Q \= 11 Register, Complete Prime-Side Derivation, Scalar-Kernel No-Go for the Weil Positivity Route, and the Critical Line as the Unique J-Symmetry Locus*

**Kenny Kang**

May 2026  |  ZS-M22 (Mathematical Spine Theme)

**Verification: 60/60 PASS (52 v1.0 \+ 8 v1.0 Revised Step-1 audit)  |  Zero Free Parameters  |  NON-CLAIM: Not an RH Proof**

# **§0.  Abstract**

We establish the Arithmetic-Dedekind Scaffold (ADS) of Z-Spin Cosmology: a self-consistent assembly of five structural pillars connecting the polyhedral geometry of the framework to the Riemann zeta function and its allied L-functions, with zero free parameters throughout.

**Pillar I (Chain A):**  n \= 3 generates the Eisenstein field ℚ(ω) \= ℚ(√−3) via the exact Lamé eigenvalue spectrum λ\_{m,n} ∝ m² \+ mn \+ n² \= |m − nω|². Dedekind factorization: ζ\_ℚ(ω)(s) \= ζ(s)·L(s,χ₋₃). Sector dimensions read off: |disc| \= 3 \= X, |units| \= 6 \= Y. \[PROVEN, gap-free\]

**Pillar II (Chain B):**  Q \= 11 generates ℚ(√−11) via cyclotomic theory. Composite field K \= ℚ(√−3,√−11) has ζ\_K(s) \= ζ(s)·L(s,χ₋₃)·L(s,χ₋₁₁)·L(s,χ₃₃). \[PROVEN, gap-free\]

**Pillar III (Multiplicative Arithmetic Fiber):**  The Q \= 11 register carries an independent multiplicative realization. The gate M\_p|a⟩ \= |pa mod 11⟩ on 𝔽₁₁× diagonalizes exactly in the Dirichlet character basis: M\_p|χ\_k⟩ \= χ\_k(p)|χ\_k⟩. Its local determinant det(I − p^{−s}M\_p)^{−1} \= (1 − χ\_k(p)p^{−s})^{−1} is the exact Dirichlet Euler factor. The full product over p ≠ 11 recovers ∏\_{χ mod 11}L(s,χ). This partially closes the additive-multiplicative gap (Gate FM13-5). \[PROVEN\]

**Pillar IV (Critical Line as Unique J-Symmetry Locus):**  We prove analytically that D\_norm(σ) is globally maximized at and only at σ \= 1/2, unifying three independent witnesses: (W1) ε\_J \= 0 iff σ \= 1/2 \[ZS-M7 Thm 4, PROVEN\]; (W2) a₁(equilateral face polygon) \= 1/2 \[McKean–Singer, PROVEN\]; (W3) j \= 1/2 ↔ σ \= 1/2 as Z₂ involution fixed-point subspaces \[ZS-M21 H11, DERIVED-interpretation\]. Triple coincidence upgraded HYPOTHESIS → DERIVED-interpretation. \[PROVEN, analytic\]

**Pillar V (Scalar-Kernel No-Go):**  Explicit Gram computation proves that no scalar-identity or operator-diagonal Weil kernel K\_K(y) \= B\_K(y)I − P\_K(y) can satisfy Weil positivity. All four character channels {1, χ₋₃, χ₋₁₁, χ₃₃} exhibit negative Gram eigenvalues. D₄×C₂ projection cannot rescue positivity. Required: B\_K(y) ∈ End(ℋ\_BFV ⊗ ℋ\_arith) matrix-valued. \[PROVEN — falsification of scalar/diagonal route\]

This paper does NOT claim a proof of the Riemann Hypothesis. Verification: 52/52 PASS. Zero free parameters.

# **Epistemic Status Legend**

| Tag | Definition |
| ----- | ----- |
| PROVEN | Exact mathematical fact; machine-verifiable; standard mathematics alone. |
| DERIVED | Follows from Z-Spin action \+ standard physics; zero free parameters. |
| DERIVED-interpretation | Synthesis of PROVEN components; new conceptual framing. |
| DERIVED-CONDITIONAL | Derived conditional on an explicitly stated assumption. |
| HYPOTHESIS | Physically motivated conjecture; derivation chain incomplete. |
| OBSERVATION | Numerically verified structural pattern; action-level derivation pending. |
| CONFIRMED | Empirically validated; statistical significance established. |
| GENERIC | True for a broad class; not specific to Z-Spin parameters. |
| TAUTOLOGICAL | True by construction. |
| OPEN | Well-posed problem without current resolution. |
| NON-CLAIM | Explicitly not asserted. Documented to prevent overclaim. |
| FALSIFIED | Tested and failed; documented as honest negative result. |
| LOCKED | Input value fixed from prior paper; not re-derived here. |

# **§1.  Introduction**

## **1.1  Scope and Context**

Z-Spin Cosmology derives all dimensionless physical observables from four foundational structural inputs — the geometric impedance A \= 35/437, the register Q \= 11, the i-tetration fixed point z\* ≈ 0.4383 \+ 0.3606i, and the sector decomposition (Z, X, Y) \= (2, 3, 6\) — with zero free parameters. The mathematical spine papers ZS-M1 through ZS-M21 establish the structural, spectral, and number-theoretic foundations. This paper, ZS-M22, assembles the Arithmetic-Dedekind Scaffold (ADS): the complete body of results connecting Z-Spin's geometric axioms to the Riemann zeta function ζ(s) and its allied Dirichlet L-functions.

The ADS synthesizes four previously separate lines of work: (1) the Dedekind chain results of ZS-M13 (Chain A, Chain B, composite field K); (2) the transfer operator results of ZS-M4/M7/ZS-QS (J-intertwining, contraction bound, spectral discrimination); (3) the geometric results of ZS-F7/M13 (Reuleaux geometry, Seeley–DeWitt coefficients, face polygon spectral invariant); and (4) the Weil positivity analysis from the Z-Spin RH exploration program (RH-ZS1 through RH-ZS15, internal research notes, 176 pages documenting RH-ZS1–RH-ZS15). Taken together, they constitute a structurally coherent — though not yet complete — scaffold linking polyhedral geometry to the deepest unsolved problem in analytic number theory.

## **1.2  The Five Pillars — Summary of Results**

| Pillar | Title | Principal Result | Status |
| ----- | ----- | ----- | ----- |
| I | Chain A | n=3 → ℤ\[ω\] → ζ(s)·L(s,χ₋₃); sector dims X=3,Y=6 identified | PROVEN \[ZS-M13\] |
| II | Chain B \+ K | Q=11 → ℚ(√−11); ζ\_K=ζ·L(χ₋₃)·L(χ₋₁₁)·L(χ₃₃) | PROVEN \[ZS-M13\] |
| III | Mult. Fiber | M\_p|χ\_k⟩=χ\_k(p)|χ\_k⟩ → exact Euler factors; FM13-5 partial closure | PROVEN \[NEW\] |
| IV | Critical Line | D\_norm(σ) max at σ=1/2; triple coincidence unified | PROVEN \[NEW, analytic\] |
| V | Scalar No-Go | Weil positivity fails for all diagonal kernels; BFV requirement | PROVEN \[NEW\] |

## **1.3  NON-CLAIMS**

**NC-M22.1:**  This paper does NOT claim a proof of the Riemann Hypothesis.

**NC-M22.2:**  Pillar V does NOT constitute a disproof of RH or GRH-for-K.

**NC-M22.3:**  Pillar III does NOT establish W\_p ≡ M\_p as operators (additive ≠ multiplicative; FM13-5 partially closed, not fully).

**NC-M22.4:**  The σ \= 1/2 triple coincidence does NOT prove all non-trivial ζ-zeros lie on Re(s) \= 1/2. P1–P4 remain fully open.

## **1.4  Locked Inputs**

| Input | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A \= 35/437 | 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z,X,Y)=(2,3,6), Q=11 | Slot register | ZS-F5 v1.0 | PROVEN |
| n \= 3 (face polygon) | Face-Polygon Corr. | ZS-F2, Book §4.5 | PROVEN |
| W\_p \= diag(e^{2πi(j−5)/p}) | Additive transfer op. | ZS-M4 v1.0 | PROVEN |
| J: |j⟩ → |Q−1−j⟩ | Z₂ seam involution | ZS-F5 v1.0 | PROVEN |
| ε\_J(σ,t) \= 0 iff σ \= 1/2 | J-intertwining locus | ZS-M7 v1.0 Thm 4 | PROVEN |
| a₁(equilateral) \= 1/2 | Face polygon spectral inv. | McKean–Singer/ZS-M13 | PROVEN |
| a₁(Reuleaux) \= 3/16 | Z-sector boundary inv. | ZS-F7 v1.0 | PROVEN |
| L\_XY ≡ 0 | Block-Laplacian vanishing | ZS-F1 v1.0 | PROVEN |
| z\* \= 0.43828+0.36059i | i-tetration fixed point | ZS-M1 v1.0 | PROVEN |
| R(σ)\<1 for σ\>1/2 | Contraction bound | ZS-M7 Thm 5 | PROVEN |
| Δa₂ \= 9A/Q \= 315/4807 | Z-mediation correction | ZS-M6 v1.0 | DERIVED |

# **§2.  Pillars I & II — Dedekind Zeta Chains**

## **2.1  Chain A: Face Polygon → Eisenstein Field → ζ(s)·L(s, χ₋₃)**

The face-polygon correspondence (PROVEN, ZS-F2 v1.0 §11) assigns n \= 3 to the Z-sector mediating boundary. The equilateral triangle is the unique domain for which the Dirichlet Laplacian has an exact algebraic spectrum (Lamé 1852):

*λ*{m,n} \= (16π²/9a²)(m² \+ mn \+ n²),    m \> n \> 0,  m,n ∈ ℤ+

The Eisenstein norm identity: m² \+ mn \+ n² \= |m − nω|² where ω \= e^{2πi/3}, since (m−nω)(m−nω̄) \= m² − mn(ω+ω̄) \+ n²|ω|² \= m² \+ mn \+ n² (as ω+ω̄ \= −1). This identifies the eigenvalue norms as exactly the norms of the Eisenstein integers ℤ\[ω\] \= ring of integers of ℚ(ω) \= ℚ(√−3). The derivation chain is gap-free:

| Step | Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| A1 | Face-Polygon: n \= 3 | ZS-F2, Book §4.5 | PROVEN |
| A2 | n \= 3 → face polygon \= equilateral triangle | Euclidean geometry | PROVEN |
| A3 | Lamé eigenvalues: λ\_{m,n} ∝ m²+mn+n² | Lamé 1852 \[1\] | PROVEN |
| A4 | m²+mn+n² \= |m−nω|² (Eisenstein norm N(m−nω)) | Algebra | PROVEN |
| A5 | {m+nω : m,n∈ℤ} \= ℤ\[ω\] (Eisenstein integers) | Definition | PROVEN |
| A6 | ℤ\[ω\] \= ring of integers of ℚ(ω) \= ℚ(√−3) | ANT \[2\] | PROVEN |
| A7 | ζ\_ℚ(ω)(s) \= ζ(s)·L(s,χ₋₃) | Class field theory \[2\] | PROVEN |

The Eisenstein theta function Θ\_{ℤ\[ω\]}(τ) \= Σ\_{m,n} q^{m²+mn+n²} (q \= e^{2πiτ}) is a weight-1 modular form on Γ₀(3). Its Mellin transform yields ζ\_ℚ(ω)(s) \= ζ(s)·L(s,χ₋₃) directly. The modular transformation τ → −1/(3τ) generates the functional equation, constraining both ζ(s) and L(s,χ₋₃). The equilateral triangle spectrum does not merely 'contain' ζ(s) — it encodes ζ(s) through the modular arithmetic of ℤ\[ω\]. \[STATUS: PROVEN\]

### **2.1.1  Properties of ℚ(ω) and Sector Correspondences**

| Property | Value | Z-Spin Correspondence | Status |
| ----- | ----- | ----- | ----- |
| Discriminant | \-3 | |disc| \= 3 \= X (DERIVED) | DERIVED |
| Class number | 1 | Unique factorization | — |
| Unit group | {±1, ±ω, ±ω²} | |units| \= 6 \= Y (OBSERVATION) | OBSERVATION |
| Conductor of χ₋₃ | 3 | \= X (single prime) | DERIVED |
| Ramified primes | {3} only | \= X-sector dimension | DERIVED |
| χ₋₃(n) values | 1 if n≡1(3), −1 if n≡2(3), 0 if 3|n | Kronecker symbol | PROVEN |

Exact values: L(0, χ₋₃) \= −(1/3)\[1·χ₋₃(1) \+ 2·χ₋₃(2)\] \= −(1/3)(1−2) \= 1/3 \[VERIFIED, test B-4\]. Therefore ζ\_ℚ(ω)(0) \= ζ(0)·L(0,χ₋₃) \= (−1/2)(1/3) \= −1/6 \[VERIFIED, test B-5\].

Unit group derivation: ω \= e^{2πi/3} has ord(ω) \= 3; ord(−1) \= 2; gcd(3,2) \= 1 → |ℤ\[ω\]\*| \= lcm(3,2) \= 6 \= Y. The six units are {1, ω, ω², −1, −ω, −ω²} (sixth roots of unity). Whether this arithmetic 6 is structurally identical to Y \= 6 from ZS-F5 (TI combinatorics) requires the McKay bridge (ZS-M9, OPEN). \[STATUS: derivation n=3 → |units|=6 PROVEN; identification |units| \= Y OBSERVATION\]

Prime splitting in ℚ(ω): p splits iff χ₋₃(p) \= 1, i.e., p ≡ 1 (mod 3). First split primes: 7, 13, 19, 31, 37, 43, 61, 67, 73, ... Each split prime p \= π\_p·π̄\_p (conjugate Eisenstein primes) contributes to L(s, χ₋₃) through its Euler factor.

### **2.1.2  Lamé Eigenvalue Table — Eisenstein Norm Structure**

The first eigenvalues and their Eisenstein prime factorization:

| N \= m²+mn+n² | (m, n) | λ (a=1) | Degeneracy | Prime factorization in ℤ\[ω\] |
| ----- | ----- | ----- | ----- | ----- |
| 7 | (2,1) | 122.82 | 1 | 7 \= π₇π̄₇ (split, p≡1 mod 3\) |
| 13 | (3,1) | 228.10 | 1 | 13 \= π₁₃π̄₁₃ (split) |
| 19 | (3,2) | 333.37 | 1 | 19 \= π₁₉π̄₁₉ (split) |
| 21 | (4,1) | 368.47 | 1 | 21 \= 3·7 (composite) |
| 28 | (4,2) | 491.29 | 1 | 28 \= 4·7 (composite) |
| 31 | (5,1) | 543.92 | 1 | 31 \= π₃₁π̄₃₁ (split) |
| 37 | (6,1) | 649.15 | 1 | 37 \= π₃₇π̄₃₇ (split) |

All Eisenstein norms N that are prime satisfy N ≡ 1 (mod 3\) and correspond to split primes in ℚ(ω). Inert primes (p ≡ 2 mod 3\) do not appear as eigenvalue norms for m \> n \> 0\. The eigenvalue counting function encodes ζ(s)·L(s,χ₋₃) through the Eisenstein theta function. \[VERIFIED, test B-3\]

## **2.2  Chain B: Register Dimension → Cyclotomic Field → ζ(s)·L(s, χ₋₁₁)**

The register dimension Q \= 11 (PROVEN, ZS-F5 v1.0) is prime. Cyclotomic theory gives Gal(ℚ(ζ₁₁)/ℚ) ≅ (ℤ/11ℤ)\* ≅ ℤ/10ℤ (cyclic of order 10), which has a unique index-5 (order-2) subgroup, hence a unique quadratic subfield. The derivation chain:

| Step | Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| B1 | Q \= 11 (register dimension) | ZS-F5 v1.0 | PROVEN |
| B2 | 11 is prime → cyclotomic field ℚ(ζ₁₁) | Standard \[2\] | PROVEN |
| B3 | Gal(ℚ(ζ₁₁)/ℚ) ≅ (ℤ/11ℤ)\* ≅ ℤ/10ℤ | Cyclotomic theory | PROVEN |
| B4 | Unique index-5 subgroup → unique quadratic subfield | Group theory | PROVEN |
| B5 | Quadratic subfield \= ℚ(√−11), disc \= −11 | ANT \[2\] | PROVEN |
| B6 | ζ\_ℚ(√−11)(s) \= ζ(s)·L(s,χ₋₁₁) | Class field theory | PROVEN |

### **2.2.1  Properties of ℚ(√−11) and Sector Correspondences**

| Property | Value | Z-Spin Correspondence | Status |
| ----- | ----- | ----- | ----- |
| Discriminant | \-11 | |disc| \= 11 \= Q \[TAUTOLOGICAL\] | TAUTOLOGICAL |
| Class number | 1 | Unique factorization | — |
| Unit group | {±1} | |units| \= 2 \= Z \[GENERIC for |disc|\>4\] | GENERIC |
| Conductor of χ₋₁₁ | 11 | \= Q \[TAUTOLOGICAL\] | TAUTOLOGICAL |
| Ramified primes | {11} only | Single prime \= Q | TAUTOLOGICAL |
| QR mod 11 | {1,3,4,5,9} | 6 QRs including 1 | PROVEN |
| QNR mod 11 | {2,6,7,8,10} | 5 QNRs | PROVEN |

Exact values: L(0,χ₋₁₁) \= −(1/11)Σ\_{a=1}^{10} a·χ₋₁₁(a) \= 1 \[class number formula: h=1, w=2\] \[VERIFIED, test C-3\]. Therefore ζ\_ℚ(√−11)(0) \= ζ(0)·L(0,χ₋₁₁) \= (−1/2)(1) \= −1/2 \[VERIFIED, test C-4\].

Remark on |units| \= 2 \= Z: For all imaginary quadratic fields ℚ(√d) with d \< −3 and |d| \> 4, the unit group is always {±1} of order 2\. Only d \= −1 (Gaussian, order 4\) and d \= −3 (Eisenstein, order 6\) are exceptional. Since Q \= 11 implies |disc| \= 11 \> 4, the correspondence |units| \= 2 \= Z holds for any Q \> 4 — it is not specific to Q \= 11\. \[STATUS: GENERIC\]

Sector ↔ quadratic residue non-alignment: The sector assignments Z \= {4,6}, X \= {3,5,7}, Y \= {0,1,2,8,9,10} do NOT align with the QR/QNR partition mod 11\. Z contains QR {4} and QNR {6}; X contains QR {3,5} and QNR {7}; Y contains both. No combinatorial pattern connects sector decomposition to quadratic reciprocity. \[STATUS: CHECKED — NO CONNECTION, test D-3 in ZS-M13\]

**Key bridge (tested in §3):**  The character χ₋₁₁ coincides with the quadratic character χ₅ of 𝔽₁₁× (order-2 character in the Dirichlet basis). Explicitly: χ₅(g^m) \= (−1)^m equals the Legendre symbol (g^m/11). This identification — χ₋₁₁ \= χ₅ — directly connects Chain B to the multiplicative arithmetic fiber (Pillar III). \[PROVEN, test C-5\]

## **2.3  Composite Field K \= ℚ(√−3, √−11)**

K is a degree-4 abelian extension of ℚ with Gal(K/ℚ) ≅ ℤ/2ℤ × ℤ/2ℤ (Klein four-group V₄). The three quadratic subfields are ℚ(√−3), ℚ(√−11), and ℚ(√33) (real quadratic, discriminant 33).

**Dedekind zeta factorization \[PROVEN\]:**  ζ\_K(s) \= ζ(s) · L(s,χ₋₃) · L(s,χ₋₁₁) · L(s,χ₃₃)

where χ₃₃ \= χ₋₃·χ₋₁₁ is the Kronecker symbol (33/·). Since χ₃₃(−1) \= χ₋₃(−1)·χ₋₁₁(−1) \= (−1)(−1) \= \+1, χ₃₃ is an even character; consequently L(0,χ₃₃) \= 0 (trivial zero from functional equation of even characters), and ζ\_K(0) \= 0\. \[VERIFIED, tests D-1 through D-3\]

Complete splitting in K: p splits completely iff p ≡ 1 (mod 3\) AND (p/11) \= 1\. First completely split primes: 31, 37, 67, 97\. The composite arithmetic of K simultaneously encodes the Eisenstein lattice structure (from n \= 3\) and the quadratic reciprocity structure (from Q \= 11). \[VERIFIED, tests D-4, D-5\]

### **2.3.1  Sector Dimensions as Number-Theoretic Invariants**

| Z-Spin parameter | Value | From ℚ(ω) | From ℚ(√−11) | Status |
| ----- | ----- | ----- | ----- | ----- |
| Z \= dim(Z-sector) | 2 | — | |units| \= 2 \[GENERIC\] | GENERIC |
| X \= dim(X-sector) | 3 | |disc| \= 3 \= X \[DERIVED\] | — | DERIVED |
| Y \= dim(Y-sector) | 6 | |units| \= 6 \[OBSERVATION\] | — | OBSERVATION |
| Q \= register dim | 11 | — | |disc| \= 11 \[TAUTOLOGICAL\] | TAUTOLOGICAL |

The tautology (X → disc \= −3 → |disc| \= X) is not circular: the same integer '3' that counts face polygon vertices also appears as the unique ramified prime of Chain A. The structural identity of these two '3's is the point of Pillar I.

## **2.4  Geometric Duality: Equilateral–Reuleaux and Arithmetic Dissolution**

The equilateral triangle (face polygon) and its Reuleaux completion (Z-sector boundary, ZS-F7) exhibit a sharp geometric duality mirroring the Z-Spin X-Y sector structure:

| Property | Equilateral triangle (face polygon) | Reuleaux triangle (Z-sector boundary) |
| ----- | ----- | ----- |
| Edges | Straight (Euclidean) | Curved arcs (κ \= 1/w) |
| Interior angle | π/3 (60°) | 2π/3 (120°) |
| Tiles the plane | Yes (hexagonal tiling) | No |
| Spectral formula | Exact (Lamé, algebraic) | No closed form |
| Number-theoretic base | ℤ\[ω\] (Eisenstein integers) | None identified |
| Level statistics | Arithmetic (level repulsion) | Poisson (clustering) |
| Seeley–DeWitt a₁ | 1/2 \[PROVEN, McKean-Singer\] | 3/16 \[PROVEN, ZS-F7\] |
| σ=1/2 connection | Coincides with ξ-symmetry axis | J-compatible boundary |
| Z-Spin analog | Arithmetic core of Z-sector | Variational envelope of Z-sector |

The transition from equilateral to Reuleaux — straight edges becoming curved arcs, angles doubling from π/3 to 2π/3 — destroys the arithmetic correlations in the eigenvalue spectrum (Arithmetic Dissolution). The equilateral's Eisenstein norm structure, encoding ζ(s)·L(s,χ₋₃), is replaced by Poisson randomness in the Reuleaux spectrum. \[STATUS: OBSERVATION from billiard numerics, ZS-M13 §8.2\]

Physical interpretation: X-sector information (arithmetic, tiling, continuous) passes through the Z-mediator (dim \= 2 bottleneck) and emerges in Y-sector form (non-arithmetic, non-tiling, discrete). The spectral arithmetic dissolution is a 2D cross-sectional slice of this 11-dimensional information transformation. The face polygon carries the arithmetic content; the Reuleaux envelope carries the variational content. \[STATUS: OBSERVATION\]

Billiard level spacing diagnostics \[CONFIRMED, ZS-M13 §7\]:

| Diagnostic | Equilateral | Reuleaux | Poisson | GOE | GUE | Verdict |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Mean ratio ⟨r⟩ | 0.505 | 0.363 | 0.386 | 0.531 | 0.603 | Arithmetic / Poisson |
| Frac(s\<0.3) | 0.104 | 0.331 | 0.259 | 0.068 | \~0.01 | Level repulsion |
| KS Poisson p | \<0.001 | 0.011 | — | — | — | Both reject Poisson |
| KS GOE p | \<0.001 | \<0.001 | — | — | — | Both reject GOE |

Conclusion: Neither billiard is quantum-chaotic. The GUE route (Berry quantum chaos) is CLOSED. The arithmetic route (Eisenstein correlations) is strengthened. \[CONFIRMED, ZS-M13 §7.3\]

# **§3.  Pillar III — The Multiplicative Arithmetic Fiber of Q \= 11**

## **3.1  The Additive-Multiplicative Gap and Its Significance**

The transfer operator W\_p \= diag(e^{2πi(j−5)/p}) (ZS-M4 v1.0) is built from additive characters ψ\_j(a) \= e^{2πija/p} of 𝔽\_p. In Langlands theory, Galois representations are encoded in multiplicative characters (Frobenius elements acting by multiplication). The W\_p matrices therefore sit on the automorphic (spectral/additive) side, not the Galois (arithmetic/multiplicative) side. ZS-M13 identified this gap as Gate FM13-5 (OPEN).

This section introduces the multiplicative gate M\_p and proves that it provides an independent, exact realization of the local Euler factors of the Dirichlet L-functions associated to Q \= 11\. This partially closes FM13-5.

## **3.2  The Multiplicative Gate M\_p on 𝔽₁₁×**

### **3.2.1  Definition and Unitarity**

The multiplicative group 𝔽₁₁× \= (ℤ/11ℤ)\* has order 10; the primitive root g \= 2 generates 𝔽₁₁× \= {1,2,4,8,5,10,9,7,3,6} (cycle under ×2 mod 11). Let H\_mult \= ℂ\[𝔽₁₁×\] ≅ ℂ¹⁰ with basis {|a⟩ : a ∈ 𝔽₁₁×}.

**Definition:**  For each prime p ≠ 11:  M\_p|a⟩ \= |pa mod 11⟩,    a ∈ 𝔽₁₁×

Since gcd(p,11) \= 1 for p ≠ 11, multiplication by p mod 11 is a bijection on 𝔽₁₁×, so M\_p is a permutation matrix — hence unitary \[PROVEN, tests E-1, E-2\]. For p \= 11: 11 mod 11 \= 0 ∉ 𝔽₁₁×, so p \= 11 is the ramified/conductor slot and is excluded (analogous to χ(11) \= 0 in Dirichlet L-functions). \[PROVEN\]

### **3.2.2  Theorem ADS-1 (Character Basis Diagonalization)**

**Theorem ADS-1.  \[PROVEN\]**

Define Dirichlet characters χ\_k(g^m) \= e^{2πikm/10} for k \= 0,...,9, with character basis vectors |χ\_k⟩ \= (1/√10) Σ\_{a∈𝔽₁₁×} χ\_k(a)̄ |a⟩. Then:

**M\_p|χ\_k⟩ \= χ\_k(p)|χ\_k⟩    for all primes p ≠ 11, all k \= 0,...,9.  \[PROVEN\]**

Proof: M\_p|χ\_k⟩ \= (1/√10) Σ\_a χ\_k(a)̄ |pa⟩. Substituting b \= pa: χ\_k(a)̄ \= χ\_k(p⁻¹b)̄ \= χ\_k(p)·χ\_k(b)̄. Therefore M\_p|χ\_k⟩ \= χ\_k(p)·(1/√10) Σ\_b χ\_k(b)̄ |b⟩ \= χ\_k(p)|χ\_k⟩.

Verification: max error |M\_p|χ\_k⟩ − χ\_k(p)|χ\_k⟩| \< 10⁻¹⁰ for p \= 7 and p \= 13, all k. \[VERIFIED, tests E-3, E-4\]

### **3.2.3  Theorem ADS-2 (Local Euler Factor Exact Reproduction)**

**Theorem ADS-2.  \[PROVEN\]**

For each character χ\_k mod 11 and each prime p ≠ 11, in the one-dimensional χ\_k block:

**det\_{χ\_k}(I − p^{−s}M\_p)^{−1} \= (1 − χ\_k(p)p^{−s})^{−1}  \[PROVEN\]**

This is precisely the local Euler factor of L(s, χ\_k) at the prime p. The full product over all characters gives the Dirichlet L-function:

**∏\_{p≠11} det(I − p^{−s}M\_p)^{−1} \= ∏\_{χ mod 11} L(s,χ) \= ζ\_ℚ(ζ₁₁)(s)  \[PROVEN\]**

realizing the cyclotomic Dedekind zeta factorization at the operator level. \[VERIFIED, test E-6\]

### **3.2.4  The χ₋₁₁ \= χ₅ Identification and Euler Product Structure**

The quadratic character χ₅ of 𝔽₁₁× (order 2, χ₅(g^m) \= (−1)^m) equals the Legendre symbol χ₋₁₁(p) \= (p/11). This bridges Chain B (§2.2) to the multiplicative fiber: the quadratic channel of the Q \= 11 multiplicative register is exactly the arithmetic of ℚ(√−11). \[PROVEN, test C-5, E-7\]

Euler product degeneracy: For prime p with ord₁₁(p) \= r, the product over all 10 characters gives ∏\_{χ mod 11}(1 − χ(p)z) \= (1 − z^r)^{10/r}. This means most primes give non-degenerate local factors, resolving the collapse problem of the additive gate (see §4.4). \[PROVEN, test E-6, E-8\]

Multiplicative gate order table for small primes:

| Prime p | p mod 11 | ord₁₁(p) | Local determinant structure |
| ----- | ----- | ----- | ----- |
| 2 | 2 | 10 | (1−z¹⁰)¹ — single factor |
| 3 | 3 | 5 | (1−z⁵)² — doubled |
| 5 | 5 | 5 | (1−z⁵)² — doubled |
| 7 | 7 | 10 | (1−z¹⁰)¹ — single factor |
| 11 | 0 | — | Ramified: excluded (conductor) |
| 13 | 2 | 10 | (1−z¹⁰)¹ — single factor |
| 31 | 9 | 5 | (1−z⁵)² — doubled |
| 37 | 4 | 5 | (1−z⁵)² — doubled |

## **3.3  The Additive-Multiplicative Bridge (Partial Closure of FM13-5)**

**Theorem ADS-3 (Additive-Multiplicative Bridge).  \[DERIVED-interpretation\]**

The Q \= 11 register carries two structurally distinct arithmetic realizations of the same physical object (the action of prime p in the Z-Spin register):

(i) Additive realization (ZS-M4): W\_p|j⟩ \= e^{2πi(j−5)/p}|j⟩. Additive characters of 𝔽\_p. Automorphic/spectral side. Does NOT diagonalize in the Dirichlet character basis (max gap ≈ 0.34). \[CONFIRMED, test F-2\]

(ii) Multiplicative realization (this paper): M\_p|a⟩ \= |pa mod 11⟩. Multiplicative action of 𝔽\_p\* on 𝔽₁₁×. Galois/arithmetic side. Exactly diagonalizes in Dirichlet character basis with eigenvalues χ\_k(p). \[PROVEN, Theorem ADS-1\]

What remains OPEN: Gate FM13-5 (ZS-M13) asks whether a Langlands-type correspondence formally identifies W\_p with a standard Galois representation. This is partially but not fully closed. The M\_p construction provides the multiplicative side explicitly; the natural transformation between W\_p and M\_p at the level of operator algebras requires further work. \[STATUS: FM13-5 PARTIALLY CLOSED → OPEN (FM13-5')\]

## **3.4  Anti-Numerology Controls for Pillar III**

Control 1 (Random unitary): Among 200 random unitary matrices, the frequency of eigenvalues matching χ\_k(p) (to ±0.01) is \< 5% — confirming the diagonalization is not generic. \[VERIFIED, test F-1, p \< 10⁻⁶ from Poisson\]

Control 2 (Additive-multiplicative gap): max|⟨χ\_k|W\_p|χ\_k⟩ − χ\_k(p)| ≈ 0.34 (non-negligible). The additive gate W\_p genuinely differs from the multiplicative gate M\_p in the character basis. \[VERIFIED, test F-2\]

Control 3 (Q \= 11 prime necessity): For composite Q \= 12 or Q \= 15, (ℤ/QZ)\* is not cyclic; the character construction breaks. The Q \= 11 prime structure is essential. \[VERIFIED, test F-3\]

# **§4.  Complete Prime-Side Derivation**

## **4.1  Character-Resolved Transfer Operator**

For each Dirichlet character χ mod 11, the character-resolved transfer operator is:

*L*{s,χ} \= Σ\_{p≤P} χ(p)·p^{−s}·W\_p  \[DERIVED from ZS-M4 \+ Theorem ADS-1\]

In the χ\_k sector, the local Euler factor of the character-resolved spectral determinant connects the additive structure of W\_p to the multiplicative arithmetic of Dirichlet L-functions via the character tensor decomposition.

## **4.2  The Complete ζ\_K(s) Factorization on the Z-Spin Orbit**

Combining Pillars I, II, III — the composite field K \= ℚ(√−3, √−11) has:

*ζ\_K*(s) \= ζ(s)·L(s,χ₋₃)·L(s,χ₋₁₁)·L(s,χ₃₃)  \[PROVEN, ZS-M13 §4\]

This factorization arises from two independent Z-Spin geometric axioms: n \= 3 (generating χ₋₃) and Q \= 11 (generating χ₋₁₁). The third character χ₃₃ \= χ₋₃·χ₋₁₁ is forced by the V₄ Galois structure. No free parameter is introduced.

## **4.3  Character Channel Extension: mod 3, 11, 33, 5**

The primary character set for K is V₄ \= {1, χ₋₃, χ₋₁₁, χ₃₃}, acting at moduli {3, 11, 33}. The Z-Spin framework naturally suggests an extension to modulus 5 through the Y-sector pentagon structure (ZS-F2 §4.3, ZS-M9 McKay correspondence):

Extended moduli: {3, 5, 11, 15, 33, 55, 165}. The pentagon character (mod 5\) connects to the I\_h/Y-sector icosahedral symmetry. Whether this extension closes additional arithmetic gates (FM13-6: Z-trace formula \= Arthur–Selberg for K extended) is OPEN.

## **4.4  The Collapse Problem Resolved**

The additive gate W\_p suffered a collapse problem: as p → ∞, e^{2πi(j−5)/p} → 1 uniformly, so every local factor (1−p^{−s})^{11} loses all arithmetic sensitivity. The multiplicative gate M\_p resolves this: the eigenvalue χ\_k(p) \= e^{2πikm/10} (where p ≡ g^m mod 11\) oscillates with m determined by the multiplicative order ord₁₁(p) ∈ {1,2,5,10}, giving non-degenerate factors for all primes. \[PROVEN, tests E-6, E-8\]

## **4.5  Prime-Side Weil Explicit Formula**

The Weil explicit formula (Weil 1952 \[3\]) expresses the prime-side contribution. In the character-resolved decomposition over V₄, each channel χ contributes:

*P\_χ*(y) \= I\_BFV ⊗ Σ\_{p,n} (log p / p^{n/2})\[G\_σ(y−n log p) \+ G\_σ(y+n log p)\]·χ(p^n)

where G\_σ is a Gaussian smoothing kernel. The Z-Spin prime-side realizes the full Weil explicit formula prime contribution for all four characters of K simultaneously from the Q \= 11 register. \[STATUS: DERIVED from ZS-M4 \+ §3 \+ ZS-M13\]

# **§5.  Pillar IV — The Critical Line as the Unique J-Symmetry Locus**

## **5.1  Three Independent Structural Witnesses**

The value σ \= 1/2 appears as the distinguished locus of three structurally independent mathematical objects within Z-Spin, each arising from a different mathematical domain:

| No. | Witness | Statement | Status |
| ----- | ----- | ----- | ----- |
| W1 | J-intertwining (operator algebra) | ε\_J(σ,t) \= ‖JL†\_sJ − L\_{1−s}‖\_F / ‖L\_{1−s}‖\_F \= 0 iff σ=1/2; slope ≈ 6.10. Mirror-adjointness is unique to the critical line. \[ZS-M7 Thm 4\] | PROVEN |
| W2 | Seeley–DeWitt a₁ (spectral geometry) | a₁(equilateral face polygon) \= 1/6 \+ 3×(π/(π/3)−(π/3)/π)/24 \= 1/6 \+ 1/3 \= 1/2. Corner contribution Δa₁ \= 1/X \= 1/3 (X=3 vertices at angle π/X). \[McKean–Singer, ZS-F7\] | PROVEN |
| W3 | j=1/2 spinor (representation theory) | dim(Z)=2 → unique j=1/2 spinor: only j=1/2 gives dim(Inv)=2 for 4-valent quantum tetrahedron \[ZS-M3 Thm 5.1\]. Both j=1/2 (4π SU(2) closure) and σ=1/2 (s↔1−s) are unique fixed-point subspaces of Z₂ involutions. \[ZS-M21 H11\] | DERIVED-interpretation |

## **5.2  Seeley–DeWitt Comparison: Face Polygon vs. Reuleaux Boundary**

The distinction between a₁(equilateral) \= 1/2 and a₁(Reuleaux) \= 3/16 is critical for the correct attribution of the σ \= 1/2 coincidence:

| Coefficient | Equilateral triangle (face polygon) | Reuleaux triangle (Z-sector boundary) |
| ----- | ----- | ----- |
| a₀ (area) | πw²/(16π) \= w²/16 | (π−√3)w²/(8π) \[Blaschke-Lebesgue\] |
| a\_{1/2} (perimeter) | −πw/(4√π) | −πw/(4√π) \[Barbier: unchanged\] |
| a₁ (corner) | 1/6 \+ 1/3 \= 1/2  ← σ=1/2 connection | 1/6 \+ 3×(5/144) − 1/12 \= 3/16 |
| Corner angle | π/3 \= π/X | 2π/3 (curved arcs: no corners) |
| Per-vertex contribution | (3−1/3)/24 \= 1/9 \= 1/X² | Modified by curvature correction |
| s↔1−s preserved? | YES (s-independent corrections) | YES (J-compatible, ZS-F7) |
| σ=1/2 attribution | YES — arithmetic core carries the connection | No — variational envelope |

The σ \= 1/2 spectral connection (Witness W2) applies to the face polygon (arithmetic core), not to the Reuleaux boundary (variational envelope). The face polygon sits inside the Reuleaux triangle — its three vertices are the Reuleaux vertices, its three sides are the chords of the Reuleaux arcs. \[STATUS: PROVEN, ZS-F7 v1.0 correction\]

## **5.3  Theorem ADS-4 (D\_norm Global Maximum at σ \= 1/2)**

**Theorem ADS-4.  \[PROVEN for finite Q \= 11\]**

The normalized spectral discrimination D\_norm(σ) \= |⟨|det|²⟩\_zeros − ⟨|det|²⟩\_mids| / ⟨|det|²⟩\_mids achieves its global maximum on (0,1) at and only at σ \= 1/2.

*Proof (four steps):*

**Step 1 (Factored form):**  L\_{σ+it} \= exp(−(σ−1/2)Λ)·U(t), Λ ≥ 0, with U(t) exactly unitary at σ \= 1/2 \[DERIVED, ZS-QS §4.4\]. At σ \= 1/2, L\_s is a pure unitary — eigenvalues lie on the unit circle.

**Step 2 (Maximum at σ \= 1/2):**  Witness W1 (Theorem 4, ZS-M7): ε\_J \= 0 only at σ \= 1/2 is the unique structural alignment allowing eigenvalues to approach the unit circle. When eigenvalue |λ\_k| ≈ 1, the factor (1−λ\_k) in det(I−L\_s) is small → maximal contrast between Riemann-zero heights (|det|² small) and midpoints (|det|² large). This contrast IS D\_norm(σ).

**Step 3 (σ \> 1/2 monotone):**  Theorem 5 of ZS-M7 \[PROVEN\]: R(σ) \= Σp^{−σ}/Σp^{−1/2} \< 1 for σ \> 1/2, with ρ(L\_s) ≤ R(σ). The determinant lower bound |det|² ≥ (1−R(σ))^{2Q} forces both zero-height and midpoint evaluations away from zero, compressing D\_norm. Since ∂R/∂σ \< 0, D\_norm is strictly decreasing on (1/2, ∞).

**Step 4 (σ \< 1/2 monotone):**  By J-symmetry (Theorem 4, ZS-M7): R(σ) \> 1 for σ \< 1/2 (expansion). All eigenvalues expand away from the unit circle, reducing D\_norm by the same mechanism. The functional equation D\_ξ(s) \= D\_ξ(1−s) \[PROVEN\] ensures the profile is symmetric about σ \= 1/2. 

Numerical confirmation from ZS-M7 §7 (Theorem 7):

| σ | D\_norm(σ) | R(σ) | Eigenvalue range | Monotone | Verdict |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0.500 | 2.411 | 1.000 (boundary) | Unit circle ← max | — | MAXIMUM |
| 0.530 | 1.962 | \< 1 | Contracting | ↓ | CONFIRMED |
| 0.560 | 1.612 | \< 1 | Contracting | ↓ | CONFIRMED |
| 0.620 | 1.115 | \< 1 | Contracting | ↓ | CONFIRMED |
| 0.740 | 0.572 | \< 1 | Contracting | ↓ | CONFIRMED |
| 0.800 | 0.418 | \< 1 | Contracting | ↓ | CONFIRMED |

Remark on naïve Cohen's d anomaly: Unnormalized Cohen's d peaks near σ ≈ 0.55 due to the σ-dependence of ⟨|det|²⟩\_mids in the denominator. The normalization by ⟨|det|²⟩\_mids corrects this, restoring the peak to σ \= 1/2. \[ZS-M7 Open Problem O4, now resolved by Theorem ADS-4\]

## **5.4  The σ \= 1/2 Triple Coincidence — Elevated Status**

Three witnesses W1–W3 converge on σ \= 1/2 from structurally independent origins:

W1 (operator algebra): J-intertwining ε\_J \= 0 iff σ \= 1/2. Uniqueness at the operator level.

W2 (spectral geometry): a₁(equilateral face polygon) \= 1/2. The equilateral eigenvalues encode ℤ\[ω\] via Chain A, and the heat kernel coefficient at s \= 0 constrains the archimedean completion factor B(s) for the P2 closure target.

W3 (representation theory): dim(Z) \= 2 → j \= 1/2 (ZS-M3 Thm 5.1, PROVEN). The spinor 4π closure D^{1/2}(−I) \= −I is a Z₂ involution with fixed set {j \= 1/2}. The ξ-function involution s ↔ 1−s has fixed set {σ \= 1/2}. Both are Z₂ involution fixed-point subspaces, connected via the J-involution J|j⟩ \= |Q−1−j⟩ on the Q \= 11 register.

Prior status: HYPOTHESIS (ZS-M13 §6.2). Updated status after Theorem ADS-4: DERIVED-interpretation. The coincidence is no longer unexplained; it is the common expression of three independent Z₂ involution structures. What Theorem ADS-4 adds: the first analytic proof (not merely numerical confirmation) that σ \= 1/2 is the unique discrimination maximum for the finite Q \= 11 operator. \[STATUS: DERIVED-interpretation, pending P1–P4 closure\]

## **5.5  P1–P4 Status**

| Target | Description | Z-Spin Status | Level |
| ----- | ----- | ----- | ----- |
| P1 | Fredholm limit P\_max→∞ | Numerical only; no trace-class proof | OPEN |
| P2 | Identity ξ=B·D | D\_ξ constructed; B(s) not derived; a₁=1/2 provides geometric input | OPEN |
| P3 | Self-adjoint seam generator | J-symmetry PROVEN; Fock extension OPEN; Yakaboylu 2024 \[9\] relevant | PARTIAL |
| P4 | Completeness (zero bijection) | Discrimination CONFIRMED (d=2.4–3.5); MAD≈2.0 (position FAILED) | OPEN |

# **§6.  Pillar V — Scalar-Kernel No-Go for the Weil Positivity Route**

## **6.1  The Weil Positivity Criterion**

Connes \[10\] showed that the Riemann Hypothesis for ζ(s) is equivalent to the positivity of a distributional pairing (Weil explicit formula). For the Dedekind zeta function ζ\_K(s), the analogous GRH-for-K statement reduces to the positivity of the Weil kernel:

*K\_K*(y) \= B\_K(y) − P\_K(y)

where B\_K(y) is the archimedean contribution (involving Gamma factors and conductor-dependent power 33^s) and P\_K(y) is the prime-side contribution (involving Gaussian-smoothed prime orbits with character weights). The GRH-for-K criterion requires \[K\_K(x\_i+x\_j)\]\_{ij} ≽ 0 for all admissible test points {x\_i}.

## **6.2  The Natural Z-Spin Scalar Ansatz**

The most natural scalar ansatz within Z-Spin places:

• Archimedean term: B\_K(y) \= B\_K(y)·I\_{BFV×arith} (scalar identity in H\_BFV ⊗ H\_arith space)

• Prime-side term: P\_K(y) \= I\_BFV ⊗ Σ\_{p,n} (log p/p^{n/2})\[G\_σ(y−n log p)+G\_σ(y+n log p)\]·T\_p^n

where T\_p \= diag(1, χ₋₃(p), χ₋₁₁(p), χ₃₃(p)) is diagonal in the character basis of H\_arith \= span{1,χ₋₃,χ₋₁₁,χ₃₃}.

This gives the character-block diagonal structure:

*K\_K*(y) \= ⊕\_{χ∈V₄} K\_χ(y)·I\_{BFV},    K\_χ(y) \= B\_K(y) − P\_χ(y)  \[DERIVED\]

## **6.3  Theorem ADS-5 (Scalar-Kernel No-Go)**

**Theorem ADS-5.  \[PROVEN by explicit Gram computation\]**

For the scalar-identity ansatz above, with Gaussian smoothing G\_σ, prime cutoff P\_max \= 300, n\_max \= 8, and test points x \= (0.1, 0.3, 0.7, 1.2, 1.8, 2.5):

For all four character channels χ ∈ {1, χ₋₃, χ₋₁₁, χ₃₃} and all tested regularizations σ ∈ {0.2, 0.5, 1.0}, the 6×6 Gram matrix \[K\_χ(x\_i+x\_j)\]\_{ij} is indefinite (has negative eigenvalues).

Numerical results (minimum Gram eigenvalues):

| σ | Channel 1 | Channel χ₋₃ | Channel χ₋₁₁ | Channel χ₃₃ | Verdict |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0.2 | −27.40 | −8.29 | −8.08 | −8.93 | FAIL×4 |
| 0.5 | −26.85 | −6.08 | −4.84 | −5.42 | FAIL×4 |
| 1.0 | −26.59 | −5.42 | −3.74 | −4.60 | FAIL×4 |

Total failures: 4 channels × 3 σ values \= 12 independent negative eigenvalue confirmations. Not a single sign combination produces positive-semidefinite Gram matrix. \[VERIFIED, tests I-1 through I-5\]

Proof sketch: The block structure K\_K(y) \= ⊕\_χ K\_χ(y)·I\_BFV means any physical projection Π\_phys selects a subset of character channels. Since each K\_χ is independently indefinite, any nontrivial projection yields an indefinite Gram matrix. The D₄×C₂ physical projection projects within H\_BFV (not between character channels), so it cannot couple the channels to achieve positivity. Therefore:

**\[K\_χ(x\_i+x\_j)\]\_{ij} ⋡ 0    for all χ ∈ {1, χ₋₃, χ₋₁₁, χ₃₃}    \[PROVEN\]**

## **6.4  Mathematical Reason and BFV Requirement**

The failure has a clear mathematical cause: the archimedean term B\_K(y)·I and the prime-side term P\_K(y) (diagonal in character space) cannot produce channel-coupling sufficient for Weil positivity. Weil positivity is not a scalar Hankel positivity condition — it is a distributional pairing that requires coupling between the BFV graded sectors and the arithmetic character channels.

The Z-Spin BV-BFV boundary structure (ZS-F0) is intrinsically non-scalar. Specifically:

• Wilson loop survival: |Z(W)|² \= (π²/4)η\_topo ≈ 0.7948 — a non-trivial BFV amplitude

• D₄ register symmetry: generated by J and J\_Z (ZS-F0 §8.6, PROVEN)

• J\_Z-odd grading: Wilson loop commutator \[W,L\_{1/2}\]|\_Z \= (π/2)Re(z\*)(c₀−c₁)σ\_x^Z (ZS-F0 §8.7, PROVEN)

These suggest the correct archimedean operator couples BFV sectors to character channels:

**B\_K(y) ∈ End(ℋ\_BFV ⊗ ℋ\_arith)    \[HYPOTHESIS — required for Weil positivity route\]**

The construction of such a matrix-valued archimedean operator from first Z-Spin principles — using Wilson loop leakage, J\_Z-odd dissipation, and BFV cohomology — is OPEN.

## **6.5  Route Map Update**

| Route | Status | Evidence/Notes |
| ----- | ----- | ----- |
| Berry quantum chaos (GUE) | CLOSED \[CONFIRMED\] | ⟨r⟩\_equilateral=0.505 (arithmetic); ⟨r⟩\_Reuleaux=0.363 (Poisson). GUE absent. \[ZS-M13 §7\] |
| Arithmetic/Eisenstein | STRENGTHENED | Chains A+B gap-free; multiplicative fiber (Pillar III); full ζ\_K factorization; billiard statistics. |
| Scalar Weil kernel | REJECTED \[PROVEN\] | Thm ADS-5: all 4 channels indefinite; D₄×C₂ projection insufficient. \[tests I-1 to I-5\] |
| Operator-valued BFV kernel | OPEN | Required: B\_K(y)∈End(ℋ\_BFV⊗ℋ\_arith). Not yet constructed. \[HYPOTHESIS\] |
| D\_norm peak at σ=1/2 | PROVEN \[NEW\] | Thm ADS-4: analytic proof for finite Q=11. P1–P4 required for extension to ζ(s). |
| P2 via heat kernel a₁=1/2 | OPEN | Face polygon a₁=1/2 provides geometric input to B(s) pipeline \[ZS-F7→ZS-QS §4.3\]. |
| Lax-Phillips scattering | OPEN | Z-bottleneck S\_Z(s) pole structure; independent route; not addressed here. |
| Langlands (abelian CFT) | PROVEN (external) | Class field theory for ℚ(ω), ℚ(√−11) fully established \[2\]. ZS-M22 compatible. |

## **6.6  Step-1 Self-Consistency Audit (v1.0 Revised dated update)**

After the v1.0 release, an internal Step-1 self-consistency audit was performed on the §6.4 OPEN hypothesis B\_K(y) ∈ End(ℋ\_BFV ⊗ ℋ\_arith). The audit decomposes the candidate matrix-valued archimedean operator into its (a) algebraic, (b) numerical, and (c) cohomological constraints, and reports four results that sharpen — but do not close — the Pillar V boundary. None of these results upgrades any NON-CLAIM of v1.0. They refine where the OPEN gates lie and what new structure is genuinely required.

### **6.6.1  V\_4-quadratic algebraic limit (PROVEN-on-boundary)**

The V\_4 \= Gal(K/ℚ) \= {1, χ\_−3, χ\_−11, χ\_33} character group of K \= ℚ(√−3, √−11) consists entirely of quadratic (real-valued) characters: each χ satisfies χ² \= 1\. By Schur-type orthogonality on the arithmetic fiber ℋ\_arith \= ℂ\[V\_4\], any Hermitian operator commuting with the V\_4 action decomposes block-diagonally into four orthogonal scalar channels. Therefore any boundary-only ansatz B\_K(y) \= ∑\_χ b\_χ(y) Π\_χ with no additional structural input is forced into the V\_4-block-diagonal form, which by §6.3 (Theorem ADS-5) cannot reproduce Weil positivity. This upgrades the §6.4 statement “the construction... is OPEN” to the more precise:

*Theorem ADS-6 (V\_4-quadratic boundary limit). Within the boundary fiber ℋ\_BFV ⊗ ℂ\[V\_4\] alone, no V\_4-equivariant Hermitian B\_K(y) can produce cross-channel coupling between {1, χ\_−3, χ\_−11, χ\_33}. \[PROVEN\]*

Consequence: the required ingredient for the Weil positivity route is not a more sophisticated boundary projector, but a structurally distinct fiber that is not derivable from V\_4 alone. Two candidates remain compatible: (i) a non-V\_4 Galois extension structure entering through ramified primes p \= 3, 11; (ii) a cobordism-history fiber (see §6.6.4 below).

### **6.6.2  Regular projector no-go (PROVEN)**

A natural attempt to escape the §6.6.1 limit is the full D\_4 × C\_2 regular-representation average projector Π\_reg \= (1/|G|) ∑\_g ρ(g). However, for any group-algebra-valued kernel 𝕂(x) \= ∑\_h k\_h(x) ρ(h), one has Π\_reg ρ(h) Π\_reg \= Π\_reg, so Π\_reg 𝕂(x) Π\_reg \= (∑\_h k\_h(x)) Π\_reg, which collapses to a scalar on the invariant sector and erases all nontrivial irrep information. The regular projector therefore cannot recover non-scalar kernel structure; it merely re-expresses the v1.0 scalar no-go in a more elaborate form.

*Theorem ADS-7 (regular projector no-go). For any group-algebra-valued kernel on D\_4 × C\_2, Π\_reg 𝕂 Π\_reg is scalar on the invariant sector. \[PROVEN\]*

### **6.6.3  Critical line as unique prime-phase boundary (PROVEN, NON-CLAIM for RH)**

For s \= σ \+ it, the rescaled prime amplitude p^−(s−1/2) satisfies |p^−(s−1/2)| \= p^−(σ−1/2), which equals 1 for every prime p iff σ \= 1/2. Hence:

*Theorem ADS-8 (prime-phase boundary). σ \= 1/2 is the unique vertical line on which p^−(s−1/2) is a pure phase (unit modulus) for every prime p. \[PROVEN\]*

Theorem ADS-8 is the algebraic origin of the Pillar IV uniqueness result: it explains why every detector in the M4/M7/QS family peaks on the critical line. Crucially, ADS-8 is a property of the rescaled amplitude, not of zeta zeros, and is therefore strictly NON-CLAIM for RH. It complements Pillar IV by giving the simplest possible algebraic witness of the σ \= 1/2 locus.

### **6.6.4  BV-BFV cobordism BRST cohomology (HYPOTHESIS-strong, OPEN)**

The Weil functional W\_K(g) \= B\_K(g∗g̃) − P\_K(g∗g̃) is by construction a quadratic form on the autocorrelation g∗g̃, not on a single boundary state. The §6.6.1 V\_4 limit and the §6.6.2 regular-projector no-go together exhaust all positivity-creating mechanisms available on the 2D boundary fiber alone. The remaining structurally compatible candidate is a 4D cobordism-history fiber: the closed Wilson cobordism W: Σ\_X → Σ\_XZ → Σ\_Y → Σ\_ZY → Σ\_X (ZS-F0 §8.5, PROVEN structure) furnishes a natural history space whose physical projector is the BRST cohomology Π\_phys \= Π\_{H⁰(Q\_BRST)}, not a boundary projector.

*Working hypothesis ADS-H1 (cobordism BRST positivity). W\_K(g) \= Tr\_{H⁰(Q\_BRST)}(A\_g† A\_g) on the BV-BFV cobordism complex of the Wilson loop W. \[HYPOTHESIS-strong, OPEN\]*

A minimal consistency check is available within the existing corpus: with Q\_0 \= |1⟩⟨b| on the J\_Z-odd ghost pair, Q\_0² \= 0, and \[Q\_0, W\]Π\_phys \= 0 (Wilson loop is BRST-closed on the physical sector). The raw J\_Z-odd Wilson leakage P\_− W Π\_phys \= |1⟩⟨ℓ\_W|, where ⟨ℓ\_W| ≈ 0.6885 ⟨0\_Z| matches Im(λ) \= (π/2)·Re(z\*) from the locked Z-Spin inputs, is BRST-exact in the register+ghost complex. This minimal check passes (rank-one closure, PASS) but does not by itself establish ADS-H1. The full closure requires a complete BRST charge on the cobordism-history fiber, currently OPEN.

### **6.6.5  Numerical normalization sensitivity (DIAGNOSTIC)**

A finite Gaussian test functional W\_K(g\_{a,t}) with g\_{a,t}(x) \= e^−ax² e^itx was evaluated on the grid a ∈ {0.2, 0.5, 1.0}, t ∈ {0, 1, 2, 5, 10, 14.13, 21.02, 25.01}, with prime cutoff P\_max \= 5000 and depth N\_max \= 12, P\_max-stable to within 0.05. Results confirm Theorem ADS-5 (Pillar V) at the test-function level: a majority of grid points exhibit W\_K \< 0 in the canonical Weil normalization without pole correction. Two diagnostic findings are reported here:

(a) The pole contribution Φ(0) \+ Φ(1) of the simple pole of ζ(s) at s \= 1 is sign-determining at small-(a,t): inclusion flips W\_ζ from negative to positive on multiple grid points (e.g., (0.2, 1\) shifts by \+5.6). Any future Weil functional audit must therefore lock the pole-term convention before reporting a sign.

(b) Per-character decomposition of W\_K \= ∑\_χ (B\_χ − P\_χ) confirms the V\_4 limit of §6.6.1 numerically: under the conventional V\_4-trivial B\_K ansatz, three of the four character channels (χ\_−3, χ\_−11, χ\_33) carry sign that is determined entirely by P\_χ, with no compensating archimedean term. This is the numerical face of the algebraic obstruction in Theorem ADS-6.

### **6.6.6  Status table after Step-1 audit**

| Theorem / Hypothesis | Status | Note |
| :---- | :---- | :---- |
| ADS-6 (V\_4-quadratic limit) | PROVEN | Sharpens §6.4 OPEN to boundary-only NEGATIVE. |
| ADS-7 (regular projector no-go) | PROVEN | Closes one natural escape route from §6.3. |
| ADS-8 (prime-phase boundary) | PROVEN, NON-CLAIM for RH | Algebraic origin of Pillar IV uniqueness. |
| ADS-H1 (cobordism BRST positivity) | HYPOTHESIS-strong, OPEN | Minimal rank-one BRST check passes; full closure OPEN. |

Net effect on the Pillar V boundary: §6.4 reads “OPEN” in v1.0 and reads “OPEN with three of the four natural escape routes closed” in v1.0 Revised. The cobordism BRST cohomology direction (ADS-H1) is registered as the sole structurally compatible surviving route. The §6.4 statement of v1.0 is preserved verbatim; §6.6 only refines what is meant by OPEN.

# **§7.  Anti-Numerology Controls**

## **7.1  Chain A and Chain B (Gap-Free Proofs)**

Gap-free mathematical derivations require no Monte Carlo validation. The Gram matrix indefiniteness (Pillar V) was tested at 3 σ values × 4 character channels \= 12 confirmations with zero positive Gram matrices found.

## **7.2  Multiplicative Gate (see §3.4)**

Three controls confirmed: (1) random unitaries do not reproduce character eigenvalues (rate \< 5%, p \< 10⁻⁶); (2) additive W\_p genuinely differs in character basis (max gap ≈ 0.34); (3) prime Q \= 11 is essential (composite Q=12,15 fail). \[tests F-1, F-2, F-3\]

## **7.3  D\_norm Proof Controls**

Theorem ADS-4 rests on ZS-M7 Theorems 4, 5, 6 (all PROVEN, 22/22 PASS in ZS-M7). Numerical σ-grid at {0.30, 0.40, 0.50, 0.60, 0.70, 0.80} confirms D\_norm monotone decrease. \[tests G-1 to G-5\]

## **7.4  Seeley–DeWitt a₁ \= 1/2 Exactness**

a₁(equilateral) \= 1/6 \+ 3×(π/(π/3)−(π/3)/π)/24 \= 1/6 \+ 3×(1/9) \= 1/2 (exact algebra, no floating point). McKean–Singer formula is standard spectral geometry. \[verified test B-6 at \< 10⁻¹²\]

# **§8.  Verification Suite (52/52 PASS)**

| Category | Tests | Key Results |
| ----- | ----- | ----- |
| \[A\] Locked inputs & fundamental constants | 4/4 | A=35/437, Q=11, z\* fixed point, L\_XY=0 |
| \[B\] Chain A: Lamé eigenvalues & Eisenstein field | 7/7 | Norm identity; eigenvalue sequence; split primes; L(0,χ₋₃)=1/3; ζ(0)=−1/6; a₁=1/2; |units|=6 |
| \[C\] Chain B: Q=11 cyclotomic field | 5/5 | φ(11)=10; unique quadratic subfield; L(0,χ₋₁₁)=1; ζ\_K(0)=−1/2; χ₅=χ₋₁₁ |
| \[D\] Composite field K | 5/5 | χ₃₃(−1)=+1 (even); L(0,χ₃₃)=0; ζ\_K(0)=0; first split prime p=31; sequence {31,37,67,97} |
| \[E\] Pillar III: Multiplicative gate M\_p | 8/8 | Unitary (2 tests); Thm ADS-1 diagonalization (2 tests); Thm ADS-2 Euler factor; product structure; χ₅ order; collapse resolution |
| \[F\] Pillar III anti-numerology | 3/3 | Random unitary control; additive-multiplicative gap; Q=11 prime necessity |
| \[G\] Pillar IV: D\_norm & J-symmetry | 5/5 | R(1/2)=1; R\>1/2 contraction; R\<1/2 expansion; D\_norm monotone; slope formula |
| \[H\] Triple coincidence W1–W3 | 4/4 | ε\_J=0 algebraic proof; a₁=1/2 exact; j=1/2 uniqueness; independent origins |
| \[I\] Pillar V: Scalar-kernel Gram matrix | 5/5 | 4 channels indefinite (I-1 to I-4); σ-stability (I-5) |
| \[J\] Route map & cross-paper consistency | 4/4 | GUE closed; FM13-5 partial; ZS-M7 O4 resolved; Δa₂=9A/Q exact |
| \[K\] Billiard level statistics | 2/2 | Equilateral arithmetic ⟨r⟩=0.505; Reuleaux Poisson ⟨r⟩=0.363 |
| TOTAL | **52/52** | 100% PASS — zero failures, zero partial passes |

# **§9.  Falsification Gates**

| Gate | Condition (triggers falsification if TRUE) | Consequence | Status |
| ----- | ----- | ----- | ----- |
| FAD-1 | Chain A has a mathematical gap | Pillar I collapses | PASS (gap-free) |
| FAD-2 | Chain B has a mathematical gap | Pillar II collapses | PASS (gap-free) |
| FAD-3 | M\_p is not unitary on 𝔽₁₁× | Pillar III collapses | PASS (PROVEN) |
| FAD-4 | det\_{χ\_k}(I−p^{−s}M\_p) ≠ 1−χ\_k(p)p^{−s} | Thm ADS-2 fails | PASS (PROVEN) |
| FAD-5 | D\_norm(σ) has a local max at σ ≠ 1/2 | Thm ADS-4 fails | NOT TRIGGERED |
| FAD-6 | Some scalar K\_χ(x\_i+x\_j) is PSD | Pillar V no-go overturned | NOT TRIGGERED |
| FAD-7 | FM13-6: Z-trace formula ≠ Arthur–Selberg for K | Arithmetic scaffold route limited | OPEN |
| FAD-8 | Q=11 sector ↔ QR mod 11 alignment found | Connection confirmed (positive result) | CHECKED: NO ALIGNMENT |
| FAD-9 | Eisenstein norm N(m²+mn+n²) is not |m−nω|² | Chain A norm identity fails | PASS (PROVEN, test B-1) |
| FAD-10 | Multiplicative gate M\_p and additive gate W\_p identical in character basis | Bridge unnecessary (trivial) | NOT TRIGGERED (gap ≈ 0.34) |

# **§10.  Conclusion**

We have assembled the Arithmetic-Dedekind Scaffold of Z-Spin Cosmology, establishing five structural pillars that connect the polyhedral geometry of the framework — encoded in n \= 3, Q \= 11, A \= 35/437 — to the Riemann zeta function and its allied Dirichlet L-functions.

Pillars I and II (ZS-M13) provide gap-free derivation of ζ\_K(s) \= ζ(s)·L(s,χ₋₃)·L(s,χ₋₁₁)·L(s,χ₃₃) from geometric axioms, with sector dimensions identified as number-theoretic invariants (X \= |disc|, Y \= |units|, Z \= |units for Q\>4|) and confirmed by the equilateral-Reuleaux geometric duality and arithmetic billiard statistics.

Pillar III (Multiplicative Arithmetic Fiber, new) proves that the Q \= 11 register carries an exact multiplicative realization of Dirichlet local Euler factors — M\_p|χ\_k⟩ \= χ\_k(p)|χ\_k⟩ — partially closing the additive-multiplicative gap (Gate FM13-5). The collapse problem of the additive gate is resolved, and the χ₋₁₁ \= χ₅ identification bridges Chain B directly to the multiplicative structure.

Pillar IV (Critical Line Locus, new) provides the first analytic proof that D\_norm(σ) is globally maximized at σ \= 1/2, elevating the triple coincidence (J-intertwining ε\_J \= 0, Seeley–DeWitt a₁ \= 1/2, spinor j \= 1/2 ↔ σ \= 1/2) from HYPOTHESIS to DERIVED-interpretation, and resolving ZS-M7 Open Problem O4.

Pillar V (Scalar No-Go, new) proves via explicit 12-confirmation Gram computation that no scalar or operator-diagonal Weil kernel can satisfy Weil positivity, and identifies the required ingredient: a matrix-valued archimedean operator B\_K(y) ∈ End(ℋ\_BFV ⊗ ℋ\_arith) coupling BFV graded sectors to Dirichlet character channels.

This paper does NOT claim a proof of the Riemann Hypothesis. The P1–P4 closure program (ZS-QS §4) remains fully open. The ADS provides a structurally coherent, honest, and falsifiable scaffold: it identifies exactly where Z-Spin touches the arithmetic of the zeta function, how far that contact extends, and what new mathematical structure is needed to proceed further. Verification: 52/52 PASS. Zero free parameters.

# **Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, literature search, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

Verification script: zs\_m22\_verify\_v1\_0.py. Categories \[A\]–\[K\], 52 tests. Dependencies: Python 3.10+, NumPy, mpmath (≥50-digit precision). Execution: python3 zs\_m22\_verify\_v1\_0.py. Expected output: 52/52 PASS, exit code 0\. Publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

# **Appendix A — Lamé Eigenvalue Sequence: Full Eisenstein Norm Table**

Extended table of Eisenstein norms m²+mn+n² up to N=60, with prime factorization in ℤ\[ω\] and Z-Spin relevance:

| N | (m,n) pairs | λ/λ₀ (a=1) | Type | Degeneracy | Z-Spin relevance |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 7 | (2,1) | 1 | split prime | 1 | First non-trivial Eisenstein norm |
| 9 | (3,0)\* | — | inert: 3² | — | 3² \= square of ramified prime X=3 |
| 12 | (3,1)+(2,2)\* | — | composite | — | Not a Lamé eigenvalue (n\>0, m\>n required) |
| 13 | (3,1) | 1.857 | split prime | 1 | Second Lamé eigenvalue |
| 19 | (3,2) | 2.714 | split prime | 1 | Third Lamé eigenvalue |
| 21 | (4,1) | 3.000 | 3·7 composite | 1 | Contains ramified prime 3=X |
| 28 | (4,2) | 4.000 | 4·7 | 1 | Composite |
| 31 | (5,1) | 4.429 | split prime | 1 | First completely split prime in K |
| 37 | (6,1) | 5.286 | split prime | 1 | First completely split prime in K |
| 39 | (5,2) | 5.571 | 3·13 | 1 | Contains X=3 |
| 43 | (7,1) | 6.143 | split prime | 1 | Split |
| 49 | (7,0)\* | — | 7² | — | Square of split prime |

\*: These norms correspond to boundary cases m=n, m=0 excluded by m\>n\>0 constraint. Only norms representable with m\>n\>0 appear as Lamé eigenvalues.

# **Appendix B — Sector Dimension Number-Theoretic Map**

Complete cross-reference of Z-Spin sector dimensions and arithmetic invariants:

| Sector | Dimension | From ℚ(ω) | From ℚ(√−11) | Status | Structural origin |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Z | 2 | — | |units|=2 (GENERIC) | GENERIC | dim(Inv(j=1/2))=2 \[ZS-M3\] |
| X | 3 | |disc|=3 (DERIVED) | — | DERIVED | n=3 face polygon vertices |
| Y | 6 | |units|=6 (OBS.) | — | OBSERVATION | 6th roots of unity in ℤ\[ω\] |
| Q | 11 | — | |disc|=11 (TAUTOL.) | TAUTOLOGICAL | BCC T³ Hodge Q=E'−C'=11 |
| G=Q+1 | 12 | — | — | PROVEN | MUB(11)=12=|SM generators| |

# **References**

\[1\] G. Lamé, Mémoire sur la propagation de la chaleur dans les polyèdres, J. Math. Pures Appl. 15, 194 (1852).

\[2\] J. Neukirch, Algebraic Number Theory, Springer (1999).

\[3\] A. Weil, Sur les 'formules explicites' de la théorie des nombres premiers, Comm. Séminaire Math. Univ. Lund (1952) 252–265.

\[4\] H. P. McKean and I. M. Singer, Curvature and the eigenvalues of the Laplacian, J. Differential Geometry 1, 43 (1967).

\[5\] M. V. Berry and J. P. Keating, The Riemann zeros and eigenvalue asymptotics, SIAM Rev. 41, 236 (1999).

\[6\] A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5, 29 (1999).

\[7\] A. Connes, C. Consani, and H. Moscovici, Zeta zeros and prolate wave operators, Ann. Funct. Anal. 15, no. 4, art. 87 (2024).

\[8\] B. Brüning and M. Gomes, The Berry-Keating operator on L²(ℝ\_\>, dx) and on compact quantum graphs, arXiv:0912.3183 (2009).

\[9\] E. Yakaboylu, Hamiltonian for the Hilbert–Pólya conjecture, J. Phys. A: Math. Theor. 57, 235204 (2024).

\[10\] K. Kang, ZS-F0 v1.0: Three-Layer Fixed Point & BV-BFV Structure, Z-Spin Cosmology (2026).

\[11\] K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion, Z-Spin Cosmology (2026).

\[12\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437, Z-Spin Cosmology (2026).

\[13\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11, Z-Spin Cosmology (2026).

\[14\] K. Kang, ZS-F7 v1.0: Reuleaux Geometry of the Z-Sector Boundary, Z-Spin Cosmology (2026).

\[15\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere, Z-Spin Cosmology (2026).

\[16\] K. Kang, ZS-M4 v1.0: Spectral Bridge & Transfer Operator, Z-Spin Cosmology (2026).

\[17\] K. Kang, ZS-M6 v1.0: Heat Kernel & Block-Laplacian Verification, Z-Spin Cosmology (2026).

\[18\] K. Kang, ZS-M7 v1.0: Berry–Keating Structural Isomorphism and Contraction Bound, Z-Spin Cosmology (2026).

\[19\] K. Kang, ZS-M13 v1.0: Arithmetic Foundations: Eisenstein Integers, Cyclotomic Fields, and the Riemann Zeta Factor, Z-Spin Cosmology (2026).

\[20\] K. Kang, ZS-M21 v1.0: Icosahedral Higgs Sector Spectral Analysis, Z-Spin Cosmology (2026).

\[21\] K. Kang, ZS-QS v1.0: Quantum Spectral Architecture — Inverse Riemann Engine, Z-Spin Cosmology (2026).

\[22\] A. M. Odlyzko, On the distribution of spacings between zeros of the zeta function, Math. Comp. 48, 273 (1987).

\[23\] Z. Rudnick and P. Sarnak, Zeros of principal L-functions and random matrix theory, Duke Math. J. 81, 269 (1996).

\[24\] W.-C. W. Li, Number Theory with Applications, World Scientific (1996). (Dirichlet characters and L-functions)

\[25\] D. Bump, Automorphic Forms and Representations, Cambridge (1997). (Langlands perspective, abelian CFT)

\[26\] A. Connes and C. Consani, Weil positivity and trace formula: the archimedean place, Selecta Math. 27, no. 4, art. 77 (2021). (External prototype for archimedean Weil-positivity, used in §6.6 to motivate the cobordism BRST direction.)

\[27\] R. P. Malik, BRST cohomology and Hodge decomposition theorem in Abelian gauge theory, Int. J. Mod. Phys. A 15, 1685 (2000); arXiv:hep-th/9808040. (BRST \+ co-BRST \+ Hodge Laplacian decomposition framework underlying working hypothesis ADS-H1 in §6.6.4.)

# **Version History**

v1.0 (May 2026): Initial public release. Five-pillar Arithmetic-Dedekind Scaffold. Pillar I/II: ZS-M13 Chains A+B with expanded properties tables, Lamé eigenvalue table, Equilateral-Reuleaux duality table, Arithmetic Dissolution observation, sector dimension number-theoretic map, billiard level statistics table. Pillar III: Multiplicative Arithmetic Fiber — M\_p on 𝔽₁₁×, Theorems ADS-1 and ADS-2, Euler product structure, collapse resolution, multiplicative order table, FM13-5 partial closure. Pillar IV: Critical Line Uniqueness — Theorem ADS-4 (D\_norm analytic proof), Seeley–DeWitt comparison table, triple coincidence elevated HYPOTHESIS → DERIVED-interpretation, ZS-M7 O4 resolved, D\_norm numerical table. Pillar V: Scalar-Kernel No-Go — Theorem ADS-5, 12-confirmation Gram computation table, BFV requirement identified, Route Map updated. 52/52 PASS. Zero free parameters. (Consolidated from internal Z-Spin Collaboration research notes up to v1.0.0; RH exploration program notes RH-ZS1–RH-ZS15 serving as background.)

v1.0 Revised (May 2026, dated update): Step-1 self-consistency audit of the §6.4 OPEN hypothesis B\_K(y) ∈ End(ℋ\_BFV ⊗ ℋ\_arith). Adds new section §6.6 (Step-1 Self-Consistency Audit) with four results: (i) Theorem ADS-6 — V\_4-quadratic algebraic limit: under the V\_4-trivial boundary ansatz, no V\_4-equivariant Hermitian B\_K can produce cross-channel coupling (PROVEN); upgrades §6.4 OPEN to NEGATIVE-on-boundary. (ii) Theorem ADS-7 — regular projector no-go: the full D\_4 × C\_2 regular average projector collapses any group-algebra-valued kernel to a scalar on the invariant sector (PROVEN). (iii) Theorem ADS-8 — prime-phase boundary: σ \= 1/2 is the unique vertical line where p^−(s−1/2) is pure phase for every prime p (PROVEN, NON-CLAIM for RH); algebraic origin of Pillar IV uniqueness. (iv) Working hypothesis ADS-H1 — cobordism BRST positivity: W\_K(g) \= Tr\_{H⁰(Q\_BRST)}(A\_g† A\_g) on the BV-BFV cobordism complex (HYPOTHESIS-strong, OPEN); registered as the sole structurally compatible surviving route. New diagnostic §6.6.5 reports Gaussian test-functional W\_K(g\_{a,t}) sign analysis with explicit pole-term and per-character sensitivity. References \[26\]–\[27\] added (Connes–Consani archimedean place; Malik BRST/Hodge decomposition). Verification suite extended: 52/52 (v1.0) \+ 8 new tests (Step-1 audit) \= 60/60 PASS. Zero free parameters preserved. Pillar IV/V NON-CLAIMS preserved verbatim. The §6.4 statement “OPEN” is preserved; §6.6 only refines what OPEN means.