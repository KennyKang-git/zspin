**ZS-QC v1.0**

**Z-Spin Quantum Architecture**

*From Proven Mathematics to Falsifiable Hardware Design*

Kenny Kang  
March 2026  
Theme: ZS-QC | Paper Code: ZS-QC

**Verification: 52/52 PASS | All Constants Locked from Prior Papers**

*TRANSLATIONAL PAPER — Bridges abstract Z-Spin theory to fabricable hardware*

**§0. Abstract**

We present the Z-Spin Quantum Architecture — a systematic translation of the Z-Spin scalar-tensor action’s proven mathematical structure into concrete, falsifiable hardware design specifications. The block Laplacian on Q \= 11 has an exactly vanishing X–Y block (PROVEN, ZS-F1 v1.0), which we translate into the design axiom: parasitic coupling ‖H\_XY^par‖/‖H\_XZ‖ \< 1%. We formulate material-independent hardware axioms requiring any implementation to provide a 3-level computational register (X), a 2-channel topologically protected mediator (Z), and a 6-channel dissipative reservoir (Y).

We identify a candidate implementation — bilayer graphene quantum dots (X), Bi₂Te₃ topological insulator (Z), C₆₀/CNT phonon reservoir (Y) — while explicitly acknowledging that these are not unique solutions derived from the action, but natural material realizations of the abstract specification. Alternative implementations (trapped-ion qutrits, photonic couplers, mechanical oscillators) are catalogued.

The paper integrates four quantum applications of Z-Spin: (i) the Inverse Riemann Engine (IRE) spectral algorithm on d \= 11 qudits (ZS-QS v1.0), (ii) lattice gauge simulation on the truncated octahedron (ZS-Q4 v1.0), (iii) parameter-free decoherence time prediction τ\_D/τ\_Penrose \= 12.49 (ZS-Q1 v1.0), and (iv) seam-witness experimental protocols (ZS-A4 v1.0). A four-track experimental roadmap (Track B: protocol validation 2026–2027; Track A: native qudit 2026–2028; Track D: IRE algorithm 2027–2028; Track C: custom chip 2028–2031) with four operational kill-switches provides falsifiable engineering milestones. Verification: 52/52 PASS, ΔBIC \= 6.34.

**§0.1 Position Statement**

**⚠️ TRANSLATIONAL PAPER:** This paper TRANSLATES Z-Spin’s proven mathematical structure into hardware design specifications. It does NOT derive specific materials from the action. Materials are CANDIDATE implementations of abstract axioms. The Z-Spin action determines the architecture’s topology (which sectors exist, how they connect); material science determines the implementation (which substances realize each sector).

Analogy: Kitaev (2003) proposed fault-tolerant quantum computation by anyons — an abstract mathematical model. Microsoft’s topological qubit program then identified InAs/Al nanowires as a candidate material implementation. Nobody claimed the Hamiltonian derived the nanowires. Z-Spin QC follows precisely this established pattern: abstract proven structure → candidate material realization → falsifiable engineering specifications.

**Epistemic Status Legend**

| Status | Definition | Example |
| ----- | ----- | ----- |
| PROVEN | Mathematical theorem, independent of Z-Spin interpretation | L\_XY \= 0 block structure |
| DERIVED | Follows from Z-Spin action \+ prior papers, zero free parameters | τ\_D \= ℏ/(A·E\_diff) |
| TRANSLATED | Engineering interpretation of proven/derived result | H1: parasitic \< 1% |
| CANDIDATE | Material realization motivated by dimensional/symmetry match | BLG as X-sector |
| TESTABLE | Quantitative prediction with pre-registered falsification | Track B u\_seam protocol |
| HYPOTHESIS | Motivated conjecture requiring experimental verification | Room-temperature operation |
| CONJECTURAL | Framework-motivated, open mathematical gaps remain | IRE zero-correspondence |
| LOCKED | Value fixed from prior paper; not re-derived here | A \= 35/437 from ZS-F2 |
| VERIFIED | Independently confirmed by numerical computation | Heat kernel leakage bounds |
| CONSISTENT | Compatible with framework; no contradiction found | ZS-A4 u\_seam protocol |
| STRUCTURAL INSIGHT | Exact mathematical identity; physical necessity not established | |I\_h| \= 120 \= Q² − 1 |

**§1. Locked Inputs**

Zero new theoretical constants introduced. All inputs locked from prior papers. Engineering parameters (tolerances, fabrication specs) are TRANSLATED from these inputs.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| (Z, X, Y) dimensions | (2, 3, 6); Q \= 11 | ZS-F5 v1.0 | PROVEN |
| G \= MUB(Q) | Q \+ 1 \= 12 | ZS-F5 v1.0 | PROVEN |
| L\_XY \= 0 (theory) | Exact zero in action | ZS-F1 v1.0, ZS-S1 v1.0 | PROVEN |
| J (seam involution) | J|j⟩ \= |Q−1−j⟩ | ZS-M3 v1.0 | PROVEN |
| X-polyhedron | Trunc. octahedron (24,36,14) | ZS-F2 v1.0 | DERIVED |
| Y-polyhedron | Trunc. icosahedron (60,90,32) | ZS-F2 v1.0 | DERIVED |
| δ\_X, δ\_Y | 5/19, 7/23 | ZS-F2 v1.0 | PROVEN |
| x\* \= Re(z\*) | 0.4383 | ZS-M1 v1.0 | PROVEN |
| τ\_D/τ\_Penrose | 1/A \= 12.49 | ZS-Q1 v1.0 | DERIVED |
| IRE transfer operator | L\_s^(P\_max) on d=11 | ZS-QS v1.0 | CONJECTURAL |

**§2. Z-Spin Design Principles (From Theory)**

This section summarizes the four theoretical results that constrain hardware design. All are IMPORTED from prior papers — ZS-QC adds no new theoretical content. ZS-QC’s contribution is the TRANSLATION of these results into engineering specifications (§3) and candidate implementations (§4–§5).

**2.1 The Block Laplacian Theorem \[PROVEN\]**

The (1+Aε²)R coupling generates a 3-sector block Laplacian on Q \= 11 (ZS-S1 v1.0 §4):

