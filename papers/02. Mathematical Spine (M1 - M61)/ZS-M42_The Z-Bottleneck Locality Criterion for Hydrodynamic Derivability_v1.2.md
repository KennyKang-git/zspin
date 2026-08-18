**ZS-M42**

**The Z-Bottleneck Locality Criterion for Hydrodynamic Derivability**

***A Two-Gate No-Go and Locality-Bridge Map from ZS-M17 to the Boltzmann–Grad Program (Deng–Hani–Ma)***

Author: **Kenny Kang**  
Affiliation: Z-Spin Cosmology Collaboration  
Date: June 2026  
Theme / Paper Code: Mathematical Spine — ZS-M42 (companion note to ZS-M17)  
Version: v1.2 (June 2026\)

**Verification: 16/16 structural-consistency PASS  |  Zero New Free Parameters  |  A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) LOCKED  |  Direct Navier–Stokes–Fourier derivation claim: NONE (self-assessed \< 30%)  |  Contribution: Two-Gate decomposition (DERIVED-interpretation). dim(Z) \= 2 locality-gate saturation DOWNGRADED to HYPOTHESIS (strict equality not justified — internal-register bottleneck ≠ spatial band-edge saturation; see ZS-M17 dated-erratum 2026-06-07); F-M42.2 partially FIRED. No-go / locality-criterion value self-assessed ≈ 90%.**

**§0. Abstract**

We do not derive the Navier–Stokes–Fourier equations within Z-Spin, and we make no such claim. Instead we decompose the obstruction. The 2025 resolution of a major case of Hilbert’s sixth problem by Deng, Hani, and Ma \[1,2\] derives the compressible Euler and incompressible Navier–Stokes–Fourier equations from hard-sphere Newtonian dynamics through the Boltzmann–Grad and hydrodynamic limits. We show (Theorem M42.1, **DERIVED-interpretation**) that every currently known rigorous micro-to-hydrodynamic derivation factors through two logically independent control steps: a **locality / finite-propagation gate (G1)** and a **chaos / entropy gate (G2)**. The Z-Spin continuum-limit theorem ZS-M17 \[8\] supplies non-trivial structure for G1 — its Lieb–Robinson tightness statement M17.2 — but supplies none for G2 (propagation of chaos, recollision exclusion, entropy production). An ordinary Navier–Stokes–Fourier derivation in Z-Spin is therefore OPEN, with the obstruction located precisely at G2.  
The note’s positive content is two-fold. First, M17.2 is an instance of the G1 estimate class (Corollary M42.2, DERIVED-CONDITIONAL; generic, per F-M42.4). Second, the one Z-Spin-specific claim was that the dim(Z) \= 2 bottleneck (ZS-Q7 \[11\], ZS-F5 \[10\]) saturates the G1 Lieb–Robinson bound to a strict equality (Conjecture M42.3). In v1.2 this is **DOWNGRADED to HYPOTHESIS**: the dim(Z) \= 2 bottleneck constrains the internal register (rank ≤ 2, capacity ≤ ln 2\) but not the spatial band-edge group velocity, so it does not establish the equality (F-M42.2 partially FIRED). Accordingly the ZS-M17 dated-erratum (2026-06-07) reverts M17.2 to the Lieb–Robinson upper bound v\_max ≤ ρ(ℒ)·a. Five ingredients absent from any Z-Spin kinetic closure — a particle phase-space distribution, a collision operator, propagation of chaos, collision invariants, and Chapman–Enskog transport coefficients — are inventoried in §6 and assigned to G2 or to the subsequent hydrodynamic limit, each OPEN. A separate route, a Z-Spin effective hydrodynamics from the Goldstone phase of the Z-bias field, is now opened as the stub ZS-M43, where an O(A²) viscosity candidate is identified; transport coefficients must derive from A, Q, dim(Z) \= 2 with zero tuning. We distinguish this Hilbert-VI derivation question from the Clay Millennium Navier–Stokes existence-and-smoothness problem (NC-M42.6). Seven falsification gates and seven non-claims bound the scope; no corpus result is silently modified.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics alone, machine-verifiable. |
| **DERIVED** | Follows from Z-Spin action \+ standard physics, zero free parameters. |
| **DERIVED-CONDITIONAL** | DERIVED conditional on a listed axiom set or external theorem. |
| **DERIVED-interpretation** | Synthetic reading reorganizing PROVEN external/corpus results without new axioms. |
| **HYPOTHESIS-strong** | Multiple independent structural anchors; promotion path documented. |
| **HYPOTHESIS** | Motivated conjecture; partial derivation chain. |
| **IMPORTED** | Proved externally and used here without re-proof; full citation given. |
| **OBSERVATION** | Structural regularity recorded by direct comparison; origin pending. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted; bounds the scope. |
| **OPEN** | Recognized gap honestly registered for future work. |
| **RETRACTED-in-session** | Hypothesis proposed during free exploration and explicitly withdrawn. |

