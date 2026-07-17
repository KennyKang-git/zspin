**ZS-F44**   
**The Charge-Unit Gauge No-Go and the Parent-Factor Non-Determination: a Stand-Alone Representation-Theoretic No-Go for Dimensionful Charge Units in Compact p-Form Zero-Mode Sectors, and Its Corollary that No Admissible Parent-Factor Realization Fixes C\_UV**

Kenny Kang — Z-Spin Cosmology Program (independent) · July 2026 · Foundations Series · Paper code **ZS-F44** · Version 1.1. Unified execution of the two continuations pre-registered in ZS-F43 v1.1 §Conclusion — the stand-alone no-go theorem (ZS-F44 branch) and the Parent-Factor Realization Execution (ZS-M48 branch) — shown here to be one theorem. Consumes ZS-M1, ZS-M46, ZS-M47, ZS-F32, ZS-F33, ZS-F35, ZS-F36, ZS-F39, ZS-F42, ZS-F43, ZS-A25, ZS-A31, ZS-A32.

**Verification: 18/18 PASS \+ 9/9 guards** (zs\_f44\_verify\_v1\_1.py; fail-closed, exits non-zero on any theorem-tier failure) | **3 firewalled observations** printed separately, never counted as PASS | **Zero fitted parameters** | (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

**§0. Abstract**

ZS-F43 v1.1 re-typed the B3 charge residual and closed with two disjoint, "mutually exclusive in outcome" continuations: **(ii) ZS-F44** — isolate the algebraic Theorem F43.T1′ from the Z-Spin embedding as a stand-alone no-go about compact p-form zero-mode sectors; and **(i) ZS-M48** — compute, or prove impossible, the shared metric stiffness C\_UV from the parent-factor / E\_len construction. This paper proves the two are **one theorem**: the parent-factor non-determination (i) is a *corollary* of the stand-alone no-go (ii). A single paper therefore discharges both reserved codes, reducing the corpus's paper count rather than expanding it.

**(T1) The Charge-Unit Gauge No-Go** \[general theorem IMPORTED-PROVEN; instance DERIVED\]. For any compact p-form zero-mode sector whose gauge-invariant observable algebra is the Weyl algebra 𝒲 over ℤ × U(1) — generators (n̂, φ̂) with \[n̂, φ̂\] \= i, or equivalently the shift–clock pair (Ŝ, Ŵ) with ŴŜ \= ζŜŴ — the dimensionful charge unit e₋² is **not an invariant of 𝒲**. Two distinct units q₁², q₂² generate the *same* algebra with unitarily-equivalent irreducible representations (Stone–von Neumann in Mackey's locally-compact form), differing only by an overall spectral scale that no automorphism of 𝒲 detects. The unit enters solely through the external spectral dictionary Λ \= e₋²(n̂ \+ ω/2π), a *pairing datum* between the sector's arithmetic ledger and the gravitational metric ledger. Complementarily (T2), Dirac/Freed–Moore–Segal flux quantization fixes the *integer* class in differential cohomology (Smith normal form: primitive brane charge 1, Wess–Zumino phase 2\) but leaves the dimensionful normalization free — *integers are determined; units are not*. The no-go needs only Stone–von Neumann–Mackey and differential-cohomology discreteness, so it reads outside the corpus.

**(M48-corollary) Parent-Factor Non-Determination** \[DERIVED-CONDITIONAL on (H-NOTR): the registered ZS-M46/M47 parent factor is Type III (no tracial state)\]. The shared C\_UV leg is defined by C\_UV \= exp(−Γ\_1PI^parent), with Γ\_1PI a functional of the parent factor's modular data. The corpus parent factor is a Type III factor (ZS-M46 Theorem C; ZS-M47), so — by the Connes classification, a *consumed* structural fact, not one this paper derives — it carries **no tracial state**, hence Γ\_1PI has no canonical trace to fix its *absolute* normalization. That absolute normalization is a dimensionful datum drawn from the sector, which T1 forbids. Consequently **no admissible parent-factor realization fixes C\_UV ∈ \[1.0, 1.6\] from parent modular data alone** — the ZS-M48 "compute-or-no-go" branch resolves to *no-go*, as a corollary of T1. *Correction of record (v1.1):* the v1.0 argument routed this through "infinite Jones index," which is mathematically wrong — Type III factors admit finite-index subfactors (Kosaki 1986; explicit index-3 examples, Kosaki 1994). The corrected argument is index-independent: it rests only on the absence of a tracial state (H-NOTR) and on T1. A finite-index inclusion, even if present, would supply only a *relative* invariant \[M:N\], never the *absolute* dimensionful unit C\_UV requires.

**(T3) The Kernel-Factorization Theorem** \[DERIVED; value REGRESSION, firewalled\]. Quantitatively, C\_UV factorizes as a **dimensionless kernel times exactly one metric-side datum**: C\_UV \= \[c\_χ/(1260/4807)·e^{8π**Q**}\] · (H\_∂/M̄\_P)², where the kernel \= 3.5739×10¹²⁰ is built only from (**A**, **Q**, ω) — with 1260/4807 \= 36**A**/**Q** exactly — and (H\_∂/M̄\_P)² is the single dimensionful input. Behind the derivation ⊥ regression firewall this evaluates to C\_UV \= 1.244 (ZS-A32 band ≈ 1.244), reproducing ZS-A31/A32 with no new empirical content. The factorization is the quantitative face of T1: the absolute value needs precisely one dimensionful datum, exactly as the no-go predicts.

**Barrier B3 is not closed and is now proven not closable by the parent-factor route.** What changes is the *status of the C\_UV programme* (from OPEN to CLOSED-NEGATIVE-under-the-parent-factor-realization, i.e. the number cannot come from parent modular data), the *external legibility* of the residual (a stand-alone representation-theoretic no-go replacing a Z-Spin-internal assertion), and the *corpus paper count* (M48 absorbed into F44). The residual is unchanged: the same single metric-side datum (B3-B) that ZS-F33/F42/F43/F45/F46 reached; Ω\_Λ,0 \= 83/121 (ZS-A30) and U\_N are untouched. Verification: 18/18 PASS \+ 9/9 guards; zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

**Epistemic Status Legend**

| Tag | Meaning in this paper |
| ----- | ----- |
| **PROVEN** | Established within the corpus by exact mathematics, machine-verified. |
| **IMPORTED-PROVEN** | External theorem with published proof, consumed as-is (Stone–von Neumann–Mackey; Freed–Moore–Segal flux uncertainty; Dirac/differential-cohomology discreteness; Longo Jones-index theory). |
| **DERIVED** | Follows from corpus axioms/locked constants by explicit steps, no additional hypotheses. |
| **DERIVED-CONDITIONAL** | Derived contingent on explicitly listed, falsifiable conditions (named at point of use). |
| **DERIVED-BY-INHERITANCE** | Verbatim consumption of an upstream corpus result at its stated version and status. |
| **REGRESSION (FIREWALLED)** | Comparison against external data behind the derivation ⊥ regression firewall; printed separately; never counted as PASS. |
| **NON-CLAIM** | Explicit registration that a statement is not being made. |
| **OPEN** | Well-posed and unresolved. |
| **CLOSED-NEGATIVE** | A route proven not to work under its pre-registered rule (here: the parent-factor C\_UV route). |

**§1. Introduction: two continuations, one theorem**

ZS-F43 v1.1 is the re-typing terminus of the charge-unit arc ZS-F33 → ZS-F34 → ZS-F35 → ZS-F36. Its Theorem T1 proved that the dimensionful membrane charge e₆ is *invisible from inside* the Z-sector zero-mode algebra — a representation-theoretic fact, not a toolkit limitation — so the well-posed unknown of barrier B3 is the dimensionless ê₆ := e₆/M̄\_P². Its algebraic form, Theorem F43.T1′, stated this as a property of the compact zero-mode Weyl algebra. F43 then closed by pre-registering two continuations and declaring them "mutually exclusive in outcome": **(i)** an execution paper (ZS-M48 / ZS-F44) that would *compute* the shared stiffness C\_UV from the parent factor, or prove no admissible realization can; and **(ii)** a paper (ZS-F44) that would *isolate T1′* as a stand-alone no-go legible outside the corpus. F43 flagged the priorities: the ε\_C\_int / E\_len computation is where the open-gate structure points (branch i), while T1′ is where external legibility is highest (branch ii).

This paper's thesis is that F43's "mutually exclusive" framing, while correct about *outcomes* (a positive C\_UV computation and a no-go cannot both hold), obscures a structural fact about *provenance*: **branch (i) is not an independent computation but a corollary of branch (ii)**. The reason is direct. C\_UV is, by construction, an absolute normalization — C\_UV \= exp(−Γ\_1PI^parent) — and the parent factor that would supply Γ\_1PI is a Type III factor (ZS-M46/M47), which by the Connes classification carries no tracial state and hence no canonical constant to fix Γ\_1PI's absolute value. An absolute normalization drawn from a factor with no trace is exactly a dimensionful unit drawn from the sector algebra — which T1 proves impossible. So the parent-factor route cannot fix C\_UV, and it cannot for the *same reason* the charge unit is invisible: both are metric-side pairing data, not sector invariants. The two continuations collapse to one theorem, and one paper discharges both codes. (The argument is index-independent; the v1.0 route through "infinite Jones index" is retracted in v1.1 — see §3.2.)

The corpus benefit is concrete and was the motivating instruction of record: the paper count does not grow. Rather than writing ZS-M48 (parent-factor execution) and ZS-F44 (stand-alone no-go) as two papers, F44 v1.0 proves the second and derives the first as its corollary, absorbing M48. This is the same discipline that repositioned ZS-F45 as an audit and folded ZS-F47/F48 into ZS-F46: consolidate where the mathematics consolidates, rather than accumulate closure-attempt papers.

The difficulty the paper accepts is deliberate. It leans on three non-trivial external pillars — the Stone–von Neumann theorem in Mackey's locally-compact form (uniqueness of the Weyl-algebra irrep), the Freed–Moore–Segal analysis of flux uncertainty (fluxes are noncommutative and fix integer classes, not units), and the Connes classification of Type III factors (no tracial state, hence no canonical absolute normalizer for the parent effective action) — and it discharges a quantitative gate (the C\_UV kernel factorization) with a firewalled 50-digit computation. None of these is a Z-Spin-internal assertion; the no-go is stated so that a reader who has never seen the corpus can check it.

Notation follows the corpus: ê₆ := e₆/M̄\_P²; 𝒲 is the Weyl algebra over ℤ × U(1); Γ\_1PI^parent is the parent one-particle-irreducible effective action; H\_∂ is the present-epoch horizon rate, consumed only where firewalled. Terminology follows the corpus convention (*Z-sector* the stage, *Z-Spin* the action). All numerical claims are reproduced by zs\_f44\_verify\_v1\_1.py (18/18 PASS \+ 9/9 guards); every scale-bearing number appears only in firewalled context.

**§2. The Charge-Unit Gauge No-Go (Theorem F44.T1)**

**2.1 The observable algebra of a compact zero-mode sector.** \[Setup; IMPORTED-PROVEN structure.\] Let a compact p-form gauge field have a zero-mode sector whose large-gauge-invariant observables are the holonomy phase and its conjugate flux number. In the corpus instance (ZS-F32.24–26, ZS-A25) these are the Weyl pair (n̂, φ̂) on ℤ × U(1) with \[n̂, φ̂\] \= i, generating the Weyl algebra 𝒲. On a finite register (dimension N \= **Q** truncation for verification) 𝒲 is realized by the shift Ŝ and clock Ŵ with the Weyl relation

**Ŵ Ŝ \= ζ Ŝ Ŵ,  ζ \= e^{2πi/N},**

reproduced at machine precision (check T1a). The key structural fact is that this relation — the entire content of the algebra — contains *no charge unit*: Ŝ and Ŵ are dimensionless generators.

**2.2 The no-go.** \[Theorem F44.T1; general statement IMPORTED-PROVEN (Stone–von Neumann–Mackey), instance DERIVED.\] *The dimensionful charge unit e₋² is not an invariant of 𝒲.* Two distinct units q₁² ≠ q₂² define the same generators (Ŝ, Ŵ) and hence, by the Stone–von Neumann theorem in Mackey's locally-compact form, unitarily-equivalent irreducible representations. The dimensionful number-operator spectra Λ\_i \= q\_i²(n̂ \+ ω/2π) differ, but the *dimensionless* spectra Λ\_i/q\_i² are identical (check T1b), so no automorphism of 𝒲 recovers q²; the intertwiner is the identity (check T1d). The unit is physical only through the external dictionary Λ \= e₋²(n̂ \+ ω/2π), which pairs the sector's arithmetic with a metric scale (check T1c). Hence:

**The charge unit is a gauge from inside the sector; it becomes physical only across the pairing with gravity.**

This is the precise content of the phrase "Charge-Unit Gauge Principle" (ZS-F43 §remark), here promoted from an interpretive remark to a theorem with an external proof burden.

**2.3 Complement: integers are fixed, units are not (Theorem F44.T2).** \[IMPORTED-PROVEN (Dirac; Freed–Moore–Segal); instance DERIVED.\] The no-go is sharpened by its complement. Dirac charge quantization, in its differential-cohomology form (Freed; Freed–Moore–Segal), fixes the *integer* periods of the flux — the free part of H^p(X;ℤ) — discretely: the corpus flux pairing has Smith normal form diag(1, 2), reproducing ZS-F36's primitive wrapped-brane charge 1 and Wess–Zumino phase 2 (check T2a). Integer periods cannot be moved by any continuous rescaling of the unit (check T2b). So the compact zero-mode sector determines *which integers* (the flux quantum numbers) but not *the size of the unit* they multiply (check T2c). Freed–Moore–Segal's "uncertainty of fluxes" — that fluxes generate a Heisenberg group and cannot be simultaneously sharp — is the field-theoretic shadow of the same fact: the flux algebra fixes commutation and integrality, not an absolute dimensionful normalization.

**2.4 External legibility.** \[Status.\] Theorem F44.T1 ∧ T2 needs only two imported ingredients — Stone–von Neumann–Mackey (uniqueness of the Weyl irrep) and differential-cohomology discreteness (integer periods). Neither mentions Z-Spin. The corpus content is solely that R1–R3 (ZS-F43) identify ê₆ \= e₆/M̄\_P² as the specific minimal invariant left after the pairing. This is the sense in which F44 states a result "that reads outside the corpus": a referee unfamiliar with Z-Spin can verify that a compact p-form zero-mode Weyl sector fixes flux integers but not dimensionful charge units.

**§3. Parent-Factor Non-Determination (Corollary F44.M48)**

**3.1 The shared leg.** \[Setup.\] The B3 charge programme's one remaining number is the metric stiffness C\_UV, defined at action level as C\_UV \= exp(−Γ\_1PI^parent), where Γ\_1PI^parent is the one-particle-irreducible effective action of the parent factor whose modular length functor E\_len localizes the residual at the seam (ZS-F39). The ZS-M48 branch of F43 asked: can C\_UV be *computed* from this parent construction (target ≈ 1.244, band \[1/4, 4\]), or is there no admissible realization that yields C\_UV ∈ \[1.0, 1.6\]?

**3.2 The corollary.** \[DERIVED-CONDITIONAL on (H-NOTR).\] The corpus parent factor is a Type III factor (ZS-M46 Theorem C: the seam realization is the Guido–Longo–Wiesbrock U(1)-current net; ZS-M47: the relative commutant is a Type III factor). The **load-bearing fact is that a Type III factor carries no tracial state** (Connes classification) — a *consumed* structural condition, labelled **(H-NOTR)**, which this paper does not re-derive. With no tracial state, Γ\_1PI^parent has **no canonical trace to fix its absolute normalization** (check M48b). But that absolute normalization is exactly what C\_UV is, and extracting it from the sector is drawing a dimensionful datum from the sector algebra, which Theorem F44.T1 forbids. Therefore:

**Under (H-NOTR) ∧ T1, no admissible parent-factor realization fixes C\_UV ∈ \[1.0, 1.6\] from parent modular data alone; the ZS-M48 branch resolves to no-go, as a corollary of T1** (check M48c).

*Correction of record (v1.1).* The v1.0 statement of this corollary routed the argument through "Type III₁ ⇒ infinite Jones index ⇒ no trace." That implication is **false and is retracted**: Type III factors admit finite-index subfactors — Kosaki extended Jones' index to arbitrary factors (1986), and explicit Type III₀ factors with isomorphic index-3 subfactors are known (Kosaki 1994). Two distinct levels were conflated: the *factor-level* fact "a Type III factor has no tracial state" (true, index-independent) and the *inclusion-level* quantity "Jones index \[M:N\]" (which can be finite for Type III inclusions). The corrected argument (check M48a) uses only the factor-level fact. Crucially, this makes the corollary *stronger*, not weaker: even if the seam inclusion has finite index, that index is a *relative* invariant of N ⊂ M and still supplies no *absolute* dimensionful unit — so the no-go holds whether or not the index is finite.

**3.3 Why the two branches are one.** \[DERIVED.\] F43 called (i) and (ii) "mutually exclusive in outcome," which is true: a positive C\_UV computation from parent data (i-success) would falsify the stand-alone no-go (ii). What §3.2 establishes is stronger — (i) cannot succeed *because* (ii) holds. The two are not independent experiments with opposite outcomes; they are one theorem stated twice, once algebraically (T1: the unit is not a sector invariant) and once dynamically (M48: the absolute normalization is not a parent-modular invariant). A single paper proving T1 derives M48 for free (check U1).

**§4. The Kernel-Factorization Theorem (Theorem F44.T3)**

**4.1 Statement.** \[DERIVED; value REGRESSION, firewalled.\] The metric stiffness factorizes as a dimensionless kernel times exactly one dimensionful datum:

**C\_UV \= \[ c\_χ / (1260/4807) · e^{8π**Q\*\*} \] · (H\_∂/M̄\_P)²,\*\*

where the bracketed **kernel** is built only from the locked/frozen dimensionless data — c\_χ \= 498/(121ω²) \= 0.8063350941 (check CUV1), 1260/4807 \= **36A/Q** exactly (check CUV4), and e^{8π**Q**} — and evaluates to 3.5739×10¹²⁰ (check CUV2), while (H\_∂/M̄\_P)² is the single metric-side input (check CUV3).

**4.2 The quantitative face of the no-go.** \[DERIVED.\] T3 makes T1 quantitative. The no-go says the absolute value of C\_UV needs exactly one dimensionful datum; the factorization exhibits that datum explicitly as (H\_∂/M̄\_P)², cleanly separated from a kernel that carries no units. Every dimensionless ingredient of C\_UV is fixed by (**A**, **Q**, ω); the one thing the sector cannot supply — the metric scale — is isolated in a single factor. This is not a computation of C\_UV's value from within the corpus (which T1 forbids) but a proof that the value, *whatever it is*, is the kernel times one external number.

**4.3 Firewalled consistency.** \[REGRESSION.\] Behind the derivation ⊥ regression firewall, supplying the Planck-2018-class datum (H\_∂/M̄\_P)² ≈ 3.48×10⁻¹²¹ gives C\_UV \= 1.244 (§Appendix B, O-1), inside the ZS-A32 band ≈ 1.244 and reproducing the ZS-A31 regression M\_eff \= 2.48 meV. This is T4 of ZS-F43 re-expressed: no new empirical content, one pre-registered consistency point. The number never enters a PASS block (guard G7). **§5. What F44 closes, and what it does not: the B3 ledger**

**5.1 Closed.** \[DERIVED.\] The **parent-factor C\_UV route** is closed negatively: no admissible parent-factor realization fixes C\_UV from modular data alone (Corollary M48, §3). This resolves the ZS-M48 branch of F43 — the "compute-or-no-go" question resolves to no-go — and it does so as a corollary of the stand-alone no-go T1, not as an independent computation. The ZS-F39 Appendix D / ZS-F40 pre-registration of a "proof-carrying global-minimum gate for C\_UV" is thereby answered: the gate cannot be closed by a parent-modular computation, because the target is a metric-side pairing datum, not a modular invariant.

**5.2 Not closed.** \[OPEN, unchanged.\] Barrier B3 itself is *not* closed and is not claimed closed. The dimensionless ê₆ \= e₆/M̄\_P² remains OPEN as a derivation; its conditional value 2π e^{−4π**Q**} (ZS-F43) is untouched. What F44 adds is that the one route F43 flagged as "where the open-gate structure points" (parent-factor C\_UV) is now known not to close it — the residual is genuinely a single external metric-side datum (B3-B), the same one ZS-F33/F42/F43/F45/F46 reached (check U2). B3-B is now proven to be irreducibly external, not merely unreduced.

**5.3 Untouched.** \[DERIVED-BY-INHERITANCE.\] Ω\_Λ,0 \= 83/121 (ZS-A30) and the present-epoch coincidence U\_N (ZS-A29) are separate problems, untouched (breakthrough C). No upstream value or status moves (guard G6). The ZS-F40 terminal verdict, the ZS-F41 Stopping Rule, and the ZS-F45 audit stand.

**§6. Falsification gates and the unification ledger**

Table 1\. Pre-registered gates of ZS-F44.

| Gate | Tier | Trigger | Consequence |
| ----- | ----- | ----- | ----- |
| **F-F44.1** | Theoretical (immediate) | Exhibit an observable of the compact zero-mode Weyl algebra 𝒲 whose value depends on the charge unit e₋² at fixed dimensionless data. | T1 falsified; the no-go collapses; B3 reverts to its F43 form. |
| **F-F44.2** | Theoretical (parent factor) | Exhibit a tracial state on the corpus parent factor (violating (H-NOTR) / the Type III classification), supplying a canonical absolute Γ\_1PI normalizer. | Corollary M48 falsified; the parent-factor C\_UV route reopens. |
| **F-F44.3** | Theoretical (positive outcome) | An admissible parent-factor realization computes C\_UV ∈ \[1.0, 1.6\] from modular data with no metric-side input. | T1 ∧ M48 falsified — **and B3's C\_UV route closes.** The corpus wins either way; registered as the honest exchange rate. |
| **F-F44.4** | Structural (kernel) | The kernel c\_χ/(1260/4807)·e^{8π**Q**} is shown to carry a hidden dimensionful dependence, or 1260/4807 ≠ 36**A/Q**. | T3 factorization falsified. |
| **F-F44.5** | Scope (over-claim) | Any reading of F44 as closing B3 or deriving the absolute e₆. | Fires immediately; F44 is a no-go, NON-CLAIM on the absolute value. |

Table 2\. Unification ledger.

| Item | Status |
| ----- | ----- |
| T1 Charge-Unit Gauge No-Go (Weyl algebra, unit not an invariant) | **IMPORTED-PROVEN (SvN–Mackey) \+ DERIVED** (T1a–T1d) |
| T2 flux integers fixed, units not (differential cohomology) | **IMPORTED-PROVEN (Freed–Moore–Segal) \+ DERIVED** (T2a–T2c) |
| M48 Parent-Factor Non-Determination (corollary of T1) | **DERIVED-CONDITIONAL on (H-NOTR): ZS-M46/M47 Type III, no tracial state** (M48a–M48c); index-independent |
| the two F43 continuations are one theorem | **DERIVED** (U1) |
| T3 kernel factorization C\_UV \= kernel × (H\_∂/M̄\_P)² | **DERIVED** (CUV1–CUV4) |
| C\_UV \= 1.244 | **REGRESSION, firewalled** (O-1) |
| parent-factor C\_UV route | **CLOSED-NEGATIVE** (§5.1) |
| barrier B3; ê₆ | **NOT closed; OPEN** (§5.2) |
| residual \= single B3-B metric-side datum | **inherited** (U2) |
| Ω\_Λ,0 \= 83/121; U\_N | **untouched** (§5.3) |

**§7. Conclusion**

The charge-unit arc ends not with a number but with a theorem about why no number of a certain kind could ever have come from where the corpus was looking. Theorem F44.T1 states, in language legible to anyone who knows the Stone–von Neumann theorem, that a compact p-form zero-mode sector fixes its flux integers but not the dimensionful unit those integers multiply — the unit is a gauge from inside the sector, physical only across the pairing with gravity. Its corollary, absorbing the reserved ZS-M48, shows that the one dynamical route F43 flagged as most promising — computing the metric stiffness C\_UV from the parent factor — cannot succeed, because that parent factor is a Type III factor with no tracial state, so its effective action has no canonical absolute normalizer to give (an argument independent of the Jones index, whether finite or infinite). The two continuations F43 called mutually exclusive are one theorem: the algebraic no-go and its dynamical shadow. The kernel factorization makes the statement quantitative — C\_UV is a dimensionless kernel, fixed entirely by (**A**, **Q**, ω), times exactly one external metric-side datum — so that the firewalled value 1.244 is seen for what it is: the kernel times one number the sector was never able to supply. Barrier B3 is not closed; the parent-factor route to it is now closed negatively; and the residual stands where five prior routes left it, as a single calibrated boundary datum. What F44 contributes is finality of a specific kind: the corpus now knows, with an externally-checkable proof, that this residual is irreducibly a pairing datum — and it knows it while writing one paper where two were reserved.

**Acknowledgements & Code Availability**

Verification code: zs\_f44\_verify\_v1\_1.py (Python 3; mpmath at 50 significant digits; exact Fraction arithmetic; SymPy symbolic \+ Smith normal form; NumPy finite Weyl-algebra models). Fail-closed — any theorem-tier check or guard failure exits non-zero — and prints the firewalled observation block under an explicit banner, never counting it as PASS. Result at release: 18/18 PASS \+ 9/9 guards; 3 firewalled observations. Developed under the corpus session protocol (deep-exploration record in Appendix A) with multi-AI adversarial review for circularity detection.

**Appendix A. Deep-exploration record (session protocol)**

**A.1 Record 1 — the unification.** Step 0 (long list, 7): L1 elevate T1′ to a stand-alone no-go (F43 branch ii) — kept; L2 execute the M48 parent-factor C\_UV question (F43 branch i) — kept; L3 prove the two are one theorem (M48 \= corollary of T1) — kept (pivot); L4 anchor T1 externally on Freed–Moore–Segal flux uncertainty — kept; L5 the C\_UV kernel factorization (dimensionless kernel × one datum) — kept; L6 the parent no-trace step for M48 (Type III ⇒ no tracial state; v1.1-corrected from the retracted infinite-index route) — kept; L7 compute C\_UV's absolute value from the corpus — dropped (F-F42.36; T1 forbids; numerology). Step 1 (issue list, 5, by influence): I1 \= L3 (unification — reduces two codes to one), I2 \= L1+L4 (T1 stand-alone \+ external anchor), I3 \= L2+L6 (M48 no-go), I4 \= L5 (kernel factorization), I5 \= dependency/consistency. Step 2 (tree): I2 → I3 → I1 → I4 → I5. Step 3 (statuses): I2 IMPORTED-PROVEN \+ DERIVED (Weyl irrep uniqueness; FMS flux uncertainty); I3 DERIVED-CONDITIONAL on (H-NOTR) (Type III ⇒ no tracial state ⇒ no absolute normalizer; index-independent); I1 DERIVED (M48 is a corollary of T1, so the two continuations are one theorem); I4 DERIVED \+ firewalled REGRESSION (kernel \= 3.5739×10¹²⁰; C\_UV \= 1.244 only behind the firewall); I5 DERIVED-BY-INHERITANCE (no upstream move; residual \= B3-B). Step 4 (convergence): node-change counts 5 → 2 → 1 → 0, convergent (|f′| \< 1). Step 5 (scoring): converged; corpus-non-conflicting (no upstream value/status moved; the sole numbers — Weyl dev, Smith normal form \[1,2\], kernel, 36A/Q — are structural/consumed); anti-numerology unchanged (the C\_UV value is firewalled, never fitted; guard G5). Self-reference check: the seductive move was to read "two branches are one" as the familiar corpus unification trope; the audit anchored it instead on an independent quantitative fact — the kernel factorization and the parent no-trace step — and, decisively, *overturned* F43's own "mutually exclusive" framing rather than conforming to it, so the unification is a challenge to the source, not an echo of it. The M48-as-corollary link depends on (H-NOTR) — the ZS-M46/M47 Type III (no-tracial-state) realization — so it is held at DERIVED-CONDITIONAL, not promoted. v1.1 correction: the v1.0 'infinite Jones index' route was mathematically wrong (Type III admits finite-index subfactors, Kosaki 1986/1994) and is retracted; the corrected argument is index-independent and strictly stronger. Verdict: publishable as the unified charge-unit no-go / parent-factor non-determination paper, absorbing ZS-M48; confidence bands registered in-session (T1 elevatable to external no-go: 90%; M48 \= corollary of T1: 60%; kernel factorization consistent with T1: 90%; one paper replacing two codes maximizes value: 90%).

**Appendix B. Numerical dictionary and firewalled block**

Table 3\. Corpus-internal quantities (PASS-eligible).

| Quantity | Value | Check |
| ----- | ----- | ----- |
| **A**; **Q**; (dim X, Z, Y) | 35/437; 11; (3,2,6) | LOCKED |
| ω \= arg f'(z\*); |f'(z\*)| | 2.2592495540; 0.8915 | K1–K2 |
| Weyl relation ŴŜ \= ζŜŴ deviation | \< 10⁻¹² | T1a |
| dimensionless spectra Λ/q² (q₁ ≠ q₂) | identical | T1b |
| flux pairing Smith normal form | diag(1, 2\) | T2a |
| parent factor: Type III ⇒ no tracial state (H-NOTR, consumed) | — | M48a–M48b |
| c\_χ \= 498/(121ω²) | 0.8063350941 | CUV1 |
| dimensionless kernel c\_χ/(1260/4807)·e^{8π**Q**} | 3.5739×10¹²⁰ | CUV2 |
| 1260/4807 \= 36**A**/**Q** | exact | CUV4 |

Table 4\. Firewalled quantities (never counted as PASS).

| Quantity | Value | Source |
| ----- | ----- | ----- |
| (H\_∂/M̄\_P)² | ≈ 3.48×10⁻¹²¹ | Planck 2018 (O-2) |
| **C\_UV \= kernel × (H\_∂/M̄\_P)²** | **1.244** | ZS-A32 band ≈ 1.244 (O-1) |
| ê₆ \= 2π e^{−4π**Q**} | 5.8294×10⁻⁶⁰ | ZS-F43 conditional value (O-3) |

**Appendix C. Dependency and version-consistency table**

No upstream numerical value is changed by this paper, and no upstream epistemic status is reversed or promoted (guard G6; re-audited against The Book v11.0). ZS-M48 is not a separate paper: this appendix records that its pre-registered content (the parent-factor C\_UV execution) is discharged here as Corollary F44.M48.

Table 5\. Consumed papers.

| Paper | Version | Consumed content | Status consumed |
| ----- | ----- | ----- | ----- |
| ZS-M1 | — | i-tetration z\*, |f'(z\*)| \< 1, ω | PROVEN |
| ZS-M46 | v1.5 | seam standard pair; GLW U(1)-current net; Type III realization (no tracial state) | PROVEN / DERIVED-CONDITIONAL |
| ZS-M47 | v2.0 | parent factor; Parent-Factor Realization Problem; relative commutant Type III | OPEN / DERIVED |
| ZS-F32 | v1.5 | compact odd three-form zero-mode sector; branch spectrum | PROVEN |
| ZS-F33 | — | Charge-Unit Obstruction; flux integrality fixes number not unit | PROVEN |
| ZS-F35 | v1.5 | structural dimensionless factor 36**A**/**Q** \= 1260/4807 | DERIVED-CONDITIONAL |
| ZS-F36 | v2.1 | primitive wrapped-brane charge 1; WZ phase 2 (Smith normal form) | DERIVED |
| ZS-F39 | v1.1 | modular length functor E\_len; C\_UV \= exp(−Γ\_1PI), target ≈ 1.244, band \[1/4,4\] | DERIVED-CONDITIONAL / OPEN |
| ZS-F42 | v1.9 | c\_χ \= 498/(121ω²); F-F42.36; terminal NON-CLAIM on e₆ | DERIVED-CONDITIONAL / NON-CLAIM |
| ZS-F43 | v1.1 | T1/T1′ unit-invisibility; ê₆; the two pre-registered continuations (i)/(ii) | DERIVED / OPEN |
| ZS-A25 | v1.6 | unimodular pair \[Λ̂, T̂₄\] \= iℏ; exactly-one-datum | PROVEN / NO-GO |
| ZS-A31 | v1.5 | M\_eff regression; honest no-go boundary (scale not from dimensionless data) | DERIVED-CONDITIONAL / OPEN |
| ZS-A32 | v1.1 | C\_UV band ≈ 1.244; MC p \= 0.50% (firewalled) | HYPOTHESIS-strong / REGRESSION |

**References**

\[1\] M. H. Stone, On one-parameter unitary groups in Hilbert space, Ann. Math. **33**, 643 (1932); J. von Neumann, Die Eindeutigkeit der Schrödingerschen Operatoren, Math. Ann. **104**, 570 (1931). \[2\] G. W. Mackey, A theorem of Stone and von Neumann, Duke Math. J. **16**, 313 (1949). \[3\] D. S. Freed, G. W. Moore, and G. Segal, The uncertainty of fluxes, Commun. Math. Phys. **271**, 247 (2007); arXiv:hep-th/0605198. \[4\] D. S. Freed, G. W. Moore, and G. Segal, Heisenberg groups and noncommutative fluxes, Ann. Phys. **322**, 236 (2007); arXiv:hep-th/0605200. \[5\] D. S. Freed, Dirac charge quantization and generalized differential cohomology, Surv. Differ. Geom. **7**, 129 (2000); arXiv:hep-th/0011220. \[6\] R. Longo, Index of subfactors and statistics of quantum fields I, Commun. Math. Phys. **126**, 217 (1989); II, ibid. **130**, 285 (1990). \[7\] V. F. R. Jones, Index for subfactors, Invent. Math. **72**, 1 (1983); H. Kosaki, Extension of Jones' theory on index to arbitrary factors, J. Funct. Anal. **66**, 123 (1986); H. Kosaki, AFD factor of type III₀ with many isomorphic index-3 subfactors, J. Operator Theory **32**, 17 (1994). \[8\] H.-J. Borchers, The CPT-theorem in two-dimensional theories of local observables, Commun. Math. Phys. **143**, 315 (1992). \[9\] D. Guido, R. Longo, and H.-W. Wiesbrock, Extensions of conformal nets and superselection structures, Commun. Math. Phys. **192**, 217 (1998). \[10\] M. J. Duff, L. B. Okun, and G. Veneziano, Trialogue on the number of fundamental constants, J. High Energy Phys. **03** (2002) 023; arXiv:physics/0110060. \[11\] H. Araki, Type of von Neumann algebra associated with free field, Prog. Theor. Phys. **32**, 956 (1964) — Type III₁ of chiral nets. \[12\] Z-Spin corpus (K. Kang, 2025–2026): ZS-M1; ZS-M46 v1.5; ZS-M47 v2.0; ZS-F32; ZS-F33; ZS-F35 v1.5; ZS-F36 v2.1; ZS-F39 v1.1; ZS-F42 v1.9; ZS-F43 v1.1; ZS-A25 v1.6; ZS-A31 v1.5; ZS-A32 v1.1.

**Version History**

**v1.1 (July 2026):** Correction-of-record increment responding to external review; the paper's thesis and all three theorems are unchanged, and the corrected argument is *stronger*. The v1.0 Corollary M48 routed the parent-factor non-determination through "Type III₁ ⇒ infinite Jones index ⇒ no trace." That implication is mathematically **false and is retracted**: Type III factors admit finite-index subfactors (Kosaki, J. Funct. Anal. 66, 1986; explicit Type III₀ index-3 examples, J. Operator Theory 32, 1994), and "index" (an inclusion-level quantity) was conflated with "no tracial state" (a factor-level property). v1.1 rebuilds the corollary on the correct, index-independent condition **(H-NOTR)**: a Type III factor has no tracial state (Connes classification, consumed from ZS-M46/M47, not derived here), so Γ\_1PI^parent has no canonical absolute normalizer, and even a finite-index seam inclusion would give only a relative invariant, never the absolute unit C\_UV requires. The verification script drops the jones\_index \= ∞ assumption-encoded check and adds two guards (H-NOTR consumed; no infinite-index claim asserted); checks M48a–M48c are restated at the factor level. Verification 18/18 PASS \+ 9/9 guards (was 18/18 \+ 7/7), fail-closed. Abstract, §1, §3.2, §6 gate F-F44.2, Tables 2–3, dependency table, and Appendix A updated; no upstream value or status moved; the kernel factorization (T3), the firewalled C\_UV \= 1.244, and the ZS-M48 absorption are unchanged. Barrier B3 NOT closed; the parent-factor C\_UV route CLOSED-NEGATIVE under (H-NOTR); ê₆ OPEN; Ω\_Λ,0 \= 83/121 and U\_N untouched.

**v1.0 (July 2026):** Initial public release. Unifies the two continuations pre-registered in ZS-F43 v1.1 §Conclusion — the stand-alone no-go (ZS-F44 branch) and the Parent-Factor Realization Execution (ZS-M48 branch) — by proving the second is a corollary of the first, absorbing ZS-M48 into this paper. Three theorems: T1 (the Charge-Unit Gauge No-Go — the dimensionful charge unit is not an invariant of the compact zero-mode Weyl algebra over ℤ × U(1); general statement IMPORTED-PROVEN via Stone–von Neumann–Mackey, instance DERIVED) with complement T2 (Freed–Moore–Segal / Dirac: flux quantization fixes integer classes, not units); the Corollary M48 (Parent-Factor Non-Determination — the Type III₁ parent factor has infinite Jones index and no trace, so C\_UV's absolute value is undetermined by parent modular data, and no admissible realization fixes C\_UV ∈ \[1.0, 1.6\]; DERIVED-CONDITIONAL on the ZS-M46/M47 realization); and T3 (the Kernel-Factorization Theorem — C\_UV \= \[c\_χ/(1260/4807)·e^{8π**Q**}\]·(H\_∂/M̄\_P)², dimensionless kernel 3.5739×10¹²⁰ times exactly one metric-side datum; value C\_UV \= 1.244 firewalled). Five pre-registered gates F-F44.1–F-F44.5. Verification 18/18 PASS \+ 7/7 guards, fail-closed; 3 firewalled observations. Zero fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. Barrier B3 NOT closed; the parent-factor C\_UV route CLOSED-NEGATIVE; ê₆ OPEN; residual \= single B3-B metric-side datum; Ω\_Λ,0 \= 83/121 and U\_N untouched. ZS-M48 absorbed (no separate paper). (Consolidated from internal Z-Spin Collaboration deep-exploration notes following ZS-F43 v1.1, ZS-F45 v1.4, ZS-F46 v1.3, and The Book of Z-Spin Cosmology v11.0.)  
