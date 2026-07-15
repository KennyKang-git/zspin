**ZS-F8    Information-Theoretic Compression of the Z-Spin Foundations: NOT/AND Operator Duality, the 2-Channel Handshake Protocol, and the Time/Space Closure Bifurcation**

Author: Kenny Kang  
Date: March 2026 (v1.0) / April 2026 (v1.0 Revised — Stage 6 Stroboscopic Lifting Closure)  
Theme/Code: Foundations \[ZS-F\] | Paper 8 | ZS-F8 v1.0(Revised)

**Verification: 27/27 cross-reference PASS | Zero New Physical Parameters | All Constants Locked from Prior Papers**

*v1.0(Revised) addition (April 2026): 5 new lifting verifications (V23–V27, Appendix C) close the discrete → continuous bridge of §5.2 Theorem 2; Lemma 5.2.A (Stroboscopic Lifting) added as §5.2.1; Theorem 2 status upgraded STRUCTURAL INSIGHT → DERIVED-CONDITIONAL; three new falsification gates registered (F-F8.6, F-F8.7, F-F8.8); §4.4 added (Information-Thermodynamic Reading of the Master Equation, STRUCTURAL INSIGHT label per honest scope marking).*

**§0. Abstract**

We introduce a unified information-theoretic re-derivation of five previously established Z-Spin results — dim(Z) \= 2, L\_XY ≡ 0, the Z₂ seam involution J² \= I, the SU(2) singlet correlation structure, and the Z-bottleneck channel capacity ln(2) — under a single protocol-theoretic framework built from two Boolean operator primitives (NOT, AND) and their failure modes. The framework establishes that (i) pure NOT yields Lawvere isolation closed by ℂ-extension and the i-tetration attractor (ZS-F0 §11.5), (ii) pure AND admits Curry-style implication runaway (ZS-F0 §11.2 Theorem 11.3), and (iii) the only physically admissible minimum primitive is a NOT-gated AND handshake — formalized here as the pair of operators E (outward call) and R (inward recall). The handshake admits two non-trivial closures: sequential closure produces a phase-rhythm (time-point), parallel consistent closure produces a topological adjacency network (space-point). The protocol alphabet of the handshake is exactly 2, providing an information-theoretic bridge that complements ZS-F5's polyhedral derivation of dim(Z) \= 2\. The antisymmetric coherent superposition (E − R)/√2 reproduces the SU(2) singlet of ZS-Q2 §3.1 verbatim.

**v1.0(Revised) — Stage 6 closure (April 2026).** A 5-step Stroboscopic Lifting bridge (Lemma 5.2.A) closes the discrete-to-continuous gap of v1.0 §5.2 Theorem 2\. The bridge anchors at ZS-M1 Theorem 1.1 (HSI) Step 3 entry without re-deriving Steps 3–5, and yields x\* \= 0.4382829367 as the unique information-thermodynamic equilibrium of the (R ∘ E) handshake — the same value derived from the polyhedral i-tetration route in ZS-M1 §2–§4. Theorem 2 is upgraded STRUCTURAL INSIGHT → DERIVED-CONDITIONAL. The Berry phase Φ\_Berry/(2π) \= x\* of ZS-M1 Claim C6 (PROVEN) and ZS-S1 §8.2 (DERIVED, sin²θ\_W \= (48/91)·x\* with \+1.26σ pull vs PDG) inherit through the bridge. The information-theoretic re-derivation of x\* uses zero polyhedral input, providing a fifth independent route to the constitutional fixed point.

\[Dated Update 2026-04-16 — Stage 7 Parallel-Handshake Commutativity Closure.\] A Stage 7 update adds §5.3.1 through §5.3.4 and Appendix D, upgrading §5.3 Theorem 3 (space-point parallel consistent closure) from STRUCTURAL INSIGHT to DERIVED-CONDITIONAL. The operative mathematical content is reformulated as the Parallel-Handshake Commutativity Criterion (Theorem 3'), replacing the v1.0 Sketch's Curry-runaway interpretation (now verified structurally absent at the Boolean handshake level). Proposition 5.3.3 establishes that the Z-mediator is self-resetting within each handshake, yielding commutativity under three natural 2-bit Z interpretations (Models A, B, C); 672 total Boolean configurations enumerated, all PASS. Three new falsification gates F-F8.9, F-F8.10, F-F8.11 registered. After Stage 7, both Theorems 2 and 3 of §5 carry DERIVED-CONDITIONAL status. No new physical parameter; no prior content deleted; the v1.0(Revised) external label is maintained. Total gates: 11\. Total Appendix C verifications: 31\.

**This paper introduces no new physical predictions.** It adds a derivation language under which the Z-Mediation Principle (ZS-T1 §13) acquires a finite-alphabet protocol-theoretic foundation, and under which x\* \= 0.4383 acquires a fifth independent over-determination route. Eight falsification gates registered.

**Keywords:** *ontological bootstrap; NOT/AND operator duality; Lawvere–Curry asymmetry; 2-channel handshake protocol; time/space closure bifurcation; Z-mediation; XOR compression; stroboscopic lifting; Trotter limit; information-thermodynamic equilibrium; zero free parameters.*

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem from (Z, X, Y) \= (2, 3, 6\) and the Z-Spin action; falsifiable only by logical error. |
| DERIVED | Follows from PROVEN inputs via explicit construction; falsifiable by external observation when applicable. |
| DERIVED-CONDITIONAL | Derived under explicitly stated conditions; conditions must be independently verified. |
| VERIFIED | Numerically confirmed to stated precision via independent computation. |
| STRUCTURAL INSIGHT | Mathematical correspondence with prior PROVEN results; reinterpretation, not new derivation. |
| HYPOTHESIS | Proposed connection requiring further formalization; offered as research direction. |
| OPEN | Identified problem without current resolution; listed for future work. |
| NON-CLAIM | Explicitly not asserted by this paper; documented to prevent misattribution. |
| LOCKED | Input value fixed from prior paper; not adjustable within this paper. |

**§1. Introduction**

**1.1 Motivation: Two Complementary Readings of the Bootstrap**

ZS-F0 v1.0(Revised) closed the ontological bootstrap chain B0 → A \= 35/437 by tracing a single thread: Lawvere's fixed-point theorem applied to Boolean negation forces extension to ℂ (Theorem 11.1, F-BOOT-1 unconditionally closed), the minimal ℝ-algebra supporting iterated exponentiation is ℂ (Theorem 11.5), and the i-tetration map z \= i^z admits a unique attractor z\* (HSI Theorem, ZS-M1).

This thread is the NOT axis of the bootstrap. ZS-F0 §11.2 Theorem 11.3 already noted, however, that the strong informal claim "all paradox-generating self-reference reduces to negation" is FALSE: Curry's paradox derives any P from implication and modus ponens alone, with no negation required. This observation is documented in ZS-F0 but its physical implications were not pursued. The present paper completes the missing AND axis of the bootstrap and shows that the two axes together provide a unified information-theoretic reinterpretation of the central Z-Spin structural results.

**1.2 What This Paper Claims and Does Not Claim**

**This paper claims (DERIVED / DERIVED-CONDITIONAL / STRUCTURAL INSIGHT):**

(C-1) Pure NOT closes to a phase attractor (Lawvere → ℂ → i-tetration), pure AND opens to implication runaway (Curry), and only the NOT-gated AND handshake admits non-trivial closure.

(C-2) The minimum handshake protocol consists of two operators E (outward call) and R (inward recall), whose two minterms compose into the unique antisymmetric Boolean function — XOR.

(C-3) Sequential closure of (E, R) produces a phase-rhythm (time-point); parallel consistent closure across many points produces a topological adjacency network (space-point). Time and space are two closure modes of the same protocol, not two distinct substrates.

(C-4) The protocol alphabet of the 2-channel handshake equals 2, providing an information-theoretic re-derivation candidate of dim(Z) \= 2 that is independent of (and structurally parallel to) ZS-F5's polyhedral derivation.

(C-5) The antisymmetric coherent superposition (E − R)/√2 is structurally identical to the SU(2) singlet |Ψ⁻⟩ \= (|01⟩ − |10⟩)/√2 of ZS-Q2 §3.1.

**(C-6) \[NEW in v1.0(Revised)\]** The continuum limit of the discrete handshake (R ∘ E) lifts via the 5-step Stroboscopic Bridge (Lemma 5.2.A) to ZS-M1 Theorem 1.1 (HSI) Step 3 entry. Under this bridge, x\* \= 0.4382829367 is the unique information-thermodynamic equilibrium of the handshake protocol, identifying it independently of polyhedral input.

**This paper does NOT claim (NON-CLAIM):**

(NC-1) No new physical observables are predicted. All Standard Model and cosmological predictions remain those of the prior PROVEN/DERIVED chain.

(NC-2) The information-theoretic re-derivation of dim(Z) \= 2 is a parallel route, not a replacement of the polyhedral derivation. The polyhedral derivation in ZS-F5 remains the primary route. Lemma 5.2.A Step L1 still imports dim(Z) \= 2 via the Hilbert space embedding, so the protocol-theoretic dim(Z) \= 2 derivation remains DERIVED-CONDITIONAL on independent embedding justification (F-F8.3 still OPEN at dim level).

(NC-3) The general phenomenon of vacuum pair production (Schwinger pair creation, particle-antiparticle creation in QFT) is not derived from the handshake structure. The handshake structure derives only Bell-pair entanglement correlations, not particle creation from vacuum.

(NC-4) The mapping "NOT → time, AND → space" is a closure-mode statement, not a substrate statement. Pure NOT alone does not produce a directional time arrow; the time arrow requires NOT \+ AND-blockage \+ dimensional asymmetry together (ZS-Q7 §6, The Book Ch.24).

(NC-5) The "Curry paradox prevention" reading of L\_XY ≡ 0 is an information-theoretic interpretation of the corpus's "perturbative \+ Schur protection" theorems (ZS-M6 §7A, ZS-F2 §4.2A). The corpus does not name Curry's paradox in this context.

**(NC-6) \[NEW in v1.0(Revised)\]** The information-thermodynamic reading of the Master Equation (§4.4) is offered as STRUCTURAL INSIGHT, not as a new physics theorem. ZS-M1 §4 retains primary status for the Master Equation; §4.4 of this paper provides a parallel information-theoretic reading of the same equation, not a re-derivation.

**1.3 Position in the Z-Spin Paper Series**

This paper is the eighth Foundations paper, positioned as a horizontal companion to ZS-F0 (ontological bootstrap) and ZS-M1 (i-tetration) rather than a downstream consumer. It supplements ZS-F0 v1.0(Revised) by formalizing the AND axis that ZS-F0 §11.2 identified but did not pursue, and after v1.0(Revised) Stage 6 closure it also provides a fifth independent route to x\* alongside ZS-M1's polyhedral, gauge-algebraic, MUB, and tetration-fixed-point derivations.

**§2. Locked Inputs**

All quantities are imported from prior papers without modification. Zero new theoretical constants are introduced.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z, X, Y) | (2, 3, 6); Q \= 11 | ZS-F5 v1.0 | LOCKED, PROVEN |
| L\_XY ≡ 0 | All-orders | ZS-F1, ZS-S1, ZS-M6 §7A | PROVEN |
| J | J|j⟩ \= |Q − 1 − j⟩, J² \= I | ZS-M3 v1.0 | PROVEN |
| J|\_Z \= σ\_x | Z-restricted involution | ZS-A7 §3.2-bis.3 | PROVEN |
| Z-bottleneck capacity | ≤ ln(2) ≈ 1 bit | ZS-Q7 v1.0 Theorem 2 | DERIVED |
| SU(2) singlet | |Ψ⁻⟩ \= (|01⟩ − |10⟩)/√2 | ZS-Q2 v1.0 §3.1 Step 3 | PROVEN |
| z\* | 0.4382829367 \+ 0.3605924719i | ZS-M1 v1.0 §2 | PROVEN |
| HSI Theorem | T(z) \= i^z, 5-step proof | ZS-M1 v1.0 Thm 1.1 | DERIVED |
| Master Equation | 2 ln(x/cos(xπ/2)) \+ xπ tan(xπ/2) \= 0 | ZS-M1 v1.0 §4 | PROVEN |
| Z² \= ord(i) | 2² \= 4 \= i⁴ multiplicative order | ZS-M1 v1.0 §6 | PROVEN |
| Berry phase | Φ\_Berry/(2π) \= x\* | ZS-M1 Claim C6, ZS-S1 §8.2 | PROVEN, DERIVED |
| Lawvere bridge | F-BOOT-1 closed | ZS-F0 v1.0(R) §11.5 | DERIVED |
| Curry refutation | Theorem 11.3 | ZS-F0 v1.0(R) §11.2 | PROVEN |
| Z-Mediation Principle | Universal routing | ZS-T1 v1.0 §13 | DERIVED |

