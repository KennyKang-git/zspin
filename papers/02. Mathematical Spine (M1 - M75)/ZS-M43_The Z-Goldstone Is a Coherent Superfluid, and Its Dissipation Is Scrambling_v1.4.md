**ZS-M43**

**The Z-Goldstone Is a Coherent Superfluid, and Its Dissipation Is Scrambling**

***Why the Effective-Hydrodynamics η/s Programme (Route B of ZS-M42) Dissolves, and the A-Scaled Unitary-Scrambling Structure That Replaces It — with an Anosov / Selberg Geometric Model and the s \= 1/2 Confluence***

Author: **Kenny Kang**  
Affiliation: Z-Spin Cosmology Collaboration  
Date: June 2026  
Theme / Paper Code: Mathematical Spine — ZS-M43 (Route B of ZS-M42 §7)  
Version: v1.4 (June 2026\)

**Verification: 22/22 structural-consistency PASS  |  Zero New Free Parameters  |  A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) LOCKED. The Z-Goldstone is a coherent Euler/superfluid field (DERIVED-interpretation; corpus static instance ρθ ∝ 1/r², DERIVED). It has no thermal viscosity: a thermal η/s and the KSS bound do not apply, because θ never thermalizes (ZS-F1 §7.2) and the dynamics is unitary (ZS-F1 §12.1). The correct, parameter-free dissipation is unitary scrambling, set by the i-tetration leak 1−|λ²| ≈ 0.205 per cycle (|λ²| ≈ 0.795, PROVEN) and the master-equation rates λ\_fast \= −A, γ\_xz \= 2A/Q, γ\_zy \= 6A/Q (PROVEN/DERIVED), propagating at a butterfly velocity v\_B ≤ ρ(ℒ)·a (ZS-M17). Its geometric model is Anosov geodesic mixing; via the Selberg bridge this meets ZS-M4’s critical line at the s \= 1/2 ↔ λ \= 1/4 confluence (HYPOTHESIS-strong).**

**§0. Abstract**

ZS-M42 \[1\] proved a Two-Gate No-Go for deriving the Navier–Stokes equations in Z-Spin and proposed, as Route B, an effective hydrodynamics built from the Goldstone phase θ of the Z-bias field. This paper resolves Route B. The Goldstone sector does furnish a coherent relativistic Euler / superfluid hydrodynamics, whose worked static instance is the corpus halo ρθ ∝ 1/r² (ZS-A1/A2/F1 \[3–5\]). Its equation of state is fixed with no free parameter: a stiff fluid (w \= 1, luminal sound speed c\_s \= 1\) when the Goldstone evolves in time, and an anisotropic global-monopole configuration (p\_r \= ρ, p\_t \= −ρ, mean w̄ \= −1/3) when it is the static halo. But the dissipative extension that Route B sought — an effective shear viscosity η, an entropy density s, and the ratio η/s — does not exist as a thermal object: θ never thermalizes (ZS-F1 §7.2 \[5\]) and the full dynamics is unitary, with scrambling rather than thermal entropy (ZS-F1 §12.1). The thermal-fluid framing fails a self-consistency test (a naive viscosity estimate is unstable and a thermal temperature is not uniquely fixed; §3 and Appendix C), which is the signature of a wrong identification, not of a hard calculation.  
The positive result is that the correct dissipation is **unitary scrambling**, a parameter-free structure already present in the corpus: the i-tetration map at its fixed point z\* rotates by arg λ ≈ 129.4° per step and ‘leaks’ by 1−|λ²| ≈ 0.205 per X→Z→Y→Z→X cycle (|λ²| ≈ 0.795, ZS-M1 PROVEN), coarse-grained for X-observers into the master-equation rates λ\_fast \= −A, γ\_xz \= 2A/Q, γ\_zy \= 6A/Q (ZS-Q7, ZS-F0). We quantify this with the out-of-time-order correlator (OTOC) and a butterfly velocity bounded by the Lieb–Robinson velocity v\_B ≤ ρ(ℒ)·a (ZS-M17 \[2\]); the Maldacena–Shenker–Starinets... \[chaos\] bound λ\_L ≤ 2πT is noted to be inapplicable for the same non-thermal reason that retires η/s. Finally, the i-tetration dilation rapidity αBK \= −ln|z\*| \= 0.5664 (ZS-M4 Theorem 3, PROVEN) places the scrambling within the Berry–Keating / Anosov geodesic-flow picture; through the Selberg trace formula this meets ZS-M4’s critical line at the s \= 1/2 ↔ λ \= 1/4 confluence, where the 2025 Anantharaman–Monk optimal spectral gap \[10,11\] lives. We test whether the underlying operator map (ZS-M4’s transfer operator → a Selberg/Laplacian operator) can be built in the Pmax → ∞ limit and find it blocked at the same gap that blocks ZS-M4’s Riemann connection, so the confluence remains HYPOTHESIS-strong (structural), not DERIVED. Several results are stated as formal claims: Lemma M43.1 (unitary \+ non-thermalizing ⇒ η/s is the indeterminate 0/0, KSS vacuous); Proposition M43.2 (the X-observer entropy-production rate cross-checks the ZS-F16 Wilson dissipation to 0.16% and is bounded by the ZS-Q7 capacity ln 2); and the identification of the stiff (w \= 1\) regime with the ZS-M12 centrifugal-launch term Q\_w²/(2a⁶ε²), Q\_w \= A, with the stiff field shown to be anisotropy-subdominant by a factor ∼ A² near the cyclic bounce; and Lemma M43.3, a cardinality obstruction (an at-most-11-point spectrum cannot map to the infinite hyperbolic-Laplacian spectrum) that rigorously blocks the fixed-Q operator map. Zero new free parameters throughout.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Established with full rigor (here: cited from the corpus or external theorems). |
| **DERIVED** | Follows from the Z-Spin action \+ standard physics, zero free parameters. |
| **DERIVED-interpretation** | Synthetic reading of standard physics; not Z-Spin-specific. |
| **HYPOTHESIS-strong** | Multiple independent structural anchors; promotion path documented. |
| **IMPORTED** | Proved externally and used without re-proof; full citation given. |
| **OPEN** | Recognized gap honestly registered for future work. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted. |

**§1. Introduction**

