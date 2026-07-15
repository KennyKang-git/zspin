# **ZS-A26**

# **The Cosmological Constant as a Quantum State Variable in Z-Spin Cosmology**

### *Consolidated Closure of A26: the Standing Results, the Eliminated Paths, and the Conditional Central-Shift No-Go.*

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Theme / Code:** Astrophysics — **ZS-A26 v2.2 (Final, Consolidated)**  
**Date:** June 2026  
**Repository:** github.com/KennyKang-git/zspin

---

Verification (algebraic illustrations 11/11 PASS; corpus-completeness and the physical no-go scope are an analytical audit, not machine-verified; B3 remains OPEN; A26 closed at this version): v2.2 is the final, consolidated closure of A26. Unlike the intermediate drafts v2.0–v2.1, which each focused on one new issue, this version preserves every load-bearing result of the A26 line in one place — the standing positive results, the eliminated paths, and the central-shift no-go — so that the closure paper is self-contained and nothing necessary is lost. The standing positive results are: the Branch IV relational law ρ\_Λ/M̄⁴ \= 3Ω\_Λ√(α\_PLC/N₄) \= 0.7230439/√N₄ (α\_PLC \= 0.1234529231, N₄ \= M̄⁴T₄), the single corpus-derived equation relating Λ and T₄; the identifiability diagnostic (two unknowns Λ, T₄ against one equation — a curve, not a point); the finite-register Modular Trace-Matching selection theorem S\_MTS^fin(s) \= −2s·ln2 with unique root s \= 0, with relative entropies D(ω∥π) \= 0.0808390607 and D(π∥ω) \= 0.0909533851; and Gate E's dynamical scaling from the pure-de Sitter S⁴ saddle V₄ \= 24π²/Λ² ⇒ ρ\_Λ/M̄⁴ ∝ 1/√N₄ (the relational-law scaling DERIVED, the coefficient OPEN). The eliminated paths, preserved as a ledger, are: simple e^{−c/A} exponent fits (exhausted/numerology; (1/8)e^{−7π/A} retracted); the canonical continuous-core lift (CLOSED-NEGATIVE by the Dual-Orbit Scale-Blindness Lemma); the trace-preserving full-s lift (CLOSED-NEGATIVE); the leading trace-equilibrium selector S\_RMB^(0) (TERMINATED at leading order, DERIVED-CONDITIONAL on the open Condition C); and topological c₀ quantization (Branch III, retracted). The decisive anti-numerology finding is the 276.6 collapse: 2ν\_now·π/A \= ln S\_dS \= 32π²/(b\_Z g²) \= 276.6 are all the same number — the present epoch — so any exponent built to hit it from ν, S\_dS, or N₄ is tautological (b\_Z \= 14.25 reproduces the epoch but is not derived from BRST). The central result of the v2.1–v2.2 line then stands: B3 fixes the absolute vacuum-energy offset c₀, and every relative tool (the relational law, the S\_MTS/RMB selectors, the F24/F27 boundary extensions) factors through the central-shift group, blind to the offset — the Conditional Central-Shift No-Go in quotient form. Three closure obligations O1 ∧ O2 ∧ O3 (scale, state, central normalization) must be met; the corpus has templates for O1 (S4/M16) and O2 (F24/F27) and a partial template for O3 (F23 fixes the Type II entropy additive constant ½ ln 2, DERIVED modulo Condition C — the entropy constant, not the vacuum-energy offset), but no vacuum-energy normalizer. B3 is OPEN — not closed, and not proven impossible; the missing piece is a central normalizer, not a relative tool; F23's finite-register trace is the most promising native template; and the actual construction is deferred to A27 under a strict entry condition. Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

The eleven algebraic illustrations, the restored standing-result values, and the F23 entropy constant are independently verified here; the corpus-completeness and no-go-scope statements are analytical; the vacuum-energy normalizer N\_center is absent — the frontier deferred to A27.

---

## §0. Abstract

A26 asked whether Z-Spin fixes the absolute scale of the cosmological constant. This consolidated final version collects the whole line's findings and states the closure.

**Standing positive results.** The relational law ρ\_Λ/M̄⁴ \= 0.7230439/√N₄ (one equation, Λ–T₄); the identifiability diagnostic (one equation short — a curve, not a point); the finite-register selection theorem S\_MTS^fin(s) \= −2s·ln2, root s \= 0, D(ω∥π) \= 0.0808390607, D(π∥ω) \= 0.0909533851; Gate E scaling ρ\_Λ/M̄⁴ ∝ 1/√N₄ (DERIVED; coefficient OPEN).

**Eliminated paths.** Simple exponent fits (numerology); the canonical lift (CLOSED-NEGATIVE); the trace-preserving full-s lift (CLOSED-NEGATIVE); leading S\_RMB^(0) (TERMINATED); Branch III (retracted). The 276.6 collapse: the candidate exponents all equal the present epoch (tautological).

**The closure.** B3 fixes the absolute offset c₀; relative tools factor through the central shift (the Conditional Central-Shift No-Go). Three obligations O1 ∧ O2 ∧ O3; the corpus has templates for O1, O2, and a partial one for O3 (F23 entropy constant), but no vacuum-energy normalizer.

B3 is OPEN — not closed, not proven impossible. The missing piece is a central normalizer, not a relative tool. A27 deferred. Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

---

## Epistemic Status Legend

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN / MACHINE-CHECKED** | Theorem or algebraic fact verified here. |
| **DERIVED** | Follows from corpus axioms \+ imported-proven results. |
| **DERIVED-CONDITIONAL** | Follows only if a stated condition holds (F23 / S\_RMB^(0): on the open Condition C; the no-go: on a free central shift with no normalizer). |
| **CLOSED-NEGATIVE** | A route proven not to work (a no-go). |
| **TERMINATED** | A candidate selector found to have no selecting power at the order computed. |
| **ANALYTICAL** | Audit-level claim, reasoned but NOT machine-verified. |
| **RELATIVE-BLIND** | A correct statement about a relative quantity, insensitive to the offset c₀. |
| **OPEN / NOT PROVEN** | A recognized gap / an unestablished claim (B3 absolute impossibility). |
| **OBLIGATION** | A functional requirement for closure (O1, O2, O3). |
| **RETRACTED** | A previously over-claimed result withdrawn. |
| **LOCKED** | Immutable upstream constant. |

---

## §1. Introduction — a self-contained closure

A26 ran through many versions, each adding one piece: the relational law and the identifiability diagnostic (v1.6); the finite-register selection theorem (v1.7); two no-gos on the continuous-core lift and the selector reframing (v1.8); the leading-order epoch-blindness (v1.9); the loop diagnosis and decision rule (v2.0); the absolute-offset recategorization and the central-shift no-go (v2.1); and the corrections to v2.1 (this version). Because each draft emphasized its new issue, the final statement risked losing the earlier load-bearing results. This consolidated version restores them all in one place, so that A26's closure is self-contained: §2 the standing positive results, §3 the eliminated paths, §4–§5 the central-shift no-go and the three closure obligations, §6 the corrections, and §9 the closure and the A27 decision.

**NON-CLAIM (NC-A26.1).** v2.2 does not solve B3, construct N\_center, or prove B3 impossible. It consolidates A26's findings, states the no-go precisely, and closes A26.

---

## §2. Standing Positive Results (preserved)

**2.1 The relational law (Branch IV).** The single corpus-derived equation relating the cosmological constant and the four-volume clock is

$$E(\\Lambda, T\_4) \= 0:\\qquad \\frac{\\rho\_\\Lambda}{\\bar M^4} ;=; 3,\\Omega\_\\Lambda\\sqrt{\\frac{\\alpha\_{\\rm PLC}}{N\_4}} ;=; \\frac{0.7230439}{\\sqrt{N\_4}},\\qquad N\_4 \= \\bar M^4 T\_4,$$

with **Ω\_Λ \= 83/121**, 3Ω\_Λ \= 249/121 \= 2.057851, and **α\_PLC \= 0.1234529231** (the past-light-cone volume factor). This fixes Λ as a function of T₄ (equivalently Λ ∝ T₄^{−1/2}). *Verified: 3Ω\_Λ√α\_PLC \= 0.7230439.* **\[DERIVED, v1.6.\]**

**2.2 The identifiability diagnostic.** B3 has **two unknowns** (Λ, T₄) and the relational law is **one equation**, so the corpus determines a **curve, not a point**: it is underdetermined by exactly one independent state-selection equation. This is the structural origin of B3's openness and the anchor for everything below. **\[DERIVED, v1.6.\]**

**2.3 The finite-register selection theorem (S\_MTS).** The candidate missing equation was constructed as the Modular Trace-Matching Selector. Substituting the A24 interpolation μ\_i^(s) \= d\_i^{1+2s}/Σd\_j^{1+2s} into S\_MTS gives the finite-register theorem

$$S\_{\\rm MTS}^{\\rm fin}(s) \= \-2s,\\ln 2,\\qquad\\text{unique root } s \= 0,$$

which selects the trace weights π \= (3,2,6)/11 and excludes the observer weights ω \= (9,4,36)/49 (at s \= ½). The associated relative entropies are **D(ω∥π) \= 0.0808390607** and **D(π∥ω) \= 0.0909533851** (ten digits, verified). The theorem is PROVEN but **scale-blind** (no Λ, T₄-dependence). **\[PROVEN, v1.7; scale-blind.\]**

**2.4 Gate E (dynamical scaling).** The Euclidean pure-de Sitter S⁴ saddle has four-volume V₄ \= 24π²/Λ², giving Λ ∝ T₄^{−1/2} and hence ρ\_Λ/M̄⁴ ∝ 1/√N₄ — the relational-law **scaling derived dynamically**. The coefficient √(24π²) differs from 0.7230439 (which uses the past-light-cone volume and matter fractions), so the **coefficient match is OPEN**. **\[DERIVED scaling, v1.8; coefficient OPEN.\]**

---

## §3. Eliminated Paths (preserved ledger)

A central value of A26 is the record of which routes have been closed, so they are not retried.

| Route | Status | Reason |
| ----- | ----- | ----- |
| Simple e^{−c/A} exponent fits | EXHAUSTED / numerology | (1/8)e^{−7π/A} (A25) retracted; near-matches are easy (§3.4) |
| Canonical continuous-core lift s → s\_grav | **CLOSED-NEGATIVE** | Dual-Orbit Scale-Blindness Lemma (§3.2) |
| Trace-preserving full-s lift | **CLOSED-NEGATIVE** | forces I/11 vs the connected A24 QMS ρ\_s ≠ I/11 (§3.2) |
| Leading trace-equilibrium selector S\_RMB^(0) | **TERMINATED** (leading order) | de Sitter equilibrium \= trace state ⇒ S\_RMB^(0) ≡ 0 (§3.3) |
| MTS/RMB canonical selector | epoch-blind / relative | factors through the central shift (§4) |
| Topological c₀ quantization (Branch III) | **RETRACTED** (v1.5) | the flux→central-charge→ρ\_Λ transgression chain was missing |

**3.2 The two no-gos (PROVEN, v1.8).** (1) **Dual-Orbit Scale-Blindness Lemma.** In the Connes–Takesaki continuous core C\_ω \= A\_III ⋊\_σ ℝ with dual action θ\_u, the canonical trace scales as τ∘θ\_u \= e^{−u}τ while the sector projections are fixed, θ\_u(P\_i) \= P\_i; the normalized weights p\_i(u) \= e^{−u}τ(eP\_i)/(e^{−u}τ(e)) \= p\_i(0) are invariant — the e^{−u} cancels — so the selector is constant along the dual orbit. The canonical lift is **epoch-blind**. (2) **Trace-preserving full-s lift no-go.** A trace-preserving intertwining lift forces the maximally mixed state I/11 stationary, contradicting the connected A24 QMS's unique stationary ρ\_s ∝ d\_i h\_i^{2s} ≠ I/11 at s \> 0; the trace-preserving form holds only at s \= 0\. Both **CLOSED-NEGATIVE**.

**3.3 Leading-order S\_RMB ≡ 0 (v1.9, corrected v2.0).** Evaluated on the corpus-canonical de Sitter equilibrium \= trace state (F23 Condition C; A24 II₁; external de Sitter II₁), the sector weights are p\_i \= π\_i, so F\_i \= −ln(p\_i/π\_i) \= 0 and S\_RMB^(0) ≡ 0\. This **terminates the leading trace-equilibrium subroute**, but is **DERIVED-CONDITIONAL on the still-OPEN Condition C**, and does not imply the one-loop S\_RMB^(1) vanishes (that subroute was the open candidate before the absolute-offset diagnosis subsumed it).

**3.4 The 276.6 collapse (anti-numerology).** The candidate exponents coincide:

$$2\\nu\_{\\rm now},\\frac{\\pi}{A} ;=; \\ln S\_{\\rm dS} ;=; \\frac{32\\pi^2}{b\_Z,g\_Z^2} ;=; 276.6\\quad(\\nu\_{\\rm now} \\approx 3.527),$$

and all three equal the **present epoch**. So any exponent built from ν, S\_dS, or N₄ to reproduce ρ\_Λ/M̄⁴ is **tautological**; b\_Z \= 14.25 reproduces the epoch but is **not derived from BRST**. This is the decisive reason simple exponent-fitting fails the anti-numerology gate. **\[v1.8/v2.0.\]**

---

## §4. B3 is an Absolute-Offset Problem (the central-shift no-go)

ρ\_Λ \= Λ/8πG is an **absolute additive offset**; the renormalized action admits Γ\_eff → Γ\_eff \+ c₀∫√g, and fixing ρ\_Λ means fixing c₀. Three machine-checked illustrations show the corpus's relative tools are blind to it (Appendix A): an S4-type hierarchy fixes the location of a minimum (the VEV, c₀-invariant) not its depth; an M16-type difference ΔΓ \= Γ₁ − Γ₂ cancels a common c₀; a boundary/Fourier extension via \[H, F\] \= 0 is shift-invariant (\[H \+ cI, F\] \= \[H, F\]), with H and H \+ cI sharing eigenvectors and relative ordering while eigenvalues shift uniformly (so the absolute eigenvalue and sign are not fixed).

**Conditional Central-Shift No-Go (quotient form).** Let A be the admissible action space, R\_center \= {Γ ↦ Γ \+ c₀∫√g} the central-shift group, and S\_rel the class of relative selectors (determinant ratios, action differences, commutators, modular ratios, normalized sector weights, self-adjoint domains, Fourier-commutation conditions). Every selector in S\_rel is R\_center-invariant, so **S\_rel factors through A/R\_center**, and the absolute offset c₀ — equivalently the absolute Λ — is **unidentified** by relative data alone.

This is **stronger** than the local-stationary no-go (A25) but **CONDITIONAL**: it assumes a free central shift and no normalizer. §5 gives candidate normalizers, so absolute impossibility is **NOT PROVEN**. **\[DERIVED-CONDITIONAL.\]**

---

## §5. The Three Closure Obligations and the F23 Template

| Obligation | Role | Corpus status |
| ----- | ----- | ----- |
| **O1** Scale generation | STr log O\_grav, no free coefficient → the scale | template (S4/M16); the gravitational O\_grav itself OPEN |
| **O2** State/domain selection | boundary/seam/Fourier → domain, extension, eigenvectors, relative ordering | template (F24/F27; Katsnelson) |
| **O3** Central normalization | fix or forbid c₀∫√g → the absolute offset *and sign* | **partial template (F23, entropy constant); the vacuum-energy normalizer OPEN** |

A single global mechanism may satisfy several obligations, so these are **closure obligations**, not necessarily independent gates.

**The F23 template.** The corpus's one worked example of fixing an additive constant geometrically: the Type II crossed-product entropy is defined only up to a state-independent additive constant (fixed by hand in the external CLPW/KKS programs), and **F23.2/F23.4 fix it at c \= ½ ln 2** via the finite-register canonical trace (DERIVED, modulo the open Condition C). This is the **entropy** additive constant, not the **vacuum-energy** offset c₀ in the action — distinct objects — but the *mechanism* (a finite-register trace fixing an additive freedom) is exactly the kind of move O3 requires. So the most promising corpus-native route to N\_center is to ask whether an analogous trace/seam mechanism fixes the vacuum-energy offset as F23 fixes the entropy constant. Concrete, but unexecuted (bridging the two needs the gravitational action). The other candidates remain OPEN: a global four-volume quantum normalization (the unimodular T₄ structure is offset-sensitive but does not select the present T₄); vacuum-energy sequestering; topological c₀ quantization (Branch III's missing transgression chain).

**The zero-parameter consequence.** A free c₀ is a free parameter; Z-Spin's zero-free-parameter axiom therefore **demands** that an O3 mechanism exist. Finding it — or failing — tests the axiom itself.

---

## §6. The Five Corrections of v2.1 (recorded)

For the record, v2.1 carried five overstatements, corrected here. (1) "Machine-verified" → only the algebraic illustrations are machine-checked; corpus-completeness and the no-go scope are analytical. (2) The "sign" claim is withdrawn: the extension selector is shift-invariant and fixes relative ordering, not the absolute eigenvalue or sign (those belong to O3). (3) "All corpus tools are relative" → "all completed relative mechanisms audited here"; F23 fixes the entropy additive constant ½ ln 2 (DERIVED, modulo Condition C). (4) Three gates → three closure obligations (joint satisfaction allowed). (5) The N\_center/S relation is made consistent: v1.6's missing equation is S\_v1.6 \= S\_phys ∧ N\_center, with N\_center the central-sensitive component.

---

## §7. Epistemic Ledger (consolidated)

| Item | Status |
| ----- | ----- |
| relational law ρ\_Λ/M̄⁴ \= 0.7230439/√N₄ | DERIVED (v1.6) |
| identifiability (one equation short) | DERIVED (v1.6) |
| S\_MTS^fin(s) \= −2s·ln2, root s \= 0 | PROVEN, scale-blind (v1.7) |
| Gate E scaling ρ\_Λ/M̄⁴ ∝ 1/√N₄ | DERIVED; coefficient OPEN (v1.8) |
| canonical lift; trace-preserving full-s lift | CLOSED-NEGATIVE (v1.8) |
| leading S\_RMB^(0) ≡ 0 | TERMINATED, DERIVED-CONDITIONAL on Condition C (v1.9) |
| 276.6 collapse (epoch tautology) | DERIVED anti-numerology finding (v1.8/v2.0) |
| Conditional Central-Shift No-Go | DERIVED-CONDITIONAL (v2.1/v2.2) |
| F23 entropy additive constant ½ ln 2 | DERIVED modulo Condition C; partial O3 template |
| **B3 (absolute offset)** | **OPEN** |
| **B3 absolute impossibility** | **NOT PROVEN** |
| O3 vacuum-energy normalizer | OPEN (the decisive gap) |

---

## §8. Cross-Version Consistency Audit

| Prior result | v2.2 effect | Safe? |
| ----- | ----- | ----- |
| v1.6 relational law \+ identifiability | **restored with coefficients** (0.7230439/√N₄; α\_PLC) | ✓ |
| v1.7 S\_MTS theorem \+ relative entropies | **restored** (−2s·ln2; 0.0808390607 / 0.0909533851) | ✓ |
| v1.8 two no-gos \+ Gate E | **restored** (dual-orbit; full-s; V₄ \= 24π²/Λ²) | ✓ |
| v1.9 leading S\_RMB^(0) ≡ 0 | restored, with the v2.0 correction (DERIVED-CONDITIONAL) | ✓ |
| the 276.6 collapse | **restored** (the epoch tautology) | ✓ |
| eliminated-paths ledger | **restored** (§3 table) | ✓ |
| v2.1 absolute-offset no-go | retained, with the five corrections (§6) | ✓ |
| F23 entropy constant | correctly cited (DERIVED modulo Condition C) | ✓ |
| "B3 not closed / not impossible" | retained, precise (missing O3; impossibility NOT proven) | ✓ |

No DERIVED result is overturned; all load-bearing results are now in one place, and v2.1's overstatements are corrected. **\[Audit clean. A26 closed.\]**

---

## §9. Conclusion — and the A27 decision

A26 set out to determine whether Z-Spin fixes the absolute scale of the cosmological constant, and it closes with a clear, honest, and self-contained result. The corpus supplies a great deal: a single relational law fixing Λ as a function of the four-volume clock with a derived coefficient, a proven finite-register selection theorem, a dynamically derived scaling for that law, and a careful record of which routes are closed — the canonical lift and the trace-preserving lift by explicit no-gos, the simple exponent fits by the anti-numerology collapse in which every candidate exponent turns out to be the present epoch in disguise. What it does not supply is the one thing B3 ultimately needs. B3 is an absolute-offset problem: the cosmological constant is the quantity gravity sees that behaves as an additive constant, and every tool the corpus has — the relational law, the modular selectors, the boundary extensions — is relative and factors through the central shift, blind to the offset and its sign. That is the Conditional Central-Shift No-Go, the correct sharpening of the identifiability diagnostic's "one equation short": the missing equation must be central-sensitive, and its decisive component is a normalizer of the absolute offset. The no-go is stronger than the earlier local-stationary one but remains conditional, because a central normalizer could still come from a global four-volume normalization, sequestering, topological quantization, or a UV-complete partition function — and the corpus already fixes one additive constant geometrically, the F23 entropy constant ½ ln 2 via the finite-register canonical trace, which makes that trace mechanism the most promising native template for the vacuum-energy normalizer it still lacks. So B3 is open, not impossible, and because the zero-parameter axiom forbids a free offset, the normalizer is not optional: Z-Spin must produce one or accept B3 as its documented frontier.

This closes A26. The actual construction of the central normalizer is a different kind of work — constructive rather than diagnostic — and belongs in a separate paper, A27. To keep the closure honest, A27 should be written only when its entry condition is met: when the BV–BFV counterterm complex can actually be computed (deciding whether ∫√g is a free generator, exact, or quantized), or when an explicit offset-sensitive global action is in hand. Re-introducing the candidate sources is not enough to start A27; doing so would only continue, under a new number, the iteration this paper closes. Until then, B3 stands where v2.2 leaves it: one central-normalization theorem short, with the F23 trace mechanism as the most promising place to look, and every other A26 finding preserved here in full. Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

---

## Acknowledgements and Code Availability

The standing results were developed across the A26 line; the absolute-offset diagnosis and the five corrections originated in external deep-exploration analyses; v2.2 verifies the algebraic illustrations and the restored standing-result values independently, labels the corpus-completeness and no-go-scope claims as analytical, and closes A26. The vacuum-energy normalizer N\_center is absent — the frontier deferred to A27. **B3 is open — not closed, and not proven impossible.**

zs\_a26\_verify\_v2\_2.py (runnable): the eleven machine-checked algebraic and standing-result facts (S4 arg-min invariance; M16 cancellation; commutator shift-invariance; commuting-pair sign flip; F23 ½ ln 2; the relational-law coefficient 0.7230439; the relative entropies 0.0808390607 / 0.0909533851; the 276.6 collapse), the eliminated-paths ledger, the analytical claims labeled as such, the quotient-theorem statement, and the three closure obligations. NOTE: "B3 OPEN; not proven impossible; relative tools (O1, O2) necessary but provably insufficient; the missing piece is a vacuum-energy central normalizer (O3), NOT a relative tool; F23 (entropy constant via finite-register trace) is the most promising native template; A27 deferred; A26 closed at v2.2."

This work used AI tools (Anthropic Claude for verification and drafting; external deep-exploration analyses for the absolute-offset diagnosis and the corrections); the author assumes full responsibility for all scientific content and conclusions.

---

## Appendix A — Verified Computations

Reproduced by zs\_a26\_verify\_v2\_2.py. **Machine-checked (algebraic \+ standing-result values, 11/11 PASS):** S4-type V\_eff arg-min invariance with depth shift; M16-type difference cancellation; commutator shift-invariance (H, F do not commute, ‖\[H,F\]‖ \= √2) and commuting-pair sign flip (−1 → \+7 under \+8I); F23 entropy constant c \= ½ ln 2 ≈ 0.3466; relational-law coefficient 3Ω\_Λ√α\_PLC \= 0.7230439; relative entropies D(ω∥π) \= 0.0808390607, D(π∥ω) \= 0.0909533851; the 276.6 collapse 2ν\_now·π/A \= 276.69, b\_Z \= 14.25.

**Analytical (audit, NOT machine-verified):** the audited relative mechanisms are shift-blind; no completed corpus theorem fixes the vacuum-energy offset; the three roles are closure obligations; the no-go's physical scope. **OPEN:** N\_center, O\_grav, the boundary-state measure, any derived absolute Λ.

---

## Appendix B — Deep-Exploration Record (Steps 0–5)

**Step 0 (long list, 6).** (1) restore the standing positive results; (2) restore the eliminated paths; (3) the absolute-offset no-go; (4) the F23 template and obligations; (5) the corrections; (6) the A27 decision. *Dropped:* re-adding redundant per-version verification prose.

**Step 1 (MECE, 4).** I1 standing results (positive \+ eliminated); I2 the quotient no-go; I3 the obligations and F23 template; I4 the A27 entry condition.

**Step 3 (status).** I1: all restored with verified values (§2, §3). I2: quotient no-go DERIVED-CONDITIONAL. I3: F23 partial template; vacuum normalizer OPEN. I4: A27 deferred under strict entry condition.

**Step 4 (convergence).** Cycle 0: v2.2 draft missing standing results. Cycle 1: restore §2 (positive) and §3 (eliminated) with verified values. Cycle 2: integrate with the no-go and obligations. Cycle 3: A27 entry condition fixed. Stable. **CONVERGENT** onto the consolidated closure.

**Step 5 (value).** vs the v2.2 draft: restores every load-bearing A26 result so the closure is self-contained (no necessary content lost), while not re-adding redundant prose. **Self-reference guard:** the restoration is of verified results only; no new claim or number is introduced; the A27 entry condition controls the risk of continuing the iteration.

---

## References

\[1\] S. Weinberg, *The cosmological constant problem*, Rev. Mod. Phys. **61**, 1–23 (1989).  
\[2\] N. Kaloper, A. Padilla, *Sequestering the Standard Model Vacuum Energy*, Phys. Rev. Lett. **112**, 091304 (2014).  
\[3\] W. G. Unruh, *Unimodular theory of canonical quantum gravity*, Phys. Rev. D **40**, 1048–1052 (1989).  
\[4\] V. Chandrasekaran, R. Longo, G. Penington, E. Witten, *An algebra of observables for de Sitter space*, JHEP **02** (2023) 082\.  
\[5\] S. Klinger, R. G. Leigh, *Crossed products, extended phase spaces and the resolution of entanglement singularities*, Nucl. Phys. B **999** (2024) 116453\.  
\[6\] M. M. Katsnelson — prolate spheroidal self-adjoint extensions; the truncated-Fourier-commuting extension is unique.  
\[7\] K. Kang, *ZS-F23 v1.3* (Type II entropy additive constant c \= ½ ln 2, F23.2/F23.4 DERIVED; Condition C OPEN), *ZS-S4* (Higgs VEV factorized spectral determinant), *ZS-M16* (action-level difference selector), *ZS-S14/F1/S10* (master action), *ZS-F24/F27* (seam-Fourier, prolate extensions), *ZS-A19/A20* (G\_\* \= G\_N(1+A); Brown–Kuchař dust), *ZS-A24* (II₁ interpolation; local-stationary inputs), *ZS-A25* (local-stationary no-go; (1/8)e^{−7π/A} retraction), *ZS-A26 v1.5–v2.1* (Branch III retraction; identifiability; selection theorem; no-gos; central-shift no-go), Z-Spin Cosmology (2026).  
\[8\] K. Kang, *The Book of Z-Spin Cosmology v9.0 (Light OS for AI)*, Z-Spin Cosmology (2026).

