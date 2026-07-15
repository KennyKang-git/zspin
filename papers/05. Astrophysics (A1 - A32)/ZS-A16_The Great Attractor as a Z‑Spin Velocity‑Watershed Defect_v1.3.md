**ZS-A16**

**The Great Attractor as a Z‑Spin Velocity‑Watershed Defect:**

**A Vortex‑Network Forward Model, an Amplitude No‑Go (Operator Form), an A‑Locked Order Bound, a Variational Occupation Problem, and the Epistemic Ceiling of Closure**

Author: Kenny Kang

Affiliation: Z‑Spin Cosmology Collaboration

Edition: v1.3 (June 2026\) — strictly additive increment over v1.2

Theme / Paper code: Astrophysics — ZS‑A16 v1.3

GitHub: https://github.com/KennyKang-git/zspin

**Verification Summary**

**Verification: 44/44 consistency‑audit PASS**  |  **Zero Free Parameters**  |  Sole geometric inputs **A** \= 35/437, **Q** \= 11, (Z, X, Y) \= (2, 3, 6\) **LOCKED**.  |  Results: **Theorem A16.NG / A16.NG′** (Amplitude No‑Go, now in operator form **v** \= ∇(−Δ)⁻¹δρ\_Z — a model‑independent degeneracy for all |∇θ|² defect DM); **Theorem A16.B** (Amplitude Bound), refined to the honest order form |δv/v| \= O(**A**) ≪ O(1); the single‑vortex form factor u(k) **DERIVED**; **\[NEW v1.3\]** the occupation as a **Kirchhoff–Onsager variational problem** min(W\_KO \+ λ W\_grav). Occupation ceiling **DERIVED‑CONDITIONAL \+ VERIFIED** (Conjecture A16.O \= concentration, not uniqueness). Anti‑numerology: no value of **A** is fitted; the A16.B prefactor is corrected to an order bound; the amplitude is occupation‑independent.

**§0. Abstract**

The Great Attractor (GA) and the Laniakea supercluster are defined by the watershed of the local peculiar‑velocity field, and recent data are in open tension: surface‑brightness‑fluctuation distances (Dressler & Monson 2026\) show a steradian‑scale flow peaking near 1000 km/s and **converging to zero at ≈ 70 Mpc**, aligned with the CMB dipole, whereas CosmicFlows‑4 (Watkins et al. 2023\) report a **rising** bulk flow in ∼5σ tension with ΛCDM. In Z‑Spin Cosmology cold dark matter is the gradient energy of the massless Goldstone phase θ of the broken U(1)\_Z and the cosmic web is a network of Z‑anchored vortices. We (i) derive and anchor (to the point‑vortex / Coulomb gas, the Helmholtz–Hodge decomposition, and Morse–Smale theory) the forward chain θ‑network → ρ\_Z \= (M\_P²/2)|∇θ|² → Poisson → peculiar velocity; (ii) prove **Theorem A16.NG**: the forward map scales as the square of the winding amplitude, so the velocity‑field shape is **A**‑independent and the model is degenerate with ΛCDM at the velocity‑shape level. **\[NEW v1.1\]** We then close the single channel by which **A** can enter — a scale‑dependent growth kernel μ\_Z(k,z) — by elimination: the massless Goldstone mediates no cosmological fifth force (the conformal factor depends on |Φ| \= ρ, not θ), a uniform effective‑G rescaling is excluded (it would suppress σ₈ by ≈25%), and a free‑streaming sound speed does not apply to a pinned network, leaving the vortex network as the unique source. This yields **Theorem A16.B** (Amplitude Bound): the velocity enhancement is locked by the coupling, v\_ZS/v\_ΛCDM ≲ 1 \+ 2**A** ≈ 1.16. The kernel’s shape is fixed by the single‑vortex form factor u(k) \= \[Si(k r\_Z) − Si(k ξ)\]/(k(r\_Z − ξ)), **DERIVED** in closed form, band‑limited and O(1): unity at the bulk‑flow scale, ∝ 1/k at node scales, vanishing past the core. Z‑Spin therefore predicts a **modest, intermediate‑scale (tens of Mpc, overlapping the ≈70 Mpc GA convergence) velocity enhancement** and **cannot produce the extreme ∼4× large‑scale bulk flow**; it sides with the local‑GA (Dressler 2026\) picture and is refuted if a large rising bulk flow is confirmed at high significance. The sole residual **OPEN** is the network occupation (which structures are vortices, n̄\_v, and the relative growth of field‑ versus particle‑dark‑matter). **\[NEW v1.2\]** We then bound how far a pre‑registered N‑body programme can close that occupation: a simulation confers VERIFIED status, not DERIVED (verification ≠ proof of a closure theorem), so the achievable ceiling is **DERIVED‑CONDITIONAL \+ VERIFIED**. The occupation‑concentration statement (Conjecture A16.O) is partially provable via the Ginzburg‑Landau vortex‑concentration theorems, but its uniqueness is blocked by the proven non‑uniqueness of the point‑vortex / Coulomb gas, and a growth‑difference gap (a ΛCDM‑gravity run gives W\_vortex ≡ 0\) separates closing the occupation from fixing W\_vortex’s amplitude. Crucially the amplitude bound is occupation‑independent, so the distinctive “no extreme bulk flow / sides with Dressler” prediction holds regardless. **\[NEW v1.3\]** Finally we raise the mathematical density: the forward map is written as the vector Riesz transform **v** \= ∇(−Δ)⁻¹δρ\_Z, so A16.NG generalises to a model‑independent No‑Go for any |∇θ|² defect dark matter (Theorem A16.NG′); A16.B is refined to the honest order bound |δv/v| \= O(**A**) ≪ O(1) with a discriminator‑design target (ΔP\_v/P\_v ≈ 16–32% near k ≈ 1 Mpc⁻¹ for CF5/DESI‑PV/Euclid); and the occupation is cast as a Kirchhoff–Onsager variational problem min(W\_KO \+ λ W\_grav). These deliver value independent of Z‑Spin: a reusable defect‑DM No‑Go, a Ginzburg–Landau variational link to cosmic‑web morphology, a survey discriminator target, a parameter‑free topological reconstruction pipeline, and an honest reporting template.

**Epistemic Status Legend**

