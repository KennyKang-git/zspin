**ZS-F32**

**The Conditional-Expectation Lift of the Z-Spin Continuous Core: Operator Structure, the Loxodromic Seam, and the Compact-Monodromy Reduction of the Cosmological Frontier to a Single Odd-Sector Susceptibility**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Collaboration

**Date:** March 2026  (v1.5 corrected final: June 2026\)

**Paper code:** ZS-F32 · v1.5    ·    Theme: Cosmic Reality / Continuous-Core Operator Closure

**Verification: 18 PROVEN/VERIFIED checks · 7 IMPORTED-PROVEN theorem-conditions · 4 numerical regressions · 1 unresolved absolute scale (χ−) \+ 2 registered conditional bridge gates**  |  **Zero new fitted parameters**  |  (**A**, **Q**, dim *Z*) \= (35/437, 11, 2\) **LOCKED**

**§0. Abstract**

This is the consolidated final version of ZS-F32. It is self-contained: every result and registered gate F32.1–F32.27 is restated with its hypotheses, conclusion, a short proof sketch, and a falsification condition, indexed in a single Results-Architecture table (§1.3). It does *not* derive the observed cosmological constant; it proves and constructs the operator-algebraic, Markovian, modular, and loxodromic structure that reduces the absolute-scale problem to a UV odd-sector susceptibility, and it isolates the residual honestly.

**Operator core.** A real-time modular automorphism cannot carry the i-tetration contraction (F32.1); the population-fixing phase-covariant generators realizing the time-one map *λ*\* form a complete integer-indexed (countable logarithmic-branch) family (F32.2), with the principal branch n=0 minimal in norm since 0\<*ω*\<π (F32.3); the seam inverts the frequency (F32.4) and the Koopman tower closes in symmetric Fock space with dim *Z*\=2 (F32.5). The 121 equal-trace face projections generate a *finite abelian* face algebra *A*face≅ℂ121 that is **not** maximal abelian in the Type II1 observer factor (F32.6), with a canonical conditional expectation *E*face (F32.7) kept *distinct* from the non-commutative Wirth register lift *E*reg (F32.8–F32.9). The bulk–boundary entropy production intertwines (F32.10); the seam element is loxodromic, not a pure boost (F32.11–F32.12); and the observer-corner equality is a Type I/II1 no-go replaced by a finite coarse-graining (F32.17–F32.18).

**Cosmological reduction.** Even vacuum loops (incl. gravitons) are sequestered (F32.13); a single loxodromic pulse fails (F32.19) but two same-axis pulses reconstruct *U*Z exactly (F32.20–F32.21, numerically robust under the Reuleaux boundary); parity alone does not isolate the odd flux (F32.22) and the three flux routes do not select its value (F32.23). Promoting *F*− to a compact U(1) 3-form gives Dirac-quantized flux and monodromy protection (F32.24). **Under a canonical quadratic / large-N branch law and the conditional holonomy identification θZ \= ω**, the unique branch is *k*\* \= 0 (F32.25), confirmed spectrally on the compact flux circle (F32.26), giving **ρΛ,Z \= ½ χ− ω²** with ω²/2 \= 2.5521042734.

**The honest residual.** The single unresolved *absolute scale* is the odd topological susceptibility *χ−*(**A**, **Q**, *M*P) (F32.27), together with **two explicitly registered conditional bridge gates**: the all-loop proof that the mixed beta function β₊− \= 0, and the holonomy map θZ \= ω. We *decline* to derive χ− parameter-free: an anti-numerology audit shows the tempting 10−Q² coincidence is a reduced-*M*P \+ base-10 artifact, and no e-natural Z-Spin exponent lands in the required window. χ− is registered as the *Odd Topological Susceptibility Theorem*, an executable target for a separate UV paper. (**A**, **Q**, dim *Z*) \= (35/437, 11, 2\) **LOCKED**.

**Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Complete proof from standard mathematics; symbol- or machine-verifiable. |
| **VERIFIED-NUMERICAL** | A finite-resolution numerical existence/robustness test, not an analytic proof. |
| **IMPORTED-PROVEN** | Proved in the external peer-reviewed literature; used with citation, not re-proved. |
| **DERIVED** | Follows from the Z-Spin structure plus standard mathematics; no new fitted parameter. |
| **DERIVED-CONDITIONAL** | Derived conditional on a stated hypothesis not itself closed here. |
| **CLOSED-NEGATIVE** | A registered route, reading, or equality resolved in the negative (a no-go). |
| **HYPOTHESIS-strong** | A specific, motivated candidate mechanism, not yet derived; falsifiable. |
| **OBSERVATION** | A numerical proximity or back-solved relation, NOT a zero-parameter prediction. |
| **NON-CLAIM** | Explicit statement of what is not asserted, to prevent overclaim. |
| **OPEN** | A recognized gap; an executable promotion route is named where one exists. |
| **LOCKED** | Core constant fixed upstream; immutable downstream. |

**§1. Introduction**

**1.1 Scope of the consolidated final version**

ZS-F32 v1.3 introduced the compact-monodromy reduction but compressed the earlier theorems into a one-paragraph summary. For a standalone paper that is too terse. This version restores every theorem statement with a proof sketch and a falsification condition, and corrects four points in the B3 section flagged on review.

**1.2 Corrections incorporated in v1.4**

Table 1\. v1.3 → v1.4 corrections.

