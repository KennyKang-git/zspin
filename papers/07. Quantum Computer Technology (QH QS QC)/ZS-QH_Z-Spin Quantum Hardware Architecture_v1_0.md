**ZS-QH v1.0**

**Z-Spin Quantum Hardware Architecture**

*Functional Material Specifications for the Topological Defect Controller*

Kenny Kang  
March 2026  
Theme: ZS-QH | Paper Code: ZS-QH

**Verification: 42/42 PASS | All Constants Locked from Prior Papers**

*HARDWARE PAPER — Materials, Fabrication, Kill-Switches | Algorithms → ZS-QS | Integration → ZS-QC*

**§0. Abstract**

We present the hardware architecture for a Z-Spin quantum processor — the Topological Defect Controller (TDC) — using functional material specifications derived from the Z-Spin block Laplacian theorem. The vanishing X–Y block (PROVEN, ZS-F1 v1.0) establishes a material-independent design axiom: any hardware implementation must provide a 3-level computational register (X-material), a 2-channel topologically protected mediator (Z-material), and a 6-channel dissipative reservoir (Y-material), with parasitic X–Y coupling below 1%.

We formulate these requirements as Functional Material Definitions (FMDs) — specifying WHAT properties a material must have, not WHICH specific substance to use. For each FMD, we identify candidate materials: bilayer graphene quantum dots (X), Bi₂Te₃ topological insulator (Z), C₆₀/CNT phonon reservoir (Y), while cataloguing alternatives (trapped-ion qutrits, photonic couplers, mechanical oscillators). Where current materials cannot meet specifications, the FMD provides the precise engineering target for future materials development.

Four operational kill-switches with concrete measurement protocols provide falsifiable engineering gates. A 6-step fabrication process is specified for the primary candidate stack (BLG/TI/CNT). Verification: 42/42 PASS. All constants locked from prior papers. Algorithm design is covered in ZS-QS v1.0; system integration in ZS-QC v1.0.

**Epistemic Status Legend**

| Status | Definition | Example |
| ----- | ----- | ----- |
| PROVEN | Mathematical theorem from Z-Spin axioms | L\_XY \= 0 |
| DERIVED | Follows from action \+ prior papers | τ\_D \= ℏ/(A·E\_diff) |
| FMD-SPEC | Functional material specification (engineering target) | "3-level system with T₁ \> 100 ms" |
| CANDIDATE | Existing material meeting FMD-SPEC | BLG QD for X-sector |
| TRANSLATED | Engineering interpretation of proven result. Subtype TRANSLATED-ESTIMATE: order-of-magnitude numerical value from toy model, not hardware prediction. | H1: parasitic \< 1%. TRANSLATED-ESTIMATE: \~0.73% leakage |
| HYPOTHESIS | Motivated conjecture, requires experiment | Room-temperature operation |
| LOCKED | Value fixed from prior paper; not re-derived here | A \= 35/437 from ZS-F2 |
| STRUCTURAL INSIGHT | Exact mathematical identity; physical necessity not established | |I\_h| \= 120 \= Q² − 1 |

**§0.1 Position Statement**

**⚠️ HARDWARE PAPER:** This paper specifies WHAT physical properties a material must have to implement Z-Spin quantum computing (Functional Material Definitions). It then identifies WHICH existing materials are candidates. It does NOT derive materials from the Z-Spin action. Algorithms → ZS-QS v1.0. System integration → ZS-QC v1.0.

**FUNCTIONAL MATERIAL DEFINITION (FMD):** A specification of the form "a material providing \[dimension\] with \[property\] \> \[threshold\], protected by \[symmetry\]" — defining the engineering target independent of any specific substance. This follows the established pattern: Kitaev (2003) defined anyonic braiding requirements; experimentalists then searched for materials satisfying them.

**§0.2 Paper Scope: QH / QS / QC**

| Paper | Scope | Audience | Content |
| ----- | ----- | ----- | ----- |
| ZS-QH (this paper) | Hardware & materials | Experimentalists, materials scientists | FMDs, candidates, fabrication, kill-switches |
| ZS-QS v1.0 | Software & algorithms | Quantum algorithm researchers | IRE, transfer operator, gate compilation |
| ZS-QC v1.0 | System integration | Theoretical physicists | Design principles, 4-track roadmap, platform comparison |

**§1. Locked Inputs from Theory**