ZS-M42 \[1\] established that an ordinary micro-to-Navier–Stokes derivation in Z-Spin factors through a locality gate G1 (to which the ZS-M17 Lieb–Robinson estimate \[2\] contributes) and a chaos/entropy gate G2 (for which Z-Spin supplies nothing), and is therefore obstructed at G2. ZS-M42 §7 proposed Route B: build an effective hydrodynamics directly from the Goldstone phase θ. This paper carries Route B to its conclusion and finds a sharper, more useful result than the one sought.  
The Goldstone sector gives a coherent Euler/superfluid hydrodynamics (§2), but not a thermal one. §3 shows that the thermal viscosity / η/s programme is not merely hard but **ill-posed**: θ never thermalizes and the dynamics is unitary, so there is no thermal temperature and no thermal entropy, and the KSS bound does not apply. The constructive content begins in §4: the dissipation that physically exists in the Z-sector is **unitary scrambling**, a parameter-free structure. §5 quantifies it (OTOC, butterfly velocity), §6 gives its geometric model (Anosov mixing, the Selberg bridge, and the s \= 1/2 confluence with ZS-M4, including a test of whether that confluence can be lifted to a theorem). §7 records gates and non-claims; §8 concludes.

**§2. The Goldstone Phase as a Coherent Hydrodynamic Field**

Write the Z-bias field as Φ \= ρ eiθ with vacuum |Φ| \= 1; the radial mode ρ is heavy and the angular mode θ is an exactly massless Goldstone boson, with conserved winding charge Q \= a³ρ²θ̇ (ZS-F1 \[5\], ZS-U11 \[6\]). At the vacuum the phase-sector stress-energy is

Tμν \= MP² \[ ∂μθ ∂νθ − ½ gμν (∂θ)² \] ,

and with uμ ∝ ∂μθ, n ∝ ρ², the conservation law ∂μTμν \= 0 is the relativistic Euler equation of a perfect (dissipationless) superfluid — the standard Madelung / superfluid correspondence \[12,13\]. Its worked static, curl-free instance is in the corpus: the radial profile θ(r) \= ln(r/r₀)/L gives ρθ ∝ 1/r², the isothermal halo of ZS-A1/A2 and ZS-F1 §4.3 \[3–5\]. The perfect-fluid content is standard physics; the Z-Spin-specific content is what plays the role of dissipation, to which the rest of the paper is devoted. \[DERIVED-interpretation; static instance DERIVED in corpus.\]

**2.1 Equation of state and sound speed**

The Euler system above has a definite equation of state, fixed with no free parameter by the canonical Lagrangian. In the homogeneous time-dependent (‘kination’) regime θ \= θ(t), the stress-energy gives ρ \= p \= ½ MP² θ̇², so the equation-of-state parameter and sound speed are

w \= p/ρ \= 1 ,    cs² \= dp/dρ \= 1   ⇒   cs \= 1   (luminal).

The Z-Goldstone is thus a **stiff fluid** — the maximally stiff causal fluid — with sound speed equal to the speed of light; for any canonical P(X) \= X theory the general formula cs² \= PX/(PX \+ 2X PXX) \[21\] reduces to 1\. In the static, curl-free (halo) regime θ \= θ(r) with θ̇ \= 0 and only ∂rθ ≠ 0, the stress-energy is instead anisotropic:

ρ \= −T t t \= ½ MP²(θ′)² ,    pr \= T r r \= \+ρ ,    pt \= T θ θ \= T φ φ \= −ρ .

This is the global-monopole / texture gradient stress \[22\]: radial pressure equal to the energy density, tangential tension equal to minus it. The angle-averaged equation of state is w̄ \= (pr \+ 2pt)/3ρ \= −1/3, and since θ′ ∝ 1/r the density is ρ ∝ 1/r² — recovering the corpus halo ρθ ∝ 1/r² and identifying its effective equation of state as the coasting / flat-rotation value w̄ \= −1/3 (the borderline between cosmic acceleration and deceleration, and the value that produces asymptotically flat rotation). Thus the same field is a stiff (w \= 1\) fluid when it evolves in time and a w̄ \= −1/3 anisotropic configuration when it is the static halo — both with zero free parameters. \[DERIVED.\]

**2.2 Cosmological placement of the stiff regime**

The two equation-of-state regimes are not abstract: each is a known phase of the corpus cyclic cosmology, and the stiff regime in particular closes a connection that was previously left implicit. Writing the radial amplitude as ε \= |Φ| (the ρ of §2, denoted ε in ZS-U5/M12/A2), the conserved comoving winding charge is Qw \= a³ε²θ̇, which ZS-M12 / ZS-U5 fix at the Z-Telomere onset to Qw \= **A** \= 35/437 \[25,26\]. Eliminating θ̇ \= Qw/(a³ε²), the kinetic (stiff) energy density of the Goldstone is

ρθ \= ½ ε²θ̇² \= Qw² / (2 a⁶ ε²) ∝ a⁻⁶ ,

which is exactly the centrifugal launch term Qw²/(2a⁶ε²) of the ZS-M12 ‘centrifugal launch mechanism’ \[26\]. The stiff w \= 1 regime of §2.1 is therefore the **near-bounce phase** of the ZS-U11 cycle: as a → 0 the conserved winding forces θ̇ ∝ a⁻³ and ρθ ∝ a⁻⁶ to grow fastest, building the barrier ε\_min(bounce) ≈ 30.7 that places the field in the large-field regime required for inflation. The static w̄ \= −1/3 configuration of §2.1 is the complementary late-time phase — the same Goldstone frozen into the halo gradient. \[DERIVED for the energy density; placement DERIVED-interpretation against ZS-M12/U11.\]  
Two honest qualifications. (i) Because w \= 1 (not w \> 1), ρθ ∝ a⁻⁶ scales like the shear anisotropy rather than dominating it, so the Z-Goldstone is marginal for ekpyrotic smoothing \[27\]; the ZS-U11 bounce relies on the topological Auto-Surgery, not on ultra-stiff dilution. (ii) Whether Qw survives the ≈ 3τ\_P dissipative Auto-Surgery is the standing ZS-M12 / ZS-U11 matching question (V1 OPEN, gate F-U11.6). We note — without claiming it — that this ≈ 3τ\_P duration is suggestively close to the ≈ 3-cycle time for the Z-channel to saturate its ln 2 capacity (§4.1); establishing or refuting that coincidence is left OPEN. \[OPEN.\]  
The marginality in (i) can be made quantitative. In a Bianchi-I (anisotropic) background the shear energy density also scales as ρshear \= σ²/16πG ∝ a⁻⁶, identically to ρθ \= Qw²/(2a⁶ε²), so their ratio is a constant fixed by initial data: ρθ/ρshear \= **A**²/(2ε² Cσ). With Qw \= **A**, the Goldstone coefficient is **A**² ≈ 6.4×10⁻³; unless the shear is itself tuned below this, the Goldstone kination is anisotropy-**subdominant** by a factor ∼ **A**²/2 ≈ 0.003 — it is neither catastrophically overwhelmed nor capable of smoothing, but it cannot be the smoothing agent (which would require w \> 1). This is the deterministic complement to the corpus’s thermal-shear constraint τ\_thermal/τ\_AS ≈ 0.81 (ZS-U11, channel P4, with τ\_AS \= 3τ\_P), and reinforces the same conclusion: the bounce smoothing is supplied by the topological Auto-Surgery, not by stiff dilution. \[DERIVED-CONDITIONAL on the shear not being tuned below **A**².\]