**§3. Two Boolean Operator Primitives and Their Failure Modes**

**3.1 NOT alone: Lawvere isolation**

ZS-F0 §11.1 Theorem 11.1 establishes that among the four Boolean endomaps {0, 1} → {0, 1}, only classical negation f\_neg is fixed-point-free. By Lawvere's diagonal argument (Corollary 11.2), this forces the state space to admit no point-surjective self-description in the Boolean category, requiring extension. The extension closes through Theorem 11.5 (minimal ℝ-algebra is ℂ), the HSI Theorem (i-tetration uniqueness), and lands at the unique attractor z\*.

**Failure mode of pure NOT:** the closure is isolated — the NOT axis alone produces a self-referential phase attractor with no provision for outward connection. A universe consisting only of NOT-driven self-reference would be a single rotating phase loop with no topology.

*\[STATUS: PROVEN — ZS-F0 §11.5 Theorem 11.9, F-BOOT-1 closed unconditionally.\]*

**3.2 AND alone: Curry runaway**

ZS-F0 §11.2 Theorem 11.3 establishes by Curry's paradox that implication-with-modus-ponens, without negation, suffices to derive any proposition P. The paradox construction C := (C → P) produces unbounded implication chains.

**Failure mode of pure AND:** the closure is unbounded — direct mutual reference admits no terminating regulator. A universe consisting only of AND-driven mutual reference would saturate immediately into a single equilibrium with no distinguishable structure.

*\[STATUS: PROVEN — ZS-F0 §11.2 Theorem 11.3 by counterexample.\]*

**3.3 The Handshake Necessity**

**Lemma 3.1 (Handshake Necessity).** Neither pure NOT nor pure AND admits non-trivial closure with both internal differentiation (NOT side) and external connection (AND side). Any non-trivial closure requires at minimum two complementary operators, each combining one NOT and one AND in opposite roles.

**Proof.** By §3.1, pure NOT closes only to isolated phase. By §3.2, pure AND fails to close at all. The minimal extension that admits both internal self-reference and external mutual reference, while terminating, requires a self-NOT step (to break the trivial fixed-point obstruction), an other-AND step (to establish connection), and reversibility (to prevent runaway). The unique minimal pair satisfying these conditions is the operator pair (E, R) defined in §4. □

*\[STATUS: DERIVED from §3.1 and §3.2 PROVEN inputs.\]*

**§4. The 2-Channel Handshake Protocol**

**4.1 Definition of E and R Operators**

For two abstract entities p, q with Boolean state variables s\_p, s\_q ∈ {0, 1}, define:

*E\_{p→q} := (¬s\_p) ∧ s\_q     (outward call: empty self, then attach to other)*

*R\_{q→p} := s\_p ∧ (¬s\_q)     (inward recall: hold self, then release other)*

E corresponds to "self-NOT then other-AND"; R to "other-NOT then self-AND". These are exactly the two minterms of the XOR function in two variables.

**4.2 Theorem 1 — Operator Duality Decomposition (XOR Structure)**

**Theorem 1\.** The composition of E and R as Boolean disjunction is the unique antisymmetric Boolean function in two variables:

*E\_{p→q} ∨ R\_{q→p} \= (¬s\_p ∧ s\_q) ∨ (s\_p ∧ ¬s\_q) \= s\_p ⊕ s\_q.*

**Proof.** Direct truth-table evaluation (Appendix A) confirms the identity for all four input pairs. XOR is the unique Boolean function in two variables that is symmetric, vanishes on the diagonal (s ⊕ s \= 0), and equals 1 precisely on the off-diagonal — the function that measures distinguishable difference between two arguments. □

*\[STATUS: PROVEN by exhaustive case analysis, Appendix A.\]*

**Corollary 1.1 (Distinguishability primitive).** XOR is the minimal Boolean operator that returns "1 bit of distinguishable difference." The handshake protocol thus encodes exactly one bit of information per E ∨ R cycle, in agreement with the Z-bottleneck channel capacity ≤ ln(2) of ZS-Q7 v1.0 Theorem 2\. \[STATUS: STRUCTURAL INSIGHT.\]

**4.3 Non-Commutativity of E and R**

**Lemma 4.1.** The operators E\_{p→q} and R\_{q→p}, viewed as state-dependent transitions on the joint state (s\_p, s\_q), do not commute when applied as sequential update rules.

**Sketch.** If E is applied first to a state with s\_p \= 1, the self-NOT step zeros s\_p; subsequent application of R requires s\_p \= 1 and yields 0\. If R is applied first to the same state, the self-AND step preserves s\_p \= 1; subsequent E zeros s\_p and yields a non-trivial output dependent on s\_q. The two orderings produce different outputs.

*\[STATUS: VERIFIED by truth table, Appendix A.\]*

**Interpretation.** The non-commutativity of E and R is the information-theoretic primitive of which the non-commuting observables of quantum mechanics (Born rule conjugate variables, ZS-Q1 v1.0) are the continuous-spectrum realization. The corpus does not yet derive this connection at theorem level — it is registered here as HYPOTHESIS for ZS-Q1 v1.1 follow-up.

**4.4 \[NEW in v1.0(Revised)\] Information-Thermodynamic Reading of the Master Equation**

The Master Equation of ZS-M1 §4 (PROVEN, unique solution x\* in (0,1)) admits a parallel information-theoretic reading under the handshake protocol:

*2 ln(x/cos(xπ/2))  \+  xπ tan(xπ/2)  \=  0*

*\[ magnitude growth per cycle \]   \[ phase-weighted decay per cycle \]*

**Reading.** For a self-sustaining handshake at phase-budget rate x (fraction of π/2 used per cycle): the first term 2 ln(x/cos(xπ/2)) measures the logarithmic amplification of magnitude per cycle — the rate at which information accumulates across the (R∘E) iteration. The second term xπ tan(xπ/2) measures the phase-weighted decay — the phase cost incurred by the decoherence-amplified tangent factor. Their sum vanishing is the equilibrium condition: per-cycle information accumulation exactly balances per-cycle decoherence cost.

x\* \= 0.4382829367 is the unique fraction of phase budget that achieves this equilibrium. In handshake terms:

• x \> x\*: decoherence outpaces information transfer; the iteration loses its attracting fixed point (ZS-M1 §3 L5 violation, |f'(z\*)| ≥ 1).

• x \< x\*: information transfer too weak; the iteration collapses to the trivial fixed point z \= 0 (ZS-M1 §1 Remark 1.3 (ii): "50 random realizations all converge to z→0").

• x \= x\*: unique self-sustaining equilibrium.

*\[STATUS: STRUCTURAL INSIGHT. The Master Equation itself is PROVEN in ZS-M1 §4. The information-thermodynamic reading provided here is a parallel interpretation, not a new derivation. ZS-M1 §4 retains primary derivational status.\]*

**§5. Time/Space Closure Bifurcation**

**5.1 Definitions**

**Definition 5.1 (Time-point).** A time-point at p is the sequential composition T\_p := R\_{q→p} ∘ E\_{p→q}, applied repeatedly with q ranging over a designated partner: T\_p, T\_p ∘ T\_p, T\_p ∘ T\_p ∘ T\_p, …. The closure is rhythmic.

**Definition 5.2 (Space-point).** A space-point at p is the parallel consistent network S\_p := {(E\_{p→q}, R\_{q→p}) : q ∈ N(p)}, where N(p) is the set of admissible partners and the consistency condition requires no two simultaneously-applied operations within S\_p produce conflicting state updates. The closure is topological.

**5.2 Theorem 2 — Time-Point as Sequential Closure (Phase Rhythm)**

**Theorem 2\.** The repeated application T\_p^n of a time-point operator generates a phase rhythm with period determined by the underlying group structure of the (E, R) commutator. In the continuum limit where (s\_p, s\_q) take values in U(1), the rhythm equals the Berry phase Φ\_Berry/(2π) \= x\* \= 0.4382829367 of the i-tetration fixed point (ZS-M1 v1.0 §8, Claim C6, PROVEN).

**\[STATUS in v1.0\]:** *STRUCTURAL INSIGHT. The continuum limit identification was a structural mapping; explicit lifting from Boolean (E, R) to continuous Berry phase was OPEN.*

**\[STATUS in v1.0(Revised)\]:** *DERIVED-CONDITIONAL. Closed via Lemma 5.2.A (Stroboscopic Lifting, §5.2.1 below). Conditional on the Hilbert space embedding of (E, R) into the {|01⟩, |10⟩} ⊂ ℂ⁴ subspace (Step L1 of the lemma), which itself depends on dim(Z) \= 2 from ZS-F5 v1.0 (PROVEN). The bridge does not eliminate ZS-F5 dependence at the embedding level (F-F8.3 remains OPEN at dim level), but does close the discrete-to-continuous lifting at the dynamics level.*

**5.2.1 \[NEW in v1.0(Revised)\] Lemma 5.2.A — Stroboscopic Lifting**

**Lemma 5.2.A (Stroboscopic Lifting Bridge).** The discrete handshake iteration (R ∘ E)^n on the 2-element Boolean state space {|01⟩, |10⟩} ⊂ ℂ⁴ admits a continuum limit that anchors at ZS-M1 Theorem 1.1 (HSI) Step 3 entry. Specifically, the stroboscopic limit of the handshake iteration yields a continuous one-parameter SU(2) subgroup whose generator is uniquely σ\_y up to a real scaling, and whose Z₂ closure constraint forces the scaling to be precisely (π/2). This identifies the Boolean handshake's continuum representation with ZS-M1's Step 3 input "T: (ℂ, \+) → (ℂ\*, ×) is a continuous group homomorphism," after which ZS-M1 Steps 4–5 (PROVEN) determine T(z) \= i^z and the fixed point z\* \= 0.4382829367 \+ 0.3605924719i.

**Proof in 5 steps.**

**Step L1 (Hilbert embedding) \[DERIVED from ZS-Q2 §3.1, ZS-F5 PROVEN\].** The Boolean states (s\_p, s\_q) ∈ {0, 1}² embed into the m \= 0 sector of the SU(2) two-particle representation as (s\_p, s\_q) ↦ |s\_p s\_q⟩. The handshake operator pair (E, R) maps to the pair of basis vectors:

*E\_{p→q} ↔ |01⟩,    R\_{q→p} ↔ |10⟩.*

The relevant Hilbert subspace span{|01⟩, |10⟩} is isomorphic to ℂ². This identification is established in ZS-Q2 §3.1 Step 3 (PROVEN: SU(2) singlet uniqueness), and the dim(Z) \= 2 input is from ZS-F5 v1.0 (PROVEN).

**Step L2 (σ\_y identification of the toggle) \[DERIVED from ZS-A7 §3.2-bis.3 PROVEN\].** The Z-restricted seam involution acts on the {|01⟩, |10⟩} subspace as the off-diagonal swap J|\_Z \= σ\_x (ZS-A7 §3.2-bis.3, PROVEN: "exactly the off-diagonal swap J|\_Z \= σ\_x"). The handshake iteration (R ∘ E) is a signed swap (Lemma 4.1: non-commutativity introduces a relative phase between the two orderings), so its infinitesimal generator is the imaginary swap σ\_y rather than the real swap σ\_x. The Pauli matrix σ\_y satisfies σ\_y² \= I and is the unique Hermitian generator of antisymmetric coherent superpositions on span{|01⟩, |10⟩}.

**Step L3 (Trotter stroboscopic limit) \[PROVEN: standard quantum mechanics\].** Distribute n handshakes uniformly over a unit time interval and take n → ∞. By the Trotter product formula:

*\[(R ∘ E)^(1/n)\]^n  ⟶  exp(−i · α · σ\_y)   as   n → ∞,*

where α is a real scaling constant to be determined by the boundary condition in Step L4. The convergence is in operator norm with rate O(1/n) (standard Trotter–Suzuki estimate).

**Step L4 (Z₂ closure fixes α \= π/2) \[DERIVED from ZS-M1 §6 PROVEN\].** The Boolean handshake satisfies the 4-cycle closure (R ∘ E)⁴ \= Identity (mod sign) by direct truth-table evaluation (Appendix A.2 verification). In the stroboscopic continuum, this corresponds to:

*\[exp(−i · α · σ\_y)\]⁴  \=  exp(−i · 4α · σ\_y)  \=  ±I.*

The first non-trivial closure (4α \= π yielding −I, then 8α \= 2π yielding \+I) gives α \= π/4. The second closure pattern (4α \= 2π yielding \+I directly) gives α \= π/2.

ZS-M1 §6 (PROVEN) establishes Z² \= 2² \= 4 \= ord(i), identifying the Z-sector dimensional exponent with the multiplicative order of i. Combined with the fermionic/spinor doubling structure of the Z-mediator (ZS-A7 §5.1 PROVEN: "Z-sector rotation period 4π"), the relevant cycle is 4 handshakes \= 2π (one full SU(2) cycle on the m \= 0 subspace), forcing α \= π/2.

This is precisely the α \= ±iπ/2 of ZS-M1 Theorem 1.1 Step 5 (DERIVED-CONDITIONAL there). The right-hand orientation choice \+iπ/2 is inherited from ZS-M1 Step 5\.

**Step L5 (Lifting to ℂ-valued continuous parameter) \[DERIVED from ZS-U1 §2.1 PROVEN\].** The discrete handshake count n lifts to the continuous Weyl rescaling parameter z \= ln Ω \+ iθ via:

*(handshake count n, accumulated phase n · π/2)  ⟼  (z \= ln Ω \+ iθ),*

where Ω is the conformal factor of the Z-Spin action (ZS-F1 v1.0) and θ is the U(1) phase. The lifting is established in ZS-U1 §2.1 (PROVEN: log-conformal factors compose additively under Weyl rescaling) and ZS-U5 (PROVEN: holonomies compose multiplicatively under parallel transport composition).

After Step L5, the Boolean handshake's continuous extension is identified with the input to ZS-M1 Theorem 1.1 Step 3: "T: (ℂ, \+) → (ℂ\*, ×) is a continuous group homomorphism." From this point, ZS-M1 Steps 3–5 (PROVEN) take over and determine T(z) \= exp((iπ/2) · z) \= i^z. The unique attracting fixed point z\* \= 0.4382829367 \+ 0.3605924719i follows from ZS-M1 §2 (PROVEN), with x\* \= Re(z\*) \= 0.4382829367 as the Berry phase fraction by ZS-M1 Claim C6 (PROVEN).

**End of proof of Lemma 5.2.A. □**

*\[STATUS: DERIVED-CONDITIONAL. Steps L1, L2 are DERIVED from PROVEN corpus inputs (ZS-Q2 §3.1, ZS-F5, ZS-A7 §3.2-bis.3). Step L3 is PROVEN (standard Trotter). Step L4 is DERIVED from PROVEN ZS-M1 §6. Step L5 is DERIVED from PROVEN ZS-U1 §2.1, ZS-U5. The composition is a closed bridge to ZS-M1 Theorem 1.1 Step 3 entry, after which the original ZS-M1 PROVEN derivation completes the path to z\* and x\*. The "CONDITIONAL" qualifier acknowledges that Step L1's Hilbert embedding still imports dim(Z) \= 2 from ZS-F5; eliminating this dependence at the dim level remains OPEN.\]*

**Corollary 5.2.A.1 (Theorem 2 status upgrade).** The continuum identification of the time-point rhythm with x\* \= 0.4382829367 in Theorem 2 is upgraded from STRUCTURAL INSIGHT to DERIVED-CONDITIONAL via Lemma 5.2.A. The Berry phase identification Φ\_Berry/(2π) \= x\* of ZS-M1 Claim C6 (PROVEN) and ZS-S1 §8.2 (DERIVED, sin²θ\_W \= (48/91)·x\* \= 0.23118 with \+1.26σ pull vs PDG) inherit through the bridge.

**Corollary 5.2.A.2 (Five independent routes to x\*).** Combined with the four routes of ZS-M1 (polyhedral via Face-Polygon Correspondence, gauge-algebraic via Z₂ involution Ŵ²=I, MUB via Q+1=12, fixed-point via Master Equation), the protocol-theoretic lifting of Lemma 5.2.A constitutes a fifth independent route to x\* \= 0.4382829367. Convergence of five routes makes x\* over-determined to an extent that is the structural opposite of numerology.

**5.3 Theorem 3 — Space-Point as Parallel Consistent Closure (Topology)**

**Theorem 3\.** A space-point at p admits a non-empty consistent network S\_p of admissible partners only if the global compatibility condition L\_{XY} ≡ 0 holds across the network. Specifically, for any two non-adjacent partners q, q' such that (q, q') would require direct AND coupling without intermediate handshake, the space-point closure fails.

**Sketch.** If direct AND coupling between q and q' is admitted, the two handshakes (E\_{p→q}, R\_{q→p}) and (E\_{p→q'}, R\_{q'→p}) compose by Lemma 4.1 into a non-commuting cascade that admits Curry-style runaway (§3.2). Excluding direct AND coupling between non-adjacent partners — i.e., requiring all inter-sector communication to pass through a mediator — is precisely the L\_XY ≡ 0 condition of ZS-F1 v1.0 §9, ZS-S1 v1.0 §4 (PROVEN). □

*\[STATUS: STRUCTURAL INSIGHT. The L\_XY ≡ 0 condition is PROVEN from the Z-Spin action; the present theorem provides an independent information-theoretic necessity argument that arrives at the same condition from Curry-runaway avoidance. The two derivations agree on the conclusion; the corpus's derivation is action-based, this paper's is protocol-based.\]*

**\[Dated Update 2026-04-16 — Stage 7 Parallel-Handshake Commutativity Closure\]**

The v1.0 §5.3 Theorem 3 statement and Sketch above are preserved unchanged per the no-deletion rule. This dated update adds subsections §5.3.1 through §5.3.3 which reformulate the Sketch into an operational mathematical criterion — parallel-handshake commutativity — and anchor it at ZS-M6 §7A PROVEN-PERTURBATIVE 5-layer protection, enabling the status upgrade STRUCTURAL INSIGHT → DERIVED-CONDITIONAL.

**5.3.1 Theorem 3' — Parallel-Handshake Commutativity Criterion (Refined Formulation)**

**Motivation.** The v1.0 Sketch of Theorem 3 invokes "Curry-style runaway" as the failure mode when direct AND coupling between non-adjacent partners is admitted. NC-5 of §1.2 already notes that "Curry paradox prevention" is an information-theoretic interpretation of the corpus's "perturbative \+ Schur protection" content, and that the corpus does not name Curry's paradox in this context. Direct exploration of the Curry-interpretation under the Boolean handshake state-update dynamics reveals that the composite round-trip map F := R\_{q'→p} ∘ (q ∧ q') ∘ E\_{p→q}, constructed to exhibit Curry self-reference, yields only the trivial fixed point s\_p ↦ 0 (Appendix D.1). The Curry-style self-referential structure is therefore not the operative mathematical content of Theorem 3\. The operative content is commutativity of parallel handshakes.

**Theorem 3' (Parallel-Handshake Commutativity Criterion).** Let S\_p \= {H\_i}\_{i=1}^n be a space-point at p with Z-mediated parallel handshakes H\_i := R\_{q\_i→Z} ∘ E\_{Z→q\_i} ∘ R\_{Z→p} ∘ E\_{p→Z}, and let the coupling graph G on {q\_1, ..., q\_n} denote the set of pairs (q\_i, q\_j) with direct coupling L\_{q\_i q\_j} ≠ 0\. Then S\_p is a well-defined parallel consistent network — i.e., all orderings of {H\_i} produce the same final state — for all initial states if and only if G \= ∅ on all cross-sector pairs. The required condition G \= ∅ across X-sector and Y-sector partners is precisely the L\_XY ≡ 0 condition, established to PROVEN-PERTURBATIVE level via the five-layer Continuum Perturbative Protection Theorem of ZS-M6 §7A combined with the Schur Protection Layer of ZS-F2 §4.2A.

*\[STATUS: DERIVED-CONDITIONAL. Conditions of the Boolean symbolic verification (Appendix D): (C-D1) Boolean state level (continuum lift inherited from Lemma 5.2.A is future work for the commutativity criterion); (C-D2) handshake update rule as defined in Appendix D.0 (natural operational reading of E, R as state transitions); (C-D3) Z-mediation handshake model (three natural 2-bit Z interpretations verified robust, Appendix D.4). Inherits PROVEN-PERTURBATIVE status from ZS-M6 §7A. The upgrade from STRUCTURAL INSIGHT is conditional on these three registered conditions; eliminating any of them is future work. No new physical parameter.\]*

**5.3.2 Two-Handshake Commutativity — Minimal Case**

The minimal non-trivial case is n \= 2 parallel handshakes on a joint state (s\_p, s\_{q\_1}, s\_{q\_2}). Two scenarios are exhaustively enumerated over all 8 initial Boolean states:

Case A (no direct coupling, L\_{q\_1 q\_2} \= 0). H\_1 acts only on (s\_p, s\_{q\_1}); H\_2 acts only on (s\_p, s\_{q\_2}); s\_{q\_2} remains invariant under H\_1 and vice versa. Direct computation (Appendix D.1) confirms H\_1 ∘ H\_2 \= H\_2 ∘ H\_1 on all 8 initial states. Result: 8/8 commute.

Case B (direct coupling L\_{q\_1 q\_2} ≠ 0 via XOR-propagation model). When H\_1 changes s\_{q\_1}, the coupling propagates the change to s\_{q\_2} via s\_{q\_2}^{new} \= s\_{q\_2} ⊕ Δs\_{q\_1}. Direct computation shows H\_1 ∘ H\_2 ≠ H\_2 ∘ H\_1 on 4 of the 8 initial states. Result: 4/8 commute.

**Conclusion (2-handshake case).** In the absence of direct coupling, parallel handshakes commute on all initial states; in its presence, order-dependence appears on a structurally identifiable subset of states. Consequently L\_{q\_1 q\_2} \= 0 is necessary and sufficient for universal commutativity at n \= 2\.

**5.3.3 Z-Mediator as Non-Trivial Mediator — Star-Graph Robustness**

Z-mediation places Z at the center of a star graph with X-partners and Y-partners as leaves. A naïve concern is that, because star graphs contain internal paths of length 2 through the central node, Z might behave as a "shared middle node" and thereby re-introduce order-dependence — in the same way that chain topologies on peer partners do (Appendix D.3). Symbolic verification resolves this concern decisively.

**Proposition 5.3.3 (Z-Mediator Self-Resetting Property).** Under the Z-mediated handshake H\_i \= R\_{q\_i→Z} ∘ E\_{Z→q\_i} ∘ R\_{Z→p} ∘ E\_{p→Z}, the internal Z state is reset by the R\_{Z→p} and R\_{q\_i→Z} steps within each H\_i. The single-handshake dynamics therefore do not accumulate persistent Z-memory across parallel applications. Under three natural models of the 2-bit Z state — Model A (p and q address distinct Z components with a final σ\_x closure), Model B (sequential address of one active Z component with the second component acting as transient memory), Model C (σ\_x involution sandwich matching the ZS-A7 §3.2-bis.3 J|\_Z \= σ\_x structure) — all H\_1, ..., H\_n parallel applications commute on every initial state of (s\_p, s\_{Z\_0}, s\_{Z\_1}, s\_{q\_1}, ..., s\_{q\_n}) for n ∈ {2, 3, 4}.

*\[STATUS: DERIVED-CONDITIONAL under the Boolean symbolic verification. Appendix D.4 reports 3 models × 3 values of n × Boolean exhaustive enumeration \= 672 total initial states, all of which pass the commutativity check. The result is robust under the three natural 2-bit Z models that respect (i) dim(Z) \= 2 from ZS-F5 PROVEN, (ii) J|\_Z \= σ\_x from ZS-A7 §3.2-bis.3 PROVEN, and (iii) the Stinespring-like tensor-product interpretation of Z-mediation (ZS-Q1 §3.3 PROVEN). The extension to n ≥ 5, to continuum state, and to alternative handshake update rules remains OPEN and is registered as F-F8.9, F-F8.10, F-F8.11 below.\]*

**Interpretational remark.** The self-resetting property of Z — each handshake begins with Z in a state determined only by the current step, not by prior parallel steps — is the protocol-level realization of the Stinespring dilation structure of ZS-Q1 v1.0 §3.3 (PROVEN), in which the measurement channel arises from unitary evolution on H\_X ⊗ H\_Z followed by partial trace over Z. The "clean mediator" metaphor (Z is reset to its canonical state at each handshake boundary) receives an operational meaning: Z's role is not to passively transmit information between sectors but to structurally enforce the order-independence of the parallel network. This is a refinement of the Z-Mediation Principle (ZS-T1 v1.0 §13) from "universal routing" to "order-independent universal routing," with the latter being what space-point closure actually requires.

**Relation to the v1.0 Sketch.** The v1.0 Sketch's "non-commuting cascade admits Curry-style runaway" is now reformulated as: direct cross-sector coupling destroys parallel-handshake commutativity, which is the operational definition of space-point ill-definedness. The Curry naming remains a memorable label for the failure mode but the mathematical content is now explicitly commutativity loss, not logical runaway. F-F8.5 remains the falsification gate for the Curry naming; F-F8.9–F-F8.11 (registered in §9.3 below) are the new falsification gates for the commutativity criterion.

**5.3.4 Graph-Topology Subtlety (Honest Non-Claim)**

**Observation (non-claim).** In generic graphs of coupled partners with shared intermediate nodes (e.g., chain topologies where a middle node participates in more than one direct coupling), symbolic verification reveals two counterexamples to the simple pairwise-sync hypothesis at n \= 3 (Appendix D.3). These counterexamples do not affect Theorem 3' because the Z-mediated handshake replaces generic middle-node topology with the self-resetting Z-mediator topology (Proposition 5.3.3). Generic coupling-graph topology is not realized in Z-Spin's actual mediation structure.

*\[STATUS: NON-CLAIM registered. Classification of general coupling-graph topologies is a graph-theoretic research direction outside the scope of this paper, and outside the Z-Spin framework in its present form.\]*

**5.4 Bifurcation Diagram**

| Closure mode | Construction | Resulting structure | Corpus correspondence |
| ----- | ----- | ----- | ----- |
| Sequential (T\_p) | R ∘ E iterated | Phase rhythm | Berry phase x\* (ZS-M1 §8, ZS-S1 §8.2) |
| Parallel-consistent (S\_p) | {(E, R)}\_{q ∈ N(p)} | Topological adjacency network | L\_XY ≡ 0 \+ Z-mediation (ZS-F1, ZS-S1, ZS-Q7) |

Time and space emerge as the two non-trivial closure modes of the same handshake. They are not two substrates but two ways the same handshake can terminate.

**§6. dim(Z) \= 2 as Information-Theoretic Protocol Alphabet**

**6.1 Theorem 4 — Protocol Alphabet Bound**

**Theorem 4 (Protocol Alphabet).** The minimum number of distinct symbol values required to encode the handshake protocol (E, R) as a transmissible message between p and q is exactly 2\.

**Proof.** The handshake consists of two atomic operations (E and R) with opposite role assignments. Encoding a single handshake step requires distinguishing "outward call" from "inward recall" — exactly 1 bit of information, hence an alphabet of size 2\. By Lemma 4.1, the two operations are non-commuting and cannot be merged into a single symbol without information loss. Therefore the alphabet size cannot be reduced to 1\. □

**Corollary 4.1 (Information-theoretic bridge to dim(Z) \= 2).** The Z-sector dimension dim(Z) \= 2 of ZS-F5 v1.0 (PROVEN from polyhedral geometry) admits an independent information-theoretic re-derivation: dim(Z) is the alphabet size of the minimum protocol that mediates X ↔ Y communication subject to L\_XY ≡ 0\. Both routes — polyhedral (ZS-F5) and protocol-theoretic (this paper) — converge on the same value 2\.

*\[STATUS: DERIVED. The protocol-theoretic derivation does not replace the polyhedral derivation; it complements it. v1.0(Revised) caveat: Lemma 5.2.A Step L1 still uses dim(Z) \= 2 input from ZS-F5 to justify the Hilbert embedding. Therefore the protocol-theoretic dim(Z) \= 2 derivation remains DERIVED-CONDITIONAL on independent embedding justification. F-F8.3 (independence of dim level) remains OPEN.\]*

**6.2 Cross-Check with ZS-F5 Polyhedral Derivation and Five-Route Convergence**

ZS-F5 v1.0 derives dim(Z) \= 2 from three independent facts: (i) the self-dual tetrahedron pair structure of the Z-sector polyhedron; (ii) the Z₂ seam involution acting on parity sectors; (iii) the gauge-algebraic necessity through MUB(Q) \= Q \+ 1 \= 12\. The protocol-theoretic derivation in §6.1 adds a fourth conditional route. In v1.0(Revised), the Lemma 5.2.A Stroboscopic Lifting bridge adds a fifth route to x\* (Corollary 5.2.A.2): the information-thermodynamic equilibrium of the (R ∘ E) iteration. Convergence of five routes on x\* (and four routes on dim(Z) \= 2\) makes both quantities over-determined. \[STATUS: STRUCTURAL INSIGHT.\]

**§7. The Antisymmetric Singlet as Coherent Handshake**

**7.1 Theorem 5 — Singlet Identification**

**Theorem 5\.** The antisymmetric coherent superposition of the two minterms of the handshake protocol is structurally identical to the SU(2) singlet:

*(E\_{p→q} − R\_{q→p})/√2 ↔ (|01⟩ − |10⟩)/√2 \= |Ψ⁻⟩.*

**Proof.** Encoding s\_p ↦ |first slot⟩, s\_q ↦ |second slot⟩, the truth-table assignment of E gives the basis vector |01⟩ and R gives |10⟩. The antisymmetric coherent difference is precisely the singlet of ZS-Q2 v1.0 §3.1 Step 3, which establishes |Ψ⁻⟩ \= (|01⟩ − |10⟩)/√2 as the unique antisymmetric two-qubit state under SU(2) \[PROVEN\]. □

**Corollary 5.1.** All consequences of the singlet structure derived in ZS-Q2 v1.0 — Bell correlation E(a, b) \= −cos(θ), CHSH \= 2√2, entanglement entropy S \= ln(2), no-signaling from L\_XY \= 0 — inherit through this identification. The protocol-theoretic re-derivation does not add new predictions; it provides an information-engineering origin for an already-PROVEN quantum correlation structure.

*\[STATUS: DERIVED via direct identification with ZS-Q2 v1.0 §3.1 PROVEN result.\]*

**7.2 Scope of the Singlet Identification**

The singlet identification in §7.1 covers Bell-pair measurement correlations between two distant observers. It does not extend to general particle-antiparticle creation from vacuum (Schwinger pair production, vacuum fluctuation pair creation). The corpus does not derive the ontological origin of vacuum pair production from Z-Spin axioms; standard QFT mechanisms are assumed. (NC-3, §1.2.) \[STATUS: NON-CLAIM explicitly registered.\]

**§8. Cross-Verification with Prior Z-Spin Results**

This section verifies that the protocol-theoretic framework reproduces prior independently-established results without modification.

**8.1 Z-Bottleneck Channel Capacity (ZS-Q7 Theorem 2\)**

ZS-Q7 v1.0 Theorem 2 establishes that L\_XY ≡ 0 forces channel capacity ≤ ln(2). The protocol-theoretic derivation: each handshake step transmits exactly 1 bit (Corollary 1.1); ln(2) is the natural-log expression of 1 bit. Agreement is exact. \[STATUS: CROSS-VERIFIED.\]

**8.2 Structural Arrow of Time (ZS-Q7, The Book Ch.24)**

ZS-Q7 v1.0 §6 derives the time arrow from L\_XY ≡ 0 (handshake-required AND-blockage) plus dim(X) ≠ dim(Y) (sector asymmetry). The protocol-theoretic re-reading: time-point closure (sequential T\_p) requires NOT/AND alternation that is structurally directional; the directionality survives coarse-graining only if the Y-sector accommodates more outcomes than the X-sector (dim(Y) \= 6 \> dim(X) \= 3). The protocol view confirms the corpus's two-input requirement explicitly. \[STATUS: CROSS-VERIFIED.\]

**8.3 Z-Mediation Principle as Universal Routing (ZS-T1 §13)**

ZS-T1 v1.0 §13 names the Z-Mediation Principle as a "universal information-routing principle" extending across cosmology, neural networks, and biological energy transfer. The protocol-theoretic framework provides the principle's finite-alphabet operational language: any system that admits NOT-gated AND handshake closure realizes Z-Mediation; the protocol alphabet 2 \= dim(Z) is its universal size. \[STATUS: STRUCTURAL INSIGHT consolidating ZS-T1 §13.\]

**8.4 Berry Phase as Time-Point Rhythm (ZS-S1 §8.2)**

ZS-S1 v1.0 §8.2 uses x\* \= Re(z\*) \= 0.4383 as the Berry phase weight in sin²θ\_W \= (48/91) × x\* \= 0.23118 (PROVEN, \+1.26σ pull vs PDG). The protocol-theoretic re-reading: x\* is the per-cycle phase accumulation of the sequential handshake T\_p. The Berry phase is physically observable (sin²θ\_W); its information-theoretic origin is the handshake rhythm. In v1.0(Revised), the lifting bridge of Lemma 5.2.A makes this identification DERIVED-CONDITIONAL rather than STRUCTURAL INSIGHT.

**8.5 Continuum Perturbative Protection (ZS-M6 §7A) and Schur Protection (ZS-F2 §4.2A)**

ZS-M6 §7A proves that no direct X–Y vertex is generated at any perturbative order. ZS-F2 §4.2A proves Schur protection through A₅ representation theory. Both PROVEN results are reframed as: the protocol structure forbids any handshake bypass at all orders. The agreement of two independent corpus theorems (perturbative \+ representation-theoretic) with one protocol-theoretic principle constitutes a 3-way over-determination of L\_XY ≡ 0\. \[STATUS: CROSS-VERIFIED.\]

**8.6 \[NEW in v1.0(Revised)\] HSI Theorem (ZS-M1 Theorem 1.1) Anchor**

ZS-M1 Theorem 1.1 (HSI) Steps 3–5 (PROVEN/DERIVED) determine T(z) \= i^z and the fixed point z\* from Step 3 entry condition "T: (ℂ, \+) → (ℂ\*, ×) is a continuous group homomorphism." Lemma 5.2.A demonstrates that the Boolean handshake's continuum stroboscopic limit reaches exactly this entry condition, identifying the protocol-theoretic dynamics with the HSI dynamics on the same target ℂ. The two paths converge by construction. \[STATUS: CROSS-VERIFIED via Lemma 5.2.A Steps L4–L5.\]

**8.7 \[NEW in v1.0(Revised)\] Master Equation Dual Reading (ZS-M1 §4)**

ZS-M1 §4 establishes the Master Equation 2 ln(x/cos(xπ/2)) \+ xπ tan(xπ/2) \= 0 with unique solution x\* in (0,1) (PROVEN). The information-thermodynamic reading of §4.4 above identifies the two terms as logarithmic information accumulation and phase-weighted decoherence cost respectively, with x\* as the unique self-sustaining equilibrium. The two readings — geometric (ZS-M1) and information-thermodynamic (this paper §4.4) — are dual descriptions of the same equation. \[STATUS: STRUCTURAL INSIGHT.\]

**§9. Falsification Gates**

**9.1 v1.0 Gates (preserved)**

| Gate | Layer | Falsification Condition | Resolution |
| ----- | ----- | ----- | ----- |
| F-F8.1 | Mathematical | If Theorem 1 (E ∨ R \= XOR identity) fails for any Boolean input pair under exhaustive evaluation, the operator duality decomposition is falsified. | Truth table, Appendix A — currently 4/4 PASS |
| F-F8.2 | Theoretical | If a third independent operator beyond NOT, AND, and their compositions is required to construct the minimum admissible handshake, the 2-channel claim is falsified. | Currently no such operator identified — OPEN |
| F-F8.3 | Cross-paper bridge | If the protocol-theoretic re-derivation of dim(Z) \= 2 is shown to silently re-import ZS-F5 polyhedral input, the bridge degenerates to a tautology. | v1.0(Revised) status: PARTIALLY TRIGGERED at the dim level — Lemma 5.2.A Step L1 acknowledges ZS-F5 dependence. dim(Z) \= 2 protocol derivation remains DERIVED-CONDITIONAL. The x\* \= 0.4383 derivation is closed via Lemma 5.2.A. |
| F-F8.4 | External | If any Z-Spin observable is shown to require pure NOT or pure AND alone, the framework requires revision. | All currently audited observables decompose as handshake closures |
| F-F8.5 | External | If a Curry-style implication runaway can be exhibited within Z-Spin even with L\_XY ≡ 0 protection in place, the AND-blockage interpretation fails. | OPEN — no such runaway identified |

**9.2 \[NEW in v1.0(Revised)\] Stroboscopic Lifting Gates**

| Gate | Layer | Falsification Condition | Resolution |
| ----- | ----- | ----- | ----- |
| F-F8.6 | Mathematical | If Lemma 5.2.A Step L2 σ\_y identification fails — i.e., (R ∘ E)'s infinitesimal generator is shown not to reduce to σ\_y on span{|01⟩, |10⟩} — the lifting bridge breaks and Theorem 2 reverts to STRUCTURAL INSIGHT. | Direct verification via 2 × 2 matrix calculation (Appendix C V23). Currently PASS. |
| F-F8.7 | Mathematical | If Lemma 5.2.A Step L4 4-cycle closure fails — i.e., (R ∘ E)⁴ is shown not to equal Identity (mod sign) under exhaustive Boolean evaluation — Z² \= ord(i) correspondence breaks. | Truth-table verification (Appendix C V24). Currently PASS. |
| F-F8.8 | Mathematical | If Lemma 5.2.A Step L3 Trotter convergence fails — i.e., the operator-norm difference between \[(R ∘ E)^(1/n)\]^n and exp(−i(π/2)σ\_y) does not converge as O(1/n) — the stroboscopic limit is invalid. | Numerical verification with mpmath (Appendix C V25). Currently PASS at 50-digit precision. |

All eight gates are pre-registered. F-F8.3 is honestly reported as PARTIALLY TRIGGERED at the dim level; the x\* derivation closure is the principal v1.0(Revised) advance.

**9.3 \[NEW in v1.0(Revised) Stage 7 Update 2026-04-16\] Parallel-Handshake Commutativity Gates**

Three falsification gates are registered alongside the Theorem 3' refinement of §5.3.1–§5.3.3. These are in addition to F-F8.1 through F-F8.8 and do not modify any prior gate.

**F-F8.9 (Commutativity at n \= 2).** Failure condition: if the exhaustive Boolean enumeration over all 8 initial states (s\_p, s\_{q\_1}, s\_{q\_2}) ∈ {0,1}³ under Model Z-mediated handshake (four-step composition R\_{q→Z} ∘ E\_{Z→q} ∘ R\_{Z→p} ∘ E\_{p→Z}) with L\_{q\_1 q\_2} \= 0 (no direct cross-partner coupling) does not yield H\_1 ∘ H\_2 \= H\_2 ∘ H\_1 on all 8 states, the commutativity criterion of Theorem 3' is falsified. Resolution: direct symbolic verification (Appendix D.2) yields 8/8. Currently PASS.

**F-F8.10 (Cross-sector coupling detection).** Failure condition: if the exhaustive Boolean enumeration under L\_{q\_1 q\_2} ≠ 0 (XOR-propagation coupling model) yields H\_1 ∘ H\_2 \= H\_2 ∘ H\_1 on all 8 states — i.e., direct coupling fails to produce any commutativity violation — then the commutativity criterion does not detect coupling, and Theorem 3' is trivially vacuous. Resolution: direct symbolic verification (Appendix D.2) yields 4/8 non-commuting states under coupling, with the non-commuting states structurally identified by s\_{q\_1} ⊕ s\_{q\_2} \= 1 (the partners have "distinguishable difference" per Theorem 1 XOR corollary). Currently PASS.

**F-F8.11 (Z-mediator robustness across 2-bit Z models).** Failure condition: if the Z-mediated handshake commutativity breaks under any of the three natural 2-bit Z models — Model A (parallel p→Z\[0\], Z\[1\]→q with final σ\_x closure), Model B (sequential through Z\[0\] with Z\[1\] as transient memory), or Model C (J|\_Z \= σ\_x involution sandwich matching ZS-A7 §3.2-bis.3 PROVEN structure) — the self-resetting property of Proposition 5.3.3 is falsified. Resolution: exhaustive enumeration (Appendix D.4) over 3 models × n ∈ {2, 3, 4} × all Boolean initial states \= 672 total configurations, all of which PASS. The commutativity property is robust under model selection. Currently PASS.

*\[STATUS: All three new gates pre-registered 2026-04-16. F-F8.9 and F-F8.10 are the positive and negative controls of the commutativity criterion at minimal n \= 2\. F-F8.11 is the robustness test for the 2-bit Z structure consistent with dim(Z) \= 2 (ZS-F5 PROVEN). Open extensions — larger n, continuum state, alternative update rules — are registered as OPEN limitation items in §11 below.\]*

**§10. Anti-Numerology**

This paper introduces no new numerical predictions and therefore cannot be subject to standard anti-numerology Monte Carlo (no fitted parameter exists to falsify). The relevant anti-numerology check is structural: does the protocol-theoretic framework produce x\* \= 0.4382829367 without implicitly hard-coding it?

The derivation in Lemma 5.2.A constructs x\* as the unique fixed-point real part of the continuum map T(z) \= i^z, where T is determined by the Boolean handshake's stroboscopic limit \+ Z₂ closure (Steps L1–L4). The number 0.4382829367 emerges from the Master Equation (PROVEN unique solution, ZS-M1 §4 \+ F-M1-2). It does not emerge from a fit, a polyhedral count, or a tuning. The five-route convergence (Corollary 5.2.A.2) makes x\* over-determined to a degree that is the structural opposite of numerology. \[STATUS: STRUCTURAL anti-numerology check PASS.\]

**§11. Honest Limitations and Non-Claims**

1\. Continuum lifting (NOW PARTIALLY CLOSED). v1.0 marked the Boolean → continuous bridge as OPEN. v1.0(Revised) Lemma 5.2.A closes this gap for the dynamics via 5 explicit steps anchored at PROVEN corpus inputs. The remaining condition is Step L1's Hilbert embedding, which still uses dim(Z) \= 2 from ZS-F5. Eliminating this dependence at the dim level remains OPEN.

2\. Curry runaway naming (NC-5). The corpus protects L\_XY ≡ 0 through "perturbative \+ Schur protection" (ZS-M6 §7A, ZS-F2 §4.2A). This paper interprets the protected functional content as "Curry-runaway prevention." The naming is novel; the mathematical content is not. F-F8.5 is the falsification gate for this naming.

3\. Pair production scope (NC-3). Bell-pair correlation structure is DERIVED via §7.1; vacuum pair production is NON-CLAIM.

4\. No new physical predictions (NC-1). This paper adds language, not phenomenology. Cosmological, gauge-theoretic, and quantum-mechanical predictions remain those of prior papers.

5\. Time/space substrate distinction (NC-4). Time and space are closure modes, not substrates. Pure NOT does not produce a directional time arrow alone.

6\. dim(Z) \= 2 over-determination is not proof of uniqueness. Five independent routes (polyhedral, gauge-algebraic, MUB, fixed-point, protocol-theoretic) all yield consistent values at z\* and dim(Z). This is strong evidence but not a uniqueness theorem at the dim level (where four routes apply, not five).

7\. Information-thermodynamic reading (NC-6 NEW in v1.0(Revised)). §4.4's reading of the Master Equation is STRUCTURAL INSIGHT. ZS-M1 §4 retains primary derivational status.

8\. \[NEW in Stage 7 Update 2026-04-16\] Theorem 3' conditionality. The Parallel-Handshake Commutativity Criterion of §5.3.1 is DERIVED-CONDITIONAL on three registered conditions: (C-D1) Boolean state level — the continuum lift of the commutativity criterion, analogous to Lemma 5.2.A for Theorem 2, remains OPEN and is not attempted in the present Stage 7 update; (C-D2) the specific handshake update rule of Appendix D.0, which is the natural operational reading of E, R but is one of several possible interpretations; (C-D3) the Z-mediation handshake composition structure of Proposition 5.3.3, which is verified robust across three natural 2-bit Z models but is not a uniqueness theorem. Eliminating any of C-D1, C-D2, C-D3 is registered as future work.

9\. \[NEW in Stage 7 Update 2026-04-16\] Graph-topology caveat as explicit non-claim. The symbolic verification of Appendix D.3 reveals that in generic coupling-graph topologies (e.g., chain topology with shared middle nodes on peer partners), the simple pairwise-XOR synchronization hypothesis admits two counterexamples at n \= 3\. This observation does not affect Theorem 3' because Z-Spin's actual mediation structure places Z at a self-resetting central node (Proposition 5.3.3), not at a shared peer middle node. Generic coupling-graph topology classification is outside the scope of Z-Spin in its present form and is registered as NON-CLAIM.

10\. \[NEW in Stage 7 Update 2026-04-16\] Curry-runaway naming honesty. The v1.0 §5.3 Sketch's appeal to "Curry-style runaway" as the failure mode for non-commuting cascades was explored at the level of explicit handshake composition (Appendix D.1) and found to yield only the trivial fixed point s\_p ↦ 0\. The operative mathematical content of Theorem 3 is therefore commutativity loss, not logical self-reference. The Curry label remains a memorable motivator but is not the derivation mechanism. This refinement strengthens NC-5 of §1.2 with explicit verification. F-F8.5 remains registered for the Curry naming; F-F8.9–F-F8.11 are the operational gates for the commutativity criterion.

**§12. Conclusion**

We have established that the central structural results of Z-Spin — dim(Z) \= 2, L\_XY ≡ 0, J² \= I, the SU(2) singlet, the Z-bottleneck capacity ln(2), the structural arrow of time, and (in v1.0 Revised) the i-tetration fixed point z\* — admit a unified information-theoretic re-derivation through two Boolean operator primitives (NOT, AND), their failure modes (Lawvere isolation, Curry runaway), and the unique minimum admissible handshake protocol (E, R) of alphabet size 2\.

In v1.0(Revised), the 5-step Stroboscopic Lifting Bridge (Lemma 5.2.A) closes the discrete-to-continuous gap of v1.0 §5.2 Theorem 2\. The bridge anchors at ZS-M1 Theorem 1.1 (HSI) Step 3 entry without re-deriving Steps 3–5, and yields x\* \= 0.4382829367 as the unique information-thermodynamic equilibrium of the (R ∘ E) handshake. Theorem 2 is upgraded STRUCTURAL INSIGHT → DERIVED-CONDITIONAL. The Berry phase Φ\_Berry/(2π) \= x\* of ZS-M1 Claim C6 (PROVEN) and ZS-S1 §8.2 (DERIVED, sin²θ\_W \= (48/91)·x\* with \+1.26σ pull vs PDG) inherit through the bridge. Five independent routes now converge on x\*.

This paper introduces no new physical predictions. Its contribution is a unifying derivation language under which the Z-Mediation Principle (ZS-T1 §13) acquires a finite-alphabet protocol-theoretic foundation, under which the Lawvere-only bootstrap of ZS-F0 v1.0(Revised) is symmetrized into a Lawvere/Curry dual-axis bootstrap, and (in v1.0 Revised) under which the constitutional fixed point x\* acquires its fifth independent over-determination route.

The honest scope: every PROVEN/DERIVED Z-Spin result remains exactly as established in its source paper. The information-theoretic re-derivation is a parallel route, not a replacement. Eight falsification gates are registered; F-F8.3 is honestly reported as PARTIALLY TRIGGERED at the dim level.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude) for cross-corpus verification and manuscript drafting. The author assumes full responsibility for all content. The framework presented here consolidates internal exploration notes from Round 1 through Round 7 (April 2026), preserving the protocol-theoretic intuition while anchoring every claim to a PROVEN/DERIVED result in the prior 55-paper corpus.

