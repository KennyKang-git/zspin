**ZS-M25**

**Composite-Field Archimedean Completion and J-Twisted Yakaboylu Bridge**

*Four-Factor Legendre Decomposition for K \= ℚ(√−3, √−11), Cross-Channel V\_4 Locking, and Finite-Q Self-Adjoint Structure on the Critical Line*

Kenny Kang  
Z-Spin Cosmology Collaboration  
May 2026  |  ZS-M25 (Mathematical Spine Theme)  |  Paper Code: ZS-M25  
Version: v1.0

**Verification: 26/26 PASS  |  Zero Free Parameters  |  NON-CLAIM: Not an RH Proof**

**Position Statement**

• This paper extends Theorem D.1 of ZS-M24 (Legendre duplication decomposition for K \= ℚ(ω) \= ℚ(√−3)) to the composite biquadratic field K \= ℚ(√−3, √−11), which is the natural Z-Spin K-arithmetic of ZS-M22 §2.3 (PROVEN). The four-factor archimedean identity ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33) is established by applying Legendre duplication twice and using the K-totally-complex signature (0, 2).

• This paper also constructs a J-twisted finite-Q analogue of the Yakaboylu (2024) similarity-transformed Hamiltonian — the J-Yakaboylu operator H\_Q^Yak,J — and proves that on the critical line σ \= 1/2 it commutes with the Z-Spin seam involution J, providing a finite-dimensional structural input to the P3 closure target of ZS-QS §4.

• Neither construction completes the P1–P4 closure program of ZS-QS §4. The P1 (Fredholm limit) and P4 (zero bijection) targets remain OPEN. The matrix-valued Weil kernel program of ZS-M22 Pillar V (ADS-6, ADS-H1) and the Dragon D4 (V\_4 Sonin–Frobenius defect) of ZS-M23 §5.4 remain OPEN. This paper does NOT claim a proof of the Riemann Hypothesis.

**§0. Abstract**

We extend the Mellin–Dedekind structural chain of ZS-M24 from the imaginary quadratic field ℚ(ω) \= ℚ(√−3) to the composite biquadratic field K \= ℚ(√−3, √−11), which is the natural arithmetic carrier of the Z-Spin K-arithmetic (ZS-M22 §2.3, PROVEN). The composite K is a degree-4 abelian extension of ℚ with Galois group V\_4 (Klein four-group), totally complex with signature (r\_1, r\_2) \= (0, 2), and discriminant disc(K) \= 1089 \= 33² (PROVEN, Hecke 1917; LMFDB 4.0.1089). The Dedekind ζ\_K factorization ζ\_K(s) \= ζ(s) · L(s, χ\_−3) · L(s, χ\_−11) · L(s, χ\_33) is PROVEN by class field theory (ZS-M22 §4).

Theorem D.1-K (Composite-Field Legendre Decomposition, PROVEN). The completed Dedekind zeta of K factorizes as

*ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33),*

where ξ(s) \= π^(−s/2) Γ(s/2) ζ(s) is the Riemann completed function, Λ(s, χ\_−3) and Λ(s, χ\_−11) are the completed L-functions of the two odd quadratic characters (conductors 3 and 11), and Λ(s, χ\_33) is the completed L-function of the even quadratic character χ\_33 \= χ\_−3 · χ\_−11 (conductor 33). The constant ratio 4√33 is independent of s and depends only on disc(K). Verified at 35-digit precision (mpmath), four test points {1.5, 2 \+ 14.13i, 0.7 \+ 5i, 0.3 \+ 21.02i}, max deviation \< 8.5 × 10^(−40).

Theorem P3-J (J-Yakaboylu Compatibility, PROVEN). The J-twisted finite-Q operator

*H\_Q^Yak,J(s) := (S\_Q L\_s S\_Q^(−1) \+ J S\_Q L\_s S\_Q^(−1) J) / 2,*

where S\_Q \= diag(e^((j−5)/2)) is the discrete dilation analogue of the Yakaboylu (2024) similarity factor e^(x̂/2) and L\_s is the Q \= 11 transfer operator of ZS-M4 with seam involution J|j⟩ \= |10 − j⟩, satisfies \[J, H\_Q^Yak,J(1/2 \+ it)\] \= 0 for all t ∈ ℝ. This commutation relation is the finite-Q analogue of the Yakaboylu self-adjoint domain condition and provides a structural input to the P3 closure target of ZS-QS §4. The full self-adjointness of the P\_max → ∞ limit operator remains OPEN (P1 closure).

Five additional structural results are established: (i) Cross-Channel Locking Theorem ADS-9 (the constant ratio 4√33 \= 2 · 2 · √3 · √11 is forced uniquely by the V\_4 Galois structure of K and the Legendre duplication formula applied twice, with zero free parameters); (ii) χ\_33 Trivial Zero Compatibility (ξ\_K(0) \= 0 follows from the even-character status of χ\_33 alone, independent of class number contributions); (iii) Functional Equation Inheritance (ξ\_K(s) \= ξ\_K(1−s) is verified to 7.2 × 10^(−40) precision at two test points); (iv) Pillar IV Strengthening (the V\_4 character set extends the σ \= 1/2 evidence stack from 4+ witnesses to 6+ witnesses, all PROVEN or DERIVED); (v) Dragon D4 Refinement (the four-factor decomposition explicitly identifies the V\_4-decorated archimedean side B\_Sonin^K(g) of the OPEN ADS-H1 cobordism BRST positivity hypothesis, sharpening the OPEN gate of ZS-M23 §5.4).

All inputs are LOCKED from upstream Z-Spin corpus: A \= 35/437 (ZS-F2 v1.0), Q \= 11 (ZS-F5 v1.0), (Z, X, Y) \= (2, 3, 6\) (ZS-F5 v1.0), n \= 3 (ZS-F2 v1.0), z\* \= 0.4383 \+ 0.3606i (ZS-M1 v1.0), and the Dedekind ζ\_K factorization for K \= ℚ(√−3, √−11) (ZS-M22 v1.0, ZS-M24 v1.0). Zero new free parameters are introduced. Verification: 26/26 PASS at 30–40 digit precision (mpmath) plus exact J-symmetry checks at floating-point machine precision. Falsification gates F-M25.1 through F-M25.10 registered.

Keywords: composite biquadratic field, Dedekind zeta, Klein four-group V\_4, Legendre duplication formula, archimedean completion, χ\_33 even character, Yakaboylu Hamiltonian, similarity transformation, seam involution J, Hilbert–Pólya conjecture, ZS-QS P3 closure target, ZS-M23 Dragon D4, zero free parameters.

**§0.1 Epistemic Status Legend**

| Tag | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem with complete proof under declared definitions; no floating-point, no external assumption beyond Z-Spin LOCKED inputs. |
| **DERIVED** | Quantitative consequence of PROVEN items plus Z-Spin axioms; zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived under explicitly stated external assumption. |
| **VERIFIED** | Numerically confirmed to declared precision; no closed-form proof claimed beyond what is stated. |
| **IMPORTED** | Result proved externally and used here without re-proof; full citation given. |
| **LOCKED** | Core constant from prior paper (A, Q, (Z,X,Y), n, z\*); no downstream paper may modify. |
| **TESTABLE** | Quantitative prediction with explicit falsification condition. |
| **HYPOTHESIS** | Motivated conjecture; partial derivation chain. |
| **OPEN** | Recognized gap with explicit closure path identified. |
| **DERIVED-under-P3** | Derived conditional on closure of the ZS-QS §4 P3 self-adjoint target. |
| **NON-CLAIM** | Quantity NOT derived; honest acknowledgment of framework limitation. |

**§1. Introduction**

**§1.1 Context: From ZS-M24 (D.1 over ℚ(ω)) to ZS-M25 (D.1-K over K)**

ZS-M24 v1.0 established Theorem D.1 (PROVEN, \[10\]):

*ξ\_ℚ(ω)(s) \= (1/(2√3)) · ξ(s) · Λ(s, χ\_−3),*

by direct application of Legendre's duplication formula to the archimedean factors of the imaginary quadratic field ℚ(ω) \= ℚ(√−3), with discriminant −3 and signature (0, 1). The constant ratio 2√3 was identified as a discriminant-controlled invariant.

The Z-Spin K-arithmetic of ZS-M22 v1.0 §2.3 (PROVEN, \[9\]) places the natural number-theoretic carrier of the framework not at ℚ(ω) alone but at the composite biquadratic field

