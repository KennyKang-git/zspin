# **ZS-U12**

# **The z\*-Locked Low-ℓ CMB Transfer:**

**A Wilson-Loop Holonomy Template with a Phase-D-Derived z\*-Locked Suppression**

**Author: Kenny Kang**

**Affiliation: Z-Spin Cosmology Collaboration (independent)**

**Date: June 2026**

**Theme / Paper Code: Early Universe \[ZS-U\] — ZS-U12 — Paper 12 of the U-series**

**Version: v2.3 (June 2026\) — consolidates v1.0–v2.2, ZS-U12.1; integrates the background**

**Verification: 52/52 PASS (structural ledger)  |  Executable suite zs\_u12\_verify.py: 46/46 PASS  |  Zero Free Parameters**

*v2.3 update: the homogeneous Einstein-frame background is now numerically integrated (§9.4), replacing the de Sitter idealization with an integrated H(N) — confirming H\_b \= A/√6 M\_P at the core and revealing a mild H-running of n\_supp. IMPORTANT (honest scope): this does NOT lift n\_supp to unconditional DERIVED. Because n\_supp \= √(12/λ\_vac)·(−ln|λ|²), it is structurally tied to λ\_vac \= 2A² (ZS-U5, DERIVED-CONDITIONAL), and the uphill topological transition into the core (ZS-A6 NC-A6.3) remains genuinely OPEN. Unconditional DERIVED is therefore unreachable from this paper; n\_supp stays DERIVED-CONDITIONAL. No content deleted.*

# **§0. Abstract**

ZS-A6 §7.2 registers, as an OPEN item, the observable C\_ℓ ∝ |z\*|^{2ℓ} with the quadrupole instance C₂/C₂^ΛCDM ∝ |z\*|⁴ \= 0.10376 (“≈10% suppression”), flagged as “requiring derivation from bounce dynamics, not mere identification.” This paper attacks that item directly and consolidates the full resolution. **(1) Multiplier (§3, Theorem U12.1, DERIVED).** The headline factor |z\*|² \= η\_topo \= 0.32212 is the *location* of the i-tetration fixed point, not a *multiplier*. By Koenigs (1884) the dynamically forced per-transit factor is **|λ| \= |f′(z\*)| \= (π/2)|z\*| \= 0.89151**, power survival **|λ|² \= (π²/4)η\_topo \= 0.79480**. The |z\*|⁴ number is RETRACTED. **(2) Transfer object (§4, Theorem U12.2, DERIVED).** The bounce mode-transfer is the corpus Wilson-loop BV-BFV partition function Z(W) \= λ (ZS-F0/F11 Thm 8.9), n-cycle survival |λ|^{2n} (gate WL-2). **(3) Continuum (§5, Szekeres 1958).** The hyperbolic fixed point embeds in a one-parameter analytic flow, so the discrete count becomes a continuous transit τ and P\_Z(k)/P(k) \= |λ|^{2τ(k)}.

**(4) Phase-D form (§6, Theorem U12.3, DERIVED).** A total-wipeout paradox — all CMB modes are superhorizon throughout the ≈78.45-cycle bounce, naively giving uniform |λ|^{2N\_{2π}} ≈ 10⁻⁸ — is resolved by the standard superhorizon-conservation theorem: ζ is conserved outside the horizon, so the Wilson loop imprints only at horizon crossing. Hence τ(k) \= ν\_c ln(k\_b/k) and the primordial suppression is the power-law cutoff **P\_Z(k)/P(k) \= (k/k\_b)^{n\_supp}, k \< k\_b. (5) Canonical exponent (§7, Theorem U12.4, DERIVED-CONDITIONAL).** With H\_b \= (A/√6)M\_P from the topological-core energy V(0) \= (λ\_vac/4)M\_P⁴, λ\_vac \= 2A², the cycles-per-e-fold is ν\_c \= √6/A ≈ 30.58 and **n\_supp \= (√6/A)·(−ln|λ|²) ≈ 7.02 (zero free parameters; bracket \[0.23, 7.02, 18.0\] over natural H\_b). (6) Section-8 closure (§8, Theorem U12.5, DERIVED-CONDITIONAL).** The per-cycle Floquet monodromy of the winding-transfer mode equation is determined, not open: modulus |λ| \= 0.8915 superhorizon (the leaky Z-block of ZS-F0 §8.8, det \= |λ|² \< 1\) and 1 deep-subhorizon (symplectic/adiabatic, det \= 1), the difference being the leakage 1−|λ|² \= 0.2052 to the Z₂-odd channel — which IS the suppression. Only the exact k-window profile near k\_b remains conditional on the bounce H(t). (7) Window closure (§9, Thms U12.6–U12.7, DERIVED). The bounce core is a hilltop near-de Sitter phase at H\_b \= (A/√6)M\_P (ε \= 0 is a potential maximum, V″(0) \< 0 PROVEN; dynamics VERIFIED by ZS-U8 §6.3 μ \= 0.1177 M\_P and ZS-U1 §3 N\_e \= 2.04), so W(k) is the de Sitter horizon-crossing window over N\_core \= 2π/√6 ≈ 2.565 e-folds and P\_Z(k)/P(k) \= W(k)·(k/k\_b)^{n\_supp}. The window FORM is DERIVED; n\_supp ≈ 7.02 stays DERIVED-CONDITIONAL (inheriting λ\_vac \= 2A² \+ the de Sitter approximation), the unconditional step requiring the full NR bounce solution (ZS-A6 NC-A6.3, OPEN). The mimicry-resistant z\*-signal is the suppression-per-e-fold −ln|λ|² \= 0.2297; the decisive discriminant is the SHARPNESS of the low-ℓ cutoff. (8) Numerical background and honest scope (§9.4, v2.3). The homogeneous Einstein-frame rolldown is integrated (λ \= λ\_vac \= 2A²): it confirms H\_b \= A/√6 M\_P at the core (= √(V\_E(0)/3), exact) and shows H running down by ≈1.8× over the core, so n\_supp runs from 7.02 at k\_b upward for k \< k\_b. This replaces the de Sitter idealization with an integrated background, but does NOT reach unconditional DERIVED: n\_supp \= √(12/λ\_vac)·(−ln|λ|²) is structurally tied to λ\_vac \= 2A² (ZS-U5, DERIVED-CONDITIONAL), and the uphill topological transition into the core (ZS-A6 NC-A6.3) remains OPEN — a structural boundary, not a computational gap. Zero free parameters are introduced.

# **Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem with complete proof; machine- or 50-digit-verified. |
| **DERIVED** | Quantitative consequence of PROVEN items \+ Z-Spin axioms; zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived conditional on a stated assumption (here: the canonical bounce ansatz and/or λ\_vac \= 2A²). |
| **STANDARD** | Established result in GR / cosmological perturbation theory (textbook). |
| **VERIFIED / TESTABLE** | Numerically confirmed against data / quantitative prediction with a pre-registered falsification condition. |
| **HYPOTHESIS-weak** | Single structural line; anti-numerology and/or derivation pending. |
| **OBSERVATION** | Numerical proximity noted; numerology-risk until tested. |
| **OPEN** | Identified gap pending future work (here: well-posed and isolated). |
| **NON-CLAIM / RETRACTED** | What this paper does NOT establish / previously asserted, now demoted with reason. |