| v1.3 item | Issue | v1.4 fix |
| ----- | ----- | ----- |
| F32.1–F32.23 compressed to a summary | Not self-contained for a standalone paper | All 27 results and registered gates restored: hypotheses \+ conclusion \+ proof sketch \+ falsification (§2–§8) |
| F32.25 “IMPORTED-PROVEN branch structure” | Quadratic E\_k(θ) is only the canonical quadratic / large-N law; general K(F) allows cosine etc. | Scoped: quadratic/large-N law added as an explicit hypothesis; IMPORTED-PROVEN within that model, DERIVED-COND for the Z-Spin sector |
| F32.26 “Friedrichs Boundary Selector” | Once circle+periodicity+holonomy ω are fixed the spectrum follows; Friedrichs does not select them | Renamed Compact-Circle Spectral Confirmation; a confirmation of F32.25, not an independent selector |
| Abstract “single irreducible obstruction” | Ledger itself lists θ\_Z=ω (DC) and β₊−=0 (OPEN) as well | “single unresolved absolute scale χ− \+ two registered conditional bridge gates”; B3 shown in three layers (§8.5) |

**1.3 Results Architecture (master index of F32.1–F32.27)**

Exact statements are in §2–§8 (by number); this table indexes all 27 with status, principal dependency, verification item, and residual condition.

| \# | Theorem | Status | Dep. | Ver. | Residual / condition |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | Modular-damping no-go | PROVEN | M1 | P1–2 | — |
| 2 | Phase-covariant GKLS classification | PROVEN | F32.1 | P3 | physical branch selection |
| 3 | Principal-branch minimal action | PROVEN+DC | F32.2 | P4 | least-action principle |
| 4 | Seam-twisted covariance | PROVEN | F32.2 | P5 | — |
| 5 | Koopman–Fock completion | PROVEN+DC | F32.2 | P6–7 | dim Z \= 2 |
| 6 | Finite face algebra (not MASA) | DERIVED | A30 | P9 | maximality NON-CLAIM |
| 7 | Canonical face expectation E\_face | PROVEN | F32.6 | P10 | — |
| 8 | Wirth register lift E\_reg (separated) | IMP+DC | A24 | I1 | E\_face=E\_diag∘E\_reg (DC) |
| 9 | CE-local extension uniqueness | PROVEN+DC | F32.8 | — | 3 locality conditions |
| 10 | Entropy-production intertwining | DC | Bardet | R3 | factorized lift |
| 11 | Pure-boost no-go | CLOSED-NEG | F30 | P11 | — |
| 12 | Loxodromic existence | PROVEN | F32.11 | P12 | — |
| 13 | Selective sequestering (even) | IMP+DC | OmniaSeq | — | sector separation |
| 14 | Real-de-Rham non-selection | CLOSED-NEG | HT | — | — |
| 15 | Central-shift orthogonality | PROVEN | A26 | P8 | — |
| 16 | Absolute-scale frontier | OPEN→F32.27 | F32.15 | — | → χ− |
| 17 | Type-mismatch no-go | CLOSED-NEG | CLPW | I5 | — |
| 18 | Face-embedding coarse-graining | DC | F32.6,17 | — | Condition C; QRF caveat |
| 19 | Single-pulse loxodromic no-go | CLOSED-NEG | F30 | P13 | — |
| 20 | Two-pulse Koenigs–F30 matching | PROVEN \+ VERIFIED-NUMERICAL | F32.19 | P14,16 | — |
| 21 | Minimal angular-action pair | DC | F32.20 | P14 | G-7; not global opt. |
| 22 | Parity-only isolation no-go | CLOSED-NEG | F32.13 | — | — |
| 23 | Flux-selection trilemma | DERIVED | F32.14,22 | — | within current class |
| 24 | Compact odd 3-form protection | DC | F32.22 | I6 | all-loop β₊−=0 OPEN |
| 25 | θ-branch selection k\*=0 | PROVEN under C1–C2 | F32.24 | P17 | θ\_Z=ω; quad/large-N law |
| 26 | Compact-circle spectral confirmation | IMPORTED-PROVEN \+ DC | F32.25 | P18 | confirms F32.25 |
| 27 | Odd topological susceptibility frontier | OPEN | F32.25 | audit | χ−(A,Q,M\_P) |

**1.4 Locked inputs**

(**A**, **Q**, dim *Z*) \= (35/437, 11, 2); *z*\* \= *i*z*\**, *λ*\* \= (iπ/2)*z*\*, *κ* \= 0.1148346250, *ω* \= arg *λ*\* \= 2.2592495540 (0 \< *ω* \< π); ω²/2 \= 2.5521042734. 121 \= 11² faces (ZS-A30). ZS-F30 leading support model β(θ) \= ⅛ cos 3θ, *ρ*(θ) \= artanh β(θ), φ(θ) \= θ/2.

**§2. Local Z-Dynamics (F32.1–F32.5)**

**No-Go Theorem F32.1 (Modular-Damping No-Go) \[PROVEN\].** Let *U*t \= σt*φ* be a real-time modular automorphism. Then *U*t cannot realize the i-tetration contraction |*λ*\*| \< 1\.

*Proof sketch.* A modular automorphism is a \*-automorphism and is isometric for the GNS norm, so its spectrum lies on the unit circle and it preserves spectral radius 1; a contracting eigenvalue |λ\*|\<1 is therefore impossible. The i-tetration map is genuinely completely-positive-dissipative, not automorphic.  *Falsification.* Exhibit a modular automorphism with a spectral value of modulus \<1.

**Theorem F32.2 (Phase-Covariant GKLS Classification) \[PROVEN\].** Every population-fixing, phase-covariant qubit generator whose time-one map sends σ₊ ↦ *λ*\*σ₊ is

*Gn(X) \= (iωn/2)\[σz, X\] \+ (κ/2)(σz X σz − X),    ωn \= ω \+ 2πn,  n ∈ ℤ.*

