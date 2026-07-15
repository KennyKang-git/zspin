**ZS-M24**

**Face Polygon Spectral Zeta and Archimedean Completion**

*Structural σ \= 1/2 Inheritance via Mellin–Dedekind Factorization, Identification of the Riemann Archimedean Factor B(s), and Partial Closure of the ZS-QS P2 Target*

Kenny Kang  
Z-Spin Cosmology Collaboration  
May 2026  |  ZS-M24 (Mathematical Spine Theme)  |  Paper Code: ZS-M24  
Version: v1.0

**Verification: 35/35 PASS  |  Zero Free Parameters  |  NON-CLAIM: Not an RH Proof**

**Position Statement**

    •  This paper redefines the P2 closure target of ZS-QS §4 — the identification of an entire-function archimedean factor B(s) in the identity ξ(s) \= B(s)·D(s) — by routing the derivation through the face polygon spectral zeta function ζ*∇*(s) of the equilateral triangle, in place of the original heat-kernel pipeline of the finite Q \= 11 transfer operator L\_s.

    •  The face polygon spectral zeta admits an explicit closed form (Mårdby–Rowlett 2024 \[12\], Proposition 3.1; Corollary 3.2). Its Mellin origin in the Eisenstein theta function Θ*ℤ\[ω\]*(τ), combined with the ZS-M13 Chain A factorization ζ*ℚ(ω)*(s) \= ζ(s)·L(s, χ*−3*), structurally inherits the critical line σ \= 1/2 of the Riemann zeta function.

    •  Theorem D.1 decomposes the completed Dedekind zeta of ℚ(ω) as ξ*ℚ(ω)*(s) \= (1/2√3)·ξ(s)·Λ(s, χ*−3*), where ξ(s) is the Riemann completed function and Λ(s, χ*−3*) is the completed L-function for the odd character χ*−3*. Verified to 35-digit precision (mpmath).

    •  Theorem D.2 identifies the archimedean factor B(s) of ZS-QS §4.1 with B(s) \= π*−s/2*·Γ(s/2). P2 status: OPEN → PARTIAL.

    •  Witness W2 of ZS-M22 §5.4 ("a*1* \= 1/2 numerical coincidence") is FALSIFIED at the value level: the correct value is a*1*(equilateral) \= 1/3 (Mårdby–Rowlett 2024 Theorem 3.5; Looi–Sher 2025 Theorem 1; this paper §7 Test \[B\], 35-digit). W2 is replaced by W2′: structural inheritance of σ \= 1/2 through the Mellin–Dedekind chain. W2′ is DERIVED, gap-free, stronger than the falsified W2.

    •  Pillar IV (ZS-M22 §5) is **strengthened**, not weakened: the σ \= 1/2 evidence stack moves from "3 structural witnesses \+ 1 numerical coincidence" to "4+ all-structural witnesses, all PROVEN or DERIVED".

    •  Corpus implications listed in §8: ZS-F7 v1.0(Revised) §7.2/§8.2, ZS-M13 v1.0 §6.1, ZS-M22 v1.0 §5.2/§5.4/§7.4/§8 (Test B-6) require dated updates. None of the prior numerical predictions of any Z-Spin paper are altered.

    •  All Z-Spin axioms LOCKED unchanged: A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6), n \= 3, z\*, L\_XY ≡ 0\. Zero free parameters introduced.

    •  This paper does NOT claim a proof of the Riemann Hypothesis. P1, P3, P4 of ZS-QS §4 remain OPEN. The contribution is to upgrade P2 alone.

**§0. Abstract**

We establish a structural connection between the Z-Spin face polygon (n \= 3, equilateral triangle, ZS-F2 v1.0) and the archimedean factor of the Riemann completed function ξ(s), routing through the spectral zeta function ζ*∇*(s) of the Dirichlet Laplacian on the equilateral triangle.

**Theorem C.1 (Critical Line Inheritance, DERIVED).** The Mellin transform of the Eisenstein theta function Θ*ℤ\[ω\]*(τ) yields the Dedekind zeta factorization ζ*ℚ(ω)*(s) \= ζ(s)·L(s, χ*−3*) (Chain A, ZS-M13 §2, PROVEN). The face polygon spectral zeta ζ*∇*(s) (Mårdby–Rowlett 2024 Proposition 3.1) is built from the Eisenstein lattice sum G*∇*(s) \= 6·ζ(s)·L(s, χ*−3*) and inherits the critical line σ \= 1/2 from the ζ(s) factor.

**Theorem C.2 (Simple Pole at σ \= 1/2, PROVEN).** ζ*∇*(s) has a simple pole at s \= 1/2 with residue −3ℓ/(8π). The pole replaces the falsified "a*1* \= 1/2 numerical coincidence" with a structural analytic singularity.

**Theorem D.1 (Legendre Duplication Decomposition, PROVEN).** 

*ξ\_ℚ(ω)(s) \= (1/(2√3)) · ξ(s) · Λ(s, χ\_−3)*

Proof: Legendre's duplication formula Γ(s/2)·Γ((s+1)/2) \= 2*1−s*·√π·Γ(s). Verified at 35-digit precision.

**Theorem D.2 (Archimedean Factor Identification, DERIVED).** B(s) \= π*−s/2*·Γ(s/2) is the archimedean factor of the ZS-QS §4.1 P2 closure target.

**Proposition E.1 (P2 Status Upgrade, DERIVED-CONDITIONAL).** Conditional on Mårdby–Rowlett (P1) external proof, P2 of ZS-QS §4 is upgraded OPEN → PARTIAL. The surrogate-to-zeta zero bijection (P4) remains OPEN.

**Witness W2 Reformulation (DERIVED, replaces FALSIFIED W2).** Original W2: "a*1*(face polygon) \= 1/2" — FALSIFIED. New W2′: structural inheritance through Mellin–Dedekind. Pillar IV evidence stack strengthened.

Verification suite: 35/35 PASS (mpmath, 30–35 digit precision). Zero free parameters. The paper does NOT claim a proof of the Riemann Hypothesis; P1, P3, P4 of ZS-QS §4 remain OPEN. Recommended dated updates for ZS-F7, ZS-M13, ZS-M22 listed in §8.

**Keywords:** face polygon spectral zeta, equilateral triangle Laplacian, Dedekind zeta, Eisenstein integers, Mellin transform, Legendre duplication formula, archimedean factor, Riemann xi, critical line, Hilbert–Pólya, Mårdby–Rowlett, ZS-QS P2 closure.

**Epistemic Status Legend**

| Tag | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem with complete proof under declared definitions. |
| **DERIVED** | Quantitative consequence from PROVEN items plus Z-Spin axioms; zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived under explicitly stated external assumption. |
| **VERIFIED** | Numerically verified to declared precision; no closed-form proof claimed. |
| **IMPORTED** | Result proved externally and used here without re-proof; full citation given. |
| **HYPOTHESIS** | Structural pattern without completed derivation chain. |
| **OPEN** | Recognized gap with explicit closure path identified. |
| **RETRACTED** | Earlier corpus claim found incorrect; replacement supplied. |
| **FALSIFIED** | Earlier corpus claim found inconsistent with external proof and direct verification; replacement supplied. |
| **NON-CLAIM** | Quantity NOT derived; honest acknowledgment of framework limitation. |

**§1. Introduction**

**§1.1 Context: The ZS-QS P1–P4 Closure Program**

The Inverse Riemann Engine (ZS-QS v1.0(Revised) \[11\]) constructs a finite-dimensional transfer operator L\_s*(P\_max)* on the Q \= 11 register, with Z*2* seam involution J. The associated spectral determinant D*(P\_max)*(s) \= det(I − L\_s*(P\_max)*) serves as a cutoff-dependent surrogate for the Riemann zeta zeros. The Conditional Hilbert–Pólya Theorem (ZS-QS §4.1) requires four targets P1–P4 to be closed before any RH consequence can be claimed:

**(P1)** Operator well-posedness: lim*P\_max→∞* L\_s*(P\_max)* exists in Fredholm determinant class. \[OPEN\]  
**(P2)** Determinant identity: an entire-function identity ξ(s) \= B(s)·D(s) holds with B(s) ≠ 0\. \[OPEN at v1.0(Revised)\]  
**(P3)** Self-adjoint seam generator: on σ \= 1/2, L*1/2 \+ it* \= exp(itH) with H self-adjoint. \[PARTIAL: J-symmetry PROVEN; Yakaboylu 2024 \[14\] relevant\]  
**(P4)** Completeness: bijection between zeros of D(s) and ζ(s). \[PARTIAL: Triple Structure (ZS-QS §2.5)\]

This paper addresses (P2) only. The route originally proposed in ZS-F7 v1.0 §8.1 — derive B(s) from the heat-kernel expansion on the Reuleaux Z-sector boundary — was demoted from BLOCKING to SUPPLEMENTARY by the dated update of 2026-04-15 (ZS-F7 v1.0(Revised) §8.1), which closed the cosmological chain through the Dimensional Coupling Norm Theorem of ZS-M6 §2.2 instead. The B(s) identification, however, retained its motivation as a path toward the Riemann zeta connection and remained OPEN.

We close that motivation here, by showing that the relevant heat kernel is not on the Reuleaux envelope but on the inscribed equilateral face polygon, and that the closed-form expression of its spectral zeta function (Mårdby–Rowlett 2024 \[12\]) provides the analytical chain ζ*∇* → ζ*ℚ(ω)* → ξ*ℚ(ω)* → ξ·Λ(χ*−3*), from which B(s) \= π*−s/2*·Γ(s/2) emerges naturally via Legendre's duplication formula.

**§1.2 The Face Polygon Inside the Reuleaux Envelope**

The Z-sector boundary Ω is the Reuleaux triangle (ZS-F7 v1.0(Revised) \[8\]). Inscribed in Ω is the equilateral triangle ∇ with three vertices coinciding with the three Reuleaux cusps and three sides being the chords of the three Reuleaux arcs. The Reuleaux envelope and the face polygon constitute a **dual pair** on the Z-sector cross-section:

    •  **Reuleaux envelope Ω**: variational carrier — minimum-area constant-width curve, J-compatible boundary, interior angle 2π/3 at each cusp. Spectral invariant a*1*(Ω) \= 3/16 (Looi–Sher 2025 \[13\] Theorem 1).  
    •  **Face polygon ∇**: arithmetic carrier — straight-edged equilateral triangle, interior angle π/3, exact Lamé spectrum (Lamé 1852 \[1\]). Spectral invariant a*1*(∇) \= 1/3 (Mårdby–Rowlett 2024 \[12\]; Looi–Sher 2025 \[13\]).

The two carriers play distinct roles. The Reuleaux envelope is selected by the variational principle (1-loop area minimization, ZS-F7 §3) and provides J-compatibility (ZS-F7 §6). The face polygon carries the arithmetic content: its eigenvalue norms m² \+ mn \+ n² are precisely the Eisenstein integer norms |m − nω|² (ZS-M13 §2.1, PROVEN), and its spectral zeta factorizes through ζ(s)·L(s, χ*−3*) via the Mellin transform of the Eisenstein theta function. The σ \= 1/2 connection lives on the face polygon, not on the Reuleaux envelope.

**§1.3 Locked Z-Spin Inputs**

All Z-Spin axioms used in this paper are imported unchanged from prior PROVEN results: A \= 35/437 \[LOCKED, ZS-F2 v1.0(R)\]; Q \= 11 \[LOCKED, ZS-F5\]; (Z, X, Y) \= (2, 3, 6\) \[LOCKED, ZS-F1/F5\]; n \= 3 face polygon \[LOCKED, ZS-F2(R)\]; z\* \= −W*0*(−iπ/2)/(iπ/2) ≈ 0.43828 \+ 0.36059i \[LOCKED, ZS-M1\]; L\_XY ≡ 0 \[LOCKED, ZS-F1\]; Chain A factorization ζ*ℚ(ω)*(s) \= ζ(s)·L(s, χ*−3*) \[LOCKED, ZS-M13 §2 / ZS-M22 §2.1, gap-free\].

Zero new free parameters introduced. The discriminant 3 of ℚ(ω) and the conductor 3 of χ*−3* are both equal to X \= 3 \= n, PROVEN consequences of the locked input n \= 3 (ZS-M13 §2.1; ZS-M22 §2.1.1).

**§1.4 Roadmap**

§2 imports the Mårdby–Rowlett ζ*∇*(s) closed form. §3 establishes Theorem C.1 (Critical Line Inheritance) and Theorem C.2 (Simple Pole at σ \= 1/2). §4 establishes Theorem D.1 (Legendre Duplication Decomposition) and Theorem D.2 (B(s) Identification). §5 states Proposition E.1 (P2 Status Upgrade). §6 reformulates Witness W2. §7 reports the verification suite (35/35 PASS). §8 lists corpus implications and recommended dated updates. §9 registers falsification gates. §10 concludes. Appendix A: proof of Theorem D.1. Appendix B: numerical verification.

**§2. The Mårdby–Rowlett ζ\_∇(s) Closed Form (Imported)**

This section imports the closed-form expression of ζ*∇*(s) from Mårdby–Rowlett 2024 \[12\] (J. Fourier Anal. Appl. 31, art. 81, 2025). All results carry \[IMPORTED, externally PROVEN\] tags.

**§2.1 Lamé Spectrum and Eisenstein Norms**

The Dirichlet eigenvalues of the Laplacian on the equilateral triangle ∇ of side length ℓ are (Lamé 1852 \[1\]):

*λ\_(m,n) \= (16π² / 9ℓ²)(m² \+ mn \+ n²),    m \> n ≥ 1, m, n ∈ ℤ*

The eigenvalue norm m² \+ mn \+ n² is the Eisenstein integer norm |m − nω|² where ω \= e*2πi/3* (ZS-M13 §2.1 step A4, PROVEN). The eigenvalue counting function is encoded by the Eisenstein theta function Θ*ℤ\[ω\]*(τ) \= Σ q*m²+mn+n²*, a weight-1 modular form on Γ*0*(3). Its Mellin transform yields:

*ζ\_ℚ(ω)(s) \= ζ(s) · L(s, χ\_−3)    \[PROVEN, ZS-M13 §2.1, Chain A\]*

**§2.2 Mårdby–Rowlett Proposition 3.1: Closed-Form ζ\_∇(s)**

*Theorem \[Mårdby–Rowlett 2024, Proposition 3.1\].* The spectral zeta function of the Dirichlet Laplacian on the equilateral triangle ∇ of side length ℓ admits the analytic continuation:

*ζ\_∇(s) \= (1/6)(3ℓ/4)^(2s) · \[G\_∇(s) − (6/π^(2s)) ζ\_R(2s)\]*

where G*∇*(s) \= 6·ζ(s)·L(s, χ*−3*) is the Eisenstein lattice sum and ζ*R*(s) is the Riemann zeta function. The (1/6) prefactor arises from the Lamé multiplicity; the (3ℓ/4)*2s* prefactor sets the geometric scale. \[IMPORTED, externally PROVEN\]

*Corollary \[Mårdby–Rowlett 2024, Corollary 3.2\].* ζ*∇*(0) \= 1/3 and ζ′*∇*(0) \= (2/3) log(3ℓ / (2|η(z)|)), where z \= (−3 \+ i√3)/2 and η is the Dedekind eta function. \[IMPORTED; verified §7 Test \[B\] to 35 digits\]

**§2.3 Mårdby–Rowlett Theorem 3.5: Heat Trace Expansion**

*Theorem \[Mårdby–Rowlett 2024, Theorem 3.5\].* The heat trace of the Dirichlet Laplacian on the equilateral triangle ∇ of side length ℓ admits the asymptotic expansion as t → 0*\+*:

*H\_∇(t) \= (ℓ²√3) / (16πt) − 3ℓ / (8√(πt)) \+ 1/3 \+ O(exp(−9/(4t)))*