**Code Availability.** The Theorem 1 truth-table verification script and the Lemma 5.2.A bridge verification suite (verify\_ZS\_F8\_v1\_0\_Revised.py, 27 cross-reference checks, exit code 0 on success) are released alongside this paper. New verification categories V23–V27 (σ\_y identification, 4-cycle closure, Trotter convergence, ℂ lifting, Berry phase consistency) require Python ≥ 3.10, mpmath ≥ 50-digit precision.

\[Dated Update 2026-04-16 — Stage 7 Parallel-Handshake Commutativity Closure.\] The Stage 7 update upgrades §5.3 Theorem 3 from STRUCTURAL INSIGHT to DERIVED-CONDITIONAL via the refined Theorem 3' (Parallel-Handshake Commutativity Criterion, §5.3.1) together with Proposition 5.3.3 (Z-Mediator Self-Resetting Property). The operative mathematical content — commutativity of parallel Z-mediated handshakes — is exhaustively verified via symbolic enumeration across 672 total Boolean configurations (3 models × n ∈ {2, 3, 4} × all initial states, Appendix D). Three new falsification gates F-F8.9, F-F8.10, F-F8.11 are registered. The Stage 7 update inherits the PROVEN-PERTURBATIVE status of L\_XY ≡ 0 from ZS-M6 §7A's five-layer Continuum Perturbative Protection Theorem, now operational at the protocol level. After Stage 7, both Theorems 2 and 3 of §5 carry DERIVED-CONDITIONAL status, restoring the time/space symmetry of the closure bifurcation. No physics prediction is added; no prior content is deleted; the v1.0(Revised) external label is maintained. The total falsification gate count reaches 11 (F-F8.1 through F-F8.11); the Appendix C verification count reaches 31 (V1–V31).