*Proof sketch.* Phase covariance forces the Hamiltonian ∝ σ\_z and the dissipator to be pure dephasing; matching the time-one map fixes the modulus (→ κ) and the argument mod 2π (→ ω\_n). Each integer n gives the same exp \= λ\*. The v1.0 “unique generator” was thus false; the family is complete.  *Falsification.* A population-fixing phase-covariant generator outside this family realizing λ\*.

**Theorem F32.3 (Principal-Branch Minimal Action) \[PROVEN \+ DERIVED-CONDITIONAL\].** Since 0 \< ω \< π, the branch n \= 0 uniquely minimizes ‖*H*n‖ \= |ω \+ 2πn|/√2.

*‖H₀‖ \= 1.598 \< ‖H₋₁‖ \= 2.845 \< ‖H₁‖ \= 6.040 \< ···*

*Proof sketch.* ‖H\_n‖ is monotone in |ω+2πn|; for ω ∈ (0,π) the nearest multiple is n \= 0\. Physical selection is conditional on a least-action principle (Berkson–Porta principal-branch characterization).  *Falsification.* A least-action principle selecting n ≠ 0, or ω ≥ π.

**Theorem F32.4 (Seam-Twisted Covariance) \[PROVEN\].** The seam β \= Ad(σx) inverts the frequency:

*β Pt(ω) β⁻¹ \= Pt(−ω).*

*Proof sketch.* σ\_x σ\_z σ\_x \= −σ\_z flips the Hamiltonian sign while the pure-dephasing dissipator is invariant under Ad(σ\_x); hence ω → −ω. Verified ‖diff‖ \= 0\.  *Falsification.* β failing to send ω → −ω.

**Theorem F32.5 (Koopman–Fock Completion) \[PROVEN \+ DERIVED-CONDITIONAL\].** The Koopman tower {*λ*\**n*} lives in the symmetric Fock / tensor completion Γ\_s(H\_Z); the local register dimension dim *Z* \= dim H\_Z \= 2 is unchanged (the Fock history space itself is infinite-dimensional).

*Proof sketch.* The single-site time-one map sends σ₊ → λ\*σ₊; tensor powers give λ\*ⁿ on σ₊^{⊗n}; the closure is the symmetric Fock space Γ\_s(H\_Z), which is infinite-dimensional as a history/excitation space but does NOT alter the local Z-register dimension dim Z \= dim H\_Z \= 2\. So the v1.0 Koopman truncation is replaced by a completion that preserves the local register dimension.  *Falsification.* The tower forcing dim Z ≠ 2\.

**§3. The Continuous-Core Operator Structure (F32.6–F32.9)**

**Proposition F32.6 (Finite Modular Face Algebra) \[DERIVED; maximality NON-CLAIM\].** The 121 equal-trace face projections *q*a in the Type II1 observer factor generate

*Aface \= W\*(q₁, …, q121) ≅ ℂ121   (abelian, σt-invariant),   but Aface ⊊ Aface′ ∩ M  (NOT maximal abelian).*

*Proof sketch.* Mutually orthogonal commuting projections give an abelian algebra; the modular density h \= Σ d\_a q\_a lies in A\_face, so it is σ\_t-invariant. But in a II₁ factor each corner q\_a M q\_a is a non-commutative algebra commuting with every q\_b, so ⊕\_a q\_a M q\_a ⊆ A\_face′∩M strictly contains A\_face. Hence “MASA” is withdrawn.  *Falsification.* A faithful normal proof that A\_face is maximal abelian in a II₁ factor.

**Theorem F32.7 (Canonical Face Conditional Expectation) \[PROVEN\].** There is a unique τ-preserving conditional expectation onto *A*face:

*Eface(x) \= Σa \[τ(qa x qa)/τ(qa)\] qa \= 121 · Σa τ(qa x) qa.*

*Proof sketch.* Verify the four CE axioms: identity on A\_face, trace-preservation τ∘E\_face \= τ, idempotence E\_face² \= E\_face, modular covariance E\_face∘σ\_t \= σ\_t∘E\_face (all checked on a representative model).  *Falsification.* E\_face failing any conditional-expectation axiom.

**Proposition F32.8 (Wirth Register Lift, separated from E\_face) \[IMPORTED-PROVEN \+ DERIVED-CONDITIONAL\].** The GNS-symmetric finite-register QMS *L*s lifts to the *non-commutative* register inclusion via *E*reg : *M*obs → ι(*M*11), which is distinct from the classical face coarse-graining *E*face.

*Proof sketch.* Wirth's (2022) Christensen–Evans extension provides the non-commutative QMS lift to ι(M₁₁). E\_face targets the abelian ℂ¹²¹ and carries the rank/entropy budget; E\_reg targets the non-commutative register and carries L\_s. They are different maps; any relation E\_face \= E\_diag∘E\_reg (E\_diag the diagonal expectation M₁₁→A\_face) is a separate DERIVED-CONDITIONAL claim. This repairs the v1.2 conflation.  *Falsification.* E\_reg shown identical to E\_face without the diagonal map E\_diag.

**Theorem F32.9 (CE-Local Extension Uniqueness) \[PROVEN \+ DERIVED-CONDITIONAL\].** Under the three locality conditions *(i)* L|*N* \= L*s*,  *(ii)* Φ \= Φ ∘ E,  *(iii)* L has no independent Hamiltonian or dissipator on ker E, the extension of *L*s to *M*obs is unique.