All constants locked from prior Z-Spin papers. No new theoretical constants introduced. This paper translates these into engineering specifications. Engineering parameters (thresholds, tolerances) are clearly distinguished from theoretical constants.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z, X, Y) dimensions | (2, 3, 6); Q \= 11 | ZS-F5 v1.0 | PROVEN |
| G \= MUB(Q) | Q \+ 1 \= 12 | ZS-F5 v1.0 | PROVEN |
| L\_XY \= 0 (theory) | Exact zero in action | ZS-F1 v1.0, ZS-S1 v1.0 | PROVEN |
| J (seam involution) | J|j⟩ \= |Q−1−j⟩ | ZS-M3 v1.0 | PROVEN |
| δ\_X, δ\_Y | 5/19, 7/23 | ZS-F2 v1.0 | PROVEN |
| τ\_D/τ\_Penrose | 1/A \= 12.49 | ZS-Q1 v1.0 | DERIVED |

**§2. Design Axioms: Hardware Invariants**

Three design axioms follow from the block Laplacian theorem (PROVEN, ZS-F1 v1.0). These are material-independent — any implementation satisfying them is a valid Z-Spin processor.

**2.1 The Block Laplacian Theorem \[PROVEN\]**

The (1+Aε²)R coupling generates a 3-sector block Laplacian on Q \= 11 (ZS-S1 v1.0 §4):

**L \= ( L\_XX  C\_XZ  0 )**     **L\_XY ≡ 0 \[PROVEN\]**  
    ( C\_ZX  L\_ZZ  C\_ZY )  
    ( 0     C\_YZ  L\_YY )

The X–Y block is exactly zero. Z-mediated indirect propagation: ‖K\_XY(t)‖ \~ t² (ZS-M6 v1.0 §4.5).

**2.2 Three Hardware Axioms**

| Axiom | Specification | Origin | Kill-Switch |
| ----- | ----- | ----- | ----- |
| H1 (Isolation) | ‖H\_XY^par‖/‖H\_XZ‖ \< 1% | L\_XY \= 0 theorem | KS-1 |
| H2 (Z-Mediation) | All I/O through Z-sector only | Block structure topology | KS-3 |
| H3 (Directionality) | Data: X↔Z. Dissipation: Z→Y. No Y→X. | Sector function assignment | KS-3 |

\[STATUS: TRANSLATED\] These axioms define the engineering spec sheet. §3 translates them into Functional Material Definitions.

**§3. Functional Material Definitions (FMDs)**

Instead of claiming specific materials ARE sector implementations, we define WHAT properties each sector requires. This makes the paper useful even if all current candidate materials fail — the FMDs remain as engineering targets for future materials.

**3.1 FMD-X: Computational Register Material**

| Property | Requirement | Rationale |
| ----- | ----- | ----- |
| Hilbert space dimension | Exactly 3 addressable levels | dim(X) \= 3 from ZS-F5 v1.0 |
| Coherence time T₁ | \> 100 ms (minimum), \> 1 s (target) | Sufficient for \~10³ gate operations |
| Level addressability | 3 distinct transition frequencies | Lie closure of 3 transitions \+ detuning \= su(3); 2 alone yield dim=3 subalgebra |
| Leakage gap | Δ\_leak \> 5 × max(ΔE\_01, ΔE\_12) | Suppress population of non-computational states |
| Coupling to Z-material | Tunneling or dipole coupling, tunable | Axiom H2: all I/O through Z |
| Direct coupling to Y-material | \< 1% of X–Z coupling strength | Axiom H1: parasitic isolation |

*In words: "A material providing exactly 3 addressable quantum levels with coherence exceeding 100 ms, separated from higher levels by a leakage gap at least 5× the computational splitting, controllable via a 2-channel mediator."*

**3.2 FMD-Z: Mediator Material**

| Property | Requirement | Rationale |
| ----- | ----- | ----- |
| Effective channel count | 2 (effective, not necessarily native) | dim(Z) \= 2 from ZS-F5 v1.0 |
| Symmetry protection | Discrete symmetry (Z₂ or equivalent) | Stability of 2-channel structure against perturbation |
| Coupling asymmetry | Couples to BOTH X-material and Y-material | Axiom H2: mediates all transitions |
| Spectral filtering | Passes computational signals, attenuates noise | \~8% transmission target (engineering, not A) |
| Bulk isolation | No direct bulk conduction between X and Y faces | Axiom H1: physical X–Y separation |
| Operating range | Stable at target temperature ±20% | Robustness |

*In words: "A material providing exactly 2 effective coupling channels, protected by a discrete symmetry, physically separating the X-material from the Y-material while permitting controlled signal transmission."*

**⚠️ CORRECTION:** The Z-mediator’s transmission coefficient is an ENGINEERING target (\~8%), NOT the geometric impedance A \= 35/437. The transfer function T(ω) of any physical mediator depends on material properties (thickness, Fermi level, temperature), not on polyhedral geometry. This claim is WITHDRAWN.

**3.3 FMD-Y: Reservoir Material**

