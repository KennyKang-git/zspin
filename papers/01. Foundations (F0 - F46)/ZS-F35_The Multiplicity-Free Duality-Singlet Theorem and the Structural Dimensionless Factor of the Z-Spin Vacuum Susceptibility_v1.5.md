# **ZS-F35**

# **The Multiplicity-Free Duality-Singlet Theorem and the Structural Dimensionless Factor of the Z-Spin Vacuum Susceptibility**

**Author:** Kenny Kang  
**Date:** June 2026  
**Theme / Code:** Foundations / ZS-F35  
**Version:** 1.5 (terminal; supersedes v1.4, v1.3, v1.2, v1.1, v1.0)  
**Verification:** 23 PROVEN \+ 4 IDENTITY PASS | 6 ASSUMPTIONS tracked (not derivations) | general theorem T1 (proof \= Schur), Lorentzian bridge, and the FULLY EXACT character-field obstruction T2 — symbolic commutant (rank 34, nullity 2), s² \= 5I, det s \= −125, \[s, R(g)\] \= 0 for all 60 g ∈ A₅, ⋆ \= (1/√5)s non-rational — machine-checked in sympy | structural dimensionless factor derived; one UV-normalization gate (C\_norm) left to ZS-F36 | Zero fitted parameters | (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.  
---

## **§0. Abstract**

We prove a general representation-theoretic result and a field-of-definition obstruction, and use them to isolate and derive the **structural dimensionless factor** of the Z-Spin odd-sector vacuum susceptibility, leaving one explicit UV-normalization gate.  
**Multiplicity-Free Duality-Singlet Theorem (T1).** Let a finite group G act on a finite-dimensional unitary complex representation V \= U₊ ⊕ U₋, where U₊, U₋ are non-isomorphic absolutely irreducible G-modules of equal complex dimension d, each of multiplicity one. Then the commutant is End\_G(V) \= ℂP₊ ⊕ ℂP₋; the unique traceless invariant (up to scale) is the duality involution J \= P₊ − P₋, with J² \= I, Tr J \= 0, and the Hilbert–Schmidt norm (relative to the invariant Hermitian inner product) ‖J‖²\_HS \= Tr(J†J) \= 2d. If a CP-odd source couples as ĉ\_θ \= λJ, then with the order-parameter metric G (with G(J, J) \= G\_J‖J‖²\_HS) the response is ĉ\_θ†G⁻¹ĉ\_θ \= |λ|²·(2d)/G\_J, a single scalar. The invariant ‖J‖² \= 2d is carrier-independent; J² \= I additionally requires V \= U₊ ⊕ U₋ exactly. The theorem follows from Schur’s lemma.  
**Z-Spin instance.** With G \= A₅ and the rank-6 bivector carrier Λ²V₄ \= **3 ⊕ 3′** (F34.BIV), the duality involution is the Hodge star ⋆, and ν\_s² \= ‖⋆‖²\_HS \= 2d \= 6 \= dim Y. The source is ⋆ on **complementary grounds**: a representation-theoretic uniqueness (T1) and a physical Pontryagin-source identification (δS\_θ/δθ has operator ⋆ since F∧F \= ⟨F, ⋆F⟩). The v1.1 group-theory error is corrected (the central inversion of I\_h ≅ A₅ × ℤ₂ cannot swap 3 ↔ 3′; the swap is the outer automorphism, S₅ ≇ A₅ × ℤ₂, physical realization OPEN \= F34 G-Outer-Physical). The Euclidean computation transfers to Lorentzian signature via J\_L \= −i⋆\_L (J\_L² \= I).  
**Character-field obstruction (T2).** The endomorphism algebra of the rational form is End\_{ℚA₅}(3 ⊕ 3′) \= ℚ(√5) — generated over ℚ by an integer operator s with s² \= 5I, Tr s \= 0, det s \= −125, commuting with the entire A₅ action — and the duality involution ⋆ \= (1/√5)s requires the irrational coefficient 1/√5. Hence no A₅-stable ℚ-form (a fortiori no A₅-stable ℤ-lattice) makes ⋆ rational; the disc(A₄) \= 5 root lattice is one concrete instance. This is a special case of a general field-of-definition phenomenon: for any Galois-conjugate pair of absolutely irreducible modules with a real quadratic character field ℚ(√m), the duality involution is (1/√m)s with s² \= mI, never rational. (Verified fully exactly in ℚ(√5): symbolic commutant, rank 34 / nullity 2, s² \= 5I, \[s, R(g)\] \= 0 for all g ∈ A₅.) Consequently ν\_s² \= 6 is the Hilbert–Schmidt norm relevant to the kinetic susceptibility; flux quantization belongs separately to the integral cohomology lattice, which the Hodge involution need not preserve. T2 identifies this metric–arithmetic mismatch — the icosahedral √5/golden ratio.  
**Result.** Collapsing the convention-dependent normalizations into one observable stiffness G̃\_s := V\_Σ G\_s/Z\_match, the dimensionless coefficient factorizes:  
χ₋⁽ˢ⁾ \= (dim Y)² · (A/Q) · C\_norm · M\_UV⁴ \= (1260/4807) · C\_norm · M\_UV⁴, C\_norm \= G̃\_s⁻¹·(c\_e/2π)².  
The arithmetic identity 36 A/Q \= 1260/4807 is PROVEN; that this is the physical structural factor is DERIVED-CONDITIONAL on ĉ\_θ \= ⋆ (the F34.BIV carrier reduction). Under the Canonical UV Normalization C\_UV \= {G̃\_s \= 1, c\_e \= 2π}, C\_norm \= 1 exactly, giving χ₋⁽ˢ⁾ \= (1260/4807) M\_UV⁴ ≈ 0.262 M\_UV⁴; but C\_norm \= 1 is the closure gate deferred to ZS-F36. The residual is **one dimensionless gate (C\_norm) plus one irreducible dimensionful scale (M\_UV)**. Verification: 23 PROVEN \+ 4 IDENTITY PASS (NumPy \+ SymPy).  
---

## **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Explicit proof or exact machine verification; no undischarged assumption. |
| **DERIVED** | Follows from PROVEN results by stated steps; no new parameter. |
| **DERIVED-CONDITIONAL** | Derived modulo explicitly named, falsifiable conditions. |
| **DERIVED-BY-INHERITANCE** | Uses an upstream corpus result, not re-proven here. |
| **HYPOTHESIS-strong** | Structurally motivated; a key value/identification not yet proven. |
| **NO-GO** | A proven impossibility/non-uniqueness disciplining the program. |
| **IDENTITY / REGRESSION** | An arithmetic or cross-version consistency; no new physical content. |
| **ASSUMPTION-CONSISTENCY** | A check that a stated assumption is internally consistent — not its derivation. |
| **OPEN** | Conceptually unresolved; a genuine gap. |
| **PROVEN-irreducible** | Proven that the quantity cannot be fixed by the stated inputs. |

---

## **§1. Introduction**

ZS-F34 reduced the odd-sector vacuum susceptibility to χ₋ \= (Z\_match g\_reg²/4π²V\_Σ) e₆² ĉ\_θᵀG⁻¹ĉ\_θ and called itself a *reduction, not a closure*. This paper’s history is a record of progressive correction: v1.0 rearranged unknowns; v1.1 over-claimed a closure on a flawed group-theoretic step; v1.2 reframed the result as a conditional factorization; v1.3 corrected the C\_norm definition, strengthened the verification, and lifted the content to a general theorem and a lattice question. A fourth review identified four remaining issues — an over-broad theorem hypothesis, a verify/probe inconsistency, a T2 conclusion stronger than its computation, and a missing Lorentzian bridge — and a route to make the lattice obstruction a genuine theorem. v1.4 implements all of them and is the **terminal** version of ZS-F35.  
The central content is a general theorem (T1, §3): in a finite-symmetry theory, a multiplicity-free pair of equal-dimension absolutely-irreducible modules carries a unique traceless invariant — a duality involution — to which a CP-odd source couples, reducing the susceptibility to a single scalar. Z-Spin is the case G \= A₅, d \= 3, J \= ⋆ (§4). The norm ν\_s² \= 2d \= 6 is the Hilbert–Schmidt norm; a field-of-definition theorem (T2, §5) proves the duality involution is non-rational on every A₅-stable ℚ-form, with disc(A₄) \= 5 — the icosahedral √5 — as one lattice instance. The remaining normalizations collapse into one observable stiffness and one Dirac coefficient (§§6–7); the result is the factorization above, with one dimensionless gate and one dimensionful scale left for ZS-F36 (§10).  
---

## **§2. The cosmic split and the single invariant mode**

The register channel algebra is End(V₁₁), V₁₁ \= ℂ¹² ⊖ 1, character (11, −1, −1, 1, 1\) \= 3 ⊕ 3′ ⊕ 5\. As an A₅-module,  
End(V₁₁) \= 3·1 ⊕ 6·3 ⊕ 6·3′ ⊕ 8·4 ⊕ 10·5, dim \= 121 \= Q².  
The trivial isotypic is three-dimensional. **\[PROVEN P1.\]** The arithmetic split 6 \+ 32 \+ 83 \= 121 with three trivial copies is PROVEN (P2a); the physical assignment of dim 6 to the baryon bivector 3 ⊕ 3′, 32 to CDM, and 83 to dark energy, with two trivial copies in CDM and one in dark energy, is DERIVED-BY-INHERITANCE from the upstream cosmic split (F34/A19). **\[P2b.\]** Within the exact-A₅, invariant-source branch (one of the three source branches of F34.SR), the dark-energy effective mode count is **N\_eff \= 1**.  
---

## **§3. The Multiplicity-Free Duality-Singlet Theorem (general)**

**Theorem T1.** Let G be a finite group and V \= U₊ ⊕ U₋ a finite-dimensional unitary complex representation, where U₊, U₋ are non-isomorphic **absolutely irreducible** G-modules with dim U₊ \= dim U₋ \= d, each of multiplicity one. Let P₊, P₋ be the equivariant orthogonal projectors (with respect to a chosen G-invariant Hermitian inner product). Then:

1) **(Schur)** End\_G(V) \= ℂP₊ ⊕ ℂP₋, of complex dimension 2\.  
2) The trace map on the two-dimensional commutant has one-dimensional kernel ℂ(P₊ − P₋); the **duality involution** J := P₊ − P₋ spans it, and the identity I \= P₊ \+ P₋ provides a canonical complementary line.  
3) J² \= I, Tr J \= 0, and the **Hilbert–Schmidt norm** relative to the invariant Hermitian structure is ‖J‖²\_HS \= Tr(J†J) \= dim U₊ \+ dim U₋ \= **2d**. The invariant ‖J‖² \= 2d is *carrier-independent*; J² \= I additionally requires V \= U₊ ⊕ U₋ exactly.  
4) If a CP-odd (θ-type) source couples as ĉ\_θ \= λJ (λ ∈ ℂ), let G be the metric on the order-parameter space with G(J, J) \= G\_J‖J‖²\_HS (G\_J the stiffness in the J direction). Then ĉ\_θ†G⁻¹ĉ\_θ \= |λ|²·(2d)/G\_J — a single scalar.

