**ZS-A21**

**Seam-Cohomology Obstruction, Single-Clock Selection, and Polyhedral Graph-Discrimination for ZHCS Dark Matter: Constraining the 32-Face Abundance Degeneracy**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Collaboration

**Date:** June 2026

**Theme / Paper Code:** Astrophysics — ZS-A21 v1.5

 

## **Verification Summary**

Verification: **28/28 computational checks PASS** (Appendix I; script released) | Zero new fitted parameters | (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED** | **Theorem 1 (Seam-Cohomology Obstruction): PROVEN** — with the A19 one-cross-edge graph **b₁(Γ₃₈) \= 66**, H³\_seam ≅ ℤ ⊕ ℤ^{66r} ⊕ T^{⊕66}; unique parent ⇔ H₁(Mᴢ) \= 0 | **Corollary 2:** single-clock \+ no-torsion ⇔ M0; M0 \= **DERIVED-CONDITIONAL on L\_clock** (reduced here to L\_clock \= L\_clock-bulk ∧ L\_clock-restrict) | **Uniform Nodewise Coupling Theorem: PROVEN within U1–U6** ⇒ **Gᴢ reduced to g₁ ∧ g₂** | **Theorem 4 (Polyhedral Graph-Discrimination): PROVEN** — the icosidodecahedron is **incompatible with the A19-fixed seam graph** (its cold b₁ \= 29 forces seam b₁ \= 36 ≠ 66; not an independent exclusion), and the truncated icosahedron and truncated dodecahedron are **non-isospectral by the exact integer invariant** tr(L²) \= Σdᵢ² \+ 2E \= 1200 vs 1560; the graph-to-physical-mode bridge is the open lemma **L\_spec** (TARGET), so the 32-face abundance degeneracy is constrained at the graph level | Physical assignment: **HYPOTHESIS-strong**, now with a concrete discriminator | Empirical program \= **TARGET-COMPUTATIONS** (ILLUSTRATIVE ratio-only selection; NON-CLAIM) | Fit-free: R\_cb \= 16/3, f\_b^{(cb)} \= Ω\_b/(Ω\_c+Ω\_b) \= 3/19, Ω\_cb \= 38/121 (nₛ \= 0.9674 imported). **No real-data result is claimed.**

# **§0. Abstract**

ZS-A21 v1.3 corrected the seam Betti number and baryon fraction and scoped the coupling theorem to an explicit ansatz; v1.4–v1.5 keep that corrected base and add a new result that **constrains the 32-face abundance degeneracy at the graph level**, a sharpening of L\_clock, and status corrections; v1.5 finalizes the framing and the proofs and is the terminal text version, all under claim-to-tool calibration.

**(i) Seam-Cohomology Obstruction (Theorem 1, PROVEN).** With H₁(Mᴢ; ℤ) \= ℤ^r ⊕ T and m \= b₁(Γ), Künneth and Poincaré–Lefschetz give H³((Mᴢ, ∂Mᴢ) × Γ; ℤ) ≅ ℤ ⊕ ℤ^{mr} ⊕ T^{⊕ m}. For the A19 one-cross-edge seam graph, b₁(Γ₃₈) \= 59 \+ 7 \= 66; a unique parent charge exists iff H₁(Mᴢ) \= 0\.

**(ii) Homology-Ball Selection (Corollary 2\) and a sharper L\_clock.** single-clock \+ no-torsion ⇔ M0 (a corollary of Theorem 1 and standard 3-manifold homology). The physics lemma L\_clock is sharpened into a conjunction: **L\_clock-bulk** (the A20 scalar kinetic matrix is rank-one, S\_cb \= 0; IMPORTED from A20) and **L\_clock-restrict** (its restriction to the seam boundary is rank-preserving). M0 is thus **DERIVED-CONDITIONAL on L\_clock \= L\_clock-bulk ∧ L\_clock-restrict**; we do not claim M0 outright, and the explicit BV–BFV zero-mode computation of L\_clock-restrict is named as the principal mathematical-physics target.

**(iii) Uniform Nodewise Coupling Theorem (PROVEN within U1–U6).** Within an explicit ansatz, graph-edge conservation dΓ k \= 0 on the connected Γ₃₈ forces a single coefficient k\_v \= k and |k| \= 1 (k \= \+1 by orientation), discharging g₃ and g₄ and reducing Gᴢ to g₁ ∧ g₂ (OPEN); the unrestricted coupling classification remains OPEN. The I\_h-invariant cold functional is two-dimensional (12-pentagon and 20-hexagon orbits), and a \= b is forced by graph connectedness, not I\_h.

**(iv) Polyhedral Graph-Discrimination Theorem (Theorem 4, PROVEN) — the new result.** Three solids realize 32 faces and hence the abundance 32/121 identically — the truncated icosahedron (12 pentagons \+ 20 hexagons), the truncated dodecahedron (20 triangles \+ 12 decagons), and the icosidodecahedron (20 triangles \+ 12 pentagons) — so a ratio-only likelihood is polyhedron-blind. We constrain the degeneracy at the graph level with two corpus-internal invariants. (a) **Topological compatibility:** the cold-module face graph has b₁ \= 59 for the first two but 29 for the icosidodecahedron, so the icosidodecahedron is **incompatible with the A19-fixed seam graph** (it would force seam b₁ \= 36 ≠ 66). This is a compatibility statement with A19's already-truncated-icosahedron specification, **not an independent selection theorem** (b₁ \= 66 is itself computed from the A19 graph; a true selection would require b₁ \= 66 derived independently — e.g. from an action zero-mode count or from L\_clock). (b) **Spectral non-isospectrality (exact):** the truncated icosahedron and truncated dodecahedron share (V, E, b₁) \= (32, 90, 59\) but have different Laplacians, proven without floating point by the integer invariant tr(L²) \= Σdᵢ² \+ 2E \= 12·5² \+ 20·6² \+ 2·90 \= 1200 versus 20·3² \+ 12·10² \+ 2·90 \= 1560\. The bridge from the graph spectrum to a physical mode spectrum is a separate open lemma **L\_spec** (that the linearized ZHCS boundary Hessian contains the cold-module Laplacian with a fixed coefficient, giving ωⱼ² \= ω₀² \+ αλⱼ); the CMB template is a TARGET-COMPUTATION. The upstream ZS-F2/A19 structure (the 12/20 orbit assignment, the C₆₀ fullerene realization, |I\_h| \= 120 \= Q² − 1\) selects the truncated icosahedron among the two. The physical assignment is thereby narrowed — the icosidodecahedron incompatible with A19, the remaining pair exactly distinguishable as graphs — HYPOTHESIS-strong, with the graph-to-physics bridge (L\_spec) and the template still open.

**(v) Empirical program (TARGET \+ ILLUSTRATIVE).** The model ladder (with electron-mass step clarified), discrete-geometry Bayes factors, held-out tests, custom-CLASS/CAMB, and the fit-free observables R\_cb \= 16/3, f\_b^{(cb)} \= 3/19, Ω\_cb \= 38/121 (nₛ imported separately) are pre-registered; an illustrative ratio-only selection gives P(16/3 | D) ≈ 1 within the discrete set but a weak discrete-versus-continuous Bayes factor (B ≈ 1.8). The honest terminus: Theorems 1, 4 PROVEN, M0 DERIVED-CONDITIONAL on a sharpened L\_clock, Gᴢ halved to g₁ ∧ g₂, the 32-face degeneracy broken in principle, and the empirical program fully specified with no real-data result asserted. Zero new fitted parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED**.

# **Epistemic Status Legend**

Table 0\. Status tags used in this paper (uppercase, bold).

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN | Theorem from standard mathematics or corpus definitions; machine-verifiable. |
| PROVEN within U1–U6 | Theorem holding under the explicitly stated coupling ansatz U1–U6 (not over all couplings). |
| DERIVED | Follows from the Z-Spin action plus PROVEN inputs; zero free parameters beyond A. |
| DERIVED-CONDITIONAL | Derived, conditional on named, independently falsifiable conditions (L\_clock-restrict, g₁, g₂). |
| IMPORTED-PROVEN | Theorem proven externally (or upstream, e.g. A20); its Z-Spin use is a separate identification. |
| LOCKED | Core constant fixed upstream (A \= 35/437, Q \= 11, (Z,X,Y) \= (2,3,6)); no downstream paper may modify. |
| TARGET-COMPUTATION | A well-posed computation not yet executed. |
| ILLUSTRATIVE | A toy/limited-scope computation demonstrating the method; a NON-CLAIM about the real quantity. |
| HYPOTHESIS-strong | Multiple independent structural anchors; promotion path documented; not yet PROVEN/DERIVED. |
| OBSERVATION | A statement of consistency with published data, not a fit. |
| OPEN | A sharply stated, falsifiable question current corpus tools cannot settle. |
| NON-CLAIM | An explicit declaration of what is not asserted. |

# **§1. Introduction and Advancement over v1.1–v1.3**

The chain ZS-A18 → A19 → A20 → A21 v1.1 (Global Parent-Charge Theorem under M0) → v1.2 (obstruction classification; single-clock selection; partial Gᴢ closure; discrete-geometry program) → v1.3 (corrections: b₁ \= 66, f\_b^{(cb)} \= 3/19, the coupling theorem scoped to U1–U6, the I\_h contradiction resolved) reaches its most stable form. The review of v1.3 noted, correctly, that further value comes not from prose but from concrete computations. Acting on that, v1.4 computed a corpus-internal invariant and v1.5 finalizes it: a graph invariant that **constrains the 32-face abundance degeneracy at the graph level** (Theorem 4, now stated as a compatibility-plus-exact-non-isospectrality result), a **sharpened L\_clock** (two falsifiable sub-lemmas), and the status corrections (the BV–BFV zero-mode wording, the coupling level k, and the electron-mass ladder).

The degeneracy result is the lead. The review observed that three distinct 32-face solids give the same abundance, so a ratio-only likelihood cannot select among them, and asked for a shape-sensitive observable. We go one step further at the graph level: the A19 seam graph requires the cold module to have b₁ \= 59, with which the icosidodecahedron (b₁ \= 29\) is incompatible — a consistency statement with A19's specification, **not an independent selection** (the value 66 is computed from that graph); and the remaining pair, the truncated icosahedron and the truncated dodecahedron, while sharing (V, E, b₁), are exactly non-isospectral by tr(L²) \= 1200 versus 1560\. The organizing question is unchanged; the new content narrows the physical-assignment residual that v1.3 left fully open, with the graph-to-physics bridge (L\_spec) named as the remaining step.

# **§2. Inherited Framework (v1.1–v1.3 recap)**

Carried unchanged: the absolute-H³ no-go on the polyhedral surface; the relative flux Hᴢ \= ι∗(∗J) classified by the relative Dixmier–Douady class in H³(Mᴢ, ∂Mᴢ; ℤ) (a bulk-trivial gerbe with a nontrivial boundary trivialization, pulled back under ι: Mᴢ → M₄); the single harmonic parent mode H⁰(Γ₃₈; ℤ) \= ℤ; the augmentation functionals εᴄ(1₃₈) \= 32, εʙ(1₃₈) \= 6 (Qᴄ : Qʙ \= 16/3); and the abundance normalization Ωᴄᵈₘ \= 32/121, Ωʙ \= 6/121 as the canonical trace τ₁₂₁(P) \= Tr P/121 on H\_ch ≅ ℂ¹²¹ (Pᴄ, Pʙ ∈ M₁₂₁(ℂ), ranks 32, 6). The locked inputs (A \= 35/437, Q \= 11, (Z,X,Y) \= (2,3,6)) introduce no parameter beyond **A** and **Q**.

# **§3. The Seam-Cohomology Obstruction Theorem (Theorem 1\)**

For a connected compact oriented 3-manifold Mᴢ with boundary and a connected finite graph Γ, Künneth (H¹(Γ) free, Tor vanishes) and Poincaré–Lefschetz duality (H³(Mᴢ, ∂Mᴢ) ≅ H₀(Mᴢ) ≅ ℤ, H²(Mᴢ, ∂Mᴢ) ≅ H₁(Mᴢ)), with H₁(Mᴢ; ℤ) \= ℤ^r ⊕ T and m \= b₁(Γ), give

H3((MZ, ∂MZ) × Γ; ℤ) ≅ ℤ ⊕ ℤmr ⊕ T⊕ m.(1)

The A19 seam graph is the truncated-icosahedron face graph (V \= 32, E \= 90, b₁ \= 59), the cube-face graph (V \= 6, E \= 12, b₁ \= 7), and one cross-edge; a bridge creates no cycle, so b₁(Γ₃₈) \= 59 \+ 7 \= 66 (E \= 103, V \= 38). **Theorem 1\.** With m \= 66, a unique integer parent charge exists **iff** H₁(Mᴢ) \= 0; otherwise each free generator opens 66 continuous channels (N\_cont \= 66r) and each torsion generator a discrete sector (T^{⊕66}); the free ranks for r \= 0, 1, 2 are 1, 67, 133\. Status: **PROVEN** (Appendix I). This identifies M0 as the exact single-parent condition and, as §8 shows, its multiplicity 66 also discriminates among the candidate cold polyhedra.

# **§4. BV–BFV Zero Modes and the Mode–Cohomology Correspondence**

A Hodge decomposition of the relative gerbe field gives the parent part, the obstruction modes of Theorem 1, and an exact remainder; the free continuous-mode count is N\_cont \= 66r and torsion gives discrete sectors T^{⊕66}. Two statuses must be kept separate. In the **abstract** abelian BF / gerbe model, these are exactly the zero modes of the boundary BV–BFV phase space (Cattaneo–Mnev–Reshetikhin): **IMPORTED-PROVEN**. Their identification with the **actual ZHCS** seam modes is a separate step, conditional on the identifications g₁ ∧ g₂ of §6: **DERIVED-CONDITIONAL on g₁ ∧ g₂** (the v1.2/v1.3 phrasing “these are exactly the zero modes” is here qualified as holding for the abstract model and conditionally for ZHCS).

# **§5. Homology-Ball Selection (Corollary 2\) and a Sharper L\_clock**

**Corollary 2 (Homology-Ball Selection).** With ∂Mᴢ \= S² and Mᴢ connected oriented, the ZHCS seam zero-mode phase space is a single continuous parent clock with no torsion sector **iff** Mᴢ is an integral homology 3-ball (M0). This is Theorem 1 combined with the standard fact that H₁ \= 0, ∂M \= S² forces a homology ball; its value is the physical reading (single-clock dynamics as a topology-selection rule). Status of the equivalence: **PROVEN** (pure-mathematics novelty moderate; mathematical-physics novelty high).

**Sharpening L\_clock.** The physics content beyond the equivalence is the lemma L\_clock — that the actual seam zero-mode phase space is rank-one and torsion-free. We factor it: **L\_clock-bulk**, that the A20 scalar kinetic matrix is rank-one with S\_cb \= 0 (this is A20's single-clock result, **IMPORTED** from A20), and **L\_clock-restrict**, that the restriction of that kinetic form to the seam boundary is rank-preserving (no extra boundary zero mode appears and none is lost). Then L\_clock \= L\_clock-bulk ∧ L\_clock-restrict, and M0 is **DERIVED-CONDITIONAL on L\_clock-restrict** (given L\_clock-bulk from A20). L\_clock-restrict is exactly a boundary BV–BFV zero-mode computation of the A19/A20 boundary action — a precise, falsifiable statement within \[11–13\], not performed here, and named as the principal mathematical-physics target. **NON-CLAIM:** M0 is not claimed derived outright.

# **§6. The Uniform Nodewise Coupling Theorem**

With the seam field a coefficient-lattice-valued relative differential character Hᴢ ∈ Ĥ³(M₄, ∂M₄; ΛΓ) and a degree-one clock character dT, the topological coupling S\_top \= 2πk ∫ Hᴢ ∪ dT reproduces the A20 parent action's topological term. Under the explicit ansatz **U1–U6** (U1 bilinear in Hᴢ and one clock character; U2 degree 3+1, first-order; U3 node-diagonal integer coefficients; U4 no background characteristic class or higher cup operation; U5 graph-edge conservation; U6 boundary counterterms modded out; **U7 k is primitive** (minimal-level sector)):

dΓ k \= 0   on connected Γ38   ⇒   kv \= k ∈ ℤ   (U1–U6);    |k| \= 1   only under U7 (primitive), k \= \+1 by orientation.(2)

**Theorem 3 (Uniform Nodewise Coupling), PROVEN within U1–U6.** The connected-graph kernel is exact, so k\_v \= k ∈ ℤ under U1–U6; the minimal level |k| \= 1 holds under U7 (large gerbe-gauge invariance alone gives only k ∈ ℤ, and primitivity gives |k| \= 1). **NON-CLAIM:** uniqueness over all local couplings (boundary counterterms, characteristic-class couplings, torsion operations, off-diagonal pairings, higher cup operations) is OPEN. Within U1–U6, g₄ (single coefficient) and g₃ (integral lattice ⇒ the augmentation pairings) are discharged, reducing Gᴢ \= g₁ ∧ g₂ ∧ g₃ ∧ g₄ to **g₁ ∧ g₂** (OPEN). C1-ID-global is **DERIVED-CONDITIONAL on M0 (← L\_clock-restrict), on g₁ ∧ g₂, and on U1–U6**.

# **§7. The Augmentation: a \= b from Connectedness, not I\_h**

The 32 truncated-icosahedron faces split into two I\_h orbits (12 pentagons, 20 hexagons), so the I\_h-invariant integer functionals on the cold module are **two-dimensional**, ε\_{a,b}(v) \= a·Σ\_pent v\_i \+ b·Σ\_hex v\_j; I\_h alone does not force a \= b. What forces a \= b \= k is the full 38-node graph-edge conservation (§6, dΓ k \= 0\) with graph connectedness — a single coefficient over all 38 nodes — so εᴄ(1₃₈) \= 12 \+ 20 \= 32 and εʙ(1₃₈) \= 6, giving Qᴄ : Qʙ \= 16/3. The uniqueness rests on connectedness and U1–U6, tying §7 to Theorem 3\. Status: ratio **DERIVED-CONDITIONAL on g₁ ∧ g₂ and U1–U6** (mathematics PROVEN under M0).

# **§8. Constraining the 32-Face Abundance Degeneracy (Theorem 4\)**

Three solids realize 32 faces and hence the abundance Ω\_cdm \= 32/121 identically: the truncated icosahedron (12 pentagons \+ 20 hexagons), the truncated dodecahedron (20 triangles \+ 12 decagons), and the icosidodecahedron (20 triangles \+ 12 pentagons). A cosmological likelihood that uses only the abundance ratio is therefore **polyhedron-blind**. Two corpus-internal observables break the degeneracy.

Table 1\. The three 32-face solids and their cold-module (face-adjacency) graphs; tr(L²) \= Σdᵢ² \+ 2E is exact (Appendix I).

| Solid (cold module) | Faces | Face graph (V, E, b₁) | seam b₁ | tr(L²) |
| ----- | ----- | ----- | ----- | ----- |
| truncated icosahedron | 12 pent \+ 20 hex | (32, 90, 59\) | 66 | 1200 |
| truncated dodecahedron | 20 tri \+ 12 decagon | (32, 90, 59\) | 66 | 1560 |
| icosidodecahedron | 20 tri \+ 12 pent | (32, 60, 29\) | 36 (≠ 66\) | 600 |

**Theorem 4 (Polyhedral Graph-Discrimination).** (i) **Topological compatibility:** the cold-module face graph has b₁ \= 59 for the truncated icosahedron and the truncated dodecahedron but b₁ \= 29 for the icosidodecahedron; hence the icosidodecahedron is **incompatible with the A19-fixed seam graph**, which has b₁(Γ₃₈) \= 66 (= 59 \+ 7\) — the icosidodecahedron would force seam b₁ \= 36\. This is a **consistency statement with A19's already-truncated-icosahedron specification, not an independent selection theorem**: the value 66 is itself computed from the A19 graph, so it cannot, on its own, independently select that graph. A genuine selection would require b₁ \= 66 to be fixed independently of the polyhedron choice (e.g. by an action zero-mode count, by L\_clock, by an observable mode multiplicity, or by an upstream symmetry theorem). (ii) **Spectral non-isospectrality (exact):** the truncated icosahedron and truncated dodecahedron have identical (V, E, b₁) \= (32, 90, 59\) face graphs but different Laplacians, proven without floating point by the integer invariant tr(L²) \= Σdᵢ² \+ 2E: for the truncated icosahedron (12 pentagons of degree 5, 20 hexagons of degree 6\) tr(L²) \= 12·25 \+ 20·36 \+ 180 \= 1200, while for the truncated dodecahedron (20 triangles of degree 3, 12 decagons of degree 10\) tr(L²) \= 20·9 \+ 12·100 \+ 180 \= 1560; 1200 ≠ 1560\. Status: (i) **PROVEN** (a compatibility statement, not a selection); (ii) **PROVEN** (exactly non-isospectral; Appendix I).

**Physical realization, lemma L\_spec, and status.** The discriminator is a graph invariant; its physical relevance requires a bridge we state as an open lemma. **L\_spec:** the linearized ZHCS seam quadratic action has the form S⁽²⁾ \= ½ ∫ dη \[ φ̇ᵀ K φ̇ − φᵀ(ω₀² I \+ α L\_Γc) φ \], so that its boundary Hessian contains the cold-module Laplacian L\_Γc with a fixed coefficient α; then the mode frequencies are ωⱼ² \= ω₀² \+ αλⱼ for the graph eigenvalues λⱼ, and the truncated-icosahedron and truncated-dodecahedron spectra induce distinct seam-mode spectra and hence distinct shape-sensitive perturbation/isocurvature templates. The explicit status ladder is therefore: graph non-isospectrality **PROVEN** (Theorem 4(ii)); the graph spectrum equals the ZHCS mode spectrum **HYPOTHESIS / TARGET** (this is L\_spec, requiring the explicit linearized boundary action); the CMB template **TARGET-COMPUTATION**. The rank-ratio likelihood (§10) tests the rank pair 32 : 6 but is polyhedron-blind. The upstream ZS-F2/A19 structure (the 12/20 pentagon–hexagon orbit assignment, the C₆₀ fullerene realization, |I\_h| \= 120 \= Q² − 1\) selects the truncated icosahedron among the two. The physical-assignment residual is thereby narrowed from a three-fold degeneracy that v1.3 left fully open to: the icosidodecahedron **incompatible with the A19 specification**, and the remaining pair **exactly distinguishable as graphs** — still HYPOTHESIS-strong (upstream selects the truncated icosahedron), with the graph-to-physics bridge L\_spec and the template realization the remaining open steps.

# **§9. The Equivariant Seam Complex (remark)**

Equivariant bundle gerbes and equivariant differential cohomology exist externally and are not novel here. The object whose construction would be new is the total complex H³\_{seam,G}(Mᴢ, ∂Mᴢ; Γ, Λ) combining relative differential cohomology, the finite-graph cochain complex, the coefficient lattice, the I\_h/O\_h action, and BV–BFV gluing; its target properties (subdivision invariance, additivity under seam gluing, naturality under graph refinement, the equivariant augmentation's universal property, functoriality of the obstruction group, and an unrestricted differential-cohomology coupling classification) are stated as a **CONJECTURE** within the BV–BFV/cellular-BF frameworks. Status: **OPEN** (a documented extension; the pure-mathematics 9-point target). It is flagged so the paper is not read as asserting a gluing theorem it has not proven.

# **§10. The Discrete-Geometry Likelihood Program (folded ZS-A22 scope)**

The empirical paper is folded here to limit paper proliferation; every execution is declared TARGET. The model ladder isolates which lock drives any result, with sampled parameters specified per row. The electron-mass step is clarified: mₑ(z)/mₑ(0) \= 1 is the standard recombination value, so to make the lock non-vacuous M\_N **frees** the electron-mass ratio as a sampled parameter and M\_Z **fixes** it to 1 (M\_Z is then a proper nested restriction of M\_N, testing whether ZS-C's prediction of no electron-mass variation is preferred). In M\_R only the ratio is fixed, so one absolute-density parameter ω\_cb \= ω\_c \+ ω\_b is sampled, with ω\_b \= (3/19)ω\_cb, ω\_c \= (16/19)ω\_cb.

Table 2\. The pre-registered model ladder (each compared to the public Planck 2018 ΛCDM baseline).

| Model | Fixed condition | Sampled cosmological parameters |
| ----- | ----- | ----- |
| MΛ | none (baseline) | ω\_b, ω\_cdm, θ\_s, τ, Aₛ, nₛ (standard six) |
| M\_R | ω\_c/ω\_b \= 16/3 | ω\_cb, θ\_s, τ, Aₛ, nₛ |
| M\_F | Ω\_b \= 6/121, Ω\_c \= 32/121 | h, τ, Aₛ, nₛ |
| M\_N | M\_F \+ nₛ \= 0.9674; electron mass free | h, τ, Aₛ, mₑ(z)/mₑ(0) |
| M\_Z | full ZS-C (M\_N \+ mₑ(z)/mₑ(0) \= 1\) | h, τ, Aₛ (residual only) |

This yields the separated increments Δχ²\_R, Δχ²\_F, Δχ²\_N, Δχ²\_Z and, by the M\_N → M\_Z step, an isolated test of the electron-mass branch. The discrete-geometry test reframes the anti-numerology question (§14) on the data side: pre-register the candidate ratio set R\_geom from the admissible polyhedra (symmetry group, sector dimension, orbit structure, rank limits, degeneracy handling, and prior weight all fixed before unblinding), run a restricted cosmology at each ratio r, and compute

P(r | D) \= Zr πr / Σr' Zr' πr',    Bgeom,Λ \= Zdisc / ZΛCDM,    Bgeom,cont \= Zdisc / Zcont.(3)

**Illustrative ratio-only result (NON-CLAIM).** Treating Planck Ω\_c/Ω\_b \= 5.36 ± 0.065 as a single Gaussian datum over the 16 distinct natural polyhedral ratios (equal priors) against a continuous-ratio model (flat prior on \[3, 8\]): within the discrete set P(16/3 | D) ≈ 1.000 (the next ratio is ≈14σ away), but the discrete-versus-continuous Bayes factor is only B ≈ 1.8 (weak), and the 32-face count alone is degenerate. **ILLUSTRATIVE only** — the rank-ratio likelihood tests 32 : 6 but, by Theorem 4, is polyhedron-blind; the polyhedron identity needs the seam-mode spectral template. The real Planck/ACT/DESI Bayes factors of (3) and the spectral-template test are **TARGET-COMPUTATIONS**; no observational support is claimed.

# **§11. Held-Out Prediction and Fit-Free Observables**

The fit-free outputs that follow exactly from the charge theorem are the three rationals

Rcb \= Ωc/Ωb \= 16/3,    fb⁽ᶜᵇ⁾ \= Ωb/(Ωc\+Ωb) \= 6/38 \= 3/19,    Ωcb \= 38/121.(4)

The spectral tilt nₛ \= 0.9674 is **separate**: not a rational, not from the charge theorem, but an upstream prediction imported from ZS-U1. It is essential to write Ω\_cb, **not** Ω\_m: a massive-neutrino contribution makes the total matter density depart from 38/121. For predictive power we pre-register a calibration/validation split: estimate {h, τ, Aₛ} on D\_train \= Planck TT \+ lowE, freeze, and predict D\_test \= {Planck TE/EE, Planck lensing, ACT DR6, DESI DR2 BAO, BBN ω\_b}, reporting per-set Δχ²\_pred, ELPD, and posterior-predictive p-values. BBN constrains ω\_b independently of the CMB; cluster gas-fraction tests of f\_b^{(cb)} carry large feedback/depletion systematics and serve only as secondary robustness. The held-out evaluations are **TARGET-COMPUTATIONS**; the present comparison of (4) to published central values (Ω\_c h²/Ω\_b h² ≈ 5.36) is an **OBSERVATION** of consistency, not a fit.

# **§12. Custom-CLASS and Cross-Code Verification**

The continuum dust is term-by-term the Ma–Bertschinger CDM system (a fluid integrator reproduces standard CDM to machine precision while controls diverge; the full generalized-dark-matter control with the entropy term −3ℋcₛ²δ deviates 7.4% at η \= 50, Appendix I). The closure replaces the cdm species in CLASS by an independent zhcs species (Ωᴄᵈₘ \= 0, Ωᴢₕᴄₛ \= 32/121) and cross-checks against unmodified CLASS and CAMB at the same restricted parameters, requiring max over ℓ of |Cℓ^{ZHCS} − Cℓ^{CDM}| below tolerance. Gates B0–B8 use the numerically stabilized norms. Passing yields VERIFIED-IN-FULL-BOLTZMANN; the compiled run is a **TARGET-COMPUTATION** and a confirmation-of-implementation, not a new observable.

# **§13. Falsification Gates**

Table 3\. Multilayer falsification gates for ZS-A21 v1.4.

| Gate | Trigger (immediate rejection) |
| ----- | ----- |
| G-A21.1 | Γ₃₈ disconnected, or its edge set differs from A19's one-cross-edge construction so that b₁ ≠ 66 ⇒ the obstruction count and Theorem 1 change. |
| G-A21.2 | L\_clock-restrict false (the boundary restriction of the A20 kinetic form is not rank-preserving) ⇒ M0 is not selected; v1.1's conditional theorem holds but M0 reverts to an assumption. |
| G-A21.3 | A block-dependent topological coefficient survives within U1–U6 (dΓ k ≠ 0 admissible) ⇒ Theorem 3 and the 32 : 6 split fail. |
| G-A21.4 | g₁ (compact gerbe connection) or g₂ (relative trivialization) fails ⇒ flux quantization / relative class fails. |
| G-A21.5 | (§8) L\_spec fails (the linearized ZHCS boundary Hessian does not contain the cold-module Laplacian), or the data prefer the icosidodecahedron (incompatible with the A19 seam graph, seam b₁ \= 36 ≠ 66), or the truncated-dodecahedron tr(L²) \= 1560 template fits better than the truncated-icosahedron tr(L²) \= 1200 ⇒ the graph-discrimination program (Theorem 4\) fails. |
| G-A21.6 | Any of B1–B5 fails, or CLASS–CAMB disagree beyond tolerance ⇒ implementation or continuum dictionary fails. |
| G-A21.7 | (§10–11) Model ladder shows p\_restrict \< 0.05 for M\_F, or a repeated \> 3σ held-out residual in independent ACT/DESI/BBN ⇒ the abundance lock is rejected. |

# **§14. Anti-Numerology**

The theorems require no Monte Carlo: H³\_seam with m \= 66 (Theorem 1), the connected-graph kernel of dimension b₀ \= 1 (Theorem 3), the augmentation values 32, 6, and the polyhedron b₁ and spectra (Theorem 4\) are exact. The audited freedom is the physical polyhedron assignment; Theorem 4 now narrows it (the icosidodecahedron is incompatible with the A19 seam graph; the remaining pair is exactly non-isospectral, tr(L²) \= 1200 vs 1560), so the residual freedom is smaller than in v1.3. The enumeration over the natural face-count menu (63 cold×baryon pairs, 16 distinct ratios) shows the Planck-consistent ratio is uniquely 16/3; the rank **values** 32, 6 are PROVEN, the **assignment** HYPOTHESIS-strong. The discrete-geometry program (§10) plus the spectral template (§8) is the data-side completion. The released script reproduces the enumeration, the illustrative selection, and the polyhedron spectra.

# **§15. Open Residuals and Conclusion**

Table 4\. Honest open residuals carried by ZS-A21 v1.4 (declared, not closed).

| Residual | Statement and path |
| ----- | ----- |
| L\_clock-restrict | That the A20 kinetic form restricts rank-preservingly to the seam boundary; with L\_clock-bulk (IMPORTED from A20) it gives M0 (Corollary 2). Needs a BV–BFV zero-mode computation of the A19/A20 boundary action. OPEN — the principal target. |
| g₁ ∧ g₂ | The two surviving Gᴢ identifications (compact gerbe connection; relative trivialization). OPEN (reduced from four within U1–U6). |
| Unrestricted coupling classification | Whether boundary counterterms, characteristic-class couplings, torsion operations, off-diagonal pairings, or higher cup operations evade U1–U6. OPEN. |
| Physical assignment (TI vs TD) | The icosidodecahedron is incompatible with the A19-fixed seam graph (Theorem 4(i); a compatibility statement, not an independent exclusion); the truncated icosahedron vs truncated dodecahedron is exactly distinguished as graphs by tr(L²) \= 1200 vs 1560\. HYPOTHESIS-strong (upstream selects the truncated icosahedron). |
| L\_spec (graph → physics) | That the linearized ZHCS boundary Hessian contains the cold-module Laplacian L\_Γc with a fixed coefficient (ωⱼ² \= ω₀² \+ αλⱼ), making the graph spectrum a physical mode spectrum and a CMB template. HYPOTHESIS / TARGET — the bridge that would make Theorem 4(ii) observational. |
| Equivariant total complex | Subdivision/gluing/functoriality and the unrestricted classification (§9); CONJECTURE, the pure-mathematics 9-point target. |
| Empirical runs | Model ladder, discrete-geometry Bayes factors, held-out predictions, custom-CLASS/CAMB, the spectral-template test. TARGET-COMPUTATIONS; no real-data result claimed. |

ZS-A21 v1.5 keeps the corrected, stable base of v1.3–v1.4 and tightens the new result to exactly what is proven. Theorem 1 classifies the seam obstruction (m \= 66); Corollary 2 reads single-clock dynamics as the topology-selection rule giving M0, DERIVED-CONDITIONAL on the sharpened L\_clock \= L\_clock-bulk ∧ L\_clock-restrict; the Uniform Nodewise Coupling Theorem discharges g₃, g₄ within U1–U6 (with k ∈ ℤ under U1–U6 and |k| \= 1 under U7), halving the open conjunction to g₁ ∧ g₂; and the **Polyhedral Graph-Discrimination Theorem (Theorem 4\)** constrains the 32-face abundance degeneracy at the graph level — the icosidodecahedron is **incompatible with the A19-fixed seam graph** (a compatibility statement, not an independent selection), and the truncated icosahedron and truncated dodecahedron are **exactly non-isospectral** by the integer invariant tr(L²) \= 1200 versus 1560 — with the bridge to a physical mode spectrum named as the open lemma L\_spec. The ledger is a stable fixed point: each theorem is PROVEN or PROVEN-within-a-stated-ansatz, each physical bridge is a named falsifiable condition (L\_clock-restrict, L\_spec, g₁, g₂), and every computational debt is declared. **This is the terminal text version of ZS-A21:** the remaining value is gated entirely on the actual computations — a BV–BFV zero-mode proof of L\_clock-restrict, the explicit linearized boundary action proving L\_spec, the action-level g₁ ∧ g₂, the compiled custom-CLASS/CAMB, and the Planck/ACT/DESI/BBN likelihood — none of which is a text revision. Two minor design refinements are deferred to those computational releases: a 2×2 factorial electron-mass ladder (separating the nₛ lock from the electron-mass freedom) and a three-way split of L\_clock-bulk into a cosmological-rank statement and a cosmology-to-BFV dictionary. Zero new fitted parameters; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) **LOCKED**.

# **Acknowledgements & Code Availability**

This paper consolidates internal Z-Spin Collaboration deep-exploration notes following ZS-A21 v1.3 and incorporates an internal review that affirmed v1.3 as the stable base and located the next value in concrete computation. Acting on that, v1.4–v1.5 contribute the Polyhedral Graph-Discrimination Theorem (Theorem 4\) and a sharpened L\_clock. The 28 computational checks of Appendix I are reproduced by the released script zs\_a21\_verify.py (NumPy/SciPy): the one-cross-edge 38-node graph (b₁ \= 66); relative cohomology under M0; the Seam-Obstruction free ranks 1, 67, 133 and torsion decomposition; the connected-graph gradient kernel; the I\_h two-orbit augmentation; the 121-dimensional trace; the full-GDM fluid isomorphism; the illustrative ratio-only selection; and the three 32-face polyhedra with their cold-module face graphs (b₁ \= 59, 59, 29\) and Laplacian spectra (truncated icosahedron versus truncated dodecahedron exactly non-isospectral, tr(L²) \= 1200 vs 1560). Only this verification script is released now; the compiled custom-CLASS/CAMB pipeline, the clik/Cobaya likelihood, the held-out tests, and the seam-mode spectral template are **future** releases tied to their TARGET runs. This work used AI tools (Anthropic Claude) for verification and drafting; the author assumes full responsibility.

# **Appendix**

## **A. Relative homology and M0**

For (Δ³, ∂Δ³): chain ranks (4,6,4,1), boundary through dimension 2, so H₃(Δ³, ∂Δ³; ℤ) \= ℤ, H≤₂ \= 0; dually H³(B³, S²; ℤ) \= ℤ, H³(B³; ℤ) \= 0\. Under M0 the same holds for Mᴢ, with H²(Mᴢ, ∂Mᴢ; ℤ) ≅ H₁(Mᴢ; ℤ) \= 0\.

## **B. The 38-node seam graph (b₁ \= 66\)**

Truncated-icosahedron vertices are even (cyclic) sign-permutations of (0, ±1, ±3φ), (±1, ±(2+φ), ±2φ), (±φ, ±2, ±(2φ+1)); coplanar facet merging gives 12 pentagons \+ 20 hexagons (32 faces, 90 edges, χ \= 2), face graph connected with b₁ \= 59\. The cube-face graph has 6 nodes, 12 edges, b₁ \= 7\. A19's single cross-edge (a bridge) gives the connected 38-node graph: E \= 103, Laplacian rank 37, b₀ \= 1, **b₁ \= 66 \= 59 \+ 7** — the obstruction multiplicity m. (The coupling-uniqueness kernel of Theorem 3 is the gradient kernel dimension b₀ \= 1, independent of b₁.)

## **C. Künneth and the obstruction (Theorem 1\)**

H³((Mᴢ,∂Mᴢ)×Γ) \= H³(Mᴢ,∂Mᴢ)⊗H⁰(Γ) ⊕ H²(Mᴢ,∂Mᴢ)⊗H¹(Γ) (Tor vanishes, H¹(Γ) free). With H³(Mᴢ,∂Mᴢ) \= ℤ, H²(Mᴢ,∂Mᴢ) \= H₁(Mᴢ) \= ℤ^r ⊕ T, H¹(Γ₃₈) \= ℤ^{66}: H³\_seam \= ℤ ⊕ ℤ^{66r} ⊕ T^{⊕66}. Free ranks at r \= 0,1,2 → 1, 67, 133\.

## **D. BV–BFV zero modes and L\_clock**

In the abstract abelian BF/gerbe model the boundary BV–BFV zero modes are the relative-cohomology classes (IMPORTED-PROVEN); the continuous-mode count 66r and discrete torsion sectors follow from §4. L\_clock \= L\_clock-bulk (A20 rank-one kinetic matrix, IMPORTED) ∧ L\_clock-restrict (rank-preserving boundary restriction); the latter is a precise BV–BFV zero-mode statement within \[11–13\], not proven here, and is the principal open target.

## **E. Differential-character coupling (Theorem 3, within U1–U6)**

Under U1–U6: S\_top \= 2πk ∫ Hᴢ ∪ dT; large-gauge invariance quantizes |k| \= 1 (k \= \+1 by orientation), dΓ k \= 0 on connected Γ₃₈ forces k\_v \= k. The unrestricted classification is OPEN; g₃, g₄ follow within the ansatz.

## **F. Custom-CLASS species**

Newtonian: δ′ \= −θ \+ 3Φ′, θ′ \= −ℋθ \+ k²Ψ; synchronous: δ′ \= −θ − ½ h′, θ′ \= −ℋθ, with θᴢₕᴄₛ \= 0 after cdm removal. Gates B0–B8 with stabilized norms; the future release bundle will include the CLASS fork, the CAMB cross-check, YAML, and git commit.

## **G. Discrete-geometry illustrative selection**

Data Ω\_c/Ω\_b \= 5.36 ± 0.065 (Gaussian, illustrative). The 16 distinct natural ratios {12,20,32,62}/{6,8,14,26}; only 32/6 \= 5.333 lies within 1σ (next nearest 4.43, ≈14σ). Equal-prior posterior P(16/3|D) ≈ 1.000; continuous-ratio Bayes factor B ≈ 1.8 (weak). Real Cℓ Bayes factors are TARGET; by Theorem 4 the ratio is polyhedron-blind.

## **H. Polyhedral graph-discrimination (Theorem 4\)**

The three 32-face solids, built from canonical coordinates and convex-hull face extraction: truncated icosahedron (60 vertices; 12 pentagons \+ 20 hexagons), truncated dodecahedron (60 vertices; 20 triangles \+ 12 decagons), icosidodecahedron (30 vertices; 20 triangles \+ 12 pentagons). Their cold-module face-adjacency graphs have (V, E, b₁) \= (32, 90, 59), (32, 90, 59), (32, 60, 29); seam b₁ \= b₁ \+ 7 \= 66, 66, 36, so the icosidodecahedron is incompatible with the A19-fixed seam graph (b₁ \= 36 ≠ 66). For the remaining pair, non-isospectrality is exact via tr(L²) \= Σdᵢ² \+ 2E (since tr(D A) \= 0 and tr(A²) \= 2E): truncated icosahedron 12·5² \+ 20·6² \+ 2·90 \= 1200, truncated dodecahedron 20·3² \+ 12·10² \+ 2·90 \= 1560 (icosidodecahedron 20·3² \+ 12·5² \+ 2·60 \= 600); 1200 ≠ 1560, no floating point. The numerically computed λ\_max (8.39 versus 12.29) is a consistency cross-check.

## **I. Verification ledger (28/28)**

(A) topology, one-cross-edge graph b₁ \= 66; (B) relative cohomology under M0; (C) Künneth single parent; (D) augmentation 32/6; (E) 121-dim trace; (F) full-GDM fluid (perfect dust ≡ CDM; imperfect 7.4%); (H) Seam-Obstruction free ranks 1/67/133 and T^{⊕66}; (I) connected-graph kernel \= b₀ \= 1, |k| \= 1, the I\_h two-orbit functional and a \= b from connectedness; (J) discrete-geometry toy P(16/3) ≈ 1, B ≈ 1.8; (K) polyhedron-identity — 32 faces all (ratio-blind), seam b₁ \= 66/66/36 (icosidodecahedron excluded), truncated icosahedron versus truncated dodecahedron non-isospectral; and the fit-free observables 16/3, 3/19, 38/121. Total 28/28 PASS.

# **References**

\[1\] K. Kang, ZS-F2 / ZS-F5 (Z-Spin Collaboration, 2026): A \= 35/437; (Z,X,Y) \= (2,3,6), Q \= 11\.

\[2\] K. Kang, ZS-A18 v1.5 (2026): massless-Goldstone recombination-CDM no-go.

\[3\] K. Kang, ZS-A19 v3.1 (2026): ZHCS boundary-tension dust; Ω\_cdm \= 32/121; 38-node seam graph (one cross-edge).

\[4\] K. Kang, ZS-A20 v2.0 (2026): continuum closure; C1-ID-global; ZS-C / ZS-0; single-clock adiabaticity.

\[5\] B. Eckmann, Comment. Math. Helv. 17, 240 (1944). (Combinatorial Hodge theory on a complex.)

\[6\] X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, Math. Program. 127, 203 (2011); arXiv:0811.1067.

\[7\] L.-H. Lim, SIAM Rev. 62, 685 (2020); arXiv:1507.05379. (Hodge Laplacians on graphs.)

\[8\] M. K. Murray, J. London Math. Soc. 54, 403 (1996); arXiv:dg-ga/9407015. (Bundle gerbes.)

\[9\] J. Dixmier, A. Douady, Bull. Soc. Math. France 91, 227 (1963). (The Dixmier–Douady class.)

\[10\] U. Bunke, T. Nikolaus, M. Völkl, J. Homotopy Relat. Struct. 11, 1–66 (2016); arXiv:1311.3188; doi:10.1007/s40062-014-0092-5.

\[11\] A. S. Cattaneo, P. Mnev, N. Reshetikhin, Commun. Math. Phys. 357, 631 (2018); arXiv:1507.01221. (BV–BFV on manifolds with boundary.)

\[12\] A. S. Cattaneo, P. Mnev, N. Reshetikhin, Commun. Math. Phys. 332, 535 (2014); arXiv:1201.0290. (Classical BV theories on manifolds with boundary.)

\[13\] A. S. Cattaneo, P. Mnev, N. Reshetikhin, Commun. Math. Phys. 374, 1229 (2020); arXiv:1701.05874. (A cellular topological field theory.)

\[14\] J. D. Brown, Class. Quantum Grav. 10, 1579 (1993); arXiv:gr-qc/9304026.

\[15\] J. D. Brown, K. V. Kuchař, Phys. Rev. D 51, 5600 (1995); arXiv:gr-qc/9409001.

\[16\] S. Weinberg, Phys. Rev. D 67, 123504 (2003); arXiv:astro-ph/0302326. (Adiabatic mode.)

\[17\] C.-P. Ma, E. Bertschinger, Astrophys. J. 455, 7 (1995); arXiv:astro-ph/9506072.

\[18\] D. Blas, J. Lesgourgues, T. Tram, JCAP 07, 034 (2011); arXiv:1104.2933. (CLASS.)

\[19\] A. Lewis, A. Challinor, A. Lasenby, Astrophys. J. 538, 473 (2000); arXiv:astro-ph/9911177. (CAMB.)

\[20\] J. Torrado, A. Lewis, JCAP 05, 057 (2021); arXiv:2005.05290. (Cobaya.)

\[21\] Planck Collaboration, Astron. Astrophys. 641, A6 (2020); arXiv:1807.06209.

\[22\] ACT Collaboration (T. Louis et al.), arXiv:2503.14452 (2025). (ACT DR6.)

\[23\] DESI Collaboration, arXiv:2503.14738 (2025). (DESI DR2 BAO.)

\[24\] Y. Toda, O. Seto, arXiv:2508.09025 (2025): varying electron mass under ACT DR6 \+ DESI DR2.

\[25\] R. Trotta, Contemp. Phys. 49, 71–104 (2008); arXiv:0803.4089. (Bayesian inference and model selection in cosmology.)

\[26\] C. Pitrou, A. Coc, J.-P. Uzan, E. Vangioni, Phys. Rep. 754, 1–66 (2018); arXiv:1801.08023. (Precision big-bang nucleosynthesis.)

# **Version History**

v1.5 (June 2026): Terminal text version — honesty/precision finalization of v1.4 (no new physics program). (1) Theorem 4 renamed **Polyhedral Graph-Discrimination** (from “Polyhedron-Identity”, which over-stated physical identity). (2) Theorem 4(i) reframed as a **compatibility statement** with the A19-fixed seam graph (the icosidodecahedron is incompatible, seam b₁ \= 36 ≠ 66), **not an independent exclusion**, since b₁ \= 66 is itself computed from that graph. (3) Theorem 4(ii) non-isospectrality made **exact** via tr(L²) \= Σdᵢ² \+ 2E \= 1200 (truncated icosahedron) vs 1560 (truncated dodecahedron), removing floating-point dependence. (4) The graph→physics bridge named as the open lemma **L\_spec** (the boundary Hessian contains the cold-module Laplacian; ωⱼ² \= ω₀² \+ αλⱼ), with the status ladder graph-non-isospectrality PROVEN / graph=mode-spectrum HYPOTHESIS-TARGET / CMB-template TARGET. (5) Theorem 3 level split: k ∈ ℤ under U1–U6; |k| \= 1 under the added primitivity assumption U7. Deferred minor refinements: a 2×2 factorial electron-mass ladder and a three-way split of L\_clock-bulk. Verification 28/28 (the spectral check is now the exact integer invariant). Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

v1.4 (June 2026): Value-leading extension of the corrected v1.3 base. New: **Theorem 4 (introduced as Polyhedron-Identity Discrimination; renamed Polyhedral Graph-Discrimination in v1.5)** constrains the 32-face abundance degeneracy — the three 32-face solids (truncated icosahedron, truncated dodecahedron, icosidodecahedron) give identical 32/121, but the cold-module face graph has b₁ \= 59, 59, 29, so the icosidodecahedron is incompatible with the A19 seam graph, and the remaining pair, though sharing (V,E,b₁) \= (32,90,59), is non-isospectral (made exact in v1.5: tr(L²) \= 1200 vs 1560), giving a shape-sensitive graph discriminator (physical bridge L\_spec, template realization TARGET). L\_clock is sharpened into L\_clock-bulk (IMPORTED from A20) ∧ L\_clock-restrict (a rank-preserving boundary-restriction BV–BFV statement, the principal target). Corrections: §4 split into abstract BF/gerbe IMPORTED-PROVEN versus ZHCS DERIVED-CONDITIONAL on g₁ ∧ g₂; the model ladder's electron-mass step clarified (M\_N frees mₑ(z)/mₑ(0), M\_Z fixes it to 1, a proper nested restriction); the physical-assignment residual rewritten per Theorem 4\. Verification 28/28. Zero new fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

v1.3 (June 2026): Error-correction of v1.2 — b₁(Γ₃₈) \= 66 (one cross-edge; ranks 1,67,133 and T^{⊕66}); baryon fraction f\_b^{(cb)} \= 3/19 (19/3 was the inverse loading), nₛ separated as imported; Corollary 2 (renamed from Theorem 2); Uniform Nodewise Coupling Theorem PROVEN within U1–U6 with |k| \= 1; §7 contradiction resolved (a \= b from connectedness, not I\_h); model-ladder sampled-parameter column; release phrasing corrected. Verification 25/25.

v1.2 (June 2026): Seam-Cohomology Obstruction Theorem; single-clock selection of M0; action-level partial closure of Gᴢ; discrete-geometry program with fit-free observables and an illustrative ratio-only selection. (Superseded numerics: b₁ \= 67, f\_b \= 19/3.)

v1.1 (June 2026): Assumption M0 (theorem PROVEN under M0); coefficient-lattice augmentation; 121-dimensional channel notation; bulk-trivial gerbe with boundary trivialization and pullback; Gᴢ as a four-condition conjunction; full-GDM fluid (7.4%).