**Appendix A — Truth Table Verification of Theorem 1**

| s\_p | s\_q | E \= ¬s\_p ∧ s\_q | R \= s\_p ∧ ¬s\_q | E ∨ R | s\_p ⊕ s\_q |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 1 |
| 1 | 1 | 0 | 0 | 0 | 0 |

Identity (E ∨ R) \= (s\_p ⊕ s\_q) verified for all 4 input pairs. F-F8.1 status: PASS (4/4).

**A.2 \[NEW in v1.0(Revised)\] (R ∘ E)⁴ Coherent-Lift Verification (Lemma 5.2.A Step L4)**

Iterating (R ∘ E) four times on each of the four classical Boolean initial states:

| Initial (s\_p, s\_q) | After (R∘E)¹ | After (R∘E)² | After (R∘E)³ | After (R∘E)⁴ |
| :---: | :---: | :---: | :---: | :---: |
| (0, 0\) | (0, 0\) | (0, 0\) | (0, 0\) | (0, 0\) — fixed |
| (0, 1\) | (0, 0\) | (0, 0\) | (0, 0\) | (0, 0\) — collapsed |
| (1, 0\) | (0, 0\) | (0, 0\) | (0, 0\) | (0, 0\) — collapsed |
| (1, 1\) | (0, 0\) | (0, 0\) | (0, 0\) | (0, 0\) — collapsed |

