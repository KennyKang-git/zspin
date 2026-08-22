**ZS-M1**

**i-Tetration & Fixed Point**

*Microscopic Origin of the Z-Bias Field: z\* \= i^{z\*}*

Kenny Kang  
March 2026 — ZS-M1 (Mathematical Spine Theme)

**Verification: 33/33 PASS | Zero Free Parameters**

**§0. Abstract**

Five locking conditions (L1–L5) completely determine the i-tetration fixed point z\* \= 0.43828 \+ 0.36059i from a unique transcendental Master Equation. The topological threshold η\_topo \= |z\*|² \= 0.32212 \= e^{−y\*π}. The polygon-tetration family b\_n \= e^{2πi/n} exhibits a critical stability transition at n\_c \= 3.2036. Face-Polygon Correspondence: square (X, n=4, first stable) ↔ trunc. octahedron, pentagon (Y, n=5) ↔ trunc. icosahedron. A-bracketing: η(4)/4 \> A \> η(5)/5. 

The HSI Theorem (§1) DERIVES the i-tetration map T(z) \= i^z from the Z-Spin action via continuous homomorphism uniqueness on ℂ — Weyl additivity of log-conformal factors (ℂ,+) combined with multiplicativity of parallel transport (ℂ\*,×) forces T(z) \= exp(αz), and the quarter-turn from Ŵ²=I fixes α \= iπ/2. Zero new axioms. Leaky Wilson Loop Identity: λ² \= −(π²/4)·(−1)^{z\*} \[PROVEN\]. Verification: 33/33 PASS.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Follows from standard mathematics alone (no physics input). Machine-verifiable. |
| **DERIVED** | Follows from the Z-Spin action \+ standard physics. Zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated assumption (e.g., orientation choice). |
| **VERIFIED** | Numerically confirmed against observational data or independent computation. |
| **TESTABLE** | Well-defined prediction awaiting experimental data. |
| **HYPOTHESIS (Hn)** | Physically motivated conjecture. Derivation chain incomplete. Labeled H1, H2, ... for tracking. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests. No action-level derivation yet. |
| **CONSISTENT** | Compatible with framework structure but not independently derived or verified. No predictive claim. |
| **NON-CLAIM** | Explicitly not asserted. Documented to prevent overclaim. |
| **RETRACTED** | Previously claimed, now withdrawn with documented reason. |

**§1. Why i^z? — The Z-Sector Transfer Map**

This section derives the map T(z) \= i^z from the Z-Spin action with zero new axioms.

**Theorem 1.1 (HSI — Z-Sector Transfer Map). \[DERIVED\]** Given the Z-Spin action with conformal factor Ω² \= 1+Aε² (ZS-F1 v1.0), the Z₂ involution Ŵ²=I (ZS-F5 v1.0, ZS-U1 v1.0), and the sector decomposition Q=11=(Z,X,Y)=(2,3,6) (ZS-F5 v1.0), the Z-sector stroboscopic transfer map is uniquely T(z) \= exp((iπ/2)·z) \= i^z.

**Proof.** Step 1 \[DERIVED: ZS-F5 v1.0\]: dim(Z) \= 2\. Step 2 \[PROVEN: Frobenius 1877\]: The unique 2D associative division algebra over ℝ is ℂ. Therefore the Z-sector state space carries the algebraic structure of ℂ, with its canonical multiplication and exponential map. Step 3 \[DERIVED\]: The transfer map T: (ℂ,+) → (ℂ\*,×) is a continuous group homomorphism. This follows from two independent facts: (3a) Z-sector states compose additively — the state z \= ln Ω \+ iθ is the log-conformal factor, and Weyl rescalings compose multiplicatively (Ω\_total \= Ω₁·Ω₂), so their logarithms add: z₁₂ \= z₁+z₂ (ZS-U1 v1.0 §2.1, ZS-U5 v1.0) \[DERIVED\]. (3b) Holonomies compose multiplicatively — the holonomy of a composite parallel transport path is the product of individual holonomies: H(γ₁∘γ₂) \= H(γ₁)·H(γ₂) (Kobayashi-Nomizu, Ch. II) \[PROVEN: standard differential geometry\]. Combining: T(z₁+z₂) \= H(γ\_{Ω₁·Ω₂}) \= H(γ\_{Ω₁})·H(γ\_{Ω₂}) \= T(z₁)·T(z₂). Continuity follows from smoothness of the ε-field (ZS-F1 v1.0) and smooth dependence of parallel transport on initial data (standard ODE theory). Step 4 \[PROVEN: Lang, Algebra Ch. IV\]: Continuous Homomorphism Uniqueness — the only continuous group homomorphisms from (ℂ,+) to (ℂ\*,×) are z ↦ exp(α·z) for a unique α ∈ ℂ. (ℂ is connected and simply connected; exp is the universal covering map of ℂ\*.) Therefore T(z) \= exp(α·z). Step 5 \[DERIVED-CONDITIONAL\]: The quarter-turn structure from Ŵ²=I fixes α \= iπ/2. The Z₂ involution restricts to z → −z on the Z-sector (the unique orientation-preserving involution on ℂ). One mediation half-cycle M satisfies M² \= −I, giving T′(0) \= α with α² \= −(π/2)², so α \= ±iπ/2. Choosing \+iπ/2 (right-hand orientation; the choice |z\*|² \= η\_topo is sign-invariant). Therefore T(z) \= exp((iπ/2)·z) \= i^z. □

