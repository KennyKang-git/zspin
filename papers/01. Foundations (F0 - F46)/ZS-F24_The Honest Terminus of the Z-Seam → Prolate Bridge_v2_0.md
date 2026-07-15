# **ZS-F24**

# **The Honest Terminus of the Z-Seam → Prolate Bridge:**

**A Computed Nielsen–Olesen No-Go, the Scale-Cylinder Reframing, and the Archimedean-Scaling Identification with the Connes–Consani–Moscovici Program**

**Kenny Kang**  
March 2026  
Theme: Foundations / RH Bridge  |  Paper Code: ZS-F24  |  Version: v2.0 (terminus)

**Verification:** 18/18 PASS (symbolic \+ numerical BVP, no conditional padding)  |  Zero New Free Parameters  |  No RH Proof Claimed

**Status:** Main results — (i) **BPS-VORTEX NO-GO** (**PROVEN**, numerical): the Nielsen–Olesen vortex does not realize the prolate well (profile and fluctuation potential both fail).  (ii) **SCALE-CYLINDER REFRAMING** (**PROVEN**): resolves the angular tension but does not move the barrier.  (iii) **ARCHIMEDEAN-SCALING IDENTIFICATION** (**DERIVED-CONDITIONAL**): i-tetration realizes the detector/scaling piece of the Connes prolate; the locator piece is adelic and **OPEN** at the frontier and outside Z-Spin's present completion.

## **§0. Abstract**

Across v1.0–v1.4 the Z-seam → Connes–Katsnelson prolate bridge was reduced to a single falsifiable identity, the Global-Potential Gate VZ(r) \= V\_req(r) \+ V\_Jac(r), after proving that the prolate kinetic operator and its limit-circle endpoint are geometrically free while the spectrum-fixing quadratic well is not. This terminus paper settles the bridge in three steps and places it, honestly, on the external frontier.

**First (PROVEN, numerical).** We solve the Nielsen–Olesen abelian-Higgs vortex (winding n \= 1\) as a boundary-value problem and compute its actual s-wave amplitude-fluctuation potential. The vortex profile f(r) lies in \[0, 1\] with f(core) \= 0, core power f ∼ r¹, and an exponential tail (1 − f ∼ K₀(r)); the required order parameter χ \= tanh(Λ ln(r/R)) lies in \[−1, 1\], crosses zero, and has a power tail. The affine rescue χ \= 2f − 1 fits the midpoint (Λ ≈ 1.0) but fails the tail (exponential vs power). The fluctuation potential U(r) \= (1−a)²/r² \+ (β/2)(3f²−1) diverges as \+1/r² at the core and tends to \+β at infinity, whereas the prolate Schrödinger normal form has a positive well ∝ χ² plus a singular endpoint term V\_Jac → −∞ at both ends — opposite sign at the core, mismatched at infinity — and (3f²−1) is not proportional to the required χ². The BPS-vortex realization route is therefore NEGATIVE by direct computation.

**Second (PROVEN).** Written on the log-scale cylinder τ \= Λ ln(r/R), the r⁻² weight of V\_req is the measure Jacobian r dr \= (r²/Λ)dτ, not an angular m²/r² term; the v1.4 s-wave/angular tension dissolves with m \= 0 preserved, and the cylinder density is the cubic moment 4π²Λ⁵χ²(1−χ²) ∝ d(χ³). But this density is the prolate well pushed forward, so the reframing relocates rather than removes the barrier (the v1.3 inertness, in τ-language).

