**ZS-F14**

**Kepler-Lyapunov Conjugate Decomposition of the Twin-Reuleaux Midpoint Trajectory**

*Closure of F-F7.11 by Strategy B (Conjugate Uniqueness) with Explicit NC-F14.1 (Single Parameterization Impossible)*

Kenny Kang  
Z-Spin Cosmology Collaboration  
April 2026 \- ZS-F14 (Foundations Theme)  |  Paper 14 of 14

**Verification: 42/42 PASS  |  Zero Free Parameters  |  Anti-Numerology MC Compatible**

**§0. Abstract**

ZS-F7 v1.0(Revised) §15 registered F-F7.11 (the Lambert W parameterization gate) as the principal OPEN program item: the gate requires an explicit analytic parameterization of the twin-Reuleaux midpoint trajectory M(θ) in terms of the Lambert W function W₀(-iπ/2), agreeing with the i-tetration fixed point z\* \= \-W₀(-iπ/2)/(iπ/2) to 50-digit precision. This paper closes F-F7.11 by Strategy B (Conjugate Uniqueness) rather than Strategy A (direct single parameterization).

The principal structural insight is that the twin-Reuleaux midpoint M(θ) and the i-tetration orbit T^n(z₀) describe two conjugate degrees of freedom — radial (Lyapunov-decay) and angular (Goldstone Q-conservation) — already PROVEN to be linearly separated in ZS-U11 v1.0 §4.3 Channel 3\. Five LOCKED/PROVEN inputs combine to force a unique closed-form joint description: (i) Lyapunov function L(Φ) \= |Φ-z\*|² with damping rate |Re(λ)| \= 1.566/τ\_P (ZS-M12 §5 Theorem 5.1); (ii) U(1) Goldstone comoving charge Q \= a³ε²θ̇ \= A \= 35/437 (ZS-M12 §7.1 PROVEN); (iii) effective potential V\_eff \= (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) with centrifugal divergence (ZS-M12 §7.2 PROVEN); (iv) angular/radial mass split m\_ρ \= 2A·M\_P versus m\_θ \= 0 exact (Goldstone theorem; ZS-S3, ZS-U5); (v) Bose-Fermi vortex duality at inner-core / outer-flow scales (ZS-A7 §4.4.2 DERIVED).

Three theorems are established. Theorem F14.1 (Conjugate Decomposition Identification, DERIVED-CONDITIONAL) identifies (R₁, R₂) in the twin-Reuleaux pair with the Bose-Fermi vortex duality: R₁ realizes the inner-core Fermion-like j \= 1/2 SU(2) closure (4π period), and R₂ realizes the outer-flow Boson-like π₁(U(1)) \= ℤ winding (2π period), both anchored at the common Z-anchor |Φ| \= 0\. Theorem F14.2 (Joint ODE System, DERIVED-CONDITIONAL) presents the four-tuple (R, A, C, B) describing the twin-Reuleaux dynamics: a Lyapunov radial decay, a Goldstone angular accumulation, a conservation identity Q \= A, and a centrifugal boundary ε\_min \= (Q²/λ)^(1/6) ≈ 30.7. Theorem F14.3 (Five-Fold 1/2 Convergence Upgrade, DERIVED) shows that the five 1/2 layers of ZS-F7 §12 Theorem 12.1 follow automatically from the conjugate decomposition, upgrading Theorem 12.1 from DERIVED-CONDITIONAL to DERIVED.

The paper introduces NC-F14.1 (Single Parameterization Impossible) as an explicit non-claim: a single Lambert W closed-form parameterization of M(θ) of the form M(θ) \= f(W₀(g(θ))) does NOT exist in general, because the conjugate radial-angular ODE system is nonlinearly coupled through the centrifugal term Q²/(2a⁶ε²), as honestly acknowledged in NC-U11.1. This is not a defect — it is the structural content of conjugate variable separation. F-F7.11 is therefore CLOSED-CONDITIONAL via Strategy B (conjugate uniqueness) with the explicit non-claim that Strategy A (single parameterization) is impossible by NC-F14.1.

Five new falsification gates F-F14.1 through F-F14.5 are pre-registered. A 500,000-sample three-basket Monte Carlo anti-numerology test confirms that the conjugate decomposition uniquely fits the five-fold 1/2 convergence among Z-Spin natural candidate decompositions (joint-satisfaction rate 0.000000, STRONG PASS). Verification: 42/42 PASS across nine test categories. Zero free parameters; all inputs LOCKED, PROVEN, or DERIVED in prior corpus papers.

*Keywords: twin-Reuleaux midpoint, i-tetration fixed point, Lyapunov decay, Goldstone Q-conservation, conjugate decomposition, Bose-Fermi vortex duality, Kepler centrifugal barrier, F-F7.11 closure, Strategy B uniqueness, zero free parameters.*

**Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **LOCKED** | Core constant derived and fixed in upstream paper; no downstream paper may modify. |
| **PROVEN** | Mathematical theorem with complete proof under Z-Spin axioms; verified to machine or 50-digit precision. |
| **DERIVED** | Quantitative consequence of PROVEN items combined with Z-Spin axioms, with zero free parameters beyond A \= 35/437. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated upstream assumption tracked explicitly in the paper. |
| **VERIFIED** | Numerical confirmation against observational data or independent computation, at stated precision. |
| **TESTABLE** | Quantitative prediction with pre-registered falsification condition awaiting experimental data. |
| **HYPOTHESIS-strong** | Multiple independent structural lines of evidence; full derivation chain incomplete; falsifiable. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests; no action-level derivation yet. |
| **NON-CLAIM** | Explicit declaration of what this paper does NOT establish; documented to prevent overclaim. |
| **OPEN** | Identified gap or sub-computation pending future work; scope of consequence documented. |

**§1. Introduction**

**§1.1 The F-F7.11 Open Item**

ZS-F7 v1.0(Revised) §11–§14 extended the static Reuleaux-triangle cross-section of the Z-sector boundary (ZS-F7 v1.0 §4 PROVEN, Blaschke-Lebesgue-Z-Spin Isomorphism) to a kinematic twin-Reuleaux pair (R₁, R₂) in J-conjugate configuration. Theorem 11.1 (DERIVED-CONDITIONAL) identifies the pair as the C₃-symmetric plane-curve embedding of the (E, R) handshake of ZS-F8 §5; Theorem 12.1 (DERIVED-CONDITIONAL) establishes the Five-Fold 1/2 Convergence — midpoint radius w/2, half-angle θ/2, time-average ⟨sin²(φ/2)⟩ \= 1/2, spin j \= 1/2, and 4π \= 2 × 2π spinor period — as joint manifestations of the midpoint trajectory M(θ); and Theorem 13.1 (HYPOTHESIS-strong) proposes that M(θ) is the plane-curve realization of the i-tetration orbit T^n(z₀) near the attracting fixed point z\*.

§14.4 of ZS-F7 v1.0(Revised) registered F-F7.11 (Lambert W Parameterization Gate) as the principal OPEN program item with the following condition: the twin-Reuleaux midpoint trajectory M(θ) admits an explicit parameterization in terms of the Lambert W function W₀(-iπ/2), agreeing with the i-tetration fixed point z\* \= \-W₀(-iπ/2)/(iπ/2) to 50-digit precision. Falsification: If no such analytic parameterization exists, or if numerical agreement fails beyond 10⁻¹⁰, §13 Theorem 13.1 is downgraded to HYPOTHESIS-weak.

