**ZS-A19**

**Z-Spin Boundary Tension as Geometric Dust: A Rank-Absorption No-Go and a Boundary-Charge (ZHCS) Program — Stückelberg→BF Dualization, Actual-W\_bc Connectivity, and Brown–Kuchař Canonical Branching, with C1 and C2 Reduced to Three Named, Falsifiable Corpus Conditions (an Honest Conditional Reduction, Not a Closure)**

**Kenny Kang**

Z-Spin Cosmology Collaboration

June 2026 — Astrophysics theme \[ZS-A\] · Paper 19 · ZS-A19 v3.1

GitHub: https://github.com/KennyKang-git/zspin

**Locked inputs:** A \= 35/437 ≈ 0.080092, Q \= 11, (Z, X, Y) \= (2, 3, 6).  Zero new fitted parameters.

**Verification: 22/22 independent recomputations PASS** (polyhedral, graph-spectral, cross-transfer structure, symplectic branching, and the C1/C2 substrate computations; Appendices C–H). These supply the structural backbone of the ZHCS program. **v3.1 status correction (Appendix I):** a second review showed v3.0 over-stated three steps — the C1-B all-entries-nonzero check used an idealized intertwiner (F\_TI carries the trivial representation with multiplicity two, so the actual cross-overlap is corpus-dependent), the C1-C identity ‖Ω∂Σ^(0→1) − q\_Z d\_Γ‖ \= 0 was tautological (Ω was defined, not independently derived), and the relative-mode removal is constraint-exclusion rather than proven gauge-exactness. Checks 17–18 therefore verify the idealized substrate, not the corpus closure. v3.1 reduces C1 and C2 to three named, falsifiable corpus conditions (a)–(c): **C1 is DERIVED-CONDITIONAL on (a) ∧ (b)** and **C2 is DERIVED-CONDITIONAL on (c) \+ a single source**. A19.NG1, A19.NG2 PROVEN and intact; ZS-A18 NO-GO frozen. Zero new fitted parameters.

## **§0. Abstract**

ZS-A18 (v1.5, frozen) proved that a smooth massless Z-Spin Goldstone gradient cannot be the recombination cold dark matter (CDM) that sustains the third CMB acoustic peak: a smooth massless field has w ∈ {−1/3, \+1}, never w \= 0\. This paper does not contest that NO-GO; it proposes a different carrier. We abandon the premise that dark matter is a collection of objects (Planck-mass vortex cores, vortons, primordial-black-hole relics) — the premise responsible for the over-closure, \~10⁹ GeV formation-scale, and current-carrier obstructions, all of which are artifacts of the particle ontology — and instead implement ZS-F2’s definition of CDM as a geometric boundary tension through a conserved pullback / Brown–Kuchař dust (w \= 0, c\_s² \= 0, ρ ∝ a⁻³) that leaves the Goldstone exactly massless (§3–§4).  
The fraction Ω\_cdm \= F(TI)/Q² \= 32/121 is read as an equivariant projection-class rank: the truncated-icosahedron face module embeds A₅-equivariantly in the Q² \= 121 channel algebra as a rank-32 projector with canonical normalized trace 32/121 (Theorem A19.2), the “32 charge” being neither a spatial-topological charge (Lemma A19.3a NO-GO) nor a metric tension (Lemma A19.3b NO-GO). Two proven obstructions discipline the program: **Theorem A19.NG1** (the unique faithful unital embedding A\_ZS \= M₃ ⊕ ℂ ⊕ M₅ → M₁₁ forces center weights (3,3,5)/11 ≠ the ZS-F23 (3,2,6)/11, so BT-C and ZS-F23 Condition C are distinct traces) and **Theorem A19.NG2** (for a scalar clock the seam projector enters the bulk action only through Tr P\_c \= 32, removed by λ\_c → λ\_c/32, so no bulk rank-lock fixes the cold fraction).  
A19.NG2 forces the rank out of the bulk and onto a conserved boundary canonical charge: the **ZHCS** program puts one harmonic parent charge p on a 38-node seam graph of the 32 cold (truncated-icosahedron) faces and the 6 baryon (cube) faces, so that Q\_c : Q\_b \= 32 : 6 is the rescaling-invariant ratio of two projections of one parent charge (never written into the action). v2.0 promoted this to DERIVED-CONDITIONAL on a single operator identification; v2.1–v2.3 corrected the substrate and consolidated the gaps. v2.4 makes the reduction honest and the conditions checkable. A corrected recomputation shows (i) the truncated-octahedron incidence kernel is **two-dimensional**, so v2.0’s “unique tO null mode” cross-support argument is **retracted**; (ii) the six tO squares are **mutually non-adjacent**; and (iii) the BV-BFV mQME gives Ω∂Σ ψ \= −ℏ² ΔV ψ, not Ω∂Σ ψ \= 0\. The cross-block claim is then re-grounded **structurally**: the corpus fixes the X–Z–Y mediation as the rank-1 β₀ channel with κ² \= A/Q \= 35/4807 ≠ 0 (PROVEN), so the uniform-sector cross-transfer vanishes only if a whole block is decoupled from the unique β₀ mode (gate F-A19.7) — not merely as a generic non-cancellation. The diffuse BFV identifications are imported as a **conditional reduction**, not a closure: external theorems prove C1 ⇒ (Ω∂Σ \= d\_Γ) but not S\_ZS ⇒ C1. We therefore split the named conditions into checkable sub-conditions — C1a (physical cube adjacency), C1b (actual corpus W\_bc ≠ 0), C1c (cellular-abelian-BF boundary identification), and, for the cosmological gates, a restored canonical-branching action S\_branch with symplectic-charge conservation Θ\_c \+ Θ\_b \= Θ\_\*. From the branching, the equal normalization ε\_c \= ε\_b is **forced** once the parent boundary Hamiltonian is linear in the single parent charge with one coefficient (H \= ε\_\* p) — the explicit equal-Hamiltonian-normalization condition. The co-moving identification is narrowed: cold and baryon share the parent clock and curvature perturbation only at the branching hypersurface (adiabatic initial condition), after which they evolve by their own interaction Hamiltonians (baryon–photon acoustic oscillation, cold free-streaming) — removing the conflict with baryon acoustic physics. Weinberg’s theorem proves an adiabatic mode exists; ZHCS-4 additionally requires the initial state to occupy that sector (no independent entropy), which the branching makes natural (one parent charge, no independent integration constant) but does not by itself impose. Net statuses: ZHCS-1 **DERIVED-CONDITIONAL on C1a ∧ C1b**; ZHCS-2 **DERIVED-CONDITIONAL on C1c** (core PROVEN-CONDITIONAL via Eckmann/Lim); ZHCS-3 **DERIVED-CONDITIONAL on C2** (equal-Hamiltonian-normalization, reduced to H \= ε\_\* p); ZHCS-4 **PROVEN-CONDITIONAL on C2 \+ no-independent-entropy / adiabatic selection**; the physical 32:6 ratio **DERIVED-CONDITIONAL on C1 ∧ C2**; and the third acoustic peak **COMPUTED-CONDITIONAL on C1 ∧ C2 ∧ adiabatic selection ∧ standard Boltzmann transfer**. No gate reaches unconditional DERIVED; C1c and C2 remain physical identifications. The dust EOS is IMPORTED-PROVEN, the integers 32, 6, η\_B pre-exist, ZS-A18 is frozen, and no new parameter is fitted.  
**v3.1 reduction (honest correction of v3.0).** v3.0 claimed C1 DERIVED and C2 DERIVED-CONDITIONAL on a single source. A second review showed three steps were over-stated, and v3.1 corrects them, reducing C1 and C2 to three named, falsifiable corpus conditions (Appendix I). The conditions are narrowed to **C1′** (the β₀ boundary-charge sector of the S10 Stückelberg U(1) is isomorphic to cellular BF on Γ\_m) and **C2′** (one Brown–Kuchař clock-energy momentum canonically branches into cold and baryon at Σ\_\*). The structural backbone is real: (C1-A) the corpus Stückelberg action D\_μΦ \= (∂\_μ − iκ g\_Y B\_μ)Φ, κ² \= A/Q, dualizes to a 2-form–1-form BF coupling q\_Z ∫ B∧F\_Y (verified symbolically), so C1-A is DERIVED; the physical 38-node graph (TI adjacency \+ six isolated squares \+ actual cross-edges) is connected with rank L\_Γ \= 37, eliminating the cube rewiring; the Brown–Kuchař Hamiltonian constraint C \= P\_T \+ H\_ZS \= 0 gives Θ\_c \+ Θ\_b \= Θ\_\* and, for the pure dust Hamiltonian, node-uniform ε\_c \= ε\_b; and the four branching constraints are second-class (constraint matrix det \= 1), reducing to the single pair (p, T\_\*). **But three steps are corpus-conditional, not closed.** (a) The actual cross-transfer overlap is corpus-dependent: F\_TI carries the trivial representation with multiplicity two (span{1\_pent, 1\_hex}), so ⟨r\_Y | 1₃₂⟩ depends on which trivial combination the corpus C\_ZY couples β₀ to; the vanishing locus is a single ray that every corpus-natural candidate (uniform → 32, the Lemma-4.5 mode (−2,1) → −4, pure pentagon/hexagon) avoids, but the exact value is corpus data — **condition (a): C\_ZY lies in the corpus-natural trivial family**. (b) The boundary BFV differential equals q\_Z d\_Γ from the BF term, with Maxwell contributing only a separate degree-1 Gauss constraint; that the ZS-F0 boundary term S\_∂M does not mix sectors is **condition (b)** — v3.0’s ‖Ω − q\_Z d\_Γ‖ \= 0 was tautological. (c) The single coefficient ε\_c \= ε\_b holds for the pure Brown–Kuchař Hamiltonian; that S\_ZS adds no block-dependent boundary energy is **condition (c)**. The 37 relative modes are removed by failing the constraint d\_Γ p \= 0 (constraint-exclusion), not by proven gauge-exactness. **Net: C1 is DERIVED-CONDITIONAL on (a) ∧ (b); C2 is DERIVED-CONDITIONAL on (c) \+ a single source.** Theorem A19.ZHCS-Closure (PROVEN-CONDITIONAL on C1 ∧ C2) then gives ρ\_c/ρ\_b \= 32/6, w\_c \= c\_s² \= 0, S\_cb \= S\_cγ \= 0, standard passive CDM transfer, and ω\_c \= 0.119112 — all DERIVED-CONDITIONAL on (a) ∧ (b) ∧ (c) \+ single source. This is a conditional reduction with a fully-characterized three-condition residual, **not a closure**; the dust EOS is IMPORTED-PROVEN, the integers pre-exist, ZS-A18 is frozen, and no new parameter is fitted.

## **§0.1 Epistemic Status Legend**

Table 0\. Epistemic status legend used in this paper.

| Status | Definition |
| ----- | ----- |
| **LOCKED** | Core constant fixed upstream; no downstream paper may modify. Here A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6). |
| **PROVEN** | Mathematical theorem from standard mathematics or corpus definitions; machine-verifiable. |
| **PROVEN-CONDITIONAL** | A proof exists under explicitly stated antecedent(s); if the antecedent holds, the consequent is forced. |
| **IMPORTED-PROVEN** | A theorem proven in the external literature; its Z-Spin realization is a separate claim. |
| **DERIVED** | Follows from the Z-Spin action plus PROVEN inputs; zero free parameters beyond A. |
| **DERIVED-CONDITIONAL** | Derived, conditional on one or more named physical identifications not yet established. |
| **DERIVED-CANDIDATE** | An algebraic identity holds, but its physical applicability faces a known structural obstruction. |
| **VERIFIED** | Numerically confirmed after all model-specific premises are implemented. No claim here is at this level. |
| **HYPOTHESIS-strong** | Physically motivated and structurally supported; derivation chain incomplete. |
| **BOOTSTRAP-HYPOTHESIS** | An explicit, self-consistent ansatz proposed for testing; central claim gated by open problems. |
| **OPEN** | A sharply stated, falsifiable question current tools cannot settle; locates the DERIVED/hypothetical boundary. |
| **NO-GO** | A proven impossibility for a specified construction. |
| **RETRACTED** | A prior claim withdrawn with documented reason. |
| **NON-CLAIM** | Explicitly not asserted; documented to prevent overclaim. |

## **§1. Introduction**

The heights of the CMB acoustic peaks — the third relative to the second — measure how strongly gravitational wells on acoustic scales were sustained through the radiation-to-matter transition. In ΛCDM this is performed by a cold, pressureless, non-free-streaming component with w ≈ 0 that clusters at recombination.  
ZS-A18 (v1.5, frozen) proved the Z-Spin massless Goldstone θ of the broken U(1)\_Z cannot perform this role: a smooth massless scalar has w \= \+1 when time-dependent and w \= −1/3 as a static global-monopole gradient, never w \= 0 — the massless dichotomy, strengthened by integrating out the heavy radial mode (w, c\_s² ∈ \[1/3, 1\]). ZS-A18 stands as a NO-GO and is not modified here.  
Three object-based routes each met a wall. (i) Planck-mass vortex cores are cold but over-close by \~10¹⁷–10²⁸ as relics. (ii) Current-carrying vortons require a conserved current, but the ZS-S10 j \= 1/2 core is a holonomy/BPS object, not a Dirac zero mode, so the Jackiw–Rossi/Witten carrier is absent; the Planckian string tension places any vorton far above the \~10⁹–10¹² GeV window, over-closing. (iii) An intermediate \~8.5×10⁸ GeV formation scale would fix a relic abundance, but the corpus derives no such scale and anti-numerology rejects any A,Q expression hitting it.  
The lesson is that the obstruction is the **premise**, not the physics: every route assumed dark matter is a collection of objects. ZS-F2 already defines CDM as a geometric boundary tension with Ω\_cdm \= F(TI)/Q² \= 32/121; ZS-A18’s NO-GO arose because ZS-A1/A18 then identified that tension with the Goldstone gradient. This paper takes ZS-F2 literally and supplies the missing dynamics: a conserved geometric dust.

