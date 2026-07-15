**ZS-Q7: Structural Arrow of Time from the Z-Bottleneck:**  
**Entropy Production without a Past Hypothesis**

Kenny Kang  
March 2026  
Theme: Quantum Mechanics \[ZS-Q\] | Paper 7 | Code: ZS-Q7 v1.0

**Verification: 33/33 PASS | Zero Free Parameters**

**§0. Abstract**

We derive a structural arrow of time within Z-Spin cosmology from the single geometric impedance A \= 35/437 with zero new parameters. The derivation proceeds in four stages: (1) unitary evolution on the full Hilbert space H\_X ⊗ H\_Z ⊗ H\_Y, (2) Stinespring dilation yielding a CPTP channel (ZS-Q1 v1.0 §3.3, PROVEN), (3) Lindblad master equation with Γ \= 2A(ΔE/ℏ)² (ZS-Q1 v1.0 §3.4, DERIVED), and (4) sector coarse-graining to a Pauli master equation. The Born-Markov approximation is quantitatively justified by the validity parameter ε\_BM \= τ\_fast/τ\_slow \= 2/Q \= 2/11 ≪ 1, a purely geometric ratio.

Three theorems are established: (I) the Dimension Ratio Theorem (PROVEN): Γ(X→Y)/Γ(Y→X) \= dim(Y)/dim(X) \= 2 is an exact mathematical identity from trace cyclicity; (II) the Z-Bottleneck Channel Bound (DERIVED): rank(T\_XY) ≤ dim(Z) \= 2 and channel capacity ≤ ln(2); (III) the Z-Mediated Master Equation (DERIVED): D\_KL(p || p\_eq) is a monotonically decreasing Lyapunov function with Schnakenberg entropy production σ ≥ 0 everywhere.

(IIIA) The Exact Eigenvalue Theorem (DERIVED): the characteristic polynomial factorizes as λ(λ \+ 2A/Q)(λ \+ A) \= 0, giving τ\_fast \= 1/A exactly—coinciding with the decoherence ratio τ\_D/τ\_Penrose from ZS-Q1 v1.0. The physical time scale is τ\_D \= ℏ/(A·E\_diff), providing concrete predictions: for gold nanospheres (10⁹ amu), τ\_relax ≈ 474 days.

The resulting Structural Arrow produces entropy ΔS \= ln(2) per Z-mediated transition without a Past Hypothesis. The non-uniform equilibrium p\_eq \= (3, 2, 6)/11 reflects gravitational entropy dominance—the Y-sector (dim \= 6\) carries twice the state density of the X-sector (dim \= 3), geometrically realizing Penrose’s intuition. The Cosmological Closure Mapping (§5.8) derives all 8 Z-Sim closure parameters from the master equation, eliminating all phenomenological freedom. Zero free parameters, 7 falsification gates, 5 non-claims, 33-test verification suite with 100% pass rate.

**Epistemic Status Legend**

| STATUS | DEFINITION | EXAMPLE | FALSIFIABLE? |
| ----- | ----- | ----- | ----- |
| PROVEN | Mathematical theorem from (Z,X,Y)=(2,3,6) | Γ ratio \= 2 | Only by logic error |
| DERIVED | Conditional on Z-Spin action being correct | dD\_KL/dt ≤ 0 | Yes (experiment) |
| NON-CLAIM | Explicitly excluded from scope | NC-Q7.1–5 | N/A |
| LOCKED | Input fixed from prior paper | A \= 35/437 | N/A |
| VERIFIED | Numerically confirmed to stated precision via verification suite | Eigenvalue factorization | By code failure |
| CONSISTENT | Cross-paper consistency check; not an independent derivation | Wald entropy | By contradiction |
| OPEN | Recognized gap requiring future work | Spectral gap | N/A |
| BLOCKING | Gate that would invalidate the paper if triggered | F-Q7.6 | Yes (structural) |
| PASSING | Gate currently satisfied by verification suite | F-Q7.4, F-Q7.7 | Yes (computational) |

**§1. Introduction**

**1.1 The Arrow of Time Problem**

The fundamental laws of physics are time-reversal symmetric at the microscopic level, yet the macroscopic world exhibits a profound asymmetry: entropy increases, eggs break but do not unbreak. This tension between microscopic reversibility and macroscopic irreversibility is the arrow of time problem.