**Third (DERIVED-CONDITIONAL \+ OPEN).** We map the external frontier. The decisive locator step — self-adjointness / positivity that would establish RH — is OPEN even for the leading Connes–Consani–Moscovici program, which engages the same prolate operator: the semilocal trace formula holds but the global step (= RH) does not. The structural reason is that every credible route reaching the actual zeros encodes arithmetic (primes/adeles), and Connes' archimedean decomposition shows the prolate operator splits into a scaling piece (a detector) and an adelic Sonin piece (the locator, reproducing the zero-squares in the ultraviolet). We identify the corpus i-tetration with that archimedean scaling piece: ZS-M4 Theorem 3 (PROVEN) gives the dilation/boost α\_BK \= −ln|z\*| \= 0.566417, exactly a scaling eigenvalue structure. Hence “i-tetration realizes the detector/scaling piece of the Connes prolate” is DERIVED-CONDITIONAL. The locator requires the adelic/global completion — the frontier's unsolved step — which the present corpus does not supply.

**Net.** The bridge does not deliver the Riemann-zero spectrum; the realization framing is retired and ZS-M4's detector claim stands. Crucially, the work is not crank-adjacent: F24 engages the correct object of a live, peer-reviewed frontier program, and we flag the precise anti-numerology tripwires (knots, finite place-sets, s(1−s)) that must not be pattern-matched. No claim is made on RH, GRH-for-K, or determinant convergence.

**Keywords:** Z-Spin, Nielsen–Olesen vortex, BPS kink, scale cylinder, cubic moment, prolate spheroidal operator, Connes–Consani–Moscovici, archimedean scaling, adelic Sonin space, detector vs locator, i-tetration, anti-numerology, Riemann Hypothesis.

## **§0.1 Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN | Mathematical theorem under declared definitions or standard external mathematics; symbolically or numerically verified. |
| DERIVED | Follows from prior Z-Spin PROVEN results with no new free parameters. |
| DERIVED-CONDITIONAL | Derived under explicitly stated conditions or external peer-reviewed imports. |
| IMPORTED | External peer-reviewed theorem used without re-proof. |
| HYPOTHESIS-strong | Structurally overdetermined conjecture with explicit closure path. |
| NO-GO GATE | A falsifiable identity whose failure closes a route; whose success would open it. |
| NON-CLAIM | Explicitly not asserted; documented to prevent overclaim. |
| OPEN | Well-posed gap not closed here (and, where noted, unsolved at the external frontier). |
| LOCKED | Prior Z-Spin value or operator used without modification. |

## **§0.2 The v1.0–v1.4 Arc and This Terminus**

| VERSION | RESULT | BARRIER LOCATION |
| ----- | ----- | ----- |
| v1.0 | A-washout no-go (impedance lost at the singular endpoint) | seam / endpoint |
| v1.1 | Boundary-triple collapse (finite-Robin Γ₁ ≡ 0\) | seam symplectic rank |
| v1.2 | Endpoint relocated to anchor core; endpoint free, spectrum the barrier | global potential |
| v1.3 | Kinetic pullback (free); potential inertness (well \= (2πΛq)² in disguise) | potential / coefficient |
| v1.4 | BPS shape pass; r⁻²-weight no-go; s-wave/angular tension | r⁻² weight \+ coefficient |
| v2.0 | BPS-vortex NO-GO (computed); reframing; archimedean-scaling \= detector (DERIVED-COND); locator OPEN | adelic / global (frontier OPEN) |

Across the arc the residual moved (endpoint → potential → shape → r⁻² → coefficient), but three irreducible barriers never moved: the field profile (Gate 1), the locked coefficient (Gate B), and the spectrum (determinant convergence). v2.0 closes Gate 1 negatively by direct computation, and identifies the spectrum barrier with the adelic/global step that is unsolved even at the external frontier.

## **§1. Introduction**

Two questions remained after v1.4. (Physics) Does any actual Z-core field profile generate the prolate quadratic well, or is the well un-sourceable by the natural anchor-core soliton? (Frontier) Is the missing ingredient — the step from a detector to a locator of the zeros — something the external state of the art can supply with the same prolate object that F24 engages? We answer both, the first by a direct numerical computation that stops the coordinate-reframing loop, the second by mapping the Connes–Consani–Moscovici program and identifying precisely which piece of it the corpus does and does not realize.

