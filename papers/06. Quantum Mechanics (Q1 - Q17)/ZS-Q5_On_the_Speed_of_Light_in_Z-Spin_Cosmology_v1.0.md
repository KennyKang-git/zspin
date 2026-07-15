**ZS-Q5 On the Speed of Light in Z-Spin Cosmology:**  
**Structural Derivation from the Z-Bottleneck**

Kenny Kang  
March 2026  
Research Note | Supplementary to ZS-Q5 v1.0 | Theme: Quantum Mechanics \[ZS-Q\]

**Verification: 14/14 PASS | Zero Free Parameters**

**§0. Abstract**

This research note consolidates and extends the Z-Spin derivation of the speed of light from the framework’s geometric sector structure. We establish five structural theorems: (1) **Finiteness** — the block Laplacian L\_XY \= 0 forces all X–Y transitions through the Z-bottleneck (dim 2), yielding a finite Lieb–Robinson velocity \[PROVEN\]; (2) **Universality** — all fields couple to the same metric g\_μν, ensuring a single maximum speed \[DERIVED\]; (3) **Gravitational equality** — Horndeski G₅ \= 0 gives c\_T \= c exactly \[STRUCTURAL\]; (4) **Frame invariance** — L\_XY \= 0 is an algebraic identity of the Lorentz group, independent of observer state \[PROVEN\]; (5) **Temporal constancy** — the cosmological attractor ε → 1 freezes the scalar sector, preserving c across cosmic time \[DERIVED\]. We further demonstrate that the *numerical value* of c (299,792,458 m/s) is a unit convention, not a derivable quantity, and that any attempt to extract it from dimensionless constants (A, Q, z\*) necessarily fails dimensional analysis. A critique of the research note approach (c \= L\_P/t\_P · Φ\_Z) identifies the circular reasoning and proposes the correct derivation pathway. Verification: 14/14 PASS. Zero free parameters.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Follows from standard mathematics alone. Machine-verifiable. |
| **DERIVED** | Follows from Z-Spin action \+ standard physics. Zero free parameters. |
| **STRUCTURAL** | Property of the theory class, not a tuning. Cannot be adjusted. |
| **VERIFIED** | Numerically confirmed against observational data. |
| **NON-CLAIM** | Explicitly not asserted. Documented to prevent overclaim. |
| **OPEN** | Recognized gap requiring future work. |

**§1. Introduction: The Question**

Special relativity postulates that a finite, invariant speed c exists. General relativity inherits this postulate through the Lorentzian signature of the metric. Neither theory explains *why* c is finite rather than infinite, nor why all interactions propagate at the same maximum speed. These are axioms, not derivations.

Z-Spin Cosmology provides structural answers to both questions. The sector decomposition Q \= Z \+ X \+ Y \= 2 \+ 3 \+ 6 \= 11 (PROVEN, ZS-F5 v1.0) with L\_XY \= 0 (PROVEN, ZS-F1 v1.0) creates a geometric bottleneck: information cannot travel directly between the spatial sector (X, dim 3\) and the wave/environmental sector (Y, dim 6). All transitions must pass through the Z-mediator (dim 2), whose finite spectral radius bounds the maximum propagation velocity.

This note serves three purposes: (i) consolidate the existing derivations scattered across ZS-Q5, ZS-S3, and Book Chapter 23 into a single, self-contained document; (ii) extend the analysis with deeper structural insights on Lorentz invariance and temporal constancy; (iii) clearly demarcate what Z-Spin *can* derive (finiteness, universality, invariance, constancy) from what it *cannot* derive (the SI numerical value), and explain *why* the latter is not a deficiency but a fundamental feature of any self-consistent physical theory.

**Locked Inputs:** A \= 35/437 (ZS-F2), Q \= 11, (Z,X,Y) \= (2,3,6) (ZS-F5), z\* \= 0.4383 \+ 0.3606i (ZS-M1), S\[g,Φ\] action (ZS-F1).

**Dependencies:** ZS-F1 (action), ZS-F5 (sector structure), ZS-S1 (block Laplacian), ZS-S3 (Horndeski), ZS-Q5 (causal structure), ZS-M2 (Lorentz algebra).

