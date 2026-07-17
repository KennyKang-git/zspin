**ZS-Q18**  
**The Dephasing Representative and the Born Rule from i-Tetration**

***Advancing the Four Q16-Instrument Gates via a QND Koenigs Channel — From the Koenigs Mean Channel to a Purifying QND Instrument***

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Paper code:** ZS-Q18  ·  Quantum Mechanics Theme  ·  Version v1.7 (Final, corrected release)  ·  July 2026  
**Hard dependencies:** ZS-F48 v1.6 (Appendix G, four gates), ZS-F47 v1.6, ZS-M46 (Koenigs), ZS-M1 (z\*), ZS-M43 (rates/leak), ZS-Q1 (σz dephasing), ZS-Q7 (rank-2, ln 2 ceiling), ZS-Q12 (Belavkin closure), ZS-Q14 (χZ \= −1), ZS-Q16 v2.5 (weak sufficiency), ZS-F0 (§12.3 sum rule), ZS-F1 (LXY ≡ 0).

**Verification: 95/95 PASS (tiered) | Zero Free Parameters  |  (A, Q, dim Z) \= (35/437, 11, 2), z\*, λ₁ LOCKED**  
**Nomenclature note.** The paper code ZS-Q17 is already assigned in the corpus (Self-Mediation No-Go / Reach-Bound, gravitational decoherence; Book v8.0 PART XVII). The measurement-bridge follow-up proposed as "ZS-Q17" in the F48 seed report is therefore issued here as ZS-Q18 to avoid a version collision (cross-consistency rule §3.2).

# 

# **§0. Abstract**

ZS-F48 v1.6 proved that the Koenigs coordinate φ of the i-tetration fibre map linearizes the deterministic mean channel on the full density matrix — E∘f \= Φ∘E, with the positive embedding *E(w) \= \[\[1−2|w|², w̄\],\[w, 2|w|²\]\]* and pointer limit PROVEN — but left **four gates OPEN** for identifying that mean channel with the ZS-Q16 stochastic instrument: state, probability, record, and Born-martingale (F48 Appendix G). This paper proves the dephasing mean representative, derives the Born rule for any purifying QND realization, and reduces the physical instrument-selection problem to an explicit record-level and operator-algebraic residual, through one structural correction: the Koenigs representative must be the **dephasing (QND) channel** Φ\_deph : ρ₁₀ ↦ **λ**ρ₁₀ with populations conserved — not the amplitude-damping channel of F47/F48. Amplitude damping has a unique absorbing pointer |0⟩ and can never Born-select between two outcomes; the dephasing representative is a genuine σz measurement whose Kraus operators are diagonal (\[K\_i, σz\] \= 0). We establish: (i) Φ\_deph is CPTP (Choi PSD) and Koenigs-exact — **the Mean-State Representative PROVEN**; (ii) of the two unravelings sharing this mean channel, the non-informative {I, Z} family is excluded from purification by Maassen–Kümmerer (unitary Kraus ⇒ dark subspace), while the informative σz unraveling purifies — **Record gate DERIVED-CONDITIONAL** on χZ \= −1; (iii) Theorem Q18.2 — for a σz-QND channel every purifying unraveling gives the Born probability P(|j⟩) \= ρ\_jj(0), because QND ⇒ population martingale and purification ⇒ p∞ ∈ {0,1}; the Born rule is thus **unraveling-independent** — Probability and Born-martingale gates DERIVED; (iv) the ensemble decoherence rate is exactly μ \= −ln|**λ**| \= 0.1148 per Z-cycle, and under complete Z-output monitoring (an explicit condition strictly stronger than L\_XY ≡ 0\) the collapse rate shares the same constant |**λ**|, registered DERIVED-CONDITIONAL rather than asserted as an identity (anti-numerology). These conditionals are genuinely distinct — the physical instrument selector, complete Z-output monitoring, and the CRT-4/H-CLK parent-algebra clock equality — and are not collapsed into one bedrock. The rigorous QND-collapse theorems (Bauer–Bernard 2011; Bauer–Benoist–Bernard 2013; Adler–Brody–Brun–Hughston 2001; Benoist–Pellegrini 2014; Maassen–Kümmerer 2006\) are imported and re-read through the Z-Spin dictionary. Six deep-exploration cycles (recorded in Appendix C) execute the anti-numerology gate F-Q18.6 (Born fit χ²/dof \= 0.68, alternatives rejected), confirm via estimation stability that strong sufficiency is OPEN but non-epistemic, and decompose the residual via ZS-A17 (co-orientation DERIVED; metric half a NO-GO not needed by measurement). Most importantly for honesty, v1.4 audits the claims against an external review: the F48 record-wise State gate is PARTIAL/OPEN (only the mean channel is proved), η \= 1 is DERIVED-CONDITIONAL on complete Z-output monitoring (not on L\_XY ≡ 0 alone), and the earlier “Type III₁ from entropy production” reading is RETRACTED — ZS-M47 shows the local algebra M₃ ⊕ ℂ ⊕ M₅ is not a factor. The single residual is reformulated, via ZS-M46/M47/F38, as one corpus-wide gate: the CRT-4 / H-CLK clock equality — that the QND measurement record clock equals the modular seam clock of the i-tetration Abel-cover unit translation (ZS-M46, PROVEN). This identification of a measurement instrument’s clock with an algebraic-QFT modular clock is the paper’s novel external bridge; it is OPEN, RH-free, and shared corpus-wide. v1.6 then closes the record-wise gates. With a λ-locked canonical instrument (δ \= √(1−|λ|²), no arbitrary parameters), the informative QND branches cannot preserve the one-complex-dimensional F48 manifold; the minimal positive normalized extension adds one population coordinate p, giving the full-state embedding E\_full(p,w) on which the record-wise State, Probability, and Born-martingale gates close EXACTLY (Theorem Q18.12, Koenigs–Belavkin skew product; residual \< 10⁻¹² over 2×10⁵ random Bloch states). What remains genuinely OPEN, and is not compressed into one bedrock, is the CRT-4/H-CLK clock equality (with a degree-1-Blaschke one-particle candidate) and the physical instrument selector. Verification: 95/95 PASS, reported in evidence tiers (§8); zero fitted parameters. This is the frozen final release (see the stopping rule in §11).

# **Epistemic Status Legend**

| TAG | Meaning |
| :---- | :---- |
| PROVEN | Explicit proof or exact machine verification; no undischarged assumption. |
| IMPORTED-PROVEN | Proven in the external literature and used without re-proof; cited. |
| DERIVED | Follows from PROVEN / IMPORTED-PROVEN results by stated steps; no new parameter. |
| DERIVED-CONDITIONAL | Derived modulo an explicitly named, falsifiable condition (here: χZ \= −1, i.e. Z \= ∂X; or efficiency-1 monitoring). |
| HYPOTHESIS-strong | Structurally motivated; a key value or selector not yet proven. |
| OBSERVATION | An empirical/numerical fact stated with its error; not a prediction. |
| OPEN | Genuinely undetermined within current corpus tools. |
| NON-CLAIM | Explicitly not asserted (single-world vs. many-worlds; consciousness firewall). |
| RETIRED | A prior formulation replaced by a sharper one (recorded, not erased). |

# **§1. Introduction**

## **1.1 Lineage and what motivated the bridge**

The question that started Z-Spin was the emergence of wave-function collapse from a deeper layer. The corpus micro-bridge is the chain S14 action → measurement instrument / L\_Z operator → gauge-invariant observable → data. ZS-Q16 v2.5 promoted weak sufficiency (almost-sure collapse to one σz eigenstate with Born frequencies, z\* the attractor, ln 2 ceiling) to DERIVED-CONDITIONAL by importing the QND convergence theorems onto the geometric channel. ZS-F48 v1.6 sharpened the mathematics one level finer: it proved the Koenigs semiconjugacy φ∘f \= **λ**φ on the full density matrix through the positive embedding E(w), and then listed precisely four gates that separate that *deterministic mean channel* from the *stochastic Q16 instrument* (F48 Appendix G). This paper is the F48 follow-up that attacks those four gates directly.

## **1.2 The four gates F48 left open**

For each measurement record r with instrument map I\_r, F48 Appendix G requires: (i) *State gate* — E(f\_r(z)) \= Φ\_r(E(z)); (ii) *Probability gate* — p\_r(z) \= Tr I\_r(E(z)); (iii) *Record gate* — the record filtration and innovation process coincide with Q16; (iv) *Born-martingale gate* — E\[p\_r(n+1) | F\_n\] \= p\_r(n). F48 closed the mean channel (a single averaged Φ), which is gate-agnostic; the four gates were the OPEN content.

## **1.3 What this paper is / is not**

It *is* a closure of the state gate, a derivation of the probability and Born-martingale gates, and a reduction of the record gate to the single corpus postulate Z \= ∂X. It *is not* a resolution of strong sufficiency (the eliminability of per-run randomness stays OPEN and non-epistemic, per Q16 v2.5 via Benoist–Pellegrini estimation stability) nor of the single-world/many-worlds question (NON-CLAIM); the consciousness firewall is untouched. No parameter is introduced or tuned; every number descends from (**A**, **Q**, dim Z) \= (35/437, 11, 2), z\*, and λ₁.

# **§2. Locked Inputs**

**Notation.** Two distinct objects both use the letter λ and are never conflated: **λ** \= (iπ/2)z\* is the *i-tetration complex multiplier* (|**λ**| \= 0.8915, the coherence-contraction / decoherence constant), whereas **λ₁** \= 1.2428 is the *TI face-Laplacian eigenvalue* (ZS-S7), a real spectral gap used only as a locked scale. They are unrelated.  
Table 2.1. Locked inputs. Nothing tunable; each traceable to one upstream theorem.