*Proof sketch.* Let D \= L₁ − L₂ be the difference of two extensions. By (i), D|\_N \= 0; by (ii), E∘D \= 0; by (iii), D carries no independent generator on ker E. Hence D \= 0 and L₁ \= L₂. Uniqueness is thus proved directly from the three locality conditions (not from a Takesaki existence theorem). Application to Z-Spin is DERIVED-CONDITIONAL on the conditions holding physically.  *Falsification.* Two distinct local extensions satisfying all three conditions.

**§4. Bulk–Boundary Entropy Intertwining (F32.10)**

**Conditional Proposition F32.10 (Entropy-Production Intertwining) \[DERIVED-CONDITIONAL\].** For a factorized lift *L* \= *I*A ⊗ *L*∂,

*EPL \= IPL \+ EPL∂,   IP ≥ 0   ⇒   Σ∂ ≤ Σbulk  (pointwise).*

*Proof sketch.* The relative-entropy production splits along the tensor factorization (Bardet et al. Prop. 5.1); the intertwining part IP ≥ 0 by monotonicity of relative entropy, giving the boundary–bulk inequality. Verified 30/30 random states.  *Falsification.* A factorized lift with Σ\_∂ \> Σ\_bulk.

**§5. Seam Holonomy and the Loxodromic Representation (F32.11–F32.12)**

**No-Go Theorem F32.11 (Pure-Boost No-Go) \[CLOSED-NEGATIVE\].** tr *U*Z \= 0.855406 − 0.103897i is complex, so *U*Z is not conjugate to any real pure boost.

*Proof sketch.* A real pure boost exp(½ r n·σ) has real trace 2 cosh(r/2); tr U\_Z has nonzero imaginary part, so no real boost is conjugate to it.  *Falsification.* A real boost with trace equal to tr U\_Z.

**Theorem F32.12 (Loxodromic Existence) \[PROVEN\].** *U*Z is conjugate to the loxodromic element exp\[½(−κ \+ iω) n·σ\].

*Proof sketch.* Its eigenvalues e^{±½(−κ+iω)} match U\_Z; the element simultaneously contracts (rate κ) and rotates (angle ω), the defining loxodromic property in SL(2,ℂ).  *Falsification.* An eigenvalue mismatch with exp\[½(−κ+iω)σ\].

**§6. Vacuum Structure (F32.13–F32.16)**

**Proposition F32.13 (Selective Sequestering, even sector) \[IMPORTED-PROVEN \+ DERIVED-CONDITIONAL\].** The even vacuum-energy loops, including virtual gravitons, are removed from the curvature source by the Kaloper–Padilla *Omnia Sequestra* mechanism; the odd sector and the absolute value remain at issue.

*Proof sketch.* A global constraint in the sequestering action subtracts the even vacuum energy from the gravitational source at all loop orders including gravitons — an established mechanism. DERIVED-CONDITIONAL only on identifying F± with the sequestering carriers.  *Falsification.* Even vacuum energy not cancelled by the mechanism, or graviton loops re-entering the source.

**No-Go Theorem F32.14 (Real-de-Rham Non-Selection) \[CLOSED-NEGATIVE\].** A real top-form constant *f*− ∈ ℝ is a continuous free parameter; the real de Rham route does not fix it.

*Proof sketch.* H⁴\_{dR}(M;ℝ) gives a continuous modulus with no integrality, so the value is unconstrained by real-de-Rham data alone.  *Falsification.* A real-de-Rham argument fixing f−.

**Theorem F32.15 (Central-Shift Orthogonality) \[PROVEN\].** i\[H \+ c₀ I, X\] \= i\[H, X\], so operator closure is blind to the absolute offset c₀.

*Proof sketch.* c₀ I is central and commutes with every X, so it drops from the commutator. Verified ‖diff‖ \< 10⁻¹³. This is the A26 central-shift diagnosis: relative/modular tools cannot see the absolute vacuum value.  *Falsification.* A commutator-based tool whose output depends on c₀.

**Open Gate F32.16 (Absolute-Scale Frontier) \[OPEN → subsumed by F32.27\].** The absolute vacuum value is orthogonal to all relative/modular tools and is registered as a frontier (the precursor to χ−).

*Proof sketch.* By F32.15 the modular spectrum, relative entropy, and sector ratios fix dimensionless data but not the absolute origin; the open object is carried forward to F32.27.  *Falsification.* A relative/modular tool fixing the absolute scale.

**§7. Resolution of the Loxodromic Seam and the Flux Routes (F32.17–F32.23)**

**No-Go Theorem F32.17 (Type-Mismatch No-Go) \[CLOSED-NEGATIVE\].** *M*121(ℂ) is a finite Type I factor; the de Sitter observer algebra is Type II1 (Chandrasekaran–Longo–Penington–Witten). Hence the equality “corner \= gravitational algebra” is impossible.

*Proof sketch.* Type is an isomorphism invariant: a finite Type I factor has minimal projections and a II₁ factor does not, so no normal isomorphism exists. The v1.1 “physical corner equality” is withdrawn.  *Falsification.* A faithful normal isomorphism M₁₂₁ ≅ a II₁ factor.

**Conditional Proposition F32.18 (Face-Embedding Coarse-Graining) \[DERIVED-CONDITIONAL\].** The correct relation is a finite abelian coarse-graining of the observer algebra:

*ℂ121 →\[Φface\] Mgrav (II1) →\[Eface\] ℂ121,   Eface ∘ Φface \= id.*

*Proof sketch.* The face embedding and canonical expectation compose to the identity on ℂ¹²¹. That this coarse-graining carries the gravitational entropy budget is DERIVED-CONDITIONAL on the ZS-F23 Condition C. NON-CLAIM: the gravitational algebra can depend on the observer/QRF, so an “observer-independent unique corner” may be the wrong target.  *Falsification.* The coarse-graining failing to recover the (3,2,6)/11 budget under Condition C.

