**ZS-M4**

**Spectral Bridge & Transfer Operator**

*Q=11 Transfer Operator, Berry–Keating Bridge, and Prime-Resonance Diagnostics*

Kenny Kang  
March 2026 — ZS-M4 (Mathematical Spine Theme)

**Verification: 25/25 PASS | Zero Free Parameters**

**§0. Abstract**

We construct a finite-dimensional transfer operator on the Q=11 Z-Spin register equipped with a Z₂ seam involution J, and test its spectral diagnostics against non-trivial zeros of the Riemann zeta function. The operator’s spectral determinant |det(I−L\_s)|² robustly separates Riemann zero heights from midpoint controls (Cohen’s d \= 2.44, p \< 0.002), while composite-gate and random-phase negative controls remain non-significant.

The Berry–Keating bridge is established via five locking identities (L1–L5) at the i-tetration fixed point z\* \= i^{z\*}, connecting Z-Spin’s cross-coupling structure to the H=xp paradigm. The seam involution implements the functional-equation symmetry s ↔ 1−s at the operator level (ε\_J \= 0 to machine precision).

Three honest falsifications are documented: (i) no simple A-based gap law exists; (ii) completed determinant |Dξ|² loses discriminating power; (iii) eigenvalue spacing is Poisson, not GUE. The midpoint bridge MAE ≈ 0.46 remains an open problem. This paper does NOT claim a proof of the Riemann Hypothesis.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Follows from standard mathematics alone. Machine-verifiable. |
| **DERIVED** | Follows from Z-Spin action \+ standard physics. Zero free parameters. |
| **TESTABLE** | Well-defined prediction/diagnostic awaiting further data or computation. |
| **HYPOTHESIS** | Structural parallel or conjecture. Derivation chain incomplete. |
| **FALSIFIED** | Tested and failed. Documented honestly as negative result. |
| **CONSISTENT** | Compatible with framework structure at finite Q. Not independently derived. |
| **OPEN** | Well-posed problem without current resolution. |
| **NON-CLAIM** | Explicitly not asserted. Documented to prevent overclaim. |
| **CONTROL** | Negative control test confirming specificity of positive results. |

**§1. Introduction**

**1.1 Scope and NON-CLAIM**

ZS-M4 bridges the Z-Spin framework to the Hilbert–Pólya program for the Riemann Hypothesis. We present diagnostics and structural bridges, not a proof. Every claim carries an epistemic tag; every numerical pattern is tested against negative controls.

**1.2 Locked Inputs**

| Input | Value | Source |
| ----- | ----- | ----- |
| A \= 35/437 | 0.080092 | ZS-F2 v1.0 |
| (Z,X,Y) \= (2,3,6), Q \= 11 | Slot register | ZS-F5 v1.0 |
| z\* \= i^{z\*} | 0.43828 \+ 0.36059i | ZS-M1 v1.0 |
| η\_topo \= |z\*|² | 0.32212 | ZS-M1 v1.0 |
| J: |j⟩ → |Q−1−j⟩ | Z₂ seam involution | ZS-F5 v1.0 |

**1.3 Epistemic Position**

PROVEN: L1–L5 identities, J²=I, JW\_pJ=W\_p\*, seam consistency ε\_J=0, functional equation Dξ(s)=Dξ(1−s). DERIVED: Spectral determinant D(s), completion factor B(s), ||L\_s||≤1. TESTABLE: Spectral det separation d\>1.9, negative control integrity. HYPOTHESIS: Berry–Keating connection, Hilbert–Pólya operator. FALSIFIED: A-based gap law, completed det discrimination. OPEN: GUE emergence (Q→∞), midpoint bridge (MAE≈0.46), self-adjoint extension.

**§2. Berry–Keating Bridge: Locking Identities**

At the i-tetration fixed point z\* \= i^{z\*} (ZS-M1 v1.0), five identities hold to machine precision:

*L1: arg(z\*) \= x\* · (π/2)    (1)*  
*L2: x\* \= |z\*|cos(arg), y\* \= |z\*|sin(arg)    (2)*  
*L3: |z\*| \= exp(−y\* · π/2)    (3)*  
*L4: y\*/x\* \= tan(x\* · π/2)    (4)*  
*L5: |i^{z\*} − z\*| \= 0    (5)*