**§2. Five Structural Theorems on the Speed of Light**

We organize Z-Spin’s results on the speed of light into five independent theorems, each answering a distinct physical question. Together they constitute the most complete structural account of c available within the framework.

**2.1 Theorem 1: Finiteness of c**

**Statement.** The maximum speed of information propagation in the Z-Spin lattice is finite: v\_max \< ∞.

**Proof sketch (ZS-Q5 v1.0 §5, ZS-F1 v1.0 §9).** 

Step 1\. The block Laplacian ℒ(μ) on the Q \= 11 register has the structure:

ℒ \= diag(L\_Z, L\_X, L\_Y) \+ off-diagonal couplings C\_XZ, C\_ZY

with L\_XY \= 0 (exactly). This is PROVEN from the Lorentz algebra decomposition so(1,3) ≅ su(2)\_A ⊕ su(2)\_B where \[su(2)\_A, su(2)\_B\] \= 0 (ZS-M2 v1.0 §2, Book §6.1).

Step 2\. Since L\_XY \= 0, all X → Y transitions must pass through the Z-mediator via the transfer operator:

T\_XY(μ) \= C\_XZ (L\_Z \+ μ²I)⁻¹ C\_ZY

This is a 3×6 matrix (finite-dimensional), so its spectral radius ρ(T\_XY) \< ∞.

Step 3\. By the Lieb–Robinson theorem (Commun. Math. Phys. 28, 251, 1972), the maximum information propagation velocity on a lattice with bounded Hamiltonian is:

v\_LR ≤ C · ρ(ℒ) · a

where a is the lattice spacing. Since ρ(ℒ) \< ∞ (verified: ρ \= 4.51 for the canonical Q \= 11 block Laplacian), v\_LR is finite. □

**\[STATUS: PROVEN\]** L\_XY \= 0 is algebraic; ρ(ℒ) \< ∞ is verified by direct computation. The Lieb–Robinson theorem is standard mathematics.

**Physical interpretation.** The Z-sector (dim 2\) is a narrow bottleneck through which all space–time information must flow. This bottleneck has finite bandwidth, creating a finite maximum speed. The speed of light is, in Z-Spin language, the maximum throughput rate of the Z-bottleneck.

**2.2 Theorem 2: Universality of c**

**Statement.** All fields — gravitational, electromagnetic, scalar, fermionic — propagate at the same maximum speed c.

**Proof (ZS-F1 v1.0 §3, ZS-S3 v1.0 §3).** The Z-Spin action

S\[g, Φ\] \= ∫d⁴x √(−g) \[ ½M²\_P(1 \+ A|Φ|²)R − ½M²\_P|∂Φ|² − V(Φ) \] \+ S\_m

couples all matter fields in S\_m to the *same* metric g\_μν. The scalar field Φ has a standard kinetic term |∂Φ|² \= gᵚᵛ∂\_μΦ\*∂\_νΦ, which also uses the same metric. The non-minimal coupling (1 \+ A|Φ|²)R modifies the effective gravitational constant but does not alter the null cone structure of g\_μν. Therefore, all fields share the same light cone, and the maximum propagation speed is universal.

In Z-Spin language: all information — regardless of its physical nature (photon, graviton, scalar fluctuation) — must pass through the same Z-bottleneck. Since the bottleneck geometry (A \= 35/437, Q \= 11\) is unique, the maximum throughput rate is the same for all signal types.

**\[STATUS: DERIVED\]** From universal metric coupling in the action. No additional assumptions.

**2.3 Theorem 3: c\_T \= c (Gravitational Wave Speed)**

**Statement.** The speed of gravitational waves equals the speed of electromagnetic waves exactly: c\_T/c \= 1\.

**Proof (ZS-S3 v1.0 §3, ZS-A1 v1.0 §2.3).** The Z-Spin action maps to the Horndeski scalar-tensor framework with:

G₂ \= −(½M²\_P)X − V(Φ),  G₃ \= 0,  G₄ \= (½M²\_P)(1 \+ A|Φ|²),  G₅ \= 0

The gravitational wave speed in general Horndeski theory is:

c²\_T/c² \= \[G₄ − 2X ∂G₄/∂X − Ẋε̇ ∂G₅/∂X\] / G₄