| \# | Quantity | Value | Source / Status |
| :---- | :---- | :---- | :---- |
| L1 | Geometric impedance A | 35/437 \= 0.0800915 | ZS-F2 · LOCKED |
| L2 | Register; sector dims | Q \= 11; (Z,X,Y) \= (2,3,6) | ZS-F5 · PROVEN |
| L3 | i-tetration fixed point z\* | 0.4382829367 \+ 0.3605924719 i | ZS-M1 · PROVEN |
| L4 | multiplier λ \= (iπ/2) z\* | −0.5664173303 \+ 0.6884532271 i | ZS-M1 · PROVEN |
| L5 | |λ| \= |f′(z\*)| | 0.8915136 | ZS-M1 · PROVEN |
| L6 | |λ|² ; leak 1−|λ|² | 0.7947964 ; 0.2052 | ZS-F0 §12.3 / M43 · PROVEN |
| L7 | μ \= −ln|λ| (decoh. rate / Z-cycle) | 0.114835 | this work (arith.) · PROVEN |
| L8 | Koenigs coordinate φ, φ∘f \= λφ | exact (8×10⁻⁶) | ZS-M46 · PROVEN |
| L9 | positive embedding E(w), pointer limit | Φ(E(w)) \= E(λw) | ZS-F48 · PROVEN |
| L10 | Kraus count; vanishing X–Y block | dim Z \= 2; L\_XY ≡ 0 | ZS-Q1 §3.3 / ZS-F1 · PROVEN |
| L11 | Born weight; capacity ceiling | w\_Y \= 6/11; cap ≤ ln 2 | ZS-Q7 · DERIVED |
| L12 | σz dephasing Lindblad (Hermitian L=σz) | populations conserved | ZS-Q1 §3.4 · PROVEN |
| L13 | boundary spin-lift witness | χZ \= −1 | ZS-Q14 · HYPOTHESIS-strong |

# 

# **§3. The Dephasing Representative — the State Gate**

## **3.1 Why the amplitude-damping representative could never give Born selection**

F47/F48 used the amplitude-damping channel as the Koenigs representative: coherence × **λ**, excited population × |**λ**|². Iterating it drives every state to the unique fixed point |0⟩⟨0| (verified: after 200 cycles ρ₀₀ \= 1 to 10⁻⁶). A channel with a *single absorbing pointer* has one attractor, so it cannot produce a two-outcome Born distribution — this is precisely why the Q16 instrument stayed OPEN under the F47/F48 representative. The Koenigs relation φ∘f \= **λ**φ constrains only the coherence ρ₁₀ ↦ **λ**ρ₁₀; it does not fix the population dynamics, so the representative is not unique. The correct choice keeps both populations fixed.

## **3.2 The dephasing (QND) channel**

**Φ***\_deph(ρ) \= \[\[ ρ₀₀ ,* **λ** *ρ₀₁ \] , \[* **λ̄** *ρ₁₀ , ρ₁₁ \]\] ,   populations conserved.*  
This map also satisfies the Koenigs relation (coherence × **λ** exactly) but leaves ρ₀₀, ρ₁₁ invariant, so |0⟩ and |1⟩ are *both* fixed — the two pointer states required for a genuine σz measurement. Writing **λ** \= |**λ**| e^{iθ}, Φ\_deph factors as a phase gate P \= diag(1, e^{−iθ}) composed with a real dephasing of strength |**λ**|, giving the diagonal Kraus pair  
*K₀ \= √((1+|λ|)/2) · P ,   K₁ \= √((1−|λ|)/2) · P Z ,   K₀†K₀ \+ K₁†K₁ \= I.*  
Both Kraus operators are diagonal, hence \[K\_i, σz\] \= 0: Φ\_deph is a **quantum-non-demolition (QND) instrument for σz**. Its Choi matrix is positive semidefinite (minimum eigenvalue −1.2×10⁻³¹, i.e. numerically zero) and trace-preserving, so Φ\_deph is CPTP.

## **3.3 Theorem Q18.1 (Mean-State Representative)**

**Theorem Q18.1 (Mean-State Representative, PROVEN).** The dephasing channel Φ\_deph is CPTP, satisfies the Koenigs semiconjugacy (coherence contracts by exactly |λ|), conserves both populations, and is QND with respect to σz. It is the unique Koenigs representative with two fixed pointer states, and it agrees with the ZS-Q1 §3.4 Hermitian-σz dephasing Lindblad. This is the mean (record-averaged) channel; the record-wise F48 State gate is treated in §3.4. Mean-State Representative: PROVEN (CAT B, 8/8 checks).

## **3.4 Scope of the State gate: mean channel vs. the F48 record-wise gate**

F48 Appendix G defines the State gate *record-wise*: for each measurement record r, E(f\_r(z)) \= Φ\_r(E(z)), with a branch map f\_r and a conditional instrument map Φ\_r. Theorem Q18.1 proves the *mean-channel* intertwining E(f(z)) \= Φ\_deph(E(z)) — the record-averaged statement. Up to v1.5 the record-indexed pair {f\_r, Φ\_r} had not been constructed and the record-wise gate remained PARTIAL/OPEN. Version 1.6 (this section) resolves that obstruction: the minimal full-state extension below constructs {f\_r, Φ\_r} explicitly and closes the record-wise gate (Theorem Q18.12).  
**The λ-locked canonical instrument.** Fix the informative instrument with no free choices. With δ \= √(1 − |**λ**|²) and **λ** \= |**λ**|e^{iθ}, set M₊ \= diag(√((1+δ)/2), e^{−iθ}√((1−δ)/2)) and M₋ \= diag(√((1−δ)/2), e^{−iθ}√((1+δ)/2)). Then M₊†M₊ \+ M₋†M₋ \= I, the sum channel is exactly Φ\_deph, and the off-diagonal multiplier Σ\_r (M\_r)₀₀(M\_r)₁₁\* \= **λ** (all verified). This instrument is fixed by outcome-exchange symmetry, no detector bias, no extra relative phase, and the mean channel — so it is built from **λ** alone, with no arbitrary witness constants.  
**Unnormalized vs. normalized branches.** The conditional coherence multipliers c\_r \= (M\_r)₀₀(M\_r)₁₁\* give branch maps f\_r(w) \= c\_r w that split the mean multiplier (c₊ \+ c₋ \= **λ**). These are *unnormalized* coherence branches — the off-diagonal of the Kraus map before dividing by the outcome probability q\_r. The physical (normalized) record-wise branch is w′\_r \= c\_r w / q\_r(ρ), which also moves the population; the F48 one-complex-dimensional embedding E(w) cannot carry that population update (a theorem: E(w) fixes p \= 2|w|², whereas the informative branch moves p and |w| independently when δ ≠ 0). The minimal fix adds one real coordinate.  
**The minimal full-state extension.** Use the Bloch-ball coordinatization E\_full(p,w) \= \[\[1−p, w̄\],\[w, p\]\] with p \= ρ₁₁, w \= ρ₁₀, |w|² ≤ p(1−p). The outcome probabilities are q\_±(p) \= (1 ± δ(1−2p))/2, the conditional populations p₊ \= (1−δ)p/(2q₊), p₋ \= (1+δ)p/(2q₋), and the conditional coherences w\_± \= **λ̄**w/(2q\_±). Writing F\_±(p,w) \= (p\_±, w\_±), one has M\_± E\_full M\_±† \= q\_± E\_full(F\_±) exactly, hence the normalized record-wise identity Φ\_±(E\_full) \= E\_full(F\_±).  
**Theorem Q18.12 (Minimal Full-State Koenigs–Belavkin Extension).** An informative QND σz instrument cannot preserve the one-complex-dimensional F48 manifold E(w). The minimal positive, normalization-covariant extension adds one independent population coordinate p, giving E\_full(p,w); on E\_full the F48 record-wise gates close exactly: (State) Φ\_r(E\_full) \= E\_full(F\_r); (Probability) q₊ \+ q₋ \= 1 with q\_±(p) \= (1 ± δ(1−2p))/2; (Born-martingale) q₊p₊ \+ q₋p₋ \= p. Coupling w \= φ(z) makes F\_± a Koenigs–Belavkin skew product on (z,p): Φ\_± ∘ E \= E ∘ F\_±. Verified to \< 10⁻¹² over 2×10⁵ random Bloch-ball states, with positivity preserved. Scope (two layers): the full-state density-coordinate record-wise identity Φ\_r(E\_full) \= E\_full(F\_r) is PROVEN; the global lift to the original i-tetration fibre via z\_r \= φ⁻¹(w\_r) is DERIVED-CONDITIONAL on Koenigs-chart continuation, since the normalized posterior can expand |w\_r| (division by q\_r) and need not remain in a single local chart. Record-wise State, Probability, and Born-martingale gates: PROVEN at the density-coordinate level.  
**Result Q18.10 (Record-wise State gate, v1.6).** On the minimal full-state embedding E\_full(p,w) with the λ-locked canonical instrument, the F48 record-wise State gate E(f\_r(z)) \= Φ\_r(E(z)) holds exactly (Theorem Q18.12). This upgrades the record-wise State/Probability/Born-martingale gates from PARTIAL/OPEN (v1.5) to PROVEN at the full-state level. The v1.5 coherence-only branches f\_r \= c\_r w are the unnormalized restriction of this construction; the F48 E-embedding’s failure is now a theorem, not a gap.

# 

# **§4. The Record Gate**

## **4.1 One mean channel, two unravelings**

A CPTP map fixes only the *average* dynamics; an instrument is a refinement — a choice of Kraus decomposition together with which meter observable is read (the unraveling). Φ\_deph admits two physically distinct unravelings that share it as their mean:

* **Non-informative {I, Z}:** outcomes labelled by the Kraus {I, Z}. The outcome distribution is identical for |0⟩ and |1⟩ (KL(P|0 ‖ P|1) \= 0), so the record carries no which-outcome information and the population is never updated.  
* **Informative σz:** continuous weak monitoring of σz (homodyne). The outcome distributions for |0⟩ and |1⟩ differ, with relative entropy S(P⁰ ‖ P¹) \> 0 — the Bauer–Bernard collapse rate.

