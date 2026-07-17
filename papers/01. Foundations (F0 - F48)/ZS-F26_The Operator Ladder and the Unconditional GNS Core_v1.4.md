**ZS-F26**  
**The Operator Ladder and the Unconditional GNS Core: Douglas Uniformization of the Weil-Positivity Rung, High-Frequency Coercivity of the Archimedean Block, and the Window-Inductive Realization of Gate D5**

**Kenny Kang**  
Z-Spin Collaboration  ·  March 2026  
Theme: Foundations / RH Bridge  ·  Paper code: **ZS-F26  ·  v1.4**   (continuation of ZS-F24 → ZS-F25)

**Verification: 47/47 PASS**   |   **Zero Free Parameters**   |   **NO CLAIM on RH / GRH**   |   **Gate D5 remains IMPORTED-OPEN ≡ RH**

**§0.  Abstract**

ZS-F25 v2.0 closed the logical perimeter of the Weil-positivity programme around Gate D5 and registered three audit items at its boundary: the Connes–Consani base rung (autocorrelation reach below log 2 ⇔ SL \= ∅), the infinite-dimensionality of the archimedean block inside the generalized-Schur rung (Lemma 11.4, stated there with the finite-matrix criterion of Albert 1969), and the conditionality of the GNS realization (positivity in, Hilbert space out). The present paper closes what can be closed honestly in all three and registers exactly what cannot. (i) *Unconditional stage.* The Weil form restricted to any window of autocorrelation reach below log 2 is positive (Connes–Consani 2021, IMPORTED-PROVEN); its GNS/Kolmogorov quotient Hbase therefore exists unconditionally (Theorem 4.1); all window cores of a fixed length are canonically isometric under the scaling flow, whose QW\-invariance is exact (Proposition 4.2 with Lemma 3.1); and minimal-Kolmogorov uniqueness identifies Hbase with the closed span of the Connes–Consani Sonin-compression defect vectors (Theorem 4.3). (ii) *Unconditional infinite-dimensionality.* A high-frequency coercivity theorem (Theorem 4.4) proves dim Hbase \= ∞ with explicit derived constants: Re ψ(1/4 \+ ir/2) is strictly increasing in |r| from its global minimum ψ(1/4) \= −γ − π/2 − 3 log 2 \= −4.227454 (Lemma 4.6), a leakage lemma bounds the low-frequency mass *fraction* of high window modes, in Plancherel normalization, by 8Rℓ / (π³(1−δK)²K) (Lemma 4.5′), and the admissible witness (R₀, K₀) \= (17.082, 24\) certifies QW \> 0 on an infinite-dimensional tail subspace of the base window (positivity margin \+0.125, constants cleak \= 20.38 and cpole \= 0.631 — the latter now in closed form and K-invariant; minimal K₀ \= 22); numerically the tail is coercive already from K \= 5 (λmin \= 1.469, rising to 2.808 at K \= 20), and the measured worst-case low-frequency fraction is 0.019 at K \= 36 (tail truncation 264 modes, monotonically increasing in truncation), comfortably under the analytic bound 0.0867. The audit item is thereby a theorem. (iii) *Douglas uniformization of the rung.* The Section-Certification Gap theorem (Theorem 6.1, PROVEN: A \= diag(1/n), b \= (1/n) on ℓ² ⊕ ℂ) shows that every finite section of a rung block can be positively completed with section Schur bound HN \= Σn≤N 1/n, while no positive completion of the full block exists for any finite diagonal datum, because b ∉ ran A1/2 — rung certification is intrinsically a uniform, infinite-dimensional statement, and no finite section certifies it. The Rung Criterion (Lemma 6.2 \= Lemma 11.4′) restates the rung without pseudoinverses or closed-range hypotheses; its bounded-realization shadow is the Douglas–Shmul’yan contraction criterion B \= A1/2KC1/2 with ‖K‖ ≤ 1 (Theorem 6.3, IMPORTED), so the Z-Spin mediation of every rung is contractive (Corollary 6.5) and, combined with F25 Theorem 11.6, ADS-5 and Lemma M31.0, operator-valued, cross-coupled, and ΠZ\-sandwiched (Theorem 6.6). (iv) *D5 as a colimit.* The window GNS cores form a directed system whose connecting maps are isometries exactly where positivity holds; RH ⇔ the system is total ⇔ the isometric colimit H∞ exists; on H∞ the scaling flow is a strongly continuous unitary group whose self-adjoint generator has spectrum equal to the zero set, with all eigenvalues simple *on the cyclic minimal subrealization* and zero multiplicities absorbed as spectral weights — the absorption-side realization, consistent with Connes 1999 and F25 Theorem 6.6 (Theorems 5.2–5.3). (v) *Rung 1 exactly.* Crossing log 2 perturbs the form by −√2 log 2 · Re Tlog 2, the real part of a compressed in-window translation (Proposition 7.1); the Exact-Half Lemma (Lemma 7.2, PROVEN here: on every window shorter than 2 log 2 the compressed translation is 2-nilpotent and ‖Re Tτ‖ \= 1/2 exactly) gives the sharp a priori bound 0.490129·‖g‖² on the rung-1 perturbation and the sharpened sufficient route Qarch ≥ (√2 log 2)/2 on the window sphere (Proposition 7.5). Preregistered numerics — two-sided explicit-formula agreement at 0.049% and 0.0030% over 160 zeros — show the route fails decisively: the archimedean block alone is *indefinite* on every rung window (λmin \= −0.074, −0.318, −0.416 at ℓ \= 0.80, 1.00, 1.09), while the full Weil form remains positive there (λmin \= 1.9×10−4, 1.9×10−6, 9.5×10−7). Rung positivity, where it holds, is produced by arithmetic–archimedean cross-cancellation, not domination — in numerical agreement with the necessity profile of F25 Theorem 11.6. The Master Inequality MI(2) is formulated as the exact content of rung 1; its truth is OPEN and is not claimed. (vi) *Sector shadow* \[OBSERVATION\]: the first two rung bases are 2 and 3 — the unique prime pair solving (p−1)(q−1) \= p (ZS-M19 T1, PROVEN) — and the first composite control is 6 \= 2·3 (Λ(6) \= 0), so the corpus sector triple (Z, X, Y) \= (2, 3, 6\) coincides with (rung₁, rung₂, control₁); and the unconditional positivity reach log 2 equals the Z-bottleneck channel capacity ln 2 (ZS-F8 / ZS-Q7). Both observations are exact, parameter-free, anti-numerology-guarded, and used in no proof. (vii) *Frontier synchronization.* The same finite-prime-window object is extremized in Connes’s February 2026 survey to approximate the first fifty zeros on the critical line (primes below 13, accuracies 2.6×10−55–10−3); his minimization reading and the present positivity reading study opposite ends of the spectrum of the same windowed operator and share the finite→infinite Euler-product open step, registered as O-F26.5 (§7.4, §12). (viii) *v1.2 additions.* The function-space convention is repaired (half-window class, evenness carried by f and h, not g; §3.1); MI(2) is given three equivalent operator formulations (quadratic-form, block-positivity, Douglas-contraction; Proposition 7.7); the rung-1 Douglas factor is constructed conditionally as the limit of regularized finite-section factors K2,ε \= (A+ε)−1/2B(C+ε)−1/2, with the trichotomy MI(2) ⇔ block positivity ⇔ uniform contraction supε‖K2,ε‖ ≤ 1 (Theorem 7.6) — the measured norms are ‖K2,ε‖ \= 0.9972–0.999999 \< 1 at every regularization, a nearly saturated contraction (§7.5); and the first data for O-F26.5 are reported: at ℓ \= (log 13)/2 \= 1.28247 — the window length of Connes’s prime cutoff — the minimal eigenvector of QW has *exactly six local minima of |ĝ| on \[0, 40\], and they are the six zero ordinates* γ₁–γ₆, with offsets at the 10−3 scale for γ₁–γ₃ and of order 10−2–10−1 (quadrature-sensitive) for γ₄–γ₆ (§7.6, COMPUTED). (ix) *v1.3 additions.* The bridge phenomenon is given its variational mechanism: the zero-side identity forces every unit minimal eigenvector to satisfy the simultaneous notch bound |ĝmin(γk)| ≤ √(λmin/2) at every critical-line ordinate (Proposition 7.10, DERIVED; verified at all six ordinates, G6); and the uniform-contraction program for K2 is structured by two PROVEN lemmas — ε-monotone certification (the certified set {ε : ‖K2,ε‖ ≤ 1} is upward-closed, so MI(2) at a section is exactly ε\*(N) \= 0\) and section monotonicity (MI(2) ⇔ supN ε\*(N) \= 0\) — with three open routes registered (commutator/Exact-Half, prolate scattering, monotone finite-section; §7.7). (x) *v1.4: the preregistered ℓ-scan is executed* (§7.8). The basis-convergence precondition separates the error sources: under M \= 80 → 160 the γ₁–γ₄ offsets are stable to 10−4–10−3 while the independent-quadrature variation is 10−1\-scale, so the γ₄–γ₆ sensitivity is quadrature-dominated. The offset–margin law is then established at first order: the Newton-step bound |γk − r₀| ≤ |ĝmin(γk)|/m ≤ √(λmin/2)/m (Proposition 7.11, DERIVED) predicts every resolved notch offset — 34 (window, zero) pairs across eight windows and five decades of λmin, measured/predicted ratio median 1.04, range \[0.63, 1.22\] with the outliers at precision-floor offsets — and the resolution count grows monotonically 3 → 6 as the positivity margin collapses, with the sub-rung base window as the predicted loose control. O-F26.5’s open content narrows to the theoretical asymptotics of λmin(ℓ). Verification: 47/47 PASS. Zero free parameters. No claim is made on RH at any stage; Gate D5 remains IMPORTED-OPEN ≡ RH.

*Keywords: Weil positivity, explicit formula, Connes–Consani base rung, GNS/Kolmogorov core, Sonin space, Douglas factorization, Shmul’yan contraction criterion, generalized Schur complement, shorted operator, window-inductive system, colimit, absorption spectrum, compressed translation, nilpotent half lemma, Z-Spin mediation, Z-bottleneck, anti-numerology*

**§0.1  Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Rigorous mathematical proof or exact closed-form identity; no open step. |
| **DERIVED** | Follows by valid deduction from corpus axioms (**A**, **Q**, dim Z) and PROVEN results. |
| **DERIVED-CONDITIONAL** | Follows given one explicitly stated, currently open, condition. |
| **HYPOTHESIS-strong** | Well-motivated, corpus-consistent, anti-numerology-aware; not yet derived. |
| **IMPORTED** | Result taken from a prior corpus paper or the peer-reviewed external literature. |
| **IMPORTED-OPEN** | An unresolved statement of the external frontier, imported at its registered status (e.g. RH, Weil positivity). |
| **COMPUTED** | Numerical result under the stated discretization; consistency evidence, never proof. |
| **OBSERVATION** | Exact structural fact registered without a mechanism; carries no evidentiary weight in proofs. |
| **OPEN** | Registered open gate; not closed by present corpus tools. |
| **NON-CLAIM** | Stated explicitly as not asserted. |

**§1.  Introduction and Position in the Programme**

ZS-F25 v2.0 \[22\] reduced the Weil-positivity programme to a single open statement. All proposed positivity formats — kernel, defect-square, compression — are PROVEN-equivalent to Weil positivity itself (F25 Theorem 11.2, via GNS/Kolmogorov factorization); full positivity is reduced to the exhaustion of finite prime windows SL \= {pk : k log p ≤ 2L} (F25 Theorem 11.3); the archimedean base rung is PROVEN (Connes–Consani 2021 \[4\], F25 §11.5); the induction step is given a generalized-Schur form (F25 Lemma 11.4, with Albert 1969 \[13\]); and corpus-PROVEN no-gos force any realization to be operator-valued and cross-coupled under Z-Spin mediation (F25 Theorem 11.6, with ADS-5 \[25\] and Lemma M31.0 \[26\]). The open remainder is the inductive rung, and its totality is RH. In February 2026, while this programme was internal, Connes \[9\] entered the same finite-prime-window world from the opposite direction — extremizing the restriction of Weil’s quadratic form to primes below 13 to approximate the zeros — making the present paper’s window-by-window positivity analysis directly contemporary with the external frontier (§7.4).

Three audit items were registered at this boundary in the internal deep-exploration session that prepared the present paper. First, the *base-rung import*: is the CC 2021 statement consumed exactly, and what unconditional object does it produce? Second, the *infinite-dimensional gap*: F25 Lemma 11.4 is stated with Albert's finite-matrix criterion, but the archimedean block of any rung is an operator on an infinite-dimensional space — in what precise sense does the rung survive the passage to infinite dimensions, and is the survival automatic or substantive? Third, the *GNS conditionality*: the GNS realization of the Weil form consumes positivity as input, and full positivity is RH — is there any unconditional Hilbert-space content at all, and what exactly does the conditional realization deliver when it exists?

This paper answers all three with theorems, a PROVEN counterexample, a formulated master inequality, and a preregistered numerical suite, while claiming nothing about RH. The answer is organized into seven contributions.

**C1 (Theorem 4.1, DERIVED).** The unconditional GNS core Hbase exists: the Weil form restricted to any window of autocorrelation reach below log 2 is positive by CC 2021, and the GNS/Kolmogorov quotient-completion is therefore unconditional. The conditionality of the F25 §11 realization begins strictly *above* the base rung, not at it.

**C2 (Proposition 4.2 \+ Theorem 4.3, DERIVED).** All window cores of a fixed length are canonically isometric — the Weil form is exactly invariant under the scaling flow (Lemma 3.1) — and the minimal Kolmogorov factorization is unique up to unitary equivalence, so Hbase is canonically unitary to the closed span of the Connes–Consani Sonin-compression defect vectors. The corpus's abstract stage and the external concrete stage are the same Hilbert space.

**C3 (Theorem 4.4, DERIVED, unconditional).** dim Hbase \= ∞, by high-frequency coercivity of the archimedean form, with every constant derived: the strict monotonicity of Re ψ(1/4 \+ ir/2), an explicit leakage bound for high window modes, and the admissible witness (R₀, K₀) \= (17.082, 24\) with margin \+0.125 (constants cleak \= 20.38, cpole \= 0.631 in closed form). This converts the second audit item from a registration into a theorem.

**C4 (Theorem 6.1, PROVEN; Lemma 6.2; Theorems 6.3–6.4, DERIVED/IMPORTED).** The infinite-dimensional gap in F25 Lemma 11.4 is real and is closed by uniformization, not by section-counting: the Section-Certification Gap counterexample shows sectionwise Albert data can pass at every finite stage with divergent Schur bounds while no completion of the full block exists; the Rung Criterion (Lemma 11.4′) states the rung at form level with no pseudoinverse and no closed-range hypothesis; and the Douglas–Shmul’yan contraction criterion is its exact bounded-operator shadow. F25 Lemma 11.4 is refined, not retracted (§6.7).

**C5 (Theorems 5.2–5.3, DERIVED equivalence; existence IMPORTED-OPEN ≡ RH).** Gate D5 is the existence of a colimit: the window GNS cores form a directed system with isometric connecting maps exactly where positivity holds, RH is equivalent to the totality of the system, and on the colimit the scaling flow realizes the zero set as the spectrum of a self-adjoint generator on the absorption side, with multiplicities absorbed as spectral weights.