A verification PASS certifies *computational/structural correctness*, not physical truth; every physical claim is tagged independently of the 41/41 PASS ledger.

# **§1. Introduction**

## **1.1 A-dependent versus z\*-dependent observables**

Most quantitative handles in the corpus depend on A \= 35/437 (ZS-F2 \[3\]) — reproducible by an external critic tuning one constant. The i-tetration fixed point z\* \= 0.4383 \+ 0.3606 i (ZS-M1 \[2\]) is transcendental, appears in no standard theory, and is self-locked (conditions L1–L5), making a z\*-dependent observable the most mimicry-resistant signal the framework can offer. This paper asks whether the CMB low-ℓ deficit can be made into such a signal.

## **1.2 The OPEN item and what v2.0 consolidates**

ZS-A6 §7.2 tabulates C\_ℓ^bounce ∝ |z\*|^{2ℓ} and C₂/C₂^ΛCDM ∝ |z\*|⁴ \= 0.10376 with the explicit caveat “requires derivation from bounce dynamics (OPEN), not mere identification” \[6\]. v1.0 corrected the multiplier; v1.1 identified the transfer object and continuum; the ZS-U12.1 companion closed the Phase-D form. v2.0 merges all of these into one paper (no content deleted) and folds the planned ZS-U12.2 program into a single precisely-posed residual (§8). The reading error in prior literature — |z\*|⁴ ≈ 0.10 is a \~90% suppression, not 10% — is adopted; this paper supersedes the |z\*|⁴ identification entirely (§11.2).

# **§2. Locked Inputs**

No new parameters. All quantities inherited from upstream papers at the indicated status.

**Table 1\. Locked constants, derived invariants, and Phase-D inputs.**

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| **A** | 35/437 \= 0.0800915 | ZS-F2 \[3\] | LOCKED |
| **(Z, X, Y); Q** | (2, 3, 6); 11 | ZS-F5 \[4\] | PROVEN |
| **z\*** | 0.4382829 \+ 0.3605925 i | ZS-M1 \[2\] | PROVEN |
| **|z\*|² \= η\_topo** | 0.3221189 | ZS-M1 \[2\] | PROVEN |
| |z\*|⁴ | 0.1037606 | ZS-M1 \[2\] | PROVEN (arith.) |
| **λ \= (iπ/2) z\*** | −0.566417 \+ 0.688453 i | ZS-M1 \[2\] | PROVEN |
| **|λ| \= |f′(z\*)|** | 0.8915136 | ZS-M1 \[2\] | PROVEN |
| **|λ|² \= (π²/4)η\_topo** | 0.7947964 | ZS-M1; ZS-F0/F11 \[2\] | PROVEN |
| **−ln|λ|²** | 0.2296693 | this work (arith.) | PROVEN |
| V(0) at ε \= 0 | (λ/4)M\_P⁴ (topological core) | ZS-F1 §4.1 \[5\] | PROVEN |
| **λ\_vac** | 2A² \= 0.012829 | ZS-U5 §8 / ZS-F1 §4.4 \[7,5\] | DERIVED-CONDITIONAL |
| N\_{2π} (bounce cycles) | 2π/A ≈ 78.45 | ZS-U5 / ZS-A6 DL-1 \[7,6\] | DERIVED-under-P6 |
| T\_micro / S\_tunnel | 2π/A; 5π/A ≈ 196.13 | ZS-U5 / ZS-A6 \[7,6\] | DERIVED-P6 / HYPOTHESIS |
| ζ superhorizon conservation | dζ/dt → 0 (k ≪ aH) | Weinberg 2008 \[22\] | STANDARD |
| L\_XY | 0 (no direct X–Y coupling) | ZS-F5 \[4\] | PROVEN |

Two arithmetic identities recur (PROVEN to machine precision): |λ| \= (π/2)|z\*| and |λ|² \= (π²/4)|z\*|². The latter is the Leaky Wilson Loop identity of ZS-M1, whose modulus |λ|² \= 0.7948 is the per-cycle survival of the Wilson-loop sum rule (ZS-F0/F11 Thm 12.3): 0.7948 \+ 0.2050 \+ 0.0001 ≈ 1\.

# **§3. The Multiplier-Selection Theorem (Koenigs)**

A power-spectrum ratio is a ratio of squared amplitudes; if a transfer multiplies a mode amplitude by g per Z-transit, the ℓ-fold power ratio is |g|^{2ℓ}. The corpus offers two conflated candidates: |z\*| \= 0.5676 (the fixed-point *location*) and |f′(z\*)| \= |λ| \= 0.8915 (the *rate*). For T(z) \= i^z \= exp((iπ/2)z), T′(z\*) \= (iπ/2)i^{z\*} \= (iπ/2)z\* \= λ, so:

*f′(z\*) \= λ,   |f′(z\*)| \= (π/2)|z\*| \= 0.89151 \= |λ| \< 1\.*

**Theorem U12.1 (DERIVED).** By Koenigs’ linearization theorem \[9\], an analytic map with attracting fixed point and multiplier λ (0 \< |λ| \< 1\) is conjugate to w ↦ λw; the m-th iterate is conjugate to w ↦ λ^m w, so amplitude deviations evolve as |λ|^m. The only dynamically admissible per-transit power factor is **|λ|² \= 0.79480**, and a transfer-induced ratio must be |λ|^{2ℓ}, not |z\*|^{2ℓ}.  Koenigs’ result is PROVEN external mathematics; its application is exact because ZS-M1 PROVES 0 \< |λ| \= 0.892 \< 1\. The |z\*|⁴ ≈ 10% identification is thereby RETRACTED (§11.2).

# **§4. The Bounce-Transfer Object (Wilson Loop)**

Naive treatments solve a smooth Mukhanov–Sasaki equation across a scale-factor minimum \[12–17\]. The Z-Telomere bounce is *topological* — uphill in V(ε), with Coleman–De Luccia, Hawking–Moss, and thin-wall all PROVEN-inapplicable (ZS-A6 §5.1 \[6\]) — so there is no smooth z\_MS background. The correct transfer object is supplied in closed form by the corpus.

**Theorem U12.2 (DERIVED).** The Z-Spin Wilson loop W (Σ\_X → Σ\_{XZ} → Σ\_Y → Σ\_{ZY} → Σ\_X) is a closed BV-BFV cobordism with partition function Z(W) \= f′(z\*) \= λ (ZS-F0/F11 Thm 8.9, PROVEN), single-cycle power survival |Z(W)|² \= |λ|² \= 0.79480, and n-cycle survival |λ|^{2n} (gate WL-2; protocol P\_b^{(n)} \= 0.7948^n, ZS-F16 §4.4, PROVEN). The bounce mode-transfer operator on a superhorizon U(1)-winding mode is therefore the iterated Wilson loop, with power transfer |λ|^{2n} after n Z-Telomere cycles.  The mis-posed MS matrix is replaced by a PROVEN object whose eigen-suppression is exactly the |λ|² of §3.