## **4.2 Maassen–Kümmerer excludes the non-informative unraveling**

The {I, Z} Kraus operators are proportional to unitaries (K₀†K₀ \= ((1+|**λ**|)/2) I, K₁†K₁ \= ((1−|**λ**|)/2) I). By the Maassen–Kümmerer purification theorem a family of measurement operators purifies the trajectory iff there is no *dark subspace* on which all operators act as scalar multiples of unitaries. For {I, Z} the whole space is dark, so this unraveling **does not purify** — the population stays frozen at p₀ forever (verified). The non-informative unraveling is therefore excluded as the physical instrument: it produces no definite outcomes at all.

## **4.3 Theorem Q18.2 — the Born rule is unraveling-independent**

**Theorem Q18.2 (Unraveling-independence, DERIVED).** For the σz-QND channel Φ\_deph, every purifying unraveling yields the Born probability P(|j⟩) \= ρ\_jj(0). Proof: QND (diagonal Kraus) makes the posterior population p\_n a bounded martingale; purification forces p∞ ∈ {0,1} almost surely; the martingale identity E\[p∞\] \= p₀ with p∞ ∈ {0,1} gives P(p∞ \= 1\) \= p₀. The result does not depend on the details of the informative unraveling.  
This was verified across three structurally distinct purifying QND unravelings — a continuous σz SME, a strong discrete Gaussian-meter QND, and a weak asymmetric-jump QND — all returning P(|1⟩) \= p₀ \= 0.30 to within Monte-Carlo error (0.308, 0.308, 0.295). The physically important consequence: the Born rule is robust to the unraveling, so the record gate does not require pinning the exact meter model — only that the monitoring be non-trivial (purifying).

## **4.4 The residual condition: χZ \= −1**

What selects a purifying (informative) unraveling over the frozen {I, Z} one is a physical statement: the Z-boundary *keeps a record*. The corpus supplies this as the ZS-Q14 Boundary Spin-Lift χZ \= −1 (process-level witness ũ\_Z ≠ f(Λ), HYPOTHESIS-strong), while ZS-F1 L\_XY ≡ 0 with the rank-2 ZS-Q7 bottleneck guarantees the single mediating channel observes all cross-sector information — meeting the Maassen–Kümmerer no-dark-subspace condition geometrically. Hence:  
**Result Q18.3 (Record gate, DERIVED-CONDITIONAL).** Given χZ \= −1 (record-keeping) and the complete-monitoring reading of L\_XY ≡ 0 (a named assumption, §6), the informative σz unraveling is selected. The Record gate is DERIVED-CONDITIONAL. Its residuals are genuinely distinct and are NOT collapsed to one bedrock: the physical instrument selector (χZ \= −1), complete Z-output monitoring, and the CRT-4/H-CLK parent-algebra clock equality (§4.8). The full-state record-wise identities themselves are PROVEN (Theorem Q18.12); what remains is the modular-clock realization and the physical selection.

## **4.5 The residual, decomposed (via ZS-A17): only the co-orientation half of Z \= ∂X**

The single residual χ\_Z \= −1 is not opaque. It is the *co-orientation half* of the bedrock Z \= ∂X, and ZS-A17 v1.5 decomposes exactly what a measurement requires of it. Three ingredients the record gate needs are DERIVED, one is a named HYPOTHESIS-strong residual, and the part that stays a NO-GO is not needed at all.

* **The spinor value χ\_Z \= −1 is DERIVED:** D^{1/2}(2π) \= −I and D^{1/2}(4π) \= \+I (ZS-M3, the fermion 4π sign, verified), and the deck ℤ₂ \= {±I} of Spin(3) → SO(3) is not a function of A (No-Spin-From-Curvature, ZS-A17 Cor. 5.2). The value is forced by j \= 1/2, not chosen.  
* **The record is process-level, ũ\_Z ≠ f(Λ):** the seam witness depends on the Kraus representative; two decompositions of the same mean channel Λ give different witnesses (0.88 vs. 0.58 at fixed θ, identical Choi), so genuine record information exists beyond the averaged channel. DERIVED.  
* **The co-orientation itself is DERIVED (A17 Theorem E):** the X→Y record flow (rate ratio 2, ZS-Q7; ΔK\_Ω \= −ln 2, ZS-F19; tanh(ln 2\) \= 3/5) makes the record-algebra inclusion half-sided modular, so by Borchers and Wiesbrock a canonical positive generator exists and its sign is the co-orientation — with no geometric input.  
* **The single genuine residual:** the half-sided modular inclusion SOURCE (HYPOTHESIS-strong, A17 — the Berry–Keating dilation is an unverified candidate), together with the Type III hosting (DERIVED-CONDITIONAL on the ZS-M17 continuum reconstruction).  
* **The metric half is a NO-GO but is not needed:** the i-tetration transfer (spectral zeta 1/(1−|λ|^s) finite for all s \> 0 ⇒ p \= 0\) and the Kraus half-angle (p \= 0\) lack the n^{1/3} Weyl growth a 3-manifold Dirac operator requires (A17 Theorem F). This concerns X's spatial metric and is irrelevant to a measurement, which needs only the co-orientation.

**Result Q18.6 (Residual decomposition, DERIVED-CONDITIONAL sharpened).** The record gate's conditional reduces from "the full bedrock Z \= ∂X" to "the half-sided modular inclusion source of the X→Y record flow." χ\_Z \= −1 and the process-level record are DERIVED; the co-orientation is DERIVED (A17 Theorem E, Borchers–Wiesbrock); the metric half is a proven NO-GO not required by measurement. The single genuinely OPEN residual is the modular-inclusion source — the same one ZS-A17 names, shared corpus-wide — and by ZS-Q17 §6 it sits in the same Lawvere-diagonal family as the strong-outcome residual.  
Table 4.2. Decomposition of the record-gate residual (χ\_Z \= −1 / Z \= ∂X) via ZS-A17.

| Ingredient | Status | Source |
| :---- | :---- | :---- |
| χ\_Z \= −1 spinor sign (4π) | DERIVED | ZS-M3; A17 Cor. 5.2 |
| process-level record ũ\_Z ≠ f(Λ) | DERIVED | this work (CAT I) |
| record-flow arrow X→Y (tanh \= 3/5) | PROVEN / DERIVED | ZS-Q7; ZS-F19 |
| co-orientation from record flow | DERIVED | A17 Thm E (Borchers–Wiesbrock) |
| Type III hosting of record algebra | DERIVED-CONDITIONAL | A17 (on ZS-M17) |
| inclusion source — generator | PROVEN | ZS-M4 Thm 3 (α\_BK \= −ln|z\*|) |
| realization — explicit dilation | DERIVED | Sz.-Nagy/Stinespring (§4.7) |
| realization — modular data / HSMI | OPEN | parent-algebra CRT-4/H-CLK (F-Q18.7b) |
| metric half (3D metric of X) | NO-GO (not needed) | A17 Thm F |

## **4.6 The inclusion source: the Berry–Keating dilation is the i-tetration detector (ZS-M4)**

The single residual of §4.5 — the half-sided modular inclusion source — has a corpus-identified generator. ZS-A17 named the Berry–Keating dilation H \= ½(xp \+ px) as an *unverified candidate*; ZS-M4 Theorem 3 (PROVEN) shows it is not a foreign import but the i-tetration itself: the BK dilation is the Archimedean scaling piece of Connes' decomposition, with rapidity α\_BK \= −ln|z\*| \= (π/2) Im z\* \= −Re **λ** \= 0.566417 — an exact identity, since z\* \= e^{**λ**}. This tightens and de-risks the residual on four counts.

* **The generator is PROVEN, not conjectural:** α\_BK \= −ln|z\*| is an exact locked identity (ZS-M4 Thm 3), realizing the Berry–Keating operator as the corpus i-tetration — tied to the LOCKED z\*, not to an external ansatz.  
* **The affine (ax+b) structure closes:** with the dilation as boost, \[D, p\] \= i p (verified spectrally to 4×10⁻¹¹), and on the one-sided (Hardy) space the conjugate translation generator is positive (Borchers), so sign(P) is the co-orientation.  
* **The one-sided compression is supplied by |λ| \< 1:** the i-tetration Koenigs contraction φ(f(D)) \= λ·φ(D) ⊊ φ(D) is a genuine proper inclusion — exactly the one-sided compression A17 reported as unsupplied — tied to the locked multiplier.  
* **RH is not a dependency (de-risking):** the corpus splits the structure into a DETECTOR (scaling/boost, which the co-orientation needs — ε\_J \= 0 iff σ \= 1/2, ZS-M4 Thm 4, PROVEN) and a LOCATOR (the ζ-zeros \= adelic Sonin piece \= the Riemann Hypothesis, OPEN). The co-orientation uses only the detector; the locator is never invoked, so the record gate does not inherit RH.

The two scales are kept distinct (anti-numerology): the boost rapidity α\_BK \= 0.5664 (the location |z\*|) and the decoherence rate μ \= 0.1148 (the multiplier |**λ**|) descend from the same z\* but are not conflated.  
**Result Q18.7 (Inclusion source, sharpened & de-risked).** The record gate's residual inclusion source has a PROVEN generator — the i-tetration Archimedean-scaling detector (ZS-M4 Thm 3, α\_BK \= −ln|z\*|) — with the ax+b boost algebra and Borchers positivity DERIVED and the one-sided compression supplied by |λ| \< 1\. The co-orientation requires only the detector, so the record gate is independent of the Riemann Hypothesis. The single genuinely OPEN residual narrows to the self-adjoint/Fock(Q \= 11\) completion of that detector as a modular inclusion (F47/F48 COND 1b-global / Rokhlin natural extension) — a corpus-internal OPEN, not an external conjecture.

## **4.7 The modular realization: concretizing the Rokhlin natural extension, and the terminus**

