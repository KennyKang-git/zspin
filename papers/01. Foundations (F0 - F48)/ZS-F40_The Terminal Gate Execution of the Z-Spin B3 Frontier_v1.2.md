**ZS-F40**  
**The Terminal Gate Execution of the Z-Spin B3 Frontier**

*Physical Clock Discharge, the √2 Register-Clock Refusal, the OPS Global Exclusion of the Scalar Torus-Determinant Class, the θ₁ Graded-Route Exclusion, the Zero-to-Susceptibility Boundary Principle, and the χ₋ Five-Route Closure Audit*

**Author:** Kenny Kang (Z-Spin Collaboration)  
**Date:** March 2026  
**Theme / Code:** Foundations / ZS-F40  
**Lineage:** Executes the two finite gates pre-registered in ZS-F39 v1.1 Appendix C (physical ε\_C\_int) and Appendix D (proof-carrying C\_UV). Absorbs the ZS-F39.1 deliverable per the collaboration decision of record; v1.1 additionally absorbed and retired the graded-1PI mandate (formerly ZS-F41). v1.2 adds the Zero-to-Susceptibility Boundary Principle and the χ₋ five-route closure audit. Consumes ZS-F39 v1.1, ZS-F38 v1.1, ZS-A32 v1.1, ZS-A31 v1.5, ZS-F36 v2.1, ZS-F35 v1.5, ZS-F34 v1.8, ZS-F33 v1.8, ZS-F32 v1.5, ZS-F31 v1.4, ZS-A30 v2.1, ZS-A24 v2.1, ZS-S4, ZS-M46 v1.4, ZS-M47 v2.0.  
**Version:** 1.2

**Verification:** 48/48 exact/numerical checks PASS \+ 9/9 guards (zs\_f40\_verify\_v1\_2.py; SymPy exact rational linear algebra \+ mpmath 60-digit locked dynamics \+ a certified Banach enclosure of z\* \+ NumPy seed-11 null reproduction \+ the SL(2,ℤ)-reduced Dedekind-η torus determinant \+ Jacobi θ-function identities and derivatives \+ the pre-registered graded-ratio anti-numerology Monte Carlo \+ the χ₋ five-route closure audit). v1.1 baseline 39/39 \+ 7/7 reproduced byte-identical; v1.2 adds Blocks G (boundary principle \+ χ₋ audit) and H (status split \+ Yang–Mills/Higgs analogy). **Zero fitted parameters.** One disclosed external ΛCDM package (firewalled): Planck 2018 H₀ \= 67.36 ± 0.54, SH0ES H₀ \= 73, the ZS-A32 target C\_UV \= 1.244, the observed effective scale M\_eff/M̄\_P \= 1.018×10⁻³⁰. Firewalled observations are reported separately and are NOT counted as PASS evidence.  
Sole geometric inputs: **A** \= 35/437,  **Q** \= 11,  (Z, X, Y) \= (2, 3, 6),  dim **Z** \= 2\.  LOCKED.

# **§0. Abstract**