# **§5. Continuous Iteration (Szekeres)**

The fixed point is hyperbolic (0 \< |λ| \= 0.892 ≠ 1). By Szekeres’ regular-iteration theorem \[18\] (building on Koenigs \[9\] and the Abel function \[19\]), an analytic germ with a hyperbolic fixed point embeds uniquely in a one-parameter analytic flow f^{\[τ\]} with f^{\[s\]} ∘ f^{\[t\]} \= f^{\[s+t\]}, f^{\[1\]} \= T; in the Koenigs coordinate Ψ(f^{\[τ\]}(z)) \= λ^{τ}Ψ(z). Hence for continuous transit τ:

**P\_Z/P \= |λ|^{2τ} \= exp(2τ·ln|λ|),   ln|λ|² \= −0.22967 (LOCKED).**

The bounce holonomy δφ \= A accumulates continuously, so τ is naturally real; the integer-ℓ ladder of v1.0 (Table 3\) is the projection of this flow onto the multipole grid.

# **§6. Superhorizon Conservation Fixes the Form of τ(k)**

## **6.1 The total-wipeout paradox**

The bounce completes one 2π winding in N\_{2π} \= 2π/A ≈ 78.45 Wilson cycles (one per Planck time), so T\_bounce ≈ 78.45 t\_P. A CMB-scale mode was superhorizon for the entire Planck-proximate bounce. If the per-cycle survival applied to such frozen modes, every observable mode would suffer the uniform, k-independent annihilation |λ|^{2N\_{2π}} \= 0.7948^{78.45} ≈ 1×10⁻⁸ — erasing all structure, with no low-ℓ feature. The naive picture is unphysical.

## **6.2 Resolution: imprint only at horizon crossing**

**Theorem U12.3 (DERIVED).** By the superhorizon-conservation theorem \[22\], the adiabatic curvature perturbation ζ\_k is conserved while k ≪ aH; a conserved mode carries no dynamical phase for the Wilson loop to act on. The holonomy transfer is non-trivial only within the mode’s horizon-crossing window. Hence the accumulated transfer is set by the cycles between bounce-era horizon crossing and the end of the bounce:

**τ(k) \= ν\_c·N(k),   N(k) \= ln(k\_b/k)   (k \< k\_b),**

with N(k) \= ln(k\_b/k) the standard e-folds-since-crossing relation \[22\] and ν\_c the Wilson cycles per e-fold (§7). Substituting into P\_Z/P \= |λ|^{2τ} gives

**P\_Z(k)/P(k) \= (k/k\_b)^{n\_supp},   n\_supp \= ν\_c·(−ln|λ|²)   (k \< k\_b),  \= 1 (k ≥ k\_b).** 

Frozen modes are untouched; only the crossing window imprints. This **closes the functional form of τ(k)** (logarithmic in k ⇒ power law in k) from two STANDARD inputs plus the PROVEN Wilson-loop transfer. The ZS-A6 §7.2 form-gap is closed.

# **§7. The Bounce Hubble Scale and the Canonical Exponent**

At the topological core ε \= 0 the energy is V(0) \= (λ/4)M\_P⁴ (ZS-F1 §4.1, PROVEN). The relevant coupling at the ε ∼ O(1) transition is the IR fixed point λ\_vac \= 2A² (ZS-U5, DERIVED-CONDITIONAL), so V(0) \= (A²/2)M\_P⁴. The Friedmann constraint 3H\_b²M\_P² \= V(0) gives H\_b \= (A/√6)M\_P ≈ 0.0327 M\_P, and with the Wilson-cycle rate locked at one per t\_P,

**ν\_c \= M\_P/H\_b \= √6/A ≈ 30.58 cycles/e-fold.**

**Theorem U12.4 (DERIVED-CONDITIONAL).** Under the canonical bounce ansatz — (i) imprint at horizon crossing (§6), (ii) Wilson-rate accumulation, (iii) H\_b \= (A/√6)M\_P — the suppression is the zero-free-parameter power law

**n\_supp \= (√6/A)·(−ln|λ|²) \= 30.58 × 0.22967 ≈ 7.02.**

**Table 2\. Suppression exponent n\_supp \= (M\_P/H\_b)·(−ln|λ|²) across natural bounce-Hubble choices.**

| Bounce Hubble H\_b | ν\_c \= M\_P/H\_b | n\_supp | Cutoff character |
| ----- | ----- | ----- | ----- |
| M\_P (Planck bounce) | 1 | 0.230 | gentle tilt |
| **(A/√6) M\_P  \[canonical, V(0)\]** | **30.58** | **7.02** | **sharp** |
| (A/2π) M\_P \= 1/T\_bounce | 78.45 | 18.0 | very sharp |

The canonical exponent makes the suppression a sharp cutoff: full power to heavy suppression within a factor ∼2 in k (Table 4), confining the observable feature to the quadrupole/octupole rather than a broad tilt — itself a falsifiable structural prediction (§12).

# **§8. The Phase-D Winding-Transfer Mode Equation (Theorem U12.5 Target)**

The canonical ansatz of §7 rests on three physical assumptions. v2.0 reduced all three to a single Floquet-monodromy computation — the program formerly planned as ZS-U12.2 — and v2.1 now carries out that computation, closing the monodromy value.

**Setup.** In the radial-frozen \+ winding sector, write the gauge-invariant scalar perturbation as v\_k \= z\_w ζ\_k, where z\_w is the winding-sector pump field of the Z-Telomere background (the holonomy flow φ(t) \= A·t/t\_P, δφ \= A per cycle, ZS-U5 Lemma 8.1). The perturbation obeys a Mukhanov–Sasaki-type equation whose effective mass is the winding-holonomy term rather than a smooth z\_MS″/z\_MS:

*v\_k″ \+ ( c\_s² k² − z\_w″/z\_w ) v\_k \= 0,   z\_w″/z\_w set by the B\_Z holonomy flow.*

The boundary holonomy operator B\_Z (ZS-A6 §3 \[6\]) acts on the winding sector once per Regge cycle with eigenvalue λ \= (iπ/2)z\* (ZS-F0/F11 Thm 8.9, PROVEN). The transfer across the crossing window is the ordered product of per-cycle holonomies, i.e. the Floquet monodromy M(k) of the equation over one cycle.

**Theorem U12.5 (DERIVED-CONDITIONAL).** The per-cycle Floquet monodromy of the winding-transfer equation is *determined*, not open. Two limits are computed exactly:

**(a) Superhorizon limit (k → 0).** The c\_s²k² term drops and the perturbation reduces to the homogeneous Z-channel deviation, whose per-cycle map is the Wilson-loop Z-block (Theorem U12.2 \+ ZS-F0/F11 §8.8, PROVEN): M\_f \= \[\[Re λ, −Im λ\],\[Im λ, Re λ\]\], eigenvalues λ, λ̄, so |M| \= |λ| \= 0.8915 and det M\_f \= |λ|² \= 0.7948 \< 1\. The map is *leaky* (non-symplectic): the missing 1−|λ|² \= 0.2052 is transferred to the Z₂-odd channel (Wilson sum rule, §2). This leakage IS the power suppression.