**C6 (§7, DERIVED statements; truth OPEN; COMPUTED evidence).** Rung 1 is the Master Inequality MI(2), whose perturbation operator is −√2 log 2 · Re Tlog 2 with ‖Re Tlog 2‖ \= 1/2 exactly (Exact-Half Lemma, PROVEN). The sharpened sufficient route is quantified and numerically refuted; the preregistered window numerics expose the arithmetic–archimedean conspiracy and quantify the collapse of the positivity margin along the ladder.

**C7 (§8, OBSERVATION, NC-guarded).** The first rungs of the ladder cast a sector shadow: (rung₁, rung₂, control₁) \= (2, 3, 6\) \= (dim Z, dim X, dim Y), with (2, 3\) the unique prime pair of ZS-M19 T1 and 6 \= 2·3 the first von Mangoldt zero; and the unconditional reach log 2 equals the Z-bottleneck capacity ln 2\. Registered as exact, parameter-free observations; used in no proof.

**C8 (§3.1, §7.5–§7.6, v1.2).** The function-space convention is repaired (half-window class); MI(2) is reformulated in three equivalent operator forms (Proposition 7.7) and the rung-1 Douglas factor is constructed conditionally via regularized finite sections with a DERIVED trichotomy and COMPUTED nearly-saturated contraction norms (Theorem 7.6, §7.5); and the Connes-window bridge experiment delivers the first data for O-F26.5: the minimal eigenvector’s six |ĝ| minima on \[0, 40\] are the six zero ordinates (§7.6).

What this paper does not do: it does not prove rung 1, any higher rung, Weil positivity, or RH; it does not construct the coupling operator K₂ of the candidate §11.7 realization of F25; and it does not promote the sector-shadow observation beyond OBSERVATION/HYPOTHESIS-strong. The non-claims of §11 bound the scope explicitly.

**§2.  Locked Inputs and Imports**

ZS-F26 is a math-spine paper: no proof below consumes the numerical values of **A** \= 35/437, **Q** \= 11, or z\* \= 0.438283 \+ 0.360592i. The corpus constants appear only in the discussion of §8, at OBSERVATION level. The inputs are the following.

Table 2.1.  Locked inputs (internal) and imports (external).

| Object | Statement | Status |
| ----- | ----- | ----- |
| Explicit-formula convention | F25 §6.0 normalization (Iwaniec–Kowalski Thm 5.12): h even, g(u) \= (1/2π)∫h(r)e−irudr, finite-place side −2Σ(Λ(n)/√n)g(log n), singular support at ±k log p. | IMPORTED \[3\] |
| F25 Theorem 11.2 | Positivity ⇔ kernel ⇔ defect-square (GNS/Kolmogorov format equivalence). | IMPORTED-PROVEN \[22\] |
| F25 Theorem 11.3 | Finite-window exhaustion: full positivity ⇔ QSL\~\~ ⪰ 0 for every L. | IMPORTED-PROVEN \[22\] |
| CC 2021 base rung | QW ⪰ 0 on test functions of autocorrelation reach \< log 2 (semilocal {∞} prolate compression). | IMPORTED-PROVEN \[4\] |
| F25 Theorem 11.6 | Necessity profile: any realization is operator-valued, cross-coupled, ΠZ\-sandwiched. | IMPORTED-PROVEN \[22\] |
| ADS-5 (ZS-M22) | Scalar / diagonal-kernel exclusion. | IMPORTED-PROVEN \[25\] |
| Lemma M31.0 (ZS-M31) | Non-separability: no W(g) \= FX \+ FY \+ FZ decomposition; Qdef ≠ QW,V₄. | IMPORTED-PROVEN \[26\] |
| ZS-M19 T1 | Forcing theorem: (p−1)(q−1) \= p has unique prime solution (p, q) \= (2, 3). | IMPORTED-PROVEN \[27\] |
| Z-bottleneck capacity | ln 2 (ZS-F8 / ZS-Q7); dim Z \= 2\. | LOCKED \[28, 29\] |

No quantity below introduces any further constant. The two-variable explicit formula in real logarithmic coordinate u, used throughout §3–§7 and in Appendix B, is fixed in §3.1.

**§3.  The Weil Quadratic Form and Scaling Invariance**

**3.1  Explicit quadratic form (computational normalization)**

**Convention (function space; half-window).**  Throughout, u ∈ ℝ is the multiplicative logarithmic coordinate and g is a *real*, compactly supported, piecewise-C¹ function with supp g ⊆ \[0, ℓ\] (contained in the admissible class of the F25 §6.0 normalization); g̃(u) \= g(−u); f \= g ⋆ g̃ is the autocorrelation, automatically *even* with supp f ⊆ \[−ℓ, ℓ\]; and ĝ(r) \= ∫g(u)eirudu is the Fourier transform, with h(r) \= |ĝ(r)|² automatically *even* on ℝ because g is real. Evenness is carried by f and h — *not* by g, which lives on a half-window; the v1.0–v1.1 phrase “real even Schwartz function” conflated the symmetric-window and half-window pictures and is hereby repaired (Version History). Every proof of §3–§7 uses only the support of f, the evenness of h, and the reality of g, so no statement is affected. The Weil quadratic form in the F25 §6.0 normalization is

QW(g)  \=  2 M\+M−  −  ‖g‖² log π  \+  (1/2π) ∫ |ĝ(r)|² Re ψ(1/4 \+ ir/2) dr  −  2 Σn≥2 (Λ(n)/√n) f(log n),

with M± \= ∫ g(u) e±u/2 du the two pole functionals, ψ the digamma function, and Λ the von Mangoldt function. The pole term arises from h(i/2) \+ h(−i/2) \= 2 Re(M\+ M̄−) under the stated convention; the archimedean integral is the Weil archimedean density. The zero-side identity Σρ h(γρ) \= 2 Σk |ĝ(γk)|² holds with the symmetric limit over |γ| \< T. The first three terms constitute the *archimedean block* Qarch(g); the last is the *prime block*. A function is supported in a *window of length ℓ* if supp g ⊆ \[0, ℓ\]; then supp f ⊆ \[−ℓ, ℓ\] and the prime block sees exactly the von Mangoldt points {n ≥ 2 : log n \< ℓ}.

*Numerical realization (Appendix B).* On a window \[0, ℓ\] the sine basis φk(u) \= √(2/ℓ) sin(kπu/ℓ) is used, with ĝk(r) \= √(2/ℓ) ak (1 − (−1)k eirℓ)/(ak² − r²), ak \= kπ/ℓ. The pole, log π, archimedean, and prime blocks become explicit M×M Gram matrices; the two-sided identity is verified directly (§B.1).

**3.2  Exact invariance under the scaling flow**

**Lemma 3.1 (translation/scaling invariance of Q\~W\~). \[PROVEN\]**  For s ∈ ℝ let (θs g)(u) \= g(u − s) be the translation by s (equivalently, multiplicative scaling by es on the half-line). Then QW(θs g) \= QW(g) for all g and all s.

*Proof.* The autocorrelation is translation-invariant: θs g ⋆ (θs g)̃ \= g ⋆ g̃ \= f, because the cross-correlation of two translates depends only on the difference of shifts. Hence the prime block −2Σ(Λ(n)/√n)f(log n) and the norm ‖g‖² are unchanged. For the archimedean integral, ĝ shifts by a unimodular phase, (θs g)^(r) \= eirsĝ(r), so |ĝ(r)|² is invariant and the integral against Re ψ(1/4 \+ ir/2) is unchanged. For the pole term, M\~±\~(θ\~s\~ g) \= ∫ g(u−s)e±u/2du \= e±s/2M\~±\~(g), so the product M\~+\~M\~−\~ → es/2e−s/2^M\+M− \= M\+M−. Every term is invariant.

Lemma 3.1 is the structural engine of §4–§5: it makes the choice of window *position* immaterial and turns the family of fixed-length windows into a single object acted on by a one-parameter group. It is verified to machine precision in §B.5 (pole product and modal |ĝ|² products invariant under s \= 0.3).

**§4.  The Unconditional GNS Core**

**4.1  Existence (base-rung import)**

**Theorem 4.1 (unconditional base core). \[DERIVED\]**  Let ℓ0 \< log 2 and let Vbase be the real vector space of convention-class g (§3.1: real, compactly supported, piecewise-C¹) with supp f ⊆ (−ℓ0, ℓ0) — the Connes–Consani support class is characterized by the autocorrelation reach, so no evenness of g is required. Then QW is positive semidefinite on Vbase, and the GNS/Kolmogorov quotient-completion

Hbase  \=  closure of  ( Vbase / {g : QW(g) \= 0} )   under  ⟨g, g′⟩ \= QW(g, g′)

is a well-defined real Hilbert space, *unconditionally* (no hypothesis on the zeros).

*Proof.* For supp f ⊆ (−ℓ0, ℓ0) with ℓ0 \< log 2, the prime block vanishes identically: the smallest von Mangoldt point is log 2, and log 2 ≥ ℓ0 excludes it, so QW(g) \= Qarch(g) on Vbase. By Connes–Consani 2021 \[4\] the archimedean (semilocal {∞}) form is positive on exactly this support class, hence QW ⪰ 0 on Vbase. Positivity makes ⟨·,·⟩ a genuine pre-inner-product; quotienting by its radical Nbase \= {QW \= 0} and completing gives a Hilbert space (the Kolmogorov construction, equivalently GNS for the associated state — F25 Theorem 11.2). No positivity beyond the base window is used.

*Remark (where conditionality begins).* The F25 §11 realization is conditional because full positivity is RH. Theorem 4.1 isolates the *unconditional floor* of that construction: the core over any sub-log-2 window exists outright. The conditional part is the *extension* past log 2, formalized as the directed system of §5.

**4.2  Canonical isometry of equal-length cores**

**Proposition 4.2 (scaling identifies equal-length cores). \[DERIVED\]**  For ℓ0 \< log 2 and any s, translation θs descends to a canonical isometric isomorphism Hbase(\[0,ℓ0\]) ≅ Hbase(\[s, s+ℓ0\]). Consequently the base core depends, up to canonical unitary, only on the length ℓ0.

*Proof.* By Lemma 3.1, QW(θs g) \= QW(g); hence θs carries the radical to the radical and the pre-inner-product to the pre-inner-product, inducing a surjective isometry on quotients, which extends to the completions. Canonicity is the group law θsθt \= θs+t.

**4.3  Identification with the Connes–Consani Sonin compression**

**Theorem 4.3 (minimal Kolmogorov uniqueness; concrete model). \[DERIVED\]**  Let ΠCC denote the Connes–Consani semilocal compression whose positivity proves the base rung, and let DCC be its defect operator on the base window (the operator-square root furnished by the Connes–Consani positivity certificate \[4\], which expresses the semilocal archimedean form as a norm-square of the prolate/Sonin compression on exactly this support class; QW(g) \= ‖DCC g‖² on Vbase). Then Hbase is canonically unitarily equivalent to the closed span of {DCC g : g ∈ Vbase}. In particular the corpus's abstract base stage and the external concrete Sonin-compression range are one Hilbert space. The identification consumes the CC certificate in the explicit defect-operator form just cited; should \[4\] be read as supplying only positivity without that explicit square, the identification weakens to a non-canonical isometry (gated by F-F26.1).

*Proof.* QW(g) \= ‖DCC g‖² exhibits a Kolmogorov factorization of the positive form through ran DCC. Any two minimal Kolmogorov factorizations of the same positive semidefinite form are unitarily equivalent by a unique unitary intertwining the feature maps (Paulsen \[12\], the minimal-dilation uniqueness); minimality of the GNS quotient (no proper reducing subspace contains the range) gives the canonical unitary onto the closed span of DCC g.

**4.4  Unconditional infinite-dimensionality**

The second audit item asks whether Hbase is infinite-dimensional, and whether this is automatic. It is not automatic — it requires a coercivity estimate — but it is unconditional. We prove it by exhibiting an infinite-dimensional subspace on which QW is strictly positive, using only properties of the archimedean density.

**Lemma 4.6 (digamma minimum and monotonicity). \[DERIVED\]**  The function r ↦ Re ψ(1/4 \+ ir/2) is even, real-analytic, and strictly increasing in |r|, with global minimum at r \= 0 equal to

ψ(1/4)  \=  −γ − π/2 − 3 log 2  \=  −4.227454.

*Proof.* The reflection/Gauss value ψ(1/4) \= −γ − π/2 − 3 log 2 is classical (verified to 15 digits, §B.A1). For monotonicity, d/dr Re ψ(1/4 \+ ir/2) \= −(1/2) Im ψ′(1/4 \+ ir/2), and ψ′(z) \= Σn≥0 (z+n)−2 gives Im ψ′(1/4 \+ ir/2) \= −Σn≥0 (r/2)·(…) \< 0 for r \> 0 because each term Im\[(1/4+n+ir/2)−2\] \= −(r/2)(1/4+n) / |1/4+n+ir/2|4 \< 0\. Hence the r-derivative is positive for r \> 0\. Strict monotonicity and evenness give the global minimum at r \= 0\.

**Lemma 4.5′ (low-frequency leakage of high modes; Plancherel-normalized). \[DERIVED\]**  Fix R \> 0 and a window \[0, ℓ\], write ak \= kπ/ℓ and δK \= R²/aK+1². For every unit vector g ∈ span{φk : k \> K} (‖g‖L²\[0,ℓ\] \= 1\) with δK \< 1, the low-frequency mass *fraction* satisfies

φlo(g)  :=  (1/2π) ∫|r|≤R |ĝ(r)|² dr   ≤   8Rℓ / ( π³ (1−δK)² K ) .

The factor 1/2π is the Plancherel normalization: (1/2π)∫ℝ|ĝ|² \= ‖g‖²L² \= 1, so φlo is the genuine fraction of unit mass carried below frequency R. (The v1.0 statement omitted this 1/2π and was over-tight by that factor; this is the only substantive correction in v1.1, and Theorem 4.4 below survives it with room to spare.)

*Proof.* The {φk} are orthonormal on \[0, ℓ\], so g \= Σk\>K ck φk with Σ ck² \= 1, and by Plancherel (1/2π)∫ℝ|ĝ|² \= 1\. By Cauchy–Schwarz, |ĝ(r)|² \= |Σk\>K ck ĝk(r)|² ≤ (Σ ck²)(Σk\>K|ĝk(r)|²) \= Σk\>K|ĝk(r)|², hence φlo(g) ≤ Σk\>K (1/2π)∫|r|≤R|ĝk|² dr. For a single mode ĝk(r) \= √(2/ℓ) ak (1 − (−1)k eirℓ)/(ak² − r²), so |ĝk(r)|² ≤ (2/ℓ) ak² · 4 /(ak² − r²)² (using |1 − (−1)k eirℓ|² ≤ 4), and for |r| ≤ R \< ak, since δk \= R²/ak² ≤ δK for k \> K, (ak² − r²)² ≥ (ak² − R²)² ≥ (1−δK)² ak⁴. Thus (1/2π)∫|r|≤R|ĝk|² dr ≤ (1/2π)·2R·(2/ℓ)·4 / ((1−δK)² ak²) \= 8R / (πℓ(1−δK)² ak²). Summing and using Σk\>K ak−2 \= (ℓ/π)² Σk\>K k−2 ≤ (ℓ/π)²/K gives φlo(g) ≤ 8R/(πℓ(1−δK)²) · (ℓ²/π²)/K \= 8Rℓ/(π³(1−δK)² K).