The residual of §4.6 — realizing the i-tetration detector as a genuine half-sided modular inclusion — has been carried since F47/F48 as the *abstract Rokhlin natural extension (OPEN as an explicit model)*. This paper concretizes it, and then makes an honest determination about where the reduction ends.  
The obstruction is explicit: the i-tetration transfer operator is a **contraction with complex spectrum** {**λ**^a **λ̄**^b} (arg **λ** \= 129.4°, |**λ**| \= 0.8915 \< 1), hence non-self-adjoint and non-unitary — it cannot itself be a modular flow, which is unitary. A unitary dilation is mandatory.  
The dilation is now explicit, not abstract. By the Sz.-Nagy–Foias theorem the scalar coherence contraction ×**λ** has a minimal unitary dilation: multiplication by e^{iφ} on L²(𝕋, μ\_**λ**), with μ\_**λ** the Poisson-kernel measure for **λ** — a genuine probability measure (density (1−|**λ**|²)/|1−**λ̄** e^{iφ}|² ≥ 0\) reproducing the power dilation ⟨1, U^n 1⟩ \= **λ**^n to machine precision (verified). The full channel's Stinespring dilation is the repeated-interaction meter chain (Attal–Pautrat): the isometry W|ψ⟩ \= K₀|ψ⟩|0⟩ \+ K₁|ψ⟩|1⟩ reproduces Φ\_deph on partial trace (verified). The same coupling each step makes it a stationary process whose past/future filtration is the candidate half-sided inclusion. This replaces the abstract Rokhlin extension with an explicit, constructible object.  
**Result Q18.8 (Modular realization, concretized; v1.4 corrected).** The abstract Rokhlin natural extension is concretized as the Sz.-Nagy–Foias / Stinespring unitary dilation of the dephasing contraction — the repeated-interaction meter chain (DERIVED). The unitary dilation exists (IMPORTED-PROVEN); its realization as the required Tomita–Takesaki modular flow of a von Neumann algebra with a faithful state remains OPEN (that is the CRT-4/H-CLK content). The co-orientation sign is DERIVED (§4.4); the construction is RH-free (§4.6). CORRECTION (per external review): the v1.3 reading "Type III₁ expected from the ΔS \= ln 2 entropy production" is RETRACTED. Entropy production does not determine factor type, and ZS-M47 v2.0 shows the local algebra M₃ ⊕ ℂ ⊕ M₅ is not even a factor (its centre is 3-dimensional; the block-tracial state is a trace). The correct object is the Parent-Factor Realization Problem (ZS-M47), and the single remaining physical gate is the exact clock equality CRT-4 / H-CLK (ZS-M46/F38), not a factor-type guess.  
**The terminus (honest determination), corrected.** Six deep-exploration cycles reduced the record-gate residual along a single chain — Z \= ∂X → the co-orientation half → the inclusion source → the self-adjoint/Fock realization → the modular type of one explicit dilation — and the sixth cycle, prompted by external review, corrected where that chain over-reached. The residual is NOT a factor-type guess about the qubit meter chain (that route is closed: ZS-M47 shows the relevant local algebra is not a factor). It is, precisely, the single corpus-wide gate that ZS-M46/M47/F38 already name.

## **4.8 The residual as a clock equality (ZS-M46/M47/F38) — and the novel bridge**

ZS-M46 v1.5 proves (Theorem M46.3A) that in the additive Koenigs coordinate the i-tetration seam is the translation w ↦ w \+ log **λ**, and on the canonical Abel cover u \= Log χ / Log **λ** it is the **unit translation u ↦ u \+ 1** — the generator U(1) of the (ax+b) group. The positive-energy standard pair and the Fock HSMI are then the Borchers completion (D \= ½ \+ p∂\_p, P \= p ≥ 0, \[D, P\] \= P, Δ^{it}U(a)Δ^{−it} \= U(e^{−2πt}a); verified), with μ/2π \= h\_K \= 0.0182765 read as the elliptic modulus height (not a modular time). The Q18 measurement layer contributes exactly one thing to this picture: its decoherence clock is the *same* germ contraction μ \= −ln|**λ**| \= 0.1148. The record gate therefore closes *iff* the QND measurement-record clock coincides with this modular seam clock — precisely the CRT-4 / H-CLK exact clock equality that ZS-M46 (CRT-4), ZS-M47, and ZS-F38 (H-CLK) already carry as the corpus's single remaining physical gate.  
**Category correction (v1.6).** The record algebra R\_record (the meter readout) is an abelian MASA, so it cannot itself carry a non-trivial Tomita–Takesaki modular flow. The clock lives on the noncommutative parent algebra M\_parent ⊃ R\_record ⊃ R\_past (system \+ unmeasured meter chain), and the measurement-record shift is the *induced action* of the parent modular flow on the record MASA. So the precise statement is: the modular flow acts on M\_parent, and its restriction/conditional-expectation onto R\_record is the record shift. The earlier phrase “record clock \= modular clock” is read in this refined sense.  
**Result Q18.9 (Residual \= clock equality; the novel bridge).** Q18's record-gate residual is not new: it is the corpus-wide CRT-4 / H-CLK clock-equality gate (ZS-M46/M47/F38), reached here from the measurement side. Stated precisely, the closing requirement is an intertwiner W with W A\_past W† \= N, W A\_full W† \= M, and the clock equality W U\_Q18(1) W† \= U\_M46(1) — the identification of the QND repeated-interaction output with the ZS-M46 positive-energy standard pair. This identification of a quantum measurement instrument's record clock with an algebraic-QFT modular (seam) clock, through the Koenigs germ of a holomorphic map, is the paper's genuinely novel external contribution — a bridge between quantum-measurement theory, complex dynamics, and Borchers–Wiesbrock modular theory. It is HYPOTHESIS-strong and OPEN (the clock equality is unproven), RH-free, and shared corpus-wide; it does not duplicate the ZS-M46 residual but re-derives it from measurement.  
**Progress (v1.5): an explicit candidate intertwiner.** The clock equality W U\_Q18(1) W† \= U\_M46(1) now has a concrete candidate. In the Sz.-Nagy–Foias functional model, the scalar coherence contraction ×**λ** has characteristic function the **degree-1 Blaschke factor** Θ\_λ(z) \= (**λ** − z)/(1 − **λ̄**z), which is inner (|Θ\_λ| \= 1 on 𝕋, verified) with exactly one zero (winding number 1). A degree-1 inner function carries *unit multiplicity* — one meter quantum per step — which is exactly the ZS-M46 unit translation u ↦ u \+ 1; and the generator scale is the same μ \= 0.1148 (§6). The functional-model unitary (composed with the Cayley transform to H²(ℂ₊)) is therefore an explicit candidate for W, matching both the clock quantum and the generator. What remains OPEN is only the exact CRT-4 operator normalization on the full record algebra (the scalar coherence match does not by itself certify the full channel).  
**Result Q18.11 (Clock-equality candidate, partial).** The Sz.-Nagy characteristic function of the coherence contraction is a degree-1 Blaschke factor; its unit multiplicity matches the ZS-M46 unit translation and its generator matches μ. This is a ONE-PARTICLE candidate only: it fixes a candidate W₁ : K\_Θ → K\_M46 at the single-particle level, but the CRT-4 clock equality requires the second quantization W \= Γ(W₁) to satisfy W M\_Q18 W† \= M, W N\_Q18 W† \= N, and the cocycle/weight conditions (CRT-4a central-phase, CRT-4b weight-preservation). Degree-1 winding certifies neither the algebra map nor the state preservation. The honest status is therefore OPEN-with-one-particle-candidate, to be tested against the ZS-F38/F39 finite ε\_clk residual protocol (not a new criterion).

# 

# **§5. The Born Rule and the Martingale**

## **5.1 The σz stochastic master equation**

The informative unraveling is the continuous weak measurement of σz (Wiseman–Milburn; Barchielli–Gregoratti). Writing p \= ρ₁₁, the posterior population obeys the driftless stochastic master equation  
*dp \= 2 √γ · p (1 − p) dW ,   E\[dW\] \= 0\.*  
**Normalization.** For the numerical representative we set γ \= μ \= −ln|**λ**| \= 0.1148; the Born-martingale theorem below holds for any γ \> 0 and is independent of this normalization. Whether the collapse rate equals μ exactly is the separate (unclaimed) question of §6.

## **5.2 The four-line derivation**

(1) p\_t ∈ \[0,1\] is bounded and drift-free ⇒ p\_t is a martingale, E\[p\_t\] \= p₀.  
(2) Doob's martingale convergence theorem ⇒ p\_t → p∞ almost surely.  
(3) The diffusion coefficient 2√γ · p(1−p) vanishes only at p ∈ {0,1} ⇒ p∞ ∈ {0,1} a.s. (purification).  
(4) E\[p∞\] \= p₀ and p∞ ∈ {0,1} ⇒ P(p∞ \= 1\) \= p₀.  This is the Born rule.

## **5.3 Rigorous import through the Z-Spin dictionary**

The heuristic four lines are made rigorous by three imported theorems, re-read on the geometric channel: Bauer–Bernard (2011) proves that repeated indirect QND measurements converge to wave-function collapse with Born statistics, relating the convergence rate to the relative entropy of each measurement (which the corpus caps at ln 2, ZS-Q7); Bauer–Benoist–Bernard (2013) supplies the discrete-to-continuous bridge; Benoist–Pellegrini (2014) gives exponential almost-sure purification and the estimation-stability that localizes Q16's strong residual as non-epistemic; Adler–Brody–Brun–Hughston (2001) casts state reduction (including the Lüders form) in explicit martingale language. Because the promotion route is a theorem rather than a numerical coincidence, no anti-numerology Monte-Carlo is required for gates (i)–(iii) — matching the Q16 v2.5 discipline.

## **5.4 Numerical verification**

Table 5.1. Born rule from the σz SME (γ \= μ, 4000 trajectories/point).

