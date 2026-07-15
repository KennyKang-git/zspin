**ZS-A24**

**Dimension-Weighted Mediator Semigroups and Their Spin-Graded Continuous-Core Lift**

*Finite-register modular unification, with the continuous-core dynamical lift left open (F-A24.9).*

*Part I — the general mediator-semigroup theorem, the exact H-theorem, the full 121×121 Liouvillian spectrum {0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**}, and perturbation stability. Part II — the genuine Type III → Type II∞ continuous core **C**\_ω \= 𝒜^III ⋊\_σ ℝ, its finite Type II₁ corner e**C**\_ω e, and the finite-register embedding ι : M₁₁ ↪ e**C**\_ω e; the de Sitter observer trace and the CLPW offset (embedding-conditional); the face-embedding frontier redefined by trace dimension; and a two-edge instanton whose factor 2 is DERIVED and whose per-edge normalisation is reduced to a sharp condition. An honest conditional lift that retracts the v1.0 finite-route Type II claim.*

**Author:** Kenny Kang

**Affiliation:** Z-Spin Cosmology Collaboration

**Theme / Code:** Astrophysics — **ZS-A24 v2.1**

**Date:** June 2026

**Repository:** github.com/KennyKang-git/zspin

**Verification: 54/54 computational, regression, and consistency checks PASS (zs\_a24\_v2\_1\_audit.py, attached and runnable) | Zero Free Parameters.** All quantities derive from **A** \= 35/437, **Q** \= 11, and (d\_Z, d\_X, d\_Y) \= (2, 3, 6); κ² \= A/Q. The checks are symbolic, regression, and consistency verifications (not 53 separate theorem proofs); the theorem-level results carry their own proofs in the text and appendices, and the per-version audit trail is in Appendix E and the Version History.

Sole geometric inputs: **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6), **LOCKED**, with **κ² \= A/Q \= 35/4807** and 1/κ² \= **Q**/**A** \= 4807/35 (PROVEN, ZS-A19 / ZS-M6 §2.2). Units: reduced Planck mass M̄\_P² \= (8πG)⁻¹; H̄₀/M̄\_P ≈ 5.9×10⁻⁶¹ is a disclosed external normalisation, **not** derived (= the corpus-wide B3 debt). A24 *consumes* the locked anchors and introduces **zero** new fitted parameters. (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED**.

**This is v2.0 — the consolidated public release.** It presents the final state of the theory in three Parts and is the result of the audit trail in Appendix E and the Version History (v1.0 → v2.0); the per-version corrections are not relitigated in the main body. The three results:

**(I) Part I — an exact open-system theory.** The dimension-weighted mediator semigroup has a general connected-graph stationary law, an exact H-theorem, a unique sector-covariant GKLS realisation, an **exact general Liouvillian spectrum** (Theorem A24.I-4G, any (a, b, c); Z-Spin {0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**}, multiplicities (1, 80, 36, 3, 1)), and **two PROVEN perturbation theorems**. Every rate is a rational multiple of **A**; zero new parameters.

**(II) Part II — the honest continuous-core lift.** The finite Type-II route is RETRACTED (inner modular flow); the genuine core is the Type III₁ → II∞ crossed product **C**\_ω \= 𝒜^III ⋊\_σ ℝ (IMPORTED-PROVEN), with a II₁ corner and a register embedding ι : M₁₁ ↪ M\_obs ⊂ **C**\_ω (DERIVED-CONDITIONAL). The corner *trace* is the matrix trace \= π \= (3, 2, 6)/11; the observer weight ω \= (9, 4, 36)/49 is the *state* τ(h·).

**(III) Part III — the modular half-density bridge, at the finite-register level.** **L**\_π (stationary π ∝ d\_i) and **L**\_ω (stationary ω ∝ d\_i²) are two reversible dynamics on M₁₁ joined by a modular half-density transform — the s \= 0 and s \= ½ endpoints of one **microscopic QMS interpolation family L**\_{(s)} (Theorem A24.III-2), with **L**\_ω proven KMS- *and* GNS-symmetric and modular-covariant (Theorem A24.III-1b). A no-go forbids a single generator from balancing both. The **continuous-core dynamical lift** — a generator **𝓛**\_s on M\_obs with E∘**𝓛**\_s \= **L**\_s∘E, modular covariance and complete positivity — is the **single honest OPEN item (F-A24.9)**, consistent with the Book's open Condition C.

Honest scope: the unification is **finite-register**; the standard tilted-Lindblad / KMS–GNS / Dirichlet machinery is credited as standard, the novelty being the exact package on the 3-2-6 register. The runnable audit reports **54/54 computational, regression, and consistency checks PASS**.

**§0. Abstract**

ZS-A23 reduced the dynamical heart of the corpus to one dimension-weighted mediator generator q\_{i→j} \= Γ₀κ²d\_j, built from the single coupling **κ² \= A/Q**. This paper is its three-Part development: a self-contained general theory of such semigroups (Part I), an honest lift of the finite register to a genuine de Sitter observer algebra (Part II), and the finite-register modular half-density bridge joining the state weight π to the operator weight ω (Part III).

**Part I (PROVEN).** For *any* finite connected graph with node multiplicities d\_i, the generator q\_{i→j} \= Γ₀κ²a\_{ij}d\_j has stationary distribution π\_i \= d\_i/Σ\_j d\_j, is reversible, obeys modular detailed balance, and has an exact H-theorem (Theorems A24.I-1–3). The sector-covariant GKLS realisation is unique (Schur per edge, plus global edge-homogeneity identifying the two edge scalars with the single κ²). Its **full 121×121 Liouvillian** closes with no new parameters:

Spec(ℒ) \= {0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**} with multiplicities (1, 80, 36, 3, 1), Σ \= 121,

the cross-sector coherences decaying at the clean rate **A**/2 (Theorem A24.I-4G — an exact spectrum for any sector dimensions). The generator is perturbation-stable with two PROVEN theorems (a reciprocal Dirichlet-form gap bound and an exact directional 3-state analysis), giving explicit simulator tolerance curves.

**Part II (the honest lift).** v1.0 claimed M₁₁ ⋊\_{σ^ω} ℝ is Type II. This is **false**: M₁₁ is a finite factor, its modular flow σ\_t^ω \= Ad(ρ\_ω^{it}) is *inner* (Skolem–Noether), and the crossed product by an inner action is M₁₁ ⊗̄ L^∞(ℝ) — Type I with diffuse centre, not a II factor (Theorem A24.II-0, **CLOSED-NEGATIVE for the finite route**). The genuine construction (Witten/CLPW/Takesaki) starts from the **Type III₁** QFT algebra 𝒜^III, whose modular flow is outer; **C**\_ω := 𝒜^III ⋊\_σ ℝ is **Type II∞** (Theorem A24.II-1, IMPORTED-PROVEN). A finite-trace corner M\_obs := e**C**\_ω e (0 \< τ(e) \< ∞) is **Type II₁**, and the finite register embeds, ι : M₁₁ ↪ M\_obs (Theorem A24.II-2, DERIVED-CONDITIONAL). The corner trace is the **matrix trace**: the **11 Hilbert microstate projections** e\_α each carry τ(e\_α) \= 1/D \= 1/11, so τ(P\_i) \= d\_i/D \= **(3, 2, 6)/11 \= π**; the **121 operator-slot projections** q\_a (the face-embedding targets) carry τ(q\_a) \= 1/121. The operator weight ω \= (9, 4, 36)/49 is the **state** ω(·) \= τ(h·) defined by the modular density h (PART III), and the CLPW offset **A**\_dS/4G enters Gate 2(ii) (DERIVED-CONDITIONAL / IMPORTED-MATCHING). The face-embedding target is realised in the II₁ corner: Φ\_face : ℂ¹²¹ → M\_obs sends 121 minimal idempotents to orthogonal projections of *continuous trace* τ(q\_a) \= 1/121 (not rank in M₁₁, which is impossible), and **v1.2 grounds the partition in ZS-F2 §11.4** — the coarse traces (6, 32, 83)/121 are (F(cube), F(truncated icosahedron), remainder), so **Gate 3 advances OPEN → DERIVED-CONDITIONAL**; **v1.3 resolves the equal-weight question** in favour of **combinatorial** (not metric) holography, since ZS-F0 §8.5 makes the Z-sector partition function a BV–BFV cobordism invariant (topological). The Gate-2 observer weight (9, 4, 36)/49 is **PROVEN** as the operator-sampling weight d\_i²/Σd\_j² (ZS-A23.MC), but **v1.5 corrects its operator-algebra identity**: the II₁-corner **trace** is the matrix trace \= d\_i/D \= **(3, 2, 6)/11 \= π** (the Part-I stationary), while ω \= (9, 4, 36)/49 is the **state** τ(h·) given by the modular density h\_i \= D d\_i/Σd\_j² (v1.4 had conflated this state with the trace, contradicting its own audit and ZS-A23). Read correctly, the Takesaki dual weight is the trace times h, so ω is the dual-weight *state*. This delivers the **complete finite-register trace/state unification (PART III)**: the dimension-weighted **L**\_π (stationary π) and the observer-balanced **L**\_ω (stationary ω) are two reversible dynamics on the *same register algebra* M₁₁, joined by a **modular half-density transform** and embedded in one interpolation family **L**\_{(s)}, s ∈ \[0, ½\] (Central Theorem A24.III; a no-go forbids a single generator from balancing both, and **v1.6 proves L**\_ω is both KMS- and GNS-symmetric on M₁₁ with \[**L**\_ω, σ\_t^ω\] \= 0). This supplies the **candidate finite-dimensional dynamics to be lifted to the continuous core**; the lift itself — a generator **𝓛**\_s on M\_obs \= e**C**\_ω e intertwining the conditional expectation with modular covariance and complete positivity — is **OPEN (F-A24.9)**, consistent with the Book/ZS-F23 keeping Condition C open. The two-edge instanton **factor 2 is DERIVED**; **v1.3 corrects the per-edge value**: 1/κ² is **RETRACTED** (no corpus instanton equals it — the corpus actions are π/A, 2π/A, 5π/A, 35π/3), and since the A24 mediation crosses the ℤ₂ seam (ZS-F23), the per-edge action is the **DERIVED seam-flip t\_flip \= π/A** (ZS-M3 §6), giving S\_{X→Y} \= 2π/A \= T\_micro. The old e^{−2/κ²} ≈ Λ motivation is exposed as numerology and RETRACTED (Gate 4, §14).

**Net.** The semigroup is now a complete open-quantum-systems theory (Part I); the continuous-core lift is on a correct algebraic footing (Part II); the cosmological-constant problem remains localised to the embedding, the B3 scale, and the per-edge instanton normalisation, with every over-claim of v1.0 retracted or made conditional. Zero free parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED**.

**Epistemic Status Legend**

*Table 1\. Epistemic status legend.*

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics alone, machine-verifiable. |
| **PROVEN-with-hypotheses** | Theorem under explicitly stated physical hypotheses (named in situ). |
| **IMPORTED-PROVEN** | Result proved externally, used without re-proof; full citation given. |
| **IMPORTED-MATCHING** | An external result invoked with a chosen reference-state normalisation; a matching, not an independent derivation. |
| **DERIVED** | Z-Spin action plus standard physics; zero free parameters. |
| **DERIVED-CONDITIONAL** | DERIVED conditional on listed hypotheses not themselves closed. |
| **PREDICTION** | A falsifiable consequence stated as such. |
| **HYPOTHESIS-strong / weak** | Motivated conjecture; documented closure route / failing chain. |
| **OBSERVATION / CONSISTENCY** | A numerical agreement reported as such, not a derivation. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted. |
| **OPEN** | Recognised gap; an executable closure route is named where one exists. |
| **CLOSED-NEGATIVE** | A registered gate / sub-route resolved in the negative (a theorem). |
| **RETRACTED** | A prior-version claim withdrawn as unsupported, with reason. |
| **LOCKED** | Core constant fixed upstream; immutable downstream. |

**§1. Introduction**

ZS-A23 established an exact correspondence between the Z-Spin-mediated finite-register operator algebra and a reversible three-sector Markov semigroup, and named (A23 §13) its own continuation: "the unified spin-graded continuous-clock program (ZS-A24)." Version 1.0 of this paper attempted that program but made a foundational error, identified in external review and corrected here.

**The v1.0 error and its correction.** v1.0 asserted (Theorem A24.1a) that the crossed product **M**\_C \= M₁₁ ⋊\_{σ^ω} ℝ is a Type II von Neumann algebra. This is incorrect. M₁₁ is a finite-dimensional factor; by the Skolem–Noether theorem every automorphism of M₁₁ is inner, and the modular automorphism v1.0 itself wrote, σ\_t^ω(x) \= ρ\_ω^{it} x ρ\_ω^{−it} \= Ad(ρ\_ω^{it})(x), is manifestly inner. The crossed product of a von Neumann algebra by an *inner* one-parameter action is the *tensor product* with the group algebra, M₁₁ ⋊\_{Ad ρ^{it}} ℝ ≅ M₁₁ ⊗̄ L^∞(ℝ̂), a Type I algebra with diffuse centre 1 ⊗ L^∞(ℝ̂) — **not a Type II factor**. v1.0's falsification gate F-A24.1 stated exactly this kill-switch ("if σ^ω is inner, Type I results and Theorem A24.1(a) fails") and then mis-cleared it by confusing *non-trivial* (the flow is non-trivial because the d\_i differ) with *outer* (a non-trivial inner action is still inner). **F-A24.1 is therefore triggered, and the finite-route Type II claim is RETRACTED** (§9, CLOSED-NEGATIVE).

The genuine construction — Witten's "gravity and the crossed product" and CLPW's de Sitter observer algebra — starts from the **Type III₁** algebra of quantum-field observables, whose modular flow *is* outer, and produces a **Type II∞** factor by Takesaki's continuous decomposition. The finite register M₁₁ is not the source of the Type II structure; it is *embedded* inside the genuine continuous core. v1.1 rebuilds Part II on this correct footing: the continuous core **C**\_ω \= 𝒜^III ⋊\_σ ℝ (II∞) contains a finite corner e**C**\_ω e (II₁), into which the register embeds, ι : M₁₁ ↪ e**C**\_ω e ⊂ **C**\_ω.

**The three-Part structure.** A23 named the dimension-weighted mediator semigroup — algebra generation, uniqueness, modular detailed balance, the H-theorem, the dimension-weighted Laplacian, the simulator — as its strongest stand-alone result. This paper develops it as a self-contained **Part I** (with the **full 121×121 Liouvillian spectrum** — the coherence modes, not only the 3×3 population sector — and **perturbation stability**, the tolerance curves a real simulator needs); **Part II** is the spin-graded continuous-core lift; and **Part III** is the finite-register modular half-density bridge joining the state weight π to the operator weight ω. This keeps the one-paper policy while ensuring no programme is buried in another.