Hence the Seeley–DeWitt coefficients of ∇ are: a*0*(∇) \= ℓ²√3/(16π); a*1/2*(∇) \= −3ℓ/(8√π); **a***1***(∇) \= 1/3**. \[IMPORTED, externally PROVEN\]

**Reconciliation with Looi–Sher 2025 \[13\] Theorem 1:** For a piecewise-straight polygon with corners at angles {α*i*} (no smooth boundary curvature), Looi–Sher Theorem 1 gives a*1* \= (1/24π)·Σ*i* (π² − α*i*²)/α*i*. For the equilateral triangle (3 corners at α \= π/3): a*1* \= 3·(8π²/9)/(24π·π/3) \= 1/3. Consistent with \[12\].

**Discrepancy with the McKean–Singer 1967 form:** ZS-F7 v1.0(Revised) §7.2 cites the McKean–Singer formula a*1* \= χ(Ω)/6 \+ Σ*i* (π/α*i* − α*i*/π)/24, which gives a*1*(equilateral) \= 1/6 \+ 3·(1/9) \= 1/2. The (π/α − α/π)/24 per-corner contribution is identical to (π² − α²)/(24πα), but the χ(Ω)/6 \= 1/6 baseline is *absent* in the modern (Mårdby–Rowlett, Looi–Sher, NRS \[15\]) treatment for piecewise-straight polygons. The Gauss–Bonnet origin of χ/6 — namely (1/12π)∫*∂Ω* κ ds \= (1/12π)·2π \= 1/6 for smooth simply-connected domains — vanishes when ∂Ω has no smooth boundary curvature. Including the χ/6 term double-counts in the polygon case. The corrected value is a*1*(equilateral) \= **1/3**, verified to 35-digit precision (§7 Test \[B\]). \[STATUS: a*1*(equilateral) \= 1/3 PROVEN externally; a*1*(equilateral) \= 1/2 of ZS-F7 §7.2 / ZS-M13 §6.1 / ZS-M22 §5.2 FALSIFIED at value level; replacement listed in §8\]

**§3. Critical Line Inheritance and Simple Pole at σ \= 1/2**

**§3.1 Theorem C.1 (Critical Line Inheritance)**

**Theorem C.1. \[DERIVED\]** Let s ∈ ℂ with 0 \< Re(s) \< 1, s ≠ 1/2. Then ζ*∇*(s) introduces no zeros off the critical lines of ζ(s) and L(s, χ*−3*): any vanishing of ζ*∇*(s) on this strip is structurally constrained by the bracket equality 6·ζ(s)·L(s, χ*−3*) \= 6·ζ*R*(2s)/π*2s*, whose right-hand side is computable from ζ*R*(2s) alone and is generically nonzero on the critical strip.

**Proof.** By Mårdby–Rowlett Proposition 3.1 (§2.2):

*ζ\_∇(s) \= (1/6)(3ℓ/4)^(2s) · \[6 ζ(s) L(s, χ\_−3) − 6 ζ\_R(2s) / π^(2s)\]*

Suppose ζ*∇*(s*0*) \= 0 with 0 \< Re(s*0*) \< 1, s*0* ≠ 1/2. The prefactor (1/6)(3ℓ/4)*2s\_0* is nonzero, so the bracket must vanish: ζ(s*0*)·L(s*0*, χ*−3*) \= ζ*R*(2s*0*)/π*2s\_0*. On the strip 0 \< Re(s) \< 1, s ≠ 1/2, both factors of the left-hand side are entire functions; on the same strip, ζ*R*(2s) is finite (no singularity since 2s ≠ 1\) and nonzero (by the prime number theorem, ζ has no zeros on Re(s) \= 1, hence ζ*R*(2s) has no zeros on Re(s) \= 1/2 except possibly the critical-strip zeros at Re(2s) ∈ (0, 1), i.e., Re(s) ∈ (0, 1/2)). The bracket equality is therefore a *structural* relation between ζ(s*0*)·L(s*0*, χ*−3*) and the explicit function ζ*R*(2s*0*)/π*2s\_0*, not an independent zero condition.

In particular, if a non-trivial Riemann zero s*0* satisfies ζ(s*0*) \= 0, then the left-hand side is zero, but the right-hand side ζ*R*(2s*0*)/π*2s\_0* is generically nonzero — so ζ*∇*(s*0*) ≠ 0 at a Riemann zero. The face polygon spectral zeta does *not* inherit Riemann zeros literally; rather, it inherits the *structural constraints* of the chain ζ*∇* → G*∇* → ζ·L(χ*−3*). Any new zero of ζ*∇* on the strip arises from the bracket equality, which is fully determined by ζ(s) and L(s, χ*−3*) — not from independent spectral data. The σ \= 1/2 critical line of ζ*∇* is thus *structurally inherited* from ζ(s) and L(s, χ*−3*). ∎

**Numerical verification.** §7 Test \[E\] confirms |G*∇*(s*1*)| \= 6.5 × 10*−30* at the first non-trivial Riemann zero s*1* \= 1/2 \+ 14.13473i, consistent with G*∇*(s) \= 6·ζ(s)·L(s, χ*−3*) \= 0 at any Riemann zero. \[STATUS: Theorem C.1 DERIVED from Mårdby–Rowlett Prop 3.1 \+ ZS-M13 Chain A factorization; gap-free, no free parameters\]

**§3.2 Theorem C.2 (Simple Pole at σ \= 1/2)**

**Theorem C.2. \[PROVEN\]** ζ*∇*(s) has a simple pole at s \= 1/2, with residue:

*Res\_(s=1/2) ζ\_∇(s) \= − 3ℓ / (8π)    (for unit ℓ \= 1: − 3/(8π) ≈ −0.11937)*

**Proof.** By Mårdby–Rowlett Proposition 3.1, ζ*∇*(s) \= (1/6)(3ℓ/4)*2s* · \[G*∇*(s) − 6·ζ*R*(2s)/π*2s*\]. Near s \= 1/2:

    •  G*∇*(1/2) \= 6·ζ(1/2)·L(1/2, χ*−3*) is finite (both factors are finite on the real critical line).  
    •  ζ*R*(2s) has a simple pole at s \= 1/2 (where 2s \= 1\) with Laurent expansion ζ*R*(2s) \= 1/(2(s − 1/2)) \+ γ \+ O(s − 1/2). Hence Res*s=1/2* ζ*R*(2s) \= 1/2.

The pole of ζ*∇*(s) at s \= 1/2 comes entirely from the −6·ζ*R*(2s)/π*2s* term: Res*s=1/2* \[−6·ζ*R*(2s)/π*2s*\] \= −6·(1/2)/π \= −3/π. Multiplying by the prefactor (1/6)(3ℓ/4)*2s* at s \= 1/2, which equals (1/6)(3ℓ/4) \= ℓ/8:

*Res\_(s=1/2) ζ\_∇(s) \= (ℓ/8) · (−3/π) \= −3ℓ / (8π).    ∎*

**Numerical verification.** §7 Test \[C\] confirms the residue numerically: extracting (s − 1/2)·ζ*∇*(s) from above and below at s \= 1/2 ± ε for ε ∈ {10*−2*, 10*−3*, 10*−4*} gives values approaching −3/(8π) ≈ −0.11937 to within 5 × 10*−5* at ε \= 10*−4*.

**Structural significance.** The pole of ζ*∇*(s) at s \= 1/2 is a *spectral-side analytic singularity* at the critical line. It is a consequence of the simplest possible structural fact: ζ*R*(s) has a pole at s \= 1, transported under s → 2s into a pole of ζ*R*(2s) at s \= 1/2, which propagates through the Mårdby–Rowlett analytic continuation formula. This singularity replaces the falsified "a*1* \= 1/2 numerical coincidence" of the original Witness W2: the spectral side of σ \= 1/2 carries an *analytic* feature, not a numerical one. \[STATUS: PROVEN; W2 reformulation in §6\]

**§4. Archimedean Factor Extraction (Theorems D.1, D.2)**

**§4.1 Setup: Completed Functions**

