# Arithmetic instability of lacunary deviations and writing-time bounds for finite phase references

**Paper code:** ZS-M72 · **Version:** 1.8 · **Date:** 2026-09-18 UTC · **Programme role:** SUPPORT/METHOD · **Output:** integrated research paper.

**Current internal assessment:** **RESEARCH GRADE 4; PAPER QUALIFICATION PASS**, for the mathematical contribution specified in §§9.10–9.13 and assessed in §13.1. This is a project-internal finding under Mission v1.7, not peer review, an absolute-priority claim, or physical CORE completion. The prior v1.7 grade-3 assessment remains a historical assessment of its own contribution.

**Scope.** The new central result concerns one uniform phase and the deterministic frequency family $aq^k+r$, with integer $q\ge2$ and nonzero integers $a,r$. It evaluates the whole limiting log-MGF and rate function in terms of the known geometric pressure, with an explicit finite-length error. The finite quantum waiting, writing and storage model, and all surviving earlier results, remain integrated below. The actual spin-band alignment limit and the action-derived measurement instrument remain OPEN.

**Substantive change.** T31 proves $\Lambda_{q;a,r}(\theta)=\Lambda_q(|\theta|)$ and $\mathcal J_q(s)=\mathcal I_q(|s|)$. Cor32 permits subexponentially growing common integer shifts and unrestricted nonzero integer multipliers. Cor33 determines the $C^q$ but non-$C^{q+1}$ singularity for even $q$. P34 exhibits a negative-tail event that is impossible for the geometric sequence but has an explicit positive exponential lower bound after a shift by one. These change the class of solvable frequency models; they are not consequences of increasing the local potential-perturbation radius.

**Audit integration.** F17-01–04 are corrected in the current text and verification disclosures; F17-05 is resolved by using an actually read, versioned source location rather than carrying an unconfirmed lemma number. Appendix R5 maps every finding and the meta-audit's process diagnosis to changes. The unchanged input files and original verification histories remain identifiable in the companion bundle.

**Verification.** The v1.8 companion checks nine new rows: C3, V4, W1, G1; **P=0**. Its six deliberate wrong predictions were each run against **all nine rows in fresh `python -O` processes**, with only the designated row failing and all other row evidence unchanged. Separately, inherited C26/V27/V35 and registry G42 were rerun successfully. The inherited v1.7 FULL 69-row run, its **45 targeted** self-tests, and the supplied auditor's **eight all-row** noninterference tests are three different profiles; none is described as a newly executed v1.8 full legacy suite. Counts do not prove the universal theorems or determine the research grade.

**Authorship and review boundary.** OpenAI prepared this integration and the new proofs. The new finite checks use different computational routes, but this session is not an independent external or cross-family audit of T31–P34. **Qualified-human anchor: NONE.** This is a disclosure, not a grade gate.

---

## Abstract

For one uniform random phase $U$, consider the lacunary cosine sum with frequencies $aq^k+r$, where $q\ge2$ is an integer and $a,r$ are nonzero integers. We prove that its limiting log moment generating function is exactly $\Lambda_q(|\theta|)$, where $\Lambda_q$ is the pressure of the unshifted geometric cosine system. Its full large-deviation rate is consequently $\mathcal I_q(|s|)$ on $[-1,1]$, with endpoint costs $\log q$. A finite Fourier majorant and a cylinder estimate give an explicit error uniform in $a$, and extend the law to common integer shifts with $\log(1+|r_n|)=o(n)$. For even $q$, this changes the negative effective endpoint from $-\cos(\pi/(q+1))$ to $-1$ and produces a limiting pressure that is $C^q$ but not $C^{q+1}$ at zero. In particular, the shifted doubling sequence has rate $s^2-|s|^3+O(s^4)$ near zero. A finite interval witness shows that adding one opens a tail event that was impossible before the shift. The theorem supplies an exact global rate reduction for this deterministic family, including the recently studied sequence $2^k+1$; it does not give an elementary closed expression for the geometric pressure itself.

These results are integrated with the earlier finite phase-reference theory. Two-boundary spectral capacity bounds, strict-crossing first-loss envelopes, the all-even geometric sub-action, actual-frequency Riesz bounds, Weyl transfer, finite first-loss certificates, and the diffusive Ornstein–Uhlenbeck window remain in the paper. The waiting contrast is transferred through a specified writing process into spatial records with a stated storage law. The inherited local additive stability result applies around the **complete-square potential** $F_0(x)=\cos(2\pi x)+\varepsilon^+(q)\cos(4\pi x)$, not around bare cosine. The new arithmetic result explains why vanishing relative frequency errors do not suffice to transfer long-time alignment. The actual spin-band alignment limit, preparation and apparatus selection from the action, and the corresponding physical CORE bridge remain unresolved.

---

## 1. Introduction

### 1.1 The problem

A finite quantum reference frame that carries a phase contrast is a resource. Three distinct questions are usually collapsed into one word, "lifetime": how long the unused contrast survives the internal dynamics of the reference (the waiting time), how the contrast can be transferred into records that live at two places (the writing interval), and how long such records survive noise afterwards (the storage time). The three questions have different objects, different time variables and different resources, and each of them is answered here in a declared finite model.

The mathematical core is the first question. For a band of charge-sector ground states of a finite spin source the contrast is a positive cosine sum $S_B(t)=\sum_k\omega_k\cos(\Delta_kt)$ whose frequencies are differences of Dirichlet eigenvalues of truncated Ehrenfest chains and are exponentially small in the source size $B$, with a spread of rates across the band. The time at which the contrast first drops by a fixed loss $\ell$ is governed by a competition between the exponentially separated frequencies and the collective alignment of their phases. The earlier seed of this work controlled one boundary of each truncated chain, used a cubic approximation to the sine profile, and left the first-loss exponent between two fronts without knowing whether either front is attained or whether the exponent exists at all. This paper closes the two-boundary problem, sharpens the fronts, and then resolves the status of the exact exponent: it is not determined by the limiting distribution of rates, it is determined by the arithmetic of the frequencies, and for several natural arithmetic classes it is computed exactly.

The v1.8 question asks what survives when the frequencies themselves change from $q^k$ to $q^k+r$. The relative change tends to zero, yet it need not be a small phase change over the observation window. Sections 9.10–9.13 now compute the full large-deviation law for $aq^k+r$: the rate is the reflection of the positive geometric branch, for every nonzero integer shift. This mathematical result can be read independently of the quantum model. Its programme use is to establish a precise boundary on transferring arithmetic alignment, not to supply the missing physical selector.

### 1.2 What the reader will find

For the central mathematical result, begin with the normalization in §9.8 and read T31, Cor32–33 and P34 in §§9.10–9.13. T31 has a self-contained finite comparison proof, with the standard geometric pressure as its only thermodynamic input. T13/T16 in §§9.6 and 9.8 give the inherited all-even geometric endpoint against which the shifted law is compared. Section 12.7 checks the nearest external results, §13.1 gives the current scoped assessment, and Appendix R5 answers the audit and meta-audit.

The complete physical and mathematical lineage remains present. Sections 2–8 contain T1–T6 on the finite source, waiting, writing and storage constructions. Sections 9.1–9.9 contain the strict-crossing first-loss formulation, sharpness and alignment results T7–T9 and T13–T16, and the actual-frequency phase-defect bound T20. Section 10 preserves the diffusive and endpoint extensions, P17 and T18–T19 on Weyl spectra, T22 on the fixed diffusive window, and C23–Cor30 on rate endpoints, excursions and local additive perturbations. Section 11 fixes the physical bridge status. Appendices S and N retain the integrated seed and spatial-record theory, Appendix L the literature lineage, Appendices R/R3/R4 the earlier correction histories, Appendix V the separated verification profiles, and Appendix H the preservation map. The new execution ledger does not replace the inherited results with a larger, misleading PASS count.

### 1.3 Contribution sentence

Under one uniform phase and integer frequencies $aq^k+r$, with $q\ge2$ and $ar\ne0$, we prove that the entire limiting pressure is $\Lambda_q(|\theta|)$ and the rate is $\mathcal I_q(|s|)$, with an explicit finite-length bound. This computes a class beyond the fixed-observable geometric model, changes the negative effective endpoint for even $q$, and explains the nonanalytic limiting pressure of the known shifted doubling example. The waiting, writing and storage results below retain their supplied physical assumptions; the new theorem determines a mathematical transfer boundary within that programme.

The claims do not include an elementary formula for the geometric pressure itself, a solution of the actual spin-band exponent, a general recurrence LDP, or the origin of a measurement instrument from the action.

### 1.4 Contribution table

| Result | New here? | Status | Assumptions | Proof / evidence | External baseline |
|---|---|---|---|---|---|
| T31 complete shifted-family LDP | **NEW in v1.8; central** | PROVEN | integer $q\ge2$, nonzero integers $a,r$, one uniform phase | finite Fourier majorant and cylinder estimate (9.40)–(9.46); C71, V72–V74 | geometric LDP and fixed-phase pressure are imported; same-example comparison in §12.7 |
| Cor32 triangular arrays | NEW consequence | PROVEN | common nonzero integer $a_n,r_n$ in each row; $\log(1+|r_n|)=o(n)$ | uniform estimate (9.40); no growth condition on $a_n$ | no arbitrary termwise perturbation claimed |
| Cor33 exact differentiability threshold | NEW consequence on an IMPORTED coefficient | PROVEN | even $q$, T31 assumptions | analytic one-sided expansions; C75–C76 and V78 are finite anchors | geometric first-resonance coefficient and shifted cumulants are credited |
| P34 impossible/possible negative-tail event | DERIVED quantitative witness | PROVEN | doubled frequencies, common shift one, $n\ge4$ | T13 and an explicit phase interval; W77 | arithmetic sensitivity itself is known |
| T1(a) finite two-boundary capacity sandwich | DERIVED on an IMPORTED engine | PROVEN | any integer $B\ge1$, proper window, interior point | Poincaré inequality with full gap 2; two Cauchy–Schwarz resistance bounds; row C01 | Bovier's capacity method; Barta/Collatz–Wielandt |
| T1(b) compact two-boundary sum, relative $O(B^{-1})$ | DERIVED | PROVEN | fixed $\epsilon,x_0$; endpoint split for $a+b=1/2$ | exact resistance ratios, geometric tails; row V02 | one-dimensional metastability asymptotics |
| Uniform gaps and weights on the band | DERIVED | PROVEN (large $B$) | (3.11) | exact adjacent ratio (3.14); Poincaré for weights | — |
| T2(a) finite envelopes | EXTENDED | PROVEN | positive weights, real frequencies | elementary; time average of $M$; rows C05, V06 | — |
| T2(b),(c) exponent interval | **EXTENDED, central** | PROVEN | weak convergence of the rate measure; continuity and strict crossing at the two original fronts | fast/slow split, no Diophantine input | hydrodynamic large-deviation coherence (different object) |
| T3 fixed-window law $\Theta(B^2/J)$ | INHERITED leading term + DERIVED remainder | PROVEN | fixed $j,w$ | explicit Schur-complement remainder; rows C03, V04 | collapse/revival of quadratic spectra |
| T4 fixed-Hamiltonian writing, quartic timing | CONSTRUCTED/SPECIALIZED | PROVEN | declared corridor and link unitaries | gauge conjugation, spectral polynomial; rows C07, V08, V11 | perfect state transfer |
| T5 interface $r=xS_B(t_w)$ | CONSTRUCTED | PROVEN | invariant C6 effects, neutral prepare | direct partial trace; row V09 | measure-and-prepare channels |
| T6 storage law and error window | IMPORTED channel algebra + DERIVED | PROVEN | history-independent parity noise, common erasure | exact generator eigenvalue; rows C10, V12 | — |
| T7 sharpness of the exponent interval | **NEW** | PROVEN (lower-end quantifier repaired in v1.1) | same hypotheses as T2(c) | odd-multiple alignment with a diagonalised family; Fejér-level positivity; rows W15, W16 | Fejér kernel positivity (classical) |
| Alignment capacity and the front $\ell/(1+\kappa)$ | **NEW formulation** | PROVEN (statement completed in v1.1, corrected for atoms in v1.2) | as T2(c), with $H_-$ and the atomic term; strict crossing of the applicable threshold; (9.1e) for the constant-$\kappa$ corollary | two-sided threshold argument (9.1a); counterexample (9.1c) for the sharpness of the hypothesis; row C38 | — |
| T9 integer-ratio spectra: $\kappa_q$ | NEW mapping to ergodic optimisation | PROVEN for odd $q$ and every even $q$ (the even case via T13 in v1.1) | exact geometric frequencies | explicit orbits and exact sub-actions; rows W17, C24 | ergodic optimisation of expanding maps (Bousch) |
| T8 Riesz–Fejér bound $\kappa\ge\cos(\pi/(m+2))$ | NEW combination | PROVEN (proof rewritten in v1.1, same constant) | Hadamard ratio $\ge2m+1$ | Riesz product with the Fejér extremal kernel and the $\ell^1$ Fourier mass; rows C18, C31, C32, V19, V20 | Riesz products, Fejér's coefficient theorem |
| Finite-size positions of the spin band | NEW numerics | VERIFIED (listed sizes, high-precision brackets, not interval certificates) | exact finite model | Lipschitz grid on computed spectra; row V14 | — |
| T10 diffusive-scale two-boundary formula | NEW | PROVEN (three proof steps repaired across v1.1–v1.2; consequences restricted) | $h\ge3\sqrt B$ per boundary, $h_{\min}\ge\sqrt{2B\log B}$ for the eigenvalue | resistance expansion with the exact $s(s-1)$ sum and the tail (10.2b) estimated after normalisation; rows V21, C32, C39 | — |
| T11 endpoint band $a=b$ | NEW | PROVEN | $0<b=a\le1/4$ | mass argument on T2(c); row V22 | — |
| P12 parent independence; Weyl parent rate | NEW observation | PROVEN (finite inequality) / VERIFIED (rate at $B=256$) / **REFUTED** (the v1.0 exact ground energy) | reversible birth–death parent; four normalisation conditions for any transfer of the exponent | same proof; rows V23, C29 | Krawtchouk/Weyl edge literature |
| T13 $\beta_q=\cos\frac\pi{q+1}$ for every even $q$, unique maximiser | **NEW in v1.1** | PROVEN | even integer $q\ge2$, all $x$ | explicit tent sub-action (9.15); rows C26, V27, V28 | Bousch's Sturmian theorem covers $q=2$ |
| T14 sparse Riesz bound for real ratios | **NEW in v1.1** | PROVEN | $\nu_{i+1}/\nu_i\ge\rho>1$ with an integer $L$ such that $\rho^L>3$ **and** $\delta=1-\rho^{-1}-(\rho^L-1)^{-1}>0$ | sparsified Riesz product with three non-resonance margins; row V33 | Riesz products; Sidon's theorem |
| T15 standard band: $\kappa^-\ge\tfrac14$ and $\limsup\le q_{4\ell/5}$ | **NEW in v1.1, central** | PROVEN (large $B$) | standard band, interior rate | T14 at $\rho=19/10$, $L=2$ on the actual spacing; row V34 | — |
| T16 effective domain of the lacunary rate function | **DERIVED COROLLARY, new in v1.1** | PROVEN | integer $q\ge2$, Lebesgue phase | T13 plus the pressure variational principle; rows C26, V35 | Aistleitner et al. state the even-$q$ case as unresolved |
| P17 lower bound on the Weyl ground-energy correction | **NEW in v1.2** | PROVEN | every $B\ge1$ | exact trial-vector identity and the Rayleigh principle; rows C40, V41 | — |
| T18 exact Weyl Green enclosure and asymptotic | NEW calculation beyond the audit enclosure | PROVEN | exact specified matrix, every $B\ge1$ | endpoint Poisson flux, rational resolvent bracket, beta-integral remainder; C43, C48 | standard rank-one perturbation and factorial asymptotics |
| T19 compact-band Weyl transfer | NEW completion of the specified-parent obligation | PROVEN | compact interior windows, fixed energy normalization | auxiliary matrix agrees exactly on each window; capacity and gap differences; C44 | reversible capacity, not WKB alone |
| T20 weighted local phase-defect bound | EXTENDED | PROVEN | even comparison ratio, positive frequencies and weights | explicit weighted telescoping and backward recurrence; W47 | T13 tent inequality |
| P21 exact finite first-loss certificates | METHOD application | CERTIFIED at listed sizes | standard band, $B=24,48,96$, $\ell=1/10$ | directed integer arithmetic and all-time exclusion; C45 | standard interval arithmetic and Sturm recurrence |
| T22 diffusive window: Ornstein–Uhlenbeck limit and $\Theta(B^{3/2})$ first loss | **NEW in v1.4** (Lemma 22.1 by the v1.4 audit) | PROVEN | even $B\to\infty$, fixed $K,\kappa$; strict first contact for (10.29) | Dirichlet-form convergence, holomorphic continuation in the window centre and Vitali; row V50 | Kramers/Ornstein–Uhlenbeck spectral asymptotics |
| T24, P24.1 endpoint entropy order and sharp coefficient $1/A_q$ | DERIVED, written by the v1.4 audit; completed for all even $q$ in v1.5 | PROVEN | even $q\ge2$ | explicit residual, Markov defect, exclusion of competing excursions; rows C53, V54, C56 | Leplaideur–Mengue Theorem A (existence, imported); their Theorem B (an explicit binary-shift family) |
| T25 stability of orbit, excursion and cost $A_q+\varepsilon B_q$ under $\varepsilon\cos4\pi x$ | **NEW in v1.5**; large-$q$ proof replaced by the v1.5 audit in v1.6 | PROVEN on $[-\tfrac1{20},\varepsilon^+(q)]$ | even $q\ge4$; $q=2$ by cohomology | tent sub-action, exact competitor geometry, two concave margins closed at both endpoints (10.64a)–(10.64c); rows C55, C56, W58, C59 | qualitative locking (Yuan–Hunt; Contreras), which fixes neither the interval nor the excursion |
| T26 positive-transition bracket and $q^2(\varepsilon_{\rm crit}-\tfrac14)\to\pi^2/8$ | DERIVED by the v1.5 audit; re-derived here | PROVEN | even $q\ge4$ | explicit period-four competitor; exact Taylor coefficients; rows C60, C61 | — |
| P27 weighted complete-square class and its switching counterexample | DERIVED by the v1.5 audit; re-derived here | PROVEN (sufficient condition) | even $q\ge4$, positive Lipschitz $h$, $\max h/\min h<R(q)$ | complete-square geometry, series cost, explicit bump weight; rows C62, W63 | Leplaideur–Mengue Theorem A (imported) |
| T28 additive stability and exact two-cost reduction | CONSTRUCTED / EXTENDED in v1.7 | PROVEN | even $q\ge4$, $\psi\in C^2$, $\mathcal N_q(\psi)\le1/2$ | Hermite jets, domination by the square, all-path gap, compensated telescoping; C65–C66, V70 | qualitative periodic locking and LM pressure representation imported; explicit domain and costs added |
| Cor29 additive third harmonic | DERIVED in v1.7 | PROVEN | $(\varepsilon,\eta)\in\mathcal T_q$ or the stated local diamond; fixed $\lvert\eta\rvert\le1/24$ for transition asymptotics | exact factorisation, convex sub-actions, period-four crossing, symbolic expansion; C67–C68 | extends T25–T27 beyond a prescribed weighted square |
| Cor30 symmetry-breaking excursion switch | DERIVED in v1.7 | PROVEN | $\lvert\eta\rvert\le1/(2K_{q,1})$ for the sine perturbation | T28, strict positive series, two reflected costs; C69, V70 | min-plus corners are familiar; explicit circle switch and path exclusion added |
| Inherited S and N results | INHERITED / SPECIALIZED / CONDITIONAL | as marked in the appendices | as marked | appendices | as marked |

The status column uses the paper-native epistemic axis (PROVEN, DERIVED, VERIFIED, HYPOTHESIS, OPEN). Novelty classes are IMPORTED, SPECIALIZED, EXTENDED, NEW; the prior-art sweep is documented in Section 12 and Appendix L, and no NOT_FOUND is treated as ABSENT.

### 1.5 Load-bearing assumptions and non-claims

The load-bearing assumptions are the charge and energy types of the rotor–compensator reference, the declared spin parent of the source, the absence of postselection everywhere, the full position space in the writing model, the explicit accounting of every supplied resource (calibration phase, source coherence, capture, clock), and, for the asymptotic statements, the weak convergence of the rate measure with a continuous strictly increasing cumulative at the relevant quantiles. The upstream dependencies are the invariant readout and joint-reference ceiling of the reference paper (ZS-M71), the boundary-current and emission forms of ZS-M70, the Coulomb projection identity of ZS-M69 and the typed action of ZS-S14; none of these is modified. The physical bridge status is CONDITIONAL throughout: the theorems supply the bounds into which any future action-derived carrier, apparatus, capture rule and storage rate must be substituted; they do not select them.


For T31–P34 specifically, the integer multiplier, nonzero integer common shift and single uniform initial phase are load-bearing. The new results are unweighted and use $n$-speed probabilities; they do not by themselves determine the first-loss maximum on a supplied physical time window. Imported inputs are classical Fourier–Bessel positivity, geometric pressure regularity, the differentiable Gärtner–Ellis theorem and the explicitly credited first-resonance coefficient. The mathematical proof is not conditional on resolving the programme's physical bridge.

## 2. The integrated model and its three times

### 2.1 Reference, compensator and finite source

The rotor $R$ has charge basis $|m\rangle$, $m\in\mathbb Z$, with bare energy $\nu m^2$. The neutral compensator $C$ has levels $n=0,\ldots,N$ with energy $\nu n$. Inside a shell with $N\ge j^2$ the logical basis is

$$
|m\rangle_j=|m\rangle_R\,|j^2-m^2\rangle_C,\qquad -j\le m\le j,
\tag{2.1}
$$

and every element of the shell has the same bare energy $\nu j^2$. The source carries a charge $b=0,\ldots,B$ in a $(B+1)$-dimensional space, and we use the exchange that conserves the total reference charge $q=m+b$. The declared spin parent of the source is

$$
A_B=-\frac{J\,S_x}{\sqrt{S(S+1)}},\quad S=\tfrac B2,\quad J>0,\qquad
(A_B)_{b,b+1}=-\frac{J\sqrt{(b+1)(B-b)}}{\sqrt{B(B+2)}}.
\tag{2.2}
$$

The matrix of sector $q$ is the compression $H_q=P_qA_BP_q$ of this parent to the window $I_q=[q-j,q+j]\subset[0,B]$ of source coordinates. The paper treats the evolution after the shell has been supplied or prepared; the energy-selection problem between different $j$ is inherited in Appendix S6, and the fixed-shell theorems here are never turned into an automatic optimisation principle.

For even $B$ we use the band $q=B/2+k$, $k=-w,\ldots,w$, with $j+w\le B/2$. Let $\psi_k$ be the positive normalised ground vector of $H_q$ and $E_k$ its energy, and supply

$$
c_k=\frac1{\sqrt{w+1}}\cos\frac{\pi k}{2w+2},\qquad
|\Psi(0)\rangle=\sum_{k=-w}^{w}c_k\,|\psi_k,q_k\rangle .
\tag{2.3}
$$

This state uses phase resources between charge sectors. We do not claim that a symmetric initial state and charge-conserving dynamics alone generate it: the existence of a conserving preparation isometry and the actual selection of an asymmetric input are different obligations (Appendix S6.9, S6.12.4).

### 2.2 Three quantities that are not merged

$$
\omega_k=c_kc_{k+1}v_k,\qquad v_k=\sum_b\psi_k(b)\psi_{k+1}(b)>0,\qquad \Delta_k=E_{k+1}-E_k,
$$
$$
S_B(t)=\sum_{k=-w}^{w-1}\omega_k\cos(\Delta_kt),\qquad
D_{\rm C6}(t)=|S_B(t)|,\qquad
\Gamma_B=S_B(0)=\sum_k\omega_k .
\tag{2.4}
$$

Vectors are extended by zero to the full source space, so $v_k$ is an overlap at equal $b$, not a product of arrays of different windows at equal array index. $S_B$ is the signed contrast of the fixed phase-zero C6 readout of Appendix S7.3; it is not claimed to equal, at all times, the general $\Gamma(\rho)$ in which the readout phase may be optimised (Appendix S6.8).

| Symbol | Meaning |
|---|---|
| $t_w$ | time at which the prepared reference, after closed evolution, is used for writing |
| $\tau=\pi/\Omega$ | length of the writing interval in which the spatial carrier visits the two memories under a fixed Hamiltonian |
| $t_s$ | storage time of the memories after the end of writing and separation of the carrier |
| $T_\ell$ | first time at which the unwritten C6 contrast has lost $\ell$ from its initial value |
| $D_{\rm order}$ | final output total-variation / trace distance between the two orders $AB$ and $BA$ of the same preparation |

Times are reported in dimensionless combinations $Jt$, $\Omega t$; logarithms always contain $JT$ or $\lambda/J$. Energies in different units and dimensionless chain eigenvalues are never added.

## 3. The two-boundary capacity theorem

### 3.1 Exact similarity and the universal finite inequality — Theorem 1(a)

Put $\pi_b=2^{-B}\binom Bb$, $\beta_b=\sqrt{\pi_b}$, $c_B=J/\sqrt{B(B+2)}$, $E_*=-c_BB$. Then

$$
\beta^{-1}(A_B-E_*)\beta=c_B\widetilde L,\qquad
(\widetilde Lf)_b=(B-b)(f_b-f_{b+1})+b(f_b-f_{b-1}),
\tag{3.1}
$$

the positive form of the Ehrenfest generator counting flips of $B$ independent two-state variables. The gap of the full space is $2$: the independent flip has eigenvalues $0,2$ and the tensor sum has eigenvalues $2r$. Hence

$$
\operatorname{Var}_\pi(f)\le\tfrac12\,\mathcal E(f,f),\qquad
\mathcal E(f,f)=\sum_{b=0}^{B-1}(B-b)\pi_b(f_{b+1}-f_b)^2 .
\tag{3.2}
$$

Take a proper window $I=[l,u]\ne[0,B]$ and an interior point $m\in I$; extend $f$ by $0$ on $I^c$. With the conductances $a_b=(B-b)\pi_b$ define

$$
R_L=\sum_{b=l-1}^{m-1}a_b^{-1},\qquad R_R=\sum_{b=m}^{u}a_b^{-1},\qquad
\mathcal C_m=R_L^{-1}+R_R^{-1}.
\tag{3.3}
$$

If $l=0$ the left term is $0$, if $u=B$ the right term is $0$; an absent boundary is never evaluated as $a_{-1}$ or $a_B$. The function $h$ with $h_m=1$, $h=0$ on $I^c$ and harmonic elsewhere is the explicit accumulated resistance towards each boundary, and

$$
\mathcal E(h,h)=\mathcal C_m,\qquad 0\le h\le1 .
\tag{3.4}
$$

**Theorem 1(a) [PROVEN].** Let $\widetilde\lambda_I$ be the smallest Dirichlet eigenvalue of $\widetilde L$ on $I$. Then

$$
\boxed{\;
\frac{\mathcal C_m}{\bigl[1+\sqrt{\mathcal C_m/2}\,(1+\pi_m^{-1/2})\bigr]^2}
\le\widetilde\lambda_I
\le\frac{\mathcal C_m}{\|h\|_\pi^2}\; }
\tag{3.5}
$$

and, whenever $\sqrt{\mathcal C_m/(2\pi_m)}<1$,

$$
\widetilde\lambda_I\le\frac{\mathcal C_m}{\bigl[1-\sqrt{\mathcal C_m/(2\pi_m)}\bigr]^2}.
\tag{3.6}
$$

*Proof.* For any $f$ the Cauchy–Schwarz resistance inequality towards each boundary, added, gives $\mathcal E(f,f)\ge\mathcal C_mf_m^2$, including the case $f_m=0$. With $\bar f=\sum\pi_bf_b$,
$$
\|f\|_\pi\le|\bar f|+\sqrt{\operatorname{Var}_\pi f}\le|f_m|+(1+\pi_m^{-1/2})\sqrt{\mathcal E(f,f)/2},
$$
so bounding $\|f\|_\pi^2/\mathcal E(f,f)$ from above gives the lower bound in (3.5). The Rayleigh quotient of $h$ is the upper bound. Using $|h_m-\bar h|\le\sqrt{\mathcal C_m/(2\pi_m)}$, $h_m=1$ and $\|h\|_\pi\ge\bar h$ gives (3.6). $\square$

The inequality is true for narrow windows as well, where it may be loose; for the full window $\widetilde\lambda=0$ and it is treated separately. The exact exit-time/Rayleigh sandwich B18-T1 of Appendix S6.14 is kept, and either finite certificate may be chosen. $h$, $\mathcal C_m$ and $\|h\|_\pi^2$ are rational; row C01 certifies the rational lower bound by positivity of all leading Sturm polynomials and the upper bound by a sign count.

### 3.2 The two-boundary sum on compact large windows — Theorem 1(b)

Fix $\epsilon,x_0>0$ and consider windows with

$$
\epsilon B\le l\le(\tfrac12-x_0)B,\qquad (\tfrac12+x_0)B\le u\le(1-\epsilon)B .
\tag{3.7}
$$

All $O(\cdot)$ constants depend on $\epsilon,x_0$ only. With $m=\lfloor B/2\rfloor$ put

$$
r_L=\frac l{B-l},\quad r_R=\frac{B-u}{u},\qquad
A_L=l\pi_l(1-r_L),\quad A_R=(B-u)\pi_u(1-r_R).
$$

**Theorem 1(b) [PROVEN].** Uniformly on (3.7),

$$
\boxed{\;\widetilde\lambda_{[l,u]}=(A_L+A_R)\,[1+O(B^{-1})]\; }
\tag{3.8}
$$

The same relative remainder holds after division by $Z=\sum_l^u\pi_b=1-O(e^{-cB})$. Because no boundary is discarded, the formula applies to fixed non-zero centre shifts.

*Proof.* $a_{l-1}=l\pi_l$, and

$$
\frac{a_{l-1+s}^{-1}}{a_{l-1}^{-1}}=\prod_{r=0}^{s-1}\frac{l+r}{B-l-r}.
\tag{3.9}
$$

Under the compact condition $r_L\le r_*<1$ and $l/B$ is bounded away from $0$. Up to a small fixed fraction $\eta B$ of the distance to the centre, each ratio is compared with $r_L[1+O(r/B)]$: choosing $\eta$ small enough, for all $s\le\eta B$ the difference between the product and $r_L^s$ is at most $Cs^2\rho^s/B$ for some $\rho<1$, because the logarithm of the product differs from $s\log r_L$ by $O(s^2/B)$ and, for small $\eta$, $r_L^se^{Cs^2/B}\le\rho^s$; summed, the difference is $O(B^{-1})$. For $s>\eta B$ the resistances towards the centre decrease monotonically and the head has ended at $O(\rho^{\eta B})$, so the whole tail is $O(B\rho^{\eta B})$. Therefore

$$
R_L=\frac1{l\pi_l}\Bigl[\frac1{1-r_L}+O(B^{-1})\Bigr],
\tag{3.10}
$$

and the right side is identical by reflection. Inverting and adding, $\mathcal C_m=(A_L+A_R)[1+O(B^{-1})]$. By the binomial tail bound $\mathcal C_m\le CBe^{-cB}$ and $\pi_m\asymp B^{-1/2}$, so (3.5)–(3.6) give
$$
\widetilde\lambda_I/\mathcal C_m=1+O\bigl(\sqrt{\mathcal C_m}(1+\pi_m^{-1/2})\bigr)=1+O(B^{3/4}e^{-cB/2}),
$$
which combines with (3.10). $\square$

The $O(B^{-1})$ is the newly proved remainder under the compact condition. It is not applied with one constant to $x\downarrow0$, $l/B\downarrow0$ or every boundary limit; the wider $O(1/h)$ statement that was only observed earlier is not promoted retroactively (Theorem 10 in Section 10 settles that regime). As a check, at $j=B/3$, $k=1$ the ratio $\widetilde\lambda/(A_L+A_R)$ is $0.985401,\ 0.994253,\ 0.997413,\ 0.998770$ at $B=48,96,192,384$; the fraction of the right boundary is still $0.038112$ at the last size, so no one-sided approximation can drive the relative error to zero. This instance targets the earlier proof gap directly.

### 3.3 Uniform lemma for adjacent sector differences and overlaps

Assume $B$ even, $j/B\to a$, $w/B\to b$ with

$$
0<b<a,\qquad a+b\le\tfrac12,\qquad j+w\le\tfrac B2 .
\tag{3.11}
$$

If $a+b<1/2$, (3.7) holds on the whole band with fixed $\epsilon,x_0$. The endpoint $a+b=1/2$ is included by the following split. Fix a small $\delta>0$. For $|k|\le\delta B$ both boundaries lie in the compact region. Otherwise the near boundary, with index $n+|k|$ where $n=B/2-j$, is still in the compact region, and the far boundary, with index $n-|k|$, is at least $2\delta B$ farther; its capacity is at most the first conductance $B\pi_{n-|k|}$ and its ratio to the near capacity vanishes like $CB^c\rho^{2\delta B}$, $\rho<1$. At the actual endpoint that capacity is set to $0$. Hence the two-boundary sum (3.8) with relative $O(B^{-1})$ holds on the entire band. For sufficiently large $B$ and $k=0,\ldots,w-1$ there are positive constants $c_1,c_2$ with

$$
0<c_1(A_L^{k+1}+A_R^{k+1})\le\widetilde\lambda_{k+1}-\widetilde\lambda_k\le c_2(A_L^{k+1}+A_R^{k+1}),
\tag{3.12}
$$

and therefore

$$
\sup_{-w\le k<w}\Bigl|\frac1B\log\frac{|\Delta_k|}{J}+I\Bigl(a-\frac{|k+\tfrac12|}{B}\Bigr)\Bigr|\longrightarrow0,\qquad
I(x)=(\tfrac12+x)\log(1+2x)+(\tfrac12-x)\log(1-2x).
\tag{3.13}
$$

At finite $B$ the argument $a$ is more accurately replaced by $j/B$.

*Proof of the difference bound.* With $n=B/2-j$ and $A(v)=v\pi_v(B-2v)/(B-v)$ the sum is $A(n+k)+A(n-k)$, and the adjacent ratio is exactly

$$
\frac{A(v+1)}{A(v)}=\frac{(B-v)^2(B-2v-2)}{v(B-v-1)(B-2v)}=\frac{B-v}{v}[1+O(B^{-1})].
\tag{3.14}
$$

On the band with $v\ge1$ this ratio exceeds a uniform $R_0>1$; $A(0)=0$ is kept aside and no ratio is taken there. Thus $A(n-k)/A(n+k)\le R_0^{-2k}$. Beyond a fixed $k_0$ the increase of the growing boundary dominates the decrease of the other by a fixed factor; for the finitely many $0\le k<k_0$, with $r=n/(B-n)$, the leading difference is

$$
A(n)(r^{-1}-1)(r^{-k}-r^{k+1})[1+O(B^{-1})]>0,
\tag{3.15}
$$

whose positive coefficient is bounded away from $0$ under the compact condition. The uniform relative remainder of (3.8) is smaller than this positive difference by $O(B^{-1})$, so (3.12) follows; Stirling or binomial-entropy bounds give (3.13); $E_k=E_{-k}$ covers negative $k$. $\square$

This is band monotonicity for sufficiently large $B$ under (3.11); universal monotonicity for all finite $B,j,k$ is not claimed here (row C01 and the exhaustive finite checks recorded in Appendix S6.14 cover finite ranges).

*Proof of the overlap bound.* Write the zero-extended normalised ground vectors as $\psi_k=\beta f_k$ with $f_k>0$ on its window, so $\|f_k\|_\pi=1$ and $\mathcal E(f_k,f_k)=\widetilde\lambda_k$. By (3.2), $\bar f_k\ge\sqrt{1-\widetilde\lambda_k/2}$, hence $\|\psi_k-\beta\|^2=2(1-\bar f_k)\le\widetilde\lambda_k$ for large $B$, and

$$
1-v_k=\tfrac12\|\psi_k-\psi_{k+1}\|^2\le\tfrac12\bigl(\sqrt{\widetilde\lambda_k}+\sqrt{\widetilde\lambda_{k+1}}\bigr)^2 .
\tag{3.16}
$$

So $v_k\to1$ and $\Gamma_B\to1$ uniformly on the band. This is the uniformity of the weights that was missing from the earlier loss-time argument. $\square$


## 4. The complete interval for the loss-dependent first time — Theorem 2

### 4.1 A stronger finite upper bound first

For arbitrary positive weights $\omega_i$ and real frequencies $\Delta_i$ put $\Gamma=\sum\omega_i$, $S(t)=\sum\omega_i\cos\Delta_it$, $M(t)=\Gamma-S(t)$, and for $0<\ell<\Gamma$

$$
T_\ell=\inf\{t\ge0:\ \Gamma-|S(t)|\ge\ell\}.
$$

By continuity the first time at which $M$ reaches $\ell$ coincides with $T_\ell$, since before it $S>\Gamma-\ell>0$. In the definitions below an empty set gives the supremum $+\infty$.

$$
A(t)=\sum_i\omega_i\min\{2,\Delta_i^2t^2/2\},\qquad
B(T)=\sum_{i:\Delta_i\ne0}\omega_i\Bigl(1-\frac1{|\Delta_i|T}\Bigr)_+ .
\tag{4.1}
$$

**Theorem 2(a) [PROVEN].**

$$
\boxed{\;\sup\{t:A(t)<\ell\}\ \le\ T_\ell\ \le\ \inf\{T:B(T)\ge\ell\}\;}
\tag{4.2}
$$

*Proof.* $1-\cos z\le\min(2,z^2/2)$ gives the lower bound. For the upper bound,

$$
\frac1T\int_0^TM(t)\,dt=\sum_i\omega_i\,[1-\operatorname{sinc}(\Delta_iT)]\ \ge\ B(T),
\tag{4.3}
$$

some time in $[0,T]$ has $M$ at least equal to its average, and continuity of the first passage applies. Only $1-\operatorname{sinc}z\ge0$ and $\operatorname{sinc}z\le1/|z|$ were used. $\square$

$A$ and $B$ are monotone, so both ends are computed without searching an oscillating first passage on a grid. The earlier bound $\tfrac12\sum_{|\Delta_i|T\ge2}\omega_i$ is at most $B(T)$, so the new upper bound is never worse. A finite upper bound arises this way only if the total weight of the non-zero frequencies exceeds $\ell$; exact zero frequencies are kept separately, not deleted.

### 4.2 Exact sine cumulative and logarithmic time

On the spin band under (3.11) fix $\ell\in(0,\tfrac12)$ independently of $B$. Define $F:[0,1]\to[0,1]$ and $x_p$ by

$$
F(y)=y-\frac{\sin\pi y}{\pi},\qquad y_p=F^{-1}(p),\qquad x_p=a-b+b\,y_p .
\tag{4.4}
$$

$F'>0$ on $(0,1)$, so the inverse is unique.

**Theorem 2(b) [PROVEN].**

$$
\boxed{\;
I(x_{\ell/2})\le\liminf_{B\to\infty}\frac{\log(JT_\ell)}B
\le\limsup_{B\to\infty}\frac{\log(JT_\ell)}B\le I(x_\ell)\;}
\tag{4.5}
$$

No claim is made that the exact exponent equals either end. The proof uses no rational independence of frequencies, no phase randomness, no recurrence-time estimate and no long-time time grid.

*Proof: limit of the weight measure.* By (2.3), (3.16) and Riemann sums,

$$
\sum_k\omega_k\delta_{k/B}\Rightarrow\frac1b\cos^2\frac{\pi s}{2b}\,\mathbf 1_{[-b,b]}(s)\,ds .
\tag{4.6}
$$

The mass of the two edge layers of thickness $d=by$ is

$$
\frac2b\int_{b-d}^{b}\cos^2\frac{\pi s}{2b}\,ds=\frac db-\frac{\sin(\pi d/b)}\pi=F(y).
\tag{4.7}
$$

So $(\pi^2/6)y^3$ is only the leading term as $y\downarrow0$; at finite loss (4.7) must be used.

*Proof: fast and slow frequencies.* Put $JT_B=e^{Bz}$. By (3.13), on the interval where $I(a-|s|)<z$ one has $|\Delta|T_B\to\infty$ exponentially, and on the complementary interval $|\Delta|T_B\to0$ exponentially. Leaving a boundary strip of width $\eta>0$, the convergence is uniform on the rest; the limiting mass of the strip vanishes as $\eta\downarrow0$, so one may take $B\to\infty$ first and then $\eta\downarrow0$. Denote the mass of the fast part by $p(z)$; then $p(I(x_p))=p$.

*Lower bound.* For all $0\le t\le T_B$ the loss of the fast terms is at most twice their weight and the slow terms go to $0$ uniformly, hence
$$
\limsup_B\sup_{0\le t\le T_B}M_B(t)\le2p(z).
$$
Choosing $z<I(x_{\ell/2})$ gives $2p(z)<\ell$, so for large $B$ the first loss occurs after $T_B$.

*Upper bound.* In the exact average (4.3) the $\operatorname{sinc}$ of the fast terms tends to $0$ and that of the slow terms to $1$; all terms are bounded by $2$ and the strip mass vanishes, so
$$
\lim_B\frac1{T_B}\int_0^{T_B}M_B(t)\,dt=p(z).
$$
Choosing $z>I(x_\ell)$ makes the average exceed $\ell$, so $T_\ell\le T_B$. Let each $z$ tend to its threshold. $\square$

The same argument gives a version for general weighted frequency families.

**Theorem 2(c), general weighted-frequency version [PROVEN].** For each $B$ let $\omega_{B,i}>0$, $\Delta_{B,i}\ne0$, $\Gamma_B=\sum_i\omega_{B,i}\to1$, and let the finite measures

$$
\mu_B=\sum_i\omega_{B,i}\,\delta_{\alpha_{B,i}},\qquad \alpha_{B,i}=-B^{-1}\log(|\Delta_{B,i}|/J)
$$

converge weakly to a probability measure $\mu$ on the real line. If the cumulative $H(z)=\mu((-\infty,z])$ is continuous and strictly increasing near the finite quantiles $q_p=\inf\{z:H(z)\ge p\}$ for $p=\ell/2,\ell$, then

$$
q_{\ell/2}\le\liminf_B B^{-1}\log(JT_\ell)\le\limsup_B B^{-1}\log(JT_\ell)\le q_\ell .
\tag{4.5a}
$$

*Proof.* With $JT_B=e^{Bz}$, terms with $\alpha<z-\eta$ are fast and terms with $\alpha>z+\eta$ are slow; the mass of the middle strip vanishes as $\eta\downarrow0$ by weak convergence and continuity of $H$. The all-time loss bound becomes $2H(z)$ and the time-average limit becomes $H(z)$. Strict monotonicity gives strict inequalities on both sides of the two critical quantiles and the first passage is squeezed as before. $\square$

Two harmless relaxations, used in Section 10, do not change the proof: a family of modes of total weight $o(1)$ may be arbitrary (including zero frequencies), since it contributes at most $o(1)$ to any loss and to any average; and the normalisation $\Gamma_B\to1$ may be replaced by $\Gamma_B\to\Gamma_\infty>0$ after rescaling $\ell$. For the spin compression the uniform profile of Section 3 and the weight limit (4.6) prove the measure convergence, with $q_p=I(x_p)$. This is an exact sufficient condition applicable to other sources. The mean exit time of a Markov chain is never identified with the first loss of a quantum record.

### 4.3 Size of the improvement and the small-loss limit

For $a=\tfrac13$, $b=\tfrac16$ the following are asymptotic exponent intervals, not a table into which finite-$B$ values of $\log(JT)/B$ must already fall.

| loss $\ell$ | lower front $I(x_{\ell/2})$ | upper front $I(x_\ell)$ | exact-sine upper front of the earlier method, $I(x_{2\ell})$ |
|---:|---:|---:|---:|
| 0.02 | 0.079974 | 0.086869 | 0.096127 |
| 0.10 | 0.099770 | 0.113894 | 0.134097 |
| 0.30 | 0.124771 | 0.150287 | 0.191095 |

At $\ell=0.3$ the upper front drops from $0.1911$ to $0.1503$, within the same definition and sine cumulative; the earlier cubic-approximation numbers are not mixed in. Moreover

$$
\lim_{\ell\downarrow0}I(x_{\ell/2})=\lim_{\ell\downarrow0}I(x_\ell)=I(a-b),
\tag{4.8}
$$

so the common exponent closes in the small-loss limit; this is not a theorem in which $\ell$ and $B$ are sent to their limits at arbitrary joint rates.

### 4.4 Certificates for the exact finite matrices — Proposition 21

The v1.2 first-loss scans used high-precision eigenvalues followed by floating weights, gaps and cosines. They did not propagate all round-off errors. C45 supplies a separate certificate for the exact finite matrix, rather than upgrading those old scans by changing their label.

**Proposition 21 [CERTIFIED in the stated finite instances].** For the standard spin band, $J=1$, $\ell=1/10$, the first loss lies in the following rational intervals. Displayed decimal endpoints are rounded outwards; the JSON stores exact rational endpoints.

| $B$ | certified lower bound | certified upper bound |
|---:|---:|---:|
| 24 | 312.70000839 | 312.70001221 |
| 48 | 5064.57369232 | 5064.57369614 |
| 96 | 1005189.33428192 | 1005189.33428574 |

The underlying rational intervals have width $2^{-18}$. For each row the complete earlier interval $[0,T_-)$ is excluded, not only a grid of sampled times.

**Certificate construction.** Scale the spin matrix by $\sqrt{B(B+2)}$; its squared positive edges are the integers $(b+1)(B-b)$. For a rational trial $x=N/Q$, the leading determinants of $xI-C$ have integer numerators satisfying
$D_{r+1}=ND_r-e_r^2Q^2D_{r-1}$, $D_0=1$, $D_1=N$.
All are positive exactly when $x$ is strictly above the largest eigenvalue. Integer bisection isolates that root. The positive eigenvector is obtained by the three-term recurrence, then normalized using outward square-root intervals. Equal-coordinate overlaps and the sine preparation coefficients are enclosed in the same arithmetic.

All interval endpoints lie on the lattice $2^{-208}\mathbb Z$. Addition is exact, multiplication and division use integer floor/ceiling, and square roots use integer square-root bounds. The Machin identity $\pi=16\arctan(1/5)-4\arctan(1/239)$ with alternating-series remainders encloses $\pi$. After reduction by an integer multiple of $2\pi$, cosine is evaluated with its degree-112 Taylor polynomial and the rigorous bound $4^{114}/114!$ on the remainder for reduced arguments of modulus at most $4$. Reduction and its error are both interval operations. No floating eigenvalue or trigonometric library is used in the certificate; a floating midpoint selects only the integer for argument reduction, whose validity is checked afterwards.

Finally, $L_*=\sum_i w_i|\nu_i|$ bounds $|M'(t)|$. A time cell with midpoint $m$ and radius $h$ is excluded whenever the outward upper bound of $M(m)+hL_*$ is below $\ell$. Cells are visited in chronological order, subdividing only unexcluded cells. The upper endpoint is accepted only when its outward **lower** loss bound is above $\ell$. If the bounds do not separate, the code returns failure, not a certificate. This proves the asserted first-loss enclosure. C45 also rejects a fault that asserts the certified crossing endpoint is still below threshold.

The engine applies to other finite sizes when it terminates successfully; no uniform complexity bound, all-$B$ success, asymptotic $\kappa$, or exact first-loss exponent is inferred from these three instances. Standard interval arithmetic and the Sturm/Sylvester criterion are imported methods; the complete propagation through this particular preparation/readout problem is the new executable closure.


## 5. A different law for fixed windows and the resource correction — Theorem 3

### 5.1 Controlled expansion of a general fixed window

Now fix $j,w$ and let even $B\to\infty$; this limit is outside (3.11). Let $K=B(B+2)$, $\theta_j=\pi/(2j+2)$, $C_j=\cos\theta_j$. With the edge index $i=0,\ldots,2j-1$ of the window and $s=k-j+i$,

$$
(H_k/J)_{i,i+1}=-\tfrac12\sqrt{1-4s(s+1)/K}=-\tfrac12+\frac{s(s+1)}K+O(K^{-2}).
\tag{5.1}
$$

Use the ground vector of the uniform path $v_i=(j+1)^{-1/2}\sin[(i+1)\theta_j]$ and its gap $d_j=C_j-\cos(2\theta_j)>0$. In this section $\psi_k-v$ is a comparison in the $(2j+1)$-dimensional coordinates of each window aligned from its left end; actual overlaps of adjacent windows are again computed after zero extension to the source space.

**Theorem 3(a) [PROVEN].** Uniformly in $|k|\le w$,

$$
E_k=-JC_j+\frac{2J}K\bigl(C_jk^2+\kappa_j\bigr)+O(JK^{-2}),\qquad \|\psi_k-v\|=O(K^{-1}),
\tag{5.2}
$$

with $\kappa_j=\sum_{i=1}^{2j}v_{i-1}v_i(j-i)(j+1-i)$. Hence, uniformly on compact $\tau$ intervals,

$$
S_B(K\tau/J)=f_{j,w}(\tau)+O(K^{-1}),\qquad
f_{j,w}(\tau)=C_j\sum_{k=-w}^{w-1}c_kc_{k+1}\cos[2C_j(2k+1)\tau].
\tag{5.3}
$$

*Proof and remainder.* $M=\max_{|k|\le w,i}|s(s+1)|$ is a fixed constant. For $K\ge8M$ the row-sum norm of the square-root Taylor remainder is at most $6JM^2/K^2$ and the full perturbation norm at most $4JM/K$. If moreover $K\ge16M/d_j$, the second-order energy error in the ground/complement Schur-complement decomposition is at most $2\|H-H_0\|^2/(Jd_j)$, so $JM^2(6+32/d_j)/K^2$ serves as the energy remainder constant in (5.2). From the complement equation the component of the ground vector orthogonal to $v$ is at most $2\|H-H_0\|/(Jd_j)$, so the vector error is $O(K^{-1})$. In the first-order Rayleigh quotient the terms odd in $k$ vanish by path reflection and the coefficient of $k^2$ is $2C_j$. Multiplying adjacent energy differences by $K\tau/J$ leaves a phase remainder $O(K^{-1})$ on compact $\tau$, and the overlaps are $C_j+O(K^{-1})$, giving (5.3). $\square$

The first-order formula is inherited from B14 (Appendix S6.11); what is added is the explicit remainder needed for fixed windows and long observation times and its stable transfer to the first passage. The already known $B^2$ finding is not counted again.

### 5.2 The transversal first loss and the exact counterexample

With $\Gamma_\infty=C_j\cos[\pi/(2w+2)]$ and $\tau_0=\pi/[4C_j(2w-1)]$, $f_{j,w}$ is non-negative and strictly decreasing on $[0,\tau_0]$, because every positive frequency has its phase in $[0,\pi/2]$ there and positive weight. For $0<\ell<\Gamma_\infty-f_{j,w}(\tau_0)$ there is a unique crossing point $\tau_\ell$. Uniformity of (5.3), a positive margin before the crossing and a negative derivative at it give

$$
\boxed{\;T_\ell=\frac KJ\,[\tau_\ell+O(K^{-1})]=\Theta(B^2/J).\;}
\tag{5.4}
$$

For $w=1$, mirror symmetry gives at every finite $B$ exactly

$$
D_B(t)=\Gamma_B|\cos(\delta_Bt)|,\qquad
T_\ell=\frac{\arccos(1-\ell/\Gamma_B)}{\delta_B},\qquad \delta_B=E_1-E_0>0,
\tag{5.5}
$$

and, for large $B$ and $0<\ell<\Gamma_B$,

$$
\frac{JT_\ell}{B(B+2)}\longrightarrow\frac1{2C_j}\arccos\Bigl(1-\frac{\sqrt2\,\ell}{C_j}\Bigr).
\tag{5.6}
$$

For $j=2$, $w=1$, $\ell=0.1$ the exact formula (5.5), with no time grid, gives

| $B$ | $\Gamma_B$ | $\delta_B/J$ | $JT_\ell$ |
|---:|---:|---:|---:|
| 6 | 0.653889 | 0.0294536 | 19.0248 |
| 24 | 0.615953 | 0.00274116 | 210.797 |
| 48 | 0.613307 | 0.000719374 | 805.020 |
| 192 | 0.612433 | $4.64909\times10^{-5}$ | 12465.6 |

A 60-digit outward interval computation of the earlier review also certified $JT_6<100<400<JT_{48}$; $T_{48}/T_6\simeq42.3142$. The counterexample lives inside the declared model and does not refute the derivative of the scalar rate function.

### 5.3 The correct resource ledger replacing B19

$$
\frac d{dB}\bigl[B\,I(h/B)\bigr]=\tfrac12\log\bigl(1-4h^2/B^2\bigr)<0
\tag{5.7}
$$

is true. But fixing $h$ and letting $B\to\infty$ leaves the large-deviation regime $h/B\ge x_0>0$. So (5.7) decides neither the actual $T_\ell$, nor the finite-time bounds, nor a global optimisation over all $B$.

| Question | Conclusion allowed here |
|---|---|
| $j,w\propto B$ under (3.11) | $\log(JT_\ell)=\Theta(B)$; the loss-dependent interval is (4.5) |
| $j,w$ fixed | $JT_\ell=\Theta(B^2)$ at a transversal loss |
| $N$ fixed, no cost or ceiling on $B$ | keeping a fixed window with $N\ge j^2$, the actual lifetime can grow as $B^2$ without bound; there is no universal lifetime ceiling from $N$ alone |
| joint budget such as $B\le c\sqrt N$, $j,w\propto\sqrt N$ | in that declared class $\log(JT)=O(\sqrt N)$ is attainable, but the global source optimum and the minimal-source attainment are separate problems |
| storage time after writing | not fixed by the source $B$; governed by the memory-channel $\chi$, the errors and the protection resources |

The unrestricted readings "the minimal source globally maximises the actual storage time" and "the compensator bandwidth alone bounds the actual lifetime by a square-root exponent" are **retracted**. The finite table and the comparison witness of that section are kept as comparisons of the listed cases (Appendix S6.15). The corrected result is that different scaling paths show opposite trends.

### 5.4 Parity, averages and storage kept apart

Let $a_0$ be the total weight of the exact zero frequencies and $a_\nu$ the weight grouped at equal absolute frequency $\nu$. Then, without rational independence,

$$
\overline S=a_0,\qquad \overline{S^2}=a_0^2+\tfrac12\sum_{\nu>0}a_\nu^2=:Q_2,
$$
$$
\frac{Q_2}{\Gamma_B}\le\liminf_{T\to\infty}\frac1T\int_0^T|S(t)|dt\le\limsup_{T\to\infty}\frac1T\int_0^T|S(t)|dt\le\sqrt{Q_2}.
\tag{5.8}
$$

The proof is the orthogonal averaging of cosines with distinct real frequencies, $S^2\le\Gamma_B|S|$, and Cauchy–Schwarz. For odd $B$ the two central adjacent windows are mirror images, so one exact degeneracy exists; all other non-degeneracies and additional frequency collisions must be checked in each range. A positive average total-variation lower bound exists for even $B$ too. The average lower bound is **not** a positive floor at all times. So the earlier "odd/even permanent record" is confined to a statement about the central zero frequency and the signed average, and stable storage is computed separately in the pointer channel of Section 8.


## 6. The order record written at two places — Theorem 4

### 6.1 The exact strong-coupling result of the note is inherited

Use logical qubits $S,A,B$ that are neutral, or share one charge and a degenerate energy. The initial state is

$$
\rho_0=\tfrac12(I+rY)_S\otimes|++\rangle\langle++|_{AB},\qquad |r|\le1 .
$$

In $U_A=I_S\otimes P_{0,A}+X_S\otimes P_{1,A}$ and $U_B=I_S\otimes P_{0,B}+Z_S\otimes P_{1,B}$ the omitted memory factors are identities. The history $AB$ is the order $U_BU_A$ and $BA$ is $U_AU_B$. Tracing the carrier,

$$
\rho^{AB}_M=\frac{I+rY_AX_B}4,\qquad \rho^{BA}_M=\frac{I-rX_AY_B}4 .
\tag{6.1}
$$

Both marginals of both histories are $I/2$; the eigenvalues of the difference are $r/2,-r/2,0,0$, so $D=|r|/2$. Every memory component is obtained from
$$
\langle ab|\rho^h_M|a'b'\rangle=\tfrac14\operatorname{tr}\bigl[W^h_{ab}\tfrac12(I+rY)W^{h\dagger}_{a'b'}\bigr],\qquad W^{AB}_{ab}=Z^bX^a,\quad W^{BA}_{ab}=X^aZ^b .
$$

The pre-declared local readouts $Y_A$, $X_B$ with later classical comparison give

$$
p(a,b|AB)=\frac{1+rab}4,\qquad p(a,b|BA)=\frac14,\qquad D_{\rm read}=|r|/2,
\tag{6.2}
$$

with single-pair success probability $3/4$ at $r=1$ under equal priors. This does not mean that an arbitrary history is perfectly recovered in one shot. The general pulse-angle result N2 and the generalisations and limits N3–N5 of the note are kept in Appendix N.

### 6.2 The full-transport construction with a fixed Hamiltonian

For each history $h\in\{AB,BA\}$ take a corridor of four positions $n=0,1,2,3$. The history is fixed by the initially occupied corridor. The Hilbert space of one complete model is

$$
\mathcal H=\mathbb C^2_{\rm route}\otimes\mathbb C^4_{\rm position}\otimes\mathbb C^2_S\otimes\mathbb C^2_A\otimes\mathbb C^2_B,\qquad \dim\mathcal H=64 .
\tag{6.3}
$$

The route is a prepared classical input and is not itself read at the end. $A,B$ are the same two local memories, visited in different orders by the two corridors; a memory couples only to the link adjacent to it. This local graph and its link couplings are declared **supplied apparatus structure**.

$$
H_h=\frac\Omega2\sum_{n=0}^{2}\sqrt{(n+1)(3-n)}\bigl(|n+1\rangle\langle n|\otimes U^h_n+{\rm h.c.}\bigr),
\tag{6.4}
$$

with $(U^{AB}_0,U^{AB}_1,U^{AB}_2)=(U_A,U_B,I)$ and $(U^{BA}_0,U^{BA}_1,U^{BA}_2)=(U_B,U_A,I)$. $H=H_{AB}\oplus H_{BA}$ is time-independent. If the internal code carries one charge, the total carrier number is conserved and so is the energy of $H$ over the writing interval; the bare kinetic energy and the memory-coupling energy are not claimed to be conserved separately.

**Theorem 4(a) [PROVEN].** At $\tau=\pi/\Omega$, for every internal input $|\chi\rangle$,

$$
e^{-iH_h\tau}|h,0\rangle|\chi\rangle=i\,|h,3\rangle\,U^h_1U^h_0|\chi\rangle .
\tag{6.5}
$$

*Proof.* With the prefixes $W_0=I$, $W_1=U_0$, $W_2=U_1U_0$, $W_3=U_1U_0$ and $D_h=\sum_n|n\rangle\langle n|\otimes W_n$,

$$
H_h=D_h\bigl(\Omega S_x^{(3/2)}\otimes I_8\bigr)D_h^\dagger,
\tag{6.6}
$$

so the propagation is computed on the whole space from the start. The $\pi$ rotation of spin $3/2$ sends $0\to3$ with amplitude $(-i)^3=i$; undoing $D_h$ gives (6.5). $\square$

No projection onto the code and no renormalisation onto a successful position is performed during transport. Row C07 verifies both 32-dimensional blocks with the exact gauge identity and $e^{-i\pi H_h/\Omega}=i[4(H_h/\Omega)^3-7H_h/\Omega]/3$; row V08 recomputes the full matrix exponential independently. The transfer itself is an application of perfect state transfer, not a new transport principle.

### 6.3 Timing error and the end of writing

The exact position probabilities are

$$
p_n(t)=\binom3n\sin^{2n}(\Omega t/2)\cos^{2(3-n)}(\Omega t/2).
\tag{6.7}
$$

Tracing the position, the different prefixes appear as a mixture with these probabilities; $n=2,3$ have completed both gates and give the same ideal memories. Hence at $t=\tau+\delta t$, with $q=\sin^2(\Omega\delta t/2)$,

$$
D\bigl(\rho^h_M(t),\rho^h_M(\tau)\bigr)\le p_0+p_1=q^2(3-2q)\le3(\Omega\delta t/2)^4 .
\tag{6.8}
$$

This is the output-state error of **each** history. Away from the exact $\tau$ partial writing can also produce local marginal differences; no claim is made that the signal sits purely in correlations at all times.

Storage begins only after the completed carrier is extracted or the coupling ended; if the carrier keeps oscillating on the same chain the gates can also run backwards. The model charges the capture/separation operation and its timing to the apparatus. Equation (6.4) is the autonomous transport of a writing interval, not an autonomous universe that locks a record for ever without an external clock or capture. Moving the carrier into a vacuum sector with zero coupling there makes the post-writing storage channel unambiguous. The energy and clock cost of the capture device is an object for microscopic derivation.

### 6.4 The 24-dimensional construction on the same map

On the 24-dimensional space of positions $O,A,B$ and the three qubits, let $T_{xy}=\exp[-i\pi(|x\rangle\langle y|+|y\rangle\langle x|)/2]\otimes I_8$, $V_A=I+|A\rangle\langle A|\otimes(U_A-I)$, $V_B=I+|B\rangle\langle B|\otimes(U_B-I)$. Then $V_AV_B=V_BV_A$ but

$$
T_{BO}V_BT_{AB}V_AT_{OA}V_0=iV_0U_BU_A,\qquad T_{AO}V_AT_{BA}V_BT_{OB}V_0=iV_0U_AU_B,
\tag{6.9}
$$

with $V_0|\chi\rangle=|O\rangle|\chi\rangle$. This construction uses external sequential control, but it is kept as the first exact embedding of the note into spatial transport without intermediate projections; the 64-dimensional model replaces the stepwise switching by a fixed Hamiltonian. Neither is evidence that S14 has selected the spatial graph or the couplings.

## 7. The explicit interface from the reference to the spatial record — Theorem 5

### 7.1 Deriving $r=\Gamma$ instead of assuming it

Distinguish the charged measurement probe $P$ from the neutral transport carrier $S$. The initial input of $P$ is $|x_X\rangle$, $x=\pm1$. The C6 effect is a contraction $O$ that acts as Pauli-$X$ on each charge-compatible pair and as $0$ on unmatched states,

$$
F_z=\tfrac12(I+zO),\qquad z=\pm1 .
\tag{7.1}
$$

$O$ pairs a charge decrease of $P$ with a charge increase of the rotor and preserves the shell energy of (2.1); hence $F_z$ commutes with the total readout charge and the bare energy, and $\sum_zF_z=I$ includes every outcome. Applying the source trace of (2.4),

$$
q(z|x,t_w)=\frac{1+zxS_B(t_w)}2 .
\tag{7.2}
$$

Define the channel that prepares the neutral carrier in $|y_z\rangle\langle y_z|=\tfrac12(I+zY)$:

$$
\mathcal P(\rho)=\sum_{z=\pm1}\operatorname{tr}(F_z\rho)\,|y_z\rangle\langle y_z| .
\tag{7.3}
$$

This is a completely positive trace-preserving measure-and-prepare channel. Since $F_z$ commutes with the conserved quantities and the output code is neutral and degenerate, it can be implemented by attaching a neutral register after the existing conserving instrument dilation. The outcome $z$ is never used to select a conditional success; all outcomes are summed.

**Theorem 5 [PROVEN].** The output of the channel is

$$
\boxed{\;\rho_S(t_w|x)=\tfrac12\bigl(I+xS_B(t_w)\,Y\bigr),\qquad r=xS_B(t_w).\;}
\tag{7.4}
$$

*Proof.* Substituting (7.2) into (7.3), $\sum_zq=1$ and $\sum_zzq=xS_B(t_w)$. $\square$

In the task of reading the order $AB/BA$ the calibration input $x=+1$ is supplied as a known state, and the phase resource of this probe stays on the cost sheet: **the reading in which all polarisation was created free by the source alone is not allowed.** If $x$ is hidden and mixed uniformly, $r=0$ and the order signal vanishes (row W13). The method is the same as the neutral-outcome-to-optical composition of Appendix S9.8, but here the outcome is moved into the preparation of an order-sensitive carrier.

### 7.2 Two different discrimination tasks

| Task | Fixed | Ideal local joint readout |
|---|---|---|
| order information | calibration $x=+1$; compare $AB$ vs $BA$ | $D=\lvert S_B(t_w)\rvert/2$ |
| input information | order $AB$; compare $x=+1$ vs $x=-1$ | $D=\lvert S_B(t_w)\rvert$ |

These are not called the same distinguishability, and there is no theorem that input and order are recovered simultaneously and unconditionally. The coherence still held by the source, the actual $z$ selected in a history, the output of the averaged channel and the spatial pointer parity are four different objects.

## 8. Storage dynamics and the positive total error window — Theorem 6

### 8.1 The exact difference after moving to pointers

After writing, dephase $A$ in the $Y_A$ basis and $B$ in the $X_B$ basis; this does not change the statistics of the fixed readouts. The two outputs are

$$
\bar\rho^{AB}_M=\frac{I+rY_AX_B}4,\qquad \bar\rho^{BA}_M=\frac I4,\qquad
\bar\rho^{AB}_M-\bar\rho^{BA}_M=\frac{rY_AX_B}4 .
\tag{8.1}
$$

Any trace-preserving channel acting only on the carrier after writing leaves the partial trace of the memories unchanged (its dual preserves the identity); re-coupling to the memories leaves the assumption.

### 8.2 The exact law under correlated noise

Let $Z_A^{e_A}Z_B^{e_B}$ act with history-independent probabilities $q_{e_A,e_B}$ and let a common probability $p_{\rm loss}$ leave the same failure flag in both histories. With $p_{\rm odd}=q_{01}+q_{10}$,

$$
\boxed{\;D_{\rm stored}=(1-p_{\rm loss})\frac{|r|}2\,|1-2p_{\rm odd}|.\;}
\tag{8.2}
$$

Each flip reverses the sign of its own pointer, so the difference operator $Y_AX_B$ acquires only $(-1)^{e_A+e_B}$, and the failure flag contributes nothing to the difference. That is the whole proof. For independent flips one gets $(1-2e_A)(1-2e_B)$; without independence the marginal error rates do not determine the value: two marginal flip probabilities of $1/2$ each preserve the contrast under perfectly simultaneous flips and erase it under independent flips.

### 8.3 Computing the storage time from explicit dynamics

Instead of leaving $p_{\rm odd}(t_s)$ free, fix a Markov storage model with Poisson jump rates $\gamma_A,\gamma_B,\gamma_c\ge0$ for $Z_A,Z_B,Z_AZ_B$ and a common erasure rate $\kappa_{\rm er}\ge0$. The generator on the surviving memories is

$$
\mathcal L\rho=\gamma_A(Z_A\rho Z_A-\rho)+\gamma_B(Z_B\rho Z_B-\rho)+\gamma_c(Z_AZ_B\rho Z_BZ_A-\rho).
\tag{8.3}
$$

The code is energy-degenerate, so this jump model is compatible with its bare energy; the rates and the Markov approximation are not derived from S14.

**Theorem 6 [PROVEN].** Composing the C6 calibration, the writing, the pointer channel, (8.3) and the common erasure,

$$
\boxed{\;D_{\rm order}(t_w,t_s)=\tfrac12|S_B(t_w)|\,e^{-\chi t_s},\qquad \chi=\kappa_{\rm er}+2(\gamma_A+\gamma_B).\;}
\tag{8.4}
$$

*Proof.* $\mathcal L(Y_AX_B)=-2(\gamma_A+\gamma_B)Y_AX_B$ and the simultaneous-flip term is exactly $0$; the common survival probability is $e^{-\kappa_{\rm er}t_s}$; combine with (7.4)–(8.2). $\square$

For a readout requirement $d_*>0$, if $\chi>0$ and $|S_B(t_w)|\ge2d_*$,

$$
t_s\le\chi^{-1}\log\frac{|S_B(t_w)|}{2d_*}
\tag{8.5}
$$

is the exact admissible storage time of the ideal channel. At $\chi=0$ the parity of this declared channel is preserved; this is not an infinite lifetime of any real material. The writing-resource time $B^2$ or $e^{BI}$ and the storage-channel time $\chi^{-1}$ are thereby separated in one formula.

### 8.4 Errors on the same output and the positivity certificate

If the actual comparison output is within trace distance $\eta_h$ of each ideal history output, the triangle inequality and data processing give

$$
D_{\rm actual}\ge\bigl[\tfrac12e^{-\chi t_s}|S_B(t_w)|-\eta_{AB}-\eta_{BA}\bigr]_+ .
\tag{8.6}
$$

With a total preparation error $\varepsilon_{\rm prep}$, a writing-Hamiltonian error $\|H_h^{\rm actual}-H_h\|\le\zeta$ and $|\delta t|\le d$, using the same capture/readout, a sufficient bound for one history is

$$
\eta_h\le\varepsilon_{\rm prep}+\sin^4(\Omega d/2)\,[3-2\sin^2(\Omega d/2)]+(\tau+d)\zeta+\varepsilon_{{\rm cap},h}+\varepsilon_{{\rm store},h},
\tag{8.7}
$$

for the symmetric timing window $0\le\Omega d\le\pi$. Duhamel's unitary norm bound and the contraction of the output trace distance give the Hamiltonian term. The capture and storage model errors must refer to the same actual output. Errors of the source-preparation stage are included in $\varepsilon_{\rm prep}$ or added separately; the ideal source time is not assumed to hold to arbitrary accuracy.

**The fixed verification instance.** $J=\Omega=1$, $B=48$, $j=2$, $w=1$, $t_w=20$, $t_s=100$, $\gamma_A=\gamma_B=10^{-4}$, $\gamma_c=0.1$, $\kappa_{\rm er}=10^{-4}$, $d=0.05$, $\zeta=10^{-4}$, $\varepsilon_{\rm prep}=10^{-4}$; the capture and storage channels are the declared models, so their model errors are $0$. These dimensionless inputs were fixed in advance to test the positivity of the source remainder and the spatial errors.

| Quantity | Value |
|---|---:|
| $S_B(t_w)$ | 0.6132433854 |
| ideal stored contrast | 0.2916675763 |
| contrast from the direct matrix exponential of (8.3) | 0.2916675763 |
| error bound of one history | 0.0004203302 |
| lower bound of the full comparison | **0.2908269159** |

So, within the declared inputs and error ranges, the order contrast of the admissible readout is positive. No claim is made that the actual occupied packet, source, memory and capture of S14 yield these numbers; the upstream obligation is to derive each term of (8.7) from those objects.

### 8.5 Accumulation, copying and wide space

Preparing independently $k$ new carrier–memory pairs and writing with $r=1$, the fixed readout of the note gives the same parity in $AB$ every time and a fair parity in $BA$, so the equal-prior error is $2^{-(k+1)}$. Copying one obtained parity to many places is a deterministic channel and cannot increase the original total variation. Reusing the same source without renewal does not supply the same $r$ each time; the instrument backaction of Appendix S must be carried into the next round.

The spatial dilution theorem of the note limits the class in which a fixed total energy contrast is spread over independent uniform diagonal cells; it does not exclude spatial patterns such as $|10\rangle,|01\rangle$ of equal energy. The parity storage above makes the form of the correlations and the operators on which noise acts more important than the size of the space as such. The history response N3, the current triple product N4 and the exact scope and proofs of N5 continue in Appendix N.


## 9. The exact exponent: sharpness, alignment capacity and lacunary bounds

Theorem 2 leaves the exponent of the first-loss time inside $[q_{\ell/2},q_\ell]$ and says nothing about which value, if any, it takes. The seed listed the existence and value of $\lim B^{-1}\log(JT_\ell)$ as its first remaining problem. This section resolves the status of that problem in the generality in which Theorem 2(c) was proved, and computes the exponent for several arithmetic classes.

### 9.1 Repairing the question

The interval of Theorem 2(c) depends on the frequency family only through the limiting rate measure $\mu$. The right question is therefore not "what is the exponent" but "is the exponent a function of $\mu$, and if not, of what". The two ends of the interval have transparent meanings: the lower front $\ell/2$ is reached only if all fast modes lose their full $2\omega_i$ simultaneously (perfect phase alignment at $\cos=-1$), and the upper front $\ell$ is reached only if no time does better than the time average. Everything between is a question of how well the phases $\Delta_it$ of exponentially separated frequencies can be aligned within a time window that is itself exponentially long. That is an arithmetic property of the frequencies, not a property of the rates.

**Definition (alignment capacity).** For a family as in Theorem 2(c), $z$ in the interior of the support of $\mu$, and $\eta>0$, let $\mathcal F_B(z,\eta)=\{i:\alpha_{B,i}\le z-\eta\}$ be the set of modes that are fast at the time $T_B=e^{Bz}/J$ with margin $\eta$, and let $\mu_B(z,\eta)=\sum_{i\in\mathcal F_B}\omega_{B,i}$. Define

$$
\kappa^{+}(z)=\limsup_{\eta\downarrow0}\ \limsup_B\ \Bigl[\frac{\Sigma_B(z,\eta)}{\mu_B(z,\eta)}\Bigr]-1,\qquad
\kappa^{-}(z)=\liminf_{\eta\downarrow0}\ \liminf_B\ \Bigl[\frac{\Sigma_B(z,\eta)}{\mu_B(z,\eta)}\Bigr]-1,
$$
$$
\Sigma_B(z,\eta)=\sup_{0\le t\le T_B}\sum_{i\in\mathcal F_B(z,\eta)}\omega_{B,i}\bigl(1-\cos\Delta_{B,i}t\bigr).
$$

The outer limits are written as $\limsup$ and $\liminf$ in $\eta$ because no monotonicity in $\eta$ is claimed; when the inner quantity has a limit as $\eta\downarrow0$ the two definitions reduce to it. Both require $\mu_B(z,\eta)>0$ for small $\eta$ and large $B$, which holds because $z$ is interior to the support of $\mu$.

Since the sum is at least its time average, which tends to $\mu_B(z,\eta)$, and at most $2\mu_B(z,\eta)$, one has $0\le\kappa^-(z)\le\kappa^+(z)\le1$. When $\kappa^-=\kappa^+$ the common value $\kappa(z)$ is the alignment capacity of the family at rate $z$.

**Proposition 9.1 [PROVEN; strict-crossing application repaired in v1.3].** Let $a_z=\mu(\{z\})$ and $H_-(z)=\mu((-\infty,z))=H(z)-a_z$. Under the hypotheses of Theorem 2(c), with both sets below restricted to the $z$ interior to the support of $\mu$, where $\kappa^\pm(z)$ are defined,

$$
\sup\{z:(1+\kappa^+(z))H_-(z)+2a_z<\ell\}\ \le\ \liminf_B\frac{\log JT_\ell}B,\qquad
\limsup_B\frac{\log JT_\ell}B\ \le\ \inf\{z:(1+\kappa^-(z))H_-(z)>\ell\}.
\tag{9.1a}
$$

At every continuity point of $\mu$ one has $a_z=0$ and $H_-(z)=H(z)$, so on a rate interval where $\mu$ has no atom (9.1a) reads

$$
\sup\{z:(1+\kappa^+(z))H(z)<\ell\}\ \le\ \liminf_B\frac{\log JT_\ell}B,\qquad
\limsup_B\frac{\log JT_\ell}B\ \le\ \inf\{z:(1+\kappa^-(z))H(z)>\ell\},
\tag{9.1a$'$}
$$

which is the form printed in v1.1. Both thresholds use strict inequalities. Equality cases remain unclassified; a plateau can separate the two thresholds and can prevent the existence of a single exponent.

**Why $H_-$ and not $H$ (finding F01 of the v1.1 audit).** The alignment capacity is defined through the modes with $\alpha\le z-\eta$, whose mass tends to $H_-(z)$, not to $H(z)$: an atom sitting exactly at $z$ is never in the fast set. v1.1 printed $H(z)$ in both halves and justified it by letting the middle strip vanish, which is legitimate only at a continuity point. Theorem 2(c) is not affected, because its proof uses $z$ near the two quantiles, where continuity is assumed; the defect belonged to the strengthening. The difference is not cosmetic — the following family refutes the v1.1 form.

**Counterexample (sharpness of the hypothesis).** Take $J=1$, $\ell=2/5$ and

$$
\mu=p\,U[2-\log2,\,2]+w\,\delta_2+r\,U[2,3]+s\,U[3,4],\qquad
p=\tfrac{21}{100},\ w=\tfrac7{100},\ r=\tfrac1{1000},\ s=\tfrac{719}{1000},
\tag{9.1c}
$$

$U[a,b]$ being the uniform probability measure. The point $z=2$ is interior to the support, and $H$ is continuous and strictly increasing near $q_{\ell/2}=2-\tfrac{\log2}{21}$ and near $q_\ell=3+\tfrac{119}{719}$, so the hypotheses of Theorem 2(c) hold as printed. Realise $\mu$ at each $B$ by four groups with positive weights summing to $1$:

| group | frequencies and weights | limiting mass |
|---|---|---|
| dyadic $D$ | $\nu_k=e^{-2B}2^k$, $k=0,\ldots,B-1$, each of weight $p/B$ | $p\,U[2-\log2,2]$ |
| Fejér $A$ | $\nu_m=(m/B)e^{-2B}$, $m=1,\ldots,B$, weight $\tfrac{2w}B(1-\tfrac m{B+1})$ | $w\,\delta_2$ |
| bridge $R$ | $B$ midpoint rates in $[2,3]$, $\nu=e^{-B\alpha}$, each of weight $r/B$ | $r\,U[2,3]$ |
| slow $S$ | $B$ midpoint rates in $[3,4]$, $\nu=e^{-B\alpha}$, each of weight $s/B$ | $s\,U[3,4]$ |

The rates of $A$ lie in $[2,2+\tfrac{\log B}B]$, so that group converges to the atom. The dyadic group is exactly geometric with ratio $2$, so by Theorem 13 its alignment capacity is $\beta_2=\tfrac12$, and since its fast tail is reached at $t_*=2\pi/(3\nu_*)\le e^{2B}$ for large $B$, $\kappa^-(2)=\kappa^+(2)=\tfrac12$. The v1.1 form would then give

$$
(1+\kappa^-(2))H(2)=\tfrac32(p+w)=\tfrac{21}{50}=0.42>\ell ,
$$

hence $\limsup_BB^{-1}\log T_\ell\le2$. But for every fixed $\varepsilon>0$ and every $t\le e^{(3-\varepsilon)B}$ the four groups obey, respectively, the sub-action bound $M_D\le\tfrac32p+\tfrac{8p}{3B}$ of Theorem 13, the Fejér positivity bound $M_A\le w(1+\tfrac1B)$, the trivial bound $M_R\le2r$ and the small-argument bound $M_S\le\tfrac s2e^{-2\varepsilon B}$, so

$$
\sup_{0\le t\le e^{(3-\varepsilon)B}}M_B(t)\ \le\ \frac{387}{1000}+\frac{63}{100B}+\frac{719}{2000}e^{-2\varepsilon B}\ \longrightarrow\ 0.387<\ell ,
\tag{9.1d}
$$

whence $\liminf_BB^{-1}\log T_\ell\ge3$. The two conclusions are incompatible, so the v1.1 form is false; the repaired form gives $(1+\kappa^-(2))H_-(2)=\tfrac32p=0.315<\ell$ at $z=2$ and no contradiction. Row C38 carries the exact rational version of (9.1d) — the printed bound $0.387+0.63/B$ first falls below $\ell$ at $B=49$, and at $B=64$ with $\varepsilon=\tfrac12$ it is $0.39684375<0.4$ with no time grid at all, while the true supremum is already below $\ell$ at much smaller $B$ ($0.3969$ at $B=10$, $0.3938$ at $B=14$) — together with the Fejér weight sum and the dyadic polynomial identity. Theorem 15 and the standard band are untouched, because the rate measure of the spin band has a continuous cumulative and no atom.

In particular, put $p_*=\ell/(1+\kappa)$. Suppose $\kappa(z)\equiv\kappa$ on the relevant rate range, $\mu$ has no atom there, and there is a finite $z_*=q_{p_*}$ with the strict-crossing property

$$
H(z_*-\varepsilon)<p_*<H(z_*+\varepsilon)
\quad\text{for every sufficiently small }\varepsilon>0.
\tag{9.1e}
$$

Assume that the bounds (9.1a) apply at continuity points arbitrarily close on both sides; local continuity and strict increase of $H$ is a sufficient condition. Then the exponent exists and equals the quantile:

$$
\boxed{\;\lim_B\frac{\log JT_\ell}B=q_{\ell/(1+\kappa)}\;}
\tag{9.1}
$$

The old v1.0 upper bound on the liminf is not retained as an unrestricted assertion: its use of $H(z)$ is also false at atoms. Equations (9.1a) and (9.1e) replace it. Existence of a constant $\kappa$ is not by itself a crossing hypothesis. For variable $\kappa(z)$, a strict crossing of $(1+\kappa(z))H(z)$ must be checked directly; the exponent, when proved, is that crossing location.


*Proof.* At time $T_B$ the total loss splits into the loss of $\mathcal F_B(z,\eta)$, the loss of the strip $\{z-\eta<\alpha\le z+\eta\}$, at most twice its mass, and the loss of the slow modes, which is $o(1)$ uniformly because $\Delta T_B=e^{-B(\alpha-z)}\to0$ there. Choose $z\pm\eta$ to be continuity points of $\mu$, which is possible for all but countably many $\eta$; then by weak convergence the fast mass tends to $\mu((-\infty,z-\eta])\uparrow H_-(z)$ and the strip mass tends to $\mu((z-\eta,z+\eta])\downarrow a_z$ as $\eta\downarrow0$.

The factor $2$ on $a_z$ cannot be lowered: realise the atom by $n_B$ modes of weight $a_z/n_B$ at the frequencies $\Delta_i=(2i+1)\pi/T_B$ with $\log n_B=o(B)$; their rates tend to $z$, so they sit in the strip for every fixed $\eta$, and at $t=T_B$ every one of them has $\cos\Delta_iT_B=-1$, so the strip contributes exactly $2a_z$.

If $(1+\kappa^+(z))H_-(z)+2a_z<\ell$, then for a small such $\eta$ and every large $B$ the supremum over $[0,T_B]$ of the total loss is below $\ell$, so $T_\ell>T_B$ for every large $B$ and $\liminf_BB^{-1}\log JT_\ell\ge z$; taking the supremum over such $z$ gives the left half of (9.1a). If $(1+\kappa^-(z))H_-(z)>\ell$, then for every large $B$ some $t\le T_B$ has fast loss above $\ell$ — the strip and the slow modes only add non-negative loss — so $T_\ell\le T_B$ and $\limsup_BB^{-1}\log JT_\ell\le z$; taking the infimum over such $z$ gives the right half. The two halves are not symmetric by accident: the first uses the $\limsup$ in the definition of $\kappa^+$ (no time in $[0,T_B]$ aligns enough, for all large $B$) and must pay for the atom, the second the $\liminf$ in $\kappa^-$ (some time aligns enough, for all large $B$) and may discard it. Continuity and strict monotonicity of $H$ turn the two thresholds into the stated quantiles when $\kappa$ is constant and $\mu$ has no atom there. $\square$

Theorem 2(c) is the special case $\kappa^-\ge0$, $\kappa^+\le1$, and its own proof is unaffected by the atom above, because it works with $z$ near the two quantiles, where continuity is part of its hypotheses. When $\kappa(z)$ is not constant the exact statement replacing (9.1) is the unique crossing
$$
(1+\kappa(z_*))H_-(z_*)=\ell ,
\tag{9.1b}
$$
and strict monotonicity of $H$ alone does not make the product $(1+\kappa)H_-$ strictly monotone: uniqueness of the crossing is an extra hypothesis, to be supplied or proved in each application. The theorem below shows that both ends of the interval are attained.

**Atomless plateau counterexample — incorporated from the v1.2 audit, §§4.2–4.4 (not a new discovery of this paper).** The v1.2 manuscript still claimed that a constant $\kappa$ and the absence of atoms were enough to collapse (9.1a) to the single quantile (9.1). They are not. The following family, supplied by that audit and reproduced here in full, refutes the collapse; v1.3 added the strict-crossing hypothesis (9.1e) that repairs it, and this section states the family in the language of the rest of the paper. *(The v1.3 text of this block was printed in Korean; it is translated here, with the mathematics unchanged, so that the manuscript is in one language.)*

**The explicit family.** Take $J=1$, $\ell=2/5$, $p=4/15$ and $d=2+2\log2$. For every integer $B\ge4$ put $p_B=p-1/B$ and use the following $2B$ positive frequencies with positive weights.

| block | $k$ | frequency $\nu$ | weight |
|---|---|---|---|
| $D$ | $0,\ldots,B-1$ | $e^{-2B}\,2^k$ | $p_B/B$ |
| $S$ | $0,\ldots,B-1$ | $e^{-2B}\,2^{k-3B}$ | $(1-p_B)/B$ |

The weights sum to exactly $1$. The empirical measure of $\alpha=-B^{-1}\log\nu$ converges weakly to

$$
\mu=p\,U[2-\log2,\,2]+(1-p)\,U[d,\,d+\log2] .
\tag{AP2}
$$

There is **no atom**, and $H$ is constant, equal to $p$, on the whole gap $[2,d]$. The two points that Theorem 2(c) requires are

$$
q_{\ell/2}=2-\tfrac14\log2,\qquad q_\ell=d+\tfrac2{11}\log2 ,
$$

both interior to intervals of positive constant density, so the hypotheses of Theorem 2(c) hold. On the other hand $q_{\ell/(1+1/2)}=q_{4/15}=2$, because $H$ first reaches the value $p=4/15$ at $z=2$ and then stays there.

**Alignment capacity $\kappa=\tfrac12$.** With $u(\phi)=\cos\phi+\tfrac13\cos2\phi$,

$$
\tfrac12+\cos\phi+u(2\phi)-u(\phi)=\tfrac23\bigl(\cos2\phi+\tfrac12\bigr)^2\ \ge\ 0 .
\tag{AP3}
$$

Telescoping (AP3) along $n$ consecutive dyadic frequencies of equal weight $w$ bounds their loss by $\tfrac32nw+\tfrac83w$ at every $t$. Each fast set is a union of terminal segments of the two blocks, so the total boundary error is $O(1/B)$. Conversely, let $\nu_*$ be the smallest fast frequency and take $t_*=2\pi/(3\nu_*)$: every fast frequency divided by $\nu_*$ is an integer power of $2$, so every fast cosine equals $-\tfrac12$ and the loss is exactly $\tfrac32$ times the fast mass; the margin $\eta>0$ gives $t_*\le(2\pi/3)e^{B(z-\eta)}\le e^{Bz}$ for large $B$. Dividing the two bounds, $\kappa^-=\kappa^+=\tfrac12$ **at every interior point of the support where the capacity is defined**, and the natural extension of the same definition to the gap $(2,d)$ also gives $\tfrac12$. The counterexample therefore does not rely on $\kappa$ secretly varying.

**The actual first-loss exponent.** For every $t$ the $D$ block obeys

$$
M_D(t)\le\tfrac32p_B+\frac{8p_B}{3B}=\ell-\frac{71}{90B}-\frac8{3B^2},
\tag{AP4}
$$

because $\tfrac32p=\ell$ exactly. The largest frequency of the $S$ block is $\tfrac12e^{-Bd}$, so for every fixed $\varepsilon>0$ and every $0\le t\le e^{B(d-\varepsilon)}$,

$$
M_S(t)\le\frac{1-p_B}8e^{-2\varepsilon B}.
\tag{AP5}
$$

(AP5) is smaller than the $1/B$ deficit in (AP4), so $M_B(t)<\ell$ on that whole time interval and $\liminf_BB^{-1}\log T_\ell\ge d$. This is an inequality on the entire continuum of times, not an observation on a grid. Conversely, for $z>d$ a small enough $\eta>0$ makes the limiting fast mass exceed $p$, and the same equal-phase choice pushes the loss above $\ell$ within $e^{Bz}$, so $\limsup_BB^{-1}\log T_\ell\le d$ and

$$
\boxed{\lim_{B\to\infty}B^{-1}\log T_\ell=2+2\log2\simeq3.3862943611\ \ne\ 2 .}
\tag{AP6}
$$

Row W46 checks the symbolic identity (AP3) and the all-time rational upper bound at $\varepsilon=\tfrac12$ and $B=16,32,64,128,256$, using $e^{-B}\le2^{-B}$ so that no transcendental rounding enters the refutation.

Existence of the limit is not guaranteed either. Replacing $p_B$ by $p+1/B$ makes the dyadic alignment at time of order $e^{2B}$ already exceed $\ell$, and the strict lower bound then pins the exponent at $2$; alternating the two signs with the parity of $B$ produces a family with the same $\mu$ and the same constant $\kappa$ whose $\liminf$ is $2$ and whose $\limsup$ is $d$. This consequence follows from (AP3)–(AP5) and the alignment times, not from a simulation.

### 9.2 Sharpness of the exponent interval — Theorem 7

**Theorem 7 [PROVEN].** Let $\mu$ be any probability measure on $\mathbb R$ with continuous, strictly increasing cumulative $H$ on an interval containing $q_{\ell/2}$ and $q_\ell$. There exist two admissible families in the sense of Theorem 2(c), both with limiting rate measure $\mu$ and $\Gamma_B\to1$, such that

$$
\lim_B\frac{\log JT_\ell}B=q_{\ell/2}\quad\text{for the first family},\qquad
\lim_B\frac{\log JT_\ell}B=q_\ell\quad\text{for the second family.}
$$

Consequently no theorem whose hypotheses involve only the limiting rate measure and the positivity of the weights can narrow the interval of Theorem 2(c); the exact exponent is a property of the arithmetic of the frequencies.

*Proof of the lower end: odd-multiple alignment.* Fix $q'>q_{\ell/2}$ with $2H(q')>\ell$ and put $\nu_0=Je^{-Bq'}$. Take any admissible family with limit $\mu$ (for instance the discretisation of $\mu$ on a grid of rates with weights equal to the cell masses) and replace every frequency with rate $\alpha<q'$ by the odd multiple $\nu_0(2m+1)$ with $m$ the nearest integer to $(e^{-B\alpha}J/\nu_0-1)/2$; the relative change of the frequency is at most $e^{-B(q'-\alpha)}$, so the rates and the weak limit are unchanged. At $t_*=\pi/\nu_0$ every modified mode has $\cos(\Delta t_*)=\cos((2m+1)\pi)=-1$ exactly, so the loss at $t_*$ is at least $2\mu_B(\{\alpha<q'\})\to2H(q')>\ell$; hence $T_\ell\le t_*$ for large $B$ and $\limsup B^{-1}\log JT_\ell\le q'$.

**Diagonalisation (repair of v1.1).** The construction above produces, for each fixed $q'$, a *different* family; letting $q'\downarrow q_{\ell/2}$ across families does not by itself exhibit one admissible family whose exponent is $q_{\ell/2}$, and the audit of v1.0 recorded this missing quantifier as finding F02. One family is obtained as follows. Choose $q_n\downarrow q_{\ell/2}$ with $2H(q_n)>\ell$ for every $n$. For each $n$ the discretisation converges to $\mu$, so there is $B_n$ such that for all $B\ge B_n$ the mass of $\{\alpha<q_n\}$ exceeds $\ell/2$; take $B_n$ strictly increasing. Define the family by performing the odd-multiple rounding at threshold $q_n$ for every $B$ with $B_n\le B<B_{n+1}$. Two properties survive the switching. First, the rounding changes each rounded frequency by a relative amount at most $e^{-B(q_n-\alpha)}\le1$ and each rate by $O(1/B)$, while the unrounded (slow) part is untouched, so the rate measure of the single family still converges weakly to $\mu$ and the family is admissible in the sense of Theorem 2(c). Second, for $B_n\le B<B_{n+1}$ the argument above applies with $q'=q_n$ and gives $B^{-1}\log JT_\ell\le q_n+o(1)$. Since $q_n\downarrow q_{\ell/2}$ along the (increasing) blocks, $\limsup_BB^{-1}\log JT_\ell\le q_{\ell/2}$ for this one family, and the lower bound of Theorem 2(c) gives the limit $q_{\ell/2}$. $\square$

*Proof of the upper end: Fejér levels.* Let $n=n_B\to\infty$ with $(\log n_B)/B\to0$ and let $\{\alpha_j\}$ be a grid of rates whose mesh tends to $0$, with masses $\mu_j$ summing to $1$ and converging weakly to $\mu$. At level $j$ place the $n$ frequencies $m\nu_j$, $m=1,\ldots,n$, with $\nu_j=Je^{-B\alpha_j}/n$, and weights

$$
\omega_{j,m}=\mu_j\,\frac{2(1-m/(n+1))}n,\qquad\sum_{m=1}^n\omega_{j,m}=\mu_j .
$$

The rates of level $j$ lie in $[\alpha_j,\alpha_j+(\log n)/B]$, so the limiting rate measure is $\mu$. With the Fejér kernel $F_n(\phi)=\sum_{|m|\le n}(1-|m|/(n+1))\cos m\phi\ge0$, for every $t$,

$$
M(t)=\sum_j\mu_j\Bigl[1+\frac1n-\frac{F_n(\nu_jt)}n\Bigr]
\ \le\ \sum_j\mu_j\min\Bigl\{1+\frac1n,\ \frac{(n+1)(n+2)}{12}(\nu_jt)^2\Bigr\},
\tag{9.2}
$$

where the second bound uses $F_n(\phi)\ge(n+1)-\phi^2n(n+1)(n+2)/12$ and the first uses $F_n\ge0$. At time $T_B=e^{Bz}/J$ the slow levels contribute $o(1)$ and the fast levels at most $(1+1/n)\mu_j$, so $\sup_{t\le T_B}M\le(1+1/n)H(z)+o(1)$. If $z<q_\ell$ then $(1+1/n)H(z)<\ell$ for large $B$, hence $T_\ell>T_B$ and $\liminf B^{-1}\log JT_\ell\ge q_\ell$; the upper bound of Theorem 2(c) closes the limit. $\square$

Rows W15 and W16 exhibit both constructions at finite $B$ for the band measure of Section 4: the odd-multiple spectrum crosses at $\log t_*/B=1.03\,q_{\ell/2}$ with every fast cosine equal to $-1$, and the Fejér-level spectrum satisfies (9.2) pointwise (identity error $<10^{-15}$, $F_n\ge0$ on a grid of $2\times10^5$ points) with its certified first loss above the finite Fejér front, which tends to the time-average front as $n$ grows.

**No-go emission record.** SIGN: the question asked is whether the limiting rate measure determines the exponent; the answer computed is the negative one. QUANTIFIER: universal over measures $\mu$ with the stated regularity, by explicit constructions for each end. SOURCE: the obstruction is external to any single spectrum — it is the freedom of the arithmetic at fixed $\mu$ — and the positive objects (the two families) were actually built. VALUE: the negative result removes the search for a $\mu$-only exponent and points to the alignment capacity as the right invariant.

### 9.3 Exact alignment capacities of integer-ratio spectra — Theorem 9

The two constructions of Theorem 7 are extreme. The physically natural spectra are lacunary: adjacent frequencies of the spin band have ratio $\Delta_{k+1}/\Delta_k\to e^{I'(x)}=(1+2x)/(1-2x)$, which runs from $2$ at the band edge $x=a-b=1/6$ to $5$ at the centre $x=a=1/3$ for the standard band. The following exactly solvable class isolates what an integer ratio does.

Let $q\ge2$ be an integer and let the fast frequencies be exactly geometric, $\Delta_k=q^k\nu_0$, with rate spacing $(\log q)/B$ and weights $\omega_k$ that vary slowly along the rate axis (a Lipschitz density in the rate, sampled on the grid). For $t$ with $\nu_0t/2\pi=x$ the phases are $2\pi q^kx$, so the loss per unit weight along the fast modes is the Birkhoff sum of $f(x)=1-\cos2\pi x$ along the orbit of the expanding map $\tau_q:x\mapsto qx\bmod1$. Define

$$
\beta_q=\sup_{x}\ \limsup_{n}\ \frac1n\sum_{k=0}^{n-1}\bigl(-\cos2\pi\tau_q^kx\bigr)
$$

the maximal ergodic average of $-\cos(2\pi\cdot)$ under $\tau_q$.

**Theorem 9 [PROVEN].** For the exact geometric family, $\kappa=\beta_q$. Under the additional strict-crossing hypothesis (9.1e) at $p_*=\ell/(1+\beta_q)$, the exponent is $q_{p_*}$; otherwise only the two strict threshold bounds are asserted. Moreover:

(i) for odd $q$, $\beta_q=1$: the fixed point $x=\tfrac12$ gives $\cos(q^k\pi)=-1$ for all $k$;

(ii) $\beta_2=\tfrac12$: the period-two orbit $\{\tfrac13,\tfrac23\}$ gives $-\cos=\tfrac12$ at every step, and the exact coboundary identity
$$
\tfrac12+\cos2\pi x+u(2x)-u(x)=\tfrac23\bigl(\cos4\pi x+\tfrac12\bigr)^2\ \ge0,\qquad u(x)=\cos2\pi x+\tfrac13\cos4\pi x,
\tag{9.5}
$$
shows that no orbit does better on average (this is also a special case of Bousch's theorem, which states that the maximising measures of the cosine family under the doubling map are Sturmian);

(iii) $\beta_4=\cos\frac\pi5$: the period-two orbit $\{\tfrac25,\tfrac35\}$ attains it, and with $u(x)=\cos2\pi x+\frac{\sqrt5-1}5\cos4\pi x$ the function $\cos\frac\pi5+\cos2\pi x+u(4x)-u(x)$, written as a quartic in $D=\cos4\pi x$, equals $\frac{8(\sqrt5-1)}5\,(D-\cos\tfrac{2\pi}5)^2\,(D^2+\tfrac{\sqrt5-1}2D+\tfrac{7-\sqrt5}{16})$ with a positive-definite quadratic factor, hence is non-negative;

(iv) for even $q\ge6$, $\beta_q\ge\cos\frac{\pi}{q+1}$: the period-two orbit $\{\frac q{2(q+1)},1-\frac q{2(q+1)}\}$ gives $-\cos=\cos(\pi/(q+1))$ at every step, and no orbit stays inside the open interval $(\frac q{2(q+1)},1-\frac q{2(q+1)})$. The candidate sub-action $u(x)=\cos2\pi x+c_q\cos4\pi x$ with the tangency constant $c_q=q/(4(q+1)\cos\frac\pi{q+1})$ (which reproduces $\tfrac13$ and $\tfrac{\sqrt5-1}5$ for $q=2,4$) is non-negative on a grid of $4\times10^5$ points for every even $q\le40$ (row V25 in v1.1). **A grid minimum is a finite diagnostic and not an all-$x$ certificate**: v1.0 reported this range as VERIFIED equality, which the audit recorded as finding F04, and the row is retyped V accordingly. The equality is not left as a hypothesis, however: Theorem 13 of Section 9.6 proves $\beta_q=\cos\frac\pi{q+1}$ for **every** even $q\ge2$, with a different and explicit sub-action, and also proves that the maximising measure is unique. The two-mode ansatz $u=\cos2\pi x+c_q\cos4\pi x$ is no longer needed for the result and is kept here as the inherited construction; whether it too is non-negative for every even $q$ is not decided in this paper.

*Proof.* Lower bound $\kappa\ge\beta_q$: let $\nu_{k_*}$ be the threshold frequency at time $T_B$ and choose $t_*=2\pi x_*/\nu_{k_*}\le T_B$ with $x_*$ a point of the optimal orbit; every faster mode has phase $2\pi q^{k-k_*}x_*$, so its loss is $1+(-\cos2\pi\tau_q^{k-k_*}x_*)$, whose weighted average over the fast set is $1+\beta_q+o(1)$ because the weights vary slowly. Upper bound $\kappa\le\beta_q$: if $f\le\beta+u\circ\tau_q-u$ for a bounded $u$ (a sub-action; (9.5) and (iii) give explicit ones for $q=2,4$, and for Lipschitz $f$ on an expanding circle map such a $u$ always exists — the Mañé/Bousch revelation lemma), then summing along the orbit with the slowly varying weights and summing by parts,
$$
\sum_k\omega_k\bigl(-\cos2\pi\tau_q^kx\bigr)\le\beta\sum_k\omega_k+2\|u\|_\infty\Bigl(\max_k\omega_k+\sum_k|\omega_{k+1}-\omega_k|\Bigr),
$$
and the correction is $O(1/B)$. The upper bound holds uniformly in $t\le T_B$ and the lower bound is attained by the explicit time, so $\kappa^-=\kappa^+=\beta_q$. Equation (9.1) applies only if the new target mass satisfies (9.1e). The orbit statements are direct: for odd $q$, $q^k/2$ is a half-integer for all $k$; for $q=2$, $2\cdot\tfrac13\equiv\tfrac23$, $2\cdot\tfrac23\equiv\tfrac13$ and $\cos(2\pi/3)=-\tfrac12$; for even $q$, with $a=q/(2(q+1))$, $qa=q/2-a$ and $q/2$ is an integer, so $qa\equiv1-a$, and $-\cos2\pi a=\cos(\pi/(q+1))$. The identity (9.5) is checked by writing $\cos8\pi x=2D^2-1$; the factorisation in (iii) is checked symbolically (row C24). For the interval statement: if $x\in(a,1-a)$ then $x=(d+r)/q$ with $r=\tau_qx\in[0,1)$ and integer $d$; $r\in(a,1-a)$ would force $d\in(qa+a-1,\,q-qa-a)=(q/2-1,q/2)$, which contains no integer. $\square$

Row W17 verifies at $B=192,384$ that the explicit alignment times $t_*=2\pi/(3\nu)$ (for $q=2$), $4\pi/(5\nu)$ ($q=4$) and $\pi/\nu$ ($q=3$) give per-mode losses exactly $\tfrac32$, $1+\cos(\pi/5)$ and $2$ on every faster mode, using exact integer arithmetic for the phases, and that the resulting certified upper bounds on $\log T_\ell/B$ approach the fronts $q_{\ell/(1+\beta_q)}$ from below as $B$ grows.

Theorem 9 is a second, interior, point of the interval realised by admissible spectra: for exact ratio $2$ the exponent is $q_{2\ell/3}$, strictly between the two ends. The value $\beta_q$ is the same kind of constant as the ergodic optimisation of expanding circle maps, and for even $q$ it coincides with the path-eigenvalue constants $\cos(\pi/(P+1))$ that govern the sine optimisers of the reference itself (Appendix S5–S7), with $P=q$.

### 9.4 Riesz–Fejér lower bound for Hadamard-lacunary spectra — Theorem 8

For non-integer ratios the orbit picture is replaced by an estimate. The classical tool is the Riesz product; combined with Fejér's extremal kernels it gives an explicit alignment gain whose constants are again $\cos(\pi/(m+2))$.

For $m\ge1$ let $s_j=\sin\frac{(j+1)\pi}{m+2}$, $j=0,\ldots,m$, and

$$
K_m(\phi)=\frac{\bigl|\sum_{j=0}^ms_je^{ij(\phi+\pi)}\bigr|^2}{\sum_js_j^2}=1+\sum_{k=1}^ma_k\cos k\phi,\qquad a_1=-2\cos\frac\pi{m+2}.
\tag{9.3}
$$

$K_m\ge0$, its mean is $1$, and $|a_1|=2\cos(\pi/(m+2))$ is the largest first coefficient of any non-negative cosine polynomial of degree $m$ with constant term $1$ (Fejér). Explicitly $K_1(\phi)=1-\cos\phi$ and $K_2(\phi)=1-\sqrt2\cos\phi+\tfrac12\cos2\phi$; row C18 checks non-negativity, unit mean and $a_1$ symbolically for $m=1,2,3$.

**Theorem 8 [PROVEN].** Let $D=\{\nu_1<\cdots<\nu_n\}$ be positive frequencies with $\nu_{i+1}/\nu_i\ge2m+1$, weights $\omega_i>0$, and $T>0$ with $N=\nu_1T$. Then

$$
\sup_{0\le t\le T}\ \sum_{i\in D}\omega_i\bigl(1-\cos\nu_it\bigr)\ \ge\ \frac{(1+\cos\frac\pi{m+2})(1-c_m/N)}{1+c_m/N}\sum_{i\in D}\omega_i ,
\tag{9.4}
$$

with the explicit constant $c_m=8(m+1)(2m+1)/m$. In a family as in Theorem 2(c) whose fast modes with margin $\eta$ satisfy the ratio condition, $\kappa^-(z)\ge\cos(\pi/(m+2))$; if all modes do, the exponent lies in $[q_{\ell/2},\,q_{\ell/(1+\cos(\pi/(m+2)))}]$.

*Proof [rewritten in v1.1].* The quantity that controls a product of kernels is not the value $K_m(0)$ but the $\ell^1$ mass of its Fourier coefficients. Write $t_j=(-1)^js_j$, so that $K_m(\phi)=\bigl|\sum_jt_je^{ij\phi}\bigr|^2/\sum_jt_j^2=\sum_{|k|\le m}\widehat K_k e^{ik\phi}$ with $\widehat K_k=\sum_jt_jt_{j+|k|}/\sum_jt_j^2$ and $2\widehat K_1=a_1=-2\cos\frac\pi{m+2}$. Then

$$
L:=\|\widehat K\|_1=\sum_{|k|\le m}|\widehat K_k|=\frac{\bigl(\sum_{j=0}^ms_j\bigr)^2}{\sum_{j=0}^ms_j^2}\ \le\ m+1 ,
\tag{9.4a}
$$

the equality because $|t_j|=s_j$ and every $\sum_jt_jt_{j+|k|}$ has the sign $(-1)^k$, the inequality by Cauchy–Schwarz. The v1.0 proof used $K_m(0)^{i^*}$ in this place, which bounds nothing: $K_1(\phi)=1-\cos\phi$ has $K_1(0)=0$ and $L=2$ (row C31). The audit of v1.0 recorded this as finding F03; the constant $c_m$ printed in (9.4) is nevertheless recovered in full by the following count.

Put $R=2m+1$, $c=\cos\frac\pi{m+2}$, $N=\nu_1T$ and $P(t)=\prod_{i\in D}K_m(\nu_it)\ge0$, and write $\langle g\rangle=T^{-1}\int_0^Tg$. Expanding $P$ gives $1$ plus terms $\widehat c_{\mathbf k}e^{i\Omega t}$, $\Omega=\sum_ik_i\nu_i$, $|k_i|\le m$, not all $k_i$ zero. Group the terms by the largest index $r$ with $k_r\ne0$. The absolute coefficient mass of the group is at most $L^r$, and

$$
|\Omega|\ \ge\ \nu_r-m\sum_{i<r}\nu_i\ \ge\ \nu_r\Bigl(1-\frac m{R-1}\Bigr)=\frac{\nu_r}2 ,
$$

because $\sum_{i<r}\nu_i\le\nu_r\sum_{a\ge1}R^{-a}=\nu_r/(R-1)$ and $m/(R-1)=\tfrac12$. The time averages are taken **after pairing each term with its conjugate**: $P$ is real and even in $t$, so the terms $\Omega$ and $-\Omega$ carry the same real coefficient $c$, and the pair contributes $2c\langle\cos\Omega t\rangle=2c\,\sin(\Omega T)/(\Omega T)$, of modulus at most $2|c|/(|\Omega|T)$, i.e. *(absolute mass of the pair)*$\times1/(|\Omega|T)$. The unpaired bound $|\langle e^{i\Omega t}\rangle|\le1/(|\Omega|T)$ would be false — the sharp value is $2|\sin(\Omega T/2)|/(|\Omega|T)$, which equals $2/\pi$ at $\Omega T=\pi$ against $1/\pi$ — so the pairing is what makes the mass bookkeeping below correct. With $\nu_r\ge R^{r-1}\nu_1$,

$$
E_0:=|\langle P\rangle-1|\ \le\ \frac2N\sum_{r\ge1}\frac{(m+1)^r}{R^{r-1}}=\frac{2(m+1)R}{mN}=\frac{c_m}{4N} .
\tag{9.4b}
$$

For a fixed $j$ combine the $j$-th kernel with the cosine before expanding: $K_m(\phi)\cos\phi$ has $\ell^1$ mass at most $L$, constant term $\widehat K_1=-c$, and degree $m+1$ instead of $m$. There is no other constant resonance, because for a group whose largest index is $r>j$

$$
|\Omega|\ \ge\ \nu_r-m\sum_{i<r}\nu_i-\nu_j\ \ge\ \nu_r\Bigl(\frac12-\frac1R\Bigr)=\sigma\nu_r,\qquad \sigma=\frac{2m-1}{2R}>0 ,
$$

and for $r\le j$ the margin is larger. Hence for every $j$

$$
E_1:=\bigl|\langle P\cos\nu_jt\rangle+c\bigr|\ \le\ \frac{(m+1)R}{\sigma mN}=\frac{2(m+1)R^2}{m(2m-1)N}\ \le\ \frac{3c_m}{4N},
\tag{9.4c}
$$

the last step being $1-\tfrac14-\frac R{4(2m-1)}=\frac{m-1}{2m-1}\ge0$ for every integer $m\ge1$ (row C32 checks this algebra, row C31 the mass identity). Therefore

$$
\langle P\,M_D\rangle=\sum_j\omega_j\bigl(\langle P\rangle-\langle P\cos\nu_jt\rangle\bigr)\ \ge\ \Bigl[(1+c)-\frac{c_m}N\Bigr]\sum_j\omega_j\ \ge\ (1+c)\Bigl(1-\frac{c_m}N\Bigr)\sum_j\omega_j .
$$

If $N\le c_m$ the right-hand side of (9.4) is non-positive and the claim is trivial because $M_D\ge0$; otherwise $\langle P\rangle\ge1-c_m/(4N)>0$, so the positive weight $P$ may be normalised, and $\sup_{t\le T}M_D\ge\langle PM_D\rangle/\langle P\rangle\ge(1+c)(1-c_m/N)/(1+c_m/N)\sum_j\omega_j$, which is (9.4). For the family statement, apply this to $\mathcal F_B(z,\eta)$, for which $N\ge e^{B\eta}$; the modes outside $D$ contribute non-negative loss at the maximising time. $\square$

Row V19 checks (9.4) on random Hadamard sets with ratios in $[3,4.5]$ ($m=1$) and $[5,6.5]$ ($m=2$): $\langle RM\rangle/\langle R\rangle$ equals $(1+\cos(\pi/(m+2)))\sum\omega$ to four digits and the scanned supremum dominates it.

For the spin band the adjacent ratio profile is $q(x)=(1+2x)/(1-2x)$. The standard band $(a,b)=(\tfrac13,\tfrac16)$ has $q\in[2,5]$, so Theorem 8 does not apply to its edge modes, which are the fast ones. The band $(a,b)=(\tfrac5{12},\tfrac1{12})$ has $x\in[\tfrac13,\tfrac5{12}]$ and $q\in[5,11]$; row V20 confirms adjacent finite-$B$ ratios above $5$ at $B=96,192,288$, so $m=2$ applies and its exponent lies in $[q_{\ell/2},q_{\ell/(1+\cos(\pi/4))}]$, a front of $0.586\,\ell$ instead of $\ell$. The standard band is reached in Section 9.7 by a different bound (Theorem 14), which needs no integer or Hadamard ratio and applies at every ratio $\rho>1$. Its certified finite-size first losses sit at fractional log-positions $\theta\in[0.05,0.26]$ between the finite envelopes, close to the full-alignment end, as a strongly lacunary spectrum should.

### 9.5 The physical band: finite-size brackets and the remaining conjecture

For the standard band the exact frequencies $\Delta_k=c_B(\widetilde\lambda_{k+1}-\widetilde\lambda_k)$ were computed to 85 digits by Sturm bisection and the exact finite cosine sum was scanned on a grid fine enough for the Lipschitz certificate $|M'|\le\sum_k\omega_k|\Delta_k|$; row V14 records a bracket $[T_{\rm safe},T_{\rm hit}]$ containing $T_\ell$ (loss below $\ell$ on $[0,T_{\rm safe}]$ by the Lipschitz bound, loss at least $\ell$ at $T_{\rm hit}$) for $B=48,\ldots,288$.

**What that bracket certifies, exactly (finding F09).** The Lipschitz inequality is valid for the exact cosine sum, and the sector energies are computed by Sturm bisection at $85$ digits; but the subsequent gap differences, the weights and the cosine evaluations are carried in double precision and their round-off is *not* propagated into the inequality. The bracket is therefore a high-precision numerical bracket, not an outward-rounded interval certificate of the exact finite matrix, and v1.1 types row V14 and its companions as V, not as exact certificates. To claim a rigorous finite-time enclosure one must wrap every $\nu_i$ and $w_i$ in outward intervals, propagate them through (9.10) and enclose the cosines; that work is listed as an obligation in Section 14 and is not done here. With $\theta=(\log T_{\rm hit}-\log t_A)/(\log t_B-\log t_A)$ the position between the finite envelopes of Theorem 2(a):

| $B$ | $\ell$ | $\log(JT_{\rm hit})/B$ | finite envelopes $\log/B$ | $\theta$ | modes past half period | loss / $2\times$mass of those modes |
|---:|---:|---:|---|---:|---:|---:|
| 48 | 0.02 | 0.16339 | 0.15664 – 0.17447 | 0.378 | 0 | — |
| 48 | 0.1 | 0.17783 | 0.17599 – 0.20195 | 0.071 | 2 | 1.000 |
| 48 | 0.3 | 0.20916 | 0.19725 – 0.23915 | 0.284 | 6 | 0.714 |
| 96 | 0.02 | 0.12503 | 0.12141 – 0.13410 | 0.285 | 2 | 0.500 |
| 96 | 0.1 | 0.14426 | 0.14021 – 0.16064 | 0.198 | 8 | 0.788 |
| 96 | 0.3 | 0.17046 | 0.16362 – 0.19671 | 0.207 | 14 | 0.828 |
| 144 | 0.02 | 0.11179 | 0.10893 – 0.11983 | 0.262 | 6 | 0.771 |
| 144 | 0.1 | 0.13341 | 0.12763 – 0.14637 | 0.309 | 14 | 0.711 |
| 144 | 0.3 | 0.15749 | 0.15245 – 0.18248 | 0.168 | 22 | 0.852 |
| 192 | 0.02 | 0.10534 | 0.10209 – 0.11247 | 0.313 | 10 | 0.657 |
| 192 | 0.1 | 0.12715 | 0.12163 – 0.13933 | 0.312 | 20 | 0.724 |
| 192 | 0.3 | 0.15123 | 0.14631 – 0.17534 | 0.170 | 28 | 0.817 |
| 240 | 0.02 | 0.10224 | 0.09829 – 0.10796 | 0.409 | 14 | 0.592 |
| 240 | 0.1 | 0.12356 | 0.11727 – 0.13474 | 0.360 | 26 | 0.709 |
| 240 | 0.3 | 0.14741 | 0.14147 – 0.17105 | 0.201 | 36 | 0.825 |
| 288 | 0.02 | 0.09779 | 0.09538 – 0.10490 | 0.254 | 16 | 0.757 |
| 288 | 0.1 | 0.11853 | 0.11501 – 0.13137 | 0.215 | 30 | 0.815 |


Two facts are stable across sizes: the first loss occurs strictly inside the finite interval, at $\theta$ between about $0.07$ and $0.41$ (between $0.17$ and $0.36$ for $B\ge96$ at $\ell=0.1,0.3$), and the modes that have completed at least half a period have lost $70$–$85\%$ of their maximum $2\omega$, well above the $50\%$ of the time average. The band therefore aligns its fast phases partially, as the Hadamard picture predicts for ratios that drift from $2$ to $5$; neither end of the interval is approached at these sizes. The finite-size exponents also carry a polynomial prefactor: the gaps behave as $\Delta\sim Jx^2B^{-1/2}e^{-BI(x)}$, so $\log(JT_\ell)=Bz+\tfrac12\log B+O(1)$ is the expected finite-size form, and the slow drift of the tabulated $\log(JT_{\rm hit})/B$ is consistent with it.

**Conjecture 9.2 [v1.0 form; the identification is RETRACTED in v1.1].** The v1.0 statement read: *for the spin band under (3.11) the alignment capacity $\kappa(z)$ exists, is continuous, and lies strictly between $0$ and $1$; it is the value of the non-autonomous ergodic optimisation problem for the chain of maps $x\mapsto q_kx\bmod1$ with $q_k\to(1+2x_k)/(1-2x_k)$, weighted by the band density.* The last clause is false as an identification of the phase dynamics and is withdrawn; the rest is decomposed below into four separate statements, of which one is now proved.

**Why the reduced torus map is the wrong object (finding F05).** Write the actual phase of mode $k$ at time $t$ as $\theta_k=\nu_kt/2\pi=n_k+x_k$ with $n_k\in\mathbb Z$ and $x_k\in[0,1)$. Then

$$
x_{k+1}=\{q_k x_k+q_kn_k\},\qquad q_k=\nu_{k+1}/\nu_k ,
\tag{9.6}
$$

and for non-integer $q_k$ the term $q_kn_k$ cannot be dropped: the winding number $n_k$, which the reduction to $[0,1)$ throws away, changes the next phase. The map $x\mapsto\{qx\}$ on representatives is a perfectly good function, but it is not the phase dynamics and it is not even well defined on $\mathbb R/\mathbb Z$ for non-integer $q$. An exact counterexample (row C30): for $q=\tfrac52$ and $x=\tfrac34$,

$$
\{q^2x\}=\tfrac{11}{16},\qquad \{q\{qx\}\}=\tfrac3{16},
\tag{9.7}
$$

a difference of exactly $\tfrac12$, so the two prescriptions give cosines of opposite sign. Integer ratios are exactly the case in which the dropped term is an integer, which is why Theorem 9 is a theorem and its extension to real ratios was not.

**Replacement objects.** The correct chain keeps the winding,

$$
(n,x)\ \longmapsto\ \bigl(\lfloor q_k(n+x)\rfloor,\ \{q_k(n+x)\}\bigr),
\tag{9.8}
$$

and the object the first-loss time actually asks about is the finite-horizon phase curve

$$
\Theta_B(t)=\frac t{2\pi}\bigl(\Delta_{B,1},\ldots,\Delta_{B,n_B}\bigr)\bmod\mathbb Z^{n_B},\qquad 0\le t\le e^{Bz}/J .
\tag{9.9}
$$

Density of the closure of an infinite orbit is not enough: the question is how well the curve approximates the optimal phase configuration *within* the finite horizon, in a dimension that grows linearly in $B$. Two quantitative warnings apply, and both are sharp enough to kill the natural shortcuts.

*(i) Approximate frequencies may not be substituted.* For non-negative weights,

$$
\sup_{0\le t\le T}\bigl|M_{\nu,w}(t)-M_{\widehat\nu,\widehat w}(t)\bigr|\ \le\ 2\sum_i|w_i-\widehat w_i|+T\sum_i\widehat w_i\,|\nu_i-\widehat\nu_i| ,
\tag{9.10}
$$

by $|\cos\alpha-\cos\beta|\le|\alpha-\beta|$ termwise. At $T=e^{Bz}/J$ a relative frequency error of order $B^{-1}$ — the accuracy at which Section 3.3 controls the gaps — is multiplied by $e^{Bz}$ and is useless. Controlling ratios and rates to $O(B^{-1})$ is enough for the *inequalities* of Theorems 1–2 and 14 and not enough to transport a phase *optimum*.

*(ii) The limiting ratio profile does not determine the alignment.* Let $J=1$ and take $\nu_{B,k}=e^{-Bz_0}2^k$ for $-\lfloor cB\rfloor\le k\le\lfloor cB\rfloor$ with equal weights; the rate measure is uniform around the interior point $z_0$ and every adjacent ratio equals $2$. Now leave $k<\lceil\sqrt B\rceil$ unchanged and replace the rest by

$$
\widehat\nu_{B,k}=\pi e^{-Bz_0}(2m_k+1),\qquad m_k\in\mathbb Z_{\ge0}\ \text{nearest to}\ \frac{2^k}{2\pi}-\frac12 .
\tag{9.11}
$$

The relative change is at most $\pi2^{-k}$, so all adjacent ratios still converge to $2$ uniformly and the rate measure is unchanged; but at $t_*=e^{Bz_0}$ every modified phase is an odd multiple of $\pi$, so $\widehat\kappa(z_0)=1$, whereas the exact dyadic family has $\kappa(z_0)=\beta_2=\tfrac12$ by Theorem 9. Row C30 and the odd-multiple witness of row W15 exhibit the mechanism. Hence no theorem whose hypotheses are "the rate measure, the weights, and the limiting adjacent-ratio profile" can compute $\kappa$; the arithmetic of the actual frequencies enters.

**Conjecture 9.2 [v1.1 form, decomposed].** For the spin band under (3.11), at every interior rate $z$:

(a) *(existence)* $\kappa^-(z)=\kappa^+(z)$;
(b) *(strict interiority from below)* $\kappa^-(z)>0$ — **PROVEN** in Section 9.7, with the explicit value $\kappa^-(z)\ge\tfrac14$ for the standard band;
(c) *(strict interiority from above)* $\kappa^+(z)<1$;
(d) *(continuity and a single exponent)* $z\mapsto\kappa(z)$ is continuous and $Q(z)=(1+\kappa(z))H(z)$ has a unique **strict crossing** $Q(z_*)=\ell$ (here $H_-=H$). The asserted exponent would then be $z_*$. A constant-\kappa quantile notation must not be substituted for this variable-\kappa equation.

Only (b) is settled. A sufficient route to (a) and (d) that makes the hidden hypotheses explicit is to prove that

$$
Q_B(z)=\sup_{0\le t\le e^{Bz}/J}M_B(t)
\tag{9.12}
$$

converges to a continuous limit $Q$ with a unique strict crossing $Q(z_*)=\ell$; then $B^{-1}\log JT_\ell\to z_*$. Stating this is not solving it.

Falsifier: a scan at larger $B$ in which $\theta$ tends to $0$ or to $1$ *with a controlled subsequence and a residual bound*, or a sequence in which $(\log JT_\ell)/B$ leaves the interior of $[q_{\ell/2},q_{4\ell/5}]$, refutes the corresponding part; a sub-action for the windowed chain (9.8), or a quantitative obstruction preventing all fast phases of positive mass from approaching $\pi$ simultaneously, would settle (c). Six or seven finite sizes moving in one direction are not a refutation, and v1.0's reading of the $\theta$ column as evidence about the limit was recorded by the audit as finding F10; the table above is a finite diagnostic and is labelled as one. The exact exponent of the physical band remains OPEN; what is no longer open is what determines it, that it is not determined by $\mu$ and the ratio profile, and that it is bounded away from the upper end.

### 9.6 The alignment cap of every integer ratio — Theorem 13

Theorem 9 computed $\beta_q$ for odd $q$ and for $q=2,4$, and left even $q\ge6$ as a grid observation. The following theorem closes the even case for all $q$ at once, with a sub-action that is not a trigonometric polynomial but a tent.

Let $T_qx=qx\bmod1$ on $\mathbb R/\mathbb Z$, let $f(x)=-\cos2\pi x$, and let

$$
d(x)=2\pi\Bigl|\{x\}-\tfrac12\Bigr|\in[0,\pi]
\tag{9.13}
$$

be the angular distance from the point $e^{2\pi ix}$ to $-1$, so that $\cos2\pi x=-\cos d(x)$. For an even integer $q\ge2$ set

$$
a=\frac\pi{q+1},\qquad \beta=\cos a,\qquad u_q(x)=\frac{\sin a}{q+1}\,d(x) .
\tag{9.14}
$$

**Theorem 13 [PROVEN; new in v1.1].** For every even integer $q\ge2$ and every $x$,

$$
\boxed{\ \beta+\cos2\pi x+u_q(T_qx)-u_q(x)\ \ge\ 0\ }
\tag{9.15}
$$

with equality exactly on the two-cycle $\{p,1-p\}$, $p=\frac q{2(q+1)}$. Consequently

$$
\boxed{\ \beta_q=\cos\frac\pi{q+1}\quad\text{for every even }q\ge2,\qquad \beta_q=1\quad\text{for every odd }q,\ }
\tag{9.16}
$$

for even $q$ the maximising measure is unique and is the uniform measure on that two-cycle. In the setting of Theorem 9, $\kappa^-=\kappa^+=\beta_q$; the first-loss exponent is $q_{\ell/(1+\beta_q)}$ only under (9.1e).

*Proof.* Since $q$ is even, $T_q(\tfrac12)=0$, whose distance to $\tfrac12$ is $\pi$. The map $T_q$ is $q$-Lipschitz for the circle metric, so $\operatorname{dist}(T_qx,0)\le q\,d(x)$ and therefore

$$
d(T_qx)\ \ge\ \pi-q\,d(x),\qquad\text{i.e.}\qquad q\,d(x)+d(T_qx)-\pi\ \ge\ 0 .
\tag{9.17}
$$

This is the only step that uses the parity of $q$. Writing $d=d(x)$, $d'=d(T_qx)$ and using $\cos2\pi x=-\cos d$ and $(q+1)a=\pi$, the left-hand side of (9.15) is **identically**

$$
\underbrace{\bigl[\cos a-\cos d-\sin a\,(d-a)\bigr]}_{g(d)}\ +\ \frac{\sin a}{q+1}\bigl[q\,d+d'-\pi\bigr] ,
\tag{9.18}
$$

as one checks by collecting the terms linear in $d$: $-\sin a\,d+\frac{q\sin a}{q+1}d=-\frac{\sin a}{q+1}d$, and $\sin a\,(a-\frac\pi{q+1})=0$ (row C26 checks the identity symbolically in $q=2n$). The bracket in (9.18) is non-negative by (9.17), so (9.15) holds wherever $g\ge0$; and using only $d'\ge0$ in (9.18) gives the second lower bound

$$
G(d)=\cos a-\cos d-\frac{\sin a}{q+1}\,d ,
\tag{9.19}
$$

after the same cancellation. It therefore suffices to show $g\ge0$ on $[0,\pi-a]$ and $G\ge0$ on $[\pi/q,\pi]$, because $\pi/q\le\pi-a$ for $q\ge2$ (this is $q+1\le q^2$) so the two intervals cover $[0,\pi]$.

*$g\ge0$ on $[0,\pi-a]$.* $g'(d)=\sin d-\sin a$ vanishes at $d=a$ and $d=\pi-a$, is negative on $[0,a)$ and positive on $(a,\pi-a)$; $g(a)=0$ and $g(0)=\cos a-1+a\sin a>0$ for $0<a\le\pi/3$. Hence $g\ge0$ there, with equality only at $d=a$.

*$G\ge0$ on $[\pi/q,\pi]$.* $G'(d)=\sin d-\frac{\sin a}{q+1}$ vanishes on $[0,\pi]$ exactly at $d_1=\arcsin\frac{\sin a}{q+1}$ and at $\pi-d_1$, is negative on $[0,d_1)$, positive on $(d_1,\pi-d_1)$ and negative on $(\pi-d_1,\pi]$. The left critical point lies **outside** the interval: using $\arcsin y\le\frac\pi2y$ and $\sin a\le a=\frac\pi{q+1}$,

$$
d_1\ \le\ \frac\pi2\cdot\frac{\sin a}{q+1}\ \le\ \frac{\pi^2}{2(q+1)^2}\ <\ \frac\pi q ,
$$

the last step because $\pi q<2(q+1)^2$ for every $q\ge2$. Hence on $[\pi/q,\pi]$ the only interior critical point is the maximum at $\pi-d_1$, and $G$ attains its minimum at one of the two endpoints. At the right endpoint, using $\pi/(q+1)=a$,

$$
G(\pi)=1+\cos a-a\sin a\ \ge\ 1+\cos\tfrac\pi3-\tfrac\pi3\sin\tfrac\pi3>0 ,
$$

because $a\mapsto1+\cos a-a\sin a$ has derivative $-2\sin a-a\cos a<0$ and $a\le\pi/3$. At the left endpoint put $\delta=\pi/q-a=\pi/(q(q+1))=a/q$, so that $\frac{\sin a}{q+1}\cdot\frac\pi q=\delta\sin a$ and

$$
G(\pi/q)=\cos a-\cos(a+\delta)-\delta\sin a=:\varphi(\delta),\qquad
\varphi(0)=0,\quad \varphi'(\delta)=\sin(a+\delta)-\sin a\ \ge0
$$

for $0\le\delta$ with $a+\delta=\pi/q\le\pi/2$, which holds for every $q\ge2$. Hence $\varphi(\delta)>0$ for $\delta>0$ and $G(\pi/q)>0$. This proves (9.15).

*Equality and uniqueness.* Summing (9.15) along an orbit telescopes the coboundary, so $\frac1n\sum_{k<n}f(T_q^kx)\le\beta+2\|u_q\|_\infty/n$ for every $x$ and every $n$, whence $\beta_q\le\beta$. The two-cycle attains it: $qp=\frac{q^2}{2(q+1)}$ and $qp-(1-p)=\frac{q-2}2\in\mathbb Z$ for even $q$, so $T_qp=1-p$ and $T_q(1-p)=p$, while $2\pi p=\pi-a$ gives $f(p)=f(1-p)=\cos a=\beta$. If $\mu$ is invariant with $\int f\,d\mu=\beta$ then the integral of the left side of (9.15) vanishes, so the left side vanishes $\mu$-a.e.; it is strictly positive whenever $d(x)\ne a$ (on $[0,\pi-a]$ because $g>0$ off $d=a$, and on $(\pi-a,\pi]$ because $G>0$ there), so $\mu$ is supported on $\{d=a\}=\{p,1-p\}$ and invariance forces equal masses. For odd $q$, $T_q(\tfrac12)=\tfrac12$ and $f(\tfrac12)=1$, which is the trivial maximum. $\square$

Rows C26 and V27 carry the symbolic identity (9.18), the tangent derivative, the two-cycle relations, and the positivity of $g(0)$, $\varphi(\delta)$ and $G(\pi)$ at $60$ digits up to $q=10^6$; row V28 enumerates every periodic orbit of $T_q$ up to period $18$ (for $q=2$) and finds no Birkhoff average above $\beta_q$, with the two-cycle attaining it. None of these rows proves (9.15); the proof is the four displayed inequalities.

Three remarks fix the scope. First, (9.16) is a statement about *exactly* geometric spectra with integer ratio; Section 9.7 shows that a family whose ratios merely converge to $q$ can have a different alignment. Second, the value $\cos\frac\pi{q+1}$ is the same constant that governs the sine optimisers of the reference itself (Appendix S5–S7 with $P=q$) and the Fejér kernels of Theorem 8 with $m+2=q+1$; the coincidence is not used as evidence for anything. Third, for $q=2$ the result is a special case of Bousch's theorem on Sturmian maximising measures for the cosine family under the doubling map, so the new content is the uniform treatment of all even $q$ by one explicit Lipschitz sub-action, and the uniqueness statement; the closest-primary-source comparison and its limits are recorded in Section 12.4. No global priority claim is made.

### 9.7 A lower bound on alignment for real frequencies — Theorems 14 and 15

Theorem 8 needs Hadamard ratio $2m+1\ge3$ and gives nothing at ratio $2$, which is exactly where the fast edge of the standard band sits. The following lemma removes the integrality and the size of the ratio at once: it sparsifies the frequency set until the surviving ratios are large, and pays only a factor $2L$ in the gain.

Let $0<\nu_1<\cdots<\nu_n$ with $\nu_{i+1}/\nu_i\ge\rho>1$, let $w_i>0$, $\Gamma=\sum_iw_i$, $N=\nu_1T$. Choose an integer $L\ge1$ with

$$
R=\rho^L>3,\qquad \delta=1-\rho^{-1}-(R-1)^{-1}>0 ,
\tag{9.20}
$$

and set $\sigma=1-(R-1)^{-1}$, $\sigma_2=1-(R-1)^{-1}-R^{-1}$,

$$
C_0=\frac1{\sigma(1-2/R)},\qquad
C_1=\max\Bigl\{1+\frac1{\delta(1-2/R)},\ \frac2{\sigma_2(1-2/R)}\Bigr\} .
\tag{9.21}
$$

**Theorem 14 [PROVEN; new in v1.1].** With these hypotheses,

$$
\boxed{\ \frac1\Gamma\sup_{0\le t\le T}\sum_iw_i\bigl(1-\cos\nu_it\bigr)\ \ge\ \Bigl[\frac{1+\frac1{2L}-(C_0+C_1)/N}{1+C_0/N}\Bigr]_+ .\ }
\tag{9.22}
$$

No integrality, no slow variation of the weights and no upper bound on $n$ is assumed.

*Proof.* Split $\{1,\ldots,n\}$ into the $L$ residue classes mod $L$ and let $S$ be the class of largest weight, $W_S\ge\Gamma/L$; its frequencies $\lambda_1<\cdots<\lambda_s$ satisfy $\lambda_{r+1}/\lambda_r\ge R$. Use the Riesz product

$$
P(t)=\prod_{r=1}^s\bigl(1-\cos\lambda_rt\bigr)\ \ge\ 0 ,
\tag{9.23}
$$

whose factors have complex Fourier coefficients $(-\tfrac12,1,-\tfrac12)$ and absolute mass $2$. Expanding and grouping by the largest active index $r$, the group has absolute mass at most $2^{r-1}$ and frequency of modulus at least $\lambda_r-\sum_{a<r}\lambda_a\ge\sigma\lambda_r$. As in the proof of Theorem 8, each term is paired with its conjugate before averaging, which is legitimate because $P$ is real and even, and gives *(absolute mass)*$\times1/(|\Omega|T)$ per pair. Hence with $\lambda_r\ge R^{r-1}\nu_1$,

$$
|\langle P\rangle-1|\ \le\ \sum_{r\ge1}\frac{2^{r-1}}{\sigma\lambda_rT}\ \le\ \frac{C_0}N .
\tag{9.24}
$$

For $j\notin S$, every non-constant frequency $\Omega$ of $P$ satisfies $|\Omega\pm\nu_j|\ge\delta\max(\lambda_r,\nu_j)$, where $\lambda_r$ is the largest active selected frequency: if $\lambda_r>\nu_j$ use $\nu_j\le\lambda_r/\rho$ and $\sum_{a<r}\lambda_a\le\lambda_r/(R-1)$; if $\lambda_r<\nu_j$ use $\lambda_r\le\nu_j/\rho$ and $\sum_{a\le r}\lambda_a\le R\lambda_r/(R-1)$. Counting the constant term of $P$ separately,

$$
\bigl|\langle P\cos\nu_jt\rangle\bigr|\ \le\ \frac1N+\sum_{r\ge1}\frac{2^{r-1}}{\delta\lambda_rT}\ \le\ \frac{C_1}N .
\tag{9.25}
$$

For $j\in S$, say $\nu_j=\lambda_A$, combine that factor with the cosine first, using

$$
(1-\cos\phi)\cos\phi=-\tfrac12+\cos\phi-\tfrac12\cos2\phi ,
$$

whose absolute mass is again $2$ and whose constant term is $-\tfrac12$; the one extra harmonic is controlled by $\lambda_A\le\lambda_r/R$ for the groups with largest index $r>A$, leaving a margin $\sigma_2\lambda_r$, and the groups with $r\le A$ have a larger margin. Hence

$$
\bigl|\langle P\cos\lambda_At\rangle+\tfrac12\bigr|\ \le\ \sum_{r\ge1}\frac{2^r}{\sigma_2\lambda_rT}\ \le\ \frac{C_1}N .
\tag{9.26}
$$

In particular the three margins show that no hidden constant resonance exists. Therefore $\langle PM\rangle\ge\Gamma+\tfrac12W_S-\Gamma(C_0+C_1)/N$, and dividing by $\langle P\rangle\le1+C_0/N$ and using $\sup M\ge\langle PM\rangle/\langle P\rangle$ and $W_S\ge\Gamma/L$ gives (9.22); when the numerator is negative the bound is trivial because $M\ge0$. $\square$

Row V33 evaluates the exact Fourier form of (9.24)–(9.26) on random real lacunary sets and on an actual finite spin band, and finds every measured margin inside its budget.

**Theorem 15 [PROVEN; new in v1.1].** Consider the standard band $(a,b)=(\tfrac13,\tfrac16)$ of Section 4 and a rate $z$ interior to the support of $\mu$. Then

$$
\boxed{\ \kappa^-(z)\ \ge\ \tfrac14\ }\qquad\text{and}\qquad
\boxed{\ q_{\ell/2}\ \le\ \liminf_B\frac{\log JT_\ell}B\ \le\ \limsup_B\frac{\log JT_\ell}B\ \le\ q_{4\ell/5}\ <\ q_\ell\ }
\tag{9.27}
$$

for every fixed $0<\ell<\tfrac12$.

*Proof.* Fix $\eta>0$ and consider the fast set $\mathcal F_B(z,\eta)$. Its modes are the band positions with $I(x_k)\le z-\eta$, i.e. $x_k=j/B-|k|/B$ below a value $x(z-\eta)<a$; since $z$ is interior, the fast set is at a positive distance from the band centre $k=0$, where the two boundary contributions are equal. The frequencies come in exactly degenerate pairs: $E_k=E_{-k}$ gives $\Delta_{-k-1}=-\Delta_k$, so the pair is $(k,-k-1)$ — not $(k,-k)$ — and merging it into a single positive frequency with the summed weight is an identity, not an approximation, because $1-\cos$ is even. Off the centre the nearer boundary dominates the far one exponentially, so the exact adjacent ratio (3.14) of the boundary term, together with the uniform relative $O(B^{-1})$ of (3.8) and the non-degeneracy of the leading difference (3.15), gives

$$
\frac{\Delta_{k+1}}{\Delta_k}=r_k\bigl(1+o(1)\bigr),\qquad r_k\longrightarrow e^{I'(x_k)}=\frac{1+2x_k}{1-2x_k}\ \ge\ 2
\tag{9.28}
$$

uniformly on the fast set, the value $2$ being attained only in the limit at the band edge $x=b=\tfrac16$. The relative error is written $o(1)$ and not $O(B^{-1})$ on purpose: (3.13) controls only $B^{-1}\log|\Delta_k|$, which is far too weak for a ratio, and the finite data of row V34 — the deviation $2-\min_kr_k$ equal to $0.153$, $0.112$, $0.052$ at $B=48,96,192$ — do not identify the rate at the edge, which is precisely where the two-boundary split of Section 3.3 is most delicate. Only $o(1)$ is used below. Hence for every $\rho<2$ there is $B_0(\rho,\eta)$ beyond which all adjacent ratios of the fast set exceed $\rho$. Take $\rho=\tfrac{19}{10}$ and $L=2$: then $R=\tfrac{361}{100}>3$, $\delta=\tfrac{449}{4959}>0$, $C_0=3.63492\ldots$, $C_1=25.76447\ldots$, and $N\ge e^{B\eta}\to\infty$, so the bracket in (9.22) tends to $1+\tfrac1{2L}=\tfrac54$. Thus $\kappa^-(z)\ge\tfrac14$ for every interior $z$. The rate measure of the band is the image of the continuous density (4.6) under $s\mapsto I(a-|s|)$, so it has no atom and $H_-=H$ throughout; Proposition 9.1 in the form (9.1a$'$) therefore gives $\limsup_BB^{-1}\log JT_\ell\le\inf\{z:\tfrac54H(z)>\ell\}=q_{4\ell/5}$. $\square$

Row V34 records the measured minimum adjacent ratio of the standard band, $1.847$, $1.888$, $1.948$ at $B=48,96,192$, increasing towards $2$: the hypothesis $\rho=1.9$ holds from a finite size on and not at every $B$, exactly as the proof states. The improvement is a genuine narrowing of the interval of Theorem 2:

| loss $\ell$ | lower front $q_{\ell/2}$ | new upper front $q_{4\ell/5}$ | v1.0 upper front $q_\ell$ |
|---|---:|---:|---:|
| 0.02 | 0.0799740047 | **0.0844296661** | 0.0868687047 |
| 0.1 | 0.0997698874 | **0.1088145336** | 0.1138937854 |
| 0.3 | 0.1247705320 | **0.1408748399** | 0.1502873475 |

The same argument applies to any band with $a>b>0$: the limiting minimum ratio is $(1+2(a-b))/(1-2(a-b))>1$, so some $\rho>1$ and some $L$ satisfy (9.20) and give $\kappa^-\ge1/(2L)>0$ with upper front $q_{\ell/(1+1/(2L))}$. The endpoint band $a=b$ of Theorem 11 is not covered by one uniform $\rho$, because its weights and ratios degenerate at the centre.

A further, computable route to better lower bounds keeps the actual real frequencies. Writing the selected Riesz product as $P(t)=\sum_h c_he^{it\,h\cdot\nu}\ge0$ and using $\operatorname{sinc}(y)=\sin y/y$,

$$
A_0=\sum_hc_h\operatorname{sinc}(T\,h\cdot\nu),\qquad
A_j=\tfrac12\sum_hc_h\bigl[\operatorname{sinc}(T(h\cdot\nu+\nu_j))+\operatorname{sinc}(T(h\cdot\nu-\nu_j))\bigr],
\tag{9.29}
$$

so that whenever $A_0>0$,

$$
\sup_{t\le T}M(t)\ \ge\ \sum_jw_j\bigl(1-A_j/A_0\bigr) .
\tag{9.30}
$$

This is an identity plus one positivity step, with no non-resonance assumption: near-resonances $|h\cdot\nu|\lesssim T^{-1}$ survive inside the sinc factors instead of being discarded. Row V33 evaluates it on the actual band at $B=24$, where the normalised gain is $\approx1.50$ against the conservative analytic value $\approx1.22$ of (9.22), which shows how much the general constants give away. Turning (9.30) into a proof of Conjecture 9.2(c) would need a matching upper bound on $\sup_{t\le T}M$ for the same spectrum — an interval branch-and-bound or a dual majorant — which is the concrete next obligation.

### 9.8 A consequence outside the model: the effective domain of the lacunary rate function — Theorem 16

Theorem 13 answers a question that was posed elsewhere, about a different quantity. Let $q\ge2$ be an integer, let $x$ be uniform on $[0,1]$ — which is the invariant measure of $T_q$ — and let $\mathcal I_q$ be the large-deviation rate function of the averages $n^{-1}\sum_{k<n}\cos(2\pi q^kx)$; we write $\mathcal I_q$ and not $I$ to keep it apart from the binomial entropy of Section 4. The standard variational representation for an expanding map with constant Jacobian is

$$
\Lambda_q(\theta)=P(\theta c)-\log q,\qquad
\mathcal I_q(s)=\sup_\theta\{\theta s-\Lambda_q(\theta)\},\qquad
P(g)=\sup_{\mu\ \text{inv}}\Bigl\{h_\mu+\int g\,d\mu\Bigr\},
\tag{9.31}
$$

with $c(x)=\cos2\pi x$; equivalently $\mathcal I_q(s)=\log q-\sup\{h_\mu:\mu\ \text{invariant},\ \int c\,d\mu=s\}$, and $\mathcal I_q(s)=+\infty$ when no invariant measure has mean $s$.

**Theorem 16 [DERIVED COROLLARY; new in v1.1].** For every even integer $q\ge2$, the effective domain of $\mathcal I_q$ is exactly $[-\cos\frac\pi{q+1},1]$; that is,

$$
\mathcal I_q(s)=+\infty\ \ \bigl(s<-\tfrac{}{}\cos\tfrac\pi{q+1}\ \text{or}\ s>1\bigr),\qquad
0\le\mathcal I_q(s)\le\log q\ \ \bigl(-\cos\tfrac\pi{q+1}\le s\le1\bigr),
\tag{9.32}
$$

and at the two endpoints

$$
\boxed{\ \mathcal I_q\bigl(-\cos\tfrac\pi{q+1}\bigr)=\mathcal I_q(1)=\log q .\ }
\tag{9.33}
$$

In particular $\mathcal I_q(-1)=+\infty$ for every even $q$, while for odd $q$ the fixed point $x=\tfrac12$ gives $\mathcal I_q(-1)=\log q<\infty$.

*Proof.* By Theorem 13 the minimum of $\int c\,d\mu$ over invariant $\mu$ is $-\beta_q=-\cos\frac\pi{q+1}$ for even $q$ and the maximum is $1$, attained at the fixed point $x=0$; mixing the two extremal measures realises every intermediate value, and every invariant measure has $0\le h_\mu\le\log q$. This gives (9.32) through (9.31). For (9.33), let $\mu_t$ be an equilibrium state of $tf$ with $f=-c$. Then $0\le P(tf)-t\beta_q=h_{\mu_t}-t(\beta_q-\int f d\mu_t)\le h_{\mu_t}\le\log q$, so $\int f\,d\mu_t\to\beta_q$; by uniqueness of the maximising measure (Theorem 13) and upper semicontinuity of the entropy for an expanding map, any weak limit of $\mu_t$ is the two-cycle measure and $h_{\mu_t}\to0$, hence $P(tf)-t\beta_q\to0$ and, putting $\theta=-t$ in (9.31), $\mathcal I_q(-\beta_q)\ge\log q$. Conversely the two-cycle measure itself gives $P(\theta c)\ge-\theta\beta_q$ for every $\theta$, so $\mathcal I_q(-\beta_q)\le\log q$. The same argument at the fixed point $x=0$ gives $\mathcal I_q(1)=\log q$. $\square$

The variational principle, the upper semicontinuity of the entropy and the zero-temperature limit are imported; the new input is the exact value of $\beta_q$ and the uniqueness of the maximising measure for all even $q$. The comparison with the source that states the question, and the exact reading of what it leaves open, are in Section 12.2; the claim made here is about the effective domain and the endpoint values only, not about $\mathcal I_q$ as a whole. Row V35 carries finite numerical endpoint averages and the explicit extremal orbits; the effective-domain proof is the analytic argument above.


### 9.9 Local phase defects: a finite-time upper certificate — Theorem 20

An integer-ratio cap cannot be transferred by replacing the actual ratios with their limits. A useful replacement measures the local failure of the exact multiplication law itself. Let $q\ge2$ be even, $\nu_1,\ldots,\nu_n>0$, $w_i>0$, $\Gamma=\sum w_i$, and define

$$
r_i=\nu_{i+1}-q\nu_i,\quad
V_w=\frac{w_1+w_n+\sum_{i=1}^{n-1}|w_{i+1}-w_i|}{2},\quad
c_q=\frac{\sin(\pi/(q+1))}{q+1},\quad \beta_q=\cos\frac\pi{q+1}.
$$

**Theorem 20 [PROVEN; weighted local-defect bound].** For every $T>0$,

$$
\boxed{
\sup_{0\le t\le T}\sum_iw_i(1-\cos\nu_it)
\le(1+\beta_q)\Gamma+c_q\pi V_w
+c_qT\sum_{i<n}w_i|r_i|.}
\tag{9.34}
$$

The trivial upper bound $2\Gamma$ may be taken if smaller. There is also a constructive lower bound. Set $A=\nu_n/q^{n-1}$, $R=\max_{i<n}|r_i|$ (zero for $n=1$), $a=\pi/(q+1)$, and $t_*=(\pi-a)/A$. If $t_*\le T$, then

$$
\frac{M(t_*)}{\Gamma}\ge1+\beta_q-\frac{Rt_*}{q-1}.
\tag{9.35}
$$

*Proof.* In angular coordinates the tent $u=c_qd$ from T13 is $c_q$-Lipschitz. Its sub-action inequality gives
$-\cos\nu_it\le\beta_q+u(q\nu_it)-u(\nu_it)$.
For $i<n$ replace $u(q\nu_it)$ by $u(\nu_{i+1}t)+c_qt|r_i|$; for the last term retain $u(q\nu_nt)$. The weighted telescoping expression is bounded above by
$c_q\pi[w_n+\sum_{i=2}^n(w_{i-1}-w_i)_+]=c_q\pi V_w$ because $0\le u\le c_q\pi$. This proves (9.34).

Backward substitution gives the exact identity
$\nu_i-Aq^{i-1}=-\sum_{j=i}^{n-1}r_j/q^{j-i+1}$,
hence $|\nu_i-Aq^{i-1}|\le R/(q-1)$. At $t_*$ the geometric comparison family alternates between the two maximizing phases. The Lipschitz bound for cosine gives (9.35). $\square$

For a sequence of fast sets, the conditions $V_w/\Gamma\to0$, $T\sum w_i|r_i|/\Gamma\to0$, $t_*\le T$ and $Rt_*\to0$ are thus a **verified sufficient criterion** for $\kappa=\beta_q$, even when the finite ratios are not exact integers. To infer a first-loss exponent one still needs the strict-crossing condition (9.1e).

**Why this sufficient criterion does not settle the actual band.** Merge the reflection pairs and order their positive frequencies increasingly. Fix an interior rate $z$ of a nondegenerate compact spin band, and any fixed even integer $q$. The limiting adjacent-ratio profile $\rho(x)=(1+2x)/(1-2x)$ is strictly varying. One can therefore choose a closed macroscopic sub-band of positive limiting weight, lying strictly inside the fast set, on which $|\rho(x)-q|\ge c>0$ and $I(x)\le z-2\eta$ for some $\eta>0$. Uniform ratio convergence makes $|r_i|\ge(c/2)\nu_i$ there for large $B$. The spectral asymptotics give $\nu_i\ge J e^{-B(z-\eta)}$ after absorbing their polynomial factors. With $T=e^{Bz}/J$, it follows that

$$
\frac{T\sum_i w_i|r_i|}{\Gamma}\ge c' e^{B\eta}\longrightarrow\infty.
\tag{9.36}
$$

The same reasoning applies to the Weyl band by T19. Thus a **fixed-q application to the full macroscopic fast band fails the small-defect test**. This is not a disproof of the alignment conjecture; it rules out this particular shortcut. An argument using blocks or variable comparison ratios would require new error control across blocks, and is not supplied here.

The defect term cannot simply be omitted. For $q=2$, $n=8$, $w_i=1/8$, $\nu_i=(2^{i+3}+1)\pi$ ($i=1,\ldots,8$), $t=1$, all phases are odd multiples of $\pi$ and $M=2$. Every $r_i=-\pi$. Omitting the defect term would incorrectly bound $M$ by $3/2+\pi\sqrt3/48<2$; the full bound is $3/2+\pi\sqrt3/6>2$. W47 verifies both inequalities with exact directed intervals. This witness is related to (9.11), not an independent discovery of arithmetic sensitivity.

### 9.10 Deterministic integer shifts: the complete large-deviation law — Theorem 31

The preceding endpoint results concern exact geometric frequencies. The next question changes the frequencies themselves, rather than perturbing the observable on the same expanding map. Let $U$ be uniform on $[0,1]$, let $q\ge2$ be an integer, and put

$$
S_n^{a,r}(U)=\sum_{k=0}^{n-1}\cos\bigl(2\pi(aq^k+r)U\bigr),\qquad
Z_n^{a,r}(\theta)=\mathbb E\exp(\theta S_n^{a,r}).
\tag{9.37}
$$

Here $a,r$ are nonzero integers. The common shift $r$ is the same for every summand; the phases are generated by **one** random variable, not independent phases. Negative frequencies and a possible isolated zero frequency are allowed. The usual sequence $q^k+r$, indexed by $k=1,\ldots,n$, corresponds to $a=q$ in (9.37). The unshifted pressure $\Lambda_q$ and rate $\mathcal I_q$ retain their normalization (9.31).

**Theorem 31 [PROVEN; new in v1.8].** For every such $q,a,r$,

$$
\boxed{\lim_{n\to\infty}\frac1n\log Z_n^{a,r}(\theta)
=\Lambda_q(|\theta|),\qquad \theta\in\mathbb R.}
\tag{9.38}
$$

The averages $S_n^{a,r}/n$ satisfy a full large-deviation principle at speed $n$, with good rate function

$$
\boxed{\mathcal J_q(s)=\mathcal I_q(|s|),\qquad
\operatorname{dom}\mathcal J_q=[-1,1],\qquad
\mathcal J_q(-1)=\mathcal J_q(1)=\log q.}
\tag{9.39}
$$

The value is $+\infty$ outside that interval. More quantitatively, for every integer $1\le m<n$, writing $t=|\theta|$ and $R=|r|$,

$$
\left|\frac1n\log Z_n^{a,r}(\theta)-\Lambda_q(t)\right|
\le \frac{m(2t+\log q)}n+
\frac{2\pi t}{(q-1)n}+4\pi tR q^{-m}.
\tag{9.40}
$$

This estimate is uniform in the nonzero integer $a$. For fixed $q,r$, choosing $m=\lceil\log_q(nR)\rceil$ once $m<n$ gives a locally uniform $O((\log n)/n)$ error in the tilt. Neither the rate nor the limiting pressure depends on the magnitude or sign of the nonzero integer shift. The change between $r=0$ and $r\ne0$ for even $q$ is an arithmetic distinction; no real-parameter continuity theorem is asserted.

We give the finite comparison that proves the theorem. It avoids an assumption that the slow phase and the expanding coordinate are independent.

**Lemma 31.1 (uniform distortion and a Fourier majorant).** Set

$$
M_N(\theta,\phi)=\int_0^1\exp\left\{\theta\sum_{k=0}^{N-1}
\cos\bigl(2\pi(q^ky+\phi)\bigr)\right\}dy.
$$

For $t\ge0$, every $N\ge1$ and every real $\phi$,

$$
0<M_N(t,\phi)\le M_N(t,0),\qquad
M_N(-t,\phi)=M_N(t,\phi+\tfrac12).
\tag{9.41}
$$

Also, for $L=2\pi|\theta|$ and $D=L/(q-1)$, the limit
$\Lambda_{q,\phi}(\theta)=\lim_N N^{-1}\log M_N(\theta,\phi)$ exists and

$$
|\log M_N(\theta,\phi)-N\Lambda_{q,\phi}(\theta)|\le D.
\tag{9.42}
$$

In particular $\Lambda_{q,0}=\Lambda_q$. The bound in (9.42) is uniform in $\phi$; no uniform spectral-gap estimate is being assumed.

*Proof.* The absolutely convergent Fourier expansion
$e^{t\cos(2\pi z)}=\sum_{h\in\mathbb Z}I_h(t)e^{2\pi ihz}$ has nonnegative coefficients for $t\ge0$. Multiplication and integration retain only tuples satisfying $\sum_{k=0}^{N-1}h_kq^k=0$. Each surviving coefficient is nonnegative, and its remaining phase is $e^{2\pi i\phi\sum_kh_k}$, of modulus one. The triangle inequality gives (9.41); the sum of absolute coefficients before integration is $e^{Nt}$, so the interchange is justified. The second identity is the half-turn identity for cosine. This is an application of classical Fourier positivity, not a new positivity principle.

For completeness, partition $[0,1]$ into cylinders $x=(j+y)/q^N$, $0\le j<q^N$. For $g(x)=\theta\cos(2\pi(x+\phi))$, the first $N$ terms of its Birkhoff sum differ at two points of a cylinder by at most
$L\sum_{k=0}^{N-1}q^{k-N}\le D$. The remaining $K$ terms are precisely the $K$-term sum at $y$. Comparing the first factor with its cylinder average proves

$$
e^{-D}M_NM_K\le M_{N+K}\le e^D M_NM_K
\tag{9.43}
$$

at the same $(\theta,\phi)$. The subadditive and superadditive bounds for $\log M_N\pm D$ give existence of the common limit. Alternatively, first take multiples of a fixed $N$ in (9.43) and then control the bounded remainder. They give (9.42). $\square$

**Lemma 31.2 (freezing a phase that is tied to the initial point).** With $N=n-m$, $\phi_j=rj/q^m$ and the preceding $L$,

$$
e^{-mt-NLRq^{-m}}\frac1{q^m}\sum_{j=0}^{q^m-1}M_N(\theta,\phi_j)
\le Z_n^{a,r}(\theta)\le
e^{mt+NLRq^{-m}}\frac1{q^m}\sum_{j=0}^{q^m-1}M_N(\theta,\phi_j).
\tag{9.44}
$$

*Proof.* On $x=(j+y)/q^m$, discard the first $m$ bounded summands. For $k=m+\ell$ the exact phase is

$$
(aq^{m+\ell}+r)x
=aq^\ell j+aq^\ell y+\frac{rj}{q^m}+\frac{ry}{q^m}.
\tag{9.45}
$$

The first term is an integer, including when $a<0$. Replacing the last term by zero changes the exponent of the tail by at most $NLRq^{-m}$. The integral of the frozen tail is $M_N(\theta,\phi_j)$ because $y\mapsto ay\pmod1$ preserves Lebesgue measure for every nonzero integer $a$. This last exact fact, rather than an equidistribution approximation, is why the error is independent of $a$. Integrate over the cylinders to obtain (9.44). $\square$

*Proof of Theorem 31.* Write $\lambda=\Lambda_q(t)$. By (9.41), every summand in the average in (9.44) is at most $M_N(t,0)$. To bound the average from below, keep one summand. For $\theta\ge0$ take $j=0$. For $\theta<0$, put $x_*=1/(2R)$ and $j=\lfloor q^mx_*\rfloor$. Then $rx_*\equiv1/2\pmod1$ and the circular distance from $\phi_j$ to $1/2$ is at most $Rq^{-m}$. The logarithm of $M_N$ is $NL$-Lipschitz in its phase, so this term is at least $e^{-NLRq^{-m}}M_N(t,0)$. Thus

$$
e^{-mt-m\log q-2NLRq^{-m}}M_N(t,0)
\le Z_n^{a,r}(\theta)
\le e^{mt+NLRq^{-m}}M_N(t,0).
\tag{9.46}
$$

By (9.42), $|\log M_N(t,0)-N\lambda|\le D$. Jensen's inequality and the bounded cosine give $0\le\lambda\le t$. Substitution in (9.46) yields (9.40), hence (9.38). Notice the cylinder probability $q^{-m}$ in the lower bound. Omitting that factor would discard a real entropy cost, even though $m=o(n)$ makes it negligible at the final speed.

The pressure $\Lambda_q$ for the geometric system is finite and real analytic on $\mathbb R$, with $\Lambda_q'(0)=\int c\,dx=0$. These are standard expanding-map pressure facts, also used in §9.8. Consequently $\theta\mapsto\Lambda_q(|\theta|)$ is differentiable everywhere, including at zero. It is finite on all of $\mathbb R$; boundedness of $S_n^{a,r}/n$ supplies exponential tightness. The differentiable Gärtner–Ellis theorem therefore gives the full LDP. Higher differentiability is not needed.

For $s\ge0$, negative tilts cannot improve the Legendre supremum for the unshifted pressure: $\theta s-\Lambda_q(\theta)\le0$ when $\theta<0$, while the value at zero is zero. Here $\Lambda_q(\theta)\ge0$ follows again from the zero mean. The even limiting pressure in (9.38) therefore has Legendre transform $\mathcal I_q(|s|)$. The positive branch of §9.8 has domain $[0,1]$ and endpoint $\mathcal I_q(1)=\log q$ for every integer $q\ge2$, giving (9.39). Endpoint values are costs of arbitrarily small neighborhoods; they do not assert positive probability of the exact event $S_n/n=\pm1$. $\square$

The proof uses neither the local perturbation radius of T28 nor the zero-temperature excursion machinery of T24–Cor30. T13/T16 remain essential to the comparison with the *unshifted negative* branch for even $q$. The all-shift computation itself is driven by the finite Fourier majorant and the cylinder estimate.

### 9.11 Shifts that grow with the observation length — Corollary 32

**Corollary 32 [PROVEN; new in v1.8].** Fix $q\ge2$. Let $a_n,r_n$ be arbitrary nonzero integers such that $\log(1+|r_n|)=o(n)$. For each $n$ use the same $a_n,r_n$ in all $n$ summands of (9.37). Then $S_n^{a_n,r_n}/n$ has the same limiting pressure and the same full LDP (9.38)–(9.39). There is no growth restriction on $|a_n|$.

*Proof.* Set $m_n=\lceil\log_q(n|r_n|)\rceil$. Then $m_n/n\to0$, $|r_n|q^{-m_n}\le1/n$, and eventually $1\le m_n<n$. The right side of (9.40) tends to zero locally uniformly in $\theta$. Apply the same differentiable Gärtner–Ellis argument. $\square$

This is a triangular-array statement for a **common** offset in each row. It does not cover arbitrary $k$-dependent errors, noninteger multipliers, exponentially growing offsets, or weighted physical spin frequencies. The displayed condition is sufficient; its necessity is not claimed.

### 9.12 A differentiable pressure that is not analytic — Corollary 33

Let $I_0$ denote the modified Bessel function and let $\widetilde{\mathcal I}$ be the Legendre transform of $\log I_0$, the rate of independent uniform-phase cosines. The first non-independent Taylor coefficient of the geometric pressure is **imported**, not a new cumulant calculation: [Aistleitner–Gantert–Kabluchko–Prochno–Ramanan, Theorem B(ii),(iv), proof in §3.3.3](https://arxiv.org/html/2012.05281v1) gives

$$
\Lambda_q(\theta)=\log I_0(\theta)
+\frac{\theta^{q+1}}{2^q q!}+O(\theta^{q+2}).
\tag{9.47}
$$

**Corollary 33 [PROVEN; new consequence of T31 and the imported coefficient].** For every even $q\ge2$ and every nonzero integer shift in T31,

$$
\Lambda_q(|\theta|)=\log I_0(\theta)
+\frac{|\theta|^{q+1}}{2^q q!}+O(|\theta|^{q+2}).
\tag{9.48}
$$

This limiting function is $C^q$ but not $C^{q+1}$ at zero. Its one-sided derivatives of order $q+1$ differ by $(q+1)/2^{q-1}$, with the right derivative larger. Its rate satisfies

$$
\mathcal J_q(s)=\widetilde{\mathcal I}(s)
-\frac{2}{q!}|s|^{q+1}+O(|s|^{q+2})\qquad(s\to0).
\tag{9.49}
$$

In particular $\mathcal J_2(s)=s^2-|s|^3+O(s^4)$ and the limiting pressure is $\theta^2/4+|\theta|^3/8+O(\theta^4)$.

*Proof.* On each side of zero (9.38) is an analytic branch. Substitution in the convergent Taylor series (9.47) gives (9.48), and the first odd power is $q+1$. This proves the asserted differentiability and derivative jump; a remainder estimate alone, without these analytic branches, would not suffice. For the rate, the independent positive saddle is $\theta_0(s)=2s+O(s^3)$, since $\log I_0(\theta)=\theta^2/4+O(\theta^4)$. Perturbing its strictly convex saddle by a term $c\theta^{q+1}$ changes the Legendre value to first order by $-c\theta_0(s)^{q+1}$; the saddle displacement contributes $O(s^{2q})$, which is $O(s^{q+2})$ for $q\ge2$. Equations (9.47) and (9.39) give (9.49). $\square$

For odd $q$, translation of the initial point by $1/2$ reverses every geometric cosine, so $\Lambda_q$ is already even. The shifted limiting pressure is then analytic and equals the unshifted one. No cusp is claimed in that case.

The sequence $2^k+1$ and its non-linear cumulants are already in [Aistleitner–Kabluchko–Prochno, Theorem B](https://arxiv.org/html/2512.15501v1). We use that result as a collision test, not as new v1.8 content. In their indexing, all odd finite-$n$ cumulants vanish, whereas for $n\ge7$
$\kappa_6(S_n)=(45n^2+380n-1875)/16$. There is no conflict with T31: each finite-$n$ MGF is even and analytic, but its limiting log-MGF per term is only $C^2$ at zero for $q=2$. Convergence on the real tilt axis does not permit passage of third or higher derivatives through the limit. Our exact Laurent-polynomial check reproduces the supplied sixth-cumulant formula at specified finite sizes; it does not derive the general published formula or prove the LDP by cumulants.

### 9.13 A tail that changes from impossible to possible — Proposition 34

**Proposition 34 [PROVEN; new quantitative consequence, using the inherited T13].** For $n\ge4$,

$$
\mathbb P\!\left[\frac1n\sum_{k=1}^{n}\cos(2\pi2^kU)\le-\frac34\right]=0,
\qquad
\mathbb P\!\left[\frac1n\sum_{k=1}^{n}\cos(2\pi(2^k+1)U)\le-\frac34\right]
\ge\frac1{6(2^n+1)}.
\tag{9.50}
$$

*Proof.* The tent inequality in T13, summed from the initial point $2U$, gives
$\sum_{k=1}^{n}\cos(2\pi2^kU)\ge-n/2-\operatorname{osc}u$, where $\operatorname{osc}u=\pi\sqrt3/6<1$. For $n\ge4$ the average is strictly larger than $-3/4$. For the shifted sum, all $2^k+1$ are odd. Whenever
$|U-1/2|\le[12(2^n+1)]^{-1}$, each phase is an odd multiple of $\pi$ plus an error of absolute size at most $\pi/6$. Every cosine is therefore at most $-\sqrt3/2<-3/4$. The interval has the stated measure. $\square$

More generally, T16 and T31 show that for even $q$ the effective domain changes from $[-\beta_q,1]$ to $[-1,1]$ after any nonzero integer shift. The positive rate branch is preserved and reflected to supply the negative branch. Since $(q^k+r)/q^k\to1$, vanishing relative frequency error is insufficient even to preserve the set of exponentially accessible averages. Arithmetic sensitivity itself was known; (9.38)–(9.40) compute its full effect on this deterministic family.

For the physical problem the lesson has an exact scope. For frequencies $\nu_k=aq^k+r$, the local recurrence error used by T20 is $\nu_{k+1}-q\nu_k=(1-q)r$, despite the vanishing relative error. A growing observation time can magnify that absolute phase defect. One may therefore not transfer a geometric alignment cap to the actual spin band using only ratio asymptotics. T20 states an appropriate sufficient phase-error test; its failure for the full compact band was already established in §9.9. T31 supplies a complete probabilistic example of the distinction. It does **not** compute the actual spin-band alignment limit, the weighted first-loss time, or an action-derived measurement instrument.

## 10. Extensions: the diffusive scale, the endpoint band and other parents

### 10.1 The two-boundary formula down to the diffusive scale — Theorem 10

Theorem 1(b) requires both boundaries at a fixed positive fraction of $B$ from the centre. The seed left the regime $j-w=o(B)$ open and recorded an observed $O(1/h)$ behaviour of the relative error without proof. The exact resistance sums settle the regime, with a sharper statement than the one observed.

Let a boundary of a proper window be at distance $h$ from the midpoint $m=\lfloor B/2\rfloor$ (so $l=m-h$ for a left boundary), and write $x=h/B$, $\rho_0=l/(B-l)$ and $A=l\pi_l(1-\rho_0)$ for the leading term of the inverse resistance.

**Theorem 10 [PROVEN].** (i) For every proper boundary with $3\sqrt B\le h\le B/2$,
$$
\frac1{R}=A\,(1+\varepsilon),\qquad |\varepsilon|\le C_0\,\frac B{h^2},
\tag{10.1}
$$
with an absolute constant $C_0$, and for $3\sqrt B\le h\le B/4$
$$
\varepsilon=-\frac{B}{4h^2}\cdot\frac{1-2x}{1+2x}+O\Bigl(\frac{B^2}{h^4}+\frac1h\Bigr).
\tag{10.2}
$$
(ii) For every proper window whose nearer boundary satisfies $h_{\min}\ge\sqrt{2B\log B}$ (and $B\ge B_0$),
$$
\boxed{\;\widetilde\lambda_{[l,u]}=(A_L+A_R)\bigl(1+O(B/h_{\min}^2)\bigr).\;}
\tag{10.3}
$$

*Proof of (i), the diffusive regime $h\le B/4$.* With $P_s=\prod_{r<s}\rho_r$, $\rho_r=(l+r)/(B-l-r)$, one has $R=(l\pi_l)^{-1}\sum_{s=0}^{h}P_s$ and
$$
\log\frac{\rho_r}{\rho_0}=\log\Bigl(1+\frac rl\Bigr)-\log\Bigl(1-\frac r{B-l}\Bigr)=r\Bigl(\frac1l+\frac1{B-l}\Bigr)-\frac{r^2}2\Bigl(\frac1{l^2}-\frac1{(B-l)^2}\Bigr)+O\Bigl(\frac{r^3}{l^3}\Bigr),
$$
so $\log P_s=s\log\rho_0+\frac{2s(s-1)}{B''}-O\bigl(s^3h/B^3\bigr)$ with $B''=B(1-4x^2)=4l(B-l)/B\ge\tfrac34B$. Split the sum at $s_1=\sqrt B$ and write $K=h/\sqrt B\ge3$. For $s\le s_1$ the exponent $u_s=2s(s-1)/B''$ satisfies $u_s\le3$, so $e^{u_s}=1+u_s+O(u_s^2)$ with an absolute constant, and

$$
\sum_{s\le s_1}\rho_0^s\,u_s=\frac2{B''}\sum_{s\ge0}s(s-1)\rho_0^s-D,\qquad
D=\frac2{B''}\sum_{s>s_1}s(s-1)\rho_0^s ,
$$

using the **exact** identity $\sum_{s\ge0}s(s-1)\rho^s=2\rho^2/(1-\rho)^3$. The omitted tail has the exact closed form

$$
D=\frac{2\rho_0^{s_1+1}}{B''}\left[\frac{s_1(s_1+1)}{1-\rho_0}+\frac{2(s_1+1)\rho_0}{(1-\rho_0)^2}+\frac{2\rho_0^2}{(1-\rho_0)^3}\right] ,
\tag{10.2b}
$$

and it must be estimated **after** dividing by the main term $1/(1-\rho_0)$, not before. v1.1 wrote it as $O(\rho_0^{\sqrt B})$ with an implied absolute constant, which is false uniformly in $B$ and $h$: at $h=3\sqrt B$, $B=m^2$, one has $\rho_0=(m-6)/(m+6)$, $B''=m^2-36$ and

$$
\lim_{m\to\infty}\frac{D}{m\,\rho_0^{m}}=\frac{85}{432}>0 ,
\tag{10.2c}
$$

so $D/\rho_0^{\sqrt B}$ grows like $\sqrt B$ (this was finding F03 of the v1.1 audit; row C39 carries the closed form and the limit). Normalised, however, the tail is comfortably inside the required second-order budget: since $1-\rho_0=4h/(B+2h)\ge8K/(3\sqrt B)$ and $\rho_0^{\sqrt B}\le e^{-4K}(1+o(1))$,

$$
(1-\rho_0)\,D\ \le\ \frac{85}{108}\,K\,e^{-4K}\bigl(1+O(K^{-1})\bigr)\ =\ O(K^{-4})\ =\ O\Bigl(\frac{B^2}{h^4}\Bigr)\qquad(K\ge3),
\tag{10.2d}
$$

because $\sup_{K\ge3}K^5e^{-4K}=3^5e^{-12}<1.5\times10^{-3}$. The same accounting upgrades the two remaining tails of this proof, which v1.1 recorded only as $O(B/h^2)$: $e^{-4K/3}\le1.4836\,K^{-4}$ and $K^2e^{-2K^2/3}\le1.81\,K^{-4}$ for every $K\ge3$. In the first, $K^4e^{-4K/3}$ has its interior critical point exactly at $K=3$ and the supremum is $81e^{-4}=1.48356\ldots$, so the rounder constant $1.48$ that an earlier draft carried is **false at $K=3$** by $2\times10^{-3}$ relative; in the second, $K^6e^{-2K^2/3}$ is decreasing for $K>\sqrt{9/2}$ and the supremum is $3^6e^{-6}=1.80701\ldots$ at the endpoint. Every discarded term is therefore $O(B^2/h^4)$, which is the order already present in (10.2). Relative to the main term $1/(1-\rho_0)$ this is, with $1-\rho_0=4h/(B+2h)$, $\rho_0=(B-2h)/(B+2h)$ and $B''=(B-2h)(B+2h)/B$, the exact rational quantity

$$
\frac{4\rho_0^2}{B''(1-\rho_0)^2}=\frac{B}{4h^2}\cdot\frac{1-2x}{1+2x} ,
\tag{10.2a}
$$

and keeping the next term $O(u_s^2)$, whose sum contributes $O(1/(B''^2(1-\rho_0)^4))=O(B^2/h^4)$, gives the remainder in (10.2). The leading coefficient and the statement of Theorem 10 are unchanged by this repair. Two further terms are dropped in the expansion of $\log P_s$ and are worth naming rather than leaving implicit: the $O(s^3h/B^3)$ shown above and an $O(s^4/B^3)$ from the same Taylor step. Summed against $\rho_0^s$ and normalised they contribute at most $(B+2h)^3/(2B^3h^2)\le1.7/h^2$, which is inside the $O(1/h)$ already allowed in (10.2); the splitting point is $s_1=\lfloor\sqrt B\rfloor$. **Correction to v1.0.** The v1.0 proof replaced $s(s-1)$ by $s^2$ and then bounded $\sum_ss^2\rho^s$ by $2\rho^2/(1-\rho)^3$. That inequality runs the wrong way: $\sum_ss^2\rho^s=\rho(1+\rho)/(1-\rho)^3\ge2\rho^2/(1-\rho)^3$ for $\rho\le1$, with equality only at $\rho=1$, and at $\rho=\tfrac13$ the two sides are $1.5$ and $0.75$. The audit of v1.0 recorded this as finding F06. Keeping the $s(s-1)$ that the expansion actually produces repairs the step and returns the same leading coefficient; row C32 carries both sums, the counterexample and the exact identity (10.2a). For $\sqrt B<s\le h/2$, using $4h/(B+2h)\ge8h/(3B)$ and $2s^2/B''\le4sh/(3B)$, $P_s\le e^{-4sh/(3B)}$, whose sum is at most $e^{-4h/(3\sqrt B)}(3B/(4h)+1)$, relatively $O(e^{-4K/3})=O(K^{-4})=O(B^2/h^4)$ for $h\ge3\sqrt B$ by the bound just given. For $s>h/2$, $P_s\le P_{\lfloor h/2\rfloor}\le e^{-2h^2/(3B)}$ and there are at most $h$ terms, relatively $O(K^2e^{-2K^2/3})=O(K^{-4})=O(B^2/h^4)$ again. The geometric main term is truncated at the splitting point, not at $h$: $\sum_{s\le s_1}\rho_0^s$ differs from $1/(1-\rho_0)$ by the relative amount $\rho_0^{s_1+1}\le e^{-4K}$, and $\sup_{K\ge3}K^4e^{-4K}=81e^{-12}=5.0\times10^{-4}$, so this deficit too is $O(K^{-4})$; the smaller quantity $\rho_0^{h+1}\le e^{-8h^2/(3B)}$ quoted in v1.1 at this point was the wrong one. Collecting, $\sum_sP_s=\frac1{1-\rho_0}(1+\varepsilon')$ with $\varepsilon'=+\frac{B}{4h^2}\frac{1-2x}{1+2x}+O(B^2/h^4+1/h)$, and inverting gives (10.2).

*Proof of (i), the far regime $h>B/4$ ($l<B/4$).* Here $\rho_0\le1/3$. For $s\le\sqrt l$ the bound $P_s\le\rho_0^se^{s(s-1)/(2l)+s^2/B}$ and $P_s\ge\rho_0^s$ give a relative deviation $O(\rho_0/l)=O(1/B)$ from the geometric sum. For $\sqrt l<s\le\tfrac12l\log(1/\rho_0)$ the same bound gives $P_s\le\rho_0^{s/2}$, whose sum is $O(\rho_0^{\sqrt l/2})$; for larger $s$, $P_s$ is monotone decreasing and at most that value, so the tail is $O(B\rho_0^{\sqrt l/2})$, superpolynomially small when $l\ge(\log B)^2$. When $l\le\sqrt B$, $P_s\le\bigl(2(l+s)/B\bigr)^s\le(4/\sqrt B)^s$ for $2\le s\le\sqrt B$, so $\sum_{s\ge2}P_s=O(1/B)$, while $\sum_{s\ge2}\rho_0^s=O(l^2/B^2)$. In all cases $|\varepsilon|\le C/B\le16C\,B/h^2$.

*Proof of (ii).* By (i), $\mathcal C_m=(A_L+A_R)(1+O(B/h_{\min}^2))$, since each inverse resistance is $A(1+O(B/h^2))$ and the larger relative error is the one of the nearer boundary. For the spectral step, (3.5)–(3.6) give $\widetilde\lambda/\mathcal C_m=1+O(\sqrt{\mathcal C_m/\pi_m}\,)$; with $\pi_l/\pi_m\le\sqrt{\pi B/2}\,e^{-2h^2/B}$ (Hoeffding on the single term) and $A\le2h\pi_l$ this is $O(h^{1/2}B^{1/4}e^{-h^2/B})$. For $h^2\ge2B\log B$ one has $e^{-h^2/B}\le B^{-2}$, so with $h\le B/2$ the bound is $O(B^{1/2}B^{1/4}B^{-2})=O(B^{-5/4})$, and since $B/h^2\ge4/B\ge B^{-5/4}$ for $B\ge1$ this is indeed $O(B/h^2)$. $\square$

*(v1.0 printed $O(B^{-3/4})$ at this point and concluded $O(B/h^2)$ "because $h\le B/2$", which does not follow — $B^{-3/4}$ is much larger than $4/B$. The audit recorded the arithmetic slip as part of finding F06; the corrected exponent $B^{-5/4}$ closes the step as stated.)*

Row V21 evaluates the exact rational capacities: at $B=1024$ and $B=4096$ the quantity $(\mathcal C_m/(A_L+A_R)-1)\,h^2/B$ follows $-(1-2x)/(4(1+2x))$ with residual ratio $0.23,0.075,0.041,0.018,0.011$ at $h/\sqrt B=2,3,4,6,8$ (the residual scales as $B/h^2$, i.e. as the $B^2/h^4$ term of (10.2)), and at $B=16384$, $h=3\sqrt B$ the measured coefficient is $-0.2432$ against its own leading value $-(1-2x)/(4(1+2x))=-0.2276$ at $x=3/128$, the $7\%$ difference being exactly the residual that the table above tabulates at $h/\sqrt B=3$. (v1.0 and v1.1 printed "$-0.243$ against the leading $-0.239$", which compared the measured value at $B=16384$ with the leading value at $B=65536$; the two sizes have been separated here.) The Sturm eigenvalue at $B=1024$, $h=96$ agrees with the capacity to $1.9\times10^{-7}$. The observed $O(1/h)$ of the earlier seed is therefore replaced by the proved $O(B/h^2)$ with explicit coefficient: at fixed $B$ the relative error decays like $h^{-2}$, not $h^{-1}$.

**Consequences [restricted in v1.1].** The two consequences printed in v1.0 were stated in a range in which they are false or unproved; the audit recorded this as finding F07. The corrected statements are the following.

(a) *Weights.* For every proper window with $h_{\min}\ge\sqrt{2B\log B}$ the weight statement of Section 3.3 survives unchanged: $1-v_k\le\tfrac12(\sqrt{\widetilde\lambda_k}+\sqrt{\widetilde\lambda_{k+1}})^2\to0$, because $\widetilde\lambda\le2h\pi_l\sqrt{2\pi B}$ is small there.

(b) *Gaps: keep the entropy, restrict the Gaussian.* The correct exponential scale of a one-boundary contribution is $e^{-BI(h/B)}$, not $e^{-2h^2/B}$. Since

$$
B\,I(h/B)-\frac{2h^2}B=\frac43\frac{h^4}{B^3}\bigl(1+O(h^2/B^2)\bigr),
\tag{10.3a}
$$

the Gaussian replacement is legitimate only in the moderate-deviation window $h=o(B^{3/4})$, and it fails badly beyond it: at $h=\lceil B^{4/5}\rceil$ the ratio $e^{-BI}/e^{-2h^2/B}$ tends to $0$ superpolynomially (row V36 evaluates both sides at $60$ digits; at $B=10^6$ the ratio is $6\times10^{-10}$). Explicitly, for $j=\lceil B^{4/5}\rceil$ and the two central windows, a Rayleigh test function obtained by truncating the full-line ground vector to the window, together with the binomial Stirling bound, gives $|E_1-E_0|\le CJB^{-1/2}e^{-BI((j-1)/B)}$, so dividing by the scale $G_B=J(j-\tfrac12)^2B^{-5/2}e^{-2(j-1/2)^2/B}$ printed in v1.0,

$$
\frac{|E_1-E_0|}{G_B}\ \le\ C\frac{B^2}{(j-1/2)^2}\exp\Bigl[-\frac{4(j-1)^4}{3B^3}+O(j/B)\Bigr]\ \longrightarrow\ 0 ,
$$

so no uniform positive $\Theta(G_B)$ lower bound holds on the whole range $h\ge\sqrt{2B\log B}$. Within $\sqrt{2B\log B}\le h=o(B^{3/4})$ the Gaussian form may be used, with the caveat of (c).

(c) *A relative error on eigenvalues is not a relative error on their differences.* (10.3) controls $\widetilde\lambda$ to relative $O(B/h_{\min}^2)$; adjacent differences can be smaller than that error when the two boundary contributions cancel, which happens near the centre of a window whose two boundaries are comparable. Extending the *adjacent-gap* lemma of Section 3.3 into the diffusive range therefore requires a separate remainder estimate for the difference, which this paper does not supply. (For the standard band of Section 4 this is not an obstruction, because there $j=B/3$, $w=B/6$ and the near boundary dominates the far one at every band position; that is the regime used in Theorem 15.)

(d) *The third time scale is a statement about frequencies, not about $T_\ell$.* For $h=K\sqrt B$ with $K$ fixed, the inverse frequency of an edge mode is of order $B^{3/2}e^{2K^2}/J$. This is a scale, and v1.0's sentence calling it "the first loss" of the band is withdrawn twice over: $h=K\sqrt B$ does not satisfy the hypothesis $h\ge\sqrt{2B\log B}$ of (10.3), so the capacity-to-eigenvalue step is not available there; and the first time at which a *fixed* loss $\ell>0$ is reached is not decided by modes whose weight tends to $0$. A first-loss law in that window would need its own scaling theorem, and is listed as open in Section 14.

### 10.2 The endpoint band $a=b$ — Theorem 11

Condition (3.11) requires $b<a$, i.e. $j-w\ge x_0B$ with $x_0>0$. The seed listed the transition $j-w=o(B)$ as open. The exponent interval passes continuously to the endpoint.

**Theorem 11 [PROVEN].** Let $j/B\to a$, $w/B\to b$ with $0<b=a\le\tfrac14$ (so $j+w\le B/2$ and $j-w=o(B)$, including $j-w=O(1)$). Then for every fixed $\ell\in(0,\tfrac12)$,
$$
I(b\,y_{\ell/2})\le\liminf_B\frac{\log(JT_\ell)}B\le\limsup_B\frac{\log(JT_\ell)}B\le I(b\,y_\ell),
\tag{10.4}
$$
which is (4.5) with $x_p=a-b+by_p$ evaluated at $a=b$.

*Proof.* Apply Theorem 2(c) in its relaxed form. Fix $\eta>0$. The modes with $x_k=j/B-|k+\tfrac12|/B\ge\eta$ form a band satisfying the compact condition with $x_0=\eta$ (and the endpoint split of Section 3.3 when $a+b=\tfrac12$), so their rates converge uniformly to $I(a-|s|)$ by (3.13) and their weights to the density (4.6) by (3.16). The modes with $x_k<\eta$ have total weight at most $F(\eta/b)+o(1)$, which tends to $0$ as $\eta\downarrow0$; they are the arbitrary family of vanishing weight allowed in Theorem 2(c). The limiting rate measure is therefore the image of the density (4.6) under $s\mapsto I(a-|s|)$ with $a=b$; its cumulative $H$ is continuous and strictly increasing on $(0,I(a))$, since $I$ is strictly increasing on $(0,\tfrac12)$ and the density is positive on $(-b,b)$. The quantiles are $q_p=I(x_p)$ with $x_p=by_p>0$. $\square$

Row V22 computes the band $j=w=B/4$ at $B=96,192$: all adjacent gaps are positive, $\Gamma_B>0.997$, and the computed first losses lie inside the finite envelopes; the finite exponents ($0.077$ and $0.048$ at $\ell=0.1$) are still far above the asymptotic fronts $[0.0126,0.0205]$ because here $BI(x_p)$ is only of order $10$ and the polynomial prefactor dominates — this is a check of the finite mechanics, not a certification of the limit.

The small-$x$ transition of Section 4.3 is thereby continuous in the exponent: as $a-b\downarrow0$ the fronts $I(x_p)$ tend to $I(by_p)>0$, while the edge modes themselves ($h_k=O(\sqrt B)$) become polynomially fast and carry vanishing weight.

Two scope notes. The proof uses Theorem 2(c) and the compact estimates of Section 3.3 on the sub-band $x_k\ge\eta$ only; it does **not** use the diffusive-range gap statements of Section 10.1, so the restrictions (b)–(d) imposed there do not touch Theorem 11. And the upper end of (10.4) is still the $q_\ell$ end: the improvement of Theorem 15 needs one ratio $\rho>1$ uniform over the fast set, which the endpoint band does not provide, since its ratios degenerate to $1$ at the centre.

### 10.3 Parent independence and the Weyl parent — Proposition 12

Theorem 1(a) used only two properties of the parent: a positive stationary weight $\pi$ with a reversible birth–death generator, and a spectral gap of the full generator.

**Proposition 12 [PROVEN].** Let $A$ be any real symmetric tridiagonal matrix on $\{0,\ldots,B\}$ with negative off-diagonal entries, ground energy $E_*$, positive normalised ground vector $\beta$, $\pi_b=\beta_b^2$, and full spectral gap $g>0$ of the similar generator $\widetilde L=\beta^{-1}(A-E_*)\beta$ (in the units in which the off-diagonal conductances are $a_b=\beta_b\beta_{b+1}|A_{b,b+1}|$). Then for every proper window and interior point, with $\mathcal C_m$ built from these conductances,
$$
\frac{\mathcal C_m}{\bigl[1+\sqrt{\mathcal C_m/g}\,(1+\pi_m^{-1/2})\bigr]^2}\le\widetilde\lambda_I\le\frac{\mathcal C_m}{\|h\|_\pi^2}.
$$
*Proof.* Identical to Theorem 1(a) with $\operatorname{Var}_\pi(f)\le\mathcal E(f,f)/g$. $\square$

Proposition 12 is a finite inequality and is unconditional. What does **not** follow from it is a statement about the exponential rate of another parent's gaps, and v1.0 drew that inference in two steps, both of which are corrected here.

**Correction 1: the Weyl ground energy is not exactly $-(1-1/B)$, and the gap to it is not superexponentially small (findings F08 of the v1.0 audit and F02 of the v1.1 audit).** For the Weyl-ordered edge of the finite-island Josephson matrix (Appendix S6.13.1), $(a^W_b)^2=1-((2b+1-B)/B)^2$, v1.0 asserted that the ground energy is exactly $-(1-1/B)$ and the gap exactly $2/B$. That is false, and v1.1 refuted it with the characteristic polynomial: with zero diagonal and off-diagonal entries $-a^W_b/2$,

$$
p_0=1,\qquad p_1=z,\qquad p_{b+2}=z\,p_{b+1}-\frac{(2b+1)(2B-2b-1)}{4B^2}\,p_b ,
\tag{10.5}
$$

and in exact rational arithmetic $p_{B+1}(-(1-1/B))$ is non-zero and positive for every $B$ tested: $5.3\times10^{-3}$ at $B=4$, $9.6\times10^{-9}$ at $B=16$, $3.6\times10^{-114}$ at $B=256$ (row C29). What a sign says is only a parity, and only relative to the dimension: $p_{B+1}(z)=\prod_i(z-\lambda_i)$ over $B+1$ eigenvalues, so $p_{B+1}(z)>0$ means $\#\{\lambda_i<z\}\equiv B+1\pmod 2$. The sampled sizes above are all even, where this reads "an odd number, in particular at least one, so $E^W_0<-(1-1/B)$"; at **odd** $B$ the same non-vanishing shows up with the opposite sign — $-1.77\times10^{-2}$ at $B=3$, $-3.33\times10^{-9}$ at $B=17$ — again with one eigenvalue below (row C40). v1.1 wrote "exactly one eigenvalue lies below", which does not follow from a determinant sign at all, and stated the parity rule without the dimension, which is wrong at odd $B$. A zero-diagonal path on seven vertices with off-diagonal $-1$ has positive characteristic polynomial at $z=-1/10$ with three eigenvalues below it (row C40). v1.1 then inferred from the size of $p_{B+1}$ that the energy deviation is superexponentially small. That inference is also invalid — the determinant is a product of $B+1$ factors, only one of which is the deviation — and the conclusion is false, as the following replacement shows.

**Proposition 17 [PROVEN; new in v1.2].** Let $C=-A^W$, so that $C_{b,b+1}=\sqrt{(2b+1)(2B-2b-1)}/(2B)$ and $E^W_0=-\lambda_{\max}(C)$, and put

$$
w_b=\frac{\binom{2B}{2b}}{\binom Bb},\qquad v_b=\sqrt{w_b},\qquad Z_B=\sum_{b=0}^Bw_b .
\tag{10.6}
$$

Then for every $B\ge1$

$$
\boxed{\ \delta_B:=-\Bigl(1-\frac1B\Bigr)-E^W_0\ \ge\ \frac1{B\,Z_B}\ \ge\ \frac1{B\,2^{2B-1}}\ >\ 0\ }
\tag{10.7}
$$

This lower bound excludes superexponential decay. It does not by itself prove an exponentially small upper bound. The v1.2 audit supplied the matching enclosure (10.11); Theorem 18 below proves a sharper rational enclosure and the leading asymptotic expansion. The former one-sided inference is withdrawn.


*Proof.* The weights satisfy $w_{b+1}/w_b=(2B-2b-1)/(2b+1)$ and $w_0=w_B=1$. For $1\le b\le B-1$,

$$
\frac{(Cv)_b}{v_b}=C_{b-1,b}\sqrt{\frac{w_{b-1}}{w_b}}+C_{b,b+1}\sqrt{\frac{w_{b+1}}{w_b}}
=\frac{2b-1}{2B}+\frac{2B-2b-1}{2B}=\frac{B-1}B ,
$$

each square root cancelling the corresponding factor exactly, while at $b=0$ and $b=B$ only one term is present and the ratio is $(2B-1)/(2B)=\tfrac{B-1}B+\tfrac1{2B}$. Hence $\langle v,Cv\rangle=\tfrac{B-1}BZ_B+\tfrac1B$ and $\langle v,v\rangle=Z_B$, so by the Rayleigh principle $\lambda_{\max}(C)\ge\tfrac{B-1}B+\tfrac1{BZ_B}$, which is (10.7); the second inequality uses $\binom Bb\ge1$ and $\sum_b\binom{2B}{2b}=2^{2B-1}$. $\square$

The bound is close to sharp: an independent $170$-digit Sturm bisection gives $\delta_{16}=2.80541\times10^{-7}$ against the bound $2.71136\times10^{-7}$, and $\delta_{256}=2.38496\times10^{-81}$ against $2.38028\times10^{-81}$, while $(-\log\delta_B)/B$ falls from $0.943$ at $B=16$ to $0.725$ at $B=256$ — a decay rate, not a collapse (row V41). The correct statement is therefore: $-(1-1/B)$ is the semiclassical value, the true ground energy is strictly below it by an amount that is exponentially small in $B$ with an explicit lower bound, and the exact asymptotics are now supplied by T18. The value $2/B$ for the full-parent spectral gap is not asserted to be exact; V23 also does not prove an all-size asymptotic for that gap. T19 uses the proved auxiliary gap (10.10).

**Correction 2: a rate is not parent-independent without a normalisation (finding F08).** The ground-state tail rate $-B^{-1}\log(\pi^W_{B/2-h}/\pi^W_{B/2})$ does coincide with $I(h/B)$ to within $4\times10^{-4}/B$ at $x\le0.3$, $B=256$ (row V23) — closer to the entropy $I$ than the binomial itself, whose Stirling correction is $\tfrac1{2B}\log(1-4x^2)$ — and the continuum reason is that both parents have the semicircle symbol $a(\beta)=\sqrt{4\beta(1-\beta)}$, whose WKB rate $2\int_{1/2}^{1/2+x}\operatorname{arccosh}(1/a)\,d\beta$ equals $I(x)$ exactly. But a WKB identity between symbols is not a theorem about the spectrum of a finite matrix, and the exponential rate of the *gaps* is not determined by $\pi$ alone: replacing $A_B$ by $e^{-cB}A_B$ leaves $\pi$ and every $I$ untouched and shifts every gap exponent by $c$. Transporting the exponent interval of Theorem 2 to another parent therefore requires, at least: (i) a fixed energy normalisation, (ii) subexponential control of the full gap and of the conductances, (iii) concentration of the boundary resistance, and (iv) a non-cancellation condition on adjacent eigenvalue differences of the kind discussed in consequence (c) of Section 10.1. Under those conditions the interval is unchanged and the finite prefactors and two-boundary constants (10.2) must be recomputed from that parent's own $\pi$. v1.0 asserted the conclusion without (i)–(iv); the numerical coincidence of the rate at $B=256$ is retained as a VERIFIED finite fact and the general transfer remains [OPEN]; the specified compact-band Weyl transfer is proved in Theorem 19 below.


### 10.4 Exact rational enclosures and the leading Weyl correction — Theorem 18

This section incorporates the v1.2 audit's two-sided estimate and then goes beyond it. All matrices and energies here are dimensionless; multiplying the Hamiltonian by the fixed energy unit $J$ multiplies every energy by $J$. The matrix is exactly the Weyl parent of §10.3, not a fitted replacement.

Write $C=-A^W$, $\lambda_0=(B-1)/B$, and retain $w_b,v_b,Z_B$ from (10.6). Define

$$
V=\frac{P_0+P_B}{2B},\quad C_0=C-V,\quad
\pi_b^0=\frac{w_b}{Z_B},\quad W_b=\sum_{r=0}^bw_r,
$$
$$
p_b=\frac{2B-2b-1}{2B}\ (b<B),\quad p_B=0,
\qquad q_b=\frac{2b-1}{2B}\ (b>0),\quad q_0=0.
\tag{10.8}
$$

The symbol $\pi^0$ denotes the reversible weight of the boundary-corrected matrix. It is **not** silently identified with the true ground-state weight of $C$. Proposition 17 gives the exact identity $C_0v=\lambda_0v$; since this identity, rather than the $\delta_B$ bound of its statement, is what all of §§10.4–10.5 rests on, it is worth displaying separately. All off-diagonal entries $\sqrt{(2b+1)(2B-2b-1)}/(2B)$ are strictly positive, so $C_0$ is irreducible with non-negative off-diagonal part, and $v>0$; by Perron–Frobenius applied to $C_0+cI$ its positive eigenvector identifies $\lambda_0$ as the **largest** eigenvalue of $C_0$. Thus

$$
L=\lambda_0 I-D_v^{-1}C_0D_v,\qquad
(Lf)_b=p_b(f_b-f_{b+1})+q_b(f_b-f_{b-1})
\tag{10.9}
$$

is a reversible birth–death operator with stationary weight $\pi^0$.

**Gap and audit estimate.** For $B\ge2$, put $g_b=f_{b+1}-f_b$. Direct subtraction gives

$$
(\nabla Lf)_b=(p_b+q_{b+1})g_b-p_{b+1}g_{b+1}-q_bg_{b-1}.
$$

The diagonal minus the sum of the off-diagonal absolute values is
$p_b-p_{b+1}+q_{b+1}-q_b$: it equals $3/(2B)$ at the two ends and $2/B$ in the interior. A nonconstant eigenfunction has a nonzero difference. Applying its eigenvalue equation at a component of largest absolute value proves

$$
\operatorname{gap}(L)\ge g_B:=\frac3{2B}.
\tag{10.10}
$$

This argument also covers $B=2$, whose difference matrix has only the two end rows. For $B=1$ all claims below are checked directly. Weyl's eigenvalue inequality gives $\lambda_2(C)\le\lambda_0-1/B$. With $y=v/\sqrt{Z_B}$ and $a_B=1/(BZ_B)$,

$$
\langle y,Cy\rangle=\lambda_0+a_B,\qquad
\|(C-\lambda_0-a_B)y\|^2=\frac1{2B^2Z_B}-a_B^2.
$$

The Rayleigh and residual bounds give
$\delta_B-a_B\le[1/(2B^2Z_B)-a_B^2]/(a_B+1/B)\le a_B/2$,
and therefore the audit's valid all-size enclosure

$$
a_B\le\delta_B:=\lambda_{\max}(C)-\lambda_0\le\frac32a_B.
\tag{10.11}
$$

**Theorem 18 [PROVEN; rational enclosure and asymptotics].** Define the rational number

$$
\mathcal R_B=\frac12\sum_{b=0}^{B-1}
\frac{(1-2W_b/Z_B)^2}{w_bp_b}.
\tag{10.12}
$$

For $B\ge2$,

$$
0\le\mathcal R_B\le\frac{2B}{3}\left(1-\frac2{Z_B}\right),
$$
$$
\boxed{
\frac{a_B}{1-\dfrac{\mathcal R_B}{2B(1+1/Z_B)}}
\ \le\ \delta_B\ \le\
\frac{a_B}{1-\dfrac{\mathcal R_B}{2B}} .}
\tag{10.13}
$$

Both denominators are positive. For $B=1$, $\mathcal R_1=0$ and $\delta_1=a_1=1/2$, so the same enclosure holds by direct calculation. In addition,

$$
\mathcal R_B=1+\frac1B+O(B^{-2}),\qquad
\frac{\delta_B}{a_B}=1+\frac1{2B}+\frac3{4B^2}+O(B^{-3}),
\tag{10.14}
$$
$$
\boxed{
\delta_B=\frac{2}{\sqrt\pi B^{3/2}2^B}
\left(1+\frac5{8B}+\frac{105}{128B^2}+O(B^{-3})\right).}
\tag{10.15}
$$

In particular, the previously open equivalence $\delta_B\sim1/(BZ_B)$ and the exact exponential rate $\log2$ are settled. The subleading coefficients in (10.15) are analytic coefficients, not a regression fit.

*Proof of the rational Green formula and enclosure.* Work in the reflection-even subspace, which contains the positive top eigenvector of $C$. Let $e=(e_0+e_B)/\sqrt2$ and $P=yy^*$; on this subspace $V=ke e^*$ with $k=1/(2B)$. The scalar resolvent equation for the positive eigenvalue shift is obtained by multiplying
$(\lambda_0+\delta-C_0)u=ke\langle e,u\rangle$ by its inverse and then by $e^*$. Since $\langle e,u\rangle>0$, cancellation is legitimate and gives

$$
1=k\left(\frac{2}{Z_B\delta}+\mathcal R_B(\delta)\right),\qquad
\mathcal R_B(\delta)=\langle e,(I-P)(\lambda_0+\delta-C_0)^{-1}(I-P)e\rangle.
\tag{10.16}
$$

At zero the inverse is restricted to $y^\perp$. To evaluate it, transfer
$\xi=(I-P)e$ to $L$ by division by $y_b$. Its cumulative source flux through edge $b$ is

$$
\sum_{r=0}^b\pi_r^0\frac{\xi_r}{y_r}
=\sqrt{\frac2{Z_B}}\left(\frac12-\frac{W_b}{Z_B}\right).
$$

For a reversible path the solution of $Lf=h$ has gradient equal to this flux divided by the conductance $\pi_b^0p_b$. Summing the resulting energy, $\sum (\text{flux})^2/(\pi_b^0p_b)$, gives precisely (10.12). Thus $\mathcal R_B=\mathcal R_B(0)$. The gap bound implies

$$
\mathcal R_B(0)\le\frac{\|(I-P)e\|^2}{g_B}
=\frac{2B}{3}(1-2/Z_B),\qquad
\frac{\mathcal R_B}{1+\delta/g_B}\le\mathcal R_B(\delta)\le\mathcal R_B.
$$

Use $\delta\le3a_B/2$ from (10.11), so $\delta/g_B\le1/Z_B$, and solve (10.16) for $\delta$. This proves (10.13) without computing an eigenvalue. The two endpoints can separately be checked using rational LDL/Sturm arithmetic; C43 does this and rejects the false equality $\delta_B=a_B$.

*Proof of the asymptotics of $\mathcal R_B$.* Reflection pairs the conductance at $b$ with that at $B-1-b$. On the left half, $p_b$ is bounded below by a positive constant. The weights increase towards the centre, with

$$
w_0=1,\quad w_1=2B-1,\quad
w_2=\frac{(2B-1)(2B-3)}3,\quad
w_3=\frac{(2B-1)(2B-3)(2B-5)}{15}.
$$

Consequently the paired $b=2$ term is $O(B^{-2})$ and all terms with $3\le b\le B/2$ together are $O(B/w_3)=O(B^{-2})$. Vandermonde's sum contains the term $\binom Bb^2$, so $w_b\ge\binom Bb$ and $Z_B\ge2^B$. Thus the factors $(1-2W_b/Z_B)^2$ for $b=0,1$ differ from $1$ by exponentially small quantities. Hence

$$
\mathcal R_B=\frac1{p_0}+\frac1{w_1p_1}+O(B^{-2})
=1+\frac1B+O(B^{-2}).
$$

The gap estimate shows $\mathcal R_B(\delta_B)-\mathcal R_B=O(B\delta_B\mathcal R_B)$, an exponentially small quantity. Expanding the **proved** secular denominator in (10.16) gives (10.14).

*An exact normalizer remainder.* Put $H_B=2B\binom{2B}{B}/2^B$. The binomial identity

$$
(B-1)Z_B=(2B-1)Z_{B-1}-1,\quad Z_1=2
\tag{10.17}
$$

follows by summing
$w_{B,b}=\frac{2B-1}{2B-2}(w_{B-1,b}+w_{B-1,b-1})$ on the interior and treating both endpoints separately. Since $H_B/H_{B-1}=(2B-1)/(B-1)$,

$$
\frac{Z_B}{H_B}=1-\sum_{j=2}^B\frac1{(j-1)H_j}.
$$

Here $1/((j-1)H_j)=2^{-j}\mathrm B(j-1,3/2)$. Summing the nonnegative beta integrals on $[0,1]$ gives
$\sum_{j=2}^\infty 1/((j-1)H_j)=\frac12\int_0^1\sqrt{1-t}/(2-t)\,dt=1-\pi/4$.
The ratio of successive summands is $(j-1)/(2j+1)<1/2$. The first omitted term multiplied by $H_B$ equals $1/(2B+1)$, proving the useful exact bounds

$$
\frac1{2B+1}<Z_B-\frac\pi4H_B<\frac2{2B+1}.
\tag{10.18}
$$

The standard factorial expansion now gives
$Z_B=2^{B-1}\sqrt{\pi B}(1-1/(8B)+1/(128B^2)+O(B^{-3}))$;
the remainder (10.18) is exponentially small relative to this expression. Combining with (10.14) proves (10.15). The factorial expansion is a standard import, for example [NIST DLMF §5.11](https://dlmf.nist.gov/5.11), not a new result of this paper. $\square$

At $B=16$ the relative width of (10.13) is below $1.51\times10^{-7}$; at $B=32$ it is below $7.66\times10^{-13}$. These are widths between exact rational endpoints. The earlier audit's $[a_B,3a_B/2]$ has relative width $1/2$. This improvement is a reusable certificate and an asymptotic calculation, not a more optimistic reading of a floating determinant.

### 10.5 A proved transfer to the actual Weyl parent — Theorem 19

The obstacle in §10.3 can be removed for this parent without replacing its true ground state by a semiclassical approximation. The key is that $C_0$ and $C$ agree on every window $I=[l,u]$ with $1\le l\le u\le B-1$. Therefore, exactly,

$$
E_I^W/J=-\lambda_0+\lambda_D^0(I),\qquad
E_I^W-E_{I'}^W=J[\lambda_D^0(I)-\lambda_D^0(I')],
\tag{10.19}
$$

where $\lambda_D^0$ is the Dirichlet eigenvalue of (10.9). The true full-parent ground energy is $-J(\lambda_0+\delta_B)$; its shift $\delta_B$ cancels in every inter-window difference. The physical parent itself has not been changed. (v1.3 said that this cancellation "is the reason for using the boundary-corrected auxiliary matrix"; that is not right — $\delta_B$ cancels in inter-window differences whatever auxiliary matrix is used. The reason for $C_0$ is that it has a closed-form Perron pair $(\lambda_0,v)$, so $L$, $\pi^0$ and the conductances are explicit, whereas $C$ has none.)

**Theorem 19 [PROVEN; compact-window Weyl transfer].** Assume the compact-window condition (3.7), fixed $J>0$, and the exact Weyl edges of §10.3. Let

$$
r_L=\frac l{B-l},\quad r_R=\frac{B-u}{u},\quad
A_L^0=\frac{2l-1}{2B}\pi_l^0(1-r_L),\quad
A_R^0=\frac{2B-2u-1}{2B}\pi_u^0(1-r_R).
$$

with the endpoint convention $A_R^0:=0$ when $u=B$ and $A_L^0:=0$ when $l=0$. The convention is forced: at $u=B$ there is no right Dirichlet boundary to escape through, $r_R=0$, and the printed formula would return the negative value $-\pi_B^0/(2B)$, which is an artefact of extrapolating the two-boundary formula one site past the lattice end. At such a window the capacity sandwich below is applied with a single Dirichlet boundary and (10.20) reads $\lambda_D^0([l,B])=A_L^0[1+O(B^{-1})]$; row V49 checks this one-sided form directly against exact eigenvalues, with $\lambda_D^0/A_L^0=0.939104,\,0.959245,\,0.982274,\,0.991726$ at $B=60,120,240,480$ — consistent with $[1+O(B^{-1})]$ and converging from below.

Uniformly in these windows,

$$
\boxed{\lambda_D^0([l,u])=(A_L^0+A_R^0)[1+O(B^{-1})].}
\tag{10.20}
$$

For a fixed band $a>b>0$ with $a+b\le1/2$, $j/B\to a$, $w/B\to b$ and bounded integer rounding errors, supply the same sine coefficients as (2.3) but the exact Weyl sector ground vectors. Then the rate measure and coherence-weight limit of Theorem 2(b) hold unchanged. The first-loss bounds of Theorem 2 and the positive alignment bound of Theorem 15 apply to this Weyl band, with the same limiting ratio profile. In particular, for $(a,b)=(1/3,1/6)$,

$$
\kappa_W^-(z)\ge\frac14,\qquad
q_{\ell/2}\le\liminf\frac{\log JT^W_\ell}{B}
\le\limsup\frac{\log JT^W_\ell}{B}\le q_{4\ell/5}.
\tag{10.21}
$$

This theorem does not identify $\kappa_W$ with $\kappa_{\rm spin}$ or equate their exact first-loss exponents.

**The endpoint windows (repair of a v1.3 statement error).** v1.3 printed the hypothesis as $a+b<1/2$ and then applied the conclusion to $(a,b)=(\tfrac13,\tfrac16)$, for which $a+b=\tfrac12$ exactly. At that endpoint the two extreme sectors have windows $[B/3,B]$ and $[0,2B/3]$, which touch a lattice end, so the hypothesis $1\le l\le u\le B-1$ of (10.19) fails there and $C_0\ne C$ on those windows. The direction matters and v1.3 left it ambiguous: by the definition $C_0=C-(P_0+P_B)/(2B)$ of Section 10.3, the auxiliary matrix has the *smaller* endpoint diagonal entry, $C-C_0=(P_0+P_B)/(2B)\succeq0$, so on a window touching a lattice end the true parent lies **above** the auxiliary one in the Loewner order and its Dirichlet ground energy is the lower of the two. The conclusion survives, by the following lemma, which is the Weyl analogue of the endpoint split of Section 3.3.

**Lemma 19.1 [PROVEN; statement and proof as corrected by the v1.4 audit (F14-01, F14-02)].** Fix $0<\epsilon<\tfrac12$ and let $I=[l,B]$ with $\epsilon B\le l\le(1-\epsilon)B$. Retain $C$, $C_0$, $\lambda_0$, $\pi^0$, $p_b$ and $a^0_b=\pi^0_bp_b$ from (10.8)–(10.10), let $\nu$ and $\nu_0$ be the largest eigenvalues of $C$ and $C_0$ restricted to $I$, and put

$$
\lambda_D=\lambda_0-\nu,\qquad \lambda_D^0=\lambda_0-\nu_0,\qquad D=\nu-\nu_0,\qquad
b_*=\max\{l,\lceil B/2\rceil\},
$$

$$
R_*=\sum_{b=b_*}^{B-1}(a^0_b)^{-1},\qquad
A_*=\frac{\pi^0_BR_*}{B},\qquad
B_*=\frac{\pi^0_B}{B\,\pi^0_{b_*}} .
$$

Let $\psi$ be the unit Perron vector of $C$ on $I$ and $V=\psi_B^2/(2B)$. Whenever $A_*<1$,

$$
0\ \le\ D\ \le\ V\ \le\ \frac{A_*\lambda_D^0+B_*}{1-A_*},
\tag{10.19a}
$$

and, uniformly over the stated range of $l$,

$$
\frac{D}{\lambda_D^0}=O(B^{-1})+O\!\left(e^{-c_\epsilon B}\right).
\tag{10.19b}
$$

Reflection gives the same statement for $[0,u]$.

*Proof.* On $I$ the rank-one difference is $C_I-C_{0,I}=P_B/(2B)$. Testing each matrix against the other's Perron vector gives $0\le D\le V$. Put $\chi_b=\psi_b/\sqrt{\pi^0_b}$; in the ground-state representation of (10.9) its unperturbed Dirichlet energy is

$$
\mathcal E(\chi)=\lambda_D+V=\lambda_D^0-D+V\ \le\ \lambda_D^0+V .
$$

This is the inequality the argument needs. (The v1.4 text wrote $\mathcal E(\chi)\le\lambda_D^0+D$ instead, which would require $V\le2D$, and nothing proved that; the audit's finding F14-02 is that the printed step did not follow, not that a counterexample exists — the measured values have $V/D\approx1.01$.) The anchor $b_*$ lies in $I$ for every admissible $l$ — the v1.4 anchor $\lceil B/2\rceil$ does not when $l>B/2$, which was finding F14-01 — and normalisation together with the path Cauchy–Schwarz inequality gives

$$
\chi_{b_*}^2\le(\pi^0_{b_*})^{-1},\qquad
\chi_B^2\le2\chi_{b_*}^2+2R_*\,\mathcal E(\chi).
$$

Hence $V\le B_*+A_*(\lambda_D^0+V)$, and solving for $V$ proves (10.19a). No coordinate of one eigenvector is ever compared with a coordinate of another.

For (10.19b): $a^0_{B-1}=(2B-1)\pi^0_B/(2B)$ and $a^0_{b+1}/a^0_b=(2B-2b-3)/(2b+1)$, so in the last quarter of the chain the reciprocals $(a^0_b)^{-1}$ are dominated geometrically by the last one, the preceding term being smaller by a factor $1/(2B-3)$; thus $\pi^0_BR_*=1+O(B^{-1})$ uniformly in $b_*$ (measured $1.0458,\,1.0218,\,1.0106,\,1.00526$ at $B=24,48,96,192$ for $b_*=\lceil B/2\rceil$, row V49) and $A_*=O(B^{-1})<1$ for large $B$. For $B_*/\lambda_D^0$ without assuming $l<B/2$: extending a normalised Dirichlet test function by zero, its mean squared is at most $\pi^0(I)$, so its variance is at least $\pi^0(I^c)$, and the gap bound (10.10) gives $\lambda_D^0\ge\tfrac3{2B}\pi^0([0,l-1])$. If $l\le B/2$ then $\pi^0_{b_*}\asymp B^{-1/2}$ and $\pi^0(I^c)\ge\pi^0_{l-1}$; if $l>B/2$ then $\pi^0(I^c)$ is bounded below by a positive constant and $b_*=l$. In both cases the exact factorial form of $\pi^0$ and Stirling's bounds give $\pi^0_B/(B\pi^0_{b_*}\lambda_D^0)\le\operatorname{poly}(B)\,e^{-c_\epsilon B}$, and a smaller $c_\epsilon$ absorbs the polynomial. Substituting into (10.19a) gives (10.19b). $\square$

Row V52 evaluates the finite bound (10.19a) at $(B,l)=(24,8),(24,16),(48,16),(48,32)$ in $90$-digit arithmetic; the two windows with $l>B/2$ are exactly the ones on which the v1.4 anchor was outside the window. What the corrected lemma delivers is the relative error $O(B^{-1})$ that (10.20) already carries, and no more. The measured size is exponentially smaller — $D/\lambda_D^0=6.67\times10^{-8},\,6.30\times10^{-15},\,1.41\times10^{-28},\,1.92\times10^{-55}$ at $B=24,48,96,192$ for $l=\lceil B/3\rceil$ — and that stronger statement is **not** claimed as proved. The lemma's history is recorded in Appendix R3: its v1.4 draft claimed $O(e^{-cB})$ through a false displayed inequality, the first repair claimed $O(B^{-2})$ through a false resistance estimate, the second repair proved $O(B^{-1})$ but with the anchor and the energy inequality just described, and the present statement is the v1.4 audit's.

Row V49 evaluates the endpoint discrepancy at $B=24,48,96$: the discrepancy between $E^W_I$ and $-\lambda_0+\lambda_D^0(I)$ at the endpoint window is $4.7\times10^{-10}$, $7.4\times10^{-18}$ and $7.8\times10^{-33}$, against level spacings $4.0\times10^{-3}$, $6.0\times10^{-4}$ and $2.8\times10^{-5}$. The relative sizes are $1.175\times10^{-7}$, $1.233\times10^{-14}$, $2.79\times10^{-28}$, whose logarithms divided by $B$ are $-0.6649,\,-0.6673,\,-0.6608$: the decay is **exponential**, not superexponential, and an earlier draft's word "superexponentially" was wrong. These three slopes drift rather than agree, as they must: the asymptotic exponential rate here is $\log2-I(1/6)=0.6365$, and the finite-$B$ slopes are contaminated by a $B^{-3/2}$ prefactor and by the polynomial decay of the level spacing, so a three-point fit cannot resolve the limit. The absolute discrepancy follows the mechanism $\nu(I)-\nu_0(I)\sim\pi_B^0/(2B)$ (one factor of the far-end weight, with an essentially flat ground function) with $\pi_B^0\sim(2/\sqrt{\pi B})2^{-B}$: the measured ratios to $2^{-B}/(2B)$ are $0.3787,\,0.1993,\,0.1184,\,0.0817$ at $B=24,48,96,192$, and multiplying by $\sqrt B$ gives $1.855,\,1.381,\,1.160,\,1.132\to2/\sqrt\pi=1.1284$. (A draft claimed these matched $2^{-B}/(2B)$ "to within a factor 3", which is false at $B\ge96$ and misses the $B^{-1/2}$; note also that the bulk expansion (10.23) is **not** valid at the lattice edge $b=B$, where it is short by a factor $\sqrt2$ — $\pi_B^0/[2^{-B}\sqrt{2/(\pi B)}]\to\sqrt2$ — which is exactly where that factor went.) The lemma as proved requires only $O(B^{-1})$, so nothing downstream depends on any of this. One further measured fact, recorded because a v1.4 draft had assumed the opposite: the spectral gap of $L$ on this window is not bounded below — it is $0.10393,\,0.046840,\,0.021313,\,0.010420$ at $B=24,48,96,192$, i.e. $\operatorname{gap}\cdot B\to2$, so the perturbation $\|C-C_0\|=1/(2B)$ is a quarter of the gap and no eigenvector perturbation argument is available, which is why the lemma is proved through the perturbed ground function alone.

*Proof of Theorem 19.* The conductances are $a_b^0=\pi_b^0p_b$. They satisfy

$$
a_{l-1}^0=\frac{2l-1}{2B}\pi_l^0,\qquad
\frac{(a_{l+s}^0)^{-1}}{(a_{l-1+s}^0)^{-1}}
=\frac{2l+2s-1}{2B-2l-2s-1}.
\tag{10.22}
$$

The proof of (3.10), with this explicit ratio, gives
$R_L^0=(a_{l-1}^0)^{-1}[(1-r_L)^{-1}+O(B^{-1})]$ and the reflected right formula. Apply the finite capacity sandwich of Proposition 12 to $C_0$, using (10.10). The ratio between its Dirichlet eigenvalue and its two-boundary capacity tends to $1$ exponentially fast, because $\pi^0$ has exponentially small compact tails and $\pi_{B/2}^0\asymp B^{-1/2}$. This proves (10.20). C44 checks the exact transform and both finite capacity bounds directly against isolated matrix eigenvalues.

For $s=b_0/B$ in a compact subinterval of $(0,1)$, the factorial ratios and (10.18) give, uniformly,

$$
\pi_{b_0}^0=\sqrt{\frac2{\pi B}}\,
e^{-BI(s-1/2)}[1+O(B^{-1})],\qquad
I(x)=\log2+(1/2-x)\log(1/2-x)+(1/2+x)\log(1/2+x).
\tag{10.23}
$$

Here $I$ is even. In particular, with $\pi^{\rm spin}_{b_0}=2^{-B}\binom B{b_0}$,

$$
\frac{\pi_{b_0}^0}{\pi^{\rm spin}_{b_0}}
=2\sqrt{s(1-s)}[1+O(B^{-1})].
\tag{10.24}
$$

For $k>0$ a positive macroscopic distance from the band centre, the left boundary is nearer the centre and dominates the right exponentially. Write $s=l/B=1/2-x$, $x=j/B-k/B$. Moving from $k$ to $k+1$ multiplies its leading term by $(1-s)/s+O(B^{-1})$. This ratio is uniformly bounded above $1$, so subtraction preserves a relative $O(B^{-1})$ error. In particular,

$$
\frac{\Delta_k^W}{J}
=\frac{8x^2}{1+2x}\sqrt{\frac2{\pi B}}
e^{-BI(x)}[1+O(B^{-1})],\qquad
\frac{\Delta_k^W}{\Delta_k^{\rm spin}}
=\sqrt{1-4x^2}[1+O(B^{-1})].
\tag{10.25}
$$

Both assertions use the same indices and fixed energy normalization in the two parents; explicitly, the spin gaps are measured as in (2.2), $\Delta^{\rm spin}_k=[\widetilde\lambda(I_{k+1})-\widetilde\lambda(I_k)]/\sqrt{B(B+2)}$, whereas §3.2's $A_L=l\pi_l(1-r_L)$ is written in Ehrenfest units with full gap $2$; the conversion factor $B/\sqrt{B(B+2)}=1+O(B^{-1})$ is exactly what turns $\pi^0_l/\pi^{\rm spin}_l=2\sqrt{s(1-s)}$ into the $\sqrt{1-4x^2}$ printed here. A reader who inserts §3.2's $A_L$ literally will find a spurious factor $B$. Reflection supplies the other half of the band. A vanishing macroscopic strip around $k=0$ may be excluded for the rate-measure limit; its sine-weight mass tends to zero as the strip shrinks. No diffusive adjacent-difference remainder is inferred from this argument.

For completeness, coherence weights also transfer. Extend a normalized Dirichlet ground function by zero. Its Dirichlet energy is exponentially small, so (10.10) makes its variance in $L^2(\pi^0)$ exponentially small up to a polynomial factor. Positivity fixes its sign, normalization fixes its mean near $1$, and multiplication by $\sqrt{\pi^0}$ shows that all sector vectors are close to the same full positive vector. Their equal-coordinate overlaps consequently tend uniformly to $1$. Multiplication by the supplied sine coefficients gives exactly the density (4.6). Equations (10.23)–(10.25) now give the rate pushforward and the fast-set Hadamard ratios required by Theorems 2 and 14. This proves (10.21). $\square$

The newly closed obligation is the transfer to the **specified Weyl matrix on compact bands**. General parents, endpoint/diffusive Weyl bands, and action-derived physical preparation remain outside this theorem. The proof uses standard capacity and rank-one perturbation methods; its added content is the exact boundary correction, computable Green quantity, non-cancellation, and explicit inter-parent gap comparison.

### 10.6 The diffusive window: an Ornstein–Uhlenbeck limit and a $B^{3/2}$ first-loss law — Theorem 22

Every version of this paper from v1.0 on has carried an open obligation at the diffusive scale $h=K\sqrt B$. v1.0 asserted a "third time scale" $JT\sim B^{3/2}e^{2K^2}$; the v1.1 audit showed that the capacity-to-eigenvalue step of Theorem 10 is unavailable there, and v1.2 withdrew the sentence, leaving two questions open: a uniform remainder for **adjacent** eigenvalue differences in that range, and a first-loss law. Both are settled here, and the answer explains why the earlier attempts failed.

**The scaling.** Write $b=\tfrac B2+\tfrac{\sqrt B}2y$, so that a shift of one lattice site is a shift of $2/\sqrt B$ in $y$. For smooth $f$ the Ehrenfest generator $(\mathcal Lf)(b)=(B-b)[f(b)-f(b+1)]+b[f(b)-f(b-1)]$ satisfies, uniformly on compact $y$-sets,

$$
\mathcal Lf=-2f''(y)+2yf'(y)+O(B^{-1/2}) ,
\tag{10.26}
$$

the Ornstein–Uhlenbeck operator $\mathcal A=-2(\partial_y^2-y\partial_y)$, which is self-adjoint and non-negative in $L^2(e^{-y^2/2}dy)$ and whose spectrum on the whole line is $\{0,2,4,\ldots\}$. The full Ehrenfest spectrum is the finite set $\{0,2,\ldots,2B\}$, of which the limit operator sees only the bottom; the agreement there is a consistency check, not a necessity. For $c\in\mathbb R$ and $K>0$ let $\Lambda(c;K)$ denote the lowest Dirichlet eigenvalue of $\mathcal A$ on the interval $(c-2K,\,c+2K)$. It is real analytic in $c$ and even, and — by Lemma 22.1 below, supplied by the v1.4 audit — convex with $\Lambda'(c;K)>0$ for $c>0$ and $\Lambda''(0;K)>0$; the v1.4 text had left the sign and the non-vanishing of the centre curvature as numerical observations, which was finding F14-03 of that audit, since the centre ratios in (iii) below require $\Lambda''(0;K)\ne0$. At $K=3/2$, $\Lambda(0;K)=0.04789260$ and $\Lambda''(0;K)=0.26435$ (Richardson-extrapolated from a uniform finite-difference discretisation; in each the last printed digit is the first uncertain one, and row V50's own coarser solver returns $0.0478925$ and $0.264362$). For large $K$ **at the centre** it obeys the Kramers law $\Lambda(0;K)=\bigl(4K\sqrt{2/\pi}+o(1)\bigr)e^{-2K^2}$ — the ratio $\Lambda(0;K)/[4K\sqrt{2/\pi}\,e^{-2K^2}]$ runs $0.9005,\,0.9276,\,0.9559,\,0.9704$ at $K=1.5,2,2.5,3$. This is **not** uniform in $c$: the two-sided Kramers form is $\Lambda(c;K)\approx\sqrt{2/\pi}\,[L_+e^{-L_+^2/2}+L_-e^{-L_-^2/2}]$ with $L_\pm=2K\mp c$, so $\Lambda(c;K)$ carries an extra factor $e^{2Kc}$ and $\Lambda(c;K)/(Ke^{-2K^2})$ is unbounded in $K$ at any fixed $c\ne0$ ($34.6,\,106.4,\,311.0$ at $c=1$, $K=2,2.5,3$). A draft of this section printed "$\Lambda(\cdot;K)=\Theta(Ke^{-2K^2})$" without the restriction to $c=0$; that is corrected here, and the correction propagates to the $K$-dependence of the first-loss constant below.

**Lemma 22.1 [DERIVED; analytic completion, supplied by the v1.4 audit].** For every finite $K>0$, $\Lambda(\cdot;K)$ is even and real analytic, convex, and $\Lambda'(c;K)>0$ for $c>0$. Moreover

$$
\Lambda''(0;K)\ \ge\ 1-\bigl(1+\Lambda(0;K)\bigr)^{-2}\ >\ 0 .
\tag{10.26a}
$$

*Proof.* The unitary ground-state transformation turns $\mathcal A$ on $(c-2K,c+2K)$ into the Schrödinger operator $H_c=-2\partial_x^2+(x+c)^2/2-1$ on $(-2K,2K)$; simplicity of the ground eigenvalue and analytic perturbation give analyticity, reflection gives evenness. Convexity under translation of the window is the Gaussian eigenvalue Brunn–Minkowski inequality, Theorem 1.2 of Colesanti–Francini–Livshyts–Salani (arXiv:2407.21354), applied to intervals of equal length; the factor $2$ between their eigenvalue and ours preserves convexity. For the centre curvature let $\lambda=\Lambda(0;K)$, $L=2K$, and let $g$ be the positive even Ornstein–Uhlenbeck ground function on $(-L,L)$. Integrating the eigenvalue equation $(e^{-x^2/2}g')'=-\tfrac\lambda2e^{-x^2/2}g$ from $0$ gives $g'(x)=-\tfrac\lambda2e^{x^2/2}\int_0^xe^{-y^2/2}g<0$ for $x>0$; with $v=-\log g$, $v''=(v')^2+xv'+\lambda/2\ge\lambda/2$ on both sides. The normalised Schrödinger ground density $\psi^2=g^2e^{-x^2/2}$ has logarithmic potential $U=x^2/2+2v$ with $U''\ge1+\lambda$, so the weighted Poincaré inequality gives $\operatorname{Var}_{\psi^2}(x)\le(1+\lambda)^{-1}$ and the ground-transformed operator has spectral gap at least $2(1+\lambda)$ (both follow from $\int(Lf)^2e^{-U}=\int[(f'')^2+U''(f')^2]e^{-U}$ for $L=-\partial_x^2+U'\partial_x$, the boundary terms vanishing because the density vanishes quadratically at the endpoints). Second-order perturbation of $H_c$ at $c=0$, with $\partial_cH=x+c$ and $\partial_c^2H=1$, gives $\Lambda''(0)=1-2\langle x\psi,(H_0-\lambda)^{-1}_{\psi^\perp}x\psi\rangle\ge1-2\operatorname{Var}(x)/[2(1+\lambda)]\ge1-(1+\lambda)^{-2}$. Finally convexity makes $\Lambda'$ non-decreasing; if it vanished at some $c_0>0$, evenness and convexity would make $\Lambda$ constant on $[-c_0,c_0]$ and hence everywhere by analyticity, contradicting $H_c\ge(|c|-2K)^2/2-1$ for $|c|>2K$. $\square$

At $K=3/2$ the bound (10.26a) gives $\Lambda''(0)\ge0.0893$ against the value $0.26435$; the bound is what the theorem needs, not the value. Row V50 checks (10.26a) at $K=1,1.5,2$ (values $\Lambda''(0;K)=0.7578,\ 0.2644,\ 0.02503$ against the bounds $0.5471,\ 0.0893,\ 0.00396$). At $K=3$ both sides are below $10^{-5}$ — $\Lambda(0;3)\approx1.4\times10^{-7}$, so the bound is $\approx2.8\times10^{-7}$ while $\Lambda''(0;3)\approx(2K)^2\Lambda(0;3)\approx5\times10^{-6}$ (the wall-dominated regime, $\Lambda(c;K)\approx\Lambda(0;K)\cosh2Kc$; numerically $4.8\times10^{-6}$) — and the second difference of the discretised eigenvalue is not resolved to that level; the $K=3$ values are recorded in the row but do not enter its verdict.

**Theorem 22 [PROVEN; new in v1.4, corrected after the v1.4 audit (F14-03, F14-04, F14-05)].** Let $B\to\infty$ through **even** integers, fix $0<\kappa<K<\infty$ and $J>0$, and put $j=\lceil K\sqrt B\rceil$, $w=\lfloor\kappa\sqrt B\rfloor$, $c_k=2k/\sqrt B$. Build the band of Section 2 with these $j,w$ and the sine coefficients (2.3). In this section $\kappa$ is the fixed **bandwidth parameter** of the band and is not the alignment capacity $\kappa^\pm(z)$ of Section 9. Then, with $\widetilde\lambda_k$ the Dirichlet ground eigenvalue of the sector window $I_k$ in Ehrenfest units:

(i) *(profile)* $\widetilde\lambda_k\to\Lambda(c_k;K)$ uniformly in $|k|\le w$;

(ii) *(adjacent differences)*
$$
\frac{\sqrt B}2\bigl(\widetilde\lambda_{k+1}-\widetilde\lambda_k\bigr)\longrightarrow\Lambda'(c_k;K) ,
\tag{10.27}
$$
uniformly on **all** of $|c_k|\le2\kappa$. Here $\Lambda'$ is odd, so $\Lambda'(c;K)$ and $c$ have the same sign; the band is symmetric, $\widetilde\lambda_k=\widetilde\lambda_{-k}$ exactly, and $\Delta_0/\Delta_{-1}=-1$. A draft of this section printed the limit as "$\Lambda'(c_k;K)>0$" over the whole range $|k|\le w$, which is false on the negative half. Strict positivity of $\Lambda'$ on $(0,2\kappa]$ is Lemma 22.1 and is used in (iv) below; the positivity of $\Lambda''(0;K)$ is (10.26a) and is what makes the centre statements of (ii) and (iii) non-vacuous. The restriction $|c_k|\ge\delta>0$ is needed only if (10.27) is read as a statement about *relative* error, since $\Lambda'$ vanishes at the centre; there $\Lambda'(0;K)=0$ by symmetry and $\widetilde\lambda_1-\widetilde\lambda_0=\bigl(2\Lambda''(0;K)+o(1)\bigr)B^{-1}=\Theta(B^{-1})$, the first-order term being absent because the interpolating profile is **exactly** even, not merely asymptotically so (see the proof);

(iii) *(frequencies)* in the physical units of (2.2), with the energy unit $J$ restored, the band frequencies are
$$
\frac{\Delta_k}{J}=\frac{2\Lambda'(c_k;K)}{B^{3/2}}+o\bigl(B^{-3/2}\bigr)\ \ \text{uniformly in }|k|\le w,
\qquad
\frac{\Delta_k}{J}=\frac{2\Lambda'(c_k;K)}{B^{3/2}}\bigl(1+o(1)\bigr)\ \ \text{uniformly on }|c_k|\ge\delta>0 ,
\qquad
\frac{\Delta_0}{J}=\bigl(2\Lambda''(0;K)+o(1)\bigr)B^{-2};
$$
the distinction is not cosmetic, since at $k=0$ the leading term is identically zero and only the absolute form can hold there. Away from the centre the frequencies are all of the same order, with $\Delta_{k+1}/\Delta_k\to1$ uniformly on $|c_k|\ge\delta>0$. At the centre they are **not**: there $\Lambda'(c_k)\to0$, the correct size is $\Theta(B^{-2})$ with the constant $2\Lambda''(0;K)>0$ of Lemma 22.1, and for each fixed $k\ge0$ the ratio is $\Delta_{k+1}/\Delta_k\to(2k+3)/(2k+1)$ — in particular $\Delta_1/\Delta_0\to3$ and $\Delta_2/\Delta_1\to5/3$, not $1$. These are limits for fixed $k$; the finite-$B$ ratios exceed them slightly (the v1.4 sentence "adjacent ratios stay bounded by $3$ throughout" is **withdrawn**, being contradicted by the paper's own values $3.00456,3.00108,3.00026$ — finding F14-04), and the spread $\max_k\Delta_k/\min_k|\Delta_k|$ across the band grows like $\Theta(\sqrt B)$. A draft of this section asserted $\Delta_{k+1}/\Delta_k\to1$ with no restriction on $k$, contradicting its own part (ii); exact diagonalisation at $K=3/2$, $\kappa=3/4$ gives $\Delta_1/\Delta_0=3.00456,\,3.00108,\,3.00026$, $\Delta_2/\Delta_1=1.67172,\,1.66787,\,1.66696$ and $\Delta_0B^2=0.48608,\,0.50710,\,0.51782$ at $B=1600,6400,25600$, against $2\Lambda''(0;K)=0.52870$ (row V50);

(iv) *(first-loss law)* with $\tau=Jt/B^{3/2}$ and $\rho(s)=\tfrac12(1+\cos\pi s)$ the density (4.6),
$$
\frac{M_B(t)}{\Gamma_B}\longrightarrow\mathfrak M(\tau)=\int_{-1}^{1}\rho(s)\Bigl[1-\cos\bigl(2\Lambda'(2\kappa s;K)\,\tau\bigr)\Bigr]ds
\tag{10.28}
$$
uniformly on compact $\tau$-sets, where $M_B=\Gamma_B-S_B$ is the **absolute** loss of §4.1. In particular $JT_\ell=\Theta(B^{3/2})$ for every fixed $0<\ell<1$. Define the first contact $\tau_\ell=\inf\{\tau\ge0:\mathfrak M(\tau)\ge\ell\}$. If this first contact is a strict crossing — every right neighbourhood of $\tau_\ell$ contains a point with $\mathfrak M>\ell$ — then
$$
\boxed{\ \frac{J\,T_\ell}{B^{3/2}}\longrightarrow\tau_\ell .\ }
\tag{10.29}
$$
No global inverse of the oscillatory function $\mathfrak M$ is assumed; the v1.4 notation $\mathfrak M^{-1}(\ell)$ meant this first contact and is replaced (finding F14-05).

*Proof.* (i) On the window $I_k$ the Dirichlet form of $\mathcal L$ with weight $\pi_b=2^{-B}\binom Bb$ converges, after the substitution $b\mapsto y$ and the local central limit theorem $\pi_b=\sqrt{2/(\pi B)}\,e^{-y^2/2}[1+O(B^{-1/2})]$ uniformly on compact $y$-sets, to the Dirichlet form of $\mathcal A$ with weight $e^{-y^2/2}$ on $(c_k-2K,c_k+2K)$. Both forms have discrete spectrum with a uniform spectral gap, the test functions are the same after interpolation, and the $y$-mesh is $2/\sqrt B$; the standard Rayleigh–Ritz two-sided comparison gives convergence of the lowest eigenvalue, uniformly in $k$ because the endpoints vary in a compact set. (ii) This is the step at which the v1.4 draft was wrong, and the repair is the substance of the theorem. The draft argued that "$\widetilde\lambda_{k+1}$ and $\widetilde\lambda_k$ are the values of the same limit profile at $c_k+2/\sqrt B$ and $c_k$ up to $o(B^{-1/2})$". They are not: the error in (i) is itself exactly of order $B^{-1/2}$ with a non-zero coefficient. Numerically $\sqrt B\,[\widetilde\lambda_k-\Lambda(c_k;K)]$ tends to $\approx-0.257$ at $c=0$ and to $\approx-1.15$ at $c=1.5$ (values $-0.2349,-0.2456,-0.2513,-0.2541$ and $-1.0864,-1.1168,-1.1323,-1.1402$ at $B=400,1600,6400,25600$), so at $B=25600$ the error in (i) is $-1.59\times10^{-3}$ while the quantity (ii) extracts is $2.02\times10^{-5}$ — a factor $79$ the wrong way. Rayleigh–Ritz gives convergence of eigenvalues and never, by itself, convergence of difference quotients. The correct argument is that the whole discrete family is analytic in the window centre, so that Vitali's theorem upgrades pointwise convergence to convergence of derivatives.

Fix $B$ and $j$ and write the window in relative coordinates, $I_\mu=\{\,\tfrac B2+\mu+r:\ |r|\le j\,\}$. In the $\pi$-symmetrised representation the Dirichlet matrix on $I_\mu$ has constant diagonal $B$ and off-diagonal entries $-\sqrt{(B-b)(b+1)}$ at $b=\tfrac B2+\mu+r$. These entries are **algebraic** in $\mu$ — no Gamma continuation is needed, and none is used: $-\sqrt{(B-b)(b+1)}$ with $b=\tfrac B2+\mu+r$ extends directly to a function holomorphic on $\{|\mathrm{Re}\,\mu|\le(\tfrac12-\epsilon)B,\ |\mathrm{Im}\,\mu|\le\eta B\}$, since the argument of the square root stays in a sector away from the negative reals there. (Take $B$ even, so that $\tfrac B2+m+r$ is a lattice site; for odd $B$ replace $\tfrac B2$ by $\lfloor\tfrac B2\rfloor$ throughout, which only shifts $\mu$ by $\tfrac12$.) Call the resulting matrix $M_B(\mu)$; it is a holomorphic family of type (A) in Kato's sense, and $M_B(m)$ is the sector matrix of $I_m$ for every integer $m$. At real $\mu$ the matrix is a nonpositive-off-diagonal Jacobi matrix, so its lowest eigenvalue is simple by Perron–Frobenius. Its spectral gap is bounded below uniformly: the min–max characterisation transfers together with the Dirichlet forms of (i) — the same two-sided form comparison applied to the second min–max level, not only the first — so $\widetilde\lambda^{(1)}-\widetilde\lambda^{(0)}\to\Lambda^{(1)}(c;K)-\Lambda(c;K)\ge g(K)>0$ uniformly in $c$ on compact sets (measured $2.2883,\,2.3045,\,2.3128$ at $B=1600,6400,25600$). A simple eigenvalue with a gap $\ge g$ stays simple and holomorphic on a complex disc of radius $\ge g/(2\|\partial_\mu M_B\|)$. Here the derivative is small: with $f(b)=(B-b)(b+1)$ one has $\partial_b\bigl(-\sqrt f\bigr)=(2b-B+1)/(2\sqrt f)$, which on the window $|b-\tfrac B2|\le j+\kappa\sqrt B=O(\sqrt B)$ is $O(\sqrt B)/O(B)=O(B^{-1/2})$, so $\|\partial_\mu M_B\|=O(B^{-1/2})$ and the disc of holomorphy has radius $\Omega(\sqrt B)$ in $\mu$ — that is, a **fixed** radius in the rescaled variable $c=2\mu/\sqrt B$. Setting

$$
\Phi_B(z):=\widetilde\lambda\bigl(M_B(z\sqrt B/2)\bigr),
$$

$\Phi_B$ is holomorphic and uniformly bounded on a complex neighbourhood $D$ of the real interval $[-2\kappa-\delta_0,\,2\kappa+\delta_0]$ whose width does not depend on $B$, and $\Phi_B(c_m)=\widetilde\lambda_m$ at the lattice points $c_m=2m/\sqrt B$. For **every** real $c$ in that interval — not only the lattice values — the argument of (i) applies verbatim, because the symmetrised matrix is algebraic in $\mu$ and obeys the same local expansion at a non-integer shift as at an integer one; hence $\Phi_B\to\Lambda(\cdot;K)$ pointwise on a set with limit points in $D$. By Vitali's convergence theorem the convergence is locally uniform on $D$, and hence $\Phi_B'\to\Lambda'$ and $\Phi_B''\to\Lambda''$ locally uniformly on the real interval, with $\sup_D|\Phi_B''|=O(1)$ by the Cauchy estimates. Therefore

$$
\widetilde\lambda_{k+1}-\widetilde\lambda_k=\Phi_B(c_{k+1})-\Phi_B(c_k)
=\frac2{\sqrt B}\Phi_B'(c_k)+O(B^{-1})
=\frac2{\sqrt B}\bigl[\Lambda'(c_k;K)+o(1)\bigr],
$$

uniformly in $|c_k|\le2\kappa$, which is (10.27). Evenness of $\Lambda$ gives $\Lambda'(0)=0$. At the centre one needs more than that: the first-order term $\Phi_B'(0)c_1$ would dominate the second unless it is known to be $O(B^{-1/2})$, and $\Phi_B'(0)\to\Lambda'(0)=0$ alone does not give this. It is in fact **exactly zero** for every $B$, because $\Phi_B$ is an even function of $\mu$: the reflection $b\mapsto B-b$ maps $I_\mu$ onto $I_{-\mu}$ and leaves $\sqrt{(B-b)(b+1)}$ invariant, so $M_B(-\mu)$ is the reversal of $M_B(\mu)$ and has the same spectrum. (Checked at non-integer arguments: $|\Phi_B(\mu)-\Phi_B(-\mu)|<5\times10^{-12}$ at $\mu=0.37,1.5,2.75,7$ for $B=1600$.) Hence $\Phi_B'(0)=0$ identically and $\widetilde\lambda_1-\widetilde\lambda_0=\tfrac12\Phi_B''(0)c_1^2+O(c_1^4)=2\Lambda''(0;K)B^{-1}(1+o(1))$, which also yields $\Delta_1/\Delta_0\to3$ and $\Delta_{k+1}/\Delta_k\to(2k+3)/(2k+1)$.

What (10.27) does **not** require is any statement about the sign of $\Lambda'$, since (iv) sees it only through the even function $1-\cos$. For the record, the sign is as one expects and the formula for it is exact but is not what a draft of this proof said. Translating the window by $c$ is the same as fixing the interval $(-2K,2K)$ and replacing the weight $e^{-y^2/2}$ by $e^{-(y+c)^2/2}=e^{-y^2/2}e^{-cy-c^2/2}$; Hellmann–Feynman then gives $\Lambda'(c)=\Lambda[\langle y\rangle_{g^2w}-\langle y\rangle_{2g'^2w/\Lambda}]$, which collapses — by the identity $\mathcal Ay=2y$, integrated by parts against $yg$ — to the **mean** $\int y\,d\varrho_c$ of the normalised ground density, not to a covariance. Numerically at $K=3/2$, $c=1$: $\Lambda'=0.3253825$ by finite differences and $\int y\,d\varrho_c=0.325378$. Its positivity for $c>0$ is *not* explained by the window being pulled towards the near barrier — that would push the mean the other way; it comes from the opposite effect, that the near (left) barrier truncates the Gaussian more severely and the surviving mass therefore sits at positive $y$. This is verified on a grid for $K=3/2$ and $K=3$ and is used nowhere in the proof of (ii). The sign itself, $\Lambda'(c;K)>0$ for $c>0$, is no longer only an observation: Lemma 22.1 proves it for every finite $K$ (the v1.5 sentence "no general proof supplied" was stale, audit finding F15-07); only the *mechanism* described in this paragraph — the mean of the truncated ground density — is the numerical remark. (ii) is thereby proved.

(iii) Divide by $\sqrt{B(B+2)}$ as in (2.2); the ratio statements follow from (ii) away from the centre and from the second-order expansion at it, since $\Delta_k\propto\Lambda(c_{k+1})-\Lambda(c_k)=\tfrac12\Lambda''(0)(c_{k+1}^2-c_k^2)(1+o(1))$ there, whence $\Delta_{k+1}/\Delta_k\to(2k+3)/(2k+1)$. (iv) Write $s_k$ for the sine coefficients (2.3), to avoid a collision with the window centres $c_k=2k/\sqrt B$ of the statement. The overlaps $\langle\psi_k,\psi_{k+1}\rangle$ tend to $1$ for two reasons that must both be accounted: the ground projection of $M_B(\mu)$ is holomorphic on $D$ with $O(1)$ derivative, which controls the change of *profile* between centres distant $2/\sqrt B$; and the physical overlap also contains a one-site **lattice shift** in the relative coordinate, $\langle\psi_k,\psi_{k+1}\rangle=\sum_r\psi^{(k)}(r+1)\psi^{(k+1)}(r)$, whose cost is $\tfrac12\|\psi-S\psi\|^2\approx\tfrac12h^2\!\int(g')^2$ with $h=2/\sqrt B$ and $g$ the limit profile — that is, $O(B^{-1})$, and at the band centre it is the dominant term ($1.9\times10^{-6}$ predicted against $1-\langle\psi_0,\psi_1\rangle=3.09\times10^{-6}$ measured at $B=25600$). Both are $O(B^{-1})$, so $\omega_k=s_ks_{k+1}\langle\psi_k,\psi_{k+1}\rangle=\rho(k/w)/w\cdot(1+o(1))$ and $\Gamma_B\to1$ (measured: $\langle\psi_k,\psi_{k+1}\rangle=0.9999969,\,0.9999933,\,0.9999839$ at $k=0,w/2,w-1$ for $B=25600$). Because (10.27) now holds uniformly on the **whole** band and not only on $|c_k|\ge\delta$, we have $\Delta_kt=2\Lambda'(c_k)\tau+o(1)$ uniformly in $|k|\le w$, and $\sum_k\omega_k[1-\cos\Delta_kt]$ is a Riemann sum for (10.28) with mesh $1/w=\Theta(B^{-1/2})$ and a uniformly Lipschitz integrand on compact $\tau$-sets. (Had (ii) been available only for $|c_k|\ge\delta$, as the draft stated it, the central strip would still be harmless — $1-\cos$ is $O(\delta^2)$ there and carries sine-weight mass $O(\delta)$ — but the proof would have had to say so, and it did not.) The ratio statement of (iii) at the centre uses $\Lambda''(0;K)\ne0$, which is (10.26a). For the two-sided order $JT_\ell=\Theta(B^{3/2})$: the rescaled frequencies $2\Lambda'(c_k)$ are uniformly bounded and $1-\cos x\le x^2/2$, which gives a positive lower bound on $JT_\ell/B^{3/2}$; and the Cesàro time average of $\mathfrak M$ tends to $\int\rho=1$ because $\Lambda'(2\kappa s)\ne0$ for $s\ne0$ (Lemma 22.1), so for every $\ell<1$ some finite $\tau$ has $\mathfrak M(\tau)>\ell$, which gives the upper bound. For the first-hit limit (10.29): on every compact interval $[0,\tau_\ell-\delta]$ the limit profile stays a positive margin below $\ell$, and strict crossing supplies a point of $[\tau_\ell,\tau_\ell+\delta]$ where it exceeds $\ell$; uniform convergence of $M_B/\Gamma_B$ on compact sets and $\Gamma_B\to1$ then trap the first finite-$B$ hitting time in $[\tau_\ell-\delta,\tau_\ell+\delta]$ in units of $B^{3/2}/J$. $\square$

**What this settles, and what it does not.** Three things follow immediately.

*The centre cancellation is real and is not a defect of the estimates.* The reason no uniform relative remainder for adjacent differences can be imported from Theorem 10 is that in this window the differences are the **derivative** of a smooth profile, and that derivative vanishes at the band centre. Any theorem claiming a uniform $\Theta(B^{-3/2})$ for $\Delta_k$ across $k=0$ is false; the true size at the centre is $\Theta(B^{-2})$, a factor $\sqrt B$ smaller. Away from the centre the differences are $\Theta(B^{-3/2})$ with relative error $o(1)$, which is (10.27); *at* the centre (10.27) still holds as an absolute statement, both sides tending to zero. This closes the second obligation of Section 14 in the only form in which it can be true.

*The first-loss law is polynomial, not exponential — but its constant is not the one v1.0 guessed.* The diffusive window has $JT_\ell=\Theta(B^{3/2})$, with the constant $\tau_\ell$ computable from the Ornstein–Uhlenbeck Dirichlet problem. A draft of this section then claimed that "$\Lambda'=\Theta(Ke^{-2K^2})$, so that constant grows like $e^{2K^2}$", and concluded that the sentence v1.0 printed, $JT\sim B^{3/2}e^{2K^2}$, was vindicated in its $K$-dependence. **Both halves are wrong and are withdrawn here.** At fixed $c\ne0$ the Kramers form gives $\Lambda'(c;K)\approx(2K-c)\Lambda(c;K)=\Theta\bigl(K^2e^{-2K^2+2Kc}\bigr)$, so $\Lambda'(1;K)/(Ke^{-2K^2})$ runs $90.2,\,394.1,\,1486.1$ at $K=2,2.5,3$ and is unbounded; at $c=0$, $\Lambda'=0$. There is therefore no $c$ at which the printed claim holds. Consequently the first-loss constant depends on $\kappa$ as well as $K$, with the large-$\Lambda'$ modes near the outer edge $c=2\kappa$ setting the exponential scale. That last statement is heuristic rather than established: $\rho(s)=\tfrac12(1+\cos\pi s)$ *vanishes* at $s=\pm1$, so the outermost modes carry no sine weight and a boundary-layer analysis would be needed to turn the heuristic into a proof. At $\kappa=3/4$,

| $K$ | $\tau_{1/10}$ | $\tau_{1/10}/e^{2K^2}$ | $\tau_{1/10}\big/\bigl[e^{2(K-\kappa)^2}/K^2\bigr]$ |
|---|---|---|---|
| $1.5$ | $1.37023$ | $1.522\times10^{-2}$ | $1.001$ |
| $2.0$ | $8.29110$ | $2.781\times10^{-3}$ | $1.457$ |
| $2.5$ | $144.740$ | $5.394\times10^{-4}$ | $1.979$ |
| $3.0$ | $8286.6$ | $1.262\times10^{-4}$ | $2.997$ |

(These are computed on the discretised Ornstein–Uhlenbeck problem of row V50; the $K=3$ entry is sensitive to the discretisation at the $10^{-4}$ level, the others at $10^{-5}$ or below.) The $e^{2K^2}$-normalised column falls by a factor $\approx5$ per half-step in $K$, while the successive increments of $\log\tau_{1/10}$ are $1.80,\,2.86,\,4.05$ against the predicted $2(K-\kappa)^2$ increments $2.0,\,3.0,\,4.0$. The last column is not constant either — it grows roughly linearly in $K$, so $e^{2(K-\kappa)^2}/K^2$ captures the exponential scale but not the polynomial prefactor. What the table supports, and what it does not, must be stated with care — the v1.4 audit (F14-10) found the previous sentence overstated. The statement $\log\tau_\ell=2(K-\kappa)^2\bigl(1+o(1)\bigr)$ has exactly the same content as $\log\tau_\ell=2K^2\bigl(1+o(1)\bigr)$, since the two differ by $O(K)$; so the table does **not** establish a $\kappa$-dependent exponent ratio, nor the linear-in-$K$ correction $-4K\kappa$, nor a prefactor — four values of $K$ cannot separate a linear correction from a slowly varying prefactor. What it does show is only this: the sampled ratios $\tau_{1/10}/e^{2K^2}$ **decrease** on $K\in\{1.5,2,2.5,3\}$; their limit, and whether a uniform positive lower bound exists as $K\to\infty$, are **not determined by this table** (the v1.5 sentence that the table shows the absence of such a lower bound was itself an asymptotic conclusion drawn from four values — audit finding F15-07 — and is withdrawn). The v1.0 sentence $JT\sim B^{3/2}e^{2K^2}$ therefore remains unproved rather than refuted by the table; what refutes its *derivation* is the $c$-dependence of the Kramers form above. The leading order $\log\tau_\ell=2K^2(1+o(1))$ is **[HYPOTHESIS]**, consistent with the Kramers form of $\Lambda'$; the correction is **[OPEN]**. What (10.29) proves is a $\Theta(B^{3/2})$ law with a constant determined by the Ornstein–Uhlenbeck problem for the given $(K,\kappa)$ **[VERIFIED]**; it does not vindicate v1.0's $K$-dependence, and the claim that it does is retracted. (Row V50 evaluates $\mathfrak M$ and $\tau_{1/10}$ at $K=3/2$, $\kappa=3/4$; the table above is checked in the same row.)

*Why the Section 9 theory gives nothing here.* At the exponential $B^{-1}\log$ scale of Section 9 the rate measure of this fixed-$K$ band is concentrated at $0$: there is no interior rate on which the alignment capacity $\kappa^\pm(z)$ of Section 9.1 is defined, so Theorems 2 and 15 make no statement about this band, and the exponential regime and the diffusive regime of Theorem 22 are different laws. The v1.4 text argued this from "bounded adjacent ratios rule out lacunarity"; that argument is **withdrawn** (finding F14-09), because bounded adjacent ratios never exclude lacunarity — the dyadic sequence has constant ratio $2$ and is the prototype of a lacunary sequence — and because a sparse subsequence of this band could well satisfy a Hadamard gap condition, so a sparse-subsequence Riesz estimate is not ruled out. Likewise, $h=o(B^{3/4})$ is the range on which replacing $BI(h/B)$ by $2h^2/B$ is accurate to additive $o(1)$ (consequence (b) of Section 10.1); it is a precision boundary of that substitution and **not** a proved dynamical transition, and Theorem 10 already covers eigenvalues in the intermediate range $h\ge\sqrt{2B\log B}$ — what is missing there is the adjacent-difference and first-loss control, not the eigenvalues.

Row V50 evaluates all four parts: at $K=3/2$, $\kappa=3/4$ the profile values $\mathfrak M(\tau)$ at $\tau=\tfrac12,1,2,4$ are $0.01393$, $0.05456$, $0.20109$, $0.58963$, approached from below by the exact band at $B=1024,\ldots,65536$ ($0.01303\to0.01382$, $0.05107\to0.05415$, $0.18867\to0.19962$, $0.55861\to0.58590$), and $JT_{1/10}/B^{3/2}$ runs $1.41994,\ 1.39338,\ 1.38138,\ 1.37570$ against the limit $\tau_{1/10}=1.37023$ (the v1.4 audit's independent Kummer-determinant computation gives $\tau_{1/10}=1.3702311741597\ldots$ with a positive slope $\mathfrak M'(\tau_{1/10})=0.13845\ldots$, so the first contact is a strict crossing there).

### 10.7 An explicit envelope for the lacunary rate function — Corollary 23

Theorem 16 determines the effective domain of $\mathcal I_q$ and its two endpoint values. The same two extremal measures give an explicit upper envelope on the whole domain, at no extra cost.

**Corollary 23 [PROVEN; new in v1.4].** For every integer $q\ge2$, with $\beta_q=\cos\frac\pi{q+1}$ for even $q$ and $\beta_q=1$ for odd $q$,

$$
\boxed{\ \mathcal I_q(s)\ \le\ (\log q)\max\Bigl\{s,\ \frac{-s}{\beta_q}\Bigr\}\qquad(-\beta_q\le s\le1),\ }
\tag{10.30}
$$

with equality at $s=-\beta_q$, at $s=0$ and at $s=1$.

*Proof.* Lebesgue measure is $T_q$-invariant with $h=\log q$ and $\int c\,d\mathrm{Leb}=0$. For $-\beta_q\le s\le0$ write $s=-(1-\theta)\beta_q$ with $\theta\in[0,1]$ and take $\mu=\theta\,\mathrm{Leb}+(1-\theta)\,\mathfrak c$, where $\mathfrak c$ is the two-cycle measure of Theorem 13 (the fixed point $\tfrac12$ for odd $q$). The sign convention needs stating once, since both directions appear in this paper: Theorem 13 proves $\beta_q+\cos2\pi x+u_q(T_qx)-u_q(x)\ge0$ with equality exactly on that two-cycle, so $\mathfrak c$ is the measure at which $\int c\,d\nu$ attains its **minimum** $-\beta_q$ — equivalently, the measure *maximising* the ergodic average of $-c$, which is the sense in which Theorem 13 calls it maximising. Then $\int c\,d\mu=s$ and $h_\mu=\theta\log q$ by affinity of the entropy, so $\mathcal I_q(s)=\log q-\sup\{h_\nu:\int c\,d\nu=s\}\le\log q-\theta\log q=(1-\theta)\log q=(\log q)(-s/\beta_q)$. For $0\le s\le1$ use the fixed point $x=0$, which has $\int c=1$ and $h=0$, in place of $\mathfrak c$. Equality at the two endpoints is Theorem 16: the content there is not merely that $\mathfrak c$ and $\delta_0$ realise the endpoint values of $\int c\,d\nu$, but that **every** invariant measure attaining an endpoint has zero entropy, which is what forces $\mathcal I_q(\pm)=\log q$ rather than something smaller. Equality at $s=0$ holds because Lebesgue attains the maximal entropy. $\square$

Two remarks on what this argument is and is not. Since $\mathcal I_q$ is convex, (10.30) is exactly the chord through the three points $(-\beta_q,\log q)$, $(0,0)$, $(1,\log q)$, so the corollary is a consequence of convexity together with the endpoint determination of Theorem 16; the convex-combination construction above is a self-contained re-derivation of it rather than an independent ingredient. And the bound is loose in the interior: computing $\mathcal I_q$ from periodic-orbit pressure sums gives a maximal slack, over the 25-point grid of row V51 (C51 in v1.4), of $0.2791$ at $s=-0.3125$ for $q=2$ and $0.6126$ at $s=-0.5829$ for $q=4$, against $\log q=0.693$ and $1.386$; on a finer grid the maxima are $0.2794$ near $s\approx-0.32$ and $0.6144$ near $s\approx-0.61$. No grid point violates the bound, and the three claimed equalities are reproduced to $5\times10^{-4}$. The estimator matters here and is stated for reproducibility: the pressure is taken as $P(t)=\tfrac12\log(Z_n/Z_{n-2})$ over **even** $n$, which cancels the $O(1/n)$ prefactor bias that a bare $n^{-1}\log Z_n$ carries at $s=-\beta_q$ (with the bare sum one would need $n\approx1400$ to reach $5\times10^{-4}$ there), and even $n$ is required because an odd-period orbit set cannot contain the $2$-cycle. Row V51 records the slack alongside the three equalities.

The content is modest and the proof is three lines, which is the point: the endpoint determination of Theorem 16 immediately controls the rate function on its whole domain from above, and the bound is attained at three points. Whether $\mathcal I_q$ is affine near the left endpoint — equivalently, whether $\sup\{h_\nu/(\beta_q+\int c\,d\nu)\}$ is finite, the freezing question for this potential — was left open in v1.4, where a first attempt to bound that ratio by an excursion count ($h_\nu\le H(p)+p\log q$ with $p$ the mass outside a neighbourhood of the cycle, $D(\nu)\ge c_0p$, and $H(p)/p\to\infty$) was shown to fail. It is settled in §10.8: there is no freezing, and $\log q-\mathcal I_q(-\beta_q+u)=\Theta(u\log(1/u))$ with the sharp coefficient $1/A_q$ of §10.9. Row V51 checks (10.30) against the two extremal measures and the entropy affinity, and against an independent numerical rate function; it was typed C in v1.4 and is retyped V here, since its verdict uses floating cosines, finite periodic sums and a finite grid (v1.4 audit, F14-06).

### 10.8 No finite-temperature freezing and quantitative endpoint entropy — Theorem 24

**Provenance.** Sections 10.8 and 10.9 were written by the v1.4 audit (a different AI family from the one that wrote v1.0–v1.4; see the AI-use record). They are reproduced here with the audit's attributions, after the following independent re-checks recorded in Appendix R3: every constant in (10.33)–(10.47) was recomputed in exact rational arithmetic (row C53), the Markov remainder (10.36) was checked numerically with a separate implementation (row V54), the imported theorem was read in its source, and the one item that was **not available in the authoring session of v1.5** — the exact finite certificates the v1.4 audit cites for $q=2,4$ in Proposition 24.1 — is replaced in §10.9 by an argument that needs no such certificate. (The v1.5 audit established that those certificate files, `verification/barrier_certificate.py` and `.json`, *were* present in the v1.4 audit ZIP as delivered; v1.5's statement that they were "not present in the delivered bundle" is corrected here — audit finding F15-06 — and the files are preserved as lineage in the v1.6 bundle under `provenance_v14/`. The alternative completion of §10.9 stands on its own.)

For every $q\ge2$ the pressure of a Hölder potential on the full $q$-shift is real analytic at every finite real parameter; the mechanism is present in Theorem B and its proof, (19)–(21), of Frühwirth–Juhos–Prochno (arXiv:2107.12860), and a general formulation is Theorem 5.4 of Cioletti–Silva (arXiv:1511.01579). A finite affine tail of the pressure would contradict analyticity unless the pressure were globally affine, which $P_q(0)=\log q$ together with its distinct extremal slopes excludes. Hence **finite-temperature freezing is absent** for $\mathcal I_q$: the question left open in §10.7 of v1.4 is closed by an imported theorem, not by a new principle. What §10.7 recorded — that the elementary excursion count cannot decide it — remains true; the decision comes from analyticity.

For even $q$ the explicit residual of Theorem 13 gives a quantitative, constructive statement about the endpoint.

**Theorem 24 [DERIVED/EXTENDED; supplied by the v1.4 audit].** Fix an even integer $q\ge2$, put $\beta=\cos(\pi/(q+1))$, and define

$$
D(\nu)=\beta+\int c\,d\nu,\qquad
h_*(u)=\sup\{h_\nu:D(\nu)=u\}.
$$

There are explicit positive constants $\delta_q,A_q$ such that, as $u\downarrow0$,

$$
\frac{u}{A_q}\log\frac1u+O_q(u)\ \le\ h_*(u)\ \le\ \frac{u}{\delta_q}\log\frac1u+O_q(u).
\tag{10.31}
$$

In particular

$$
\log q-\mathcal I_q(-\beta+u)=\Theta_q\!\left(u\log\frac1u\right),
\tag{10.32}
$$

so the left endpoint has an infinite negative right slope and no affine interval adjoins it. Theorem 24 determines the endpoint order; Proposition 24.1 determines the sharp leading coefficient. Neither determines the whole rate function.

*Proof, upper bound.* Use the exact non-negative residual of Theorem 13, $r_q(x)=\beta+c(x)+u_q(T_qx)-u_q(x)$, whose only zeros are $p=q/[2(q+1)]$ and $1-p$, and note $D(\nu)=\int r_q\,d\nu$. Put $a=(q-2)/2$, $b=q/2$; the maximising two-cycle has alternating base-$q$ digits $a,b$. Predict the next digit by $F(a)=b$ and $F(d)=a$ for $d\ne a$, and let $E_q$ be the union of the closed two-digit cylinders whose second digit differs from this prediction. The two-cycle lies strictly inside the two correct cylinders, so

$$
\delta_q:=\min_{x\in E_q}r_q(x)>0 .
\tag{10.33}
$$

This is a finite explicit minimisation: on every cylinder the tent terms are piecewise linear, and every candidate minimum is an endpoint or a root of a sine equation. For the stationary digit process of an invariant measure with prediction-error probability $e$, $D\ge\delta_qe$, and conditioning on the previous digit and the error indicator gives $h_\nu\le H_2(e)+e\log(q-1)$, $H_2(e)=-e\log e-(1-e)\log(1-e)$. For $u/\delta_q<(q-1)/q$ the right side is increasing in $e\le u/\delta_q$, so

$$
h_*(u)\le H_2(u/\delta_q)+(u/\delta_q)\log(q-1).
\tag{10.34}
$$

The digit partition is generating and the finite ambiguity of base-$q$ expansions adds no entropy.

*Proof, lower bound.* On the two digits $a,b$ take the stationary Markov chain with equal stationary probabilities and transition matrix $\bigl(\begin{smallmatrix}\varepsilon&1-\varepsilon\\1-\varepsilon&\varepsilon\end{smallmatrix}\bigr)$: it alternates with probability $1-\varepsilon$ and repeats with probability $\varepsilon$, and its entropy is exactly $H_2(\varepsilon)$. Map the digit sequence to the circle. A single repeat after digit $j$, starting in the $a$-phase, shifts $p$ by $(-1)^jq^{-j}/(q+1)$; the other phase is the reflection and has the same cosine cost. Consequently

$$
A_q=\sum_{j=1}^{\infty}\Bigl[\cos\Bigl(2\pi\Bigl[p+\frac{(-1)^j}{(q+1)q^j}\Bigr]\Bigr)+\beta\Bigr],
\tag{10.35}
$$

an absolutely convergent series. If $D_\varepsilon$ is the mean defect of this Markov measure then for all $0\le\varepsilon\le1$

$$
|D_\varepsilon-A_q\varepsilon|\le C_q\varepsilon^2,\qquad C_q=\frac{4\pi}{(q-1)^3}.
\tag{10.36}
$$

Parametrise the chain by its independent repeat indicators; flipping indicator $j$ changes only digits after $j$, hence the coded point by at most $q^{-j}/(q-1)$, and a mixed difference in indicators $i<j$ of the cosine is at most $4\pi q^{-j}/(q-1)$. Taylor's formula for the Bernoulli product expectation and the summable bound $\sum_{j\ge2}(j-1)4\pi q^{-j}/(q-1)=4\pi/(q-1)^3$ give (10.36); truncation sets later indicators to zero and keeps the alternating tail, and the limit with its first two derivatives follows from the same bounds. For this chain the prediction-error probability is exactly $\varepsilon$, so $D_\varepsilon\ge\delta_q\varepsilon$ and $A_q\ge\delta_q>0$. The inverse function theorem gives $\varepsilon(u)=u/A_q+O_q(u^2)$ with $D_{\varepsilon(u)}=u$, whose entropy $H_2(\varepsilon(u))=(u/A_q)\log(1/u)+O_q(u)$ is a lower bound for $h_*(u)$. With (10.34) and the pressure–entropy representation this is (10.31)–(10.32). $\square$

**Finite pressure consequences.** For $t\ge0$ and $0<\varepsilon<1$,

$$
P_q(-t)-t\beta\ \ge\ H_2(\varepsilon)-t\bigl(A_q\varepsilon+C_q\varepsilon^2\bigr),
\tag{10.37}
$$

which is strictly positive for every finite $t$ once $\varepsilon$ is small enough, and conversely the prediction-error argument gives

$$
P_q(-t)-t\beta\ \le\ \log\bigl[1+(q-1)e^{-t\delta_q}\bigr].
\tag{10.38}
$$

For $q=2$, $E_2=[0,\tfrac14]\cup[\tfrac34,1]$, symmetry and the negative derivative on the first interval give

$$
\delta_2=\tfrac12-\frac{\pi\sqrt3}{12}=0.0465501589414\ldots,\qquad A_2=0.8055731326765\ldots ,
$$

and with the **exact** witness $\varepsilon=1/200000$ the rational bounds of row C53 establish

$$
\boxed{\ P_2(-15)-\tfrac{15}2>5.6076\times10^{-6}.\ }
\tag{10.39}
$$

This has a consequence for v1.4. Section 14 of that version printed a periodic-orbit estimate of $P_2(-15)-\tfrac{15}2\approx1.08\times10^{-8}$, obtained from the ratio estimator $\tfrac12\log(Z_n/Z_{n-2})$ at $n=22$, and read its apparent decay in $t$ as evidence against freezing. The estimate is more than a factor $500$ **below** a rigorous lower bound for the true pressure defect (row V54 reproduces both numbers); the finite-period sum has an uncontrolled remainder at low temperature, because period-$22$ orbits cannot resolve repeat rates of order $10^{-6}$. That estimator and the inference drawn from it are **withdrawn**. The conclusion it was offered for — no freezing — happens to be true, by the analyticity argument above, but the v1.4 evidence for it was worthless, and v1.4 had itself flagged the probe as unasserted. It is now asserted, by (10.37) and analyticity, and no longer by any orbit sum.

**Attribution and scope.** Entropy conditioning, Bernoulli defect constructions and the variational principle are standard. The added calculation is their explicit combination with the all-even residual of Theorem 13, the series (10.35), the uniform remainder (10.36) and the diagnostic (10.39). No global priority or new thermodynamic method is claimed, and nothing in (10.31)–(10.39) concerns the finite-horizon alignment capacity of the actual spin eigenvalue differences.

### 10.9 Sharp completion of Theorem 24: the optimal excursion cost — Proposition 24.1

**Proposition 24.1 [DERIVED; supplied by the v1.4 audit; proof completed for every even $q$ in this version].** For every fixed even integer $q\ge2$, with $p=q/[2(q+1)]$, $\alpha=\pi/(q+1)$, $\beta=\cos\alpha$ and the series $A_q$ of (10.35),

$$
\boxed{\ \lim_{t\to\infty}-\frac1t\log\bigl(P_q(-t)-t\beta\bigr)=A_q ,\ }
\tag{10.40}
$$

$$
\boxed{\ \lim_{u\downarrow0}\frac{\log q-\mathcal I_q(-\beta+u)}{u\log(1/u)}=\frac1{A_q}.\ }
\tag{10.41}
$$

The optimal coefficient is thus the reciprocal of the single-repeat series, not merely bounded below by it. As even $q\to\infty$,

$$
q^3A_q\longrightarrow2\pi^2 .
\tag{10.42}
$$

#### Pressure reduction and its exact scope

Use the non-negative residual $r=r_q$ of Theorem 13 and the symbolic potential $\mathscr A=-r$ on the full $q$-shift, a mixing shift of finite type on which the coding of $r$ is Lipschitz. The zero set of $r$ consists of the two alternating sequences; a point with $r(x)>0$ has strictly positive cost on every sufficiently close return and cannot be an Aubry point, while the two zero sequences have zero-cost periodic returns. The Aubry set is therefore exactly this period-two orbit: one irreducible component, entropy $0$ (the two points are not two ground-state components). Theorem A and §§3.3–3.5, in particular Proposition 23, of Leplaideur–Mengue, *On the selection of subaction and measure for perturbed potentials* (arXiv:2404.02182; read in the source for this version), then give the existence of a positive pressure-decay cost $E_q$, equal to the one-component external Mañé cost. In the present sign convention, with $S$ the non-positive Mañé potential of $\mathscr A$ and $\Omega=\{p,1-p\}$,

$$
E_q=\min_{z\in T_q^{-1}(\Omega)\setminus\Omega}\bigl\{r(z)-S(\Omega,z)\bigr\},
\tag{10.43}
$$

where $-S(\Omega,z)$ is the infimum of the residual sums over arbitrarily long backward paths from $z$ approaching $\Omega$; cohomology gives $P(t\mathscr A)=P_q(-t)-t\beta$. This imports an existence-and-representation theorem. It does not import the value: every backward path approaching $\Omega$ gives an upper bound on $E_q$, and minimising over **all** prefixes of a fixed length gives a lower bound. The identification $E_q=A_q$ is the content below.

#### The candidate path and its tail

Put $s=1/[q(q+1)]$. The two candidate last preimages are $x_1=p-s$ and its reflection. From $x_1$ prepend at each step the digit whose inverse branch is centred on the other ground point; the displacement contracts by $1/q$ at every step and, up to reflection, the visited cosines are those at $p+(-1)^j/[(q+1)q^j]$, $j\ge1$. The tent coboundary telescopes with equal limiting tent values at the two ground points, so the total cost of this path is exactly $A_q$, and $E_q\le A_q$. (Lemma 25.3 of §10.10 records this path and its exact residuals, including the fact that the sub-action bracket is $2\alpha$ at the first step and $0$ afterwards.)

Let $r_0=r(p-s)$. Direct substitution gives

$$
r_0=\cos\alpha-\cos\Bigl(\alpha+\frac{2\alpha}q\Bigr)-\frac{2\alpha\sin\alpha}{q(q+1)} .
\tag{10.44}
$$

All subsequent points of the path have their tent terms on the ground-state linear branches, so their residuals are tangent remainders of $-\cos d$ with angular displacements $2\alpha/q^j$, and non-negativity with Taylor's remainder gives

$$
0\le A_q-r_0\le U_q:=\frac{2\alpha^2}{q^2(q^2-1)} .
\tag{10.45}
$$

Also $\operatorname{Lip}(r)\le2\pi(1+\sin\alpha)<4\pi$ in circle distance measured in turns, and

$$
A_q\le\frac{2\pi}{q^2-1},
\tag{10.46}
$$

an absolute-sum bound on (10.35), not an estimate from a finite-temperature fit.

#### Excluding every competing path for even $q\ge6$ (the audit's argument)

Every preimage of a ground point other than the correct ground preimage and the candidate $p-s$ (or its reflection) has angular distance $d\ge3\alpha$ from $\tfrac12$: consecutive preimages are spaced by $2\pi/q$ in angle, so after the distances $\alpha$ and $\alpha(1+2/q)$ the next possible distance is at least $3\alpha$ (this is Lemma 25.4(a) of §10.10). For $3\alpha\le d\le\pi-\alpha$ the tangent bound $g$ of Theorem 13 gives $r\ge g(d)\ge g(3\alpha)=2\sin\alpha(\sin2\alpha-\alpha)$, and since $\alpha^2<10/49$,

$$
g(3\alpha)\ge2\alpha^2\Bigl(1-\frac{\alpha^2}6\Bigr)\Bigl(1-\frac{4\alpha^2}3\Bigr)\ge\frac{30388}{21609}\alpha^2>\frac75\alpha^2 ;
$$

for $\pi-\alpha\le d\le\pi$ the bound $G$ of Theorem 13 satisfies $G(d)\ge2\cos\alpha-\alpha\sin\alpha\ge2-2\alpha^2\ge2\alpha^2$, and $G$ has at most one interior maximum there, so its endpoint values suffice. Meanwhile (10.46) gives $A_q\le\frac2\pi\frac{q+1}{q-1}\alpha^2<\frac{14}{15}\alpha^2$. Every other last preimage therefore costs more than the entire candidate excursion, and only the two candidate starts remain, at cost $r_0$.

It remains to exclude a later deviation, however late. On the candidate path every current point is within $s$ of its ground centre; a wrong inverse branch lands within $s/q$ of an off-orbit preimage of that centre, whose residual is at least $r_0$, so the residual on the wrong branch is at least $r_0-4\pi s/q$ by the Lipschitz bound. The accumulated cost already contains $r_0$, so a deviation costs at least $2r_0-4\pi s/q$. On $[\alpha,\alpha+2\alpha/q]$, $\sin d\ge\sin\alpha$, so (10.44) gives $r_0\ge2\alpha\sin\alpha/(q+1)$; with $\sin\alpha\ge\alpha(1-\alpha^2/6)$, $\pi>3$ and $q\ge6$,

$$
r_0-U_q-\frac{4\pi s}q\ \ge\ \frac{\alpha^2}{q+1}\Bigl(\frac{284}{147}-\frac1{90}-\frac{49}{27}\Bigr)=\frac{\alpha^2}{q+1}\cdot\frac{1403}{13230}>0 ,
\tag{10.47}
$$

the tail term after division by $\alpha^2/(q+1)$ being at most $2(q+1)/[q^2(q^2-1)]\le1/90$ and the Lipschitz term at most $4(q+1)^2/(\pi q^2)<49/27$. Any deviation therefore exceeds $r_0+U_q\ge A_q$, induction forces the candidate branch forever on every minimising excursion, and $E_q=A_q$ for every even $q\ge6$. Row C53 re-derives (10.44)–(10.47) in exact arithmetic at $q=6,8,10,14,20$; the margin in (10.47) is in fact $0.53\,\alpha^2/(q+1)$ at $q=6$ and increases to $0.71$ at $q=50$, the printed $1403/13230=0.106$ being the audit's uniform lower bound.

#### Completion for $q=2$ and $q=4$

The v1.4 audit closed these two cases by a finite branch-and-bound certificate (its equation (10.48)) whose script and output, `verification/barrier_certificate.py` and `.json`, were not available in the session that wrote v1.5 (v1.5 wrongly wrote that they were absent from the delivered bundle; they were in it, and are now carried as lineage in `provenance_v14/` — finding F15-06 of the v1.5 audit). This version does not rely on them; it supplies an alternative completion. Two things replace them. For $q=4$ the audit's own argument closes the case once the actual numbers are used instead of the uniform constants printed for $q\ge6$: the exact quantity $r_0-U_4-4\pi s/q$ equals $+0.303\,\alpha^2/(q+1)$, $g(3\alpha)=0.961\,\alpha^2>A_4=0.474\,\alpha^2$, and $G\ge2-2\alpha^2$ on $[\pi-\alpha,\pi]$ (row C53); only the printed bounds $\alpha^2<10/49$ and $q\ge6$ fail at $q=4$, not the argument. For $q=2$ the Lipschitz route genuinely fails ($r_0-U_2-4\pi s/q=0.698-0.183-1.047<0$), and there Lemma 25.4(c) of §10.10 — which holds for $q=2$ as well, although that section's standing hypothesis is $q\ge4$ — gives the residual at the wrong-branch point **exactly**: the sub-action bracket there is $2\alpha\pm4\alpha/q^j$, not merely "$\ge2\alpha-4\pi s/q$". With that the deviation cost at any step is at least $r_0+R_{\rm dev}$ with $R_{\rm dev}$ as in (10.64) at $\varepsilon=0$, and $R_{\rm dev}>A_q-r_0$ is certified in exact rational arithmetic in row C56, with margin $0.2731$ for $q=2$ (and, redundantly, $0.1589$ for $q=4$ and $0.0615$ for $q=6$). At $q=2$ the point $d_1=2\pi/3=\pi-\alpha$ is a critical point of $g_0$ — a local **maximum**, since $g_0'(d)=\sin d-\sin\tfrac\pi3<0$ on $(2\pi/3,5\pi/6]$ — so the minimum of $g_0$ over the segment $[d_1,d_1+2\alpha/q^2]=[2\pi/3,5\pi/6]$ sits at its right end, not at $d_1$ as for $q\ge4$; v1.5 called it an interior minimum, which was wrong (audit finding F15-08) but immaterial, because row C56 lower-bounds $g_0$ over the whole segment and never assumed where the minimum lies. For $q=2$ there is no other last preimage at all ($T_2^{-1}(\tfrac13)=\{\tfrac16,\tfrac23\}$). Hence $E_q=A_q$ for $q=2$ and $q=4$ as well, and (10.40) holds for every even $q$.

For the record, the same exact computation gives at $q=2$ the enclosure $0.8055731326765144\le A_2\le0.8055731326765158$ (row C53), which contains the audit's interval $[0.805573132676514469,\ 0.805573132676515768]$.

#### Entropy duality and large-$q$ behaviour

The entropy profile has the variational duality $h_*(u)=\inf_{t\in\mathbb R}\{P_q(-t)-t\beta+tu\}$. For small $u>0$ the minimisers tend to $+\infty$ (any bounded set of $t$ has a positive pressure defect, while the entropy tends to $0$ at the unique zero-entropy optimising orbit). For every fixed $0<\epsilon<A_q$, (10.40) bounds that defect between $e^{-(A_q+\epsilon)t}$ and $e^{-(A_q-\epsilon)t}$ for large $t$; minimising $e^{-at}+tu$ gives $(u/a)[\log(a/u)+1]$, and dividing by $u\log(1/u)$ and letting $\epsilon\downarrow0$ proves (10.41), as a relative $o(1)$ statement — no sharp additive $O(u)$ remainder and no multiplicative pressure prefactor is claimed. Finally, Taylor expansion of (10.44) with $\alpha=\pi/(q+1)$ gives $r_0=2\pi^2q^{-3}[1+O(q^{-1})]$ and the tail (10.45) is $O(q^{-6})$, which proves (10.42); row C53 records $q^3A_q=11.97,14.20,16.20,17.87$ at $q=4,6,10,20$, increasing towards $2\pi^2=19.74$.

**Attribution and status.** Pressure existence and the abstract cost representation are consequences of Leplaideur–Mengue; entropy duality is standard. The added result is the all-even evaluation of that cost by exclusion of competing inverse branches — the audit's explicit margin (10.47) for $q\ge6$, and, since v1.5, the exact competitor geometry of Lemma 25.4 for $q=2,4$ (which the v1.4 audit had handled by a finite certificate that was not available in the v1.5 authoring session). It remains a result about integer-geometric spectra; its novelty and significance are to be compared as this explicit result, without any claim to have invented the zero-temperature formalism or to have solved the actual-spin $\kappa$. The audit's authorship of (10.40)–(10.47) and this version's completion are both recorded in the AI-use record; neither has been reviewed by a human.

### 10.10 Stability of the optimal orbit and of the optimal excursion under the first harmonic — Theorem 25

Proposition 24.1 identifies, for the potential $c(x)=\cos2\pi x$ under $T_q$, the optimal orbit (the two-cycle $\Omega=\{p,1-p\}$), the optimal excursion (a single digit repeat) and the resulting zero-temperature cost $E_q=A_q$. The natural next question — the first target named in the v1.4 audit — is whether that structure is a coincidence of the pure cosine or is stable. This section answers it for the family

$$
f_\varepsilon(x)=\cos2\pi x+\varepsilon\cos4\pi x ,\qquad \varepsilon\in\mathbb R ,
\tag{10.49}
$$

with an **explicit** interval of $\varepsilon$ on which everything persists — uniform in $q$ on the left, and reaching the endpoint $\varepsilon^+(q)$ of the non-negative-slope proof on the right — and, in §10.11, with a certified two-sided bracket of the positive transition whose width is $O(q^{-3})$. The large-$q$ proof printed in v1.5 for this theorem was found defective by the v1.5 cross-family audit (F15-01) and is replaced below by that audit's repair; the theorem's statement is strengthened, not weakened, by the repair.

**Notation.** Throughout, $q\ge4$ is even (the case $q=2$ is degenerate and is settled in Lemma 25.0), $a=\pi/(q+1)$, $d(x)=2\pi|\{x\}-\tfrac12|\in[0,\pi]$ is the tent variable of (9.13), so that $\cos2\pi x=-\cos d(x)$ and $\cos4\pi x=\cos2d(x)$; $p=q/[2(q+1)]$, $\Omega=\{p,1-p\}$, $s=1/[q(q+1)]$, and $d'=d(T_qx)$. Put

$$
\beta_q(\varepsilon)=\cos a-\varepsilon\cos2a,\qquad
c_\varepsilon=\frac{\sin a-2\varepsilon\sin2a}{q+1},\qquad
u_\varepsilon(x)=c_\varepsilon\,d(x),
\tag{10.50}
$$

$$
r_\varepsilon(x)=\beta_q(\varepsilon)+f_\varepsilon(x)+u_\varepsilon(T_qx)-u_\varepsilon(x),
\tag{10.51}
$$

and, on $[0,\pi]$,

$$
g_\varepsilon(d)=\cos a-\cos d+\varepsilon(\cos2d-\cos2a)-(q+1)c_\varepsilon(d-a),\qquad
G_\varepsilon(d)=g_\varepsilon(d)+c_\varepsilon(qd-\pi).
\tag{10.52}
$$

At $\varepsilon=0$ these are $\beta_q$, $u_q$, $r_q$, $g$ and $G$ of Theorem 13. Finally let

$$
\eta_2(q)=\frac{\cos a-\tfrac a2\sin a}{2\sin^2a+2a\sin2a},\qquad
\varepsilon^+(q)=\frac1{4\cos a},
\tag{10.53}
$$

so that $\varepsilon^+(q)>\tfrac14$ for every $q$ and $\varepsilon^+(q)\downarrow\tfrac14$, while $\eta_2(4)=0.3310$, $\eta_2(6)=0.7453$, $\eta_2(8)=1.2890$ and $\eta_2(q)\sim(q+1)^2/(6\pi^2)$.

**Lemma 25.0 [PROVEN; the case $q=2$ is a coboundary].** For $q=2$ one has $\cos4\pi x=c(T_2x)$, hence $f_\varepsilon=(1+\varepsilon)c+\varepsilon(c\circ T_2-c)$ is cohomologous to $(1+\varepsilon)\cos2\pi x$. Consequently, for every $\varepsilon>-1$, the unique $f_\varepsilon$-minimising measure is the two-cycle $\{\tfrac13,\tfrac23\}$, $\beta_2(\varepsilon)=(1+\varepsilon)/2$, every invariant measure has $\int f_\varepsilon\,d\nu=(1+\varepsilon)\int c\,d\nu$, and the zero-temperature cost is $E_2(\varepsilon)=(1+\varepsilon)A_2$. At $\varepsilon=-1$ every invariant measure is minimising; for $\varepsilon<-1$ the minimiser is the fixed point $0$. In particular $B_2=A_2$ exactly (this identity is also visible term by term: $\cos2d_j-\cos2a=\cos a-\cos d_{j-1}$ for the points $d_j$ of Lemma 25.3, with $d_0=a$). $\square$

For $q\ge4$ the perturbation $\cos4\pi x=c(2x)$ is not of the form $c\circ T_q$ and nothing of the sort is available; the two parts below are genuine.

**Lemma 25.1 [PROVEN; the perturbed residual identity].** For every $x$,

$$
r_\varepsilon(x)=g_\varepsilon(d)+c_\varepsilon\bigl[q\,d+d'-\pi\bigr],
\qquad d=d(x),\ d'=d(T_qx),
\tag{10.54}
$$

and $qd+d'-\pi\ge0$ by (9.17). Hence, whenever $c_\varepsilon\ge0$, both $r_\varepsilon\ge g_\varepsilon(d)$ (using the bracket) and $r_\varepsilon\ge G_\varepsilon(d)$ (using only $d'\ge0$). Moreover $r_\varepsilon(1-x)=r_\varepsilon(x)$.

*Proof.* Expand (10.51) with $\cos2\pi x=-\cos d$, $\cos4\pi x=\cos2d$ and $(q+1)a=\pi$: the terms linear in $d$ are $-c_\varepsilon d$ on the left and $-(q+1)c_\varepsilon d+qc_\varepsilon d$ on the right, and the constants are $(q+1)c_\varepsilon a-\pi c_\varepsilon=0$. Reflection symmetry follows from the evenness of $f_\varepsilon$ and of $d$, and from $T_q(1-x)=1-T_qx$ modulo $1$. $\square$

Note that $g_\varepsilon=g_0+\varepsilon k$ with $k(d)=\cos2d-\cos2a+2\sin2a\,(d-a)$, the second-order Taylor remainder of $\cos2d$ at $d=a$; $g_\varepsilon$ and $G_\varepsilon$ are affine in $\varepsilon$, and $g_\varepsilon(a)=g_\varepsilon'(a)=0$ for every $\varepsilon$, with $g_\varepsilon''(a)=\cos a-4\varepsilon\cos2a$.

#### Part A: the two-cycle remains the unique optimal orbit

**Proposition 25.2 [PROVEN].** Let $q\ge4$ be even and $-\eta_2(q)<\varepsilon\le\varepsilon^+(q)$. Then $c_\varepsilon\ge0$, $r_\varepsilon\ge0$ everywhere, and $r_\varepsilon(x)=0$ exactly for $x\in\Omega$. Consequently

$$
\min_{\nu\in\mathcal M(T_q)}\int f_\varepsilon\,d\nu=-\beta_q(\varepsilon)=-\cos a+\varepsilon\cos2a ,
\tag{10.55}
$$

attained by the uniform measure on $\Omega$ and by no other invariant measure; $u_\varepsilon$ is a Lipschitz sub-action for $f_\varepsilon$.

*Proof.* $c_\varepsilon\ge0$ is $\sin a(1-4\varepsilon\cos a)\ge0$, i.e. $\varepsilon\le\varepsilon^+(q)$. By Lemma 25.1 it suffices to prove: $g_\varepsilon\ge0$ on $[0,\pi/q]$ with $a$ as its only zero, and $G_\varepsilon>0$ on $[\pi/q,\pi]$. (The two intervals cover $[0,\pi]$, and $\pi/q>a$.) Given these, $r_\varepsilon\ge0$; if $r_\varepsilon(x)=0$ then $d(x)\le\pi/q$ (else $r_\varepsilon\ge G_\varepsilon>0$), so $g_\varepsilon(d)=0$, $d=a$, and $x\in\Omega$. The minimisation statement then follows exactly as in the last paragraph of the proof of Theorem 13, by telescoping (10.51) along orbits.

*The case $0\le\varepsilon\le\varepsilon^+(q)$.* Write $\theta=(d+a)/2$, $\varphi=(d-a)/2$. Differentiating (10.52),

$$
g_\varepsilon'(d)=2\sin\varphi\,\bigl[\cos\theta-4\varepsilon\cos2\theta\cos\varphi\bigr]=:2\sin\varphi\,h_\varepsilon(d).
\tag{10.56}
$$

For $d\in[0,\pi-a]$ one has $\theta\in[a/2,\pi/2]$ and $\cos\varphi>0$. Where $\cos2\theta\le0$, $h_\varepsilon\ge\cos\theta\ge0$ with equality only at $d=\pi-a$. Where $\cos2\theta>0$, use $4\varepsilon\le1/\cos a$ and the exact identity

$$
\cos\theta\cos a-\cos2\theta\cos\varphi=\sin\theta\,\sin(\theta+\varphi)=\sin\theta\,\sin d ,
\tag{10.57}
$$

(expand $\cos a=\cos(\theta-\varphi)$ and $\cos2\theta=2\cos^2\theta-1$), which gives $h_\varepsilon\ge\sin\theta\sin d/\cos a>0$ for $0<d<\pi-a$. Hence $g_\varepsilon'$ has the sign of $d-a$ on $[0,\pi-a]$: $g_\varepsilon$ decreases on $[0,a]$, increases on $[a,\pi-a]$, and $g_\varepsilon\ge0$ there with $a$ as its only zero. This covers $[0,\pi/q]$ and more. On $[\pi/q,\pi-a]$, $G_\varepsilon=g_\varepsilon+c_\varepsilon(qd-\pi)>0$ because both terms are $\ge0$ and they vanish only at $d=a$ and $d=\pi/q$ respectively. On $[\pi-a,\pi]$ write $G_\varepsilon=G_0+\varepsilon m$ with $m(d)=\cos2d-\cos2a+2\sin2a\,d/(q+1)$; there $2d\in[2\pi-2a,2\pi]$, so $\cos2d\ge\cos2a$ and $m\ge0$, whence $G_\varepsilon\ge G_0>0$ by Theorem 13.

*The case $-\eta_2(q)<\varepsilon<0$; write $\varepsilon=-\eta$.* On $[0,\pi/q]$ one has $2d\le2\pi/q\le\pi/2$, so $g_\varepsilon''(d)=\cos d+4\eta\cos2d\ge\cos d>0$: $g_\varepsilon$ is strictly convex there, and $g_\varepsilon(a)=g_\varepsilon'(a)=0$ gives $g_\varepsilon\ge0$ with the single zero $a$. On $[\pi/q,\pi]$, $G_\varepsilon=G_0-\eta m$. The function $m$ is negative on $[\pi/q,\pi/2]$. At the left end, $\cos2a-\cos(2\pi/q)=2\sin(2a+a/q)\sin(a/q)=\sin2a\sin(2a/q)+2\cos2a\sin^2(a/q)$, so
$$-m(\pi/q)=\sin2a\bigl[\sin\tfrac{2a}q-\tfrac{2a}q\bigr]+2\cos2a\sin^2\tfrac aq\ \ge\ -\frac{8a^4}{3q^3}+\frac{1.9\cos2a\,a^2}{q^2}>0$$
for $q\ge4$ (using $\sin y\ge y-y^3/6$ and $\sin^2(a/q)\ge0.95\,a^2/q^2$; at $q=4$ the two exact terms are $-0.0049$ and $+0.0151$); $m'(d)=-2\sin2d+2\sin2a/(q+1)<0$ on $[\pi/q,\pi/4]$ since $\sin2d\ge\sin2a$ there; and on $[\pi/4,\pi/2]$, $m''=-4\cos2d\ge0$ with $m(\pi/4)=-\cos2a+\tfrac a2\sin2a<0$ and $m(\pi/2)=-1-\cos2a+a\sin2a<0$. So $G_\varepsilon\ge G_0>0$ on $[\pi/q,\pi/2]$. On $[\pi/2,\pi]$, $m$ is increasing ($\sin2d\le0$), so $m\le m(\pi)=2\sin^2a+2a\sin2a$, while $G_0$ attains its minimum over $[\pi/2,\pi]$ at an endpoint (Theorem 13 shows $G_0$ has a single interior maximum on $[\pi/q,\pi]$), and $G_0(\pi/2)=\cos a-\tfrac a2\sin a<G_0(\pi)$. Therefore $G_\varepsilon\ge\cos a-\tfrac a2\sin a-\eta\,(2\sin^2a+2a\sin2a)>0$ exactly when $\eta<\eta_2(q)$. $\square$

Two remarks. First, the upper endpoint is the limit of this *proof*: at $\varepsilon=\varepsilon^+(q)$ the tent slope $c_\varepsilon$ vanishes, and for $\varepsilon>\varepsilon^+(q)$ the bracket term of (10.54) changes sign, so neither $r_\varepsilon\ge g_\varepsilon$ nor $r_\varepsilon\ge G_\varepsilon$ is available; the same sub-action does remain non-negative somewhat beyond $\varepsilon^+(q)$ (§10.10.4), but Part B below needs $c_\varepsilon\ge0$ in any case. Second, the interval is not claimed to be the exact stability interval of the minimiser on either side; §10.11 brackets the positive transition between $\varepsilon^+(q)$ and an explicit competitor, and §10.10.4 records how lossy the two-line bound on $[\pi/2,\pi]$ is.

#### Part B: the single-repeat excursion remains the unique optimal one

The objects of Proposition 24.1 for the perturbed potential are the following. Let $x_1=p-s$ and, inductively, let $x_{j+1}$ be the preimage of $x_j$ on the inverse branch through the ground point $\omega_{j+1}$, where $\omega_j=p$ for odd $j$ and $\omega_j=1-p$ for even $j$. Let $A_q(\varepsilon)$ be the total residual of this path and

$$
B_q=\sum_{j\ge1}\bigl[\cos4\pi x_j-\cos4\pi p\bigr]=\sum_{j\ge1}\bigl[\cos2d_j-\cos2a\bigr].
\tag{10.58}
$$

**Lemma 25.3 [PROVEN; the candidate path].** For $j\ge1$: $x_j=\omega_j-s\,q^{1-j}$, $d_j:=d(x_j)=a+(-1)^{j+1}2a/q^j$, and the bracket of (10.54) at $x_j$ equals $2a$ for $j=1$ and $0$ for $j\ge2$. Hence

$$
r_\varepsilon(x_1)=g_\varepsilon(d_1)+2a\,c_\varepsilon=:r_0(\varepsilon),\qquad
r_\varepsilon(x_j)=g_\varepsilon(d_j)\ (j\ge2),\qquad
A_q(\varepsilon)=\sum_{j\ge1}r_\varepsilon(x_j)=A_q+\varepsilon B_q .
\tag{10.59}
$$

The series converge absolutely, $A_q(0)=A_q$ is the series (10.35), and $A_q(\varepsilon)$ is affine in $\varepsilon$.

*Proof.* $T_q(p-s)=qp-1/(q+1)\equiv p$ since $qp\equiv1-p$ and $1-p-1/(q+1)=p$; so $x_1$ is an off-orbit preimage of $p$, at distance $s$ from $\omega_1=p$. The inverse branch through $\omega_{j+1}$ is $y\mapsto\omega_{j+1}+(y-\omega_j)/q$ near $\omega_j$, which gives $x_{j+1}-\omega_{j+1}=(x_j-\omega_j)/q$ and the formula for $x_j$. The angle of $\omega_j$ is $\pi\mp a$ (upper sign for $p$), and $x_j$ shifts it by $-2\pi sq^{1-j}=-2aq^{-j}$; this gives $d_j$. For the bracket, $d(T_qx_j)=d(x_{j-1})=d_{j-1}$ for $j\ge2$ and $=a$ for $j=1$; substituting, $qd_j+d_{j-1}-\pi=(q+1)a-\pi+(-1)^{j+1}(2a/q^{j-1}-2a/q^{j-1})=0$ for $j\ge2$ and $qd_1+a-\pi=2a$ for $j=1$. Summing (10.51) along the path, the sub-action terms telescope to $u_\varepsilon(x_0)-\lim_ju_\varepsilon(x_j)=c_\varepsilon(a-a)=0$ since $d_j\to a$, and what remains is $\sum_j[\cos a-\cos d_j]+\varepsilon\sum_j[\cos2d_j-\cos2a]=A_q+\varepsilon B_q$. Absolute convergence follows from $|d_j-a|=2a/q^j$. $\square$

**Lemma 25.4 [PROVEN; the competitors].** (a) Every $z\in T_q^{-1}(\Omega)\setminus\bigl(\Omega\cup\{p-s,\,1-p+s\}\bigr)$ has $d(z)\ge3a$. (b) Let $j\ge1$ and let $x'$ be a preimage of $x_j$ other than $x_{j+1}$; then $x'=z''-sq^{-j}$ for some $z''\in T_q^{-1}(\omega_j)\setminus\{\omega_{j+1}\}$, and $|d(x')-d(z'')|\le2a/q^{j+1}$. (c) If $z''$ is the candidate-type preimage $\omega_j\mp s$ (the sign being $-$ for $\omega_j=p$), then exactly

$$
d(x')=d_1+(-1)^{j+1}\frac{2a}{q^{j+1}},\qquad
q\,d(x')+d(T_qx')-\pi=2a+(-1)^{j+1}\frac{4a}{q^{j}} .
\tag{10.60}
$$

*Proof.* (a) The preimages of $p$ have angles $(\pi-a+2\pi k)/q$, $k=0,\dots,q-1$, spaced by $2\pi/q=2a(q+1)/q$. The ground preimage $1-p$ ($k=q/2$) has $d=a$ and the candidate $p-s$ ($k=q/2-1$) has $d=a+2a/q$; the next angles on either side have $d\ge a+2a(q+1)/q>3a$ and $d\ge a+2a/q+2a(q+1)/q>3a$. Reflection handles $1-p$. (b) $T_q$ is affine with slope $q$ on each inverse branch, so $x'-z''=(x_j-\omega_j)/q=-sq^{-j}$, and $d$ is $2\pi$-Lipschitz. (c) For odd $j$, $\omega_j=p$ and $z''=p-s$ has angle $\pi-a-2a/q$; the shift $-sq^{-j}$ lowers the angle by $2aq^{-j-1}$, giving $d(x')=d_1+2a/q^{j+1}$, while $T_qx'=p-sq^{1-j}$ has angle $\pi-a-2aq^{-j}$ and $d(T_qx')=a+2aq^{-j}$; the bracket is $q(a+2a/q+2a/q^{j+1})+a+2a/q^j-\pi=2a+4a/q^j$. For even $j$, $\omega_j=1-p$ and $z''=1-p+s$ has angle $\pi+a+2a/q$; the same shift gives $d(x')=d_1-2a/q^{j+1}$, $T_qx'=1-p-sq^{1-j}$ has angle $\pi+a-2aq^{-j}$ and $d(T_qx')=a-2aq^{-j}$, so the bracket is $2a-4a/q^j$. $\square$

The bracket in (10.60) is the entire difference between the two parities: at even steps the wrong branch lands on the side where the sub-action term is *smaller* than at $z''$, and this is the only loss that the argument has to absorb. The v1.4-audit proof of Proposition 24.1 absorbed it with the global Lipschitz bound $4\pi s/q$, which is what forced its finite certificates for $q=2,4$; (10.60) replaces that bound by the exact value.

**Lemma 25.5 [IMPORTED + PROVEN; the cost functional].** Assume the conclusion of Proposition 25.2. Then the Aubry set of the symbolic potential $-r_\varepsilon$ is the two-cycle, Theorem A of Leplaideur–Mengue applies, and

$$
E_q(\varepsilon):=\lim_{t\to\infty}-\frac1t\log\bigl(P_{q,\varepsilon}(-t)-t\beta_q(\varepsilon)\bigr)
=\inf_{\gamma}\ \sum_{y\in\gamma}r_\varepsilon(y),
\tag{10.61}
$$

where $P_{q,\varepsilon}(\theta)=\sup_\nu\{h_\nu+\theta\int f_\varepsilon\,d\nu\}$ and the infimum runs over all backward excursions $\gamma=(y_1,y_2,\dots)$ with $T_qy_1\in\Omega$, $y_1\notin\Omega$, $T_qy_{k+1}=y_k$ and $\operatorname{dist}(y_k,\Omega)\to0$.

*Proof.* $r_\varepsilon\circ$(coding) is Lipschitz on the full $q$-shift and vanishes exactly on the two alternating sequences; a point with $r_\varepsilon>0$ has $S(x,x)<0$ in the notation of that paper, so the Aubry set is the period-two orbit, an irreducible subshift of finite type with entropy $0$. Cohomology gives $P(-tr_\varepsilon)=P_{q,\varepsilon}(-t)-t\beta_q(\varepsilon)$. Theorem A then gives the limit and identifies it with $-\sup_{y}[-r_\varepsilon(y)+S(\Omega,y)]$ over $y\in\sigma^{-1}\Omega\setminus\Omega$, and $-S(\Omega,y)$ is the infimum, as $\epsilon'\downarrow0$, of the residual sums over finite backward paths from $y$ whose last point is within $\epsilon'$ of $\Omega$. Passing from these finite paths to the infinite excursions of (10.61) is routine in both directions: a finite path ending within $\epsilon'$ of $\Omega$ is completed by the ground branches at an additional cost $O(\epsilon'^2)$ (the residual is quadratic at $\Omega$ and the ground branches contract by $1/q$), and an infinite excursion is truncated at a point within $\epsilon'$ of $\Omega$ at no cost. Paths that never approach $\Omega$ do not enter $S(\Omega,\cdot)$ and need no discussion. So (10.61) is Theorem A in circle coordinates; the same argument is (10.43) of §10.9, whose hypotheses are unchanged by the perturbation. $\square$

**Theorem 25 [PROVEN; stability of the optimal excursion; interval extended to $\varepsilon^+(q)$ and large-$q$ proof replaced in v1.6 after the v1.5 audit (its Theorem A15-1)].** Let $q\ge4$ be even and $-\tfrac1{20}\le\varepsilon\le\varepsilon^+(q)=1/(4\cos a)$. Then $\varepsilon$ lies in the range of Proposition 25.2 (the endpoint $\varepsilon^+(q)$ included, where $c_\varepsilon=0$), and

$$
\boxed{\ E_q(\varepsilon)=A_q+\varepsilon B_q ,\ }
\tag{10.62}
$$

attained by the single-repeat excursion of Lemma 25.3 and by its reflection, and by no other backward excursion: every other excursion has total residual at least $A_q(\varepsilon)+\mu_q(\varepsilon)$ with an explicit $\mu_q(\varepsilon)>0$. Consequently

$$
\lim_{u\downarrow0}\frac{\log q-\mathcal I_{q,\varepsilon}(-\beta_q(\varepsilon)+u)}{u\log(1/u)}=\frac1{A_q+\varepsilon B_q},
\tag{10.63}
$$

where $\mathcal I_{q,\varepsilon}$ is the Lebesgue large-deviation rate function of $\frac1n\sum_{k<n}f_\varepsilon(T_q^kx)$. For $q=2$ the same conclusions hold for every $\varepsilon>-1$, with $E_2(\varepsilon)=(1+\varepsilon)A_2$, by Lemma 25.0.

*Proof.* Range of the interval: $\varepsilon^+(q)>\tfrac14$ always, and $\eta_2(q)\ge\eta_2(4)>\tfrac1{20}$ since $\eta_2$ is increasing in $q$ (its numerator increases and its denominator decreases as $a$ decreases on $(0,\pi/5]$). So Proposition 25.2 and Lemma 25.5 apply on the whole closed interval, including the endpoint $\varepsilon^+(q)$, at which the residual is the perfect square (10.64b) below. Write $A=A_q(\varepsilon)$ and $\mathrm{tail}=A-r_0(\varepsilon)=\sum_{j\ge2}g_\varepsilon(d_j)\ge0$.

*Reduction.* Fix an excursion $\gamma\ne$ candidate. Either its first point $y_1$ is not $p-s$ or $1-p+s$, or it agrees with the candidate (up to reflection) for exactly $j\ge1$ steps and then takes a wrong branch at step $j+1$. In the first case Lemma 25.4(a) gives $d(y_1)\ge3a\ge\pi/q$, so $r_\varepsilon(y_1)\ge G_\varepsilon(d(y_1))$ by Lemma 25.1, and the total residual is at least $\min_{[3a,\pi]}G_\varepsilon$. In the second case the accumulated residual is $\ge r_\varepsilon(x_1)=r_0(\varepsilon)$ and the wrong-branch point $x'$ contributes, by Lemma 25.4(b),(c), either $\ge G_\varepsilon(d(x'))$ with $d(x')\ge3a-2a/q^{j+1}\ge d_3:=3a-2a/q^2\ge\pi/q$, or exactly

$$
g_\varepsilon\Bigl(d_1+(-1)^{j+1}\tfrac{2a}{q^{j+1}}\Bigr)+c_\varepsilon\Bigl(2a+(-1)^{j+1}\tfrac{4a}{q^{j}}\Bigr)
\ \ge\ R_{\rm dev}(\varepsilon):=\min\Bigl\{\min_{[d_1-2a/q^3,\,d_1]}g_\varepsilon+c_\varepsilon\bigl(2a-\tfrac{4a}{q^2}\bigr),\ \min_{[d_1,\,d_1+2a/q^2]}g_\varepsilon+2ac_\varepsilon\Bigr\}.
$$

All later residuals are $\ge0$. Therefore the theorem follows from the two inequalities

$$
\text{(C1)}\quad \min_{[d_3,\pi]}G_\varepsilon>A ,\qquad\qquad
\text{(C2)}\quad R_{\rm dev}(\varepsilon)>\mathrm{tail},
\tag{10.64}
$$

with $\mu_q(\varepsilon)$ the smaller of the two differences. Both sides of (C1) and (C2) are, as functions of $\varepsilon$, either affine ($A$, $r_0$, $\mathrm{tail}$) or minima of affine functions ($\min G_\varepsilon$, $R_{\rm dev}$), so each margin is concave in $\varepsilon$ and it suffices to verify (C1)–(C2) at the two endpoints $\varepsilon=-\tfrac1{20}$ and $\varepsilon=\varepsilon^+(q)$.

*What v1.5 printed here, and why it is replaced.* The v1.5 text verified the two endpoints $\varepsilon=-\tfrac1{20}$ and $\varepsilon=\tfrac14$ for $q\ge8$ by a chain of rounded constants that ended in the two brackets $1.95(1-2/q^2)/(q+1)-4.8/q^4-0.001$ and $0.96(1-2/q^2)/(q+1)-9.4/q^4-0.002$, asserted positive "for all $q\ge8$". They are not: the first is $-2.5488\times10^{-5}$ at $q=2000$ and the second $-1.0410\times10^{-3}$ at $q=1000$, because the tail was bounded by a $q$-independent constant ($0.001\,a^2$, $0.002\,a^4$) while every positive term tends to zero (v1.5 audit, finding F15-01; row W58 records the exact values). Two rounded constants in the same chain were also not valid lower bounds: $\sin(\pi/9)/(\pi/9)=0.97981\ldots<0.98$ and $2\cos(\pi/9)-1.2\pi\sin(\pi/9)=0.589999\ldots<0.59$. The conclusion of the theorem was not refuted — no counterexample to $E_q(\varepsilon)=A_q+\varepsilon B_q$ exists in any row — but the printed proof did not prove it for large $q$. The verification below is the audit's replacement (its Theorem A15-1), reproduced with attribution and re-derived here; it keeps the tail $q$-dependent on the negative side and closes the positive side at the true endpoint $\varepsilon^+(q)$ by an exact complete square, so that the theorem is now stated on $[-\tfrac1{20},\varepsilon^+(q)]$ rather than on $[-\tfrac1{20},\tfrac14]$.

*Negative endpoint $\varepsilon=-\tfrac1{20}$, analytic for $q\ge8$* ($a\le\pi/9$, so $3a\le\pi/3$ and $a^2<0.122$). Since $G_\varepsilon\ge g_\varepsilon$ on $[\pi/q,\pi]$ (because $c_\varepsilon\ge0$), it suffices to bound $g_\varepsilon$ from below on $[d_3,\pi-a]$ and $G_\varepsilon$ on $[\pi-a,\pi]$. By the sign analysis in the proof of Proposition 25.2, for $-\tfrac1{20}\le\varepsilon<0$ the function $h_\varepsilon/\cos\varphi=\frac{1-\tan(d/2)\tan(a/2)}{1+\tan(d/2)\tan(a/2)}+4|\varepsilon|\cos2\theta$ is strictly decreasing in $d$, so $g_\varepsilon$ increases on $[a,d^*]$ and decreases on $[d^*,\pi-a]$ for a single $d^*$, with $d^*\ge\pi/2-a\ge d_1+2a/q^2$ because $h_\varepsilon\ge\cos\theta>0$ wherever $\cos2\theta\ge0$. Hence $\min_{[d_3,\pi-a]}g_\varepsilon=\min\{g_\varepsilon(d_3),g_\varepsilon(\pi-a)\}$, and $g_\varepsilon\ge0$ on both short segments $[d_1-2a/q^3,d_1]$ and $[d_1,d_1+2a/q^2]$, which lie in the increasing range. Now, with all constants rounded conservatively:

$$
g_\varepsilon(d_3)\ge0.58\,a^2,\qquad g_\varepsilon(\pi-a)\ge0.58,\qquad \min_{[\pi-a,\pi]}G_\varepsilon\ge0.7,\qquad r_0(\varepsilon)\le0.305\,a^2,\qquad 0\le\mathrm{tail}\le\frac{2.4\,a^2}{q^2(q^2-1)}<0.001\,a^2 .
$$

The first is $g_\varepsilon''=\cos t+\tfrac15\cos2t\ge\cos3a-\tfrac15\ge0.3$ on $[a,d_3]$ together with $g_\varepsilon(a)=g_\varepsilon'(a)=0$ and $(d_3-a)^2=4a^2(1-q^{-2})^2\ge4a^2(63/64)^2$. The second is $g_\varepsilon(\pi-a)=2\cos a-(\pi-2a)(\sin a+\tfrac1{10}\sin2a)\ge2\cos a-1.2\pi\sin a$, which at $a=\pi/9$ equals $0.589999\ldots$ and increases as $a$ decreases; $0.58$ is a valid bound where v1.5's $0.59$ was not. The third is $G_\varepsilon=G_0+\varepsilon m$ with $m\ge0$ and $m\le m(\pi)\le6a^2$ on $[\pi-a,\pi]$, and $G_0\ge\cos a-\tfrac a2\sin a$ there (proof of Proposition 25.2), so $G_\varepsilon\ge\cos a-\tfrac a2\sin a-0.3a^2\ge0.84$ at $a=\pi/9$. The last two are $|g_\varepsilon''|\le1.2$, $c_\varepsilon\le1.2\sin a/(q+1)$, $r_0\le\tfrac12(1.2)(2a/q)^2+2.4a^2/(q+1)$, and the geometric sum $\mathrm{tail}=\sum_{j\ge2}g_\varepsilon(d_j)\le0.6\sum_{j\ge2}(2a/q^j)^2=2.4a^2/[q^2(q^2-1)]$ — the tail is kept **$q$-dependent**, which is the whole repair. Then $A=r_0+\mathrm{tail}\le0.306\,a^2<0.58\,a^2\le\min_{[d_3,\pi]}G_\varepsilon$, which is (C1). For (C2), since $g_\varepsilon\ge0$ on both short segments no derivative loss has to be subtracted at all:
$$
R_{\rm dev}(\varepsilon)\ \ge\ 2ac_\varepsilon\bigl(1-2/q^2\bigr)\ \ge\ \frac{1.95\,a^2(1-2/q^2)}{q+1},
$$
using $c_\varepsilon\ge\sin a/(q+1)$ and $\sin a\ge a(1-a^2/6)>0.975\,a$ for $a\le\pi/9$ (this is where $1.95$ comes from; $1.96$ would need $\sin a/a\ge0.98$, which fails at $a=\pi/9$). Therefore
$$
C_2(-\tfrac1{20})=R_{\rm dev}-\mathrm{tail}\ \ge\ a^2\Bigl[\frac{1.95(1-2/q^2)}{q+1}-\frac{2.4}{q^2(q^2-1)}\Bigr]>0\qquad(q\ge8),
\tag{10.64a}
$$
because after multiplication by $q+1$ the positive term is at least $1.95\cdot\tfrac{31}{32}=1.889$ while the negative one is $2.4/[q^2(q-1)]\le2.4/448=0.0054$. This closes every $q\ge8$ without enumeration. (If one prefers to keep v1.5's derivative loss $4.8a^2/q^4$, the bracket $1.95(1-2/q^2)/(q+1)-4.8/q^4-2.4/[q^2(q^2-1)]$ is also positive for all $q\ge8$: substituting $q=t+8$ its numerator is a polynomial in $t$ with all coefficients positive, row C59.)

*Positive endpoint $\varepsilon=\varepsilon^+(q)$, analytic for every even $q\ge4$ (complete square).* At $\varepsilon=\varepsilon^+(q)=1/(4\cos a)$ the tent slope vanishes, $c_\varepsilon=0$, and substituting $\cos2d=2\cos^2d-1$ into (10.52) gives, for every $d\in[0,\pi]$, the exact identity
$$
\boxed{\ r_{\varepsilon^+}(x)=g_{\varepsilon^+}(d(x))=G_{\varepsilon^+}(d(x))=\frac{(\cos d(x)-\cos a)^2}{2\cos a}\ }
\tag{10.64b}
$$
(row C59 checks it symbolically). The residual is a perfect square, non-negative, and zero only at $d=a$, i.e. on $\Omega$ — so Proposition 25.2 holds at the endpoint with no sign condition on $c_\varepsilon$, and the inequalities (C1)–(C2) are estimates of one explicit function $w(d)=(\cos d-\cos a)^2/(2\cos a)$, which is increasing in $d$ on $[a,\pi]$. Put
$$
K_q=\frac{2a^2\sin^2a}{\cos a},\qquad D_q=\Bigl(1-\frac1{q^2}\Bigr)^2-\frac{(1+2/q)^2}{q^2-1}\ \ge\ D_4=\Bigl(\frac{15}{16}\Bigr)^2-\frac{9/4}{15}=\frac{933}{1280}>0 .
$$
The candidate points satisfy $0<a-2a/q^2\le d_j\le d_1\le3\pi/10<\pi/2$, so $|\cos d_j-\cos a|\le\sin d_1\,|d_j-a|=\sin d_1\cdot2a/q^j$ with $\sin d_1=\sin((1+2/q)a)\le(1+2/q)\sin a$ (concavity of $\sin$ on $[0,\pi/2]$); hence
$$
A_q+\varepsilon^+B_q=\sum_{j\ge1}w(d_j)\le K_q\frac{(1+2/q)^2}{q^2-1},\qquad
\mathrm{tail}=\sum_{j\ge2}w(d_j)\le\frac{K_q}{q^2}\frac{(1+2/q)^2}{q^2-1}.
$$
On the other side, $\cos a-\cos d\ge\sin a\,(d-a)$ for $d\in[a,\pi-a]$, so $\min_{[d_3,\pi]}w=w(d_3)\ge K_q(1-q^{-2})^2$, and the nearest point of the two candidate-type deviation segments is $d_1-2a/q^3$, at distance $(2a/q)(1-q^{-2})$ from $a$, so $R_{\rm dev}=\min w$ over the segments $\ge K_q(1-q^{-2})^2/q^2$. Therefore
$$
C_1(\varepsilon^+)\ \ge\ K_qD_q>0,\qquad C_2(\varepsilon^+)\ \ge\ \frac{K_qD_q}{q^2}>0\qquad\text{for every even }q\ge4 ,
\tag{10.64c}
$$
with no case distinction and no enumeration. Row C59 encloses $C_1(\varepsilon^+)$ and $C_2(\varepsilon^+)$ directly from the series for $q=4,\dots,40$ and confirms in each case that they exceed the closed-form lower bounds (e.g. $C_1\ge0.640$, $C_2\ge0.0248$ at $q=4$ against $K_4D_4=0.246$, $K_4D_4/16=0.0154$).

*The old endpoint $\varepsilon=\tfrac14$.* It is no longer an endpoint of the argument, since $\tfrac14<\varepsilon^+(q)$ and concavity covers it. For the record, v1.5's chain at $\varepsilon=\tfrac14$ is repaired in the same way — its tail is $\le4.7a^4/[q^2(q^2-1)]$ rather than $0.002\,a^4$, and the resulting bracket $0.96(1-2/q^2)/(q+1)-9.4/q^4-4.7/[q^2(q^2-1)]$ is positive for all $q\ge8$ by the same positive-coefficient certificate (row C59) — but nothing below depends on it.

*Exact verification for $q=4,6$ at the negative endpoint.* Row C56 evaluates (C1) and (C2) at $\varepsilon\in\{-\tfrac1{20},0,\tfrac14\}$ for $q=4$ and $q=6$ in directed rational interval arithmetic ($\pi$ by Machin's formula, $\cos$ and $\sin$ by Taylor series with remainders, the minima over the three intervals by the mean-value form on $120$ sub-intervals, the series $A_q,B_q$ with an explicit tail). The certified margins at $\varepsilon=-\tfrac1{20}$ are $C_1\ge0.6435$, $C_2\ge0.1805$ for $q=4$ and $C_1\ge0.5556$, $C_2\ge0.0721$ for $q=6$; the v1.5 audit's independent implementation (a global derivative bound with a $256$-cell covering, not the mean-value engine) certifies the same two points with margins $0.6424,\,0.1805$ and $0.5547,\,0.0721$. The positive endpoint of these two cases is (10.64c), as for every $q$.

*Concavity.* Both margins are concave in $\varepsilon$, so positivity at $\varepsilon=-\tfrac1{20}$ (analytic for $q\ge8$, exact for $q=4,6$) and at $\varepsilon=\varepsilon^+(q)$ (analytic for all $q$) gives positivity on all of $[-\tfrac1{20},\varepsilon^+(q)]$, and $c_\varepsilon\ge0$ holds throughout by Proposition 25.2. This proves (10.62) on the stated interval, with $\mu_q(\varepsilon)$ the smaller of the two margins.

*Consequence (10.63).* Given (10.62), the duality argument of §10.9 — $h_*(u)=\inf_t\{P_{q,\varepsilon}(-t)-t\beta_q(\varepsilon)+tu\}$, the minimisers tending to $+\infty$ as $u\downarrow0$, and the two-sided exponential bounds on the pressure defect — applies verbatim with $A_q$ replaced by $A_q+\varepsilon B_q$. $\square$

#### 10.10.3 The certified intervals for each $q$

The uniform interval $[-\tfrac1{20},\varepsilon^+(q)]$ is what the analytic argument gives for every $q$ at once. For each fixed $q$ the same two inequalities can be certified further to the left, and row C56 does so for $q=4,6,\dots,40$ at two **rational** points $\varepsilon_{\rm lo}(q)<0<\varepsilon_{\rm hi}(q)$ chosen strictly inside $(-\eta_2(q),\varepsilon^+(q))$: $\varepsilon_{\rm hi}(q)=\lfloor10^4/(4\cos a)\rfloor/10^4$ and $\varepsilon_{\rm lo}(q)=-\lfloor10^3(\eta_2(q)-0.003)\rfloor/10^3$ (the floating computation is used only to choose these rationals; their validity is then certified exactly, and the row requires $c_\varepsilon>0$, which excludes $\varepsilon^+$ itself). By concavity the inequalities hold between the two certified points; combining with the endpoint certificate (10.64c) at $\varepsilon^+(q)$ and concavity once more, one obtains, for every even $4\le q\le40$,
$$
E_q(\varepsilon)=A_q+\varepsilon B_q\qquad\text{for all }\ \varepsilon\in\bigl[\varepsilon_{\rm lo}(q),\ \varepsilon^+(q)\bigr] ,
\tag{10.65}
$$
e.g. $[-\tfrac{41}{125},\varepsilon^+(4)]=[-0.328,0.30902]$ for $q=4$, $[-\tfrac{371}{500},\varepsilon^+(6)]=[-0.742,0.27748]$ for $q=6$, $[-\tfrac{257}{200},\varepsilon^+(8)]=[-1.285,0.26604]$ for $q=8$. Three things must be said precisely, because v1.5 did not (audit finding F15-02). First, (10.65) is the conclusion of **C56 together with (10.64c) and concavity**, not of C56 alone: C56 by itself reaches only $\varepsilon_{\rm hi}(q)$, which is below $\varepsilon^+(q)$ (for $q=6$, $0.2774$ against $\varepsilon^+(6)=0.277479\ldots$; v1.5 printed "$0.2775$", which exceeds both). Second, the left endpoint $\varepsilon_{\rm lo}(q)$ is a rational strictly inside the proved range of Part A, and **no row certifies the whole negative range** $(-\eta_2(q),\varepsilon_{\rm lo}(q))$; v1.5's phrase "the entire proved range of Proposition 25.2" is withdrawn and replaced by (10.65) as stated. Third, the endpoints of (10.65) are those of the *proof* of Part A — the tent slope $c_\varepsilon\ge0$ on the right, the lossy bound $\min_{[\pi/2,\pi]}G_\varepsilon\ge G_0(\pi/2)-\eta\,m(\pi)$ on the left — and not failure points of (C1)–(C2), whose margins remain large at $\varepsilon_{\rm lo}$ (at $\varepsilon=-\eta_2(q)$ the true minimum of $G_\varepsilon$ over $[\pi/2,\pi]$ is $0.82$ for $q=4$ and $0.94$ for $q=8$; row V57). A draft of this subsection in v1.5 asserted that (C1) fails "slightly before Part A does"; that was an artefact of a search that had the Part A range built into it, and remains withdrawn.

#### 10.10.4 What the two inequalities decide, and what is not claimed

*Sufficient, not necessary.* The proved implication is $(\mathrm{C1})\wedge(\mathrm{C2})\Rightarrow E_q(\varepsilon)=A_q+\varepsilon B_q$, **under** the standing hypotheses that $r_\varepsilon\ge0$ with zero set $\Omega$ (Proposition 25.2, which supplies the Aubry set for Lemma 25.5) and $c_\varepsilon\ge0$ (Lemma 25.1). The converse is not proved. v1.5 described (10.64) as a procedure that "decides, for any $(q,\varepsilon)$ in the family, whether the closed form persists"; that overstates it (audit finding F15-04). The correct statement is: *the inequalities provide a sufficient certificate for the proposed optimal excursion once the non-negative residual and the Aubry-set hypotheses have been established; a failed or unresolved test is inconclusive.* In particular, no value of $\varepsilon$ outside the certified intervals is decided either way by a failure of (C1)–(C2).

*The positive side: a bracket, not a value.* v1.5 reported the "true transition" $\varepsilon^*(q)$ from an exhaustive search over periodic orbits of period $\le10$ ($q=4$), $\le8$ ($q=6$), $\le6$ ($q=8$), found the period-four orbit $aabb$ as the first competitor, and stated that the transition "is where the excursion cost $A_q+\varepsilon B_q$ becomes free". Both statements are withdrawn (audit finding F15-03). A finite-period enumeration, however exhaustive within its period bound, cannot exclude a longer periodic orbit or a non-periodic invariant measure from crossing earlier; affinity of $\int f_\varepsilon\,d\nu$ in $\varepsilon$ makes each orbit's crossing a closed formula but makes no orbit the global first competitor. And the numbers themselves contradict the "free cost" reading: at $q=4$ the period-four crossing $0.370398$ is strictly *below* $A_4/|B_4|=0.371648$, so when this competitor appears the single-repeat cost is still positive. What is proved is the two-sided bracket of §10.11, $\varepsilon^+(q)\le\varepsilon_{\rm crit}(q)\le\varepsilon_4(q)$, with both ends explicit; the "within $2\%$ at $q=8$" of v1.5 survives only as a statement about the **width of that bracket** relative to its upper end, and never meant that the common endpoint $\tfrac14$ is within $2\%$ of anything. Row V57 keeps the finite-period search as a diagnostic; its PASS does not fix the transition. On $(\varepsilon^+(q),\varepsilon_4(q))$ the two-cycle is still the minimiser in every finite search, but the reduction of Part B needs $c_\varepsilon\ge0$ and gives nothing, so the pressure exponent there is **[OPEN]**; the same tent sub-action does certify $r_\varepsilon\ge0$ on a fine grid up to $0.3537$ for $q=4$ and $0.2910$ for $q=6$ (row V57), so Part A could be extended by a finite computation, but no extension is claimed. The fixed point $x_f=\tfrac12-\tfrac1{2(q-1)}$ of $T_q$ nearest $\tfrac12$, with $d(x_f)=\pi/(q-1)$, crosses the two-cycle at
$$
\varepsilon_f(q)=\frac{\cos d_f-\cos a}{\cos2d_f-\cos2a}
\tag{10.66}
$$
($0.3820,0.2924,0.2716,0.2531$ at $q=4,6,8,20$; $\varepsilon_f-\varepsilon^+=\pi^2/(4q^3)+O(q^{-4})$), later than the period-four orbit; it is one more explicit upper bound on $\varepsilon_{\rm crit}$, weaker than $\varepsilon_4$.

*The negative side is not sharp, and the loss is in the proof, not in the sub-action.* The same tent $u_\varepsilon$ certifies $r_\varepsilon\ge0$ with zeros only on $\Omega$ far below $-\eta_2(q)$: on a fine grid, down to $-1.877$ for $q=4$, $-3.253$ for $q=6$ and $-5.052$ for $q=8$ (row V57), about three times $\eta_2(q)$, and (C1)–(C2) hold there too with $c_\varepsilon>0$. What stops at $-\eta_2(q)$ is only the two-line bound $G_\varepsilon\ge G_0(\pi/2)-\eta\,m(\pi)$ in the proof of Proposition 25.2, which is lossy because $m$ changes sign on $[\pi/2,\pi]$ and $G_0(\pi)>G_0(\pi/2)$. A sharper certified left endpoint is a finite computation (a rigorous minimisation of $G_\varepsilon$ over $[\pi/2,\pi]$ at the endpoint); it is not carried out here, and the true left transition of the minimiser is **[OPEN]**.

*What is proved and what is imported.* Part A is elementary and self-contained. Part B imports the existence-and-identification theorem of Leplaideur–Mengue exactly as §10.9 does; the additional content is the exact competitor geometry (10.60), which removes the global Lipschitz loss of the v1.4-audit argument, the reduction of the whole question to the two explicit inequalities (10.64), and — new in v1.6, from the v1.5 audit — the complete-square identity (10.64b) that closes the positive endpoint for every $q$ and the $q$-dependent tail that closes the negative endpoint for $q\ge8$. Nothing here concerns additive perturbations other than the first harmonic (the multiplicative class of §10.12 is a different family), and nothing here concerns the actual spin band of Section 9: the alignment capacity $\kappa^\pm(z)$ of Conjecture 9.2 is untouched.

*Why it matters for the programme.* The value of Proposition 24.1 was that a barrier cost could be computed in closed form for one potential. Theorem 25 shows that the closed form persists on an explicit interval, with the optimal excursion and its cost stable and not merely the optimal measure — which is more than the qualitative locking of §12.5 supplies. It supplies a **sufficient certificate with a certified domain**, not a general decision procedure; the reusable object is the pair of inequalities together with the hypotheses under which they are conclusive. The actual spin first-loss exponent is not advanced by it.

### 10.11 The positive transition: a certified bracket and its asymptotics — Theorem 26

**Provenance.** This section and §10.12 were derived by the v1.5 audit (ChatGPT, OpenAI; its report §§6–7, rows C15-05, C15-06, C15-07, W15-02 of its independent script). They are reproduced here with attribution after independent re-derivation of every displayed constant in this session (rows C60–W63, plus a separate mpmath/sympy recheck), and are not counted as the author-side system's own results.

Define the onset of a competitor on the positive side, without any assumption about *which* measure competes first:
$$
\varepsilon_{\rm crit}(q)=\sup\bigl\{\varepsilon\ge0:\ \mu_\Omega\text{ minimises }\int f_t\,d\nu\ \text{for every }0\le t\le\varepsilon\bigr\}.
$$
The minimising condition is the intersection, over all invariant $\nu$, of the affine inequalities $\int f_t\,d\mu_\Omega\le\int f_t\,d\nu$ in $t$, so the set of such $t$ is a closed interval and the definition is sound; it does not presuppose that the first competitor is periodic or of any particular period, and it distinguishes losing minimality from losing uniqueness.

**Theorem 26 [PROVEN; supplied by the v1.5 audit, re-derived here].** Let $q\ge4$ be even, $a=\pi/(q+1)$. Put
$$
x_0=\frac{q(q-1)}{2(q^2+1)},\qquad \mathcal O_4=\{T_q^kx_0:\ 0\le k<4\},
$$
the orbit of the base-$q$ word $k\,k\,(k+1)\,(k+1)$ with $k=q/2-1$ (for $q=4$: $\{\tfrac6{17},\tfrac7{17},\tfrac{11}{17},\tfrac{10}{17}\}$). It has minimal period $4$, its angular distances alternate between $d_+=\pi(q+1)/(q^2+1)$ and $d_-=\pi(q-1)/(q^2+1)$, each taken twice, and with $C_4=\tfrac12(\cos d_-+\cos d_+)$, $D_4=\tfrac12(\cos2d_-+\cos2d_+)$ its mean of $f_\varepsilon$ is $-C_4+\varepsilon D_4$. Hence the crossing with the two-cycle is the explicit value
$$
\varepsilon_4(q)=\frac{\cos a-C_4}{\cos2a-D_4},
\tag{10.67}
$$
whose numerator and denominator are both positive, and
$$
\boxed{\ \varepsilon^+(q)\ \le\ \varepsilon_{\rm crit}(q)\ \le\ \varepsilon_4(q)\qquad(q\ge4\text{ even}).\ }
\tag{10.68}
$$
Moreover, with $x=1/q$,
$$
\varepsilon_4(q)=\frac14+\frac{\pi^2}{8q^2}+O(q^{-4}),\qquad
\varepsilon^+(q)=\frac14+\frac{\pi^2}{8q^2}-\frac{\pi^2}{4q^3}+O(q^{-4}),
\tag{10.69}
$$
so that
$$
\boxed{\ q^2\Bigl(\varepsilon_{\rm crit}(q)-\frac14\Bigr)\longrightarrow\frac{\pi^2}{8},\qquad 0\le\varepsilon_{\rm crit}(q)-\varepsilon^+(q)\le\frac{\pi^2}{4q^3}+O(q^{-4}).\ }
\tag{10.70}
$$

*Proof.* $T_qx_0=qx_0\bmod1$: writing $u=\pi q/(q^2+1)$ and $v=\pi/(q^2+1)$, the four points have angular distances $d_+=u+v$, $d_-=u-v$, $d_+$, $d_-$ in turn (for $q=4$: $\tfrac{5\pi}{17},\tfrac{3\pi}{17},\tfrac{5\pi}{17},\tfrac{3\pi}{17}$), and $T_q^4x_0=x_0$ since $q^4\equiv1\pmod{q^2+1}$ and $q$ is even; the four points are distinct, so the period is exactly $4$ (row C60 checks the orbit in exact rationals for $q\le40$). Then $C_4=\cos u\cos v$ and $D_4=\cos2u\cos2v$. Since $a<u\le4\pi/17<\pi/4$ and $0<v<u$, one has $C_4<\cos u<\cos a$ and $D_4<\cos2u<\cos2a$, so both numerator and denominator of (10.67) are positive. For $\varepsilon>\varepsilon_4(q)$ the orbit has strictly smaller mean than $\mu_\Omega$, which gives the upper bound in (10.68); the lower bound is Proposition 25.2. For (10.69), $\cos a-\cos u\cos v$ and $\cos2a-\cos2u\cos2v$ are analytic in $x$ near $0$ with a common zero of order exactly $3$ (numerator $\pi^2x^3+O(x^4)$), so their quotient is analytic and its Taylor coefficients are those printed (row C61, exact symbolic series); $\varepsilon^+=1/(4\cos(\pi x/(1+x)))$ is expanded directly. Squeezing (10.68) between (10.69) gives (10.70). $\square$

| $q$ | proved lower end $\varepsilon^+(q)$ | period-four upper end $\varepsilon_4(q)$ | relative width $(\varepsilon_4-\varepsilon^+)/\varepsilon_4$ | $A_q/\lvert B_q\rvert$ |
|---:|---:|---:|---:|---:|
| 4 | 0.3090169944 | 0.3703980775 | 16.57% | 0.371648 |
| 6 | 0.2774790660 | 0.2914034279 | 4.78% | 0.291502 |
| 8 | 0.2660444431 | 0.2714366262 | 1.99% | 0.271454 |
| 10 | 0.2605542791 | 0.2632083635 | 1.01% | 0.263213 |
| 20 | 0.2528238333 | 0.2531382138 | 0.124% | 0.253138 |
| 40 | 0.2507357084 | 0.2507744526 | 0.0155% | 0.250774 |

(Displayed values; row C60 holds the exact rational enclosures and certifies $\varepsilon^+<\varepsilon_4<A_q/|B_q|$ for every even $q\le40$.) Two remarks. The last column is the point where the single-repeat cost $A_q+\varepsilon B_q$ vanishes; it lies strictly **above** $\varepsilon_4(q)$, which is why v1.5's sentence "the transition is where the excursion becomes free" is false and is withdrawn — the cost formula, proved only on $[-\tfrac1{20},\varepsilon^+]$, cannot be extrapolated past its domain to locate a transition. And (10.70) is a statement about the limit: it determines the leading correction of $\varepsilon_{\rm crit}(q)$ without asserting the finite-$q$ equality $\varepsilon_{\rm crit}(q)=\varepsilon_4(q)$, which is **[OPEN]** (row V57's finite-period search finds no earlier competitor of period $\le10$ at $q=4$, and that is all it finds).

### 10.12 A weighted complete-square class: a sufficient condition and a switching counterexample — Proposition 27

**Provenance.** As for §10.11: derived by the v1.5 audit (its Proposition A15-2 and §7.3), reproduced with attribution and re-derived here. It answers, in a restricted form, the question left as a target in v1.5 ("try $\cos6\pi x$"): it is a **multiplicative** family with the zero set and the complete-square factor fixed, not the additive family $f_\varepsilon+\eta\cos6\pi x$, which was open in v1.6 and is treated in §§10.13–10.14 of the present revision.

**Proposition 27 [PROVEN; supplied by the v1.5 audit].** Fix an even $q\ge4$ and let $h:[0,\pi]\to(0,\infty)$ be Lipschitz with $0<m\le h\le M$ and
$$
\frac Mm<R(q):=\frac{(q^2-1)(1-q^{-2})^2}{(1+2/q)^2}\ \ \Bigl(\ge R(4)=\frac{375}{64}\Bigr).
\tag{10.71}
$$
For the potential $W_{q,h}(x)=h(d(x))\,(\cos d(x)-\cos a)^2/(2\cos a)$ on the circle, the minimal ergodic average is $0$, attained only by $\mu_\Omega$; the zero-temperature pressure exponent is the explicit series
$$
\boxed{\ \lim_{t\to\infty}-\frac1t\log P_{T_q}(-tW_{q,h})=E_{q,h}=\sum_{j\ge1}h(d_j)\,\frac{(\cos d_j-\cos a)^2}{2\cos a},\ }
\tag{10.72}
$$
attained by the single-repeat excursion of Lemma 25.3 and its reflection only; and the Lebesgue rate function of $W_{q,h}$ has endpoint coefficient $\lim_{u\downarrow0}[\log q-\mathcal I_{W_{q,h}}(u)]/[u\log(1/u)]=1/E_{q,h}$.

*Proof.* $W\ge0$ with zero set $\Omega$; after coding it is Lipschitz, the Aubry set of $-W$ is the period-two orbit, and Leplaideur–Mengue's Theorem A applies as in Lemma 25.5 ($W=O(\operatorname{dist}(x,\Omega)^2)$ controls the completion cost of finite paths geometrically). With $K_q$ as in (10.64c), the candidate cost and its tail are bounded above by $MK_q(1+2/q)^2/(q^2-1)$ and $MK_q(1+2/q)^2/[q^2(q^2-1)]$; the pointwise cost of a non-candidate branch is at least $mK_q(1-q^{-2})^2$ and of a candidate-type wrong branch at least $mK_q(1-q^{-2})^2/q^2$, by the same monotonicity of $(\cos d-\cos a)^2$ as in (10.64c). Every other excursion therefore costs at least
$$
\mu_{q,h}\ \ge\ \frac{mK_q}{q^2}\Bigl[(1-q^{-2})^2-\frac Mm\frac{(1+2/q)^2}{q^2-1}\Bigr]>0
$$
more than the candidate, which is (10.71); the entropy statement is the duality of §10.9. $\square$

*A higher-harmonic instance.* $h_\eta(d)=1+\eta\cos3d$ with $|\eta|<\tfrac{311}{439}$ satisfies $(1+|\eta|)/(1-|\eta|)<\tfrac{375}{64}$ (equality exactly at $\tfrac{311}{439}$), so (10.71) holds for every even $q\ge4$ at once. Since $\cos3d=-\cos6\pi x$, this potential contains the third harmonic on the circle; at $\eta=\tfrac12$ row C62 encloses $E_{q,h}=0.0170683645750$, $0.0028271572023$, $0.0006790132054$, $0.0002060033990$, $0.0000039976755$ for $q=4,6,8,10,20$ (60 terms plus a non-negative tail bound), with certified excursion gaps $\tfrac12K_qD^{(3)}_q/q^2\ge0.00452,\,0.000927,\,0.000212,\,0.0000632,\,0.00000124$. For fixed $h$ the first term dominates and $q^6E_{q,h}\to2\pi^4h(0)$; in particular $q^6E_q(\varepsilon^+(q))\to2\pi^4$, a different order from $q^3A_q\to2\pi^2$ at $\varepsilon=0$ (10.42). No interchange of the $q\to\infty$ and $t\to\infty$ limits is claimed.

*Example 27.1 [the ratio hypothesis cannot be dropped; supplied by the v1.5 audit].* Take $q=4$, $a=\pi/5$, $w(d)=(\cos d-\cos a)^2/(2\cos a)$, and the positive Lipschitz weight $h_R(d)=1+(R-1)\phi(d)$ with $\phi$ the triangular bump of half-width $\pi/1000$ centred at $7\pi/40$ — the candidate's second angular distance $d_2=a(1-2/16)=7\pi/40$ exactly. Every other candidate point avoids the bump ($|d_j-a|\le\pi/160$ for $j\ge3$ while $|7\pi/40-a|=\pi/40$), so the candidate cost is exactly $C(R)=E_0+(R-1)w_2$ with $E_0=\sum_jw(d_j)=0.0315148470$ and $w_2=w(7\pi/40)=0.0011761069$. The alternative backward excursion $x'_1=\tfrac7{20}$, $x'_j=(\tfrac25\text{ or }\tfrac35)-1/(16\cdot4^{j-2})$ for $j\ge2$ (even/odd $j$), which takes the other near-ground inverse branch at the second step and then follows the ground branches, has $T_4x'_1=\tfrac25$, $T_4x'_j=x'_{j-1}$, angular distances $d'_1=3\pi/10$, $d'_j/\pi=\tfrac15+(-1)^j/(8\cdot4^{j-2})$, avoids the bump entirely, and costs $D=0.0829097465$ independently of $R$. Hence at $R=64$ the candidate ($C(64)=0.1056096$) is strictly non-optimal by $0.0226998$, while Proposition 27 guarantees its optimality for $1\le R<\tfrac{375}{64}$. Defining $R_{\rm crit}$ as the upper end of the interval of $R$ on which the candidate is optimal (all path costs are affine in $R$, so this is an interval),
$$
\boxed{\ \frac{375}{64}\le R_{\rm crit}\le R_{\rm alt}=1+\frac{D-E_0}{w_2}=44.699173\ldots\ }
\tag{10.73}
$$
(row W63, exact enclosures). This is a switch of the optimal **excursion** at fixed minimising measure $\mu_\Omega$, not a change of ground state; the alternative path is a witness and is not claimed globally optimal, and neither $R_{\rm crit}$ nor the optimality of the ratio (10.71) is determined.

*What §§10.11–10.12 close and what they leave.* Closed: the large-$q$ gap in the proof of Theorem 25 on its original interval; the positive endpoint $\varepsilon^+(q)$ for every even $q$; the leading $q^{-2}$ correction of the positive transition; a sufficient condition fixing the optimal excursion on the weighted complete-square class; and an explicit positive Lipschitz weight that switches the excursion, with a certified bracket of the switching contrast. Open: the exact finite-$q$ transition on either side; the necessity of (C1)–(C2); the global additive-family phase diagram (local stability and a derived sub-action are now supplied by §§10.13–10.14); and the arithmetic alignment of the actual spin spectrum.

### 10.13 An explicit additive neighbourhood and reduction to two excursions — Theorem 28

**Question and provenance.** Proposition 27 starts with a prescribed non-negative weighted square. It does not by itself construct a sub-action for a raw additive perturbation. The present section constructs that missing object, including perturbations without reflection symmetry. The construction, proof and counter-tests in §§10.13–10.15 were developed for v1.7 by the OpenAI system; they are not attributed to the v1.6 audit or to its author-side system. The pressure representation is imported from Leplaideur–Mengue as in Lemma 25.5, and the inverse-branch geometry is inherited from Lemma 25.4 and Proposition 27. The additional obligation is a quantitative, constructive reduction from a raw potential to that geometry.

Fix an even integer $q\ge4$, $a=\pi/(q+1)$, $c=\cos a$, $p=q/[2(q+1)]$, $p_0=p$, $p_1=1-p$, and $\Omega=\{p_0,p_1\}$. Derivatives below are with respect to the circle coordinate $x\in\mathbb R/\mathbb Z$, not the angle $2\pi x$. Write
\[
 F_0(x)=\cos2\pi x+\varepsilon^+(q)\cos4\pi x,\quad
 m_0=-c+\varepsilon^+(q)\cos2a,\quad
 w_q(x)=F_0(x)-m_0=\frac{(\cos2\pi x+c)^2}{2c}.
\tag{10.74}
\]
Thus $w_q=(\cos d-c)^2/(2c)$ is the square already used in Proposition 27. For a real $\psi\in C^2(\mathbb R/\mathbb Z)$ put
\[
 \bar\psi=\frac{\psi(p_0)+\psi(p_1)}2,\qquad
 H_q=(q+1)\left(3+\frac8{q-1}\right),\qquad
 \mathcal N_q(\psi)=\frac{c}{16\sin^2(a/2)}
 \left[\|\psi''\|_\infty+(q^2+1)H_q\|\psi'\|_\infty\right].
\tag{10.75}
\]
This is a seminorm insensitive to additive constants. It bounds an explicitly constructed residual; it is not a fitted tolerance or a claim of an optimal radius.

**Theorem 28 [PROVEN; constructive additive stability and exact two-path reduction].** Suppose $\rho:=\mathcal N_q(\psi)\le1/2$. For the raw potential $F_\psi=F_0+\psi$:

1. A periodic $C^{1,1}$ sub-action $u_\psi$, given below, has residual
\[
 r_\psi=F_\psi-(m_0+\bar\psi)+u_\psi\circ T_q-u_\psi,
 \qquad (1-\rho)w_q\le r_\psi\le(1+\rho)w_q.
\tag{10.76}
\]
In particular, the unique minimising invariant measure is the uniform measure on $\Omega$, its mean is $m_0+\bar\psi$, and the Aubry set is this single period-two component.

2. As in Lemma 25.5, excursions are read from their first off-orbit inverse step; inserting zero-cost motion along $\Omega$ does not define a different excursion. Let $s=1/[q(q+1)]$, $\omega_j=p_0$ for odd $j$ and $p_1$ for even $j$, and $x_j=\omega_j-sq^{1-j}$. Define bounded linear functionals
\[
 L_q^+(\psi)=\frac{\psi(p_0)-\psi(p_1)}2+\sum_{j\ge1}[\psi(x_j)-\psi(\omega_j)],\qquad
 L_q^-(\psi)=\frac{\psi(p_1)-\psi(p_0)}2+\sum_{j\ge1}[\psi(1-x_j)-\psi(1-\omega_j)].
\tag{10.77}
\]
With $E_0=\sum_{j\ge1}w_q(x_j)=A_q+\varepsilon^+(q)B_q$, the exact pressure exponent is
\[
 \boxed{\ E_q(\psi)=\lim_{t\to\infty}-\frac1t
 \log\bigl(P_{T_q}(-tF_\psi)+t(m_0+\bar\psi)\bigr)
 =E_0+\min\{L_q^+(\psi),L_q^-(\psi)\}.\ }
\tag{10.78}
\]
Only the two displayed excursions can minimise. The one with the smaller functional is the unique minimising excursion; on their equality hyperplane both minimise. Every excursion other than these two has a strictly larger cost, with the uniform-in-path margin
\[
 \mu_q(\rho)=\frac{K_q}{q^2}
 \left[(1-\rho)(1-q^{-2})^2
 -(1+\rho)\frac{(1+2/q)^2}{q^2-1}\right]>0,
 \qquad K_q=\frac{2a^2\sin^2a}{c}.
\tag{10.79}
\]
The losing member of the two candidates is not asserted to have this margin: their costs can be arbitrarily close.

3. The Lebesgue large-deviation rate function of $F_\psi$ has endpoint coefficient
\[
 \lim_{u\downarrow0}\frac{\log q-\mathcal I_{F_\psi}(m_0+\bar\psi+u)}{u\log(1/u)}=\frac1{E_q(\psi)}.
\tag{10.80}
\]
No limit in $q$ is exchanged with $t\to\infty$ or $u\downarrow0$.

*Proof: construction rather than an assumed zero set.* Let $v_i=\psi(p_i)$ and $z_i=\psi'(p_i)$. Prescribe
\[
 b_0=(v_0-v_1)/4,\quad b_1=-b_0,\qquad
 t_0=-\frac{z_0+qz_1}{q^2-1},\quad
 t_1=-\frac{qz_0+z_1}{q^2-1}.
\tag{10.81}
\]
On each of the two positively oriented arcs from $p_i$ to $p_{1-i}$, with lengths $\ell=1/(q+1)$ and $1-\ell$, respectively, use cubic Hermite interpolation. On an arc of length $L$, at normalised position $z\in[0,1]$, set
\[
 u=(2z^3-3z^2+1)b_i+(-2z^3+3z^2)b_{1-i}
 +L(z^3-2z^2+z)t_i+L(z^3-z^2)t_{1-i}.
\tag{10.82}
\]
The values and first derivatives agree at both joins, including the periodic join. Thus $u=u_\psi$ is globally $C^{1,1}$; its second derivative need not be continuous. Direct substitution in (10.81) gives, for $R_\psi:=\psi-\bar\psi+u\circ T_q-u$,
\[
 R_\psi(p_i)=0,\qquad R_\psi'(p_i)=z_i+qt_{1-i}-t_i=0.
\]
The sign and the factor $q$ in this equation are essential; row C65 checks the equations symbolically for arbitrary values and slopes.

Let $N_1=\|\psi'\|_\infty$. The shorter arc gives $|b_0-b_1|\le N_1\ell/2$, while $|t_i|\le N_1/(q-1)$. Differentiating (10.82) twice and using $|12z-6|\le6$, $|6z-4|,|6z-2|\le4$ shows, on either arc,
\[
 \|u''\|_\infty\le\frac{6|b_0-b_1|}{L^2}
 +\frac{4(|t_0|+|t_1|)}L\le H_qN_1.
\]
Here $u''$ is interpreted almost everywhere. Therefore $R_\psi'$ is globally Lipschitz, with constant at most
$D_\psi=\|\psi''\|_\infty+(q^2+1)H_qN_1$.
Taylor's formula with an integral remainder along a shortest arc to $\Omega$ gives
$|R_\psi(x)|\le D_\psi\operatorname{dist}(x,\Omega)^2/2$.
This remains valid when an arc crosses a Hermite join or a branch of $T_q$: the periodic $C^1$ matching removes a derivative jump, and the Lipschitz derivative bound is global.

For $d\in[0,\pi]$, the elementary identity for the difference of two cosines yields
\[
 |\cos d-\cos a|
 =2\sin((d+a)/2)\sin(|d-a|/2)
 \ge\frac{2\sin(a/2)}\pi|d-a|.
\]
Since $|d(x)-a|=2\pi\operatorname{dist}(x,\Omega)$,
\[
 w_q(x)\ge\frac{8\sin^2(a/2)}c\operatorname{dist}(x,\Omega)^2.
\tag{10.83}
\]
Combining these inequalities proves $|R_\psi|\le\rho w_q$ and hence (10.76). The residual has zero set exactly $\Omega$. Integrating against an invariant measure proves the minimum and its uniqueness; the non-negative residual and its quadratic vanishing identify the symbolic Aubry set exactly as in Lemma 25.5. The two points belong to one irreducible component, not two components.

*Exclusion of all other paths.* This step does not assume reflection symmetry of $r_\psi$. By the geometry of Lemma 25.4 and the square estimates in Proposition 27, the square cost of either candidate is at most $K_q(1+2/q)^2/(q^2-1)$ and its tail after the first point is at most this quantity divided by $q^2$. A non-candidate first inverse branch has square cost at least $K_q(1-q^{-2})^2$. If a path first follows one of the candidates and then takes a wrong branch, that branch has square cost at least $K_q(1-q^{-2})^2/q^2$. All subsequent residuals are non-negative. Subtract the corresponding candidate cost in the first case, and cancel the common prefix then bound the candidate's remaining tail in the second. Using (10.76) gives at least (10.79) in either case. Positivity follows from
\[
 \frac{1+\rho}{1-\rho}\le3<\frac{375}{64}\le R(q).
\]
This treats a first deviation at any finite index, however late. A path with no first deviation is the candidate itself. Thus no unenumerated infinite competitor is hidden in the reduction.

*Evaluation of the two surviving costs.* Subtract $r_\psi(\omega_j)=0$ from the residual at $x_j$ and sum. The $u$ differences telescope to
$u(x_0)-u(\omega_0)-[u(x_N)-u(\omega_N)]$. Here $x_0=p_0$ but $\omega_0=T_q\omega_1=p_1$; thus the limit is $b_0-b_1=(v_0-v_1)/2$, not zero. This endpoint compensation is exactly the first term in (10.77), and what remains is $E_0+L_q^+(\psi)$. Reflection of the path gives the second functional even when the potential itself is not reflection invariant. Both series converge absolutely, with the useful certified tail
\[
 \left|\sum_{j>N}[\psi(x_j)-\psi(\omega_j)]\right|
 \le\frac{\|\psi'\|_\infty}{q^2-1}q^{-N},
\tag{10.84}
\]
and the same bound for the reflected path. The pressure representation from Lemma 25.5 now proves (10.78). In particular the minimum is positive, also directly because $r_\psi\ge w_q/2$. The endpoint duality in §10.9 proves (10.80). $\square$

*Cohomology check of the endpoint term.* If $\psi=h-h\circ T_q+C$ with $h\in C^2$, then $\bar\psi=C$. The endpoint term in $L_q^+$ is $h(p_0)-h(p_1)$, while its series telescopes to the negative of that value. Thus $L_q^+=L_q^-=0$, as invariance of the normalised pressure under a constant plus a coboundary requires. Omitting the endpoint compensation would fail this structural check even before a numerical comparison. This identity does not extend the non-coboundary stability domain of the theorem.

**Scope of the advance.** This is an open neighbourhood of arbitrary $C^2$ additive perturbations modulo constants, not only functions pre-factored by a square and not only even perturbations. Its radius depends on $q$ and is deliberately conservative. The qualitative persistence of a periodic Aubry set is already known; the additional output here is an explicit construction, an explicit all-path gap and the evaluated two-functional cost on the displayed neighbourhood. It does not classify all locking regions, prove robustness in the $C^0$ norm, or determine the spin-spectrum alignment capacity.

### 10.14 The additive third harmonic: a finite triangle and transition asymptotics — Corollary 29

Write
\[
 f_{\varepsilon,\eta}(x)=\cos2\pi x+\varepsilon\cos4\pi x+\eta\cos6\pi x,
 \quad D_q^{(h)}=\frac{3(4c^2-1)}{4c},\quad
 \varepsilon_b(q,\eta)=\frac1{4c}+D_q^{(h)}\eta.
\tag{10.85}
\]
The superscript distinguishes $D_q^{(h)}$ from the gap constant $D_q$ in (10.64c). Put $e_0=-1/20$, and let $\mathcal T_q$ be the closed triangle with vertices
\[
 (e_0,0),\qquad (\varepsilon_b(q,1/24),1/24),\qquad
 (\varepsilon_b(q,-1/24),-1/24).
\tag{10.86}
\]
Equivalently, $t=(\varepsilon-e_0-D_q^{(h)}\eta)/(\varepsilon^+-e_0)$ satisfies $0\le t\le1$ and $|\eta|\le t/24$. This has nonempty two-dimensional interior and contains $(0,0)$ in its interior. No zero set has been imposed on the raw potential.

**Corollary 29 [PROVEN].** On $\mathcal T_q$, the unique ground measure is $\mu_\Omega$, its mean is
$-c+\varepsilon\cos2a-\eta\cos3a$, the only optimal excursions are the single-repeat path and its reflection, and
\[
 \boxed{\ E_q(\varepsilon,\eta)=A_q+\varepsilon B_q+\eta C_q,\qquad
 C_q=\sum_{j\ge1}(\cos3a-\cos3d_j).\ }
\tag{10.87}
\]
The endpoint entropy coefficient is its reciprocal.

There is also an open neighbourhood of $(\varepsilon^+,0)$, including points with $\varepsilon>\varepsilon^+$, on which the same conclusions hold. An explicit sufficient condition is
\[
 K_{q,2}|\varepsilon-\varepsilon^+|+K_{q,3}|\eta|\le\tfrac12,\qquad
 K_{q,k}=\frac{c}{16\sin^2(a/2)}
 \big[(2\pi k)^2+(q^2+1)H_q(2\pi k)\big].
\tag{10.88}
\]
In particular the unperturbed positive transition satisfies the strictly improved lower bound
\[
 \varepsilon_{\rm crit}(q)\ge\varepsilon^+(q)+\frac1{2K_{q,2}}>\varepsilon^+(q).
\tag{10.89}
\]
The radii in C66 are exact rational values at or below $1/(2K_{q,2})$. Their approximate values for $q=4,6,8,10$ are $0.0001520392$, $0.0000290601$, $0.0000083856$, $0.0000031013$, respectively. This is a proved, small extension; it is not the exact transition.

For each fixed $|\eta|\le1/24$, define $\varepsilon_{\rm crit}(q,\eta)$ as the upper endpoint of the closed interval of $\varepsilon$ for which $\mu_\Omega$ minimises $f_{\varepsilon,\eta}$. The interval is nonempty by its point $\varepsilon_b(q,\eta)$; no assumption that its left endpoint is zero is made. Set $u_q=\pi q/(q^2+1)$, $v_q=\pi/(q^2+1)$, and
$\Delta_m=\cos(ma)-\cos(mu_q)\cos(mv_q)$. Then
\[
 \boxed{\ \varepsilon_b(q,\eta)<\varepsilon_4(q,\eta):=
 \frac{\Delta_1+\eta\Delta_3}{\Delta_2},\qquad
 \varepsilon_b(q,\eta)\le\varepsilon_{\rm crit}(q,\eta)\le\varepsilon_4(q,\eta).\ }
\tag{10.90}
\]
The following expansions are uniform for $|\eta|\le1/24$:
\[
 \begin{split}
 \varepsilon_b(q,\eta)&=\frac{1+9\eta}{4}
 +\frac{\pi^2(1-15\eta)}{8q^2}
 -\frac{\pi^2(1-15\eta)}{4q^3}+O(q^{-4}),\\
 \varepsilon_4(q,\eta)&=\frac{1+9\eta}{4}
 +\frac{\pi^2(1-15\eta)}{8q^2}+O(q^{-4}).
 \end{split}
\tag{10.91}
\]
Consequently
\[
 q^2\left(\varepsilon_{\rm crit}(q,\eta)-\frac{1+9\eta}{4}\right)
 \longrightarrow\frac{\pi^2(1-15\eta)}8,
\tag{10.92}
\]
uniformly on this fixed $\eta$ interval. The exact finite-$q$ equality with $\varepsilon_4(q,\eta)$ remains open.

*Proof.* At the boundary $\varepsilon=\varepsilon_b(q,\eta)$ the derivative of
$-\cos d+\varepsilon\cos2d-\eta\cos3d$ at $d=a$ vanishes. Polynomial division in $y=\cos d$ gives the exact identity
\[
 f_{\varepsilon_b,\eta}(x)-f_{\varepsilon_b,\eta}(p)
 =\big[1-\eta(3+4c^2+8c\cos d)\big]w_q(x).
\tag{10.93}
\]
For $|\eta|\le1/24$, the weight lies between $3/8$ and $13/8$, since
$|3+4c^2+8c\cos d|\le15$. Its ratio is at most $13/3<375/64\le R(q)$. Proposition 27 therefore evaluates the cost at every boundary point and establishes its two optimal paths. A general point of (10.86) is a convex combination of $f_{e_0,0}$ and $f_{\varepsilon_b(q,\eta/t),\eta/t}$, with coefficients $1-t,t$. At $t=0$ use Theorem 25 directly. At $t>0$, the sub-action is $(1-t)c_{e_0}d$, because the boundary potential needs only the constant sub-action. Its residual is the same convex combination of two non-negative residuals with zero set $\Omega$. Every competing path is more expensive than either common candidate at each endpoint, so its excess cost at the combination is at least the same convex combination of positive endpoint gaps. The cost is affine by telescoping, which proves (10.87). The open diamond (10.88) follows by applying Theorem 28 to
$\psi=(\varepsilon-\varepsilon^+)\cos4\pi x+\eta\cos6\pi x$; reflection makes its two functionals equal. Together with Theorem 25, it proves (10.89).

For the transition, the period-four orbit of Theorem 26 has potential difference from the two-cycle equal to
$\Delta_1-\varepsilon\Delta_2+\eta\Delta_3$. The already proved $\Delta_2>0$ gives the upper crossing. At $\varepsilon_b$ the difference is strictly positive by (10.93), since none of the four points is in $\Omega$, establishing the first strict inequality in (10.90). Invariance imposes affine inequalities in $\varepsilon$, so the minimising set is an interval and its upper endpoint has the displayed bracket. With $x=1/q$, $\Delta_2=4\pi^2x^3+O(x^4)$; expanding the numerator and denominator and removing this common zero gives (10.91). Row C68 checks that subtracting the displayed quotient times the denominator cancels every coefficient through degree six, with $\eta$ symbolic. Analyticity at the removable zero and compactness of the $\eta$ interval make the remainder uniform. Squeezing proves (10.92). $\square$

**What has changed.** The additive two-parameter question now has an explicit two-dimensional region, a derived sub-action, all-path exclusion, exact barrier and a parameter-dependent transition asymptotic. The stronger request for a complete phase diagram or an exact finite-$q$ transition is not solved. A different ground orbit is not necessary to solve a stability question: on this region the original orbit survives by proof, despite the additive perturbation changing the raw potential's pointwise minima.

### 10.15 A path switch without a change of the ground measure — Corollary 30

Consider the reflection-breaking family
\[
 F_\eta(x)=F_0(x)+\eta\sin2\pi x,\qquad |\eta|\le\frac1{2K_{q,1}},
\tag{10.94}
\]
with $K_{q,1}$ from (10.88). The bound is explicit and positive for every even $q\ge4$.

**Corollary 30 [PROVEN].** The minimum ergodic average remains $m_0$ and its unique measure remains $\mu_\Omega$ throughout (10.94). Nevertheless the exponent is
\[
 \boxed{\ E_q(\eta)=E_0-|\eta|\mathcal L_q,\qquad
 \mathcal L_q=\sin a+\sum_{j\ge1}(-1)^{j+1}(\sin d_j-\sin a)>0.\ }
\tag{10.95}
\]
For $\eta>0$ the reflected excursion is the unique optimum, and for $\eta<0$ the original excursion is the unique optimum; at zero both minimise. Thus $E_q$ has a corner at zero while the ground measure and ground mean do not change. This concerns the zero-temperature exponential rate, not a singularity of pressure at finite temperature.

*Proof.* The sine has zero mean on $\Omega$, and reflection negates it. On the original path
$\sin2\pi x_j-\sin2\pi\omega_j=(-1)^{j+1}(\sin d_j-\sin a)$.
Here $d_j-a$ has sign $(-1)^{j+1}$ and all intervening angles lie in
$[a(1-2/q^2),a(1+2/q)]\subset(0,\pi/2)$; the largest upper endpoint is $3\pi/10$ at $q=4$. The endpoint term from (10.77) is $\sin a$, and every term in the displayed series is positive. More quantitatively,
\[
 \sin a+\frac{2a\cos(a(1+2/q))}{q-1}\le\mathcal L_q\le\sin a+\frac{2a}{q-1}.
\tag{10.96}
\]
Apply Theorem 28, using $\mathcal N_q(\eta\sin2\pi x)\le|\eta|K_{q,1}\le1/2$. Its two costs are $E_0\pm\eta\mathcal L_q$ and all other paths have the positive gap (10.79). This gives the formula and uniqueness assertions. $\square$

The ground-state locking and the choice of the cheapest excursion are therefore different observables. Proposition 27's bump example already separated them at a large multiplicative contrast; (10.95) does so for arbitrarily small smooth additive perturbations, with an exact switching law. A corner arising from a minimum of linear costs is familiar in max-plus theory; no claim that corners or selection by costs are new concepts is made. The additional result is the constructive all-path reduction and explicit sine law for the circle family.
## 11. The upstream chain: initial ideas, the physical corpus and the same derivation chain

### 11.1 The role of every input

The integration does not merge sentences of different types into one proof. The initial intuition supplies questions, the operating rules fix what evidence a claim needs, the upstream papers supply the allowed operators and the remaining debts, and the earlier seed and the spatial-record note supply the two computable models.

| Input | What was integrated | Position and force here |
|---|---|---|
| founding research note (initial ideas) | the founding questions of time–space, wave–particle, and a Z-Spin that mediates relations | the physical target of this section; spatial records are not identified with the origin of time |
| operating rules and research kernel | user mission first, corpus text first, types/assumptions/evidence/history, disclosure of independence | the contract of the whole document and Appendices V, H |
| breakthrough and deep-exploration rules | rounds with minimal inputs, counterexamples and replacement objects, research that solves the actual bottleneck | the rounds of the seed and Section 9 |
| manuscript, verification-artifact and audit rules | central contribution, source comparison, executable and failure evidence, paper qualification | Sections 12–14, the companion script, JSON and self-test |
| 11D existence–change–observation seed (v1.4) | the roles of $2,3,6$, the two non-identical $3$s, observer pairing, classical subalgebras, composition and cocycle | Section 11.2: hypotheses connected to dynamical record objects; no 11-dimensional derivation is claimed |
| the Book (v14.0) | the research chain at the time of 220 papers, the formal/physical, rank/energy, state/clock distinctions, retractions and upstream debts | Section 11.3; a synthesis snapshot that does not override the current M70/M71 |
| Mission (v1.7) | FQ/RQ, research-grade floor 3 and the four paper criteria | Section 13 |
| supplied history H0001–H0375 | the lineage of decisions and failures | H0376 is provided as a separate append file; past wording is not rewritten |
| seed v1.8 with its code, self-test and agent audit | state space, preparation and cooling, source spectrum, clock, Gauss/current, finite-time instrument, optical output | Sections 2–5, Appendices S, L, V; errors replaced as in the repair ledger |
| the spatial-record note with its code | observational equivalence of histories, order contrast of two memories, response rank, current commutators, projection counterexample, dilution limit | Sections 6–8 and Appendix N; the three files form one claim/verification lineage |
| the earlier readiness review and its eight new checks | the B19 counterexample, signed average versus total variation, the need for actual transport and a preparation map | the replacement theorems of Sections 3–8 |

### 11.2 Connecting the hypotheses of the 11D seed to operational objects

The arithmetic of the 11D seed — $(1\oplus X_3)\otimes(1\oplus Z_2)$ is twelve-dimensional and the dimensions of its non-identity components sum to eleven — is exact in its declared vector space. But choosing $B_3\to A_3^*$ in $A_3\otimes B_3$ and deriving that choice dynamically are different things. This paper supplies the following correspondence.

| Research question of the 11D seed | Object made explicit here | Arrow still open |
|---|---|---|
| H24, H28: observer pairing and commutation | the commuting pointer algebra reading $Y_A,X_B$ and the explicit dephasing channel | why this pairing and pointer are selected by S14 |
| H30: the residue of composition and time | the different joint memories produced by $U_BU_A$ and $U_AU_B$; the iterated integrals of N3 | derivation of the order parameter as physical time or a positive Hamiltonian clock |
| R9, R10: algebras of objects and events | actual Hilbert spaces, complete CPTP preparation/writing/storage maps, observational history equivalence | the upstream selection of the space, its subsystem split and the action |
| R11: cocycle clock | the distinct operational times of waiting, writing and storage | the additive cocycle of time, the metric, the origin of spacetime |
| R12: the Z interface | the explicit map carrying the C6 contrast to a neutral carrier and a pointer | whether this map arises from the actual action of the Z-sector |

The dimension of the 64-dimensional writing model is not adjusted to $Q=11$; the several candidate representations of $2,3,6,12$ in the 11D seed are not summed as independent evidence; and the history recovery of the note deals only with observational equivalence classes of finite memories, not with a recoverable storage of the complete past of the universe in present space.

### 11.3 What is joined and what remains open in S14–M69–M70–M71

The earlier manuscript and supplied audit record consultation of the corpus index and ZS-M71 v1.4.1 §7. For v1.3, the current debt registry, constants/lemmas index and M70/M71 update log were rechecked; the full upstream proofs were not re-audited. In the earlier search record, the index snapshot available to this work contains no entry for a first-loss exponent, an alignment capacity or the two-boundary capacity formula (NOT_FOUND, not ABSENT). The Book's paper counts and versions were not used as the sole basis of the current state. This paper does not modify any repository canonical file.

Appendix S8 preserves the boundary current, the charge grading, the zero-frequency shift, the Gauss-law reduction, the actual gap/dipole/rate computation and the finite-time map including the no-photon outcome of the M70 lineage. Appendix N9 preserves the order sensitivity and the danger of the positive-band projection when that current is coupled to two spatial memories. To join them the following must be computed on the same physical object.

| Upstream obligation | Conditional object already computed | Current state |
|---|---|---|
| D-M69-MOVING, the moving carrier | the 24-dimensional sequential model and the 64-dimensional fixed-Hamiltonian writing interval on the full space | OPEN: transport, recoil, bulk leakage and common Coulomb error of the actual occupied packet |
| D-M69-INSTRUMENT / K17, K18 | the admissible C6 effect, the preparation map, the neutral-memory instrument | OPEN: selection of apparatus, pointer, subsystem and update rule in S14 |
| D-S14-EVENT-001 | postselection-free probabilities and trace distances with commuting pointers | OPEN: action-derived single actual outcome and Born event |
| D-HCLK-001 | $t_w,\tau,t_s$ for given Hamiltonians and the conditional performance of clock readouts | OPEN, and the obligation is narrower than "an external time scale remains": separating the waiting, writing and storage times is useful but does not prove that the record clock and the modular/seam clock of the upstream chain are the *same* clock; that identity, and the clock bridge it requires, is what is missing |
| Gauss/source matching | the finite electrostatic model of S8, the source-only sufficient condition of S6.13 and its counterexample | OPEN: choice of the spin coefficients from the actual CAR/CCR source, geometry, units, renormalisation |
| stability after writing | parity storage after explicit capture, computed $\chi$ and error window | OPEN: action derivation of capture, environment rates and protection resources |

None of these debts is closed. The new results do not declare them solved; they complete which actual computations, once done, can be substituted into which lower bound. The contribution to the physical targets FQ/RQ is a refinement of the conditional bridge; the mathematical results of the closed quantum models stand in their own scope.

## 12. Prior work and what is actually added

### 12.1 Central comparison for the spectral engine and the first-loss task

The following compares designated equations and theorems of the sources with the present results; "not subsumed" means that the source's conclusion does not yield the present statement, not that the world literature contains no such result. The comparison date is 2026-09-14/15.

| Source and location | What the source gives | Correspondence and addition here |
|---|---|---|
| Bovier, *Metastability: a potential theoretic approach*, §3 (3.7)–(3.9), Thm. 4.7, Cor. 5.7 | capacity variational principle of reversible dynamics and the metastable exit/eigenvalue relation | the capacity engine is IMPORTED; Theorem 1 evaluates the constants of a finite Ehrenfest compression with two hard walls and closes the remainder uniformly; Theorem 2 moves from the Markov exit time to the first loss of a coherent cosine contrast |
| Navascués–Popescu, *How energy conservation limits our measurements*, §5.3 (32)–(34), Appendix E | adjacent-coherence optimisation of an energy-limited battery, path ceiling and sine profile | the symmetric restriction of effects and the sine optimisation are IMPORTED; connecting that value to the time-dependent loss of a prepared sector ground band and to the storage contrast of spatial records is added |
| Bartlett–Rudolph–Spekkens–Turner, *Degradation of a quantum reference frame*, §II, §IV C (21), §V | number of uses and success rate under repeated-measurement backaction; quadratic longevity | $B^2$ itself is not a novelty basis; Theorem 2 concerns Hamiltonian phase differences of the unused state on a macroscopic band and does not claim to improve the number-of-uses theorem |
| Bartlett–Rudolph–Sanders–Turner, *Degradation of a quantum directional reference frame as a random walk*, §II (1)–(5) | directional reference degradation with trivial dynamics between measurements | a different task (idle dynamics); the earlier attribution of this reference to other authors was an error and is corrected |
| Wright–Walls–Garrison, *Collapses and revivals in the interference between two BECs*, (20)–(22) | adjacent coherence of the number distribution and collapse/revival from quadratic phase dispersion | the physical mechanism of the fixed-window Theorem 3 is of the same lineage; the exponentially small non-quadratic gap profile and the loss quantiles of Theorem 2 are not a change of variables of these equations |
| Koch et al., *Charge-insensitive qubit design derived from the Cooper pair box*, §II B (2.5) | exponential suppression of offset-charge dispersion at large $E_J/E_C$ | conceptual precedent that localisation suppresses charge sensitivity; the Hamiltonian and observables of hard-wall spin compression, two-boundary binomial rates and first-loss computation are different |
| McCulloch–Jacoby–Gopalakrishnan, *Long-lived local quantum coherences from hydrodynamic large deviations*, §III (15), §IV (22)–(27), (29)–(34) | diffusing many-body charge and coherence-void conditioned dynamics; weak-noise stationary saddle and noiseless aging | the link between long-lived coherence and large deviations is prior; the spatial void and tilted evolution differ from the sector hard wall of a finite source; the $B$-dependent first-passage quantile interval of Theorem 2 is not provided |
| ZS-M71 v1.4.1, §7.2 T-JCE (R3), §7.3 T-JB (R5), T-SBC | joint/separable reference optimisation at fixed bandwidth under the same admissible measurement and a strict cost gap | the operational graph and ceiling are INHERITED; the centre here is the waiting time of the supplied source and the memory dynamics after writing; the separability result of M71 is not re-published |

The strongest overlap attack reads: "Theorem 1 recomputes a one-dimensional capacity, and the rest is known quantum control." The attack is correct for the auxiliary engines and for several constructions, and the paper does not place its central contribution in their invention. The central added statements are Theorem 2 with its rigorous application — the loss-dependent first-time interval from uniformly controlled spectrum and weights without assuming phase alignment — and the resolution of its exact exponent in Section 9. Without the uniform difference control of Theorem 1 the exponential size of the gaps alone does not yield the interval; without Theorem 7 the interval would remain an unexplained pair of fronts.

### 12.2 Comparison for the exact-exponent results of Section 9

**Historical v1.2 comparison record.** The current source correspondence and novelty assessment are in §12.4; unresolved labels below record the earlier assessment.

| Source and location | What the source gives | Correspondence and addition here |
|---|---|---|
| Fejér (1915); Szegő (1926); Egerváry–Szász (1928), as stated in Dimitrov's survey *Extremal positive trigonometric polynomials*, Theorem 6 | for a non-negative trigonometric polynomial $1+\sum_{k\le n}(a_k\cos k\theta+b_k\sin k\theta)$, $\sqrt{a_1^2+b_1^2}\le2\cos(\pi/(n+2))$, with the extremal polynomial a squared modulus of a sine-profile polynomial | IMPORTED. Theorem 8 uses the extremal kernel inside a Riesz product; the value $\cos(\pi/(m+2))$ of the alignment gain is the Fejér constant. Extremality is used only to say that no degree-$m$ kernel does better in this argument |
| Sidon's theorem for Hadamard lacunary series, as stated in Kahane's survey *Lacunary Taylor and Fourier series*, §II.1 | for Hadamard lacunary frequencies the norms $\sum\vert a_n\vert $ and $\sup\vert P\vert $ are equivalent, with a constant $K(q)$ | IMPORTED as lineage; Theorem 8 is the one-sided, positive-weight, finite-time-window version with explicit constants and explicit $O(1/N)$ window errors, which is what the first-loss problem needs |
| Riesz products (classical; Zygmund, *Trigonometric Series*, Ch. V) | non-negative products $\prod(1+a_k\cos n_kt)$ with lacunary $n_k$ and their Fourier expansion | the method is classical; the combination with degree-$m$ Fejér kernels and the finite-window bookkeeping of Theorem 8 are the additions; no claim that the product itself is new |
| Bousch, *Le poisson n'a pas d'arêtes* (2000), and Jenkinson's survey *Ergodic optimization in dynamical systems* (§3, Theorem 6.2) | for the doubling map the maximising measures of $\cos2\pi(x-\theta)$ are Sturmian; for expanding maps and Lipschitz $f$ a Lipschitz sub-action (revelation) exists | IMPORTED as context and as the general existence of sub-actions. Theorem 9 does not rely on them for $q=2,4$: the sub-actions (9.5) and (iii) are explicit and elementary. The mapping of the first-loss exponent of integer-ratio spectra to ergodic optimisation of $x\mapsto qx$ is the addition |
| Fejér kernel positivity (classical) | $F_n\ge0$ | IMPORTED; used in the upper-end construction of Theorem 7 |
| *The first passage time in quantum dynamics* (Physica A, 2026), located by title only | a first-passage notion in quantum dynamics | not examined in full text; listed as an unread nearby title, not as a comparison |

| Aistleitner, Gantert, Kabluchko, Prochno, Ramanan, *Large deviation principles for lacunary sums* (arXiv:2012.05281; accepted manuscript read at the NSF public-access copy) | an LDP for $n^{-1}\sum_k\cos(2\pi a_kx)$ with $a_k=q^k$, a transfer-operator representation of the rate function $I_q$ (§3.3 normalisation), the odd/even symmetry discussion after Lemma 2.3, and Theorem D / Remark 2.5 showing that perturbations preserving the ratio limit $2$ can change the LDP | **the closest external statement of the question answered by Theorem 16.** Both versions read state, in §2.2 immediately after Lemma 2.3: "For even $q$, it remains unclear whether $I_q(-1)$ is finite (and in fact, it is not even clear whether $I_q(x)$ is finite for all $-1<x<0$)." Theorem 16 answers both halves for every even $q$: the effective domain is exactly $[-\cos\frac\pi{q+1},1]$, so $I_q(-1)=+\infty$ and $I_q$ is finite on $(-\cos\frac\pi{q+1},0)$ and infinite below. Their Theorem D / Remark 2.5 is the external analogue of the ratio-profile counterexample (9.11) |
| Frühwirth, Juhos, Prochno, *The large deviation behavior of lacunary sums* | LDP for Lipschitz observables along geometric systems via transfer operators; Example 1.3(3) exhibits a telescoping (coboundary) degeneracy | the coboundary mechanism is known in this literature; the effective-domain endpoint for the cosine and every even $q$ is not computed there. Not applicable to drifting real spin frequencies with a growing finite horizon |
| Aistleitner et al., *Moment generating functions and moderate deviation principles for lacunary sums* (2025); Prochno–Strzelecka, *Moderate deviation principles for lacunary trigonometric sums*, Math. Nachr. (2026), §1.2 Theorems 1–2 | small-parameter MGF and moderate-deviation universality; for the cosine the stated range is $\sqrt n\ll y_n\ll n/\log n$ | central and moderate deviations are not extreme alignment or first passage. v1.1 recorded the 2026 article as unreachable (publisher 403); the v1.1 audit read the publisher version and reports that its theorems live strictly between the central limit theorem and the large-deviation regime, so they do not compute the endpoint of $\mathcal I_q$; an independent read of the companion arXiv text confirms that scaling range. The access caveat of v1.1 is therefore removed, and this source does **not** subsume Theorem 16 |

Search scope for Section 9: lacunary trigonometric sums and Sidon sets, Riesz products, extremal non-negative trigonometric polynomials, ergodic optimisation of expanding circle maps, large deviations of lacunary sums, collapse and dephasing times of quasi-periodic sums. No source was found that formulates the first-loss exponent of a lacunary rate spectrum, and NOT_FOUND is not read as ABSENT.

**Novelty status of the v1.1 results, stated exactly.** For Theorem 13 at $q=2$ the value $\beta_2=\tfrac12$ is a special case of Bousch's Sturmian theorem, so only the uniform treatment of every even $q$ by one explicit Lipschitz sub-action, and the uniqueness of the maximising measure, are candidates for novelty; whether an equivalent trigonometric inequality is already in the ergodic-optimisation or positive-polynomial literature is **OPEN-NOVELTY**. For Theorem 14 the Riesz-product method and the sparsification device are classical; the candidate is the explicit finite-time constant for arbitrary real ratios $\rho>1$ with no slow variation of the weights. For Theorem 16 the pressure route is entirely standard and the only new input is Theorem 13, which is why it is typed DERIVED COROLLARY; its interest is that the question it answers is stated as unresolved in the source read here. A short elementary proof is not a reason to lower a result, and an unresolved novelty comparison is not a reason to raise one.

### 12.3 Comparison for the spatial-record results

| Source and location | Already known | Use here |
|---|---|---|
| Christandl–Datta–Ekert–Landahl, *Perfect state transfer in quantum spin networks*, (13)–(15) | the $\sqrt{n(N-n)}$ coupled $S_x$ chain and the perfect-transfer time | the transport engine of Theorem 4 is IMPORTED/SPECIALIZED; the two gated histories on the full space with capture and timing errors are built for the present record task |
| Mitchison–Jozsa–Popescu, *Sequential weak measurement*, §III (7)–(10) | several pointer responses of sequential couplings and order information | the note's N1 computes all outcomes of the strong Pauli construction exactly; no claim of first discovery of the principle that order remains in pointer correlations |
| Fewster–Verch, *Quantum fields and local measurements*, Thm. 3.5 (3.29)–(3.30) | causal composition of local measurements and compatibility of spacelike orders | precedent for history composition; the finite graph of Theorem 4 supplies no relativistic local field theory or spacetime derivation |
| Campbell et al., *Collisional unfolding of quantum Darwinism*, §II (1)–(3) | sequential collisions of a system with environment ancillas and information distribution | precedent for comparing accumulation with fresh resources against re-contact cost; the note's distinction that the size of space alone does not guarantee record recovery is kept |

| Present result | Class | Role in the manuscript |
|---|---|---|
| two-boundary finite capacity inequality, compact remainder, gap/weight uniformity, diffusive-scale formula | DERIVED/SPECIALIZED lemmas on an IMPORTED engine; Theorem 10 NEW in its explicit form | complete the missing assumptions of the central time theorem in the actual spin model |
| exact cumulative, finite envelopes, loss-exponent interval (Theorem 2) | **EXTENDED, central** | rigorous interval and stronger upper bound for a non-trivial first-time problem |
| sharpness, alignment capacity, integer-ratio values, Riesz–Fejér bound (Theorems 7–9) | **NEW** in formulation and combination; ingredients IMPORTED; the v1.0 proofs of Theorems 7 and 8 repaired in v1.1 | settle what determines the exponent and compute it for arithmetic classes |
| tent sub-action and $\beta_q=\cos\frac\pi{q+1}$ for every even $q$, with uniqueness (Theorem 13) | **NEW**, elementary; $q=2$ subsumed by Bousch | closes the even-$q$ case that v1.0 left as a grid observation |
| sparse Riesz bound for real ratios and $\kappa^-\ge\tfrac14$, $\limsup\le q_{4\ell/5}$ for the standard band (Theorems 14–15) | **NEW** constant on a classical method | first positive lower bound on alignment for the actual physical band, and the first strict narrowing of the v1.0 interval |
| effective domain and endpoints of the lacunary rate function (Theorem 16) | **DERIVED COROLLARY** of Theorem 13 and standard pressure theory | answers a question stated as unresolved in the source read here |
| fixed-window remainder and crossing stability (Theorem 3) | INHERITED leading term + DERIVED extension | unify the different scaling path and exclude the wrong global resource verdict |
| 64-dimensional writing, timing error, actual preparation channel (Theorems 4, 5) | CONSTRUCTED/SPECIALIZED | fill the empty interface with concrete maps |
| parity storage, Poisson dynamics, composed error window (Theorem 6) | IMPORTED channel algebra + DERIVED-in-model | separate and compute writing and storage lifetimes on the same observable |
| inherited current/Gauss/WW/optical results and N3–N5 | INHERITED / SPECIALIZED / CONDITIONAL | physical connection, counterexamples and limits; not counted as separate central novelty |

The comparison scope is finite quantum reference degradation, truncated spin/Ehrenfest spectra, capacity and quasi-stationarity, collapse/revival, sequential memories, perfect transfer, hydrodynamic coherence, lacunary series and ergodic optimisation. The full text of Chazottes–Collet–Méléard, the exact K6 correspondence of Schöll et al., the full microscopic derivation of the hydrodynamic paper, and all latest follow-up papers were not reviewed in full here; none of them is a premise of the present theorems, and none is carried as "reviewed".

### 12.4 Current primary-source comparison and the contribution boundary

**Read status and date.** The following comparison updates the v1.2 search record in §12.2, as of 2026-09-15. The named primary texts were retrieved and their relevant definitions and theorem statements inspected; proofs were inspected where a proposed transfer depended on them. This is a bounded comparison, not a proof of worldwide priority. The current executable result does not grade novelty. The original paper already contained T13–T16: their survival and clarified comparison are not new v1.3 discoveries.

| Closest result and exact location | Source assumptions, object and conclusion | Mapping to M72 and the additional obligation |
|---|---|---|
| Aistleitner–Gantert–Kabluchko–Prochno–Ramanan, *Large deviation principles for lacunary sums*, **Theorem B** and the paragraph after Lemma 2.3, printed p. 515 | Integer geometric frequencies, Lebesgue phase, observable $\cos(2\pi x)$; an LDP and properties of its rate function. The even-ratio negative range is left undetermined there. | Same map and observable. T13 computes the minimum invariant average for every even ratio; T16 then gives the exact effective domain and both endpoint values. The full interior rate function is not computed; Corollary 23 adds an explicit affine upper envelope on the whole domain, exact at $s=-\beta_q,0,1$. *(v1.3 cited Theorem A of that paper here. Theorem A is the large-gap theorem, whose hypothesis $a_{k+1}/a_k\to\infty$ excludes geometric progressions; the geometric case with the rate function $I_q$ is Theorem B. The pointer is corrected in v1.4.)* [Published primary text](https://mediatum.ub.tum.de/doc/1695199/wecu289shj4exnyvifycditp8.S0002-9947-2022-08788-2.pdf). |
| Gao, *Regularity of calibrated sub-actions for circle expanding maps and Sturmian optimization*, Theorems A/2.3 and B/3.8, start of §3 | General integer degree in the regularity theorem; the cosine-translation optimization application explicitly fixes degree two. | Existence and regularity of a sub-action are imported methodology. They do not evaluate the extreme average for each even degree. Degree two overlaps the classical result; T13's added content is the explicit formula, global tent inequality and equality set for all even degrees. [Primary text](https://arxiv.org/pdf/2105.10767). |
| Fan–Schmeling–Shen, *L∞-estimation of generalized Thue–Morse trigonometric polynomials and ergodic maximization*, definition of $f_c$ and Theorem 4.1 | All integer degrees $q$, with $f_c(x)=\log\vert \sin(q\pi(x+c))/\sin(\pi(x+c))\vert $; a unique $q$-Sturmian maximizing measure for that potential. | This is the strongest apparent all-degree overlap. Its logarithmic, possibly singular potential differs from $-\cos(2\pi x)$. Taking a nonlinear function does not preserve optimizing averages. Its conclusion cannot be substituted for T13 without an additional argument, which is not supplied by that theorem. [Primary text](https://arxiv.org/pdf/1903.09425). |
| Frühwirth–Juhos–Prochno, *The large deviation behavior of lacunary sums*, Theorem B, Corollary 1.2 and Example 1.3 | LDPs for more general periodic observables and geometric dilations, with nontrivial coboundary dependence. | The general LDP/pressure mechanism is an import, not an M72 innovation. It does not give the evaluated all-even cosine extreme or replace the equality-set proof needed for the endpoint entropy. [Primary text](https://arxiv.org/pdf/2107.12860). |
| Aistleitner–Frühwirth–Hauke–Manskova, *Moment generating functions and moderate deviation principles for lacunary sums*, Theorem 1 and moderate-deviation consequences | Small-parameter cumulant-generating estimates and a scaling between the central-limit and large-deviation regimes. | These estimates do not take the negative zero-temperature limit needed by T16. The comparison excludes this specific proposed overlap; it does not assert that no later work exists. [Primary text](https://arxiv.org/html/2502.20930v2). |
| Gao–Shen–Zhang, *Typicality of periodic optimization over an expanding circle map*, Theorems A–C | Typicality/prevalence statements for analytic observables and expanding maps. | A generic statement does not identify the maximizing orbit of a specified cosine observable or its exact value. This recent route does not eliminate the explicit computation in T13. [Primary text](https://arxiv.org/pdf/2501.10949). |
| Bourgain, *Sidon sets and Riesz products*, construction and quasi-independent-set estimates | Positive Riesz products and lacunary/Sidon interpolation methods. | Sparsification and positive-product averaging are standard. T14 is an extension with an explicit finite interval, actual real-frequency margins and errors; no new Riesz method or sharp universal Sidon constant is claimed. The two positivity hypotheses and all error terms are retained. [Primary text](https://www.numdam.org/item/10.5802/aif.1003.pdf). |

**What changes for a reader.** For the infinite family of even geometric ratios, one may now use the displayed extreme value, unique maximizing two-cycle and endpoint rate values without numerically optimizing a transfer operator or guessing from finite orbits. The explicit equality set also determines the zero-temperature maximizing measure. For the specified Weyl matrix, T18 provides a rational enclosure with exponentially shrinking relative width and computed asymptotic coefficients; T19 then proves the fixed-normalization transfer that a matching WKB symbol could not justify. P21 makes a precise finite first-loss statement reproducible with all errors enclosed. These are concrete mathematical uses, not evidence that the physical measurement problem is solved.

**Strong alternative explanations.** The audit already proved $a_B\le\delta_B\le3a_B/2$ and the rate $\log2$; those are credited to it, not counted as new here. Schur complements, rank-one resolvents, reversible-path capacity and factorial asymptotics are standard. T18's additional work is the exact endpoint Green sum, its rational enclosure, and the coefficients in (10.15). T19's additional work is the exact interior-window identification and non-cancelling adjacent differences with their explicit prefactor. The general perturbation and orthogonal-polynomial frameworks alone do not supply those calculations. The retrieved *Zeros of Meixner and Krawtchouk polynomials* concerns a related polynomial setting; its statements were not used as a proved identification of this half-shift matrix. No complete classification of associated Krawtchouk identities is claimed. Novelty of a new numerical eigensolver is likewise not claimed for P21.

The sharpest unresolved issue is different: none of these comparisons proves the limiting alignment capacity of the actual spin spectrum. T20 gives a sufficient local-defect test; (9.36) proves that a fixed-ratio application to its entire macroscopic fast band fails that test. A rate measure and a ratio profile alone cannot determine alignment, as the counterexamples show. Consequently the supported novelty claim is a substantive mathematical extension relative to the closest compared results, with explicit reusable outputs. A claim of grade-4 innovation remains unestablished; neither a longer verifier nor the label “published open question” alone establishes the importance and size of the change required by the Mission.

### 12.5 Comparison for the endpoint cost and its stability (Theorems 24–25, Proposition 24.1)

**Lineage note.** This inherited comparison records source use through v1.6. The current-session source reading and strongest-overlap assessment are in §12.6.

**Read status and date.** As of 2026-09-17. Leplaideur–Mengue was read in the arXiv HTML text by the author-side system (Theorem A, the definition of the Mañé potential, the cost $a_{ij}$ and the setting: subshift of finite type, Lipschitz potential); the v1.4 audit reports reading §§3.3–3.5 and Proposition 23; the v1.5 audit (2026-09-16 UTC) reports reading, in the primary texts, Leplaideur–Mengue Theorem A, §§3.3–3.5, Theorem B and §4, Yuan–Hunt Proposition 4.1, Remarks 4.2 and 4.5 and Theorem 4.6, Contreras Theorem A and Proposition 2.6, and Contreras–Lopes–Thieullen Definition 7 and Theorem 8, and its quantifier corrections are adopted in the table below. The author-side session that produced v1.6 could not fetch the two locking texts (network access to those hosts was not granted), so the locking rows below rest on the v1.5 audit's reading and are marked accordingly; the reading debt named in v1.5 ("two locking references not re-read") is closed by that cross-family reading, not by this session. NOT_FOUND is not read as ABSENT.

| Closest result and exact location | Source assumptions, object and conclusion | Mapping to M72 and the additional obligation |
|---|---|---|
| Leplaideur–Mengue, *On the selection of subaction and measure for perturbed potentials* (arXiv:2404.02182), Theorem A, Definition 1 (Mañé potential), the cost $a_{ij}=\sup_{y\in\sigma^{-1}\Sigma_i\setminus\Sigma_i}[A(y)+S_j(y)]$ | Subshift of finite type, Lipschitz $A$, Aubry set a subshift of finite type with entropy $h$; then $\lim\beta^{-1}\log(P(\beta A)-h)$ exists and is the max-plus eigenvalue of the cost matrix | **IMPORTED** in §10.9 and §10.10 (Lemma 25.5). The theorem gives existence and the abstract representation (10.43); it gives no value. Proposition 24.1 evaluates the cost for the cosine family (audit), and Theorem 25 for the first-harmonic family. |
| Leplaideur–Mengue, same paper, Theorem B and §4 | An explicit example: a specific Walters-type family on the binary shift for which the cost series and the selection are computed | Read by the v1.5 audit. The abstract theorem is therefore **not** the only content of that paper: an explicit infinite family with computed costs exists there, so this paper must not say that "only the existence theorem was known". What M72 adds is a different object — a non-local potential on the circle under $T_q$, with the competing inverse branches excluded by exact geometry — which does not satisfy that example's run-length-constant hypothesis; the strength of the overlap is compared in §13.1. |
| Leplaideur, follow-up on more general Aubry sets (arXiv:2501.10932), Theorem A | A lower bound in a more general setting | Not used; the equality needed here is the finite-type case of the paper above. |
| Frühwirth–Juhos–Prochno, Theorem B and (19)–(21); Cioletti–Silva, Theorem 5.4 | Analyticity of the pressure of Hölder potentials on finite-alphabet shifts at all finite parameters | **IMPORTED** in §10.8 for the absence of freezing. |
| Colesanti–Francini–Livshyts–Salani (arXiv:2407.21354), Theorem 1.2 | Brunn–Minkowski-type convexity of the Gaussian Dirichlet eigenvalue under Minkowski combination of domains | **IMPORTED** in Lemma 22.1 for the convexity of $c\mapsto\Lambda(c;K)$; the centre curvature bound (10.26a) is the audit's own argument. |
| Yuan–Hunt, *Optimal orbits of hyperbolic systems* (Nonlinearity 1999), Proposition 4.1, Remarks 4.2 and 4.5, Theorem 4.6 (read by the v1.5 audit) | Proposition 4.1: **for each periodic orbit** there is an open set of potentials for which that orbit is optimal; Remark 4.5 perturbs a given optimal potential into such an open set; Theorem 4.6: non-periodic optimal orbits are unstable under small perturbations | v1.5 paraphrased this as "a periodic maximising measure of a Lipschitz potential persists on an open set of Lipschitz perturbations", i.e. that **every** potential with a periodic optimal measure lies inside an open stability set; that quantifier is not what the cited proposition states (audit finding F15-05) and is corrected here. The result gives no stability interval and no barrier cost for a *given* potential; the direct evidence for Part A of Theorem 25 is the explicit sub-action $u_\varepsilon$, and locking is cited as background only. |
| Contreras, *Ground states are generically a periodic orbit* (Invent. Math. 2016; arXiv:1307.0559), Theorem A, Proposition 2.6; Contreras–Lopes–Thieullen (ETDS 2001), Definition 7, Theorem 8 (read by the v1.5 audit) | Theorem A: for expanding maps, an open and dense set of Lipschitz potentials has a unique maximising measure supported on a periodic orbit; Proposition 2.6 constructs orbit-dependent perturbation neighbourhoods; CLT state the continuity-of-support condition under which the stable set is open | Neither contains the statement that the same excursion has minimal cost for every $(q,\varepsilon)$ in a family, nor a value of that cost; "periodic unique optimum" and "stability of a given potential" are not identified unconditionally. What Theorem 25 adds relative to these is the explicit domain $[-\tfrac1{20},\varepsilon^+(q)]$ with the persistence of the **optimal excursion and of the closed-form exponent** $A_q+\varepsilon B_q$, which locking says nothing about; and §10.11 brackets the positive transition, which locking does not locate. The specific debt "primary texts not re-read" is closed by the v1.5 audit's reading; the possibility of an overlapping *quantitative* result elsewhere in the Sturmian/cosine literature is not thereby excluded, and remains recorded as a bounded comparison. |
| Leplaideur–Watbled, mean-field XY example (arXiv:2003.09535, §5.1) | A pressure problem with global coupling and a continuous alphabet in which a cosine appears | Checked by the v1.5 audit for the word "cosine" only; a different problem (global coupling, continuous alphabet), not a subsumption of Theorem 25. |
| Bousch, *Le poisson n'a pas d'arêtes* (Ann. IHP 2000) and the cosine/Sturmian literature (§12.2) | Maximising measures of $\cos2\pi(x-\theta)$ under the doubling map are Sturmian | For $q=2$, Lemma 25.0 shows the first harmonic is a coboundary of a rescaling, so nothing beyond Bousch is claimed there; for $q\ge4$ the family is outside the doubling-map literature read. |

**What changes for a reader.** Given an even $q$ and an $\varepsilon\in[-\tfrac1{20},\varepsilon^+(q)]$ (or in the certified per-$q$ interval (10.65)), the zero-temperature exponent and the endpoint entropy coefficient of the perturbed cosine family are available in closed form. The two inequalities (10.64) provide a **sufficient certificate** for the proposed optimal excursion once the non-negative residual and the Aubry-set hypotheses have been established; a failed or unresolved test is inconclusive, and (10.64) is not a decision procedure for $(q,\varepsilon)$ outside the proved range (v1.5 said otherwise; audit finding F15-04). The reader also learns where the two-cycle certainly stops being the minimiser — at or before the period-four crossing $\varepsilon_4(q)$ of (10.67), with the transition bracketed by (10.68) — and that the weighted complete-square class of §10.12 has the same excursion structure under the explicit ratio condition (10.71), with an explicit weight outside that condition that switches the excursion.

**Strong alternative explanations.** Everything in Part A is elementary and could be regarded as a worked instance of locking; the paper does not claim otherwise. The exact competitor geometry (10.60) is a computation. The claim of the section is the combination — an explicit domain on which an explicit barrier cost is exact — and its value is to be judged on that, not on any single ingredient.

### 12.6 The v1.6 audit's comparison, extended for the additive results

**Historical reading record (2026-09-17 UTC), with the GSZ locator corrected in v1.8.** The v1.6 audit's written strongest-overlap comparison is incorporated here. In v1.7 the primary text of Leplaideur–Mengue was directly re-opened at Theorem A, Proposition 23, Theorem B and §4, including its explicit max-plus formula. The v1.7 record also reported retrieval of Gao–Shen–Zhang, Contreras and the lacunary LDP source. The current checked GSZ location is v2 Lemma 2.6; the old Corollary 2.7 locator is withdrawn (R5.1). Broad keyword queries returned mostly unrelated results and are not counted as a completed literature sweep. No conclusion of absence is drawn from them. Yuan–Hunt and the older CLT source retain their inherited read status; they are background and are not additional unverified dependencies of T28.

| Closest primary result | Exact overlap | Additional result here / limitation |
|---|---|---|
| [Leplaideur–Mengue, Theorem A and Proposition 23](https://arxiv.org/html/2404.02182v1) | A Lipschitz non-positive symbolic potential with finite-type Aubry set has a pressure exponent represented by a max-plus cost matrix. This is the imported pressure engine. | T28 proves which two infinite inverse paths evaluate the single-component entry, for an explicit raw C2 perturbation neighbourhood of a smooth circle potential. It is not a replacement for their general theorem. |
| [Same source, Theorem B, §4 and Proposition 26](https://arxiv.org/html/2404.02182v1) | An explicit binary-shift run-length family has two fixed-point components and evaluated costs; §4 already has a maximum of affine cost combinations. | The circle potential depends on the coded tail rather than only its first run length. Our arbitrary fixed additive perturbations, single period-two component, quantitative path exclusion and circle series are different inputs and outputs. A corner or finite affine minimum by itself is not novel. No theorem ruling out every recoding/cohomology equivalence is claimed. |
| [Gao–Shen–Zhang, arXiv:2501.10949v2, Lemma 2.6](https://arxiv.org/html/2501.10949v2) | The condition that the Aubry set is a periodic orbit is open in C1 potential and expanding-map topology (v2 Lemma 2.6, statement and proof read in this session). This directly overlaps qualitative ground-state stability and is stronger in topology than merely a C2 existence statement. | T28 adds a computable sufficient radius, constructed sub-action and evaluated excursion costs; it does not improve their genericity or qualitative locking theorem. |
| [Contreras, Theorem A and Proposition 2.6](https://arxiv.org/pdf/1307.0559) | Periodic ground states are generic for expanding maps; suitable orbit-dependent perturbations yield locking. | No claim of a new genericity result. Cor29 gives a specified two-parameter region and a transition coefficient for a named trigonometric family. |
| [Aistleitner et al., §2.2 after Lemma 2.3](https://arxiv.org/pdf/2012.05281) | The source identifies the undetermined even-ratio negative endpoint. T13/T16 answer that stated endpoint question in the paper's setting. | T24–Cor30 evaluate endpoint entropy/cost and explicit perturbations. The existence of the old question does not establish that every subsequent publication left it open. |

**Historical v1.7 corpus comparison.** The internal comparison at that revision used the retrieved Repo3 Manifest, Constants & Lemmas and Manifest Log. The Manifest snapshot runs through M69 and the log through M71; neither is represented as an M72 status authority. The v1.7 integration used the then-uploaded v1.6 manuscript and audit, with the supplied H-0385; the current v1.8 sources are specified in §12.7. No relevant duplicate of the new additive construction was located in those retrieved index texts, a limited index observation rather than an exhaustive absence claim. Repo5 was not searched. No global debt ID or future paper code is created.

**Strongest alternative explanation.** T28 uses standard Hermite interpolation and an existing positive path gap; the passage from a finite set of isolated minimisers to a minimum of affine costs is structurally familiar. Its added mathematical content must therefore be judged on the explicit domain, the verified all-path reduction and the computed circle-family consequences. This comparison supports a concrete extension, while preventing the elementary normal form or the min-plus corner alone from being advertised as a new paradigm.

### 12.7 Current comparison: from geometric endpoints to shifted-family rates

This is the active comparison for the v1.8 central contribution. Earlier sections preserve the history of other results; their version-relative novelty and grade language does not override this section. The comparison distinguishes a known method, a known example, and a new conclusion about that example.

| Primary source and exact location read | Source object and conclusion | Correspondence and additional result here |
|---|---|---|
| [Aistleitner–Gantert–Kabluchko–Prochno–Ramanan, *Large Deviation Principles for Lacunary Sums*, Theorem B, §2.2 after Lemma 2.3, §2.4.1, §3.3.3, Theorem D](https://arxiv.org/html/2012.05281v1); published as *Trans. AMS* 376 (2023), 507–553 | Geometric cosine LDP; undetermined even-ratio negative endpoint; first resonance coefficient; random perturbation sensitivity. Section 2.4.1 specifically proposes $2^k+1$ for further LDP analysis. | T13/T16 answer the endpoint question stated there. T31 computes the full shifted-family rate, including the specifically proposed example. Arithmetic sensitivity and (9.47) are imported. The transcendental-ratio Problem 2.6 and the original global negative comparison remain outside this result. |
| [Frühwirth–Juhos–Prochno, *The large deviation behavior of lacunary sums*, Theorem B and Example 1.3](https://arxiv.org/html/2107.12860v1) | A fixed periodic Lipschitz observable evaluated along $q^kU$ has an analytic pressure and an LDP. | Applies to each frozen phase $\phi$. It does not by direct substitution give $\cos(2\pi(aq^k+r)U)$: the phase $rU$ is tied to the initial point. Lemma 31.2 supplies that missing comparison, and Lemma 31.1 evaluates the maximizing phase exactly. For even $q$, the resulting limit is not analytic. |
| [Aistleitner–Kabluchko–Prochno, *Arithmetic sensitivity of cumulant growth in lacunary sums*, Theorem B, §1.4(i), Theorem C and Problem 3](https://arxiv.org/html/2512.15501v1) | Theorem B computes non-linear cumulants for $2^k+1$. Theorem C assumes an irreducible characteristic polynomial. | The example is already theirs; T31 adds its global LDP and covers the full integer affine-geometric class. Its two-root polynomial $(z-q)(z-1)$ is reducible, so it is not a direct instance of their Theorem C. We do not claim to solve their general recurrence or transcendental-ratio LDP questions. |
| [Aistleitner–Frühwirth–Hauke–Manskova, *Moment generating functions and moderate deviation principles for lacunary sums*, Theorem 1](https://arxiv.org/html/2502.20930v1) | Small-tilt MGF control and moderate deviations, with the cosine normalized by $\sqrt2$. | Under the normalization change $\theta=\sqrt2\lambda$, a cubic correction is compatible with that control. The result does not evaluate the fixed nonzero-tilt shifted rate. A moderate-deviation theorem is not contradicted by Cor33. |
| [Conze–Le Borgne, *Limit law for some modified ergodic sums*, §1.1, Lemma 1.3 and Theorem 1.5](https://arxiv.org/pdf/1001.4862) | Translated modified sums $\varphi(2^kx-x+y)$ and a mixture limit at the $\sqrt n$ scale; the phase-dependent Gaussian variance is explicit. | The tied-phase representation and mixture viewpoint have this earlier precedent. The compared theorem is a central-limit statement; T31 evaluates the exponential scale and its phase maximum for pure cosine, with uniform finite bounds and all integer ratios/shifts. No invention of modified ergodic sums is claimed. |
| Classical Fourier positivity, bounded distortion, Laplace maximization, and differentiable Gärtner–Ellis | Standard proof mechanisms, used explicitly in Lemmas 31.1–31.2 and the LDP step. | No new general mixture principle or new pressure formalism is claimed. The contribution is the exact evaluation for the tied-phase deterministic family, its uniform error, and its consequences. The finite cylinder proof supplies the dependence control rather than treating the two coordinates as independent. |

**Before and after, with the object held fixed.** The original LDP paper explicitly singles out $2^k+1$ in §2.4.1, immediately after Problem 2.6; this paragraph remains on **p.519 of the [published version](https://mediatum.ub.tum.de/doc/1695199/wecu289shj4exnyvifycditp8.S0002-9947-2022-08788-2.pdf)**. It is a proposed example, not the transcendental-ratio problem itself. The directly compared 2025 paper supplies its cumulants. T31 supplies the log-MGF limit at every real tilt and the full rate; Cor33 identifies the loss of analyticity that prevents a naive derivative interchange. For every even $q$, T13/T16 give the geometric negative endpoint, whereas T31 changes it to $-1$ after any nonzero integer shift. A single positive geometric rate curve therefore determines all these shifted laws, including Cor32. An elementary closed form for that geometric curve is not asserted.

**Strongest overlap and alternative explanation.** One might regard the argument as a standard Laplace principle over a latent phase. The modified-ergodic-sum viewpoint is indeed earlier, as the Conze–Le Borgne comparison shows. That structure does not itself evaluate the phase maximum at exponential scale. The finite Fourier majorant evaluates it, and the explicit cylinder probability and error in (9.46) prove the reduction with the dependence on the initial point present. Conversely, the generality of expanding-map pressure cannot be advertised as ours, and the already known shifted example cannot be counted as a new discovery. The assessed change is the complete law and its singularity for a family that is not a single fixed observable under the original expanding map.

**Bounded scope of the search.** The primary texts above were read at their stated versions and relevant theorem/proof locations on 2026-09-18. The generalized Thue–Morse comparison was also checked at [Fan–Schmeling–Shen, Theorem 4.1](https://arxiv.org/pdf/1903.09425): its logarithmic sine-ratio potential differs from the pure cosine and is not substituted for T13. No claim of worldwide priority or an exhaustive post-publication search is made. The general mixtures paper of Biggins, *Large deviations for mixtures* (2004), was located bibliographically but its full text was not retrieved; no theorem number or negative subsumption claim is attributed to it, and the present proof does not invoke it. Failed broad queries are not evidence of absence.

The retrieved Repo3 Manifest, Constants & Lemmas, Debt/Gates, and Manifest Log were searched for the changed mathematical object as well as the older additive-potential target. Their coverage stops before the supplied M72 revision; they are context, not an M72 status authority. The attached v1.7 paper, audit, meta-audit and supplied history through H-0387 govern this integration. Repo5 was not searched. No new global debt identifier or future paper code is introduced.

## 13. Paper qualification and claim cards

### 13.1 Current assessment and limits

**TARGET GRADE: 4. RESEARCH GRADE: 4, internally established for the specified mathematical contribution. PAPER QUALIFICATION: PASS. OUTPUT FORM: RESEARCH PAPER. PROGRAMME ROLE: SUPPORT/METHOD.** This finding uses Mission v1.7 §1.4. It is neither a report of peer review nor a cosmological CORE claim. The v1.7 grade-3 finding and its AUDIT-PASS-MINOR remain correct historical records of that revision; adding confidence or changing the requested target would not change them.

| Required axis | Current finding | Concrete evidence and limit |
|---|---|---|
| Correctness | PASS within the stated hypotheses | T31 is proved by finite inequalities (9.41)–(9.46), including the cylinder probability and phase error. Analytic geometric pressure is an imported input; differentiability at zero is checked explicitly. Cor32–33 and P34 have complete derivations. None uses a finite scan to prove an infinite limit. |
| Novelty | PASS relative to the enumerated primary-source comparison | §12.7 compares the same $2^k+1$ example and the broader affine-geometric class. Known cumulants, geometric pressure and arithmetic sensitivity are credited. The new conclusion is the full rate reduction with a uniform finite bound and the resulting singularity. Absolute priority is unclaimed and remains revisable on new primary evidence. |
| Significance | Grade 4 supported for this mathematical branch | The solved object changes from a local perturbation of a fixed potential to a deterministic frequency class, with all nonzero integer shifts, both signs of tilt, and triangular arrays. The known anomalous-cumulant example gains a full LDP. The effective negative domain expands after an integer shift for even $q$, and (9.50) turns an impossible event into an explicitly possible one. These are exact changes in calculable laws and admissible transfers. |
| Verification | PASS in the disclosed routes; P=0 | Fourier coefficient expansion versus direct phase quadrature; exact rational cylinder identities; unfrozen cylinder integration versus the frozen model; exact Laurent-polynomial cumulants; the finite interval witness; six wrong predictions rejected with all-row noninterference. The inherited central sub-action rows were also rerun. This is one authoring session with computational cross-routes, not independent human or cross-family validation of the new proof. |

The grade-4 additional requirements are met as follows. **Previous limit:** the geometric and fixed-observable LDPs do not directly evaluate a phase tied to the initial point. The published 2023 source explicitly proposes $2^k+1$ for LDP analysis (§2.4.1, p.519); the 2025 source computes its cumulants. The source locations, hypotheses and conclusions are tabulated in §12.7. **Changed capability:** T31 answers that named-example question within a much broader common-shift family; one positive geometric pressure computes every law in T31/Cor32, determines the newly accessible tails and identifies exactly where analyticity fails. **Adversarial review:** the strongest same-example collision, the reducibility distinction, the standard-mixture explanation, the excluded zero shift, both parities, negative multipliers, endpoint interpretation, and the invalid interchange of derivatives were explicitly checked. The six mutations test actual wrong formulas, not negated copies of a PASS predicate.

The short elementary proof does not by itself raise or lower the grade. The evidence is its consequence for the solved class. A future primary source with the same reduction and scope, or a counterexample to the finite cylinder comparison, would require reassessment. **No grade-5 claim is made.** The original all-even global negative-rate comparison with the independent model, general recurrence LDPs, and the physical spin problem are not represented as solved.

The programme contribution has an explicit FQ/RQ contract. It supports **FQ2 / RQ3** by determining which frequency-model calculations may be used in a record-lifetime argument, and **RQ5** by supplying a concrete falsifier for ratio-only transfer. The Z-Spin-specific input is the actual weighted spin contrast and exponentially long observation windows in §§2–4 and 9.9. T31 itself is reusable mathematics independent of that origin. The mathematical model bridge is strengthened, but the bridge from the action to the carrier, instrument, preparation, clock, capture and storage parameters remains CONDITIONAL or OPEN. Actual spin-band $\kappa$ is OPEN. The programme role stays SUPPORT/METHOD.

The inherited Lemma 22.1 sign result and its bounded $K$-range retain their exact status in §10.6. The growing-$K$ spectral problem remains open; no earlier finite $K$ table is converted into a proof. T28 remains a local theorem at the complete-square base potential, and its conservative radius is neither enlarged nor used as the grade-4 argument.

### 13.2 Claim cards for the central theorems

**Current v1.8 claim cards.** T31: one uniform phase, integer $q\ge2$ and $ar\ne0$; full pressure/rate reduction with finite bound; falsifier is a failure of (9.44)–(9.46). Cor32: the same rowwise common offset with subexponential growth; no arbitrary termwise perturbation. Cor33: even $q$, imported coefficient, analytic branches; falsifier is a lower-order odd coefficient or failure of T31. P34: the explicit doubled sequence and $n\ge4$; its interval can be checked without pressure numerics. Their status is PROVEN by the text, finitely anchored by C71–G79, and SUPPORT/METHOD in the programme.

**Inherited claim cards.** The following cards retain the assumptions and limitations of T1–Cor30. Version-relative “new” labels refer to the edition in which a result first appeared; the current research-grade finding is §13.1.

| Claim | Assumptions and quantifier | Proof and cross-route | Actual remaining limit |
|---|---|---|---|
| Theorem 1(a) | every integer $B\ge1$, proper window, $m\in I$ | resistance Cauchy–Schwarz + full gap 2; row C01 rational/Sturm | full window is $0$ separately; sample verification never replaces the universal proof |
| Theorem 1(b) and the gap lemma | fixed compact condition or the endpoint split of §3.3, sufficiently large $B$ | exact resistance ratio, tails, two-boundary differences; row V02 | universal finite band monotonicity not claimed |
| Theorem 2 | positive weights; the spectral/weight limit; $0<\ell<1/2$ | all-time lower envelope and time-average upper; rows C05, V06 | finite numbers are not finite certificates of the asymptotic interval |
| Theorem 3 | fixed $j,w$, transversal loss, $B\to\infty$ | explicit perturbation remainder, uniform root control; rows C03, V04 and the interval counterexample | not an optimisation over all losses and all finite $B$ |
| Theorem 4 | degenerate neutral code, two declared routes, supplied clock/capture | exact gauge conjugation and matrix polynomial, direct 64-dimensional exponential; rows C07, V08, V11 | no S14 derivation of dynamical carrier separation or apparatus |
| Theorem 5 | original reference, charged probe, all C6 outcomes, neutral preparation | direct partial trace and complete map; rows V09, W13 | the known probe phase is a resource; an unknown sign averages to zero contrast |
| Theorem 6 and the error window | history-independent parity noise/erasure and stated norm errors | exact generator, direct Lindblad, Duhamel; rows C10, V12 | obtaining $\chi,\zeta,\varepsilon$ from real matter is separate |
| Theorem 7 | measures with continuous strictly increasing $H$ at the two quantiles | two explicit families, the lower one assembled by the v1.1 diagonalisation; rows W15, W16 | the v1.0 proof built a separate family for each $q'$ (finding F02); the repaired proof exhibits one |
| Theorem 8 | Hadamard ratio $\ge2m+1$ on the fast set with margin | Riesz product with the Fejér extremal kernel; **proof rewritten in v1.1** around the $\ell^1$ Fourier mass (9.4a), same constant $c_m$; rows C18, C31, C32, V19, V20 | not applicable when adjacent ratios fall below $3$; Theorem 14 covers that case with a weaker constant |
| Theorem 9 | exact geometric frequencies, slowly varying weights; strict crossing for its exponent application | explicit orbits; exact sub-actions for $q=2,4$; general sub-action existence for the upper bound; rows W17, C24 | the even-$q\ge6$ equality, VERIFIED on a grid only in v1.0, is now PROVEN for every even $q$ by Theorem 13; the hypothesis of *exact* integer ratios is essential (counterexample (9.11)) |
| Theorem 10 | $h\ge3\sqrt B$ per boundary; $h_{\min}\ge\sqrt{2B\log B}$ for the eigenvalue | exact resistance expansion with the $s(s-1)$ sum and the $B^{-5/4}$ spectral step, both repaired in v1.1; rows V21, C32 | constants $C_0,B_0$ not optimised; the v1.0 consequences are restricted to $h=o(B^{3/4})$ for the Gaussian form, and the adjacent-difference and fixed-$K$ statements are withdrawn (findings F06, F07) |
| Theorem 13 | every even integer $q\ge2$, all $x$; strict crossing for its exponent application | tent sub-action (9.15) with two endpoint inequalities; rows C26, V27, V28 | a statement about exactly geometric integer-ratio spectra only |
| Theorem 14 | $\nu_{i+1}/\nu_i\ge\rho>1$, positive weights, $R=\rho^L>3$ and $\delta=1-\rho^{-1}-(R-1)^{-1}>0$ | sparsified Riesz product with three explicit non-resonance margins; row V33 | the constant $1+1/(2L)$ is far from the observed gain; no upper bound on $\sup M$ |
| Theorem 15 | standard band, interior rate, $B$ beyond a finite size | Theorem 14 with $\rho=19/10$, $L=2$, on the actual spacing (9.28); row V34 | gives $\kappa^-\ge1/4$, not the exact $\kappa$; the edge ratio approaches $2$ from below, so the hypothesis holds only for large $B$ |
| Theorem 16 | integer $q\ge2$, Lebesgue initial phase | Theorem 13 plus the standard pressure representation; row V35 | determines the effective domain and the two endpoint values, not $\mathcal I_q$ as a function |
| Proposition 12 | finite symmetric tridiagonal parent | identical to Theorem 1(a) | unconditional as an inequality; the transfer of the *exponent* to another parent needs the four normalisation conditions of Section 10.3 |
| Proposition 9.1 | as Theorem 2(c), **plus $H_-$ and the atom term**; the constant-$\kappa$ corollary needs the strict crossing (9.1e) | two-sided threshold argument (9.1a); the counterexample (9.1c) shows the atom term cannot be dropped | gives an interval unless both strict thresholds coincide; existence and constancy of $\kappa$ alone are insufficient |
| Proposition 17 | every $B\ge1$, Weyl-edge parent | exact trial-vector identity and the Rayleigh principle; rows C40, V41 | a lower bound on $\delta_B$ with an explicit constant; the exact asymptotics are now supplied by T18 |
| Theorem 11 | $0<b=a\le1/4$ | relaxed Theorem 2(c) with a vanishing-weight family; row V22 | finite sizes far from the asymptotic regime |
| Theorem 18 | exact Weyl matrix, all $B\ge1$ | endpoint Green formula, rational LDL crosscheck C43, beta-integral remainder C48 | does not make the matrix an action-derived physical system |
| Theorem 19 | fixed normalization, compact windows, declared band preparation | exact auxiliary transform and capacity proof, C44 | does not equate Weyl and spin phase optima; diffusive bands excluded |
| Theorem 20 | even integer comparison ratio, actual real frequencies, positive weights | weighted telescoping and backward recurrence; W47 | (9.36) excludes a fixed-ratio application to the whole macroscopic spin band |
| Proposition 21 | standard band, the three listed finite sizes, loss $\ell=1/10$ **as the absolute contrast loss $\Gamma-S$ of §4.1, not a relative loss** | exact directed matrix/readout/time intervals, C45, with the weight-positivity and bracket invariants now asserted | no all-B complexity or asymptotic exponent claim; `--quick` certifies only $B=24$ and says so |
| Lemma 19.1 | endpoint window $[l,B]$, $\epsilon B\le l\le(1-\epsilon)B$; $A_*<1$ | two one-sided Rayleigh quotients across a sign-definite rank-one endpoint perturbation and a path Cauchy–Schwarz run on the perturbed ground function, with the anchor $b_*=\max\{l,\lceil B/2\rceil\}$ and the energy inequality $\mathcal E(\chi)\le\lambda_D^0+V$ (v1.4 audit); rows V49, V52 | supplies the $a+b=1/2$ case only; the **proved** relative error is $O(B^{-1})+O(e^{-c_\epsilon B})$, the order (10.20) already carries; the exponentially small measured size is not claimed as proved; no diffusive endpoint claim |
| Theorem 22 | even $B\to\infty$, fixed $0<\kappa<K<\infty$ and $J>0$, $j=\lceil K\sqrt B\rceil$, $w=\lfloor\kappa\sqrt B\rfloor$; $\kappa$ is the bandwidth, not the alignment capacity | Dirichlet-form convergence to the Ornstein–Uhlenbeck operator with min–max transfer of the second level; an algebraic continuation of the sector matrix in the window centre plus Vitali for the difference quotients; exact evenness at the centre; Lemma 22.1 (convexity, $\Lambda'>0$, $\Lambda''(0)>0$, v1.4 audit) for the centre constants and the Cesàro bound; Riemann sum and first-contact trapping for the loss; row V50 | (10.27) is uniform as an absolute statement and relative only on $\lvert c_k\rvert\ge\delta$; the finite adjacent ratios exceed their fixed-$k$ limits $3,5/3,\dots$; (10.29) holds under strict first contact of $\mathfrak M$ with $\ell$ and no global inverse is assumed; the $K$-dependence of $\tau_\ell$ is known only at leading order $2K^2(1+o(1))$ [HYPOTHESIS]; no statement for $h$ between the diffusive and macroscopic scales, and no dynamical transition at $B^{3/4}$ is claimed |
| Corollary 23 | integer $q\ge2$ | two extremal invariant measures and affinity of the entropy — equivalently, convexity of $\mathcal I_q$ plus the endpoint determination of Theorem 16; row V51 (numerical) | an upper envelope, exact at three points and loose between them; the endpoint behaviour is now determined by Theorem 24 and Proposition 24.1, which supersede any question this corollary left open |
| Theorem 24 | even $q\ge2$; $u\downarrow0$ at fixed $q$ | explicit prediction-error residual $\delta_q$ for the upper bound, a two-digit Markov chain with the single-repeat series $A_q$ and the remainder $C_q\varepsilon^2$ for the lower bound; analyticity of the pressure (imported) for the absence of freezing; rows C53, V54 | order $\Theta(u\log(1/u))$ with constants $1/A_q$ and $1/\delta_q$ only; no additive $O(u)$ remainder; nothing about the interior of $\mathcal I_q$ or about the actual spin band; authored by the v1.4 audit |
| Proposition 24.1 | even $q\ge2$; $t\to\infty$ and $u\downarrow0$ at fixed $q$; even $q\to\infty$ separately in (10.42) | Leplaideur–Mengue Theorem A (imported: existence and Mañé-cost representation of the exponent); exclusion of every competing excursion — the audit's Lipschitz margin (10.47) for $q\ge6$ and the exact competitor geometry of Lemma 25.4 for $q=2,4$; entropy duality; rows C53, C56 | equals $A_q$, the single-repeat series; relative $o(1)$ in (10.41), no pressure prefactor; the two limits in (10.40)–(10.42) are not interchanged; the v1.4 audit's finite certificate for $q=2,4$ (present in its ZIP, not available in the v1.5 authoring session) is not relied upon |
| Theorem 25 | even $q\ge4$ and $\varepsilon\in[-\tfrac1{20},\varepsilon^+(q)]$, $\varepsilon^+(q)=1/(4\cos a)$ (uniform in $q$ on the left, the non-negative-slope proof endpoint on the right); $\varepsilon\in(-\eta_2(q),\varepsilon^+(q)]$ for Part A; $[\varepsilon_{\rm lo}(q),\varepsilon^+(q)]$ with the printed rational $\varepsilon_{\rm lo}(q)$ for $4\le q\le40$; $q=2$ for all $\varepsilon>-1$ by cohomology | tent sub-action $c_\varepsilon d$ with the exact identity (10.57) on the positive side and convexity plus the sign of $m$ on the negative side; exact competitor geometry (10.60); reduction to the two inequalities (10.64), concave in $\varepsilon$; at $\varepsilon=-\tfrac1{20}$ a $q$-dependent tail bound for $q\ge8$ (10.64a) and exact rational arithmetic for $q=4,6$; at $\varepsilon^+(q)$ the complete square (10.64b)–(10.64c) for every $q$; the large-$q$ chain of v1.5 is withdrawn (W58); rows C55, C56, C59, V57 | sufficient, not necessary: (10.64) is a certificate under the stated hypotheses and a failed test is inconclusive; the positive transition is bracketed, $\varepsilon^+\le\varepsilon_{\rm crit}\le\varepsilon_4$ (Theorem 26), width $1.99\%$ of $\varepsilon_4$ at $q=8$, and its exact value is OPEN; on the negative side the proof is lossy by a factor about $3$ and the transition is OPEN; T25 itself treats only the second harmonic; T28 and Cor29 now cover further additive perturbations; nothing about the actual spin band; one internal referee pass and one cross-family audit (Appendix R3), whose repair this row incorporates |
| Theorem 26 | even $q\ge4$; $q\to\infty$ for (10.69)–(10.70) | explicit minimal-period-4 orbit and its crossing (10.67); Proposition 25.2 for the lower end; exact Taylor coefficients with a removable common zero; rows C60, C61; supplied by the v1.5 audit, re-derived here | a bracket, not a value: $\varepsilon_{\rm crit}(q)=\varepsilon_4(q)$ at finite $q$ is not claimed; the finite-period search of V57 is a diagnostic only; nothing about the negative side |
| Proposition 27 and Example 27.1 | even $q\ge4$; positive Lipschitz $h$ with $M/m<R(q)$, $R(q)\ge375/64$ | Leplaideur–Mengue Theorem A (imported) with the complete-square geometry of (10.64c); series cost (10.72); explicit bump weight at $q=4$ with an explicit alternative excursion; rows C62, W63; supplied by the v1.5 audit, re-derived here | P27 itself is a multiplicative class with fixed zero set and square factor; the additive family is treated separately by T28 and Cor29; sufficient condition only; $R_{\rm crit}$ bracketed in $[375/64,44.699]$, not determined; priority of the class not assessed |
| Theorem 28 | every even $q\ge4$, arbitrary real $C^2$ perturbation with $\mathcal N_q(\psi)\le1/2$ | explicit periodic Hermite construction, quadratic domination, inherited branch geometry, all-path gap, endpoint-compensated costs; C65, C66, V70 | local sufficient radius, not sharp or C0-robust; single Aubry component; pressure representation imported |
| Corollary 29 | explicit triangle $\mathcal T_q$ and local diamond; $\lvert\eta\rvert\le1/24$ for the uniform transition limit | raw polynomial factorisation, convex residual and path gaps, period-four crossing; C67, C68 | exact finite-q positive and negative transitions remain open; the third harmonic does not model the physical spin arithmetic |
| Corollary 30 | sine perturbation of $F_0$ with $\lvert\eta\rvert\le1/(2K_{q,1})$ | compensated series, strict term signs, T28 and independent residual costs; C69, V70 | corner of the zero-temperature exponent, not finite-temperature pressure; no changed ground measure is claimed |

### 13.3 Criteria that reverse the verdict

If the relative remainder of Theorem 1 is found non-uniform at a fixed non-zero shift, or if a sequence exists along which the gap differences fall below the claimed scale, Theorem 2's application is reopened. If the preparation map is found to discard outcomes or to yield the same contrast for an unknown sign, the interface is reopened. The reading that the same chain keeps a permanent record without capture is rejected at once. Replacing joint flips by independent flips while claiming the same storage rate violates the assumptions of Theorem 6. If the same first-loss theorem is found under the same source assumptions, the novelty classification is re-judged. If a scan at larger $B$ shows $\theta\to0$ or $\theta\to1$ for the standard band **along a controlled subsequence with a residual bound**, the corresponding part of Conjecture 9.2 is refuted; a handful of finite sizes drifting in one direction is not a refutation. If an admissible family with a given $\mu$ is found whose exponent lies outside $[q_{\ell/2},q_\ell]$, Theorem 2(c) is refuted (it would contradict its proof). If a spectrum satisfying the hypotheses of Theorem 14 is exhibited whose supremum over $[0,T]$ falls below (9.22), that theorem is refuted; if the standard band is shown to have a fast-set adjacent ratio staying below some $\rho>1$ for arbitrarily large $B$, Theorem 15 loses its hypothesis and $q_{4\ell/5}$ reverts to $q_\ell$. If a $T_q$-invariant measure with $\int(-\cos2\pi x)\,d\mu>\cos\frac\pi{q+1}$ is exhibited for an even $q$, Theorem 13 and with it Theorem 16 are refuted; row V28 is the finite search that has not found one. If the *ground* eigenvalue of the Weyl-edge matrix is shown to equal $-(1-1/B)$ exactly for some $B$, Proposition 17 is refuted at that $B$; a coincidence at one $B$, or an agreement with some other eigenvalue, would not restore the v1.0 claim, which was about the ground energy at every $B$. If some $B$ is exhibited with $\delta_B<1/(BZ_B)$, the trial-vector computation of Proposition 17 is wrong. If a non-negative degree-$m$ kernel with first coefficient exceeding $2\cos(\pi/(m+2))$ existed, Fejér's theorem would be false; the constants of Theorem 8 would still stand as lower bounds. Stating these reversal conditions is compatible with the completeness of the present proofs; the impossibility of testing an infinite range is not a reason to leave the work unfinished.

For T28, a perturbation within (10.75) whose constructed residual violates (10.76), a non-candidate path beating the claimed gap, or failure of the endpoint compensation reopens the central new result. For Cor29, failure of the raw factorisation, the convex path-gap argument or the symbolic quotient coefficient does the same. For Cor30, a cheaper third excursion within the stated radius or unequal ground means contradicts the conclusion. A primary result that already evaluates the same circle class under the same hypotheses changes the novelty assessment even if every calculation still passes.

For the v1.8 central result, an admissible failure of the finite majorant (9.41), the tied-phase estimate (9.44), or the retained cylinder mass in (9.46) would reopen T31. An unrecognized nonzero derivative of the geometric pressure at zero would reopen the LDP step. A source with the same shifted rate and assumptions would reopen novelty even if all checks pass. These are separate from the inherited local-additive reversal conditions above.

## 14. Discussion and remaining problems

The central v1.8 advance is the complete shifted-family rate reduction in T31, its array extension in Cor32, the precise nonanalyticity in Cor33 and the tail distinction in P34. The following earlier closures remain valid. Theorem 22 settles the diffusive window that had been open since v1.0, with the limit object (an Ornstein–Uhlenbeck Dirichlet problem), the law ($\Theta(B^{3/2})$) and the reason the earlier attempts failed (the centre degeneracy) all identified, and Lemma 22.1 supplies the curvature its centre statements need. Corollary 23 turns the endpoint determination of Theorem 16 into a bound on the whole domain. Theorem 24 and Proposition 24.1 (v1.4 audit; completed in v1.5 for every even $q$) settle the endpoint behaviour of the rate function — no freezing, order $u\log(1/u)$, sharp coefficient $1/A_q$ — and Theorem 25 (proof repaired by the v1.5 audit) shows that the closed-form cost is stable, with an explicit interval reaching the endpoint of its non-negative-slope proof, under the first harmonic; Theorem 26 brackets the positive transition with its leading asymptotics, and Proposition 27 extends the excursion result to a weighted complete-square class with an explicit switching counterexample (both v1.5 audit). Three obligations were closed in v1.3: the leading Weyl energy correction (T18), the compact-band spectral transfer to the actual Weyl parent (T19), and rigorous finite-matrix first-loss certification in the listed instances (P21). T20 provides a sufficient finite-horizon test for transferring exact integer-ratio alignment to a controlled class of real-frequency perturbations. These results preserve the distinction between the waiting, writing and storage times.

T28 reduces an explicit $C^2$ additive neighbourhood of the complete-square potential $F_0(x)=\cos(2\pi x)+\varepsilon^+(q)\cos(4\pi x)$ to two evaluated path costs; Cor29 proves a raw third-harmonic region and transition asymptotic, and Cor30 distinguishes ground-state persistence from optimal-path selection. These settle the stated local additive target. The following obligations and boundaries remain.

1. **Actual spin-band alignment:** Conjecture 9.2(a), (c) and (d): existence, strict upper interiority, and a continuous strict-crossing limit. The Weyl band has the same bounds, not an identified common optimum. The v1.4 audit's reduction is worth recording: the exponent $z_*$ of $JT_\ell$ for one fixed $\ell$ is determined as soon as $\sup_{t\le e^{B(z_*-\delta)}/J}M_B(t)<\ell$ and $\sup_{t\le e^{B(z_*+\delta)}/J}M_B(t)>\ell$ are proved for the actual frequencies and every fixed $\delta>0$ — a smaller target than the whole function $\kappa^\pm(z)$, but one that must be met with the actual eigenvalues, because a relative $O(B^{-1})$ spectral approximation cannot be substituted into a phase optimisation over exponentially long times (the error $T\sum_i\omega_i|\Delta_i-\widehat\Delta_i|$ is not small), and the counterexamples (9.11) and (9.36) forbid importing $\kappa$ from an approximating spectrum.
2. **Diffusive spectral differences: closed in v1.4, with a negative component.** Theorem 22 supplies the fixed-$K$ first-loss law $JT_\ell=\Theta(B^{3/2})$ with the first-contact constant $\tau_\ell$, and identifies the adjacent differences as $2J\Lambda'(c)/B^{3/2}$ — uniformly on the whole band as an absolute statement, and with relative error $o(1)$ on $|c|\ge\delta$. A uniform *relative* remainder across the whole band does **not** exist: $\Lambda'(0)=0$ by symmetry, the differences degenerate at the band centre to $\Theta(B^{-2})$, and the adjacent ratios there are $3$ and $5/3$ rather than $1$. Open: the crossover window $B^{1/2}\ll h\ll B$, where neither Theorem 22 nor Theorem 10 controls the adjacent differences and the first loss (Theorem 10 does control the eigenvalues for $h\ge\sqrt{2B\log B}$); a theorem allowing $K=K_B\to\infty$ with an explicit admissible growth rate, a relative remainder and a strict first-contact condition; and the $K$-dependence of $\tau_\ell$ beyond the leading $2K^2(1+o(1))$ [HYPOTHESIS], for which a Kramers asymptotic of $\Lambda'(c;K)$ uniform in $c\in[0,2\kappa]$ would be needed.
3. **General parent classification:** T19 covers the specified Weyl matrix. It is not a theorem for every parent with the same symbol or stationary rate.
4. **Physical derivation:** the actual S14 state, subsystem, instrument, readout, transport, capture and bath, with a common operating-time error bound. D-M69-MOVING/INSTRUMENT, K17/K18, D-S14-EVENT-001 and D-HCLK-001 remain OPEN.
5. **The interior of the rate function: the endpoint is closed, the interior is not.** Theorem 24 and Proposition 24.1 give $\log q-\mathcal I_q(-\beta_q+u)=(u/A_q)\log(1/u)(1+o(1))$ and no freezing. Open: the additive $O(u)$ remainder and the pressure prefactor; $\mathcal I_q$ on any interval away from its endpoints, for which Corollary 23 gives only an envelope with measured slack up to $0.61$ at $q=4$. The v1.4 numerical freezing probe is withdrawn (§10.8); nothing numerical is now offered on this point.
6. **Stability and transitions.** T25–T27 remain valid in their stated ranges. T28/Cor29 additionally prove stability for sufficiently small $C^2$ additive perturbations at the complete-square base $F_0=f_{\varepsilon^+}$, the two-dimensional region $\mathcal T_q$, and a nonempty interval strictly above $\varepsilon^+(q)$. The old statement that the entire interval $(\varepsilon^+,\varepsilon_4)$ is unidentified is therefore narrowed: a short initial subinterval is now identified by (10.89), and the rest is open. Exact finite-$q$ equality with the period-four crossing, the negative transition, optimal radii, necessity of (C1)–(C2), other Aubry components and the global additive-family phase diagram are unresolved. Cor30's exact path switch does not determine Example 27.1's large-contrast switching threshold. None of these model-family certificates determines actual spin-band alignment.
7. **Current grade and open mathematical targets.** The grade-4 judgment in §13.1 concerns T31–P34 and the solved shifted-frequency class. It is not an upgrade of the old local-radius evidence. The exact finite-$q$ transition $\varepsilon_{\rm crit}=\varepsilon_4$, the original global negative-rate comparison with the independent model, and more general recurrence or termwise-perturbed LDPs remain open here. Actual spin-band alignment remains a separate physical target. None is claimed as solved by restricting to a smaller family.

Neither finite PASS counts nor absence of a counterexample is used to prove an infinite-size limit. Further work should address these named obligations, rather than repeat a positive self-assessment of the same claims.

---

## Appendix S. Integrated state-space, selection, preparation, cooling, current, Gauss-law, finite-time and optical results

This appendix carries the computations and counterexamples on state spaces, selection, preparation, cooling, currents and outputs so that they can be used from the main text. The letter S marks inherited seed material; the original equation labels (B14-1, FT1, G1, C1, …) are kept. Section numbers inside this appendix are those of the earlier seed (its §8.17 is S8.17 here). The earlier operational, qualification and verification records are replaced by the main text and Appendices L, V, H; the original wording is preserved in the lineage. S6.14–S6.15 are replaced by repaired statements. Where an inherited section speaks of "storage" of a not-yet-used reference contrast, read the waiting/writing-availability time $T_\ell$ of the main text; the storage time after transfer to pointers is $t_s$ of Section 8. The inherited "[proven]" marks refer to the originally declared models and never to a derivation from the whole of S14.

## S5. The optimal state space: theorems kept and a uniqueness retracted

### S5.1 Definitions, energy shells and the top eigenspace

From here until restored otherwise, $\hbar=1$ and the energy unit of the M71 reference is $\Delta=1$. The physical split is **fixed** as $\mathcal H_R=\ell^2(\mathbb Z)$, $\mathcal H_C=\operatorname{span}\{|k\rangle:0\le k\le N\}$. The rotor charge is $M|m\rangle=m|m\rangle$ and the total reference energy is $E=M^2+K_C$. Only $N\ge1$ is treated; at $N=0$ the record ceiling is $0$.

$$
T_N=\sum_{\substack{m\in\mathbb Z,\ 0\le k\le N\\0\le k-2m-1\le N}}|m+1,k-2m-1\rangle\langle m,k|,\qquad A_N=\frac{T_N+T_N^\dagger}2,\qquad \Gamma(\rho)=\sum_{\rm edges}|\rho_{uv}| .
\tag{S1}
$$

By M71 T-JCE, $\Gamma(\rho)$ is the total variation of $|\pm x\rangle$ optimised over admissible charge- and energy-conserving effects for that fixed reference, with the same binary discrimination task and equal priors; it is not automatically extended to other cost functions.

Each edge conserves $e=m^2+k$. A shell with $0\le e\le N$ is the central path $-\lfloor\sqrt e\rfloor\le m\le\lfloor\sqrt e\rfloor$; for $e>N$ it can split into two one-sided paths. The top eigenvalue of a $P$-vertex path is $\cos[\pi/(P+1)]$. Hence with $L=\lfloor\sqrt N\rfloor$

$$
C_L=\|A_N\|=\cos\frac\pi{2L+2},\qquad \mathcal V_N=\operatorname{span}\{|\phi_e\rangle:L^2\le e\le N\},\qquad \dim_{\mathbb C}\mathcal V_N=d=N-L^2+1,
\tag{S2}
$$

$$
|\phi_e\rangle=\sum_{m=-L}^{L}s_m|m,e-m^2\rangle,\qquad s_m=\frac1{\sqrt{L+1}}\cos\frac{\pi m}{2L+2}.
\tag{S3}
$$

Different $e$ are orthogonal and each path's top eigenvector is simple at the fixed positive edge phase. The bound that a one-sided path cannot reach the same maximal length is in M71 §7.3. So the dimension in (S2) is a **recount of M71's description of the top space**, and the graph spectrum and sine optimiser are classified IMPORTED/SPECIALIZED (M71 §§7.2–7.3; Navascués–Popescu §5.3 and Appendix E).

### S5.2 What $d$ counts and what it does not

The density operators maximising the fixed witness $A_N$ are all states supported in $\mathcal V_N$. That set has real affine dimension $d^2-1$ and its pure rays have real dimension $2d-2$; $d$ itself is not called the real dimension of a state manifold.

$$
1\le d\le2L+1;\qquad d=1\iff N=L^2 .
\tag{S4}
$$

For $N=1,2,3$: $d=1,2,3$; for $N=4,\ldots,8$: $d=1,\ldots,5$. The earlier "oscillation up to $2L$" was one short. What becomes unique at a perfect square is the **top ray of the fixed positive witness**.

### S5.3 The full record-optimal set and the perfect-square counterexample

The union of paths is a forest without cycles. The phases of every edge of a density matrix can be aligned simultaneously by a vertex-diagonal unitary $U$, so

$$
\Gamma(\rho)=\max_{U\ \rm diagonal}\operatorname{tr}(\rho\,UA_NU^\dagger),\qquad
\boxed{\operatorname*{argmax}_\rho\Gamma=\bigcup_U\{U\tau U^\dagger:\tau\ge0,\ \operatorname{tr}\tau=1,\ \operatorname{supp}\tau\subseteq\mathcal V_N\}.}
\tag{S5}
$$

**Proof.** A diagonal unitary fixes each edge's phase difference independently; with no cycles there is no additional constraint on phase sums. Once aligned, the sum of moduli is the expectation of the rotated $A_N$. For the expectation of $C_LI-UA_NU^\dagger\ge0$ in a positive state to vanish, the state must be supported in its kernel; the converse is direct substitution. In the original infinite space the edges are finitely many once $N$ is fixed, and since $C_L>0$ an isolated-vertex support cannot enter the optimal set. $\square$

These $U$ commute with $M,E$ but need not be of the form $U_R\otimes U_C$ for the physical $R:C$ split; they are not interpreted as physically free local transformations. They were used to describe the set that can be jointly optimised with the reading effect; which transformations count as the same instrument equivalence class is a separate definition.

In the $N=1$ shell $(|-1,0\rangle,|0,1\rangle,|1,0\rangle)$,

$$
|\phi\rangle=(\tfrac12,\tfrac1{\sqrt2},\tfrac12),\qquad |\widetilde\phi\rangle=(-\tfrac12,\tfrac1{\sqrt2},-\tfrac12)
\tag{S6}
$$

are orthogonal but both have $\Gamma=1/\sqrt2$, with $\langle A_N\rangle=\pm1/\sqrt2$. So the sentence "the record-optimal state is unique only at perfect squares" is **retracted for the general state-and-effect optimisation**; the uniqueness of (S4) may be used only under a fixed-phase witness or after quotient by a declared phase equivalence.

**Exact gauge recovery.** For $N\ge1$ the $\Gamma$-optimal pure states are, up to diagonal phases, of the form $\sum_{e=L^2}^Nc_e\phi_e$. A common phase on a whole shell is an allowed diagonal gauge, so the phases of $c_e$ are not orbit invariants. Orbits are classified by

$$
(p_{L^2},\ldots,p_N),\qquad p_e=|c_e|^2,\qquad \sum_ep_e=1,\qquad\text{i.e. }\Delta_{d-1},
\tag{S6a}
$$

since diagonal transformations cannot change vertex probabilities and all phases at equal $p$ can be removed. So "a single orbit iff $d=1$ iff $N$ is a perfect square" stands, but distinct rays of the complex top space are not read as distinct orbits. At $N=0$, $\Gamma$ vanishes for every state and the uniqueness statement has its exception. Gauge equivalence and physically free local operations remain distinct.

### S5.4 Energy minimisation and the variational inequality

$$
\langle A_N\rangle_\rho\le\Gamma(\rho)\le C_L .
\tag{S7}
$$

Both equalities hold simultaneously exactly for density operators supported in $\mathcal V_N$; for pure states $\sum_ec_e\phi_e$ with arbitrary complex $c_e$, $\sum|c_e|^2=1$ — positivity of all coefficients is not needed; mixed states are included.

Since the $U$ of (S5) commute with $E$,

$$
\boxed{\min_{\Gamma(\rho)=C_L}\operatorname{tr}(\rho E)=L^2.}
\tag{S8}
$$

The shell energies of the optimal set are $L^2,\ldots,N$, and the mean energy is minimised only with support on the lowest shell. For the fixed witness $|\phi_{L^2}\rangle$ is unique; for the full $\Gamma$ optimisation its edge-phase family remains. That minimal-energy state is an $E$ eigenstate and carries no time-phase information. Energy selection and clock use are different preparation choices, not two theorems that automatically deliver the same initial state.

## S6. The selection Hamiltonian: exact variational results and finite-resource extensions

### S6.1 Conserved quantities checked first

Write the candidate with explicit energy units:

$$
H_{\rm sel}=\nu E-JA_N,\qquad \nu,J>0,\qquad \kappa=J/\nu .
\tag{G1}
$$

Here $E$ is the dimensionless $M^2+K_C$ and $\nu,J$ carry energy units; if the notation $\nu H_{RC}$ is used, the ratio must be redefined according to whether $H_{RC}$ already contains $\Delta$.

$$
[E,T_N]=0,\quad[M,T_N]=T_N,\qquad[E,H_{\rm sel}]=0,\qquad
\boxed{[M,H_{\rm sel}]=-\tfrac J2(T_N-T_N^\dagger)\ne0.}
\tag{G2}
$$

So (G1) is **not** a reference-only charge-conserving dynamics of the original M71 kind. A system–reference exchange that conserves total charge must include the opposite charge change of the system; a phase/charge reference can hide in $-JA_N$ once that freedom is dropped. Also $[H_{\rm sel},E]=0$, so unitary evolution under this Hamiltonian never changes the initial shell probabilities. Computing the ground state and proving that the state is cooled/prepared into it are different tasks.

### S6.2 Complete derivation of the ground state and the thresholds

Let $C_j=\cos[\pi/(2j+2)]$, $C_0=0$. For central shells $e$ with the same $j=\lfloor\sqrt e\rfloor$ the top path eigenvalue is $C_j$, so the lowest $H_{\rm sel}$ energy in that family is at $e=j^2$.

For a one-sided broken shell $e>N$ with $w$ vertices, positive vertex range $a,\ldots,b$, $a\ge1$, one has $b^2-a^2\le N$ and $b=a+w-1$. Taking $j=\lceil(w-1)/2\rceil$ gives $2j+1\ge w$, $j\le L$, $j^2<e$, so the central $j^2$ shell has at least as large a top eigenvalue as this broken path and lower bare energy; the central state strictly dominates the broken-shell candidate for all $J,\nu>0$. The negative side is identical, and an isolated vertex cannot beat the minimal energy $e=0$.

Hence the ground-state problem of the whole infinite rotor reduces exactly to

$$
\boxed{j_*(N,\kappa)\in\operatorname*{argmin}_{0\le j\le L}f_j(\kappa),\qquad f_j=j^2-\kappa C_j.}
\tag{G3}
$$

This is an analytic conclusion excluding every broken shell, not an estimate observed by increasing a finite cutoff. The crossing points of adjacent candidates are

$$
\boxed{\kappa_j=\frac{2j+1}{C_{j+1}-C_j},\qquad j=0,\ldots,L-1.}
\tag{G4}
$$

For real $x\ge0$, $C(x)=\cos[\pi/(2x+2)]$ is increasing and strictly concave, so $C_{j+1}-C_j$ decreases and (G4) strictly increases; every $j$ becomes optimal in turn, and away from thresholds the top path ray is unique; at a threshold the ground states of two adjacent central shells are degenerate.

The first values are $\sqrt2,\ 18.87758622,\ 86.42425545,\ 257.57089365,\ 605.27354690,\ldots$ For $\kappa<\sqrt2$ the ground state is $|m=0,k=0\rangle$ with $\Gamma=0$. Away from thresholds the ground state is an $E$ eigenstate with $\operatorname{Var}(E)=0$ and zero clock QFI of the state itself; at a threshold a coherent ground superposition of two shells, if separately prepared, can carry time information, and that exception is not erased.

### S6.3 Deficit asymptotics and cutoff saturation

Let $j_\infty(\kappa)$ be one discrete minimiser without bandwidth restriction. From the continuum approximation at large $\kappa$,

$$
f_j\simeq j^2-\kappa+\frac{\kappa\pi^2}{8(j+1)^2},\qquad j_\infty(j_\infty+1)^3\sim\frac{\pi^2\kappa}8,\qquad 1-C_{j_\infty}\sim\frac\pi{2\sqrt2}\kappa^{-1/2}.
\tag{G5}
$$

Integer rounding does not change the large-$j$ leading term. Convergence is slow: for $\kappa=10^2,10^3,10^4,10^5,10^6$ one finds $j_\infty=3,5,10,18,33$ and $(1-C_{j_\infty})/[(\pi/2\sqrt2)\kappa^{-1/2}]=0.69,0.97,0.92,0.97,0.96$. At finite $\kappa$ only the exact integer minimisation (G3) is used. At **fixed finite $N$**, however, $\kappa\to\infty$ saturates at $j_*=L$, $\Gamma=C_L<1$; (G5) applies only in the joint limit where the cutoff does not truncate the optimal $j$. Bandwidth independence on $N\ge j_\infty(\kappa)^2$ is correct but does not remove the original resource constraint $N$.

At equal $N,\kappa$, extra diagonal terms, edge weights, phases or admissible state families change the state and the record; and different outcome-conditioned updates implement the same POVM. Hence **the generic ground-ray selection of one reference proxy does not prove a minimal selection datum for the instrument equivalence class**; that class must be defined operationally and the necessity that fewer data cannot select must be proved.

### S6.4 An additional construction: a conserving proxy with a finite charge source

Give the auxiliary system $B_Q$ charges $b=0,\ldots,B$, $Q_B=\sum_bb|b\rangle\langle b|$ and the lowering operator $L_B=\sum_{b=1}^B|b-1\rangle\langle b|$. In **this comparison model only** the bare Hamiltonian of the auxiliary is declared $0$; this is not a derived energy–charge relation of the actual S14 carrier.

$$
H_{\rm cons}=\nu E\otimes I-\frac J2\bigl(T_N\otimes L_B+T_N^\dagger\otimes L_B^\dagger\bigr),\qquad [H_{\rm cons},M+Q_B]=[H_{\rm cons},E]=0 .
\tag{G6}
$$

**Supplying** the initial auxiliary state $|\beta_B\rangle=(B+1)^{-1/2}\sum_{b=0}^B|b\rangle$,

$$
b_B=\langle L_B\rangle=\frac B{B+1},\qquad H_{\rm mf}=\nu E-Jb_BA_N .
\tag{G7}
$$

This is an explicit mean-field approximation that produces the form (G1) from a finite source with charge asymmetry; a charge-diagonal auxiliary state gives $\langle L_B\rangle=0$ and no such first-order term.

$T_N$ is a partial shift on paths, so $\|T_N\|\le1$; moreover $\|(L_B-b_B)|\beta_B\rangle\|=\|(L_B^\dagger-b_B)|\beta_B\rangle\|=\sqrt B/(B+1)$. Duhamel's formula on the initial product state gives, for every normalised $\psi$,

$$
\boxed{\bigl\|\{e^{-itH_{\rm cons}}-e^{-itH_{\rm mf}}\otimes I\}(\psi\otimes\beta_B)\bigr\|\le J|t|\frac{\sqrt B}{B+1}.}
\tag{G8}
$$

**Derivation.** $H_{\rm cons}-H_{\rm mf}\otimes I$ is $T_N\otimes(L_B-b_B)$ plus its adjoint; under the mean-field evolution the auxiliary stays at $\beta_B$, so the integrand norm is at most $J\sqrt B/(B+1)$ by the two residuals and $\|T_N\|\le1$; integrate in time. The difference of the Hamiltonians is bounded, so the state-wise Duhamel comparison is valid even with the common unbounded $\nu E$. $\square$

The bound also controls the trace distance of the joint pure states and of the reduced states; mixed inputs follow by purification and convexity. Numerically the auxiliary marginal does change. (G8) is a bound for **one use of a given initial auxiliary**, not a free-reuse theorem re-inserting $\beta_B$ at every step.

This provides the explicit finite comparison for the earlier O-2, but the exact $-JA_N$ does not appear automatically at finite $B$: $Jb_B$ and an error arise. $N$, $B$, initial asymmetry and preparation, reading time and coupling form are all inputs. Moreover (G6) does not mix $E$ shells and provides no cooling selection. **The existence of a conserving coupling and the dynamical preparation of the ground state remain separate obligations.**

### S6.5 Correcting the Gibbs statement: existence, monotonicity and clocks separated

In the original $\mathcal H_R=\ell^2(\mathbb Z)$, $A_N$ acts as $0$ on infinitely many vertices outside the finitely many edges, so $\operatorname{tr}e^{\beta JA_N}=\infty$. The state produced by the earlier finite rotor cutoff code is **the Gibbs state of that cutoff Hamiltonian**, not the thermal state of the unconstrained rotor. On a $\nu=0$ finite matrix, $d\langle A_N\rangle/d\beta=J\operatorname{Var}(A_N)\ge0$, so the observed monotonicity holds inside that model.

With $\nu>0$, $E$ is confining and $A_N$ bounded, so

$$
\rho_\beta=Z_\beta^{-1}e^{-\beta(\nu E-JA_N)}
\tag{G9}
$$

is trace class. With real positive edges and $[E,A_N]=0$ the in-shell matrix elements are non-negative, so $\Gamma(\rho_\beta)=\langle A_N\rangle_\beta$, and

$$
\frac{d\Gamma}{d\beta}=J\operatorname{Var}_\beta(A_N)-\nu\operatorname{Cov}_\beta(A_N,E),
\tag{G10}
$$

so there is no general monotonicity. For $N=1$, $\nu=1$, $J=1/2$ and $\beta=0.1,1,2,4,32$ one finds $\Gamma\simeq0.004238,\ 0.075993,\ 0.097031,\ 0.045617,\ 7.34\times10^{-10}$: at low temperature the ground state sits at $e=0$ and the record disappears again. The counterexample was computed with a theta-series partition function; the $|m|>60$ tail is far below numerical resolution even at $\beta=0.1$.

Since $[\rho_\beta,E]=0$, the **reference state itself** in (G9) is invariant under time translation by $E$, though within-shell charge coherence can exist. Reading this as "a symmetric equilibrium selected a record without external asymmetry" hides the charge violation of (G2) again; the full charge-conserving system with symmetric initial conditions must be modelled separately. Unitary phase clocks, thermodynamic ticking clocks and modular seam clocks are not the same object.


### S6.6 The exact conserving model: no record and the full ground space

From here $B$ is the maximal charge of the charge source $B_Q$ with $H_B=0$. The total generator is $Q=M+Q_B$ and the conserved energy $E=M^2+K$. The front-end measurement accesses only $S$ and $RC$; $B_Q$ is traced out. This is distinct from tasks in which the source is measured as well.

**T-NOREC — no record from covariant preparation.** If $[\rho_{RC},M]=0$ then $\Gamma(\rho)=0$. If $[\rho_{RCB},M+Q_B]=0$ then $[\operatorname{tr}_B\rho,M]=0$ and the same follows. If moreover the initial state is $Q$-invariant and the preparation channel $\Phi$ satisfies $\Phi(e^{-i\theta Q}\rho e^{i\theta Q})=e^{-i\theta Q}\Phi(\rho)e^{i\theta Q}$ for all $\theta,\rho$, the output carries no record either.

*Proof.* Every edge of $\Gamma$ joins distinct $M$ eigenvalues, so the first sentence is a trivial matrix-element computation. Commutators of $B$ operators vanish under the partial trace. The last sentence follows by substituting an invariant initial state into the covariant channel. Unitaries with $[H,Q]=0$, or dynamics whose Hamiltonian and all Lindblad jumps commute with $Q$, are sufficient; the statement is not universal for a Hamiltonian that commutes while the dissipator is unspecified. $\square$

This is not a new symmetry principle; it specialises the monotonicity of mode-wise trace norms under $U(1)$-covariant channels (Marvian–Spekkens §II A, (2.16)–(2.19)). The adjacent mode norm $\sum_q|\sigma_{q,q+1}|$ of the source quantifies the necessary resource for a positive record, but its positivity alone does not make the transfer formula positive.

**G11–G13 — starting point for the ground-space classification.** For $\nu,J>0$, $\kappa=J/\nu$, the $(e,q)$ block of $H_{\rm cons}$ is, on each connected component of $\{|m,e-m^2,q-m\rangle:0\le e-m^2\le N,\ 0\le q-m\le B\}$, a path with diagonal $\nu e$ and adjacent coupling $-J/2$. A $P$-vertex component has lowest energy $\nu e-J\cos[\pi/(P+1)]$. Broken one-sided components with $e>N$ are excluded by the central-dominance argument of S6.2. Among shells giving the same maximal length the lowest energy is $e=j^2$, so

$$
f_j=j^2-\kappa c_j^{(B)},\qquad c_j^{(B)}=\cos\frac\pi{\min(2j+1,B+1)+1},\qquad j\in\{0,\ldots,L\},\quad L=\lfloor\sqrt N\rfloor .
\tag{G13}
$$

Write $j_*$ for the unique minimiser away from thresholds. After $c_j^{(B)}$ saturates only $j^2$ grows, so $j_*\le\min(L,\lceil B/2\rceil)$ — **not** $\lfloor B/2\rfloor$. The thresholds of the truncated problem are $(2j+1)/(c^{(B)}_{j+1}-c^{(B)}_j)$ over the increasing $c^{(B)}_j$, and the infinite-source thresholds (G4) are not used up to the endpoint.

If $B\ge2j_*$ the complete paths are $q=j_*,\ldots,B-j_*$. With $j=j_*$,

$$
|\psi_q\rangle=\sum_{m=-j}^js_m|m,j^2-m^2\rangle|q-m\rangle,\qquad s_m=\frac1{\sqrt{j+1}}\cos\frac{\pi m}{2j+2},\qquad D=B-2j+1 .
\tag{G11}
$$

Each $\psi_q$ has fixed $Q$, so its accessible record is $0$. The **maximum over the full ground space**, allowing their coherent combination, is

$$
\Gamma_{\max}=C_j\cos\frac\pi{D+1},\qquad C_j=\cos\frac\pi{2j+2}.
\tag{G12}
$$

Its proof and the actual value for an arbitrary mixed source are in S6.8. (G12) is the valid part of the earlier T-2D; the reading "exactly two items of minimal physical data" is not included.

### S6.7 Counterexamples: truncated ends, thresholds and stronger coupling

**G14 — truncated ground space.** If a shell with $B<2j$ is the actual global ground, then $B$ is odd and $j=(B+1)/2$; only the two sectors $q=j-1,j$ survive. Each path has the $B+1=2j$ vertices $m=q-B,\ldots,q$ and

$$
|\psi_q\rangle=\sum_{m=q-B}^{q}a_{m-q+B}|m,j^2-m^2\rangle|q-m\rangle,\qquad a_r=\sqrt{\frac2{B+2}}\sin\frac{\pi(r+1)}{B+2}.
\tag{G14}
$$

Adjacent-$q$ paths overlap exactly under the shift $m\to m+1$, so the record overlap weight is $\sum_ra_r^2=1$, and the optimal coherent superposition of the two sectors gives

$$
\boxed{\Gamma_{\max}=\tfrac12\quad(\text{truncated end, }B\text{ odd}).}
\tag{G15}
$$

*Proof.* A larger $j$ gives the same $B+1$ length at higher $j^2$ cost. $B<2j\le2\lceil B/2\rceil$ with integers forces $B$ odd and $j=\lceil B/2\rceil$; the sector range comes from $-j\le q-B$ and $q\le j$. The $\Gamma$ between the two sectors is $|\sigma_{q,q+1}|$, at most $1/2$ for a positive trace-one $2\times2$ state. $\square$

**Even end.** If $B=2j$ only $q=j$ survives; the ground is a single total-charge state with $\Gamma=0$. The table below assumes the cutoff admits the end shell and $\kappa$ is large enough.

| $B$ | selected $j$ | ground sectors | ground-space maximum $\Gamma$ |
|---|---:|---:|---:|
| even | $B/2$ | 1 | 0 |
| odd | $(B+1)/2$ | 2 | 1/2 |

The maxima assume source-sector coherence; a symmetric source gives $\Gamma=0$ in both cases.

**W01 — a counterexample to coupling monotonicity.** At $N=4$, $B=4$, $\kappa=5$ selects $j=1$ with $\Gamma_{\max}=1/2$, while $\kappa=50$ selects $j=2$ with $\Gamma_{\max}=0$: strengthening the coupling at the same finite source widens the in-path charge range but reduces the number of total-charge sectors available to the ground space. Looking at the two factors of (G12) separately hides this trade-off.

**Thresholds.** When two adjacent $j$ have equal $f_j$ the direct sum of the ground spaces is used; coherence between different $e$ does not appear on equal-energy edges of $\Gamma$, so the maximum over the full ground space is the larger of the per-shell maxima. The degeneracy at a threshold is not erased by pretending a single $j$ was selected; clock tasks using other-shell coherence can be defined separately from S7.

### S6.8 Mixed-source transfer, phases and the exact scope of the optimisation

**G16 — the actual transfer formula.** For $B\ge2j$ and $\rho_{RCB}=\sum_{q,r}\sigma_{qr}|\psi_q\rangle\langle\psi_r|$, $\sigma\ge0$, $\operatorname{tr}\sigma=1$, tracing the source gives

$$
(\rho_{RC})_{mn}=s_ms_n\sum_q\sigma_{q,q+n-m},\qquad z_1:=\sum_{q=j}^{B-j-1}\sigma_{q,q+1},\qquad \boxed{\Gamma(\rho_{RC})=C_j|z_1|.}
\tag{G16}
$$

Elements outside the admissible $q,r$ are $0$ in the sums; this is a direct substitution of the source-trace condition $q-m=r-n$. The signed contrast of the fixed-phase C6 readout is $C_j\operatorname{Re}z_1$, and with a reading phase $\phi$ it is $C_j\operatorname{Re}(e^{i\phi}z_1)$, optimal at $\phi=-\arg z_1$; the fixed C6 does not select that phase automatically for an arbitrary complex profile.

For positive $\sigma$,
$$
|z_1|\le\sum_q|\sigma_{q,q+1}|\le\sum_q\sqrt{\sigma_{qq}\sigma_{q+1,q+1}}\le\cos\frac\pi{D+1},
$$
the last inequality being the Rayleigh maximum of a $D$-vertex path, attained by the pure sine amplitudes $c_r=\sqrt{2/(D+1)}\sin[\pi(r+1)/(D+1)]$; so (G12) follows. Profiles with constant adjacent phase difference give the same value after phase optimisation. At $D=1$, $z_1=0$. The battery's adjacent-coherence optimisation and the sine-optimal state are prior results (Navascués–Popescu §5.3 (32)–(34), Appendix E Theorem 2); the work here substitutes the **ground-space and accessible-$RC$ transfer restrictions**.

| Counterexample | Preparation | Actual result |
|---|---|---|
| W02: fixed phase is not optimal | $j=1$, $B=3$, $c=(1,i)/\sqrt2$ | $\Gamma=1/(2\sqrt2)$, fixed C6 contrast $=0$ |
| W03: asymmetry alone is not enough | $j=1$, $B=4$, $c=(1,1,-1)/\sqrt3$ | source mode-1 norm $2/3$ but $z_1=0$, $\Gamma=0$ |
| W05: an arbitrary profile is not maximal | $j=1$, $B=3$, $c=(\sqrt{0.9},\sqrt{0.1})$ | $\Gamma=0.3/\sqrt2$, ceiling $1/(2\sqrt2)$ |

**Weighted-sector lemma.** More generally, if the ground vectors of equal $e$ have non-negative amplitudes $a_q(m)$ and $q$ is consecutive, with $w_q=\sum_ma_q(m)a_{q+1}(m+1)$ and $(A_w)_{q,q+1}=(A_w)_{q+1,q}=w_q/2$, the maximum $\Gamma$ over the full ground space is $\lambda_{\max}(A_w)$: the triangle inequality on each edge gives $\Gamma\le\sum_qw_q|\sigma_{q,q+1}|$, and the Rayleigh principle after the positivity inequality gives the upper bound; in the pure sector state with non-negative Perron vector every edge sum has the same phase, so both inequalities are equalities. Complete paths have $w_q=C_j$, truncated ends $w_q=1$. This proof is compared with actual sector-eigenvector overlaps (V01/V04 of the inherited ledger), not with a closed formula re-entered into code.

### S6.9 Allocating a finite budget and actually preparing the ground state

**G17 — source budget allocation.** When $\kappa$ and the source state may be chosen but $N,B$ are fixed, the attainable maximum in the complete-path region is

$$
F_{B,N}(j)=\cos\frac\pi{2j+2}\cos\frac\pi{B-2j+2},\qquad 0\le j\le\min(L,\lfloor B/2\rfloor).
\tag{G17}
$$

For $B\ge4$, $N\ge1$ the global optimum is the admissible integer nearest $B/4$; the truncated odd-end value $1/2$ does not exceed it. Small cases: $N=0$ always $0$; $B=0,2$ give $0$; $B=1$ gives $1/2$ for $N\ge1$; $B=3$ gives $1/2$ for $N\ge4$ and $1/(2\sqrt2)$ for $1\le N<4$.

*Proof.* With $x=2j+2$, $y=B-2j+2$, $x+y=B+4$; for $x>2$, $f(x)=\log\cos(\pi/x)$ is increasing and
$$
f''(x)=-\frac{2\pi}{x^3}\tan\frac\pi x-\frac{\pi^2}{x^4}\sec^2\frac\pi x<0,
$$
so $f(x)+f(y)$ is maximal at $x=y$ and decreases symmetrically; on the integer lattice choose the admissible $j$ nearest $B/4$. At $B=4$ the value is $1/2$, and for $B\ge5$ the admissible $j=1$ alone exceeds $1/2$, so the truncated end is never better. Cutoff $L=0$ and $B\le3$ are computed directly from (G12)/(G15). $\square$

If $N$ is large enough to allow $j\approx B/4$,

$$
1-\max_jF_{B,N}(j)\sim\frac{4\pi^2}{(B+4)^2},
\tag{G18}
$$

and at $B=4a$ exactly $\Gamma_{\rm opt}=\cos^2[2\pi/(B+4)]$. This is a result on **distributing a paid source** in the given model, not a statement that increasing $B$ for free removes all reference cost.

**P1 — a type-preserving preparation isometry.** For $B\ge2j$, $q=j,\ldots,B-j$,

$$
Y|m,q\rangle=|m,j^2-m^2,q-m\rangle,\qquad Y^\dagger QY=I\otimes\operatorname{diag}(q),\qquad Y^\dagger EY=j^2I .
\tag{P1}
$$

The initial $|m=0,k=j^2\rangle\langle\cdot|\otimes\sigma_B$ is $|0\rangle\langle0|\otimes\sigma$ in this code; the source's charge coherence is supplied from the start.

**P2 — a finite control unitary.** With $s=(s_m)$, $s_0=1/\sqrt{j+1}$, $j\ge1$,

$$
w=\frac{s-s_0|0\rangle}{\sqrt{1-s_0^2}},\qquad h=i(|w\rangle\langle0|-|0\rangle\langle w|),\qquad \alpha=\arccos s_0,\qquad U=e^{-i\alpha h},
\tag{P2}
$$

$U|0\rangle=s$. Extending $Y(U\otimes I)Y^\dagger$ by the identity outside the code prepares the ground-space state $Y(|s\rangle\langle s|\otimes\sigma)Y^\dagger$ while conserving total $Q$ and $E$; $j=0$ is the identity. This is an existence construction with the control operation and the energy-$j^2$ initial preparation as inputs; $H_{\rm cons}$ alone does not generate this control, and an $E$-conserving unitary does not cool other bare-energy shells.

**P3 — cooling that acts consistently on the same sector.** In the code take $H_{\rm path}=-JA$ with eigenvectors $v_0=s,v_1,\ldots,v_{2j}$ and the jumps

$$
L_a=\sqrt\gamma\,|s\rangle\langle v_a|\otimes I_q,\qquad a=1,\ldots,2j .
\tag{P3}
$$

Together with $H_{\rm path}\otimes I_q$ the Lindblad generator is compatible with $Q,E$; it is an all-outcome channel with no successful-branch selection; the unitary part's energy relaxes into the environment while $E=j^2$ is unchanged; the sector degree of freedom is acted on by the identity, so the supplied $\sigma$ is preserved. Spectral-projector cooling and decoherence-free/noiseless structures are known general tools (Zhan et al. §II; Lidar–Chuang–Whaley); no efficient or local S14 cooling algorithm is claimed.

From the initial path state $|0\rangle$ the ground fidelity and trace distance are

$$
F(t)=1-(1-a_j)e^{-\gamma t},\qquad \epsilon_{\rm prep}(t)=\sqrt{1-a_j}\,e^{-\gamma t/2},\qquad D(\rho(t),\rho_\infty)\le\epsilon_{\rm prep}(t).
\tag{P4}
$$

*Proof.* Each excited population decays at rate $\gamma$ and its sum enters the ground; the sector state is unchanged; the fidelity–trace-distance inequality for the pure target $s$ and the contractivity of isometries and partial traces apply. Since any fixed-phase witness has norm $C_j$,
$$
\Gamma(t)\ge\max\{0,\Gamma_\infty-2C_j\epsilon_{\rm prep}(t)\}.
$$
This device gives an actual path from a real initial state without re-assuming (G12); the physical debt that the control, jumps and source are supplied as inputs is explicit.

### S6.10 Key additional result: environment correlation kernels with equal cooling rate and different records

That the jumps of P3 do not distinguish sectors is additional structure. The following comparison class relaxes it while fixing $H_{\rm path}$, $Q$, $E$ and the relaxation rate $\gamma$ of each energy.

**K1 — relaxation Gram matrix.** Take any $D\times D$ matrix $G\succeq0$ with $G_{qq}=1$, decompose $G_{qr}=\sum_\lambda b_{\lambda q}\overline{b_{\lambda r}}$, set $D_\lambda=\operatorname{diag}(b_{\lambda q})$ and use

$$
L_{a\lambda}=\sqrt\gamma\,|s\rangle\langle v_a|\otimes D_\lambda .
\tag{K1}
$$

All jumps commute with $Q,E$ and

$$
\sum_{a,\lambda}L_{a\lambda}^\dagger L_{a\lambda}=\gamma(I-|s\rangle\langle s|)\otimes I_q ,
\tag{K2}
$$

so the excited-population decay, the ground fidelity (P4) and the Hamiltonian energy relaxation are independent of $G$. $G$ carries the relative phases and overlaps that the relaxation paths of different $q$ have in the environment; it is not fixed by distinguishability moduli alone.

**K3 — exact transformation of the final source.** From the initial $|0\rangle\langle0|\otimes\sigma$,

$$
\boxed{\rho_\infty=|s\rangle\langle s|\otimes\sigma_\infty,\qquad \sigma_\infty=\bigl[a_j\mathbf 1\mathbf 1^{\mathsf T}+(1-a_j)G\bigr]\odot\sigma.}
\tag{K3}
$$

$\odot$ is the entrywise product; the bracket is a positive correlation matrix, so this is a trace-preserving CP Schur channel.

*Proof.* After a jump to the ground no further jump occurs. The excited part of the no-jump operation decays as $e^{-\gamma t/2}e^{-iH_{\rm path}t}$, and the initial ground component has weight $a_j=s_0^2$; that path transmits $\sigma$ unchanged. The total jump probability of the $a$-th excited component is $|\langle v_a|0\rangle|^2$ and its $q,r$ element summed over $\lambda$ is $G_{qr}\sigma_{qr}$; summing over $a\ge1$ gives $1-a_j$. Cross components between different excited $a$ do not survive this jump class, and the no-jump ground–excited cross terms decay. Adding the two paths gives (K3). $\square$

**K4 — separation of cooling and record.** Substituting (K3) in (G16) gives the transfer formula (U0) of S9.9. Supplying the same sine source, three environments compare as follows.

| $G$ | record after relaxation to the ground | $j=1$, $B=4$ |
|---|---|---:|
| $G=\mathbf 1\mathbf 1^{\mathsf T}$ | $\Gamma=\Gamma_{\rm ideal}$ | $1/2$ |
| $G=I$, an environment that distinguishes sectors | $\Gamma=a_j\Gamma_{\rm ideal}$ | $1/4$ |
| adjacent $G_{q,q+1}=-a_j/(1-a_j)$ | $\Gamma=0$ | $0$ |

The last row is admissible for $j\ge1$: with $t=-a_j/(1-a_j)\in[-1,0]$ and $v_q=(-1)^q$, $G=\tfrac{1+t}2\mathbf 1\mathbf 1^{\mathsf T}+\tfrac{1-t}2vv^{\mathsf T}$ is positive semidefinite with unit diagonal and adjacent entries $t$; the negative overlap phase cancels the adjacent coherence of the no-jump and jump paths. This is not a process generating symmetry resources; it is a process that keeps or loses a supplied resource.

**The judgement newly made possible.** Measuring the ground energy, spectral gap, cooling rate and final ground fidelity cannot certify record preparation; the additional information needed is the cross-sector correlation induced by the actual environment. For a specific initial state and record task one complex response $\sum_q[a_j+(1-a_j)G_{q,q+1}]\sigma_{q,q+1}$ suffices, but predicting every source, reuse and conditional update needs more channel data; counting "exactly two data" does not replace this operational distinction.

**Limits.** The construction uses a common $\gamma$ and a common $G$ for all excited $a$; if the actual bath gives $a$-dependent rates or $G$, or Lamb shifts create sector dependence, (K3) must be recomputed from the generator. The in-model proof of the kernel formula is complete, but it is not marked as a general theorem absent from the literature nor as the unique environment prediction of S14. S8.9 distinguishes the exact K5a of a specified GKLS generator and the absorbing cascade K6 from the exponential-emission/WW K5; K3 is the specialisation with common rate, common basis, complete absorption and no extra dephasing; general finite-time baths are computed directly in S8.15.


### S6.11 B14 — sector dispersion of the declared spin source (inherited, scope repaired)

#### S6.11.1 Motivation and the decisive kill test

The exact degeneracy of S6.6–S6.9 is a peculiarity of the flat $L_B$. B14 compares it with the declared spin source $L_S=S_-/\sqrt{S(S+1)}$. Two bosonic modes at fixed total particle number give this representation, but the finite-island Weyl quantisation of E26 has different finite edges (S6.13.1), and the CAR vertex of M70 does not automatically supply an arbitrarily large spin (S8.18.1). The flat ladder is also a $U(1)$ tensor with $[Q_B,L_B]=-L_B$, and the earlier sentence "it has no symmetry" is retracted. The kill test kept here is **whether the exact flat degeneracy is robust under changes of the source matrix elements** — the answer is no. All B14 numbers are for the declared model $J=1$, fixed shell $e=j^2$, complete paths $B\ge2j$.

#### S6.11.2 Definitions and types of the two finite sources

$$
L_B=\sum_{b=1}^B|b-1\rangle\langle b|\ \ (\text{flat}),\qquad
L_S=\frac{S_-}{\sqrt{S(S+1)}}=\sum_{b=1}^Ba_b|b-1\rangle\langle b|,\qquad a_b^2=\frac{b(B-b+1)}{S(S+1)},\ S=\frac B2 .
\tag{B14-0}
$$

The normalisation $\sqrt{S(S+1)}$ makes the two central amplitudes of even $B$ equal to $1$, $a_{B/2}=a_{B/2+1}=1$. Expanding,

$$
a_b^2=1+\frac{1-(2b-B-1)^2}{B(B+2)},\qquad a_b=a_{B+1-b}.
\tag{B14-0$'$}
$$

**B14-L1 [algebra].** $[L_B,L_B^\dagger]=|0\rangle\langle0|-|B\rangle\langle B|$ (boundary terms only) while $[S_-,S_+]=-2S_z$ (bulk). For $B\ge3$, $L_B$ is no scalar multiple of any $S_-$ ($a_1^2:a_2^2=B:2(B-1)$, equal only at $B=2$, where $L_S=L_B$). The flat ladder is a finite-dimensional truncation of a Susskind–Glogower-type shift, and the uniform superposition $|\beta_B\rangle$ is its phase state ($\langle L_B\rangle=B/(B+1)$ in G7). In the literature's classification the two sources correspond to "a phase reference of an energy-bounded oscillator mode" and "a spin-$j$ directional reference" (E25). **This distinction does not decide which one S14 supplies.** Fixed occupation of two CCR modes gives a spin representation, but the CAR bilinear of M70 alone does not select a large spin; the map between occupation, regional charge and collective representation is distinguished in S8.18.1 and remains OPEN.

The path Hamiltonian of sector $q$, whose edge $m\to m+1$ consumes source charge $b=q-m$, is

$$
H_q=-\frac J2\sum_{m=-j}^{j-1}a_{q-m}\bigl(|m\rangle\langle m+1|+{\rm h.c.}\bigr),\qquad b\in\{q-j+1,\ldots,q+j\}.
\tag{B14-H}
$$

#### S6.11.3 The sector dispersion theorem

**B14-T1 [fixed $j$, bounded $|q-B/2|$; first-order identity C12, remainder order V28 of the inherited ledger].** With $\psi_i=\sqrt{2/(P+1)}\sin[i\pi/(P+1)]$, $P=2j+1$, $s_i=\psi_i\psi_{i+1}$,

$$
E_q=-JC_j+\frac{2J}{B(B+2)}\Bigl[C_j\bigl(q-\tfrac B2\bigr)^2+\kappa_j\Bigr]+R_q,\qquad \kappa_j=\sum_{i=1}^{2j}s_i(j-i)(j+1-i),
\tag{B14-1}
$$

with $\kappa_1=0$, $\kappa_2=1/\sqrt3$, $\kappa_3=\sqrt{5/2-\sqrt2/4}$; for fixed $|q-B/2|\le3$, $|R_q|$ decreases by a factor of about $1/16$ when $B$ doubles (ratios $15.0$–$15.9$ from $B=16$ to $128$). For $j=1$ and even $B$ the central sector has both amplitudes exactly $1$, so $E_{B/2}=-JC_1$ is **exact**.

*Proof.* $a_b=1+\delta_b$, $\delta_b=(a_b^2-1)/2+O(B^{-4})=[1-(2b-B-1)^2]/[2B(B+2)]+O(B^{-4})$. First-order perturbation of the uniform path ground state $\psi$ gives $\Delta E=-J\sum_{i=1}^{P-1}\delta_{b(i)}\psi_i\psi_{i+1}$ with $b(i)=q+j+1-i$. With $u_i=j+\tfrac12-i$, $2b(i)-B-1=2(q-\tfrac{B+1}2)+2u_i+1$; the mirror symmetry $s_i=s_{P-i}$, $u_{P-i}=-u_i$ kills the odd moments, so
$$
\Delta E=\frac{2J}{B(B+2)}\Bigl[S_0\bigl((q-\tfrac{B+1}2)^2+(q-\tfrac{B+1}2)\bigr)+\sum_is_iu_i^2\Bigr],\qquad S_0=\sum_is_i=C_j .
$$
Substituting $(y^2+y)=(q-B/2)^2-1/4$ and $\sum_is_i(u_i^2-\tfrac14)=\sum_is_i(j-i)(j+1-i)=\kappa_j$ gives (B14-1). The identity was checked as an exact polynomial identity in $(q,B)$ for $j=1,2,3$ (for $j=3$, by expanding the numerator of the symbolic difference and verifying that every coefficient vanishes to 30 digits); second-order perturbation and the second-order part of $\delta_b$ are both $O(B^{-4})$, which the doubling ratios measure. $\square$

**B14-T2 [exact; V29].** For all $j,B$, $E_q=E_{B-q}$ and $\psi_{B-q}(m)=\psi_q(-m)$. *Proof.* $a_{B-q-m}=a_{q+m+1}$, so the amplitude of edge $(m,m+1)$ in sector $B-q$ equals that of edge $(-m-1,-m)$ in sector $q$: $H_{B-q}$ is the reflection of $H_q$. $\square$ The parabola of (B14-1) is centred at $B/2$, not $(B+1)/2$, as a consequence of this exact symmetry; the inherited fault injection rejects "centre $(B+1)/2$".

**B14-T3 [exact diagonalisation for $j\le2$, $B\le13$; no counterexample for $j\le4$, $B\le60$ in a separate audit; general $B$ rests on first-order perturbation and is a hypothesis].** The ground sector is unique, $q=B/2$, for even $B$, and an exactly degenerate adjacent pair $q=(B\pm1)/2$ for odd $B$. By the weighted-sector lemma of S6.8 the **maximal record of the exact ground space** is

$$
\Gamma_{\max}^{\rm ground}=\begin{cases}0,&B\text{ even},\\ w/2,&B\text{ odd},\end{cases}\qquad
w=\sum_m\psi_{(B-1)/2}(m)\psi_{(B+1)/2}(m+1),\qquad C_j<w<1,\ \ w\to C_j\ (B\to\infty).
\tag{B14-2}
$$

| $j$ | $B$ | ground sectors | $\Gamma_{\max}^{\rm ground}$ (su(2)) | flat (G12) $C_j\cos[\pi/(D+1)]$ |
|---|---|---|---:|---:|
| 1 | 4 | {2} | 0 | 0.5000 |
| 1 | 5 | {2,3} | 0.3638 ($w$=0.7276) | 0.5721 |
| 1 | 8 | {4} | 0 | 0.6533 |
| 1 | 9 | {4,5} | 0.3571 ($w$=0.7143) | 0.6645 |
| 1 | 13 | {6,7} | 0.3554 ($w$=0.7107) | 0.6866 |
| 2 | 6 | {3} | 0 | 0.6124 |
| 2 | 7 | {3,4} | 0.4564 ($w$=0.9128) | 0.7006 |
| 2 | 13 | {6,7} | 0.4410 ($w$=0.8820) | 0.8309 |

The direction of the parity effect (odd → two sectors, even → one) agrees with the truncated ends G14–G15 but the origin differs: there it was clipping at $B<2j$ with the exact values $1/2$ and $0$; here it is bulk dispersion in the complete-path region $B\ge2j$ with values $w/2\in(C_j/2,1/2)$ and $0$. At $D=2$ ($B=2j+1$) the su(2) value slightly exceeds the flat one ($w>C_j$), and for $D\ge3$ it falls below the flat G12 value. $w>C_j$ because the two adjacent ground vectors are mirror images tilted toward the central edge, so the overlaps of the pairs $m\leftrightarrow-m-1$ exceed those of the uniform sine. For $j=1$ and odd $B$ the closed form $w=(B+1)/\sqrt{2(B^2+2B-1)}$ holds (exact three-site ground vector; derived by a separate audit agent and re-confirmed symbolically), proving $C_1<w<1$; for $j\ge2$, $C_j<w<1$ is verified in the numerical range.

**B14-T4 [fixed $j$; rigorous Weyl upper bound with $O(1/B)$ convergence, V30].** For fixed $\alpha=(q-B/2)/B$, $|\alpha|<1/2$,

$$
\frac{E_q}J\longrightarrow-C_j\sqrt{1-4\alpha^2}\qquad(B\to\infty),
\tag{B14-3}
$$

with relative error halving as $B$ doubles (ratios $1.9$–$2.4$ from $B=32$ to $256$). *Proof (upper bound).* With $s=\sqrt{1-4\alpha^2}$, $H_q=sH_{\rm unif}+\Delta H$, $\Delta H=-\tfrac J2\sum_m(a_{q-m}-s)(|m\rangle\langle m+1|+{\rm h.c.})$; the path adjacency norm is $2C_j$, so $\|\Delta H\|\le JC_j\max_b|a_b-s|$, and Weyl's inequality gives $|E_q+JC_js|\le JC_j\max_b|a_b-s|$; over the $2j$ values of $b$ in the sector, $a_b^2-s^2=O(j/B)$, so the bound is $O(j/B)$. Verified for $j\le3$, $B\le512$, $\alpha\in\{.1,.25,.4\}$ (actual error over bound at most $0.46$). $\square$ At the end sector $q=j$, $a_1^2=4/(B+2)$ suppresses hopping and $E_j\to0$ as $B^{-1/2}$ ($E_1$ halves as $B$ quadruples). (B14-3) has the functional form of the tunnelling suppression $\sqrt{1-(n/N)^2}$ of finite-island Josephson junctions (E26) with $n/N\leftrightarrow2\alpha$; this is a continuum coincidence of form, not an identity of finite models — the exact Weyl edge and the spin edge are distinguished in S6.13.1. Expanding (B14-3) at small $\alpha$ reproduces the curvature $2C_j/B^2$ of (B14-1).

#### S6.11.4 Dynamics of the record: cost, lifetime and revival

**B14-T5 [verified: $j=1$, $B\in\{32,64\}$, $D\in\{8,16\}$; $j=2$, $(B,D)=(32,8),(64,8),(33,8)$; V31, W15 of the inherited ledger].** Loading the sine profile $c_r$ (S6.8) on the ground vectors of the central $D$ sectors ($q=B/2-\lfloor D/2\rfloor,\ldots$; for even $D$ the window is offset by $-\tfrac12$) and evolving the pure state $\sum_qc_q|\psi_q\rangle$ under the closed $H_{\rm cons}$ of the su(2) source, the record (G16) is

$$
\Gamma(t)=\sum_m\Bigl|\sum_qc_qc_{q+1}e^{-i(E_q-E_{q+1})t}\psi_q(m)\psi_{q+1}(m+1)\Bigr|,\qquad
E_q-E_{q+1}=-\Omega\bigl(q-\tfrac B2+\tfrac12\bigr)+O(B^{-4}),\quad \Omega=\frac{4JC_j}{B(B+2)} .
\tag{B14-4}
$$

The adjacent-sector coherence rotates as a **linear chirp** in $q$. Results:

| $(j;B,D)$ | $\Gamma(0)$ | flat prediction $C_j\cos\frac\pi{D+1}$ | $\Gamma_{\min}$ | $t_{1/2}$ (± grid 2–8) | $t_{1/2}\Omega D$ | $\Gamma(T_{\rm rev})/\Gamma(0)$ | energy above ground (computed / formula) |
|---|---:|---:|---:|---:|---:|---:|---|
| (1; 32, 8) | 0.6651 | 0.6645 | 1.3e−4 | 277.5 | 5.77 | 0.990 | 3.785e−3 / 3.760e−3 |
| (1; 32,16) | 0.6958 | 0.6951 | 5.2e−5 | 138.9 | 5.78 | 0.758 | 1.289e−2 / 1.260e−2 |
| (1; 64, 8) | 0.6646 | 0.6645 | 8.8e−5 | 1085.5 | 5.82 | 0.9994 | 9.70e−4 / 9.68e−4 |
| (1; 64,16) | 0.6952 | 0.6951 | 2.9e−5 | 553.6 | 5.93 | 0.970 | 3.263e−3 / 3.245e−3 |
| (2; 32, 8) | 0.8166 | 0.8138 | 6.9e−4 | 228.6 | 5.82 | 0.997 | 4.597e−3 / 4.605e−3 |
| (2; 64, 8) | 0.8145 | 0.8138 | 1.9e−4 | 888.2 | 5.83 | 0.9998 | 1.186e−3 / 1.186e−3 |
| (2; 33, 8) | 0.8164 | 0.8138 | 6.6e−4 | 241.7 | 5.80 | 0.992 | 5.091e−3 / 5.087e−3 |

(i) **The initial record equals the flat value** (difference $<3\times10^{-3}$): the value of (G12) for the sine profile and $D$ is kept. (ii) **Decay.** $t_{1/2}\Omega D\simeq5.8$ is constant across $j=1,2$, the parity of $B$ and $D$, so $t_{1/2}\simeq0.92\cdot2\pi/(\Omega D)=1.45\,B(B+2)/(C_jJD)$ ($2.05\,B(B+2)/(JD)$ at $j=1$); a factor $3.91$ when $B$ doubles (predicted $64\cdot66/(32\cdot34)=3.88$) and $0.50$ when $D$ doubles. The constant $5.8$ is a window-dependent number set by the Fourier width of the $D$-sector sine (Hann-type) window and is not proved in closed form. The earlier $j$-independent constant $2.1$ absorbed $1/C_1$ and was $20\%$ wrong at $j=2$; corrected. At $t=4\pi/(\Omega D)$ the record is $2.7\%$ of its initial value and $1.6\%$ at $6\pi/(\Omega D)$. (iii) **Revival.** The equally spaced chirp of (B14-4) gives revival at $T_{\rm rev}=2\pi/\Omega=\pi B(B+2)/(2C_jJ)$; the $O(B^{-4})$ energy remainder accumulates phase error $O(B^{-2})$ over $T_{\rm rev}=O(B^2)$ and the revival deficit is its square, $O(B^{-4})$ (deficit $0.0097\to0.0006$, ratio $15.6$, for $D=8$, $j=1$). At $D=16$ the wider window makes the $O((q-B/2)^4/B^4)$ terms larger and the revival incomplete. (iv) **Cost.** This state is not the ground state of the su(2) model; its mean energy above the exact ground sector is the weighted average of (B14-1) minus the ground energy, $\frac{2JC_j}{B(B+2)}[\langle(q-B/2)^2\rangle_c-\tfrac{B\bmod2}4]+O(B^{-4})$. **$\kappa_j$ enters the ground-sector energy with the same size and cancels.** An earlier draft kept $\kappa_j$, invisible at $j=1$ ($\kappa_1=0$) but $19\%$ wrong at $j=2$; found and corrected in a separate audit (V31 now rejects the draft formula at $j=2$ explicitly). The relative error is $O(B^{-2})$ (ratio $3.9$ from $B=32$ to $64$). (v) **Flat contrast.** Evolving the same initial state with the flat source keeps $\Gamma$ constant to machine precision.

**Interpretation.** What the earlier versions read as "the record of a degenerate ground space" is, in this fixed-$j$ regime of the declared spin source, **a finite-lifetime record prepared at an energy cost**; size ($\Gamma(0)\to C_j$ needs large $D$) and lifetime ($\propto B^2/D$) trade against each other. This quantifies the clock task of S7.2 and the "persistence is not automatic" of S9.6; the record's own rotation with period $T_{\rm rev}$ does not conflict with the no-free-clock rule D-HCLK-001 (the phase comes from real energy differences of $H_{\rm cons}$). The scaling matches E25's quadratic lifetime of a bounded reference but the origins differ (measurement backaction versus Hamiltonian dispersion), so they are not identified. The collapse and revival of a superposition over a quadratic spectrum is the standard phase-diffusion mechanism (E27), and the semicircle law is classically $\langle S_x\rangle_{\max}=S\sqrt{1-(S_z/S)^2}$; what B14 adds is the exact placement of this standard mechanism in the rotor–source sector structure and the record quantity (G16).

**B14-T6 [verified, V32].** The transition frequencies $\omega_q^{(a)}=E_q^{(a)}-E_q^{(1)}$ of the excited levels $a=2,\ldots,P$ differ between adjacent sectors by

$$
\omega_{q+1}^{(a)}-\omega_q^{(a)}=\frac{2J}{B(B+2)}\Bigl[\cos\frac{a\pi}{P+1}-C_j\Bigr]\bigl(2(q-\tfrac B2)+1\bigr)+O(B^{-4})
\tag{B14-5}
$$

(remainder doubling ratios $15.1$–$15.9$ for $j=1,2$, $B=16\to128$). **This differs qualitatively from (T2) of T-TILT**: there $Uq^2$ was an additive term common to all levels and the transition-frequency difference was $O(U^2)$, whereas the source amplitudes multiply each level's Rayleigh quotient, so the difference is **first order**. In the K5 kernel of S8.9, $|G_{q,q+1}|=[1+(\delta\omega/\gamma)^2]^{-1/2}$ (same rate, same basis) now has $\delta\omega$ fixed by (B14-5) rather than free. For $j=1$, $B=32$ at the top level, $\delta\omega=2.60\times10^{-3}J$, and $\gamma=\delta\omega/10,\ \delta\omega,\ 10\delta\omega$ give $|G|=0.0995,\ 0.7071,\ 0.9950$. The adjacent mismatch is proportional to $|2(q-B/2)+1|$, hence up to $\sim D$ times larger over a $D$-sector window. Record-preserving cooling requires $\gamma\gg2|\cos(a\pi/(P+1))-C_j|\,JD/(B(B+2))$; large $B$ alone does not guarantee that inequality for actual rates. The rate was not recomputed in v1.6; S8.18 computes it from the gap and dipole of the same block.

**B14-T7 [verified, the limit direction of V28, V31].** At fixed $j$ and fixed sector window $|q-B/2|\le w$: $\sup_q|E_q-E^{\rm flat}|=O(J(w^2+1)/B^2)$, ground-vector difference $O(B^{-2})$, record lifetime $t_{1/2}\to\infty$. The flat results of S6.6–S6.9 are the $B\to\infty$ leading term of the su(2) source, but not uniformly: end sectors do not converge, by (B14-3).

#### S6.11.5 What changes and what remains

| Object | up to v1.5 | v1.6 |
|---|---|---|
| G11 degenerate ground space | property of the finite source | flat $L_B$ only; W14: any $b$-dependent amplitude perturbation $\epsilon$ splits the degeneracy by $\propto\epsilon$ |
| G12, G16 | ground-space maximal record | approximated by the initial value in the fixed-$j$ spin regime; the joint limit is computed with the different bound of B15 |
| G14–G15 clipping parity | $B<2j$, values $1/2$, $0$ | kept; in addition the bulk parity $w/2$, $0$ of the complete-path region (B14-T3) |
| G17–G18 budget allocation | ground-space optimum $j\approx B/4$ | exact for flat only; fixed-$j$ asymptotics cannot justify a $j\propto B$ optimisation; replaced by the separate joint-limit construction of S6.12 |
| P1–P4 preparation isometry and cooling | identity on sectors | kept; since the target is not a ground space, the "ground fidelity" of P3 refers to the direct sum of per-sector grounds |
| K1–K4, K5, K6 | $G$ free, $\delta\omega$ free | physical origin of $\delta\omega$ secured (B14-T6); K5 applicability condition $\gamma\gg\Omega D\,\vert \cos(a\pi/(P+1))-C_j\vert /(2C_j)$ |
| T-TILT | additive $Uq^2$ | distinguished from multiplicative dispersion; both to be recomputed from the physical $H_C$ (S8.13) |
| T★ | OPEN | OPEN; which source is used is now an explicit additional input |

**Left by v1.6 and handed to v1.7.** (a) Whether the S14/M70 boundary current is of flat, su(2) or bounded-oscillator type (amplitudes $\sqrt b$, no mirror symmetry) is OPEN; the third type was not entered in the verifier, and preliminary numerics ($j\le2$, $B\le64$) only showed sector energies decreasing monotonically in $q$ with the ground sector at the end $q=B-j$ (hypothesis). (b) Recomputation of K5a/K6 at finite $B$ including the competition of the cooling rate with $\Omega$. (c) A coupled model of the su(2) source with the electrostatic $H_C$ of S8.13. The first bright-transition competition of (b) is computed in S8.18 and the explicit coupled model of (c) in S6.13; the S14 selection of the source and the full bath remain obligations.


### S6.12 B15 — a record-preserving band from localisation of a common parent matrix

#### S6.12.1 The question missed by fixed-shell expansions

The asymptotics of B14-T1, T4, T7 are for **fixed $j$**; the remainder constant of B14-T1 contains $j$-dependent matrix sizes, moments and inverse gaps. So one cannot let $j$ grow with $B$, as in the budget allocation of S6.9, and substitute the lifetime formula of B14-T5. Instead of that extrapolation, a separate route reads the $H_q$ as different principal submatrices of one parent matrix.

Take $\hbar=1$, $J>0$, integers $B\ge2$, $j\ge1$, $N\ge j^2$. The physical basis of sector $q$ is

$$
|m\rangle_q=|m,\ j^2-m^2,\ q-m\rangle_{R,C,B},\qquad -j\le m\le j,
\tag{B15-0}
$$

all with $E=M^2+K=j^2$ and $Q=M+Q_B=q$. In this section $E$ is the bare conserved quantity and $H_q$ the interaction inside its shell; the common energy $\nu j^2$ is dropped once, and no sector-dependent energy zero is subtracted.

Reordering by $b=q-m$, B14-H is exactly

$$
H_q=P_qA_BP_q\big|_{\operatorname{Ran}P_q},\qquad A_B=-\frac{JS_x}{\sqrt{S(S+1)}},\qquad I_q=\{q-j,\ldots,q+j\},\qquad P_q=\sum_{b\in I_q}|b\rangle\langle b| .
\tag{B15-1}
$$

This is not an approximation matching different $q$ matrices; it is an exact identity that each sector cuts the same parent at the **same source coordinate $b$**.

#### S6.12.2 The general parent-matrix theorem: common bounds on energy, vectors and record

**B15-T1 [proven, stated range of finite matrices].** Let $A$ be a real symmetric tridiagonal matrix on $\{0,\ldots,B\}$ with all interior off-diagonal entries negative, simple ground eigenvalue $E_*$, normalised positive ground vector $\beta$, gap $g=\lambda_1(A)-E_*>0$ and width $\Lambda=\lambda_{\max}(A)-E_*$. Use equal-length intervals $I_q=[q-j,q+j]\subseteq[0,B]$, with $\psi_q,E_q$ the normalised positive ground vector and energy of $H_q$, and

$$
p_q=\|(1-P_q)\beta\|^2,\quad p=\max_qp_q<1,\quad \zeta_q=\frac{P_q\beta}{\sqrt{1-p_q}},\quad \delta=\frac{\Lambda p}{1-p},\quad \varepsilon=\sqrt{\frac{2\delta}g}.
\tag{B15-2}
$$

Then

$$
E_*\le E_q\le E_*+\delta,\qquad \|\psi_q-\zeta_q\|\le\varepsilon ,
\tag{B15-3}
$$

norms taken after zero extension to the common $b$ space.

*Proof.* $X=A-E_*\ge0$, $X\beta=0$. With $\phi=P_q\beta$, $\eta=(1-P_q)\beta$: $\langle\phi,X\phi\rangle=\langle\eta,X\eta\rangle\le\Lambda\|\eta\|^2=\Lambda p_q$. The Rayleigh principle and min–max for compressions give $0\le E_q-E_*\le\langle\zeta_q,H_q\zeta_q\rangle-E_*\le\Lambda p_q/(1-p_q)\le\delta$. The second eigenvalue of the compression satisfies $\lambda_1(H_q)\ge\lambda_1(A)=E_*+g$. Decomposing $\zeta_q=a\psi_q+\xi_q$ with $\xi_q\perp\psi_q$: $\langle\zeta_q,(H_q-E_*)\zeta_q\rangle\ge g\|\xi_q\|^2$, so $\|\xi_q\|^2\le\delta/g$; the positive phase convention gives $a\ge0$ and $\|\zeta_q-\psi_q\|^2=2(1-a)\le2(1-a^2)=2\|\xi_q\|^2$. $\delta<g$ is not a condition of the theorem, but a useful lower bound needs a small enough tail. $\square$

**B15-T2 [proven, same assumptions].** Choose $D\ge2$ consecutive sectors and supply the positive amplitudes

$$
c_r=\sqrt{\frac2{D+1}}\sin\frac{(r+1)\pi}{D+1},\qquad 0\le r<D,\qquad C_D=\cos\frac\pi{D+1}.
\tag{B15-4}
$$

Reading $\psi_q(m)$ in the coordinates (B15-0),

$$
w_q=\sum_{m=-j}^{j-1}\psi_q(m)\psi_{q+1}(m+1)\ge1-2p-2\varepsilon,
\tag{B15-5}
$$
$$
\Gamma(0)=D_{\rm C6}(0)=\sum_qc_qc_{q+1}w_q\ge C_D(1-2p-2\varepsilon).
\tag{B15-6}
$$

At $D=1$ there is no inter-sector coherence and the record is $0$.

*Proof.* Adjacent terms share the source coordinate $q-m=(q+1)-(m+1)=b$, so the overlap of the truncated parent vectors is $w_q^{(\zeta)}=\sum_{b\in I_q\cap I_{q+1}}|\beta_b|^2/\sqrt{(1-p_q)(1-p_{q+1})}\ge1-p_q-p_{q+1}\ge1-2p$ (trivial if the right side is negative; otherwise the denominator is at most $1$). The one-step shift has norm $1$, so replacing $\zeta$ by $\psi$ costs at most $\varepsilon$ per vector. The sine path identity $\sum_qc_qc_{q+1}=C_D$ gives (B15-6). All initial coherences are real and non-negative, so the phase-zero C6 realises $\Gamma(0)$ without modulus optimisation. $\square$

**B15-T3 [proven; closed storage evolution and C6 readout].** Evolving

$$
|\Psi_0\rangle=\sum_qc_q\sum_m\psi_q(m)|m,j^2-m^2,q-m\rangle
\tag{B15-7}
$$

under $H=\bigoplus_qH_q$, for every real $t$,

$$
\Gamma(t)\ge D_{\rm C6}(t)\ge\bigl[C_D(1-2p-2\varepsilon)-2|t|\delta\bigr]_+ .
\tag{B15-8}
$$

*Proof.* All $E_q\in[E_*,E_*+\delta]$, so $\|\,|\Psi_t\rangle-e^{-iE_*t}|\Psi_0\rangle\,\|^2=\sum_qc_q^2|e^{-i(E_q-E_*)t}-1|^2\le t^2\delta^2$. The trace distance of pure states is at most this norm and does not increase under partial trace, attachment of the probe input or the C6 instrument. Each probe input's outcome distribution moves by at most $|t|\delta$, so the total variation between the two inputs decreases by at most $2|t|\delta$. Substitute (B15-6). $\square$

No $q$-dependent phase corrections and no time-adapted readout are used. The C6 device is that of S7.3 with $[F_\pm,N_S+M]=[F_\pm,E]=0$. **This is not a proof that C6 commutes with the full Hamiltonian including a switched-on storage interaction**; the switching, apparatus and work budget at readout remain to be implemented physically.

#### S6.12.3 The spin parent: exact ground, boundary flux and tail

The full spectrum of the spin parent is the equally spaced spectrum of $S_x$, so

$$
E_*=-J\sqrt{\frac B{B+2}},\qquad g=\frac{2J}{\sqrt{B(B+2)}},\qquad \Lambda=2J\sqrt{\frac B{B+2}},\qquad \beta_b=2^{-B/2}\sqrt{\binom Bb}.
\tag{B15-9}
$$

In particular $\Lambda/g=B$. The ground equation is confirmed at the rational level by binomial adjacent ratios (C15 of the inherited ledger) and compared with dense diagonalisation (V33).

For $I=[l,u]$, $\pi_b=|\beta_b|^2$, $Z=\sum_I\pi_b$, $c=J/\sqrt{B(B+2)}$, the Rayleigh deficit of the truncated trial state is exactly

$$
\langle\zeta,(H_I-E_*)\zeta\rangle=\frac{c[l\pi_l+(B-u)\pi_u]}Z .
\tag{B15-10}
$$

*Derivation.* Multiplying the $b\leftrightarrow b+1$ hopping modulus by $\beta_b\beta_{b+1}$ gives $c(B-b)\pi_b=c(b+1)\pi_{b+1}$; interior edges of $P\beta$ cancel in the ground equation and only the flux across the two boundaries survives; a boundary at $l=0$ or $u=B$ has zero flux. This also gives per-sector upper bounds sharper than the universal tail bound of (B15-3).

The ground similarity transform of the parent is the Ehrenfest birth–death generator

$$
-\beta^{-1}(A_B-E_*)\beta\,f(b)=c\bigl[(B-b)(f(b+1)-f(b))+b(f(b-1)-f(b))\bigr],
\tag{B15-11}
$$

a known tool (binomial/Krawtchouk structure) not named here as a new principle.

Now let $B$ be even, $q=B/2-w,\ldots,B/2+w$, $D=2w+1$, integers $0\le w<j$, $j+w\le B/2$. Every $I_q$ contains at least $h=j-w$ on both sides of the centre, so

$$
p\le\Pr\{|X-B/2|>h\}\le2e^{-2h^2/B},\qquad X\sim{\rm Binomial}(B,\tfrac12),
\tag{B15-12}
$$

by Chernoff with $\mathbb Ee^{s(X-B/2)}=(\cosh(s/2))^B\le e^{Bs^2/8}$ and $s=4h/B$ on each tail. In computations the exact binomial sum is used for $p$, and the exponential form is not used as a denominator bound when it exceeds $1$.

For admissible integer sequences $j=aB+O(1)$, $w=bB+O(1)$, $0<b<a$, $a+b\le1/2$,

$$
\delta=O\bigl(Je^{-2(a-b)^2B}\bigr),\qquad \varepsilon=O\bigl(\sqrt B\,e^{-(a-b)^2B}\bigr),\qquad \Gamma(0)\ge1-O(B^{-2})-O\bigl(\sqrt B\,e^{-(a-b)^2B}\bigr).
\tag{B15-13}
$$

For a fixed loss $\ell>0$, (B15-8) guarantees an additional loss at most $\ell$ up to $T_\ell=\ell/(2\delta)$, so the sufficient storage time grows at least like $J^{-1}\exp[2(a-b)^2B]$. This is neither an upper bound on the optimal lifetime nor a result for all initial states. The exponent $2(a-b)^2$ is the Hoeffding approximation; the exact rate is $I(a-b)\ge2(a-b)^2$ (B18-T2 iv). $T_\ell=\ell/(2\delta)$ is only a sufficient condition; the actual first-passage time is decided by the two-sided brackets of B18-T4 (differences of $e^{8.7}$–$e^{12.6}$ at finite loss, W20). In the main text Theorem 2 replaces both by the exact interval.

#### S6.12.4 Preparation and the resource ledger

For each $q$ there is a finite-dimensional unitary $U_q$ sending $|0,j^2,q\rangle$ to $|\psi_q\rangle$ of (B15-7): if two normalised real vectors $u,v$ differ, the Householder reflection $I-2|u-v\rangle\langle u-v|/\|u-v\|^2$ sends $u$ to $v$; if equal use the identity. Extending $U=\bigoplus_{q,E}U_{q,E}$ by the identity outside the shells,

$$
[U,Q]=[U,E]=0,\qquad U\sum_qc_q|0,j^2,q\rangle=|\Psi_0\rangle .
\tag{B15-14}
$$

This is the $q$-dependent-target extension of P2. Conservation is with respect to M71's bare $Q,E$ operation class and does not mean $[U,H_{\rm cons}]=0$; the work and switching needed to change the interaction energy are separate preparation costs whose physical derivation remains.

The $c_q$ coherence of the input is a **supplied resource**; a block-diagonal $U$ does not create coherence between different total-$Q$ sectors from nothing. Interpreting $Q$ as actual electromagnetic total charge requires a separate proof of physical admissibility of preparation and purification. The $q$-wise unitary control is a capability of the declared operation space, not a natural relaxation selected by S14.

The compensator cutoff and bare energy are $N\ge j^2$ and $\nu j^2$, so a linear-$j$ construction pays budgets of order $B^2$ in both, plus the source particle number $B$, the width $D$ of the total-$Q$ distribution, the initial asymmetry, preparation time and control, bath and readout. The exponentially small **band width** is never turned into an exponentially small total preparation energy. With $N=j^2$ the lifetime lower bound is exponential in $B$, but as a function of the compensator bandwidth $N$ it is a sufficient bound of the form $J^{-1}\exp[\Omega(\sqrt N)]$, not $\exp(\Omega(N))$.

| Resource / task | Secured by B15 | Not secured |
|---|---|---|
| initial record | high $\Gamma$ from given coherence and conserving unitary | free asymmetry from a symmetric state |
| storage | closed $H$, all-outcome distribution bound of fixed C6 | lifetime under general noise and repeated-measurement backaction |
| energy | same $E=j^2$ shell and the stated small band width | free supply of $N,\nu j^2$ or full-$H$ readout conservation |
| clock | record bound with time as a parameter | physical clock and loss function of D-HCLK-001 |
| source | declared spin or general parent | S14/M70 microstates selecting that representation |

#### S6.12.5 Numerics and adversarial tests

In the $J=1$ table below the time is $T_{0.01}=0.01/(2\delta)$ with $\delta$ from the exact binomial tail sum (V35 of the inherited ledger).

| $B,j,D$ | required $N$ | $p$ | $\delta/J$ | $\Gamma(0)$ | $JT_{0.01}$ | $D_{\rm C6}(T_{0.01})$ | proved lower bound |
|---|---:|---:|---:|---:|---:|---:|---:|
| 64,21,11 | 441 | $1.21823\,10^{-5}$ | $2.39929\,10^{-5}$ | 0.965925 | 208.395 | 0.965925 | 0.879616 |
| 96,32,17 | 1024 | $1.55512\,10^{-7}$ | $3.07833\,10^{-7}$ | 0.984808 | 16242.6 | 0.984808 | 0.964045 |
| 128,42,21 | 1764 | $2.07800\,10^{-9}$ | $4.12390\,10^{-9}$ | 0.989821 | 1212443.8 | 0.989821 | 0.978378 |

These are float64 evaluations of the theorem's bound, rounded, not interval certificates; the nearly unchanged floating values do not mean infinite lifetime or exact degeneracy — only the displayed lower bound is guaranteed. V34 constructs the full state on small models and compares the sector formula with the source partial trace and the actual C6 effects; V33 compares dense diagonalisation, Rayleigh and vector bounds.

W16 applies B14-T5 outside its range to $B=96$, $j=32$, $D=17$ at $Jt=803.357$ and finds $\Gamma(t)/\Gamma(0)>0.999999$ — a counterexample to the **unrestricted extrapolation** of the fixed-$j$ theorem, not to the theorem, and consistent with the finite checks of B14-T3 that the exact global ground is one or two sectors: B15 uses a very narrow low-energy band, not that single ground point.

### S6.13 B16 — extensions and counterexamples allowed by electrostatics and actual source coefficients

#### S6.13.1 The exact coefficients of E26 and their separation from the spin model

In the same edge notation, the spin coefficient $b\to b+1$ of B14-0 is

$$
(a_b^S)^2=\frac{4(b+1)(B-b)}{B(B+2)},\qquad 0\le b<B .
\tag{B16-0}
$$

Equation (6) of Maldonado–Rodriguez–Türeci (E26), in the imbalance coordinate $n=b-B/2$, $B=2N$, with midpoint/Weyl ordering, gives

$$
(a_b^W)^2=1-\Bigl(\frac{2b+1-B}B\Bigr)^2 .
\tag{B16-1}
$$

Both share the semicircle form in the continuum limit but the finite matrices differ: at $B=4$ the first two squared edges are spin $(2/3,1)$ and Weyl $(7/16,15/16)$, with different ratios, so no single overall coupling redefinition identifies them (C14 of the inherited ledger). This is not a claim that E26's quantisation is wrong; it is a correction of the earlier mapping to that source.

B15-T1–T3 are not restricted to spin coefficients: the Weyl matrix also has negative interior edges and a positive ground, so recomputing $\beta,g,\Lambda,p$ for it gives the same compression theorem. The binomial law, gap and exponential constants of the spin case are not copied to the Weyl model (see Proposition 12 of the main text for the verified equality of the exponential rate).

#### S6.13.2 Source-only charging fits into one parent matrix

Adding a term $V(b)$ depending only on the source charge,

$$
A^{(V)}=A_B+\operatorname{diag}V(b),\qquad H_q=P_qA^{(V)}P_q ,
\tag{B16-2}
$$

preserves the assumptions of the B15 theorems. Whether the ground distribution broadens or narrows is decided by the actual $V$; no assumption that every charging strengthens localisation is made.

The comparison of V36 at $B=48$, $j=16$, $w=4$, $D=9$ with $V(b)=\kappa(b-24)^2$ ($\kappa$ in units of $J$):

| source | $\kappa/J$ | $p$ | actual band width$/J$ | $\delta/J$ | $\Gamma(0)$ | initial proved bound |
|---|---:|---:|---:|---:|---:|---:|
| spin | 0 | $1.11123\,10^{-4}$ | $3.86082\,10^{-5}$ | $2.17779\,10^{-4}$ | 0.951051 | 0.754375 |
| spin | 0.002 | $3.54570\,10^{-7}$ | $3.09334\,10^{-7}$ | $8.25373\,10^{-7}$ | 0.951057 | 0.942092 |
| Weyl | 0 | $9.36261\,10^{-5}$ | $3.37363\,10^{-5}$ | $1.83368\,10^{-4}$ | 0.951052 | 0.772427 |
| Weyl | 0.002 | $3.19131\,10^{-7}$ | $2.80828\,10^{-7}$ | $7.31060\,10^{-7}$ | 0.951057 | 0.942645 |

V36 also keeps a spin exploration at $\kappa/J=0.02$ whose band width is below the estimated floating-point resolution; that row carries band_spread_resolved=false and is not used as a certified fine width or as evidence of exact degeneracy. The proof of the general theorem and the certification level of finite-precision inputs are kept apart.

#### S6.13.3 A counterexample with an actual Gauss quadratic added

The grounded three-node reduction ES2 of S8.13 gives, for $n=(m,0,q-m)$, $H_C=\tfrac12m^2-\tfrac12mq+\tfrac38q^2$. With a neutral background $B/2$ in the source and $x=q-B/2$, $y=b-B/2=x-m$, the same quadratic of strength $\eta$ is

$$
H_C^{\rm cent}=\eta\Bigl(\tfrac12m^2-\tfrac12xm+\tfrac38x^2\Bigr)=\eta\Bigl(\tfrac38m^2+\tfrac14my+\tfrac38y^2\Bigr),
\tag{B16-3}
$$

a positive electrostatic energy, not an arbitrary-sign perturbation invented for a counterexample. Adding $\eta/J=10^{-4}$ to the B15 case $B=96$, $j=32$, $D=17$ and preparing **the ground of that charged block** in each sector,

$$
\Gamma(0)=0.984756857,\qquad \max_qE_q-\min_qE_q=0.00224868846\,J,\qquad
Jt=16242.5615:\ \ \Gamma(t)=0.0126046,\ \ D_{\rm C6}(t)=0.00874789 .
\tag{B16-4}
$$

Using the bare spin width bound $3.07833\times10^{-7}J$ for the charged model is wrong (W17). This counterexample is an existence statement for a specific geometry, background, strength, preparation and time, not a no-go against all electrostatic couplings.

A $q$-wise scalar is physical too: $U(q-B/2)^2I$ leaves each block's eigenvectors and transition gaps untouched while rotating inter-sector phases. In W18 ($B=24$, $j=8$, $D=5$, $U=\pi/60$, $t=30$) $\Gamma$ drops from $0.865447$ to $0.0371319$. Subtracting each sector's ground energy separately is not a choice of common energy zero.

#### S6.13.4 A physical sufficient condition and the remaining minimal input

Write the general reduced electric energy as

$$
\tfrac12K_{RR}m^2+K_{RB}my+\tfrac12K_{BB}y^2 .
\tag{B16-5}
$$

**If** the actual $K_{RR}/2$ coincides with the $M^2$ coefficient of the original compensator shell, and that self-energy is already counted **exactly once** in $\Delta(M^2+K)$, the remaining terms are

$$
K_{RB}xy+\bigl(\tfrac12K_{BB}-K_{RB}\bigr)y^2 .
\tag{B16-6}
$$

So $K_{RB}=0$ makes the source-only parent (B16-2) a sufficient condition; this is a condition to be realised by geometry, screening, boundary reduction and the actual compensator. Adding the self-energy first and subtracting it by an arbitrary counterterm is not allowed. ES2 has $K_{RB}=\eta/4\ne0$ and falls outside the sufficient condition. **There is no derivation that S14 selects this coefficient matching or $K_{RB}=0$.**

If the actual blocks deviating from the common parent can be written $H_q^{\rm phys}=H_q+R_q$ with $r=\max_q\|R_q\|$, then for the same B15 initial state, by Duhamel,

$$
D_{\rm C6}^{\rm phys}(t)\ge\bigl[C_D(1-2p-2\varepsilon)-2|t|(\delta+r)\bigr]_+ .
\tag{B16-7}
$$

Row V38 of the inherited ledger includes cases in which **a positive lower bound actually survives** small positive $r$, and checks that the difference of the two directly evolved readouts is at most $2|t|r$. The $r$ condition is sufficient, not necessary, and not an optimal norm estimate for all geometries.

Defining per-input trace-distance errors of state preparation, bath approximation and detector as $\epsilon_{\rm prep},\epsilon_{\rm bath}(t),\epsilon_{\rm det}$, the bound above loses an additional $2[\epsilon_{\rm prep}+\epsilon_{\rm bath}(t)+\epsilon_{\rm det}]$; the flagged leakage cost of S8.17 is merged into that $\epsilon$ only under the assumptions of that section. Small errors from different time windows or different initial states are not merged into one physical certificate.


### S6.14 The finite certificates of B18 and the replacement theorems

Here $c=J/\sqrt{B(B+2)}$, and $\widetilde L$, $\pi$ are as in (3.1)–(3.2) of the main text; $\lambda_q=c\widetilde\lambda_q$, and the smallest Dirichlet eigenvalue of a proper window is positive, while for the full window it is $0$ and the inverse exit-time formula is not applied. $Z=\sum_{b=l}^u\pi_b$, $r_l=l/(B-l)$, $r_u=(B-u)/u$, $\widetilde F_l=l\pi_l/Z$, $\widetilde F_u=(B-u)\pi_u/Z$.

#### S6.14.2 The exact rational sandwich (B18-T1)

**B18-T1 [proven].** For every window $[l,u]$ with $(l,u)\ne(0,B)$, $0\le l<u\le B$ (at $(0,B)$, $\widetilde L_D=\widetilde L$ is singular),

$$
\frac1{\max_{b\in[l,u]}\widetilde u(b)}\ \le\ \widetilde\lambda\ \le\ \widetilde R[\varphi]:=
\frac{\sum_{b=l}^{u-1}(B-b)\pi_b(\varphi_b-\varphi_{b+1})^2+l\pi_l\varphi_l^2+(B-u)\pi_u\varphi_u^2}{\sum_{b=l}^u\pi_b\varphi_b^2},
\tag{B18-3}
$$

where $\widetilde u$ is the unique solution of $\widetilde L_D\widetilde u=\mathbf 1$ (the dimensionless mean exit time of the killed chain; physical time $\widetilde u/c$) and $\varphi$ is any non-zero real vector on the window. The lower bound is rational, and the Rayleigh upper bound of a rational trial vector is rational. In particular the boundary-layer trial function

$$
\varphi_b=(1-r_l^{\,b-l+1})(1-r_u^{\,u-b+1})
\tag{B18-4}
$$

is used (with the corresponding factor set to $1$ when $l=0$ or $u=B$).

*Proof.* (Lower) $\widetilde L_D$ is a non-singular M-matrix, so $\widetilde u=\widetilde L_D^{-1}\mathbf 1>0$ exists. With $g>0$ the Perron vector of $\widetilde L_D^{\mathsf T}$, $\widetilde\lambda\langle g,\widetilde u\rangle=\langle g,\widetilde L_D\widetilde u\rangle=\langle g,\mathbf 1\rangle\ge\min_b(1/\widetilde u(b))\langle g,\widetilde u\rangle$ — the Collatz–Wielandt (Barta-type) inequality. (Upper) The symmetrised $\widetilde X:=P(X/c)P$ has $\widetilde X_{bb}=B$, $\widetilde X_{b,b+1}=-\sqrt{(b+1)(B-b)}$; with $\phi_b=\sqrt{\pi_b}\varphi_b$ and $\sqrt{(b+1)(B-b)\pi_b\pi_{b+1}}=(B-b)\pi_b$, one has $\langle\phi,\widetilde X\phi\rangle=\sum_bB\pi_b\varphi_b^2-2\sum_{b<u}(B-b)\pi_b\varphi_b\varphi_{b+1}$, and rearranging with $(B-b)\pi_b=(b+1)\pi_{b+1}$ gives the numerator of (B18-3) (Dirichlet form plus the two boundary killings). Rayleigh's principle gives $\widetilde\lambda\le\widetilde R[\varphi]$. $\square$

(B15-10) is the special case $\varphi\equiv1$, giving $\widetilde\lambda\le\widetilde F_l+\widetilde F_u$. (B18-4) attaches a layer lowered by $1-r$ at each boundary; Theorem 1 of the main text proves the uniform asymptotics of the sum of the two boundary fluxes each multiplied by $(1-r)$.

**Certification (C17 of the inherited ledger).** For $(B,j)=(32,11),(64,21),(128,43),(256,85)$ and all $k=q-B/2\in[0,w]$, 84 windows in total, (B18-3) was evaluated in exact rationals and compared with the eigenvalues of 40–125-digit Sturm bisection. The minimum of lower/actual is $0.9008$ ($B=32$), $0.9342$ (64), $0.99853$ (128), $0.9999956$ (256); the maximum of upper/actual is $1.0430,\ 1.0464,\ 1.0142,\ 1.0041$. The lower bound becomes essentially exact as $B$ grows: at exponentially small $\widetilde\lambda$ the exit time is nearly exponentially distributed under the quasi-stationary law and its mean is the same from any starting point in the well.

**Range of the trial function.** (B18-3) holds for every proper window and non-zero trial vector; (B18-4) is used only where that vector is non-zero. If $l=B/2$ or $u=B/2$ makes one factor vanish identically, the harmonic $h$ of (3.4) or another non-zero vector is used instead. The finite C17 cases include the centre and are free of that issue.

#### S6.14.3 Current statements of the two-sided constants, times and parity

| earlier label | present location | repaired status |
|---|---|---|
| B18-0–B18-2 | (3.1), notation above | exact similarity; physical/dimensionless eigenvalues distinguished |
| B18-T1, B18-3–B18-4 | S6.14.2, (3.5) | exit-time/Rayleigh and the new capacity inequality used side by side |
| B18-T2, B18-5–B18-8 | Theorem 1, (3.5)–(3.16) | no general sum formula declared from a one-boundary lower bound; replaced by the compact two-boundary sum with $O(B^{-1})$; dimensional $\ln\lambda_q$ normalised to $\ln(\lambda_q/J)$ |
| B18-T3 | §3.3 and C17 | finite Sturm monotonicity cases preserved; universal finite monotonicity not claimed; proved for large $B$ under (3.11) |
| B18-T4, B18-9–B18-11 | (2.4), Theorem 2 | exact cosine sum kept; earlier finite cutoff bound kept and strengthened; small-tail sine approximation replaced by the exact $F^{-1}$ |
| B18-T5, B18-12 | (5.8) | central zero frequency, signed average, average TV and all-time floor separated |
| asymptotic comparisons V40, V41 | inherited namespace | finite tables and trends; not promoted to universal proofs or grid first-passage certificates |

The earlier finite-time upper bound is also kept explicitly: with $A(t)$ as in (4.1) and $S_{1/2}(T)=\tfrac12\sum_{|\Delta_i|T\ge2}\omega_i$, $S_{1/2}(T)\ge\ell$ implies $T_\ell\le T$; this is the special form in which each fast term of (4.3) is bounded below by $1/2$, and the main text uses the actual $1-1/(|\Delta_i|T)$, which is stronger. The broad $O(1/h)$ observation of V40 is preserved as a record and is now superseded by Theorem 10, which proves $O(B/h^2)$ with an explicit coefficient.

### S6.15 The correction of B19 and the preserved finite comparison

The current resource theorem is Section 5.3 of the main text. The decrease of the scalar $BI(h/B)$ is exact, but the actual lifetime of the same window grows as $B^2$ for sufficiently large $B$. The following finite case ($j=24$, $w=4$, $J=1$) is preserved as it stood; the decrease over the listed $B$ is not extended to all $B$.

| $B$ | $x=(j-w)/B$ | $BI(x)$ | $-\ln\max\lvert\Delta\rvert$ | $\ln T_{\rm up}(0.02)$ | $\ln t_{\rm low}(0.02)$ | $\Gamma_B$ |
|---:|---:|---:|---:|---:|---:|---:|
| 56 | 0.357 | 15.85 | 20.05 | 20.75 | 19.73 | 0.9511 |
| 64 | 0.313 | 13.48 | 17.74 | 18.44 | 17.38 | 0.9511 |
| 88 | 0.227 | 9.43 | 14.05 | 14.74 | 13.56 | 0.9511 |
| 152 | 0.132 | 5.33 | 10.90 | 11.59 | 10.17 | 0.9510 |
| 256 | 0.078 | 3.14 | 9.93 | 10.63 | 9.08 | 0.9508 |

The first-loss comparison of W21 at $B=56,152$ is a regression of this case and does not contradict the $j=2$, $w=1$ counterexample of the main text. The explicit current conclusion is that, if large sources are supplied for free, there is no universal lifetime ceiling from the compensator bandwidth $N$ alone; "the minimal source globally optimises the actual lifetime" is not among the claims of this appendix.

## S7. Conserving code, clock and readout

### S7.1 The logical code inside the optimal shell

For $d=N-L^2+1$ define the isometry

$$
\boxed{W_N:\ |m\rangle_P|a\rangle_T\mapsto|m,L^2+a-m^2\rangle_{RC},\qquad -L\le m\le L,\ 0\le a\le d-1.}
\tag{C1}
$$

All right-hand $k$ satisfy $0\le k\le N$ and distinct $(m,a)$ go to distinct vertices, so this is an isometry; $\mathcal H_P$ is the path charge index and $\mathcal H_T$ the shell clock index — **logical coordinates**.

$$
W_N^\dagger MW_N=M_P\otimes I_T,\qquad W_N^\dagger EW_N=I_P\otimes(L^2I_T+K_T),\qquad W_N^\dagger A_NW_N=A_P\otimes I_T .
\tag{C2}
$$

Hence for any clock state $\tau_T$,

$$
\rho_{RC}=W_N(|s_L\rangle\langle s_L|\otimes\tau_T)W_N^\dagger,\qquad \Gamma(\rho_{RC})=C_L,
\tag{C3}
$$

and time evolution acts on $\tau_T$ only. This is the exact representation of every state maximising the fixed positive witness; the arbitrary-phase family of (S5) is not claimed to be a product for the same fixed $W_N$.

**Physical scope.** (C1) does not replace the existing $R:C$ by new physical subsystems; in general a state of this code is entangled between the rotor and the compensator. The logical factorisation neither erases the separable cost nor constructs the physical subsystems of M56/M68.

### S7.2 Clock performance needs a task and a loss function

Restoring the energy unit $\Delta$, $H_T=\Delta K_T$ with period $2\pi/\Delta$. For a pure $|c\rangle=\sum_ac_a|a\rangle$,

$$
F_Q(t)=4\Delta^2\operatorname{Var}(a).
\tag{C4}
$$

Uniform coefficients give $\operatorname{Var}(a)=(d^2-1)/12$; the maximal QFI $F_Q^{\max}=\Delta^2(d-1)^2$ is attained by the equal superposition of the two endpoints. This optimises the **local time-estimation QFI**, not the global phase estimation with uniform prior.

Fixing the global problem as "uniform prior on $\theta=\Delta t$, loss $4\sin^2[(\widehat\theta-\theta)/2]$, ideal covariant phase POVM",

$$
\bar c=2-2\operatorname{Re}\sum_{a=0}^{d-2}c_{a+1}^*c_a,\qquad
\boxed{\bar c_{\min}=2\Bigl[1-\cos\frac\pi{d+1}\Bigr]},\qquad c_a^{\rm opt}=\sqrt{\frac2{d+1}}\sin\frac{\pi(a+1)}{d+1},
\tag{C5}
$$

the lowest eigenpair of the cost matrix $2I-S-S^\dagger$. So $\sqrt{\bar c_{\min}}\sim\pi/(d+1)$, but it is not called an unconditional "best time resolution". Bužek–Derka–Massar's equation (9) gives exactly this cost-matrix method; the finite path is re-diagonalised here rather than quoting their large-$d$ approximation as an exact finite formula. This clock optimisation is IMPORTED/SPECIALIZED (BDM (7)–(10)).

Reference-only effects commuting with $E$ are insensitive to inter-shell phases, so (C4)–(C5) speak of the time information a state can hold and of ideal measurement performance, not of what M71's original invariant readout reads. The next subsection fills that gap with an actual effect.

### S7.3 A record instrument conserving charge and energy while leaving the clock untouched

The system qubit $S$ has charge $N_S=|1\rangle\langle1|$ and zero bare Hamiltonian. On the logical $S\otimes P$ put

$$
B_R=\sum_{m=-L}^{L-1}\bigl(|0,m+1\rangle\langle1,m|+|1,m\rangle\langle0,m+1|\bigr),\qquad F_r^R=\frac{I+rB_R}2,\qquad K_r^R=\sqrt{F_r^R},\qquad r=\pm1 .
\tag{C6}
$$

Each term acts on a disjoint qubit–path doublet and $B_R=0$ on the two end singletons; so $\|B_R\|=1$, $F_+^R+F_-^R=I$, $F_r^R\ge0$. Only states of equal charge $N_S+M_P$ are connected, so $[K_r^R,N_S+M_P]=0$; by (C2) the energy acts only on the clock factor, so $K_r^R\otimes I_T$ commutes with the energy too.

With $|x\rangle_S=(|0\rangle+x|1\rangle)/\sqrt2$, $x=\pm1$,

$$
\langle B_R\rangle_{|x\rangle\otimes|s_L\rangle}=xC_L,\qquad \Pr(r\mid x)=\frac{1+rxC_L}2,\qquad D_R=C_L .
\tag{C7}
$$

From the initial $\rho_{SP}\otimes\tau_T$ the per-outcome map is $(K_r^R\rho_{SP}K_r^R)\otimes\tau_T$, so **the clock marginal conditioned on any outcome is exactly $\tau_T$**. Extending by two Kraus operators $I/\sqrt2$ outside the code gives a CP, TP instrument on the whole space commuting with the conserved quantities; the standard dilation attaching a neutral, zero-energy pointer is possible within each conserved sector.

This is an **existence construction** of an admissible instrument with explicit Kraus operators; which physical action selects this Lüders update and pointer is unproved. After one reading the path resource generally changes; the non-disturbance of the clock is not confused with free repeated use of the path reference. The Born trace rule is used.

### S7.4 A finite-reference clock readout that does not damage the record resource

For $d\ge2$, use only $a=0,1$ of the clock to prepare $|\chi_t\rangle=(|0\rangle+e^{-i\Delta t}|1\rangle)/\sqrt2$. A neutral auxiliary $B_T$ has energies $\Delta b$, $b=0,\ldots,B$, supplied in

$$
|\beta_T\rangle=\sum_{b=0}^B\beta_b|b\rangle,\qquad \beta_b=\sqrt{\frac2{B+2}}\sin\frac{\pi(b+1)}{B+2}.
\tag{C8}
$$

On $T\otimes B_T$ take the effects

$$
B_T^{\rm read}=\sum_{b=1}^B\bigl(|1,b-1\rangle\langle0,b|+{\rm h.c.}\bigr),\qquad F_\pm^T=\frac{I\pm B_T^{\rm read}}2 .
\tag{C9}
$$

$[F_\pm^T,H_T+H_{B_T}]=0$ and everything is neutral, so charge is conserved; each doublet has equal total energy. The total variation between the outcome distributions at $t=0$ and $t=\pi/\Delta$ is

$$
\boxed{D_T=\sum_{b=0}^{B-1}\beta_b\beta_{b+1}=\cos\frac\pi{B+2}.}
\tag{C10}
$$

Writing the full effects and Kraus operators as $I_P\otimes F^T$, $I_P\otimes\sqrt{F^T}$, the path state $|s_L\rangle$ is unchanged for every outcome. Tracing the auxiliary alone may change the clock state, but $R:C$ keeps the form (C3) and the subsequent M71 record performance is $C_L$; conversely, executing (C6) first leaves the clock state conditioned on that outcome unchanged, so the same binary clock reading is possible. The two readings act on different logical factors.

For $N=2$, $d=2$ and auxiliary maximal level $B=1$, $D_T=1/2$ and the record performance is $C_L=1/\sqrt2$; for $B=2,4,8$, $D_T=1/\sqrt2,\ \sqrt3/2,\ 0.9510565\ldots$ The computation is the task of distinguishing two antipodal times; no claim that the global phase cost (C5) is achieved optimally with the same auxiliary.

So to "does an additional reference for reading necessarily lower the record optimality?" this comparison class gives a **positive counterexample: it need not**. But the energy coherence of $B_T$, the charge coherence of $B_Q$ and the photon energy of a pump are three different resources; there is no theorem of free time reading without an auxiliary clock or of permanent equal performance without restoring the auxiliary after measurement. Whether the specific physical return of M68 preserves these logical factors is OPEN.

### S7.5 A ledger that does not merge different resources into one free reference

The preparation energy of (C3) is exactly

$$
\langle H_{RC}\rangle=\Delta\bigl(L^2+\operatorname{tr}(\tau_TK_T)\bigr).
\tag{C11}
$$

Unlike the clockless lowest optimal shell, the two-level $\chi_t$ carries extra mean energy $\Delta/2$; the sine clock of (C5) adds $\Delta(d-1)/2$. "Does not lower the record ceiling" and "no extra preparation resource" are different statements.

| Resource | Input made explicit in the comparison model | Not computed here |
|---|---|---|
| M71 $R:C$ | bandwidth $N$, states and phases of the curved shell, bare energy (C11) | cost, probability and time of preparing that state and entanglement in an actual field |
| charge source $B_Q$ | $B+1$ levels, uniform charge coherence, $\operatorname{Var}(Q_B)=B(B+2)/12$, declared $H_{B_Q}=0$ | the actual energy–charge relation and asymmetry supply in S14 |
| clock-reading reference $B_T$ | $B+1$ levels, coherence (C8), mean bare energy $\Delta B/2$ | preparation, post-measurement recovery, macroscopic tick amplification |
| optical pump | Fock number $n$, initial bare energy $n\omega$ | source and mode preparation, losses and dissipation of real detectors |
| neutral outcome $O$ | pointer and outcome effects with zero charge and energy | ready-state preparation, action origin of the reading axis, thermodynamics of the final medium |

These are declared bare-energy ledgers, not sums of total preparation work or Landauer costs; a full physical model with coupling energies, preparation processes and detectors is needed to compute those.


## S8. Carrier conditions and entry into the actual boundary action

### S8.1 The correct resonance gate for Dirac-type spectra

For a charge ladder $m$ with energies $\varepsilon_m$ and compensator spacing $\delta$, an actual edge requires

$$
\frac{\varepsilon_{m+1}-\varepsilon_m}\delta\in\mathbb Z,\qquad \Bigl|\frac{\varepsilon_{m+1}-\varepsilon_m}\delta\Bigr|\le N,
\tag{R1}
$$

**and a non-zero matrix element of an actual interaction connecting that charge change.** This is a local condition on each gap; a positive record does not require every gap to be the same rational multiple globally, and one edge already allows $\Gamma=1/2$ on a two-vertex path (Navascués–Popescu §3.2, resonance condition (11)).

As an exact counterexample, **assigning charge $m$ mathematically**, take $\varepsilon_m=\sqrt{m^2+16}$, $\delta=\sqrt{17}-4$, $N=1$. On the three vertices

$$
(-1,0),\quad(0,1),\quad(1,0)\qquad\text{all have}\qquad \varepsilon_m+\delta k=\sqrt{17},
\tag{R2}
$$

so a three-vertex resonant path with $\Gamma=1/\sqrt2$ exists exactly. The universal earlier claim "Dirac bands admit no exact invariant record" is retracted by this counterexample; a numerical table of rational approximations with denominators up to 50 is not a proof of irrationality and does not exclude it.

The $\delta$ of this counterexample is **an explicitly chosen value** for an existence counterexample; no claim that S14 predicts that spacing, nor that a general Dirac ladder always attains the M71 maximal length. The actual momentum $\mathbf k$ of M70 is not the electric charge label $m$; several momentum states of one species share a charge, so M70's $E(\mathbf k)=\sqrt{|\mathbf k|^2+\mu^2}$ alone cannot produce an M71 charge ladder — one needs the **bundle of conserved generator, spectrum and graded vertex**.

**Incommensurate-carrier ceiling theorem — inherited with explicit conditions.** (R2) shows that an exact record is *possible*; *how much* is a separate question. For a ladder $m\in\mathbb Z$ with energies $\varepsilon_m$ and gaps $g_m=\varepsilon_{m+1}-\varepsilon_m$, the resonance graph is still a union of paths and an edge $m$ exists at spacing $\delta$ only if $g_m/\delta\in\mathbb Z$, $|g_m/\delta|\le N$. Individual gap conditions do not imply long paths: for a common start $k_0$ over $m=a,\ldots,b$ it is necessary and sufficient (energy resonance only; the vertex is separate) that

$$
\frac{\varepsilon_m-\varepsilon_a}\delta\in\mathbb Z\ (a\le m\le b),\qquad \max_{a\le m\le b}\varepsilon_m-\min_{a\le m\le b}\varepsilon_m\le N\delta,
\tag{R1a}
$$

i.e. an integer $k_0$ with all $k_m=k_0-(\varepsilon_m-\varepsilon_a)/\delta$ in $[0,N]$. In the counterexample $\varepsilon=(0,1,2)$, $\delta=1$, $N=1$ both individual gaps are admissible but the three vertices cannot be placed together; the longest path has two vertices (W06).

> **Theorem (incommensurate ceiling).** If $\varepsilon_m=\varepsilon_{-m}$, the energies are strictly increasing for $m\ge0$, all gaps are non-zero and the nonnegative representative gaps $\{g_m:m\ge0\}$ are pairwise incommensurate ($g_m/g_{m'}\notin\mathbb Q$ for distinct $m,m'\ge0$), then for every $N\ge1$ and every $\delta>0$ a resonant path has at most three vertices and
> $$
> \Gamma\le\cos\frac\pi4=\frac1{\sqrt2},
> \tag{R3}
> $$
> with equality only for the central three-vertex path of type (R2) when $\delta\mid g_0$, $g_0/\delta\le N$. On a one-sided ladder ($m\ge0$), $\Gamma\le1/2$.

*Proof.* For a given $\delta$ at most one $m\ge0$ has $g_m/\delta\in\mathbb Z$ (two would make $g_m/g_{m'}$ rational). By symmetry $g_{-m-1}=-g_m$ its mirror edge is added. Two consecutive edges $m,m+1$ resonate simultaneously only if $|g_m|$ and $|g_{m+1}|$ are commensurate, which happens only for the mirror pair $m=-1,0$. So the maximal path is the three-vertex (R2) type with top eigenvalue $\cos(\pi/4)$; a one-sided ladder has no mirror pair and stops at two vertices, i.e. $1/2$ (the isolated-pair case of M71 T-AR). $\square$

M71 T-AR gave the exact rational/irrational-$r$ results for the rotor ($g_m=2m+1$, all integers). (R3) transports that argument to **non-rotor carriers** (EXTENDED) and bounds the exact record of incommensurate carriers by a constant **independent of the bandwidth**, in contrast with the rotor's $\Gamma\to1$. The finite-time witness T-DT is not subject to this ceiling (approximate resonance allowed).

*Irrationality certificates.* The hypothesis is verified per carrier. For $\mu=4$: $g_0=\sqrt{17}-4$, $g_1=2\sqrt5-\sqrt{17}$, $g_2=5-2\sqrt5$, $g_3=4\sqrt2-5$; for $\mu=3$: $g_0=\sqrt{10}-3$, $g_1=\sqrt{13}-\sqrt{10}$, $g_2=3\sqrt2-\sqrt{13}$, $g_3=5-3\sqrt2$. The minimal polynomials over $\mathbb Q$ of the six ratios $g_b/g_a$ have degree 4 or 8 (e.g. $g_1/g_0$ for $\mu=4$: $x^4+68x^3-130x^2-204x+9$), hence are irrational (supplementary check S3 of the earlier lineage, SymPy minimal polynomials). Incommensurability beyond the first four gaps for general $m$ remains a **hypothesis**, certifiable in finite ranges for a specific carrier by the same method. Whether the actual M70 carrier is subject to this theorem is a question that follows the generator–spectrum–vertex connection of the opening paragraph.

### S8.2 The half-line $\ell(\ell+1)$: two exact formulas depending on units

Let $\ell=0,1,\ldots$ with the charge transfer declared as $\ell\to\ell+1$. The table gives the top-space dimension of the resonance graph, not the physical existence of the interaction.

| energy / compensator spacing | maximal path parameter | top eigenspace dimension |
|---|---|---|
| $\varepsilon_\ell/\Delta=\ell(\ell+1)$, spacing $\Delta$ | $L(L+1)\le N<(L+1)(L+2)$, $r=N-L(L+1)$ | $d_{\rm half}=(r+1)+\max(0,r+1-2L)$ |
| same $\varepsilon_\ell$, spacing $2\Delta$, unit reset to $2\Delta$ | $L(L+1)/2\le N<(L+1)(L+2)/2$, $r'=N-L(L+1)/2$ | $d'_{\rm half}=(r'+1)+\max(0,r'+1-L)$ |

In both cases the maximal number of path vertices is $L+1$ and the top eigenvalue $\cos[\pi/(L+2)]$; the formulas are for $L\ge1$ with degenerate small $N$ separated by hand.

**Short derivation.** In the first unit the energy width of $a,\ldots,a+L$ is $L(L+1)+2aL$; since $0\le r\le2L+1$ the admissible starts are $a=0$ and sometimes $a=1$, giving $r+1$ and $\max(0,r+1-2L)$ energy shells. In the second unit the width is $L(L+1)/2+aL$ with $0\le r'\le L$ and the same reasoning gives the second formula. $\square$

The attached code verified the first convention; writing "renormalised to spacing $2\Delta$" while keeping the same $N$ and $\ell(\ell+1)$ does not test the second case. The $N=2,\ldots,60$ checks of both conventions are a report of an earlier version; the present verifier does not count those past rows as new executions.

### S8.3 From S14 to boundary currents and scattering coefficients

S14 v2.1 Definition 3.1′ contains the typed fermion kinetic term $\bar\psi_fi\gamma^\mu D_\mu\psi_f$, gauge kinetic terms and the specified Yukawa contraction. After electroweak symmetry breaking and the associated boundary reduction are justified, the coupling of that current to the electromagnetic field can be extracted; **but no qubit coupling of the form $Z\otimes B$ is printed there from the start.**

Writing the justified boundary-mode isometry as $W_\partial$, the first object to compute is

$$
J_\partial^a=W_\partial^\dagger\alpha^aW_\partial,\qquad H_{\rm int}\supset q\int_\partial j_\partial^aA_a ,
\tag{A3}
$$

an expression **given the projection**. The existence, normalisation and gap of boundary modes, the Gauss condition, and the effects of discarded bulk and negative-energy states are all needed together. That M67's boundary carrier is a push-forward of the bulk field does not by itself produce an independent tensor factor (M67 §22; M68 K17; E04).

The first physical computation is taken to be **scattering of an incoming photon on boundary matter** rather than vacuum spontaneous emission. Its effective photon-mode transformation coefficient is, schematically,

$$
G_{ab}(E)\sim PV_aP^\perp(E-P^\perp HP^\perp+i0)^{-1}P^\perp V_bP\ +\ \text{other time orderings and needed contact terms},
\tag{A4}
$$

with $P$ the projector of the retained matter code, $P^\perp=1-P$, $V_a$ the actual current vertex, the resolvent restricted to the complement. (A4) is not a finished formula but **the second-order scattering object to be computed**; a Ward identity is not assumed to survive keeping one time ordering or the positive band only; the intermediate states, contact terms and energy denominators must be computed exactly. Renaming M70's one-photon creation amplitude as the scattering coefficient of (A4) is forbidden.

### S8.4 A simple test that does not fit a pointer by hand

Decompose the actually computed coefficients on a two-dimensional code as

$$
G_{ab}=g^0_{ab}I+\mathbf v_{ab}\cdot\boldsymbol\sigma ,
\tag{A5}
$$

putting the real and imaginary parts of complex $\mathbf v_{ab}$ separately into a list of real vectors $\{\mathbf v_\nu\}$. A common exact QND pointer $Z_{\mathbf n}=\mathbf n\cdot\boldsymbol\sigma$ exists iff $[G_{ab},Z_{\mathbf n}]=0$ for all $a,b$ iff $\mathbf v_\nu\times\mathbf n=0$ for all $\nu$. Hence compute

$$
M_{\rm ptr}=\sum_\nu\mathbf v_\nu\mathbf v_\nu^{\mathsf T},\qquad C_{\rm ptr}=(\operatorname{tr}M_{\rm ptr})I-M_{\rm ptr},
\tag{A6}
$$

so that $\mathbf n^{\mathsf T}C_{\rm ptr}\mathbf n=\sum_\nu|\mathbf v_\nu\times\mathbf n|^2$: rank $0$ — the coefficients select no pointer; rank $1$ — one axis selected up to sign; rank $\ge2$ — no non-trivial exact QND axis commutes with all coefficients.

This is a **conditional linear-algebra diagnostic, not a novelty claim**; conditions on $H_S$, conserved quantities and grading must be checked afterwards, and only after obtaining the axis from scattering coefficients is it compared with the physical registers of M56/M60/M68. Finding a common axis in a model where $Z$ was fixed beforehand is not called a discovery. Rank $\ge2$ defeats the exact-QND route proposed here but does not make finite-time non-QND instruments impossible; such a construction must include the error of a pointer that changes during measurement.

### S8.5 An operation space that does not evade K17

In a local gauge theory $\mathcal H_S\otimes\mathcal H_R\otimes\mathcal H_F$ is not written as a starting axiom. First the constraint-satisfying observable algebra and the boundary flux sectors are specified; if needed, gauge-invariant dressed operators or neutral bilinears build the code algebra at finite regulator with explicit embedding and restriction; the centre of the spatial split is not erased arbitrarily.

When an admissible coupling and probe state are secured, the instrument structure

$$
\mathcal I_r^*(A)=(\mathrm{id}\otimes\sigma_F)\bigl[U^\dagger(A\otimes Q_r)U\bigr]
\tag{A7}
$$

can be used — an **IMPORTED** finite representation of the structure of E01/E03, where $A$ includes the operations of the reference and energy source to be kept for the next round; tracing them and multiplying a fresh state is a different physical process. The gauge invariance of $Q_r$, energy-compatible readout, actual localisation and $\sum_rQ_r=I$ are checked separately; failure, leakage and vacuum outcomes are included in $r$. The CP structure of (A7) proves neither the existence and preparation of a causal apparatus nor a unique reading basis (E01 (3.19); E03 (26)).

### S8.6 Types confirmed from the actual M70 current and the next computational object

In M70 §1.1's single-species positive-energy band,
$$
h(\mathbf k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z,\qquad P_+(\mathbf k)=\tfrac12(I+h/E),\qquad\operatorname{rank}P_+=1 .
$$
The current–photon vertex is of the form $b^\dagger_{\mathbf k-\mathbf p}b_{\mathbf k}a^\dagger_{\mathbf p,z,\lambda}$ with a spinor matrix element as coefficient. For the electric charge of one species $Q_{\rm em}=q_{\rm ch}\sum_{\mathbf k}b^\dagger_{\mathbf k}b_{\mathbf k}$,

$$
[Q_{\rm em},b^\dagger_{\mathbf p}b_{\mathbf k}]=0 .
\tag{A6a}
$$

So identifying this vertex directly with M71's "one-step electric charge shift" $[M,T]=T$ fails (C04 of the inherited ledger). This does not mean M71's abstract generator must be electric charge; choosing another conserved quantity such as momentum requires constructing that generator's spectrum, the photon's compensation and the vertex of the same map anew (M70 v1.5 §§1.1–1.2).

Also, the $P_+$ fibre at one $\mathbf k$ has rank $1$, so a two-state pointer cannot simply be put inside it. In the two-component spinor code before projection, if both $\sigma_x,\sigma_y$ currents are allowed,

$$
C_{ij}=\frac18\sum_{V=\sigma_x,\sigma_y}\operatorname{tr}\bigl([\sigma_i,V]^\dagger[\sigma_j,V]\bigr)=\operatorname{diag}(1,1,2)_{ij}
\tag{A6b}
$$

and there is no common QND axis (C05) — a check of that code and vertex class, not a no-go for every two-momentum, flavour or boundary model.

**Physical specification of $G$.** With an actual code, split $H_I=\sum_\alpha A_\alpha\otimes B_\alpha$ into Bohr-frequency components, fix a convention

$$
\Gamma_{\alpha\beta}(\omega)=\int_0^\infty ds\,e^{i\omega s}\operatorname{tr}\bigl[e^{-iH_Bs}B_\alpha^\dagger e^{iH_Bs}B_\beta\sigma_B\bigr],\qquad C_{\alpha\beta}(\omega)=\Gamma_{\alpha\beta}(\omega)+\overline{\Gamma_{\beta\alpha}(\omega)},
\tag{A6c}
$$

and confirm the weak-coupling conditions that yield a positive Kossakowski matrix. Defining the recycling coefficient matrix directly in the $q$-labelled jump basis as $C^{(a)}_{qr}$, under positive diagonals and equal rates $G^{(a)}_{qr}=C^{(a)}_{qr}/\sqrt{C^{(a)}_{qq}C^{(a)}_{rr}}$; the transposition/conjugation between $\alpha,\beta$ and $q,r$ is fixed by the chosen jump convention and checked by direct substitution. Cross-$q$ terms are not discarded because sectors are degenerate — equal-Bohr-frequency cross terms survive even in the secular theory (Trushechkin §II (4)–(6), §III B).

What is required from S14 is not an arbitrary $G$ chosen to reproduce a target $\Gamma$ but **this matrix and its error computed from boundary conditions, the actual environment state and current matrix elements**; the present computation does not replace it, and neither M67 Definition 40's required signature nor S14 Definition 3.1′ supplies these data automatically. S8.7–S8.11 repair the exact conditions of the earlier coupling class; S8.12–S8.17 compute actual coefficients and the all-outcome finite-time response in the declared boundary/electrostatic models; the values selected by the actual S14 and the common error remain separate obligations.

### S8.7 The electric-charge constraint preserved in S14: T-GRADE

The typed fermion term of S14 v2.1 Definition 3.1′ contains, after electroweak breaking, the standard QED current coupling. In Coulomb gauge the structure to be used is

$$
H=H_{\rm matter}+H_C+H_{\rm ph}-\int d^3x\,\mathbf j\cdot\mathbf A_\perp,\qquad H_C=\frac12\int d^3x\,d^3y\,\rho(x)G_C(x,y)\rho(y),
\tag{S14-1}
$$

with the boundary-condition-dependent $G_C$ a separate input, equal to $1/(4\pi|x-y|)$ only in free space. Unlike Dirac minimal coupling, the non-relativistic kinetic term produces $e^2\mathbf A^2/(2m)$; the earlier "this coefficient is also first order in the charge" was wrong. More fundamentally, **the order in the species charge $e$ and the order in the total sector label $q$ of a compressed matrix over several particles are different things.**

**T-GRADE [algebra; application of a standard principle].** Take the whole charged matter as the system and only the photons as environment, with $[H,Q_{\rm em}\otimes I]=0$, initial state $\rho\otimes\sigma_{\rm ph}$, arbitrary photon state and photon readout. Then every outcome instrument has a Kraus representation commuting with the charge and the induced channel is $U(1)_{\rm em}$-covariant.

*Proof.* $U=e^{-itH}$ commutes with $Q_{\rm em}$; after purifying the mixed photon state, the Kraus operators $K_{r\mu}$ obtained by taking matrix elements in the photon indices satisfy $[K_{r\mu},Q_{\rm em}]=0$; hence $\mathcal I_r(e^{i\theta Q}\rho e^{-i\theta Q})=e^{i\theta Q}\mathcal I_r(\rho)e^{-i\theta Q}$ for each outcome and for their sum. $\square$

When electric charge is the generator and the environment is photons only, the charge-preserving class of K1 is a consequence, not an assumption: photon states and readouts added to a charge-invariant input cannot create electric-charge asymmetry. The proof does not carry over to a channel on $R$ alone obtained by tracing a charged $B$ in $R+B$; the charged source of S6 supplies exactly that separate resource. Generators other than electric charge — the seam $Z_2$, momentum, angular momentum — need separate analysis.

**No-go gate record.** SIGN: the question was a phase selector of the electric charge of the total matter. QUANTIFIER: all photon states, times and photon readouts in the factorised-channel setting. SOURCE: charge conservation of the action and neutrality of photons. VALUE: only this route is removed; charged-matter references, other generators and the seam route remain. The evolution of a specific initially correlated state is not extended to a CP channel on arbitrary inputs. The seam obligation of D-S14-EVENT-001 is OPEN. C06 of the inherited ledger is the finite CAR/boson regression of this theorem; the general proof is the algebra above.

### S8.8 T-SHIFT and the repaired T-BLIND′: zero frequency and finite time

If, in the common level basis $v_a$ of the complete-path region, the actual compressed coupling is

$$
A_{\alpha q}=A_{\alpha*}+\alpha_\alpha qI ,
\tag{SH1}
$$

then $\langle v_b|A_{\alpha q}|v_a\rangle=\langle v_b|A_{\alpha*}|v_a\rangle$ for $a\ne b$. That is all of **T-SHIFT**, elementary algebra; when occupations, wavefunctions or boundary positions vary with $q$, (SH1) must be checked first, and the linearity of the bare QED coupling alone does not give it.

**The missing $\omega=0$.** In the Davies decomposition $A_{\alpha,0}$, $qI$ is the identity within a sector but $Q$ on the whole space. The smallest example is

$$
L_1=\sqrt\gamma\,|g\rangle\langle e|\otimes I_q,\qquad L_0=\sqrt\kappa\,I_{eg}\otimes Q,\qquad \sigma_{qr}(t)=e^{-\kappa(q-r)^2t/2}\sigma_{qr}(0):
\tag{ZF1}
$$

equal non-zero Bohr relaxation in every sector yet a lost record; in W09 with $\kappa=.4$, $t=3$, $\sigma_{01}(0)=.5$ the coherence drops to $0.2744058$. This does not assert $C(0)>0$ for the free QED vacuum; it refutes the earlier unconditional dissipator statement.

With a general zero-frequency PSD matrix $C_{\alpha\beta}(0)$ and diagonal response differences $\delta a_\alpha=a_{\alpha,a,q}-a_{\alpha,a,r}$, the real decay rate of that coherence is

$$
\kappa_{a;qr}=\tfrac12\,\delta a^\dagger C(0)\delta a\ge0 .
\tag{ZF2}
$$

So **T-BLIND′ [conditional]** guarantees record transfer by the dissipator only with a common basis, identical non-zero Bohr jumps, vanishing (ZF2) for every used coherence and absorption of the necessary downward paths at the ground; the Hamiltonian/Lamb-shift phases and transition frequencies of the full generator are checked separately. This re-applies the zero-frequency condition already noted in M69 §C.3 and is not a new general theorem.

**Markovian $C(0)=0$ does not mean exact finite-time losslessness either.** For the independent-boson comparison Hamiltonian $H_q=\sum_\nu[\nu a_\nu^\dagger a_\nu+qg_\nu(a_\nu+a_\nu^\dagger)]$ with a factorised vacuum/thermal initial state, direct displacement gives

$$
|G_{qr}(t)|=\exp\Bigl[-(q-r)^2\int_0^\infty\frac{J_d(\nu)}{\nu^2}(1-\cos\nu t)\coth\frac{\beta\nu}2\,d\nu\Bigr],
\tag{ZF3}
$$

with single-mode phase $(q^2-r^2)g^2(\nu t-\sin\nu t)/\nu^2$. For $T=0$, $J_d(\nu)=\eta\nu^3e^{-\nu/\Omega}$, the exponent integral is $\eta[\Omega^2-\Re(1/\Omega-it)^{-2}]\to\eta\Omega^2$: even at zero low-frequency Markov rate the initial dressing reduces the modulus. V20 of the inherited ledger compared a 64-dimensional oscillator exponential, the analytic displacement and a separate integral. The longitudinal coupling and initial preparation of this model are not identified with the transverse radiation of the actual S14; the source conflict with the standard independent-boson result is recorded at E19.

### S8.9 The exact scope of K5, K6 and T-ORDER, T-PARITY

**T-ORDER [operator model].** If the actual system–bath coupling operator is $\beta(q-M)^2$, the off-diagonal transition amplitude is

$$
c_q^{ba}=\langle v_b|A_*|v_a\rangle-2\beta q\langle v_b|M|v_a\rangle,\qquad a\ne b .
\tag{OR1}
$$

A polynomial of degree $k$ gives at most degree $k-1$, less if coefficients cancel. **A static $H_C$ by itself contains no bath and is not the emission jump of (OR1)**: electrostatics changes levels and states; emission is made by separately computed currents and a dynamical environment. If boundary or medium fluctuations turn the electrostatic coupling into noise, those dynamical degrees of freedom and their spectrum must be derived.

**T-PARITY.** If the reflection $M\mapsto-M$ of $H_{\rm path}$ holds and two levels have equal parity, $\langle v_b|M|v_a\rangle=0$ and the $q$-linear term of (OR1) vanishes; this protects the direct path of a symmetric initial state, not symmetry-breaking tilts, other baths or indirect cascades. The operator computations V12–V14 of the inherited ledger are inherited within that restriction.

**Normalisation separated.** $c$ is the bare compressed matrix element, $g_{q\lambda}$ the Hamiltonian matrix element with bath normalisation, $\ell_{q\lambda}^{ba}$ the chosen GKLS jump coefficient; $\gamma_q^{(a)}=\sum_{b<a,\lambda}|\ell_{q\lambda}^{ba}|^2$ is the width **summed over all admitted downward paths** — a single partial rate is never used as the total width.

**K5a [exact for the specified GKLS].** With only $L_{a\lambda}=|g\rangle\langle v_a|\otimes\operatorname{diag}_q\ell^{0a}_{q\lambda}$, common level energies, no extra dephasing and $\gamma_q^{(a)}>0$ for all used excited states, with $u_a=\langle v_a|{\rm in}\rangle$,

$$
\sigma_\infty=\Bigl[|u_0|^2\mathbf 1\mathbf 1^{\mathsf T}+\sum_{a>0}|u_a|^2G^{(a)}\Bigr]\odot\sigma,\qquad
G^{(a)}_{qr}=\frac{\sum_\lambda\ell^{0a}_{q\lambda}\overline{\ell^{0a}_{r\lambda}}}{(\gamma_q^{(a)}+\gamma_r^{(a)})/2}.
\tag{K5a}
$$

*Proof.* The excited diagonal block is $\rho_{aa;qr}(t)=|u_a|^2\sigma_{qr}e^{-(\gamma_q+\gamma_r)t/2}$ and the ground inflow is the product of the numerator coefficient with this block; integrate in time. Coherences between different initial levels do not enter the ground diagonal block in this jump class. $\square$

**K5 [exponential emission / WW / white-noise class].** Declaring normalised wavepackets $b_{q\lambda}(s)=\ell_{q\lambda}\exp[-(\gamma_q/2+i\omega_q)s]$, $s\ge0$, in a common time mode,

$$
G_{qr}=\sum_\lambda\int_0^\infty b_{q\lambda}(s)\overline{b_{r\lambda}(s)}\,ds=\widehat O_{qr}\frac{\sqrt{\gamma_q\gamma_r}}{(\gamma_q+\gamma_r)/2+i(\omega_q-\omega_r)},\qquad
\widehat O_{qr}=\frac{\sum_\lambda\ell_{q\lambda}\overline{\ell_{r\lambda}}}{\sqrt{\gamma_q\gamma_r}},
\tag{K5}
$$

exact as an integral of exponentials. A general positive-frequency bath may have memory, band edges and bound states, so the packet need not be exponential, and if the relative mode shape changes with frequency the two factors (mode, time/frequency) do not separate. The earlier V15 compared a finite band with a Lorentzian approximation and does not prove "exact Lorentz for a general single-excitation Hamiltonian".

**Order of limits.** In the strict Davies limit distinct fixed Bohr frequencies are secularly separated; a common jump with retained small detuning needs near-degenerate scaling $H=H_0+\lambda^2\delta H$, a justified coarse graining, or a declared white-noise model. W10 computes directly the different cross coherences (non-zero versus zero) given by common versus separated jumps. The earlier Liouvillian V18 is a **common-channel model**, not the strict Davies limit at fixed detuning — a correction reflecting the source conflict E18.

**K6 [absorbing downward cascade].** With non-degenerate levels, sector-common energies and no zero-frequency dephasing, define $C^{ba}_{qr}=\sum_\lambda\ell^{ba}_{q\lambda}\overline{\ell^{ba}_{r\lambda}}$ and $F_a=\int_0^\infty\rho_{aa}(t)dt$; then

$$
(F_a)_{qr}=\frac{|u_a|^2\sigma_{qr}+\sum_{a'>a}C^{aa'}_{qr}(F_{a'})_{qr}}{(\gamma_q^{(a)}+\gamma_r^{(a)})/2},\qquad
(\sigma_\infty)_{qr}=|u_0|^2\sigma_{qr}+\sum_{a>0}C^{0a}_{qr}(F_a)_{qr},
\tag{K6}
$$

the integration, from the highest level downward, of the linear ODE of the diagonal blocks. Grouped cross terms of transitions sharing a Bohr frequency flow only into coherences between different levels when levels are non-degenerate, so the diagonal cascade closes. With dark nodes or non-absorbing branches $F_a$ may diverge; then (K6) is not used and the finite-time ODE / full instrument is kept. With detuning, the channel model is specified first. The earlier $u_a^2$ is corrected to $|u_a|^2$ for complex amplitudes.


### S8.10 T-TILT: ground phases, the bright condition and the dark counterexample

Keep first the earlier comparison Hamiltonian $H_q=H_{\rm path}+U(q-M)^2$. For a finite range of $q$, non-degenerate parity levels and a positive fixed gap,

$$
E_{qa}=E_a+U[q^2+\langle M^2\rangle_a]+O(U^2),\qquad \Delta_q:=E_{q+1,0}-E_{q,0}=U(2q+1)+O(U^2),
\tag{T1}
$$
$$
E^{(2)}_{q0}=-U^2\sum_{a>0}\frac{|\langle v_a|(q-M)^2|s\rangle|^2}{E_a-E_0},\qquad \omega_{qa}-\omega_{ra}=O(U^2),
\tag{T2}
$$

because $\langle M\rangle_a=0$ and $Uq^2$ is common to all levels and cancels in transition energies. Vectors tilt by $O(U)$ and the actual ground overlap weights change. With the adjacent-coherence convention $\sigma_{q,q+1}$ the free phase is $e^{+i\Delta_qt}$; using only the $U(2q+1)$ approximation, $|\sum_q\sigma_{q,q+1}e^{i\Delta_qt}|$ revives at $\pi/U$; a perfect revival of the exact spectrum is not claimed.

**Bright version.** Assuming in addition $\inf\gamma_q(0)>0$ on the used transitions, smooth amplitudes and a common $U=0$ mode, the normalised mode loss is $O(U^2)$, the rate-mismatch factor $1-O((\delta\gamma/\gamma)^2)=1-O(U^2)$ and the frequency factor $1-O((\delta\omega/\gamma)^2)=1-O(U^4)$; so $1-|G|=O(U^2)$ in K5. The constants depend on the rate lower bound and the fixed sector range; smallness of $Uq^2$ alone does not make the result uniform.

**W12 [an explicit dark boundary].** In the $j=1$ Gauss model of S8.13 with $\eta_C=\eta\to0$, dipole $M$, transition $a=2\to0$: expanding the normalised eigenvectors to second order,

$$
d_{02}(q,\eta)=\pm q\eta^2/4+O(\eta^3),\qquad \gamma_{20}(q,\eta)=O(q^2\eta^4),\qquad \omega_{q,20}-\omega_{r,20}=O(\eta^2).
\tag{T3}
$$

The first-order dipole coefficient is exactly $0$. The same second-order transition energy is $\omega_{q,20}=\sqrt2+\sqrt2(4q^2+1)\eta^2/16+O(\eta^3)$, so the $q=1,2$ difference has the non-zero coefficient $3\sqrt2/4$, also checked symbolically. **In the WW counterexample using this partial rate as the full width, a spectrum blocking $\nu<1.1$ is declared separately**: at the small $\eta$ used, the competing $2\to1$ transition at about $.707$ is blocked and $2\to0$ at about $1.414$ is allowed; without that filter, in a three-level dipole bath $\gamma_{20}$ cannot serve as the full lifetime. Exact dynamics with a band edge is not claimed to equal WW.

In this restricted WW class the rate ratio of $q=1,2$ tends to $1:4$ and the time overlap to $2\sqrt{1\cdot4}/5=.8$; including detuning, $\delta\omega/\gamma\sim\eta^{-2}$ so the overlap tends to $0$. From $\eta=.002$ to $.001$ the rate reduction ratio is about $16$ and the transition-frequency difference goes from $4.24\times10^{-6}$ to $1.06\times10^{-6}$. This excludes "for small $U$ the long-time kernel loss is always $O(U^2)$"; at fixed finite time the emission probability itself vanishes, so there is no contradiction.

**Failure path preserved.** The first exploration expected $\gamma=O(\eta^2)$; the halving ratio came out $16$ rather than $4$ and was rejected; the second-order eigenvector computation then confirmed (T3). No tolerance was changed afterwards to manufacture a PASS. The source comparison also found a possible omission of competing transitions, which led to the filter condition above.

The earlier draft $U(2q+1)\ll\gamma$ that placed the ground splitting into transition frequencies stays retracted; V16/W07 (ground splitting, non-monotone ceiling, approximate revival) and V18 (bright common-channel comparison) are kept within their ranges. In actual electrostatics the full capacitance of S8.13 must be computed before a single $UQ_B^2$, without double-counting the charging energy already in the rotor.

**Relation to B14.** The structure of (T1)–(T2) — sector splitting $U(2q+1)$, revival $\pi/U$, transition-frequency differences $O(U^2)$ — is confined to **an additive term common to all levels**. The su(2) source of S6.11 creates the same parabolic splitting without an additive term, through the hopping amplitudes, with $U_{\rm eff}=2JC_j/[B(B+2)]$ centred at $B/2$, but with level-dependent coefficients $\cos[a\pi/(P+1)]$, so its transition-frequency differences are first order (B14-T6). The revival $\pi/U$ of W07 and $T_{\rm rev}=\pi/U_{\rm eff}$ of B14-T5 have the same form. An explicit $H_C$+spin model with both origins is computed in S6.13 and S8.18; which coupling S14 supplies remains open. Since the $U(2q+1)$ splitting of T-TILT is the standard charging-energy dispersion of a charge qubit/finite island (E26), it is reclassified IMPORTED in Section 12.

### S8.11 The reading instrument: vertex-commutant theorem, sign reading, QND axis (T-VERTEX, W08, V17)

**Theorem T-VERTEX.** For a code operator $B$ (e.g. $B_R$ of C6) and a probe operator $V$ with vertex $H_I=B\otimes V$ and $[H_{\rm code},B]=0$, the Kraus operators of the instrument produced by any probe state and any probe readout lie in the commutative algebra $\mathcal C$ generated by $B$ and $H_{\rm code}$; hence the instrument preserves the spectral blocks of $B$: $\mathcal I_r(P_\lambda\rho P_\mu)=P_\lambda\mathcal I_r(\rho)P_\mu$. Conversely, the charge-dephasing alternative $\mathcal J_r$ of S11.1 does not preserve the blocks (exact rational witness C07), so **it arises from no vertex of the form $B_R\otimes V$ with any probe state or readout.**

*Proof.* With $H=H_{\rm code}\otimes I+B\otimes V+I\otimes H_{\rm probe}$, $U=\sum_{\lambda,\epsilon}P_\lambda\Pi_\epsilon\otimes e^{-it(\epsilon+\lambda V+H_{\rm probe})}$, so $K_r=\langle r|U|{\rm probe}\rangle=\sum f_{r\lambda\epsilon}P_\lambda\Pi_\epsilon\in\mathcal C$; the unitary freedom of Kraus representations stays in $\mathcal C$; block preservation follows since elements of $\mathcal C$ commute with $P_\lambda$. The charge projections $\Pi_m$ do not commute with $B_R$, so the failure of block preservation for $\mathcal J_r$ is the computation C07. $\square$

For C6, $B_R^3=B_R$ (symbolically certified), so the vertex with a single-mode swap $X$ on a pure single-photon probe gives exactly $K_a=-i\sin\theta\,B_R$, $K_c=I-(1-\cos\theta)B_R^2$ (exponential and polynomial agree to zero error), and $\sqrt{F_+}=P_{+1}+P_0/\sqrt2$ exactly. The theorem proves **one direction**: a $B_R\otimes V$ vertex implies an instrument in the $B_R$-block-preserving class; that class contains the Lüders instrument but not only it (mixed probe states give non-Lüders instruments in the same class). The converse and "charge-dephasing instruments come from Coulomb coupling" are not proved; the latter is a hypothesis. The theorem restricts the class an admissible vertex can produce; actual selection needs the whole coupling matrix, probe state, interaction time and readout, and cannot be reduced to a single $U/\gamma$ ratio. There is no evidence yet that $B_R\otimes V$ is the natural unique form of actual S14 transverse radiation, and the static Coulomb term is not claimed to be a charge-dephasing instrument.

**W08 — the sign is not read by a single-mode number probe.** With one photon in the vertex above and counting only mode $a$, the effect is $F_a=\sin^2\theta\,B_R^2$, blind to $B_R=\pm1$; the contrast of $|\pm x\rangle\otimes|s_L\rangle$ inputs is exactly $0$. Reading the sign needs a **phase reference**. Adding the common channel $g_0(c^\dagger a+{\rm h.c.})\otimes I$ of S9.2 in the balanced model ($g_0=g_1$, $Gt=\pi/2$) and counting the ports $(a\pm b)/\sqrt2$ restores the contrast $C_L=1/\sqrt2$ ($N=1$; sufficiency witness). A phase-carrying probe state (e.g. $(|0\rangle+i|1\rangle)/\sqrt2$) with a phase-sensitive coupling/readout is another option, so the common channel is not the unique method. The $g_0$ channel of (A9) is not decoration but an optical form of phase reference, and reading a non-commuting record with a charge-conserving pointer costs such a resource (consistent with E06).

**V17 — the second-order transfer tensor and the origin of the QND axis.** For a vertex $\sum_i\sum_x\lambda_{ix}|e_i\rangle\langle\sigma_i|x+{\rm h.c.}$ in which each excited level $e_i$ attaches to one register state (single photon, detuning $\delta_i$), the exact diagonalisation of the low-energy block agrees with the Schrieffer–Wolff leading term

$$
G_{xx'}=-\sum_i\frac{\overline{\lambda_{ix}}\lambda_{ix'}}{\delta_i}|\sigma_i\rangle\langle\sigma_i|
\tag{A9a}
$$

to within $15\%$ (three samples, relative error $\le1.1\%$), and $G_{xx'}$ is diagonal in the register basis; so the rank of $M_{\rm ptr}$ in (A6) is $1$ and the QND axis is fixed by the **level-attachment structure**. The $(g_0,g_1)$ of (A9) are (sum, difference)/2 of the dipole products of the two branches, and balance $g_0=g_1$ is the symmetric condition that one branch does not couple to that channel. If one excited level couples to both register states, rank $\ge2$ is possible; the control case used has rank $3$ and no exact QND axis. No universal claim that every mixed vertex has rank $\ge2$. This applies the diagnostic of S8.4 to an actual second-order object; which level structure emerges from the S14 boundary code is OPEN.

**What remains.** Closed here: "a $B_R\otimes V$ vertex puts the instrument in the $B_R$-block-preserving class" and "a single-mode number probe cannot read the sign; a phase reference is needed". Not closed: constructing C6 itself as the actual vertex of the S14 boundary code; the probe state (the preparation/selection of the initial photon state, vacuum included, is an apparatus/boundary input); the readout port; and the origin of the single outcome and Born weights. (T1) of T★ is still OPEN.

### S8.12 From the boundary current to the required complex spectral data

For M70's declared positive Dirac band $h(k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z$, $M>0$, $E_k=\sqrt{k^2+M^2}$,

$$
u(k)=\frac{(E_k+M,\ k_x+ik_y)^{\mathsf T}}{\sqrt{2E_k(E_k+M)}},\qquad \rho_\perp(y)=ae^{-ay}\ (y\ge0),\qquad F(z)=\frac a{a-iz},
\tag{BC1}
$$

with $u^\dagger u=1$, $\int\rho_\perp dy=1$. Keeping M70's normalisation, the photon-creation current amplitude is

$$
g_{k,p,z,\lambda}=\frac{eF(z)}{\sqrt{2(2\pi)^3\omega}}\,u(k-p)^\dagger(\epsilon^*_{\lambda x}\sigma_x+\epsilon^*_{\lambda y}\sigma_y)u(k),\qquad \omega=\sqrt{p^2+z^2}.
\tag{BC2}
$$

Occupation, final matter state and boundary modes must be attached before this is an actual transition amplitude; $b^\dagger_{k-p}b_k$ has electric-charge grade $0$ within one species, and relabelling momentum as the electric sector $q$ contradicts T-GRADE.

**Independent check.** Sandwiching $h(k)-h(k-p)=p_x\sigma_x+p_y\sigma_y$ with eigenvectors,

$$
(E_k-E_{k-p})\,u(k-p)^\dagger u(k)=p_a\,u(k-p)^\dagger\sigma_au(k).
\tag{BC3}
$$

C10 is the matrix identity, V19 compares spinor/projector tensors and normal integrals on 16 declared samples — a continuity check of this band, not a proof of full-QED Ward renormalisation. M70's exclusion of static intraband emission (S9.1) stands; the confined transition model below is an explicit comparison with different assumptions.

**Why the diagonal spectrum is not enough.** Fix the common basis of the actual per-sector initial/final codes and the environment and compute

$$
g^{ba}_{q\lambda}=\langle b,q;1_\lambda|H_I|a,q;0\rangle,\qquad
\mathcal J^{ba,b'a'}_{qr}(\nu)=\sum_\lambda g^{ba}_{q\lambda}\overline{g^{b'a'}_{r\lambda}}\,\delta(\nu-\nu_\lambda),
\tag{BC4}
$$

including any unobserved final-matter label in $\lambda$ or its overlap. The diagonal $\mathcal J_{qq}$ fixes inclusive emission rates but not the cross complex phases; assembling a Gram from scalar rates computed in different sectors loses the environment distinguishability.

With a chosen macroscopic boundary the computation can also be written as a contraction of the current with the electromagnetic Green tensor; the dipole-limit $\Gamma=(2\mu_0/\hbar)\omega^2d\cdot\Im G\cdot d^*$ is an imported standard formula, with E17 confirming its Markov assumptions. The Green tensor, current normalisation, occupation and recoil are not values fixed by S14 here.

### S8.13 The exact finite reduction of Gauss's law and the order of projection

**C08 [finite-regulator construction].** For four electric-field variables joining three interior points and grounded ends,

$$
D=\begin{pmatrix}1&-1&0&0\\0&1&-1&0\\0&0&1&-1\end{pmatrix},\qquad L=DD^{\mathsf T},\qquad L^{-1}=\frac14\begin{pmatrix}3&2&1\\2&4&2\\1&2&3\end{pmatrix}.
\tag{ES1}
$$

Minimising $\tfrac12E^{\mathsf T}E$ under the Gauss constraint $DE=n$ gives $E_*=D^{\mathsf T}L^{-1}n$ with energy $\tfrac12n^{\mathsf T}L^{-1}n$; any solution is $E_*+z(1,1,1,1)$ with energy increased by $2z^2$. For $n=(m,0,q-m)^{\mathsf T}$,

$$
H_C(m,q)=\tfrac12m^2-\tfrac12mq+\tfrac38q^2 .
\tag{ES2}
$$

This is a **non-compact electrostatic regulator**; it does not construct the integer electric-link spectrum of compact $U(1)$ or a tensor factorisation of the full Gauss physical Hilbert space, and it does not close K17.

For general normalised source profiles $f_R,f_B$, $K_{ij}=e^2f_i^{\mathsf T}L^{-1}f_j$ and

$$
H_C=\tfrac12K_{RR}M^2+K_{RB}M(q-M)+\tfrac12K_{BB}(q-M)^2 ,
\tag{ES3}
$$

so knowing $U=K_{BB}/2$ does not fix the Hamiltonian; the mutual term, the rotor self-energy and the origin of the existing $\Delta M^2$ must be matched together. A continuum grounded Green function has the same quadratic structure but needs UV regulation and self-energy subtraction.

**C09 [upstream reuse].** Under a general boundary projection

$$
P\rho(x)\rho(y)P=P\rho(x)P\rho(y)P+P\rho(x)Q\rho(y)P,\qquad Q=I-P,
\tag{ES4}
$$

the formula of M69 §C.4; squaring the compressed density first misses the last term, which for the square of a Hermitian density is $(Q\rho P)^\dagger(Q\rho P)\ge0$ and is non-zero in the exact rational matrix of C09. The finite model below has a diagonal code density defined from the start, so it does not hide this omission; an actual field reduction must compute or bound the (ES4) term and the leakage.

### S8.14 $U,\omega,d,\gamma$ from one Gauss model, and a restricted self-energy

**Declared inputs.** $j=1$, $B=4$, $m=-1,0,1$, $q=1,2,3$, $J=1$, $\eta_C=.04$, $e\times{\rm length}=1$, dimensionless comparison units $\hbar=c=\epsilon_0=1$; $\eta_C$ multiplies the electrostatic kernel of (ES1); the in-shell $\Delta E$ is subtracted as a constant; hopping $-J(S+S^\dagger)/2$ plus this electrostatic term. No claim that this is the actual rotor self-energy decomposition of S14.

$$
H_q=-\tfrac12(S+S^\dagger)+.02M^2-.02qM+.015q^2I,\qquad K_{RR}=K_{BB}=.03,\quad K_{RB}=.01,\quad U=.015 .
\tag{MIC1}
$$

Declaring the profile centres $x_B=0$, $e(x_R-x_B)=1$, the dipole of the density is $e[x_RM+x_B(q-M)]=M$; so $D_{\rm dip}=M$ and the current is $I=i[H_q,D_{\rm dip}]$; one common position axis, with the photon polarisation contracted against that dipole. These position/length inputs are not S14 choices. Eigenvector phases follow the real positive-pivot convention of the verifier, and the initial sector coherence is supplied in the same convention. Then

$$
I^{ba}_q=-i\omega^{ab}_qd^{ba}_q,\qquad d^{ba}_q=\langle v_{bq}|D_{\rm dip}|v_{aq}\rangle,\qquad \omega^{ab}_q=E_{aq}-E_{bq}.
\tag{MIC2}
$$

**Declared radiation model.** A free-space dipole angular integral with a UV form factor,

$$
\mathcal J_{\rm env}(\nu)=\frac{\nu^3e^{-\nu/\Omega}}{6\pi^2},\quad\Omega=2,\qquad
\gamma_q^{a\to b}=2\pi|d_q^{ba}|^2\mathcal J_{\rm env}(\omega_q^{ab})=\frac{(\omega_q^{ab})^3|d_q^{ba}|^2e^{-\omega_q^{ab}/2}}{3\pi},
\tag{MIC3}
$$

with $\int d\Omega_{\mathbf n}[1-(\widehat d\cdot\mathbf n)^2]=8\pi/3$ checked by separate quadrature. (MIC3) is the prior weak-coupling on-shell rate and does not replace exact finite-time populations; it is a normalised comparison specialisation of the standard dipole formula (E17).

| $q$ | $E_{\rm ground}$ | $\omega_{10}$ | $d_{01}$ | $\gamma_{10}$ | $\omega_{20}$ | $d_{02}$ | $\gamma_{20}$ (partial) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | −0.68245237 | 0.71743638 | 0.70183004 | 0.01348198 | 1.41492072 | 0.00039932 | 2.362230e−08 |
| 2 | −0.63827639 | 0.71821260 | 0.70105335 | 0.01349063 | 1.41661658 | 0.00079482 | 9.384495e−08 |
| 3 | −0.56464777 | 0.71950480 | 0.69976431 | 0.01350501 | 1.41943850 | 0.00118278 | 2.087643e−07 |

$\gamma_{20}$ is a partial rate; in a general three-level bath the total $a=2$ width adds $2\to1$. S8.15 chooses the $1\to0$ single-excitation submodel from the start; only the dark witness of S8.10 uses a separate filter.

**RWA self-energy from the same data.** For the single $1\to0$ star, the second-order on-shell real shift with zero counterterm is

$$
\delta\omega_q^{(2)}=\frac{|d_q^{01}|^2}{6\pi^2}\,{\rm PV}\int_0^\infty\frac{\nu^3e^{-\nu/\Omega}}{\omega_q-\nu}\,d\nu,
\tag{LS1}
$$
$$
{\rm PV}\int_0^\infty\frac{\nu^3e^{-\nu/\Omega}}{\omega-\nu}d\nu=-2\Omega^3-\omega\Omega^2-\omega^2\Omega+\omega^3e^{-\omega/\Omega}\operatorname{Ei}(\omega/\Omega),
\tag{LS2}
$$

by polynomial division and ${\rm PV}\int e^{-\nu/\Omega}/(\nu-\omega)d\nu=-e^{-\omega/\Omega}\operatorname{Ei}(\omega/\Omega)$, compared with Cauchy-weight quadrature (V23 of the inherited ledger). At $q=1$: about $-.165636$ for $\Omega=2$ and $-1.17974$ for $\Omega=4$; the latter exceeds the bare gap $\approx.717$ and cannot be used as an exact small-perturbation pole prediction. These are **regulator-dependent second-order coefficients**, not the renormalised QED Lamb shift; counter-rotating terms, other levels and mass/boundary renormalisation are OPEN, and (LS1) is not fed back into the Hamiltonian when solving the exact star.

**W13: the same rate does not fix the shift.** Adding $\delta J(\nu)=\varepsilon(\nu-\omega)^2\nu e^{-\nu/\Omega}\ge0$ leaves the on-shell density unchanged but changes the PV by $-\varepsilon(2\Omega^3-\omega\Omega^2)$, e.g. $-.396$ at $\omega=.7$, $\Omega=2$, $\varepsilon=.03$. Off-shell bath data are needed; rates alone cannot substitute for all underived values.

### S8.15 Direct finite-time computation preserving memory and the no-photon outcome

In a common environment mode space per sector define

$$
H_q^{(1)}=E_{q0}I+\omega_q|e\rangle\langle e|+\sum_\lambda\nu_\lambda|\lambda\rangle\langle\lambda|+\sum_\lambda\bigl(g_{q\lambda}|\lambda\rangle\langle e|+\overline g_{q\lambda}|e\rangle\langle\lambda|\bigr).
\tag{FT4}
$$

From the initial $|e\rangle$, $a_q,b_{q\lambda}$ are the first column of the full exponential $e^{-itH_q^{(1)}}$. The physical initial embedding $\sum_qc_q|v_{1q},q\rangle$ is a **supplied preparation input**; the $q$-dependent excited vectors and energies are not prepared free by the action, and they differ from the initial $|m=0\rangle$ of S6; their preparation, switching and phase remain an open obligation. If $E_{q0}$ was subtracted, the **sector-dependent $e^{-iE_{q0}t}$** must be restored at the end; the physical comparison of overlaps at equal environment label is not replaced by arbitrary rephasing.

The amplitude with the ground phase removed satisfies

$$
\dot{\widetilde a}_q(t)=-i\omega_q\widetilde a_q(t)-\int_0^tK_q(t-s)\widetilde a_q(s)\,ds,\qquad K_q(\tau)=\sum_\lambda|g_{q\lambda}|^2e^{-i\nu_\lambda\tau},
\tag{FT5}
$$
$$
\widetilde b_{q\lambda}(t)=-ig_{q\lambda}\int_0^te^{-i\nu_\lambda(t-s)}\widetilde a_q(s)\,ds,
\tag{FT6}
$$

exact after integrating the bath variables of the component Schrödinger equation. Also

$$
P(z-H)^{-1}P=\bigl[z-PHP-PHQ(z-QHQ)^{-1}QHP\bigr]^{-1},
\tag{FT7}
$$

so rate, shift and memory are different approximations of one resolvent; (FT7) is the imported Feshbach–Schur theorem with a rational sub-check (C11). Separate $\gamma,\delta\omega$ are not tuned independently of the cutoff and initial state.

**Actual finite computation.** $N_{\rm mode}=192$, $\nu_k=(k+.5)8/192$, $\Delta\nu=8/192$, $g_{qk}=d_q^{01}\sqrt{\mathcal J_{\rm env}(\nu_k)\Delta\nu}$, $T=8$; this mode set is itself the declared model, without certification of the continuum discretisation error. V24 of the inherited ledger compares Hermitian diagonalisation with a separate DOP853 component ODE. About $85.5\%$ of the excited population remains, so neither complete cooling nor $t=\infty$ is claimed.

**All-outcome instrument.** The isometry (FT0) sends the logical input $q$ to the matter output $(q,e/g)$ and the photon number; reading it,

$$
K_0=\sum_qa_q|e,q\rangle\langle q|,\qquad K_\lambda=\sum_qb_{q\lambda}|g,q\rangle\langle q|,\qquad K_0^\dagger K_0+\sum_\lambda K_\lambda^\dagger K_\lambda=I .
\tag{FT8}
$$

Discarding the logical excitation label gives the Schur channel (FT1); keeping only the ground-photon branch is a trace-non-increasing map with $R_{qq}=1-|a_q|^2$. "Success, so renormalise each sector" is not the original instrument and does not remove the re-preparation cost of the discarded excited state. V25 compares the partial trace of the full isometry with the Kraus sum directly.

### S8.16 The finite-time actual record combination and conditional certified numbers

The ground embedding is $|g_q\rangle=\sum_ms_{mq}|m,j^2-m^2,q-m\rangle$. From the initial $\sigma$ and the photon Gram $R$, the physical $RC$ adjacent element of the success branch is

$$
(\rho_{RC,g})_{m,m+1}=\sum_qs_{mq}\overline{s_{m+1,q+1}}R_{q,q+1}\sigma_{q,q+1},
\tag{REC1}
$$

so with $w_q=\sum_ms_{mq}\overline{s_{m+1,q+1}}$ and $z_g=\sum_qw_qR_{q,q+1}\sigma_{q,q+1}$,

$$
\Gamma_g=\sum_m|(\rho_{RC,g})_{m,m+1}|\ \ge\ |z_g| .
\tag{REC2}
$$

A single-global-phase C6 readout gives $|\Re(e^{i\phi}z_g)|$, optimised to $|z_g|$; for general $q$-dependent ground vectors this need not equal $\Gamma_g$, and the resource that aligns this image with the source/clock/probe reference that created it is required.

With the sine source $s_3=(1/2,1/\sqrt2,1/2)$, $\sigma=s_3s_3^{\mathsf T}$ and (FT4), V27 obtains

$$
w=(.71620994,.71511840),\qquad z_g=.0647646890+.0334077824i,\qquad |z_g|=.0728734854,\qquad \Gamma_g=.0728735862 .
\tag{REC3}
$$

Keeping both success and no-success flags, and giving the no-success branch the same inconclusive output, this is the phase-optimal contrast of the **entire procedure**; nothing is divided by a success probability. For the same reason the finite photon amplification of S9 is attached together with its success flag and pump budget.

As an illustration, **additionally assuming** the error envelope $T=8$, $b=.001$, $\delta_H=.0001$ for both inputs, S8.17 gives $\epsilon_\pm=T\delta_H+(bT)^2=.000864$ and the lower bound (FT3) $.0711454854>0$. $b,\delta_H$ are not S14 estimates; the number is a conditional target ("secure this common bound and the record of this model is certified"), not a certification of a full S14 record.

### S8.17 Leakage and model error in a common time window: proof and remaining conditions

**T-FLAG [conditional mathematics].** For bounded self-adjoint $H$, orthogonal projections $P$, $Q=I-P$, $A=PHP$, $B=QHP$, $D=QHQ$, $b=\|B\|$, with input supported in $P$, and outputs that distinguish $P/Q$ by an orthogonal flag without reading their coherence, the error between the full flagged evolution and $e^{-itA}$ in trace distance $\tfrac12\|\cdot\|_1$ with arbitrary ancillas is

$$
\epsilon_{\rm leak}(t)\le\min\{1,b^2t^2\}.
\tag{ERR1}
$$

*Proof.* With $U=e^{-itH}$, $K=PUP$, $R=QUP$, $V=e^{-itA}$, variation of constants gives $R(t)=-i\int_0^te^{-iD(t-s)}BK(s)ds$, $\|R(t)\|\le bt$, and $K(t)-V(t)=-i\int_0^te^{-iA(t-s)}B^\dagger R(s)ds$, $\|K-V\|\le b^2t^2/2$. The flagged output difference is the direct sum of the retained block $K\rho K^\dagger-V\rho V^\dagger$ and the leakage block $R\rho R^\dagger$; the trace norm of the first is at most $2\|K-V\|$ and the trace of the second at most $\|R\|^2$, so half the sum is at most $b^2t^2$; tensoring $I_{\rm anc}$ keeps the norms, and trace distances are at most $1$. $\square$

The four entangled-input examples of V26 (inherited) are sub-checks; the Duhamel lineage of this bound was compared with E21 and it is not claimed as a new general theorem. **W11**: for $H=b\sigma_x$, $\rho=|0\rangle\langle0|$, the full trace distance reading coherence is $|\sin bt|=O(bt)$, while the flagged reading is $\sin^2bt=O(b^2t^2)$; the output hypothesis cannot be dropped.

With the difference between the actual generator embedded in the same retained space and the computational model, $\delta_H(s)=\|A-H_{\rm model}(s)\|$, and input, bath-replacement and detector errors in the same trace distance, contractivity and the triangle inequality give

$$
\epsilon_\pm(T)\le\min\Bigl\{1,\ \epsilon_{{\rm in},\pm}+b^2T^2+\int_0^T\delta_H(s)ds+\epsilon_{{\rm bath},\pm}+\epsilon_{{\rm det},\pm}\Bigr\}.
\tag{ERR2}
$$

The reverse triangle inequality yields (FT3) for the contrast of two inputs through the same output flag. Summing several omitted interactions, $b=\|Q(H_1+H_2+\cdots)P\|\le\sum_i\|QH_iP\|$ — projection, bulk and Coulomb are not set to zero individually and then added; external switching enters $H(t)$ and the energy/clock ledger with the integral bound over that time.

**Unclosed range.** Full QFT usually has infinite operator norms; moving a finite regulator to the physical continuum needs energy-constrained/state-dependent regularity and cutoff errors, and whether the actual apparatus implements the $P/Q$ flag is a separate condition. This subsection advances from "common error only defined" to "a computable sufficient formula proved for bounded, flagged cases"; since no same-$T$ numbers are supplied for the actual occupied packet, recoil, bulk, boundary projection and Coulomb, D-M69-MOVING stays OPEN.


### S8.18 B17 — the source type of M70 and cooling computed in the same block

#### S8.18.1 CAR and CCR, global and regional charge

The conditional emission vertex of M70 v1.5 §§1.1–1.2, re-read for this work, uses the fermion bilinear $b^\dagger_{k-p}b_k$ of the occupied positive Dirac band and a photon creator, in the static, one-photon, specified-occupation and boundary-form-factor scope. One may call that operator a "two-mode number-conserving transfer", but that phrase alone does not give the arbitrary $S=B/2$ representation of B14.

For one pair of CAR modes $f_1,f_2$ with

$$
S_+=f_1^\dagger f_2,\qquad S_-=f_2^\dagger f_1,\qquad S_z=(n_1-n_2)/2,
\tag{B17-0}
$$

$[S_+,S_-]=2S_z$, but on the full four-dimensional Fock space

$$
S^2=0\oplus\tfrac34I_2\oplus0 :
\tag{B17-1}
$$

the empty and doubly occupied states are singlets and only the singly occupied subspace is spin $1/2$ (C16 checks this with the exact $4\times4$ matrices including Jordan–Wigner signs). Adding several pairs allows representations containing large spins, but the occupation of each pair and the preparation of the maximal-spin symmetric subspace are additional conditions.

Two **bosonic CCR** modes at fixed $n_1+n_2=B$ give, by the Schwinger representation, spin $B/2$ with transfer elements $\sqrt{(b+1)(B-b)}$ — an algebraic conditional derivation, not a map turning M70's CAR state into that CCR state.

Also

$$
[n_1+n_2,f_1^\dagger f_2]=0,\qquad [n_1,f_1^\dagger f_2]=f_1^\dagger f_2 ,
\tag{B17-2}
$$

neutral for the global electric charge and of grade $1$ for the regional occupation. How $Q_B$ is read as a regional, collective or boundary charge and how it is tied to $M$ must be specified together with the actual Gauss subsystem; the obligations of T-GRADE and K17/K18 are not evaded by renaming a regional charge. The flat $L_B$ is also a proper $U(1)$ tensor with $[Q_B,L_B]=-L_B$; what B14-L1 proves is that for $B\ge3$ it is **not a scalar su(2) lowering operator**.

#### S8.18.2 Actual gap, dipole and rate

With $|g_q\rangle,|e_q\rangle$ the ground and first excited states of each $H_q$ and energies $E_{gq},E_{eq}$,

$$
\omega_q=E_{eq}-E_{gq},\qquad d_q=\langle g_q|M|e_q\rangle,\qquad \gamma_q=\frac{\omega_q^3|d_q|^2}{3\pi}e^{-\omega_q/\Lambda_{\rm UV}} ,
\tag{B17-3}
$$

the last being the declared dipole/unit/cutoff model MIC3 of S8.14 with $J=1$, $\Lambda_{\rm UV}=2$ in the tables. Charge and space units and the mode form factor were chosen separately, so no SI lifetime or S14 emission rate is predicted. Eigenvector phases are fixed so that each $d_q\ge0$.

For the full spin parent itself,

$$
\omega=\frac{2J}{\sqrt{B(B+2)}},\qquad |\langle g|M|e\rangle|^2=B/4,\qquad \gamma\sim\frac{2J^3}{3\pi B^2},
\tag{B17-4}
$$

the first from the $S_x$ spectrum and the second from the adjacent matrix element of $S_z$ in the $S_x$ quantisation axis — exact identities and asymptotics of the full parent, not a general theorem that cooling completes uniformly at this rate in every truncated $H_q$.

V37 diagonalised the actual truncated blocks at $B=96$, $j=32$, $D=17$:

| electrostatic $\eta/J$ | range of $\omega_q/J$ | range of $\lvert d_q\rvert^2$ | range of $\gamma_q$ (declared units) | max adjacent $\omega$ difference$/J$ |
|---|---|---|---|---:|
| 0 | 0.0206197–0.0206209 | 23.9986–24.0000 | $2.20956\,10^{-5}$–$2.20982\,10^{-5}$ | $7.84089\,10^{-7}$ |
| $10^{-4}$ | 0.0228738–0.0228760 | 21.6289–21.6337 | $2.71585\,10^{-5}$–$2.71603\,10^{-5}$ | $5.93342\,10^{-7}$ |

All rates come from the same spectrum/dipole; that equal rates or high photon overlap do not by themselves imply preservation of the ground phase is shown by W17 and V39 below.

#### S8.18.3 A finite-time instrument including the no-photon outcome

To avoid assuming complete cooling, use the following **explicit exponential-emission model**: all $q$ share one dipole output channel, there is no zero-frequency noise, and only the bright transition from the first excited state to the ground is active; the spatial mode overlap is $1$, and rates and transition energies are (B17-3). The prepared input is $\sum_qc_q|e_q\rangle$, whose sector coherence and phases are supplied resources.

At time $T$ the no-photon Kraus operator and the photon Kraus operators of the time mode $\tau\in[0,T]$ are

$$
L_0=\sum_qa_q(T)|e_q\rangle\langle e_q|,\qquad a_q(T)=e^{-\gamma_qT/2-iE_{eq}T},
\tag{B17-5}
$$
$$
L_\tau=\sum_q\sqrt{\gamma_q}\,e^{-\gamma_q\tau/2-i\omega_q\tau-iE_{gq}T}|g_q\rangle\langle e_q| ,
\tag{B17-6}
$$

and since the $q$ are orthogonal,

$$
L_0^\dagger L_0+\int_0^TL_\tau^\dagger L_\tau\,d\tau=I_{\rm excited}
\tag{B17-7}
$$

exactly. The sector Gram of the photon success branch is

$$
R_{qr}(T)=e^{-i(E_{gq}-E_{gr})T}\sqrt{\gamma_q\gamma_r}\,\frac{1-e^{-[A_{qr}+i(\omega_q-\omega_r)]T}}{A_{qr}+i(\omega_q-\omega_r)},\qquad A_{qr}=\frac{\gamma_q+\gamma_r}2 ,
\tag{B17-8}
$$

obtained directly from $\int_0^TL_\tau(\cdot)L_\tau^\dagger d\tau$; $R\ge0$, $R_{qq}=1-e^{-\gamma_qT}$, $F=R+aa^\dagger\ge0$ with $F_{qq}=1$ — $F$ is an auxiliary Gram for completeness and does not identify the distinct excited/ground output spaces.

The actual output has three outcomes $\{0,+,-\}$: no-photon is kept as the single outcome $0$; in the photon branch C6 of S7.3 is applied to the ground reference. The probability of $0$ is independent of the probe input $\pm$, so the all-outcome total variation is

$$
D_{{\rm flag},{\rm C6}}(T)=\Bigl|\Re\sum_qc_qc_{q+1}w_qR_{q,q+1}(T)\Bigr|,\qquad p_{\rm em}(T)=\sum_qc_q^2\bigl(1-e^{-\gamma_qT}\bigr).
\tag{B17-9}
$$

Neither expression is divided by $p_{\rm em}$; the time modes are integrated, so no time-resolved detection or feedback is used for free.

V39 compares the closed form (B17-8) with direct numerical integration at $T=5/\min_q\gamma_q$, and checks Gram positivity, diagonal completeness and the un-normalised three-outcome contrast.

| $B,j,D$ | $\eta/J$ | $JT$ | photon probability | no-photon probability | all-outcome $D_{{\rm flag},{\rm C6}}$ |
|---|---:|---:|---:|---:|---:|
| 96,32,17 | 0 | 226288.96 | 0.993262 | 0.006738 | 0.978145 |
| 128,42,21 | 0 | 398196.90 | 0.993262 | 0.006738 | 0.983152 |
| 96,32,17 | $10^{-4}$ | 184104.52 | 0.993262 | 0.006738 | 0.446420 |

Similar emission probabilities do not guarantee similar record contrasts; the low contrast of the charged case carries the actual ground phases of (B17-8). The third row is at a different time from W17 and the two values are not joined as points on one monotone decay curve.

This instrument is exact within the stated WW channel. It does not certify the initial and long-time tails of a finite positive-frequency bath, reabsorption, non-Markovian memory, additional transitions, zero-frequency noise or real detection errors, and since different finite $\omega_q$ are bundled into one channel it is not the strict Davies secular limit either. The next physical step is to apply the finite-band direct Hamiltonian method of S8.15 and the common errors of S8.17 to this source; no claim is made that those long-time errors were shown small here.

## S9. From a finite pump to a readable output record

### S9.1 M70's static one-photon channel and the supplied resources

The derivations of this section are **conditional results for defined comparison models**, tools for guessing the S14 coupling of later work, not a completion of the physical bridge or a new optical principle. $\hbar=c=1$.

For M70's massive boundary band $E(\mathbf k)=\sqrt{|\mathbf k|^2+m_b^2}$, $m_b>0$, one has $|\nabla E|<1$ at finite $\mathbf k$, so for non-zero photon momentum $(\mathbf p,k_\perp)$

$$
\Omega=E(\mathbf k-\mathbf p)+\sqrt{|\mathbf p|^2+k_\perp^2}-E(\mathbf k)>0
\tag{A8}
$$

(the Lipschitz inequality for $\mathbf p\ne0$; positivity of the photon energy for $\mathbf p=0$). So in this **static, single positive band, one-photon channel** there is no on-shell emission — inherited from M70 §7.1.

External switching $\chi(t)$ can create an amplitude $\widehat\chi(\Omega)$ whose energy and timing are apparatus inputs. Subsequent constructions therefore first decide **what supplies the energy: an incoming probe, an actual boundary transition, or a dynamical boundary background**; here a mode explicitly holding the incoming energy is chosen as the smallest positive comparison object.

### S9.2 One finite energy source and two output channels

Let the neutral degenerate register $O$ holding the front-end outcome of S7.3 have states $|z\rangle$, $z=\pm1$, $Z:=Z_O$, $Z_O|z\rangle=z|z\rangle$, with bare Hamiltonian and charge declared $0$. The photon mode $c$ is the finite energy source and $a,b$ the two outputs. For real $g_0,g_1$,

$$
H_0=\omega(N_c+N_a+N_b),\qquad H_{\rm int}=g_0(c^\dagger a+a^\dagger c)+g_1Z(c^\dagger b+b^\dagger c).
\tag{A9}
$$

With $G=\sqrt{g_0^2+g_1^2}>0$ and $\omega>G$ the photon Hamiltonian is bounded below on the full Fock space; $[H_0,H_{\rm int}]=0$, $[Z,H_{\rm int}]=0$; the two register states have equal charge and photons are neutral, so this **declared model** conserves total photon number and bare energy. The common phase symmetry of photon number is not the electromagnetic local gauge symmetry; that (A9) satisfies the full Gauss law, boundary momentum and the M56 grading is not derived. The model's measured quantities commute with the conserved quantities, so it is not a counterexample to the non-commuting-target cost of M71.

On a fixed branch let the bright mode be

$$
d_z^\dagger=\frac{g_0a^\dagger+zg_1b^\dagger}G,\qquad p=\sin^2(Gt),
$$

so $H_{{\rm int},z}=G(c^\dagger d_z+d_z^\dagger c)$. With exactly $n$ photons initially in $c$ and vacuum outputs, in the interaction picture

$$
|\Psi_z(t)\rangle=\frac{\bigl[\sqrt{1-p}\,c^\dagger-i\sqrt p\,d_z^\dagger\bigr]^n}{\sqrt{n!}}|0\rangle ,
\tag{A10}
$$

written for $0\le Gt\le\pi/2$ (otherwise $\cos Gt,\sin Gt$ with signs replace $\sqrt{1-p},\sqrt p$). No external optical coherent phase is needed in the initial state. **The initial $|n\rangle_c$, mode geometry, couplings and reading time remain preparation/apparatus inputs**; using a time-independent Hamiltonian does not derive preparation and clock.

### S9.3 Coherence can vanish while no output record exists

Keep $c$ for the next round and read only $a,b$; define $D_{\rm out}=\tfrac12\|\rho_{{\rm out},+}-\rho_{{\rm out},-}\|_1$. The probability of $\ell$ output photons and the overlap of the two bright modes are

$$
w_\ell=\binom n\ell p^\ell(1-p)^{n-\ell},\qquad s=\langle1_{d_-}|1_{d_+}\rangle=\frac{g_0^2-g_1^2}{g_0^2+g_1^2}.
$$

Different $\ell$ sectors are orthogonal and within a sector the two pure states overlap by $s^\ell$, so

$$
\boxed{D_{\rm out}(n,p,s)=\sum_{\ell=0}^nw_\ell\sqrt{1-|s|^{2\ell}}.}
\tag{A11}
$$

All number-conserving effects on the two output modes are allowed; the optimal effect in each $\ell$ block commutes with total energy, so the unrestricted trace distance and the optimal discrimination in that admissible algebra coincide. Whether an actual local detector implements that effect is a separate question.

Applying this optical channel to a coherent register input, the environment overlap multiplying the register off-diagonal is

$$
\gamma_n=\langle\Psi_-|\Psi_+\rangle=(1-p+ps)^n .
\tag{A12}
$$

In particular **without a common output channel**, $g_0=0$, $s=-1$, and

$$
D_{\rm out}=0\quad\text{while}\quad\gamma_n=(1-2p)^n .
\tag{A13}
$$

At $n=1$, $p=1/2$ the register is completely dephased while the outputs alone cannot read the branch at all; the information sits in the **correlation** between the retained source and the outputs, and accessing $c$ together with the outputs gives trace distance $1$ between the two pure states. Where one draws the observable subsystem of the same field changes the physical conclusion. (A11)–(A13) are conditional comparison results derived here and checked by the joint unitary; consistent with E11, vanished off-diagonals are not replaced by an external objective record.

### S9.4 A positive construction of relational reading

When the common and branch-dependent channels are balanced, $g_0=g_1\ne0$,

$$
d_\pm=(a\pm b)/\sqrt2,\qquad s=0,
$$

so non-vacuum bright-mode states are orthogonal: count which port carries the photon behind a fixed passive mode mixer, which conserves energy and photon number for equal-frequency modes. Hence

$$
\boxed{D_{\rm out}=1-(1-p)^n.}
\tag{A14}
$$

Only the common vacuum outcome, probability $(1-p)^n$, carries no branch information: $D=1/2$ at $n=1$, $p=1/2$ and $D=15/16$ at $n=4$, $p=1/2$. Balance, relative phase and mixer axis are present apparatus choices with no proof that S14 fixes them. **Relational optical reading is a known family of methods and must be compared with E06.**

For $n=1$ with $P_\pm=(I\pm Z)/2$, the all-outcome map for the initial source $|1\rangle_c$ is

$$
\mathcal I_\varnothing(\rho)=(1-p)\rho\otimes|1\rangle\langle1|_c,\qquad
\mathcal I_+(\rho)=pP_+\rho P_+\otimes|0\rangle\langle0|_c,\qquad
\mathcal I_-(\rho)=pP_-\rho P_-\otimes|0\rangle\langle0|_c,
\tag{A15}
$$

each CP with traces summing to $1$; the click probabilities are $p\rho_{++},p\rho_{--}$ and the no-detection probability $1-p$; conditioning on success gives the standard Born weighting — a **standard instrument computation using the Born trace rule**, not a derivation of that postulate or of the occurrence of a single outcome. The domain of (A15) is **one preparation with the pump fixed at $|1\rangle$**; reducing it to a map on $O$ alone and iterating hides the cost of replacing the emptied pump by a fresh $|1\rangle$; repetition must update the whole $O+c$ state.

### S9.5 What remains when one writes again

Consider mutually orthogonal output-mode pairs $(a_j,b_j)$ interacting sequentially with the same pump, with equal $p$, balanced coupling and a fixed branch, never re-acting on earlier outputs. The probability that a photon goes to the $j$-th fragment and that it remains in the pump after $m$ rounds are

$$
q_j=p(1-p)^{j-1},\qquad q_c=(1-p)^m,\qquad q_c+\sum_{j=1}^mq_j=1 .
\tag{A16}
$$

For an initial $n$-photon Fock state each fragment's photon number has the binomial marginal of $q_j$ and non-vacuum branch states are orthogonal, so

$$
\boxed{D_j=1-(1-q_j)^n,\qquad \sum_jD_j\le n\sum_jq_j\le n,}
\tag{A17}
$$

the last from $1-(1-q)^n\le nq$; a diagonal mixture of initial photon numbers gives the same with $n\to\langle N\rangle$. Defining $R_\epsilon$ as the number of disjoint fragments with $D_j\ge1-\epsilon$,

$$
\boxed{R_\epsilon(1-\epsilon)\le\langle N\rangle=E_{\rm probe}/\omega .}
\tag{A18}
$$

This is **a simple resource bound of that passive outgoing-photon record class**, neither a universal energy lower bound for measurements nor a Landauer cost per bit; processes in which an existing photon marks several matter memories in turn, extra amplification or energy input, and soft modes without a frequency floor are outside the class, and with finite mean energy and $\omega\to0$ allowed no energy lower bound follows from the photon-number bound.

For $n=1$, $p=1/2$, $m=4$:

| round | $D_j$ with the actually retained pump | $D_j$ in a different model with a fresh pump each round |
|---|---:|---:|
| 1 | 0.5 | 0.5 |
| 2 | 0.25 | 0.5 |
| 3 | 0.125 | 0.5 |
| 4 | 0.0625 | 0.5 |
| emitted energy sum / $\omega$ | 0.9375 | 2.0 |

The residual pump energy is $0.0625\,\omega$. The right column is not wrong mathematics but **a different preparation process that supplies a photon each round**; comparing repeated performance without recording the supply is the error.

The ensemble condition that different fragments each have high distinguishability and the condition that several fragments hold the record in one trial are distinguished; in the passive one-photon model only one fragment receives the photon per trial, and (A18) is not read as a proof of simultaneous definite records of many observers.

### S9.6 Persistence is not automatic

Re-coupling to the same closed output mode and executing $U(-t)U(t)$ returns the initial state; in the actual computation the output record was erased after the echo — a result of the **closed comparison model without added external reading/recording in between**, not an erasure of a record already held by an external detector without interacting with it.

A claim of persistent records must therefore identify which of the following arises from the actual action: a scattering structure in which the record mode leaves the interaction region and never recombines; a record transferred to additional degrees of freedom with their residual apparatus state; or a quantitative bound making recurrence/reversal probabilities small over a finite time interval. That vacua of orthogonal modes factorise in free Fock space does not prove that spacetime regions of a local QFT are independent vacuum ancillas; positive frequency, localisation and waveform overlap must be handled together. The independent output pairs of (A16) are an exact finite comparison assumption, and deriving them from actual spacetime fragments remains.

### S9.7 The smallest form for attaching physical error

If two self-adjoint Hamiltonians on a finite-cutoff space satisfy $\|H_{\rm full}-H_{\rm eff}\|\le\delta_H$, Duhamel gives

$$
\|U_{\rm full}(t)-U_{\rm eff}(t)\|\le|t|\delta_H ,
\tag{A19}
$$

controlling the trace distance of each branch output for the same initial state and reading. If the total implementation error of each branch is actually proved to be $\eta_\pm$, the triangle inequality gives

$$
\boxed{D^{\rm full}_{\rm readable}\ge D^{\rm eff}_{\rm readable}-\eta_+-\eta_- ,}
\tag{A20}
$$

the shortest success condition for later work. **The reading admitted on the left must correspond physically to the reading on the right**; the optimal effect may not be swapped arbitrarily, and unrestricted trace distance may not be replaced by realisable detector distinguishability.

The operator-norm assumption of (A19) cannot be used as is for unbounded global-QFT interactions; cutoff removal, energy-constrained norms, packet tails, leakage and localisation errors must be derived separately. No $\eta_\pm$ for S14 was obtained, so the physical positivity certification of (A20) is still **OPEN**.

Leakage handling was checked in a simple finite example: with $K=PUP$ and $L=(1-P)UP$,

$$
K^\dagger K+L^\dagger L=I_P ,
\tag{A21}
$$

and normalising $K$ alone into a trace-preserving map generally mixes in non-linear conditioning; keeping failure/leakage outcomes separately is the correct comparison. (A19)–(A21) are standard tools, not new contributions.

### S9.8 Joining the two seeds: neutral outcome register and final input distinguishability

Assume the optimal M71 reference is supplied. The combined front-end readout and balanced optical transmission give

$$
D_{{\rm input}\to{\rm out}}=C_L[1-(1-p)^n],\qquad L=\lfloor\sqrt N\rfloor .
\tag{U1}
$$

Write the outcome $r$ of S7.3 into the neutral degenerate register $O$ with $Z_O|r\rangle=r|r\rangle$; the $Z$ of the optical model is this $Z_O$. The instrument still uses a quantum-to-classical outcome rule and does not derive the ontology of a single outcome or the Born postulate.

For the M71 states $x=\pm1$ the outcome distribution is $q(r|x)=(1+rxC_L)/2$; with the balanced pump's $\eta_n=1-(1-p)^n$ the no-detection, positive and negative port probabilities of the final output are

$$
\Pr(\varnothing\mid x)=1-\eta_n,\qquad \Pr(r\mid x)=\eta_n\frac{1+rxC_L}2 .
\tag{U2}
$$

The vacuum probability is input-independent and non-vacuum ports are orthogonal, so the TV of the two output distributions is (U1). More generally with optical branch states $\rho_\pm^{\rm out}$,

$$
\rho^{\rm out}_{x=+}-\rho^{\rm out}_{x=-}=C_L(\rho_+^{\rm out}-\rho_-^{\rm out}),\qquad D_{{\rm input}\to{\rm out}}=C_LD_{\rm optical},
\tag{U3}
$$

with $D_{\rm optical}$ the general unbalanced (A11) and the same admissible-algebra condition inherited; balanced coupling reads it by a passive mixer and counting.

Writing the full state update for $n=1$, with $\rho$ the $S+RC$ state and $K_r$ the Kraus operators of S7.3 moved to the fixed $R:C$ code,

$$
\mathcal J_\varnothing(\rho)=(1-p)\sum_rK_r\rho K_r^\dagger\otimes|r\rangle\langle r|_O\otimes|1\rangle\langle1|_c,\qquad
\mathcal J_r(\rho)=pK_r\rho K_r^\dagger\otimes|r\rangle\langle r|_O\otimes|0\rangle\langle0|_c,
\tag{U4}
$$

all CP with total trace $1$. $\varnothing$ means **no record in the optical output**, not that the front-end M71 measurement is undone; the $RC$ backaction of the front end must be preserved even in the no-detection branch — an important condition added at integration, distinct from the error of repeating (A15) on the system alone.

With one M71 outcome register and one pump feeding several fragments,

$$
\boxed{D_j^{\rm input}=C_L[1-(1-q_j)^n],\qquad q_j=p(1-p)^{j-1},\qquad \sum_jD_j^{\rm input}\le C_Ln ,}
\tag{U5}
$$

and with a diagonal mixture of initial photon numbers the right side becomes $C_L\langle N_c\rangle$. The number $R_\epsilon$ of fragments with $D_j^{\rm input}\ge1-\epsilon$ satisfies $R_\epsilon(1-\epsilon)\le C_LE_{\rm probe}/\omega$ in this class, and if $1-\epsilon>C_L$ there is no such fragment at all. For $N=2$, $n=1$, $p=1/2$ the first four fragments have $D_j^{\rm input}=(0.35355339,0.17677670,0.08838835,0.04419417)$; the earlier $(0.5,0.25,0.125,0.0625)$ were distinguishabilities of the already fixed optical branch label, and attaching the imperfect M71 front end multiplies by $C_L$.

All fragments share the same classical outcome $r$ and the pump; they are not a product distribution of independent fresh measurements. Measuring several $|\pm x\rangle$ inputs **repeatedly with the same M71 reference** is a different problem from (U5): then the $RC$ backaction of (U4) must be carried to the next input and $C_L$ cannot be re-attached each round.

Two checkable predictions are $D_n^{\rm input}=C_L[1-(1-D_1^{\rm input}/C_L)^n]$ and, when one photon and the same outcome feed several fragments, $D_{j+1}^{\rm input}/D_j^{\rm input}=1-p$; the two settings are not mixed. These remain predictions of the comparison model, not of a Z-Spin-specific scale.

### S9.9 The present integration of preparation, relaxation, reading and output

U1–U5 are for the declared model with an optimal M71 reference given. Attaching the reference after an actual preparation uses that state's readout response; only in the common-ground-basis, complete-cooling K3 class do $z_1^{\rm out}$, $\Gamma=C_j|z_1^{\rm out}|$ and (U0) hold; in the finite-time, $q$-dependent-ground case FT1–FT2 and REC1–REC2 are used.

If the optical states for the two neutral-register values are $\tau_0,\tau_1$ and the probability difference of the preceding actual readout is $\chi_\phi$,

$$
\rho_{\rm out}^{(+)}-\rho_{\rm out}^{(-)}=\chi_\phi(\tau_0-\tau_1),\qquad D_{\rm out}=|\chi_\phi|\,D(\tau_0,\tau_1).
\tag{U0a}
$$

In the balanced channel $D(\tau_0,\tau_1)=1-(1-p)^n$; for the flag-preserving procedure of S8.16, $\chi_\phi=\Re(e^{i\phi}z_g)$, and no postselection removes the success probability. The three-environment example of K4 at $j=1$, $B=4$ is kept as a mathematical comparison showing that equal population cooling can give different records; the earlier identification of those three with the radiation/Coulomb limits of S14 is retracted.

For the restricted finite-time preparation P3 the conservative bound $D_{\rm out}(t)\ge\eta\max\{0,\Gamma_\infty-2C_j\epsilon_{\rm prep}(t)\}$ is kept within its assumptions; adding full-model errors uses trace distances of the same all-outcome output and the same admissible measurement, as in FT3/ERR2. Source, phase, clock, detector, pump and memory reuse each stay on the ledger.

**Connection.** B15 adds explicit lower bounds to the preparation and storage stages of this record chain and B17 adds the all-outcome cooling example of the first bright transition; the finite pump, output and reuse budget of S9 are not supplied free from them.


## S11. The retracted central candidate and the surviving physical research target

### S11.1 The decisive counterexample I1 to T-MD(i)

**Theorem I1 — same conserving effects, same preparation, inequivalent $RC$ updates.** Even inside the M71 class declared earlier, $\kappa$, the source profile and $B$ do not fix the equivalence class of the instrument.

*Construction.* $N=1$, $B=3$, $\kappa=5$ give $j=1$, $D=2$; supply the source profile $c=(1,1)/\sqrt2$. In the $e=1$ $RC$ basis $(|-1,0\rangle,|0,1\rangle,|1,0\rangle)$ the reduced state is

$$
\rho_{RC}=\begin{pmatrix}1/4&1/(4\sqrt2)&0\\1/(4\sqrt2)&1/2&1/(4\sqrt2)\\0&1/(4\sqrt2)&1/4\end{pmatrix}.
\tag{I1}
$$

With $F_\pm=(I\pm B_R)/2$, $K_\pm=\sqrt{F_\pm}$ of S7.3 and $\Pi_m$ the $RC$ projection onto charge $m$, compare the two all-outcome instruments

$$
\mathcal I_r(\rho)=K_r\rho K_r^\dagger,\qquad \mathcal J_r(\rho)=\sum_m(I_S\otimes\Pi_m)K_r\rho K_r^\dagger(I_S\otimes\Pi_m).
\tag{I2}
$$

All Kraus operators commute with $N_S+M$ and $E$, and the effects coincide exactly: $\mathcal I_r^*(I)=F_r=\mathcal J_r^*(I)$, $\sum_rF_r=I$. Outside the code a common conserving completion is attached; the dephasing uses charge-commuting projections and any extra environment can be a neutral ancilla degenerate in charge and energy — forbidding it would itself be a separate apparatus-class constraint absent from T-MD.

*Inequivalence certificate.* For the input $S=|+x\rangle$ the probability of $r=+$ is $p_+=\tfrac12+\tfrac{\sqrt2}8$ in both cases. The purities of the conditional $RC$ states after discarding $S$ are

$$
\operatorname{tr}\rho_{RC|+}^{\,2}=\frac{415+66\sqrt2}{784},\qquad \operatorname{tr}\widetilde\rho_{RC|+}^{\,2}=\frac{265+2\sqrt2}{784},
\tag{I3}
$$

and the trace distance of the two $RC$ states is about $0.429567$. More strongly, the Choi ranks of the joint operations for that outcome are $1$ versus $3$, and the Choi ranks of the **$RC$-output operations** after tracing $S$ are $2$ versus $6$; for $r=-$ the same rank gap holds by a diagonal $S$ phase conjugation. Choi ranks are invariant under input/output unitary conjugation and outcome relabelling, so the invariant diagonal gauge equivalence of the earlier version cannot merge the two. C01 of the inherited ledger certifies effect equality, commutators, exact purities and both ranks in symbolic arithmetic. $\square$

"Designating the update C6 as a definition fixes the update" is not a selection theorem. That a general instrument for a fixed POVM is a Lüders instrument followed by outcome-dependent channels is known; the contribution of I1 is to make it **an exact counterexample that cannot be removed within the conserving class already admitted here** (Leppäjärvi–Sedlák §2).

### S11.2 Replacing the minimal-data claim by operational statements

| original clause | final status | exact replacement |
|---|---|---|
| (i) optimal value and unique instrument for any $c$ | **FALSE** | actual value (G16)/(U0), ceiling (G12), instrument fibre I4 |
| (ii) necessity of $\kappa$ and $d$-fold non-identifiability | **proof wording retracted** | $\kappa=3$ and $4$ give the same $j=1$ ground space; specifying the $e=j^2$ to be prepared makes $\kappa$ a non-essential coordinate of the state |
| (iii) removing sector coherence gives $0$ | **kept conditionally** | the full $U(1)$-covariant preparation condition of T-NOREC; asymmetry alone is not sufficient (W03, K4) |
| (iv) no continuous reduction to one real number | **original statement retracted** | which data space, injectivity, inversion and quotient are required must be fixed first; degenerate exceptions at $D=1$ / single task exist |

In particular the claim that the absence of $\kappa$ restores the $d$ of S2 mixes different problems: S2 is the family of top shells at the fixed $\Gamma$ ceiling, while the ground problem of $H_{\rm cons}$ includes source and energy costs; as $\kappa$ varies continuously between thresholds, the ground vector and its update candidates do not change. That $\kappa$ affects the time scale of actual control dynamics and that it is minimal identifying data of the resulting state are separate matters.

**I4 — a sufficient specification naming the needed objects.** In a finite active space the joint operations with fixed effects $F_r$ are described by Choi matrices

$$
J_r\succeq0,\qquad \operatorname{tr}_{\rm out}J_r=F_r^{\mathsf T},
\tag{I4}
$$

and if strictly every Kraus operator conserves $Q,E$, the support of $J_r$ is restricted to $\operatorname{span}\{|K\rangle\!\rangle:[K,Q]=[K,E]=0\}$. One element of this set must be chosen by the action, or a quotient proved in which the difference disappears for the present task; this rewrites the general CP specification and is not named a theorem of minimal "physical" data.

| To be predicted | Sufficient information in the declared class | Not predictable from it alone |
|---|---|---|
| optimal single-shot contrast of a prepared reference | $j$ and $z_1^{\rm out}$ | higher source coherences, subsequent $RC$ state |
| probabilities of a fixed-phase detector | $j$, $z_1^{\rm out}$, $\phi$ and the input state | outcome-wise backaction |
| record after K1 cooling | $j$, $\sigma$, normalised $G$ and the declared rate class | the action origin of the actual $G$ |
| outcome-wise $RC$ update for equal effects | the Choi operation or equivalent channel data | physical localisation and apparatus preparation origin |
| repeated record and clock | joint channel history including all retained subsystems | identity with a repetition that secretly supplies fresh sources |

The sufficiency in this table is mathematical for fixed task and model, not unique minimal physical data; the $j,z_1$ expressions hold in the common-ground preparation class, while the finite-time/tilted class uses FT1–FT2 and REC1. T-VERTEX selects the $B_R$-block-preserving class but not one instrument in it; the full vertex, probe state, time and readout are needed and are not reduced to a single $U/\gamma$ ratio.

### S11.3 The physical target T★ that stands and the present conditional attainment

**T★ [OPEN].** In one concrete boundary class of the printed S14 action, construct the physical operation space, $\iota$, the occupied state, environment, source and admissible instrument, and obtain a positive lower bound of the actual record contrast at the same finite time $T$ and the same all-outcome output:

$$
D^{\rm full}_{\rm readable}(T)\ge\max\{0,\ D^{\rm model}_{\rm same\ task}(T)-\epsilon_+(T)-\epsilon_-(T)\}>0 .
\tag{TSTAR}
$$

With the designated optical encoder of S9 attached, $D^{\rm model}=\eta|\Re(e^{i\phi}z_g)|$, $\eta=1-(1-p)^n$, is one example class. The hoped-for ceiling of $\Gamma$ or the conditional value of a success branch is never put in the place of the full actual contrast; the composition is used only when every channel is actually in place.

| Obligation | Secured here | Actual unresolved input |
|---|---|---|
| boundary/current | BC1–BC3 of M70's declared band; common complex spectral specification BC4 | S14-selected geometry, occupation, code embedding; final-matter states and actual photon modes |
| Coulomb | finite full-capacitance example; projection complement ES4 | continuum density matrix elements, self-energy subtraction, actual $P\rho Q\rho P$ |
| $c,\gamma,\omega,U$ | same-model numbers MIC1–MIC3 | numbers fixed by actual units, scales and boundary state |
| Lamb shift | cutoff-explicit PV coefficient of the same spectral density and a non-identifiability counterexample | renormalised full-QED value; off-shell, other-level, counter-rotating data |
| finite-time instrument | FT8 and V25 all-outcome completeness | the same instrument in the actual full-field Hilbert space and apparatus |
| common error | ERR1–ERR2 proofs for bounded/flagged cases; positive FT3 for an example envelope | actual same-$T$ bounds for occupied packet, recoil, bulk, projection, Coulomb, detector |
| selection/observation | separation of phase-optimal and fixed-phase contrast of a supplied reference | action origin of source asymmetry, actual readout selection, single outcome, Born weights |
| **source type** | quantified differences of sector spectra and record dynamics between flat and su(2) (S6.11) | which charge-source type (flat, su(2), bounded oscillator) the S14/M70 boundary current supplies; the competition of cooling rate and $\Omega$ at finite $B$ |

The earlier reduction "obtain four numbers and the original obligation closes" is not adopted: zero-frequency, off-shell, initial-environment, no-detection and recoil/leakage data are required as well; conversely, not every value must first be compressed into Markov parameters — given an actual boundary Hamiltonian, the finite-time route (FT4)–(FT8) computes the needed record response directly.

### S11.4 Before/after of the debts: no new global IDs, no closures

| Existing object | change from v1.6 to v1.7 (last two rows: v1.7 to v1.8) | current state |
|---|---|---|
| D-M69-MOVING | energy, dipole, rate and record of the declared spin/Gauss block computed together; sufficient condition on the remainder norm | OPEN: occupied moving packet, recoil, bulk, projection, Coulomb, detector in a common window |
| D-M69-INSTRUMENT | common-parent record connected to the fixed C6 and the three-outcome cooling instrument | OPEN: no derivation of the S14-selected apparatus, boundary and initial state |
| K17/K18 | CAR/CCR and global/regional charge distinguished; costed block preparation made explicit | OPEN: actual gauge subsystem and reuse conditions |
| D-S14-EVENT-001 | the electric-$U(1)$-limited no-go of T-GRADE kept | OPEN: seam selection and single event not derived |
| D-HCLK-001 | fixed-C6 storage bound without phase correction; time and readout costs explicit | OPEN: physical clock and equality-record connection |
| T-MD(i) | counterexample I1 preserved | FALSE, not restored |
| G11–G18 | flat results preserved; fixed-$j$ spin limit and joint limit distinguished | scope repaired; B15 is a different positive construction on a narrow low-energy band |
| B14 remaining rate/charging computations | performed on declared examples (V36–V39, W17–W18) | partially resolved at model level; the physical source choice is OPEN |
| novelty of K5/K6/T-TILT | K5 subsumed; K6 exact mapping unrestored; E26 spin identification removed | central non-subsumption still undetermined |
| sharpness and lifetime ceiling of B15 | repaired by Theorems 1–2 and Section 5.4 of the main text | two-sided exponent interval proved for the declared band; the exact exponent is now characterised by Section 9, and the physical source choice is OPEN |
| source-size allocation | replacement Theorem 3 and Section 5.3 | scalar rate decrease and fixed-window lifetime growth separated; full-cost optimisation OPEN |


---

## Appendix N. The spatial-record note: general history response, recovery rank, currents, projection and dilution

This appendix keeps the mathematics of the note with its original assumptions; section numbers carry the prefix N and the original equations (1)–(64) and Propositions N1–N5 are retained. So that the simple N1–N2 computations are not read as providing physical spatial transport automatically, actual writing and capture are those of Section 6 of the main text; the independent-flip storage formula is extended to joint flips in Section 8.2; the polarisation is derived in Theorem 5, and the free input $r$ of the note is never counted as a free resource.

## N2. The basic object of recovery: from history to the present record

Let $S$ be the carrier, $F$ the memory finally read, and $E$ the other degrees of freedom. For a history $h$,

$$
U_h=\mathcal T\exp\Bigl[-i\int H_h(t)\,dt\Bigr],\qquad \rho_h^F=\mathcal R_F\bigl(U_h\rho_0U_h^\dagger\bigr),
\tag{1}
$$

where $\mathcal R_F$ is the same CPTP map comprising removal of inaccessible degrees of freedom, a fixed reading device and preserved failure flags; the compared histories share the initial preparation and access rule.

With $\mathcal A_F$ the algebra of admissible effects on the spatial region, the relevant quantity is

$$
D_{\mathcal A_F}(h,h')=\sup_{\substack{0\le M\le I\\M\in\mathcal A_F}}\bigl|\omega_h(M)-\omega_{h'}(M)\bigr| .
\tag{2}
$$

If every effect of the finite memory is admissible this is the trace distance of the two density matrices in (1); if the device implements only certain measurements, the total variation of their outcome distributions is used, and the performance of an unimplemented optimal measurement is not read as actual detector performance. For equal priors,

$$
P^F_{\rm guess}(h,h')=\frac{1+D_{\mathcal A_F}(h,h')}2 ,
\tag{3}
$$

standard state discrimination; in the two-memory models below simple individual measurements with outcome comparison attain the optimum (Watrous, Thm. 3.4).

### N2.1 What can be recovered is an observationally different history

Define

$$
h\sim_Fh'\iff\omega_h|_{\mathcal A_F}=\omega_{h'}|_{\mathcal A_F}.
\tag{4}
$$

Histories producing the same record state cannot be distinguished by that record; the proper object of recovery is **the equivalence class of histories distinguished by the record channel**, a consequence of the definition, not a new classification theorem. If the initial state may also vary, non-identifiability is stronger: for any final total state $\sigma$ and any $U_h$, $\rho_{0,h}=U_h^\dagger\sigma U_h$ gives the same final state. **Without information on initial preparation, coupling and the reading method, the present structure alone does not determine the past uniquely.** History reading and calibration of the process are different tasks; process-tensor work on operations and outputs at several times is an important comparison (Pollock et al.).

### N2.2 Information at one place and between places

Splitting the memory into $F_1,\ldots,F_m$,

$$
D^{(k)}(h,h')=\max_{\substack{J\subseteq\{1,\ldots,m\}\\|J|\le k}}D_{\mathcal A_{\cup_{j\in J}F_j}}(h,h')
\tag{5}
$$

is the distinguishability when at most $k$ places are read together; with consistently included effects $D^{(1)}\le D^{(2)}\le\cdots$. In the order-record example of N3, $D^{(1)}=0$, $D^{(2)}=1/2$: **each place looking like an empty record does not mean the whole space holds none.** In actual gauge QFT the spatial split cannot be assumed to be a tensor product of independent qubits; the observable-algebra form of (2) leaves this open, and the finite-qubit example assumes two separately prepared devices. The Fewster–Verch framework for constructing measurement maps from local couplings and composing causally separated operations is the field-theoretic reference.

### N2.3 A positive example: content perfectly kept, order not

With the carrier's two known contents $Z_S|z\rangle=z|z\rangle$, $z=\pm1$, each memory starting at $|0\rangle_j$, and local collisions

$$
U_j=\exp[-i\theta_jZ_S\otimes Y_j/2],
\tag{5a}
$$

the memories conditioned on content $z$ are

$$
|m_{j,z}\rangle=\cos(\theta_j/2)|0\rangle_j+z\sin(\theta_j/2)|1\rangle_j,\qquad
\boxed{D_F(+,-)=\sqrt{1-\prod_{j\in F}\cos^2\theta_j}.}
\tag{5b}
$$

Each memory's conditional overlap is $\cos\theta_j$ and product states multiply overlaps, so the pure-state trace-distance formula applies; $D_F$ is the optimal distinguishability of the chosen set of fragments. Implementing the optimal joint measurement at general angles is separate, but at $\theta_j=\pi/2$ each memory holds $|\pm X\rangle$ and **the local $X_j$ measurement alone reads the content exactly**. This copies two classically distinguishable contents; it clones no unknown quantum state. Yet for different memories $j,k$,

$$
[Z_S\otimes Y_j,\ Z_S\otimes Y_k]=0,
\tag{5c}
$$

so the **order** of equal-angle collisions leaves no trace in the final record: many places may know the content of an event perfectly without knowing which place touched it first. This is the standard conditional-environment-record model applied to the content/order distinction; the direct unitary check W08 of the note confirms perfect content discrimination with zero order discrimination.

## N3. The exact minimal construction: order survives in the correlation of two places

### N3.1 The model

The carrier $S$ interacts once with each of the memory qubits at places $A$ and $B$; all $X,Y,Z$ here are logical Paulis, not identified with Z-Spin sector names. The initial state is

$$
\rho_0=\frac{I_S+rY_S}2\otimes|+\rangle\langle+|_A\otimes|+\rangle\langle+|_B,\qquad |r|\le1,
\tag{6}
$$

$r$ the known carrier polarisation ($r=1$ the positive $Y_S$ eigenstate). With $P_0=|0\rangle\langle0|$, $P_1=|1\rangle\langle1|$ on the memories,

$$
C_X=I_S\otimes P_{0,A}\otimes I_B+X_S\otimes P_{1,A}\otimes I_B,\qquad
C_Z=I_S\otimes I_A\otimes P_{0,B}+Z_S\otimes I_A\otimes P_{1,B},
\tag{7}
$$

and the two histories are

$$
h_{AB}:U_{AB}=C_ZC_X,\qquad h_{BA}:U_{BA}=C_XC_Z .
\tag{8}
$$

After the interactions the carrier is discarded and only the memories at $A,B$ are read. This is an effective collision model in which the carrier **visits the two places causally in sequence**, not an instantaneous coupling of one qubit to two distant devices.

### N3.2 Proposition N1: equal local marginals, different joint records

From (6)–(8), exactly

$$
\boxed{\rho^{AB}_{AB}=\frac{I_{AB}+rY_AX_B}4,\qquad \rho^{AB}_{BA}=\frac{I_{AB}-rX_AY_B}4,}
\tag{9}
$$

hence

$$
\rho^A_{AB}=\rho^A_{BA}=\rho^B_{AB}=\rho^B_{BA}=I/2,\qquad \boxed{D_{AB}=|r|/2.}
\tag{10}
$$

**Derivation.** Labelling the memory computational basis by $a,b\in\{0,1\}$, the conditional carrier operations are $W^{AB}_{ab}=Z^bX^a$, $W^{BA}_{ab}=X^aZ^b$, and

$$
\langle ab|\rho^{AB}_h|a'b'\rangle=\frac14\operatorname{tr}_S\Bigl(W^h_{ab}\frac{I+rY}2W^{h\dagger}_{a'b'}\Bigr).
\tag{11}
$$

Pauli multiplication gives (9); tracing one memory removes the Pauli term, giving (10); the difference $r(Y_AX_B+X_AY_B)/4$ has eigenvalues $r/2,-r/2,0,0$, so the trace distance is $|r|/2$. (9) was confirmed by symbolic matrix computation (C01 of the note ledger) and the general-angle extension by C02 and V01. $\square$

### N3.3 Actual reading and the meaning of 75%

Measure $Y_A$ at $A$ and $X_B$ at $B$ and compare the results $a,b=\pm1$ afterwards — no quantum gate between the places, and the bases fixed before seeing the history:

$$
P(a,b|AB)=\frac{1+rab}4,\qquad P(a,b|BA)=\frac14 .
\tag{12}
$$

All outcomes at $r=1$:

| value at $A$ | value at $B$ | $A\to B$ | $B\to A$ |
|---:|---:|---:|---:|
| −1 | −1 | 1/2 | 1/4 |
| −1 | +1 | 0 | 1/4 |
| +1 | −1 | 0 | 1/4 |
| +1 | +1 | 1/2 | 1/4 |

In $A\to B$ the two values always agree; in $B\to A$ they agree half the time. Guessing "$AB$ if equal, $BA$ if different" succeeds with probability $3/4$ at equal priors, and the total variation $1/2$ of this measurement attains the optimum of (3). This does not mean one actual record always fixes the past: a differing pair fixes $BA$ in this model, but an equal pair is possible in both histories. **One record and the statistical reading of many repetitions must be distinguished.** Obtaining information about non-commuting observables from correlations of two sequentially coupled pointers is prior art — the sequential weak measurements of Mitchison–Jozsa–Popescu and the collision models of Campbell et al. are the closest lines; (9)–(12) is the finite, strong-coupling, postselection-free computation for this question, and its existence alone does not fix external novelty.

### N3.4 Conserved quantities and supplied resources

If the logical states share a charge, (7) conserves it: in the singly occupied subspace of two CAR modes,

$$
X=f_1^\dagger f_2+f_2^\dagger f_1,\qquad Y=-i(f_1^\dagger f_2-f_2^\dagger f_1),\qquad Z=n_1-n_2
\tag{13}
$$

commute with $n_1+n_2$ — an exact algebraic fact (C03), not a model supplying superpositions of different electric charges for free. **Charge conservation is not the full physical realisation of the device**: conserving bare energy too requires degenerate code states or a declared compensating energy source; the carrier's preparation and transport, the spin direction reference, the memories' initial $|+\rangle$, pulses and measurement devices are supplied resources; no claim of deriving total angular momentum, total energy and the Gauss constraint from S14.

## N4. Exact order distinguishability at arbitrary coupling strength

To check that this is not special to strong Pauli gates, use

$$
G_A=X_S\otimes P_{1,A}\otimes I_B,\qquad G_B=Z_S\otimes I_A\otimes P_{1,B},\qquad U_A=e^{-i\alpha G_A},\qquad U_B=e^{-i\beta G_B}
\tag{14}
$$

with dimensionless pulse areas $\alpha,\beta$ and the initial state (6).

**Proposition N2.** The distance between the final memories of the two orders is

$$
\boxed{D_{\rm order}(\alpha,\beta,r)=\frac{|r\sin\alpha\sin\beta|}2\sqrt{1+\cos^2\alpha+\cos^2\beta}.}
\tag{15}
$$

**Derivation.** $\Delta=\rho_{AB}-\rho_{BA}$ has non-zero entries only in the last row and column of the basis $00,01,10,11$; the three off-diagonal entries of the last row are

$$
(\Delta_{11,00},\Delta_{11,01},\Delta_{11,10})=-\frac{ir\sin\alpha\sin\beta}2(1,\cos\beta,\cos\alpha),
\tag{16}
$$

the last column their conjugates; the non-zero eigenvalues of such a Hermitian matrix are $\pm$ the length of that vector, giving (15). C02 checks (16) symbolically. $\square$

At $\alpha=\beta=\pi/2$ an identical known local phase correction on each memory recovers (7); being common to both orders it does not change the trace distance. No claim that the optimal measurement at general angles always equals the fixed measurement (12).

(15) also shows $D\le|r|/2$ in this **two-orthogonal-axes polarised family**: with $x=\sin^2\alpha$, $y=\sin^2\beta$, $4D^2/r^2=xy(3-x-y)\le1$. At small angles

$$
D_{\rm order}=\frac{\sqrt3}2|r\alpha\beta|\bigl[1+O(\alpha^2+\beta^2)\bigr].
\tag{17}
$$

For a completely mixed carrier (15) vanishes; more generally, **for a completely mixed carrier of any dimension and two controlled unitaries each acting once**, the memories after discarding the carrier do not distinguish the orders: with an initial product of memories and carrier, every memory matrix element that could change under reordering has a carrier trace equal by cyclicity. This two-gate statement does not cover three or more visits or a carrier initially entangled with the memories; W02 checks it numerically in dimensions 2, 3, 4.

## N5. How the record remains after writing

### N5.1 A persistent carrier phase is not necessary

After the carrier–memory interaction ends, any trace-preserving channel $\Phi_S$ on the carrier alone satisfies

$$
\operatorname{tr}_S\bigl[(\Phi_S\otimes{\rm id}_{AB})(\rho_{SAB})\bigr]=\operatorname{tr}_S\rho_{SAB} ,
\tag{18}
$$

so dephasing or discarding the carrier later leaves the written memories' marginals unchanged; conditional postselection or recoupling to the memories is outside this statement. This is the most direct formula separating "continuous phase preservation in time" from "maintenance of a record in space": phase and polarisation resources may be needed to write a good record at the front end, but **no conclusion follows that the same carrier's phase must keep being preserved after writing.**

### N5.2 It can be moved to suitable classical pointers

Dephase $A$ in the $Y$ basis and $B$ in the $X$ basis:

$$
\mathcal D_Y^A\otimes\mathcal D_X^B:\qquad \rho_{AB}\mapsto\frac{I+rY_AX_B}4,\qquad \rho_{BA}\mapsto\frac I4 .
\tag{19}
$$

The correlation of the first state survives and the $X_AY_B$ term of the second disappears, while the fixed-readout TV of (12) stays $|r|/2$: keeping only the **classical correlation** of the two local pointer values preserves the same order-discrimination performance, and no permanent entanglement between the memories is required. Dephasing both memories in the $Z$ basis instead sends both states to $I/4$ and erases the order: "recorded in space" alone does not guarantee stability — which physical observable serves as pointer and whether environmental noise preserves its value are needed, connecting to quantum Darwinism and spectrum-broadcast-structure work on readability and stability of records.

### N5.3 The derived formula for actual certification

After the classical pointer transformation let independent value flips occur at $A$ and $B$ with probabilities $e_A(T),e_B(T)$, and let a loss of probability $p_\varnothing$ leave the same history-independent failure flag. In this **declared storage channel**

$$
\boxed{D_{\rm stored}(T)=\frac{(1-p_\varnothing)|r|}2|1-2e_A(T)|\,|1-2e_B(T)|.}
\tag{20}
$$

Each independent bit flip multiplies the mean of the pointer product by $1-2e_j$, and the common failure block contributes nothing to the difference; failures are neither discarded nor normalised away.

If the trace-distance error between actual preparation, transport, coupling, readout and this effective model is at most $\eta_{AB},\eta_{BA}$ per history,

$$
\boxed{D^{\rm physical}_{\rm readable}(T)\ge\Bigl[\frac{(1-p_\varnothing)|r|}2|1-2e_A(T)|\,|1-2e_B(T)|-\eta_{AB}-\eta_{BA}\Bigr]_+ ,}
\tag{21}
$$

$[x]_+=\max(0,x)$, by the reverse triangle inequality on the same fixed total output, inheriting the actual-readout-error connection of the earlier seed. For $r=1$, $e_A=0.1$, $e_B=0.2$, $p_\varnothing=0.1$ the effective-model TV is exactly $0.216$; a physical bound that the actual error sum is smaller is needed for a positive readable lower bound.

(20) uses independence of the two errors, symmetric flips of memory values and history-independent loss; general noise or history-dependent loss requires recomputing the actual channel. The identification of $r$ with the seed's $\Gamma$ is not yet made here (Theorem 5 of the main text supplies it).

## N6. When spatial accumulation improves recovery accuracy

Prepare $k$ **new carrier–memory pairs** undergoing the same unknown order, with outputs conditionally independent given the history. At $r=1$ the pointer products $s_i=a_ib_i$ satisfy

$$
AB:\ s_i=+1\ \text{always},\qquad BA:\ s_i=\pm1\ \text{with probability }1/2\text{ each}.
\tag{22}
$$

Guess $BA$ if any $s_i=-1$, else $AB$; the optimum of the full outcome distribution is

$$
\boxed{P_{{\rm err},k}=2^{-(k+1)},\qquad D_k=1-2^{-k}.}
\tag{23}
$$

With an independent common loss $p_\varnothing$ per pair and all flags retained,

$$
\boxed{P_{{\rm err},k}=\frac12\Bigl(\frac{1+p_\varnothing}2\Bigr)^k,}
\tag{24}
$$

the probability that no opposite sign is ever observed in $BA$; if every outcome is lost the likelihoods are equal and either decision has the same average error. C04 of the note ledger checks finite cases by exact integer/rational enumeration.

| independent memory pairs $k$ | optimal error without loss |
|---:|---:|
| 1 | 25% |
| 2 | 12.5% |
| 4 | 3.125% |
| 8 | 0.1953125% |

The important distinction is between **making more records and copying a record already made**: copying one $s$ as $s,s,\ldots,s$ creates no new evidence and the TV stays $1/2$. (23) does not mean a unique past event can be re-run afterwards; it needs enough independent carriers and memories to have participated when the event was recorded, or a repeatable identical process. And gathering all records at $A$ without the corresponding values at $B$ does not read the order in this example: "many observers each seeing one piece know the same event" (redundant records) and "pieces must be gathered to know the order" (distributed records) are different performances.


## N7. The general derivation: integrals carry accumulated exposure, iterated integrals carry order

### N7.1 Integrals versus iterated integrals

At finite cutoff or on a bounded code write

$$
H_h(t)=\sum_{a=1}^mu_a^h(t)G_a,\qquad \mathcal L_a(\rho)=-i[G_a,\rho],
\tag{25}
$$

with fixed dimensionless Hermitian $G_a$ and real functions $u_a$ of inverse-time dimension. This assumes a fixed operator expansion; with free propagation, the interaction-picture time dependence or the free Hamiltonian must be included in the expansion. Define

$$
I_a[h]=\int_0^{T_h}u_a^h(t)\,dt,\qquad I_{ab}[h]=\int_{0<t_1<t_2<T_h}u_a^h(t_1)u_b^h(t_2)\,dt_1dt_2,
\tag{26}
$$
$$
\mathsf A_{ab}[h]=\frac{I_{ab}[h]-I_{ba}[h]}2\qquad(a<b).
\tag{27}
$$

$I_a$ is the total exposure to interaction $a$; $\mathsf A_{ab}$ is the asymmetry between "$a$ before $b$" and its reverse. For non-overlapping single pulses of areas $\alpha,\beta>0$,

$$
\mathsf A_{ab}(AB)=+\alpha\beta/2,\qquad \mathsf A_{ab}(BA)=-\alpha\beta/2 .
\tag{28}
$$

With the accumulated coordinates $x_a(t)=\int_0^tu_a(s)ds$,

$$
\mathsf A_{ab}=\frac12\int(x_a\,dx_b-x_b\,dx_a),
\tag{29}
$$

an oriented area in accumulated-exposure space — **not automatically an area of physical three-space**; it is the dynamical coefficient deciding how an event is left in spatial memories. These iterated integrals are the standard mathematics of path signatures and the Magnus expansion; they are used to separate order information from total integrals and are not claimed as new (Blanes–Casas–Oteo–Ros; Hambly–Lyons).

### N7.2 Proposition N3: second-order response of the spatial record

With $\mathcal L_I=\sum_aI_a\mathcal L_a$, the Dyson expansion and $I_{ab}+I_{ba}=I_aI_b$, $I_{aa}=I_a^2/2$ give

$$
\boxed{\rho_h^F=\mathcal R_F\Bigl[\rho_0+\mathcal L_I\rho_0+\tfrac12\mathcal L_I^2\rho_0+\sum_{a<b}\mathsf A_{ab}[h]\,[\mathcal L_b,\mathcal L_a]\rho_0\Bigr]+R_3^F[h],}
\tag{30}
$$

with the commutator sign

$$
[\mathcal L_b,\mathcal L_a](\rho)=[[G_a,G_b],\rho].
\tag{31}
$$

Comparing two histories with equal $I_a$, the terms depending only on accumulated exposure cancel and at second order

$$
\boxed{\Delta\rho_F=\sum_{a<b}\Delta\mathsf A_{ab}\,\mathcal R_F\bigl([[G_a,G_b],\rho_0]\bigr)\ +\ \text{terms of order three and higher.}}
\tag{32}
$$

**The minimal condition for a difference of process order to be left in a spatial record** is not merely $[G_a,G_b]\ne0$: the commutator must act on the initial state, survive the removal of inaccessible degrees of freedom, and be caught by the admissible readout.

### N7.3 A computable remainder instead of "small terms"

Let

$$
\Lambda_h=2\sum_a\|G_a\|\int|u_a^h(t)|\,dt,\qquad \mathfrak r_3(\Lambda)=e^\Lambda-1-\Lambda-\Lambda^2/2 ;
\tag{33}
$$

then

$$
\|R_3^F[h]\|_1\le\mathfrak r_3(\Lambda_h)\le e^{\Lambda_h}\Lambda_h^3/6 .
\tag{34}
$$

**Derivation.** $\|\mathcal L_a(X)\|_1\le2\|G_a\|\|X\|_1$ applied to each Dyson term bounds the $n$-th order by $\Lambda_h^n/n!$; summing from the third order and using trace-norm contractivity of the output map on Hermitian operators gives (34). Bounded generators and integrable $u_a$ are used; this does not apply to unbounded QFT. $\square$

If the two pulses $AB$ and $BA$ have the same $\Lambda$ bound,

$$
D_F(AB,BA)\ge\Bigl[\frac{|\alpha\beta|}2\bigl\|\mathcal R_F([[G_A,G_B],\rho_0])\bigr\|_1-\mathfrak r_3(\Lambda)\Bigr]_+ .
\tag{35}
$$

For a restricted measurement the leading difference obtained by that measurement replaces the norm; (35) does not supply an accessible optimal effect where none was specified.

For (14) with $r=1$, $\alpha=\beta=\theta$, $\Lambda=4\theta$ and the leading term of (35) is $\sqrt3\theta^2/2$; compared with the direct unitary computation:

| $\theta$ | exact $D$ | second-order leading term | lower bound (35) |
|---:|---:|---:|---:|
| 0.01 | 0.0000865968 | 0.0000866025 | 0.0000758283 |
| 0.02 | 0.000346318 | 0.000346410 | 0.000259342 |
| 0.05 | 0.00216146 | 0.00216506 | 0.000762305 |
| 0.10 | 0.00860270 | 0.00866025 | 0 |

The last row does not mean a vanishing signal, only that this conservative remainder bound cannot certify positivity there; the decimals are floating evaluations, not interval certificates.

### N7.4 Actual inversion is a rank problem of the response matrix

With fixed observables $M_\mu$ read from the memories and $y_\mu$ the signal after removing the contributions of the known accumulated $I_a$, (30) gives

$$
y_\mu=\sum_{a<b}K_{\mu,ab}\mathsf A_{ab}+\epsilon_\mu,\qquad K_{\mu,ab}=\operatorname{tr}\bigl[M_\mu\,\mathcal R_F([[G_a,G_b],\rho_0])\bigr] .
\tag{36}
$$

If $K$ has full column rank on the chosen order coordinates, the least-squares inversion error is

$$
\|\widehat{\boldsymbol{\mathsf A}}-\boldsymbol{\mathsf A}\|_2\le\frac{\|\boldsymbol\epsilon\|_2}{\sigma_{\min}(K)} ,
\tag{37}
$$

the standard linear inverse-problem estimate. Order differences in the null space of $K$ cannot be recovered by this readout, and those along small singular values are noise-sensitive; if the $I_a$ are unknown too, exposure and order must be estimated jointly and (37) alone does not solve the whole inverse problem.

## N8. How far recovery can go

### N8.1 Commuting orders can produce identical records

With equal initial state and output, exchanging two adjacent commuting unitaries leaves the total result unchanged; if all events commute and couplings and free propagation are otherwise identical, only total exposures remain. Non-commutation alone is not enough either: applying $X$ and $Z$ to a carrier without recording devices gives $ZX=-XZ$ but identical final density matrices, the difference being a global phase; in (7) that sign attaches conditionally to different memory components and becomes a readable relative phase (W01). In relativistic field theory, assigning observer-dependent coordinate orders to two causally separated local operations creates no new physical history; under proper causal composition conditions those orders give the same observations — Fewster–Verch Theorem 3.5.

In bounded lattice models satisfying a verified Lieb–Robinson condition, the time-displaced commutator of distant regions is controlled by

$$
\|[G_A(t),G_B]\|\le C_{AB}e^{-\mu(d(A,B)-v|t|)},
\tag{38}
$$

with constants matched to the system and supports and the trivial bound preferred where the right side is large; combined with

$$
D_F(AB,BA)\le\|e^{-i\beta G_B}e^{-i\alpha G_A}-e^{-i\alpha G_A}e^{-i\beta G_B}\|\le|\alpha\beta|\,\|[G_A,G_B]\|
\tag{39}
$$

(the last from the Duhamel representation integrating the commutator of the two exponentials twice), this is a conditional upper bound: no large order signal at distances and times the actual propagation does not allow. (38) is a lattice locality theorem, not a derivation of the physical light speed from S14 (Nachtergaele–Sims).

### N8.2 Second-order records cannot recover every history

The unit-area pulse histories $ABBA$ and $BAAB$ share $I_A=I_B=2$, $I_{AB}=I_{BA}=2$, so records up to second order cannot separate them; third-order iterated integrals differ — e.g. the difference of $I_{AAB}$ is $-1$, including the $1/n!$ of iterated integrals within one pulse (W05, exact rationals). Yet even when higher iterated integrals differ, a specific finite operator representation may re-merge the histories: for the Pauli gates of (7), $C_XC_ZC_ZC_X=C_ZC_XC_XC_Z=I$. **The mathematical signature of a process and the record left in an actual device do not carry the same information.**

Hambly–Lyons' theorem says that the **full infinite signature** of a bounded-variation path determines the path up to tree-like equivalence; that uniqueness cannot be transferred to a few coefficients read from finitely many pointers, unitaries compressed into finite matrices, or a once-observed spatial structure. Iterated integrals are also invariant under monotone reparametrisation: without a separate clock coordinate or the time scale of free dynamics, knowing part of the order gives neither absolute times nor durations; recovery with additional interval data is a different task.

### N8.3 Capacity of a finite memory and a single observation

To distinguish $M$ histories without error in one shot with a memory of dimension $d_F$, the record supports must be orthogonal, so

$$
M\le d_F .
\tag{40}
$$

Storing perfectly all records of length $L$ with $q$ values per event requires $q^L\le d_F$; restricted or compressible history families are not excluded. Infinitely many distinct density matrices parametrised by real numbers exist, but they cannot all be read exactly from a single copy; exact knowledge of density matrices or correlation functions usually means many copies or extra calibration data. The recovery formulas of this note do not assume **unlimited tomography of one state of the universe**: a single memory has the error of (3), and improvement by repetition needs the resources of (22).

## N9. Concrete connection to Z-Spin: does the commutator of currents remain as a record?

### N9.1 The actual starting point and the proposed additional coupling

S14 v2.1's typed action contains $\bar\psi i\gamma^\mu D_\mu\psi$ and the specified gauge carriers; M70 v1.5 treats, within its declared scope, the candidate positive-energy boundary Dirac band and the current's emission vertex. Neither yields a prepared record qubit or controlled gate automatically. The **effective coupling hypothesis** for a spatial record is therefore written as

$$
H_{\rm record}(t)=\sum_au_a(t)\,P_{1,a}\otimes J_a,\qquad J_a=\Pi\widehat{\mathcal J}_a\Pi\big|_{\mathcal C},
\tag{41}
$$
$$
\widehat{\mathcal J}_a=\int d^2x\,dy\ f_a(\mathbf x,y)\,\psi^\dagger(\mathbf x,y)(\mathbf n_a\cdot\boldsymbol\sigma)\psi(\mathbf x,y),
\tag{42}
$$

with $f_a$ the real spatial coupling profile at place $a$, $\mathbf n_a$ the chosen current component, $\Pi$ the projection onto the carrier code $\mathcal C$; charge and coupling units may be absorbed in $u_a$; bilinears joining different gauge representations must carry the required index contractions and transport; (42) refers to the neutral bilinear of one charge component. With M70's normalised boundary spinor and packets $\phi_i(\mathbf k)$, the candidate two-dimensional code matrix is

$$
(J_a)_{ij}=\int d^2k\,d^2k'\ \phi_i^*(\mathbf k')\phi_j(\mathbf k)\,u_+^\dagger(\mathbf k')(\mathbf n_a\cdot\boldsymbol\sigma)u_+(\mathbf k)\,\mathfrak f_a(\mathbf k-\mathbf k'),
\tag{43}
$$
$$
\mathfrak f_a(\mathbf q)=\frac1{(2\pi)^2}\int d^2x\,dy\ f_a(\mathbf x,y)\rho(y)e^{i\mathbf q\cdot\mathbf x},
\tag{44}
$$

with plane Fourier normalisation $(2\pi)^{-1}$ and $\int\rho(y)dy=1$ — a proposal for computing the matrix from actual packets and spatial profiles, not a substitution of M70's inclusive emission rate for a record rate.

### N9.2 Proposition N4: the polarisation–current triple product of order sensitivity

On a two-state code, expanding

$$
J_a=j_{a0}I+\mathbf j_a\cdot\boldsymbol\sigma,\qquad \rho_S=(I+\mathbf r\cdot\boldsymbol\sigma)/2,
\tag{45}
$$

one has

$$
[J_a,J_b]=2i(\mathbf j_a\times\mathbf j_b)\cdot\boldsymbol\sigma,\qquad \kappa_{ab}:=\mathbf r\cdot(\mathbf j_a\times\mathbf j_b),
\tag{46}
$$

and with $G_a=J_a\otimes P_{1,a}$, $G_b=J_b\otimes P_{1,b}$ and initial memories $\sigma_M=|++\rangle\langle++|$,

$$
\operatorname{tr}_S\bigl([[G_a,G_b],\rho_S\otimes\sigma_M]\bigr)=2i\kappa_{ab}[P_{1,a}P_{1,b},\sigma_M],
\tag{47}
$$

so the leading distinguishability when the two pulses are exchanged is

$$
\boxed{D^{(2)}_{\rm order}=\frac{\sqrt3}2|\alpha\beta\kappa_{ab}|.}
\tag{48}
$$

**Derivation.** The Pauli commutator and $\operatorname{tr}(\rho_S\boldsymbol\sigma)=\mathbf r$ give (47); for $P=P_{1,a}P_{1,b}$, $\langle P\rangle=1/4$, $\operatorname{var}P=3/16$, and for a pure state $\|[P,\sigma_M]\|_1=2\sqrt{\operatorname{var}P}=\sqrt3/2$; substitute in (32). (47) for general vectors was verified symbolically (C06). $\square$

The triple product is invariant under a common code basis change; comparing code bases at different places requires the actual transport map first; code-basis invariance is not full gauge invariance. (48) shows that **a non-zero polarisation–current triple product is a sufficient leading-order condition for a weak-coupling order record**; $\kappa_{ab}=0$ does not kill order records at all orders — other initial states, higher orders or other memory couplings may produce a signal.

### N9.3 The first obstruction: the positive band at fixed momentum is one state

In M70's

$$
h(\mathbf k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z,\qquad E(\mathbf k)=\sqrt{|\mathbf k|^2+M^2},
\tag{49}
$$

the positive-energy projection $P_+(\mathbf k)$ at fixed $\mathbf k$ has rank $1$, so

$$
P_+\sigma_xP_+=\frac{k_x}EP_+,\qquad P_+\sigma_yP_+=\frac{k_y}EP_+ :
\tag{50}
$$

within that one state the currents act as numbers, and the pre-projection $[\sigma_x,\sigma_y]=2i\sigma_z$ cannot be inserted into (48). **The present minimal missing object is a code carrying at least two states on which the actual local currents act non-commutatively, together with control of its propagation and leakage.** Two momenta of equal energy, several boundary channels or a packet space including recoil are candidates; which one the actual occupation and boundary conditions of S14 select is open, and renaming one large spin into the code does not solve it.

### N9.4 The decisive counterexample: projection can create spurious non-commutativity

With $Q=I-\Pi$, exactly

$$
\boxed{[\Pi A\Pi,\Pi B\Pi]=\Pi[A,B]\Pi-\Pi AQB\Pi+\Pi BQA\Pi .}
\tag{51}
$$

So even if $[A,B]=0$ on the full space, the projected matrices fail to commute whenever the two paths through the discarded degrees of freedom differ: **a projected commutator alone cannot certify an actual order signal.** Concretely, on the four-dimensional single-particle space of two positions and two spin components let

$$
A=|0\rangle\langle0|_{\rm pos}\otimes X,\qquad B=|1\rangle\langle1|_{\rm pos}\otimes Y,
\tag{52}
$$

which act at different positions and commute. With the finite positive-band spinors

$$
u_+=\frac{(3,1)^{\mathsf T}}{\sqrt{10}},\qquad u_-=\frac{(3,-1)^{\mathsf T}}{\sqrt{10}}
\tag{53}
$$

(positive eigenstates of $(3X+4Z)/5$ and $(-3X+4Z)/5$) and the orthonormal code

$$
|\phi_+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2}\otimes u_+,\qquad |\phi_-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}\otimes u_-,
\tag{54}
$$

one finds

$$
A_{\rm code}=\frac3{10}Z,\qquad B_{\rm code}=\frac3{10}Y,\qquad [A_{\rm code},B_{\rm code}]=-\frac{9i}{50}X :
\tag{55}
$$

the full commutator has norm $0$, the code commutator norm $9/50=0.18$. Without free propagation, two local pulses give an exactly commuting total unitary and no order signal; the discarded paths in (51) cancel the code non-commutativity exactly (C05, W07). This two-position model claims no realisation of the M70 continuum; it is the exact counterexample to **closing a finite code before actual spatial locality**. The carrier's causal propagation, dynamical isolation by energy selection and the physical cost of added control must be included before (41) can be trusted; if projections are repeated to protect the code, the projecting apparatus is a new input.

### N9.5 Weak coupling does not remove this problem automatically

The order signal (48) is $O(\alpha\beta)$, and the omitted paths of (51) can contribute at the same second order; reducing the coupling shrinks both and does not improve the signal-to-error ratio. On a bounded space with off-code coupling norm $b=\|QH\Pi\|$, the earlier seed's sufficient formula controls the leakage error by $b^2T^2$ when the output actually flags in-code/out-of-code; without the flag, the full error including coherence can be $O(bT)$; which bound applies to the actual reading must be decided first.

The positive physical certification target of Z-Spin is finally

$$
\boxed{\text{order contrast of the admitted spatial readout}\ >\ \text{sum of transport, projection, leakage, environment and detection errors},}
\tag{56}
$$

and (21), (35), (43), (48), (51) convert that target into computable obligations.

## N10. Does more space automatically improve the record?

### N10.1 The positive route from external work

The 2026 preprint of Cao–Nussinov shows that when the initial recording process makes the conserved-quantity densities of the environment differ between branches, and subsequent subsystem thermalisation satisfies certain large-deviation properties, small environment fragments can hold distinguishable records; the key input is not energy conservation alone but **branch-dependent conserved-density differences and subsystem statistics able to read them**, and the paper states that the initial broadcasting interaction changing macroscopic densities is itself a strong input. This supports reading record persistence as a spatial accumulation structure, but "a finite Z-Spin carrier passed locally" alone does not satisfy that paper's macroscopic initial-record condition.

### N10.2 Proposition N5: the limit of diluting a fixed energy contrast over space

Quantify the difference in the simplest model: $N$ memory cells with $H_M=\omega\sum_in_i$ and the two histories' records as independent diagonal states

$$
\tau_\pm^{(N)}=\bigotimes_{i=1}^N\operatorname{diag}(1-p_\pm,p_\pm),\qquad p_\pm=\tfrac12\pm\delta,\quad 0<\delta<\tfrac12 .
\tag{57}
$$

The mean total-energy difference is

$$
\Delta E=2\omega N\delta .
\tag{58}
$$

The optimal distinguishability of $n$ cells is exactly the binomial TV,

$$
D_n=\frac12\sum_{j=0}^n\binom nj\bigl|p_+^j(1-p_+)^{n-j}-p_-^j(1-p_-)^{n-j}\bigr| ,
\tag{59}
$$

since each bit string's likelihood ratio depends only on the occupation count $j$. The Bernoulli relative entropy (natural logarithm) is

$$
D_{\rm KL}(p_+\|p_-)=2\delta\ln\frac{1+2\delta}{1-2\delta},
\tag{60}
$$

and additivity plus Pinsker's inequality give

$$
D_n\le\min\Bigl\{1,\sqrt{\tfrac n2D_{\rm KL}(p_+\|p_-)}\Bigr\}\le\min\Bigl\{1,\frac{2|\delta|\sqrt n}{\sqrt{1-4\delta^2}}\Bigr\},
\tag{61}
$$

using $\ln[(1+x)/(1-x)]\le2x/(1-x^2)$ on $0<x<1$ (bounding the integrand of $2\int_0^x(1-t^2)^{-1}dt$ by its endpoint value); Pinsker is standard (Watrous Thm. 5.15). So $D_n\ge1-\varepsilon$ requires

$$
\boxed{n\ge(1-\varepsilon)^2\Bigl[\Bigl(\frac{\omega N}{\Delta E}\Bigr)^2-1\Bigr].}
\tag{62}
$$

With $\Delta E$ fixed and $N$ increased, the needed fragment size grows like $N^2$ and eventually exceeds $N$ itself; even reading everything,

$$
D_N\le\frac{|\Delta E|}{\omega\sqrt N}\frac1{\sqrt{1-(\Delta E/\omega N)^2}}\longrightarrow0 .
\tag{63}
$$

**Using more space does not by itself turn the same finite contrast into a better record**; if the signal is diluted below the background fluctuations of each place, even the total readout worsens. With $\Delta E/\omega=4$ fixed and all cells read:

| $N$ | exact binomial TV | Pinsker bound |
|---:|---:|---:|
| 64 | 0.381896 | 0.500326 |
| 256 | 0.197236 | 0.250010 |
| 1024 | 0.0994527 | 0.125000 |
| 4096 | 0.0498323 | 0.0625000 |

Conversely with $\delta$ fixed the energy **contrast** (58) grows with $N$; a median-threshold readout of the occupation count and a direct Chernoff bound give

$$
P_{{\rm err},n}\le e^{-2n\delta^2},\qquad D_n\ge[1-2e^{-2n\delta^2}]_+ ,
\tag{64}
$$

by an exponential Markov inequality on the occupation tail with optimised parameter, giving $(2\sqrt{p_+(1-p_+)})^n=(1-4\delta^2)^{n/2}\le e^{-2n\delta^2}$ on each branch, including odd cell counts and ties at the threshold. Fixed density difference and fixed total contrast are different resource limits; (61)–(64) are standard concentration/information inequalities applied to this comparison model — a meeting point with the large-deviation assumptions of the external work, not a replacement for it.

### N10.3 The exact scope of this limit

(62) is a necessary condition for the **independent, diagonal, uniform-density record model** (57), not a universal energy lower bound for general spatial records, correlated states, topological memories or metastable amplifiers; the model already contains an $O(N)$ mean-energy background and $\Delta E$ is the contrast between two such branches, not the work of recording or the whole initial low-entropy resource. An immediate counterexample: the two-cell states $|10\rangle$, $|01\rangle$ have the same energy $\omega$ but are perfectly distinguishable — the information is in the **spatial arrangement** (W04). Even with conserved quantities one must decide whether the record sits in the total density, a pattern, correlations, or boundary/topological structure. The earlier seed's $R_\varepsilon(1-\varepsilon)\le\langle N_\gamma\rangle$ is likewise a bound for a specified passive output-photon class and is not identified with processes in which one passing photon marks several matter memories or with additional amplifiers.

## N11. Thought experiments and the concrete content of the breakthrough

### N11.1 The event forgotten, the footprint kept

Write the order record of (7), move it to classical pointers by (19), then erase the carrier's polarisation and phase completely, and check whether reading the pointer values at the same places keeps the order-discrimination performance; predictions (18) and (20). This **separates the resources for writing a record from those for storing one already written**; success does not prove the origin of time — it removes the demand that the original carrier's phase persist for ever in order to record.

### N11.2 Nothing at each place, something at two places

Distinguish a group accessing only one place from a group comparing the values of two places; (9) predicts $D^{(1)}=0$ and $D^{(2)}=|r|/2$ — a direct test that order is stored as a relation between places rather than a value at one place, with no superluminal signalling and no inference of causation from correlation alone; the two devices interacted causally with the same carrier in the past and the family of histories and preparation are known.

### N11.3 Same exposure, different order, different spatial trace

Compare $AB$ and $BA$ at fixed $I_a$; at weak coupling the signal must scale with $\alpha\beta$ and the triple product $\kappa_{ab}$; reversing the polarisation or removing one coupling tests the direction and order of the leading response; exposure and preparation are calibrated together so that differences due to event content or coupling strength are not called order signals. The actual current matrices are computed before and after projection; if the omitted paths of (51) cancel the whole signal, the effective model is discarded — a physical test to pass before pretty numbers on a small code.

### N11.4 Does a larger space accumulate or dilute the record?

Compare spreading the same input contrast over a larger environment with increasing resources so that each place keeps a fixed contrast; (63) and (64) predict opposite trends, discriminating the reading of "much space" as "much independent evidence".

### N13. The present position of the note's physical obligations

The note's obligations — actual carrier, spatial path, two current vertices, polarisation, readout, common leakage and noise — correspond to Sections 6–9 of the main text and Appendix S8. The preparation, transport and storage of the declared models are complete; the actual apparatus and states selected by S14 are left open. The response rank of N3 fixes the observational equivalence classes of the chosen experiment; that the upstream current is given does not by itself recover the whole history uniquely.


---

## Appendix L. Inherited literature and the range of what was checked

The tables below preserve the wide literature lineage used by the earlier seed and note. Past markers such as "checked directly" and version labels are **records of the time each source was consulted**, not claims that everything was re-read for this version. The actual re-comparison of the present central theorems is in Section 12. No inherited source is treated as independently audited in full.

### L1. Lineage of the seed's literature comparison

#### L-S10.1 Sources checked directly at v1.5 (comparison date 2026-09-13 UTC)

| ID and source | Location actually checked | Effect on the present conclusions |
|---|---|---|
| E17. Scheel–Buhmann, *Macroscopic quantum electrodynamics — concepts and applications* | [text](https://arxiv.org/html/0902.3586v1), §§2.2, 4.1, (334)–(340) | electromagnetic Green tensor, dipole emission rate and PV shift, with the Markov step explicit; MIC3 is a comparison specialisation of an imported formula, not a full S14 computation |
| E18. Trushechkin, *Unified GKLS quantum master equation beyond the secular approximation* | [text](https://arxiv.org/pdf/2103.12042), §II (4)–(6), §III A (7)–(8) | distinction of distinct fixed Bohr frequencies and near-degenerate clusters; the sentence calling V18 a strict Davies limit repaired; W10 separates the two models |
| E19. Pazy, *Calculation of pure dephasing for excitons in quantum dots* | [text](https://arxiv.org/pdf/cond-mat/0212509), (2.4), §III | the exact independent-boson dephasing exponent is prior; ZF3 is a direct re-derivation of the imported structure and excludes an overstatement of finite-time blindness at $C(0)=0$ |
| E20. Dusson–Sigal–Stamm, *The Feshbach–Schur map and perturbation theory* | [text](https://arxiv.org/pdf/2105.02058), Theorem 1.2, (1.10)–(1.16) | block resolvents and energy-dependent self-energy are known; FT7 is not counted as a new general reduction theorem |
| E21. Burgarth–Facchi–Gramegna–Yuasa, *One bound to rule them all: from Adiabatic to Zeno* | [text](https://arxiv.org/pdf/2111.08961), Lemma 1, Proposition 1, Appendix A Corollary 6 (A16) | Duhamel-based propagator bounds are prior; ERR1 is classified as an application/direct proof for a specific flagged output, and the misreading extending it to coherent outputs is rejected by W11 |

The zero-frequency and Coulomb-projection points of upstream M69 §§C.3–C.4 were checked before the external search; an earlier "not found in the index" record is not read as absence from that source.

#### L-S10.1b Sources checked directly at v1.6 (audit conflicts E22–E24, B14 lineage E25–E27; dates 2026-09-13/14 UTC)

"Equation location" means the equation was compared directly; "abstract/bibliographic" means only that level was checked.

| ID and source | Location checked | Effect on the present conclusions |
|---|---|---|
| E22. Kambs–Becher, *Limitations on the indistinguishability of photons from remote solid state sources*, NJP 20, 115003 (2018) | [journal](https://iopscience.iop.org/article/10.1088/1367-2630/aaea99) · [arXiv:1806.08213](https://arxiv.org/abs/1806.08213); equation (27): HOM visibility of two photons with different frequencies, lifetimes and pure dephasing | at zero pure dephasing (27) equals $\gamma_1\gamma_2/[(\gamma_1+\gamma_2)^2/4+\Delta\omega^2]$, the $\vert G_{qr}\vert ^2$ of the K5 time factor. **The K5 time factor is IMPORTED**; the work here places it in the sector kernel (SPECIALIZED) |
| E23. Legero–Wilk–Hennrich–Rempe–Kuhn, *Quantum beat of two single photons*, PRL 93, 070503 (2004) | [journal](https://dx.doi.org/10.1103/PhysRevLett.93.070503) · [arXiv:quant-ph/0406096](https://arxiv.org/pdf/quant-ph/0406096); abstract/bibliographic | time-resolved interference of photons of different frequencies is prior; supports that the $\omega_q-\omega_r$ dependence of K5 is not new |
| E24. Schöll et al., *Crux of Using the Cascaded Emission of a Three-Level Quantum Ladder System to Generate Indistinguishable Photons*, PRL 125, 233605 (2020) | [journal](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.125.233605); abstract/bibliographic | the upper-level lifetime limits the indistinguishability of the lower photon; the "absorbing cascade recursion" of K6 is the sector version of this structure; equation-level comparison incomplete (hypothesis: same structure) |
| E25. Bartlett–Rudolph–Spekkens–Turner, *Degradation of a quantum reference frame*, NJP 8, 58 (2006) | [journal](https://iopscience.iop.org/article/10.1088/1367-2630/8/4/058) · [abstract](https://research-information.bris.ac.uk/en/publications/degradation-of-a-quantum-reference-frame/); spin-$j$ directional reference and the phase reference of an energy-bounded oscillator mode, lifetime quadratic in size | the flat $L_B$ (bounded phase reference) and su(2) $L_S$ (spin-$j$ reference) classification corresponds to two standard models; B14's "choice of reference type" is not a new concept; the work here computes the sector spectra and record dynamics of the two types; the quadratic lifetime scaling has a different origin and is not identified |
| E26. Maldonado–Rodriguez–Türeci, *Quantum theory of the Josephson junction between finite islands*, arXiv:2504.13779 | the earlier exact $S_x$ citation corrected by direct comparison with (6); [text](https://arxiv.org/html/2504.13779v1) | Weyl midpoint edges differ from spin edges (C14); only the semicircle form and charging structure are shared; not used as evidence of an exact su(2) realisation |
| E27. Milburn–Corney–Wright–Walls, *Quantum dynamics of an atomic Bose–Einstein condensate in a double-well potential*, PRA 55, 4318 (1997) | [journal](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.55.4318); abstract: two-mode approximation, collapse/revival of mean-field oscillations | two-mode tunnelling at total number $B$ ($S_\pm$ in the Schwinger representation) is another realisation of the su(2) source; equation locations not checked (access limited) |
| (bibliographic) Pegg–Barnett, *Phase properties of the quantized single-mode electromagnetic field*, PRA 39, 1665 (1989) | [journal](https://link.aps.org/doi/10.1103/PhysRevA.39.1665); bibliographic only | pointer for classifying the earlier $\vert \beta_B\rangle$ as a truncated phase state; not load-bearing |

The E22 check changed the seed's earlier qualification: the K5 previously marked "high WW-subsumption risk" is subsumed at equation level by the HOM-visibility literature, more specifically than by WW.

#### L-S10.1c Source comparisons and nearest prior work at v1.7 (date 2026-09-14 UTC)

| ID and source | Location checked | Exact relation to B15–B17 and remaining difference |
|---|---|---|
| E26 re-audited. Maldonado–Rodriguez–Türeci | [arXiv HTML v1](https://arxiv.org/html/2504.13779v1), (1), (6) | the Weyl edge of (6) differs from B14's spin edge; the common semicircle form is not evidence of finite-model identity |
| E25 re-read. Bartlett–Rudolph–Spekkens–Turner | [text](https://arxiv.org/pdf/quant-ph/0602069), §II longevity definition, directional/phase reference analysis | their lifetime task counts repeated measurements and backaction; B15 is storage **time** under a closed Hamiltonian, so no violation or improvement of their quadratic law is claimed |
| E28. Christandl–Datta–Ekert–Landahl, *Perfect state transfer in quantum spin networks* | [text](https://arxiv.org/pdf/quant-ph/0309131), p.3 (13)–(15) | the correspondence of edges $\lambda\sqrt{n(N-n)}/2$ with $\lambda S_x$ is an exact precedent; B15's parent-matrix spin mapping is IMPORTED; the added task is the common lower bound of the moving compressed window, supplied sector coherence and C6 record |
| E29. Groenland–Schoutens, *Many-body strategies for multi-qubit gates — quantum control through Krawtchouk chain dynamics* | [text](https://arxiv.org/pdf/1707.05144), §II B (6)–(7) | Krawtchouk couplings and fermion-chain representations are prior; no evidence that M70 naturally selects an arbitrary maximal-spin source occupation |
| E30. R. Sasaki, *Multivariate Krawtchouk polynomials as Birth and Death polynomials* | [text](https://arxiv.org/pdf/2305.08581), §2.1 (2.2), (2.7)–(2.8) | birth–death rates, stationary weights and symmetric similarity are prior; tool lineage of B15-11; that source does not prove the whole C6 readout inequality of moving windows |
| E31. Koch et al., *Charge-insensitive qubit design derived from the Cooper pair box* | [text](https://arxiv.org/pdf/cond-mat/0703002), §II B (2.5), §V charge noise | exponentially small charge dispersion is well known; B15's variables are the finite-source binomial tail and compensator bandwidth, its task the readout of sector coherence, but this difference alone does not establish non-subsumed novelty |

Mapping the nearest sources, the broad slogan "exponentially long lifetime in a finite reference" cannot be a novelty claim; times, numbers of uses and $B,N,E_J/E_C$ from different tasks are not compared as the same resource variable. B15's potential contribution is **the exact unification in one conserving code where one parent-matrix tail governs band energy, vector overlap and fixed readout, connected to preparation, electrostatics and all-outcome cooling**; whether that unification is an independent contribution beyond direct specialisation of standard compression/localisation techniques remains under external review.

#### L-S10.1d Source comparisons and nearest prior work at v1.8 (date 2026-09-14 UTC)

| ID and source | Location checked | Exact relation to B18–B19 and remaining difference |
|---|---|---|
| E32. A. Bovier, *Metastability: a potential theoretic approach* (ICM 2006) | [text](https://wt.iam.uni-bonn.de/fileadmin/WT/Inhalt/people/Anton_Bovier/publications/icmbovier.pdf), Thm. 4.7 $E_x\tau_J=Q(A(x))/{\rm cap}(x,J)(1+o(1))$, Cor. 5.7 $\lambda_i={\rm cap}_{x_i}(M_{i-1})/Q(A(x_i))(1+O(\delta))$ | B18-T2(iii)'s $\widetilde F_l(1-r_l)$ is the one-dimensional value of this formula (inverse resistance sum). **Method IMPORTED**; the main text gives self-contained Rayleigh/exit-time proofs; the present first-loss and storage comparison is Section 12, and the global reading of B19 is retracted |
| E33. Chazottes–Collet–Méléard, *Sharp asymptotics for the quasi-stationary distribution of birth-and-death processes* | [journal](https://link.springer.com/article/10.1007/s00440-014-0612-6); limited earlier reading | general quasi-stationarity lineage; the specific prefactor of the earlier table was not compared with the full text and is not re-cited as a current result; Theorem 1 is self-contained |
| E34. Barta's inequality and exit-time moment spectra (Hurtado–Markvorsen–Palmer, [arXiv:1307.5265](https://arxiv.org/html/1307.5265), Thm. A and the Barta [1937] citation) | §1: $\inf(-\Delta u/u)\le\lambda_1\le\sup(-\Delta u/u)$; $\lambda_1$ lower bound from mean exit time | the B18-T1 lower bound is the finite M-matrix (Collatz–Wielandt) version; IMPORTED |
| E35. Bartlett–Rudolph–Spekkens–Turner (E25) re-read; Bartlett–Rudolph–Sanders–Turner, *Degradation of a quantum directional reference frame as a random walk* ([arXiv:quant-ph/0607107](https://ar5iv.labs.arxiv.org/html/quant-ph/0607107), §II, Eq. (5)); Ahmadi–Jennings–Rudolph, *Dynamics of a quantum reference frame undergoing selective measurements…* ([arXiv:1005.0798](https://arxiv.org/html/1005.0798), §II Eqs. (10)–(14)) | all three are degradation by **measurement backaction** with "trivial dynamics between measurements" | B18 is the opposite axis: **idle degradation from the reference's own Hamiltonian dispersion without measurement**; no claim to exceed their $j^2$ (or $j$) longevity theorems; different tasks |
| E36. Wright–Walls–Garrison, *Collapses and revivals in the interference between two BECs formed in small atomic samples* ([arXiv:cond-mat/9611211](https://arxiv.org/html/cond-mat/9611211)), Eqs. (21)–(22), (30) | collapse $t_{\rm coll}\approx T/\Delta N$ and revival $T=\pi\hbar/\mu'$ for $H=\hbar\kappa(a^\dagger a)^2/2$ | same mechanism as B14-T5's chirp collapse/revival (fixed $j$); B18's band is not a quadratic spectrum but an exponentially small deficit, a different regime; no claim to improve the $1/\Delta N$ law |
| E37. *Long-lived local quantum coherences from hydrodynamic large deviations* ([arXiv:2604.27074](https://arxiv.org/html/2604.27074), 2026), §IV Eqs. (22)–(27), (33)–(38) | in $U(1)$-conserving many-body systems, the lifetime of local coherence between charge sectors is set by a hydrodynamic large-deviation rate ("coherence-void polaron") | **closest in topic**: "sector-coherence lifetime = large-deviation rate"; object (many-body hydrodynamic void vs. binomial tail of a finite reference ground), mechanism and formulas ($\sqrt{D\gamma}$, stretched exponential vs. $B\,I(x)$) differ; no finite reference, window compression, parity or resource optimum; not subsumed, but the slogan "exponentially long sector coherence" is not new |
| E31 re-read. Koch et al., charge dispersion $\epsilon_m\propto e^{-\sqrt{8E_J/E_C}}$ | §II B, (2.5) | localisation mechanism of offset-charge insensitivity; B18's objects are the window hard wall and binomial tail with a different functional form; cited as conceptual precedent |

**The current novelty judgement follows Sections 12–13 of the main text.** The table above is the original map and does not re-issue the earlier B18/B19 qualification; the E35 author error and the unverified E33 prefactor are repaired.

### L2. The wide inherited literature map

The following tables preserve the material of the earlier v1.4 with interpretations corrected where they conflict with the present corrections. Reading ranges, dates and the P/A/L markers are **past records**, not re-reading performed here. The sources on which the present text depends directly are those of Section 12 and L-S10.1–L-S10.1d.

#### Inherited N1–N16: comparison records up to v1.4

| ID and source | Location checked | Agreement / remaining difference |
|---|---|---|
| N1. [Navascués–Popescu, *How energy conservation limits our measurements*](https://arxiv.org/pdf/1211.2101) | §5.3 (32)–(34); App. D Theorem 2 (81)–(86) | adjacent coherence and the sine-optimal battery are **IMPORTED**; (G12) is the ground-space specialisation of that method; truncated sectors, $\kappa$ allocation and preparation $G$ are separate computations but not by themselves non-subsumed novelty |
| N2. [Marvian–Spekkens, *Modes of asymmetry*](https://arxiv.org/pdf/1312.0680) | §II A, (2.16)–(2.19) | modewise norm monotonicity of covariant channels is **IMPORTED**; T-NOREC is a specialisation; the operational information of this transfer class is the distinction of the sum of adjacent elements from the sum of moduli in (G16) and the cancellation counterexample |
| N3. [Åberg, *Catalytic Coherence*](https://arxiv.org/pdf/1304.1060) | shift coupling, (5), App. B (B41), half-infinite boundary discussion | source shift coherence entering operational performance is prior; free repeated use erasing finite-$B$ boundary, consumption and correlations does not follow |
| N4. [Leppäjärvi–Sedlák, *Incompatibility of quantum instruments*](https://quantum-journal.org/papers/q-2024-02-12-1246/pdf/) | §2, Example 1, and the Lüders-plus-conditional-channel representation | that a fixed POVM does not determine the update is **IMPORTED**; I1 is an exact counterexample inside the earlier declared conserving class, not a new non-uniqueness theorem |
| N5. [Soulas–Franzmann–Di Biagio, *On the emergence of preferred structures in quantum theory*](https://arxiv.org/html/2512.07468v1) | Theorem 3.9 and assumptions | structure selection by a property built under non-degenerate $H$, sufficient state support and a specified tensor dimension; not importable as a conclusion that the actual instrument of this degenerate ground space is uniquely fixed by two data |
| N6. [Zhan et al., *Rapid quantum ground state preparation via dissipative dynamics*](https://arxiv.org/html/2503.15827v2) | §II (2), §IV | constructing energy-lowering jumps is prior; the exact spectral jump here is a chosen control input and proves no efficiency, locality or physical bath origin |
| N7. [Lidar–Chuang–Whaley, *Decoherence-Free Subspaces for Quantum Computation*](https://arxiv.org/pdf/quant-ph/9807004) | protection conditions under common action of noise generators | the general principle that information on residual degrees of freedom acted on by the identity is preserved is prior; the sector protection of P3 is not a new principle |
| N8. [Trushechkin, *Unified GKLS quantum master equation beyond the secular approximation*](https://arxiv.org/pdf/2103.12042) | §II (4)–(6), §III B | bath correlation matrices and equal-Bohr-frequency cross terms exist in the standard derivation; (K3) is the explicit result of a specific finite-source preparation class, not a discovery of general non-secular effects |
| N9. [Giulini–Kiefer–Zeh, *Symmetries, superselection rules, and decoherence*](https://arxiv.org/abs/gr-qc/9410029) | earlier abstract/text record | prior line discussing Gauss/Coulomb information and radiation; using it as the basis of "static Coulomb is a second-order emission jump" was retracted at v1.5 |
| N10. [Zurek, *Decoherence, einselection, and the quantum origins of the classical*](https://link.aps.org/doi/10.1103/RevModPhys.75.715) | earlier einselection record | standard principle that the environment's coupling observable decides protection; T-BLIND′ needs the actual zero-frequency noise condition in addition |
| N11. [Strocchi–Wightman, *Proof of the charge superselection rule in local relativistic QFT*, J. Math. Phys. 15, 2198 (1974)](https://www.semanticscholar.org/paper/Proof-of-the-charge-superselection-rule-in-local-Strocchi-Wightman/ac4d60ef091c0671dbac63a6ae80d6517155df25) | bibliographic and theorem statement | total-charge superselection is **IMPORTED**; T-GRADE applies its local-QED consequence (covariance of the photon sector) to this environment class |
| N12. [Aharonov–Susskind, *Charge Superselection Rule*, Phys. Rev. 155, 1428 (1967)](https://link.aps.org/doi/10.1103/PhysRev.155.1428) | bibliographic and claim | charge coherence is meaningful relative to a charged reference; consistent with S8.7's conclusion that the source $B_Q$, not the photon environment, plays that role |
| N13. [Ozawa, *Conservation laws, uncertainty relations, and quantum limits of measurements*, PRL 88, 050402 (2002)](https://arxiv.org/abs/quant-ph/0112154) | (13) Yanase condition, (14) $\epsilon^2\ge\|\langle[A,L_1]\rangle\|^2/(4\Delta L_1^2+4\Delta L_2^2)$ | observables read by a neutral pointer (photons with $L_2=0$) must commute with $Q$ (WAY); that C6's $B_R$ satisfies it is a consistency check, not a new proof of an imported theorem |
| N14. [Breuer–Petruccione, *Destruction of quantum coherence through emission of bremsstrahlung*, PRA 63, 032102 (2001)](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.63.032102) | abstract: "bremsstrahlung … caused by the relative motion of the interfering components" | radiative decoherence requires a current difference between branches; T-BLIND (same photon emission) and T-ORDER (different amplitudes/frequencies) are code-level discriminants of that condition; IMPORTED principle |
| N15. Weisskopf–Wigner, *Berechnung der natürlichen Linienbreite…*, [Z. Phys. 63, 54 (1930)](https://link.springer.com/article/10.1007/BF01336768) | Lorentz linewidth and exponential decay | the spectral factor of (K5) is the **IMPORTED** overlap of two Lorentzian packets; its placement in the sector kernel is the work here |
| N16. Danielson–Satishchandran–Wald, [2023](https://arxiv.org/abs/2301.00026), [2025](https://arxiv.org/abs/2407.02567) | earlier abstract/local-description record | spatial superpositions and soft radiation are a different object from this seed's charge-sector coherence; not identified by coupling order alone; not imported as a basis for a universal statement |
| (re-check) N4′. [Katsube–Ozawa–Hotta, arXiv:2211.13433 (v5, 2026-05)](https://arxiv.org/html/2211.13433) | definition of scattering-type measurements ($U=e^{-i\tau H}$, $[U,H]=0$, Yanase condition), Theorem 1 | the frame of T-VERTEX ("Kraus operators are fixed by the scattering unitary, probe and readout") is the **IMPORTED** structure of this paper and standard QND theory (Braginsky–Khalili); the addition here is the exact witness (C07) that the dephasing alternative is excluded in the $B_R\otimes V$ class |

#### Inherited map A: field theory, detectors and records

| ID and source | Range checked | What to take / difference to overcome |
|---|---|---|
| E01. Fewster–Verch, *Quantum fields and local measurements*, arXiv:1810.06512 | introduction, §3 (3.19)–(3.26), locality discussion | the general structure obtaining pre-instruments from local couplings and probe effects is **IMPORTED**; it does not select the physical origin of probe preparation and measurement. [text](https://arxiv.org/pdf/1810.06512) |
| E02. Fewster–Jubb–Ruep, *Asymptotic measurement schemes for every observable of a quantum field theory*, arXiv:2203.09529 | abstract, introduction, explicit comparison in E03 | asymptotic measurement/tomography line for scalar QFT; not identified with the implementation of every concrete instrument; its detailed theorems are not core evidence here. [text](https://arxiv.org/abs/2203.09529) |
| E03. Mandrysch–Navascués, *Quantum field measurements in the Fewster–Verch framework*, LMP 115, 115 (2025) | Theorem 1, §§4–5, (26)–(43), measurement-chain construction | asymptotically movable FV–Heisenberg cuts already proved for Gaussian measurements and dephased instruments of linear scalar fields; not posed here as a new open problem; the quantitative implementation with finite resources and a specified interacting boundary action is the comparison target. [text](https://link.springer.com/article/10.1007/s11005-025-02001-3) |
| E04. Donnelly–Freidel, *Local subsystems in gauge theory and gravity* (2016) | introduction (1.1)–(1.5), boundary phase-space picture | the warning that Gauss constraints prevent a naive tensor split and the role of boundary variables; not a selection theorem for S14's quantum CPTP subsystems. [text](https://arxiv.org/pdf/1601.04744) |
| E05. Kazinski–Ryakin–Shevchenko, *Radiation from Dirac fermions caused by a projective measurement* (2024) | abstract, introduction, setup; compared with M70 §7.1 (34)–(39), (67)–(69), (130)–(134) | radiation computed given a measurement; not the same event sequence as M70's external-pulse response; the measurement itself is not derived from that radiation formula. [text](https://arxiv.org/pdf/2406.19429) |
| E06. Piccione et al., *Exploring the Accuracy of Interferometric Quantum Measurements under Conservation Laws*, PRL 133, 240202 (2024) | introduction, measurement setup, Ozawa bound (2), scattering interpretation | reading a qubit with an energy-conserving interferometer already exists; the two-channel comparison model and cost formulas are not presented as central originality. [text](https://arxiv.org/pdf/2404.12910) |
| E07. Schwarzhans et al., *Quantum detectors as autonomous machines: assessing the nonequilibrium thermodynamics of information acquisition*, PRX Quantum 7, 033001 (2026) | abstract, §I P.1–P.4, detector performance definitions | detector approach including energy sources, non-equilibrium maintenance, repeated use and amplification; linking autonomous detectors and consumption cost is not claimed new. [preprint](https://arxiv.org/pdf/2508.16375), [journal](https://journals.aps.org/prxquantum/abstract/10.1103/wm5p-tjtg) |
| E08. Lostaglio–Müller, *Coherence and asymmetry cannot be broadcast* (2019) | abstract, finite-dimensional scope | warns against free-reference assumptions broadcasting continuous-symmetry asymmetry losslessly in finite dimension; not used as a theorem forbidding copying of classical branch labels. [text](https://arxiv.org/pdf/1812.08214) |
| E09. van Luijk–Werner–Wilming, *Covariant catalysis requires correlations and good quantum reference frames degrade little*, Quantum 7, 1166 (2023) | Theorems 1, 5 and the connected-group restriction | distinguishes marginal preservation of a catalyst from correlation-free reuse; not read as a universal reset theorem without symmetry-group, dimension and error conditions. [text](https://arxiv.org/pdf/2301.09877) |
| E10. Hokkyo–Tajima, *Quantitative Wigner–Araki–Yanase Theorems for Unitary and Antiunitary Symmetries* (2026 preprint) | abstract, introduction, implementation setting | recent competing work on apparatus asymmetry cost including discrete and antiunitary symmetries; "$Z_2$ also needs resources" alone cannot secure novelty; no quantitative theorem imported into the proofs. [text](https://arxiv.org/pdf/2607.09075) |
| E11. Ferté–Farci–Cao, *Decoherent Histories with(out) Objectivity in a (Broken) Apparatus*, PRL 136, 090404 (2026) | publication data; preprint v4 introduction and model (1)–(3) | separates decoherent histories from readable objective records in a solvable apparatus/scrambler model; recent source that loss of coherence cannot replace the formation of a record. [journal](https://journals.aps.org/prl/abstract/10.1103/8qzx-xpfz), [text](https://arxiv.org/pdf/2508.16482) |
| E12. Girard–Cheng–Cao, *Demystifying Objectivity with Operator Algebra Quantum Error Correction* (2026 preprint) | title, authors, abstract from arXiv search; full text not obtained | objectivity and algebraic local recoverability already have competing work; the name "algebraic record" gives no novelty; overlap review **HOLD** and not load-bearing. [abstract](https://arxiv.org/abs/2606.06588) |

E07 was updated from "2025 preprint" to the PRX Quantum 7, 033001 (2026-07-01) publication; publication data and purpose were checked, not the full proofs. E12's full text was not obtained then either and remains an abstract-level pointer.

#### Inherited map B: reference frames, clocks and selection

| ID | Source and location | Use and check record |
|---|---|---|
| F01 = Book E1 | M. Navascués, S. Popescu, *How energy conservation limits our measurements*, PRL 112, 140502 (2014); [extended text](https://arxiv.org/pdf/1211.2101), §§3.1–3.2, (11), §5.3 (32)–(34), §5.4 | **P.** Nearest baseline for resonance, battery coherence and the cosine ceiling; finite-auxiliary readout and variational framing are not counted new; §5.4 has an energy-constrained variational problem too |
| F02 = Book E2 | V. Bužek, R. Derka, S. Massar, *Optimal quantum clocks*, PRL 82, 2207 (1999); [text](https://arxiv.org/pdf/quant-ph/9808042), (7)–(10) | **P.** The cost-matrix minimal eigenvector giving the clock optimum; re-derived in S7.2 with explicit loss function and finite bound |
| F03 = Book E3 | T. Paterek, P. Kurzyński, D. K. L. Oi, D. Kaszlikowski, *Reference frames for Bell inequality violation in the presence of superselection rules*, NJP 13, 043027 (2011); [text](https://arxiv.org/abs/1004.5184) | **A**, compared with M71 §9.2 (11)–(12), (16)–(19). Sine optimisation of separable references is prior; not the same optimisation as M71's shared-compensator multi-lag problem |
| F04 = Book E4 | S. D. Bartlett, T. Rudolph, R. W. Spekkens, *Reference frames, superselection rules, and quantum information*, RMP 79, 555 (2007); [text](https://arxiv.org/pdf/quant-ph/0610030) | **A / review pointer.** Standard frame of references, twirling and relational encoding; the energy-dephasing claims were checked by direct commutator formulas |
| F05 = Book E5 | Y. Guryanova, N. Friis, M. Huber, *Ideal Projective Measurements Have Infinite Resource Costs*, Quantum 4, 222 (2020); [text](https://arxiv.org/pdf/1805.11899), §1 | **P.** Considers the cost of perfect pointer preparation and correlation at finite temperature; not read as deriving the unique choice of a physical instrument or a specific single outcome; "the optimal pointer is thermal" does not decide the reference-selector difference |
| F06 = Book E6 | Erker et al., *Autonomous quantum clocks…*, PRX 7, 031022 (2017), [text](https://arxiv.org/abs/1609.06704); Schwarzhans et al., *Autonomous Temporal Probability Concentration…*, PRX 11, 011046 (2021), [journal](https://doi.org/10.1103/PhysRevX.11.011046); Meier et al., *Fundamental Accuracy-Resolution Trade-Off for Timekeeping Devices*, PRL 131, 220201 (2023), [text](https://arxiv.org/abs/2301.05173) | **A / bibliographic.** Ticking-clock performance–resource literature; their bound definitions and memoryless conditions are not attached to the phase QFI here |
| F06b = Book E6 (continued) | F. Meier et al., *Precision is not limited by the second law of thermodynamics*, Nature Physics 21, 1147 (2025), [text](https://arxiv.org/abs/2407.07948); M. P. Woods, M. Horodecki, *Autonomous Quantum Devices: When Are They Realizable without Additional Thermodynamic Costs?*, PRX 13, 011016 (2023), [journal](https://doi.org/10.1103/PhysRevX.13.011016) | **A / bibliographic.** The first exhibits coherent many-body clocks beyond simple precision–dissipation relations; the second treats realisability of autonomous devices; not used as evidence that clocks always obey one universal cost formula |
| F07 = Book E7 | H. Tajima, N. Shiraishi, K. Saito, PRL 121, 110403 (2018), [journal](https://doi.org/10.1103/PhysRevLett.121.110403); Y. Kuramochi, H. Tajima, *Wigner–Araki–Yanase theorem for continuous and unbounded conserved observables*, [arXiv:2208.13494](https://arxiv.org/abs/2208.13494); A. Hokkyo, H. Tajima = E10 | **L/A**, Hokkyo within E10's range. Exact task, error definition and equality conditions must be transferred first; no computation that the M71 optimum saturates these bounds |
| F08 = Book E8 | C. J. Riedel, *Living bibliography for the problem of defining wavefunction branches*, blog updated 2026-01-07 as recorded then | **L, non-paper pointer.** Kept as an exploration path, not as decisive source for problem rankings; URL and date not re-verified |
| F09 = Book E9 | A. Soulas, G. Franzmann, A. Di Biagio, *On the emergence of preferred structures in quantum theory*, [arXiv:2512.07468](https://arxiv.org/pdf/2512.07468), Theorem 3.9, conclusion | **P.** Existence of unitary-invariant properties fixing structure under fixed factor number/dimension, non-degenerate $H$ and sufficient state support; re-compared at v1.3 |
| F10 = Book E10 | E. Schwarzhans, F. C. Binder, M. Huber, M. P. E. Lock, *Quantum measurements and equilibration: the emergence of objective outcomes via entropy maximisation*, PRR 7, 043279 (2025), [arXiv v3](https://arxiv.org/pdf/2302.11253), abstract, §I | **P.** Shows in a specific setting that equilibration of standard couplings does not automatically give objectivity, with approximate improvements for given Hamiltonian forms; not a no-go for all unitary measurements |
| F11 = Book E11 | D. A. Chisholm, G. M. Palma, L. Innocenti, *On the emergence of quantum Darwinism and pointer states for non-commuting evolutions*, APS Open Science 1, 000024 (2026), [text](https://arxiv.org/pdf/2510.06867), introduction, model (1) | **P.** Objectivity and SBS pointers can arise with non-commuting $H_S,H_I$ depending on the model; direct comparison line preventing the extension of the exact-QND failure of S8 to all records |
| F12 = Book E12 | R. Katsube, M. Ozawa, M. Hotta, *Limitations of Quantum Measurements and Operations of Scattering Type under the Energy Conservation Law*, [arXiv:2211.13433v5](https://arxiv.org/abs/2211.13433v5), 2026-05-12; G. Chiribella, Y. Yang, *Optimal quantum operations at zero energy cost*, PRA 96, 022327 (2017), [journal](https://doi.org/10.1103/PhysRevA.96.022327) | **A / bibliographic.** The earlier version cited v4 (36), (38); those theorems were not re-compared in v5; scattering/gate conditions are not converted into a universal commensurability law for different rotor tasks |
| F13 = Book E13 | J. Zhang, *Summing to Uncertainty: On the Necessity of Additivity in Deriving the Born Rule*, [arXiv:2603.06211](https://arxiv.org/abs/2603.06211); L. Masanes, T. D. Galley, M. P. Müller, Nat. Commun. 10, 1361 (2019), [text](https://www.nature.com/articles/s41467-019-09348-x); A. Kent, Quantum 9, 1749 (2025), inherited pointer; E. O. Torres Alegre, *Causal Consistency Selects the Born Rule…*, [arXiv:2512.12636v3](https://arxiv.org/abs/2512.12636v3) | **A**: abstracts/bibliographic for Zhang and Torres Alegre; **L**: detailed proofs of Masanes et al. and Kent. The Born-rule debates across postulate systems are not claimed resolved; the instrument computations here use the trace rule explicitly |

### L3. The note's comparison and source lineage

| Line | Secured by prior work | Way used here | Remaining difference / limit |
|---|---|---|---|
| state discrimination theory | optimal readout and trace distance | (2), (3), contrast including failures | standard tool; no new general theorem |
| sequential weak measurement | pointer correlations and ordered operator products | exact finite computation of two memories | weak/postselected formulas distinguished from all-outcome strong coupling; novelty undetermined |
| collision models | records through sequential environment interactions | causally moving carrier model | actual S14 transport and device selection are additional obligations |
| quantum Darwinism / SBS | readable content in many environment fragments | comparison of local redundancy with two-place joint readout | SBS does not guarantee general recovery of process order |
| Magnus / path signature | non-commutative accumulation and iterated integrals | order response and inverse problem (30)–(37) | uniqueness of the infinite signature not imported into finite records |
| local QFT / Lieb–Robinson | causal composition, propagation bounds | (38), (39), physical criterion for the projection counterexample | whether a finite code preserves actual spatial locality is checked separately |
| conserved densities and thermalisation | persistent redundant records given initial density differences | comparison of fixed density difference with fixed total contrast | initial broadcasting, background resources and subsystem thermalisation conditions needed |
| timeless detector studies | models relating paths and detector records in energy-eigenstate/constraint settings | historical link of the question of reading paths from records | this note derives no clock or origin of time from constraints |

Halliwell's detector model related paths and final records in a setting without the usual time parameter; only the problem setting is connected here and its path-probability formulas were not applied. The recent Ferté–Farci–Cao model likewise separates decoherent histories from readable objective records, so it does not support certifying spatial records by loss of coherence alone.

The research change secured by the note is clear: the interpretation "accumulation of space" was replaced by the actual state (9), the storage lower bound (21), the order response (32) and the current condition (48), while (51)–(55) exclude declaring physical success from an apparent current condition alone. This is **the resolution of an internal concrete construction and discrimination target**, not a confirmation of external originality of those mathematical tools or of the spatial-record idea.

**Note sources.** Project founding research note v1.3 (items 5, 6, 13; source of the founding questions, not of verified physical laws). Project seed v1.7 (§§6.12, 7.3, 8.17–8.18, 9.2–9.9, 11.3, 13.1; the distinction of finite references from output records, CAR charge, failure flags and leakage bounds, repeated pumps and storage limits). J. Watrous, *The Theory of Quantum Information* (2018), [Chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) §3.1 Theorem 3.4 and [Chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) §5.1, Theorem 5.15 (Pinsker). F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, K. Modi, [*Operational Markov Condition for Quantum Processes*](https://arxiv.org/pdf/1801.09811), PRL 120, 040405 (2018). C. J. Fewster, R. Verch, [*Quantum fields and local measurements*](https://arxiv.org/pdf/1810.06512), CMP 378, 851 (2020), §3, Theorem 3.5, (3.28)–(3.30), Appendix D. G. Mitchison, R. Jozsa, S. Popescu, [*Sequential weak measurement*](https://arxiv.org/pdf/0706.1508), PRA 76, 062105 (2007), §III (7)–(9). S. Campbell, B. Çakmak, Ö. E. Müstecaplıoğlu, M. Paternostro, B. Vacchini, [*Collisional unfolding of quantum Darwinism*](https://arxiv.org/pdf/1901.03335), PRA 99, 042103 (2019). W. H. Zurek, [*Quantum Darwinism*](https://arxiv.org/abs/0903.5082), Nature Physics 5, 181 (2009). R. Horodecki, J. K. Korbicz, P. Horodecki, [*Quantum Origins of Objectivity*](https://arxiv.org/pdf/1312.6588), PRA 91, 032122 (2015). S. Blanes, F. Casas, J. A. Oteo, J. Ros, [*The Magnus expansion and some of its applications*](https://arxiv.org/pdf/0810.5488), Phys. Rep. 470, 151 (2009), (42)–(45). B. Hambly, T. Lyons, [*Uniqueness for the signature of a path of bounded variation and the reduced path group*](https://arxiv.org/pdf/math/0507536), Ann. Math. 171, 109 (2010), §1.4, Theorem 1, Corollaries 1.5–1.7. B. Nachtergaele, R. Sims, [*Lieb–Robinson Bounds and the Exponential Clustering Theorem*](https://arxiv.org/pdf/math-ph/0506030), CMP 265, 119 (2006), Theorem 1, (4), (7). Project S14, [*ZS-S14 v2.1: typed master action*](https://docs.google.com/document/d/1m0on1fMN5tRxGfdKxx8b380EAai2hnOfhx7Pp8FoLIg/edit), Definition 3.1′. Project M70, [*M70 v1.5*](https://drive.google.com/file/d/19tfkq-eYMWDvt1nFaHS7QTnrCaBSX-uv/view), §§1.1–1.2. X. Cao, Z. Nussinov, [*Redundancy from Subsystem Thermalization*](https://arxiv.org/pdf/2603.15743), arXiv:2603.15743v2 (2026), pp. 1–4, (5)–(15), Proposition 1. J. J. Halliwell, [*Trajectories for the wave function of the universe from a simple detector model*](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.64.044008), PRD 64, 044008 (2001), bibliographic. B. Ferté, D. Farci, X. Cao, [*Decoherent histories with(out) objectivity in a (broken) apparatus*](https://arxiv.org/pdf/2508.16482), arXiv:2508.16482v4 (2026).


## Appendix R. The two audits and what each revision did with them

**Lineage note (v1.5).** The statements in this appendix that the audits of v1.0 and v1.1 were carried out "in the same AI lineage" are preserved as written at the time but are **corrected** by the AI-use record of v1.5: according to the user-reported workflow, every audit of this paper was carried out by a different AI family from its author. The substance of those audits and the verdicts recorded here are unaffected; only the independence label changes, in the direction of more independence, not less.

**Historical correction log.** The version-specific verdicts and claims below retain their original chronology. Current statements are §§9–10, the current literature comparison is §12.4, and the current qualification is §13.1. They supersede conflicting earlier descriptions.

### R1. The audit of v1.0: what was audited and under what independence

After v1.0 was issued, an integrated audit of the manuscript, its verifier and its results was carried out in the same AI lineage, with access to v1.0's own claims and to the project history: it is **not** a blank-context review, and it is **not** a cross-lineage or human review. Its own disclosure states this, and this paper repeats it: **qualified-human anchor: NONE**, and the earlier self-audit budget is treated as spent and is not reset by a version change. What the audit did supply, and what makes its findings usable, is adversarial substance rather than status: it re-ran v1.0's verifier unmodified and reproduced 25/25 PASS, it wrote a separate check script that imports nothing from the verifier, and it produced exact rational counterexamples rather than tolerance failures. Its verdict on v1.0 was AUDIT-MAJOR-REVISION with PAPER QUALIFICATION: FAIL. That verdict is recorded and stands as a statement about v1.0.

The claims of the audit were not adopted on its word. Every counterexample and every constant reproduced below was recomputed independently for v1.1, by code written for this revision, before any text was changed; where the recomputation disagreed with the audit or could be strengthened, this appendix says so (R4 and R5).

### R2. Findings F01–F11: repair, location, status

| ID | v1.0 defect | Severity as audited | Repair in v1.1 | Status |
|---|---|---|---|---|
| F01 | Proposition 9.1 printed only the upper bound on $\liminf$; the no-hit lower bound needed for the interval was proved in the text but absent from the statement, and later sentences read a variable $\kappa$ as a constant | S2 | statement replaced by the two-sided (9.1a) with strict thresholds; the variable-$\kappa$ crossing written as (9.1b) with uniqueness flagged as an extra hypothesis | **REPAIRED**, statement now matches the proof |
| F02 | Theorem 7's lower-end construction built a different family for each $q'>q_{\ell/2}$, so no single admissible family was exhibited | S2 | explicit diagonalisation over blocks $B_n\le B<B_{n+1}$ with thresholds $q_n\downarrow q_{\ell/2}$, added to the proof in Section 9.2 | **REPAIRED**, sharpness recovered |
| F03 | Theorem 8's proof bounded the coefficient mass of a product group by $K_m(0)^{i^*}$; $K_1(0)=0$, so this bounds nothing | S2 | proof rewritten around the $\ell^1$ Fourier mass (9.4a) with the two margins (9.4b)–(9.4c); the **same** printed constant $c_m=8(m+1)(2m+1)/m$ is recovered; the unproved side remark "$6$ for $m=1$" is deleted | **REPAIRED-PROVEN**, constant unchanged |
| F04 | Theorem 9(iv) reported grid non-negativity for even $6\le q\le40$ as a VERIFIED equality of $\beta_q$ | S2 | the grid claim is retyped as a diagnostic (row V25) and the equality is **proved for every even $q\ge2$** by Theorem 13, with uniqueness of the maximising measure | **SUPERSEDED BY PROOF** |
| F05 | Conjecture 9.2 identified the phase dynamics with the reduced torus map $x\mapsto\{qx\}$ for non-integer ratios | S2 | identification **retracted**; exact counterexample (9.7); replacement objects (9.8)–(9.9), the stability inequality (9.10) and the ratio-profile counterexample (9.11); the conjecture is decomposed into (a)–(d) | **RETRACTED + REPLACED**; (b) proved |
| F06 | In the proof of Theorem 10, $\sum_ss^2\rho^s$ was bounded by $2\rho^2/(1-\rho)^3$, which is the value of $\sum_ss(s-1)\rho^s$ and runs the wrong way; and the spectral step's $O(B^{-3/4})=O(B/h^2)$ does not follow from $h\le B/2$ | S2 | the expansion's own $s(s-1)$ is kept, giving the exact (10.2a) and the same leading coefficient; the spectral step is recomputed as $O(B^{-5/4})$, which *is* $O(B/h^2)$ | **REPAIRED**, statement of Theorem 10 unchanged |
| F07 | The consequences of Theorem 10 asserted a Gaussian gap scale on the whole range $h\ge\sqrt{2B\log B}$, extended the adjacent-gap lemma without a difference remainder, and called $B^{3/2}e^{2K^2}$ a first-loss law at $h=K\sqrt B$ | S2 | consequences rewritten as (a)–(d): weights kept; the Gaussian form restricted to $h=o(B^{3/4})$ with the analytic counterexample at $h=B^{4/5}$ and the exact excess (10.3a); the adjacent-difference extension withdrawn as open; the fixed-$K$ sentence demoted to a statement about frequencies | **RESTRICTED / PARTLY WITHDRAWN** |
| F08 | Section 10.3 asserted an exact Weyl ground energy $-(1-1/B)$ and gap $2/B$, and transferred the gap exponent to other parents unconditionally | S2 | exactness **refuted** by the exact rational characteristic polynomial (10.5) and withdrawn; the rate coincidence kept as a VERIFIED finite fact; the transfer made conditional on four explicit normalisation requirements | **REFUTED + RESTRICTED** |
| F09 | Floating Lipschitz scans were described as certified intervals of the exact matrix | S2 | Section 9.5 states exactly what the bracket certifies and what it does not; row types corrected; a rigorous enclosure listed as obligation (2) of Section 14 | **RETYPED** |
| F10 | The finite $T_{\rm hit}$ and $\theta$ columns were read as evidence about limits and as potential refutations | S1 | the table is labelled a finite diagnostic; the falsifier of Conjecture 9.2 now requires a controlled subsequence with a residual bound | **RETYPED** |
| F11 | The verifier's scope strings pointed at the seed's old theorem numbers (T19.1, T19.2(a), T19.3); the history row, the text and the code disagreed about status | S1 | pointers rewritten to Theorem 1(a)–(b), 2(a), 3; the row ledger, the text and the appended history row are aligned at v1.1 | **REPAIRED** |

Highest severity of v1.0 as audited: **S2**. Release-blocking for v1.0: yes. SSOT impact: yes — the status recorded for v1.0 is corrected by an appended history row, not by editing the old one. Downstream propagation: any later use of the Weyl exactness, of the even-$q$ VERIFIED range, of the non-integer torus identification, or of the v1.0 consequences (a)–(b) of Section 10.1 must be re-derived from v1.1.

### R3. The audit's own check rows and where they are used

The audit ran eleven checks (7 exact, 4 floating diagnostics) in a script that imports nothing from the verifier. Each was recomputed independently for v1.1; the right-hand column names the v1.1 row that carries the same content.

| Audit row | Object | Recomputed for v1.1 | Carried by |
|---|---|---|---|
| A01 | $B=256$ Weyl characteristic polynomial in exact rationals | yes, and extended to $B=4,8,16,64$ with the sign argument and the $2.8\times10^{-7}$ deviation at $B=16$ | C29 |
| A02 | $\{q^2x\}$ versus $\{q\{qx\}\}$ at $q=\tfrac52$ | yes, plus the opposite-sign check on the two cosines | C30 |
| A03 | $K_1(0)=0$ against Fourier mass $2$ | yes, generalised to the mass identity $(\sum s_j)^2/\sum s_j^2$ for $m=1,2,3$ | C31 |
| A04 | the false $s^2$ bound at $B=1024$, $h=256$ | yes, with both closed forms and the coefficient identity (10.2a) | C32 |
| A05 | symbolic $q=2,4$ sub-action factorisations | unchanged from v1.0 | C24 |
| A06 | tent sub-action on a grid, $q\le1000$ | yes, plus the endpoint quantities at 60 digits up to $q=10^6$ | V27 |
| A07 | the algebra $1-\tfrac14-\frac{R}{4(2m-1)}=\frac{m-1}{2m-1}$ | yes, inside the rewritten proof of Theorem 8 | C32, text (9.4c) |
| A08 | dyadic family with odd-multiple rounding | yes, as the ratio-profile counterexample (9.11) | text; mechanism in W15 |
| A09 | positive-kernel bound on an actual $B=24$ spin band | yes, with the reflection pairs merged correctly | V33 |
| A10 | 95-digit centre gaps at $h\approx\sqrt{2B\log B}$ | recomputed; **not adopted as a theorem** (see R5) | — |
| A11 | sparse Riesz constants and the standard-band quantiles | yes, with independent evaluation of $C_0$, $C_1$ and the fronts | V33, V34 |

### R4. The audit's new theorems, and where v1.1 goes further

Three results were supplied by the audit rather than by v1.0. All three are integrated, with their proofs rewritten for this manuscript and their scope stated here.

1. **All-even-$q$ sub-action.** The audit proved $\beta_q=\cos\frac\pi{q+1}$ for even $q\ge6$, using the bound $g(\pi)\ge\tfrac32-\pi^2/7>0$, which needs $a=\pi/(q+1)\le\pi/7$, and it closed $q=2,4$ by citing v1.0's polynomial identities. **v1.1 proves the theorem for every even $q\ge2$ with the same tent sub-action**, by splitting $[0,\pi]$ at $d=\pi/q$ and using the second lower bound $G(d)=\cos a-\cos d-\frac{\sin a}{q+1}d$ on $[\pi/q,\pi]$, whose two endpoint values are positive for all $q\ge2$: $G(\pi)=1+\cos a-a\sin a$ is decreasing in $a$ and positive at $a=\pi/3$, and $G(\pi/q)=\varphi(\delta)$ with $\varphi(0)=0$, $\varphi'\ge0$. The polynomial sub-actions for $q=2,4$ are therefore no longer load-bearing, and the uniqueness of the maximising measure follows for every even $q$ from the same inequality.
2. **Sparse Riesz lower bound for real frequencies** (Theorem 14) and its application to the standard band (Theorem 15). Integrated as stated, with the three non-resonance margins spelled out and the constants recomputed. One correction of emphasis: the hypothesis $\rho=19/10$ is *not* satisfied at every $B$ — the measured minimum adjacent ratio is $1.847$, $1.888$, $1.948$ at $B=48,96,192$, rising to $2$ — so Theorem 15 is stated "beyond a finite size", and row V34 reports the approach rather than asserting the hypothesis at all $B$.
3. **Effective domain of the lacunary rate function** (Theorem 16). Integrated as a DERIVED COROLLARY. The source's open sentence was re-read directly in two independent copies of the paper before the claim was made, and the one 2026 article that might bear on it could not be retrieved; both facts are recorded in Section 12.2.

### R5. What v1.1 did **not** adopt

- The audit's high-precision diagnostic A10 at $h\approx\sqrt{2B\log B}$ suggests an extra factor of order $h/B$ in the centre adjacent gap. The audit itself declined to promote it, and v1.1 does not either: four sizes do not determine an asymptotic law. The honest outcome is consequence (c) of Section 10.1 — the adjacent-difference remainder in the diffusive range is **open** — not a replacement formula.
- The audit's suggestion to keep the spectral step of Theorem 10(ii) as an unresolved uniform bound is not adopted, because the step closes exactly once the arithmetic is corrected: $e^{-h^2/B}\le B^{-2}$ gives $O(B^{-5/4})$, which is $O(B/h^2)$ for every $h\le B/2$.
- The audit's re-census moved row C21 to a V row and split the C24 grid part. v1.1 adopts both, and implements them as renamed rows (V21 and the new V25) rather than as a class label contradicting the row's own identifier.
- No part of the audit's text is treated as an instruction about the verdict. The verdict in Section 13.1 is re-derived here from the four criteria, and it is HOLD — not PASS, and not the audit's FAIL, which was a verdict on v1.0.

### R6. Status of v1.0 and of v1.1

v1.0 is superseded. Its verdict (PAPER QUALIFICATION: PASS) is corrected to FAIL as a statement about that manuscript, its Weyl exactness claim is REFUTED, its even-$q$ VERIFIED range is SUPERSEDED, and its Conjecture 9.2 identification is RETRACTED; the remaining v1.0 results stand as repaired here. v1.1 carries PAPER QUALIFICATION: HOLD with novelty open, RESEARCH GRADE 3 in SUPPORT/METHOD scope, CANDIDATE GRADE 4 with the unmet items of Section 13.1. Nothing in this appendix promotes a result to CORE, closes an S14 debt, or claims an external review that did not happen.

### R7. A referee pass on the theorems that were new in v1.1

The three theorems that are new in v1.1 were not audited by anyone before this manuscript, so before issuing it they were given to a separate hostile-referee pass whose only instruction was to break them: check the identities symbolically, hunt for counterexamples to the pointwise inequality (9.15) and to the bound (9.22), and attack the orientation of the argument in Theorem 15. It found no counterexample to any of the three — the tent inequality was minimised branch by branch for every even $q\le40$ and at 60 digits up to $q=10^6$, the three non-resonance margins of Theorem 14 were checked term by term over 400 random lacunary sets with zero violations, and the orientation of Theorem 15 (the fast modes are at the band edge, where the limiting ratio is $2$, not at the centre, where it is $5$) was confirmed as the one the proof uses. It did find four defects, all of which are repaired in the text above and are listed here because they were found after the audit of v1.0 and belong to v1.1's own record.

| Defect found in the v1.1 drafts | Where | Repair |
|---|---|---|
| The step $\vert \langle e^{i\Omega t}\rangle\vert \le1/(\vert \Omega\vert T)$, used in the proofs of both Theorem 8 and Theorem 14, is false: the sharp value is $2\vert \sin(\Omega T/2)\vert /(\vert \Omega\vert T)$, which is $2/\pi$ at $\Omega T=\pi$ against $1/\pi$ | §9.4, §9.7 | the terms are now paired with their conjugates **before** averaging, which is legitimate because the Riesz products are real and even in $t$ and gives (absolute mass of the pair)$\times1/(\vert \Omega\vert T)$; all printed constants are unchanged |
| In Theorem 13 the claim that $G$ attains its minimum on $[\pi/q,\pi]$ at an endpoint was asserted, not proved: an interior minimum at the left critical point $d_1$ had to be excluded | §9.6 | the line $d_1=\arcsin\frac{\sin a}{q+1}\le\frac{\pi^2}{2(q+1)^2}<\frac\pi q$ is added, using $\arcsin y\le\frac\pi2y$ and $\pi q<2(q+1)^2$ |
| Theorem 15 cited (3.12)–(3.13) for the adjacent-ratio statement (9.28); those control only $B^{-1}\log\vert \Delta_k\vert $ and cannot give an $O(1)$ ratio, and the printed relative error $O(B^{-1})$ is not corroborated by the finite data at the band edge | §9.7 | the citation is corrected to the exact adjacent ratio (3.14) with (3.8) and (3.15), and the relative error is weakened to $o(1)$, which is all the proof uses; the finite deviations of row V34 are quoted in place of the unearned rate |
| The reflection pair of degenerate frequencies was labelled $(k,-k)$; the gaps pair as $(k,-k-1)$ | §9.7 | corrected, with the merge shown to be an identity from $E_k=E_{-k}$ rather than an approximation |

Two softer points were also raised and are answered in place: the definition of $\kappa^\pm$ now uses $\limsup$ and $\liminf$ in $\eta$ rather than assuming a limit, and records that it needs $\mu_B(z,\eta)>0$; and the observation that the tent inequality is razor-tight at $d=\pi/q$, with $G(\pi/q)=\Theta(q^{-4})$, is exactly why the added line matters. This pass was run in the same lineage as the rest of the work and is not counted as independent review either; it is reported because its findings changed the text.

### R8. The audit of v1.1: findings and repairs

v1.1 was audited in turn, in the same lineage and under the same disclosure — no cross-lineage or human review, self-audit budget not reset, **qualified-human anchor: NONE** — and again with adversarial substance rather than status: the auditor re-ran the shipped verifier unmodified and reproduced 37/37 PASS and the live self-test 13/13 with every data field matching the shipped JSON apart from runtime metadata, wrote a nine-row check script that imports nothing from the verifier, and produced exact counterexamples. Its verdict on v1.1 was AUDIT-MAJOR-REVISION with PAPER QUALIFICATION: FAIL, highest severity S3, and that verdict stands as a statement about v1.1. As with the first audit, nothing was adopted on its word: every counterexample and constant below was recomputed for v1.2 before any text was changed, and one recomputation found an error in the checking code rather than in the audit (R9).

| ID | v1.1 defect | Severity as audited | Repair in v1.2 | Status |
|---|---|---|---|---|
| F01 | Proposition 9.1 was stated "under the hypotheses of Theorem 2(c)" with $H(z)$ in both thresholds. The alignment capacity is defined through the modes with $\alpha\le z-\eta$, whose mass is $H_-(z)$; if $\mu$ has an atom at $z$ the middle strip does not vanish. An explicit family with an atom of mass $0.07$ at $z=2$ makes the printed statement give $\limsup\le2$ while the true exponent is $\ge3$ | **S3** | Proposition 9.1 restated with $H_-(z)$ and the atomic term $2a_z$, with (9.1a$'$) as the no-atom corollary; the counterexample is carried in the text as (9.1c)–(9.1d) with its four groups and its exact rational witness; every application is checked for atoms, and the spin band has none | **REFUTED (as printed) + REPLACED**; the corrected form is proved |
| F02 | §10.3 asserted that the Weyl ground-energy correction "decreases superexponentially in $B$", inferred from the size of the characteristic polynomial | S2 | replaced by **Proposition 17**: an explicit positive trial vector gives $\delta_B\ge1/(BZ_B)\ge1/(B2^{2B-1})$ for every $B\ge1$, so $(-\log\delta_B)/B\le2\log2$ and superexponential decay is impossible; the determinant is a product of $B+1$ factors and its size does not measure one of them | **REFUTED + REPLACED by a proved bound** |
| F03 | Inside the proof of Theorem 10 the omitted tail was written $O(\rho_0^{\sqrt B})$ with an implied absolute constant. At $h=3\sqrt B$ the exact tail satisfies $D/(\sqrt B\rho_0^{\sqrt B})\to85/432$, so the constant depends on $B$ | S2 | the tail is carried in closed form (10.2b), its divergence is stated as (10.2c), and it is estimated **after** normalisation: $(1-\rho_0)D=O(K^{-4})=O(B^2/h^4)$, together with the two remaining tails, whose $O(B/h^2)$ labels are upgraded to $O(K^{-4})$ with the explicit suprema $1.48$ and $1.81$ | **REPAIRED**; Theorem 10 and its coefficient are unchanged |
| F04 | §10.3 and row C29 read "exactly one eigenvalue lies below $z$" from a positive characteristic polynomial | S1 | the text now says an **odd** number, hence at least one, which is all that was needed; the seven-vertex counterexample (positive determinant, three eigenvalues below) is row C40, and Proposition 17 supersedes the argument altogether | **REPAIRED** |
| F05 | The status line carried an achieved "RESEARCH GRADE: 3" and the role "research paper" while the novelty axis was HOLD | S2 (status policy) | achieved grade set to **UNASSESSED** and the role to **research note** until the external comparison identifies a central contribution whose difference from the nearest prior result is established; candidate 4 retained and separated from the achieved grade | **CORRECTED** |
| F06 | Row C35 was typed C but evaluates orbit averages with floating cosines inside a $10^{-12}$ tolerance | S1 | retyped **V35**, with the exact endpoint identity left in the symbolic row C26 and the scope string rewritten | **RETYPED** |

Two further corrections requested by that audit are made: the summary lines and the claim card for Theorem 14 now carry **both** conditions of (9.20), $R=\rho^L>3$ **and** $\delta>0$, not only the first; and the reversal criterion in §13.3 that spoke of "an eigenvalue" equal to the old value now speaks of the **ground** eigenvalue and of what a single $B$ can and cannot restore.

The audit also removed an access caveat rather than adding one: the 2026 *Mathematische Nachrichten* article that v1.1 recorded as unreachable was read in its publisher version, and its theorems live in the moderate-deviation range strictly between the central limit theorem and the large-deviation regime, so they do not compute the endpoint that Theorem 16 determines. Section 12.2 is updated accordingly, and an independent read of the companion arXiv text confirms that scaling range.

| Audit check | Object | Recomputed for v1.2 | Carried by |
|---|---|---|---|
| A01 | atomic-mass family: dyadic identity, Fejér weight sum, all-time rational bound | yes, and extended to $B=64,128,256,1024$ with the two fronts $0.42$ and $0.315$ | C38 |
| A02 | Weyl trial vector: local action, binomial weights, $\delta$ lower bound | yes, symbolically for general $b,B$ and exactly for the weights | C40 |
| A03 | 170-digit Sturm eigenvalues of the Weyl matrix | yes, independently of row C29 | V41 |
| A04 | omitted tail identity and the $85/432$ limit | yes, plus the three suprema that close the normalised estimate | C39 |
| A05 | Theorem 10 coefficient and the $-5/4$ spectral exponent | already carried since v1.1 | C32 |
| A06 | tent sub-action by piecewise extrema rather than a grid | recomputed; the earlier grid row is kept and the analytic proof is the authority | V27, V28 |
| A07 | sparse Riesz moments on rational real ratios | already carried since v1.1 | V33 |
| A08 | spatial-order density operators and correlated-noise parity | already carried since v1.0 | C07, V08, C10 |
| A09 | determinant sign versus eigenvalue count | yes, exactly | C40 |

### R9. Where the recomputation disagreed, and what v1.2 declines to adopt

- Checking F02 the first time, **this session's own script was wrong**, not the audit: it evaluated the tridiagonal action as $C_{b-1,b}v_{b-1}+C_{b,b+1}v_b$ instead of $C_{b,b+1}v_{b+1}$, and appeared to contradict the trial-vector identity. Corrected, the identity holds exactly for every $B$ tested and symbolically in general, and the audit's constants are reproduced to the digit ($\delta_{16}=2.80541376392019\times10^{-7}$). The episode is recorded because the recomputation is only worth as much as its own correctness.
- The audit suggests that Proposition 9.1 could instead be restricted to continuity points of $\mu$. v1.2 states the general form with $H_-$ and $2a_z$, which is strictly stronger and degenerates to the v1.1 display exactly at continuity points, and keeps the restriction as the corollary actually used for the spin band.
- The audit's A06 replaces the tent grid by a piecewise extremum enumeration. v1.2 keeps both finite rows and adds neither as evidence for the theorem: the all-$q$ proof of Theorem 13 is the four displayed inequalities, and no enumeration over a finite list of $q$ certifies it.
- The audit leaves the *exact asymptotics* of $\delta_B$ open, and so does v1.2: Proposition 17 is a lower bound with an explicit constant, the computed $(-\log\delta_B)/B$ falls from $0.943$ to $0.725$ over $B=16$–$256$, and no limit is claimed.

### R10. A referee pass on the v1.2 repairs

As with v1.1, the material new in this revision — the restated Proposition 9.1 with its counterexample, the repaired Theorem 10 tail, and Proposition 17 — was given to a hostile-referee pass before the manuscript was issued. It confirmed the two central new results and could not break either: the corrected Proposition 9.1 is sound in both directions, the factor $2$ on the atomic term is **sharp** (a construction realising the atom by modes at $(2i+1)\pi/T_B$ attains it, and that construction is now in the proof), the counterexample's four groups and four loss bounds all check out with the true supremum at $0.3969$, $0.3952$, $0.3938$ for $B=10,12,14$, the closed form (10.2b) and the limit $85/432$ are exact, the repaired remainder is $O(B^2/h^4)$ **uniformly** over the whole range $3\sqrt B\le h\le B/4$ when tested against exact rational resistance sums, and Proposition 17 holds at every $B$ including $B=1$, where the bound is attained with equality.

It also found three numerical errors, all now corrected in place, and they are worth listing because two of them had survived three drafts.

| Defect | Where | Correction |
|---|---|---|
| The constant in $e^{-4K/3}\le1.48K^{-4}$ is too small: $\sup_{K\ge3}K^4e^{-4K/3}=81e^{-4}=1.48356\ldots$, attained at the interior critical point $K=3$, so the printed inequality is false there by $2\times10^{-3}$ relative | §10.1 | constant changed to $1.4836$, with the location of the supremum stated |
| "At $B=16384$, $h=3\sqrt B$ the coefficient is $-0.243$ against the leading $-0.239$" compares the measured value at $B=16384$ with the leading value at $B=65536$; at $B=16384$ the leading value is $-0.2276$ | §10.1, inherited from v1.0 | the two sizes are separated and the $7\%$ difference is identified with the tabulated residual |
| "A positive value says that an odd number of eigenvalues lies strictly below $z$" is true only when the dimension $B+1$ is odd. At odd $B$ the Weyl characteristic polynomial at $-(1-1/B)$ is **negative** — $-1.77\times10^{-2}$ at $B=3$, $-3.33\times10^{-9}$ at $B=17$ — with one eigenvalue below in every case | §10.3 | the rule is restated as $\#\{\lambda<z\}\equiv B+1\pmod2$, the even and odd sampled sizes are both shown, and row C40 now carries the Weyl signs at $B=3,4,5,7,16,17,64$ |

Three benign bookkeeping gaps were also closed: the head of the geometric sum is truncated at the splitting point $s_1$, not at $h$, so the deficit is $\rho_0^{s_1+1}\le e^{-4K}$ and not the much smaller $\rho_0^{h+1}$ that v1.1 quoted there; the two Taylor terms dropped from $\log P_s$ are now named and bounded rather than left implicit, and the sentence claiming that no step hides a $B$- or $h$-dependent constant is replaced by that accounting; and the two threshold sets in Proposition 9.1 are restricted to the interior of the support, where $\kappa^\pm$ are defined.

One observation is recorded rather than acted on: $Z_B/(2^B\sqrt B)$ appears to approach $\sqrt\pi/2$, so a Stirling estimate would replace $2\log2$ by $\log2$ in Proposition 17, which is where the computed $(-\log\delta_B)/B$ seems to be heading. That estimate is not proved here and the constant is presented as what it is — not sharp. This pass, like the earlier ones, was run in the same lineage and is not counted as independent review.


## Appendix V. Current verification ledger and reproduction contract

### V1. Executions belonging to v1.8

From the companion bundle root:

```bash
python zs_m72_verify_v1_8.py --output zs_m72_verify_v1_8.json
python -O zs_m72_verify_v1_8.py --self-test --output zs_m72_selftest_v1_8.json
python inherited_v1_7/zs_m72_verify_v1_7.py --rows C26,V27,V35 --output inherited_central_v1_8.json
```

Python 3.10+ with NumPy and SciPy suffices for the new verifier. The recorded run used Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. The inherited verifier additionally uses its original dependencies, including SymPy and mpmath. Exact rational values serialize as strings. Floating quadrature and transfer-operator approximations are never represented as directed intervals.

| Execution | Result actually obtained | Scope |
|---|---|---|
| V1.8-NEW-ALL | 9/9 PASS: C3, V4, W1, G1; P=0 | New T31–P34 finite anchors and guards |
| V1.8 SELF-TEST-ALL-ROWS | 6/6 wrong predictions rejected | Every mutation ran all nine rows in a fresh optimized interpreter; the designated row alone failed and all unaffected row evidence was unchanged |
| Inherited central SELECTED-FULL | C26, V27, V35 and G42: 4/4 PASS | Rerun of the original sub-action and endpoint prerequisites, plus registry guard |
| v1.7 FULL / author self-test | 69/69; 45/45 targeted, inherited | Original author outputs, separately reproduced by the supplied v1.7 auditor; not a new v1.8 legacy FULL run |
| v1.7 auditor noninterference | 8/8, inherited | Supplied auditor ran the eight new v1.7 mutations against all QUICK rows; not all 45 mutations |

| Row | Type | What it actually tests |
|---|---|---|
| C71 | finite exact identities | 4,608 rational cylinder identities and phase-error/coverage cases, including negative multipliers and shifts; recurrence defect $(1-q)r$ |
| V72 | numerical cross-route | Bessel coefficient sums versus doubled phase quadrature for 24 finite cases; phase majorization and half-turn identity |
| V73 | numerical cross-route | Unfrozen cylinder tails integrated with 16- and 32-point composite Gauss rules versus the frozen periodic model; both sides of the finite sandwich (9.46) in specified cases |
| V74 | numerical diagnostic | Almost multiplicativity (9.43) for $N=K=3$, three ratios, four tilts and three phases |
| C75 | exact imported-result reproduction | Integer Laurent-polynomial counts reproduce the known shifted cumulants through order six for $n=7,8,9$ |
| C76 | exact imported-coefficient reproduction | First geometric resonance at $q=2,4,6$ and specified lengths; the asymptotic coefficient and cusp conclusion still use the analytic argument |
| W77 | exact witness | Rational intervals in P34 at four lengths, odd parity, and an inherited T13 bound excluding the unshifted event |
| V78 | numerical diagnostic | Finite MGFs for shifts $0,1,2,-1$ and transfer-operator branch checks for $q=2,3,4$; slow convergence is displayed, not converted into a proof |
| G79 | guard | Parameter domain and row registry; zero shifts and noninteger multipliers are outside T31 |

**An actual failed check and its repair.** The initial V73 run failed its 8-versus-16-point quadrature-resolution check. Discrepancies reached about $2.1\times10^{-6}$. The mathematical bound was not contradicted. Resolution was increased to compare 16 and 32 points, with the same tolerance; the largest observed discrepancy was below $2.2\times10^{-14}$. The initial failed JSON is preserved in `research_trace/`, so the final PASS is not presented as an error-free first attempt. No theorem was fitted to these numbers.

**Independence and limits.** These checks expose arithmetic, normalization, freezing and derivative-interchange errors through different finite computations. They do not formally verify the universal proofs, establish priority, calculate the actual spin alignment limit, or certify a research grade. All new work was generated in this authoring session. Qualified-human anchor: NONE.

### V2. Inherited v1.7 ledger, with current scope clarifications

The commands and full 69-row ledger below belong to v1.7. The original executable is preserved under `inherited_v1_7/`; its legacy V70 claim string is read with the explicit p0-only scope recorded here. The original source bytes are retained for reproducibility. Its 45-fault author self-test was targeted, and only the auditor's separate eight-fault experiment checked all-row noninterference. Current v1.8 executions are listed in V1 above.


Run the standalone companion from any directory:

```bash
python zs_m72_verify_v1_7.py --output zs_m72_verify_v1_7.json
python -O zs_m72_verify_v1_7.py --self-test --output zs_m72_selftest_v1_7.json
```

The code requires Python 3.10+, NumPy, SciPy, SymPy and mpmath. It uses no network. `--quick` skips the inherited slowest scans and runs C45 at B=24; the FULL profile additionally certifies B=48 and B=96. No source attachments or previous verifier files are needed to execute it.

| Rows | Role | Evidence scope |
|---|---|---|
| C01–V41 and G42, with the source's existing gaps in numbering | inherited calculations and registry | Original 41 checks retained. V23 and V41 scopes are repaired; V35 is the correct endpoint label. |
| C43 | endpoint Green enclosure | Exact rational formula crosschecked against independent rational LDL eigenvalue bracketing. |
| C44 | Weyl transfer | Exact ground-transform identity and finite capacity sandwich. Displayed asymptotic ratios remain diagnostics. |
| C45 | exact first loss | Directed integer intervals enclose eigenvalues, eigenvectors, weights, frequencies, cosine evaluations and the complete earlier time interval. |
| W46 | plateau counterexample | Incorporates the supplied audit's exact dyadic counterexample; no novelty claimed. |
| W47 | local-defect null | Exact odd-phase family rejects transfer of the cap without a local-error term. |
| C48 | normalizer | Recurrence and beta-integral remainder bounds, checked with rational/directed arithmetic. |
| V49 | Weyl endpoint window | Three checks behind Lemma 19.1, all in 200-digit arithmetic: the physical/auxiliary discrepancy on $[B/3,B]$ against the band level spacing, with the assertion that $\log(\text{ratio})/B$ stays in a fixed band near $-0.665$ (exponential and **not** superexponential); the flatness of the Dirichlet ground function at the far end, $\varphi_B^2\to1$; the resistance ratio $\pi_B^0R_B\to1$, which is what makes the proved relative error $O(B^{-1})$ rather than $O(B^{-2})$; the edge weight $\pi_B^0\sqrt{\pi B}\,2^{B}/2\to1$; the one-sided capacity form with $A_R^0:=0$ against exact eigenvalues at $B=60,120,240$; and the window gap, $\operatorname{gap}\cdot B\to2$, which is why the lemma is proved through the perturbed ground function and not by perturbing an eigenvector. The chain is built from (10.8), not from the binomial Ehrenfest generator. |
| V50 | diffusive window | Eight quantities behind Theorem 22: the Ornstein–Uhlenbeck profile; the gap derivative; the suppression of the centre difference; $JT_\ell/B^{3/2}\to\tau_\ell$; the centre ratios $\Delta_1/\Delta_0\to3$, $\Delta_2/\Delta_1\to5/3$ and $\Delta_0B^2\to2\Lambda''(0;K)=0.52870$, which refute the draft's "$\Delta_{k+1}/\Delta_k\to1$"; the finite $K$-table reporting the two exponential rescalings and a decreasing sampled $e^{2K^2}$-normalised column, without establishing or refuting a growing-$K$ asymptotic; the adjacent ground-vector overlaps used for $\Gamma_B\to1$; and (v1.5) the Lemma 22.1 curvature bound (10.26a) at $K=1,1.5,2$, with the unresolved $K=3$ values recorded outside the verdict. |
| V51 (C51 in v1.4) | rate-function envelope | Exact extremal orbit means and entropy affinity behind Corollary 23, plus an independent numerical $\mathcal I_q$ from even-length periodic-orbit pressure sums: no violation of (10.30) on a 25-point grid, the three claimed equalities to $5\times10^{-4}$, and genuine interior slack. The $q=2$ freezing probe of Section 14 is recorded in the same row under a field explicitly marked unasserted; the row's verdict does not depend on it. Retyped V in v1.5: its verdict uses floating cosines, finite periodic sums and a finite grid (v1.4 audit F14-06). |
| V52 | corrected Lemma 19.1 | The finite trace bound (10.19a) of the v1.4 audit — $0\le D\le V\le(A_*\lambda_D^0+B_*)/(1-A_*)$ — at $(B,l)=(24,8),(24,16),(48,16),(48,32)$ in $90$-digit arithmetic, two of them with $l>B/2$ where the v1.4 anchor lay outside the window. |
| C53 | Theorem 24 / Proposition 24.1 constants | Exact rational enclosures of $\delta_2$, of $A_q$ and $B_q$ with explicit tails (the $A_2$ enclosure contains the audit's), of the witness bound $P_2(-15)-\tfrac{15}2>5.6076\times10^{-6}$ (own implementation, conditional on (10.36)–(10.37)), of the chain (10.44)–(10.47) at $q=6,\dots,20$, and of $q^3A_q$ increasing towards $2\pi^2$. |
| V54 | Theorem 24 numerics | The Markov defect $D_\varepsilon$ against $A_q\varepsilon+C_q\varepsilon^2$ for $q=2,4,6$ (remainder ratio at most $0.34$ against $C_2=12.57$), and the v1.4 finite-period pressure estimate reproduced and shown to lie more than two orders of magnitude below the certified bound. |
| C55 | Theorem 25, Part A | Symbolic identities (10.54), (10.56), (10.57) and the $q=2$ term identity; the sign facts $m(\pi/q),m(\pi/4),m(\pi/2)<0$, $\varepsilon^+(q)>\tfrac14$ and $\eta_2(q)>\tfrac1{20}$ increasing, in rational interval arithmetic for even $q\le40$. |
| C56 | Theorem 25, Part B | Exact certificates of (C1)–(C2) at $\varepsilon\in\{-\tfrac1{20},0,\tfrac14\}$ for $q=4,6$, at $\varepsilon=0$ for $q=2$ (which completes Proposition 24.1 there), and at two printed **rational** points $\varepsilon_{\rm lo}(q)<0<\varepsilon_{\rm hi}(q)$ strictly inside $(-\eta_2(q),\varepsilon^+(q))$ for even $4\le q\le40$ (FULL profile); the row requires $c_\varepsilon>0$ and therefore never reaches $\varepsilon^+(q)$ (v1.5 audit F15-02). Directed rational arithmetic throughout; concavity in $\varepsilon$ extends each pair of certificates to the interval between them, and (10.65) additionally uses C59. |
| V57 | Theorem 25 numerics | The fixed-point crossing $\varepsilon_f(q)$ of (10.66) and its ordering above $\varepsilon^+(q)$; exhaustive periodic-orbit minimisation over an $\varepsilon$-grid for $q=4$ (period $10$) and $q=6$ (period $8$); the first crossing among orbits of period $\le P$ (the period-four orbit, strictly below $A_q/|B_q|$) as a **finite-period diagnostic** that does not determine $\varepsilon_{\rm crit}$ (F15-03); branch-and-bound survivors at six $(q,\varepsilon)$ pairs inside the certified intervals; the grid validity range of the tent. Floating exploration only. |
| W58 | withdrawn v1.5 bounds | Exact rational values of the two v1.5 "for all $q\ge8$" brackets at $q=2000$ and $q=1000$ (both negative), the two rounded constants $\sin(\pi/9)/(\pi/9)<0.98$ and $2\cos(\pi/9)-1.2\pi\sin(\pi/9)<0.59$ in rational interval arithmetic, and positivity of the repaired bracket at the same $q$. Witnesses against the v1.5 proof chain, not against the theorem. |
| C59 | Theorem 25 at $\varepsilon^+(q)$ | The complete-square identity (10.64b) symbolically; $D_q\ge933/1280$; direct exact enclosures of $C_1(\varepsilon^+),C_2(\varepsilon^+)$ from the series for even $q\le40$, each above the closed-form bounds $K_qD_q$, $K_qD_q/q^2$; positive-coefficient polynomial certificates ($q=t+8$, resp. $t+4$) for the repaired universal brackets (10.64a), the repaired $\varepsilon=\tfrac14$ bracket and $D_q>0$. |
| C60 | Theorem 26, bracket | The period-four orbit in exact rationals (minimal period $4$), $\varepsilon_4(q)$ enclosed, and $\varepsilon^+(q)<\varepsilon_4(q)<A_q/\lvert B_q\rvert$ for even $q\le40$. An upper bound on $\varepsilon_{\rm crit}$, not its value. |
| C61 | Theorem 26, asymptotics | Exact symbolic Taylor coefficients of $\varepsilon_4$ and $\varepsilon^+$ in $x=1/q$ (agreement through $x^2$, first difference $\pi^2x^3/4$) and the order-$3$ common zero of numerator and denominator. |
| C62 | Proposition 27 | $R(4)=375/64$, the identity $(1+\tfrac{311}{439})/(1-\tfrac{311}{439})=375/64$, and for $h=1+\tfrac12\cos3d$ at $q=4,6,8,10,20$ the enclosed series cost $E_{q,h}$ (60 terms plus a non-negative tail bound) and the positive certified excursion gap $\tfrac12K_qD^{(3)}_q/q^2$. |
| W63 | Example 27.1 | The $q=4$ bump weight: support avoidance of every candidate point except $d_2$ and of the whole alternative path, exact enclosures of $E_0$, $w_2$, $D$, the failure margin at $R=64$, and the bracket $375/64\le R_{\rm crit}\le R_{\rm alt}$. |
| G64 | certificate serialization | Exact rational endpoint JSON round-trip and the q=4 algebraic enclosure; the float-collapse mutation must fail. |
| C65 | T28 Hermite jets | Symbolic value and derivative cancellation for arbitrary orbit values/slopes; symbolic cubic interpolation endpoints; the interpolation norm bound is proved in the text. |
| C66 | T28 constants and explicit extension | Exact ratio identity and positive all-path bracket; directed enclosures of K(q,k), rational safe radii, and the strict extension beyond epsilon-plus. |
| C67 | Cor29 raw third harmonic | Symbolic factorisation by the complete square, exact convex coordinates and weight-ratio certificate. |
| C68 | Cor29 transition | Symbolic cancellation through degree six after removing the common order-three zero, with eta symbolic; the uniform analytic remainder is proved in the text. |
| C69 | Cor30 sine switch | Directed positive series and tail enclosures at stated q, including the orbit endpoint term, sign bounds and the selected cost. Reflection and the termwise sign argument are proved in the text. |
| V70 | independent additive construction | Direct Hermite residual and both candidate costs; every off-orbit inverse prefix of depth three ending at p0 at q=4,6,8, followed by the specified ground-branch completion. The reflected candidate is evaluated separately. Finite floating attack, not the all-path proof or an exhaustive search of both endpoints. Two mutations test the residual prediction and omission of the endpoint compensation. |

The JSON is the machine-generated census. C means a finite exact identity/enclosure, V a numerical check, W a witness and G a guard. P=0 means that the code does not certify every analytic proof or any novelty/grade decision — the v1.5 audit's counterexample to a universal chain that no row checked is the concrete instance of this sentence. The inherited seed's 109 checks are not rerun or added to this census. The 45 live mutations are executed in fresh `python -O` processes against the designated comparator plus the registry, with QUICK-size inputs. This **SELF-TEST-TARGETED** profile tests genuine comparator sensitivity. It does not test whether every other row remains unchanged under the same mutation. The optional command `--self-test --self-test-all-rows` retains the expensive legacy all-QUICK-rows-per-mutation mode; that optional mode was not the released self-test run. The unmutated FULL run is separate.

**Historical census of v1.7.** FULL: **69/69 PASS (C31, V28, W8, G2; P=0)**. SELF-TEST-TARGETED: **45/45 genuine faulty predictions rejected at their designated comparator, in fresh `python -O` processes**. These were completed v1.7 executions and are inherited by v1.8; they were distinct from the earlier author-supplied v1.6 results. The inherited rows and their stated mathematical comparators are retained; seven rows G64–V70 and eight mutations are new. The executable ledger, not historical counts quoted in older appendices, controls this release. P=0 throughout.

**Saved interval contract.** EI enclosures carry rational-string `lo` and `hi` endpoints; `approx` is a display value only. Parsing uses `fractions.Fraction`. For example, the two rational endpoints of the $q=4$ $\varepsilon^+$ interval remain distinct even if both round to the same IEEE float. Exact directed-integer certificates retain their integer endpoints and scale. Floating diagnostic pairs elsewhere in the ledger are not upgraded to exact intervals.

**Row typing and tolerances (corrected in v1.4).** The single `tolerance` field in the JSON is the default floating comparison level; it is **not** the operative threshold of most V rows, which state their own in their scope strings. Row C18 asserted non-negativity of the extremal kernel on a 4001-point floating grid while typed C; it now certifies the exact sum-of-two-squares identity instead. The remaining C rows that still carry a floating conjunct — C01 (a redundant float cross-check beside the exact Sturm certificate), C05 (numerical quantiles beside a symbolic density identity), C24, C29, C30, C31, C39 — disclose it in their scope, and in each case the exact part alone carries the row's claim.

**Fault injection (corrected in v1.4).** The six mutations added in v1.3 were not fault injections: each conjoined the negation of a condition already asserted in the same predicate, so the designated row was guaranteed to fail and nothing about the comparator was tested. All six now inject a genuinely false prediction — the first-loss threshold one dyadic cell early, a Dirichlet shift above twice the capacity bound, the defect-free right-hand side of Theorem 20, the false equality $\delta_B=a_B$, the plateau family reaching the loss, and a normalizer remainder outside the proved band — and the three rows new in v1.4 carry genuine ones as well.

**Limits.** Historical V14 scans still use floating postprocessing and are not exact certificates. C45 is separate and bounded in size. The explicit exact-arithmetic operations and Taylor remainder establish its enclosure mechanism; it is not an externally audited proof assistant. Same author lineage and shared model definitions remain disclosed.

## Appendix R3. The v1.2–v1.5 audits, and the v1.3–v1.6 additions

**Historical integration record.** This appendix records the v1.4/v1.5 audits and the v1.6 response. Version-relative statements and run counts below refer to those targets. Current v1.6-audit integration and new results are in R4; the current run ledger is Appendix V. Lineage files mentioned here remain attributed to their original bundles and are not asserted to have been re-supplied in this release.


| Source finding | Integrated repair |
|---|---|
| F01 | Strict crossing (9.1e), corrected T9/T13 applications, variable-capacity root statement and incorporated atomless plateau counterexample W46. |
| F02 | Unrestricted old H(z) upper inequality removed; atom-aware (9.1a) retained. |
| F03 | One-sided exponential inference withdrawn; audit (10.11) incorporated, then T18 supplies rational sharp bounds and leading coefficients. |
| F04 | S8.1 noncommensurability ranges only over distinct nonnegative gap representatives. Mirror edges are permitted. |
| F05 | Current V35 labels and V23 numerical scope synchronized. Historical correction logs remain historical. |
| F06 | Both T14 conditions appear in current summaries. The old 3% statement is superseded: B=16 has about 3.3525% relative shortfall or 3.4688% ratio excess. |
| New T18/T19 | Exact boundary Green construction, normalizer remainder, Weyl correction and specified parent transfer. |
| New T20/P21 | Local phase-defect theorem and exact finite-matrix first-loss certificate. |

### The v1.3 audit and the v1.4 repairs

| Finding | Severity | Repair in v1.4 |
|---|---|---|
| Theorem 19 stated for $a+b<1/2$ but applied to $(a,b)=(1/3,1/6)$, where $a+b=1/2$ and the extreme windows touch a lattice end, so the exact window identity (10.19) fails there | statement error, conclusion survives | hypothesis corrected to $a+b\le1/2$, the endpoint convention $A_R^0:=0$ at $u=B$ stated, and **Lemma 19.1** added: the neglected term is a sign-definite rank-one endpoint perturbation of **proved** relative size $O(B^{-2})$ (measured size $e^{-0.665B}$); row V49 measures it against the level spacing at $B=24,48,96$, and also checks the ground-function flatness and the one-sided capacity form |
| §12.4 cited Theorem A of Aistleitner et al. for integer geometric frequencies; Theorem A assumes $a_{k+1}/a_k\to\infty$, which excludes them | citation error | pointer corrected to **Theorem B**; the quoted open sentence after Lemma 2.3 is unaffected and was re-read in two independent copies |
| Row C18, typed C, checked kernel non-negativity on a 4001-point floating grid at $-10^{-12}$, undisclosed | row typing | replaced by the exact identity $K=(\Re P)^2+(\Im P)^2$ over $\sum_js_j^2$ |
| The six mutations added in v1.3 were negations of already-asserted conjuncts | verification hygiene | all six replaced by genuine false predictions; see Appendix V |
| C45's Lipschitz bound used $\sum\omega_i|\Delta_i|$ without asserting $\omega_i>0$; the largest-eigenvalue bracket was widened once without a loop or an invariant check; `--quick` reduced Proposition 21 to $B=24$ silently | three soundness gaps, none triggered at the certified sizes | positivity is now asserted and raises on failure; the bracket loops and both invariants are checked; the reduced profile is recorded in the row |
| One block of §9.1 was printed in Korean | language | translated, mathematics unchanged |

What the audit did **not** find is as much to the point: Theorem 18's enclosure, expansion and normalizer bounds, Theorem 20 with its $340$ adversarial configurations, Proposition 21's three certified intervals — recomputed from scratch with a different eigenvalue engine, the true values falling at $37\%$, $48\%$ and $73\%$ of the way across their brackets — and Theorem 13's value and uniqueness all survived. A search of the ergodic-optimisation literature for any source computing the maximal cosine average under $x\mapsto qx$ for general $q$ returned nothing, and the three nearest candidates were read in the primary text and do not subsume it.

### The v1.4 pre-shipping referee pass and what it changed in v1.4 itself

The two new v1.4 results were attacked before shipping, with independent numerics. Corollary 23 survived in substance; Lemma 19.1 and Theorem 22 did not survive as drafted.

| Finding in the v1.4 draft | Severity | Repair, in this version |
|---|---|---|
| Lemma 19.1's chain (10.19a) asserted $\varphi_B^2\le2Ce^{-BI(1/2)}$; the true endpoint value tends to $1$ ($1.599853,1.207699,1.021709,1.000161$ at $B=24,48,96,192$), so the printed inequality fails by a factor $2^{B}$ | **false displayed inequality**; conclusion survives | statement and proof replaced: two one-sided Rayleigh quotients plus a path Cauchy–Schwarz give (10.19a)–(10.19b) with relative error $O(B^{-2})$, which is what (10.20) needs |
| The mechanism sentence — the ground function "decays towards the far end with the reciprocal of the stationary weight" — asserts $\pi_B^0\varphi_B^2\asymp(\pi_B^0)^{-1}$, contradicting its own $L^2$ normalisation $\pi_B^0\varphi_B^2\le1$ by 15 orders of magnitude at $B=24$ | **false mechanism** | corrected: the ground function is essentially flat at the far end and $\pi_B^0\varphi_B^2\asymp\pi_B^0$, one factor of the weight, not two; checked in V49 |
| "First-order perturbation with the exact remainder sign" | unlicensed step (fixed-size perturbation against an exponentially small gap) | replaced by one-sided Rayleigh–Ritz, which needs no radius of convergence |
| Loewner direction left ambiguous, and the ordering $0\le\lambda_D-\lambda_D^0$ printed the wrong way round | sign error | $C-C_0\succeq0$ stated explicitly, giving $\lambda_D\le\lambda_D^0$ |
| "A relative size that falls superexponentially" | **false**, and contradicted by the paper's own row | the relative sizes have $\log/B=-0.665$ at all three sizes: exactly exponential. V49 now asserts a constant slope |
| $A_R^0$ returns $-\pi_B^0/(2B)<0$ at $u=B$ | negative capacity, a symptom of extrapolating past the lattice end | endpoint convention $A_R^0:=0$ stated; the one-sided form $\lambda_D^0=A_L^0[1+O(B^{-1})]$ checked in V49 at $B=60,120,240$ |
| Theorem 22(iii) claimed $\Delta_{k+1}/\Delta_k\to1$ across the band, contradicting its own (ii) | **false at the centre**: $\Delta_1/\Delta_0\to3$, $\Delta_2/\Delta_1\to5/3$, $\Delta_0=\Theta(B^{-2})$ | (iii) restated with the centre behaviour and the constant $2\Lambda''(0;K)=0.52870$; V50 checks all three |
| (10.27) printed the limit as $\Lambda'(c_k;K)>0$ for all $|k|\le w$ | **false on the negative half** ($\Lambda$ is even, $\Delta_0/\Delta_{-1}=-1$) | sign restricted to $c>0$, with the reflected statement given |
| The proof of (ii) deduced difference-quotient convergence from Rayleigh–Ritz eigenvalue convergence, but the error in (i) is itself $\Theta(B^{-1/2})$ — at $B=25600$ it is $79\times$ the difference extracted | **invalid proof step**; conclusion true | replaced by a Gamma-continued holomorphic family in the window centre plus Vitali's theorem and Cauchy estimates, which does give convergence of derivatives, uniformly on the whole band |
| "Positivity of $\Lambda'$ for $c>0$ is the monotonicity of a Dirichlet eigenvalue under translation" | restatement, not an argument | replaced by the explicit tilt representation and Hellmann–Feynman |
| "$\Lambda(\cdot;K)=\Theta(Ke^{-2K^2})$" | true at $c=0$ only; at $c=1$ the ratio runs $34.6,106.4,311.0$ for $K=2,2.5,3$ | restricted to the centre, with the two-sided Kramers form given |
| "$\Lambda'=\Theta(Ke^{-2K^2})$, so that constant grows like $e^{2K^2}$: the sentence v1.0 printed … is the correct order in its $K$-dependence. It now has one [a proof]" | **overclaim, retracted**: $\Lambda'(c;K)=\Theta(K^2e^{-2K^2+2Kc})$, and the first-loss constant grows like $e^{2(K-\kappa)^2}$, differing by the unbounded factor $e^{4K\kappa-2\kappa^2}$ | the vindication claim is withdrawn; the $K$-table is printed and checked in V50, and the growth law is labelled **[HYPOTHESIS]** |
| (iv) asserted a Riemann sum needing uniformity that (ii) had been stated without | uniformity gap | (ii) now holds on the whole band, so the gap closes; the alternative central-strip argument is recorded in parentheses |
| Corollary 23: "$\mathfrak c$ is the maximising two-cycle measure" | sign convention: here it *minimises* $\int c\,d\nu$ | wording fixed |
| Corollary 23: equality at $s=-\beta_q$ silently needs every endpoint-attaining measure to have zero entropy | delegated hypothesis | made explicit as the content of Theorem 16 |

### The second pass, on the repairs themselves

The rewritten sections were attacked a second time, and seven more defects appeared, five of them introduced by the first round of repairs.

| Finding in the repaired text | Severity | Repair, in this version |
|---|---|---|
| "$R_B$ is dominated by its last term and $R_B\asymp(B\pi_B^0)^{-1}$" | **false second half**: by (10.22), $a_{B-1}^0=\tfrac{2B-1}{2B}\pi_B^0$, so $R_B\ge(\pi_B^0)^{-1}$ and $\pi_B^0R_B\to1$ ($1.0458,1.0218,1.0106,1.00526$) | the proved relative error is restated as $O(B^{-1})$, which is the order (10.20) carries anyway; V49 measures $\pi_B^0R_B$ |
| "$\lambda_D^0(I)-\lambda_D(I)\le\dots=O(B^{-2})\lambda_D^0(I)$" and "the rigorous relative error is thus $O(B^{-2})$, which is what (10.20) needs" | claimed more than proved, and internally inconsistent with "absorbed by the $[1+O(B^{-1})]$" two paragraphs earlier | both corrected to $O(B^{-1})$; the measured exponential size is reported separately and explicitly not claimed as proved |
| The $\psi\to\varphi$ step: "their endpoint components differ by a relative $O(B^{-1}[\nu-\nu_0]/\mathrm{gap})$, and the gap of $C$ on $I$ is bounded below uniformly" | **no proof, and a false premise**: (10.10) gives only $\operatorname{gap}\ge3/(2B)$, measured $\operatorname{gap}\cdot B\to2$, so $\|C-C_0\|/\operatorname{gap}\to1/4$; the quoted bound is also numerically too small by $\sim10^{30}$ | the step is deleted: the whole estimate now runs on the perturbed ground function $\chi$ and no eigenvectors are compared. V49 records the gap |
| $\varphi_B^2=1.650,1.221,1.023,1.000$ and $\lambda_D^0/A_L^0=0.9504,0.9646,0.9852$ | computed on the **binomial Ehrenfest chain**, not on this paper's $\pi^0_b\propto\binom{2B}{2b}/\binom Bb$ | recomputed: $1.599853,1.207699,1.021709,1.000161$ and $0.939104,0.959245,0.982274,0.991726$; V49 now builds the chain from (10.8) |
| "the absolute discrepancies match $2^{-B}/(2B)$ to within a factor 3" and "$-0.665B$ to three digits … exactly exponential" | **false** at $B\ge96$ (the ratios are $0.379,0.199,0.118,0.082$) and an overstated three-point fit (slopes $-0.6649,-0.6673,-0.6608$, drifting) | the $B^{-1/2}$ is restored, $\nu-\nu_0\sim\pi_B^0/(2B)$ with $\pi_B^0\sim(2/\sqrt{\pi B})2^{-B}$; noted that (10.23) is short by $\sqrt2$ at the lattice edge, which is where the factor went |
| Theorem 22(iii): "$\Delta_k=2\Lambda'(c_k)B^{-3/2}(1+o(1))$ **uniformly in $|k|\le w$**" | **false at $k=0$**, where the right side is identically zero — the same error the paragraph beneath it was correcting | absolute and relative forms separated in the display |
| Centre expansion "carried one order further with $\Phi_B'(0)\to\Lambda'(0)=0$" | dominant term dropped: $o(1)\cdot c_1=o(B^{-1/2})$ swamps the retained $\Theta(B^{-1})$ | replaced by **exact** evenness of $\Phi_B$ ($b\mapsto B-b$ maps $I_\mu\to I_{-\mu}$ and fixes the entries), so $\Phi_B'(0)=0$ identically; V50 checks it at non-integer centres |
| "Replacing the factorials by Gamma functions extends every entry" | vacuous: the entries are algebraic in $\mu$ and contain no factorials | rewritten as a direct algebraic continuation, with the parity of $B$ fixed |
| "by (i) the spectral gap above it converges to the gap of the OU Dirichlet problem" | (i) controls the lowest eigenvalue only | replaced by the min–max transfer of the second level |
| "$\partial_c\Lambda$ is … the $\Lambda$-weighted covariance $\int y\,d\varrho_c$ … strictly positive because the tilt shifts the ground density towards the near barrier" | the formula is right but is a **mean**, not a covariance, and only via $\mathcal Ay=2y$; the stated reason argues for the **wrong sign** | corrected, and positivity demoted to a numerical observation used nowhere in the proof; the same demotion applied to "strictly increasing in $|c|$" |
| $\omega_k=c_kc_{k+1}\langle\psi_k,\psi_{k+1}\rangle$ | symbol collision: $c_k$ is the window centre in the theorem's own statement, so $c_0=0$ and $\omega_0=0$ | sine coefficients renamed $s_k$; the overlap argument now also accounts for the one-site lattice shift, which is the dominant term at the band centre |
| "the first-loss constant is governed by the **outer** edge of the band" | unhedged: $\rho(\pm1)=0$, so the outermost modes carry no weight | marked heuristic, with the boundary-layer analysis named as what is missing |
| $\Lambda(0;3/2)=0.04789264$, $\Lambda''(0;3/2)=0.264361$ | wrong in the last digits | $0.04789260$ and $0.26435$, Richardson-extrapolated; V50's tolerances widened to match its own coarser solver |
| Corollary 23 slack "$0.613$ at $s\approx-0.58$", equalities "to $5\times10^{-4}$" | grid maximum reported as if it were the true maximum; the estimator was not stated, and a bare orbit sum does not reach $5\times10^{-4}$ | grid and finer-grid values both given ($0.2791/0.6126$ on the grid, $0.2794/0.6144$ refined), and the estimator $P(t)=\tfrac12\log(Z_n/Z_{n-2})$ over even $n$ stated with the reason |

Three things are worth recording about these two passes. First, every *conclusion* of Theorem 22 and of Lemma 19.1 survived both; what failed, repeatedly, were the routes to them. Second, five of the seven second-round defects were **created by the first round of repairs** — a repair is a new claim and needs the same scrutiny as the claim it replaces, which is the argument for running the pass twice rather than once. Third, almost every failure was findable by numerics the paper could have run and had not: the flatness of $\varphi$, $\pi_B^0R_B\to1$, $\Delta_1/\Delta_0=3$, the window gap, the $K$-table. The verifier rows have been extended so that a future version cannot reprint any of these particular sentences and still pass.

### The v1.4 audit (cross-family) and the v1.5 repairs

The audit re-ran the shipped v1.4 verifier unmodified (50/50 PASS, 26/26 mutations, all non-runtime fields identical), ran an independent 14-row audit script with five targeted mutations, and read the sources. Its verdict on v1.4 as shipped: **correctness FAIL, repairable, severity S2**; on the repaired claims: PASS in the specified mathematical scope; supported research grade 3, target 4 not established. Every finding and its treatment here:

| ID | Finding (v1.4) | Severity | Treatment in v1.5 |
|---|---|---|---|
| F14-01 | Lemma 19.1 allowed $l>B/2$ but used the anchor $b_0=\lceil B/2\rceil\in I$; at $B=24$, $l=16$ the anchor is outside the window | S2 | anchor $b_*=\max\{l,\lceil B/2\rceil\}$; proof rewritten over the whole declared range (§10.5); row V52 |
| F14-02 | $\mathcal E(\chi)=\lambda_D+V\le\lambda_D^0+D$ does not follow from the Rayleigh argument (it needs $V\le2D$) | S2 | replaced by $\mathcal E(\chi)\le\lambda_D^0+V$ and the finite trace bound (10.19a), solved for $V$; the printed step did not follow, no counterexample is asserted |
| F14-03 | oddness of $\Lambda'$ does not give its sign; the relative error, the centre $\Theta$ and the ratios need $\Lambda'\ne0$ and $\Lambda''(0)>0$ | S2 | Lemma 22.1 (audit): convexity via Colesanti et al., $\Lambda'>0$, and the own bound $\Lambda''(0)\ge1-(1+\Lambda(0))^{-2}$ |
| F14-04 | "finite adjacent ratios are bounded by $3$" contradicts the paper's own $3.00456$ | S2 | sentence withdrawn; fixed-$k$ limits retained |
| F14-05 | $J$ missing in Theorem 22(iii); even-$B$ hypothesis inconsistent; global inverse $\mathfrak M^{-1}$ | S1 | $\Delta_k/J$; even $B$; first contact $\tau_\ell$ with strict crossing |
| F14-06 | C51 typed C but numerical | S1 | retyped V51 |
| F14-07 | finite-temperature freezing left OPEN | S2 (research state) | closed by pressure analyticity (imported); T24 quantitative (§10.8) |
| F14-08 | the low-temperature periodic sum's slope and negative values read as rounding | S2 (numerics) | the estimate lies $>500\times$ below a certified lower bound on the true defect; estimator withdrawn (§10.8, rows C53, V54) |
| F14-09 | "bounded adjacent ratios exclude lacunarity"; $B^{3/4}$ called a dynamical transition | S2 (scope) | both withdrawn (dyadic counterexample; $B^{3/4}$ is a precision boundary of a substitution) — §10.6 |
| F14-10 | $2(K-\kappa)^2(1+o(1))$ read as fixing a $\kappa$-dependent ratio and a linear correction | S1 | same leading content as $2K^2(1+o(1))$ stated; the correction is OPEN — §10.6 |
| F14-11 | lineage, absence of human review and external impact mixed into the grade | S2 (operational) | AI-use record corrected (cross-family audits); Mission v1.7 applied — human review is disclosed, not a gate — §13.1 |
| F14-12 | summary, claim cards, mutation count and history mixed with current state | S1 | synchronised: T22, T24, 24.1, T25 cards; 26 mutations in v1.4, 31 in v1.5 |

**What the audit added and what was checked here.** Theorem 24 and Proposition 24.1 were written by the audit. Re-checks in this version, all recorded in rows C53–V54: the constants $\delta_2$, $A_q$, $B_q$, $C_q$; the witness bound (10.39) with an independent implementation; the chain (10.44)–(10.47) at $q=6,\dots,20$ (the printed margin $1403/13230$ is a valid uniform lower bound; the actual margin is $0.53$ at $q=6$); the remainder (10.36) numerically; and the imported theorem's statement in its source. **Not available in the v1.5 authoring session (corrected in v1.6):** the audit cites `verification/barrier_certificate.py` and `.json` for the $q=2,4$ cases of Proposition 24.1 and a table of certified bounds (its (10.48)). v1.5 wrote that neither file was in the bundle; the v1.5 audit opened the v1.4 audit ZIP and found both (6,670 and 34,465 bytes, plus a 135-byte self-test), so the correct statement is that they were not available to the session that wrote v1.5 (finding F15-06). Those cases are proved by other means (§10.9, Lemma 25.4, row C56), the certificate is not relied upon, and the files are carried as lineage in `provenance_v14/` of the v1.6 bundle. **Not adopted as stated:** the audit's "$P_2(-15)-15/2>5.60749\times10^{-6}$" is reproduced as $5.6076\times10^{-6}$ by this version's own rational bound (the two agree to the printed precision); the audit's independent OU values $\Lambda(0;1.5)=0.04789260128606$ and $\Lambda''(0;1.5)=0.26434737593$ agree with the Richardson values of v1.4 to $8$ and $5$ digits respectively and are recorded in §10.6. **A point on which this version goes further than the audit:** the audit's own history rows and its report describe the Claude-authored v1.4 as audited cross-family; that is adopted, and the earlier "same lineage" statements are corrected rather than deleted.

### The pre-shipping referee pass on Theorem 25 and §§10.8–10.9

Before shipping, §§10.8–10.10 were attacked by an internal referee pass (Claude, separate context) with independent numerics (mpmath at 30–40 digits, grids up to $8\times10^6$ points, sympy for every identity, exhaustive periodic-orbit enumeration). Every theorem statement survived; the discussion of sharpness did not, and the following were corrected in the text above.

| Finding in the draft | Severity | Treatment |
|---|---|---|
| §10.10.4 named the fixed point $x_f$ as the first competitor of the two-cycle and placed the transition at $\varepsilon_f(q)$, while printing $A_q/|B_q|<\varepsilon_f(q)$ — an internal contradiction, since $A_q(\varepsilon)<0$ already forces a competitor | substantive | v1.5 replaced it by the period-four orbit $aabb$ as "the actual first competitor at $\varepsilon^*(q)$" and added a "theorem predicts its own breakdown" observation; the v1.5 audit then showed (F15-03) that a finite-period search cannot name a global first competitor and that the period-four crossing lies strictly *below* $A_q/\lvert B_q\rvert$, so both the "$\varepsilon^*$" and the "breakdown" sentences are withdrawn in v1.6 in favour of the bracket of Theorem 26 |
| §10.10.3 claimed (C1)–(C2) fail "slightly before Part A does" near $-\eta_2(q)$ | false explanation | with the true minima both inequalities hold on the whole proved range with large margins; the draft's search had the Part A range built into it; sentence withdrawn and the endpoints of (10.65) attributed to the proof of Part A |
| "no other sub-action is constructed" for $\varepsilon<-\eta_2(q)$, and "the upper endpoint is the natural limit of this method" | misdescription | the same tent certifies $r_\varepsilon\ge0$ on a grid down to about $-3\eta_2(q)$ and slightly beyond $\varepsilon^+(q)$; the loss is in the two-line bound of the proof; §10.10.4 rewritten, V57 measures the grid range |
| Lemma 25.1: "$r_\varepsilon\ge G_\varepsilon(d)$ always" | wrong word | needs $c_\varepsilon\ge0$; corrected |
| analytic chain at $\varepsilon=-\tfrac1{20}$: "$2a\sin a/(q+1)\ge1.96a^2/(q+1)$" | arithmetic slip ($2\sin a/a=1.9596$ at $q=8$) | constant changed to $1.95$ |
| §10.9 said the Lipschitz route "fails for $q\le4$" | inaccurate | it fails only at $q=2$; at $q=4$ the audit's own quantity is $+0.303\,\alpha^2/(q+1)$ and only its printed uniform constants fail; corrected |
| §10.9 used Lemma 25.4 at $q=2$ under a $q\ge4$ standing hypothesis | scope | the lemma holds at $q=2$ (checked for $j\le5$); stated, together with the interior minimum in $R_{\rm dev}$ at $q=2$ |
| Lemma 25.5 passed from finite paths to infinite excursions without comment | gap in exposition | the $O(\epsilon'^2)$ completion argument is now stated |

What the pass confirmed, in its own computations: the identities (10.54), (10.56), (10.57) and the $q=2$ term identity (exact); every sign fact in the proof of Proposition 25.2 for $q=4,\dots,40$ and every constant of the analytic chain for $q=8,10,12,20,50,200$ — a finite sample that, as the v1.5 audit then showed with $q=1000$ and $q=2000$, did not test the universal bracket and could not have; the path, brackets and $A_q(\varepsilon)=A_q+\varepsilon B_q$ to $39$ digits; both parities of (10.60) for $j\le5$; the exhaustiveness of the case split and the concavity argument; the certified margins of C56; the constants of Theorem 24 and Proposition 24.1 including $A_2$ to $18$ digits; and the statement of the imported theorem as far as it could be read from the arXiv text. It could not verify the full-text hypotheses of Leplaideur–Mengue's Theorem A beyond the abstract and the statement, which is recorded in §12.5 as the remaining reading obligation.

### The v1.5 audit (cross-family) and the v1.6 repairs

The audit (ChatGPT; report dated 2026-09-16 UTC; bundle with original inputs, the original FULL and self-test re-runs, an independent 9-row exact script `zs_m72_independent_audit_v1_5.py` with five fault injections, input hashes and the v1.4 certificate lineage) re-ran the shipped v1.5 verifier unmodified (56/56 PASS, 31/31 mutations; one numerical field differing by $5.55\times10^{-17}$, no non-numerical difference), read Leplaideur–Mengue, Yuan–Hunt, Contreras and Contreras–Lopes–Thieullen in the primary texts, and attacked §10.10 along twelve axes. Its verdict on v1.5 as shipped: **correctness FAIL, repairable, severity S2**; supported research grade 3; grade 4 not established, for reasons of significance evidence and not of independence. Every finding and its treatment here:

| ID | Finding (v1.5) | Severity | Treatment in v1.6 |
|---|---|---|---|
| F15-01 | the large-$q$ brackets of the Theorem 25 proof, asserted positive for all $q\ge8$, are $-2.55\times10^{-5}$ at $q=2000$ and $-1.04\times10^{-3}$ at $q=1000$ ($q$-independent tail constants); $\sin(\pi/9)/(\pi/9)<0.98$ and $2\cos(\pi/9)-1.2\pi\sin(\pi/9)<0.59$ were used as bounds | S2 | proof replaced by the audit's (§10.10 Part B): $q$-dependent tail at $\varepsilon=-\tfrac1{20}$ (10.64a), complete square at $\varepsilon^+(q)$ (10.64b)–(10.64c); theorem extended to $[-\tfrac1{20},\varepsilon^+(q)]$; rows W58, C59 |
| F15-02 | C56 certifies rational points strictly inside $(-\eta_2,\varepsilon^+)$, not "the whole proved range"; $0.2775$ printed for $q=6$ exceeds both the certified $0.2774$ and $\varepsilon^+(6)$ | S2 | (10.65) restated with the exact certified rationals, extended to $\varepsilon^+(q)$ only via C59 and concavity; "whole range" withdrawn; C56 claim/scope text corrected; C not demoted to V since the chosen rationals are certified exactly |
| F15-03 | finite-period search (period $\le10$) reported as the global transition $\varepsilon^*(q)$; "transition is where the excursion becomes free" contradicted by $\varepsilon_4(4)<A_4/\lvert B_4\rvert$; "$2\%$" mixed the common endpoint with the per-$q$ endpoint | S2 | replaced by Theorem 26 (bracket $\varepsilon^+\le\varepsilon_{\rm crit}\le\varepsilon_4$, asymptotics (10.69)–(10.70)); V57 re-labelled a diagnostic; rows C60, C61 |
| F15-04 | (10.64) called a procedure that decides any $(q,\varepsilon)$ outside the proved interval | S2 (research) | "sufficient certificate under the stated hypotheses; a failed test is inconclusive" — §10.10.4, §12.5, §13.1; not counted as an algorithmic achievement |
| F15-05 | Yuan–Hunt Proposition 4.1 misquoted as an open stability set around every potential with a periodic optimum; Contreras/CLT conditions not stated | S2 (research) | §12.5 rewritten from the audit's primary-text reading; explicit sub-action is the direct evidence; locking cited as background; the "not re-read" debt closed by the audit's reading (this session could not fetch the texts and says so) |
| F15-06 | "certificate files not present in the delivered bundle" was false (they were in the v1.4 audit ZIP); "first cross-family audit" vs "five cross-family audits" | S1 (ops) | "not available in the v1.5 authoring session"; files carried as lineage; ordinal removed and generators named per result — Revision, §10.8, §10.9, Appendix R3, AI-use record |
| F15-07 | four-entry $K$-table read as proving the absence of a positive lower bound for $\tau_\ell/e^{2K^2}$; "$B^{3/4}$ crossover" in §13; stale "no general proof supplied" after Lemma 22.1 | S2 | §10.6: "the sampled ratios decrease; limit and uniform lower bound not determined by this table"; $B^{3/4}$ described as a substitution-accuracy boundary everywhere; Lemma 22.1 credited with the sign |
| F15-08 | at $q=2$, $d_1=2\pi/3$ is a maximum of $g_0$, not an interior minimum of $R_{\rm dev}$; verifier docstring said 23 mutations | S1 | sentence corrected in §10.9 (the certificate never depended on it); docstring says 37 |

**What the audit added and what was checked here.** The replacement proof of Theorem 25 (A15-1), Theorem 26 and Proposition 27 with Example 27.1 (A15-2, §7.3 of the report) were written by the audit. Re-checks in this version, all recorded in rows W58–W63 and in a separate mpmath/sympy recheck: the two counterexample values; the complete-square identity; $D_q$, $K_q$ and the direct $C_1,C_2$ enclosures at $\varepsilon^+$ for $q\le40$; the period-four orbit in exact rationals and the ordering $\varepsilon^+<\varepsilon_4<A_q/|B_q|$; the Taylor coefficients; $R(4)=375/64$, the $\tfrac{311}{439}$ threshold and the five example costs (to the printed thirteen digits); the bump example's support avoidance, $E_0$, $w_2$, $D$, $C(64)-D$ and $R_{\rm alt}$ (to the printed digits). The audit's independent script was re-run here unmodified (9/9 PASS). **Adopted with a change of emphasis:** the audit's §5.3 offered two repairs of the negative endpoint (with and without v1.5's derivative loss); the text uses the first (no loss to subtract, since $g\ge0$ on the short segments) and records the second as a polynomial certificate. **Not adopted:** nothing; no finding is disputed. **Beyond the audit:** the audit's row C15-07 certified the weighted example's gap with $m=\tfrac12$; row C62 does the same and additionally checks the $\tfrac{311}{439}$ identity exactly; row C59 adds direct series enclosures of $C_1(\varepsilon^+),C_2(\varepsilon^+)$ beside the closed-form bounds, which the audit did not print.

The old Appendix R and following preservation notes record previous versions. Their original exact-energy/superexponential/qualification statements are **SUPERSEDED where contradicted by §§9.1, 10.4–10.5 and 13**; they are not current assertions. Original files are preserved separately, so this integration does not erase evidence of the previous failures.

## Appendix R4. Integration of the v1.6 audit and the v1.7 research trace

The audited target is the exact uploaded v1.6 source; its manuscript SHA-256 is `1d925c11d4c63590fe3ae784a55baf89001ef87ff186610c2b64fb7204129d21`. The other original-input hashes, final artifact hashes and measured row changes are in `zs_m72_release_v1_7.json`. The audit's verdict is AUDIT-PASS-MINOR for its explicitly examined mathematical scope, with S1 local corrections. It did not certify the entire inherited corpus or complete the original FULL/SELF-TEST runs.

| Finding | Integration in v1.7 | Verification / preserved limit |
|---|---|---|
| F16-01: float interval endpoints can exclude the exact value | Every matched EI interval formerly printed as `[float(lo),float(hi)]` is now an object with exact rational-string `lo`, `hi` and a separate display-only `approx`. Runtime packing round-trips the strings. Existing exact DI/Fraction certificates are preserved. | G64 reproduces the q=4 algebraic enclosure and rejects a collapsed float interval. The final JSON is not treated as certified merely because it parses. The old artifact error is not relabelled as a theorem counterexample. |
| F16-02: historical positivity and K-table statements read as current | §13.1 now states Lemma 22.1's proved sign and current T22 dependence. Repeated superseded draft assessments were removed from the current assessment; their substantive correction history remains in Appendix R3, and the unabridged original v1.6 text is retained under the bundle's provenance/original_inputs. Appendix V's K-table scope is also corrected. | Current §10.6/§13.1/claim-card meanings were compared. Finite table values are not used to prove a growing-K asymptotic. |
| F16-03: unsupported absolute priority | The sentence claiming that no earlier value was known is withdrawn. §12.6 limits novelty to explicit primary-source comparisons and distinguishes the degree-two overlap. | Actual hypotheses, objects and conclusions compared; unsuccessful broad searches do not prove priority. |
| S0 wording: “exact endpoint of the sub-action” | Replaced in current summaries by the endpoint of the non-negative-slope proof. | Cor29 now proves a small extension beyond that point using a different sub-action, directly showing why proof endpoint and true transition must be distinguished. |
| Strongest-overlap comparison | The audit's LM A/B comparison is integrated and extended for T28–Cor30; it is CLOSED as a missing written comparison. | Grade 4 is reconsidered on significance, not left blocked by an already completed paragraph. |
| Original full-run reproduction gap | The final verifier runs every inherited row and every new row in its FULL profile. Mutation testing has an explicit targeted mode and an optional legacy all-row mode. | Actual completed-run results are in Appendix V and the release manifest. Targeted sensitivity is not described as checking every other row under each mutation. |
| Open obligations | Finite-q exact transition, negative transition, necessity of the certificate conditions (C1)–(C2), spin alignment, growing-K first contact and S14-derived instrument remain distinct. | Additive local stability is changed by proof; the unsolved stronger obligations are not silently closed. |

**Three substantive research rounds.** The work contract fixed FQ2/RQ3/RQ5, the additive-stability debt, SUPPORT/METHOD, the actual Tq model, and an all-path kill test before further construction. Round 1 obtained the cubic boundary factorisation, a convex two-parameter triangle and its transition bracket. Round 2 replaced imposed residual zeros by a periodic Hermite construction for arbitrary C2 perturbations, giving a quantitative domination bound and two-path reduction. Round 3 broke reflection symmetry with a sine perturbation and derived the path-selection corner. These are concrete results rather than candidate cards; the achieved scope is ESTABLISHED for the stated local construction and classification, while the grade-4 assessment remains separate.

| Breakthrough evidence-card field | Actual result and locator |
|---|---|
| Central result | T28 and Cor29–Cor30, §§10.13–10.15. |
| Construction / proof | Periodic Hermite interpolation cancels arbitrary orbit values and slopes; quadratic domination transfers the inherited geometric gap to a raw additive potential. Compensated telescoping evaluates the surviving costs. |
| Original obligation | The v1.6 audit §6.3, target 1: determine the ground orbit, sub-action, competitor exclusion and exact barrier for an additive two-parameter region without imposing the residual zero set. Cor29 meets it on the stated triangle; T28 enlarges the perturbation class locally. |
| Before → after | The fixed-factor multiplicative class did not identify a raw additive region or asymmetric cost. There is now a constructed additive neighbourhood, two cost functionals, a third-harmonic transition coefficient and an exact path-selection rule. |
| Closest prior collision | §12.6: qualitative C1 locking and the general pressure/max-plus mechanism are existing inputs. The explicit circle domain and all-path evaluation are the additional work; absolute priority is unclaimed. |
| Strong attack and outcome | Independent residual construction rejected the first cost formula's omitted endpoint term. The corrected term is retained and deliberately removed in a mutation. The universal path-gap proof addresses deviations at arbitrarily late indices. |
| Verification route | C65–C69 use exact symbolic/rational checks; V70 uses a separate numerical Hermite implementation and finite inverse prefixes. The all-path theorem is analytic, not extrapolated from V70. Execution profiles are in Appendix V. |
| Achievement status | BT-ROUTE / ESTABLISHED for this bounded mathematical obstacle. Research grade 4 is NOT ESTABLISHED; the current paper assessment remains 3 with candidate 4. |
| Remaining obligation | Global phase diagram, sharp radii and exact finite-q transitions; the distinct physical alignment and action-to-instrument obligations remain open. |

**A rejected first draft, preserved as a failure lesson.** The first formula for (10.77) omitted its endpoint compensation, incorrectly setting $x_0=\omega_0$. An independent numerical construction of the Hermite residual contradicted the predicted sine cost. In fact $x_0=p_0$ while $\omega_0=p_1$, so telescoping contributes $(\psi(p_0)-\psi(p_1))/2$. The corrected sine coefficient is $\sin a+\sum_{j\ge1}(-1)^{j+1}(\sin d_j-\sin a)$, not the sum alone. At q=4 the omitted amount is $\sin(\pi/5)$. V70 compares direct residual sums to the corrected series; the `endpoint_compensation` fault deliberately removes the term and must fail. The erroneous draft was never issued as v1.7. This cross-route correction is not an independent peer review.

A second implementation-only issue arose when a rational chosen exactly at a radius boundary was converted again to the EI dyadic lattice: an outward endpoint exceeded $1/2$ by a rounding unit. The certificate now compares the original exact rational product to $1/2$, retaining the outward upper bound for its constant. This changes no theoretical radius or tolerance.

**Source and mission boundary.** KERNEL 2.3, MANUSCRIPT/VERIFY 2.3 and Mission 1.7 were loaded in this turn, with research/breakthrough steps applied sequentially. Their ACTIVE major and EVIDENCE-LOOP-1 contract resolve the older 2.1 label in the project header. The supplied founding-ideas note and 11D seed were inspected for role; they remain NON-SSOT hypotheses and are not proof inputs. The before/after concerns a mathematical stability obligation. It does not derive a carrier, preparation, clock or instrument from an action. No new CORE result, physical no-go, global SSOT promotion or future paper identifier is declared.
## Appendix R5. Integration of the v1.7 audit, meta-audit and v1.8 research

### R5.1 Source authority and audit findings

The working sources are the uploaded complete v1.7 manuscript and bundle, the v1.7 audit report and bundle, and `M72_research_process_diagnosis_v1_7.md`. The applicable rules are the ACTIVE, compatible ZSPIN-RULES-2 package at minor 2.3, with Mission v1.7. The later compatible rule bodies take precedence over a stale package-minor reference in an older index. No rule file was modified. This is an integration into M72, not a new paper-code reservation.

| Supplied finding | Completed change | Evidence and remaining boundary |
|---|---|---|
| F17-01: additive stability base point omitted in summaries | The abstract and §14 explicitly identify $F_0=\cos(2\pi x)+\varepsilon^+(q)\cos(4\pi x)$. | T28–Cor30 are preserved in their stated local domains; no claim of arbitrary stability around bare cosine. |
| F17-02: targeted self-test could be read as all-row testing | Front matter, Appendix V and current README separate the author's 45 targeted faults, the auditor's eight all-row faults, and the six new v1.8 all-row faults. | Inherited results are labelled inherited. The new all-row protocol compares every unaffected row's evidence, not just its verdict. |
| F17-03: a vertical-tab escape corrupted `\varepsilon` | The single control character is replaced by the literal LaTeX command. | Final manuscript scan permits only tab/newline/carriage return below U+0020. Source bytes remain unchanged in provenance. |
| F17-04: V70 scope overstates endpoint enumeration | The current ledger states: depth-three prefixes ending at p0, with the reflected candidate evaluated separately. | The supplied auditor's deeper two-endpoint attack remains separate inherited evidence. The preserved legacy script is not silently relabelled as a broader enumeration. |
| F17-05: unconfirmed GSZ lemma/corollary numbering | §12.6 now cites **arXiv:2501.10949v2, Lemma 2.6**, whose statement and proof were directly read in this session. The unconfirmed “Corollary 2.7” locator is removed. | In v2, Lemma 2.6 states openness of the periodic-Aubry condition in $C^1\times\mathcal E^1$; Lemma 2.7 is a different family-openness statement. No claim that v3 was retrieved or that v2/v3 numbering is identical. |

The supplied v1.7 audit reports AUDIT-PASS-MINOR, highest severity S1, with the central local results surviving. That result is preserved for its exact target. Its author-lineage independence statement applies to the v1.7 additions; it does not become an independent audit of the v1.8 theorem merely because both files are now bundled.

### R5.2 What the meta-audit changed

The meta-audit diagnosed a repeated displacement of the external mathematical question by smaller local repair targets. It identified T13/T16 as the strongest earlier external contribution and warned that further radius improvements would not establish a major advance by themselves. The response here is operational and mathematical:

| Diagnosed failure | Change in this revision |
|---|---|
| An external question disappears behind audit maintenance | The introduction and abstract lead with the geometric/shifted large-deviation question, and §12.7 holds the source object fixed during comparison. |
| Another local radius is treated as the next breakthrough | T28–Cor30 remain intact; no new radius optimization is the central research target. T31 changes the frequency class and evaluates the full rate reduction. |
| Correctness PASS is mistaken for significance | §13.1 separates the finite checks from the changed capability: full shifted laws, a precise singularity and a newly accessible tail. |
| More audits repeat the same conclusion | This revision supplies a new theorem with a finite comparison, tests its actual failure modes, and stops after the evidence needed for that scope. It does not require another identical audit before recording the result. |
| Physical and mathematical value drift together | T31–P34 support an internal mathematical grade-4 finding; actual spin alignment and action-derived instrument selection remain OPEN. |

### R5.3 Three substantive research cycles and rejected shortcuts

**Cycle 1 — recover the external object.** Re-read T13/T16, the stated negative-endpoint question and the supplied process diagnosis. Re-check the nearest geometric and fixed-observable LDP sources. This confirms the earlier endpoint result as useful but does not count it again as new v1.8 work. A direct attempt at the original global negative comparison with the independent rate was considered; no proof was obtained and no closure is recorded.

**Cycle 2 — compute the deterministic shifted law.** Fix a single random phase and the common integer shift before constructing the proof. The initial representation is a family of frozen-phase pressures. A stronger finite form then emerges: Fourier positivity bounds every frozen integral by the positive-tilt geometric integral, while one cylinder near the half-turn gives the matching exponential lower bound. Keeping the cylinder probability and both phase errors yields (9.40). This removes any need to assume uniform spectral gaps across the phase family. The bound is uniform in the integer multiplier and yields Cor32 without another numerical ansatz.

**Cycle 3 — attack the conclusion and develop its consequences.** Compare the exact same $2^k+1$ sequence with the 2025 cumulant paper. Identify the reducibility restriction in its Theorem C. Import, rather than rediscover, the geometric first-resonance coefficient. Derive the nonanalyticity and the small-deviation rate expansion, and prove the impossible/possible tail distinction using the retained tent. Test negative shifts, negative multipliers, both parities, the excluded $r=0$, frozen-phase dependence, finite distortion and exact cumulants. The initial quadrature-resolution failure and its numerical repair are recorded in Appendix V. All six substantive wrong predictions fail their comparators under the all-row protocol. The final source collision also located the explicit shifted-example proposal in the original LDP paper's §2.4.1 and confirmed its retention on published p.519; this strengthens the external before/after comparison without changing the proved theorem.

**Approaches not promoted.** Finite scans do not establish the limit. An asymptotic ratio does not identify a phase process. Analyticity of every finite MGF does not imply analyticity of its limiting normalized logarithm. A rate value at an endpoint is not an atom at that endpoint. The general recurrence LDP and the original negative-rate comparison are not solved by restricting to affine-geometric frequencies. No future route or paper code is reserved.

### R5.4 Release and reversal contract

The final new claims are T31, Cor32, Cor33 and P34 under their explicit integer, common-offset and uniform-phase assumptions. A valid counterexample to (9.44) or its phase majorant, an omitted non-negligible prefix cost, failure of differentiability at zero, or a primary theorem already giving the same rate reduction would reopen the applicable correctness or novelty judgment. Noninteger multipliers, arbitrary termwise perturbations and actual spin eigenvalues are outside these claims, not counterexamples within them.

The artifact manifest records exact input hashes, output hashes, preservation checks and completed executions. The full historical file through H-0387 is copied without changing its prefix and extended by one H-0388 event row; the row is also supplied separately. No remote project index or history was changed. No publication or CORE promotion is included.

## Appendix H. Preservation and correction map

**Current v1.8 preservation contract.** Sections 2–9.9, Sections 10–11, and Appendices S/N are retained byte-for-byte as complete sections. New results are inserted as §§9.10–9.13. Front matter, introduction summaries, current comparison/assessment, discussion, verification disclosures and availability are updated. The actual control-character and GSZ-locator repairs are recorded in R5. The manifest measures the retained-section hashes. Earlier maps below remain historical records of their own revisions.

### H1. Where every part of the seed and of the note is integrated

| source | location in this paper | treatment |
|---|---|---|
| seed §§1–3 (conclusion, inputs, round history) | §§1, 11, 13; Appendix H | current claims and verdict restated; the round-by-round history is not reproduced, the decisions it records are |
| seed §4 (corpus, upstream obligations) | §11.3, Appendix S11 | latest status and role separation; no debt closed |
| seed §5 | Appendix S5 | optimal sets, non-uniqueness, variational computations preserved |
| seed §§6.1–6.13 | Appendix S6.1–S6.13 | preparation, flat/spin, cooling kernels, charged source and counterexamples preserved |
| seed §6.14 | §§2–5, Appendix S6.14 | exact T1 preserved; the earlier insufficient general asymptotics, time and parity interpretations replaced by Theorems 1–2 |
| seed §6.15 | §5.3, Appendix S6.15 | scalar derivative and finite tables preserved; the global optimum retracted |
| seed §7 | Appendix S7, §7 | code/clock/instrument resource ledger tied to explicit preparation |
| seed §8 | Appendix S8, §11 | current, Gauss law, finite time, no-photon, error and actual-value ranges preserved |
| seed §9 | Appendix S9, §§7–8 | pump, optical output and neutral-outcome composition kept with the spatial-record composition |
| seed §10 | §12, Appendix L | closest sources re-compared; E35 author correction; unverified E33 details not inherited |
| seed §11 | Appendix S11, §11.3 | T-MD counterexample, T★ target and debts preserved |
| seed §12, JSON, self-test, agent audit | Appendix V | live regression separated from the independence of past audits |
| seed §13, Appendices A–C | §§13–14, Appendix H | present qualification updated by the new proofs; past verdicts remain in the project history |
| seed Sections 2–8 (six theorems) | §§2–8 | proofs carried in full, equation numbering made continuous |
| seed Section 9 (open exponent) | §9, §10 | the open problem replaced by Theorems 7–9, the alignment-capacity formulation, Theorem 10–11, Proposition 12 and Conjecture 9.2 with its falsifier |
| note §§1–2 | §§1, 6; Appendix N2 | question, observational equivalence, content/order distinction |
| note §§3–6 | §§6–8, Appendix N3–N6 | exact gate, variable angle, storage, independent accumulation and copy counterexample preserved and extended |
| note §§7–8 | Appendix N7–N8 | signature, second-order response, remainder, rank and recovery limits |
| note §§9–10 | Appendix N9–N10, S8 | current triple product, rank-1, spurious projection, weak-coupling leakage, spatial dilution limit |
| note §§11–14 and sources | Appendix N11, N13, §12.3, Appendices L and V | thought experiments, physical obligations, source lineage, the 19-row regression |
| founding note, 11D seed, Book, Mission, rule set | §§11.1–11.2, §1 | research questions and hypotheses integrated as operational objects; the originals are not reproduced |
| prior sufficiency review | §§3–8, Appendix V | the empty objects demanded by that review replaced by actual theorems, channels and full-space motion |
| ZS-M72 v1.0 (this paper's previous version) | every section, marked in place; Appendix R | all eleven audit findings repaired, retracted or restricted; no v1.0 text is silently deleted, and the two refuted claims are shown with their refutations |
| the v1.0 audit report and its eleven check rows | §§9.5–9.8, 10.1, 10.3, 12.2, 13.1; Appendices R and V | findings answered one by one; its three new theorems integrated with proofs rewritten and, for the even-$q$ cap, extended from $q\ge6$ to every even $q\ge2$ |
| ZS-M72 v1.1 and the audit of it | §§9.1, 10.1, 10.3, 12.2, 13.1; Appendices R8–R9 and V | all six findings repaired, replaced or corrected; the two refuted items (the printed generality of Proposition 9.1, the superexponential Weyl claim) are shown with their refutations, and Proposition 17 replaces the second |

### H2. Corrections carried and corrections made

Carried from the seed:

1. The unrestricted actual-lifetime global optimum of B19 is retracted; the macroscopic band and the fixed window have different limits (Theorem 3, Appendix S6.15).
2. The general sum and uniform remainder for two boundaries of comparable size are supplied by a new proof (Theorem 1).
3. The exact sine cumulative, the uniformity of gaps and weights and the time-average upper bound together complete the first-loss argument (Theorem 2).
4. The positive-sign average is separated from the total-variation average, the all-time floor and physical storage (Sections 5–6).
5. The polarisation of the note is obtained from an actual preparation map, with the calibration-phase cost and null tests (Theorem 5, row W13).
6. Actual motion is realised on the full position Hilbert space with the capture obligation and timing error made explicit (Theorem 4).
7. Correlated flips are not confused with independent environmental flips; the storage rate and the full output error are computed (Theorem 6).
8. The authors of arXiv:quant-ph/0607107 (E35) are Bartlett, Rudolph, Sanders and Turner; the battery sine-state proof is in that paper's Appendix E.

Made in this paper:

9. The seed's transition remainder $O(1/h)$ for the two-boundary capacity at $h\sim\sqrt B$ is replaced by the explicit relative error $-(B/4h^2)(1-2x)/(1+2x)+O(B^2/h^4+1/h)$ (Theorem 10, row V21); the seed's statement was not wrong for fixed $\epsilon$ but was silent at the diffusive scale.
10. The seed's exponent interval $[I(x_{\ell/2}),I(x_\ell)]$ is shown to be sharp at both ends within the class of admissible spectra (Theorem 7), so "narrow the interval by a better general inequality" is closed as a research direction; the exponent is a spectral alignment quantity, $\kappa$.
11. The seed's assumption $a<b$ (a strictly interior band) is removed for the exponent interval (Theorem 11).
12. The parent-independence of the rate function is stated as Proposition 12 with the Weyl ground energy $-(1-1/B)$, replacing the seed's remark that the spin and Weyl parents "share the semicircle form" without a rate statement.
13. Section 9's finite-size table is generated from the scan output rather than transcribed; the earlier hand-entered value at one size is superseded.

Made in v1.1, in answer to the audit of v1.0 (the finding IDs are those of Appendix R):

14. **F08, REFUTED.** The Weyl-parent ground energy is not exactly $-(1-1/B)$ and the gap is not exactly $2/B$; the exact rational characteristic polynomial is non-zero at that value for every $B$ tested, and at $B=16$ the true ground energy is lower by $2.8\times10^{-7}$. The claim is withdrawn and replaced by a semiclassical statement whose correction $\delta_B$ is exponentially, **not** superexponentially, small — Proposition 17 and Theorem 18 bound and then locate it, $\delta_B=2/(\sqrt\pi B^{3/2}2^B)[1+O(B^{-1})]$ (Section 10.3, rows C29, V41, C42).
15. **F05, RETRACTED.** The identification of the spin band's phase dynamics with the reduced torus map $x\mapsto\{qx\}$ for non-integer ratios is withdrawn; it loses the winding number, and $\{q^2x\}$ and $\{q\{qx\}\}$ differ by $\tfrac12$ at $q=\tfrac52$, $x=\tfrac34$ (row C30). Conjecture 9.2 is decomposed into four statements, of which $\kappa^->0$ is now proved.
16. **F06.** The step $\sum_ss^2\rho^s\le2\rho^2/(1-\rho)^3$ in the proof of Theorem 10 is false — that is the value of $\sum_ss(s-1)\rho^s$ — and the spectral step's $O(B^{-3/4})$ was arithmetically wrong. Both are repaired with the same final statement, the first by keeping the $s(s-1)$ the expansion produces, the second with the correct $O(B^{-5/4})$.
17. **F07.** The consequences of Theorem 10 are restricted: the Gaussian gap form holds only for $h=o(B^{3/4})$ (with an analytic counterexample at $h=B^{4/5}$), the extension of the adjacent-gap lemma into the diffusive range is withdrawn pending a difference remainder, and the fixed-$K$ sentence is demoted to a statement about frequencies.
18. **F03.** The proof of Theorem 8 is rewritten around the $\ell^1$ Fourier mass, because $K_m(0)^r$ bounds nothing ($K_1(0)=0$); the printed constant $c_m=8(m+1)(2m+1)/m$ is recovered unchanged, and the unproved remark "a sharper count gives $6$ for $m=1$" is deleted.
19. **F01, F02.** Proposition 9.1's statement is completed to the two-sided (9.1a) with strict thresholds and the variable-$\kappa$ crossing (9.1b); Theorem 7's lower-end construction is closed by a diagonalisation that exhibits one admissible family.
20. **F04.** The even-$q$ grid observation is retyped as a diagnostic and superseded by a proof for every even $q\ge2$ (Theorem 13).
21. **F09, F10.** The Lipschitz brackets are no longer called interval certificates, and the finite $\theta$ column is no longer read as evidence about the limit; the falsifier of Conjecture 9.2 now requires a controlled subsequence with a residual bound.
22. **F11.** The verifier's scope strings no longer point at the seed's old theorem numbers, and the row ledger, the text and the appended history row agree at v1.1.

Made in v1.2, in answer to the audit of v1.1 (the finding IDs are those of Appendix R8):

23. **F01, REFUTED as printed.** Proposition 9.1 was false whenever the limiting rate measure has an atom at the threshold. The family (9.1c), with an atom of mass $0.07$ at $z=2$, makes the v1.1 statement predict $\limsup_BB^{-1}\log T_\ell\le2$ while the true loss never reaches $\ell=0.4$ before $e^{3B}$; the exact rational bound at $B=64$ is $0.39684375$ (row C38). The statement is replaced by the form with $H_-(z)$ and the atomic term $2a_z$, with the v1.1 display kept as the no-atom corollary. Theorem 2(c) and Theorem 15 are unaffected.
24. **F02, REFUTED.** The claim that the Weyl ground-energy correction is superexponentially small is false. Proposition 17 gives $\delta_B\ge1/(BZ_B)\ge1/(B2^{2B-1})$ for every $B\ge1$ by an exact trial vector, so $(-\log\delta_B)/B\le2\log2$; the computed value falls from $0.943$ at $B=16$ to $0.725$ at $B=256$ (row V41). The inference from the size of the characteristic polynomial to the size of one eigenvalue deviation is withdrawn.
25. **F03.** The omitted tail in the proof of Theorem 10 was written $O(\rho_0^{\sqrt B})$ with an implied absolute constant; at $h=3\sqrt B$ the exact tail divided by $\sqrt B\rho_0^{\sqrt B}$ tends to $85/432$. The tail is now carried in closed form and estimated after normalisation, where it and the two remaining tails are all $O(K^{-4})=O(B^2/h^4)$ (row C39). The statement and the leading coefficient of Theorem 10 are unchanged.
26. **F04.** "Exactly one eigenvalue lies below $z$" is not implied by a positive characteristic polynomial; the correct reading is an odd number, hence at least one. A seven-vertex path with three eigenvalues below a point of positive determinant is row C40.
27. **F05.** The achieved research grade is set to UNASSESSED and the document role to research note while novelty is HOLD; candidate grade 4 is kept and separated from the achieved grade.
28. **F06.** Row C35 is retyped V35, its floating tolerance being incompatible with the C class; the exact endpoint identity stays in the symbolic row C26. The Theorem 14 summaries now carry both conditions of (9.20), and the reversal criterion of §13.3 concerning the Weyl eigenvalue is restated for the ground eigenvalue.

### H3. History

`history_append_H-0388.md` contains one new event after the supplied H-0387. `history_h0001-h0388.md` preserves the complete supplied history as an unchanged byte prefix and appends that row. It records the new proof, actual run profiles, grade scope and unresolved physical bridge. Earlier grades and audit verdicts are historical facts, not overwritten statuses. No remote project history, global index, public submission or CORE state was changed.

## Availability

`ZS-M72_v1_8_bundle.zip` contains this complete integrated manuscript, the standalone new verifier and its two completed ledgers, the inherited central rerun, a Korean research report, README, release manifest, one H-0388 row and the extended history. `inherited_v1_7/` preserves the original verifier and original run evidence. `provenance/` contains the supplied v1.7 paper, audit, meta-audit and the two input bundles unchanged. `research_trace/` contains the fixed research contract, the initial quadrature-resolution failure and the integration/preservation record. The initial failure is not counted as a passing run. Input and output hashes are in `zs_m72_release_v1_8.json`.

The new verifier reproduces its stated finite checks without network access; it does not reproduce every inherited exploratory table or replace a proof assistant. No unsupplied historical artifact is asserted to be included.

## AI-use record

The inherited v1.0–v1.6 author-side manuscripts were prepared using Claude (Anthropic), according to the supplied records; the user-reported audits of v1.0–v1.6 used ChatGPT/OpenAI. This is provenance reported by the sources, not a claim that this session independently witnessed all prior executions. T24/P24.1 originated in the v1.4 OpenAI audit; the author-side v1.5 supplied the q=2,4 completion and T25's statement/reduction; the v1.5 OpenAI audit supplied the replacement large-q proof of T25, T26 and P27 with its example. v1.6 integrated those contributions. The supplied v1.6 audit is scope-limited and did not complete the entire original full-run and mutation suite.

OpenAI prepared v1.7, including the audit corrections, T28/Cor29/Cor30, new verification rows, directed-endpoint serialization, integration and current assessment. Standard Hermite interpolation, the inherited geometric gap and Leplaideur–Mengue's pressure representation are explicit inputs. An independent numerical implementation within this same authoring session exposed and corrected the missing endpoint compensation in the first draft of T28. Deterministic cross-routes and deliberate faulty predictions were used; this is not an independent external audit of the new proofs, and shared definitions and mathematical premises remain. No autonomous sub-agents or claimed human reviews were used for this revision. Qualified-human anchor: NONE is disclosed without making it a prerequisite of paper qualification or research grade.

OpenAI prepared v1.8: the fresh T31–P34 mathematical development, primary-source collision, cross-route checks, full integration, and current internal grade assessment. No autonomous sub-agents were used. The supplied v1.7 audit is attributed to its stated author lineage; it was not performed by this session and does not certify the new results. The active authoring role progressed from RESEARCH, with a BREAKTHROUGH target, to MANUSCRIPT with VERIFY as helper; multiple simultaneous dominant roles are not claimed. The new work has no independent human or external cross-family audit. Qualified-human anchor: NONE.

## References

Sources are cited at the point of use with their locators; the tables of Section 12 and Appendix L (L1–L3, L-S10.1–L-S10.1d) list every external source consulted for this paper, the range in which each was read (full text, abstract, theorem statement or bibliographic pointer), and the status assigned to it. Mathematical inputs used in the new proofs are: L. Fejér's extremal theorem for nonnegative cosine polynomials (via D. K. Dimitrov's survey, Theorem 6); the Riesz–Fejér representation of nonnegative trigonometric polynomials; Sidon's theorem on lacunary sequences (via J.-P. Kahane's survey, §II.1); Bousch's sub-action theorem and the Jenkinson survey of ergodic optimisation (Theorem 6.2, and §4 Theorem 4.1 for the pressure variational principle, the upper semicontinuity of the entropy and the zero-temperature limit used in Theorem 16); the large-deviation formulation and normalisation of lacunary sums of Aistleitner, Gantert, Kabluchko, Prochno and Ramanan (arXiv:2012.05281, §2.2 after Lemma 2.3, §3.3, Theorem D and Remark 2.5), whose stated open question Theorem 16 answers; the Ehrenfest-chain spectral results and Bovier's capacity method inherited from Sections 2–3; and the exact combinatorial identities of the seed. No source is cited for the first-loss formulation itself; the search that failed to find one is recorded in Section 12.2, and NOT_FOUND is not read as ABSENT.


The v1.8 additions use the versioned primary sources and exact locations in §12.7 and the coefficient citation at (9.47). The GSZ correction uses v2 Lemma 2.6, not an unverified v3 locator. Classical Fourier positivity and Gärtner–Ellis are credited proof inputs, not novelty claims.