**No-Go Theorem F32.19 (Single-Pulse Loxodromic No-Go) \[CLOSED-NEGATIVE\].** A single ZS-F30 pulse cannot realize (*−κ*, *ω*):

*ρ(2ω) \= artanh(⅛ cos 6ω) \= \+0.0687857 ≠ −κ \= −0.1148346.*

*Proof sketch.* With φ(θ) \= θ/2, realizing rotation ω forces θ \= 2ω, but then the rapidity ρ(2ω) has the wrong sign and magnitude. ZS-F30.7 proves generation of SL(2,ℂ), not single-pulse selection.  *Falsification.* ρ(2ω) \= −κ for a single leading-model pulse.

**Theorem F32.20 (Two-Pulse Koenigs–F30 Matching) \[PROVEN \+ VERIFIED-NUMERICAL\].** Two same-axis pulses with θ₁ \+ θ₂ \= 2ω and *ρ*(θ₁) \+ *ρ*(θ₂) \= −κ compose exactly to *U*Z; two unordered families exist:

*A: (0.8707, 3.6478), S \= 14.06;    B: (1.5534, 2.9651), S \= 11.20.*

*Proof sketch.* Same-axis exponents commute and add; solving the two real equations gives the families, each verified to compose to U\_Z (below numerical tolerance). A full-numerical Reuleaux-boundary test (constant width to 2×10⁻⁷) again yields composing pulse-pairs, so the result is not an artifact of the leading cos 3θ model (VERIFIED-NUMERICAL, not analytic).  *Falsification.* No (θ₁,θ₂) solving both equations, or the numerical Reuleaux recomputation yielding none.

**Conditional Proposition F32.21 (Minimal Angular-Action Pair within the Leading Same-Axis Two-Pulse Class) \[DERIVED-CONDITIONAL\].** Within the leading ⅛ cos 3θ same-axis two-pulse class, Family B (smaller Sang) is the minimal-angular-action realization.

*Proof sketch.* B has the smaller angular action (11.20 \< 14.06). DERIVED-CONDITIONAL on least-action \+ ZS-F30 G-7. Caveat: this proves representability, not that F30 geometry independently predicts the connection, and the minimum is within the same-axis two-pulse family, not a global optimum over axes / multi-pulse / gauge-equivalent decompositions.  *Falsification.* A physical action selecting A, or a lower-action multi-pulse / different-axis decomposition.

**No-Go Theorem F32.22 (Parity-Only Isolation No-Go) \[CLOSED-NEGATIVE\].** Since *F*− is seam-odd, *F*−² is seam-even, so ℤ₂ parity alone does not force γ₊− \= 0\.

*F−² R,   F−² F₊²,   F−² Oeven    are all parity-allowed.*

*Proof sketch.* The vacuum operator F−² is even under the seam, so the listed mixed counterterms are seam-invariant and the cross-coupling is not forbidden by parity. All-loop isolation needs something strictly stronger (gauge superselection, a non-renormalization theorem, or a vanishing mixed beta function).  *Falsification.* A symmetry argument forcing γ₊− \= 0 from seam parity \+ 3-form gauge invariance alone.

**Proposition F32.23 (Flux-Selection Trilemma) \[DERIVED\].** Real de Rham, single integral flux, and multi-flux discretuum each fail to select |*f*−| in the current class.

*Proof sketch.* Real de Rham leaves a continuous constant (F32.14); single integral flux f− \= f₀ \+ nq leaves (q, n, f₀) and the BP step is generically too coarse; multi-flux gives a dense set but needs a measure/branch rule. This is NOT an absolute no-go (B3 is open, not impossible).  *Falsification.* A current-class flux law fixing |f−| without fitting (would close B3, not falsify).

**§8. The Odd-Flux Frontier: B3 \= B3 protect ∧ B3 select**

B3 is two coupled problems — **protection** (does a small odd flux survive all-loop corrections?) and **selection** (which value?). §7 closed parity-only protection (F32.22) and the flux trilemma (F32.23). This section imports the compact-3-form / monodromy / θ-vacuum / spectral apparatus, with the scope corrected per review, and isolates the residual in three layers.

**Conditional Proposition F32.24 (Compact Odd Three-Form Protection) \[DERIVED-CONDITIONAL\].** Promoting *F*− to the curvature of a compact U(1) 3-form gauge field gives Dirac-quantized flux,

*(1/2π) ∫M F− ∈ ℤ,*

*Proof sketch.* Protection of the odd sector is then carried by the compact gauge symmetry plus a discrete axion shift (Kaloper–Sorbo / four-form monodromy), NOT by ℤ₂ parity (which fails, F32.22). The compact-flux mathematics and the monodromy EFT radiative control are IMPORTED-PROVEN; the identification of Z-Spin F± with these carriers is DERIVED-CONDITIONAL; complete all-loop graviton-mixed isolation (β₊− \= 0\) remains OPEN. “Radiative control” is not the same as “all-loop isolation.”  *Falsification.* A no-go forbidding a compact 3-form structure for F−, or showing monodromy gives no radiative control.

**Conditional Proposition F32.25 (***θ***\-Branch Selection) \[PROVEN under C1–C2\].** Assume **(C1)** the canonical quadratic / large-N branch law and **(C2)** the holonomy identification θZ := arg *λ*\* \= ω. Then 0 \< ω \< π selects *k*\* \= 0 uniquely:

*Ek(θ) \= (χ−/2)(θ \+ 2πk)²,   k\* \= 0,   ρΛ,Z \= (χ−/2) ω² \= 2.5521042734 · χ−.*