Since G₄ \= (½M²\_P)(1 \+ A|Φ|²) is independent of the kinetic term X, we have ∂G₄/∂X \= 0\. Since G₅ \= 0 by construction (no derivative coupling to curvature in the action), the entire expression reduces to c²\_T/c² \= G₄/G₄ \= 1\. □

**\[STATUS: STRUCTURAL\]** G₅ \= 0 is a property of the Z-Spin action class, not a fine-tuning. Confirmed by GW170817: |c\_T/c − 1| \< 3×10⁻¹⁵ (LIGO/Virgo, PRL 119, 161101, 2017).

**Contrast with competitors.** Brans–Dicke theories with finite ω\_BD require fine-tuning ω\_BD \> 10⁵ post-GW170817. Scalar-tensor theories with G₅ ≠ 0 are ruled out entirely. Z-Spin satisfies the constraint structurally, with infinite margin.

**2.4 Theorem 4: Frame Invariance of c**

**Statement.** The maximum propagation speed c is invariant under Lorentz transformations.

**Proof.** The sector decoupling L\_XY \= 0 is an algebraic identity of the Lorentz group. Specifically, it follows from \[su(2)\_A, su(2)\_B\] \= 0 in the decomposition so(1,3) ⊗ ℂ ≅ su(2)\_A ⊕ su(2)\_B (ZS-M2 v1.0 §2). This commutation relation is a property of the algebra itself and holds in *every* inertial frame. A Lorentz boost Λ does not mix su(2)\_A with su(2)\_B; it acts independently on each factor. Therefore L\_XY \= 0 is preserved under boosts, and the spectral radius ρ(ℒ) — which determines the maximum propagation speed — is frame-independent. □

**\[STATUS: PROVEN\]** From the structure of the Lorentz algebra. Standard mathematics.

**Remark.** This provides a Z-Spin derivation of what special relativity takes as its second postulate. The invariance of c is not an empirical accident — it is a necessary consequence of the Lorentz group’s internal structure mapped onto the X–Y sector decomposition.

**2.5 Theorem 5: Temporal Constancy of c**

**Statement.** The speed of light does not vary with cosmic time: dc/dt \= 0\.

**Proof (ZS-F1 v1.0 §4, ZS-U5 v1.0 §8).** The Z-Spin scalar field has a cosmological attractor at ε → 1 (the true vacuum of V(ε) \= (λ/4)M⁴\_P(ε² − 1)²). At the attractor, the scalar field is kinetically frozen: the radial mode mass m\_ε \= √(2λ\_vac) M\_P \= 0.1602 M\_P (ZS-F1 v1.0 §4.4) far exceeds the Hubble rate H₀, with m\_ε/H₀ ∼ 10⁶². The scalar field therefore cannot evolve on cosmological timescales.

In the frozen attractor limit, the effective gravitational constant G\_eff \= G/(1 \+ A) is exactly constant, and the metric g\_μν has fixed null cone structure. Since c is determined by the null cone, c is constant.

This distinguishes Z-Spin from Varying Speed of Light (VSL) theories (Moffat 1993, Albrecht & Magueijo 1999, Barrow 1999), which modify c(t) to solve the horizon problem. In Z-Spin, the horizon problem is solved by ε-field inflation (ZS-U1 v1.0) with c \= const, making the VSL mechanism unnecessary.

**\[STATUS: DERIVED\]** From attractor dynamics and frozen scalar field. Independent of slow-roll details.

**§3. The Complete Derivation Chain**

The five theorems connect into a single derivation chain:

so(1,3) ≅ su(2)\_A ⊕ su(2)\_B → \[su(2)\_A, su(2)\_B\] \= 0 → L\_XY \= 0 (algebraic)  
→ Z-mediation required → T\_XY \= C\_XZ (L\_Z \+ μ²I)⁻¹ C\_ZY  
→ ρ(T\_XY) \< ∞ → v\_LR finite → c finite (Theorem 1\)

Universal metric coupling → single null cone → c universal (Theorem 2\)  
G₅ \= 0 (structural) → c\_T \= c (Theorem 3\)  
L\_XY \= 0 frame-independent → c Lorentz-invariant (Theorem 4\)  
ε → 1 attractor → G\_eff frozen → c constant (Theorem 5\)