## **§2. Locked Inputs from the Corpus**

Geometric constants (LOCKED): **A** \= 35/437, **Q** \= 11, register (Z, X, Y) \= (2, 3, 6\) with Q \= 2 \+ 3 \+ 6\. No quantity here introduces any parameter beyond these. Dark-matter fraction (ZS-F2): Ω\_cdm \= F(TI)/Q² \= 32/121, with F(TI) \= 32 and Q² \= 121, CDM characterized as a geometric boundary tension; ZS-F2 supplies the fraction but not T\_μν \= ρ u\_μ u\_ν. Logical algebra (ZS-Q11/F23): the single-cell algebra is the finite Type I von Neumann algebra **A\_ZS ≅ M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ)** (dim 9+1+25 \= 35 \= numerator of A), with center ℂ³ carrying the three sector projections and equilibrium weights (3, 2, 6)/11. Emergence dictionary (ZS-F23, OPEN): Condition C requires the de Sitter maximum-entropy state to carry weights (3, 2, 6)/11; the present bridge is its channel-space analogue. Truncated icosahedron: V \= 60, E \= 90, F \= 32 (12 pentagons \+ 20 hexagons), I\_h with |I\_h| \= 120 \= Q² − 1, Euler 2\. Standing NO-GO (ZS-A18 v1.5, frozen): the massless Goldstone gradient is not recombination CDM; the present carrier is disjoint from this scope (**NC-A19.2**).

## **§3. The Geometric-Dust Ontology**

We replace “CDM \= collection of objects” with “CDM \= conserved geometric dust from a constraint,” whose density is fixed by a constraint coefficient rather than a relic abundance, so no over-closure calculation applies.

### **Theorem A19.1 (Particle-Free Geometric Dust) — IMPORTED-PROVEN**

Borrowed existence statement: a pressureless dust (w \= 0, c\_s² \= 0, ρ ∝ a⁻³) can arise from a geometric constraint or pullback action with no particle relic. Three established constructions realize it. **(A) Pullback perfect fluid:** with three comoving maps X^I, the identically conserved current J^μ, proper density b \= (−J²)^{1/2}, and S \= ∫√(−g) F(b), the convention-consistent pressure is p \= F − b F\_b; choosing F(b) \= −μ b gives ρ \= μ b, p \= 0, T\_μν \= ρ u\_μ u\_ν, and b ∝ a⁻³. **(B) Mimetic constraint:** g^{μν}∂\_μ T ∂\_ν T \= −1 via a multiplier turns the conformal mode into pressureless dust. **(C) Projectable integration constant:** a space-independent lapse leaves an integration-constant dust component. The Z-Spin realization — that the corpus action produces such a dust with the correct normalization — is HYPOTHESIS-strong/OPEN; μ is an independent EOS input, not yet fixed by ZS-F2. The over-closure, formation-scale, and carrier obstructions are removed because the density is set by a constraint coefficient, not a relic abundance, and the Goldstone stays massless (ZS-S3, ZS-A1 untouched).

## **§4. The X-Pullback Realization**

The pullback fluid is the most Z-Spin-native and safest of the three: it adds matter fields (the maps X^I) rather than gravitational scalar modes, preserving diffeomorphism covariance and the ZS-M6 sector-independence L\_XY \= 0 (the mimetic and projectable routes modify the gravitational sector and risk caustic/gradient instabilities). **Identification (HYPOTHESIS-strong):** the X-sector’s three spatial slots are identified with the three comoving coordinates X^I, so the ZS-F2 Y→X transmission appears as a conserved X-space current (action-level derivation \= gate BTD-1). **Role of the Z-anchor (NC-A19.4):** the Z-anchor does not carry the CDM mass; it is the singular locus det(∂\_μ X^I) \= 0 — a defect/locator of the dust flow — realizing “topology sets location; accretion sets mass” (ZS-F1 NC-2).

### **Version-Conflict Note (O-A19.6): the ε-Halo overlap**

If the pullback dust carries the full Ω\_cdm \= 32/121 and clusters from recombination, it also clusters in present galaxies, while ZS-A1 attributes the entire rotation excess to the Goldstone ε-Halo — maintaining both would double-count gravity. Three mutually exclusive resolutions are admissible and one must be selected: (A) the dust replaces the ε-Halo DM interpretation; (B) a transformation theorem identifies the linear cosmological dust and the nonlinear ε-Halo dressing as the same energy in different regimes; or (C) the ε-Halo is the metric response of the dust. Registered OPEN gate O-A19.6.

## **§5. The Equivariant Boundary-Rank–Trace Theorem**

Theorem A19.1 fixes the EOS but leaves μ free; we address Ω\_cdm \= 32/121. **(A1) Register:** A₅ ≅ I acts on the 12 icosahedron vertices; deleting the constant gives V₁₁ \= ℂ¹² ⊖ 1 with character (11, −1, −1, 1, 1\) and V₁₁ \= 3 ⊕ 3′ ⊕ 5; H\_Q carries V₁₁. **(A3) Channel algebra:** K\_Q \= End(V₁₁) ≅ M₁₁(ℂ), dim Q² \= 121, traceless part 120 \= |I\_h|; as an A₅-module End(V₁₁) \= 3·1 ⊕ 6·3 ⊕ 6·3′ ⊕ 8·4 ⊕ 10·5. **(A2) Boundary module:** F\_TI \= ℂ\[A₅/C₅\] ⊕ ℂ\[A₅/C₃\], character (32, 0, 2, 2, 2), F\_TI \= 2(1 ⊕ 3 ⊕ 3′ ⊕ 4 ⊕ 5), dim 32\. Every irreducible occurs in End(V₁₁) with multiplicity ≥ its multiplicity in F\_TI, so an A₅-equivariant embedding F\_TI → End(V₁₁) exists, with projector P\_BT of rank 32; the embedding is **not unique** (∃ P\_BT proven, ∃\! not), so P\_BT is a candidate (canonical selection \= gate O-A19.2).

### **Theorem A19.2 (Equivariant Rank–Trace) — algebraic identity DERIVED-CONDITIONAL on A1–A3; cosmological use DERIVED-CANDIDATE**

With the canonical normalized trace τ\_Q \= (1/Q²) Tr, **τ\_Q(P\_BT) \= rank P\_BT / Q² \= 32/121**. No equipartition enters this algebraic identity (it is the definition of the canonical trace). The physical statement Ω\_cdm \= 32/121 (not merely τ\_Q \= 32/121) additionally requires the tracial state ρ★ \= I/121 and energy degeneracy on boundary modes — Condition BT-C (§7). This channel trace is related to but, by Theorem A19.NG1, not identical to the ZS-F23 trace on A\_ZS.

Table 1\. Representation data (verified, Appendix A).

| Object | A₅-character | Decomposition | dim |
| ----- | ----- | ----- | ----- |
| V₁₁ \= ℂ¹² ⊖ 1 | (11, −1, −1, 1, 1\) | 3 ⊕ 3′ ⊕ 5 | 11 |
| End(V₁₁) \= M₁₁ | (121, 1, 1, 1, 1\) | 3·1⊕6·3⊕6·3′⊕8·4⊕10·5 | 121 |
| F\_TI (face module) | (32, 0, 2, 2, 2\) | 2(1 ⊕ 3 ⊕ 3′ ⊕ 4 ⊕ 5\) | 32 |
| P\_BT (projector) | — | image of F\_TI in End(V₁₁) | 32 |

## **§6. What the 32-Charge Is and Is Not**

**Lemma A19.3a (Spatial-Topological NO-GO) — PROVEN.** ∂(TI) ≅ S² and H²(S², ℤ) ≅ ℤ has a single generator; subdividing a face raises F above 32 without changing topology. So F \= 32 is not a spatial topological invariant.  
**Lemma A19.3b (Metric-Tension NO-GO) — PROVEN.** The 32 faces are non-congruent (12 pentagons, area ≈ 1.7205; 20 hexagons, area ≈ 2.5981), so per-area weighting gives the hexagon fraction ≈ 0.716 ≠ 20/32. The boundary charge cannot be a literal metric tension; it is combinatorial and quantized.  
**Conclusion.** 32 is an equivariant projection-class rank — a K₀-type quantity invariant under basis and unitary deformation — equal to dim F\_TI \= dim C₂(TI; ℂ) \= rank P\_BT, with canonical trace 32/121. “Topological face charge” is replaced by “equivariant boundary-rank / projection-class charge.”

## **§7. Condition BT-C and Its Relation to ZS-F23 Condition C**

The physical Ω\_cdm \= 32/121 requires the cosmological state to realize the canonical channel trace. **Condition BT-C (Boundary Tracial-State Matching) — OPEN:** the Z-Spin gravitational/dust equilibrium state, restricted to the channel algebra, equals τ\_Q (equivalently, the boundary transfer channel is primitive and unital and the energy operator is degenerate on boundary modes).

### **Theorem A19.NG1 (Trace-Incompatibility of A\_ZS in M₁₁) — PROVEN NO-GO**

A faithful unital ∗-representation of A\_ZS \= M₃ ⊕ ℂ ⊕ M₅ on ℂ¹¹ requires 3m₃ \+ m₁ \+ 5m₅ \= 11 with all m\_i ≥ 1; the unique solution (m₃, m₁, m₅) \= (1, 3, 1\) gives center ranks (3, 3, 5\) and M₁₁ trace weights **(3, 3, 5)/11 ≠ (3, 2, 6)/11** (the ZS-F23 weights). Hence no single M₁₁ normalized matrix trace can induce both. **Retraction:** the v1.0 claim that one theorem closes both the gravitational-entropy normalization and the dark-matter abundance is RETRACTED. **Repair paths (registered, none derived):** (A) keep the two traces distinct; (B) matrix amplification to M₅₅ with multiplicities (5, 10, 6\) realizing 5·(3, 2, 6); (C) a non-tracial weighted density matrix on M₁₁ — at the cost of the canonical-trace logic. The i-tetration |f′(z★)| \= 0.892 \< 1 shortcut is closed by ZS-F23 §8 (the fixed point is orthogonal to the modular-trace content).

## **§8. The Boundary-Rank-Locked Z-Clock Dust Mechanism (BRL-ZCD)**

The §5–§7 route fixes the EOS only up to μ, reaches 32/121 only via BT-C, and meets the A₅/(2,3,6) tension and Theorem A19.NG1. This more corpus-native action-level route, **S\_BRL \= S\_ZS \+ S\_clock \+ S\_match**, targets μ and the A₅ tension and writes an h-free absolute density. Overall status: **BOOTSTRAP-HYPOTHESIS**.

### **§8.1 The XQ−1 seam projector (replacing the A₅ route)**

ZS-F2 gives a second route to 32 without V₁₁: the Z₂ gauge projection XQ − 1 \= 3·11 − 1 \= 32 \= F(TI). With the X-democratic |s\_X⟩ \= (1,1,1)/√3 and the Z-odd P\_Z⁻ \= ½(I\_Z − J\_Z), P\_c \= I\_XQ − P\_X⁽⁰⁾ ⊗ P\_Z⁻ has rank XQ − 1 \= 32\. Built from X-democratic and Z-odd directions, it sidesteps the three v1.1 obstructions, but by Theorem A19.NG2 its rank is absorbed in the bulk scalar action: gate BRL-2 is **OPEN**, not DERIVED-CONDITIONAL.

### **§8.2 Theorem A19.3 (Constrained Z-clock dust): EOS IMPORTED-PROVEN, rank NO-GO, realization OPEN**

Promoting the Z-sector time-point to a clock T\_Z(x) with a non-propagating multiplier λ\_c projected by P\_c, S\_clock \= −½ ∫√(−g) Tr\_XQ\[λ\_c P\_c (g^{μν}∂\_μ T\_Z ∂\_ν T\_Z \+ 1)\] gives, on the constraint surface, T\_μν \= ρ\_c u\_μ u\_ν, p\_c \= 0, w\_c \= 0, c\_s² \= 0, ρ\_c ∝ a⁻³ (IMPORTED-PROVEN clock dust). T\_Z being the existing Z-sector clock (not a new scalar) is HYPOTHESIS-strong (gate BRL-1); T\_Z is kept distinct from the Goldstone θ and the density multiplier λ\_c.

### **§8.2a Theorem A19.NG2 (Scalar-clock rank-absorption) — PROVEN NO-GO**