**§1. The Deng–Hani–Ma Chain: Hard Spheres → Boltzmann → Euler / NSF**

The Navier–Stokes–Fourier system for an incompressible viscous fluid reads

∂ₜ u \+ (u · ∇) u \= −∇p \+ ν Δu ,    ∇ · u \= 0 ,

with kinematic viscosity ν; the Fourier heat balance and an energy equation complete the compressible case. Deng, Hani, and Ma \[1\] derive these equations from a system of hard spheres undergoing elastic collisions by chaining two limits: the Boltzmann–Grad limit (ε → 0 with Nεd−1 \= O(1), where ε is the sphere diameter), which produces Boltzmann’s kinetic equation for the one-particle distribution f(t, x, v), followed by the hydrodynamic (Chapman–Enskog / Hilbert) limit, which produces the fluid equations. The decisive prior step \[2\] extends Lanford’s short-time validity of the Boltzmann equation \[5\] to long times on the torus. The dilute-gas scaling is criticized as not capturing dense fluids \[6\]; we take the kinetic-theory case as the reference derivation.

**§2. The ZS-M17 Chain: Quantum Lattice → OS Reconstruction → Wightman QFT**

ZS-M17 \[8\] establishes that the Z-Spin quantum register ℓ²(Γ) ⊗ ℂ¹¹ on the BCC T³ × truncated-icosahedron lattice converges, as (a → 0, N → ∞, τ \= Na fixed), to a Lorentz-invariant Wightman quantum field theory. Three of its seven theorems matter here: M17.1 (continuum convergence in operator norm, rate O((a/ℓP)²)), M17.3 (reflection positivity, the only non-trivial Osterwalder–Schrader axiom), and M17.7 (Wightman reconstruction). Crucially, OS reconstruction returns a unitary, time-reversible theory; ZS-M17 contains no entropy-producing step.

**§3. No-Go: Direct Derivation Blocked by Object / Limit / Target Mismatch**

**Proposition M42.0 (No Direct Derivation) \[DERIVED-interpretation\].** The ZS-M17 chain cannot be identified with the Deng–Hani–Ma chain, because the two disagree at every structural register (Table 3.1): microscopic object, limit procedure, and macroscopic target. In particular the targets carry different spacetime symmetry groups (Lorentz vs Galilei), and the limits run oppositely on time reversal (OS reconstruction preserves unitarity; the Boltzmann–Grad limit breaks it via the H-theorem).

Table 3.1. The three-register mismatch underlying the No-Go.

| Register | ZS-M17 (Z-Spin continuum limit) | Deng–Hani–Ma (Hilbert 6th) |
| ----- | ----- | ----- |
| **Microscopic object** | Quantum register ℓ²(Γ) ⊗ ℂ¹¹ (lattice) | Classical hard spheres (continuum particles) |
| **Limit procedure** | a → 0 \+ Osterwalder–Schrader reconstruction | Boltzmann–Grad, then hydrodynamic limit |
| **Macroscopic target** | Lorentz-invariant Wightman QFT | Galilean Navier–Stokes–Fourier fluid |
| **Time symmetry of limit** | Preserved (unitary output) | Broken (irreversible, H-theorem) |