**Scope and posture.** This is v2.0, the consolidated public release. Part I is PROVEN, with an exact general spectrum (Theorem A24.I-4G) and two PROVEN perturbation theorems. In Part II the II∞ core is IMPORTED-PROVEN; the Gate-2 trace/state identity is correct (corner *trace* \= matrix trace \= π \= (3, 2, 6)/11; observer weight ω \= (9, 4, 36)/49 \= the *state* τ(h·)). PART III proves the **finite-register** unification — **L**\_π and **L**\_ω are the s \= 0, ½ endpoints of one **microscopic QMS interpolation family L**\_{(s)} on M₁₁ (Theorem A24.III-2), with **L**\_ω KMS- *and* GNS-symmetric and modular-covariant (Theorem A24.III-1b). The honest scope is *finite-register* unification plus a *candidate dynamics to be lifted*; the **continuous-core dynamical lift is OPEN** (F-A24.9), the single honest gap. The surviving residuals are explicitly **upstream** (ZS-F0's deferred state-sum, CLPW's reference state), **corpus-wide** (B3), or **registered** (C5). No new free parameter is introduced, and the standard tilted-Lindblad / KMS–GNS / Dirichlet machinery is credited as standard (the novelty is the exact package on the 3-2-6 register).

**§2. Locked Inputs and Conventions**

**Time-normalisation convention.** Throughout, time is measured in units of the common microscopic attempt rate Γ₀: t\_dimensionless \= Γ₀ t, so that **Γ₀ ≡ 1** in all quoted spectra and simulator rates (the dimension-weighted rate is q\_{i→j} \= Γ₀κ²d\_j, and with Γ₀ \= 1 it is κ²d\_j). **Γ₀ is therefore a unit convention, not a fitted parameter** — every reported eigenvalue carries an implicit overall factor Γ₀, e.g. the population spectrum is Γ₀·{0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**}. This is what "zero free parameters" means here: the *ratios* and the *dimensionless* structure are fixed entirely by **A**, **Q**, and the sector dimensions; Γ₀ only sets the clock.

(**A**, **Q**, (Z, X, Y)) \= (35/437, 11, (2, 3, 6)) **LOCKED**. **κ² \= A/Q \= 35/4807**; 1/κ² \= **Q**/**A** \= 4807/35 (PROVEN, ZS-A19; ZS-M6 §2.2). Units: M̄\_P² \= (8πG)⁻¹; H̄₀/M̄\_P ≈ 5.9×10⁻⁶¹ (NON-CLAIM, \= B3). Sector dimensions (d\_X, d\_Z, d\_Y) \= (a, b, c) \= (3, 2, 6), D \= a+b+c \= **Q** \= 11\.

Inherited from A23 (PROVEN): finite dynamical algebra 𝒜\_phys \= M₁₁(ℂ) (Hilbert dim 11, operator dim 121); observer algebra **N** \= M₃ ⊕ M₂ ⊕ M₆ (operator dim 49); the mediator graph is the path X–Z–Y with L\_XY ≡ 0; stationary π \= (3, 2, 6)/11; population spectrum {0, −2**A**/**Q**, −**A**}; observer weights ω \= (9, 4, 36)/49; RN density h\_i \= 11d\_i/49; modular flow σ\_t^ω(C\_{ij}) \= (d\_i/d\_j)^{it}C\_{ij}; modular centralizer \= **N**; e^{−c} \= 121/49 \= dim M₁₁/dim **N**; index 3\.

New objects (Part II): the Type III₁ field algebra 𝒜^III; its outer modular flow σ\_t; the continuous core **C**\_ω \= 𝒜^III ⋊\_σ ℝ (II∞) with trace τ; a finite projection e (0 \< τ(e) \< ∞); the finite corner M\_obs \= e**C**\_ω e (II₁) with normalised trace τ\_e \= τ(·)/τ(e); the ZS-F23 ℤ₂ seam grading β (β² \= 1, τ∘β \= τ, βσ\_t \= σ\_tβ); the face algebra 𝒜\_face \= ℂ¹²¹.

**§2.5. Deep-Exploration Records (v1.2–v2.0).** The per-version deep-exploration records — for each version the brainstorm long-list, the MECE issue-list, the issue-tree status assignments (PROVEN / DERIVED / RETRACTED / OPEN / …), the convergence check, and the value/posture score, as required by the exploration protocol — are collected compactly in **Appendix E** to keep the main body on the final theory. The audit trail there documents every correction and retraction made on the way to v2.0 (notably the v1.3 per-edge retraction, the v1.4→v1.5 trace/state correction, and the v1.6 scope correction).

**PART I — The Dimension-Weighted Mediator Semigroup**

**§3. The General Connected-Graph Generator \[PROVEN\]**

**Theorem A24.I-1 (General stationary law, PROVEN).** Let G \= (V, E) be a finite connected undirected graph with adjacency a\_{ij} and positive node multiplicities d\_i, and define q\_{i→j} \= Γ₀κ²a\_{ij}d\_j (off-diagonal), q\_{i→i} \= −Σ\_{j≠i} q\_{i→j}. Then the unique stationary distribution is π\_i \= d\_i/Σ\_j d\_j, and the chain is reversible: π\_i q\_{i→j} \= κ²Γ₀ a\_{ij} d\_i d\_j/Σ\_k d\_k is symmetric in i, j, so π\_i q\_{i→j} \= π\_j q\_{j→i}. *Proof:* Appendix A; verified on the path (3, 2, 6), a 4-node mixed graph, and a triangle (4, 7, 2\) — stationarity and reversibility hold for all. 

This generalises A23's three-node result: the dimension-weighted rule produces the *size-by-multiplicity* equilibrium on **every** connected graph, not only the mediator path. The Z-Spin case is the path X–Z–Y (L\_XY ≡ 0), recovering π \= (3, 2, 6)/11.

**§4. Modular Detailed Balance and the Exact H-Theorem \[PROVEN\]**

**Theorem A24.I-2 (Modular detailed balance, PROVEN).** With **K**\_i \= −ln π\_i, q\_{i→j}/q\_{j→i} \= d\_j/d\_i \= π\_j/π\_i \= e^{−(K\_j − K\_i)}, i.e. ln(q\_{i→j}/q\_{j→i}) \= −Δ**K**\_{i→j}. On the mediator path this gives Δ**K**\_{X→Z} \= −ln(3/2), Δ**K**\_{Z→Y} \= −ln 3, and Δ**K**\_{X→Y} \= −ln 2 (the ZS-F19 value) as the composite of the two edges.

**Theorem A24.I-3 (Exact H-theorem, PROVEN).** With detailed balance, writing x \= r\_i q\_{i→j}, y \= r\_j q\_{j→i},

d/dt D(r‖π) \= −½ Σ\_{i,j} (x − y) ln(x/y) ≤ 0,

since (x − y)ln(x/y) ≥ 0\. Hence D(r‖π) is a Lyapunov function (verified: max dD/dt \= −7×10⁻⁶ over 5000 random states; the v1.0 Monte-Carlo is retained only as a regression test). The relaxation rates are γ\_slow \= 2**A**/**Q** and γ\_fast \= **A**, with γ\_fast/γ\_slow \= **Q**/2 \= 11/2, and the reverse rates γ\_zx \= 3**A**/**Q**, γ\_yz \= 2**A**/**Q** (four edge rates 2 : 3 : 6 : 2). **\[PREDICTION — testable on a 3-2-6 open-system simulator.\]**

**§5. Sector-Covariant GKLS Uniqueness \[PROVEN\]**

**Lemma A24.I-uniq (Schur per edge PROVEN; full uniqueness DERIVED; from A23.14c).** Among GKLS generators that are (i) covariant under U(d\_X)×U(d\_Z)×U(d\_Y), (ii) free of any direct X–Y channel, and (iii) primitive and trace-preserving, the jump operators on an edge (i, j) live in Hom(H\_j, H\_i), on which U(d\_i)×U(d\_j) acts as fund ⊠ antifund with one-dimensional commutant; **by Schur the Kossakowski block of each edge is a scalar**, leaving *one scalar per undirected edge-orbit* — here **two** independent values γ\_XZ and γ\_ZY, since the X–Z and Z–Y Hom-spaces are inequivalent representation blocks. Covariance alone does **not** force γ\_XZ \= γ\_ZY. The **global edge-homogeneity** condition — every microscopic mediator edge carries the *same* geometric impedance, the single Z-Spin constant κ² \= **A**/**Q** (there is one impedance, not one per sector pair) — identifies them: γ\_XZ \= γ\_ZY \= Γ₀κ². With that condition the dimension-weighted generator is unique, realised by L\_{jβ←iα} \= √(Γ₀κ²)|j,β⟩⟨i,α| (and L\_{Y←X} \= 0\) with **no energy ladder, no equal-spacing assumption, and no bath spectral density** — L\_XY \= 0 reflects the absent X–Y intertwiner directly. **\[Sector covariance fixes one scalar per edge (Schur); the Z-Spin action-level global-edge condition identifies them with the common Γ₀κ².\]**

**§6. The Full Liouvillian Spectrum — Exact and General \[PROVEN, generalised in v1.5\]**

v1.0 computed only the 3×3 population spectrum; v1.1 reported the full 121×121 spectrum by numerical diagonalisation. **v1.5 replaces the diagonalisation with an exact representation-theoretic theorem valid for any sector dimensions**, so the 121×121 matrix audit becomes a regression test, not the proof.

**Setup.** Let dim X \= a, dim Z \= b, dim Y \= c, and set m := a \+ c, D := a \+ b \+ c \= m \+ b, γ := Γ₀κ². There is no direct X–Y jump, but for the Liouvillian *spectrum* the union H\_U := H\_X ⊕ H\_Y (dim m) couples to H\_Z (dim b) as a **complete bipartite** graph: every U-microstate connects to every Z-microstate with the single microscopic rate γ. The jump operators are L\_{z←u} \= √γ |z⟩⟨u| and L\_{u←z} \= √γ |u⟩⟨z| for u ∈ U, z ∈ Z.

**Lemma A24.I-4a (matrix-unit action).** Writing deg(u) \= b (each U-state meets b Z-states) and deg(z) \= m, the number operator is N := Σ\_k L\_k†L\_k \= γ(b·P\_U \+ m·P\_Z). For an off-diagonal unit E\_rs \= |r⟩⟨s| (r ≠ s) the recycling term L\_k E\_rs L\_k† vanishes, so

**ℒ(E\_rs) \= −(γ/2)(deg r \+ deg s) E\_rs.**

Hence E\_rs is already an eigenvector. *Proof:* the recycling term γ⟨α|r⟩⟨s|α⟩|β⟩⟨β| is nonzero only if r \= s \= α. 

**Invariant decomposition.** This yields four off-diagonal eigenspaces and a diagonal block:

| Operator class | Eigenvalue | Count |
| ----- | ----- | ----- |
| U–U coherence E\_uv (u ≠ v) | −bγ | m(m−1) |
| Z–Z coherence E\_zw (z ≠ w) | −mγ | b(b−1) |
| U–Z and Z–U coherence E\_uz, E\_zu | −Dγ/2 | 2mb |
| diagonal D\_U⁰ \= {Σx\_u E\_uu : Σx\_u \= 0} | −bγ | m−1 |
| diagonal D\_Z⁰ \= {Σy\_z E\_zz : Σy\_z \= 0} | −mγ | b−1 |
| diagonal span{I\_U, I\_Z} | 0, −Dγ | 2 |

The recycling term cancels on D\_U⁰ and D\_Z⁰ (because every U-state meets the *same* Z-set and Σx\_u \= 0), giving the bare decay there; on span{I\_U, I\_Z} the 2×2 block \[\[−bγ, bγ\], \[mγ, −mγ\]\] has eigenvalues 0 (trace \= π) and −Dγ.

**Theorem A24.I-4G (General exact Liouvillian spectrum, PROVEN).** Collecting the U–U coherences with D\_U⁰ (total m²−1 at −bγ) and the Z–Z coherences with D\_Z⁰ (total b²−1 at −mγ),

**Spec(ℒ) \= { 0^{(1)}, (−bγ)^{(m²−1)}, (−Dγ/2)^{(2mb)}, (−mγ)^{(b²−1)}, (−Dγ)^{(1)} },**

with characteristic polynomial χ\_ℒ(λ) \= λ(λ \+ Dγ)(λ \+ bγ)^{m²−1}(λ \+ Dγ/2)^{2mb}(λ \+ mγ)^{b²−1} and dimension sum 1 \+ (m²−1) \+ 2mb \+ (b²−1) \+ 1 \= (m \+ b)² \= D². *Proof:* Lemma A24.I-4a plus the invariant decomposition above; verified against the explicit 121×121 build for (3, 2, 6\) and against a second case (2, 3, 4\) in zs\_a24\_v2\_1\_audit.py. 

**Corollary A24.I-4 (Z-Spin, PROVEN).** For (a, b, c) \= (3, 2, 6), m \= 9, D \= 11, γ \= κ² \= **A**/**Q** (so Dκ² \= **A**),

**Spec(ℒ) \= { 0, −2A/Q, −A/2, −9A/Q, −A }, multiplicities ( 1, 80, 36, 3, 1 ), Σ \= 121\.**

The 36-fold −**A**/2 block is the X–Z and Z–Y cross-sector coherence space (6 \+ 6 and 12 \+ 12), decohering at exactly half the fast population rate **A**. Every relaxation and decoherence rate is a rational multiple of **A**, with **no new parameters**. The earlier numerical diagonalisation is now a regression check, not the derivation.

**§7. Perturbation Stability \[two theorems PROVEN in v1.5; generic numerical\]**

Real hardware never realises perfectly uniform jumps. v1.1 bounded the response numerically; v1.5 splits the perturbation into two MECE classes and closes each with an exact theorem.

**§7.1 Reciprocal (detailed-balance-preserving) perturbations \[PROVEN\].** Write the reversible conductance C\_{ij} := π\_i q\_{ij} \= C\_{ji}, and perturb the *conductance* symmetrically: C\_{ij}(ε) \= C\_{ij}(1 \+ s\_{ij}), s\_{ij} \= s\_{ji}, |s\_{ij}| ≤ ε \< 1, with q\_{ij}(ε) \= C\_{ij}(ε)/π\_i. Then π is **exactly** unchanged and detailed balance is exactly preserved (π\_i q\_{ij}(ε) \= C\_{ij}(ε) \= C\_{ji}(ε) \= π\_j q\_{ji}(ε)). The Dirichlet form E\_ε(f, f) \= ½ Σ\_{ij} C\_{ij}(1 \+ s\_{ij})(f\_i − f\_j)² obeys (1 − ε)E\_0 ≤ E\_ε ≤ (1 \+ ε)E\_0, so by Rayleigh–Ritz

**(1 − ε) λ\_gap ≤ λ\_gap(ε) ≤ (1 \+ ε) λ\_gap,    λ\_gap \= 2A/Q.**

The same bound holds for the full GKLS Liouvillian (each undirected microscopic pair carries γ\_{uz} \= γ(1 \+ s\_{uz}), s\_{uz} \= s\_{zu}; the HS Dirichlet form is a nonnegative sum and scales identically). **\[PROVEN for all 0 ≤ ε \< 1.\]**