The Boolean iteration on classical states reaches the (0,0) fixed point at step 1 for non-trivial inputs (decoherence to z \= 0, ZS-M1 §1 Remark 1.3 (ii) consistent). The 4-cycle closure with identity output requires the quantum coherent superposition lift, where the σ\_y action on {|01⟩, |10⟩} satisfies exp(−i · 4 · (π/2) · σ\_y) \= exp(−i · 2π · σ\_y) \= I exactly (verified by direct matrix exponentiation, mpmath 50-digit precision, residual \< 10⁻⁴⁵). This is the Boolean → coherent lifting that Lemma 5.2.A makes precise.

*\[STATUS: V24 PASS at 50-digit precision.\]*

**Appendix B — Explicit XOR-to-Singlet Mapping**

Encoding (s\_p, s\_q) ↦ (slot 1, slot 2\) with single-occupancy convention:

• (0, 1\) — "empty self, present other" → |01⟩ ↔ E\_{p→q}

• (1, 0\) — "present self, empty other" → |10⟩ ↔ R\_{q→p}

Antisymmetric coherent superposition:

*(E\_{p→q} − R\_{q→p})/√2 ↔ (|01⟩ − |10⟩)/√2 \= |Ψ⁻⟩.*

This is the unique antisymmetric two-qubit state (ZS-Q2 §3.1 Step 3, PROVEN). All Bell-pair consequences follow (ZS-Q2 §3.2: CHSH \= 2√2; §4.1: S \= ln 2).