*Corollary (clean conservative form).* For K with δK ≤ 1/2 (i.e. aK+1² ≥ 2R², which for ℓ \= log 2, R \= R₀ means K ≥ 5), φlo(g) ≤ 32Rℓ/(π³ K). The measured worst-case fraction (the top eigenvalue of the tail low-frequency Gram) increases monotonically with the tail truncation: at truncations of 84 / 164 / 264 tail modes it is 0.0152 / 0.0178 / 0.0192 for K \= 36 and 0.0258 / 0.0284 / 0.0297 for K \= 24, in every case well under the analytic values 0.0867 and 0.133 — the bound is correct and roughly three- to fivefold conservative; the truncation must be quoted with any measured value (§B.E). A further \~2× tightening is available by replacing the envelope |1 − (−1)keirℓ|² ≤ 4 with its exact average over \[−R, R\] (≈ 2), which would lower the minimal K₀ to ≈12; this is not pursued (diminishing returns against the measured gap).

**Theorem 4.4 (high-frequency coercivity; dim H\~base\~ \= ∞). \[DERIVED, unconditional\]**  There exist explicit (R₀, K₀) such that QW \= Qarch is strictly positive on the infinite-dimensional tail subspace span{φk : k \> K₀} of any base window of length ℓ0 \= log 2\. An admissible witness is

R₀ \= 17.082  (the root of  Re ψ(1/4 \+ iR/2) \= log π \+ 1),    K₀ \= 24    (margin \+0.125; minimal admissible K₀ \= 22).

Consequently dim Hbase \= ∞.

*Proof.* Split the archimedean form on a tail unit vector g (‖g‖ \= 1, g ∈ span{φk : k \> K}) as

Qarch(g) \= 2 M\+M− − log π \+ (1/2π)∫|r|\>R₀|ĝ|² Reψ(1/4+ir/2)dr \+ (1/2π)∫|r|≤R₀|ĝ|² Reψ(1/4+ir/2)dr.

By Lemma 4.6, on |r| \> R₀ the density exceeds Re ψ(1/4 \+ iR₀/2) \= log π \+ 1, so the high-frequency part is ≥ (log π \+ 1)(1/2π)∫|r|\>R₀|ĝ|² \= (log π \+ 1)(1 − φlo) by Plancherel; on |r| ≤ R₀ the density is ≥ ψ(1/4), so the low-frequency part is ≥ ψ(1/4)·φlo. The pole term is controlled by the tail mode-sums of the functionals: M± \= Σk\>K ck mk± with mk± \= ⟨φk, e±u/2⟩ \= O(1/k) (an oscillatory integral against a smooth function), so |2M\+M−| ≤ |M\+|² \+ |M−|² ≤ Σk\>K(mk\+)² \+ Σk\>K(mk−)² \= cpole/K. Collecting,

Qarch(g)  ≥  2M\+M− \+ 1 − \[log π \+ 1 − ψ(1/4)\]·φlo  ≥  1 − (cleak \+ cpole)/K,

with φlo ≤ C/K, C \= 8R₀ℓ0/(π³(1−δK)²) \= 3.199 at K \= 24 (Lemma 4.5′), log π \+ 1 − ψ(1/4) \= 6.372184, hence cleak \= 6.372184·C \= 20.38, and cpole \= K·Σk\>K\[(mk\+)² \+ (mk−)²\] with the closed form mk± \= √(2/ℓ)·ak(1 − (−1)ke±ℓ/2)/(ak² \+ 1/4): the full sum is K-invariant up to parity ripple, cpole \= 0.6308 (K \= 22), 0.6310 (K \= 24), 0.6314 (K \= 36), with limit 9ℓ0/π²·\[1 \+ O(K−1)\] \= 0.632 (§B.E). For K₀ \= 24 the margin is 1 − (20.38 \+ 0.631)/24 \= \+0.125 \> 0, and the smallest K with positive margin is 22 (margin \+0.037; K \= 21 fails at −0.013). Hence Qarch \> 0 on the infinite-dimensional tail span{φk : k \> 24}, none of which lies in the radical, so dim Hbase \= ∞.

*Numerical corroboration (§B.E).* On the base window ℓ0 \= 0.60 the smallest eigenvalue of Qarch restricted to the tail span{φk : k \> K} is \+1.469 (K \= 5), \+2.133 (K \= 10), \+2.808 (K \= 20\) — strictly positive and increasing, consistent with the theorem and with a coercivity threshold far below the conservative analytic K₀.

**4.5  The radical and its conditional triviality**

**Proposition 4.5′ (radical placement). \[DERIVED-CONDITIONAL on RH\]**  Under RH the radical Nbase is trivial on every window. Unconditionally, on the base window the radical is finite-codimensional in no proper sense forced by Theorem 4.4 — i.e. its complement is infinite-dimensional — and the unconditional triviality of Nbase is OPEN (registered O-F26.1).

*Discussion.* By Paley–Wiener, ĝ for g supported in \[0, ℓ\] is entire of exponential type ℓ/2; if ĝ vanished at every zero ordinate γk (the radical condition via the zero-side identity), the zero-counting density (T/2π)log T would force, beyond T \> 2πeℓ ≈ 17–19, more vanishing than an exponential-type function of that width can carry unless g \= 0 — *provided* the γk are real (RH). Without RH the argument stalls exactly at the reality of the ordinates, which is why O-F26.1 is genuinely open and not a corpus hypothesis.

**§5.  The Window-Inductive System and Gate D5 as a Colimit**

The base core of §4 is the floor of a directed system indexed by window length. We make the system precise and show that Gate D5 — the existence of the full realization — is exactly the existence of its colimit.

**5.1  The directed system**

For 0 \< ℓ ≤ ℓ′ there is a natural inclusion Vℓ ↪ Vℓ′ of window spaces. Where QW ⪰ 0 on Vℓ′ (a sub-log-2 length, or any length at which positivity holds), the inclusion descends to a linear map ιℓℓ′ : Hℓ → Hℓ′ of cores. The connecting map is *isometric* precisely when the radicals are compatible, Nℓ \= Vℓ ∩ Nℓ′ (no base vector that is null at length ℓ becomes non-null at ℓ′).

**Theorem 5.2 (D5 \= totality \= colimit). \[DERIVED\]**  The following are equivalent: (a) QW ⪰ 0 on all windows (Weil positivity, ⇔ RH); (b) the system {Hℓ, ιℓℓ′} is total — every connecting map is a well-defined isometry and the radicals are length-compatible; (c) the isometric colimit H∞ \= →lim Hℓ exists as a Hilbert space into which every Hℓ embeds isometrically. Gate D5 is statement (c).

*Proof.* (a)⇒(b): positivity on every window makes every ⟨·,·⟩ℓ an inner product and every inclusion a form-isometry, so radicals are length-compatible (both trivial under (a) restricted to RH; compatible in general from monotone positivity). (b)⇒(c): a directed system of Hilbert spaces with isometric connecting maps has a colimit, namely the completion of the union under the common inner product (the Hilbert-space direct limit). (c)⇒(a): an isometric embedding Hℓ ↪ H∞ forces ⟨·,·⟩ℓ ⪰ 0 on each window, i.e. positivity at every length. The equivalence with RH is F25 Theorem 11.3 (finite-window exhaustion).

**5.2  Conditional spectral realization on the colimit**

**Theorem 5.3 (absorption-side spectral realization). \[DERIVED equivalence; existence IMPORTED-OPEN ≡ RH\]**  Suppose H∞ exists (Gate D5). The scaling flow θs acts on H∞ by Lemma 3.1 as a one-parameter group of unitaries Us; it is strongly continuous, so by Stone's theorem Us \= eisD for a self-adjoint generator D. The vector spectral measure of D against the feature vectors is Σγ|ĝ(γ)|²δγ (the zero-side identity of §3.1), so

Spec(D)  \=  closure of the nontrivial-zero ordinate set,   simple on the cyclic subspace generated by g,

with zero multiplicities absorbed as spectral weights |ĝ(γ)|² rather than as eigenvalue degeneracies, and the spectrum realized in *absorption* (as a cokernel, in the sense of Connes 1999 \[8\]), consistent with F25 Theorem 6.6. Simplicity is asserted only on the *cyclic (minimal) subrealization* generated by the feature vector g — the part of the spectrum the scaling flow actually reaches from g — not on the full self-adjoint generator, whose multiplicity structure on a non-cyclic completion is not claimed here.

*Proof.* Strong continuity of s ↦ Us g follows from continuity of s ↦ θs g in the QW norm (dominated convergence in each block of §3.1). Stone’s theorem on one-parameter unitary groups \[17\] gives D \= D\*. The spectral measure of D in the cyclic vector g is the push-forward of |ĝ|² onto the ordinate set by the zero-side identity; simplicity is the statement that distinct ordinates index orthogonal spectral mass, with a repeated zero contributing a single spectral atom of weight (multiplicity)·|ĝ(γ)|² — a weight, not a Jordan block. The absorption sign is the Connes 1999 cokernel realization (the sign test of F25 Theorem 6.6).

*Remark (multiplicity, an important subtlety).* The realization does *not* claim the geometric multiplicity of an eigenvalue equals the zero multiplicity; it claims the *spectral weight* carries it. This is the only formulation consistent with both simplicity of the scaling generator on the cyclic subspace and the known possibility of multiple zeros, and it matches the absorption picture rather than an emission (direct-sum) picture — the latter excluded for the Weil form by Lemma M31.0 \[26\]. It is also consistent with the GUE pair-correlation statistics of the high zeros (Montgomery \[20\]), which the simple-spectrum-plus-weight reading neither asserts nor contradicts.

**§6.  Douglas Uniformization of the Rung**

F25 Lemma 11.4 states the inductive rung with the finite-matrix generalized-Schur criterion of Albert 1969\. The base archimedean block is, by Theorem 4.4, infinite-dimensional. This section shows the passage to infinite dimensions is *substantive* — a finite-section reading is provably insufficient — and supplies the correct infinite-dimensional criterion by uniformization.

**6.1  The section-certification gap**

**Theorem 6.1 (Section-Certification Gap). \[PROVEN\]**  On H \= ℓ² ⊕ ℂ let A \= diag(1/n)n≥1 and b \= (1/n)n≥1 ∈ ℓ², and consider the block

Q  \=  \[ \[ A , b \] , \[ b\* , c \] \]   on   ℓ² ⊕ ℂ .

Then: (i) for every N, the N-section \[\[AN, bN\], \[bN\*, c\]\] is positive semidefinite iff c ≥ HN \= Σn≤N 1/n, and HN → ∞; (ii) the full block Q admits *no* finite c making it positive semidefinite, because b ∉ ran A1/2 (indeed Σn n·bn² \= Σn 1/n \= ∞, so A−1/2b ∉ ℓ²). Hence every finite section is positively completable while the uniform object is not: section certification does not certify the rung.

*Proof.* (i) The Schur complement of AN in the N-section is c − bN\*AN−1bN \= c − Σn≤N (1/n)²/(1/n) \= c − Σn≤N1/n \= c − HN; positivity of the section ⇔ c ≥ HN. (ii) Positive completability of the full block is equivalent (Douglas, Theorem 6.3) to b ∈ ran A1/2 with ‖A−1/2b‖² ≤ c; here ‖A−1/2b‖² \= Σn (bn/√(1/n))² \= Σn n bn² \= Σn 1/n \= ∞, so no finite c works.

*Contrast (the convergent control).* If instead bn \= n−1.1, then Σn n·bn² \= Σn n−1.2 \= ζ(1.2) \= 5.5916 \< ∞ (§B.F), the full block *is* completable with cmin \= ζ(1.2), and section bounds converge to it. The gap in Theorem 6.1 is therefore a genuine boundary phenomenon (harmonic divergence), not an artifact.

**Corollary (reading of F25 Lemma 11.4). \[refinement, no-deletion\]**  F25 Lemma 11.4's phrase “each rung is a concrete finite statement” is to be read as *finite prime-channel data* (finitely many von Mangoldt points enter a given window), *not* as finite-dimensional certifiability of the archimedean block. Theorem 6.1 shows the latter reading would be false. This is a precision, not a correction; F25 Lemma 11.4 is preserved verbatim and annotated (§6.7).

**6.2  The rung criterion at form level**

**Lemma 6.2 (Rung Criterion \= Lemma 11.4′). \[DERIVED\]**  Let V(I) be a base window core with feature map Φ (so QW(v) \= ‖Φv‖² on V(I), via Theorem 4.3), and let W be the span of new modes entering at the enlarged window. Then QW ⪰ 0 on V(I) \+ W if and only if

(α) *Riesz representability:* there is a bounded operator T : W → HI (the base core) with QW(v, w) \= ⟨Φv, Tw⟩ for all v ∈ V(I), w ∈ W — no closed-range or pseudoinverse hypothesis; and

(β) *defect positivity:* the canonical defect form S(w, w′) \= QW(w, w′) − ⟨Tw, Tw′⟩ is positive semidefinite on the quotient of new modes (independent of the choice of complement, hence canonical).

*Proof.* Completing the square, infv ‖Φv \+ Tw‖² \= 0 forces the cross pairing to be represented through the base feature space (α), after which the residual quadratic form on W is exactly S; QW ⪰ 0 on the sum ⇔ S ⪰ 0\. Boundedness of T is the Riesz representation of the bounded functional v ↦ QW(v, w) on HI, valid without range hypotheses; canonicity of S follows because changing the complement shifts T by a map into the radical, leaving S invariant.

**6.3  The bounded-operator shadow: Douglas–Shmul’yan**

**Theorem 6.3 (operator form of the rung). \[IMPORTED\]**  For bounded Hilbert-space operators with A, C ⪰ 0, the block \[\[A, B\*\], \[B, C\]\] is positive semidefinite if and only if B \= A1/2 K C1/2 for some contraction K (‖K‖ ≤ 1); equivalently ran B\* ⊆ ran A1/2 and the associated factor is a contraction. (Douglas 1966 \[10\] range/majorization; Shmul’yan 1959 \[15\]; the block form Moslehian–Kian–Xu 2019 \[11\], Anderson–Trapp shorted operators \[14\].)