*Proof.* (i) Over ℂ with U± absolutely irreducible, Schur’s lemma gives Hom\_G(U₊, U₋) \= Hom\_G(U₋, U₊) \= 0 and End\_G(U±) \= ℂ; hence the commutant is ℂP₊ ⊕ ℂP₋. (ii) Tr(aP₊ \+ bP₋) \= (a \+ b)d, vanishing iff a \= −b. (iii) J \= \+1 on U₊, −1 on U₋, so J² \= I and Tr J \= 0; ‖J‖²\_HS \= Tr(P₊) \+ Tr(P₋) \= 2d. The HS norm uses the invariant Hermitian structure (it is not invariant under non-orthogonal change of basis); J² \= I uses P₊ \+ P₋ \= I\_V, valid only when V is exactly U₊ ⊕ U₋. (iv) Apply F34.SR with c \= λJ and G⁻¹ acting as G\_J⁻¹ on the J line.   
The theorem **follows analytically from Schur’s lemma**; it is illustrated numerically for three groups — A₅ (d \= 3), S₅ (d \= 4), S₃ (d \= 1\) — and the carrier-dependence of J² \= I is exhibited explicitly (‖J‖² \= 2d on both an exact and an enlarged carrier, J² \= I only on the exact one). **\[Illustrations T1-A5, T1-S5, T1-S3, T1-carrier, T1-chi.\]**  
**Balanced-involution converse (remark).** A G-invariant involution J (J² \= I) with Tr J \= 0 on a 2d-dimensional carrier forces each ±1 eigenspace to have dimension d; if the two eigenspaces are non-isomorphic irreps (equivalently, exchanged by an outer automorphism), the carrier is exactly U₊ ⊕ U₋. A *balanced* duality involution thus selects the d ⊕ d split structurally.  
T1 is a direct corollary of Schur’s lemma; its value here is in combination with the Pontryagin source identification (§4.3) and the field-of-definition obstruction (§5).  
---