**Remark 1.2 (Leaky Wilson Loop Identity). \[PROVEN\]** The Lyapunov multiplier at the fixed point satisfies λ² \= −(π²/4)·(−1)^{z\*} \= −(π²/4)·exp(iπz\*), where λ \= (iπ/2)·z\*. This gives |λ²| \= (π²/4)·η\_topo ≈ 0.795. Physical meaning: the Wilson loop around one X→Z→Y→Z→X cycle “leaks” by a factor |λ²| \< 1 per cycle. This leakage IS the damping that makes z\* an attracting fixed point. A closed Wilson loop (|λ²|=1) would give marginal stability. The attracting nature of z\* requires η\_topo \< 4/π² (L5, §3).

**Remark 1.3 (Negative results documented).** Three alternative derivation routes were attempted and failed, each yielding a useful lesson. (i) Ŵ²=I alone: proves the linear quarter-turn M\_lin(z) \= iz but cannot determine the nonlinear extension M(z) \= i^z. Linear symmetry underdetermines nonlinear dynamics. (ii) Quantum channel (toy lattice): CPTP maps are linear; i-tetration is nonlinear. 50 random realizations all converge to z→0 (decoherence). Conclusion: i-tetration is pre-quantum classical geometry. (iii) Lawvere fixed-point theorem: proves z\* exists IF the map is given, but cannot determine WHICH map. Direction: HSI → z\*, not ??? → HSI. The successful route uses group-homomorphism uniqueness — a structure unavailable to the three failed approaches.

**§2. The Fixed Point z\* \= i^{z\*}**

Having established that the Z-sector transfer map is T(z) \= i^z (§1, HSI Theorem), we now compute its unique attracting fixed point.

*z\* \= i^{z\*} \= exp(z\* · iπ/2)  ;  z\* \= −W₀(−iπ/2) / (iπ/2)    (1)*

| Quantity | Symbol | Value | Significance |
| ----- | ----- | ----- | ----- |
| Real part | x\* | 0.4382829367 | Phase budget rate |
| Imag part | y\* | 0.3605924719 | Decay parameter |
| Magnitude | |z\*| | 0.5675551633 | 89.15% of 2/π |
| Phase | arg(z\*) | 39.45° | \= x\*π/2 |
| η\_topo | |z\*|² | 0.3221188634 | Topological threshold |
| |f′(z\*)| | — | 0.8915135658 | \< 1 (attractive) |

**§3. Five Locking Conditions**

*L1: arg(z\*) \= x\* × π/2  \[error \< 10⁻¹⁶\]    (3)*  
*L2: |z\*| \= x\* / cos(x\*π/2)  \[error \< 10⁻¹⁶\]    (4)*  
*L3: |z\*|² \= e^{−y\*π}  \[error \< 10⁻¹⁷\]    (5)*  
*L4: y\*/x\* \= tan(x\*π/2)  \[error \< 10⁻¹⁶\]    (6)*  
*L5: |z\*| \< 2/π ⇔ |f′(z\*)| \< 1    (7)*

Self-locking: x\* → y\* → |z\*| → arg(z\*) → stability. One number determines everything. \[ALL PROVEN\]

**§4. Master Equation**

*2 ln(x/cos(xπ/2)) \+ xπ tan(xπ/2) \= 0    (8)*

**Unique** solution x\* ≈ 0.4382829367 in (0,1). \[PROVEN\]

**§5. π/2 Phase Budget**

| Budget | Total | Used | Usage Rate |
| ----- | ----- | ----- | ----- |
| Phase | π/2 \= 90° | θ\* \= 39.45° | 43.83% \= x\* |
| Magnitude | 2/π \= 0.6366 | |z\*| \= 0.5676 | 89.15% |