Three principal approaches exist. Boltzmann’s H-theorem requires a low-entropy initial state but cannot explain why it was special. Penrose’s Weyl Curvature Hypothesis invokes the Past Hypothesis as an additional postulate. Carroll’s “Mad-Dog Everettian” approach embeds the arrow in quantum branching but involves untestable multiverse claims. All three require either special initial conditions or additional postulates beyond the dynamical laws.

**1.2 The Z-Spin Approach: Structural Asymmetry**

Z-Spin cosmology offers a fundamentally different resolution. The sector decomposition Q \= Z \+ X \+ Y \= 2 \+ 3 \+ 6 \= 11 (PROVEN, ZS-F5 v1.0) with L\_XY ≡ 0 (PROVEN, ZS-F1 v1.0) creates a structural asymmetry: the Y-sector (dim \= 6\) has twice the dimension of the X-sector (dim \= 3), and all transitions must pass through the Z-sector (dim \= 2\) bottleneck. This is not an initial condition but a geometric property of the theory itself.

**1.3 Scope and Relation to ZS-A6**

ZS-A6 v1.0 §6 introduced the structural arrow as a corollary. This paper elevates it to a self-contained treatment with five new contributions: (1) a rigorous derivation chain from unitary dynamics to the master equation (§5.0), (2) proof that the transition rate ratio is a mathematical identity (Theorem 1), (3) the Z-Bottleneck Channel Bound (Theorem 2), (4) the complete Pauli master equation with KL divergence as the correct Lyapunov function (Theorem 3), and (5) exact analytical eigenvalues with physical time scale identification (Theorem 3A).

**§2. Locked Inputs**

All quantities are locked from prior papers. Zero new parameters are introduced.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z, X, Y) dimensions | (2, 3, 6); Q \= 11 | ZS-F5 v1.0 | PROVEN |
| L\_XY | ≡ 0 (exact) | ZS-F1 v1.0 | PROVEN |
| κ (coupling) | √(A/Q) \= 0.08533 | ZS-S1 v1.0 | DERIVED |
| τ\_D (decoherence time) | ℏ / (A · E\_diff) | ZS-Q1 v1.0 §5.1 | DERIVED |
| Γ (Lindblad rate) | 2A(ΔE/ℏ)² | ZS-Q1 v1.0 §3.4 | DERIVED |

**§3. Theorem 1: Dimension Ratio Identity \[PROVEN\]**

**3.1 Statement and Proof**

**Theorem 1 (Dimension Ratio Identity).** For any linear map T: H\_A → H\_B with dim(H\_A) \= d\_A, dim(H\_B) \= d\_B, the uniform-averaged transition rate ratio is:

Γ(A→B) / Γ(B→A) \= d\_B / d\_A                    (1)

***Proof.*** By trace cyclicity, Tr(T†T) \= Σ\_k σ²\_k \= Tr(TT†). Therefore Γ(A→B)/Γ(B→A) \= \[Tr(T†T)/d\_A\] / \[Tr(TT†)/d\_B\] \= d\_B/d\_A. □

**\[STATUS: PROVEN\] Pure mathematical identity. No physics assumptions required. Variance \= 0 across 10⁴ random matrices.**

**3.2 Key Insight**

Theorem 1 holds for any linear map T between any two Hilbert spaces. The ratio 2 is a mathematical certainty, not a statistical averaging result. Z-Spin’s contribution is not the ratio itself, but the mechanism (L\_XY \= 0\) that makes this ratio the only physical pathway.

**§4. Theorem 2: Z-Bottleneck Channel Bound \[DERIVED\]**

**Theorem 2\.** If L\_XY ≡ 0, then T\_XY \= V\_ZY · V\_XZ, so rank(T\_XY) ≤ dim(Z) \= 2 and channel capacity ≤ ln(2).

***Proof.*** L\_XY \= 0 prohibits first-order X→Y propagation. Heat kernel: ||K\_XY(t)|| \~ t² (ZS-M6 v1.0 §4.5). All paths factor X→Z→Y, forcing rank(T\_XY) ≤ dim(Z) \= 2\. □

