# ZS-Q14

# Canonical Kraus-Lift Selection by a Spin-1/2 Boundary

## 

## From Choi-Invisibility to Process-Level Falsification in Z-Spin Boundary Mediation

**Kenny Kang** June 2026 Theme: Quantum Channel Geometry / Quantum Mechanics / Quantum Hardware Interface | Paper Code: ZS-Q14 Version: v1.4 (supersedes v1.3)

**Verification Summary:** zs\_q14\_verify\_v1\_4.py — **33/33 PASS** across categories A–I (= the v1.3 suite's 30/30 plus a new Category I verifying the Boundary Spin-Lift Lemma). Central witness inherited verbatim from ZS-A7R Eq. (F.2) \[34/34 PASS\]. Zero new theoretical constants. **Status:** TESTABLE-PROTOCOL / DERIVED-CONDITIONAL / VERIFIED-SIM / HARDWARE-PENDING **Primary Claim:** A quantum channel alone does **not** determine a physical Kraus lift (Choi-invisibility No-Go \+ single-channel non-identifiability — both established and verified). If the Z-boundary physically carries the nontrivial (spinor) projective class of SO(3) — i.e. dim Z \= 2 \= *j* \= 1/2 (ZS-M3 Thm 5.1; Z \= ∂X, ZS-Q12) — then the half-angle SU(2) connection is *forced* (Lemma 5.1, Boundary Spin-Lift), giving closure class χ\_Z \= −1. The signed lift witness ũ\_Z(θ) is a *process/dilation-level* observable, ũ\_Z \= F(V, G\_Z, φ\_Z) ≠ f(Λ), that kills (χ\_Z \= \+1) or survives (χ\_Z \= −1) this selection principle. Necessary-not-sufficient; **not** a new general theorem (the bundle/holonomy/No-Go/representation-theory results are prior art).

---

# §0. Abstract

A completely positive trace-preserving (CPTP) channel is represented by Kraus operators only up to a unitary gauge freedom K\_a ↦ Σ\_b U\_ab K\_b, U ∈ U(r), and the Choi/Jamiołkowski matrix is the gauge-invariant that fixes the channel. We organize ZS-Q14 around a question meaningful to general quantum-information theory: **when does one lift of the Kraus gauge freedom cease to be a mere representation choice and become physical structure?**

Two facts bound the answer, and both are established or directly verified rather than claimed as new. (i) **Channel-Level Invisibility (No-Go, Theorem 1):** any function of the channel alone is invariant under closed loops in the Kraus-gauge fiber, so it cannot distinguish a 2π from a 4π closure; this is the gauge-invariance of the Choi matrix. (ii) **Single-Channel Non-Identifiability (Theorem 2):** the *same* channel yields closure class χ \= −1 under a half-angle lift U₁/₂(θ) \= e^{−iθσ\_y/2} and χ \= \+1 under a full-angle lift U₁(θ) \= e^{−iθσ\_y}; the 4π is **injected by the chosen lift, not intrinsic** (verified to machine precision).

The contingent content is therefore not "one can see 4π" (textbook spinor/holonomy physics; Werner–Colella–Overhauser 1975, read as channel holonomy by Kult, Åberg & Sjøqvist 2007\) but a **lift-selection criterion** (§4), and — new in v1.4 — a representation-theoretic ground for it. The **Boundary Spin-Lift Lemma** (Lemma 5.1) states that if the two-dimensional Z-boundary carries a faithful projective representation of SO(3) in the nontrivial class of H²(SO(3), U(1)) ≅ ℤ₂ (whose nontrivial 2π loop acts as −I), then the induced Kraus-frame connection is forced to be the half-angle generator G \= σ\_y/2 up to conjugation and orientation, whence χ\_Z \= −1. This upgrades the criterion's connection condition (C3) from an independent assumption to a consequence of the premise that the Z-boundary is a physical spinor — exactly the Z-Spin postulate (dim Z \= 2 \= *j* \= 1/2; Z \= ∂X). We are explicit that the lemma is elementary representation theory (the spin-½ representation is its canonical instance); its role is to tighten the paper's logic, not to claim new mathematics.

Z-Spin is thus a **candidate** lift-selector whose spinor-boundary postulate supplies the half-angle connection (§5). The signed lift witness ũ\_Z(θ) \= Re Tr\[K₀(0)† K₀(θ)\]/‖K₀(0)‖*F² (ZS-A7R Eq. F.2) and the closure class χ\_Z \= sgn\[ũ\_Z(2π)/ũ\_Z(0)\] are the operational objects (§6). Crucially, ũ\_Z is **not a channel observable** — it is gauge-dependent — but a process/comb-level observable: with Λ \= Tr\_Z ∘ U\_XZ, one has ũ\_Z(θ) ≠ f(Λ) and ũ\_Z(θ) \= F(Υ*{2:0}, G\_Z, R\_Z) \= F(V, G\_Z, φ\_Z), where V is the Stinespring isometry, G\_Z \= σ\_y/2 the selected connection, and φ\_Z the environment phase reference exposed by the process tensor/comb Υ\_{2:0} but discarded by the channel marginal Λ (§7). The witness is read on the X-block of the OAQEC algebra M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ), the Z-block being a scalar gauge subsystem (§8).