| initial p₀ | P(|1⟩) simulated | Born target | mean p(1−p) |
| ----- | ----- | ----- | ----- |
| 0.20 | 0.192 | 0.20 | 0.0011 |
| 0.35 | 0.355 | 0.35 | 0.0006 |
| 0.50 | 0.494 | 0.50 | 0.0008 |
| 0.65 | 0.655 | 0.65 | 0.0009 |
| 0.80 | 0.798 | 0.80 | 0.0010 |

The Born gate (P(|1⟩) \= p₀, |err| \< 0.03) and the purification (mean p(1−p) → 0\) both pass; the martingale gate E\[dp\] \= 0 at p \= 0.5 passes (9×10⁻⁵). Probability and Born-martingale gates: DERIVED.

# **§6. The Collapse Rate and the Single Constant |λ|**

The ensemble decoherence rate is exact and PROVEN: iterating Φ\_deph multiplies |ρ₁₀| by |**λ**| per Z-cycle, so the off-diagonal decays as e^{−μn} with μ \= −ln|**λ**| \= 0.1148 (verified: fitted rate 0.11483). The *collapse (purification) rate* of the informative unraveling is instead the measurement's relative entropy S(P⁰ ‖ P¹), bounded by the ln 2 \= 0.693 capacity ceiling (ZS-Q7, Holevo × rank-2). These are *distinct* quantities — one is loss of ensemble coherence, the other is per-trajectory information gain.  
They are nonetheless governed by the same constant under one condition. For a QND measurement the conditional purification rate equals the ensemble decoherence rate times the monitoring efficiency η. The Z-channel observes *all* cross-sector information under complete monitoring of the minimal Stinespring output (L\_XY ≡ 0 and rank-2 being necessary but not sufficient), η \= 1, so the collapse timescale is set by the same |**λ**| that governs the transfer spectrum. This upgrades the seed report's "one constant, both layers" claim from HYPOTHESIS to:  
**Result Q18.4 (Rate, DERIVED-CONDITIONAL).** Under complete Z-output monitoring (η \= 1\) — the assumption that the physical Z-environment is the minimal Stinespring dilation, strictly stronger than L\_XY ≡ 0 — the collapse and ensemble-decoherence layers share the single constant |λ|. The exact numerical equality collapse-rate \= μ is NOT asserted (it depends on informativeness saturation) and is left as a pre-registered anti-numerology gate.

# 

# **§7. Strong Sufficiency and the Anti-Numerology Gate**

## **7.1 Strong sufficiency stays OPEN, but is non-epistemic on this channel**

Weak sufficiency (almost-sure collapse to one σz eigenstate with Born frequencies) is delivered by §§4–5. Strong sufficiency — the eliminability of the per-run randomness — is not, and following ZS-Q16 v2.5 it remains OPEN. What can be shown is that the residual is *non-epistemic*: the per-run outcome is a functional of the measurement record, not of the observer's prior. Using the Benoist–Pellegrini estimation-stability construction, two observers who process the *same* record with opposite priors (p₁ \= 0.2 vs. 0.8) agree on the inferred outcome in 3000/3000 records, and each recovers the true pointer in 3000/3000. No refinement of state knowledge alters the outcome; the irreducible randomness is localized at the binary innovation of the dim Z \= 2 seam. Strong sufficiency: OPEN, non-epistemic (confirmed on the Q18 dephasing channel).

## **7.2 The anti-numerology gate F-Q18.6 (EXECUTED)**

The only place ZS-Q18 could hide a coincidence is the claim that the observed collapse statistics are specifically the Born rule P(|1⟩) \= p₀. This was pre-registered as a model-selection test: over a randomized grid of ten (p₀, γ) configurations, the simulated frequency (purified subset) must fit Born and reject the alternatives P \= p₀², a normalized square-root rule, and the uniform P \= 0.5.  
Table 7.1. Anti-numerology model selection (10 random (p₀, γ) configurations).

| Candidate rule | χ²/dof | Verdict |
| :---- | ----- | :---- |
| Born  P \= p₀ | 0.68 | CONSISTENT |
| square  P \= p₀² | 1054 | REJECTED |
| square-root rule | 238 | REJECTED |
| uniform  P \= 0.5 | 1286 | REJECTED |

Only Born survives. As a coincidence p-value, random monotone power-rules P \= p₀^k (k \~ U\[0.3, 3\]) fit as well as Born in just 2.2% of draws, and Born is the unique k \= 1 rule forced by the driftless-martingale identity of §5.2 — not a tunable number. F-Q18.6: EXECUTED, PASS. The Born result therefore carries no numerology; it is theorem-driven and parameter-free.

## **7.3 Strong sufficiency, decomposed: the seam-phase deterministic dilation**

Strong sufficiency (the eliminability of per-run randomness) splits into three levels: SS-1 pathwise determinism (a complete micro-state fixes the future record), SS-2 no external innovations (no fresh dW\_n added per step), and SS-3 single-world selection (why this one path is actualized). SS-1/SS-2 are addressable; SS-3 coincides with the single-world NON-CLAIM. A concrete candidate closes SS-1/SS-2: introduce a seam-phase coordinate ξ ∈ \[0,1) with Haar measure (read as the microscopic Z-seam phase, not an external random number), set the outcome r(x,ξ) \= \+ iff ξ \< q₊(p), and define the deterministic skew product  
*T(p,w,ξ) \= ( F₊(p,w), ξ/q₊ )  if ξ \< q₊,   ( F₋(p,w), (ξ−q₊)/q₋ )  if ξ ≥ q₋.*  
This map adds no fresh randomness: given (p₀, w₀, ξ₀) the entire record is determined (SS-1, SS-2). If ξ₀ is Haar-uniform the record statistics reproduce q\_± exactly (Born), the state coordinate purifies (vertical contraction), and the ξ coordinate expands at rate 1/q\_r \> 1 (horizontal expansion) — the F47 vertical-contraction / horizontal-expansion picture realized as one deterministic skew product. Verified: mean outcome frequency 0.50 at p₀ \= 0.5, purification \> 0.9.  
**Result Q18.13 (Seam-phase dilation; strong sufficiency partial).** The seam-phase skew product T gives, from initial (p₀, w₀, ξ₀): pathwise determinism (PROVEN) and no per-step fresh noise (PROVEN); under Haar initialization it reproduces finite-record QND cylinder statistics (DERIVED, by induction on record length). Invariance of the Haar × state measure and the generating-partition property remain OPEN; the Z-Spin origin of ξ, contextuality beyond σz, and single-world actualization are OPEN/NON-CLAIM. Precise status: the OPERATIONAL deterministic representation is DERIVED-CONDITIONAL on the ontic seam-phase hypothesis and Haar initialization, while Z-Spin STRONG SUFFICIENCY as a whole remains OPEN — it is not claimed closed.

# 

# **§8. Verification: Evidence Tiers**

The companion suite reports 95/95 PASS, but a flat count would overstate the evidence: an exact algebraic identity, a finite Monte-Carlo estimate, an imported theorem, a conditional assumption, and a falsification guard are not the same kind of evidence. Following the F48 discipline (and the external-review recommendation), the checks are reported in tiers. A ‘PASS’ in the GUARD/FALSIFIER and CONDITIONAL tiers means ‘the guard did not trip / the assumption is stated’, not ‘the physics is proved’.  
Table 8.1. Verification evidence tiers. A PASS certifies only at its own tier.

| Tier | Representative checks (what a PASS certifies) |
| :---- | :---- |
| EXACT / SYMBOLIC | CPTP, Choi PSD, Kraus completeness, diagonal-Kraus QND, Koenigs |λ| contraction, \[D,P\] \= P, Sz.-Nagy moments ⟨1,U^n1⟩ \= λ^n, α\_BK \= −ln|z\*|, centre-dim \= 3; λ-locked instrument completeness; off-diagonal multiplier \= λ; Θ\_λ degree-1 inner (winding 1). — genuine proofs/identities. |
| NUMERICAL | Born trajectories P(|1⟩) \= p₀, purification, estimation stability 3000/3000, anti-numerology model selection χ²/dof; full-state record-wise identity Φ\_r(E\_full)=E\_full(F\_r) over 2×10⁵ Bloch states (residual \< 10⁻¹²); seam-phase Born reproduction. — high-confidence numerical/near-exact evidence. |
| IMPORTED-THEOREM | QND purification and Born statistics (Bauer–Bernard; Benoist–Pellegrini; Maassen–Kümmerer), martingale reduction (Adler et al.), Sz.-Nagy–Foias dilation, Stinespring, Borchers 2π. — used, not re-proved. |
| CONDITIONAL | η \= 1 (complete Z-output monitoring); the informative-unraveling selector χ\_Z \= −1. — hold modulo a named, falsifiable condition. |
| GUARD / FALSIFIER | trivial modular operator under the selected faithful state, or no record-shift-compatible HSMI ⇒ reject (F-Q18.7b); the CRT-4/H-CLK clock equality pending. — a PASS means the guard has not tripped. |
| OPEN | the physical instrument selector; the complete-monitoring condition; the CRT-4/H-CLK parent-algebra clock-equality normalization (one-particle candidate only); the global Koenigs-fibre lift domain; and the strong-sufficiency SS-5–SS-7 frontier. The record-wise State/Probability/Born-martingale identities are PROVEN (Theorem Q18.12) and are NOT listed here. |

With this tiering, the honest reading of ‘95/95 PASS’ is: every exact identity and numerical test passed, every imported theorem is correctly invoked, and no falsification guard tripped — the record-wise State, Probability, and Born-martingale identities are PROVEN (Theorem Q18.12), while the physical instrument selector, the complete-monitoring condition, and the CRT-4/H-CLK parent-algebra clock equality remain OPEN. The count certifies the mathematics that is done, not the physical selection and modular-clock realization that are still open.

# **§9. Cross-Version Consistency and Observational Compatibility**