**\[STATUS: DERIVED\] From L\_XY \= 0 (PROVEN) \+ Block Laplacian structure.**

Physical consequences: (i) information channel capacity ≤ ln(2) ≈ 1 bit; (ii) shortcut prohibition (L\_XY \= 0 blocks bypass); (iii) irreversible information loss (3-dim info through 2-dim bottleneck). Theorem 1 determines the magnitude (ratio \= 2); Theorem 2 provides the mechanism (Z-bottleneck) that forces this asymmetry to be physically realized.

**§5. Theorem 3: Z-Mediated Master Equation \[DERIVED\]**

**§5.0 From Unitary Evolution to Master Equation**

A critical question arises: the full universe evolves unitarily, yet we employ an irreversible master equation. This section demonstrates that the master equation is not an assumption but a derived consequence of unitary dynamics plus coarse-graining. The derivation proceeds in four steps:

**Step 0 (Full Hilbert space):** H\_total \= H\_X ⊗ H\_Z ⊗ H\_Y (dim \= 36). H \= H\_X \+ H\_Z \+ H\_Y \+ V\_XZ \+ V\_ZY, with V\_XY \= 0 from L\_XY ≡ 0\.

**Step 1 (Stinespring → CPTP):** ρ\_X(t) \= Tr\_{Z,Y}\[U(t) ρ(0) U†(t)\]. By ZS-Q1 v1.0 §3.3, this yields a CPTP channel with dim(Z) \= 2 Kraus operators.

**Step 2 (SSE → Lindblad):** F(ε) \= 1 \+ Aε² generates stochastic phase kicks. dρ/dt \= −(i/ℏ)\[H, ρ\] \+ Γ(σ\_z ρ σ\_z − ρ) with Γ \= 2A(ΔE/ℏ)².

**Step 3 (Sector coarse-graining → Pauli master equation):** dp/dt \= M·p with W\_AB \= dim(B) × A/Q from Fermi’s golden rule.

**5.0.1 Born-Markov Approximation: Quantitative Justification**

ε\_BM \= τ\_fast / τ\_slow \= 2/Q \= 2/11 ≈ 0.18                    (4)

This ratio is purely geometric—it depends only on Q \= 11, not on A or any dynamical parameter. For Q → ∞, ε\_BM → 0 and the Markov approximation becomes exact.

**5.1 Construction**

dp\_X/dt \= −W\_XZ p\_X \+ W\_ZX p\_Z                    (5a)

dp\_Z/dt \= W\_XZ p\_X − (W\_ZX \+ W\_ZY) p\_Z \+ W\_YZ p\_Y                    (5b)

dp\_Y/dt \= W\_ZY p\_Z − W\_YZ p\_Y                    (5c)

with rates W\_AB \= dim(B) × A/Q. The ratio W\_ZY/W\_ZX \= dim(Y)/dim(X) \= 2 is Theorem 1 realized within the master equation.

**5.2 Equilibrium Distribution**

**p\_eq \= (dim\_X, dim\_Z, dim\_Y)/Q \= (3, 2, 6)/11                    (6)**

This is not the uniform distribution (1/3, 1/3, 1/3). The Y-sector (gravity, dim \= 6\) carries 54.5% of the probability, reflecting the dominance of gravitational degrees of freedom.

**5.3 KL Divergence as Lyapunov Function**

**Theorem 3 (KL Monotonicity).** D\_KL(p(t) || p\_eq) is a monotonically decreasing function of time:

dD\_KL/dt ≤ 0,     equality iff p \= p\_eq                    (7)

**\[STATUS: DERIVED\] From Fermi golden rule \+ L\_XY \= 0 \+ microscopic reversibility.**

**5.4 Shannon Entropy Is NOT the Correct Lyapunov Function**

Because p\_eq \= (3, 2, 6)/11 is non-uniform, Shannon entropy S(p) \= −Σ p\_i ln p\_i is not monotonically increasing. Starting from p \= (1, 0, 0), Shannon entropy rises to S ≈ 1.040 (overshooting S\_eq ≈ 0.995) before decreasing. The correct potential is D\_KL, which monotonically decreases. The Schnakenberg entropy production σ \= ½ Σ (J\_αβ − J\_βα) ln(J\_αβ/J\_βα) ≥ 0 provides a complementary guarantee.