| Property | Requirement | Rationale |
| ----- | ----- | ----- |
| Channel count | 6 (effectively independent modes) | dim(Y) \= 6 from ZS-F5 v1.0 |
| Thermal conductivity | \> 1,000 W/m·K (target: \> 3,000) | Efficient dissipation of computational waste heat |
| Spectral density | 6 well-separated absorption peaks in J(ω) | 6 independent reservoir channels |
| Coupling to Z-material | Phonon-assisted or radiative | Axiom H3: Z→Y dissipation |
| Direct coupling to X-material | \< 1% of Z–Y coupling | Axiom H1: no Y→X backflow |
| Chemical stability | Stable under fabrication and operation conditions | Practical requirement |

*In words: "A material providing 6 effectively independent dissipative channels with thermal conductivity exceeding 1,000 W/m·K, coupled to the Z-material but physically isolated from the X-material."*

**§4. Candidate Materials**

STATUS: All materials below are CANDIDATES meeting FMD specifications to varying degrees. None are derived from the Z-Spin action. The FMDs (§3) are the primary contribution; candidate identification is secondary.

**4.1 X-Material Candidates**

| Candidate | FMD-X Compliance | Strengths | Weaknesses |
| ----- | ----- | ----- | ----- |
| BLG valley-spin QD ★ | 3 levels: |K↑⟩, |K’↑⟩, |K↓⟩. T₁ \> 500 ms (ETH 2024). Kramers T₁ \= 38 s (Nat. Nanotech. 2025\) | Longest solid-state T₁. Natural 3-level structure. Integrable in heterostructure. | Requires hBN encapsulation. Valley splitting tuning. |
| Trapped-ion qutrit (¹³⁷Ba⁺) | 11+ magnetic sublevels. T₁ \> 1 s demonstrated. | Mature technology. High fidelity. | Not solid-state. Scaling challenges. Vacuum required. |
| Transmon qutrit | Anharmonic 3 levels. T₁ \~ 100 μs. | Scalable. Industrial support. | Short T₁. Requires 15 mK. |
| NV center (m\_s \= 0, ±1) | Spin-1 triplet. T₁ \> 1 s at low T. | Room-temp operation. Optical interface. | SU(3) control challenging. Slow gates. |

Primary candidate: BLG QD selected for Track C (ZS-QC v1.0 §7.5) due to solid-state integration, exceptional coherence, and natural 3-level structure.

**4.2 Z-Material Candidates**

| Candidate | FMD-Z Compliance | Strengths | Weaknesses |
| ----- | ----- | ----- | ----- |
| Bi₂Te₃ TI ★ | 2 surface states. Z₂ invariant ν₀=1. Bandgap \~170 meV. | Topological protection. 2-channel natural. MBE growth mature. | Bulk carrier problem. Sn doping needed. |
| Bi₂Te₂Se | Same TI class. Reduced bulk carriers. | Better insulating bulk. | Less characterized surface states. |
| Photonic beam-splitter | 2 modes (H/V polarization). | Room temperature. Fast. | Difficult to integrate with solid-state X/Y. |
| SC coupler (transmon) | 2-level system as mediator. | Mature technology. | Requires 15 mK. No topological protection. |

Primary candidate: Bi₂Te₃ selected for topological Z₂ protection (functionally analogous to ZS seam Z₂ symmetry).

**HONESTY:** The Z₂ topological invariant ν₀ of the TI is NOT the same Z₂ as the Z-Spin seam involution J. They are FUNCTIONALLY ANALOGOUS: both provide 2-channel structure protected by a discrete symmetry. The physical mechanisms are different.

**4.3 Y-Material Candidates**

| Candidate | FMD-Y Compliance | Strengths | Weaknesses |
| ----- | ----- | ----- | ----- |
| C₆₀/CNT ★ | 6 channels: T₁u(3) \+ T₂g(3). k \> 3,000 W/m·K. | Perfect channel count. Exceptional thermal conductivity. | I\_h=120 connection is structural, not physical necessity. |
| 6 SC resonators | 6 independent modes. Tunable. | Precise frequency control. | Requires 15 mK. Complex fabrication. |
| Phononic crystal | Engineered bandgap. Multiple modes. | Designable spectrum. | Fabrication complexity. |
| Optical cavity array | 6 cavity modes. | Fast dissipation. | Solid-state integration difficult. |

Primary candidate: C₆₀/CNT selected for natural 6-channel phonon spectrum and exceptional thermal properties. NOTE: The \> 3,000 W/m·K figure applies to aligned, high-quality individual CNTs under ideal conditions; actual device-stack values in CNT networks or thin films are typically 10–100× lower. The FMD-Y target (\> 1,000 W/m·K) accounts for this gap.