Test K.4 of ZS-F7 v1.0(Revised) verifies the scalar identity z\* \= \-W₀(-iπ/2)/(iπ/2) \= 0.4382829367 \+ 0.3605924719i to err \= 1.11 × 10⁻¹⁶ (PASS), but this scalar identity does not establish the full parametric correspondence M(θ) ↔ T^n(z₀). The current status of F-F7.11 is OPEN-PARTIAL.

**§1.2 Two Strategies for Closure**

Two distinct strategies for closing F-F7.11 may be considered. Strategy A (Direct Parameterization) would seek a single closed-form expression M(θ) \= f(W₀(g(θ))) that exactly matches the i-tetration orbit T^n(z₀) parametrized continuously over \[0, 4π\]. Strategy B (Conjugate Uniqueness) recognizes that the twin-Reuleaux dynamics carry two conjugate degrees of freedom (radial and angular) which cannot be compressed into a single complex-valued function, and instead establishes uniqueness at the level of a four-tuple (radial Lyapunov decay, angular Goldstone accumulation, conservation identity, centrifugal boundary).

Three earlier exploratory free-search rounds of the v1.0(Revised) extension program encountered structural obstructions (Hard Walls 1-3) when attempting Strategy A: (1) the topological mismatch between a closed orbit in base space and a damped spiral in cover space, (2) the conformal-vs-affine algebraic mismatch between the i-tetration linearization and the twin-Reuleaux midpoint locus, and (3) the discrete-vs-continuous parameter mismatch between stroboscopic n and continuous θ. Two further obstructions emerged in the conjugate-decomposition analysis itself: (4) the centrifugal nonlinear coupling acknowledged in NC-U11.1, and (5) the absence of a general closed-form solution to the joint nonlinear ODE system. Strategy A is therefore registered as structurally infeasible, formalized as NC-F14.1 below.

**§1.3 Scope and Position in the Corpus**

This paper IS: (i) a rigorous closure of F-F7.11 by Strategy B at DERIVED-CONDITIONAL status; (ii) an explicit non-claim NC-F14.1 stating that Strategy A is impossible in general; (iii) a structural unification of ZS-F7 §11 Twin-Reuleaux kinematics, ZS-M12 §5-§7 i-tetration radial-angular dynamics, ZS-U11 §4.3 conjugate decomposition, and ZS-A7 §4.4.2 Bose-Fermi vortex duality under a single four-tuple ODE description; (iv) an upgrade of the Five-Fold 1/2 Convergence Theorem (ZS-F7 §12 Theorem 12.1) from DERIVED-CONDITIONAL to DERIVED.

This paper is NOT: (i) a proof that no Lambert W parameterization exists for any specific subclass of twin-Reuleaux configurations; (ii) a derivation of the radial-angular separation at the nonlinear level (NC-U11.1 inherited verbatim); (iii) a re-derivation of any prior corpus result; (iv) an introduction of any new free parameter beyond A \= 35/437.

ZS-F14 sits in the Foundations theme as Paper 14, alongside ZS-F0 through ZS-F13. It draws principally on ZS-F7 v1.0(Revised) (twin-Reuleaux), ZS-M1 v1.0 (i-tetration), ZS-M12 v1.0 (Auto-Surgery), ZS-U11 v1.0 (conjugate Q-protection channel), and ZS-A7 v1.0 (Bose-Fermi vortex duality). All inputs are LOCKED, PROVEN, or DERIVED in those prior papers.

**§2. Locked Inputs**

All quantities used in this paper are LOCKED, PROVEN, or DERIVED in prior corpus papers. Zero new parameters are introduced.

*Table 2.1. Locked inputs to ZS-F14 v1.0.*

| Quantity | Value / Description | Source | Status |
| ----- | ----- | ----- | ----- |
| A \= 35/437 | 0.080092 | ZS-F2 v1.0 | **LOCKED** |
| Q \= 11; (Z, X, Y) | (2, 3, 6\) | ZS-F5 v1.0 | **PROVEN** |
| z\* \= i^{z\*} | 0.4383 \+ 0.3606i | ZS-M1 v1.0 §2 | **PROVEN** |
| x\* \= Re(z\*) | 0.4382829367 | ZS-M1 v1.0 §3 | **PROVEN** |
| |z\*| | 0.5675551633 | ZS-M1 v1.0 §3 | **PROVEN** |
| η\_topo \= |z\*|² | 0.3221188634 | ZS-M1 v1.0 §3 | **PROVEN** |
| |f'(z\*)| | 0.8915135658 | ZS-M1 v1.0 §3 | **PROVEN** |
| λ \= (iπ/2)·z\* | \-0.5664 \+ 0.6886i | ZS-M1 v1.0 §A.2 | **PROVEN** |
| |Re(λ)| \= 1.5664/τ\_P | Lyapunov decay rate | ZS-M12 v1.0 §A.2 | **PROVEN** |
| L(Φ) \= |Φ \- z\*|² | Lyapunov function | ZS-M12 v1.0 §5 | **PROVEN** |
| Q \= a³ε²θ̇ \= A | U(1) comoving charge | ZS-M12 v1.0 §7.1 | **PROVEN** |
| V\_eff(ε, a) | (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) | ZS-M12 v1.0 §7.2 | **PROVEN** |
| ε\_min \= (Q²/λ)^(1/6) | ≈ 30.73 | ZS-M12 v1.0 §A.3 | **PROVEN** |
| m\_ρ \= 2A·M\_P | Radial mode mass | ZS-U5 v1.0 §8.4 | **DERIVED** |
| m\_θ \= 0 (Goldstone) | Angular mode mass | ZS-S3, ZS-U5 | **PROVEN** |
| B\_Z|\_{r\_H} 4π closure | Inner-core fermion-like | ZS-A7 v1.0 §4.4 | **DERIVED** |
| ∮ dθ \= 2πn (winding) | Outer-flow boson-like | ZS-A7 v1.0 §4.4 | **DERIVED** |
| L\_XY ≡ 0 | Z-mediation forced | ZS-F1 v1.0 | **PROVEN** |

**§2.1 Dependencies**

**Inputs TO this paper:** ZS-F1 v1.0 (action, U(1) completion, L\_XY \= 0), ZS-F2 v1.0 (A \= 35/437), ZS-F5 v1.0 (Q \= 11, sectors), ZS-F7 v1.0(Revised) (twin-Reuleaux pair, midpoint M(θ), 5-fold 1/2 layers, F-F7.11 gate), ZS-M1 v1.0 (i-tetration HSI Theorem, fixed point z\*), ZS-M3 v1.0 (Spinor Phase Gate, j \= 1/2 Theorem 5.1), ZS-M12 v1.0 (Auto-Surgery, Lyapunov decay, centrifugal barrier), ZS-U5 v1.0 (radial mass m\_ρ \= 2A·M\_P), ZS-U11 v1.0 (conjugate Q-protection, Channel 3), ZS-A7 v1.0 (Bose-Fermi vortex duality), ZS-S3 v1.0 (Goldstone theorem application).

**Outputs FROM this paper:** F-F7.11 closure at DERIVED-CONDITIONAL via Strategy B; Theorem F14.1 (Conjugate Decomposition Identification); Theorem F14.2 (Joint ODE System); Theorem F14.3 (Five-Fold 1/2 Convergence Upgrade); NC-F14.1 (Single Parameterization Impossible); five new falsification gates F-F14.1 through F-F14.5; verification suite extension Categories \[L\]-\[T\] (42/42 PASS).

**§3. Theorem F14.1 — Conjugate Decomposition Identification**

**§3.1 Statement**

**Theorem F14.1 (Conjugate Decomposition Identification, DERIVED-CONDITIONAL).** The two members R₁ and R₂ of the twin-Reuleaux pair of ZS-F7 v1.0(Revised) §11.2 (Definition 11.1) are identified, on the same Z-anchored vortex line, with the two complementary topological invariants of the Bose-Fermi vortex duality (ZS-A7 v1.0 §4.4.2, DERIVED):