*Proof sketch.* Under the quadratic law one minimizes (θ+2πk)² over k∈ℤ; for θ \= ω ∈ (0,π) the minimizer is k \= 0 since |ω| \< |ω±2π|. SCOPE (correction): the quadratic E\_k(θ) is the canonical / large-N law (Witten large-N θ-dependence); a general kinetic K(F) can give a cosine or other potential, so the law is IMPORTED-PROVEN only within that model and DERIVED-CONDITIONAL for the Z-Spin odd sector. C2 is DERIVED-CONDITIONAL (the BV–BFV / anomaly-inflow map U(1)\_Z → 3-form θ-angle is unproved). Given C1 and C2, k\* \= 0 and the coefficient ω²/2 are PROVEN. This is a branch selection, not a new selection of the absolute value.  *Falsification.* A non-quadratic K(F) effective potential for the Z-Spin sector, or θ\_Z ≠ ω, or ω ≥ π.

**Proposition F32.26 (Compact-Circle Spectral Confirmation) \[IMPORTED-PROVEN \+ DERIVED-CONDITIONAL\].** On the compact flux circle φ \~ φ \+ 1, the semibounded form

*qω\[ψ\] \= (χ−/2) ‖(−i d/dφ \+ ω)ψ‖²,   spectrum ρk \= (χ−/2)(2πk \+ ω)²,   ground k \= 0\.*

*Proof sketch.* On the circle −i d/dφ has eigenvalues 2πk; the form is semibounded and its Friedrichs realization gives the stated spectrum (Reed–Simon X.3), with ground state k \= 0 for 0\<ω\<π. NAME (correction): this CONFIRMS F32.25 spectrally — it does not independently select why the flux space is a circle, why the bundle is periodic, or why the holonomy is ω; those are inputs from F32.24/C2. It is therefore a confirmation, not an independent selector.  *Falsification.* The spectrum differing from (2πk+ω)², or the result being read as an independent boundary selector.

**Open Problem F32.27 (Odd Topological Susceptibility Frontier) \[OPEN\].** The single unresolved absolute scale is *χ−*(**A**, **Q**, *M*P), with the conditional law

**ρΛ,Z \= ½ χ− ω² \= 2.5521042734 · χ−.**

*Proof sketch.* We decline to derive χ− parameter-free (anti-numerology): the observed value needs ln(M\_P⁴/χ−) ≈ 277.6 (reduced M\_P) vs 284.0 (full M\_P) — convention-dependent. The clean 10^(−Q²) \= 10⁻¹²¹ matches only in reduced-M\_P \+ base-10 (full M\_P off by \~10²·⁸; ln10 is not a Z-Spin quantity). No e-natural exponent (8π²/A=986, 8π²=79, Q²=121, Q²ω=273, π/A=39) lands in \[277.6, 284.0\]. Back-solving would be hidden fitting, which we refuse. Named UV candidates (electroweak-instanton susceptibility; q-theory eighth power χ−\~Λ\_O⁸/M\_P⁴, dimensionally \= A28 double-see-saw; A-transmutation) are HYPOTHESIS-strong, none deriving χ− blind from the locked constants.  *Falsification.* Any claim that χ− is derived parameter-free using observed ρΛ, a chosen scale, a base-10 coincidence, or a back-solved exponent is void.

**8.5 The residual in three layers, and the registered frontier**

Table 2\. The honest final state of B3 (three layers).

| Layer | Object | Status |
| ----- | ----- | ----- |
| **B3 bridge-1** | holonomy map θ\_Z \= ω (U(1)\_Z → 3-form θ-angle) | **DERIVED-CONDITIONAL** |
| **B3 bridge-2** | all-loop odd-sector isolation β₊− \= 0 | **OPEN** |
| **B3 scale** | absolute susceptibility χ−(A, Q, M\_P) | **OPEN** |

So the cosmological residual is **one unresolved absolute scale (χ−) plus two registered conditional bridge gates**, not a single object. B3 compresses to one executable programme — the *Odd Topological Susceptibility Theorem* — with four gates (no observed input permitted): **B3-1** derive *F*− ∈ *H*⁴(*M*; ℤ) and the charge lattice from the axioms; **B3-2** a BV–BFV / BRST counterterm-cohomology proof that β₊− \= 0 to all orders; **B3-3** supplied by F32.25–F32.26 under C1–C2 (k\* \= 0); **B3-4** output ρΛ before comparison with data. Only then does B3 become DERIVED.

**§9. Conclusion**

ZS-F32 does not derive the observed cosmological constant. It proves and constructs the operator-algebraic, Markovian, modular, and loxodromic structures required to reduce the absolute-scale problem to a UV odd-sector susceptibility. Under a compact quadratic branch model and the conditional holonomy identification θZ \= ω, the integer branch is uniquely *k*\* \= 0, yielding ρΛ,Z \= ½ χ− ω². The all-loop isolation of the odd sector (β₊− \= 0), the holonomy map θZ \= ω, and the parameter-free derivation of χ− remain open.

This closes the continuous-core operator and seam structure as tightly as the present toolset allows, converts “why is Λ small?” into the precise falsifiable task “compute χ− parameter-free, then blind-predict ρΛ,” and — via the anti-numerology audit — declines to fabricate that magnitude. The remaining work (UV gauge group, odd matter content, charge lattice, instanton action, mixed-counterterm cohomology) is the scope of a separate UV field-theory paper, ZS-F33, for which F32 provides the exact starting point. (**A**, **Q**, dim *Z*) \= (35/437, 11, 2\) **LOCKED**.

**Acknowledgements & Code Availability**