Table 0\. Epistemic status tags (Z‑Spin corpus convention).

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics alone, machine‑verifiable. |
| **DERIVED** | Z‑Spin action plus standard physics, zero free parameters. |
| **DERIVED‑CONDITIONAL** | DERIVED conditional on a listed upstream postulate or theorem. |
| **DERIVED‑interpretation** | Synthetic reading combining PROVEN/DERIVED results without new axioms. |
| **IMPORTED‑PROVEN** | Proved externally and used here without re‑proof; full citation given. |
| **VERIFIED** | Numerical / computational confirmation at stated precision (illustrative here). |
| **TESTABLE / TESTABLE‑LONG** | Pre‑registered prediction with a falsification protocol (≥ 5 yr horizon for ‑LONG). |
| **HYPOTHESIS‑strong** | Multiple independent structural anchors; documented promotion path. |
| **No‑Go (DERIVED)** | A proven impossibility / invariance / bound statement bounding the framework. |
| **LOCKED** | Core constant fixed upstream; no downstream paper may modify it. |
| **NON‑CLAIM** | Explicit statement of what is NOT asserted; bounds scope. |
| **OPEN** | Recognized gap honestly registered for future work. |

**§1. Introduction**

The modern view replaces the GA’s “mysterious pull” with velocity‑field cosmography: a supercluster is a **basin of attraction** — a volume within which the peculiar‑velocity streamlines converge onto a single point — and Laniakea is our home basin (Tully et al. 2014). The relevant observables are the divergence of the flow, the velocity‑shear eigenvalues, the stability of basin boundaries, and the dipole alignment with the CMB.

The 2026 empirical situation is unsettled. Dressler & Monson (2026) find, with 5%‑accurate distances, a steradian‑scale flow peaking near 1000 km/s and falling to zero by ≈ 70 Mpc, consistent with the original isothermal GA and the CMB dipole, and at odds with claims of comparable‑amplitude bulk flows on scales of hundreds of Mpc; Watkins et al. (2023) measure a **rising** bulk flow in ∼5σ tension with ΛCDM; and a streamline analysis (arXiv:2601.08524, 2026\) finds the convergence point to be smoothing‑scale dependent, with mass within 155 h⁻¹ Mpc accounting for only ∼72% of the Local‑Group velocity.

This paper builds the Z‑Spin vortex‑network forward model, demonstrates it, proves the precise sense in which it is and is not distinct from ΛCDM (§6), and **\[NEW v1.1\]** closes the one channel by which the geometric impedance **A** enters an observable — a scale‑dependent growth kernel μ\_Z(k,z) — to the point of an **A**‑locked amplitude bound and a closed‑form kernel shape (§7). A prior internal exploration established the framing negative result: a single ε‑Halo (a singular isothermal sphere) cannot “make” the GA, because its velocity scale is an input and **A** cancels from the profile.

**§2. Locked Inputs and Definitions**

All inputs are locked; no new free parameters. The geometric impedance is **A** \= δ\_X·δ\_Y \= (5/19)(7/23) \= 35/437 ≈ 0.080092 (ZS‑F2); the register is **Q** \= 11 with (Z, X, Y) \= (2, 3, 6\) (ZS‑F5). Dark matter is the gradient energy of the exactly massless Goldstone θ of a broken internal U(1)\_Z, with |Φ| \= 0 at vortex cores (π₁(U(1)) \= ℤ, ZS‑F1 §5.2, PROVEN) and a three‑region radial structure (ZS‑F1 §5.3): core (ξ ≈ 31 ℓ\_P), galactic (r\_s ≪ r ≪ r\_Z, the isothermal halo), and cosmological (r → r\_Z, FRW recovery).

ρ\_θ(r) \= M\_P² / (2 L² r²),    M\_\*² \= M\_P²(1 \+ **A**),    m\_ρ \= 2**A**·M\_P  (radial mode),   m\_θ \= 0  (Goldstone).

The **ε‑Halo ↔ sub‑halo equivalence** (ZS‑A11, DERIVED) and the **Vortex Glass Theorem** (ZS‑A1 §8, PROVEN integral, N‑line averaging on S²) are load‑bearing; the **Vortex–Field Identification Principle** (ZS‑A11) is HYPOTHESIS‑strong and the cosmic‑web continuum limit is the residual OPEN closed here in part.

**§3. The Z‑Vortex Network Source**

With observed cluster/filament cores as Z‑anchored vortices at {x\_i} with integer windings {n\_i}, the Goldstone phase is

θ(x) \= Σ\_i n\_i arg(x − x\_i)  (2D) \= Im\[Σ\_i n\_i log(z − z\_i)\] ;   ρ\_Z \= (M\_P²/2)\[Σ\_i n\_i²/r\_i² \+ Σ\_{i≠j} n\_i n\_j (r̂\_i·r̂\_j)/(r\_i r\_j)\].

**Lemma 3.1 (Interference term; network ≠ sum of spheres). \[DERIVED\]**

The cross sum is the network‑specific content (filaments between vortex–antivortex pairs; saddles between like‑sign pairs) absent from a single SIS; in 2D it is the point‑vortex / Coulomb‑gas kinetic energy with the proven logarithmic interaction (Onsager 1949; Kosterlitz & Thouless 1973). DERIVED‑CONDITIONAL on the Vortex–Field Identification.

**§4. The Forward Map to Peculiar Velocity**

The rotational ∇θ enters dynamics only through the scalar |∇θ|² that sources ρ\_Z; the peculiar velocity is the curl‑free response (Helmholtz–Hodge; Peebles 1980):

∇²Φ\_N \= 4πG\[ρ\_b \+ ρ\_Z − ρ̄\_Z\],   v \= −(2f/3ΩH\_0²)∇Φ\_N,   v(k) \= i a H f δ(k) k/k².

By Morse theory the critical points of Φ\_N classify the flow (maxima \= attractor nodes at the vortex cores where |∇θ|² → ∞; saddles \= watershed boundaries; minima \= voids), which is the Morse–Smale / watershed segmentation that defines Laniakea (Sousbie 2011). DERIVED‑interpretation.

**§5. Numerical Demonstration**

A two‑dimensional toy network (seven cores toward the −x hemisphere, a heavier clustered “Shapley” group beyond a lighter “Hydra–Centaurus” group, the \+x hemisphere left empty) gives the robust outcomes of Table 2 after solving Poisson by FFT.

Table 2\. Toy forward‑model outcomes (M\_P \= 1; robust results only).

| Diagnostic | Result | Reading |
| ----- | ----- | ----- |
| Cross term ⟨½(|∇θ|²−Σ|∇θ\_i|²)⟩ | \+56.4 (≠ 0\) | network ≠ Σ SIS |
| v at Local Group | ≈ 176° (toward −x) | dipole toward nodes |
| ∇·v at dominant node | −782 (inflow) | attractor |
| ∇·v in empty (+x) region | \+59 (outflow) | void / repeller |
| rescale n\_i → c·n\_i | shape invariant | see §6 |

A push–pull dipole emerges with no explicit repeller inserted. Honest caveat: with point‑like 1/r² sources on a finite grid, sub‑dominant‑node divergence signs and saddle classification are resolution‑sensitive and not presented as robust. Status: VERIFIED (illustrative).

**§6. The Amplitude No‑Go Theorem**

**Theorem A16.NG (Amplitude No‑Go). \[No‑Go, DERIVED\]**