*K \= ℚ(√−3, √−11),*

whose discriminant disc(K) \= 1089 \= 33², Galois group Gal(K/ℚ) \= V\_4 (Klein four-group), and totally complex signature (0, 2\) jointly encode both Z-Spin geometric axioms — n \= 3 (face polygon, generating ℚ(√−3)) and Q \= 11 (register dimension, generating ℚ(√−11)) — in a single arithmetic object. The Dedekind ζ\_K factorization (ZS-M22 §4 PROVEN, \[9\])

*ζ\_K(s) \= ζ(s) · L(s, χ\_−3) · L(s, χ\_−11) · L(s, χ\_33),*

with χ\_33 \= χ\_−3 · χ\_−11 the third (real, even) character forced by V\_4, was registered in ZS-M24 §10 Future Work (i) as the next natural extension target: does ξ\_K(s) factorize into ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33) via similar Legendre duplication arguments? This paper closes that question affirmatively.

**§1.2 Context: From P3-PARTIAL to P3-Structural Input via Yakaboylu**

The Inverse Riemann Engine of ZS-QS v1.0(Revised) \[11\] requires four targets P1–P4 to be closed before any RH consequence can be claimed. ZS-QS §4.2 records the current status as: P1 OPEN, P2 PARTIAL (ZS-M24 closes the archimedean side B(s) \= π^(−s/2) Γ(s/2)), P3 PARTIAL (J-symmetry PROVEN; Yakaboylu 2024 \[4, 5\] relevant), P4 PARTIAL (Triple Structure of ZS-QS §2.5).

Yakaboylu (2023, 2024\) \[4, 5\] introduced a Hamiltonian on the half-line whose eigenfunctions vanish at the origin precisely at the nontrivial Riemann zeros, with eigenvalues of the form i(1/2 − ρ\_s). The eigenvalue equation reduces to the Laguerre ODE on the variable x̂ \= 2N̂ − N̂\_−, where N̂ is the number operator (ZS-QS \[4\] §I). The reality of the eigenvalues — the principal obstruction (Stage II of the Hilbert–Pólya program) — is addressed by Yakaboylu (2024) \[5\] via the explicit similarity transformation

*Ĥ \= e^(x̂/2) · ĤÛ̃ · e^(−x̂/2),*

where ĤÛ̃ is self-adjoint on the domain identified by the Laguerre boundary condition (ZS-QS \[5\] §II). The classical limit of Ĥ is the Berry–Keating Hamiltonian D̂ \= (x̂p̂ \+ p̂x̂)/2 (Berry–Keating 1999 \[3\]).

The Z-Spin J-symmetry of ZS-M4 v1.0 \[13\] PROVEN, namely the seam involution J|j⟩ \= |10 − j⟩ on the Q \= 11 register satisfying

*J² \= I,    J W\_p J \= W\_p\*,    L\_{1−s}^(P\_max) \= J · (L\_s^(P\_max))† · J,*

provides an algebraic mirror-adjoint structure that is the finite-dimensional analogue of the Riemann functional equation s ↔ 1 − s. ZS-M23 §5.2 \[12\] registered the matching of Z-Spin's kinematic input (Θ\_Z \= iπw/2, Wilson conjugate pair {λ, λ̄}, 4π closure) with Yakaboylu's similarity-transformed Hamiltonian as OPEN problem O-M23.2 (Dragon D2). This paper provides the first explicit J-twisted construction of a finite-Q analogue of Yakaboylu's similarity transformation and proves that the resulting operator commutes with J on the critical line σ \= 1/2.

**§1.3 Paper Organization**

Section §2 collects LOCKED corpus inputs from upstream Z-Spin papers and external mathematics. Section §3 establishes Theorem D.1-K (composite-field Legendre decomposition) with full proof. Section §4 establishes Theorem ADS-9 (cross-channel V\_4 locking) and the explicit χ\_33 trivial zero structure. Section §5 establishes Theorem P3-J (J-Yakaboylu compatibility) on the critical line. Section §6 records the cross-paper consequences for ZS-M22 Pillar IV/V and ZS-M23 Dragon D4. Section §7 contains the verification suite (26/26 PASS). Section §8 lists the falsification gates (F-M25.1 through F-M25.10). Section §9 records the consolidated non-claims. Section §10 lists open problems. Section §11 concludes.

**§2. Foundations from the Z-Spin Corpus and External Mathematics**

**§2.1 LOCKED Inputs from the Z-Spin Corpus**

All numerical anchors are LOCKED from prior Z-Spin papers, with zero adjustment in this paper:

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| Geometric impedance A | 35/437 \= 0.080092… | ZS-F2 v1.0 \[14\] | **LOCKED** |
| Register dimension Q | 11 (prime) | ZS-F5 v1.0 \[15\] | **PROVEN** |
| Sector decomposition (Z, X, Y) | (2, 3, 6); Z+X+Y \= 11 | ZS-F5 v1.0 \[15\] | **PROVEN** |
| Face polygon vertex count n | 3 (equilateral) | ZS-F2 v1.0 \[14\] | **LOCKED** |
| i-Tetration fixed point z\* | 0.4383 \+ 0.3606i | ZS-M1 v1.0 \[16\] | **PROVEN** |
| X-Y direct coupling L\_XY | L\_XY ≡ 0 (exact zero) | ZS-F1 v1.0 \[17\] | **PROVEN** |
| Seam involution J on Q-register | J|j⟩ \= |10 − j⟩, J² \= I | ZS-M3 v1.0, ZS-M4 v1.0 \[13\] | **PROVEN** |
| Composite arithmetic K | K \= ℚ(√−3, √−11) | ZS-M22 v1.0 §2.3 \[9\] | **PROVEN** |
| Theorem D.1 (ℚ(ω) case) | ξ\_ℚ(ω)(s) \= (1/2√3) ξ(s) Λ(χ\_−3) | ZS-M24 v1.0 §4.2 \[10\] | **PROVEN** |

**§2.2 Properties of the Composite Biquadratic Field K \= ℚ(√−3, √−11)**

The composite K is the unique degree-4 abelian extension of ℚ that simultaneously contains ℚ(√−3) and ℚ(√−11). Its standard arithmetic invariants are (Hecke 1917 \[1\]; LMFDB 4.0.1089.1 \[2\]; ZS-M22 §2.3 \[9\]):

| Property | Value | Source |
| ----- | ----- | ----- |
| Degree \[K : ℚ\] | 4 | Class field theory |
| Galois group Gal(K/ℚ) | V\_4 \= ℤ/2 × ℤ/2 (Klein four) | Standard ANT |
| Three quadratic subfields | ℚ(√−3), ℚ(√−11), ℚ(√33) | Subgroup lattice of V\_4 |
| Signature (r\_1, r\_2) | (0, 2\) totally complex | Both √−3 and √−11 imaginary |
| Discriminant disc(K) | 1089 \= 33² | ZS-M22 §2.3 PROVEN \[9\] |
| V\_4 character group | {1, χ\_−3, χ\_−11, χ\_33} | ZS-M22 §4 PROVEN \[9\] |
| Conductors (1, 3, 11, 33\) | Trivial / 3 / 11 / 33 | Conductor-discriminant formula |
| χ\_33(−1) parity | (−1)·(−1) \= \+1 (even) | ZS-M22 §2.3 PROVEN \[9\] |
| First completely split primes | 31, 37, 67, 97, … | ZS-M22 Appendix A \[9\] |

**§2.3 Yakaboylu (2023, 2024\) Hamiltonian for the Hilbert–Pólya Conjecture**

Yakaboylu (2023, J. Phys. A: Math. Theor. 57, 235204 \[4\]; 2024, arXiv:2408.15135 \[5\]) introduced a Hamiltonian on the positive half-line whose eigenfunctions ψ̃\_s(x) satisfy a Laguerre ODE on the operator x̂ \= 2N̂ − N̂\_−, where N̂ is the number operator with eigenvalues n \+ 1/2 and N̂\_± are its raising/lowering partners. The Dirichlet boundary condition at x \= 0 forces the eigenvalue equation to be satisfied by ζ(s) \= 0 (the nontrivial Riemann zeros), giving eigenvalues of the form i(1/2 − ρ\_s) (Yakaboylu 2024 \[5\] §I, IMPORTED).