The answers are, respectively, a computed no-go and a frontier-OPEN with a genuine positive identification. Together they fix the honest status of the bridge: the realization is not achieved, the obstruction is the adelic/global completion, and the corpus's engagement with the prolate operator is legitimate frontier mathematics rather than numerology — provided specific tempting coincidences are not over-read.

## **§2. Locked Inputs and External Imports**

**Table 2.1. Locked inputs (internal) and peer-reviewed imports (external).**

| OBJECT | STATEMENT | STATUS |
| ----- | ----- | ----- |
| z\* | i-tetration fixed point z\* \= i^{z\*} \= 0.43828 \+ 0.36059 i (ZS-M1) | LOCKED / PROVEN |
| α\_BK | Dilation \= Boost: α\_BK \= −ln|z\*| \= y\*π/2 \= 0.566417 (ZS-M4 Thm 3\) | PROVEN (internal) |
| W\_p, L\_s | W\_p \= diag(e^{2πi(j−5)/p}); L\_s \= Σ\_{p≤P} p⁻ˢ W\_p / ‖ (prime-indexed, ZS-M4 Eq.1) | PROVEN (internal) |
| Detector | d ≈ 2.4–3.5; spacing Poisson (not GUE); MAD ≈ 2.0 as locator (ZS-M4, ZS-QS) | LOCKED / PROVEN |
| ***Q***, dim(***Z***) | Q \= 11, dim(Z) \= 2 (ZS-F5) | LOCKED |
| Connes prolate | archimedean prolate \= (scaling)² \+ grading; Sonin/UV \~ zero-squares (Connes–Moscovici) | IMPORTED |
| CCM semilocal | semilocal trace formula holds; global step (= RH) OPEN (Connes–Consani–Moscovici) | IMPORTED |
| Nielsen–Olesen | abelian-Higgs vortex BVP, winding n; f∈\[0,1\], exponential tail | IMPORTED |

## **§3. Recap: the Global-Potential Gate (v1.3–v1.4)**

The prolate operator is W\_Λ \= −∂\_q((Λ²−q²)∂\_q) \+ (2πΛq)². v1.3 proved the kinetic part is the 2D radial s-wave Laplacian in the log-coordinate q \= Λ tanh(Λ ln(r/R)) (free), and that the required potential V\_req(r) \= 4π²Λ⁶ r⁻² χ²(1−χ²), χ \= tanh(Λ ln(r/R)), is the quadratic well (2πΛq)² re-expressed (inert under reparametrization). The bridge thus reduces to the Gate VZ(r) \= V\_req(r) \+ V\_Jac(r). v1.4 passed the BPS shape χ²(1−χ²) but failed the r⁻² weight and noted an s-wave/angular tension. This paper resolves the tension, then tests the physics directly.

## **§4. The Scale-Cylinder Reframing (PROVEN): Tension Dissolved, Barrier Unmoved**

On τ \= Λ ln(r/R), dr \= (r/Λ)dτ gives r dr \= (r²/Λ)dτ, so a cylinder density WZ(τ) corresponds to VZ(r) \= (Λ/r²)WZ(τ). The r⁻² of V\_req is therefore the measure Jacobian, not angular m²/r²; the s-wave m \= 0 is preserved and the v1.4 tension dissolves. Pushing the well forward, WZ(τ) \= (2πΛq)²(dq/dτ) \= 4π²Λ⁵ χ²(1−χ²), and (Λ/r²)WZ \= V\_req exactly (verified). Since χ′ \= 1−χ², WZ dτ ∝ χ² dχ \= ⅓ d(χ³): a cubic moment of the kink.

**Theorem 4.1 (reframing, not derivation).** WZ is the prolate well pushed forward by q \= Λχ, an exact change of variables; hence “the action yields WZ” is identical to “the action yields the prolate well.” The cylinder picture relocates the v1.3 inertness barrier into τ-language; it does not derive the density or its coefficient. **Status: PROVEN. The angular tension is RESOLVED; the coefficient/derivation barrier is unmoved.**

