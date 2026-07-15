**ZS-M48**  
**Suzuki’s Finite-Interval Operator on Dirichlet Channels, and Character Decomposition as Numerical Preconditioning**

**A Channel Perturbation Theorem, the Frobenius-Resolved Kernel, and a Certified V₄ Case Study for K \= ℚ(√−3, √−11)**

Author: Kenny Kang  
Affiliation: Z-Spin Collaboration  
Date: July 2026  
Paper code: ZS-M48 v2.7  ·  Math Spine series  
This is a compact rewrite. Versions v1.0–v1.9 were internal audit drafts; every correction made during that process is recorded in the Correction History Supplement and is not repeated in the body.

Verification: one self-contained fail-closed suite, zs\_m48\_verify\_v2\_7.py — \*\*380 checks\*\*; the expected count is \*\*hard-coded\*\* (no environment override) and the script exits non-zero on the first failure. \*\*Theorem-tier blocks decided in arb ball arithmetic:\*\* the enclosures of §4, the real-zero certification of §4.3, the certified zero brackets, the interval Cholesky of §5, the budget inversions of §6, and the Frobenius resolution of §8.1. \*\*VERIFIED (not arb-certified):\*\* the perturbation norms ‖ν\_{χ,a}‖\_TV of Table 8.1 (Theorem T11 itself is PROVEN; only the numerical values of its bound are floating-point), and the threshold-law residuals of Table 6.1. \*\*DIAGNOSTIC:\*\* the sampled screw-Gram and Schoenberg matrices, the exploratory null model, the detected-zero list, and the fixed-point count. \`--fast\` is a smoke test, \*\*not\*\* the public certificate.  \*\*Provenance, stated exactly:\*\* the analytic blocks of this version were executed to completion in isolation; a single-process run of all 380 checks takes roughly 15 minutes and exceeded the interactive limit of the drafting environment, so its stdout, JSON ledger, library versions, script SHA-256 and wall-clock time are \*\*not yet included\*\*. They are required before public release, and the hard-coded guard is what prevents a partial run from being reported as a complete one.

# **§0. Abstract**

Suzuki attached to a Dirichlet series in the extended Selberg class a real even kernel g\_F — the **screw function** — whose non-positivity is equivalent to GRH for F, and built a finite-interval self-adjoint operator from it \[1–3\]. This paper takes that machinery to a **decorated** object: the Dedekind zeta of the biquadratic field K \= ℚ(√−3, √−11), whose genus characters have conductors 1, 3, 11, 33\. **Five** results follow. The first is an operator theorem; the last is the reason to read the paper.

**(0) The channel perturbation theorem — Suzuki’s operator, transferred.** Suzuki proves that the finite-interval quadratic form of the **ζ** screw kernel is closed, lower semibounded, and has a self-adjoint Friedrichs extension with discrete spectrum \[3\]. That theorem does **not** transfer to Dirichlet L-functions for free. We prove that it does, and cheaply. Writing h\_χ := g\_χ − g\_ζ, the two archimedean densities have the **same** 1/(2|x|) singularity at the origin, so it cancels in the difference: ω\_{c\_χ}(x) − ω\_{1/4}(x) → ¼ − c\_χ. Consequently, on any \[−2a, 2a\],  
\*\*h\_χ″ \= ν\_{χ,a}, a FINITE signed Radon measure\*\*: finitely many prime atoms (n ≤ e^{2a}), a point mass of \*\*exactly −log q\_χ\*\* at the origin, and a bounded density.  
Since the form difference is q\_χ\[u\] − q\_ζ\[u\] \= −⟨ν\_{χ,a}, u \* ũ⟩ and |(u \* ũ)(t)| ≤ ‖u‖², the perturbation is **L²-bounded** with explicit norm ‖ν\_{χ,a}‖\_TV. By KLMN, q\_χ is closed and lower semibounded on the **same form domain** as q\_ζ; the associated operator is A\_a^χ \= A\_a^ζ \+ B\_{χ,a} with ‖B‖ ≤ ‖ν‖\_TV, so it is self-adjoint, has **compact resolvent and discrete spectrum**, and its eigenvalues satisfy |λ\_n(A\_a^χ) − λ\_n(A\_a^ζ)| ≤ ‖ν\_{χ,a}‖\_TV for every n. **No new compactness proof is required for each channel** — the perturbation lemma itself is of course new operator analysis.

**(i) The abelian screw decomposition.** For any finite abelian K/ℚ with Galois group G, g\_K \= Σ\_{χ ∈ Ĝ} g\_χ, and the prime-power coefficient of g\_K reads the splitting type: Σ\_χ χ(Frob\_{p^m}) \= |G| · 1\[Frob \= e\] at unramified p. **The screw kernel of an abelian field is a Frobenius detector.** All constants are derived, not fitted: the linear coefficient is β\_χ \= (L′/L)(½, χ) \= −½(ψ(c\_χ) − log(π/q\_χ)), forced by Λ′(½, χ) \= 0\.  
**(ii) The kink measure.** g\_χ is not analytic data but a distribution: g\_χ″ \= μ\_Λ^χ \+ 2β\_χδ₀ \+ T\_{c\_χ} − (pole), where μ\_Λ^χ \= Σ\_{p,m} χ(p^m)(log p)p^{−m/2}δ\_{m log p} is the **character-decorated prime-orbit measure**. This identifies the singular part of the screw kernel with an orbit measure and thereby states, exactly, what a dynamical realisation would have to produce: orbits carrying a Galois holonomy (POME-K, §7.3, OPEN).  
**(iii) A certified Weil audit.** The arithmetic side of the Weil functional is enclosed in rigorous intervals by ball arithmetic, with the prime tail bounded in closed form (Abel summation against ψ(x) \< 1.03883x) and the gamma-factor tail by a two-term Watson expansion. On the canonical 12-point grid inherited from earlier work, **0 of 48 channel entries is certifiably negative and the V₄ sum is CERTIFIED POSITIVE at all twelve grid points, without assuming GRH.** Historical negative readings on that grid are refuted. Positivity is further certified, by an interval Cholesky factorisation, on an **11-dimensional space** of test functions.

**(iv) Character-channel preconditioning — a certified case study.** Under GRH the Weil functional is a **sum of squares** over the zeros, W\_χ(v \* ṽ) \= Σ\_γ|v̂(γ)|². Retaining a **single** term therefore gives a rigorous lower bound, and for a Gaussian test packet of width a centred at t the retained term is governed by exp(−(γ\_cert − t)²/2a), where γ is any certified zero of the channel. For ζ, γ\_cert \= 14.1347 and the certified lower bound at (a,t) \= (0.2, 0\) is 1.28×10⁻²¹⁶; the closed-form prime-tail bound of §4 then guarantees a certified **sign** only after a cutoff of about **10³²**. But K carries a channel, χ₋₁₁, whose lowest zero is **2.477**, and the same one-term bound gives 5.83×10⁻⁶ — certified after a cutoff of **1.5×10⁶**.  
\*\*Certified prime budget at (a, t) \= (0.2, 0):  ζ alone ≈ 10³²;  the decorated audit ≈ 10⁶.  A collapse of 25.4 orders of magnitude.\*\*  
The sharpest form of the statement uses different currencies on the two sides. At the cutoff actually used, P \= 4×10⁶, the ζ enclosure at (0.2, 0\) is **UNDETERMINED** — and even **granting GRH** this method would need ≈ 10³² primes to decide its sign. At the same cutoff the V₄-decorated functional is **CERTIFIED POSITIVE with no arithmetic hypothesis at all.** **The decorated audit decides a sign the undecorated one cannot.**  
**And the effect obeys a law.** Equating the closed-form tail with the one-term target gives \*\*log N\*(a,t,γ) \= |γ − t|/a \+ 1/(2a) \+ …\*\* (Theorem T9; accurate to under one nat while log N\* ranges over 2.8–97.5). **The cost of a certified sign is linear in the distance from the test frequency to the nearest usable zero, divided by the Gaussian width.** The 25.4 orders are then not an accident of this field — they are (14.1347 − 2.4772)/0.2 nats, the law evaluated at K’s lowest certified zero.  
The effect is **not** a property of the conductor — the lowest zero of L(·,χ) is not monotone in q (6.02 at q \= 4, 6.65 at q \= 5; 2.48 at q \= 11, 3.12 at q \= 13). It is a property of **whether the character group contains a low-zero channel**. That is the correct and provable statement, and it is what makes the audit of §4–§5 computable at all. Whether enlarging a character family reliably supplies such a channel is left as a heuristic and an open problem (§6.7).

Nothing here proves or advances RH or GRH. **Global** positivity of the Weil functional on the full admissible test space is equivalent to GRH(ζ\_K); the finite-grid and finite-dimensional certificates established here are unconditional but do **not** imply it. §7 records the open operator frontier honestly, including a conditional lower bound on the assembly error of Suzuki’s finite-interval operator and the precise statement — the Weyl–truncation bridge — that would close the Herglotz route.

Keywords: screw function, Krein–Langer, extended Selberg class, Dedekind zeta, genus theory, Frobenius detector, Weil quadratic form, interval arithmetic, ball arithmetic, certification budget, preconditioning, prime-orbit measure.

# **§0.1 Epistemic status legend**

| STATUS | MEANING |
| ----- | ----- |
| PROVEN | Complete proof here; only classical theory as input. |
| IMPORTED | Proved externally; used without re-proof; cited. |
| DERIVED | Consequence of PROVEN/IMPORTED items; zero free parameters. |
| DERIVED-CONDITIONAL | Derived under a stated hypothesis (usually RH/GRH). |
| CERTIFIED | Numerical statement decided inside ball arithmetic with all truncations bounded in closed form. |
| VERIFIED | Numerical statement to a declared precision, with the error budget stated but not enclosed. |
| OPEN | Recognised gap with an explicit closure condition. |
| NON-CLAIM | Explicit statement of what is not established. |

# **§1. Introduction, contributions, and scope**

**Imported machinery.** (I1) \[2, Thm 1.1\]: for F in the extended Selberg class with no real zeros except possibly at ½, GRH(F) ⇔ ℜ(−g\_F(t)) ≥ 0 for t ≥ t₀. (I2) \[2, Thm 4.1\]: the zero-free closed form of g\_F. (I3) Krein–Langer \[4\]: g is a screw function iff the kernel K\_g(t,u) \= g(t−u) − g(t) − g(−u) \+ g(0) is positive semidefinite. (I4) Schoenberg \[5\]: ψ with ψ(0) \= 0 is conditionally negative definite iff exp(−τψ) is positive definite for all τ \> 0\. (I5) \[3\]: the finite-interval operator A\_a \= Friedrichs(D\*G\_aD) is self-adjoint, lower semibounded, with discrete spectrum; its a → ∞ limit is left conjectural.  
\*\*Sign conventions.\*\* K\_g ⪾ 0 ⇔ \*\*g is conditionally positive definite\*\* ⇔ −g is conditionally negative definite ⇔ exp(τg) is positive definite for every τ \> 0\. Under GRH, −g(t) \= Σ\_γ (1 − cos γt)/γ².

## **§1.1 Why this field**

K \= ℚ(√−3, √−11) is a small imaginary biquadratic field whose four genus characters have **pairwise distinct and small** conductors 1, 3, 11, 33 (disc K \= 1089 \= 33², and 1·3·11·33 \= 1089). It is therefore a compact four-channel laboratory in which the abelian decomposition of §2 is non-trivial in every channel, and — as §6 shows — the conductor 11 supplies a channel which carries a certified low-lying zero at 2.477, which is what makes the whole audit computable.

## **§1.2 Contributions and status**

| \# | Result | Status |
| ----- | ----- | ----- |
| T1 | Abelian screw decomposition g\_K \= Σ\_{χ∈Ĝ} g\_χ and the Frobenius coefficient layer Σ\_χ χ(Frob) \= |G|·1\[Frob \= e\] | PROVEN |
| T2 | Channel kernels with β\_χ \= (L′/L)(½,χ) forced by the functional equation | DERIVED (specialisation of I2) |
| T3 | No real zeros of L(σ,χ) on (0,1) for the three non-principal channels — the standing hypothesis of I1 | CERTIFIED |
| T4 | Kink-measure form: g\_χ″ \= μ\_Λ^χ \+ 2β\_χδ₀ \+ T\_{c\_χ} − (pole) | PROVEN \+ VERIFIED |
| T5 | Rigorous enclosures of the Weil functional; 0/48 negative; V₄ sum 12/12 positive \*\*without GRH\*\* | CERTIFIED |
| T6 | Weil form positive definite on an 11-dimensional test-function space (interval Cholesky) | CERTIFIED |
| T7 | One-term bound: W\_χ(F\_{a,t}) ≥ 2|v̂(γ\_cert(χ))|², hence W\_K ≥ 2|v̂(γ\_{cert,min}(K))|² — the budget is set by the smallest certified |γ − t| across channels | DERIVED-CONDITIONAL on GRH |
| T9 | \*\*Certification threshold law\*\*: log N\* \= d/a \+ 1/(2a) \+ (1/d)log(A/B) \+ 1/d² \+ O(1/d³), d \= |γ−t| — the cost of a certified sign is linear in the distance to the nearest usable zero over the Gaussian width; accurate to 2×10⁻⁴ nats where log N\* ≈ 73 | DERIVED-ASYMPTOTIC (d²/a ≳ 30\) \+ VERIFIED |
| T10 | \*\*Frobenius-resolved kernel\*\*: g\_h := (1/|G|)Σ\_χ χ̄(h)g\_χ has prime coefficients Λ(n)n^{−½}·1\[Frob \= h\] at every \*\*unramified\*\* p^m — a Chebotarev resolution of the kernel | PROVEN |
| T11 | \*\*Channel Perturbation Theorem\*\*: h\_χ″ is a finite signed measure on \[−2a,2a\] (the archimedean singularity cancels; the δ₀ mass is −log q\_χ), so q\_χ \= q\_ζ \+ (L²-bounded form). Suzuki’s ζ operator theorem therefore transfers to every \*\*real primitive\*\* Dirichlet channel (and hence to multiquadratic abelian Dedekind zetas; complex conjugate-pair channels need a separate realified block), with |λ\_n(A\_a^χ) − λ\_n(A\_a^ζ)| ≤ ‖ν\_{χ,a}‖\_TV | \*\*PROVEN\*\* |
| T12 | \*\*The Galois-graded operator\*\* 𝔄\_a on L²(−a,a) ⊗ ℂ\[G\]: self-adjoint, lower semibounded, discrete, G-equivariant, Ĝ-graded — unconditional, given T11 | DERIVED |
| O6 | POME-K and its pre-gate (§8.4): the unpruned map has infinitely many periodic points (DERIVED); the entropy and orbit-count conclusions are \*\*OPEN\*\* | OPEN |
| T8 | Certified case study: at (0.2, 0\) the ζ enclosure is undetermined and needs ≈ 10³² primes even granting GRH, while the decorated enclosure is certified positive \*\*unconditionally\*\* at an explicit cutoff P \= 4×10⁶ plus analytic tail — a 25.4-order collapse of the budget | CERTIFIED |
| O1 | POME-K: a dynamical realisation of g\_K must carry a Galois holonomy on its orbits (§7.3) | OPEN (pre-registered) |
| O4 | The family statement: does enlarging a character group reliably supply a low-zero channel? (§6.4) | OPEN / HEURISTIC |
| O2 | The Weyl–truncation bridge for the Herglotz route to RH | OPEN (load-bearing) |
| O3 | A rigorous ball-arithmetic assembly of Suzuki’s A\_a (the operator-norm error of a truncated assembly) | OPEN |

## **§1.3 Scope**

This paper does not prove or advance RH or GRH (NC-1). It consumes Λ(n)χ(n) as external arithmetic input and derives it from nothing (NC-2). The field K and its V₄ data are **given arithmetic input**; no derivation of K from any external structure is claimed (NC-3). The certified positivity results concern a finite grid and a finite-dimensional subspace; Weil positivity is the infinite-dimensional limit and is exactly GRH(ζ\_K) (NC-4). §7 lists what remains open, with closure conditions.

# **§2. The abelian screw decomposition**

## **§2.1 Channel kernels**

**Theorem T2 \[DERIVED\].** For χ primitive of conductor q\_χ and parity a\_χ, with c\_χ \= ¼ \+ a\_χ/2,  
g\_χ(t) \= Σ\_{n ≤ e^{|t|}} χ(n)Λ(n) n^{−½}(|t| − log n) \+ β\_χ|t| − ¼\[Φ(1,2,c\_χ) − e^{−2c\_χ|t|}Φ(e^{−2|t|},2,c\_χ)\],  
β\_χ \= −½(ψ(c\_χ) − log(π/q\_χ)),  
\*\*β\_χ is defined by the gamma-factor expression above\*\*, which makes sense for every primitive χ. \*\*When L(½, χ) ≠ 0\*\* — which §4.3 certifies for the three non-principal channels of K — the functional equation identifies it with (L′/L)(½, χ). Theorem T11 uses only the gamma-factor definition and therefore does not require a non-vanishing central value; the identification with the logarithmic derivative is used only where it is certified.

with the extra term −4(e^{|t|/2}+e^{−|t|/2}−2) when χ \= 1\. The coefficient β\_χ is **not a convention**: differentiating Λ(s,χ) \= ε(χ)Λ(1−s,χ) at s \= ½ with ε \= \+1 gives Λ′(½,χ) \= 0, hence (L′/L)(½,χ) \= −½(ψ(c\_χ) − log(π/q\_χ)) \= β\_χ. \[Certified against numerical logarithmic differentiation to 5×10⁻¹⁷.\]  
Table 2.1. The four channels of K. All ε(χ) \= \+1, so Λ(½+it,χ) is real (verified to 1.5×10⁻¹⁵).

| χ | q\_χ | a\_χ | c\_χ | β\_χ \= (L′/L)(½,χ) | certified low-lying zero γ\_cert |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 (ζ) | 1 | 0 | 1/4 | 2.6860917096 | 14.134725 |
| χ₋₃ | 3 | 1 | 3/4 | 0.5659892385 | 8.039737 |
| χ₋₁₁ | 11 | 1 | 3/4 | −0.0836522536 | \*\*2.477244\*\* |
| χ₃₃ | 33 | 0 | 1/4 | 0.9378379289 | 2.996951 |

The bold entry is the pivot of the whole paper: see §6.

## **§2.2 The decomposition and the Frobenius detector**

**Theorem T1 \[PROVEN\].** Let K/ℚ be finite abelian with group G and character group Ĝ (viewed as primitive Dirichlet characters). Then ξ\_K ∈ S♯♭ and  
g\_K(t) \= Σ\_{χ ∈ Ĝ} g\_χ(t);   and for p unramified,  Σ\_{χ ∈ Ĝ} χ(p^m) \= |G| · 1\[Frob\_{p^m} \= e\].  
Proof. ζ\_K \= ∏\_χ L(·,χ); S♯ is a multiplicative monoid, so ξ′/ξ is additive over the factorisation, and by \[2, (3.1)\] the transform ∫₀^∞ g\_F(t)e^{izt}dt \= z^{−2}(ξ′\_F/ξ\_F)(½ − iz) is additive; uniqueness of the inverse transform gives the first claim. The second is orthogonality of Ĝ.  
Table 2.2. Verified coefficient layer for K (|G| \= 4). Unramified values lie in {0, 4} for all n \< 2000 coprime to 33; Σχ(3^k) \= 2 for all k; Σχ(11^k) \= 2·1\[k even\] — the fingerprint of e \= f \= 2 at 11\.

| p | 2 | 3 | 5 | 7 | 11 | 13 | 31 | 37 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| Σχ(p) | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 4 |
| Σχ(p²) | 4 | 2 | 4 | 4 | 2 | 4 | 4 | 4 |

# **§3. The kink measure and the decorated prime-orbit target**

**Theorem T4 \[PROVEN \+ VERIFIED\].** On ℝ, as distributions,  
g\_χ″ \= μ\_Λ^χ \+ 2β\_χ δ₀ \+ T\_{c\_χ} − m\_χ(e^{|x|/2} \+ e^{−|x|/2}),   μ\_Λ^χ := Σ\_{p,m≥1} χ(p^m)(log p)p^{−m/2}(δ\_{m log p} \+ δ\_{−m log p}),  
where T\_c is **defined as the distribution** D²\[−¼Σ\_{k≥0}(1 − e^{−2(k+c)|x|})/(k+c)²\], with T\_c|\_{ℝ\\{0}} \= e^{−2c|x|}/(1 − e^{−2|x|}) ∼ 1/(2|x|) — which is **not locally integrable at 0**, so T\_c and not ω\_c is the correct object. Proof: (|x| − L)₊″ \= δ\_L \+ δ\_{−L}; |x|″ \= 2δ₀; and the Lerch series differentiates term by term. \[VERIFIED: the jump of g\_χ′ at log n equals χ(n)Λ(n)n^{−½} to 8×10⁻⁶ at ten kinks per channel.\]  
This is the Weil explicit formula written **on the kernel** rather than on test functions, and it is the form in which the kernel meets a dynamical system: the singular part of g\_χ″ **is** a weighted orbit measure.

The kink-measure identity also supplies a precise \*\*decorated orbit-measure target\*\*: any dynamical system whose Ruelle zeta reproduces g\_K must have primitive orbits carrying a Galois holonomy h\_γ ∈ Gal(K/ℚ) with Σ\_{γ,m} χ(h\_γ^m)ℓ\_γ e^{−mℓ\_γ/2}δ\_{mℓ\_γ} \= μ\_Λ^χ for every χ. Its dynamical realisation is left open and is discussed in the Outlook (§7.3).

# **§4. The certified Weil audit**

## **§4.1 The two sides, and the two tails**

For v(x) \= e^{−ax²}cos(tx) and F \= v \* ṽ, integration by parts against the screw kernel gives exactly  
W\_χ(F) \= −∫\_ℝ g\_χ(x)F″(x)dx \= Σ\_γ |v̂(γ)|²   (the zero side, a sum of squares under GRH).  
The arithmetic side is enclosed in ball arithmetic; the only two truncations are bounded in closed form.  
**(R1) Prime tail.** With G(u) \= C(1+κ)e^{−au²/2} ≥ |F(u)|, Abel summation against ψ(x) \< 1.03883x (Rosser–Schoenfeld) and completion of the square give  
|E\_P| ≤ 2·1.03883·C(1+κ)e^{1/(8a)}\[e^{−as₀²/2} \+ √(π/2a)·erfc(s₀√(a/2))\],   s₀ \= log N − 1/(2a).  
**(R2) Gamma-factor tail.** F is entire and even, so F′(0) \= F‴(0) \= F⁽⁵⁾(0) \= 0 and Watson’s lemma with explicit remainder gives  
|½Σ\_{k≥K} J(2μ\_k)/μ\_k² − ½\[F″(0)ζ(3,K+c)/2 \+ F⁽⁴⁾(0)ζ(5,K+c)/8\]| ≤ ‖F⁽⁶⁾‖\_∞ · ζ(7,K+c)/64,  
with ‖F⁽⁶⁾‖\_∞ ≤ (1/2π)∫r⁶F̂(r)dr — a Gaussian sixth moment, legitimate because F̂ \= |v̂|² ≥ 0\. Both remainders are controlled by explicit analytic bounds; **no numerical quadrature is used for either tail**.

## **§4.2 Theorem T5 \[CERTIFIED\]**

On the canonical grid (a,t) ∈ {0.2, 0.5, 1.0} × {0, 1, 5, 14.13}, the interval \[L, U\] provably contains W\_χ(F\_{a,t}). **The certificate sums prime powers explicitly through P \= 4×10⁶ and encloses the remainder analytically** by the closed-form tail (R1), whose value at a \= 0.2 is then ≈ 1.1×10⁻⁶, comfortably below the V₄ target of 6.8×10⁻⁶. All statements below refer to that protocol: explicit summation to 4×10⁶ plus a rigorous analytic tail.) for each of the 48 entries. **No entry is certifiably negative; 33 are certifiably positive; and the V₄ sum Σ\_χ W\_χ is certifiably positive at all twelve grid points.** No arithmetic hypothesis is used — in particular GRH is not assumed.  
Table 4.1. The V₄-summed Weil functional on the canonical grid (arb, 320 bits). All twelve certified positive.

| (a, t) | L | U | verdict |
| ----- | ----- | ----- | ----- |
| (0.2, 0\) | 6.182e-6 | 7.573e-6 | POSITIVE |
| (0.2, 1\) | 3.392e-2 | 3.392e-2 | POSITIVE |
| (0.2, 5\) | 3.859e+0 | 3.859e+0 | POSITIVE |
| (0.2, 14.13) | 1.520e+1 | 1.520e+1 | POSITIVE |
| (0.5, 0\) | 2.875e-2 | 2.875e-2 | POSITIVE |
| (0.5, 1\) | 4.179e-1 | 4.179e-1 | POSITIVE |
| (0.5, 5\) | 3.023e+0 | 3.023e+0 | POSITIVE |
| (0.5, 14.13) | 9.217e+0 | 9.217e+0 | POSITIVE |
| (1.0, 0\) | 3.629e-1 | 3.629e-1 | POSITIVE |
| (1.0, 1\) | 8.597e-1 | 8.597e-1 | POSITIVE |
| (1.0, 5\) | 2.613e+0 | 2.613e+0 | POSITIVE |
| (1.0, 14.13) | 6.692e+0 | 6.692e+0 | POSITIVE |

Historical readings of ‘negative’ entries on this grid (5/12, 4/12, 1/12 in earlier internal work) are \*\*refuted\*\*: they were the sign of a truncation error. The complete 48-entry table and the per-channel verdicts are in the Supplement.

## **§4.3 Theorem T3 \[CERTIFIED\] — the standing hypothesis of (I1)**

(I1) requires that L(·,χ) have no real zeros in (0,1). The functional equation with a positive gamma factor reduces this to L \> 0 on \[½, 1\]. On \[½, 0.9\] we certify by adaptively subdivided Hurwitz-zeta balls; near s \= 1 that representation is useless to interval arithmetic (the poles cancel only because Σχ(r) \= 0, a cancellation an interval evaluation cannot see), so on \[0.9, 1\] we use a truncated Dirichlet series with the rigorous Abel remainder |Σ\_{n\>M}χ(n)n^{−σ}| ≤ 2B\_χ M^{−σ}, B\_χ \= max\_x|Σ\_{n≤x}χ(n)| \= 1, 3, 3\. Every enclosure is strictly positive.

# **§5. Positivity on a finite-dimensional space**

A grid of twelve test functions is twelve points. The natural strengthening is a **space**. With v\_j(x) \= e^{−ax²}cos(jx), a \= ½, V\_N \= span{v\_0,…,v\_{N−1}}, the Gram entries have the closed form  
v\_j \* ṽ\_k \= A₁ e^{−ax²/2}cos(ω₁x) \+ A₂ e^{−ax²/2}cos(ω₂x),  ω\_{1,2} \= (t\_j ± t\_k)/2,  A\_{1,2} \= ½√(π/2a)e^{−(t\_j ∓ t\_k)²/(8a)},  
so every entry of M\_N is two evaluations of the same shape functional that §4 already encloses.  
**Theorem T6 \[CERTIFIED\].** With P\_max \= 2×10⁶ and K \= 6000, the V₄ Weil form is positive definite on V\_N for every N ≤ 11\. The certificate is an **interval Cholesky**: with L the Cholesky factor of mid(M\_N) (80 digits, then treated as exact), E := L⁻¹M\_N L⁻ᵀ − I is computed in ball arithmetic and ‖E‖\_F \< 1 is certified; then M\_N \= L(I+E)Lᵀ ≻ 0\.  
Table 5.1. Interval Cholesky certificate. The λ\_min column is descriptive (a high-precision midpoint eigenvalue); the certificate is ‖E‖\_F.

| N | λ\_min(mid M\_N) | certified ‖E‖\_F | verdict |
| ----- | ----- | ----- | ----- |
| 4 | 1.572e-09 | 6.80e-19 | CERTIFIED M\_N ≻ 0 |
| 6 | 6.322e-13 | 3.11e-14 | CERTIFIED M\_N ≻ 0 |
| 8 | 2.220e-15 | 2.45e-04 | CERTIFIED M\_N ≻ 0 |
| 10 | 1.166e-17 | 4.68e-02 | CERTIFIED M\_N ≻ 0 |
| 11 | 8.674e-19 | 6.28e-01 | CERTIFIED M\_N ≻ 0 |
| 12 | — | 1.67e+00 | not certified |

\*\*Scope.\*\* V\_N is the fixed-width family a \= ½ with integer frequencies; it contains three of the twelve canonical test functions, namely (a,t) \= (0.5, 0), (0.5, 1), (0.5, 5). What is certified is positivity on an entire 11-dimensional space, i.e. on an uncountable family, not at isolated points.

# **§6. Character-channel preconditioning**

This section is the new contribution. It is independent of the operator-theoretic programme; it is a statement about **how to compute**; and it is what makes §4 and §5 possible.

## **§6.1 One term of a sum of squares**

Under GRH the Weil functional is a Gram evaluation against the zeros, W\_χ(v \* ṽ) \= Σ\_γ|v̂(γ)|². Every summand is a **square**, so retaining any single zero gives a rigorous lower bound. Retaining the lowest:  
\*\*Theorem T7 (one-term bound) \[DERIVED-CONDITIONAL on GRH\].\*\*   W\_χ(F\_{a,t}) ≥ 2 |v̂\_{a,t}(γ)|²   for \*\*any\*\* zero γ of the channel \= (π/2a)·\[ e^{−(γ−t)²/4a} \+ e^{−(γ+t)²/4a} \]²,  
and for a finite abelian K with character group Ĝ, since W\_K \= Σ\_χ W\_χ with every term non-negative,  
W\_K(F\_{a,t}) ≥ 2 |v̂\_{a,t}(γ\_low)|²   for \*\*any\*\* certified zero γ\_low of \*\*any\*\* channel of K.  
**The budget is therefore set by one number: the smallest |γ − t| among the certified zeros of all channels.** The bound is computed inside ball arithmetic: γ is enclosed by a strict sign change of Λ(½ \+ iγ, χ) in arb, and |v̂|² is bounded below on the bracket by monotonicity of each Gaussian in the distance from its centre.  
\*\*Firstness is not claimed.\*\* A sign change certifies a zero of \*\*odd multiplicity\*\* in the bracket; it does not exclude a lower zero of even multiplicity, nor an undetected pair. \*\*Nothing in T7–T9 needs firstness\*\*: the zero side is a sum of non-negative terms, so \*\*one certified low-lying zero suffices\*\*. A genuine first-zero claim would need a Turing-type zero count, which is not run here; the OPEN registry says so.

## **§6.2 Theorem T9 — the certification threshold law**

T7 says the budget is set by one number. **T9 says exactly which number, and how.** Equate the closed-form tail (R1) with the one-term target of T7. Writing s₀ \= log N − 1/(2a), the tail is A(a,t)·e^{−a s₀²/2}(1 \+ O(1/(a s₀))) with A(a,t) \= 2·1.03883·C(1+κ)e^{1/(8a)}, and the target is (π/2a)·e^{−(γ−t)²/(2a)}(1 \+ o(1)). Solving for s₀:  
\*\*Theorem T9 (Certification Threshold Law) \[DERIVED-ASYMPTOTIC in d²/a → ∞; VERIFIED\].\*\*   log N\*(a, t, γ) \= \*\*d/a\*\*  \+  1/(2a)  \+  (1/d)·log( A(a,t)/B(a,t,γ) )  \+  \*\*1/d²\*\*  −  (1 \+ aL²)/(2d³)  \+  O\_{a,t}(d⁻⁴),   d := |γ − t|,  L := log(A/B),  
with A(a,t) \= 2·1.03883·C(1+κ)e^{1/(8a)} the tail prefactor and **B(a,t,γ) \= (π/2a)·(1 \+ e^{−γt/a})²** the target prefactor — note the factor (1+e^{−γt/a})², which equals **4** at t \= 0 because the two Gaussian lobes of v̂ coincide there.  
**The cost of a certified sign is linear in the distance from the test frequency to the nearest usable zero, divided by the Gaussian width.** The subleading term is a single logarithm over d. The expansion is asymptotic in d²/a; near resonance (d²/a ≲ 1\) it breaks down and the tail bound must be inverted directly, which is what the code does.  
**The 1/d² term is derived, not fitted.** The erfc part of the tail contributes a factor \[1 \+ 1/(a s₀) − 1/(a²s₀³) \+ …\]; substituting s₀ \= d/a \+ δ and expanding gives dδ \+ (a/2)δ² \= L \+ 1/d − 1/(2d²) \+ O(d⁻³) with L := log(A/B), hence  
δ \= L/d \+ 1/d² − (1 \+ aL²)/(2d³) \+ O(d⁻⁴).  
\*\*Correction to the previous version.\*\* It claimed ‘the remainder is independent of a’. That is false, and is \*\*retracted\*\*: only the \*\*universal 1/d² coefficient\*\* is independent of a. The next coefficient, −(1 \+ aL²)/2, depends on both a and L. What the a-independence of the 1/d² term does explain is the striking constancy of the residual across a \= 0.15 … 1.0 in Table 6.1.

\*\*Accuracy (Table 6.1).\*\* With the 1/d² term the residual is O(1/d³). At γ \= 14.13 the law is accurate to \*\*2×10⁻⁴ nats\*\* while log N\* runs from 14.6 to 97.5 — a relative accuracy of 2×10⁻⁶ — and this holds unchanged for a \= 0.15, 0.2, 0.3, 0.5, 0.8, 1.0. At γ \= 8.04 it is 1×10⁻³; at γ \= 2.48 (d²/a ≈ 31, the edge of the regime) it is 0.03. Below d²/a ≈ 30 the expansion is not used: the tail bound is inverted directly in arb.

Table 6.1. Theorem T9 (closed form, with the derived 1/d² term) against the exact cutoff obtained by inverting the tail bound in arb. ‘v2.3’ is the law without the 1/d² term, shown for contrast.

| (a, t) | γ | exact log N\* | d²/a | law error (no 1/d²) | \*\*law error (T9)\*\* |
| ----- | ----- | ----- | ----- | ----- | ----- |
| (0.15, 0\) | 14.135 | 97.499 | 1332 | −0.0048 | \*\*+0.00019\*\* |
| (0.20, 0\) | 14.135 | 73.103 | 999 | −0.0048 | \*\*+0.00020\*\* |
| (0.30, 0\) | 14.135 | 48.712 | 666 | −0.0048 | \*\*+0.00022\*\* |
| (0.50, 0\) | 14.135 | 29.205 | 400 | −0.0048 | \*\*+0.00024\*\* |
| (1.00, 0\) | 14.135 | 14.586 | 200 | −0.0048 | \*\*+0.00026\*\* |
| (0.20, 0\) | 8.040 | 42.581 | 323 | −0.0144 | \+0.0011 |
| (0.50, 1\) | 8.040 | 15.102 | 99 | −0.0187 | \+0.0015 |
| (0.20, 0\) | 2.477 | 14.591 | 31 | −0.1325 | \+0.0305 |

**Corollary T9a (the preconditioning gain, in closed form) \[DERIVED\].** Replacing the ζ channel’s usable zero by a low-lying zero of a decorated channel changes the certified budget by  
Δ log N\*  \=  ( |γ\_ζ − t| − |γ\_low − t| ) / a  \+  O( a·log(·)/|γ| ),  
which at (a, t) \= (0.2, 0\) with γ\_ζ \= 14.1347 and γ\_low \= 2.4772 gives (14.1347 − 2.4772)/0.2 \= **58.29 nats \= 25.31 decimal orders** — matching the certified value of 25.4 in Table 6.2. **The 25 orders are not a coincidence of this field: they are the law evaluated at this field’s lowest certified zero.**  
\*\*Why this is the theoretical content, and not merely a computation.\*\* T9 turns the question ‘can this Weil functional be audited?’ into an arithmetic one: \*how far is the nearest zero, in units of the test width?\* It predicts the cost before any computation is run; it explains why the ζ audit at low frequency is hopeless (γ\_cert/a \= 70 nats) and why the decorated audit is routine (γ\_low/a \= 12 nats); and it converts the choice of field into an optimisation — minimise |γ − t| over the channels. To our knowledge no such law has been stated.

## **§6.3 Theorem T8 \[CERTIFIED case study\] — the budget collapse for K**

Inverting the closed-form prime tail (R1) of §4.1 gives, for a target τ, the cutoff N\*(a,t,τ) at which |E\_P| \< τ — the **certification budget**: the price, in primes, that \*this method\* must pay for a legible sign. Applying it to the one-term bounds of §6.1, entirely in ball arithmetic:  
Table 6.2. Certified zero brackets (strict ball sign changes of Λ(½+iγ,χ)) and the resulting certified budgets. the smallest certified sign-change zero found is 2.477, supplied by χ₋₁₁. The last column uses the \*\*unconditional\*\* arithmetic enclosure of §4.2 as the decorated target — no GRH — against the GRH-conditional one-term bound of the ζ channel. Every entry is decided in arb (blocks D0–D6, 16/16 PASS).

| χ | certified γ bracket | (a,t) | one-term LB (GRH) | log N\* | uncond. V₄ target → log N\* | gain over ζ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| ζ | \[14.130, 14.150\] | (0.2, 0\) | 1.283e-216 | 73.2 | — | — |
| χ₋₁₁ / V₄ | \[2.470, 2.490\] | (0.2, 0\) | 5.827e-06 | 14.7 | 6.182e-06 → 14.6 | \*\*25.4 orders\*\* |
| ζ | \[14.130, 14.150\] | (0.2, 1\) | 1.402e-187 | 68.2 | — | — |
| χ₋₁₁ / V₄ | \[2.470, 2.490\] | (0.2, 1\) | 3.052e-02 | 10.1 | 3.392e-02 → 10.0 | \*\*25.3 orders\*\* |
| ζ | \[14.130, 14.150\] | (0.5, 0\) | 1.392e-86 | 29.2 | — | — |
| χ₋₁₁ / V₄ | \[2.470, 2.490\] | (0.5, 0\) | 2.550e-02 | 5.7 | 2.875e-02 → 5.7 | \*\*10.2 orders\*\* |
| ζ | \[14.130, 14.150\] | (1.0, 0\) | 2.091e-43 | 14.6 | — | — |
| χ₋₁₁ / V₄ | \[2.470, 2.490\] | (1.0, 0\) | 2.830e-01 | 5.0 | 3.629e-01 → 5.0 | 4.2 orders |

## **§6.4 The unconditional form of the comparison — and why it is the strongest one**

Theorem T7 is GRH-conditional on both sides, which makes the comparison fair but not maximally sharp. The sharp form uses **different currencies on the two sides**, and it is the honest one:

 • On the ζ side we **grant GRH**. Even then, the one-term bound is 1.283×10⁻²¹⁶ and the present tail bound certifies the sign only after a cutoff of ≈ 10³². At the cutoff actually used, P \= 4×10⁶, the ζ enclosure at (0.2, 0\) is **UNDETERMINED**: the interval contains zero.  
 • On the decorated side we **grant nothing**. The arithmetic enclosure of §4.2 is unconditional — it uses only the explicit formula, the Chebyshev bound ψ(x) \< 1.03883x, and ball arithmetic — and at the same cutoff it gives \[6.182×10⁻⁶, 7.573×10⁻⁶\]: **CERTIFIED POSITIVE, without GRH.**

**Theorem T8 (unconditional form) \[CERTIFIED\].** At (a, t) \= (0.2, 0\) and P \= 4×10⁶: the ζ channel’s sign is not decided, and — granting GRH — this method would need about 10³² primes to decide it; the V₄-decorated functional’s sign **is** decided, positively, with no arithmetic hypothesis whatever. **The decorated audit sees a sign that the undecorated one cannot.**  
This is the form to quote. It does not compare two conditional bounds; it compares \*what can be certified\* with \*what cannot\*, at the same computational cost, on the same grid point.

## **§6.5 What the table does NOT say**

\*\*Two statements this table does NOT make.\*\* (a) 1.283×10⁻²¹⁶ is \*\*not\*\* the true value of W\_ζ at (0.2, 0); it is a certified GRH-conditional \*\*lower bound\*\* — the omitted zeros contribute positively. (b) 10³² is \*\*not\*\* an information-theoretic minimum; it is the cutoff at which the \*\*present closed-form tail bound\*\* guarantees a certified sign. A sharper tail bound, or a different method, could do better. What the table does say is that with \*this\* protocol, and on this grid, the decorated audit is certified 25 orders of magnitude more cheaply.

## **§6.6 Why the historical negatives happened**

**Corollary \[DERIVED\].** Earlier computations on this grid used P\_max \= 500\. At a \= 0.2 the closed-form prime-tail bound at that cutoff is of order 10⁻¹, while the signal at the worst grid point is below 10⁻²¹⁶. **The sign that was read was the sign of the truncation error.** The remedy is not more primes — no attainable cutoff repairs the ζ channel at low frequency — it is the low-zero channel.  
\*\*The one-sentence export.\*\* \*A negative truncated Weil or screw computation is scientifically meaningless unless it comes with an error enclosure smaller than the target margin; at low frequency on ζ no attainable enclosure is; and a character decomposition containing a low-zero channel supplies one.\*

## **§6.7 The generalisation is open, and the obvious guess is wrong**

It is tempting to say that a larger conductor gives a lower first zero (i.e. a lower γ\_cert), since the zero density of L(·,χ) is (1/2π)log(qT/2πe). **That is false as stated.** The smallest certified sign-change zeros found for the real primitive characters of small conductor are

| q | 1 (ζ) | 3 | 4 | 5 | 7 | 11 | 13 | 33 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| γ\_cert | 14.1347 | 8.0397 | 6.0210 | 6.6485 | 4.4757 | \*\*2.4772\*\* | 3.1193 | 2.9970 |

— not monotone (6.02 at q \= 4 but 6.65 at q \= 5; 2.48 at q \= 11 but 3.12 at q \= 13). The density heuristic controls an **average**, not the first zero of an individual L-function.

**Conjectural design principle \[HEURISTIC / OPEN\].** A character decomposition containing a low-zero channel acts as a numerical preconditioner for a finite Weil audit; and since γ\_cert is, empirically, a roughly independent draw per channel, enlarging the character group raises the chance that γ\_cert^{min} is small. Quantifying that — e.g. a bound on the expected γ\_cert^{min} over the genus characters of K as a function of |G| and disc K — is open. **What is established here is the mechanism (T7) and the case (T8); the family statement is a target, not a theorem.**

## **§6.8 Two further failure modes of numerical Weil work**

**(a) The margin collapses with dimension.** On the certified range 2 ≤ N ≤ 10 of §5, log₁₀λ\_min(M\_N) ≈ −1.677N − 1.136 (least squares; descriptive, no asymptotic law claimed). The Weil form is the Gram matrix of the zero-evaluation map, so its **effective numerical rank** is bounded by the number of zeros the subspace resolves in its frequency window. Certification buys dimensions, not the theorem: the tail step is GRH.  
**(b) A truncated kernel needs all primes to e^{2a}.** Any finite-interval construction from g on \[−a,a\] evaluates the kernel at |t| ≤ 2a, and the prime part of g at t carries every prime power n ≤ e^{|t|}; so exact assembly needs **all** prime powers to e^{2a}. (The cutoff is already visible in Suzuki’s own finite-interval form; the contribution here is to read it as a budget.) A **fixed** shortfall δ in the log-cutoff costs, pointwise at t \= 2a, ½ e^{a}δ² \+ O(e^aδ³) — an error that **grows with a**. The corresponding operator-norm bound ‖ΔA\_a(P)‖ ≤ ∫\_{log P}^{2a}|Δg\_P(t)|·‖Q\_a(t)‖dt has **not** been evaluated (O3). With the prime table cut at e⁸ instead of e¹⁶, the screw margin of the K-kernel at a \= 8 returns −29424.7 instead of \+0.204.

# **§7. The open operator frontier**

**The operator programmes in this section remain open; several supporting propositions and no-go results are established.** They are recorded because the closure conditions are precise, and because two of them were reached by eliminating wrong answers.

## **§7.1 Suzuki’s finite-a operator: two tracks, not one**

\[3\] proves (I5) that A\_a is self-adjoint, lower semibounded, with discrete spectrum. It does **not** prove A\_a ⪾ 0 — positivity for all a is RH-equivalent. Two distinct conjectural limits must not be conflated:  
 **Track G** (the motivating statement): c\_a·v̂\_a(z) → ξ(½ \+ iz) for the ground vector v\_a.  
 **Track W** (the main conjectural statement of \[3\]): with boundary data W(a, θ; z) of the self-adjoint extensions and a normalisation ϕ(a,z), e^{ϕ}W(a,θ;z) → z² ξ′/ξ(½ − iz).  
This paper constructs neither. It supplies the budget for constructing them (§6.4(b)) and the following lemma, which is what a pilot computation can legitimately yield.

**Lemma 7.1 (conditional assembly-error lower bound) \[DERIVED-CONDITIONAL on RH\].** Let B\* be the exact Galerkin form matrix of A\_a in a basis, B\_num a computed approximation, and c a normalised coefficient vector. If a zero-side partial sum gives a lower bound L\_T(c) ≤ c\*B\*c (legitimate under RH, since c\*B\*c \= Σ\_γ |f̂\_c(γ)|²/γ² is a sum of squares with f \= Du), and if c\*B\_num c \< 0, then  
‖B\* − B\_num‖₂ ≥ |c\*(B\* − B\_num)c| ≥ L\_T(c) − c\*B\_num c \> 0\.  
This **bounds the assembly error from below**. It does **not** determine λ\_min(B\*) nor the scale of the true quadratic form: a partial sum of a positive series is a lower bound only, and a Rayleigh quotient at one vector bounds λ\_min from **above**, not below. \[A pilot float64 assembly at a \= 3, 4 gives ‖ΔB‖₂ ≳ 5.9×10⁻⁶ and ≳ 3.1×10⁻⁵ respectively. These are diagnostics, not certificates; the numbers and the code are in the Supplement.\]  
\*\*Two errors are recorded here so they are not repeated.\*\* (i) A negative computed λ₀ does \*\*not\*\* certify an assembly error, because A\_a ⪾ 0 is not an unconditional theorem. (ii) A small zero-side partial sum does \*\*not\*\* show that the true form value is small. Both were asserted in internal drafts and are retracted; see the Supplement.

## **§7.2 The Herglotz route, and the one statement that would close it**

Set M(z) := i(ξ′/ξ)(½ − iz) on ℂ₊. Four things are proved.  
**(a) \[PROVEN\]** M is Herglotz on ℂ₊ **iff** RH. (⇒) a Herglotz function is holomorphic, and an off-line zero gives M a pole in ℂ₊. (⇐) under RH the Hadamard product gives M(z) \= Σ\_{γ\>0} m\_γ\[1/(γ−z) \+ 1/(−γ−z)\] (the compensating −1/γ terms cancel pairwise, and ξ′(½) \= 0 by evenness), and each summand has positive imaginary part on ℂ₊.  
**(b) \[PROVEN\]** |g(t)| ≤ 20(1+t)e^{t/2} (Abel \+ Chebyshev), and for ℑz \> ½, M(z) \= i z²∫₀^∞ g(t)e^{izt}dt with  
|M(z) − m\_a^{trunc}(z)| ≤ |z|²·20·e^{−(ℑz−½)·2a}\[(1+2a)/(ℑz−½) \+ 1/(ℑz−½)²\],   m\_a^{trunc}(z) := iz²∫₀^{2a} g e^{izt}dt.  
**(c) \[PROVEN\]** If (m\_a) are Weyl functions of self-adjoint operators (hence Herglotz on all of ℂ₊), sup\_a|m\_a(i)| \< ∞, and m\_a → M uniformly on **one** compact of {ℑz \> ½}, then RH. (Herglotz normal families \+ identity theorem \+ no poles.)  
**(d) \[PROVEN, negative\]** m\_a^{trunc} is **not** Herglotz — iz² times the transform of a compactly supported kernel is entire of exponential type, and a non-affine entire Herglotz function does not exist. So the naive shortcut is closed.

**Therefore the whole gate is \[OPEN\]:**

| \# | Condition | Status |
| ----- | ----- | ----- |
| S′1 | Fix a canonical Weyl function: A\_a alone does not determine m\_a — a boundary triple, or a cyclic vector and normalisation, must be chosen. | OPEN |
| S′2 | sup\_a|m\_a(i)| \< ∞. Since m\_a(i) \= α\_a \+ i(β\_a \+ ∫dτ\_a/(1+t²)), this is equivalent to a bound on α\_a \*\*and\*\* on β\_a \+ ∫dτ\_a/(1+t²) — not on the measure alone. | OPEN |
| S′3 | \*\*The Weyl–truncation bridge:\*\* sup\_{z∈K}|m\_a(z) − m\_a^{trunc}(z)| → 0 on one compact of {ℑz \> ½}. With (b) this is equivalent to m\_a → M. | \*\*OPEN — load-bearing\*\* |

Convergence of Weyl functions is governed by Grommer–Hamburger: m\_a → M locally uniformly iff α\_a → α, τ\_a → τ vaguely, \*\*and\*\* β\_a \+ ∫dτ\_a/(1+t²) → β \+ ∫dτ/(1+t²). Separate convergence of β\_a, and weak convergence of the weighted measures, do \*\*not\*\* follow — spectral mass escaping to infinity can be converted into the linear coefficient (take τ\_n \= n²δ\_n, α\_n \= β\_n \= 0: then m\_n → z, whose β is 1).

## **§7.3 Outlook: the decorated orbit-measure target (POME-K)**

Theorem T4 identifies the singular part of g\_χ″ with a **character-decorated prime-orbit measure**. That turns a vague programme — ‘realise ζ as a dynamical zeta’ — into an explicit and falsifiable one. Write μ\_IT^χ \= Σ\_{γ,m} χ(h\_γ^m)ℓ\_γ e^{−mℓ\_γ/2}δ\_{mℓ\_γ} for a flow whose primitive orbits carry a holonomy h\_γ ∈ Gal(K/ℚ). Under local finiteness and absolute convergence of the dynamical Euler product for ℜs \> 1 with Z\_IT → 1 at ∞,  
\*\*POME-K \[OPEN, PRE-REGISTERED\]:\*\*  μ\_IT^χ \= μ\_Λ^χ for every χ ∈ Ĝ  ⇔  Z\_{IT,χ}(s) \= L(s, χ)  for every χ.  
(The kernel step: if D²h \= 0 then h is affine; h even kills the linear term; h(0) \= 0 kills the constant. So equality of the atomic parts on ℝ\\{0} forces equality of the kernels, hence of ξ′/ξ.) **The decoration is what gives the target teeth.** A candidate dynamics whose orbit lengths are right but whose holonomy is trivial passes a ζ-only test and fails three of the four decorated ones; a single-channel test cannot see that.  
The dynamical realisation of POME-K, and the pre-gate that constrains it, are discussed in §8.4.

## **§7.4 What is not claimed**

NC-1. No progress on RH or GRH. NC-2. Λ(n)χ(n) is external input; nothing here derives the primes. NC-3. K and its V₄ data are given arithmetic input. NC-4. §4 certifies twelve test functions and §5 an 11-dimensional space; Weil positivity is the limit and is exactly GRH(ζ\_K). NC-5. Track G and Track W are untested; the pilot assembly of §7.1 has no evidential status. NC-6. POME-K is a target, not a result. NC-7. To our knowledge no certified numerical implementation of Suzuki’s A\_a has been published; we claim no more than that.

# **§8. Frobenius resolution, and a conditional outlook**

## **§8.1 Theorem T10 — the Frobenius-resolved kernel \[PROVEN\]**

The decomposition of §2 splits the kernel by **character**. Inverting the finite Fourier transform on Ĝ splits it by **Frobenius class**. For h ∈ G \= Gal(K/ℚ) define the **Frobenius-resolved kernel component**  
g\_h(t) := (1/|G|) Σ\_{χ ∈ Ĝ} χ̄(h)·g\_χ(t).  
**Theorem T10 \[PROVEN\].** For every **unramified** prime power n \= p^m (p ∤ disc K), the prime coefficient of g\_h at n is  
Λ(n)·n^{−½}·\*\*1\[ Frob\_{p^m} \= h \]\*\*.  
Proof. The coefficient is (1/|G|)Λ(n)n^{−½} Σ\_χ χ̄(h)χ(Frob\_{p^m}), and orthogonality of Ĝ gives |G|·1\[Frob \= h\]. \[VERIFIED: zero mismatches for every n \< 400 coprime to 33 and every h ∈ V₄. The ramified primes 3 and 11 are excluded, as they must be: Frobenius is defined only at unramified places.\]  
\*\*What T10 is, precisely.\*\* g\_e sees only the totally split primes; each g\_h sees only the primes with Frobenius h. This is a \*\*Chebotarev resolution of the screw kernel\*\* — an arithmetic decomposition with no counterpart for ζ. It is \*\*not\*\* a claim that g\_h is itself a screw function: a signed combination of conditionally positive definite functions need not be conditionally positive definite, and we make no such claim. The correct name is \*Frobenius-resolved kernel component\*.

## **§8.2 Theorem T11 — the Channel Perturbation Theorem \[PROVEN\]**

Suzuki’s finite-interval theorem (I5) is proved for **ζ**. It does not follow, and cannot simply be assumed, that for each Dirichlet character the localised form is closable, lower semibounded, has a form core and a compact resolvent. **We prove it, by a bounded-form perturbation whose norm we compute.**

**Lemma T11a (the singularities cancel) \[PROVEN\].** For x ≠ 0, ω\_c(x) \= e^{−2c|x|}/(1 − e^{−2|x|}) ∼ 1/(2|x|), the **same** leading singularity for every c. In the difference the singularity cancels exactly:  
ω\_{c\_χ}(x) − ω\_{1/4}(x) \= \[e^{−2c\_χ|x|} − e^{−|x|/2}\] / (1 − e^{−2|x|})  ⟶  \*\*¼ − c\_χ\*\*   as x → 0,  
so the difference extends to a bounded continuous function on ℝ. Moreover ψ := Φ\_{c\_χ} − Φ\_{1/4} (the antiderivative pair of §3) has a **finite** one-sided derivative ψ′(0+) \= ½(ψ\_{dg}(c\_χ) − ψ\_{dg}(¼)), because Σ\_k\[1/(k+c) − 1/(k+¼)\] converges absolutely — whereas each Φ separately has a logarithmically divergent derivative at 0\. Hence T\_{c\_χ} − T\_{1/4} \= (ω\_{c\_χ} − ω\_{1/4})·dx \+ 2ψ′(0+)·δ₀.

**Lemma T11b (the difference kernel has a finite second derivative measure) \[PROVEN\].** Put h\_χ := g\_χ − g\_ζ. Then on any interval \[−2a, 2a\],  
h\_χ″ \= ν\_{χ,a}  \=  \*\*−(log q\_χ)·δ₀\*\*  \+  Σ\_{n ≤ e^{2a}} (χ(n)−1)Λ(n)n^{−½}(δ\_{log n} \+ δ\_{−log n})  \+  \[ω\_{c\_χ} − ω\_{1/4} \+ e^{|x|/2} \+ e^{−|x|/2}\]·dx,  
a **finite signed Radon measure**: finitely many prime atoms (only n ≤ e^{2a} contribute on this interval), one point mass, and a bounded density. The δ₀ coefficient is exactly −log q\_χ, because 2(β\_χ − β\_ζ) \+ 2ψ′(0+) \= −log q\_χ — the digamma terms cancel and only the conductor survives. \[VERIFIED to 10⁻⁸: −1.09861 \= −log 3, −2.39790 \= −log 11, −3.49651 \= −log 33.\]

**Theorem T11 (Channel Perturbation) \[PROVEN\].** Let u ∈ C\_c^∞(−a, a) and U := u \* ũ. Since Du has mean zero and (Du) \* (Du)̃ \= −U″, the localised Weil forms differ by  
q\_χ\[u\] − q\_ζ\[u\] \= −⟨h\_χ″, U⟩ \= −⟨ν\_{χ,a}, U⟩,   and   |U(t)| \= |⟨τ\_t u, u⟩| ≤ ‖u‖²₂,  
hence   \*\*| q\_χ\[u\] − q\_ζ\[u\] |  ≤  ‖ν\_{χ,a}‖\_TV · ‖u‖²₂\*\*   — an \*\*L²-bounded\*\* symmetric form perturbation.  
**The perturbation as a bounded operator (the step written out).** Define the sesquilinear form  
Let E\_a : L²(−a,a) → L²(ℝ) be extension by zero, P\_a : L²(ℝ) → L²(−a,a) restriction, τ\_t translation, and set **T\_t := P\_a τ\_t E\_a**, a contraction on L²(−a,a) with ‖T\_t‖ ≤ 1 for every t (this is the point at which the interval must be handled: τ\_t alone does not map L²(−a,a) to itself). Define  
b\_{χ,a}\[u, v\] := − ∫\_{\[−2a, 2a\]} ⟨T\_t u, v⟩ · dν\_{χ,a}(t),   u, v ∈ L²(−a, a),  
Note ⟨T\_t u, v⟩ \= (u \* ṽ)(−t) up to conjugation, so this is exactly the pairing that appears in the form difference. Since |⟨T\_t u, v⟩| ≤ ‖T\_t‖·‖u‖₂‖v‖₂ ≤ ‖u‖₂‖v‖₂ for every t, we get |b\_{χ,a}\[u,v\]| ≤ ‖ν\_{χ,a}‖\_TV · ‖u‖₂‖v‖₂, so b is a **bounded** sesquilinear form; it is symmetric because ν is real and even and T\_t\* \= T\_{−t}. By the Riesz representation theorem there is a **unique bounded self-adjoint** B\_{χ,a} on L²(−a,a) with b\_{χ,a}\[u,v\] \= ⟨B\_{χ,a} u, v⟩ and ‖B\_{χ,a}‖ ≤ ‖ν\_{χ,a}‖\_TV. Taking u \= v recovers the quadratic estimate above.  
**Compact resolvent, written out.** For z real and sufficiently negative, ‖B\_{χ,a}(A\_a^ζ − z)⁻¹‖ \< 1, and  
(A\_a^χ − z)⁻¹ \= (A\_a^ζ − z)⁻¹ · \[ I \+ B\_{χ,a}(A\_a^ζ − z)⁻¹ \]⁻¹ .  
The first factor is compact (Suzuki, I5) and the second is bounded, so the product is compact. Hence A\_a^χ has compact resolvent, discrete spectrum and finite multiplicities, and D(A\_a^χ) \= D(A\_a^ζ).

**Consequences (KLMN \+ bounded perturbation), all unconditional:** (i) q\_χ is closed and lower semibounded on the **same form domain** as q\_ζ, with lower bound shifted by at most ‖ν\_{χ,a}‖\_TV; (ii) the associated self-adjoint operator is A\_a^χ \= A\_a^ζ \+ B\_{χ,a} with B symmetric and ‖B‖ ≤ ‖ν\_{χ,a}‖\_TV; (iii) a bounded perturbation preserves compact resolvent, so A\_a^χ has **discrete spectrum with finite multiplicities**; (iv) by Weyl’s inequality  
\*\*|λ\_n(A\_a^χ) − λ\_n(A\_a^ζ)| ≤ ‖ν\_{χ,a}‖\_TV\*\*   for every n.  
Table 8.1. The perturbation norm ‖ν\_{χ,a}‖\_TV (from the closed form of Lemma T11b; prime cutoff n ≤ ⌊e^{2a}⌋). It is dominated by the prime atoms and grows like O(e^a), as it must: the prime part of g at |t| ≤ 2a carries every prime power up to e^{2a}. \*\*These are VERIFIED floating-point values of a PROVEN finite bound\*\*, not ball-arithmetic certificates.

| a | χ₋₃ | χ₋₁₁ | χ₃₃ | ⌊e^{2a}⌋ |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 14.877 | 14.970 | 19.988 | 7 |
| 2 | 53.748 | 52.040 | 57.087 | 54 |
| 3 | 154.351 | 154.763 | 160.643 | 403 |
| 4 | 432.527 | 431.399 | 436.364 | 2980 |
| 6 | 3221.744 | 3221.248 | 3226.716 | 162754 |
| 8 | 23841.094 | 23844.519 | 23847.045 | 8886110 |

\*\*What this closes.\*\* The channelwise operator theorem was, in the previous version, an assumed hypothesis (O5). It is now a \*\*theorem\*\*, obtained without redoing any of Suzuki’s analysis: the only input is his ζ-theorem plus the observation that the archimedean singularity is \*the same\* in every channel and therefore cancels in the difference. \*\*This is the step that extends Suzuki’s finite-interval operator theory from ζ to the real primitive Dirichlet characters, and hence to the Dedekind zeta functions of multiquadratic abelian fields\*\* — those whose entire character group consists of real characters, which is exactly the case for K \= ℚ(√−3, √−11). \*\*Scope, stated precisely:\*\* a general finite abelian extension has complex characters occurring in conjugate pairs χ, χ̄; for those the kernel g\_χ need not be real and even, and a realified conjugate-pair block must be built before the same perturbation argument applies. That construction is straightforward in principle but is \*\*not carried out here\*\*, so T11 as proved covers the real primitive characters and the multiquadratic fields they generate.

## **§8.3 Theorem T12 — the Galois-graded operator \[DERIVED, now unconditional\]**

With T11 in hand the graded operator is unconditional. Assemble the Frobenius-resolved components into ℳ((x,h),(y,h′)) := g\_{h h′^{−1}}(x−y) on L²(−a,a) ⊗ ℂ\[G\], and set 𝔄\_a := D\*𝔊\_a D (mean-zero compression, D \= i d/dx Dirichlet).  
**Theorem T12 \[DERIVED\].** The finite Fourier transform on G block-diagonalises 𝔄\_a into ⊕\_{χ ∈ Ĝ} A\_a^χ. By T11 each block is self-adjoint, lower semibounded and discrete; therefore **𝔄\_a is self-adjoint, lower semibounded, and has discrete spectrum**. It commutes with the regular representation of G — a symmetry the ζ operator does not possess — and its spectrum is **graded by Ĝ**, the grading being the Frobenius grading of the arithmetic.  
Suzuki’s A\_a is the trivial-character block. 𝔄\_a is the \*\*canonical finite direct-sum operator containing all four character blocks\*\* — the smallest such assembly in the obvious sense that it has exactly one block per element of Ĝ — and it is obtained at the cost of one perturbation lemma. No universal property is claimed.

## **§8.4 What the grading detects — and what we actually observed**

**Under** GRH(ζ\_K) and a channelwise spectral limit (T11 now supplies the operator theorem itself), the limiting multiplicity of γ in Spec(𝔄\_∞) would be **Σ\_{χ∈Ĝ} m\_χ(γ)**, the total analytic multiplicity across the four L-functions. A multiplicity ≥ 2 therefore signals **either** a zero shared by two channels **or** a repeated zero within one channel; separating the two requires the additional hypothesis that each channel’s zeros are simple.  
**What we observed is a statement about zeros, not about an operator.** Comparing the sign-change zeros detected below T \= 40:  
Table 8.2. Detected sign-change zeros below T \= 40, and the closest approach between distinct channels. This is a \*\*numerical observation about a detected list\*\*, not a certification: no Turing-type zero count was run, so undetected or even-multiplicity zeros are not excluded.

| channel | detected zeros, T \< 40 | lowest certified γ |
| ----- | ----- | ----- |
| ζ | 6 | 14.134725 |
| χ₋₃ | 13 | 8.039737 |
| χ₋₁₁ | 21 | 2.477244 |
| χ₃₃ | 28 | 2.996951 |
| closest approach across distinct channels | ζ at 25.010858 vs χ₃₃ at 25.011945 | Δ \= 1.087×10⁻³ |

\*\*No coincidence occurs among the detected zeros below T \= 40\*\*, and the closest approach is 1.1×10⁻³ — a near-degeneracy in the very first range one looks at. We do \*\*not\*\* claim this certifies simplicity or the Grand Simplicity Hypothesis for this family; it is an observation, and it is recorded because a \*\*limiting\*\* graded operator — if the channelwise spectral limit exists — would see it as a splitting between two Ĝ-blocks (the finite-a graded operator itself exists unconditionally by T12).

## **§8.5 Conditional outlook — POME, and what the pre-gate does and does not show**

The kink measure (T4) makes the corpus’s dynamical target explicit: a flow whose primitive orbits carry a Galois holonomy and reproduce μ\_Λ^χ for every χ (POME-K). A necessary condition is the orbit count N\_IT(L) \~ π(e^L) \~ e^L/L. By Parry–Pollicott that count is **automatic** for any weak-mixing Axiom-A flow of entropy 1, so **the counting condition does not by itself decide POME** — an earlier internal claim to the contrary is retracted.  
**What the pre-gate does establish \[DERIVED\].** The corpus’s map is f(z) \= i^z \= exp((iπ/2)z), whose fixed points are exactly z\_k \= −(2/iπ)·W\_k(−iπ/2) over the branches k ∈ ℤ of the Lambert function. Since |W\_k(w)| \~ 2π|k|, we get |z\_k| \~ 4|k| and hence  
N\_fix(R) := \#{ fixed points with |z| ≤ R } \~ R/2   (asymptotically; the argument principle gives 3, 5, 10, 20 at R \= 5, 10, 20, 40).  
**So f has infinitely many fixed points, and hence infinitely many periodic points in total.** (Whether it has infinitely many points of **every exact period** is \*not\* established here: the Lambert-W computation solves f(z) \= z only, and the period-n count would require analysing f^n(z) \= z. The external-address heuristic suggests it, but we do not claim it.) Consequently, **if the roof function is bounded on the invariant set**, infinitely many orbits have length below some finite L, contradicting N\_IT(L) \< ∞. POME therefore requires **either** a roof unbounded on the invariant set **or** a pruning selecting finitely many orbits per period — and, to avoid circularity, the pruning must be prime-blind.  
\*\*Status, stated exactly.\*\* ‘The unpruned map has infinitely many periodic points’: \*\*DERIVED\*\* (Lambert-W branches). ‘Its topological entropy on the Julia set is infinite’ and ‘no prime-orbit asymptotic can hold’: \*\*OPEN\*\* — the radius R is not an orbit length, and entropy is not determined by a fixed-point count. An earlier version asserted these as PROVEN; that is \*\*retracted\*\*. What remains is a sharp open question: \*is there a canonical, prime-blind pruning of the i-tetration dynamics, with an unbounded roof, whose primitive orbit lengths are exactly {log p}?\*

## **§8.6 A remark on operator routes**

A Hilbert-space Gram realisation of the screw kernel, K\_g(t,u) \= ⟨b(t), b(u)⟩, exists \*\*if and only if\*\* K\_g ⪾ 0 — which, globally, is RH. So \*asserting the existence of such a realisation\* is asserting the positivity, not explaining it. This does \*\*not\*\* say that operator-theoretic routes are futile: Suzuki’s A\_a exists as a self-adjoint, lower-semibounded operator \*\*without\*\* assuming RH (its spectrum may a priori contain negative values), and proving its positivity by independently established operator structure would be a genuine proof. An earlier version claimed that no operator built from g can be a route and that only a dynamical construction remains; \*\*both claims are withdrawn\*\* as overreach.

# **§9. Conclusion**

Three things are established. The screw kernel of an abelian field decomposes over the character group and detects Frobenius (§2). Its second distributional derivative is a decorated prime-orbit measure, which turns the dynamical programme into an explicit and falsifiable target (§3). And the Weil functional of K can be **certified** — positive on the canonical grid without GRH, and positive definite on an 11-dimensional space of test functions — by ball arithmetic with closed-form tails (§4–§5).  
The fourth is the one to take away, and it is a statement about computation rather than about zeta functions. Because the zero side is a sum of squares, a **single** zero gives a rigorous lower bound; the budget of a finite Weil audit is therefore set by the **nearest certified usable zero among the channels**. K supplies a certified low-lying zero at 2.477 where the smallest certified sign-change zero of ζ found in the declared scan is 14.135 (firstness is not claimed anywhere; see §6.1), and that single fact moves the certified prime budget of the worst grid point from 10³² to 10⁶. **A character decomposition containing a low-zero channel is a numerical preconditioner.** Whether enlarging a character family reliably supplies such a channel — the family statement — is open, and the naive conductor heuristic is false. What is established is the mechanism and the case.  
One further thing is established. §8.1 resolves the screw kernel by **Frobenius class** rather than by character: g\_h sees exactly the primes with Frobenius h, so g\_e sees exactly the totally split primes. This is a Chebotarev decomposition of the kernel with no counterpart for ζ, and it is unconditional.  
**§8.1–§8.3 are established results, not an outlook.** §8.1 resolves the kernel by Frobenius class (T10, PROVEN). §8.2 **transfers Suzuki’s finite-interval operator theorem from ζ to every real primitive Dirichlet channel** (T11, PROVEN): the archimedean singularity 1/(2|x|) is the same in every channel and cancels in the difference, so h\_χ″ is a finite signed measure with δ₀-mass exactly −log q\_χ, the localised forms differ by an L²-bounded symmetric form, and KLMN plus the resolvent identity give a self-adjoint A\_a^χ with the same form domain, compact resolvent, discrete spectrum, and |λ\_n(A\_a^χ) − λ\_n(A\_a^ζ)| ≤ ‖ν\_{χ,a}‖\_TV. §8.3 assembles the channels into a **Galois-graded self-adjoint operator** 𝔄\_a (T12, DERIVED, unconditional given T11), G-equivariant and Ĝ-graded. **The channelwise operator hypothesis that earlier versions carried as OPEN is closed.**  
**§8.4–§8.6 remain observational or conditional, and are labelled so.** The closest approach between the detected zeros of distinct channels below T \= 40 is 1.1×10⁻³ — an observation about a detected list, not a certification, since no Turing-type count was run. The dynamical route (POME-K) is constrained but not decided: the unpruned map provably has infinitely many periodic points (Lambert-W branches), while the entropy and orbit-count conclusions remain open. And the Gram remark of §8.6 stands as a caution, not a no-go.  
What is not established is stated as such. The operator frontier is open, its two tracks are separated, and the single missing statement of the Herglotz route — the Weyl–truncation bridge — is written down. The next paper in this line will be written when one of those changes status, and not before.

# **Acknowledgements & Code Availability**

## **Reproducibility record**

| item | value |
| ----- | ----- |
| script | zs\_m48\_verify\_v2\_7.py |
| SHA-256 | 366e9c0e247daa65ff87b1e4200e9d1b1f3ec37e54275081848065c172a9d3c8 |
| expected checks | \*\*380\*\* (hard-coded; 360 with \--fast, which is a smoke test, not the certificate). v2.6 advertised 378 but had added two P3 checks (a \= 3, 6\) without updating the guard; corrected here. A full run must confirm 380 — and if it does not, the hard-coded guard \*\*fails loudly\*\*, which is its purpose. |
| Python | 3.12.3 |
| numpy / scipy | 2.4.4 / 1.17.1 |
| mpmath / python-flint (arb) | 1.3.0 / 0.9.0 |
| still required before public release | the stdout and JSON ledger of a full 380/380 run, and its wall-clock time |

The companion script zs\_m48\_verify\_v2\_7.py is a single self-contained fail-closed suite. Every theorem-tier certificate (the enclosures of §4, the real-zero certification of §4.3, the zero brackets, the Cholesky certificate of §5, the budget inversions of §6) is formed and decided inside arb ball arithmetic; floats appear only in the JSON report. The Herglotz and pilot-assembly blocks are labelled **diagnostics** and are not certificates. The script prints its OPEN registry, refuses to report a check count different from the advertised one, and exits non-zero on the first failure. This work used AI tools for verification, adversarial audit and drafting; the author is responsible for all content.

# **Appendix A. Specialisation of the zero-free formula**

\[2, Thm 4.1\] with r \= 1, λ \= ½, μ \= a\_χ/2, Q \= (q\_χ/π)^{1/2}, m\_F \= 0 (1 for ζ), c\_F(n) \= χ(n)Λ(n) gives λ/2 \+ μ \= c\_χ, λ² \= ¼, e^{−t(½+μ/λ)} \= e^{−2c\_χt}, e^{−t/λ} \= e^{−2t}, and log Q \+ λψ(c\_χ) \= −β\_χ — which is Theorem T2.

# **Appendix B. Closed forms**

F(x) \= C e^{−ax²/2}(cos tx \+ κ), C \= ½√(π/2a), κ \= e^{−t²/2a}; v̂(z) \= ½√(π/a)\[e^{−(z−t)²/4a} \+ e^{−(z+t)²/4a}\]. Prime part, exact: ∫(|x|−L)₊F″dx \= 2F(L). Linear part: ∫β|x|F″dx \= 2βF(0). Gamma-factor part: −½Σ\_k J(2μ\_k)/μ\_k² with J(β) \= −βF(0) \+ β²G(β), G(β) \= C\[ℜH(β−it) \+ κH(β)\], H(w) \= √(π/2a)·erfcx(w/√(2a)) (Faddeeva; no cancellation). Pole part (ζ only): 2∫ e^{x/2}F dx, a Gaussian integral.

# **Appendix C. The subspace Gram matrix**

Multiplying two Gaussian-cosine transforms and using e^{−(z−p)²/4a}e^{−(z−q)²/4a} \= e^{−(p−q)²/8a}e^{−(z−(p+q)/2)²/2a}, then inverting, gives the closed form of §5. Hence every Gram entry is a combination of two evaluations of Φ(a, ω) \= −∫g\_χ(x)\[e^{−ax²/2}cos(ωx)\]″dx, and the enclosure machinery of §4 applies verbatim.

# **Appendix D. Verification ledger and Supplement**

The full ledger, the 48-entry table, the per-channel verdicts, the zero brackets, the anti-numerology Monte Carlo (0/200 successes per null model in each of three channels; 95% upper bound 3/200 \= 1.5% by the rule of three), the pilot assembly outputs, and the complete **Correction History** of drafts v1.0–v1.9 — including every retraction — are in the Supplement. Nothing in the body depends on the Supplement; the Supplement exists so that the corrections are on the record.

# **References**

\[1\] M. Suzuki, Aspects of the screw function corresponding to the Riemann zeta-function, J. London Math. Soc. 108 (2023) 1448–1487; arXiv:2206.03682.  
\[2\] M. Suzuki, Screw functions of Dirichlet series in the extended Selberg class, Int. J. Number Theory 21 (2025) 1815–1823; arXiv:2209.12832.  
\[3\] M. Suzuki, Weil’s quadratic form via the screw function, arXiv:2606.09096 (2026).  
\[4\] M. G. Kreĭn and H. Langer, Continuation of Hermitian positive definite functions and related questions, Integral Equations Operator Theory 78 (2014) 1–69.  
\[5\] I. J. Schoenberg, Metric spaces and completely monotone functions, Ann. of Math. 39 (1938) 811–841.  
\[6\] A. Weil, Sur les ‘formules explicites’ de la théorie des nombres premiers, Comm. Sém. Math. Univ. Lund (1952) 252–265.  
\[7\] E. Bombieri, Remarks on Weil’s quadratic functional in the theory of prime numbers I, Rend. Lincei Mat. Appl. 11 (2000) 183–233.  
\[8\] A. Connes and C. Consani, Weil positivity and trace formula: the archimedean place, Selecta Math. 27 (2021) 77\.  
\[9\] J. B. Rosser and L. Schoenfeld, Approximate formulas for some functions of prime numbers, Illinois J. Math. 6 (1962) 64–94.  
\[10\] F. Johansson, Arb: efficient arbitrary-precision midpoint-radius interval arithmetic, IEEE Trans. Computers 66 (2017) 1281–1292.  
\[11\] N. I. Akhiezer, The Classical Moment Problem, Oliver & Boyd (1965) §3 (Grommer–Hamburger convergence criterion).  
\[12\] H. Iwaniec and E. Kowalski, Analytic Number Theory, AMS Colloq. Publ. 53 (2004).  
\[13\] W. Parry and M. Pollicott, An analogue of the prime number theorem for closed orbits of Axiom A flows, Ann. of Math. 118 (1983) 573–591.  
\[14\] D. Ruelle, Dynamical Zeta Functions for Piecewise Monotone Maps of the Interval, CRM Monograph Series 4, AMS (1994).

# **Version History**

v2.7 (July 2026): **release candidate.** Corrigendum to v2.6, with no content removed. Fixes: the fail-closed guard is corrected from 378 to **380** (v2.6 added two P3 checks at a \= 3, 6 without updating it — a full run would have failed); T11’s scope is stated precisely (real primitive Dirichlet characters, hence **multiquadratic** abelian Dedekind zetas; complex conjugate-pair channels require a separate realified block, not carried out here); the translation used in the sesquilinear form is defined as the contraction T\_t \= P\_a τ\_t E\_a (zero extension then restriction), since τ\_t alone does not preserve L²(−a,a); the claim of infinitely many periodic points **of every exact period** is retracted (only the total set is shown infinite); ‘Four results’ → ‘Five’; the duplicate Table 8.1 is renumbered 8.2; §7’s opening sentence no longer says everything in it is OPEN; §8.4 refers to the **limiting** graded operator; ‘no new operator analysis is required’ → ‘no new compactness proof is required for each channel’; and the remaining ‘lowest zero’ wording is replaced by ‘certified low-lying zero / smallest certified sign-change zero found in the declared scan’. **Status: release candidate, not yet a public release** — the stdout, JSON ledger and wall-clock of a full 380/380 run are still required.  
v2.6 (July 2026): corrigendum to v2.5, with no content removed. Fixes: the Conclusion now states §8.1–§8.3 as established (it had still called them a conditional outlook, contradicting T11); the OPEN registry no longer lists the channelwise operator hypothesis (T11 closes it); T11 gains the explicit sesquilinear-form, Riesz-representation and resolvent-identity paragraphs; the perturbation norms are relabelled VERIFIED rather than arb-certified (the theorem is PROVEN, only its numerical bound is floating-point); the prime cutoff in Table 8.1 is corrected to n ≤ ⌊e^{2a}⌋, changing the a \= 1 entries from 15.86/15.95 to **14.877/14.970**; a \= 3 and a \= 6 are added to the verification loop so every table row has provenance; the T8 cutoff in the contributions table is corrected to P \= 4×10⁶; β\_χ is defined by the gamma-factor expression (with the L′/L identification used only where L(½,χ) ≠ 0 is certified); ‘smallest self-adjoint operator’ is replaced by ‘canonical finite direct-sum operator’; and the remaining first/lowest-zero wording is unified on γ\_cert.  
v2.5 (July 2026): draft. **Proves the Channel Perturbation Theorem (T11)**: the archimedean singularity 1/(2|x|) is the same in every channel and cancels in h\_χ \= g\_χ − g\_ζ, so h\_χ″ is a finite signed measure on \[−2a,2a\] with δ₀-mass exactly −log q\_χ; the localised forms therefore differ by an L²-bounded symmetric form, and Suzuki’s ζ operator theorem transfers to every real primitive Dirichlet channel by KLMN, with |λ\_n(A\_a^χ) − λ\_n(A\_a^ζ)| ≤ ‖ν\_{χ,a}‖\_TV. This closes the former hypothesis O5 and makes the Galois-graded operator (T12) unconditional. Also: **retracts** ‘the T9 remainder is independent of a’ (only the 1/d² coefficient is; the next is −(1+aL²)/2d³, now given); unifies the certificate cutoff at an explicit P \= 4×10⁶ plus analytic tail; removes the environment override of the check-count guard; and separates theorem-tier from diagnostic blocks in the ledger.  
v2.4 (July 2026): draft. **Closes Theorem T9**: the 1/d² remainder is now derived (from the complementary-error-function factor of the tail) rather than measured, is independent of a, and reduces the error to 2×10⁻⁴ nats where log N\* ≈ 73–97. **Narrows T10** to unramified prime powers and renames it a Frobenius-\*resolved kernel component\* (a signed combination of cpd functions need not be cpd, and no screw property is claimed). **Demotes the Galois-graded operator, the shared-zero statement and the POME pre-gate to a labelled conditional outlook** (§8.2–8.4), with three explicit retractions: the channelwise operator theorem is **not** inherited from Suzuki; the multiplicity formula is Σ\_χ m\_χ(γ) and does not by itself separate shared from repeated zeros; and neither infinite entropy nor the impossibility of a prime-orbit asymptotic was proved. **Withdraws** the claim that no operator built from g can be a route to RH, and the claim that only a dynamical construction remains.  
v2.3 (July 2026): draft. Corrects Theorem T9 (the target prefactor carries (1+e^{−γt/a})² — a factor 4 at t \= 0 — and the subleading term is (1/d)log(A/B), not (a/d)log(·); the corrected law is accurate to 0.005 nats where log N\* \= 73, with residual ≈ 4.5a/d², and its regime d²/a → ∞ is stated). Replaces all ‘first zero’ language by ‘certified zero’. Adds §8 (the Galois-twisted screw operator: T10 Frobenius-class kernel, T11 the operator, T12 simplicity detection, T13 the no-go for g-built operators) and §7.3.1 (the POME pre-gate, executed: the unpruned i-tetration dynamics has infinitely many fixed points, N(R) \= R/2, hence infinite entropy and no prime-orbit asymptotic — and a retraction of the earlier claim that the counting condition alone decides POME).  
v2.2 (July 2026): draft. Adds the certification threshold law (Theorem T9); replaces the ‘first zero’ language by ‘a certified low-lying zero’ (a sign change certifies an odd-multiplicity zero in the bracket, not the absence of lower ones — and T7/T8 do not need firstness); makes the budget inversion fail-closed with two-sided postconditions; decides the gain entirely in arb; states the prime cutoff of the certificate exactly (explicit summation to 4×10⁶ plus the closed-form tail). Compact rewrite. Versions v1.0–v1.9 were internal audit drafts and are superseded; their corrections — including the retraction of a false positivity certificate for A\_a, of an over-read zero-side lower bound, and of an incorrect Nevanlinna convergence criterion — are preserved in the Correction History Supplement rather than in the body. The new result of this release is §6, the Decoration Principle.