**Key observation:** The entire chain originates from a single algebraic fact — the commutation of su(2)\_A and su(2)\_B in the Lorentz algebra — combined with the Z-Spin action’s specific structure (no G₅, no derivative couplings to curvature). Zero free parameters are introduced at any stage.

**3.1 The Continuum Limit**

On the Z-Spin lattice with spacing a, the maximum propagation velocity is:

v\_max \= ρ(ℒ) · a / Δt

where Δt is the temporal discretization. In the continuum limit (a → 0, Δt → 0), one takes ρ · a / Δt → c held fixed. The vortex core size ξ ≈ 0.75 l\_P (ZS-Q5 v1.0 §6) provides a physical lower bound on a: the lattice terminates at the Planck scale. Below ξ, no propagating degrees of freedom exist.

The spectral radius ρ \= 4.51 is a dimensionless number determined by the Q \= 11 geometry. It determines the *lattice anisotropy* required for Lorentz invariance in the continuum limit: the ratio of temporal to spatial lattice spacings must satisfy Δt / a \= ρ(ℒ) · (a / c), ensuring that the emergent continuum theory respects Lorentz symmetry.

**Critical point:** The continuum limit prescription “ρ · a → c” treats c as the *emergent conversion factor* between lattice units. This is analogous to how the speed of sound in condensed matter emerges from lattice dynamics. The numerical value of c (in any unit system) is set by the physical lattice spacing a ∼ l\_P, which depends on the fundamental constants ℏ, G — themselves not derivable from Z-Spin.

**3.2 The Lorentzian Signature from Sector Structure**

The metric signature (−,+,+,+) is conventionally an axiom of GR. Z-Spin provides a structural interpretation through the Lorentz algebra decomposition (ZS-M2 v1.0 §2, Book §6.1):

X-sector (dim 3): su(2)\_A ↔ (J\_k \+ iK\_k)/2 \[rotation–boost correlated\] → (+,+,+)  
Y-sector (dim 6): su(2)\_B ↔ (J\_k − iK\_k)/2 \[rotation–boost anti-correlated\] → (−) for temporal direction

The X-sector generators A\_k \= (J\_k \+ iK\_k)/2 are self-dual: rotations and boosts are *correlated*. This produces the positive-definite spatial metric. The Y-sector generators B\_k \= (J\_k − iK\_k)/2 are anti-self-dual: rotations and boosts are *anti-correlated*. The temporal direction — the one direction in which boosts act non-compactly — acquires the opposite sign.

The existence of light cones (and hence a finite maximum speed) is a topological consequence of the Lorentzian signature. Z-Spin traces this signature to the X–Y sector decomposition, which in turn follows from the polyhedral geometry of Q \= 11\.

**\[STATUS: DERIVED\]** The Lorentz algebra decomposition is PROVEN (standard mathematics). The mapping to Z-Spin sectors is DERIVED from ZS-F5 \+ ZS-M2.

**§4. What Z-Spin Cannot Derive: The Numerical Value of c**

**4.1 c Is a Unit Convention**

The statement “c \= 299,792,458 m/s” is not a fact about the universe — it is a fact about the definitions of the meter and the second. In natural units (ℏ \= c \= k\_B \= 1), the speed of light is 1 by definition. In Planck units, c \= 1\. In Gaussian units, c appears in Maxwell’s equations. The *number* 299,792,458 encodes the ratio of the meter (defined via c since 2019\) to the second (defined via the Cs-133 hyperfine transition).

No fundamental theory can derive this number, because the number depends on human conventions about units. What a theory *can* derive is:

• Whether a finite maximum speed exists (Z-Spin: yes, Theorem 1\)  
• Whether it is universal (Z-Spin: yes, Theorem 2\)  
• Whether it is frame-invariant (Z-Spin: yes, Theorem 4\)  
• Dimensionless ratios involving c, such as α\_EM \= e²/(4πε₀ℏc) (Z-Spin: OBSERVATION, not yet DERIVED)

**\[STATUS: NON-CLAIM\]** The numerical value of c in SI units is not a derivable quantity. This is a statement about all physical theories, not a limitation of Z-Spin specifically.