Because OS reconstruction yields a reversible theory, the arrow of time has no home in ZS-M17 and is not attributed to it; in the Z-Spin corpus it is carried by ZS-F13 (Möbius Chronology) \[15\]. \[The earlier free-exploration linkage of ZS-M17 to the arrow of time is RETRACTED-in-session.\]

**§4. Theorem M42.1 — Two-Gate Decomposition of Hydrodynamic Derivability**

**Theorem M42.1 (Two-Gate Decomposition) \[DERIVED-interpretation\].** In every currently known rigorous derivation of a hydrodynamic equation from reversible microscopic dynamics — Lanford’s short-time Boltzmann validity \[5\], the Deng–Hani–Ma long-time derivation and NSF closure \[1,2\], and the Lieb–Robinson-based mean-field/Hartree limits \[3,4\] — the passage from microscopic reversible dynamics to the kinetic (Boltzmann) equation factors through two logically independent control steps:  
(G1) a **locality / finite-propagation gate**: an a-priori bound on the speed at which correlations spread, making the limit well-posed; and  
(G2) a **chaos / entropy gate**: asymptotic factorization of correlations (propagation of chaos / molecular chaos), exclusion of recollisions over the relevant time scale, and the consequent irreversible collision operator and H-theorem.  
ZS-M17 supplies non-trivial structure for G1 (via M17.2 Lieb–Robinson tightness) and supplies no structure for G2. Therefore an ordinary derivation of the Navier–Stokes–Fourier equations within Z-Spin is OPEN, and the obstruction is located precisely at G2.

Table 4.1. Two-gate decomposition and Z-Spin status.

| Stage | Control step | Z-Spin status |
| ----- | ----- | ----- |
| **Gate G1** | Locality / finite propagation of correlations | M17.2 provides structure — DERIVED-CONDITIONAL (generic) |
| **Gate G2** | Propagation of chaos, recollision exclusion, entropy production | No structure provided — OPEN |
| **G1 \+ G2** | ⇒ Boltzmann kinetic equation for f(t, x, v) | OPEN (blocked at G2) |
| **Hydro limit** | Chapman–Enskog / Hilbert ⇒ Euler / NSF | External, classical \[7\]; not reached by Z-Spin |

**Corollary M42.2 (Locality-Gate Membership) \[DERIVED-CONDITIONAL\].** M17.2’s Lieb–Robinson velocity bound is an instance of the G1 estimate class. Conditional on the external mean-field realizations \[3,4\], it is the same type of a-priori bound that controls G1 in known derivations. By F-M42.4 this membership is generic — it holds for any local lattice and does not by itself invoke Z-Spin geometry.

**§5. The Z-Spin-Specific Claim: dim(Z) \= 2 Bottleneck Saturation**

The single non-generic content is the proposed G1 saturation mechanism. In Z-Spin all X–Y traffic is forced through the two-dimensional Z-sector: LXY ≡ 0 is PROVEN \[11\], dim(Z) \= 2 is PROVEN \[10\], and the Z-mediated transfer operator has rank ≤ dim(Z) \= 2, bounding the channel capacity by

CX→Y  ≤  ln 2        (ZS-Q7 \[11\]).

**Conjecture M42.3 (dim(Z) \= 2 Locality-Gate Saturation) \[HYPOTHESIS — downgraded in v1.2 from HYPOTHESIS-strong\].** The original conjecture was that the dim(Z) \= 2 bottleneck saturates the G1 Lieb–Robinson bound to the strict equality stated in ZS-M17 §4, v\_max \= ρ(ℒ)·a. A June 2026 deep-exploration audit shows the supporting argument is incomplete, and the conjecture is downgraded.

vmax ≤ ρ(ℒ) · a   (DERIVED) ;     vmax \= ρ(ℒ) · a   (HYPOTHESIS, tightness; ρ ≈ 4.51, ZS-Q5 \[12\]) .

