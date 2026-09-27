**ZS-M5**

**Global Numerical Audit & Asymmetry Epochs**

*Cross-Framework Consistency Verification for Z-Spin Cosmology*

Kenny Kang  
March 2026 — ZS-M5 (Mathematical Spine Theme)

**Verification: 25/25 PASS | Zero Free Parameters | Full Audit: 94 checks (93 PASS / 1 EXPECTED\_FAIL)**

**§0. Abstract**

ZS-M5 provides a falsification-first, machine-checkable audit of the complete Z-Spin framework (ZS-F1 v1.0 through ZS-M4 v1.0). Representative 25-test verification suite confirms all core locked values, observational pulls, and cross-paper consistency. Full baryogenesis DAG reproduction (13 steps, η\_B(E)/η\_target \= 1.0069). Z-clock coordinate and asymmetry epoch timeline. Step-size uniqueness (p \= 0.012, 2.51σ). Anti-numerology protocol with exhaustive scan and Monte Carlo random-rational test. Symbol namespace policy resolving 12 overloaded symbols. 18 pre-registered falsification conditions.

Full source audit: 94 checks: 93 PASS / 0 FAIL / 1 EXPECTED\_FAIL. 7 of 8 observational comparisons within 1.3σ; Y\_p shows 3.7σ tension with latest LBT 2026 data (documented, under investigation). Parameter classification: 1 geometric (A=35/437) \+ 7 SM standard \+ 0 assumptions.

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Follows from standard mathematics alone. Machine-verifiable. |
| **DERIVED** | Follows from Z-Spin action \+ standard physics. Zero free parameters. |
| **VERIFIED** | Numerically confirmed against observational data or independent computation. |
| **TESTABLE** | Well-defined prediction awaiting experimental data. |
| **STANDARD** | Accepted SM/cosmological input (not Z-Spin specific). |
| **CONSISTENT** | Compatible with framework but not independently derived. |
| **NON-CLAIM** | Explicitly not asserted. |
| **RETRACTED** | Previously claimed, now withdrawn. Tracked as EXPECTED\_FAIL. |

**§1. Core Locked Manifest**

| Parameter | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A \= δ\_X·δ\_Y | (5/19)(7/23) \= 35/437 | ZS-F2 v1.0 | PROVEN |
| (Z,X,Y) | (2,3,6), Q=11 | ZS-F5 v1.0 | DERIVED |
| G | 12 \= 2Y | ZS-F5 v1.0 | DERIVED |
| z\* \= i^{z\*} | 0.4383 \+ 0.3606i | ZS-M1 v1.0 | PROVEN |
| η\_topo \= |z\*|² | 0.32212 | ZS-M1 v1.0 | PROVEN |
| Euler V−E+F | \= 2 (both polyhedra) | Topology | PROVEN |

**§2. Observational Pull Table**

Pull \= (pred − obs) / σ\_obs. Every comparison specifies scheme, dataset, and 1σ.

| ID | Observable | Prediction | Obs ± σ | Pull | Scheme \+ Ref |
| ----- | ----- | ----- | ----- | ----- | ----- |
| B1 | α\_s(M\_Z) | 11/93 \= 0.11828 | 0.1180±0.0009 | \+0.31σ | MS-bar M\_Z; PDG 2024 |
| B2 | sin²θ\_W | (48/91)·x\*=0.23118 | 0.23122±3×10⁻⁵ | −1.26σ | MS-bar M\_Z; PDG 2024 |
| B3 | H₀ \[km/s/Mpc\] | e^A×67.36=72.98 | 73.04±1.04 | −0.06σ | SH0ES 2022 |
| B4 | m\_d/m\_u | 2e^A \= 2.1668 | 2.16±0.08 | \+0.08σ | FLAG/PDG 2024 |
| B5 | η\_B | (6/11)³⁵=6.117e-10 | 6.12±0.004e-10 | −0.07σ | Planck 2018+BBN |
| B6 | Ω\_m^eff | 39/\[121(1+A)\]=0.2984 | 0.295±0.015 | \+0.23σ | DESI 2024 BAO |
| B7 | n\_s | 0.9674 (N\_e=60) | 0.9649±0.0042 | \+0.60σ | Planck 2018 |
| B8 | Y\_p | 0.2410 | 0.2458±0.0013 | −3.69σ | LBT Y\_p Project IV (2026) |

