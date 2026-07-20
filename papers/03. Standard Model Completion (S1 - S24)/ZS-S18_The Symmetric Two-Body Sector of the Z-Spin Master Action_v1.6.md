# **ZS-S18**

# **The Symmetric Two-Body Sector of the Z-Spin Master Action**

**A Closed Form for the Symmetric Cup Product, the Exact Harmonic Anchoring Identity, a Wilson-Holonomy Audit of the Discrete Action, and a Closed Form for the Leading Two-Body Exchange**

---

**Author:** Kenny Kang **Affiliation:** Z-Spin Cosmology Collaboration **Date:** March 2026 (internal draft) — **revised July 2026** **Theme / Paper Code:** Standard Model — **ZS-S18** **Version:** v1.6 (final) **Locked inputs:** **A** \= 35/437, **Q** \= 11, dim(**Z**) \= 2, v \= 245.93 GeV, λ₁ \= 1.2428416164, λ\_h \= 7.5210904061, α\_s(M\_Z) \= 11/93 **Companion:** zs\_s18\_verify\_v1\_6.py — one self-contained file. No data assets, no JSON file, no auxiliary scripts. **Supersedes:** v1.0 – v1.5.

---

**Verification: 74/74 computed & proof checks PASS | 5 OPEN gates \+ 2 EXTERNAL confrontations, NOT counted | Zero New Geometric Parameters | Running-Coupling Matching Gate OPEN**