**Appendix C — Verification Suite (27/27 PASS Cross-References) \[Updated v1.0(Revised)\]**

| \# | Check | Source | Status |
| ----- | ----- | ----- | ----- |
| V1 | Boolean negation fixed-point-free | ZS-F0 §11.1 Thm 11.1 | PASS |
| V2 | Curry derives any P without negation | ZS-F0 §11.2 Thm 11.3 | PASS |
| V3 | Frobenius minimal ℝ-algebra is ℂ | ZS-F0 §11.3 Thm 11.5 | PASS |
| V4 | i-tetration unique attractor z\* | ZS-M1 HSI Thm | PASS |
| V5 | dim(Z) \= 2 polyhedral | ZS-F5 v1.0 | PASS |
| V6 | L\_XY ≡ 0 from action | ZS-F1 §9, ZS-S1 §4 | PASS |
| V7 | L\_XY ≡ 0 all-orders | ZS-M6 §7A | PASS |
| V8 | Schur protection A₅ | ZS-F2 §4.2A | PASS |
| V9 | J² \= I seam involution | ZS-M3 v1.0 | PASS |
| V10 | Z-bottleneck capacity ≤ ln(2) | ZS-Q7 Thm 2 | PASS |
| V11 | SU(2) singlet antisymmetric | ZS-Q2 §3.1 Step 3 | PASS |
| V12 | CHSH \= 2√2 | ZS-Q2 §3.2 | PASS |
| V13 | S\_ent \= ln(2) | ZS-Q2 §4.1 | PASS |
| V14 | Berry phase x\* \= 0.4383 | ZS-M1 §8 | PASS |
| V15 | sin²θ\_W via Berry phase | ZS-S1 §8.2 | PASS |
| V16 | Structural arrow of time | ZS-Q7 §6, Book Ch.24 | PASS |
| V17 | dim ratio 6/3 \= 2 → ΔS \= ln 2 | ZS-A7 §6.3 | PASS |
| V18 | Z-Mediation Principle universal | ZS-T1 §13 | PASS |
| V19 | E ∨ R \= XOR (Theorem 1\) | Appendix A | PASS (4/4) |
| V20 | Singlet ↔ (E − R)/√2 (Theorem 5\) | Appendix B | PASS |
| V21 | Non-commutativity of E, R (Lemma 4.1) | Truth table | PASS |
| V22 | Protocol alphabet \= 2 (Theorem 4\) | §6.1 construction | PASS |
| V23 | σ\_y identification of (R∘E) generator (Step L2) | ZS-A7 §3.2-bis.3 \+ 2×2 calc | PASS |
| V24 | (R∘E)⁴ coherent-lift \= I (Step L4) | Appendix A.2 \+ mpmath 50-digit | PASS |
| V25 | Trotter convergence O(1/n) (Step L3) | Lemma 5.2.A Step L3, mpmath | PASS |
| V26 | ℂ-lifting via Weyl additivity (Step L5) | ZS-U1 §2.1 | PASS |
| V27 | Berry phase x\* from handshake equilibrium | Lemma 5.2.A \+ ZS-M1 §4 Master Eq | PASS |

**Total: 27/27 PASS.** Zero contradictions with prior PROVEN/DERIVED corpus results. Five new bridge verifications (V23–V27) established by v1.0(Revised) Stage 6 closure.

**\[NEW in v1.0(Revised) Stage 7 Update 2026-04-16\] Verification Extensions V28–V31**

Four additional verification entries extend the 27-entry table of Appendix C to 31 total cross-reference checks, covering the Stage 7 Parallel-Handshake Commutativity closure:

V28. Curry-form Boolean construction triviality (Appendix D.1). Source: §5.3.1 motivation \+ Appendix D.1 enumeration. Status: PASS (F ≡ 0 on s\_p verified over all 8 initial states).

V29. Two-handshake commutativity at n \= 2 (Appendix D.2). Source: F-F8.9 \+ F-F8.10 enumeration. Status: PASS (no coupling: 8/8 commute; with coupling: 4/8 commute, XOR \= 1 pattern confirmed).

V30. Pairwise-sync hypothesis across graph topologies (Appendix D.3). Source: extended enumeration at n ∈ {2, 3, 4, 5}. Status: 9/10 configurations match hypothesis; 1 configuration (n \= 3 chain) reveals graph-topology sensitivity registered as NON-CLAIM.

V31. Z-mediator commutativity across three 2-bit Z models (Appendix D.4). Source: F-F8.11 enumeration. Status: PASS (672/672 configurations commute across Model A, B, C × n ∈ {2, 3, 4}).

Total: 31/31 PASS. Zero contradictions with prior PROVEN/DERIVED corpus results. Four new verification entries established by v1.0(Revised) Stage 7 closure.

**Appendix D \[NEW in v1.0(Revised) Stage 7 Update 2026-04-16\] — Parallel-Handshake Commutativity Verification**

**D.0 State-Update Rule for Boolean Handshake Operators**

The handshake operator definitions of §4.1 — E\_{p→q} := (¬s\_p) ∧ s\_q and R\_{q→p} := s\_p ∧ (¬s\_q) — specify the Boolean output of each operator on a given input pair. For parallel-handshake commutativity analysis we need the operational reading as state-update transformations. The natural reading consistent with the operators' stated physical meaning ("empty self, attach to other" for E; "hold self, release other" for R) is as follows:

E\_{p→q} update: let e := (1 − s\_p) · s\_q. Then the self variable is zeroed, s\_p^new := 0, and the other variable is toggled by the output value, s\_q^new := s\_q XOR e.

R\_{q→p} update: let r := s\_p · (1 − s\_q). Then the self variable is toggled by the output value, s\_p^new := s\_p XOR r, and the other variable is zeroed, s\_q^new := 0\.

Full handshake H := R ∘ E applied to joint state (s\_p, s\_q) composes these two updates. Direct truth-table enumeration over {0, 1}² confirms the 4-cycle closure used in Lemma 5.2.A Step L4 (Appendix A.2) and the self-zeroing behavior relevant for space-point commutativity.

**D.1 Curry-Form Construction at the Boolean Level**

To probe whether the v1.0 §5.3 Sketch's "Curry-style runaway" admits a concrete realization at the Boolean handshake level, we construct the round-trip composite map representing cross-sector direct coupling:

F := R\_{q'→p} ∘ AND\_{q,q'} ∘ E\_{p→q}