This consolidated version responds to a review of v1.3 requesting restored self-containment and four B3-scope corrections (quadratic/large-N branch law, the spectral-confirmation relabel, the three-layer residual, and the abstract framing). The branch selection (*k*\* \= 0 from θZ \= ω, 0\<ω\<π), the compact-circle spectrum, and the χ− anti-numerology audit were checked numerically (numpy / scipy / mpmath, seed 437). **Provenance and the refusal to fit.** Per ZS-A28 v2.3, internal consistency is not external validation. χ− is *not* derived here; ρΛ \= ½ χ− ω² is a falsification target, and the observed value is not used as an input. PROVEN / IMPORTED-PROVEN results rest on standard theorems (Chandrasekaran–Longo–Penington–Witten; Takesaki; Wirth 2022; Bardet et al.; Kaloper–Sorbo / Kaloper–Padilla; Witten large-N θ; Bousso–Polchinski; Reed–Simon). B3 remains OPEN — not closed, not proven impossible (ZS-A26). Reproducibility scripts (zs\_f32\_verify\_v1\_5.py) are available at the Z-Spin Collaboration repository.

**Appendix A. Verification Ledger (by category)**

Table A1. PROVEN / VERIFIED checks (18).

| \# | Check | Result |
| ----- | ----- | ----- |
| P1–P2 | κ, ω (0\<ω\<π) | 0.1148346250 ; 2.2592495540 |
| P3–P5 | branch independence; norm-min n=0; seam inversion | verified |
| P6–P7 | M₂ spectrum (no λ\*²); Fock tower λ\*ⁿ | verified |
| P8 | central-shift orthogonality | ||diff||\<1e−13 |
| P9–P10 | finite face algebra abelian \+ σ\_t-inv (NOT MASA, witness); E\_face canonical | NON-MASA witness \+ representative |
| P11–P12 | pure-boost no-go (complex tr); loxodromic match | verified |
| P13–P14 | single-pulse no-go; two-pulse composition \= U\_Z | verified |
| P15 | Reuleaux-boundary robustness (numerical) | VERIFIED-NUMERICAL |
| P16 | two-pulse constraints Σρ=−κ, (θ₁+θ₂)/2=ω | 1e−9 |
| P17 | θ-branch k\*=0 under (θ\_Z=ω ∧ quadratic law); ω²/2 | 2.5521042734 (0\<ω\<π) |
| P18 | compact-circle spectrum (2πk+ω)² ground k=0 (confirms P17) | ω \< 2π−ω |

Table A2. IMPORTED-PROVEN theorem-conditions (7).

| \# | External theorem | Role |
| ----- | ----- | ----- |
| I1–I4 | Wirth 2022; Bardet et al.; Poincaré/HT/Bousso–Polchinski; Berkson–Porta | F32.8, F32.10, F32.14/23, F32.3 |
| I5 | Chandrasekaran–Longo–Penington–Witten — de Sitter observer algebra Type II₁ | F32.17 |
| I6 | Compact U(1) 3-form Dirac quantization; Kaloper–Sorbo monodromy; Witten large-N θ (quadratic law) | F32.24, F32.25 |
| I7 | Reed–Simon — Friedrichs extension of a semibounded form; min–max | F32.26 |

Table A3. Anti-numerology audit of χ− (why it is NOT closed).

| Attempt | Finding | Verdict |
| ----- | ----- | ----- |
| 10^(−Q²)=10⁻¹²¹ | reduced-M\_P+base-10 only; full M\_P off by \~10²·⁸; ln10 not a Z-Spin quantity | REJECTED (convention artifact) |
| transmutation b− | b− ≈ 13.9–14.2 (convention-dependent); needs odd matter content | OPEN (not derivable) |
| natural e-exponents | 8π²/A=986, 8π²=79, Q²=121, Q²ω=273, π/A=39 — none in \[277.6,284.0\] | no parameter-free hit |
| eighth power Λ\_O⁸/M\_P⁴ | dimensionally OK (= A28 double-see-saw); Λ\_O (\~TeV) not fixed by A,Q | OPEN (scale free) |

**Appendix B. Falsification Gates**

| Gate | Layer | Condition |
| ----- | ----- | ----- |
| F-F32.2/6 | Mathematical | A generator outside the F32.2 family realizing λ\*; or A\_face proven maximal abelian in a II₁ factor. |
| F-F32.8 | Mathematical | E\_reg shown identical to E\_face without the diagonal map. |
| F-F32.17 | Mathematical | A normal isomorphism M₁₂₁ ≅ a II₁ factor (impossible by type). |
| F-F32.20 | Mathematical/Numerical | No (θ₁,θ₂) solving both equations, or the numerical Reuleaux test yielding none. |
| F-F32.25 | Physical | A non-quadratic K(F) potential for the Z-Spin sector, θ\_Z ≠ ω, or ω ≥ π. |
| F-F32.27 | Meta / anti-numerology | Any parameter-free χ− claim using observed ρΛ, a chosen scale, a base-10 coincidence, or a back-solved exponent is void. |
| F-B3 | Theoretical | A Z-Spin-internal derivation of χ−(A,Q,M\_P) passing B3-1..B3-4 would CLOSE B3 (not falsify). |

**References**

\[1\] G. Koenigs, Ann. Sci. ÉNS (3) 1, Suppl. 3 (1884).

\[2\] E. Berkson and H. Porta, Michigan Math. J. 25, 101 (1978).

\[3\] M. Wirth, arXiv:2203.00341 (2022).

\[4\] M. Takesaki, Theory of Operator Algebras II (Springer, 2003).