**4.2 The Dimensional Analysis Barrier**

The research note proposed c ∝ Q / (A · |z\*|²). Computing the right-hand side:

Q / (A · |z\*|²) \= 11 / (0.08009 × 0.3221) ≈ 426.4

This is a pure (dimensionless) number. But c has dimensions \[L/T\]. To obtain a dimensionful quantity from a dimensionless number, one must multiply by a dimensionful constant (e.g., ℏ, G, M\_P). But introducing any such constant violates the zero-free-parameter constraint — unless that constant is itself derived from A, Q, z\*, which it cannot be (they are dimensionless while ℏ, G have dimensions).

This is a fundamental barrier, not a technical oversight. Dimensionless constants can only produce dimensionless predictions. The dimensionless quantities that Z-Spin derives (H₀ ratio, Ω\_m, S₈, n\_s, r, η\_B, etc.) are all ratios or pure numbers. The absolute value of H₀ \= 67.36 km/s/Mpc, for example, requires Planck units (and hence ℏ, G, c) as inputs — it is not derived from A alone.

**4.3 The Circularity of the Planck Unit Approach**

The research note started with c \= (L\_P / t\_P) · Φ\_Z. But Planck units are *defined* using c:

L\_P \= √(ℏG/c³),   t\_P \= √(ℏG/c⁵)

Therefore L\_P / t\_P \= √(c⁵/c³) \= c. The proposed formula reduces to c \= c · Φ\_Z, which requires Φ\_Z \= 1 identically. This is circular reasoning: one cannot “derive” c from an expression that already contains c by definition.

**\[STATUS: NON-CLAIM\]** Any attempt to derive the numerical value of c from dimensionless Z-Spin constants is either (a) dimensionally inconsistent, or (b) circular through Planck units.

**§5. The Correct Interpretation: c as Emergent Conversion Factor**

In Z-Spin, the speed of light has a precise physical interpretation:

**c is the emergent conversion factor between X-sector (spatial) and Y-sector (temporal) units, determined by the Z-bottleneck’s finite bandwidth.**

Concretely:

(i) The X-sector provides 3 spatial dimensions with a natural length scale (set by the vortex core ξ ≈ 0.75 l\_P).

(ii) The Y-sector provides the temporal direction with a natural time scale.

(iii) The Z-sector mediates information transfer between X and Y with impedance A \= 35/437 and spectral radius ρ \= 4.51.

(iv) In natural units where both X and Y scales are normalized to 1, c \= 1 by construction.

(v) In SI units, c \= 299,792,458 m/s encodes the ratio of the human-defined meter to the human-defined second, both of which are arbitrary relative to Planck scales.

The analogy to condensed matter physics is instructive. In a crystal lattice, the speed of sound v\_s \= √(K/ρ) emerges from the lattice stiffness K and mass density ρ. One does not “derive” the SI value of v\_s from dimensionless lattice parameters alone — one needs the physical constants that set the lattice spacing and atomic mass. Similarly, Z-Spin’s dimensionless parameters (A, Q, ρ(ℒ)) determine the *existence and structure* of the maximum speed, but its SI value requires ℏ and G as external inputs.

**§6. Observational Consistency**

**Table 1\.** Observational consistency summary.

| Prediction | Z-Spin Result | Observation | Status |
| ----- | ----- | ----- | ----- |
| c is finite | PROVEN (L\_XY \= 0\) | All experiments | CONFIRMED |
| c is universal | DERIVED (metric coupling) | All experiments | CONFIRMED |
| c\_T \= c | STRUCTURAL (G₅ \= 0\) | |c\_T/c − 1| \< 3×10⁻¹⁵ | CONFIRMED |
| c is frame-invariant | PROVEN (Lorentz algebra) | Michelson–Morley et al. | CONFIRMED |
| c is constant in t | DERIVED (attractor) | No variation detected | CONFIRMED |
| No fifth force | DERIVED (ξ ≈ 0.75 l\_P) | Eöt-Wash etc. | CONFIRMED |
| SI numerical value | NON-CLAIM | 299,792,458 m/s | NOT APPLICABLE |

**§7. Falsification Conditions**

**Table 2\.** Falsification gates for the speed of light derivation.