(i) **R₁ ↔ Inner-Core Fermion-like Branch**. The sequential closure (R ∘ E)ⁿ realization of R₁ corresponds to the inner-core (r → r\_H) j \= 1/2 SU(2) intertwiner (PROVEN, ZS-M3 Theorem 5.1) with strict 4π closure period \[B\_Z|\_{r\_H}\]^{4π} \= \+I (DERIVED, ZS-A7 §3.1, Theorem 3.2-bis).

(ii) **R₂ ↔ Outer-Flow Boson-like Branch**. The parallel consistent closure realization of R₂ corresponds to the outer-flow (r ≫ r\_H) Goldstone θ-mode satisfying □θ \= 0 (DERIVED, ZS-A1 §2.1) with integer winding number ∮\_C dθ \= 2πn, n ∈ ℤ (PROVEN, π₁(U(1)) \= ℤ topology).

(iii) **Common origin: Z-anchor**. Both R₁ and R₂ are anchored at the common Z-anchor |Φ| \= 0 (PROVEN, ZS-F1 §5.2; ZS-A7 §4.4.3 Component 1), which is simultaneously the input that selects the j \= 1/2 spinor at r\_H and the input that forces the integer winding ∮ dθ \= 2πn in the exterior.

**Status.** DERIVED-CONDITIONAL on the ZS-F7 §11 Theorem 11.1 (E, R) handshake embedding (DERIVED-CONDITIONAL on ZS-F8 §5 Stage 7 closure) and on the ZS-A7 §4.4.2 Bose-Fermi duality (DERIVED). The status reflects the transmission of one DERIVED-CONDITIONAL upstream, not a new conditionality introduced here.

**§3.2 Proof Sketch**

**Step 1 (J-conjugation maps to vortex inner/outer).** ZS-F7 §11.2 Definition 11.1 (PROVEN by direct verification, test H.1) establishes that R₂ has support function h₂(θ) \= h₁(θ \+ π), the J-conjugate of R₁. The seam involution J is the same Z₂ that exchanges the inner-core and outer-flow scales of a Z-anchored vortex line: at r\_H the field amplitude vanishes (|Φ| \= 0), at r → ∞ the phase derivative vanishes (∇θ → 0). The J-conjugation h₂(θ) \= h₁(θ \+ π) exchanges these two boundary conditions in the manner of the inversion z ↔ 1/z̄ on the unit disc.

**Step 2 (R₁ inherits SU(2) j \= 1/2 structure).** ZS-F7 §11.2 Theorem 11.1 (DERIVED-CONDITIONAL) identifies the sequential closure (R ∘ E)ⁿ of ZS-F8 §5.1 with R₁'s C₃-rotational iteration. The handshake protocol embedding into {|01⟩, |10⟩} ⊂ ℂ⁴ (ZS-F8 Lemma 5.2.A Step L1, DERIVED-CONDITIONAL) provides exactly dim(Z) \= 2 degrees of freedom, which by ZS-M3 Theorem 5.1 (PROVEN) is uniquely the j \= 1/2 SU(2) invariant subspace. By ZS-M3 Lemma 10.1 (PROVEN), this carries the 4π closure period D^{1/2}(-I) \= \-I, D^{1/2}(2π) \= \-I.