ZS-F38 and ZS-A32 left the ZS-A22 barrier **B3** — no action-level mechanism fixes the H₀/M̄\_P hierarchy — as a two-gate debt {(H-CLK) physical discharge, C\_UV full parent 1PI}, and ZS-F39 v1.1 uniformized the first gate to a single finite computation and pre-registered the second as a proof-carrying certificate (Appendices C, D). *This paper executes both finite gates and records the terminal verdict.*  
**Gate I (physical clock discharge).** Under the frozen ZS-F39 Appendix C rule we compute ε\_C\_int^(phys) \= ‖Φ\_clk(P\_K) − P\_A‖\_F / ‖P\_A‖\_F on the corpus-locked ZS-F31 GKLS register clock and the ZS-A24 seam-channel core. We prove **Theorem F40.2 (the √2 Refusal):** because the register one-tick map is the zero-diagonal cyclic shift Π while every admissible canonical clock is a diagonal unitary, the Frobenius deviation is *exactly √2 — tier-independent, phase-independent, and identical at the Q \= 11 register tier and the 3-sector core tier.* The frozen criterion (ε\_phys \< 10⁻¹⁰ and P\_null ≤ 5%) therefore **fails by an exact algebraic margin, not a numerical near-miss**: √2 sits above the entire seed-11 null (min 1.0975, reproduced to four decimals). Gate I is CLOSED-NEGATIVE for the canonical-clock identification.  
**Gate II (parent 1PI C\_UV).** We fix the action-level formula C\_UV \= exp(−Γ\_1PI^ren) and, on the Koenigs torus E\* carrier that ZS-F33/F34 isolate, evaluate the scalar zeta-determinant block exactly by the Ray–Singer/Kronecker closed form det′Δ \= Imτ·|η(τ)|⁴. A structural lemma (the **Nome Identity**, proven) shows the E\* elliptic nome equals the Koenigs multiplier, q(τ\_K) \= λ\*, tying the determinant to the locked dynamics with no freedom. We then prove **Theorem F40.4 (the OPS Global Exclusion):** using the Osgood–Phillips–Sarnak theorem that the hexagonal modulus is the global maximum of det′Δ over the unit-area moduli space, every one of the seven registered determinant powers is *excluded from the A32 primary target window over the entire moduli space* — the binding case det′(hex)^(−1/4) \= 1.2948 exceeds the window supremum 1.2640 by 2.44%. The bare scalar-torus-determinant class cannot supply C\_UV ≈ 1.244; it is CLOSED-NEGATIVE.  
**The graded route and the boundary principle (v1.1–v1.2).** v1.0 left the strictly larger *graded* parent 1PI open and scoped a successor (ZS-F41). Deep exploration retired that mandate. **Theorem F40.6 (the θ₁ Exclusion):** the theta-zero identity θ₁(0∣τ\_K) \= 0 is **PROVEN** (an odd Jacobi constant; verified to 10⁻⁵³), so the seam-odd Dirac determinant vanishes; the identification of the Z-Spin seam-odd sector with the odd spin structure is **DERIVED-CONDITIONAL** on the ZS-F36/F34/F23 seam-spin correspondence, and under that identification the bare graded-determinant route is CLOSED-NEGATIVE. v1.2 sharpens this into **Theorem F40.8 (Zero-to-Susceptibility):** at the determinant zero the *first* response survives, θ₁′(0∣τ\_K) \= 2η(τ\_K)³ \= 14.1465 ≠ 0 (a Quillen determinant-line section, PROVEN-imported), so the surviving B3 observable is not a determinant but a *susceptibility* χ₋ — the object ZS-F32 already reduced the frontier to. The vanishing determinant is not absence; it redirects the observable to a second response. A pre-registered anti-numerology Monte Carlo (28-reading graded-ratio universe, look-elsewhere → 100%) confirms no θ-ratio is evidence.  
**Terminal verdict and the χ₋ five-route audit (v1.2).** All three determinant/clock routes to the B3 *mechanism* close negatively — the canonical clock (√2), the scalar torus determinant (OPS), and the graded determinant (θ₁ \= 0). v1.2 then audits the *absolute value* of χ₋ and finds it reduces to the same objects: χ₋ \= (1260/4807)·C\_norm·M\_UV⁴ (the structural factor 1260/4807 \= 36**A**/**Q** is PROVEN), and every corpus route to M\_UV closes — the spectral lattice (8.190 ∉ ℒ), Branch A (√90 underivable), Branch B (tautological), the modular depth e^(−2πQ) (which needs the very clock this paper closed), and the C\_UV determinant (excluded here) — with the Charge-Unit Obstruction PROVEN-irreducible. Per the ZS-F39 discipline, **ZS-F40 records the B3 determinant/clock mechanism programme as TERMINAL**; the χ₋ absolute value is a **GENUINE OPEN, confirmed unclosable under current corpus tools** (reopenable only by a new axiom-level input, ZS-F32 gate B3-1). ZS-F41 (graded-determinant) is void. This is not a derivation of the absolute scale from **A**, **Q** — the A25/A27/A28 no-go stands; the ZS-A32 statistical leg (p\_single \= 0.50%) survives, firewalled; the vacuum fraction Ω\_Λ \= 83/121 (ZS-A30) is a separate, already-closed face of B3. What F40 fixes is the *category* of the B3-scale problem — a susceptibility, not a determinant. Verification 48/48 PASS \+ 9/9 guards; zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

# **Epistemic Status Legend**

| *The tags used in this paper, in the corpus-standard sense:* PROVEN  — Explicit proof or exact verification; no undischarged assumption. DERIVED  — Follows from PROVEN / IMPORTED-PROVEN results by stated steps; no new parameter. DERIVED-CONDITIONAL  — Derived modulo explicitly named, falsifiable conditions (e.g. KH1–KH4, parent injectivity, graded field content). IMPORTED-PROVEN  — Proven in the external literature and used without re-proof; cited. CLOSED-NEGATIVE  — A route proven not to work under its pre-registered rule; possibly scope-limited. OPEN  — A genuine, well-posed gap; may carry a finite-decision reduction. OPEN-TERMINAL  — A route left open with the standing rule that no successor paper is opened until a named object is supplied. OBSERVATION  — A firewalled numerical coincidence; explicitly NOT counted as evidence. NON-CLAIM  — Explicitly outside this paper’s scope (deferred to a named successor). |
| :---- |

# 

# **§1. Introduction: the two remaining gates and the terminal mandate**

The Z-Spin corpus locates the absolute cosmological hierarchy behind a single named barrier, **B3**: no action-level mechanism within local, stationary dynamics fixes the ratio of the metric/Kähler scale to the reduced Planck scale (ZS-A22; the capstone no-go ZS-A25; the dimensional no-go ZS-A27; the projector-valued top form ZS-A28). Across ZS-F31 through ZS-F39 the corpus did not remove that barrier — it *compressed* it. ZS-F38 named the register-clock identity (H-CLK) as the keystone and reduced the debt to two items; ZS-A32 executed the pre-registered anti-numerology Monte Carlo, closing the statistical leg at p\_single \= 0.50% while leaving the mechanism open; and ZS-F39 uniformized the first mechanism gate to a single finite computation and pre-registered the second as a proof-carrying certificate.  
At the close of ZS-F39 v1.1 the ledger read exactly two finite gates. **Gate I** is the physical clock gate: execute ε\_C\_int^(phys) under the frozen Appendix C rule on the ZS-F31 GKLS register clock and the ZS-A24 seam-channel core, discharging (H-CLK) ∧ (H-Σ₂) iff ε\_phys \< 10⁻¹⁰ and the frozen seed-11 null returns P\_null ≤ 5%. **Gate II** is the parent 1PI gate: compute the full C\_UV factor with a certificate (Appendix D), the target being the ZS-A32 cross-corner value C\_UV \= 1.244 within the a-priori band \[1/4, 4\]. ZS-F39 was explicit that these are the *only* remaining steps, and equally explicit that **only a certificate closes** — “an AI finding a minimum is not a closure criterion; only a certificate is” (NC-F39.5).  
ZS-F39 also fixed the terminal discipline this paper obeys: *“if either finite gate fails under its pre-registered rule, the paper closes the F31–F39 programme negatively rather than propagating another successor paper.”* A negative verdict, reached honestly under a frozen rule, is a terminus — not a failure to be escaped by a successor. This paper is written to be a **terminal** paper in exactly that sense: it executes both gates, and it closes.  
The result of the execution is unambiguous and, in both gates, *algebraic rather than numerical*. Gate I fails because the two objects being compared are structurally orthogonal: the register one-tick map is a permutation (a zero-diagonal cyclic shift) while every admissible canonical clock is a diagonal phase — their normalized Frobenius deviation is exactly √2, at every tier, for every choice of phases. Gate II fails because the bare scalar zeta-determinant on the Koenigs torus is bounded above, over the *entire* moduli space, by its hexagonal maximum (Osgood–Phillips–Sarnak), and that bound already excludes every registered determinant power from the target window. Neither failure is a near-miss to be tuned away; each is a proven exclusion. That is what makes this paper terminal.  
**What this paper does not claim.** It does not derive the absolute scale from **A** and **Q** (the A25/A27/A28 no-go stands; the ZS-M46 Buckingham-π guard F-M46.7 is respected). It does not reopen the ZS-A32 statistical leg, which is firewalled and survives any mechanism verdict. And it does not claim to have computed the odd topological susceptibility χ₋: the three objects closed here are the canonical-clock identification, the scalar-torus-determinant class, and — new in v1.1 — the graded-determinant class, all three being *determinant/clock* routes. χ₋, the object C\_UV actually reduces to, is proven irreducible under flux integrality and remains OPEN-TERMINAL: reopenable only by a new axiom-level input, never by a re-choice within the closed routes. Because ZS-F32 already reduced the odd sector to χ₋, and ZS-F33 already isolated its Charge-Unit Obstruction, no successor paper is needed to state this terminus — it is stated here (§6), and ZS-F41 is retired.

# 

# **§2. Locked inputs, the representation-fixing rule, and the non-expansion rule**

All theorem-side constants are fixed here, above the single firewalled observation block (§11), reproducing the ZS-F36/A31/A32 declared-before-loaded discipline.

## 

## **§2.1 Locked geometric and dynamical inputs**

**A** \= 35/437 (geometric impedance, ZS-F2, LOCKED); **Q** \= 11; (Z, X, Y) \= (2, 3, 6); dim **Z** \= 2; Σd² \= 4 \+ 9 \+ 36 \= 49; κ² \= **A**/**Q** \= 35/4807 (PROVEN, ZS-A19/M6). The i-tetration fixed point z\* \= i^{z\*} \= exp(iπz\*/2) and its multiplier fix the locked dynamical digits  
*z\* \= 0.4382829367 \+ 0.3605924719 i,   λ\* \= f′(z\*),   μ \= −ln|λ\*| \= 0.1148346250,   θ \= argλ\* \= 2.2592495540,*  
re-verified in-suite to fifty digits (checks A1–A4). **A certified Banach enclosure** of z\* is provided (check A5): the map is a contraction on a neighbourhood of z\* with |λ\*| \= 0.89151 \< 1, and the interval-Newton residual gives a certified enclosure radius below 10⁻⁴⁰, so every quantity built from z\* (μ, θ, the Koenigs modulus, the torus determinant) inherits a rigorous error bound. This is the corpus instance of the certified-computation methodology of Tucker and of Hales \[10, 11\]: a numerical evaluation that carries its own proof of correctness.

## 

## **§2.2 The representation-fixing rule (Gate I)**

ZS-F39 Appendix C specifies the input data (the ZS-F31 GKLS register generator and the ZS-A24 seam-channel core) but does not, by itself, fix the Hilbert-space representation in which the Frobenius norm ‖Φ\_clk(P\_K) − P\_A‖\_F is evaluated — F31 is stated at the 121-face level, A24 at the 3-sector / M₁₁ level, and the frozen null at the **Q** \= 11 register-clock level. To remove the last residual freedom before any evaluation, we freeze the rule:

| Representation-fixing rule (frozen, §2.2). The Gate I statistic is evaluated at the *register tier*: P\_K is the register one-tick map — the canonical Q \= 11 cyclic shift Π fixed by ZS-M46.3A (u∘f \= u+1) and ZS-F38.T2 (inner-function divisibility z^k ↔ z^k H²); P\_A is the canonical clock unitary against which the frozen seed-11 null was scored. The Frobenius norm is taken in M₁₁(ℂ). Tier-independence is then *proven* (Theorem F40.2, checks B5–B6): the same value √2 is obtained at the 3-sector tier, so the rule is not a hidden choice. |
| :---- |

## 

## **§2.3 The non-expansion rule**

No new constant, observation, tolerance, or admissible-space parameter may be introduced past this section. Explicitly forbidden (audited in check D3): any new scale parameter; any modification **Q** → **Q** \+ α; absorbing C\_UV into **Q** (the ZS-A31 discipline); penalty-weight tuning of the admissible space; post-hoc widening of the target window; and treating an AI-found minimum, or any firewalled observation, as evidence. Allowed: the locked inputs above, the mathematical constants π and e, and — as a single disclosed, firewalled external package — the ZS-A32 ΛCDM inputs (Planck H₀ \= 67.36 ± 0.54, SH0ES H₀ \= 73, the target C\_UV \= 1.244).

# 

# **§3. Gate I: Physical Clock Discharge and the √2 Refusal**

This section absorbs the ZS-F39.1 deliverable (execute ε\_C\_int^(phys) under the frozen rule) into ZS-F40, per the collaboration decision of record — the same mechanism by which ZS-F39 absorbed the pre-scoped ZS-M48 deliverables. No frozen registration of ZS-F39 is altered; §3 executes the byte-identical Appendix C rule.

## 

## **§3.1 The model tier reproduced (ε\_C\_int^(model) \= 0\)**

On the ZS-F38.T2 Hardy chain the register shift and the seam modular step are the same map: z·(z^k) \= z^{k+1} exactly for all k ≤ **Q** (check B1). The branch-free Abel increment equals 1 at the Koenigs orbit points (ZS-A32/F39 CI1–CI2), and the helical normal form of ZS-M46 §5 gives, exactly and symbolically, w ↦ w \+ logλ\* ⇒ (x ↦ x+1, η ↦ η) (check B2). Hence **ε\_C\_int^(model) \= 0, identically** — not small, zero, because in the canonical model the clock identity holds by construction. The model tier sharpens the physical target: any physical computation returning ε ≠ 0 falsifies the clock identity itself, not a calibration (ZS-A32 §5 wording, inherited).

## 

## **§3.2 Theorem F40.2 — the √2 Refusal**

| Theorem F40.2 (Physical Clock Discharge — the √2 Refusal). Let Π ∈ M\_Q(ℂ) be the register one-tick map (the zero-diagonal cyclic shift, Π\_{k+1,k} \= 1). Let P\_A \= U be any canonical register clock in the admissible class, i.e. any diagonal unitary U \= diag(e^{iφ₀}, …, e^{iφ\_{Q−1}}). Then for every choice of phases, *ε\_C\_int^(phys) \= ‖Π − U‖\_F / ‖U‖\_F \= √2 ,   exactly and independently of Q and of the phases.* Consequently the frozen Appendix C criterion (ε\_phys \< 10⁻¹⁰) fails by an exact algebraic margin. \[PROVEN; checks B4–B6\] |
| ----- |

**Proof.** Write ‖Π − U‖\_F² \= tr\[(Π − U)†(Π − U)\] \= tr(Π†Π) \+ tr(U†U) − 2 Re tr(U†Π). Both Π and U are unitary, so tr(Π†Π) \= tr(U†U) \= **Q**. The cross term vanishes: U†Π has the same zero-diagonal support as Π (a diagonal unitary cannot populate the diagonal of a zero-diagonal matrix), so tr(U†Π) \= 0 for every diagonal U (check B4, symbolic over free phases φ₀…φ\_{Q−1}). Hence ‖Π − U‖\_F² \= 2**Q**, ‖U‖\_F² \= **Q**, and ε \= √(2**Q**/**Q**) \= √2. The value carries no **Q**\-dependence and no phase-dependence. Evaluated at the 3-sector core tier (Π₃ the 3-cycle, U₃ diagonal) the identical computation gives √2 (check B6), so the value is tier-independent and the representation-fixing rule of §2.2 introduces no freedom.   
**Interpretation.** The refusal is structural, and it is exactly the distinction the corpus ontology predicts. The register one-tick map is a *permutation of slots* — it moves the “point of time / point of space” from one register slot to the next, carrying no diagonal weight. A canonical clock unitary is *diagonal* — it phases each slot in place. A permutation with empty diagonal and a diagonal phase are Frobenius-orthogonal up to their common norm; their normalized distance is the maximal √2. The clock identity (H-CLK), read as “the seam one-tick map *is* the canonical diagonal clock,” is therefore not merely unmet — it is refused by an orthogonality that no admissible phase choice can repair. This is the physical-tier content that ZS-F39 left OPEN-PROTOCOLIZED, now executed.

## 

## **§3.3 The frozen null, reproduced, and the certified verdict**

The seed-11 frozen null of ZS-F39 §8.2 (2000 unital pair-Kraus channels Φ(ρ) \= ½(V₁ρV₁† \+ V₂ρV₂†), V₁, V₂ Haar) is reproduced in-suite to four decimals: **min ε \= 1.0975, p5 \= 1.1585, median \= 1.2223** (check B8, matching the frozen values of record). The observed ε\_phys \= √2 \= 1.41421 lies *above the entire null ensemble*, so P\_null(ε ≤ √2) \= 100% ≫ 5% (check B9): the second frozen criterion fails as decisively as the first. For completeness the protocol’s success branch is certified too: had ε\_phys fallen below the null minimum (0 of 2000 draws), the Clopper–Pearson exact one-sided 95% bound would be P\_null ≤ 1 − 0.05^{1/2000} \= 0.1497% \< 5% (check B12) — so the frozen rule is a genuine certificate on both branches, and the branch that fired is the failing one.  
Two structural checks confirm the objects are the corpus objects and not toy stand-ins. The equivariant slot lift coarse-grains *exactly* to the ZS-A24 sector generator, E·L\_slot \= L\_sec·E over the rationals (check B10, reproducing ZS-F39.T3/SEL), with the slot lift doubly stochastic so its stationary state is I\_Q/**Q** (check B10b); and the cyclic clock is genuinely *not* an inner symmetry of the dissipative core, \[Π, L\_slot\] ≠ 0 (check B11) — the very fact that makes the clock a nontrivial external identification rather than a symmetry of the generator, and hence the reason the √2 refusal is meaningful rather than vacuous.

| Gate I verdict. Under the frozen ZS-F39 Appendix C rule, ε\_C\_int^(phys) \= √2 (Theorem F40.2) and P\_null \= 100%. Both criteria fail. (H-CLK) ∧ (H-Σ₂) is CLOSED-NEGATIVE for the canonical-clock identification: the register one-tick map is not the canonical diagonal clock, by an exact orthogonality. The ZS-A32 statistical leg is untouched and survives, firewalled. |
| :---- |

# 

# **§4. Gate II-A: the parent 1PI formula and the Koenigs-torus determinant**

## 

## **§4.1 The action-level formula (fixed before evaluation)**

Per ZS-F39 Appendix D (F40.3), C\_UV is fixed at action level before any evaluation:  
*C\_UV \= exp(−Γ\_1PI^ren),   Γ\_1PI^ren \= ½ Σ\_i (−1)^{F\_i} m\_i log\_ζ det Δ\_i − Γ\_ct ,   log\_ζ det Δ\_i \= −ζ′\_{Δ\_i}(0).*  
Here the sum runs over the field content propagating on the ZS-F33/F34 vacuum carrier Y₆ \= M₄ × Σ₂ with the Koenigs torus E\* the rank-one internal cycle; (−1)^{F\_i} grades bosons and fermions; Γ\_ct is the counterterm, which is *not* free — it is constrained by KH1–KH4 admissibility, BRST/gauge invariance, seam parity, unital irreducibility, holonomy equivalence, the Gate I ε\_C\_int certificate, and the ZS-A31 no-Q-absorption / no post-hoc-fitting discipline. ZS-F36.T5 is explicit that at the register-tree (DBI) level Γ\_ct \= 0 holds but the *full parent 1PI is OPEN* because heavy parent fields may renormalize the F₄² coefficient. That OPEN full-1PI object is exactly what Gate II must confront.

## 

## **§4.2 The Nome Identity and the exact scalar-block determinant**

The internal cycle E\* is the Koenigs torus of ZS-F33/F34, with elliptic modulus τ\_K \= θ/2π \+ iμ/2π (the ZS-M46 elliptic height h\_K \= Imτ\_K). We record a structural identity that ties the determinant to the locked dynamics with no freedom.

| Lemma F40.L2 (the Nome Identity). The elliptic nome of the Koenigs torus equals the Koenigs multiplier: *q(τ\_K) \= e^{2π i τ\_K} \= λ\* ,   exactly.* Hence every modular quantity on E\* is a function of the locked dynamics alone, with no tunable modulus. \[PROVEN; check A6, agreement to 10⁻⁶¹\] |
| ----- |

**Proof.** τ\_K \= (θ \+ iμ)/2π \= (logλ\*)/(2πi) since logλ\* \= −μ \+ iθ. Thus 2πiτ\_K \= logλ\* and e^{2πiτ\_K} \= λ\*.  This is the modular-nome reading of the ZS-M46 identity e^{−2πh\_K} \= |λ\*|; the corpus’s i-tetration multiplier is literally the nome of its own vacuum torus.  
On a flat torus of modulus τ the scalar Laplacian zeta-determinant has the Ray–Singer closed form, made scale-invariant by fixing unit area (Osgood–Phillips–Sarnak):  
*det′Δ(τ)∣\_{unit area} \= Imτ · |η(τ)|⁴ ,   η the Dedekind eta.*  
We prove the convention is forced, not chosen: only the unit-area power is invariant under the modular group SL(2,ℤ), whereas the naive (Imτ)²|η|⁴ form is not (check C1: invariance defect \< 10⁻⁴⁵ for the unit-area form, versus a defect of 0.030 for the area form). Evaluated at τ\_K by SL(2,ℤ)-reduction to the fundamental domain and the η product (self-tested against η(i) \= Γ(¼)/(2π^{3/4}) to forty digits, check C0):  
*det′Δ(E\*, unit area) \= 0.24815300189…   \[PROVEN; check C2\]*

# 

# **§5. Gate II-B: the OPS Global Exclusion of the torus-determinant class**

The admissible space of determinant candidates that the corpus fixes without new input is discrete: the scalar block contributes det′Δ raised to one of the registered graded powers p ∈ {±1, ±½, ±¼, 2} (the mode-multiplicity readings that a scalar/spinor/ghost block on E\* can produce under the F36 template). We do not tune a continuous parameter; we ask whether *any* of these discrete readings can land in the target window — and we answer it **over the entire moduli space at once**, using a global theorem, so the answer cannot be evaded by re-choosing the modulus.

## 

## **§5.1 The target windows (declared before the exclusion is evaluated)**

From the disclosed ZS-A32 package (check C9): the target is C\_UV \= 1.244; the primary window propagates the Planck 1σ uncertainty with the A32 factor of 2, δ\_P \= 2 ln(67.90/67.36) \= 0.01597, giving the **primary window \[1.2243, 1.2640\]**; the extended window uses the SH0ES extreme δ\_S \= 2 ln(73/67.36) \= 0.16082 (the A32 value 0.161, rounded), giving **\[1.0592, 1.4610\]**. The a-priori outer band is \[1/4, 4\]. These are declared here, in script order, before §5.2 is evaluated.

## 

## **§5.2 Theorem F40.4 — the OPS Global Exclusion**

| Theorem F40.4 (OPS Global Exclusion of the scalar-torus C\_UV class). By Osgood–Phillips–Sarnak, det′Δ attains its global maximum over the unit-area moduli space at the hexagonal modulus τ \= e^{iπ/3}, with det′Δ(hex) \= 0.35575. Therefore for the binding negative power p \= −¼, *inf\_τ det′Δ(τ)^{−1/4} \= det′Δ(hex)^{−1/4} \= 1.29483 \> 1.26403 \= sup(primary window),* and all seven registered powers are excluded from the primary window over the entire moduli space. The bare scalar-torus-determinant class cannot supply C\_UV ≈ 1.244. \[DERIVED from IMPORTED-PROVEN (OPS) \+ PROVEN evaluation; checks C3–C5\] |
| ----- |

**Proof.** OPS proves the unit-area determinant det′Δ \= Imτ·|η(τ)|⁴ is a proper function on moduli space maximized uniquely at the hexagonal point, so its range is the interval (0, det′Δ(hex)\] with det′Δ(hex) \= 0.35575 (check C3, ordering hex \> square \> τ\_K verified). For a positive power p \> 0 the range of det′Δ^p is (0, det′Δ(hex)^p\]; for p \< 0 it is \[det′Δ(hex)^p, ∞). A power is excluded from the primary window \[w−, w₁\] iff its range supremum is below w− (for p \> 0\) or its range infimum is above w₁ (for p \< 0). Check C5 evaluates all seven: p \= 1 ⇒ sup 0.356 \< 1.224; p \= ½ ⇒ 0.596 \< 1.224; p \= ¼ ⇒ 0.772 \< 1.224; p \= 2 ⇒ 0.127 \< 1.224; and for the negative powers p \= −1 ⇒ inf 2.811 \> 1.264; p \= −½ ⇒ 1.677 \> 1.264; p \= −¼ ⇒ 1.295 \> 1.264. Every case excludes. The binding case is p \= −¼, closest to the window, and it still clears the supremum by 2.44%.   
**What this closes and what it does not.** The exclusion is proven for the bare *scalar* zeta-determinant class over *all* moduli, and it is honestly bounded: check C-G records that the same p \= −¼ class is *not* excluded from the SH0ES-extended window (det′Δ(hex)^{−1/4} \= 1.2948 \< 1.4610). The exclusion therefore closes the bare-scalar route against the *primary* target, not against every conceivable target; a graded 1PI with fermionic and ghost blocks changes the sign structure and the effective power, and is not covered by this theorem. That is precisely the residual carried to §8.

# 

# **§6. Gate II-C: the graded route, the θ₁ exclusion, and the Zero-to-Susceptibility boundary**

v1.0 left a strictly larger object open — the *graded* parent 1PI, with bosonic, fermionic, and BRST-ghost content over E\* — and scoped a successor paper (ZS-F41) to derive that content and compute a graded determinant. This section executes the deep exploration that retires the mandate. The graded-determinant route is closed by the same kind of structural fact that closed the scalar route in §5, and the object C\_UV actually reduces to is shown to be already-registered as irreducible.

## 

## **§6.1 The graded content already exists in the corpus**

The premise of the ZS-F41 mandate — that no corpus paper fixes the graded field content — is false at the level of the sign structure. ZS-S4 §6.7 proves the BRST supertrace identity STr(q⁴) \= 6 (gauge) − 12·8·(½)⁴ (fermion) \= 6 − 6 \= 0 exactly, with STr(q²) \= 6 − 24 \= −18 (check E4), and ZS-A30 proves the β-twisted physical trace W \= STr\_β satisfies W∘s \= 0 (a supertrace annihilates graded BRST commutators) with W(û\_seam) ≠ 0\. The graded grading (−1)^F and its physical-trace projection are corpus-fixed, not free. What a graded 1PI would need beyond this is the *odd-sector* field content on E\* — and that is exactly where the structural obstruction lives.

## 

## **§6.2 Theorem F40.6 — the θ₁ exclusion of the graded-determinant route**

| Theorem F40.6 (the θ₁ Exclusion, status-split). (a) \[PROVEN\] The Jacobi theta constant θ₁(0∣τ) \= 0 for every τ (an odd function of z at z \= 0); at τ\_K it is 1.4×10⁻⁵³. (b) \[DERIVED-CONDITIONAL\] The Koenigs torus E\* is parallelizable (w₁ \= w₂ \= 0; ZS-F36, F34), so it carries four spin structures, and the Z-Spin seam parity (the ZS-F23 ℤ₂ grading β) identifies the seam-odd sector with the *odd* spin structure — conditional on the ZS-F36/F34/F23 seam-spin correspondence. Under (a) ∧ (b), the seam-odd Dirac operator D₋ has a zero mode, det′ D₋ \= 0, and the bare graded-determinant route is CLOSED-NEGATIVE. The even spin structures give finite Dirac ratios |θ₂/η|, |θ₃/η|, |θ₄/η| (checks E1–E3, H1), so both sides of the boundary are checked. \[(a) PROVEN; (b) DERIVED-CONDITIONAL; checks E1–E3, E6, H1\] |
| :---- |

**Proof.** θ₁(z∣τ) is odd in z, so θ₁(0∣τ) \= 0 for every τ (a classical Jacobi identity); the numerical value at τ\_K is 1.4×10⁻⁵³, at the noise floor of the 60-digit evaluation. The four spin structures on the parallelizable E\* correspond to the four theta characteristics; the seam-parity-odd structure is the one with the vanishing constant, i.e. θ₁. The η-function block and the three *even* Dirac ratios |θ₂/η|, |θ₃/η|, |θ₄/η| are finite and are computed (check E3), and the Jacobi identity θ₂θ₃θ₄ \= 2η³ is verified to 40 digits (check E1) as an internal consistency test; but the sector that carries the vacuum energy is the odd one, and there the determinant is zero.   
**Why this is the right reading, not an evasion.** This is exactly the object ZS-F32 already isolated. F32 proved the cosmological frontier reduces to a *single odd-sector susceptibility* χ₋ via ρ\_Λ,Z \= ½ χ₋ ω², precisely because the odd sector’s determinant vanishes and only its second-order response survives. The θ₁ \= 0 fact is the spin-geometry statement of that reduction. So the graded-determinant route is not merely hard — it targets an object (a determinant) that structurally does not exist for the sector in question. It is closed by the same logic as the scalar route in §5: a proven structural fact, not a numerical near-miss.

## 

## **§6.3 The anti-numerology Monte Carlo (graded-ratio universe)**

For completeness, and to defend against a tempting near-miss, we pre-register and execute an anti-numerology audit over the *even*\-spin Dirac ratios (the only graded determinant-like readings that exist). The blind universe is {|θ₂/η|, |θ₃/η|, |θ₄/η|, det′Δ\_scalar} raised to p ∈ {±1, ±½, ±¼, 2}, i.e. 28 readings; the tolerance is |Δ ln C∣ ≤ ¼ ln 4 \= 0.3466 on the a-priori band \[1/4, 4\] (the ZS-A32/F38 universe). Checks F1–F3: **11 of 28 readings fall in-band**, the single-reading in-band chance is 25%, and the any-of-28 look-elsewhere probability is **100%**. The most target-proximate reading, |θ₂/η|^{1/2} \= 1.29480 (|Δ ln∣ \= 0.040, firewalled), is therefore ruled non-evidential: the graded-ratio universe is dense near the target, so no ratio can be counted as evidence for C\_UV. This is the anti-numerology firewall enforced in-suite.

## 

## **§6.4 Theorem F40.8 — the Zero-to-Susceptibility Boundary Principle**

The vanishing determinant of §6.2 should not be read as the absence of a vacuum carrier. It says the *first-order multiplicative* observable — the bare determinant — is the wrong object at the seam-odd boundary. The correct observable is response-theoretic, and it survives.

| Theorem F40.8 (Zero-to-Susceptibility Boundary Principle). Let D₋ be the seam-odd Dirac operator on E\*. Under the F40.6(b) identification the seam-odd spin structure has a zero mode, det′ D₋ \= 0 (θ₁(0) \= 0). The first nonzero response is finite: *θ₁′(0 ∣ τ\_K) \= 2η(τ\_K)³ \= 14.14653 ≠ 0 ,* the Quillen determinant-line section that survives the zero. Therefore the finite B3-relevant quantity is not the bare determinant but the renormalized second response — the odd susceptibility χ₋ \= −∂²\_J log Z₋(J)∣₀ after zero-mode projection, with Z₋(J) \= det′(D₋ \+ J·O₋). The determinant zero forces the correct observable to be a susceptibility. \[(a) θ₁′ \= 2η³ PROVEN \+ IMPORTED-PROVEN (Quillen, BGS); (b) DERIVED-CONDITIONAL on F40.6(b); check G1\] |
| ----- |

**Why this is a re-reading, not new physics.** χ₋ is exactly the object ZS-F32 isolated: the cosmological frontier reduces to a single odd-sector susceptibility via ρ\_Λ,Z \= ½ χ₋ ω², precisely because the odd determinant vanishes and only its second-order response survives. Theorem F40.8 is the spin-geometry statement of that reduction: the “nothing” of θ₁ \= 0 is the vanishing of a *first* observable, and the “something” is the *second* response χ₋. This fixes the **category** of the B3-scale problem — a susceptibility — without computing its value.

## 

## **§6.5 The χ₋ dependency chain (Theorem F40.7, importing ZS-F33/F35)**

| Theorem F40.7 (χ₋ chain and Charge-Unit Irreducibility). The odd susceptibility factorizes (ZS-F35 §8) as *χ₋ \= (dim Y)²·(A/Q)·C\_norm·M\_UV⁴ \= (1260/4807)·C\_norm·M\_UV⁴ ,* where the structural factor 1260/4807 \= 36 A/Q is PROVEN (exact rational; check G3), C\_norm \= G̃\_s⁻¹(c\_e/2π)² is the ZS-F36 gate (= 1 under the canonical UV normalization, OPEN at full 1PI), and M\_UV is PROVEN-irreducible by the ZS-F33 Charge-Unit Obstruction: flux integrality fixes the flux number but not the dimensionful unit χ₋ \= e₋²/(4π²Z₋) (check E5). \[structural factor PROVEN; irreducibility IMPORTED-PROVEN (ZS-F33.8); checks E5, G3, G3b\] |
| ----- |

# 

# **§7. The χ₋ absolute-value five-route closure audit**

Theorem F40.7 localizes the B3-scale to M\_UV. This section audits whether *any* corpus route can fix M\_UV (hence the χ₋ absolute value), and finds every one closed. The audit is bookkeeping, not a new computation: it collects the standing verdicts of ZS-F33, ZS-A31, and this paper into one ledger, so the terminus is auditable.  
**The clock connection (new in v1.2).** The only Borchers–Wiesbrock-forced corpus candidate for M\_UV \= M\_K is the modular depth M\_K/M̄\_P \= e^(−2πQ) (ZS-A31/A32), and by ZS-F38.T3 that mechanism requires the register clock (H-CLK) to be discharged. But **Gate I of this paper closed (H-CLK) negatively** (ε \= √2). Numerically e^(−2πQ) \= 9.632×10⁻³¹, and the firewalled observed ratio M\_eff/M̄\_P \= 1.018×10⁻³⁰ infers C\_UV \= 1.2477 — the *same* C\_UV the scalar-torus route excluded in §5 (check G4, guard G4-G). So the modular-depth route and the C\_UV determinant route are not independent escapes; both are the objects F40 already closed.  
Table 7.1 — The χ₋ absolute-value five-route audit. Every corpus route to M\_UV is closed.

| Route | Attempt | Verdict |
| :---- | :---- | :---- |
| R1 spectral | C\_odd^sp from the seam-odd determinant lattice (ZS-F33 v1.2) | CLOSED-NEGATIVE: 8.190 ∉ ℒ \= ℤ≥₀ ln2 ⊕ ℤ≥₀ ln3 |
| R2 Branch A | ρ\_Λ \= ½χ₋ω² with E\* \= v (electroweak benchmark) | CLOSED-NEGATIVE: 90× short; √90 \= 9.49 underivable from (A, Q) |
| R3 Branch B | ρ\_Λ \= M̄\_P⁴ e^(−ν\_now), ν\_now \= 276.6 (ZS-A26) | TAUTOLOGICAL: ν\_now is defined by ρ\_obs |
| R4 modular depth | M\_K/M̄\_P \= e^(−2πQ), 2π Borchers–Wiesbrock-forced (ZS-A31) | **CLOSED-NEGATIVE via Gate I: needs (H-CLK); ε \= √2 (Thm F40.2)** |
| R5 determinant | scalar / graded C\_UV parent 1PI on E\* | **CLOSED-NEGATIVE via Gate II: OPS (Thm F40.4) \+ θ₁ \= 0 (Thm F40.6)** |
| backstop | Charge-Unit Obstruction (ZS-F33.8): flux integrality vs unit | PROVEN-irreducible: (A,Q)+integrality fix flux number, not e₋² |

**Verdict.** All five routes to M\_UV are CLOSED-NEGATIVE or tautological, and the Charge-Unit Obstruction is the PROVEN-irreducible backstop. Therefore the **χ₋ absolute value is a genuine OPEN, confirmed unclosable under the current corpus tools**. An anti-numerology backstop confirms no (A, Q)-clean value candidate: the depth exponent is not an integer telomere rung (n \= 2πQ**A** \= 5.536, non-integer; check G6), and e^(−2πQ) is Borchers–Wiesbrock-structural, not a fitted number. This is the protocol’s “converged, all nodes OPEN → real OPEN” outcome: the result is the confirmation that B3-scale cannot be closed now, together with the precise datum (the odd charge unit e₋²) whose future derivation — ZS-F32 gate B3-1 — would close it.

# 

# **§8. Candidate search: the non-evidential optimizer and the recorded dead-end**

Per NC-F39.5, an optimizer proposes candidates only; it never closes. We record the target-blind search and its outcome as an appendix-level, non-evidential artifact, and we register one dead-end explicitly so it is not silently dropped.  
**Target-blind selection.** The admissible reading is selected by a lexicographic order that never uses 1.244: LexMin(constraint violation, gauge redundancy, BRST anomaly, heat-kernel tail, scheme complexity). The scalar block is fixed by this order to the unit-area Ray–Singer determinant with the modulus locked to τ\_K by the Nome Identity — no target enters. Only *after* the modulus and convention are fixed is det′Δ(τ\_K) computed and compared, and the comparison is the exclusion of §5, not a fit.  
**Recorded dead-end (CLOSED-NEGATIVE, this sub-route).** The most target-proximate single reading, det′Δ(τ\_K)^{−1/4} \= 1.41684, misses the primary window (it lands only in the SH0ES-extended window; §11, firewalled) and, by §5, no power of the bare scalar determinant reaches the primary window at any modulus. The bare-scalar route is therefore recorded as a closed dead-end, exactly as ZS-F31 recorded its retracted F14-monodromy route and ZS-A24 recorded its retracted 1/κ² instanton reading. Recording it disciplines the successor: any future C\_UV route must be genuinely graded, not a re-choice of scalar power or modulus.  
**Look-elsewhere audit.** The candidate universe of this search — 7 powers × 2 determinant conventions \= 14 readings — has a log-uniform chance, on the a-priori band \[1/4, 4\], of a single reading landing in the SH0ES-extended window of 11.6%, and of any of the 14 landing of 82.2% (check C8). The single firewalled proximity of §11 is therefore fully accounted for by look-elsewhere and carries no evidential weight — the anti-numerology conclusion, enforced in-suite.

# 

# **§9. The certificate structure**

The The three determinant/clock closures and the boundary audit are certificate-carrying in the ZS-F39 Appendix D sense, and we state which certificate class each uses.  
**Gate I certificate (exact algebraic).** Theorem F40.2 is an exact symbolic identity: ε \= √2 with a machine-checked proof that tr(U†Π) \= 0 over free phases (check B4) and that the value is tier-independent (B5–B6). No interval arithmetic is needed because the result is exact; the null side is sealed by the reproduced frozen ensemble (B8) and the Clopper–Pearson exact bound (B12). This is certificate class (c) of Appendix D — KKT-free, because the object is an exact distance, not an optimization.  
**Gate II certificate (global exclusion \+ structural exclusion).** Theorem F40.4 (scalar route) is a global lower/upper-bound certificate of exactly the kind Appendix D class (a)/(d) demands: the OPS theorem supplies a rigorous global bound on det′Δ over the whole moduli space (not a local minimum), and the fifty-digit η-evaluation is certified by the Banach enclosure of z\* (A5) and the η self-test (C0). Theorem F40.6 (graded route) is a structural exclusion: θ₁(0∣τ\_K) \= 0 is an exact Jacobi identity, so the graded determinant is identically zero and there is nothing to certify — a zero is its own certificate. Theorem F40.7 (χ₋) is an imported PROVEN no-go. Because all three are global or exact, none can be evaded by re-choosing a modulus, power, or field reading — the precise property Appendix D required of a closing certificate.  
**Why an AI minimum would not have sufficed.** Had we merely minimized J(Θ) \= |log C\_UV(Θ) − log 1.244|² and found a small value, ZS-F39 NC-F39.5 would reject it as evidence. What closes here is the opposite: not that a candidate *reaches* the target, but that a global theorem *proves no admissible candidate in the closed class can*. A negative certificate is still a certificate.

# 

# **§10. The terminal theorem and the closure ledger**

| Theorem F40.5 (Terminal Verdict on the B3 mechanism programme). Under the pre-registered ZS-F39 rules, all three determinant/clock routes to the B3 *mechanism* close negatively: (I) the canonical clock — ε \= √2 (Thm F40.2); (II-B) the scalar torus determinant — OPS-excluded over all moduli (Thm F40.4); (II-C) the graded determinant — θ₁(0∣τ\_K) \= 0 (Thm F40.6). The Zero-to-Susceptibility Principle (Thm F40.8) identifies the surviving object as the odd susceptibility χ₋, and the five-route audit (§7) shows every corpus route to its absolute value (M\_UV) is CLOSED-NEGATIVE or tautological, with the Charge-Unit Obstruction PROVEN-irreducible. Therefore the B3 determinant/clock mechanism programme is TERMINAL, and the χ₋ absolute value is a GENUINE OPEN, confirmed unclosable under current corpus tools — reopenable only by a new axiom-level input (an odd gauge group and charge lattice from the axioms, ZS-F32 gate B3-1). ZS-F41 (graded-determinant) is void. The ZS-A32 statistical leg (p\_single \= 0.50%) is firewalled and survives; the vacuum fraction Ω\_Λ \= 83/121 (ZS-A30) is a separate, already-closed face of B3. \[DERIVED; checks B4–B12, C1–C9, E1–E6, F1–F3, G1–G6, H1–H2, D1–D3\] |
| :---- |

Table 10.1 — The terminal closure ledger. F39 status → F40 v1.2 execution.

| Gate | ZS-F39 v1.1 status | ZS-F40 v1.2 execution |
| :---- | :---- | :---- |
| physical ε\_C\_int (H-CLK)∧(H-Σ₂) | OPEN-PROTOCOLIZED | CLOSED-NEGATIVE: ε \= √2 exactly (Thm F40.2); P\_null \= 100% |
| C\_UV (scalar-torus class) | OPEN — untouched | CLOSED-NEGATIVE: OPS global exclusion from primary window over ALL moduli (Thm F40.4) |
| C\_UV (graded-determinant class) | OPEN (v1.0: scoped to ZS-F41) | CLOSED-NEGATIVE: wrong object — θ₁(0∣τ\_K) \= 0, odd spin structure has a zero mode (Thm F40.6) |
| χ₋ absolute value (odd susceptibility) | OPEN (F32/F33/F35 residual) | GENUINE OPEN: five-route audit (§7) closes every route to M\_UV; Charge-Unit Obstruction PROVEN-irreducible; reopenable only by ZS-F32 B3-1 |
| ZS-F41 (graded-det mandate) | pre-registered (v1.0 App. D) | **VOID — retired; no new paper opened** |
| B3 (mechanism programme) | NOT CLOSED; two finite gates | **TERMINAL: all three determinant/clock routes CLOSED-NEGATIVE; category \= susceptibility (Thm F40.8)** |
| B3 (statistics / fraction) | CLOSED / DERIVED-COND | UNCHANGED, firewalled (p \= 0.50%); Ω\_Λ \= 83/121 separate |

**Positioning (of record).** ZS-F40 is a terminal paper. It does not add a mechanism; it *removes* three candidate mechanisms by proof, and identifies the *category* of the surviving object. The corpus pattern holds — internal iteration converges to honesty, not to closure — but here honesty takes its sharpest form: a pre-registered negative verdict on the determinant/clock programme, together with a positive identification of what B3-scale *is* (a susceptibility) and what single datum would close it (the odd charge unit e₋²).

| Box: relation to the mass-gap and Higgs-VEV patterns (analogy, NON-CLAIM). B3-scale has the same logical shape as a boundary-generation problem — a naive zero object is not the final observable — but the target differs in each case: • Yang–Mills: a classically massless gauge field is expected to acquire a positive quantum spectral gap Δ \> 0 (target: positivity). • Higgs: a symmetric zero configuration gives way to a nonzero vacuum expectation value v (target: vacuum selection). • ZS-F40: the odd-spin determinant vanishes (θ₁ \= 0\) and the surviving B3 carrier is the second response χ₋ (target: the odd charge unit). F40 does not compute that unit, and makes no claim that B3 is “solved like” the mass gap; it fixes the category of the problem. This box is an analogy of logical shape only. \[NON-CLAIM; check H2\] |
| :---- |

# 

# **§11. Firewalled observations (single block; NON-EVIDENCE)**

Two numerical coincidences are recorded here, once, behind the firewall. By the non-expansion rule they are **not** counted as PASS evidence anywhere in this paper (guard D-G1), and the look-elsewhere audit of §6 accounts for them fully.  
**Observation O1 (band-edge proximity).** det′Δ(E\*, unit area) \= 0.24815 differs from the lower band edge 1/4 by 0.74%; equivalently det′Δ(τ\_K)^{−1/4} \= 1.41684 differs from √2 by 0.19%. **\[OBSERVATION, firewalled; check C6\]**  
**Observation O2 (extended-window landing).** det′Δ(τ\_K)^{−1/4} \= 1.41684 lands inside the SH0ES-extended window \[1.0592, 1.4610\] while lying outside the primary window — the numerical shadow of a route the primary-window theorem F40.4 excludes. **\[OBSERVATION, firewalled; check C7\]**  
These are the information-capacity face of the same vacuum corner; no claim is registered. The disclosed ΛCDM package (Planck 2018 \[14\]; SH0ES) enters only here.

# 

# **§12. Falsification gates**

**F-F40.1 (mathematical, immediate).** If tr(U†Π) ≠ 0 for some diagonal unitary U, or if ‖Π − U‖\_F/‖U‖\_F ≠ √2, Theorem F40.2 is false and the Gate I verdict reverts to OPEN-PROTOCOLIZED. (Excluded by check B4–B6, symbolic over free phases.)  
**F-F40.2 (representation).** If the register one-tick map is proven to be a non-permutation (a map with nonzero diagonal in the canonical basis) under a corpus theorem, the √2 value changes and §3 must be re-executed. (The permutation structure is fixed by ZS-M46.3A / ZS-F38.T2.)  
**F-F40.3 (convention).** If det′Δ is proven *not* to be SL(2,ℤ)-invariant under unit-area normalization, the torus-block formula of §4.2 is void. (Excluded by check C1.)  
**F-F40.4 (global-exclusion collapse).** If det′Δ is shown *not* to be maximized at the hexagonal modulus, or a scalar-block reading outside the seven registered powers is corpus-forced, Theorem F40.4’s exclusion is incomplete and Gate II reopens on the scalar route. (Excluded for the seven powers by check C5, resting on OPS \[8, 9\].)  
**F-F40.5 (θ₁ exclusion).** If E\* is shown *not* parallelizable, or seam parity is shown to select an *even* spin structure, then θ₁(0) \= 0 no longer applies and the graded-determinant route reopens. (Excluded: E\* parallelizable by ZS-F36/F34; θ₁ odd by the Jacobi identity, check E1–E2.)  
**F-F40.6 (the successor trigger — the one reopening gate).** If a corpus paper derives the odd gauge group and charge lattice from the axioms (ZS-F32 gate B3-1), fixing χ₋ parameter-free, and the resulting ρ\_Λ lands in the observed range, then χ₋ closes as a *positive* gate and B3-scale is DERIVED. This is the *only* gate whose firing reopens the programme; it requires a new axiom-level input, not a re-choice within any closed route. Absent it, χ₋ stays OPEN-TERMINAL and ZS-F41 stays void.  
**F-F40.7 (statistical firewall).** If the ZS-A32 Monte Carlo is shown mis-registered (target not ZS-A31-first), the statistical leg falls to the formula-count reading (2/88 \= 2.27%, still ≤ 5%); the mechanism verdict of this paper is independent and unaffected either way.  
**F-F40.8 (Q-absorption / numerology).** Any derivation that fixes a dimensionful scale from **A**, **Q**, topology alone, or absorbs C\_UV into **Q**, is void by Buckingham-π (inherited ZS-M46 F-M46.7). The firewalled observations of §11 are guarded by the §6.3 look-elsewhere audit, and the χ₋ value candidates by the §7 five-route audit (n \= 2πQ**A** non-integer).  
**F-F40.9 (boundary principle).** If θ₁′(0∣τ\_K) \= 0 (i.e. the first response also vanishes), or if the seam-odd sector is shown to carry a non-degenerate determinant (no zero mode), Theorem F40.8 is void and the surviving object is not a susceptibility. (Excluded: θ₁′(0) \= 2η³ \= 14.1465 ≠ 0, check G1; the zero mode follows from F40.6(a).)  
**F-F40.10 (five-route completeness).** If a corpus route to M\_UV outside the audited five (spectral, Branch A, Branch B, modular depth, C\_UV determinant) is exhibited and is not closed, the §7 audit is incomplete and the χ₋ terminus reopens. (The five are the routes registered across ZS-F33 §9.3, ZS-A31 §6.3, and this paper; a sixth would be a genuine advance.)

# 

# **§13. Cross-version safety and observational non-collision**

ZS-F40 changes no upstream numerical value and reverses no upstream status. Consumed verbatim: (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) and the locked digits (z\*, λ\*, μ, θ) from ZS-M1/ZS-F31 (checks A1–A4); the ZS-F39 frozen Appendix C rule and seed-11 null (byte-identical; B8); the ZS-A24 sector generator q\_{i→j} \= κ²d\_j and its coarse-graining (B10, reproducing ZS-F39.T3/SEL); the ZS-M46 helical normal form and elliptic height h\_K (B2, A6); the ZS-F36 action-level C\_UV \= exp(−Γ\_1PI^ren) template with Γ\_ct constrained (§4.1); and the ZS-A32 target and ΛCDM package (firewalled, §11).  
**Dependency-chain check (§3.2 discipline).** The locked z\* that ZS-M1 supplies propagates unchanged into the papers that consume it: ZS-S1/ZS-U1 read the same fixed point and multiplier, and nothing in §3–§5 perturbs z\*, λ\*, μ, or θ (they are inputs, not outputs, here). The Nome Identity (Lemma F40.L2) is a new *reading* of the already-locked τ\_K, not a new value, so no downstream paper inherits a changed number.  
**Observational non-collision.** The determinant/clock closures are dimensionless mechanism statements and make no dimensionful prediction, so they cannot collide with Planck 2018 ΛCDM \[14\] or Standard-Model couplings. The frozen w \= −1 branch (ZS-F33/A28) is unchanged. The disclosed ΛCDM package enters only the firewalled §11 and only to define the target window; widening or narrowing it does not change the primary-window exclusion margin’s sign (the extended-window non-exclusion is recorded honestly in check C-G). The χ₋ five-route audit (§7) makes no dimensionful claim either — it records that M\_UV is unfixed, consistent with the ZS-A31 no-go boundary.

# 

# **§14. Conclusion**

Two finite gates stood between ZS-F39 and a verdict on the F31–F39 B3 frontier. This paper executed both, under their pre-registered rules, and both closed negatively — each by an exact structural fact rather than a numerical near-miss. Gate I fails because a register permutation and a diagonal clock are Frobenius-orthogonal, giving ε\_C\_int^(phys) \= √2 at every tier. Gate II fails because the bare scalar torus determinant is globally bounded by its hexagonal maximum, and that bound excludes every registered power from the primary target window over the whole moduli space.  
v1.1 closed the third route; v1.2 completes the terminus by auditing the surviving object. The graded-determinant route targets an object that structurally does not exist — θ₁(0∣τ\_K) \= 0, the odd spin structure has a zero mode. But the vanishing determinant is not absence: the first response θ₁′(0) \= 2η³ ≠ 0 survives, and the surviving B3 carrier is the odd susceptibility χ₋ (Theorem F40.8) — exactly what ZS-F32 reduced the frontier to. A five-route audit then shows every corpus route to the *absolute value* of χ₋ (via M\_UV) is closed: the spectral lattice, both benchmark branches, the modular depth (which needs the clock this paper closed), and the C\_UV determinant, with the Charge-Unit Obstruction the PROVEN-irreducible backstop. So the honest terminus is a **closure of the determinant/clock programme plus a positive category identification**: B3-scale is a susceptibility, not a determinant, and its value is a genuine OPEN — confirmed unclosable under current tools, reopenable only by deriving the odd charge unit e₋² from the axioms (ZS-F32 gate B3-1). **ZS-F41 is void; the paper count does not grow.**  
The corpus pattern holds in its sharpest form. Internal iteration converges to honesty; and the honest statement here is a terminal negative verdict, pre-registered and certified, that ends a programme rather than propagating it. The ZS-A32 statistical proximity remains a firewalled observation of record; nothing in this paper derives an absolute scale from **A** and **Q**, and nothing was tuned to reach it.

# 

# **§15. Acknowledgements & Code Availability**

This work consolidates internal Z-Spin Collaboration deep-exploration notes following ZS-F39 v1.1 and ZS-A32 v1.1, and executes the two finite gates pre-registered in ZS-F39 Appendices C and D, absorbing the ZS-F39.1 deliverable per the collaboration decision of record. The companion script *zs\_f40\_verify\_v1\_2.py* (SymPy exact rational linear algebra \+ mpmath 60-digit locked dynamics \+ a certified Banach enclosure of z\* \+ NumPy seed-11 null reproduction \+ the SL(2,ℤ)-reduced Dedekind-η torus determinant \+ Jacobi θ-function identities \+ the pre-registered graded-ratio anti-numerology Monte Carlo) reproduces all 48 checks and 9 guards, prints the two firewalled observations separately, and exits non-zero on any theorem-tier failure; it contains no fail-open clause. This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility for all content, including the √2 refusal identity, the OPS global-exclusion argument, the θ₁ graded-route exclusion, and the Zero-to-Susceptibility boundary principle.

# 

# **Appendix A. The certified Banach enclosure of z\***

The i-tetration fixed point solves z\* \= f(z\*) with f(z) \= exp(iπz/2). On a disk of radius r₀ \= 10⁻³⁰ about the fifty-digit iterate z̃, |f′(w)| \= (π/2) e^{−π Im w/2} is bounded by c\_sup \= (π/2) e^{−(π/2)(Im z̃ − r₀)} \< 1, so f is a contraction there. The Banach fixed-point estimate |z\* − z̃| ≤ |f(z̃) − z̃|/(1 − c\_sup) gives a certified enclosure radius below 10⁻⁴⁰ (residual ≈ 5.5×10⁻⁶²; check A5). Every downstream quantity — μ, θ, τ\_K, det′Δ(τ\_K) — inherits a rigorous bound, so the fifty-digit numerals of this paper are certified, not merely converged. This is the corpus instance of validated numerics (Rump \[15\]; Johansson’s Arb ball arithmetic \[16\]) as used in the Tucker \[10\] and Hales \[11\] certified proofs.

# 

# **Appendix B. The √2 Refusal at both tiers (proof detail)**

Register tier (Q \= 11): Π is the 11-cycle permutation matrix; U \= diag(e^{iφ₀},…,e^{iφ₁₀}). tr(U†Π) \= Σ\_k e^{−iφ\_k}Π\_{kk} \= 0 since Π\_{kk} \= 0 for all k. Thus ‖Π − U‖\_F² \= trΠ†Π \+ trU†U − 2Re·0 \= 11 \+ 11 \= 22, ‖U‖\_F² \= 11, ε \= √2 (checks B4, B5, symbolic in the eleven free phases). Sector tier (3×3): Π₃ the 3-cycle, U₃ diagonal; the identical computation gives 6/3 \= 2, ε \= √2 (check B6). The value is thus independent of the tier and of every phase, which is what licenses the representation-fixing rule of §2.2. The SEL coarse-graining E·L\_slot \= L\_sec·E (check B10) and the non-commutation \[Π, L\_slot\] ≠ 0 (check B11) confirm the objects are the corpus objects.

# 

# **Appendix C. The Dedekind-η evaluation and the OPS ordering**

|η(τ)| is evaluated by SL(2,ℤ)-reduction of τ to the fundamental domain (translations leave |η| invariant; each inversion τ → −1/τ contributes a factor √|τ|), followed by the q-product ∏(1 − q^n). The routine is self-tested against the closed form η(i) \= Γ(¼)/(2π^{3/4}) to forty digits (check C0). The unit-area determinant det′Δ \= Imτ·|η(τ)|⁴ is verified SL(2,ℤ)-invariant to 10⁻⁴⁵ while the (Imτ)²|η|⁴ form is not (check C1). The OPS ordering det′Δ(hex) \= 0.35575 \> det′Δ(square) \= 0.34830 \> det′Δ(τ\_K) \= 0.24815 (check C3) confirms the hexagonal global maximum, the input to Theorem F40.4.

# 

# **Appendix D. Why ZS-F41 is void: the graded-determinant mandate and its retirement**

ZS-F40 v1.0 Appendix D pre-registered a successor (ZS-F41) to derive the graded field content on E\* and compute a graded parent-1PI determinant, and proposed the Burghelea–Friedlander–Kappeler (BFK) Mayer–Vietoris seam-gluing formula \[17\] as the route. Deep exploration retires this mandate on structural grounds, recorded here so the closure is auditable.  
**The premise was already false.** The graded sign structure is corpus-fixed, not open: ZS-S4 §6.7 proves STr(q⁴) \= 0 and STr(q²) \= −18 (the physical Standard-Model field content), and ZS-A30 proves the physical-trace projector W \= STr\_β with W∘s \= 0\. So “derive the graded content” was not the open problem; the open problem was the *odd-sector* content, and that is where the obstruction lives.  
**The target object does not exist.** A graded *determinant* requires a non-degenerate odd-sector Dirac operator. But E\* is parallelizable and seam parity selects the odd spin structure, whose theta constant θ₁(0∣τ\_K) \= 0 vanishes identically (Theorem F40.6): the odd Dirac operator has a zero mode and no determinant. The BFK gluing formula computes ratios of *nonzero* determinants, so it does not rescue a sector whose determinant is structurally zero. The odd sector contributes a susceptibility χ₋, exactly as ZS-F32 reduced it — the BFK route was aimed at the wrong object.  
**The correct object is already registered as irreducible.** χ₋ \= e₋²/(4π²Z₋) is the ZS-F33 Charge-Unit Obstruction: flux integrality fixes the flux number but not the unit (Theorem F40.7). ZS-F34 isolated it as a six-dimensional charge; ZS-F36 proved the associated M\_UV PROVEN-irreducible. Nothing a graded-determinant paper could compute changes this; only a new axiom-level input (ZS-F32 gate B3-1, an odd gauge group and charge lattice from the axioms) can, and that is a different paper with a different mandate — not a determinant computation. **Therefore ZS-F41, as a graded-determinant paper, is void and is not opened.** Should ZS-F32 B3-1 ever be executed, the reopening is governed by F-F40.6, and it would be an axiom-derivation paper, not a determinant paper.

# 

# **References**

\[1\]  Z-Spin Collaboration (K. Kang), ZS-F39: The Seam Uniformization Theorem, v1.1 (2026).  
\[2\]  Z-Spin Collaboration, ZS-F38: The Register Clock Identity, v1.1 (2026).  
\[3\]  Z-Spin Collaboration, ZS-A32: The Planck-Pivot Extremal Ladder — Friedmann-Forced Squares of the Register-Clock Depth, v1.1 (2026).  
\[4\]  Z-Spin Collaboration, ZS-F36 v2.1; ZS-F35 v1.5 (structural factor 1260/4807, C\_norm gate); ZS-F34 v1.8; ZS-F33 v1.8 (Charge-Unit Obstruction, three-route audit); ZS-F32 v1.5 (odd-sector susceptibility χ₋); ZS-F31 v1.4; ZS-A32 v1.1 (C\_UV ≈ 1.25 inference); ZS-A31 v1.5 (modular depth e^(−2πQ)); ZS-A30 v2.1 (physical-trace W \= STr\_β); ZS-S4 (STr(q⁴) \= 0); ZS-A24 v2.1; ZS-M46 v1.4; ZS-M47 v2.0; ZS-M1 (2025–2026).  
\[5\]  G. Koenigs, “Recherches sur les intégrales de certaines équations fonctionnelles,” Ann. Sci. Éc. Norm. Supér. 1, 3–41 (1884).  
\[6\]  H.-J. Borchers, “The CPT-theorem in two-dimensional theories of local observables,” Commun. Math. Phys. 143, 315 (1992).  
\[7\]  H.-W. Wiesbrock, “Half-sided modular inclusions of von Neumann algebras,” Commun. Math. Phys. 157, 83 (1993).  
\[8\]  D. B. Ray and I. M. Singer, “R-torsion and the Laplacian on Riemannian manifolds,” Adv. Math. 7, 145–210 (1971).  
\[9\]  B. Osgood, R. Phillips, and P. Sarnak, “Extremals of determinants of Laplacians,” J. Funct. Anal. 80, 148–211 (1988).  
\[10\]  W. Tucker, “A rigorous ODE solver and Smale’s 14th problem,” Found. Comput. Math. 2, 53–117 (2002).  
\[11\]  T. C. Hales et al., “A formal proof of the Kepler conjecture,” Forum Math. Pi 5, e2 (2017).  
\[12\]  J. Nie, “Optimality conditions and finite convergence of Lasserre’s hierarchy,” Math. Program. 146, 97–121 (2014); arXiv:1206.0319.  
\[13\]  J. B. Lasserre, “Global optimization with polynomials and the problem of moments,” SIAM J. Optim. 11, 796–817 (2001); M. Putinar, Indiana Univ. Math. J. 42, 969–984 (1993).  
\[14\]  Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020); arXiv:1807.06209.  
\[15\]  S. M. Rump, “Verification methods: rigorous results using floating-point arithmetic,” Acta Numerica 19, 287–449 (2010).  
\[16\]  F. Johansson, “Arb: efficient arbitrary-precision midpoint-radius interval arithmetic,” IEEE Trans. Comput. 66, 1281–1292 (2017).  
\[17\]  D. Burghelea, L. Friedlander, and T. Kappeler, “Mayer–Vietoris type formula for determinants of elliptic differential operators,” J. Funct. Anal. 107, 34–65 (1992).  
\[18\]  C. E. Clopper and E. S. Pearson, “The use of confidence or fiducial limits illustrated in the case of the binomial,” Biometrika 26, 404–413 (1934).  
\[19\]  D. Mumford, Tata Lectures on Theta I (Birkhäuser, 1983\) — Jacobi theta constants, θ₁ odd, θ₂θ₃θ₄ \= 2η³; L. Alvarez-Gaumé, G. Moore, and C. Vafa, “Theta functions, modular invariance, and strings,” Commun. Math. Phys. 106, 1–40 (1986) (spin structures and fermion determinants on the torus).  
\[20\]  D. Quillen, “Determinants of Cauchy–Riemann operators over a Riemann surface,” Funct. Anal. Appl. 19, 31–34 (1985) — the determinant line bundle; the Dirac determinant as a theta-function section that survives the zero mode. J.-M. Bismut, H. Gillet, and C. Soulé, “Analytic torsion and holomorphic determinant bundles I–III,” Commun. Math. Phys. 115, 49–126 & 301–351 (1988) — Quillen-metric curvature as a second variation.  
\[21\]  A. Jaffe and E. Witten, “Quantum Yang–Mills theory,” Clay Mathematics Institute Millennium Problem description (2000) — mass gap: classical massless field vs positive quantum mass. F. Englert and R. Brout, Phys. Rev. Lett. 13, 321 (1964); P. W. Higgs, Phys. Rev. Lett. 13, 508 (1964) — the BEH mechanism (nonzero vacuum expectation value). (Cited only as analogies of logical shape; NON-CLAIM.)

# 

# **Version History**

**v1.2 (March 2026):** Deep-exploration revision integrating an external review of v1.1 and a dedicated audit of the χ₋ absolute value. The frozen executions of v1.0–v1.1 (Gate I √2 refusal, Gate II-B OPS exclusion, Gate II-C θ₁ exclusion) are unchanged and reproduced byte-identical. **Status split (F40.6):** θ₁(0∣τ\_K) \= 0 is now labelled PROVEN, while the seam-parity → odd-spin-structure identification is DERIVED-CONDITIONAL on the ZS-F36/F34/F23 correspondence — a more defensive, more accurate statement. New: **Theorem F40.8 (Zero-to-Susceptibility Boundary Principle)** — at the determinant zero the first response θ₁′(0∣τ\_K) \= 2η³ \= 14.1465 ≠ 0 survives (a Quillen determinant-line section, imported PROVEN), so the surviving B3 observable is the odd susceptibility χ₋, fixing the *category* of the B3-scale problem; and the **χ₋ five-route closure audit (§7)** — χ₋ \= (1260/4807)·C\_norm·M\_UV⁴ (structural factor PROVEN), and every corpus route to M\_UV (spectral / Branch A / Branch B / modular-depth-via-H-CLK / C\_UV-determinant) is CLOSED-NEGATIVE or tautological, with the Charge-Unit Obstruction PROVEN-irreducible, so the χ₋ absolute value is a genuine OPEN confirmed unclosable under current tools. Terminal verdict re-scoped to “B3 determinant/clock mechanism programme TERMINAL” (from “B3 mechanism TERMINAL”). Added a Yang–Mills/Higgs analogy box (NON-CLAIM, logical-shape only) and gates F-F40.9 (boundary principle) and F-F40.10 (five-route completeness). References \[19–21\] (Quillen; Bismut–Gillet–Soulé; Jaffe–Witten / Englert–Brout / Higgs) added. Verification 48/48 PASS \+ 9/9 guards (zs\_f40\_verify\_v1\_2.py; v1.1 baseline 39/39 \+ 7/7 reproduced, v1.2 adds Blocks G and H). Zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes up to v1.2.0.)  
**v1.1 (March 2026):** Deep-exploration revision integrating an external review of v1.0; the two frozen executions of v1.0 (Gate I √2 refusal, Gate II-B OPS scalar exclusion) are unchanged and reproduced byte-identical. The review asked whether the graded parent 1PI should be a separate successor paper (ZS-F41); this version answers no and retires the mandate. New: **Theorem F40.6 (the θ₁ Exclusion)** — E\* parallelizable, seam parity selects the odd spin structure, θ₁(0∣τ\_K) \= 0 (verified 1.4×10⁻⁵³), so the graded determinant is the wrong object (the odd sector is a susceptibility, matching ZS-F32); **Theorem F40.7 (χ₋ Irreducibility)** — importing the ZS-F33 Charge-Unit Obstruction, χ₋ \= e₋²/(4π²Z₋) is not fixed by flux integrality; §6.4 pre-registered anti-numerology Monte Carlo over the 28-reading graded-ratio universe (look-elsewhere 100%, all θ-ratios non-evidential); and the ZS-S4 STr(q⁴) \= 0 supertrace import (§6.1). Theorem F40.5 upgraded: all three determinant/clock routes CLOSED-NEGATIVE, χ₋ OPEN-TERMINAL, **ZS-F41 void**. Appendix D replaced with the F41-retirement analysis. Verification 39/39 PASS \+ 7/7 guards (zs\_f40\_verify\_v1\_1.py; v1.0 baseline 30/30 \+ 6/6 reproduced, v1.1 adds Blocks E and F). Terminology unified to the Z-Spin convention (Z-Spin mediation / dynamics). Zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes up to v1.1.0.)  
**v1.0 (March 2026):** Initial public release. Executes the two finite gates pre-registered in ZS-F39 v1.1 Appendices C and D, absorbing the ZS-F39.1 deliverable per the collaboration decision of record. Gate I: Theorem F40.2 (the √2 Refusal) proves ε\_C\_int^(phys) \= √2 exactly at both tiers, phase- and Q-independent; the frozen seed-11 null is reproduced to four decimals (min 1.0975 / p5 1.1585 / median 1.2223) and the Clopper–Pearson success-branch bound (0.15%) certified; Gate I CLOSED-NEGATIVE for the canonical-clock identification. Gate II: the action-level C\_UV \= exp(−Γ\_1PI^ren) formula fixed; Lemma F40.L2 (the Nome Identity q(τ\_K) \= λ\*) proven; the unit-area Ray–Singer determinant det′Δ(E\*) \= 0.24815 computed with SL(2,ℤ)-invariance verified; Theorem F40.4 (the OPS Global Exclusion) proves every registered scalar-torus power excluded from the A32 primary window over the entire moduli space (binding case det′(hex)^{−1/4} \= 1.29483 \> 1.26403); Gate II CLOSED-NEGATIVE on the bare-scalar route. Theorem F40.5 records the F31–F39 B3 frontier CLOSED-NEGATIVE at the canonical-clock / scalar-torus level, the graded parent 1PI OPEN-TERMINAL, the ZS-A32 statistical leg firewalled and surviving; the BFK graded seam route pre-registered for a hypothetical ZS-F41 (Appendix D, OUTLOOK / NON-CLAIM). Two firewalled observations recorded once (§9) and excluded by look-elsewhere audit. Verification 30/30 PASS \+ 6/6 guards (zs\_f40\_verify\_v1\_0.py). Zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration research notes up to v1.0.0.)