## **§4. The Z-Spin instance (d \= 3\)**

### **§4.1 Group-theory correction: I\_h ≠ S₅**

The two A₅-triplets 3, 3′ are exchanged by the outer automorphism σ ∈ Out(A₅), realized by an odd permutation in S₅. The v1.1 claim that the full icosahedral symmetry I\_h ≅ A₅ × ℤ₂ forces this is **incorrect**: the ℤ₂ of I\_h is the central inversion, which commutes with A₅ and (Schur) acts as a scalar on each irrep, hence *preserves* 3, 3′. The swap-implementer is non-central (**P4, P6**), belonging to S₅ ∖ A₅, and S₅ ≇ A₅ × ℤ₂ (trivial center). The physical realization of σ is the OPEN gate **G-Outer-Physical** inherited from F34. A symmetry-based forcing is unavailable; §§4.2–4.3 are used instead.

### **§4.2 Carrier uniqueness, and the Lorentzian bridge**

By Theorem T1 with G \= A₅, V \= Λ²V₄ \= Λ²₊ ⊕ Λ²₋ \= 3 ⊕ 3′ (F34.BIV), d \= 3: the A₅-commutant is span{P₃, P₃′} (dimension 2; **P5**), and the unique traceless invariant is ⋆ \= P₃ − P₃′. A character check confirms the eigenspaces are the irreps 3, 3′ (χ at a 5-cycle equals φ̄, φ; **P3**); the traceless commutant is exactly span{⋆} (**P7**, residual 10⁻¹⁶).  
**Signature.** The representation-theoretic computation is performed in Euclidean signature, where the 4-dimensional 2-form Hodge star satisfies ⋆² \= \+1, giving the real self-dual/anti-self-dual split 3 ⊕ 3′. In Lorentzian signature (1, 3\) the 2-form Hodge star satisfies ⋆\_L² \= −1, with eigenvalues ±i on the complexified bivector; the corresponding involution is J\_L := −i⋆\_L, satisfying J\_L² \= I with ±1 eigenspaces (3 each). The algebraic identities (⋆\_L² \= −I, J\_L² \= I) are PROVEN; the further step of applying the Euclidean 3 ⊕ 3′ susceptibility norm to the physical Lorentzian EFT uses this complexification/Wick-rotation identification and is DERIVED-CONDITIONAL. **\[PROVEN: L1, L2, L3.\]**

### **§4.3 The Pontryagin source: an action-level derivation**