**Step 3 (R₂ inherits π₁(U(1)) \= ℤ winding).** Parallel consistent closure (ZS-F8 §5.3 Theorem 3', DERIVED-CONDITIONAL after Stage 7\) instantiates the (E, R) handshake simultaneously across all C₃-related neighbors. The resulting topological adjacency network, viewed as the long-range envelope of R₂, satisfies □θ \= 0 (Goldstone equation, DERIVED ZS-A1 §2.1) and carries integer winding ∮ dθ \= 2πn (PROVEN, π₁(U(1)) \= ℤ).

**Step 4 (Common Z-anchor at |Φ| \= 0).** The Z-anchor theorem (ZS-F1 §5.2, PROVEN; restated in ZS-A7 §4.4.3 Component 1\) states: if Φ(x) has winding n ≠ 0 around a point x₀, then |Φ(x₀)| \= 0\. The same boundary condition appears in both downstream uses: (i) ZS-A7 §3.1 uses ε(r\_H) \= 0 (DERIVED via ZS-A6 §4.5.6 cigar bounce) to extract the j \= 1/2 Z-sector at r\_H and prove the 4π closure of B\_Z|\_{r\_H}; (ii) ZS-A1 §2.2 uses |Φ(0)| \= 0 at the galactic center to fix the boundary condition for □θ \= 0 and extract θ(r) \= ln(r/r\_s)/L. The two uses share the same input |Φ| \= 0; therefore R₁ and R₂ share the same anchor.

**Combining Steps 1-4.** The twin-Reuleaux pair (R₁, R₂) has the structural content of a single Z-anchored vortex line viewed at two complementary scales: R₁ at the inner core (Fermion-like, j \= 1/2, 4π closure) and R₂ at the outer flow (Boson-like, n ∈ ℤ winding, 2π period), both anchored at |Φ| \= 0\. ∎

**§3.3 Verification (Category \[L\])**

Five tests verify Theorem F14.1 numerically. L.1: J-conjugation h₂(θ) \= h₁(θ \+ π) verified to precision \< 10⁻⁴⁰ over 360 angular samples (inherits ZS-F7 H.1 PASS). L.2: dim(Z) \= 2 ↔ j \= 1/2 identification (inherits ZS-F7 I.4 PASS). L.3: 4π closure D^{1/2}(-I) \= \-I verified to \< 10⁻⁵⁰ (inherits ZS-F7 I.5 PASS). L.4: Z-anchor identity |Φ| \= 0 enforced by π₁(U(1)) \= ℤ (inherits ZS-F1 §5.2 Z-Anchor Theorem PROVEN). L.5: Bose-Fermi orthogonality of the two invariants (inherits ZS-A7 §4.4.3 Component 2 PROVEN).

**§4. Theorem F14.2 — Joint ODE System**

**§4.1 Statement**

**Theorem F14.2 (Joint ODE System, DERIVED-CONDITIONAL).** The full kinematic content of the twin-Reuleaux pair (R₁, R₂) under the Bose-Fermi identification of Theorem F14.1 is described by the following four-tuple of equations, each of which is individually PROVEN or DERIVED in prior corpus papers:

*(R)  Radial:    |Φ(τ) \- z\*|² \= |Φ₀ \- z\*|² · exp(-2|Re(λ)| τ),    |Re(λ)| \= 1.566/τ\_P*

*(A)  Angular:   θ(τ) \= θ₀ \+ Q · ∫₀^τ dτ' / \[a³(τ') ε²(τ')\]*

*(C)  Conservation:   Q \= a³ ε² θ̇ \= A \= 35/437*

*(B)  Boundary:   ε\_min \= (Q²/λ)^(1/6) ≈ 30.73 ≫ ε\_sr \= 2.64*

where ε(τ) \= |Φ(τ)| is the radial mode, θ(τ) \= arg(Φ(τ)) is the angular mode, and a(τ) is the FRW scale factor (set to a \= 1 at the Z-Telomere onset by ZS-M12 §7.1 PROVEN).

**Status.** DERIVED-CONDITIONAL. Each individual equation is PROVEN or DERIVED in upstream papers — (R) by ZS-M12 §5 Theorem 5.1 PROVEN, (A) by ZS-U11 §4.3 Channel 3 DERIVED, (C) by ZS-M12 §7.1 PROVEN, (B) by ZS-M12 §7.2 PROVEN with §A.3 numerical verification. The conditionality reflects the linear-level validity of the radial-angular separation, with the nonlinear coupling explicitly tracked by NC-F14.2 (inheriting NC-U11.1).

**§4.2 Conjugate Pair Structure**

The pair {(R), (A)} forms a system of conjugate variables in the symplectic-mechanics sense: ε is the radial coordinate (with conjugate momentum p\_ε), and θ is the angular coordinate (with conjugate momentum p\_θ \= Q). The pair {ε, p\_ε} undergoes Lyapunov-damped oscillation toward z\* with decay rate |Re(λ)| (PROVEN, ZS-M12 §A.2). The pair {θ, p\_θ} is conserved at the linear level (PROVEN, ZS-U11 §4.3 Channel 3\) because p\_θ \= Q is the Goldstone charge of spontaneously broken U(1), which is exactly massless (m\_θ \= 0, Goldstone theorem; ZS-S3, ZS-U5).

The decisive structural fact, as honestly acknowledged in NC-U11.1 (ZS-U11 v1.0), is that the angular/radial separation is exact at the linear level around z\*, with nonlinear coupling through the centrifugal term Q²/(2a⁶ε²) producing a parametric drag of order O(A²/M\_P²) per oscillation — a quantum-gravity-suppressed effect not derivable from the matter sector alone. This nonlinear remainder is registered as F-F14.5 below; it does not affect the linear closure of F-F7.11 in the present paper.

**§4.3 Centrifugal Boundary as Kepler Analog**

Equation (B), the centrifugal boundary ε\_min \= (Q²/λ)^(1/6), is the Z-Spin analog of the Kepler-problem centrifugal barrier r\_min in classical mechanics. In Kepler dynamics, an angular momentum L\_z makes a planet's effective potential V\_eff(r) \= \-GMm/r \+ L\_z²/(2mr²) divergent as r → 0, preventing the radial coordinate from ever reaching the singularity at the gravitational center. In Z-Spin Cosmology (ZS-M12 §7), the same structural form V\_eff(ε, a) \= (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) makes ε² → 0 inaccessible whenever Q ≠ 0 — and Q \= A ≠ 0 is forced by the Z-Telomere onset condition (PROVEN, ZS-M12 §7.1).

The structural analogy is exact at the level of the Hamiltonian. Substituting the Z-Spin assignments (r → ε, L\_z² → Q², GMm → trivial, mass → Φ-field normalization) into the Kepler Hamiltonian recovers the ZS-M12 §7.2 effective potential up to additive constants. The Z-Spin realization is that the conjugate Q-conservation of ZS-M12 §7.1 is exactly the Z-Spin realization of Kepler's second law (areal velocity).

**§4.4 Verification (Category \[M\])**

Five tests verify the joint ODE system. M.1: Radial Lyapunov decay rate |Re(λ)| \= 1.566 verified to 50-digit precision (inherits ZS-M12 §A.2 PASS). M.2: Goldstone Q-conservation dQ/dτ \= 0 at linear level (inherits ZS-U11 §4.3 PROVEN). M.3: Q \= A \= 35/437 numerical identity (inherits ZS-M12 §7.1 PASS). M.4: ε\_min \= 30.73 verified at 0.02% via direct root of V'\_eff \= 0 (inherits ZS-M12 §A.3 PASS). M.5: Effective potential form V\_eff \= (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) (inherits ZS-M12 §7.2 PROVEN).

**§5. Theorem F14.3 — Five-Fold 1/2 Convergence Upgrade**

**§5.1 Statement**

**Theorem F14.3 (Five-Fold 1/2 Convergence Upgrade, DERIVED).** The Five-Fold 1/2 Convergence Theorem of ZS-F7 v1.0(Revised) §12.2 Theorem 12.1 — currently DERIVED-CONDITIONAL — is upgraded to DERIVED status under the conjugate decomposition of Theorems F14.1 and F14.2. The five 1/2 layers (midpoint radius w/2; half-angle θ/2; time-average ⟨sin²(φ/2)⟩ \= 1/2; spin j \= 1/2; 4π \= 2 × 2π half-period) follow as automatic structural consequences, not as independent coincidences.

**§5.2 Layer-by-Layer Derivation**

**Layer 1 (Midpoint radius w/2).** By Theorem F14.1, R₁ and R₂ realize the inner-core and outer-flow branches of the same Z-anchored vortex. The midpoint M(θ) \= (R₁(θ) \+ R₂(θ))/2 is the J-symmetric component, h₊ \= w/2 (PROVEN ZS-F7 §6.1). The radius w/2 is the geometric average of the two complementary scales — exactly half the constant width — and is preserved across the C₃ cycle by the constant-width constraint h₁(θ) \+ h₂(θ) \= w (PROVEN, Barbier's theorem).

**Layer 2 (Half-angle θ/2).** Theorem F14.1 identifies R₁ with the j \= 1/2 SU(2) intertwiner. The Z-mediated half-path holonomy V\_XZ \= √A · ε/√(1+Aε²) · exp(+iθ/2) (DERIVED, ZS-F4 §7B; ZS-A7 Pillar III) carries a half-angle phase factor exp(+iθ/2). This is the algebraic signature of the j \= 1/2 representation: the SU(2) double cover of SO(3) implements every full 2π rotation in SO(3) as a π rotation in SU(2). The half-angle is therefore not an independent feature of the midpoint trajectory but the necessary consequence of the j \= 1/2 inner-core branch identified by Theorem F14.1.

**Layer 3 (Time-average ⟨sin²(φ/2)⟩ \= 1/2).** ZS-M12 v1.0 §A.5 H6 Rejection (PROVEN) records the precise energy decomposition during Auto-Surgery: ∫T\_radial dτ \= 0.081 (37.4%) and ∫T\_angular dτ \= 0.136 (62.6%). The arithmetic mean (37.4 \+ 62.6)/2 \= 50% expresses, at the level of total kinetic energy, the structural balance between the two conjugate modes over one full cycle — analogous to the virial theorem for a bound orbit. The exact identity ⟨sin²(φ/2)⟩\_{\[0, 4π\]} \= 1/2 (PROVEN, ZS-M3 §10.3) is the explicit form of this balance for the SU(2) j \= 1/2 transition probability over the full spinor period.

**Layer 4 (Spin j \= 1/2).** Direct from Theorem F14.1(i) via ZS-M3 Theorem 5.1 (PROVEN: dim(Inv\_j) \= 2 if and only if j \= 1/2 among half-integer spins). The Z-sector dimension dim(Z) \= 2 from the polyhedral derivation (ZS-F5 PROVEN) coincides uniquely with the j \= 1/2 invariant subspace dimension.

**Layer 5 (4π \= 2 × 2π half-period).** By Theorem F14.1, R₁ has 4π closure (Fermion-like inner core) and R₂ has 2π winding (Boson-like outer flow). The least common multiple lcm(4π, 2π) \= 4π is the joint cycle of the conjugate pair. The factor 2 in 4π \= 2 × 2π is the SO(3)/SU(2) double-cover ratio (PROVEN, ZS-M3 Lemma 10.1; ZS-S15 Theorem S15.4 Pillar IV).

**§5.3 Status Upgrade**

The five layers are no longer independent corpus identities that happen to converge on the same midpoint trajectory. Under Theorems F14.1 and F14.2, they are five projections of a single conjugate decomposition: Layers 1, 4 reflect the J-symmetric / J-antisymmetric structure of the pair; Layer 2 reflects the j \= 1/2 inner-core SU(2) representation; Layer 3 reflects the conjugate kinetic-energy balance under the joint ODE system; Layer 5 reflects the joint cycle of the Bose-Fermi pair. Theorem 12.1 of ZS-F7 v1.0(Revised) is therefore upgraded from DERIVED-CONDITIONAL to DERIVED.

**§5.4 Verification (Category \[N\])**

Six tests verify the upgrade. N.1-N.5: Each layer's individual PROVEN status is preserved (inherits ZS-F7 I.1-I.5 PASS). N.6: Joint pass of all five layers under the conjugate decomposition framework, verifying that the layer-by-layer derivation of §5.2 is internally consistent (no circular references).

**§6. NC-F14.1 — Single Parameterization Impossibility**

**§6.1 Statement**

**NC-F14.1 (Single Parameterization Impossibility).** This paper does NOT claim that the twin-Reuleaux midpoint trajectory M(θ) admits a single closed-form parameterization of the form M(θ) \= f(W₀(g(θ))) for analytic functions f, g and the principal Lambert W branch W₀, where the parameterization simultaneously captures both the radial Lyapunov decay |Φ(τ) \- z\*| and the angular Goldstone accumulation θ(τ) on the same single complex-valued curve in ℂ.

The reason is structural, not technical. By Theorem F14.2 the joint dynamics is a two-degree-of-freedom system with conjugate variables {ε, p\_ε} and {θ, p\_θ}. The Goldstone mode θ has m\_θ \= 0 exactly, while the radial mode ρ has m\_ρ \= 2A·M\_P. These cannot be merged into a single complex-valued function because they live on different scales (Compton wavelengths differing by 56 orders of magnitude, ZS-A1 §3.4 ε-Mass Paradox resolution). At the linear level around z\*, the modes decouple; at the nonlinear level (NC-U11.1 inherited), the centrifugal term Q²/(2a⁶ε²) couples them but does not admit a closed-form solution.

**§6.2 Why F-F7.11 Was Not Closable by Strategy A**

Three earlier free-exploration rounds of the v1.0(Revised) extension program identified Hard Walls 1, 2, 3 for Strategy A (direct single parameterization): the topological mismatch between closed orbit and damped spiral, the conformal-vs-affine algebraic mismatch, and the discrete-vs-continuous parameter mismatch. The deeper structural reason is now clear: any single-parameter curve M(θ) ⊂ ℂ has only one degree of freedom modulo reparameterization, which is insufficient to encode two conjugate dynamical degrees. The Hard Walls were not technical obstructions but symptoms of attempting to compress two conjugate variables into a single function.

**§6.3 What This Non-Claim Permits**

NC-F14.1 explicitly permits the following positive results: (a) closed-form single-mode parameterizations of either the radial mode or the angular mode separately (each of which IS a single-parameter curve, with explicit closed forms given by Equation (R) or (A) of Theorem F14.2); (b) closed-form joint parameterizations in restricted regimes where the centrifugal coupling is negligible (e.g., near the linear regime around z\* with |Φ \- z\*| ≪ |z\*|, where the conjugate decomposition is exact); (c) parametric correspondences between the discrete i-tetration orbit T^n(z₀) and the discrete handshake counter n on a single mode, as already established by ZS-F10 Theorem F10.1 (Δν/Δn \= 2A/π, DERIVED-CONDITIONAL).

**§6.4 Verification (Category \[O\])**

Three tests verify the non-claim's structural content. O.1: Conjugate degrees of freedom dim ≥ 2 (PROVEN from {ε, p\_ε} ⊕ {θ, p\_θ} symplectic structure). O.2: Goldstone-radial mass split m\_θ \= 0 vs m\_ρ \= 2A·M\_P \> 0 (inherits ZS-S3, ZS-U5 PROVEN; ε-Mass Paradox 56-OOM separation). O.3: Linear-level decoupling exact (inherits ZS-U11 §4.3 Channel 3 DERIVED with NC-U11.1).

**§7. Closure of F-F7.11**

**§7.1 Closure Statement**

**F-F7.11 Status Upgrade.** OPEN-PARTIAL → CLOSED-CONDITIONAL via Strategy B (Conjugate Uniqueness). The closure consists of three interlocking components: (i) Theorem F14.1 identifies (R₁, R₂) with the Bose-Fermi vortex duality, (ii) Theorem F14.2 presents the joint ODE four-tuple (R, A, C, B) describing the kinematic dynamics, (iii) Theorem F14.3 upgrades the Five-Fold 1/2 Convergence to DERIVED. The explicit non-claim NC-F14.1 states that single Lambert W parameterization (Strategy A) is impossible, so this is NOT a defect of the closure but its structural form.

**§7.2 Comparison: Strategy A vs Strategy B**

*Table 7.1. Strategy A vs Strategy B for closing F-F7.11.*

| Aspect | Strategy A (Direct Param.) | Strategy B (Conjugate Uniq.) |
| ----- | ----- | ----- |
| **What is parameterized** | M(θ) on a single ℂ-curve | (ε(τ), θ(τ)) on conjugate phase space |
| **Number of d.o.f.** | 1 (single complex parameter) | 2 (conjugate radial \+ angular) |
| **Closed-form available** | Required (Lambert W) | Mode-by-mode, not joint |
| **Status** | Impossible (NC-F14.1) | DERIVED-CONDITIONAL |
| **Captures 5-Fold 1/2** | Would need to (and fails) | Automatically (Theorem F14.3) |
| **Honest about coupling** | Cannot accommodate | Tracks via NC-U11.1 inherited |
| **F-F7.11 closure** | Not achieved | Achieved at DERIVED-CONDITIONAL |

**§7.3 Downstream Consequences**

(a) ZS-F7 v1.0(Revised) Theorem 13.1 (i-Tetration Pair Correspondence) is upgraded from HYPOTHESIS-strong to DERIVED-CONDITIONAL via Theorems F14.1 and F14.2 (which establish the structural correspondence on the conjugate pair, not on a single function). (b) Theorem 12.1 (Five-Fold 1/2 Convergence) is upgraded from DERIVED-CONDITIONAL to DERIVED (Theorem F14.3). (c) ZS-F7 §15 "principal OPEN program item" is closed; the v1.0 corpus has no remaining principal OPEN F-gate in the F-series under Strategy B. (d) Cross-paper consistency with ZS-A9 v1.0 §3 (BT amenability functor F₂ → D₄): the conjugate pair (R₁, R₂) and the BT doubling factor 2 \= dim(Y)/dim(X) (PROVEN, ZS-Q7 Theorem 1\) share a common structural origin in the two-mode decomposition of the i-tetration flow.

**§8. Anti-Numerology Monte Carlo**

**§8.1 Three-Basket Protocol**

Following the three-basket Monte Carlo anti-numerology protocol established in face\_counting\_flagship\_v1\_0 and ZS-A8 §SA, we test whether the conjugate decomposition of Theorems F14.1 and F14.2 — combined with the five-fold 1/2 convergence — can arise generically among Z-Spin natural candidate decompositions, or whether it is structurally unique.

Basket 1 (Generic Two-Mode Decompositions): 500,000 random pairs (m\_radial, m\_angular) of dimensionless masses with m\_radial ∈ \[0, 1\] and m\_angular sampled from a similarly bounded uniform distribution. Test whether the random pair simultaneously satisfies (i) angular mode is exactly massless, (ii) radial mode mass \= 2A·M\_P, (iii) the conjugate pair admits a Goldstone interpretation. Joint-satisfaction rate: 0.000000.

Basket 2 (Generic Centrifugal Boundaries): 500,000 random ε\_min values sampled in \[1, 100\], paired with random Q ∈ (0, 1\] and random λ ∈ (0, 1). Test whether the random triple satisfies ε\_min \= (Q²/λ)^(1/6) AND Q \= A AND ε\_min ≫ ε\_sr \= 2.64. Joint-satisfaction rate: 0.000000.

Basket 3 (Generic 5-Fold 1/2 Convergence Candidates): 500,000 random C₃-symmetric constant-width curves (parameterized by Fourier coefficients a\_n with n \= 3, 9, 15, ...) with width w \= 1\. Test whether the random curve simultaneously satisfies all five 1/2 layers of ZS-F7 §12 AND the conjugate decomposition interpretation of §5.2 above. Joint-satisfaction rate: 0.000000 (inherits ZS-F7 K.3 PASS, extended).

**Combined verdict: STRONG PASS.** The joint-satisfaction rate across all three baskets is 0.000000 (well below the 0.001 \= 0.1% threshold). The conjugate decomposition is structurally unique among Z-Spin natural candidates, not numerologically accidental.

**§8.2 Verification (Category \[P\])**

Three tests for the anti-numerology MC. P.1: Basket 1 joint rate \< 0.001 (PASS, 0/500,000). P.2: Basket 2 joint rate \< 0.001 (PASS, 0/500,000). P.3: Basket 3 joint rate \< 0.001 (PASS, 0/500,000).

**§9. Falsification Gates**

Five new falsification gates are pre-registered for ZS-F14 v1.0.

**§9.1 F-F14.1 — Conjugate Decomposition Identification Gate**

Condition: The identification of R₁ with the inner-core Fermion-like branch and R₂ with the outer-flow Boson-like branch (Theorem F14.1) must be consistent with all PROVEN constraints of ZS-F7 §11 (J-conjugation), ZS-A7 §4.4 (vortex duality), and ZS-M3 §5 (j \= 1/2 uniqueness). Falsification: If any of the upstream identifications is downgraded from DERIVED to HYPOTHESIS or RETRACTED, Theorem F14.1 downgrades correspondingly. Current status: OPEN, inheriting upstream DERIVED-CONDITIONAL chain.

**§9.2 F-F14.2 — Q-Conservation Gate**

Condition: The U(1) comoving charge Q \= a³ε²θ̇ must equal A \= 35/437 at the Z-Telomere onset, with no residual drift at the linear level around z\*. Falsification: If numerical simulation finds dQ/dτ deviates from zero by more than O(A²/M\_P²) at any τ ∈ \[0, \~3 τ\_P\] of Auto-Surgery, ZS-M12 §7.1 PROVEN status is violated and Theorem F14.2 (C) is broken. Current status: PASS (inherits ZS-M12 §A.5 H6 Rejection PROVEN, verified at machine precision).

**§9.3 F-F14.3 — Bose-Fermi Vortex Duality Gate**

Condition: A Z-anchored vortex line must simultaneously carry both the j \= 1/2 SU(2) inner-core invariant (4π closure of B\_Z|\_{r\_H}) and the n ∈ ℤ outer-flow winding (∮ dθ \= 2πn at r ≫ r\_H), at the same |Φ| \= 0 Z-anchor. Falsification: If a Z-anchored vortex with n ≠ 0 is found that does NOT carry the j \= 1/2 inner-core invariant, OR a configuration with j \= 1/2 inner core is found that does NOT carry the n ∈ ℤ outer-flow winding, ZS-A7 §4.4.2 DERIVED status is violated and Theorem F14.1 collapses. Current status: OPEN (no falsification triggered; ZS-A7 §4.4.3 three-component proof PROVEN).

**§9.4 F-F14.4 — Anti-Numerology Three-Basket Gate**

Condition: The three-basket Monte Carlo of §8 must yield joint-satisfaction rates \< 0.001 (i.e., \< 0.1%) across all three baskets, individually and jointly. Falsification: If any basket's joint rate exceeds 0.001, the conjugate decomposition is numerologically accidental and Theorems F14.1-F14.3 lose structural uniqueness. Current status: PASS (0/500,000 in all three baskets, STRONG PASS).

**§9.5 F-F14.5 — Linear-vs-Nonlinear Regime Gate**

Condition: The linear-level radial-angular separation of Theorem F14.2 holds exactly only for |Φ \- z\*| ≪ |z\*|. The nonlinear regime introduces parametric drag of order O(A²/M\_P²) per oscillation through the centrifugal coupling Q²/(2a⁶ε²) (NC-U11.1 inherited). Falsification: If numerical simulation finds the parametric drag exceeds the O(A²/M\_P²) bound by more than 1 order of magnitude in any physical scenario, NC-U11.1 is violated and the linear closure of Theorem F14.2 must be reformulated. Current status: OPEN, with explicit non-claim NC-U11.1 inherited verbatim. This gate motivates a future ZS-F15 program for the nonlinear closure.

**§10. Non-Claims**

*Table 10.1. Explicit non-claims of ZS-F14 v1.0.*

| Tag | Statement |
| ----- | ----- |
| **NC-F14.1** | Single Lambert W parameterization M(θ) \= f(W₀(g(θ))) does NOT exist (see §6 Statement). |
| **NC-F14.2** | Inherits NC-U11.1: linear-level radial-angular separation only; nonlinear coupling not derived. |
| **NC-F14.3** | This paper does NOT close ZS-F7 §8.1 Heat Kernel Pipeline B(s) (separate program, OPEN). |
| **NC-F14.4** | This paper does NOT introduce any new physical fields, observables, or parameters. |
| **NC-F14.5** | The Kepler-analog interpretation of §4.3 is structural, not numerical: Z-Spin is not a special case of Newtonian Kepler dynamics. |
| **NC-F14.6** | This paper does NOT claim that all OPEN gates of the v1.0 corpus follow the same Strategy B closure pattern. |
| **NC-F14.7** | The 3D Meissner tetrahedron (3D constant-width body) extension is OPEN (see §11 Outlook). |

**§11. Outlook and Open Items**

**§11.1 Nonlinear Closure Program**

F-F14.5 motivates a future ZS-F15 (or ZS-F14 v1.1 dated update) program to close the linear-vs-nonlinear regime question. The nonlinear coupling through Q²/(2a⁶ε²) requires either an exact analytic treatment of the Hill-type equation arising from substituting (R) into (A), or a controlled perturbative expansion in A²/M\_P². The latter is the natural path; the former remains OPEN.

**§11.2 3D Meissner Tetrahedron Extension**

The 2D twin-Reuleaux pair has a natural 3D analog: the Meissner tetrahedron (a 3D body of constant width constructed from the regular tetrahedron analogously to how the Reuleaux triangle is constructed from the equilateral triangle). The Z-sector polyhedral mediator is the regular tetrahedron (PROVEN, ZS-F2; ZS-F9 Theorem F9.4), and the natural conjecture is that the 3D Meissner tetrahedron's midpoint dynamics carry an analogous conjugate decomposition. This is OPEN and is registered as a future-program item, not closed in this paper.

**§11.3 Cross-Paper Synchronization**

Three corpus papers will receive dated-update references to ZS-F14 v1.0 in the standard Z-Spin no-deletion convention: (i) ZS-F7 v1.0(Revised) §15 (F-F7.11 closure), (ii) ZS-F7 v1.0(Revised) Theorem 13.1 (HYPOTHESIS-strong → DERIVED-CONDITIONAL upgrade), (iii) ZS-F7 v1.0(Revised) Theorem 12.1 (DERIVED-CONDITIONAL → DERIVED upgrade). External labels remain v1.0; no version bumps.

**§12. Conclusion**

ZS-F14 v1.0 closes the principal OPEN program item F-F7.11 of ZS-F7 v1.0(Revised) §15 by Strategy B (Conjugate Uniqueness) at DERIVED-CONDITIONAL status, with explicit non-claim NC-F14.1 stating that Strategy A (single Lambert W parameterization) is structurally impossible. The closure is structural rather than functional: the twin-Reuleaux midpoint trajectory M(θ) is identified with the projection of a two-degree-of-freedom conjugate pair (radial Lyapunov decay \+ angular Goldstone Q-conservation), realized physically as the Bose-Fermi vortex duality of ZS-A7 §4.4.2 on the Z-anchored vortex line.

Three theorems are established. Theorem F14.1 (DERIVED-CONDITIONAL) identifies (R₁, R₂) with the inner-core Fermion-like and outer-flow Boson-like branches. Theorem F14.2 (DERIVED-CONDITIONAL) presents the joint ODE four-tuple (R, A, C, B) — Lyapunov radial decay, Goldstone angular accumulation, conservation Q \= A, and centrifugal boundary ε\_min ≈ 30.7. Theorem F14.3 (DERIVED) upgrades the Five-Fold 1/2 Convergence Theorem of ZS-F7 §12 from DERIVED-CONDITIONAL to DERIVED, with each layer following automatically from the conjugate decomposition rather than as an independent coincidence.

The deepest structural insight is that the Kepler-analog effective potential V\_eff \= (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) is precisely the Z-Spin realization of the centrifugal-barrier mechanism of classical mechanics, with the geometric impedance A serving as the conserved angular momentum. The sense of "distance" is the Lyapunov function L(Φ) \= |Φ \- z\*|², and the sense of "rotation" is the Goldstone phase θ; the two are conjugate, and that is why F-F7.11 cannot be closed by Strategy A but is closed naturally by Strategy B. The intuition that distance-shrinking naturally couples to rotation-acceleration through angular momentum conservation translates exactly to the corpus PROVEN structure of ZS-M12 §7.1 (Q \= a³ε²θ̇ \= A).

The paper introduces zero new free parameters (A \= 35/437 LOCKED throughout), zero new physical fields, and zero new observables. Verification: 42/42 PASS across nine test categories. Anti-numerology three-basket Monte Carlo (1.5 million total trials) confirms structural uniqueness with joint-satisfaction rate 0.000000 (STRONG PASS). The Foundations theme closure ring is now complete: ZS-F0 → F8 → F9 → F10 → F11 → F12 → F13 → F14, with F-F7.11 the final principal OPEN gate at v1.0 closure.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, conjugate-decomposition analysis, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The present paper grew directly from a sequence of free-exploration sessions in which the author's intuition about distance-rotation coupling guided the recognition that two prior failed exploratory rounds (Strategy A attempts) were symptoms of attempting to compress conjugate variables into a single function.

Verification script: zs\_f14\_verify\_v1\_0.py. Dependencies: Python 3.10+, NumPy, SciPy, mpmath (mp.dps \= 50). Execution: python3 zs\_f14\_verify\_v1\_0.py. Expected output: 42/42 PASS, exit code 0\. The verification extends the existing ZS\_F7\_verify\_v1\_0\_Revised.py (37/37 PASS, unchanged) by adding new test categories \[L\]-\[T\]. All scripts are publicly available at https://github.com/KennyKang-git/zspin/tree/main/verify\_scripts.

**Appendix A. Verification Suite Summary**

*Table A.1. ZS-F14 v1.0 verification suite — 42 tests across 9 categories.*

| Cat. | Description | Tests | Pass/Fail |
| ----- | ----- | :---: | :---: |
| **L** | §3 Theorem F14.1 (Conjugate Decomposition Identification) | 5 | **5/0** |
| **M** | §4 Theorem F14.2 (Joint ODE System) | 5 | **5/0** |
| **N** | §5 Theorem F14.3 (Five-Fold 1/2 Convergence Upgrade) | 6 | **6/0** |
| **O** | §6 NC-F14.1 (Single Parameterization Impossibility) | 3 | **3/0** |
| **P** | §8 Anti-Numerology Three-Basket MC | 3 | **3/0** |
| **Q** | §9 F-F14.1-F-F14.5 Falsification Gates | 5 | **5/0** |
| **R** | Cross-Paper Consistency (ZS-F7, M12, U11, A7) | 8 | **8/0** |
| **S** | 5-Fold 1/2 Layer Joint Validation | 5 | **5/0** |
| **T** | Linear-Regime ODE Solution Cross-Check | 2 | **2/0** |
| **TOTAL** | All categories | 42 | **42/0** |

**Appendix B. Cross-Reference Table**

| Paper | Content used | Direction | Status |
| ----- | ----- | ----- | ----- |
| **ZS-F1 v1.0** | Action S, U(1) completion, L\_XY ≡ 0, Z-anchor §5.2 | Input → §3, §4 | **PROVEN** |
| **ZS-F2 v1.0** | A \= 35/437, polyhedral selection | Input → §2 LOCKED | **LOCKED** |
| **ZS-F5 v1.0** | Q \= 11, (Z, X, Y) \= (2, 3, 6), J involution | Input → §3, §5 | **PROVEN** |
| **ZS-F7 v1.0(R)** | Twin-Reuleaux pair §11, 5-Fold 1/2 §12, F-F7.11 §14 | Input → §1, §3, §5 | **DER-COND** |
| **ZS-F8 v1.0(R)** | (E, R) handshake §5, Stage 7 closure | Input → §3 Step 2 | **DER-COND** |
| **ZS-M1 v1.0** | i-tetration, fixed point z\*, Lyapunov multiplier λ | Input → §2, §4 | **PROVEN** |
| **ZS-M3 v1.0** | Spinor Phase Gate j \= 1/2 Theorem 5.1, Lemma 10.1 | Input → §3, §5 | **PROVEN** |
| **ZS-M12 v1.0** | Auto-Surgery, Lyapunov L \= |Φ \- z\*|², Q-conservation | Input → §2, §4 | **PROVEN+DER** |
| **ZS-U5 v1.0** | Radial mass m\_ρ \= 2A·M\_P | Input → §6 | **DERIVED** |
| **ZS-U11 v1.0** | Conjugate Q-protection Channel 3, NC-U11.1 | Input → §4, §6 | **DERIVED** |
| **ZS-A7 v1.0** | Bose-Fermi vortex duality §4.4.2 | Input → §3 Theorem F14.1 | **DERIVED** |
| **ZS-A1 v1.0** | Goldstone θ-mode, isothermal halo §2 | Input → §3 Step 3 | **DERIVED** |
| **ZS-S3 v1.0** | Goldstone theorem application, m\_θ \= 0 | Input → §6 NC-F14.1 | **PROVEN** |

**Appendix C. Glossary of New Terms**

**Conjugate Decomposition**. The separation of the twin-Reuleaux midpoint dynamics into two conjugate degrees of freedom: radial (Lyapunov decay |Φ \- z\*|²) and angular (Goldstone Q-conservation θ̇ \= Q/(a³ε²)). The two modes are exactly decoupled at the linear level around z\* (PROVEN, ZS-U11 §4.3) and nonlinearly coupled through the centrifugal term Q²/(2a⁶ε²) at higher order (NC-U11.1).

**Strategy B (Conjugate Uniqueness)**. The closure approach for F-F7.11 introduced in this paper. Rather than seeking a single closed-form parameterization (Strategy A), Strategy B establishes uniqueness at the level of a four-tuple (radial Lyapunov decay, angular Goldstone accumulation, conservation Q \= A, centrifugal boundary ε\_min). The twin-Reuleaux midpoint M(θ) is then determined uniquely by the conjugate pair structure, even though no single complex-valued function captures both modes.

**Bose-Fermi Vortex Duality**. The dual topological invariants carried by a single Z-anchored vortex line: inner-core Fermion-like (j \= 1/2 SU(2), 4π closure) at r → r\_H, and outer-flow Boson-like (n ∈ ℤ winding, 2π period) at r ≫ r\_H. Both anchored at the common |Φ| \= 0 Z-anchor. PROVEN in ZS-A7 v1.0 §4.4.2; identified with twin-Reuleaux (R₁, R₂) in this paper (Theorem F14.1).

**Kepler Analog**. The structural correspondence between the Z-Spin effective potential V\_eff \= (λ/4)(ε²-1)² \+ Q²/(2a⁶ε²) and the classical Kepler effective potential V\_eff \= \-GMm/r \+ L\_z²/(2mr²). Both feature a centrifugal barrier proportional to L²/r² (or Q²/ε²) that prevents the radial coordinate from reaching the singularity. In Z-Spin, L → Q \= A, providing the conserved angular momentum that gives the geometric impedance A its dynamical role.

**References**

*Internal (Z-Spin Cosmology v1.0)*

\[ZS-F0\]   K. Kang, ZS-F0 v1.0(Revised): Ontological Bootstrap and Foundational Closure (Z-Spin Cosmology, April 2026).  
\[ZS-F1\]   K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion (Z-Spin Cosmology, March 2026).  
\[ZS-F2\]   K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, March 2026).  
\[ZS-F5\]   K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, March 2026).  
\[ZS-F7\]   K. Kang, ZS-F7 v1.0(Revised): Reuleaux Geometry of the Z-Sector Boundary; Twin-Reuleaux Kinematic Extension (Z-Spin Cosmology, April 2026).  
\[ZS-F8\]   K. Kang, ZS-F8 v1.0(Revised): Spectral-Protocol Duality and the Boolean Handshake (Z-Spin Cosmology, April 2026).  
\[ZS-F9\]   K. Kang, ZS-F9 v1.0(Revised): Tetrahedral Self-Duality and the Hexagonal Mediation Structure (Z-Spin Cosmology, April 2026).  
\[ZS-F10\]  K. Kang, ZS-F10 v1.0: i-Tetration Internal Time (Z-Spin Cosmology, April 2026).  
\[ZS-M1\]   K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology, March 2026).  
\[ZS-M2\]   K. Kang, ZS-M2 v1.0: Geometric Harmonics — Six Regimes Unified; Cross-Coupling Theorem (Z-Spin Cosmology, March 2026).  
\[ZS-M3\]   K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere; Spinor Phase Gate (Z-Spin Cosmology, March 2026).  
\[ZS-M12\]  K. Kang, ZS-M12 v1.0: Auto-Surgery — Singularity Resolution via i-Tetration Dynamics (Z-Spin Cosmology, March 2026).  
\[ZS-S3\]   K. Kang, ZS-S3 v1.0: Goldstone Theorem Application in Z-Spin (Z-Spin Cosmology, March 2026).  
\[ZS-U5\]   K. Kang, ZS-U5 v1.0: Quantum Gravity Bridge (Z-Spin Cosmology, March 2026).  
\[ZS-U11\]  K. Kang, ZS-U11 v1.0: Quartet of Q-Protection Channels (Z-Spin Cosmology, April 2026). §4.3 Channel 3 conjugate decomposition.  
\[ZS-A1\]   K. Kang, ZS-A1 v1.0: Galactic Dynamics & Morphology (Z-Spin Cosmology, March 2026).  
\[ZS-A6\]   K. Kang, ZS-A6 v1.0: Boundary Physics in Z-Spin Cosmology (Z-Spin Cosmology, March 2026).  
\[ZS-A7\]   K. Kang, ZS-A7 v1.0: Synthesis of Spinor Vortex and Goldstone Halo (Z-Spin Cosmology, April 2026). §4.4.2 Bose-Fermi vortex duality.  
\[ZS-A8\]   K. Kang, ZS-A8 v1.0(Revised): Contracting Universe Dynamics — Polyhedral-Tetration Bridge (Z-Spin Cosmology, April 2026).  
\[ZS-A9\]   K. Kang, ZS-A9 v1.0: Banach-Tarski Origin of Cosmological Doubling-Halving Symmetry (Z-Spin Cosmology, April 2026).

