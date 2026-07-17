**ZS-F2 — Geometric Impedance A \= 35/437:**

**Reflection-Coefficient Derivation and the Limits of Testability**

**Kenny Kang**

Theme: Foundations \[ZS-F\]  |  Paper 2  |  **Version 1.1 — June 2026**  (corrected revision of v1.0, March 2026\)

Epistemic posture: *verify, do not trust* — every claim below is tagged; reproducibility code in Appendix A.

# **Verification Summary**

**A \= 35/437** — **DERIVED-CONDITIONAL** \+ observationally **STERILE**.  δ-uniqueness theorem — **PROVEN**.  Product structure — **DERIVED-CONDITIONAL** via double-reflection (the v1.0 heat-kernel route is **RETRACTED**).  

**RETRACTED:** ΔN\_eff \= 2A (rejected by Planck 2018 at Δχ² \= \+408, ≈17.6σ; v1.0 absorbed it by sub-casing).  **DEMOTED to NON-CLAIM:** η\_B \= (6/11)³⁵ baryogenesis bridge; face-counting matter budget; the §11.8 η\_topo→Ω\_m chain.  **Zero free parameters** retained for the value of **A**; the downstream cosmological applications are shown to carry undisclosed choices.

# **§0. Abstract**

This is a corrected revision of ZS-F2 v1.0. The duality-deviation invariant δ(P) \= |F−V|/(F+V) is the unique invariant under axioms A0–A6 (§3) and — the structural fact v1.0 understated — is *exactly* the transmission-line reflection coefficient (ē\_V − ē\_F)/(ē\_V \+ ē\_F) \= tanh(½ ln(ē\_V/ē\_F)) between the primal and dual Regge curvature densities (§4). It is this identity, **not** heat-kernel factorization, that forces the product **A** \= δ\_X·δ\_Y: with L\_XY \= 0 (PROVEN), the X–Z–Y channel is a two-seam cavity, and the leading X–Y coupling must cross both seams, double-reflecting into the product (§6). The heat-kernel derivation of v1.0 §7 is withdrawn: heat-kernel factorizes the trace, but the coupling-carrying Seeley–DeWitt a₂ coefficient combines additively, naturally giving the sum δ\_X \+ δ\_Y ≈ 0.567, not the product.

Consequently **A** \= 35/437 is DERIVED-CONDITIONAL on two uniqueness-backed sector-assignment principles (X \= unique space-filler; Z \= unique self-dual), with zero free parameters in its value. However, the deriving cavity is necessarily scale-independent: the observed \~8% gravitational reduction requires the topological spinor phase φ \= π, which is scale-invariant; a wavelength-dependent (resonant) phase gives the wrong sign at cosmological scales, and the round-trip length cannot be fixed parameter-free (§7). Therefore **A** makes no parameter-free prediction distinguishable from a constant-A fit — it is observationally **STERILE**.

Acting on this, v1.1 RETRACTS the ΔN\_eff \= 2A prediction — rejected by the full Planck 2018 likelihood at Δχ² \= \+408 (≈17.6σ on the acoustic angular scale) in v1.0's own §11.5 record, where it was absorbed by sub-casing rather than counted as a falsification — and DEMOTES the η\_B \= (6/11)³⁵ baryogenesis bridge (a reverse-engineered exponent) and the face-counting matter budget (post-hoc fraction selection) to numerological observations. What survives intact: the δ-uniqueness theorem, the reflection-coefficient identity, the space-filling selection SR-X, and the gauge-algebraic A₅ selection (with its SM assignment honestly held as OBSERVATION).

# **Epistemic Status Legend**

| TAG | Meaning |
| ----- | ----- |
| PROVEN | Mathematical theorem, verified to machine precision. |
| DERIVED | Follows from the Z-Spin action \+ prior papers with zero free parameters. |
| DERIVED-CONDITIONAL | Derived under one or more explicitly stated, irreducible assumptions. |
| VERIFIED | Numerical confirmation of a derived/proven result. |
| TESTABLE | Quantitative prediction with an explicit falsification condition. |
| HYPOTHESIS | Plausible, internally consistent, not yet derived or tested. |
| OBSERVATION | Empirically consistent, but the theoretical derivation is post-hoc or pending. |
| STERILE | Internally derived but observationally indistinguishable from a free fit; no parameter-free test exists. |
| NON-CLAIM | Explicitly NOT asserted as a result (e.g., a numerical coincidence, not a derivation). |
| RETRACTED | Previously asserted; withdrawn after a falsification or an error was found. |
| OPEN | Recognized gap requiring future work. |