The experiment (§9) is a near-term, pre-registered, kill-or-survive test: χ\_Z \= \+1 refutes the spin-½ lift-selection, χ\_Z \= −1 with the three load-bearing controls null is a *necessary* success. The same formalism applies to a second, independent physical channel — the hydrogenic hyperfine transition and its H / anti-H / muonium / positronium extensions (§10) — making ZS-Q14 a physical-channel-geometry program, not a single-circuit proposal.

**Keywords:** Kraus-gauge bundle, lift selection, boundary spin-lift, projective SO(3) representation, channel holonomy, Choi/Jamiołkowski invariance, process tensor/comb, signed seam witness, closure class, spin-1/2 boundary, Z-Spin Cosmology, falsification test.

---

# §0.1 Epistemic Status Legend

| Status | Definition |
| :---- | :---- |
| PROVEN | Theorem inherited from prior Z-Spin papers or standard mathematics. |
| ELEMENTARY-KNOWN | True and provable here, already standard externally; stated only to locate the construction. |
| DERIVED | Follows from the Z-Spin action plus locked prior results, no new constants. |
| DERIVED-CONDITIONAL | Derived under a stated physical postulate (here: Z \= ∂X / Z a physical spinor boundary). |
| CRITERION | A definition of when a contingent condition is taken to hold; not itself a derived theorem. |
| POSITION | A framing/localization statement, true and clarifying, not claimed as a new theorem. |
| TESTABLE-PROTOCOL | Concrete hardware experiment with pass/fail gates; not yet executed. |
| VERIFIED-SIM | Confirmed by classical simulation (zs\_q14\_verify\_v1\_4.py, inherited ZS-A7R suite). |
| HARDWARE-PENDING | Requires quantum-device execution. |
| CONTROL (load-bearing) | Negative experiment that *is* diagnostic. |
| CONTROL (non-diagnostic) | Negative experiment that, on analysis, does *not* separate the hypotheses. |
| NON-CLAIM | Explicitly not asserted. |
| OPEN | Well-posed unresolved issue. |
| RETRACTED | Previously circulated claim withdrawn. |

---

# §0.2 Position Statement

This paper's thesis is a **position**, not a new theorem: *a quantum channel does not determine a physical Kraus lift, but a physical boundary theory may.* The channel-holonomy field already operates under this fact — it introduces connections precisely because channels alone do not fix a holonomy (Uhlmann 1986; Kult, Åberg & Sjøqvist 2007). Z-Spin's contribution is a **specific candidate connection** (a spin-½ boundary), an experiment that kills or confirms it, and — in v1.4 — a representation-theoretic statement (Lemma 5.1) showing the half-angle connection is forced *given* that the boundary is a physical spinor.

This paper does **not** claim: a new general theorem about quantum channels; that the 4π closure is intrinsic to any channel (it is injected, §3); that ũ\_Z is a channel observable (it is gauge-dependent / process-level, §6–§7); that Lemma 5.1 is new mathematics (it is elementary representation theory, §5); any new quantum-computing algorithm, code, or primitive (the measurement is the standard Hadamard test); or that current hardware realizes the Z-sector. The one positive content is conditional: *if the Z-boundary is a physical spinor (the Z-Spin postulate), the half-angle lift is forced and ũ\_Z exhibits χ\_Z \= −1; a 2π closure on hardware refutes the selection.* The positive outcome is **necessary but not sufficient** for the full framework.

---

# §1. The Lift-Selection Problem

In standard quantum-information theory the Kraus representation carries a U(r) redundancy; the Choi/Jamiołkowski matrix is the gauge-invariant physical object. The channel-holonomy program (Kult, Åberg & Sjøqvist 2007), linked to Uhlmann's (1986) mixed-state holonomy via the Jamiołkowski isomorphism, studies the geometry of the Kraus → CPTP map and identifies a gauge-*invariant* holonomy as physical; the process-tensor framework (Pollock et al. 2018; Chiribella, D'Ariano & Perinotti 2009\) carries more system–environment information than a single channel.

Against this backdrop the organizing question is:

**When is a particular lift of the Kraus gauge freedom not a representation choice but physical structure?**

The honest answer has three parts. The negative parts are established or verified (§3): a channel alone *cannot* select a lift (No-Go), and the *same* channel admits both a 2π and a 4π lift (non-identifiability). The constructive part (§4–§5) is a *criterion* sharpened by a representation-theoretic *lemma*: a physical theory whose boundary carries the nontrivial spinor class of SO(3) forces the half-angle connection (Lemma 5.1) and, with an accessible dilation and bypass exclusion, selects the half-angle lift physically. Z-Spin is a candidate that supplies these via its spin-½ boundary. The experiment (§9–§10) tests that candidate.

---

# §2. The Minimal Kraus Frame Bundle

**Definition 1 (Minimal Kraus frame bundle).** For a channel Λ of Kraus rank r, P\_Λ \= { (K₀, …, K\_{r−1}) : Σ\_a K\_a† K\_a \= I,  Λ(ρ) \= Σ\_a K\_a ρ K\_a† } . Any two minimal frames are related by the gauge action (K\_a) ↦ (Σ\_b U\_ab K\_b), U ∈ U(r); P\_Λ is a U(r)-torsor (a fiber). The assignment (frame) ↦ Λ is the bundle projection of Kult, Åberg & Sjøqvist (2007), with base invariant the Choi matrix C\_Λ \= Σ\_a |K\_a⟩⟩⟨⟨K\_a|. \[ELEMENTARY-KNOWN\]