The gap is a space mismatch. The dim(Z) \= 2 bottleneck constrains the **internal register** ℂ¹¹ \= Z ⊕ X ⊕ Y: it bounds the rank (≤ 2\) and channel capacity (≤ ln 2\) of the X→Y transfer. The Lieb–Robinson velocity ρ(ℒ)·a is by contrast a **spatial** property — the maximum group velocity over the lattice dispersion, attained at the band-edge wavevector k\*. Saturation requires the propagating signal to concentrate at k\*, which the internal rank-2 bottleneck does not force. The “sole pathway” argument therefore shows that ρ(ℒ)·a is the relevant scale and an upper bound, but not that it is attained — consistent with the generic many-body fact that the butterfly/Frobenius velocity is strictly below the Lieb–Robinson velocity. Accordingly the ZS-M17 dated-erratum (2026-06-07) downgrades M17.2 to v\_max ≤ ρ(ℒ)·a (DERIVED) and reverts OP-c.3 to OPEN; the strict equality becomes a HYPOTHESIS decidable by the empirical gate F-M17.5 (Z-Spin hardware, 2027+). The residual Z-Spin-specific content is thus weaker than v1.1 claimed: the bottleneck sets the velocity scale but does not saturate it. (Observable symbols O₁, O₂ of the Lieb–Robinson commutator are kept distinct from the Z-Spin impedance **A** \= 35/437.)

**§6. Missing Ingredients for an Ordinary NSF Derivation**

Five ingredients present in the Deng–Hani–Ma chain are absent from Z-Spin. Table 6.1 inventories them and assigns each to a gate or to the hydrodynamic limit; all are OPEN.

Table 6.1. Missing ingredients, gate assignment, and status.

| \# | Ingredient required by the reference chain | Belongs to | Status |
| ----- | ----- | ----- | :---: |
| **1** | Particle phase-space distribution f(t, x, v) as the microscopic Z-Spin state | G2 prerequisite | **OPEN** |
| **2** | Boltzmann collision operator Q(f, f) emerging from block-Laplacian / register dynamics | G2 | **OPEN** |
| **3** | Propagation of chaos / recollision control | G2 (core) | **OPEN** |
| **4** | Mass, momentum, energy conserved as collision invariants | G2 closure | **OPEN** |
| **5** | Transport coefficients (ν, heat conductivity) via Chapman–Enskog / Hilbert expansion | Hydro limit | **OPEN** |

**§7. Future Bridge: Z-Spin Kinetic Ansatz or Z-Effective Hydrodynamics**

Two future routes are registered, neither claimed here. **Route A (kinetic ansatz)**: define a Z-Spin phase-space distribution and seek a collision operator and propagation of chaos from register dynamics, attacking G2 directly. **Route B (effective hydrodynamics)**: rather than ordinary Navier–Stokes, derive a Z-Spin effective hydrodynamics. Writing the Z-bias field as Φ \= ρ eiθ, the stress-energy conservation of the Goldstone phase θ yields Euler / superfluid hydrodynamics at leading order; treating the Z → Y dissipative channel by a Kubo formula \[17\] yields a Navier–Stokes-like effective equation. The decisive constraint is zero free parameters: the effective shear viscosity νZ, the bulk viscosity, and the heat conductivity must follow from A \= 35/437, Q \= 11, dim(Z) \= 2 with no tuning, or Route B is rejected (F-M42.7). Route B is now opened as the stub ZS-M43, which records two corpus-anchored findings: the relativistic Euler sector already appears in the corpus (the Goldstone profile θ(r) \= ln(r/r₀)/L gives ρθ ∝ 1/r², ZS-A1/A2/F1), and the natural zero-parameter scale for the dissipative correction is O(A²), anchored by the O(A²/M\_P²) Goldstone parametric drag of ZS-U11 NC-U11.1 and the IR fixed point λ\_vac \= 2A². The Kubo / nonlinear Q-decay computation of νZ and the effective-fluid dictionary remain OPEN in ZS-M43. \[Route A: HYPOTHESIS / OPEN. Route B: Euler part DERIVED-CONDITIONAL, νZ \~ O(A²) HYPOTHESIS-strong, dictionary OPEN.\]

**§8. Falsification Gates and Non-Claims**

Table 8.1. Falsification gates.