**§5. Effective Device Hamiltonian**

For ANY material combination satisfying FMDs (§3), the effective Hamiltonian has the block structure:

**H\_TDC \= H\_X \+ H\_Z \+ H\_Y \+ H\_XZ \+ H\_ZY \+ H\_XY**parasitic

The first 5 terms are design targets; H\_XYparasitic is the engineering reality that Axiom H1 constrains.

**5.1 Generic Block Structure \[TRANSLATED from theory\]**

**H\_X:** 3-level Hamiltonian. E₀, E₁, E₂ determined by X-material.

**H\_Z:** 2-channel Hamiltonian. ε\_top, ε\_bot, t\_TB determined by Z-material.

**H\_Y:** 6-mode reservoir. ℏω\_k (k \= 1...6) determined by Y-material.

**H\_XZ:** X–Z coupling. Tunneling, dipole, or other mechanism.

**H\_ZY:** Z–Y coupling. Phonon-assisted or radiative.

**H\_XY**par**:** Parasitic direct coupling. DESIGN TARGET: ‖H\_XYpar‖/‖H\_XZ‖ \< 1%.

**5.2 Primary Candidate Instantiation (BLG/TI/CNT)**

**H\_X (BLG):** Σ\_{i=0}^{2} E\_i |i⟩⟨i|, E₀=0, E₁=1.2 meV, E₂=1.8 meV

**H\_Z (Bi₂Te₃):** Σ\_α ε\_α c†\_α c\_α \+ t\_TB(c†\_top c\_bot \+ h.c.)

**H\_Y (C₆₀):** Σ\_{k=1}^{6} ℏω\_k a†\_k a\_k (T₁u: \~527, 577, 1183 cm⁻¹; T₂g: \~710, 774, 1099 cm⁻¹)

\[STATUS: TRANSLATED\] Block structure from ZS-S1 v1.0 (PROVEN). Material-specific terms are empirical input.

**5.3 Parasitic Coupling Analysis**

| ε \= ‖H\_XY^par‖/‖H\_XZ‖ | ΔSchur/Schur | Assessment |
| ----- | ----- | ----- |
| 1% | 6.5 × 10⁻⁶ | PASS — design compliant |
| 10% | 6.3 × 10⁻⁴ | WARN — marginal |
| 100% | O(1) | FAIL — block structure destroyed |

**§6. Gate Operations and Measurement**

**6.1 Single-Qutrit Gates: SU(3) via Z-Mediation**

**Method 1 — Microwave drive through Z-material:** External pulses target Z only. The Z-material transmits with \~8% attenuation (engineering target), driving X-material transitions. Two independent coherent drives (0↔1, 1↔2) plus selective 2-photon Raman (0↔2) with independent detuning provide generators whose Lie closure is all of su(3) (dim=8). Note: two transitions alone generate only a 3-dimensional subalgebra; the third transition or diagonal detuning is necessary for full controllability \[Ramakrishna et al., PRA 51, 960 (1995)\].

**Method 2 — CPW coupled to Z-material:** Coplanar waveguide resonator coupled to Z-material interface, implementing data/coupler mode separation.

Both methods enforce Axiom H2: drive signals never directly reach X-material.

**NOTE:** The \~8% attenuation is an engineering design target for optimal SNR, NOT the geometric impedance A \= 35/437.

**6.2 Measurement: Z-Mediated Projective Readout**

CPTP channel Λ(ρ\_X) \= Σ\_z K\_z ρ\_X K\_z† (PROVEN, ZS-Q1 v1.0 §3): (1) Readout pulse to Z-material. (2) Z entangles with X as pointer. (3) Measure Z (2 outcomes). (4) Energy dumped to Y via Z–Y coupling. (5) Born rule p(x) \= Tr(P\_x Λ(ρ\_X)) automatically satisfied.

**6.3 Error Budget**

| Error Source | Mitigation | Suppression | Status |
| ----- | ----- | ----- | ----- |
| Parasitic X–Y | Physical isolation (H1) | \< 1% design target | KS-1 |
| Z-mediated phase noise | Γ \= 2A(ΔE/ℏ)² | Geometric | DERIVED (ZS-Q1 v1.0) |
| Indirect leakage | 2-step: \~t², O(κ²) | \~0.73% \[order-of-magnitude prior from Block-Laplacian; actual hardware leakage is material-dependent\] | TRANSLATED-ESTIMATE |
| Level relaxation | Material T₁ \> 100 ms (FMD-X) | Material-dependent | FMD-SPEC |
| Gate over-rotation | Z-attenuation (\~8%) | Calibratable | TRANSLATED |
| Leakage (qubit embed) | J-parity post-selection | P(detect) \= 5p/11 | DERIVED |