**§7.2 Directional (3-state path) perturbations \[PROVEN\].** Let the four independent rates be α \= q\_{X→Z}, β \= q\_{Z→X}, δ \= q\_{Z→Y}, η \= q\_{Y→Z}. The matrix-tree theorem gives the **exact** stationary measure

**π^(ε) \= (βη, αη, αδ) / (βη \+ αη \+ αδ),**

and the two nonzero decay rates are exactly g\_± \= (S ± √(S² − 4T))/2 with S \= α \+ β \+ δ \+ η, T \= αδ \+ αη \+ βη. At the base rates (α₀ \= η₀ \= bγ, β₀ \= aγ, δ₀ \= cγ) this returns π \= (3, 2, 6)/11, g\_− \= bγ \= 2**A**/**Q**, g\_+ \= Dγ \= **A**. With r\_k \= r\_{k,0}(1 \+ ε\_k), |ε\_k| ≤ ε, each spanning-tree weight is a product of two rates, giving the rigorous total-variation bound ‖π\_ε − π‖\_TV ≤ 2ε/(1 \+ ε²). The first-order gap shift is

**g\_−^ε \= bγ\[ 1 \+ (c ε\_{X→Z} \+ a ε\_{Y→Z})/(a \+ c) \] \+ O(ε²)**

— it depends on the **forward** rates only; the reverse rates ε\_{Z→X}, ε\_{Z→Y} drop out at first order (a new analytic result, invisible to the earlier Monte Carlo). For (a, c) \= (3, 6): g\_−^ε \= 2γ\[1 \+ (2/3)ε\_{X→Z} \+ (1/3)ε\_{Y→Z}\]. **\[PROVEN.\]**

**§7.3 Generic perturbations — coarse and full microscopic \[VERIFIED-NUMERICAL\].** Two distinct Monte-Carlo tests. (a) **Coarse 3-state generic (non-reciprocal) perturbation:** the four population rates of the 3-state chain are shaken independently (500 random perturbations per scale):

| ε (rate) | gap (base 2A/Q \= 0.01456) | max\_i |Δπ\_i| |
| ----- | ----- | ----- |
| ±0.01 | 0.01456 ± 0.00006 | 0.0065 |
| ±0.05 | 0.01456 ± 0.00032 | 0.0315 |
| ±0.10 | 0.01452 ± 0.00064 | 0.0599 |
| ±0.20 | 0.01459 ± 0.00127 | 0.1138 |

(b) **Full microscopic 121×121 symmetry-breaking:** each of the 36 microscopic jump *rates* is perturbed independently and the full 121×121 superoperator is rebuilt every trial; at ±5% the spectral gap deviates by ≤ 5% and the sector populations by max\_i |Δp\_i| \< 0.02 (the audit's PASS threshold; the fixed-seed run gives ≈ 0.011), consistent with the §7.1–7.2 analytic bounds. **\[VERIFIED-NUMERICAL — both the coarse chain and the full 121×121 microscopic Liouvillian are MC-tested (zs\_a24\_v2\_1\_audit.py); the figure is a robustness illustration, not a certified statistical tolerance.\]**

**§8. Simulator Protocol and Hardware Tolerance \[TESTABLE\]**

The architecture **H** \= ℂ³ ⊕ ℂ² ⊕ ℂ⁶ (a 3-level X register, a 2-channel Z mediator, a 6-channel Y reservoir; ZS-QH) realises both generators by a choice of jump amplitude. The two stationary samplings are **distinct dynamics** and require **two protocols** (π is the stationary state of **L**\_π, ω that of **L**\_ω):

**Protocol A (state sampling).** Activate only the X–Z and Z–Y channels with *equal* microtransition amplitude √(Γ₀κ²) (this is **L**\_π). Measure p\_X(t), p\_Z(t), p\_Y(t). **Predictions:** p(∞) \= (3, 2, 6)/11 \= π; λ\_slow \= −2**A**/**Q**, λ\_fast \= −**A**, λ\_fast/λ\_slow \= **Q**/2 \= 11/2; cross-sector coherences decay at **A**/2 (a Ramsey/echo measurement).

**Protocol B (operator sampling).** Tilt each jump amplitude by (d\_j/d\_i)^{1/4} (this is **L**\_ω). Then the stationary populations are p(∞) \= (9, 4, 36)/49 \= ω; observer tomography of the operator-size-biased weight returns ω.

**Tolerance (§7):** ≤ 5% **rate** non-uniformity (≈ 2.5% amplitude, since rate ∝ amplitude²) holds the stationary populations to an absolute deviation max\_i |Δp\_i| ≲ 0.03 (the §7.3 figure is an absolute probability deviation, not a ratio error). **\[TESTABLE — the entire Part I/Part III finite-register dynamics is verifiable on a small open-system simulator without awaiting any cosmological scale.\]**

**PART II — The Spin-Graded Continuous-Core Lift**

**§9. Gate 1, Step 0 — Why the Finite Route Fails \[CLOSED-NEGATIVE\]**

**Theorem A24.II-0 (Finite-route obstruction, CLOSED-NEGATIVE).** Let σ\_t^ω \= Ad(ρ\_ω^{it}) be the modular flow of ω\_reg on M₁₁. Then:

1. **σ^ω is inner.** M₁₁ is a finite-dimensional factor; by Skolem–Noether every automorphism is inner, and σ\_t^ω is implemented by ρ\_ω^{it} ∈ M₁₁.

2. **The crossed product is not a II factor.** For an inner one-parameter action implemented by U(t) ∈ M, the crossed product M ⋊\_{Ad U} ℝ is isomorphic to M ⊗̄ W\*(U(t)'') ≅ M₁₁ ⊗̄ L^∞(ℝ̂), with diffuse centre 1 ⊗ L^∞(ℝ̂). This is a Type I algebra with continuous centre — **not a Type II factor**, and it carries no canonical finite trace distinct from the M₁₁ trace tensored with Lebesgue measure.

Hence v1.0's Theorem A24.1(a) is **RETRACTED** for the finite route, and the v1.0 statements "This seals Gate 1" and "the Type II trace recovers …" are withdrawn. The error in v1.0 was to read the *non-triviality* of σ^ω (the d\_i differ) as *outerness*; a non-trivial inner action is still inner. *Verified:* audit II.1. 

**§10. The Genuine Type III → II∞ Continuous Core \[IMPORTED-PROVEN\]**

**Theorem A24.II-1 (Continuous core, IMPORTED-PROVEN).** Let 𝒜^III be the Type III₁ von Neumann algebra of quantum-field observables in a de Sitter static patch (CLPW). Its Tomita–Takesaki modular automorphism group σ\_t (for the cyclic separating vacuum) is **outer**. The crossed product

**C**\_ω := 𝒜^III ⋊\_σ ℝ

is a **Type II∞** factor carrying a faithful normal semifinite **canonical trace τ** — distinct from the dual weight, which is φ̂(x) \= τ(h\_φ x) for the modular density h\_φ (the same trace-vs-weight distinction made precise for the finite register in §12). Takesaki's continuous decomposition of a Type III₁ factor, specialised to gravity by Witten ("gravity and the crossed product") and to the static patch by CLPW, supplies it. The gauged modular boost intrinsically regularises the entanglement entropy with no explicit UV cutoff; in Z-Spin the polyhedral lattice supplies the finite-dimensional regulator (ZS-F19 §12). The ℤ₂ seam grading (ZS-F23) acts as a trace-preserving order-2 automorphism β (β² \= 1, τ∘β \= τ, βσ\_t \= σ\_tβ); the spin-graded core is **C**\_ω ⋊ β. *This theorem is imported, not re-proved.* 

The construction direction is therefore **𝒜^III \--⋊\_σ ℝ--\> C\_ω (II∞) \--corner--\> M\_obs (II₁)**, into which the finite register embeds **M₁₁ \--ι--\> M\_obs ⊂ C\_ω**, not the (false) "M₁₁ \--cross--\> II."

**§11. The Finite II₁ Corner and the Register Embedding \[DERIVED-CONDITIONAL\]**

**Theorem A24.II-2 (Finite corner and embedding, DERIVED-CONDITIONAL).** Choose a projection e ∈ **C**\_ω with 0 \< τ(e) \< ∞. Then the corner

M\_obs := e**C**\_ω e is a **Type II₁** factor, with normalised trace τ\_e(x) \= τ(exe)/τ(e),

(a finite corner of a II∞ factor is II₁). The finite register embeds as a unital ∗-homomorphism

ι : M₁₁ ↪ M\_obs,

and the A23 dimension-weighted semigroup acts on ι(M₁₁) as the population dynamics (Part I), so that a conditional expectation E : M\_obs → ι(M₁₁) carries it to the modular clock of **C**\_ω at the **population** level. Lifting the full **bridge** to the core *would require* a generator **𝓛**\_s on M\_obs (yet to be constructed) intertwining the finite generator **L**\_s built on M₁₁ in §U4,

**E ∘ 𝓛\_s \= L\_s ∘ E** (with modular covariance and complete positivity),

which is **not** done here. **Conditional on:** the existence of the embedding ι — proved *realisable* (II₁ factors admit such unital embeddings, for which the trace is automatically the normalised matrix trace) but not *selected from the Z-Spin action*. The remaining conditions are not the trace weight (that is fixed) but the **compatibility of the modular density h with the core dual weight** and the **dynamical lift 𝓛\_s** (§U6, OPEN). **\[DERIVED-CONDITIONAL on the existence of ι and modular-density compatibility; the trace-preserving conditional expectation E exists, but the dynamical intertwining E∘𝓛\_s \= L\_s∘E is a requirement on the still-unconstructed continuous-core lift and remains OPEN (F-A24.9).\]**

**§12. Gate 2 — Observer Trace \[corrected v1.5: trace \= π, observer weight ω \= τ(h·)\] and CLPW Offset \[Gate 2(ii) DERIVED-CONDITIONAL\]**

**Theorem A24.II-3 (Observer trace and observer state, DERIVED — corrected in v1.5).** The II₁-corner **trace** of the embedded projectors is the **matrix trace**

**τ\_e(ι(P\_i)) \= d\_i/D \= (3, 2, 6)/11 \= π** (the Part-I stationary),

realised in continuous trace dimension (each of the **11 Hilbert microstate projections e\_α** has τ\_e(e\_α) \= 1/D \= 1/11, well-posed in II₁ where the v1.0 rank statement was not; the symbol q\_a is reserved for the **121 operator-slot** projections of §13, τ\_e(q\_a) \= 1/121). The A23 **observer weight** (9, 4, 36)/49 is **not this trace** but the **state**

**ω\_e(x) \= τ\_e(h x),    ω\_e(ι(P\_i)) \= d\_i²/Σ\_j d\_j² \= (9, 4, 36)/49,    h\_i \= D d\_i/Σ\_j d\_j²,**

where h is the modular density (τ\_e(h) \= 1). Both are PROVEN: τ\_e(ι(P\_i)) \= d\_i/11 is the matrix trace, and ω\_e(ι(P\_i)) \= τ\_e(h ι(P\_i)) \= (1/11)(11 d\_i/49) d\_i \= d\_i²/49.

**v1.5 correction (this fixes a conflation carried from v1.0).** v1.4 identified the corner trace itself with (9, 4, 36)/49 via the Takesaki dual weight. That **conflated a state with a trace**: the Takesaki dual weight of **C**\_ω \= 𝒜^III ⋊\_σ ℝ is the **trace times the modular density** (φ̂ \= τ(h\_φ ·)), so restricting it to the register gives the *state* ω\_reg \= τ\_e(h ·), **not** the trace. The corner *trace* is the matrix trace, τ\_e(ι(P\_i)) \= d\_i/11 \= π. This also resolves an internal inconsistency: v1.4's own audit check II.2b already recorded that the rank-normalised corner trace is (3, 2, 6)/11; and it **restores consistency with ZS-A23**, which calls (3, 2, 6)/11 the "trace weights / stationary distribution" (A23.5a) and (9, 4, 36)/49 the operator-sampling state ω\_reg (A23.MC). ZS-A23.MC and A23 §5(iii) PROVE ω\_i \= d\_i π\_i/Σ\_j d\_j π\_j \= d\_i²/Σ\_j d\_j² two independent ways (the operator-space size-bias of π, and the modular centralizer of ω\_reg with density h\_i \= 11 d\_i/49 — exactly the h above).

**Consequence — the unification.** Because the corner carries the *same* trace π as the Part-I dynamics, and ω is the modular state τ\_e(h ·) on the *same* algebra, the dimension-weighted **L**\_π and the observer-balanced **L**\_ω are two reversible dynamics on one algebra joined by a modular half-density transform — the **finite-register** Part I ↔ Part II unification developed in **PART III** (the continuous-core dynamical lift remains OPEN, F-A24.9). **\[Gate 2(i): DERIVED — corner trace \= matrix trace \= π \= (3, 2, 6)/11; observer weight ω \= (9, 4, 36)/49 \= τ\_e(h ·), the modular state. The v1.4 trace-vs-state conflation is corrected.\]**

**Theorem A24.II-4 (CLPW offset, IMPORTED-MATCHING / DERIVED-CONDITIONAL).** CLPW give S\_alg \= S\_gen \+ C with C a state-independent additive constant fixed by the Type II renormalisation; the maximum-entropy state of the II₁ corner is empty de Sitter. Choosing empty de Sitter as the normalised tracial *reference* (where S\_τ \= 0\) matches the offset to the de Sitter horizon entropy,

S₀ \= **A**\_dS/4G \= 8π²M̄\_P²/H²   (Gibbons–Hawking).

This is a **matching under a chosen reference normalisation, not a unique algebraic derivation** — the corpus (Book/ZS-F23) keeps the generalised-entropy formula itself unproved, the identification of a specific hyperfinite factor with the gravitational subregion algebra as Condition C (OPEN), and the observer/clock identification as HYPOTHESIS-level. v1.0 over-stated this; v1.1 lowers it. The residual O(1) and the absolute scale reduce to the corpus-wide **B3** scale H̄/M̄\_P (§15). **\[Gate 2(ii): IMPORTED-MATCHING / DERIVED-CONDITIONAL.\]**

**§13. Gate 3 — The Face Embedding: Partition DERIVED from ZS-F2 §11.4 \[DERIVED-CONDITIONAL\]**

v1.0 wrote that 𝒜\_face \= ℂ¹²¹ embeds "as a MASA of M₁₁." This is **mathematically false**: a maximal abelian subalgebra of M₁₁ is ℂ¹¹ (the diagonal), there is no unital injective ∗-homomorphism ℂ¹²¹ ↪ M₁₁ (one cannot place 121 orthogonal nonzero projections in M₁₁), and (6, 32, 83\) cannot be projection ranks in M₁₁ (they sum to 121 \> 11). The error was to confuse the operator dimension (121) with a projection count. The correct target lives in the **II₁ corner**, where projections carry *continuous trace* ∈ \[0, 1\], not integer rank.

**Corrected Gate-3 target (well-posed, OPEN).** The face embedding is a trace-preserving ∗-homomorphism