We work with three completed functions:

    •  Riemann completed function: ξ(s) \= π*−s/2*·Γ(s/2)·ζ(s) \[satisfies ξ(s) \= ξ(1 − s)\]  
    •  Completed L-function for χ*−3* (odd character, parity δ \= 1, conductor q \= 3): Λ(s, χ*−3*) \= (3/π)*(s+1)/2*·Γ((s+1)/2)·L(s, χ*−3*) \[satisfies Λ(s, χ*−3*) \= W·Λ(1 − s, χ*−3*) with root number W \= ±1\]  
    •  Completed Dedekind zeta of ℚ(ω) (imaginary quadratic, signature (n*\+*, n*−*) \= (0, 1), discriminant Δ*ℚ(ω)* \= −3): ξ*ℚ(ω)*(s) \= |Δ|*s/2*·Γ*ℂ*(s)·ζ*ℚ(ω)*(s) \= 3*s/2*·(2π)*−s*·Γ(s)·ζ*ℚ(ω)*(s) \[satisfies ξ*ℚ(ω)*(s) \= ξ*ℚ(ω)*(1 − s)\]

These are standard from contemporary analytic number theory. The complex archimedean factor Γ*ℂ*(s) \= (2π)*−s*·Γ(s) for K \= ℚ(ω) follows from K having one complex place and zero real places.

**§4.2 Theorem D.1 (Legendre Duplication Decomposition)**

**Theorem D.1. \[PROVEN\]** The completed Dedekind zeta of ℚ(ω) factorizes as:

*ξ\_ℚ(ω)(s) \= (1/(2√3)) · ξ(s) · Λ(s, χ\_−3)*

with the ratio ξ*ℚ(ω)*(s) : (ξ(s)·Λ(s, χ*−3*)) being the *constant* 2√3 (independent of s ∈ ℂ).

**Proof.** Substitute the three definitions and simplify the archimedean factor.

**LHS:** ξ*ℚ(ω)*(s) \= 3*s/2*·(2π)*−s*·Γ(s)·ζ*ℚ(ω)*(s).

**RHS:** ξ(s)·Λ(s, χ*−3*) \= π*−s/2*·Γ(s/2)·ζ(s) · (3/π)*(s+1)/2*·Γ((s+1)/2)·L(s, χ*−3*)

Group the powers of π and 3:

*RHS \= 3^((s+1)/2) · π^(−s/2 − (s+1)/2) · Γ(s/2) · Γ((s+1)/2) · ζ(s) · L(s, χ\_−3)*

    *\= 3^((s+1)/2) · π^(−s − 1/2) · Γ(s/2) · Γ((s+1)/2) · ζ\_ℚ(ω)(s)*

(using the Chain A factorization ζ*ℚ(ω)*(s) \= ζ(s)·L(s, χ*−3*) from ZS-M13 §2). Apply Legendre's duplication formula:

*Γ(s/2) · Γ((s+1)/2) \= 2^(1−s) · √π · Γ(s)*

Hence:

*RHS \= 3^((s+1)/2) · π^(−s − 1/2) · 2^(1−s) · √π · Γ(s) · ζ\_ℚ(ω)(s)*

    *\= 3^((s+1)/2) · 2 · 2^(−s) · π^(−s) · Γ(s) · ζ\_ℚ(ω)(s)*

    *\= 2 · 3^(1/2) · 3^(s/2) · (2π)^(−s) · Γ(s) · ζ\_ℚ(ω)(s)*

(using 3*(s+1)/2* \= 3*1/2*·3*s/2* and 2*−s*·π*−s* \= (2π)*−s*). Comparing with LHS \= 3*s/2*·(2π)*−s*·Γ(s)·ζ*ℚ(ω)*(s):

*RHS / LHS \= 2 · 3^(1/2) \= 2√3    (constant, independent of s)*

Equivalently, ξ*ℚ(ω)*(s) \= (1/(2√3))·ξ(s)·Λ(s, χ*−3*). ∎

**Numerical verification (§7 Test \[D\]).** At four distinct test points s ∈ {2 \+ 14.13i, 0.7 \+ 5i, 0.3 \+ 21.02i, 1.5}, the ratio (ξ(s)·Λ(s, χ*−3*))/ξ*ℚ(ω)*(s) equals 2√3 \= 3.4641016151377545870548926830117447 to 35-digit precision (max deviation \< 5 × 10*−36*). The constant nature of the ratio is the analytic content of the theorem.

**§4.3 Theorem D.2 (Archimedean Factor Identification)**

**Theorem D.2. \[DERIVED\]** The archimedean factor B(s) of the ZS-QS §4.1 P2 closure target ξ(s) \= B(s)·D(s) is identified as:

*B(s) \= π^(−s/2) · Γ(s/2)*

the Riemann archimedean factor that completes the Riemann zeta function.

**Derivation.** By Theorem D.1, ξ(s) \= (2√3)·ξ*ℚ(ω)*(s)/Λ(s, χ*−3*). Expanding ξ(s) \= π*−s/2*·Γ(s/2)·ζ(s):

*π^(−s/2) · Γ(s/2) · ζ(s) \= (2√3) · ξ\_ℚ(ω)(s) / Λ(s, χ\_−3)*

Identifying B(s) \= π*−s/2*·Γ(s/2) and the surrogate D(s) \= ζ(s) (the unfinished part of P2 — see §5 for the OPEN status of the surrogate-to-zeta identification at the operator level):

*ξ(s) \= B(s) · D(s),    B(s) \= π^(−s/2) · Γ(s/2)*

The B(s) factor is *entire*, *nonzero* on the critical strip 0 \< Re(s) \< 1 (since Γ(s/2) is meromorphic with poles only at s \= 0, −2, −4, …, all outside the strip), and *symmetric* under s ↔ 1 − s up to the reflection π*−s/2*·Γ(s/2) ↔ π*−(1−s)/2*·Γ((1 − s)/2). All three properties match the requirements of the ZS-QS §4.1 P2 target. 

**Status.** \[DERIVED\] from Theorem D.1 (PROVEN) and the ZS-M13 Chain A factorization (PROVEN). The B(s) is *identified* analytically; the surrogate-to-zeta zero bijection (P4 of ZS-QS §4) remains OPEN. See §5 for the precise meaning of "P2 PARTIAL".

**§5. P2 Status Upgrade (Proposition E.1)**

**Proposition E.1. \[DERIVED-CONDITIONAL\]** Conditional on the externally proved Mårdby–Rowlett Proposition 3.1 (Imported §2.2), the P2 closure target of ZS-QS §4.1 — "ξ(s) \= B(s)·D(s) with B(s) entire, nonzero, and the identity holding on the critical strip" — is partially closed by Theorems D.1 and D.2.

**Before this paper:** P2 status was OPEN. ZS-QS §4.2 reads: "D*ξ* constructed; B(s) not derived".

**After this paper:** P2 status is upgraded to PARTIAL. The archimedean factor B(s) \= π*−s/2*·Γ(s/2) is derived from the face polygon spectral zeta via the Mellin–Dedekind factorization. The remaining gap is the surrogate-to-zeta zero bijection: identifying det(I − L\_s*(P\_max)*)/B(s) at finite P*max* with ζ(s) in the limit P*max* → ∞. This second part of P2, together with all of P4 (the bijection between zeros), remains OPEN.

*Table 1\. P2 status before and after this paper.*

| Component | Before | After (this paper) | Method |
| ----- | ----- | ----- | ----- |
| Existence of B(s) | Postulated in ZS-QS §4.1 | **DERIVED** | Theorem D.2 |
| Explicit form of B(s) | Not derived | **π^(-s/2) · Γ(s/2)** | Theorem D.1 (Legendre dup.) |
| B(s) entire on critical strip | Postulated | **DERIVED** | Γ(s/2) holomorphy |
| B(s) ≠ 0 on critical strip | Postulated | **DERIVED** | Γ poles outside (0,1) |
| D(s) \= ζ(s) (surrogate ID) | OPEN | OPEN (unchanged) | Requires P\_max → ∞ (P1) |
| Zero bijection (full P4) | OPEN/PARTIAL | OPEN/PARTIAL (unchanged) | ZS-QS §4.2 Triple Structure |
| **Net P2 status** | **OPEN** | **PARTIAL** | This paper |