The CP-odd (θ) coupling of a 2-form field strength F is the topological term S\_θ \= (θ/8π²)∫\_{M₄} F∧F. In four dimensions the Pontryagin density equals the Hodge pairing, F∧F \= ⟨F, ⋆F⟩ vol, so δS\_θ/δθ \= (1/8π²)⟨F, ⋆F⟩, and the θ-source operator is exactly ⋆. Two conditions complete the bridge: (a) the F34 odd three-form A₃⁻ reduces (on Y₆ \= M₄ × Σ₂) to this bivector Pontryagin source — the F34.BIV carrier reduction; (b) no other A₅-invariant CP-odd operator mixes — *guaranteed by Theorem T1*, since ⋆ is the only traceless A₅-invariant on the carrier. Hence  
**ĉ\_θ \= ⋆**, giving ν\_s² \= ‖⋆‖²\_HS \= 2d \= 6 \= dim Y.  
The two arguments are **complementary, not independent**: the mathematics (T1) supplies a unique traceless line; the physics (the Pontryagin action) supplies that the θ-source lies on that line, and its tracelessness. With (b) PROVEN via T1, ĉ\_θ \= ⋆ is DERIVED modulo only the carrier reduction (a). **\[S1: DERIVED-CONDITIONAL on the F34.BIV carrier reduction.\]**

### **§4.4 Why A₅-equivariance alone is insufficient (NO-GO)**

In the full three-dimensional trivial isotypic of End(V₁₁) without the carrier restriction or coupling identification, the source would be a free line orthogonal to the CDM 2-plane, and ν\_s² would not be invariant (3 vs 49 for two admissible embeddings). **\[PROVEN P10.\]** The carrier/coupling identification of §§4.2–4.3 is load-bearing.  
---

## **§5. The character-field obstruction (T2)**

**Theorem T2 (no rational duality involution).** Let W \= 3 ⊕ 3′ be the six-dimensional rational A₅-representation (the Galois orbit of the two absolutely-irreducible triplets). Then the rational endomorphism algebra is the **character field**  
End\_{ℚA₅}(W) \= ℚ(√5),  
generated over ℚ by an **integer** operator s (in the A₄ root basis) with s² \= 5I, Tr s \= 0, det s \= −125, and \[s, R(g)\] \= 0 for all g ∈ A₅. The duality involution ⋆ \= P₃ − P₃′ satisfies ⋆ \= (1/√5)·s, whose coefficient 1/√5 ∉ ℚ. Therefore ⋆ is not a rational endomorphism of any A₅-stable ℚ-form — equivalently, ⋆ does not preserve any A₅-stable ℚ-lattice — and a fortiori it is non-integral on every A₅-stable ℤ-lattice. **\[PROVEN fully exactly in ℚ(√5) via a symbolic commutant (rank 34, nullity 2), with no kron/vec convention: T2-int, T2-dim, T2-exact, T2-comm, T2-obs.\]**  
*Proof.* W is ℚ-irreducible (a single Galois orbit under √5 ↦ −√5, which exchanges 3 and 3′); its endomorphism algebra is the field generated by the character, ℚ(χ₃) \= ℚ(φ) \= ℚ(√5), of degree 2\. A general rational endomorphism is pI \+ qs (p, q ∈ ℚ), acting as p ± q√5 on 3, 3′. Requiring ±1 (the eigenvalues of ⋆) forces p \= 0, q \= 1/√5 ∉ ℚ. If instead ⋆ preserved an A₅-stable ℚ-lattice, ker(⋆ − I) and ker(⋆ \+ I) would be 3-dimensional rational A₅-submodules, i.e. 3 and 3′ would each be defined over ℚ — impossible, since their characters are irrational.   
The numerical disc(A₄) \= 5 finding (⋆\_root \= (1/√5)·M in the A₄ root lattice) is **one concrete lattice manifestation** of this obstruction; the integer M is the generator s, with M² \= 5I. The integrality obstruction is exactly the icosahedral √5 / golden ratio.  
**General form (Galois-conjugate pairs).** The argument is not special to A₅. Let U, U^σ be a Galois-conjugate pair of absolutely irreducible G-modules whose common character field K \= ℚ(χ\_U) is a real quadratic field ℚ(√m) (m \> 0 squarefree), with σ the nontrivial element of Gal(K/ℚ) exchanging U and U^σ. Then End\_{ℚG}(U ⊕ U^σ) \= K \= ℚ(√m), generated over ℚ by an operator s — integral on a G-stable order — with s² \= mI and Tr s \= 0, and the duality involution ⋆ \= P\_U − P\_{U^σ} \= (1/√m)s requires the coefficient 1/√m ∉ ℚ. Hence ⋆ is never rational on a G-stable ℚ-form. The Z-Spin case is m \= 5 (G \= A₅), with disc(A₄) \= 5 as one realization; the same statement holds verbatim for any such pair, the coefficient 1/√m being the field-of-definition obstruction. This is the externally most transferable result of ZS-F35.  
**Interpretation (metric vs arithmetic).** The value ν\_s² \= 6 is the **Hilbert–Schmidt norm** relevant to the kinetic susceptibility (the quadratic form ĉ\_θ†G⁻¹ĉ\_θ). Flux quantization belongs **separately** to the integral cohomology (charge) lattice, which is metric-independent and which the Hodge involution **need not preserve**; T2 identifies precisely this metric–arithmetic mismatch for the A₄ realization. ν\_s² \= 6 is therefore a kinetic-norm statement, not a claim about the charge lattice, and is unaffected by the obstruction.  
---

## **§6. The single observable stiffness**

ZS-F34 carried three convention-dependent normalizations — Z\_match, V\_Σ, G\_s — only in the combination Z\_s^phys \= V\_Σ G\_s/(Z\_match g\_reg²). Define the **single observable kinetic stiffness**  
G̃\_s := V\_Σ G\_s / Z\_match, so that Z\_s^phys \= G̃\_s / g\_reg².  
The susceptibility depends on Z\_match, V\_Σ, G\_s only through G̃\_s; their separate values are pure convention. This removes the convention-dependent three-way split entirely, leaving one observable. **\[DERIVED.\]** It is a reparameterization, not a computation of G̃\_s.  
---