**5.5 Theorem 3A: Exact Eigenvalue Factorization**

**Theorem 3A (Exact Eigenvalues).** The characteristic polynomial of the transition matrix M factorizes as:

**λ(λ \+ 2A/Q)(λ \+ A) \= 0                    (8)**

with eigenvalues λ₀ \= 0, λ₁ \= −2A/Q, λ₂ \= −A and relaxation timescales:

τ₀ \= ∞ (stationary),     τ\_slow \= Q/(2A),     τ\_fast \= 1/A                    (9)

**Physical interpretation:** (i) τ\_fast \= 1/A \= 437/35 \= 12.4857... coincides exactly with τ\_D/τ\_Penrose from ZS-Q1 v1.0. (ii) λ₁ \= −2A/Q governs inter-sector thermalization, slower by Q/2 \= 5.5. (iii) ε\_BM \= |λ₁|/|λ₂| \= 2/Q \= 2/11 is purely geometric.

**5.6 Physical Time Scale**

τ\_D \= ℏ / (A · E\_diff)                    (10)

Concrete predictions for gold nanospheres (10⁹ amu, R ≈ 50 nm):

| Quantity | Value | Timescale |
| ----- | ----- | ----- |
| τ\_Penrose | ℏ/E\_diff | ≈13.3 hours |
| τ\_D (Z-Spin decoherence) | τ\_Pen / A | ≈6.9 days |
| τ\_fast (bottleneck relaxation) | τ\_D / A \= τ\_Pen / A² | ≈86 days |
| τ\_slow (thermalization) | (Q/2) × τ\_fast | ≈474 days |

**5.7 Entropy Production Rate**

dS\_Z/dt ∝ A × (dim\_X/Q) × ln(dim\_Y/dim\_X) \= (35/437) × (3/11) × ln(2) ≈ 0.01514 nats/transition                    (12)

**5.8 Cosmological Closure Mapping**

The Pauli master equation with W\_AB \= dim(B)·A/Q provides a complete, parameter-free specification of cosmological sector energy exchange. Matching coefficients: γ\_xz \= 2A/Q \= 0.01456, α\_xz \= dim(X)/dim(Z) \= 3/2, γ\_zy \= 6A/Q \= 0.04369, α\_zy \= dim(Z)/dim(Y) \= 1/3. The ratio γ\_zy/γ\_xz \= 3 \= dim(Y)/dim(Z) is structural. Equilibrium initial conditions: p\_eq \= (3, 2, 6)/11. All 8 Z-Sim closure parameters are now DERIVED. \[STATUS: DERIVED\]

**§6. Corollary: Structural Arrow of Time \[DERIVED\]**

**6.1 Synthesis**

Combining Theorems 1–3A: (i) D\_KL monotonically decreases from any initial state (Thm 3). (ii) Net probability current flows X→Y through Z with rate ratio 2:1 (Thm 1). (iii) No shortcut bypasses the Z-bottleneck (Thm 2). (iv) Each Z-mediated transition produces ΔS \= ln(2). (v) Relaxation occurs on timescale τ\_D with exact eigenvalues λ \= 0, −2A/Q, −A (Thm 3A).

**6.2 Past Hypothesis Unnecessary**

Whether the universe began in a low-entropy state, high-entropy state, or random state, the asymmetric relaxation toward p\_eq occurs identically. The arrow is not a consequence of where the universe started but of how the state space is structured.

**6.3 Rapidity Asymmetry**

The curvature rapidities ψ\_X \= artanh(5/19) \= 0.2695 and ψ\_Y \= artanh(7/23) \= 0.3143 satisfy Δψ \= 0.0448 \> 0 \[PROVEN\]. The Y-sector carries more curvature “momentum” than X.

**6.4 Gravitational Entropy Dominance**

The non-uniform equilibrium p\_eq \= (3, 2, 6)/11 reflects a fundamental asymmetry: the Y-sector (gravitational modes, dim \= 6\) dominates the entropy budget by factor 2 over the X-sector (matter modes, dim \= 3). This is the Z-Spin geometric realization of Penrose’s physical intuition—derived from polyhedral geometry rather than assumed as an initial condition.

**§7. Comparison with Existing Approaches**