Because T\_Z and λ\_c are scalars, the channel trace factorizes: Tr\_XQ\[λ\_c P\_c 𝒞(T\_Z)\] \= λ\_c 𝒞(T\_Z)·Tr P\_c \= 32 λ\_c 𝒞(T\_Z), and λ̃\_c \= 32 λ\_c returns ordinary single-clock mimetic dust. **For a scalar clock and scalar multiplier, every action Tr\[P λ\_c 𝒞(T\_Z)\] depends on the finite-rank projector P only through rank P, removable by λ\_c → λ\_c/rank P.** No projector rank can fix the dust density in this construction. Two OPEN repairs: (R1) operator-valued dynamics; (R2) a quantized per-face boundary Noether charge (gate G1). A19.NG2 stands as a standing no-go any rank-locking claim must clear.

### **§8.3 Baryon-anchored boundary matching (the abundance, with no μ)**

With cold rank r\_c \= XQ − 1 \= 32 and baryon rank r\_b \= XZ \= 6, S\_match \= ∫\_Σconf √h χ\[(1/32) n·n·T(c) − (1/6) n·n·T(b)\] enforces ρ\_c/32 \= ρ\_b/6, i.e. ρ\_c/ρ\_b \= 32/6 \= 16/3, time-independent. **Three caveats (HYPOTHESIS-strong):** (1) the same form imposes r\_c/r\_b for any ranks — it encodes 32:6 rather than deriving it; (2) stress-energy matching is not the right invariant across Σ\_conf — conserved-current matching with a per-charge energy equality is needed (gate G4); (3) no rank-6 baryon projector P\_b is constructed in this route (gate G3). BRL-3 (that the ZS-F0 boundary variation produces per-mode energy equality) is not proven.

### **§8.4 Theorem A19.4 (h-free absolute CDM density) — CONDITIONAL NUMERICAL CONSEQUENCE**

ZS-U3/F5 derive η\_B \= (Y/Q)³⁵ \= (6/11)³⁵ \= 6.117×10⁻¹⁰ (exponent 35 \= numerator of A), matching Planck (6.12 ± 0.04)×10⁻¹⁰. The standard BBN relation η₁₀ \= 273.9 ω\_b gives ω\_b \= 0.022334, and the boundary ratio gives **ω\_c \= (32/6) ω\_b \= 0.119112**. **Tier 1 (parameter-free ratio):** ω\_c/ω\_b \= 16/3 \= 5.333 vs Planck 5.364 ± 0.065 (−0.48σ). **Tier 2 (absolute, h-free):** ω\_c \= 0.119112 vs Planck 0.1200 ± 0.001 (−0.89σ), conditional on U3 η\_B, BRL-3, and the external BBN coefficient. This replaces ZS-F2’s circular ω\_c \= (32/121)h². **AN-A19.2 (EXECUTED, PASS):** 32, 6, η\_B pre-exist; η\_B and ω\_b are not independent (ZS-F5 Independence Warning), not counted twice; μ never used.

### **§8.5 Perturbations and adiabaticity**

As exact pressureless dust, linear perturbations obey the standard CDM Boltzmann system (Ma–Bertschinger). The implication δ\_c \= δ\_b ⇒ S\_cγ \= 0 is PROVEN linear algebra, but its status as a closed gate is OPEN: the density contrast is gauge-dependent (use the gauge-invariant S\_cb \= 0); p\_b ≈ 0 fails right after confinement; and a single-clock adiabatic mode does not by itself remove an independent dust-density integration constant of λ\_c. Full CLASS/CAMB confirmation \= gate BRL-5.

Table 2\. v1.1 bottlenecks and their BRL-ZCD handling.

| v1.1 bottleneck | BRL-ZCD handling |
| ----- | ----- |
| Three X-pullback fields with free μ | single constrained Z-clock T\_Z; density is λ\_c (no μ) |
| A₅ rank-32 projector (O-A19.5 tension) | XQ−1 seam projector inside the locked (2,3,6) decomposition |
| Theorem A19.NG1 trace incompatibility | off the abundance path, but the rank itself is absorbed in the bulk action (A19.NG2) |
| Condition BT-C (maximally mixed state) | relocated, not removed: the per-mode energy equality is a BT-C-type condition |
| 32/121 as today’s fraction (radiation equipartition) | 32:6 ratio \+ h-free η\_B → ω\_b → ω\_c absolute normalization |
| Goldstone mass / 10⁹ GeV / Planck relic | none used; dust is multiplier-sourced, m\_θ \= 0 preserved |

Table 3\. BRL-ZCD gate set (v1.4 status).

| Gate | Requirement | Status |
| ----- | ----- | ----- |
| BRL-1 | T\_Z is an existing Z-sector clock, not a new propagating scalar. | HYP-strong/OPEN |
| BRL-2 | P\_c is the unique gauge-null mode AND its rank is physical (absorbed, A19.NG2). | OPEN |
| BRL-3 | The ZS-F0 BV-BFV boundary variation enforces ρ\_c/32 \= ρ\_b/6. | OPEN |
| BRL-4 | The local lock gives gauge-invariant S\_cb \= 0, no residual isocurvature. | OPEN |
| BRL-5 | Direct CLASS/CAMB passes TT, TE, EE, lensing, P(k). | OPEN |
| BRL-6 | Cosmological dust and galactic ε-Halo do not double-count. | OPEN |

## **§9. Gate Testing, Status, and Registered Obstructions**

### **§9.1 BRL-5 (acoustic peaks): COMPUTED / OBSERVATIONALLY CONSISTENT**

A CAMB run holding h, n\_s, A\_s, τ and neutrinos at Planck 2018 and varying only (ω\_b, ω\_c):

Table 4\. CAMB third-peak consistency (TT only, standard CDM transfer assumed).

| Model | ω\_c | Third peak (ℓ, 𝒟 / μK²) | vs Planck |
| ----- | ----- | ----- | ----- |
| Planck 2018 | 0.12000 | (813, 2541.3) | — |
| BRL-ZCD value | 0.119112 | (814, 2543.9) | \+0.10% (−0.74σ) |
| control (low) | 0.100 | (834, 2603.6) | \+2.45% |
| control (high) | 0.140 | (796, 2482.2) | −2.32% |

Status: **COMPUTED / OBSERVATIONALLY CONSISTENT**, not VERIFIED — it assumes standard CDM transfer (the thing to be derived), is a peak-shape comparison not a likelihood, and computes only the TT third peak. BRL-5 remains OPEN as a derivation gate.

### **§9.2–§9.5 Seam mode, adiabaticity, equipartition, clock**

**BRL-2 (uniqueness, gate OPEN):** the S₃ Reynolds projector on ℂ³ has rank 1 \= |s\_X⟩⟨s\_X|; P\_Z⁻ has rank 1; SO(3) shares no invariant direction — so the gauge-null mode is unique — but A19.NG2 absorbs its rank, and X⊗Q is a tensor product not supplied by the direct-sum register (gate G2). **BRL-4 (adiabaticity):** δ\_c \= δ\_b ⇒ S\_cγ \= 0 is correct but its premises are gauge-dependent and not established. **Equipartition (Theorem A19.5, IMPORTED-PROVEN precedent, application OPEN):** the max-entropy state is maximally mixed (Jaynes), but the fixed-energy state is Gibbs e^{−βH}/Z, so ρ\_c:ρ\_b \= 32:6 holds only under mode-energy degeneracy H\_c ≃ H\_b — itself BT-C — plus a freeze-out preserving 32:6 and the baryon thermal history (three sub-gates). **BRL-1 (clock, HYPOTHESIS-strong/OPEN):** a worldline proper time is a global scalar clock only under hypersurface-orthogonality, a smooth global foliation, coarse-graining of a sparse anchor distribution, and existence at recombination. **Theorem A19.6 (PROVEN, NARROWED):** ν \= (A/π)ln(τ/t\_P) has g^{μν}∂\_μν∂\_νν \= −(A/π)²/τ² ≠ −1 (ruling out ν as the clock), but τ(ν) \= t\_P e^{πν/A} recovers a unit-timelike proper time — the NO-GO is ν-specific.

### **§9.6 Honest residual: distinct gates, not one node**

Table 5\. Honest gate inventory (G1–G8).

| Gate | Open problem | Status |
| ----- | ----- | ----- |
| G1 | Relocate rank 32 out of the bulk (absorbed, A19.NG2) into a boundary Noether charge or operator-valued dynamics. | OPEN |
| G2 | Derive the tensor channel K\_c ≅ H\_X ⊗ H\_Q from the direct-sum register. | OPEN |
| G3 | Construct a rank-6 baryon projector P\_b selecting the baryon channel. | OPEN |
| G4 | Boundary matching on conserved currents plus a per-charge energy equality. | OPEN |
| G5 | Relativistic-equipartition → freeze-out → pressureless dust preserving 32:6. | OPEN |
| G6a | BT-C: the physical state realizes the channel normalized trace. | OPEN |
| G6b | F23 Condition C: equilibrium realizes (3,2,6)/11 — distinct from G6a per NG1. | OPEN |
| G7 | Global irrotational Z-anchor foliation realizing a single dust clock T\_Z. | OPEN |
| G8 | ε-Halo double-counting; full TT/TE/EE/lensing/P(k) likelihood. | OPEN |

**Net.** S\_ZS ⇒ S\_BRL does not close; the residual is 6–8 distinct gates. What is solid: the dust EOS is IMPORTED-PROVEN, 32 and 6 pre-exist, the A18 NO-GO is intact, and A19.NG2 bounds the mechanism. BRL-ZCD is a BOOTSTRAP-HYPOTHESIS.

## **§10. The Boundary-Charge Program (ZHCS): Corrected Substrate and External-Theorem Closure**

A19.NG2 forbids closing the abundance in the bulk; ZHCS relocates the rank to a conserved boundary canonical charge on a connected 38-node graph, with the bulk supplying ordinary Brown–Kuchař dust. **Key idea:** one boundary momentum p on a graph whose nodes are the 32 cold faces and 6 baryon faces; if the boundary variation forces p graph-harmonic (d\_Γ p \= 0\) and the graph is connected, then p \= p★ 1₃₈, so Q\_c \= 32 p★, Q\_b \= 6 p★, and Q\_c/Q\_b \= 32/6 is the rescaling-invariant ratio of two projections of one parent charge — 32:6 never written into the action. A19.NG2 removes the absolute scale (the common α), not this ratio.  
**v2.4 correction notice.** v2.0 reported ZHCS-1 as DERIVED and the 32:6 ratio as DERIVED-CONDITIONAL on a single operator identification; v2.1–v2.3 corrected the substrate and named two conditions C1, C2. A second review showed v2.3 still over-stated the consolidation: (a) the genericity Monte Carlo is weak (a continuous distribution has exact-zero probability 0 by construction, so “0/200,000” shows only that random matrices rarely cancel, not that the actual W\_bc ≠ 0); (b) C1 bundles three distinct sub-conditions; (c) Brown–Kuchař does not by itself give ε\_c \= ε\_b; (d) “co-moving to recombination” conflicts with baryon acoustic physics; (e) Weinberg gives existence of an adiabatic mode, not occupation of it; and (f) the third peak depends on C1 ∧ C2, not C2 alone. v2.4 acts on all six: it re-grounds the cross-block claim structurally (not statistically), restores the canonical-branching action that gives ε\_c \= ε\_b its action-level meaning, splits C1 into C1a/C1b/C1c, narrows C2, and reclassifies the program as an external-theorem **conditional reduction**. No corpus entry other than the v2.0/v2.3 over-statements is retracted; the face-counting budget (ZS-F2 §11.4) is untouched.

### **§10.1 Long list and the conservative choice**

Seven repair routes were enumerated: (L1) operator-valued clock and (L2) 32 independent bulk clocks evade A19.NG2 but break minimality; (L3) thermal equipartition then freeze-out is gate G5; (L4) projectable integration constant modifies the Hamiltonian constraint; (L5) per-face flux re-imports occupancy. The two adopted are (L6) a common parent BFV charge branching into a 32- and a 6-module and (L7) a connected dual-face graph whose harmonic charge is automatically equipartitioned; the bulk uses Brown–Kuchař dust. L6+L7 add no new field and no new number beyond the two fixed face-module ranks.

### **§10.2 The parent matter face module (rank-6 projector, gate G3)**

Cold module E\_c \= C²(TI), dim 32; baryon module E\_b \= C²\_□(tO) ≅ C²(cube), dim 6 \= XZ. Their direct sum E\_m \= E\_c ⊕ E\_b (dim 38\) carries canonical projectors P\_c \= diag(I₃₂, 0), P\_b \= diag(0, I₆), with P\_c \+ P\_b \= I₃₈ — the rank-6 projector v1.4 lacked (G3). Status DERIVED-CONDITIONAL on identifying E\_c ⊕ E\_b as the physical matter boundary phase space; the direct sum sidesteps gate G2 (the unproven X⊗Q tensor product) rather than resolving it.

### **§10.3 ZHCS-1 (seam connectivity): corrected to DERIVED-CONDITIONAL; cross-block repaired**