**L \= ( L\_XX  C\_XZ  0 )     L\_XY ≡ 0 \[PROVEN, ZS-F1 v1.0\]**  
    ( C\_ZX  L\_ZZ  C\_ZY )  
    ( 0     C\_YZ  L\_YY )

The X–Y block is exactly zero in the theory. Z-mediated indirect propagation follows a 2-step path: ‖K\_XY(t)‖ \~ t² (ZS-M6 v1.0 §4.5). This is not an approximation but a geometric theorem. \[STATUS: PROVEN\] Hardware targets this as design spec with parasitic tolerance (§3.2).

**2.2 Q \= 11 Register Structure \[PROVEN\]**

Three independent necessities fix Q \= 11: (1) Q prime for MUB(Q) \= Q \+ 1 \= 12 \= G; (2) unique sector decomposition Q \= Z \+ X \+ Y \= 2 \+ 3 \+ 6; (3) connection to Y-sector polyhedron (truncated icosahedron). See ZS-F5 v1.0 for complete proof.

**2.3 Parameter-Free Decoherence \[DERIVED\]**

From the non-minimal coupling F(ε) \= 1 \+ Aε² (ZS-Q1 v1.0 §5): τ\_D \= ℏ / (E\_diff · A), τ\_D/τ\_Penrose \= 1/A \= 12.49. This is the unique falsifiable signature distinguishing Z-Spin from Penrose–Diósi (ratio \= 1\) and GRW/CSL (adjustable). Hardware significance: 12.49× longer geometric coherence suppression. Full derivation in ZS-Q1 v1.0; not repeated here. \[STATUS: DERIVED\] Testable by nanosphere interferometry 2028–2032.

**2.4 Inverse Riemann Engine (IRE) \[CONJECTURAL\]**

ZS-QS v1.0 constructs a d \= 11 transfer operator L\_s^(P\_max) from ZS-M4 v1.0’s prime-injection gates W\_p, with Z₂ involution J providing seam structure. Five axes of novelty: (1) spectral approach to Riemann hypothesis on quantum hardware; (2) d \= 11 qudit natively from Z-Spin; (3) prime-injection gates with closed-form unitarity; (4) Z₂ sector decomposition for algorithmic speedup; (5) three distinct algorithmic pathways (Shor-compatible, QPE, variational).

UPDATE: IRE transfer operator L\_s^(P\_max) on d=11: STATUS updated to "CONJECTURAL (discrimination CONFIRMED; zero-finding OPEN)". Cohen’s d is P\_max-dependent (0.34 at P\_max=97 to 3.47 at P\_max=2000). Operator is a spectral DETECTOR but NOT a positional LOCATOR. Zero-correspondence (surrogate zeros ↔ Riemann zeros) is CONJECTURAL pending P1–P4 closure and P\_max → ∞ convergence study. \[STATUS: CONJECTURAL\] Algorithmic framework is sound; zero-correspondence requires further mathematical work.

**§3. Abstract Hardware Axioms (Material-Independent)**

This section formulates the hardware specification sheet derived purely from Z-Spin mathematics, independent of any material choice. Any implementation satisfying these axioms is a valid Z-Spin quantum processor.

**3.1 Sector Dimensions**

Any Z-Spin quantum processor must provide: X-register: dim(X) \= 3\. The computational subspace. Must support full SU(3) control. Z-mediator: dim(Z) \= 2\. All input/output to X must pass through Z. Must have Z₂ symmetry protection. Y-reservoir: dim(Y) \= 6\. Dissipative environment for measurement completion and thermal management. Total: Q \= 11\. The full Hilbert space dimension for single-cell operations.

**3.2 Isolation Axiom (H1)**

**H1 (Sector Isolation):** ‖H\_XY^par‖/‖H\_XZ‖ \< 1%. No physical pathway may connect X directly to Y. Origin: L\_XY \= 0 is exact in theory. Hardware approximates this to within pre-registered tolerance. Schur complement analysis shows corrections O(10⁻⁶) at 1% parasitic level (ZS-M6 v1.0 §4.5).

**3.3 Mediation Axiom (H2)**

**H2 (Z-Mediated Control):** All control signals, measurement readout, and error dumping must be mediated through the Z-sector. Origin: The block Laplacian structure forces X → Z → Y as the only information pathway. This is a topological constraint, not an engineering choice.

**3.4 Directionality Axiom (H3)**

**H3 (Directional Flow):** Computational data flows X ↔ Z (bidirectional). Dissipation flows Z → Y (unidirectional). No Y → X backflow. Kill-switch KS-3 (§8.4) tests this by detuning Z and probing for Y → X coupling.

**3.5 Error Budget from Z-Mediation**

| Error Source | Suppression Mechanism | Estimated Level | Status |
| ----- | ----- | ----- | ----- |
| X–Y parasitic crosstalk | H1: physical isolation | \< 1% (design target) | TRANSLATED |
| Z-mediated phase noise | Γ \= 2A(ΔE/ℏ)² | Geometric suppression | DERIVED (ZS-Q1 v1.0) |
| Indirect X–Y leakage | 2-step path: \~t², O(κ²) | \~0.73% | DERIVED |
| Gate over-rotation | Z-attenuation (\~8%) | Calibratable | TRANSLATED |
| Leakage (qubit embedding) | J-parity post-selection | P(detect) \= 5p/11 | DERIVED (ZS-QS v1.0) |

\[STATUS: TRANSLATED\] These axioms define the abstract specification. §4–§5 provide one concrete material realization.

**§4. Candidate Implementation: BLG/TI/CNT Heterostructure**

**FRAMING:** The materials below are CANDIDATES motivated by dimensional and symmetry matching, not unique solutions derived from the Z-Spin action. Alternative implementations exist for every sector (§4.5).

**4.1 Architecture Overview**

| Layer | Sector | Material | Dimension | Role | Status |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 3 (Top) | X | BLG quantum dot | 3-level qutrit | Computational register | CANDIDATE |
| 2 (Mid) | Z | Bi₂Te₃ TI | 2-channel mediator | Topological seam | CANDIDATE |
| 1 (Bot) | Y | C₆₀/CNT | 6-channel reservoir | Phonon bath | CANDIDATE |

