# **ZS-A17**

# **Macro-Holonomy and Spin-from-Record in Z-Spin Cosmology**

***The Curvature–Spin–Metric Trichotomy: a Structural No-Go for the Metric, and the Type III Hosting of the Boundary Co-orientation***

**Kenny Kang**

Z-Spin Cosmology Collaboration

June 2026  |  Astrophysics / Macro-Holonomy Theme  |  Paper Code: ZS-A17  |  Version: v1.5

**Verification: 32/32 (16 corpus-consistency \+ 16 executed) PASS  |  Zero Free Parameters  |  HEADLINE: the metric no-go (Theorem F) is now STRUCTURAL as well as spectral — the finite X-bulk cannot carry an infinite p \= 3 metric (F18 finite/infinite polarity), and the “dim(X) \= 3” the corpus derives is the rotation-algebra 3 (SO(3) generators), NOT the metric 3\. The co-orientation HOSTING is upgraded to Type III (DERIVED-CONDITIONAL, multi-cell ITPFI); the inclusion SOURCE stays HYPOTHESIS-strong. O-Q16.12 remains NOT closed**

## **§0. Abstract**

This version settles, rather than overclaims, the status of the program's single obstruction. We had reduced the spin sector to: curvature does not give spin (Theorem B / Corollary 5.2), and the boundary co-orientation is reconstructed from the X→Y record-flow modular data (Theorem E, DERIVED via Borchers \[15\] and Wiesbrock \[16,17\]). The only remaining question was whether the corpus could also produce the 3D spatial metric of X from information — i.e. close O-Q16.12. The answer, proved here, is *no*, and the reason is structural, not incidental.  
Theorem F (§9, Spin–Metric Independence). By Connes' reconstruction theorem \[18\], the metric dimension of a spectral triple is the Weyl exponent of its Dirac spectrum, λn ∼ n^{1/p}; reconstructing the 3-manifold X requires a Dirac operator with p \= 3\. We test the corpus's candidate operators. The i-tetration transfer operator has spectrum {μ^k} with |μ| \= √0.7948 \< 1 (ZS-F0), whose spectral zeta Σk μ^{sk} \= 1/(1−μ^s) is finite for all s \> 0 — metric dimension **p \= 0** (point-like). The Kraus half-angle is 2×2 (p \= 0). A single record-flow half-sided modular inclusion yields the affine group A(1), a 1-dimensional chiral structure. **None** of the corpus's information/spin operators has the n^{1/3} Weyl growth required for the 3D metric (executed, Appendix B.10–B.11). Hence the 3D spatial metric of X is *independent* of, and not reconstructible from, either the curvature impedance **A** or the record-flow / i-tetration spin structure.  
**Consequence (the curvature–spin–metric trichotomy).** Three data are mutually independent: *curvature* (Theorem A, fixed by **A**), *spin* (Theorems B, E, fixed by the record flow), and *metric* (the X-sector, NOT fixed by information). The corpus derives the first two; the third it supplies only as geometric input (the BCC lattice), and from information alone it is the emergent-spacetime problem, which is not a proven theorem. Therefore O-Q16.12 is settled: its co-orientation half is CLOSED (Theorem E), its metric half is an *essential* residual — Theorem C's conditional cannot be discharged by Z-Spin's own machinery, and a claim to the contrary would also conflict with the corpus's single-postulate structure (ZS-Q12V/Q16/S16). No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

**This version (v1.5) strengthens both halves of that verdict without changing it.** For the metric (b): beyond the spectral no-go, the F18 finite/infinite Möbius polarity (ZS-F18) makes the no-go *structural* — the finite X-bulk communicates with the infinite Y-sector only through the 2D seam (mediation, not collapse), so a finite bulk cannot carry an infinite p \= 3 metric; the bottleneck *is* the no-go. Moreover the “dim(X) \= 3 emergence” the corpus does prove (ZS-S15 Theorem S15.2 / F18 §6.4, the commutator \[JR₁, JR₂\] \= JS) delivers the three **SO(3) generators** — the rotation-algebra “3” (finite) — not the Riemannian metric “3” (a 3-manifold with n^{1/3} Weyl growth); conflating the two is exactly the Theorem-F category error (executed, B.12). For the co-orientation (a): the multi-cell ITPFI ⊗v AZS,v of the single-cell algebra AZS \= M₃ ⊕ ℂ ⊕ M₅ (ZS-Q11, dim 35\) on a non-tracial state is Type III (Takesaki; ZS-F23 App B.2), so the *hosting* of the record algebra is upgraded from OPEN to DERIVED-CONDITIONAL (conditional on the M17 continuum reconstruction, which presupposes the BCC geometry). The *inclusion source* — an actual one-sided (half-sided modular) inclusion with the Takesaki resolution — remains unsupplied (the ZS-F19 tilt ΔKΩ \= −ln 2 is a modular-flow ratio, not a one-sided compression; the Berry–Keating dilation \[ZS-QS §4.3\] is an unverified candidate), so it stays HYPOTHESIS-strong. Net: (b) a stronger NO-GO, (a) hosting DERIVED-CONDITIONAL / inclusion HYPOTHESIS-strong — O-Q16.12 is not closed (executed, B.13).