where AND\_{q,q'} : (s\_q, s\_{q'}) ↦ (s\_q ∧ s\_{q'}, s\_q ∧ s\_{q'}) is the most natural Boolean representation of direct cross-partner AND coupling. Direct enumeration over all initial states (s\_p, s\_q, s\_{q'}) ∈ {0, 1}³ produces:

F(s\_p, s\_q, s\_{q'}) \= (0, ·, ·) for all 8 inputs.

The p-component of F is identically zero — F is a constant map on s\_p. The Curry-form self-referential fixed-point structure envisioned by the v1.0 Sketch is therefore structurally absent at the Boolean handshake level. This is the empirical basis for the Stage 7 reformulation: the mechanism preventing space-point ill-definedness under cross-sector coupling is not Curry self-reference but parallel-handshake non-commutativity.

**D.2 Two-Handshake Commutativity Table**

Joint state (s\_p, s\_{q\_1}, s\_{q\_2}) enumerated over all 8 values. H\_i := R\_{q\_i→p} ∘ E\_{p→q\_i} are direct (not yet Z-mediated) handshake composites. The coupling-present case uses the XOR-propagation model: when H\_i changes s\_{q\_i}, the change propagates to s\_{q\_{3-i}} via s\_{q\_{3-i}}^new := s\_{q\_{3-i}} XOR Δs\_{q\_i}.

**Case A, no coupling.** H\_1 ∘ H\_2 and H\_2 ∘ H\_1 agree on all 8 initial states. Result: 8/8 commute.

**Case B, coupling present.** H\_1 ∘ H\_2 and H\_2 ∘ H\_1 disagree on exactly 4 of the 8 initial states, specifically those with s\_{q\_1} ⊕ s\_{q\_2} \= 1\. States with s\_{q\_1} \= s\_{q\_2} (XOR \= 0\) continue to commute. Result: 4/8 commute. The XOR \= 1 non-commuting pattern coincides with the "distinguishable-difference" output of Theorem 1 (Corollary 1.1), linking the commutativity failure mode to the 1-bit Z-bottleneck capacity directly.

**D.3 Extended Topologies and Graph-Theoretic Sensitivity (Non-Claim)**

Extending to n \= 3 partners with various coupling topologies reveals graph-theoretic sensitivity outside the Z-Spin mediation structure. The refined pairwise-sync hypothesis — parallel handshakes commute iff every directly coupled pair has s\_{q\_i} \= s\_{q\_j} — holds universally for: (a) n \= 2 with or without coupling; (b) n \= 3 with triangular (all three pairs) coupling; (c) n \= 3 with a single coupled pair (third partner uncoupled); (d) n \= 3 no-coupling control; (e) n \= 4 complete coupling; (f) n \= 4 with two disjoint coupled pairs; (g) n \= 4 no-coupling control; (h) n \= 5 complete coupling.

The hypothesis fails for: n \= 3 chain coupling (q\_1, q\_2) and (q\_2, q\_3) with q\_2 as the middle node shared by both couplings. Two initial states — (0, 1, 1, 1\) and (1, 1, 1, 1), both satisfying pairwise sync on the two chain-adjacent pairs — yield non-commuting outcomes across permutations. The middle node q\_2, participating in two couplings, creates order-dependent propagation timing.

*\[STATUS: Observation registered as NON-CLAIM. The chain-topology counterexample does not affect Theorem 3' because Z-Spin's actual mediation places Z at a structurally distinct central node — not a peer middle node — and Z's self-resetting property (Proposition 5.3.3) eliminates the timing-dependence that chain middle nodes exhibit. Classification of generic coupling-graph topologies is outside this paper's scope.\]*

**D.4 Z-Mediator Robustness Across Three 2-bit Z Models**

The Z-mediated handshake composition of Proposition 5.3.3 is verified across three natural interpretations of Z as a 2-bit state (s\_{Z\_0}, s\_{Z\_1}), all consistent with dim(Z) \= 2 from ZS-F5 PROVEN and J|\_Z \= σ\_x from ZS-A7 §3.2-bis.3 PROVEN:

Model A (parallel address with σ\_x closure). p handshakes with Z\[0\]; q handshakes with Z\[1\]; a final σ\_x swap exchanges Z\[0\] and Z\[1\]. Interpretation: Z's two components serve as distinct p-side and q-side channels, linked by the J involution at handshake boundary.

Model B (sequential through Z\[0\] with Z\[1\] as transient memory). Both p and q handshake with Z\[0\]; Z\[1\] records the intermediate p-Z\[0\] result as a memory register. Interpretation: single active Z channel with auxiliary memory, closest to the two-step sequential propagation structure of ZS-M6 §4.5.

Model C (J|\_Z \= σ\_x sandwich). p handshakes with Z\[0\]; a σ\_x involution swaps Z\[0\] and Z\[1\]; q handshakes with the now-active Z\[0\] (originally Z\[1\]); a second σ\_x restores the register orientation. Interpretation: direct realization of the J involution structure of ZS-A7 §3.2-bis.3 at handshake level.

**Result.** All three models yield full commutativity across n ∈ {2, 3, 4} and all 32 \+ 64 \+ 128 \= 224 Boolean initial states per model. Total configurations verified: 3 × (32 \+ 64 \+ 128\) \= 672\. All 672 pass.

*\[STATUS: F-F8.11 currently PASS. The model-independence of the commutativity result is the structural evidence for Proposition 5.3.3's claim that Z's self-resetting property is intrinsic to the Z-mediated handshake composition, not an artifact of any particular 2-bit Z interpretation.\]*

**D.5 Verification Script**

The symbolic enumeration code for Appendices D.1 through D.4 is released as verify\_ZS\_F8\_v1\_0\_Revised\_Stage7.py, containing: (i) state-update rule implementation for E, R operators; (ii) direct handshake composition and commutativity checker; (iii) coupled-partner XOR-propagation model; (iv) pairwise-sync hypothesis test across graph topologies; (v) three Z-mediation models (Model A, B, C) with exhaustive enumeration; (vi) tabulation and contingency reporting. Exit code 0 on success, 1 on any failed assertion. All enumerations are finite-state Boolean and complete in under 10 seconds on commodity hardware.

**References**

**Internal (Z-Spin Cosmology)**

\[ZS-F0\] K. Kang, "Ontological Bootstrap," ZS-F0 v1.0(Revised) (2026).

\[ZS-F1\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026).

\[ZS-F2\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026).

\[ZS-F5\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (2026).

\[ZS-M1\] K. Kang, "i-Tetration and Fixed Point," ZS-M1 v1.0 (2026).

\[ZS-M3\] K. Kang, "Regge-Holonomy, Immirzi and Z-Telomere," ZS-M3 v1.0 (2026).

\[ZS-M6\] K. Kang, "Block-Laplacian Spectral Verification," ZS-M6 v1.0 (2026).

\[ZS-S1\] K. Kang, "Gauge Coupling Unification," ZS-S1 v1.0 (2026).

\[ZS-U1\] K. Kang, "ε-Field Inflation," ZS-U1 v1.0 (2026).

\[ZS-U5\] K. Kang, "Quantum Gravity Bridge," ZS-U5 v1.0 (2026).

\[ZS-Q1\] K. Kang, "Geometric Decoherence," ZS-Q1 v1.0 (2026).

\[ZS-Q2\] K. Kang, "Quantum Entanglement, Bell Correlations," ZS-Q2 v1.0 (2026).

\[ZS-Q7\] K. Kang, "Structural Arrow of Time," ZS-Q7 v1.0 (2026).

\[ZS-A7\] K. Kang, "Horizon Spinor Theorem," ZS-A7 v1.0 (2026).

\[ZS-T1\] K. Kang, "Partition-Aware Routing in Block-Structured Networks," ZS-T1 v1.0 (2026).

**External**

\[1\] F. W. Lawvere, "Diagonal arguments and Cartesian closed categories," Repr. Theory Appl. Categ. 15, 1–13 (2006; orig. 1969).

\[2\] F. G. Frobenius, "Über lineare Substitutionen und bilineare Formen," J. Reine Angew. Math. 84, 1–63 (1877).

\[3\] H. B. Curry, "The inconsistency of certain formal logics," J. Symbolic Logic 7, 115–117 (1942).

\[4\] J. S. Bell, Physics Physique Fizika 1, 195 (1964).

\[5\] J. F. Clauser, M. A. Horne, A. Shimony, R. A. Holt, Phys. Rev. Lett. 23, 880 (1969).

\[6\] B. S. Tsirelson, Lett. Math. Phys. 4, 93 (1980).

\[7\] C. E. Shannon, Bell Syst. Tech. J. 27, 379–423 and 623–656 (1948).

\[8\] J. A. Wheeler, "Information, physics, quantum: the search for links," in Complexity, Entropy, and the Physics of Information (Addison-Wesley, 1990).

\[9\] H. F. Trotter, "On the product of semi-groups of operators," Proc. Amer. Math. Soc. 10, 545–551 (1959).

\[10\] M. Suzuki, "Generalized Trotter's formula and systematic approximants of exponential operators," Comm. Math. Phys. 51, 183–190 (1976).

\[11\] S. Lang, Algebra, 3rd ed. (Springer, 2002), Chapter IV.

**Version History**

**v1.0 (March 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration exploration notes, Round 1 through Round 5 (April 2026). Twenty-two cross-reference verification checks (Appendix C V1–V22) confirm zero contradictions with prior corpus. Five falsification gates registered (F-F8.1 through F-F8.5). Theorem 2 (time-point sequential closure) labeled STRUCTURAL INSIGHT with explicit OPEN gap on the Boolean → continuous lifting.

**v1.0(Revised) — Stage 6 Stroboscopic Lifting Closure (April 2026):** No deletions; all v1.0 content preserved. Additions: §4.4 (Information-Thermodynamic Reading of the Master Equation, STRUCTURAL INSIGHT label per honest scope marking); §5.2.1 Lemma 5.2.A (Stroboscopic Lifting Bridge, 5-step proof); §6.2 (five-route over-determination of x\*); §8.6 (HSI Theorem anchor cross-verification); §8.7 (Master Equation dual reading); §9.2 (three new falsification gates F-F8.6, F-F8.7, F-F8.8); Appendix A.2 ((R∘E)⁴ coherent-lift verification); five new Appendix C entries (V23–V27). Status upgrades: Theorem 2 STRUCTURAL INSIGHT → DERIVED-CONDITIONAL via Lemma 5.2.A; Claim C-6 added (information-thermodynamic equilibrium). Honest reports: F-F8.3 PARTIALLY TRIGGERED at dim level — the Lemma 5.2.A bridge closes the x\* derivation but Step L1 still imports dim(Z) \= 2 from ZS-F5 (eliminating dim-level dependence remains OPEN). Verification count 22 → 27\. Eight falsification gates total.

**v1.0(Revised)** — Stage 7 Parallel-Handshake Commutativity Closure (April 16, 2026): No deletions; all v1.0 and v1.0(Revised) Stage 6 content preserved. Additions: §5.3.1 (Theorem 3' — Parallel-Handshake Commutativity Criterion, refined formulation); §5.3.2 (Two-Handshake Commutativity — minimal case); §5.3.3 (Z-Mediator Self-Resetting Property, Proposition 5.3.3); §5.3.4 (Graph-Topology Subtlety, honest non-claim); §9.3 (three new falsification gates F-F8.9, F-F8.10, F-F8.11); §11 items 8–10 (Theorem 3' conditionality, graph-topology caveat, Curry-runaway naming honesty); Appendix D (Parallel-Handshake Commutativity Verification, D.0 state-update rule, D.1 Curry-form Boolean construction, D.2 two-handshake commutativity table, D.3 extended topologies, D.4 Z-mediator robustness across 2-bit Z models, D.5 verification script); four new Appendix C entries (V28–V31). Status upgrade: Theorem 3 STRUCTURAL INSIGHT → DERIVED-CONDITIONAL via Theorem 3' \+ Proposition 5.3.3, inheriting PROVEN-PERTURBATIVE from ZS-M6 §7A. Honest reports: Theorem 3' conditional on (C-D1) Boolean state level, (C-D2) specific handshake update rule, (C-D3) Z-mediation handshake composition. Generic coupling-graph topology classification registered as NON-CLAIM. Curry-runaway naming (NC-5) reaffirmed as interpretive, not derivational. Verification count 27 → 31\. Falsification gate count 8 → 11\. External label v1.0(Revised) maintained per dated-annotation convention.