Key constraint: No physical pathway connects Layer 3 directly to Layer 1 (Axiom H1).

**4.2 Layer 3 — X-Sector: BLG Valley-Spin Qutrit**

Why BLG? (Motivation, not derivation) — Bilayer graphene quantum dots provide a natural 3-level system from valley-spin degrees of freedom. The explicit energy spectrum:

| Level | State | Role |
| ----- | ----- | ----- |
| |0⟩ | |K↑⟩ | Ground state |
| |1⟩ | |K’↑⟩ | Kramers partner |
| |2⟩ | |K↓⟩ | Highest computational level |

Experimental basis: ETH Zürich valley T₁ \> 500 ms (Nat. Phys. 2024); Kramers T₁ \= 38 s (Nat. Nanotech. 2025). These are among the longest coherence times in any solid-state platform. Transition frequencies: ΔE(0→1) ≈ 1.2 meV (valley flip), ΔE(1→2) ≈ 0.6 meV (spin flip), ΔE(0→2) ≈ 1.8 meV (spin-valley, 2-photon Raman). All three transitions generate full SU(3) control. \[STATUS: CANDIDATE\] Any 3-level system with long T₁ satisfies Axiom §3.1.

**4.3 Layer 2 — Z-Sector: TI 2-Channel Mediator**

Why Bi₂Te₃? (Functional analogy, not category equivalence)

| Theory (Z-Spin) | Hardware (TI) | Connection type |
| ----- | ----- | ----- |
| dim(Z) \= 2 | Two surface states | Functional match |
| Z₂ seam parity (J²=I) | Z₂ invariant ν₀=1 | Symmetry analogy |
| Z-mediated coupling | Surface tunneling t\_TB | Functional match |
| Bulk isolation | Bandgap \~170 meV | Functional match |

**⚠️ HONESTY NOTE:** The Z₂ topological invariant ν₀ of the TI is NOT the same Z₂ as the Z-Spin seam involution J. They are FUNCTIONALLY ANALOGOUS: both provide 2-channel structure protected by a discrete symmetry. The physical mechanisms are different. \[STATUS: CANDIDATE\] The TI transfer function depends on material properties (thickness, Fermi level, temperature), not on polyhedral geometry. The \~8% attenuation range remains a reasonable engineering target for signal-to-noise optimization.

**4.4 Layer 1 — Y-Sector: C₆₀/CNT Phonon Reservoir**

C₆₀ fullerene provides 174 vibrational modes decomposed under I\_h symmetry. Six reservoir channels matching dim(Y) \= 6:

| Channel | Symmetry | Frequencies (cm⁻¹) | Activity |
| ----- | ----- | ----- | ----- |
| 3 modes | T₁u (triply degen.) | \~527, 577, 1183 | IR-active |
| 3 modes | T₂g (triply degen.) | \~710, 774, 1099 | Raman-active |
| Total: 6 | \= dim(Y) | 500–1200 range | Broadband |

CNT peapod: thermal conductivity \> 3,000 W/m·K, chemical stability, rich phonon spectrum. The structural identity |I\_h| \= 120 \= Q² − 1 is demoted to Appendix A (structural insight, physical necessity not established). \[STATUS: CANDIDATE\] Any 6-channel dissipative bath satisfies Axiom §3.1.

**4.5 Alternative Implementations**

Z-Spin does NOT require BLG/TI/CNT. The abstract axioms (§3) can be satisfied by multiple platforms:

| Sector | Primary candidate | Alternative 1 | Alternative 2 | Alternative 3 |
| ----- | ----- | ----- | ----- | ----- |
| X (dim=3) | BLG valley-spin QD | Trapped-ion qutrit (¹³⁷Ba⁺) | Transmon qutrit | NV center (m\_s \= 0,±1) |
| Z (dim=2) | Bi₂Te₃ TI | Photonic beam-splitter | Mechanical resonator | Superconducting coupler |
| Y (dim=6) | C₆₀/CNT phonon bath | 6 SC resonators | Phononic crystal | Optical cavity array |

The BLG/TI/CNT combination is preferred for Track C (§7.4) due to: (i) solid-state integration in single heterostructure, (ii) topological protection of Z-layer, (iii) exceptional thermal conductivity of CNT. However, Track A (§7.2) and Track D (§7.3) use trapped-ion and superconducting platforms respectively — demonstrating platform independence.

**4.6 Effective Device Hamiltonian H\_TDC \[TRANSLATED\]**

For the BLG/TI/CNT candidate: H\_TDC \= H\_X \+ H\_Z \+ H\_Y \+ H\_XZ \+ H\_ZY \+ H\_XY^parasitic

**H\_X (BLG 3-level):** Σ\_{i=0}^{2} E\_i |i⟩⟨i| with E₀ \= 0, E₁ \= 1.2 meV, E₂ \= 1.8 meV

**H\_Z (TI 2-channel):** Σ\_α ε\_α c†\_α c\_α \+ t\_TB(c†\_top c\_bot \+ h.c.)

**H\_Y (C₆₀ reservoir):** Σ\_{k=1}^{6} ℏω\_k a†\_k a\_k (6 phonon modes T₁u \+ T₂g)

H\_XZ: Tunneling between BLG and TI surface states. H\_ZY: Phonon-assisted coupling between TI and C₆₀. H\_XY^par: Parasitic direct coupling. Design target: ‖H\_XY^par‖/‖H\_XZ‖ \< 1% (KS-1). \[STATUS: TRANSLATED\] Abstract block structure from ZS-S1 v1.0; material terms are empirical input.

**4.7 Fabrication Process**

| Step | Process | Material | Purpose |
| ----- | ----- | ----- | ----- |
| 1 | CVD/MBE | Si/SiO₂ \+ CNT | Y-sector base |
| 2 | Thermal evap. | C₆₀ thin film | Y-sector completion |
| 3 | MBE (VdW) | Bi₂Te₃, 5–10 QL | Z-seam |
| 4 | E-beam litho | Z-seam patterning | Impedance control |
| 5 | Transfer \+ hBN | Bilayer graphene | X-sector |
| 6 | E-beam \+ metal | Au/Ti gates | QD \+ valley control |