**§6. Z-Sector Bridge**

*Z^Z \= 2² \= 4 \= ord(i)    (9)*

where ord(i) \= 4 denotes the multiplicative order of i in ℂ\* (i.e., i⁴ \= 1). The Z-sector dimensional exponent Z^Z equals the period of the i-tetration base. \[PROVEN\]

Z² × π/2 \= 2π (boson); Z³ × π/2 \= 4π (fermion). \[CONSISTENT\]

**§7. Polygon-Tetration Family**

*b\_n \= e^{2πi/n}  ;  z\*(n) \= −W₀(−2πi/n) / (2πi/n)    (10)*  
*Critical transition: n\_c \= 3.2036 where |f′| \= 1    (11)*

| n | Polygon | |f′| | Stable? | η(n) | Sector |
| :---: | ----- | :---: | :---: | :---: | ----- |
| 3 | Triangle | 1.0330 | NO | 0.2433 | Z-mediator |
| 4 | Square | 0.8915 | YES (1st) | 0.3221 | X-sector |
| 5 | Pentagon | 0.7878 | YES | 0.3930 | Y-sector |
| 6 | Hexagon | 0.7072 | YES | 0.4561 | Shared |

η(n) monotone increasing (n≥4). Asymptotic: 1 − η(n) \~ 8π²/n² \= 78.957/n². \[PROVEN\]

**Theorem 7.1 (Lyapunov–Lambert Identity). \[PROVEN\]** For all n such that z\*(n) is well-defined:

*α(n) \= Re(W₀(−2πi/n))    (12)*

where W₀ is the principal branch of the Lambert W function.

**Proof.** By definition, z\*(n) \= −W₀(−2πi/n)/(2πi/n), so |z\*(n)| \= |W₀|·n/(2π). The defining relation W·e^W \= −2πi/n gives |W|·e^{Re(W)} \= 2π/n. Therefore Re(W) \= ln(2π/n) − ln|W| \= −ln|z\*(n)| \= α(n).

In particular, α\_BK \= Re(W₀(−πi/2)), which is the unique bridge between the i-tetration constitutional fixed point and the BK rapidity (ZS-M7 v1.0 Theorem 3). The two pillars of Z-Spin Cosmology (A from polyhedral geometry; z\* from i-tetration) share a common analytic language: both α\_BK and φ\_sum \= artanh(δ\_X) \+ artanh(δ\_Y) are evaluations of the same function Re(W₀(−2πi/n)) at different arguments — n \= 4 and n \= n\_eff ≈ 3.854 respectively.

**Corollary 7.2 (Closed-Form α′(4)). \[PROVEN\]** Differentiating α(n) \= Re(W₀(−2πi/n)) with respect to n at n \= 4, using W′(z) \= W(z)/\[z(1+W(z))\] and Locking condition L3 (η \= e^{−y\*π}):

*α′(4) \= −(π/4)(πe^{−y\*π} \+ 2y\*) / (π²e^{−y\*π} \+ 4 \+ 4y\*π) \= −0.116238498161...    (13)*

Independently verified via the analytic W-derivative W′(z) \= W(z)/\[z(1+W(z))\]: |α′(4)\_Cor.7.2 − α′(4)\_W-route| \< 10⁻⁴⁵ (50-digit precision, mpmath). \[PROVEN\]

**§8. Face-Polygon Correspondence**

| Polyhedron | Sector | Char. Face | n | Tetration | Status |
| ----- | :---: | ----- | :---: | ----- | ----- |
| Trunc. octahedron | X | Square (×6) | 4 | FIRST STABLE | **PROVEN** |
| Trunc. icosahedron | Y | Pentagon (×12) | 5 | Stable | **PROVEN** |
| Tetrahedron | Z | Triangle (×4) | 3 | UNSTABLE | **PROVEN** |

**Cyclic Subgroup Exclusion:** C₄ exclusive to O\_h, C₅ exclusive to I\_h. \[PROVEN\]

**A-Bracketing:** η(4)/4 \= 0.08053 \> A \= 0.08009 \> η(5)/5 \= 0.07860. \[PROVEN\]

**Berry Phase:** Φ\_Berry/(2π) \= x\* \= 0.4383. \[PROVEN\]

**Edge Universality:** 2/3 of edges are characteristic for both polyhedra. \[PROVEN\]

**§9. Confinement-Instability Parallel**

**Identity:** b₃ \= ω₃ \= e^{2πi/3} — SU(3) color phase \= triangle tetration base. \[PROVEN\]

n\_c \= 3.204 marks confinement boundary: quarks (n=3, confined) vs leptons (n≥4, free). \[HYPOTHESIS H1\]