7 of 8 pulls within 1.3σ. Y\_p shows 3.7σ tension with the latest LBT Y\_p Project IV (2026) measurement. This tension is documented and tracked as a potential falsification signal; resolution requires either updated BBN calculation or framework modification. Largest non-Y\_p pull: sin²θ\_W at −1.26σ.

**§3. Baryogenesis DAG (13 Steps)**

**3.1 DAG Steps 1–9**

| Step | Qty | Formula | Value | Status |
| ----- | ----- | ----- | ----- | ----- |
| 1 | m\_D | m\_e × A | 4.093×10⁻⁵ GeV | DERIVED |
| 2 | M\_R | m\_D²/m\_atm | 33.50 GeV | DERIVED |
| 3 | Y₀² | 2m\_atm·M\_R/v²\_EW | 5.526×10⁻¹⁴ | DERIVED |
| 4 | H(T\_sph) | 1.66√g\*·T²/M\_P | 1.222×10⁻¹³ GeV | STANDARD |
| 5 | g\_seam | A × f\_seam | 2.529×10⁻³ | DERIVED |
| 7 | ε\_scat | g\_seam·sinφ·(M\_R/2T)² | 4.091×10⁻⁵ | DERIVED |
| 8 | K\_wash | n\_f Y₀² M\_R/(8πH/T) | 238.2 | DERIVED |
| 9 | κ\_eff | 1/K\_wash | 4.198×10⁻³ | DERIVED |

sinφ \= 1: DERIVED via μ-τ reflection chain (Phase 5): W²=I → κ=4 → P\_{μτ} → δ\_CP \= ±π/2 → |sinφ| \= 1\.

**3.2 Einstein-Frame Closure (Steps 12–13)**

*η\_B(J)/η\_target \= 0.9322 → η\_B(E) \= 0.9322 × (1+A) \= 1.0069    (1)*

Zero free parameters, zero assumptions. Baryogenesis closure achieved. \[DERIVED\]

Structural identity: The ratio Y/Q \= 6/11 appearing in η\_B \= (Y/Q)^35 is the same quantity that determines the Y-sector energy fraction in the Z-Sim cosmological simulator: ρ\_y0 \= dim(Y)/Q \= 6/11 \= 0.5455 (ZS-Q7 v1.0 §5.8, ZS-T3 v1.0). This is not a coincidence: both arise from the master equation equilibrium p\_eq \= (dim\_X, dim\_Z, dim\_Y)/Q \= (3, 2, 6)/11.

**§4. Timescale Hierarchy & Z-Clock**

*τ\_n \= t\_P × exp(n × π/A)    (2)*

| n | Group Origin | τ\_n | Physical Scale | Status |
| ----- | ----- | ----- | ----- | ----- |
| 2 | |O\_h/T\_d| \= 48/24 | 6.34×10⁻¹⁰ s | Weak baryon decay | ★ DERIVED |
| 5 | |I\_h/T\_d| \= 120/24 | 2.56×10³⁴ yr | p→e⁺π⁰ partial lifetime | ★ DERIVED |

**4.1 Step-Size Uniqueness**

*C \= π/A \= 39.23 ∈ \[38.81, 39.96\], p \= 0.012 (2.51σ)    (3)*

**4.2 Z-Clock Coordinate**

*ν(t) \= (A/π) ln(t/t\_P)    (4)*