**(b) Deep-subhorizon limit (k → ∞).** Here the equation is an adiabatic oscillator v\_k″ \+ c\_s²k² v\_k ≈ 0; its monodromy is symplectic (Wronskian conserved, det \= 1), so |M| \= 1 and there is no net suppression — the standard adiabatic theorem. Subhorizon modes do not leak.

The crossover from |M| \= |λ| (superhorizon) to |M| \= 1 (subhorizon) occurs at horizon crossing k ≈ k\_b. Both limits are verified numerically (suite categories C, F: superhorizon |eig| \= 0.891514, det \= 0.794796; subhorizon |eig| \= 1.000, det \= 1.000). 

**Status of §8: OPEN → DERIVED-CONDITIONAL.** The monodromy VALUE is now derived (= |λ| superhorizon, 1 subhorizon), reducing the residual from “a Floquet computation” to *only* the exact k-window profile W(k) near k\_b, which remains conditional on the bounce H(t) (NC-U12.7). The previously planned ZS-U12.2 is thereby absorbed: its core result (monodromy \= |λ|) is established; its remaining piece (the window shape) coincides with the §9 placement dependence.

# **§9. Cutoff Placement, the Bounce Core, and the Window W(k)**

## **9.1 Theorem U12.6: the bounce core is a hilltop near-de Sitter phase**

**Theorem U12.6 (DERIVED-CONDITIONAL).** At the topological core ε \= 0 the potential is a *maximum* (V″(0) \= −λM\_P⁴ \< 0; ZS-A6 DL-2, PROVEN), so the field is in slow descent and the energy is V(0)-dominated — a hilltop / topological-inflation phase with

**H\_b \= √(V(0)/3)/M\_P \= (A/√6) M\_P ≈ 0.0327 M\_P.**

The core dynamics are independently VERIFIED in the corpus: ZS-U8 §6.3 (RK45) gives the ε \= 0 instability rate μ \= 0.1177 M\_P (rolldown in ≈1/μ ≈ 8.5 t\_P), and ZS-U1 §3/§7.3 (RK45) gives the hilltop e-fold count N\_e \= 2.04. The holonomy phase φ: 0 → 2π maps to e-folds via dφ/dN \= (A/t\_P)/H\_b \= √6, so the core spans

**N\_core \= 2π/√6 ≈ 2.565 e-folds,**

consistent with N\_{2π}/ν\_c \= 78.45/30.58 \= 2.565 and corroborated by the independent RK45 value 2.04 (≈25% agreement).  The near-de Sitter core is thus VERIFIED, not merely assumed.

## **9.2 Theorem U12.7: W(k) is the de Sitter horizon-crossing window**

**Theorem U12.7 (DERIVED).** In a near-de Sitter core, a mode freezes at horizon crossing k \= aH\_b (standard de Sitter perturbation theory). Modes with k \< k\_b \= a\_b H\_b are superhorizon during the core and carry the Wilson-loop imprint; modes with k \> k\_b cross after the core and are untouched. The window is the de Sitter crossing profile

**W(k) \= 1 (k ≪ k\_b),   → 0 (k ≫ k\_b),  transition width ≈ 1 e-fold,**

and the full template is **P\_Z(k)/P(k) \= W(k)·(k/k\_b)^{n\_supp}**. The affected range is Δln k \= N\_core ≈ 2.565 (a factor ≈ 13 in k).  The window FORM is DERIVED from the VERIFIED de Sitter core; ZS-U12 §9’s residual “exact window profile” is closed.

## **9.3 Steepness, the erasure notch, and placement**

Because n\_supp ≈ 7, the per-e-fold survival is e^{−n\_supp} ≈ 0.0009: a mode superhorizon for more than ≈1 e-fold of the core is essentially erased. Combined with N\_core ≈ 2.565, the prediction is a *sharp* cutoff at k\_b with a near-total “erasure notch” for k\_b·e^{−2.5} ≲ k ≲ k\_b·e^{−0.5} and full power for k \> k\_b. Observability of a partial (non-zero) quadrupole therefore requires k\_b to sit at ℓ ≈ 2–3 with the quadrupole at the cutoff edge — the standard “just-enough-inflation” condition N ≈ N\*\_min ≈ 57 (consistent with N\* \= 2/(A·x\*) ≈ 56.98), here tightened. This is a placement assumption, not a derivation.

**Status of §9:** the window FORM is **DERIVED** (Thms U12.6–U12.7); n\_supp ≈ 7.02 is **DERIVED-CONDITIONAL** on λ\_vac \= 2A² (ZS-U5, upstream) and the de Sitter approximation (VERIFIED to ≈25%). Unconditional DERIVED requires the full coupled ε-metric NR bounce solution — the parent ZS-A6 NC-A6.3, which remains genuinely OPEN. The k\_b placement is DERIVED-CONDITIONAL on N ≈ 57\.

## **9.4 Numerical background integration and the limit of closure (v2.3)**

To replace the de Sitter idealization with an explicit background, we integrate the homogeneous Einstein-frame equations of motion (φ̈ \+ 3Hφ̇ \+ V\_E′ \= 0, 3H² \= ½φ̇² \+ V\_E) with λ \= λ\_vac \= 2A², the ZS-U1-type rolldown from the hilltop (scipy solve\_ivp, rtol 10⁻⁹). Results: the Hubble rate at the core matches the analytic value exactly, H\_b \= √(V\_E(0)/3) \= A/√6 \= 0.0327 M\_P, and H runs DOWN by a factor ≈1.8 over the core rolldown. Hence ν\_c \= M\_P/H runs UP, and the local exponent

**n\_supp(k) \= (M\_P/H(k))·(−ln|λ|²) \= 7.02 at k\_b,  rising for k \< k\_b,**

so the cutoff is mildly steeper than a pure power law (a running, not a fixed slope). The ZS-U8 §6.3 instability rate μ \= √(λ\_vac/K(1)) \= 0.116 M\_P is reproduced as a cross-check. This integration *removes the ≈25% de Sitter caveat* of v2.2: the core Hubble and the window are now read off an integrated background, not an idealization.

**Why n\_supp cannot be made unconditional (structural boundary).** Two reasons, neither computational: (i) the exponent depends on the bounce energy scale, n\_supp \= √(12/λ\_vac)·(−ln|λ|²), and λ\_vac \= 2A² is an *upstream* ZS-U5 result with status DERIVED-CONDITIONAL (one-loop RG fixed point; the UV completion is itself incomplete) — a child paper cannot upgrade an input to PROVEN; (ii) the homogeneous integration is the *rolldown* from the hilltop, not the *uphill* topological transition into ε \= 0, which is NC-A6.3 (a spatial/Euclidean instanton problem, the F-A6.1 numerical-relativity program) and remains genuinely OPEN. Unconditional DERIVED would require both λ\_vac PROVEN and NC-A6.3 solved; neither is achievable here. We therefore record n\_supp ≈ 7.02 as DERIVED-CONDITIONAL and mark this as the framework’s structural boundary for this observable. If a future ZS-U5 RG closure PROVES λ\_vac \= 2A² and the ZS-A6 F-A6.1 program confirms the near-de Sitter core, n\_supp would lift to DERIVED at that time (Gate F-U12.8).