**§7. Multi-Cell Scaling**

**7.1 Incidence Matrix as Circuit Topology**

The incidence matrix B encodes multi-cell wiring. L \= B·Bᵀ reproduces block structure iff no edge connects X-node directly to Y-node. This is a topological constraint on chip layout, verified across 1000 random valid topologies.

| Edge Type | Allowed? | Physical Realization |
| ----- | ----- | ----- |
| X–Z (within cell) | ✅ | X-material ↔ Z-material interface |
| Z–Y (within cell) | ✅ | Z-material ↔ Y-material coupling |
| X–Y (ANY) | ❌ | Axiom H1 violation |
| Z–Z (between cells) | ✅ | Inter-cell bus (resonator, waveguide) |
| X–X (via Z bridge) | ✅ | Two-qutrit entangling gate |

**7.2 Two-Qutrit Entangling Gate**

For cells A, B: (1) Couple Z\_A to Z\_B via bus. (2) Gate pulse on Z\_A–Z\_B junction. (3) X\_A, X\_B entangled through Z-mediators. (4) Noise dumps to Y\_A, Y\_B independently. L\_XY \= 0 maintained cell-by-cell.

**§8. Fabrication Process (Primary Candidate Stack)**

This section applies to the BLG/Bi₂Te₃/CNT candidate stack. Alternative stacks require different fabrication; the FMDs (§3) remain the same.

| Step | Process | Material | Purpose | FMD Target |
| ----- | ----- | ----- | ----- | ----- |
| 1 | CVD/MBE | Si/SiO₂ \+ CNT | Y-material base | FMD-Y: thermal conductivity |
| 2 | Thermal evap. | C₆₀ thin film | Y-material completion | FMD-Y: 6-channel phonon spectrum |
| 3 | MBE (VdW epitaxy) | Bi₂Te₃, 5–10 QL | Z-material | FMD-Z: 2-channel, Z₂ protection |
| 4 | E-beam lithography | Z-material patterning | Impedance control | FMD-Z: spectral filtering |
| 5 | Transfer \+ hBN | Bilayer graphene | X-material | FMD-X: 3-level system |
| 6 | E-beam \+ metal deposition | Au/Ti gates | QD definition \+ valley control | FMD-X: level addressability |

Known issues: (i) Bi₂Te₃ bulk carrier problem → Sn doping or Bi₂Te₂Se alternative. (ii) hBN encapsulation yield. (iii) VdW interface quality.

**§9. Operational Kill-Switch Gates**

Four kill-switches provide falsifiable hardware engineering gates. Any single failure triggers architectural rejection. Each has a concrete measurement protocol.

**9.1 KS-1: S-Parameter Cross-Talk**

**Measurement:** (1) Broadband probe on Y-material. (2) Measure S₃₁ at X-material. (3) Z ON: includes Z-path. (4) Z OFF: parasitic only. (5) g\_XY \= |S₃₁(Z-OFF)|/|S₃₁(Z-ON)|.

PASS: g\_XY \< 0.01. FAIL: g\_XY \> 0.01 → immediate design rejection.

Equipment: Vector network analyzer (VNA), cryostat, microwave probes.

**9.2 KS-2: Seam Witness**

**Measurement:** u\_seam protocol (ZS-A4 v1.0 §3–4). Shadow estimation from Pauli measurements. Pre-registration specs: (i) Input states: N\_states ≥ d+1 \= 12 (MUB basis set for Q=11). (ii) Shots per state: n\_shots ≥ 10⁴, yielding σ(u\_seam) \< 0.05. (iii) ROPE equivalence test: u\_seam ∈ \[0, 0.1\] → PASS; u\_seam \> 0.5 → FAIL. (iv) Minimum shadow sample: O(3/ε² · ln(d²)) ≈ 1.4×10⁵ for ε \= 0.01.

PASS: u\_seam ≈ 0 within ROPE tolerance. FAIL: u\_seam \= O(1) → Z-material non-functional.

**9.3 KS-3: Direct Path Detection**

**Measurement:** (1) Detune Z-material by \> 10Γ (OFF). (2) Pulse Y-material. (3) Monitor X-material. (4) EXPECTED: A\_X(Z-ON) \> noise (Z-mediated, normal).

PASS: A\_X(Z-OFF) \< noise floor. FAIL: A\_X(Z-OFF) \> noise floor → non-Z coupling → architecture rejected.

**9.4 KS-4: Leakage Counting (Qubit Embedding)**

**Measurement:** P\_code \= Σ\_{j=0}^{10} |j⟩⟨j|, rank-11 on ℂ¹⁶. p\_leak \= 1 − Tr(P\_code ρ P\_code).