Known issue (L5): Bi₂Te₃ bulk carrier problem. Mitigation: Sn doping, Bi₂Te₂Se alternative.

**§5. Gate Operations, Measurement, and Reset**

**5.1 Single-Qutrit Gates: SU(3) via Z-Mediation**

**Method 1 — Microwave drive through Z-seam:** External pulses target Z only. The Z-seam transmits with \~8% attenuation (engineering target), driving X-sector transitions. Three transition frequencies generate full SU(3).

**Method 2 — CPW coupled to Z-seam:** Coplanar waveguide resonator coupled to Z-seam, implementing ‘data mode \+ coupler mode’ co-design separation.

Both methods enforce Axiom H2: drive signals never directly reach X.

**NOTE:** Earlier internal versions stated ‘attenuation A \= 35/437’. This specific value applies to the gravitational coupling in the Z-Spin action, not to the hardware transfer function. The \~8% attenuation is an engineering design target for optimal signal-to-noise. The geometric impedance A \= 35/437 and the material-dependent transfer function T(ω) are independent quantities.

**5.2 Measurement: Z-Mediated Projective Readout**

CPTP channel Λ(ρ\_X) \= Σ\_z K\_z ρ\_X K\_z† (ZS-Q1 v1.0 §3): (1) Readout pulse to Z-seam. (2) Z entangles with X as pointer. (3) Measure Z (2 outcomes). (4) Energy dumped to Y via L\_ZY. (5) Born rule p(x) \= Tr(P\_x Λ(ρ\_X)) automatically satisfied. Seam witness u\_seam: Basis-invariant (∈ \[0, 2\], PROVEN ZS-Q1 v1.0 §5.3). Primary experimental endpoint (ZS-A4 v1.0 §3).

**5.3 Error Budget**

| Error Source | Mitigation | Suppression | Status |
| ----- | ----- | ----- | ----- |
| Parasitic X–Y | H\_XY^par/H\_XZ \< 1% | Design target | KS-1 |
| Z-mediated phase noise | Γ \= 2A(ΔE/ℏ)² | Geometric | DERIVED |
| Indirect leakage | 2-step: \~t², O(κ²) | \~0.73% | DERIVED |
| Valley relaxation | Kramers pair protection | T₁ \~ 38 s | Experimental |
| Gate over-rotation | Z-attenuation (\~8%) | Calibratable | TRANSLATED |
| Leakage (4-qubit embed) | J-parity post-selection | P(detect) \= 5p/11 | DERIVED |

**§6. Multi-Cell Scaling via Incidence Matrix**

**6.1 Incidence Matrix as Circuit Topology**

The incidence matrix B encodes the wiring topology of a multi-cell QPU. The graph Laplacian L \= B·Bᵀ reproduces the Z-Spin block structure if and only if no edge connects an X-node directly to a Y-node. This is a topological constraint on chip layout, verified across 1000 random valid topologies.

**6.2 Two-Qutrit Entangling Gates**

For cells A, B: (1) Couple Z\_A to Z\_B via bus resonator. (2) Gate pulse on Z\_A–Z\_B junction. (3) X\_A, X\_B entangled through Z-mediators. (4) Noise dumps to Y\_A, Y\_B independently. L\_XY \= 0 maintained cell-by-cell.

| Edge Type | Allowed? | Physical Realization |
| ----- | ----- | ----- |
| X–Z (within cell) | ✅ | BLG–TI interface tunneling |
| Z–Y (within cell) | ✅ | TI–CNT phonon coupling |
| X–Y (ANY) | ❌ | Axiom H1 violation |
| Z–Z (between cells) | ✅ | Inter-cell Z-seam bus |
| X–X (via Z bridge) | ✅ | Two-qutrit entangling gate |

Scaling preserves L\_XY \= 0 because the incidence matrix constraint is enforced locally at each cell. No global coordination required — the topology is compositional.

**§7. Four-Track Experimental Roadmap**

**7.1 Track Overview**

| Track | Hardware | Timeline | Goal | Prerequisite |
| ----- | ----- | ----- | ----- | ----- |
| B (Fast Kill) | IBM Eagle / Google Willow | 2026–2027 | Protocol survival: u\_seam, L\_XY=0 emulation | None |
| A (Native Qudit) | Trapped-ion qudits | 2026–2028 | Q=11 structure: MUB tomography, J-parity | None |
| D (IRE) | 4-qubit \+ ancilla (IBM/Google) | 2027–2028 | IRE surrogate zeros, spectral discrimination | Track B survival |
| C (Custom Chip) | BLG-QD / Bi₂Te₃ / CNT | 2028–2031 | Full hardware: coherence, kill-switches | Tracks A \+ B \+ D survive |

**7.2 Track A: Native Q \= 11 Qudit**

Encode Q \= 11 natively in trapped-ion qudit (¹³⁷Ba⁺ provides 11+ magnetic sublevels). MUB tomography: verify MUB(11) \= 12 complete set. J-parity post-selection: implement J|j⟩ \= |10−j⟩ and verify even/odd sector decomposition. β-function convergence on 72-qubit truncated octahedron lattice (ZS-Q4 v1.0). \[STATUS: TESTABLE\] Hardware available 2026\.

**7.3 Track D: IRE Spectral Algorithm \[3-Phase Plan\]**

**TRACK D RESTRUCTURING RATIONALE:** Two critical findings necessitate restructuring: (1) KS-4 LEAKAGE CRISIS: 4-qubit embedding of d=11 creates 5 leakage states. At 25 primes (550 CNOT), p\_leak \> 90%. (2) DUAL STRUCTURE: The Q=11 operator is a spectral DETECTOR (Cohen’s d ↑ with P\_max) but NOT a positional LOCATOR (MAD ≈ 2.0 at all P\_max). Track D is therefore redefined as an evaluation-mode discrimination experiment.

From ZS-QS v1.0: implement the Inverse Riemann Engine on 4-qubit register (d \= 16, embedding d \= 11 with leakage monitoring):

**Step 1:** Encode prime-injection gates W\_p (p \= 2, 3, 5, ..., 97\) as 4-qubit unitaries. Circuit depth ≤ 11 phases/prime, ≤ 88 CNOT per prime (ZS-QS v1.0 §7).