**Cold block — PROVEN.** The truncated-icosahedron face graph has 32 nodes, 90 edges, one component, Laplacian rank 31 (Appendix C). **Baryon block — the cube graph is a re-wiring.** v2.0 wired the six tO square faces as a cube face graph (K\_{2,2,2}: 12 edges, connected, rank 5). The recomputation confirms that abstract graph is connected, but also that **in tO the six squares are mutually non-adjacent** (zero shared edges, separated pairwise by hexagons), so the physical square adjacency is six isolated nodes (rank 0). The cube wiring is a count/duality re-identification, not the seam’s physical face-adjacency; baryon-block connectivity is therefore DERIVED-CONDITIONAL on “cube adjacency \= physical baryon adjacency.” v2.0 recorded this as an isolated-square failure mode; v2.3 elevates it to a gate.  
**Cross-block W\_bc — v2.0 argument retracted; re-grounded structurally.** v2.0 inferred full cross-support from the truncated-icosahedron incidence null vector being nowhere zero, then invoked “the analogous tO null mode.” Two errors: an incidence-kernel vector v satisfies R\_c v \= 0 by definition and is generically a different object from the transfer-support vector; and **the tO incidence kernel is two-dimensional** (Appendix C), so there is no unique tO null mode. v2.3 replaced this with a uniform-sector Monte Carlo, but that is also weak: a continuous coupling distribution has exact-zero probability 0 by construction, so “zero hits” shows only that random matrices rarely cancel — not that the actual corpus W\_bc ≠ 0\. v2.4 re-grounds the claim on the corpus’s own mediation structure. Because L\_XY ≡ 0 (PROVEN, ZS-F1/S1/M6), all cross-transfer passes through the single β₀ (Z₂-even) mode z₀, as the PROVEN rank-1 channel C\_ZX \= κ|z₀⟩⟨r\_X|, C\_ZY \= κ|r\_Y⟩⟨z₀|, with

κ² \= A/Q \= (35/437)/11 \= 35/4807 ≈ 7.28×10⁻³ ≠ 0  (PROVEN).

The uniform-sector cross-transfer is then W\_bc(uniform) \= κ² ⟨baryon\_uniform | r\_X⟩ ⟨r\_Y | cold\_uniform⟩, which vanishes **only if a whole block has zero overlap with z₀** — i.e. a block decoupled from the unique mediation mode, exchanging no information across the seam, hence not part of the seam at all (gate F-A19.7, a separately falsifiable structural pathology, not a generic fine-tuning). This is a structural argument, not a statistical one; κ² \= A/Q ≠ 0 is PROVEN, so vanishing would require an orthogonality not present in the corpus mediation. **Status: ZHCS-1 DERIVED-CONDITIONAL on C1a ∧ C1b**, where **C1a** \= the physical baryon adjacency is the cube graph (corpus-supported: ZS-F2 §11.4 defines the baryon module as the 6 \= F(cube) \= XZ face module, not the tO-square embedding) and **C1b** \= the explicit corpus overlaps ⟨z₀ | r\_X⟩, ⟨z₀ | r\_Y⟩ are nonzero (confirmation gate F-A19.2). The tO incidence kernel never enters this argument, so its two-dimensionality is irrelevant.

### **§10.4 ZHCS-2 (harmonic boundary charge): corrected, then collapsed to one condition C1**

The boundary action carries only a harmonicity constraint, S\_Σ^harm \= ∫\_Σ √h ⟨χ, d\_Γ p⟩ ⇒ d\_Γ p \= 0\. **v2.0 correction:** the BV-BFV modified quantum master equation gives Ω∂Σ ψ \= −ℏ² ΔV ψ, **not** Ω∂Σ ψ \= 0; the latter needs ΔV ψ \= 0 as well. Moreover the 2D-Abelian U(1) Hodge construction v2.0 cited (Malik) is a special case, not a general BFV theorem. **Co-closedness dissolved:** the parent charge is a 0-cochain on the 38 nodes; the Hodge 0-Laplacian L₀ \= d₀† d₀ has no down-part (no degree −1), so ker L₀ \= ker d₀ and “harmonic” equals “closed” — no separate co-closed condition exists. **Collapse to C1:** in cellular abelian BF theory on a CW complex (Cattaneo–Mnev–Reshetikhin), the cellular cochains carry the BFV structure with the boundary operator equal to the cellular coboundary, the mQME holds, and the abelian case is non-anomalous so ΔV annihilates the state, giving Ω∂Σ ψ \= 0 with Ω∂Σ \= d\_Γ. This is a **conditional reduction, not a closure**: CMR proves C1c ⇒ (Ω∂Σ \= d\_Γ), but **not** S\_ZS ⇒ C1c — that the discretization of the ZS-F0 boundary action on Γ\_m is exactly the cellular cochain complex remains to be shown. **Status: ZHCS-2 DERIVED-CONDITIONAL** on **C1c: the seam boundary theory is cellular abelian BF on Γ\_m** (corpus-supported but not derived; C1c as a Z-Spin statement is HYPOTHESIS-strong/OPEN).  
**Conditional core (ZHCS-2★) — PROVEN-CONDITIONAL.** On a connected Γ\_m the combinatorial Hodge theorem (Eckmann; Lim) gives ker L\_Γ \= span(1₃₈); with Ω∂Σ \= d\_Γ the harmonic parent charge is uniform, so Q\_c : Q\_b \= 32 : 6, invariant under p ↦ α p (verified, Appendix C). PROVEN-CONDITIONAL on C1c ∧ connectivity, co-closedness caveat removed.

### **§10.5 The rank-ratio theorem: DERIVED-CONDITIONAL on C1 ∧ C2**

Given ZHCS-1 and ZHCS-2, Q\_c \= 32 p★, Q\_b \= 6 p★, **Q\_c/Q\_b \= 32/6 \= 16/3**. The graph ratio is PROVEN-CONDITIONAL on C1 ∧ connectivity; the **physical density** ratio additionally needs equal normalization ε\_c \= ε\_b (ZHCS-3, condition C2 below). Correcting v2.0, the physical 32:6 is **DERIVED-CONDITIONAL on C1 ∧ C2**, not on a single identification. A19.NG2 is respected: the common p★ → α p★ leaves the ratio invariant.

### **§10.6 ZHCS-3 (canonical gluing): DERIVED-CONDITIONAL on C2**

The bulk uses the full Brown–Kuchař reference dust S\_c^BK \= −½ ∫√(−g) ρ\_c (g^{μν} U\_μ U\_ν \+ 1), U\_μ \= −∂\_μ T\_Z \+ W\_I ∂\_μ X^I, giving w\_c \= c\_s² \= 0, ρ\_c ∝ a⁻³ (IMPORTED-PROVEN), the Z-anchor surviving only as a Jacobian locator. **Restored canonical-branching action** (dropped in v2.3): the rank enters only through the boundary branching

S\_branch \= ∫\_Σ\* √h \[ ⟨Λ\_c, Π\_c − P\_c p⟩ \+ ⟨Λ\_b, Π\_b − P\_b p⟩ \] ,   T\_c| \= T\_b| \= T\_\* .

The constraints set Π\_c \= P\_c p, Π\_b \= P\_b p; since P\_c \+ P\_b \= I₃₈ the boundary symplectic potentials add to the conserved parent charge,

Θ\_c \+ Θ\_b \= ⟨(P\_c \+ P\_b) p, δT\_\*⟩ \= ⟨p, δT\_\*⟩ \= Θ\_\* ,

an identity carrying no 32 or 6 in the action. **Equal-normalization theorem (explicit, feedback 7.1):** Brown–Kuchař alone does NOT give ε\_c \= ε\_b. It is FORCED once the parent boundary Hamiltonian is single-coefficient linear in the parent charge, H\_parent \= ε\_\* (P\_c \+ P\_b) p \= ε\_\* p; then H\_c \= ε\_\* Q\_c, H\_b \= ε\_\* Q\_b, so ε\_c \= ε\_b \= ε\_\* (verified, Appendix F). **Status: ZHCS-3 DERIVED-CONDITIONAL** on **C2**, split into **C2-norm** (single-coefficient linearity H \= ε\_\* p) and **C2-branch** (S\_branch descends from ZS-F0). ZHCS-3 is reduced to these two explicit statements, not closed by the name C2.

### **§10.7 ZHCS-4 (adiabaticity): PROVEN-CONDITIONAL on C2 \+ adiabatic selection**

Because both species are projections of one parent charge p, the branching leaves the charge sector parametrized by p alone — no independent dust-density integration constant of the old multiplier λ\_c (Appendix F); a perturbation p★ → p★(1 \+ δ) gives δQ\_c/Q̄\_c \= δQ\_b/Q̄\_b, so ζ\_c \= ζ\_b, S\_cb \= 0 gauge-invariantly. **Weinberg gives existence, not occupation:** the theorem proves an adiabatic mode always exists, not that the initial state occupies only it — non-adiabatic modes can coexist. Closing ζ\_c \= ζ\_b \= ζ\_γ additionally requires the initial state to lie in the adiabatic sector; the branching makes this natural but does not impose it. **Status: ZHCS-4 PROVEN-CONDITIONAL** on **C2 \+ no-independent-entropy / adiabatic selection** (corrected from v2.3). **Co-moving narrowed (feedback 7.2):** cold and baryon share the parent clock T\_\* and curvature perturbation only at the branching hypersurface Σ\_\* (adiabatic IC); after Σ\_\* the baryon couples to photons (BAO) and the cold free-streams, so co-moving to recombination is RETRACTED and standard Boltzmann transfer handles the divergence — no conflict with baryon acoustic physics.

### **§10.8 The four ZHCS theorems and the two named conditions**

Table 6\. ZHCS theorems: v2.0 (as claimed) vs v3.1 (conditional reduction). Named corpus conditions: (a) C\_ZY couples β₀ to a corpus-natural trivial combination (so ⟨r\_Y|1₃₂⟩ ≠ 0); (b) the ZS-F0 boundary term S\_∂M does not mix the BF and Maxwell sectors at degree 0→1; (c) S\_ZS adds no block-dependent boundary energy (so ε\_c \= ε\_b). C1-A (Stückelberg→BF dual) is DERIVED unconditionally.

| Theorem | Statement | v2.0 | v3.1 (conditional reduction) |
| ----- | ----- | ----- | ----- |
| ZHCS-1 | Seam graph connected via actual W\_bc. | DERIVED | **DERIVED-CONDITIONAL** on (a) \[C1-B\] |
| ZHCS-2 | Ω∂Σ^(0→1) \= q\_Z d\_Γ (BF dual). | DERIVED | **DERIVED-CONDITIONAL** on (b) \[C1-C\]; C1-A DERIVED |
| ZHCS-2★ | Connected \+ harmonic ⇒ 32:6. | (folded in) | **PROVEN-CONDITIONAL** (Eckmann/Lim) |
| ZHCS-3 | ε\_c \= ε\_b from P\_T \= −H\_ZS. | OPEN | **DERIVED-CONDITIONAL** on (c) \[C2-E\] |
| ZHCS-4 | ζ\_c \= ζ\_b \= ζ\_γ, S\_cb \= S\_cγ \= 0\. | OPEN | **DERIVED-CONDITIONAL** on single source |
| 32:6 (physical) | Cold-to-baryon density ratio. | DERIVED-COND (single ID) | **DERIVED-CONDITIONAL on C1 ∧ C2** |
| 32:6 ω\_c=0.119112 | Action-level abundance. | — | **DERIVED-CONDITIONAL on (a)∧(b)∧(c) \+ single source** |

**Verdict (v3.1).** ZHCS reduces G1–G8 to four theorems with a real structural backbone (Stückelberg→BF dual, connected physical graph, second-class branching reduction). v3.1 corrects the v3.0 over-statement: C1 is DERIVED-CONDITIONAL on (a) ∧ (b) and C2 on (c) \+ a single source, where (a)–(c) are three named, falsifiable corpus conditions (Appendix I). The physical 32:6 ratio and ω\_c \= 0.119112 are DERIVED-CONDITIONAL on (a) ∧ (b) ∧ (c) \+ single source. This is a conditional reduction, not a closure; the residual is now fully characterized rather than diffuse. Details in §10.9–§10.11 and Appendix I.

## **§10.9 Closing C1: Stückelberg→BF dualization, actual-W\_bc connectivity, and the BFV differential**

Following the v2.4 review, C1 is narrowed to **C1′**: the β₀ boundary-charge sector of the S10 Stückelberg U(1) is isomorphic to cellular BF on the actual seam graph Γ\_m. C1′ is closed by three explicit steps (Appendix G).

### **§10.9.1 C1-A — Stückelberg → BF dual**

The corpus gives the Stückelberg covariant derivative D\_μΦ \= (∂\_μ − iκ g\_Y B\_μ)Φ with κ² \= A/Q; in the frozen-radial limit Φ \= e^{iθ} the gauge-invariant combination is dθ − q\_Z B\_Y with q\_Z \= κ g\_Y. Introduce the first-order parent action

S\_par \= ∫\_M \[ −(1/2f\_Z²) H∧\*H \+ H∧(dθ − q\_Z B\_Y) − (1/2g\_Y²) F\_Y∧\*F\_Y \]

with H an independent 3-form. Varying H gives H \= f\_Z² \*(dθ − q\_Z B\_Y), which on back-substitution recovers the original Stückelberg kinetic (f\_Z²/2)(dθ − q\_Z B\_Y)∧\*(·) (verified, Appendix G). Varying θ instead gives dH \= 0, so locally H \= dB for a 2-form B, and the dual action is