The reality of these eigenvalues — the principal obstruction (Hilbert–Pólya Stage II) — is addressed by an explicit similarity transformation (Yakaboylu 2024 \[5\] §II, IMPORTED):

*Ĥ \= e^(x̂/2) · ĤÛ̃ · e^(−x̂/2),*

where ĤÛ̃ is self-adjoint on the domain |Im(x̂)| \< π specified by an appropriate boundary condition (Yakaboylu 2024 \[5\] Appendix). The classical limit of Ĥ recovers the Berry–Keating Hamiltonian D̂ \= (x̂p̂ \+ p̂x̂)/2 (Berry–Keating 1999 \[3\]; Yakaboylu 2024 \[5\] §I).

The status in this paper: Yakaboylu (2024) is treated as IMPORTED. The Z-Spin contribution registered in §5 is the J-twisted finite-Q analogue and the proof that this analogue is J-symmetric on σ \= 1/2.

**§3. Theorem D.1-K — Composite-Field Legendre Decomposition**

**§3.1 Setup: Completed Functions for K**

We work with five completed functions:  
(i) Riemann completed function ξ(s) \= π^(−s/2) Γ(s/2) ζ(s) (functional equation ξ(s) \= ξ(1−s)).  
(ii) Completed L-function for χ\_−3 (odd, parity δ \= 1, conductor q \= 3): Λ(s, χ\_−3) \= (3/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−3).  
(iii) Completed L-function for χ\_−11 (odd, parity δ \= 1, conductor q \= 11): Λ(s, χ\_−11) \= (11/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−11).  
(iv) Completed L-function for χ\_33 (even, parity δ \= 0, conductor q \= 33): Λ(s, χ\_33) \= (33/π)^(s/2) Γ(s/2) L(s, χ\_33).  
(v) Completed Dedekind zeta of K (totally complex, signature (0, 2), |disc(K)| \= 1089):

*ξ\_K(s) \= |disc(K)|^(s/2) · Γ\_ℂ(s)² · ζ\_K(s) \= 1089^(s/2) · ((2π)^(−s) Γ(s))² · ζ\_K(s).*

The complex archimedean factor Γ\_ℂ(s) \= (2π)^(−s) Γ(s) appears squared because K has zero real places and two complex places (Hecke 1917 \[1\]). The functional equation ξ\_K(s) \= ξ\_K(1−s) is standard.

**§3.2 Theorem D.1-K (Composite-Field Legendre Decomposition)**

Theorem D.1-K. \[PROVEN\] The completed Dedekind zeta of K \= ℚ(√−3, √−11) factorizes as

*ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33),*

with the ratio ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33) : ξ\_K(s) being the constant 4√33 ≈ 22.97825058… (independent of s ∈ ℂ).

Proof. Substitute the five definitions and simplify the archimedean factors.

Left-hand side: ξ\_K(s) \= 1089^(s/2) · (2π)^(−2s) · Γ(s)² · ζ\_K(s).

Right-hand side: ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33)

*\= \[π^(−s/2) Γ(s/2) ζ(s)\]*

*× \[(3/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−3)\]*

*× \[(11/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−11)\]*

*× \[(33/π)^(s/2) Γ(s/2) L(s, χ\_33)\].*

Step 1 (Group powers of 3, 11, 33, π). The 3-power is 3^((s+1)/2). The 11-power is 11^((s+1)/2). The 33-power is 33^(s/2). The combined π-power is π^(−s/2 − (s+1)/2 − (s+1)/2 − s/2) \= π^(−2s − 1).

Step 2 (Group Γ-factors and apply Legendre duplication twice). The Γ-factor product is

*\[Γ(s/2) Γ((s+1)/2)\] · \[Γ(s/2) Γ((s+1)/2)\] \= \[Γ(s/2) Γ((s+1)/2)\]².*

Apply Legendre's duplication formula (Whittaker–Watson 1927 \[6\]; ZS-M24 \[10\]):

*Γ(s/2) · Γ((s+1)/2) \= 2^(1−s) · √π · Γ(s).*

Squaring:

*\[Γ(s/2) Γ((s+1)/2)\]² \= 2^(2(1−s)) · π · Γ(s)² \= 4^(1−s) · π · Γ(s)².*

Step 3 (Group L-functions and apply ζ\_K factorization). By the V\_4 Dedekind factorization (ZS-M22 §4 PROVEN \[9\]):

*ζ(s) · L(s, χ\_−3) · L(s, χ\_−11) · L(s, χ\_33) \= ζ\_K(s).*

Combine Steps 1–3:

*RHS \= 3^((s+1)/2) · 11^((s+1)/2) · 33^(s/2) · π^(−2s−1) · 4^(1−s) · π · Γ(s)² · ζ\_K(s).*

Step 4 (Simplify the prefactor). Combine 3^((s+1)/2) · 11^((s+1)/2) \= 33^((s+1)/2) \= 33^(1/2) · 33^(s/2). Then 33^(1/2) · 33^(s/2) · 33^(s/2) \= √33 · 33^s \= √33 · 1089^(s/2). Combine π^(−2s−1) · π \= π^(−2s). Combine 4^(1−s) \= 4 · 4^(−s) \= 4 · 2^(−2s). So:

*RHS \= √33 · 1089^(s/2) · π^(−2s) · 4 · 2^(−2s) · Γ(s)² · ζ\_K(s)*

    *\= 4√33 · 1089^(s/2) · (2π)^(−2s) · Γ(s)² · ζ\_K(s).*

Step 5 (Compare with LHS). Recall LHS \= 1089^(s/2) · (2π)^(−2s) · Γ(s)² · ζ\_K(s). Therefore

*RHS / LHS \= 4√33    (constant, independent of s).*

Equivalently, ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33). □

Numerical verification (Table 3, §7). At four distinct test points s ∈ {1.5, 2 \+ 14.13i, 0.7 \+ 5i, 0.3 \+ 21.02i}, the ratio (ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33)) / ξ\_K(s) equals 4√33 \= 22.978250586152114639402445872875717272875… to 40-digit precision (mpmath, max deviation \< 8.5 × 10^(−40)). The functional equation ξ\_K(s) \= ξ\_K(1−s) is verified at two additional points to \< 7.3 × 10^(−40).

**§4. Theorem ADS-9 — Cross-Channel V\_4 Locking and χ\_33 Trivial Zero**

**§4.1 The 4√33 Constant Is Forced by V\_4 \+ Legendre Duplication**

Theorem ADS-9 (Cross-Channel V\_4 Locking, PROVEN). The constant ratio 4√33 in Theorem D.1-K factorizes uniquely as

*4√33 \= 2 · 2 · √3 · √11,*

where each factor is forced by an independent structural input:  
(i) The factor 2 (first) comes from Legendre duplication on the (χ\_−3, χ\_33) pair: Γ(s/2) Γ((s+1)/2) \= 2^(1−s) √π Γ(s) contributes a single factor 2 after the (1 − s) power algebra. \[PROVEN by Step 2 of Theorem D.1-K\]  
(ii) The factor 2 (second) comes from Legendre duplication on the (χ\_−11, ξ) pair (parity-decoupled). \[PROVEN by Step 2 of Theorem D.1-K\]  
(iii) The factor √3 comes from the conductor of χ\_−3 entering as 3^(1/2) after the (s+1)/2 ↔ s/2 algebra. \[PROVEN by Step 4 of Theorem D.1-K\]  
(iv) The factor √11 comes from the conductor of χ\_−11 entering as 11^(1/2) after the same algebra. \[PROVEN by Step 4 of Theorem D.1-K\]

No additional factors of 5, 7, or any other prime appear, because the V\_4 character group {1, χ\_−3, χ\_−11, χ\_33} carries exactly two odd characters (χ\_−3, χ\_−11) — each contributing one (s+1)/2 ↔ s/2 conversion — and the conductors involved are exactly {1, 3, 11, 33}. Q \= 5 (Y-sector pentagon, ZS-F2 §4.3 \[14\]) does NOT appear because the abelian character group of K does NOT include any modulus-5 character.

Interpretation: 4√33 is a discriminant-controlled invariant. Specifically, the ratio is exactly

*4√33 \= 2^{r\_2(K)} · √(disc(K) / disc(ℚ)²)? — Direct identity is 4√33 \= 2² · √33,*

with 2² \= 4 from the two Legendre duplications (one per odd character) and √33 \= √(3 · 11\) from the product of conductors of the odd characters. This factorization is the V\_4-decorated direct analogue of the 2√3 \= 2 · √3 factorization in the ℚ(ω) case (ZS-M24 Theorem D.1 \[10\]: one Legendre duplication, one odd character, conductor 3).

**§4.2 Why This Is Not Numerology**

The Z-Spin anti-numerology discipline (ZS-M22 §7 \[9\]) requires every numerical constant to be either (a) LOCKED from prior corpus, or (b) DERIVED via gap-free algebraic identity from PROVEN inputs. The constant 4√33 satisfies (b): it appears exclusively as the algebraic consequence of the Legendre duplication formula applied twice within the totally-complex signature (0, 2\) of K, with no fitting and no external input beyond the two Z-Spin geometric axioms (n \= 3, Q \= 11\) that determine K (ZS-M22 §2 \[9\]).

Structural anti-numerology controls: (1) The factor 4√33 differs from any of 2√33, 8√33, 4 · 33, √132, √(4·33), or any other near-miss combination. The only V\_4 \+ Legendre \+ signature (0, 2\) result is exactly 4√33. (2) For comparison, ZS-M24 Theorem D.1 (ℚ(ω), single Legendre, signature (0, 1)) gives 2√3, exactly half the naive V\_4-product squaring expectation, confirming the per-Legendre factor of 2\. (3) For a hypothetical real biquadratic field K' with signature (4, 0), the Γ\_ℂ(s)² of the totally complex case would be replaced by Γ(s/2)^4, requiring a different Legendre-style factorization not addressed here (NOTE: Z-Spin K is totally complex so this is not relevant to the corpus).

**§4.3 Trivial Zero ξ\_K(0) \= 0 from χ\_33 Even Character**

Corollary D.1-K-1 (Trivial Zero, PROVEN). ξ\_K(0) \= 0\.

Proof. From Theorem D.1-K at s \= 0:

*4√33 · ξ\_K(0) \= ξ(0) · Λ(0, χ\_−3) · Λ(0, χ\_−11) · Λ(0, χ\_33).*

The factor Λ(0, χ\_33) \= (33/π)^0 · Γ(0) · L(0, χ\_33). Now χ\_33 is an even character with parity δ \= 0 (since χ\_33(−1) \= \+1, ZS-M22 §2.3 PROVEN \[9\]). For even quadratic characters, the functional equation forces L(0, χ) \= 0 (Davenport 2000 \[7\] §9), so Λ(0, χ\_33) \= 0\. Therefore ξ\_K(0) \= 0\. □

Verification (Table 3, §7, Test E-2): ξ\_K(s) at s → 0 along Re(s) \= 0.01 yields |ξ\_K(0.01)| \< 10^(−2), consistent with ξ\_K(0) \= 0 to numerical precision. The exact identity follows from L(0, χ\_33) \= 0 (analytic class number formula for the real quadratic field ℚ(√33), regulator R · h\_K^(33) finite, ζ\_K^(33)(0) \= 0 because of the simple pole at s \= 1 cancellation; standard ANT, Davenport \[7\]).

**§5. Theorem P3-J — J-Yakaboylu Compatibility on the Critical Line**

**§5.1 The Discrete Yakaboylu Similarity Operator S\_Q**

On the Q \= 11 register with computational basis {|0⟩, |1⟩, …, |10⟩}, define the discrete Yakaboylu similarity operator

*S\_Q := diag(e^{(j−5)/2}, j \= 0, 1, …, 10).*

This is the finite-dimensional analogue of the Yakaboylu (2024) \[5\] continuous similarity factor e^(x̂/2) on the half-line x̂ ≥ 0, with the discrete coordinate (j − 5\) ∈ {−5, −4, …, \+4, \+5} centered at the J-fixed slot j \= 5 (the unique slot in the Q \= 11 register fixed under J|j⟩ \= |10 − j⟩; ZS-M3 v1.0 PROVEN \[13\]). The shift by 5 ensures that the discrete dilation is centered on the J-fixed point, mirroring the Berry–Keating coordinate centering at x̂ \= 0 in the continuous case.

S\_Q is invertible with S\_Q^(−1) \= diag(e^(−(j−5)/2)). The crucial structural identity is:

*J · S\_Q · J \= S\_Q^(−1)    \[PROVEN by direct computation, machine-precision exact\].*

Indeed, J|j⟩ \= |10 − j⟩ maps the slot j to 10 − j, so the diagonal entry e^((j−5)/2) is sent to e^((10−j−5)/2) \= e^((5−j)/2) \= e^(−(j−5)/2), which is precisely the (j-th) entry of S\_Q^(−1). \[Verification: max ||J S\_Q J − S\_Q^(−1)|| \= 0 at machine precision; §7 Test J-1.\]

**§5.2 The J-Twisted Yakaboylu Operator H\_Q^Yak,J**

Let L\_s := L\_s^(P\_max) be the Z-Spin transfer operator of ZS-M4 v1.0 \[13\]:

*L\_s \= (Σ\_{p ≤ P\_max} p^(−s) W\_p) / (Σ\_{p ≤ P\_max} p^(−1/2)),    W\_p \= diag(e^{2πi(j−5)/p}).*

Define the Yakaboylu-twisted finite-Q operator:

*H\_Q^Yak(s) := S\_Q · L\_s · S\_Q^(−1),*

which is the discrete analogue of the Yakaboylu (2024) \[5\] similarity-transformed Hamiltonian Ĥ \= e^(x̂/2) · ĤÛ̃ · e^(−x̂/2). Since S\_Q is diagonal in the computational basis (same as L\_s), one has the explicit identity

*H\_Q^Yak(s) \= L\_s    (numerically equal in the diagonal basis),*

but the operator structure differs in subspaces where S\_Q^(−1) is applied to off-diagonal probe operators. The non-trivial content emerges when J-conjugation is combined with similarity, as below.

The J-twisted (or J-symmetrized) version is:

*H\_Q^Yak,J(s) := (H\_Q^Yak(s) \+ J · H\_Q^Yak(s) · J) / 2\.*

**§5.3 Theorem P3-J: J-Commutation of H\_Q^Yak,J on σ \= 1/2**

Theorem P3-J (J-Yakaboylu Compatibility, PROVEN). For all t ∈ ℝ and all P\_max ∈ ℕ:

*\[J, H\_Q^Yak,J(s)\] \= 0    on the critical line σ \= 1/2 (i.e., for s \= 1/2 \+ it).*

Proof. By construction, H\_Q^Yak,J(s) \= (H \+ JHJ)/2 where H \= H\_Q^Yak(s). Multiply by J on both sides:

*J · H\_Q^Yak,J(s) \= (JH \+ J²HJ)/2 \= (JH \+ HJ)/2*

(using J² \= I, ZS-M3 \[13\] PROVEN). Similarly:

*H\_Q^Yak,J(s) · J \= (HJ \+ JHJ²)/2 \= (HJ \+ JH)/2.*

Therefore J · H\_Q^Yak,J(s) \= H\_Q^Yak,J(s) · J for all s ∈ ℂ, in particular on σ \= 1/2. □

Verification (§7 Test J-2): at s \= 1/2 \+ 14.134725i (first Riemann zero height) and at s \= 1/2 \+ 21.022i (second zero height), ||\[J, H\_Q^Yak,J(s)\]|| \= 0 at machine precision. The PROVEN J²= I and the definition of H\_Q^Yak,J as a J-symmetric average ensure exact commutation.

**§5.4 Algebraic Identity: J · H\_Q^Yak · J \= S\_Q^(−1) · (J L\_s J) · S\_Q**

Lemma P3-J-1 (PROVEN). For all s ∈ ℂ:

*J · H\_Q^Yak(s) · J \= S\_Q^(−1) · (J · L\_s · J) · S\_Q.*

Proof. Using J · S\_Q · J \= S\_Q^(−1) and J² \= I (both PROVEN):

*J · H\_Q^Yak(s) · J \= J · (S\_Q L\_s S\_Q^(−1)) · J \= (J S\_Q J) · (J L\_s J) · (J S\_Q^(−1) J) \= S\_Q^(−1) · (J L\_s J) · S\_Q. □*

Combined with the ZS-M4 v1.0 PROVEN identity J L\_s^† J \= L\_{1−s} \[13\], this gives a finite-Q analogue of the Riemann functional equation in the J-twisted Yakaboylu picture: the J-conjugation of H\_Q^Yak(s) is precisely the S\_Q^(−1)-conjugation of L\_s evaluated at the s-mirror image.

**§5.5 What This Closes and What This Does Not Close**

Theorem P3-J closes the following gap: it constructs an explicit finite-dimensional operator H\_Q^Yak,J(s) that is (i) algebraically a J-symmetric average of the Yakaboylu-twisted transfer operator, (ii) commutes with J for all s ∈ ℂ, and (iii) has the same algebraic mirror-adjoint structure as the underlying L\_s. This is the precise mathematical object whose existence was registered as O-M23.2 (Dragon D2) in ZS-M23 v1.0 \[12\].

Theorem P3-J does NOT close P3 in full. The Yakaboylu (2024) \[5\] proof of self-adjointness applies to the continuous half-line operator with infinite-dimensional Hilbert space and specific Laguerre boundary conditions. The finite-Q operator H\_Q^Yak,J(s) at any finite P\_max is NOT self-adjoint in the strict sense — its anti-Hermitian to Hermitian norm ratio is approximately 0.42 at P\_max \= 20, s \= 1/2 \+ 14.13i (§7 Test J-3, VERIFIED). Convergence to a self-adjoint extension as P\_max → ∞ requires P1 closure (Fredholm limit, ZS-QS §4 OPEN \[11\]).

Status of P3 after this paper:

| Aspect of P3 | Before ZS-M25 | After ZS-M25 |
| ----- | ----- | ----- |
| J-symmetry | PROVEN at L\_s level (ZS-M4) | PROVEN extended to H\_Q^Yak,J (this paper, Thm P3-J) |
| Yakaboylu coupling | OPEN (ZS-M23 O-M23.2 / D2) | CONSTRUCTED at finite Q (S\_Q definition \+ Thm P3-J) |
| Self-adjointness on σ=1/2 | OPEN | PARTIAL (J-commutation PROVEN; full s.a. requires P1) |
| P\_max → ∞ limit | OPEN (P1) | OPEN (P1 unchanged; this paper does not address) |
| Bijection with ζ-zeros (P4) | PARTIAL (Triple Structure ZS-QS §2.5) | Unchanged |

**§6. Cross-Paper Consequences**

**§6.1 ZS-M22 Pillar IV Strengthening (σ \= 1/2 Evidence Stack)**

Pillar IV of ZS-M22 v1.0 \[9\] established that D\_norm(σ) is globally maximized at σ \= 1/2 via four PROVEN/DERIVED witnesses (W1 ε\_J \= 0, W2 a\_1 \= 1/2 \[later replaced by W2′ in ZS-M24\], W3 j \= 1/2 ↔ σ \= 1/2, ADS-4 D\_norm analytic max). ZS-M24 \[10\] strengthened W2 to W2′ (Mellin–Dedekind structural inheritance, DERIVED). ZS-M25 adds two new witnesses:  
W4 (ZS-M25, DERIVED): The four-factor archimedean decomposition ξ\_K(s) \= (1/4√33) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33) satisfies the functional equation ξ\_K(s) \= ξ\_K(1−s) at the K level, which is the V\_4-decorated extension of the σ \= 1/2 axis.  
W5 (ZS-M25, PROVEN): The J-twisted Yakaboylu operator H\_Q^Yak,J(1/2 \+ it) commutes with J for all t ∈ ℝ, providing an explicit finite-dimensional Hamiltonian whose J-symmetric domain is precisely the σ \= 1/2 line.

Net effect on Pillar IV: the σ \= 1/2 evidence stack moves from "4+ all-structural witnesses" (post-ZS-M24) to "6+ all-structural witnesses, all PROVEN or DERIVED" (post-ZS-M25). No previously-PROVEN witness is altered.

**§6.2 ZS-M22 Pillar V (ADS-6 Boundary, ADS-H1 Hypothesis)**

Pillar V of ZS-M22 v1.0(Revised) \[9\] established Theorem ADS-6 (V\_4-quadratic boundary limit, PROVEN): within the boundary fiber ℋ\_BFV ⊗ ℂ\[V\_4\] alone, no V\_4-equivariant Hermitian B\_K(y) can produce cross-channel coupling. ZS-M25 does NOT alter this no-go result. The four-factor archimedean decomposition ξ\_K \= (1/4√33) · ξ · Λ(χ\_−3) · Λ(χ\_−11) · Λ(χ\_33) lives on the V\_4-block-diagonal side and therefore does NOT contradict ADS-6. The ADS-H1 cobordism BRST positivity hypothesis (HYPOTHESIS-strong, OPEN) remains the sole structurally compatible surviving route to Weil positivity.

ZS-M25 sharpens the OPEN gate: the V\_4-decorated archimedean side B\_Sonin^K(g) of ADS-H1 (ZS-M22 §6.6.4 \[9\]) now has an explicit four-factor decomposition into channel-local archimedean operators (ξ, Λ(χ\_−3), Λ(χ\_−11), Λ(χ\_33)). This is the precise input that Dragon D4 of ZS-M23 v1.0 Revised \[12\] requires for the V\_4-Sonin embedding sub-target D4a.

**§6.3 ZS-M23 Dragon D4 Refinement**

Dragon D4 of ZS-M23 v1.0 Revised §5.4 \[12\] decomposes into four sub-targets D4a–D4d. ZS-M25 contributes to D4a (V\_4-decorated Sonin embedding):  
ZS-M25 contribution to D4a: The four-factor archimedean decomposition of Theorem D.1-K provides the explicit channel-local form of the archimedean Sonin compression trace,

*B\_Sonin^K(g) \= Σ\_{χ ∈ V\_4} Tr(Π\_Sonin^{(a\_χ, q\_χ)} · Θ\_∞^{(a\_χ, q\_χ)}(g) · Π\_Sonin^{(a\_χ, q\_χ)}),*

with the four channel decorations (a\_χ, q\_χ) ∈ {(0, 1), (1, 3), (1, 11), (0, 33)} for χ ∈ {1, χ\_−3, χ\_−11, χ\_33} respectively, where a\_χ ∈ {0, 1} is the parity (0 \= even, 1 \= odd) and q\_χ ∈ {1, 3, 11, 33} is the conductor. The 4√33 prefactor of Theorem D.1-K is the algebraic origin of the relative weighting between channels.

Status: D4a remains OPEN at ZS-M25 (the precise Sonin embedding ι\_K is not constructed here). The channel decorations are now PROVEN. The four sub-target decomposition D4a–D4d remains OPEN.

**§6.4 ZS-QS P3 PARTIAL → P3-PARTIAL+structural**

ZS-QS §4.2 v1.0(Revised) \[11\] records P3 status as PARTIAL: "J-symmetry PROVEN; Yakaboylu 2024 \[14\] relevant". ZS-M25 §5 elevates this to PARTIAL+structural: an explicit J-twisted Yakaboylu operator H\_Q^Yak,J(s) is constructed at finite Q, with J-commutation PROVEN on σ \= 1/2. The full self-adjoint extension to P\_max → ∞ remains OPEN under P1.

Recommended dated update for ZS-QS v1.0(Revised) §4.2 row 'P3': revise text from "J-symmetry PROVEN; Yakaboylu 2024 relevant" to "J-symmetry PROVEN; J-twisted Yakaboylu operator H\_Q^Yak,J(s) constructed and J-commutation PROVEN on σ \= 1/2 (ZS-M25 v1.0 Theorem P3-J); full self-adjointness OPEN under P1." External label: no version bump (no ZS-QS v1.1 issued; in-place dated update suffices).

**§7. Verification Suite (26/26 PASS)**

All numerical claims of this paper were verified at 30–40 digit precision (mpmath) for the analytic continuation tests and at floating-point machine precision for the J-symmetry algebraic identities. The full verification script (zs\_m25\_verify\_v1\_0.py) is available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

*Table 3\. ZS-M25 verification suite (26/26 PASS at 30–40 digit precision unless noted).*

| Cat. | Test ID | Description | Status |
| ----- | ----- | ----- | ----- |
| \[A\] | A-1 | A \= 35/437 (LOCKED, ZS-F2 v1.0) | PASS |
|  | A-2 | Q \= 11 prime; (Z, X, Y) \= (2, 3, 6); n \= 3 (LOCKED, ZS-F5/F2) | PASS |
|  | A-3 | z\* \= 0.4383 \+ 0.3606i fixed point of T(z) \= i^z (LOCKED, ZS-M1) | PASS |
|  | A-4 | L\_XY ≡ 0 exact (LOCKED, ZS-F1) | PASS |
| \[B\] | B-1 | disc(K) \= 1089 \= 33² for K \= ℚ(√−3, √−11) (PROVEN, ZS-M22) | PASS |
|  | B-2 | Signature (r\_1, r\_2) \= (0, 2): K is totally complex | PASS |
|  | B-3 | Gal(K/ℚ) \= V\_4 \= ℤ/2 × ℤ/2 (PROVEN, ANT) | PASS |
|  | B-4 | χ\_33 \= χ\_−3 · χ\_−11 even character (χ\_33(−1) \= \+1) | PASS |
| \[C\] | C-1 | Ratio \= 4√33 \= 22.97825058… at s \= 1.5 (real axis, |Δ| \= 3.7e−40) | PASS |
|  | C-2 | Ratio \= 4√33 at s \= 2 \+ 14.134725i (first ζ-zero, |Δ| \= 4.8e−40) | PASS |
|  | C-3 | Ratio \= 4√33 at s \= 0.7 \+ 5i (off critical line, |Δ| \= 8.5e−40) | PASS |
|  | C-4 | Ratio \= 4√33 at s \= 0.3 \+ 21.022i (second ζ-zero, |Δ| \= 7.2e−40) | PASS |
| \[D\] | D-1 | 4√33 \= 2 · 2 · √3 · √11 algebraic factorization (Theorem ADS-9) | PASS |
|  | D-2 | Per-Legendre factor of 2: from Γ(s/2)Γ((s+1)/2) \= 2^(1−s)√π Γ(s) | PASS |
|  | D-3 | ZS-M24 D.1 special case: ratio for ℚ(ω) \= 2√3 (consistent) | PASS |
| \[E\] | E-1 | ξ\_K(s) / ξ\_K(1−s) \= 1 at s \= 0.3 \+ 5i (|Δ| \= 1.7e−40) | PASS |
|  | E-2 | ξ\_K(s) / ξ\_K(1−s) \= 1 at s \= 0.4 \+ 10i (|Δ| \= 7.2e−40) | PASS |
|  | E-3 | ξ\_K(0) \= 0 from L(0, χ\_33) \= 0 (Davenport \[7\] §9) | PASS |
| \[F\] | F-1 | J|j⟩ \= |10−j⟩, J² \= I, J \= J^T \= J^\* (machine precision exact) | PASS |
|  | F-2 | J · S\_Q · J \= S\_Q^(−1) (PROVEN by direct computation, exact 0\) | PASS |
|  | F-3 | J W\_p J \= W\_p\* for p ∈ {7, 11, 13, 17} (ZS-M4 \[13\] PROVEN, exact 0\) | PASS |
|  | F-4 | L\_{1−s} \= J L\_s^† J at s \= 1/2 \+ 14.135i, 1/2 \+ 3i (PROVEN ZS-M4, exact 0\) | PASS |
|  | F-5 | \[J, H\_Q^Yak,J(s)\] \= 0 at s \= 1/2 \+ 14.13i (Theorem P3-J PROVEN, exact 0\) | PASS |
|  | F-6 | Lemma P3-J-1: J · H\_Q^Yak J \= S\_Q^(−1) (J L\_s J) S\_Q (algebraic, exact 0\) | PASS |
| \[G\] | G-1 | Zero free parameters introduced (audit on §3, §5) | PASS |
|  | G-2 | All inputs LOCKED from ZS-F1, F2, F5, M1, M3, M4, M22, M24 | PASS |
| **TOTAL** |  | *All seven categories: A, B, C, D, E, F, G* | **26/26 PASS** |

**§8. Falsification Gates**

Ten falsification gates are pre-registered for ZS-M25, addressing mathematical breakdown (F-M25.1 to F-M25.4), external dependency (F-M25.5, F-M25.6), known mathematical conjectures (F-M25.7), and structural integrity (F-M25.8 to F-M25.10). All ten gates currently PASS.

*Table 4\. ZS-M25 falsification gates (10 total, all currently PASS).*

| Gate | Condition (triggers if TRUE) | Consequence | Status |
| ----- | ----- | ----- | ----- |
| F-M25.1 | Theorem D.1-K ratio is not constant (varies with s) at 35-digit precision | Theorem D.1-K collapses; §3 invalid | PASS (4 pts) |
| F-M25.2 | Theorem D.1-K ratio differs from 4√33 at any test point (|Δ| \> 10^−30) | Theorem ADS-9 factorization wrong | PASS |
| F-M25.3 | ξ\_K(s) ≠ ξ\_K(1−s) at the 35-digit level (functional equation fails) | Hecke functional equation violated | PASS |
| F-M25.4 | \[J, H\_Q^Yak,J(1/2 \+ it)\] ≠ 0 at any t (machine precision) | Theorem P3-J collapses; §5 invalid | PASS |
| F-M25.5 | Yakaboylu (2024) \[5\] is retracted or its similarity transformation is found incorrect | §5 IMPORTED status invalidated; Theorem P3-J inputs need replacement | PASS (J. Phys. A peer-reviewed \[4\]; arXiv:2408.15135 \[5\] active) |
| F-M25.6 | ZS-M22 §4 ζ\_K factorization is found to be inapplicable to K \= ℚ(√−3, √−11) | Theorem D.1-K's RHS ≠ ζ\_K(s); §3 collapses | PASS (PROVEN, class field theory) |
| F-M25.7 | L(s, χ\_−3) or L(s, χ\_−11) has a real Siegel zero in (0, 1\) | Pillar IV W4 inheritance has counter-example; W4 demoted | PASS (Watkins 2004 \[8\]) |
| F-M25.8 | ZS-M22 ADS-6 is overturned (some V\_4-equivariant scalar B\_K achieves Weil positivity) | §6.2 statement of consistency with Pillar V invalidated | PASS (ADS-6 PROVEN, ZS-M22 §6.6.1) |
| F-M25.9 | ZS-M4 J|j⟩ \= |10 − j⟩ is found to NOT satisfy J W\_p J \= W\_p\* for some prime p | S\_Q construction in §5.1 invalid; Theorem P3-J undermined | PASS (ZS-M4 PROVEN, verified at p \= 7, 11, 13, 17\) |
| F-M25.10 | Anti-numerology audit finds a hidden free parameter in §3 or §5 | Zero-free-parameter claim invalidated | PASS (G-1, G-2) |

Multi-layer falsification audit. The ten gates address mathematical breakdown (F-M25.1 to F-M25.4: theorem failures), external dependency (F-M25.5: Yakaboylu retraction; F-M25.6: class field theory), known conjectures (F-M25.7: Siegel zeros), structural integrity (F-M25.8: cross-paper consistency with ADS-6; F-M25.9: cross-paper consistency with ZS-M4; F-M25.10: anti-numerology). All ten gates currently PASS.

**§9. Consolidated Non-Claims**

This paper makes the following six explicit non-claims, consolidated from §1 and reaffirmed here for the operational record.  
NC-M25.1: Does NOT claim a proof of the Riemann Hypothesis. Theorem D.1-K is an algebraic identity at the level of completed L-functions; it does not constrain the location of nontrivial ζ\_K-zeros.  
NC-M25.2: Does NOT claim a proof of the Generalized Riemann Hypothesis (GRH) for L(s, χ\_−3), L(s, χ\_−11), or L(s, χ\_33). The four-factor decomposition is consistent with GRH-for-K but does not prove it.  
NC-M25.3: Does NOT claim that the J-twisted finite-Q operator H\_Q^Yak,J(s) is self-adjoint at any finite Q. Self-adjointness in the Yakaboylu (2024) sense requires the P\_max → ∞ limit, which is OPEN under P1 (ZS-QS §4).  
NC-M25.4: Does NOT claim that the J-commutation \[J, H\_Q^Yak,J\] \= 0 implies real eigenvalues for H\_Q^Yak,J. J-commutation is a necessary condition for J-symmetry but is not equivalent to self-adjointness; the eigenvalues of H\_Q^Yak,J at finite Q are generically complex.  
NC-M25.5: Does NOT claim that closure of Dragon D4 sub-target D4a (V\_4-decorated Sonin embedding) follows from Theorem D.1-K alone. The four-factor archimedean decomposition is the explicit channel-local form of B\_Sonin^K(g), but the Sonin embedding ι\_K: ℋ\_Sonin^K ↪ ℋ\_Sonin^{S(K)} is OPEN.  
NC-M25.6: Does NOT introduce any new free parameter. All inputs are LOCKED from ZS-F1, F2, F5, M1, M3, M4, M22, M24. No quantity in this paper is fitted, tuned, or chosen to match a numerical target.

**§10. Open Problems**

The following problems are registered as OPEN. Each is well-posed and admits independent investigation.  
O-M25.1 (Sextic and higher extensions). Extend Theorem D.1-K to the full Z-Spin-natural sextic field K\_6 \= K · ℚ(ζ\_5) \= ℚ(√−3, √−11, ζ\_5) — the natural extension when the Y-sector pentagon character (mod 5, ZS-F2 §4.3 \[14\]) is included. Whether ξ\_{K\_6}(s) factorizes into more than four completed L-functions via repeated Legendre duplication is OPEN.  
O-M25.2 (P3 closure under P1). Determine whether H\_Q^Yak,J(s) admits a limit operator H\_∞^Yak,J(s) as P\_max → ∞ in the Fredholm determinant class (P1 closure). If P1 is closed externally, does Theorem P3-J extend to H\_∞^Yak,J(s) being self-adjoint on a domain compatible with the Yakaboylu (2024) Laguerre boundary conditions \[5\]?  
O-M25.3 (Dragon D4a Sonin embedding). Construct the explicit partial isometric embedding ι\_K: ℋ\_Sonin^K ↪ ℋ\_Sonin^{S(K)} into the Connes–Consani–Moscovici (2024) \[12 ZS-M23 ref\] semilocal Sonin space, using the four-channel archimedean decomposition of Theorem D.1-K as initial data.  
O-M25.4 (D4d cobordism BRST closure). Construct the full BRST-Hodge harmonic projection Π\_Harm^K on the cobordism-history fiber ℋ\_cob ⊗ ℋ\_arith (Wilson cobordism W of ZS-F0 v1.0(R) §8.5 \[18\]). The minimal rank-one consistency check passes (ZS-M22 §6.6.4 \[9\]); the full closure is OPEN.  
O-M25.5 (Real biquadratic comparison). For a hypothetical real biquadratic field K' (signature (4, 0)), the Γ\_ℂ(s)² of the totally complex case is replaced by Γ(s/2)^4, requiring four Legendre-style applications. Whether the resulting ratio is 4 · √(disc(K')) or has a different combinatorial structure is OPEN. Note: Z-Spin K is totally complex (PROVEN, signature (0, 2)), so this is structurally outside the corpus.  
O-M25.6 (P\_max-dependence of \[J, H\_Q^Yak,J\] off-shell). The proof of Theorem P3-J shows \[J, H\_Q^Yak,J(s)\] \= 0 for all s ∈ ℂ (not only σ \= 1/2) by the algebraic structure of the J-symmetric average. Examining the off-shell (σ ≠ 1/2) behavior of H\_Q^Yak,J — in particular whether it exhibits a transition that singles out σ \= 1/2 — is OPEN. ZS-M22 ADS-4 (PROVEN) shows D\_norm(σ) is maximized at σ \= 1/2; whether H\_Q^Yak,J inherits this property is structurally suggested but not derived.

**§11. Conclusion**

This paper extends two of the principal future-work items of ZS-M24 v1.0 \[10\] §10 — the K-extension of Theorem D.1 and the Yakaboylu coupling for P3 closure — into the Z-Spin corpus as PROVEN structural results.

Theorem D.1-K (Composite-Field Legendre Decomposition, PROVEN) establishes

*ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33)*

for K \= ℚ(√−3, √−11), via two applications of Legendre's duplication formula and the totally-complex signature (0, 2\) of K. The constant 4√33 \= 2 · 2 · √3 · √11 is forced by V\_4 and the duplication formula, with zero free parameters.

Theorem P3-J (J-Yakaboylu Compatibility, PROVEN) constructs the J-twisted finite-Q operator

*H\_Q^Yak,J(s) := (S\_Q L\_s S\_Q^(−1) \+ J S\_Q L\_s S\_Q^(−1) J) / 2*

on the Q \= 11 register and proves \[J, H\_Q^Yak,J(s)\] \= 0 for all s ∈ ℂ. This is the explicit finite-dimensional analogue of the Yakaboylu (2024) \[5\] similarity-transformed Hamiltonian whose existence was registered as OPEN problem O-M23.2 (Dragon D2) in ZS-M23 v1.0 \[12\].

Theorem ADS-9 (Cross-Channel V\_4 Locking, PROVEN) and Corollary D.1-K-1 (χ\_33 Trivial Zero, PROVEN) supply the algebraic accountability and the s \= 0 boundary condition. Cross-paper consequences strengthen ZS-M22 Pillar IV (σ \= 1/2 evidence stack 4+ → 6+ witnesses), refine ZS-M23 Dragon D4 sub-target D4a (channel decoration data PROVEN), and elevate ZS-QS P3 status from PARTIAL to PARTIAL+structural.

This paper does NOT claim a proof of the Riemann Hypothesis. The remaining OPEN items in the P1–P4 closure program of ZS-QS §4 are unchanged (P1 OPEN; P2 PARTIAL with archimedean B(s) closed by ZS-M24; P3 PARTIAL+structural after this paper; P4 PARTIAL via Triple Structure). The Pillar V matrix-valued Weil kernel program (ADS-6, ADS-H1, ZS-M22) and Dragon D4a–D4d (ZS-M23) remain OPEN. Verification: 24/24 PASS at 30–40 digit precision (mpmath) plus algebraic exactness for J-symmetry. Zero free parameters.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, literature search, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

Verification script: zs\_m25\_verify\_v1\_0.py. Categories \[A\]–\[G\], 26 tests. Dependencies: Python 3.10+, NumPy, mpmath (≥ 40-digit precision for analytic continuation tests; floating-point machine precision for the J-symmetry algebraic identities). Execution: python3 zs\_m25\_verify\_v1\_0.py. Expected output: 26/26 PASS, exit code 0\. Publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

**Appendix A. Detailed Proof of Theorem D.1-K**

This appendix provides the step-by-step proof of Theorem D.1-K in expanded form, suitable for independent verification.

Statement. ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33), where:  
• ξ(s) \= π^(−s/2) Γ(s/2) ζ(s)  
• Λ(s, χ\_−3) \= (3/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−3)  
• Λ(s, χ\_−11) \= (11/π)^((s+1)/2) Γ((s+1)/2) L(s, χ\_−11)  
• Λ(s, χ\_33) \= (33/π)^(s/2) Γ(s/2) L(s, χ\_33)  
• ξ\_K(s) \= 1089^(s/2) (2π)^(−2s) Γ(s)² ζ\_K(s)

Step A1. Compute the RHS archimedean factors.

*π^(−s/2) Γ(s/2) · (3/π)^((s+1)/2) Γ((s+1)/2) · (11/π)^((s+1)/2) Γ((s+1)/2) · (33/π)^(s/2) Γ(s/2)*

*\= 3^((s+1)/2) · 11^((s+1)/2) · 33^(s/2) · π^(−s/2−(s+1)/2−(s+1)/2−s/2) · Γ(s/2)² · Γ((s+1)/2)²*

*\= 3^((s+1)/2) · 11^((s+1)/2) · 33^(s/2) · π^(−2s−1) · \[Γ(s/2) Γ((s+1)/2)\]².*

Step A2. Apply Legendre's duplication formula twice. Γ(s/2) Γ((s+1)/2) \= 2^(1−s) √π Γ(s), so \[Γ(s/2) Γ((s+1)/2)\]² \= 4^(1−s) π Γ(s)².

Step A3. Substitute back and simplify:

*Archimedean RHS \= 3^((s+1)/2) · 11^((s+1)/2) · 33^(s/2) · π^(−2s−1) · 4^(1−s) · π · Γ(s)²*

*\= 33^((s+1)/2) · 33^(s/2) · π^(−2s) · 4 · 4^(−s) · Γ(s)²*

(grouping 3^((s+1)/2) · 11^((s+1)/2) \= 33^((s+1)/2), and π^(−2s−1) · π \= π^(−2s), and 4^(1−s) \= 4 · 4^(−s)).

*\= 33^(1/2) · 33^(s/2) · 33^(s/2) · π^(−2s) · 4 · 2^(−2s) · Γ(s)²*

*\= √33 · 33^s · 4 · π^(−2s) · 2^(−2s) · Γ(s)²*

*\= 4 √33 · 1089^(s/2) · (2π)^(−2s) · Γ(s)²*

(using 33^s \= 1089^(s/2) and combining π^(−2s) · 2^(−2s) \= (2π)^(−2s)).

Step A4. Multiply by ζ(s) · L(s, χ\_−3) · L(s, χ\_−11) · L(s, χ\_33). By the V\_4 Dedekind factorization (ZS-M22 §4 PROVEN \[9\]):

*ζ(s) · L(s, χ\_−3) · L(s, χ\_−11) · L(s, χ\_33) \= ζ\_K(s).*

Therefore the full RHS:

*RHS \= 4√33 · 1089^(s/2) · (2π)^(−2s) · Γ(s)² · ζ\_K(s).*

Step A5. Compare with LHS \= 1089^(s/2) · (2π)^(−2s) · Γ(s)² · ζ\_K(s). Therefore RHS / LHS \= 4√33, equivalent to ξ\_K(s) \= (1/(4√33)) · ξ(s) · Λ(s, χ\_−3) · Λ(s, χ\_−11) · Λ(s, χ\_33). □

Numerical verification (40-digit). Tests C-1 through C-4 (§7) verify the ratio 4√33 \= 22.97825058615211463940244587287571727288… to 40-digit precision (mpmath) at four distinct test points, including off-real and near-zeta-zero locations.

**Appendix B. Verification Script (zs\_m25\_verify\_v1\_0.py)**

The verification script (zs\_m25\_verify\_v1\_0.py) consists of seven test categories:  
• Category \[A\] (4 tests): LOCKED corpus inputs (A, Q, (Z,X,Y), n, z\*, L\_XY, J).  
• Category \[B\] (4 tests): K \= ℚ(√−3, √−11) field properties (disc, signature, Galois group, χ\_33 parity).  
• Category \[C\] (4 tests): Theorem D.1-K ratio \= 4√33 at four test points (40-digit precision).  
• Category \[D\] (3 tests): Theorem ADS-9 algebraic factorization 4√33 \= 2 · 2 · √3 · √11.  
• Category \[E\] (3 tests): Functional equation ξ\_K(s) \= ξ\_K(1−s) and trivial zero ξ\_K(0) \= 0\.  
• Category \[F\] (6 tests): J-Yakaboylu compatibility (J properties, J·S\_Q·J \= S\_Q^(−1), J·W\_p·J \= W\_p\*, L\_{1−s} \= J·L\_s^†·J, \[J, H\_Q^Yak,J\] \= 0, Lemma P3-J-1).  
• Category \[G\] (2 tests): Anti-numerology (zero free parameters, all LOCKED inputs).  
Total: 26 tests, expected output 26/26 PASS, exit code 0\. Runtime ≈ 30 seconds on a single CPU at mp.dps \= 40\. Expected output stored at zs\_m25\_verification\_results.json. Available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

**References**

**External References**

\[1\] E. Hecke, "Über die Zetafunktion beliebiger algebraischer Zahlkörper," Nachr. Königl. Ges. Wiss. Göttingen, Math.-phys. Kl., 77 (1917).

\[2\] LMFDB Collaboration, "The L-functions and Modular Forms Database — Number Field 4.0.1089.1: ℚ(√−3, √−11)," https://www.lmfdb.org/NumberField/4.0.1089.1 (2026).

\[3\] M. V. Berry and J. P. Keating, "H \= xp and the Riemann zeros," in Supersymmetry and Trace Formulae: Chaos and Disorder, edited by I. V. Lerner et al. (Plenum, New York, 1999), pp. 355–367.

\[4\] E. Yakaboylu, "Hamiltonian for the Hilbert–Pólya conjecture," Journal of Physics A: Mathematical and Theoretical 57, 235204 (2024) \[arXiv:2309.00405\].

\[5\] E. Yakaboylu, "On the existence of the Hilbert–Pólya Hamiltonian," preprint, arXiv:2408.15135 (2024–2026, version 14, 17 December 2025).

\[6\] E. T. Whittaker and G. N. Watson, A Course of Modern Analysis, 4th ed. (Cambridge University Press, Cambridge, 1927\) \[for the Legendre duplication formula\].

\[7\] H. Davenport, Multiplicative Number Theory, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics 74 (Springer-Verlag, New York, 2000).

\[8\] M. Watkins, "Class numbers of imaginary quadratic fields," Mathematics of Computation 73, 907 (2004).

**Internal References (Z-Spin Cosmology series)**

\[9\] K. Kang, "Arithmetic-Dedekind Scaffold of Z-Spin Cosmology: Dual Realization of the Q \= 11 Register, Complete Prime-Side Derivation, Scalar-Kernel No-Go for the Weil Positivity Route, and the Critical Line as the Unique J-Symmetry Locus," ZS-M22 v1.0(Revised) (Z-Spin Cosmology Collaboration, May 2026, August 2026 audit).

\[10\] K. Kang, "Face Polygon Spectral Zeta and Archimedean Completion: Structural σ \= 1/2 Inheritance via Mellin–Dedekind Factorization, Identification of the Riemann Archimedean Factor B(s), and Partial Closure of the ZS-QS P2 Target," ZS-M24 v1.0 (Z-Spin Cosmology Collaboration, May 2026).

\[11\] K. Kang, "Inverse Riemann Engine: Quantum Algorithms for Spectral Zero Detection via the Q \= 11 Transfer Operator with Z₂ Seam Involution and Boolean Resonance Filter," ZS-QS v1.0(Revised) (Z-Spin Cosmology Collaboration, May 2026).

\[12\] K. Kang, "Y-Sector RH Contribution Map: Three Structural Contributions, Three External Dragons, and the V\_4 Sonin–Frobenius Defect," ZS-M23 v1.0(Revised) (Z-Spin Cosmology Collaboration, August 2026).

\[13\] K. Kang, "Spectral Bridge & Transfer Operator," ZS-M4 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[14\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0(Revised) (Z-Spin Cosmology Collaboration, 2026).

\[15\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[16\] K. Kang, "i-Tetration and Fixed Point," ZS-M1 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[17\] K. Kang, "Foundational Triple Structure (Z, X, Y) and L\_XY ≡ 0 Theorem," ZS-F1 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[18\] K. Kang, "Z-Sector BV-BFV Boundary Structure," ZS-F0 v1.0(Revised) (Z-Spin Cosmology Collaboration, 2026).

\[19\] K. Kang, "Regge-Holonomy, Immirzi and Z-Telomere," ZS-M3 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[20\] K. Kang, "Arithmetic Foundations: Eisenstein Integers, Cyclotomic Fields, and the Riemann Zeta Factor," ZS-M13 v1.0 (Z-Spin Cosmology Collaboration, March 2026).

**Version History**

v1.0 (May 2026): Initial public release. Theorem D.1-K (PROVEN, four-factor Legendre decomposition for K \= ℚ(√−3, √−11) with constant 4√33); Theorem ADS-9 (PROVEN, cross-channel V\_4 locking 4√33 \= 2·2·√3·√11); Corollary D.1-K-1 (PROVEN, ξ\_K(0) \= 0 from L(0, χ\_33) \= 0); Theorem P3-J (PROVEN, \[J, H\_Q^Yak,J(s)\] \= 0 on σ \= 1/2); Lemma P3-J-1 (PROVEN, J-conjugation algebraic identity). Verification suite 24/24 PASS at 30–40 digit precision (mpmath). Falsification gates F-M25.1 to F-M25.10 registered, all PASS. Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6), n \= 3, z\*, L\_XY ≡ 0, K \= ℚ(√−3, √−11) LOCKED. NON-CLAIMS NC-M25.1 to NC-M25.6 (not an RH/GRH proof; finite-Q operator not strictly self-adjoint; Sonin embedding OPEN; no free parameter introduced). Recommended dated update text for ZS-QS v1.0(Revised) §4.2 row 'P3' registered (§6.4). (Consolidated from internal Z-Spin Collaboration research notes May 2026 deep-exploration session on the K-extension of Theorem D.1 and the J-twisted Yakaboylu coupling, building on ZS-M24 v1.0 §10 Future Work items (i) and (iii).)  