| Criterion | Boltzmann | Penrose | Carroll | Z-Spin (Q7) |
| ----- | ----- | ----- | ----- | ----- |
| Initial conditions? | Required | Required | No | No |
| Past Hypothesis? | Yes | Yes (Weyl) | No | No |
| Free parameters | S\_initial | 0 (postulate) | 0 | 0 |
| Testable? | Indirect | Indirect | No | Yes (7 gates) |
| Entropy quantum | N/A | N/A | N/A | ln(2) per step |
| Time scale derived? | No | No | No | Yes (τ\_D \= ℏ/AE) |
| Markov justified? | Assumed | N/A | N/A | Yes (ε=2/Q) |

**§8. Quantum Information Perspective**

The Z-mediated transition is a CPTP channel Φ\_Z: B(H\_X) → B(H\_Y) via Stinespring dilation (ZS-Q1 v1.0): Φ\_Z(ρ\_X) \= Tr\_Z\[V(ρ\_X ⊗ |0⟩⟨0|\_Z)V†\], with V: H\_X ⊗ H\_Z → H\_Y ⊗ H\_Z isometry. Properties: (a) output rank ≤ 2, (b) Holevo capacity χ ≤ 1 bit, (c) structural entropy production.

**§9. Verification Suite**

**33 tests organized in 7 categories. All PASS.**

| Category | Tests | Result | Key Test |
| ----- | ----- | ----- | ----- |
| A. Locked Constants | 5 | 5/5 | A=35/437, Q=11, L\_XY=0 |
| B. Theorem 1 (Dim Ratio) | 5 | 5/5 | 10⁴ random matrices, var=0 |
| C. Theorem 2 (Z-Bottleneck) | 5 | 5/5 | 10⁴ trials, max rank=2 |
| D. Theorem 3 (Master Eq.) | 5 | 5/5 | D\_KL monotone, σ≥0 |
| E. Theorem 3A (Eigenvalues) | 3 | 3/3 | λ₂=−A exact, ε\_BM=2/Q |
| F. Anti-Numerology | 5 | 5/5 | Ratio tracks dim, not A |
| G. Cross-Paper Consistency | 5 | 5/5 | ZS-Q1 τ\_D, ZS-A6 §6 compat |

**§10. Falsification Gates**

| Gate | Falsification Condition | Type | Status |
| ----- | ----- | ----- | ----- |
| F-Q7.1 | CPT-independent T-violation observed with magnitude independent of A | Experimental | OPEN |
| F-Q7.2 | Isolated single-body shows spontaneous irreversibility without Z-mediation | Experimental | OPEN |
| F-Q7.3 | L\_XY ≠ 0 discovered in Z-Spin action | Theoretical | OPEN |
| F-Q7.4 | dD\_KL/dt \> 0 under Z-Spin compatible dynamics | Computational | PASSING |
| F-Q7.5 | Z-Spin hardware (3,2,6) transition statistics ≠ dimension ratio | Experimental | OPEN (2028+) |
| F-Q7.6 | dim(X) \= dim(Y) in physical sector decomposition | Structural | BLOCKING |
| F-Q7.7 | Master eqn eigenvalue λ₂ ≠ −A | Computational | PASSING |

**§11. Non-Claims**

**NC-Q7.1:** This arrow is a coarse-grained entropy bias. No CPT violation is claimed. Individual transitions are bidirectional.

**NC-Q7.2:** ΔS \= ln(2) and γ\_LQG \= ln(2)/(π√3) may be structurally related, but this paper does NOT derive the Immirzi parameter.

**NC-Q7.3:** This paper derives the thermodynamic arrow. The cosmological arrow (expansion direction) is ZS-U scope.

**NC-Q7.4:** The arrow does not explain conscious temporal experience.

**NC-Q7.5:** The Z-bottleneck eliminates the Past Hypothesis but does NOT quantitatively suppress Boltzmann brain rates.

**§12. Conclusion**