Version-conflict audit (§3.2). The load-bearing constants are used exactly as upstream: |**λ**| \= (π/2)|z\*| (ZS-U12.1 Multiplier-Selection Theorem), |**λ**|² \= (π²/4)|z\*|² \= 0.7948 (ZS-M1 Leaky Wilson Loop, matching ZS-F0/F11/U12), leak 0.2052 (ZS-M43), Born weight w\_Y \= dim(Y)/Q \= 6/11 (ZS-Q7), capacity ceiling ln 2 (ZS-Q7) — all reproduced to machine precision (CAT A, 10/10). No downstream result (ZS-S1 sin²θ\_W, ZS-U1/U12 inflationary transfer) is disturbed, because ZS-Q18 consumes these constants without re-fitting them.  
Physics compatibility (§3.3). The construction reproduces standard continuous-measurement quantum theory (the σz SME and its martingale/Born content are textbook), so it cannot conflict with laboratory quantum mechanics; it adds only the geometric origin of the rate μ and the pointer basis. It touches neither the Planck-2018 ΛCDM fit nor Standard-Model couplings, which live in the X- and Y-sectors; the Z-sector measurement layer is orthogonal to them.

# **§10. Falsification Gates**

Table 10.1. ZS-Q18 falsification gates (multi-layer: math / simulation / observation).

| Gate | Layer | Falsification condition | Status |
| :---- | :---- | :---- | :---- |
| F-Q18.1 | Math / immediate | Φ\_deph not CPTP, or Choi has a negative eigenvalue \> tol, or Kraus non-diagonal (not QND). | PASS |
| F-Q18.2 | Math / theorem | A purifying QND unraveling exists that does NOT give P(|j⟩)=ρ\_jj(0) (would break Theorem Q18.2). | PASS |
| F-Q18.3 | Simulation | SME Born frequency deviates from p₀ by \> 3σ over the 5-point grid, or trajectories fail to purify. | PASS |
| F-Q18.4 | Consistency | {I,Z} unraveling purifies (would contradict Maassen–Kümmerer dark-subspace exclusion). | PASS |
| F-Q18.5 | Corpus / conditional | χZ \= \+1 established ⇒ record gate falsified; or the i-tetration detector is shown NOT to admit a self-adjoint/Fock modular realization ⇒ Result Q18.7 retracts. (Independent of RH.) | OPEN (self-adj/Fock realization) |
| F-Q18.6 | Anti-numerology | Pre-registered: collapse statistics must fit Born and reject alternatives; random-rule coincidence \< 5%. | EXECUTED — PASS (§7) |
| F-Q18.7b | Operator-algebra | The candidate parent algebra has trivial modular operator under the physically selected faithful state, or admits no standard half-sided modular inclusion compatible with the record shift ⇒ record gate falsified. (Falsification is on modular data \+ HSMI, not on factor type.) | OPEN |
| F-Q18.8 | Strong sufficiency | If T does not preserve the Haar × state measure, or the binary record is not a generating partition ⇒ the operational representation fails (Result Q18.13 retracts). Pathwise determinism and no-fresh-noise are PROVEN; invariant-measure and generating-partition are OPEN. | OPEN |

# 

# **§11. Conclusion**

Table 11.1. Final status of the F48 four gates (plus the rate bonus).

| Gate | Before (F48) | ZS-Q18 v1.6 (audited) |
| :---- | :---- | :---- |
| State — mean channel | OPEN | PROVEN — Φ\_deph CPTP, Koenigs-exact, diagonal Kraus (QND) |
| State — F48 record-wise | OPEN | PROVEN (full-state) — Theorem Q18.12, E\_full(p,w), λ-locked instrument; residual \< 10⁻¹² over 2×10⁵ states |
| Probability | OPEN | DERIVED (mean) \+ PROVEN record-wise — q₊ \+ q₋ \= 1 (Theorem Q18.12) |
| Born-martingale | OPEN | DERIVED \+ PROVEN record-wise — q₊p₊ \+ q₋p₋ \= p (Theorem Q18.12) |
| Record | OPEN | DERIVED-CONDITIONAL — co-orientation DERIVED (A17 Thm E); source generator PROVEN (i-tetration detector, ZS-M4); dilation explicit (Sz.-Nagy/Stinespring); residual \= the CRT-4/H-CLK clock equality (ZS-M46/M47/F38); now OPEN-with-candidate — the Sz.-Nagy degree-1 Blaschke intertwiner matches the M46 unit translation, leaving only the exact operator normalization (§4.8) |
| Rate (bonus) | HYPOTHESIS | DERIVED-CONDITIONAL — η \= 1 on complete Z-output monitoring (minimal Stinespring), stronger than L\_XY ≡ 0 |

The honest scorecard is: two gates (Probability, Born-martingale) are DERIVED; the F48 record-wise State, Probability, and Born-martingale gates now close EXACTLY on the full-state embedding (Theorem Q18.12), so the State gate is record-wise closed at the full-state level (the mean-state representative was already PROVEN); and one gate — the Record gate — is DERIVED-CONDITIONAL, its remaining residual being the CRT-4/H-CLK parent-algebra clock equality (with a one-particle Blaschke candidate). The remaining OPENs are genuinely distinct (full-state selector, complete monitoring, clock equality, strong sufficiency) and are not collapsed into a single bedrock. Together with F48's proved lemmas this gives, for the first time, an end-to-end deterministic-plus-stochastic account from the i-tetration action to a Born-distributed σz measurement, with the collapse timescale set by the same |**λ**| that governs the transfer spectrum. The single structural correction — reading the Koenigs representative as the dephasing (QND) channel rather than amplitude damping — is what converts F48's mean-channel result into a genuine derivation of the Born rule. Strong sufficiency and the single-world question are deliberately left as OPEN (non-epistemic) and NON-CLAIM.

## **Novelty and external contribution**

Independently of the Z-Spin interpretation, this paper provides two structural constructions and one theorem-based integration relevant to quantum measurement. (i) A *Koenigs–Belavkin skew-product construction*: the record-wise QND instrument is exhibited as a Koenigs-type linearization carrying a holomorphic multiplier **λ**, coupling the Koenigs coordinate w \= φ(z) of a holomorphic germ to the Belavkin a-posteriori (filtered) state through the branch maps F\_r. (ii) A *minimal full-state carrier result within the stated embedding class* (Theorem Q18.12): among positive, normalization-covariant density-coordinate embeddings, an informative QND σz instrument cannot act on the one-complex-dimensional coherence manifold, and the carrier that supports it adds exactly one real (population) coordinate. We state this as a result within that embedding class, not as a categorical minimality/uniqueness theorem (the minimality category, the admissible manifold class, and uniqueness-up-to-isomorphism are left to a dedicated treatment). (iii) The *imported QND Born theorem* (Bauer–Bernard and related), applied to the λ-locked channel: unraveling-independence of the Born probability for a σz-QND channel is a standard result used here, not a new theorem. The domain-limited lift (density-coordinate PROVEN; global fibre lift Koenigs-chart-conditional) is stated precisely so the results are usable as-is.  
**Stopping rule (final release).** ZS-Q18 is frozen once the document, the code output, and the four-gate ledger agree on the status of Theorem Q18.12 — which they now do (v1.7). The CRT-4/H-CLK parent-algebra clock equality, the Parent-Factor Realization Problem, the action-level derivation of complete monitoring, the uniqueness of the instrument selector, the Z-Spin origin of the seam phase, contextual extension to non-commuting settings, and single-world actualization are *out of scope* for ZS-Q18; they are separate corpus-wide gates (ZS-M46/M47/F38/F39, ZS-Q14, ZS-Q16) and shall not trigger a further ZS-Q18 revision. Q18 is the full-state QND-instrument and record-wise Born-martingale layer; the physical selection and modular-clock realization are transferred to those gates.

# **Acknowledgements & Code Availability**

Consolidated from internal Z-Spin Collaboration notes following ZS-F48 v1.6 and the F48 seed report, and advanced by the deep-exploration cycle recorded in Appendix C. The companion script zs\_q18\_verify\_v1\_7.py performs 95 computational checks (reported in evidence tiers, §8) across fourteen categories — locked-constant and cross-version audit; the CPTP/Koenigs/diagonal-Kraus state gate; the informative/non-informative unraveling diagnostic with the Maassen–Kümmerer dark-subspace exclusion; the σz-SME Born rule and martingale; the unraveling-independence theorem across three distinct QND unravelings; the efficiency-1 rate analysis; the Benoist–Pellegrini estimation-stability test; the anti-numerology model-selection gate; and the ZS-A17 residual decomposition (spinor sign, process-level witness, Theorem E co-orientation, Theorem F metric no-go); and the ZS-M4 Berry–Keating inclusion-source identification (α\_BK identity, ax+b algebra, Borchers positivity, detector/locator split); and the modular-realization concretization (contraction obstruction, Sz.-Nagy–Foias Poisson dilation, Stinespring channel dilation, and the honest Type III/half-sided terminus); and the external-review precision corrections with the ZS-M46/M47/F38 clock reformulation. 95/95 PASS, reported in evidence tiers rather than as a single flat count. It imports only the locked constants; zero fitted parameters. (A, Q, dim Z) \= (35/437, 11, 2), z\*, λ₁ LOCKED.

# **Appendix A — CPTP Proof and the Diagonal-Kraus Decomposition**

Complete positivity is equivalent to positivity of the Choi matrix C \= Σ\_{ij} |i⟩⟨j| ⊗ Φ\_deph(|i⟩⟨j|). Evaluating the four blocks gives a Hermitian C with eigenvalues {1, 1, (1+|**λ**|)/2 ± …} all ≥ 0 (minimum −1.2×10⁻³¹, machine zero), so Φ\_deph is completely positive; the partial trace over the output equals I, so it is trace-preserving. For the Kraus form, write **λ** \= |**λ**| e^{iθ}. A real dephasing D\_{|λ|} has Kraus {√((1+|**λ**|)/2) I, √((1−|**λ**|)/2) Z}; composing with the phase gate P \= diag(1, e^{−iθ}) sends ρ₀₁ ↦ |**λ**| e^{iθ} ρ₀₁ \= **λ** ρ₀₁, giving K₀ \= √((1+|**λ**|)/2) P and K₁ \= √((1−|**λ**|)/2) P Z. Both are diagonal, so \[K\_i, σz\] \= 0 and the instrument is QND; K₀†K₀ \+ K₁†K₁ \= I; and the Kraus sum reproduces Φ\_deph to 8×10⁻¹⁷.