For r \= 2 the fiber is U(2); a *lift* is a path γ(θ) ∈ P\_Λ generated by K̇(θ) \= −iG K(θ) for a generator G ∈ u(2) (a *connection*). Which connection, if any, is physically selected is the question of §1.

---

# §3. Choi-Invisibility and Single-Channel Non-Identifiability

**Theorem 1 (Channel-Level Invisibility No-Go) \[ELEMENTARY-KNOWN\].** Any function f(Λ) of the channel alone — any process-tomography observable — is invariant under the entire U(r) fiber, in particular under any closed loop θ ↦ U(θ). Hence no channel observable distinguishes a Kraus-fiber loop's 2π from 4π closure. *Proof.* Under K\_a ↦ Σ\_b U\_ab K\_b, C\_Λ ↦ Σ\_{b,c}(U†U)\_{cb}|K\_b⟩⟩⟨⟨K\_c| \= C\_Λ.  (Verified to 3.3 × 10⁻¹⁶; suite Category C.)

**Theorem 2 (Single-Channel Non-Identifiability) \[DERIVED \+ VERIFIED-SIM\].** Fix Λ. The closure class χ \= sgn\[ũ(2π)/ũ(0)\] is **not** a function of Λ: under G \= σ\_y/2 it is −1 (period 4π), under G \= σ\_y it is \+1 (period 2π). The 4π is a property of the *chosen lift*. Equivalently the twist is a gauge no-op (Λ\_θ \= Λ) and ũ is gauge-dependent. *Proof.* Half-angle: U(2π) \= −I ⇒ ũ(2π) \= −ũ(0). Full-angle: U(2π) \= \+I ⇒ ũ(2π) \= \+ũ(0).  (Verified: Category E — Λ\_θ(ρ) \= Λ(ρ) to 2.3 × 10⁻¹⁶; r\_half \= −1, r\_full \= \+1; ũ gauge-dependent.)

Theorem 2 forecloses any claim that the channel "hides" a 4π. This is what makes the constructive content of §4–§5 honest rather than numerological.

---

# §4. The Physical Kraus-Lift Selection Criterion

We *define* when a lift is physically selected; we do not derive that any particular channel must be.

**Criterion 4.1 (Physical lift selection) \[CRITERION\].** A connection G on the minimal frame bundle P\_Λ of a rank-2 channel is *physically selected* when all four hold: **(C1) Minimal rank.** r \= rank C\_Λ \= dim Z \= 2\. **(C2) Accessible dilation.** In a Stinespring dilation V : H\_X → H\_X ⊗ H\_Z, the environment H\_Z carries an experimentally accessible phase reference (the Kraus index is a controllable boundary degree of freedom). **(C3) Fixed connection.** The half-angle generator G \= σ\_y/2 is fixed (K̇(θ) \= −i(σ\_y/2) K(θ)). *— In v1.4 this is supplied by Lemma 5.1 below, not assumed.* **(C4) Bypass exclusion.** The direct X→Y path is absent or removed by load-bearing controls.

**Proposition 4.1 (Closure-Class Connection-Invariance) \[DERIVED \+ VERIFIED-SIM\].** Given a fixed connection (C3), χ\_Z is independent of the residual U(2) gauge (the Kraus-frame anchor): χ\_Z \= −1 for the half-angle generator and \+1 for the full-angle generator, for *every* anchor. Hence χ\_Z is a function of the connection, not of the gauge. *Proof.* Under G \= σ\_y/2, U(2π) \= −I gives K₀(2π) \= −K₀(0) for any anchor, so ũ\_Z(2π) \= −ũ\_Z(0); under G \= σ\_y, χ\_Z \= \+1.  (Verified: Category F — NC2, 2000 anchors, all −1 \= anchor-independence; Category E — connection-dependence.)

**Honest boundary.** Criterion 4.1 is not a theorem and Proposition 4.1 is modest: its substance — *a connection promotes a gauge-dependent holonomy to a connection-relative invariant* — is the channel-holonomy framework of Kult, Åberg & Sjøqvist (2007), building on Uhlmann (1986). What the criterion buys is clarity about which contingent inputs make the lift physical, hence exactly what the experiment falsifies.

---

# §5. Z-Spin as a Candidate Spin-1/2 Lift Selector

**Definition 2 (Z-Spin lift selector).** Σ\_Z : (Λ, H\_Z, J\_Z, L\_XY ≡ 0\) ↦ γ\_Z(θ) ∈ P\_Λ,  γ\_Z(θ) \= e^{−iθσ\_y/2} · (K₀, K₁): not an arbitrary gauge path but the path selected by the Z-sector conditions.

The connection condition (C3) is now a representation-theoretic consequence, not a free assumption:

**Lemma 5.1 (Boundary Spin-Lift Lemma).** *\[Representation-theory content: ELEMENTARY-KNOWN. Use here: DERIVED-CONDITIONAL.\]* Let H\_Z ≅ ℂ² carry a faithful projective unitary representation of SO(3) in the **nontrivial class** of H²(SO(3), U(1)) ≅ ℤ₂ — equivalently, a representation under which the generator of a nontrivial 2π loop in π₁(SO(3)) ≅ ℤ₂ acts as −I. Then (i) the representation is unitarily equivalent to the spin-½ (*j* \= 1/2) representation of SU(2) \= Spin(3); (ii) the induced connection on the rank-2 Kraus frame of a dilation with environment H\_Z is generated by a half-angle generator G \= n·σ/2 for some unit vector n, i.e. G ≅ σ\_y/2 up to conjugation (axis) and orientation (sign); (iii) consequently χ\_Z \= −1. Conversely, a representation in the **trivial class** (2π ↦ \+I) gives the full-angle (vector) connection and χ\_Z \= \+1.