**§3. There Is No Thermal Viscosity**

A Navier–Stokes-like extension would need a shear viscosity η and, for the dimensionless ratio η/s, an entropy density s and a temperature T. Two standing corpus results block this. First, the Goldstone **never thermalizes**: at the attractor θ has zero direct coupling to matter (ZS-F1 §7.2 \[5\], gate F-F1.5) — it is a coherent classical field, the same one whose static profile gives ρθ ∝ 1/r², not a thermal gas. Second, the full Z-Spin dynamics is **unitary**, and the entropy seen by X-observers is scrambling/entanglement entropy, not thermal entropy (ZS-F1 §12.1). With no thermal T and no thermal s, the ratio η/s is not the right object: for a pure coherent superfluid the thermal normal component is absent, so a thermal η and s both vanish and η/s is 0/0. The KSS bound η/s ≥ 1/4π \[14\], a theorem about thermal fluids, simply does not apply.  
This is confirmed by a self-consistency test (detailed in Appendix C): every attempt to assign a viscosity value is unstable. Reading the Goldstone drag as a hydrodynamic mode-damping gives a small ν \~ A², whose implied η/s ≈ 4×10⁻⁴ lies \~200× below the KSS bound — unphysical for any thermal fluid; reading it as a microscopic relaxation rate gives a large ν \~ 1/A²; and the candidate temperatures (a cyclic-period value and a vortex-core value) differ by \~2×, so no η/s value is parameter-free. An estimate that flips sign and magnitude with each re-derivation, while a required input (T) cannot be uniquely fixed, is the signature that the **imported framework is wrong** — here, that thermal hydrodynamics does not match the corpus’s unitary, non-thermalizing ontology. The instability is therefore informative, not a defect to be patched.

**Lemma M43.1 (No-Thermal-Transport).** Let a system evolve under a one-parameter unitary group U(t) \= e−iHt (global unitarity), and suppose it does not thermalize: there is no inverse temperature β and Gibbs state ρβ \= e−βH/Z to which reduced observables relax (e.g. a conserved coherent mode with no relaxation channel, as for θ in ZS-F1 §7.2). Then: (a) the Kubo shear viscosity η \= limω→0 ω⁻¹ Im GR(ω, 0), defined through the KMS (thermal) stress-tensor correlator, has no thermal state in which to be evaluated; (b) the thermal entropy density s \= (ρ \+ p)/T is undefined, there being no T; (c) in the pure-coherent (two-fluid T → 0\) limit the normal component that carries η and s vanishes, so η → 0 and s → 0 and the ratio η/s is the indeterminate form 0/0. Hence the KSS bound η/s ≥ 1/4π, a theorem about thermal fluids, constrains nothing here. The sole well-defined irreversibility is the entanglement-entropy production of a traced subsystem (§4.1), which is information-theoretic, not thermodynamic. \[DERIVED — a careful application of the definitions (Kubo needs KMS; thermal s needs T) to the corpus’s unitarity and non-thermalization; not a new theorem.\]

**Remark (two-fluid limit).** Part (c) is sharp in Landau’s two-fluid description \[28\]: the shear viscosity and the entropy reside entirely in the normal component of density ρn(T) — η ∼ ρn⟨v⟩ℓ and s ∝ ρn — while the superfluid component ρs carries neither. As T → 0 the thermal quasiparticles vanish, ρn(T) → 0, so η → 0 and s → 0 together. The Z-Goldstone, a non-thermalizing coherent condensate, sits at ρn ≡ 0 (a T \= 0 state), so η \= s \= 0 identically and η/s \= 0/0. The KSS bound concerns the universal T → 0 limit of strongly-coupled, normal-component-dominated plasmas; with no normal component, the Z-Goldstone lies outside its domain entirely. \[DERIVED.\]

**§4. The Correct Dissipation: Z-Spin Scrambling**

What physically dissipates in the Z-sector — the ‘leak’ an X-observer perceives — is unitary scrambling, and it is parameter-free. The i-tetration map f(z) \= i^z has the attracting fixed point z\* \= 0.4383 \+ 0.3606i with multiplier λ \= (iπ/2)z\* \= −0.5664 \+ 0.6886i, |λ| \= 0.8916 (ZS-M1 \[8\], PROVEN). Two PROVEN facts make it a scrambler rather than a simple sink:  
**(i) Quasi-periodic rotation.** Because the real matrix M\_f forces |λ| \= |λ̄|, no single ray is selected: the trajectory rotates by arg λ ≈ 129.4° per step within the 2-dimensional Z subspace (ZS-M1; ZS-F0 V35). This is the mechanism that, for X-observers, implements scrambling (ZS-F1 §12.1).  
**(ii) The Wilson-loop leak.** The holonomy around one X→Z→Y→Z→X cycle is |λ²| \= (π²/4)·η\_topo ≈ 0.795 (ZS-M1 Remark 1.2, PROVEN); the per-cycle leak is 1−|λ²| ≈ 0.205, equivalently a per-cycle entropy-production rate −ln|λ²| ≈ 0.229. A closed loop (|λ²| \= 1\) would be non-scrambling and marginally stable; the leak is precisely what scrambles.  
Coarse-grained for an X-observer, this unitary scrambling is the Pauli/Lindblad master equation of ZS-Q7 \[7\], with the inter-sector rates

λfast \= −**A** ,    λslow \= −2**A**/Q ,    γxz \= 2**A**/Q ,    γzy \= 6**A**/Q   (ZS-Q7, ZS-F0; PROVEN/DERIVED).