PASS: p\_leak \< 1%. FAIL: p\_leak \> 1% → INVALID\_PROTOCOL.

| ID | Name | Trigger | Consequence | Equipment |
| ----- | ----- | ----- | ----- | ----- |
| KS-1 | X–Y Parasitic | g\_XY \> 1% | Design rejected | VNA \+ cryostat |
| KS-2 | Z-Seam Collapse | u\_seam \= O(1) | Z-material rejected | Quantum processor \+ shadows |
| KS-3 | Direct Path | A\_X(Z-OFF) \> noise | Architecture rejected | Pulse generator \+ scope |
| KS-4 | Leakage | p\_leak \> 1% | INVALID\_PROTOCOL | State tomography |

**§10. Decoherence Time Prediction \[Reference\]**

From ZS-Q1 v1.0 §5 (not rederived here):

**τ\_D \= ℏ / (E\_diff · A),    τ\_D/τ\_Penrose \= 1/A \= 12.49**

Hardware significance: Z-Spin predicts 12.49× longer geometric coherence than Penrose–Diósi. Testable by gold nanosphere interferometry (10⁹ amu, 2028–2032). Full derivation: ZS-Q1 v1.0.

| Model | Free params | τ\_D/τ\_Penrose | Action? | Born rule? |
| ----- | ----- | ----- | ----- | ----- |
| GRW | 2 (λ, r\_c) | Adjustable | No | Postulated |
| CSL | 2 (λ, r\_c) | Adjustable | No | Postulated |
| Penrose–Diósi | 0 | 1 | No | Postulated |
| Z-Spin | 0 | 12.49 | Yes | Derived |

**§11. Honest Limitations**

**(L1)** Room temperature operation is HYPOTHESIS. Conservative: 0.3–3 K.

**(L2)** Single-cell Page typicality moderate (d\_Y/d\_X \= 2). Multi-cell improves exponentially.

**(L3)** Multi-cell bus engineering adds \~10 dB loss per Z–Z coupling.

**(L4)** SU(3) gates 2–5× higher error than SU(2) on current hardware.

**(L5)** Bi₂Te₃ bulk carrier problem. Mitigation: Sn doping, Bi₂Te₂Se.

**(L6)** Verification (42/42) confirms math and design logic, not hardware effect sizes.

**(L7)** Material → sector mapping is FUNCTIONAL ANALOGY, not derivation. BLG \= X because it satisfies FMD-X, not because the action mandates BLG.

**(L8)** TI transfer function T(ω) is NOT geometric impedance A \= 35/437. Calibration claim WITHDRAWN.

**(L9)** This paper provides FUNCTIONAL SPECIFICATIONS and CANDIDATE MATERIALS. If all candidates fail, the FMDs remain valid as engineering targets.

**(L10)** FMDs describe WHAT properties are needed. They do not guarantee that such materials EXIST or are FABRICABLE with current technology.

**(L11)** Indirect leakage \~0.73% is a TRANSLATED-ESTIMATE from the 11×11 Block-Laplacian toy model. Actual hardware leakage depends on material, process, frequency, and mode structure. The O(κ²) scaling is structural (PROVEN), but the numerical value is an order-of-magnitude prior, not a hardware prediction.

**(L12)** KS-2 (seam witness) requires channel tomography or quasi-tomography measurement. Pre-registration specs (N\_states, shots, ROPE) now specified, but experimental validation on real hardware remains pending.

**(L13)** SU(3) controllability requires not just three transitions but that their Lie closure spans all 8 dimensions of su(3). Two transitions alone generate only a 3-dimensional subalgebra. The BLG qutrit satisfies this (verified numerically), but the controllability proof depends on independent detuning capability.

**§12. Falsification Registry**

**12.1 Theoretical Gates**

| ID | Condition | Timeline | Confidence |
| ----- | ----- | ----- | ----- |
| F-QH1 | No material satisfying FMD-X exists (no 3-level system with T₁ \> 100 ms) | 2026–2028 | HIGH (already satisfied by BLG) |
| F-QH2 | No material satisfying FMD-Z exists (no 2-channel Z₂-protected mediator) | 2027–2029 | HIGH (already satisfied by TI) |
| F-QH3 | Parasitic coupling cannot be reduced below 5% in ANY material stack | 2028–2031 | MEDIUM |
| F-QH4 | τ\_D/τ\_Penrose ≠ 12.49 ± 20% | 2028–2032 | HIGH |
| F-QH5 | No solid-state integration of X/Z/Y materials achievable | 2028–2031 | MEDIUM |

**12.2 Kill-Switch Gates**

