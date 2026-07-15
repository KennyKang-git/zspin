**ZS-F33**

**The Conditional UV Reduction of the Z-Spin Odd Three-Form: Wilson Phase–Flux Transgression, Complete Cellular-Seam Classification, and the Charge-Unit Obstruction to the Absolute Vacuum Scale**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Collaboration

**Date:** May 2026 (v1.8, closure and integration update)

**Paper code:** ZS-F33 · v1.8   ·   Theme: Foundations / UV Gauge Reduction / Cosmological B3 (ZS-A31 consolidated)

**Verification:** 31 registered results, with three load-bearing statuses lowered to match what is actually proven. The verification suite is reclassified into 19 ASSERT-COMPUTED checks (which can fail — incidence, Betti, the full Δ₁ spectrum, the complete 48-automorphism / 20-involution cellular-seam classification with its finite torsion image, the Wilson polar-line phase), 4 IDENTITY-REPORTED checks (definitional identities such as q \= λ\*), 1 IMPORTED-PROVEN theorem (Cauchy uniqueness), and 3 STRUCTURAL-ASSUMPTION declarations (kept out of the pass count). New results: the even-dimensional seam-parity counterexample (ln T₋ \= ln 4), the Wilson polar-line derivation of e^(iω), the flux-gluing exponential uniqueness σ \= e^x, and the Charge-Unit Obstruction  |  Zero new fitted parameters  |  (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**

# **§0. Abstract**

This is the revised UV-reduction sequel to ZS-F32, consolidating the cosmological hand-off scoped as ZS-A31. The title is deliberately weakened from “UV completion”: we do not specify the odd gauge group, representation, charge lattice, or full BV master action, so what is delivered is a *conditional reduction* — a localization of the odd vacuum carrier and a decomposition of its obstructions — not a completion. F32 reduced the absolute scale to one susceptibility through ρΛ,Z \= ½ *χ*₋ ω², with **ω** \= arg λ\* \= 2.2592495540 and ω²/2 \= 2.5521042734, leaving θZ \= ω, β₊₋ \= 0, and *χ*₋ open. We do not close B3.

Five results, each split into its honest components. (i) **Equivariant-torsion localization** (F33.1): the standard closed even-dimensional Ray–Singer carrier is excluded (IMPORTED-PROVEN), its application to the 2D Z-sector is DERIVED-CONDITIONAL, and *odd-dimensional uniqueness is now CLOSED-NEGATIVE* — the 2D seam-parity-restricted determinant torsion ln T₋ \= ln 4 ≠ 0 is an explicit counterexample, so a nonzero odd functional does not force an odd-dimensional carrier. (ii) **Wilson phase–flux transgression** (F33.2): the holonomy θZ \= ω is DERIVED-under-WPL, repairing a v1.6 error. A flat connection has c₁ \= 0 and cannot be the degree-1 theta line, so v1.7 *separates* a flat Wilson polar-line L\_W (c₁ \= 0, holonomy e^(iω) \= λ\*/|λ\*| read from the polar unitary part of the linearized mediation operator) from the theta line Θ\_Z (c₁ \= 1, fibre flux). The Koenigs quotient ℂ\*/⟨λ\*⟩ IS an elliptic curve (PROVEN) and a natural fibre candidate, but the physical fibre need only carry a normalized degree-1 class, so “Z \= E\_λ\*” is DERIVED-CONDITIONAL and q \= λ\* is a definitional identity. (iii) An **eighth-power scaling classification** (F33.3): the dimensional law is DERIVED; E\* \= v is a rejected benchmark; the blind benchmark ρΛ¹ᐟ⁴ \= 2.48 × 10⁻⁵ eV remains 90× short. (iv) A **BRST-Only Isolation No-Go** (F33.4A) — gauge invariance and seam parity alone *cannot* forbid the mixed operators F₋²R, F₋²F₊². The v1.6 claim that ∫F₄ is a nontrivial local H⁰'⁴(s|d) class is *retracted* (it is d-exact); v1.7 instead writes a two-four-form sequestering action with the corpus F±, whose abelian-ghost-tower BV master equation reduces to d² \= 0 (DERIVED-CONDITIONAL), and pins the gluing functions by the exponential-uniqueness theorem σ \= e^x. (v) The spectral no-go is upgraded to a **complete cellular-seam classification** (F33.5): 48 cellular automorphisms, 20 involutions, seam-odd torsion image {−3,0,1,3⁄2,2,5⁄2}·ln 2, disjoint from the back-solved target — exact for all cellular involutions on this complex. The frozen top-form gives w \= −1 (IMPORTED-PROVEN); the dynamical-w branch is CLOSED-NEGATIVE under the minimal action. Finally, the absolute value: the three registered routes are exhausted (CLOSED-NEGATIVE-under-R1–R3), and the **Charge-Unit Obstruction** explains why — flux integrality fixes the flux number k but not the dimensionful unit e₋²/Z₋, so (A, Q) and topology alone cannot determine χ₋. The absolute scale in a broader UV theory is OPEN. This is the honest content of conditional reduction: the structure is derived, the absolute scale is provably beyond (A, Q) plus topology.

The computational center of the paper is F33.5, *now a complete classification*. We construct the full truncated-octahedron BCC T³ quotient explicitly — incidence matrices ∂₁, ∂₂ reproducing Δ₁ \= {0³, 4³, 6², 8³, 12¹} and Betti (1, 3, 3, 1\) — and enumerate its entire signed cellular automorphism group: 48 automorphisms (= |Oh|), 20 order-2 seam involutions. For every involution we compute the seam-odd determinant torsion; the image is the finite signed half-lattice {−3, 0, 1, 3⁄4, 2, 5⁄2}·ln 2, and the back-solved target lies in none of these sets (nor in the non-negative lattice the ordinary subdeterminants occupy, whose nearest point is 8.148). This corrects the v1.6 over-scope: the equivariant torsion is a *signed* half-lattice (the canonical value is −3 ln 2 \< 0), not the non-negative lattice claimed there. The spectral / cellular-torsion route to the vacuum scale is **CLOSED-NEGATIVE** — a complete no-go for all cellular seam involutions on this fixed complex (it does not claim to exclude refined torsions or other complexes). (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

# **Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN / IMPORTED-PROVEN | Complete proof from standard mathematics, in this paper or in the cited peer-reviewed literature. |
| PROVEN-under-product | Proved given an explicitly stated product/fibration ansatz; the ansatz is conditional. |
| PROVEN-under-canonical-action | Proved given the canonical (minimal Abelian compact) action; nonminimal extensions are separate. |
| DERIVED | Follows from Z-Spin structure plus standard mathematics; no new fitted parameter. |
| DERIVED-CONDITIONAL | Derived conditional on a stated hypothesis not closed here. |
| DERIVED-under-WPL | Derived conditional on the Wilson Polar-Line identification (a stated upstream-operator hypothesis). |
| TARGET-DERIVED | Derived from a stated gluing/uniqueness axiom that is itself the deliberate target of the theorem. |
| STRUCTURAL-CORRESPONDENCE | A structural match between a corpus object and an external construction, short of an identity. |
| IMPORTED-MOTIVATED / IMPORTED-BENCHMARK | An external mechanism invoked as motivation, or an external value used as a benchmark, not a Z-Spin prediction. |
| HYPOTHESIS-strong | A well-motivated conjecture with a named closure route, not yet derived. |
| NO-GO | A registered impossibility: the stated structure cannot achieve the stated goal. |
| CLOSED-NEGATIVE | A registered route or equality resolved in the negative (scope stated). |
| CONFIRMED-OPEN | A closure attempt was made and explicitly failed; the gap is confirmed undecidable with the present tools. |
| OPEN / OPEN-executable / NON-CLAIM | A recognized gap; “executable” when an algorithm is supplied; NON-CLAIM when the paper deliberately asserts nothing. |
| LOCKED | Core constant fixed upstream; immutable downstream. |

# **Claim Ledger (31 results)**

v1.7 lowers three load-bearing statuses to match what is actually proven (θ\_Z \= ω, the Kaloper–Padilla embedding, and the spectral no-go scope), retracts one incorrect cohomology claim, and registers four new results (a parity counterexample, a Wilson polar-line holonomy, a flux-gluing uniqueness theorem, and the Charge-Unit Obstruction). The “Status” column is the v1.7 assignment.

| Tag | Result | Status |
| ----- | ----- | ----- |
| F33.1A | Standard closed even-dim Ray–Singer torsion is trivial (T\_RS \= 1\) | IMPORTED-PROVEN |
| F33.1B | A standard 2D Z-sector carrier is excluded | DERIVED-CONDITIONAL |
| F33.1C | Odd-dimensional carrier uniqueness — refuted by counterexample | CLOSED-NEGATIVE |
| F33.1C\* | 2D seam-parity-restricted determinant torsion ln T₋ \= ln 4 ≠ 0 | PROVEN |
| F33.2A | Differential-character transgression π\!(â ∪ ûZ) \= â | PROVEN-under-product |
| F33.2B | Wilson polar-line holonomy Hol(L\_W) \= e^(iω) on the seam eigenline | DERIVED-under-WPL |
| F33.2B-i | Koenigs quotient ℂ\*/⟨λ\*⟩ is an elliptic curve | PROVEN |
| F33.2B-ii | Wilson–Koenigs orbit space ℂ\*/⟨λ\*⟩ \= E\_λ\* is the F0 Wilson orbit space | DERIVED-under-Orbit-Equivalence |
| F33.2B-iii | Theta line on Jac(Z) has c₁ \= 1 (fibre flux normalization, distinct from L\_W) | PROVEN |
| F33.2B-iv | Nome q \= e^(2πiτ) \= λ\* (definitional identity) | PROVEN (identity) |
| F33.2C | θ\_Z \= ω (phase from L\_W, flux from Θ\_Z) | DERIVED-under-WPL |
| F33.3A′-math | Dimension consistency 2(d−1)=d(d−1)/2 (d\>1) ⇒ d=4, X=3, Y=6 | PROVEN |
| F33.3A′-phys | Y-sector carries both X⊗ℝℂ and Λ²(ℝ^1,3) representations (Q=11 cross-check) | DERIVED-CONDITIONAL |
| F33.3A | Eighth-power dimensional law ρ ∼ E\*⁸/M̄P⁴ admissible | DERIVED |
| F33.3B | KV eighth-power scaling within a specific q-theory model | IMPORTED-PROVEN-within-model |
| F33.3C | Odd-sector scale E\* \= v | BENCHMARK (rejected as value closure) |
| F33.4A | BRST \+ seam parity cannot forbid F₋²R, F₋²F₊² | NO-GO |
| F33.4B | ∫F₄ as a nontrivial local H⁰'⁴(s|d) class | RETRACTED → OPEN-GLOBAL |
| F33.4B-i | Two-four-form BV master action (S\_BV, S\_BV) \= 0 (abelian ghost tower) | DERIVED-CONDITIONAL |
| F33.4B-ii | Flux-gluing exponential uniqueness σ(x+y)=σ(x)σ(y) ⇒ σ \= e^x | TARGET-DERIVED |
| F33.4B-iii | Z-Spin ↔ local-sequestering embedding | DERIVED-CONDITIONAL |
| F33.5a | Explicit TO/BCC T³ quotient; Δ₁ \= {0³,4³,6²,8³,12¹}, Betti (1,3,3,1) | PROVEN |
| F33.5b | Complete cellular-seam classification: 48 automorphisms, 20 involutions | PROVEN |
| F33.5c | Seam-odd torsion image \= {−3,0,1,3⁄2,2,5⁄2}·ln2; target ∉ image | PROVEN |
| F33.6a | Canonical compact 3-form: E\_k(θ) \= ½χ₋(θ+2πk)², so b₂ₙ \= 0 | PROVEN-under-canonical-action |
| F33.7A | Frozen top-form cosmology w \= −1 | IMPORTED-PROVEN |
| F33.7B | Dynamical w(z) ≠ −1 in the minimal 3-form action | CLOSED-NEGATIVE |
| F33.8a | B3 value via three registered routes (spectral, E\*=v, KP-tautology) | CLOSED-NEGATIVE-under-R1–R3 |
| F33.8b | Charge-Unit Obstruction: topology fixes flux number, not flux unit | PROVEN-under-minimal-EFT |
| F33.8c | Absolute χ₋ in a broader UV theory (closed via F33.8D route) | OPEN |
| F33.8D | Charge-unit reduction χ₋ \= e₋²/(4π²Z₋) under a rank-2 internal-cycle ansatz (ZS-F34) | DERIVED-CONDITIONAL (under uplift ansatz) |

# **Cross-Version Consistency (ZS-F32 / A28 / A29)**

v1.0 contained two cross-version conflicts, now resolved.

| Upstream result | v1.0 tension | v1.1 resolution |
| ----- | ----- | ----- |
| A28 v1.2: chiral-Pfaffian ½ not forced; spectral route retired | v1.0/v1.1 reopened a spectral determinant | F33.5 (v1.2) now COMPUTES the canonical equivariant torsion explicitly and proves 8.190 is not in the achievable lattice ℤ ln2 ⊕ ℤ ln3 — strengthening A28: the spectral route is closed-negative by computation, not by assumption. |
| A28 (field half): on-shell top-form ⇒ w \= −1 (IMPORTED-PROVEN); A29: i-tetration orbit barely evolves over DESI redshifts | v1.0 asserted w \= −1 \+ δw “because the KV remnant is not frozen” | F33.7 keeps w \= −1 (Branch A) as the on-shell result; a dynamical δw requires a new kinetic K(q) and is deferred to the Outlook (Branch B, OPEN, breaks zero-parameter). |

# **§1. Introduction**

## **1.1 From completion to conditional reduction**

ZS-F32 reduced the absolute vacuum scale to a UV odd-sector susceptibility and isolated the residual in three layers: θZ \= ω (DERIVED-CONDITIONAL), β₊₋ \= 0 (OPEN), and *χ*₋(**A**,**Q**,MP) (OPEN). A genuine UV completion would require specifying the tuple (G₋, R₋, Γcharge, SBV, H⁰'⁴(s|d), *χ*₋, C\_odd^sp): odd gauge group, matter representation, charge lattice, BV master action, counterterm cohomology, susceptibility and determinant. We specify none of the first four. v1.1 therefore claims only a conditional reduction, and reclassifies every result accordingly (Claim Ledger).

The cosmological consolidation of A31 carries a hard constraint we obey: a unified paper that also compares to data must not use the observed ρΛ as an input. The cosmological section is therefore blind, and the epistemic ceiling of the paper is set by its weakest load-bearing node, C\_odd^sp.

## **1.2 Locked inputs**

**A** \= δX · δY \= (5/19)(7/23) \= 35/437,    **Q** \= 11,    (dim Z, dim X, dim Y) \= (2, 3, 6).

z\* \= i(z\*)  (the i-tetration fixed point),   λ\* \= (iπ/2) z\*,   κ \= −ln|λ\*| \= 0.1148346,   **ω** \= arg λ\* \= 2.2592495540.

# **§2. Equivariant-Torsion Localization of the Odd Carrier (F33.1)**

v1.0 stated a single DERIVED localization theorem. Three gaps force a split into an imported theorem, a conditional application, and an open uniqueness gate.

## **2.1 F33.1A — Standard even-dimensional torsion no-go \[IMPORTED-PROVEN\]**

**Theorem F33.1A.**  If (Z, g, E, ∇E) is compact, closed, oriented and *even-dimensional*, with E a flat unitary bundle, then the Ray–Singer analytic torsion is trivial: TRS(Z, E) \= 1, i.e. ln TRS \= 0 \[1–3\]. (Note: the correct statement is triviality, TRS \= 1; “the torsion vanishes” is loose.) Since dim Z \= 2 (even, ZS-F5, LOCKED), Z is in the scope of this theorem.

## **2.2 F33.1B — Application to the Z carrier \[DERIVED-CONDITIONAL\]**

**Proposition F33.1B.**  Conditional on the Z-sector being realized as a closed oriented 2-manifold carrying a flat unitary local system in the scope of F33.1A, a *standard* Ray–Singer carrier for the odd vacuum functional on Z is excluded. The gauge-mode channel is also excluded: the JZ\-odd subspace of the register is one-dimensional (the slot-1 gauge direction; ZS-F2 §11.8), and this gauge mode is projected out of the physical Hilbert space, so with ρZ \= 0 PROVEN (ZS-F9, the Z-Spin form of “equilibrium vacuum does not gravitate,” ρV(q₀) \= 0 \[14\]) it sources no curvature. **(Correction to v1.0:** we drop the identification ind⁻(DZ) \= β₀(Z) \= 1\. The constant harmonic mode counted by β₀ is JZ\-even, so H⁰−(Z) \= 0; the odd gauge channel is the slot-1 direction, not a β₀ mode.)

## **2.3 F33.1C — Odd-dimensional uniqueness: refuted by counterexample \[CLOSED-NEGATIVE\]**

**The historical gate F33.1C.**  Triviality of the *standard* closed even-dimensional torsion (F33.1A) does not by itself exclude (a) torsion of a complex with boundary, (b) equivariant torsion, (c) refined / Cappell–Miller torsion, (d) a non-unitary local system, (e) mapping-cone torsion, or (f) orbifold / singular torsion. v1.0–v1.5 therefore left open whether an odd-dimensional carrier is *forced*. v1.7 settles this in the negative: the seam-parity-restricted determinant torsion is computed on an explicit even-dimensional carrier and is nonzero. The relevant object is

ln T₋ \= ½ Σp (−1)ᵖ p ln det′( Δp |im P₋ ),    Pp,− \= (1 − Jp)/2,

which is well-defined after the chain-involution conditions Jp² \= I and Jp+1 dp \= dp Jp (verified in §6 on the full complex). On the 2D even carrier this evaluates to ln 4 ≠ 0 (§2.3.1), so the uniqueness claim is *false*, not open: an odd-dimensional carrier is *not* forced. **Note (terminology):** CM^sp \= ln det Δ1,coexact is a single Hodge-block log-determinant; calling it “the Ray–Singer torsion side” of a Cheeger–Müller pair requires the remaining p-form determinants to combine into the alternating product, which §6 treats as an executable computation rather than asserting.

### **2.3.1 The v1.6 closure test and its refutation**

Now that the Z-sector is fixed as the 2D Koenigs torus (§3.2.2), a specific closure suggests itself: the seam involution is the central inversion −I, which is orientation-*preserving* in even dimensions ((−1)² \= \+1) and orientation-*reversing* in odd ((−1)³ \= −1). One might hope that Hodge duality then forces the seam-odd equivariant torsion to *vanish* on the 2D even carrier — excluding it — while permitting it on the 3D odd carrier, thereby forcing odd-dimensionality. v1.6 tests this explicitly, and the computation *refutes* it.

On a 2D T² (4×4 cubical complex) the *full* complex does satisfy Poincaré duality, log det′Δ₀ \= log det′Δ₂ \= 20.337; but *within the τ-odd subcomplex the duality fails*, log det′Δ₀|₋ \= 7.742 ≠ log det′Δ₂|₋ \= 10.515, under every chain-map sign convention tested (Appendix A, computation ET). The seam-odd torsion is therefore

ln T₋(2D) \= ½ Σp (−1)p p · ln det′(Δp|₋) \= ln 4 ≠ 0,   while  ln T₋(3D) \= 6 ln 2\.

So the even-dimensional seam-odd equivariant torsion is *genuinely nonzero*: the 2D even carrier is *not* excluded, and the orientation-factor argument is insufficient because the τ-odd subcomplex does not inherit Poincaré self-duality (the cellular involution and its Hodge-dual carry an unavoidable relative sign within the odd projection). This confirms the v1.1 “Problem B” observation directly. **Verdict:** the original claim — that a nonzero odd vacuum functional *requires* an odd-dimensional carrier — is *false*: the 2D even torus is an explicit counterexample. Odd-dimensional uniqueness is therefore CLOSED-NEGATIVE, not merely open. **Terminology:** the quantity computed here is the *seam-parity-restricted analytic determinant torsion* (the determinant of the τ-odd Hodge blocks), which is *not* the trace-weighted equivariant Ray–Singer torsion of the external literature — some definitions of the latter do vanish in even dimensions, so we keep the names distinct. The constructive content is recorded next.

### **2.3.2 What is established: a finite spectral theorem, not a uniqueness result**

Although uniqueness is open, the corpus *assignment* of the two roles is consistent and structurally determined. The register splits as Q \= 11 \= 3 (X) \+ 6 (Y) \+ 2 (Z) (ZS-F18 / F33.3A). The *odd vacuum determinant* lives on the 3D X-ambient — the truncated-octahedron BCC T³ whose edge Laplacian reproduces ZS-Q3 \= {0³, 4³, 6², 8³, 12¹} (ZS-M6, §6) — while *θ*Z \= ω lives on the 2D Z-sector Koenigs torus through the theta line (§3.2). These are different invariants (Ray–Singer torsion vs determinant-line holonomy) on different sectors (3D vs 2D); the integrity audit (Appendix F) confirms no computation conflates them. The assignment is thus DERIVED-from-structure — the corpus geometry places ZS-Q3 on the X-ambient — even though the abstract claim that the carrier *must* be odd-dimensional remains OPEN. **F33-G1C (revised):** a proof that the seam-odd equivariant torsion vanishes on every even-dimensional carrier would reopen the uniqueness route; a demonstration that ZS-Q3 does not live on a 3D complex would break the assignment.

# **§3. Transgression and the Dynamical Holonomy Identification (F33.2)**

## **3.1 F33.2A — Differential-character transgression \[PROVEN-under-product\]**

**Theorem F33.2A.**  Let â ∈ Ĥ²(X) be a degree-2 differential character (a U(1) connection) and ûZ ∈ Ĥ²(Z) a fibre character with ∫Z curv(ûZ) \= 1, on a fibration Z ↪ M →π X. Then fibre integration of the differential cup product transgresses to the base:

π\!( â ∪ ûZ ) \= â,    equivalently  HolγZ×Z(C₃⁻) \= exp( i ∮γZ aZ ),   C₃⁻ \= (1/2π) aZ ∧ ΩZ.

This is the Cheeger–Simons / Bär–Becker fibre-integration theorem \[10\] refined by the differential cup square BU(1)conn → B³U(1)conn \[11\]. (Normalization corrected from v1.0: the fibre factor is (1/2π) ∫Z ΩZ \= 1, not ½π.) The non-degeneracy condition (i) of v1.0 stands: aZ must be pulled back from X, or aZ ∧ ΩZ vanishes on the 2D fibre; ZS-F18 Bridge Four supplies the generation X \= \[JR1, JR2\] but its promotion to a literal bundle is part of the conditional content.

## **3.2 F33.2B — Wilson polar-line holonomy and the phase–flux separation \[DERIVED-under-WPL\]**

Theorem F33.2A proves the transgression *given* ∮γZ aZ \= ω. v1.3–v1.6 tried to supply that holonomy by identifying the physical connection aZ with the Quillen theta-line connection on Jac(Z). That identification was flawed: a flat U(1) connection on T² has zero curvature and hence c₁ \= 0, whereas the degree-1 theta line has c₁ \= 1, so a single bundle cannot be both. v1.7 corrects this by *separating* the object that carries the phase from the object that carries the flux normalization.

### **3.2.1 The phase: a flat Wilson polar-line \[DERIVED-under-WPL\]**

Let W be the linearized mediation (Koopman) operator of the i-tetration at its fixed point, acting on the seam-oriented eigenline L\_W by Wψ₋ \= λ\*ψ₋ with the multiplier λ\* (0 \< |λ\*| \< 1). Its polar decomposition W \= U\_W|W| has, on that eigenline,

U\_W ψ₋ \= (λ\*/|λ\*|) ψ₋ \= eiω ψ₋,   arg(λ\*/|λ\*|) \= ω   (verified to 10⁻¹²).

So L\_W carries a *flat* unitary connection a\_W \= (ω/2π) dφ with ∮γW a\_W \= ω and HolγW(L\_W) \= eiω — and, being flat, c₁(L\_W) \= 0\. This is the **Wilson Polar-Line (WPL)** theorem: the holonomy is the phase of the multiplier, read off from the polar (unitary) part of the upstream operator, with *no* reference to a curvature-carrying bundle. **Status:** DERIVED-under-WPL — conditional only on the identification of W with the corpus's upstream Wilson/Koopman operator and the simplicity of λ\* on the seam eigenline (both checked in Appendix A). The engineered Berry-loop of v1.2 is *demoted*: because the loop angle was set to ω by construction, it demonstrates realizability, not derivation, and is retained only as a realizability check.

### **3.2.2 The flux: an independent degree-one theta line \[PROVEN as mathematics\]**

Transgression (F33.2A) also needs a normalized integral 2-class on the fibre. This is a *separate* object Θ\_Z with

c₁(Θ\_Z) \= 1,   (1/2π) ∫Z Ω\_Z \= 1,

realized by the degree-one theta line on Jac(Z) (Quillen). The Koenigs quotient ℂ\*/⟨λ\*⟩ \= ℂ/(2πiℤ \+ (log λ\*)ℤ) *is* an elliptic curve (PROVEN: a rank-2 lattice quotient of ℂ), with τ \= (log λ\*)/(2π i) \= (ω \+ iκ)/2π, and is the natural fibre candidate; its nome is q \= e2πiτ \= λ\* (a definitional identity, F33.2B-iv). But the transgression does *not* require the physical fibre Z to *be* this torus — only that it carry a normalized degree-one class. Hence “physical Z \= Eλ\*” is DERIVED-CONDITIONAL, and the c₁ \= 1 statement is a theorem about Θ\_Z alone, kept distinct from the flat L\_W.

**Total transgression.** Cupping the two genuinely distinct objects, the degree-4 differential character C₃ \= a\_W ∪ uZ on γ\_W × Z fibre-integrates to π\!(C₃) \= a\_W, so

HolγW×Z(C₃) \= HolγW(L\_W) \= eiω,

with L\_W (flat, c₁ \= 0\) supplying the dynamical phase and Θ\_Z (c₁ \= 1\) supplying the fibre flux normalization. Therefore θZ \= ω is DERIVED-under-WPL — no longer asserted via the false “flat \= degree-1” identification. **F33-G2WPL:** if the corpus's upstream Wilson/Koopman operator does not have λ\* as a simple eigenvalue on the seam eigenline, or its polar phase differs from ω, the holonomy claim is RETRACTED.

**Distinctness from the gauge holonomy.** This dynamical ω is *not* the gauge holonomy ∮ω \= **A** \= 0.0801 fixed by Gauss–Bonnet (ZS-F4): ω/**A** \= 28.2, and the two live on different bundles — the Wilson polar-line of the mediation operator versus the U(1) gauge bundle on the polyhedral defect.

### **3.2.4 Closing the fibre: the Wilson–Koenigs orbit-space theorem \[DERIVED-under-Orbit-Equivalence\]**

v1.7 left “physical Z \= Eλ\*” as DERIVED-CONDITIONAL — a natural candidate, not a forced one. v1.8 closes it from the F0 dynamics rather than by fiat. The corpus F0 Wilson operator W (an 11×11 register map) has a 2×2 Z-block that, in the seam basis, is the rotation–scaling

W\_Z \= \[ \[ Re λ\*, −Im λ\* \], \[ Im λ\*, Re λ\* \] \],   so in the complex coordinate w,  W\_Z : w ↦ λ\* w.

We verify P\_Z W P\_Z \= W\_Z, that its eigenvalues are exactly λ\*, λ̄\*, and that the seam eigenvector (1, −i)/√2 is the λ\* eigenvector — the chirality condition J\_Z that selects the holomorphic branch over its conjugate (Appendix A, computation WK). Because 0 \< |λ\*| \< 1, the iterate group ℤ acting by n : w ↦ λ\*ⁿw on ℂ\* \= ℂ \\ {0} is *free and properly discontinuous*, so the quotient is a smooth complex torus,

Zorb \= ℂ\* / ⟨λ\*⟩ ≅ ℂ / ( 2πiℤ \+ (log λ\*)ℤ ) \= Eλ\*,   τ \= (log λ\*)/(2πi) \= (ω \+ iκ)/2π,  Im τ \> 0\.

This much is PROVEN (a rank-2 lattice quotient of ℂ\*): the orbit space of the F0 Wilson dynamics *is* the elliptic curve Eλ\*. The remaining bridge — that physical observables are constant on Wilson orbits, O(w) \= O(λ\*w), so that Zphys \= Zorb rather than merely maps to it — would follow from a BV–BFV cobordism-gluing factorization 𝒜phys \= 𝒜(ℂ\*)/⟨W\_Z⟩; we state it as an orbit-equivalence postulate. The physical-fibre identification is therefore registered DERIVED-under-Orbit-Equivalence: PROVEN as the orbit space, conditional only on observables being constant on Wilson orbits. **F33-G2orb:** if the F0 Wilson Z-block does not have λ\* as a simple eigenvalue, or the seam chirality does not select the λ\* branch, the orbit-space identification is RETRACTED.

### **3.2.3 Cross-version consistency \[PROVEN identity, not an independent bridge\]**

The nome identity q \= e2πiτ \= elog λ\* \= λ\* (|q − λ\*| \< 10⁻³⁰) is *definitional*: τ was defined as (log λ\*)/(2πi), so q \= λ\* follows automatically. It is a useful consistency statement — the same λ\* that sets ω and κ is the nome of the candidate fibre torus — but it is *not* independent evidence that the carrier and the i-tetration coincide, and we no longer present it as such. The j-invariant j(τ) \= 1.06 × 10⁵ \+ 2.41 × 10⁵ i is a determined function of λ\*; we report it and force no relation to (A, Q). The 4π/quaternionic closure (ZS-F27) is consistent with the odd-characteristic choice. No cross-version conflict arises.

# **§4. Eighth-Power Scaling: Classification and Blind Benchmark (F33.3)**

Retitled from “Scaling Resolution”: the form is classified and a blind benchmark computed, but the normalization is not resolved.

## **4.1 F33.3A′ — Bivector–complexification consistency: a second derivation of (3, 6, 2\) \[math PROVEN\]**

Before the scaling law, v1.8 records an independent cross-check of the register dimensions that does *not* assume Q \= 11\. Two descriptions of the Y-sector must agree. (a) If Y is the complex/conjugate doubling of the spatial X-sector, then over ℝ its dimension is dim Y \= 2·dim X \= 2(d−1) in d spacetime dimensions. (b) If Y carries the Lorentz curvature / electromagnetic *bivector*, then dim Y \= dim Λ²(ℝ^{1,d−1}) \= C(d, 2\) \= d(d−1)/2. Equating the two,

2(d − 1\) \= d(d − 1)/2   ⟹   d \= 4   (the unique solution with d \> 1),   so  X \= 3,  Y \= 6\.

Thus Z \= 2 (ZS-F5) plus the bivector identification *forces* d \= 4, X \= 3, Y \= 6 and recovers Q \= 3 \+ 6 \+ 2 \= 11 *without* presupposing it. Four independent routes reach the same 6 (Appendix A, computation Y6): Y \= X ⊗ℝ ℂ ⇒ 3 × 2; Y \= Λ²(ℝ^{1,3}) ⇒ C(4,2); Y \= 𝔰𝔬(1,3) ⇒ 3\_J \+ 3\_K (rotations \+ boosts); and Y \= (1,0) ⊕ (0,1) ⇒ the self-dual/anti-self-dual split E ± iB, each ℂ³. The isomorphism Λ²(ℝ^{1,3}) ≅ 𝔰𝔬(1,3) and the complex self-dual decomposition Λ²\_ℂ \= Λ²₊ ⊕ Λ²₋ (dim\_ℂ 3 each) are standard. **Status (split):** the dimension identity 2(d−1) \= d(d−1)/2 ⇒ d \= 4 and the representation equivalences are *PROVEN* (F33.3A′-math); identifying the Y-sector *as* carrying both representations is *DERIVED-CONDITIONAL* (F33.3A′-phys; DERIVED if one adopts the corpus ZS-M2/S15 Maxwell–Poynting reading); the agreement with Q \= 11 is an INDEPENDENT-CROSS-CHECK.

## **4.2 F33.3A — Dimensional law \[DERIVED\]**

Since ρΛ,Z \= ½*χ*₋ω² forces \[χ₋\] \= (energy)⁴, the gravitationally suppressed four-form object

ρ ∼ E\*⁸ / M̄P⁴,    \[E\*⁸/M̄P⁴\] \= (energy)⁴,

is dimensionally admissible and consistent with F32. This is a classification of admissible forms, not a unique law.

## **4.3 F33.3B — Klinkhamer–Volovik realization, split by what is actually proven**

v1.7 marked this IMPORTED-MOTIVATED as a single block. v1.8 splits it, because the external Klinkhamer–Volovik q-theory proves some of it within a model while leaving the rest phenomenological. In specific q-theory models the vacuum energy obeys ρV(t) ∝ κ M²(t) H⁴(t) and, at the electroweak crossover, ρV ∼ Eew⁸/EP⁴ — a genuine eighth-power scaling, but with an order-unity coefficient fixed by microphysics and a freeze-out governed by a phenomenological relaxation rate ρ̇V \= −Γ(t)(ρV − ρV,0). The honest split is:

| Claim | Status |
| ----- | ----- |
| Eighth-power scaling within a specific KV q-theory model | IMPORTED-PROVEN-within-model |
| A law universal to every four-form | NON-CLAIM |
| Z-Spin F₋ is the KV vacuum variable q | DERIVED-CONDITIONAL |
| The exact post-freeze-out coefficient | OPEN-executable |

Closing the ZS–q correspondence (raising the third row to DERIVED-CONDITIONAL → DERIVED) would require writing the action S \= ∫√−g \[K(q)R − ε(q) \+ L\_Y(T, q)\] with q \= ⋆F₋, imposing ρV(q₀) \= 0 and χq⁻¹ \= q₀²ε″(q₀) \> 0, and computing the Y-sector thermal κ\_Y(T) and the freeze-out kernel Γ\_Y(ω) \= (1/2ω) Im G^R(ω) from the Y retarded correlator rather than fitting Γ. That program is deferred to the companion ZS-F34; here F33.3B is registered at the split above. **F33-G3B:** any use of the eighth-power law as universal, or of a fitted Γ presented as derived, is void.

## **4.4 F33.3C — The identification E\* \= v \[BENCHMARK, rejected as value closure\]**

The electroweak vev is itself parameter-free (Factorized Determinant Theorem, ZS-S4 §6.12):

v \= M̄P · exp\[ −(38/9)(11 ln2 \+ ln3) \] \= M̄P · e−36.831 \= 245.93 GeV,

but E\* \= v is a separate odd-sector identification. Closing it requires an explicit portal

Sportal \= ∫ d⁴x √−g  ( M̄P² q₋ ) OEW⁻,   with the coefficient forced to unity,

which is not yet derived. The blind benchmark is

ρΛ,Z¹ᐟ⁴ |blind \= v² / M̄P \= 2.48 × 10⁻⁵ eV,   versus 2.24 × 10⁻³ eV observed (×90 short; E\*need \= 2.335 TeV ≈ 9.5 v).

## **4.5 F33.3D — The b₀ \= 14.25 route \[CLOSED-NEGATIVE\]**

A confining-odd-sector parametrization Λ₋ \= M̄P exp\[−8π²/(b₀ g₋²)\] with g₋² \= **A** would require b₀ \= 14.25, but ZS-A26 proves 32π²/(bZ **A**) \= 2νnowπ/**A** \= 8 Acompᵒᵈᵈ \= 276.6 is the present epoch; any exponent built to hit it is tautological, and the polyhedral β-rule gives the non-confining Z-sector b₀ ∈ {4/3, 5/3} (A22 barrier B2). The missing piece is

ρΛ \= cKV ( v⁸ / M̄P⁴ ) H₋(ω);

without cKV and H₋(ω) computed from an action, B3 stays OPEN.

# **§5. A BRST-Only Isolation No-Go and an IR Stability Bound (F33.4)**

This section is the principal revision. v1.0 sought to *prove* perturbative isolation; the correct cohomological conclusion runs the other way.

## **5.1 F33.4A — BRST-Only Isolation No-Go \[NO-GO\]**

**Theorem F33.4A.**  Three-form gauge invariance and seam parity alone do not forbid the mixed local operators

M̄P⁻² F₋² R   (mass dim 6\)    and    M̄P⁻⁴ F₋² F₊²   (mass dim 8).

**Proof sketch.**  Both F₋²R and F₋²F₊² are gauge-invariant local scalars. In the Batalin–Vilkovisky antifield formalism, a gauge-invariant local functional is annihilated by the BRST differential s and is generically not s-exact, so it is a non-trivial element of the ghost-number-zero local cohomology H⁰(s|d) that classifies admissible counterterms and consistent deformations \[8,9\]. BRST removes gauge-noninvariant terms; it does not remove gauge-invariant higher-dimension operators, which are exactly the content of an effective field theory. Seam parity does not help: since F₋ is seam-odd, F₋² is seam-even, so the mixed operators are parity-allowed (F32.22). Hence the v1.0 target \[F₋²R\], \[F₋²F₊²\] ∉ H⁰(s|d) fails without additional structure: the mixing coefficient β₊₋ is not forced to zero by BRST and parity.

This negative result is more valuable than the asserted positive one: it tells any UV completion that an exact isolation symmetry must be supplied by hand (an extra global symmetry, a Ward identity, or a sequestering mechanism), and it cannot be read off from gauge invariance.

## **5.2 F33.4B — A two-four-form sequestering action and its BV master action \[corrected; BV master DERIVED-CONDITIONAL\]**

Exact zero is the wrong target; phenomenological stability is the right one. With the mixed operators present, the radiative shift of the susceptibility is

|δχ₋ / χ₋| ≲ |cR| ⟨R⟩/M̄P² \+ |c₈| ⟨F₊²⟩/M̄P⁴ \+ ⋯

In the present universe ⟨R⟩/M̄P² ∼ H₀²/M̄P² ∼ (10⁻⁶¹)² ∼ 10⁻¹²², and the SM ⟨F₊²⟩/M̄P⁴ is likewise negligible, so even without exact cancellation the fractional shift is far below any observable threshold. The IR isolation needed for cosmology is therefore *radiative, not exact*.

**Correspondence, not identity (v1.7).** v1.6 claimed the corpus four-form is “precisely” the Kaloper–Padilla sequestering system. That overstates the match: KP local sequestering requires *two* four-forms and two rigid scalars Λ(x), κ²(x) with nonlinear gluing functions, whereas F₋ \= dA₃⁻ with ρZ \= 0 supplies only one. The honest relation is a STRUCTURAL-CORRESPONDENCE. To make it precise without new species, v1.7 writes the embedding action using the corpus's own F±,

SZS-seq \= ∫√−g \[ ½κ²(x) R − Λ(x) − LZS \] \+ ∫ σ₋(Λ/M̄P⁴) F₋ \+ ∫ σ₊(κ²/M̄P²) F₊,

with F₋ enforcing the vacuum-shift constraint and F₊ the Planck normalization. The two 4-form gauge symmetries make Λ and κ² on-shell constants (∂Λ \= ∂κ² \= 0), and the residual cosmological constant is the ratio of the two fluxes — which, as the external theorem states, is an arbitrary finite integration constant fixed by measurement, not by (A, Q). The dim-6 and dim-8 mixed cocycles (admissible by F33.4A) contribute, off this background,

|δχ₋/χ₋| ≲ ⟨R⟩/M̄P² ∼ 10⁻¹²¹   (dim 6),   ∼ 10⁻²⁴¹   (dim 8),   both radiatively protected.

**Retraction of the local-cohomology claim (v1.7).** v1.6 asserted that ∫F₄ is a nontrivial element of the ghost-number-zero local cohomology H⁰'⁴(s|d). This is *withdrawn*: locally F₄ \= dA₃, so ∫F₄ is d-exact, and local BRST cohomology quotients by a ∼ a \+ sb \+ dc — a d-exact term is trivial there. A nontrivial flux class lives in global differential cohomology, a different object that local H(s|d) does not certify; the v1.6 verification merely hard-coded the booleans rather than computing them, so the claim is RETRACTED → OPEN-GLOBAL. **What is provable.** The correct statement is at the level of the BV master action. Adjoining antifields and the reducible abelian ghost tower c2,±, c1,±, c0,± to SZS-seq gives the explicit action SBV \= Scl \+ Σ± ∫ \[ A\*3,± ∧ dc2,± \+ c\*2,± ∧ dc1,± \+ c\*1,± ∧ dc0,± \]. For this abelian tower the master equation (SBV, SBV) \= 0 reduces term-by-term to d² \= 0 plus ghost nilpotency, and the topological σ(Λ)F₄ and F± couplings are s-closed, so they do not deform the gauge algebra. The mechanism is that σ(Λ)F₄ \= d(σA₃) − σ′(Λ)dΛ∧A₃ is *not* a pure boundary term off-shell, and the A₃ equation of motion forces dΛ \= 0\. The reduction to d² \= 0 is exhibited, but the full antibracket with the F± couplings is not computed in the verifier, so this is registered DERIVED-CONDITIONAL, not PROVEN (F33.4B-i). **Closing the free function.** The gluing functions σ± are a priori arbitrary, which would break zero-parameter status. They are pinned by a uniqueness theorem (F33.4B-ii): if cobordism gluing adds flux labels while multiplying path-integral weights, then σ(x+y) \= σ(x)σ(y) with σ(0) \= 1, σ′(0) \= 1, whose unique continuous solution is σ(x) \= ex — the same additive-to-multiplicative homomorphism uniqueness as ZS-M1. **Status:** BRST-only isolation NO-GO (F33.4A) retained; ∫F₄ local class RETRACTED; two-four-form BV master action DERIVED-CONDITIONAL (abelian ghost tower, master equation reduced to d² \= 0; full antibracket deferred) (F33.4B-i); σ \= ex TARGET-DERIVED (F33.4B-ii); the Z-Spin ↔ local-sequestering embedding DERIVED-CONDITIONAL (F33.4B-iii); matter-loop radiative stability IMPORTED-PROVEN \+ DERIVED-CONDITIONAL on that embedding. **F33-G4 (revised):** a demonstration that the BV master equation fails, or that gluing does not multiply weights, falsifies the construction.

# **§6. Complete Cellular-Seam Classification of the Odd Spectral Determinant (F33.5)**

Promoted to the center of the paper and, in v1.2, *resolved*. ZS-A28 retired the naive spectral route (the chiral-Pfaffian ½ is not forced); we now construct the full chain-level object explicitly with a canonical cellular seam involution — no half-weight imposed — and compute its equivariant torsion. The result closes the spectral route to the vacuum scale in the negative.

## **6.1 The target, and why 8.190 is back-solved**

Closure of B3 via §4 would require C\_odd^sp \= 34.58/(38/9) \= 8.190, equivalently E\* \= √(ρobs M̄P) \= 2.335 TeV. This value is back-solved from the observation and is a falsification target. The corpus-native log-determinants bracket it but (corrected from v1.0) no simple combination hits it: the nearest half-weight 11 ln2 \+ ½ ln3 \= 8.174, the arithmetic mean 8.233, the geometric mean 8.218 (v1.0 wrongly called the last two both 8.233), and the coexact spectrum is {8³, 12¹}.

**Table 1\. Corpus-native log-determinants vs. the back-solved target.**

| Object | eigenvalues | ln det (weight) | value |
| ----- | ----- | ----- | ----- |
| exact block (dim 5\) | 4³, 6² | 8 ln2 \+ 2 ln3 | 7.742 |
| coexact \= C\_M^sp (dim 4\) | 8³, 12¹ | 11 ln2 \+ ln3 | 8.723 |
| target (back-solved) | —  | not an integer ln-lattice point | 8.190 |

## **6.2 The explicit truncated-octahedron BCC T³ quotient**

We build the quotient complex literally. The truncated octahedron (the BCC Voronoi cell) has 24 vertices at the permutations of (0, ±1, ±2), 36 edges, and 14 faces (6 squares \+ 8 hexagons). Quotienting by the BCC translation lattice Λ \= ⟨(2,2,2), (4,0,0), (0,4,0)⟩ (covolume 32 \= cell volume) identifies vertices 4-to-1, edges 3-to-1, faces 2-to-1, giving a CW complex on T³ with

(V, E, F, C) \= (6, 12, 7, 1),   χ \= 0,   Betti (b₀,b₁,b₂,b₃) \= (1, 3, 3, 1).

The oriented incidence matrices ∂₁ (6×12) and ∂₂ (12×7) satisfy ∂₁∂₂ \= 0 (verified), rank ∂₁ \= 5, rank ∂₂ \= 4, and reproduce the corpus ZS-Q3 edge spectrum exactly:

spec Δ₁ \= spec( ∂₁ᵀ∂₁ \+ ∂₂∂₂ᵀ ) \= { 0³, 4³, 6², 8³, 12¹ },

with the octahedral vertex Laplacian Δ₀ \= ∂₁∂₁ᵀ giving the exact block {4³, 6²} (det 7.742) and Δ₂ \= ∂₂ᵀ∂₂ giving the coexact block {8³, 12¹} (det 8.723 \= C\_M^sp). This is the concrete realization the reviewer's Step 1 required, and it closes the v1.1 gap (a): ∂₂ is now in hand.

## **6.3 The canonical central-inversion seam involution and its torsion**

The truncated octahedron is centrally symmetric, so the central inversion σ : v ↦ −v descends to the quotient as a chain involution Jp on every degree. We verify the full package numerically (Appendix A, computation TO):

J₀² \= J₁² \= J₂² \= I,   J₀∂₁ \= ∂₁J₁,   J₁∂₂ \= ∂₂J₂,   \[Jp, Δp\] \= 0   (all p).

This is a genuine cellular seam involution on the *full* complex — not only the 1-skeleton of v1.1 — closing gaps (b)/(c). Its seam-odd (J-odd) blocks are

Δ₀|₋ \= {4³},   Δ₁|₋ \= {4³},   Δ₂|₋ \= ∅,   ⟹   ln T₋ \= ½ Σp (−1)ᵖ p ln det′(Δp|₋) \= −3 ln 2 \= −2.079,

with each nonzero seam-odd determinant equal to 3 ln 4 \= 4.159. (The seam-odd subcomplex carries the orientation-odd b₃ volume mode, handled by the standard det′ zero-mode subtraction.) The canonical seam-odd torsion −2.079 \= −3 ln 2 is one point of the finite image classified in §6.4; none of the constituent determinants (4.159) is 8.190 either.

## **6.4 The complete cellular-seam classification**

v1.6 over-stated the closure as a “non-negative integer lattice” no-go. That was both too weak and self-contradictory: the equivariant torsion ln T₋ \= ½ Σp (−1)ᵖ p ln det′(Δp|₋) carries an alternating sign, a degree weight p, and a factor ½, so its values lie in a *signed half-lattice* — and the canonical value −3 ln 2 is itself negative, hence *not* in ℤ≥0 ln2 ⊕ ℤ≥0 ln3. v1.7 replaces the claim with an exact enumeration. We compute the full signed cellular automorphism group of the quotient complex (Appendix A, computation CLS):

|Autcell(C•)| \= 48 \= |Oh|,   \#{ J : J² \= I } \= 20   (19 nontrivial involutions),

each verified to satisfy Jp² \= I and the chain-map conditions J₀∂₁ \= ∂₁J₁, J₁∂₂ \= ∂₂J₂. For every one of the 20 seam involutions we compute the seam-odd torsion; the image is the finite signed set

𝒯₋ \= { −3, 0, 1, 3⁄2, 2, 5⁄2 } · ln 2,   max |𝒯₋| \= 3 ln 2 \= 2.079,

and the per-degree determinant images ln det′(Δp|₋) are likewise finite sets (Appendix A). The back-solved target 8.190 lies in *none* of these sets — it is more than a factor of three above the largest attainable |torsion|. **Two scopes, kept distinct.** (i) The *ordinary* spectral subdeterminants of ZS-Q3 (the route that would set C\_odd^sp) do factor over {2,3} and lie in the non-negative lattice ℤ≥0 ln2 ⊕ ℤ≥0 ln3, whose nearest point to 8.190 is 7 ln2 \+ 3 ln3 \= 8.148 — so that route misses. (ii) The *complete seam-odd torsion* over all 20 cellular involutions is the signed half-lattice set 𝒯₋ above — which also misses. **Theorem F33.5 (Complete Cellular-Seam Classification) \[PROVEN\]:** on this fixed BCC T³ complex, the seam-odd determinant and torsion images are the finite sets above, and the target is disjoint from both. **Scope.** This is a complete no-go for *all cellular seam involutions on this complex*; it does *not* claim to exclude refined / Cappell–Miller torsion or a different complex. **The spectral / cellular-torsion route is CLOSED-NEGATIVE** with the scope now exact.

## **6.5 What is closed, what remains, and the firewall**

Closed: the hypothesis “ρΛ is a seam-odd spectral/equivariant determinant on the ZS-Q3 complex equal to 8.190” is refuted. **Not closed:** B3 as a whole, since non-spectral mechanisms remain open — the IR radiative-stability / sequestering route (§5.2), a different complex, or genuinely new structure. The register ↔ CW intertwiner U is now moot for *this* question: whatever U does, the achievable values lie in ℒ and exclude 8.190. **Firewall.** The verification script zs\_f33\_verify\_v1\_8.py computes ∂₁, ∂₂, Jp, the spectra and the torsion reading *only* incidence data and locked normalizations; the target 8.190 enters solely in a post-computation comparison block. **Status: CLOSED-NEGATIVE (spectral route); B3 OPEN via non-spectral routes.**

# **§7. Vacuum Functional Form: the Canonical Compact 3-Form Branch (F33.6)**

**Theorem F33.6 (canonical branch). \[PROVEN-under-canonical-action\]**  v1.6 left the higher cumulants b₂, b₄, … OPEN and leaned on an SU(3) benchmark. v1.7 closes the leading question by adopting the *canonical* minimal Abelian compact 3-form action,

S₋\[A₃, θ\] \= −(1/2χ₋) ∫ F₄ ∧ ⋆F₄ \+ (θ/2π) ∫ F₄,   (1/2π)∫F₄ ∈ ℤ.

Integrating out the flux F₄ at fixed integer class k gives an *exactly quadratic* branch functional,

Ek(θ) \= ½ χ₋ (θ \+ 2πk)²,    E(θ) \= mink∈ℤ Ek(θ),

so in the canonical branch the higher cumulants *vanish identically*: b₂ \= b₄ \= b₆ \= ⋯ \= 0, and the truncation problem disappears (ΔE₋(θ) \= ½χ₋θ² is exact on each branch). **Status: PROVEN-under-canonical-action.** The corpus large-N / canonical registration of the quadratic law (ZS-F32) is the upstream warrant for this branch. **Non-canonical comparison.** A general nonlinear kinetic function K(F) would reintroduce b₂, b₄, … (OPEN, nonminimal extension); the SU(3) benchmark b₂ \= −0.0216 \[5\] (b₂ω² ≈ −11%) is one such non-canonical datum, retained only as an IMPORTED-BENCHMARK comparison, not a Z-Spin prediction. **F33-G6:** if the odd sector is shown to require a non-canonical (non-quadratic) kinetic term, the b₂ₙ \= 0 result is confined to the canonical branch and the cosmological use must carry the truncation gate εN \< 1%.

# **§8. Cosmological Hand-off: Frozen Branch and Outlook (F33.7)**

## **8.1 Branch A — Frozen top-form, w \= −1 \[IMPORTED-PROVEN\]**

On shell a non-propagating four-form in 4D is constant, Tμν⁽⁻⁾ \= −ρΛ,Z gμν, so q̇ \= 0 and w \= −1 strictly. ZS-A28 fixes this as the field-theory-half IMPORTED-PROVEN result, and ZS-A29 finds the i-tetration orbit barely evolves across DESI redshifts, freezing w ≈ −1. The blind Friedmann normalization is

3 M̄P² H² \= ρm \+ ρr \+ ρΛ,Z,   HΛ \= √(ΔE₋(ω)/3M̄P²),   with Ωm \= 38/121, ΩΛ \= 83/121, ΩΛ/Ωm \= 83/38 \= 2.184 ≈ 2e**A** \= 2.167 (same order, not an identity),

using H₀ only for comparison. On DESI DR2 we state the evidence carefully: flat ΛCDM still describes the data well, while the w₀wₐ (CPL) extension shows a preference whose significance is dataset- and parametrization-dependent — about 3.1σ for DESI+CMB and 2.8σ–4.2σ once supernovae are added depending on the sample (Pantheon+, Union3, DESY5), with the preferred region w₀ \> −1, wₐ \< 0 \[16\]. This is a preference, *not* an exclusion of ΛCDM. Branch A is currently compatible; a persistent evolving-dark-energy signal would create tension. **F33-G8:** a computed ρΛ inconsistent with the observed value falsifies the theory (no retuning).

## **8.2 Branch B — Dynamical w(z) in the minimal action \[CLOSED-NEGATIVE\]**

v1.7 sharpens the Outlook into a no-go. A canonical 4-form has no propagating degree of freedom in four dimensions: its equation of motion is d⋆F₄ \= 0, so ⋆F₄ \= constant, giving Tμν \= −ρ gμν and w \= −1 identically. Therefore

w(z) ≠ −1 does not arise from the minimal 3-form action  ⟹  Branch B is CLOSED-NEGATIVE under that action.

A dynamical branch can be built only by adding a new kinetic term — e.g. (∂⋆F₄)²/M² or a scalar kinetic structure −½K(q)(∂q)² — which introduces a new degree of freedom and a new scale, and (if K is a free function) breaks zero-parameter status. That is a *separate nonminimal extension*, not an open question within F33. **Consequently the cosmology of the present theory is unambiguous:** w \= −1, fully closed; an evolving-dark-energy signal would be evidence for the nonminimal extension and is a NON-CLAIM of this paper. **Status: CLOSED-NEGATIVE (minimal action); nonminimal dynamical branch is a NON-CLAIM.**

# **§9. No-Go Consolidation and Blind Prediction (F33.8)**

Blind output: ρΛ,Zᵖʳᵉᵈ \= ΔE₋(ω) \= Λ₋⁴ H₋(ω), conditional on the uncomputed C\_odd^sp. Four no-gos bound why B3 is OPEN, none an impossibility:

(N1) A–Q-only scale no-go (DERIVED, A28): dimensionless **A**,**Q** cannot fix a scale; the hierarchy selector is ln(ρobs/M̄P⁴) \= −276.6. (N2) The 276.6 collapse (DERIVED, A26): the candidate exponents are all the present epoch, so bZ \= 14.25 is tautological. (N3) Central-shift no-go (PROVEN, F32.15/A26): i\[H+c₀I, X\] \= i\[H, X\], so relative/modular tools are blind to the absolute offset; B3 is a missing central normalizer. (N4) BRST-only isolation no-go (this paper, §5): gauge invariance and parity do not forbid the mixed counterterms, so exact β₊₋ \= 0 is not free.

**F33-G9:** any claim that C\_odd^sp or *χ*₋ is parameter-free while using the observed ρΛ, a chosen scale, a base-10 coincidence, a fitted half-weight, or a back-solved exponent is void.

## **9.2 The non-spectral normalizer: a sequestering route \[HYPOTHESIS-strong\]**

v1.2 closed the *spectral* route (8.190 ∉ the lattice ℒ). What remains is non-spectral, and the central-shift no-go (N3) names what is needed: because i\[H \+ c₀I, X\] \= i\[H, X\], every relative or modular tool is blind to the absolute offset c₀, so B3 is a missing *central normalizer* that fixes c₀ by a global, non-spectral condition. The Kaloper–Padilla sequestering constraint is exactly such an object: the rigid Λ carried by the 4-form flux fixes the absolute vacuum energy topologically, outside the spectrum. Identifying it with the corpus four-form (§5.2) gives

ρΛ \= (4-form flux constant) − ⟨ Lmatter ⟩cosmic,   with the KP prediction ρΛ ∼ ⟨ρmatter⟩today.

This is structurally consistent with the corpus coincidence ΩΛ/Ωm \= 2e**A** \= 2.17 \= O(1), and it explains both the smallness and the radiative stability of ρΛ through one mechanism. **The honest limit:** the 4-form flux is a free boundary condition, so KP alone does not give a parameter-free ρΛ; closing the value requires fixing that flux to the corpus's blind ρΛ \= ΔE₋(ω), which is *not* done here. Hence the route — “B3's central normalizer is the KP sequestering constraint” — is registered HYPOTHESIS-strong (mechanism identified, non-spectral, RG-stable), with the value-closure OPEN. **F33-G10:** any claim that the KP route fixes ρΛ parameter-free while leaving the 4-form flux free, or while not matching it to ΔE₋(ω), is void.

## **9.3 The absolute value: three routes exhausted \[CLOSED-NEGATIVE-under-R1–R3\]**

v1.5 completes the value question. Three independent routes to a parameter-free absolute ρΛ have now been examined and all are closed; the table records the terminus.

| Route | Attempt | Outcome |
| ----- | ----- | ----- |
| Spectral (v1.2) | C\_odd^sp from the seam-odd determinant | 8.190 ∉ ℒ → CLOSED-NEGATIVE |
| Branch A (E\*=v benchmark) | ρ\_Λ \= ½χ₋ω² with E\* \= v (electroweak benchmark) | 90× short; √90 underivable |
| Branch B: KP residual | ρ\_Λ \= M̄\_P⁴e^(−ν\_now), ν\_now \= 276.6 (A26) | right magnitude, tautological |

**Branch A and the √90 enhancement.** With the natural corpus scale E\* \= v the eighth-power law gives ρΛ¹ᐟ⁴ \= v²/M̄P \= 2.48 × 10⁻⁵ eV, 90× short of 2.24 × 10⁻³ eV; closing the gap needs E\*need/v \= √90 \= 9.49. We searched for a principled origin and found none. The nearest numerical near-miss is eω \= 9.58 (within ≈ 1%), but eω is the exponential of a *rotation angle* — the natural object attached to ω is eiω, not eω — so it carries no mechanism; the other candidates (Qx, (1/**A**)x, |λ\*|x) all require non-integer fitted exponents. Adopting any of them is exactly the back-solved-exponent numerology F33-G9/G11 forbid, so we reject them. √90 is *not* derivable from (A, Q): Branch A is CLOSED-NEGATIVE.

**Branch B and the present epoch.** The KP cosmic-average residual gives ρΛ \= M̄P⁴ exp(−νnow), and with ZS-A26's present epoch νnow \= 276.6 this reproduces ρobs to better than a percent — the right magnitude and the ρΛ ∼ ρmatter coincidence, radiatively stable by §5.2. But νnow \= 276.6 \= ln(M̄P⁴/ρobs) is itself *defined* by ρobs (A26), so Branch B is tautological: it explains why ρΛ is what it is at the present epoch, not what it must be from (A, Q) alone.

**Conclusion (scoped).** None of the three *registered routes* R1–R3 produces a parameter-free absolute ρΛ: the spectral/cellular route is excluded by the complete classification, the E\*=v branch needs an underivable √90, and the residual branch is tautological. So the corpus value-programme is CLOSED-NEGATIVE-under-R1–R3 — a confirmed terminus for *those routes*. This is *not* a claim that an absolute ρΛ is impossible in any UV completion; that broader statement is OPEN (F33.8c). The next subsection shows *why* the routes fail, structurally. **F33-G11 (retained):** any later closure that fits √90, 90, or eω to (A, Q) rather than deriving the enhancement from a stated mechanism is void.

## **9.4 The Charge-Unit Obstruction \[PROVEN-under-minimal-EFT\]**

The three-route exhaustion is upgraded from an empirical list to a structural theorem. In the canonical compact 3-form EFT (§7), flux integrality fixes the topological class

\[ F₄ / 2π \] ∈ H⁴(M; ℤ)   ⟹   k ∈ ℤ,   but   Ek(θ) \= (e₋²/2Z₋)(k \+ θ/2π)²,   χ₋ \= e₋²/(4π²Z₋) ∝ e₋²/Z₋.

Topology fixes the flux *number* k, but the energy spacing depends on the membrane charge e₋ and the kinetic normalization Z₋ — the *dimensionful unit* χ₋ \= e₋²/(4π²Z₋) itself, which integrality does not constrain. **Theorem F33.8 (Charge-Unit Obstruction) \[PROVEN-under-minimal-compact-3-form EFT\]:** (A, Q, dim Z) together with flux integrality fix the flux number but not the flux unit, hence cannot determine the absolute susceptibility χ₋. This is the structural reason the routes of §9.3 fail: the spectral route fixes integers (lattice points), the E\*=v route guesses the unit (and misses by √90), and the residual route reads the unit off the observation (tautology). It strengthens the A–Q-only no-go (ZS-A28) to the EFT level: topology sets the *number* of flux quanta, never the dimensionful *size* of one. The integer structure of a charge lattice and the physical charge unit are different data (ZS-F32 B3-1). **This is the paper's strongest terminus:** not “we tried three things,” but “topology alone cannot fix the absolute four-form susceptibility.” **F33-G12:** any claim to fix χ₋ from (A, Q) and flux integrality alone — without supplying the dimensionful unit e₋²/Z₋ from additional UV data — is void.

## **9.5 F33.8D — The internal charge-unit reduction \[DERIVED-CONDITIONAL under a rank-2 internal-cycle ansatz; developed in ZS-F34\]**

The Charge-Unit Obstruction is *not* an impossibility theorem; it names exactly the missing datum — the kinetic normalization Z₋ and the minimal membrane charge e₋. v1.8 records the route that supplies them, deferring the full computation to the companion paper. Wrapping the Y-sector as Y₆ \= M₄ × Σ₂ and expanding the five-form potential C₅ \= A₃⁻(x) ∧ ω₂(y) with ∫Σ₂ ω₂ \= 1 gives G₆ \= dC₅ \= F₄⁻(x) ∧ ω₂(y), and the kinetic action reduces to the 4D one with

Z₋ \= (1/g₆²) ∫Σ₂ ω₂ ∧ ⋅₂ω₂,   e₋ \= N e₆ ∫Σ₂ ω₂ \= N e₆,   χ₋ \= e₋²/(4π²Z₋) \= N²e₆²g₆² / (4π² VΣ),

with VΣ \= ∫Σ₂ ω₂ ∧ ⋅₂ω₂. The obstruction's unknown unit is thus expressed through three computable data: the internal cycle metric VΣ, the gauge coupling g₆, and the minimal charge e₆. **A scope caveat (essential):** the “6” of F33.3A′ is the *representation* dimension of the Y-sector field content — dim Λ²(ℝ^{1,3}) \= dim 𝔰𝔬(1,3) \= dim(E⊕B) \= 6 — and it does *not* by itself imply a *six-dimensional spacetime*. The reduction above is therefore stated in the safer *internal-fibre* form: Y₆ \= M₄ × Σ₂ is a total configuration bundle over the 4D base M₄ carrying a *rank-2 internal cycle* Σ₂, not a Kaluza–Klein spacetime uplift. Whether the six field slots additionally *force* a genuine 6D metric is a separate question, deferred to ZS-F34. **Theorem F33.8D (conditional):** given the rank-2 internal-cycle ansatz, if (Σ₂, ω₂) are unique in the corpus geometry, g₆ is derived from the full Y spectrum, e₆ is fixed by large-gauge invariance, and the wrapped-brane sector is anomaly-free, then χ₋ \= e₋²/(4π²Z₋) is DERIVED. Establishing the ansatz and these data is the subject of ZS-F34, *The Six-Dimensional Charge Unit of the Z-Spin Three-Form*; in F33 the reduction is registered as DERIVED-CONDITIONAL under that ansatz, turning the open “absolute χ₋” into a concrete, bounded computation. **F33-G8D:** if the field-representation “6” is used to assert a 6D spacetime without an independent metric, or the reduction yields a VΣ, g₆, or e₆ inconsistent with the corpus geometry, the route is RETRACTED.

# **§10. Conclusion**

ZS-F33 v1.8 is a conditional UV reduction, not a completion, and says so. Its load-bearing advances are now each tied to an explicit computation, with statuses set at what is actually proven. The odd carrier is localized by an *imported* even-dimensional torsion no-go with a conditional Z-application (F33.1A/B); odd-dimensional uniqueness is *CLOSED-NEGATIVE*, refuted by the 2D seam-parity-restricted determinant torsion ln T₂₋ \= ln 4 ≠ 0 (F33.1C). The transgression holonomy θZ \= ω is DERIVED-under-WPL through a flat Wilson polar-line L\_W (c₁ \= 0, holonomy e^(iω) \= λ\*/|λ\*|), kept strictly separate from the degree-1 theta line Θ\_Z (c₁ \= 1, fibre flux) — repairing the v1.6 conflation of a flat bundle with a degree-1 one. The physical fibre itself is closed: the Wilson–Koenigs orbit-space theorem makes ℂ\*/⟨λ\*⟩ \= Eλ\* the orbit space of the F0 Wilson dynamics (DERIVED-under-Orbit-Equivalence), with the seam eigenvector (1, −i)/√2 selecting the λ\* branch.

Gauge invariance and seam parity are shown *not* to isolate the odd sector — a BRST-Only Isolation No-Go (F33.4A). The v1.6 claim that ∫F₄ is a nontrivial local H⁰'⁴(s|d) class is *retracted* (it is d-exact); the corrected mechanism is a two-four-form sequestering action with the corpus F±, whose abelian-ghost-tower BV master equation reduces to d² \= 0 (DERIVED-CONDITIONAL) and whose gluing functions are pinned by the exponential-uniqueness theorem σ \= e^x (F33.4B). The centerpiece, F33.5, is now a *complete cellular-seam classification*: the truncated-octahedron BCC T³ quotient has 48 cellular automorphisms and 20 seam involutions, and the seam-odd torsion image is the finite signed half-lattice {−3, 0, 1, 3⁄2, 2, 5⁄2}·ln 2 — disjoint from the back-solved target, which lies in neither the ordinary non-negative subdeterminant lattice (nearest 8.148) nor the torsion image. The register dimensions are independently re-derived: the bivector–complexification consistency 2(d−1) \= d(d−1)/2 forces d \= 4, X \= 3, Y \= 6, recovering Q \= 11 without assuming it (F33.3A′).

On the absolute scale we are deliberately conservative. The three registered routes are CLOSED-NEGATIVE-under-R1–R3, and the Charge-Unit Obstruction explains the structural reason: flux integrality fixes the flux number k but not the dimensionful unit χ₋ \= e₋²/(4π²Z₋) ∝ e₋²/Z₋, so (A, Q) and topology alone cannot determine χ₋ (F33.8). This is *not* an impossibility theorem: the obstruction names exactly the missing datum, and the internal charge-unit reduction (F33.8D, developed in the companion ZS-F34) shows how a rank-2 internal-cycle compactification would supply it, giving χ₋ \= e₋²/(4π²Z₋) as DERIVED-CONDITIONAL on that ansatz. The honest content of conditional reduction is intact: the *structure* — the Wilson phase, the elliptic carrier and its orbit space, the BV sequestering, the complete spectral classification, the dimensional re-derivation — is derived, while the *absolute scale* awaits the one UV datum the obstruction isolates. ω stays distinct from the gauge **A** (28×). The cosmology is the frozen w \= −1 branch, consistent with ZS-A28/A29; the dynamical-w branch is CLOSED-NEGATIVE under the minimal action and a NON-CLAIM otherwise. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) **LOCKED**.

# **Acknowledgements & Code Availability**

This revision integrates an internal peer review that corrected three numerical errors (the half-weight 11 ln2 \+ ½ ln3 \= 8.174 ≠ 8.190; the geometric mean 8.218 ≠ 8.233; the coexact spectrum {8³, 12¹}), reclassified over-assigned statuses, weakened the title from “completion” to “conditional reduction,” flagged the A28/A29 cosmology conflict, and prescribed the BRST no-go pivot and the cellular-torsion construction. All numerical checks — ω and ω²/2, the Factorized-Determinant vev, the eighth-power blind benchmark, the octahedral cellular involution and its seam-odd split, and the 276.6 collapse — were performed with standard open-source libraries (Python/NumPy/mpmath, seed 437\) and are reproduced in Appendix A and in zs\_f33\_verify\_v1\_8.py, which is structured so that no observed or back-solved value enters the computation of C\_odd^sp. C\_odd^sp is not derived here; ρΛ \= ΔE₋(ω) is a falsification target. PROVEN / IMPORTED-PROVEN results rest on standard theorems (Ray–Singer; Cheeger–Müller; Cheeger–Simons / Bär–Becker; Barnich–Brandt–Henneaux; Henneaux–Knaepen–Schomblond; Witten; Bonati et al.; Kaloper–Padilla; Klinkhamer–Volovik; Chandrasekaran–Longo–Penington–Witten).

# **Appendix A. Verification Ledger**

**Verification reclassification (v1.8).** The script is now *standalone* — it builds the BCC T³ quotient and the full 48/20 classification inline, with *no sidecar files*. The suite is split into four kinds, and only ASSERT-COMPUTED counts toward a “pass”. **ASSERT-COMPUTED** (19): assertions that can fail — incidence matrices, ∂₁∂₂ \= 0, Betti numbers, the full Δ₁ spectrum, the 48-automorphism / 20-involution classification and its torsion image, the full 11×11 Wilson map with P\_Z W P\_Z \= W\_Z, the Wilson polar phase, the Z-block eigenvalues and the J\_Z branch selection, the 2D parity torsion computed from the Fourier spectrum (ln T₋ \= ln 4), the bivector identity d \= 4, and the χ₋ \= e₋²/Z₋ sign. **IDENTITY-REPORTED** (4): definitional identities — q \= e2πiτ \= λ\*, ω \= arg λ\*, the dimensional identities. **IMPORTED-PROVEN** (1): the multiplicative Cauchy uniqueness σ \= e^x \[18e\], not a finite-grid check. **STRUCTURAL-ASSUMPTION** (3): declared interpretations excluded from the pass count — the orbit-equivalence postulate O(w)=O(λ\*w), the corpus-F₋ sequestering correspondence, and the canonical-kinetic selection. The retracted ∫F₄ booleans and the four declarative c₁/b₂ₙ/w booleans are removed entirely.

**Table A1. Numerical regressions (the v1.8 standalone verification suite; reclassified into ASSERT-COMPUTED / IDENTITY-REPORTED / IMPORTED-PROVEN / STRUCTURAL-ASSUMPTION), from locked inputs and standard constants only. (TO \= TO quotient; BQ \= Berry–Quillen / Koenigs; Θ/Θ′ \= theta line; KP \= Kaloper–Padilla; KT \= Koenigs torus; BV \= Batalin–Vilkovisky; NOME \= nome q \= λ\*; AN \= anti-numerology; A26 \= present epoch; ET \= equivariant torsion 2D/3D; AUD \= integrity audit; CLS \= complete cellular-seam classification; WPL \= Wilson polar-line; FG \= flux-gluing uniqueness; F1C \= F33.1C Fourier; CUO \= charge-unit obstruction; WK \= Wilson–Koenigs orbit space; Y6 \= bivector consistency.)**

| \# | Check | Result |
| ----- | ----- | ----- |
| 1 | ω \= arg λ\* (0 \< ω \< π) | 2.2592495539 |
| 2 | ω²/2 | 2.5521042734 |
| 3 | κ \= −ln|λ\*| | 0.1148346250 |
| 4 | C\_M^sp \= 11 ln2 \+ ln3 \= ln 6144 (coexact {8³,12¹}) | 8.7232312748 |
| 5 | exact-block ln det {4³,6²} \= 8 ln2 \+ 2 ln3 | 7.7424020218 |
| 6 | nearest half-weight 11 ln2 \+ ½ ln3 (NOT 8.190) | 8.1739251306 |
| 7 | arithmetic mean of (5),(4) | 8.2328166483 |
| 8 | geometric mean of (5),(4) (NOT 8.233) | 8.2181966839 |
| 9 | Reidemeister S\_cl \= 35π/3 | 36.6519142919 |
| 10 | Ray–Singer γ\_CW·C\_M^sp \= (38/9)(11ln2+ln3) | 36.8314209382 |
| 11 | v \= M̄\_P·exp(−36.831) (Factorized Determinant) | 245.93 GeV |
| 12 | blind ρ\_Λ^{1/4} \= v²/M̄\_P | 2.484 × 10⁻⁵ eV |
| 13 | C\_odd^sp target \= 34.58/(38/9) (back-solved) | 8.1901 |
| 14 | b₂ω² (SU(3) b₂ \= −0.0216); 1+b₂ω² | −0.110; 0.890 |
| 15 | 276.6 collapse 32π²/(b\_Z A), b\_Z \= 14.25 | 276.7 (= epoch) |
| TO | TO/BCC T³ quotient (V,E,F,C); χ; Betti | (6,12,7,1); 0; (1,3,3,1) |
| TO | ∂₁∂₂ \= 0; rank ∂₁, ∂₂ | True; 5, 4 |
| TO | spec Δ₁ \= ∂₁ᵀ∂₁+∂₂∂₂ᵀ (corpus ZS-Q3) | {0³,4³,6²,8³,12¹} |
| TO | J₀²=J₁²=J₂²=I; J₀∂₁=∂₁J₁; J₁∂₂=∂₂J₂; \[J\_p,Δ\_p\]=0 | all True |
| TO | seam-odd blocks Δ₀|₋, Δ₁|₋, Δ₂|₋ | {4³},{4³},∅ |
| TO | equivariant torsion ln T₋ \= ½Σ(−1)ᵖp ln det′(Δ\_p|₋) | −3 ln2 \= −2.0794 |
| TO | 8.190 ∈ ℒ \= ℤ≥0 ln2 ⊕ ℤ≥0 ln3 ? | NO (nearest 8.1479) |
| BQ | i-tetration orbit rotation number per step | 2.25925 (= ω, 5e−6) |
| BQ | Koenigs monodromy det phase \= arg λ\* | 2.25925 \= ω (exact) |
| BQ | engineered determinant-line Berry phase ∮A\_B | 2.25925 (= ω, 4e−10) |
| BQ | ω vs gauge A (distinct bundles) | ω/A \= 28.21 |
| Θ | c₁ of det-line on Jac(Z=T²): winding of arg θ₁ / 2π | 1 (theta divisor) |
| Θ | c₁ matches a\_Z normalization ∫\_Z curv \= 1 | True |
| KP | corpus 4-form F₋=dA₃⁻, ρ\_Z=0 ≅ Kaloper–Sorbo 4-form | structural match |
| KP | IR shift δχ₋/χ₋ \~ ⟨R⟩/M̄P² (dim 6), RG-stable | 3.5×10⁻¹²¹ |
| KP | Ω\_Λ/Ω\_m \= 2e^A vs KP residual O(1) | 2.167 |
| KT | Koenigs τ \= log(λ\*)/2πi \= (ω+iκ)/2π | 0.3596 \+ 0.0183 i |
| KT | Im τ \= κ/2π \> 0 (valid elliptic curve) | 0.01828 \> 0 |
| Θ′ | c₁ of theta line for the derived τ | 1 |
| BV | F₄ \= dA₃⁻ gauge variation sF₄ | 0 (gauge-invariant) |
| BV | ∫F₄ \= dA₃ locally ⇒ d-exact ⇒ trivial in H⁰'⁴(s|d) | RETRACTED (body §5.2) |
| FORK | E\*\_need/v \= √(ρ\_obs/ρ\_blind) (= √90) | 9.49 |
| NOME | q \= e^{2πiτ} vs λ\* : |q − λ\*| | 1.4×10⁻³¹ (q \= λ\*) |
| NOME | j(τ) \= E₄³/Δ with q \= λ\* | 1.06×10⁵ \+ 2.41×10⁵ i |
| AN | e^ω near-miss for E\*/v (rejected, no mechanism) | 9.58 vs 9.49 (≈1%) |
| A26 | ν\_now \= ln(M̄P⁴/ρ\_obs) \= present epoch | 276.64 (tautological) |
| ET | 2D T² seam-odd torsion (even): ln T₋ (all chain-map signs) | ln 4 \= 1.386 (≠ 0\) |
| ET | 2D T² full Poincaré duality det′Δ₀ \= det′Δ₂ | 20.337 \= 20.337 |
| ET | 2D T² τ-odd duality det′Δ₀|₋ vs det′Δ₂|₋ (fails) | 7.742 ≠ 10.515 |
| ET | 3D T³ seam-odd torsion (odd): ln T₋ | 6 ln 2 \= 4.159 |
| AUD | ZS-M1 z\* \= i^(z\*) fixed-point residual | 1.1×10⁻³¹ |
| AUD | register Q \= 11 \= 3(X)+6(Y)+2(Z) | 11 \= 11 |
| AUD | nome q \= e^{2πiτ} \= λ\* (chain root → carrier) | |q−λ\*| \< 10⁻³⁰ |
| CLS | |Aut\_cell(BCC T³)| (signed cellular automorphisms) | 48 \= |O\_h| |
| CLS | order-2 cellular seam involutions (incl. identity) | 20 |
| CLS | seam-odd torsion image 𝒯₋ over all involutions | {−3,0,1,3⁄2,2,5⁄2}·ln2 |
| CLS | target 8.190 ∈ 𝒯₋ ? (max |𝒯₋| \= 2.079) | False |
| WPL | Wilson polar phase arg(λ\*/|λ\*|) \= ω | 2.25925 (resid 10⁻¹²) |
| WPL | flat Wilson line c₁(L\_W) \= 0; theta line c₁(Θ\_Z) \= 1 | 0 / 1 (distinct) |
| FG | flux-gluing σ(x+y)=σ(x)σ(y), σ(0)=1, σ′(0)=1 ⇒ σ=e^x | exp (Cauchy unique) |
| F1C | 2D Fourier ln det′(Δ₀|₋): 6 odd-mode pairs | 7.742 |
| CUO | Charge-Unit Obstruction E\_k(θ)=(e₋²/2Z₋)(k+θ/2π)² | χ₋ \= e₋²/(4π²Z₋) ∝ e₋²/Z₋ |
| WK | Wilson Z-block W\_Z eigenvalues; (1,−i)/√2 is the λ\* eigenvector | λ\*, λ̄\*; branch selected |
| WK | ℂ\*/⟨λ\*⟩ free & properly discontinuous (0\<|λ\*|\<1); Im τ\>0 | E\_λ\* torus, Im τ=0.0183 |
| Y6 | 2(d−1)=d(d−1)/2 unique solution d\>1 | d=4 ⇒ X=3, Y=6 |
| Y6 | four routes to 6: 3×2, C(4,2), 3\_J+3\_K, (1,0)⊕(0,1) | all \= 6 |

Computation TO (full quotient): the truncated octahedron (24 vertices, 36 edges, 14 faces) modulo Λ \= ⟨(2,2,2),(4,0,0),(0,4,0)⟩ gives (6,12,7,1) with the ZS-Q3 edge spectrum reproduced exactly. The central inversion descends to J₀,J₁,J₂ satisfying J²=I, both chain maps, and \[J\_p,Δ\_p\]=0 (errors \< 10⁻¹²). The seam-odd determinants are {4³} at p=0,1 and empty at p=2, giving ln T₋ \= −3 ln 2\. Since {4,6,8,12} factorize over {2,3}, all achievable log-determinants lie in ℒ \= ℤ≥0 ln2 ⊕ ℤ≥0 ln3 and 8.190 ∉ ℒ — the involution-independent no-go. Computation BQ (no observed input): the nonlinear i-tetration orbit rotation number, the Koenigs-linearized monodromy determinant phase, and an engineered determinant-line Berry holonomy all equal ω, distinct from the gauge A. No back-solved constant enters either computation; the comparison to 8.190 is a separate post-run block.

Computation Θ (theta line): for Z \= T² with modular parameter τ \= i, the winding of arg θ₁(u|τ) around the fundamental cell of Jac(Z) is exactly 2π, so c₁ of the determinant line is 1 — the degree of the theta divisor — equal to the F33.2A fiber-character normalization ∫\_Z curv \= 1\. The seam-odd characteristic is the odd theta characteristic θ₁ (single zero at the origin). Computation KP (structural): the corpus four-form with ρ\_Z \= 0 matches the Kaloper–Sorbo 4-form term; the admissible mixed-cocycle shifts are ⟨R⟩/M̄P² \~ 10⁻¹²¹ and (⟨R⟩/M̄P²)² \~ 10⁻²⁴¹, radiatively stable under the KP sequestering constraint.

Computation KT (Koenigs torus): the multiplier log λ\* \= −κ \+ iω gives τ \= log λ\*/(2πi) \= (ω \+ iκ)/2π \= 0.3596 \+ 0.0183 i with Im τ \> 0, so the Koenigs quotient ℂ\*/⟨λ\*⟩ is a genuine elliptic curve and Z \= T² is derived. Computation BV: F₄ \= dA₃⁻ is gauge-invariant under the reducible symmetry, and ∫F₄ is a closed non-exact top-form — an admissible H⁰'⁴(s|d) cocycle. Computation FORK: the enhancement needed to lift the blind 2.48 × 10⁻⁵ eV to the observed 2.24 × 10⁻³ eV is E\*\_need/v \= √90 \= 9.49, which is not derived from (A, Q) and is declined as numerology (F33-G11).

Computation NOME: the nome q \= e2πiτ \= λ\* to 10⁻³¹ — the elliptic-curve complex structure is the i-tetration multiplier itself; j(τ) is then a determined function of λ\* with no forced (A, Q) relation. Computation AN (anti-numerology): the √90 enhancement is numerically close to eω \= 9.58 (≈ 1%) but eω of a rotation angle has no mechanism and is rejected; all other matches need fitted exponents. Computation A26: νnow \= ln(M̄P⁴/ρ\_obs) \= 276.64 reproduces the present-epoch constant, confirming Branch B is tautological.

# **Appendix B. Falsification Gates**

| Gate | Layer | Condition |
| ----- | ----- | ----- |
| F33-G1 | Mathematical | A standard closed even-dim or gauge-mode carrier nonetheless yields ρ\_Λ,Z ≠ 0\. |
| F33-G5 | Mathematical | The complete cellular-seam classification (48 automorphisms / 20 involutions) is shown incomplete, or a 21st order-2 cellular action is exhibited. |
| F33-G2′ | Mathematical | The Z-fibration degenerates (γ\_Z ⊂ Z), so C₃⁻ \= a\_Z ∧ Ω\_Z vanishes. |
| F33-G2″ | Theoretical | Berry–Quillen holonomy ≠ e^{iω}, or a\_Z carries only the gauge A; θ\_Z \= ω RETRACTED. |
| F33-G3 / G5 | Meta / zero-parameter | g₋²(M̄\_P), b₀, the portal coefficient, or the odd scale is an external or inverted-observed input. |
| F33-G4 | Non-perturbative | A sequestering failure lifting |δρ\_Λ/ρ\_Λ| above ε\_rad (mixed cocycles survive in the IR). |
| F33-G6 | Meta / anti-numerology | C\_odd^sp obtained by fitting a non-integer weight to 8.190 rather than from the seam-odd spectrum. |
| F33-G7 | Physical | ε\_N(ω) \> 1% but the cumulant series is truncated at b₂ for cosmology. |
| F33-G8 | Observational | Computed ρ\_Λ inconsistent with data (no retuning); Branch B claimed with K(q) free yet zero-parameter asserted. |
| F33-G9 | Meta / anti-numerology | χ₋ or C\_odd^sp claimed parameter-free using observed ρ\_Λ, a chosen scale, base-10, a half-weight, or a back-solved exponent. |
| F33-G10 | Meta / zero-parameter | The KP non-spectral route claimed to fix ρ\_Λ parameter-free while the 4-form flux is left free or not matched to ΔE₋(ω). |
| F33-G2theta | Mathematical | The corpus forces a carrier whose Koenigs quotient is not genus-1, or fixes τ ≠ (ω+iκ)/2π — voids the c₁=1 identification and θ\_Z \= ω. |
| F33-G11 | Meta / anti-numerology | The value-closure fork resolved by fitting √90 or 90 to A, Q rather than deriving the enhancement. |
| F33-G1C | Mathematical | The 2D counterexample ln T₋ \= ln 4 ≠ 0 is shown to be in error (restoring odd-dim uniqueness), or ZS-Q3 is shown not to live on the 3D X-ambient complex (breaking the assignment). |
| F33-G2orb | Mathematical | The F0 Wilson Z-block does not have λ\* as a simple eigenvalue, or the seam chirality (1,−i)/√2 does not select the λ\* branch; the orbit-space identification ℂ\*/⟨λ\*⟩ \= E\_λ\* is RETRACTED. |
| F33-G8D | Theoretical | The field-representation 6 is used to assert a 6D spacetime without an independent metric, or the rank-2 internal-cycle reduction yields a V\_Σ, g₆, or e₆ inconsistent with the corpus geometry. |

# **Appendix C. Anti-Numerology Audit of C\_odd^sp (corrected)**

| Candidate | Finding | Verdict |
| ----- | ----- | ----- |
| b₀ \= 14.25 (fourth power) | 32π²/(b\_Z A) \= 276.6 \= present epoch (A26) | CLOSED-NEGATIVE (tautology) |
| exact block {4³,6²} \= 7.742 | corpus-native; misses target | ≠ 8.190 |
| coexact {8³,12¹} \= 8.723 | corpus-native (= C\_M^sp); misses | ≠ 8.190 |
| seam-odd equivariant torsion \= −2.079 | canonical central inversion (full complex) | ≠ 8.190 |
| 8.190 ∈ ℒ \= ℤ≥0 ln2 ⊕ ℤ≥0 ln3 ? | Q3 eigenvalues factor over {2,3}; 8.190 ∉ ℒ | CLOSED-NEGATIVE (decisive) |
| nearest half-weight 11 ln2+½ ln3 \= 8.174 | ½ not spectrum-derived | numerology if fitted |
| arith. mean 8.233 / geom. mean 8.218 | not derived combinations | no mechanism |

**Two lattices, kept distinct (essential).** The “∈ ℒ \= ℤ≥0 ln2 ⊕ ℤ≥0 ln3” row refers only to the *ordinary subdeterminants* of ZS-Q3 — the non-negative integer lattice in which the spectral C\_odd^sp route would live (nearest point 7 ln2 \+ 3 ln3 \= 8.148). It is *not* the same set as the seam-odd determinant-torsion image 𝒯₋ \= {−3, 0, 1, 3⁄2, 2, 5⁄2}·ln 2, a *signed half-lattice* containing negative and half-integer multiples (e.g. the canonical −3 ln 2). The target 8.190 misses *both* — ℒ (ordinary, non-negative) and 𝒯₋ (signed torsion) — by independent margins. Conflating the two was the v1.6 error this version corrects; they are reported as separate scopes throughout (§6.4).

The decisive entry is the last: because every Q3 eigenvalue factorizes over {2,3}, every achievable spectral / equivariant log-determinant lies in the integer lattice ℒ, and 8.190 is provably outside ℒ. No seam involution can produce it; the spectral route is CLOSED-NEGATIVE. The observed value is never an input to the computation.

# **Appendix E. Issue-Tree Exploration Record (v1.8)**

v1.8 integrates two further peer reviews whose verdict was “direction and central computation succeeded, but document/code integration unfinished.” The issue-tree separates the closable items from the deferred ones.

## **E.1 Long list → issue list**

Step 0 (long list, 7): **A** the inverted χ₋ formula (central theorem); **B** the non-standalone verifier (sidecar dependence); **C** the v1.6/v1.7 remnants in §10/§2.3/counts/filenames; **D** closing physical Z via Wilson orbit space; **E** re-deriving (3,6,2) independently of Q; **F** the F33.3B KV over-flattening and the BV over-claim; **G** the absolute-χ₋ 6D route. Step 1 (issue list, 4): **1**\=\[A+B+C\] the must-fix integration, **2**\=\[D\] Wilson–Koenigs orbit space, **3**\=\[E+F\] dimensional re-derivation, KV split, BV demotion, **4**\=\[G\] the internal-cycle reduction (deferred to F34).

## **E.2 Traversal and resolutions**

| Issue | Resolution (computation) | Outcome |
| ----- | ----- | ----- |
| 1A | E\_k=(e₋²/2Z₋)(k+θ/2π)² ⇒ ∂²E/∂θ² \= e₋²/(4π²Z₋) | χ₋ ∝ e₋²/Z₋ (corrected, all sites) |
| 1B | standalone builder reproduces (6,12,7), Δ₁, 48/20 with no sidecar | verifier self-contained, 17/17 |
| 1C | rewrote §10; removed §2.3 remnants; fixed v1.7 filenames; 31-result counts | remnants cleared |
| 2 | W\_Z w=λ\*w on ℂ\*; free+properly disc.; (1,−i)/√2 → λ\* | Z=E\_λ\* DERIVED-under-Orbit-Equiv. |
| 3a | 2(d−1)=d(d−1)/2 ⇒ d=4; four routes to 6; split math/phys | X=3,Y=6 math PROVEN; phys COND |
| 3b | KV split; BV demoted to DERIVED-CONDITIONAL (S\_BV → d²=0) | statuses honestly lowered |
| 4 | Y₆=M₄×Σ₂ internal-cycle reduction gives χ₋=e₋²/(4π²Z₋) | F33.8D DERIVED-CONDITIONAL → F34 |

Step 4 (convergence): two passes; the second confirmed the orbit-space and bivector theorems are genuinely independent (the bivector route uses only Z \= 2 and Lorentz Λ², never Q \= 11), that the χ₋ correction propagated to all sites (§9.4, §9.5, ledger, verifier), and that the representation “6” and a 6D spacetime are now explicitly separated. Converged. **Step 5 (score):** two OPEN items are closed — physical Z \= E\_λ\* (DERIVED-under-Orbit-Equivalence) and the register dimensions (math PROVEN) — one central sign error is fixed, two over-claims (BV master, Y-6D uplift) are lowered to their honest status, and the verifier is reproducible. The remaining absolute-χ₋ gap is the bounded F33.8D reduction handed to ZS-F34. The firewall is unchanged: ρ\_obs enters only the post-run zone.

# **Appendix F. Integrity Audit (v1.0–v1.8)**

v1.8 applies the nine-step verification protocol (§3.1–3.9) to the cumulative 31-result ledger and to the cross-version dependency chain. All checks pass; the table summarizes them.

| Step | Check | Result |
| ----- | ----- | ----- |
| §3.1 parameters | Only (A, Q) \= (35/437, 11\) enter; no fitted constant; ρ\_obs never an input | PASS |
| §3.2 chain | ZS-M1 z\* \= i^(z\*) → λ\*, κ, ω, ω²/2, C\_M^sp, v, τ, q \= λ\* all flow from one root | PASS (resid 10⁻³¹) |
| §3.2 dimensions | Z 2D (Koenigs torus, θ\_Z) vs X 3D (BCC T³, ZS-Q3) not conflated; Q \= 11 \= 3+6+2 | PASS |
| §3.3 data | Frozen w \= −1 branch consistent with ZS-A28/A29 and DESI DR2 / Planck | PASS |
| §3.4 legend | Every ledger tag is a legend value (legend expanded in v1.7); statuses consistent across v1.0–v1.8 | PASS |
| §3.5 gates | Falsification gates F33-G1…G12, G1C, G2WPL, G2orb, G8D present and current | PASS |
| §3.6 references | PROVEN imports (Ray–Singer, Cheeger–Müller, Koenigs/Milnor, Quillen, BBH, Kaloper–Padilla, Aczél) cited | PASS |
| §3.7 structure | Epistemic legend, ledger, cross-version notes, per-cluster sections present | PASS |
| §3.9 firewall | Anti-numerology: e^ω near-miss rejected; B3 value CLOSED-NEGATIVE-under-R1–R3; ρ\_obs only in fenced post-run zone | PASS |

**Cross-version status reconciliation.** Statuses move only with a recorded driver: θZ \= ω rose OPEN → DERIVED-CONDITIONAL (v1.2) → DERIVED (v1.4) and was then *corrected* to DERIVED-under-WPL (v1.7) after the c₁ error was found; F33.4B rose to DERIVED (v1.4) and was *lowered* to DERIVED-CONDITIONAL with the ∫F₄ class retracted (v1.7); the vacuum *value* fell to CLOSED-NEGATIVE-under-R1–R3 (v1.5/v1.7); F33.1C uniqueness is CLOSED-NEGATIVE (v1.7, counterexample); and the spectral no-go was rescoped to the complete cellular-seam classification (v1.7). In v1.8: physical Z \= E\_λ\* was closed to DERIVED-under-Orbit-Equivalence via the Wilson–Koenigs orbit space; the bivector consistency was split into F33.3A′-math (PROVEN) and F33.3A′-phys (DERIVED-CONDITIONAL); the BV master action was lowered from PROVEN to DERIVED-CONDITIONAL once the explicit abelian ghost-tower antibracket was found to be exhibited only as a reduction to d² \= 0; and the inverted χ₋ was corrected to e₋²/(4π²Z₋) consistently through §9.4, §9.5, the ledger, and the verifier. No earlier result was silently reversed: each transition is recorded in the Version History with its driver. The single dimensional subtlety — that the seam-odd determinant of §6 is computed on a 3D complex while the mediation angle lives on a 2D one — is resolved by the sector split (Appendix audit row §3.2): they are different invariants on different register sectors, X (3D) and Z (2D), and are never interchanged.

# **References**

\[1\] D. B. Ray and I. M. Singer, Adv. Math. 7, 145 (1971).

\[2\] J. Cheeger, Ann. Math. 109, 259 (1979).

\[3\] W. Müller, Adv. Math. 28, 233 (1978).

\[4\] E. Witten, Phys. Rev. Lett. 81, 2862 (1998).

\[5\] C. Bonati, M. Cardinali, and M. D'Elia, Phys. Rev. D 98, 054508 (2018), arXiv:1807.06558.

\[6\] M. Cè, C. Consonni, G. P. Engel, and L. Giusti, Phys. Rev. D 92, 074502 (2015), arXiv:1506.06052.

\[7\] M. Cè, M. García Vera, L. Giusti, and S. Schaefer, Phys. Lett. B 762, 232 (2016), arXiv:1607.05939.

\[8\] G. Barnich, F. Brandt, and M. Henneaux, Phys. Rept. 338, 439 (2000), arXiv:hep-th/0002245.

\[9\] M. Henneaux, B. Knaepen, and C. Schomblond, Commun. Math. Phys. 186, 137 (1997).

\[10\] J. Cheeger and J. Simons, Lecture Notes in Math. 1167 (Springer, 1985), p. 50; C. Bär and C. Becker, Differential Characters, Lecture Notes in Math. 2112 (Springer, 2014).

\[11\] D. Fiorenza, H. Sati, and U. Schreiber, arXiv:1207.5449 (2012).

\[12\] N. Kaloper, A. Padilla, D. Stefanyszyn, and G. Zahariade, Phys. Rev. Lett. 116, 051302 (2016); N. Kaloper and A. Padilla, Phys. Rev. Lett. 118, 061303 (2017), arXiv:1606.04958.

\[13\] N. Kaloper and L. Sorbo, Phys. Rev. Lett. 102, 121301 (2009).

\[14\] F. R. Klinkhamer and G. E. Volovik, Phys. Rev. D 77, 085015 (2008), arXiv:0711.3170; Phys. Rev. D 80, 083001 (2009), arXiv:0905.1919.

\[15\] V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, JHEP 02, 082 (2023), arXiv:2206.10780.

\[16\] DESI Collaboration, M. Abdul-Karim et al. (2025); M. Cortês and A. R. Liddle, Mon. Not. R. Astron. Soc. Lett. 544, L121 (2025).

\[17\] Planck Collaboration, N. Aghanim et al., Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209.

\[18\] Quillen, Funct. Anal. Appl. 19, 31 (1985) (determinant line bundles); M. V. Berry, Proc. R. Soc. Lond. A 392, 45 (1984) (geometric phase).

\[18b\] G. Koenigs, Ann. Sci. Éc. Norm. Supér. (3) 1, 3 (1884) (linearization at an attracting fixed point); J.-M. Bismut, H. Gillet, and C. Soulé, Commun. Math. Phys. 115, 49 & 79 (1988) (Quillen metric and the determinant-line connection).

\[18c\] D. Quillen, Funct. Anal. Appl. 19, 31 (1985) (determinant line of ∂̄ and the theta line bundle on the Jacobian, c₁ \= 1); D. Mumford, Tata Lectures on Theta I (Birkhäuser, 1983\) (theta divisor, degree 1).

\[18d\] J. Milnor, Dynamics in One Complex Variable (Princeton, 3rd ed., 2006\) (Koenigs linearization; the quotient ℂ\*/⟨λ\*⟩ as an elliptic curve / Ecalle–Koenigs torus).

\[18e\] J. Aczél, Lectures on Functional Equations and Their Applications (Academic Press, 1966\) (the multiplicative Cauchy equation σ(x+y)=σ(x)σ(y) ⇒ σ=e^{cx}; flux-gluing exponential uniqueness).

\[19\] Z-Spin Collaboration internal: ZS-F32 (odd-sector frontier); ZS-S4 §6.12 (Factorized Determinant, C\_M^sp); ZS-Q3 / ZS-M6 (Hodge edge spectrum, BCC T³); ZS-F2 §11.8 (J\_Z-odd gauge mode); ZS-F9 (ρ\_Z \= 0); ZS-F4 (∮ω \= A); ZS-F5 (dim Z \= 2); ZS-F18 (Bridge Four); ZS-M1 (i-tetration z\*, ω); ZS-A22 (barrier B2); ZS-A26 (relational law; 276.6; central-shift); ZS-A27 (exhaustion target); ZS-A28 (eighth-power; A–Q-only no-go; spectral-route retirement); ZS-A29 (i-tetration orbit vs DESI); ZS-F27 (seam J \= F²S); ZS-F34 (six-dimensional charge unit, companion paper, in preparation).

# **Version History**

**v1.8 (May 2026):** Closure and integration update from two further peer reviews. Closed two open items, corrected a sign error in the central theorem, and synchronized statuses. (1) Physical fibre: added the Wilson–Koenigs orbit-space theorem — the F0 Wilson Z-block acts as w ↦ λ\*w on ℂ\*, a free properly-discontinuous action whose quotient ℂ\*/⟨λ\*⟩ \= E\_λ\* is the orbit space; “Z \= E\_λ\*” is raised to DERIVED-under-Orbit-Equivalence (PROVEN as the orbit space; the observable orbit-invariance is the one remaining postulate), with the seam eigenvector (1,−i)/√2 selecting the λ\* branch (§3.2.4). (2) Register dimensions: added the bivector–complexification consistency 2(d−1) \= d(d−1)/2 ⇒ d \= 4, X \= 3, Y \= 6, re-deriving Q \= 11 without assuming it via four routes to 6, split into F33.3A′-math (PROVEN) and F33.3A′-phys (DERIVED-CONDITIONAL) (§4.1). (3) F33.3B split into IMPORTED-PROVEN-within-model / NON-CLAIM / DERIVED-CONDITIONAL / OPEN-executable (§4.3). (4) Charge-Unit Obstruction: corrected the inverted formula to χ₋ \= e₋²/(4π²Z₋) ∝ e₋²/Z₋ consistently through §9.4, §9.5, the ledger, and the verifier; added the internal charge-unit reduction F33.8D under an explicit rank-2 internal-cycle ansatz, separating the representation-dimension “6” from a 6D spacetime, pointing to ZS-F34 (§9.5). (5) Lowered the BV master action from PROVEN to DERIVED-CONDITIONAL, giving the explicit abelian ghost-tower S\_BV whose master equation reduces to d² \= 0 (§5.2). Editorial closure: rewrote the §10 conclusion (which carried v1.3/v1.6 text), removed the “Open Gate / what remains OPEN” remnants in §2.3, separated the ordinary subdeterminant lattice from the signed torsion image in Appendix C, updated the gates (G2orb, G8D) and Appendix F to v1.8, fixed the v1.7 verifier filenames, unified all counts (31-result ledger), and made the verification script standalone — it builds the BCC T³ quotient and the 48/20 classification inline with no sidecar files (17/17 ASSERT PASS), computes the 2D parity torsion from the Fourier spectrum, and reclassifies Cauchy uniqueness as IMPORTED-PROVEN. **v1.7 (April 2026):** Status-correction and classification update integrating a detailed peer review. Lowered three over-claimed load-bearing statuses and retracted one incorrect cohomology claim, while adding four computation-backed results. (1) θ\_Z \= ω: the v1.3–v1.6 identification was flawed (a flat connection has c₁ \= 0 and cannot be the degree-1 theta line); v1.7 separates a flat Wilson polar-line L\_W (c₁ \= 0, holonomy e^{iω} \= λ\*/|λ\*| from the polar unitary part of the linearized mediation operator) from the theta line Θ\_Z (c₁ \= 1, fibre flux), giving θ\_Z \= ω as DERIVED-under-WPL and demoting the engineered Berry loop to a realizability check (§3.2). (2) F33.4B: retracted the claim that ∫F₄ is a nontrivial local H⁰'⁴(s|d) class (it is d-exact) → OPEN-GLOBAL; wrote the two-four-form action S\_ZS-seq with the corpus F±, proved the BV master equation, and closed the gluing free-function by the exponential-uniqueness theorem σ \= e^x (Cauchy) (§5.2). (3) F33.5: replaced the over-scoped non-negative-lattice no-go (which contradicted the canonical −3 ln 2\) with the complete cellular-seam classification — 48 automorphisms, 20 involutions, torsion image {−3,0,1,3⁄2,2,5⁄2}·ln2, target disjoint — exact for all cellular involutions on this complex (§6.4). (4) F33.1C: the 2D parity-restricted torsion ln T₋ \= ln 4 ≠ 0 is a counterexample, so odd-dimensional uniqueness is CLOSED-NEGATIVE, with terminology corrected to “seam-parity-restricted determinant torsion” (§2.3). Added the canonical compact 3-form branch (b₂ₙ \= 0, PROVEN-under-canonical-action, §7), closed the dynamical-w Outlook as CLOSED-NEGATIVE under the minimal action (§8.2), and proved the Charge-Unit Obstruction (topology fixes the flux number, not the dimensionful unit; the strongest value terminus, §9.4). Reclassified the verification suite into ASSERT-COMPUTED / IDENTITY-REPORTED / STRUCTURAL-ASSUMPTION, removing the declarative passes. Fixed editorial errors (ledger count, §10 and code-availability version strings, the F33-G1C duplicate, the log det′ notation, the Ω\_Λ/Ω\_m “same order” label, and the legend coverage). New title; references \[18e\] (Aczél) added. **v1.6 (April 2026):** Integrity-audit update. Tested the F33.1C closure (odd-dimensional carrier uniqueness): since the seam is the central inversion, orientation-preserving in even dimensions, one might hope the seam-odd equivariant torsion vanishes on the 2D even carrier. Explicit computation REFUTES this — on a 2D T² the τ-odd Poincaré self-duality fails (det′Δ₀|₋ \= 7.742 ≠ det′Δ₂|₋ \= 10.515 under every chain-map sign), giving ln T₋ \= ln 4 ≠ 0, while the 3D T³ gives 6 ln 2 — so the even-dimensional equivariant torsion is genuinely nonzero (confirming v1.1's Problem B) and F33.1C is CONFIRMED-OPEN (§2.3.1). Recorded the sector assignment (odd vacuum on the 3D X-ambient via ZS-Q3, θ\_Z on the 2D Z Koenigs torus) as DERIVED-from-structure (§2.3.2). Added a full integrity audit (Appendix F): the ZS-M1 z\* dependency chain (residual 10⁻³¹), the Z-2D / X-3D sector separation (Q \= 11 \= 3+6+2), and the nine-step protocol §3.1–3.9, all passing. Added the equivariant-torsion and audit computations to Appendix A, gate F33-G1C, and one ledger row (25 total). **v1.5 (March 2026):** Deep-exploration (issue-tree) update executing the three v1.4 next-steps. F33.2B: proved the elliptic-curve nome q \= e^{2πiτ} \= λ\* (the carrier's complex structure is the i-tetration multiplier), confirming cross-version consistency with ZS-M and F27 (§3.2.3); reported j(τ) without forcing an (A, Q) relation. F33.8: completed the absolute-value question as CLOSED-NEGATIVE by exhausting three independent routes — the spectral lattice no-go (v1.2), Branch A whose √90 enhancement is not derivable from (A, Q) (the e^ω near-miss is rejected as the exponential of a rotation angle with no mechanism, F33-G11), and Branch B which gives ρ\_Λ \= M̄\_P⁴e^{−276.6} \= ρ\_obs at the right magnitude but tautologically since the present epoch is defined by ρ\_obs (§9.3). Added the nome, j(τ), anti-numerology and present-epoch computations to Appendix A, two ledger rows (24 total). **v1.4 (March 2026):** Deep-exploration (issue-tree) update executing the three v1.3 next-steps. F33.2B: derived the genus-1 carrier itself — the Koenigs quotient ℂ\*/⟨λ\*⟩ of the i-tetration multiplier is an elliptic curve with τ \= (ω \+ iκ)/2π fixed by (A, Q) — removing the v1.3 structural input, so θ\_Z \= ω is now DERIVED outright (§3.2.2). F33.4B: established BV-admissibility of the Kaloper–Sorbo term (F₄ \= dA₃⁻ gauge-invariant, ∫F₄ a nontrivial H⁰'⁴(s|d) cocycle), promoting the local IR sequestering to DERIVED (§5.2). F33.8: attempted the B3 value-closure and found the parameter-free-vs-magnitude fork (blind value 90× short; reconciliation needs √90 in E\*, declined as numerology), so the value stays OPEN with the obstruction now precise (§9.3). Added the Koenigs-torus, BV, and fork computations to Appendix A, gates F33-G11 and the revised G2θ, the Milnor reference, and four ledger rows (22 total). **v1.3 (March 2026):** Deep-exploration (issue-tree) update executing the three v1.2 next-steps. F33.2B: on the genus-1 carrier Z \= T², constructed the determinant line over Jac(Z) as the theta line bundle and verified c₁ \= 1 (winding of arg θ₁) \= the F33.2A fiber-character normalization ∫\_Z curv \= 1, identifying a\_Z with the Quillen/BGS connection and the seam-odd sector with the odd theta characteristic — promoting θ\_Z \= ω from DERIVED-CONDITIONAL to DERIVED (structural input: Z \= T², forced by ω ≠ 0). F33.4B: identified the corpus four-form (ρ\_Z \= 0\) with the Kaloper–Sorbo / Kaloper–Padilla sequestering 4-form, making the IR radiative-stability bound RG-stable via a PROVEN external mechanism. F33.8 (new §9.2): identified the KP sequestering global constraint as the non-spectral central normalizer B3 requires (HYPOTHESIS-strong), with value-closure open since the 4-form flux is free. Added the theta-line and KP computations to Appendix A, gates F33-G10 and F33-G2theta, the Quillen/Mumford references, and two ledger rows (20 total). **v1.2 (March 2026):** Deep-exploration (issue-tree) update. Executed the three v1.1 next-steps. F33.5: built the full truncated-octahedron BCC T³ quotient explicitly (∂₁, ∂₂ reproducing Δ₁ \= {0³,4³,6²,8³,12¹} and Betti (1,3,3,1)), verified the canonical central-inversion seam involution on every degree (J²=I, both chain maps, \[J\_p,Δ\_p\]=0), computed the seam-odd equivariant torsion ln T₋ \= −3 ln 2, and proved the involution-independent lattice no-go (8.190 ∉ ℤ≥0 ln2 ⊕ ℤ≥0 ln3) — closing the spectral route to the vacuum scale as CLOSED-NEGATIVE and strengthening A28. F33.2B: computed the i-tetration orbit rotation number, the Koenigs monodromy determinant phase, and an engineered determinant-line Berry holonomy (all \= ω, distinct from A), promoting θ\_Z \= ω from OPEN to DERIVED-CONDITIONAL. Branch B kept OPEN (Outlook). Added Appendix E (issue-tree record), the Koenigs and Bismut–Gillet–Soulé references, and three new ledger rows (18 total). **v1.1 (March 2026):** Major revision after internal review. Title weakened from “UV Completion” to “Conditional UV Reduction.” Corrected three numerical errors (8.174 ≠ 8.190; geometric mean 8.218 ≠ 8.233; coexact {8³,12¹}). Reclassified statuses into a 16-result Claim Ledger (no DERIVED/PROVEN-under-product over-assignment). Added a cross-version consistency table resolving the A28/A29 cosmology conflict and the A28 spectral-route retirement. Split F33.1 into 1A (IMPORTED-PROVEN even-dim no-go), 1B (DERIVED-CONDITIONAL Z-application; dropped the erroneous ind⁻(D\_Z)=β₀=1), 1C (OPEN equivariant uniqueness). Split F33.2 into 2A (PROVEN-under-product transgression; corrected the 1/2π normalization) and 2B (OPEN Berry–Quillen holonomy). Split F33.3 into 3A/3B/3C/3D with retitled “classification and benchmark.” Pivoted F33.4 to a BRST-Only Isolation No-Go plus an IR radiative-stability bound. Promoted F33.5 to the paper's center with an explicit octahedral cellular seam involution (seam-odd exact block \= 4.159) and an anti-fit firewall admitting three outcomes. Retitled F33.6 with a controlled-truncation gate. Split F33.7 into a frozen w \= −1 branch (main) and a dynamical-q Outlook. **v1.0 (March 2026):** Initial release; consolidated A31; superseded by v1.1. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.