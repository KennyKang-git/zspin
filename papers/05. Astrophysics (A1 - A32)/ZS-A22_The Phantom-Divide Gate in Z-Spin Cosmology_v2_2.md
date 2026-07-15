**ZS-A22**

**The Phantom-Divide Gate in Z-Spin Cosmology**

***A Conditional Frozen-Attractor No-Go, an Operational Total-Superacceleration Diagnostic, and a Map of Admissible Crossing Routes***

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Theme / Code:** Astrophysics — **ZS-A22 v2.2**  
**Date:** June 2026  
**Repository:** github.com/KennyKang-git/zspin

**Verification (three layers): algebraic identities, dependency / status, and logical-claim checks. The audit is implemented and attached (zs\_a22\_v2\_2\_audit.py, 26 checks); independent rerun is recommended.  |  Zero Free Parameters**

Sole geometric inputs: **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6), LOCKED. No new fitted parameter; standard external cosmological inputs (h via the acoustic scale θs, ns \= 0.9674) disclosed. Anti-numerology Monte Carlo: NOT APPLICABLE — the paper asserts no numerical coincidence; its content is a conditional No-Go plus a working classification and a candidate-survey barrier map. Pre-registered falsification gates: A22-G1 … A22-G16 (§13).

**Status note.** This paper is the product of six honest-correction rounds. Across v1.2→v2.2 two over-stated closures were demoted to scoped propositions (A22.6, A22.7), the C5 gate was demoted from a “trichotomy theorem” to a candidate-survey barrier map (Proposition A22.8), the extension classification was relaxed to a working taxonomy, the late-time vacuum source was made an explicit Premise P0, the central No-Go was split into an exact result (A22.1a) and a conditional estimate (A22.1b), the §5 criterion was rescoped to a total-superacceleration diagnostic, and three errata in the conformal energy-exchange (the factor ½, the braiding, and the sign of Q) were fixed. The full change log is in the Version History; the present text supersedes all earlier drafts.

# **§0. Abstract**

The DESI DR2 baryon-acoustic-oscillation data (2025) prefer a dynamical dark-energy sector whose Chevallier–Polarski–Linder reconstruction (w0 \> −1, wa \< 0\) suggests a recent crossing of the phantom divide w \= −1, at 2.8–4.2σ depending on the dataset and supernova compilation \[1, 34\]; whether the preference survives global Bayesian model comparison is itself debated \[35\]. A tempting reading of Z-Spin Cosmology identifies the expansion–contraction duality (1+**A**) ↔ (1−2**A**) of ZS-A8/A9 as a parameter-free Quintom trajectory. We show this reading is premature and, in its baseline form, in conflict with the corpus. This paper is a viability gate and a frontier map, not a closure; its central tool — a split-independent diagnostic of total super-acceleration (§5), applicable to any survey — tests whether an inferred crossing entails a total null-energy-condition violation, while remaining agnostic about a dark-energy component crossing, which the background alone cannot decide.

The firmest results are exact or structural. **Theorem A22.1a (Exact Strict-Attractor No-Crossing):** given an explicitly specified P0 vacuum source (Tμν(P0) \= −ρP0 gμν), the combined late-time vacuum sector has wDE \= −1 exactly at the fixed point (ε̇ \= 0, F constant, Q \= 0). **Proposition A22.1b (Heavy-Mode Decoupling Estimate):** for mρ ≫ H the deviation decouples; the quasi-static contribution scales as 1 \+ wqs ∼ (αMP)²(H/mρ)⁴, and the transient depends on a pre-specified initial amplitude, so (H0/mρ)² ≈ 5.6×10⁻¹²¹ is reported as a benchmark decoupling ratio, not a derived bound on 1 \+ w (DERIVED-CONDITIONAL). Both are conditional on Premise P0 (the late-time vacuum source, §2.3, §12). **Theorem A22.2 (Accounting-Invariance) and the Total-Superacceleration Diagnostic (TSD):** only the total source is split-invariant, so wtot \< −1 (split-independent total super-acceleration) holds if and only if the expansion super-accelerates, Ḣ \> 0\. The DESI mean CPL fits give min wtot(z) ≈ −0.5 \> −1 over 0 ≤ z ≤ 3, i.e. no super-acceleration, so the inferred w0wa crossing is not identifiable from the background as split-independent total super-acceleration and is degenerate with interacting and modified-gravity interpretations \[34, 35\] — a structural companion to the statistical non-robustness, not a claim that the crossing is unphysical. The corpus carries a documented retracted accounting instance (ZS-U2). **Theorem A22.3 (Existing-Carrier No-Go in the Strict Adiabatic Baseline):** each existing carrier is No-Go under stated conditions — the heavy radial ε, the canonical Goldstone θ (by the null energy condition and the single-field Quintom no-go), the conserved ZHCS dust, and frozen-F modified gravity (αM \= αB \= αT \= 0 at the attractor). **Lemma A22.5a & Proposition A22.5b (Topological Conservation and the Rank-One Channel):** the ZHCS current Jᵘ \= ∇ν ΣZμν is identically conserved (structural), and the corpus block-Laplacian coupling reduces, under the rank-one residue-mode approximation, to the single β0 channel (κ² \= **A**/**Q** \= 35/4807).

Two v1.2 closures are demoted to their honest scope. **Proposition A22.6 (Frozen Conformal-Channel Suppression):** the unique linearized cross-sector channel is curvature-sourced by F(ε)R, so the energy exchange it mediates is Q \= −½ αM H ρc ∝ −Ḟ (Einstein-frame cold mass ∝ F−1/2), which vanishes at the strict attractor; this closes only the existing-field, linearized conformal subroute, and the general interacting route C4 (disformal, curvature-current, multi-derivative, or a second light field) remains OPEN. **Proposition A22.7 (Conditional Seam Constraint-Exclusion):** the 37 non-uniform modes of the 38-node seam Laplacian are constraint-excluded under the reduced cellular-BF model (dΓ p \= 0), reproducing ZS-A19 v3.1; whether they are genuinely gauge (BRST-exact) requires the edge-sector ghost complex (OPEN), so the baseline no-crossing result is conditional, not complete. The NEC-floor bound wtot ≥ −1 holds for non-interacting positive-density components, but an observationally reconstructed weffobs can dip below −1 with interaction, so it is gated by C4, not excluded.

**Proposition A22.8 (a three-barrier map for the surveyed completions)** organises the frontier. Of seven zero-parameter, ghost-free dynamical completions surveyed (App. E), each is found to encounter at least one of three presently unresolved barriers: (B1) reflection-positivity / healthiness (ZS-M17.3 — generic higher-derivative completions with rational propagators violate OS-3 \[31\], though reflection positivity is not categorically forbidden for higher-derivative theories \[32\], so B1 is a healthiness *test*, not a universal No-Go); (B2) departure from the continuum sectoral allocation (ZS-M17.1 — only the X-sector becomes a propagating continuum field, the Z-sector remaining a rank-≤2, ln 2-capacity mediator, so a propagating seam requires *leaving the assumptions* of the allocation rather than falsifying it); or (B3) the absence of a *derived* late-time IR scale (the corpus derives ratios such as eA and 2eA but no action-level mechanism fixes H0/MP \~ 10⁻⁶¹ — an OPEN debt, not an impossibility, since the DERIVED ZS-F10/U8 hierarchy τn \= tP·exp(nπ/**A**) already spans the relevant range). The map is a candidate survey, not a universal classification, and “exactly one” is *not* claimed. C5 thus remains a genuine OPEN. A confirmed crossing would falsify the conditional frozen-attractor baseline and *activate* the C1–C5 extension audit; which upstream structure must change is itself OPEN. Zero free parameters throughout; (**A**, **Q**, dim Z) \= (35/437, 11, 2\) LOCKED.

# **Epistemic Status Legend**

The following tags are used throughout; each numbered claim in §4–§11 carries one. Tags are written UPPERCASE BOLD.

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics alone, machine-verifiable. |
| **DERIVED** | Z-Spin action plus standard physics; zero free parameters. |
| **DERIVED-CONDITIONAL** | DERIVED conditional on a listed axiom set or upstream theorem. |
| **DERIVED-interpretation** | Synthetic reading composing PROVEN results without new axioms. |
| **IMPORTED-PROVEN** | Result proved externally and used here without re-proof; full citation given. |
| **NO-GO** | A proven impossibility statement under explicitly stated conditions. |
| **HYPOTHESIS-strong / weak** | Motivated conjecture; documented promotion path / partial chain. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted; bounds the scope. |
| **OPEN** | Recognized gap honestly registered for future work; not closable with current corpus/external tools. |
| **LOCKED** | Core constant fixed upstream; no downstream paper may modify. |

# **§1. Introduction**

The Dark Energy Spectroscopic Instrument's second data release (DESI DR2, 2025\) sharpened a tension already visible in DR1: when the dark-energy equation of state is allowed to evolve through the Chevallier–Polarski–Linder (CPL) form w(a) \= w0 \+ wa(1−a), the data favour a region with w0 \> −1 today and wa \< 0 in the past — a Quintom-B trajectory that crosses the phantom divide w \= −1 at intermediate redshift. The reported significance ranges from 2.8σ to 4.2σ depending on the supernova compilation (DESY5, Union3, or Pantheon+), and the crossing redshift is not strongly determined.

There is a robust theoretical obstruction to a literal phantom crossing. The Quintom no-go theorem (Vikman 2005; Hu 2005; Caldwell–Doran 2005; reviewed by Cai et al. 2010\) states that within general relativity a single minimally-coupled scalar field — or a single perfect fluid — cannot smoothly and stably cross w \= −1: at the would-be crossing the kinetic factor FX vanishes, forcing the adiabatic sound speed cs2 to vanish and then turn negative in the phantom regime, a gradient instability. A stable crossing requires at least one of four ingredients: (i) an extra propagating field, (ii) higher-derivative degrees of freedom, (iii) modified gravity, or (iv) an interacting dark sector.

Z-Spin Cosmology derives its late-time phenomenology from the single geometric impedance **A** \= 35/437 and the register **Q** \= 11 (ZS-F1, ZS-F2, ZS-F5). The expansion–contraction symmetry of ZS-A8/A9 reads the dual factors (1+**A**) and (1−2**A**) as the two analytic branches of the i-tetration fixed point, with (1+**A**)(1−2**A**) ≈ 0.9071. It is tempting to read this duality as a built-in Quintom trajectory. We argue that this is exactly the conclusion-first inference the corpus is designed to resist, and that in its baseline form it conflicts with an already-DERIVED result.

The conflict is concrete. ZS-U2 §3 evaluates the late-time Friedmann system on the canonical attractor (ε \= ±1, ε̇ \= 0\) and finds w(z) \= −1 exactly, with w0 \= −1, wa \= 0; it registers a falsification gate. An A22 that simultaneously keeps the existing late-time action, the heavy radial attractor, and extracts an O(**A**) crossing from that baseline cannot coexist with ZS-U2 §3. The duality (1+**A**) ↔ (1−2**A**) is, moreover, a scale-flow correspondence, not an equation of state: it does not by itself supply ρDE(a), pDE(a), or H(a), and therefore does not supply w(a).

This paper therefore takes the opposite posture from a discovery announcement. We first ask whether the baseline can cross at all, prove that it cannot through the existing fields (conditional on Premise P0), isolate and exclude the most likely false positive (a frame artifact), exhaust the existing carriers, organise the admissible non-baseline extensions into a working taxonomy, and survey seven zero-parameter ghost-free completions, finding that each encounters at least one of three present barriers (Proposition A22.8). The result is an honest terminus in the style of the ZS-A18 → A21 cluster: a chain of conditional No-Gos, a frontier map, and a candidate survey — not a universal theorem. Relative to v1.2 we correct three errata and demote two over-statements (§9, §10) and register one inherited debt (§12); relative to v1.3 we further demote the C5 gate from a “trichotomy theorem” to a Proposition / barrier map and correct its scale barrier against the ZS-F10/U8 hierarchy. The net effect is a more conservative but more defensible paper.

# **§2. The Baseline System**

## **2.1 The locked action and its two scalar modes**

The Z-Spin action (ZS-F1, Eq. 3\) is a scalar–tensor theory with a single complex Z-bias field Φ \= ε eiθ ∈ ℂ non-minimally coupled to gravity:

S\[g,Φ\] \= ∫ d⁴x √(−g) \[ ½MP2 (1 \+ A|Φ|²) R − ½MP2 |∂Φ|² − V(Φ) \] \+ Sm

V(Φ) \= λ / 4MP4 (|Φ|² − 1)²,    F(ε) ≡ 1 \+ Aε2,    M\*2 \= MP2 (1 \+ Aε2)

Both the non-minimal coupling F(ε) and the double-well potential V are LOCKED in ZS-F1; **A** \= 35/437 is the geometric impedance (ZS-F2). The polar decomposition exhibits two intrinsic scalar degrees of freedom: the radial mode ε \= |Φ| and the Goldstone phase θ of the spontaneously broken U(1)Z. There is no third scalar in the gravitational sector — the fact that makes the carrier exhaustion of §6 finite. \[DERIVED from ZS-F1.\]

## **2.2 Horndeski class and gravitational-wave speed**

Action (1) belongs to the Horndeski class with G4 \= ½ MP2(1 \+ **A**|Φ|²), G2 \= −½ MP2|∂Φ|² − V, and G3 \= G5 \= 0 (ZS-A6 §2.3, via ZS-S3). The equations of motion are second order (no Ostrogradsky ghost), and the tensor speed is exactly cT \= c, consistent with GW170817. We note carefully for §6(d) that G3 \= G5 \= 0 forces the tensor-speed excess αT \= 0, but does *not* by itself force the braiding αB \= 0: a field-dependent G4(Φ) generates kinetic mixing even when G3 \= 0 (Appendix A). \[DERIVED.\]

## **2.3 The heavy radial mode, the late-time attractor, and the de Sitter premise**

The potential has its global minima at ε \= ±1, where V \= V′ \= 0 and V″ \= 2λ MP4, and a local maximum (the topological core) at ε \= 0\. The one-loop RG trajectory βλ \= (3/16π²)(λ − 6**A**²)(λ − 2**A**²) has the IR-stable fixed point λvac \= 2**A**² \= 0.01283 (ZS-U5 §8, DERIVED-CONDITIONAL), giving the radial mass

mρ \= √(2 λvac) MP \= 2A · MP \= 0.1602 MP

For the No-Go of §4 only the robust statement mρ ≫ H0 is needed. With H0/MP ≈ 1.2×10⁻⁶¹, the heavy radial mode is frozen at ε \= 1 throughout the late universe; the sub-Compton Yukawa range renders the scalar invisible to fifth-force tests.

**Premise P0 — the late-time de Sitter vacuum source (inherited, conditional).** At the attractor V(1) \= 0 and F \= 1 \+ **A** is constant. ZS-F1 §6.4 states that V(1) \= 0 fixes the observed cosmological constant to arise from the (1 \+ **A**) gravity modification, with ΩΛ/Ωm \= 2eA \= 2.1668 (ZS-F4/F12), in agreement with Planck 2018 at −0.16σ. We flag honestly that this premise carries an upstream debt (§12): a constant conformal factor F \= 1 \+ **A** rescales MP2 → MP2(1 \+ **A**) but does not by itself generate a positive cosmological constant; Wald's cosmic no-hair theorem (1983) governs the asymptotics *given* a positive Λ, it does not source one. The *late-time crossing* results depend on this premise — A22.1, the radial/vacuum part of A22.3, and the strict-attractor limit of A22.6 — whereas the *structural* results do not: current conservation (A22.5a), the rank-one reduction (A22.5b), the seam constraint-exclusion (A22.7), and the Goldstone NEC bound hold independently of P0. A per-result dependency ledger is given in §12. \[DERIVED-CONDITIONAL on the ZS-F1 §6.4 / ZS-U2 late-time vacuum source; the action-level mechanism is OPEN, §12.\]

## **2.4 The ZHCS dust**

Cold dark matter is not a particle in the current corpus. ZS-A18 proved that the exactly massless Goldstone θ has w ∈ {1, −1/3}, never the w ≈ 0 the third acoustic peak demands, retracting an earlier closure. ZS-A19/A20 changed the carrier: CDM is implemented as a conserved geometric Brown–Kuchař boundary-tension dust through a first-order parent action SZHCS \= −μZ ∫ √(−gμν Jᵘ Jᵛ) \+ ∫ Jᵘ ∂μ T, with Jᵘ \= ∂ν ΣZμν, which on variation yields Brown dust (Tμν \= ρ uμ uν, p \= 0, cs2 \= 0, ρ ∝ a⁻³). A shared clock yields exactly one physical scalar in the cold–baryon sector, with vanishing relative entropy Scb \= 3(ζc − ζb) and a reduced kinetic matrix of rank one (ghost-free, cs2 \= 0). The cold fraction Ωcdm \= 32/121 and Ωb \= 6/121 are equivariant projection ranks.

**Scope of Scb \= 0 (carried forward exactly from ZS-A19 v3.1 / ZS-A20).** This identification is DERIVED in ZS-A20 conditional only on the global charge quantization C1-ID-global, and Scb \= 0 is itself DERIVED-CONDITIONAL on single-source / adiabatic selection (no independent spectator at the branching hypersurface). Critically, Scb is the *cold–baryon* relative entropy; it is *not* the Goldstone–cold relative entropy Sθc \= 3(ζθ − ζc), which the corpus does not compute. This scope distinction is used in §10. The corpus mediation is the rank-one β0 channel CZX \= κ|z0⟩⟨rX|, CZY \= κ|rY⟩⟨z0| with κ² \= **A**/**Q** \= 35/4807 ≠ 0 (PROVEN), because the direct X–Y coupling vanishes, LXY ≡ 0\.

# **§3. Three Equations of State and the Dark Degeneracy**

Because the theory is scalar–tensor, “the dark-energy equation of state” is ambiguous, and the ambiguity is the source of most false-positive crossings. We distinguish three quantities.

**wfield** — the ratio p/ρ of the genuine scalar stress tensor, computed from the field Lagrangian in the Einstein frame.  
**wgeometric** — the ratio obtained after a chosen subset of the F(ε)R-derived terms is moved from the geometric (left) side of the field equations to an “effective dark-energy” (right) side.  
**weffobs** — the value recovered when an observer fits the measured expansion history H(z) with a model assuming general relativity plus non-interacting dark components.

These three need not coincide. The relation among them is governed by the dark degeneracy (Wasserman 2002; Kunz 2009): gravity couples only to the total energy–momentum tensor, so only the total dark density ρtot(z) — equivalently H(z) — is observable, while its split into “dark matter” and “dark energy”, and hence the reconstructed w(z), is a convention. DESI's reported w(z) is of the third kind, weffobs, obtained under the non-interacting assumption. This degeneracy is the rigorous reason a frame or bookkeeping choice can manufacture an apparent crossing, and it underlies Theorem A22.2. It is also the reason — made precise in §10 and Appendix B — that an interaction can push weffobs below −1 with no fundamental phantom, so the NEC floor bounds wfield and wtot of non-interacting components but not weffobs.

# **§4. Theorem A22.1a (Exact Strict-Attractor No-Crossing) and Proposition A22.1b (Heavy-Mode Decoupling Estimate)**

**Theorem A22.1a (exact, combined vacuum sector).** The locked potential satisfies V(1) \= 0, so the frozen scalar alone carries no vacuum energy; the late-time Λ is supplied by Premise P0, made explicit here as a separate source with stress tensor Tμν(P0) \= −ρP0 gμν (ρP0 \> 0). At the exact strict attractor — ε \= 1, ε̇ \= 0 (φ \= φ\*, φ̇ \= 0\) and F \= constant (Ḟ \= 0\) — the *combined* late-time vacuum sector (P0 plus the frozen scalar) has, exactly,

ρDE \= ρP0 \+ ½φ̇² \+ Ulock(φ\*),    pDE \= −ρP0 \+ ½φ̇² − Ulock(φ\*),    wDE \= (−ρP0) / (ρP0) \= −1.

**Proof.** At φ̇ \= 0 and Ulock(φ\*) \= 0 the scalar contributes neither density nor pressure, so ρDE \= ρP0, pDE \= −ρP0, and wDE \= −1. (Were P0 instead realised as an additive constant ρP0 inside U, the same result follows from Utot \= V/F² \+ ρP0; the scalar-only ratio 0/0 is then simply not the object of interest.) With Ḟ \= 0 the running Planck mass is frozen (αM \= 0), so the conformal exchange of §9 vanishes, Q \= −½ αM H ρc \= 0, and no reassignment shifts the split. ∎ \[**DERIVED-CONDITIONAL** on an explicitly specified P0 vacuum source; the result wDE \= −1 is then *exact* (no perturbative corrections). This is the robust core of the No-Go: once a positive vacuum source is given, the strict attractor does not cross, full stop.\]

**Proposition A22.1b (heavy-mode decoupling estimate).** Off the exact fixed point the Einstein-frame description must include the matter coupling already used in §9: with gᴱ \= F gᴶ, matter sees F⁻¹(φ) gᴱ, so the canonical action and scalar equation are

Sᴱ \= ∫√−gᴱ \[ (MP2) / 2 Rᴱ − ½(∂φ)² − U(φ) \] \+ Sm\[ F⁻¹(φ) gᴱμν, ψm \],

φ̈ \+ 3Hφ̇ \+ U′(φ) \= α(φ) ρm,    3MP2 H² \= ½φ̇² \+ U(φ) \+ ρm,    α(φ) \= −½ d ln F/dφ.

(For pressureless dust the matter trace is Tm \= −ρm; the source αρm is the same conformal coupling that gives mc ∝ F−1/2 and Q \= −½ αM H ρc in §9. Earlier drafts of this section dropped this source, an internal inconsistency now removed.) For mρ ≫ H the heavy mode decouples: the source pins a *quasi-static* displacement at the matter-dressed minimum, δφqs ≃ αρm/mρ2 (sourced by the diluting matter, not by H alone), with φ̇ ∼ −3Hαρm/mρ2; the homogeneous transient δφtr ∝ a−3/2 cos(mρ t) carries a matter-like energy diluting as a−3. Both contributions to 1 \+ wφ \= φ̇²/ρφ vanish as the attractor is approached.

**Scope of the estimate.** The *decoupling* — |1 \+ weff| → 0 as ε̇, Ḟ → 0 for mρ ≫ H — is robust. The two contributions, however, are *not* bounded by a single power of H/mρ. Carrying the quasi-static solution through 1 \+ wφ \= φ̇²/ρDE with ρm \= 3MP2H²Ωm and ρDE \= 3MP2H²ΩDE gives a *fourth*\-power suppression,

1 \+ wqs ≃ 27 (α MP)² (Ωm2) / (ΩDE) (H / (mρ))⁴,

not O(H²/mρ2). The homogeneous transient δφtr ∝ a−3/2 cos(mρ t) dilutes as a−3, but its present amplitude is set by an *initial condition*, not by mρ ≫ H; it must be pre-specified (e.g. ρtr(zi) fixed at some early epoch) before |1 \+ wtr| can be bounded. Accordingly we do not present a single derived bound on 1 \+ w. The decoupling *ratio*

((H02) / (mρ2)) ≈ 5.6×10⁻¹²¹    (mρ \= 2**A** MP)

is reported as a *benchmark heavy-mode decoupling ratio*, not as a bound on 1 \+ w (the quasi-static deviation is the far smaller (H0/mρ)⁴). \[**DERIVED-CONDITIONAL**: the quasi-static (H/mρ)⁴ scaling follows from the field equation given the coupling α(φ); the transient and the overall normalisation require a pre-registered initial amplitude; the coefficient 2**A** in mρ is itself DERIVED-CONDITIONAL. Only mρ ≫ H is needed for the decoupling.\] Wald’s cosmic no-hair theorem (1983) supplies the de Sitter approach given ρP0 \> 0; a scalar with mρ ≫ H cannot sustain a slow roll.

**Corollary A22.1.1.** Any observable crossing requires leaving the strict-attractor branch of A22.1a — relaxing mρ ≫ H0 or ε̇ → 0, or introducing a degree of freedom not in §2.1. This is the formal entry point to the classification of §7.

# **§5. Theorem A22.2 — The Accounting-Invariance Theorem**

**Statement.** Write the modified Einstein equation as Gμν \= M\*−2 \[ Tμν(m) \+ Tμν(ε) \+ ∇μ∇ν M\*2 − gμν □ M\*2 \]. Any reassignment of the F(ε)R-derived terms between the geometric side and a defined effective-dark-energy stress tensor changes wgeometric but leaves the observables { H(z), DM(z), DH(z), fσ8(z) } invariant. A crossing that appears only in wgeometric is therefore not a physical crossing. \[**DERIVED-interpretation**, grounded in the dark degeneracy of §3.\]

**Worked corpus instance.** ZS-U2 §3.1 records exactly this artifact. An initial evaluation produced w0 ≈ −0.997, wa ≈ \+0.12 — a small near-phantom deviation that, taken at face value, would have looked like weak support for a crossing. A subsequent audit found that the 3**A** MP2 H² term had been placed on the dark-energy side when it belongs on the gravity side; reassigned correctly, the result collapses to w(z) \= −1 exactly. The corpus thus already carries a documented, retracted example of precisely the false positive this theorem excludes.

**Admissibility (qualitative).** A claimed phantom crossing in Z-Spin is admissible only if it (i) is invariant under reassignment of gravitational terms between the two sides of the field equations, and (ii) appears in the frame-invariant observables { H(z), DM(z), DH(z), fσ8(z) }, not merely in a chosen dark-energy bookkeeping. This dispatches the single most likely false positive — a conformal/frame crossing — before any extension is considered. The operational sharpening of (i)–(ii) is the following diagnostic.

**Total-Superacceleration Diagnostic (TSD).** Only the total stress tensor sources gravity, so in the observational (matter) frame the total combination is convention-free:

ρtot \+ ptot \= −2 MP2 Ḣ,    wtot \= −1 − (2/3) Ḣ / H².

Hence the *total* equation of state satisfies wtot \< −1 if and only if the expansion super-accelerates, Ḣ \> 0\. This is a *split-independent* reading because ρtot and ptot are unambiguous; only their decomposition into components is a convention. Precisely, the relation ρtot \+ ptot \= −2MP2Ḣ is a GR-form (constant-M\*) Friedmann identity, so the TSD is a *kinematic total-effective-equation-of-state diagnostic in the fixed matter frame under the constant-M\* reconstruction* — not a theorem about a fundamental matter-plus-field NEC violation: in a scalar-tensor branch with Ḟ ≠ 0 the geometric terms contribute, and Ḣ \> 0 then signals super-acceleration of the effective fluid rather than ghost matter. At the strict attractor F \= constant, so it applies cleanly to the A22 baseline. \[**DERIVED**; the Ḣ–wtot relation is exact in flat FRW under the constant-M\* reconstruction.\]

**What the TSD does and does not decide.** Ḣ \> 0 ⇔ total super-acceleration is necessary and sufficient for wtot \< −1 (ρtot \+ ptot \< 0\) of the effective fluid in the fixed matter frame. It is *not* a criterion for whether a dark-energy *component* crosses −1. With matter present, wtot \= Ωde wde, so a genuine wde \< −1 — realisable by a multi-field Quintom action \[12, 14\] — can coexist with Ḣ \< 0 (e.g. Ωde \= 0.7, wde \= −1.1 gives wtot \= −0.77 \> −1); conversely a dark-sector interaction can produce an observer-reconstructed wdeeff \< −1 with no fundamental phantom. Therefore, when Ḣ ≤ 0 the background *alone* neither confirms nor refutes a component crossing; it establishes only that there is no split-independent total super-acceleration, and the inferred wde crossing is *degenerate* with interacting and modified-gravity reinterpretations. Degeneracy is not proof of artifact.

**Frame caveat.** Raw Ḣ is not a general conformal invariant: under gᴱ \= F gᴶ one has Hᴱ \= F−1/2(Hᴶ \+ Ḟ/2F), so the value and sign of Ḣ shift when Ḟ ≠ 0\. At the strict attractor Ḟ \= 0 the two frames differ by a constant rescaling and the sign of Ḣ is preserved; away from it the TSD must be applied in a fixed physical (matter-defining) frame. The fully frame-independent objects are the observables { redshift, DM, DH, fσ8 }; the TSD is their split-independent reading in that frame, not a statement about all frames.

**Application to the DESI signal.** For the DESI DR2 mean CPL fits, wtot(z) \= Ωde(z) wde(z) has minimum over 0 ≤ z ≤ 3 of about −0.58 (Pantheon+), −0.49 (Union3) and −0.52 (DESY5) — all above −1. The DESI mean fits therefore do *not* imply total super-acceleration (Ḣ \< 0 throughout). Their inferred dark-energy crossing is consequently not identifiable from the background alone as split-independent total super-acceleration, and remains degenerate with interacting and modified-gravity interpretations. This is the structural complement to the statistical finding that the crossing is not robust under global Bayesian model comparison \[35\] and is parametrisation-dependent \[34\]; it is *not* a claim that the component crossing is unphysical.

**Operational test (any survey, Z-Spin or not).** (1) From the reconstructed H(z), form wtot(z) \= −1 − (2/3)Ḣ/H² and check whether it dips below −1 (⇔ Ḣ \> 0). (2) If it does, a split-independent total super-acceleration is present. (3) If it does not, the inferred wde crossing is degenerate with interacting / modified-gravity models; deciding it requires additional input (a measured dark-sector coupling, the perturbation sector, or a direct wtot determination), which the background cannot supply. \[**DERIVED** for the Ḣ–wtot relation in a fixed matter frame; this is a total-fluid test, not a component-crossing criterion.\]

# **§6. Theorem A22.3 — Existing-Carrier No-Go in the Strict Adiabatic Baseline**

**Statement.** In the strict baseline of §2, each existing carrier is No-Go for an observable phantom crossing, under the conditions stated below.

## **(a) The bare radial mode ε**

By Theorem A22.1a the radial mode sits at weff \= −1 exactly at the fixed point (given P0); by A22.1b its departures decouple conditionally for mρ ≫ H, the magnitude depending on the matter source and the initial oscillation amplitude rather than on a universal number. It is the only canonical scalar with a potential, and on the strict adiabatic branch it does not roll. \[**NO-GO** on the strict adiabatic baseline, conditional on mρ ≫ H0 and P0.\]

## **(b) The canonical massless Goldstone θ**

The operative obstruction is the null energy condition, not role-occupation. ZS-A19/A20 freed θ from the CDM role by moving the carrier to the ZHCS boundary dust, leaving θ exactly massless. A canonical, positive-energy, minimally-coupled scalar satisfies ρθ \+ pθ \= θ̇² ≥ 0 (the NEC), so wθ ≥ −1 pointwise; combined with the w \= −1 vacuum floor, wtot ≥ −1. The single-field Vikman/Quintom no-go makes this sharp at the perturbative level. \[**NO-GO** for w \< −1 with a single canonical θ; IMPORTED-PROVEN from Vikman 2005, Cai et al. 2010.\]

## **(c) The conserved ZHCS Brown dust**

The ZHCS dust is exact pressureless dust: w \= 0, cs2 \= 0, ρ ∝ a⁻³, with a reduced kinetic matrix of rank one and Scb \= 0 (ZS-A20). It is not a propagating dark-energy scalar, and as an independent component it cannot be the second Quintom field. We are careful about scope: this is a statement about the cold–baryon dust sector — there is no independent isocurvature scalar between baryon and ZHCS dust. It is NOT the claim that the entire Z-Spin action has exactly one scalar degree of freedom (ε and θ are separate, and boundary collective modes are not excluded here). \[**NO-GO** for the ZHCS dust as an independent Quintom field; scope as stated. **NON-CLAIM**: a global single-degree-of-freedom statement.\]

## **(d) Frozen-F modified gravity (corrected EFT mapping)**

With ε frozen at 1, the conformal factor F \= 1 \+ **A**ε² → 1 \+ **A** is constant, so the running-Planck-mass function αM \= d ln F/d ln a \= 0\. We correct the v1.2 treatment of the braiding. With G5 \= 0 and G4 independent of X, the tensor excess αT \= 0 (cT \= c). But the braiding is *not* zero merely because G3 \= 0: for a field-dependent non-minimal coupling G4(Φ) the standard EFT-of-DE relation (Bellini–Sawicki 2014\) is αB \= −αM. The correct statement is therefore that αB is *tied to* αM, and that both vanish at the strict attractor where Ḟ \= 0:

αM \= Ḟ / HF,    αB \= −αM,    αT \= 0;    at ε̇ → 0:  αM \= αB \= αT \= 0\.

The remaining αK (kinetic) does not produce a crossing on its own. \[**NO-GO** for the baseline Horndeski subclass with frozen ε. **Scope:** this is not the general statement that modified-gravity crossing requires αM ≠ 0; away from the attractor αB \= −αM ≠ 0 reintroduces braiding. Appendix A gives the explicit evaluation.\]

**Conclusion.** In the strict baseline every existing carrier is No-Go. Combined with §4 and §5, a crossing in Z-Spin can come neither from the existing fields nor from a bookkeeping choice; it requires a genuine extension, classified next.

# **§7. Proposition A22.4 — Classification of Admissible Extensions**

**Statement.** By Corollary A22.1.1, an observable crossing requires a degree of freedom or a dynamical regime outside the strict baseline of §2. We organise the presently identified corpus-compatible routes into ***five working classes*** and give each its honest status. This is a working taxonomy, *not* a closed EFT classification theorem: a single completion — e.g. a vector–tensor, nonlocal, dissipative / open-system, multi-fluid, or composite route — can cross more than one class. *None* of the non-trivial classes is closed by a No-Go, and the v1.2 assertion that C5 is the unique survivor is withdrawn (see below). \[DERIVED-interpretation; a working taxonomy of presently identified routes, not an exhaustiveness theorem.\]

Table 7.1 — Five working extension classes and their status.

| Class | Completion mechanism | Status | Controlling barrier / note |
| :---: | ----- | :---: | ----- |
| **C1** | Dynamical completion of the topological seam (cellular BF → a propagating boundary sector promoting the 37 relative modes) | **OPEN** | Full BFV/BRST cohomology uncomputed (§10, App. D); promotion collides with the M17.1 allocation (B2 of §11). |
| **C2** | Multi-component / non-adiabatic Goldstone (a second clock or an entropy perturbation in the θ sector) | **OPEN** | Goldstone–cold relative entropy Sθc uncomputed (App. D); NEC closes only the single-field *adiabatic* branch. |
| **C3** | An emergent light pole with a protective symmetry (a naturally light new field) | OPEN (weakly motivated) | No protective symmetry identified in the corpus; low prior, but *not* a No-Go. |
| **C4** | Dark-sector interaction / energy exchange (disformal, curvature-current, multi-derivative, or a second light field) | **OPEN** | Operator survey only to mass-dim ≤ 6, two derivatives (§9, App. C); general interaction not closed. An explicit realization (Antusch–King–Wang \[15\]) gives apparent weff \< −1 with no phantom scalar. |
| **C5** | Zero-parameter, ghost-free dynamical seam completion producing an observable w \< −1 crossing | **OPEN (genuine frontier)** | Three-barrier map B1/B2/B3 (Proposition A22.8, §11): each surveyed crossing encounters at least one present barrier; uniqueness and exhaustiveness are OPEN. |

**Withdrawal of the v1.2 uniqueness claim.** Version 1.2 concluded “the unique escape is C5.” That sentence is retracted. Because §9 closes only the linearized conformal subroute of C4 (not general interaction), §10 only constraint-excludes the seam modes under the reduced cellular-BF model (not the full BFV/BRST complex), and C2’s non-adiabatic branch and C3 are not No-Go, the correct statement is: ***C5 is the most explicit outside-baseline class currently identified, but C1 full boundary dynamics, C2 multi-component non-adiabatic route, C3 emergent pole, and general C4 interaction all remain OPEN; uniqueness is OPEN.***

# **§8. Lemma A22.5a & Proposition A22.5b — Topological Current Conservation and the Rank-One Conformal Channel**

**Lemma A22.5a (topological current conservation).** The ZHCS current is the divergence of the antisymmetric Z-spin flux ΣZμν \= −ΣZνμ. In curved spacetime the covariant statement is Jμ \= ∇ν ΣZμν \= (1/√−g) ∂ν(√−g ΣZμν), with ΣZμν an ordinary antisymmetric tensor (we use this convention throughout, not a densitized one), so by antisymmetry ∇μ Jμ \= ∇μ∇ν ΣZμν ≡ 0 identically (off-shell); the flat-space ∂μ Jμ \= 0 is its M⁴ limit. \[**DERIVED**, structural — it follows from antisymmetry alone, with no dynamical input.\]

**Proposition A22.5b (rank-one linearized conformal channel).** The corpus’s *linearized block-Laplacian* conformal coupling built from Jμ (respecting U(1)Z and diffeomorphism invariance) reduces, *under the rank-one residue-mode approximation* of ZS-A19/A21, to a single conformal channel

CZX ≈ κ |z0⟩⟨rX|,    κ² \= A / Q \= 35 / 4807\.

\[**DERIVED-CONDITIONAL**, on the rank-1 residue-mode approximation of ZS-A19/A21; it is a statement about that specific block-Laplacian coupling, not about every conceivable linearized coupling.\]

**Scope (split and tightened in v1.4).** Lemma A22.5a is an exact structural identity; Proposition A22.5b is an *approximation*. The rank-one structure CZX ≈ κ|z0⟩⟨rX| of the block Laplacian does *not* bound general nonlinear, higher-order, or boundary operators, which are treated in §9 and App. C and remain partly OPEN. The v1.2 reading that every admissible interaction is forced through the unique rank-one β0 channel was an over-extension and is corrected here. The v1.3 §8 bundled the conservation and the rank-one reduction into one “Theorem A22.5”; v1.4 separates them, because the conservation is exact while the rank-one reduction is only approximate.

# **§9. Proposition A22.6 — Frozen Conformal-Channel Suppression**

**Statement (demoted from the v1.2 Theorem A22.6).** The unique linearized cross-sector channel of §8 is curvature-sourced through F(ε)R. In the Einstein frame (gᴱ \= F gᴶ) a Jordan-constant cold mass scales as mc ∝ F−1/2, so the energy it exchanges between the cold sector and the ε-sector is

Q \= (d ln mc) / dε · ε̇ · ρc \= −½ (Ḟ / F) ρc \= −½ αM H ρc,

which is ∝ −Ḟ and therefore vanishes identically at the strict attractor (ε̇ → 0 ⇒ Ḟ \= 0 ⇒ Q \= 0). \[**DERIVED** for the linearized conformal channel.\] The factor ½ — dropped in v1.2 — follows from αM \= d ln F / d ln a \= Ḟ/(HF). The *sign* is corrected in v1.5: with gᴱ \= F gᴶ the cold mass obeys mc ∝ F−1/2, so d ln mc/dε · ε̇ \= −½ Ḟ/F \= −½ αM H, giving Q \= −½ αM H ρc (v1.4 carried the opposite sign). The qualitative conclusion Q → 0 at the frozen attractor is unaffected.

**Direction of flow (corrected sign; see App. B).** With the convention ρ̇de \+ 3H(ρde \+ pde) \= −Q and ρ̇c \+ 3Hρc \= \+Q, a positive Q transfers energy *from dark energy to dust*, and the effective dark-energy equation of state is weff \= wde \+ Q/(3Hρde). An apparent phantom weff \< wde therefore requires Q \< 0, i.e. dust → dark energy; with Q \= −½ αM H ρc this is the epoch αM \> 0 (F increasing). The convention is unchanged from v1.4; only the microphysical sign of Q is corrected.

**Scope and re-opening (the central v1.3 correction).** This is *not* the general interacting No-Go claimed in v1.2. It closes only the existing-field, linearized conformal subroute. The general route **C4** — disformal couplings, curvature-current operators, multi-derivative operators, or a second light field — is re-opened **OPEN**. An “operator exhaustion” claim is meaningful only once the basis is fixed; we restrict to local operators up to mass dimension 6 and two derivatives, imposing exact U(1)Z, Z2, and diffeomorphism invariance together with current conservation, and removing redundancies by integration by parts and field redefinition. Even within this basis the following structures are *not* covered by the rank-one channel of §8 and are listed for completeness (App. C):

Rμν JμJν,   JμJν ∇με ∇νε,   J²(∇θ)²,   f(ε, J²),   (∇μJν)(∇μJν),   and disformal / nonlocal boundary operators.

Accordingly A22.6 closes the ***baseline conformal C4 subroute*** only, and the verification banner records this as a corrected (not retracted) result.

# **§10. Proposition A22.7 — Conditional Seam Constraint-Exclusion**

**Statement (demoted from the v1.2 Theorem A22.7).** On the 38-node seam graph Γ38 (32 truncated-icosahedron cold faces and 6 cube baryon faces) the relative graph Laplacian LΓ has rank 37\. Under the reduced cellular-BF model with the flatness constraint dΓ p \= 0, the 37 non-uniform relative modes satisfy dΓ p ≠ 0 and are therefore *constraint-excluded* from the allowed configuration space, leaving the reduced cohomology dim H⁰ \= 1 (reproducing ZS-A19 v3.1). \[**DERIVED-CONDITIONAL** on the reduced cellular-BF model.\]

**What is withdrawn.** Whether these 37 modes are genuinely gauge — i.e. lie in im QBRST and are BRST-exact — is *not* established; that requires the full edge-sector ghost complex / BFV presymplectic treatment, which is OPEN, and the ZS-F0 boundary term must still be checked for mixing. We therefore explicitly withdraw the four v1.2 claims: “the 37 modes are BRST-exact,” “the physical BRST cohomology is exactly one-dimensional,” “C1 is closed,” and “Lclock-restrict is effectively solved.” The correct upstream status is constraint-exclusion under dΓ p \= 0, not gauge-exactness.

**Lclock-restrict** restored to OPEN. The first computation that must actually be carried out is

full boundary BFV presymplectic form  →  ghost complex  →  H•(QBFV)  →  rank K∂,phys.

Version 1.2 pre-empted this calculation and asserted its outcome; v1.3 restores it as the leading open task.

**NEC-floor, with its mandatory condition.** For non-interacting positive-density components the null energy condition gives wi ≥ −1 and ρi \> 0 ⇒ wtot ≥ −1. But an observationally reconstructed weffobs can dip below −1 in the presence of interaction (Q ≠ 0\) *without* any fundamental phantom — as in the canonical-quintessence-plus-field-dependent-dark-matter-mass construction (Antusch, King, Wang). The NEC-floor argument therefore carries the mandatory qualifier

wtot ≥ −1    only if   Q \= 0   or   the components are independently conserved.

Since §9 does not close general C4, weffobs is *gated by C4, not excluded*.

**C2 re-opened, with Sθc** defined separately. The canonical single-field PNGB self-crossing remains **NO-GO** (NEC, single-field Quintom no-go). However, the v1.2 use of Scb \= 0 to exclude the Goldstone non-adiabatic mode is a scope error: Scb \= 3(ζc − ζb) is the *cold–baryon* relative entropy (ZS-A20), and its vanishing is itself derived-conditional on single-source/adiabatic selection. The *Goldstone–cold* relative entropy is a *distinct* quantity,

Sθc \= 3(ζθ − ζc),

which the corpus does not compute; Scb \= 0 does *not* imply Sθc \= 0\. The multi-component non-adiabatic branch is therefore **OPEN** (falsification gate G-A18.M / G14).

# **§11. Proposition A22.8 — A Three-Barrier Map for the Surveyed Dynamical Completions**

**Statement (demoted from the v1.3 “Theorem A22.8 / C5 Gating Trichotomy”).** For the seven candidate completions examined in Appendix E — each (i) *zero-parameter* (no fitted constant beyond the locked **A**, **Q**), (ii) *ghost-free*, and (iii) intended to produce an observable w \< −1 crossing satisfying the admissibility criterion of §5 — each one is found to encounter ***at least one*** of three presently unresolved barriers. The map is a survey of the examined candidates, *not* a universal classification: a single completion may strike more than one barrier, and no claim is made that an as-yet-unsurveyed completion must strike any.

Table 11.1 — The three barriers, their corpus / literature source, and their honest status.

|  | Barrier a surveyed crossing encounters | Source | Honest status |
| :---: | ----- | ----- | ----- |
| **B1** | Reflection-positivity / healthiness. The lattice action’s OS-3 reflection positivity is proven for “positive A, V(ε) ≥ 0, no higher derivatives.” A generic higher-derivative (DHOST-type) completion with a rational propagator violates OS-3. | ZS-M17.3 (DERIVED); Arici et al. 2018 \[31\] | Healthiness *test*, not a universal No-Go. Higher derivatives generically break OS-3 \[31\], *but* reflection positivity is not categorically forbidden for them: an explicit six-derivative complex-ghost bound-state model satisfies OS-3 and a positive Källén–Lehmann representation \[32\]. \[**DERIVED-CONDITIONAL** for the restricted M17 rational-propagator class; **OPEN** in general.\] |
| **B2** | Departure from baseline M17.1 allocation. In the joint scaling limit only the X-sector converges to L²(M⁴) ⊗ ℂ¹¹ as a propagating continuum field; the Z-sector (seam) stays rank ≤ 2, an ln 2-capacity mediator. A propagating seam requires *leaving the assumptions* of this allocation. | ZS-M17.1 (DERIVED) | Two cases must be distinguished. (a) A Z-mode generated *within* the M17.1 assumptions conflicts with the theorem. (b) Adding a *new* boundary action or continuum sector *extends* the theory — it does not falsify M17.1. “Leaving the assumption scope” ≠ “falsifying the theorem.” \[**DERIVED** within the baseline; extension is a different theory.\] |
| **B3** | Absence of a *derived* late-time IR scale. The corpus derives ratios — H0ⁿᵒᶜ/H0ᶜᵐᴮ \= eA, ΩΛ/Ωm \= 2eA \= 2.1668 (−0.16σ) — but no action-level mechanism fixes the absolute scale H0/MP \~ 10⁻⁶¹. | ZS-F4; ZS-F10/U8 (DERIVED); NC-A19.3 | Not “impossible.” ZS-F10/U8 register τn \= tP·exp(nπ/A) (DERIVED, n \= 2, 5, 6), so exp(π/A) ≈ 1.08×10¹⁷ is a *single* Y-cycle factor, not a ceiling; e⁻³π/ᴬ ≈ 7.8×10⁻⁵² and e⁻⁴π/ᴬ ≈ 7.2×10⁻⁶⁹ bracket 10⁻⁶¹. The open question is which corpus mechanism fixes the exponent and prefactor; none is derived. \[**OPEN** debt, not a No-Go.\] |

Hence ***C5 remains a genuine OPEN***: of the surveyed completions none clears all three barriers, but the barriers are an inventory of present obstructions, not a proof that crossing is impossible. \[**DERIVED-interpretation / candidate-survey result.** B1 is **DERIVED-CONDITIONAL** for the restricted action class and **OPEN** in general; B2 is **DERIVED** within the baseline allocation; B3 is an **OPEN** debt.\]

**Candidate survey (Appendix E).** Seven zero-parameter completions were screened: (1) degenerate higher-derivative DHOST, (2) a kinetic term on the seam BF sector promoting the 37 modes, (3) a bimetric / massive-graviton sector, (4) a nonlocal completion, (5) integrating out the heavy radial mode, (6) a second Goldstone pairing with θ, and (7) seam i-tetration dynamics. In the survey, (1), (3), (4), (6) encounter B1 (a ghost or a rational-propagator OS-3 violation); (2) and (7) require leaving the M17.1 allocation (B2); (5) yields only 1/MP2\-suppressed corrections ≈ 10⁻¹²¹, an unobservable effect that does not generate the IR scale (B3-side). Several candidates encounter *more than one* barrier; this is expected and is the reason “exactly one” cannot be asserted. The survey is *not* exhaustive over all conceivable completions — a vector-tensor, dissipative, or multi-field route compatible with all three barriers cannot be excluded at this stage and is the content of the OPEN status.

**Corollary A22.8.1 (what a confirmed crossing decides).** A confirmed total super-acceleration (wtot \< −1, i.e. Ḣ \> 0\) at ≥ 3σ, or a dark-energy crossing shown physical beyond the §5 degeneracy, ***falsifies the strict frozen-attractor baseline*** (A22.1, under Premise P0) and ***activates the C1–C5 extension audit***. Which upstream structure must then change — a boundary dynamics (C1), a non-adiabatic Goldstone (C2), an emergent pole (C3), a general interaction (C4), or a dynamical seam (C5) — is **OPEN** and is decided only after the action-level analysis of each route. The v1.3 reading that a crossing “falsifies exactly one core axiom” over-states what a single observation determines and is withdrawn.

**Meta-confidence (stated honestly).** We assign ≈ 90% to the narrow judgement that *none of the seven surveyed candidates* evades all three barriers, and leave genuinely **OPEN** — with no committed probability — whether some unsurveyed zero-parameter, healthy completion can. This is the terminus the single paper ZS-A22 can reach; a dynamical seam completion is the subject of a future ZS-A23+ program (“dynamical completion of the topological seam,” or “a Z-Spin-compatible DHOST extension”). \[**NON-CLAIM** on the probability; it summarises the survey of App. E, not a measurement, and is explicitly not a universality claim.\]

# **§12. Premise P0 in Detail — The Late-Time Vacuum-Source Debt (Inherited)**

Premise P0, stated in §2.3 and used by the late-time crossing results (not by the structural lemmas), deserves an explicit ledger entry. The locked action has V(1) \= 0 and F(1) \= 1 \+ **A** constant. A *constant* F merely rescales the Planck mass, MP2 → MP2(1 \+ **A**); it does not by itself source a positive cosmological constant. In a matter-empty late-time limit the Friedmann equation then generically tends to H → 0, *not* de Sitter. The statement “V(1) \= 0 and F \= 1 \+ **A**, therefore the background is de Sitter” is thus conditional on an unspecified vacuum source.

Wald’s cosmic no-hair theorem assumes a positive Λ is *given*; it drives an existing Λ-dominated background to de Sitter, but it does not manufacture Λ from a constant Planck-mass rescaling. A22 must therefore declare which of the following supplies Λ \> 0, and include it at the action level: (i) a separate V0 \> 0; (ii) a boundary vacuum energy; (iii) an effective cosmological-constant term; or (iv) an FRW source actually derived upstream. ZS-F1 §6.4 records that V(1) \= 0 fixes Λ to arise from the (1 \+ **A**) gravity modification, but NC1 leaves the microscopic origin OPEN — so this is an inherited upstream debt, not a result of A22.

**Status.** \[**DERIVED-CONDITIONAL** / inherited OPEN.\] Premise P0 is logically *prior* to the phantom-divide question: until the vacuum source is fixed, A22.1 reads “if the late-time background is de Sitter, then ….” This is why the abstract and §4 label the result a *conditional* frozen-attractor No-Go. The debt is registered as falsification gate G16-F (§13), and discharging it — an upstream derivation of Λ \> 0 from (**A**, **Q**) — is a prerequisite for any unconditional version of the No-Go (gate G16-C).

**Per-result dependency ledger.** P0 is not a single point of failure for the whole paper. Only the late-time / cosmological statements rest on it; the structural results stand independently.

Table 12.1 — Dependence of each result on Premise P0.

| Result | Needs P0? | Why |
| ----- | :---: | ----- |
| A22.1 (strict-attractor No-Go) | **Yes** | Asserts a de Sitter late-time attractor. |
| A22.2 (accounting-invariance) | Partial | The TSD / reassignment argument is frame-algebraic; only its de Sitter reference branch uses P0. |
| A22.3 radial / vacuum carriers | **Yes** | Uses mρ ≫ H and the frozen attractor. |
| A22.3 Goldstone NEC bound | No | NEC \+ single-field Quintom no-go are background-independent. |
| A22.5a (current conservation) | No | Structural identity from antisymmetry. |
| A22.5b (rank-one channel) | No | Block-Laplacian rank-one reduction; algebraic. |
| A22.6 (conformal Q suppression) | Yes (strict-attractor part) | Q → 0 invokes the frozen attractor; the Q expression itself does not. |
| A22.7 (seam constraint-exclusion) | No | Reduced cellular-BF constraint dΓ p \= 0; kinematic. |

# **§13. Pre-Registered Gates**

The gates are sorted by logical role (a v1.5 reorganisation). **Falsification gates** (Table 13.1) would refute Premise P0 or a stated baseline result; **promotion / extension gates** (Table 13.2) would not refute the baseline but would move an OPEN route (C1–C5) toward DERIVED-CONDITIONAL. A22 makes no fitted parameter, so every gate is structural, not statistical. G13/G14 correct v1.2 (which presupposed BRST-exactness and mis-used Scb).

Table 13.1 — Falsification gates (refute Premise P0 or a baseline result).

| Gate | A stated result is falsified if … | Target |
| :---: | ----- | :---: |
| G1 | a total super-acceleration wtot \< −1 (Ḣ \> 0\) is confirmed at ≥ 3σ in {H, DM, DH, fσ8}, or a dark-energy crossing is shown physical beyond the §5 degeneracy. | A22.1 baseline |
| G2 | one of the seven surveyed candidates (App. E) is shown, on closer analysis, to clear *all three* barriers B1/B2/B3 (the survey misclassified it). | A22.8 survey |
| G3 | |1 \+ weff| is measured genuinely (not by accounting) at a level *inconsistent with heavy-mode decoupling* — i.e. not → 0 as the attractor is approached. This falsifies only the *strict-attractor application* (A22.1a/b baseline) and activates a rolling / non-adiabatic branch; it does not falsify the general heavy-field system, and no fixed numerical threshold is asserted (A22.1b gives only a conditional (H/mρ)⁴ quasi-static scaling). | A22.1a/b baseline |
| G4 | a spurious crossing *survives* correct reassignment of gravitational terms (the §5 reassignment-invariance fails to remove it). | A22.2 |
| G5 | cT ≠ c is observed at the relevant redshift (αT ≠ 0). | A22.3(d) |
| G6 | a running Planck mass αM ≠ 0 is detected at the late-time attractor (ε̇ ≠ 0). | A22.3(d) |
| G7 | an independent Quintom scalar is identified *inside* the cold–baryon dust sector. | A22.3(c) |
| G8 | a canonical, NEC-respecting single-field PNGB self-crossing is constructed. | A22.3(b) |
| G9 | the linearized conformal exchange is shown to be Q ≠ −½ αM H ρc (wrong coefficient or sign). | A22.6 |
| G10 | a linearized conformal crossing is produced with Ḟ \= 0 (contradicting Q ∝ Ḟ). | A22.6 |
| G16-F | no action-level Λ \> 0 source exists under the locked (A, Q) assumptions, so Premise P0 cannot be met. | P0 |

Table 13.2 — Promotion / extension gates (activate an OPEN route; not a falsification of the baseline).

| Gate | An OPEN route is promoted if … | Target |
| :---: | ----- | :---: |
| G11 | an admissible dim-≤ 6 / two-derivative operator outside the §8 channel produces a crossing (activates C4). | C4 / §9 |
| G12 | an explicit interacting C4 model gives a fundamental-phantom-free weffobs \< −1 (activates C4). | C4 / A22.7 |
| G13 | a full BFV/BRST computation shows the 37 seam modes are *not* all gauge — some are physical collective modes (supplies a C1 mechanism). *Corrected: v1.2 presupposed BRST-exactness.* | C1 / A22.7 |
| G14 | a computed Goldstone–cold relative entropy Sθc \= 3(ζθ − ζc) ≠ 0 admits a viable non-adiabatic crossing. *Corrected: v1.2 mis-used Scb.* | C2 / A22.7 |
| G15 | a zero-parameter ghost-free completion — surveyed or new — is constructed that clears *all three* barriers B1/B2/B3 and produces a crossing. | C5 / A22.8 |
| G16-C | an action-level Λ(A, Q) \> 0 source is derived, discharging the P0 debt and lifting A22.1 to an unconditional No-Go. | P0 closure |

# **§14. Conclusion**

The phantom divide w \= −1 is robust in Z-Spin against every *existing-field* and *bookkeeping* evasion we can test, *conditional on Premise P0*: the exact strict-attractor no-crossing and its heavy-mode decoupling estimate (A22.1a/b), the accounting-invariance theorem and its Total-Superacceleration Diagnostic (A22.2), existing-carrier No-Go in the strict adiabatic baseline (A22.3), the topological-current conservation lemma and its rank-one conformal-channel proposition (A22.5a/b), and frozen conformal-channel suppression with the corrected Q \= −½ αM H ρc (A22.6). These show that a Z-Spin crossing can come neither from the heavy radial mode, the canonical Goldstone, the conserved dust, frozen-F modified gravity, the linearized conformal channel, nor a frame choice.

The baseline No-Go is ***conditional, not complete***. Across v1.2→v1.5 four over-statements have been demoted — the seam result is constraint-exclusion under the reduced cellular-BF model, not BRST-exactness (A22.7, with Lclock-restrict restored to OPEN); the conformal suppression closes only the baseline C4 subroute (A22.6); the classification is a working taxonomy, not an “exactly five” theorem (§7); and the C5 gate is a *barrier map*, not a “trichotomy theorem” (A22.8, now a Proposition). C1 full boundary dynamics, the C2 multi-component non-adiabatic route, the C3 emergent pole, and general C4 interaction all remain OPEN, and a late-time vacuum source (Premise P0, §12) is owed upstream.

What this paper adds is a sharper, honestly bounded frontier. Proposition A22.8 replaces the vague “C5 is outside the baseline” with a survey: of seven zero-parameter healthy completions, each encounters at least one of three barriers — reflection-positivity / healthiness (B1), departure from the M17.1 allocation (B2), or the absence of a derived IR scale (B3) — while none is shown to clear all three and the inventory is not claimed exhaustive. A confirmed crossing therefore falsifies the conditional baseline and opens, rather than closes, the C1–C5 audit. Six concrete tasks remain: the full BFV presymplectic / ghost-complex computation behind Lclock-restrict; the Goldstone–cold relative entropy Sθc; a complete mass-dimension-6 operator basis with redundancy matrix for C4; an action-level mechanism fixing the late-time IR scale; the vacuum source of Premise P0; and a dynamical seam completion (C5), left to a ZS-A23+ program. The paper provides no new *dynamical* dark-energy solution, perturbation equations, or Boltzmann likelihood; it is a theoretical audit and a no-go map.

A ***cross-consistency audit*** of the dark sector (Appendix F) records what is and is not fixed. The *fractions* are zero-parameter-fixed by face counting (Ωm \= 38/121, ΩΛ \= 83/121, DERIVED, Planck 0.4%); the holonomy ratio 2eA is a second DERIVED expression agreeing with the face-counting ratio 83/38 to 0.8%, the residual being the *open* finite-Q correction F-F12.6 (1/Q² candidate, not derived). The locked action fixes these conditional dimensionless relations and the frozen-field response but *not* the absolute scale (Premise P0, B3) or any w ≠ −1 dynamics (B3, C5). So the corpus fixes *how much* dark energy there is (up to a known 0.8% internal tension), while *the absolute scale* and *whether it can cross* remain the open ZS-A23 targets. This appendix is a correction-of-record, not a closure.

# **Acknowledgements**

The v1.2→v1.3 revision was prompted by detailed external referee feedback identifying over-closures in v1.2 (the BRST-exactness claim, the missing factor ½ in Q, the EFT braiding sign, the energy-flow direction, the operator-exhaustion scope, the Scb vs Sθc conflation, and the late-time vacuum source). The v1.3→v1.4 revision was prompted by a second round of feedback identifying a new over-statement — the v1.3 “Theorem A22.8 / C5 Gating Trichotomy” — and a corpus conflict in its scale barrier with the ZS-F10/U8 τn \= tP·exp(nπ/**A**) hierarchy; A22.8 is accordingly demoted to a Proposition and a candidate-survey barrier map. The v1.4→v1.5 revision was prompted by a third round identifying the residual sign error in the conformal energy exchange (corrected here by the Einstein-frame derivation to Q \= −½ αM H ρc), a numerical residual inconsistency (now |1 \+ w| ≈ 5.6×10⁻¹²¹), and several scope and bookkeeping refinements; it also adds the constructive Appendix F. The v1.5→v2.0 revision was prompted by a fourth round: the v1.5 Appendix F was found to combine the face-counting Ωm with the holonomy ratio, reintroducing an over-closure that the upstream ZS-F12(Revised) had already corrected (the 0.8% face-counting-vs-holonomy gap is F-F12.6 OPEN). Appendix F is recast here as a cross-consistency audit; in addition, the central No-Go A22.1 is given its explicit Einstein-frame field-equation derivation, and the Frame-Independent Crossing Criterion (§5) is elevated to an operational diagnostic (the Ḣ-sign test). The v2.0→v2.1 revision was prompted by a fifth round that flagged two over-promotions in the strengthened §4–§5: A22.1’s Einstein-frame “proof” had dropped the matter-trace coupling that §9 uses (so its O(H²/mρ2) bound was not established), and the §5 criterion conflated a total-fluid super-acceleration with a dark-energy component crossing. In response, A22.1 is split into the exact Theorem A22.1a (w \= −1 at the attractor) and the DERIVED-CONDITIONAL Proposition A22.1b (heavy-mode decoupling estimate, now with the matter coupling restored), and the §5 diagnostic is rescoped and renamed the Total-Superacceleration Diagnostic: Ḣ \> 0 ⇔ wtot \< −1 is retained as a split-independent total-NEC test, while the “physical dark-energy crossing iff Ḣ \> 0” universal was withdrawn (a Quintom component crossing can have Ḣ \< 0; a frame caveat on Ḣ was added). The v2.1→v2.2 revision was prompted by a sixth round identifying three residual over-reaches: (i) A22.1a set U(φ\*) \= ρΛ while the locked potential has V(1) \= 0, so P0 is now made explicit as a separate vacuum source Tμν(P0) \= −ρP0 gμν and A22.1a is the combined-sector result, tagged DERIVED-CONDITIONAL (its w \= −1 being exact once P0 is given); (ii) A22.1b’s O(H²/mρ2) “upper envelope” was not derived — the quasi-static contribution in fact scales as 1 \+ wqs ≃ 27(αMP)²(Ωm2/ΩDE)(H/mρ)⁴, so 5.6×10⁻¹²¹ is now reported as a benchmark decoupling ratio, not a bound, and the transient is tied to a pre-specified initial amplitude; and (iii) gate G3 is made a conditional gate (a measured nonzero 1 \+ w falsifies only the strict-attractor application, not the general heavy-field system). The TSD is further scoped as a kinematic total-effective-EoS diagnostic under the constant-M\* reconstruction, and A22.3 retitled to its strict-adiabatic baseline. All numerical inputs derive from the locked geometric data (**A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6)); no parameter was fitted.

**Code Availability.** A three-layer verification script — (i) algebraic identities (Q \= −½ αM H ρc, the energy-flow sign, the e⁻ⁿπ/ᴬ hierarchy values, the residual 5.6×10⁻¹²¹, the TSD Ḣ-sign relation wtot \= −1 − (2/3)Ḣ/H², the A22.1b quasi-static (H/mρ)⁴ scaling (not (H/mρ)²), the face-counting fractions Ωm \= 38/121 and ΩΛ \= 83/121, and the OPEN F-F12.6 mismatch 83/38 ≠ 2eA), (ii) dependency / status checks (C1–C4 OPEN, A22.1a/b DERIVED-CONDITIONAL, the A19 v3.1 BRST scope, the Premise-P0 ledger, the F-F12.6 OPEN status), and (iii) logical-claim checks (P0 supplied as an explicit sector in A22.1a, the G3 conditional-gate consistency, the “at least one” vs “exactly one” distinction, the non-exhaustiveness of the candidate list, and that Appendix F claims neither a fraction closure nor a crossing) — accompanies this paper as zs\_a22\_v2\_2\_audit.py.

# **Appendix A — EFT-of-Dark-Energy Mapping (Corrected Braiding)**

For the locked action the only non-minimal Horndeski function is G4(Φ) \= ½ MP2 F(ε), with G3 \= G5 \= 0\. The effective-field-theory functions of Bellini–Sawicki (2014) are then

αM \= (d ln M\*2) / d ln a \= Ḟ / HF,    αT \= 0    (G5 \= 0, so cT \= c).

**The v1.2 error.** Version 1.2 wrote “G3 \= 0, therefore the braiding αB \= 0.” This is incorrect: for a field-dependent non-minimal coupling G4(Φ) the scalar and the metric mix kinetically even when G3 \= 0, and braiding arises from that field-dependence, not from G3 alone. In the standard normalization the conformal (non-minimal) subclass obeys

αB \= −αM,

so αB is *tied to* αM and is non-zero on any branch with Ḟ ≠ 0\. At the strict attractor, however, ε̇ → 0 ⇒ Ḟ \= 0 ⇒

αM \= αB \= αT \= 0,

and the residual kinetic function αK produces no crossing on its own. The baseline conclusion of A22.3(d) therefore stands, but its justification is the simultaneous vanishing of αM and αB at Ḟ \= 0, not the vanishing of G3. Away from the attractor, αB \= −αM ≠ 0 reintroduces braiding and is part of why general modified-gravity crossing (C4) is not closed.

# **Appendix B — Interaction-Frame Energy Budget (Corrected Sign and Factor)**

We fix the coupled continuity equations in the convention

ρ̇de \+ 3H(ρde \+ pde) \= −Q,    ρ̇c \+ 3Hρc \= \+Q.

In this convention Q \> 0 transfers energy from dark energy to dust (DE → dust) and Q \< 0 from dust to dark energy (dust → DE). The v1.2 text reversed this, calling Q \> 0 a dust-to-dark-energy flow; that is corrected here. The effective dark-energy equation of state that reproduces the same expansion history as if the sector were uncoupled is

weff \= wde \+ Q / (3Hρde),

so an *apparent* phantom weff \< wde (and a fortiori weff \< −1 when wde ≥ −1) requires Q \< 0\. To fix the sign of Q we work in the Einstein frame. With the standard conformal transformation gᴱμν \= F gᴶμν (so that the Einstein-frame action carries the canonical (MP2/2)RE), proper time scales as dτE \= √F dτJ and a Jordan-constant rest mass becomes mE \= mJ/√F ∝ F−1/2. For pressureless dust of conserved comoving number, the Einstein-frame source is the rate of change of this mass,

ρ̇c \+ 3Hρc \= (d ln mE) / dt ρc \= −½ Ḟ / F ρc,

and matching to ρ̇c \+ 3Hρc \= \+Q with αM \= Ḟ/(HF) gives

Q \= −½ αM H ρc ∝ −Ḟ,

which vanishes at the attractor (Ḟ \= 0\) and is negative — the apparent-phantom direction — precisely when αM \> 0 (F increasing). Three v1.2–v1.4 defects are now jointly repaired: the missing factor ½ (fixed in v1.3), the reversed flow direction (v1.3), and the *sign* of the coefficient (fixed here in v1.5: v1.4 wrote Q \= \+½ αM H ρc, which corresponds to mE ∝ F\+1/2, the opposite conformal convention). The qualitative result — no exchange at Ḟ \= 0, hence Q → 0 at the frozen attractor — is unchanged.

# **Appendix C — Scope of the Operator Census (Representative List)**

An “exhaustion” of couplings is well defined only after the operator basis is fixed. We restrict attention to a ***local*** sector: ***local operators up to mass dimension 6 and two derivatives, invariant under U(1)Z, Z2, and diffeomorphisms, with current conservation ∇μ Jμ \= 0 imposed.*** We list *representative* structures rather than constructing a complete basis with a redundancy matrix; integration by parts and field redefinition would still have to be applied systematically before any count is asserted. Within this local sector the five v1.2 representatives are the conformal current term Jμ∂μf, the density coupling F(ε)J², the curvature coupling F(ε)R, the Goldstone coupling G(θ)J², and a generic higher-derivative term.

**Not covered by the rank-one channel of §8.** The following independent tensor structures are admissible in the declared basis yet are *not* captured by the rank-1 residue-mode approximation, and must be examined individually before any exhaustion is claimed:  
    • Rμν Jμ Jν  (curvature–current);  
    • Jμ Jν ∇με ∇νε  (mixed derivative);  
    • J² (∇θ)²  (Goldstone–current);  
    • f(ε, J²)  (general scalar function);  
    • (∇μ Jν)(∇μ Jν)  (current-gradient).

**Outside the local sector.** Disformal couplings and nonlocal / boundary operators lie *outside* the declared local basis altogether and are *not* part of the local census above; they would require a separate weakly-nonlocal or boundary-operator treatment. (The v1.3 text listed them inside the “local basis” enumeration, which was a category error and is corrected here.)

**Status.** \[**OPEN** operator-census specification.\] Appendix C of v1.2, and the present §9, constitute a ***check of representative baseline couplings***, not a complete operator census with a redundancy matrix, and the disformal / nonlocal / boundary sector is untouched. The general interacting class C4 is correspondingly OPEN.

# **Appendix D — Seam Cohomology Status and the Uncomputed Sθc**

**Seam modes.** On Γ38 the relative Laplacian LΓ has rank 37\. Under the reduced cellular-BF flatness constraint dΓ p \= 0, the 37 non-uniform relative modes fail the constraint and are *constraint-excluded*, giving dim H⁰ \= 1 in that reduced model. This reproduces ZS-A19 v3.1 Appendix I exactly. What is *not* established — contrary to v1.2 — is that these modes are BRST-exact (im QBRST): that requires the full edge-sector ghost complex, and the ZS-F0 boundary term must be checked for mixing. The clock-restriction computation

BFV presymplectic form → ghost complex → H•(QBFV) → rank K∂,phys

is therefore restored to OPEN as the leading task, and C1 is not closed.

**Relative entropies.** The cold–baryon relative entropy is Scb \= 3(ζc − ζb), computed in ZS-A20; Scb \= 0 is derived-conditional on single-source/adiabatic selection on the branching hypersurface. The *Goldstone–cold* relative entropy relevant to a non-adiabatic Quintom escape is a *distinct* quantity,

Sθc \= 3(ζθ − ζc),

which the corpus does not compute. Hence Scb \= 0 does not imply Sθc \= 0, the v1.2 use of Scb to close the Goldstone non-adiabatic mode is a scope error, and the multi-component non-adiabatic branch of C2 is OPEN (gate G-A18.M / G14). Deriving the Sθc perturbation system is a concrete next step.

# **Appendix E — Candidate-Survey Record for C5 (the Barrier Map)**

This appendix records the structured survey behind Proposition A22.8, following the corpus deep-exploration protocol (long list → MECE issue list → issue tree → per-node epistemic tagging → convergence test → scoring / self-reference). It is a survey of the examined candidates, not an exhaustiveness proof.

## **E.1 Long list (seven candidate completions)**

C5-DHOST (degenerate higher-derivative scalar-tensor, Ostrogradsky-evading); C5-seam-kinetic (a kinetic term promoting the 37 BF modes); C5-bimetric (a second metric / massive graviton); C5-nonlocal (integrating out heavy modes nonlocally); C5-integrate-out (heavy radial mode → effective higher-derivative corrections); C5-extra-Goldstone (a second Goldstone pairing with θ); C5-i-tetration (seam i-tetration dynamics generating light modes). Dropped to the issue tree: bimetric, nonlocal, and extra-Goldstone collapse into the healthiness gate I1; integrate-out is a Planck-suppressed null handled under I3; i-tetration is NON-CLAIM under I2.

## **E.2 Issue list (MECE, in order of leverage)**

Table E.1 — Three issues controlling C5.

| Rank | Issue | Why it dominates |
| :---: | ----- | ----- |
| **I1** | Healthiness gate — which completion passes ghost-free, OS-positive, cT \= c? | An unhealthy completion is eliminated immediately (B1). |
| **I2** | Continuum structure — does M17 supply a propagating seam mode? | A propagating Z-sector requires leaving the M17.1 allocation (B2). |
| **I3** | Scale problem — can the H0 mass be generated from A, Q with no free parameter? | Absence of a derived IR scale (B3). |

## **E.3 Issue tree and per-node epistemic status**

**ROOT:** is a zero-parameter ghost-free C5 with w \< −1 possible?  
├─ I1 Healthiness gate  
│   ├─ I1.a DHOST higher-derivative with a rational propagator → violates OS-3 reflection positivity \[31\]; *but* not universally — an explicit six-derivative complex-ghost bound-state model satisfies OS-3 \[32\], so B1 is a healthiness *test*. \[**DERIVED-CONDITIONAL** for the restricted class; **OPEN** in general.\]  
│   ├─ I1.b phantom (wrong-sign kinetic) → ghost; excluded by the ghost-free baseline. \[**PROVEN**.\]  
│   └─ I1.c GW170817 cT \= c → narrows DHOST to class Ia; stable crossing there needs multiple α-functions. \[**IMPORTED-PROVEN**.\]  
├─ I2 Continuum structure  
│   ├─ I2.a M17.1: only the X-sector becomes a continuum field; the Z-sector is an ln 2 mediator. \[**DERIVED**.\]  
│   ├─ I2.b promoting the 37 BF modes → requires leaving the M17.1 allocation assumptions (an extension, not a falsification of the theorem). \[**DERIVED** within the baseline.\]  
│   └─ I2.c i-tetration contraction (|f′(z\*)| \= 0.892) → stable, opposing light modes; conjugacy to the Friedmann flow unproven. \[**NON-CLAIM**.\]  
└─ I3 Scale problem  
    ├─ I3.a H0/MP \~ 10⁻⁶¹ not derived; only ratios eA, 2eA. \[**DERIVED**.\]  
    ├─ I3.b exp(π/A) ≈ 1.08×10¹⁷ is a *single* Y-cycle factor, not a ceiling: ZS-F10/U8 register τn \= tP·exp(nπ/A) (DERIVED, n \= 2, 5, 6), and e−3π/A ≈ 7.8×10⁻⁵², e−4π/A ≈ 7.2×10⁻⁶⁹ bracket 10⁻⁶¹ — so the scale is arithmetically reachable. What is missing is a derived exponent and prefactor. \[**OPEN** debt, not a No-Go.\]  
    ├─ I3.c anti-numerology (NC-A19.3) forbids a tuned A,Q exponent. \[**DERIVED**.\]  
    └─ I3.d integrating out the heavy radial mode → 1/MP2\-suppressed corrections ≈ 10⁻¹²¹ (no observable effect). \[**DERIVED**.\]

## **E.4 Convergence and scoring**

All seven surveyed candidates encounter at least one of the three barriers — reflection-positivity / healthiness (I1/B1), departure from the M17.1 allocation (I2/B2), or the absence of a derived IR scale (I3/B3). Several encounter *more than one*, which is why “exactly one” is not asserted. This is the protocol’s “converged but not closed → genuine OPEN” case (cf. ZS-F23 Condition C / Step 1′): of the surveyed completions none clears all three barriers, but the survey is *not* exhaustive over all conceivable completions, and the barriers are an inventory of present obstructions, not absolute no-gos — each barrier’s honest status is in Table 11.1 (B1 conditional / OPEN, B2 derived-within-baseline, B3 OPEN debt). Meta-confidence: ≈ 90% that *none of the seven surveyed candidates* evades all three barriers; whether an unsurveyed zero-parameter healthy completion can is left genuinely OPEN, with no committed probability. \[**NON-CLAIM**; explicitly not a universality claim.\]

# **Appendix F — A Cross-Consistency Audit of the Face-Counting and Holonomy Dark-Sector Fractions**

The No-Go results of §4–§11 concern a *crossing* of w \= −1; they do not say the corpus lacks dark energy. A22.1 describes the equation-of-state behaviour *conditional on an independently supplied late-time vacuum source* (Premise P0). A natural follow-up question is whether the dark-sector *fractions* are themselves zero-parameter-fixed. They are — by face counting — but the corpus also carries a second, holonomy route, and the two agree only to 0.8%. This appendix audits the two routes and inherits the upstream status of their mismatch, correcting an over-statement in the v1.5 draft of this appendix.

**Route 1 — the face-counting budget (DERIVED).** The Q² \= 121 register partitions into polyhedral face slots:

Ωb \= 6/121,    Ωcdm \= 32/121,    Ωm \= (6 \+ 32)/121 \= 38/121 \= 0.3140,    ΩΛ \= 83/121 \= 0.6860.

These close exactly, (6 \+ 32 \+ 83)/121 \= 1, so flatness is built in, *not* an independent check. Against Planck 2018 the budget matches to 0.4% (Ωm \= 0.3153 ± 0.0073, ΩΛ \= 0.6847). \[**DERIVED**; ZS-F2 §11.4, The Book L16. The face value 38/121 differs from the slot count 39/121 by exactly 1/Q², the Z₂-odd gauge mode of the Boundary Mode Theorem (ZS-F2 §11.7).\] The implied face-counting ratio is

rface \= ΩΛ/Ωm \= 83/38 \= 2.1842.

**Route 2 — the holonomy ratio (DERIVED expression).** Independently, ZS-F4 §6 derives the Wilson-loop holonomy factor eA, and ZS-F12 (Theorem TDO-1) the tetrahedral V↔F factor 2, giving a closed-form ratio

rhol \= 2eA \= 2.1668.

**The mismatch is OPEN, not closed (correction-of-record).** The two routes do *not* coincide: (rface − rhol)/rhol \= (2.1842 − 2.1668)/2.1668 \= 0.805%. The upstream corpus registers this as **F-F12.6 OPEN**, with a candidate 1/Q² \= 0.826% finite-Q correction that matches the gap to about 3% but is *not* derived (NC-F12.5). The v1.5 draft of this appendix combined the face-counting Ωm with the holonomy ratio and reported the resulting 0.55% as a “joint determination”; that mixed the two routes and is withdrawn. The honest statement is that face counting fixes the fractions, the holonomy ratio is a second DERIVED expression agreeing to 0.8%, and the exact bridge between them is an open finite-Q correction.

**What the locked action does and does not provide.** The locked action (V(1) \= 0, F \= 1 \+ **A**, mρ \= 2**A** MP) fixes these conditional dimensionless fraction relations and the frozen-field response (A22.1), but it does *not* by itself provide the absolute late-time vacuum source: a *constant* F merely rescales the Planck mass. The overall normalisation (ρcrit, H0) enters through the Z-Clock value νnow ≈ 3.575, which is *calibrated* to the present epoch rather than derived from (**A**, **Q**); and ρZ \= 0 is PROVEN (ZS-F9), so the Z-sector sources no vacuum energy. Absolute scale: OPEN (Premise P0, B3). Dynamics (any w ≠ −1 evolution): OPEN (B3, C5).

**Status.** \[Face-counting fractions ΩΛ \= 83/121, Ωm \= 38/121: **DERIVED** (ZS-F2; Planck 0.4%). Holonomy ratio 2eA: **DERIVED** as a holonomy expression; its identification with the cosmic ratio is **DERIVED-CONDITIONAL** on F-F12.6. Face↔holonomy agreement (83/38 ≈ 2eA): **OBSERVATION / OPEN** finite-Q bridge (F-F12.6; 1/Q² candidate, not derived). Absolute scale and dynamics: **OPEN**.\] Read correctly, this appendix is a cross-consistency audit and a correction-of-record: it surfaces a genuine 0.8% internal tension in the dark sector and inherits its OPEN status, rather than claiming a closure. Deriving the finite-Q bridge, or νnow from (**A**, **Q**), is left to the ZS-A23 program.

**\[1\]**  DESI Collaboration (M. Abdul-Karim et al.), DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints, Phys. Rev. D 112, 083515 (2025), arXiv:2503.14738 \[astro-ph.CO\].

**\[2\]**  R. M. Wald, Asymptotic behavior of homogeneous cosmological models in the presence of a positive cosmological constant, Phys. Rev. D 28, 2118 (1983).

**\[3\]**  E. Bellini and I. Sawicki, Maximal freedom at minimum cost: linear large-scale structure in general modifications of gravity, JCAP 07 (2014) 050\.

**\[4\]**  P. Creminelli and F. Vernizzi, Dark energy after GW170817, Phys. Rev. Lett. 119, 251302 (2017).

**\[5\]**  J. M. Ezquiaga and M. Zumalacárregui, Dark energy after GW170817: dead ends and the road ahead, Phys. Rev. Lett. 119, 251304 (2017).

**\[6\]**  L. Amendola, Coupled quintessence, Phys. Rev. D 62, 043511 (2000).

**\[7\]**  J. D. Brown, Action functionals for relativistic perfect fluids, Class. Quantum Grav. 10, 1579 (1993).

**\[8\]**  M. Chevallier and D. Polarski, Accelerating universes with scaling dark matter, Int. J. Mod. Phys. D 10, 213 (2001).

**\[9\]**  E. V. Linder, Exploring the expansion history of the universe, Phys. Rev. Lett. 90, 091301 (2003).

**\[10\]**  R. R. Caldwell, A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state, Phys. Lett. B 545, 23 (2002).

**\[11\]**  A. Vikman, Can dark energy evolve to the phantom?, Phys. Rev. D 71, 023515 (2005).

**\[12\]**  B. Feng, X. Wang and X. Zhang, Dark energy constraints from the cosmic age and supernova (Quintom), Phys. Lett. B 607, 35 (2005).

**\[13\]**  W. Hu, Crossing the phantom divide: dark energy internal degrees of freedom, Phys. Rev. D 71, 047301 (2005).

**\[14\]**  G.-B. Zhao, J.-Q. Xia, M. Li, B. Feng and X. Zhang, Perturbations of the quintom models of dark energy, Phys. Rev. D 72, 123515 (2005).

**\[15\]**  S. Antusch, S. F. King and X. Wang, Coupled Dark Energy and Dark Matter for DESI: An Effective Guide to the Phantom Divide, arXiv:2604.08449 \[astro-ph.CO\] (2026).

**\[16\]**  LIGO Scientific and Virgo Collaborations et al., Multi-messenger observations of a binary neutron star merger (GW170817), Astrophys. J. Lett. 848, L13 (2017).

**\[17\]**  Z-Spin Cosmology, ZS-F0: Foundations and the boundary term.

**\[18\]**  Z-Spin Cosmology, ZS-F1 §6.4: vacuum structure and V(1) \= 0 (NC1).

**\[19\]**  Z-Spin Cosmology, ZS-F2: the locked geometric data (A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6)).

**\[20\]**  Z-Spin Cosmology, ZS-F4: the duality ratio e^A and Ω\_Λ/Ω\_m \= 2e^A.

**\[21\]**  Z-Spin Cosmology, ZS-F10 / ZS-U8 §4: the timescale hierarchy τ\_n \= t\_P·exp(nπ/A) (DERIVED; registered for n \= 2, 5, 6).

**\[22\]**  Z-Spin Cosmology, ZS-F23: Condition C / Step 1′ (the genuine-OPEN protocol).

**\[23\]**  Z-Spin Cosmology, ZS-M17: the continuum limit (M17.1 sectoral allocation) and healthy-QFT structure (M17.3 reflection positivity).

**\[24\]**  Z-Spin Cosmology, ZS-A8 / A9: the expansion–contraction duality (1 \+ A) ↔ (1 − 2A).

**\[25\]**  Z-Spin Cosmology, ZS-A18: the multi-component / non-adiabatic gate (G-A18.M).

**\[26\]**  Z-Spin Cosmology, ZS-A19 v3.1, Appendix I: seam graph Γ₃₈, constraint-exclusion under d\_Γ p \= 0\.

**\[27\]**  Z-Spin Cosmology, ZS-A20: cold–baryon relative entropy S\_cb \= 3(ζ\_c − ζ\_b).

**\[28\]**  Z-Spin Cosmology, ZS-A21: rank-one residue-mode structure of the conformal channel.

**\[29\]**  Z-Spin Cosmology, ZS-U2 §3.1: retracted accounting-artifact instance (w₀ ≈ −0.997, w\_a ≈ \+0.12).

**\[30\]**  Z-Spin Cosmology, The Book of Z-Spin Cosmology v9.0 (Light OS for AI).

**\[31\]**  F. Arici, D. Becker, C. Ripken, F. Saueressig and W. D. van Suijlekom, Reflection positivity in higher derivative scalar theories, J. Math. Phys. 59, 082302 (2018), arXiv:1712.04308.

**\[32\]**  M. Asorey, G. Krein, M. Pardina and I. L. Shapiro, Reflection positivity in a higher-derivative model with physical bound states of ghosts, JHEP 02 (2026) 020, arXiv:2511.15283.

**\[33\]**  M. Asorey, G. Krein, M. Pardina and I. L. Shapiro, Bound states of massive complex ghosts in superrenormalizable quantum gravity theories, JHEP 01 (2025) 113, arXiv:2408.16514.

**\[34\]**  K. Lodha et al. (DESI Collaboration), Extended Dark Energy analysis using DESI DR2 BAO measurements (2025), arXiv:2503.14743 \[astro-ph.CO\].

**\[35\]**  B. R. Dinda, R. Maartens and S. Saito, No evidence for phantom crossing: local goodness-of-fit improvements do not persist under global Bayesian model comparison (2026), arXiv:2605.13546 \[astro-ph.CO\].

# **Version History**

| Version | Date | Change |
| :---: | :---: | ----- |
| v1.0 | — | Conservative gate-paper skeleton: strict-attractor No-Go, accounting-invariance, carrier exhaustion, extension classification. No premature closure. |
| v1.1 | — | Added the β0\-channel energy-exchange argument (A22.6). Qualitative conclusion retained but with equation and uniqueness errors. |
| v1.2 | — | Added the seam BRST argument (A22.7) and claimed C1, C2, C4 closed with C5 the unique survivor. Over-closed relative to the corpus. |
| **v1.3** | Jun 2026 | Honest reclassification. A22.6 → Proposition (Frozen Conformal-Channel Suppression), Q \= ½ αM H ρc; A22.7 → Proposition (Conditional Seam Constraint-Exclusion), Lclock-restrict restored OPEN. Errata fixed: factor ½ in Q, αB \= −αM, energy-flow sign. C1/C2-non-adiabatic/C3/general-C4 re-opened; Sθc defined. New Theorem A22.8 (C5 Gating Trichotomy) and §12 vacuum-source debt. Gates extended to G1–G16. Display equations typeset as centred Unicode math runs; Heading styles applied. |
| **v1.4** | Jun 2026 | Second-round corrections. “Theorem A22.8 / C5 Gating Trichotomy” → Proposition A22.8 (a candidate-survey three-barrier map): “exactly one” → “at least one of the surveyed barriers,” and the scale barrier B3 corrected against the DERIVED ZS-F10/U8 hierarchy τn \= tP·exp(nπ/A) (n \= 2, 5, 6\) — exp(π/A) is a single Y-cycle factor, so B3 is an OPEN debt, not a No-Go. B1 (reflection positivity) made a conditional healthiness test, citing the OS-3 counterexample \[32\]; B2 reworded as “leaving the M17.1 assumptions,” not falsifying. Corollary A22.8.1 softened (a crossing falsifies the conditional baseline and opens the C1–C5 audit). “Exactly five classes” → working taxonomy (§7); A22.5 split into Lemma A22.5a (current conservation, covariant Jμ \= ∇νΣμν) and Proposition A22.5b (rank-one channel); Appendix C relabelled a representative list (OPEN census); vacuum source promoted to Premise P0 (§2.3); subtitle drops “Trichotomy.” References restored to full APS/arXiv form (\[1\], \[15\], \[21\], \[31\]–\[35\]); verification split into three layers with an accompanying audit script. |
| **v1.5** | Jun 2026 | Third-round corrections. The conformal energy-exchange *sign* is corrected: with gᴱ \= F gᴶ the Einstein-frame cold mass is mE ∝ F−1/2, giving Q \= −½ αM H ρc (v1.4 had \+½); App. B now carries the explicit Einstein-frame derivation, and gate G9 is updated. The attractor residual is made consistent with the paper’s own inputs, |1 \+ weff| ≈ 5.6×10⁻¹²¹ \= (H0/mρ)² (was 1.9×10⁻¹²¹). Abstract recount (“Four results”; Lemma A22.5a / Proposition A22.5b, not “Theorem A22.5”). A22.5b narrowed to the corpus block-Laplacian coupling and tagged DERIVED-CONDITIONAL; Σμν fixed to an ordinary antisymmetric tensor (no “tensor density”). Gates split into Falsification (Table 13.1, G1–G10, G16-F) and Promotion / Extension (Table 13.2, G11–G15, G16-C); G2 rescoped to the surveyed candidates; G16 split. A per-result Premise-P0 dependency ledger added (Table 12.1). \[35\] authors added (Dinda, Maartens, Saito). Front-page note shortened to a brief status pointer. **New: Appendix F** — a zero-parameter account of the dark-energy density (ΩΛ/Ωm \= 2eA and Ωm \= 38/121), explicitly NOT a closure of P0/B3/C5. Verification banner reworded (audit implemented and attached; rerun recommended); audit script zs\_a22\_v1\_5\_audit.py. |
| **v2.0** | Jun 2026 | Fourth-round corrections plus substantive strengthening. **Appendix F corrected**: the v1.5 draft combined the face-counting Ωm \= 38/121 with the holonomy ratio 2eA and reported the 0.55% residual as a “joint determination,” reintroducing an over-closure the upstream ZS-F12(Revised) had already fixed. Recast as a *cross-consistency audit*: the face-counting fractions (Ωm \= 38/121, ΩΛ \= 83/121) are DERIVED and close exactly; the holonomy ratio 2eA \= 2.1668 agrees with the face-counting ratio 83/38 \= 2.1842 only to 0.8%, the residual being the OPEN finite-Q correction F-F12.6 (1/Q² candidate, not derived). The “A22.1 is a dark-energy solution” and “the locked action is the solution” over-statements are withdrawn. **A22.1 strengthened**: explicit Einstein-frame scalar-tensor FRW field equations and a two-channel suppression derivation (transient a⁻³ \+ quasi-static H²/mρ2) added; |1 \+ w| notation fixed to a reference scale. **FICC elevated (§5)**: a sharp, model-independent, operational form added — a phantom crossing is physical iff Ḣ \> 0 (super-acceleration), wtot \= −1 − (2/3)Ḣ/H²; applied to DESI (wtot ≈ −0.7) it shows the w0wa crossing is split-dependent, a structural companion to \[35\]. Subtitle updated; audit script zs\_a22\_v2\_0\_audit.py adds the F-F12.6 and FICC tests. |
| **v2.1** | Jun 2026 | Fifth-round corrections to the two claims strengthened in v2.0. **A22.1 split and matter coupling restored**: v2.0’s Einstein-frame “proof” dropped the matter-trace source that §9 uses, so its O(H²/mρ2) bound was not established. A22.1 is now **Theorem A22.1a** (EXACT: ε̇ \= 0, F constant, Q \= 0 ⇒ w \= −1, a theorem given P0) plus **Proposition A22.1b** (heavy-mode decoupling *estimate*, DERIVED-CONDITIONAL), with the coupled-quintessence source αρm restored (consistent with §9); only the decoupling is claimed robust, the coefficient is not. **FICC → Total-Superacceleration Diagnostic (TSD)**: the v2.0 universal “physical dark-energy crossing iff Ḣ \> 0” conflated a total-fluid super-acceleration with a component crossing and is withdrawn. Retained: Ḣ \> 0 ⇔ wtot \< −1, a split-independent *total* NEC test in the matter frame. Added: a Quintom counterexample (wde \< −1 with Ḣ \< 0), a frame caveat (Hᴱ \= F−1/2(Hᴶ \+ Ḟ/2F), so Ḣ is not a universal invariant), and the corrected DESI reading — the mean CPL fits give min wtot(z) ≈ −0.5 \> −1, so the crossing is *degenerate* with interacting/MG models, not shown unphysical. Subtitle renamed; audit zs\_a22\_v2\_1\_audit.py. |
| **v2.2** | Jun 2026 | Sixth-round corrections; three physics fixes plus editorial. **A22.1a P0 made explicit**: since the locked potential has V(1) \= 0, the Λ is now an explicit separate source Tμν(P0) \= −ρP0 gμν, and A22.1a is stated as the combined-sector result wDE \= −1, tagged **DERIVED-CONDITIONAL** (the earlier “DERIVED, exact, conditional” tag was a classification contradiction; the result is exact once P0 is given). **A22.1b benchmark, not bound**: the quasi-static contribution is derived to scale as 1 \+ wqs ≃ 27(αMP)²(Ωm2/ΩDE)(H/mρ)⁴ — a *fourth*\-power, not (H/mρ)² — so 5.6×10⁻¹²¹ is recast as a benchmark heavy-mode decoupling ratio, not an upper bound on 1 \+ w, and the transient is tied to a pre-specified initial amplitude. **G3 made conditional**: a genuine nonzero 1 \+ w now falsifies only the strict-attractor application (A22.1a/b baseline) and activates a rolling branch, with no fixed numerical threshold asserted. **TSD scope tightened**: rescoped as a kinematic total-effective-EoS diagnostic under the constant-M\* reconstruction (Ḣ \> 0 ⇔ wtot \< −1, not a fundamental matter+field NEC theorem when Ḟ ≠ 0). Editorial: A22.3 retitled “Existing-Carrier No-Go in the Strict Adiabatic Baseline”; §6 radial-mode line dropped the universal 10⁻¹²¹ number; correction-round count fixed to six; audit zs\_a22\_v2\_2\_audit.py adds the (H/mρ)⁴ power, P0-in-sector, and G3-consistency checks. |

*— End of ZS-A22 v2.2 —*