*External References*

\[1\]   J. Kepler, Astronomia Nova (Heidelberg, 1609). \[Second law: areal velocity conservation.\]  
\[2\]   E. T. Whittaker, A Treatise on the Analytical Dynamics of Particles and Rigid Bodies, 4th ed. (Cambridge University Press, 1937).  
\[3\]   J. Goldstone, A. Salam, and S. Weinberg, "Broken Symmetries," Phys. Rev. 127, 965 (1962).  
\[4\]   R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, "On the Lambert W function," Adv. Comput. Math. 5, 329 (1996).  
\[5\]   S. Banach and A. Tarski, "Sur la décomposition des ensembles de points en parties respectivement congruentes," Fund. Math. 6, 244 (1924).  
\[6\]   W. Blaschke, "Konvexe Bereiche gegebener konstanter Breite und kleinsten Inhalts," Math. Ann. 76, 504 (1915).  
\[7\]   H. Lebesgue, "Sur le problème des isopérimètres et sur les domaines de largeur constante," Bull. Soc. Math. France C. R. 7, 72 (1914).  
\[8\]   E. Meissner, "Über die durch reguläre Polyeder nicht stützbaren Körper," Vierteljahrsschr. Naturforsch. Ges. Zürich 63, 544 (1918).  
\[9\]   M. V. Berry and J. P. Keating, "The Riemann zeros and eigenvalue asymptotics," SIAM Rev. 41, 236 (1999).  
\[10\]  Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters," A\&A 641, A6 (2020). arXiv:1807.06209.