**§10. Claims**

| ID | Statement | Status |
| :---: | ----- | :---: |
| C1 | L1–L5 hold to 10⁻¹⁶ | **PROVEN** |
| C2 | Master Eq. unique root in (0,1) | **PROVEN** |
| C3 | Phase budget \= π/2 | **PROVEN** |
| C4 | n\_c \= 3.2036 critical transition | **PROVEN** |
| C5 | All n ≥ 4 stable | **PROVEN** |
| C6 | Berry: Φ/(2π) \= x\* | **PROVEN** |
| C7 | 1−η \~ 8π²/n² asymptotics | **PROVEN** |
| C8 | A-bracketing: g(4)\>A\>g(5) | **PROVEN** |
| C9 | Cyclic exclusion: C₄↔O\_h, C₅↔I\_h | **PROVEN** |
| C10 | b₃ \= ω₃ (color phase identity) | **PROVEN** |
| C11 | α(n) \= Re(W₀(−2πi/n)) for all stable n \[Thm 7.1\] | **PROVEN** |
| C12 | α′(4) closed-form \[Cor. 7.2\] | **PROVEN** |
| C13 | HSI Theorem: T(z)=i^z derived from Z-Spin action \[Thm 1.1\] | **DERIVED** |
| C14 | Leaky Wilson Loop Identity \[Remark 1.2\] | **PROVEN** |

**§11. Verification Suite**

| Category | Tests | Pass | Scope |
| ----- | :---: | :---: | ----- |
| A: Locking L1–L5 | 5 | 5 | Phase, magnitude, decay, ratio, stability |
| B: Master Equation | 3 | 3 | Residual, uniqueness, self-consistency |
| C: Polygon family | 5 | 5 | n\_c, n=3, n≥4, monotone, asymptotic |
| D: Face-Polygon | 4 | 4 | Cyclic, A-bracket, Berry, edges |
| E: Physical | 4 | 4 | η\_topo, Z^Z=ord(i), budget, b₃=ω₃ |
| F: Near-misses | 4 | 4 | All 4 near-misses REJECTED |
| G: Lyapunov–Lambert | 2 | 2 | Thm 7.1: α(n)=Re(W₀); Cor. 7.2: α′(4) via W-derivative \< 10⁻⁴⁵ |
| H: HSI Theorem | 4 | 4 | Homomorphism, continuity, α determination, uniqueness |
| I: Leaky Wilson Loop | 2 | 2 | λ² identity; |λ²| \= (π²/4)η\_topo |
| **TOTAL** | **33** | **33** | 100% pass rate |

The complete verification suite (ZS\_M1\_Verification\_Suite\_v1\_0.py) is publicly available. Required dependencies: numpy, scipy, mpmath. Categories G, H, I use 50-digit precision (mpmath, threshold \< 10⁻⁴⁵). Categories A–F use machine precision (numpy/scipy). The suite will not run without mpmath.

**§12. Conclusion**

This paper establishes the i-tetration fixed point z\* \= i^{z\*} as a rigorous mathematical object derived from the Z-Spin action, rather than postulated. The HSI Theorem (§1) shows that the transfer map T(z) \= i^z is the unique continuous group homomorphism from additive Weyl rescalings to multiplicative holonomies on the 2-dimensional Z-sector, with the quarter-turn structure from the Z₂ involution Ŵ²=I fixing the exponential base to i. This derivation requires zero new axioms beyond the Z-Spin action (ZS-F1 v1.0), the sector decomposition Q=11 (ZS-F5 v1.0), and the Z₂ involution (ZS-F5 v1.0, ZS-U1 v1.0).

The fixed point z\* \= 0.43828 \+ 0.36059i is completely characterized by five self-locking conditions (L1–L5) and a unique transcendental Master Equation. The topological threshold η\_topo \= |z\*|² \= 0.32212 connects to the cosmic matter density budget via the face counting route (ZS-A5 v1.0, ZS-A6 v1.0). The polygon-tetration family reveals a critical stability transition at n\_c \= 3.2036, with the Face-Polygon Correspondence linking the first stable polygon (n=4, square) to the X-sector truncated octahedron and the next polygon (n=5, pentagon) to the Y-sector truncated icosahedron. The A-bracketing inequality η(4)/4 \> A \> η(5)/5 confirms that the geometric impedance A \= 35/437 sits precisely in the stability window between the two characteristic polyhedra.