S\_dual \= −(1/2f\_Z²) ∫ dB∧\*dB \+ q\_Z ∫ B∧F\_Y − (1/2g\_Y²) ∫ F\_Y∧\*F\_Y \+ S\_∂M .

The 4D Stückelberg/Proca system dualizes to a 2-form–1-form BF coupling q\_Z ∫ B∧F\_Y — an externally established structure. The full seam theory need not be pure BF; the Maxwell/kinetic terms carry bulk propagation while the BF term carries the boundary charge constraint. **C1-A is DERIVED** (the BF subsector follows from the corpus Stückelberg action, not assumed).

### **§10.9.2 C1-B — actual corpus W\_bc, no cube rewiring**

On 38 face-nodes set p\_f \= ∫\_{f∨} B (parent charge on faces) and a\_e \= ∫\_e B\_Y (seam edge variable). The corpus fixes the cross-transfer as the rank-1 β₀ channel C\_bZ \= κ|r\_b⟩⟨z₀|, C\_Zc \= κ|z₀⟩⟨r\_c| with r\_b \= 1₆/√6, r\_c \= 1₃₂/√32, z₀ \= 1₂/√2, giving

W\_bc \= C\_bZ K\_Z C\_Zc \= κ² ⟨z₀|K\_Z|z₀⟩ |r\_b⟩⟨r\_c| \= κ² k₀ |r\_b⟩⟨r\_c| ,   κ² \= A/Q \= 35/4807 ≠ 0 .

Since k₀ \= ⟨z₀|K\_Z|z₀⟩ ≠ 0 (z₀ is the physical β₀ mediation mode; k₀ \= 0 would mean no mediation, contradicting κ² ≠ 0), all 6×32 entries are nonzero and min\_i Σ\_j |W\_ij|² \> 0: **every baryon node attaches to the connected TI block**. Building the physical graph as the real TI face adjacency (32 nodes, connected) plus six **isolated** square nodes plus the actual W\_bc cross-edges, the 38-node Laplacian has rank L\_Γ \= 37 and ker \= span{1₃₈} (Appendix G). The cube rewiring is **eliminated**: connectivity holds on the genuine tO-square (isolated) baryon block via the actual transfer. **C1-B is DERIVED** (conditional only on k₀ ≠ 0, which is structural).

### **§10.9.3 C1-C — boundary BFV differential**

Discretizing the dual boundary action on Γ\_m, the cellular BF boundary action is S\_∂,Γ \= q\_Z ∫\_{Σ\_\*} aᵀ d\_Γ p; varying a gives d\_Γ p \= 0, and the boundary BFV operator’s degree-0→1 block is Ω∂Σ^(0→1) \= q\_Z d\_Γ (cellular BF, Cattaneo–Mnev–Reshetikhin). Building d\_Γ as the signed incidence of the physical graph, ‖Ω∂Σ^(0→1) − q\_Z d\_Γ‖ \= 0 with rank d\_Γ \= 37, dim ker d\_Γ \= 1, so d\_Γ p \= 0 ⇒ p \= p\_\* 1₃₈. **C1-C is DERIVED** (residual: that the discretization of the dual boundary action on Γ\_m is exactly the cellular cochain complex — the natural 1-complex discretization).  
**C1 verdict (v3.1, corrected).** C1-A (Stückelberg→BF dual) is DERIVED. C1-B is DERIVED-CONDITIONAL on **(a)**: F\_TI carries the trivial representation with multiplicity two (span{1\_pent, 1\_hex}), so the cross-overlap ⟨r\_Y | 1₃₂⟩ is corpus-dependent — the vanishing locus is a single ray that every corpus-natural candidate avoids (uniform → 32, Lemma-4.5 mode (−2,1) → −4, pure pentagon/hexagon), but the actual C\_ZY value is corpus data. C1-C is DERIVED-CONDITIONAL on **(b)**: v3.0’s ‖Ω − q\_Z d\_Γ‖ \= 0 was tautological (Ω was defined as q\_Z d\_Γ); the BF term genuinely gives q\_Z d\_Γ and Maxwell a separate degree-1 Gauss constraint, but that the ZS-F0 boundary term S\_∂M does not mix sectors needs the explicit S\_∂M. **So C1 \= C1-A ∧ C1-B ∧ C1-C is DERIVED-CONDITIONAL on (a) ∧ (b).**

## **§10.10 Closing C2: Brown–Kuchař clock-energy branching, equal normalization, and entropy**

C2 is narrowed to **C2′**: one Brown–Kuchař clock-energy momentum canonically branches into cold and baryon at Σ\_\*. C2′ \= C2-E ∧ C2-A ∧ C2-D (Appendix H).

### **§10.10.1 C2-E — equal normalization from P\_T \= −H\_ZS**

Performing the ADM decomposition of S\_ZS \+ S\_BK \+ S\_branch, the total Hamiltonian constraint is C \= P\_T \+ H\_ZS \= 0, so P\_T \= −H\_ZS: the parent charge p is the clock-energy momentum, not a mere number charge. The branching constraints Π\_c \= P\_c p, Π\_b \= P\_b p are then complementary projections of one P\_T (P\_c \+ P\_b \= I₃₈), so the node-wise Legendre transform gives Π\_{T,a} \= −√h ρ\_a with the **same** coefficient for all 38 nodes — ε\_c \= ε\_b is forced, with no separate equal-normalization assumption (Appendix H). The symplectic potentials add to the conserved parent charge, Θ\_c \+ Θ\_b \= ⟨(P\_c \+ P\_b)p, δT\_\*⟩ \= Θ\_\*. **C2-E is DERIVED** (on the Brown–Kuchař ADM constraint structure).

### **§10.10.2 C2-A — no independent entropy mode**

Choosing Σ\_\* as the uniform-total-density hypersurface (δρ\_tot \= 0\) and tying the parent amplitude to the single clock (δp\_\* − (ε/ρ̄̇) p̄̇\_\* δρ\_ε \= 0), the intrinsic transfer perturbations vanish, δQ\_c^intr \= δQ\_b^intr \= 0, so S\_cb \= 3(ζ\_c − ζ\_b) \= 0 and S\_cγ \= 3(ζ\_c − ζ\_γ) \= 0 follow as constraint consequences, not as a chosen initial condition. Weinberg’s theorem guarantees the existence of the adiabatic mode; occupation requires that no independent spectator generate p\_\*. **C2-A is DERIVED-CONDITIONAL on a single source** (no independent spectator at Σ\_\*) — the one genuine remaining physical input.

### **§10.10.3 C2-D — post-branching separation, and relative-mode removal**

After Σ\_\* the components separate by their own interaction Hamiltonians: the cold component is geodesic (u\_c·∇u\_c \= 0\) and the baryon couples to photons (∇·T\_b \= C\_γb), so “co-moving to recombination” is not asserted and there is no conflict with baryon acoustic physics. Of the 38 graph modes, the uniform mode is the parent charge and the 37 relative modes (eigenvalues λ₂, …, λ₃₈ \> 0 of L\_Γ) are BRST-exact in the topological BF (which carries no local degrees of freedom), so the physical cohomology is H⁰\_phys(Γ\_m) \= span{1₃₈}: the independent cold–baryon entropy mode is removed at the action level. **C2-D is DERIVED.**  
**C2 verdict (v3.1, corrected).** The Dirac analysis is real: the four branching constraints are second-class (constraint matrix det \= 1), reducing to the single pair (p, T\_\*) with Θ\_red \= Θ\_\*. C2-E (ε\_c \= ε\_b) is DERIVED-CONDITIONAL on **(c)**: it follows from the pure Brown–Kuchař Hamiltonian, but if S\_ZS adds a block-dependent boundary term ε\_c′ P\_c p \+ ε\_b′ P\_b p with ε\_c′ ≠ ε\_b′ the reduction gives ε\_c ≠ ε\_b. C2-A is DERIVED-CONDITIONAL on a single source (no independent spectator at Σ\_\*). The 37 relative modes are removed by failing the constraint d\_Γ p \= 0 (constraint-exclusion); the stronger gauge-exactness reading needs the edge-sector ghost complex (not done). **So C2 \= C2-E ∧ C2-A ∧ C2-D is DERIVED-CONDITIONAL on (c) \+ a single source.**

## **§10.11 Theorem A19.ZHCS-Closure**

**Theorem A19.ZHCS-Closure (PROVEN-CONDITIONAL on C1 ∧ C2).** Assume, now established by the computations above rather than assumed: (1) the β₀ sector of the S10 Stückelberg U(1) dualizes to cellular BF on Γ\_m (C1-A); (2) the actual corpus W\_bc connects all six baryon nodes to the connected TI block (C1-B); (3) the boundary BFV differential is Ω∂Σ^(0→1) \= q\_Z d\_Γ (C1-C); (4) the parent BF charge is canonically identified with the Brown–Kuchař clock-energy momentum P\_T \= −H\_ZS (C2-E); and (5) there is no independent entropy source at Σ\_\* (C2-A). Then

d\_Γ p \= 0  ⇒  p \= p\_\* 1₃₈ ,   ρ\_c/ρ\_b \= (1ᵀ P\_c p)/(1ᵀ P\_b p) \= 32/6 \= 16/3 ,

w\_c \= 0, c\_s,c² \= 0, π\_c \= 0 ,   S\_cb \= S\_cγ \= 0 ,

**Status (v3.1): the physical 32:6 ratio and ω\_c \= 0.119112 are DERIVED-CONDITIONAL on (a) ∧ (b) ∧ (c) \+ a single source.** C1-A is DERIVED; C1-B, C1-C, and C2-E carry the named corpus conditions (a), (b), (c) respectively (Appendix I); the single-source condition (C2-A) and the constraint-exclusion of the relative modes complete the residual. A19.NG2 is respected throughout (the common p\_\* → α p\_\* leaves the ratio invariant). This is the honest terminus: a conditional reduction with a three-condition residual, not an unconditional derivation.

## **§11. Consistency Conditions and Registered Gaps**

**O-A19.4 (Algebra / trace, sharpened by A19.NG1).** The rank-32 projector lives in the 121-dimensional channel space, whereas A\_ZS sits in M₁₁ with center weights (3, 3, 5)/11 ≠ (3, 2, 6)/11; reconciliation needs a §7 repair path, none derived.  
**O-A19.5 (A₅ vs the (2,3,6) blocks).** The A₅-invariant subspace dims of V₁₁ are {0, 3, 5, 6, 8, 11}; 2 does not occur, so dim(Z) \= 2 is not an A₅-subrepresentation. If A₅ is the full register symmetry the Z-sector is not preserved; if the Z-sector is an exact block, A₅ does not commute with (2,3,6). Admissible repairs: A₅ acts on a separate module; A₅ breaks to a subgroup; withdraw V₁₁; or build an explicit intertwiner. Pending this, the cosmological status of Theorem A19.2 is DERIVED-CANDIDATE.  
**O-A19.2 (Canonicality).** End(V₁₁) has repeated irreducibles, so ∃ P\_BT but not ∃\! P\_BT; canonical selection needs a physical principle (incidence map, Z-seam parity, transfer spectral projector). **O-A19.3 (Primitivity).** A dynamical equipartition needs the boundary channel unital and primitive; an A₅-twirl is insufficient (reducible rep, w₅/w₆ freedom). OPEN.

## **§12. Consistency with Observation**

Table 7\. Geometric partition versus Planck 2018\.

| Component | Fraction | Value | Planck 2018 | Status |
| ----- | ----- | ----- | ----- | ----- |
| Baryons Ω\_b | 6/121 | 0.0496 | 0.0493 | PASS |
| Cold DM Ω\_cdm | 32/121 | 0.2645 | 0.264 | PASS |
| Matter Ω\_m | 38/121 | 0.3140 | 0.315 | PASS |
| Dark energy Ω\_Λ | 83/121 | 0.6860 | 0.685 | PASS |

With h \= 0.6736, Ω\_cdm h² \= 0.12000, matching ω\_c \= 0.120; (38 \+ 83)/121 \= 1\. No tension is introduced and the ZS-A18 NO-GO is preserved. As of v2.3 the structural ratio is a DERIVED-CONDITIONAL output of the ZHCS harmonic boundary charge (conditional on C1 ∧ C2), not merely imposed: ω\_c/ω\_b \= 16/3 \= 5.333 vs Planck 5.364 ± 0.065 (−0.48σ); ω\_c \= 0.119112 vs 0.1200 ± 0.001 (−0.89σ). Neither uses h, removing ZS-F2’s circularity; η\_B and ω\_b are not counted as two successes.

## **§13. Falsification Gates**

Table 8\. Multilayered falsification gates for ZS-A19 (v3.1).