**Φ\_face : 𝒜\_face \= ℂ¹²¹ → M\_obs (II₁),   e\_a ↦ q\_a,   q\_a q\_b \= δ\_{ab} q\_a,   τ\_e(q\_a) \= 1/121,**

sending the 121 minimal face idempotents to 121 mutually orthogonal projections each of continuous trace 1/121 (possible in a II₁ factor; impossible in M₁₁). The coarse projections

q\_b \= Σ\_{a∈B} q\_a,   q\_c \= Σ\_{a∈C} q\_a,   q\_Λ \= Σ\_{a∈Λ} q\_a,   with   τ\_e(q\_b, q\_c, q\_Λ) \= (6, 32, 83)/121,

then carry the face-counting budget Ω\_b \= 6/121, Ω\_cdm \= 32/121, Ω\_Λ \= 83/121 (ZS-F2; Planck 0.4%) as **trace dimensions, not ranks**.

**v1.2 — the partition is DERIVED from ZS-F2 §11.4.** The three-block decomposition is no longer asserted; it is read off the face-counting construction (ZS-F2 §11.4, Theorem 11.7, Boundary Mode Theorem):

b \= **F(cube) \= 6** (the X-sector spatial frame; visible matter \= F(cube)/Q² \= 6/121 \= slot count X·Z/Q²);

c \= **F(truncated icosahedron) \= 32** (the Y→X mediator; CDM \= dim Ω²(Γ\_med) \= F(Γ\_med) \= 32/121, the Hodge 2-form dimension);

Λ \= **121 − 6 − 32 \= 83** (the remaining background slots; Ω\_Λ \= 83/121),

with Q² \= 121 \= dim M₁₁ the operator dimension and one slot \= 1/Q² per face. ZS-F2's anti-numerology already certifies this: of n ∈ \[1, 120\] only n \= 32 places ω\_cdm within 1σ of Planck, 0.0 % of 500 000 random fractions outperform 32/121, and 32 \= F(truncated icosahedron) was the Y-mediator assignment *before* the face-counting discovery. The A24 contribution is to realise ZS-F2's "121 operator slots" as **121 genuine orthogonal projections of continuous trace 1/121 in the II₁ corner** — which M₁₁ cannot host but a II₁ factor can — so that (6, 32, 83)/121 are well-defined trace dimensions. **\[Gate-3 partition: DERIVED (ZS-F2 §11.4); realised as II₁ projections (A24).\]**

**What remains conditional.** The equal one-quantum-per-face weight τ\_e(q\_a) \= 1/121 is **combinatorial (not metric) holography** — the polyhedral faces have unequal areas (cube ≈ 1.33, dodecahedron ≈ 0.88), so a metric/area weighting would be unequal. **v1.3 resolves the combinatorial-vs-metric question in favour of combinatorial.** ZS-F0 §8.5 (Theorem 8.9) constructs the Z-sector partition function as a **BV–BFV cobordism invariant**: the closed 4-cobordism Wilson loop W maps under the functor B\_Z to the i-tetration evolution, with partition function Z(W) \= (iπ/2)z\\ *and survival probability |Z(W)|² \= (π²/4)η\_topo ≈ 0.7948 — a **topological** quantity (the i-tetration trace), not a metric/area integral. A topological boundary partition function counts states* combinatorially *(one quantum per face, area-independent), so the equal weight 1/121 is the combinatorial dimension count, **not** an area weight. The residual is therefore narrowed to a single deferred item: the* explicit *face-weight state-sum (a Turaev–Viro / Barrett–Westbury realisation with Pachner-move invariance forcing equal weights), which is ZS-F0's own deferred categorical formalisation (F0 §166, "DERIVED-CONDITIONAL … modulo categorical polish"). **v1.4 — the equal weight is the monoidal functor's per-face assignment; the residual is upstream.** ZS-F0 §8.3 (Definition 8.3) makes B\_Z a **monoidal functor** that assigns the sector decomposition of ℂ¹¹ to each boundary cell. By functoriality and locality, every face of the same type receives the* same *assignment (one copy of the representation space per face), so the weight is equal per face — the combinatorial 1/121. The* explicit\* face-weight state-sum (the Turaev–Viro / Barrett–Westbury realisation with Pachner-move invariance) is precisely **ZS-F0's own deferred categorical formalisation** (F0 §166: "Full closure requires the formalization of the BV-BFV monoidal functor structure at the categorical level"). It is therefore an **upstream** item — ZS-F0's to complete — not an A24-internal gap. **\[Gate 3: partition DERIVED (ZS-F2 §11.4); combinatorial nature DERIVED (ZS-F0 §8.5); equal weight \= the local monoidal functor's per-face assignment (ZS-F0 §8.3); the only residual is ZS-F0's deferred categorical state-sum (UPSTREAM), not A24.\]**

**§14. Gate 4 — The Two-Edge Instanton: Factor 2 DERIVED, Per-Edge Corrected to π/A (F-A24.4)**

A23 sharpened the period-2 absolute factor |Δ**W**| \= 2 to a two-edge structure and left the per-edge action OPEN. The reviewer correctly noted that two-edge additivity S\_{X→Y} \= S\_{X→Z} \+ S\_{Z→Y} alone gives neither equal edges nor the value 1/κ². F-A24.4 resolves the equality and reports the value honestly.

**§14.1 The factor 2 is DERIVED \[equal edges\].**

**Theorem A24.II-5 (Equal-edge doubling, DERIVED).** Both seam crossings of the path X–Z–Y are mediated by the **same** Z-sector topological object — the Z-Anchor Bogomolnyi vortex, the unique |Φ| \= 0 core forced by π₁(U(1)) \= ℤ (ZS-F1). The instanton action of a BPS vortex is *topological*: it is fixed by the winding number and the VEV, and is **independent of the sector multiplicities d\_i** (which weight the dissipative rate q \= κ²d\_j, a logically separate structure). Hence S\_{X→Z} \= S\_{Z→Y} \= S\_vortex despite the different edge dimensions (3↔2 vs 2↔6), and

**S\_{X→Y} \= 2 S\_vortex.**

This upgrades the period-2 factor from "graph-distance additivity" to **exact doubling**: the cosmologically relevant factor |Δ**W**| \= 2 is DERIVED. **\[Gate 4 factor 2: DERIVED.\]**

**§14.2 The per-edge value: 1/κ² RETRACTED, corrected to the seam-flip π/A \[F-A24.4, v1.3\].**

**Computation A24.II-6 (the Z-Anchor action from ZS-F1, v1.2).** Reading the actual ZS-F1 action settles what kind of object the Z-Anchor is. ZS-F1 §7 keeps the Goldstone θ **massless and physical** (ΔN\_eff \= 0; it drives the ZS-A1 isothermal halo), so the U(1) is **global**, not Higgsed. A global vortex has a **logarithmically divergent** energy E ≈ π v² ln(L/ξ) (ξ \= ℏc/m\_ρ ≈ 31 l\_P, ZS-F1 §5.3), **not** the BPS-finite tension 2πv²|n|. Two readings, the same conclusion:

• **Global (the ZS-F1 reading):** per-edge action ∝ ln(L/ξ), IR-cutoff-dependent — not a clean 1/κ² at all.

• **Gauged BPS (counterfactual):** S\_vortex \= 2πv²|n| \= 2π ≈ 6.28 for the minimal v \= 1, n \= 1 — and S\_vortex \= 1/κ² \= **Q**/**A** ≈ 137.34 would require v²|n| \= **Q**/(2π**A**) ≈ 21.86, i.e. winding n ≈ 22, which ZS-F1 §5 **excludes** (the minimal topologically-stable winding is n \= 1).

In neither reading does the Z-Anchor supply per-edge \= 1/κ². **The Bogomolnyi-vortex route to the per-edge action is therefore CLOSED-NEGATIVE.**

**Computation A24.II-7 (the θ-instanton search and the corrected per-edge value, v1.3).** v1.2 left per-edge \= 1/κ² to a Z-EFT θ-instanton. Reading the corpus instanton ledger settles it: the corpus's *actual* non-perturbative actions are **t\_flip \= π/A ≈ 39.22** (one ℤ₂ half-event, ZS-M3 §6), **T\_micro \= 2π/A ≈ 78.45** (one full period), **S\_tunnel \= 5π/A ≈ 196** (five seam flips, ZS-M3/ZS-A3 proton decay), and **S\_cl \= 35π/3 ≈ 36.65** (the EWSB instanton, ZS-S4 §6.11). **None equals 1/κ² \= Q/A ≈ 137.34** — indeed 1/κ² ÷ (π/A) \= **Q**/π ≈ 3.50 is not an integer, so 1/κ² is not a seam-flip count; a θ-instanton tuned to 1/κ² would *conflict* with these established scales (exactly the conflict that demotes the ZS-M14 NC-4 1/α-instanton term to HYPOTHESIS-weak). **So per-edge \= 1/κ² is RETRACTED.** Since the A24 mediation **crosses the ℤ₂ seam** (ZS-F23: X-even → Y-odd through the Z-seam, no direct X–Y channel), its per-edge action is the corpus seam-flip:

**per-edge action \= t\_flip \= π/A** (one ℤ₂ half-event, ZS-M3 §6, DERIVED),   **S\_{X→Y} \= 2 × (π/A) \= 2π/A \= T\_micro**,

with the **factor 2 \= the two ℤ₂ half-events of one full seam event** — exactly v1.2's "two equal edges \= the same topological Z-Anchor," now identified with ZS-M3's T\_micro \= 2 t\_flip. **\[Gate 4 per-edge value: 1/κ² RETRACTED; per-edge \= π/A DERIVED-CONDITIONAL on the A24-edge \= ZS-M3-half-event identification; the Z-EFT θ-instanton route is superseded — the corpus seam action is π/A, not 1/κ².\]**

**The 1/κ² ↔ Λ motivation was numerology.** A23 chose per-edge \= 1/κ² because S\_{X→Y} \= 2/κ² gives e^{−2/κ²} ≈ 5×10⁻¹²⁰ ≈ (H̄₀/M̄\_P)² — a *fit* to the cosmological-constant scale. The corpus-grounded value gives e^{−2π/A} ≈ 8×10⁻³⁵, which is **not** Λ; and ZS-F1 §6.4 derives Λ **geometrically** (the (1 \+ A) modification with V(1) \= 0). The e^{−2/κ²} ≈ Λ coincidence is therefore an **anti-numerology RETRACTION**: it played no derivational role, the true seam action does not reproduce it, and Λ is geometric.

**v1.4 — the same-seam lemma fixes the scale.** The identification "A24 per-edge \= a ZS-M3 seam-flip" rests on one fact: the A24 seam *is* the ZS-M3 seam. ZS-F23's ℤ₂ seam grading is the J-grading of ZS-F0 §8.4 (Theorem 8.5–8.6: J|j⟩ \= |10−j⟩, the unique fixed point |5⟩, forced by **Q** \= 11 odd), and ZS-M3's Z-Telomere flips exactly this ℤ₂. They are **one object**, so the A24 mediation's seam crossing carries the ZS-M3 seam-flip action. ZS-M3 §8's hierarchy τ\_n \= t\_P e^{nπ/A} establishes **π/A as the fundamental per-flip action unit**; hence the per-edge action is fixed *at the π/A scale* (DERIVED), with per-edge \= t\_flip \= π/A and S\_{X→Y} \= T\_micro \= 2π/A on the two-edge \= two-half-event reading. The only residual is the leg-count (whether one A24 edge is one ℤ₂ half-event or half of one — i.e. per-edge \= π/A vs π/2A), which is **non-load-bearing**: the cosmological factor 2 and the π/A scale are DERIVED regardless, and nothing downstream depends on the exact multiple. **\[Gate 4 per-edge: scale π/A DERIVED (same-seam lemma \+ ZS-M3 §8); the exact value (π/A) DERIVED-CONDITIONAL on the leg-count, which is non-load-bearing.\]**

**§15. The Physics Payoff — B3 Absolute Scale and the C5 Clock-DOF Candidate \[OPEN\]**