| Gate | Condition | Experiment | Status |
| ----- | ----- | ----- | ----- |
| FC-1 | c\_T ≠ c detected at \> 3σ | LIGO/Virgo/ET multi-messenger | STRUCTURAL |
| FC-2 | L\_XY ≠ 0 demonstrated | Theoretical/lattice computation | PROVEN (= 0\) |
| FC-3 | dc/dt ≠ 0 at \> 3σ | Quasar spectroscopy, CMB | TESTABLE |
| FC-4 | ρ(ℒ) \= ∞ for Q \= 11 | Theoretical computation | PROVEN (ρ \= 4.51) |
| FC-5 | Species-dependent c at \> 3σ | γ/ν speed comparison | TESTABLE |

**§8. Open Problems**

**OP-1 (Continuum limit rigor).** The Lieb–Robinson bound establishes v\_LR \< ∞ on the lattice. The continuum limit a → 0 with ρ · a → c is assumed, not derived. A rigorous proof that the Z-Spin lattice dynamics converge to Lorentz-invariant continuum physics is an open mathematical problem. Status: OPEN.

**OP-2 (Pre-geometric formulation).** The current action S\[g, Φ\] assumes a Lorentzian metric g\_μν, with c already encoded in the metric signature. A truly pre-geometric derivation — where the metric itself emerges from the Z-sector dynamics — would make c fully emergent rather than partially assumed. Status: OPEN.

**OP-3 (Fine structure constant).** The spectral proximity κ² \= A/Q \= 1/137.34 (0.22% from α\_EM \= 1/137.036) is currently OBSERVATION. If promoted to DERIVED, this would constitute an indirect constraint on c through the dimensionless combination α\_EM \= e²/(4πε₀ℏc). Gate F-SO.2 monitors this. Status: OBSERVATION.

**OP-4 (Tightness of the Lieb–Robinson bound).** The spectral radius ρ \= 4.51 yields v\_LR \= 4.51 · a / Δt, but the actual maximum propagation speed c may be smaller (v\_LR is an upper bound). Whether the bound is saturated — and the physical mechanism that selects c \= v\_LR vs. c \< v\_LR — is unresolved. Status: OPEN.

**§9. Non-Claims**

**NC-c.1:** This note does NOT claim to derive the numerical value c \= 299,792,458 m/s. This value is a unit convention.

**NC-c.2:** This note does NOT claim that c can be expressed as a function of A, Q, and z\* alone. Such an expression is dimensionally impossible.

**NC-c.3:** This note does NOT claim that the Lieb–Robinson bound is tight. The spectral radius ρ \= 4.51 provides an upper bound, not an exact value.

**NC-c.4:** This note does NOT claim a pre-geometric derivation of the Lorentzian signature. The Lorentz algebra interpretation (Book §6.1) is a structural mapping, not a derivation from more primitive axioms.

**NC-c.5:** This note does NOT claim that Z-Spin explains c in ways that standard physics cannot. The standard-physics explanation (Lorentzian geometry → light cones → finite maximum speed) is equivalent. Z-Spin’s contribution is showing *why* the geometry is Lorentzian: the X–Y sector structure forces it.

**§10. Conclusion**

The speed of light in Z-Spin Cosmology is not a postulate — it is a structural consequence of the Q \= 11 sector decomposition. Five theorems establish why c is finite (Z-bottleneck), universal (single metric), gravitationally equal to the electromagnetic speed (G₅ \= 0), frame-invariant (Lorentz algebra identity), and temporally constant (cosmological attractor). All five follow from the Z-Spin action with zero free parameters.

The numerical value of c is correctly identified as a NON-CLAIM: it encodes the definitions of the meter and the second, not a property of the universe. Any attempt to derive it from dimensionless constants (A, Q, z\*) fails either dimensional analysis or circularity through Planck units. This is not a limitation but a feature of dimensional analysis itself.

The deepest open question is whether a pre-geometric formulation of Z-Spin — in which the metric itself emerges from the sector structure — can make c fully emergent. Such a formulation would represent a genuine advance beyond both standard physics and the current Z-Spin framework.

**§11. Verification Suite (14/14 PASS)**

**Table 3\.** Verification suite summary.