*Proof.* H²(SO(3), U(1)) ≅ ℤ₂ (Bargmann 1954); the nontrivial class consists of the genuine (linear) representations of the universal double cover SU(2). The unique 2-dimensional irreducible representation of SU(2) is the spin-½ representation, with generators J\_k \= σ\_k/2; a rotation by θ about axis n is e^{−iθ n·σ/2}, and the lift of a 2π rotation is the path I → −I in SU(2), acting as D^{1/2}(−I) \= −I (ZS-M3 Lemma 10.1). Faithfulness as a projective SO(3) representation follows from PU(2) ≅ SO(3). Since every n·σ has eigenvalues ±1, a unitary conjugation sends n·σ ↦ σ\_y, hence G \= n·σ/2 ≅ σ\_y/2 up to conjugation and orientation. The closure class follows from Theorem 2\. The converse (trivial class) factors through SO(3) with 2π ↦ \+I, giving the full-angle generator and χ\_Z \= \+1.  (Verified: suite Category I — 2π ↦ −I for 200 random axes to 1.2 × 10⁻¹⁶; n·σ/2 \~ σ\_y/2 by explicit unitary to 8.9 × 10⁻¹⁶; spinor/vector dichotomy.)

**Effect on the criterion (logical economy).** With Lemma 5.1, (C3) is no longer an independent assumption: it is forced by the premise that H\_Z physically carries the nontrivial spinor class. That premise is exactly the Z-Spin postulate — dim Z \= 2 \= the *unique j \= 1/2 spinor subspace* (ZS-M3 Theorem 5.1, PROVEN), anchored as the boundary Z \= ∂X (ZS-Q12, DERIVED-CONDITIONAL). Hence the spinor-boundary postulate now implies **(C1)** \[2-dim\] and **(C3)** \[half-angle connection\] *jointly*, leaving only **(C2)** \[accessible dilation\] and **(C4)** \[bypass exclusion\] as operational/experimental conditions. The remaining Z-Spin inputs:

- **(C2)** The Z-sector is the physical Planck-scale boundary H\_Z \= ∂(H\_X); the dilation environment is the Z-boundary with the seam phase as reference (ZS-Q12).  
- **(C4)** L\_XY ≡ 0 (ZS-F5, PROVEN) is bypass exclusion at the level of the action; on hardware it is enforced by the load-bearing controls (§9).

**Honest boundary.** Lemma 5.1 is textbook representation theory — the spin-½ representation is its canonical example, and H²(SO(3), U(1)) ≅ ℤ₂ is standard (Bargmann 1954; Hall 2015). It introduces no new mathematics; its contribution is to the paper's logical economy, deriving the half-angle connection from the already-postulated spinor nature of the Z-boundary rather than positing it separately. The contingency (and the falsifiability) is unchanged: *if* the boundary is a physical spinor, χ\_Z \= −1; a hardware χ\_Z \= \+1 refutes that premise.

---

# §6. The Signed Lift Witness and the Closure Class

**Definition 3 (Signed lift witness).** ũ\_Z(θ) \= Re Tr\[K₀(0)† K₀(θ)\]/‖K₀(0)‖\_F²,  K₀(θ) \= \[e^{−iθσ\_y/2}\]₀ᵤ Kᵤ(0) \= cos(θ/2)K₀(0) − sin(θ/2)K₁(0). (= ZS-A7R Eq. F.2.)

**Definition 4 (Closure class).** χ\_Z \= sgn\[ũ\_Z(2π)/ũ\_Z(0)\] ∈ {−1, \+1}; χ\_Z \= −1 ⟺ spinorial (half-angle) lift, \+1 ⟺ vector (full-angle) lift.

Properties (ZS-A7R Theorem 3.2-bis, PROVEN; suite Category B): ũ\_Z(0) \= \+1; ũ\_Z(θ) \= cos(θ/2) for seam-orthogonal Kraus; ũ\_Z(θ+2π) \= −ũ\_Z(θ); ũ\_Z(θ+4π) \= \+ũ\_Z(θ); uniqueness as the Kraus-linear discriminator (given the half-angle structure). ũ\_Z is *linear* in K₀(θ) and inherits the *j* \= 1/2 sign flip.

**Why a bilinear/probability witness fails (RETRACTED).** A probability contrast W \= P(0|2π) − P(0|4π) is bilinear and θ-constant by Theorem 1 (verified to 3.3 × 10⁻¹⁶, Category D); the θ-trivial "double-J echo" channel is likewise retracted (Category D). The witness is the linear ũ\_Z; the discriminant is the sign χ\_Z — never an absolute amplitude, never equal to A.

---

# §7. Process-Level Identifiability and Experimental Access \[POSITION — formalized\]