# **Appendix B — The Q18 Four-Gate Ledger**

| Gate | Requirement (F48 App. G) | Discharge in ZS-Q18 |
| :---- | :---- | :---- |
| State | E(f\_r(z)) \= Φ\_r(E(z)) | mean-state PROVEN (Thm Q18.1); record-wise PROVEN on full-state E\_full(p,w) (Thm Q18.12, λ-locked instrument). |
| Probability | p\_r(z) \= Tr I\_r(E(z)) | σz-SME \+ Thm Q18.2 (unraveling-independent Born); §4–5. DERIVED. |
| Record | filtration/innovation \= Q16 | informative unraveling selected by χZ \= −1 \+ no-dark-subspace; §4.4. DERIVED-COND. |
| Born-martingale | E\[p(n+1)|F\_n\] \= p(n) | driftless SME ⇒ martingale; §5.2(1). DERIVED. |

# 

# **Appendix C — Deep-Exploration Record (condensed)**

The paper consolidates eight deep-exploration cycles; the full per-cycle notes are archived, and only the load-bearing outcomes are kept here. Cycles 1–2 fixed the dephasing representative and executed the anti-numerology and estimation-stability tests. Cycle 3 (ZS-A17) reduced the record-gate residual to the co-orientation half (metric half a NO-GO). Cycle 4 (ZS-M4) identified the inclusion-source generator with the i-tetration Archimedean-scaling detector (α\_BK), de-risking from RH. Cycle 5 concretized the Rokhlin natural extension as the Sz.-Nagy–Foias / Stinespring dilation. Cycle 6 (external review) corrected over-tagged statuses (record-wise State PARTIAL/OPEN, η \= 1 conditional, Type III₁ retracted) and reformulated the residual as the CRT-4/H-CLK clock equality. Cycle 7 built the coherence-level branches and the degree-1-Blaschke clock candidate.  
**Cycle 8 (full-state closure).** Prompted by the second external review, the λ-locked canonical instrument (δ \= √(1−|λ|²)) was introduced (removing arbitrary witness constants), and the minimal full-state embedding E\_full(p,w) was shown to close the record-wise State, Probability, and Born-martingale gates exactly (Theorem Q18.12; residual \< 10⁻¹² over 2×10⁵ Bloch-ball states), with the F48 one-dimensional manifold’s failure proven rather than observed. The seam-phase deterministic skew product (Result Q18.13) closes SS-1–4 of strong sufficiency conditionally. The clock equality was category-corrected (modular flow on the parent algebra; record shift induced on the abelian MASA) and the Blaschke candidate downgraded to a one-particle candidate. CAT M/N: exact/numerical PASS; no prior exact result reversed.  
**Method (Steps 0–5), retained in brief.** Each cycle ran the MECE issue-tree protocol (long list → issue list → dependency tree → epistemic-status traversal → convergence check → scoring against prior corpus). Convergence was declared only when re-scans changed no node status; over-reaches were retracted rather than carried, and residuals were named as concrete objects, not diffuse gaps.

# 

# **References**