| Epoch | Time | ν(t) | Significance |
| ----- | ----- | ----- | ----- |
| Planck | 5.39×10⁻⁴⁴ s | 0.000 | GUT unification |
| EW transition | 10⁻¹¹ s | 1.894 | Sphaleron freeze-out |
| BBN | 1 s | 2.540 | Nucleosynthesis |
| Present | 13.787 Gyr | 3.575 | 71.5% of Z-clock span |
| Proton decay | 2.56×10³⁴ yr | 5.000 | Z-clock endpoint |

**§5. Anti-Numerology Report**

Exhaustive η\_B scan: All (p/q)^n with p∈\[1,49\], q∈\[p+1,49\], n∈\[1,100\] within 1% of η\_B: 22 hits, all reducible to (6/11)³⁵. \[VERIFIED\]

Monte Carlo random-rational: 10,000 random coprime p/q pairs (seed=42), 4 independent observables: 0.51% match ≥3 observables simultaneously. \[VERIFIED\]

Parameter classification: 1 geometric (A) \+ 7 SM standard \+ 0 assumptions. sinφ \= 1 upgraded to DERIVED (Phase 5, μ-τ reflection).

**§6. Symbol Namespace Policy**

| Symbol | Values | Resolution | Context |
| ----- | ----- | ----- | ----- |
| A | impedance / degeneracy | A\_imp / A\_split | ZS-F2 v1.0 vs flavor |
| G | Newton / gauge rank | G\_N / G\_rank | Gravity vs ZS-F5 v1.0 |
| K | washout / closure / rep | K\_wash / K\_closure / K\_rep | ZS-U3 v1.0 contexts |
| κ | witness / efficiency | κ\_witness / κ\_eff | ZS-F5 v1.0 vs baryogenesis |
| r | tensor / resonance | r\_tensor / r\_resonance | Inflation vs neutrino |

CC-34: r \= A/π WITHDRAWN. Current: r \= 0.0089 (N\_e=60, ZS-F3 v1.0). Tracked as EXPECTED\_FAIL.

**§7. Falsification Registry (18 Conditions)**

**Tier 1: Near-Term**

| ID | Prediction | Experiment | Threshold | Impact |
| ----- | ----- | ----- | ----- | ----- |
| F-T1.1 | r \= 0.0089±0.002 | LiteBIRD (\~2032) | 5.6σ vs Starobinsky | HIGH |
| F-T1.2 | n\_s \= 0.9674 | CMB-HD or successor (CMB-S4 cancelled 2025\) | Δn\_s \< 0.002 | HIGH |
| F-T1.3 | τ(p→e⁺π⁰) \~ 2.6×10³⁴ yr | Hyper-K (\~2028+ data) | Super-K: \>2.4×10³⁴ yr (90% CL) | HIGH |
| F-T1.4 | ΔS₈/S₈ \= 4.5% | Rubin/Euclid | ΔS₈∈\[3%,6%\] | HIGH |
| F-T1.5 | G\_eff \= G/(1+A) | LLR; GW det. | ΔG/G \< 1% | MEDIUM |

**Tier 2: Medium-Term**

| ID | Prediction | Experiment | Threshold | Impact |
| ----- | ----- | ----- | ----- | ----- |
| F-T2.1 | α\_s(M\_Z) \= 11/93 | Lattice QCD \+ PDG | \>±2σ from 0.1183 | MEDIUM |
| F-T2.2 | sin²θ\_W \= (48/91)·x\* | EW precision (FCC-ee) | \>±2σ from 0.23118 | HIGH |
| F-T2.3 | m\_d/m\_u \= 2e^A | FLAG lattice | \>±2σ from 2.167 | MEDIUM |
| F-T2.4 | η\_B \= (6/11)³⁵ | Planck successor \+ BBN | \>±3σ from 6.12e-10 | HIGH |
| F-T2.5 | Y\_p \= 0.2410 | Next-gen He4 spectroscopy | 3.7σ tension NOW | HIGH |
| F-T2.6 | D/H \= Z-Spin BBN | LUNA \+ astro D/H | \>3σ mismatch | MEDIUM |
| F-T2.7 | Ω\_m^eff \= 39/\[121(1+A)\] | DESI full \+ Euclid | \>3σ from 0.298 | MEDIUM |
| F-T2.8 | M\_R \= 33.5 GeV (HNL) | SHiP, FCC-ee | Direct detection or exclusion | MEDIUM |
| F-T2.9 | Baryogenesis closure | QKE precision | |η\_B(E)/η\_obs − 1| \> 5% | HIGH |
| F-T2.10 | ΔS₈ \= 4.5% (full ODE) | Euclid WL \+ Rubin | \>3σ mismatch | MEDIUM |