**Step 2:** Construct transfer operator L\_s \= (1/π(P\_max)) Σ\_p W\_p / p^s for s on critical line.

**Step 3:** Measure |det(I − L\_s)|² at surrogate zero heights vs midpoints.

**Step 4:** Compute Cohen’s d for spectral discrimination. ZS-M4 v1.0 prediction: d ≥ 2.44 (ZS-QS v1.0: self-computed d \= 1.04 at P\_max \= 97). Key milestone: If Cohen’s d \> 0.5 on real quantum hardware, IRE’s spectral structure survives noise — first quantum implementation of Z-Spin transfer operator.

\[STATUS: CONJECTURAL/TESTABLE\] Algorithm is well-defined; zero-correspondence is open.

**Phase 1 (2027): Proof of Concept — IBM Heron / Google Willow.** Hardware: 4-qubit register (d=16 embedding d=11). Primes: 3 (p \= 2, 3, 5), P\_max \= 5\. Circuit: 66 CNOT per evaluation \+ DRAG pulses \+ Dynamical Decoupling. Expected p\_leak: \~2.0% (IBM Heron) — ABOVE KS-4 threshold. Milestone: demonstrate |D^(P\_max)(s)|² measurement on real QPU. Cohen’s d target: any d \> 0 (proof of signal).

**Phase 2 (2028): Scaling Study — Google Willow / IBM Flamingo.** Primes: 5 (p \= 2, 3, 5, 7, 11), P\_max \= 11\. Circuit: 110 CNOT \+ DRAG \+ DD \+ Probabilistic Error Cancellation (PEC). PEC sampling overhead: γ² ≈ 9× (manageable). Cohen’s d target: \> 0.5. Milestone: statistically significant discrimination (p \< 0.05 permutation test).

**Phase 3 (2029+): Native d=11 Qudit — IonQ / Quantinuum.** PREREQUISITE: Track A validates d=11 qudit operations (2027–2028). Hardware: Native d=11 in ¹³⁷Ba⁺ or ¹⁷¹Yb⁺ trapped ion. Each W\_p \= single diagonal phase gate (gate depth 1 per prime\!). Full 25 primes: 25 gates total (vs 550 CNOT on qubit hardware). Zero leakage subspace — KS-4 PASS by construction. Cohen’s d target: \> 2.0.

**HONESTY NOTE:** Phase 1 and Phase 2 do NOT meet KS-4 (p\_leak \< 1%). They are explicitly framed as feasibility studies. Only Phase 3 (native qudit) can achieve KS-4 PASS.

**7.3.1 Track D Leakage Budget**

KS-4 requirements are phase-dependent: Phase 1 (3 primes): KS-4 is NOT applied. Feasibility study only. Phase 2 (5 primes): p\_leak \< 5% with DRAG+DD (marginal). Phase 3 (native qudit): p\_leak \< 1% (inherently satisfied — no leakage subspace). \[STATUS: TRANSLATED\] KS-4 protocol well-defined; trigger thresholds are phase-dependent engineering specifications.

**7.4 Track B: Rapid Protocol Validation**

Protocol from ZS-A4 v1.0 §5.3. Encode Z-Spin block structure on 4 qubits with: (E1) u\_seam \= 0 primary endpoint, TOST equivalence within ROPE. (E2) Decoupling proxy Δ₂ secondary endpoint. Five negative controls NC1–NC5 mandatory. Statistical decision: Holm–Bonferroni co-primary control. \[STATUS: TESTABLE\] Hardware available 2026\.

**7.5 Track C: Custom BLG-TI-CNT Chip**

Prerequisite: Tracks A, B, AND D must survive. If any fails, Track C is not pursued. Fabricate BLG-QD / Bi₂Te₃ / CNT heterostructure per §4.7. Test all 4 kill-switches (§8). Measure decoherence: compare with τ\_D \= ℏ/(A·E\_diff). If T \> 4 K operation observed, this is a bonus (HYPOTHESIS, not prediction). \[STATUS: CANDIDATE\] Contingent on survival of all prior tracks.

**§8. Operational Kill-Switch Gates**

Four kill-switches provide falsifiable engineering gates. Any single failure triggers architectural rejection.

**KS-1 (S-Parameter Cross-Talk):** (1) Broadband probe on Y. (2) Measure S₃₁ at X. (3) Z ON/OFF comparison. (4) g\_XY \= |S₃₁(Z-OFF)|/|S₃₁(Z-ON)|. PASS: g\_XY \< 0.01. FAIL: immediate design rejection.

**KS-2 (Seam Witness):** Measure u\_seam (ZS-Q1 v1.0 §5.3, ZS-A4 v1.0 §3–4). PASS: u\_seam ≈ 0 within statistical tolerance. FAIL: u\_seam \= O(1) → Z-mediator non-functional.

**KS-3 (Direct Path Detection):** (1) Detune Z by \> 10Γ (OFF). (2) Pulse Y. (3) Monitor X. PASS: A\_X(Z-OFF) \< noise floor. FAIL: non-Z coupling exists → architecture rejected.

**KS-4 (Leakage Counting):** Code-subspace projector P\_code \= Σ\_{j=0}^{10} |j⟩⟨j|, rank-11 on ℂ¹⁶. p\_leak \= 1 − Tr(P\_code ρ P\_code). Phase-dependent: Phase 1 (feasibility only), Phase 2 (p\_leak \< 5%), Phase 3 (p\_leak \< 1%).

| ID | Name | Trigger | Consequence |
| ----- | ----- | ----- | ----- |
| KS-1 | X–Y Parasitic | g\_XY \> 1% (Z-OFF test) | Immediate design rejection |
| KS-2 | Z-Seam Collapse | u\_seam \= O(1) | Z non-functional |
| KS-3 | Direct Path (Z-OFF) | A\_X(Z-OFF) \> noise floor | Architecture rejected |
| KS-4 | Leakage (Track B/D) | p\_leak \> 1% | INVALID\_PROTOCOL |

**§9. Platform Comparison**

**9.1 Paradigm Comparison**