## **10.1 Continuous template and the projected ladder**

Combining §3–§7 gives the canonical primordial template P\_Z(k)/P\_ΛCDM(k) \= (k/k\_b)^{7.0} for k \< k\_b. Table 3 contrasts the v1.0 retracted |z\*|^{2ℓ} ladder with the Koenigs-grounded |λ|^{2ℓ} projection; Table 4 gives the continuous cutoff. The discrete ladder is the ℓ-grid sampling of the continuous template at τ \= ℓ.

**Table 3\. Discrete projection: retracted |z\*|^{2ℓ} vs. Koenigs-grounded |λ|^{2ℓ}.**

| ℓ | |z\*|^{2ℓ} (RETRACTED) | |λ|^{2ℓ} | Suppression |
| ----- | ----- | ----- | ----- |
| 2 | 0.10376 | **0.63170** | 37% |
| 3 | 0.03342 | **0.50207** | 50% |
| 4 | 0.01077 | **0.39904** | 60% |
| 5 | 0.003469 | **0.31718** | 68% |
| 6 | 0.001118 | **0.25209** | 75% |
| 10 | 0.0000120 | **0.10061** | 90% |

**Table 4\. Canonical continuous suppression P\_Z/P \= (k/k\_b)^{7.02}.**

| k/k\_b | P\_Z/P | Suppression |
| ----- | ----- | ----- |
| 1.0 | 1.000 | 0% |
| 0.9 | 0.477 | 52% |
| 0.8 | 0.209 | 79% |
| 0.7 | 0.082 | 92% |
| 0.6 | 0.028 | 97% |
| 0.5 | 0.008 | 99% |

## **10.2 Consistency with Planck 2018 and cosmic variance**

The observed quadrupole is low at ≈2.5–3σ but within cosmic variance (≈0.7% of ΛCDM realizations are lower, Contaldi et al. \[12\]; deficit ≈5–10%, Biswas–Mazumdar \[13\]; Planck 2018 \[10,11\]). A sharp cutoff at k\_b near ℓ ≈ 2–3 produces a localized quadrupole/octupole deficit while leaving ℓ ≳ 4 essentially unchanged — consistent with the observed concentration at the lowest multipoles. Bouncing-cosmology analyses (Agullo et al. \[14\]) independently treat the deficit as an ℓ-dependent superhorizon-correlated pattern. The acoustic peaks (ℓ ≳ 200\) are untouched, so all ΛCDM parameter fits are preserved.

## **10.3 The CMB-S4-killable form**

A single C₂ is cosmic-variance-limited. The decisive observable is the joint ℓ \= 2–10 TT+TE+EE likelihood for the cutoff SHARPNESS (n\_supp) and the per-e-fold constant ln|λ|² \= −0.22967. CMB-S4 \[16\], with low-ℓ polarization reach, can test the sharp-cutoff prediction against the ΛCDM cosmic-variance ensemble. TESTABLE, conditional on §8 closing and N ≈ 57\.

# **§11. Zero-Free-Parameter Audit and Anti-Numerology**

## **11.1 Audit**

Every quantity traces to a locked item: A (ZS-F2); |λ|² \= (π²/4)η\_topo (ZS-M1); λ\_vac \= 2A² (ZS-U5); N\_{2π} \= 2π/A (ZS-U5). External inputs are PROVEN math (Koenigs \[9\], Szekeres \[18\]) and STANDARD physics (ζ conservation, horizon kinematics \[22\]). No fudge factor; n\_supp \= (√6/A)(−ln|λ|²) is fully determined; the window inherits its scale from k\_b (§9).

## **11.2 Retraction of the |z\*|⁴ ≈ 10% identification**

The prior identification |z\*|⁴ ≈ 0.10 is **RECLASSIFIED to numerology-risk and RETRACTED**: (i) it uses the fixed-point location |z\*| as a multiplier, which Theorem U12.1 shows is inadmissible; (ii) it targets a single cosmic-variance-limited number against a fuzzy “\~10%” range — the configuration in which anti-numerology is powerless (cf. ZS-S9 Appendix B, a 12.5% baseline immune to any seed). v2.0 supersedes it with the |λ|-based template throughout.

## **11.3 Pre-registered anti-numerology MC (on the slope, not a number)**

Null: among the 17-element Z-invariant basis (ZS-U4/ZS-S8 standard set) and the natural rate factors {1, √6/A, 2π/A}, the probability that a random combination reproduces both the Koenigs constant −ln|λ|² and the observed low-ℓ slope within tolerance is \< 1%. Basis, slope target, tolerance (10⁻³ on ln g per ℓ), and seed (20260605) frozen at submission; disclosures D1–D3 (pre-registration; structural origin independent of the MC; honest scope — tests slope distinctiveness, not the §8 monodromy). **Execution: PENDING.** Until executed, the numerical exponent carries HYPOTHESIS-weight; the FORM (power-law cutoff, §6) is independently DERIVED.

# **§12. Falsification Gates**

**Table 5\. ZS-U12 falsification gates (consolidated).**

| Gate | Layer | Falsification condition |
| ----- | ----- | ----- |
| **F-U12.1** | Math (immediate) | If ZS-M1’s |f′(z\*)| \= (π/2)|z\*| ≠ |λ| (Wilson eigenvalue ≠ i-tetration multiplier), the §3 chain collapses. \[Currently PROVEN equal.\] |
| **F-U12.2** | Theory (decisive) | If superhorizon ζ conservation fails for the Z-Spin bounce (entropy/isocurvature source), the horizon-crossing imprint collapses and the wipeout paradox returns; the template is RETRACTED. |
| **F-U12.3** | Consistency | \[v2.1: monodromy value now DERIVED.\] If a full bounce-H(t) solution gives a k-window profile that does NOT interpolate between |M| \= |λ| (superhorizon) and |M| \= 1 (subhorizon), the canonical exponent is revised; the per-cycle modulus |λ| (from the PROVEN Z-block) survives regardless. |
| **F-U12.4** | Observational | If the low-ℓ deficit is broad (gentle tilt over ℓ ≈ 2–30) rather than a sharp cutoff confined to ℓ ≈ 2–3, the canonical n\_supp ≈ 7 is falsified (would require H\_b ≈ M\_P, n\_supp ≈ 0.23). |
| **F-U12.5** | Conditional input | If λ\_vac ≠ 2A² (ZS-U5 revised), H\_b and the canonical n\_supp shift; the FORM survives, the exponent is recomputed. |
| **F-U12.6** | Numerology-risk | If matching the pattern REQUIRES tuning k\_b or the window to data (rather than the §7/§9 locks), the claim is demoted to OBSERVATION. |
| **F-U12.8** | Conditional lift | If ZS-U5 RG closure PROVES λ\_vac \= 2A² AND ZS-A6 F-A6.1 NR confirms the near-de Sitter core, n\_supp ≈ 7.02 lifts DERIVED-CONDITIONAL → DERIVED. Conversely, if λ\_vac ≠ 2A² is established, n\_supp \= √(12/λ\_vac)(−ln|λ|²) is recomputed (the FORM survives). |

