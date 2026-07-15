**ZS-A15**

**Pre-Registered Gaia DR4 Falsification Protocol for the ε-Halo Outer Boundary: Enclosed-Mass Saturation, Keplerian Slope, and the NFW/MOND Degeneracy**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Cosmology Collaboration

**Theme / Paper Code:** Astrophysics — ZS-A15 v1.5

**Date:** March 2026

**Dependencies:** ZS-F1, ZS-A1, ZS-A5, ZS-A11 v1.1.

**Frozen protocol:** a15\_dr4\_protocol.yaml | SHA-256 1d04ee2f73b6f7791586fa3964d201e2336e54f690a75fc25f3ee0f773b283e2

**GitHub:** https://github.com/KennyKang-git/zspin

**Verification Summary**

Verification: 36/36 PASS | Zero free parameters in the structural claim (a finite outer cutoff exists). The value r\_Z is DERIVED-CONDITIONAL on the observed inputs (M\_total, v\_flat) and is registered, not predicted ab initio. Sole geometric inputs: A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6). Pre-registered before Gaia DR4 (2 December 2026); the frozen analysis protocol is hash-locked (SHA-256 above). The verification suite includes a five-truth confusion-matrix (T20a–e) and a zeroth-order transition-width measurement (T23a–c).

**§0. Abstract**

The ε-Halo of Z-Spin Cosmology models galactic dark matter as the gradient energy of the exactly massless Goldstone mode θ of a spontaneously broken internal U(1)\_Z, giving ρ\_θ ∝ 1/r² — functionally identical to a singular isothermal sphere and, across seven macroscopic observables, to a ΛCDM sub-halo (ZS-A11 v1.1). The descriptions break only at microscopic ontology (the one-way detection asymmetry F-A5.7) and at the outer boundary, where the Three-Region structure of ZS-F1 §5.3 terminates the halo at a finite radius r\_Z (DERIVED).

This is not a claim that Z-Spin has measured the Galaxy; it is a pre-registered, hash-locked falsification protocol fixed before Gaia DR4. We freeze a single decisive Milky Way test: whether the enclosed mass saturates near M\_total ≈ 2×10¹¹ M☉ by ≈25 kpc (logarithmic slope γ → −1/2) versus continuing to grow toward M\_200 ≈ 8×10¹¹ M☉. Four honesties are built in. (i) A finite cutoff is DERIVED upstream and shared by every finite-mass halo (truncated or cored NFW included); it is not advanced as novel (§2A). (ii) The value r\_Z is conditional on observed inputs (DERIVED-CONDITIONAL); the derivation gap is split into the now-closed well-posedness of the boundary-value problem (A15-T1a, IMPORTED-PROVEN via Ginzburg–Landau / harmonic-map theory) and the transition width. We prove a No-Intrinsic-Width Lemma: the strictly massless equation □θ \= 0 fixes the logarithmic profile but determines no universal width coefficient, so the observed Δr/r\_Z ≲ 0.4 (an upper bound, A15-T1b-0) cannot come from the bulk equation; the v1.2 geometric candidates {A, 1/Q, Z/Q} are accordingly RETRACTED, and a smooth massless-edge ansatz is shown to be both non-harmonic and ≈5× too gradual. The open question is reframed as a Sharp-Edge Mechanism (A15-T1b-3): a scale census shows no locked length equals ≈0.4, so the edge must be short-scale (sharp). The corpus matching M\_ε(r\_Z) \= M\_total is a global point boundary condition, which on the scale-free interior yields a near-step edge (DERIVED-CONDITIONAL, no new parameter) — turning the v1.4 “data sharper than the smooth field” tension into a prediction, and registering a new falsifier (F-A15.7: a wide DR4-resolved intrinsic width would refute it). No numerical Δr/r\_Z is claimed. (iii) The protocol does not exclude all particle dark matter and, on the rotation curve alone, does not separate ε-Halo from the Moffat-type MOG family; this is structured as a four-model decision matrix (§4B) and a five-truth confusion-matrix verification (T20a–e), not hidden. (iv) An Imported No-Go Ledger (§2A) records, with external citations, exactly where the rotation curve alone cannot decide. The present record is contested (Jiao et al. 2023 low-mass versus Zhou et al. 2022 full-halo), which is why advance registration converts a possible post-DR4 agreement from numerology into evidence.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem; standard mathematics alone, machine-verifiable. |
| DERIVED | Z-Spin action \+ standard physics, zero free parameters. |
| DERIVED-CONDITIONAL | DERIVED conditional on a listed observational input or upstream theorem. |
| IMPORTED-PROVEN | Result proved externally and used here without re-proof; full citation given. |
| IMPORTED-NO-GO | External result that bounds what the present data can decide. |
| TESTABLE | Pre-registered prediction with an explicit falsification protocol. |
| HYPOTHESIS-weak | Motivated conjecture with a partial derivation chain; promotion path noted. |
| OBSERVATION | Empirical regularity; anti-numerology controlled; origin/discrimination pending. |
| LOCKED | Core constant fixed upstream; no downstream paper may modify it. |
| NON-CLAIM | Explicit declaration of what is NOT asserted; bounds the framework’s scope. |
| OPEN | Recognized gap honestly registered for future work. |
| OBSERVATION-upper-bound | Empirical quantity that bounds, but does not measure, the underlying value. |
| HYPOTHESIS-strong | Conjecture with a clear derivation target and a plausible mechanism identified. |
| RETRACTED-in-session | Previously registered claim withdrawn within this work after new evidence. |
| DERIVED-interpretation | Qualitative reading of a derived structure; not a quantitative prediction. |

**§1. Introduction**

In Z-Spin Cosmology the flat rotation of disk galaxies is produced not by massive particles but by the gradient energy of a Goldstone field. The Z-anchor theorem (ZS-F1 §5.2, PROVEN) forces |Φ| \= 0 at any point of non-zero winding from π₁(U(1)) \= ℤ; around the resulting vortex line the angular mode θ is the exactly massless Goldstone boson (ZS-F1 §4.2, DERIVED) with profile θ(r) \= ln(r/r₀)/L, giving the isothermal energy density of equation (3). ZS-A11 v1.1 showed this ε-Halo is degenerate with a ΛCDM sub-halo across profile, source, and seven observables, breaking only at microscopic ontology and at the outer boundary.

Gaia DR4 is scheduled for 2 December 2026 (first 5.5 years / 66 months of mission astrometry, epoch data, improved proper motions). Because a prediction fixed after the data carries no evidential weight, this paper freezes the discriminating prediction, its pipeline, and its decision rules in advance, binding them with a cryptographic hash (§4A). Section 2A imports the external theorems and no-go results that bound the test; §3 separates what is already derived from the one quantity DR4 genuinely puts at risk.

**§2. Locked Inputs and External Proven Lemmas**

All Z-Spin inputs are LOCKED upstream; no new parameter is introduced. External lemmas are standard galactic dynamics, quoted as PROVEN.

**Table 2.1. Locked inputs and their sources.**

| Symbol | Value | Source / Status |
| ----- | ----- | ----- |
| **A** | 35/437 \= 0.080092… | ZS-F2 geometric impedance — LOCKED |
| **Q** | 11 (prime) | ZS-F5 register dimension — PROVEN |
| **(Z, X, Y)** | (2, 3, 6\) | ZS-F5 sector decomposition — PROVEN |
| M\_P, ℓ\_P | 1.221×10¹⁹ GeV, 1.616×10⁻³⁵ m | CODATA 2022 — STANDARD |
| M\_total (MW) | 2.06 (+0.24,−0.13)×10¹¹ M☉ | Jiao et al. 2023 — OBSERVATION |
| v\_flat (MW) | 220 – 237 km/s | Jiao 2023; Cepheid 2025 — OBSERVATION |

**Lemma 1 (SIS profile and velocity, PROVEN).**

For a self-gravitating isothermal system \[5\], ρ\_SIS \= σ²/(2πG r²), M(\<r) \= 2σ² r/G, v\_c² \= G M(\<r)/r \= 2σ²; hence v\_flat \= √2·σ. The MW’s observed 220 km/s is the circular velocity, so the equivalent SIS dispersion is σ ≈ 156 km/s (this closes the σ↔v\_flat normalization of ZS-A11 §3.2; it affects L only, not r\_Z).

**Lemma 2 (Finite-region enclosed mass, PROVEN).**

In the flat region M(\<r) \= v\_flat² r/G grows linearly and terminates at r\_Z \= G M\_total / v\_flat² (2), elementary Newtonian dynamics and framework-independent.

**Lemma 3 (Cutoff necessity, PROVEN).**

A profile ρ ∝ r⁻α with α ≤ 3 has divergent total mass \[5\]; the α \= 2 law must truncate. A finite cutoff is a theorem of classical dynamics, shared by the isothermal halo, truncated NFW, and any finite-mass model alike.

**§2A. Imported Theorem and No-Go Ledger**

To prevent cherry-picking, we fix — with external citations — both the theorems we rely on and the boundaries beyond which the rotation curve alone cannot decide. The no-go rows are not weaknesses to be hidden; they are the scope of the test.

**Table 2A.1. Imported theorems (I) and no-go results (N).**

| ID | Imported result | A15 consequence | Status |
| ----- | ----- | ----- | ----- |
| I1 | Finite-mass isothermal no-go: ρ∝1/r² cannot persist to infinity \[5\] | the halo must have a finite cutoff r\_Z | IMPORTED-PROVEN |
| I2 | Exterior point-mass theorem: M saturates ⇒ v\_c∝r⁻¹ᵐ² \[5\] | saturation ⇒ Keplerian γ \= −1/2 | PROVEN |
| I3 | Annular winding BVP well-posed (Ginzburg–Landau / S¹ harmonic map, prescribed degree) \[13–15\] | the θ-transition BVP (A15-T1a) is a normal, solvable problem | IMPORTED-PROVEN |
| N1 | Ou et al. cored-Einasto fit to the MW decline \[7\] | a decline alone does NOT falsify particle DM | IMPORTED-NO-GO |
| N2 | MOG fit to the declining MW curve \[9\] | ε-Halo vs MOG unresolved by the rotation curve alone | IMPORTED-NO-GO |
| N3 | Disk–halo (maximum-disk) degeneracy \[16\] | an independent mass channel is required | IMPORTED-NO-GO |
| N4 | Klacka–Sturc axisymmetric-Jeans critique \[10\] | spherical/axisymmetric consistency clause is mandatory | IMPORTED-NO-GO |
| N5 | Transition radius is model-dependent: MOG R₀ \= 18.1 kpc vs Newtonian R₀ \= 33.8 kpc on the same four DR3 datasets \[9\] | Δr must be read from a model-independent slope break, not a fitted R₀ | IMPORTED-NO-GO |
| N6 | FIRE-2 synthetic-Gaia Jeans systematics 5–20%, large galaxy-to-galaxy variance \[17\] | the zeroth-order Δr is a loose band; precise quantization needs DR4 | IMPORTED-NO-GO |

**§3. What Is Already Derived versus What Is Registered**

The Z-Spin halo energy density is ρ\_θ(r) \= M\_P²/(2 L² r²) (3), the gradient energy of the Goldstone solution (ZS-F1 §4.3, DERIVED); equating with Lemma 1 gives L² \= πG M\_P²/σ², L of order the Hubble radius.

**Table 3.1. Status ledger: what this paper does and does not claim.**

| Statement | Status | Source |
| ----- | ----- | ----- |
| ρ\_θ ∝ 1/r² from the massless Goldstone mode | DERIVED | ZS-F1 §4.3 |
| Z-anchor |Φ| \= 0 from π₁(U(1)) \= ℤ | PROVEN | ZS-F1 §5.2 |
| A finite outer cutoff r\_Z exists | DERIVED | ZS-F1 §5.3 |
| Existence of a cutoff is novel to Z-Spin | NON-CLAIM | I1, Lemma 3 |
| Equivalence with sub-halo across 7 observables | DERIVED | ZS-A11 §3 |
| One-way detection asymmetry F-A5.7 | PROVEN | ZS-A5 |
| Discriminating DR4 protocol (saturation vs growth) | TESTABLE | §4, §4A |
| Numerical value r\_Z ≈ 18 kpc | DERIVED-COND. | Eq. (2)+obs. |
| θ-transition BVP is well-posed (A15-T1a) | DERIVED-COND. | §5, I3 |
| □θ=0 fixes no width coefficient (No-Intrinsic-Width) | PROVEN | §5, T24 |
| Transition width Δr/r\_Z ≲ 0.4 (A15-T1b-0) | OBS-upper-bnd | §5, T23a |
| Geometric Δr candidates {A,1/Q,Z/Q} | RETRACTED | §5, T23b |
| Intrinsic edge near-step (Path A, point matching) | DERIVED-COND. | §5, T25 |
| Numerical Δr/r\_Z value | OPEN / unclaimed | §5 |
| ε-Halo separated from MOG by RC alone | OPEN | §4B, N2 |

**§4. Pre-Registered Prediction and Falsification Gates**

The contested record. All recent analyses agree the outer curve declines but disagree on the implied mass. Jiao et al. (2023): sharp Keplerian onset from ≈19 kpc, M\_total \= 2.06×10¹¹ M☉. Zhou et al. (2022): milder decline, full halo M\_200 \= 8.05×10¹¹ M☉ to R\_200 ≈ 192 kpc. Ou et al. (2024): faster outer decline but a cored DM profile. Because r\_Z ∝ M\_total, the ε-Halo reading holds only at low mass; at M\_200 ≈ 8×10¹¹ M☉ equation (2) gives r\_Z ≈ 71 kpc. The decisive observable is the enclosed-mass behaviour at large radii.

Frozen statistic. γ ≡ d ln v\_c/d ln r (0 flat, −1/2 Keplerian). The gates below, and the full pipeline of §4A, are frozen and hash-locked before DR4.

**Table 4.1. Pre-registered Gaia DR4 falsification gates.**

| Gate | Pre-registered condition and falsifier | Status |
| ----- | ----- | ----- |
| G-DR4.1 | Structural. Enclosed mass saturates near 2×10¹¹ M☉ by ≈25 kpc (γ → −0.5±0.1, maintained). FALSIFY if γ \> −0.3 beyond 25 kpc or M(\<r) grows toward 8×10¹¹ M☉. | TESTABLE |
| G-DR4.2 | Numerical. Onset r\_Z in \[15,21\] kpc (propagated from M\_total=1.93–2.30×10¹¹, v\_flat=220–237). FALSIFY if outside \[13,25\] kpc at 2σ. | DERIVED-COND. |
| G-DR4.3 | Systematic. γ from spherical AND axisymmetric Jeans (N4). If the spherical treatment removes the decline, G-DR4.1/2 are N/A — not PASS. | TESTABLE |

**§4A. Frozen DR4 Analysis Protocol**

The pipeline is fixed in a15\_dr4\_protocol.yaml (SHA-256 1d04ee2f73b6f7791586fa3964d201e2336e54f690a75fc25f3ee0f773b283e2); any post-release change alters the hash and voids the registration. Tracers: RGB/LRGB, classical Cepheids, RR Lyrae, BHB, K giants — none may be dropped to recover a slope. Radius bins (kpc): \[15,20\],\[20,25\],\[25,30\],\[30,40\],\[40,60\]; γ is evaluated on the three outer bins (≥25 kpc). Estimators: at least two of axisymmetric Jeans, spherical Jeans, action-based DF, with the spherical-Jeans result mandatory (it directly tests N4). Decision statistics: γ\_outer, dM/dr, M\_enclosed; gates G-DR4.1–G-DR4.3 are applied verbatim. The reference implementation verify\_zsa15.py executes this rule: mock gate recovery (T17–T19) returns PASS / FAIL / N/A correctly, a hash check (T21) and a paper/code/protocol consistency check (T22) guard against silent edits.

**§4B. Four-Model Decision Matrix and Confusion-Matrix Validation**

The ε-Halo is not tested against particle-NFW alone. Within modified gravity the matrix distinguishes deep-MOND (asymptotically flat, hence disfavoured by a genuine decline) from the Moffat-type MOG family (running effective G, which fits a decline and stays degenerate with ε-Halo on the rotation curve).

**Table 4B.1. Frozen DR4 outcome → model decision matrix.**

| DR4 outcome | ε-Halo | Particle NFW | Truncated / cored NFW | Modified gravity |
| ----- | ----- | ----- | ----- | ----- |
| γ≈−1/2 maintained; M saturates ≈2×10¹¹ | strongly supported | weakened | possible (tuned r\_t) | MOG possible; MOND disfavoured |
| γ≈0 or M grows → 8×10¹¹ | FALSIFIED | supported | supported | model-dependent |
| decline vanishes under spherical Jeans | N/A | N/A | N/A | N/A |
| decline \+ no lensing/dyn-mass mismatch | supported | weakened | possible | possible |
| decline \+ MOG fits equally | not sole winner | weakened | possible | MOG supported |

Confusion-matrix validation. The verification suite implements this matrix as a five-truth Bayesian-information-criterion comparison (T20a–e): a saturated truth selects the sharp-decline class (ε-Halo wins over NFW and flat); an M\_200 \= 8×10¹¹ NFW truth selects NFW (ε-Halo loses); a cored mild-decline truth selects the cored model (ε-Halo loses); a MOG-decline truth leaves ε-Halo and MOG within ΔBIC \< 2 (UNRESOLVED, |ΔBIC| \= 1.34); and a spherical-Jeans artifact returns N/A. The classifier therefore changes verdict with the truth model — it is not tuned to let ε-Halo win.

**§5. Open Gate A15-T1: Finite θ-BVP Closure**

The weakest link in the value prediction is that equation (2) is a Newtonian identity in which M\_total is fitted from the curve, so r\_Z ≈ onset is near-tautological. We split the route to removing this conditionality into two sub-gates.

**A15-T1a — BVP mathematical admissibility (IMPORTED-PROVEN / DERIVED-CONDITIONAL).**

The transition profile is the solution of a winding-phase boundary-value problem on an annular region, θ ∼ ln r (r ≪ r\_Z), ∂\_rθ → 0 (r → r\_Z), θ → const (r \> r\_Z) (5), with FRW matching as the outer condition. This falls within the standard class of prescribed-degree Ginzburg–Landau / S¹-valued harmonic-map problems, for which existence of a rotationally invariant minimizer and convergence to the harmonic-map solution are established theorems \[13–15\]. The BVP is therefore a normal, well-posed problem; A15-T1a is closed (IMPORTED-PROVEN), so the residual uncertainty is purely the Z-Spin-specific numerical scale, not the mathematical legitimacy of the construction.

**No-Intrinsic-Width Lemma (PROVEN).**

On a source-free annular domain the strictly massless equation □θ \= 0 has the unique rotationally symmetric solution θ(r) \= a·ln r \+ b (the radial Laplace ODE (1/r)(rθ′)′ \= 0 integrates to θ′ \= a/r). This solution is scale-free: it fixes the logarithmic interior profile and the 1/r² halo, and it admits a finite outer boundary-matching problem (A15-T1a), but it contains no length scale that could set a universal transition-width coefficient. Therefore any value such as Δr/r\_Z ≈ 0.4 must originate in the matching operator, finite vortex-line geometry, boundary regularization, or the observational inference pipeline — not in the bulk massless equation itself. This is why A15-T1b is OPEN, and it is a theorem, not a gap in effort (gate T24).

**A15-T1b-0 — observational width proxy (OBSERVATION-upper-bound).**

Existing Gaia DR3 analyses provide a coarse proxy, not a sharp intrinsic width. Jiao et al. (2023) place the roll-off from flat to Keplerian between ≈19.5 and ≈26.5 kpc, with the enclosed mass essentially constant (1.9–2.0×10¹¹ M☉) beyond ≈19 kpc \[6\]; independent stellar-halo number-density and σ\_r profiles show a break radius r\_b ≈ 16–27 kpc \[17, 18\]. Together these give Δr ≲ 7.5 kpc, i.e. Δr/r\_Z ≲ 0.4. Because of the transition-radius model dependence (MOG R₀ \= 18.1 kpc vs Newtonian R₀ \= 33.8 kpc on the same data, N5) and FIRE-2 Jeans systematics of 5–20% (N6), this is an upper bound on the rotation-curve roll-off width, not a measurement of the field-theoretic width (gate T23a).

**A15-T1b-1 — small-ratio candidates (RETRACTED-in-session).**

The v1.2 candidates Δr/r\_Z ∈ {A \= 0.080, 1/Q \= 0.091, Z/Q \= 0.182} predicted Δr ≈ 1.5–3.3 kpc. The proxy Δr/r\_Z ≲ 0.4 exceeds the largest by ≈2.3× and the smallest by ≈5.1× (gate T23b); we withdraw the simple-ratio hypothesis rather than carry one the data already disfavour.

**A15-T1b-2 — smooth-edge no-go (DERIVED-CONDITIONAL / toy ansatz).**

A phenomenological smooth edge ρ\_θ ∝ r⁻² e⁻ʳᐟʳᶜ normalizes cleanly: M\_total \= 2σ²r\_c/G forces r\_c \= G M\_total/(2σ²) \= r\_Z exactly (gate T24a), a result worth registering. But this ansatz is not a solution of □θ \= 0: with ∂\_rθ ∝ e⁻ʳᐟ²ʳᶜ/r, the cylindrical Laplacian gives □θ \= −e⁻ʳᐟ²ʳᶜ/(2r·r\_c) ≠ 0 (gate T24b), implying a hidden source or damping. Moreover its slope transition is broad: γ runs from −0.1 to −0.4 over Δr/r\_Z ≈ 2.2 (gate T24c), about 5× wider than the observed proxy of ≈0.4 (gate T24d). Hence Δr/r\_Z ≈ 0.4 is NOT recovered by any smooth massless-edge ansatz; the earlier v1.3 statement that a roll-off of order r\_Z “matches” the data is corrected here — the smooth edge is in fact too gradual, and the data are sharper.

**A15-T1b-3 — Sharp-Edge Mechanism (Path A upgraded, DERIVED-CONDITIONAL).**

The open problem is not “which small ratio gives 0.4” but: why is the physical Region-II → Region-III matching sharper than a smooth massless edge? A scale census settles the direction. The only locked lengths in the problem are the Region-I radial-mode scale ξ ≈ 31 ℓ\_P (ξ/r\_Z ≈ 9×10⁻⁵⁵), the boundary location r\_Z itself (r\_Z/r\_Z \= 1), and the infrared log scale L ∼ Hubble radius (L/r\_Z ≈ 4×10⁵). None equals ≈0.4: a genuine field scale is either ≪ r\_Z (sharp) or ≫ r\_Z (gradual), so the observed Δr/r\_Z ≲ 0.4 selects the SHORT-scale (sharp) branch (gate T25a).

Path A (FRW point matching) — upgraded. In the corpus the Region-II/III matching is fixed by continuity of enclosed mass, M\_ε(r\_Z) \= M\_total (ZS-A1 §2.4.2): it is a global point boundary condition, not a local damping length r\_c. Imposed on the scale-free 1/r² interior, a point condition produces a near-step edge, Δr/r\_Z ≪ 1 (gate T25b), governed by the short scale rather than the IR scale. This introduces no new parameter and resolves the v1.4 “tension” constructively: the fact that the data are ≈5× sharper than a smooth massless edge is not an anomaly but the PREDICTION of short-scale point matching (gate T25c). The qualitative claim — the intrinsic edge is near-step, not a smooth O(r\_Z) roll-off — is therefore DERIVED-CONDITIONAL (conditional on the matching being short-scale/topological, as the mass-exhaustion boundary condition implies). The corresponding paths B (smooth finite-line crossover with a simple geometric n) is DISFAVOURED — it is the wrong, too-gradual picture — and path C (observational upper bound) MERGES with A: the observed Δr/r\_Z ≲ 0.4 is the resolution-limited upper bound on an intrinsically sharp edge.

What stays open and what is now falsifiable. No numerical value of Δr/r\_Z is claimed; by the No-Intrinsic-Width Lemma the bulk equation fixes none, and the short-scale census only bounds it small. The new content is a falsifier (F-A15.7): if Gaia DR4 robustly RESOLVES a wide intrinsic transition, Δr/r\_Z ∼ O(1), the short-scale point-matching prediction of Path A is falsified — turning the previously open sharpness question into a registered, pre-DR4 observational gate.

**§6. Zero-Free-Parameter and Anti-Numerology Audit**

Structural claim. Equation (3), the Goldstone origin of ρ\_θ ∝ 1/r², and Region III use only A, Q, (Z, X, Y); nothing is tuned (gates T3–T6, T10, T13). Numerical value. Equation (2) is an identity, not a fit, so no candidate-scan Monte Carlo applies; the near-tautology of §5 is why the registered discriminant (§4) is the out-of-sample saturation-versus-growth behaviour and why A15-T1b is OPEN: the No-Intrinsic-Width Lemma (§5) shows □θ=0 fixes no width coefficient, so no candidate-scan applies. r\_Z is labelled DERIVED-CONDITIONAL throughout. Cosmological consistency. ΔN\_eff(θ) \= 0 exactly in FRW (ZS-F1 §7.1), so the Planck 2018 background is unperturbed (T14); the only internal correction is the σ↔v\_flat (√2) fix in ZS-A11 §3.2, affecting L only (T6).

**§7. Scope and Non-Claims**

NC1. A finite outer cutoff is DERIVED upstream (ZS-F1 §5.3) and shared by all finite-mass halo models; not novel (I1).

NC2. r\_Z is conditional on observed M\_total and v\_flat; no zero-parameter value prediction is asserted. The mathematical BVP is well-posed (A15-T1a); by the No-Intrinsic-Width Lemma the massless equation fixes no width coefficient, the observed Δr/r\_Z ≲ 0.4 is an upper bound (A15-T1b-0), and Path A (point matching) makes the intrinsic edge near-step (A15-T1b-3, DERIVED-CONDITIONAL).

NC3. A15 does not claim that all particle dark-matter models are excluded by a declining MW rotation curve. The frozen gate targets the standard extended-growth (M\_200-scale, NFW-like) interpretation. Truncated or cored particle halos remain comparator models, penalized only by their additional truncation/profile freedom (N1, N3). On the rotation curve alone the protocol does not separate ε-Halo from declining MOG (N2).

NC4. By F-A5.7, a DR4 outcome that falsifies the ε-Halo outer boundary does not by itself confirm particle dark matter; it removes ε-Halo at the outer boundary and leaves the remaining classes to be separated by the independent channels of §8.

**§8. Conclusion and Future Work**

We have frozen and hash-locked, ahead of Gaia DR4 (2 December 2026), a single decisive Milky Way prediction: the enclosed mass saturates near 2×10¹¹ M☉ by ≈25 kpc, so γ → −1/2 and is maintained outward, versus a particle halo growing toward M\_200 ≈ 8×10¹¹ M☉ to ≈190 kpc. γ \> −0.3 beyond 25 kpc, or a still-growing enclosed mass, falsifies the ε-Halo outer boundary. The test establishes finite versus extended-growth particle-NFW; it cannot alone separate ε-Halo from tuned cored halos or declining MOG (§2A, §4B).

Two extensions are flagged. Closing A15-T1b (§5) would lift the value prediction above its conditional status. A companion paper, ZS-A16 (degeneracy-breaking), is reserved to add the independent channels that the no-go ledger shows are required: external-galaxy outer declines, stellar streams and satellite kinematics, the vertical force K\_z, weak-lensing mass normalization, the CGM baryon-mass constraint, and an explicit profile-complexity penalty against cored-NFW and MOG. A15 is the DR4 pre-registration; A16 is where the cored-NFW and MOG degeneracies left OPEN here are broken.

**Acknowledgements, Code and Data Availability**

This paper consolidates internal Z-Spin Collaboration research notes. The frozen protocol (a15\_dr4\_protocol.yaml, SHA-256 1d04ee2f73b6f7791586fa3964d201e2336e54f690a75fc25f3ee0f773b283e2) and the 36-test verification suite (verify\_zsa15.py) are available at https://github.com/KennyKang-git/zspin. All observational inputs are from the cited public literature and the forthcoming Gaia DR4 archive.

**Appendix A. Worked SIS Lemmas**

Isothermal hydrostatic equilibrium with P \= ρσ² and dM/dr \= 4πr²ρ gives ρ \= σ²/(2πG r²), M(\<r) \= 2σ² r/G, v\_c² \= 2σ² (flat). Beyond saturation the point-mass limit gives v\_c ∝ r⁻¹ᵐ² (γ \= −1/2). Equating M\_P²/(2L²r²) to σ²/(2πG r²) gives L² \= πG M\_P²/σ²; with σ ≈ 156 km/s, L ≈ 3.3×10²⁶ m.

**Appendix B. Observational Input Compilation**

**Table B.1. Milky Way measurements relevant to the DR4 gates.**

| Study | Key quantity | Bearing on the gates |
| ----- | ----- | ----- |
| Jiao et al. 2023 | M\_total=2.06×10¹¹; onset ≈19 kpc; flat rejected 3σ | Supports low-mass reading; r\_Z≈18 kpc |
| Ou et al. 2024 | faster decline to ≈30 kpc; cored Einasto | Decline confirmed, DM retained (N1) |
| Zhou et al. 2022 | M\_200=8.05×10¹¹; R\_200≈192 kpc | Full-halo reading; would falsify G-DR4.1 |
| Cepheid Gaia DR3 2025 | V\_c(R☉)=236.8±0.8 km/s | Shifts r\_Z band toward ≈16 kpc |
| Klacka & Sturc 2025 | decline may be Jeans artifact | Motivates G-DR4.3 (N4) |
| LZ 2025 (417 d) | no WIMP 3–9 GeV; ν-floor reached | F-A5.7 currently PASS (asymmetric) |

**References**

\[1\] K. Kang, “ZS-F1: Goldstone θ-halo, Z-anchor topology, and the Three-Region vortex structure,” Z-Spin Cosmology Collaboration (2026).

\[2\] K. Kang, “ZS-A1: The ε-Halo and galactic rotation without particle dark matter,” Z-Spin Cosmology Collaboration (2026).

\[3\] K. Kang, “ZS-A5: The falsification asymmetry F-A5.7 of dark-matter direct detection,” Z-Spin Cosmology Collaboration (2026).

\[4\] K. Kang, “ZS-A11 v1.1: Vortex Cosmology II — the ε-Halo ↔ sub-halo Equivalence Theorem,” Z-Spin Cosmology Collaboration (2026).

\[5\] J. Binney and S. Tremaine, Galactic Dynamics (Princeton University Press, 1987), §2.1.

\[6\] Y. Jiao, F. Hammer, H. Wang, et al., “Detection of the Keplerian decline in the Milky Way rotation curve,” Astron. Astrophys. 678, A208 (2023).

\[7\] X. Ou, A.-C. Eilers, L. Necib, and A. Frebel, “The dark matter profile of the Milky Way inferred from its circular velocity curve,” Mon. Not. R. Astron. Soc. 528, 693 (2024).