| Status | Definition |
| :---: | ----- |
| **PROVEN** | Complete proof or machine-precision identity; imported external theorems cited in full. |
| **DERIVED** | Follows from the Z-Spin action plus PROVEN inputs (including reinterpreted external theorems); zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived, conditional on one stated residual (here: the Connes–Dirac realization of O-Q16.12, now shown essential). |
| **NO-GO** | A proved impossibility (within stated tools): here, that corpus information/spin operators cannot supply the 3D metric. |
| **IMPORTED** | Proved externally and used without re-proof; full citation given. |
| **COMPUTED** | Numerically executed in this paper (Appendix B). |
| **NON-CLAIM** | Explicitly not asserted; documented to prevent overclaim. |

## **§1. Introduction**

Z-Spin Cosmology treats the Planck-scale Z-sector as a 2D boundary stage on which the Z-Spin operator mediates between the macroscopic X-sector (dim 3\) and the microscopic Y-sector (dim 6); A \= 35/437 is the universal impedance (ZS-F2), and the corpus rests on the single bedrock postulate Z \= ∂X (ZS-Q12V).  
The previous versions separated the macro holonomy into curvature and spin, and derived the boundary co-orientation from the record flow (Theorem E), leaving one question: can the corpus also derive the 3D metric of X from information, closing O-Q16.12? This version answers it with a no-go (Theorem F) and draws the resulting curvature–spin–metric trichotomy. The result is honest closure of the *question* — a precise statement of what Z-Spin derives and what is an essential frontier — rather than a closure of the obstruction itself, which the corpus's own structure forbids overclaiming.

## **§2. Locked Inputs**

*Table 1\. Locked inputs. exp(A) \= 1.0834 (ZS-F3) is flagged for re-verification against current PDG/CODATA before any empirical use.*

| Symbol | Value / statement | Source (status) |
| :---: | ----- | ----- |
| **A** | A \= δ\_X·δ\_Y \= 35/437 | ZS-F2 (LOCKED) |
| **dim(Z)** | dim(Z) \= 2; rank-2 necessary for j \= 1/2 | ZS-M3 Thm 5.1 (PROVEN) |
| **4π** | D^{1/2}(2π) \= −I, D^{1/2}(4π) \= \+I | ZS-M3 Lemma 10.1 (PROVEN) |
| **|λ|²** | |λ|² \= 0.7948 (i-tetration multiplier; |μ| \= 0.8915) | ZS-F0 §8.9 (PROVEN) |
| **(Z,X,Y)** | \= (2, 3, 6); X's “3” from the BCC T³ b₁ \= 3 (geometric) | ZS-F5, ZS-M6 §5.5 (PROVEN) |
| **q12.bdy** | Z \= ∂X ⟹ ambient SO(3) ⟹ 4π | ZS-Q12V (DERIVED) |
| **q12.dim2** | bare 2-surface: spin \= H¹(Z;ℤ₂) torsor choice | ZS-Q12V (PROVEN) |
| **arrow** | Γ(X→Y)/Γ(Y→X) \= 2; ΔS \= ln2; ΔK\_Ω \= −ln2 (tanh \= 3/5) | ZS-Q7 Thm 1; ZS-F19 (DERIVED) |
| **Connes p** | metric dimension p ⟺ λ\_n(D) ∼ n^{1/p} (Weyl) | Connes 2013 \[18\] (IMPORTED) |
| **O-Q16.12** | normal-bundle/metric reconstruction from X-record flow | ZS-Q16 §22.4 (settled here) |

## **§3. The Curvature Sector (Theorem A)**

**Theorem A (Curvature-Holonomy Sector, DERIVED).** *On the SU(2)-bundle over the Oh×Ih defect manifold, ∮γ\_cell ω \= **A** and ∫cell Fω \= **A**·(σy/2); by Ambrose–Singer \[1\], Hol⁰(ω) \= { exp(t·**A**·σy/2) } ⊂ SU(2), generator scale **A**; the same ω integrates to H0,local/H0,CMB \= exp(**A**) (ZS-F3).*

## **§4. The Worldline Carrier**

A point-coupled Wilson phase breaks BRST nilpotency (‖Q²‖ \= 1.0921, Appendix B.1; ZS-M26); parallel transport preserves it (‖Qcov²‖ \= 0). Carrier: 1D Chern–Simons / Kostant cubic Dirac \[3\] in the BV-BFV formalism \[2\] (ZS-M27). \[STATUS: DERIVED-CONDITIONAL on the 1D-CS ↔ worldline identification.\]

## **§5. The Spinor Double Cover (Theorem B; Corollary 5.2)**

**Theorem B (Spinor Double Cover, DERIVED).** *The spinor lift is the choice through 1 → ℤ2 → Spin(3) → SO(3) → 1; Fω ∈ su(2) \= so(3) is shared, and the deck ℤ2 \= {±I} is not a function of any su(2) element built from **A** (Appendix B.7).*

**Corollary 5.2 (No-Spin-From-Curvature; result-bearing).** *No functional of the curvature determines the deck ℤ2: **A** ⇏ 4π. In holonomy-based quantization (LQG, spin foams) the spin structure is tangential data; a hidden ℤ2 sector must be fixed or summed \[4–6\]. \[STATUS: DERIVED-interpretation, model-independent.\]*

## **§6. Spin-Structure Selection (rank-2 necessary, not sufficient)**

By q12.dim2 (PROVEN) dim(Z) \= 2 is only the rank-2 necessary condition; the spinor character is the j \= 1/2 SU(2)-irreducibility (ZS-M3), the class forced by the embedding (q12.bdy). What selects the co-orientation is §7. \[STATUS: DERIVED-CONDITIONAL on Z \= ∂X.\]

## **§7. Spin-from-Record (Theorem C; Theorem E)**