## **§7. The Canonical UV Normalization and C\_norm**

Two quantities remain, each a normalization rather than a derived number:

* G̃\_s (the single observable stiffness). Under the topological Kaloper–Sorbo/BF reading of the odd flux (ZS-F33), the kinetic normalization is taken canonical, G̃\_s \= 1\. The physical EFT Hessian is not computed. **\[ASSUMPTION S3.\]**  
* **c\_e \= 2π** (the membrane-charge coefficient, e₆ \= c\_e M\_UV²). Large-gauge (Dirac) quantization gives c\_e an O(1) constant; 2π is natural, exact determination pending. **\[HYPOTHESIS-strong, S4; ≈ 30%.\]**

**Canonical UV Normalization (C\_UV):** G̃\_s \= 1 and c\_e \= 2π.  
Define C\_norm \= G̃\_s⁻¹·(c\_e/2π)². Under C\_UV, **C\_norm \= 1 exactly** (with no residual Z\_match, the v1.2 inconsistency removed by folding Z\_match, V\_Σ, G\_s into G̃\_s). C\_norm \= 1 is the closure gate deferred to ZS-F36. **\[ASSUMPTION S5.\]**  
---

## **§8. The structural dimensionless factor**

Assembling §§2–7 with ĉ\_θ \= ⋆ (ν\_s² \= 6), Z\_s^phys \= G̃\_s/g\_reg², and e₆ \= c\_e M\_UV²,  
χ₋⁽ˢ⁾ \= e\_s² / (4π² Z\_s^phys) \= (ν\_s² g\_reg² / 4π²)·G̃\_s⁻¹·e₆² \= 6 g\_reg²·\[G̃\_s⁻¹ (c\_e/2π)²\]·M\_UV⁴,  
so that, with 6 g\_reg² \= 36 A/Q \= (dim Y)² A/Q,  
χ₋⁽ˢ⁾ \= (dim Y)² · (A/Q) · C\_norm · M\_UV⁴ \= (1260/4807) · C\_norm · M\_UV⁴, C\_norm \= G̃\_s⁻¹ (c\_e/2π)².  
The arithmetic identity 36 A/Q \= 1260/4807 is **PROVEN** (an exact rational identity in the locked inputs; **I1**). That this rational number is the **physical structural factor** is **DERIVED-CONDITIONAL** on ĉ\_θ \= ⋆ (the F34.BIV carrier reduction; §4.3). Under C\_UV, C\_norm \= 1, giving χ₋⁽ˢ⁾ \= (1260/4807) M\_UV⁴ ≈ 0.262 M\_UV⁴, but **C\_norm \= 1 is not established here** — it is the F36 gate. The structural factor — what F35 derives — is the dimensionless rational (dim Y)² A/Q.  
---

## **§9. The branch ratio is a regression, not independent evidence**

The single-mode value reproduces the corpus path-(c) benchmark χ\_83 \= 0.091847 e₆² via χ\_83/χ\_singlet \= 83/q\_s. **This is a tautology:** both numbers are q·g\_reg²/4π², so the ratio is 83/q\_s for **any** q\_s (16.6, 13.83, 11.86 at q\_s \= 5, 6, 7\) and tests nothing about the derived value. **\[IDENTITY I2.\]** It is a cross-version arithmetic regression, not independent evidence.  
---

## **§10. The two residuals**

What remains is **one dimensionless normalization gate (C\_norm) plus one irreducible dimensionful scale (M\_UV)**. M\_UV is the sole *dimensionful* residual, but not the sole unknown: C\_norm \= 1 is an undischarged dimensionless gate. By the Charge-Unit Obstruction (ZS-F33.8, PROVEN), M\_UV cannot be obtained from (A, Q) and flux integrality. **\[PROVEN-irreducible.\]** ZS-F36 inherits both: compute G̃\_s and c\_e (hence C\_norm) and fix M\_UV from one explicit UV completion.  
---

## **§11. Claim ledger**

| \# | Claim | Status | Confidence | Conditions |
| ----- | ----- | ----- | ----- | ----- |
| T1 | Multiplicity-Free Duality-Singlet theorem | PROVEN (Schur) | — | unitary ℂ, absolutely irreducible, d \= d, mult 1 |
| §2 | N\_eff \= 1 | DERIVED | 90% | exact-A₅ invariant-source branch |
| §4.1 | I\_h central inversion cannot swap 3↔3′ | PROVEN | — | none |
| §4.1 | physical realization of σ | OPEN | — | inherits F34 G-Outer-Physical |
| §4.2 | ⋆ unique traceless A₅-invariant on the carrier | PROVEN | — | rank-6 carrier (T1) |
| §4.2 | Lorentzian identities ⋆\_L² \= −I, J\_L \= −i⋆\_L, J\_L² \= I | PROVEN | — | none |
| §4.2 | Euclidean 3 ⊕ 3′ norm applies to the Lorentzian EFT | DERIVED-COND | 70% | complexification/Wick identification |
| §4.3 | ĉ\_θ \= ⋆ (Pontryagin action \+ T1) | DERIVED-COND | 70% | F34.BIV carrier reduction |
| §4.3 | ν\_s² \= 6 (Hilbert–Schmidt norm) | PROVEN (HS) | 75% (physical) | metric norm; source identification |
| T2 | ⋆ non-rational on every A₅-stable ℚ-form | PROVEN (exact) | — | none |
| §6 | G̃\_s the single observable stiffness | DERIVED | 90% | none |
| §8 | 36 A/Q \= 1260/4807 (arithmetic) | IDENTITY / PROVEN | — | none |
| §8 | 1260/4807 is the physical structural factor | DERIVED-COND | 70% | ĉ\_θ \= ⋆ |
| §8 | χ₋⁽ˢ⁾ \= (1260/4807) C\_norm M\_UV⁴ | DERIVED (factorization) | 90% | as a factorization |
| §7 | C\_norm \= 1 (absolute coefficient) | OPEN | — | C\_UV; F36 gate |
| §9 | branch ratio 83/q\_s | IDENTITY | — | tautological |
| §10 | M\_UV the sole dimensionful residual | PROVEN-irreducible | 90% | Charge-Unit Obstruction |