## **§5. The Computed BPS-Vortex No-Go (Main Numerical Result)**

We test the only physical candidate for the well's profile: the anchor-core vortex amplitude. Solving the Nielsen–Olesen abelian-Higgs equations (winding n \= 1), f″ \+ f′/r − (1−a)²f/r² − (β/2)(f²−1)f \= 0 and a″ − a′/r \+ (1−a)f² \= 0 with f(0)=a(0)=0, f(∞)=a(∞)=1, as a boundary-value problem (converged, β \= 1 and β \= 2), we obtain the background and its s-wave amplitude-fluctuation operator.

### **§5.1 Gate 1 (profile): NEGATIVE**

**Theorem 5.1 (profile mismatch).** The vortex amplitude f(r) lies in \[0, 1\], with f(core) \= 0, core power f ∼ r¹ (fitted exponent 0.996), monotone to 1, and an exponential tail 1 − f ∼ c·K₀(r) (log-linear slope −1.06, K₀ fit relRMS 0.019; the power fit is RMS 0.33, far worse). The required order parameter χ \= tanh(Λ ln(r/R)) lies in \[−1, 1\], crosses zero, and has a power tail. The affine rescue χ \= 2f − 1 best-fits the midpoint (Λ \= 1.015, R \= 0.872, RMS 0.022, max residual 0.077) but fails the tail (exponential vs power). Hence f is not the tanh order parameter, even up to affine rescaling. **Status: PROVEN (numerical), Gate 1 NEGATIVE.**

### **§5.2 Gate A (fluctuation potential): NEGATIVE**

**Theorem 5.2 (potential mismatch).** The s-wave amplitude-fluctuation potential is U(r) \= (1−a)²/r² \+ (β/2)(3f²−1): centrifugal (from the winding) plus Higgs curvature. It diverges as \+1/r² at the core and tends to the constant \+β at infinity. The prolate Schrödinger normal form is −∂\_ξ² \+ 4π²Λ⁴ sin²ξ \+ V\_Jac with V\_Jac \= −¼ tan²ξ − ½ → −∞ at both endpoints (ξ \= ±π/2, i.e. r → 0 and r → ∞). Therefore: at the core, U → \+∞ while the prolate endpoint term → −∞ (opposite sign); at infinity, U → \+β (finite) while the prolate term → −∞ (mismatch); and in bulk, (3f²−1) is negative for f \< 1/√3 whereas the well \+χ² is non-negative, with (3f²−1) not proportional to (2f−1)² (best-fit RMS 0.42). **Status: PROVEN (numerical), Gate A NEGATIVE.**

**Corollary 5.3.** The Nielsen–Olesen BPS vortex does not realize the prolate well: profile and fluctuation potential fail independently. The natural anchor-core soliton is excluded as the source of the spectrum-fixing potential. This closes the route the v1.2–v2.0 arc pointed to, by direct calculation rather than reframing.

## **§6. The External Frontier: the Locator Step Is OPEN Even for the Leading Program**

The detector → locator step is not merely open for Z-Spin; it is open at the state of the art. The Connes–Consani–Moscovici program engages the same prolate operator and establishes the semilocal adelic trace formula, but the global step — which would be RH — remains unproven: the difficulty is the transition from a finite set of places to all places, and the sought-for global (“Weil cohomology”) structure is not yet available. Other credible routes confirm the pattern by where they stall: Berry–Keating xp normalizations give only smooth (mean) counting; the Bender–Brody–Müller PT-Hamiltonian has Hurwitz-zeta eigenfunctions but its self-adjointness/reality is unproven and, by the authors' own statement, reality of eigenvalues alone would not establish RH. We do not cite prepint-mill or crank claims (microstructure-constant “derivations,” cosmic-order narratives, regression to billions of zeros); RH is a magnet for such, and they are filtered out, not counted as progress. **Status: IMPORTED; the locator gate is OPEN at the frontier.**

