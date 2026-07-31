# **ZS-M59**

# **The Aliasing-Fiber Completion of the Formal Z-Spin QND Event**

*Complete Logarithm Classification, the Branch Torsor, Anchor Rigidity, and the Divisor Calculus of the Seam*

**Author:** Kenny Kang · **Affiliation:** Z-Spin Cosmology Collaboration

**Theme / Paper code:** Mathematical Spine — **ZS-M59 v1.8 · TERMINAL-IN-SCOPE** (supersedes v1.7 and earlier; full-length release)

**Date:** July 2026

**Parent (event):** ZS-S28 v3.1 TERMINAL · **Parent (comparison):** ZS-M46 v1.5 · **Successor seeded:** ZS-M60

**Companion:** \`zs\_m59\_verify\_v1\_8.py\` — one file, fixed-size fail-closed ledger, 148 rows

**Verification: 148/148 PASS** (82 THEOREM-PROOF · 31 NUMERIC-WITNESS · 3 PROXY · 30 GUARD · 2 IMPORTED) **| 0 FAIL | Zero Free Parameters** | (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED; **Q** enters only through named hypotheses.

**Status: TERMINAL-IN-SCOPE.** *The logarithm, positive-energy completion, branch-torsor, anchor-rigidity and finite-transversal divisor classifications are closed. The S14-derived seam transport, its closure prescription and θ-family, the physical anchor divisor, the eleven-dimensional carrier intertwiner, the pointer-preserving CPTP realization and F-M54-16′ are explicitly outside the completed scope and are transferred to the successor.* ZS-M59 is not incomplete because those remain open; it is closeable **because what it did and did not classify is now fully exhibited**. State-level faithfulness remains PROVEN in the canonical Hardy model and DERIVED-CONDITIONAL in its Z-Spin seam realization.

**Scope declaration.** Every object below derives from the **formal** pointer-QND event frozen by ZS-S28 v3.1, which proved that the declared Whitney/DEC/S14 reduction does **not** select a physical event (0 of 13 fields S14-derived). Nothing here is a statement about the physical ZS-S14 measurement event, and no result may be cited as one. The permitted claim form is: *the formal Z-Spin QND event admits, fails to admit, or fails to select a pointed positive-energy completion with specified invariants.*

**On this release.** v1.7 restored §§2–10 at full length. v1.8 preserves that text without deletion, adds the type correction of §11.2.1, the terminal-in-scope declaration of §15, and the retitled successor of §18.

# **What v1.8 corrects**

The v1.7 review found the manuscript ready to close in scope, subject to **one local type error**. It is upheld, and correcting it makes the paper internally consistent for the first time on this point: §17 had already said that the frozen path is open and carries no winding number, while §11.2's corollary used a winding theorem on it.

*Table 0\. The v1.7 review findings and their disposition.*

| \# | Finding | Verdict | Disposition |
| ----- | ----- | ----- | ----- |
| 1 | **Corollary M59.21b applies a closed-loop winding theorem to an open path.** ZS-S28's a(s) \= exp(sℓ) runs from 1 to **λ** ≠ 1 and carries no θ-index, so Theorem M59.21(1) — which is about continuous **closed loop families** over 𝕋\_θ — does not apply | **UPHELD; the v1.7 corollary is a type error** | Retracted. Replaced by three statements (§11.2.1, rows T1–T5): **(a)** the honest and trivial fact that a single path has no θ-dependence and therefore carries no field at all; **(b)** an executed **closure-dependence counterexample** — the same open path admits a closure of winding **0** (straight segment back) and one of winding **1** (argument carried on through 2π), neither passing through the origin, so the prescription *is* the datum; **(c)** the corrected **Corollary M59.21b′ \[DERIVED-CONDITIONAL\]**. Also re-typed: ZS-S28's "winding zero" is a statement about the **continuous lift** of an open path — ZS-M58 layer L2 — not a loop winding number. |
| 2 | Fix required in four places: the Abstract's seed sentence, Corollary M59.21b, verifier rows N6 and S2 | **UPHELD** | All four corrected in this release; N6 and S2 claim strings rewritten (block T, and the desync rule of §13.5). |
| 3 | "Not TERMINAL" invites indefinite revision; the correct status is **TERMINAL-IN-SCOPE** | **UPHELD** | Adopted, with an explicit scope table (§0 and §15). |
| 4 | The successor title *The Anchor Divisor of the Seam* presupposes that a divisor exists | **UPHELD** | Retitled \**ZS-M60,* The S14 Seam-Transport Dichotomy: Nonvanishing Rigidity or Anchor-Divisor Selection\***, with** D \= 0 declared a complete result\*\* — a no-go for intrinsic branch selection along the S14 path — rather than a failure (§17). |
| 5 | M60 should be limited to four deliverables and no papers reserved beyond it | **UPHELD** | §17 lists exactly four; no successor beyond M60 is registered, and the reason is stated. |

**What the correction bought.** A number the paper had been leaning on turns out to be a *choice*: the winding of the closed extension of the frozen path is **0 for one closure and 1 for another**, both admissible, neither singular. That is the sharpest possible statement of why ZS-M60's first deliverable is a closure prescription and not a calculation — and it removes the last place where this line inferred a structural conclusion from an object it had not constructed.

# **§0. Abstract**

ZS-S28 v3.1 constructed an exact formal pointer-QND channel with multiplier **λ**, together with its pointed minimal unitary dilation, and proved that the principal logarithmic suspension is bounded and cannot match the ZS-M46 positive-energy generator, while other positive logarithms exist. The remaining question was not existence but **selection**.

**Classification.** Every self-adjoint logarithm of the minimal event unitary is a measurable integer branch p(θ) \= θ \+ 2πn(θ) (Thm M59.2, PROVEN). Each selects one **section** of the integer alias bundle and carries its cyclic measure on a translated set of total Lebesgue measure exactly 2π (Thm M59.3, PROVEN) — even when its spectrum closes to \[0,∞). The ZS-M46 translation, sampled at unit time, folds by an exact direct integral into a circle representation of countably infinite alias multiplicity (Thm M59.4, PROVEN); since spectral multiplicity is a complete unitary invariant, **no logarithm on the minimal dilation is the M46 generator** (Thm M59.5, CLOSED-NEGATIVE).

**Completions.** Alias-disintegration embeddings exist for every measurable unit field and reproduce identical integer moments (Thms M59.6–7, PROVEN), so the event selects no completion. A pointed completion is unitarily equivalent to the M46 pair **at generator level** iff its spectral measure is equivalent to dp iff its alias field is non-vanishing a.e. (Thm M59.12, Support Dichotomy); consequently the ZS-S28 gate B4-general splits, its generator, multiplicity and measure-class clauses closing positively and automatically, leaving only the pointing. The completion set 𝔐 is convex and **not** weak-\\ *compact, compactness holding exactly on the energy slices 𝔐\_E for E ≥ E\_min \= 2.31340315203018; its extreme points are exactly the transversal-carried completions, which are exactly the same-space logarithms, and every completion is an explicit inverse-CDF barycentre of them (Thm M59.13, PROVEN). Demanding λ^t on any nonempty open interval forces, by Schwarz reflection and Bochner uniqueness, the Cauchy measure of location χ \+ 2πk, whose negative-axis weight δ\_neg^{(k)} \= (1/π)arctan(μ/(χ+2πk)) is strictly positive on every branch, equal to 0.0161653528682918434*\* at k \= 0 (Thm M59.14). Maximum entropy at fixed energy is the θ-independent geometric field, so the Gibbs route is exactly one-parameter (Thm M59.17).

**Comparison.** No positive-energy standard pair has U\_event as unit-time element (Thm M59.9), and no **ray** of the M46 one-particle space is invariant under its translations or modular dilations, since both generators are purely absolutely continuous (Thm M59.18); the pointed clause of the comparison is therefore **UNDECLARED**. Transported structural Fock data are constant across full-support completions, while coherent states on ℛ(H) separate the canonical representatives with the exact dual norm **sup{|Im⟨δ,h⟩| : h ∈ H, ‖h‖ ≤ 1} \= ‖δ‖/√2** (Thm M59.11).

**The residual.** 𝔏 is a torsor under 𝒢 \= L⁰(\[0,2π); ℤ), and the event, seeing only e^{ip}, is invariant under all of 𝒢, so **the event data alone distinguish no origin**; ZS-M57 T.2′ and ZS-M58 layer L2 are the **constant subgroup** ℤ \< 𝒢 (Thm M59.19). **Anchor Rigidity** (Thm M59.21): a continuous nonvanishing family of seam transport loops has constant winding, so a non-constant branch field **requires** a degeneracy locus, while the converse needs a transverse crossing of nonzero net local degree; the field is then piecewise constant with jump divisor D of degree zero, and **\#supp D ≥ V** while **‖D‖ ≥ 2(V−1)**, both sharp and in different currencies.

**Divisor calculus** (Thm M59.22, for finite transversal transports). The divisor determines the minimal admissible field n\_D \= S\_D − min S\_D, the additive constant being fixed by the predeclared rule S1. The energy is the harmonic pairing

**E(D) \= E\_min \+ 2π \[ n₀(D) \+ Σⱼ mⱼ F(θⱼ) \],     F(θ) \= μ\_λ((θ, 2π))**

verified against quadrature to 1.6 × 10⁻¹⁹, with **F in closed form** and **E\_min \= ∫₀^{2π}F**. The anchor cost obeys **E(D) ≤ E\_min \+ π‖D‖**. The wrapped-Cauchy CDF is (2/π)arctan(κ tan(a/2)); its **half-mass radius is a\_{1/2} \= 2 arctan(inf ρ\_λ) \= 0.114583066682673187**, not μ; and F varies most steeply near χ, so signed configurations straddling χ carry the largest contribution.

**What the frozen path does and does not give (corrected at v1.8).** ZS-S28's endpoint path a(s) \= exp(sℓ) is **open** — a(0) \= 1, a(1) \= **λ**, |a(1)−a(0)| \= 1.711032173 — and carries **no θ-index**. Theorem M59.21(1), a statement about continuous **closed loop families**, therefore does not apply to it. What is true is trivial and honest: **a single path has no θ-dependence, so it carries no field**, which is why ZS-M57 and ZS-M58 each found one integer. Moreover the winding of a closed extension is **not determined** by the open path: closing by the straight segment gives winding **0**, closing by carrying the argument through 2π gives **1**, and neither closure meets the origin (Thm M59.24). ZS-S28's recorded "winding zero" is a statement about the **continuous lift** ending inside the principal branch — ZS-M58 layer L2 — not a loop winding number.

**Seed.** ZS-M60 is therefore a **dichotomy**, not a divisor computation: construct the closure prescription and the θ-family from the S14 action, then decide between **nonvanishing rigidity** (D \= 0, the field is constant, a complete no-go for intrinsic branch selection along that path) and **anchor-divisor selection** (D ≠ 0, and §11.3 computes the field and its energy). Verification 148/148 PASS. Zero free parameters. No physical S14 clock is claimed.

# **Epistemic Status Legend**

| Status | Meaning in this paper |
| ----- | ----- |
| **PROVEN** | Complete analytic proof given here; no undischarged assumption. |
| **IMPORTED-PROVEN** | External theorem used at its exact hypotheses, cited, not re-proved. |
| **DERIVED** | Follows from frozen inputs and PROVEN steps; no new parameter. |
| **DERIVED-CONDITIONAL** | Exact under named, falsifiable hypotheses carried in the theorem line. |
| **CANDIDATE** | A construction satisfying every admissibility axiom but requiring a selection principle not derived here. |
| **CLOSED-NEGATIVE** | A route excluded under stated premises. |
| **CLOSED-VACUOUS** | A gate that closes trivially by construction and carries no information. |
| **TERMINAL-IN-SCOPE** | The declared classification is complete; named items lie outside it and pass to the successor. *(New at v1.8.)* |
| **UNDECLARED** | Neither supplied nor proven impossible. |
| **REFORMULATED** | Shown not to be one well-posed question; re-expressed without being answered. |
| **COMPARISON-DEFINED** | Defined by pulling ZS-M46 data backward; **not** event-derived. |
| **OBSERVATION** | A numerical or structural coincidence recorded without identification. |
| **PROXY** | Finite truncation or finite model; never evidence for the infinite target. |
| **NON-CLAIM / OPEN / RETRACTED** | Outside scope / well-typed unresolved node / shown false, retained with its refutation. |

**Ledger tiers and rules (cumulative).** Rows are THEOREM-PROOF, NUMERIC-WITNESS, GUARD, PROXY or IMPORTED. A claim string asserts only what its computation tests. Every universally quantified claim ships with an executed counterexample attempt. Group-theoretic vocabulary requires its own rows (closure, invertibility, transitivity, fixed points). A separation claim must ship with the explicit obstruction it rules out. A quantitative adjective requires its constant, and a bound must name its currency. **New at v1.7: an "exact" claim may not be certified by a tolerance test; exactness and approximation occupy separate rows.** **148/148 PASS is the integrity of a ledger, not the peer review of a manuscript.**

# **Pre-registered outcomes**

| Outcome | Trigger | Terminal conclusion |
| ----- | ----- | ----- |
| **A** | M59.5 proved; no intrinsic selector survives | Minimal clock impossible; enlarged compatibility generic |
| B | Unique intrinsic alias selector matching ZS-M46 | The formal event selects the M46 one-particle clock |
| C | Finite selector class, all pointed-standard-pair equivalent | Clock fixed up to a declared gauge |
| **D** | Infinite selector family remains | Positive-energy completion exists but is non-identifying |
| E | Intrinsic selector exists but standardness fails | Modular clock CLOSED-NEGATIVE |
| F | Standard pair exists but differs from ZS-M46 | Event clock exists; M46 identity CLOSED-NEGATIVE |
| J | ZS-M46 data used to choose the field or the real subspace | Compatibility demonstration only; derivation claim INVALID |
| K | The formal event called the physical S14 event *\[PROHIBITED-FORM, quoted for the guard\]* | Scope violation; release FAIL |

**Outcomes A and D fired jointly.** B, C, E, F did not fire. J and K did not fire (guards R1, W1).

# **Construction / comparison firewall**

**Artifact A — formal event, available.** ZS-S28 v3.1 pointer matrix units and pointer observable; formal Kraus/Choi data; multiplier **λ**; pointed minimal dilation and harmonic measure; the formal endpoint path; the eleven-dimensional collision carrier. Status: **FORMAL / TARGET-INSTANTIATED / NOT S14-DERIVED.**

**Artifact B — physical S14 event, unavailable.** The declared reduction did not select the event (ZS-S28 §4.2).

**One-way rules, obeyed throughout.** ZS-M59 reads Artifact A and ZS-M46. It does not modify any ZS-S28 field; does not use ZS-M46 to choose a branch, alias profile, instrument or pointing and then relabel the result event-derived; does not feed any ZS-M59 construction backward into ZS-S28; and does not count a comparison-defined embedding as a derivation. All event-side objects of §§2–8 and §11 are constructed and frozen before §9 loads any M46 datum; §§2–8 contain no occurrence of an M46 quantity (guard R1).

# **§1. Frozen inputs, conventions, and the gate table**

## **1.1 The frozen data**

**λ \= −0.566417330285464403 \+ 0.688453227107702130 i**

**r \= |λ| \= 0.891513565776047 ,     χ \= arg λ \= 2.259249553902599 ,     μ \= −ln r \= 0.114834624996010**

**R \= χ/μ \= 19.6739402770 ,     (𝒦\_event , U\_event , Ω\_event) \= ( L²(𝕋, μ\_λ) , M\_z , 1 )**

**dμ\_λ \= ρ\_λ(θ) dθ / 2π ,     ρ\_λ(θ) \= (1 − r²) / |e^{iθ} − λ|²**

All are reproduced from ZS-M1's z *alone: λ \= (iπ/2)z* matches the ZS-S28 printed multiplier to 10⁻¹⁶ (row A1), and r, χ, μ, R match ZS-S28 / ZS-M46 / ZS-M57 to their last printed digits (row A2). Total mass 1 to 10⁻³⁰ (row A4); pointed moments ⟨Ω, UⁿΩ⟩ \= **λ**ⁿ for n \= 0…8 with maximum error **2.57 × 10⁻⁴¹** (row A5).

Also frozen and load-bearing: the **eleven-dimensional collision carrier**, which reproduces the channel to 1.11 × 10⁻¹⁶ with real positive environment overlap 0.891513565776047 and evades the ZS-M56 tensor-factor no-go; and the **endpoint path a(s) \= exp(sℓ)**, ℓ \= −μ \+ iχ, nonvanishing and **open** — a(0) \= 1, a(1) \= **λ**, |a(1) − a(0)| \= **1.711032173** (row T1); its recorded "winding zero" is re-typed in §11.2.1 as a statement about the continuous lift.

## **1.2 Conventions, declared once**

**Normalization (guard W2).** dμ \= ρ dθ/2π, total mass 1\. The alias-disintegration equation therefore reads Σ\_k |ψ(θ+2πk)|² \= ρ\_**λ**(θ)/2π; omitting the 2π makes the embedding isometry wrong by exactly that factor.

**Unit and branch (required by ZS-M57 F-M57.Y2).** "Unit time" is the ZS-M46 Abel unit translation u ↦ u+1 of Theorem M46.3A, and every fractional time is a fraction of that unit. The principal branch χ ∈ (0,2π) is declared; §7.4 gives the branch-complete statements.

**Exactness upgrade, not a retraction (rows A3, A3g).**

**inf ρ\_λ \= (1 − r)/(1 \+ r) \= 0.0573542987937511 ,     sup ρ\_λ \= (1 \+ r)/(1 − r) \= 17.4354847157325**

ZS-S28's printed maximum 17.4354846876 is a 200 000-point grid sample lying **2.81 × 10⁻⁸** below the true supremum; its printed minimum agrees to 6.2 × 10⁻¹². This paper uses the closed forms as THEOREM-PROOF and records the ZS-S28 figures as NUMERIC/grid. **No ZS-S28 field is altered.** Likewise ZS-S28's exponential residuals 8.01 × 10⁻¹⁶ and 4.46 × 10⁻¹⁰ are float64 artifacts of large-argument exponentials: at 40 digits all three branch residuals are ≈ 10⁻⁴⁰ (rows C2–C4), and ZS-S28's PROXY typing of the unbounded row is inherited (guard C5).

## **1.3 Gate table**

*Table 1\. Every gate at ZS-M59 v1.8.*

| Gate | Content | Status |
| ----- | ----- | ----- |
| **B0** | input freeze, Artifact A/B firewall | **EXECUTED** (§1, guard R1) |
| **B1** | pointed minimal dilation and harmonic measure | **DERIVED** (Thm M59.1; precedent ZS-M58.6) |
| **B2a** | classify all same-space self-adjoint logarithms | **PROVEN** (Thm M59.2) |
| **B2b** | fold ZS-M46 at unit time; compute multiplicity | **PROVEN** (Thm M59.4) |
| **B2c** | section versus bundle; minimal equivalence | **PROVEN / CLOSED-NEGATIVE** (Thm M59.5) |
| **B3** | intrinsic completion, real subspace, pointing | **Above:** a 𝒢-torsor coordinate; the event data alone distinguish no origin (Thm M59.19). **Restricted:** only piecewise-constant fields with a degree-zero divisor are realizable by finite transversal transports (Thm M59.21). **Given D:** the field is determined by the predeclared rule S1 (Thm M59.22(i)). **From the action:** OPEN (§17) |
| **B4-principal** | principal branch versus ZS-M46 | **CLOSED-NEGATIVE** (ZS-S28) |
| **B4-general** | generator support, multiplicity, cyclic measure, real subspace, pointing | **SPLIT**: generator / multiplicity / measure-class clauses close **automatically** (Thm M59.12); real-subspace clause closed negatively at pair level on the minimal space (Thm M59.9); **pointing clause UNDECLARED on the M46 side** (Thm M59.18) and a Z-bias field on the event side |
| **B5** | explicit one-particle intertwiner | **CLOSED** in its well-posed form: W\_c is canonical for every full-support completion |
| **B6 / B7** | second quantization; Connes cocycle | **CLOSED-VACUOUS for transported structures**; the state-level route is faithful (Thm M59.11(b)) |
| **HP-noise** | repeated-interaction limit | coefficients imported; convergence OPEN; **not a clock substitute** |
| **F-M54-16′ / Artifact B** | physical realization | **OUTSIDE SCOPE**, transferred to ZS-M60 (§15, §18) |

# **§2. The pointed minimal event dilation**

**Theorem M59.1 (Minimal Event Dilation). \[DERIVED\].** The triple (L²(𝕋, μ\_**λ**), M\_z, **1**) has spectral multiplicity one, full-circle support, and cyclic spectral measure μ\_**λ** equivalent to Lebesgue measure.

*Proof.* ρ\_**λ** is continuous on the compact circle with inf \> 0 and sup \< ∞ (§1.2), hence μ\_**λ** ≡ dθ; therefore supp μ\_**λ** \= 𝕋 and σ(U\_event) \= 𝕋. Multiplication by √ρ\_**λ** is unitary L²(μ\_**λ**) → L²(dθ/2π) and intertwines M\_z with M\_z, so U\_event is unitarily equivalent to the bilateral shift of multiplicity one. Since trigonometric polynomials are dense in L²(𝕋, μ\_**λ**), Ω \= **1** is cyclic for the unitary (both powers). □

**Internal precedent, consumed not re-derived.** ZS-M58 v1.7 Theorem M58.6 (*Unpointed Dilation Non-Identifiability*, PROVEN) establishes the sharper statement that **every** strict scalar contraction has the *same* unpointed multiplicity-one bilateral shift, the parameter migrating entirely into the cyclic vector. Two consequences are load-bearing. First, M59.1 is an instance of a corpus theorem. Second — and this is why the whole paper is written in pointed language — **unpointed comparison with ZS-M46 is vacuous**: it cannot distinguish our event from any other scalar contraction. M58.6 also records that W V W\* \= U\_M46(1) is ill-typed for an isometric V, which is why §6 uses isometric embeddings J\_c and §9 uses unitaries only between completions.

**Numerical witness (row B3).** The Gram matrix of {UⁿΩ}\_{n=−12…12} is the Toeplitz matrix of the moment sequence; its least eigenvalue is **0.07056008 \> 0**, consistent with the theoretical bound λ\_min ≥ inf ρ\_**λ** \= 0.0573542988. Positive definiteness is the numerical face of cyclicity together with multiplicity one.

# **§3. Classification of every self-adjoint logarithm**

**Theorem M59.2 (Complete Logarithm Classification). \[PROVEN\].** Let P be self-adjoint on 𝒦\_event with e^{iP} \= U\_event. Then P is multiplication by a real measurable function of the form

**p\_n(θ) \= θ \+ 2π n(θ) ,     n : \[0, 2π) → ℤ  measurable**

and conversely every such p\_n defines a self-adjoint logarithm. Positivity of P is n(θ) ≥ 0 almost everywhere in the \[0,2π) convention.

*Proof.* U\_event \= e^{iP} is a Borel function of P, so every spectral projection of P commutes with U\_event; equivalently P is affiliated with the commutant U′\_event. By Theorem M59.1 the multiplicity is one, so U′\_event \= L^∞(𝕋, μ\_**λ**) is maximal abelian, and a self-adjoint operator affiliated with a maximal abelian multiplication algebra is itself multiplication by a real measurable function p. Then e^{ip(θ)} \= e^{iθ} for μ\_**λ**\-a.e. θ; since μ\_**λ** ≡ dθ this holds a.e.-Lebesgue, so p(θ) − θ ∈ 2πℤ pointwise a.e., and measurability of p gives measurability of n \= (p − θ)/2π. The converse is immediate. □ *(Expanded argument in Appendix B.1.)*

**Branch discipline (mandatory).** ZS-M57 v1.8 Theorem M57.T.2′ proved that a channel determines Arg **λ** only modulo 2π and therefore selects **no branch** of the generator logarithm; its gates F-M57.V1 and F-M57.Y2 forbid any successor from reporting a branch-dependent quantity without declaring the branch. Accordingly every logarithm in this paper carries a branch identifier, and no statement about one branch is summarized as a statement about all.

*Table 2\. The three declared branches, with exponential residuals at 40 digits.*

| Branch id | n(θ) | spectrum | bounded | positive | residual of e^{iP} \= U\_event |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **B-pr** (principal) | 0 on \[0, π), −1 on \[π, 2π) | \[−π, π\] | yes | **no** | 4.14 × 10⁻⁴¹ |
| **B-plus** | ≡ 0 | \[0, 2π\] | yes | yes | 0 |
| **B-dense** | ⌊−log₂(1 − θ/2π)⌋ | unbounded ⊂ \[0, ∞) | **no** | yes | 7.21 × 10⁻⁴⁰ |

**Cross-paper resonance, of record.** ZS-F32 v1.5 Theorem F32.2 proves the identical integer-indexed structure one level down: every population-fixing phase-covariant generator realizing **λ** is G\_n with ω\_n \= ω \+ 2πn, n ∈ ℤ, and F32 explicitly records that its own earlier "unique generator" claim was false because the family is complete. Theorem M59.2 is the self-adjoint-logarithm face of F32.2. This matters for §7: F32.3 rates the *selection* of the principal branch by norm-minimality as **PROVEN \+ DERIVED-CONDITIONAL on a least-action principle**, not as a derivation, and ZS-M59 inherits that ceiling exactly.

# **§4. The section measure-class obstruction**

**Theorem M59.3 (Section Measure-Class). \[PROVEN\].** Let E\_k \= {θ ∈ \[0,2π) : n(θ) \= k}. The spectral image of P\_n is S\_n \= ⋃\_{k}(E\_k \+ 2πk); the translated pieces are pairwise disjoint modulo null sets, so

**m(S\_n) \= Σ\_k m(E\_k) \= 2π     for every branch, bounded or not**

The cyclic spectral measure ν\_n \= (p\_n)\_*μ\_λ is equivalent to Lebesgue measure restricted to S\_n, with density inherited from ρ\_λ*\*.

*Proof.* E\_k \+ 2πk ⊂ \[2πk, 2π(k+1)), so the translated pieces lie in disjoint windows; {E\_k} partitions \[0, 2π); translation preserves Lebesgue measure. p\_n is injective on each E\_k, and μ\_**λ** ≡ dθ, giving the equivalence and the density. □

**Consequences.** (i) P\_n may be bounded or unbounded. (ii) Its spectrum may have closure \[0, ∞). (iii) Nevertheless its cyclic measure class is carried by a set of finite Lebesgue measure 2π. (iv) It is therefore **never** equivalent to full Lebesgue measure on ℝ₊.

**Negative control (row D3) — spectrum is not measure class.** Let E\_k be a union of 2^{k+1} intervals of total length 2π·2^{−(k+1)}, distributed uniformly across \[0, 2π). Then the maximum gap of S\_n inside window k is 2π/2^{k+1} — measured at **3.835 × 10⁻⁴** by k \= 13 — so S\_n is dense in \[0, ∞) and σ(P\_n) \= \[0, ∞), while m(S\_n) \= 2π exactly. This is the precise content of the warning ZS-S28 attached to its unbounded-branch row, and it forbids inferring M46 compatibility from σ(P\_n) \= \[0, ∞).

# **§5. Folding the ZS-M46 translation, and the minimal no-go**

Before any comparison, the mandatory category table (gate F1 of the inherited failure ledger).

*Table 3\. Category table for the unit-step comparison.*

| field | event side | ZS-M46 side |
| ----- | ----- | ----- |
| carrier | L²(𝕋, μ\_**λ**) | L²(ℝ₊, dp) |
| scalar field | complex-linear | complex-linear |
| operator type | unitary M\_z | unitary group U(t), self-adjoint generator P \= M\_p ≥ 0 |
| boundedness | bounded unitary | P unbounded, domain C\_c^∞(ℝ₊) declared in ZS-M46 §4 |
| spectrum | 𝕋 | \[0, ∞) |
| multiplicity | 1 (Thm M59.1) | of U(1): ℵ₀ (Thm M59.4) |
| pointing | Ω \= **1**, cyclic | **none declared, and none ax+b-natural** (Thm M59.18) |
| real structure | §8 | canonical standard pair (H, U), IMPORTED-PROVEN |

**Theorem M59.4 (M46 Unit-Step Folding). \[PROVEN\].** Define

**ℱ : L²(ℝ₊, dp) → L²( \[0, 2π), dθ ; ℓ²(ℕ₀) ) ,     (ℱψ)(θ)\_k \= ψ(θ \+ 2πk)**

Then ℱ is unitary and ℱ U\_M46(1) ℱ^{−1} \= M\_{e^{iθ}} ⊗ I\_{ℓ²(ℕ₀)}, so the multiplicity function of U\_M46(1) is ℵ₀ almost everywhere, whereas that of U\_event is 1\.

*Proof.* ℝ₊ \= ⨆\_{k≥0}\[2πk, 2π(k+1)) up to a null set; Tonelli gives ‖ψ‖² \= Σ\_k ∫₀^{2π}|ψ(θ+2πk)|²dθ \= ‖ℱψ‖², and surjectivity holds on the dense set of finitely supported fiber sequences. For the unit step, (U\_M46(1)ψ)(p) \= e^{ip}ψ(p) and e^{i(θ+2πk)} \= e^{iθ} for every k, so the fiber index is invisible and the action is the scalar M\_{e^{iθ}} on each fiber. □

**Theorem M59.5 (Minimal Clock Non-Equivalence). \[PROVEN / CLOSED-NEGATIVE\].** U\_event ≄ U\_M46(1) as unitary representations, and no same-space logarithm P\_n carries the Lebesgue measure class of ℝ₊. Hence **no logarithm on the minimal ZS-S28 dilation is the ZS-M46 generator.**

*Proof.* Two independent arguments. (a) Spectral multiplicity is a complete unitary invariant (Hahn–Hellinger; Halmos): 1 ≠ ℵ₀ by Theorems M59.1 and M59.4. (b) Measure class: ν\_n is carried by a set of Lebesgue measure 2π (Theorem M59.3), while dp is not. □

**Scope.** This excludes neither a non-minimal positive-energy extension whose unit-step compression contains the event (§6), nor a completion built on an enlarged carrier. It is scoped to the minimal dilation and to nothing else.

**Verification typing (row E2).** A K \= 400 truncation reproduces folding-norm preservation to **3.09 × 10⁻⁴** relative. This is labelled **PROXY**: a finite truncation cannot certify ℵ₀ and is barred from the theorem tables.

# **§6. Universal alias-fiber embeddings, and the Support Dichotomy**

## **6.1 The missing object**

The unit-step unitary records e^{ip} \= e^{iθ} and forgets the integer k in p \= θ \+ 2πk. A logarithm on the minimal space chooses one integer per phase — a measurable **section**. The M46 carrier holds every nonnegative alias — the full **bundle**. To pass from one to the other one must supply a measurable unit vector field

**c(θ) \= ( c₀(θ), c₁(θ), … ) ∈ ℓ²(ℕ₀) ,     Σ\_{k≥0} |c\_k(θ)|² \= 1  a.e.**

The event determines the *sum* over aliases and nothing else.

## **6.2 The embedding theorem**

**Theorem M59.6 (Alias-Disintegration Embedding). \[PROVEN\].** For any measurable unit field c, the map

**(J\_c f)(θ)\_k \= √( ρ\_λ(θ) / 2π ) · c\_k(θ) · f(θ)**

is an isometry L²(𝕋, μ\_**λ**) → L²(\[0,2π); ℓ²(ℕ₀)) satisfying J\_c U\_event \= U\_M46(1) J\_c. The embedded vector Ψ\_c, written on the half-line as ψ\_c(θ+2πk) \= √(ρ\_**λ**(θ)/2π)·c\_k(θ), obeys

**Σ\_{k≥0} | ψ\_c(θ \+ 2πk) |² \= ρ\_λ(θ) / 2π**

and reproduces every integer moment: ⟨Ψ\_c, U\_M46(n)Ψ\_c⟩ \= **λ**ⁿ for all n ≥ 0\. If ψ\_c ≠ 0 almost everywhere on ℝ₊ then Ψ\_c is cyclic for the continuous generator P \= M\_p.

*Proof.* Isometry is the stated normalization together with Σ\_k|c\_k|² \= 1\. Intertwining: U\_M46(1) acts as the *scalar* e^{iθ} on each alias fiber (Theorem M59.4), so J\_c intertwines it with M\_z. Moments reduce to the circle moments of μ\_**λ** because the alias phase e^{2πink} \= 1\. Cyclicity: for ψ ≠ 0 a.e., {f·ψ : f ∈ C\_c(ℝ₊)} is dense in L²(ℝ₊, |ψ|²dp). □

**Theorem M59.7 (Universal Compatibility / Non-Selection). \[PROVEN\].** The field c is arbitrary subject to unit norm; hence the formal event does **not** select a positive-energy completion, and compatibility with a positive-energy clock is generic and non-identifying. A construction that obtains c from ZS-M46 data is a representation of the event, **COMPARISON-DEFINED**, and not a derivation of the M46 clock from the event.

**Gauge, correctly typed (row N4).** The unitary class of a pointed cyclic representation depends only on the spectral measure ν\_c \= |ψ\_c|²dp. Therefore multiplication by any measurable unimodular φ(p) is a **true gauge**: it commutes with P\_c and preserves *all* moments, including non-integer ones. By contrast a measurable fiber unitary V(θ) ∈ U(ℓ²(ℕ₀)) generally changes |c\_k|² and so moves between *inequivalent* classes. The non-uniqueness of M59.7 is a genuine moduli space, not a single orbit.

## **6.3 Four executed fields**

*Table 4\. Executed alias fields. All reproduce λⁿ for n \= 0…6 to 1.48 × 10⁻³⁰ (row G3).*

| id | field | full support | cyclic | E\[p\] |
| ----- | ----- | ----- | ----- | ----- |
| **F1** | section k ≡ 0 (equals the ZS-S28 θ₊ branch) | no | no | **2.313403** (minimum) |
| **F2** | two-alias, |c₀|² \= |c₁|² \= ½ | no | no | 5.454996 |
| **F3** | reflection-folded canonical unfolding (§7.5) | yes | yes | **\+∞** (log-divergent) |
| **F4** | geometric q \= ½ | yes | yes | 8.596588 |

F4 was presented in v1.0 as a "prohibited control carrying a free parameter". Theorem M59.17 shows it is in fact the **maximum-entropy field at its own energy**; it remains barred from primary selection, but the reason is now a theorem rather than a bookkeeping rule.

## **6.4 The Support Dichotomy**

**Theorem M59.12 (Support Dichotomy, with disjoint refinement). \[PROVEN\].** Let 𝒦\_c be the continuous-cyclic span of Ψ\_c and ν\_c \= |ψ\_c|²dp.

**Dichotomy.** (𝒦\_c, U\_c(t)) ≅ (L²(ℝ₊,dp), U\_M46(t)) **iff** ν\_c ≡ dp **iff** ψ\_c ≠ 0 a.e., the equivalence being implemented by the canonical unitary

**W\_c : 𝒦\_c → L²(ℝ₊, dp) ,     (W\_c g)(p) \= g(p) · |ψ\_c(p)|**

which carries Ψ\_c to |ψ\_c|.

**Refinement (disjoint).** The non-equivalent class splits as **Type I** — ν\_c carried by a measurable transversal, equivalently extreme in 𝔐 — and **Type II** — ψ\_c vanishes on a set of positive measure but ν\_c is not transversal-carried.

*Proof.* 𝒦\_c \= L²(ℝ₊, ν\_c) with P\_c \= M\_p by construction, and J\_c𝒦\_event ⊂ 𝒦\_c because J\_cf \= (f∘π)(P)Ψ\_c with π(p) \= p mod 2π bounded measurable, so admissibility A2, A3, A5, A6 hold. The map g ↦ g|ψ\_c| is unitary L²(ν\_c) → L²(dp) precisely when ν\_c ≡ dp, i.e. when ψ\_c ≠ 0 a.e., and it manifestly commutes with multiplication by p. □ *(Rows K-full, K-part: isometry deviation 0.00, intertwining residual 1.59 × 10⁻¹⁴.)*

**Corollary M59.12a (B4-general splits). \[PROVEN\].** For every full-support completion the clauses *generator representation*, *spectral multiplicity* and *cyclic measure class* close positively and automatically; the only non-automatic invariant is ν\_c — the pointing.

**Corollary M59.12b. \[PROVEN, source-verified\].** ZS-M46 v1.5 §4 declares the carrier L²(ℝ₊,dp), the translation, the positive generator, the dilation D \= ½ \+ p∂\_p on C\_c^∞(ℝ₊), and by Theorem A(i) the *unique irreducible standard pair* (H, U). It declares **no one-particle pointing**: the words "pointing", "pointed" and "vector" do not occur in ZS-M46 v1.5, and its only Ω is the Fock vacuum of Theorem A′. §8 shows that no ax+b-natural pointing exists either.

# **§7. The completion set and the selection problem**

## **7.1 Admissibility**

A completion 𝔠 \= (𝒦\_c, U\_c(t), P\_c, Ψ\_c, H\_c^ℝ, J\_c) is admissible only if: **A0** the ZS-S28 data are read from the frozen artifact and never changed; **A1** the field is constructed without ZS-M46 spectral vectors, standard subspaces or target cocycles; **A2** J\_cU\_event \= U\_c(1)J\_c; **A3** ⟨Ψ\_c, U\_c(n)Ψ\_c⟩ \= **λ**ⁿ; **A4** P\_c ≥ 0; **A5** Ψ\_c is cyclic for the continuous generator; **A6** no proper reducing subspace contains J\_c𝒦\_event and is U\_c-invariant; **A7** H\_c^ℝ ∩ iH\_c^ℝ \= {0} and H\_c^ℝ \+ iH\_c^ℝ dense; **A8** half-sided invariance; **A9** the pointing reduces to the ZS-S28 pointing under integer-time compression; **A10** no free temperature, decay profile, alias weight, smoothing width, entropy multiplier or branch cutoff is tuned; **A11** ZS-M46 data load only after the event completion is serialized; **A12** the semantic pairs *existence / selection*, *section / bundle*, *spectrum / measure class*, *unit-step multiplicity / generator multiplicity*, *complex Hardy space / standard real subspace*, *compatibility / derivation*, *one-particle closure / Fock closure*, *central cocycle / weight preservation*, *formal event / physical S14 event* are never conflated.

By **A10** the forms q \= r, q \= r², β \= −log r, β \= χ are **prohibited as primary selectors** and may appear only as pre-registered null families.

## **7.2 The convex structure of 𝔐**

Write 𝔐 \= {ν ≥ 0 on ℝ₊ : Σ\_{k≥0} ν(θ+2πk) \= ρ\_**λ**(θ)dθ/2π}. Disintegrating over the phase identifies 𝔐 with the measurable Markov kernels θ ↦ w(θ) ∈ 𝒫(ℕ₀), via dν \= w\_k(θ)dμ\_**λ**(θ) in folded coordinates.

**(a) Convex, bounded — but NOT compact. \[PROVEN\].** 𝔐 is convex and contained in the probability measures. It is **not** weak-\\ *compact: let ν\_N be the transversal with n ≡ N; for every f ∈ C\_c(ℝ₊), ∫f dν\_N → 0, so ν\_N → 0 vaguely and 0 ∉ 𝔐 (row V4: 0.5534, 1.07 × 10⁻⁴³, 4.02 × 10⁻³⁵⁵, 1.59 × 10⁻¹⁵⁵⁹, 7.18 × 10⁻⁶⁵⁴⁰ for N \= 0, 2, 5, 10, 20 with a Gaussian test function centred at p \= 3).* The v1.0 claim of compactness is RETRACTED.\*

**(b) Compactness restored exactly on energy slices. \[PROVEN\].** 𝔐\_E \= {ν ∈ 𝔐 : ∫p dν ≤ E} is convex (linear constraint), tight (Markov), and narrowly closed; hence narrowly compact by Prokhorov, and non-empty **iff E ≥ E\_min \= 2.31340315203018** (row V5). *(Appendix B.4.)*

**(c) Extreme points, PROVEN without compactness (row V2).** ν is extreme iff its alias kernel is a.e. a Dirac mass. *(⇐)* an average of probability measures equal to a Dirac mass forces both to be that Dirac mass. *(⇒)* on the positive-measure set where w(θ) is not Dirac, let k₁(θ) \< k₂(θ) be the two smallest elements of supp w(θ) — measurable, since {θ : w\_k(θ) \> 0} is measurable — and set ε \= ½min(w\_{k₁},w\_{k₂}); then w ± ε(δ\_{k₁}−δ\_{k₂}) are distinct admissible kernels with midpoint w. *(Appendix B.2.)*

**(d) Explicit barycentre, PROVEN (row V3).** With n\_u(θ) \= F\_θ^{−1}(u) the inverse CDF, ν \= ∫₀¹ ν\_{n\_u} du, reconstruction error **4.8 × 10⁻⁶** over 2 × 10⁵ randomizations. Choquet's theorem is not needed and the decomposition is constructive. *(Appendix B.3.)*

**Theorem M59.13 (Transversal–Extreme–Section equivalence). \[PROVEN\].** For ν ∈ 𝔐 the following are equivalent: (1) ν is extreme; (2) ν is carried by a measurable transversal; (3) ν \= (p\_n)\_*μ\_λ for a measurable branch, i.e. ν is the cyclic measure of a same-space logarithm; (4) periodization is injective on the measures carried by supp ν. Each such ν has cyclic measure of total Lebesgue measure 2π, hence no extreme completion is M46-equivalent*\*; M46-equivalence forces full alias support, hence a non-extreme point.

**Corollary M59.13a (Aliasing Dichotomy). \[PROVEN\].** Identifiability-by-declared-support and M46-equivalence are **mutually exclusive**. **Boundedness is irrelevant** — the v1.0 statement "identifiable ⟺ single-window ⟺ bounded" is RETRACTED, the unbounded transversal n(θ) \= ⌊−log₂(1−θ/2π)⌋ being identifiable with support supremum diverging as 62.83, 75.40, 87.96, 100.53 under grid refinement while mass stays 1 (row V1). What survives is the interval-transversal corollary: a transversal that is an interval has length exactly 2π, the generator is bounded with spectrum in \[a, a+2π\], and E\[p\] over that subfamily is minimized at a \= 0 (row P2: 2.313403, 2.416375, 3.088235, 8.249139, 8.577862 for a \= 0, 1, 2, 3, 6).

## **7.3 Selectors, executed**

**S1 — minimal energy. \[PROVEN inequality \+ DERIVED-CONDITIONAL selection\].** For any admissible completion,

**E\[p\] \= ∫₀^{2π} θ dμ\_λ \+ 2π Σ\_{k≥0} k w\_k  ≥  E\_min \= 2.31340315203018 ,     w\_k \= ∫ |c\_k|² dμ\_λ**

with equality **iff w₀ \= 1 a.e.** So the minimal-energy rule selects the k ≡ 0 transversal **uniquely** — exactly the ZS-S28 θ₊ branch with spectrum \[0, 2π\], **bounded**, hence M46-incompatible. The *promotion of minimality to a selection principle* is DERIVED-CONDITIONAL on a least-action principle, exactly as ZS-F32 Theorem F32.3 rates its own norm-minimality argument. Executed: E(F1) \= 2.313403, E(F2) \= 5.454996, E(F4) \= 8.596588 (row L1).

**S2 — continuous-extension minimality. \[PROVEN, CLOSED-NEGATIVE as a selector\].** If ψ\_c ≠ 0 a.e. then {f(P)Ψ\_c : f ∈ C\_c(ℝ₊)} is dense, so A5 and A6 hold for **every** full-support field; S2 cannot distinguish fields.

**S3 — outer spectral factor. \[REFORMULATED\].** The Szegő condition holds *unconditionally* for the event measure: ρ\_**λ** is bounded above and below, so log ρ\_**λ** ∈ L¹(𝕋) — exactly the analytic gate ZS-M47 v2.0 registers as **M47.SZ** with **(SZ): ∫ log w dμ \> −∞**. The outer factor therefore exists and is unique up to a unimodular constant. But outer factorization fixes the *phase given the modulus*, while the alias equation constrains only aliased sums of |ψ|². S3 splits into **S3a** (an intrinsic modulus rule — OPEN) and **S3b** (phase by outer factorization — SETTLED).

**S8 — the folded canonical unfolding. \[REFUTED against interest\].** Fold the negative-energy weight of the canonical unfolding into the lowest alias and fix the phase by outerness: constructible, parameter-free, satisfying A2–A6, **but its energy diverges**. The Cauchy tail gives alias mass ≈ μ/(2π²k²) at energy ≈ 2πk, so partial energies grow logarithmically: E₁₀ \= 0.118255, E₁₀₀ \= 0.204860, E₁₀₀₀ \= 0.289264, measured slope per ln 10 **0.036656** against the prediction μ/π \= **0.036553** (row J2). Under any finite-energy requirement F3 is excluded. **Candidate axiom A13 (finite energy)** narrows — killing the canonical unfolding and F3 — but does not select, since F2 and F4 survive; it is not imposed.

**S6/S7 — Gibbs and alias temperature. \[CLOSED-NEGATIVE by Theorem M59.17\].**

**Theorem M59.17 (MaxEnt Family). \[PROVEN\].** Maximizing the phase-averaged alias entropy S(ν) \= ∫H(w(θ))dμ\_**λ** subject to ∫p dν \= E gives w\_k(θ) ∝ e^{−β(θ+2πk)}; the factor e^{−βθ} **cancels on normalization**, so the maximizer is the θ-independent **geometric field**

**w\_k \= (1 − q) q^k ,     q \= e^{−2πβ} ,     E(q) \= E\_min \+ 2π q/(1 − q) ,     q \= (E − E\_min)/(E − E\_min \+ 2π)**

a bijection onto E ∈ \[E\_min, ∞) (row V6, round-trip error 3.7 × 10⁻⁴⁰). **Corollary.** The MaxEnt route is exactly one-parameter and the event fixes no energy, so S6 and S7 do not select. β \= μ is an ordinary member (q \= 0.48600944, E \= 8.2545383); the q → 0 endpoint is the S1 transversal, so **S1 and S6 are the two ends of one line**, and F4 is the MaxEnt element at its own energy.

**Theorem M59.8 (Intrinsic Alias Selector). \[UNDERDETERMINED\].** In the executed order: S1 selects only after a branch declaration and lands on a bounded transversal; S2 is provably non-selecting; S3 is two rules of which one is settled; S6/S7 are closed by M59.17; S8 is refuted; S5 requires a pair that §8 excludes on the minimal space and cannot import M46's. *Scope:* this concerns the executed candidate set, not a proof that no selector can exist; §11 explains the structure uniformly.

## **7.4 The Continuous-Moment No-Go**

**Theorem M59.14. \[PROVEN\].**

**(i) Identification.** The ZS-S28 harmonic measure *is* the wrapped Cauchy of location χ and scale μ:

**Σ\_{k∈ℤ} C\_{χ,μ}(θ \+ 2πk) \= ρ\_λ(θ) / 2π ,     C\_{χ,μ}(p) \= (μ/π) / ( (p − χ)² \+ μ² )**

verified to **7.89 × 10⁻³¹** over 44 angles (row H1 of the spine).

**(ii) Interval sharpness.** Fix a branch k. If a positive-energy pointed completion satisfies ⟨Ψ, U(t)Ψ⟩ \= **λ**^t on *some nonempty open interval* I ⊂ ℝ₊, then φ\_ν(t) \= ∫e^{itp}dν is holomorphic on the open upper half-plane and continuous up to ℝ; its difference from the entire function e^{it(χ+2πk)}e^{−μt} vanishes on I, hence vanishes identically by the Schwarz reflection principle; with φ(−t) \= conj φ(t) and Bochner uniqueness, ν \= C\_{χ+2πk,μ} on ℝ. *(Appendix B.5.)*

**(iii) Branch-complete deficit.** That measure charges ℝ₋ with

**δ\_neg^(k) \= (1/π) · arctan( μ / (χ \+ 2πk) )  \>  0**

strictly decreasing, infimum 0 never attained: **0.016165353, 0.0042787326, 0.0024654797, 0.0017316298, 0.0013344332, 0.001085454** for k \= 0…5. Positivity fails on **every** branch. At the principal branch

**δ\_neg \= (1/π) · arctan(1/R) \= 0.0161653528682918434 ,     R \= χ/μ \= 19.6739402770**

*Alias masses of the canonical unfolding (row H4 of the spine):* 0.97475322, 0.00553519, 0.00134300, 0.00060520, 0.00034437, 0.00022226, tail k ≥ 6: 0.00103141, ℝ₋: 0.01616535.

**Reading.** The event determines its completion on ℤ and nothing more; *any* open interval of continuous times over-determines it into inconsistency. All of the non-identifiability lives in the gap between a countable set and an interval.

# **§8. The real structure and the standard-pair obstruction**

**(i) Standard real subspaces are abundant. \[PROVEN\].** (Jf)(θ) \= conj f(θ) is an antiunitary involution on L²(𝕋, μ\_**λ**) — well defined because ρ\_**λ** is real — with JΩ \= Ω and J U\_event J \= U*\_event; and H\_ev \= {real-valued f} satisfies H\_ev ∩ iH\_ev \= {0} and H\_ev \+ iH\_ev \= L² exactly*\*. This is the positive counterpart of ZS-S28's row LAD-02: a complex-linear Hardy space is not a real subspace, but the event's own conjugation is.

**(ii) Invariant ones exist too. \[PROVEN, row V9\].** In the L²(𝕋,dθ) picture, H\_F \= {f : all Fourier coefficients real} is standard **and** shift-invariant with **U H\_F \= H\_F**. Invariance per se is therefore not the obstruction; such a subspace yields an inclusion with equality, hence a trivial one.

**(iii) Standard-Pair Obstruction. \[PROVEN from an imported decomposition\].** Every positive-energy standard pair is a direct sum or integral of copies of the unique irreducible one on L²(ℝ₊,dp) (Rieffel–van Daele; Longo; imported by ZS-M46 Theorem A(i)); by Theorem M59.4 its unit-time element has multiplicity ℵ₀, and multiplicities add. Hence **U(1) has multiplicity ℵ₀ for every positive-energy standard pair, so none has U\_event as its unit-time element.** *(Appendix B.6 states the imported hypotheses exactly.)*

**(iv) Theorem M59.18 (M46-side pointing, ray level). \[PROVEN, scope declared\].** A ray \[Ψ\] invariant under a one-parameter unitary group is an eigenvector of its generator: Δ^{it}Ψ \= c(t)Ψ with c a continuous character forces c(t) \= e^{iαt} and DΨ \= αΨ. Now **P \= M\_p** on L²(ℝ₊,dp) is multiplication against a non-atomic measure and has **no eigenvector**; and **D \= ½ \+ p∂\_p** satisfies **VDV^{−1} \= d/dx** on L²(ℝ,dx) under (Vψ)(x) \= e^{x/2}ψ(e^x), verified on a test vector to **5.74 × 10⁻⁴²**, hence is purely absolutely continuous with Lebesgue spectrum and **no eigenvector**; consistently the formal solution p^{−1/2} of Dψ \= 0 fails square-integrability logarithmically at both ends (∫₁₀^{−8}¹ dp/p \= 18.42). Hence **no ray is invariant** under either group, and **no pointing is natural for the ax+b symmetry** that a standard pair carries by Borchers' theorem.

**Scope.** This does not prove that no canonical pointing can be constructed by other means. The {±1} rigidity of the pair's automorphism group (Longo–Witten, row Z10) is **not** part of the argument, since ψ and −ψ give the same ray. Status of the pointed comparison: **UNDECLARED**.

**Status decomposition of the seed's M59.9.** *(a)* event-intrinsic standard real subspace: **PROVEN**. *(b)* invariant one: **PROVEN**, with equality, hence trivial. *(c)* standard pair with U\_event as unit step on the minimal space: **CLOSED-NEGATIVE**. *(d)* ax+b-natural one-particle pointing on the M46 side: **CLOSED-NEGATIVE**. *(e)* canonical pointing by any other principle: **OPEN**.

# **§9. Blind comparison with ZS-M46**

Only this section loads ZS-M46 data; §§2–8 are fixed and hashed first (guard R1).

*Table 5\. The ZS-M58.7 Eq. (7.3) checklist, evaluated.*

| clause | verdict | basis |
| ----- | ----- | ----- |
| W U\_event W\* \= U\_M46(1) | **automatic** for every full-support completion | Thm M59.12 |
| W P\_c W\* \= P\_M46 | **automatic** (same W\_c) | Thm M59.12 |
| W Ψ\_c \= Ψ\_M46 | **UNDECLARED** — none declared, and none ax+b-natural | Cor. M59.12b, Thm M59.18 |
| W A\_past W *\= N ; W A\_full W* \= M | **CLOSED-VACUOUS for transported structures** | Thm M59.11(a) |
| W R\_record W\* \= R\_M46 | CLOSED-VACUOUS, same reason; record MASA kept distinct | A12 |

**Theorem M59.10 (Pointed Standard-Pair Compatibility). \[DERIVED for the unpointed clauses; UNDECLARED for the pointed clause\].** For every full-support completion there exists a unitary W\_c with W\_cU\_c(t)W\_c *\= U\_M46(t) for all real t, and W\_c carries the ZS-M46 standard real subspace back to a standard real subspace of 𝒦\_c. Since no ax+b-natural M46 pointing exists, the result is standard-pair compatibility without pointed-state equality, and the pullback is labelled COMPARISON-DEFINED*\*.

**Theorem M59.15 (Continuous-Time Separation). \[PROVEN\].** For t ∈ ℝ,

**φ\_c(t) \= ∫₀^{2π} e^{iθt} · ŵ\_θ(t) · dμ\_λ(θ) ,     ŵ\_θ(t) \= Σ\_{k≥0} e^{2πikt} |c\_k(θ)|²**

so continuous time measures exactly the **alias characteristic function** on the dual circle ℝ/ℤ. At t ∈ ℤ, ŵ\_θ ≡ 1 for every field — which is Theorem M59.7 — and off ℤ it separates fields: row V11 gives 0 at t \= 0, 1, 2 and 0.6996, 0.9613, 0.6544 at t \= 0.25, 0.5, 0.75.

**Corollary M59.15a (Half-step witness).** At t \= ½ the alias phase is (−1)^k and the separating functional is the alternating alias weight. Executed: F1 gives |φ(½)| \= **0.961335104687841**; F2 gives **exactly 0**; F3 gives 0.952267; F4 gives 0.320445; the principal-branch transversal gives 0.917981. For F1 the closed form

**φ\_F1(½) \= Σ\_{n∈ℤ} r^{|n|} e^{−inχ} · i / ( π (n \+ ½) ) \= 0.395368262918181725 \+ 0.876270004155250397 i**

agrees with quadrature to **9.86 × 10⁻³²**.

**Scope.** M59.15 concerns amplitudes of the formal event's completions. It is **not** the claim that an experiment at a fractional seam step decides anything: Artifact B is unavailable and no physical process is designated. "t \= ½" is half of the ZS-M46 Abel unit declared in §1.2.

# **§10. Fock and modular lift**

**Theorem M59.11(a) (Structural rigidity). \[PROVEN\].** For full-support ν, ν′ the map

**V : L²(ℝ₊, ν) → L²(ℝ₊, ν′) ,     (V g)(p) \= g(p) · |ψ\_ν(p)| / |ψ\_{ν′}(p)|**

is unitary and intertwines the generators (isometry deviation exactly **0**, intertwining **2.54 × 10⁻¹³**, |V| ∈ \[0.710, 3.414\]). Hence Γ(V) carries ℛ(H), its half-sided inclusion, its modular flow and its Connes cocycle across, **with the Fock vacuum preserved**, and every invariant built from (H, U, Ω\_F) is **constant on the full-support stratum**. B6 and B7 therefore close **vacuously**: on a comparison-defined completion the cocycle is u\_t \= 1 by construction, which must never be reported as a result (guard Z9, gate F-M59.42).

**RETRACTED \[v1.4 Appendix B.7\].** *"Since H is standard, H \+ iH is dense, so knowing Im⟨Ψ,h⟩ for h ∈ H determines Ψ."* Invalid. Two vectors give the same coherent state on ℛ(H) **iff** their difference lies in the symplectic complement H′ \= {ξ : Im⟨ξ,h⟩ \= 0 ∀h ∈ H}, which for a standard subspace is itself standard and infinite-dimensional; the toy pair H \= ℝ ⊂ ℂ has H′ \= H, and Ψ \= 1, Ψ′ \= 0 are not separated (row P1).

**Theorem M59.11(b) (State-level faithfulness). \[PROVEN in the canonical Hardy model; DERIVED-CONDITIONAL on ZS-M46 KH1–KH4 for the seam realization\].**

**(i) Reality lemma.** In the M46 one-particle space, a **nonzero real-valued** ψ ∈ L²(ℝ₊, dp) lies in **neither H nor H′**. *Proof.* Extend ψ to ℝ by conjugate symmetry; for real ψ the extension is **even and real**, so its inverse Fourier transform f is even and real. Membership in H requires supp f ⊆ \[0,∞) and in H′ requires supp f ⊆ (−∞,0\]; either together with evenness forces supp f ⊆ {0}, hence f \= 0 and ψ \= 0\. □ *(Row P2. The toy pair carries no Fourier-support structure, which is exactly why the counterexample does not transfer.)*

**(ii) Separation.** W\_c sends Ψ\_ν to |ψ\_ν| ≥ 0, which is real. For ν ≠ ν′ the difference δ \= |ψ\_ν| − |ψ\_{ν′}| is real and nonzero, hence δ ∉ H′, hence ω\_{Ψ\_ν} ≠ ω\_{Ψ\_{ν′}} on ℛ(H).

**(iii) The exact dual norm.** For f real supported in (0,∞) put h\_f \= f̂|\_{ℝ₊}. Then ‖h\_f‖ \= √π‖f‖ by Plancherel and evenness of |f̂|, while Im h\_f \= √(π/2)F\_s\[f\] with F\_s the unitary involutive sine transform. Hence

**sup { | Im⟨δ, h⟩ | : h ∈ H , ‖h‖ ≤ 1 } \= ‖δ‖ / √2**

attained at f \= F\_s\[δ\] (row C6: ratios **0.707160** and **0.708544** against 1/√2 \= 0.707107). *(Appendix B.7″.)*

**Scope, layered (row H10).** Faithfulness is claimed for the **canonical representatives** |ψ\_ν| and for those only; for arbitrary vectors the v1.4 statement remains false. The theorem is **PROVEN in the canonical Hardy standard-pair model**; its Z-Spin seam realization inherits ZS-M46's KH1–KH4 and is therefore **DERIVED-CONDITIONAL**.

**Corollary.** The downstream tier is powerless exactly where it is **structural** and faithful exactly where it uses the **state** — and the state is the missing datum. This is the seed's Pattern 6 warning as a theorem rather than a caution.

# **§11. The residual: torsor, rigidity, divisor calculus**

## **11.1 Above — the Branch Torsor**

**Theorem M59.19. \[PROVEN\].** Let 𝔏 be the set of self-adjoint logarithms of U\_event, identified by Theorem M59.2 with measurable n : \[0,2π) → ℤ modulo null sets, and 𝒢 \= L⁰(\[0,2π); ℤ) the abelian group of such functions.

1. **𝒢 acts freely and transitively** (row Y3): n \+ m \= n forces m \= 0 a.e.; and m := n′ − n is measurable ℤ-valued. 𝔏 is a **𝒢-torsor**.  
2. **The event is 𝒢-invariant**: U\_event \= e^{iP\_n} for every n, so channel, multiplier, pointed moments and the entire integer-time representation are unchanged by all of 𝒢. **Hence the event data alone distinguish no origin in 𝔏** — and nothing more is claimed, since an external declaration supplies one at once (row X2).  
3. **Positivity breaks the group to a semigroup** (row Y4): 𝔏₊ \= {n ≥ 0} is stable only under 𝒢₊.  
4. **ZS-M57 T.2′ and ZS-M58 layer L2 are the constant subgroup ℤ \< 𝒢** (row Y5); the quotient **𝒢/ℤ** is content new to ZS-M59.

**Interpretation \[DERIVED, interpretive\].** In the corpus's ontology — Z-sector the stage, Z-Spin the action, Z-bias field the degree of freedom — the residual is a function on the seam phase circle valued in ℤ, free at each phase, invisible to the channel:

***the completion residual of the formal QND event is a discrete Z-bias field n : ∂Z → ℤ, whose constant mode is the ZS-M57 branch.***

**What survives of the v1.2 shift argument.** σ : ν ↦ ν(·−2π) preserves every event datum while twisting the continuous group by e^{2πit}, which is 1 exactly on ℤ (row Z3); on transversals it realizes n ↦ n+1 (row Z4); it has no fixed point in 𝔐 (row Z2). But σ is **injective and not surjective** — the window-0 transversal puts mass 1.0 on \[0,2π) and has no preimage (row Y1) — and shifts are **not transitive**, the alias entropy being shift-invariant with S(F1) \= 0 and S(F2) \= log 2 (row Y2). *The v1.2 "free ℤ-action / alias torsor on 𝔐" and "B3 CLOSED-EMPTY" are RETRACTED.*

## **11.2 Restricted below — Anchor Rigidity**

**Theorem M59.21. \[PROVEN\].** Let a : 𝕋\_θ × S¹\_s → ℂ be a continuous family of **closed** seam transport loops and n(θ) \= wind(a(θ,·); 0).

5. **Rigidity.** If a is nowhere zero, n is a homotopy invariant of a family over the connected circle and is therefore **constant** (row N1: winding 1 over 40 angles). *The v1.4 trichotomy — constant, Q-valued, or unbounded — is RETRACTED: only the first is possible under these hypotheses.*  
6. **Necessity, not equivalence.** A non-constant n **requires** a degeneracy locus. The converse **fails**: two anchors entering and leaving at the same phase cancel, leaving zeros present and the winding constant (row C4). A degeneracy produces a jump only if the crossing is **transverse with nonzero net local degree**. *The v1.5 "anchors ⟺ non-constant" is RETRACTED.*  
7. **Degree zero.** Single-valuedness around 𝕋 forces Σ\_j m\_j \= 0 (row N3).  
8. **Two bounds, two currencies.** With V the number of distinct values,

**\# supp D  ≥  V ,           ‖D‖ := Σⱼ |mⱼ|  ≥  2(V − 1\)**

both sharp. *Proof.* V distinct values need at least V arcs and on a circle \#arcs \= \#jumps; the staircase attains it. For the second, the total variation is Σ|m\_j| and is at least twice the range max n − min n, while V distinct integers force the range ≥ V−1. □ *(Rows C1–C3. The v1.5 counterexample — jumps \+1 ten times then −10 — has eleven values at eleven locations and ‖D‖ \= 20 exactly, refuting the location form and confirming the multiplicity form. The v1.5 "≥ 2(Q−1) crossing locations" is RETRACTED.)*

9. **Scope of "finitely generated" (row C5).** For a **fixed** support of size k the jump data {m ∈ ℤ^k : Σm \= 0} form a free abelian group of **rank k−1**. Over all admissible transports the support varies, so there is no single finitely generated group; and reducing the admissible set is a **realizability restriction**, not a lower bound. *The v1.5 unqualified claim is RETRACTED.*

### **11.2.1 The frozen path carries no winding — type correction (new at v1.8)**

**RETRACTED \[v1.7 Corollary M59.21b\].** *"ZS-S28's endpoint path is nonvanishing, so by (1) it carries only the constant mode."* Theorem M59.21(1) quantifies over continuous families of **closed loops indexed by θ**. The frozen path is neither: it is **open**, running from a(0) \= 1 to a(1) \= **λ** with |a(1) − a(0)| \= **1.711032173**, and it carries **no θ-index at all** (row T1). §17 of v1.7 already stated that no winding number exists for it; §11.2 contradicted that, and the contradiction is resolved here in favour of §17.

**Theorem M59.24 (Closure Dependence). \[PROVEN, executed\].** The winding of a closed extension of the frozen path is **not determined by the path**. Closing by the straight segment **λ** → 1 gives total winding **0**; closing by carrying the argument on through 2π gives **1**. Neither closure meets the origin (minimum modulus 0.4024 and 0.8915 respectively). *(Row T2; proof in Appendix B.11.)* Hence **a closure prescription is not a technicality but the datum that fixes the answer.**

**Proposition M59.25 (No family, no field). \[PROVEN, trivial\].** A single path has no θ-dependence and therefore carries no field on the seam circle. The constant mode is all there is — **for want of a family, not by a homotopy theorem**. This is the honest explanation of why ZS-M57 and ZS-M58 each found one integer (row T3; Appendix B.12).

**Corollary M59.21b′ (Conditional application to the frozen path). \[DERIVED-CONDITIONAL\].** If a successor supplies a **closure prescription** and a **continuous nonvanishing closed θ-family** ã : 𝕋\_θ × S¹\_s → ℂ^× extending the frozen path, then Theorem M59.21(1) forces its winding field to be **constant**. The single integers found in ZS-M57 and ZS-M58 are therefore **consistent with the constant subgroup but are not derived from the frozen open path alone** (row T4).

**Re-typing of ZS-S28's "winding zero" (row T5).** arg a(s) rises continuously from 0 to χ \= 2.259250 \< 2π, so the **continuous lift** ends inside the principal branch. That is ZS-M58 layer **L2** — a statement about the lift of an open path — and **not** a loop winding number. No ZS-S28 field is altered; only its reading is corrected.

## **11.3 The divisor calculus**

**Theorem M59.22. \[PROVEN for finite transversal transports whose projected degeneracies are isolated with nonzero local degree — row H8\].** Let n be a transversal branch field with jump divisor D \= Σ\_j m\_j δ\_{θ\_j}, deg D \= 0, and S\_D(θ) \= Σ\_{θ\_j\<θ} m\_j.

**(i) The divisor determines the field.** n \= n₀ \+ S\_D with n₀ ∈ ℤ, and positivity forces n₀ ≥ −min S\_D. The **minimal admissible field** is therefore

**n\_D := S\_D − min\_θ S\_D**

unique. Given D, the additive branch constant is fixed by the **predeclared minimal-lift rule S1**; **no additional axiom** — not (H-MAXENT), not (H-EQUIVARIANT-SELECTION), not any register hypothesis — is required (rows D2, H9).

**(ii) Energy is the harmonic pairing of the divisor.** With F(θ) \= μ\_**λ**((θ,2π)),

**E(D) \= E\_min \+ 2π \[ n₀(D) \+ Σⱼ mⱼ F(θⱼ) \]**

verified against direct quadrature on three divisors to **1.6 × 10⁻¹⁹** (row D1). *Proof:* E \= E\_min \+ 2π∫n dμ and ∫S\_D dμ \= Σ\_j m\_j μ((θ\_j,2π)) by Fubini on S\_D \= Σ\_j m\_j **1**\_{(θ\_j,2π)}.

**(iii) Anchor cost.** Since the range of n is at most half the total variation,

**E(D)  ≤  E\_min \+ π ‖D‖**

**Anchor multiplicity is the currency of energy** (row D3).

## **11.4 Closed forms, and where the pairing is sensitive**

**Theorem M59.23 (Closed forms). \[PROVEN, new at v1.7\].** With κ \= (1+r)/(1−r):

**(i) Exact CDF.** Pr(|Θ−χ| \< a) \= (2/π)arctan(κ tan(a/2)), matching quadrature at a \= μ to **0.0** (row H2).

**(ii) Exact half-mass radius.**

**a\_½ \= 2 arctan( (1 − r)/(1 \+ r) ) \= 2 arctan tanh(μ/2) \= 0.114583066682673187**

with CDF exactly ½. **The v1.6 claim that exactly half the mass lies within |θ−χ| \< μ is RETRACTED**: the measured mass at radius μ is **0.50069959154154853**, and μ − a\_{1/2} \= 2.5156 × 10⁻⁴ (rows H1, H3).

**(iii) An identity between two frozen quantities.** (1−r)/(1+r) \= **inf ρ\_λ** \= tanh(μ/2), hence

**a\_½ \= 2 arctan( inf ρ\_λ )**

The half-mass radius of the harmonic measure is fixed by the **minimum of its own density** — two independently frozen ZS-S28 quantities linked exactly (row H4).

**(iv) The pairing weight in closed form.** F(θ) \= G(2π) − G(θ) with

**G(θ) \= (1/π) \[ arctan( κ · tan((θ − χ)/2) ) \+ π · ⌊ (θ − χ \+ π) / 2π ⌋ \]**

matching quadrature over six phases to **4.93 × 10⁻³¹** (row H5). Sample values: F(0.3) \= 0.996370158231, F(1.0) \= 0.983611456105, F(2.0) \= 0.876681696588, F(χ) \= 0.508618812835, F(3.0) \= 0.0552982332812, F(4.5) \= 0.0174448998453, F(6.0) \= 0.00298044623329.

**(v) Layer-cake identity.** E\_min \= ∫₀^{2π}F(t)dt, verified to **0.0** (row H6). The minimal energy and the divisor pairing are two readings of the same function.

**Interpretation, corrected (row H7).** In a degree-zero divisor no anchor has an independent cost: the energy is the **signed** pairing Σ\_j m\_j F(θ\_j) together with the minimal-lift correction n₀(D). The correct statement is that **F varies most steeply near χ** — the mass within radius μ is 0.50070, within 0.5 is 0.85933856, within 1.0 is 0.93340757 — so **signed configurations straddling χ carry the largest harmonic contribution**. *The v1.6 statement "anchors away from χ are almost free while χ is the expensive phase" is RETRACTED.*

## **11.5 What is new here, stated against the literature**

Theorem M59.22 combines four standard ingredients: the distributional derivative of an integer-valued BV function on a circle; a total-variation bound; Fubini on an indicator decomposition; and the Poisson harmonic measure of a disc automorphism. Spectral-flow theory already treats winding change, degeneracy, Fredholm crossings and local index systematically. **The claim to novelty is therefore the combination in the sampled-unitary setting** — that the positive-energy completions of a sampled cyclic unitary that arise from finite transversal transports are indexed by a degree-zero divisor on the phase circle; that the divisor determines the completion once a lift rule is declared; that the energy is exactly the divisor's pairing with the harmonic measure; and that the anchor charge bounds the energy. No claim is made that any single ingredient is new (row H12).

# **§12. The register variants, with all axioms named**

**(H-CARRIER-11).** *The alias fiber is the record index of the ZS-S28 frozen eleven-dimensional collision carrier.* **Status: REFORMULATED, not derived.** By M59.21(4) an eleven-valued field requires ‖D‖ ≥ 20; but an anchor charge of 20 is not an eleven-dimensional carrier, and the passage would require a **representation and an intertwiner** that no paper has produced. ‖D‖ ≥ 2(V−1) is a **necessary condition once a V-valued field is given**, not a derivation of V or of the carrier (rows D5, H11).

**Variant A — (H-TRUNC) \+ (H-MAXENT). \[CANDIDATE\].** Spectrum in \[0, 2π**Q**\] \= \[0, **69.1150383789755**\], time group ℝ, positivity kept; 𝔐\_Q is convex and weak-\\ *compact; every generator is bounded so no completion is M46-equivalent. The shift stays partial, so equivariance is unavailable and (H-MAXENT) must be adopted; the unique maximizer is the uniform field with S \= log Q \= 2.397895273 and E\_Q \= E\_min \+ π(Q−1) \= 33.7293296879281*\*.

**Variant B — (H-CARRIER-11) \+ (H-WRAP) \+ (H-EQUIVARIANT-SELECTION).** On a cyclic fiber σ generates a ℤ/**Q** action and ker(I − σ) is one-dimensional, spanned by the uniform vector (row X4, 8.33 × 10⁻¹⁷), so uniformity follows **given the selection-naturality axiom**. Cost: the time group collapses to **(1/Q)ℤ**, the completion is a **Q**\-fold refined discrete clock, and M46's ℝ-flow is excluded structurally.

**Q-comb and parity.** ŵ(t) \= (1/**Q**)Σ\_{k\<**Q**}e^{2πikt} has period 1 and vanishes exactly on **(1/Q)ℤ \\ ℤ** (row X1, verified at 1/**Q**, 2/**Q** and 1+1/**Q** to 1.13 × 10⁻⁴⁰); |ŵ(½)| \= 1/**Q** for **Q** odd and 0 for **Q** even (row X7, executed at **Q** \= 11, 10, 3, 2). Under (H-TRUNC) the half-step witness is 0.961335104687841/11 \= **0.0873941004262**.

**OBSERVATION, not a claim (row E2).** ℤ/**Q** with **Q** odd has no element of order two, so a half-turn requires a degree-two cover, (1/2**Q**)ℤ with 2**Q** \= 22\. That degree is 2 and dim **Z** \= 2 **numerically**; **no structural identification is claimed**, and under (H-WRAP) t \= ½ is not an admissible time.

**The divisor route dominates both** for the transversal stratum: it needs no register hypothesis, no entropy axiom and no equivariance axiom — only S1's pre-existing minimality conditional.

# **§13. Audit**

**13.1 Zero free parameters.** Allowed inputs: **λ**, r, χ, μ, ρ\_**λ**, U\_event, Ω\_event, all reproducible from ZS-M1's z*; and, under named hypotheses only, Q*\* \= 11\. Introduced: nothing tunable — no alias temperature, decay ratio, branch cutoff, smoothing width, entropy multiplier, preferred energy or window function. F4 is the MaxEnt element at its own energy and remains barred from primary selection. §11.3–11.4 use none of the geometric constants.

**13.2 Anti-numerology.** Target δ\_neg \= 0.0161653528682918434 on the declared principal branch. Universe: 30 corpus constants × 7 elementary transforms \= **210 formulas**; tolerance 10⁻³ primary, 10⁻² audit; null log-uniform on \[10⁻³, 10⁻¹\].

| statistic | value |
| ----- | ----- |
| hits at 10⁻³ / 10⁻² | **0 / 0** |
| look-elsewhere coverage at 10⁻³ / 10⁻² | 3.06 % / 25.42 % |

δ\_neg is branch-indexed with δ\_neg^{(k)} ↓ 0, forbidding any single member being read as distinguished. E\_Q and the half-step value: nearest relative distance 2.36 × 10⁻², **no identification claimed**. **NON-CLAIM (Q3):** every number here is a function of **λ** and, conditionally, of **Q**; none is independent evidence about either. **Proximity of record:** E\_min \= 2.313403 and χ \= 2.259250 differ by 0.054 and are different objects. **New at v1.7:** a\_{1/2} \= 0.114583066682673187 and μ \= 0.114834624996010 differ by 2.5 × 10⁻⁴ and are different objects — the near-coincidence is the small-μ asymptotic tanh(μ/2) ≈ μ/2 and nothing more.

**13.3 Cross-version dependency trace: twelve upstream statuses, zero reversals (guard R1).**

| upstream item | consumed as | use here |
| ----- | ----- | ----- |
| ZS-S28 B4-principal / B3 / LAD-01 r3 / LAD-02 | CLOSED-NEGATIVE / OPEN / PROXY / negative | unchanged / narrowed / typing inherited / answered constructively (§8(i)) |
| ZS-S28 eleven-dimensional carrier; nonvanishing endpoint path | frozen Artifact A | §12 hypothesis; input to the retracted Cor. M59.21b and to Thm M59.24 / Cor. M59.21b′ |
| ZS-M46 KH1–KH4 / pointing / Thm A(i) | DERIVED-CONDITIONAL / undeclared / IMPORTED-PROVEN | never unconditional; not invented; the uniqueness input of §8(iii) |
| ZS-M47 M47.SZ | DERIVED reformulation | (SZ) free for the event measure |
| ZS-M57 T.2′, F-M57.V1/Y2 | branch OPEN | identified as the constant subgroup of 𝒢; unit and branch declared |
| ZS-M58 M58.6 / M58.7 / L2 | PROVEN / OPEN / PROVEN | precedent; §9 checklist verbatim; L2 \= constant mode |
| ZS-F32 F32.3 | PROVEN \+ DERIVED-CONDITIONAL | the same conditional ceiling on S1 |
| ZS-F38 t\\ *\= Q*\* | motivation only | for (H-WRAP), never as proof |
| ZS-F39 T1 / ZS-A24 F-A24.9 | uniqueness-not-existence / OPEN | disciplines mirrored |
| Z-anchor (Bogomolnyi vortex core) | corpus object | consumed, not invented |

**13.4 Semantic guard (row W1).** Ten retracted phrases scanned across every active claim row: *"the physical S14 event"*, *"the action-selected instrument"*, *"the action-derived branch"*, *"the Hardy space is the standard real subspace"*, *"positive logarithms do not exist"*, *"the principal branch proves a global no-go"*, *"same spectrum implies equivalence"*, *"unit-step equality implies generator equality"*, *"compatibility proves selection"*, *"B1 through B4 executed"*. **Violations: 0\.** They appear only where quoted to be excluded, with explicit markers. **"The action-derived branch" remains prohibited** until §17 is executed.

**13.5 Verifier synchronization.** v1.6 corrected rows S2 and X6, which had retained retracted v1.4 language. v1.7 corrected row D4, whose claim string asserted an exact half while its test was a 2 × 10⁻³ tolerance; **v1.8 corrects rows N6 and S2, which had applied the winding theorem to the open frozen path.** Rules adopted: manuscript retractions propagate into claim strings in the same release; an "exact" claim may not be certified by a tolerance test; and **a theorem may be applied only to objects of the type it quantifies over, the type check being itself a row.**

**13.6 Observational non-collision.** ZS-M59 makes no dimensionful and no dimensionless *physical* prediction; it cannot collide with Planck 2018 ΛCDM parameters, Standard-Model couplings, or DESI DR2, for the reason ZS-M46 v1.5 gives in its own §9: the content is dimensionless modular kinematics.

**13.7 The failure-mode record.** v1.0 "identifiable ⟺ bounded"; v1.2 "free ℤ-action"; v1.4 faithfulness from density; v1.5 the 2(Q−1) location bound and "anchors ⟺ non-constant"; v1.6 "exactly half within μ", certified by a tolerance; **v1.7 a closed-loop theorem applied to an open path**. Seven instances of F2 — declared, not constructed. Each new ledger rule is the direct lesson of one of them, and the v1.8 rule closes the type-check loophole. The pattern is stable enough to be the paper's methodological contribution: **the refutation is usually a theorem about the right object, and the right object is usually the one that was never constructed.**

# **§14. Falsification gates**

**Tier 1 — mathematical, immediate rejection.** F-M59.1 (a logarithm outside the measurable integer classification); F-M59.2 (U\_event not multiplicity one); F-M59.3 (harmonic measure not ≡ Lebesgue); F-M59.4 (a same-space branch with full Lebesgue class); F-M59.5 (M46 unit-step multiplicity ≠ ℵ₀); F-M59.6 (an equivalence despite the mismatch); F-M59.27 (M46-equivalent completion with vanishing ψ\_c); F-M59.29 (interval agreement with **λ**^t on any branch); F-M59.33 (a positive-energy standard pair with finite unit-time multiplicity); F-M59.34 (a non-transversal extreme point); F-M59.39 (an eigenvector of P or D, or an ax+b-invariant ray); F-M59.45 (a 𝒢-orbit failing to exhaust 𝔏); F-M59.52 (canonical representatives differing by an element of H′); F-M59.53 (a continuous nonvanishing family with non-constant winding); F-M59.59 (fewer jump locations than values, or ‖D‖ \< 2(V−1)); F-M59.60 (an energy differing from the pairing formula); F-M59.61 (a real ψ ≠ 0 in H or H′, or a witness exceeding ‖δ‖/√2). **F-M59.66 (new): a CDF value differing from (2/π)arctan(κ tan(a/2)), or a half-mass radius differing from 2 arctan(tanh(μ/2)) — refutes M59.23(i)–(ii).** **F-M59.67: F(θ) differing from G(2π) − G(θ), or E\_min ≠ ∫₀^{2π}F — refutes M59.23(iv)–(v).** **F-M59.71 (new): if either of the two explicitly constructed closures of Theorem M59.24 is shown to cross the origin, or their computed windings are not respectively 0 and 1, then Theorem M59.24 is refuted.** \**F-M59.72 (new): a θ-family exhibited as* derived from the frozen path alone*, without an independent closure prescription — would refute Proposition M59.25.*\*

**Tier 2 — consistency collapse.** F-M59.7–10 (isometry, moments, cyclicity, spectators); F-M59.28; F-M59.32; F-M59.35; F-M59.36; F-M59.41; F-M59.46; F-M59.49; F-M59.55; F-M59.62 (a minimal admissible field other than n\_D); F-M59.63 (E(D) \> E\_min \+ π‖D‖). **F-M59.68 (new): a non-transversal or accumulating degeneracy set for which the divisor description still holds — would extend M59.22 beyond its declared scope and require restating it.**

**Tier 3 — selection and provenance.** F-M59.11–14; F-M59.19; F-M59.23–26; F-M59.37; F-M59.42–44; F-M59.50; F-M59.51; F-M59.56–58; F-M59.64 (presenting (H-CARRIER-11) as derived without the representation and intertwiner); F-M59.65 (citing v1.5's retracted claims as live). **F-M59.69 (new): citing v1.6's "exactly half", "anchors away from χ are free", "no selection principle needed", or the unrestricted generality claim as live.** **F-M59.70: certifying any exactness claim with a tolerance test.** **F-M59.73 (new): citing v1.7's Corollary M59.21b, or any statement that the frozen open path "carries the constant mode by M59.21(1)", as live.** **F-M59.74 (new): reopening ZS-M59 for work that §15's scope table assigns to the successor.**

# **§15. Terminal-in-scope declaration**

*Table 6\. What ZS-M59 closed and what it did not.*

| Item | Status |
| ----- | ----- |
| Classification of all same-space self-adjoint logarithms | **CLOSED** (Thm M59.2) |
| Section measure-class obstruction; spectrum ≠ measure class | **CLOSED** (Thm M59.3) |
| ZS-M46 unit-step folding and the ℵ₀ multiplicity | **CLOSED** (Thm M59.4) |
| Minimal-space M46 equivalence | **CLOSED-NEGATIVE** (Thm M59.5) |
| Positive-energy completion classification; universality; gauge typing | **CLOSED** (Thms M59.6, M59.7, M59.12) |
| Convex structure, extreme points, explicit barycentre, energy slices | **CLOSED** (Thm M59.13) |
| Interval-interpolation positivity obstruction, branch-complete | **CLOSED** (Thm M59.14) |
| MaxEnt one-parameter theorem; selector audit S1–S8 | **CLOSED** (Thms M59.17, M59.8) |
| Standard-pair obstruction; ax+b-natural pointing | **CLOSED-NEGATIVE** (Thms M59.9, M59.18) |
| Structural rigidity and state-level faithfulness | **PROVEN in the canonical Hardy model**; seam realization DERIVED-CONDITIONAL |
| Branch torsor 𝒢 \= L⁰(𝕋;ℤ); ℤ as the constant subgroup | **CLOSED** (Thm M59.19) |
| Anchor rigidity; the two bounds; closure dependence | **CLOSED** (Thms M59.21, M59.24, Prop. M59.25) |
| Finite-transversal divisor calculus and closed forms | **CLOSED in declared scope** (Thms M59.22, M59.23) |
| S14-derived closure prescription and θ-family | **OUTSIDE SCOPE** → ZS-M60 |
| The physical anchor divisor | **OUTSIDE SCOPE** → ZS-M60 |
| Eleven-dimensional carrier intertwiner | **OUTSIDE SCOPE** → successor of ZS-M60 |
| Pointer-preserving CPTP realization; event clock; F-M54-16′ | **OUTSIDE SCOPE** → successor of ZS-M60 |

**Declaration.** ZS-M59 is **TERMINAL-IN-SCOPE**. It is not incomplete because the last four rows are open; it is closeable **because the boundary between the first thirteen rows and the last four is now exhibited exactly**. Reopening ZS-M59 for work assigned to the successor is gate F-M59.74.

# **§16. Conclusion**

Eight versions, seven retracted centrepieces, and a stable method: when a claim is refuted, the refutation is usually a theorem about the right object, and the right object is usually the one that was never constructed. v1.0 named a bound of a quantity it had not identified. v1.2 called a semigroup a group. v1.4 proved a true theorem invalidly. v1.5 counted places when it should have counted charge. v1.6 called an approximation exact. **v1.7 applied a theorem about closed loops to an open path**, and its correction produced the sharpest statement in the seed: the winding of the frozen path's closure is **0 for one closure and 1 for another**, so the prescription is the answer, not a preliminary.

**What stands unconditionally.** Every self-adjoint logarithm of the event unitary is a measurable integer branch, and each carries its cyclic measure on a set of Lebesgue measure exactly 2π, even when its spectrum fills the half-line. The M46 translation at unit time is the full alias bundle of infinite multiplicity, so the minimal route is closed twice over, by multiplicity and by measure class. Alias completions exist for every measurable unit field and all reproduce the same integer moments; generator-level M46 equivalence holds exactly for the full-support ones, so the spectral clauses of the comparison close automatically and carry no information. The completion set is convex and not compact, its extreme points are precisely the transversals, precisely the same-space logarithms, and every completion is an explicit inverse-CDF barycentre of them. Demanding the event's semigroup on any open interval forces a measure that leaks onto the negative axis on every branch. No positive-energy standard pair has a multiplicity-one unit-time element, and no ray of the M46 one-particle space is ax+b-invariant. Coherent states separate the canonical representatives at exactly ‖δ‖/√2.

**What the residual is.** A torsor coordinate: the branch is not an integer but a **field** on the seam circle, phase-local, ℤ-valued, invisible to the channel, with ZS-M57 and ZS-M58 holding its constant mode. And it is not free: a continuous nonvanishing seam has constant winding, so a genuine field requires anchors, and then it is piecewise constant with a degree-zero divisor obeying \#supp D ≥ V and ‖D‖ ≥ 2(V−1).

**What v1.7 adds.** The calculus is now explicit. The divisor determines the field once the predeclared lift rule is applied. The energy is the divisor's pairing with the harmonic measure, and both the pairing weight F and the minimal energy are closed forms of one elementary function — F(θ) \= G(2π) − G(θ), and E\_min \= ∫F. The anchor charge bounds the energy above by π‖D‖. The wrapped Cauchy's half-mass radius is 2 arctan(inf ρ\_λ), an exact link between two frozen quantities that the false "exactly half" had hidden. And the pairing is most sensitive near χ, so it is signed configurations straddling arg **λ** that carry the harmonic weight — not isolated anchors, which have no independent cost.

**What it does not do.** It does not close the physical seam. A divisor is not a CPTP map, not a pointer conservation law, not the multiplier **λ**, and not an event clock. **One candidate route to physical selection has been reduced to an anchor-divisor computation, followed by an open channel-realization gate.** (H-CARRIER-11) is reformulated, not derived: twenty units of anchor charge is a number, an eleven-dimensional carrier is a representation, and the map between them has not been built.

# **§17. General form**

| Result | General hypothesis | Statement |
| ----- | ----- | ----- |
| M59.2 | U cyclic (multiplicity one) | every self-adjoint logarithm is M\_{θ+2πn(θ)} |
| M59.3 | μ ≡ dθ | every section's cyclic measure has total Lebesgue measure 2π |
| M59.4, M59.5 | none / U cyclic | folding multiplicity ℵ₀; minimal-space no-go |
| M59.6, M59.7 | any μ | alias embeddings for every unit field; integer moments blind to the fiber |
| M59.12, M59.13 | any μ | generator equivalence ⟺ full support; extreme ⟺ transversal ⟺ section; explicit barycentre |
| **M59.19** | any μ | **the self-adjoint logarithms of a cyclic unitary form a torsor under L⁰(𝕋;ℤ); positivity reduces it to a semigroup; the sampled data are invariant under the whole group** |
| M59.14 | any strict contraction a | wrapped-Cauchy identification; **δ\_neg(a) \= (1/π)arctan(−ln|a|/arg a)** |
| M59.18, M59.9 | none | no ax+b-invariant ray; no standard pair with a multiplicity-one unit step |
| M59.11 | canonical Hardy model | transported structural invariants constant; canonical representatives separated at ‖δ‖/√2 |
| M59.17 | any μ | MaxEnt at fixed energy is the θ-independent geometric field |
| **M59.21, M59.24, M59.25** | closed families / open paths | rigidity and the two bounds; **closure dependence**; no family ⇒ no field |
| **M59.22, M59.23** | finite transversal transports; any strict contraction for the harmonic part | **branch field ↔ degree-zero divisor; E(D) \= E\_min \+ 2π\[n₀ \+ Σm\_jF(θ\_j)\]; E ≤ E\_min \+ π‖D‖; a\_{1/2} \= 2 arctan((1−r)/(1+r))** |

**Z-Spin content, isolated.** Four things and nothing else: the value **λ** \= (iπ/2)z*; the unit as ZS-M46's Abel translation; the reading of the branch field as a discrete Z-bias field whose jump points are the corpus's Z-anchors; and the register hypotheses that would fix its range at Q*\* \= 11\. Everything else is a theorem about sampled unitaries, degree theory and harmonic measure.

# \**§18. Seed — ZS-M60,* The S14 Seam-Transport Dichotomy: Nonvanishing Rigidity or Anchor-Divisor Selection\*\*\*

*Retitled at v1.8. The former title, "The Anchor Divisor of the Seam", presupposed that a divisor exists. It is a dichotomy, and both branches are complete results.*

**The dichotomy.** Construct from the S14 action a continuous closed θ-family ã; then

**ã nowhere zero  ⟹  D \= 0 , n(θ) constant ;     ã vanishing somewhere  ⟹  D \= Σⱼ mⱼ δ\_{θⱼ}  computed**

**D \= 0 is a complete result, not a failure**: it is a no-go showing that intrinsic branch selection is impossible along the S14 path, and the anchor-divisor route would then be CLOSED-NEGATIVE.

**Exactly four deliverables.** ZS-M60 should attempt these and nothing more; folding the channel, the carrier and the clock into one paper is how the earlier versions of this line accumulated their retractions.

10. **Derive the open seam transport from the S14 action** — not assume it.  
11. **Construct a closure prescription without external choice, or prove that no canonical closure exists.** Theorem M59.24 shows this is the decisive step: two admissible closures of the frozen path give windings 0 and 1\.  
12. **Construct the θ-family from the action.** dim **Z** \= 2 supplies coordinates, not a family; v1.4's assertion that it did was retracted.  
13. **Decide nonvanishing versus transverse zeros with nonzero local degree**, and in the latter case compute D.

**What §11.3–11.4 then supply for free.** Given D: the field n\_D by M59.22(i) with the predeclared S1 lift; the energy E(D) exactly by M59.22(ii) with F in closed form; the ceiling E\_min \+ π‖D‖ by M59.22(iii); and the maximum number of values by M59.21(4).

**Beyond M60, nothing is reserved.** If D \= 0 the anchor route closes and a new code should be assigned only when a different physical realization route is found. If D ≠ 0, the next paper is *From the S14 Anchor Divisor to a Pointer-Preserving Z-Spin-Mediated QND Channel*, which must construct D → n\_D → completion → eleven-dimensional record representation → CPTP channel and prove ⟨Ψ\_D, U\_D(n)Ψ\_D⟩ \= **λ**ⁿ with pointer preservation. **Its code is assigned after M60 reports, not before.**

**Discipline.** Pre-register D before comparing with ρ\_**λ** (F-M59.51). Report the nonvanishing branch as a full result. Do not import completion-side or ZS-M46 objects. **"The action-derived branch" remains prohibited** until the dichotomy is decided.

# **Acknowledgements and Code Availability**

The author thanks the reviewers of v1.0, v1.2, v1.3, v1.4, v1.5 and v1.6. The v1.6 review found an exactness claim certified by a tolerance, an interpretation that misread a signed pairing, an overstated generality, an unnamed selector, and an abbreviated bibliography; chasing the first produced the closed forms of §11.4 and the identity a\_{1/2} \= 2 arctan(inf ρ\_λ). The v1.7 review found a single local type error — a closed-loop theorem applied to an open path — and its correction produced Theorem M59.24, which is the reason ZS-M60's first deliverable is a closure prescription.

**Code.** \`zs\_m59\_verify\_v1\_8.py\` — one file, mpmath and numpy, exactly **148 ledger rows** in every scenario, explicit FAIL rows for missing evidence, exit code 1 on any FAIL, JSON to \`zs\_m59\_verify\_v1\_8.json\`. Blocks: A–W (spine), V (v1.1), Z (v1.2, re-typed), Y (v1.3), X (v1.4), S (seed), P (faithfulness repair), N (anchor rigidity), E (named axioms), C (v1.6 corrections), D (divisor calculus), H (v1.7: exact CDF, half-mass radius, the inf ρ identity, closed-form F, layer-cake, and the seven scope fixes), **T (v1.8: open-path retraction, closure-dependence counterexample, no-family proposition, corrected corollary, lift re-typing, terminal-in-scope declaration)**. Block N row N6 and seed row S2 are type-corrected in this release. During v1.6 construction the fail-closed mechanism fired correctly, emitting explicit FAIL rows when the declared ledger size exceeded the rows produced; the size was corrected rather than the mechanism relaxed.

This work used AI tools (Anthropic Claude) for corpus and external-literature search, cross-paper integration, symbolic and numerical verification, and drafting, under the author's editorial direction. The author assumes full responsibility for all content.

# **Appendix A — Verification ledger (148 rows, 0 FAIL)**

| Block | Rows | Tiers | Headline |
| ----- | ----- | ----- | ----- |
| A freeze | 6 | 3T·2N·1G | **λ** from z\*; moments 2.57 × 10⁻⁴¹; exact ρ extrema; sup gap 2.81 × 10⁻⁸ |
| B minimal dilation | 3 | 1T·1N·1I | Toeplitz λ\_min \= 0.07056008 |
| C logarithms | 5 | 1T·3N·1G | three branches; residuals ≈ 10⁻⁴⁰ |
| D section measure | 4 | 3T·1N | m(S\_n) \= 2π; dense gap 3.835 × 10⁻⁴ |
| E,F folding | 4 | 3T·1P | 1 versus ℵ₀ |
| G embeddings | 4 | 2T·2N | four fields to 1.48 × 10⁻³⁰ |
| H unfolding (spine) | 5 | 4T·1N | wrapped Cauchy 7.89 × 10⁻³¹; δ\_neg |
| I half-step | 2 | 1T·1N | F2 \= 0 exactly |
| J,L energy and S1 | 5 | 3T·2N | E\_min \= 2.31340315; μ/π divergence |
| K dichotomy | 5 | 3T·2N | isometry 0.00; intertwining 1.59 × 10⁻¹⁴ |
| M real structure | 3 | 2T·1G | conjugation; H\_ev not invariant |
| N convex (spine) | 4 | 1T·2P·1G | finite model 1.11 × 10⁻¹⁶ |
| P window family | 3 | 2T·1G | retraction control |
| Q anti-numerology | 3 | 2N·1G | 0 hits; 3.06 % / 25.42 % |
| R,W guards | 3 | 3G | 12 statuses; 0 banned phrases |
| V (v1.1) | 11 | 9T·2N | transversal counterexample; extreme points; barycentre 4.8 × 10⁻⁶; escape sequence; energy slice; MaxEnt 3.7 × 10⁻⁴⁰; branch deficits; invariant subspace; pair obstruction |
| Z (v1.2, re-typed) | 11 | 7T·2N·1G·1I | σ into 𝔐; no fixed point; character −1 at ½; E\_S1 → π; ray-level P; VDV⁻¹ \= d/dx 5.74 × 10⁻⁴²; transport isometry 0; vacuity guard |
| Y (v1.3) | 12 | 7T·3N·2G | σ not surjective; not transitive; 𝒢-torsor; ℤ constant subgroup; separation witness; 2π**Q**; E\_Q; Q-comb; type guard |
| X (v1.4) | 7 | 4T·1N·2G | comb zeros on (1/**Q**)ℤ\\ℤ; ker(I−σ) \= 1; time group; 2**Q** \= 22; parity law |
| S (seed) | 4 | 4G | target; anchor divisor; 13 → 1; falsifiers |
| P (faithfulness) | 4 | 3T·1N | counterexample; reality lemma |
| N (anchor rigidity) | 7 | 6T·1N | rigidity; jumps; degree zero; staircase; ZS-S28 path nonvanishing |
| E (axioms) | 3 | 3G | (H-EQUIVARIANT-SELECTION); double-cover downgrade; wording |
| C (v1.6) | 6 | 5T·1N | location counterexample; \#supp ≥ V; ‖D‖ ≥ 2(V−1) with 20 on the counterexample; cancellation control; rank k−1; dual norm 0.707160 |
| D (divisor) | 5 | 4T·1G | E(D) to 1.6 × 10⁻¹⁹; n\_D; E ≤ E\_min \+ π‖D‖; concentration; status |
| **H (v1.7)** | **13** | **6T·7G** | **exact-half retraction; CDF closed form 0.0; a\_{1/2} \= 0.114583066682673187 with CDF ½; inf ρ identity; F closed form 4.93 × 10⁻³¹; layer-cake 0.0; and the seven scope fixes** |
| **T (v1.8)** | **6** | **4T·1N·1G** | **open-path retraction (|a(1)−a(0)| \= 1.711032173); closure winding 0 vs 1; no-family proposition; corrected corollary; lift re-typing; TERMINAL-IN-SCOPE** |
| **Total** | **148** | **82T · 31N · 3P · 30G · 2I** | **0 FAIL** |

**PROXY rows barred from theorem tables:** E2 (K \= 400 folding truncation), N1, N2 (finite convex model).

# **Appendix B — Proofs**

**B.1 (Theorem M59.2, affiliation).** U \= M\_z on L²(𝕋,μ) with μ ≡ dθ and cyclic vector **1**. The polynomials in z and z̄ are weak-\\ *dense in L^∞(𝕋) for a measure equivalent to Lebesgue, so the von Neumann algebra generated by U is L^∞(μ), whose commutant is itself: U′ \= L^∞(μ) is maximal abelian*\*, the operator content of multiplicity one. If P is self-adjoint with e^{iP} \= U, every spectral projection E\_P(B) commutes with U \= e^{iP}, hence lies in U′; so P is affiliated with a maximal abelian multiplication algebra and is multiplication by a real measurable p on {f : pf ∈ L²}. From e^{ip(θ)} \= e^{iθ} μ-a.e. and μ ≡ dθ, p(θ) − θ ∈ 2πℤ a.e., and n := (p−θ)/2π is measurable. Conversely each p\_n exponentiates to U.

**B.2 (Extreme points, measurable kernels).** Identify ν ∈ 𝔐 with a measurable kernel θ ↦ w(θ) ∈ 𝒫(ℕ₀). *(⇐)* If w \= δ\_{n(θ)} a.e. and ν \= ½(ν₁+ν₂) with ν\_i ∈ 𝔐, then for a.e. θ two probability measures average to a Dirac mass, which is extreme in 𝒫(ℕ₀), so w₁ \= w₂ \= δ\_{n(θ)}. *(⇒)* Let A \= {θ : w(θ) not Dirac} with μ\_**λ**(A) \> 0\. The sets {θ : w\_k(θ) \> 0} are measurable, so k₁(θ) \= min supp w(θ) and k₂(θ) \= min(supp w(θ)\\{k₁}) are measurable selections on A. With ε \= ½min(w\_{k₁}, w\_{k₂}) \> 0 on A and 0 off A, the kernels w^± \= w ± ε(δ\_{k₁} − δ\_{k₂}) are admissible, distinct, and average to w.

**B.3 (Inverse-CDF barycentre).** Set F\_θ(k) \= Σ\_{j≤k}w\_j(θ) and n\_u(θ) \= min{k : F\_θ(k) ≥ u}. Each F\_θ(k) is measurable in θ, so {(θ,u) : n\_u(θ) \= k} \= {F\_θ(k) ≥ u \> F\_θ(k−1)} is product-measurable; hence n\_u is a measurable section for each u and ν\_{n\_u} ∈ ext 𝔐 by B.2. For fixed θ and U uniform, Pr\[n\_U(θ) \= k\] \= w\_k(θ), so Fubini gives ∫₀¹(∫g dν\_{n\_u})du \= ∫Σ\_k w\_k(θ)g(θ+2πk)dμ\_**λ** \= ∫g dν.

**B.4 (Energy slices).** Convexity: ν ↦ ∫p dν is linear. Tightness: ν(\[P,∞)) ≤ E/P uniformly on 𝔐\_E. Narrow closedness: for f ∈ C(𝕋), p ↦ f(p mod 2π) is bounded continuous, so the periodization constraint passes to narrow limits; and p ≥ 0 is continuous, so ∫p dν ≤ liminf ∫p dν\_j ≤ E by portmanteau. Prokhorov gives narrow compactness. Non-emptiness: the infimum of ∫p dν over 𝔐 is E\_min, attained by the k ≡ 0 transversal, so 𝔐\_E ≠ ∅ iff E ≥ E\_min.

**B.5 (Interval agreement forces the Cauchy measure).** φ\_ν(t) \= ∫\_{ℝ₊}e^{itp}dν is holomorphic on the open upper half-plane ℍ (dominated convergence, |e^{itp}| ≤ 1 there) and continuous on ℍ ∪ ℝ. On branch k, **λ**^t \= e^{t(−μ+i(χ+2πk))} is entire. Let g \= φ\_ν − **λ**^{(·)} vanish on a nonempty open interval I ⊂ ℝ₊. Define G \= g on ℍ ∪ I and G \= 0 on ℍ⁻; G is continuous across I and holomorphic off ℝ, hence holomorphic on the connected set ℍ ∪ I ∪ ℍ⁻ by Morera on rectangles straddling I. Since G ≡ 0 on the open set ℍ⁻, the identity theorem gives G ≡ 0, so φ\_ν \= **λ**^t on ℝ₊. With φ\_ν(−t) \= conj φ\_ν(t), φ(t) \= e^{−μ|t|}e^{i(χ+2πk)t}, the characteristic function of the Cauchy law of location χ+2πk and scale μ; Bochner uniqueness identifies ν with it, and its ℝ₋ mass is (1/π)arctan(μ/(χ+2πk)) \> 0, contradicting supp ν ⊆ ℝ₊.

**B.6 (Imported standard-pair uniqueness).** The imported statement: *a standard pair (H,U) with U(t) \= e^{itP}, P ≥ 0, U(t)H ⊆ H for t ≥ 0 and no nonzero U-invariant vector is unitarily equivalent to a direct sum or integral of copies of the unique irreducible such pair, realized on L²(ℝ₊,dp) with U(a)ψ(p) \= e^{iap}ψ(p)* \[Rieffel–van Daele 1977; Longo 2008; Borchers 1992; imported by ZS-M46 Theorem A(i)\]. Non-degeneracy is part of the hypothesis and automatic for a standard pair, a nonzero invariant vector lying in H ∩ iH after averaging. Theorem M59.4 gives multiplicity ℵ₀ for the irreducible unit-time element, and multiplicities add over sums and integrate over direct integrals.

**B.7″ (State-level faithfulness, final).** *(1)* ω\_Ψ \= ω\_{Ψ′} on ℛ(H) iff Ψ−Ψ′ ∈ H′. *(2) Reality lemma:* a real ψ ∈ L²(ℝ₊,dp) in H or H′ has an even real conjugate-symmetric extension, hence an even real inverse Fourier transform; one-sided support forces support in {0} and ψ \= 0\. *(3)* W\_c gives real representatives |ψ\_ν|, so distinct completions are separated. *(4) Dual norm:* for f real supported in (0,∞), h\_f \= f̂|\_{ℝ₊} has ‖h\_f‖ \= √π‖f‖ by Plancherel and evenness of |f̂|, while Im h\_f(p) \= ∫₀^∞f(x)sin(px)dx \= √(π/2)F\_s\[f\](p). Hence |Im⟨δ,h\_f⟩| \= √(π/2)|⟨δ, F\_s f⟩| ≤ √(π/2)‖δ‖‖f‖ \= ‖δ‖‖h\_f‖/√2, with equality at f \= F\_s\[δ\] since F\_s is unitary and involutive on L²(0,∞).

**B.8′ (Anchor Rigidity).** *(1)* The space of nonvanishing loops has components indexed by winding, and 𝕋 is connected. *(2)* Off the projection of the zero set the family is locally nonvanishing so n is locally constant; the argument principle gives Δn \= ± the local intersection multiplicity at a transverse crossing, while cancelling crossings give Δn \= 0 — necessity but not sufficiency. *(3)* n is single-valued on 𝕋. *(4)* V values need V arcs and \#arcs \= \#jumps; and Σ|m\_j| \= total variation ≥ 2(max n − min n) ≥ 2(V−1).

**B.9 (Divisor calculus).** *(i)* n − S\_D is locally constant and 𝕋 is connected, so n \= n₀ \+ S\_D; n ≥ 0 iff n₀ ≥ −min S\_D, minimal at equality. *(ii)* E \= E\_min \+ 2π∫n dμ and ∫S\_D dμ \= Σ\_j m\_j μ((θ\_j,2π)) by Fubini on S\_D \= Σ\_j m\_j **1**\_{(θ\_j,2π)}. *(iii)* With min n \= 0, max n \= range(S\_D) ≤ ½Σ|m\_j|, so ∫n dμ ≤ ‖D‖/2.

**B.10 (Closed forms, new).** The Poisson kernel has the antiderivative ∫dφ/(1−2r cos φ \+ r²) \= (2/(1−r²))arctan(κ tan(φ/2)) with κ \= (1+r)/(1−r). *(i)* Integrating the wrapped-Cauchy density over (−a,a) gives Pr(|Θ−χ| \< a) \= (2/π)arctan(κ tan(a/2)). *(ii)* Setting this to ½ gives κ tan(a/2) \= 1, i.e. a\_{1/2} \= 2 arctan(1/κ) \= 2 arctan((1−r)/(1+r)); and (1−r)/(1+r) \= (1−e^{−μ})/(1+e^{−μ}) \= tanh(μ/2). *(iii)* (1−r)/(1+r) \= inf ρ\_**λ** by §1.2, whence a\_{1/2} \= 2 arctan(inf ρ\_**λ**). *(iv)* G is the continuous branch of the same antiderivative, and F \= G(2π) − G. *(v)* ∫₀^{2π}θ dμ \= ∫₀^{2π}μ((t,2π))dt by the layer-cake formula.

**B.11 (Closure dependence, Theorem M59.24). \[new\].** The frozen path γ(s) \= exp(sℓ) has γ(0) \= 1 and γ(1) \= **λ** ≠ 1, so it is not a loop and wind(γ) is undefined. Let γ\_A be γ followed by the straight segment **λ** → 1, and γ\_B be γ followed by an arc from **λ** to 1 whose continuous argument increases to 2π. Both are closed curves avoiding the origin — minimum modulus 0.4024 and 0.8915 along the segments — and their total argument increments are 0 and 2π, so wind(γ\_A) \= 0 and wind(γ\_B) \= 1\. Hence the winding of a closure is a function of the closure, not of γ. *(Row T2.)*

**B.12 (No family, no field, Proposition M59.25). \[new\].** A branch field is by definition a function on 𝕋\_θ. A single path is a family indexed by a one-point set, whose only functions to ℤ are constants. Hence a single path determines at most a constant, independently of any topological hypothesis.

# **Appendix G — Retraction register of ZS-M59** *(cumulative)*

| Retracted | Version | Replacement |
| ----- | ----- | ----- |
| "identifiable ⟺ single-window ⟺ bounded"; "Nyquist Dichotomy"; 𝔐 weak-\\\* compact; extreme points "HYPOTHESIS-strong"; "exactly one of the following"; "half-sided invariance fails"; F-M59.29 wording; "standardness half of B3 closed" | v1.0 | Thm M59.13; energy slices; PROVEN extreme points; dichotomy \+ refinement; Standard-Pair Obstruction; interval hypothesis; §8 decomposition |
| "the selector jumps across the cut" | v1.2 draft | equivariance, not continuity |
| free ℤ-action / alias torsor on 𝔐; B3 CLOSED-EMPTY; VOID pointing; unrestricted downstream powerlessness; TERMINAL | v1.2 | 𝒢-torsor on 𝔏; conditional B3; UNDECLARED; structural/state split; withdrawn |
| "j/Q, j \= 1…Q−1"; unqualified "no canonical origin"; M59.20 without its selection principle | v1.3 | (1/**Q**)ℤ\\ℤ; "event data alone"; (H-TRUNC)+(H-MAXENT) vs (H-WRAP) |
| Appendix B.7's density argument; the winding trichotomy; "dim Z \= 2 guarantees the family"; "the doubling being exactly dim Z"; M59.20B without its axiom | v1.4 | B.7″; Theorem M59.21 with four prerequisites; OBSERVATION; three named hypotheses |
| "≥ 2(Q−1) crossing LOCATIONS"; "anchors ⟺ non-constant field"; unqualified "finitely generated residual" and "lower bound"; "isometric" without its constant; "physical selection reduced to a computation"; (H-CARRIER-11) "becomes a count" | v1.5 | \#supp D ≥ V and ‖D‖ ≥ 2(V−1); necessity with transversality; rank k−1 for fixed support and a realizability restriction; sup \= ‖δ‖/√2; one candidate route plus an open gate; REFORMULATED |
| **"exactly half the mass within |θ−χ| \< μ"; "the Cauchy quartile"; "an independent confirmation"** | **v1.6** | **a\_{1/2} \= 2 arctan(tanh(μ/2)) \= 0.114583066682673187 with CDF exactly ½; measured mass at radius μ \= 0.50069959154154853** |
| **"anchors away from χ are almost free, χ is the expensive phase"** | **v1.6** | **the cost is the signed pairing plus n₀(D); F varies most steeply near χ** |
| **"no selection principle needed"** | **v1.6** | \**no* additional *axiom beyond the predeclared minimal-lift rule S1*\* |
| **"for an arbitrary strict contraction / arbitrary continuous transports"** | **v1.6** | **finite transversal transports with isolated projected degeneracies of nonzero local degree** |
| **row D4's tolerance test certifying an exact claim** | **v1.6** | **exactness and approximation on separate rows (H2–H4); new ledger rule** |
| **Corollary M59.21b — a closed-loop winding theorem applied to the open frozen path; the Abstract sentence resting on it; verifier rows N6 and S2** | **v1.7** | **Theorem M59.24 (closure dependence: winding 0 versus 1); Proposition M59.25 (no family, no field); Corollary M59.21b′ \[DERIVED-CONDITIONAL\]; "winding zero" re-typed as a ZS-M58 layer-L2 lift statement** |

# **References**

\[1\] B. Sz.-Nagy, "Sur les contractions de l'espace de Hilbert," *Acta Sci. Math. (Szeged)* **15**, 87–92 (1953); B. Sz.-Nagy and C. Foiaş, *Harmonic Analysis of Operators on Hilbert Space* (North-Holland, Amsterdam, 1970; revised edition, Springer, New York, 2010).  
\[2\] P. R. Halmos, *Introduction to Hilbert Space and the Theory of Spectral Multiplicity*, 2nd ed. (Chelsea, New York, 1957).  
\[3\] M. H. Stone, "On one-parameter unitary groups in Hilbert space," *Ann. Math.* **33**, 643–648 (1932).  
\[4\] W. Rudin, *Functional Analysis*, 2nd ed. (McGraw-Hill, New York, 1991), Chs. 12–13.  
\[5\] K. Schmüdgen, *Unbounded Self-adjoint Operators on Hilbert Space*, Graduate Texts in Mathematics **265** (Springer, Dordrecht, 2012).  
\[6\] J. Zak, "Finite translations in solid-state physics," *Phys. Rev. Lett.* **19**, 1385–1387 (1967).  
\[7\] M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, New York, 1978), §XIII.16.  
\[8\] S. Bochner, *Vorlesungen über Fouriersche Integrale* (Akademische Verlagsgesellschaft, Leipzig, 1932); G. Herglotz, "Über Potenzreihen mit positivem, reellem Teil im Einheitskreis," *Ber. Verh. Sächs. Akad. Wiss. Leipzig* **63**, 501–511 (1911).  
\[9\] M. G. Krein, "Sur le problème du prolongement des fonctions hermitiennes positives et continues," *C. R. (Doklady) Acad. Sci. URSS* **26**, 17–22 (1940).  
\[10\] A. Devinatz, "On the extensions of positive definite functions," *Acta Math.* **102**, 109–134 (1959).  
\[11\] P. E. T. Jorgensen and R. Niedzialomski, "Extension of positive definite functions," *J. Math. Anal. Appl.* **422**, 712–740 (2015); arXiv:1212.3047.  
\[12\] H. S. Shapiro and R. A. Silverman, "Alias-free sampling of random noise," *J. Soc. Indust. Appl. Math.* **8**, 225–248 (1960).  
\[13\] F. J. Beutler, "Alias-free randomly timed sampling of stochastic processes," *SIAM J. Appl. Math.* **19**, 447–464 (1970).  
\[14\] M. A. Rieffel and A. van Daele, "A bounded operator approach to Tomita–Takesaki theory," *Pacific J. Math.* **69**, 187–221 (1977).  
\[15\] R. Longo, "Real Hilbert subspaces, modular theory, SL(2,ℝ) and CFT," in *Von Neumann Algebras in Sibiu*, Theta Series in Advanced Mathematics **10** (Theta, Bucharest, 2008), pp. 33–91.  
\[16\] H.-J. Borchers, "The CPT theorem in two-dimensional theories of local observables," *Commun. Math. Phys.* **143**, 315–332 (1992).  
\[17\] H.-W. Wiesbrock, "Half-sided modular inclusions of von Neumann algebras," *Commun. Math. Phys.* **157**, 83–92 (1993); Erratum *ibid.* **184**, 683–685 (1997).  
\[18\] R. Longo and E. Witten, "An algebraic construction of boundary quantum field theory," *Commun. Math. Phys.* **303**, 213–232 (2011).  
\[19\] Y. Tanimoto, "Construction of wedge-local nets of observables through Longo–Witten endomorphisms," *Commun. Math. Phys.* **314**, 443–469 (2012).  
\[20\] R. Correa da Silva and G. Lechner, *Inclusions of Standard Subspaces*, preprint (first circulated 2021; current public version 2025). *The v1.6 manuscript dated this entry 2021; the discrepancy with the current version is recorded rather than silently corrected.*  
\[21\] A. Beurling, "On two problems concerning linear transformations in Hilbert space," *Acta Math.* **81**, 239–255 (1949).  
\[22\] P. D. Lax, "Translation invariant spaces," *Acta Math.* **101**, 163–178 (1959).  
\[23\] K. Hoffman, *Banach Spaces of Analytic Functions* (Prentice-Hall, Englewood Cliffs, NJ, 1962).  
\[24\] P. Koosis, *Introduction to H\_p Spaces*, 2nd ed. (Cambridge University Press, Cambridge, 1998).  
\[25\] E. C. Titchmarsh, *Introduction to the Theory of Fourier Integrals*, 2nd ed. (Oxford University Press, Oxford, 1948). \[Sine transform: unitary and involutive on L²(0,∞).\]  
\[26\] M. A. Naimark, "On a representation of additive operator set functions," *Izv. Akad. Nauk SSSR Ser. Mat.* **7**, 237–244 (1943).  
\[27\] A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory* (North-Holland, Amsterdam, 1982; 2nd ed., Edizioni della Normale, Pisa, 2011).  
\[28\] P. Busch, M. Grabowski and P. J. Lahti, *Operational Quantum Physics*, Lecture Notes in Physics m31 (Springer, Berlin, 1995).  
\[29\] R. F. Werner, "Screen observables in relativistic and nonrelativistic quantum mechanics," *J. Math. Phys.* **27**, 793–803 (1986).  
\[30\] W. Pauli, "Die allgemeinen Prinzipien der Wellenmechanik," in *Handbuch der Physik*, Vol. 5/1 (Springer, Berlin, 1958), p. 60\.  
\[31\] W. G. Unruh and R. M. Wald, "Time and the interpretation of canonical quantum gravity," *Phys. Rev. D* **40**, 2598–2614 (1989).  
\[32\] M. Takesaki, "Conditional expectations in von Neumann algebras," *J. Funct. Anal.* **9**, 306–321 (1972); *Theory of Operator Algebras II* (Springer, Berlin, 2003).  
\[33\] A. Connes, "Une classification des facteurs de type III," *Ann. Sci. Éc. Norm. Supér.* **6**, 133–252 (1973).  
\[34\] U. Haagerup, "Connes' bicentralizer problem and uniqueness of the injective factor of type III₁," *Acta Math.* **158**, 95–148 (1987).  
\[35\] R. L. Hudson and K. R. Parthasarathy, "Quantum Itô's formula and stochastic evolutions," *Commun. Math. Phys.* **93**, 301–323 (1984).  
\[36\] S. Attal and Y. Pautrat, "From repeated to continuous quantum interactions," *Ann. Henri Poincaré* **7**, 59–104 (2006).  
\[37\] R. R. Phelps, *Lectures on Choquet's Theorem*, 2nd ed., Lecture Notes in Mathematics **1757** (Springer, Berlin, 2001).  
\[38\] C. Castaing and M. Valadier, *Convex Analysis and Measurable Multifunctions*, Lecture Notes in Mathematics **580** (Springer, Berlin, 1977).  
\[39\] E. T. Jaynes, "Information theory and statistical mechanics," *Phys. Rev.* **106**, 620–630 (1957).  
\[40\] T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, Hoboken, NJ, 2006), Ch. 12\.  
\[41\] Yu. V. Prokhorov, "Convergence of random processes and limit theorems in probability theory," *Theory Probab. Appl.* **1**, 157–214 (1956).  
\[42\] M. F. Atiyah, V. K. Patodi and I. M. Singer, "Spectral asymmetry and Riemannian geometry III," *Math. Proc. Camb. Phil. Soc.* **79**, 71–99 (1976); see also I, *ibid.* **77**, 43–69 (1975).  
\[43\] J. Phillips, "Self-adjoint Fredholm operators and spectral flow," *Canad. Math. Bull.* **39**, 460–467 (1996).  
\[44\] C. Wahl, "On the noncommutative spectral flow," *J. Ramanujan Math. Soc.* **22**, 135–187 (2007).  
\[45\] E. B. Bogomolny, "The stability of classical solutions," *Sov. J. Nucl. Phys.* **24**, 449–454 (1976).  
\[46\] L. V. Ahlfors, *Complex Analysis*, 3rd ed. (McGraw-Hill, New York, 1979), Ch. 4\. \[Argument principle and the winding number of closed curves — the type constraint of Theorem M59.24.\]  
\[47\] K. Kang, ZS-S28 v3.1 (TERMINAL), ZS-M46 v1.5, ZS-M47 v2.0, ZS-M49 v1.3, ZS-M51 v1.3, ZS-M53 v1.5, ZS-M54 v2.2, ZS-M56 v1.8, ZS-M57 v1.8, ZS-M58 v1.7, ZS-M1 v1.0 (Z-Spin Cosmology Collaboration, 2026).  
\[48\] K. Kang, ZS-F31 v1.4, ZS-F32 v1.5, ZS-F38 v1.2, ZS-F39 v1.1, ZS-A24 v2.1, ZS-A32 v1.1, ZS-Q18 v1.7 (Z-Spin Cosmology Collaboration, 2026).  
\[49\] K. Kang, *ZS-M59 Successor Seed Report*, version 2.1 (Z-Spin Cosmology Collaboration, July 2026); *Compass, Spear and Shield*, version 3.2.

# **Version History**

**v1.0** 59/59 · **v1.1** 70/70 · **v1.2** (TERMINAL, withdrawn) · **v1.3** 93/93 · **v1.4** 104/104 · **v1.5** 118/118 · **v1.6** 129/129 · **v1.7** 142/142 — cumulative retractions in Appendix G.

**v1.7 (July 2026): full-length release.** All ten v1.6 findings upheld. **Retractions:** "exactly half the mass within |θ−χ| \< μ" and its description as a Cauchy quartile and an independent confirmation; "anchors away from χ are almost free"; "no selection principle needed"; the unrestricted generality of the divisor calculus; and row D4's tolerance test for an exact claim. **New results:** **Theorem M59.23** — the exact wrapped-Cauchy CDF (2/π)arctan(κ tan(a/2)); the exact half-mass radius a\_{1/2} \= 2 arctan(tanh(μ/2)) \= 0.114583066682673187 with CDF exactly ½; the identity **(1−r)/(1+r) \= inf ρ\_λ \= tanh(μ/2)**, hence **a\_{1/2} \= 2 arctan(inf ρ\_λ)**; the closed form F(θ) \= G(2π) − G(θ) matching quadrature to 4.93 × 10⁻³¹; and the layer-cake identity **E\_min \= ∫₀^{2π}F** to 0.0, so the whole divisor calculus runs on one elementary function. **Scope corrections:** M59.22 restricted to finite transversal transports with isolated projected degeneracies of nonzero local degree; the divisor route stated as requiring the *predeclared* rule S1 and no additional axiom; the cost of a divisor stated as a signed configuration pairing; faithfulness layered as PROVEN in the canonical Hardy model and DERIVED-CONDITIONAL on ZS-M46 KH1–KH4; ‖D‖ ≥ 2(V−1) stated as necessary given a V-valued field; (H-CARRIER-11) held at REFORMULATED. **Presentation:** §§2–10 restored at full length with every derivation, table and numerical witness; a novelty paragraph placed against the spectral-flow literature; the bibliography written in full APS form with the disputed entry's version discrepancy recorded. **Process:** new ledger rule — an "exact" claim may not be certified by a tolerance test. Verification **142/142 PASS** (78 THEOREM-PROOF · 30 NUMERIC-WITNESS · 3 PROXY · 29 GUARD · 2 IMPORTED), 0 FAIL.

**v1.8 (July 2026): TERMINAL-IN-SCOPE, full-length release.** All five v1.7 findings upheld. **Retraction:** Corollary M59.21b, which applied Theorem M59.21(1) — a statement about continuous **closed loop families** — to ZS-S28's **open** endpoint path; together with the Abstract sentence resting on it and verifier rows N6 and S2. **New results:** **Theorem M59.24 (Closure Dependence)** — the same open path admits closures of winding **0** and **1**, neither meeting the origin, so a closure prescription is the datum that fixes the answer; **Proposition M59.25 (No family, no field)** — a single path has no θ-dependence and therefore carries no field, which is the honest reason ZS-M57 and ZS-M58 each found one integer; **Corollary M59.21b′ \[DERIVED-CONDITIONAL\]** — given a closure prescription and a continuous nonvanishing closed θ-family, M59.21(1) forces a constant winding field, so the corpus's single integers are *consistent with* but not *derived from* the frozen path; and the **re-typing of ZS-S28's "winding zero"** as a ZS-M58 layer-L2 statement about the continuous lift of an open path, with no ZS-S28 field altered. **Status:** ZS-M59 is declared **TERMINAL-IN-SCOPE**, with an explicit scope table (§15) separating the thirteen closed classifications from the four items transferred to the successor. **Successor:** retitled \**ZS-M60,* The S14 Seam-Transport Dichotomy: Nonvanishing Rigidity or Anchor-Divisor Selection\***, limited to four deliverables, with** D \= 0 declared a complete result**; no paper beyond M60 is reserved.** Process: **new ledger rule — a theorem may be applied only to objects of the type it quantifies over, and the type check is itself a row. Verification** 148/148 PASS\*\* (82 THEOREM-PROOF · 31 NUMERIC-WITNESS · 3 PROXY · 30 GUARD · 2 IMPORTED), 0 FAIL.

*Status: TERMINAL-IN-SCOPE. Logarithm, completion, branch-torsor, anchor-rigidity and finite-transversal divisor classifications closed; state-level faithfulness proven in the canonical Hardy model and conditional in its seam realization; the S14 seam transport, its divisor, the carrier intertwiner and the channel realization transferred to ZS-M60.*

*Document formatting specification (protocol §3.8) applied on export: base text Times New Roman 11 pt, line spacing 1.15, paragraph spacing 0 pt before and after, left-aligned, blank line between paragraphs; title 16 pt bold left, section headings 13 pt bold left, subsection headings 12 pt bold left; footnotes and references 9 pt in APS style; table captions 10 pt left, header cells 9 pt bold centred on background \#f3f3f3, borders 0.75 pt black, body cells 9 pt, tables at maximum width; block equations centred with A, Q, λ and key variables in bold; metadata 10 pt with epistemic tags in bold capitals.*  