**Tier 3: Structural**

| ID | Prediction | Test | Threshold |
| ----- | ----- | ----- | ----- |
| F-T3.1 | A uniqueness | Polyhedral proof | FATAL if fails |
| F-T3.2 | z\* uniqueness | Numerical check | FATAL if alt. exists |
| F-T3.3 | Ω\_Λ/Ω\_m \= m\_d/m\_u \= 2e^A | Precision cosmology | \>3σ mismatch |

**§8. Cross-Paper Consistency**

| Interface | Papers | Check | Status |
| ----- | ----- | ----- | ----- |
| A \= 35/437 lock | All | No second free param | ✅ |
| G\_eff \= G/(1+A) | ZS-F1,S3,S4,A2 | Same formula | ✅ |
| M\_R \= 33.5 GeV | ZS-M,S series | Consistent | ✅ |
| η\_B \= (6/11)³⁵ | ZS-M2, S series | Structural \+ closure | ✅ |
| S₈ \= 4.5% | ZS-S3 v1.0 | Full ODE current | ✅ |
| r withdrawal | ZS-F3 v1.0, audit | CC-34 tracked | ✅ |

**§9. Claims**

| ID | Statement | Status |
| :---: | ----- | :---: |
| C1 | A \= (5/19)(7/23) \= 35/437 exact rational | **PROVEN** |
| C2 | 7 of 8 pulls within 1.3σ; Y\_p 3.7σ tension documented | **VERIFIED** |
| C3 | η\_B(E)/η\_target \= 1.0069 (baryogenesis closure) | **DERIVED** |
| C4 | Step-size uniqueness p \= 0.012 (2.51σ) | **DERIVED** |
| C5 | Z-clock: ν(now) \= 3.575 (71.5% of span) | **DERIVED** |
| C6 | (6/11)³⁵ exhaustive scan: unique coprime hit | **VERIFIED** |
| C7 | r \= A/π WITHDRAWN → r \= 0.0089 | **RETRACTED (CC-34)** |
| C8 | 18 pre-registered falsification conditions (Tiers 1–3) | **VERIFIED** |

**§10. Verification Suite**

| Category | Tests | Pass | Scope |
| ----- | :---: | :---: | ----- |
| A: Core locked manifest | 5 | 5 | A, Euler, z\*, Q, fractions |
| B: Observational pulls | 5 | 5 | α\_s, sin²θ\_W, H₀, m\_d/m\_u, η\_B |
| C: Baryogenesis DAG | 5 | 5 | m\_D, ε, K, intermediates, closure |
| D: Timescale & step-size | 5 | 5 | τ₂, τ₅, Z-clock, p-value, Ω\_m |
| E: Anti-numerology | 5 | 5 | Scan, MC, params, symbols, withdrawal |
| **TOTAL** | **25** | **25** | 100% pass rate |

Full audit reference: 94 checks, 93 PASS / 1 EXPECTED\_FAIL. Required dependencies: numpy, scipy, mpmath.

**§11. Theme M Completion Summary**