| Gate | Layer | Falsification condition | Status |
| ----- | ----- | ----- | ----- |
| F-A19.1 | Math | A₅ rep theory wrong (V₁₁ ≠ 3⊕3′⊕5, or rank P\_BT ≠ 32). | PASSING |
| F-A19.2 | Sim/consistency | Explicit W\_bc on corpus matrices \= 0 (lands on the codim-1 locus). | OPEN |
| F-A19.3 | Theoretical | Seam theory shown NOT cellular abelian BF (C1 false), or Ω∂Σ ≠ d\_Γ. | OPEN |
| F-A19.4 | Theoretical | Canonical analysis forces ε\_c ≠ ε\_b (C2 false). | OPEN |
| F-A19.5 | Cross-paper | Closing BT-C requires modifying A or Q, or contradicts ZS-A18. | PASSING |
| F-A19.6 | Observational | The partition 6/32/38/83 over 121 inconsistent with data. | PASSING |
| F-A19.7 | Math (immediate) | A block decouples from Z (a \= 0 or c \= 0), collapsing the seam. | PASSING |
| F-A19.8 | Cross-paper (NG1) | All three §7 repair paths shown unavailable → F23 link void. | OPEN |
| F-A19.9 | Cross-paper (ε-Halo) | No resolution of O-A19.6 → carrier conflicts with ZS-A1. | OPEN |
| F-A19.10 | Observational | Isocurvature detected between cold and baryon (no single clock) → C2 / ζ\_c=ζ\_b refuted. | OPEN |
| F-A19.11 | Observational | Future ΛCDM fits move ω\_c/ω\_b away from 16/3 beyond face-counting tolerance. | OPEN |
| F-A19.12 | Anti-numerology | An MC for the specific ZHCS closure returns p \> 5% → ratio → HYPOTHESIS-weak. | OPEN |
| F-A19.13 | Decisive (emergence) | Microscopic equilibrium-state weights ≠ rank-proportional (≠ 32:6, ≠ (3,2,6)/11). | OPEN (decisive) |
| F-A19.14 | Decisive (rank) | No construction relocates rank 32 into a physical observable (G1) → by A19.NG2 the claim is empty. | OPEN (decisive) |

**AN-A19.1 (EXECUTED, PASS).** No parameter beyond (A, Q, (Z, X, Y)). The instanton survival probability P\_cand \= (A/2Q)e^{−π/A} ≈ 3.4×10⁻²⁰, numerically near the relic-dilution target, is REJECTED (neither factor derived; selected after seeing the target). The \~10⁹ GeV scale is external context only. The 32/121 normalization is admissible only if μ is fixed by F2 without fitting (F-A19.7-type); fitting μ is the explicit failure mode.

## **§14. The Closure Program and Non-Claims**

Two action-level routes remain on the table: the geometric Z-clock dust of §8 (gates BRL-1–6) and the X-pullback route of v1.0–v1.1 (gates BTD-1–6 below), retained as a nonlinear completion and cross-check. Each gate is settled by action variation, a Noether/current computation, an external PROVEN theorem, or a finite matrix computation — never by fitting a number.

Table 9\. Closure program (Z-Spin Boundary-Tension-to-Dust).

| Gate | Requirement | Status |
| ----- | ----- | ----- |
| BTD-1 | X-sector slots as action-level comoving maps X^I : M → T³. | HYP-strong |
| BTD-2 | Conserved J^μ from F0/F2 boundary variation as a quantized per-face charge. | OPEN |
| BTD-3 | Boundary energy S \= −∫√(−g) μ(−J²)^{1/2}, giving p \= 0, c\_s² \= 0, ρ ∝ a⁻³. | DERIVED-COND |
| BTD-4 | Q\_BT/Q\_total \= 32/121 (Theorem A19.2) with no observational fit of μ. | DERIVED-COND |
| BTD-5 | Adiabatic, passive initial conditions S\_BTγ \= 0 from a single Z-Spin clock. | OPEN |
| BTD-6 | Z-anchor as the Jacobian singularity det(∂X) \= 0, linked to the SMBH locator. | HYP-strong |
| NG1 / trace | Reconcile A\_ZS/M₁₁ via a §7 repair path. | NO-GO+OPEN |
| A₅-align | Make A₅ (V₁₁) compatible with the (2,3,6) blocks and L\_XY \= 0\. | OPEN |
| O-A19.6 | Resolve the ε-Halo overlap so dust and Goldstone halo do not double-count. | OPEN |
| Boltzmann | Implement boundary-dust perturbations in CLASS/CAMB; reproduce C\_ℓ and P(k). | OPEN |

**Non-claims.** **NC-A19.1:** ZS-A19 does not claim the third peak is solved; C1, C2, BT-C and the gate sets are OPEN, and no gate reaches unconditional DERIVED. **NC-A19.2:** does not contradict ZS-A18; a different carrier outside the Goldstone scope, frozen at v1.5. **NC-A19.3:** the \~10⁹ GeV scale and instanton probability are not derivations (anti-numerology). **NC-A19.4:** Z-anchors are locators, not CDM mass carriers. **NC-A19.5:** does not claim one theorem closes both ZS-F23 and the abundance — RETRACTED by A19.NG1. **NC-A19.6:** μ is not derived from ZS-F2; BRL-ZCD removes μ but introduces BRL-1/BRL-3. **NC-A19.7:** ω\_c \= 0.119112 is a conditional output (on η\_B, the boundary lock, and the external BBN coefficient), not an independent measurement; η\_B and ω\_b are not two successes. **NC-A19.8:** Weinberg constancy is invoked only in the standard single-clock regime. **NC-A19.9:** v2.3 does not claim C1 or C2 are established; both are physical identifications backed by external theorems, not theorems of the corpus.

## **§15. Conclusion**

Every previously blocked route to the Z-Spin third peak assumed dark matter is a collection of objects, and each met an obstruction — over-closure, an underived \~10⁹ GeV scale, or an absent carrier — that is an artifact of that premise. Taking ZS-F2’s definition of CDM as a geometric boundary tension literally, and supplying a conserved pullback / Brown–Kuchař dust, removes the EOS, sound-speed, and over-closure problems at once, with the Goldstone exactly massless and the ZS-A18 NO-GO intact. The fraction 32/121 is a machine-checked algebraic statement: F\_TI embeds A₅-equivariantly in the 121-dimensional channel space as a rank-32 projection of canonical trace 32/121, the “32 charge” disciplined as a projection-class rank (not a spatial-topological charge or a metric tension). Two proven no-gos bound the program: A19.NG1 (BT-C and ZS-F23 Condition C are distinct traces) and A19.NG2 (a bulk scalar-clock rank-lock is absorbed by a multiplier).  
It then imports four PROVEN theorems as a conditional reduction (not a closure): they prove the implications but not that the Z-Spin seam satisfies their antecedents. The cross-block claim is re-grounded structurally on the corpus rank-1 β₀ mediation (κ² \= A/Q \= 35/4807 ≠ 0, PROVEN), so W\_bc \= 0 would require a block decoupled from the unique mediation mode, not a generic non-cancellation. The restored canonical-branching action S\_branch, with symplectic-charge conservation Θ\_c \+ Θ\_b \= Θ\_\*, gives the equal normalization ε\_c \= ε\_b an action-level meaning: it is forced once the parent boundary Hamiltonian is single-coefficient linear (H \= ε\_\* p). The named conditions are split into checkable sub-conditions — C1a (physical cube adjacency), C1b (corpus W\_bc ≠ 0), C1c (cellular-abelian-BF seam, via Cattaneo–Mnev–Reshetikhin, with the conditional core PROVEN-CONDITIONAL via Eckmann/Lim), C2-norm and C2-branch (equal-Hamiltonian normalization and its action), and adiabatic selection (Weinberg gives an adiabatic mode’s existence, not its occupation). The honest terminus: the physical 32:6 ratio is DERIVED-CONDITIONAL on C1 ∧ C2, and the third acoustic peak COMPUTED-CONDITIONAL on C1 ∧ C2 ∧ adiabatic selection ∧ standard Boltzmann transfer, with each sub-condition carrying a proven backbone and an explicit falsification gate. ZS-A19 ends not with a closure but with a precise, falsifiable, partly computable map of exactly what remains — the physical identifications C1c, C2-norm, C2-branch, and adiabatic occupation — with the dust EOS IMPORTED-PROVEN, the integers pre-existing, the ZS-A18 NO-GO frozen, and no new parameter fitted.  
**v3.1 terminus.** v3.0 claimed to close C1 and C2; a second review showed the closure over-stated three steps, and v3.1 records the correction honestly. The structural backbone stands: the Stückelberg→BF dualization of the corpus S10 action (C1-A DERIVED), the connected physical 38-node graph with the cube rewiring eliminated, the Brown–Kuchař constraint P\_T \= −H\_ZS with Θ\_c \+ Θ\_b \= Θ\_\*, and the second-class branching reduction to the single pair (p, T\_\*). But the cross-transfer overlap is corpus-dependent (F\_TI carries two trivial-representation copies, so ⟨r\_Y | 1₃₂⟩ needs the corpus C\_ZY — condition (a)); the boundary differential equals q\_Z d\_Γ only if the ZS-F0 boundary term does not mix sectors (condition (b), v3.0’s identity being tautological); and the single normalization ε\_c \= ε\_b holds only if S\_ZS is block-independent (condition (c)). The relative modes are constraint-excluded, not proven gauge-exact. Accordingly C1 is DERIVED-CONDITIONAL on (a) ∧ (b) and C2 on (c) \+ a single source, and the 32:6 ratio and ω\_c \= 0.119112 are DERIVED-CONDITIONAL on (a) ∧ (b) ∧ (c) \+ single source. This is the honest terminus: not a closed program, but a conditional reduction whose residual is three sharp, named, falsifiable corpus conditions (Appendix I) rather than diffuse identifications. The dust EOS remains IMPORTED-PROVEN, the integers pre-exist, the ZS-A18 NO-GO is frozen, A19.NG1/NG2 stand, and no new parameter is fitted.

## **Acknowledgements and Code Availability**

This paper consolidates internal Z-Spin Collaboration deep-exploration notes following ZS-A18 v1.5. The corrected polyhedral and graph-spectral results (Appendix C) are reproduced by zs\_a19\_verify\_v2\_1.py (14 checks) and the cross-transfer genericity (Appendix D) by zs\_a19\_i1c\_genericity.py (200,000-sample Monte Carlo), both NumPy/SciPy, no other dependencies. The v2.0 representation-theory, partition, EOS, NG1/NG2, anti-numerology, and CAMB checks are retained as previously archived. External dust, von Neumann embedding, BV-BFV/mQME, cellular BF, combinatorial-Hodge, Brown–Kuchař, and adiabatic-mode results are cited in full. This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility for all content.

## **Appendix A. Representation-Theory Verification**

A₅ table on classes (1A, 2A, 3A, 5A, 5B) with sizes (1, 15, 20, 12, 12); irreducibles 1, 3, 3′, 4, 5 (Σ dim² \= 60). The 12-vertex permutation character (12, 0, 0, 2, 2\) minus trivial gives χ(V₁₁) \= (11, −1, −1, 1, 1\) \= 3 ⊕ 3′ ⊕ 5; squaring gives χ(End V₁₁) \= (121, 1, 1, 1, 1\) with multiplicities (3, 6, 6, 8, 10\) and traceless 120 \= |I\_h|. The pentagon orbit (12, 0, 0, 2, 2\) and hexagon orbit (20, 0, 2, 0, 0\) sum to χ(F\_TI) \= (32, 0, 2, 2, 2\) \= 2(1 ⊕ 3 ⊕ 3′ ⊕ 4 ⊕ 5); each multiplicity (2) ≤ that in End(V₁₁), so the rank-32 embedding exists. For A19.NG1, 3m₃ \+ m₁ \+ 5m₅ \= 11 has the unique solution (1, 3, 1\) → weights (3, 3, 5)/11; the minimal amplification realizing 5·(3, 2, 6\) is (5, 10, 6\) on M₅₅. The pullback pressure p \= F − bF\_b vanishes for F \= −μb.

## **Appendix B. Dependencies and Cross-References**

Table B1. Principal corpus dependencies.

| Paper | Role in ZS-A19 |
| ----- | ----- |
| ZS-F2 | Ω\_cdm \= F(TI)/Q² \= 32/121; CDM as geometric boundary tension. |
| ZS-A18 (v1.5) | Massless-Goldstone NO-GO; frozen; defines the scope this carrier lies outside. |
| ZS-Q11 / ZS-F23 | A\_ZS \= M₃ ⊕ ℂ ⊕ M₅; canonical trace; Condition C, distinct from BT-C per A19.NG1. |
| ZS-M9 | Truncated-icosahedron 32-dim face module; A₅ ≅ I structure. |
| ZS-S10 | Vortex Bose/Fermi duality; holonomy (not Dirac) core spinor. |
| ZS-A1 / ZS-S3 | Massless Goldstone ε-Halo and Goldstone theorem (m\_θ \= 0). |
| ZS-U3 / ZS-F5 | η\_B \= (6/11)³⁵; η\_B→ω\_b Independence Warning; used by A19.4. |
| ZS-F0 | GHY term, Robin condition, BV-BFV functor, seam J as boundary operator. |
| ZS-A15 | Broken internal U(1)\_Z (supports the abelian structure of condition C1). |
| ZS-U6 | Radiation-era equipartition does not transfer to the matter era (§8.7). |
| ZS-S1 | Z-sector Z₂ split (one Z₂-even β₀, one Z₂-odd gauge); basis for XQ−1 \= 32\. |
| ZS-F10 | i-tetration internal time ν; ruled out as the dust clock by A19.6. |

## **Appendix C. Corrected Polyhedral / Graph Verification (14/14 PASS)**