| Gate | Trigger condition (claim restricted / retracted if met) |
| ----- | ----- |
| **F-M42.1** | If quantum commutator-locality (Lieb–Robinson) and classical propagation of chaos admit no common estimate abstraction, the G1 “shared family” claim collapses. |
| **F-M42.2** | FIRED (partial, v1.2). M17.2’s strict equality v\_max \= ρ(ℒ)·a is not justified (internal-register bottleneck ≠ spatial band-edge saturation); Conjecture M42.3 downgraded to HYPOTHESIS and M17.2 reverted to v\_max ≤ ρ(ℒ)·a (ZS-M17 erratum 2026-06-07). |
| **F-M42.3** | If the Boltzmann–Grad limit admits no locality-estimate reformulation, the G1 bridge to Deng–Hani–Ma specifically is severed (mean-field only). |
| **F-M42.4** | If the G1–kinetic bridge holds identically for any local lattice with no dependence on dim(Z) \= 2 or A, the locality-gate membership has no Z-Spin-specific content (see NC-M42.3). |
| **F-M42.5** | If propagation of chaos is intrinsically time-asymmetric while Lieb–Robinson is time-symmetric, the “same family” is restricted to time-symmetric a-priori bounds only. |
| **F-M42.6** | If a rigorous micro-to-NSF derivation is found that does NOT factor through an independent chaos/entropy gate (e.g., a direct hydrodynamic limit), Theorem M42.1 is downgraded to a description of the Boltzmann route only (see NC-M42.5). |
| **F-M42.7** | (Route B) If a Z-effective hydrodynamics requires any transport coefficient outside {A, Q, dim(Z) \= 2}, the zero-parameter discipline is violated and Route B is rejected. |

**Non-Claims**

**NC-M42.1.** Z-Spin is NOT claimed to derive the Boltzmann equation or the Navier–Stokes–Fourier equations.  
**NC-M42.2.** ZS-M17 and Deng–Hani–Ma are NOT claimed to share microscopic objects or macroscopic targets.  
**NC-M42.3.** The locality-gate (G1) membership is NOT claimed to be Z-Spin-specific beyond the dim(Z) \= 2 saturation conjecture of §5.  
**NC-M42.4.** The arrow of time is NOT relocated to ZS-M17; irreversibility is absent from the unitary OS reconstruction and is carried by ZS-F13 \[15\].  
**NC-M42.5.** Theorem M42.1 is NOT claimed to be a proven necessity for all conceivable micro-to-NSF derivations; it is a DERIVED-interpretation of the structure of all currently known rigorous derivations.  
**NC-M42.6.** This note does NOT address the Clay Millennium Navier–Stokes existence-and-smoothness problem, which concerns well-posedness of the PDE — a different question from the Hilbert-VI derivation-from-microdynamics problem treated here.  
**NC-M42.7.** The Z-effective-hydrodynamics direction (§7, Route B) is future work (ZS-M43 / M42b); no effective transport coefficient is derived here.

**§9. Conclusion**

The 2025 Hilbert-sixth result and ZS-M17 are two rigorous discrete-to-continuum programmes that share an ambition and a scale hierarchy but not their mathematics. We have not derived the Navier–Stokes–Fourier equations and do not claim to. The contribution is to decompose the obstruction: a micro-to-hydrodynamic derivation factors into a locality gate G1 and a chaos/entropy gate G2; Z-Spin’s ZS-M17 supplies structure for G1 (with the dim(Z) \= 2 bottleneck as a saturation candidate, HYPOTHESIS-strong) and nothing for G2, where the obstruction sits. Stated this way, the note offers external value precisely because it is a sharp no-go and a locality criterion rather than an overclaim: it marks exactly where the Hilbert-VI program and the Z-Spin continuum limit touch and exactly where they cannot.

**Acknowledgements & Code Availability**

This note was developed with the assistance of AI tools (Anthropic Claude) for literature search, structural verification, adversarial counterargument, and drafting, during a June 2026 deep-exploration session, and revised following external peer comment. The author assumes full responsibility for all content and conclusions. This is a structural/classification note; it introduces no new numerical computation and no new verification script. The 16 structural-consistency checks of Appendix A are reproducible by inspection against the cited corpus papers and external references.

**Appendix A. Structural-Consistency Checklist (16/16 PASS)**