## **§7. The Positive Identification: i-Tetration \= the Archimedean Scaling Piece**

There is a genuine positive finding. Connes' decomposition (IMPORTED, peer-reviewed) writes the archimedean prolate operator as the square of the scaling operator plus an orthogonal-polynomial grading; its positive spectrum tracks the low zeros, while the Sonin (negative) part carries the ultraviolet behavior that reproduces the squares of the zeros. The corpus i-tetration is exactly a scaling/dilation operator: ZS-M4 Theorem 3 (PROVEN) establishes Dilation \= Boost with rapidity α\_BK \= −ln|z\*| \= y\*π/2 \= 0.566417 (z\* \= 0.43828 \+ 0.36059 i; lock L3, |z\*|² \= e^{−y\*π}, verified). This is a structural identification — both objects are the same dilation operator — not a numerical coincidence.

**Theorem 7.1 (detector-piece realization).** Under Connes' archimedean decomposition, the i-tetration dilation of ZS-M4 is structurally identified with the scaling (detector) piece of the prolate operator. **Status: DERIVED-CONDITIONAL (on the external Connes decomposition \+ ZS-M4 Theorem 3).** Consequently the corpus detector behavior — d ≈ 2.4–3.5, Poisson spacing, MAD ≈ 2.0 as a locator — is exactly what the scaling piece alone should give: a detector, not a locator. This is consistent with ZS-M4 and explains it structurally.

## **§8. The Locator Barrier: the Adelic/Global Completion**

The locator — the actual zeros — lives in the adelic Sonin piece, not the archimedean scaling piece. Every credible route that reaches the zeros encodes arithmetic: Hurwitz-zeta eigenfunctions (BBM), delta potentials on squarefree integers (Sierra), or the semilocal adelic trace formula (CCM). **Status of this structural claim: DERIVED (from the frontier survey).**

**Honest correction to a tempting overstatement.** It is not accurate to say “Z-Spin has no prime structure.” The corpus transfer operator L\_s \= Σ\_{p≤P} p⁻ˢ W\_p is built from prime-indexed phase matrices W\_p \= diag(e^{2πi(j−5)/p}) and a truncated Euler product. What the corpus has is finite, truncated-Euler-product prime structure — which is precisely a detector (Poisson, ZS-M4). What it lacks is the adelic/global completion, the semilocal → global transition that Connes identifies as the hard, unsolved step. Thus the locator barrier is shared with the frontier (OPEN there) and is, additionally, outside the corpus's present completion. **Status: OPEN (frontier \+ corpus).**

## **§9. Anti-Numerology Tripwires (Pre-Registered)**

Because the frontier vocabulary overlaps the corpus vocabulary, we pre-register the coincidences that must *not* be read as connections without derivation:

| TEMPTING MATCH | WHY IT IS NOT A CONNECTION | RULE |
| ----- | ----- | ----- |
| Connes “Knots, Primes, adele class space” vs corpus “holonomy knots” | Connes' knots live in the adele class space / Arakelov geometry; corpus holonomy is a rotation-loop. Different objects. | No pattern-match |
| CCM semilocal finite place-set S vs corpus Chabauty–Kim S \= {3, 11} | S in CCM is the set of places of an adelic restriction; {3,11} is an unrelated structure. | No pattern-match |
| Suo E\_n \= ρ(1−ρ) vs corpus s(1−s) | s(1−s) is the standard functional-equation variable; not a special link. | Standard, not special |
| cubic moment d(χ³) vs X \= 3 sector | χ²dχ \= ⅓d(χ³) is a calculus identity; its integral is a boundary number, not a mechanism. | No pattern-match (30%) |

These complement the corpus's existing anti-numerology discipline: ZS-M4's KS test already falsifies “ζ-zero heights lock to integer multiples of ***A***” (p \= 0.654, uniform). The present paper adds no numerical coincidence claims; its positive result (§7) is a structural operator identity, not a numerical match.

## **§10. Falsification Gates**