tO: (V, E, F) \= (24, 36, 14), Euler 2; vertex–face incidence rank 12, kernel dim **2** (a uniform square mode and an independent hexagonal mode); the six square faces mutually non-adjacent (0 edges); cube face graph K\_{2,2,2} connected (rank 5). tI: (60, 90, 32), Euler 2; incidence rank 31, kernel dim 1; pentagon/hexagon entry ratio −2; (Σv)²/∥v∥² \= 4/17; face graph 32 nodes / 90 edges / connected / Laplacian rank 31\. Combined 38-node graph (cold ⊕ cube ⊕ one cross-edge) connected with one-dimensional constant Laplacian kernel, returning Q\_c : Q\_b \= 32 : 6\.

## **Appendix D. Conditional-Core Lemma (degree-0 Hodge)**

**Degree-0 Hodge.** For a finite connected graph with N nodes, L₀ \= d₀† d₀ has no down-part, so ker L₀ \= ker d₀ \= span(1\_N): a harmonic 0-cochain is constant, with no separate co-closed condition. With P\_c, P\_b (dims 32, 6; P\_c \+ P\_b \= I₃₈), Q\_c \= 32 p★, Q\_b \= 6 p★, ratio 32 : 6 independent of p★. **Note (v2.4):** the v2.3 uniform-sector genericity Monte Carlo is SUPERSEDED — a continuous distribution has exact-zero probability 0 by construction, so it could only show that random matrices rarely cancel. The cross-block claim is re-grounded structurally on the corpus β₀ mediation in Appendix F.

## **Appendix E. Verification Provenance (v2.0 60-check suite → v2.4)**

Table E1. Provenance of the verification suite. RETAINED: still valid as stated. SUPERSEDED: invalidated by the corrected substrate. RECOMPUTED: re-derived here with corrected values. NEW: added in v2.1–v2.4.

| Check group | Class | Note |
| ----- | ----- | ----- |
| A₅ rep theory, F\_TI embedding, τ\_Q \= 32/121 (Table 1\) | RETAINED | Appendix A; unaffected by the ZHCS corrections. |
| A19.NG1 trace incompatibility; A19.NG2 rank absorption | RETAINED | PROVEN no-gos; intact. |
| Planck partition 6/32/38/83 over 121 (Table 7\) | RETAINED | Face-counting budget; ZS-F2 §11.4. |
| CAMB third-peak consistency (Table 4\) | RETAINED | COMPUTED / OBSERVATIONALLY CONSISTENT, TT only. |
| tI face graph (32, 90, connected, rank 31); incidence kernel dim 1; v\_p \= −2 v\_h; (Σv)²/∥v∥² \= 4/17 | RECOMPUTED | Appendix C; confirms the v2.0 tI values. |
| tO 6 squares cube-adjacent; “unique tO null mode” cross-support | SUPERSEDED | tO incidence kernel is 2-dimensional; the six squares are mutually non-adjacent (Appendix C). v2.0’s cross-support argument retracted. |
| 38-node graph connected ⇒ harmonic charge uniform ⇒ 32:6 | RECOMPUTED | Appendix C; the conditional core, now PROVEN-CONDITIONAL via Eckmann/Lim. |
| Cross-block W\_bc ≠ 0 (uniform-sector Monte Carlo) | SUPERSEDED | Statistically weak (exact-zero probability 0 by construction); replaced by the structural β₀ argument, κ² \= A/Q (Appendix F). |
| Symplectic branching: Θ\_c \+ Θ\_b \= Θ\_\*; ε\_c \= ε\_b under H \= ε\_\* p | NEW | Appendix F; restores the v2.0 §10.6 branching and makes equal normalization explicit. |

## **Appendix F. Explicit C1/C2 Computation (16th–17th checks)**

**C1b (cross-transfer structure).** The corpus fixes the X–Z–Y mediation as the rank-1 β₀ channel C\_ZX \= κ|z₀⟩⟨r\_X|, C\_ZY \= κ|r\_Y⟩⟨z₀| with κ² \= A/Q \= (35/437)/11 \= 35/4807 ≈ 7.28×10⁻³ ≠ 0 (PROVEN). The uniform-sector cross-transfer is W\_bc(uniform) \= κ² ⟨baryon\_uniform | r\_X⟩ ⟨r\_Y | cold\_uniform⟩, vanishing only if a block has zero overlap with the unique β₀ mode z₀ — i.e. a block decoupled from all cross-seam transfer (L\_XY ≡ 0 forces every channel through z₀). This is a structural condition (gate F-A19.7), not a generic non-cancellation; the residual C1b is the explicit nonzero overlaps ⟨z₀|r\_X⟩, ⟨z₀|r\_Y⟩.  
**C2 (symplectic branching and equal normalization).** With P\_c \= diag(I₃₂, 0), P\_b \= diag(0, I₆) (P\_c \+ P\_b \= I₃₈), parent charge p \= p\_\* 1₃₈, the branching S\_branch sets Π\_c \= P\_c p, Π\_b \= P\_b p, giving Q\_c \= 32 p\_\*, Q\_b \= 6 p\_\*, and Θ\_c \+ Θ\_b \= ⟨(P\_c \+ P\_b)p, δT\_\*⟩ \= Θ\_\* (verified identity). Under the single-coefficient parent Hamiltonian H \= ε\_\* p, the block energies give ε\_c \= H\_c/Q\_c \= ε\_b \= H\_b/Q\_b \= ε\_\* exactly — equal normalization is forced, not assumed. The constraint surface is parametrized by p alone, so no independent dust-density integration constant survives; with harmonicity p \= p\_\* 1₃₈ (one dof), a perturbation gives ζ\_c \= ζ\_b. These results are reproduced by zs\_a19\_c1c2\_compute.py.

## **Appendix G. C1 closure computation (18th–20th checks)**

**C1-A (symbolic).** In the parent action S\_par, integrating out the 3-form H gives H \= f\_Z² \*(dθ − q\_Z B\_Y) and back-substitution returns the Stückelberg kinetic (f\_Z²/2)(dθ − q\_Z B\_Y)∧\*(·) (sympy-verified coefficient f\_Z²/2); varying θ gives dH \= 0, H \= dB, and the dual S\_dual \= −(1/2f\_Z²)∫dB∧\*dB \+ q\_Z∫B∧F\_Y − (1/2g\_Y²)∫F\_Y∧\*F\_Y. **C1-B.** With κ² \= A/Q \= 35/4807 and k₀ \= ⟨z₀|K\_Z|z₀⟩ ≠ 0, W\_bc \= κ² k₀ |r\_b⟩⟨r\_c| has all 6×32 entries nonzero (min |W\_ij| \> 0, min\_i Σ\_j|W\_ij|² \> 0). The physical graph (real TI adjacency \+ six isolated square nodes \+ actual cross-edges) has one component, Laplacian rank 37, kernel span{1₃₈} — no cube rewiring. **C1-C.** Building d\_Γ as the signed incidence of the physical graph, ‖Ω∂Σ^(0→1) − q\_Z d\_Γ‖ \= 0, rank d\_Γ \= 37, dim ker d\_Γ \= 1\. Reproduced by zs\_a19\_c1c2\_closure.py.

## **Appendix H. C2 closure computation (21st–22nd checks)**

**C2-E.** With P\_c \= diag(I₃₂, 0), P\_b \= diag(0, I₆) and the clock-energy momentum P\_T (= −H\_ZS), the node-wise normalization ε\_a \= Π\_{T,a}/(−√h ρ\_a) is equal across all 38 nodes (ε\_c \= ε\_b), and Θ\_c \+ Θ\_b \= ⟨(P\_c \+ P\_b)p, δT\_\*⟩ \= Θ\_\* (P\_c \+ P\_b \= I₃₈). **C2-A.** A single parent perturbation gives δQ\_c/Q\_c \= δQ\_b/Q\_b, so S\_cb \= 0; on the uniform-density slice the intrinsic transfers vanish, giving S\_cγ \= 0, conditional on a single source. **Relative modes.** L\_Γ has λ₁ \= 0 (uniform) and λ₂, …, λ₃₈ \> 0; in the topological BF these 37 modes are BRST-exact, so H⁰\_phys(Γ\_m) \= span{1₃₈}, dim 1\. **Consequence.** ρ\_c/ρ\_b \= 32/6, ω\_c \= (32/6) ω\_b \= 0.119112. Reproduced by zs\_a19\_c1c2\_closure.py.

## **Appendix I. Open Derivations: the three named corpus conditions (a)–(c)**

v3.0 reported C1 as DERIVED and C2 as DERIVED-CONDITIONAL on a single source. A second review identified three over-statements; v3.1 records them and reduces C1, C2 to the following named, falsifiable corpus conditions. Each is a sharp statement about corpus data (an intertwiner, a boundary term, or a sector weight), not a theorem the present tools can compute; supplying them would raise the corresponding gate to unconditional DERIVED.

Table I1. The three open derivations reducing C1 and C2.

| Cond. | Statement (what must be supplied) | Falsification / status |
| ----- | ----- | ----- |
| (a) | C\_ZY couples β₀ to a corpus-natural trivial combination, so ⟨r\_Y | 1₃₂⟩ ≠ 0 (C1-B). | F: if the corpus C\_ZY lands on the single vanishing ray (e.g. 5·1\_pent − 3·1\_hex), the uniform cross-transfer vanishes and the seam disconnects. Status: OPEN (corpus C\_ZY). |
| (b) | The ZS-F0 boundary term S\_∂M does not mix the BF and Maxwell sectors at degree 0→1 (C1-C). | F: if S\_∂M adds a boundary-localized degree-0→1 term, Ω∂Σ^(0→1) ≠ q\_Z d\_Γ. Status: OPEN (corpus S\_∂M). |
| (c) | S\_ZS adds no block-dependent boundary energy, so ε\_c \= ε\_b (C2-E). | F: if S\_ZS contributes ε\_c′ P\_c p \+ ε\_b′ P\_b p with ε\_c′ ≠ ε\_b′, equal normalization fails. Status: OPEN (corpus S\_ZS / ZS-A15). |

### **I.1 The F\_TI trivial multiplicity-two finding (condition a)**

F\_TI \= 2(1 ⊕ 3 ⊕ 3′ ⊕ 4 ⊕ 5\) carries the trivial representation with multiplicity **two**: the invariant subspace is span{1\_pent, 1\_hex} (uniform on the 12 pentagons, uniform on the 20 hexagons). The uniform parent charge 1₃₂ \= 1\_pent \+ 1\_hex is one vector in this plane; the β₀-coupled direction r\_Y is a corpus-determined combination. Scanning the family, the overlap ⟨r\_Y | 1₃₂⟩ vanishes on a single ray (≈ 5·1\_pent − 3·1\_hex, since 5·12 − 3·20 \= 0). Every corpus-distinguished candidate avoids it: uniform → 32, the ZS-F2 Lemma-4.5 mode (−2, 1\) → −4, pure pentagons → 12, pure hexagons → 20\. So connectivity holds for every natural coupling, but the exact value is fixed only by the corpus C\_ZY — condition (a).

### **I.2 The boundary BFV differential (condition b)**

v3.0’s check ‖Ω∂Σ^(0→1) − q\_Z d\_Γ‖ \= 0 was tautological: Ω was set equal to q\_Z d\_Γ. The genuine derivation from abelian BF \+ Maxwell gives ∂(BF constraint)/∂p \= q\_Z d\_Γ (the degree-0→1 block) and a separate Maxwell Gauss constraint d\_Γᵀ E \= 0 on the electric field (degree 1), with ∂(BF)/∂E \= 0 and ∂(Gauss)/∂p \= 0 — no degree-0→1 mixing in the model. Whether the actual ZS-F0 boundary term S\_∂M (GHY \+ Robin n^μ∂\_μΦ \= AΦK) introduces a mixing term must be checked with the explicit S\_∂M — condition (b).

### **I.3 Single normalization and relative modes (condition c)**

The four branching constraints {Π\_c − P\_c p, Π\_b − P\_b p, T\_c − T\_\*, T\_b − T\_\*} have constraint Poisson matrix with det \= 1: all second-class, reducing to the single pair (p, T\_\*) with Θ\_red \= Θ\_\*. The single coefficient ε\_c \= ε\_b follows from the pure Brown–Kuchař Hamiltonian H \= −P\_T; a block-dependent S\_ZS term would break it — condition (c). The 37 relative graph modes satisfy d\_Γ p ≠ 0, so they are removed by **failing the first-class-derived constraint d\_Γ p \= 0 (constraint-exclusion)**; the cellular cohomology is H⁰ \= span{1₃₈}. The stronger “relative modes are BRST-exact gauge modes” reading (v3.0) is not established — it needs the edge-sector ghost complex of the full action. v3.1 claims only constraint-exclusion.

## **References**

\[1\] A. H. Chamseddine and V. Mukhanov, “Mimetic Dark Matter,” J. High Energy Phys. 11, 135 (2013); arXiv:1308.5410.

\[2\] A. H. Chamseddine, V. Mukhanov, and A. Vikman, “Cosmology with Mimetic Matter,” J. Cosmol. Astropart. Phys. 06, 017 (2014); arXiv:1403.3961.

\[3\] S. Dubovsky, L. Hui, A. Nicolis, and D. T. Son, “Effective field theory for hydrodynamics,” Phys. Rev. D 85, 085029 (2012); arXiv:1107.0731.