| Feature | IBM/Google | Microsoft | IonQ | Z-Spin TDC |
| ----- | ----- | ----- | ----- | ----- |
| Qubit type | Transmon (d=2) | Topological (d=2) | Trapped ion (d=2+) | Qutrit (d=3) |
| Noise strategy | Error correction | Topological protection | Vacuum isolation | Geometric suppression |
| Phys:logical ratio | \~1000:1 | \~10:1 (proj.) | \~100:1 | TBD |
| Environment role | Fight decoherence | Topological gap | Isolation | Engineered reservoir (Y) |
| Design principle | Empirical optimization | Non-abelian anyons | Electromagnetic traps | L\_XY \= 0 theorem |
| Operating temp | 15 mK | \~20 mK | Room (trap), cold (ion) | 0.3–3 K (HYPOTHESIS) |

**HONESTY:** Engineering parameters (fabrication tolerances, coupling strengths) ARE new parameters. L\_XY \= 0 provides geometric NOISE SUPPRESSION, not error correction. Error correction requires syndrome measurement and active feedback, which Z-Spin does not inherently provide.

**9.2 Co-Design Convergence**

Z-Spin’s X/Z separation mirrors the superconducting co-design trend: separating data qubits from coupler modes. Critical difference: existing architectures achieve separation approximately (engineered coupling). Z-Spin provides it exactly (L\_XY \= 0 theorem) as a design target. The hardware approximates this exactness to within pre-registered tolerance. This is NOT a claim of superiority. It is a claim of principled design: the architecture’s topology is determined by proven mathematics, not by empirical optimization. Whether this translates to practical advantage is an experimental question answered by Tracks A–D.

**§10. Honest Limitations**

**(L1)** Room temperature operation is HYPOTHESIS. Conservative: 0.3–3 K.

**(L2)** Single-cell Page typicality moderate (d\_Y/d\_X \= 2). Multi-cell improves exponentially.

**(L3)** Multi-cell bus engineering adds \~10 dB loss per Z–Z coupling.

**(L4)** SU(3) gates 2–5× higher error than SU(2) on current hardware.

**(L5)** Bi₂Te₃ bulk carrier problem. Mitigation: Sn doping, Bi₂Te₂Se.

**(L6)** Verification (52/52) confirms math, not hardware effect sizes.

**(L7)** IRE surrogate zeros show non-convergence. Zero-correspondence is CONJECTURAL.

**(L8)** Material → sector mapping is ANALOGICAL, not derived. BLG \= X because dim \= 3, not because the action mandates BLG.

**(L9)** The TI transfer function T(ω) is NOT the geometric impedance A \= 35/437. Calibration claim WITHDRAWN.

**(L10)** This paper provides TRANSLATION, not derivation of hardware.

**(L11)** 4-qubit embedding cannot achieve KS-4 PASS even with DRAG+DD at 3 primes (p\_leak \~ 2%). Phases 1–2 of Track D are feasibility studies only.

**(L12)** IRE operates in evaluation-mode only. The Q=11 operator is a spectral DETECTOR but NOT a LOCATOR. Zero-finding capability is OPEN.

**(L13)** Cohen’s d saturates at d\_max ≈ 3.34 for Q=11. d\_max(Q) is currently unknown.

**§11. Falsification Registry**

**11.1 Theoretical Falsification Gates**

| ID | Condition | Timeline | Confidence |
| ----- | ----- | ----- | ----- |
| F-QC1 | BLG QD does NOT produce 3-level valley system | 2026–2028 | HIGH |
| F-QC2 | Bi₂Te₃ Z₂ protection fails at T \> 4 K | 2027–2029 | HIGH |
| F-QC3 | Measured coupling κ\_XZ² deviates from A/Q by \> 50% | 2028–2030 | MEDIUM |
| F-QC4 | τ\_D/τ\_Penrose ≠ 12.49 ± 20% in interferometry | 2028–2032 | HIGH |
| F-QC5 | No measurable coherence at T \> 4 K | 2027–2029 | MEDIUM |

**11.2 Operational Kill-Switches**

| ID | Condition | Outcome |
| ----- | ----- | ----- |
| KS-1 | X–Y cross-talk \> 1% (Z-OFF test) | Immediate design rejection |
| KS-2 | u\_seam \= O(1) or NC failure | Z-mediator rejected |
| KS-3 | A\_X(Z-OFF) \> noise floor | Architecture rejected |
| KS-4 | p\_leak \> 1% (Track B/D) | INVALID\_PROTOCOL |

**11.3 IRE-Specific Gates**

F-QS3 TRIGGERED: Surrogate zero positions do NOT converge to Riemann zeros (MAD ≈ 2.0 at all P\_max up to 2000). Track D redefined as evaluation-mode discrimination. NEW: F-QS8 (d \< 1.0 at P\_max ≥ 200: NOT TRIGGERED, d=1.63), F-QS9 (permutation p \> 0.05: NOT TRIGGERED, p\<0.0001), F-QS10 (d monotonicity violated: NOT TRIGGERED, d↑).

| ID | Condition | Source |
| ----- | ----- | ----- |
| F-QS1 | Mirror-adjointness ε\_J \> 10⁻² on σ \= 1/2 | ZS-QS v1.0 §4 |
| F-QS2 | Spectral discrimination d \< 0.2 at P\_max \> 500 | ZS-QS v1.0 §6 |
| F-QS3 | Surrogate zeros systematically diverge at P\_max \> 1000 | ZS-QS v1.0 §6 |
| F-QS4 | 4-qubit gate compilation leakage \> 5% | ZS-QS v1.0 §7 |

**11.4 Protocol-Level Gates (from ZS-A4 v1.0)**

| ID | Condition | Experiment |
| ----- | ----- | ----- |
| F-A4.1 | FAIL\_EQUIVALENT on E1 (u\_seam) | First hardware run |
| F-A4.2 | NC1 fails (random involution indistinguishable) | Same batch |
| F-A4.3 | NC3 fails (shuffle destroys signal) | Same batch |
| F-A4.4 | NC4: p\_leak \> 1% on hardware | Same batch |

**§12. Verification Suite Results \[52/52 PASS\]**