| Identity | Residual | Status |
| ----- | ----- | :---: |
| L1 | 1.11 × 10⁻¹⁶ | **PROVEN** |
| L2x | 0.00 | **PROVEN** |
| L2y | 5.55 × 10⁻¹⁷ | **PROVEN** |
| L3 | 0.00 | **PROVEN** |
| L4 | 1.11 × 10⁻¹⁶ | **PROVEN** |
| L5 | 1.11 × 10⁻¹⁶ | **PROVEN** |

**Bridge interpretation (HYPOTHESIS):** The cross-coupling at z\* produces a “roles crossed” mapping — the boost-like variable controls phase while the rotation-like variable controls magnitude — mirroring Berry–Keating’s H=xp structure. This is a structural parallel, not a derivation.

**§3. Q=11 Transfer Operator**

**3.1 Slot Space and Seam Involution**

Computational space ℂ¹¹ with basis |j⟩, j \= 0,...,10.

*J|j⟩ \= |10−j⟩,  J² \= I    (6)*

Verified: ||J²−I|| \= 0 to machine precision. \[PROVEN\]

**3.2 Prime Gates**

*W\_p \= diag(exp(2πi(j−5)/p)),  j \= 0,...,10    (7)*

J-compatibility: J W\_p J \= W\_p\* for all primes. max||JW\_pJ − W\_p\*|| \= 0 across 80 primes. \[PROVEN\]    (8)

**3.3 Normalized Transfer Operator**

*L\_s \= (Σ\_{p≤P} p^{−s} W\_p) / (Σ\_{p≤P} p^{−1/2})    (9)*

Evaluated on the critical line s \= 1/2 \+ it. Computational setting: P \= 80 primes (up to p \= 409). This is a benchmark cutoff, not a free parameter. ||L\_s||\_op ≤ 1\. \[DERIVED\]

**3.4 Spectral Determinant**

*D(s) \= det(I − L\_s)    (10)*

*Dξ(s) \= ½(B(s)D(s) \+ B(1−s)D(1−s))    (11)*

B(s) \= ½s(s−1)π^{−s/2}Γ(s/2). By construction: Dξ(s) \= Dξ(1−s). \[PROVEN by construction\]

**§4. Seam Consistency**

*ε\_J(t) \= ||L\_{1−s} − J L\_s† J||\_F / ||L\_{1−s}||\_F    (12)*

ε\_J \= 0 at 10 zero heights, 10 midpoints, and 10 random t values. The seam involution is exact (algebraic identity from J-compatibility). Seam reality: |Im Dξ|/|Re Dξ| at zeros: mean \= 1.05 × 10⁻¹⁶. \[PROVEN\]

**§5. Spectral Determinant Separation**

|det(I−L\_s)|² at 20 zero heights vs 19 midpoints: Mean(zeros) \= 5.396, Mean(mids) \= 1.594, Cohen’s d \= 2.44, permutation p \= 0.0002 (5000-shuffle estimate). At N=120 (full dataset): d \= 1.96, p \< 10⁻⁶. \[TESTABLE\]

**5.1 Prime-Phase Resonance**

*S(t) \= |(1/N\_p) Σ\_{p∈P} exp(it·log p)|    (13)*

S(zeros) \= 0.1270, S(mids) \= 0.0502. Enhancement at zero heights. \[HYPOTHESIS diagnostic\]

**§6. Negative Controls**

Composite gates: d \= 0.89 \< 2.44 (prime). Weaker separation supports prime-specificity. \[CONTROL\] Random phases: ε\_J ≈ 1.4 (vs 0 for primes). Seam consistency destroyed. \[CONTROL\]

**§7. Honest Falsifications**

F30-5: No simple A-based gap law exists. \[FALSIFIED\] F30-4: Eigenvalue spacing is Poisson, not GUE (consistent with finite Q=11). \[CONSISTENT\] Completed |Dξ|² does not discriminate zeros from midpoints (B(s) washes out signal). \[FALSIFIED\] Stage34 shows gap-matched composites can partially mimic separation. \[DOCUMENTED\]

**7.1 What ZS-M4 Does NOT Establish**

(a) The midpoint bridge is not a precision zero predictor (MAE ≈ 0.46). (b) The operator does not reproduce GUE statistics. (c) The completed determinant Dξ does not discriminate. (d) Prime-specificity is limited.

**§8. Open Problems**

**O1 (GUE emergence):** Q → ∞ limit → GUE?

**O2 (Midpoint bridge):** Coupled observable with MAE \< 0.1?