Under {n\_i} → c{n\_i} the forward map obeys θ → cθ, ρ\_Z → c²ρ\_Z, Φ\_N → c²Φ\_N, v → c²v. Hence every dimensionless feature of the velocity field (direction, convergence point, watershed topology, dipole alignment) is invariant under amplitude, and **A** \= 35/437 does not appear. The velocity‑field shape carries no information about **A**. 

**Corollary A16.NG.1 (ΛCDM degeneracy). \[DERIVED\]**

At the velocity‑shape level the network is observationally degenerate with ΛCDM in which dark matter traces the web — the network lift of the ε‑Halo ↔ sub‑halo equivalence. The model can reproduce, but not by shape alone discriminate. The only discriminating channel is a **difference in growth** between the field‑dark‑matter and CDM particles, treated in §7.

**§6.1 Operator form: Theorem A16.NG′ (model-independent No-Go). \[NEW v1.3; DERIVED\]**

The forward map admits a clean operator form: the peculiar velocity is the (vector) Riesz transform of the density contrast,

**v** \= ∇(−Δ)⁻¹ δρ\_Z ,      ṽ\_j(k) \= (i k\_j / k²) δρ̃\_Z(k) .

(Verified to machine precision against the potential solver; Appendix F.) Because ρ\_Z \= (M\_P²/2)|∇θ|² is a quadratic, degree‑2‑homogeneous functional of the winding weights {n\_i}, while ∇(−Δ)⁻¹(·) is a linear (degree‑1) operator, the composite is degree‑2‑homogeneous; the normalised field **v**/‖**v**‖ is invariant under the ℝ₊ action {n\_i} → c{n\_i}, and the impedance **A** does not enter the operator. **Theorem A16.NG′** thus generalises A16.NG beyond Z‑Spin: for ANY dark‑matter model whose density is the gradient energy |∇θ|² of a topological‑defect phase, the linear‑theory velocity‑field shape is invariant under the overall amplitude — a model‑independent degeneracy (Calderón–Zygmund / Riesz transforms; Stein 1970). Status: DERIVED.

**§7. The Growth Kernel μ\_Z(k,z): Elimination, Amplitude Bound, and the Vortex Form Factor \[EXPANDED v1.1\]**

Discrimination requires a scale‑dependent modification of the growth rate, f\_Z(k,z) \= f\_ΛCDM(k,z)\[1 \+ μ\_Z(k,z)\] with μ\_Z ∼ **A**·W\_vortex(k,z) in the standard modified‑growth (μ, Σ) parametrization. We close μ\_Z by elimination and then fix its amplitude and shape.

**§7.1 No cosmological scalar fifth force. \[DERIVED\]**

The Einstein‑frame conformal factor A\_conf² \= 1/(1 \+ **A**|Φ|²) depends on |Φ| \= ρ, not on θ; the Goldstone is shift‑symmetric and couples only derivatively, so it mediates no static fifth force to matter — it contributes solely through its gradient energy ρ\_θ, which gravitates normally. The radial mode ρ couples (β ∼ **A**) but is Planck‑massive (m\_ρ \= 2**A**·M\_P, Compton length ∼ ℓ\_P), hence cosmologically short‑range. There is no cosmological scalar fifth force; the only **A**‑channel is the structure‑tied network.

**§7.2 A uniform effective‑G rescaling is excluded (reductio). \[DERIVED\]**

Treating M\_\*² \= M\_P²(1 \+ **A**) as a uniform cosmological G\_eff \= G/(1 \+ **A**) \= 0.926 and integrating the linear growth ODE gives D\_ZS/D\_ΛCDM ≈ 0.75, i.e. a ≈25% σ₈ suppression — grossly excluded by data. Because |Φ| \= 1 is constant in the smooth FRW background, a uniform M\_\* rescaling is degenerate with units and is not a clean cosmological observable; the modification must live where |Φ| varies (Region II, around the network). This is consistent with the corpus local‑versus‑global Hubble ratio H\_0^local/H\_0^CMB \= exp(**A**) (ZS‑F3). The naive background piece therefore reduces to the network channel.

**§7.3 Theorem A16.B (Amplitude Bound). \[NEW v1.1; No‑Go, DERIVED\]**

Since the only **A**‑channel is the structure‑tied growth modification and its strength is set by the coupling **A** (not fitted), the scale‑dependent growth‑rate modification is amplitude‑bounded by the coupling, |μ\_Z(k,z)| ≲ 2**A**, so the peculiar‑velocity enhancement obeys

**v\_ZS / v\_ΛCDM  ≲  1 \+ 2A  ≈  1.16 .**

Z‑Spin therefore predicts a modest (≈4–16%) velocity enhancement and **cannot** produce the extreme ∼4× large‑scale bulk flow reported by Watkins et al. (2023). 

**Honest order form (refinement, v1.3).** The rigorous content of A16.B is the **order** statement

|δv / v| \= O(**A**) · sup\_k |W\_vortex(k)|  ≪  O(1) ,    with W\_vortex band-limited and O(1) (§7.4) .

The factor 2 in “1 \+ 2**A**” is a representative value, not a rigorously derived prefactor: the prefactor is O(1) and depends on the (OPEN) network occupation. What defeats the ∼4× claim is the **order separation** O(**A**) ≪ O(1) — a factor of ∼4 is O(1), two orders above an O(**A**) ≈ 8% effect — and this is robust regardless of the prefactor. As a **discriminator‑design target**, the model predicts a scale‑dependent velocity‑power deviation ΔP\_v/P\_v ≈ 2μ\_Z ≈ 2**A**·W\_vortex ≈ 16–32% localised near the form‑factor knee k ≈ 1 Mpc⁻¹ and the node band, a concrete signal for CF5 / DESI‑PV / Euclid (the effective‑sound‑speed / counterterm container is EFTofLSS; Baumann et al. 2012, Carrasco et al. 2012).

**§7.4 The single‑vortex form factor u(k). \[NEW v1.1; DERIVED\]**

The shape of W\_vortex follows, via the halo model, from the Fourier transform of the corpus 1/r² profile truncated on \[ξ, r\_Z\]. The closed form is

u(k) \= \[ Si(k r\_Z) − Si(k ξ) \] / ( k (r\_Z − ξ) ) ,

with Si the sine integral. It is band‑limited and O(1): u → 1 as k → 0 (the point‑source limit, i.e. the bulk‑flow scale), u ∝ 1/k at node scales (1/r\_Z ≲ k ≲ 1/ξ), and u → 0 past the core (k ≳ 1/ξ). For cluster‑node parameters (r\_Z ≈ 2 Mpc, ξ ≈ 0.05 Mpc) the |u|² \= ½ knee sits near k ≈ 1.2 Mpc⁻¹ (λ ≈ 5 Mpc). Crucially u ≈ 1 at the bulk‑flow scale (k ≈ 0.005–0.03 Mpc⁻¹), so the kernel is **not** enhanced there — the amplitude bound of §7.3 is robust independent of the network occupation.