We have established a structural arrow of time within Z-Spin cosmology through three theorems plus a subsidiary eigenvalue theorem, with zero new parameters. The master equation is derived from unitary dynamics via Stinespring → CPTP → Lindblad → Pauli master equation. The Born-Markov approximation is justified by ε\_BM \= 2/Q \= 2/11. The exact eigenvalue factorization λ(λ \+ 2A/Q)(λ \+ A) \= 0 gives τ\_fast \= 1/A exactly, coinciding with τ\_D/τ\_Penrose. The Cosmological Closure Mapping derives all 8 Z-Sim closure parameters. Shannon entropy is not the correct Lyapunov function. The Y-sector’s dominance realizes Penrose’s gravitational entropy intuition from geometry. Seven falsification gates and five non-claims. Priority: F-Q7.5 (Z-Spin hardware, \~2028–2032).

**Appendix A. Cross-Reference Table**

| Paper | Input to ZS-Q7 | Status | Section |
| ----- | ----- | ----- | ----- |
| ZS-F1 v1.0 | Action S, L\_XY \= 0 | PROVEN | §2, §4, §5.0 |
| ZS-F2 v1.0 | A \= 35/437, δ\_X, δ\_Y | PROVEN | §2 |
| ZS-F5 v1.0 | (Z,X,Y)=(2,3,6), Q=11 | PROVEN | §2, §3 |
| ZS-Q1 v1.0 §3.3 | Stinespring → CPTP | PROVEN | §5.0 Step 1 |
| ZS-Q1 v1.0 §3.4 | SSE → Lindblad, Γ=2A(ΔE/ℏ)² | DERIVED | §5.0 Step 2 |
| ZS-Q1 v1.0 §5.1 | τ\_D \= ℏ/(A·E\_diff) | DERIVED | §5.5, §5.6 |
| ZS-M6 v1.0 | K\_XY \~ t² (two-step) | VERIFIED | §4 |
| ZS-A6 v1.0 §6 | Arrow (precursor) | DERIVED | §1, §6 |
| ZS-T3 v1.0 | Z-Sim forward simulator | CONSISTENT | Cross-check |

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite (ZS-Q7\_v1\_0\_verification.py) is publicly available. Dependencies: Python 3.10+, NumPy, SciPy, fractions (stdlib). Execution: python3 ZS-Q7\_v1\_0\_verification.py. Expected output: 33/33 PASS, exit code 0\.

**References**

\[1\] L. Boltzmann, Vorlesungen über Gastheorie (1896).  
\[2\] R. Penrose, The Road to Reality, Ch. 27 (Jonathan Cape, 2004).  
\[3\] S. Carroll, From Eternity to Here (Dutton, 2010).  
\[4\] D. Albert, Time and Chance (Harvard University Press, 2000).  
\[5\] J. Schnakenberg, Rev. Mod. Phys. 48, 571 (1976).  
\[6\] G. Lindblad, Commun. Math. Phys. 48, 119 (1976).  
\[7\] V. Gorini, A. Kossakowski, E.C.G. Sudarshan, J. Math. Phys. 17, 821 (1976).  
\[8\] S. Ryu, T. Takayanagi, PRL 96, 181602 (2006).  
\[9\] W.H. Zurek, Rev. Mod. Phys. 75, 715 (2003).  
\[10\] M.A. Nielsen, I.L. Chuang, Quantum Computation and QI (CUP, 2000).  
\[11\] A.S. Holevo, Probl. Inf. Transm. 9, 177 (1973).  
\[12\] Planck Collaboration, A\&A 641, A6 (2020).  
\[13\] W.F. Stinespring, Proc. AMS 6, 211 (1955).  
\[14\] Z-Spin Cosmology, ZS-F1 v1.0: The Z-Spin Action (2026).  
\[15\] Z-Spin Cosmology, ZS-F2 v1.0: Geometric Impedance A \= 35/437 (2026).  
\[16\] Z-Spin Cosmology, ZS-F5 v1.0: Gauge Symmetry Constraint Q \= 11 (2026).  
\[17\] Z-Spin Cosmology, ZS-Q1 v1.0: Geometric Decoherence (2026).  
\[18\] Z-Spin Cosmology, ZS-M6 v1.0: Block-Laplacian Spectral Verification (2026).  
\[19\] Z-Spin Cosmology, ZS-A6 v1.0: Boundary Physics (2026).  
\[20\] Z-Spin Cosmology, ZS-T3 v1.0: Z-Sim Forward Simulator (2026).

**Version History**

**v1.0 (March 2026):** Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v1.2.0)  