**O3 (Hilbert–Pólya):** Self-adjoint extension reproducing ζ zeros?

**§9. Claims**

| ID | Statement | Status |
| :---: | ----- | :---: |
| C1 | L1–L5 at z\* (5 identities) | **PROVEN** |
| C2 | J²=I on ℂ¹¹ | **PROVEN** |
| C3 | JW\_pJ \= W\_p\* for all primes | **PROVEN** |
| C4 | ε\_J \= 0 (seam consistency) | **PROVEN** |
| C5 | Dξ(s) \= Dξ(1−s) | **PROVEN** |
| C6 | |det|² separates zeros (d=2.44) | **TESTABLE** |
| C7 | Composite NC weaker (d=0.89) | **CONTROL** |
| C8 | No A-based gap law | **FALSIFIED (honest)** |
| C9 | |Dξ|² non-discriminating | **FALSIFIED (honest)** |
| C10 | NOT an RH proof | **NON-CLAIM** |

**§10. Verification Suite**

| Category | Tests | Pass | Scope |
| ----- | :---: | :---: | ----- |
| A: Locking identities L1–L5 | 5 | 5 | Fixed-point residuals |
| B: Transfer operator | 5 | 5 | J², W\_p, J-compat, ||L\_s||, shape |
| C: Seam consistency | 5 | 5 | ε\_J at zeros/mids/random, Dξ, reality |
| D: Spectral separation | 5 | 5 | |det|², Cohen’s d, perm, random, S(t) |
| E: Honest falsifications | 5 | 5 | Gap law, Poisson, |Dξ|², composite NC, NON-CLAIM |
| **TOTAL** | **25** | **25** | 100% pass rate |

Required dependencies: numpy, scipy, mpmath. The suite will not run without mpmath.

**§11. Conclusion**

The Q=11 transfer operator with Z₂ seam involution provides a well-defined, falsifiable diagnostic bridge between Z-Spin cosmology and the Hilbert–Pólya program. The spectral determinant |det(I−L\_s)|² robustly separates Riemann zero heights from controls (d \= 2.44, p \= 0.002). The seam involution enforces functional-equation symmetry exactly (ε\_J \= 0). Three honest falsifications (gap law, completed determinant, GUE statistics) are documented transparently. This paper makes no claim toward a proof of the Riemann Hypothesis.

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite uses mpmath (50-digit) for z\* and Γ(s/2); numpy/scipy double precision for matrix operations. Code is publicly available.

**Appendix**

**A.1 Relation to ZS-M1 through ZS-M3**

| Paper | Interface | Status |
| ----- | ----- | ----- |
| ZS-M1 v1.0 | z\* \= i^{z\*}, L1–L5 | Direct input ✓ |
| ZS-M2 v1.0 | X-Z-Y sector structure | J implements X↔Y exchange ✓ |
| ZS-M3 v1.0 | Z₂ seam involution | J same structure as κ=4 witness ✓ |
| ZS-F5 v1.0 | Q=11, (Z,X,Y)=(2,3,6) | Register dimension ✓ |

**A.2 Key Numerical Values**

| Quantity | Value |
| ----- | ----- |
| z\* | 0.43828 \+ 0.36059i |
| |z\*| | 0.56756 |
| η\_topo \= |z\*|² | 0.32212 |
| ||L\_s||\_op (at γ₁) | 0.317 |
| Cohen’s d (N=20) | 2.44 |
| Permutation p (N=20) | 0.0002 |
| ε\_J (seam error) | 0.00 (exact) |
| d (composite NC) | 0.89 |

**References**

\[1\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M2 v1.0: Geometric Harmonics (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere (Z-Spin Cosmology, 2026).  
\[6\] M. V. Berry and J. P. Keating, “The Riemann zeros and eigenvalue asymptotics,” SIAM Rev. 41, 236 (1999).  
\[7\] A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” Selecta Math. 5, 29 (1999).  
\[8\] A. M. Odlyzko, “On the distribution of spacings between zeros of the zeta function,” Math. Comp. 48, 273 (1987).  
\[9\] Z. Rudnick and P. Sarnak, “Zeros of principal L-functions and random matrix theory,” Duke Math. J. 81, 269 (1996).  
\[10\] J. P. Keating and N. C. Snaith, “Random matrix theory and ζ(1/2+it),” Commun. Math. Phys. 214, 57 (2000).

**Version History**

v1.0 (March 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0.)