\[1\] K. Kang, ZS-F48 v1.6: The Local Skew Normal Form and the Global Transfer Programme — Appendix G, the four Q16 gates (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F47 v1.6: The Expansion–Contraction Complementarity Principle (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-M1 v1.0: i-Tetration and the Fixed Point z\* (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M46: Koenigs Linearization of the i-Tetration Fibre Map (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M43 v1.4: reduced rates; leak 1 − |λ|² \= 0.205 (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-Q1: Quantum Geometric Decoherence — the Z-Bottleneck σz Dephasing CPTP Channel (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-Q7: The Z-Bottleneck — rank ≤ 2, capacity ≤ ln 2, p\_eq \= (3,2,6)/11 (Z-Spin Cosmology, 2026).  
\[8\] K. Kang, ZS-Q12: Self-Referential (Belavkin) Measurement Closure Q12.A (Z-Spin Cosmology, 2026).  
\[9\] K. Kang, ZS-Q14: Boundary Spin-Lift, χZ \= −1 (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-Q16 v2.5: Single-Outcome Selection — weak sufficiency DERIVED-CONDITIONAL; strong OPEN; single-world NON-CLAIM (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-F0 v1.0(Revised): Ontological Bootstrap — §12.3 retain/leak sum rule (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, ZS-F1: the vanishing X–Y block L\_XY ≡ 0 (Z-Spin Cosmology, 2026).  
\[13\] M. Bauer and D. Bernard, Convergence of repeated quantum non-demolition measurements and wave-function collapse, Phys. Rev. A 84, 044103 (2011); arXiv:1106.4953.  
\[14\] M. Bauer, T. Benoist, and D. Bernard, Repeated Quantum Non-Demolition Measurements: Convergence and Continuous Time Limit, Ann. Henri Poincaré 14, 639–679 (2013).  
\[15\] S. L. Adler, D. C. Brody, T. A. Brun, and L. P. Hughston, Martingale models for quantum state reduction, J. Phys. A: Math. Gen. 34, 8795–8820 (2001).  
\[16\] H. Maassen and B. Kümmerer, Purification of quantum trajectories, IMS Lecture Notes Monogr. Ser. 48, 252–261 (2006); B. Kümmerer and H. Maassen, A pathwise ergodic theorem for quantum trajectories, J. Phys. A 37, 11889–11896 (2004).  
\[17\] T. Benoist and C. Pellegrini, Large time behaviour and convergence for quantum trajectories, Comm. Math. Phys. 331, 703–723 (2014).  
\[18\] H. M. Wiseman and G. J. Milburn, Quantum Measurement and Control (Cambridge University Press, 2010).  
\[19\] A. Barchielli and M. Gregoratti, Quantum Trajectories and Measurements in Continuous Time, Lect. Notes Phys. 782 (Springer, 2009).  
\[20\] N. Gisin, Quantum measurements and stochastic processes, Phys. Rev. Lett. 52, 1657 (1984).  
\[21\] G. Königs, Recherches sur les intégrales de certaines équations fonctionnelles, Ann. Sci. ÉNS 1, 3–41 (1884).  
\[22\] K. Kang, ZS-A17 v1.5: Macro-Holonomy and Spin-Structure Selection — the curvature–spin–metric trichotomy; Theorem E (co-orientation from record flow), Theorem F (Spin–Metric No-Go); Z \= ∂X decomposition (Z-Spin Cosmology, 2026).  
\[23\] K. Kang, ZS-M3: j \= 1/2 and the spinor lift, D^{1/2}(2π) \= −I (Z-Spin Cosmology, 2026).  
\[24\] K. Kang, ZS-F19: the record-flow orientation ΔK\_Ω \= −ln 2 (Z-Spin Cosmology, 2026).  
\[25\] K. Kang, ZS-Q12V: the bedrock postulate Z \= ∂X (Z-Spin Cosmology, 2026).  
\[26\] H.-J. Borchers, The CPT-theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143, 315 (1992).  
\[27\] H.-W. Wiesbrock, Half-sided modular inclusions of von Neumann algebras, Commun. Math. Phys. 157, 83 (1993); Erratum 184, 683 (1997).  
\[28\] A. Connes, On the spectral characterization of manifolds, J. Noncommut. Geom. 7, 1 (2013).  
\[29\] M. Takesaki, Tomita's Theory of Modular Hilbert Algebras and Its Applications, Lecture Notes in Math. 128 (Springer, 1970).  
\[30\] K. Kang, ZS-M4: the i-Tetration Transfer Operator and the Berry–Keating Correspondence — Theorem 3 (Dilation \= Boost, α\_BK \= −ln|z\*|), Theorem 4 (J-intertwining at σ \= 1/2) (Z-Spin Cosmology, 2026).  
\[31\] K. Kang, ZS-QS: the Detector–Locator Dichotomy of the Z-Spin RH Bridge (Z-Spin Cosmology, 2026).  
\[32\] K. Kang, ZS-F24 v2.0: the Archimedean-Scaling Identification with the Connes–Consani–Moscovici Program (Z-Spin Cosmology, 2026).  
\[33\] M. V. Berry and J. P. Keating, H \= xp and the Riemann zeros, in Supersymmetry and Trace Formulae, eds. Lerner et al. (Kluwer, 1999), pp. 355–367; The Riemann zeros and eigenvalue asymptotics, SIAM Rev. 41, 236 (1999).  
\[34\] A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5, 29 (1999).  
\[35\] A. Connes, C. Consani, and H. Moscovici, prolate-wave / adelic-Sonin scaling program (2024).  
\[36\] B. Sz.-Nagy, C. Foias, H. Bercovici, and L. Kérchy, Harmonic Analysis of Operators on Hilbert Space, 2nd ed. (Springer, 2010\) — minimal unitary dilation of a contraction.  
\[37\] W. F. Stinespring, Positive functions on C\*-algebras, Proc. Amer. Math. Soc. 6, 211 (1955).  
\[38\] S. Attal and Y. Pautrat, From repeated to continuous quantum interactions, Ann. Henri Poincaré 7, 59 (2006).  
\[39\] H. Araki and E. J. Woods, Representations of the CCR describing a free Bose gas, J. Math. Phys. 4, 637 (1963) — quasi-free states and Type III factors.  
\[40\] J. J. Bisognano and E. H. Wichmann, On the duality condition for a Hermitian scalar field, J. Math. Phys. 16, 985 (1975) — modular theory of the wedge / half-line.  
\[41\] V. A. Rokhlin, Exact endomorphisms of a Lebesgue space, Izv. Akad. Nauk SSSR 25, 499 (1961) — natural extensions.  
\[42\] K. Kang, ZS-M46 v1.5: Koenigs Linearization and Half-Sided Modular Inclusions — the cover-level unit translation, positive-energy standard pair, Cocycle Realization Theorem; CRT-4 exact clock equality OPEN (Z-Spin Cosmology, 2026).  
\[43\] K. Kang, ZS-M47 v2.0: The Seam Modular-Depth Theorem — the Parent-Factor Realization Problem (Araki–Woods classification of M₃ ⊕ ℂ ⊕ M₅ RETRACTED: not a factor) (Z-Spin Cosmology, 2026).  
\[44\] K. Kang, ZS-F38: The Register Clock Identity (H-CLK) — the GKLS register clock as the modular seam clock (Z-Spin Cosmology, 2026).  
\[45\] R. Longo, Real Hilbert subspaces, modular theory, SL(2,ℝ) and CFT, in Von Neumann Algebras in Sibiu (Theta, 2008), pp. 33–91.  
\[46\] M. A. Rieffel and A. van Daele, A bounded operator approach to Tomita–Takesaki theory, Pacific J. Math. 69, 187 (1977).  
\[47\] A. Connes, Une classification des facteurs de type III, Ann. Sci. ÉNS 6, 133 (1973); U. Haagerup, Connes bicentralizer problem and uniqueness of the injective factor of type III₁, Acta Math. 158, 95 (1987).

# **Version History**

**v1.7 (July 2026, Final):** Final release: status synchronization after the third external review; no new theorems or explorations added (per the review’s stopping recommendation). Removes all remaining v1.5-era stale statuses that conflicted with Theorem Q18.12: the §8 evidence-tier OPEN list no longer names the record-wise intertwiner (now PROVEN); the abstract η \= 1 wording is corrected to “complete Z-output monitoring, stronger than L\_XY ≡ 0”; the §3.4 opening is reframed historically; §4.4 lists the distinct residuals rather than a single Z \= ∂X bedrock. Splits Theorem Q18.12 into the density-coordinate identity (PROVEN) and the global i-tetration-fibre lift (DERIVED-CONDITIONAL on Koenigs-chart domain). Sharpens the strong-sufficiency ledger (pathwise determinism and no-fresh-noise PROVEN; finite-cylinder statistics DERIVED; invariant-measure and generating-partition OPEN; operational representation DERIVED-CONDITIONAL, Z-Spin strong sufficiency OPEN). Adds a Novelty/external-contribution statement (operator-valued Koenigs–Belavkin skew product; minimal-extension theorem) and an explicit stopping rule. Vectorizes the CAT N verification block; adds the N6b lift-domain check. Corrected release (errata, same version): Result Q18.8 now reads “unitary dilation exists; realization as the modular flow OPEN” and drops the “Type I would falsify” line (falsification is on modular data/HSMI, F-Q18.7b); §6 states η \= 1 as complete-monitoring-conditional, not L\_XY ≡ 0; §5.1 marks γ \= μ as the representative normalization (Born holds for any γ \> 0); the Novelty section is lowered to two constructions plus one imported theorem within the stated embedding class; and the verifier’s CAT K/L/F2 labels and the N2/N3 full-matrix ∞-norm residual are synchronized. Verification 94/94 → 95/95 PASS (tiered).  
**v1.6 (July 2026):** Second external-review audit and closure (cycle 8). Introduces the λ-locked canonical informative instrument (δ \= √(1−|λ|²)), removing the earlier arbitrary witness constants. Proves Theorem Q18.12 (Minimal Full-State Koenigs–Belavkin Extension): on the Bloch-ball embedding E\_full(p,w) the record-wise State, Probability, and Born-martingale gates close EXACTLY (residual \< 10⁻¹² over 2×10⁵ states), with the F48 one-dimensional manifold’s non-preservation now a theorem. Distinguishes unnormalized coherence branches from normalized full-state branches. Adds the seam-phase deterministic dilation (Result Q18.13; strong sufficiency SS-1–4 conditional). Category-corrects the clock claim (modular flow on the parent algebra, record shift induced on the abelian MASA) and downgrades the Blaschke result to a one-particle candidate. Removes all residual Type III₁ wording and reformulates F-Q18.7b on modular data/HSMI (not factor type). Unifies the State-gate status throughout (mean-state PROVEN; record-wise PROVEN on full-state), fixes the conclusion column title and abstract duplication, lists the distinct residuals rather than collapsing them to Z \= ∂X, and condenses Appendix C. Adds CAT M (λ-locked) and CAT N (full-state \+ seam-phase). Verification 86/86 → 94/94 PASS (tiered).  
**v1.5 (July 2026):** Deep-exploration cycle 7 integrated (the next steps proposed at the close of v1.4), as honest partial progress on two gates. (b) Record-wise branches: an informative σz instrument yields conditional branch maps f\_r(w) \= c\_r w that split the mean multiplier (c₊ \+ c₋ \= λ), and a direct computation shows the F48 embedding E(w) cannot carry the informative population update — upgrading the record-wise State gate from PARTIAL/OPEN to coherence-level DERIVED \+ full-state DERIVED-CONDITIONAL, with the obstruction identified (§3.4, Result Q18.10). (a) Clock equality: the Sz.-Nagy characteristic function of ×λ is the degree-1 Blaschke factor, whose unit multiplicity matches the ZS-M46 unit translation and whose generator matches μ, giving an explicit candidate intertwiner — advancing CRT-4/H-CLK from bare OPEN to OPEN-with-candidate (§4.8, Result Q18.11). Neither gate is closed. Adds CAT M (10 checks). Verification 76/76 → 86/86 PASS (tiered).  
**v1.4 (July 2026):** External-review audit and precision correction (deep-exploration cycle 6); no speculative content added. Softens the subtitle from “Closing” to “Advancing” and the abstract’s central claim. Corrections: the F48 State gate is record-wise, so only the mean-channel intertwining is PROVEN and the record-wise gate is PARTIAL/OPEN (§3.4); η \= 1 is DERIVED-CONDITIONAL on complete Z-output monitoring, stronger than L\_XY ≡ 0 (§6); the v1.3 “Type III₁ from entropy production” reading is RETRACTED per ZS-M47 (the local algebra is not a factor). Reformulates the residual via ZS-M46/M47/F38 as the single CRT-4 / H-CLK clock-equality gate and states the novel measurement-clock ↔ modular-seam-clock bridge (§4.8, Result Q18.9). Adds an evidence-tier verification ledger (§8) and a λ vs λ₁ notation note. Adds CAT L (9 checks) and references to M46/M47/F38/Longo/Rieffel–van Daele/Connes–Haagerup. Verification 67/67 → 76/76 PASS (tiered).  
**v1.3 (July 2026):** Deep-exploration cycle 5 integrated, with explicit anti-hallucination discipline. Concretizes the record-gate modular realization: the i-tetration transfer operator is a contraction with complex spectrum (non-self-adjoint), so a unitary dilation is mandatory; the abstract Rokhlin natural extension is replaced by the explicit Sz.-Nagy–Foias Poisson-measure dilation (⟨1, U^n 1⟩ \= λ^n verified) and the Stinespring repeated-interaction chain. The single remaining OPEN — Type III₁ \+ half-sided of that dilation — is registered as the honest terminus of the five-cycle reduction chain (corpus-internal, RH-free; Type I would falsify, F-Q18.7b). Adds §4.7 and Result Q18.8, CAT K (9 checks), and references to Sz.-Nagy–Foias/Stinespring/Attal–Pautrat/Araki–Woods/Bisognano–Wichmann/Rokhlin. Verification 58/58 → 67/67 PASS.  
**v1.2 (July 2026):** Deep-exploration cycle 4 integrated. Names the record-gate inclusion source: ZS-M4 Theorem 3 (PROVEN) identifies the Berry–Keating dilation with the i-tetration Archimedean-scaling detector (α\_BK \= −ln|z\*| \= 0.5664, exact); the ax+b boost algebra closes, Borchers positivity holds, and |λ| \< 1 supplies the one-sided compression. The corpus detector/locator split de-risks the record gate to independence from the Riemann Hypothesis, narrowing the residual to the self-adjoint/Fock(Q \= 11\) modular realization (corpus-internal OPEN). Adds §4.6 and Result Q18.7, CAT J (13 checks), and references to M4/QS/F24/Berry–Keating/Connes/CCM. Verification 45/45 → 58/58 PASS.  
**v1.1 (July 2026):** Deep-exploration cycle 3 integrated. Decomposes the record-gate residual via ZS-A17 v1.5: χ\_Z \= −1 (spinor sign) and the process-level record ũ\_Z ≠ f(Λ) are shown DERIVED, the co-orientation is DERIVED (A17 Theorem E, Borchers–Wiesbrock), and the metric half of Z \= ∂X is a proven NO-GO not required by measurement — sharpening the record gate’s conditional to a single HYPOTHESIS-strong residual (the half-sided modular inclusion source). Adds §4.5 and Result Q18.6, CAT I (10 checks), and references to A17/M3/Q7/F19/Borchers/Wiesbrock/Connes/Takesaki. Verification 35/35 → 45/45 PASS.  
**v1.0 (July 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes following ZS-F48 v1.6 and the F48 physical-bridge seed report. Closes the F48 state gate (PROVEN), derives the probability and Born-martingale gates (DERIVED), reduces the record gate to χZ \= −1 (DERIVED-CONDITIONAL) via Theorem Q18.2 and the Maassen–Kümmerer dark-subspace exclusion, and upgrades the collapse-rate to DERIVED-CONDITIONAL under efficiency-1 monitoring. Executes the anti-numerology gate F-Q18.6 (Born fit χ²/dof \= 0.68, alternatives rejected) and confirms via Benoist–Pellegrini estimation stability that strong sufficiency, though OPEN, is non-epistemic. Issued as ZS-Q18 (not ZS-Q17, which is already assigned).