---

## **§12. Falsification gates**

* **F-F35.1.** If End(V₁₁) does not decompose as stated, the construction fails. *PASS (P1).*  
* **F-F35.2.** If U₊, U₋ are isomorphic, not absolutely irreducible, or unequal-dimensional, T1’s commutant is not two-dimensional. *T1 hypotheses stated.*  
* **F-F35.3.** If the carrier is not Λ²V₄ \= 3 ⊕ 3′ (F34.BIV), §4.2 is void.  
* **F-F35.4.** If the source is not the bivector Pontryagin coupling (ĉ\_θ ≠ ⋆), ν\_s² changes. *Principal risk to §4.3.*  
* **F-F35.5.** If C\_norm ≠ 1 (G̃\_s ≠ 1 or c\_e ≠ 2π), the absolute coefficient differs by C\_norm; the structural factor survives. *F36 gate.*  
* **F-F35.6.** If ⋆ were rational on some A₅-stable ℚ-form, T2 (hence the metric–arithmetic interpretation) would fail. *Excluded by the character-field proof.*  
* **F-F35.7.** Any claim to fix the absolute χ₋ without M\_UV from UV data is void. *M\_UV → F36.*

---

## **§13. Anti-numerology**

The structural factor is (dim Y)² A/Q \= 36 × 35/(437 × 11\) \= 1260/4807, all factors pre-existing locked inputs. The only integer beyond (A, Q) is ν\_s² \= 2d \= 6, fixed by T1 (the rank-6 carrier, d \= 3\) — not scanned. No coefficient was fitted. We **decline** to count the branch-ratio match (§9) as evidence (tautological). The disc-5 obstruction (T2) shows ν\_s² \= 6 is a kinetic-norm statement, not fitted arithmetic. The *structural factor* is forced; the *absolute value* carries the unproven C\_norm and the UV scale M\_UV and is not claimed.  
---

## **§14. Cross-version safety**

* (A, Q, dim Z) \= (35/437, 11, 2), (Z, X, Y) \= (2, 3, 6), g\_reg² \= 210/4807, ω \= 2.2592495540, z\* \= 0.43828 \+ 0.36059 i: unchanged.  
* ZS-F34’s master form is not modified; v1.4 supplies a factorized value for its dimensionless content via G̃\_s and inherits its OPEN gate G-Outer-Physical.  
* ZS-F33’s Charge-Unit Obstruction is preserved and used (§10).  
* ZS-A19’s O-A19.2 embedding question is bypassed (not closed) by the coupling route (§4.3); the unconstrained non-invariance is a NO-GO (§4.4).  
* Retained from v1.0–v1.3: the single-mode reduction, embedding independence, Schur O(ε²) stability. **Superseded:** the v1.1 σ-parity closure and “exact absolute coefficient”; the v1.2 C\_norm definition (corrected via G̃\_s in v1.3); the v1.3 “machine-verified across” wording for T1 and its over-strong T2 universal claim; and the v1.4 verification’s kron/vec transpose in the T2 generator recovery (fixed in v1.5 by a symbolic commutant, with \[s, R(g)\] \= 0 now checked for all 60 g).

---

## **§15. Verification**

zs\_f35\_verify\_v1\_5.py (NumPy \+ SymPy, seed 437\) is the single source of truth (resolving the v1.3 verify/probe S3 inconsistency; T2 now fully exact via a symbolic commutant), in three honest classes:

* **PROVEN/COMPUTED (23/23 PASS):** End(V₁₁) decomposition (P1); arithmetic split (P2a); the character check that Λ²₊/Λ²₋ ARE 3/3′ via χ(5A) \= φ̄/φ (P3); the swap R(t)⋆ \= −⋆R(t) with non-centrality (P4); commutant dimension 2 (P5); block-preservation (P6); the connected uniqueness ⋆ \= span of the traceless commutant (P7, residual 10⁻¹⁶); ⋆ unimodular, det \= −1 (P8); ν\_s² \= 6 as a Hilbert–Schmidt norm (P9); the NO-GO contrast (P10); the **general theorem T1** illustrated on A₅/S₅/S₃ with carrier-dependence shown explicitly and the susceptibility refinement (T1-A5, T1-S5, T1-S3, T1-carrier, T1-chi); the **Lorentzian bridge** ⋆\_E² \= \+I, ⋆\_L² \= −I, J\_L \= −i⋆\_L with J\_L² \= I (L1, L2, L3); and the **FULLY EXACT character-field obstruction T2** in ℚ(√5), computed via a symbolic commutant (no kron/vec convention, fixing the v1.4 transpose error): integral A₅ action and disc(A₄) \= 5 (T2-int), exact rank 34 / nullity 2 (T2-dim), integral s with s² \= 5I and det \= −125 (T2-exact), \[s, R(g)\] \= 0 for all 60 g ∈ A₅ (T2-comm — the check that catches the transpose), and ⋆ \= (1/√5)s non-rational (T2-obs).  
* **IDENTITY/REGRESSION (4/4 PASS):** 36 A/Q \= 1260/4807 (I1); the branch ratio shown tautological (I2); the corrected C\_norm (I3); the ρ\_Λ,Z regression (I4).  
* **ASSUMPTION-CONSISTENCY (6 tracked, not derivations):** the physical split/N\_eff inheritance (P2b); ĉ\_θ \= ⋆ (S1); ν\_s² \= 6 as a kinetic HS-norm, distinct from the charge lattice (S2); G̃\_s \= 1 (S3); c\_e \= 2π (S4); C\_norm \= 1 (S5).

---

## **§16. Acknowledgements & Code Availability**

This work consolidates internal Z-Spin Collaboration deep-exploration notes following ZS-F34 v1.8, incorporating five detailed peer reviews (v1.0 through v1.4). The verification script zs\_f35\_verify\_v1\_5.py (NumPy \+ SymPy) reproduces all PROVEN and IDENTITY checks, including the general theorem T1, the Lorentzian bridge, and the fully exact character-field obstruction T2; the standalone zs\_f35\_T2\_exact.py reproduces the exact ℚ(√5) computation (symbolic commutant; rank 34, s² \= 5I, \[s, R(g)\] \= 0 for all 60 g ∈ A₅). This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility for all content, including the corrections recorded here.  
---

## **§17. Appendix A — Deep-exploration (issue-tree) record**

**Step 0 (long list).** Singlet-selection principles: (1) I\_h geometric; (2) seam involution J; (3) physical σ (S₅); (4) Pontryagin/θ; (5) ⋆ as the unique invariant complex structure; (6) parent-Hessian minimal mode; (7) tracelessness \+ A₅-invariance on the carrier. Generalization/strengthening: (8) group-independent theorem; (9) integral-lattice status of ν\_s²; (10) action-level source; (11) Lorentzian bridge; (12) exact field-of-definition obstruction.  
**Step 1 (MECE).** Dropped (2) (distinct ℤ₂, conflation rejected ZS-F12) and (6) (circular). Retained I1–I4 for selection; promoted (8) → T1, (10) → §4.3, (11) → §4.2, (9)+(12) → T2.  
**Step 2–3 (tree \+ status).** I1 \= NO-GO \[PROVEN\]; I2 \= OPEN \[G-Outer-Physical\]; I4 \= PROVEN \[T1\]; I3 \= DERIVED-CONDITIONAL \[§4.3\]. T1 PROVEN (Schur) \+ illustrated on three groups; the Lorentzian bridge PROVEN (L1–L3); T2 PROVEN exactly (the character field ℚ(√5) obstructs a rational ⋆).  
**Step 4 (convergence).** The number of OPEN nodes is one (I2, physical σ), which §§4.2–4.3 bypass. T1, T2, and the Lorentzian bridge are closed results. Converged.  
**Step 5 (value).** The Z-Spin singlet computation is a corollary of a general theorem (T1); the lattice question becomes a genuine field-of-definition theorem (T2, exact), the most original element; the source is derived at action level (§4.3); the Euclidean–Lorentzian gap is bridged (§4.2). External value rises from an internal debt-closure to general statements about finite-symmetry top-form susceptibilities and the rational structure of duality involutions.  
---

## **§18. References**

1. J.-M. Bismut, H. Gillet, C. Soulé, *Analytic torsion and holomorphic determinant bundles I–III*, Commun. Math. Phys. **115** (1988) 49, 79, 301\.  
2. D. Quillen, *Determinants of Cauchy–Riemann operators over a Riemann surface*, Funct. Anal. Appl. **19** (1985) 31\.  
3. R. Bousso, J. Polchinski, *Quantization of four-form fluxes and dynamical neutralization of the cosmological constant*, JHEP **06** (2000) 006, hep-th/0004134.  
4. N. Kaloper, L. Sorbo, *Of pNGB quintessence and the cosmological constant*, Phys. Rev. Lett. **102** (2009) 121301\.  
5. N. Kaloper, A. Padilla, *Sequestering the standard model vacuum energy*, Phys. Rev. Lett. **112** (2014) 091304\.  
6. J.-P. Serre, *Linear Representations of Finite Groups*, GTM **42**, Springer (1977). \[Schur’s lemma; character fields; Galois action on characters\]  
7. W. Fulton, J. Harris, *Representation Theory: A First Course*, GTM **129**, Springer (1991).  
8. J. H. Conway, N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, 3rd ed., Springer (1999). \[A₄ root lattice, disc 5\]  
9. I. Reiner, *Maximal Orders*, Academic Press (1975). \[endomorphism algebras / fields of definition\]  
10. Planck Collaboration, *Planck 2018 results VI: Cosmological parameters*, arXiv:1807.06209.  
11. ZS-F33, *The Compact Three-Form and the Charge-Unit Obstruction* (Z-Spin corpus).  
12. ZS-F34 v1.8, *The Six-Dimensional Charge Unit of the Z-Spin Three-Form* (Z-Spin corpus).  
13. ZS-A19 v3.1, *Geometric Dark Matter and the Boundary-Rank Trace* (Z-Spin corpus).  
14. ZS-M6, *The Hodge–Dirac Operator and the Internal Spectrum* (Z-Spin corpus).