# **§1. Introduction and Scope**

ZS-F2 v1.0 made one defensible claim and several overclaims. The defensible claim — that δ(P) \= |F−V|/(F+V) is a principled, essentially unique mismatch invariant of polyhedral curvature — is strengthened here. The overclaims — that heat-kernel factorization derives the product, that **A** is unconditionally DERIVED and LOCKED, that ΔN\_eff \= 2A and η\_B \= (6/11)³⁵ are zero-free-parameter predictions, and that the face-counting matter budget is derived — are corrected. This section states the changes; the body justifies each.

## **1.1 What this revision changes**

**(i) Product mechanism (§6).** The v1.0 §7 heat-kernel derivation is RETRACTED and replaced by the double-reflection mechanism. Heat-kernel factorizes the trace, but the coupling-carrying coefficient is additive; the product is instead forced by the two-seam cavity structure, in which δ is literally a seam reflection coefficient (§4).

**(ii) Status of A (§6–§7).** **A** \= 35/437 is downgraded from DERIVED \+ LOCKED to DERIVED-CONDITIONAL, and is additionally shown to be observationally STERILE.

**(iii) ΔN\_eff \= 2A (§8).** RETRACTED. The full Planck 2018 likelihood rejects it at Δχ² \= \+408 (≈17.6σ), as v1.0 §11.5 itself recorded. v1.0 protected the framework by splitting the prediction into three “Possibilities” and discarding only the tested one; v1.1 counts the \+408 as the falsification it is.

**(iv) η\_B \= (6/11)³⁵ (§9).** DEMOTED to NON-CLAIM. v1.0 §1.2 concedes these sections were written to answer whether the pre-existing ZS-U3 formula was “derived or reverse-engineered”; the exponent 35 \= lcm(5,7) rests on a weakly-motivated order-7 constraint, η\_B is exponentially sensitive to it, and the supporting computation is circular.

**(v) Face-counting matter budget (§10).** DEMOTED to OBSERVATION. Slot-counting (39/121) failed against Planck at Δχ² \= 226; face-counting (38/121, 32/121) was adopted afterward. The anti-numerology test fixed the form and varied only the integer, missing the real freedom. The §11.8 η\_topo→Ω\_m chain (residual absorbed by ÷e at a chosen t \= 1\) is demoted with it.

**(vi) Honesty bookkeeping.** Each surviving claim is re-tagged (§11); each withdrawn claim is recorded rather than deleted.

## **1.2 What survives unchanged**

The δ-uniqueness theorem (§3, PROVEN), the reflection-coefficient identity (§4, PROVEN — implicit in v1.0 §3.7 as the “rapidity” structure, here named correctly), the space-filling selection SR-X (truncated octahedron, Kelvin; PROVEN/STANDARD), and the gauge-algebraic A₅ selection (Theorem 4.2A; DERIVED, with the Standard-Model irrep assignment held as OBSERVATION) are retained. The polyhedral arithmetic is unchanged and correct.

## **1.3 Dependency and version-conflict audit**

The corrections propagate. Downstream papers that consumed the withdrawn results must be re-examined: **ZS-U3** (baryogenesis) inherits the η\_B demotion; **ZS-U6** (dark radiation) and **ZS-T1** (ΔN\_eff \= 2A chain) inherit the ΔN\_eff retraction and should drop the sub-casing defense; **ZS-F0 §3.3**, **ZS-A5 §1**, and **The Book §2.5** inherit the §11.8 demotion. Upstream inputs are unaffected: **ZS-M1** (z\*, the i-tetration fixed point) and **L\_XY \= 0** (ZS-F1, ZS-S1, ZS-M6) are PROVEN and are not used by any withdrawn claim. The Koenigs-multiplier results that depend on z\* alone (e.g. the ZS-F16 quasi-revival) are independent of **A** and are untouched by this revision.

# **§2. Definitions and Polyhedral Data**

For a convex polyhedron P on S² with F faces and V vertices, Gauss–Bonnet gives total curvature 4π on both the primal and dual Regge lattices. The average curvature densities are the physical observables whose mismatch defines δ:

*ē\_F := 4π/F  (dual),   ē\_V := 4π/V  (primal)*

*δ(P) := |F − V| / (F \+ V) ∈ \[0, 1\)*