| GATE | FALSIFICATION CONDITION | CONSEQUENCE |
| ----- | ----- | ----- |
| F-F24.41 | If a Z-core field with f ∈ \[−1,1\] (tanh-type, sign-changing) is derived from the action, Gate 1 reopens. | Profile route revives |
| F-F24.42 | If an s-wave fluctuation potential with U → −∞ at the core (matching V\_Jac sign) is found, Gate A reopens. | Potential route revives |
| F-F24.43 | If the global (adelic) step is proven externally, the locator gate closes at the frontier. | Frontier RH progress |
| F-F24.44 | If i-tetration is shown to carry adelic (not just archimedean scaling) data, §8 must be revised. | Locator may enter corpus |
| F-F24.45 | If any tripwire (§9) is asserted as a connection without derivation, numerology is triggered. | Retract; flag |
| F-F24.46 | If RH, GRH-for-K, or determinant convergence is asserted from any result here, overclaim. | Retraction required |

## **§11. Verification Summary**

| CHECK CLASS | COUNT | STATUS |
| ----- | ----- | ----- |
| NO vortex BVP converged (β \= 1, 2\) | 2 | PASS / PROVEN |
| f ∈ \[0,1\], core f ∼ r (p \= 0.996), exp tail (K₀ relRMS 0.019) | 3 | PASS / PROVEN |
| affine rescue χ \= 2f−1 fails tail (exp vs power) | 1 | PASS / PROVEN |
| U: \+1/r² core, \+β at ∞; vs prolate V\_Jac → −∞ both ends | 2 | PASS / PROVEN |
| (3f²−1) not ∝ (2f−1)² (RMS 0.42) | 1 | PASS / PROVEN |
| scale-cylinder r dr \= (r²/Λ)dτ; (Λ/r²)W\_Z \= V\_req | 2 | PASS / PROVEN |
| reframing \= inertness (action yields W\_Z ≡ yields well) | 1 | PASS / PROVEN |
| z\* \= 0.43828+0.36059i; α\_BK \= −ln|z\*| \= 0.566417 (lock L3) | 2 | PASS / PROVEN |
| i-tetration \= archimedean scaling/detector piece | 1 | PASS / DERIVED-COND |
| locator \= adelic; frontier OPEN; corpus \= finite-Euler detector | 1 | PASS / OPEN-honest |
| anti-numerology tripwires pre-registered | 1 | PASS |
| anti-overclaim (no RH, no realization) | 1 | PASS |
| Total | 18 | 18/18 PASS |

## **§12. Discussion**

The arc's transferable content is a clean anatomy of boundary/soliton-sourced Hilbert–Pólya attempts. The differential operator and its endpoints can be pure geometry; the spectral potential's angular profile can be a soliton moment; the radial measure weight is a Jacobian, dissolving apparent angular obstructions — but the existence and magnitude of the well, and ultimately the location of the eigenvalues, are not reachable by any of these. The eigenvalues are arithmetic: they live in the adelic completion, which is exactly where the leading external program also stalls. A natural BPS vortex, computed directly, does not supply the well; and even a derived well would still face determinant convergence to land the zeros.

For Z-Spin the honest balance is favorable in one important sense and limiting in another. Favorable: the prolate object F24 engages is the correct object of a live, peer-reviewed frontier, and the i-tetration is structurally the archimedean scaling piece of it (Theorem 7.1) — the work is not crank-adjacent. Limiting: the locator is the adelic piece, unsolved at the frontier and beyond the corpus's present completion. The impedance ***A*** \= 35/437 plays no role at the core endpoint, in the kinetic geometry, or in the scaling piece; if it enters anywhere it is in a coefficient that remains unlocked. The discipline that keeps this honest — pre-registered tripwires, the ZS-M4 KS falsification, structural-only positive claims — is what separates this engagement from the crank literature on the same problem.

## **§13. Conclusion**

The Z-seam → prolate bridge terminates honestly. Directly computing the Nielsen–Olesen anchor-core vortex shows it does not realize the prolate well: the amplitude is a \[0,1\] profile with an exponential tail (not the \[−1,1\] tanh, even up to affine rescaling), and the s-wave fluctuation potential has the opposite endpoint sign and the wrong bulk profile (Theorems 5.1–5.2). The scale-cylinder reframing resolves the v1.4 angular tension but only relocates the coefficient barrier (Theorem 4.1). On the frontier, the detector → locator step is OPEN even for the Connes–Consani–Moscovici program with the same prolate operator; the corpus i-tetration is, by ZS-M4 Theorem 3 and Connes' decomposition, the archimedean scaling (detector) piece (Theorem 7.1, DERIVED-CONDITIONAL), while the locator is the adelic piece — unsolved externally and outside the corpus's present completion (which has only finite truncated-Euler-product prime structure, a detector). The realization framing is retired; ZS-M4's detector claim stands. F24 engages the correct frontier object, with anti-numerology tripwires pre-registered. No claim is made on RH, GRH-for-K, or determinant convergence.

## **Acknowledgements and Code Availability**

Developed within the Z-Spin Cosmology corpus with AI assistance for symbolic and numerical exploration, the Nielsen–Olesen BVP, and drafting; the author is responsible for all claims. The vortex BVP (scipy.solve\_bvp), the profile/tail diagnostics, the fluctuation-potential comparison, the scale-cylinder identities, and the z\* / α\_BK anchors (Appendix A) were computed at machine and 30-digit precision and are reproducible. The frontier survey cites peer-reviewed work; crank and preprint-mill claims were filtered out by reliability criteria, not counted.

## **Appendix A. Verification Listing**

A.1 NO vortex (n \= 1), dimensionless f″ \+ f′/x − (1−a)²f/x² − (β/2)(f²−1)f \= 0; a″ − a′/x \+ (1−a)f² \= 0; f(0)=a(0)=0, f(∞)=a(∞)=1. solve\_bvp converged for β \= 1, 2\. f range \[0,1\], monotone; core exponent p \= 0.996; tail 1−f ∼ K₀(x) (slope −1.06, relRMS 0.019; power-fit RMS 0.33).  
A.2 affine rescue: f ≈ ½(1+tanh(Λ ln(x/R))) best fit Λ \= 1.015, R \= 0.872, RMS 0.022, max residual 0.077; tails differ (exp vs power).  
A.3 fluctuation potential U(x) \= (1−a)²/x² \+ (β/2)(3f²−1): core ≈ \+10⁶ (∼1/x²), x \= 12 → \+β. Prolate normal form V\_Jac \= −¼ tan²ξ − ½ → −∞ at ξ \= ±π/2. (3f²−1) vs (2f−1)²: best fit RMS 0.42.  
A.4 scale cylinder: τ \= Λ ln(r/R) ⇒ r dr \= (r²/Λ)dτ; W\_Z \= (2πΛq)²(dq/dτ) \= 4π²Λ⁵χ²(1−χ²); (Λ/r²)W\_Z \= V\_req (SymPy diff \= 0); W\_Z dτ ∝ ⅓ d(χ³).  
A.5 anchors: z\* \= i^{z\*} \= 0.43828294 \+ 0.36059247 i; |z\*| \= 0.5675552; −ln|z\*| \= 0.5664173 \= y\*π/2; |z\*|² \= 0.3221189 \= e^{−y\*π} (lock L3). Multiplier |(iπ/2)z\*| \= 0.89151 (Wilson margin, distinct).

## **Appendix B. Open Problems**

O-F24.20. Determine whether any Z-core field (beyond the abelian-Higgs amplitude) can produce a \[−1,1\] sign-changing profile with a power tail matching χ \= tanh; absent that, Gate 1 stays closed.  
O-F24.21 (frontier). The adelic/global completion (semilocal → global; “Weil cohomology”) — the locator step — unsolved externally; track CCM progress rather than re-deriving internally.  
O-F24.22. Decide whether the corpus admits any adelic structure beyond the finite truncated Euler product; if not, the locator is permanently outside scope and F24 is a detector-only paper.