The Leaky Wilson Loop Identity (Remark 1.2) provides the physical interpretation: the Wilson loop around one mediation cycle leaks by a factor |λ²| \= (π²/4)·η\_topo ≈ 0.795 \< 1, and this leakage IS the damping mechanism that makes z\* an attracting fixed point. The Lyapunov–Lambert Identity (Theorem 7.1) establishes α(n) \= Re(W₀(−2πi/n)) as the common analytic language connecting the two pillars of Z-Spin Cosmology: polyhedral geometry (A) and i-tetration (z\*). All 33 verification tests pass at machine or 50-digit precision.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite (Python/mpmath, 50-digit precision) is publicly available.

**Appendix**

**A.1 Multi-Layered Falsification Gates**

| Layer | Gate ID | Falsification Condition |
| ----- | :---: | ----- |
| Mathematical(Theoretical collapse) | F-M1-1 | If z\* \= i^{z\*} admits a second attracting fixed point in the principal branch (k\_W \= 0), the uniqueness claim (C2) is destroyed and the entire downstream chain collapses. |
| Mathematical(Theoretical collapse) | F-M1-2 | If the Master Equation 2ln(x/cos(xπ/2)) \+ xπ tan(xπ/2) \= 0 has more than one root in (0,1), the self-locking chain L1–L5 loses determinacy. |
| Immediate rejection | F-M1-3 | If any locking condition L1–L5 fails at higher precision (e.g., 100-digit mpmath), the fixed-point self-consistency is broken. |
| Consistency collapse | F-M1-4 | If the A-bracketing inequality η(4)/4 \> A \> η(5)/5 fails for the exact value A \= 35/437, the face-polygon correspondence loses its geometric anchor. |
| Consistency collapse | F-M1-5 | If the HSI derivation step (Theorem 1.1) requires an axiom not present in ZS-F1 \+ ZS-F5 \+ ZS-U1, the zero-new-axioms claim is invalidated. |
| Observational | F-M1-6 | If future precision measurements of Ω\_m exclude both 39/121 and 38/121 at \> 5σ, the η\_topo ≈ Ω\_m connection is severed (does not destroy the pure mathematics of z\*). |
| Modification required | F-M1-7 | If a continuous homomorphism (C,+)→(C\*,×) other than exp(αz) is found, Step 4 of the HSI proof fails and must be repaired. |

Current status: All gates OPEN (no falsification triggered). F-M1-1 and F-M1-2 are protected by the Lambert W uniqueness theorem (principal branch). F-M1-3 is verified to 50-digit precision. F-M1-7 is protected by Lang’s theorem (Algebra, Ch. IV).

**A.2 Key Notation**

| Symbol | Definition / Value |
| ----- | ----- |
| A \= 35/437 | Geometric impedance (ZS-F2 v1.0) |
| Q \= 11 | Total register slots; (Z,X,Y) \= (2,3,6) (ZS-F5 v1.0) |
| z\* \= i^{z\*} | i-tetration fixed point (this paper) |
| η\_topo \= |z\*|² | Topological threshold \= 0.3221188634 |
| T(z) \= i^z | Z-sector transfer map (HSI Theorem) |
| λ \= (iπ/2)·z\* | Lyapunov multiplier at the fixed point |
| W₀ | Principal branch of the Lambert W function |
| n\_c \= 3.2036 | Critical polygon-tetration transition number |
| ord(i) \= 4 | Multiplicative order of i in ℂ\* (i⁴ \= 1\) |

**References**

\[1\] K. Kang, ZS-F0 v1.0: Ontological Bootstrap (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-U1 v1.0: ε-Field Inflation (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-U5 v1.0: Quantum Gravity Bridge (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere (Z-Spin Cosmology, 2026).  
\[8\] K. Kang, ZS-M7 v1.0: Berry–Keating Structural Isomorphism (Z-Spin Cosmology, 2026).  
\[9\] K. Kang, ZS-Q7 v1.0: Structural Arrow of Time (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-A5 v1.0: Dark Matter & ε-Halo (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-A6 v1.0: Boundary Physics in Z-Spin Cosmology (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, ZS-T3 v1.0: Z-Sim Forward Simulator (Z-Spin Cosmology, 2026).  
\[13\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” A\&A 641, A6 (2020). arXiv:1807.06209.  
\[14\] G. Frobenius, “Über lineare Substitutionen und bilineare Formen,” J. Reine Angew. Math. 84, 1–63 (1877).  
\[15\] S. Lang, Algebra, 3rd ed. (Springer, 2002), Ch. IV.  
\[16\] S. Kobayashi and K. Nomizu, Foundations of Differential Geometry, Vol. I (Wiley, 1963), Ch. II.

**Version History**

v1.0 (March 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v3.0.0.)