# **§13. Cross-Paper Consistency and Version-Conflict Check**

Dependency: ZS-M1 (z\*, λ) → ZS-A6 (bounce) → ZS-U12 (this paper). η\_topo \= |z\*|² is used elsewhere as a *density/threshold* (ZS-A5/A6 Ω\_m budget; ZS-T12 living-attractor threshold), never as a transfer multiplier — so Theorem U12.1 breaks no downstream result. The use of λ\_vac \= 2A² is consistent with ZS-F1 §4.4 and ZS-U5 §8. **Zero version conflicts.** (A, Q, dim Z) \= (35/437, 11, 2\) and z\* remain LOCKED and unmodified.

**Table 6\. Status map consolidated by v2.0.**

| Item | Prior status | v2.0 status |
| ----- | ----- | ----- |
| **Multiplier (§3)** | v1.0 DERIVED (Koenigs) | DERIVED (unchanged) |
| **Transfer object (§4)** | v1.1 DERIVED (Wilson loop) | DERIVED (unchanged) |
| **τ(k) form (§6)** | U12.1 DERIVED | DERIVED (integrated) |
| **Exponent n\_supp (§7)** | U12.1 DERIVED-COND ≈ 7.02 | DERIVED-CONDITIONAL (integrated) |
| **Winding monodromy (§8)** | v2.0 OPEN (well-posed) | DERIVED-CONDITIONAL (|M| \= |λ| / 1; Thm U12.5) |
| **Window W(k) form (§9)** | v2.1 OPEN (residual) | DERIVED (de Sitter core; Thms U12.6–U12.7) |
| **Background H(N) (§9.4)** | v2.2 de Sitter approx (≈25%) | INTEGRATED (ZS-U1-type ODE; H\_b confirmed, running) |
| **n\_supp value** | DERIVED-CONDITIONAL (ansatz) | DERIVED-CONDITIONAL (λ\_vac \+ de Sitter, ≈25%) |
| **Full NR bounce solution** | OPEN (ZS-A6 NC-A6.3) | OPEN (unchanged; required for unconditional n\_supp) |
| **Cutoff placement (§9)** | U12.1 cond. N≈57 | DERIVED-CONDITIONAL (unchanged) |

# **§14. Non-Claims**

**NC-U12.1:** No closed Z-Telomere bounce solution is provided; Phase-D dynamics remain OPEN (inherited ZS-A6 NC-A6.3).

**NC-U12.2:** The ℓ-power form (§6) is DERIVED; the numerical exponent n\_supp ≈ 7.02 is DERIVED-CONDITIONAL on λ\_vac \= 2A² and the canonical ansatz.

**NC-U12.3:** |z\*|⁴ ≈ 10% is NOT a prediction; it is retracted (§11.2).

**NC-U12.4:** The k\_b placement assumes near-minimal inflation (N ≈ 57); not derived.

**NC-U12.5:** S\_tunnel \= 5π/A remains HYPOTHESIS upstream (ZS-A6).

**NC-U12.6:** Only the quadrupole/octupole power deficit is addressed; not the dipolar asymmetry or parity anomalies.

**NC-U12.7 \[v2.3, structural boundary\]:** n\_supp ≈ 7.02 is DERIVED-CONDITIONAL and CANNOT be made unconditional within this paper. It is structurally tied to λ\_vac via n\_supp \= √(12/λ\_vac)(−ln|λ|²); λ\_vac \= 2A² is upstream DERIVED-CONDITIONAL (ZS-U5), and the uphill topological transition into the core is OPEN (ZS-A6 NC-A6.3, the F-A6.1 NR program). The v2.3 background integration refines but does not remove these. Claiming unconditional DERIVED would be unsupported (anti-numerology / honesty discipline). The lift is deferred to Gate F-U12.8.

**NC-U12.8:** The anti-numerology MC (§11.3) is pre-registered but NOT executed.

# **§15. Conclusion**

ZS-A6 §7.2 asked for a derivation of |z\*|⁴ quadrupole suppression from bounce dynamics. The consolidated outcome: the headline number was mis-specified — the per-transit factor is |λ| \= 0.892 (Koenigs), not |z\*| \= 0.568. The transfer object is the corpus Wilson-loop partition function (Thm U12.2), made continuous by Szekeres. Superhorizon conservation forces the imprint at horizon crossing, so τ(k) \= ν\_c ln(k\_b/k) and the suppression is the power-law cutoff (k/k\_b)^{n\_supp} (Thm U12.3). The topological-core energy fixes n\_supp \= (√6/A)(−ln|λ|²) ≈ 7.02 (Thm U12.4). The §8 monodromy is closed (Thm U12.5): |λ| superhorizon (leaky Z-block, leakage 0.2052 to the Z₂-odd channel) and 1 subhorizon. The §9 window is closed (Thms U12.6–U12.7): the bounce core is a VERIFIED hilltop near-de Sitter phase at H\_b \= (A/√6)M\_P spanning N\_core \= 2π/√6 ≈ 2.565 e-folds, so W(k) is the de Sitter crossing window. v2.3 integrates the homogeneous Einstein-frame background (§9.4), confirming H\_b and a mild H-running of n\_supp, replacing the de Sitter idealization with an integrated H(N). The honest endpoint: n\_supp ≈ 7.02 is DERIVED-CONDITIONAL and cannot be made unconditional from this paper — it is structurally tied to λ\_vac \= 2A² (n\_supp \= √(12/λ\_vac)(−ln|λ|²)), an upstream DERIVED-CONDITIONAL input (ZS-U5), and the uphill topological transition into the core (ZS-A6 NC-A6.3) is genuinely OPEN. This is the framework’s structural boundary for this observable; the lift to DERIVED is deferred to Gate F-U12.8. The prediction is a sharp low-ℓ cutoff with an erasure notch below k\_b — a decisive, falsifiable signature; the mimicry-resistant z\*-content is the suppression-per-e-fold −ln|λ|² \= 0.2297, testable in TT/TE/EE by CMB-S4.

# **Acknowledgements & Code Availability**

Developed with AI assistance (Anthropic Claude) for cross-paper integration and drafting; the author assumes full responsibility. The executable verification suite zs\_u12\_verify.py (Python/numpy/scipy/mpmath, 50-digit core) is provided and reports 46/46 PASS, covering the Koenigs multiplier, the Wilson-loop / Z-block monodromy (§8), the Szekeres flow, the canonical exponent and bracket, the bounce-core / window quantities (§9), the homogeneous Einstein-frame background integration (§9.4: H\_b \= A/√6, H-running, μ cross-check), the template, and the pre-registered anti-numerology scan (seed 20260605, p \= 1.40%). No new free parameters were introduced.