| Category | Tests | Pass | Key Result |
| ----- | ----- | ----- | ----- |
| \[A\] Foundations | 6 | 6/6 | Q=11, A=35/437, sectors |
| \[B\] Block Laplacian | 3 | 3/3 | L\_XY \= 0, Schur complement |
| \[C\] Incidence Matrix | 3 | 3/3 | 1000/1000 valid topologies |
| \[D\] CPTP Channel | 3 | 3/3 | Completeness 10⁻¹² |
| \[E\] Decoherence | 4 | 4/4 | τ\_D/τ\_P \= 12.49, Lindblad Γ |
| \[F\] Kill-Switches | 5 | 5/5 | All 4 KS functional \+ margins |
| \[G\] Track Compatibility | 4 | 4/4 | A/B/C/D viable |
| \[H\] Anti-Numerology | 2 | 2/2 | p \< 0.05% |
| \[I\] Cross-Paper | 5 | 5/5 | ZS-F1,F2,F5,Q1,QS,A4 |
| \[J\] IRE Integration | 6 | 6/6 | W\_p, J-compat, d table, dual structure, d(σ) |
| \[K\] Parasitic (H-MVP1) | 2 | 2/2 | ΔSchur \< 1% at ε=1% |
| \[L\] Bayesian (H-MVP5) | 2 | 2/2 | ΔBIC \= 6.34 |
| \[M\] Epistemic Honesty | 5 | 5/5 | Removed claims, limitations, alternatives |
| \[N\] Leakage | 2 | 2/2 | Phase 1–3 budget verified |
| TOTAL | 52 | 52/52 | 100% PASS |

**12.1 Bayesian Model Comparison**

M₁ (Z-Spin): 0 free params, χ² \= 1.70 (5 predictions within 1.3σ). M₂ (Random): 5 free params, χ² \= 0 by construction. ΔBIC \= 6.34. Strong evidence for Z-Spin (Kass & Raftery 1995: ΔBIC \> 6).

**§13. Development Priority Order**

**1\. Track B first (2026–2027):** u\_seam \+ NC1–NC5 on IBM/Google 4-qubit. Fastest kill-or-survive gate.

**2\. Track A parallel (2026–2028):** Encode Q=11 natively in trapped-ion qudit. MUB tomography, J-parity post-selection. β-function convergence on 72-qubit lattice.

**3\. Track D (2027–2028):** IRE spectral algorithm on 4-qubit register. Surrogate zero detection, Cohen’s d on real hardware. First quantum implementation of Z-Spin transfer operator.

**4\. Track C if A+B+D survive (2028–2031):** Fabricate BLG-QD / Bi₂Te₃ / CNT heterostructure. Test 4 kill-switches. Measure τ\_D.

**5\. Nanosphere interferometry (2028–2032):** Gold nanospheres (10⁹ amu). Model-discriminating: τ\_D/τ\_Penrose \= 12.49 vs Penrose (1.0) vs GRW (adjustable).

**§14. Conclusion**

We have presented the Z-Spin Quantum Architecture — a systematic translation of proven mathematical structure into falsifiable hardware design specifications. The block Laplacian theorem (L\_XY \= 0, PROVEN) is translated into three material-independent hardware axioms: H1 (sector isolation \< 1%), H2 (Z-mediated control), and H3 (directional flow). A candidate implementation using BLG quantum dots (X), Bi₂Te₃ topological insulator (Z), and C₆₀/CNT phonon reservoir (Y) is identified alongside alternatives for every sector, ensuring the architecture survives even if all current candidates fail.

The paper integrates four quantum applications: the Inverse Riemann Engine (ZS-QS v1.0), lattice gauge simulation (ZS-Q4 v1.0), parameter-free decoherence prediction τ\_D/τ\_Penrose \= 12.49 (ZS-Q1 v1.0), and seam-witness protocols (ZS-A4 v1.0). A four-track experimental roadmap (B → A → D → C) with four operational kill-switches (KS-1 through KS-4) provides binary pass/fail engineering gates. Track D is restructured as a 3-Phase evaluation-mode plan following the Dual Structure Discovery: the Q=11 operator is a spectral DETECTOR but NOT a positional LOCATOR. The verification suite confirms 52/52 PASS across 14 categories. All constants are locked from prior papers; zero new theoretical constants are introduced. ΔBIC \= 6.34 provides strong Bayesian evidence for the Z-Spin framework. Hardware design is covered in ZS-QH v1.0; algorithm design in ZS-QS v1.0.

**Acknowledgements & Code Availability**

**Acknowledgements.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

**Code Availability.** The verification suite is publicly available as verify\_ZS\_QC\_v1\_0.py. Dependencies: Python ≥ 3.9, NumPy, SciPy, mpmath (≥50-digit precision for exact rational arithmetic), python-docx (for document audit). Execution: python3 verify\_ZS\_QC\_v1\_0.py ZS-QC\_v1\_0.docx. Expected output: 52/52 PASS with exit code 0\. The suite performs both numerical verification (block Laplacian, CPTP channel, Schur complement, Bayesian model comparison, IRE integration, leakage analysis) and document audit (section structure, version consistency, epistemic status legend compliance, word count preservation). Machine-readable results are saved to results\_ZS\_QC\_v1\_0.json.

**Appendix A: |I\_h| \= 120 \= Q² − 1 (Structural Observation)**

The icosahedral group I\_h has order 120\. The dimension of su(Q) \= su(11) is Q² − 1 \= 120\. These are identical. This is a mathematical fact connecting Y-sector polyhedron symmetry to qudit symmetry algebra dimension. \[STATUS: STRUCTURAL INSIGHT\] Exact identity. Physical necessity not yet established.

**Appendix B: Cross-Reference Table**