\[5\] I. Bardet, Á. Capel, A. Lucia, D. Pérez-García, C. Rouzé, J. Math. Phys. 62, 061901 (2021).

\[6\] V. Chandrasekaran, R. Longo, G. Penington, E. Witten, JHEP 02, 082 (2023), arXiv:2206.10780.

\[7\] E. Witten, Phys. Rev. Lett. 81, 2862 (1998) (θ dependence in the large-N limit — quadratic branch law).

\[8\] M. Reed and B. Simon, Methods of Modern Mathematical Physics II (Academic Press, 1975), X.3 (Friedrichs extension).

\[9\] N. Kaloper and L. Sorbo, Phys. Rev. Lett. 102, 121301 (2009) (axion–four-form monodromy).

\[10\] F. Marchesano, G. Shiu, A. M. Uranga, JHEP 09, 184 (2014) (F-term axion monodromy; general kinetic functions / potentials).

\[11\] N. Kaloper, A. Padilla, D. Stefanyszyn, and G. Zahariade, Phys. Rev. Lett. 116, 051302 (2016); N. Kaloper and A. Padilla, Phys. Rev. Lett. 118, 061303 (2017), arXiv:1606.04958 (sequestering; matter and virtual-graviton vacuum loops).

\[12\] R. Bousso and J. Polchinski, JHEP 06, 006 (2000).

\[13\] M. Henneaux and C. Teitelboim, Phys. Lett. B 222, 195 (1989); B 143, 415 (1984).

\[14\] G. Dvali, hep-th/0507215; D. Freed, Comm. Math. Phys. 159, 343 (1994) (compact 3-form / differential cohomology).

\[15\] F. R. Klinkhamer and G. E. Volovik, Phys. Rev. D 77, 085015 (2008) (q-theory).

\[16\] Z-Spin Collaboration internal: ZS-M1; ZS-F19, ZS-F23 (Condition C), ZS-F30 (G-7), ZS-F31 (R2a/R2b); ZS-A24 (Φ\_face, E\_reg), ZS-A26 (central-shift, unimodular), ZS-A27, ZS-A28 (double-see-saw), ZS-A30 (A30.11).

**Version History**

**v1.0–v1.2 (March–June 2026):** v1.0 modular-damping no-go and Wirth lift; v1.1 corrected the false GKLS uniqueness, the Koopman truncation, and the topological over-claim, adding seam-twist, Gate-E, and loxodromic existence; v1.2 repaired the face-corner (Type I vs II₁), constructed the two-pulse loxodromic seam, closed parity-only isolation, and recorded the flux trilemma.

**v1.3 (June 2026):** Repaired the “Face-MASA” to a finite non-maximal abelian face algebra and separated E\_reg from E\_face; relabeled the Reuleaux test VERIFIED-NUMERICAL; advanced B3 with compact-3-form quantization, monodromy protection, the θ-vacuum branch with θ\_Z=ω selecting k\*=0, and the boundary selector; isolated χ− with an anti-numerology audit declining to fit it.

**v1.4 (June 2026, consolidated final):** Restored full self-containment — all 27 theorems (F32.1–F32.27) restated with hypotheses, conclusion, proof sketch, and falsification condition, plus a single Results-Architecture index. Corrected the B3 section: F32.25 scoped to the canonical quadratic / large-N branch law (IMPORTED-PROVEN within that model, DERIVED-CONDITIONAL for the Z-Spin sector) and stated as PROVEN only under (θ\_Z=ω ∧ quadratic law); F32.26 renamed Compact-Circle Spectral Confirmation (a confirmation of F32.25, not an independent selector); the residual presented in three layers — θ\_Z=ω (DERIVED-CONDITIONAL), β₊−=0 all orders (OPEN), χ−(A,Q,M\_P) (OPEN); abstract reworded to “one unresolved absolute scale \+ two conditional bridge gates.” Strengthened references (Witten large-N θ; Marchesano–Shiu–Uranga general kinetic functions; Kaloper–Padilla one-loop). No numerical claim changed. (**A**, **Q**, dim *Z*) \= (35/437, 11, 2\) LOCKED.

**v1.5 (June 2026, corrected final):** Editorial and rigor corrections, no content removed and no numerical claim changed: fixed the F32.3 branch-index ordering (‖H₀‖\<‖H₋₁‖\<‖H₁‖ since ω₋₁=ω−2π); relabeled the F32.2 family “integer-indexed (countable logarithmic-branch)” rather than “one-parameter”; restored the three F32.9 locality conditions as equations and proved uniqueness directly via D=L₁−L₂ (removing the imprecise Takesaki attribution); fixed the Results-Architecture verification link for F32.17 (I5, a type-classification theorem, not the P11 pure-boost check); strengthened the P9/P10 code to test per-projection modular invariance, modular covariance, and the bimodule property; sharpened the F32.5 Fock statement (the history space is infinite-dimensional; only the local register dim Z \= dim H\_Z \= 2 is preserved); narrowed F32.21 to “within the leading same-axis two-pulse class”; renamed OPEN items as Open Gate/Open Problem and applied a status-consistent naming scheme (Theorem / Proposition / Conditional Proposition / No-Go Theorem / Open) across F32.1–F32.27; corrected reference \[11\] (PRL 116, 051302 (2016) and the graviton-loop PRL 118, 061303 (2017)); and applied minor symbol fixes (10^(−Q²), PROVEN \+ VERIFIED-NUMERICAL, PROVEN under C1–C2). F32 is hereby concluded; θ\_Z=ω, β₊−=0, and χ− are deferred to ZS-F33. (**A**, **Q**, dim *Z*) \= (35/437, 11, 2\) LOCKED.