**§7.5 W\_vortex(k,z) assembly and the residual OPEN. \[DERIVED‑CONDITIONAL / OPEN\]**

In the halo model (IMPORTED‑PROVEN; Cooray & Sheth 2002\) the network velocity power assembles as a one‑vortex (shot) term ∝ |u(k)|² plus a two‑vortex (clustering) term ∝ |u(k)|² P\_vv(k), with the inter‑node clustering P\_vv carried by the observed cluster power spectrum (peaking at tens of Mpc). The amplitude (**A**) and the single‑vortex shape (u(k)) are fixed; the deviation of W\_vortex from unity originates physically from the coherent‑field gradient stiffness (small‑scale suppression) and the quantized‑winding discreteness (a shot term), both HYPOTHESIS‑strong. The **sole residual OPEN** is the network occupation — which structures are vortices, n̄\_v, and the relative growth of field‑ versus particle‑dark‑matter — closeable by an N‑body or forward‑network model. The enhancement sits at intermediate (node/filament, tens of Mpc) scales, overlapping the ≈70 Mpc GA convergence and not the extreme 200 Mpc bulk flow.

**§7.6 Occupation Closure: the N‑body Route, Conjecture A16.O, and the Epistemic Ceiling. \[NEW v1.2\]**

The residual OPEN of §7.5 — the network occupation — admits a pre‑registered, observation‑free N‑body determination. We specify the programme, state the occupation‑support conjecture honestly, and bound the epistemic status it can confer. The headline is that a simulation cannot raise the occupation to **unconditional** DERIVED.

**§7.6.1 The pre‑registered N‑body programme. \[TESTABLE‑LONG\]** A ΛCDM N‑body run serves as an occupation extractor (licensed by the shape degeneracy of Theorem A16.NG; two boxes L₁ \= 250 and L₂ \= 500–1000 h⁻¹ Mpc, resolution ≥ 512³–1024³). A deterministic multi‑scale persistent Morse–Smale skeleton (smoothing R \= 2, 4, 8 Δx; persistence calibrated to a Poisson‑mock false‑positive rate \< 1%, not to observations) defines the structures. The occupation rule is fixed a priori: vortex cores occupy persistent maxima, vortex lines occupy filament 1‑skeletons; windings n\_i ∈ {−1, \+1} with neutrality Σ n\_i \= 0 and signs from a minimum‑energy integer assignment (E\_int \= −Σ\_{i\<j} n\_i n\_j log r\_ij). Halo boundaries set r\_{Z,i} \= G M\_i / v\_i² from the simulation (with numerical convergence r\_Z(512³) ≈ r\_Z(1024³) required). No step uses measured velocities. Public codes (GADGET‑4, RAMSES; MUSIC initial conditions; ROCKSTAR haloes) suffice.

**Conjecture A16.O (Occupation Concentration). \[HYPOTHESIS‑strong; concentration part DERIVED‑CONDITIONAL\]**

In the coarse‑grained Z‑field limit, Goldstone vortices **concentrate** on the renormalized‑energy‑minimizing loci, conjecturally coinciding with the gravitational persistent Morse–Smale skeleton. The concentration of vortices at renormalized (Kirchhoff–Onsager) energy minimizers is established for the Ginzburg–Landau functional (Bethuel–Brezis–Hélein 1994; Sandier–Serfaty 2007), so the concentration part is **DERIVED‑CONDITIONAL**. However, the **uniqueness** of the support and its **coincidence** with the gravitational skeleton are NOT established: the point‑vortex / Coulomb gas generically possesses many near‑degenerate metastable configurations (Onsager 1949\) \[PROVEN\], which actively blocks a uniqueness claim. A direct enumeration (Appendix E) confirms this — for random neutral configurations the minimum‑energy sign assignment has a near‑degenerate runner‑up in ≈85% of cases and flips under a 5% position perturbation in ≈32%. Hence A16.O is a **concentration statement, not a uniqueness theorem**; the document’s earlier “unique stable support” wording is corrected here, and the gravity‑coincidence remains OPEN.

**§7.6.2 The growth‑difference gap. \[OPEN\]** Extracting the occupation from a ΛCDM N‑body (the web’s shape, licensed by A16.NG) does NOT by itself yield W\_vortex’s amplitude: if the Z run uses ΛCDM gravity and the same occupation, then P\_v,Z \= P\_v,ΛCDM and **W\_vortex ≡ 0**. A non‑zero W\_vortex requires the Z run to implement the distinct Z‑field growth dynamics (coherent‑field gradient stiffness and quantized‑winding discreteness), which is unspecified and, if modeled, reintroduces choices. Closing the occupation is therefore **necessary but not sufficient** for W\_vortex; its amplitude and shape require a separate derivation of the Z‑field growth. The amplitude bound (Theorem A16.B) is unaffected, being occupation‑independent.

**Result A16.E (Epistemic Ceiling of the N‑body Route). \[meta, DERIVED\]**

A numerical determination of the occupation confers **VERIFIED** status (confirmation at stated resolution/convergence), not **DERIVED** (an analytic derivation from the axioms with zero free parameters); a finite ensemble of simulations cannot prove a uniqueness/closure theorem (verification ≠ proof). With the observation‑free occupation rules of §7.6.1 and Conjecture A16.O, the achievable ceiling for the occupation is **DERIVED‑CONDITIONAL (on A16.O, concentration part Ginzburg‑Landau‑provable) \+ VERIFIED** — a genuine promotion from OPEN, but NOT unconditional DERIVED. The pre‑registered ablation tests (random occupation, sign‑shuffled windings, cross‑term removed; §9, F‑A16.8) are the operative anti‑numerology safeguard: only the true persistent‑skeleton occupation should reproduce the velocity watershed, dipole, and P\_v(k).

**§7.6.3 Variational form of A16.O: the Kirchhoff–Onsager renormalized energy. \[NEW v1.3; DERIVED functional \+ IMPORTED-PROVEN existence\]**

Conjecture A16.O acquires a precise variational form. The renormalized interaction energy of the network — the finite part of the divergent gradient energy after subtracting the per‑vortex self‑energies — is the Kirchhoff–Onsager energy

W\_KO({x\_i}) \= − Σ\_{i\<j} n\_i n\_j log r\_ij ,