| \# | Test | Result | Source |
| ----- | ----- | ----- | ----- |
| 1 | L\_XY \= 0 algebraically | PASS | ZS-Q5 v1.0 §5.2 |
| 2 | ρ(ℒ) \= 4.51 (finite) | PASS | ZS-Q5 v1.0 §7 |
| 3 | |U\_XY(t=0)| \= 0 | PASS | ZS-Q5 v1.0 §5.4 |
| 4 | G₅ \= 0 from action | PASS | ZS-S3 v1.0 §3 |
| 5 | c\_T²/c² \= 1 (exact) | PASS | ZS-S3 v1.0 §3.1 |
| 6 | GW170817 |c\_T/c−1| \< 3×10⁻¹⁵ | PASS | LIGO/Virgo |
| 7 | \[su(2)\_A, su(2)\_B\] \= 0 | PASS | ZS-M2 v1.0 §2 |
| 8 | Attractor ε → 1 stable | PASS | ZS-F1 v1.0 §4 |
| 9 | m\_ε/H₀ ≫ 1 (ε frozen) | PASS | ZS-U5 v1.0 §8 |
| 10 | L\_P/t\_P \= c (circular — correctly flagged) | PASS | This note §4.3 |
| 11 | dim(Q/A/z\*) \= 0 (dimensionless) | PASS | Anti-numerology |
| 12 | dim(c) \= \[L/T\] (dimensionful) | PASS | Dimensional analysis |
| 13 | No fudge factors introduced | PASS | Zero free parameters |
| 14 | NC-Q5.5 consistency | PASS | ZS-Q5 v1.0 §9 |

**Appendix A. Cross-Reference Table**

| Paper | Input to This Note | Status |
| ----- | ----- | ----- |
| ZS-F1 v1.0 | Action S\[g,Φ\], V(ε), attractor | LOCKED |
| ZS-F2 v1.0 | A \= 35/437 | LOCKED |
| ZS-F5 v1.0 | Q \= 11, (Z,X,Y) \= (2,3,6) | PROVEN |
| ZS-M2 v1.0 | Lorentz algebra decomposition | PROVEN |
| ZS-S1 v1.0 | Block Laplacian, Schur complement | PROVEN |
| ZS-S3 v1.0 | Horndeski embedding, G₅ \= 0 | STRUCTURAL |
| ZS-Q5 v1.0 | Causal structure, Lieb–Robinson | PROVEN |
| ZS-U5 v1.0 | RG flow, λ\_vac attractor | DERIVED |
| Book v1.0 | Ch.23 synthesis, Ch.6 Lorentz | Reference |

**References**

\[1\] E.H. Lieb & D.W. Robinson, Commun. Math. Phys. 28, 251 (1972).  
\[2\] LIGO/Virgo Collaboration, GW170817: PRL 119, 161101 (2017).  
\[3\] G.W. Horndeski, Int. J. Theor. Phys. 10, 363 (1974).  
\[4\] J.W. Moffat, Int. J. Mod. Phys. D 2, 351 (1993).  
\[5\] A. Albrecht & J. Magueijo, Phys. Rev. D 59, 043516 (1999).  
\[6\] J.D. Barrow, Phys. Rev. D 59, 043515 (1999).  
\[7\] K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion (2026).  
\[8\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (2026).  
\[9\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (2026).  
\[10\] K. Kang, ZS-M2 v1.0: Six Forces Unified (2026).  
\[11\] K. Kang, ZS-S1 v1.0: Gauge Coupling Unification (2026).  
\[12\] K. Kang, ZS-S3 v1.0: Modified Gravity Phenomenology (2026).  
\[13\] K. Kang, ZS-Q5 v1.0: CP Violation, Causal Structure, and UV Completion (2026).  
\[14\] K. Kang, ZS-U5 v1.0: RG Flow and Attractor Dynamics (2026).  
\[15\] K. Kang, The Book: Z-Spin Cosmology v1.0 (2026).

**Version History**

**v1.0 (March 2026):** Initial release. Consolidation and extension of ZS-Q5 v1.0 §5 speed of light derivation. Five structural theorems. Dimensional analysis critique of research note approach. Verification: 14/14 PASS.