\[8\] Y. Zhou et al., “The circular velocity curve of the Milky Way from 5 to 25 kpc using luminous red giant branch stars,” arXiv:2212.10393 (2022).

\[9\] J. W. Moffat, H. Sharron, and V. T. Toth, “Implications of the Milky Way declining rotation curve,” arXiv:2409.17371 (2024).

\[10\] J. Klačka and M. Šturc, “On the interpretation of the Milky Way rotation-curve decline,” preprint (2025).

\[11\] J. Aalbers et al. (LUX-ZEPLIN Collaboration), Phys. Rev. Lett. (2025); first results Phys. Rev. Lett. 131, 041002 (2023), arXiv:2207.03764.

\[12\] Gaia Collaboration / ESA, “Gaia Data Release 4,” expected 2 December 2026, https://www.cosmos.esa.int/web/gaia/dr4.

\[13\] L. Berlyand, D. Golovaty, O. Iaroshenko, and V. Rybalko, “Ginzburg–Landau minimizers with prescribed degrees on annular domains,” arXiv:1701.01534 (2008/2018).

\[14\] P. Bauman and D. Phillips, “Minimax solutions of the Ginzburg–Landau equations on an annulus with prescribed degree,” (1997).

\[15\] H. Brezis, J.-M. Coron, and E. H. Lieb, “Harmonic maps with defects,” Commun. Math. Phys. 107, 649 (1986).

\[16\] T. S. van Albada, J. N. Bahcall, K. Begeman, and R. Sancisi, “Distribution of dark matter in the spiral galaxy NGC 3198,” Astrophys. J. 295, 305 (1985).

\[17\] Y. Huang, X.-W. Liu, H.-B. Yuan, et al., “The Milky Way’s rotation curve out to 100 kpc and its constraint on the Galactic mass distribution,” Mon. Not. R. Astron. Soc. 463, 2623 (2016), arXiv:1604.01216 (stellar-halo break radius ≈16–27 kpc).

\[18\] I. B. Santistevan et al., “Decoding the Galactic twirl: Milky Way-mass rotation curves in the FIRE simulations,” arXiv:2503.05877 (2025) (Jeans systematics 5–20%).

**Version History**

v1.5 (March 2026): Upgraded Path A of the Sharp-Edge Mechanism (A15-T1b-3) to DERIVED-CONDITIONAL with no new parameter. A scale census shows none of the locked lengths (ξ/r\_Z ≈ 9×10⁻⁵⁵, r\_Z/r\_Z \= 1, L/r\_Z ≈ 4×10⁵) equals the observed ≈0.4, so the edge must be short-scale; the corpus matching M\_ε(r\_Z) \= M\_total is a global point boundary condition that, on the scale-free interior, yields a near-step edge (Δr/r\_Z ≪ 1). This recasts the v1.4 “data sharper than the smooth field” tension as a prediction, disfavours path B, merges path C, and registers a new falsifier F-A15.7 (a wide DR4-resolved intrinsic width refutes it). The numerical Δr/r\_Z stays unclaimed (No-Intrinsic-Width Lemma). Verification suite 33 → 36 tests (T25a–c); SHA-256 re-locked. v1.4 (March 2026): Proved the No-Intrinsic-Width Lemma — □θ \= 0 on a source-free annulus fixes θ \= a ln r \+ b and determines no universal Δr/r\_Z coefficient (PROVEN, gate T24). Corrected the v1.3 “roll-off matches the data” reading: the smooth edge ρ∝r⁻²e⁻ʳᐟʳᶜ gives r\_c \= r\_Z exactly but is non-harmonic and ≈5× too gradual. Restructured §5 into A15-T1b-0/1/2/3. Verification suite 29 → 33 tests (T24a–d). v1.3 (March 2026): Split A15-T1b into A15-T1b-0 (Gaia DR3 width proxy) and A15-T1b-1 (geometric quantization); RETRACTED {A, 1/Q, Z/Q}. Added N5, N6; suite 26 → 29 (T23a–c). v1.2 (March 2026): Added §2A Imported Theorem and No-Go Ledger (I1–I3, N1–N4); split A15-T1 into A15-T1a (IMPORTED-PROVEN) and A15-T1b; §4B five-truth confusion-matrix; suite 22 → 26\. v1.1 (March 2026): renumbered ZS-A13 → ZS-A15; added §4A frozen hash-locked pipeline, §4B decision matrix, §5 Open Gate A15-T1; softened NFW wording (NC3); suite 16 → 22\. v1.0 content preserved; changes are additive.