---

## **§19. Version History**

* **v1.0 (June 2026).** Initial release; parent-Hessian reduction (a reduction, not a closure). 35/35.  
* **v1.1 (June 2026).** Closure-claim revision on a flawed I\_h-equivariance step. 34/34.  
* **v1.2 (June 2026).** Honest-closure revision (first review): corrected I\_h ≠ S₅, carrier-uniqueness \+ Pontryagin, C\_UV bundle, factorization, branch-ratio tautology, three verification classes (10+4 PASS).  
* **v1.3 (June 2026).** Surgical corrections plus generalization (second review): corrected C\_norm via G̃\_s; promoted to the general theorem T1; action-level ĉ\_θ \= ⋆; the disc-5 lattice observation; status refinements; verification fixes (17+4 PASS).  
* **v1.4 (June 2026).** *Mathematical-scope and code cleanup (third review).* (1) **Restricted T1** to a finite-dimensional unitary complex representation with U₊, U₋ non-isomorphic *absolutely irreducible* of equal complex dimension d, so End\_G(U±) \= ℂ exactly; the norm is the *Hilbert–Schmidt* norm relative to the invariant Hermitian structure; the susceptibility statement (iv) is refined to ĉ\_θ†G⁻¹ĉ\_θ \= |λ|²·(2d)/G\_J, with the physical prefactor assembled only in the Z-Spin corollary. (2) **Resolved the verify/probe inconsistency**: a single verification script, with the carrier-dependence of J² \= I exhibited explicitly (replacing v1.3’s declarative T1-rob), and the T1 wording changed from “machine-verified across” to “follows from Schur’s lemma; illustrated for three groups.” (3) **Upgraded T2 to an exact universal theorem**: End\_{ℚA₅}(3 ⊕ 3′) \= ℚ(√5), the integral generator s with s² \= 5I, and ⋆ \= (1/√5)s non-rational on every A₅-stable ℚ-form (proven exactly in ℚ(√5) via sympy; disc(A₄) \= 5 is one lattice instance), replacing v1.3’s over-strong “M₁₁(ℤ) provably obstructed” with a precise field-of-definition obstruction. (4) **Added the Lorentzian bridge** J\_L \= −i⋆\_L (J\_L² \= I), reinstating the v1.2 signature caveat the v1.3 draft dropped. (5) **Corrected the metric/flux-quantization framing**: ν\_s² \= 6 is the kinetic Hilbert–Schmidt norm; flux quantization is a separate integral-cohomology question that the Hodge involution need not respect — T2 is exactly this mismatch. (6) **Abstract** rephrased from “close the dimensionless content” to “isolate and derive the structural dimensionless factor, leaving one UV-normalization gate,” and standalone normalization equations cleaned. Verification: 22 PROVEN \+ 4 IDENTITY (NumPy \+ SymPy).  
* **v1.5 (June 2026, terminal).** *Exact-verification and notation cleanup (fourth review).* (1) **Fixed the T2 verification transpose**: v1.4 recovered the commutant generator from a Kronecker system with NumPy’s row-major reshape, while the vec identity is column-major, so the recovered matrix was the transpose (the theorem was unaffected, and s² \= 5I passed because it is transpose-invariant, but \[s, R(g)\] \= 0 was never checked). v1.5 builds the commutant **symbolically** (M·R − R·M with symbolic M), removing the kron/vec convention entirely. (2) **Made T2 fully exact**: the commutant dimension is now an exact sympy rank (rank 34, nullity 2), and the integral generator satisfies, exactly, s² \= 5I, Tr s \= 0, det s \= −125, and \[s, R(g)\] \= 0 for all 60 g ∈ A₅ (T2-comm) — the verification now matches the analytic proof. (3) **Added the general Galois-conjugate-pair form** of T2: for any such pair with real quadratic character field ℚ(√m), the duality involution is (1/√m)s with s² \= mI, never rational; A₅ (m \= 5\) is the instance. (4) **Fixed T1 notation**: replaced the inaccurate G|\_{V^G} with the order-parameter metric G satisfying G(J, J) \= G\_J‖J‖²\_HS; and replaced “the identity spans the trace-carrying invariants” with the precise statement that the trace map on the 2-dimensional commutant has 1-dimensional kernel ℂ(P₊ − P₋), the identity providing a canonical complementary line. (5) **Split the Lorentzian status**: the algebraic identities (⋆\_L² \= −I, J\_L² \= I) are PROVEN, while applying the Euclidean 3 ⊕ 3′ norm to the Lorentzian EFT is DERIVED-CONDITIONAL on the Wick identification. (6) **Fixed the remaining §4.2 Markdown bold** on the J\_L span (an underscore-adjacent-to-symbol that broke pandoc emphasis). Verification: 23 PROVEN \+ 4 IDENTITY (NumPy \+ SymPy). (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new fitted parameter. **This is the terminal version of ZS-F35**; the absolute UV normalization (G̃\_s, c\_e, M\_UV) is the task of ZS-F36.