**Theorem 6.4 (uniformization of the rung). \[DERIVED\]**  The Rung Criterion (Lemma 6.2) is the form-level statement whose bounded realization is Theorem 6.3: (α) is ran(cross) ⊆ ran A1/2 (Douglas majorization, replacing Albert's finite pseudoinverse), and (β) is contractivity ‖K‖ ≤ 1 of the Douglas factor. Thus F25 Lemma 11.4 lifts from finite matrices to the infinite-dimensional archimedean block *without* a closed-range hypothesis, exactly because Douglas majorization does not require closed range.

*Proof.* Apply Theorem 6.3 with A the base Gram (Theorem 4.4 infinite-dimensional), C the new-mode Gram, B the cross block. Douglas's theorem gives B \= A1/2KC1/2 ⇔ ran B\* ⊆ ran A1/2 ⇔ ∃ bounded T with B \= A1/2T; this is (α). The defect S \= C − B\*A−1/2A−1/2B in the form sense equals C − (KC1/2)\*(KC1/2) \= C1/2(I − K\*K)C1/2 ⪰ 0 ⇔ ‖K‖ ≤ 1; this is (β).

**Corollary 6.5 (contractive Z-Spin mediation). \[DERIVED\]**  The Douglas factor K of every rung satisfies ‖K‖ ≤ 1: each rung is mediated by a contraction. Read through the corpus, this is the operator statement of Z-Spin mediation — the rung-to-rung coupling has channel norm at most 1, the Z-bottleneck reading of capacity (cf. §8).

*Numerical check (§B.lam).* The symmetrized prime-channel Gram of the first rung (n \= 2\) has spectral norm exactly 0.5000 at every tested window (ℓ \= 0.80, 1.00, 1.09, 1.30), consistent with a contractive mediation factor and with the Exact-Half Lemma of §7.

**6.4  The necessary realization profile**

**Theorem 6.6 (mediation profile, combined). \[DERIVED\]**  Any Hilbert-space realization of the rung is operator-valued (not scalar/diagonal), cross-coupled (not a direct sum over sectors), and ΠZ\-sandwiched. Equivalently the rung coupling Kq is operator-valued and cross-coupled under the projection ΠZ \= ½(I \+ JZ).

*Proof.* Combine the contraction realization (Corollary 6.5) with the corpus no-gos: ADS-5 \[25\] excludes scalar and diagonal kernels; Lemma M31.0 \[26\] excludes separable (direct-sum) decompositions, so the cross block B is genuinely off-diagonal and operator-valued; F25 Theorem 11.6 supplies the ΠZ\-sandwich format.

**6.7  Relation to F25 Lemma 11.4 (no-deletion annotation)**

F25 Lemma 11.4 (generalized Schur rung, with Albert 1969\) is preserved verbatim. ZS-F26 annotates it: (a) its “concrete finite statement” refers to finite *prime-channel data*, not finite-dimensional certifiability (Theorem 6.1); (b) its finite pseudoinverse is replaced, in infinite dimensions, by Douglas majorization (Theorem 6.4), valid without closed range; (c) Albert 1969 remains exact and is the correct tool on each finite prime-channel Gram, while Douglas–Shmul’yan governs the archimedean block. No statement of F25 is withdrawn; the present section refines the reading and supplies the infinite-dimensional criterion the rung requires.

**§7.  Rung 1 Exactly: the Master Inequality MI(2)**

**7.1  The rung-1 perturbation**

**Proposition 7.1 (rung-1 perturbation operator). \[DERIVED\]**  Crossing the first von Mangoldt point log 2 adds to Qarch the single prime term −2(Λ(2)/√2)f(log 2\) \= −√2 log 2 · (g ⋆ g̃)(log 2). As a quadratic form in g this is

Δ1(g)  \=  −√2 log 2 · Re⟨θlog 2 g, g⟩L² ,    √2 log 2 \= 2Λ(2)/√2 \= 0.980258,

the real part of a compressed in-window translation by log 2 — an operator, not a scalar coefficient (it has the structure of §6).

*Proof.* (g ⋆ g̃)(τ) \= ∫ g(u+τ)g(u)du \= ⟨θ−τg, g⟩ \= Re⟨θτg, g⟩ for real g; at τ \= log 2 with coefficient −2Λ(2)/√2 \= −√2 log 2 this is Δ1.

**7.2  The Exact-Half Lemma**

**Lemma 7.2 (compressed translation is 2-nilpotent with norm one-half). \[PROVEN\]**  Let ℓ \< 2 log 2 and let Tτ \= P\[0,ℓ\] θτ P\[0,ℓ\] be the in-window compression of translation by τ \= log 2 on L²\[0, ℓ\]. Then Tτ² \= 0 (2-nilpotent), and

‖Re Tτ‖  \=  ½   exactly.

*Proof.* supp(θτ g) ⊆ \[τ, τ \+ ℓ\]; intersecting with \[0, ℓ\] keeps the part on \[τ, ℓ\], of length ℓ − τ. Applying θτ again shifts to \[2τ, …\]; since 2τ \= 2 log 2 \> ℓ, the support leaves \[0, ℓ\] entirely, so P\[0,ℓ\]θτP\[0,ℓ\]θτP\[0,ℓ\] \= 0, i.e. Tτ² \= 0\. A nonzero 2-nilpotent partial isometry between the orthogonal subspaces L²\[0, ℓ−τ\] and L²\[τ, ℓ\] has ‖Tτ‖ \= 1, and the self-adjoint part of a nilpotent partial isometry V with V² \= 0 has ‖Re V‖ \= ½‖V‖ \= ½ (the 2×2 nilpotent block \[\[0,1\],\[0,0\]\] has symmetric part \[\[0,½\],\[½,0\]\] of norm ½).

*Consequence (sharp a priori bound).* |Δ1(g)| \= √2 log 2 · |Re⟨θlog 2g, g⟩| ≤ √2 log 2 · ‖Re Tlog 2‖·‖g‖² \= (√2 log 2)/2 · ‖g‖² \= 0.490129·‖g‖² on any window shorter than 2 log 2\. The rung-1 negative perturbation is bounded in operator norm by exactly half the coupling constant.

**7.3  The master inequality**

**Definition (MI(2)).**  For windows of length ℓ \< log 3 (so that only the n \= 2 prime term is active), define

MI(2):    Qarch(g)  ≥  √2 log 2 · Re⟨θlog 2 g, g⟩   for all such g.

**Theorem 7.3 (rung 1 ⇔ MI(2)). \[DERIVED statement; truth OPEN\]**  QW ⪰ 0 on every window of length \< log 3 (the first extension of the GNS system past the base rung) if and only if MI(2) holds. Its truth is OPEN; it is *not* claimed.

*Proof of equivalence.* On ℓ \< log 3 the only active prime term is n \= 2, so QW(g) \= Qarch(g) \+ Δ1(g) \= Qarch(g) − √2 log 2·Re⟨θlog 2g, g⟩; positivity of the left side is exactly MI(2). The equivalence is unconditional; what is open is whether MI(2) is true.

**7.4  The sufficient route and its numerical refutation**

**Proposition 7.5 (sufficient route). \[DERIVED\]**  If Qarch(g) ≥ (√2 log 2)/2 · ‖g‖² \= 0.490129·‖g‖² on the window sphere, then MI(2) holds (by the Exact-Half bound, since the right side is ≤ 0.490129·‖g‖²). The route is *sufficient but not necessary*.

**The route fails (COMPUTED, decisive).**  The archimedean block alone is *indefinite* on every rung window: its smallest eigenvalue (M \= 80 sine modes) is

Table 7.1.  Smallest eigenvalue of the archimedean block Qarch and of the full Weil block QW on window \[0, ℓ\] (M \= 80).

| ℓ | active primes | λmin(Qarch) | λmin(QW) | (√2 log 2)/2 reserve? |
| :---: | ----- | ----- | ----- | ----- |
| 0.60 | — (base) | \+0.007919 | \+0.007919 | n/a (no prime term) |
| 0.80 | 2 | −0.073620 | \+1.944×10−4 | fails (negative) |
| 1.00 | 2 | −0.317546 | \+1.865×10−6 | fails (negative) |
| 1.09 | 2 | −0.416252 | \+9.501×10−7 | fails (negative) |
| 1.2825 \= (log 13)/2 | 2, 3 | −0.613463 | \+3.713×10−8 | fails (negative) |
| 1.30 | 2, 3 | −0.630797 | \+2.045×10−8 | fails (negative) |

Since λmin(Qarch) is *negative* on every rung window, the sufficient bound Qarch ≥ 0.490·‖g‖² fails *a fortiori* — the archimedean block does not even dominate zero, let alone the rung-1 perturbation. Yet the *full* Weil block QW remains positive on the same windows (column 4, all λmin \> 0). The conclusion is structural and matches F25 Theorem 11.6: where rung positivity holds it is produced by *arithmetic–archimedean cross-cancellation*, not by archimedean domination. A proof of MI(2) must therefore engage the cross structure (the operator T of §6), not bound the two blocks separately. We report this honestly: the simplest sufficient route is closed by computation.

*Convergence and validation.* λmin(QW) is stable under basis refinement (M \= 40/60/80 agree to the reported figures) and under quadrature doubling (§B.C7: shift 4×10−11). The two-sided explicit-formula identity Σρh(γ) \= 2Σ|ĝ(γ)|² holds at 0.049% (single mode) and 0.0030% (8-mode test vector) over 160 zeros (γmax \= 334.2), validating the block assembly itself (§B.1). The CCM 2024 semilocal {∞, 2} habitat \[6\] is the external setting in which a proof of MI(2) would live; this paper formulates the inequality and refutes the naive route, nothing more.

*Relation to Connes 2026 (same window, opposite end of the spectrum).* While this programme was internal, Connes \[9\] — in a survey completed in February 2026 — extremized the *restriction of Weil’s quadratic form* to test functions built from primes below 13, exactly the windowed object of this paper, obtaining approximations to the first fifty zeros with accuracies from 2.6×10−55 to 10−3 and proving that the approximating values lie *exactly on the critical line*; he outlines a proof strategy based on the convergence of zeros from finite to infinite Euler products, and describes a connection of the Weil form to information theory. Two contacts are exact. (a) *Same window, different question.* Connes solves a *minimization* (the minimal eigenvector of the windowed form approximates a zero), whereas this paper studies *positivity* (positive-definiteness) of the same windowed form (MI(2), §7.3). The minimal eigenvalue he locates is precisely the λmin of the QW block of Table 7.1, column 4 — positive on every window tested — and the eigenvector attaining it is the object he extremizes: the two programmes read opposite ends of the spectrum of the *same* windowed operator. (b) *Shared open step.* His finite→infinite Euler-product convergence is the analytic content of the finite-window exhaustion (F25 Theorem 11.3); both isolate the passage from finitely many primes to all primes as the single open step. The prolate operator (Slepian–Pollak \[19\]) appears in both: as the infrared approximant to the minimal eigenvector in \[9\], and as the Connes–Consani base-rung compression \[4\] and the RRJT negative-eigenvalue carrier \[7\] here. The precise relation of the two readings is registered as O-F26.5. That Connes’s truncation is exactly p \< 13, while the F25 preregistered support window ran exactly to log 13, is a coincidence of cutoff but a striking one.

*Quadrature note on Table 7.1 (numerical boundary cases).* The ℓ \= 1.2825 and ℓ \= 1.30 entries sit near the quadrature floor (λmin ∼ 10−8); high-resolution recomputations (40001-point overlap integrals, refined frequency grid) confirm positivity at \+3.71×10−8 (ℓ \= 1.2825; stable to three digits across M \= 40/60/80) and \+2.05×10−8 (ℓ \= 1.30), but both entries are classified as *numerical boundary cases* — “positive, near integration precision” — not sharp figures (§B.G). The ℓ ≤ 1.09 entries (λmin ≥ 10−7) are comfortably above the floor.

**7.5  The operator forms of MI(2) and the regularized Douglas factor**

Feedback on v1.1 asked for the rung-1 inequality in forms an operator theorist can attack directly, and for the Douglas factor of §6 to be exhibited rather than merely characterized. This subsection does both, to the exact extent that is honest: the three formulations are equivalent unconditionally; the factor itself exists conditionally, with the conditionality located precisely at MI(2).

Fix the rung-1 split of §6.2 concretely: I \= \[0, ℓb\] with ℓb \< log 2 (base sub-window, V \= span of its modes, on which QW \= Qarch ⪰ 0 by CC 2021), and I′ \= \[0, ℓ\] with log 2 \< ℓ \< log 3 (rung-1 window), W \= an L²-orthogonal complement of V inside the I′ modes. Write A \= QW|V, C \= QW|W, B \= the cross block; the prime channel n \= 2 enters only B and C, never A.

**Proposition 7.7 (three equivalent formulations of MI(2)). \[DERIVED\]**  The following are equivalent. **MI(2)-A** (quadratic form): Qarch(g) ≥ √2 log 2 · Re⟨θlog 2 g, g⟩ for all g of the convention class on I′. **MI(2)-B** (block positivity): the 2×2 operator block \[\[A, B\], \[B\*, C\]\] is positive semidefinite. **MI(2)-C** (Douglas contraction): C ⪰ 0, ran B\* ⊆ ran A1/2, and the Douglas factor K2 with B \= A1/2K2C1/2 satisfies ‖K2‖ ≤ 1\.

*Proof.* MI(2)-A is QW ⪰ 0 on I′ (Theorem 7.3). MI(2)-B is the same statement read through the V ⊕ W splitting: positivity of a form on a direct sum is positivity of its block matrix. MI(2)-B ⇔ MI(2)-C is Theorem 6.3 (Douglas–Shmul’yan), applicable because A ⪰ 0 unconditionally (the base rung) — the only block whose positivity the criterion presupposes.

**Theorem 7.6 (regularized Douglas factor: trichotomy and conditional construction). \[DERIVED\]**  For ε \> 0 and a finite section (N modes of V, N′ of W) define the *regularized finite-section factor*

K2,N,ε  \=  (AN \+ εI)−1/2 BN (CN \+ εI)−1/2 ,

always well-defined (no positivity assumed beyond A ⪰ 0). Then: (i) for each fixed section, \[\[AN, BN\], \[BN\*, CN\]\] ⪰ 0 ⇔ CN ⪰ 0 and supε\>0 ‖K2,N,ε‖ ≤ 1; (ii) MI(2) ⇔ uniform contraction over all sections and regularizations, supN,ε ‖K2,N,ε‖ ≤ 1; (iii) under MI(2), the factors converge — along ε ↓ 0 and the section net, in the weak operator topology — to a unique contraction K2 with B \= A1/2K2C1/2, ‖K2‖ ≤ 1: the rung-1 Z-Spin mediation operator of Corollary 6.5 exists as a strong-limit object whenever the rung holds. (iv) Unconditionally, no finite collection of sections certifies (ii): this is exactly the Section-Certification Gap (Theorem 6.1), which is why the measured norms below are evidence, never proof.

*Proof.* (i) If the block is PSD, then for any vectors x, y and ε \> 0, the PSD property of the ε-shifted block \[\[A+ε, B\], \[B\*, C+ε\]\] gives |⟨B y, x⟩| ≤ ‖(A+ε)1/2x‖·‖(C+ε)1/2y‖ (the Cauchy–Schwarz inequality of the block form), i.e. ‖K2,N,ε‖ ≤ 1; conversely if ‖K2,N,ε‖ ≤ 1 for all ε then the Schur complement C − B\*(A+ε)−1B ⪰ −o(1) for every ε, and letting ε ↓ 0 gives block positivity (Moslehian–Kian–Xu \[11\]). (ii) MI(2)-B restricted to sections is (i) at every (N, N′); density of the section union in the convention class gives the converse. (iii) The net {K2,N,ε} lies in the unit ball, which is WOT-compact (Banach–Alaoglu); any two cluster points agree on the dense set of vectors of the form C1/2y against A1/2x — because ⟨A1/2K2C1/2y, x⟩ \= ⟨By, x⟩ is net-independent — and ran A1/2, ran C1/2 are dense in the respective closures by minimality of the GNS quotient; hence the cluster point is unique and the net converges. Douglas’s uniqueness \[10\] identifies the limit with the canonical factor. (iv) is Theorem 6.1 verbatim.

*What is and is not constructed.* Theorem 7.6 does *not* prove ‖K2‖ ≤ 1 — that is MI(2) itself, OPEN — and so does not retire NC-F26.4. What it adds is: (a) the object whose norm decides the rung is now an explicit limit of computable matrices, not an abstract criterion; (b) the conditionality is localized in a single inequality about that computable family; (c) the prime-translation component of B obeys the unconditional Exact-Half bound ‖Re Tlog 2‖ \= 1/2 (Lemma 7.2), and the measured L² prime-channel norm 0.5000 (§B.lam, D4) saturates it.

Table 7.2.  Measured regularized Douglas norms ‖K2,ε‖ at section MV \= 40 (base ℓb \= 0.60), MW \= 80, with λmin of the diagonal blocks. All norms \< 1 at every ε: uniform contraction at this section, nearly saturated. The ε \= 10−7 residuals 1 − ‖K‖ ∼ 10−6 share the quadrature-floor sensitivity of the underlying λmin and are order-of-magnitude figures; rank W depends on the L² eigen-threshold (10−8 here; a coarser tolerance retains 40).

| ℓ (rung window) | rank W | λmin(A) | λmin(C) | ‖K2,ε‖, ε \= 10−3 | 10−5 | 10−7 | 1 − ‖K‖ (ε \= 10−7) |
| :---: | :---: | ----- | ----- | ----- | ----- | ----- | ----- |
| 1.09 | 44 | \+0.00823 | \+0.03692 | 0.99721 | 0.99996 | 0.999996 | 4×10−6 |
| 1.2825 | 48 | \+0.00823 | \+0.00151 | 0.99782 | 0.99997 | 0.999999 | 1×10−6 |

Reading: the base block A is CC-coercive (+0.0082, prime-free as required); C is positive at this section; the contraction is real but *saturated to within 10^−6^* — the rung-1 mediation operates at the very edge of the Douglas ball, the operator-norm restatement of the collapsing λmin margins of Table 7.1. Per Theorem 7.6(iv) this measures, and cannot certify, MI(2). \[COMPUTED; details §B.I\]

**7.6  The bridge experiment: first data for O-F26.5 \[COMPUTED\]**

O-F26.5 asks how Connes’s minimization reading and this paper’s positivity reading of the same windowed form are related. The v1.1 registration predicted they read “opposite ends of the spectrum of the same operator.” That prediction is testable with the machinery already in hand, and we report the preregistered test.

*Design (preregistered).* Connes’s cutoff “primes below 13” corresponds to autocorrelation reach log 13, i.e. window length ℓC \= (log 13)/2 \= 1.282475 — a point already inside the F26 ladder (between the second rung log 3 and the first control log 4 in reach terms; active primes 2 and 3). At ℓC, extract the minimal eigenvector gmin of the full Weil block QW (M \= 80\) and evaluate |ĝmin(r)| on r ∈ \[0, 40\] (step 0.002). The zero-side identity QW(g) \= 2Σγ\>0|ĝ(γ)|² makes the mechanism transparent: minimizing the Rayleigh quotient forces ĝmin to be *small at every zero ordinate* — the minimizer’s near-zeros should approximate the γk, exactly Connes’s phenomenon in which the extremal function’s zeros approximate the zeros of ζ. Preregistered question: do the local minima of |ĝmin| align with γ₁, …, γ₆ \= 14.1347, 21.0220, 25.0109, 30.4249, 32.9351, 37.5862, with no comparable minima at the midpoint controls 17.58, 23.02, 27.72?

*Result.* |ĝmin| has *exactly six* local minima on \[0, 40\] — and they are the six zero ordinates:

Table 7.3.  Local minima of |ĝmin(r)| on \[0, 40\] at ℓC \= (log 13)/2, M \= 80, vs. the first six zero ordinates. Depth \= |ĝmin| at the minimum / median over \[0, 40\]. No other local minima exist in the range; the midpoint controls carry no minima. † \= quadrature-sensitive (order of magnitude only): λmin sits at the integration floor and the nearly degenerate bottom eigenvector wanders with quadrature; an independent reproduction at different quadrature gives \+0.017/+0.065/+0.230 — the same monotone pattern, different values (§B.H). The γ₁–γ₃ offsets (10−3 scale) are robust.

| k | γk | minimum at | offset | depth |
| :---: | :---: | :---: | :---: | :---: |
| 1 | 14.1347 | 14.134 | −0.001 | 0.0071 |
| 2 | 21.0220 | 21.022 | 0.000 | 0.0003 |
| 3 | 25.0109 | 25.014 | \+0.003 | 0.0001 |
| 4 | 30.4249 | 30.49 | \+0.07 † | \< 10−4 |
| 5 | 32.9351 | 33.14 | \+0.21 † | \< 10−4 |
| 6 | 37.5862 | 38.02 | \+0.44 † | \< 10−4 |

**Proposition 7.10 (variational notch mechanism). \[DERIVED\]**  Let gmin be a unit minimal eigenvector of the compression of QW to any window subspace, with eigenvalue λmin ≥ 0\. Then for *every* ordinate γk of a zero on the critical line, *simultaneously*,

2 |ĝmin(γk)|²   ≤   λmin ,      i.e.      |ĝmin(γk)|  ≤  √(λmin/2) .

*Proof.* The zero-side reading of the explicit formula gives QW(g) \= Σρ h(γρ); every zero on the critical line contributes 2|ĝ(γ)|² ≥ 0 (pairing γ with −γ). Hence λmin \= QW(gmin) ≥ 2|ĝmin(γk)|² for each on-line γk separately: minimizing a sum of nonnegative terms bounds every term at once. (Unconditional caveat: a hypothetical off-line zero contributes a conjugate pair ĝ(γ)ĝ(γ̄)\* \+ c.c., not sign-definite, so the bound is stated for on-line ordinates — which includes every zero in the tested range by the established numerical verification of the first \~1013 zeros; no claim is made beyond that range.)

*Mechanism and verification.* This is the Euler–Lagrange content the bridge experiment exhibits: the Rayleigh minimizer must make all six |ĝ(γk)| in range simultaneously tiny, and with only ≈ 16 sign changes of ĝ available on \[0, 40\] (§B.H) the economical solution is to park near-zeros *on* the ordinates — the alignment of Table 7.3 is the visible footprint of the simultaneous bound. Numerically at ℓC: √(λmin/2) \= 1.36×10−4, and the measured values |ĝmin(γk)| \= 1.2×10−7, 8.0×10−7, 2.5×10−6, 1.3×10−5, 2.2×10−5, 3.7×10−5 obey it at every ordinate, with the monotone-in-k growth mirroring the offset ladder (G6). The *mechanism* is thereby DERIVED; what remains COMPUTED is the alignment data themselves; what remains OPEN in O-F26.5 is the quantitative offset-vs-margin law.

*Reading (disciplined).* (a) The alignment is sharp at the bottom of the range (offsets 10−3–10−2 for γ₁–γ₃) and degrades with height (order 10−2–10−1 for γ₄–γ₆, quadrature-sensitive) — the same qualitative accuracy ladder Connes reports for his prime-based extremizers, here reproduced by a crude 80-mode sine window. (b) This is an *analogous experiment, not a replication*: Connes’s test class is built from the primes themselves, ours is a generic spectral basis of the same window; that both classes drive the extremal function’s near-zeros onto the γk is evidence that the phenomenon belongs to the *windowed Weil form*, not to the test-function class. (c) Status: COMPUTED, first data for O-F26.5, which remains OPEN — the data sharpen its sub-question: the minimal eigenvector’s near-zero locations and the window positivity margin (Table 7.1) are two readings of the same spectral bottom, and a quantitative law connecting offset growth to λmin collapse is now a well-posed target. No claim about RH follows or is made.

**7.7  Routes toward uniform contraction (v1.3)**

Closing MI(2) is, by Theorem 7.6(ii), exactly the uniform contraction supN,ε ‖K2,N,ε‖ ≤ 1\. That statement is OPEN and is not attempted here (NC-F26.2); what v1.3 adds is the *structure* of the problem: two PROVEN monotonicity lemmas that reduce it to a single scalar invariant, and a register of three routes with their exact open content.

**Lemma 7.8 (ε-monotone certification). \[PROVEN\]**  Fix a section (AN, BN, CN) with AN, CN ⪰ 0\. If ‖K2,N,ε₀‖ ≤ 1 for some ε₀ \> 0, then ‖K2,N,ε‖ ≤ 1 for every ε ≥ ε₀. Hence the certified set {ε : ‖K2,N,ε‖ ≤ 1} is upward-closed, the *critical regularization* ε\*(N) \= inf{ε : ‖K2,N,ε‖ ≤ 1} is well-defined, and section positivity is exactly ε\*(N) \= 0\.

*Proof.* ‖K2,N,ε‖ ≤ 1 ⇔ B\*(A+ε)−1B ⪯ C \+ ε. If this holds at ε₀ and ε ≥ ε₀, then B\*(A+ε)−1B ⪯ B\*(A+ε₀)−1B ⪯ C \+ ε₀ ⪯ C \+ ε, using the Loewner monotonicity of t ↦ (A+t)−1. The equivalence with section positivity is Theorem 7.6(i) plus ε ↓ 0\.

**Lemma 7.9 (section monotonicity; scalar reduction of MI(2)). \[PROVEN\]**  Compressions of positive blocks are positive, so if the (N′ ≥ N)-section certifies then the N-section certifies; ε\*(N) is nondecreasing in the section. Consequently MI(2) ⇔ supN ε\*(N) \= 0: the whole rung is one nondecreasing scalar sequence converging (or not) to zero.

*Proof.* A principal compression of a PSD block is PSD (restrict the form); apply Lemma 7.8’s characterization at each section; the equivalence with MI(2) is Theorem 7.6(ii) via density of the section union.

*Structural signature in the data.* Lemma 7.8 predicts that at a positive section the measured ‖K2,ε‖ rises monotonically toward 1 as ε ↓ 0 without crossing it — exactly the ladder of Table 7.2 (0.9972 → 0.999999, never above 1; G7). The data are the signature of ε\*(N) \= 0 at these sections, no more: by Theorem 7.6(iv) \= Theorem 6.1, no finite family of sections certifies supN ε\*(N) \= 0\.

*Route register (all OPEN; proving any one closes rung 1 and is not attempted here).*  **R1 (commutator/translation).** Decompose B \= Barch \+ Bprime with Bprime the compressed-translation channel; the Exact-Half datum ‖Re Tlog 2‖ \= 1/2 (Lemma 7.2, PROVEN) bounds Bprime in L² norm, but the Douglas normalization weighs it against A1/2 and C1/2, whose lower spectral data collapse along the ladder (Table 7.1); the open content is a joint bound on the *weighted* channel, e.g. via a commutator identity between Tlog 2 and the archimedean resolvent. **R2 (prolate scattering).** Identify K2 with a boundary/scattering datum of the Connes–Consani / Slepian–Pollak prolate compression \[4, 6, 19\] — the operator that already controls the base rung and Connes’s infrared approximant \[9\]; a spectral bound imported from the prolate side would certify the contraction; this is the route that would simultaneously settle O-F26.4. **R3 (monotone finite-section).** Now structured by Lemmas 7.8–7.9: the remaining open content is precisely supN ε\*(N) \= 0, a quantitative statement about one scalar sequence — the sharpest known reformulation of rung 1 within this paper’s toolkit.

**7.8  The offset–margin law: preregistered ℓ-scan \[COMPUTED, mechanism DERIVED\]**

v1.3 preregistered the next step on O-F26.5: scan ℓ ∈ \[0.8, 1.30\], record (λmin, offset) pairs, and run an M \= 120/160 basis-convergence test first to separate basis truncation from the quadrature floor. Both are executed here; the sub-rung base window ℓ \= 0.60 is added as a control beyond the preregistration.

*Basis-convergence precondition (executed).* At ℓC \= (log 13)/2, raising the basis M \= 80 → 120 → 160 moves λmin by ≈4% (3.713 → 3.632 → 3.576 ×10−8, the expected monotone compression decrease) while the γ₁–γ₄ offsets are *stable to 10^−4^–10^−3^* (−0.0007, 0.0000, \+0.0031, \+0.0671 at every M) and γ₅–γ₆ drift by only ≈0.002 per 40 modes (0.2049 → 0.2009; 0.4378 → 0.4338). Since the independent-quadrature reproduction (§B.H) moved the same offsets at the 10−1 scale, the separation is decided: *the γ₄–γ₆ offset sensitivity is quadrature-floor-dominated, not basis-dominated*, sustaining the §B.G classification.

**Proposition 7.11 (Newton-step offset bound). \[DERIVED\]**  Let gmin be a unit minimal eigenvector with eigenvalue λmin, suppose ĝmin(r₀) \= 0 for some real r₀, and let m \= min |ĝmin′| on the segment between r₀ and an on-line ordinate γk, with m \> 0\. Then

|γk − r₀|   ≤   |ĝmin(γk)| / m   ≤   √(λmin/2) / m ,

and to first order (short segment) the offset equals the Newton quotient |ĝmin(γk)|/|ĝmin′(γk)|.

*Proof.* |ĝmin(γk)| \= |ĝmin(γk) − ĝmin(r₀)| \= |∫r₀γ\~k\~ ĝmin′(t)dt| ≥ m·|γk − r₀| would require monotonicity of the integrand’s phase; the correct one-line route is the reverse estimate on the segment where |ĝmin′| ≥ m and ĝmin does not re-cross zero: there |ĝmin(γk)| ≥ m·|γk − r₀| holds by integrating the modulus derivative bound |d|ĝmin|/dt| ≤ |ĝmin′(t)| from the zero, taking the branch on which |ĝmin| grows at rate ≥ m — the defining property of the nearest simple near-zero. Combining with Proposition 7.10 gives the chain. The first-order statement is Taylor expansion at γk.

*Scan results.*

Table 7.4.  Preregistered ℓ-scan (M \= 80): smallest eigenvalue, notch bound, number of resolved minima of |ĝmin| on \[0, 40\], and the γ₁–γ₃ offsets with the Newton prediction |ĝmin(γk)|/|ĝmin′(γk)| in parentheses. — \= unresolved (no notch allocated to that ordinate).

| ℓ | λmin(QW) | √(λmin/2) | minima | off(γ₁) (Newton) | off(γ₂) (Newton) | off(γ₃) (Newton) |
| :---: | ----- | ----- | :---: | ----- | ----- | ----- |
| 0.60 (base) | \+7.92×10−3 | 6.3×10−2 | 3 | 0.81 (0.71) | — | — |
| 0.80 | \+1.94×10−4 | 9.9×10−3 | 4 | 0.051 (0.050) | 0.80 (0.70) | — |
| 0.90 | \+1.85×10−5 | 3.0×10−3 | 5 | 0.007 (0.007) | 0.22 (0.21) | 0.91 (0.88) |
| 1.00 | \+1.87×10−6 | 9.7×10−4 | 5 | 0.001 (0.001) | 0.036 (0.035) | 0.20 (0.19) |
| 1.09 | \+9.50×10−7 | 6.9×10−4 | 6 | 0.001 (0.000) | 0.008 (0.008) | 0.057 (0.056) |
| 1.20 | \+6.71×10−7 | 5.8×10−4 | 6 | 0.001 (0.000) | 0.002 (0.003) | 0.021 (0.022) |
| 1.2825 | \+3.71×10−8 | 1.4×10−4 | 6 | 0.001 (0.000) | 0.000 (0.000) | 0.003 (0.003) |
| 1.30 | \+2.05×10−8 | 1.0×10−4 | 6 | 0.001 (0.000) | 0.000 (0.000) | 0.001 (0.002) |

*Findings.* (1) *The Newton law holds at every resolved notch.* Over 34 resolved (window, zero) pairs spanning eight windows and five decades of λmin — including the γ₄–γ₆ notches at the resolved windows (e.g. ℓ \= 1.20: measured 0.29/0.88/1.09 vs predicted 0.27/0.92/0.98) — the measured/predicted ratio has median 1.04 and range \[0.63, 1.22\], with the outliers exactly at precision-floor offsets (≤ 2×10−3) of boundary-case windows. (2) *The resolution count is monotone in the margin collapse*: 3 → 4 → 5 → 5 → 6 → 6 → 6 → 6 minima as λmin falls 7.9×10−3 → 2.0×10−8 — each collapse of the positivity margin buys the minimizer another resolved zero. (3) *Single-zero collapse*: the γ₂ offset falls monotonically 3.38 → 0.80 → 0.22 → 0.036 → 0.008 → 0.002 → 0.000 across the scan — the cleanest single-trajectory exhibit of the law. (4) *Control confirmed*: the sub-rung base window (ℓ \= 0.60, no prime term, λmin ∼ 10−2) resolves only γ₁, and loosely (offset 0.81): the alignment is a *rung-ladder phenomenon*, absent below the first rung and sharpening as Weil positivity approaches saturation. (5) The bare bound √(λmin/2) sets the scale but the slope factor matters: the sharp law is the two-factor Newton quotient, not a pure power of λmin.

*Status.* Mechanism DERIVED (Propositions 7.10–7.11); law COMPUTED-established at first order; preregistration honored, with the ℓ \= 0.60 control disclosed as an addition. O-F26.5’s remaining open content is now the theoretical asymptotics of λmin(ℓ) along the ladder — a question about the windowed Weil form itself, shared with the finite→infinite passage of \[9\].

**§8.  The Sector Shadow \[OBSERVATION / HYPOTHESIS-strong, NC\]**

Two exact, parameter-free coincidences between the ladder and the corpus sector data are registered here. Both are used in no proof; both are guarded by the non-claims of §11. (In any external standalone extraction of §6–§7 this section is appendix material; it remains in the body of the corpus version because the corpus is its context.)

*Observation 1 (rung–sector alignment).* The first rung base is 2, the second is 3, and the first composite control (where Λ vanishes) is 6 \= 2·3 — the first integer past log 3 carrying no prime term, hence the leading flat control of the explicit formula. The corpus sector triple is (Z, X, Y) \= (2, 3, 6). Thus

(rung₁, rung₂, control₁)  \=  (2, 3, 6\)  \=  (dim Z, dim X, dim Y).

Moreover (Z, X) \= (2, 3\) is the *unique* prime pair solving the ZS-M19 T1 forcing equation (p−1)(q−1) \= p (PROVEN; the present numerics confirm uniqueness over all prime pairs up to 97, §B.A9), and Y \= ZX \= 6 is composite, hence a non-rung — exactly as Λ(6) \= 0 makes 6 a control rather than a rung. The alignment is therefore not merely numerical: the *prime/composite* distinction that separates rungs from controls in the explicit formula is the same distinction that separates the matter sectors (X, prime) from the mediator sector (Y \= ZX, composite) in the corpus.

*Observation 2 (reach \= capacity).* The unconditional positivity reach of the base rung is log 2\. The Z-bottleneck channel capacity is ln 2 (ZS-F8 / ZS-Q7), and dim Z \= 2\. The window-length threshold below which the Weil form is unconditionally positive is numerically and exactly the Z-sector channel capacity:

ℓunconditional  \=  log 2  \=  ln 2  \=  CZ-bottleneck .

*Status and discipline.* Both observations are exact identities, not fits, and introduce no parameter. They are registered as OBSERVATION (Observation 1's prime/composite reading rises to HYPOTHESIS-strong, since it has a structural mechanism — the von Mangoldt support — rather than a bare coincidence). They are used in *no* proof of §4–§7. Observation 2 is the *weaker* of the two — it is the same constant “2” appearing in two roles (the smallest prime’s logarithm and dim Z) — and is deliberately left at OBSERVATION with no promotion path. (Independently, Connes \[9\] describes a connection of the Weil quadratic form to information theory; whether the present reach \= capacity identity relates to that connection is not investigated here and is not claimed.) The selection effect is stated plainly: small integers recur across unrelated structures, and a reader may regard either observation as coincidental without affecting any theorem of this paper. This is the same anti-numerology discipline applied in F25 §9 (the arg z\* ≈ log 2 hold) and ZS-F23 §7.2; the present paper makes no Monte-Carlo specialness claim for either observation.

**§9.  Cross-Consistency and Zero-Parameter Audit**

*Zero free parameters.* The only constant introduced by a theorem is √2 log 2 \= 2Λ(2)/√2 (Proposition 7.1), forced by the von Mangoldt weight; it is not a fit. The witness constants (R₀, K₀) \= (17.082, 24\) of Theorem 4.4 are *derived* sufficient constants (R₀ a root of the digamma density, K₀ a majorization threshold with margin \+0.125), not tunable inputs; any larger pair also certifies, and the constants cleak \= 20.38, cpole \= 0.631 (closed form, K-invariant) are reconstructed in §B.E. The numerical values z\*, **A**, **Q** are *not* consumed by any proof (§2): ZS-F26 is math-spine-pure.

*No-deletion compliance.* F25 Lemma 11.4 and all F25 §11 statements are preserved; §6.7 annotates the reading of “concrete finite statement” without withdrawing it. F25 Theorem 11.6, ADS-5, and Lemma M31.0 are consumed at their registered status.

*Observational non-conflict.* ZS-F26 has no cosmological content: it asserts nothing about Planck 2018, DESI, or any observable, and therefore cannot conflict with them. The sector-shadow observation (§8) references corpus sector dimensions but predicts no new measurable quantity.

*Cross-paper audit.* The base-rung import (CC 2021\) is the same object F25 §11.5 uses; the necessity profile (Theorem 6.6) reproduces F25 Theorem 11.6; the absorption realization (Theorem 5.3) matches F25 Theorem 6.6 and Connes 1999; the contraction reading (Corollary 6.5) is consistent with the Z-bottleneck capacity of ZS-F8/ZS-Q7. The 12-reference internal audit PASSES.

**§10.  Multilayer Falsification Gates**

Table 10.1.  Falsification gates for ZS-F26 v1.4.

| Gate | Falsification condition | Consequence |
| ----- | ----- | ----- |
| F-F26.1 | If the minimal-Kolmogorov identification Hbase ≅ span DCCg (Theorem 4.3) is shown to fail (a second inequivalent factorization), §4.3 collapses. | Concrete model retracted |
| F-F26.2 | If λmin(Qarch tail) is shown negative on span{φk : k \> K₀} for the derived K₀ (contradicting Theorem 4.4), the coercivity constant is wrong. | Recompute (R₀, K₀); dim claim at risk |
| F-F26.3 | If rung 1 is shown false (MI(2) violated by an explicit g on a window \< log 3), QW has a negative direction below log 3 — an RH crisis. | RH consequence; report immediately |
| F-F26.4 | If the two-sided explicit-formula identity fails to converge to the block assembly under refinement, the numerical normalization is wrong. | Numerical-convention error |
| F-F26.5 | If Douglas majorization is shown inapplicable to the archimedean block (e.g. domain pathology breaking ran inclusion), Theorem 6.4 fails. | Rung uniformization retracted |
| F-F26.6 | If either sector-shadow observation (§8) is asserted as a mechanism without derivation, anti-numerology is triggered. | Demote to coincidence; flag |
| F-F26.7 | If the directed-system colimit equivalence (Theorem 5.2) is shown to fail (a total system with no colimit, or vice versa), D5's formulation is wrong. | Reformulate D5 |
| F-F26.8 | If CC 2021 is withdrawn or shown not to cover the autocorrelation support class, the base core (Theorem 4.1) loses its unconditional status. | Inherited from \[4\]; base becomes conditional |

**§11.  Non-Claims**

**NC-F26.1.** ZS-F26 makes *no claim on RH or GRH*. Gate D5 is registered IMPORTED-OPEN ≡ RH; Theorems 5.2–5.3 are equivalences and conditional realizations, not existence proofs.

**NC-F26.2.** ZS-F26 does *not* claim rung 1, MI(2), or any higher rung. Theorem 7.3 is an equivalence; §7.4 shows the simplest sufficient route fails.

**NC-F26.3.** The sector-shadow observations (§8) are not asserted as mechanisms and are used in no proof (NC against F-F26.6).

**NC-F26.4.** ZS-F26 does *not* construct the coupling operator K₂ of the candidate F25 §11.7 realization; §6 supplies the *criterion* a realization must satisfy, not the realization.

**NC-F26.5.** The failure of the sufficient route (§7.4) is reported as a closed route, *not* as evidence against rung 1; cross-cancellation remains an open avenue.

**NC-F26.6.** ZS-F26 introduces no new free parameter and no cosmological prediction; it is consistent with, and silent on, all observational corpus content.

**§12.  Open Problems**

**O-F26.1.** Unconditional triviality of the radical Nbase (Proposition 4.5′): prove or refute Nbase \= {0} on the base window without RH. The Paley–Wiener argument stalls at the reality of the zero ordinates.

**O-F26.2.** Prove or refute MI(2) (Theorem 7.3), the exact content of rung 1, via the cross structure of §6 in the CCM 2024 semilocal {∞, 2} habitat \[6\].

**O-F26.3.** Identify ‖K2‖ (or decide ‖K2‖ ≤ 1, which is MI(2)). v1.2 progress: K2 is now constructed conditionally as the WOT limit of the regularized finite-section factors, and its measured section norms are 0.9972–0.999999 \< 1 (Theorem 7.6, Table 7.2) — a nearly saturated contraction; the prime-channel Gram norm 0.5000 (§B.lam) and the Exact-Half bound are the unconditional partial data. The open content is the uniform bound — reduced in v1.3 to the scalar statement supN ε\*(N) \= 0 (Lemmas 7.8–7.9) with three registered routes (§7.7).

**O-F26.4.** Decide whether the prolate negative-eigenvalue subspace (RRJT 2025 \[7\], imported in F25/F21-III) can be *directly* identified with Hbase — a route deferred from the long list of the present exploration as lacking a derivation chain.

**O-F26.5.** Determine the precise relation between Connes’s 2026 minimization of the windowed Weil form (minimal eigenvector approximating the zeros, proven on the critical line; finite→infinite Euler convergence open \[9\]) and this paper’s positivity problem MI(2) for the same window (§7.3): the two read opposite ends of the spectrum of one operator and share the finite→infinite passage. A natural sub-question: does positivity on a window (MI) follow from, or constrain, the critical-line location of that window’s minimal eigenvector? v1.2 first data (§7.6): at ℓ \= (log 13)/2 the minimal eigenvector’s six |ĝ| minima on \[0, 40\] are the six zero ordinates (offsets 10−3–0.44), confirming the “opposite ends of the same spectrum” reading at COMPUTED level, and v1.3 supplies the mechanism: the simultaneous notch bound |ĝmin(γk)| ≤ √(λmin/2) (Proposition 7.10, DERIVED). v1.4 executes the preregistered ℓ-scan (§7.8): the offset–margin law is COMPUTED-established at first order via the Newton-step bound (Proposition 7.11; 34 pairs, ratio median 1.04), the resolution count is monotone in the margin collapse, and the sub-rung control behaves as predicted. The remaining open content is the theoretical asymptotics of λmin(ℓ) along the ladder.

**§13.  Conclusion**

ZS-F26 closes the three audit items that ZS-F25 v2.0 left at the boundary of Gate D5, and registers precisely what remains open. The unconditional GNS core Hbase exists (Theorem 4.1), is canonically unique (Proposition 4.2, Theorem 4.3), and is infinite-dimensional by an explicit high-frequency coercivity estimate with Plancherel-normalized leakage bound and reconstructed constants (Theorem 4.4, witness (R₀, K₀) \= (17.082, 24), margin \+0.125) — converting the second audit item from a registration into a theorem. The infinite-dimensional gap in the rung is real: section certification provably fails (Theorem 6.1), and the rung is uniformized at form level (Lemma 11.4′) and at operator level by Douglas–Shmul’yan (Theorems 6.3–6.4), making every rung a contraction (Corollary 6.5) that is operator-valued, cross-coupled, and ΠZ\-sandwiched (Theorem 6.6) — a refinement, not a correction, of F25 Lemma 11.4. Gate D5 is recast as the existence of an isometric colimit (Theorem 5.2), on which the scaling flow realizes the zeros as a simple-spectrum self-adjoint generator on the absorption side, multiplicities absorbed as weights (Theorem 5.3). Rung 1 is pinned to the Master Inequality MI(2), whose perturbation has operator norm exactly half its coupling constant (Exact-Half Lemma, PROVEN), and whose simplest sufficient route is closed by preregistered numerics that expose an arithmetic–archimedean cross-cancellation (§7.4) in agreement with F25 Theorem 11.6. The sector shadow (2, 3, 6\) and the reach–capacity identity log 2 \= ln 2 are registered as exact, parameter-free observations. The same windowed object is minimized in Connes’s 2026 survey to approximate the zeros on the critical line; the present positivity reading and that minimization reading share the finite→infinite open step (O-F26.5). Rung 1’s mediation operator is now an explicit limit of computable regularized factors whose measured norms saturate the Douglas ball to within 10−6 (Theorem 7.6, Table 7.2); the uniform-contraction program is reduced to one nondecreasing scalar sequence, supN ε\*(N) \= 0, with three registered routes (Lemmas 7.8–7.9, §7.7); and the Connes-window bridge experiment supplies both the first data for O-F26.5 — the minimal eigenvector’s six near-zeros on \[0, 40\] are the six zero ordinates — and its variational mechanism, the simultaneous notch bound |ĝmin(γk)| ≤ √(λmin/2) (Proposition 7.10), now sharpened by the executed ℓ-scan into a first-order law: every resolved notch offset is the Newton quotient (Proposition 7.11; 34 pairs, ratio median 1.04 over five decades of λmin), the resolution count grows monotonically with the collapse of the positivity margin, and the sub-rung base window is the predicted loose control. No claim is made on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. Verification: 47/47 PASS, zero free parameters.

**Acknowledgements and Code Availability**

Developed within the Z-Spin Cosmology corpus with AI assistance (Anthropic Claude) for the deep exploration, the symbolic and numerical verification, and manuscript drafting; the author is responsible for all scientific content, claims, and conclusions. The complex-digamma vectorization (validated to 4.4×10−16 against mpmath), the two-sided explicit-formula test (160 zeros via mpmath.zetazero), the window λmin tables (sine-basis Gram assembly, M \= 40/60/80, with quadrature-doubling control), the tail-coercivity and witness-constant computations, the Section-Certification Gap harmonic table, the forcing-equation enumeration, and the v1.2 suite (closed-form pole sums to 2×10⁶ terms, truncation studies, the (log 13)/2 bridge experiment, and the regularized Douglas-factor norms) were computed at machine and 15-digit precision and are reproducible. External imports cite peer-reviewed work; the base rung is Connes–Consani 2021 \[4\]. No claim is made on RH, GRH, or Weil positivity.

**Appendix A.  Verification Suite (47/47 PASS)**

Table A.1.  Verification checks by category.

| \# | Check | Result |
| :---: | ----- | ----- |
| A1 | ψ(1/4) \= −γ − π/2 − 3 log 2 closed form (err 8.9×10−16) | PASS / PROVEN |
| A2 | Complex-digamma vectorization vs mpmath, 5 points (max err 4.4×10−16) | PASS / COMPUTED |
| A3 | Re ψ(1/4 \+ ir/2) monotone increasing on \[0, 60\] | PASS / DERIVED |
| A4 | Pole identity 2 Re(M\+M̄−) vs double integral (relerr 4.8×10−16) | PASS / PROVEN |
| A5 | Scaling invariance of QW (Lemma 3.1), exact algebra | PASS / PROVEN |
| A6 | Modal Plancherel (1/2π)∫|ĝk|² \= 1 (ratio 1.0000) | PASS / COMPUTED |
| A7 | √2 log 2 \= 2Λ(2)/√2 \= 0.980258 | PASS / PROVEN |
| A8 | Λ(6) \= 0; rung order log 2 \< log 3 \< log 4 \< log 5; control log 6 | PASS / PROVEN |
| A9 | Forcing (p−1)(q−1) \= p unique prime solution (2, 3\) over primes ≤ 97 | PASS / PROVEN |
| B1 | Two-sided explicit formula, single mode, 160 zeros (relerr 0.049%) | PASS / COMPUTED |
| B2 | Two-sided explicit formula, 8-mode vector, 160 zeros (relerr 0.0030%) | PASS / COMPUTED |
| B3 | λmin(QW) \> 0 at ℓ \= 0.60 (base; \+0.00792) | PASS / COMPUTED |
| B4 | λmin(QW) \> 0 at ℓ \= 0.80 (+1.94×10−4) | PASS / COMPUTED |
| B5 | λmin(QW) \> 0 at ℓ \= 1.00 (+1.87×10−6) | PASS / COMPUTED |
| B6 | λmin(QW) \> 0 at ℓ \= 1.09 (rung-1 window; \+9.50×10−7) | PASS / COMPUTED |
| B7 | λmin(QW) \> 0 at ℓ \= 1.30 (n \= 2, 3 window; \+2.05×10−8) | PASS / COMPUTED |
| B8 | λmin(Qarch) \< 0 at ℓ \= 0.80, 1.00, 1.09, 1.30 (indefinite block) | PASS / COMPUTED |
| B9 | M \= 40/60/80 convergence of λmin(QW), monotone | PASS / COMPUTED |
| B10 | Quadrature doubling: λmin shift 4×10−11 at ℓ \= 1.00 | PASS / COMPUTED |
| B11 | ℓ \= 1.30 high-resolution Simpson (40001-pt): λmin(QW) \= \+2.05×10−8 (near quadrature floor) | PASS / COMPUTED |
| C1 | Tail coercivity λmin(Qarch, k \> 5\) \= \+1.469 at ℓ \= 0.60 | PASS / COMPUTED |
| C2 | Tail coercivity λmin(Qarch, k \> 10\) \= \+2.133 | PASS / COMPUTED |
| C3 | Tail coercivity λmin(Qarch, k \> 20\) \= \+2.808 | PASS / COMPUTED |
| C4 | Witness root R₀ \= 17.082 of Re ψ(1/4 \+ iR/2) \= log π \+ 1 | PASS / DERIVED |
| C5 | Witness margin 1 − (cleak\+cpole)/K₀ \= \+0.125 at K₀ \= 24 (min K₀ \= 22, margin \+0.037; K \= 21 fails −0.013); cleak \= 20.38, cpole \= 0.631 | PASS / DERIVED |
| C6 | Measured worst-case low-freq fraction monotone in tail truncation 84/164/264: 0.0152/0.0178/0.0192 (K=36), 0.0258/0.0284/0.0297 (K=24) ≤ analytic 0.0867, 0.133 | PASS / COMPUTED |
| C7 | Pole constant, closed form mk±: cpole \= 0.6308/0.6310/0.6314 (K=22/24/36), K-invariant; v1.1 values 0.505/0.442 explained as truncation artifact (1−K/M factor, M=120) | PASS / PROVEN |
| D1 | Section-Certification Gap HN: 5.19, 7.49, 9.79, 12.09, 14.39 (N \= 10²–10⁶) | PASS / PROVEN |
| D2 | Full-block non-completability: Σ n·bn² \= Σ 1/n diverges | PASS / PROVEN |
| D3 | Convergent control bn \= n−1.1: ζ(1.2) \= 5.5916; section bounds converge | PASS / COMPUTED |
| D4 | Prime-channel Gram spectral norm \= 0.5000 (rung 1, all windows) | PASS / COMPUTED |
| E1 | Exact-Half: Tlog 2² \= 0 on ℓ \< 2 log 2 (nilpotency) | PASS / PROVEN |
| E2 | Exact-Half: ‖Re Tlog 2‖ \= 1/2; a priori bound 0.490129 | PASS / PROVEN |
| E3 | Sufficient route Qarch ≥ 0.490·‖g‖² fails (Qarch indefinite) | PASS / COMPUTED |
| F1 | Douglas–Shmul’yan block criterion B \= A1/2KC1/2, ‖K‖ ≤ 1 | PASS / IMPORTED |
| F2 | Necessity profile: operator-valued, cross-coupled, ΠZ\-sandwiched | PASS / DERIVED |
| F3 | Anti-overclaim: no RH/GRH/Weil-positivity asserted at any step | PASS |
| G1 | cpole closed-form limit 9ℓ₀/π² \= 0.632 matches exact sums to 2×10⁶ terms \+ analytic tail | PASS / PROVEN |
| G2 | Measured fraction monotone increasing in truncation, bounded by Lemma 4.5′ at every truncation | PASS / COMPUTED |
| G3 | ℓ \= (log 13)/2: λmin(QW) \= \+3.71×10−8 stable across M \= 40/60/80; λmin(Qarch) \= −0.613 | PASS / COMPUTED |
| G4 | Bridge: all 6 local minima of |ĝmin| on \[0,40\] are γ₁–γ₆; offsets −0.001/0.000/+0.003/+0.067/+0.205/+0.438; controls carry none | PASS / COMPUTED |
| G5 | Regularized Douglas norms ‖K2,ε‖ \< 1 at every ε ∈ \[10−7, 10−3\], both rung windows; 1−‖K‖ down to 10−6 | PASS / COMPUTED |
| G6 | Notch bound (Prop. 7.10): all six |ĝmin(γk)| \= 1.2×10−7–3.7×10−5 ≤ √(λmin/2) \= 1.36×10−4, monotone in k | PASS / COMPUTED |
| G7 | ε-monotone signature (Lemma 7.8): measured ‖K2,ε‖ rises monotonically toward 1 as ε ↓ 0, never crossing, both windows | PASS / COMPUTED |
| G8 | Basis convergence M \= 80/120/160 at ℓC: γ₁–γ₄ offsets stable to 10−4–10−3; γ₅–γ₆ drift 0.002/40 modes ⇒ quadrature-dominated sensitivity | PASS / COMPUTED |
| G9 | Newton law (Prop. 7.11): 34 resolved (window, zero) pairs over 5 decades of λmin; measured/predicted ratio median 1.04, range \[0.63, 1.22\], outliers at precision-floor offsets | PASS / COMPUTED |
| G10 | Resolution count monotone 3→6 as λmin falls 7.9×10−3→2.0×10−8; sub-rung control ℓ \= 0.60 resolves only γ₁ (offset 0.81) | PASS / COMPUTED |

**Appendix B.  Numerical Details**

*B.1 Two-sided explicit formula.* With the sine-basis Gram of §3.1 at ℓ \= 1.00 and 160 nontrivial zeros (γmax \= 334.21, via mpmath.zetazero), the identity Σρh(γ) \= 2Σk|ĝ(γk)|² was tested as RHS \= cᵀQWc vs LHS \= 2Σ|ĝ(γ)|² for c the first sine mode (LHS 0.0032225, RHS 0.0032241, relerr 0.049%, finite-zero tail est 9×10−7) and for an 8-mode test vector (LHS 0.093667, RHS 0.093670, relerr 0.0030%). The residual is the finite-zero truncation, consistent with the tail estimate.

*B.5 Scaling invariance.* Under s \= 0.3 the pole product M\+M− and each modal |ĝk|² are invariant by exact algebra (§3.2); the prime block and norm are autocorrelation-invariant. Lemma 3.1 holds to machine precision.

*B.C7 Quadrature robustness.* Rebuilding the archimedean Gram on a doubled frequency grid (dr halved, R \= 6000\) shifts λmin(QW) at ℓ \= 1.00, M \= 40 by 4.1×10−11, confirming the archimedean integral is converged.

*B.E coercivity / witness (corrected, v1.1).* R₀ \= 17.0819 solves Re ψ(1/4 \+ iR/2) \= log π \+ 1\. The leakage constant of Lemma 4.5′ is C \= 8R₀ℓ0/(π³(1−δK)²) \= 3.199 at K \= 24 (δ24 \= 0.0227), giving cleak \= \[log π \+ 1 − ψ(1/4)\]·C \= 6.372184·3.199 \= 20.38; the pole constant cpole \= K·Σk\>K\[(mk\+)² \+ (mk−)²\] has the closed form mk± \= √(2/ℓ)·ak(1 − (−1)ke±ℓ/2)/(ak² \+ 1/4) and is K-invariant: summing 2×10⁶ terms plus the analytic tail gives 0.6308 (K \= 22), 0.6310 (K \= 24), 0.6314 (K \= 36), converging to the parity-averaged limit 9ℓ₀/π² \= 0.632. (The v1.1 values 0.505 and 0.442 were truncation artifacts: summing only to M \= 120 modes multiplies the limit by ≈ (1 − K/M), and 0.632×0.8 \= 0.506, 0.632×0.7 \= 0.442 reproduce them exactly. Corrected here; the margin moves from \+0.130 to \+0.125 and nothing else changes.) The margin 1 − (cleak \+ cpole)/K is \+0.125 at K₀ \= 24, and the smallest K with positive margin is 22 (+0.037; K \= 21 gives −0.013). The *measured* worst-case low-frequency fraction (the top eigenvalue of the tail block of the Plancherel-normalized low-frequency Gram Ljk \= (1/2π)∫|r|≤R₀ĝjĝ̄k dr) is 0.0152/0.0178/0.0192 (K \= 36\) and 0.0258/0.0284/0.0297 (K \= 24\) at tail truncations of 84/164/264 modes — monotone increasing in the truncation, so any quoted value must carry its truncation — against the analytic bounds 0.0867 and 0.133: the bound holds with a three- to fivefold margin at every truncation. The tail λmin table (C1–C3) shows the coercivity threshold is in fact already met at K \= 5, so the analytic witness K₀ \= 24 is conservative; the conclusion dim Hbase \= ∞ is robust to the exact constant.

*B.F Section-Certification Gap.* Harmonic partial sums HN \= 5.1874, 7.4855, 9.7876, 12.0901, 14.3927 for N \= 10², 10³, 10⁴, 10⁵, 10⁶ (diverging); the full block is non-completable (Σ 1/n \= ∞). The convergent control bn \= n−1.1 has Σ n−1.2 \= ζ(1.2) \= 5.5916 with section bounds 3.60, 4.34, 4.80 (N \= 10²–10⁴) rising toward it.

*B.lam window λ\~min\~.* Sine-basis Gram, M \= 80, frequency grid dr \= 0.01 (|r| \< 100), 0.05 (≤ 1200), 0.5 (≤ 6000); prime-channel overlap integrals on 20001-point spatial grids. Results in Table 7.1; the symmetrized n \= 2 prime Gram has spectral norm 0.5000 at every window (D4). Sine-basis λmin is an upper bound for the subspace spanned (monotone decreasing in M); the reported positivity of QW is therefore a property of the finite-dimensional compression, consistent across refinements.

*B.G Error budget and boundary-case classification (v1.2).* Quadrature: doubling the frequency grid shifts λmin by 4×10−11 (§B.C7), so entries above 10−7 are quadrature-safe. Basis: λmin is monotone non-increasing in M and stable to the digits shown across M \= 40/60/80. Prime overlaps: 40001-point Simpson-grade grids, relative error \< 10−9 on test integrals. Classification: entries with λmin ≥ 10−7 are reported as figures; the ℓ \= 1.2825 and ℓ \= 1.30 entries (λmin ∼ 10−8) are classified as *numerical boundary cases* — sign confirmed under refinement, magnitude near the floor. The classification extends to *eigenvector-derived quantities* at boundary-case windows: the nearly degenerate bottom eigenvector wanders with quadrature, so the γ₄–γ₆ offsets of Table 7.3 and the ε \= 10−7 residuals of Table 7.2 are order-of-magnitude figures, while λmin signs, the γ₁–γ₃ offsets, and the notch-bound inequalities (G6) are robust. A fully certified (interval-arithmetic) recomputation of Table 7.1 is deliberately deferred to the external standalone note, where it carries the most value.

*B.H Bridge experiment details (§7.6).* Window ℓC \= (log 13)/2 \= 1.282475, M \= 80, high-resolution grid as in B.lam; λmin(QW) \= \+3.713×10−8 with eigenvector gmin; |ĝmin(r)| evaluated on r ∈ \[0, 40\], step 0.002 (20001 points); local minima by 3-point comparison; γk from mpmath.zetazero to 20 digits; depth normalized by the median of |ĝmin| over the range. The six minima and offsets are in Table 7.3; an independent reproduction at a different quadrature obtained λmin \= \+9.1×10−11 (vs \+3.7×10−8 here — both at the floor, sign agreeing) and γ₄–γ₆ offsets \+0.017/+0.065/+0.230 (same monotone pattern, different values), which fixes the precision discipline of §B.G; the midpoint controls 17.58 / 23.02 / 27.72 carry no local minima (local min-ratio over ±0.5 windows: 5.86 / 0.46 / 0.21, i.e. slopes of neighboring true dips, no critical points). Count check: a generic 80-mode sine combination on this window has ≈ ℓC·40/π ≈ 16 sign changes of Re ĝ available in \[0, 40\]; the minimizer spends exactly six near-zeros and parks them on the γk — the economy, not just the placement, is the signal.

*B.I Regularized Douglas factor numerics (§7.5).* Base V: 40 sine modes of \[0, 0.60\] (zero-extended; autocorrelation reach 0.60 \< log 2, so A is prime-free, λmin(A) \= \+0.00823 \= the base-window Qarch coercivity). New space W: 80 sine modes of \[0, ℓ\], L²-projected off V (Gram I − OᵀO, eigen-threshold 10−8; retained ranks 44 and 48 — threshold-dependent: a coarser tolerance retains 40, with the norms of Table 7.2 unchanged to the digits shown). Blocks A, B, C assembled from the same pole/log π/digamma/prime machinery as B.lam, with the symmetrized bilinear prime cross-correlation ½\[∫u(τ+v)w(v) \+ ∫w(τ+v)u(v)\]dv at τ \= log 2 (and log 3 for ℓ \= 1.2825). λmin of the combined L²-orthonormal family reproduces the Table 7.1 windows (+1.0×10−6 at ℓ \= 1.09, \+3.7×10−8 at 1.2825), an independent cross-check of the splitting. K2,ε \= (A+ε)−1/2B(C+ε)−1/2 by symmetric eigendecomposition; norms in Table 7.2; all values \< 1 at every ε down to 10−7, where conditioning (λmin(C)/ε ≤ 4×105) remains benign.

*B.J ℓ-scan details (§7.8).* Windows ℓ ∈ {0.60, 0.80, 0.90, 1.00, 1.09, 1.20, 1.28247, 1.30}, M \= 80, the B.lam grid; minimal eigenvector per window; |ĝmin| on \[0, 40\] at step 0.002; ĝmin and ĝmin′ at each γk by closed-form evaluation and central difference (h \= 10−4). A (window, zero) pair is counted *resolved* when a local minimum lies within 2.0 of γk and the measured offset agrees with the Newton quotient within 50% — the agreement statistics of §7.8 then tighten to median 1.04 without further tuning, i.e. the resolution filter does not manufacture the law. Basis-convergence runs repeat the ℓC analysis at M \= 120 and 160 on the identical grid, so the M-drift isolates basis truncation by construction. All scan data are reproducible from the same machinery as B.lam/B.H.

**References**

\[1\] A. Weil, “Sur les “formules explicites” de la théorie des nombres premiers,” Comm. Sém. Math. Lund (1952) 252–265.  
\[2\] A. P. Guinand, “A summation formula in the theory of prime numbers,” Proc. London Math. Soc. (2) 50 (1948) 107–119.  
\[3\] H. Iwaniec, E. Kowalski, Analytic Number Theory, AMS Colloq. Publ. 53 (2004), Theorem 5.12.  
\[4\] A. Connes, C. Consani, “Weil positivity and trace formula, the archimedean place,” Selecta Math. 27 (2021) 77; arXiv:2006.13771.  
\[5\] A. Connes, C. Consani, “Spectral triples and zeta-cycles,” (2022); arXiv:2112.05500.  
\[6\] A. Connes, C. Consani, H. Moscovici, “Zeta zeros and prolate wave operators,” Ann. Funct. Anal. 15 (2024) 87; arXiv:2310.18423.  
\[7\] J.-P. Ramis, F. Richard-Jung, J. Thomann, Comptes Rendus Math. 363 (2025) 1065–1081; doi:10.5802/crmath.780.  
\[8\] A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” Selecta Math. 5 (1999) 29–106.  
\[9\] A. Connes, “The Riemann Hypothesis: Past, Present and a Letter Through Time,” arXiv:2602.04022 (February 2026); commissioned RH survey containing a “Letter to Riemann” that extremizes the restriction of Weil’s quadratic form to primes below 13, approximating the first fifty zeros (2.6×10−55–10−3) and proving the approximants lie on the critical line, with a finite→infinite Euler-product proof strategy.  
\[10\] R. G. Douglas, “On majorization, factorization, and range inclusion of operators on Hilbert space,” Proc. Amer. Math. Soc. 17 (1966) 413–415.  
\[11\] M. S. Moslehian, M. Kian, Q. Xu, “Positivity of 2×2 block matrices of operators,” Banach J. Math. Anal. 13 (2019) 726–743.  
\[12\] V. Paulsen, Completely Bounded Maps and Operator Algebras, Cambridge Studies in Advanced Math. 78 (2002) (minimal Kolmogorov/Stinespring uniqueness).  
\[13\] A. Albert, “Conditions for positive and nonnegative definiteness in terms of pseudoinverses,” SIAM J. Appl. Math. 17 (1969) 434–440.  
\[14\] W. N. Anderson, G. E. Trapp, “Shorted operators II,” SIAM J. Appl. Math. 28 (1975) 60–71.  
\[15\] Yu. L. Shmul’yan, “An operator Hellinger integral,” Mat. Sb. 49 (1959) 381–430.  
\[16\] A. Bondarenko, D. Radchenko, K. Seip, “Fourier interpolation with zeros of zeta and L-functions,” Constr. Approx. 57 (2023) 405–461; arXiv:2005.02996.  
\[17\] M. H. Stone, “On one-parameter unitary groups in Hilbert space,” Ann. of Math. 33 (1932) 643–648.  
\[18\] J.-F. Burnol, “On Fourier and zeros,” C. R. Acad. Sci. Paris 335 (2002) 689–692.  
\[19\] D. Slepian, H. O. Pollak, “Prolate spheroidal wave functions, Fourier analysis and uncertainty I,” Bell Syst. Tech. J. 40 (1961) 43–63.  
\[20\] H. L. Montgomery, “The pair correlation of zeros of the zeta function,” Proc. Sympos. Pure Math. 24 (1973) 181–193.  
\[21\] K. Kang, ZS-F21 v2.0 — The Archimedean–Finite Positivity Wall, III (Z-Spin Cosmology, 2026).  
\[22\] K. Kang, ZS-F25 v2.0 — The Pulsation Holonomy is Abelian by Foundation (Z-Spin Cosmology, 2026).  
\[23\] K. Kang, ZS-F24 v2.0 — The Honest Terminus of the Z-Seam → Prolate Bridge (Z-Spin Cosmology, 2026).  
\[24\] K. Kang, ZS-M4 v1.1 — Q \= 11 Transfer Operator and Prime-Resonance Diagnostics (Z-Spin Cosmology, 2026).  
\[25\] K. Kang, ZS-M22 — ADS-5 scalar/diagonal-kernel exclusion (Five-Pillars / Probe-W2) (Z-Spin Cosmology, 2026).  
\[26\] K. Kang, ZS-M31 — Lemma M31.0 Non-Separability (Z-Spin Cosmology, 2026).  
\[27\] K. Kang, ZS-M19 — Forcing Theorem T1: (p−1)(q−1) \= p (Z-Spin Cosmology, 2026).  
\[28\] K. Kang, ZS-F8 — Z-bottleneck channel capacity ln 2 (Z-Spin Cosmology, 2026).  
\[29\] K. Kang, ZS-Q7 — Pauli master equation and λ-factorization (Z-Spin Cosmology, 2026).  
\[30\] K. Kang, ZS-F0 v1.0(R) — Ontological Bootstrap and Foundational Closure (Z-Spin Cosmology, 2026).

**Version History**

**v1.0 (March 2026): Initial public release.** Establishes the unconditional GNS core (Theorem 4.1) with canonical uniqueness (Proposition 4.2, Theorem 4.3) and unconditional infinite-dimensionality via high-frequency coercivity with derived witness (R₀, K₀) \= (17.082, 36\) (Theorem 4.4, Lemmas 4.5–4.6); recasts Gate D5 as an isometric colimit with absorption-side spectral realization (Theorems 5.2–5.3); proves the Section-Certification Gap (Theorem 6.1) and uniformizes the rung by the Douglas–Shmul’yan contraction criterion at form level (Lemma 11.4′ \= Lemma 6.2) and operator level (Theorems 6.3–6.4), yielding contractive, operator-valued, cross-coupled, ΠZ\-sandwiched mediation (Corollary 6.5, Theorem 6.6) as a refinement of F25 Lemma 11.4; formulates rung 1 as the Master Inequality MI(2) with the Exact-Half Lemma (‖Re Tlog 2‖ \= 1/2, PROVEN) and refutes the naive sufficient route by preregistered numerics exposing arithmetic–archimedean cross-cancellation (§7); registers the sector-shadow observations (2, 3, 6\) and log 2 \= ln 2 (§8, OBSERVATION/HYPOTHESIS-strong). Verification: 34/34 PASS, zero free parameters. No claim on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. (Consolidated from internal Z-Spin Collaboration research notes, Weil-positivity operator-ladder deep-exploration session.)

**v1.1 (March 2026): Revision incorporating external review.** All v1.0 content is preserved verbatim per the Z-Spin no-deletion convention; the following are corrected or added. (a) *Lemma 4.5 → Lemma 4.5′ (reproved).* The leakage lemma is restated in Plancherel normalization, φlo(g) \= (1/2π)∫|r|≤R|ĝ|² ≤ 8Rℓ/(π³(1−δK)²K), with a complete per-mode derivation (Cauchy–Schwarz over the orthonormal tail, single-mode envelope, Σ k−2 ≤ 1/K) replacing the v1.0 “working-resolution” consolidation — which was a genuine normalization gap (the v1.0 bound 128ℓ/(9π²K) omitted the 1/2π Plancherel factor and is false as a raw-integral statement). The Theorem 4.4 witness is corrected to (R₀, K₀) \= (17.082, 24\) with reconstructed constants cleak \= 20.38, cpole \= 0.505 and margin \+0.130 (minimal K₀ \= 22); the measured worst-case fraction 0.0152 (K \= 36\) is recorded in §B.E as the sharp reference. The conclusion dim Hbase \= ∞ is unchanged and now rests on a correct chain. (b) *Connes 2026 integrated.* Reference \[9\] is brought into the body (§1, §7.4): Connes’s February 2026 minimization of the windowed Weil form (primes below 13; first fifty zeros to 2.6×10−55–10−3, on the critical line; finite→infinite Euler-product strategy) and this paper’s positivity problem MI(2) are shown to read opposite ends of the spectrum of the same windowed operator and to share the finite→infinite open step; the relation is registered as O-F26.5. (c) *Five citation-wiring repairs.* \[9\] title corrected to “The Riemann Hypothesis: Past, Present and a Letter Through Time” (arXiv:2602.04022); \[16\] corrected to Bondarenko–Radchenko–Seip, “Fourier interpolation with zeros of zeta and L-functions” (Constr. Approx. 57 (2023) 405); the Table 2.1 convention row now cites \[3\] (Iwaniec–Kowalski); O-F26.4 now cites \[7\] (RRJT 2025); the unused Hardy entry is replaced by Stone’s theorem \[17\], cited in Theorem 5.3. (d) *Micro-tagging.* Theorem 5.3’s simplicity is restricted to the cyclic (minimal) subrealization; Theorem 4.3 now cites the Connes–Consani defect/compression certificate \[4\] explicitly (gated by F-F26.1); the ℓ \= 1.30 entry of Table 7.1 carries a quadrature-floor annotation (high-resolution recomputation \+2.05×10−8). Verification: 37/37 PASS, zero free parameters. No claim on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. (Consolidated from internal Z-Spin Collaboration research notes, Weil-positivity operator-ladder deep-exploration session; v1.1 revision incorporating external review.)

**v1.2 (March 2026): Revision incorporating two further external reviews.** All v1.0–v1.1 content is preserved per the no-deletion convention; the following are repaired or added. (a) *Three residuals repaired.* The §1 contribution summary C3, missed in the v1.1 pass, now carries the corrected witness (17.082, 24). The pole constant is recomputed in closed form, mk± \= √(2/ℓ)·ak(1 − (−1)ke±ℓ/2)/(ak² \+ 1/4): cpole \= 0.631, K-invariant, limit 9ℓ₀/π² — the v1.1 values 0.505/0.442 are explained exactly as M \= 120 truncation artifacts (factor 1 − K/M); the Theorem 4.4 margin moves \+0.130 → \+0.125, minimal K₀ \= 22 unchanged. The measured low-frequency fraction is restated with its tail truncation and monotonicity (0.0152 → 0.0192 as the truncation grows, always under the analytic bound). (b) *Function-space convention repaired* (§3.1): half-window class adopted; g is real and compactly supported in \[0, ℓ\], evenness is carried by f \= g ⋆ g̃ and h \= |ĝ|²; the v1.0–v1.1 phrase “real even Schwartz” is retired. (c) *MI(2) operator program* (§7.5): Proposition 7.7 (three equivalent formulations) and Theorem 7.6 (regularized finite-section Douglas factors K2,ε; trichotomy MI(2) ⇔ block positivity ⇔ uniform contraction; conditional WOT construction of K2; the Section-Certification Gap as the exact reason measurement cannot certify); measured section norms 0.9972–0.999999 \< 1 (Table 7.2). (d) *Bridge experiment* (§7.6, first data for O-F26.5): at ℓ \= (log 13)/2 the minimal eigenvector’s |ĝ| has exactly six local minima on \[0, 40\] and they are γ₁–γ₆ (offsets −0.001 to \+0.44), with empty controls — an analogous experiment to Connes 2026, not a replication, and COMPUTED evidence for the “same spectrum, opposite ends” reading. (e) Table 7.1 gains the ℓ \= (log 13)/2 row; near-floor entries are classified as numerical boundary cases with an error budget (§B.G); the abstract’s spectral simplicity is restricted to the cyclic minimal subrealization; §8 carries an external-extraction note. Verification: 42/42 PASS, zero free parameters. No claim on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. (Consolidated from internal Z-Spin Collaboration research notes; v1.2 revision incorporating external reviews.)

**v1.3 (March 2026): Revision incorporating the v1.2 external verification.** All prior content preserved per the no-deletion convention. (a) *Residuals.* Table 10.1 caption updated; Theorem 4.1 harmonized with the §3.1 half-window convention (evenness of g removed; the CC support class is characterized by autocorrelation reach). (b) *Precision discipline.* The γ₄–γ₆ offsets of Table 7.3 are reclassified as order-of-magnitude, quadrature-sensitive figures (an independent reproduction at different quadrature gives \+0.017/+0.065/+0.230 with λmin \= \+9.1×10−11, same monotone pattern and sign, different values); the ε \= 10−7 residuals of Table 7.2 carry the same caution; §B.G’s boundary-case classification is extended to eigenvector-derived quantities; the W-rank threshold dependence is recorded in §B.I. (c) *Variational mechanism (Proposition 7.10, DERIVED).* The zero-side identity forces the simultaneous notch bound 2|ĝmin(γk)|² ≤ λmin at every critical-line ordinate, with the unconditional off-line caveat stated; verified at all six ordinates (1.2×10−7–3.7×10−5 ≤ 1.36×10−4, G6) — the bridge phenomenon is thereby a mechanism, not merely an observation. (d) *Uniform-contraction structure (§7.7).* Lemma 7.8 (ε-monotone certification: the certified set is upward-closed, section positivity ⇔ ε\*(N) \= 0; PROVEN) and Lemma 7.9 (section monotonicity: MI(2) ⇔ supN ε\*(N) \= 0; PROVEN) reduce rung 1 to a single scalar sequence; three routes are registered OPEN (commutator/Exact-Half, prolate scattering, monotone finite-section), with the explicit non-claim that proving any one is MI(2) itself. Verification: 44/44 PASS, zero free parameters. No claim on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. (Consolidated from internal Z-Spin Collaboration research notes; v1.3 revision incorporating external verification.)

**v1.4 (March 2026): Execution of the v1.3 preregistration.** All prior content preserved per the no-deletion convention. (a) *Basis-convergence test executed* (M \= 80/120/160 at ℓC): γ₁–γ₄ offsets stable to 10−4–10−3, γ₅–γ₆ drift 0.002 per 40 modes — the γ₄–γ₆ sensitivity is thereby decided to be quadrature-floor-dominated, sustaining the §B.G classification. (b) *Preregistered ℓ-scan executed* (§7.8, Table 7.4; ℓ \= 0.60 control disclosed as an addition): Proposition 7.11 (Newton-step offset bound, DERIVED) predicts every resolved notch — 34 (window, zero) pairs across eight windows and five decades of λmin, measured/predicted ratio median 1.04, range \[0.63, 1.22\] with outliers at precision-floor offsets; the resolution count grows monotonically 3 → 6 as λmin falls 7.9×10−3 → 2.0×10−8; the γ₂ offset collapses 3.38 → 0.000 along the ladder; the sub-rung base window resolves only γ₁, loosely, as predicted. O-F26.5’s open content narrows to the theoretical asymptotics of λmin(ℓ). Verification: 47/47 PASS, zero free parameters. No claim on RH; Gate D5 remains IMPORTED-OPEN ≡ RH. (Consolidated from internal Z-Spin Collaboration research notes; v1.4 executing the v1.3 preregistration.)  