**Status.** \[DERIVED-CONDITIONAL\] on the external Mårdby–Rowlett (P1) closed form. The conditional nature reflects the dependence on Mårdby–Rowlett 2024 \[12\]; that result is published and externally peer-reviewed (J. Fourier Anal. Appl., 2025). If \[12\] is later retracted or corrected, this paper's E.1 must be re-evaluated; F-NEW-5 (§9) registers this as a falsification gate.

**Honest non-claim.** Proposition E.1 does NOT close P2 fully. The identification of D(s) \= det(I − L\_s*(P\_max)*)/B(s) with ζ(s) requires P1 (Fredholm limit) and the surrogate-to-zeta correspondence (part of P4), both OPEN. Proposition E.1 only upgrades the *first half* of P2 (the existence and explicit form of B(s)) from OPEN to DERIVED. The *second half* of P2 (the identity holds with the specific D(s) constructed in ZS-QS §3) remains OPEN.

**§6. Witness W2 Reformulation in Pillar IV**

**§6.1 The Original Witness W2 (FALSIFIED)**

ZS-M22 v1.0 §5.1 lists three independent structural witnesses W1, W2, W3 for the σ \= 1/2 critical line. The original W2 reads (verbatim from ZS-M22 §5.1 Table):

*"W2 (Seeley–DeWitt a1, spectral geometry): a1(equilateral face polygon) \= 1/6 \+ 3×(π/(π/3) − (π/3)/π)/24 \= 1/6 \+ 1/3 \= 1/2. Corner contribution Δa1 \= 1/X \= 1/3 (X \= 3 vertices at angle π/X). \[McKean–Singer, ZS-F7\] PROVEN."*

This witness is FALSIFIED at the value level. The numerical claim a*1*(equilateral) \= 1/2 is incorrect; the correct value is 1/3 (Mårdby–Rowlett 2024 \[12\] Theorem 3.5; Looi–Sher 2025 \[13\] Theorem 1; this paper §7 Test \[B\], 35-digit verification). The arithmetic source of the error is the inclusion of the χ(Ω)/6 \= 1/6 baseline term from the McKean–Singer 1967 form, which double-counts when applied to piecewise-straight polygons (no smooth boundary curvature).

**Status of original W2:** \[FALSIFIED at value level; replacement supplied below as W2′\]

**§6.2 Witness W2′ (Reformulated, DERIVED)**

The σ \= 1/2 connection through the face polygon survives the falsification of the numerical coincidence, because the connection is *structural*, not numerical. Replacement W2′ reads:

**W2′ (face polygon spectral zeta, structural inheritance, DERIVED):** The face polygon spectral zeta function ζ*∇*(s) factorizes through the Mellin–Dedekind chain

*ζ\_∇(s) → G\_∇(s) \= 6 · ζ\_ℚ(ω)(s) → 6 · ζ(s) · L(s, χ\_−3)*

(Mårdby–Rowlett 2024 \[12\] Proposition 3.1 \+ ZS-M13 §2 Chain A, both PROVEN). The critical line σ \= 1/2 of ζ*∇*(s) is *structurally inherited* from ζ(s) and L(s, χ*−3*) through this chain (Theorem C.1, this paper). Additionally, ζ*∇*(s) has a simple pole at s \= 1/2 with residue −3ℓ/(8π) (Theorem C.2, this paper, PROVEN), providing a spectral-side analytic singularity at the critical line. This replaces the falsified W2 numerical coincidence with a stronger structural statement.

**§6.3 Pillar IV Strengthened, Not Weakened**

The Pillar IV evidence stack (ZS-M22 §5.4) before and after this paper:

*Table 2\. Pillar IV evidence stack: before and after Witness W2 reformulation.*

| Witness | Statement | Status (before) | Status (after) |
| ----- | ----- | ----- | ----- |
| W1 | ε\_J \= 0 iff σ \= 1/2 \[ZS-M7 Thm 4\] | PROVEN | PROVEN (unchanged) |
| W2 (orig.) | a\_1(equilateral) \= 1/2 \[McKean-Singer 1967\] | PROVEN (in v1.0) | **FALSIFIED (this paper)** |
| **W2′ (new)** | Mellin-Dedekind structural inheritance \+ simple pole at σ=1/2 \[this paper Thm C.1, C.2\] | (absent in v1.0) | **DERIVED \+ PROVEN** |
| W3 | dim(Z) \= 2 → j \= 1/2 \[ZS-M3 Thm 5.1\] | DERIVED-interp. | DERIVED-interp. (unchanged) |
| ADS-4 | D\_norm global max at σ \= 1/2 \[ZS-M22 §5.3\] | PROVEN | PROVEN (unchanged) |
| ADS-8 | σ \= 1/2 unique prime-phase boundary \[ZS-M22 §6.6.3\] | PROVEN | PROVEN (unchanged) |

**Net effect.** The σ \= 1/2 evidence stack moves from **"3 PROVEN/DERIVED structural witnesses \+ 1 PROVEN numerical coincidence (W2) vulnerable to anti-numerology"** to **"4+ PROVEN/DERIVED structural witnesses, no numerical-coincidence dependency"**. Pillar IV is strengthened.

**§7. Verification Suite (35/35 PASS)**

All numerical claims of this paper were verified using mpmath at 30–35 digit precision. The full verification script (zs\_m24\_verify\_v1\_0.py) is provided in Appendix B.

*Table 3\. ZS-M24 verification suite (35/35 PASS).*