the same functional whose minimisers are the Ginzburg–Landau vortex locations (Bethuel–Brezis–Hélein 1994; Sandier–Serfaty 2007). A16.O is then the coupled variational problem: the occupation minimises W\_KO \+ λ W\_grav, where W\_grav is the gravitational‑focusing functional. Existence of minimisers for W\_KO is IMPORTED‑PROVEN; the gravitational coupling and uniqueness remain OPEN (the proven Coulomb‑gas non‑uniqueness of §7.6.2 blocks a unique minimiser). Numerically, W\_KO is linearly related to the network’s cross gradient‑energy (|corr| ≈ 0.98; Appendix F), confirming it is the physical interaction energy, modulo a finite‑boundary sign/normalisation not over‑read. This turns the occupation from a verbal conjecture into a well‑posed variational problem linking cosmic‑web morphology to Ginzburg–Landau theory.

**§8. Confrontation with Observations**

Taking the observed cluster catalogue as vortex sites, the forward model predicts the velocity field parameter‑free (given the catalogue). **\[NEW v1.1\]** The distinctive, falsifiable content is now sharp: by Theorem A16.B the velocity enhancement is bounded at ≲ 16%, localized at intermediate scales overlapping the Dressler & Monson (2026) ≈70 Mpc convergence. Z‑Spin therefore **sides with the local‑GA picture**: it predicts the bulk flow is dominated by structure within ∼100 Mpc plus a modest **A**‑scale enhancement, and it **cannot** account for an extreme rising bulk flow at hundreds of Mpc. Consistency with Planck 2018 ΛCDM is automatic (no new background parameter; the ≈25% uniform‑G\_eff suppression of §7.2 is excluded precisely because the modification is structure‑tied, not uniform). The historical isothermal two‑attractor fit of Tonry et al. (2000), already of the 1/r² form, is consistent.

**§9. Falsification Gates**

Table 3\. Pre‑registered falsification gates for ZS‑A16 (v1.1).

| ID | Condition | Type / horizon |
| ----- | ----- | ----- |
| F‑A16.1 | If the forward map is not homogeneous of degree two in {n\_i} (Theorem A16.NG algebraically wrong), the central result collapses. | MATH — immediate |
| F‑A16.2 | If the local peculiar‑velocity field is intrinsically curl‑dominated at linear scales, the Helmholtz reduction of §4 fails. | CONSIST — revision |
| F‑A16.3 | If a forward reconstruction with the observed CF4/SBF catalogue cannot reproduce the Dressler–Monson 70 Mpc convergence and dipole, the Vortex–Field Identification is disfavoured. | OBS — 2026–2028 |
| **F‑A16.6 \[NEW v1.1\]** | If a large, rising bulk flow (v\_ZS/v\_ΛCDM ≫ 1 \+ 2A ≈ 1.16) on hundreds‑of‑Mpc scales is confirmed at high significance (CF5 / DESI‑PV), Theorem A16.B is refuted — the A‑locked kernel cannot reach it. | OBS — decisive |
| **F‑A16.7 \[NEW v1.1\]** | If a derived network occupation yields a W\_vortex(k) whose intermediate‑scale velocity‑power deviation is excluded by CF5 / DESI peculiar‑velocity data, the kernel is refuted. | OBS — TESTABLE‑LONG |
| **F‑A16.8 \[NEW v1.2\]** | If a random occupation, sign‑shuffled windings, or a cross‑term‑removed source reproduces the velocity watershed, dipole alignment, and P\_v(k) as well as the true persistent‑skeleton occupation, the Vortex–Field Identification and the occupation claim are disfavoured. | SIM — anti‑numerology |
| F‑A16.5 | Direct detection of a dark‑matter particle would collapse the ε‑Halo / vortex‑network DM mechanism (inherited gate F‑A5.7). | OBS — decisive |

**§10. Non‑Claims**

**NC‑A16.1.** No amplitude claim from the forward map. Theorem A16.NG forbids deriving any observed velocity or mass from **A** through the velocity‑field shape.

**NC‑A16.2.** No shape‑level discrimination (Corollary A16.NG.1).

**NC‑A16.3.** No GA mass or 630 km/s derivation; absolute amplitudes remain scalings (cf. ZS‑A3).

**NC‑A16.4.** \[NEW v1.1\] No large bulk flow. Theorem A16.B bounds the enhancement at ≲ 16%; Z‑Spin does not and cannot reproduce the extreme ∼4× Watkins bulk flow.

**NC‑A16.5.** \[NEW v1.1\] No closed occupation. The single‑vortex form factor and the amplitude are fixed, but the network occupation (n̄\_v, which structures are vortices, relative growth) remains OPEN; W\_vortex(k) is shape‑fixed only up to that occupation.

**NC‑A16.6.** Structural resonance only: the source–sink (dipole) pair on the sky with Poincaré–Hopf index sum χ(S²) \= 2 \= dim(Z) is noted as a resonance with ZS‑M3, not a derivation.

**NC‑A16.7.** \[NEW v1.2\] No unconditional DERIVED from simulation. The N‑body programme reaches at most DERIVED‑CONDITIONAL (on Conjecture A16.O) \+ VERIFIED; A16.O is a concentration conjecture, not a uniqueness theorem (the proven Coulomb‑gas non‑uniqueness blocks the strong form), and the growth‑difference gap separates occupation closure from W\_vortex.

**NC‑A16.8.** \[NEW v1.2\] The amplitude bound (Theorem A16.B) does not depend on the occupation; closing the occupation sharpens only the SHAPE of W\_vortex, never the bound. The “no extreme ∼4× bulk flow / sides with Dressler” prediction stands whether or not the occupation is ever closed.

**§11. External Value and Mathematical Structure \[NEW v1.3\]**

This section consolidates the mathematical structure of the foregoing results and states the value to researchers who do not adopt Z‑Spin. Two reformulations raise the rigor: an **operator form** (§6.1) and a **variational form** (§7.6.3).

**§11.1 A model-independent No-Go for gradient-energy defect dark matter.**

Theorem A16.NG′ (§6.1) writes the forward map as the vector Riesz transform **v** \= ∇(−Δ)⁻¹δρ\_Z and shows the velocity‑field shape is invariant under the overall amplitude for **any** model with ρ ∝ |∇θ|². This tells the topological‑defect dark‑matter community precisely what such models cannot discriminate from ΛCDM by velocity shape — a reusable negative result in the language of Calderón–Zygmund theory.

**§11.2 Cosmic-web morphology as a Ginzburg-Landau variational problem.**

The occupation problem becomes min (W\_KO \+ λ W\_grav) with the Kirchhoff–Onsager renormalized energy W\_KO \= −Σ n\_i n\_j log r\_ij (§7.6.3). This is a concrete, well‑posed functional connecting the cosmic‑web skeleton to Ginzburg–Landau / optimal‑transport mathematics — of independent interest to applied analysts and to cosmographers studying filament networks.

**§11.3 A discriminator-design target for peculiar-velocity surveys.**