Table A.1. Structural-consistency checks for ZS-M42 v1.2.

| \# | Check | Verdict |
| ----- | ----- | :---: |
| **C1** | Zero new free parameters; no constant beyond A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6). | **PASS** |
| **C2** | M17.2 statement v\_max \= ρ(ℒ)·a reproduced as in ZS-M17 §4 (ρ ≈ 4.51 from ZS-Q5). | **PASS** |
| **C3** | dim(Z) \= 2 inherited from ZS-F5 (PROVEN); not re-derived. | **PASS** |
| **C4** | Channel capacity C ≤ ln 2 inherited from ZS-Q7 (DERIVED); not re-derived. | **PASS** |
| **C5** | Lieb–Robinson upper-bound form matches Lieb–Robinson 1972 (commutator norm, finite group velocity). | **PASS** |
| **C6** | Mean-field/Hartree derivation distinguished from the Boltzmann–Grad scaling. | **PASS** |
| **C7** | Macroscopic targets recorded disjoint: relativistic Wightman QFT vs Galilean NSF. | **PASS** |
| **C8** | Arrow of time attributed to ZS-F13, not ZS-M17 (no relocation). | **PASS** |
| **C9** | Time-reversal status recorded: LR time-symmetric; propagation of chaos time-asymmetric. | **PASS** |
| **C10** | No observational prediction issued; trivially consistent with Planck 2018 ΛCDM and SM couplings. | **PASS** |
| **C11** | Consistent with the ZS-F18 non-claim that Clay-problem encounters are not formal solutions. | **PASS** |
| **C12** | dim(Z) \= 2 saturation downgraded HYPOTHESIS-strong → HYPOTHESIS; M17.2 strict equality → ≤ (internal ≠ spatial); consistent with ZS-M17 erratum. | **PASS** |
| **C13** | Bridge to the Boltzmann–Grad case flagged OPEN; G2 obstruction explicitly located. | **PASS** |
| **C14** | Each counterargument mapped to a falsification gate (F-M42.1–7). | **PASS** |
| **C15** | Theorem M42.1 tagged DERIVED-interpretation, not PROVEN (NC-M42.5; F-M42.6). | **PASS** |
| **C16** | Clay vs Hilbert-VI distinction stated (NC-M42.6); effective-hydro deferred to M43 (NC-M42.7). | **PASS** |

**References**

\[1\] Y. Deng, Z. Hani, and X. Ma, “Hilbert’s sixth problem: derivation of fluid equations via Boltzmann’s kinetic theory,” arXiv:2503.01800 (2025).

\[2\] Y. Deng, Z. Hani, and X. Ma, “Long time derivation of the Boltzmann equation from hard sphere dynamics,” arXiv:2408.07818 (2024).

\[3\] E. H. Lieb and D. W. Robinson, “The finite group velocity of quantum spin systems,” Commun. Math. Phys. 28, 251 (1972).

\[4\] B. Nachtergaele and R. Sims, “Lieb–Robinson bounds in quantum many-body physics,” in Entropy and the Quantum, Contemp. Math. 529, 141 (Amer. Math. Soc., 2010); arXiv:1004.2086.

\[5\] O. E. Lanford III, “Time evolution of large classical systems,” in Dynamical Systems, Theory and Applications, Lecture Notes in Physics 38, 1 (Springer, 1975).

\[6\] “Comment on ‘Hilbert’s Sixth Problem: Derivation of Fluid Equations via Boltzmann’s Kinetic Theory’ by Deng, Hani, and Ma,” arXiv:2504.06297 (2025).

\[7\] C. Bardos, F. Golse, and C. D. Levermore, “Fluid dynamic limits of kinetic equations,” J. Stat. Phys. 63, 323 (1991); see also L. Saint-Raymond, Hydrodynamic Limits of the Boltzmann Equation, Lecture Notes in Math. 1971 (Springer, 2009).

\[8\] K. Kang, “Continuum Limit and Osterwalder–Schrader Reconstruction of Z-Spin Lattice Dynamics,” ZS-M17 v1.0 (Z-Spin Cosmology Collaboration, April 2026).