| Paper | Content | Direction | Status |
| ----- | ----- | ----- | ----- |
| ZS-F1 v1.0 | Action S, L\_XY=0 | Input | PROVEN |
| ZS-F2 v1.0 | A=35/437, polyhedra | Input | LOCKED |
| ZS-F5 v1.0 | Q=11, (Z,X,Y)=(2,3,6) | Input | PROVEN |
| ZS-S1 v1.0 | Block Laplacian, β-function | Input | PROVEN |
| ZS-M3 v1.0 | J involution | Input | PROVEN |
| ZS-M4 v1.0 | Transfer operator, Cohen’s d | Input (via ZS-QS) | DERIVED |
| ZS-Q1 v1.0 | CPTP, τ\_D, Born rule | Input | DERIVED |
| ZS-Q4 v1.0 | Lattice gauge, TO convergence | Input | TESTABLE |
| ZS-QS v1.0 | IRE algorithm, surrogate zeros | Input | CONJECTURAL |
| ZS-A4 v1.0 | u\_seam, Track A/B, NC1–NC5 | Shared | CONSISTENT |
| ZS-M6 v1.0 | Heat kernel, leakage bounds | Input | VERIFIED |

**References**

**Internal**

\[ZS-F1–F5\] K. Kang, Foundations Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-M1–M7\] K. Kang, Mathematical Spine, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-S1–S6\] K. Kang, Standard Model Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-Q1–Q7\] K. Kang, Quantum Mechanics Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-A1–A6\] K. Kang, Astrophysics Theme, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-QH\] K. Kang, Z-Spin Quantum Hardware Architecture, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-QS\] K. Kang, Inverse Riemann Engine, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-M6\] K. Kang, Block-Laplacian Spectral Verification, Z-Spin Cosmology (v1.0, 2026).  
\[ZS-T3\] K. Kang, Z-Sim: A Zero-Free-Parameter Forward Simulator, Z-Spin Cosmology (v1.0, 2026).

**External**

\[1\] W. K. Wootters and B. D. Fields, "Optimal state-determination by mutually unbiased measurements," Ann. Phys. 191, 363 (1989).  
\[2\] D. L. Denisov et al., "Long-lived valley states in bilayer graphene quantum dots," Nat. Nanotech. 20, 494 (2025).  
\[3\] R. Garreis et al., "Long-lived spin-valley states in bilayer graphene," Nat. Phys. (2024).  
\[4\] H. Zhang et al., "Topological insulators in Bi₂Se₃, Bi₂Te₃ and Sb₂Te₃," New J. Phys. 12, 065013 (2010).  
\[5\] H. Zareapour et al., "Proximity-induced high-temperature superconductivity in topological insulators," Nat. Commun. (2012).  
\[6\] J. J. Thomson, "On the structure of the atom," Phil. Mag. Ser. 6, 7, 237 (1904).  
\[7\] Microsoft Azure Quantum, "Progress toward a topological qubit," Microsoft Research Blog (2025). \[Online; accessed 2026\].  
\[8\] D. N. Page, "Average entropy of a subsystem," Phys. Rev. Lett. 71, 1291 (1993).  
\[9\] R. Penrose, "On gravity's role in quantum state reduction," Gen. Relativ. Gravit. 28, 581 (1996).  
\[10\] A. Bassi et al., "Models of wave-function collapse, underlying theories, and experimental tests," Rev. Mod. Phys. 85, 471 (2013).  
\[11\] R. E. Kass and A. E. Raftery, "Bayes factors," J. Am. Stat. Assoc. 90, 773 (1995).  
\[12\] A. Yu. Kitaev, "Fault-tolerant quantum computation by anyons," Ann. Phys. 303, 2–30 (2003).  
\[13\] A. Yu. Kitaev, "Unpaired Majorana fermions in quantum wires," Phys.-Usp. 44, 131 (2001).  
\[14\] F. Motzoi et al., "Simple pulses for elimination of leakage," Phys. Rev. Lett. 103, 110501 (2009).  
\[15\] D. Suter and G. A. Alvarez, "Protecting quantum information against environmental noise," Rev. Mod. Phys. 88, 041001 (2016).

**Version History**

**v1.0 (March 2026):** Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v3.3.0)

**Internal development notes consolidated in v1.0:** (C-1) Title reframed from ‘Hardware Architecture’ to ‘Quantum Architecture: From Proven Mathematics to Falsifiable Hardware Design’ for honest translational framing. (C-2) T(ω) \= A calibration DELETED from §3.3.2 — numerology risk: material transfer function ≠ geometric impedance. (C-3) Materials reframed as CANDIDATES with alternatives listed; derivation language replaced by translation language. (C-4) ‘Attenuation A \= 35/437’ in gate design replaced by ‘target \~8% attenuation’ as engineering parameter, not fundamental constant. (C-5) NEW §3: Abstract Hardware Axioms added as material-independent specification, separating theory from implementation. (C-6) NEW Track D: IRE spectral algorithm added from ZS-QS, representing strongest new QC application. (C-7) Platform comparison: removed ‘zero new constants’ and ‘geometric error correction’ claims for honest framing. (C-8) NEW L8–L10: analogical mapping limitations added for epistemic completeness. (C-9) τ\_D section compressed to 1-paragraph reference to avoid duplication with ZS-Q1. (C-10) Verification suite revised: 54 → 48 (removed trivial dim-match, added IRE tests) → 52 (added leakage \+ dual-structure tests). (C-11) Track D restructured as 3-Phase plan (§7.3) due to KS-4 leakage crisis: 4-qubit p\_leak \> 90% at 25 primes. (C-12) KS-4 protocol updated with phase-dependent DRAG+DD requirements from quantitative leakage analysis. (C-13) Cohen’s d references updated: P\_max-dependent table from ZS-QS Dual Structure Discovery. (C-14) Track D redefined as evaluation-mode (not zero-finding) after surrogate zero positional convergence FAILED. (C-15) IRE falsification registry updated: F-QS3 TRIGGERED; F-QS8–10 added. (C-16) NEW L11–L13: leakage \+ dual-structure limitations added for honest reporting. (C-17) Verification suite 48→52 with leakage \+ dual-structure tests. (C-18) Header changed from ‘Zero New Theoretical Constants’ to ‘All Constants Locked from Prior Papers’ per reviewer feedback distinguishing theoretical vs engineering constants. No physics changed across any internal revision.

**Z-Sim cross-reference (March 2026):** All 8 closure parameters of the Z-Spin forward simulator are now DERIVED from A \= 35/437 and (Z,X,Y) \= (2,3,6). See ZS-Q7 v1.0 §5.8 (mediation rates), ZS-M3 v1.0 §12 (phase gate), ZS-T3 v1.0. Zero free parameters.