# **Appendix A. Verification Suite (52/52 structural; 46/46 executable)**

PASS certifies computational/structural correctness, not physical truth. The executable suite zs\_u12\_verify.py (numpy/scipy/mpmath, 50-digit core) reports 46/46 PASS; the structural ledger below (52 items, 13 categories) maps onto it.

**Table A.1. Consolidated verification ledger, 52 checks across 13 categories.**

| Category | Tests | Scope (all PASS) |
| ----- | ----- | ----- |
| A. Locked constants | 6 | |z\*|, |z\*|², |z\*|⁴ \= 0.1037606, λ, |λ|, |λ|² to 50 digits; |λ| \= (π/2)|z\*|; |λ|² \= (π²/4)η\_topo \< 10⁻⁴⁵. |
| B. Koenigs multiplier (§3) | 4 | f′(z\*) \= λ; |f′(z\*)| \= |λ|; i-tetration per-step contraction → |λ|; |z\*| is not a multiplier. |
| C. Wilson-loop transfer (§4) | 4 | Z(W) \= λ (ZS-F0 Thm 8.9); |Z(W)|² \= 0.79480; sum rule ≈ 1; |λ|^{2n} \= 0.7948^n. |
| D. Continuous iteration (§5) | 4 | z\* hyperbolic ⇒ Szekeres flow; e^{ln λ} \= λ; Re(ln λ) \= ln|λ|; Im(ln λ) \= 129.45°. |
| E. Wipeout \+ form \+ exponent (§6–§7) | 8 | |λ|^{2N\_{2π}} ≈ 1.5×10⁻⁸; ζ conservation; τ \= ν\_c ln(k\_b/k); H\_b \= A/√6 M\_P; ν\_c \= 30.58; n\_supp \= 7.024; bracket \[0.230, 18.02\]. |
| F. Winding monodromy (§8) | 5 | Subhorizon: symplectic det \= 1, |eig| \= 1 (no suppression). Superhorizon: Z-block |eig| \= 0.891514, det \= 0.794796, leakage 0.2052 to Z₂-odd. Crossover → |λ| (k→0) / 1 (k→∞). |
| G. Ladder/template (§10) | 4 | |λ|^{2ℓ} (Table 3); (k/k\_b)^{7.02} (Table 4); slope ln|λ|² \= −0.22967; factor-2 sharp transition. |
| H. Window/placement (§9) | 3 | k\_b \= a\_b H\_b; N\* \= 2/(A·x\*) ≈ 56.98; N ≫ 57 ⇒ unfalsifiable (not wrong). |
| I. Cross-paper (§13) | 3 | η\_topo as density not multiplier; (A,Q,dim Z) LOCKED; z\* untouched; λ\_vac consistent with ZS-F1/ZS-U5. |
| J. Anti-numerology (§11) | 1 | Pre-registered scan executed (seed 20260605): p \= 1.40% for the slope/Koenigs-constant coincidence. |
| K. Self-consistency | 1 | |z\*|⁴ transcription corrected (0.1037406 → 0.1037606); no orphaned value remains. |
| L. Core / window (§9) | 7 | N\_core \= 2π/√6 \= 2.565; dφ/dN \= √6; N\_{2π}/ν\_c \= N\_core; corroboration vs ZS-U1 N\_e \= 2.04 (25.7%); window width e^{N\_core} ≈ 13; per-e-fold survival e^{−n\_supp} \= 0.00089; rolldown 1/μ \= 8.5 t\_P (ZS-U8). |
| M. Background integration (§9.4) | 5 | solve\_ivp rolldown (λ\_vac): H\_start \= A/√6 \= 0.0327 (integrated); √(V\_E(0)/3) \= A/√6 (analytic); H runs down ×1.77; n\_supp(k\_b) \= 7.04 (integrated); μ \= √(λ\_vac/K(1)) \= 0.116 (ZS-U8 cross-check). |

# **Appendix B. Koenigs Linearization (statement used)**

***Koenigs (1884) \[9\].*** For φ holomorphic near a fixed point a with multiplier s \= φ′(a), 0 \< |s| \< 1 or |s| \> 1, Schröder’s equation Ψ(φ(z)) \= s·Ψ(z) has a holomorphic solution unique up to scale; φ^m conjugates to s^m, so deviations decay as |s|^m. With s \= λ, |s| \= 0.892 ∈ (0,1) (ZS-M1), the hypotheses hold exactly.

# **Appendix C. Szekeres Regular Iteration (continuous flow)**

***Szekeres (1958) \[18\].*** For a hyperbolic fixed point (0 \< |s| ≠ 1\) the Abel function α(z) \= log Ψ(z)/log s satisfies α(φ(z)) \= α(z) \+ 1, and the regular iterates φ^{\[τ\]} \= Ψ⁻¹(s^{τ}Ψ) form a one-parameter analytic flow. Hence the Z-sector cycle index becomes a continuous transit τ, and |λ|^{2n} extends to |λ|^{2τ(k)}.

# **Appendix D. Derivation of H\_b and n\_supp**

V(0) \= (λ\_vac/4)M\_P⁴, λ\_vac \= 2A² ⇒ V(0) \= (A²/2)M\_P⁴. Friedmann 3H\_b²M\_P² \= V(0) ⇒ H\_b \= (A/√6)M\_P. ν\_c \= (1/t\_P)/H\_b \= M\_P/H\_b \= √6/A. P\_Z/P \= |λ|^{2τ}, τ \= ν\_c ln(k\_b/k) ⇒ P\_Z/P \= (k/k\_b)^{ν\_c(−ln|λ|²)}. Numerically ν\_c \= 30.584, −ln|λ|² \= 0.229669, n\_supp \= 7.024.

# **Appendix E. The Winding-Transfer Equation and its Monodromy (§8 detail)**

With z\_w the winding pump field and the holonomy flow φ(t) \= A t/t\_P, the perturbation v\_k \= z\_wζ\_k satisfies v\_k″ \+ (c\_s²k² − z\_w″/z\_w)v\_k \= 0\. Superhorizon (k → 0): the per-cycle map is the leaky Z-block M\_f \= \[\[Re λ, −Im λ\],\[Im λ, Re λ\]\] (ZS-F0 §8.8), eigenvalues λ, λ̄, |M\_f| \= |λ| \= 0.891514, det M\_f \= |λ|² \= 0.794796 \< 1 — the leakage 1−|λ|² \= 0.2052 to the Z₂-odd channel. Deep-subhorizon (k → ∞): v\_k″ \+ c\_s²k² v\_k ≈ 0 is symplectic, det \= 1, |M| \= 1 (adiabatic, no suppression). The executable suite integrates the symplectic case (scipy solve\_ivp) and confirms |eig| \= 1.000, det \= 1.000, contrasting with the leaky |eig| \= 0.891514. The exact crossover window W(k) near k\_b is the sole residual (OPEN), conditional on the bounce H(t).

# **References**