Theorems 1–2 say ũ\_Z is invisible at the channel level and gauge-dependent. The correct formal statement of *what it is* uses the process tensor / quantum comb (Chiribella, D'Ariano & Perinotti 2009; Pollock et al. 2018). Let Υ\_{2:0} denote the two-time process comb of the controlled dilation — the higher-order map taking the inserted control operation on the environment H\_Z (here the twist e^{−iθ G\_Z}) to the output system state. The channel is the zero-control marginal:

Λ \= Tr\_Z ∘ U\_XZ ,    U\_XZ(·) \= V(·)V† ,   V : H\_X → H\_X ⊗ H\_Z the Stinespring isometry.

The signed lift witness is **not** a function of Λ:

**ũ\_Z(θ) ≠ f(Λ),    ũ\_Z(θ) \= F(Υ\_{2:0}, G\_Z, R\_Z) \= F(V, G\_Z, φ\_Z),**

where V is the Stinespring isometry (the dilation), G\_Z \= σ\_y/2 is the selected connection (Lemma 5.1), and φ\_Z is the environment phase reference R\_Z — the control degree of freedom that the comb Υ\_{2:0} exposes but the channel marginal Λ discards. Concretely, F(V, G\_Z, φ\_Z) \= Re Tr\[K₀(0)† K₀(θ)\]/‖K₀(0)‖\_F² with K\_a(θ) the Kraus operators of V twisted by e^{−iθ G\_Z}, the reference φ\_Z fixing the anchor K₀(0).

The "≠ f(Λ)" is exactly the gauge-dependence verified in Theorem 2 / suite Category E: two dilations V, V′ of the *same* Λ give different ũ\_Z. The content: **ũ\_Z is a process-level observable of the comb Υ\_{2:0}, recoverable only with control of the dilation (the environment phase reference φ\_Z)** — the multi-time/dilation information the comb carries beyond Λ. Operationally this is a Hadamard test on the Kraus index (ZS-QH §6.1; Nielsen–Chuang) with the untwisted anchor K₀(0) as reference beam — the quantum-information analogue of the Werner–Colella–Overhauser (1975) reference beam that Kult, Åberg & Sjøqvist (2007) read as an early channel-holonomy realization. ZS-Q14 is therefore a *reduced comb/dilation tomography* of a physically-selected lift, not channel tomography. (This is a localization; the underlying fact that dilation phases require dilation access is Uhlmann 1986 — no new theorem is claimed.)

---

# §8. OAQEC Localization: Why the Witness is Read on X, not Z

ZS-Q11 (Theorem Q11.A, PROVEN) gives the single-cell logical algebra A\_ZS ≅ M₃(ℂ) ⊕ **ℂ** ⊕ M₅(ℂ), code dim 9 \= 1 \+ 3 \+ 5 (suite Category G reproduces this). The Z-logical block is the scalar ℂ — a *gauge subsystem* with trivial logical algebra — so ũ\_Z is **not** a Z-logical observable; it is read on the X-block M₃(ℂ) under the Z-frame error set E\_Z \= {I\_X ⊕ V ⊕ I\_Y}, against which X-logical information is correctable (Theorem Q11.B). The witness probes J\_Z-graded transport *through* the Z-gauge subsystem, detected on X — consistent with its being a process/dilation observable (§7). Following Dauphinais, Kribs & Vasmer (2024) (OAQEC stabilizer formalism characterizing correctable errors), and per ZS-Q11's own non-claim (NC-XIV.4), this is recognition of external mathematics, not a new Z-Spin claim.

---

# §9. Hardware Protocol and Load-Bearing Controls (Track B0)

**Encoding.** Embed {X: x₀,x₁,x₂}, {Z: z₀,z₁}, {Y: y₀,…,y₅} into a 16-dim four-qubit space (5 leakage states); p\_leak \= 1 − Tr(P\_code ρ P\_code) \< 1% (\< 5% feasibility-only).

**Circuit.** (1) Prepare |ψ\_X⟩, ancilla |+⟩. (2) Inject X→Z (the 2-channel Kraus index \= dilation environment). (3) Controlled half-angle twist e^{−iθσ\_y/2} on the Kraus index, θ ∈ {0, 2π, 4π} \+ fine sweep. (4) Hadamard-test readout of ũ\_Z(θ). (5) Form χ\_Z \= sgn\[ũ\_Z(2π)/ũ\_Z(0)\]. (6) Run all controls. Cost \~8% shots over ZS-A4 KS-2.

**Negative controls (three load-bearing, two non-diagnostic; suite Category F).**

- **NC1 — Bypass** (removes the 2-channel Z transit → removes the half-angle): χ\_Z \= \+1 (null). Tests (C4).  
- **NC4 — Phase-only** (full- vs half-angle generator): χ\_Z \= \+1 (null). Tests (C3) / Lemma 5.1.  
- **NC5 — Z-off** (no twist): χ\_Z \= \+1 (null). Tests (C2); a residual X-response to Y-stimulation independently violates L\_XY ≡ 0\.  
- **NC2 — Random involution / NC3 — Label shuffle:** χ\_Z \= −1 (do **not** null), because they perturb J\_Z / labels but not the half-angle connection (Proposition 4.1). **Non-diagnostic** — recorded as diagnostics, never as gates.

**Decision rule.** Pre-register N\_s ≥ 12 input states, ≥ 10⁴ shots, p \< 0.01 after correction, bootstrap CIs, TOST on the load-bearing controls only. Pass: χ\_Z \= −1 at \> 5σ; NC1/NC4/NC5 inside ROPE (χ ≈ \+1); p\_leak below threshold; reproduced on ≥ 2 backends or one backend \+ classical noise-injection audit. Native qudit/qutrit (Track A0) gives p\_leak ≈ 0; a material-stack realization (Track C0; ZS-QH FMDs) is future work.

---

# §10. The Hydrogenic Hyperfine Channel as a Second Physical Target

The lift-selection formalism is not specific to engineered hardware; the same Σ\_Z applies to a second, independent physical channel, which is why ZS-Q14 is a *physical-channel-geometry program* rather than a single-circuit proposal.

ZS-Q13 treats the hydrogen hyperfine transition as a Z-Spin-mediated rank-2 channel. There the *unsigned* Choi seam witness vanishes in the ideal limit (u\_seam → 0\) — a channel-level (bilinear) quantity, blind to the lift by Theorem 1 — while the *signed* lift witness ũ\_Z must carry the Kraus-level 4π closure (χ\_Z \= −1) if the spin-½ boundary selects the half-angle lift (Lemma 5.1). This is the same Choi-invisible / process-visible split as §3–§7, realized in atomic physics.

The discriminating power grows across the hydrogenic family. A program over **H / anti-H / muonium / positronium** separates proton-structure, CPT, and leptonic systematics, because the Σ\_Z prediction (χ\_Z \= −1, a parameter-free sign) is common while the conventional backgrounds differ by system. Two independent physical instances of the *same* closure-class prediction — an engineered four-qubit channel and the hydrogenic hyperfine channel — constitute a far stronger test of the lift-selection principle than either alone. (Status inherited from ZS-Q13; not re-derived here.)

---

# §11. Falsification Gates

| Gate | Condition | Consequence |
| :---- | :---- | :---- |
| F-Q14.1 | χ\_Z \= \+1 (2π / vector) on the Z-mediated channel | **spin-½ lift-selection refuted — primary kill** |
| F-Q14.2 | NC1 bypass gives χ\_Z \= −1 | effect not tied to Z transit ((C4) fails) |
| F-Q14.4 | NC4 phase-only gives χ\_Z \= −1 | ordinary phase, not the half-angle connection ((C3)/Lemma 5.1 fails) |
| F-Q14.5 | NC5 Z-off gives a signed signal | twist not located in Z ((C2) fails) |
| F-Q14.6 | leakage exceeds threshold | invalid protocol |
| F-Q14.7 | backend-to-backend reproduction fails | hardware artifact |
| F-Q14.9 | Z-off gives X-response to Y-stimulation | direct X–Y path (violates L\_XY ≡ 0\) |
| F-Q14.10 | no sim/hardware agreement after calibration | model invalid |
| F-Q14.11 | hydrogenic χ\_Z \= \+1 (ZS-Q13 target) | selection principle fails in the second physical instance |

A single failure among F-Q14.1, F-Q14.2, F-Q14.4, F-Q14.5, F-Q14.6 blocks any claim that the lift is physically selected.

---

# §12. Non-Claims and Prior-Art Boundary

This paper does **not** claim: (1) a new general theorem about quantum channels — the bundle (Kult, Åberg & Sjøqvist 2007), mixed-state holonomy (Uhlmann 1986), Choi/Jamiołkowski invariance (Choi 1975; Jamiołkowski 1972), the No-Go (Theorem 1), the process-comb localization (Chiribella et al. 2009; Pollock et al. 2018), and the representation theory of Lemma 5.1 (Bargmann 1954; Hall 2015\) are all prior art; (2) that quantum channels generically hide a 4π topology (Theorem 2); (3) that ũ\_Z is a channel observable (§6–§7); (4) any new quantum-computing algorithm, code, or primitive; (5) that Criterion 4.1 is a derived theorem, or that Lemma 5.1 is new mathematics (it is textbook representation theory used for logical economy); (6) that the selection is unconditional (DERIVED-CONDITIONAL on Z being a physical spinor boundary, Z \= ∂X); (7) that NC2/NC3 are diagnostic; (8) that a positive result proves the full Z-Spin framework (necessary, not sufficient); (9) that current hardware realizes the Z-sector or the full Topological Defect Controller. The single contingent positive content is the *candidate* spin-½ lift-selection (§5) and its falsifiable prediction χ\_Z \= −1.

---

# §13. Conclusion

A quantum channel cannot, by itself, select a Kraus lift (Theorem 1, known), and the same channel admits both a 2π and a 4π lift (Theorem 2, verified): the 4π is injected, not intrinsic. What can select a lift is a *physical connection* on the Kraus bundle — the established channel-holonomy fact — together with an accessible dilation. v1.4 grounds the connection condition representation-theoretically: if the Z-boundary carries the nontrivial spinor class of SO(3), the half-angle generator σ\_y/2 is forced (Lemma 5.1), so the spinor-boundary postulate alone implies both the minimal rank (C1) and the half-angle connection (C3). Z-Spin is then a candidate selector whose spin-½ boundary makes χ\_Z \= −1 a falsifiable, parameter-free, sign-valued prediction; the signed lift witness that measures it is a process/comb-level observable ũ\_Z \= F(V, G\_Z, φ\_Z) ≠ f(Λ) (§7), read on the X-block of the OAQEC algebra (§8), testable on near-term hardware (§9) and in the hydrogenic hyperfine channel (§10). The paper is a proposal — a *selection principle* with a representation-theoretic spine — rather than a defense: a 2π result kills it, a 4π result with controls null is a necessary success, and the framing claims no mathematics that is not either Z-Spin's own postulate or established prior art.

---

# Acknowledgements & Code Availability

Consolidated under Kenny Kang's editorial direction. The verification suite zs\_q14\_verify\_v1\_4.py (33/33 PASS, categories A–I) and the inherited ZS\_A7\_v1\_0\_verification.py (34/34, ZS-A7R) reproduce all quantitative claims of v1.4. No new theoretical constants; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

---

# Appendix A. Circuit Notation

Encoded basis {|0⟩,…,|10⟩} \= X₃ ⊕ Z₂ ⊕ Y₆; J\_Z: |z₀⟩↔|z₁⟩ (Z-internal, distinct from antipodal J: |j⟩↦|Q−1−j⟩; ⟨J,J\_Z⟩ ≅ D₄). Connection generator G \= σ\_y/2 (half-angle, forced by Lemma 5.1 under the spinor-boundary premise), lift U(θ) \= e^{−iθσ\_y/2}. Witness by the Hadamard-test estimator of ũ\_Z(θ) \= Re Tr\[K₀(0)† K₀(θ)\]/‖K₀(0)‖\_F², K₀(θ) \= cos(θ/2)K₀(0) − sin(θ/2)K₁(0); closure class χ\_Z \= sgn\[ũ\_Z(2π)/ũ\_Z(0)\]. **Do not** use the bilinear probability witness (θ-constant; Thm 1, Category D) or the double-J echo channel (θ-trivial; Category D).

---

# Appendix B. Pre-Registration Template

Fix before running: (1) backend; (2) date/calibration snapshot; (3) encoding map; (4) J\_Z and the connection generator G \= σ\_y/2; (5) the three load-bearing controls (NC1, NC4, NC5) and ROPE; (6) angle set {0, 2π, 4π} \+ fine sweep; (7) shot count; (8) input-state set (N\_s ≥ 12); (9) leakage threshold; (10) test (bootstrap \+ TOST on load-bearing controls only); (11) gates of §11. NC2/NC3 recorded as diagnostics, not gates. Post-hoc changes are exploratory.

---

# Appendix C. Verification (mapping to v1.4)

zs\_q14\_verify\_v1\_4.py, seed 20260601, numpy only, **33/33 PASS** (A 4/4 | B 5/5 | C 3/3 | D 2/2 | E 4/4 | F 5/5 | G 4/4 | H 3/3 | **I 3/3**). Mapping: **A** well-posedness; **B** Definition 3 properties; **C** Theorem 1; **D** §6 retractions; **E** Theorem 2 (gauge no-op; χ connection-dependent; ũ\_Z gauge-dependent — the "≠ f(Λ)" of §7); **F** Criterion 4.1 / Proposition 4.1 (NC1/NC4/NC5 null; NC2 2000 anchors all −1; NC3 −1); **G** §8 OAQEC ((Z,X,Y) \= (1,3,5), Z-block scalar; reproduces ZS-Q11 Thm Q11.A); **H** noise; **I — Lemma 5.1 (Boundary Spin-Lift):** the nontrivial 2π loop acts as −I for 200 random axes (1.2 × 10⁻¹⁶); every half-angle generator n·σ/2 is unitarily conjugate to σ\_y/2 (8.9 × 10⁻¹⁶); spinor→−I (χ=−1) vs vector→+I (χ=+1) dichotomy. Key residuals ≤ 4.4 × 10⁻¹⁶.

---

# Appendix D. Deep-Exploration Record (v1.4)

- **Adopted (both feedback items, judged sound):** (1) the **Boundary Spin-Lift Lemma** (Lemma 5.1), which upgrades condition (C3) from an independent assumption to a representation-theoretic consequence of the spinor-boundary premise, so that the postulate now implies (C1) \+ (C3) jointly; verified by the new suite Category I. (2) the **formalization of §7** via the process comb Υ\_{2:0} and the explicit ũ\_Z(θ) \= F(V, G\_Z, φ\_Z) ≠ f(Λ), with V the Stinespring isometry, G\_Z \= σ\_y/2 the connection, φ\_Z the environment phase reference.  
- **Honest guardrails:** Lemma 5.1 is elementary representation theory (the spin-½ representation; H²(SO(3),U(1)) ≅ ℤ₂); it adds no new mathematics and is tagged accordingly — its role is the paper's logical economy. The §7 formalization is a POSITION/localization (the dilation-access fact is Uhlmann 1986), not a new theorem. Verification grows 30 → 33 with the genuinely new Category I; no claim is verified beyond what the simulations show.

---

# References

**Internal (Z-Spin Cosmology):**

\[1\] K. Kang, *ZS-Q1: Geometric Decoherence and the Born Rule from the Z-Spin Action* (2026). \[2\] K. Kang, *ZS-Q7: Structural Arrow of Time and the Z-Bottleneck* (2026). \[3\] K. Kang, *ZS-Q11 v1.2: QRF↔OAQEC Correspondence — Direct-Sum Operator-Algebraic Stabilizer Code with Z-Frame Gauge Subsystem* (2026). \[4\] K. Kang, *ZS-Q12 v4.0: The Self-Referential Closure / Z \= ∂X Holographic-Interface Postulate* (2026). \[5\] K. Kang, *ZS-Q13 v1.2: Hydrogenic Hyperfine Channel — Signed vs Unsigned Seam Witness and the H/anti-H/muonium/positronium Programme* (2026). \[6\] K. Kang, *ZS-A4: Seam-Witness Protocols and the Z-Spin-Mediated CPTP Channel* (2026). \[7\] K. Kang, *ZS-A7R (Revised): Horizon as Spinor — 4π Closure and the Signed Seam Witness* (2026); Eq. (F.2), Theorem 3.2-bis, Appendix C. \[8\] K. Kang, *ZS-QH: Quantum Hardware Architecture* (2026); §6.1 Hadamard test. \[9\] K. Kang, *ZS-F1: The Z-Spin Action*; *ZS-F5: Why Q \= 11*; *ZS-M3: Regge-Holonomy* (Thm 5.1, Lemma 10.1) (2026).

**External:**

\[10\] A. Uhlmann, "Parallel transport and 'quantum holonomy' along density operators," Rep. Math. Phys. **24**, 229 (1986). \[11\] H. Kult, J. Åberg, E. Sjöqvist, "Holonomy for quantum channels," Phys. Rev. A **74**, 022106 (2006); arXiv:0711.2140. \[12\] B. Grygielski, J. Mielczarek, "Spin networks of quantum channels," arXiv:2602.12145 (2026). \[13\] A. Jamiołkowski, Rep. Math. Phys. **3**, 275 (1972); M.-D. Choi, Linear Algebra Appl. **10**, 285 (1975). \[14\] V. Bargmann, "On unitary ray representations of continuous groups," Ann. Math. **59**, 1 (1954); B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed. (Springer, 2015). \[15\] G. Chiribella, G. M. D'Ariano, P. Perinotti, "Theoretical framework for quantum networks," Phys. Rev. A **80**, 022339 (2009); "Quantum circuit architecture," Phys. Rev. Lett. **101**, 060401 (2008). \[16\] F. A. Pollock, C. Rodríguez-Rosario, T. Frauenheim, M. Paternostro, K. Modi, "Non-Markovian quantum processes: Complete framework and efficient characterization," Phys. Rev. A **97**, 012127 (2018); S. Milz, K. Modi, PRX Quantum **2**, 030201 (2021). \[17\] G. Dauphinais, D. W. Kribs, M. Vasmer, "Stabilizer formalism for operator algebra quantum error correction," arXiv (2024); C. Bény, A. Kempf, D. W. Kribs, Phys. Rev. Lett. **98**, 100502 (2007). \[18\] E. Sjöqvist et al., Phys. Rev. Lett. **85**, 2845 (2000); H. Rauch et al., Phys. Lett. A **54**, 425 (1975); S. A. Werner, R. Colella, A. W. Overhauser, C. F. Eagen, Phys. Rev. Lett. **35**, 1053 (1975). \[19\] M. A. Nielsen, I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge, 2010); J. Watrous, *The Theory of Quantum Information* (Cambridge, 2018).

---

# Version History

**v1.4, June 2026 (this version):** Adds **Lemma 5.1 (Boundary Spin-Lift Lemma)** — if H\_Z carries a faithful projective SO(3) representation in the nontrivial class of H²(SO(3), U(1)) ≅ ℤ₂ (2π ↦ −I), the induced Kraus-frame connection is the half-angle generator σ\_y/2 up to conjugation/orientation — which upgrades criterion condition (C3) from an independent assumption to a representation-theoretic consequence of the spinor-boundary postulate (the postulate now implies (C1) \+ (C3) jointly). **Formalizes §7** with the process comb Υ\_{2:0} and the explicit ũ\_Z(θ) \= F(Υ\_{2:0}, G\_Z, R\_Z) \= F(V, G\_Z, φ\_Z) ≠ f(Λ) (V Stinespring isometry, G\_Z \= σ\_y/2 connection, φ\_Z environment phase reference). Verification suite grows 30 → **33/33** with a new Category I (zs\_q14\_verify\_v1\_4.py). Honest guardrails retained: Lemma 5.1 is elementary representation theory (no new mathematics; logical-economy role), the §7 formalization is a localization (Uhlmann 1986), and no new general theorem or quantum-computing contribution is claimed. All v1.3 content retained (lift-selection reframing; Definitions 1–4; Theorems 1–2; Criterion 4.1 / Proposition 4.1; candidate-selector framing; hydrogenic second target), as are all v1.1 corrections (linear ũ\_Z; bilinear-witness and double-J-echo retractions; OAQEC M₃⊕ℂ⊕M₅ with the witness on X; corrected controls; "Z-Spin-mediated" terminology). Positive outcome **necessary but not sufficient**. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**v1.3, June 2026 (superseded):** Recentered the paper on the lift-selection question; added Definitions 1–4, Theorem 1 (No-Go), Theorem 2 (non-identifiability), Criterion 4.1 and Proposition 4.1, §5 (Z-Spin as candidate selector), §7 (process-level localization), and §10 (hydrogenic second target); recast the feedback's two "theorems" as a criterion \+ conditional proposition and a position.

**v1.1, June 2026 (superseded):** Added the Kraus-gauge-bundle formalism and the Choi-invisibility proposition with external attribution; established by simulation the gauge no-op, injected 4π, and gauge-dependence; corrected the OAQEC dimension (M₅) and control structure; replaced the bilinear witness with the linear ũ\_Z and retracted the double-J echo.

**v1.0, June 2026 (superseded):** Initial consolidation into a near-term falsification test.  