These are A-scaled and contain no free parameter. The decoherence time τ\_fast \= 1/**A** ≈ 12.49 coincides with the Z-bottleneck relaxation of ZS-F0 and the decoherence ratio τ\_D/τ\_Penrose of ZS-Q1. The scrambling, not a thermal viscosity, is the genuine Z-sector ‘dissipation’; it is information-theoretic and unitary at the fundamental level, dissipative only in the reduced X-description. \[DERIVED/PROVEN.\]

**4.1 The dynamical character: scrambling without chaos**

Precision about the dynamical type is essential, because it bounds what may be claimed. The i-tetration fixed point is **attracting**: |λ| \= 0.8916 \< 1, so ln|λ| \= −0.115 \< 0\. By Pesin’s identity the Kolmogorov–Sinai entropy equals the sum of the positive Lyapunov exponents \[23\], and an attracting fixed point has none — so the map’s KS entropy is zero and there is **no positive quantum Lyapunov exponent** λ\_L. The system is therefore not chaotic in the dynamical-systems sense. ‘Scrambling’ here means unitary information delocalization, not chaotic-flow mixing: per X→Z→Y→Z→X cycle a fraction 1−|λ²| ≈ 0.205 of the information leaks to the traced-out Z/Y sectors, giving the reduced X-observer an entropy growth −ln|λ²| ≈ 0.229 per cycle — equivalently the CPTP master equation above. Two consequences follow. (i) The decoherence/scrambling time is a **fixed constant**, τ\_fast \= 1/A ≈ 12.49 (or ≈ 1/(−ln|λ²|) ≈ 4.4 Wilson cycles), independent of the system size S. (ii) The well-posed, parameter-free ‘irreversibility’ of the Z-sector is therefore not a transport coefficient η but the X-observer **entropy-production rate** Ṡ\_X ≈ (−ln|λ²|)/T\_cycle — the Page-curve growth of ZS-F1 §12.1 — an information-theoretic quantity that is the correct replacement for the ill-posed η/s of §3. \[DERIVED.\]

**Proposition M43.2 (cross-validation of Ṡ\_X).** The rate Ṡ\_X is consistent with two independent corpus quantities. (i) Exactly: per cycle, Ṡ\_X·T\_cycle \= −ln|λ²| \= 2(−ln|λ|) \= 0.2294, while the ZS-F16 Wilson-loop dissipation gives Γ\_Z·T\_cycle ≈ 0.1149; since −ln|λ| \= 0.1147, these agree to 0.16% — as they must, both being the same |λ²| \= 0.7948 Wilson loop, the factor 2 being the amplitude-to-probability relation. (ii) Approximately: the coarse-grained Markovian leak γ\_xz·τ\_fast \= (2**A**/Q)(1/**A**) \= 2/Q ≈ 0.182 reproduces the exact per-cycle linear leak 1−|λ²| ≈ 0.205 to \~11%, the residual being the expected Markovian-approximation error (the rate misses the arg λ ≈ 129.4° rotation). (iii) Bounded: the accumulated X-entropy saturates at the Z-channel capacity ≤ ln 2 (ZS-Q7) after ≈ ln 2 / (−ln|λ²|) ≈ 3.0 cycles. Thus Ṡ\_X is fixed (zero free parameters), cross-checked against ZS-F16 exactly and ZS-Q7 within the Markovian error, and capacity-bounded. \[DERIVED; cross-checks consistent.\]

**§5. Scrambling Quantified: OTOC and the Butterfly Velocity**

Scrambling is measured by the out-of-time-order correlator (OTOC) \[15\], C(t) \= ⟨\[W(t), V\]†\[W(t), V\]⟩, whose growth defines a rate and a spatial spreading speed, the butterfly velocity vB \[16,17\]. Two Z-Spin statements follow without new assumptions. The spreading speed is bounded by the Lieb–Robinson velocity of the Z-Spin lattice,

vB ≤ vLR \= ρ(ℒ)·a   (ZS-M17 \[2\], ≤-form per the 2026-06-07 erratum),

and generically the inequality is strict (the butterfly/operator-growth velocity is typically below the Lieb–Robinson velocity), consistent with the erratum’s downgrade of the M17.2 tightness claim. The per-cycle scrambling rate is the leak −ln|λ²| ≈ 0.229 of §4.  
One boundary must be respected. The Maldacena–Shenker–Stanford chaos bound λL ≤ 2πkBT/ℏ \[18\] is a *thermal* bound; since the Z-Goldstone has no thermal temperature (§3), it does not apply here — exactly the inapplicability that retires η/s and the KSS bound. The scrambling is therefore characterized by its unitary, parameter-free leak and its sub-Lieb–Robinson light-cone, not by a thermal Lyapunov bound. \[DERIVED-interpretation; external OTOC/butterfly framework IMPORTED.\]  
The non-chaotic character of §4.1 sharpens what the OTOC framework does and does not give. The butterfly **velocity** — the operator-spreading speed — is well-defined and bounded by v\_B ≤ ρ(ℒ)·a irrespective of chaos, because that bound is a Lieb–Robinson statement. But the exponential OTOC **growth** e^{λ\_L t} that marks a chaotic fast scrambler is absent here, since λ\_L \= 0 (KS \= 0). In particular the fast-scrambling relation t\* \~ (1/λ\_L) ln S \[24\] does **not** apply: the Z-sector is not a black-hole-like fast scrambler but a fixed-rate decoherer, with a size-independent scrambling time set by 1/A (§4.1). This is the OTOC counterpart of the MSS-bound inapplicability — both the chaos bound and the logarithmic fast-scrambling time presuppose the chaotic, thermal dynamics the Z-Goldstone does not have. \[DERIVED.\]

**§6. The Geometric Model: Anosov Mixing, the Selberg Bridge, and the s \= 1/2 Confluence**

The scrambling has a natural geometric model, supplied by ZS-M4 \[9\]. Theorem 3 of ZS-M4 (PROVEN) identifies the Berry–Keating dilation rapidity with an i-tetration quantity,

αBK \= ln(dilation) \= −ln|z\*| \= y\*·π/2 \= 0.566417   (y\* \= Im z\* \= 0.36059; locking L3: |z\*|² \= e^{−y\*π}).

The Berry–Keating xp Hamiltonian generates a hyperbolic (dilation) flow, and the Selberg trace formula \[19\] relates the Laplacian spectrum of a hyperbolic surface to the lengths of its closed geodesics — the periodic orbits of the **Anosov geodesic flow**, whose hallmark is exponential mixing (scrambling). The Z-sector scrambling and the geodesic-flow mixing are thus the same kind of dynamics, which is the defensible content of the i-tetration ↔ hyperbolic-flow correspondence. Two caveats keep this precise: the i-tetration fixed point is an *attractor* (|λ| \< 1), not an Anosov saddle, so the correspondence is through mixing/scrambling, not through an equality of Lyapunov exponents; and αBK \= 0.5664 is a Z-Spin-specific dilation rate, not the curvature−–1 geodesic exponent (= 1). \[DERIVED-interpretation for the mixing correspondence; the literal exponent identification is OPEN.\]

**6.1 The s \= 1/2 confluence**

The same Selberg bridge connects the scrambling to a number-theoretic structure. ZS-M4 Theorem 4 (PROVEN) shows the seam-involution mirror-adjointness JLs†J \= L1−s holds iff σ \= 1/2, marking the critical line as the unique unitarity line of the transfer operator. Independently, Anantharaman and Monk proved in 2025 \[10,11\] that typical (Weil–Petersson random) hyperbolic surfaces of large genus attain the optimal spectral gap λ₁ → 1/4, where 1/4 \= s(1−s) at s \= 1/2 is the bottom of the L²-spectrum of ℍ² and the tempered (unitary, principal-series) threshold. Both single out the same s \= 1/2 fixed line of the same s ↔ 1−s functional-equation symmetry: ZS-M4’s ‘σ \= 1/2 is the unique unitarity line’ is the operator mirror of ‘typical hyperbolic surfaces are maximally tempered.’ \[HYPOTHESIS-strong.\]

**6.2 Can the confluence be lifted to a theorem? (Test of gate F-PN.1)**

A DERIVED status would require an actual operator map from ZS-M4’s Ls to a Selberg/hyperbolic-Laplacian operator. We tested whether such a map exists in the Pmax → ∞ limit. The phase matrices W\_p are diagonal, so Ls is a diagonal operator on a **fixed** ℂ¹¹; its eigenvalues are eleven prime-phase Dirichlet sums (the j \= 5 entry being the prime zeta function). A Selberg/Laplacian operator is, by contrast, infinite-dimensional with a continuous-plus-discrete spectrum and heat-kernel structure. At fixed Q \= 11 the map is therefore categorically impossible (finite versus infinite dimension); and the infinite-dimensional (Fock/trace-class, Q → ∞) extension is exactly the construction ZS-M4 itself flags as conjectural and unbuilt (its O1, O3, and Gap 1 / P1–P4). The lift is thus blocked at the same gap that blocks ZS-M4’s Riemann connection. Gate F-PN.1 does not fully fire — impossibility at Q → ∞ is not shown, only non-construction — but the conclusion is firm: the confluence cannot presently be raised above HYPOTHESIS-strong. It is not, however, ‘merely numerical’: what the two results share is the s ↔ 1−s symmetry and its tempered fixed line, which is operator-independent, so the structural status is genuine. \[Lift route: OPEN; confluence: HYPOTHESIS-strong.\]

**Lemma M43.3 (No-Operator-Map at fixed Q).** The fixed-Q transfer operator Ls, being diagonal on ℂQ with Q \= 11, has a spectrum of at most Q \= 11 points. The Laplacian −Δ on a closed hyperbolic surface of genus g has area 4π(g−1) (Gauss–Bonnet) and, by the Weyl law, an eigenvalue counting function N(λ) ∼ (g−1)λ → ∞ — an infinite discrete spectrum (with, for finite-volume cusped surfaces, an additional continuous part on \[1/4, ∞)). A similarity or unitary equivalence preserves the cardinality of the spectrum, and no map can take an at-most-11-point spectrum to an infinite one. Hence at fixed Q no correspondence Ls → (hyperbolic Laplacian / Selberg operator) exists — a dimension/cardinality obstruction, independent of the detailed entries. It is removed only by Q → ∞ (an inductive-limit / Fock construction), which is exactly ZS-M4’s conjectural and unbuilt O1/O3/Gap 1\. This is the rigorous form of the F-PN.1 verdict. \[PROVEN at fixed Q; OPEN at Q → ∞.\]

**Anti-numerology declarations.** Two numerical near-coincidences are explicitly declined. (i) The recurring ‘1/2’ — j \= 1/2 (spin invariant, ZS-M3), σ \= 1/2 (critical line), s \= 1/2 — is claimed as one structural object ONLY for σ \= 1/2 ↔ s \= 1/2; j \= 1/2 has a distinct origin and is not asserted to be the same. (ii) Embedding α\_BK as a curvature scale gives a base-of-spectrum |z\*|²/4 ≈ 0.0805 (and α\_BK²/4 ≈ 0.0802) numerically near A \= 0.0801; this 0.1–0.5% agreement has no derivation and is NOT claimed.

**§7. Falsification Gates and Non-Claims**

Table 7.1. Falsification gates for ZS-M43.

| Gate | Trigger condition |
| ----- | ----- |
| **F-M43.1** | If a future construction shows the Z-Goldstone does reach a thermal state with a well-defined temperature and thermal entropy, the §3 retirement of η/s is wrong and a thermal hydrodynamics must be built after all. |
| **F-M43.2** | If the Goldstone-phase Euler does not reduce to the corpus ρ\_θ ∝ 1/r² in the static curl-free limit, §2 is inconsistent with ZS-A1/A2/F1. (Not triggered.) |
| **F-M43.3** | If the scrambling light-cone is measured (or derived) to exceed the Lieb–Robinson velocity, v\_B ≤ ρ(ℒ)·a fails and §5 is wrong (cross-link to ZS-M17 gate F-M17.5, hardware 2027+). |
| **F-M43.4** | If the i-tetration leak |λ²| ≈ 0.795 or the master-equation rates 2A/Q, 6A/Q were shown not to govern X-observer decoherence, the scrambling identification of §4 fails. |
| **F-M43.5** | If an operator map L\_s → Selberg/Laplacian were constructed at P\_max → ∞, the s \= 1/2 confluence would be promoted to DERIVED (a promotion gate, not a refutation). |

**Non-Claims**

**NC-M43.1.** No derivation of the Navier–Stokes equations is claimed; Route B yields a coherent Euler/superfluid plus a scrambling structure, not a thermal Navier–Stokes.  
**NC-M43.2.** No thermal transport coefficient, no thermal entropy density, and no η/s value is claimed; these are declared inapplicable, not merely unknown.  
**NC-M43.3.** The Euler limit and the OTOC/butterfly framework are standard physics; the Z-Spin-specific content is the parameter-free scrambling structure (|λ²| leak; 2A/Q, 6A/Q) and its v\_B ≤ ρ(ℒ)·a bound.  
**NC-M43.4.** The s \= 1/2 confluence is a structural correspondence, NOT an operator identity and NOT a Riemann-Hypothesis claim; ZS-M4’s own non-claims stand.

**§8. Conclusion**

Route B of ZS-M42 is resolved. The Z-Goldstone is a coherent Euler/superfluid field with the corpus halo ρ\_θ ∝ 1/r² as its static instance, and it has no thermal viscosity: η/s and the KSS bound are inapplicable because the Goldstone never thermalizes and the dynamics is unitary. The dissipation that does exist is unitary scrambling, a parameter-free structure governed by the i-tetration leak 1−|λ²| ≈ 0.205 per cycle and the master-equation rates λ\_fast \= −A, γ\_xz \= 2A/Q, γ\_zy \= 6A/Q, propagating at a butterfly velocity v\_B ≤ ρ(ℒ)·a. Its geometric model is Anosov geodesic mixing; via the Selberg bridge it meets ZS-M4’s critical line at the s \= 1/2 ↔ λ \= 1/4 confluence, which a direct operator map cannot presently raise above HYPOTHESIS-strong. The methodological lesson is general for the corpus: when an estimate in a Z-Spin sector is unstable under re-derivation, the productive move is to ask whether the imported framework (here thermal hydrodynamics) matches the corpus ontology (here unitary scrambling), rather than to refine a coefficient.

**Acknowledgements & Code Availability**

This paper consolidates the June 2026 ZS-M42 Route-B program, including the dependency audit against the ZS-M17 dated-erratum (2026-06-07). The numerical checks (the viscosity-instability and temperature comparisons of Appendix C, the |λ²| leak, and the structure of the ZS-M4 transfer operator) are elementary and reproducible from the locked constants A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6), the i-tetration fixed point z\* (ZS-M1), and ξ ≈ 0.75 ℓ\_P (ZS-Q5); a short verification script is available on request.

**Appendix A. Structural-Consistency Checklist (22/22 PASS)**

Table A.1. Structural-consistency checks for ZS-M43 v1.4.

| \# | Check | Verdict |
| ----- | ----- | :---: |
| **C1** | Zero new free parameters; no scale beyond A, Q, dim(Z) \= 2, z\*, ξ, τ\_P. | **PASS** |
| **C2** | Goldstone θ massless, Q \= a³ρ²θ̇ conserved (ZS-F1 / ZS-U11). | **PASS** |
| **C3** | Relativistic Euler from T\_μν conservation — standard superfluid hydro (NC-M43.3). | **PASS** |
| **C4** | Static curl-free limit matches corpus ρ\_θ ∝ 1/r² (ZS-A1/A2/F1). | **PASS** |
| **C5** | θ never thermalizes (ZS-F1 §7.2); dynamics unitary, entropy \= scrambling (§12.1). | **PASS** |
| **C6** | Hence thermal T, s, η/s, and the KSS bound are inapplicable (§3; Appendix C instability). | **PASS** |
| **C7** | Scrambling rotation arg λ ≈ 129.4°/step and leak |λ²| ≈ 0.795 cited from ZS-M1 (PROVEN). | **PASS** |
| **C8** | Coarse-grained rates λ\_fast \= −A, γ\_xz \= 2A/Q, γ\_zy \= 6A/Q from ZS-Q7/F0 (PROVEN/DERIVED). | **PASS** |
| **C9** | Butterfly velocity v\_B ≤ v\_LR \= ρ(ℒ)·a (ZS-M17, ≤-form per erratum); generically strict. | **PASS** |
| **C10** | MSS chaos bound and KSS bound correctly noted inapplicable (non-thermal) — no thermal-bound overreach. | **PASS** |
| **C11** | α\_BK \= −ln|z\*| \= 0.5664 cited from ZS-M4 Theorem 3 (PROVEN); i-tetration is an attractor, not Anosov. | **PASS** |
| **C12** | s \= 1/2 ↔ λ \= 1/4 confluence: same s ↔ 1−s symmetry; HYPOTHESIS-strong, not numerical. | **PASS** |
| **C13** | F-PN.1 tested: L\_s diagonal on fixed ℂ¹¹; map to Laplacian impossible at fixed Q, OPEN at Q→∞. | **PASS** |
| **C14** | Anti-numerology: |z\*|²/4 ≈ 0.0805 ≈ A and the recurring 1/2 are declined, not claimed (§6.2). | **PASS** |
| **C15** | EOS/sound speed (§2.1): kination w \= 1, c\_s \= 1 (stiff/luminal); static halo p\_r \= ρ, p\_t \= −ρ, w̄ \= −1/3, ρ ∝ 1/r² — matches corpus. | **PASS** |
| **C16** | Dynamical character (§4.1): KS \= 0 (attracting, non-chaotic, λ\_L \= 0); fixed-rate decoherence 1/A; t\_\* \~ ln S explicitly inapplicable (§5). | **PASS** |
| **C17** | Lemma M43.1 (§3): unitary \+ non-thermalizing ⇒ Kubo η and thermal s undefined; η/s \= 0/0 (T→0 normal component); KSS vacuous. DERIVED. | **PASS** |
| **C18** | Prop. M43.2 (§4.1): Ṡ\_X·T\_cycle \= \-ln|λ²| \= 2(Γ\_Z·T\_cycle)\_{F16} (0.16%); Markovian 2/Q vs 0.205 (\~11%); ≤ ln2 (Q7). Consistent. | **PASS** |
| **C19** | §2.2: kination ρ\_θ \= Q\_w²/(2a⁶ε²) ∝ a⁻⁶ \= ZS-M12 centrifugal term, Q\_w \= A; near-bounce phase; w=1 anisotropy-marginal \+ Q-survival OPEN (honest). | **PASS** |
| **C20** | Remark to Lemma M43.1 (§3): two-fluid η ∝ ρ\_n, s ∝ ρ\_n; T=0 condensate ρ\_n≡0 ⇒ η=s=0 ⇒ 0/0; KSS (finite-T, normal-dominated) out of domain. Landau \[28\]. | **PASS** |
| **C21** | §2.2 (quantified): ρ\_θ/ρ\_shear \= A²/(2ε²C\_σ) const (both ∝a⁻⁶); A²≈6.4e-3 ⇒ anisotropy-subdominant; complements thermal τ\_thermal/τ\_AS≈0.81; Auto-Surgery necessary. | **PASS** |
| **C22** | Lemma M43.3 (§6.2): fixed-Q diagonal L\_s has ≤11-pt spectrum; hyperbolic Δ infinite (Weyl) \+ cont \[1/4,∞); cardinality obstruction ⇒ no map. PROVEN at fixed Q; OPEN at Q→∞. | **PASS** |

**Appendix B. Cross-Paper Dependency and Version-Conflict Audit**

All imported corpus results are used as stated; none is modified, and the constants A, Q, dim(Z) \= 2 are used identically throughout. No version conflict.

Table B.1. Upstream dependencies and status.

| Source | Result used | Status / conflict check |
| ----- | ----- | ----- |
| **ZS-M42 v1.2** | Two-Gate No-Go; Route B mandate | Consistent (this paper closes Route B) |
| **ZS-M17 (erratum 2026-06-07)** | v\_max ≤ ρ(ℒ)·a (≤-form) | Consistent; ≤ used for v\_B bound, not the retracted equality |
| **ZS-F1 §7.2 / §12.1** | θ non-thermalizing; unitary scrambling | Load-bearing (§3, §4); used as stated |
| **ZS-A1 / A2 / F1** | ρ\_θ ∝ 1/r² (DERIVED) | Static instance (§2) |
| **ZS-M1** | z\*, |λ| \= 0.8916, |λ²| ≈ 0.795 (PROVEN) | Scrambling rotation/leak (§4) |
| **ZS-Q7 / ZS-F0** | λ\_fast \= −A, γ\_xz \= 2A/Q, γ\_zy \= 6A/Q | Coarse-grained rates (§4) |
| **ZS-M4 (Thms 3, 4\)** | α\_BK \= −ln|z\*|; J-mirror iff σ \= 1/2 | Geometric model and confluence (§6) |
| **KSS 2005; MSS 2016** | η/s ≥ 1/4π; λ\_L ≤ 2πT (external) | Used as physicality filters; shown inapplicable (non-thermal) |
| **Anantharaman–Monk 2025** | λ₁ → 1/4 optimal gap (external) | Geometric anchor of the confluence (§6.1) |

**Appendix C. The Viscosity Instability, for the Record**

This appendix documents the dead-end that §3 summarizes, so that it is not re-attempted. If one nonetheless treats the Goldstone drag (O(A²/MP²) per oscillation, ZS-U11 NC-U11.1 \[6\]) as a transport input and writes η/s \= τ\_R·T (with η \= (ρ+p)τ\_R, s \= (ρ+p)/T at μ \= 0), the result depends entirely on two unfixed choices, as Table C.1 shows.

Table C.1. The two instabilities that signal a wrong framework.

| Choice | Outcome | Verdict |
| ----- | ----- | :---: |
| **Drag as mode-damping → ν \~ A²ξ² ≈ 0.0036 ℓ\_P** | η/s ≈ 4×10⁻⁴ ≪ 1/4π | **KSS-violating → unphysical** |
| **Drag as relaxation rate → ν \~ τ\_P/A² ≈ 156 ℓ\_P** | η/s \~ O(10–10²) | **Opposite scaling; no unique value** |
| **Temperature: cyclic vs core** | T ≈ 0.11–0.36 vs 0.21 M\_P (×\~2–3) | **Not unique → η/s not parameter-free** |

The sign of the A-exponent is undetermined and the temperature is non-unique; by the convergence test of the deep-exploration protocol, this instability is the diagnostic that the thermal-fluid framework does not fit, which §3–§4 act on. The KSS bound is used here only as a physicality filter; it is not a claim about the Z-fluid.

**References**

\[1\] K. Kang, “The Z-Bottleneck Locality Criterion for Hydrodynamic Derivability,” ZS-M42 v1.2 (Z-Spin Cosmology Collaboration, June 2026).

\[2\] K. Kang, “Continuum Limit and Osterwalder–Schrader Reconstruction of Z-Spin Lattice Dynamics,” ZS-M17 v1.0 (Z-Spin Cosmology Collaboration, April 2026); dated update 2026-06-07.

\[3\] K. Kang, “Galactic Dynamics & Morphology (ε-Halo),” ZS-A1 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[4\] K. Kang, “Dark Sector Assignment of the Goldstone Modes,” ZS-A2 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[5\] K. Kang, “The Z-Spin Action, U(1)\_Z Completion, and the Goldstone Mode θ,” ZS-F1 v1.0 §4, §7.2, §12.1 (Z-Spin Cosmology Collaboration, 2026).

\[6\] K. Kang, “Cyclic Cosmology and Auto-Surgery: Angular–Radial Mode Separation,” ZS-U11 v1.0, NC-U11.1 (Z-Spin Cosmology Collaboration, 2026).

\[7\] K. Kang, “The Z-Bottleneck: L\_XY ≡ 0, Channel Capacity ≤ ln 2, and the Pauli Master Equation,” ZS-Q7 (Z-Spin Cosmology Collaboration, 2026).

\[8\] K. Kang, “i-Tetration, the Fixed Point z\*, and the Leaky Wilson Loop,” ZS-M1 v1.0, Remark 1.2 (Z-Spin Cosmology Collaboration, 2026).

\[9\] K. Kang, “A Q \= 11 Transfer Operator with Z₂ Seam Involution: a Berry–Keating Bridge to the Critical Line,” ZS-M4 v1.0 (Z-Spin Cosmology Collaboration, 2026); dated update 2026-04-15.

\[10\] N. Anantharaman and L. Monk, “Friedman–Ramanujan functions in random hyperbolic geometry and application to spectral gaps II,” arXiv:2502.12268 (2025).

\[11\] N. Anantharaman and L. Monk, “Spectral gap of random hyperbolic surfaces,” arXiv:2403.12576 (2024); arXiv:2304.02678 (2023).

\[12\] E. Madelung, “Quantentheorie in hydrodynamischer Form,” Z. Phys. 40, 322 (1927).

\[13\] D. T. Son and M. Wingate, “General coordinate invariance and conformal invariance in nonrelativistic physics,” Ann. Phys. 321, 197 (2006).

\[14\] P. K. Kovtun, D. T. Son, and A. O. Starinets, “Viscosity in strongly interacting quantum field theories from black hole physics,” Phys. Rev. Lett. 94, 111601 (2005).

\[15\] A. I. Larkin and Y. N. Ovchinnikov, “Quasiclassical method in the theory of superconductivity,” Sov. Phys. JETP 28, 1200 (1969).

\[16\] S. H. Shenker and D. Stanford, “Black holes and the butterfly effect,” JHEP 03, 067 (2014).

\[17\] D. A. Roberts and B. Swingle, “Lieb–Robinson bound and the butterfly effect in quantum field theories,” Phys. Rev. Lett. 117, 091602 (2016).

\[18\] J. Maldacena, S. H. Shenker, and D. Stanford, “A bound on chaos,” JHEP 08, 106 (2016).

\[19\] A. Selberg, “Harmonic analysis and discontinuous groups…,” J. Indian Math. Soc. 20, 47 (1956).

\[20\] R. Kubo, “Statistical-mechanical theory of irreversible processes. I,” J. Phys. Soc. Jpn. 12, 570 (1957).

\[21\] J. Garriga and V. F. Mukhanov, “Perturbations in k-inflation,” Phys. Lett. B 458, 219 (1999).

\[22\] M. Barriola and A. Vilenkin, “Gravitational field of a global monopole,” Phys. Rev. Lett. 63, 341 (1989).

\[23\] Ya. B. Pesin, “Characteristic Lyapunov exponents and smooth ergodic theory,” Russ. Math. Surveys 32(4), 55 (1977).

\[24\] Y. Sekino and L. Susskind, “Fast scramblers,” JHEP 10, 065 (2008).

\[25\] K. Kang, “Two Z-Sector Wilson-Loop Protocols and the Effective Dissipation Γ\_Z·T\_cycle,” ZS-F16 v1.0 (Z-Spin Cosmology Collaboration, 2026).

\[26\] K. Kang, “The Centrifugal Launch Mechanism: Comoving Winding Q \= a³ε²θ̇ \= A and Large-Field Initial Conditions,” ZS-M12 v1.0 (Z-Spin Cosmology Collaboration, 2026); see also ZS-U5, ZS-U11.

\[27\] J. Khoury, B. A. Ovrut, P. J. Steinhardt, and N. Turok, “Ekpyrotic universe: colliding branes and the origin of the hot big bang,” Phys. Rev. D 64, 123522 (2001).

\[28\] L. D. Landau, “The theory of superfluidity of helium II,” J. Phys. USSR 5, 71 (1941).

\[29\] H. Weyl, “Über die asymptotische Verteilung der Eigenwerte,” Nachr. Königl. Ges. Wiss. Göttingen, 110 (1911).

**Version History**

v1.4 (June 2026): Second-layer deepening of the same three sections (no new fragment). The three v1.3 claims are tightened with rigorous limiting arguments. (§3) A two-fluid Remark makes Lemma M43.1(c) sharp: η and s both reside in the Landau normal component ρ\_n(T), which vanishes as T → 0; the non-thermalizing condensate sits at ρ\_n ≡ 0, so η \= s \= 0 and η/s \= 0/0, and the KSS bound (a normal-component-dominated, finite-T statement) is out of domain. (§2.2) The w \= 1 anisotropy-marginality is quantified: ρ\_θ and the Bianchi shear both ∝ a⁻⁶, so their ratio is a constant ∝ A² ≈ 6.4×10⁻³, making the Goldstone anisotropy-subdominant — the deterministic complement to the corpus thermal-shear constraint τ\_thermal/τ\_AS ≈ 0.81 — so the topological Auto-Surgery, not stiff dilution, must smooth the bounce. (§6.2) Lemma M43.3 (No-Operator-Map) gives the rigorous form of F-PN.1: the fixed-Q diagonal L\_s has an at-most-11-point spectrum while the hyperbolic Laplacian has an infinite (Weyl) spectrum, a cardinality obstruction that no similarity can bridge; the lift is OPEN only at Q → ∞. Structural checks 19 → 22; references \+2 (\[28–29\]). Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged.  
v1.3 (June 2026): Internal-density deepening (no new fragment). Three previously-prose points are made into formal, cross-validated claims. (§3) Lemma M43.1 (No-Thermal-Transport) states that global unitarity plus non-thermalization make the Kubo η and the thermal entropy density undefined, so η/s is the indeterminate 0/0 in the pure-coherent (T→0) limit and the KSS bound is vacuous. (§4.1) Proposition M43.2 cross-validates the X-observer entropy-production rate Ṡ\_X three ways: exactly against the ZS-F16 Wilson dissipation (Ṡ\_X·T\_cycle \= −ln|λ²| \= 2·Γ\_Z·T\_cycle, 0.16%), approximately against the ZS-Q7 Markovian rates (2/Q vs 1−|λ²|, \~11% expected error), and as bounded by the Z-channel capacity ln 2\. (§2.2) The stiff w \= 1 regime is identified with the ZS-M12 centrifugal-launch term ρ\_θ \= Q\_w²/(2a⁶ε²) ∝ a⁻⁶ with comoving winding Q\_w \= A, placing it at the near-bounce phase of the ZS-U11 cycle; the w \= 1 anisotropy-marginality and the Q-survival through the ≈3τ\_P Auto-Surgery are flagged OPEN. Structural checks 16 → 19; references \+3 (\[25–27\]). Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged.  
v1.2 (June 2026): Mathematical-density deepening of the existing sections (no new fragment, no new scope). §2.1 adds the equation of state and sound speed, derived with zero free parameters — a stiff fluid (w \= 1, c\_s \= 1\) in the time-dependent regime and an anisotropic global-monopole configuration (p\_r \= ρ, p\_t \= −ρ, w̄ \= −1/3, ρ ∝ 1/r²) in the static-halo regime, matching the corpus halo. §4.1 pins the dynamical character of the scrambling: the i-tetration fixed point is attracting, so by Pesin’s identity the Kolmogorov–Sinai entropy is zero, there is no positive quantum Lyapunov exponent, and the scrambling is unitary information delocalization (CPTP) with a fixed, size-independent decoherence time 1/A; the correct replacement for η/s is the X-observer entropy-production rate. §5 is sharpened accordingly: the OTOC framework gives a bounded butterfly velocity but no exponential growth, and the fast-scrambling time t\_\* \~ ln S is shown explicitly NOT to apply (the Z-sector is a fixed-rate decoherer, not a black-hole-like fast scrambler) — the OTOC counterpart of the MSS-bound inapplicability. Structural checks 14 → 16, all PASS; references \+4 (\[21–24\]). Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged.  
v1.1 (June 2026): Full revision. The paper is reorganized around its constructive result — the Z-sector dissipation is unitary scrambling — with the thermal-η/s retirement reduced to its essential argument (§3) and the unstable viscosity estimate moved to Appendix C as a documented dead-end. New material folded in: §4–§5 elevate scrambling to a first-class subject (i-tetration |λ²| leak; ZS-Q7 master-equation rates; OTOC and the butterfly velocity v\_B ≤ ρ(ℒ)·a; the non-applicability of the MSS chaos bound), and §6 gives the Anosov / Selberg geometric model together with the s \= 1/2 ↔ λ \= 1/4 confluence and a test of gate F-PN.1 (the operator map L\_s → Selberg/Laplacian is blocked, so the confluence stays HYPOTHESIS-strong). The standalone position note PN-M4.1 is superseded by §6. Structural checks 12 → 14, all PASS. Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) unchanged.  
v1.0 (June 2026): First public release. Established the coherent Euler/superfluid result and the retirement of the thermal η/s programme. (Consolidated from internal Z-Spin Collaboration deep-exploration notes up to v0.4, June 2026.)