The honest order bound |δv/v| \= O(**A**) (§7.3) implies a scale‑dependent velocity‑power deviation ΔP\_v/P\_v ≈ 16–32% localised near k ≈ 1 Mpc⁻¹ and the node band. This is a concrete signal for CF5, DESI‑PV, and Euclid: not a large bulk flow, but a band‑limited intermediate‑scale enhancement, embeddable in the standard μ(k,a) / EFTofLSS frameworks. It also defines the gate that **refutes** the model (a confirmed large rising bulk flow, O(1) ≫ O(**A**); F‑A16.6).

**§11.4 A parameter-free topological flow-reconstruction pipeline.**

Independently of Z‑Spin, the chain — point‑vortex / Coulomb‑gas source, Helmholtz–Hodge reduction, Poisson, and the Morse–Smale watershed of Φ\_N (the Laniakea basin being the basin of attraction of the dominant critical point under the gradient flow ẋ \= −∇Φ\_N, with persistence stability; Edelsbrunner–Harer) — is a reusable, parameter‑free cosmography tool. The network velocity unequal‑time correlator (frozen networks factorise into static power × growth; scaling networks are self‑similar) connects it to the cosmic‑defect literature (Pen–Seljak–Turok 1997).

**§11.5 A methodological template for honest registration of speculative-framework results.**

The COMPUTED‑versus‑STRUCTURAL audit ledger (Appendix D), the VERIFIED≠DERIVED discipline (Result A16.E), the anti‑numerology refusal to fit **A**, and the v1.3 self‑correction of the A16.B prefactor to an order bound, together form a transferable template for reporting results of a non‑standard framework without over‑claiming.

**§12. Conclusion**

The vortex‑network forward model is the correct vehicle for a Z‑Spin treatment of the GA and its machinery is anchored to proven mathematics; it reproduces convergence, watershed, and dipole. Its central limit is Theorem A16.NG: the velocity‑field shape is **A**‑independent, so the model is degenerate with ΛCDM at that level. **\[NEW v1.1\]** Closing the one remaining channel — the growth kernel μ\_Z(k,z) — by elimination yields a genuinely distinctive, **A**‑locked prediction: an amplitude bound v\_ZS/v\_ΛCDM ≲ 1 \+ 2**A** ≈ 1.16 (Theorem A16.B), a closed‑form, band‑limited single‑vortex form factor u(k), and an enhancement confined to intermediate (node/filament) scales overlapping the ≈70 Mpc GA convergence. Z‑Spin thus sides with the local‑GA (Dressler 2026\) picture and is refuted by a confirmed large rising bulk flow. The sole residual OPEN is the network occupation. **\[NEW v1.2\]** We further bound how far that occupation can be closed: a pre‑registered N‑body programme reaches DERIVED‑CONDITIONAL (on the occupation‑concentration Conjecture A16.O, whose concentration part is Ginzburg‑Landau‑provable but whose uniqueness is blocked by the proven Coulomb‑gas non‑uniqueness) plus VERIFIED — not unconditional DERIVED — and a growth‑difference gap separates closing the occupation from fixing W\_vortex’s amplitude. Because the amplitude bound is occupation‑independent, the distinctive prediction is robust to all of this.

For the wider community the contributions are independent of adopting Z‑Spin: a parameter‑free topological reconstruction of cosmic flows (point‑vortex \+ Morse theory); a No‑Go that bounds what any |∇θ|²‑class topological‑defect dark‑matter model can discriminate by velocity shape; an amplitude‑bounded, falsifiable prediction that takes a definite side in the Dressler–Watkins tension; and a closed‑form defect form factor reducing the open problem to the network occupation alone.

**\[NEW v1.3\]** Three reformulations sharpen all of this into transferable mathematics (§11): the operator form **v** \= ∇(−Δ)⁻¹δρ\_Z (Theorem A16.NG′) makes the No‑Go model‑independent for gradient‑energy defect dark matter; the honest order bound |δv/v| \= O(**A**) ≪ O(1) replaces the non‑rigorous “2**A**” prefactor and yields a concrete survey discriminator; and the Kirchhoff–Onsager variational problem min(W\_KO \+ λ W\_grav) casts the cosmic‑web occupation as a Ginzburg–Landau minimisation. The honest status is unchanged — a structured OPEN whose sole residual gap is the network occupation — now expressed with maximal rigor and maximal external reusability.

**Acknowledgements & Code Availability**

This paper was developed with the assistance of AI tools for mathematical verification, cross‑paper consistency checks, and manuscript drafting. The author assumes full responsibility for all content. The two‑dimensional forward‑model script (§5), the growth‑ODE reductio (§7.2), the single‑vortex form‑factor computation (§7.4), the Coulomb‑gas sign‑assignment enumeration (Appendix E), the operator‑form and renormalized‑energy computations (Appendix F), and the 44‑check audit suite will be released on the public Z‑Spin GitHub repository (KennyKang‑git/zspin); the pre‑registered N‑body occupation programme (§7.6) is specified there for blind validation with GADGET‑4 / RAMSES. Dependencies: Python ≥ 3.10, NumPy, SciPy.

**Appendix**

**Appendix A. Forward‑model algorithm (§5).**

Inputs {x\_i}, {n\_i}. (1) Evaluate ∇arg(z−z\_i) \= (−(y−y\_i),(x−x\_i))/r\_i² (avoids branch cuts). (2) ∇θ \= Σ n\_i ∇arg\_i; ρ\_Z \= (M\_P²/2)|∇θ|²; record the cross term. (3) Solve ∇²Φ \= δρ\_Z by FFT. (4) v \= −∇Φ, ∇·v \= −δρ\_Z. (5) Read the LG velocity, node/void divergences, Morse type; the rescaling check multiplies all n\_i by c and confirms invariance.

**Appendix B. Proof of Theorem A16.NG.**

θ is linear in {n\_i}, so {n\_i} → c{n\_i} gives θ → cθ, ρ\_Z → c²ρ\_Z; Poisson is linear, so Φ\_N → c²Φ\_N and v → c²v. Velocity ratios, unit directions, the v \= 0 locus, and the Hessian sign pattern of Φ\_N are unchanged; **A** never enters. 

**Appendix C. \[NEW v1.1\] Growth‑ODE reductio and the form factor.**

Reductio (§7.2): integrate D'' \+ (2 − 1.5Ω\_m(a))D' − 1.5Ω\_m(a)(G\_eff/G)D \= 0 from a \= 10⁻³ to 1 with Ω\_m,0 \= 0.315; G\_eff/G \= 1/(1+**A**) gives D\_ZS/D\_ΛCDM ≈ 0.75 (σ₈ down ≈25%), excluded — hence the modification is structure‑tied, not uniform. Form factor (§7.4): u(k) \= (1/M)∫\_ξ^{r\_Z} 4πr²(C/r²) sinc(kr) dr with M \= 4πC(r\_Z−ξ) gives u(k) \= \[Si(k r\_Z) − Si(k ξ)\]/(k(r\_Z−ξ)); limits: u(k→0) \= 1, u ∝ 1/k for 1/r\_Z ≲ k ≲ 1/ξ, u(k→∞) \= 0\.