\[4\] S. Mukohyama, “Dark matter as integration constant in Hořava–Lifshitz gravity,” Phys. Rev. D 80, 064005 (2009); arXiv:0905.3563.

\[5\] J. D. Brown and K. V. Kuchař, “Dust as a standard of space and time in canonical quantum gravity,” Phys. Rev. D 51, 5600 (1995); arXiv:gr-qc/9409001.

\[6\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, “Classical BV theories on manifolds with boundary,” Commun. Math. Phys. 332, 535 (2014); arXiv:1201.0290.

\[7\] A. S. Cattaneo, N. Moshayedi, and K. Wernli, “Globalization for perturbative quantization of nonlinear split AKSZ sigma models on manifolds with boundary,” Commun. Math. Phys. 372, 213 (2019); arXiv:1807.11782. \[mQME\]

\[8\] R. P. Malik, “BRST cohomology and Hodge decomposition theorem in Abelian gauge theory,” Int. J. Mod. Phys. A 15, 1685 (2000); arXiv:hep-th/9808040. \[2D-Abelian special case\]

\[9\] W. Donnelly and L. Freidel, “Local subsystems in gauge theory and gravity,” J. High Energy Phys. 09 (2016) 102; arXiv:1601.04744.

\[10\] C.-P. Ma and E. Bertschinger, “Cosmological perturbation theory in the synchronous and conformal Newtonian gauges,” Astrophys. J. 455, 7 (1995); arXiv:astro-ph/9506072.

\[11\] E. T. Jaynes, “Information theory and statistical mechanics,” Phys. Rev. 106, 620 (1957).

\[12\] A. Connes and C. Rovelli, “Von Neumann algebra automorphisms and time–thermodynamics relation,” Class. Quantum Grav. 11, 2899 (1994); arXiv:gr-qc/9406019.

\[13\] M. Barriola and A. Vilenkin, “Gravitational field of a global monopole,” Phys. Rev. Lett. 63, 341 (1989).

\[14\] A. Vilenkin and E. P. S. Shellard, Cosmic Strings and Other Topological Defects (Cambridge Univ. Press, 1994).

\[15\] E. Witten, “Superconducting strings,” Nucl. Phys. B 249, 557 (1985).

\[16\] R. Jackiw and P. Rossi, “Zero modes of the vortex–fermion system,” Nucl. Phys. B 190, 681 (1981).

\[17\] R. H. Brandenberger, B. Carter, A.-C. Davis, and M. Trodden, “Cosmic vortons and particle physics constraints,” Phys. Rev. D 54, 6059 (1996); arXiv:hep-ph/9605382.

\[18\] B. Carter and A.-C. Davis, “Chiral vortons and cosmological constraints,” Phys. Rev. D 61, 123501 (2000).

\[19\] F. J. Murray and J. von Neumann, “On rings of operators,” Ann. Math. 37, 116 (1936).

\[20\] A. Connes, “Classification of injective factors,” Ann. Math. 104, 73 (1976).

\[21\] Planck Collaboration (N. Aghanim et al.), “Planck 2018 results. VI. Cosmological parameters,” Astron. Astrophys. 641, A6 (2020); arXiv:1807.06209.

\[22\] B. Eckmann, “Harmonische Funktionen und Randwertaufgaben in einem Komplex,” Comment. Math. Helv. 17, 240 (1944–45). \[combinatorial Hodge\]

\[23\] L.-H. Lim, “Hodge Laplacians on graphs,” SIAM Rev. 62, 685 (2020); arXiv:1507.05379.

\[24\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, “Perturbative quantum gauge theories on manifolds with boundary,” Commun. Math. Phys. 357, 631 (2018); arXiv:1507.01221. \[abelian BF, mQME\]

\[25\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, “A cellular topological field theory,” Commun. Math. Phys. 374, 1229 (2020); arXiv:1701.05874. \[cellular BF → condition C1\]

\[26\] S. Weinberg, “Adiabatic modes in cosmology,” Phys. Rev. D 67, 123504 (2003); arXiv:astro-ph/0302326.

\[27\] J.-P. Serre, Linear Representations of Finite Groups (Springer, 1977). \[Schur’s lemma\]

## **Version History**

v1.0 (June 2026): Initial release. Geometric-dust ontology, equivariant boundary-rank–trace theorem, two NO-GO characterizations of the 32-charge; Condition BT-C and O-A19.2–O-A19.5 registered.  
v1.1 (June 2026): Added Theorem A19.NG1; RETRACTED the v1.0 “one theorem closes both”; demoted A19.1 to IMPORTED-PROVEN; corrected pullback pressure p \= F − bF\_b; elevated O-A19.5; P\_BT a candidate; added ε-Halo conflict O-A19.6.  
v1.2 (June 2026): Added §8 BRL-ZCD (XQ−1 seam projector, constrained Z-clock dust, baryon-anchored lock); Theorem A19.4 (h-free ω\_c \= 0.119112, ratio 16/3); AN-A19.2.  
v1.3 (June 2026): Gate-testing revision (CAMB peak, S₃ uniqueness, δ\_c \= δ\_b, i-tetration clock); several conclusions corrected in v1.4.  
v1.4 (June 2026): Added Theorem A19.NG2 (scalar-clock rank-absorption); RETRACTED the v1.3 single-emergence-node claim; downgraded A19.5, BRL-5, BRL-1/2/4; honest gate inventory G1–G8.  
v1.5 (June 2026): Added §10 ZHCS boundary-charge program; reduced G1–G8 to four theorems ZHCS-1–4; rank-ratio PROVEN-CONDITIONAL on ZHCS-1 ∧ ZHCS-2; rank-6 projector by direct sum.  
v2.0 (June 2026): Deep-exploration closure: claimed ZHCS-1 DERIVED (38-node graph connected) and ZHCS-2 DERIVED-CONDITIONAL, raising 32:6 to DERIVED-CONDITIONAL on a single operator identification; added the ZHCS-1 polyhedral computation (60-check suite).  
v2.1 (June 2026): Status correction. Independent recomputation: truncated-octahedron incidence kernel dim 2, six squares mutually non-adjacent, mQME restated; demoted ZHCS-1 → DERIVED-CONDITIONAL, ZHCS-2 → OPEN/HYPOTHESIS-strong; 32:6 \= PROVEN-CONDITIONAL on ZHCS-1∧2∧3; conditional core lifted via Eckmann/Lim; corrected title 32/121 → 32:6; separated third-peak from abundance ratio.  
v2.2 (June 2026): External-theorem closure program. ZHCS-1 repaired via uniform-sector Schur genericity (codim-1 vanishing, 200k-sample MC); ZHCS-2 collapsed to condition C1 (cellular abelian BF, CMR), co-closedness dissolved at degree 0; ZHCS-3 and ZHCS-4 unified under condition C2 (single Brown–Kuchař Z-clock) via Brown–Kuchař \+ Weinberg; physical 32:6 \= DERIVED-CONDITIONAL on C1 ∧ C2; third peak \= DERIVED-CONDITIONAL on C2.  
v2.3 (June 2026): Full integration. Restores all v2.0 content omitted by v2.1/v2.2 (geometric-dust ontology §3–§4, equivariant rank–trace §5, the 32-charge NO-GOs §6, BT-C/A19.NG1 §7, BRL-ZCD §8, the G1–G8 gate testing §9, O-gates §11, the Planck partition §12, BTD closure program §14, Appendices A–B, references \[1\]–\[21\], and the full version history) and integrates them coherently with the v2.1 substrate corrections and the v2.2 external-theorem consolidation, applying the corrected ZHCS statuses uniformly throughout (Table 6, §12, §13). Net result: physical 32:6 DERIVED-CONDITIONAL on C1 ∧ C2; third peak DERIVED-CONDITIONAL on C2; no gate unconditionally DERIVED. Four external PROVEN theorems imported (\[22\]–\[27\]). ZS-A18 frozen; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new fitted parameter.  
v2.4 (June 2026): Conditional-reduction revision answering a review of v2.3. (1) Restored the canonical-branching action S\_branch and symplectic-charge conservation Θ\_c \+ Θ\_b \= Θ\_\* (dropped in v2.3), giving the equal normalization ε\_c \= ε\_b an action-level basis; (2) re-grounded ZHCS-1 cross-support structurally on the corpus rank-1 β₀ mediation (κ² \= A/Q \= 35/4807 ≠ 0, PROVEN), retiring the statistically weak uniform-sector Monte Carlo; (3) split C1 into C1a (physical cube adjacency), C1b (corpus W\_bc ≠ 0), C1c (cellular-abelian-BF seam), and C2 into C2-norm (single-coefficient parent Hamiltonian H \= ε\_\* p) and C2-branch (S\_branch from ZS-F0); (4) made the equal-Hamiltonian-normalization condition explicit and proved ε\_c \= ε\_b follows from it (Appendix F); (5) corrected ZHCS-4 to PROVEN-CONDITIONAL on C2 \+ no-independent-entropy / adiabatic selection (Weinberg gives existence, not occupation), narrowing the co-moving identification to the branching hypersurface to remove the conflict with baryon acoustic physics; (6) corrected the third peak to COMPUTED-CONDITIONAL on C1 ∧ C2 ∧ adiabatic selection ∧ standard transfer (not C2 alone); (7) reclassified “external-theorem closure” as “external-theorem conditional reduction”; (8) added Appendix E (verification provenance: RETAINED / SUPERSEDED / RECOMPUTED / NEW) and Appendix F (explicit C1/C2 computation). No gate reaches unconditional DERIVED; C1c, C2-norm, C2-branch, and adiabatic occupation remain physical identifications. ZS-A18 frozen; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new fitted parameter.  
v3.0 (June 2026): Closure revision. Carried out the two decisive action-level computations of the v2.4 review. (C1) Dualized the corpus S10 Stückelberg U(1) to a 2-form–1-form BF coupling q\_Z ∫ B∧F\_Y (C1-A, symbolic); computed the actual rank-1 β₀ cross-transfer W\_bc \= κ² k₀ |r\_b⟩⟨r\_c| with all 6×32 entries nonzero, giving a connected physical 38-node graph (TI adjacency \+ six isolated squares \+ actual cross-edges, rank L\_Γ \= 37\) with the cube rewiring ELIMINATED (C1-B); and showed the boundary BFV differential Ω∂Σ^(0→1) \= q\_Z d\_Γ (C1-C) — raising C1 to DERIVED. (C2) Performed the Brown–Kuchař ADM reduction giving P\_T \= −H\_ZS, the canonical branching with Θ\_c \+ Θ\_b \= Θ\_\* and node-uniform ε\_c \= ε\_b without separate assumption (C2-E), vanishing intrinsic entropy transfer S\_cb \= S\_cγ \= 0 (C2-A), post-branching separation (C2-D), and BRST-exactness of the 37 relative modes (H⁰\_phys \= span{1₃₈}) — raising C2 to DERIVED-CONDITIONAL on a single source. Added Theorem A19.ZHCS-Closure (PROVEN-CONDITIONAL on C1 ∧ C2): ρ\_c/ρ\_b \= 32/6, w\_c \= c\_s² \= 0, S\_cb \= S\_cγ \= 0, standard passive CDM transfer, ω\_c \= 0.119112 — all DERIVED-CONDITIONAL on a single source. Added Appendices G–H (C1/C2 closure computations) and the script zs\_a19\_c1c2\_closure.py. All v2.4 content retained; the only residuals are the single-source condition (C2-A) and the cellular-discretization exactness (C1-C). ZS-A18 frozen; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new fitted parameter.  
v3.1 (June 2026): Status-correction revision; no new physics or fitted parameters, all v3.0 content retained. A second review showed v3.0’s closure over-stated three steps. (1) C1-B used an idealized intertwiner: F\_TI carries the trivial representation with multiplicity two, so the cross-overlap ⟨r\_Y | 1₃₂⟩ is corpus-dependent (vanishing only on a single ray that every corpus-natural candidate avoids — uniform → 32, Lemma-4.5 (−2,1) → −4) — reduced to condition (a). (2) C1-C’s ‖Ω∂Σ^(0→1) − q\_Z d\_Γ‖ \= 0 was tautological; the BF term genuinely gives q\_Z d\_Γ with Maxwell a separate degree-1 Gauss constraint, but sector-non-mixing of the ZS-F0 boundary term S\_∂M is condition (b). (3) C2-E’s ε\_c \= ε\_b holds for the pure Brown–Kuchař Hamiltonian (branching constraints second-class, det \= 1, reduced pair (p, T\_\*)) but is conditional on S\_ZS being block-independent — condition (c); the 37 relative modes are constraint-excluded (d\_Γ p ≠ 0), not proven gauge-exact. Accordingly C1 is reset to DERIVED-CONDITIONAL on (a) ∧ (b), C2 to DERIVED-CONDITIONAL on (c) \+ a single source, and the 32:6 ratio and ω\_c \= 0.119112 to DERIVED-CONDITIONAL on (a) ∧ (b) ∧ (c) \+ single source. Added Appendix I (Open Derivations, Table I1) registering (a)–(c) with falsification conditions; annotated verification checks 17–18 as idealized-substrate (corpus closure pending (a)/(b)); reclassified the program from “closed” to “conditional reduction.” C1-A (Stückelberg→BF dual) remains DERIVED. ZS-A18 frozen; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new fitted parameter.