δ is duality-invariant (δ(P) \= δ(P\*); Euler duality swaps F ↔ V). The relevant Archimedean mediators are:

Table 1\. Key polyhedra and their δ-values (full table in v1.0 §2.3).

| Polyhedron | (F, V, E) | Symmetry | δ | Role |
| ----- | ----- | ----- | ----- | ----- |
| Truncated tetrahedron | (8, 12, 18\) | T\_d | 1/5 | Z-mediator |
| Truncated octahedron | (14, 24, 36\) | O\_h | 5/19 | SR-X (space-filler) |
| Truncated cube | (14, 24, 36\) | O\_h | 5/19 | X-class (= trunc. oct.) |
| Truncated icosahedron | (32, 60, 90\) | I\_h | 7/23 | SR-Y (mediator) |
| Truncated dodecahedron | (32, 60, 90\) | I\_h | 7/23 | Y-class (= trunc. icos.) |

# **§3. The δ-Uniqueness Theorem**

Seeking a mismatch function δ(a,b) ∈ \[0,1) of two positive densities a \= ē\_F, b \= ē\_V, v1.0 imposed axioms A0 (domain/smoothness), A1 (scale invariance), A2 (primal/dual symmetry), A3 (separation: δ \= 0 ⟺ a \= b), A4 (saturation: δ → 1 as a/b → ∞), A5 (holonomy composition: oriented mismatches add by Einstein addition x ⊕ y \= (x+y)/(1+xy)), and A6 (linearization: δ ≈ |ε|/2 for b \= a(1+ε)).