**§15.1 B3 stays OPEN.** The II₁ trace carries precisely a state-independent additive constant (CLPW), which is *exactly* the freedom that leaves the absolute scale H̄/M̄\_P ≈ 5.9×10⁻⁶¹ undetermined. No action-level mechanism fixes it; the DERIVED hierarchy τ\_n \= t\_P·exp(nπ/**A**) (ZS-F10/U8) spans the range but does not pin H̄₀. **v1.3 note (anti-numerology RETRACTION).** v1.2 recorded, as an OBSERVATION, the hope that the per-edge instanton feeds B3 — *if* per-edge \= 1/κ² then e^{−2/κ²} ≈ 5×10⁻¹²⁰, within \~2 orders of (H̄₀/M̄\_P)² ≈ 3×10⁻¹²¹. **v1.3 retracts this:** §14.2 shows the corpus seam action is **π/A**, not 1/κ², giving e^{−2π/A} ≈ 8×10⁻³⁵ — nowhere near Λ. The e^{−2/κ²} ≈ Λ match was a numerological coincidence with no derivational role, and the true seam action does not reproduce it. ZS-F1 §6.4 derives Λ **geometrically** (the (1 \+ A) modification with V(1) \= 0). So B3 is **not** fed by the per-edge action and is **not** built on any e^{−2/κ²} coincidence. **A24 does not close B3.** \[OPEN; NON-CLAIM; the v1.2 per-edge↔B3 OBSERVATION is RETRACTED.\]

**§15.2 The clock DOF as a C5 candidate \[HYPOTHESIS-weak\].** The crossed product ⋊\_σ ℝ of Part II adjoins one continuous degree of freedom — the clock — which is structurally the Quintom ingredient (i) ("an extra propagating field") that A22 (Prop A22.8) requires for a healthy w \= −1 crossing. This registers the clock DOF as a C5 candidate. The barrier is A22's B1 (reflection-positivity / healthiness): the clock-sector EFT must be shown to propagate healthily in the IR and to satisfy OS-3. Neither is shown here. **The continuous-core lift opens, rather than closes, the C5 audit; a confirmed DESI crossing would activate it.** \[HYPOTHESIS-weak; closure route \= a reflection-positivity proof for the clock-sector EFT; failing chain \= OS-3 violation (ZS-M17.3).\]

**PART III — The Modular Half-Density Bridge: Finite-Register Unification (and the Conditional Lift)**

Part I built a reversible dynamics **L**\_π whose stationary distribution is the state-sampling weight π ∝ d\_i; Part II identified the observer weight ω ∝ d\_i². The two-Part split left open whether these are one structure. **At the finite-register level they are — not as one stationary state, but as two reversible dynamics on the same algebra M₁₁ joined by a modular half-density transform.** This Part proves the finite-register statement (and proves **L**\_ω is a genuine quantum-detailed-balance generator), then states precisely what remains to lift it to the continuous core (§U6, OPEN).

**§U1. The no-go (why a single generator does not suffice) \[PROVEN\].** The Part-I coarse generator is q\_{i→j} \= γd\_j, with stationary π\_i \= d\_i/D. Suppose the *same* generator were ω-detailed-balance. Then ω\_i q\_{i→j} \= γ d\_i² d\_j/S₂ would have to equal ω\_j q\_{j→i} \= γ d\_j² d\_i/S₂, i.e. d\_i \= d\_j. Since the sector dimensions differ,

**q\_{i→j} \= γd\_j cannot be detailed-balance for both π and ω** (verified: DB-π holds, DB-ω fails).

Quantum detailed balance, the GKLS detailed-balance adjoint, the jump-operator conditions, and the relative-entropy / gradient-flow structure are all defined *relative to a fixed faithful invariant state*. So π and ω require **two** generators, not a reinterpretation of one. This no-go is the reason v1.0's hope ("one **L**\_π explains both") fails, and it sets up the correct bridge.

**§U2. Trace and observer state are different functionals \[PROVEN\].** With the normalised matrix trace τ(x) \= (1/D)Tr(x), the sector projectors carry

**τ(P\_i) \= d\_i/D \= (3, 2, 6)/11 \= π,**

the Part-I stationary (this is the corrected Gate-2 statement, §12). The observer weight is the **state** ω(x) \= τ(h x) defined by the modular density

**h \= ⊕\_i (D d\_i/S₂) I\_{d\_i},    S₂ := Σ\_i d\_i² \= 49,    τ(h) \= 1,    ω(P\_i) \= τ(h P\_i) \= d\_i²/S₂ \= (9, 4, 36)/49.**

The modular flow of ω is σ\_t^ω(x) \= h^{it} x h^{−it}, so on a sector block C\_{ij} \= P\_i C P\_j it acts as σ\_t^ω(C\_{ij}) \= (h\_i/h\_j)^{it} C\_{ij} \= (d\_i/d\_j)^{it} C\_{ij} — **exactly the ZS-A23 / ZS-F19 modular ratio**, now recovered with no trace/state confusion. (Theorem A24.III-0.)

**§U3. The observer-balanced generator L\_ω \[PROVEN\].** Define microscopic jumps tilted by the modular half-density:

**L^ω\_{jβ←iα} \= √γ (h\_j/h\_i)^{1/4} |j,β⟩⟨i,α| \= √γ (d\_j/d\_i)^{1/4} |j,β⟩⟨i,α|,**

with reverse L^ω\_{iα←jβ} \= √γ (d\_i/d\_j)^{1/4} |i,α⟩⟨j,β|, for adjacent sectors (X–Z, Z–Y) and all microstate pairs. The coarse rate is q^ω\_{i→j} \= γ d\_j √(d\_j/d\_i) (each target sector j supplying d\_j microstates), and at the coarse level

**ω\_i q^ω\_{i→j} \= (γ/S₂) d\_i^{3/2} d\_j^{3/2} \= ω\_j q^ω\_{j→i}** (symmetric ⇒ ω-detailed-balance),

so the coarse generator is reversible with stationary ω \= (9, 4, 36)/49 (Theorem A24.III-1).

**Theorem A24.III-1b (full quantum detailed balance, PROVEN — v1.6).** On the *full* register M₁₁ (not merely the coarse 3×3), the GKLS generator **L**\_ω with the jumps above is **both KMS-symmetric and GNS-symmetric** with respect to ρ\_ω \= ⊕\_i (d\_i/S₂) I\_{d\_i}, is modular-covariant, and fixes ρ\_ω:

(i) **L**\_ω^\*(ρ\_ω) \= 0;

(ii) **\[L**\_ω, σ\_t^ω**\] \= 0**, since each jump is a modular eigenoperator, σ\_t^ω(|j,β⟩⟨i,α|) \= (d\_j/d\_i)^{it} |j,β⟩⟨i,α| (eigenvalue from h\_j/h\_i \= d\_j/d\_i);

(iii) **GNS symmetry:** ⟨X, **L**\_ω(Y)⟩\_GNS \= ⟨**L**\_ω(X), Y⟩\_GNS with ⟨X, Y⟩\_GNS \= Tr(ρ\_ω X† Y);

(iv) **KMS symmetry:** ⟨X, **L**\_ω(Y)⟩\_KMS \= ⟨**L**\_ω(X), Y⟩\_KMS with ⟨X, Y⟩\_KMS \= Tr(ρ\_ω^{1/2} X† ρ\_ω^{1/2} Y).

*Proof:* the paired modular relation ρ\_ω^{1/2} (L^ω\_{j←i})† ρ\_ω^{−1/2} \= L^ω\_{i←j} holds for every jump, and the jumps are modular eigenoperators, so the Frigerio–Gorini–Kossakowski–Verri / Fagnola–Umanità criterion gives GNS symmetry; GNS symmetry plus (ii) gives KMS symmetry. The explicit matrix-unit computation on M₁₁ verifies all four: the weighted-adjoint residuals ‖G\_GNS**L**\_ω − **L**\_ω^† G\_GNS‖ and ‖G\_KMS**L**\_ω − **L**\_ω^† G\_KMS‖ and ‖**L**\_ω^\*(ρ\_ω)‖ are \~10⁻¹⁸, and ‖\[**L**\_ω, σ\_t^ω\]‖ \= 0 exactly (zs\_a24\_v2\_1\_audit.py).  This upgrades v1.5's coarse-only detailed balance to a genuine quantum detailed-balance theorem; GNS and KMS symmetry are distinct conditions (Fagnola–Umanità), and both hold. Its full Liouvillian spectrum closes by the §6 invariant-subspace method (escape rates R\_i \= γ Σ\_{j∼i} d\_j √(d\_j/d\_i); recorded as an optional extension, §20).

**§U4. The modular interpolation family — full microscopic QMS \[DERIVED\].** The coarse rate interpolates the two generators by q^{(s)}\_{i→j} \= q^π\_{i→j} (h\_j/h\_i)^s, s ∈ \[0, ½\], with stationary measure μ^{(s)}\_i ∝ π\_i h\_i^{2s} (one line: μ^{(s)}\_i q^{(s)}\_{i→j} \= π\_i q^π\_{i→j} h\_i^s h\_j^s is symmetric in i ↔ j). To make "a family of QMS on M₁₁" literal, the **microscopic** generator is defined for every s by tilting each jump:

**L^{(s)}\_{jβ←iα} \= √γ (h\_j/h\_i)^{s/2} |j,β⟩⟨i,α|,    with invariant state   ρ\_s \= (⊕\_i h\_i^{2s} I\_{d\_i}) / Σ\_k d\_k h\_k^{2s}.**

**Theorem A24.III-2 (interpolation family, PROVEN).** For every s ∈ \[0, ½\], **L**\_{(s)} is a GKLS generator on M₁₁ with ρ\_s^{1/2} (L^{(s)}\_{j←i})† ρ\_s^{−1/2} \= L^{(s)}\_{i←j} (KMS detailed balance), invariant ρ\_s, and sector weight μ^{(s)}\_i \= Tr(P\_i ρ\_s) ∝ d\_i h\_i^{2s} \= π\_i h\_i^{2s}. The endpoints are **L**\_{(0)} \= **L**\_π (ρ\_0 \= I\_D/D, μ \= π ∝ d\_i) and **L**\_{(½)} \= **L**\_ω (ρ\_{½} \= ρ\_ω, μ \= ω ∝ d\_i²). *Proof:* the tilt is a modular half-density (Doob-type) transform; the displayed pairing is the GNS/KMS detailed-balance condition; verified at s \= 0, ¼, ½ on the full M₁₁ (stationarity, the pairing, and GNS/KMS symmetry, residuals \~10⁻¹⁸; zs\_a24\_v2\_1\_audit.py).  A single modular half-density interpolation thus carries the state-sampling dynamics to the operator-sampling dynamics through a continuum of genuine quantum Markov semigroups.

**§U5. Central Theorem \[DERIVED — finite-register\].**

**Theorem A24.III (finite-register trace/state unification).** The **state sampling** π ∝ d\_i and the observer **operator sampling** ω ∝ d\_i² are **not one stationary state** but the s \= 0 and s \= ½ endpoints of **one modular half-density interpolation** **L**\_{(s)}, a family of **QMS on M₁₁ that preserve the block-diagonal subalgebra N** \= M₃ ⊕ M₂ ⊕ M₆ (the cross-sector jumps |j,β⟩⟨i,α| are off-diagonal elements of M₁₁, not of **N**; restricting each **L**\_{(s)} to **N** gives the sector population process). With the single matrix trace τ on M₁₁, they are two reversible quantum dynamics joined by the modular half-density transform h \= ⊕\_i (D d\_i/S₂) I\_{d\_i}: **L**\_ω is obtained from **L**\_π by tilting each jump by (h\_j/h\_i)^{1/4}, ω(·) \= τ(h ·), and (Theorem A24.III-1b) **L**\_ω is KMS- and GNS-symmetric and modular-covariant. *Proof:* §§U1–U4. 

This is the complete unification **at the finite-register level**. Part I is the *dynamics* (how the register relaxes, stationary π); Part II is the *observer* (operator-space size-bias, ω); the **bridge** is the modular density h that both defines the A23 modular flow *and* maps **L**\_π to **L**\_ω. The conflation corrected in §12 (treating ω as the trace) was precisely what had hidden this: once the trace is π and ω is the modular state τ(h·), the two Parts are visibly one family.

**§U6. What is NOT yet unified — the continuous-core dynamical lift \[OPEN\].** PART III lives on the finite register M₁₁. Part II's actual object is the continuous-core corner M\_obs \= e**C**\_ω e, **C**\_ω \= 𝒜^III ⋊\_σ ℝ. §11 supplies a conditional expectation E : M\_obs → ι(M₁₁) intertwining the *population* generator (E∘𝓛 \= 𝓛\_pop∘E). What is **not** constructed is the dynamical lift of the *bridge*: a generator **𝓛**\_s on M\_obs with

**E ∘ 𝓛\_s \= L\_s ∘ E**   (intertwining), plus modular-clock covariance, complete positivity, core-trace preservation, and extension to the ℤ₂-graded core.

PART III thus proves the **finite-register modular unification** and supplies the **candidate finite-dimensional dynamics to be lifted**; the continuous-core dynamical unification is **OPEN** (F-A24.9). This is consistent with the Book/ZS-F23, which keep Condition C (the identification of a specific gravitational subregion algebra with the finite register) open under current tools. **\[Honest scope: "complete Part I ↔ Part II unification" would be an over-claim; the proven statement is the finite-register unification plus a conditional lift.\]**

**§16. Cross-Version Consistency Audit**

*Table 2\. Cross-version dependency audit (the buildup check of protocol §3.2).*

| Upstream result | Status | v1.5's effect | Safe? |
| ----- | ----- | ----- | ----- |
| ZS-A19/M6 **κ²** \= **A**/**Q** \= 35/4807 | PROVEN | the single generator coupling; unchanged | ✓ |
| ZS-M1 i-tetration z\\\* | PROVEN | not consumed; spectrum anchor only | ✓ |
| A23.5a/A23.14a π \= (3, 2, 6)/11 | PROVEN | Part I §3: stationary of the general generator | ✓ |
| ZS-Q7 cubic {0, −2**A**/**Q**, −**A**} | PROVEN | Part I §6: the population block of the 121-spectrum | ✓ |
| A23.MC ω \= (9, 4, 36)/49, σ\_t^ω \= (d\_i/d\_j)^{it} | PROVEN | §12/PART III: ω \= (9,4,36)/49 is the **state** τ(h·); the corner **trace** is π \= (3,2,6)/11 | ✓ |
| Takesaki dual weight (dual weight \= trace × density) | IMPORTED-PROVEN | §12: corrects v1.4 — the dual weight is τ(h·), so ω is the dual-weight **state**, not the trace | ✓ |
| A24 §6 invariant-subspace decomposition | PROVEN (this work) | general exact spectrum A24.I-4G; 121×121 becomes a regression test | ✓ |
| A24 PART III modular half-density bridge | DERIVED (finite-register) | **L**\_π (π) and **L**\_ω (ω) unified as s \= 0, ½ endpoints **on M₁₁**; continuous-core lift OPEN (F-A24.9) | ✓ |
| A24 §U3 full quantum detailed balance of **L**\_ω | PROVEN (this work) | KMS- and GNS-symmetric on M₁₁, \[**L**\_ω, σ\_t^ω\] \= 0, **L**\_ω^\*(ρ\_ω) \= 0 (matrix-unit, \~10⁻¹⁸) | ✓ |
| Fagnola–Umanità GNS/KMS detailed-balance structure | IMPORTED-PROVEN | §U3: criterion for GNS ⇒ KMS symmetry of **L**\_ω; the bridge machinery is standard (positioning) | ✓ |
| A23.15 modular detailed balance −Δ**K** | PROVEN | Part I §4; the KMS link to the modular clock | ✓ |
| ZS-F19 Δ**K**\_{X→Y} \= −ln 2, lattice \= UV regulator | DERIVED | §10: II∞ core regulator; §12: offset matching | ✓ |
| ZS-F23 ℤ₂ seam grading (J, J\_Z) | PROVEN | §10: the trace-preserving β | ✓ |
| ZS-F2 §11.4 Ω\_Λ \= 83/121, Thm 11.7 | DERIVED | §13: **partition (6,32,83) \= (F(cube), F(TI), rem.) DERIVED**; Gate 3 → DERIVED-COND. | ✓ |
| CLPW de Sitter Type II₁, max-entropy \= empty dS | IMPORTED-PROVEN | §10–§12: the continuous core and offset | ✓ |
| ZS-F1 Z-Anchor vortex (global; §6.4 Λ) | PROVEN | §14: equal-edge doubling DERIVED; vortex route closed → **per-edge \= π/A (ZS-M3)**; geometric Λ | ✓ |
| A23 G12b-exponent 1/κ² \= **Q**/**A** | PROVEN | §14: **RETRACTED as the per-edge action** (numerology; no corpus instanton \= 1/κ²); stays the LOCKED inverse-coupling | ✓ (corrected) |
| ZS-M3 §6 t\_flip \= π/A, T\_micro \= 2π/A, S\_tunnel \= 5π/A | DERIVED | §14: **per-edge \= π/A (seam half-event)**, S\_{X→Y} \= 2π/A \= T\_micro, factor 2 \= two half-events | ✓ |
| ZS-F0 §8.5 Wilson loop \= BV–BFV cobordism invariant | DERIVED | §13: Z-sector partition function is **topological** ⇒ holography combinatorial, not metric | ✓ |
| **v1.0 A24.1a (M₁₁ ⋊ ℝ Type II)** | **RETRACTED** | §9: finite route CLOSED-NEGATIVE; replaced by §10–§11 | ✓ (corrected) |

**Result.** No version conflict. v1.3 *consumes* the locked anchors with zero new fitted parameters; it consumes ZS-M3 §6 (the seam-flip per-edge action), ZS-A23.MC (the operator-sampling weight), and ZS-F0 §8.5 (the cobordism/combinatorial holography), and it retracts only A24's own over-claims (the v1.0 finite route and the A23 per-edge \= 1/κ² guess). Nothing upstream is disturbed. **\[DERIVED.\]**

**§17. Consolidated Gate Ledger**

*Table 3\. Consolidated gate ledger (v2.1).*

| Gate | Calculation | Status (v1.5) |
| ----- | ----- | ----- |
| G-I.general (A24.I-1) | q\_{ij} \= Γ₀κ²a\_{ij}d\_j on any connected graph; π \= d/Σd | PROVEN. |
| G-I.Htheorem (A24.I-3) | exact H-theorem; **Q**/2; reverse rates 2:3:6:2 | PROVEN. |
| G-I.uniqueness (A24.I-uniq) | one scalar per edge (Schur, PROVEN) \+ global edge-homogeneity ⇒ unique | **DERIVED** (the full uniqueness rests on the single-κ² action-level homogeneity input; the per-edge Schur step alone is PROVEN). |
| G-I.Liouvillian (A24.I-4) | full 121×121 spectrum {0,−2A/Q,−A/2,−9A/Q,−A}, mult (1,80,36,3,1) | PROVEN (NEW). |
| G-I.spectrum (A24.I-4G) | general exact Spec(**L**) for any (a,b,c); Z-Spin {0,−2A/Q,−A/2,−9A/Q,−A} | PROVEN (v1.5, representation-theoretic; 121×121 \= regression). |
| G-I.stability (A24.I-5) | reciprocal: π exact, gap (1±ε); directional 3-state: exact π, g\_±, TV, forward-only gap; generic: numerical | **PROVEN** (§7.1–7.2) / VERIFIED-NUMERICAL (§7.3). |
| G-II.finite-route (A24.II-0) | M₁₁ ⋊\_{σ^ω} ℝ is Type I (inner action) | CLOSED-NEGATIVE; v1.0 claim RETRACTED. |
| G-II.core (A24.II-1) | 𝒜^III ⋊\_σ ℝ \= II∞ continuous core | IMPORTED-PROVEN (Witten/CLPW/Takesaki). |
| G-II.corner (A24.II-2) | e**C**\_ω e \= II₁; ι: M₁₁ ↪ M\_obs | DERIVED-CONDITIONAL on the embedding. |
| G2(i) observer trace/state (A24.II-3) | corner trace \= matrix trace \= π \= (3,2,6)/11; observer weight ω \= τ(h·) \= (9,4,36)/49 | **DERIVED** (corrected v1.5: trace \= π, ω \= modular state via h; restores A23 consistency). |
| G-III unification (A24.III) | **L**\_π (π) and **L**\_ω (ω) joined by modular half-density h on **M₁₁**; one family **L**\_{(s)}, s ∈ \[0,½\] | **DERIVED (finite-register)** (no-go PROVEN, **L**\_ω PROVEN, interpolation DERIVED). |
| G-III.DB full quantum DB (A24.III-1b) | **L**\_ω KMS- and GNS-symmetric on M₁₁; \[**L**\_ω, σ\_t^ω\]=0; **L**\_ω^\*(ρ\_ω)=0 | **PROVEN** (matrix-unit, v1.6). |
| G-III.lift continuous-core (F-A24.9) | ∃ **𝓛**\_s on M\_obs with E∘**𝓛**\_s \= **L**\_s∘E \+ modular covariance \+ CP \+ core-trace | **OPEN** (the single honest gap; candidate finite dynamics supplied). |
| G2(ii) CLPW offset (A24.II-4) | S₀ \= **A**\_dS/4G; residual \= B3 | IMPORTED-MATCHING / DERIVED-CONDITIONAL. |
| G3 face partition (§13) | (6,32,83) \= (F(cube), F(TI), rem.), ZS-F2 §11.4 | **DERIVED**; realised as II₁ trace-1/121 projections. |
| G3 face weight (§13) | one quantum per face \= combinatorial (not metric) | **combinatorial nature DERIVED** (ZS-F0 §8.5 cobordism); residual \= F0's deferred explicit state-sum. |
| G4 factor 2 (A24.II-5) | S\_{X→Y} \= 2 S\_vortex (equal edges) | DERIVED (topological Z-Anchor). |
| G4 per-edge (A24.II-7) | 1/κ² RETRACTED; per-edge \= π/A (ZS-M3 ℤ₂ half-event) | **per-edge \= π/A DERIVED-CONDITIONAL**; S\_{X→Y}=2π/A=T\_micro; 1/κ²↔Λ numerology retracted. |
| G-B3 (§15.1) | absolute scale H̄/M̄\_P | OPEN — corpus-wide debt. |
| G-C5 (§15.2) | clock DOF ⋊ℝ as Quintom field (i) | HYPOTHESIS-weak — B1 reflection-positivity pending. |

**§18. Falsification Gates**

Multilayer falsification (protocol §3.5): mathematical/theoretical, simulation/consistency, observational/external.

* **F-A24.1 (mathematical — now correctly read).** "If σ^ω is inner, the finite crossed product is Type I and a finite-route Type II claim fails." σ^ω \= Ad(ρ\_ω^{it}) **is** inner (Skolem–Noether); F-A24.1 is **TRIGGERED**, and the finite-route claim is retracted (§9). The genuine route (§10) starts from the Type III₁ algebra whose modular flow is outer, and is not subject to this gate.

* **F-A24.2 (mathematical).** If the full Liouvillian spectrum is **not** {0, −2A/Q, −A/2, −9A/Q, −A} with multiplicities (1, 80, 36, 3, 1), Theorem A24.I-4G fails. *Check:* the representation-theoretic theorem matches the 121×121 build and the (2,3,4) control (audit). \[Cleared.\]

* **F-A24.3 (mathematical).** If π \= d/Σd is **not** stationary/reversible for a connected graph, Theorem A24.I-1 fails. *Check:* three test graphs pass (audit I.1). \[Cleared.\]

* **F-A24.4 (instanton — the priority gate, resolved in v1.3).** If the per-edge action differs from the claimed value, the claim fails. *Result (v1.3):* the per-edge \= 1/κ² claim is **RETRACTED** — no corpus instanton has action 1/κ² \= **Q**/**A** ≈ 137.34 (the corpus actions are t\_flip \= π/A, T\_micro \= 2π/A, S\_tunnel \= 5π/A, S\_cl \= 35π/3; Q/π ≈ 3.5 is not a flip count), and the 1/κ²↔Λ motivation was numerology. Since the A24 mediation crosses the ℤ₂ seam (ZS-F23), the corrected per-edge action is the **DERIVED seam-flip t\_flip \= π/A** (ZS-M3 §6), with S\_{X→Y} \= 2π/A \= T\_micro and **factor 2 \= two half-events** (DERIVED). \[Fired against 1/κ²; the per-edge value is corrected to the corpus seam-flip π/A.\]

* **F-A24.5 (consistency — observer trace/state, corrected v1.5).** If the corner trace were not the matrix trace π \= (3, 2, 6)/11, or the observer state ω(·) \= τ(h·) not equal to (9, 4, 36)/49, Gate 2 would fail. *Status (v1.5):* **DERIVED** — τ(P\_i) \= d\_i/D \= (3, 2, 6)/11 is the matrix trace, and ω(P\_i) \= τ(h P\_i) \= d\_i²/Σd\_j² \= (9, 4, 36)/49 with h\_i \= D d\_i/Σd\_j² (both verified). v1.4's identification of the corner *trace* with ω is **corrected**: the dual weight is the trace times h, so ω is the dual-weight *state*. This restores consistency with ZS-A23 (trace weights \= (3, 2, 6)/11; ω\_reg \= (9, 4, 36)/49) and enables the PART III unification.

* **F-A24.6 (observational — Part I).** A small 3-2-6 open-system simulator measuring p(∞) ≠ (3, 2, 6)/11, or λ\_fast/λ\_slow ≠ 11/2, or cross-sector coherence decay ≠ **A**/2, falsifies the Part I dynamics. \[TESTABLE now.\]

* **F-A24.7 (unification — PART III).** If a single generator could be detailed-balance for both π and ω (contradicting the no-go), or if the tilted generator **L**\_ω with q^ω\_{i→j} \= γd\_j√(d\_j/d\_i) did not have stationary ω \= (9, 4, 36)/49, or if the interpolation μ^{(s)} ∝ π\_i h\_i^{2s} did not run from π (s \= 0\) to ω (s \= ½), the modular half-density bridge fails. *Check:* the no-go, **L**\_ω detailed balance, and the interpolation endpoints all verify (audit). \[Cleared.\]

* **F-A24.8 (observational — C5).** A confirmed healthy phantom-divide crossing (DESI \+ global model comparison) activates the clock-DOF C5 candidate (§15.2), which must then provide the healthy crossing or be excluded by B1.

* **F-A24.9 (continuous-core lift — OPEN).** The finite-register unification (PART III) lifts to the continuous core only if there exists a generator **𝓛**\_s on M\_obs \= e**C**\_ω e with E∘**𝓛**\_s \= **L**\_s∘E (intertwining the §11 conditional expectation), modular-clock covariance, complete positivity, core-trace preservation, and a ℤ₂-graded extension. No such **L**\_s is constructed here. *Status:* **OPEN** — the single honest gap of A24; its closure would promote "finite-register unification" to "Part I ↔ Part II dynamical unification." Consistent with the Book/ZS-F23 keeping Condition C open.

**§19. Conclusion**

ZS-A23 reduced the corpus's dynamical core to one dimension-weighted mediator generator. v1.0 of A24 attempted to lift it to a de Sitter observer algebra but mis-identified a finite inner crossed product as Type II. The genuine Type III₁ → II∞ continuous core corrects that, and the present work develops the programme in three Parts — the dimension-weighted dynamics (I), the honest continuous-core lift (II), and the finite-register modular bridge (III).

**Part I** is a self-contained, PROVEN theory of dimension-weighted mediator semigroups: a general connected-graph stationary law, modular detailed balance, an exact H-theorem, a unique sector-covariant GKLS realisation, an **exact general Liouvillian spectrum** (Theorem A24.I-4G, any (a, b, c); for Z-Spin {0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**} with the cross-sector coherences decaying at the clean rate **A**/2), and **two PROVEN perturbation theorems** (a reciprocal Dirichlet-form gap bound and an exact directional 3-state analysis with a forward-only first-order gap shift), generic microscopic errors staying numerical. Every relaxation and decoherence rate is a rational multiple of **A**, with zero new parameters; the whole of Part I is testable on a small open-system simulator.

**Part II** rebuilds the lift on the correct algebraic footing. The finite route is **retracted** (an inner modular flow cannot generate a Type II factor); the genuine continuous core is the Type III₁ → II∞ crossed product 𝒜^III ⋊\_σ ℝ (IMPORTED-PROVEN), with a finite II₁ corner e**C**\_ω e and a register embedding ι : M₁₁ ↪ e**C**\_ω e (DERIVED-CONDITIONAL). The register embeds, ι : M₁₁ ↪ e**C**\_ω e (DERIVED-CONDITIONAL on the embedding's existence and modular-density compatibility; the corner trace is automatically the matrix trace π \= (3, 2, 6)/11). The observer weight ω \= (9, 4, 36)/49 is recovered **not** as a trace but as the modular *state* τ(h·) (v1.5/§12), and the CLPW offset **A**\_dS/4G under an empty-de-Sitter reference (IMPORTED-MATCHING). The face-embedding target is realised in II₁ continuous trace dimension (τ(q\_a) \= 1/121, coarse trace (6, 32, 83)/121), well-posed where the v1.0 rank statement was impossible; **v1.2 grounds the partition in ZS-F2 §11.4** — (6, 32, 83\) \= (F(cube), F(truncated icosahedron), remainder) — and **v1.3 resolves the equal-weight as combinatorial** (not metric) holography, since ZS-F0 §8.5 makes the Z-sector partition function a BV–BFV cobordism invariant (Gate 3: DERIVED-CONDITIONAL, residual \= F0's deferred explicit state-sum). The Gate-2 observer weight (9, 4, 36)/49 is **PROVEN** as the operator-sampling weight (ZS-A23.MC), but **v1.5 corrects its operator-algebra identity**: the corner **trace** is the matrix trace \= π \= (3, 2, 6)/11 (the Part-I stationary), while ω \= (9, 4, 36)/49 is the **state** τ(h·) given by the modular density h (v1.4 had conflated this state with the trace, contradicting its own audit and ZS-A23). The surviving residuals are explicitly upstream (ZS-F0's deferred state-sum, CLPW's reference state), corpus-wide (B3), or registered (C5). The two-edge instanton **factor 2 is DERIVED**, and **v1.3 corrects the per-edge value**: 1/κ² is **RETRACTED** (no corpus instanton equals it; the 1/κ²↔Λ match was numerology), and the corpus-grounded per-edge action is the **ℤ₂ seam-flip t\_flip \= π/A** (ZS-M3 §6, DERIVED), with S\_{X→Y} \= 2π/A \= T\_micro and the factor 2 \= two half-events. Λ remains geometric (ZS-F1 §6.4), decoupled from the seam action.

**Part III** is the unification the two-Part split had gestured at — **at the finite-register level**. A no-go shows a single generator cannot detailed-balance both the state weight π ∝ d\_i and the operator weight ω ∝ d\_i². The correct picture (forced by the §12 trace/state correction) is **two** reversible dynamics on the *same* register algebra M₁₁ with the *same* trace π: the dimension-weighted **L**\_π (stationary π) and the observer-balanced **L**\_ω (stationary ω, jumps tilted by (h\_j/h\_i)^{1/4}), joined by the **modular half-density** h and embedded in one interpolation family **L**\_{(s)}, s ∈ \[0, ½\]. v1.6 proves **L**\_ω is a genuine quantum-detailed-balance generator (KMS- *and* GNS-symmetric on M₁₁, modular-covariant). The central theorem A24.III states it plainly: *finite-register state sampling and observer operator sampling are not one stationary state but two reversible quantum dynamics joined by a modular half-density transform.* This unifies Part I (the dynamics) and Part II (the observer) **on the finite register**, and supplies the candidate dynamics to be lifted; the **continuous-core dynamical lift** — a generator **𝓛**\_s on M\_obs \= e**C**\_ω e intertwining the conditional expectation with modular covariance and complete positivity — remains the single honest **OPEN** item (F-A24.9).

**Relation to standard constructions.** The individual tools used here — the modular (Doob-type) half-density tilt of a generator, KMS- and GNS-symmetric quantum Markov semigroups, and Dirichlet-form / Rayleigh–Ritz spectral-gap bounds — are **standard** (Fagnola–Umanità; the quantum-Doob / tilted-Lindblad literature). A24 does **not** claim them as new mathematics. Its contribution is the *exact package* assembled on one specific object: the dimension-weighted 3-2-6 register, where the dimension multiplicity fixes the exact Liouvillian spectrum (A24.I-4G), the two stationary samplings (π ∝ d, ω ∝ d²) are the modular-bridge endpoints, and the whole is a concrete small-simulator proposal. The "first exact spectrum of the isotropic complete-bipartite Lindbladian" framing is stated as a clean reusable proposition pending a fuller literature search, not as a major-problem resolution.

**Net.** The semigroup is a complete open-quantum-systems theory with an exact general spectrum, two PROVEN perturbation theorems, and a full quantum-detailed-balance theorem for the observer generator; the continuous-core lift is correctly founded; **Parts I and II are unified by the modular half-density bridge at the finite-register level**, with the continuous-core dynamical lift the single honest OPEN item (F-A24.9). The cosmological-constant problem is localised to the same named, falsifiable items — the Gate-2(ii) reference state, the B3 absolute scale, and the per-edge instanton normalisation. The corpus standard is maintained: the central trace-vs-state conflation carried from v1.0 is corrected, the central claim is bounded to what is proved, anti-numerology enforced, every over-claim retracted or made conditional. Zero free parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED**.

**§20. Remaining Programs**

**As of v2.0: the finite-register mathematics is final; the single honest OPEN item is the continuous-core dynamical lift. The remaining items are upstream, corpus-wide, registered, or optional extensions.**

3. **(continuous-core dynamical lift — the single honest OPEN, F-A24.9)** Construct a generator **𝓛**\_s on M\_obs \= e**C**\_ω e with E∘**𝓛**\_s \= **L**\_s∘E (intertwining the §11 conditional expectation), modular-clock covariance, complete positivity, core-trace preservation, and a ℤ₂-graded extension. PART III supplies the candidate finite-dimensional dynamics; this lift would promote the finite-register unification to a genuine Part I ↔ Part II dynamical unification. Consistent with the Book's open Condition C.

4. **(embedding — Gates 2, 3: A24-internal part CLOSED)** Gate 2 is DERIVED with the corrected trace/state reading (§12); Gate 3's partition and combinatorial nature are DERIVED. The single surviving embedding item is **upstream, not A24's**: the *explicit* ZS-F0 face-weight state-sum (a Turaev–Viro / Barrett–Westbury realisation forcing the equal 1/121 weight) is ZS-F0's own deferred categorical formalisation (F0 §166). A24 has supplied the local monoidal-functor argument; the categorical polish is ZS-F0's.

5. **(per-edge — Gate 4: scale DERIVED)** The per-edge action is the ZS-M3 seam-flip at the **π/A scale** (same-seam lemma \+ ZS-M3 §8, DERIVED), with per-edge \= t\_flip \= π/A and S\_{X→Y} \= T\_micro \= 2π/A. The only residual is the **non-load-bearing** leg-count (π/A vs π/2A); the cosmological factor 2 and the scale are DERIVED, and Λ is geometric (ZS-F1 §6.4), decoupled.

6. **(Gate 2(ii) — upstream)** The CLPW entropy offset S₀ \= **A**\_dS/4G is IMPORTED-MATCHING from CLPW's empty-de-Sitter reference state.

7. **(B3)** The action-level absolute IR scale H̄/M̄\_P (the corpus-wide debt; not local to A24).

8. **(C5)** A reflection-positivity proof (or B1 exclusion) for the clock-sector EFT.

9. **(L\_ω full spectrum — optional extension)** The observer-balanced **L**\_ω (PART III) has an exact spectrum by the §6 invariant-subspace method (sector-internal traceless modes at −R\_i, multiplicity d\_i²−1; cross-sector coherences at −(R\_i+R\_j)/2, multiplicity 2d\_id\_j; and the 3-state identity block giving 0, −g\_−^ω, −g\_+^ω from the §7.2 formula), with R\_i \= γ Σ\_{j∼i} d\_j√(d\_j/d\_i). Writing it out gives a second full Liouvillian theorem; not required for the unification.

10. **(full graded Liouvillian)** Extend to the spin-graded core **C**\_ω ⋊ β and the continuous-clock sector, with the modular-flow phases (d\_i/d\_j)^{it} as the conservative companion to the §6 dissipative spectrum.

**Appendix A — General Proof of the Stationary Law (Theorem A24.I-1)**

For a connected undirected graph with adjacency a\_{ij} \= a\_{ji} and node multiplicities d\_i, set q\_{i→j} \= Γ₀κ²a\_{ij}d\_j (i ≠ j), q\_{i→i} \= −Σ\_{k≠i} q\_{i→k}. Detailed balance with π\_i \= d\_i/D (D \= Σ\_k d\_k): π\_i q\_{i→j} \= (d\_i/D)Γ₀κ²a\_{ij}d\_j \= (Γ₀κ²/D)a\_{ij}d\_i d\_j, which is symmetric in i, j (a\_{ij} \= a\_{ji}); hence π\_i q\_{i→j} \= π\_j q\_{j→i}. Summing over j: Σ\_j π\_i q\_{i→j} \= Σ\_j π\_j q\_{j→i}, i.e. (πQ)\_i \= 0, so π is stationary. Connectedness ⇒ the chain is irreducible ⇒ π is unique. Reversibility ⇒ ℒ is self-adjoint in the π-weighted inner product, so the spectrum is real and the relaxation is monotone (Theorem A24.I-3). 

**Appendix B — The Full 121×121 Liouvillian (Theorem A24.I-4)**

Hilbert space **H** \= ℂ³ ⊕ ℂ² ⊕ ℂ⁶ (X \= {0,1,2}, Z \= {3,4}, Y \= {5,…,10}). Jump operators L\_{(j)←(i)} \= √(Γ₀κ²)|j⟩⟨i| for every ordered adjacent pair on the path X–Z–Y (X↔Z and Z↔Y, both directions; no X–Y): 6 \+ 6 (X–Z) \+ 12 \+ 12 (Z–Y) \= 36 operators. The Liouvillian on ℒ(**H**) ≅ ℂ¹²¹ is, in column-stacking convention,

ℒ \= Σ\_k \[ L̄\_k ⊗ L\_k − ½(I ⊗ L\_k†L\_k \+ (L\_k†L\_k)ᵀ ⊗ I) \].

By the analytic Theorem A24.I-4G (§6, invariant-subspace decomposition) the spectrum is, for Z-Spin, Spec(ℒ) \= {0, −2**A**/**Q**, −**A**/2, −9**A**/**Q**, −**A**} with multiplicities (1, 80, 36, 3, 1), Σ \= 121\. As an **independent reproduction** (regression test, not the derivation), numerical diagonalisation of the 121×121 superoperator at Γ₀κ² \= 1 returns exactly {0, −2, −11/2, −9, −11}×κ² with the same multiplicities, all eigenvalues real (max |Im| \< 10⁻⁹). The 36-fold −**A**/2 block is the cross-sector coherence space (X–Z: 6+6; Z–Y: 12+12 \= 36). Reproduced by zs\_a24\_v2\_1\_audit.py (the analytic theorem and the numerical spectrum agree for (3, 2, 6\) and the (2, 3, 4\) control). 

**Appendix C — The Bogomolnyi Per-Edge Action (Computation A24.II-6)**

**v1.2 — the Z-Anchor is a global vortex.** ZS-F1 §7 keeps the Goldstone massless and physical (ΔN\_eff \= 0), so the U(1) is global and the energy is **log-divergent**, E ≈ π v² ln(L/ξ) — the BPS-finite tension below is the *gauged counterfactual*, recorded to show the per-edge value even in the most favourable (BPS) reading. Critically-coupled abelian Higgs model (λ \= e²/2), Euclidean action S \= ∫d²x\[¼F² \+ |Dφ|² \+ (λ/4)(|φ|²−v²)²\]. Bogomolnyi completion: S \= ½∫\[F₁₂ ∓ e(|φ|²−v²)\]² \+ |D₁φ ∓ iD₂φ|² ± e v²∫F₁₂, with bound S ≥ e v²|∫F₁₂| \= e v²|Φ\_B|, Φ\_B \= 2πn/e (flux quantisation). Saturation: S\_vortex \= 2π v²|n|. With v \= 1 (M̄\_P units), n \= 1: S \= 2π ≈ 6.283. Target 1/κ² \= **Q**/**A** \= 4807/35 ≈ 137.343. Condition for S\_vortex \= 1/κ²: v²|n| \= 1/(2πκ²) \= **Q**/(2π**A**) \= 4807/(70π) ≈ 21.859 — i.e. n ≈ 22 (v \= 1), excluded by the minimal stable winding n \= 1 (ZS-F1 §5). Both readings (global log-divergence; gauged 2π) miss 1/κ², so the vortex per-edge route is closed. **v1.3:** the corpus instanton ledger (t\_flip \= π/A, T\_micro \= 2π/A, S\_tunnel \= 5π/A, S\_cl \= 35π/3) contains no action equal to 1/κ² (Q/π ≈ 3.5 is not a flip count), so per-edge \= 1/κ² is **RETRACTED**; since the A24 mediation crosses the ℤ₂ seam (ZS-F23), the corrected per-edge action is the ZS-M3 §6 half-event **t\_flip \= π/A**, with S\_{X→Y} \= 2π/A \= T\_micro. Reproduced by zs\_a24\_v2\_1\_audit.py checks F4.b–c, the global-vortex check, and the corpus-instanton-ledger check. 

**Appendix D — Anti-Numerology Pre-Registration**

*MC \#1 — the face triple (6, 32, 83).* Uniform random ordered 3-partition of 121 into positive parts; P(unordered set \= {6, 32, 83}) \= 6/C(120, 2\) \= 6/7140 ≈ 8.40×10⁻⁴ (Monte-Carlo 2×10⁵: 0.00090). P ≪ 5%, so the Gate-3 target is **non-generic**; a future Φ\_face derivation landing on it is meaningful, not a fit. (A24 does not derive it.)

*MC \#2 — the per-edge value 1/κ² \= Q/A ≈ 137.343.* The coincidence with 1/α\_em ≈ 137 is reported as an **OBSERVATION** and used in no derivation. The value is the LOCKED inverse-coupling, not a fit. **v1.3 note:** 1/κ² is *not* the per-edge instanton action — that identification (and the e^{−2/κ²} ≈ Λ motivation behind it) is RETRACTED as numerology (§14.2); the corpus per-edge action is π/A (ZS-M3 §6). 1/κ² remains only the inverse-coupling.

*Cross-version safety.* z\\\* (ZS-M1), **κ²** \= 35/4807 (ZS-A19/M6), π \= (3, 2, 6)/11 (A23.5a), ω \= (9, 4, 36)/49 (A23.MC), the population spectrum {0, −2**A**/**Q**, −**A**} (ZS-Q7) are unchanged and consumed; zero new fitted parameters.

**Acknowledgements and Code Availability**

This v2.1 is the consolidated public release; the full development is recorded in Appendix E and the Version History. The Gate-2 operator-algebra identity is correct — the II₁-corner *trace* is the matrix trace π \= (3, 2, 6)/11, while the observer weight ω \= (9, 4, 36)/49 is the *state* τ(h·) given by the modular density h — and PART III builds the **modular half-density bridge**. The central claim is **bounded to the finite-register level** (the continuous-core dynamical lift is the single honest OPEN item, F-A24.9), **proves the full quantum detailed-balance theorem** (Theorem A24.III-1b: **L**\_ω is KMS- *and* GNS-symmetric on M₁₁, modular-covariant, ρ\_ω-stationary, by explicit matrix-unit computation), and fixes the residual textual errors. No new physics is added. The continuous-core construction follows Takesaki's continuous decomposition and the gravitational crossed-product programme of Witten and Chandrasekaran–Longo–Penington–Witten; the trace/state split and modular density follow Tomita–Takesaki theory; the GNS/KMS detailed-balance structure follows Fagnola–Umanità and the tilted-Lindblad / quantum-Doob literature (standard machinery — A24's contribution is the exact package on the specific 3-2-6 register); the spectrum theorem follows the Lindblad/representation-theory of the GKLS generator; the perturbation theorems follow Dirichlet-form / Rayleigh–Ritz and the matrix-tree theorem.

zs\_a24\_v2\_1\_audit.py (exact symbolic \+ Monte-Carlo, runnable; **54/54 computational, regression, and consistency checks PASS** — not 53 separate theorem proofs) covers, by Part: **Part I** — the general-graph stationary law, modular detailed balance, the exact H-theorem, the Schur-uniqueness inputs, the exact general spectrum A24.I-4G against the 121×121 build and the (2, 3, 4\) control, and the two perturbation theorems (reciprocal Dirichlet sandwich, directional exact stationary/decay-rates/TV/forward-only gap, and the full 121×121 microscopic Monte Carlo); **Part II** — the Gate-1 inner-action retraction, the Gate-3 partition (6, 32, 83)/121, the operator-dimension weights (9, 4, 36\) with Σ \= 49, the F-A24.4 Bogomolnyi coefficient and global-vortex finding, the corpus-instanton ledger and per-edge retraction, and the trace/state split (corner trace π \= (3, 2, 6)/11 vs ω \= τ(h·) \= (9, 4, 36)/49); **Part III** — the no-go, the full quantum detailed balance of **L**\_ω on M₁₁ (KMS- and GNS-symmetric, modular-covariant, ρ\_ω-stationary, residuals \~10⁻¹⁸), and the microscopic interpolation family **L**\_{(s)} (stationarity, KMS pairing, and endpoints at s \= 0, ¼, ½); plus the anti-numerology face-triple test and cross-version safety. NOTE: "these are computational/regression/consistency verifications, **not** theorem proofs (the theorems carry their own proofs in the text); the unification is **finite-register**, and the **continuous-core dynamical lift is the single honest OPEN item** (F-A24.9); the surviving residuals — the Gate-2(ii) CLPW reference, the per-edge leg-count, ZS-F0's explicit state-sum, and B3 — are upstream, registered, or non-load-bearing." Independent rerun recommended. This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility.

**Appendix E — Deep-Exploration Records (v1.2–v2.0, condensed)**

Each version was developed by the standard exploration protocol (Step 0 long-list → Step 1 MECE issue-list → Step 2 issue-tree → Step 3 epistemic-status assignment → Step 4 convergence → Step 5 value). The records below are the condensed audit trail; status tags use the legend of §0.

**v1.2 — the two §20 programs (Gate-3 partition; per-edge vortex).** *Issue-list:* (I1) the ℂ¹²¹ face partition; (I2) the per-edge instanton as a Bogomolnyi vortex. *Status:* I1 **DERIVED** — the coarse traces (6, 32, 83)/121 are (F(cube), F(truncated icosahedron), remainder) from ZS-F2 §11.4; I2 **CLOSED-NEGATIVE** — the minimal BPS vortex action is 2π, not 1/κ², so the per-edge-vortex route fails. *Convergent;* value: grounded the Gate-3 partition, excluded a wrong instanton route.

**v1.3 — closing the two §20 residuals.** *Issue-list:* (I1) the per-edge action value; (I2) the observer-weight status; (I3) the e^{−2/κ²}↔Λ motivation. *Status:* I1 **RETRACTED→DERIVED** — 1/κ² has no corpus instanton (the corpus actions are π/A, 2π/A, 5π/A, 35π/3); the corrected per-edge action is the ℤ₂ seam-flip t\_flip \= π/A (ZS-M3 §6), S\_{X→Y} \= 2π/A; I2 **PROVEN** — ω \= (9, 4, 36)/49 \= d\_i²/Σd\_j² two ways (ZS-A23.MC); I3 **RETRACTED** as numerology. *Convergent;* value: removed two over-claims, fixed the per-edge scale.

**v1.4 — last internal closure \+ residual audit.** *Issue-list:* (I1) the corner-trace identification; (I2) the per-edge same-seam lemma; (I3–4) the residual audit and C5. *Status (as recorded then):* I1 "DERIVED via Takesaki" — **later corrected in v1.5** (the dual weight is the trace times the modular density, so that argument fixes the *state* ω, not the trace); I2 **DERIVED** — the A24 seam is the ZS-F23/ZS-F0 §8.4 J-grading \= the ZS-M3 ℤ₂, fixing the scale at π/A; residuals located as upstream/registered. *Convergent;* value: clarified residuals; its Gate-2 statement was the error v1.5 fixed.

**v1.5 — finite-register trace/state unification \+ Gate-2 correction.** *Issue-list:* (I1) the trace/state correction; (I2) the general exact spectrum; (I3) the two perturbation theorems. *Status:* I1 **DERIVED** — corner trace \= matrix trace \= (3, 2, 6)/11 \= π; ω \= (9, 4, 36)/49 \= τ(h·) is the modular *state* (correcting the v1.4 conflation, restoring consistency with ZS-A23); no-go PROVEN; **L**\_ω PROVEN; interpolation DERIVED; I2 **PROVEN** (Theorem A24.I-4G); I3 **PROVEN** (reciprocal \+ directional). *Convergent;* value: fixed the central conflation, built the modular bridge — but over-stated it as "complete Part I↔II unification."

**v1.6/v2.0 — scope correction, full quantum detailed balance, and the v2.0 patch.** *Issue-list:* (I1) bound the claim to finite-register; (I2) the full quantum DB theorem; (I3) symbol/textual fixes; (I4) audit strengthening. *Status:* I1 **DERIVED (finite) / OPEN (lift)** — PART III unifies π and ω on M₁₁ and supplies the candidate dynamics; the continuous-core dynamical lift (a generator **𝓛**\_s on M\_obs with E∘**𝓛**\_s \= **L**\_s∘E, modular covariance, CP) is **OPEN** (F-A24.9); I2 **PROVEN** (Theorem A24.III-1b: **L**\_ω is KMS- and GNS-symmetric on M₁₁, modular-covariant). The v2.0 patch additionally made the interpolation family a full microscopic QMS (Theorem A24.III-2), corrected the Schur uniqueness to "one scalar per edge \+ global edge-homogeneity," made the §7.3 full-121×121 microscopic Monte Carlo explicit, split the simulator into two protocols, fixed the trace/dual-weight and 𝓛\_s/L\_s expressions, and added the Fagnola–Umanità and quantum-Doob references. *Convergent;* value: A24 bounded to what is proved, with the single honest OPEN registered.

**References**

\[CLPW22\]  V. Chandrasekaran, R. Longo, G. Penington and E. Witten, *An Algebra of Observables for de Sitter Space*, JHEP **02** (2023) 082, arXiv:2206.10780.

\[Wit22\]  E. Witten, *Gravity and the Crossed Product*, JHEP **10** (2022) 008, arXiv:2112.12828.

\[DEHK25a\]  K. De Vuyst, S. Eccles, P. A. Höhn and J. Kirklin, *Gravitational entropy is observer-dependent*, JHEP **07** (2025) 146, arXiv:2405.00114.

\[DEHK25b\]  K. De Vuyst, S. Eccles, P. A. Höhn and J. Kirklin, *Crossed products and quantum reference frames*, JHEP **07** (2025) 063, arXiv:2412.15502.

\[Tak73\]  M. Takesaki, *Duality for crossed products and the structure of von Neumann algebras of type III*, Acta Math. **131**, 249 (1973).

\[Tak03\]  M. Takesaki, *Theory of Operator Algebras II*, Springer (2003) \[continuous crossed products, continuous decomposition\].

\[vD78\]  A. van Daele, *Continuous Crossed Products and Type III von Neumann Algebras*, LMS Lecture Note Series **31**, Cambridge University Press (1978).

\[Con73\]  A. Connes, *Une classification des facteurs de type III*, Ann. Sci. ÉNS **6**, 133 (1973).

\[SN\]  T. Skolem (1927); E. Noether — the Skolem–Noether theorem: every automorphism of a finite-dimensional central simple algebra is inner.

\[Dav74\]  E. B. Davies, *Markovian Master Equations*, Commun. Math. Phys. **39**, 91 (1974).

\[Lin76\]  G. Lindblad, *On the Generators of Quantum Dynamical Semigroups*, Commun. Math. Phys. **48**, 119 (1976).

\[GKS76\]  V. Gorini, A. Kossakowski and E. C. G. Sudarshan, *Completely positive dynamical semigroups of N-level systems*, J. Math. Phys. **17**, 821 (1976).

\[FU07\]  F. Fagnola and V. Umanità, *Generators of Detailed Balance Quantum Markov Semigroups*, Infin. Dimens. Anal. Quantum Probab. Relat. Top. **10**, 335–363 (2007).

\[FU10\]  F. Fagnola and V. Umanità, *Generators of KMS Symmetric Markov Semigroups on B(h): Symmetry and Quantum Detailed Balance*, Commun. Math. Phys. **298**, 523–547 (2010).

\[CGLP18\]  F. Carollo, J. P. Garrahan, I. Lesanovsky and C. Pérez-Espigares, *Making Rare Events Typical in Markovian Open Quantum Systems*, Phys. Rev. A **98**, 010103(R) (2018) \[quantum Doob / tilted-generator transform\].

\[Nor97\]  J. R. Norris, *Markov Chains*, Cambridge University Press (1997).

\[Bog76\]  E. B. Bogomolny, *Stability of Classical Solutions*, Sov. J. Nucl. Phys. **24**, 449 (1976).

\[FW98\]  M. I. Freidlin and A. D. Wentzell, *Random Perturbations of Dynamical Systems*, 2nd ed., Springer (1998).

\[GH77\]  G. W. Gibbons and S. W. Hawking, *Cosmological Event Horizons, Thermodynamics, and Particle Creation*, Phys. Rev. D **15**, 2738 (1977).

\[PP86\]  M. Pimsner and S. Popa, *Entropy and Index for Subfactors*, Ann. Sci. ÉNS **19**, 57 (1986).

\[Vik05\]  A. Vikman, *Can Dark Energy Evolve to the Phantom?*, Phys. Rev. D **71**, 023515 (2005).

\[DESI25\]  DESI Collaboration, *DESI DR2: Baryon Acoustic Oscillations and Cosmological Constraints* (2025).

\[ZS-A19\]  K. Kang, *ZS-A19: Z-Spin Boundary Tension as Geometric Dust* (κ² \= **A**/**Q**), Z-Spin Cosmology (2026).

\[ZS-A22\]  K. Kang, *ZS-A22 v2.2: The Phantom-Divide Gate* (B1/B3/C5 frontier), Z-Spin Cosmology (2026).

\[ZS-A23\]  K. Kang, *ZS-A23 v3.3: Dimension-Weighted Mediator Semigroups and Observer-Algebra Weights in a Finite-Register de Sitter Model*, Z-Spin Cosmology (2026).

\[ZS-F0\]  K. Kang, *ZS-F0: BV–BFV Cobordism and Wilson Loops*, Z-Spin Cosmology (2026).

\[ZS-F1\]  K. Kang, *ZS-F1: The Z-Anchor as a Bogomolnyi Vortex*, Z-Spin Cosmology (2026).

\[ZS-F2\]  K. Kang, *ZS-F2: Geometric Impedance A \= 35/437* (§11.4 face counting), Z-Spin Cosmology (2026).

\[ZS-F19\]  K. Kang, *ZS-F19: Frame-Invariant Tilt Theorem* (KMS-modular rapidity; Type II crossed-product bridge; lattice UV regulator), Z-Spin Cosmology (2026).

\[ZS-F23\]  K. Kang, *ZS-F23: Geometric Fixing of the Type II Trace Normalization — the ℤ₂-Seam ln 2*, Z-Spin Cosmology (2026).

\[ZS-M1\]  K. Kang, \*ZS-M1: i-Tetration and the Fixed Point z\\\*\*, Z-Spin Cosmology (2026).

\[ZS-M6\]  K. Kang, *ZS-M6: Register-Total Normalization (κ² \= A/Q) and Dimensional Coupling Norm*, Z-Spin Cosmology (2026).

\[ZS-M17\]  K. Kang, *ZS-M17: Continuum Limit and the Reflection-Positivity (OS-3) Test*, Z-Spin Cosmology (2026).

\[ZS-Q7\]  K. Kang, *ZS-Q7: Y-Sector Gravitational Entropy Dominance* (the relaxation cubic), Z-Spin Cosmology (2026).

\[ZS-QH\]  K. Kang, *ZS-QH: A 3-2-6 Open-System Hardware Architecture*, Z-Spin Cosmology (2026).

\[Book\]  K. Kang, *The Book of Z-Spin Cosmology v9.0 (Light OS for AI)*, Z-Spin Cosmology (2026).

**Version History**

*Table 4\. Version history.*

| Version | Date | Change |
| ----- | ----- | ----- |
| v1.0 | June 2026 | Initial draft. Four-gate continuous-clock lift. **Contained a foundational error:** claimed M₁₁ ⋊\_{σ^ω} ℝ is Type II. Superseded. |
| v1.1 | June 2026 | **Foundational revision.** Retracted v1.0's finite-route Type-II error (inner modular flow ⇒ Type I, CLOSED-NEGATIVE); rebuilt Part II on the genuine III₁ → II∞ core with a II₁ corner and register embedding; absorbed the self-contained Part I (general theorem, H-theorem, full 121×121 spectrum, perturbation); redefined the Gate-3 target in continuous trace dimension. Audit zs\_a24\_v1\_1\_audit.py, **18/18 PASS**. (A, Q, dim Z) \= (35/437, 11, 2\) **LOCKED**. |
| v1.2 | June 2026 | **§20 programs (Appendix E).** Derived the Gate-3 partition (6, 32, 83)/121 from ZS-F2 §11.4; closed the per-edge Z-Anchor-vortex route as **CLOSED-NEGATIVE** (minimal BPS action 2π ≠ 1/κ²); grounded the observer weights as operator dimensions d\_i². Audit **24/24 PASS**. **LOCKED**. |
| v1.3 | June 2026 | **Residual closure (Appendix E).** Proved ω \= (9, 4, 36)/49 (ZS-A23.MC, two routes); resolved the equal-weight as combinatorial holography (ZS-F0 §8.5); **retracted** per-edge \= 1/κ² (no corpus instanton) for the seam-flip π/A (ZS-M3 §6); retracted the e^{−2/κ²}↔Λ numerology. Audit **30/30 PASS**. **LOCKED**. |
| v1.4 | June 2026 | **Internal closure \+ residual audit (Appendix E).** Recorded a Takesaki argument for the corner trace (**later corrected in v1.5** — it fixes the *state*, not the trace) and the same-seam lemma fixing the per-edge scale at π/A; located the remaining items as upstream/registered. Audit **35/35 PASS**. **LOCKED**. |
| v1.5 | June 2026 | **Trace/state correction \+ finite-register bridge (Appendix E).** Corrected the v1.0-era conflation: corner *trace* \= matrix trace \= (3, 2, 6)/11 \= π, while ω \= (9, 4, 36)/49 \= the *state* τ(h·) (restoring ZS-A23 consistency). New **PART III**: no-go, observer-balanced **L**\_ω, and the interpolation joining **L**\_π to **L**\_ω. Upgraded §6 to the exact general spectrum A24.I-4G and §7 to two PROVEN perturbation theorems. Audit zs\_a24\_v1\_5\_audit.py, **42/42 PASS**. **LOCKED**. |
| v1.6 | June 2026 | **Scope correction \+ full quantum DB (Appendix E).** Bounded the claim to **finite-register** unification (the continuous-core dynamical lift registered **OPEN**, F-A24.9); proved the full quantum detailed-balance theorem (A24.III-1b: **L**\_ω KMS- *and* GNS-symmetric on M₁₁, modular-covariant); separated the e\_α/q\_a symbols; fixed the embedding-arrow, §11, §19, falsification-numbering, and amplitude/rate items; positioned the standard machinery honestly. Audit zs\_a24\_v1\_6\_audit.py, **48/48 PASS**. **LOCKED**. |
| v2.0 | June 2026 | **Consolidated public release (Appendix E).** Editorial/mathematical patch on v1.6, no new physics: made the interpolation a **full microscopic QMS family** **L**\_{(s)} (Theorem A24.III-2, jumps √γ(h\_j/h\_i)^{s/2}, ρ\_s, endpoints **L**\_π, **L**\_ω); corrected the GKLS uniqueness to **one scalar per edge (Schur) \+ global edge-homogeneity**; made the **full 121×121 microscopic Monte Carlo** explicit (§7.3); split the simulator into two protocols (π via **L**\_π, ω via **L**\_ω); fixed the trace/dual-weight and **𝓛**\_s/**L**\_s expressions; added the Fagnola–Umanità and quantum-Doob references; **moved the deep-exploration records to Appendix E** and compressed the body. Audit zs\_a24\_v2\_0\_audit.py, **53/53 PASS**. (A, Q, dim Z) \= (35/437, 11, 2\) **LOCKED**. (Consolidated from internal Z-Spin Collaboration notes and external review v1.0 → v2.0.) |
| v2.1 | June 2026 | **Editorial/mathematical patch of v2.0 (public release).** No new physics; closes the final review items. (1) **Γ₀ time-normalisation convention** stated in §2 (Γ₀ ≡ 1 is a unit, not a fitted parameter — closing the last zero-free-parameter gap). (2) **Subtitle added** making explicit that the unification is finite-register and the continuous-core dynamical lift is left open (F-A24.9). (3) **§10 embedding arrow corrected** to M₁₁ ↪ M\_obs ⊂ **C**\_ω. (4) **§U6 intertwining** corrected to E ∘ **𝓛**\_s \= **L**\_s ∘ E. (5) **§11 status** corrected — the conditional expectation E exists, but the dynamical intertwining is a requirement on the unconstructed lift and remains **OPEN**. (6) **§7.3 figure** stated as max\_i |Δp\_i| \< 0.02 (the audit PASS threshold; fixed-seed run ≈ 0.011) and described as a robustness illustration, not a certified tolerance. (7) **§5 status downgraded** to **DERIVED** (the per-edge Schur step is PROVEN; full uniqueness rests on the action-level global-edge-homogeneity input). (8) **Audit strengthened (V7.6):** full GNS- and KMS-symmetry of **L**\_s at the intermediate s \= ¼ and all 36 jump-pair modular pairings, matching the §U4 text. (9) Residual v1.x/two-Part self-references replaced by v2.0/three-Part framing (Title/§1/§17/§20/Acknowledgements); the historical attributions in §12/§19 and the version trail are retained. Audit zs\_a24\_v2\_1\_audit.py, **54/54 PASS**. (A, Q, dim Z) \= (35/437, 11, 2\) **LOCKED**. |

*— End of ZS-A24 v2.1 —*