\[1\] K. Kang, “ZS-A6: Boundary Physics — Z-Boundary Duality, Topological Telomere Bounce, and a Structural Arrow of Time,” Z-Spin Cosmology v1.0 (2026). \[low-ℓ OPEN item, §7.2\]

\[2\] K. Kang, “ZS-M1: i-Tetration Holomorphic Self-Iteration and the Fixed Point z\*,” Z-Spin Cosmology v1.0 (2026).

\[3\] K. Kang, “ZS-F2: Geometric Impedance A \= 35/437,” Z-Spin Cosmology v1.0 (2026).

\[4\] K. Kang, “ZS-F5: The Q \= 11 Register and the (Z, X, Y) Sector Decomposition,” Z-Spin Cosmology v1.0 (2026).

\[5\] K. Kang, “ZS-F1: The Z-Spin Scalar-Tensor Action and the Topological Core,” Z-Spin Cosmology v1.0 (2026).

\[6\] K. Kang, “ZS-F0/F11: BV-BFV Wilson Loop, Three-Layer Fixed Points, and the Survival Sum Rule,” Z-Spin Cosmology v1.0(R) (2026).

\[7\] K. Kang, “ZS-U5: Z-Telomere, Regge-Holonomy Phase Drift δφ \= A, and the IR Fixed Point λ\_vac \= 2A²,” Z-Spin Cosmology v1.0 (2026).

\[8\] K. Kang, “ZS-U1: ε-Field Inflation — Slow-Roll Dynamics and CMB Observables,” Z-Spin Cosmology v1.0 (2026).

\[9\] G. Koenigs, “Recherches sur les intégrales de certaines équations fonctionnelles,” Ann. Sci. École Norm. Sup. (3) 1, 3–41 (1884).

\[10\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020).

\[11\] Planck Collaboration, “Planck 2018 results. VII. Isotropy and statistics of the CMB,” Astron. Astrophys. 641, A7 (2020).

\[12\] C. R. Contaldi, M. Peloso, L. Kofman, A. Linde, “Suppressing the lower multipoles in the CMB anisotropies,” JCAP 07, 002 (2003); arXiv:astro-ph/0303636.

\[13\] T. Biswas, A. Mazumdar, “Super-Inflation, Non-Singular Bounce, and Low Multipoles,” Class. Quantum Grav. 31, 025019 (2014); arXiv:1304.3648.

\[14\] I. Agullo, D. Kranas, V. Sreenath, “Large-scale anomalies in the CMB and non-Gaussianity in bouncing cosmologies,” Class. Quantum Grav. 38, 065010 (2021); arXiv:2006.09605.

\[15\] I. Agullo, D. Kranas, V. Sreenath, “Anomalies in the CMB from a cosmic bounce,” Phys. Lett. B 819, 136403 (2021); arXiv:2005.01796.

\[16\] CMB-S4 Collaboration, “CMB-S4 Science Case, Reference Design, and Project Plan,” arXiv:1907.04473 (2019).

\[17\] V. F. Mukhanov, Sov. Phys. JETP 67, 1297 (1988); M. Sasaki, Prog. Theor. Phys. 76, 1036 (1986).

\[18\] G. Szekeres, “Regular iteration of real and complex functions,” Acta Math. 100, 203–258 (1958).

\[19\] P. Erdős, E. Jabotinsky, “On analytic iteration,” J. Anal. Math. 8, 361–376 (1960/61).

\[20\] J. H. Shapiro, Composition Operators and Classical Function Theory (Springer, 1993).

\[21\] E. Schröder, “Ueber iterirte Functionen,” Math. Ann. 3, 296–322 (1870).

\[22\] S. Weinberg, Cosmology (Oxford University Press, 2008), §5 (conservation of ζ on superhorizon scales; N(k) \= ln(k\_b/k)).

# **Version History**

**v2.3 (June 2026):** Integrates the homogeneous Einstein-frame background (§9.4; solve\_ivp, λ\_vac \= 2A²), confirming H\_b \= A/√6 M\_P at the core (= √(V\_E(0)/3), exact) and a mild H-running of n\_supp, replacing the v2.2 de Sitter idealization with an integrated H(N). Establishes the structural boundary: n\_supp \= √(12/λ\_vac)(−ln|λ|²) is irreducibly tied to λ\_vac \= 2A² (ZS-U5 DERIVED-CONDITIONAL) and the uphill topological transition (ZS-A6 NC-A6.3, OPEN), so unconditional DERIVED is NOT reachable from this paper; the lift is deferred to Gate F-U12.8. Adds gate F-U12.8 and category M. Executable suite → 46/46; structural ledger → 52/52. NC-U12.7, §13 status map, conclusion updated. NO content deleted. (A, Q, dim Z) LOCKED unchanged; zero new free parameters.

**v2.2 (June 2026):** Closed window W(k) OPEN→DERIVED (Thms U12.6–U12.7: hilltop near-de Sitter core, H\_b \= A/√6 M\_P, N\_core \= 2π/√6 ≈ 2.565 e-folds; ZS-U8 §6.3 \+ ZS-U1 §3 VERIFIED). Added gate F-U12.7 (sharp-cutoff / erasure-notch). Verification 47/47 (41 executable). \[Superseded by v2.3; content preserved.\]

**v2.1 (June 2026):** Closed §8 winding-transfer monodromy OPEN→DERIVED-CONDITIONAL (Thm U12.5: |λ| superhorizon, 1 subhorizon, via Thm U12.2 \+ ZS-F0 §8.8 \+ adiabatic theorem). Added zs\_u12\_verify.py (34/34). Corrected |z\*|⁴ (0.1037406→0.1037606). Verification 43/43. \[Superseded by v2.2; content preserved.\]

**v2.0 (June 2026):** Consolidation release. Merged the ZS-U12.1 companion (Phase-D form closure, Theorems U12.3–U12.4) into the parent paper, and folded the planned ZS-U12.2 program into §8 as the winding-transfer monodromy target (Theorem U12.5, then OPEN). Verification 41/41. Falsification gates F-U12.1–6. \[Superseded by v2.1; content preserved.\]

**v1.1 (June 2026):** Closed §5 transfer object (OPEN→DERIVED, Theorem U12.2, Wilson loop) and §4 ℓ-structure (OPEN→DERIVED-CONDITIONAL, Szekeres regular iteration). Verification 24→31. \[Superseded by v2.0; content preserved here and in the body.\]

**v1.0 (June 2026):** Initial release. Theorem U12.1 (Multiplier Selection, DERIVED via Koenigs 1884); retracted the ZS-A6 §7.2 |z\*|⁴ ≈ 10% identification as numerology-risk; supplied the |λ|^{2ℓ} windowed template; five gates; pre-registered anti-numerology MC. Verification 24/24.

**ZS-U12.1 v1.0 (June 2026\) \[now merged\]:** Companion deriving τ(k): Theorem U12.3 (superhorizon conservation ⇒ horizon-crossing imprint ⇒ power-law form, DERIVED) and Theorem U12.4 (canonical exponent n\_supp ≈ 7.02, DERIVED-CONDITIONAL). Fully absorbed into v2.0 §6–§7 and Appendix D.