*Runtime **6 s** (v1.5: 70 s here, and unfinished at 600 s in the reviewer's environment). Verified in an empty directory containing only the script: exit 0, no files written.*

environment: python 3.12.3, numpy 2.4.4, scipy 1.17.1, x86\_64

SHA256(result block, canonically rounded to 10 significant digits)  
   \= ccc76829a4fcf91dbd863ab33c39d0f94a580deb155d4a94eb82b76ce579aaea

---

## §0. Abstract

ZS-S17 closed the antisymmetric summand of T₁ ⊗ T₁ and isolated the remaining physics to the symmetric summand, where the glueball states live. This paper executes that sector, audits its own dynamical reduction against the Wilson holonomy, and states with precision what is and is not thereby established.

**The kinematic sector is closed.** The symmetric part of the cup product has a closed form with no basepoint (**Lemma S18.A**); Sym²(T₁) closes on exactly six dimensions, the A ⊕ H isotype; the pairing with the harmonic 2-form is the exact identity ⟨h, Θ(a\_α,a\_β)⟩ \= δ\_{αβ}(λ₁−2)/λ₁, so the traceless tensor channel has identically zero harmonic overlap (**Theorem S18.4**); and the **parity dictionary** (**Theorem S18.8**) fixes A → 0⁺⁺, H → 2⁺⁺ unconditionally.

**The gauge-covariant cubic bridge is closed.** The quadratic Wilson term reproduces ½Σ\_f(δA)² exactly and the **cubic** term is exactly the cup-product form with the Baker–Campbell–Hausdorff coefficient **μ \= −1/2**. **Theorem S18.9**: the *fully polarised* cubic vertex couples two external T₁(λ₁) legs into T₁(λ₁) ⊕ T₁(λ\_h) and nowhere else among the 31 physical modes, relative leakage 1.4 × 10⁻¹⁵, at all six basepoints. The physical vertex is the totally symmetrised trilinear, whose mode part is totally antisymmetric (residual exactly 0); its λ\_h block gives **c\_{h,pol}² \= 0.0012658090**, *not* the raw cup projection 0.0095045494 — **ZS-S17's 7.1395 % power split is a projection, not a coupling** (v1.5 correction, retained).

**The leading exchange now has a closed form (new in v1.6).** The two closed channels contribute **additively with the same universal coefficient**, because the virtual eigenvalue cancels: the squared vertex supplies λ\_r, the oscillator normalisation and the energy denominator supply 1/ω\_r², and λ\_r/ω\_r² \= 1\. Hence

$$\\boxed{\\ G\_{\\rm exch} ;=; \\frac{9}{4}\\sqrt{\\lambda\_1}\\sum\_r c\_{r,\\rm pol}^2 ;=; \\frac{9}{4}\\sqrt{\\lambda\_1}\\big(c\_1^2+c\_{h,\\rm pol}^2\\big) ;=; 0.3132643168\\ }$$

matching the brute-force Fock-space computation to **7 × 10⁻¹⁶**, and the λ\_h channel alone matching (9/4)√λ₁c\_{h,pol}² \= 0.0031751087 to thirteen digits for SU(2) and SU(3). v1.5 declared this quantity to have no closed form; that is **corrected**, and **Proposition S18.6A′ is promoted to Theorem S18.6A′**.

**A ledger value is retracted.** v1.0 – v1.5 recorded the two-T₁ content of the un-averaged antisymmetric cup as 61.9257 %. Because λ₁ is three-fold degenerate, that number depends on the arbitrary O(3) rotation returned by the eigensolver — random bases give 63.6 %, 74.6 %, 84.3 %, and the reviewer's environment gave 72.4 %, *failing the check*. It is replaced by the **basis-invariant trace ratio**

$$\\frac{\\operatorname{Tr}\!\\big(M P\_{2T\_1} M^{\\mathsf T}\\big)}{\\operatorname{Tr}\!\\big(M M^{\\mathsf T}\\big)} \= 71.0350815252,%,$$

verified stable to 3 × 10⁻¹⁶ under random rotations of the degenerate eigenbasis.

**The result, in three layers.**

$$\\textbf{Thm S18.6A: } G\_{\\rm exch}^{(1)} \= \\tfrac94 c\_1^2\\sqrt{\\lambda\_1} \= 0.3100892081 \\qquad \\textbf{Thm S18.6A}': G\_{\\rm exch} \= \\tfrac94\\sqrt{\\lambda\_1}(c\_1^2+c\_{h,\\rm pol}^2) \= 0.3132643168$$ $$\\textbf{Prop S18.6B: } s(N)/N \\simeq \-0.0120898 \- 0.0043825/N^2 \\qquad \\textbf{Cor S18.6C: } G\_\\infty \\simeq 0.298805,; a\_{\\rm geom} \\simeq \-0.005241$$

with λ\_t \= 5.539 ± 0.11 against ZS-S1's λ\_t(M\_Z) \= 4.459. **Only the seagull remains numerical**; the entire exchange sector is now analytic.

**Positioning.** *The kinematic sector and the gauge-covariant cubic action bridge are closed, and the leading exchange has an exact closed form; the Wilson quartic is extracted to machine precision but not derived; the non-perturbative glueball spectrum bridge remains open.*

---

## §0.1 Retractions and Corrections

**RETRACTED (v1.3), from v1.2 §4.5 Theorem S18.6.** **G** \= 1.1025394066 with a \= b \= 0 exactly. Two errors: BCH gives **μ \= −1/2**, not \+1, and both O(g²) contributions are quadratic in μ; and the quartic vertex is not ½Σ\_a\[f^{abc}(A^b⌣A^c)\]².

**CORRECTED (v1.5), the λ\_h vertex.** The cubic Hamiltonian is a cubic *form*, so only the totally symmetrised tensor matters: $$T\_{r\\alpha\\beta} \= \\tfrac13\\big\[R\_{r\\alpha\\beta} \+ R\_{\\alpha\\beta r} \+ R\_{\\beta r\\alpha}\\big\], \\qquad R\_{r\\alpha\\beta} := \\langle u\_r,\\mathbf{B\_{anti}}(a\_\\alpha,a\_\\beta)\\rangle,$$ giving c\_{h,pol}² \= 0.0012658090 in place of the raw 0.0095045494. The λ₁ block is unchanged, since for three λ₁ legs R is already ε-structured. Discipline (x): **a projection is not a coupling.**

**CORRECTED (v1.6), "no closed form".** v1.5's Proposition S18.6A′ asserted that the two-channel exchange had no closed form. It does — see §5.4 — and the failure was to notice that the same 9/4 appears for every channel. The lesson is narrower than the previous two but worth recording: *having found that a previously-assumed closed form was wrong, do not conclude that no closed form exists.* A retraction is not a licence to stop looking.

**RETRACTED (v1.6), the ledger value 61.9257 %.** Basis-dependent; see §3.5 and Check 25\.

---

## Epistemic Status Legend

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Exact identity or theorem; algebraic proof, verified on exact data. |
| **CERTIFIED** | Structurally forced by representation theory, confirmed numerically, resting on floating-point eigendecomposition and a tolerance. |
| **DERIVED** | Follows from PROVEN/CERTIFIED inputs plus the Z-Spin action; no new parameters. |
| **DERIVED-PERTURBATIVE-CONDITIONAL** | DERIVED within a named perturbative order, active-space truncation and gauge-fixing approximation, all registered as open gates. |
| **COMPUTED** | Numerical result, conditional on floating-point evaluation. |
| **COMPUTED-PERTURBATIVE-CONDITIONAL** | A numerical extraction inside the same three approximations; no closed form claimed. |
| **COMPUTED-EXTRAPOLATED** | Obtained by fitting computed values and extrapolating; the fit form is part of the claim. |
| **CORRECTED** | Previously asserted; fixed here, with the error identified. |
| **RETRACTED** | A headline or ledger claim of an earlier version, withdrawn. |
| **CLOSED-NEGATIVE** | Settled, and the route fails. |
| **EXTERNAL-CONFRONTATION** | A comparison with data or another corpus paper. Printed, not counted. |
| **NON-CLAIM** | Explicitly outside scope. |
| **OPEN** | Well-posed, not settled; pre-registered and excluded from the pass ratio. |
| **LOCKED** | Core constant fixed upstream. |

**Accounting rule.** 74/74 on computed and proof checks. Five gates OPEN — F-S18.4, F-S18.10, F-S18.13, F-S18.15, F-S18.16 — and two confrontations EXTERNAL. None of the seven is counted.

---

## §1. Introduction

### 1.1 The arc across seven versions

| version | what it asked | what it got |
| ----- | ----- | ----- |
| v1.0 | Is the symmetric channel diffuse? | No — it closes on 6 dimensions |
| v1.1 | Can the equivariance be proved? | Lemma S18.A; an exact harmonic identity |
| v1.2 | What *is* the two-body operator? | A Feshbach effective Hamiltonian |
| v1.3 | Is the reduction actually Yang–Mills? | Cubic yes, quartic no — **retraction** |
| v1.4 | Is the claim reproducible and scoped? | One file; three layers; two new gates |
| v1.5 | Is the vertex the one in the Hamiltonian? | No — λ\_h **corrected** |
| **v1.6** | **Does the verifier actually run, and is the closed form really absent?** | **No, and no — both fixed** |

### 1.2 Method discipline

(i) canonical normalization fixed before the action is touched; (ii) projected vs full curvature, alternating vs general bilinear, search vs global count kept distinct; (iii) any derivation using the ZS-S7 hyperfine ansatz to produce the ¼ is circular and refused; (iv) a refutation is reported as a refutation; (v) a small residual is diagnosed to its source before being tolerated; (vi) a status is not claimed above what the evidence supports; (vii) N-dependence is derived from the colour algebra before any lattice number is consulted; (viii) a discrete action is not trusted until audited against a manifestly gauge-covariant construction; (ix) the companion code **is** the claim; (x) a projection is not a coupling; (xi) *(v1.6, new)* **no quantity computed in a degenerate eigenbasis enters the ledger unless it is invariant under rotations of that eigenspace.** The 61.9257 % of §3.5 passed six versions of review because it was reproducible *within one BLAS implementation*; it failed the moment an independent reviewer ran it. Every ledger number must now be either exactly invariant or explicitly labelled a convention-dependent diagnostic.

---

## §2. Locked Inputs and Canonical Normalization

*Table 2.1. Zero new geometric parameters.*

| \# | Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- | ----- |
| L1 | **A** | 35/437 \= 0.080091533 | ZS-F2 §5 | LOCKED |
| L2 | **Q** | 11 | ZS-F5 | LOCKED |
| L3 | dim(**Z**) | 2 | ZS-F5, ZS-M3 | PROVEN |
| L4 | v | 245.93 GeV | ZS-S4 §6.12 | DERIVED |
| L5 | TI complex | V \= 60, E \= 90, F \= 32 | ZS-F5, ZS-M6 | PROVEN |
| L6 | λ₁ | 1.2428416164 | ZS-S7 §2.2 | CERTIFIED |
| L7 | λ\_h | 7.5210904061 | ZS-S17 §1 | CERTIFIED |
| L8 | m(0⁺⁺) \= v**A**/**Q** | 1.7906 GeV | ZS-S7 §6 | DERIVED-COND |
| L9 | Λ\_QCD | 264.1 MeV | ZS-S7 §5 | DERIVED-COND |
| L10 | T₁ ⊗ T₁ \= A\_g ⊕ T₁ ⊕ H | — | ZS-S17 §0 | PROVEN |
| L11 | **I\_Z** \= λ₁ **S₁·S₂** | — | ZS-S17 §3 | DERIVED |
| L12 | α\_s(M\_Z) \= 11/93 | 0.118280 | ZS-S1 | DERIVED |
| L13 | anti-numerology band | 89/3600 \= 2.4722 % | ZS-S17 §4 | COMPUTED |
| L14 | Σδ\_v \= 2πχ \= 4π | — | ZS-S7 §3 | PROVEN |

**Canonical normalization.** a\_α \= B₂ᵀu\_α/λ₁ gives ⟨a\_α,a\_β⟩ \= δ\_{αβ}/λ₁ (residual 1.8 × 10⁻¹⁵) and **δa\_α \= u\_α**. With **Q** \= q/√λ₁,

$$\\boxed{\\ \\Omega\_0 \= \\sqrt{\\lambda\_1} \= 1.1148280659\\ }$$

**\[DERIVED — Checks 12, 13\]**

---

## §3. Part I — Structure of the Symmetric Channel

**3.1 Signed I\_h action.** P\_F(g)B₂ \= B₂P\_E(g) and \[P\_F(g), L₂\] \= 0 for all 120 elements, residual exactly 0; the face sign equals det(g). **\[PROVEN — Checks 7, 8\]**

**3.2 Isotype decomposition.** Ω² \= 2A\_u ⊕ 2T₁g ⊕ 2T₂g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u over the nine levels {0, 1.242842, 5−√3, 4.844366, 6, 5+√3, 7.521090, 8, 8.391702}. **\[CERTIFIED — Checks 9, 11\]**

**Correction S18.C1 \[CORRECTED\].** ZS-S7 §2.2's "all ten irreps once" is false: six distinct irreps, four with multiplicity two. **Load-bearing: none.** **\[Check 10\]**

**3.3 Lemma S18.A.** For 1-cochains x, y and any face f,

$$\\big(x\\smile y \+ y\\smile x\\big)(f) \= (\\delta x)(f)(\\delta y)(f) \- \\sum\_{t\\in\\partial f} x(t)y(t) \=: \\Theta(x,y)(f).$$

*Proof.* With e\_j \= x(v\_j→v\_{j+1}), f\_j \= y(v\_j→v\_{j+1}) mod n, put t \= b+k and b \= t+r (r \= 1,…,n−1), enumerating every b ≠ t once; the inner bracket becomes Σ\_{u=r}^{n−1}e\_{t+u}, and summing over r gives (1/n)Σ\_t f\_tΣ\_u u,e\_{t+u}. In the mirror term substitute t → t+u, u → n−u, so the weight becomes n−u. The weights sum to n, giving **B\_sym**(x,y)(f) \= Σ\_t f\_t(E\_x − e\_t) with E\_x \= (δx)(f). **\[PROVEN — Checks 41, 42\]**

Corollaries: **B\_sym** is exactly basepoint-free; **B\_anti** is exactly odd under face-orientation reversal; Θ(a\_α,a\_β) \= u\_αu\_β − Σ\_{∂f}a\_αa\_β.

**3.4 Theorem S18.1 (equivariance twist).** For proper g both channels are equivariant (4.2 × 10⁻¹⁶); for improper g, **B\_sym** carries the det(g) twist and **B\_anti** is orientation-blind. **\[PROVEN — Checks 21–23\]** The v1.0 residual 7.45 × 10⁻¹⁰ was the floating-point determinant (worst −0.999999999254644).

**3.5 Theorem S18.2 (basepoint dichotomy) — ledger value corrected in v1.6.** **B\_sym** is exactly basepoint-free (2.08 × 10⁻¹⁷). **B\_anti** is not, and without averaging the raw map is not closed on the two-T₁ space.

**RETRACTED ledger value.** v1.0 – v1.5 quoted "61.9257 % two-T₁ content" for the pair (a₀,a₁). Since λ₁ is three-fold degenerate, the eigensolver returns an arbitrary element of O(3) acting on the T₁ basis, and the *averaged* **B\_anti** is equivariant while the *raw* one is not — so this ratio is not a basis-invariant quantity. Random rotations give 63.6 %, 74.6 %, 76.5 %, 84.3 %; an independent reviewer's environment returned 72.4 %, failing the check. The number was a diagnostic of one LAPACK output, not a property of the geometry.

**Replacement, basis-invariant.** With M : Λ²T₁ → Ω² the raw single-basepoint map and P the projector on T₁(λ₁) ⊕ T₁(λ\_h), $$\\frac{\\operatorname{Tr}(MPM^{\\mathsf T})}{\\operatorname{Tr}(MM^{\\mathsf T})} \= \\mathbf{71.0350815252,%},$$ invariant because Λ²R is orthogonal for R ∈ O(3). Measured drift over random eigenbases: **3.3 × 10⁻¹⁶**. **\[Check 25\]** The qualitative content — the raw map leaks about 29 % out of the two-T₁ space, so basepoint averaging is *not* optional for the raw bilinear — is unchanged, and is in any case superseded by Theorem S18.9, which shows the *physical* vertex needs no averaging at all.

**3.6 Theorem S18.3.** The Sym²(T₁) image is exactly 6-dimensional and exactly the A\_u ⊕ H\_u isotype; leakage 4.80 × 10⁻²⁹. **\[CERTIFIED — Checks 16–19\]** ZS-S17's 29.54 % was measured against the wrong reference space **\[CORRECTED, S18.C2\]**.

**3.7 Theorem S18.4 (harmonic anchoring).** ⟨h, Θ(a\_α,a\_β)⟩ \= δ\_{αβ}(λ₁−2)/λ₁ \= −0.6092155054875·δ\_{αβ}.

*Proof.* By Lemma S18.A the pairing is Σ\_f u\_αu\_β − Σ\_fΣ\_{t∈∂f}a\_αa\_β \= δ\_{αβ} − 2δ\_{αβ}/λ₁, since every edge lies in exactly two faces. **\[PROVEN — Checks 46, 47\]**

| channel | support | share |
| :---- | :---- | :---- |
| **A** → |0⁺⁺⟩ | λ \= 0 / λ \= 8 | **85.5169968971 %** / 14.4830031029 % |
| **H** → |2⁺⁺⟩ | λ \= 5−√3 / λ \= 5+√3 | **96.9178108 %** / 3.0821892 % |
| **H** → |2⁺⁺⟩ | λ \= 0 | **exactly 0** |

Closed form: share\_{λ=0} \= (λ₁−2)²/(32λ₁²‖ψ\_A‖²) \= 0.855169968971 **\[Check 48\]**. This is a statement about state-space overlap, not protection of a mass eigenvalue; it *explains* ZS-S7's gate F-S7.5.

**3.8 Theorem S18.8 (parity dictionary).** P\_F^{unsigned}(g) \= det(g)P\_F^{signed}(g), so the Sym² image is **A\_g ⊕ H\_g** physically. With C \= \+ from δ^{ab}, A → 0⁺⁺ and H → 2⁺⁺, the 5-plet being exactly ℓ \= 2\. **\[CERTIFIED — Checks 70, 71, 72\]**

**3.9 Status.** Four v1.1 statements resting on floating-point eigendecomposition are **CERTIFIED**, not PROVEN. Check 39 is renamed *locked-input consistency*.

---

## §4. Part II — Gate A: the Wilson-Holonomy Audit

### 4.1 Construction and extraction

$$V(g) ;=; \\frac{2}{g^2}\\sum\_{f}\\Big\[N \- \\mathrm{Re},\\mathrm{Tr},U\_f\\Big\] ;=; \\tfrac12\\sum\_f\\big(B^a\_f\\big)^2 \+ \\cdots$$

**Contour extraction.** Define the entire continuation W(g) \= Σ\_f\[N − ½(TrU\_f(g) \+ TrŪ\_f(g))\] with Ū\_f the reverse-ordered product of exp(−igA\_e); for real g this equals Σ\_f\[N − ReTrU\_f\], and both terms are entire. The g² coefficient of V is the g⁴ coefficient of 2W, obtained on |g| \= r by

$$V\_2 \= \\frac{2}{M}\\sum\_{k=0}^{M-1}\\frac{W\!\\left(re^{2\\pi i k/M}\\right)e^{-8\\pi i k/M}}{r^{4}}.$$

*Table 4.1. Stability across six independent contour choices (SU(2), displayed field).* **\[Check 74\]**

| (r, M) | (0.3, 16\) | (0.4, 16\) | (0.5, 16\) | (0.6, 24\) | (0.8, 20\) | (0.5, 32\) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| V₂ | 0.0283516667398407 | …7396910 | …7396910 | …7396952 | …7396829 | …7397047 |

Spread **1.6 × 10⁻¹³**, against 0.028351666835 from v1.4's degree-7 least-squares fit.

**Terminology \[CORRECTED from v1.5\].** v1.5 called this "exact". It is not: a finite-node contour and floating-point exponentials are used. The correct description is **a machine-precision numerical extraction**. An *exact* quartic requires the analytic Magnus evaluation of Tr(Ω₂² \+ 2Ω₁Ω₃ \+ Ω₁⁴/12), which remains ZS-S19 work.

### 4.2 Gate A(i) — the quadratic term is exact

V₀^Wilson \= 2.0948528041 vs ½Σ\_f(δA)² \= 2.0948528118. Ω₀ \= √λ₁ stands. **\[CERTIFIED — Check 55\]**

### 4.3 Gate A(ii) — the cubic term is exact, with μ \= −1/2

BCH gives log∏e^{X\_k} \= ΣX\_k \+ ½Σ\_{j\<k}\[X\_j,X\_k\] \+ …, so with X\_k \= igA\_k^aT^a,

$$B^a ;=; (\\delta A)^a ;-; \\frac{g}{2},f^{abc}\\big(A^b\\smile A^c\\big)(f),$$

because Σ\_{j\<k}A^b\_jA^c\_k around the boundary cycle *is* the single-basepoint cup product. Measured: μ \= −0.5000119 (SU(2)), −0.4999990 (SU(3)); basepoint spread \< 10⁻¹⁰. **\[CERTIFIED — Check 56\]**

### 4.4 Gate A(iii) — the quartic is NOT the square of the cup curvature

Across two groups, two random fields and two basepoint conventions the ratio (Wilson quartic)/(naive μ²·cup²) spans **−0.083 to \+0.389, including a sign change** — not a rescaling, and not a universal constant (**NC-S18.12**). **\[Checks 57, 67\]** Two omitted effects contribute at the same order: the third-order BCH term interfering with the first inside Tr(Z²), and the quartic piece −(1/12)Tr(Z⁴)/g² of N − ReTrU.

### 4.5 Theorem S18.9 — Two-Channel Closure for the Polarised Vertex

Since f^{abc} is totally antisymmetric, total symmetry of the combined multi-index forces the mode tensor to be totally antisymmetric, and

$$H\_3 \= \\frac{\\mu g}{2}\\sum f^{abc},q^a\_r q^b\_\\alpha q^c\_\\beta, T\_{r\\alpha\\beta}, \\qquad T \\text{ totally antisymmetric (residual exactly 0)},$$

with **no family-dependent factors**.

**Theorem S18.9.** For α, β ∈ T₁(λ₁), T\_{rαβ} is non-zero only for r ∈ T₁(λ₁) ⊕ T₁(λ\_h), over all 31 physical modes, with relative leakage **1.4 × 10⁻¹⁵** at **every one of the six basepoints**. The retained magnitude is exactly c₁ \= 0.3515993958.

**\[CERTIFIED — Check 66\]** The two exchange channels are a property of the gauge-covariant vertex, not of a cochain convention — and this, not §3.5's ratio, is what disposes of the basepoint question.

### 4.6 Gauge fixing

Ω¹ \= im(B₁) ⊕ im(B₂ᵀ), 90 \= 59 \+ 31\. **\[CERTIFIED — Check 49\]** This is a complete **linearized** Hodge gauge fixing; the non-abelian constraint D\_i\[A\]E\_i \= 0 brings a field-dependent projector, a Coulomb kernel at O(g²), a non-trivial Faddeev–Popov determinant and the Gribov horizon. **F-S18.10 (Gate B)**.

### 4.7 F-S18.16 — the metric-weight gate, reduced to one ratio

Pentagons and hexagons are each a single I\_h orbit, so every I\_h-invariant face weight is one ratio ρ \= w₅/w₆ (the common scale is absorbed into g).

| ρ | interpretation | gap λ₁(ρ) | shift | degeneracy |
| ----- | ----- | ----- | ----- | ----- |
| 0.66221 | w\_f ∝ A\_f | 1.1711184846 | **−5.771 %** | 3 |
| **1.00000** | **unweighted (used)** | **1.2428416164** | 0.000 % | 3 |
| \~1.05 | argmax of λ₁(ρ) | 1.2436124 | \+0.062 % | 3 |
| 1.51009 | w\_f ∝ 1/A\_f (DEC Hodge) | 1.1984933703 | **−3.568 %** | 3 |

**\[COMPUTED — Check 68\]** Three readings: the unweighted convention is fixed by consistency with ZS-S7's locked λ₁, not derived (a −5.77 % shift would raise Λ\_QCD by \+6.13 %); **Part I is immune**, since the gap stays three-fold for every ρ; and **there is no variational characterisation** — λ₁(ρ) is not stationary at ρ \= 1, its maximum sitting near ρ ≈ 1.05. Only the two natural weights were tested (**NC-S18.13**).

---

## §5. Part III — The Two-Body Effective Hamiltonian

### 5.1 Setup

$$H\_{\\rm eff}^{(2)} \= PH\_0P \+ g^2\\Big\[P\!:\!H\_4\!:\!P \+ PH\_3\\frac{Q}{E\_0-QH\_0Q}H\_3P\\Big\] \= \\mu\_A P\_A \+ \\mu\_H P\_H$$

by Schur. One-body pieces cancel in μ\_H − μ\_A; the 2 → 1 channel vanishes since f^{abc}δ^{bc} \= 0\.

### 5.2 The seagull

**(a)** V₂ is extracted in Galerkin coefficients; canonical variables **Q** \= q/√λ₁ give a factor λ₁² \= 1.5446554846. **(b)** T\_{iijj} \= \[V₂(e\_i+e\_j) \+ V₂(e\_i−e\_j) − 2V₂(e\_i) − 2V₂(e\_j)\]/12. **(c)** For Σ|S\_{ij}|² \= ½, ⟨:V₄:⟩ \= (6/Ω₀²)λ₁²Σ\_{ij}T\_{iijj}σ\_iσ\_j with σ\_{(a,α)} \= R\_{αα}/√(2d\_A), R\_A \= **1**/√3, R\_H \= diag(1,−1,0)/√2.

**Reduction (new in v1.6).** Only two contractions are needed, not the full T\_{iijj} matrix. Global SU(N) invariance makes Σ\_a T\_{(aα)(aα)(bβ)(bβ)} independent of b, since summing one adjoint index against two free ones must give an invariant ∝ δ^{bc}. Hence the 3 × 3 register matrix needs **d\_A** pair-evaluations per (α,β) rather than d\_A², validated against the full tensor to 5 × 10⁻¹⁴.

*Table 5.1. Seagull contribution to μ\_H − μ\_A, per unit N.*

| N | s(N)/N | retracted v1.2 value |
| ----- | ----- | ----- |
| 2 | −0.013185445 | −0.124091538 |
| 3 | −0.012576762 | −0.124091538 |
| 4 | −0.012363723 | −0.124091538 |
| 5 † | −0.012256018 | — |
| 6 † | −0.012201191 | — |
| fit (N \= 2,3,4) | **−0.0120898 − 0.0043825/N²** | −(3/4)κ²λ₁ |

**\[COMPUTED — Check 58\]** † *\--extended only; **non-ledger exploratory values**.* The seagull is about one tenth of the naive value and **is not proportional to N**; the residual 1/N⁴ coefficient is below 10⁻⁷.

### 5.3 The exchange sector

**(a) λ₁ channel.** The 3-particle norm is ∝ 4(Tr R)², so the exchange **vanishes identically in the H channel**; the coefficient is exactly \+27/4. **\[DERIVED — Check 59\]**

**(b) λ\_h channel.** Same structure with c\_{h,pol} (§0.1).

**(c) Five-particle sector.** A disconnected self-energy: identical in A and H, contributing **exactly zero**. **\[DERIVED — Check 63\]**

Colour factors are analytic and verified against explicit generators for N \= 2, 3, 4\. **\[Check 54\]**

### 5.4 Theorem S18.6A′ — Full Exchange Closure (new in v1.6)

Let r label a closed exchange channel with eigenvalue λ\_r and frequency ω\_r \= √λ\_r. In second-order perturbation theory the canonical cubic vertex carries √λ\_r·λ₁·T\_r; squaring gives λ\_r λ₁², the oscillator normalisations give 1/(ω\_rω₁²), and the energy denominator gives a further 1/ω\_r. The virtual eigenvalue therefore **cancels**:

$$\\frac{\\lambda\_r}{\\omega\_r^{2}} \= \\frac{\\lambda\_r}{\\lambda\_r} \= 1 .$$

Every closed channel contributes the *same* register-and-colour coefficient 9/4, weighted only by its own polarised norm.

**Theorem S18.6A′ (Full Exchange Closure).** $$G\_{\\rm exch} ;=; \\frac{9}{4}\\sqrt{\\lambda\_1}\\sum\_r c\_{r,\\rm pol}^2 ;=; \\frac{9}{4}\\sqrt{\\lambda\_1}\\big(c\_1^2+c\_{h,\\rm pol}^2\\big) ;=; \\mathbf{0.313264316799300},$$ exactly N-independent at O(g²). Brute-force Fock-space perturbation theory gives 0.313264316799300 (SU(2)) and 0.313264316799 (SU(3)) — agreement to **7 × 10⁻¹⁶**. The λ\_h channel *alone* gives 0.003175108696600 against (9/4)√λ₁c\_{h,pol}² \= 0.003175108696600, confirming **exact additivity with no interference**. **\[DERIVED-PERTURBATIVE-CONDITIONAL — Check 62\]**

Theorem S18.6A is now simply the r \= λ₁ term:

$$G\_{\\rm exch}^{(1)} \= \\tfrac94 c\_1^2\\sqrt{\\lambda\_1} \= 0.310089208103,$$

reproduced by Fock to twelve digits for SU(2) and SU(3). **\[Check 61\]**

*Table 5.2. Status of each ingredient after v1.6.*

| ingredient | v1.5 | v1.6 |
| ----- | ----- | ----- |
| λ₁ exchange | closed form | closed form |
| λ\_h exchange | numerical | **closed form** |
| two-channel total | "no closed form" | **closed form (Thm S18.6A′)** |
| seagull s(N) | numerical | numerical (machine-precision contour) |
| G\_∞, a\_geom | extrapolated | extrapolated |

**Corollary S18.6C.** g\_hf(N)/λ\_t \= G\_exch \+ (4/3)s(N)/√λ₁ ≃ G\_∞ \+ a\_geom/N² with **G\_∞ ≃ 0.298805**, **a\_geom ≃ −0.005241**, and G(2) \= 0.29749454, G(3) \= 0.29822252, G(4) \= 0.29847731. The fit form c₀ \+ c₂/N² is part of the claim. **\[COMPUTED-EXTRAPOLATED — Check 64\]** *The only remaining numerical ingredient is the seagull.*

**Theorem S18.6R (retraction).** v1.2's **G** \= 1.1025394066 is too large by **3.6899**, and a \= b \= 0 is false. **\[Check 65\]**

**Scope.** At O(g²) the exchange part has no 1/N² or 1/N⁴ term; the seagull does. Nothing is claimed about full Yang–Mills, where higher orders admit G₀λ\_t \+ G₁λ\_t² \+ H₁(λ\_t)/N² \+ ⋯.

---

## §6. Part IV — Confrontation

### 6.1 Theorem S18.5 — the geometric Hessian route is closed negative

The induced H-channel scalar is 3.3747193575 × I₅ against the Casimir-coproduct lift 3λ₁ \= 3.7285248492, a **9.489 %** deficit that no natural spectral average closes. **\[CLOSED-NEGATIVE, CERTIFIED — Checks 28, 29, 33, 34\]** §5 explains why: the physical operator is a Feshbach projection with a seagull and an exchange at two different energy denominators.

**Anti-numerology refusal, retained.** 0.905108453 agrees with 1 − **A**(1+2**A**) \= 0.907079159 to 0.2177 %. **Refused**: a convention-dependent Rayleigh quotient, 0.2 % far outside the corpus's structural precision, no mechanism. **\[NON-CLAIM — Check 40\]**

### 6.2 F-S18.5 — the pure-geometry Layer-Lift, CLOSED-NEGATIVE

From \[18\], m(0⁺⁺)/√σ \= 3.072(14) and m(2⁺⁺)/√σ \= 4.599(14) give R\_∞ \= 1.4971 and g\_hf(∞) \= 1.655 ± 0.033, against λ₁ \= 1.2428 (R \= 1.3900). **\[E-S18.1\]** The surviving geometric slope is a\_geom·λ\_t ≈ −0.029 against an observed a ≈ −3.06 ± 0.95 — about **one per cent**.

### 6.3 E-S18.2 — the running-coupling tension

$$\\lambda\_{\\rm t}\\big|\_{\\rm TI} \= \\frac{1.655}{0.298805} \= 5.539 \\pm 0.11,$$

against λ\_t(M\_Z, N \= 3\) \= 4.459 from ZS-S1, i.e. α\_s \= 0.1475 and one-loop μ\_TI ≈ 30 GeV. Three items remain in **F-S18.13 (Gate D)**: the scheme relation g\_{S14} \= Z\_g(a\_TI,μ)g\_MS̄(μ) is not derived; a\_TI must be fixed from an independent observable, not the 2⁺⁺/0⁺⁺ ratio; and λ\_t ≈ 5.5 is not small.

**Fixed-point recipe \[CORRECTED in v1.6\].** Let ε₀(λ\_t) be the *dimensionless* scalar eigenenergy of the lattice Hamiltonian, so that the physical mass is m(0⁺⁺) \= ε₀/a\_TI and hence a\_TI⁻¹ \= m(0⁺⁺)/ε₀. The scale entering the running is therefore a **ratio**, not a product: $$\\lambda\_{\\rm t} ;=; 12\\pi,\\alpha\_s^{\\rm S14}\!\\left(\\frac{m\_{0^{++}}^{\\rm ZS}}{\\varepsilon\_0(\\lambda\_{\\rm t})}\\right).$$ *(v1.5 wrote the argument as ε₀·m, which is dimensionally wrong. The reviewer's correction is adopted.)* If this fixed point converges uniquely, a\_TI, λ\_t and m(2⁺⁺)/m(0⁺⁺) are determined together **without** taking any lattice ratio as input.

### 6.4 Theorem S18.7

The relevant operator is H\_eff, whose O(g²) content is a Wilson seagull plus one-gluon exchange over exactly two channels. ZS-S17's ¼ is **G**λ\_t/λ₁ times the coproduct normalization, not a pure number.

---

## §7. Falsification Gates

| ID | Layer | Condition | Status |
| ----- | ----- | ----- | ----- |
| **F-S18.1–3** | MATH, decisive | equivariance / 6-dim closure / Schur scalar | **PASS** |
| **F-S18.4** | SIMULATION *(Gate C, redefined)* | Theorem S18.9 makes the one-gluon space already complete at O(g²). Build the A\_g (dim 12\) and H\_g (dim 140\) blocks from all unordered pairs of the 31 physical modes (Sym² dim 496), include the exact Wilson quartic and cubic couplings to adjacent Fock sectors, test convergence under an occupation cutoff; use sparse Lanczos at λ\_t ≈ 5.5 | **OPEN** |
| **F-S18.5** | OBSERVATIONAL | g\_hf(∞) ≠ λ₁ in continuum SU(N) data | **CLOSED-NEGATIVE** |
| **F-S18.6** | MATH, upgrade | Lemma S18.A fails | **PASS — CLOSED in v1.1** |
| **F-S18.7** | ANTI-NUMEROLOGY | 0.905108 asserted \= 1 − **A**(1+2**A**) | **PASS** |
| **F-S18.8** | CONSISTENCY | locked-input drift | **PASS** |
| **F-S18.9** | MATH, decisive | ⟨h,Θ⟩ ≠ δ\_{αβ}(λ₁−2)/λ₁ | **PASS** (8.9 × 10⁻¹⁶) |
| **F-S18.10** | THEORY *(Gate B)* | Reduce D\[A\] \= B₁ \+ g·ad(A), M\[A\] \= D†D, log det M to O(g²), K \= M⁻¹(−Δ₀)M⁻¹; report Δμ^{FP}*{A,H}, Δμ^{Coul}*{A,H}. If μ\_H − μ\_A is gauge-dependent | **OPEN** |
| **F-S18.11** | MATH, structural | the exchange is not exactly N-independent | **PASS** |
| **F-S18.12** | MATH, structural | unsigned Sym² isotype ≠ A\_g ⊕ H\_g | **PASS** |
| **F-S18.13** | THEORY / OBS *(Gate D)* | Fix a\_TI independently; derive Z\_g; solve λ\_t \= 12πα\_s^{S14}(m₀₊₊/ε₀(λ\_t)) | **OPEN** |
| **F-S18.14** | MATH, audit *(Gate A)* | Wilson cubic coefficient ≠ −1/2 | **PASS** |
| **F-S18.15** | OBSERVATIONAL *(Gate E)* | Covariance-aware fit of \[18\] N \= 2…12; then test the same H\_eff against 0⁺⁺\*, 0⁻⁺, 2⁻⁺ | **OPEN** |
| **F-S18.16** | THEORY | Determine ρ \= w₅/w₆ from the ZS-S14 Hodge inner product | **OPEN** |
| **F-S18.17** | MATH, structural | polarised vertex leaks \> 10⁻¹² relative, or needs averaging | **PASS** (1.4 × 10⁻¹⁵, six basepoints) |
| **F-S18.18** | CODE | external asset needed, file written, or a retracted value reproduced | **PASS** |
| **F-S18.19** | MATH, structural | symmetrised cubic tensor not totally antisymmetric | **PASS** (residual exactly 0\) |
| **F-S18.20** | MATH, structural *(new in v1.6)* | G\_exch ≠ (9/4)√λ₁Σ\_r c²\_{r,pol}, or the channels are not exactly additive | **PASS** (7 × 10⁻¹⁶; λ\_h channel alone to 13 digits) |
| **F-S18.21** | CODE *(new in v1.6)* | Any ledger value varies under O(3) rotation of a degenerate eigenbasis, or the contour spread exceeds 10⁻¹¹ | **PASS** (3.3 × 10⁻¹⁶; 1.6 × 10⁻¹³) |

---

## §8. Non-Claims

**NC-S18.1** λ\_t is not derived. **NC-S18.2** The cup-product image is the kinematic carrier. **NC-S18.3** The polynomial reduced model is not re-opened. **NC-S18.4** No per-N Athenodorou–Teper mass is extracted here; the 1σ assumes independent errors. **NC-S18.5** No Clay Millennium claim. **NC-S18.6** 0.905108453 is not identified with any corpus constant. **NC-S18.7** ZS-Q19 remains separate. **NC-S18.8** Lemma S18.A is not a new result in algebraic topology. **NC-S18.9** §5 is perturbative O(g²) in a linearized gauge fixing and a six-mode active space; at λ\_t ≈ 5.5 it is outside its domain of control. **NC-S18.10** λ\_t \= 5.54 is not a prediction. **NC-S18.11** s(N) is a numerical extraction; no algebraic identity is asserted for −0.0120898 or −0.0043825. **NC-S18.12** The (Wilson quartic)/(naive cup-square) ratio is not a constant of the geometry. **NC-S18.13** ρ \= 1 is not derived; only two non-constant weights were tested.

**NC-S18.14 (revised in v1.6).** Theorem S18.6A′ is a closed form *within the two closed channels of Theorem S18.9 and at O(g²)*. No claim is made that Σ\_r c²\_{r,pol} is a corpus constant, nor that the 9/4 survives beyond leading order.

**NC-S18.15 (new in v1.6).** The published SHA-256 is computed over values canonically rounded to ten significant digits. It detects manuscript–code drift within a fixed environment; it is **not** a proof of bit-identical reproducibility across BLAS implementations, and the environment is recorded alongside it.

---

## §9. Verification Suite

zs\_s18\_verify\_v1\_6.py is one self-contained file: numpy and scipy only, the TI complex rebuilt from Cartesian coordinates, no imported geometry, no absolute paths, **no files written**.

**74/74 PASS | 5 OPEN \+ 2 EXTERNAL | runtime 6 s | \--extended adds N \= 5, 6**

*Changes in v1.6, following the external review of v1.5:*

| review item | change |
| ----- | ----- |
| §3 missed closed form | **Theorem S18.6A′** proved and verified; Proposition → Theorem; new gate F-S18.20 |
| §4 Check 25 FAILS elsewhere | 61.9257 % **retracted** as basis-dependent; replaced by the invariant trace ratio 71.0350815252 % with a rotation-drift assertion; discipline (xi); gate F-S18.21 |
| §5 runtime 600 s+ | **70 s → 6 s**: eigh hoisted out of the contour loop; matrix inversions removed (exp(igX)⁻¹ \= exp(−igX) exactly, also for complex g); face products batched over contour nodes and face type; seagull reduced from O(n²) to O(d\_A) pair-evaluations by colour invariance |
| §6 "exact" overstated | reworded to **machine-precision numerical extraction**; six-contour stability added as **Check 74** |
| §7.1 docstring still v1.4 | corrected |
| §7.2 F-S18.4 register text stale | now matches the redefined Gate C |
| §7.3 SHA not environment-independent | canonical rounding to 10 significant digits; environment recorded; explicit caveat (**NC-S18.15**) |
| §8 fixed-point scale inverted | corrected to λ\_t \= 12πα\_s^{S14}(m₀₊₊/ε₀) |

---

## §10. Conclusion

Three versions of this paper looked for a pure number; both candidates are closed negative. v1.2 identified the mis-specification; v1.3 audited the reduction against the Wilson holonomy and retracted its own headline; v1.4 made the companion code the claim; v1.5 found that a projection had been used as a coupling; v1.6 finds two things — that a ledger number had been surviving on one BLAS implementation, and that the closed form v1.5 declared absent was there all along.

The second is the substantive one. The two exchange channels contribute additively with the same coefficient because the virtual eigenvalue cancels between the vertex and the propagator, so

$$G\_{\\rm exch} \= \\frac{9}{4}\\sqrt{\\lambda\_1}\\sum\_r c\_{r,\\rm pol}^2 \= 0.313264316799300,$$

agreeing with brute-force Fock-space perturbation theory to 7 × 10⁻¹⁶, and channel by channel to thirteen digits. The **entire exchange sector is now analytic**; the seagull is the only numerical ingredient left in Corollary S18.6C.

The first is the more uncomfortable. "61.9257 %" sat in the ledger through six versions and two external reviews, and was wrong in the specific sense that it was never a property of the geometry — only of an arbitrary rotation inside a three-fold degenerate eigenspace. It survived because it was reproducible on one machine. That is now discipline (xi), and the guard is F-S18.21.

 kinematics       S17 ANTISYM closed | S18 SYM closed | parity dictionary closed     CLOSED  
 cubic bridge     quadratic exact | cubic exact (mu=-1/2) | polarised closure         CLOSED  
 exchange         Thm S18.6A' \-- closed form, both channels, additive                 CLOSED  
 quartic          machine-precision contour extraction; no closed form                CONDITIONAL  
 gauge fixing     linearized Hodge, 90 \= 59 \+ 31                                      PARTIAL   (F-S18.10)  
 dynamics         S18.6C \= analytic exchange \+ numerical seagull                      CONDITIONAL (F-S18.4)  
 normalization    lambda\_t \= 5.539 \+/- 0.11; scheme and scale undetermined            OPEN      (F-S18.13)  
 metric weight    one ratio rho; rho \= 1 fixed by consistency only                    OPEN      (F-S18.16)  
 blind test       one ratio matched; 0++\*, 0-+, 2-+ not attempted                     OPEN      (F-S18.15)

Three lines closed, two conditional, four open — one more closed than v1.5, and the conditional lines have shrunk to a single numerical ingredient each.

**ZS-S18 is complete at this scope and is closed with v1.6.** ZS-S19 inherits, in the order the reviews recommend: (1) the exact Wilson quartic by the Magnus combination Tr(Ω₂² \+ 2Ω₁Ω₃ \+ Ω₁⁴/12), together with Hodge-weight closure of ρ, which would lift Proposition S18.6B and Corollary S18.6C to DERIVED; (2) the non-abelian Gauss–Coulomb–Faddeev–Popov reduction, which on the TI is a finite-matrix problem; (3) the full 31-mode non-perturbative spectrum by sparse Lanczos, since at λ\_t ≈ 5.5 no perturbative series is controlled; and (4) the ZS-S1/ZS-S7 scale matching through λ\_t \= 12πα\_s^{S14}(m₀₊₊/ε₀(λ\_t)). That, and not the present calculation, would be the zero-free-parameter Yang–Mills bridge.

---

## Acknowledgements & Code Availability

This work was developed with the assistance of AI tools for symbolic verification, code generation and manuscript drafting. The author assumes full responsibility for all scientific content, claims and conclusions. The author thanks the external reviewers of v1.2 – v1.5, whose successive audits produced the Gate A retraction, the single-file rebuild, the vertex correction, and — in the final round — both the closed form of Theorem S18.6A′ and the discovery that a six-version-old ledger value was basis-dependent.

**zs\_s18\_verify\_v1\_6.py** — the entire computational content of this paper in one file. Code: https://github.com/KennyKang-git/zspin.

---

## Appendix

### Appendix A. Verification Ledger (74 checks)

| \# | check | \# | check |
| ----- | ----- | ----- | ----- |
| 1–6 | cell complex, L₂ spectrum, |I\_h| \= 120 | 41–42 | **LEMMA S18.A** |
| 7–8 | B₂ intertwines; \[P\_F, L₂\] \= 0 | 43–45 | Corollaries A1, A2; h spans ker L₂ |
| 9–11 | Ω² isotype; **S18.C1** | 46–48 | **THM S18.4** \+ closed form |
| 12–13 | ⟨a,a⟩ \= δ/λ₁; Ω₀ \= √λ₁ | 49–53 | gauge census; ε structure; two channels |
| 14–15 | alternating split 92.8605/7.1395 | 54 | colour identities vs N \= 2,3,4 |
| 16–20 | images, isotypes, leakage; **S18.C2** | 55–57 | **GATE A(i),(ii),(iii)** |
| 21–24 | equivariance twist; SYM basepoint-free | 58 | **seagull, 1/N²** |
| **25** | **BASIS-INVARIANT raw-map ratio 71.0350815252 %** | 59–60 | \+27/4; **λ\_h vertex correction** |
| 26–27 | harmonic shares | **61–62** | **S18.6A and S18.6A′ closed forms** |
| 28–29 | Schur H block | 63–65 | 5-particle zero; S18.6C; **v1.2 retraction** |
| 30–32 | C₂(T₁); **Q\_Z**; R | **66** | **THM S18.9, six basepoints** |
| 33–34 | geometric ≠ coproduct | 67–68 | ratio not universal; **ρ-reduction** |
| 35–38 | masses; MP SU(3) | 69 | anti-regression |
| 39–40 | locked inputs; anti-numerology | 70–73 | parity dictionary; **full-mode block dims** |
|  |  | **74** | **contour stability over six (r,M)** |

### 

### Appendix B. Reproducing the Key Numbers

$ mkdir empty && cd empty && cp .../zs\_s18\_verify\_v1\_6.py . && python zs\_s18\_verify\_v1\_6.py

  VERIFICATION: 74/74 PASS | 5 OPEN gates \+ 2 EXTERNAL, NOT counted

  environment: {"python":"3.12.3","numpy":"2.4.4","scipy":"1.17.1","machine":"x86\_64"}

  SHA256(result block) \= ccc76829a4fcf91dbd863ab33c39d0f94a580deb155d4a94eb82b76ce579aaea

$ ls

  zs\_s18\_verify\_v1\_6.py

| quantity | value |
| ----- | ----- |
| λ₁ / λ\_h / Ω₀ | 1.2428416164 / 7.5210904061 / 1.1148280659 |
| c₁ / c₁² | 0.3515993958 / 0.1236221351 |
| **c\_{h,pol}²** (physical vertex) | **0.0012658090** |
| c\_h² (raw cup projection) | 0.0095045494 — **not a coupling** |
| symmetrised tensor antisymmetry residual | **exactly 0** |
| **raw-map two-T₁ ratio (basis-invariant)** | **71.0350815252 %** (drift 3.3 × 10⁻¹⁶) |
| retracted basis-dependent value | 61.9257 % (random bases: 63.6, 74.6, 76.5, 84.3 %) |
| Gate A: cubic coefficient μ | −0.50000 (basepoint spread \< 10⁻¹⁰) |
| Gate A: quartic, six contours | 0.02835166674 ± 1.6 × 10⁻¹³ |
| Gate A: quartic ratio range | −0.0834 … \+0.3893 (sign change) |
| polarised cubic: leakage / retained | 1.365 × 10⁻¹⁵ (six basepoints) / c₁ |
| metric weight ρ: gap at 1 / 0.66221 / 1.51009 | 1.2428416164 / 1.1711184846 / 1.1984933703 |
| metric weight: argmax; degeneracy | ρ ≈ 1.05 (**not** 1); 3-fold for every ρ |
| seagull s(N)/N, N \= 2, 3, 4 | −0.013185445, −0.012576762, −0.012363723 |
| seagull fit | −0.0120898 − 0.0043825/N² |
| **G\_exch^{(1)} \= (9/4)c₁²√λ₁** | **0.310089208103** (Fock, 12 digits, both N) |
| **G\_exch \= (9/4)√λ₁(c₁²+c\_{h,pol}²)** | **0.313264316799300** (Fock diff 7 × 10⁻¹⁶) |
| λ\_h channel alone | 0.003175108696600 (Fock \= closed form, 13 digits) |
| **G\_∞** ; **a\_geom** | **0.29880491** ; **−0.00524148** |
| G(2), G(3), G(4) | 0.29749454, 0.29822252, 0.29847731 |
| retracted v1.2 **G** ; overshoot | 1.1025394066 ; 3.6899 |
| λ\_t required ; λ\_t(M\_Z) from ZS-S1 | 5.5387 ± 0.11 ; 4.4590 |
| full two-gluon basis (31 modes) | Sym² dim 496 \= A\_g 12 ⊕ H\_g 140 ⊕ … |
| ⟨h, Θ(a\_α,a\_α)⟩ | −0.6092155054875 |
| induced L₂ on H / ratio to coproduct | 3.3747193575 × I₅ / 0.905108453 |

### 

### Appendix C. Cross-Reference Table

| paper | uses | returns |
| ----- | ----- | ----- |
| ZS-F2 / F5 / S4 | **A**, **Q**, dim(**Z**), v | unchanged |
| ZS-S1 | α\_s(M\_Z) \= 11/93 | E-S18.2; F-S18.13 fixed-point recipe |
| ZS-S7 | λ₁, L₂ spectrum, m(0⁺⁺) | S18.C1; F-S7.5 explained; **F-S18.16 asks ZS-S7 to justify ρ \= 1** |
| ZS-S14 | master action, −¼G² | cubic exact; quartic corrected, contour-extracted |
| ZS-S17 | two-T₁ closure, **I\_Z**, **Q\_Z**, R | closure promoted to the polarised vertex; **the 7.14 % split confirmed as a projection and denied vertex status**; R \= 1.3900 is not a zero-parameter prediction |
| ZS-S19 (planned) | — | inherits Gates B, C, D, E, the ρ problem, the Magnus quartic, the 496-dim census |

---

## References

\[1\] K. Kang, *Geometric Impedance: A \= 35/437*, ZS-F2 v1.0 (2026). \[2\] K. Kang, *Gauge Symmetry Constraint: Why Q \= 11*, ZS-F5 v1.0 (2026). \[3\] K. Kang, *Electroweak Completion*, ZS-S4 (2026). \[4\] K. Kang, *The Spinor Mass Gap*, ZS-S7 v1.0 (April 2026). \[5\] K. Kang, *Master Action Total Closure*, ZS-S14 v2.0 (May 2026). \[6\] K. Kang, *The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex*, ZS-S17 v2.2 FINAL (July 2026). \[7\] K. Kang, *Holonomy, Spinor Gate, and Regge Phase*, ZS-M3 v1.0 (2026). \[8\] N. E. Steenrod, "Products of cocycles and extensions of mappings," Ann. Math. **48**, 290 (1947). \[9\] G. Hirsch, "Quelques propriétés des produits de Steenrod," C. R. Acad. Sci. Paris **241**, 923 (1955). \[10\] A. N. Hirani, *Discrete Exterior Calculus*, Ph.D. thesis, Caltech (2003). \[11\] J. Dodziuk and V. K. Patodi, "Riemannian structures and triangulations of manifolds," J. Indian Math. Soc. **40**, 1 (1976). \[12\] K. G. Wilson, "Confinement of quarks," Phys. Rev. D **10**, 2445 (1974). \[13\] M. Creutz, *Quarks, Gluons and Lattices* (Cambridge University Press, 1983). \[14\] M. Lüscher, "Some analytic results concerning the mass spectrum of Yang–Mills gauge theories on a torus," Nucl. Phys. B **219**, 233 (1983). \[15\] P. van Baal, "The small-volume expansion of gauge theories coupled to massless fermions," Nucl. Phys. B **264**, 548 (1986). \[16\] C. J. Morningstar and M. J. Peardon, "The glueball spectrum from an anisotropic lattice study," Phys. Rev. D **60**, 034509 (1999), arXiv:hep-lat/9901004. \[17\] A. Athenodorou and M. Teper, "The glueball spectrum of SU(3) gauge theory in 3+1 dimensions," JHEP **11**, 172 (2020), arXiv:2007.06422. \[18\] A. Athenodorou and M. Teper, "SU(N) gauge theories in 3+1 dimensions: glueball spectrum, string tensions and topology," JHEP **12**, 082 (2021), arXiv:2106.00364. \[19\] H. Feshbach, "Unified theory of nuclear reactions," Ann. Phys. (N.Y.) **5**, 357 (1958). \[20\] G. 't Hooft, "A planar diagram theory for strong interactions," Nucl. Phys. B **72**, 461 (1974). \[21\] V. N. Gribov, "Quantization of non-Abelian gauge theories," Nucl. Phys. B **139**, 1 (1978). \[22\] D. Zwanziger, "Fundamental modular region, Boltzmann factor and area law in lattice gauge theory," Nucl. Phys. B **412**, 657 (1994). \[23\] W. Magnus, "On the exponential solution of differential equations for a linear operator," Comm. Pure Appl. Math. **7**, 649 (1954). \[24\] H.-P. Pavel, "SU(3) Yang–Mills Hamiltonian in the flux-tube gauge," arXiv:1611.06542 \[hep-th\]. \[25\] H.-P. Pavel, "Low-energy spectrum of SU(3) Yang–Mills quantum mechanics," arXiv:2112.06248 \[hep-th\]. \[26\] R. E. Moore, R. B. Kearfott and M. J. Cloud, *Introduction to Interval Analysis* (SIAM, 2009), ch. 8\. \[27\] J. F. Cornwell, *Group Theory in Physics*, Vol. 1 (Academic Press, 1984). \[28\] C. Lanczos, "An iteration method for the solution of the eigenvalue problem of linear differential and integral operators," J. Res. Natl. Bur. Stand. **45**, 255 (1950). \[29\] A. Jaffe and E. Witten, "Quantum Yang–Mills Theory," Clay Mathematics Institute Millennium Prize Problem description (2000).

---

## Version History

**v1.6 (July 2026\) — final.** **Theorem S18.6A′ (Full Exchange Closure), new:** the two closed channels contribute additively with the same universal coefficient because the virtual eigenvalue cancels (λ\_r/ω\_r² \= 1), giving **G\_exch \= (9/4)√λ₁ Σ\_r c²\_{r,pol} \= (9/4)√λ₁(c₁²+c\_{h,pol}²) \= 0.313264316799300**, matching Fock-space perturbation theory to 7 × 10⁻¹⁶ and channel-by-channel to thirteen digits. v1.5's declaration that this quantity had no closed form is **CORRECTED**, and Proposition S18.6A′ is **promoted to a Theorem**; the whole exchange sector is now analytic, leaving the seagull as the only numerical ingredient of Corollary S18.6C. New gate F-S18.20. **The ledger value 61.9257 % is RETRACTED as basis-dependent:** λ₁ is three-fold degenerate, so the un-averaged two-T₁ content depends on the arbitrary O(3) rotation returned by the eigensolver (random bases give 63.6–84.3 %; an independent reviewer's environment returned 72.4 % and the check FAILED). It is replaced by the **basis-invariant trace ratio 71.0350815252 %** with a rotation-drift assertion of 3.3 × 10⁻¹⁶; new discipline (xi) and gate F-S18.21. **Runtime 70 s → 6 s**: eigh hoisted out of the contour loop, matrix inversions removed (exp(igX)⁻¹ \= exp(−igX) exactly, also for complex g), face products batched over contour nodes and face type, and the seagull reduced from O(n²) to O(d\_A) pair-evaluations using the colour invariance of Σ\_a T\_{(aα)(aα)(bβ)(bβ)}, validated to 5 × 10⁻¹⁴ against the full tensor. The contour extraction is reworded from "exact" to **machine-precision numerical extraction**, with six-contour stability (spread 1.6 × 10⁻¹³) added as **Check 74**. Verifier docstring corrected (still said v1.4); the F-S18.4 register text now matches the redefined Gate C; the digest is computed over canonically rounded values with the environment recorded and an explicit caveat (**NC-S18.15**); and the Gate D fixed point is corrected to λ\_t \= 12πα\_s^{S14}(m₀₊₊/ε₀), a ratio rather than a product. **74 checks, 5 OPEN \+ 2 EXTERNAL, runtime 6 s.**

**v1.5 (July 2026).** **Corrected the λ\_h cubic vertex:** c\_{h,pol}² \= 0.0012658090, not the raw projection 0.0095045494 — a projection is not a coupling (discipline x). v1.4's (√λ₁/4)(9c₁²+c\_h²) retracted. Quartic moved from polynomial fit to Cauchy contour. F-S18.16 reduced to ρ \= w₅/w₆; λ₁(ρ) peaks near 1.05, so no variational characterisation. F-S18.4 redefined. 73 checks.

**v1.4 (July 2026).** All companion code merged into one self-contained file; no JSON. v1.3's Fock companion (which computed the retracted v1.2 Hamiltonian) withdrawn and rebuilt with μ \= −1/2. **Theorem S18.9**. Theorem S18.6 split into three layers. New gate F-S18.16. 71 checks.

**v1.3 (July 2026).** Executed **Gate A**. Cubic exact with μ \= −1/2; quartic **not** μ² times the cup-square. **RETRACTED v1.2 Theorem S18.6.** λ\_t 1.51 → 5.55. 66 checks.

**v1.2 (July 2026).** Gauge fixing, reduction of ZS-S14, Feshbach effective Hamiltonian. Theorems S18.6 (**retracted**), S18.7, S18.8. F-S18.5 → CLOSED-NEGATIVE. 64 checks.

**v1.1 (March 2026).** Closed F-S18.6. **Lemma S18.A** with complete proof. Theorem S18.4 upgraded to an exact identity. 48 checks.

**v1.0 (March 2026).** Initial public release. Consolidated from internal Z-Spin Collaboration research notes up to the ZS-S17 v2.2 FINAL follow-up seed. Theorems S18.1–S18.5; Corrections S18.C1, S18.C2. 40 checks.  