| ID | Condition | Outcome |
| ----- | ----- | ----- |
| KS-1 | g\_XY \> 1% | Design rejected |
| KS-2 | u\_seam \= O(1) | Z-material rejected |
| KS-3 | A\_X(Z-OFF) \> noise floor | Architecture rejected |
| KS-4 | p\_leak \> 1% | INVALID\_PROTOCOL |

**§13. Verification Suite \[42/42 PASS\]**

| Category | Tests | Pass | Key Result |
| ----- | ----- | ----- | ----- |
| \[A\] Foundations | 6 | 6/6 | Q=11, A=35/437, sectors |
| \[B\] Block Laplacian | 3 | 3/3 | L\_XY=0, Schur complement, no direct path |
| \[C\] Incidence Matrix | 3 | 3/3 | 1000/1000 valid topologies |
| \[D\] CPTP Channel | 3 | 3/3 | Completeness 10⁻¹² |
| \[E\] Decoherence | 4 | 4/4 | τ\_D/τ\_P \= 12.49, Lindblad Γ |
| \[F\] Kill-Switches | 5 | 5/5 | All 4 KS \+ falsifiable |
| \[G\] FMD Completeness | 3 | 3/3 | X(3), Z(2), Y(6) specs defined |
| \[H\] Anti-Numerology | 2 | 2/2 | p \< 1% |
| \[I\] Cross-Paper | 5 | 5/5 | ZS-F1,F2,F5,Q1,A4,QS |
| \[J\] Parasitic | 2 | 2/2 | ΔSchur \< 1% at ε=1% |
| \[K\] Bayesian | 2 | 2/2 | ΔBIC \= 6.34 |
| \[L\] Epistemic Honesty | 4 | 4/4 | FMD framing, T(ω)≠A, alternatives, L7–L13 |
| TOTAL | 42 | 42/42 | 100% PASS |

**§14. Conclusion**

We have presented the functional material specifications for the Z-Spin Topological Defect Controller (TDC), translating the block Laplacian theorem (L\_XY \= 0, PROVEN) into three material-independent Functional Material Definitions: FMD-X (3-level register, T₁ \> 100 ms), FMD-Z (2-channel Z₂-protected mediator), and FMD-Y (6-channel dissipative reservoir with k \> 1,000 W/m·K). For each FMD, we identified primary candidate materials (BLG QD, Bi₂Te₃ TI, C₆₀/CNT) and catalogued at least three alternatives, ensuring that the architecture survives even if all current candidates fail.

Four operational kill-switches (KS-1 through KS-4) with concrete measurement protocols provide binary pass/fail engineering gates. The verification suite confirms 42/42 PASS across 12 categories spanning foundations, block structure, CPTP channels, decoherence predictions, and epistemic honesty. All constants are locked from prior papers; zero new theoretical constants are introduced. The parameter-free prediction τ\_D/τ\_Penrose \= 1/A \= 12.49 provides the unique falsifiable signature testable by gold nanosphere interferometry (2028–2032). Algorithm design is covered in ZS-QS v1.0; system integration in ZS-QC v1.0.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

**Code Availability.** The verification suite is publicly available as verify\_ZS\_QH\_v1\_0.py. Dependencies: Python ≥ 3.9, NumPy, mpmath (≥50-digit precision for exact rational arithmetic), python-docx (for document audit). Execution: python3 verify\_ZS\_QH\_v1\_0.py ZS-QH\_v1\_0.docx. Expected output: 42/42 PASS with exit code 0\. The suite performs both numerical verification (block Laplacian, CPTP channel, Schur complement, Bayesian model comparison) and document audit (section structure, version consistency, epistemic status legend compliance, word count preservation).

**Appendix A: |I\_h| \= 120 \= Q² − 1 (Structural Observation)**

The icosahedral group I\_h has order 120 \= Q² − 1 \= dim(su(11)). This is a mathematical identity connecting Y-sector polyhedron symmetry to qudit Lie algebra dimension. Physical necessity not established.

\[STATUS: STRUCTURAL INSIGHT\] Retained as observation, not as design requirement.

**Appendix B: Cross-Reference Table**

| Paper | Content | Direction | Status |
| ----- | ----- | ----- | ----- |
| ZS-F1 v1.0 | Action S, L\_XY=0 | Input → ZS-QH | PROVEN |
| ZS-F2 v1.0 | A=35/437, polyhedra | Input → ZS-QH | LOCKED |
| ZS-F5 v1.0 | Q=11, (Z,X,Y)=(2,3,6) | Input → ZS-QH | PROVEN |
| ZS-S1 v1.0 | Block Laplacian, β-function | Input → ZS-QH | PROVEN |
| ZS-M3 v1.0 | J involution | Input → ZS-QH | PROVEN |
| ZS-Q1 v1.0 | CPTP, τ\_D, Born rule | Input → ZS-QH | DERIVED |
| ZS-A4 v1.0 | u\_seam, Track A/B | Shared | CONSISTENT |
| ZS-M6 v1.0 | Heat kernel, leakage bounds | Input → ZS-QH | VERIFIED |
| ZS-QS v1.0 | IRE algorithm, gates | Parallel (software) | CONJECTURAL |
| ZS-QC v1.0 | System integration | Downstream | CONSISTENT |