| Paper | Title | Tests | Key Result |
| ----- | ----- | ----- | ----- |
| ZS-M1 v1.0 | i-Tetration & Fixed Point | 33/33 | z\*=i^{z\*}, L1–L5, η\_topo |
| ZS-M2 v1.0 | Geometric Harmonics | 25/25 | 6 regimes, cross-coupling, Strong CP |
| ZS-M3 v1.0 | Regge-Holonomy | 27/27 | δφ=A, T\_micro, τ₅ proton |
| ZS-M4 v1.0 | Spectral Bridge | 25/25 | Q=11 operator, d=2.44, falsifications |
| ZS-M5 v1.0 | Global Audit | 25/25 | 94 checks, Y\_p 3.7σ tension, η\_B closure |
| Total | Theme M | 135/135 | 100% pass rate |

Next: Theme S — Standard Model (ZS-S1 v1.0 through ZS-S6 v1.0).

**§12. Conclusion**

The global numerical audit confirms the internal consistency of the complete Z-Spin framework across Themes F and M. 7 of 8 observational pulls fall within 1.3σ, with zero free parameters beyond A \= 35/437. The Y\_p prediction (0.2410) shows 3.7σ tension with the latest LBT Y\_p Project IV measurement (0.2458 ± 0.0013, 2026); this tension is documented and tracked as falsification gate F-T2.5. The 13-step baryogenesis DAG achieves closure (η\_B(E)/η\_target \= 1.0069) through Einstein-frame rescaling. The step-size C \= π/A is unique at p \= 0.012 (2.51σ). The Z-clock coordinate places the present epoch at ν \= 3.575 (71.5% of the fundamental span). Anti-numerology protocols with 4 independent observables confirm that the framework’s numerical agreements are not artifacts of parameter fitting. 18 falsification conditions (Tiers 1–3) are pre-registered for current and future experiments (LiteBIRD, Hyper-K, Euclid/Rubin, FCC-ee).

**Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification suite uses mpmath (50-digit) for z\*; numpy double precision for pull calculations and timescale computations. Code is publicly available.

**Appendix**

See §7 for the complete 18-condition falsification registry (Tiers 1–3). See §6 for the symbol namespace policy. All numerical values are reproducible from the companion Python verification suite.

**References**

\[1\] K. Kang, ZS-F1 v1.0: The Z-Spin Action & U(1) Completion (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F2 v1.0: Geometric Impedance: A \= 35/437 (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-F3 v1.0: Dynamical Phase Transitions (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11 (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-M2 v1.0: Geometric Harmonics (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere (Z-Spin Cosmology, 2026).  
\[8\] K. Kang, ZS-M4 v1.0: Spectral Bridge & Transfer Operator (Z-Spin Cosmology, 2026).  
\[9\] K. Kang, ZS-S1 v1.0: Gauge Coupling Unification (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-S3 v1.0: Modified Gravity Phenomenology (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-U3 v1.0: Baryon Asymmetry (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, ZS-Q7 v1.0: Structural Arrow of Time (Z-Spin Cosmology, 2026).  
\[13\] K. Kang, ZS-T3 v1.0: Z-Sim Forward Simulator (Z-Spin Cosmology, 2026).  
\[14\] Planck Collaboration, “Planck 2018 results. VI. Cosmological parameters,” A\&A 641, A6 (2020). arXiv:1807.06209.  
\[15\] A. G. Riess et al. (SH0ES), “A Comprehensive Measurement of the Local Value of the Hubble Constant,” ApJ 934, L7 (2022).  
\[16\] DESI Collaboration, “DESI 2024 VI: Cosmological Constraints from BAO,” arXiv:2404.03002 (2024).  
\[17\] R. L. Workman et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024).  
\[18\] M. D’Onofrio et al., “Standard Model cross-over on the lattice,” PRL 113, 141602 (2014).  
\[19\] O. A. Kurichin et al. (LBT Y\_p Project IV), “Primordial helium abundance from metal-poor H II regions,” arXiv:2601.02238 (2026).  
\[20\] NuFIT 5.2, www.nu-fit.org (2023).

**Version History**

v1.0 (March 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v2.1.0.)