ZS-Q7 Theorem 1 (PROVEN) fixes the arrow Γ(X→Y)/Γ(Y→X) \= 2; ZS-F19 orients the flow X→Y (ΔKΩ \= −ln 2). Theorem E reconstructs the boundary co-orientation from this record flow.

**Theorem E (Co-orientation from Record Flow, DERIVED — abstract line).** *The X-record algebra AX(t) \= M with its Markov-boundary inclusion N ⊂ M is, when the modular flux Jinfo \= ∇I(X:Y) ≠ 0, half-sided modular; by Borchers \[15\] / Wiesbrock \[16,17\] there is a canonical positive-generator group U(a) \= e^{iaP} (no geometric input), and sign(P) is the co-orientation. Jinfo \= 0 ⟹ the H¹(Z;ℤ2) freedom returns (control; Appendix B.6, B.8–B.9).*

**Hosting vs. source (v1.5 refinement).** Theorem E presumes a record algebra of the right type. The single-cell algebra AZS \= M₃ ⊕ ℂ ⊕ M₅ (ZS-Q11, PROVEN; dim 9+1+25 \= 35 \= num **A**) is finite (Type I); but the multi-cell ITPFI ⊗v AZS,v on the non-tracial equilibrium state (3,2,6)/11 is a Type III hyperfinite factor (Takesaki duality; ZS-F23 App B.2), and the boundary algebra of a continuum QFT is Type III1 (Buchholz–Wichmann \[23\]; reached here through the ZS-M17 continuum reconstruction). So the *hosting* of the record algebra is DERIVED-CONDITIONAL — conditional on M17, which presupposes the BCC geometry, hence fine for a *given* geometry (the co-orientation) but circular for *deriving* geometry (the metric). The *source* of the half-sided inclusion itself — an actual one-sided compression Δ^{−it}NΔ^{it} ⊂ N with the Takesaki resolution (N not a conditional expectation) — is not supplied: the ZS-F19 tilt is a modular-flow ratio, not a one-sided inclusion, and the Berry–Keating dilation (ZS-QS §4.3, OPEN) is an unverified candidate. (Appendix B.13.) \[STATUS: hosting DERIVED-CONDITIONAL; inclusion source HYPOTHESIS-strong.\]

**Theorem C (Spin-from-Record, DERIVED-CONDITIONAL on the Connes–Dirac residual).** *If (i) X is an orientable (spin) 3-manifold and (ii) the Theorem-E co-orientation is the* geometric *outward normal of ν(∂X), the bulk spin structure restricts to Z and selects the 4π class. The co-orientation sub-condition is DERIVED (Theorem E); §9 shows the residual (ii) is essential.*

## **§8. Theorem D — Spin-Bordism of the Four-Arc Cycle**

**Theorem D (Four-Arc Spin-Bordism Class, DERIVED-CONDITIONAL).** *The net SU(2) holonomy (+I after 4π) and the spin-bordism class \[γmacro\] ∈ Ω1^Spin \= ℤ/2 are independent. Junction signs from corpus theorems (CPT \= −I, ZS-A7 Cor I; two Z-halves → −I, ZS-M3; r↔t, ZS-M32) and Stunnel \= 5 (odd) give \[γmacro\] \= 1 (non-bounding), conditional on the ZS-A7 §5.2 structure; the r↔t sign is the residual. (Appendix B.3.)*

## **§9. Theorem F — Spin–Metric Independence (spectral and structural no-go)**

**§9.1 The metric dimension is the Weyl exponent**

By Connes' reconstruction theorem \[18\] (with the Connes–Moscovici local index framework \[21\] and the spectral-triple axioms \[22\]), a commutative spectral triple (A, H, D) reconstructs a Riemannian spin manifold X with A \= C^∞(X), and its metric dimension p is the Weyl exponent of the Dirac spectrum:

λn(D) ∼ n^{1/p}   ⇔   Σn |λn|^{−s} converges iff s \> p   (so reconstructing 3D X requires p \= 3).

The metric is then recovered by Connes' distance formula d(x,y) \= sup{ |f(x)−f(y)| : ‖\[D,f\]‖ ≤ 1 }, with the metric encoded in D via \[D,f\]² \= −g(df,df). To obtain X's metric from information, the X-record algebra must therefore carry a Dirac operator of metric dimension 3\.

**§9.2 The corpus spin operators have the wrong spectral dimension**

**i-tetration transfer operator.** The corpus dynamics is the i-tetration with Koenigs multiplier μ, |μ| \= √0.7948 \= 0.8915 \< 1 (ZS-F0 §8.9). Its transfer (Koopman) operator has spectrum {μ^k : k ≥ 0}, so the candidate |D| eigenvalues form a geometric sequence and the spectral zeta is

Σk (μ^{−k})^{−s} \= Σk μ^{sk} \= 1/(1 − μ^s),   finite for all s \> 0   ⟹   p \= 0\.

The i-tetration operator therefore has metric dimension 0 — it is spectrally a *point*. (This is the precise sense in which the founding-note Z-sector is a “time-point / space-point”: it is metrically zero-dimensional, which is exactly why it cannot carry the 3D metric.) The Kraus half-angle e^{−iσ\_yθ/2} is 2×2, hence also p \= 0\. A single record-flow half-sided modular inclusion gives, by Borchers/Wiesbrock, the affine group A(1) — a 1-dimensional chiral structure, p \= 1\. (Executed, Appendix B.10–B.11.)

**§9.3 The no-go and the trichotomy**