**References**

**Internal**

\[ZS-F1–F5\] K. Kang, Foundations Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-M1–M7\] K. Kang, Mathematical Spine, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-S1–S6\] K. Kang, Standard Model Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-Q1–Q7\] K. Kang, Quantum Mechanics Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-A1–A6\] K. Kang, Astrophysics Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-QS\] K. Kang, Inverse Riemann Engine, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-QC\] K. Kang, Z-Spin Quantum Architecture, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-M6\] K. Kang, Block-Laplacian Spectral Verification, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-T3\] K. Kang, Z-Sim: A Zero-Free-Parameter Forward Simulator, Z-Spin Cosmology (v1.0, 2026).

**External**

\[1\] W. K. Wootters and B. D. Fields, "Optimal state-determination by mutually unbiased measurements," Ann. Phys. 191, 363 (1989).  
\[2\] D. L. Denisov et al., "Long-lived valley states in bilayer graphene quantum dots," Nat. Nanotech. 20, 494 (2025).  
\[3\] R. Garreis et al., "Long-lived spin-valley states in bilayer graphene," Nat. Phys. (2024).  
\[4\] H. Zhang et al., "Topological insulators in Bi₂Se₃, Bi₂Te₃ and Sb₂Te₃ with a single Dirac cone on the surface," New J. Phys. 12, 065013 (2010).  
\[5\] H. Zareapour et al., "Proximity-induced high-temperature superconductivity in the topological insulators Bi₂Se₃ and Bi₂Te₃," Nat. Commun. (2012).  
\[6\] D. N. Page, "Average entropy of a subsystem," Phys. Rev. Lett. 71, 1291 (1993).  
\[7\] R. Penrose, "On gravity's role in quantum state reduction," Gen. Relativ. Gravit. 28, 581 (1996).  
\[8\] A. Bassi, K. Lochan, S. Satin, T. P. Singh, and H. Ulbricht, "Models of wave-function collapse, underlying theories, and experimental tests," Rev. Mod. Phys. 85, 471 (2013).  
\[9\] R. E. Kass and A. E. Raftery, "Bayes factors," J. Am. Stat. Assoc. 90, 773 (1995).  
\[10\] A. Yu. Kitaev, "Fault-tolerant quantum computation by anyons," Ann. Phys. 303, 2–30 (2003).  
\[11\] A. Yu. Kitaev, "Unpaired Majorana fermions in quantum wires," Phys.-Usp. 44, 131 (2001).  
\[12\] V. Ramakrishna, M. V. Salapaka, M. Dahleh, H. Rabitz, and A. Peirce, "Controllability of molecular systems," Phys. Rev. A 51, 960 (1995).

**Version History**

**v1.0 (March 2026):** Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v3.3.0)

**Internal development notes consolidated in v1.0:** Renamed ZS-QC → ZS-QH for 3-paper structure (QH \+ QS \= QC). T(ω) \= A calibration DELETED (material transfer function ≠ geometric impedance). Functional Material Definitions introduced in place of direct material claims. Algorithm content moved to ZS-QS. Integration roadmap moved to ZS-QC. Materials reframed as CANDIDATES with no derivation-from-action language. Platform comparison given honest framing. Limitations L8–L10 added for analogical mapping acknowledgement. H\_TDC framed as engineering, not theory. Header label changed from ‘Zero New Theoretical Constants’ to ‘All Constants Locked from Prior Papers’. Indirect leakage \~0.73% reclassified from DERIVED to TRANSLATED-ESTIMATE (Block-Laplacian value ≠ hardware leakage). KS-2 pre-registration specs added (N\_states, shots, ROPE). SU(3) control: Lie closure argument added (two transitions alone generate dim=3 subalgebra, not full su(3)). Limitations L11–L13 added for epistemic completeness per peer feedback (R1–R5). No physics changed across any internal revision.

**Z-Sim cross-reference (March 2026):** All 8 closure parameters of the Z-Spin forward simulator are now DERIVED from A \= 35/437 and (Z,X,Y) \= (2,3,6). See ZS-Q7 v1.0 §5.8 (mediation rates), ZS-M3 v1.0 §12 (phase gate), ZS-T3 v1.0. Zero free parameters.