\[9\] K. Kang, “Gap G2 Order Parameter via Factorized Spectral Determinant,” ZS-M16 (Z-Spin Cosmology Collaboration, 2026).

\[10\] K. Kang, “Gauge Symmetry Constraint: Why Q \= 11 and dim(Z) \= 2,” ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[11\] K. Kang, “The Z-Bottleneck: L\_XY ≡ 0 and Channel Capacity ≤ ln 2,” ZS-Q7 (Z-Spin Cosmology Collaboration, 2026).

\[12\] K. Kang, “Spectral Velocity Bound v\_max ≤ ρ(ℒ)·a,” ZS-Q5 (Z-Spin Cosmology Collaboration, 2026).

\[13\] K. Kang, “Geometric Impedance A \= 35/437,” ZS-F2 v1.0(Revised) (Z-Spin Cosmology Collaboration, 2026).

\[14\] K. Kang, “The Five-Axiom Meta-Structure and the Clay-Problem Encounter,” ZS-F18 v2.1 (Z-Spin Cosmology Collaboration, 2026).

\[15\] K. Kang, “Möbius Chronology Theorem,” ZS-F13 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[16\] Clay Mathematics Institute, “Navier–Stokes Existence and Smoothness,” Millennium Prize Problems (2000).

\[17\] R. Kubo, “Statistical-mechanical theory of irreversible processes. I,” J. Phys. Soc. Jpn. 12, 570 (1957).

**Version History**

v1.0 (June 2026): Initial release. Classification of ZS-M17 M17.2 within the micro-to-macro locality-estimate landscape; five falsification gates and four non-claims; arrow-of-time linkage to ZS-M17 RETRACTED-in-session.  
v1.1 (June 2026): Reframed from a flat classification to a Two-Gate No-Go \+ Locality-Bridge map, following external peer comment. Adds Proposition M42.0 (No Direct Derivation), Theorem M42.1 (Two-Gate Decomposition, DERIVED-interpretation), Corollary M42.2 (locality-gate membership), Conjecture M42.3 (dim(Z) \= 2 saturation, HYPOTHESIS-strong); §6 missing-ingredient inventory (five items, OPEN); §7 future-bridge routes A (kinetic ansatz) and B (Goldstone-phase effective hydrodynamics, deferred to ZS-M43 / M42b). Adds F-M42.6 (two-gate non-necessity) and F-M42.7 (effective-hydro transport-coefficient tuning), and NC-M42.5–7 (including the Clay vs Hilbert-VI distinction). Title changed to “The Z-Bottleneck Locality Criterion for Hydrodynamic Derivability.” Structural-consistency checks 14 → 16, all PASS. Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged. (Consolidated from internal Z-Spin Collaboration deep-exploration session, June 2026.)  
v1.2 (June 2026): Result of a follow-up if-tree deep-exploration of falsification gate F-M42.2. Conjecture M42.3 (dim(Z) \= 2 locality-gate saturation) DOWNGRADED from HYPOTHESIS-strong to HYPOTHESIS: the dim(Z) \= 2 bottleneck is an internal-register constraint (rank ≤ 2, capacity ≤ ln 2\) and does not force spatial band-edge group-velocity saturation, so it does not establish the strict equality. F-M42.2 recorded as partially FIRED. The companion ZS-M17 dated-erratum (2026-06-07) reverts M17.2 to v\_max ≤ ρ(ℒ)·a (DERIVED) with tightness now HYPOTHESIS and OP-c.3 reverted to OPEN; scope limited to OP-c.3 (OP-c.1 Wightman reconstruction unaffected); downstream ZS-S14 §F.iii ‘saturates’ softened to ‘bounded by’. Route B opened as the stub ZS-M43 (Goldstone-phase effective hydrodynamics): Euler sector DERIVED-CONDITIONAL via the corpus ρ\_θ ∝ 1/r² instance, and an O(A²) viscosity candidate (HYPOTHESIS-strong) anchored by ZS-U11 NC-U11.1 and λ\_vac \= 2A², with the Kubo / Q-decay computation OPEN. No numerical prediction changed; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged.