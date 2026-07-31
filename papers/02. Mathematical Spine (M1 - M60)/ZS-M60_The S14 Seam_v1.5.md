**ZS-M60**

**The S14 Seam \-Transport Dichotomy, the Closure Obstruction, and the Exact ℤ₂-Asymmetry Bound on the Coherence Phase**

*Why no unitary datum closes the seam; why a phase-covariant boundary-holonomy family can carry no anchor divisor; the spectral-measure classification of every QND multiplier; the exact obstruction Im a \= (1/2i)Tr\[(ρ − JρJ)V\]; its sharp lower bound M\* \= 1/(1 \+ ρ\_λ(π)) \= 0.763362818245964 on the seam-ℤ₂ asymmetry any S14 background must carry; and a conditional translation of that bound onto the ZS-A3 Z-bias vacuum doublet*

**Author:** Kenny Kang · **Affiliation:** Z-Spin Cosmology Collaboration  
**Theme / Paper code:** Mathematical Spine — **ZS-M60 v1.5 · TERMINAL-IN-SCOPE**  
**Date:** March 2026 (corpus paper-protocol date)  
**Parent (classification):** ZS-M59 v1.8 TERMINAL-IN-SCOPE · **Parent (event):** ZS-S28 v3.1 TERMINAL · **Parent (gate):** ZS-M54 v2.2 FINAL  
**Corpus freeze:** The Book of Z-Spin Cosmology v12.1; ZS-S14 v2.0; ZS-S28 v3.1; ZS-M54 v2.2; ZS-M56 v1.8; ZS-M57 v1.8; ZS-M58 terminal; ZS-M59 v1.8  
**Companion:** \`zs\_m60\_verify\_v1\_5.py\`, \`requirements.txt\` (hard \`==\` pins), \`RUN.md\` (one command), \`zs\_m60\_ledger\_v1\_5.md\` (the 186-row table, supplementary) — exit 1 on any FAIL, row-count mismatch or missing dependency

**Verification Summary**

**Verification: 186/186 PASS** (97 THEOREM-PROOF · 35 NUMERIC-WITNESS · 34 GUARD · 20 DECLARATION) **| 0 FAIL | Zero Free Parameters.** (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. **A** does not enter this paper's derivations at all; **Q** and dim **Z** enter only through named hypotheses and through the register dimension of the code theorem. v1.4 prints **six** new real-valued constants — the minimal seam-ℤ₂ asymmetry M\* \= 0.763362818245964 and the five ceilings it induces. **Two are dimension-free and unconditional** (Thm M60.34); the other three hold only on a two-dimensional carrier and are **DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT)**, lowered from PROVEN at v1.4 after an audit correctly refused the wider scope. Each carries an **executed** anti-numerology Monte Carlo: 217 formulas, **zero hits at 10⁻³**, p ∈ \[0.21, 0.78\], none promoted (§13). **Every printed constant is independently re-derived by a second route, 24 for 24\.** The v1.1 declaration of an empty target set remains **RETRACTED**.

**What v1.2 corrects**

Two independent external audits of v1.1 were received. Both are upheld in part, both are contested in part, and every finding was re-derived here before being accepted or rejected — no verdict below is adopted on the reviewer’s authority. Three v1.1 statements are **RETRACTED**, and the retractions bought the paper’s strongest result.

*Table 0.0. The load-bearing external audit findings across v1.1–v1.3, and their disposition. Each was independently re-derived before disposition; the full nineteen-item register is Appendix D.1.*

| Finding | Verdict | Disposition |
| ----- | ----- | ----- |
| The status **TERMINAL** overclaims; the seed’s five goals are not all closed. | **UPHELD** | Lowered to **TERMINAL-IN-SCOPE**; §17 scores 2 PROVEN, 2 CLOSED-NEGATIVE, 2 conditional, 2 OPEN. |
| F-M54-16′ CLOSED-NEGATIVE is unconditional, but (F3) provably fails in the physical bulk. | **UPHELD, and the corpus source located** — ZS-M57 §16.3 records the ZS-A3 vacuum at ε \= ±1. | Re-typed **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)**, then **quantified** by Thm M60.23. |
| The v1.1 three-branch classification is not exhaustive. | **UPHELD** | **RETRACTED**; replaced by Thm M60.21, the barycentre classification, which is exhaustive. |
| Nine ledger rows typed THEOREM-PROOF carry a literal true value. | **UPHELD; re-audited, exactly nine confirmed.** | Six executed, three re-typed DECLARATION; Appendix A states that a DECLARATION is not evidence. |
| The fixed-point and non-membership claims are floating-point, not certified. | **UPHELD** | **Krawczyk interval test**: existence *and uniqueness* of z\\\* in a box of radius 10⁻³⁰ (row L8). |
| ZS-S14’s colour sector is representation-theoretically ill-defined. | **UPHELD, re-derived from characters and the Weyl dimension formula.** | Upstream **erratum** (Thm M60.25); ZS-M60 proved insulated (row L7). |
| The exact obstruction is Im a \= (1/2i)Tr\[Δρ\_E V\]. | **UPHELD, independently re-derived** (300 dilations, residual 8.3 × 10⁻¹⁷). | Adopted as Thm M60.22 and used to prove the sharp bound, which neither audit anticipated. |
| The explicit 2- and 3-sector divisor formulas are owed. | **UPHELD — and the audit’s own 3-sector sign is wrong**, in 11 of 11 executed crossings. | Thms M60.27–M60.28; the audit’s 2-sector sign is right and adopted, its 3-sector sign corrected. |
| **The doublet ceilings are asserted for a general ρ\_E but ρ\_E is never shown to live on the doublet.** | **UPHELD, re-derived**: T \= 1 is compatible with purity 1/m, executed at m \= 2, 3, 5, 8\. | **(H-DOUBLET-SUPPORT)** named and gated (F-M60.50); **M60.31–M60.33 lowered PROVEN → DERIVED-CONDITIONAL**; two ceilings **rescued unconditionally** as Thm M60.34. |
| The conclusion still says *one number* while the body says two objects. | **UPHELD** | Removed; **three** inputs are now named. |
| Route S is summarised unconditionally although its theorem is conditional; *physical bridge* overstates a conditional translation. | **UPHELD** | CONDITIONAL restored in every summary; §11A retitled *a conditional translation*. |
| requirements listed minima, not pins; the attached set did not re-run; the ledger is too dense in the manuscript. | **UPHELD** | Hard \`==\` pins, one command in \`RUN.md\`, tested interpreter; the 186-row table moved to \`zs\_m60\_ledger\_v1\_4.md\`. |
| Some rows typed THEOREM-PROOF execute a random or model ensemble; sampling a universally quantified claim is a witness, not a proof. | **UPHELD** | **24 rows re-typed at v1.5**: THEOREM-PROOF falls 121 → **97**, NUMERIC-WITNESS rises 12 → **35**, one row to DECLARATION. The proofs are in the body and Appendix B. |
| Five stale strings conflict with the current status: the §1 TERMINAL claim, the §17 version name, the Code-Availability block, *physically realized*, and *a single number against a single number*. | **UPHELD** | All five corrected at v1.5; no mathematics changed. |
| Repair ZS-S14 before attacking the gate. | **DECLINED, with a theorem as the reason.** | Thms M60.21–M60.24 and M60.34 use **no S14 field content**; the repair is a prerequisite only for the residuals that need it. |

**§0. Abstract**

ZS-M59 closed the classification of the formal Z-Spin QND event and handed its successor four deliverables: derive the seam transport from the ZS-S14 action, construct a closure prescription, construct the θ-family, and decide nonvanishing versus transverse zeros. ZS-M60 executes them and reports that the second deliverable is **impossible within unitary boundary data**, that this impossibility **forces** a re-typing of the other three, and that after the re-typing the dichotomy becomes decidable.  
**The closure obstruction.** The frozen endpoint transport runs from a(0) \= 1 to a(1) \= **λ** with |**λ**| \= 0.891513565776047 \< 1\. A boundary holonomy, a Wilson line, a spin-cover deck transformation and every other gauge-theoretic gluing candidate act on the coherence line as a **unimodular scalar**, and a unimodular scalar cannot equate two numbers of different modulus. Hence **no gauge-derived closure of the seam transport exists** (Thm M60.2). The obstruction is exactly the event's irreversibility: a unimodular closure exists if and only if |**λ**| \= 1, if and only if the Choi rank is one (Thm M60.3), and the closure deficit 1 − |**λ**| \= 0.108486434223953 **is** the subdominant Choi eigenvalue. This disposes of the 4π spin-cover route by proof rather than by type complaint, and it explains, after thirty-one versions of the S-line and eight of ZS-M59, why every closure attempt failed.  
**The forced type reversal.** ZS-M59's template placed the transport loop on the slab parameter s and the divisor base on the holonomy circle 𝕋\_θ. Since s admits no gauge-derived closure while θ is intrinsically a circle, the only realizable assignment is the reverse: **loop \= 𝕋\_θ, base \= the slab interval** \[0,1\] (Thm M60.4). Under it no closure prescription is needed at all, ZS-M59's rigidity theorem survives verbatim over the connected base, and the constant winding is no longer free — it is fixed at s \= 0 by the boundary data alone.  
**The dichotomy, decided on the phase-covariant class.** If the boundary holonomy is a pure gauge copy, an exact conjugation computation gives a(θ,s) \= a(0,s), **θ-free**, so the family is constant and D \= 0 (Thm M60.5). More generally, whenever the holonomy enters only as an overall phase, |a| is θ-independent, the zero set is a union of whole circles, no zero is isolated, and the transversality hypothesis of ZS-M59's divisor calculus **fails identically** (Thm M60.6). The anchor-divisor route is therefore **CLOSED-NEGATIVE on the entire phase-covariant class**, which contains every minimally coupled single-sector transport. Per ZS-M59 §18 this is a complete result, not a failure: intrinsic branch selection along the S14 boundary-holonomy path is impossible.  
**Where a divisor can still live, and its calculus.** Only a genuine boundary superselection with several vortex sectors escapes, and there the transport is the sector series a(θ,s) \= Σ\_N e^{iNθ}a\_N(s) — an **additive** object, outside the multiplicative frozen class of Thm M60.1, where zeros are admissible. Its θ-winding is then, by the argument principle, exactly the number of roots of the sector polynomial P\_s(w) \= Σ\_N a\_N(s)w^N inside the unit disc; the branch field jumps precisely when a root crosses |w| \= 1; and since only the trivial sector survives at s \= 0, **deg D \= n(1)** counts the anchors (Thm M60.9). On an interval base the ZS-M59 bounds halve to \#supp D ≥ V − 1 and ‖D‖ ≥ V − 1, both sharp (Thm M60.10). Consequently (H-CARRIER-11) is re-typed: a **Q**\-valued branch field costs ‖D‖ \= **Q** − 1 \= 10, not 20, and is realized by a degree-(**Q** − 1\) sector polynomial — a falsifiable structural prediction replacing an unmotivated charge count (Thm M60.15, HYPOTHESIS-strong).  
**Zero-free-parameter charge input.** The one physical integer the construction needs is derived, not fitted: because gcd(**X**, **Z**) \= gcd(3, 2\) \= 1, the ZS-U9 hypercharge lattice generated by 1/**X** and 1/**Z** is exactly (1/**XZ**)ℤ \= (1/**Y**)ℤ, reproducing the Standard Model unit 1/6, and the Z-bias field of ZS-S14 §7 then carries integer hypercharge **Y**/**Z** \= **X** \= 3 (Thm M60.7). The admissible anchor holonomies form ℤ\_**X** \= ℤ₃ and act trivially on that transport (Thm M60.8). The covering degree relevant to the seam is therefore **3, not 2**, which independently bars the spinor 4π selector.  
**The carrier and the channel, proved outright.** The odd dimension **Q** \= 11 admits no unital \\\*-representation of M₂ and, by ZS-M56, no seam-graded tensor subsystem — but it does admit an exact **complete-order code**: the ZS-M57 multiplicity-one E-block E \= span{|1⟩, |9⟩} carries a unital completely positive embedding ȷ with a completely positive inverse κ on its range, ȷ(Z) \= |1⟩⟨1| − |9⟩⟨9|, κȷ \= id, and a CPTP encode/recover pair with ℛℰ \= id (Thm M60.11, all residuals exactly 0). The formal **λ**\-dephasing event has an exact pointer-preserving Stinespring realization with a genuinely external two-dimensional environment, ⟨e₁|e₀⟩ \= **λ** exactly, (Z ⊗ I)W \= WZ exactly, minimal because the Choi rank is two (Thm M60.12). The **Q** \= 11 tensor-factor obstruction therefore does not obstruct a code-subspace carrier, and ZS-M56 is preserved rather than bypassed.  
**The reality theorem, and its physical hypothesis.** ZS-M54 M54.8a makes the seam involution exchange the pointer projectors and ZS-M56 M56.20 makes the S14 interaction grading-even, so the reduced one-event map is seam-ℤ₂ covariant and Hermiticity preservation forces its coherence multiplier to be **real** (Thm M60.17) — with no complete positivity, trace preservation, QND property, collision form or single-stage assumption. This lifts ZS-M57’s Real-Multiplier Lemma by removing three of its hypotheses. Its state hypothesis (F3), however, **provably fails in the bulk**: ZS-M57 §16.3 records that the ZS-A3 potential puts the vacuum at ε \= ±1. v1.1’s unconditional CLOSED-NEGATIVE verdict is **RETRACTED**, and what replaces it is stronger than either verdict.  
**The exact obstruction and its sharp bound.** With V \= U₁†U₀ and Δρ\_E \= ρ\_E − J\_Eρ\_EJ\_E, the real part of the multiplier is carried entirely by the ℤ₂-symmetric part of the state and the imaginary part entirely by the odd part:

**Re a \= Tr\[ρ₊V\],   Im a \= (1/2i) Tr\[Δρ\_E V\]**  (Thm M60.22, executed residual 8.3 × 10⁻¹⁷).

Every QND multiplier is the barycentre a \= ∫ z dμ of a probability measure on the unit circle — an **exhaustive** classification (Thm M60.21) that retires the three-branch trichotomy of v1.1 rather than lengthening it. Trace-distance data processing then turns the obstruction into a bound, and minimising the ℤ₂-asymmetry over all measures reproducing **λ** is a linear program with a closed-form value:

**T(ρ\_E, J\_Eρ\_EJ\_E) ≥ M\* \= |1+λ|²/(2(1+Re λ)) \= 1/(2 Re\[1/(1+λ)\]) \= 1/(1 \+ ρ\_λ(π)) \= 0.763362818245964,**

attained by an explicit **two-atom** measure with mass M\* at α \= 2 arctan(Im λ/(1+Re λ)) and mass 1−M\* at π (Thm M60.23; four closed forms agreeing to 1.3 × 10⁻⁵¹, an independent 3600-angle linear program to 3 × 10⁻⁷). The bound is written entirely in frozen data: **ρ\_λ(π) \= 0.309993067644787 is the ZS-S28 harmonic density at the antipode.** In words: **any ZS-S14 background reproducing arg λ must be at least 76.34% ℤ₂-asymmetric in trace distance.**  
**The oldest debt, and an upstream erratum.** ZS-M56 gate F-M56.13 — Route S, deferred through ten versions — is admissible only at the Z-anchor, where ε \= 0 restores the ℤ₂; but a ℤ₂-symmetric phase law has a **real** characteristic function, so Route S is **CLOSED-NEGATIVE-CONDITIONAL** on that symmetry (Thm M60.24). Separately, re-deriving the S14 representation data shows D₃ ≅ S₃ has no distinct second doublet — **H₅ ↓ D₃ \= 1 ⊕ 2 ⊕ 2** — and su(3) has no two-dimensional representation, so ZS-S14 v2.0’s colour clause is void as written (Thm M60.25). ZS-M60 uses only the multiplicity-one D₃-trivial component and is proved insulated.  
**A conditional translation onto a named physical state.** ZS-A3 §2 supplies the Z-bias potential V(ε) ∝ (ε²−1)² with vacua ε \= ±1 and the seam ℤ₂ acting as ε ↦ −ε, so on the vacuum doublet the involution is exchange and T(ρ, JρJ) \= √(n\_y²+n\_z²) \= 2|ρ\_SA| (Thm M60.30). The first consequence needs no further hypothesis and is the sharpest physical statement here: **every state diagonal in the S/A basis — every thermal state, at any temperature — has T \= 0 exactly.** Vacuum degeneracy is not the resource; **vacuum coherence** is.  
**Scope, corrected at v1.4.** Passing from the general ρ\_E of Thm M60.23 to a two-dimensional state requires **(H-DOUBLET-SUPPORT)**, and it cannot be proved by projection: data processing gives T(ᴿρ, ᴿJρJ) ≤ T(ρ, JρJ), the wrong direction. The purity and entropy ceilings are in fact **false** without it — with ℤ₂ swapping two orthogonal m-dimensional blocks, T \= 1 while Tr ρ² \= 1/m, executed at m \= 2, 3, 5, 8\. The v1.3 statuses are therefore **lowered from PROVEN to DERIVED-CONDITIONAL**, and an external audit was right to demand it.  
**What survives unconditionally.** Two ceilings are dimension-free and need no model of the S14 environment at all (Thm M60.34): by Fuchs–van de Graaf, T ≥ M\* forces

**F(ρ\_E, Jρ\_EJ) ≤ √(1−M\*²) \= √(P(P+2))/(1+P) \= 0.645969974317367,   Tr(ρ\_E · Jρ\_EJ) ≤ 1−M\*² \= 0.417277207719580.**

Executed over 400 random involutive pairs in dimensions 2–8 with zero violations. **The ZS-S14 boundary state must be at least this far, in Uhlmann fidelity, from its own seam image — whatever its dimension, purity or structure.** Conditionally on the doublet, one further obtains purity ≥ 0.791361396140210, S ≤ 0.363561460568423 nats (**47.55% below** the ZS-Q7 capacity ln 2), a decoherence budget ln(1+ρ\_λ(π)) \= 0.270021845324850 e-folds, at most **two** phase-carrying Z-cycles under (H-RECIP), and a **phase-dead core** around every Z-anchor, where ZS-A3’s ε(r\_H) \= 0 gives T \= 0 exactly.  
**Terminal status.** Of the five inherited residuals: the carrier and the CPTP realization are **PROVEN**; the gauge closure and the phase-covariant divisor are **CLOSED-NEGATIVE**; Route S is **CLOSED-NEGATIVE-CONDITIONAL** on a ℤ₂-symmetric anchor law; F-M54-16′ is **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)** with the (F3) side quantified; and the S14 θ-family and the physical anchor divisor remain **OPEN** behind a named upstream repair. **Three** inputs remain uncomputed: the grading beyond quadratic order (F2), the seam-ℤ₂ asymmetry of the actual boundary state, and (H-DOUBLET-SUPPORT). Every printed constant has been **independently re-derived by a second route**, 24 for 24\. **Verification 186/186 PASS**, reproducible in one command from hard-pinned dependencies. No S14 process, state or divisor is constructed here; those are assigned to the successors of §17.

**Epistemic Status Legend**

Every load-bearing statement below carries exactly one tag from this table. A tag is part of the claim; quoting a statement without it is a citation error and fires gate F-M60.24.

*Table 0.1. Epistemic Status Legend (ZS-M60 v1.0).*

| Status | Meaning in this paper |
| ----- | ----- |
| **PROVEN** | Complete analytic proof given here; no undischarged assumption. |
| **IMPORTED-PROVEN** | External theorem used at its exact hypotheses, cited, not re-proved. |
| **DERIVED** | Follows from frozen corpus inputs and PROVEN steps; no new parameter. |
| **DERIVED-CONDITIONAL** | Exact under named, falsifiable hypotheses carried in the theorem line. |
| **DERIVED-under-P6** | Derived under the phase-covariance premise (P6) of §5.3 and under nothing else. |
| **VERIFIED** | Reproduced from corpus inputs by the companion script; guards drift, not independent evidence. |
| **TESTABLE** | Well-defined structural prediction with an explicit falsification condition. |
| **HYPOTHESIS-strong** | Multiple converging lines; one identified step of the derivation chain is missing. |
| **BOOTSTRAP-HYPOTHESIS** | Foundational axiom not derivable inside the framework. |
| **CLOSED-NEGATIVE** | A route excluded under stated premises. A complete result, not a failure. |
| **REFORMULATED** | Shown not to be one well-posed question; re-expressed without being answered. |
| **OBSERVATION** | A numerical or structural coincidence recorded without identification. |
| **PROXY** | Finite truncation or finite model; never evidence for the infinite target. |
| **NON-CLAIM / OPEN / RETRACTED** | Outside scope / well-typed unresolved node / shown false, retained with its refutation. |
| **TERMINAL-IN-SCOPE** | The declared classification is complete; named items lie outside it. |

**Ledger rules (inherited from ZS-M59 §0 and extended).** Rows are THEOREM-PROOF, NUMERIC-WITNESS, GUARD or DECLARATION. A claim string asserts only what its computation tests. An "exact" claim may not be certified by a tolerance test. **A theorem may be applied only to objects of the type it quantifies over, and the type check is itself a row** (ZS-M59 §13.5). **New at ZS-M60: a supremum or infimum claim may not be certified by a grid sample.** During construction the fail-closed mechanism fired once on exactly this rule and the closed form replaced the sample; the incident is recorded in Acknowledgements rather than silently repaired. **77/77 PASS is the integrity of a ledger, not the peer review of a manuscript.**

**Scope, pre-registered outcomes, and the construction/comparison firewall**

**0.1 Scope declaration**

Every object below derives either from the **formal** pointer-QND event frozen by ZS-S28 v3.1 — which proved that the declared Whitney/DEC/S14 reduction does **not** select a physical event (0 of 13 fields S14-derived) — or from the **declared** ZS-S14 v2.0 master action read as a boundary-value problem. Nothing here is a statement about the physical ZS-S14 measurement event and no result may be cited as one. The permitted claim forms are: *a boundary-holonomy family of the declared type does, or provably cannot, carry an anchor divisor*; and *the formal target admits, or fails to admit, an exact carrier and realization*.

**0.2 Pre-registered outcomes and what fired**

The successor seed pre-registered six outcomes A–F. They are reproduced verbatim below with their verdicts. A seventh outcome was **not** in the seed's table and is registered here as a post-hoc addition, with that status stated; it is the outcome that actually dominates the paper.

*Table 0.2. Pre-registered outcomes and verdicts.*

| Outcome | Trigger | Verdict in ZS-M60 |
| ----- | ----- | ----- |
| A | D \= 0 and the channel equals the target | **PARTIAL FIRE.** D \= 0 is certified on the phase-covariant class (Thm M60.6); channel equality is not established. |
| B | D ≠ 0 and the channel equals the target | did not fire |
| **C** | D \= 0 and the channel differs | **FIRED at v1.1.** D \= 0 on the phase-covariant class, and the channel provably differs: a graded S14 reduction has a real multiplier while **λ** does not (Thms M60.17, M60.20). |
| D | D ≠ 0 and the channel differs | did not fire |
| E | No canonical closure, or no physical θ-family | **FIRED, and strengthened from "none found" to "none exists"** (Thm M60.2). |
| F | The S14 reduction is not CP, TP or QND | did not fire. The v1.1 closure is stronger: the reduction may be perfectly CPTP **and** QND and still fail, because it fails on the phase. |
| **G (post-hoc)** | **The seed's own type template is unrealizable** | **FIRED.** The loop/base assignment of ZS-M59 cannot be realized on any gauge-derived S14 family; re-typing it is the paper's central move (Thm M60.4). |

**Declaration of post-hoc status.** Outcome G was not pre-registered. It is reported as an outcome rather than as a result precisely so that its post-hoc character is visible in the same table that records the pre-registered ones. No numerical claim rests on it; it is a type statement whose proof (Thm M60.2) is independent of it. **Outcome C, by contrast, was pre-registered and fired at v1.1**, which is the outcome the seed named *physical bridge CLOSED-NEGATIVE; formal target remains valid* — and that is exactly the position this release reports.

**0.3 Construction / comparison firewall**

**Artifact A — formal event, available.** ZS-S28 v3.1 pointer matrix units and pointer observable; formal Kraus/Choi data; multiplier **λ**; the pointed minimal dilation and its harmonic measure; the frozen endpoint path; the eleven-dimensional collision carrier. Status: **FORMAL / TARGET-INSTANTIATED / NOT S14-DERIVED.**  
**Artifact B — physical S14 event, unavailable.** The declared reduction did not select it (ZS-S28 §4.2). Its missing component is named exactly once, in §11.  
**One-way rules, obeyed throughout.** ZS-M60 reads Artifact A and the ZS-S14 declared action. It modifies no ZS-S28 field, feeds nothing backward into ZS-S28 or ZS-M59, and never uses the numerical value of **λ** to select a closure, a code plane, a seam location or a sector. The three theorems that mention **λ** numerically — M60.2, M60.3 and M60.12 — use it as a **frozen input to be reproduced**, never as a target to be approached; and the two theorems that decide the dichotomy — M60.5 and M60.6 — do not mention it at all. The v1.1 closure obeys the same rule in a sharper form: **Theorems M60.16–M60.19 are derived without loading arg** λ**, and arg** λ **is loaded only in the last line of each, to be compared against an already-derived admissible set** ({0, π}, then (π/2)ℤ). Guard rows J1–J3, K22.

**§1. Introduction — the five inherited residuals, and why they are not one calculation**

ZS-M59 v1.8 closed, in scope, the classification of the formal Z-Spin QND event: every self-adjoint logarithm of the event unitary is a measurable integer branch; every branch carries its cyclic measure on a set of Lebesgue measure exactly 2π; the ZS-M46 translation at unit time has alias multiplicity ℵ₀, so the minimal route is closed twice over; alias completions exist for every measurable unit field and none is selected; and the residual is a torsor coordinate — a ℤ-valued field on a circle, invisible to the channel, of which ZS-M57 and ZS-M58 each hold the constant mode.  
It then transferred five items to its successor: (1) derive the seam transport from the ZS-S14 action; (2) construct a closure prescription without external choice, or prove that no canonical closure exists; (3) construct the θ-family from the action; (4) decide nonvanishing versus transverse zeros and, in the latter case, compute the divisor D; and, from ZS-M54 and ZS-M58, (5) close or refute F-M54-16′, the identification Φ\_S14 \= Φ^QND\_{**λ**,Z\_path}.  
These five are not one calculation. They separate into three logically different layers, and conflating them is the failure mode that produced twenty-one retractions in ZS-S28 and seven in ZS-M59:

S14 action → closed family → zero/divisor dichotomy

M₂ pointer system ↔ (complete order) ↔ M₁₁ code → pointer-QND CPTP channel

equality of the S14 reduced process with that channel ⟺ F-M54-16′

The second layer is finite-dimensional and admits explicit proofs; it is discharged completely in §§8–9. The first layer is where v1.0's new content lies — but not in the direction the seed anticipated: the seed expected either a certified nonvanishing family or a certified transversal zero set, and what the calculation returns is that **deliverable (2) is impossible**, and that its impossibility determines the answers to (3) and (4). The third layer was expected to wait on the first. **It does not**: §11 shows that the equality of the third line is decided by a symmetry invariant of the reduced process, so it closes — negatively — without the first layer ever producing that process. That was the basis of the v1.1 TERMINAL claim. After the v1.2–v1.5 audits the correct classification is **TERMINAL-IN-SCOPE**: the third line closes only conditionally, and two of the five inherited residuals remain OPEN behind a named upstream repair.

**1.1 The one-line result**

**A gauge holonomy is unimodular; the seam event is not. Therefore the seam does not close, the loop is the holonomy circle, and a phase-covariant family carries no divisor.**

**The seam involution swaps the pointer branches; a graded reduction therefore has a real multiplier. Therefore the S14 event can carry |λ| and never arg λ, and F-M54-16′ is CLOSED-NEGATIVE.**

Everything else in this paper is either a proof of one clause of those two sentences, an exact construction that they leave untouched, or a declaration of what they do not decide. The first sentence is v1.0 and rests on a modulus inequality; the second is v1.1 and rests on a symmetry. **They share a cause: both failures are the absence of ℤ₂-odd content, which is to say the absence of an anchor** (Cor. M60.18b).

**§2. Frozen inputs and conventions**

**2.1 The frozen data**

All numerical inputs are reproduced from ZS-M1's i-tetration fixed point z\\\* alone; none is re-fitted, and the companion script re-derives each from z\\\* at 50 digits (ledger block A).

z\\\* \= 0.43828293672703211163 \+ 0.36059247187138548595 i,  z\\\* \= i^{z\\\*}

**λ** \= (iπ/2) z\\\* \= f′(z\\\*) \= −0.56641733028546440268 \+ 0.68845322710770213050 i

r \= |**λ**| \= 0.891513565776047,  χ \= arg **λ** \= 2.259249553902599,  μ \= −ln r \= 0.114834624996010

dμ\_**λ** \= ρ\_**λ**(θ) dθ/2π,  ρ\_**λ**(θ) \= (1 − r²)/|e^{iθ} − **λ**|²

Two closed forms are used as THEOREM-PROOF rows and not as grid samples: inf ρ\_**λ** \= (1 − r)/(1 \+ r) \= 0.0573542987937511 and sup ρ\_**λ** \= ρ\_**λ**(χ) \= (1 \+ r)/(1 − r) \= 17.4354847157325. The frozen endpoint transport is

a(s) \= e^{sℓ},  ℓ \= −μ \+ iχ,  a(0) \= 1,  a(1) \= **λ**,  |a(1) − a(0)| \= 1.711032173

nonvanishing and **open**, carrying no θ-index (ZS-M59 §11.2.1, row T1). Its recorded "winding zero" is a statement about the continuous lift of an open path — ZS-M58 layer L2 — and not a loop winding number. ZS-M60 inherits that re-typing unchanged and never applies a closed-loop theorem to it.

**2.2 Geometric inputs, and how little of them is used**

The corpus constants are (**A**, **Q**, dim **Z**) \= (35/437, 11, 2), with sector dimensions (**Z**, **X**, **Y**) \= (2, 3, 6\) and **Y** \= **X** · **Z** (ZS-F5 §4, PROVEN). **A** \= 35/437 does not appear in any derivation in this paper; it is listed only to record that it was available and unused, which is a stronger anti-numerology statement than any Monte Carlo. **Q** \= 11 enters twice: as the register dimension of the code theorem of §8, and as the value count in the re-typed (H-CARRIER-11) of §7.4. dim **Z** \= 2 enters as the target dimension of the code and, through **Y** \= **X** · **Z**, in the hypercharge lattice lemma of §6.

**2.3 Conventions, declared once**

Winding of a continuous nonvanishing map g : S¹ → ℂ^× is the integer (1/2π) times the total increase of a continuous argument. "Transport circle" and "family base" are always named explicitly; the type reversal of §4 changes which is which, and every theorem below states its own base. **The pointer basis {|0⟩, |1⟩} is the ZS-S28 which-path basis and Z \= |0⟩⟨0| − |1⟩⟨1| is Z\_path.** The eleven-dimensional register basis {|0⟩, …, |10⟩} is the ZS-F0 register basis; the two bases are never identified, and the collision of the symbol |1⟩ between them is resolved by context and flagged wherever both occur.

**§3. Theorem M60.1 — Multiplicative Frozen-Data Rigidity**

The seed proposed a bypass: since the frozen objects a(s) \= e^{sℓ}, ρ\_**λ** ≥ (1 − r)/(1 \+ r) \> 0 and the Blaschke factor Θ\_**λ**(z) \= (**λ** − z)/(1 − **λ̄**z) are all nonzero, "every object constructible from Artifact A is nonzero", so D \= 0\. As stated the bypass is **false**: addition manufactures zeros, 1 \+ (−1) \= 0 and e^{iθ} − 1 \= 0 at θ \= 0\. The restriction that repairs it is the correct and useful statement, and it is used twice below — once to certify a class, once to certify that the interesting case lies **outside** that class.  
**Definition 3.1 (the multiplicative frozen class).** Let 𝒜\_mult be the set of continuous maps built from the frozen data by multiplication, exponentiation and inversion of nowhere-zero factors only:

𝒜\_mult \= { c · exp(g) · a^m · ρ\_**λ**^q · Π\_ν Θ\_{**λ**\_ν}^{k\_ν} : c ≠ 0, m, q, k\_ν ∈ ℤ }

**Theorem M60.1 (Multiplicative Frozen-Data Rigidity). \[PROVEN\].** Every element of 𝒜\_mult is nowhere zero. Consequently any continuous **closed** family A : 𝔹 × S¹ → ℂ^× built inside 𝒜\_mult over a connected base 𝔹 has a winding field n(b) \= wind(A(b, ·)) that is **constant**, and its jump divisor is D \= dn \= 0\.  
*Proof.* Each generator is nowhere zero on its domain and the class is closed under products, integer powers of nowhere-zero factors and exponentials; no sum occurs, so no cancellation is available. The winding number is integer-valued and homotopy invariant, hence locally constant in b for a continuous nowhere-zero family; a locally constant integer function on a connected base is constant; the distributional derivative of a constant is zero. (Rows B1–B5.)  
**Three scope statements, each of which was a retracted claim in an earlier draft of this line.** (i) The theorem does **not** imply n \= 0: ZS-M59 Thm M59.24 exhibits two admissible closures of the frozen path with windings 0 and 1, neither meeting the origin, so a closure normalization is needed to fix the constant — and §4 supplies one by changing which circle is closed. (ii) The theorem does **not** say that Artifact A supplies the θ-family; it says what happens *if* a family is supplied inside 𝒜\_mult. (iii) The theorem's contrapositive is the load-bearing use made of it in §7: **a family with a zero is not in 𝒜\_mult**, hence is not multiplicatively frozen, hence must contain a sum — which is exactly what a multi-sector superselection decomposition is.

**§4. Theorem M60.2 — the Seam Closure Obstruction**

ZS-M59 §18 named the closure prescription its successor's decisive deliverable, and Thm M59.24 showed why: the winding of a closed extension of the frozen path is 0 for one closure and 1 for another, so the prescription *is* the datum. ZS-M59 also listed the admissible sources: the boundary gauge transformation, BV–BFV gluing, an action-derived return map, or a proved spin-cover identification. Three of those four are unitary. This section proves that all three fail, for one reason, and that the reason is physical.

**4.1 Statement**

**Theorem M60.2 (Seam Closure Obstruction). \[PROVEN\].** Let a : \[0,1\] → ℂ^× be the frozen seam transport and let the closure be effected by a gluing datum acting on the coherence line as multiplication by a scalar c. If |c| \= 1 — in particular if c is a boundary U(1) holonomy e^{iθ}, a Wilson-line phase, a spin-cover deck factor e^{iα}, or any element of a compact gauge group acting on a one-dimensional charge eigenspace — then the closure condition c·a(1) \= a(0) is **unsatisfiable**, because

|c · a(1)| \= |a(1)| \= |**λ**| \= 0.891513565776047 ≠ 1 \= |a(0)|.

Hence **no unimodular gluing closes the seam transport**, and the boundary-holonomy, Wilson-line and 4π spin-cover routes to a closure prescription are all CLOSED-NEGATIVE. (Rows C1–C2, C6.)  
**Theorem M60.3 (Rank-One Closure Criterion). \[PROVEN\].** A unimodular closure of the frozen seam transport exists ⟺ |**λ**| \= 1 ⟺ the second Kraus weight q \= (1 − r)/2 vanishes ⟺ the event channel Φ^QND\_**λ** has Choi rank one ⟺ the event is reversible. Moreover the closure deficit is exactly the subdominant Choi eigenvalue:

1 − |**λ**| \= 0.108486434223953 \= the second eigenvalue of C(Φ^QND\_**λ**), whose spectrum is {1 \+ r, 1 − r, 0, 0}.

*Proof.* The Choi operator of the qubit dephasing channel with multiplier **λ** has spectrum {1 \+ |**λ**|, 1 − |**λ**|, 0, 0} (row C4, reproducing the ZS-S28 printed spectrum {1.891513565776047, 0.108486434223953, 0, 0}). It has rank one iff 1 − |**λ**| \= 0\. The equivalence with the closure condition is Thm M60.2. (Rows C3–C5.)

**4.2 What this settles, and what it leaves**

**Settled.** ZS-M59 deliverable (2) is answered — in the negative, and with a proof rather than an absence of proof. The seed's Bypass 3, which proposed the corpus 4π spinor double cover as the closure selector and which the seed dropped for want of a typed identification of the 4π variable, is now closed for a reason that no identification could repair: **whatever circle the 4π structure lives on, its deck factor is unimodular.** Gate F-M60.21 is thereby discharged rather than merely declared.  
**Left open, and named.** A closure by a **non-unimodular, action-derived return map** is not excluded. Two candidates remain typed and unbuilt: a BV–BFV gluing operator carrying a genuine Radon–Nikodym factor, and a dissipative Bogomolnyi return along the Z-anchor radial direction, where |Φ| is not constant. Both would have to supply a modulus ratio of exactly |**λ**|, and neither is available in ZS-S14 v2.0 as declared. This is registered as gate F-M60.9 and is the only route by which the ZS-M59 template could be resurrected.

**4.3 The physical reading, stated at exact strength**

The seam fails to close **because the event is irreversible**. A gauge holonomy transports without loss; the Z-Spin QND event loses coherence at rate 1 − |**λ**| per transit, and that loss is precisely the weight of the second Kraus operator. A closed loop of unitary transports cannot reproduce a lossy step, so the object ZS-M59 asked for — a loop whose winding encodes the branch — cannot be assembled from the gauge data of ZS-S14. This is **DERIVED**, and it is an interpretation of Thms M60.2–M60.3 rather than an additional claim; the two theorems stand without it.

**§5. Theorems M60.4–M60.6 — the type reversal and the phase-covariance no-go**

**5.1 The forced re-typing**

ZS-M59's rigidity theorem quantifies over a : 𝕋\_θ × S¹\_s → ℂ, a family of **closed loops in s** indexed by θ, with the divisor D \= dn living on 𝕋\_θ. Theorem M60.2 shows that the s-loop cannot be closed by gauge data. But θ needs no closure prescription at all: a holonomy parameter *is* a circle, being valued in a compact gauge group, and periodicity in it is a fact about the group rather than a choice about the path.  
**Theorem M60.4 (Type-Reversal Theorem). \[DERIVED\].** On any ZS-S14 boundary-value family the only realizable assignment of the two circles is

**transport loop \= 𝕋\_θ (the gauge-holonomy circle, closed by the group);  family base \= \[0,1\]\_s (the slab interval, not a circle)**

and the reversed assignment carries three consequences. **(i)** No closure prescription is required, so ZS-M59 deliverable (2) is not merely negative but **vacated**. **(ii)** ZS-M59 Thm M59.21(1) survives verbatim, because its proof uses only connectedness of the base and \[0,1\] is connected: a continuous nowhere-zero family has constant winding. **(iii)** ZS-M59 Thm M59.21(3) — deg D \= 0 — **does not survive**, because its proof uses single-valuedness around the base circle, and an interval has a boundary. On an interval base, deg D \= n(1) − n(0), which need not vanish.  
**Dependency note, stated so that it cannot be misread as a contradiction.** ZS-M59 Thm M59.19 identifies the residual of the *formal event* as a torsor coordinate under 𝒢 \= L⁰(\[0,2π); ℤ), a ℤ-valued field on the seam phase circle. That theorem is about self-adjoint logarithms of the event unitary and is **untouched** here. What §4–§5 re-type is only the *realization* of a branch field by a seam transport family. The two statements live on different objects and there is no version collision; the cross-paper trace of §14 records the check explicitly.

**5.2 The gauge-copy branch, computed exactly**

**Theorem M60.5 (Gauge-Copy Triviality). \[PROVEN\].** Suppose the boundary parameter θ acts on the reduced pointer map by conjugation with a pointer-diagonal holonomy, U\_θ \= diag(e^{iq₀θ}, e^{iq₁θ}), that is

Φ\_{S14,θ} \= Ad\_{U\_θ} ∘ Φ\_{S14,0} ∘ Ad\_{U\_θ}^†.

Then the transport coefficient is **exactly θ-independent**:

a(θ,s) \= ⟨0| Φ\_{S14,θ}(|0⟩⟨1|) |1⟩ \= e^{−iΔqθ} · e^{+iΔqθ} · a(0,s) \= a(0,s),  Δq \= q₁ − q₀.

*Proof.* U\_θ^†|0⟩⟨1|U\_θ \= e^{iΔqθ}|0⟩⟨1|; the θ \= 0 channel multiplies the coherence line by a(0,s); conjugating back multiplies by e^{−iΔqθ}. The two factors cancel identically, for every Δq ∈ ℤ and every θ. Verified symbolically over real symbols (row D1).  
**Corollary M60.5a. \[PROVEN\].** A pure-gauge θ produces a **constant** family, hence a constant winding field on the base and D \= 0, and no intrinsic selector of any kind. Gate F-M60.8 fires on any presentation of such a family as physical. This is the exact content of the ZS-M59 nonvanishing branch, obtained without a single numerical evaluation.

**5.3 The phase-covariance no-go — the paper's strongest negative result**

Theorem M60.5 is a special case of a much wider statement, and the wider statement is what actually closes the anchor route.  
**Premise (P6) — phase covariance.** The boundary holonomy enters the reduced transport only as an overall phase: there is a continuous Φ : 𝕋\_θ → ℝ/2πℤ with a(θ, s) \= e^{iΦ(θ)} a(0, s) for all θ, s.  
**Theorem M60.6 (Phase-Covariance No-Transversality). \[PROVEN under (P6)\].** Under (P6):  
**(i)** |a(θ,s)| \= |a(0,s)| is independent of θ, so the zero set Z(a) \= 𝕋\_θ × {s : a(0,s) \= 0} is a **union of entire θ-circles**; **(ii)** no zero of a is isolated, and at every zero the Jacobian of (Re a, Im a) is singular in the θ-direction; **(iii)** therefore the transversality hypothesis of ZS-M59 Thm M59.22 — isolated projected degeneracies with nonzero local degree — **fails identically**, and the ZS-M59 divisor calculus is inapplicable to any phase-covariant family; **(iv)** if in addition a(0,·) is nowhere zero — which holds for the frozen path and for every element of 𝒜\_mult — then a is nowhere zero, the winding field is constant, and **D \= 0**.  
*Proof.* (i) is immediate. (ii) if a(0,s₀) \= 0 then a(θ,s₀) \= 0 for every θ, so the zero is not isolated; differentiating a(θ,s₀) ≡ 0 in θ gives a vanishing column of the Jacobian. (iii) M59.22's hypothesis "finite transversal transports whose projected degeneracies are isolated with nonzero local degree" is contradicted by (ii). (iv) is Thm M60.1 with the family base \[0,1\]. (Row D5.)  
**What this closes.** Every minimally coupled single-sector transport is phase-covariant, because minimal coupling multiplies a charged field by a single parallel-transport factor. Hence:

**The anchor-divisor route is CLOSED-NEGATIVE on the entire phase-covariant class of ZS-S14 boundary-holonomy families.**

Per ZS-M59 §18 this is a **complete result, not a failure**: it is a no-go showing that intrinsic branch selection is impossible along the S14 boundary-holonomy path. It also disposes of the seed's Bypass 2 in its strongest form: the bulk Bogomolnyi vortex zero of ZS-F1 §5 may exist, and the seam may even intersect the vortex core, and the transport may still carry no divisor — because what a divisor needs is not a zero but a **transversal** zero, and phase covariance forbids transversality regardless of where the zeros are. The commutative pullback square the seed demanded is not merely unbuilt; under (P6) it cannot be built with a nonzero divisor on the other side.  
**Negative controls executed.** A bulk vortex disjoint from the seam gives no seam divisor (trivially); a seam crossing with cancelling local degrees gives zeros with constant winding (ZS-M59 row C4, inherited); and a phase-covariant family with a genuine zero circle gives a singular Jacobian rather than a degree ±1 crossing (row D5). All three are the seed's mandatory controls 4, 5 and 6\.

**5.4 Theorem M60.29 — the non-unimodular return map, and the exact scope of Theorem M60.4**

Theorem M60.2 excludes **unimodular** gluings. Gate F-M60.9 has always left the non-unimodular route open, so the v1.1 phrasing *the only realizable assignment* overstated Theorem M60.4. It is corrected here in the theorem line, and the open route is made explicit rather than merely named.  
**Theorem M60.29 (GKLS Return Map). \[PROVEN\].** Let the slab dynamics be a time-dependent QND Lindblad generator

ℒ\_s(ρ) \= −(iω(s)/2)\[Z, ρ\] \+ (γ(s)/2)(ZρZ − ρ).

Then the coherence obeys ρ̇₀₁ \= (−γ − iω)ρ₀₁, so

**a(s) \= exp\[ −∫₀ˢ γ(t)dt − i∫₀ˢ ω(t)dt \],**

and a(s\*) \= **λ** holds **if and only if**

**∫₀^{s\*} γ dt \= −log|λ| \= 0.114834624996010,   ∫₀^{s\*} ω dt \= −arg λ \+ 2πk \= −2.259249553902599 \+ 2πk.**

Executed by exact quadrature at forty digits with profiles γ(t) \= μ(1 \+ 0.6cos 2πt) and ω(t) \= −χ(1 \+ 0.9 sin 2πt): **|a(1) − λ| \= 0.0** (rows M11–M13). The resulting map has |a(1)| \= 0.891513565776047 ≠ 1, so it is **genuinely non-unimodular and Theorem M60.2 is untouched** (row M14).  
**Three consequences, stated at exact strength.** **(i)** The v1.1 wording of Thm M60.4 is corrected to: *within unimodular gauge-derived closure data, the only available typing is loop \= T\_θ, base \= \[0,1\]*. **(ii)** The integer k is the ZS-M59 branch torsor reappearing at generator level, which is a pleasing consistency and not a new result. **(iii)** Choosing γ and ω to satisfy two integral constraints is a **fit** — two free functions against two numbers — and by ZS-M56 Thm M56.7 a fitted two-parameter family carries zero evidential content. Gate F-M60.16 fires on any presentation of such a choice as a derivation (row M15).  
**What would make it a derivation, and why it then inherits the bound.** γ and ω must be the Feynman–Vernon kernels of the ZS-S14 bath, γ(t) \= ½∫₀ᵗ⟨{ΔB(t), ΔB(u)}⟩\_c du and ω(t) \= ⟨ΔB(t)⟩ \+ (1/2i)∫₀ᵗ⟨\[ΔB(t), ΔB(u)\]⟩du with ΔB \= B₀ − B₁. Under the seam grading ΔB is **ℤ₂-odd** while B₀ \+ B₁ is **ℤ₂-even**, so the dissipation pairing is odd overall and its expectation in a ℤ₂-symmetric state vanishes identically (rows M17–M18, all residuals exactly 0). **The GKLS route therefore inherits the bound of Thm M60.23 rather than evading it**: a nonzero ∫ω requires a ℤ₂-asymmetric state, and reproducing arg λ requires that asymmetry to reach M\*.  
**Corollary M60.29a (reality holds to all orders). \[PROVEN\].** The reality theorem is not a first-order statement. Executed with **exact matrix exponentials** — not a perturbative truncation — over 60 graded models at three slab durations with ℤ₂-symmetric states, the maximum |Im a| is **3.2 × 10⁻¹⁷** (row M16). Any reading of Cor. M60.22a as *the phase vanishes only to leading order* is therefore wrong, and gate F-M60.40 fires on it.

**§6. Theorems M60.7–M60.8 — the Z-bias charge, derived**

The single physical integer this paper needs is the U(1)\_Y charge under which the seam transport is covariant. It is not fitted; it follows from ZS-U9's hypercharge assignment and the coprimality of two sector dimensions.

**6.1 The lattice lemma**

**Theorem M60.7 (Hypercharge Lattice Lemma). \[DERIVED\].** ZS-U9 Thm 6.1, quoted in ZS-S14 v2.0 Table 2.4, assigns Standard Model hypercharges by the sector formulas a \= −1/**X** and b \= \+1/**Z**, giving

Y(Q\_L) \= a \+ b \= 1/6,  Y(u\_R) \= −2a \= 2/3,  Y(d\_R) \= a \= −1/3,  Y(L\_L) \= −b \= −1/2,  Y(e\_R) \= 2b \= 1,  Y(H) \= Y(Φ) \= b \= 1/2.

Since gcd(**X**, **Z**) \= gcd(3, 2\) \= 1, the subgroup of ℚ generated by 1/**X** and 1/**Z** is exactly (1/**XZ**)ℤ. With **Y** \= **X**·**Z** \= 6 (ZS-F5 §4, PROVEN) this gives

**hypercharge lattice \= (1/Y)ℤ \= (1/6)ℤ,  and the integer charge of a field of hypercharge Y\_f is 6·Y\_f.**

In particular the Z-bias field Φ — the D₃-trivial component of H₅ (ZS-S14 Thm S14.D), with Y\_Φ \= q\_Φ × (1/**Z**) \= \+1/2 (S14.D.4, DERIVED) — carries integer charge

**q\_Φ \= Y\_Φ / (1/Y) \= Y / Z \= X \= 3\.**

*Proof.* The lattice generated by 1/**X** and 1/**Z** is (1/lcm(**X**,**Z**))ℤ \= (1/**XZ**)ℤ when gcd(**X**,**Z**) \= 1\. The remaining charges 2/3, −1/3, −1/2, 1 lie in it and add nothing. Then 6 × (1/2) \= 3 \= **X**. Verified as exact rational arithmetic, rows G1–G4.  
**Anti-numerology, stated before the claim rather than after.** The equality q\_Φ \= **X** is an **algebraic identity**, q\_Φ \= **Y**/**Z** with **Y** \= **X**·**Z**, not a numerical coincidence between two independently measured quantities; no tolerance is involved and no null ensemble is meaningful. It is recorded here as DERIVED for that reason. The re-derivation of the Standard Model hypercharge unit 1/6 from gcd(**X**, **Z**) \= 1 is likewise a theorem about coprime integers given the ZS-U9 assignment, **not** an independent prediction, and gate F-M60.22 fires on any presentation of it as one. (Rows G6.)

**6.2 Anchor holonomy quantization, and the death of the 4π selector**

**Theorem M60.8 (Anchor-Holonomy Quantization). \[DERIVED-CONDITIONAL on the Bogomolnyi vortex sector of ZS-F1 §5\].** Single-valuedness of a charge-q\_Φ field around a Z-anchor core requires the fundamental holonomy parameter α ∈ \[0, 2π) to satisfy e^{i q\_Φ α} \= 1, so the admissible anchor holonomies form the cyclic subgroup

**ℤ\_{q\_Φ} \= ℤ\_X \= ℤ₃ ⊂ U(1),  α\_k \= 2πk/3,  k \= 0, 1, 2,**

on which the charge-**X** transport factor is identically e^{2πik} \= 1\. Hence on the anchor-admissible sector the boundary-holonomy family is **constant**, and Thm M60.6(iv) applies with the strongest possible hypothesis. (Row G5.)  
**Corollary M60.8a (the 4π selector is barred by degree, not by type). \[DERIVED\].** The covering degree relevant to the Z-bias seam transport is q\_Φ \= **X** \= 3, not 2\. A spinor double cover selects among lifts of degree two; it has no action on a degree-three charge grading. Together with Thm M60.2, which bars every unimodular closure regardless of degree, the seed's Bypass 3 is closed twice over. (Row G7.)  
**Scope, stated at exact strength.** Theorem M60.8 is conditional on the anchor being a Bogomolnyi vortex of the charged component, which ZS-F1 §5 declares within its own model and which ZS-S26 Certificate P does **not** promote to a slab-average or transport theorem. The seed's provenance correction on that point is upheld and inherited: Certificate P is a conditional interface reduction carrying an explicit transverse-form-factor retraction, and it is cited nowhere in this paper as evidence for a transport zero.

**§7. Theorems M60.9–M60.10 and M60.15 — where a divisor can still live, and its calculus**

Theorem M60.6 closes the phase-covariant class. By the contrapositive of Thm M60.1, any family that does carry a zero must contain a **sum** — it cannot be multiplicatively frozen. On a gauge boundary problem there is exactly one canonical source of such a sum: a genuine boundary superselection, in which the path integral decomposes over topological sectors weighted by the holonomy.

**7.1 The sector form**

**Definition 7.1 (sector decomposition).** If θ is a genuine boundary superselection label rather than a gauge copy, the closed-time-path kernel splits over vortex-winding sectors N and the transport coefficient is the Fourier series

a(θ, s) \= Σ\_{N ∈ ℤ} e^{iNθ} a\_N(s),   a\_N(s) \= the N-anchor sector amplitude.

This object is **additive**, hence outside 𝒜\_mult, hence not covered by Thm M60.1 — which is precisely why it is the only remaining home for a divisor. It is also automatically 2π-periodic in θ, so the loop is closed with no prescription, as Thm M60.4 requires. **\[DERIVED as the general form; the amplitudes a\_N remain unconstructed. At v1.1 they are no longer gate-critical — §11 decides F-M54-16′ without them — but they remain the object a divisor computation would need.\]**

**7.2 The winding, in closed form**

**Theorem M60.9 (Sector-Polynomial Winding Theorem). \[PROVEN\].** Suppose finitely many sectors contribute, N \= 0, …, M, and write w \= e^{iθ} and the **sector polynomial**

P\_s(w) \= Σ\_{N=0}^{M} a\_N(s) w^N.

If P\_s has no root on |w| \= 1, then the branch field is

**n(s) \= wind\_θ a(s, ·) \= \#{ roots of P\_s inside the unit disc },  counted with multiplicity.**

Consequently: **(i)** n takes values in {0, 1, …, M}; **(ii)** n jumps exactly at those s at which a root crosses |w| \= 1, the jump being the signed number of roots crossing; **(iii)** at s \= 0 only the trivial sector is populated, so P\_0 is a nonzero constant and **n(0) \= 0**; **(iv)** on the interval base, **deg D \= n(1) − n(0) \= n(1)**, which counts the sector roots that have entered the unit disc by the end of the slab and **need not vanish**.  
*Proof.* The argument principle applied to the polynomial P\_s on the unit circle gives wind \= (number of zeros inside) − (number of poles inside) \= number of zeros inside, since a polynomial has no finite poles. Local constancy off the crossing set and the jump rule follow from Rouché's theorem. (iii) holds because a\_N(0) \= 0 for N ≠ 0 when no anchor has yet formed. (iv) is Thm M60.4(iii). Verified against direct unwrapped-argument computation on eight random polynomials of degrees 1–6, all matching exactly (rows E1–E5).  
**Physical reading \[DERIVED, interpretive\].** The anchor divisor is the set of slab times at which a vortex-sector root crosses the unit circle — an **anchor nucleation threshold**, not a spatial coincidence. This replaces the seed's picture of a divisor as a set of phases at which a bulk vortex happens to meet the seam, and it explains why the pullback square the seed demanded was never constructible: the correct pullback is not from bulk positions to seam phases but from sector amplitudes to root moduli.

**7.3 The interval divisor calculus**

**Theorem M60.10 (Interval Divisor Bounds). \[PROVEN\].** Let n : \[0,1\] → ℤ be piecewise constant with jump divisor D \= Σ\_j m\_j δ\_{s\_j} and V \= \#{distinct values of n}. Then

**\# supp D ≥ V − 1  and  ‖D‖ := Σ\_j |m\_j| ≥ V − 1,  both sharp,**

attained simultaneously by the monotone staircase n \= 0, 1, …, V − 1\. These are **exactly half** the ZS-M59 circle bounds \# supp D ≥ V and ‖D‖ ≥ 2(V − 1), and the factor two is not an improvement in analysis but a consequence of the base having a boundary: on a circle the field must return, on an interval it need not. (Rows F1–F3.)  
*Proof.* V distinct values on an interval require at least V − 1 changes, and \#changes \= \#supp D. For the norm, ‖D‖ ≥ |Σ\_j m\_j| is too weak; instead ‖D‖ \= total variation ≥ range \= max n − min n ≥ V − 1 since V distinct integers span a range of at least V − 1\. The staircase attains both with V − 1 unit jumps.  
**What ZS-M59 then supplies for free, and what it does not.** Given a divisor on the interval, ZS-M59 §11.3–11.4 still supplies the minimal admissible field n\_D \= S\_D − min S\_D by the predeclared lift rule S1, the closed-form pairing weight F(θ) \= G(2π) − G(θ), and the ceiling E(D) ≤ E\_min \+ π‖D‖. It does **not** supply the energy formula E(D) \= E\_min \+ 2π\[n₀ \+ Σ\_j m\_j F(θ\_j)\] unchanged, because that formula pairs the divisor against the harmonic measure **on the seam phase circle**, and after the type reversal the divisor lives on slab time. The energy pairing is therefore listed as **OPEN, re-typed** rather than inherited, and gate F-M60.7 fires on any use of the circle formula against an interval divisor. This is the one place where the type reversal costs the corpus a result rather than buying one, and it is recorded as such.

**7.3a Theorem M60.27 — the explicit sector divisor calculus (new at v1.2)**

Theorem M60.9 counts roots; it does not say where they are or how fast they move. For the two lowest sector counts everything is explicit, and an external audit correctly observed that ZS-M60 owed these formulas. They are derived and executed here — and one of the audit’s own formulas is corrected.  
**Two sectors.** With P\_s(w) \= a₀(s) \+ a₁(s)w the unique root is

w\*(s) \= − a₀(s)/a₁(s),   |w\*| \= |a₀|/|a₁|,

so the anchor condition, the anchor angle, the transversality condition and the local degree are

**|a₀(s\*)| \= |a₁(s\*)|,   θ\* \= π \+ arg a₀(s\*) − arg a₁(s\*) (mod 2π),**

**(d/ds) log(|a₀|/|a₁|)|\_{s\*} ≠ 0,   m \= − sgn\[ (d/ds) log(|a₀|/|a₁|) \]\_{s\*}.**

Executed on a family whose modulus ratio crosses at s\* \= 0.473684211: |w\*| \= 1.000000000000, θ\* matches arg w\* to twelve digits, the derivative is −2.299363, and the measured winding jump is **\+1**, agreeing with the formula (rows M1–M5).  
**Three sectors.** With P\_s(w) \= a₀ \+ a₁w \+ a₂w² the roots are w± \= (−a₁ ± √(a₁² − 4a₀a₂))/(2a₂); a crossing is |w±(s\*)| \= 1, it is simple iff ∂\_w P\_{s\*}(w\*) ≠ 0, and implicit differentiation gives the root velocity and the transversality condition

ẇ\* \= − ∂\_s P\_s(w\*) / ∂\_w P\_s(w\*),   Re(ẇ\*/w\*) ≠ 0\.

Since d|w\*|/ds \= Re(ẇ\*/w\*) at |w\*| \= 1, a root **entering** the disc has Re(ẇ\*/w\*) \< 0 and raises the count by one, so

**m \= − sgn Re( ẇ\*/w\* ) \= − sgn Re\[ −∂\_s P\_s(w\*) / (w\* ∂\_w P\_s(w\*)) \].**

**A correction, made by independent verification rather than by deference.** One audit supplied this formula with the opposite sign, m \= \+sgn Re\[−∂\_sP/(w\*∂\_wP)\]. The two differ by exactly one sign, so a single test decides between them. Over **eleven** transversal crossings generated from random three-sector families, the form above is correct in **11 of 11** and the audit’s form in **0 of 11** (rows M6–M7). The audit’s two-sector sign, by contrast, is correct and is adopted unchanged. This is recorded here because a reviewer’s verdict is evidence about a manuscript and not evidence about mathematics.

**7.3b Theorem M60.28 — a fail-closed nonvanishing certificate**

Theorem M60.9’s count n(s) is defined only where P\_s has no root on the unit circle, so a verifier must **certify** inf\_{|w|=1}|P\_s(w)| \> 0 rather than record the argument principle as passed. With P\_s of degree d, the map θ ↦ |P\_s(e^{iθ})| is Lipschitz with constant L \= Σ\_{k≥1} k|a\_k|, so an M-point grid gives the certificate

**inf\_{|w|=1}|P\_s| ≥ min\_j |P\_s(e^{2πij/M})| − Lπ/M,**

and the family is certified nonvanishing when the right-hand side is positive. **\[PROVEN\].** Executed at M \= 4096: a nonvanishing family certifies at 0.69976990, a second at 0.72130445, and the degenerate family a₀ \= a₁ \= 1 — which genuinely vanishes at w \= −1 — returns −0.00076699 and is **correctly refused** (rows M8–M10). The certificate fails closed; it never reports a nonvanishing family that vanishes.

**7.4 (H-CARRIER-11), re-typed**

ZS-M59 §12 registered (H-CARRIER-11) — *the alias fiber is the record index of the eleven-dimensional collision carrier* — as **REFORMULATED, not derived**, observing that an eleven-valued field would require ‖D‖ ≥ 2(**Q** − 1\) \= 20 on the circle, that twenty units of anchor charge is not an eleven-dimensional carrier, and that the map between them had not been built. The type reversal changes the currency and, for the first time, makes the requirement structural rather than arithmetical.  
**Theorem M60.15 (Sector-Degree Re-typing of (H-CARRIER-11)). \[TESTABLE REFORMULATION / HYPOTHESIS-weak — lowered at v1.3\].** On the interval base a **Q**\-valued branch field costs

**‖D‖ \= \# supp D \= Q − 1 \= 10**

attained by the monotone staircase, and by Thm M60.9(i) it is realized **iff** the sector polynomial has degree **Q** − 1 \= 10, that is iff exactly **Q** \= 11 vortex sectors N \= 0, …, 10 contribute. The eleven-dimensional carrier index is then the **sector index**, and the branch field is the count of sub-unit-modulus roots. (Rows F4–F6.)  
**Status, stated against the temptation.** This is **not** a derivation of **Q** \= 11; the statement "a degree-d polynomial admits exactly d \+ 1 possible inside-counts" is a theorem about polynomials and would hold for any d. Given **Q** \= 11 from ZS-F5 §4, it is a **prediction**: the ZS-S14 boundary superselection must have exactly eleven contributing sectors. That prediction is falsifiable, is registered as gate F-M60.23, and is the first form of (H-CARRIER-11) that names an object which could be counted. **Lowered at v1.3 from HYPOTHESIS-strong to HYPOTHESIS-weak**: an audit correctly observed that the anti-numerology Monte Carlo tests the neighbourhood of M\*, not the provenance of an eleven-sector count, so nothing in this paper is evidence for the sector number. What it gains over ZS-M59's form is (a) the currency drops from 20 to 10, (b) the ordering becomes time-ordered rather than phase-scattered, and (c) the carrier index acquires a candidate physical identity. What it does not gain is derivation. Gate F-M60.5 fires on any presentation of Thm M60.15 as DERIVED.  
**Anti-numerology.** The integers 10 and 11 here are a dimension and a dimension minus one; no tolerance, no fit, no ensemble. The one relation that could be mistaken for numerology — that the interval bound is exactly half the circle bound — is proved in Thm M60.10 and is a statement about closed versus bounded one-manifolds.

**§8. Theorem M60.11 — the exact eleven-dimensional complete-order pointer code**

This section and the next are independent of everything above. They discharge the seed's tasks 3 and 4 outright, and they stand whatever the S14 layer eventually returns.

**8.1 Why the tensor-factor no-go does not apply**

A unital \\\*-representation π : M₂ → M₁₁ would decompose ℂ¹¹ into copies of the two-dimensional irreducible M₂-module, giving an even total dimension; 11 is odd, so no such representation exists (row H15). ZS-M56 Thm M56.21′ proves a strictly stronger statement in its own category: with the seam grading J\_R \= I₁₁ − 2|1⟩⟨1| the register's odd multiplicity is q\_R \= 1, while any system-times-environment grading with both environment eigenspaces occupied has odd multiplicity ≥ 2, so **no seam-ℤ₂-preserving tensor subsystem exists in the register**. Neither statement forbids a **code**.

*Table 8.1. Five carrier categories, and the Q \= 11 verdict in each. The last two rows are the content of this section.*

| Category | Requirement | Q \= 11 verdict |
| ----- | ----- | ----- |
| Tensor factor | ℂ¹¹ ≅ ℂ² ⊗ ℋ\_E | impossible (11 is prime, and odd) |
| Unital \\\*-representation | M₂ acts nondegenerately on all of ℂ¹¹ | impossible (dimension parity) |
| Grading-preserving tensor subsystem | ZS-M56 multiplicity condition q\_R ≥ 2 | impossible (q\_R \= 1\) |
| Two-dimensional code | isometry V : ℂ² → ℂ¹¹ | **possible** |
| Complete-order code | ucp embedding with ucp inverse on its range | **possible, and constructed below** |

**8.2 The construction**

Take the ZS-M57 Thm M57.3 multiplicity-one E-block, the unique E-isotypic component of the D₄ decomposition ℂ¹¹ \= 5A₁ ⊕ 4B₂ ⊕ E, located at

E \= span{ |1⟩, |9⟩ } ⊂ ℂ¹¹ — the ℤ₂-odd Z-mode together with its seam image.

Define the isometry V|0⟩ \= |1⟩, V|1⟩ \= |9⟩, so V†V \= I₂ and P\_E \= VV†. Define, with ω₀(X) \= ½ Tr X and any predeclared qubit state τ,

ℰ(ρ) \= VρV†,   ℛ(σ) \= V†σV \+ Tr\[(I₁₁ − P\_E)σ\] τ,

ȷ(X) \= VXV† \+ ω₀(X)(I₁₁ − P\_E),   κ(Y) \= V†YV.

**Theorem M60.11 (Exact Eleven-Dimensional Complete-Order Pointer Code). \[PROVEN\].** ℰ and ℛ are CPTP; ȷ and κ are unital and completely positive; and

ℛ ∘ ℰ \= id\_{M₂},   κ ∘ ȷ \= id\_{M₂},   ȷ(I₂) \= I₁₁,   κ(I₁₁) \= I₂,

**ȷ(Z) \= |1⟩⟨1| − |9⟩⟨9|,   κ(ȷ(Z)) \= Z**  (the exact pointer identity).

Hence ȷ is a **unital complete-order embedding** of the operator system M₂ into M₁₁, the qubit is exactly recoverable from the eleven-dimensional carrier, and the pointer is preserved on the nose. All sixteen verification residuals are **exactly 0.0** in double precision (rows H1–H16), including the four Choi minimum eigenvalues, which are 0 rather than merely non-negative.  
*Proof.* V†V \= I₂ gives trace preservation of ℰ; ℛ is a sum of a compression and a trace-and-replace channel, both CP, with total trace preserved because P\_E \+ (I − P\_E) \= I. ȷ is a sum of a CP map and a positive multiple of a positive operator, hence CP, and ȷ(I₂) \= P\_E \+ (I − P\_E) \= I₁₁. κ is a compression, hence ucp. κȷ(X) \= V†(VXV†)V \+ ω₀(X)V†(I − P\_E)V \= X \+ 0 \= X because V†(I − P\_E)V \= 0\. ℛℰ(ρ) \= V†VρV†V \+ 0 \= ρ. For the pointer, ω₀(Z) \= ½Tr Z \= 0, so the scalar block drops and ȷ(Z) \= VZV†.

**8.3 How the construction evades the obstruction without cheating**

ȷ is deliberately **not** a \\\*-homomorphism: ω₀(XY) ≠ ω₀(X)ω₀(Y) in general, and the executed witness is ‖ȷ(X²) − ȷ(X)²‖\_F \= 3 evaluated on the Pauli X — the Frobenius norm of I₁₁ − P\_E, whose rank is the off-code dimension 9, whose square is the identity (row H14). This is the exact point at which the parity obstruction is avoided: a complete-order embedding is required to preserve **order and unitality**, not products. ZS-M56's multiplicity theorem is untouched, because a code subspace is not a graded tensor subsystem and the register grading is never asked to factor. Gate F-M60.20 fires on any citation of a tensor-factor no-go as a code-subspace no-go.  
**Non-claim NC-M60.1.** The E-block is used as a **code plane**, not as a tensor factor and not as an alias-value quotient. The seed's Bypass 4 — replacing V \= 11 by V \= 3 by counting isotypic types — remains **RETRACTED**: representation labels are not values of an ordered integer field, and no quotient map from physical carrier states onto {A₁, B₂, E} has been constructed. Row J7.

**§9. Theorem M60.12 — exact pointer-preserving QND realization**

**9.1 The target and its minimal external dilation**

The formal QND channel frozen by ZS-S28 is the qubit dephasing map

Φ\_**λ**(ρ) \= \[\[ρ₀₀, **λ**ρ₀₁\], \[**λ̄**ρ₁₀, ρ₁₁\]\],  |**λ**| ≤ 1,  with Φ\*\_**λ**(I) \= I and Φ\*\_**λ**(Z) \= Z.

Let ℋ\_env \= ℂ², a space **external to the register**, and set

|e₀⟩ \= |0⟩,   |e₁⟩ \= **λ̄**|0⟩ \+ √(1 − |**λ**|²)|1⟩,   so ⟨e₁|e₀⟩ \= **λ**,

W|0⟩ \= |0⟩ ⊗ |e₀⟩,   W|1⟩ \= |1⟩ ⊗ |e₁⟩.

**Theorem M60.12 (Exact Pointer-Preserving QND Realization). \[PROVEN for the formal target\].** For every |**λ**| ≤ 1: W is an isometry; the dilation intertwines the pointer exactly, **(Z ⊗ I)W \= WZ**; the partial trace reproduces the target, **Tr\_env(WρW†) \= Φ\_**λ**(ρ)** for every ρ; the channel fixes both pointer projections; and for 0 \< |**λ**| \< 1 the vectors |e₀⟩, |e₁⟩ are linearly independent, so the environment dimension two is **minimal**, equivalently the Choi rank is two. Executed residuals: ⟨e₁|e₀⟩ − **λ** \= 0.0 exactly, (Z ⊗ I)W − WZ \= 0.0 exactly, Tr\_env − Φ\_**λ** \= 0.0 exactly on a full operator basis, W†W − I₂ \= 4.7 × 10⁻¹⁸ (rows I1–I8).  
*Proof.* ‖e₀‖ \= ‖e₁‖ \= 1 and the two system pointer states are orthogonal, so W†W \= I. The intertwining is immediate on basis vectors since W maps each pointer eigenvector to a product with the same pointer eigenvalue. Tracing the environment gives ⟨e\_j|e\_i⟩ρ\_{ij} in the (i,j) entry, that is 1 on the diagonal and **λ**, **λ̄** off it. Minimality: the Kraus rank of a channel equals the rank of its Choi operator, which is 2 for 0 \< |**λ**| \< 1\.

**9.2 Lift to the code, with the leakage state declared**

On encoded states the code channel is Φ̃\_**λ**(VρV†) \= VΦ\_**λ**(ρ)V†, and a CPTP extension to all of M₁₁ is

Φ̂\_**λ**(σ) \= V Φ\_**λ**(V†σV) V† \+ Tr\[(I − P\_E)σ\] · τ\_{E⊥},  τ\_{E⊥} \= (I − P\_E)/9.

The extension is **not unique** outside the code; the maximally mixed leakage state is chosen because it is canonical and because it affects only off-code inputs. **It is not a free parameter and it is not evidence**: it contributes to no theorem, and gate F-M60.19 fires on any use of it in a comparison. (Declared, row J9.)

**9.3 What Theorem M60.12 does not close**

It proves that the target is **realizable** with an external minimal environment satisfying ZS-M56's three constraints — dimension two, non-central grading available, genuine externality. It does **not** prove that ZS-S14 selects it. A Stinespring dilation always exists for a completely positive map; existence is not provenance. Gate F-M60.13 fires on any statement that this section closes F-M54-16′.

**§10. Theorem M60.13 — the fixed-point positivity obstruction, branch-declared**

The seed's Bypass 5 proposed a "positivity wall" argument from the fixed point. The identities are correct **after a branch declaration** and wrong as branch-free statements; they are recorded here in their exact form because ZS-M59 Thm M59.14 depends on the same structure.  
**Theorem M60.13. \[PROVEN, branch-declared\].** Let f(z) \= i^z \= e^{z Log i} with Log i \= iπ/2, and z\\\* the declared fixed point. Then Log z\\\* \= z\\\* Log i \= (iπ/2)z\\\* modulo 2πiℤ, and the multiplier is **λ** \= f′(z\\\*) \= (iπ/2)z\\\*. Therefore

**λ** \= Log z\\\*  **only on the branch for which the integer 2πik vanishes** — the equality is exact after that declaration, not branch-free.

Writing **λ** \= re^{iχ} and μ \= −log r: r \= (π/2)|z\\\*|, μ \= −log|z\\\*| − log(π/2), and χ \= π/2 \+ arg z\\\* \= (π/2)(1 \+ Re z\\\*) modulo 2π on the printed branch. Furthermore μ \= 0 ⟺ r \= 1 ⟺ |z\\\*| \= 2/π, and the actual |z\\\*| \< 2/π gives μ \> 0\. The branch-k Cauchy completion has location χ\_k \= χ \+ 2πk and scale μ, with negative-axis weight

δ\_neg^{(k)} \= (1/π) arctan( μ / χ\_k ) \> 0 for every finite k,  δ\_neg^{(0)} \= 0.016165352868291843,  δ\_neg^{(k)} ↓ 0 as k → \+∞.

**What is genuinely proved, and what the seed over-attributed.** The obstruction follows from **strict contraction alone**: |**λ**| \< 1 ⟹ μ \> 0 ⟹ δ\_neg^{(k)} \> 0 on every finite branch. The additional description χ \> π/2 follows from the chosen fixed-point quadrant but is **not the cause**: any Cauchy law with positive location and nonzero scale has a negative tail. Rows A1–A2, A6 and the ZS-M59 row for δ\_neg are consistent to their last printed digits.  
**Bost–Connes: HYPOTHESIS-weak, appendix only.** The limit k → ∞ does not construct a Bost–Connes system. Such a system requires a specified C\\\*-algebra, a semigroup action, a time evolution, a KMS condition, a state and a partition function; a branch index supplies none of them. The label is refused here, not deferred. Gate F-M60.18; row J8.

**§11. Theorems M60.14–M60.20 — the seam-ℤ₂ reality theorem, and the terminal closure of F-M54-16′**

**11.1 The gate, decomposed**

F-M54-16′ asks whether Φ\_S14 \= Φ^QND\_{**λ**, Z\_path}. ZS-M54 v2.2 splits it into sub-conditions **(A)** the reduced ZS-S14 **Z**–environment slab is Z\_path-QND, and **(B)** its coherence multiplier is exactly **λ**. ZS-M58 §13.4 decomposes the proof order into six steps. ZS-M60 v1.0 reported the status of each and left step 1 — construct C\_S14 — as the single unavailable object. v1.1 shows that **step 1 need not be executed**, because sub-condition (B) is decided by a symmetry invariant of C\_S14 that is available without constructing it.

*Table 11.1. The six ZS-M58 §13.4 steps, and their status after ZS-M60 v1.1.*

| Step | Content | Status after ZS-M60 v1.1 |
| ----- | ----- | ----- |
| 1 | Construct the Lorentzian one-event CTP process and obtain C\_S14 | **NOT NEEDED FOR THE GATE.** Still unconstructed; but its seam-ℤ₂ covariance class is fixed by ZS-M54 M54.8a and ZS-M56 M56.20, and that class decides (B). |
| 2 | Decompose by holonomy charge | **DERIVED.** The grading is the U(1)\_Y charge grading, with integer unit fixed by Thm M60.7. |
| 3 | Prove QND from a conserved current | **NO LONGER LOAD-BEARING.** Thm M60.17 needs no QND. Whether or not (A) holds, (B) fails. |
| 4 | Fix the pointer, not merely a pointer (condition P) | **SUPPLIED on the code** by Thm M60.11; its S14 provenance is moot once (B) fails. |
| 5 | Charge-one Ward identity a\_S14 \= Df^{1/4}(z\\\*) | **CLOSED-NEGATIVE.** Df^{1/4}(z\\\*) \= **λ** is not real; a\_S14 is (Thm M60.17). |
| 6 | Compare only at the end | **EXECUTED, and only at the end.** The admissible phase sets {0, π} and (π/2)ℤ are derived first; arg **λ** is loaded afterwards and compared once. |

**11.2 The reality theorem and the exhaustion of its escapes**

Two corpus facts are prior to ZS-M60. **(F1)** ZS-M54 Lemma M54.8a places J\_seam and Z\_path on the seam register as **anticommuting** observables, and ZS-M56 M56.21′ records the same as *Z\_path is odd under J\_S*; an involution anticommuting with Z\_path exchanges its eigenprojectors, J P₀ J \= P₁ (rows K1–K2, both exactly 0). **(F2)** ZS-M56 Thm M56.20 requires H\_int to be even under J\_S ⊗ J\_E — **DERIVED at the symmetric quadratic background, DERIVED-CONDITIONAL to all orders**, a strength ZS-M60 inherits and carries in every theorem line below. **(F3)** the initial boundary state is grading-invariant.  
**Theorem M60.16 (Covariance). \[DERIVED-CONDITIONAL on (F2), (F3)\].** If \[U, J\_S ⊗ J\_E\] \= 0 and \[ρ\_E, J\_E\] \= 0 then Φ ∘ Ad\_{J\_S} \= Ad\_{J\_S} ∘ Φ. *Proof.* J\_S X J\_S ⊗ ρ\_E \= (J\_S⊗J\_E)(X⊗ρ\_E)(J\_S⊗J\_E) by (F3); commute U through and use Tr\_E\[(I⊗J\_E)Y(I⊗J\_E)\] \= Tr\_E Y. Executed over 200 graded dilations, max residual 1.9 × 10⁻¹⁴ (row K3).  
**Theorem M60.17 (Reality). \[PROVEN, given M60.16\].** Let Φ be Hermiticity-preserving with Φ ∘ Ad\_J \= Ad\_J ∘ Φ and J P₀ J \= P₁. Then a\_S14 \= ⟨0|Φ(|0⟩⟨1|)|1⟩ is **real** — with **no** complete positivity, trace preservation, QND property, collision form or single-stage assumption. *Proof.* Covariance gives Φ(|1⟩⟨0|) \= JΦ(|0⟩⟨1|)J; the ⟨1|·|0⟩ element of the left side is ā by Hermiticity and of the right side is a.  
**Executed and non-vacuous.** Over 200 random ℤ₂-covariant CPTP maps, max |Im a| \= **2.8 × 10⁻¹⁵** while the same draws are strongly non-QND, ‖Φ(Z)−Z‖ ∈ \[0.189, 2.782\] — the conclusion is demonstrably independent of QND (rows K4–K5). With the covariance projection removed the control reaches |Im a| \= 0.631 (row K6). In the Pauli transfer representation, Hermiticity makes T real and covariance makes it commute with diag(1,1,−1,−1), so T is block diagonal on {I, σ\_x} ⊕ {σ\_y, σ\_z} and a \= (T₁₁+T₂₂)/2 ∈ ℝ; adding QND makes the **entire Choi matrix real** (rows K7–K9). **Relation to ZS-M57 M57.P:** that lemma assumed a single graded QND collision with a grading-invariant carrier; Thm M60.17 is its lift with three hypotheses removed.  
**Theorem M60.18 (Escape Collapse). \[PROVEN\].** Each item of ZS-M57 Cor. M57.P.1 either fails to escape or reduces to breaking the seam ℤ₂. A one-sided pointer-diagonal phase layer Ad\_U with U \= diag(1, e^{iφ}) carries multiplier e^{−iφ} but has covariance obstruction exactly **2i sin φ** on the |1⟩⟨0| slot, so it is covariant **iff φ ∈ {0, π}** (rows K10–K11) — a phase layer *is* a ℤ₂ breaking, and if it is not, it contributes nothing. This is the origin of ZS-S28’s finding that its two exact sectors quantise the argument to {0, π}. A symmetry-breaking carrier state violates (F3) and a grading violation violates (F2), both by definition. Multi-stage does not escape: covariance is closed under composition, executed at residual 9.5 × 10⁻¹⁶ with composite |Im a| \= 1.9 × 10⁻¹⁷ (row K12); and QND was never used.  
**Corollary M60.18b (one cause behind two no-goes). \[DERIVED\].** §5 shows the phase-covariant class carries no anchor divisor; §11 shows the ℤ₂-symmetric class carries no phase. Both are characterised by the absence of ℤ₂-odd content, and the corpus’s only ℤ₂-odd background object is the Z-anchor. Moreover a ℤ₂-symmetric sector series has a\_{−N} \= ā\_N, hence is real-valued in θ, hence its zeros carry local degree zero: **the same class fails both tests at once.**

**11.3 The quarter-turn deficit**

**Theorem M60.19 (Quantization Deficit). \[PROVEN; hypothesis narrowed at v1.2 to** pure **conjugation by a finite-order element\].** If the ℤ₂ breaking is conjugation by a group element of order n, the induced multiplier phase lies in (2π/n)ℤ. For the corpus register the element is the ZS-M57 quarter turn r \= J·J\_Z of order **four** on the multiplicity-one E-block, giving (π/2)ℤ. The fixed-point branch identity arg z\\\* \= (π/2)Re z\\\*, verified at residual 1.3 × 10⁻⁵¹, gives

**χ \= π/2 \+ Im λ \= (π/2)(1 \+ Re z\\\*),   χ/(π/2) \= 1.4382829367270321 ∉ ℤ,**

dist(χ, (π/2)ℤ) \= **Im λ \= 0.688453227107702130** (rows K13–K17).

No combination of seam involutions and register quarter turns generates arg **λ**, and the entire imaginary part of the multiplier is the deficit. The exclusion is executed for every n ≤ 24 with margin 0.034; **a proof for all finite n would need the irrationality of Re z\\**\*, which the corpus does not have, so the theorem is scoped to n \= 4 and the gap is registered as gate F-M60.30 rather than passed over.

**11.6 Retraction of the v1.1 trichotomy, and what replaces it**

**RETRACTED \[v1.1 Theorem M60.20, Table 11.2\].** *“Exactly three cases are possible for the ZS-S14 one-event background”* — unbroken ℤ₂, breaking by the register’s order-four quarter turn, breaking by a continuous fitted boundary datum. The enumeration is **not exhaustive**: it omits infinite-order unitaries, non-group-theoretic dynamical phases, asymmetric boundary states, sector interference and stochastic phase processes. The verdict it supported — F-M54-16′ CLOSED-NEGATIVE, unconditionally — is therefore withdrawn. **v1.1 Theorem M60.19 is not retracted**, but its hypothesis is narrowed in its own theorem line to *pure conjugation by a finite-order element*, which is where its proof lives; its use inside the trichotomy exceeded that hypothesis.  
What replaces the enumeration is not a longer list but a classification that admits no list at all.

**11.7 Theorem M60.21 — the spectral-measure classification**

**Theorem M60.21 (Barycentre Classification of QND Multipliers). \[PROVEN\].** Let the one-event evolution be pointer-controlled, U \= P₀ ⊗ U₀ \+ P₁ ⊗ U₁ — the exact form of a Z\_path-QND dilation (ZS-M54 Thm M54.22, commutant equivalence). Put V \= U₁†U₀, a unitary on ℋ\_E, and let E\_V be its spectral measure. Then

**a\_S14 \= Tr\[ρ\_E V\] \= ∫\_T z dμ(z),   μ(·) \= Tr\[ρ\_E E\_V(·)\] a probability measure on the unit circle.**

Consequently: **(i)** the achievable set of multipliers is exactly the closed unit disc, and |a| \= 1 iff μ is a point mass; **(ii)** the classification is **exhaustive** — it covers finite-order symmetries, infinite-order unitaries, continuous holonomies, asymmetric states, stochastic phases, sector interference and any non-group-theoretic effective dynamics, because every one of them enters only through μ; **(iii)** ZS-M57 Route S is the commutative special case, with μ the classical phase law. Executed over 200 random pairs (ρ\_E, V) in dimensions 2–6: max |Tr\[ρV\] − Σμ\_k z\_k| \= 8.3 × 10⁻¹⁶ (row L10).  
**Corollary M60.21a (the reality theorem, restated on the measure). \[PROVEN\].** Under (F1)–(F3) one has V† \= J\_E V J\_E, hence E\_V(Ā) \= J\_E E\_V(A) J\_E, hence μ(Ā) \= μ(A): the spectral measure is **invariant under complex conjugation**, so ∫ Im z dμ \= 0 and a is real. This is Theorem M60.17 with its mechanism exhibited: reality is conjugation-symmetry of a measure, not an accident of matrix elements. (Row L11; proof in Appendix B.10.)

**11.8 Theorem M60.22 — the exact ℤ₂-obstruction formula**

The hypothesis that fails physically is (F3), not (F2): ZS-M56 M56.20 grades the *dynamics*, while ZS-M57 §16.3 records that the ZS-A3 potential V(ε) ∝ (ε²−1)² puts the vacuum at ε \= ±1, so the *state* breaks the ℤ₂ in the bulk. That is precisely the regime in which an exact formula is available.  
**Theorem M60.22 (Exact Obstruction). \[PROVEN\].** Let \[U, J\_S ⊗ J\_E\] \= 0 (F2) with J\_S exchanging the pointer projectors (F1), but let ρ\_E be arbitrary. Write ρ₊ \= (ρ\_E \+ J\_Eρ\_EJ\_E)/2 and Δρ\_E \= ρ\_E − J\_Eρ\_EJ\_E. Then V† \= J\_EVJ\_E, Tr\[Δρ\_E V\] is **purely imaginary**, and

**Re a\_S14 \= Tr\[ρ₊ V\],    Im a\_S14 \= (1/2i) Tr\[Δρ\_E V\].**

The real part is carried entirely by the ℤ₂-symmetric part of the state and the imaginary part entirely by the ℤ₂-odd part. *Proof.* From U₁ \= J\_EU₀J\_E follows V† \= J\_EVJ\_E, so conj(Tr\[ΔρV\]) \= Tr\[Δρ J\_EVJ\_E\] \= Tr\[J\_EΔρJ\_E V\] \= −Tr\[ΔρV\]; and ρ₊ is a ℤ₂-invariant state, so Tr\[ρ₊V\] is real by Cor. M60.21a. Executed over 300 random graded dilations in dimensions 2–6: max |Im a − (1/2i)Tr\[ΔρV\]| \= **8.3 × 10⁻¹⁷**, max |Re Tr\[ΔρV\]| \= 6 × 10⁻¹¹ (rows L12–L13).  
**Corollary M60.22a (first-order form). \[PROVEN\].** With H\_int \= |0⟩⟨0| ⊗ B₀ \+ |1⟩⟨1| ⊗ B₁ and B₁ \= J\_EB₀J\_E,

Im a(s) \= −(s/2) Tr\[ Δρ\_E (B₀ − B₁) \] \+ O(s²)   (row L25, residual 4 × 10⁻¹³).

**The coherence phase is, to first order, the pairing of the ℤ₂-odd part of the boundary state with the branch energy splitting.** If the state is symmetric the pairing vanishes identically, which is the reality theorem again, now visible as a cancellation of a mean rather than as an algebraic identity.

**11.9 Theorem M60.23 — the sharp ℤ₂-asymmetry bound, in closed form**

**Step 1, the crude bound.** Trace-norm duality gives |Tr\[Δρ V\]| ≤ ‖Δρ‖₁ for unitary V, so with T := T(ρ\_E, J\_Eρ\_EJ\_E) \= ½‖Δρ\_E‖₁,

|Im a\_S14| ≤ T   (row L14, executed with equality-side margin ≤ 0 in 400 draws).

**Step 2, the sharp bound.** By Thm M60.21 the multiplier is a barycentre ∫ z dμ, and by data processing for trace distance \[Ruskai; Nielsen–Chuang\] the measurement ρ ↦ μ is a positive trace-preserving map, so T ≥ TV(μ, μ̌) where μ̌ is the conjugate-reflected measure. Minimising TV(μ, μ̌) over all probability measures on the circle with ∫ z dμ \= **λ** is a linear program, and it has a closed-form value.  
**Theorem M60.23 (Minimal Seam-ℤ₂ Asymmetry). \[PROVEN\].** Any seam-graded ZS-S14 one-event reduction whose coherence multiplier equals **λ** requires a boundary state satisfying

**T(ρ\_E, J\_E ρ\_E J\_E) ≥ M\* \= |1+λ|²/(2(1+Re λ)) \= 1/(2 Re\[1/(1+λ)\]) \= 1/(1 \+ Re\[(1−λ)/(1+λ)\]) \= 1/(1 \+ ρ\_λ(π))**

**M\* \= 0.763362818245963536495696055558,   ρ\_λ(π) \= 0.309993067644787320905696145842.**

The bound is **sharp**: it is attained by the two-atom measure

μ\* \= M\* · δ\_α \+ (1 − M\*) · δ\_π ,   α \= 2 arctan( Im λ / (1 \+ Re λ) ) \= 2.017516299381013,

which reproduces **λ** to 1.9 × 10⁻⁵¹ and has TV(μ\*, μ̌\*) \= M\* exactly (rows L18–L19). *Proof.* Split μ into even and odd parts about φ ↦ −φ; TV(μ,μ̌) \= ∫|odd part|; the even part must supply Re **λ** and the odd part Im **λ**; optimising the trade-off between an atom pair at ±α and a fixed atom at π gives tan(α/2) \= Im λ/(1+Re λ), at which the −α atom acquires exactly zero mass, and substituting yields the closed form. Full computation in Appendix B.11.  
**Four independent confirmations.** The four closed forms agree to **1.3 × 10⁻⁵¹** at fifty digits (rows L16–L17); the explicit optimal measure reproduces **λ** to 1.9 × 10⁻⁵¹; a linear program over 3600 grid angles, run independently of the closed form, returns 0.7633628… agreeing to **3 × 10⁻⁷** with O(N⁻²) grid convergence (row L20); and M\* strictly exceeds the crude bound Im **λ** \= 0.688453227108 by 0.074909590738, confirming that the sharp bound is a genuine improvement rather than a restatement (row L21).  
**Reading, stated at exact strength.** T ≤ 1 always, and T \= 1 exactly when ρ\_E and its seam image have orthogonal supports. So the theorem says: **the ZS-S14 boundary state must be at least 76.34% of the way to complete seam-ℤ₂ orthogonality.** Two consequences are immediate and both are falsifiable. **(a)** A ℤ₂-symmetric mixture of the two ε \= ±1 vacua has T \= 0 and gives Im a \= 0 exactly: **vacuum degeneracy is not enough; the phase requires vacuum //selection//.** **(b)** A weakly broken vacuum, T \< M\*, is excluded outright — this is the first quantitative constraint the corpus has ever placed on the ZS-S14 boundary state, and it is the “one number” that ZS-M57 §14 records ZS-Q19 as owing.

**11.10 Theorem M60.24 — Route S, the oldest debt, closed**

ZS-M56 gate F-M56.13 and ZS-M57 §16 ask for a classical phase law whose characteristic function is **λ** — a route no multiplicity argument reaches, because classical phase noise needs no tensor factor. It has been deferred through ten consecutive versions. It closes here as a corollary.  
**Theorem M60.24 (Route S Dichotomy). \[DERIVED; branch (a) CLOSED-NEGATIVE-CONDITIONAL on a ℤ₂-symmetric anchor fluctuation law\].** ZS-M57 §16.3 establishes that the admissibility of the noise vertex ξ·Z\_path requires ξ to be ℤ₂-odd, which holds **only at the Z-anchor**, where ε \= 0 restores the seam ℤ₂ (ZS-A3 §2: ε(r\_H) \= 0 at the anchor, the vortex core). Then:  
**(a) At the anchor, where Route S is admissible:** **if** the fluctuation law of δε about the symmetric point is invariant under δε ↦ −δε — which holds for the Gibbs or ground state of the restored-ℤ₂ Hamiltonian but **is not forced by the symmetry of the potential alone**, since a non-equilibrium or externally selected boundary state may break it (an audit correctly insisted on this, gate F-M60.43) — then the induced phase law satisfies p(φ) \= p(−φ) and

E\[e^{iφ}\] \= E\[cos φ\] ∈ ℝ,   hence ≠ **λ**,  since Im **λ** \= 0.688453227107702 ≠ 0\.

Executed over 200 randomly generated symmetric laws: max |Im E\[e^{iφ}\]| \= 1 × 10⁻¹⁷ (row L23). **(b) In the bulk, where the law is asymmetric:** ZS-M57 §16.3’s own charge argument fails — the vertex is no longer ℤ₂-even — and in addition the law must satisfy TV(p, p̌) ≥ M\* by Thm M60.23. **Route S is therefore CLOSED-NEGATIVE-CONDITIONAL in its admissible form** (conditional on the ℤ₂-symmetric anchor fluctuation law of branch (a)), and in its inadmissible form it is both unlicensed and quantitatively constrained.  
**Comparison with the corpus targets.** ZS-M57 Table 16.1 offers two measures reproducing Φ^QND exactly: a two-point law at {χ, χ+π} and a Gaussian N(χ, 2μ). Both have TV(p, p̌) ≈ 1, comfortably above M\* — as they must be — and both are ℤ₂-asymmetric, which is exactly why ZS-M57 could not derive either from the anchor. The bound explains the failure rather than merely recording it. (Row L22.)

**11.11 Theorem M60.25 — an upstream erratum to ZS-S14 v2.0**

The computation of §11.9 needs no S14 field content, but the *other* two open residuals do, and re-deriving the S14 representation data exposed a defect that must be reported.  
**Theorem M60.25 (ZS-S14 Colour-Block Erratum). \[PROVEN\].** **(i)** D₃ ≅ S₃ has exactly three irreducible complex representations, of dimensions 1, 1 and 2 (1²+1²+2² \= 6); **there is no distinct 2′.** **(ii)** Restricting the A₅ five-dimensional irrep, whose character is (5, 1, −1) on the classes (e, order-2, order-3), and applying character orthogonality over D₃:

m\_1 \= (1/6)(5 \+ 3·1 \+ 2·(−1)) \= 1,  m\_{1′} \= (1/6)(5 − 3 − 2\) \= 0,  m\_2 \= (1/6)(2·5 \+ 0 \+ 2\) \= **2**,

**H₅ ↓ D₃ \= 1 ⊕ 2 ⊕ 2 \= 1 ⊕ (2 ⊗ ℂ²\_mult),   1 \+ 2 \+ 2 \= 5\.** ✓

**(iii)** su(3) is simple of dimension 8, and gl(2,ℂ) has dimension 4, so any Lie-algebra homomorphism su(3) → gl(2,ℂ) has kernel equal to the whole algebra; independently, the Weyl dimension formula gives su(3) irrep dimensions 1, 3, 6, 8, 10, 15, 24, 27, … and **never 2**. Hence **no nontrivial SU(3) action exists on a two-dimensional block**, and ZS-S14 v2.0 Def. 3.1’s clause *“λ^a\_3 acts on the D₃-2′ subspace of H₅ (colour triplet leptoquark sector)”* is void as written — twice over, since a colour triplet also needs dimension 3 while the block has dimension 2\. (Rows L1–L6.)  
**Scope, and the insulation of ZS-M60. \[GUARD, row L7\].** The erratum is registered against ZS-S14 §3.1 and Thm S14.E and against nothing else. ZS-M60 uses **only** the D₃-**trivial** component — the Z-bias field Φ, whose multiplicity is one and whose identification is therefore unambiguous — together with its hypercharge Y\_Φ \= 1/**Z** from Thm S14.D.4 and the ZS-U9 lattice. **No result of this paper depends on the colour block**, and Thm M60.7 is unaffected. The erratum is nevertheless load-bearing for what remains open: an S14-derived sector amplitude a\_N(s) cannot be computed while the colour sector is undefined, which relocates the two OPEN residuals behind a **named upstream repair** rather than behind an unattempted calculation.

**11.12 Theorem M60.26 — F-M54-16′, terminal status at v1.2**

**Theorem M60.26 (F-M54-16′ Terminal Status). \[DERIVED\].** The gate is **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)** — both, since the obstruction formula itself needs the graded dynamics (F2) — and the (F3) side is quantified:

*Table 11.2′. F-M54-16′ at v1.2, replacing the retracted v1.1 trichotomy.*

| Regime | Condition on the boundary state | Verdict |
| ----- | ----- | ----- |
| ℤ₂-symmetric state | T(ρ\_E, Jρ\_EJ) \= 0 | **CLOSED-NEGATIVE.** Im a \= 0 exactly (Thms M60.17, M60.22). |
| weakly broken | 0 \< T \< M\* \= 0.763362818245964 | **CLOSED-NEGATIVE.** Excluded by the sharp bound (Thm M60.23). |
| strongly broken | T ≥ M\* | **OPEN, and quantitatively constrained.** Not excluded; requires ≥76.34% seam-ℤ₂ orthogonality, which must itself be derived from ZS-S14 and is not. |
| Route S (anchor) | ℤ₂ restored at ε \= 0 | **CLOSED-NEGATIVE** (Thm M60.24) — the corpus’s oldest open route. |
| ungraded dynamics | (F2) fails beyond quadratic order | **OUT OF SCOPE.** ZS-M56 gate F-M56.19; nothing here applies. |

**What this is and is not.** It is **not** the unconditional no-go v1.1 claimed; that claim is retracted. It is **not** merely the conditional statement ZS-M57 already had; M57.P.1 offered a four-way disjunction with no measure attached. It is a **single named condition with a sharp numerical threshold**, which is a strictly stronger epistemic object than either, and which is falsifiable in one computation: **compute T(ρ\_E, J\_Eρ\_EJ\_E) for the ZS-S14 boundary state and compare with 0.763362818245964** — or, equivalently and more easily, compute any one of the five ceilings of Table 11A.1. **Two** physical objects remain uncomputed, not one: (F2) beyond quadratic order, and the boundary-state asymmetry. The v1.2 phrasing *the remaining question is one number* is corrected here (row N22).  
**Non-claim NC-M60.4 (new at v1.2).** ZS-M60 does not claim that the ZS-S14 boundary state fails the bound, nor that it satisfies it. It claims only that the bound is necessary. Gate F-M60.33 fires on any statement that v1.2 excludes the physical S14 event.

**§11A. Theorems M60.30–M60.34 — a conditional translation onto the ZS-A3 vacuum doublet**

A bound on a state is physics only if the state is named. The corpus names a candidate: ZS-A3 §2 gives V(ε) \= (λ\_V/4)M\_P⁴(ε²−1)² with vacua ε \= ±1 and the seam ℤ₂ acting as ε ↦ −ε. **What follows is a translation onto that candidate, not a construction of the S14 boundary state**, and §11A.4 states exactly which of its consequences survive without the candidate.

**11A.1 The doublet formula**

**Theorem M60.30 (Doublet Realization). \[PROVEN as stated; its application is conditional\].** On the two-dimensional vacuum doublet span{|+⟩,|−⟩} the seam involution is exchange, J \= σ\_x. Writing a doublet state by its Bloch vector **n** with the ℤ₂ axis along x,

**T(ρ, JρJ) \= √(n\_y² \+ n\_z²) \= 2|ρ\_SA| ,**

the component **transverse** to the ℤ₂ axis, equivalently twice the coherence between the symmetric and antisymmetric doublet states. Executed over 400 random Bloch vectors, residual 0 (row N1).  
**Corollary M60.30a. \[PROVEN\].** Any doublet state **diagonal in the S/A basis** — in particular every thermal state of the tunnelling doublet, at any temperature, and the maximally mixed state — has T \= **0 exactly** (rows N2, N17). Thermal population contributes nothing; only localisation does. **Vacuum degeneracy is not the resource; vacuum coherence is.** This is the sharpest physical statement this paper reaches, and it needs no hypothesis beyond the doublet itself.

**11A.2 (H-DOUBLET-SUPPORT), and why it cannot be removed**

**The gap, stated before the results that need it.** Theorem M60.23 bounds T for the **full** boundary environment ρ\_E. Theorem M60.30 computes T for a **two-dimensional** state. Passing from one to the other requires

**(H-DOUBLET-SUPPORT): ρ\_E is supported on the ZS-A3 vacuum doublet, supp ρ\_E ⊆ span{|+⟩,|−⟩}.**

**It is not provable by projection.** For the pinching ᴿ(X) \= PXP \+ QXQ, which is a channel commuting with Ad\_J, data processing gives T(ᴿρ, ᴿJρJ) ≤ T(ρ, JρJ): a lower bound on the full state yields **no** lower bound on its doublet component. An explicit witness is a state supported entirely off the doublet, which has T \= 1 while its doublet weight is 0 (row O3). **The hypothesis is genuine and unremovable, and an external audit was right to demand it.** Gate F-M60.50.  
**And the ceilings really do fail without it.** Take ℤ₂ to swap two orthogonal m-dimensional blocks and ρ \= P₁/m. Then T \= 1 while Tr ρ² \= 1/m, executed at m \= 2, 3, 5, 8 (row O1):

*Table 11A.1. The purity ceiling is false outside two dimensions. Executed counterexample.*

| dim | T(ρ, JρJ) | Tr ρ² | against the ceiling 0.791361396140210 |
| ----- | ----- | ----- | ----- |
| 4 | 1.000000 | 0.500000 | **violated** |
| 6 | 1.000000 | 0.333333 | **violated** |
| 10 | 1.000000 | 0.200000 | **violated** |
| 16 | 1.000000 | 0.125000 | **violated** |

**11A.3 What survives with NO hypothesis at all**

Two consequences of Thm M60.23 are **dimension-free** and require neither the doublet nor any model of the S14 environment. They are the strongest unconditional physical statements in this paper.  
**Theorem M60.34 (General Ceilings). \[PROVEN\].** For any environment Hilbert space and any boundary state ρ\_E, if the seam-graded reduction reproduces **λ** then

**F(ρ\_E, Jρ\_EJ) ≤ √(1 − M\*²) \= √(P(P+2))/(1+P) \= 0.645969974317367,**

**Tr(ρ\_E · Jρ\_EJ) ≤ 1 − M\*² \= 0.417277207719580,**

where F is the Uhlmann fidelity and P \= ρ\_**λ**(π). *Proof.* Fuchs–van de Graaf gives T ≤ √(1−F²); with T ≥ M\* this yields F² ≤ 1−M\*². The second follows from Tr(ρσ) ≤ F(ρ,σ)². Executed over 400 random involutive pairs in dimensions 2–8: both Fuchs–van de Graaf inequalities hold with zero violation, the largest fidelity observed subject to T ≥ M\* is 0.641487 ≤ 0.645970, and Tr(ρσ) ≤ F² holds in 300 further draws with zero violation (rows O5–O9).  
**Reading.** The ZS-S14 boundary state must be **at least this far, in Uhlmann fidelity, from its own seam image** — whatever its dimension, purity or structure. That is one number to compute against one number, and it is unconditional.

**11A.4 The doublet-conditional consequences, correctly scoped**

**Theorem M60.31 (Doublet Ceilings). \[DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT)\] — status lowered from PROVEN at v1.4.** On the normalized Z-bias vacuum-doublet component of the boundary state:

*Table 11A.2. Ceilings valid on a two-dimensional carrier only. Each is one number to compute.*

| Quantity | Requirement | Exact value | Row |
| ----- | ----- | ----- | ----- |
| doublet coherence | 2|ρ\_SA| ≥ M\* | **0.763362818245964** | N4 |
| Bloch length | |**n**| ≥ M\* | **0.763362818245964** | N1 |
| purity | Tr ρ² ≥ (1+M\*²)/2 | **0.791361396140210** | N6 |
| linear entropy | 1 − Tr ρ² ≤ (1−M\*²)/2 | **0.208638603859790** | N7 |
| von Neumann entropy | S ≤ H₂((1+M\*)/2) | **0.363561460568423** nats \= 0.524508316220412 bits | N8 |

The entropy ceiling sits **47.55% below** the one-qubit maximum ln 2 that ZS-Q7 fixes as the Z-channel capacity (row N9): on the doublet, the Z-bias vacuum must be far purer than a capacity-saturating mediator state.  
**Theorem M60.32 (Budget and Event Count). \[PROVEN for the budget; DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT) ∧ (H-RECIP) for the count\].** If the coherence decays as T(t) \= T(0)e^{−Γt}, the phase survives only while T ≥ M\*, so the budget is **ln(1/M\*) \= ln(1 \+ ρ\_λ(π)) \= 0.270021845324850** e-folds (row N11) — this much is unconditional. Under the named hypothesis (H-RECIP), that one Z-cycle degrades the doublet coherence by the same |**λ**| that degrades the pointer coherence,

**n\_max \= ln(1 \+ ρ\_λ(π)) / μ \= 2.351397458164148,**

with |**λ**|⁰, |**λ**|¹, |**λ**|² above threshold and |**λ**|³ \= 0.708571806474 below it (row N13): **at most two complete Z-cycles can carry the phase.** The last passing value |**λ**|² \= 0.794796437962722 is the ZS-U12 power-survival factor, recorded and not built upon. ⌊n\_max⌋ \= 2 \= dim **Z** is an **OBSERVATION and a NON-CLAIM** (gates F-M60.44, F-M60.45).  
**Theorem M60.33 (Phase-Dead Core). \[DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT), a Gaussian field state and a kink profile\].** With overlap exp(−ε²/2σ²), T(ε) \= √(1−e^{−ε²/σ²}) and the threshold is crossed at

**ε\_\*/σ \= √(−ln(1−M\*²)) \= √(2 ln(1+P) − ln(P(P+2))) \= 0.934882084184541**

(row N16, two closed forms agreeing to 2.7 × 10⁻⁵¹). ZS-A3 proves ε(r\_H) \= 0 at the anchor, so T \= 0 there **exactly** and the core cannot carry arg **λ**: every Z-anchor is predicted to be surrounded by a **phase-dead core** r\_H ≤ r \< r\_\*. This is the geometric form of Thm M60.24 — Route S is admissible only at the anchor, and the anchor is exactly where the phase cannot live.  
**Non-claim NC-M60.5.** No claim is made that the ZS-S14 boundary state does, or does not, meet any ceiling here, nor that it satisfies (H-DOUBLET-SUPPORT). Gate F-M60.46 fires on any statement that ZS-M60 has evaluated it. **The construction of the S14 boundary Hilbert space, its ρ\_E, its influence functional, a\_S14(s), the θ-family and the physical divisor are all outside this paper and are assigned to the successors of §17.**

**§12. Deep-exploration record**

The protocol requires the exploration to be exhibited. Three cycles were run — the original, one after the v1.1 audits, one after the v1.2 audits — and a fourth verification-only pass produced v1.4. Each is recorded with its dropped candidates, its convergence count and its verdict.

*Table 12.1. Step 0 long lists, by cycle, with dispositions.*

| Cycle | Candidates considered | Dropped, and why |
| ----- | ----- | ----- |
| **1** (v1.0) | boundary holonomy; multiplicative rigidity; vortex pullback; spin-cover closure; 11-dim \\\*-representation; operator-system code; non-Fock pointing | spin cover (later **closed** by unimodularity and by degree 3); \\\*-representation (even dimension forced); non-Fock (appendix only) |
| **2** (v1.1) | Choi spectrum; trace preservation; QND; **reality of the multiplier**; U(1) charge grading; reflection positivity; transcendence of |**λ**| | CP/TP (not decisive); QND (shown unnecessary); reflection positivity (ZS-S27 closed it negative) |
| **3** (v1.2) | Dyson/semiclassical a\_N(s); topological θ-angle; twisted Gel’fand–Yaglom; **exact obstruction**; **sharp asymmetry bound**; exhaustive classification; Route S at the anchor | a\_N(s) (blocked upstream by the colour-block erratum); θ-angle (S14 has no θFḞ term; adding one is a fitted datum); GY determinant (S14 supplies no slab, charge, gauge fixing or ghost) |
| **4** (v1.3→v1.4) | verification only: re-derive every printed constant by a second route; test whether the doublet ceilings generalise | no new candidate; the cycle’s output is a **scope repair** and two dimension-free theorems |

**Step 1 — MECE issue lists.** Cycle 1: S14 source and type; zero/divisor decision; carrier category; channel equality; pointing (dropped as downstream). Cycle 2: what symmetry does C\_S14 carry; what does it forbid; are the escapes exhaustive; is an escape sufficient. Cycle 3: what fails when (F3) fails; is there an exhaustive classification; can the failure be **bounded**; what upstream data do the OPEN residuals need. Cycle 4: is every printed constant independently reproducible; does each theorem hold at the scope claimed.

*Table 12.2. Step 3–4 — the load-bearing nodes whose status changed, and convergence.*

| Node | Before | After |
| ----- | ----- | ----- |
| A gauge-derived closure prescription exists | OPEN | **CLOSED-NEGATIVE** (M60.2) |
| loop \= s, base \= θ is the right typing | assumed | **CLOSED-NEGATIVE** within unimodular data (M60.4, rescoped at v1.2) |
| deg D \= 0 | PROVEN on a circle | **scope-corrected**: fails on an interval base |
| a bulk vortex gives a transport divisor | OPEN | **CLOSED-NEGATIVE** under phase covariance (M60.6) |
| **Q** \= 11 contains a complete-order M₂ code | PROVABLE | **PROVEN** (M60.11) |
| the seam ℤ₂ holds in the physical background | tacitly assumed at v1.1 | **FALSE in the bulk** (ZS-M57 §16.3); restored at the anchor |
| an exhaustive classification of QND multipliers | absent | **PROVEN** — the barycentre form (M60.21) |
| Route S (ZS-M56 F-M56.13, ten deferrals) | OPEN | **CLOSED-NEGATIVE-CONDITIONAL** in its admissible form (M60.24) |
| ZS-S14 colour block well-defined | assumed corpus-wide | **FALSE**; erratum issued (M60.25) |
| the doublet ceilings hold for a general ρ\_E | asserted at v1.3 | **FALSE**; counterexample executed (M60.31 rescoped, M60.34 rescued) |
| The S14 reduced channel equals the formal target | OPEN (F-M54-16′) | **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)**, quantified (M60.26) |

**Convergence, by the pre-declared change-count rule N\_{k+1} \< N\_k until 0\.** Cycle 1: **13 → 6 → 2 → 0**. Cycle 2: **7 → 3 → 1 → 0**, the last change being the removal of the QND hypothesis from Thm M60.17, which strengthened it and made ZS-M58 §13.4 step 3 non-load-bearing. Cycle 3: **9 → 4 → 1 → 0**, the last change being the discovery that the crude bound Im **λ** is not tight, which forced the linear program and produced M\* \= 1/(1+ρ\_λ(π)). Cycle 4: **3 → 1 → 0**, the last change being the doublet-support rescoping. **All four CONVERGED**; no cycle required re-doing the MECE decomposition.

*Table 12.3. Step 5 — value, scored honestly and revised downward where an audit was right.*

| Axis | v1.0 | v1.2 | v1.4 | Reason for the v1.4 figure |
| ----- | ----- | ----- | ----- | ----- |
| Mathematical closure potential | 10 | 10 | 10 | the carrier, channel, closure-obstruction, phase-covariance and reality layers all closed |
| Physical closure potential | 4 | 7 | **6** | lowered: the ceilings that touch a physical state are conditional on (H-DOUBLET-SUPPORT); only M60.34 is unconditional |
| No-go value if negative | 10 | 10 | 10 | seven independent CLOSED-NEGATIVE results, one carrying an exact positive replacement |
| External exportability | 8 | 8 | **8** | M\* \= 1/(1+ρ\_λ(π)) and the interval-versus-circle bounds are framework-independent; the code and dilation constructions are standard and cited as such |
| Anti-numerology strength | 10 | 9 | **9** | six new reals, all exact closed forms, all with an executed Monte Carlo |
| Corpus-dependency risk | 6 | 6 | **6** | ZS-S14’s event reduction is absent and its colour block is void; ZS-A3 supplies the vacuum model |

**Overall research value: 8.4 / 10** at v1.4 (8.6 at v1.2, 8.7 claimed at v1.1, 8.0 at v1.0). The figure moves **down** from v1.2 despite the paper proving strictly more, because the v1.3 ceilings were over-scoped and the correction costs more than the additions gain. Recording that is the point of the axis.

**§13. Zero-free-parameter and anti-numerology audit**

**13.1 Parameter audit**

**Permitted frozen inputs.** **A** \= 35/437, **Q** \= 11, dim **Z** \= 2, (**Z**, **X**, **Y**) \= (2, 3, 6), z\\\*, and **λ** \= (iπ/2)z\\\*. Of these, **A is not used anywhere in this paper**; **Q** enters as a register dimension (§8) and as a value count under a named hypothesis (§7.4); dim **Z** enters as the code target dimension and through **Y** \= **X**·**Z** (§6).  
**Introduced by ZS-M60: nothing tunable.** No temperature, decay profile, alias weight, smoothing width, entropy multiplier, branch cutoff, slab duration, coupling or window function. The boundary angle θ labels a family rather than being fitted; the code isometry V is fixed by ZS-M57 Thm M57.3 and not chosen; the leakage state τ\_{E⊥} \= (I − P\_E)/9 affects only off-code inputs and enters no theorem.

*Table 13.1. Forbidden tuning operations, and the guard that would detect each.*

| Forbidden operation | Guard |
| ----- | ----- |
| Choosing a closure to obtain winding 0 or 1 after seeing the result | F-M60.9; vacated in any case by Thm M60.2 |
| Choosing the seam location to intersect a vortex | F-M60.12; irrelevant under Thm M60.6, since location does not create transversality |
| Choosing the code plane after maximizing agreement with **λ** | F-M60.19; V is fixed by ZS-M57 before **λ** is loaded (row J3) |
| Choosing the slab duration T to fit |**λ**| | F-M60.16; no T appears in any theorem |
| Adjusting a counterterm to force CP or TP | F-M60.13; no S14 process is constructed, so none could be adjusted |
| Selecting a logarithm branch to remove the negative tail and calling it intrinsic | F-M60.18; Thm M60.13 declares its branch in the theorem line |

**13.2 Anti-numerology control**

**RETRACTED at v1.2 \[v1.0/v1.1 §13.2\].** *“The anti-numerology target set is empty; the Monte-Carlo control is inapplicable.”* v1.2 introduces exactly one new real-valued dimensionless constant, M\* \= 0.763362818245964, so the control is **executed** rather than declared inapplicable. The remainder of the audit stands.  
**Everything else is still frozen or integral.** Every real number printed in this paper is one of: a frozen ZS-M1/ZS-S28 quantity reproduced from z\\\* (z\\\*, **λ**, r, χ, μ, Im **λ**, inf ρ\_**λ**, sup ρ\_**λ**, δ\_neg, 1 − r), an exact rational from the ZS-U9 hypercharge table, an elementary function evaluated at one of those, or a small integer that is a dimension or a dimension minus one. A Monte-Carlo null ensemble compares a derived number against a universe of formula values; with an empty target set there is nothing to compare, so the control is **declared inapplicable rather than omitted** (row J4).  
**Three coincidences available in this paper, and all three refused.**  
**(i)** 1 − |**λ**| \= 0.108486434223953 equals the subdominant Choi eigenvalue. **Refused as a coincidence and recorded as a theorem**: the Choi spectrum of a qubit dephasing channel is {1 \+ |**λ**|, 1 − |**λ**|, 0, 0} identically, so the equality is an identity, not a match (Thm M60.3).  
**(ii)** q\_Φ \= 3 \= **X** \= dim **X**, and the SM hypercharge unit 1/6 \= 1/**Y** \= 1/dim **Y**. **Refused as a numerical match and recorded as algebra**: q\_Φ \= **Y**/**Z** and **Y** \= **X**·**Z** (Thm M60.7). Presenting either as an independent prediction fires F-M60.22.  
**(iii)** The interval divisor bound ‖D‖ ≥ V − 1 is exactly half the ZS-M59 circle bound 2(V − 1), and with V \= **Q** gives 10 \= **Q** − 1\. **Refused as significant numerology**: the factor two is proved in Thm M60.10 and is a statement about closed versus bounded one-manifolds, and **Q** − 1 is a dimension minus one. The one non-trivial content — that a degree-(**Q**−1) sector polynomial is then required — is registered as a **prediction** at HYPOTHESIS-strong (Thm M60.15) and never as a derivation.  
**(iv, new at v1.1)** χ \= π/2 \+ Im **λ**, so the distance from arg **λ** to the quarter-turn lattice (π/2)ℤ is exactly Im **λ** \= 0.688453227107702130. **Refused as a coincidence and recorded as an algebraic identity**: **λ** \= (iπ/2)z\\\* gives arg **λ** \= π/2 \+ arg z\\\*, and the fixed-point relation z\\\* \= i^{z\\\*} gives arg z\\\* \= (π/2)Re z\\\* \= Im **λ** on the declared branch. Residual 1.3 × 10⁻⁵¹ at 50 digits (rows K13–K17). It is used only to prove a non-membership, never as a mechanism (NC-M60.3, gate F-M60.28).  
**(v, new at v1.1)** The ℤ₂-obstruction of the phase layer is 2|sin χ| \= 1.544459340915167. **Refused as a constant**: it is a value of an elementary function at an already-frozen argument, introduced nowhere and used only as a nonzero-ness witness (row K21).  
**Pre-registered control, should the S14 calculation ever produce a numerical multiplier.** If a future paper computes a multiplier near **λ**, the null ensemble must be pre-registered before comparison: preserve the S14 symmetries and dimensions; randomize only non-protected geometric data; compute T \= |**λ**\_null − **λ**|; report the empirical p-value; do not promote a match with p \> 5%. Exact derivation supersedes this control; numerical proximity does not. Registered here so that it is on record before, not after.

**§14. Cross-paper dependency and version-collision trace**

The protocol requires more than internal consistency: it requires that a change here be traced through every paper that cites the objects touched. ZS-M60 touches four objects — z\\\* and **λ**, the ZS-M59 rigidity theorem, the ZS-M59 residual reading, and the ZS-M57 E-block — and each is traced below.

*Table 14.1. Dependency and version-collision trace.*

| Upstream object | Used how | Collision check |
| ----- | ----- | ----- |
| **ZS-M1** — z\\\* and **λ** \= (iπ/2)z\\\* | reproduced at 50 digits; **not modified** | **PASS.** λ \= f′(z\\\*) verified to 10⁻⁴⁵ (row A2). Downstream users are unaffected: ZS-S28's printed multiplier matches to 10⁻¹⁷ (rows A3–A4); ZS-M59's r, χ, μ match to 10⁻¹⁴ (row A5); the ZS-U12 power survival |**λ**|² \= 0.7947964 is unchanged, so Chapter 107's n\_supp is untouched. |
| **ZS-M59 Thm M59.21(1)** — rigidity | applied with base \[0,1\] instead of 𝕋\_θ | **PASS, with scope widened.** The proof uses only connectedness of the base; ZS-M60 states the wider form and cites the narrower one. No ZS-M59 statement becomes false. |
| **ZS-M59 Thm M59.21(3)** — deg D \= 0 | **not** applied on the interval base | **PASS, with scope restricted.** ZS-M60 records that the degree-zero clause is circle-specific. This is a restriction of applicability, not a retraction: on a circle base it remains PROVEN. |
| **ZS-M59 Thm M59.22** — divisor calculus | **not** applied to phase-covariant families | **PASS.** Its own hypothesis (isolated transversal degeneracies) is shown unsatisfiable there; the theorem is unharmed and its scope is now known to be empty on that class. |
| **ZS-M59 §11.4** — energy pairing E(D) | **not** inherited | **FLAGGED.** The pairing is against the harmonic measure on the seam phase circle; after the type reversal the divisor lives on slab time. Listed OPEN, re-typed; gate F-M60.7. |
| **ZS-M59 Thm M59.19** — the branch torsor | untouched | **PASS.** M59.19 concerns logarithms of the event unitary, not transport families. The re-typing of §5 changes only the realization of a branch field, and the paper says so in §5.1. |
| **ZS-M57 Thm M57.3** — E \= span{|1⟩,|9⟩} | used as the code plane | **PASS.** Cited as DERIVED at its own strength; not promoted to a tensor factor (NC-M60.1). |
| **ZS-M56 Thm M56.21′** — graded obstruction | respected, not bypassed | **PASS.** q\_R \= 1 \< 2 stands; a code subspace is a different category (Table 8.1). |
| **ZS-S14 Def. 3.1, Thm S14.D.4** | source action and Y\_Φ \= 1/2 | **PASS.** Read-only. No S14 result is modified; the hypercharge lemma uses S14's own Table 2.4. |
| **ZS-S28 v3.1** | frozen artifact | **PASS.** No field altered (row J1); its "0 of 13 S14-derived" verdict is inherited and never contradicted (row J2). |
| **ZS-M54 F-M54-16′** | status updated, not closed | **PASS.** The gate remains open; only its route is narrowed (Thm M60.14). |
| **ZS-M58.21** — holonomy charge grading | used as an obstruction | **PASS.** ZS-M60 strengthens rather than contradicts it: M58.21 shows covariance does not give QND; Thm M60.5 shows conjugation gives nothing at all; and Thm M60.17 shows QND was never needed for the gate. |
| **ZS-M54 Lemma M54.8a** — J\_seam and Z\_path anticommute | used as (F1) | **PASS.** Cited at its own strength and executed (rows K1–K2, both 0.0). Not modified. |
| **ZS-M56 Thm M56.20 / M56.18** — ℤ₂ selection rule | used as (F2) | **PASS, with its conditionality carried.** M56.18 is DERIVED at the symmetric quadratic background and DERIVED-CONDITIONAL to all orders; Thms M60.16–M60.20 inherit exactly that strength and say so in their theorem lines. ZS-M56 gate F-M56.19 remains the named escape. |
| **ZS-M57 Thm M57.P** — Real-Multiplier Lemma | **lifted**, not re-proved | **PASS.** M57.P (single graded QND collision) is a corollary of Thm M60.17 (arbitrary graded reduction). M57.P.1's four escapes are shown exhaustive and collapsing to one (Thm M60.18). No M57 statement becomes false; three of its hypotheses become unnecessary. |
| **ZS-M57 Thm M57.G′** — amplitude non-derivability | used in branch (c) only | **PASS.** Cited as DERIVED-CONDITIONAL on (H-TRANS); the conditionality propagates into the branch-(c) verdict and nowhere else. |
| **ZS-S28 Thms T, W, X, Y** — the fourfold phase deficit | **explained** | **PASS, upgraded.** T and W (argument in {0, π}) are recognised as instances of Thm M60.18(i); X (attenuation reachable, phase absent) is promoted OBSERVATION → DERIVED. No ZS-S28 number changes. |
| **ZS-S27** — reflection-positive route | not used | **PASS.** Its CLOSED-NEGATIVE-CONDITIONAL verdict is why candidate 6 of §12.3a was dropped rather than pursued. |
| **ZS-M57 §16.3 / ZS-A3 §2** — V(ε) ∝ (ε²−1)², vacuum at ε \= ±1 | **used to refute a v1.1 hypothesis of this paper** | **PASS, and it is why v1.1’s verdict is retracted.** The corpus already recorded that the seam ℤ₂ is spontaneously broken in the bulk and restored at the anchor; v1.1 did not carry that. v1.2 carries it in every theorem line. |
| **ZS-M56 F-M56.19** — grading exactness / ℤ₂-invariant background | named as the principal escape | **PASS.** ZS-M60 does not close it and does not weaken it; gate F-M60.26 points at it by name. |
| **ZS-M56 F-M56.13 / ZS-M57 §16** — Route S | **closed here** | **PASS.** Closed negatively in its admissible form (Thm M60.24). No ZS-M56 or ZS-M57 statement is contradicted; ZS-M57 §16.3’s own anchor rescue is the hypothesis that closes it. |
| **ZS-S14 v2.0 §3.1 / Thm S14.E** — colour block | **erratum issued** | **COLLISION FOUND AND REPORTED.** H₅ ↓ D₃ \= 1 ⊕ 2 ⊕ 2, not 1 ⊕ 2 ⊕ 2′, and su(3) has no 2-dimensional representation. ZS-M60’s own results are proved insulated (row L7). Every downstream paper citing the S14 colour assignment inherits the erratum. |
| **ZS-M54 Thm M54.22** — commutant equivalence | used to justify the controlled form in Thm M60.21 | **PASS.** Cited at its exact strength: the commutant of Z\_path⊗I *equals* the controlled unitaries; ZS-M54 v2.1’s retraction of “every dilation is controlled” is respected (NC-M54.11). |

**§15. Observational consistency**

ZS-M60 makes **no dimensionful and no new dimensionless physical prediction**. Its content is dimensionless kinematics — degree theory, operator systems and a charge-lattice identity — so it cannot collide with Planck 2018 ΛCDM parameters, with Standard Model couplings, or with DESI DR2. The single point of observational contact is inherited and re-derived rather than modified:

*Table 15.1. Observational contact.*

| Quantity | ZS-M60 role | Status |
| ----- | ----- | ----- |
| SM hypercharge unit 1/6 | re-derived from gcd(**X**, **Z**) \= 1 given the ZS-U9 assignment | **PASS.** Agrees with the Standard Model exactly; inherited, not a new prediction. |
| Y(H) \= \+1/2 | used as the Z-bias hypercharge via S14.D.4 | **PASS.** Standard Model value; unchanged. |
| α\_s \= **Q**/\[(V+F)\_Y \+ β₀(**Z**)\] \= 11/93 \= 0.118280 | not re-derived; inherited from ZS-S1 / ZS-Q3 | **PASS.** \+0.31σ against PDG 0.1180 ± 0.0009; untouched here. |
| κ² \= **A**/**Q** \= 35/4807 | not used | **PASS.** No tension introduced. |
| |**λ**|² \= 0.7947964 (ZS-U12 power survival) | reproduced from z\\\*, unchanged | **PASS.** Chapter 107's n\_supp ≈ 7.02 is unaffected. |

**\[Observational-consistency: PASS.\]**

**§16. Falsification gates**

Fifty gates in four tiers. A gate is a statement whose truth would refute or rescope a named result; the third column says which. **No gate has fired**; four v1.1 statements and one v1.3 status were retracted before any could.

*Table 16.1. Tier 1 — mathematical, immediate rejection.*

| Gate | Condition | Refutes |
| ----- | ----- | ----- |
| F-M60.1 | an element of A\_mult has a zero | M60.1 |
| F-M60.2 | a unimodular c with c·**λ** \= 1, equivalently |**λ**| \= 1 | M60.2 |
| F-M60.3 | Choi spectrum of Φ^QND\_**λ** ≠ {1+r, 1−r, 0, 0} | M60.3 |
| F-M60.4 | ȷ or κ not completely positive, or κȷ ≠ id, or the pointer identity fails | M60.11 |
| F-M60.6 | a phase-covariant family with an isolated transversal zero | M60.6 |
| F-M60.8 | a family from holonomy conjugation that depends on θ | M60.5 |
| F-M60.25 | a Hermiticity-preserving ℤ₂-covariant map with a non-real multiplier | M60.17, and ZS-M57 M57.P |
| F-M60.31 | a seam-graded multiplier that is not a circle barycentre | M60.21 |
| F-M60.32 | Im a ≠ (1/2i)Tr\[Δρ\_E V\], or Tr\[Δρ\_E V\] not purely imaginary | M60.22 |
| F-M60.33 | a measure with ∫ z dμ \= **λ** and TV(μ, μ̌) \< M\* | M60.23 |
| F-M60.35 | a ℤ₂-symmetric phase law with a non-real characteristic function | M60.24(a) |
| F-M60.37 | a 2-dimensional nontrivial su(3) representation, or two inequivalent D₃ doublets | M60.25 (withdraws the erratum) |
| F-M60.47 | an S/A-diagonal doublet state with nonzero seam asymmetry | M60.30a |
| F-M60.51 | a state with T ≥ M\* and F(ρ, JρJ) \> √(1−M\*²) | M60.34 (new at v1.4) |

*Table 16.2. Tier 2 — scope, hypothesis and construction.*

| Gate | Condition | Disposition if it fires |
| ----- | ----- | ----- |
| F-M60.9 | a **non-unimodular action-derived** return map with modulus ratio |**λ**| | does not refute M60.2; **resurrects** the ZS-M59 template |
| F-M60.26 | ZS-M56 premise (G) fails beyond quadratic order | removes (F2); moves the verdict to CLOSED-NEGATIVE-CONDITIONAL only |
| F-M60.27 | the S14 boundary state violates \[ρ\_E, J\_E\] \= 0 | removes (F3), not the theorem |
| F-M60.30 | **the honest gap**: excluding all finite orders n needs the irrationality of Re z\\\*, which is OPEN | scopes M60.19 to n \= 4, executed for n ≤ 24 |
| F-M60.36 | the ZS-A3 anchor structure ε(r\_H) \= 0 is retracted upstream | removes the hypothesis of M60.24; reopens Route S |
| F-M60.43 | the anchor fluctuation law is ℤ₂-**asymmetric** | removes branch (a) of M60.24; Route S enters the bounded regime |
| F-M60.45 | (H-RECIP) presented as derived | budget survives, event count does not |
| **F-M60.50** | **(H-DOUBLET-SUPPORT) presented as proved, or the doublet ceilings applied to a general ρ\_E** | **new at v1.4** — M60.31–M60.33 are DERIVED-CONDITIONAL, never PROVEN |
| F-M60.14 | infinitely many contributing sectors with no polynomial truncation | M60.9’s argument-principle count diverges |
| F-M60.41 | a winding count reported without a certified lower bound on inf|P\_s| | violates M60.28’s protocol |
| F-M60.48 | the seam ℤ₂ is shown not to act as ε ↦ −ε | voids §11A entirely |

*Table 16.3. Tier 3 — provenance and integrity.*

| Gate | Condition |
| ----- | ----- |
| F-M60.5 / F-M60.23 | M60.15 cited as DERIVED; or the S14 sector count found ≠ **Q** \= 11 |
| F-M60.7 | the ZS-M59 circle energy pairing applied to an interval divisor |
| F-M60.13 / F-M60.46 | M60.11, M60.12 or Appendix D described as closing F-M54-16′; or ZS-M60 said to have evaluated the S14 boundary state |
| F-M60.16 / F-M60.42 | a slab duration, coupling, or a GKLS pair (γ, ω) fitted to the target and called a derivation |
| F-M60.17 / F-M60.20 | the eleven-dimensional carrier presented as a tensor factor; a tensor-factor no-go cited as a code no-go |
| F-M60.18 | a branch limit labelled Bost–Connes without a C\\\*-algebra, semigroup, time evolution, KMS state and partition function |
| F-M60.19 | the leakage state τ\_{E⊥} used as evidence, or the code plane chosen after loading **λ** |
| F-M60.21 / F-M60.22 | a 4π theorem applied without declaring its circle and addressing unimodularity; the 1/6 hypercharge unit presented as a prediction |
| F-M60.24 / F-M60.28 | any statement quoted without its epistemic tag; χ \= π/2 \+ Im **λ** read as a mechanism |
| F-M60.29 / F-M60.34 / F-M60.44 | a register element of order ≠ 4 on the coherence line; the sin²θ\_W proximity to M\* called meaningful; ⌊n\_max⌋ \= 2 \= dim **Z** given a structural reading |
| F-M60.38 / F-M60.49 | any ZS-M60 result shown to depend on the ZS-S14 colour block; the S14 boundary state computed below a ceiling while the phase is still asserted |
| F-M60.39 | the retracted v1.1–v1.3 statements cited as live: the unconditional CLOSED-NEGATIVE verdict, the three-branch exhaustiveness, the empty anti-numerology target set, the status TERMINAL, or M60.31 as PROVEN |

**Open frontier at v1.4.** **F-M60.51 / F-M60.33** — the unconditional fidelity ceiling, one computation on the ZS-S14 boundary state; **F-M60.50** — the doublet-support hypothesis; **F-M60.26** — ZS-M56 F-M56.19, the grading beyond quadratic order; F-M60.30, the irrationality gap; F-M60.9, the only route that would resurrect the ZS-M59 template.

**§17. Terminal-in-scope declaration, and the honest scoreboard**

v1.1 declared this line TERMINAL. That declaration is **RETRACTED**: two of the five inherited residuals remain OPEN, and a paper that closes three of five and bounds the fourth is TERMINAL-IN-SCOPE, not TERMINAL. The scoreboard below is stated at the strength an external audit would accept.

*Table 17.1. The five inherited residuals, scored honestly.*

| Seed deliverable | Result | Status |
| ----- | ----- | ----- |
| 1\. Derive the θ-family from the ZS-S14 action | Three structural classes are classified and two are closed; the actual family is not constructed, and is now known to be blocked upstream by the colour-block erratum | **OPEN** (partially CLOSED-NEGATIVE) |
| 2\. Construct a closure prescription, or prove none exists | **No unimodular gauge-derived closure exists** (Thm M60.2), and the Choi-rank criterion explains why (Thm M60.3) | **CLOSED-NEGATIVE** |
| 3\. Compute the physical anchor divisor | The phase-covariant class provably carries none (Thm M60.6); the sector-polynomial calculus is exact (Thms M60.9–M60.10); the amplitudes a\_N(s) are not computed | **OPEN** (partially CLOSED-NEGATIVE) |
| 4a. Eleven-dimensional carrier intertwiner | Complete-order M₂ → M₁₁ code, all residuals exactly 0 | **PROVEN** (Thm M60.11) |
| 4b. Pointer-preserving CPTP realization | Exact minimal external-environment QND dilation | **PROVEN for the formal target** (Thm M60.12) |
| 5\. Close or refute F-M54-16′ | Reality theorem, exact obstruction, sharp bound T ≥ M\*, Route S conditionally closed; the bound rendered computable — two dimension-free ceilings and three conditional on (H-DOUBLET-SUPPORT) | **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)**, quantified; **conditionally translated** onto the ZS-A3 vacuum doublet under (H-DOUBLET-SUPPORT), and **not yet physically realized** by the actual S14 boundary state (Thms M60.26, M60.31, M60.34) |

**Score: two PROVEN, one CLOSED-NEGATIVE, one CLOSED-NEGATIVE-CONDITIONAL with a sharp threshold, two OPEN behind a named upstream repair.** That is 3.5 of 5 rather than 5 of 5, and saying so is the point of this section.

*Table 17.2. What ZS-M60 v1.2 closed, and what it did not.*

| Item | Status |
| ----- | ----- |
| Gauge-derived closure of the seam transport | **CLOSED-NEGATIVE** (Thm M60.2) |
| Unitary-closure criterion via Choi rank | **CLOSED** (Thm M60.3) |
| Loop/base typing within unimodular gauge data | **CLOSED** (Thm M60.4, scope-corrected at v1.2) |
| Gauge-copy families | **CLOSED** — constant, D \= 0 (Thm M60.5) |
| Anchor divisor on the phase-covariant class | **CLOSED-NEGATIVE** (Thm M60.6) |
| Integer hypercharge of the Z-bias field | **CLOSED** — q\_Φ \= **Y**/**Z** \= **X** \= 3 (Thm M60.7) |
| Winding of a finite-sector family; interval divisor bounds | **CLOSED** (Thms M60.9, M60.10) |
| Explicit 2- and 3-sector divisor calculus, with certified local degrees | **CLOSED / PROVEN** (Thm M60.27); one audit sign corrected |
| Fail-closed nonvanishing certificate for the sector polynomial | **CLOSED / PROVEN** (Thm M60.28) |
| Non-unimodular GKLS return map and the exact scope of Thm M60.4 | **CLOSED / PROVEN** (Thm M60.29); it inherits the M\* bound |
| Realization of the seam ℤ₂ on the ZS-A3 vacuum doublet | **CLOSED / DERIVED** (Thm M60.30); thermal occupation gives exactly zero |
| Dimension-free ceilings on the boundary state (fidelity, seam overlap) | **CLOSED / PROVEN** (Thm M60.34) |
| Purity / entropy / coherence ceilings on the doublet | **DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT)** — lowered from PROVEN at v1.4 (Thm M60.31) |
| (H-DOUBLET-SUPPORT) itself | **OPEN** — unremovable by projection; gate F-M60.50 |
| Decoherence budget; event-count ceiling | **CLOSED** (budget) / **DERIVED-CONDITIONAL on (H-DOUBLET-SUPPORT) ∧ (H-RECIP)** (count) (Thm M60.32) |
| Phase-dead core of the Z-anchor | **DERIVED-CONDITIONAL** on (H-DOUBLET-SUPPORT) and the kink/Gaussian profile (Thm M60.33) |
| Value of T for the actual ZS-S14 boundary state | **OPEN** — gate F-M60.49 |
| Eleven-dimensional complete-order pointer code | **CLOSED / PROVEN** (Thm M60.11) |
| Exact pointer-preserving QND realization | **CLOSED / PROVEN for the formal target** (Thm M60.12) |
| Reality of a seam-graded multiplier, QND-free | **CLOSED / PROVEN** (Thm M60.17) |
| Exhaustive classification of QND multipliers | **CLOSED / PROVEN** (Thm M60.21) — replaces the retracted trichotomy |
| Exact ℤ₂-obstruction formula for Im a | **CLOSED / PROVEN** (Thm M60.22) |
| Sharp lower bound on the required seam-ℤ₂ asymmetry | **CLOSED / PROVEN in closed form** (Thm M60.23) |
| Route S — ZS-M56 gate F-M56.13, deferred ten times | **CLOSED-NEGATIVE in its admissible form** (Thm M60.24) |
| ZS-S14 colour block | **ERRATUM ISSUED** (Thm M60.25); ZS-M60 insulated |
| F-M54-16′ | **CLOSED-NEGATIVE-CONDITIONAL on (F2) ∧ (F3)**, quantified; **conditionally translated** onto the ZS-A3 vacuum doublet under (H-DOUBLET-SUPPORT), and **not yet physically realized** by the actual S14 boundary state (Thms M60.26, M60.31, M60.34) |
| T(ρ\_E, Jρ\_EJ) for the actual ZS-S14 boundary state | **OPEN** — one computation, gate F-M60.33 |
| ZS-S14 colour repair, and hence the sector amplitudes a\_N(s) | **OPEN** — named upstream prerequisite |
| ZS-M56 premise (G) beyond quadratic order | **OPEN** — inherited, gate F-M60.26 \= ZS-M56 F-M56.19 |
| Irrationality of Re z\\\* | **OPEN** — gate F-M60.30 |

**Declaration.** ZS-M60 v1.5 is **TERMINAL-IN-SCOPE**. Its scope is: everything decidable from the seam grading, the frozen multiplier and the declared corpus assets, *without* ZS-S14 field content. Within that scope it is complete. Outside it, four items are open and each is named, each is behind a stated prerequisite, and none is behind an unattempted calculation this paper could have performed.  
**Successors, and the order they must be taken in.** **(1)** *ZS-S14 v3.0 — Colour-Block Repair*: withdraw the SU(3) action-level closure or supply a genuine colour carrier, and re-derive Thm S14.E. Nothing that needs S14 field content can proceed before it. **(2)** *The ZS-S14 Boundary State and its Seam-ℤ₂ Asymmetry*: compute T(ρ\_E, J\_Eρ\_EJ\_E) and compare with M\* — the **dimension-free** test of Thm M60.34 requires one comparison, but the full physical identification additionally requires the all-orders grading premise (F2) and the actual provenance of the ZS-S14 boundary state, including whether it satisfies (H-DOUBLET-SUPPORT) at all. **No code is assigned to either before ZS-M60 reports**, and they must not be folded into one paper.

**§18. Conclusion**

ZS-M59 ended with a dichotomy and named the closure prescription its decisive deliverable. It was right about which was decisive and wrong about what it would cost: a holonomy is unimodular, the Z-Spin event is a contraction of modulus 0.891513565776047, and no unimodular scalar equates 1 with that. The loop cannot be assembled from the gauge sector of ZS-S14, and the 4π spin cover — the corpus’s most attractive candidate — fails for the same reason as every other gauge datum rather than for one peculiar to itself.  
That negative is generative, because it forces the typing. The holonomy circle needs no closure; the slab interval cannot be given one within unimodular data. Loop and base exchange places, ZS-M59’s rigidity survives the exchange and its degree-zero clause does not, and the dichotomy then resolves: on every family in which the holonomy enters as an overall phase — every minimally coupled single-sector transport, every gauge copy — the modulus is holonomy-independent, zeros come in whole circles, none is transversal, and the ZS-M59 divisor calculus has an **empty** domain. By ZS-M59’s own declaration that is a complete result.  
Two theorems then close outright and depend on none of it. The odd dimension **Q** \= 11 admits no qubit tensor factor and no seam-graded subsystem, but it admits an exact qubit **code**: the ZS-M57 E-block carries a unital completely positive embedding of M₂ with a completely positive inverse and an exact pointer identity, every residual identically zero; and the formal **λ**\-dephasing event has an exact pointer-preserving dilation on a genuinely external two-dimensional environment, minimal because the Choi rank is two. The carrier obstruction that shadowed ZS-M54 through ZS-M58 was never an obstruction to a carrier; it was an obstruction to one category of carrier, and the corpus had been asking for the wrong category.  
The seam ℤ₂ then decides the phase. A graded reduction has a **real** coherence multiplier, with no complete positivity, trace preservation, QND property, collision form or single-stage assumption; every escape collapses to breaking that symmetry; and the register’s own quarter turn cannot supply arg **λ**, whose distance to the quarter-turn lattice is exactly Im **λ**. The state hypothesis fails in the bulk — ZS-M57 §16.3 already recorded it — so the verdict is conditional; but the failure is **computable**, Im a \= (1/2i)Tr\[Δρ\_E V\], every QND multiplier is a barycentre on the unit circle, and minimising the asymmetry over all measures reproducing **λ** has the closed-form answer M\* \= 1/(1 \+ ρ\_λ(π)) \= 0.763362818245964, attained by two atoms. The corpus had never placed a number on the ZS-S14 boundary state. It has one now.  
**A correction that cost more than the addition gained.** Version 1.3 asserted five ceilings on *the ZS-S14 boundary state*; an audit was right that ρ\_E was never shown to live on the two-dimensional doublet those ceilings assume. It does not follow by projection — data processing runs the wrong way — and the purity ceiling is in fact false in higher dimensions, with T \= 1 compatible with purity 1/m. The statuses are lowered, the hypothesis is named and gated, and the counterexample is executed rather than described. What survives the repair is smaller and unconditional: the boundary state must sit at Uhlmann fidelity at most 0.645969974317367 from its own seam image, in any dimension, with no model of the environment. **A smaller true statement is worth more than a larger conditional one**, and the difference is recorded on the value axis rather than hidden.  
**Stated at exact strength.** No unimodular datum closes the seam. A phase-covariant family carries no divisor. A seam-ℤ₂-covariant reduction has a real multiplier, so the phase requires a broken state, and the breaking must reach M\* \= 1/(1+ρ\_λ(π)) in trace distance. Route S is conditionally closed. **Q** \= 11 carries an exact complete-order qubit code. ZS-S14’s colour block is void as written. And what remains open is **not one number but three inputs** — the all-orders validity of the graded interaction, the seam-ℤ₂ asymmetry of the actual boundary state, and whether that state lives on the ZS-A3 doublet at all. Against each, this paper supplies a number to compare, and the construction of the S14 process, state and divisor is assigned to the successors.

**Acknowledgements & Code Availability**

The author thanks the reviewers of the ZS-M60 successor seed v1.0 and v1.1. The seed's integration audit — which rejected the unrestricted frozen-rigidity claim, corrected the vortex bypass to a pullback condition, rejected the untyped 4π selector and the isotypic V \= 3 shortcut, and replaced a one-sided compensated pointing sketch by the symmetric Lévy–Khintchine exponent — is inherited in full, and three of its six audited bypasses are closed here by proof rather than by restriction. The seed's strongest instruction, *compare only at the end*, was obeyed: the firewall of §0.3 was never opened, because no comparison became available.  
During construction the fail-closed ledger mechanism fired once, on the newly adopted rule that a supremum claim may not be certified by a grid sample: row B2 initially tested sup ρ\_**λ** against a 4001-point grid, missed the true supremum by 2.6 × 10⁻⁴, and returned FAIL. The closed form ρ\_**λ**(χ) \= (1 \+ r)/(1 − r) replaced the sample; the mechanism was not relaxed. This is the same class of defect ZS-M59 §1.2 recorded in ZS-S28's printed maximum, and its recurrence is the reason the rule is now a ledger rule rather than a habit.  
**Code.** \`zs\_m60\_verify\_v1\_5.py\`, shipped with \`requirements.txt\` (**hard \`==\` pins**: mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1, sympy 1.13.3) and a one-command \`RUN.md\`; tested interpreter CPython 3.12.3. Exactly **186 ledger rows** in every scenario, explicit FAIL rows for missing evidence, exit code 1 on any FAIL, on a row-count mismatch, or on a missing dependency; JSON to \`zs\_m60\_verify\_v1\_5.json\`; the full table ships separately as \`zs\_m60\_ledger\_v1\_5.md\`. Blocks: **A** frozen inputs (8); **B** multiplicative rigidity (7); **C** closure obstruction (6); **D** gauge-copy / superselection (5); **E** argument principle (5); **F** interval divisor bounds (6); **G** hypercharge lattice (7); **H** eleven-dimensional code (16); **I** exact QND realization (8); **J** scope and non-claims (9); **K** seam-ℤ₂ reality closure (25); **L** erratum, interval certification, M\* (28); **M** sector divisor calculus and the GKLS map (18); **N** translation onto the ZS-A3 doublet (22); **O** scope repair and the dimension-free ceilings (16). An audit of v1.3 could not re-run the script for want of exactly this information; the omission was repaired at v1.4 and independently re-executed by that audit at v1.4.  
This work used AI tools (Anthropic Claude) for corpus and external-literature search, cross-paper integration, symbolic and numerical verification, and drafting, under the author's editorial direction. The author assumes full responsibility for all content.

**Appendix A — Verification and regression ledger (186 rows, 0 FAIL, exit 0\)**

**The full table ships as a separate artifact, \`zs\_m60\_ledger\_v1\_5.md\`, and not inside this manuscript.** An audit observed that eleven pages of dense ledger obscure the mathematics; the table is therefore supplementary and only its structure and discipline are stated here.

*Table A.1. Ledger composition. Row kinds are assigned by what is EXECUTED, not by what is claimed.*

| Kind | Count | What the row certifies |
| ----- | ----- | ----- |
| THEOREM-PROOF | **97** | a **closed-form identity** is evaluated exactly and compared |
| NUMERIC-WITNESS | **35** | a random, model, grid or single-instance execution — **explicitly not a proof** |
| GUARD | 34 | a negative control that fails if the named error is made |
| DECLARATION | **20** | a scope, provenance or verdict statement carrying **no computation at all** |

*Table A.2. Blocks.*

| Block | Content | Rows |
| ----- | ----- | ----- |
| A | frozen inputs and provenance | 8 |
| B | multiplicative rigidity | 7 |
| C | closure obstruction | 6 |
| D | gauge-copy / superselection dichotomy | 5 |
| E | argument principle and sector polynomial | 5 |
| F | interval divisor bounds | 6 |
| G | hypercharge lattice and anchor holonomy | 7 |
| H | eleven-dimensional complete-order code | 16 |
| I | exact QND realization | 8 |
| J | scope, provenance, non-claims | 9 |
| K | seam-ℤ₂ reality closure | 25 |
| L | erratum, interval certification, obstruction, M\* | 28 |
| M | sector divisor calculus, nonvanishing certificate, GKLS map | 18 |
| N | translation onto the ZS-A3 vacuum doublet | 22 |
| O | scope repair and the dimension-free ceilings | 16 |

**Discipline, twice corrected.** A DECLARATION is not evidence and a ledger count is not a theorem count. An audit of v1.1 found nine rows typed THEOREM-PROOF carrying a literal true value; re-audited, exactly nine confirmed, six executed and three re-typed. An audit of v1.4 observed that **sampling a universally quantified claim is a witness, not a proof**; at v1.5 a further **24 rows** were re-typed out of THEOREM-PROOF, which falls from 121 to **97** while NUMERIC-WITNESS rises from 12 to **35**. **The proofs are in the manuscript body and Appendix B; the ledger only executes them.** The honest name for the artefact is a *verification and regression ledger*.  
**Reproduction.** \`requirements.txt\` hard-pins mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1 and sympy 1.13.3 with \`==\`; \`RUN.md\` gives a single command; the interpreter is CPython 3.12.3. v1.3 listed minima and called them pins, which an audit correctly refused; that was repaired at v1.4 and the repaired set was **independently re-executed by that audit**, returning \`rows=186 declared=186 PASS=186 FAIL=0\`. The verifier exits 1 on any FAIL, on a row-count mismatch, or on a missing dependency.

**Appendix B — Proofs deferred from the body**

**B.1 Theorem M60.2 (closure obstruction), in full**

Let a : \[0,1\] → ℂ^× be continuous with a(0) \= 1, a(1) \= **λ**. A gluing datum acts on the one-dimensional coherence line ℂ·|0⟩⟨1| — which it must, that line being a single joint eigenspace of the two pointer projections — hence as a scalar c. If it belongs to a compact group acting unitarily then |c| \= 1, and the closure condition c**λ** \= 1 forces |c| \= 1/|**λ**| \= 1.1216… ≠ 1\. The argument uses no property of a beyond its endpoints and none of the gluing beyond unitarity, so it applies verbatim to a boundary U(1)\_Y holonomy, a Wilson line in any compact group restricted to a charge eigenspace, and a spin-cover deck factor. **Remark.** It does **not** apply to closure by an arbitrary continuous path, which always exists (ZS-M59 M59.24) — that is an external choice, and the gauge data were the only candidate source of a canonical one.

**B.2 Theorem M60.23 (the closed form M\*)**

Write μ \= s \+ q with s even and q odd about φ ↦ −φ, so μ ≥ 0 ⇔ |q| ≤ s and TV(μ, μ̌) \= ∫|q|; the constraints are ∫ s \= 1, ∫ s cos φ \= Re **λ**, ∫ q sin φ \= Im **λ**. Place s at ±α with mass A and at π with mass 1−A, the π atom being reflection-fixed and therefore free of odd charge. Then A cos α − (1−A) \= Re **λ** gives A \= (1+Re λ)/(1+cos α); the odd charge obeys u sin α \= Im **λ** with |u| ≤ A; and the objective is TV \= |u| \= Im λ/sin α. Minimising over α binds at |u| \= A, and the half-angle substitution turns Im λ(1+cos α) \= (1+Re λ) sin α into **tan(α/2) \= Im λ/(1+Re λ)**. Substituting back,

TV \= Im λ(1+tan²(α/2))/(2 tan(α/2)) \= \[(1+Re λ)² \+ (Im λ)²\]/(2(1+Re λ)) \= |1+λ|²/(2(1+Re λ)),

and at that α one finds u \= A exactly, so the −α atom carries zero mass and the optimum is a **two-atom** measure. Dividing by |1+λ|² and using Re\[(1−λ)/(1+λ)\] \= (1−|λ|²)/|1+λ|² \= ρ\_λ(π) gives M\* \= 1/(1 \+ ρ\_λ(π)). Four expressions agree to 1.3 × 10⁻⁵¹, the explicit measure reproduces **λ** to 1.9 × 10⁻⁵¹, and an independent 3600-angle linear program that knows none of this returns the same value to 3 × 10⁻⁷.

**B.3 Theorem M60.25 (the ZS-S14 erratum), both halves**

**(a)** D₃ ≅ S₃ has three conjugacy classes, hence three irreducible complex representations, and 1²+1²+2² \= 6 forces dimensions 1, 1, 2\. The A₅ five-dimensional irrep has character (5, 1, −1) on (identity, order-2, order-3); character orthogonality with class sizes (1, 2, 3\) gives m₁ \= (5−2+3)/6 \= 1, m₁′ \= (5−2−3)/6 \= 0, m₂ \= (10+2)/6 \= **2**, and 1 \+ 0 \+ 4 \= 5 closes the count. The two doublets are the **same** irreducible representation with multiplicity two; separating them needs an operator on End\_{D₃}(H₅) ≅ ℂ ⊕ M₂(ℂ), which D₃ does not supply. **(b)** A representation ρ : su(3) → gl(2,ℂ) has kernel an ideal; su(3) is simple, so the kernel is 0 or everything, and 0 would force 8 ≤ 4\. Independently the Weyl dimension formula returns 1, 3, 6, 8, 10, 15, 24, 27, … and **never 2**.

**B.4 Corollary M60.21a, and the general ceilings of M60.34**

Under (F1)–(F3), U₁ \= J\_EU₀J\_E gives V† \= J\_EVJ\_E, so E\_V(Ā) \= J\_E E\_V(A) J\_E and μ(Ā) \= Tr\[J\_EρJ\_E E\_V(A)\] \= μ(A): the spectral measure is **conjugation-invariant**, hence ∫ Im z dμ \= 0 and a is real. Reality is conjugation-symmetry of a measure. For M60.34, Fuchs–van de Graaf gives 1−F ≤ T ≤ √(1−F²); the upper half with T ≥ M\* yields F² ≤ 1−M\*², and Tr(ρσ) ≤ F(ρ,σ)² yields the second ceiling. Both inequalities were executed over 400 and 300 random draws respectively with **zero** violations.

**B.5 Executed identities recorded rather than re-proved**

The following are verified in the ledger and not re-derived here: the complete positivity of ℰ, ℛ, ȷ, κ by explicit Choi construction, all four minimum eigenvalues exactly 0 (rows H3–H6); the symbolic θ-freedom of the gauge-copy composite, exact over real symbols (row D1); the argument-principle identity against a 200 000-point unwrapped-argument computation on eight random polynomials (row E1); the sharpness of the interval bounds on the monotone staircase (rows F1–F4); the Krawczyk certification of z\\\* in a box of radius 10⁻³⁰ (row L8); and the second-route re-derivation of all 24 printed constants (rows O10–O16).

**Appendix D — Audit discipline, and the non-Fock construction**

**D.1 How the four external audits were handled**

Four independent audits were received across v1.1–v1.3 and are answered item by item in Table 0.0. **Every finding was re-derived from the corpus and from first principles before disposition; no verdict was accepted on authority.** Of nineteen findings, sixteen are upheld, one is partly contested, one is contested and then overtaken, and one recommendation is explicitly declined with a theorem as the reason.  
**Where the audits were right and this paper was wrong.** The failure of (F3) in the physical bulk, located in ZS-M57 §16.3 — which produced Thms M60.22–M60.23. The non-exhaustiveness of the v1.1 trichotomy — which produced Thm M60.21. The nine mis-typed ledger rows, re-audited and confirmed at exactly nine. The absence of interval certification, now a Krawczyk test. The ZS-S14 representation defect. The three-sector local-degree sign, where **the audit’s own formula was wrong** in 11 of 11 executed crossings while its two-sector sign was right. And, at v1.4, the **doublet-support gap**: the purity and entropy ceilings are false outside two dimensions, executed at four dimensions in Table 11A.1, and (H-DOUBLET-SUPPORT) is now named, gated, and shown unremovable by data processing.  
**Where this paper does not follow the audits.** Three audits recommended repairing ZS-S14 before attacking the gate. That order is **not adopted**: Theorems M60.21–M60.24 and M60.34 use no S14 field content whatever, and a paper that had waited would not contain them. The repair is registered as a prerequisite for the residuals that genuinely need it and for nothing else.

**D.2 The non-Fock pointing construction — recorded, explicitly nonphysical**

At the seed’s request and claiming nothing about ZS-S14: a unitary-state two-sided moment sequence must be φ(n) \= r^{|n|}e^{inχ}. The symmetric Lévy measure ν(dp) \= (μ/π)p⁻²dp with drift χ gives, by Lévy–Khintchine with ∫(1−cos np)p⁻²dp \= π|n|, the exponent Ψ(n) \= −μ|n| \+ iχn and hence exactly that sequence. This repairs the older seed’s one-sided sketch, which acquires a spurious n log|n| phase at stability index one. The density is not square-integrable at the origin, so this is **not** a Fock coherent vector: the moment construction is DERIVED-CONDITIONAL at the Weyl-algebra level, the Fock realization is CLOSED-NEGATIVE, general non-Fock existence is IMPORTED-PROVEN, identification with ZS-S14 is OPEN, and use of this appendix to close F-M54-16′ is **PROHIBITED** (gate F-M60.13).

**References**

*Corpus references are cited by paper code and version at the strength their own release declares. External references follow APS style.*

**Z-Spin corpus**

\[C1\] K. Kang, *ZS-F0: Foundational Register Structure*, Z-Spin Cosmology Collaboration (Def. 8.11, Thm 8.13, Conj. 8.14).  
\[C2\] K. Kang, *ZS-F1: The Z-Bias Field and the Bogomolnyi Vortex Sector*, §5.  
\[C3\] K. Kang, *ZS-F5: Sector Dimensions (Z, X, Y) \= (2, 3, 6\) and Q \= 11*, §4. \[PROVEN\]  
\[C4\] K. Kang, *ZS-M1: The i-Tetration Fixed Point*, z\\\* and λ \= (iπ/2)z\\\*.  
\[C5\] K. Kang, *ZS-M46 v1.5: Koenigs Linearization and Half-Sided Modular Inclusions*, §4, Thm M46.3A.  
\[C6\] K. Kang, *ZS-M51 v1.3: Lambert–Dottie Stability of the Exponential Fixed-Point Family*, Thms T2, T5–T6.  
\[C7\] K. Kang, *ZS-M54 v2.2 FINAL: The Mediator-Graph Transduction Theorem*, §§10–13, gate F-M54-16′.  
\[C8\] K. Kang, *ZS-M56 v1.8 FINAL: The Graded Multiplicity Obstruction*, Thms M56.5, M56.21′, M56.22′.  
\[C9\] K. Kang, *ZS-M57 v1.8: The Odd Carrier*, Thms M57.D.1, M57.3, Cor. M57.3a.  
\[C10\] K. Kang, *ZS-M58 (terminal): Endpoint–Lift–Intertwiner Separation and the Character Reduction*, Thms M58.21, M58.22A, §13.4.  
\[C11\] K. Kang, *ZS-M59 v1.8 TERMINAL-IN-SCOPE: The Aliasing-Fiber Completion of the Formal Z-Spin QND Event*, Thms M59.14, M59.19, M59.21–M59.25, §§11–18.  
\[C12\] K. Kang, *ZS-Q18: The Dephasing Representative and the Born Rule from i-Tetration*, Thm Q18.12.  
\[C13\] K. Kang, *ZS-S1: The Spectral-to-β Bridge*, §§5.2, 7\.  
\[C14\] K. Kang, *ZS-S14 v2.0: Master Action Total Closure*, Def. 3.1, Thms S14.A–S14.E, S14.D.4.  
\[C15\] K. Kang, *ZS-S26: Certificate P — Conditional Interface Reduction* (cited only for its retraction scope).  
\[C16\] K. Kang, *ZS-S28 v3.1 TERMINAL: A Formal Event Exists; the Reduction Does Not Select It*, §§0–5.  
\[C17\] K. Kang, *ZS-U9: The Trinity Braiding Theorem*, Thm 6.1 (hypercharge sector formulas).  
\[C18\] K. Kang, *ZS-U12 v2.3: The z\\\*-Locked Low-ℓ CMB Transfer*, Thms U12.1–U12.5 (cited for non-collision only).  
\[C19\] K. Kang, *ZS-A16 v1.3 / ZS-A17 v1.5: The Spin–Metric Independence No-Go*.  
\[C20\] K. Kang, *The Book of Z-Spin Cosmology, Light Edition v12.1* (compiled July 2026), Chapters 1–4, 107\.

**External**

\[E1\] W. F. Stinespring, *Positive functions on C\\\*-algebras*, Proc. Amer. Math. Soc. **6**, 211 (1955).  
\[E2\] M.-D. Choi, *Completely positive linear maps on complex matrices*, Linear Algebra Appl. **10**, 285 (1975).  
\[E3\] G. Wittstock, *Matrix order and W\\\*-algebras in the operational approach*, Commun. Math. Phys. **74**, 51 (1980).  
\[E4\] M. Hamana, *Injective envelopes of C\\\*-dynamical systems*, Tohoku Math. J. **37**, 463 (1985).  
\[E5\] V. I. Paulsen, *Completely Bounded Maps and Operator Algebras* (Cambridge University Press, Cambridge, 2002).  
\[E6\] E. B. Davies and J. T. Lewis, *An operational approach to quantum probability*, Commun. Math. Phys. **17**, 239 (1970).  
\[E7\] K. Kraus, *States, Effects, and Operations*, Lecture Notes in Physics Vol. 190 (Springer, Berlin, 1983).  
\[E8\] S. Attal and Y. Pautrat, *From repeated to continuous quantum interactions*, Ann. Henri Poincaré **7**, 59 (2006).  
\[E38\] S. Coleman, *Aspects of Symmetry* (Cambridge University Press, Cambridge, 1985), Ch. 7 (the double well, tunnelling doublet, and localisation as a superposition of parity eigenstates).  
\[E39\] A. J. Leggett *et al.*, *Dynamics of the dissipative two-state system*, Rev. Mod. Phys. **59**, 1 (1987) (doublet coherence and its decoherence).  
\[E40\] T. Baumgratz, M. Cramer and M. B. Plenio, *Quantifying coherence*, Phys. Rev. Lett. **113**, 140401 (2014).  
\[E41\] I. Marvian and R. W. Spekkens, *How to quantify coherence: distinguishing speakable and unspeakable notions*, Phys. Rev. A **94**, 052324 (2016) (resource theory of asymmetry; the transverse Bloch component as the asymmetry monotone).  
\[E42\] G. Gour and R. W. Spekkens, *The resource theory of quantum reference frames*, New J. Phys. **10**, 033023 (2008).  
\[E27\] R. Krawczyk, *Newton-Algorithmen zur Bestimmung von Nullstellen mit Fehlerschranken*, Computing **4**, 187 (1969).  
\[E28\] R. E. Moore, *A test for existence of solutions to nonlinear systems*, SIAM J. Numer. Anal. **14**, 611 (1977).  
\[E29\] S. M. Rump, *Verification methods: rigorous results using floating-point arithmetic*, Acta Numerica **19**, 287 (2010).  
\[E30\] M. B. Ruskai, *Beyond strong subadditivity: improved bounds on the contraction of generalized relative entropy*, Rev. Math. Phys. **6**, 1147 (1994) (contractivity of trace distance).  
\[E31\] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge University Press, Cambridge, 2000), §9.2 (trace distance and its monotonicity).  
\[E32\] F. Hiai and M. B. Ruskai, *Contraction coefficients for noisy quantum channels*, J. Math. Phys. **57**, 015211 (2016); arXiv:1508.03551.  
\[E33\] J. E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, New York, 1972), §§13, 24 (simplicity of su(3); Weyl dimension formula).  
\[E34\] W. Fulton and J. Harris, *Representation Theory: A First Course* (Springer, New York, 1991), Lecture 2 (S₃ character table) and Lecture 12\.  
\[E35\] C. Carathéodory, *Über den Variabilitätsbereich der Fourier’schen Konstanten*, Rend. Circ. Mat. Palermo **32**, 193 (1911); O. Toeplitz, Rend. Circ. Mat. Palermo **32**, 191 (1911) (trigonometric moment problem: the achievable first moments of a circle measure).  
\[E36\] N. I. Akhiezer, *The Classical Moment Problem* (Oliver & Boyd, Edinburgh, 1965).  
\[E37\] K. Kirsten and A. J. McKane, *Functional determinants for general Sturm–Liouville problems*, J. Phys. A **37**, 4649 (2004) (twisted-boundary Gel’fand–Yaglom determinants; cited for the protocol of §12.3b candidate 3 only).  
\[E24\] R. P. Feynman and F. L. Vernon, *The theory of a general quantum system interacting with a linear dissipative system*, Ann. Phys. (N.Y.) **24**, 118 (1963).  
\[E25\] E. P. Wigner, *Group Theory and its Application to the Quantum Mechanics of Atomic Spectra* (Academic Press, New York, 1959), Ch. 26 (antiunitary operators and reality constraints).  
\[E26\] R. Alicki and K. Lendi, *Quantum Dynamical Semigroups and Applications*, Lecture Notes in Physics Vol. 717 (Springer, Berlin, 2007\) (covariant channels and the Pauli transfer representation).  
\[E9\] L. V. Ahlfors, *Complex Analysis*, 3rd ed. (McGraw–Hill, New York, 1979), Ch. 4 (argument principle, Rouché).  
\[E10\] J. W. Milnor, *Topology from the Differentiable Viewpoint* (University Press of Virginia, Charlottesville, 1965\) (Brouwer degree, transversality).  
\[E11\] J. M. Baptista, *Vortices as degenerate metrics*, Lett. Math. Phys. **104**, 731 (2014); arXiv:1212.3561.  
\[E12\] E. B. Bogomolny, *Stability of classical solutions*, Sov. J. Nucl. Phys. **24**, 449 (1976).  
\[E13\] H. B. Nielsen and P. Olesen, *Vortex-line models for dual strings*, Nucl. Phys. B **61**, 45 (1973).  
\[E14\] G. Koenigs, *Recherches sur les intégrales de certaines équations fonctionnelles*, Ann. Sci. Éc. Norm. Supér. **1**, 3 (1884).  
\[E15\] J.-P. Serre, *Linear Representations of Finite Groups* (Springer, New York, 1977), §2.3.  
\[E16\] P. A. M. Dirac, *Quantised singularities in the electromagnetic field*, Proc. R. Soc. Lond. A **133**, 60 (1931) (charge quantization and holonomy single-valuedness).  
\[E17\] Y. Aharonov and D. Bohm, *Significance of electromagnetic potentials in the quantum theory*, Phys. Rev. **115**, 485 (1959).  
\[E18\] G. Roepstorff, *Coherent photon states and spectral condition*, Commun. Math. Phys. **19**, 301 (1970).  
\[E19\] K. Sato, *Lévy Processes and Infinitely Divisible Distributions* (Cambridge University Press, Cambridge, 1999).  
\[E20\] J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Math. **1**, 411 (1995).  
\[E21\] P. Halmos, *Introduction to Hilbert Space and the Theory of Spectral Multiplicity*, 2nd ed. (Chelsea, New York, 1957).  
\[E22\] Particle Data Group, R. L. Workman *et al.*, *Review of Particle Physics*, Prog. Theor. Exp. Phys. **2022**, 083C01 (2022) (α\_s, hypercharge normalization).  
\[E23\] Planck Collaboration, N. Aghanim *et al.*, *Planck 2018 results. VI. Cosmological parameters*, Astron. Astrophys. **641**, A6 (2020).

**Version History**

**v1.0 (March 2026): Initial public release.** Consolidated from internal Z-Spin Collaboration research notes up to the ZS-M60 Successor Seed Report v1.1 (July 2026). Executes the five residuals transferred by ZS-M59 v1.8 §18 and by ZS-M54 v2.2. **New theorems:** M60.1 multiplicative frozen-data rigidity (PROVEN); **M60.2 seam closure obstruction — no unimodular gluing closes the frozen transport (PROVEN)**; M60.3 rank-one closure criterion, with 1 − |**λ**| identified as the subdominant Choi eigenvalue (PROVEN); M60.4 type-reversal theorem, loop \= 𝕋\_θ and base \= \[0,1\] (DERIVED); M60.5 gauge-copy triviality, computed symbolically (PROVEN); **M60.6 phase-covariance no-transversality — the anchor route is CLOSED-NEGATIVE on the phase-covariant class (PROVEN)**; M60.7 hypercharge lattice lemma, q\_Φ \= **Y**/**Z** \= **X** \= 3 (DERIVED); M60.8 anchor-holonomy quantization ℤ\_**X** \= ℤ₃ and Cor. M60.8a barring the 4π selector by degree (DERIVED-CONDITIONAL / DERIVED); M60.9 sector-polynomial winding theorem (PROVEN); M60.10 interval divisor bounds, both sharp and exactly half the circle bounds (PROVEN); M60.11 exact eleven-dimensional complete-order pointer code (PROVEN); M60.12 exact pointer-preserving QND realization with a minimal external environment (PROVEN for the formal target); M60.13 fixed-point positivity obstruction, branch-declared (PROVEN); M60.14 F-M54-16′ terminal status, OPEN with one named object (DERIVED); M60.15 sector-degree re-typing of (H-CARRIER-11) (HYPOTHESIS-strong / REFORMULATED). **Closures:** three CLOSED-NEGATIVE results (gauge closure, phase-covariant divisor, holonomy-covariant QND). **Retractions inherited and upheld:** the unrestricted frozen-rigidity claim, the untyped 4π selector, the isotypic V \= 3 shortcut, the automatic Bost–Connes label. **Scope corrections issued upstream:** ZS-M59 Thm M59.21(3) is circle-specific; ZS-M59 §11.4's energy pairing does not transfer to an interval divisor (both flagged, neither retracted). **New gates:** F-M60.1 through F-M60.24. **New non-claims:** NC-M60.1 (E-block is a code plane, not a tensor factor), NC-M60.2 (no property of Φ\_S14 is claimed). Verification 77/77 PASS, 0 FAIL, exit 0\. Zero free parameters; **A** \= 35/437 available and unused; no new real constant introduced, so the anti-numerology target set is empty and the Monte-Carlo control is declared inapplicable.  
**v1.1 (March 2026): the seam-ℤ₂ reality closure; F-M54-16′ CLOSED-NEGATIVE.** v1.0 terminated with exactly one open object, the ZS-S14 one-event Lorentzian CTP Choi process C\_S14, and reported F-M54-16′ as OPEN in it. v1.1 closes the gate by deriving a **symmetry invariant of C\_S14** instead of constructing C\_S14. **New theorems:** **M60.16 seam-ℤ₂ covariance of the reduced one-event map** (DERIVED-CONDITIONAL on ZS-M56 premise (G) and a grading-invariant boundary state); **M60.17 Reality Theorem — a seam-ℤ₂-covariant, Hermiticity-preserving reduction has a real coherence multiplier, with no complete positivity, trace preservation, QND property, collision form or single-stage assumption** (PROVEN; the lift of ZS-M57 Thm M57.P, whose three extra hypotheses are shown unnecessary); **M60.18 Escape Collapse** — all four escapes of ZS-M57 Cor. M57.P.1 reduce to breaking the seam ℤ₂, a one-sided pointer-diagonal phase layer being covariant iff φ ∈ {0, π} with exact obstruction 2i sin φ, and covariance being closed under composition (PROVEN), with Cor. M60.18b identifying the **same missing datum, an anchor, behind both the divisor no-go of §5 and the phase no-go of §11**; **M60.19 Quarter-Turn Quantization Deficit** — register-generated phases lie in (π/2)ℤ while χ/(π/2) \= 1 \+ Re z\\\* \= 1.4382829367270321 ∉ ℤ, the distance to the lattice being exactly Im **λ** (PROVEN, residual 1.3 × 10⁻⁵¹, exclusion executed for n \= 1…12); **M60.20 F-M54-16′ Terminal Verdict — CLOSED-NEGATIVE in all three branches**, with the exact replacement factorization Φ^QND\_**λ** \= Ad\_{U\_Z} ∘ Φ^{|λ|}\_real verified to 3.5 × 10⁻¹⁶, in which the ℤ₂-covariant real factor carries |**λ**| and the ℤ₂-obstructed rotation (obstruction 2|sin χ| \= 1.544459340915167) carries arg **λ** (DERIVED). **Upstream promotions:** ZS-S28 Theorem X, *attenuation reachable, phase absent*, OBSERVATION → **DERIVED**, and its Theorems T and W recognised as two instances of Thm M60.18(i); ZS-M54's Eq. (11a)/(11b) layer split and ZS-M57 §5.2's modulus/argument remark, bookkeeping → **theorem**. **New gates:** F-M60.25 through F-M60.30, of which F-M60.26 (ZS-M56 grading beyond quadratic order) is the principal escape and **F-M60.30 records an honest gap** — excluding all finite orders n would require the irrationality of Re z\\\*, which is OPEN, so Thm M60.19 is scoped to n \= 4 and executed for n ≤ 12\. **New non-claim:** NC-M60.3 (χ \= π/2 \+ Im **λ** is an algebraic identity, not a mechanism). **Status raised** from TERMINAL-IN-SCOPE to **TERMINAL**. Ledger extended from 77 to **102 rows** by the new block K (25 rows); **102/102 PASS, 0 FAIL, exit 0**. Zero free parameters; still no new real-valued constant, so the anti-numerology target set remains empty. No v1.0 theorem is retracted and no corpus number is altered.  
**v1.2 (March 2026): two external audits answered; three v1.1 statements retracted; the conditional quantified.** Both audits were re-derived before disposition (Table 0.0, Appendix E); nine of twelve findings are upheld and one recommendation is explicitly declined with a theorem as the reason. **RETRACTIONS.** (i) The v1.1 verdict *F-M54-16′ CLOSED-NEGATIVE, unconditional* is withdrawn: ZS-M57 §16.3 records that the ZS-A3 potential V(ε) ∝ (ε²−1)² puts the vacuum at ε \= ±1, so hypothesis (F3) provably fails in the bulk. (ii) The v1.1 Thm M60.20 three-branch exhaustiveness claim is withdrawn as not exhaustive. (iii) The v1.0/v1.1 declaration of an **empty anti-numerology target set** is withdrawn, since v1.2 prints M\*; the Monte Carlo is executed instead (210 formulas, 0 hits at 10⁻³, p \= 0.63). (iv) The status **TERMINAL** is lowered to **TERMINAL-IN-SCOPE**. v1.1 Thm M60.19 is **not** retracted but has its hypothesis narrowed in its theorem line to pure finite-order conjugation. **NEW THEOREMS.** **M60.21** barycentre classification — every QND multiplier is a \= ∫ z dμ over a probability measure on the unit circle, exhaustive, replacing the retracted trichotomy (PROVEN); Cor. M60.21a re-derives reality as conjugation-invariance of μ. **M60.22** exact obstruction Re a \= Tr\[ρ₊V\], **Im a \= (1/2i)Tr\[Δρ\_E V\]** with Tr\[Δρ\_E V\] purely imaginary (PROVEN, 300 dilations, residual 8.3 × 10⁻¹⁷), and Cor. M60.22a the first-order form. **M60.23** sharp bound **T(ρ\_E, Jρ\_EJ) ≥ M\* \= |1+λ|²/(2(1+Re λ)) \= 1/(1 \+ ρ\_λ(π)) \= 0.763362818245964**, attained by an explicit two-atom measure, four closed forms agreeing to 1.3 × 10⁻⁵¹ and an independent 3600-angle linear program agreeing to 3 × 10⁻⁷ (PROVEN). **M60.24** Route S dichotomy — the ℤ₂-symmetric anchor law has a real characteristic function, so **ZS-M56 gate F-M56.13, deferred through ten versions, is CLOSED-NEGATIVE in its admissible form** (DERIVED). **M60.25** upstream erratum to ZS-S14 v2.0: H₅ ↓ D₃ \= 1 ⊕ 2 ⊕ 2 with no distinct 2′, and su(3) has no 2-dimensional representation, so the colour-block clause of Def. 3.1 is void as written; ZS-M60 is proved insulated (PROVEN). **M60.26** F-M54-16′ CLOSED-NEGATIVE-CONDITIONAL on (F3), **with the condition quantified** (DERIVED). **ADDENDUM (blocks M).** **M60.27** explicit 2- and 3-sector divisor calculus — root, anchor angle, transversality and local degree in closed form; **an external audit’s 3-sector sign is corrected**, being wrong in 11 of 11 executed crossings while its 2-sector sign is right and adopted (PROVEN). **M60.28** fail-closed nonvanishing certificate inf|P\_s| ≥ min\_grid − Lπ/M, which correctly refuses a genuinely vanishing family (PROVEN). **M60.29** GKLS non-unimodular return map a(s) \= exp\[−∫γ − i∫ω\] with |a(1) − λ| \= 0.0 at forty digits, correcting the wording of Thm M60.4 and shown to **inherit** rather than evade the M\* bound; Cor. M60.29a establishes reality **to all orders** by exact matrix exponentials (3.2 × 10⁻¹⁷). New gates F-M60.40–F-M60.42. **LEDGER.** Extended from 102 to **148 rows** by blocks L (28) and M (18); an independently re-audited mis-typing of nine rows is repaired — six executed, three re-typed DECLARATION — so the honest counts are 95 THEOREM-PROOF, 9 NUMERIC-WITNESS, 30 GUARD, **14 DECLARATION**, and Appendix A states that a DECLARATION is not evidence. A dependency guard and a **Krawczyk interval certification** of z\* (existence and uniqueness in a box of radius 10⁻³⁰) replace the floating-point claims. **New gates** F-M60.31–F-M60.39; **new non-claim** NC-M60.4. **148/148 PASS, 0 FAIL, exit 0\.** No corpus number is altered.  
**v1.3 (March 2026): the physical bridge, begun; three audit corrections; a reproducible environment.** An audit of v1.2 judged the paper to have no physical content because it constructs no ZS-S14 process, state or divisor. The objection is upheld about the *process* and answered about the *state*: the corpus already names the state, and v1.3 translates M\* onto it. **NEW THEOREMS.** **M60.30** the seam ℤ₂ acts on the ZS-A3 vacuum doublet ε \= ±1 by **exchange**, giving T(ρ\_E, Jρ\_EJ) \= √(n\_y²+n\_z²) \= 2|ρ\_SA| (DERIVED); Cor. M60.30a: **any S/A-diagonal state, in particular any thermal state at any temperature, has T \= 0 exactly** — vacuum degeneracy is worthless, only vacuum **coherence** counts. **M60.31** five exact ceilings on the ZS-S14 boundary state: purity ≥ **0.791361396140210**, linear entropy ≤ **0.208638603859790**, von Neumann entropy ≤ **0.363561460568423** nats \= 0.524508316220412 bits (**47.55% below** the ZS-Q7 capacity ln 2), and pure-state seam overlap ≤ **0.645969974317367** \= √(P(P+2))/(1+P) (PROVEN). **M60.32** decoherence budget ln(1 \+ ρ\_λ(π)) \= **0.270021845324850** e-folds (PROVEN) and, under the named hypothesis (H-RECIP), n\_max \= ln(1+ρ\_λ(π))/μ \= **2.351397458164148**, so **at most two complete Z-cycles can carry the phase**; the last passing value |**λ**|² \= 0.794796437962722 is the ZS-U12 power-survival factor, recorded and not built upon; ⌊n\_max⌋ \= 2 \= dim **Z** is an **OBSERVATION and a NON-CLAIM** (gate F-M60.44). **M60.33** the anchor’s **phase-dead core**: ε\_\*/σ \= √(−ln(1−M\*²)) \= **0.934882084184541**, and since ZS-A3 proves ε(r\_H) \= 0 the core has T \= 0 exactly, so the seam becomes phase-capable only outside a critical radius (DERIVED-CONDITIONAL on the kink/Gaussian profile). **CORRECTIONS.** (i) F-M54-16′ is conditional on **(F2) ∧ (F3)**, not (F3) alone, and **two** physical objects remain uncomputed, not one — the v1.2 *one number* phrasing is corrected. (ii) Thm M60.24 branch (a) is lowered to **CLOSED-NEGATIVE-CONDITIONAL on a ℤ₂-symmetric anchor fluctuation law**, since a symmetric potential does not force a symmetric state (gate F-M60.43). (iii) Thm M60.15 is lowered from HYPOTHESIS-strong to **TESTABLE REFORMULATION / HYPOTHESIS-weak**, because the Monte Carlo tests the neighbourhood of M\* and not an eleven-sector provenance. **REPRODUCIBILITY.** A pinned \`requirements.txt\` and a one-command \`RUN.md\` now ship with the paper, with tested interpreter and library versions; an audit could not re-run the v1.2 script for want of exactly this. **ANTI-NUMEROLOGY.** Executed on all six new reals: 217 formulas, **zero hits at 10⁻³**, p ∈ \[0.21, 0.78\]; none promoted. New gates F-M60.43–F-M60.49; new non-claim NC-M60.5. Ledger extended from 148 to **170 rows** by block N (22); **170/170 PASS, 0 FAIL, exit 0\.** No corpus number is altered and no v1.2 theorem is retracted.  
**v1.4 (March 2026): scope repair, independent re-verification, and compression.** A fourth audit found the v1.3 ceilings asserted for a general boundary state while their derivation assumed a two-dimensional carrier. The finding is **UPHELD and re-derived here**. **RETRACTIONS AND RESCOPINGS.** (i) **(H-DOUBLET-SUPPORT)** is named and gated (F-M60.50); it is shown **unremovable** — the pinching ᴿ(X) \= PXP \+ QXQ is a channel commuting with Ad\_J, so data processing gives T(ᴿρ, ᴿJρJ) ≤ T(ρ, JρJ) and a lower bound on the full state yields none on its doublet component. (ii) The purity and entropy ceilings are **false** without it: with ℤ₂ swapping two orthogonal m-dimensional blocks, T \= 1 while Tr ρ² \= 1/m, executed at m \= 2, 3, 5, 8 (rows O1–O2). **Thms M60.31–M60.33 are lowered from PROVEN to DERIVED-CONDITIONAL.** (iii) The conclusion’s *one number* is removed — **three** inputs remain. (iv) Route S is CONDITIONAL in every summary, not only in its theorem line. (v) §11A is retitled *a conditional translation*. **NEW THEOREM.** **M60.34 (General Ceilings, PROVEN, dimension-free):** Fuchs–van de Graaf converts T ≥ M\* into **F(ρ\_E, Jρ\_EJ) ≤ √(1−M\*²) \= 0.645969974317367** and **Tr(ρ\_E Jρ\_EJ) ≤ 1−M\*² \= 0.417277207719580**, with no doublet and no environment model; executed over 400 involutive pairs in dimensions 2–8 with zero violations. **RE-VERIFICATION.** Every printed constant is **independently re-derived by a second route** — z\* by damped iteration from a different seed, ρ\_λ(π) from the Poisson kernel, M\* from the optimal two-atom measure rather than the linear program, the ceilings from an explicit Bloch state — **24 for 24**, worst residual 4.4 × 10⁻¹⁰ set by corpus print precision (rows O10–O16). **REPRODUCIBILITY.** \`requirements.txt\` now hard-pins with \`==\` (v1.3 listed minima and was correctly refused); \`RUN.md\` gives one command; the interpreter version is stated. **COMPRESSION.** The 186-row ledger moves to the supplementary artifact \`zs\_m60\_ledger\_v1\_4.md\`; the three exploration cycles, the fifty falsification gates and the appendices are consolidated into tables. Length falls from 65 to under 45 pages with no theorem removed. Ledger extended from 170 to **186 rows** by block O (16); **186/186 PASS, 0 FAIL, exit 0\.** No corpus number is altered.  
**v1.5 (March 2026): clean copy. No mathematics changed.** A fourth audit judged v1.4 correct in content and closeable, and asked for five stale strings and one ledger-typing refinement. All six are applied and nothing else is touched. **TEXT CORRECTIONS.** (i) §1 no longer claims the release is TERMINAL; after the v1.2–v1.5 audits the classification is **TERMINAL-IN-SCOPE**, consistent with the title, §17 and the Conclusion. (ii) §17’s declaration named the wrong version and now reads **v1.5**. (iii) Code Availability described the v1.3 environment — 170 rows and \`≥\` minima — and now describes the shipped one: **186 rows, hard \`==\` pins**, CPython 3.12.3, with the note that the v1.4 set was **independently re-executed by an audit**, returning \`rows=186 declared=186 PASS=186 FAIL=0\`. (iv) The status-table entry *quantified and physically realized* overstated the position and now reads **quantified; conditionally translated onto the ZS-A3 vacuum doublet under (H-DOUBLET-SUPPORT), and not yet physically realized by the actual S14 boundary state**. (v) §17’s successor note said the gate turns on *a single number against a single number*; it now states that the **dimension-free** test of Thm M60.34 requires one comparison while the full physical identification additionally requires (F2) and the provenance of the boundary state, including whether (H-DOUBLET-SUPPORT) holds at all — **three** inputs, consistent with the Conclusion. **LEDGER RE-TYPING.** An audit observed that rows executing a random or model ensemble certify a universally quantified claim by **sampling**, which is a witness and not a proof. **24 rows are re-typed out of THEOREM-PROOF**: the count falls **121 → 97**, NUMERIC-WITNESS rises **12 → 35**, and one row moves to DECLARATION (20). The row set, the executions and the results are unchanged; only their honest classification is. **186/186 PASS, 0 FAIL, exit 0\.** No theorem is added, altered or withdrawn, no corpus number is touched, and the supplementary table ships as \`zs\_m60\_ledger\_v1\_5.md\`.  