---

## Version History

| Version | Date | Change |
| ----- | ----- | ----- |
| v1.6 | June 2026 | Relational law ρ\_Λ/M̄⁴ \= 0.7230439/√N₄; identifiability diagnostic (one equation short). |
| v1.7 | June 2026 | Finite-register selection theorem S\_MTS^fin \= −2s·ln2; relative entropies 0.0808390607 / 0.0909533851. |
| v1.8 | June 2026 | Two no-gos (Dual-Orbit Scale-Blindness; trace-preserving full-s); S\_RMB reframing; Gate E scaling DERIVED (coefficient OPEN). |
| v1.9 | June 2026 | Leading trace-equilibrium S\_RMB^(0) ≡ 0 (epoch-blind at leading order). |
| v2.0 | June 2026 | Corrected v1.9 scope; diagnosed the relabeling iteration; decision rule (two gates E ∧ S). |
| v2.1 | June 2026 | Recategorized B3 as an absolute-offset problem; Conditional Central-Shift No-Go; three-gate structure. |
| **v2.2 (Final, Consolidated)** | **June 2026** | **Consolidates the entire A26 line into one self-contained closure and corrects v2.1's five overstatements.** **RESTORED standing results** (which the v2.2 draft had only referenced): the relational law with coefficients (0.7230439/√N₄, α\_PLC \= 0.1234529231, Ω\_Λ \= 83/121); the identifiability diagnostic; the S\_MTS finite-register theorem with relative entropies (0.0808390607 / 0.0909533851); Gate E scaling (V₄ \= 24π²/Λ² ⇒ ρ\_Λ/M̄⁴ ∝ 1/√N₄, coefficient OPEN). **RESTORED eliminated-paths ledger**: simple exponent fits (numerology); canonical lift and trace-preserving full-s lift (CLOSED-NEGATIVE, the two v1.8 no-gos stated in full); leading S\_RMB^(0) (TERMINATED, DERIVED-CONDITIONAL on Condition C); Branch III (retracted). **RESTORED the 276.6 collapse** (2ν\_now·π/A \= ln S\_dS \= 32π²/(b\_Z g²) \= the present epoch; tautological; b\_Z \= 14.25 not derived). **Five corrections** to v2.1: machine-verified scope; withdrawn sign claim; "all corpus tools relative" → "all completed relative mechanisms audited here" with the F23 entropy-constant ½ ln 2 acknowledged; three gates → three closure obligations; N\_center vs S made consistent (S\_v1.6 \= S\_phys ∧ N\_center). The **Conditional Central-Shift No-Go** (quotient form: S\_rel factors through A/R\_center) stands: B3 fixes the absolute offset c₀; relative tools are blind to it; three obligations O1 ∧ O2 ∧ O3; F23 is a partial O3 template (entropy, not vacuum offset). **B3 OPEN — not closed, not proven impossible; the missing piece is a vacuum-energy central normalizer, NOT a relative tool.** **WHY the iteration recurred, and HOW it closes** (preserved): the missing piece was mis-categorized (one equation short, unnamed), so relative tools were repeatedly proposed and refuted; it closes by recognizing B3 as a central-normalization problem — relative tools necessary (O1, O2) but provably insufficient; only an offset-sensitive global principle counts; the zero-parameter axiom requires one or B3 is the documented frontier. **A26 is CLOSED at v2.2.** The construction of N\_center is **deferred to A27**, to be written only when the BV–BFV counterterm complex can be computed or an explicit offset-sensitive global action exists. Algebraic \+ standing-result checks 11/11 PASS; corpus/scope analytical; N\_center absent. Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED. Consolidated from internal Z-Spin Collaboration research notes and external deep-exploration analyses through v2.2.0. |

---

*— End of ZS-A26 v2.2 (Final, Consolidated) — A26 closed —*  