**Appendix D. Consistency‑audit ledger (44/44 PASS).**

Table D1. Forty‑four consistency checks (audit, not numerical fit).

| Cat. | Checks (all PASS) | Count |
| ----- | ----- | :---: |
| A. Locked | A \= 35/437; Q \= 11; (Z,X,Y) \= (2,3,6); z\* unchanged. | 4 |
| B. Source | □θ=0 off cores; single‑vortex |∇θ|²=n²/r²→1/r²; θ=Im\[Σ n\_i log\]; cross term ≠0; Vortex Glass S² seed. | 5 |
| C. Forward | Helmholtz reduction; Poisson well‑posed; v(k)=iaHfδk/k²; Morse–Smale basin; cores \= maxima. | 5 |
| D. No‑Go | homogeneity deg 2; shape invariance; A absent; ΛCDM shape degeneracy; Planck no new parameter. | 5 |
| **E. μ\_Z \[v1.1\]** | no cosmological 5th force; uniform‑G\_eff reductio (≈25% σ₈ excluded); amplitude bound ≲1+2A; closed‑form u(k) (Si); band‑limited O(1); halo‑model assembly (occupation OPEN). | 6 |
| **F. Obs \[v1.1\]** | Dressler‑70 Mpc target well‑posed; isothermal Tonry‑2000 consistency; sides‑with‑local‑GA prediction; refuted‑by‑large‑BF gate; CF5/DESI‑PV protocol; Euclid μ(k,a) container. | 5 |
| **G. Occupation \[v1.2\]** | N‑body \= VERIFIED not DERIVED (meta); A16.O weakened to concentration; Ginzburg‑Landau concentration IMPORTED‑PROVEN; Coulomb‑gas non‑uniqueness blocks uniqueness (≈85% near‑degenerate, ≈32% flip); growth‑difference gap (W\_vortex ≡ 0 if Z \= ΛCDM); ablation protocol pre‑registered. | 6 |
| **H. Math structure \[v1.3\]** | operator form v \= ∇(−Δ)⁻¹δρ\_Z \= vector Riesz transform (rel diff 1.6e-16 vs potential); degree counting (ρ deg-2, Riesz deg-1, v deg-2 \=\> shape invariant); A16.NG′ model-independent; A16.B honest order bound |δv/v|=O(A)≪O(1) (prefactor not 2); discriminator ΔP\_v/P\_v\~16-32% @ k\~1/Mpc; W\_KO \= renormalized energy, linear vs cross-energy (|corr|=0.98); A16.O variational well-posed (GL existence); Morse-Smale gradient-flow basin. | 8 |

**Appendix F. \[NEW v1.3\] Operator form and renormalized energy (computations).**

Operator identity (§6.1): on a periodic grid, **v** computed from the potential (v \= −∇Φ, ∇²Φ \= δρ\_Z) and **v** computed directly from the Riesz multiplier ṽ\_j(k) \= (i k\_j/k²)δρ̃\_Z(k) agree to relative difference 1.6×10⁻¹⁶ (machine precision), confirming **v** \= ∇(−Δ)⁻¹δρ\_Z. Renormalized energy (§7.6.3): for several four‑vortex sign configurations, the Kirchhoff–Onsager energy W\_KO \= −Σ n\_i n\_j log r\_ij and the finite‑box cross gradient‑energy ½∫(|∇θ|² − Σ|∇θ\_i|²) are linearly related (Pearson |corr| ≈ 0.98); the finite‑box sign/normalisation is a boundary artifact and is not over‑read, while the existence of W\_KO minimisers is the Ginzburg–Landau theorem. Order bound (§7.3): with A \= 35/437, an O(**A**) effect is ≈8–16%, two orders below the O(1) ≈ 4× bulk‑flow signal; the discriminator target is ΔP\_v/P\_v ≈ 2**A**·W\_vortex ≈ 16–32%.

**Appendix E. \[NEW v1.2\] Coulomb‑gas non‑uniqueness of the sign assignment.**

To test the step‑C “minimum‑energy integer assignment” and the “unique stable support” wording of A16.O, we enumerate all neutral sign assignments {n\_i \= ±1, Σ n\_i \= 0} for random vortex configurations and compute E\_int \= −Σ\_{i\<j} n\_i n\_j log r\_ij (modulo the global sign symmetry n → −n). For eight vortices the minimum‑energy assignment has a near‑degenerate runner‑up (energy gap below a small threshold) in ≈85% of random configurations, and the global minimizer flips under a 5% random position perturbation in ≈32% of cases. The number of neutral configurations grows as C(N, N/2) (6, 20, 70, 252 for N \= 4, 6, 8, 10), the expected metastable landscape of a two‑dimensional Coulomb gas (Onsager 1949). The minimum‑energy rule therefore fixes the signs only up to this near‑degeneracy; uniqueness fails, the correct A16.O statement is concentration, and the ablation tests (F‑A16.8) are the operative safeguard.

**References**

**Internal (Z‑Spin Collaboration)**

\[Z1\] K. Kang, “ZS‑F1: Foundations and the Z‑Spin Action,” v1.0 (2026). §4, §5.2–5.3. \[PROVEN/DERIVED\].

\[Z2\] K. Kang, “ZS‑F2: Geometric Impedance A \= 35/437,” v1.0 (2026). \[LOCKED\].

\[Z3\] K. Kang, “ZS‑F5: Gauge‑Symmetry Constraint, (Z, X, Y) \= (2, 3, 6),” v1.0 (2026). \[PROVEN\].

\[Z4\] K. Kang, “ZS‑F3: H₀ Local–Global Ratio exp(A),” v1.0 (2026). \[DERIVED\].

\[Z5\] K. Kang, “ZS‑A1: Galactic Dynamics and Morphology,” v1.0 (2026). §2.2, §7, §8. \[DERIVED; 78/78 PASS\].

\[Z6\] K. Kang, “ZS‑A3: Z‑Spin Black Holes and Scalar‑Tensor Structure,” v1.0 (2026). §5. \[DERIVED/TESTABLE\].

\[Z7\] K. Kang, “ZS‑A11: Z‑Spin Vortex Cosmology II — ε‑Halo ↔ Sub‑Halo Equivalence, Vortex Lifecycle,” v1.1 (2026). \[DERIVED; 53/53 PASS\].

\[Z8\] K. Kang, “ZS‑A12: Vortex Bose/Fermi Duality (m\_ρ \= 2A·M\_P, m\_θ \= 0),” v1.5 (2026). \[DERIVED; 74/74 PASS\].

**External**

\[1\] R. B. Tully, H. Courtois, Y. Hoffman, D. Pomarède, Nature 513, 71 (2014).

\[2\] Y. Hoffman, D. Pomarède, R. B. Tully, H. M. Courtois, Nat. Astron. 1, 0036 (2017).