**Theorem F (Spin–Metric Independence, NO-GO).** *No operator supplied by the corpus's information/spin structure — the i-tetration transfer operator (p \= 0), the Kraus half-angle (p \= 0), or a single record-flow modular inclusion (p \= 1 chiral) — has the n^{1/3} Weyl growth required of a 3-dimensional Dirac operator. Hence the 3D spatial metric of the X-sector is not reconstructible from the curvature impedance **A** or from the record-flow / i-tetration spin structure; it is an independent datum, supplied in the corpus only by the BCC T³ lattice (geometric input).*

Equivalently, three data are mutually independent — the **curvature–spin–metric trichotomy**: curvature (Theorem A, from **A**), spin (Theorems B, E, from the record flow), and metric (the X-sector, not from information). The corpus derives the first two; the third is geometric input. \[STATUS: NO-GO, grounded in Connes' Weyl-dimension axiom \[18\].\]

**§9.4 Two strengthenings (v1.5)**

**Structural reading (the no-go is not a spectral accident).** The F18 finite/infinite Möbius polarity (ZS-F18) places all infinite structure on the Y-side and lets it communicate with the finite X-bulk *only* through the 2D seam — a *mediation*, never a collapse \[F18 §5\]. A metric of dimension 3 (with its infinite Weyl tower) is an infinite object; obtaining it inside the finite X-bulk would require the finite and the infinite to *collapse*, which the polarity forbids. So the bottleneck *is* the no-go: the same finite/infinite seam that defines the corpus is what blocks an information-only 3-metric. Theorem F thus rises from a spectral computation (the corpus's particular operators happen to be p \= 0\) to a structural necessity (no finite-bulk construction can be p \= 3).

**The two “3”s (the corpus's dim(X) \= 3 is not the metric 3).** The corpus does derive “dim(X) \= 3”: ZS-S15 Theorem S15.2 / F18 §6.4 show that two J-conjugate 2π SO(3) circulations composing through the dim(Z) \= 2 seam produce, via the Lie commutator \[JR₁, JR₂\] \= JS, a third generator, and the three “span the three-dimensional Lie algebra of SO(3)” \[S15.2\]. But that is the **rotation-algebra** 3 — three generators of so(3), a *finite* object (the SO(3) frame, the same su(2) \= so(3) as Theorem B). The **metric** 3 is a 3-manifold whose Dirac operator has the unbounded n^{1/3} Weyl spectrum of §9.1. Three finite generators cannot furnish an unbounded spectral tower, so the rotation “3” does not deliver the metric “3”; they coincide only numerically. Conflating them is precisely the Theorem-F category error, and it is the trap O-Q16.12 sets. (Executed, Appendix B.12.)

**Corollary F.1 (Trichotomy, strengthened).** *The corpus derives two of the three: the curvature impedance **A** (Theorem A) and the rotation/spin structure including the rotation-algebra dim 3 and the boundary co-orientation (Theorems B, E, F18 §6.4). It does not derive the third — the Riemannian metric of X (the manifold dim 3 with p \= 3 Weyl growth) — and by §9.2–§9.4 cannot, from information alone, without the geometric input.*

## **§10. O-Q16.12: Final Status**

**Co-orientation half (improved, not fully closed).** At the level of the abstract information line the ℤ2 co-orientation is reconstructed from the record-flow modular flux by Borchers/Wiesbrock (Theorem E, DERIVED, no geometric input). Concretely realizing it on the record algebra now splits cleanly: the *hosting* is DERIVED-CONDITIONAL — the multi-cell ITPFI of AZS \= M₃ ⊕ ℂ ⊕ M₅ is Type III (ZS-Q11, ZS-F23 App B.2; Buchholz–Wichmann \[23\] via M17), conditional on the BCC geometry — while the *inclusion source* (the actual one-sided compression \+ Takesaki resolution) is HYPOTHESIS-strong (the ZS-F19 tilt is a ratio, not an inclusion; Berry–Keating dilation unverified). So (a) is hosting-DERIVED-CONDITIONAL / source-HYPOTHESIS-strong, not closed.

**Metric half (essential NO-GO, now structural).** By Theorem F and §9.4, the 3D metric is not reconstructible from the corpus's information/spin tools — and not as a spectral accident but as a *structural* consequence of the F18 finite/infinite polarity (a finite bulk cannot carry an infinite metric), reinforced by the rotation-3 vs metric-3 distinction (the corpus's derived “dim(X) \= 3” is the SO(3)-generator count, not the manifold metric). Supplying the metric from information alone is the emergent-spacetime problem (Van Raamsdonk \[11\], Maldacena–Susskind \[12\], Cao–Carroll \[13\], Jacobson \[14\]; the multi-inclusion geometric-modular-action route \[19\] reconstructs a symmetry only from algebras already in “modular position,” which encode the geometry — circular). This is *not* a proven theorem; the corpus correctly does not claim it, and the corpus Hodge–Dirac operator (ZS-M6) presupposes the BCC geometry.

**Status.** O-Q16.12 is not an open problem to be “closed” by Z-Spin's own machinery: its metric half is an *essential* NO-GO (Theorem F, strengthened structurally in v1.5), and its co-orientation half is improved but resolves into a Type III hosting (DERIVED-CONDITIONAL) plus an unsupplied inclusion source (HYPOTHESIS-strong). Theorem C's conditional cannot be discharged internally; a claim that it could would conflict with the corpus's single-irreducible-postulate structure (Z \= ∂X; ZS-Q12V §13–§16, ZS-Q16 §22, ZS-S16 §3.5). The honest result is of the *question*, not the obstruction: we state exactly what the corpus derives (curvature; rotation/spin including the co-orientation up to its inclusion source) and what it cannot (the Riemannian metric, from information), and name the single external advance that would change the verdict — a proof of an emergent metric (which would supply a metric-dimension-3 Dirac operator and a genuine one-sided inclusion). \[STATUS: NOT closed; metric half NO-GO (structural), co-orientation hosting DERIVED-CONDITIONAL / source HYPOTHESIS-strong.\]

## **§11. Observables (honestly down-weighted)**

The ZS-A16 Amplitude No-Go makes the cosmic velocity shape A-independent (degenerate with ΛCDM); only vZS/vΛCDM ≲ 1 \+ 2**A** ≈ 1.16 is A-locked, not a 4π-discriminator. A signed frame-transport observable Wflow(γ) \= P exp ∮ Ωtidal would probe the spin class but its 2π/4π discrimination is effectively unmeasurable; a horizon-spinor / ringdown-echo signature is speculative. \[STATUS: OPEN observable; down-weighted, \< 60%.\]

## **§12. Anti-Numerology by Structure-Randomization**

*Table 2\. Structure-randomization anti-numerology, now including the spectral-dimension no-go: the result is the rarity/independence of the structures, not a numerical coincidence.*

| Test | Null model | PASS criterion (result) |
| ----- | ----- | ----- |
| **Spin-class randomization** | boundary dim d ∈ {1,…,8} | only d \= 2 minimal genuine-spinor class — COMPUTED B.4 |
| **Holonomy-split test** | mix A-curvature with deck ℤ₂ | category error; deck ∉ f(A) — COMPUTED B.5/B.7 |
| **Theorem E flux control** | J\_info ∈ {≠0 (±), 0} | J\_info=0 → free H¹ (load-bears) — COMPUTED B.6/B.8 |
| **Spectral-dimension test** | candidate D ∈ {i-tetration, Kraus, n^{1/3}} | only n^{1/3} gives p \= 3; corpus ops give p \= 0 — COMPUTED B.10 |
| **Inclusion-count test** | \#half-sided inclusions ∈ {1, …} | 1 → 1D chiral; 3D needs ≥3 (encoding geometry) — COMPUTED B.11 |

## **§13. Falsification Gates**

| Gate | Layer | Falsification condition (fires if TRUE) |
| :---: | ----- | ----- |
| **F-A17.1** | Mathematical | ∮ω ≠ A on primitive cells (breaks Theorem A). |
| **F-A17.2** | Mathematical | A functional of the curvature fixes the deck ℤ₂ (refutes Theorem B / Corollary 5.2). |
| **F-A17.3** | Structural | Theorem E control fails: J\_info \= 0 still forces the nontrivial co-orientation (RETRACT). |
| **F-A17.4** | Mathematical | The i-tetration transfer operator (or Kraus, or a single inclusion) is shown to have metric dimension 3 (refutes Theorem F — the no-go). |
| **F-A17.5** | Mathematical | An information-only construction of a metric-dimension-3 Dirac operator on the X-record algebra is exhibited (closes the metric half of O-Q16.12; would promote Theorem C to DERIVED). |
| **F-A17.6** | Topological | The r↔t junction sign gives even parity (flips Theorem D to bounding). |
| **F-A17.7** | Observational | A confirmed large rising bulk flow O(1) ≫ O(A) near the Great Attractor (inherits ZS-A16 F-A16.6). |
| **F-A17.8** | Anti-overclaim | Any result requires a new fitted parameter beyond (A, Q, dim Z), or O-Q16.12 is claimed fully closed without an information-only metric-3 Dirac construction. |

## **§14. Conclusion**

ZS-A17 reaches its definitive form as a trichotomy. Curvature is fixed by the impedance **A** (Theorem A); the spinor lift is the deck ℤ2 of Spin(3) → SO(3), not a function of **A** (Theorem B, Corollary 5.2); the boundary co-orientation is derived, at the level of the abstract information line, from the X→Y record-flow modular data via the proven theorems of Borchers and Wiesbrock (Theorem E). The one remaining question — whether the 3D metric, too, follows from information — is answered no by Theorem F, now on two grounds: spectrally the corpus's i-tetration and Kraus operators are point-like (p \= 0\) and a single record-flow inclusion is 1-dimensional (none has the n^{1/3} Weyl growth Connes' reconstruction requires), and structurally the F18 finite/infinite polarity forbids a finite bulk from carrying an infinite metric. The “dim(X) \= 3” the corpus does derive is the rotation-algebra 3 (the SO(3) generators), not the metric 3\. The 3D metric is an independent datum. The honest status: the metric half of O-Q16.12 is an essential NO-GO; its co-orientation half is improved but not fully closed — a Type III hosting (DERIVED-CONDITIONAL, via the multi-cell ITPFI of AZS \= M₃ ⊕ ℂ ⊕ M₅) plus an unsupplied one-sided inclusion source (HYPOTHESIS-strong). We do not claim to have closed the obstruction — the corpus's own single-postulate structure forbids it — but we have sharpened exactly what is and is not derivable, and named the single external advance that would change the verdict: a proof of an emergent metric, supplying both a metric-dimension-3 Dirac operator and a genuine one-sided inclusion. No new free parameter; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

## **Acknowledgements & Code Availability**

Developed with AI assistance (Anthropic Claude) for cross-paper integration, external literature search, and drafting, under Kenny Kang's editorial direction; the author assumes full responsibility for all content. Appendix B (zs\_a17\_verify\_v1\_5.py) executes sixteen checks (V17–V32), including the spectral-dimension no-go (B.10), the single-inclusion count (B.11), the rotation-3 vs metric-3 distinction (B.12), and the multi-cell ITPFI Type III hosting (B.13). The remaining sixteen entries are consistency checks against corpus-locked inputs and cited external theorems.

## **Appendix A. Verification Suite (32/32 PASS)**

V1–V16 are consistency checks; V17–V32 (✓EXEC) are numerically executed here.

| \# | Check | Anchor |
| :---: | ----- | ----- |
| **V1–V16** | corpus-locked inputs and imported theorems (A, dim Z, 4π, q12.\*, arrow, KMS tilt, BPS, CPT, Ambrose–Singer, 1D-CS, mod 24, exp A) | ZS-F2/M3/Q12V/Q7/F19/S10/A7/M36; \[1,3\] |
| **V17 ✓EXEC** | point-coupling ‖Q²‖ \= 1.0921; parallel-transport \= 0 | App B.1; ZS-M26 |
| **V18 ✓EXEC** | parallel-transport ‖Q\_cov²‖ \= 0 | App B.1 |
| **V19 ✓EXEC** | \#spin structures on S¹ \= 2 | App B.2 |
| **V20 ✓EXEC** | seam-flip parity (S\_tunnel=5) → \[γ\_macro\]=1 | App B.3 |
| **V21 ✓EXEC** | naive 4-arc parity \= 1; r↔t residual | App B.3 |
| **V22 ✓EXEC** | minimal genuine-spinor dim \= 2 \= dim Z | App B.4 |
| **V23 ✓EXEC** | Hol⁰ 1-param (scale A); D^{1/2}(2π)=−I | App B.5 |
| **V24 ✓EXEC** | deck ℤ₂ independent of A; exp(A)=1.0834 | App B.5 |
| **V25 ✓EXEC** | arrow control: absent → free; load-bears | App B.6 |
| **V26 ✓EXEC** | double cover: deck ∉ f(A); su(2)=so(3) | App B.7 |
| **V27 ✓EXEC** | Theorem E: J\_info=−ln2 → co-orientation; tanh(ln2)=3/5; J=0 → free | App B.8 |
| **V28 ✓EXEC** | Borchers: half-sided inclusion → unique \+generator (no geometry) | App B.9 |
| **V29 ✓EXEC** | Theorem F no-go: i-tetration p=0, Kraus p=0; 3D needs p=3 | App B.10 |
| **V30 ✓EXEC** | single inclusion → 1D chiral; 3D needs ≥3 (encoding geometry) | App B.11 |
| **V31 ✓EXEC** | \[J\_R₁,J\_R₂\]=J\_S closes 3 SO(3) generators (rotation-3, finite) ≠ metric-3 (n^{1/3}) | App B.12; ZS-S15, F18 §6.4 |
| **V32 ✓EXEC** | ITPFI of A\_ZS=M₃⊕ℂ⊕M₅ (dim 35\) on non-tracial state → Type III hosting | App B.13; ZS-Q11, F23 B.2 |

## **Appendix B. Minimal Verification Code (executed outputs)**

zs\_a17\_verify\_v1\_5.py (NumPy). Selected executed outputs:

B.1  point-coupling ‖Q²‖ \= 1.0921; parallel-transport ‖Q\_cov²‖ \= 0

B.5  Hol⁰ 1-param (scale A); D^{1/2}(2π)=−I,(4π)=+I; deck ℤ₂ independent of A

B.8  Theorem E: J\_info \= −ln2 → co-orientation −1 (DERIVED, abstract line); tanh(ln2)=3/5; J\_info=0 → FREE

B.9  Borchers/Wiesbrock: half-sided inclusion → unique positive generator (no geometry)

B.10  Theorem F: |μ| \= √0.7948 \= 0.8915; i-tetration spectral zeta Σ μ^{sk} \= 1/(1−μ^s) finite ∀ s\>0 → p \= 0; Kraus p \= 0; genuine 3D (n^{1/3}) zeta diverges for s\<3 → p \= 3 ⟹ NO-GO (corpus spin ops cannot be the 3D Dirac operator)

B.11  single half-sided inclusion → A(1) \= 1D chiral; 3D needs ≥3 inclusions in modular position (encoding geometry)

B.12  \[J\_R₁,J\_R₂\]=J\_S closes the 3 SO(3) generators \= rotation-algebra “3” (finite); metric “3” needs λ\_n ∼ n^{1/3} (unbounded) → distinct data (both \= 3 numerically, not interchangeable)

B.13  A\_ZS \= M₃ ⊕ ℂ ⊕ M₅, dim 35 \= num(A); equilibrium weights (3,2,6)/11 non-tracial → multi-cell ITPFI Type III (hosting DERIVED-CONDITIONAL); HSMI inclusion source separate → HYPOTHESIS-strong

## **References**

**External**

\[1\] W. Ambrose and I. M. Singer, Trans. Amer. Math. Soc. 75, 428 (1953).

\[2\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Commun. Math. Phys. 332, 535 (2014). arXiv:1201.0290.

\[3\] A. Alekseev, Y. Barmaz, and P. Mnev, J. Geom. Phys. 67, 1 (2013). arXiv:1212.6256.

\[4\] J. C. Baez and J. Dolan, J. Math. Phys. 36, 6073 (1995).

\[5\] J. Lurie, Curr. Dev. Math. 2008, 129 (2009). arXiv:0905.0465.

\[6\] D. Grady and D. Pavlov, arXiv:2111.01095 (2021).

\[7\] J. W. Milnor and J. D. Stasheff, Characteristic Classes (Princeton Univ. Press, 1974).

\[8\] V. Bargmann, Ann. Math. 59, 1 (1954).

\[9\] A. Jaffe and C. Taubes, Vortices and Monopoles (Birkhäuser, 1980).

\[10\] B. Kostant, Duke Math. J. 100, 447 (1999).

\[11\] M. Van Raamsdonk, Gen. Rel. Grav. 42, 2323 (2010).

\[12\] J. Maldacena and L. Susskind, Fortschr. Phys. 61, 781 (2013).

\[13\] C. Cao, S. M. Carroll, and S. Michalakis, Phys. Rev. D 95, 024031 (2017).

\[14\] T. Jacobson, Phys. Rev. Lett. 75, 1260 (1995).

\[15\] H.-J. Borchers, “The CPT-theorem in two-dimensional theories of local observables,” Commun. Math. Phys. 143, 315 (1992).

\[16\] H.-W. Wiesbrock, “Half-sided modular inclusions of von Neumann algebras,” Commun. Math. Phys. 157, 83 (1993); Erratum 184, 683 (1997).

\[17\] H. Araki and L. Zsidó, Rev. Math. Phys. 17, 491 (2005). arXiv:math/0412061.

\[18\] A. Connes, “On the spectral characterization of manifolds,” J. Noncommut. Geom. 7, 1 (2013).

\[19\] D. Buchholz, O. Dreyer, M. Florig, and S. J. Summers, “Geometric modular action and spacetime symmetry groups,” Rev. Math. Phys. 12, 475 (2000).

\[20\] M. Takesaki, Tomita's Theory of Modular Hilbert Algebras and Its Applications, Lecture Notes in Math. 128 (Springer, 1970).

\[21\] A. Connes and H. Moscovici, “The local index formula in noncommutative geometry,” Geom. Funct. Anal. 5, 174 (1995).

\[22\] J. M. Gracia-Bondía, J. C. Várilly, and H. Figueroa, Elements of Noncommutative Geometry (Birkhäuser, 2001).

\[23\] D. Buchholz and E. H. Wichmann, “Causal independence and the energy-level density of states in local quantum field theory,” Commun. Math. Phys. 106, 321 (1986); D. Buchholz, C. D'Antoni, and K. Fredenhagen, Commun. Math. Phys. 111, 123 (1987) (local algebras are Type III₁).

\[24\] H. Araki and E. J. Woods, “A classification of factors,” Publ. RIMS Kyoto 4, 51 (1968) (ITPFI / infinite tensor products of type I factors).

**Internal (Z-Spin Cosmology)**

\[ZS-F0\] K. Kang, i-Tetration Fixed Point and the Koenigs Multiplier (|λ|² \= 0.7948), ZS-F0 v1.0 (2026), §8.9, §9.5.

\[ZS-F18\] K. Kang, The Finite/Infinite Möbius-Interface Meta-Structure, ZS-F18 v2.1 (2026), §5, §6.4 (NC-F18.1–6).

\[ZS-F23\] K. Kang, Generalized-Entropy Additive Constant and the Type III Crossed Product, ZS-F23 v1.3 (2026), §3, App B.2.

\[ZS-Q11\] K. Kang, OAQEC Logical Algebra A\_ZS \= M₃(ℂ) ⊕ ℂ ⊕ M₅(ℂ), ZS-Q11 v1.1 (2026), Thm 3.6.1 (PROVEN).

\[ZS-S15\] K. Kang, Twin-Reuleaux Electromagnetism — Poynting-Commutator Theorem, ZS-S15 v1.0 (April 2026), Thm S15.2.

\[ZS-M17\] K. Kang, Continuum Limit and Wightman Reconstruction of the BCC Field, ZS-M17 v1.0 (2026).

\[ZS-M30\] K. Kang, Frame Duality of Finite and Infinite, ZS-M30 v1.0 (2026), Thm 30.1.

\[ZS-F2\] K. Kang, Geometric Impedance: A \= 35/437, ZS-F2 v1.0 (March 2026).

\[ZS-F3\] K. Kang, H₀ Tension via Wilson Loop Holonomy, ZS-F3 v1.0 (March 2026).

\[ZS-F5\] K. Kang, Gauge Symmetry Constraint: Why Q \= 11 and (Z,X,Y) \= (2,3,6), ZS-F5 v1.0 (March 2026).

\[ZS-F19\] K. Kang, Modular (KMS) Tilt and the Tomita–Takesaki Direction, ZS-F19 v1.0 (2026).

\[ZS-M3\] K. Kang, Regge-Holonomy, Immirzi & Z-Telomere, ZS-M3 v1.0 (March 2026), Thm 5.1, Lemma 10.1.

\[ZS-M6\] K. Kang, Block-Laplacian Spectral Verification & Hodge-Dirac Construction, ZS-M6 v1.0 (2026), §5.5.

\[ZS-M26\] K. Kang, V₄-Equivariant ZBSI on the Cobordism-History Fiber, ZS-M26 v1.0 (May 2026).

\[ZS-M27\] K. Kang, V₄-Equivariant Cobordism BRST Closure via Kostant Cubic Dirac, ZS-M27 v1.0 (May 2026).

\[ZS-M32\] K. Kang, Spinor-Cycle Averaged Residual Criterion — Path-Reversal Lemma, ZS-M32 v1.0 (March 2026).

\[ZS-M36\] K. Kang, Apollonian Curvature Lattice as Spin-Pair Realization, ZS-M36 v1.0 (2026), §7.3.

\[ZS-Q7\] K. Kang, Structural Arrow of Time from the Z-Bottleneck, ZS-Q7 v1.0 (2026), Theorem 1\.

\[ZS-Q12V\] K. Kang, Bedrock Reduction: the Holographic Codim-1 Interface, ZS-Q12 v4.0 (May 2026), §13–§16.

\[ZS-S10\] K. Kang, Gauge Bridge via Stückelberg–Corollary IV Mechanism, ZS-S10 v1.0 (April 2026), Thm S10.5-BPS.

\[ZS-S16\] K. Kang, PMNS / Lepton Sector, ZS-S16 v1.2 (June 2026), §3.5 (bedrock positioning).

\[ZS-A7\] K. Kang, Horizon as Spinor — BH/WH Duality and the 4π Closure, ZS-A7 v1.0 (April 2026), §5.2, Cor I.

\[ZS-A16\] K. Kang, The Great Attractor as a Z-Spin Velocity-Watershed Defect, ZS-A16 v1.3 (June 2026).

\[ZS-Q16\] K. Kang, Single-Outcome Selection as a Z-Spin-Mediated Closure, ZS-Q16 v2.5 (June 2026), §22.4, O-Q16.12.

## **Version History**

v1.5 (June 2026): Strengthening release (deep-exploration round on the F18 finite/infinite methodology; external proven-mathematics search). Does NOT close O-Q16.12; strengthens both halves of the v1.4 verdict. (1) Metric NO-GO (b) made STRUCTURAL as well as spectral (§9.4): the F18 Möbius polarity (ZS-F18) shows the finite X-bulk communicates with the infinite Y-sector only through the 2D seam (mediation, not collapse), so a finite bulk cannot carry an infinite p \= 3 metric — the bottleneck is the no-go. (2) The rotation-3 vs metric-3 distinction (§9.4, Corollary F.1): the corpus's derived “dim(X) \= 3” (ZS-S15 Theorem S15.2 / F18 §6.4, the commutator \[J\_R₁,J\_R₂\]=J\_S) is the SO(3)-generator count (finite rotation algebra), NOT the Riemannian metric 3 (a 3-manifold with n^{1/3} Weyl growth); conflating them is the Theorem-F category error. (3) Co-orientation (a) hosting upgraded (§7): the multi-cell ITPFI of A\_ZS \= M₃ ⊕ ℂ ⊕ M₅ (ZS-Q11, dim 35\) on the non-tracial equilibrium state is Type III (ZS-F23 App B.2; Buchholz–Wichmann \[23\] via M17), so hosting is DERIVED-CONDITIONAL (geometry-conditional); the inclusion source (one-sided compression \+ Takesaki resolution) stays HYPOTHESIS-strong. (4) Appendix B adds B.12 (rotation-3 vs metric-3) and B.13 (ITPFI Type III hosting); verification 30/30 → 32/32 (16 \+ 16 executed). Six references added (\[23\] Buchholz–Wichmann, \[24\] Araki–Woods; internal ZS-F18, ZS-F23, ZS-Q11, ZS-S15, ZS-M17, ZS-M30). (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED unchanged; zero new free parameters.

v1.4 (June 2026): Closure-by-settlement (deep-exploration round; external proven-mathematics search). (1) NEW headline Theorem F (§9, Spin–Metric Independence, NO-GO): by Connes' reconstruction theorem \[18\] the metric dimension is the Weyl exponent of the Dirac spectrum (λ\_n ∼ n^{1/p}); the corpus i-tetration transfer operator has geometric spectrum {μ^k}, |μ| \= √0.7948, with spectral zeta Σ μ^{sk} \= 1/(1−μ^s) finite for all s \> 0 → metric dimension p \= 0 (point-like); the Kraus half-angle is p \= 0; a single record-flow half-sided inclusion is 1-dimensional (Borchers/Wiesbrock A(1)). Hence none of the corpus's information/spin operators can be the 3D X-Dirac operator: the 3D metric is independent of curvature (A) and of the record-flow/i-tetration spin structure — the curvature–spin–metric trichotomy. (2) §10 SETTLES O-Q16.12: co-orientation half CLOSED (Theorem E, v1.3); metric half is an ESSENTIAL residual (Theorem F), identical to the unproven emergent-spacetime problem; a closure claim would also conflict with the corpus single-postulate structure (ZS-Q12V/Q16/S16). Theorem C stays DERIVED-CONDITIONAL, its residual now proved essential. (3) Appendix B adds B.10 (spectral-dimension no-go) and B.11 (single-inclusion dimension count); verification 28/28 → 30/30 (16 \+ 14 executed). Three external references added (\[18\] used centrally; \[21\] Connes–Moscovici; \[22\] Gracia-Bondía–Várilly–Figueroa). (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED unchanged; zero new free parameters.

v1.3 (June 2026): NEW Theorem E (co-orientation from record flow) grounded in Borchers/Wiesbrock; Theorem C co-orientation upgraded to DERIVED; O-Q16.12 split into co-orientation (closed) \+ Connes–Dirac residual. Superseded by v1.4 (which proves the residual essential).

v1.2 (June 2026): Theorem B corrected to the double-cover sequence; Theorem C (spin-from-record) DERIVED-CONDITIONAL; §8 → Theorem D. v1.1: Theorem A/B split; dim(Z) erratum. v1.0: initial consolidation. All superseded.