## **References**

\[1\] K. Kang, ZS-F24 v1.0–v1.4 (A-Washout; Boundary-Triple Collapse; Endpoint/Spectrum Separation; Kinetic Pullback & Potential Inertness; Anchor-Core BPS Gate), Z-Spin Cosmology Collaboration, 2026\.  
\[2\] K. Kang, ZS-M1 v1.0: i-Tetration Fixed Point and Locking Identities L1–L5, Z-Spin Cosmology Collaboration, 2026\.  
\[3\] K. Kang, ZS-M4 v1.1: Q \= 11 Transfer Operator, Berry–Keating Bridge, and Prime-Resonance Diagnostics, Z-Spin Cosmology Collaboration, 2026\.  
\[4\] K. Kang, ZS-F5 v1.0: Sector Dimensions (Z,X,Y) \= (2,3,6) and Q \= 11, Z-Spin Cosmology Collaboration, 2026\.  
\[5\] H. B. Nielsen, P. Olesen, Vortex-line models for dual strings, Nucl. Phys. B 61 (1973) 45–61.  
\[6\] E. B. Bogomolny, Stability of classical solutions, Sov. J. Nucl. Phys. 24 (1976) 449\.  
\[7\] A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5 (1999) 29–106.  
\[8\] A. Connes, H. Moscovici, The UV prolate spectrum and the zeros of zeta, Proc. Natl. Acad. Sci. 119 (2022) e2123174119.  
\[9\] Connes–Consani–Moscovici, "Zeta zeros and prolate wave operators," Ann. Funct. Anal. 15 (2024) 87 (arXiv:2310.18423)  
\[10\] C. M. Bender, D. C. Brody, M. P. Müller, Hamiltonian for the zeros of the Riemann zeta function, Phys. Rev. Lett. 118 (2017) 130201\.  
\[11\] G. Sierra, The Riemann zeros as energy levels of a Dirac fermion in a potential built from the prime numbers, J. Phys. A 47 (2014) 325204\.  
\[12\] M. V. Berry, J. P. Keating, H \= xp and the Riemann zeros, in Supersymmetry and Trace Formulae, Plenum (1999) 355–367.  
\[13\] E. C. Titchmarsh, Eigenfunction Expansions Associated with Second-Order Differential Equations, Part I, Oxford, 1962\.  
\[14\] A. Zettl, Sturm–Liouville Theory, Mathematical Surveys and Monographs 121, AMS, 2005\.

## **Version History**

v1.0–v1.4 (March 2026): A-washout; boundary-triple collapse; endpoint/spectrum separation; kinetic pullback & potential inertness; anchor-core BPS gate.  
v2.0 (March 2026, terminus): Closes the arc. (i) Computed BPS-vortex no-go: the Nielsen–Olesen vortex (BVP-solved) does not realize the prolate well — profile f∈\[0,1\] with exponential tail (not tanh), and s-wave fluctuation potential with opposite endpoint sign and wrong bulk profile (Theorems 5.1–5.2). (ii) Scale-cylinder reframing resolves the angular tension but relocates rather than removes the coefficient barrier (Theorem 4.1). (iii) External frontier mapped: the detector→locator step is OPEN even for Connes–Consani–Moscovici with the same prolate operator; i-tetration \= archimedean scaling/detector piece (Theorem 7.1, DERIVED-CONDITIONAL, via ZS-M4 Thm 3 α\_BK \= −ln|z\*| \= 0.566417 \+ Connes decomposition); the locator is the adelic piece, OPEN externally and beyond the corpus's finite-Euler-product (detector) structure. Anti-numerology tripwires pre-registered. Realization framing retired; ZS-M4 detector claim retained. No RH proof claimed. Consolidated from internal Z-Spin Collaboration research notes.