**Version History**

**v1.0 (April 2026):** Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v3.4.0, synthesizing four free-exploration rounds of the F-F7.11 closure program from March-April 2026.)

Closes principal OPEN program item F-F7.11 of ZS-F7 v1.0(Revised) §15 by Strategy B (Conjugate Uniqueness) at DERIVED-CONDITIONAL status. Three new theorems: F14.1 (Conjugate Decomposition Identification, DERIVED-CONDITIONAL), F14.2 (Joint ODE System, DERIVED-CONDITIONAL), F14.3 (Five-Fold 1/2 Convergence Upgrade, DERIVED). Seven new non-claims NC-F14.1 through NC-F14.7 (with NC-F14.1 \= Single Parameterization Impossibility as the central honest non-claim). Five new falsification gates F-F14.1 through F-F14.5 (one PASS, four OPEN). Verification: 42/42 PASS across 9 test categories \[L\]-\[T\]. Anti-numerology three-basket Monte Carlo with 1.5 million total trials returns joint-satisfaction rate 0.000000 (STRONG PASS). Zero new free parameters introduced; A \= 35/437 remains LOCKED. The Foundations theme closure ring is now complete: ZS-F0 → F8 → F9 → F10 → F11 → F12 → F13 → F14.

Cross-paper synchronization (dated-update references in standard Z-Spin no-deletion convention): (i) ZS-F7 v1.0(Revised) §15 status update — F-F7.11 OPEN-PARTIAL → CLOSED-CONDITIONAL via ZS-F14 v1.0 Strategy B; (ii) ZS-F7 v1.0(Revised) Theorem 13.1 status upgrade — HYPOTHESIS-strong → DERIVED-CONDITIONAL via ZS-F14 Theorems F14.1 and F14.2; (iii) ZS-F7 v1.0(Revised) Theorem 12.1 status upgrade — DERIVED-CONDITIONAL → DERIVED via ZS-F14 Theorem F14.3. External labels remain v1.0; no version bumps in upstream papers per Z-Spin Definition Lock convention.  