**Theorem 3.1 (δ-uniqueness).** The unique function satisfying A0–A6 is δ(a,b) \= |a−b|/(a+b) \= |tanh(½ ln(a/b))|.  **PROVEN** (Aczél's functional equation forces the logarithmic variable; A4 forces Φ \= artanh; A6 fixes the coefficient k \= ½.)

**Honest caveat.** Uniqueness is uniqueness *given* A5 and A6. A5 was added in v1.0 specifically because the weaker set A0–A4 admits infinitely many functions; it encodes a *modeling choice* (that holonomy/log-det corrections compose additively in log-coordinates). A6 is a *normalization choice* (k \= ½ selects |a−b|/(a+b) over, e.g., 2|a−b|/(a+b)). Both are physically reasonable, but they are inputs, not consequences. The theorem is therefore correctly read as: *if* mismatches compose by Einstein addition and the leading coefficient is ½, *then* δ \= |F−V|/(F+V) is forced.

# **§4. δ Is a Transmission-Line Reflection Coefficient**

The structural identity that v1.0 left implicit (its §3.7 “rapidity” remark) is the key to the product (§6) and is worth stating plainly.

**Proposition 4.1.** With a \= ē\_F, b \= ē\_V, δ(P) \= (ē\_V − ē\_F)/(ē\_V \+ ē\_F) \= tanh(½ ln(ē\_V/ē\_F)). This is *identically* the Fresnel / transmission-line reflection coefficient between two media of impedance ē\_F and ē\_V. **PROVEN** (algebraic identity).

In words: a polyhedron's duality-deviation δ is the reflection coefficient seen by a wave crossing the impedance mismatch between its primal (vertex) and dual (face) curvature densities. The “curvature rapidity” ψ \= ½ ln(ē\_V/ē\_F) adds along a chain exactly as relativistic rapidities do (the content of A5). For the two mediators, |δ\_X| \= 5/19 and |δ\_Y| \= 7/23; the sign of (ē\_V − ē\_F) is the reflection phase, and since both mediators have V \> F, both reflection coefficients are negative, so the product (−)(−) \= \+ is positive: A \= \+35/437.

# **§5. Sector Selection**

## **5.1 SR-X — the space-filling criterion (PROVEN/STANDARD)**

The truncated octahedron is the unique Archimedean solid that tiles ℝ³ (Kelvin 1894). This selects the O\_h sector and **δ\_X \= 5/19**. **STANDARD**. (The truncated cube shares δ \= 5/19, so the within-class labelling is immaterial to A.)

## **5.2 SR-Y — the gauge-algebraic criterion (DERIVED, with caveat)**

v1.0 offered two routes to δ\_Y. The isotropy route (Conjecture 4.3) is **VERIFIED** by exhaustive computation over the 13 Archimedean solids but is *not formally proven*. The stronger route is Theorem 4.2A (Adjoint Obstruction): among finite subgroups of SO(3), the icosahedral group A₅ is the unique one admitting a 3-dimensional irrep with adj(SU(3))|\_{A₅} \= 3 ⊕ 5 and Schur-protected gauge-sector isolation. This forces I\_h symmetry, and with the unique I\_h mediator (truncated icosahedron, Theorem 11.4) gives **δ\_Y \= 7/23**. **DERIVED**.

**Honest caveat (inherited NC-R1).** The decomposition 12 \= 1 ⊕ 3′ ⊕ (3⊕5) is proven, but the *dynamical* Standard-Model assignment — that 3′ → SU(2)\_L rather than the other 3-dimensional irrep — is not derived from the action; it is selected by the golden-ratio χ-value separation and held as **OBSERVATION**. Thus δ\_Y is DERIVED for its *value* but the physical sector identification it rides on is OBSERVATION.

# **§6. Product Structure: Double-Reflection in the Two-Seam Cavity**

## **6.1 Why the heat-kernel derivation fails (RETRACTED)**

v1.0 §7 claimed A \= δ\_X·δ\_Y follows from heat-kernel factorization on Γ\_X ⊗ Γ\_Y. This is **RETRACTED**. Heat-kernel factorization makes the *trace* multiply, K(t) \= K\_X(t)·K\_Y(t); but the quantity that carries the non-minimal coupling is a Seeley–DeWitt a₂-type coefficient, and across independent sectors such coefficients combine *additively* (a convolution), so the natural combination is δ\_X \+ δ\_Y \= 5/19 \+ 7/23 ≈ **0.567**, not the product ≈ 0.080. This additive character is the *same* character as the paper's own composition axiom A5 (Einstein addition of rapidities; §3–§4). Heat-kernel therefore does not force the product — if anything it points to the sum. v1.0's §7.2 self-flag (“DERIVED modulo explicit lattice computation, NC-1”) confirms the step was never computed.

## **6.2 The mechanism that does force the product**

**Theorem 6.1 (double-reflection).** Because L\_XY ≡ 0 (PROVEN; ZS-F1, ZS-S1, ZS-M6), every X↔Y transition is mediated by Z: the X–Z–Y channel is a cavity with two reflecting seams, X|Z and Z|Y. By Proposition 4.1, δ is the reflection coefficient at such a seam. The leading X–Y coupling must cross *both* seams, so its amplitude is the round-trip product of the two seam reflection coefficients,

***A** \= ξ\_eff \= (seam\_X)·(seam\_Y) \= δ\_X · δ\_Y \= (5/19)(7/23) \= **35/437**.*

The geometric-series resummation of the cavity ladder gives the closed form 1/(1 ± A) that v1.0 used downstream. Unlike heat-kernel, this mechanism *requires* the product: a single seam crossing would give a sum-like, not a product-like, leading term.

**Status: DERIVED-CONDITIONAL.** Honest caveats: (a) the construction is post-hoc — it was built knowing the target; (b) it is conditional on the sector-assignment principles of §5; (c) the two seams are assigned reflection coefficients δ\_X and δ\_Y, but a stricter X|Z and Z|Y treatment could involve the Z-mediator's own δ\_Z \= 1/5 (truncated tetrahedron), which is an unresolved loose end (NC-1.2). The X↔Y labelling leaves the product invariant (δ\_X·δ\_Y \= δ\_Y·δ\_X), so the value 35/437 is robust to that ambiguity.

# **§7. The Sterility Theorem**

A value being forced (§6) does not make it confirmable. To distinguish **A** \= 35/437 from a constant-A fit, one needs a parameter-free prediction the fit cannot mimic. The natural candidate is the cavity's resonant scale-dependence — a redshift at which the correction turns around. Constructing it parameter-free runs into two walls.

**Wall 1 — the round-trip length is not derivable parameter-free.** The X–Z–Y cavity is a Planck-scale object (Z is the Planck 2D boundary). For any cosmological probe scale λ, the round-trip phase is φ \= 2π·l\_P/λ ≈ 10⁻⁵⁶ ≈ 0 (frozen). At φ ≈ 0 the cavity correction is 1/(1−A) ≈ **1.087 — an enhancement, the wrong sign** for the observed \~8% reduction. Placing a resonance at a cosmological scale would require L\_rt ≈ a cosmological length, i.e. a new free parameter — exactly what the programme forbids.

**Wall 2 — the 8% reduction requires a scale-independent phase.** The minus sign per round-trip in 1/(1+A) \= 1 − A \+ A² − ⋯ is e^{iπ}. The only way to obtain a *reduction* is to read this π as the topological spinor phase (a 2π rotation → −1 for spin-½), which applies to every round-trip *regardless of wavelength*. That makes the correction a constant 1/(1+A) at all scales. A genuinely wavelength-dependent (Fabry–Pérot) phase would give φ ≈ 0 cosmologically → enhancement → wrong sign. The 8% reduction and any resonant scale-dependence are therefore mutually exclusive.

**Theorem 7.1 (Sterility).** The cavity model that yields the observed sign is necessarily scale-independent; hence **A** \= 35/437 makes no parameter-free prediction distinguishable from a constant-A fit. **STERILE**.

**Corollary 7.2.** The mildly descending H₀(z) trend reported in parts of the lensing/quasar/FRB literature (\~1.7–2σ, contested), *if real*, would mildly **disfavor** the constant cavity — which has no redshift freedom — rather than support it. (This reverses a claim made during the internal audit before the round-trip length was analyzed; the reversal is recorded in the A-CLOSURE note and here.)

**Net status of A:** **DERIVED-CONDITIONAL** \+ **STERILE** — a zero-free-parameter, conditionally-derived quantity that is permanently undecidable with current tools. It is neither free numerology nor confirmed physics.

# **§8. Retraction: ΔN\_eff \= 2A**

**The record.** v1.0 §11.5 (Update 2026-04-13) reported that including the Z-sector dark radiation ΔN\_eff \= 2A \= **0.160** in a converged Cobaya run against the full Planck 2018 likelihood (plik TTTEEE \+ commander \+ simall \+ SMICA lensing) produced Δχ²(Step 2 − Step 1\) \= **\+408.27**, with the dominant contribution a ≈**17.6σ** pull on the acoustic angular scale θ\_s.

**The v1.0 defense, and why it fails.** v1.0 invoked the pre-registered ZS-U6 §7.2 definition — “Δχ² \> 20 excludes Possibility 1 (always-on Z-sector); does NOT falsify the base framework” — to conclude that \+408 rejects only “Possibility 1,” leaving “Possibility 2 (BBN-only)” and “Possibility 3 (gradual decay)” intact. But ΔN\_eff \= 2A *is* the clean, parameter-free A-prediction; splitting it into three scenarios after the fact and discarding only the tested one is post-hoc sub-casing that immunizes the framework against its own sharpest test.

**v1.1 action.** The ΔN\_eff \= 2A prediction is **RETRACTED**. A \+408 / 17.6σ rejection is a falsification and is counted as one. The v1.0 §15 summary claim — “five predictions, zero free parameters, all within 1.3σ” — is withdrawn: its cleanest, most direct test failed catastrophically. The corpus-wide ZS-U6 §7.2 sub-casing convention should be re-examined under the same standard.

# **§9. Demotion: η\_B \= (6/11)³⁵**

**Reverse-engineering, conceded.** v1.0 §1.2 states that §9–§10 were written to answer ZS-U3's open question — “η\_B \= (Y/Q)³⁵: is this derived from the action, or reverse-engineered?” The formula pre-existed in ZS-U3; §9–§10 supply a post-hoc justification.

**The exponent is the weak link.** n \= 35 \= lcm(5,7). The order-5 (pentagonal/icosahedral) constraint is well-motivated; the order-7 (“seven temporal layers”) is weakly asserted. And η\_B is *exponentially* sensitive to n: (6/11)³⁴ \= 1.12×10⁻⁹ (1.83× too large), (6/11)³⁵ \= 6.12×10⁻¹⁰ (the Planck value), (6/11)³⁶ \= 3.34×10⁻¹⁰. The celebrated \+0.07σ match requires *exactly* 35 — and 35 also happens to be the numerator of A, which v1.0 presents as confirmation but is more naturally the tell.

**The verification is circular.** v1.0 §14 Category J builds a transfer operator with explicit Z₅×Z₇ symmetry and confirms its CP-odd invariant has period lcm(5,7) \= 35\. Building in Z₅×Z₇ and recovering period 35 assumes what it tests. The genuine question — whether the physics carries both order-5 and order-7 — is the uncomputed part (NC-7), and NC-5/NC-6 concede the O(1) prefactor and the base 6/11 are assumed, not proven.

**v1.1 action.** η\_B \= (6/11)³⁵ is **DEMOTED** to a **NON-CLAIM**: a striking numerical coincidence, not a zero-free-parameter derivation. The base 6/11 \= Y/Q is structurally real; the exponent and the integer-power agreement are not established.

# **§10. Demotion: Face-Counting Matter Budget**

**Fraction-switching after a failure.** v1.0 §11 deploys 6/121 (baryons), 32/121 (CDM), 38/121 (Ω\_m), 83/121 (Ω\_Λ), with a ±1/Q² \= 0.0083 “Z₂ gauge mode” knob that moves between adjacent fractions (39→38, 33→32). Decisively, §11.5 records that slot-counting (39/121) failed against Planck at Δχ² \= 226, after which face-counting (38/121, 32/121) — which passes at Δχ² \= 3.9 — was adopted. The form that matched the data was kept.

**The anti-numerology test checks the wrong freedom.** v1.0 §11.6 fixes the form k/121 and Monte-Carlo-varies only the integer k, certifying k \= 32 as special. It never tests the choices that actually had freedom: face vs slot counting, whether to divide by Q² at all, and the ±1/Q² knob. A small p-value on the wrong variable certifies nothing.

**v1.1 action.** the face-counting matter budget is **DEMOTED** to **OBSERVATION** — empirically consistent after the fact, not a parameter-free prediction. The §11.8 η\_topo→Ω\_m chain is demoted with it: its 2% residual is “explained” by Δa₂/e (dividing by e, justified by a chosen heat-kernel time t \= 1\) plus an uncomputed higher-order term ε\_higher absorbing the remainder — residual-absorption, not derivation. (**NON-CLAIM** for the structural-derivation claim; the numerical convergence remains a **VERIFIED** coincidence at 0.06%.)

# **§11. What Survives — The Honest Ledger**

Confidences are the author's; verify per Appendix A. “v1.1” is the corrected status.

| Item | v1.0 status | v1.1 status |
| ----- | ----- | ----- |
| δ-uniqueness theorem (form of δ) | PROVEN | PROVEN (A5/A6 are modeling choices) |
| δ \= transmission-line reflection coefficient | implicit (“rapidity”) | PROVEN (named) |
| SR-X: truncated octahedron space-fills | STANDARD | PROVEN / STANDARD |
| SR-Y: gauge-algebraic A₅ selection | PROVEN | DERIVED (SM assignment \= OBSERVATION) |
| Value A \= 35/437 | DERIVED \+ LOCKED | DERIVED-CONDITIONAL |
| Product structure A \= δ\_X·δ\_Y | DERIVED (heat-kernel) | DERIVED-CONDITIONAL (double-reflection; heat-kernel RETRACTED) |
| Testability of A | implied predictive | STERILE |
| ΔN\_eff \= 2A | TESTABLE (sub-cased) | RETRACTED (Δχ² \= \+408) |
| η\_B \= (6/11)³⁵ | DERIVED | NON-CLAIM (reverse-engineered) |
| Matter budget (face counting) | DERIVED | OBSERVATION (post-hoc) |
| η\_topo → Ω\_m chain (§11.8) | DERIVED-under-R123 | NON-CLAIM (residual-absorption) |

**Bottom line.** ZS-F2 contains a genuine, principled geometric object (δ, a reflection coefficient) and a forced-but-untestable constant (**A** \= 35/437, DERIVED-CONDITIONAL \+ STERILE). It does not contain a verified, unfitted derivation of any observable: the one clean prediction that was tested (ΔN\_eff) failed; the rest are reverse-engineered or post-hoc fits. The honest programme is to keep the δ-spine, hold **A** as a conditionally-derived sterile constant, discard the fits, and pursue instead the one parameter-free prediction that does not depend on **A** — the z\*-based ZS-F16 quasi-revival — which this paper does not touch.

# **§12. Falsification Conditions (Multi-Layer)**

| Layer / ID | Condition | What dies |
| ----- | ----- | ----- |
| Mathematical (immediate) | δ fails Einstein-addition A5 for Regge densities at 3+ scales | Theorem 3.1 (δ form) |
| Mechanism | A rigorous two-seam cavity computation shows the leading X–Y coupling is not the product δ\_X·δ\_Y | §6 (product); A reverts to undecidable |
| Sterility-breaking | A cosmological length scale is derived from the axioms with no new input | §7 sterility (A would become TESTABLE) |
| Seam-assignment | The seam reflection coefficients provably involve δ\_Z \= 1/5 | the value 35/437 (would shift) |
| Observational (recorded) | ΔN\_eff \= 2A vs Planck | FAILED: Δχ² \= \+408 (§8, RETRACTED) |

Note the asymmetry: the surviving claims (δ form, reflection identity, product mechanism) are falsifiable in principle but, by §7, **A**'s *value* is not observationally falsifiable — that sterility is itself the central finding, not a gap awaiting data.

# **§13. Non-Claims**

**NC-1.1.** The double-reflection derivation (§6) is post-hoc and conditional; it is not a first-principles theorem and does not, by itself, elevate **A** to PROVEN.

**NC-1.2.** Whether the X|Z and Z|Y seam reflections involve the Z-mediator's own δ\_Z \= 1/5 is unresolved; §6 assigns δ\_X, δ\_Y to the seams.

**NC-1.3.** **A** \= 35/437 is not claimed to be PROVEN, and is not claimed to be confirmed by any observation; it is DERIVED-CONDITIONAL \+ STERILE.

**NC-1.4.** η\_B \= (6/11)³⁵, the face-counting matter budget, and the §11.8 chain are numerological / post-hoc; they are not derivations of observables.

**NC-1.5.** The Standard-Model gauge assignment (3′ → SU(2)\_L) is OBSERVATION, not derived from the action (inherited NC-R1).

# **§14. Conclusion**

The geometry of ZS-F2 is real; the bridge from that geometry to confirmed physics is not. The duality-deviation invariant δ is a principled object — exactly a transmission-line reflection coefficient — and that identity, not heat-kernel factorization, is what forces the product **A** \= δ\_X·δ\_Y. **A** \= 35/437 is therefore a zero-free-parameter, conditionally-derived constant; but the cavity that derives it is necessarily scale-independent, so **A** is observationally sterile — it can be neither confirmed nor refuted beyond the post-hoc \~8% match. Acting on this, v1.1 retracts the one clean prediction that was tested and failed (ΔN\_eff \= 2A, \+408/17.6σ) and demotes the reverse-engineered (η\_B) and fraction-switched (matter budget) applications to numerology. What remains is honest and small: a principled δ-object, a forced-but-untestable **A**, and a clear statement of where the programme's reach ends.

# **Acknowledgements & Code Availability**

This revision was produced with AI assistance for verification and drafting; the author retains full responsibility for all content. The corrections consolidate the internal A-CLOSURE audit (June 2026). Verification code: all numerical claims in this paper are reproduced by the script in Appendix A (Python 3.10+, mpmath). No external data files are required.

# **Appendix A. Reproducibility**

Per the epistemic posture — verify, do not trust. Elementary arithmetic plus the Planck length reproduce every load-bearing number.

import mpmath as mp  
from fractions import Fraction as F  
mp.mp.dps \= 30  
   
\# (Prop 4.1) delta IS the reflection coefficient (e=4\*pi/N; 4\*pi cancels)  
def delta\_FV(Fc, Vc): return F(Fc \- Vc, Fc \+ Vc)  
def refl(Fc, Vc):  
    eF, eV \= mp.mpf(1)/Fc, mp.mpf(1)/Vc  
    return (eV \- eF)/(eV \+ eF)  
print(delta\_FV(14,24), mp.nstr(refl(14,24),6))   \# \-5/19 both ways  
print(delta\_FV(32,60), mp.nstr(refl(32,60),6))   \# \-7/23 both ways  
   
\# (Thm 6.1) double-reflection product is forced; X\<-\>Y invariant  
dX, dY \= F(5,19), F(7,23); A \= dX\*dY  
print('A \=', A, '=', mp.nstr(mp.mpf(35)/437,8))  \# 35/437 \= 0.08009153  
print('swap invariant:', dY\*dX \== A)             \# True  
   
\# (Thm 7.1) Planck cavity is frozen at cosmological scales \-\> wrong sign  
Af \= 35.0/437.0; lP, lam \= 1.616e-35, 1e22  
print('phi(cosmo) \=', mp.nstr(2\*mp.pi\*lP/lam,4))  \# \~1e-56  
print('T(phi\~0)=1/(1-A)=', round(1/(1-Af),6))     \# 1.087  ENHANCEMENT  
print('T(topo pi)=1/(1+A)=', round(1/(1+Af),6))   \# 0.926  CONSTANT  
   
\# (sec 9\) eta\_B is exponentially sensitive to the exponent  
for n in (34,35,36): print(n, mp.nstr((mp.mpf(6)/11)\*\*n,4))  
\# 34-\>1.121e-9 (1.83x off) ; 35-\>6.117e-10 (Planck) ; 36-\>3.337e-10  
   
\# (sec 10\) the \+-1/Q^2 fraction knob  
print('1/Q^2 \=', mp.nstr(mp.mpf(1)/121,4))         \# 0.0083  
print('slot 39/121 FAIL(226) \-\> face 38/121 PASS(3.9)')

# **References**

\[1\] T. Regge, Nuovo Cimento 19, 558 (1961).

\[2\] Lord Kelvin, Proc. R. Soc. London 55, 1 (1894).

\[3\] J. Aczél, Lectures on Functional Equations and Their Applications (Academic Press, New York, 1966).

\[4\] P. B. Gilkey, Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem, 2nd ed. (CRC Press, Boca Raton, 1995).

\[5\] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, Adv. Comput. Math. 5, 329 (1996).

\[6\] Planck Collaboration, Astron. Astrophys. 641, A6 (2020).

\[7\] A. G. Riess et al., Astrophys. J. Lett. 934, L7 (2022).

\[8\] J. H. Conway and N. J. A. Sloane, Sphere Packings, Lattices and Groups, 3rd ed. (Springer, New York, 1999).

\[9\] K. Kang, “i-Tetration and the Fixed Point,” ZS-M1 v1.0 (2026).

\[10\] K. Kang, “The Z-Spin Action and U(1) Completion,” ZS-F1 v1.0 (2026).

\[11\] K. Kang, “Gauge Symmetry Constraint: Why Q \= 11,” ZS-F5 v1.0 (2026).

\[12\] K. Kang, “Block-Laplacian Spectral Verification,” ZS-M6 v1.0 (2026).

\[13\] K. Kang, “Baryogenesis,” ZS-U3 v1.0 (2026).

\[14\] K. Kang, “Dark Radiation and N\_eff,” ZS-U6 v1.0 (2026).

\[15\] Z-Spin Collaboration, “A-CLOSURE: Internal Audit of the Geometric Impedance,” internal note (June 2026).

# **Version History**

**v1.1 (June 2026): corrected and honest revision.** Consolidated from the internal Z-Spin Collaboration A-CLOSURE audit (June 2026). Supersedes v1.0 on six points: (1) the product-structure derivation is changed from heat-kernel factorization (RETRACTED) to the double-reflection mechanism in the two-seam X–Z–Y cavity, with δ identified as a transmission-line reflection coefficient (new §4, §6); (2) the status of A \= 35/437 is changed from DERIVED \+ LOCKED to DERIVED-CONDITIONAL, and the Sterility Theorem (new §7) establishes that A is observationally indistinguishable from a constant-A fit; (3) the ΔN\_eff \= 2A prediction is RETRACTED (Planck Δχ² \= \+408, ≈17.6σ; the v1.0 sub-casing defense is rejected, §8); (4) η\_B \= (6/11)³⁵ is DEMOTED to NON-CLAIM (reverse-engineered exponent; circular verification, §9); (5) the face-counting matter budget and the §11.8 η\_topo→Ω\_m chain are DEMOTED to OBSERVATION / NON-CLAIM (post-hoc fraction selection; residual-absorption, §10); (6) all surviving claims are re-tagged in an honest ledger (§11). Retained intact: δ-uniqueness (§3), the reflection-coefficient identity (§4), SR-X (§5.1), and the gauge-algebraic A₅ selection (§5.2, with the SM assignment held as OBSERVATION). No prior content was silently deleted; withdrawn claims are recorded.

**v1.0 (March 2026):** Initial public release (consolidated from internal Z-Spin research notes up to v4.3.0). Geometric impedance A \= 35/437 from polyhedral curvature asymmetry; strengthened δ-uniqueness (A0–A6); sector selection; product structure from heat-kernel factorization; Measure-Projection Weight Theorem and Minimality Lemma (η\_B \= (6/11)³⁵); Truncation-Dual Theorem and face-counting matter budget; Spectral–Index Projection Theorem (§11.8). Reported 81/81 PASS. (Several of these claims are corrected or withdrawn in v1.1; see above.)