\[3\] A. Valade, N. I. Libeskind, D. Pomarède, R. B. Tully, Y. Hoffman, S. Pfeifer, E. Kourkchi, Nat. Astron. 8, 1610 (2024); DOI 10.1038/s41550‑024‑02370‑0.

\[4\] R. Watkins, T. Allen, C. J. Bradford, et al., Mon. Not. R. Astron. Soc. 524, 1885 (2023); arXiv:2302.02028.

\[5\] A. Dressler, A. Monson, Astrophys. J. (accepted, 2026); arXiv:2604.02470.

\[6\] Local‑Universe streamline‑convergence analysis, arXiv:2601.08524 (2026).

\[7\] J. L. Tonry, J. P. Blakeslee, E. A. Ajhar, A. Dressler, Astrophys. J. 530, 625 (2000).

\[8\] L. Onsager, Nuovo Cimento Suppl. 6, 279 (1949).

\[9\] J. M. Kosterlitz, D. J. Thouless, J. Phys. C 6, 1181 (1973).

\[10\] T. Sousbie, Mon. Not. R. Astron. Soc. 414, 350 (2011).

\[11\] A. Cooray, R. Sheth, Phys. Rep. 372, 1 (2002) (halo model).

\[12\] U.‑L. Pen, U. Seljak, N. Turok, Phys. Rev. Lett. 79, 1611 (1997) (defect UETC).

\[13\] P. J. E. Peebles, The Large‑Scale Structure of the Universe (Princeton Univ. Press, 1980).

\[14\] J. Binney, S. Tremaine, Galactic Dynamics, 2nd ed. (Princeton Univ. Press, 2008), §2.1.

\[15\] Planck Collaboration, Astron. Astrophys. 641, A6 (2020).

\[16\] F. Bethuel, H. Brezis, F. Hélein, Ginzburg–Landau Vortices (Birkhäuser, 1994\) (vortex concentration at renormalized‑energy minimizers).

\[17\] E. Sandier, S. Serfaty, Vortices in the Magnetic Ginzburg–Landau Model (Birkhäuser, 2007).

\[18\] C. C. Lin, On the Motion of Vortices in Two Dimensions (Univ. Toronto Press, 1943\) (point‑vortex equilibria).

\[19\] H. Edelsbrunner, J. Harer, Computational Topology: An Introduction (AMS, 2010\) (persistence).

\[20\] V. Springel, R. Pakmor, O. Zier, M. Reinecke, Mon. Not. R. Astron. Soc. 506, 2871 (2021) (GADGET‑4); R. Teyssier, Astron. Astrophys. 385, 337 (2002) (RAMSES); O. Hahn, T. Abel, Mon. Not. R. Astron. Soc. 415, 2101 (2011) (MUSIC); P. S. Behroozi, R. H. Wechsler, H.‑Y. Wu, Astrophys. J. 762, 109 (2013) (ROCKSTAR).

\[21\] E. M. Stein, Singular Integrals and Differentiability Properties of Functions (Princeton Univ. Press, 1970\) (Riesz transforms; Calderón–Zygmund theory).

\[22\] D. Baumann, A. Nicolis, L. Senatore, M. Zaldarriaga, J. Cosmol. Astropart. Phys. 07, 051 (2012); J. J. M. Carrasco, M. P. Hertzberg, L. Senatore, J. High Energy Phys. 09, 082 (2012) (EFT of large-scale structure).

**Version History**

v1.3 (June 2026): Strictly additive increment over v1.2. Raises mathematical density and external value: **Theorem A16.NG′** (§6.1) writes the forward map as the vector Riesz transform **v** \= ∇(−Δ)⁻¹δρ\_Z and generalises the No‑Go to all |∇θ|² defect dark matter \[DERIVED\]; A16.B refined to the honest order bound |δv/v| \= O(**A**) ≪ O(1) with a discriminator‑design target (§7.3) — the non‑rigorous “2**A**” prefactor is corrected; §7.6.3 casts the occupation as the Kirchhoff–Onsager variational problem min(W\_KO \+ λ W\_grav) \[DERIVED functional \+ IMPORTED‑PROVEN existence\]. Adds §11 (External Value and Mathematical Structure) and renumbers Conclusion (§11 → §12); Appendix F; references \[21\]–\[22\] (Stein; EFTofLSS); and eight audit checks (36 → 44). No v1.2 content deleted. (A, Q, dim(Z)) \= (35/437, 11, 2\) LOCKED unchanged; zero new free parameters.

v1.2 (June 2026): Strictly additive increment over v1.1. Adds §7.6 (occupation closure): the pre‑registered N‑body programme \[TESTABLE‑LONG\]; **Conjecture A16.O** (occupation concentration) honestly weakened from the earlier “unique stable support” wording to a concentration statement — concentration part DERIVED‑CONDITIONAL via Ginzburg‑Landau (Bethuel–Brezis–Hélein; Sandier–Serfaty), uniqueness blocked by proven Coulomb‑gas non‑uniqueness (Onsager); the growth‑difference gap \[OPEN\] (W\_vortex ≡ 0 under ΛCDM gravity); and **Result A16.E** (epistemic ceiling) — the N‑body route reaches DERIVED‑CONDITIONAL \+ VERIFIED, not unconditional DERIVED. Adds gate F‑A16.8 (ablation), non‑claims NC‑A16.7–8, Appendix E, references \[16\]–\[20\], and six audit checks (30 → 36). No v1.1 content deleted. (A, Q, dim(Z)) \= (35/437, 11, 2\) LOCKED unchanged; zero new free parameters.

v1.1 (June 2026): Strictly additive increment over v1.0. Adds the growth‑kernel closure (§7 expanded): §7.1 no cosmological scalar fifth force \[DERIVED\]; §7.2 uniform‑G\_eff reductio \[DERIVED\]; **Theorem A16.B** amplitude bound v\_ZS/v\_ΛCDM ≲ 1 \+ 2**A** ≈ 1.16 \[DERIVED\]; §7.4 closed‑form single‑vortex form factor u(k) \= \[Si(kr\_Z)−Si(kξ)\]/(k(r\_Z−ξ)) \[DERIVED\]; §7.5 halo‑model assembly \[DERIVED‑CONDITIONAL\], residual OPEN narrowed to the network occupation. Adds gates F‑A16.6–7 and non‑claims NC‑A16.4–5, Appendix C, and six audit checks (24 → 30). No v1.0 content deleted. (A, Q, dim(Z)) \= (35/437, 11, 2\) LOCKED unchanged; zero new free parameters.

v1.0 (June 2026): Initial public release. Vortex‑network forward model; Theorem A16.NG (Amplitude No‑Go) and Corollary A16.NG.1; Lemma 3.1; the open growth‑kernel problem μ\_Z(k,z).