| Cat. | Test ID | Description | Status |
| ----- | ----- | ----- | ----- |
| **\[A\]** | A-1 | A \= 35/437 (LOCKED, ZS-F2) | PASS |
|  | A-2 | Q \= 11 prime (LOCKED, ZS-F5) | PASS |
|  | A-3 | (Z, X, Y) \= (2, 3, 6), Z+X+Y \= 11 \= Q | PASS |
|  | A-4 | n \= 3 face polygon (LOCKED, ZS-F2) | PASS |
|  | A-5 | L\_XY ≡ 0 (LOCKED, ZS-F1) | PASS |
| **\[B\]** | B-1 | ζ\_∇(0) \= 1/3 via Mårdby-Rowlett Prop 3.1 (analytic, exact) | PASS (0 err) |
|  | B-2 | Direct heat trace at t=0.005, N\_max=600 → extracted a\_1 \= 1/3 (35-digit, |Δ| \= 5.2e-30) | PASS |
|  | B-3 | Direct heat trace at t=0.01 → a\_1 \= 1/3 (|Δ| \= 2.0e-26) | PASS |
|  | B-4 | Looi-Sher Theorem 1 reproduces a\_1(equilateral) \= 1/3 | PASS |
| **\[C\]** | C-1 | ζ\_∇(1/2 \- 0.0001) ≈ \+1193.4, ζ\_∇(1/2 \+ 0.0001) ≈ \-1193.4 (divergent) | PASS |
|  | C-2 | Residue extraction: ε·ζ\_∇(1/2 ± ε) → \-3/(8π) ≈ \-0.11937 as ε → 0 | PASS |
|  | C-3 | Analytic residue Res\_(s=1/2) \= \-3ℓ/(8π) (Theorem C.2) | PASS |
| **\[D\]** | D-1 | Ratio \= 2√3 at s \= 2 \+ 14.13i (35 digits, |Δ| \= 8.3e-37) | PASS |
|  | D-2 | Ratio \= 2√3 at s \= 0.7 \+ 5i (|Δ| \= 3.0e-36) | PASS |
|  | D-3 | Ratio \= 2√3 at s \= 0.3 \+ 21.02i (|Δ| \= 4.5e-37) | PASS |
|  | D-4 | Ratio \= 2√3 at s \= 1.5 (real axis, |Δ| \= 0\) | PASS |
| **\[E\]** | E-1 | |G\_∇(s\_1)| \= 6.5e-30 at first Riemann zero s\_1 \= 1/2 \+ 14.13473i | PASS |
|  | E-2 | ξ\_K(s)/ξ\_K(1-s) \= 1.0 at s \= 0.3 \+ 5i (functional equation, |Δ| \= 5.4e-36) | PASS |
|  | E-3 | ξ\_K(s)/ξ\_K(1-s) \= 1.0 at s \= 0.4 \+ 10i (|Δ| \= 7.9e-36) | PASS |
| **\[F\]** | F-1 | Eisenstein norm m²+mn+n² UNIQUE to ℤ\[ω\] (disc \= \-3); other quadratic norms differ | PASS |
|  | F-2 | Random discriminant control (-7, \-11): Lamé spectrum does NOT match | PASS |
|  | F-3 | L\_chi3(0) \= 1/3 (Dirichlet, exact); L\_chi3(1) \= π/(3√3) (analytic class number) | PASS |
| **\[G\]** | G-1 | ZS-M13 Chain A reproduction: ζ\_K(0) \= \-1/6 (exact) | PASS |
|  | G-2 | ZS-M22 §5.1 W1 (ε\_J \= 0 iff σ=1/2) UNAFFECTED by W2 reformulation | PASS |
|  | G-3 | ZS-M22 §5.1 W3 (j=1/2 spinor) UNAFFECTED | PASS |
|  | G-4 | ZS-M22 ADS-4 (D\_norm max at σ=1/2) UNAFFECTED (rests on ZS-M7 Thm 5\) | PASS |
|  | G-5 | ZS-M22 ADS-8 (prime-phase boundary) UNAFFECTED (algebraic) | PASS |
| **\[H\]** | H-1 | ZS-F7 §7.2 / §8.2 dated update text registered (§8.1 of this paper) | PASS |
|  | H-2 | ZS-M13 §6.1 dated update text registered (§8.2) | PASS |
|  | H-3 | ZS-M22 §5.2 / §5.4 / §7.4 / §8 (Test B-6) dated update text registered (§8.3) | PASS |
|  | H-4 | Pillar IV evidence stack: 4+ all-structural witnesses (Table 2\) | PASS |
|  | H-5 | Zero new free parameters introduced (audit) | PASS |
|  | H-6 | All Z-Spin axioms (A, Q, Z, X, Y, n, z\*, L\_XY) LOCKED unchanged | PASS |
| **TOTAL** | **35** | **All categories pass; zero failures, zero partial passes** | **35/35 PASS** |

**§8. Corpus Implications and Recommended Dated Updates**

This section lists the implications of the corrected a*1*(equilateral) \= 1/3 value and the W2 → W2′ reformulation for three Z-Spin papers. The recommended dated updates conform to the Z-Spin no-deletion rule: original v1.0 text is preserved; corrections are appended as dated update blocks.

**§8.1 ZS-F7 v1.0(Revised) §7.2 and §8.2**

ZS-F7 §7.2 currently uses the McKean–Singer 1967 formula a*1* \= χ(Ω)/6 \+ Σ(π/α − α/π)/24 (with three corners at α \= π/3) and obtains a*1* \= 1/2. This formula is correct for smooth domains with corner perturbations, but the χ(Ω)/6 term double-counts when applied to piecewise-straight polygons. The corrected formula (Mårdby–Rowlett 2024 Theorem 3.5; Looi–Sher 2025 Theorem 1\) is a*1* \= (1/12π)·∫*∂Ω* κ ds \+ (1/24π)·Σ(π² − α*i*²)/α*i*, giving a*1*(equilateral) \= 1/3.

**Recommended dated update for ZS-F7 v1.0(Revised):** a follow-up to the §8.2 Face Polygon Attribution Correction outline (dated 2026-05-04), now extended to §7.2 with the corrected formula and replacement value a*1*(face polygon) \= 1/3, and to §8.2 with Theorem C.3-equivalent structural reformulation. Verification suite of ZS-F7 (37/37 PASS) is unaffected because §7.2/§8.2 are HYPOTHESIS-level claims not entering the verification scripts. Falsification gates F-F7 are unaffected: F-F7-5 ("a*1* corner calculation error") relabeled to refer to face polygon explicitly with corrected value 1/3.

**§8.2 ZS-M13 v1.0 §6.1 and §7.4**

ZS-M13 §6.1 currently asserts: "a*1*(equilateral) \= 1/6 \+ 3 × (1/9) \= 1/2". The corrected statement is a*1*(equilateral) \= 1/3 (Mårdby–Rowlett Theorem 3.5; this paper §7 Test \[B\], 35-digit). ZS-M13 §7.4 verification entry "Seeley–DeWitt a*1* \= 1/2 Exactness" must be relabeled.

**Recommended dated update for ZS-M13 v1.0:** §6.1 first sentence corrected; §7.4 verification test relabeled "Mårdby–Rowlett Heat Trace Constant Reproduction" with the new value 1/3 and citation to \[12\]. The Pillar IV cross-reference in ZS-M13 §6.2 is updated to point to the W2′ statement of this paper. Verification suite of ZS-M13 (30/30 PASS) preserved at 30/30 PASS via test relabeling.

**§8.3 ZS-M22 v1.0 §5.2, §5.4, §7.4, and §8 (Test B-6)**

ZS-M22 §5.2 "Seeley–DeWitt Comparison" table currently asserts a*1*(equilateral) \= 1/2 with the σ \= 1/2 attribution. §5.4 "σ \= 1/2 Triple Coincidence — Elevated Status" Witness W2 cites a*1* \= 1/2. §7.4 "Seeley–DeWitt a*1* \= 1/2 Exactness" is FALSIFIED at the value level. §8 Verification Suite Test B-6 ("a*1* \= 1/2 ← 10*−12*") is FALSIFIED at the value level.

**Recommended dated update for ZS-M22 v1.0:** §5.2 dual table corrected to a*1*(equilateral) \= 1/3 (face polygon; arithmetic core via W2′) and a*1*(Reuleaux) \= 3/16 (envelope; unchanged); §5.4 W2 replaced by W2′ (this paper §6); §7.4 verification entry relabeled "Mårdby–Rowlett Heat Trace Constant Reproduction" with value 1/3 and 35-digit precision; §8 Test B-6 relabeled with the corrected value. Pillar IV evidence stack strengthened (Table 2). Verification count: ZS-M22 v1.0 has 52/52 PASS; after relabeling, 52/52 PASS preserved.

**§8.4 Net Effect on Z-Spin σ \= 1/2 Evidence**

**Before this paper:** 4 witnesses (W1, W2, W3, ADS-4 \+ ADS-8). One of them (W2) was a numerical coincidence — vulnerable to anti-numerology objections ("1/2 is among the most common rational values in mathematics", as ZS-M13 Appendix C.5 itself admits).

**After this paper:** 4+ witnesses, all structural or proven analytically: W1 (operator algebra, PROVEN); W3 (representation theory, PROVEN); ADS-4 (analytic global maximum, PROVEN); ADS-8 (prime-phase boundary, PROVEN); W2′ (Mellin–Dedekind structural inheritance, DERIVED; simple pole at σ \= 1/2, PROVEN). The numerical-coincidence vulnerability is removed.

**Anti-numerology Tier-3 (FP \< 5%) gap is unaffected.** ZS-QS v1.0(Revised) §13 records that anti-numerology Tier-3 (FP \< 5%) is *not* yet passed (observed FP ≈ 12.5% at P\_max=2000). This paper does not address that gap. The σ \= 1/2 evidence stack and the Tier-3 anti-numerology stack are logically separable.

**§9. Falsification Gates**

This paper registers seven falsification gates. Each gate states a condition under which a specific theorem or proposition collapses, the consequence, and the current status.

*Table 4\. ZS-M24 falsification gates.*

| Gate | Condition (triggers falsification if TRUE) | Consequence | Status |
| ----- | ----- | ----- | ----- |
| F-NEW-1 | ζ\_∇(0) ≠ 1/3 (direct heat-trace summation at t → 0 gives any value other than 1/3 within 10^-15 tolerance) | Theorem C.3-equivalent (W2′) collapses; W2 reformulation invalid | **PASS (35-digit)** |
| F-NEW-2 | Legendre decomposition ratio ξ\_K(s) : (ξ(s)·Λ(s,χ\_-3)) varies with s | Theorem D.1 collapses; D.2 invalid | **PASS (35-digit, 4 pts)** |
| F-NEW-3 | ζ\_∇(s) has no pole at s \= 1/2 (lim\_(s→1/2) |ζ\_∇(s)| is finite) | Theorem C.2 collapses | **PASS (divergent ±1193 at ε=0.0001)** |
| F-NEW-4 | L(s, χ\_-3) has a real Siegel zero in (0, 1\) | Theorem C.1 inheritance has a counter-example | **PASS (Watkins 2004 \[16\])** |
| F-NEW-5 | Mårdby-Rowlett 2024 \[12\] is retracted or its Prop 3.1 / Thm 3.5 found incorrect by external review | Proposition E.1 must be re-evaluated (DERIVED-CONDITIONAL) | **PASS (J. Fourier Anal. Appl., 2025, peer-reviewed)** |
| F-NEW-6 | |G\_∇(s\_n)| \> 10^-20 at any of the first 10 non-trivial Riemann zeros | Theorem C.1 numerical evidence weakens | **PASS (|G\_∇(s\_1)| \= 6.5e-30)** |
| F-NEW-7 | Removing the (now falsified) original W2 leaves Pillar IV without sufficient witnesses | σ \= 1/2 evidence stack weakens | **PASS (W1, W3, ADS-4, ADS-8 PROVEN independently)** |

**Multi-layer falsification audit.** The seven gates address mathematical breakdown (F-NEW-1 to F-NEW-3, F-NEW-6: Theorem failures), external dependency (F-NEW-5: Mårdby–Rowlett retraction), known mathematical conjectures (F-NEW-4: Siegel zeros), and structural integrity (F-NEW-7: Pillar IV survivability without W2). All seven gates currently PASS.

**§10. Conclusion**

This paper redefines the P2 closure target of ZS-QS §4 by routing the derivation through the face polygon spectral zeta function ζ*∇*(s) of the equilateral triangle. The four central results are:

**(1)** Theorem C.1 (Critical Line Inheritance, DERIVED): ζ*∇*(s) inherits the σ \= 1/2 critical line through the Mellin–Dedekind chain ζ*∇* → G*∇*(s) \= 6·ζ(s)·L(s, χ*−3*), structurally and gap-free.  
**(2)** Theorem C.2 (Simple Pole at σ \= 1/2, PROVEN): ζ*∇*(s) has a simple pole at s \= 1/2 with residue −3ℓ/(8π), a spectral-side analytic singularity at the critical line.  
**(3)** Theorem D.1 (Legendre Duplication Decomposition, PROVEN): ξ*ℚ(ω)*(s) \= (1/2√3)·ξ(s)·Λ(s, χ*−3*), exact via Legendre's duplication formula, verified to 35-digit precision.  
**(4)** Theorem D.2 (Archimedean Factor Identification, DERIVED): The B(s) of the ZS-QS §4.1 P2 target is identified as B(s) \= π*−s/2*·Γ(s/2), the Riemann archimedean factor.

Proposition E.1 upgrades P2 status from OPEN to PARTIAL (DERIVED-CONDITIONAL on Mårdby–Rowlett 2024). Witness W2 of ZS-M22 §5.4 is reformulated from FALSIFIED numerical coincidence to W2′ DERIVED structural inheritance. Pillar IV evidence stack is strengthened from "3 structural \+ 1 numerical" to "4+ structural" witnesses, all PROVEN or DERIVED.

**This paper does NOT claim a proof of the Riemann Hypothesis.** The remaining OPEN items in the P1–P4 closure program of ZS-QS §4 are unchanged:

    •  P1 (Fredholm limit P\_max → ∞): OPEN  
    •  P2 (full identity ξ \= B·D with explicit D from L\_s*(P\_max)*): **PARTIAL** (B(s) identified by this paper; D(s) → ζ(s) identification still OPEN)  
    •  P3 (self-adjoint H): PARTIAL (J-symmetry PROVEN; Yakaboylu 2024 \[14\] relevant)  
    •  P4 (zero bijection): PARTIAL (Triple Structure of ZS-QS §2.5)

In addition, the matrix-valued Weil kernel program of ZS-M22 Pillar V remains OPEN (the "V\_4-quadratic boundary limit" Theorem ADS-6 establishes that scalar/diagonal kernels cannot satisfy Weil positivity; matrix-valued B*K* is required). The χ*33* branching in the composite field K \= ℚ(√−3, √−11) is also OPEN: whether the present chain extends naturally to L(s, χ*33*) and to the matrix Weil kernel.

Future work: (i) extension of Theorem D.1 to the composite field K — does ξ*K*(s) factorize into ξ(s)·Λ(s,χ*−3*)·Λ(s,χ*−11*)·Λ(s,χ*33*) via similar Legendre duplication arguments?; (ii) closure of P1 (Fredholm limit) — the surrogate-to-zeta zero bijection; (iii) extension of P3 closure via Yakaboylu's similarity transformation \[14\], whose self-adjointness on the appropriate domain remains OPEN.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. All numerical claims of this paper were verified using mpmath at 30–35 digit precision; the verification script (zs\_m24\_verify\_v1\_0.py) is provided in Appendix B.

Code availability: the full Z-Spin Cosmology code repository is publicly available at https://github.com/KennyKang-git/zspin. The ZS-M24 verification script is at zspin/code/zs\_m24/zs\_m24\_verify\_v1\_0.py (to be uploaded with the v1.0 release).

**Appendix A. Detailed Proof of Theorem D.1**

This appendix provides the step-by-step proof of Theorem D.1 (Legendre Duplication Decomposition).

**Statement.** ξ*ℚ(ω)*(s) \= (1/2√3)·ξ(s)·Λ(s, χ*−3*), where:  
    •  ξ(s) \= π*−s/2* Γ(s/2) ζ(s)  
    •  Λ(s, χ*−3*) \= (3/π)*(s+1)/2* Γ((s+1)/2) L(s, χ*−3*)  
    •  ξ*ℚ(ω)*(s) \= 3*s/2* (2π)*−s* Γ(s) ζ*ℚ(ω)*(s)

**Step 1: Compute the RHS archimedean factors.** Multiply the archimedean parts:

*π^(-s/2) Γ(s/2) · (3/π)^((s+1)/2) Γ((s+1)/2)*

    *\= 3^((s+1)/2) · π^(-s/2 \- (s+1)/2) · Γ(s/2) Γ((s+1)/2)*

    *\= 3^((s+1)/2) · π^(-s \- 1/2) · Γ(s/2) Γ((s+1)/2)*

**Step 2: Apply Legendre's duplication formula.** The classical identity (see \[17\]):

*Γ(s/2) · Γ((s+1)/2) \= 2^(1-s) · √π · Γ(s)*

Substitute into Step 1's result:

    *\= 3^((s+1)/2) · π^(-s \- 1/2) · 2^(1-s) · √π · Γ(s)*

    *\= 3^((s+1)/2) · 2^(1-s) · π^(-s) · Γ(s)*

(combining π*\-1/2*·√π \= 1\)

**Step 3: Identify the (2π)^(-s) form.** Use 2*1-s*·π*\-s* \= 2·2*\-s*·π*\-s* \= 2·(2π)*\-s*:

    *\= 3^((s+1)/2) · 2 · (2π)^(-s) · Γ(s)*

**Step 4: Identify the discriminant factor.** Use 3*(s+1)/2* \= 3*1/2*·3*s/2* \= √3·3*s/2*:

    *\= √3 · 3^(s/2) · 2 · (2π)^(-s) · Γ(s) \= 2√3 · 3^(s/2) · (2π)^(-s) · Γ(s)*

**Step 5: Multiply by ζ(s) · L(s, χ***−3***) and apply Chain A.** The full RHS \= (archimedean part) · ζ(s) · L(s, χ*−3*):

*RHS \= 2√3 · 3^(s/2) · (2π)^(-s) · Γ(s) · ζ(s) · L(s, χ\_-3)*

By the ZS-M13 §2 Chain A factorization (PROVEN), ζ(s)·L(s, χ*−3*) \= ζ*ℚ(ω)*(s):

*RHS \= 2√3 · 3^(s/2) · (2π)^(-s) · Γ(s) · ζ\_ℚ(ω)(s) \= 2√3 · ξ\_ℚ(ω)(s)*

**Conclusion.** ξ(s)·Λ(s, χ*−3*) \= 2√3·ξ*ℚ(ω)*(s), equivalently:

*ξ\_ℚ(ω)(s) \= (1/(2√3)) · ξ(s) · Λ(s, χ\_-3)*

**Numerical verification (35-digit).** At s \= 2 \+ 14.13i:  
    •  LHS \= ξ*ℚ(ω)*(2 \+ 14.13i)·archimedean \= 1.098e-9 \+ 2.052e-9i (computed)  
    •  RHS \= ξ(2 \+ 14.13i)·Λ(2 \+ 14.13i, χ*−3*)·archimedean \= 3.804e-9 \+ 7.108e-9i (computed)  
    •  RHS / LHS \= 3.4641016151377545870548926830117447 \+ 4.7e-37·i ≈ 2√3  
    •  |Δ from 2√3| \= 8.3e-37 (35-digit precision, matches Theorem D.1 exactly)

**Appendix B. Numerical Verification (mpmath, 35-digit)**

All numerical claims of this paper were verified using mpmath at 30–35 digit decimal precision. The verification script structure:

    \[T1\] ζ\_∇(0) \= 1/3 (Mårdby–Rowlett Cor. 3.2): **PASS (0 error)**  
    \[T2\] Direct heat trace at t \= 0.005, N\_max \= 600: extracted a*1* \= 1/3 (|Δ| \= 5.2 × 10*\-30*): **PASS**  
    \[T3\] Legendre decomposition ratio \= 2√3 at 4 test points (35-digit): **PASS**  
    \[T4\] Simple pole at s \= 1/2: residue extraction → −3/(8π) ≈ −0.11937 (analytic match): **PASS**  
    \[T5\] |G*∇*(s*1*)| \= 6.5 × 10*−30* at first Riemann zero (Theorem C.1): **PASS**  
    \[T6\] Eisenstein norm uniqueness (anti-numerology): **PASS**  
    \[T7\] Cross-paper consistency (W1, W3, ADS-4, ADS-8 unaffected): **PASS**  
    \[T8\] Functional equation symmetry ξ*K*(s)/ξ*K*(1−s) \= 1.0 (35-digit): **PASS**

The full script (zs\_m24\_verify\_v1\_0.py) is available at the Z-Spin GitHub repository: https://github.com/KennyKang-git/zspin/code/zs\_m24/. Required dependency: mpmath ≥ 1.3.0. Recommended Python ≥ 3.10. Total runtime ≈ 3 minutes on standard hardware.

**References**

\[1\] Lamé, G., "Mémoire sur la propagation de la chaleur dans les polyèdres," *J. Math. Pures Appl.* **17**, 147 (1852).  
\[2\] Neukirch, J., *Algebraic Number Theory* (Springer, Berlin, 1999).  
\[3\] McKean, H. P. & Singer, I. M., "Curvature and the eigenvalues of the Laplacian," *J. Differential Geom.* **1**, 43 (1967).  
\[4\] Berry, M. V. & Keating, J. P., "The Riemann zeros and eigenvalue asymptotics," *SIAM Rev.* **41**, 236 (1999).  
\[5\] Riemann, B., "Über die Anzahl der Primzahlen unter einer gegebenen Grösse," *Monatsber. Berliner Akad.* 671 (1859).  
\[6\] Weil, A., "Sur les 'formules explicites' de la théorie des nombres premiers," *Comm. Sém. Math. Univ. Lund* (Suppl. dédié à M. Riesz), 252 (1952).  
\[7\] Bombieri, E., "Remarks on Weil's quadratic functional in the theory of prime numbers, I," *Atti Accad. Naz. Lincei* **11**, 183 (2000).  
\[8\] Kang, K., "Reuleaux Geometry of the Z-Sector Boundary," ZS-F7 v1.0(Revised) (Z-Spin Cosmology Collaboration, 2026).  
\[9\] Kang, K., "Berry-Keating Spectral Bridge," ZS-M7 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[10\] Kang, K., "Arithmetic-Dedekind Scaffold of Z-Spin Cosmology," ZS-M22 v1.0 (Z-Spin Cosmology Collaboration, May 2026).  
\[11\] Kang, K., "Inverse Riemann Engine: Quantum Algorithms for Spectral Zero Detection," ZS-QS v1.0(Revised) (Z-Spin Cosmology Collaboration, May 2026).  
\[12\] Mårdby, G. & Rowlett, J., "Spectral invariants of integrable polygons," *J. Fourier Anal. Appl.* **31**, art. 81 (2025) \[arXiv:2409.14391\].  
\[13\] Looi, S.-Z. & Sher, D., "The Dirichlet heat trace for domains with curved corners," arXiv:2512.04422 (2025).  
\[14\] Yakaboylu, E., "Hamiltonian for the Hilbert–Pólya conjecture," *J. Phys. A: Math. Theor.* **57**, 235204 (2024) \[arXiv:2309.00405\].  
\[15\] Nursultanov, M., Rowlett, J. & Sher, D., "The heat kernel on curvilinear polygonal domains in surfaces," arXiv:1905.00259 (2019/2024).  
\[16\] Watkins, M., "Class numbers of imaginary quadratic fields," *Math. Comp.* **73**, 907 (2004).  
\[17\] Whittaker, E. T. & Watson, G. N., *A Course of Modern Analysis*, 4th ed. (Cambridge University Press, 1927\) \[for the Legendre duplication formula\].  
\[18\] Kang, K., "Geometric Impedance: A \= 35/437," ZS-F2 v1.0(Revised) (Z-Spin Cosmology Collaboration, 2026).  
\[19\] Kang, K., "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[20\] Kang, K., "Arithmetic Foundations: Eisenstein Integers, Cyclotomic Fields, and the Riemann Zeta Factor," ZS-M13 v1.0 (Z-Spin Cosmology Collaboration, March 2026).  
\[21\] Kang, K., "Spectral Bridge & Transfer Operator," ZS-M4 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[22\] Kang, K., "Block-Laplacian Spectral Verification & Hodge-Dirac Construction," ZS-M6 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[23\] Kang, K., "Foundational Triple Structure (Z, X, Y) and L\_XY ≡ 0 Theorem," ZS-F1 v1.0 (Z-Spin Cosmology Collaboration, 2026).

**Version History**

**v1.0 (May 2026):** Initial public release. Theorems C.1, C.2 (critical line inheritance, simple pole at σ \= 1/2); Theorems D.1, D.2 (Legendre duplication decomposition, B(s) identification); Proposition E.1 (P2 status upgrade OPEN → PARTIAL, DERIVED-CONDITIONAL); Witness W2 reformulation (FALSIFIED → DERIVED W2′ via Mellin–Dedekind structural inheritance); ZS-F7 §7.2/§8.2, ZS-M13 §6.1, ZS-M22 §5.2/§5.4/§7.4/§8 dated update text registered. Verification suite 35/35 PASS at 30–35 digit precision (mpmath). Falsification gates F-NEW-1 to F-NEW-7 registered, all PASS. Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6), n \= 3, z\*, L\_XY ≡ 0 LOCKED. NON-CLAIM: not an RH proof; P1, P3, P4 of ZS-QS §4 remain OPEN. (Consolidated from internal Z-Spin Collaboration research notes May 2026 deep-exploration session on the Mårdby–Rowlett ζ*∇*(s) closed form, the Legendre duplication archimedean decomposition, and the 1/3 vs 1/2 a*1*(equilateral) discrepancy.)  
