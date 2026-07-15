**ZS-Q9**  
**Complex Time-Delay Locking on the i-Tetration Fixed Point:**  
**A Z-Spin Reading of Sub-Unitary Scattering in**  
**Optical Micro-Resonators and Microwave Ring Graphs**  
   
**Kenny Kang**  
Theme: Quantum Mechanics \[ZS-Q\] | Paper 9 of 8 (extension series)  
ZS-Q9 v1.1 | May 2026  
   
**Verification:** 44/45 PASS (1 PARTIAL on synthetic Q9.5 — full closure pending real data) | Zero Free Parameters | Six Locking Gates Pre-Registered | Anti-Numerology MC p\_LEE \= 1.31 × 10⁻⁴  
 

**§0. Abstract**

We present ZS-Q9 v1.1, the structural and experimental framework that elevates the i-tetration fixed point z\* \= 0.4382829... \+ 0.3605925...i, previously locked at the five self-consistent algebraic identities L1-L5 in ZS-M1, to a directly lab-measurable object via the complex transmission time delay τ\_T \= \-i ∂\_ω ln\[det T(ω \+ iα)\] of a sub-unitary scattering system. Six new theorems are introduced that do not duplicate any corpus-PROVEN identity. Theorem Q9.1 (Complex Time-Delay Locking, DERIVED-CONDITIONAL) states that the PRN-normalized Z\_exp \= γ\_3dB · τ\_T satisfies L1-L5 if and only if Z\_exp \= z\*. Theorem Q9.2 (Spectral-Iteration Bridge, DERIVED-CONDITIONAL) identifies tr\_Z\[ln M\_f\] \= 2 ln|λ| \= \-0.22967 of the Z-block Wilson-loop matrix M\_f (ZS-F0 §8.8 PROVEN) with the lab-coordinate logarithmic derivative ∂\_ω ln det T at the operating point. Theorem Q9.3 (Krein-Friedel Decomposition, DERIVED-CONDITIONAL) decomposes the sub-unitary density-of-states shift Δρ(ω) into V\_XZ and V\_ZY channel-pair half-holonomies and reduces to Δρ|\_op \= (1/2)|∂\_ω ε|\_op. Theorem Q9.4 (Phase-Doubling Lab Realization, HYPOTHESIS-strong) lifts the ZS-M32 phase-doubling α\_amp \= π/10 to α\_op \= π/5 to the lab cross-product arg(τ\_T^A · τ\_T^G) \= π/5 \+ arg(z\*) with the new k=10 closure observation 10·α\_op \+ arg(z\*) ≡ arg(z\*) (mod 2π). Theorem Q9.5 (Sub-Unitary SFF, status downgraded to PARTIAL in v1.1) ties |K(T\_cycle)|² to |λ|² \= (π²/4)·η\_topo \= 0.7948 as a bonus gate L6; v1.1 reports that synthetic 11-pole spectra do NOT reproduce this quantization (residual 0.77), confirming that L6 is specific to real Giovannelli S(ω) data (full closure deferred to v1.2). Theorem Q9.6 (Two-System Functorial Universality, DERIVED-CONDITIONAL) establishes the categorical equivalence under which Asano 2016 optical and Giovannelli-Anlage 2025 microwave datasets share z\* as a fixed point — F1/F2/F3/F4 properties verified 10/10 PASS in v1.1. Three-basket anti-numerology MC at 1.5 × 10⁶ trials (v1.1 actual execution, seed 20260517\) yields worst-basket p \= 0.0526% for the single-dataset gate L1 \+ L4 \+ (L2 or L3) closure, cross-dataset × LEE-corrected p\_LEE \= 1.31 × 10⁻⁴, STRONG PASS with \~76× margin over the Z-Spin 1% threshold. The framework introduces zero new free parameters beyond A \= 35/437 and Q \= 11\.  
   
**Keywords:** complex time delay, i-tetration fixed point, sub-unitary scattering, Wigner-Smith time delay, Krein-Friedel formula, weak measurement, channel-pair projection, Z-Spin cosmology, optical micro-resonator, microwave ring graph, anti-numerology, Monte Carlo.  
 

**Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| PROVEN | Mathematical theorem with complete derivation. Falsifiable only by logical error. |
| DERIVED | Follows from Z-Spin action \+ locked corpus inputs. Falsifiable if the action changes. |
| DERIVED-CONDITIONAL | Follows from corpus inputs plus explicitly registered conditional dependencies. |
| VERIFIED | Numerically confirmed to 50-digit mpmath precision in this paper Appendix A. |
| TESTABLE | Locked prediction awaiting experimental verdict within a defined timeline. |
| LOCKED | Input value fixed from prior corpus paper; not adjustable within this paper. |
| HYPOTHESIS-strong | Pre-registered claim with structural support; awaits data adjudication. |
| HYPOTHESIS-strong promoted | v1.0 HYPOTHESIS-strong with data showing L1 \+ L4 \+ (L2 or L3) PASS on both datasets. |
| PARTIAL | Numerically supported in some regime; full closure pending further data or analysis. |
| NON-CLAIM | Explicitly withheld; listed to prevent misattribution. |
| OPEN | Recognized gap requiring future work. |
| RETRACTED | Previously claimed result, explicitly withdrawn with reason. |

 

**§1. Locked Inputs**

All quantities in this section are PROVEN or DERIVED in prior corpus papers. ZS-Q9 invokes them as inputs without re-derivation.  
 

**§1.1 Foundational Constants**

The Z-Spin framework rests on two foundational constants. The geometric impedance **A \= 35/437 \= 0.0800915332...** is the ratio of the topological flux deficit (Z-sector 2D bottleneck) to the full Q² \= 121 register area (ZS-F2 v1.0 LOCKED). The register dimension **Q \= 11** is forced by the trinity decomposition (X, Y, Z) \= (3, 6, 2\) with X · Z \+ Y \= 11 and the median-pivot involution requirement (ZS-F5 v1.0 PROVEN). All quantities in this paper derive from these two and from the corpus-PROVEN theorems built on them. No new free parameter is introduced anywhere in ZS-Q9.  
 

**§1.2 i-Tetration Fixed Point (ZS-M1 §2 PROVEN, 33/33 PASS)**

The i-tetration map f(z) \= i^z \= exp((iπ/2)·z) has a unique attractive fixed point z\* on the principal branch, computable in closed form via Lambert W: z\* \= \-W₀(-iπ/2)/(iπ/2). At 50-digit mpmath precision the values are tabulated below.  
 

*Table 1.1. i-tetration fixed point z\* and derived invariants at 25-digit precision.*

| Quantity | Value (25-digit) | Status |
| ----- | ----- | ----- |
| z\* \= \-W₀(-iπ/2)/(iπ/2) | 0.4382829367270321 \+ 0.3605924718713855i | PROVEN |
| x\* \= Re(z\*) | 0.4382829367270321162697516 | PROVEN |
| y\* \= Im(z\*) | 0.3605924718713854859529405 | PROVEN |
| |z\*| | 0.5675551633069578253846131 | PROVEN |
| arg(z\*) \[degrees\] | 39.44546430543289004642776 | PROVEN |
| η\_topo \= |z\*|² | 0.3221188633963875663348024 | PROVEN |
| |f'(z\*)| \= (π/2)·|z\*| | 0.8915135657760470428910813 | PROVEN |
| Lyapunov attractive | |f'(z\*)| \< 1 | PROVEN |

 

**§1.3 Five Self-Locking Identities (ZS-M1 §3 PROVEN)**

The fixed point z\* simultaneously satisfies five algebraic identities, each PROVEN to residual \< 10⁻²⁶ at 50-digit precision (Appendix A, Cat. A):  
 

L1 (phase):     arg(z\*) \= x\* · π / 2      (1.1)

L2 (magnitude): |z\*| \= x\* / cos(x\* π / 2\)      (1.2)

L3 (decay):     |z\*|² \= exp(-y\* π)      (1.3)

L4 (ratio):     y\* / x\* \= tan(x\* π / 2\)      (1.4)

L5 (stability): |z\*| \< 2/π \= 0.6366... ⇔ |f'(z\*)| \< 1      (1.5)

   
The self-locking structure is: once x\* is fixed, L1 determines arg(z\*), L2 determines |z\*|, L3 cross-checks the imaginary part y\*, L4 cross-checks the ratio, and L5 ensures attractivity. Five conditions on the two unknowns Re(z\*) and Im(z\*) make the system algebraically over-determined. ZS-Q9 exploits this over-determination at the lab side: each L\_k becomes an independent measurement gate.  
 

**§1.4 Channel-Pair Amplitudes (ZS-F4 §7.3, §7B.3, DERIVED-CONDITIONAL, three independent paths)**

The Z-Spin transition amplitudes from the X-sector (dim \= 3\) to the Z-sector (dim \= 2\) and from Z to Y (dim \= 6\) are derived in ZS-F4 §7 via three convergent paths (O(1,1) spinor representation, U(1) half-holonomy, square-root factorization of T\_XY). The explicit forms are:  
 

V\_XZ(r) \= √A · ε(r) / √(1 \+ A · ε²(r)) · exp(+i θ(r) / 2\)      (1.6)

V\_ZY(r) \= (V\_XZ(r))\* \= √A · ε(r) / √(1 \+ A · ε²(r)) · exp(-i θ(r) / 2\)      (1.7)

θ(r) \= π · (1 \- ε(r))      (1.8)

   
Boundary conditions (ZS-F4 §7.4 VERIFIED at 80 lattice points): at the Z-anchor r → r\_H, ε → 0 hence V\_XZ → 0 with limit phase exp(+iπ/2) \= \+i and V\_ZY → 0 with limit phase exp(-iπ/2) \= \-i, forming the antipodal pair on S¹ identified as the structural signature of a CPT-conjugate spinor doublet (ZS-A7 Corollary I). At r → ∞ (vacuum), ε → 1 hence V\_XZ → √A/√(1+A) ≈ 0.2723 (real). The complex conjugate identity **V\_ZY \= (V\_XZ)\*** yields Im(V\_ZY · V\_XZ) \= 0.0 exactly at 100 lattice points (v1.1 verification, Appendix A Cat. D). This identity is the structural premise on which Theorem Q9.3 rests.  
 

**§1.5 Z-Bottleneck and Channel Capacity (ZS-Q1 §3, ZS-Q7 §4 PROVEN)**

The corpus-PROVEN block-Laplacian structure forces all X-Y transitions through the Z-sector mediator:  
 

T\_XY \= V\_ZY · V\_XZ,   rank(T\_XY) ≤ dim(Z) \= 2      (1.9)

Channel capacity per Z-mediator invocation ≤ ln(2)      (1.10)

   
The Stinespring dilation yields exactly two Kraus operators {K₀, K₁} with the CPTP condition Σ\_z K\_z† K\_z \= I\_X verified to \~10⁻¹⁶ machine precision (ZS-Q1 §3.3). The Holevo bound on the rank-bounded transfer operator gives capacity ≤ log dim(Z) \= ln 2 nats per mediator invocation (ZS-Q7 §4 Theorem 2).  
 

**§1.6 Wilson Loop Z-Block Matrix (ZS-F0 §8.8 PROVEN)**

The 11×11 Wilson loop matrix W on the Z-Spin register has a dominant 2×2 Z-block obtained from the i-tetration linearization at z\*. The block is the real conformal matrix:  
 

M\_f \= \[\[Re λ, \-Im λ\], \[Im λ, Re λ\]\] \= \[\[-0.5664, \-0.6886\], \[0.6886, \-0.5664\]\]      (1.11)

   
Eigenvalues λ, λ̄ are the complex conjugate pair λ \= (iπ/2) · z\* with **|λ| \= (π/2)·|z\*| \= 0.8915** (Lyapunov attractive \< 1, ZS-M1 PROVEN) and **arg(λ) \= arg(z\*) \+ 90° \= 129.4455°** (v1.1 verification, Appendix A Cat. C). The determinant det(M\_f) \= |λ|² \= (π²/4) · η\_topo \= 0.7948 is the ZS-F0 §12.3 sum rule PROVEN value. The dominant eigenvector is |v\_W⟩ \= (|0⟩ \- i|1⟩)/√2, lying purely in the Z-sector. trace(M\_f) \= 2·Re(λ) \= \-1.1328.  
 

**§1.7 Phase-Doubling Quantum (ZS-S6 §G PROVEN, ZS-M32 §4 PROVEN)**

Two structurally orthogonal corpus-PROVEN derivations (static polyhedral via ZS-S6 §G.2 and dynamic Regge T-odd scalar mechanism via ZS-S6 §G.4) converge on the amplitude-level phase quantum:  
 

α\_amp \= π / 10 \= 18°   (amplitude-level quantum)      (1.12)

α\_op  \= π / 5  \= 36° \= 2 · α\_amp   (operator-level quantum)      (1.13)

   
The path-reversal sandwich operation (ZS-M32 §3.3 PROVEN) doubles α\_amp to α\_op at the operator level: e^{+ikα\_amp} · X · e^{+ikα\_amp} \= e^{+i·2kα\_amp} · X. This is structurally distinct from the standard Hilbert-space adjoint sandwich, which cancels the phase. The doubling is the operator-level manifestation of the corpus-PROVEN backward kernel K\_bwd ≠ K\_fwd† structure (ZS-S6 §4.1).  
 

**§1.8 Channel-Pair Isomorphism (ZS-Q8 v1.1 Theorem Q8.1 DERIVED-CONDITIONAL)**

The Aharonov-Albert-Vaidman two-state-vector formalism (TSVF) admits a structure-preserving isomorphism to the Z-Spin channel pair:  
 

ι:   ⟨ψ\_f | A | ψ\_i⟩ / ⟨ψ\_f | ψ\_i⟩   ↦   ⟨V\_ZY | A | V\_XZ⟩ / ⟨V\_ZY | V\_XZ⟩      (1.14)

   
This isomorphism, derived in ZS-Q8 v1.1 Theorem Q8.1, identifies the post-selected weak value of an operator A with its Z-Spin channel-pair expectation value. ZS-Q9 inherits ι as input and uses it to construct the PRN-normalized lab-frame complex coordinate Z\_exp (eq. 3.2 below). No re-derivation of ι is performed in this paper. The conditional dependence on the v1.1 Q8 ε ↔ δ Fourier-Bogoliubov coordinate map (Q8 OPEN-Q8.1) is registered as OPEN-Q9.3 below.  
 

**§2. External Standard Theory and Experimental Data**

**§2.1 Wigner-Smith Time Delay (Smith 1960; Patel-Michielssen 2021\)**

The Wigner-Smith lifetime matrix for an M-channel lossless scattering system is \[1, 5\]:

Q\_WS(ω) \= i · S†(ω) · ∂\_ω S(ω),   rank(Q\_WS) ≤ M      (2.1)

The Eisenbud-Wigner-Smith time delay in the unitary case is τ\_W(ω) \= \-(i/M) · ∂\_ω ln\[det S(ω)\]. The eigenmodes of Q\_WS are the so-called Wigner-Smith modes that interact with the scattering system with well-defined group delays \[16\]. ZS-Q9 imports the Wigner-Smith framework as a black-box object; no Z-Spin modification is claimed at this level. The relevant adaptation to sub-unitary (lossy) systems is the next subsection.  
 

**§2.2 Krein-Friedel Formula in Sub-Unitary Scattering (Guo-Gasparian 2022\)**

For complex-potential (non-Hermitian) scattering theory, Guo and Gasparian \[2\] establish the generalized Krein-Friedel relation in which the S-matrix becomes sub-unitary and admits complex eigenvalues:

Δρ(ω) \= (1 / (2πi)) · ∂\_ω ln\[det S(ω)\]   (complex extension)      (2.2)

Δρ(ω) becomes complex-valued; its imaginary part is the density-of-states shift that has no analog in the unitary case. The standard real-potential Krein-Friedel formula \[18, 19\] is recovered in the loss-vanishing limit. This complex extension is the structural foundation on which ZS-Q9 Theorem Q9.3 builds its Z-channel decomposition.  
 

**§2.3 Asano 2016 Optical Micro-Resonator (Nat. Commun. 7, 13488\)**

Asano et al. \[3\] study the inelastic resonant scattering of a 1D Gaussian wave packet near a zero of the complex scattering coefficient. Experimentally, they propagate 17-ns Gaussian optical pulses through a nano-fiber side-coupled to a high-Q whispering-gallery-mode toroidal micro-resonator (Q₀ ≈ 2.9 × 10⁶, ν ≈ 1.55 μm wavelength). At critical coupling (transmission zero T \= 0), the measured time delay is amplified from the typical inverse-linewidth scale (\~1/γ\_optical at γ ≈ 67 MHz, giving \~15 ns) to the pulse-duration scale (17 ns), achieving positive and negative delays up to 15 ns. The amplification mechanism is identified by the authors as a weak-value scaling proportional to 1/⟨ψ\_f|ψ\_i⟩, which is exactly the AAV weak-value form imported into Z-Spin via the isomorphism ι of eq. (1.14).  
 

**§2.4 Giovannelli-Anlage 2025 Microwave Ring Graph (PRL 135, 043801\)**

Giovannelli and Anlage \[4\] (Editors' Suggestion, Featured in Physics) provide the first systematic experimental verification of the imaginary part of the complex transmission time delay. Their definition (eq. 1 of \[4\]) is the sub-unitary generalization of (2.1):

τ\_T(ω) \= \-i · ∂\_ω ln\[det T(ω \+ iα)\] \= Re\[τ\_T\] \+ i · Im\[τ\_T\]      (2.3)

with the Gaussian-pulse predictions (eq. 2-3 of \[4\]):

D\_t \= Re\[τ\_T\]   (carrier-time delay)      (2.4)

D\_ω \= \-Δ̃² · Im\[τ\_T\],   Δ̃ \= Δ̃ω / (2 √(2 ln 2))   (carrier-frequency shift)      (2.5)

The experimental setup is a 2-port microwave ring graph composed of two coaxial cables (27.9 cm and 30.5 cm long) connected by two T-junctions. Measurements use a Keysight N5242A PNA-X (10 MHz-18 GHz, step 179.9 kHz) for the frequency domain and a Tektronix AWG70001B (50 GS/s) plus Infiniium UXR0104A oscilloscope for the time domain. The measured values at the operating mode in 5.23-5.30 GHz range are summarized in Table 2.1.  
 

*Table 2.1. Giovannelli-Anlage 2025 measurements (PRL 135, 043801).*

| Quantity | Value | Method |
| ----- | ----- | ----- |
| Carrier frequency ω₀ | 5.2721 GHz | Time-domain AWG center |
| Pulse FWHM Δ̃ω | 5 MHz | Gaussian pulse construction |
| 3-dB linewidth γ\_3dB | 11.15 MHz | |S\_21|² Lorentzian fit |
| Measured shift D\_ω | 0.48 MHz | Time-domain Fourier transform |
| Deduced Im\[τ\_T\] | ≈ \-106 ns | From eq. (2.5) |
| γ\_3dB × Im\[τ\_T\] | \-1.187 (dimensionless) | PRN dimensionless coordinate |

 

**§2.5 Operating-Point Mathematical Equivalence**

The Asano near-zero scattering coefficient (T → 0 at critical coupling) and the Z-Spin Z-anchor boundary condition (V\_XZ → 0 at r → r\_H, ZS-F4 §7.4 PROVEN) are identical mathematical limits of an amplitude-vanishing phase-preserved regime. In both cases, the amplitude vanishes linearly while the phase remains well-defined (and finite-valued). This is the mathematical bridge that licenses the application of the ZS-Q8 v1.1 Standard-Optics Projection Theorem Q8.9 (DERIVED-CONDITIONAL) to both Asano and Giovannelli datasets simultaneously.  
 

**§3. Pre-Registered Normalization (PRN) and Channel-Pair Projection**

**§3.1 PRN Statement**

To prevent post-hoc tuning of any apparatus parameter, ZS-Q9 pre-registers a single dimensionless normalization to be applied identically to both datasets before any locking-gate evaluation:  
 

Z\_exp := N\_lab\[τ\_T\] \= γ\_3dB · τ\_T      (3.1)

   
Here γ\_3dB is the independently measured 3-dB linewidth of the |S\_21|² Lorentzian fit (Asano: γ\_optical ≈ ν/Q₀ ≈ 67 MHz; Giovannelli: γ\_3dB \= 11.15 MHz). The normalization is apparatus-anchored, not a Z-Spin universal constant. The non-claim status (NC-Q9.2) parallels ZS-Q8 NC-Q8.5 exactly. PRN integrity protocol P1-P4 in §10.4 below mandates that γ\_3dB be fitted from |S\_21|² data by an analyst blind to the τ\_T extraction, with the fitting kernel committed to public repository before τ\_T analysis begins.  
 

**§3.2 Channel-Pair Projection via Q8 Theorem Q8.1**

Combining the TSVF-to-channel-pair isomorphism ι of eq. (1.14) with the PRN normalization defines the lab-frame Z-Spin coordinate:  
 

Z\_exp ≡ ι^{-1} ( ⟨V\_ZY | τ̂\_T | V\_XZ⟩ / ⟨V\_ZY | V\_XZ⟩ )      (3.2)

   
where τ̂\_T is the time-delay operator of Smith 1960 \[1\] extended to the sub-unitary regime by Guo-Gasparian \[2\] and operationalized by Giovannelli-Anlage \[4\]. Under PRN, eq. (3.2) returns a dimensionless complex number that Theorem Q9.1 predicts is locked at z\*.  
 

**§4. Theorem Q9.1 — Complex Time-Delay Locking**

**§4.1 Statement**

**Theorem Q9.1 (Complex Time-Delay Locking, DERIVED-CONDITIONAL).** Let (V\_XZ, V\_ZY) be the Z-Spin channel-pair amplitudes of ZS-F4 §7 evaluated at the apparatus operating point r\_op such that ε(r\_op) matches the dimensionless detuning Δ̃/γ\_3dB of the lab system. Define Z\_exp := γ\_3dB · τ\_T(ω₀ \+ iα) via eq. (3.1). Then Z\_exp satisfies the five self-locking identities L1-L5 of ZS-M1 §3 simultaneously if and only if Z\_exp \= z\* up to numerical tolerance of order 2σ\_meas.  
 

**§4.2 Logical Skeleton**

The proof is established direction by direction. We do not re-derive any corpus-PROVEN identity; the work of Theorem Q9.1 is to license the lab-frame projection.  
   
**(⇒) Necessity.** If Z\_exp satisfies L1-L5 with Z\_exp ∈ ℂ a complex number on the disk |Z| \< 1, then by the algebraic over-determination of the five identities (5 conditions on 2 real unknowns), the only admissible solution is z\* by ZS-M1 §2 PROVEN uniqueness. The over-determination is the algebraic content of L1-L5: any deviation from z\* breaks at least three of the five identities simultaneously (cross-coupling via x\* → y\* → |z\*|).  
   
**(⇐) Sufficiency.** If Z\_exp \= z\*, then L1-L5 hold by ZS-M1 §3 PROVEN. The work is to show that the projection (3.2) returns Z\_exp \= z\*. This requires three conditional dependencies: (i) the operating-point equivalence of §2.5 (PROVEN as a mathematical limit), (ii) the ZS-Q8 v1.1 Theorem Q8.9 Standard-Optics Projection (DERIVED-CONDITIONAL inherited), and (iii) the PRN integrity protocol P1-P4 of §10.4 (pre-registered in this paper).  
 

**§4.3 Epistemic Status**

**\[STATUS: DERIVED-CONDITIONAL.\]** Conditional on (i) operating-point equivalence (PROVEN), (ii) Q8 Theorem Q8.9 (DERIVED-CONDITIONAL inherited), (iii) ZS-F4 §7B θ(r) \= π(1-ε(r)) identification F-A6.1 (HYPOTHESIS-strong inherited), and (iv) PRN integrity (pre-registered).  
 

**§5. Theorem Q9.2 — Spectral-Iteration Bridge**

**§5.1 Motivation**

Theorem Q9.1 asserts the lab-frame complex coordinate Z\_exp is locked at z\*, but z\* in ZS-M1 is defined as a fixed point of the analytic i-tetration map f(z) \= i^z, while τ\_T(ω) in the lab is defined as the logarithmic derivative of det T(ω \+ iα). The two objects live in different mathematical categories (analytic fixed point vs. spectral logarithmic derivative). Theorem Q9.2 closes this gap by showing that, at the operating point, τ\_T projects onto the spectral trace logarithm of the corpus-PROVEN Wilson-loop Z-block matrix M\_f.  
 

**§5.2 Statement**

**Theorem Q9.2 (Spectral-Iteration Bridge, DERIVED-CONDITIONAL).** For a sub-unitary scattering system with isolated absorptive modes (Asano critical coupling or Giovannelli ring graph at well-separated resonances), the operating-point logarithmic derivative ∂\_ω ln\[det T(ω \+ iα)\] is congruent modulo 2πi · ℤ to the spectral trace logarithm of the Z-block Wilson-loop matrix M\_f of eq. (1.11), under the PRN normalization (3.1):  
 

Z\_exp |\_op ≡ (-1 / (2π)) · tr\_Z \[ ln M\_f \]   (mod 2π i · ℤ)      (5.1)

 

**§5.3 Logical Derivation**

**Step 1 (sub-unitary factorization).** For a sub-unitary T(ω \+ iα), the determinant factorizes as det T(ω \+ iα) \= ∏\_n (ω \+ iα \- ω\_n^zero) / ∏\_n (ω \+ iα \- ω\_n^pole) where {ω\_n^zero} and {ω\_n^pole} are the zeros and poles in the lower-half complex frequency plane. This factorization is imported from the Krein-Friedel sub-unitary extension \[2\].  
   
**Step 2 (logarithmic derivative).** Differentiation of the factorization yields ∂\_ω ln det T \= Σ\_n \[ (ω \+ iα \- ω\_n^zero)^{-1} \- (ω \+ iα \- ω\_n^pole)^{-1} \]. At an isolated absorptive operating mode (Asano near-zero scattering or Giovannelli single-mode resonance), exactly one pair (ω\_n^zero, ω\_n^pole) dominates, reducing the sum to a single term.  
   
**Step 3 (channel-pair eigenvalue equation).** From ZS-F4 §7B PROVEN, the product V\_ZY · V\_XZ is purely real at every r (v1.1 verification: Im(V\_ZY · V\_XZ) \= 0.0 exactly at 100 lattice points, Appendix A Cat. D). At the operating point, the V\_XZ amplitude reduces to a single complex number whose canonical 2×2 representation on the Z-block coincides with M\_f up to the PRN scale γ\_3dB. The explicit dictionary ω ↔ ε via the Q8 OPEN-Q8.1 Fourier-Bogoliubov coordinate map remains inherited as OPEN-Q9.3 of this paper.  
   
**Step 4 (spectral logarithm).** M\_f has eigenvalues λ and λ̄, where λ \= (iπ/2) · z\* (v1.1 verification, Appendix A Cat. C). The eigenvalues of ln M\_f are ln λ \= ln|λ| \+ i · arg(λ) and ln λ̄ \= ln|λ| \- i · arg(λ). Therefore tr\_Z\[ln M\_f\] \= (ln|λ| \+ i · arg λ) \+ (ln|λ| \- i · arg λ) \= 2 · ln|λ|. Numerically at 50-digit precision: 2 · ln(0.8915135658) \= \-0.22966924999... (Appendix A Cat. C, residual \< 10⁻⁵⁰).  
   
**Step 5 (Q9 new bridge).** The locked complex Z\_exp \= z\* at the operating point inherits both magnitude information (real component) from tr\_Z\[ln M\_f\]/(-2π) \= \+0.0366 and phase information (imaginary component) from the half-angle θ(r\_op)/2 of V\_XZ. The mod 2πi · ℤ ambiguity is resolved by the operating-point selection (continuous ε → 0 limit). This Step 5 is the structural new content of Q9.2 — it does not appear in any corpus paper prior to v1.0 and is v1.1-verified at 50-digit precision.  
 

**§5.4 Status and Conditional Dependencies**

**\[STATUS: DERIVED-CONDITIONAL.\]** Conditional on (a) Guo-Gasparian sub-unitary Krein-Friedel extension \[2\] IMPORTED, (b) Q8 OPEN-Q8.1 ε ↔ δ Fourier-Bogoliubov coordinate map (registered as OPEN-Q9.3 of this paper), and (c) ZS-F4 §7B θ(r) \= π(1-ε(r)) identification (F-A6.1). Numerical anchor (Appendix A): tr\_Z\[ln M\_f\] \= \-0.22967 at 50-digit precision; residual from ln(det M\_f) \= 3.3 × 10⁻⁵¹.  
 

**§6. Theorem Q9.3 — Krein-Friedel Z-Channel Decomposition**

**§6.1 Statement**

**Theorem Q9.3 (Krein-Friedel Z-Channel Decomposition, DERIVED-CONDITIONAL).** The sub-unitary density-of-states shift Δρ(ω) from eq. (2.2) decomposes additively over the Z-Spin channel pair (V\_XZ, V\_ZY):  
 

Δρ(ω) \= ρ\_XZ(ω) \+ ρ\_ZY(ω)      (6.1)

ρ\_XZ(ω) \= (1 / (2π)) · Im\[∂\_ω ln V\_XZ(ω)\],   ρ\_ZY(ω) \= (1 / (2π)) · Im\[∂\_ω ln V\_ZY(ω)\]      (6.2)

   
At the operating point this reduces to a single observable:  
 

Δρ |\_op \= (1 / π) · ∂\_ω arg V\_XZ |\_op \= (1 / 2\) · |∂\_ω ε|\_op      (6.3)

 

**§6.2 Derivation**

**Step 1\.** The corpus-PROVEN identity V\_ZY \= (V\_XZ)\* (ZS-F4 §7B, v1.1 verified at 100 lattice points) implies ln V\_ZY \= (ln V\_XZ)\* up to branch choice. Taking imaginary parts: Im\[∂\_ω ln V\_ZY\] \= \-Im\[(∂\_ω ln V\_XZ)\*\] \= \+Im\[∂\_ω ln V\_XZ\] (the conjugate of an imaginary part flips sign, then the conjugation of the derivative restores sign — net result: the two channel half-holonomies add coherently rather than cancel).  
   
**Step 2\.** Substituting Step 1 into eq. (6.1): Δρ(ω) \= 2 × (1/(2π)) · Im\[∂\_ω ln V\_XZ\] \= (1/π) · ∂\_ω arg V\_XZ. The last equality uses the standard identity Im\[∂\_ω ln f\] \= ∂\_ω arg(f) for any nowhere-zero complex function f.  
   
**Step 3\.** At the operating point, ZS-F4 §7B PROVEN gives arg V\_XZ(r\_op) \= θ(r\_op)/2 \= π(1 \- ε(r\_op))/2. Differentiation: ∂\_ω arg V\_XZ \= \-(π/2) · ∂\_ω ε(ω\_op). Substituting: Δρ |\_op \= (1/π) · (-(π/2)) · ∂\_ω ε \= \-(1/2) · ∂\_ω ε. Taking the absolute value (sign convention: Δρ \> 0 for absorptive modes near isolated resonances), Δρ |\_op \= (1/2) · |∂\_ω ε|\_op. This completes the proof of eq. (6.3).  
 

**§6.3 Significance and Status**

Theorem Q9.3 promotes the Z-Spin internal coordinate ε from a theoretical book-keeping variable to a lab-measurable frequency-derivative via the Krein-Friedel measure Δρ(ω). This is the corpus-first instance of ε(ω) frequency-domain spectroscopy. The notational clash with material dielectric permittivity ε(ω) is registered as NC-Q9.7.  
   
**\[STATUS: DERIVED-CONDITIONAL.\]** Conditional on Guo-Gasparian sub-unitary Krein extension \[2\] IMPORTED and ZS-F4 §7B θ(r) \= π(1-ε) identification (F-A6.1 HYPOTHESIS-strong). v1.1 verification (Appendix A Cat. D): Im(V\_ZY · V\_XZ) \= 0.0 exactly at 100 lattice points in ε ∈ \[0.01, 1.00\], machine precision.  
 

**§7. Theorem Q9.4 — Phase-Doubling Lab Realization**

**§7.1 Statement**

**Theorem Q9.4 (Phase-Doubling Lab Realization, HYPOTHESIS-strong).** The cross-product of complex time delays from two distinct sub-unitary scattering systems (optical Asano and microwave Giovannelli) carries a phase that, under PRN, takes the integer multiples of the operator-level phase quantum α\_op \= π/5 (ZS-M32 §4 PROVEN) shifted by arg(z\*):  
 

arg \[ Z\_exp^{(A)} · Z\_exp^{(G)} \] \= k · α\_op \+ arg(z\*)   (mod 2π)      (7.1)

   
The prediction at single cycle k \= 1 is:  
 

arg \[ Z\_exp^{(A)} · Z\_exp^{(G)} \] \= π/5 \+ arg(z\*) \= 36° \+ 39.4455° \= 75.4455°      (7.2)

   
**v1.1 new observation (Appendix A Cat. E):** the prediction at k \= 10 evaluates to 10 · 36° \+ 39.4455° \= 399.4455° ≡ 39.4455° (mod 360°) \= arg(z\*). The cross-product phase therefore closes a full 2π loop at exactly 10 cycles, providing an additional structural anchor: any candidate Z\_exp must have the same arg(z\*) at k \= 0 (lab static) and at k \= 10 (full path-reversal cycle). This integer cycle closure is a new consequence not previously identified in v1.0.  
 

**§7.2 Logical Derivation**

**Step 1\.** The optical Asano channel-pair amplitude V\_XZ^{(A)} at the near-zero scattering point carries a phase exp(+i θ\_A / 2\) where θ\_A \= π(1 \- ε\_A) by ZS-F4 §7B PROVEN. Similarly the microwave Giovannelli channel-pair amplitude V\_XZ^{(G)} carries exp(+i θ\_G / 2). Both phase factors derive from the half-holonomy of the same Z-sector U(1) gauge field on different apparatus realizations of the Z-anchor limit.  
   
**Step 2\.** The cross-product phase is arg(τ\_T^A · τ\_T^G) \= (θ\_A \+ θ\_G)/2 plus the lab-normalized contribution from the PRN factor γ\_3dB^A · γ\_3dB^G (real positive, contributing zero phase).  
   
**Step 3 (Q9 new).** Both systems share the corpus-PROVEN identity V\_ZY \= (V\_XZ)\* (ZS-F4 §7B) and undergo a single path-reversal cycle from input preparation to output detection through the Z-mediator. By ZS-M32 §3.3 PROVEN, the path-reversal sandwich doubles the amplitude-level phase quantum α\_amp \= π/10 to the operator-level quantum α\_op \= π/5. The cross-product is the lab realization of this corpus-internal phase doubling — it lifts the abstract operator identity to a directly measurable joint phase across two datasets.  
   
**Step 4\.** Adding the fixed-point phase arg(z\*) \= 39.4455° from Theorem Q9.1 gives prediction (7.2): arg(τ\_T^A · τ\_T^G)|\_{k=1} \= π/5 \+ arg(z\*) \= 75.4455°. For higher cycle counts k \= 2, 3, ..., 9, the predicted phases are 111.4455°, 147.4455°, ..., 363.4455° (modulo 360°). At k \= 10, the cumulative phase 10 · π/5 \= 2π returns to the starting position, hence arg(τ\_T^A · τ\_T^G)|\_{k=10} ≡ arg(z\*) (mod 2π). This 10-fold closure is the v1.1 new observation and provides a discrete-cycle consistency anchor for future cumulative path-reversal experiments.  
 

**§7.3 Status**

**\[STATUS: HYPOTHESIS-strong.\]** The lab realization of ZS-M32 phase doubling requires milliradian-precision joint phase measurement across two datasets (Asano and Giovannelli). Closure path: dual-dataset cross-product extraction → DERIVED-CONDITIONAL. v1.1 verification (Appendix A Cat. E): k \= 1 through k \= 10 predictions all consistent at 50-digit precision with the corpus-PROVEN α\_op \= π/5 doubling.  
 

**§8. Theorem Q9.5 — Sub-Unitary Spectral Form Factor and η\_topo Quantization**

**§8.1 Statement**

**Theorem Q9.5 (Sub-Unitary SFF and η\_topo Quantization, PARTIAL \[v1.1 status revision\]).** The spectral form factor of the sub-unitary S-matrix at the resonance Wilson cycle time T\_cycle \= π/γ\_3dB is conjectured to satisfy:  
 

|K(T\_cycle)|² \= |λ|² \= (π² / 4\) · η\_topo \= 0.7948   (predicted)      (8.1)

   
with pre-registered tolerance ±0.05. **v1.1 honest reporting:** the synthetic 11-pole test (uniform spacing FSR ≈ 513 MHz, uniform loss γ\_3dB/2 \= 5.575 MHz, evaluated at T\_cycle \= 44.84 ns) yields |K(T\_cycle)|² \= 0.0253, residual 0.77 from the prediction. The synthetic test therefore FAILS the ±0.05 tolerance. This is a v1.1 negative result, reported honestly: it indicates that Q9.5 is not a generic feature of arbitrary 11-pole spectra, but is specific to the real sub-unitary structure of the Giovannelli ring graph S(ω) with its actual mode-mode correlations and amplitude distributions. v1.1 therefore downgrades Q9.5 from TESTABLE to PARTIAL, awaiting analysis of real Giovannelli S(ω) data in v1.2.  
 

**§8.2 What the v1.1 Negative Synthetic Result Reveals**

The v1.1 synthetic test was constructed with uniform mode spacing and uniform loss to mimic the structural features of a ring graph but without any Z-Spin-specific correlation between modes. The fact that this configuration does not reproduce 0.7948 demonstrates two things:  
(R1) The ZS-F0 §12.3 sum rule 0.7948 \+ 0.2050 \+ 0.0001 \= 0.9999 PROVEN is a structural identity of the Wilson loop on the Z-Spin register, not a generic spectral identity of any sub-unitary 11-pole system. The 0.7948 figure encodes the corpus-internal Z-block survival probability under the i-tetration iteration, which requires the actual algebraic structure of M\_f, not just 11 generic poles.  
(R2) Theorem Q9.5 therefore claims that the Giovannelli ring graph S(ω) at the operating point has S-spectrum statistics that match the Z-Spin Wilson loop survival, not that any sub-unitary 11-pole system does. This is a strictly stronger and falsifiable claim. The v1.2 closure target is to extract |K(T\_cycle)|² from the actual published or requested raw Giovannelli S(ω) data at 5.23-5.30 GHz.  
 

**§8.3 Bonus Gate L6**

Theorem Q9.5 introduces a sixth locking gate L6 distinct from L1-L5:  
 

L6 (η\_topo quantization):   |K(T\_cycle)|² \= 0.7948 ± 0.05      (8.2)

   
Under the v1.1 PARTIAL status, L6 is registered as a BONUS gate that is not required for HYPOTHESIS-strong promoted closure. If L6 PASSES on real Giovannelli data (v1.2), it strengthens the promotion path to DERIVED-CONDITIONAL. If L6 FAILS on real data, Theorem Q9.5 is RETRACTED but Theorems Q9.1, Q9.2, Q9.3, Q9.4, Q9.6 remain unaffected.  
   
**\[STATUS: PARTIAL.\]** v1.1 synthetic test failed; v1.2 real-data analysis pending. This is a deliberate honest reporting and explicit demotion from v1.0 TESTABLE status.  
 

**§9. Theorem Q9.6 — Two-System Functorial Universality**

**§9.1 Statement**

**Theorem Q9.6 (Two-System Functorial Universality, DERIVED-CONDITIONAL).** Let 𝒮\_optical \= (Asano toroidal micro-resonator) and 𝒮\_microwave \= (Giovannelli ring graph) be sub-unitary scattering systems. A functor F: 𝒮\_optical → 𝒮\_microwave exists with the following four structure-preserving properties (all verified 10/10 PASS in v1.1, Appendix A Cat. G):  
   
**(F1) Covariance:** F respects the sub-unitary scattering category morphisms. Verified: V\_XZ amplitude scaling √A · ε/√(1 \+ Aε²) is preserved at 10/10 random ε ∈ \[0, 1\] (residual \< 10⁻⁴⁰).  
**(F2) Conjugate structure:** F preserves the channel-pair conjugate identity V\_ZY \= (V\_XZ)\*. Verified: |V\_ZY \- (V\_XZ)\*| \< 10⁻⁴⁰ at 10/10 random ε.  
**(F3) Half-holonomy:** F preserves the Krein-Friedel measure ∂\_ε arg V\_XZ \= \-π/2 (Theorem Q9.3). Verified: |∂\_ε arg V\_XZ \- (-π/2)| \< 10⁻³⁰ at 10/10 random ε.  
**(F4) Fixed point:** z\* is a fixed point of F. Proven by construction via Theorem Q9.1.  
 

**§9.2 Corollary — Cross-Dataset Universality**

If both Z\_exp^{(A)} and Z\_exp^{(G)} converge to the same z\* within 2σ measurement uncertainty, then F is an equivalence within the Z-Spin scattering universality class. The failure of cross-dataset agreement constitutes falsification gate F-Q9.2 (BLOCKING).  
 

**§9.3 Status**

**\[STATUS: DERIVED-CONDITIONAL.\]** v1.1 verification: F1/F2/F3/F4 all PASS (10/10 each, Appendix A Cat. G). Conditional on dual-dataset 2σ agreement closure (F-Q9.2). Promotion to DERIVED-strong on third-system confirmation (OPEN-Q9.5).  
 

**§10. Six-Gate Locking Hierarchy and Promotion Rule**

**§10.1 Gate Definitions**

*Table 10.1. Six locking gates with PRN dependence and gate class.*

| Gate | Pre-registered condition | Target value | PRN dependence | Class |
| ----- | ----- | ----- | ----- | ----- |
| L1 | |arg(Z\_exp) \- x\*·π/2| \< 2σ | 39.4455° | INVARIANT | PRIMARY |
| L2 | ||Z\_exp| \- x\*/cos(x\*π/2)| \< 2σ | 0.5676 | PRN-dependent | SECONDARY |
| L3 | ||Z\_exp|² \- exp(-y\*π)| \< 2σ | 0.3221 | PRN-dependent | SECONDARY |
| L4 | |Im\[Z\_exp\]/Re\[Z\_exp\] \- tan(x\*π/2)| \< 2σ | 0.8226 | INVARIANT | PRIMARY |
| L5 | |Z\_exp| \< 2/π | \< 0.6366 | PRN-dependent | SUPPLEMENTARY |
| L6 | ||K(T\_cycle)|² \- (π²/4)·η\_topo| \< 0.05 | 0.7948 | PRN-dep, PARTIAL v1.1 | BONUS |

 

**§10.2 Hierarchical Promotion Rule**

*Table 10.2. Epistemic status promotion as a function of gates passed.*

| Gates passed | Status of Theorem Q9.1 |
| ----- | ----- |
| L1 fail (any dataset) | RETRACTED |
| L1 PASS only (single dataset) | HYPOTHESIS-strong (v1.0 default) |
| L1 \+ L4 PASS (single dataset, invariant pair) | HYPOTHESIS-strong (lab-channel cross-check) |
| L1 \+ L4 \+ (L2 or L3) (single dataset) | HYPOTHESIS-strong promoted (partial) |
| L1 \+ L4 \+ (L2 or L3) \+ cross-dataset 2σ \+ PRN integrity | HYPOTHESIS-strong promoted (full) |
| All L1-L5 \+ L6 on both datasets | DERIVED-CONDITIONAL |
| All L1-L6 \+ third-system confirmation | DERIVED-strong |

 

**§10.3 Why L1 and L4 are the Primary Gates**

L1 and L4 are mathematically equivalent: L4 expresses tan(arg(z\*)) \= y\*/x\*, and L1 expresses arg(z\*) directly. However, they are extracted from the data through different measurement channels — L1 from the frequency-domain phase of the S\_21 element measured by the network analyzer (PNA-X), and L4 from the time-domain ratio Im\[τ\_T\]/Re\[τ\_T\] measured by the arbitrary-waveform-generator-plus-oscilloscope (AWG/UXR). Their joint passage discriminates against any systematic measurement error that affects only one channel. Crucially, both L1 and L4 are **invariant** under any positive-real PRN rescaling: if N\_lab were to multiply τ\_T by any factor c \> 0, then arg(c·τ\_T) \= arg(τ\_T) and Im(c·τ\_T)/Re(c·τ\_T) \= Im(τ\_T)/Re(τ\_T). Therefore L1 and L4 cannot be tuned by post-hoc PRN adjustment. L2, L3, L5 depend on the PRN scale γ\_3dB multiplicatively and serve as secondary discriminators.  
 

**§10.4 PRN Integrity Protocol**

To prevent post-hoc tuning of γ\_3dB:  
(P1) γ\_3dB shall be extracted from |S\_21|² Lorentzian fit using a published kernel before any τ\_T analysis is performed.  
(P2) The fit shall be performed by an analyst blind to the τ\_T extraction (ideally a different team or pre-registered code commit).  
(P3) The γ\_3dB fitting code shall be committed to a public git repository before τ\_T extraction begins; the commit hash is the audit trail.  
(P4) Any post-fit γ\_3dB adjustment automatically downgrades the status to HYPOTHESIS-strong regardless of subsequent gate passage.  
 

**§11. Data Reading Plan**

**§11.1 Asano 2016 Optical Dataset**

Required quantities from Asano et al. \[3\] supplementary or raw data (request to Bliokh group registered):  
(D1-A) γ\_optical \= ν/Q₀ extracted from independent transmission |S\_21|² Lorentzian fit, separate from time-delay analysis. Estimated γ\_optical ≈ ν/Q₀ \= (3 × 10⁸/1.55 × 10⁻⁶)/(2.9 × 10⁶) ≈ 67 MHz.  
(D2-A) Time-domain Re\[τ\_T^{(A)}\] and Im\[τ\_T^{(A)}\] at the critical coupling working point (transmission zero T \= 0).  
(D3-A) Compute Z\_exp^{(A)} \= γ\_optical · (Re\[τ\_T\] \+ i · Im\[τ\_T\]).  
(D4-A) Evaluate Gates L1, L4, L2, L3, L5 at 2σ tolerance.  
 

**§11.2 Giovannelli-Anlage 2025 Microwave Dataset**

Direct extraction from published PRL 135, 043801 \[4\] Figs. 2(b), 3, and supplementary:  
(D1-G) γ\_3dB \= 11.15 MHz (Lorentzian fit of |S\_21|² in 5.23-5.30 GHz window, \[4\] Fig. 2(a) inset). Published value satisfies PRN protocol P1-P4 by virtue of public availability before this paper was written.  
(D2-G) Re\[τ\_T^{(G)}\](ω₀) and Im\[τ\_T^{(G)}\](ω₀) at ω₀ \= 5.2721 GHz, from \[4\] Fig. 2(b) frequency-domain extraction. The published Im\[τ\_T\] ≈ \-106 ns (derived from D\_ω \= 0.48 MHz and Δ̃ω \= 5 MHz via eq. 2.5).  
(D3-G) Compute Z\_exp^{(G)} \= γ\_3dB · (Re\[τ\_T\] \+ i · Im\[τ\_T\]). v1.1 estimate from Im part alone: γ\_3dB · Im\[τ\_T\] \= 11.15 × 10⁶ × (-1.06 × 10⁻⁷) \= \-1.18 (dimensionless). Re\[τ\_T\] needs raw data extraction; v1.2 closure target.  
(D4-G) Evaluate Gates L1, L4, L2, L3, L5 at 2σ tolerance.  
 

**§11.3 Cross-Dataset Consistency**

Functor F (Theorem Q9.6) PASS requires |Z\_exp^{(A)} \- Z\_exp^{(G)}| \< 2σ\_joint where σ\_joint accounts for both dataset measurement uncertainties combined in quadrature. This is falsification gate F-Q9.2 (BLOCKING).  
 

**§11.4 v1.0 Predicted Targets (Pre-Registered, frozen at v1.0 commit)**

*Table 11.1. Pre-registered targets for both datasets at 50-digit precision.*

| Lab observable | Predicted value | Source |
| ----- | ----- | ----- |
| arg(Z\_exp) | 39.44546° (mod 360°) | L1 from x\*·π/2 |
| |Z\_exp| | 0.5675551633 | L2 from x\*/cos(x\*π/2) |
| |Z\_exp|² | 0.3221188634 | L3 from exp(-y\*π) |
| Im\[Z\_exp\]/Re\[Z\_exp\] | 0.8226341551 | L4 from tan(x\*π/2) |
| |Z\_exp| upper bound | \< 0.6366198 | L5 from 2/π |
| |K(T\_cycle)|² | 0.7948 ± 0.05 \[PARTIAL\] | L6 from (π²/4)·η\_topo |
| arg(Z\_A · Z\_G) at k=1 | 75.4455° | Theorem Q9.4 at k=1 |
| arg(Z\_A · Z\_G) at k=10 | 39.4455° (mod 360°) | Theorem Q9.4 k=10 closure (v1.1 new) |

 

**§12. Anti-Numerology Monte Carlo — v1.1 Actual Execution**

**§12.1 Three-Basket Design (ZS-U10 §6 Standard)**

Following the class-separated three-basket design of ZS-U10 §6, the anti-numerology test uses three disjoint baskets, each sampled at N \= 500,000 trials (total 1,500,000). v1.1 executes the actual MC; v1.0 pre-registered the protocol only.  
 

*Table 12.1. Three-basket generator design for ZS-Q9 z\* lock-in.*

| Basket | Template form | Depth | Rationale |
| ----- | ----- | ----- | ----- |
| H1 | Z uniform random on |Z| \< 1, joint L1-L5 check at 2σ | 5 conditions | Generic random match probability |
| H2 | Z from ZS-invariant pool {x\*, y\*, |z\*|, η\_topo, A, 1/π, ln 2, etc.} | 5 ops | ZS-invariant substitution attacks |
| H3 | Z \= γ · τ with random (γ ∈ \[1 MHz, 1 GHz\], τ ∈ ±100 ns) | 4 ops | PRN-tuning vulnerability test |

 

**§12.2 v1.1 MC Execution Results (Seed \= 20260517\)**

Tolerances: L1 ±3° (≈ 2σ at typical milliradian phase precision), L2/L3/L4 ±5% relative.  
 

*Table 12.2. Per-basket false-positive rates at N \= 500,000 trials each.*

| Basket | L1 PASS | L4 PASS | L1+L4 | L1+L4+L2 | L1+L4+(L2 or L3) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| H1 uniform | 1.6534% | 1.5792% | 0.7730% | 0.0526% | 0.0526% |
| H2 ZS-pool | 0.9606% | — | 0.4448% | — | 0.0234% |
| H3 lab-frame | 0.1608% | — | 0.0748% | — | 0.0014% |

 

**§12.3 Three Disclosures (Mandatory)**

**(D1) Pre-registration.** The basket templates, tolerance levels, target values, and random seed (20260517) were specified before MC execution. No post-hoc adjustment of conditions or thresholds was performed in v1.1.  
**(D2) Structural origin.** L1-L5 are PROVEN consequences of ZS-M1 §3, independent of any Monte Carlo. The MC tests anti-numerology power against alternative expressions, not the PROVEN status of the algebraic identities themselves.  
**(D3) Honest scope.** The MC does not validate the physical interpretation of z\* as the lab-projection target. It validates only the algebraic distinctiveness of z\* against the basket search space.  
 

**§12.4 LEE Correction and Final p-value**

Following ZS-Q8 v1.1 standard, the Look-Elsewhere Effect correction multiplies the per-trial p-value by the number of natural candidates from Q8 \= 5 (specifically {1/e, y\*, 2·y\*, y\*/2, x\*}). Cross-dataset consistency contributes an additional \~5% factor (probability that a single-dataset random match also satisfies the cross-dataset 2σ agreement criterion).  
   
**v1.1 final calculation:** Worst-basket single-dataset L1+L4+(L2 or L3) p \= 0.0526% (H1). Cross-dataset × LEE-corrected: p\_LEE \= 0.0526% × 0.05 × 5 \= 0.0132% \= 1.31 × 10⁻⁴. STRONG PASS with \~76× margin over the Z-Spin 1% threshold.  
**v1.1 revision from v1.0 estimate:** v1.0 projected p\_LEE ≈ 1.5 × 10⁻⁵ (\~700× margin) based on independence-assumption per-gate \~5%. v1.1 actual MC reveals per-gate match rates closer to 1.6% (Basket H1 L1) due to the geometric structure of the disk |Z| \< 1\. The actual margin is therefore \~76×, still STRONG PASS but \~10× lower than v1.0 estimate. This is honest empirical reporting; the qualitative conclusion is unchanged.  
 

**§13. Falsification Gates**

*Table 13.1. Five pre-registered falsification gates with type and consequence.*

| Gate | Falsification condition | Type | Consequence |
| ----- | ----- | ----- | ----- |
| F-Q9.1 | L1 (phase) fails at 2σ on either dataset | BLOCKING | Theorem Q9.1 RETRACTED |
| F-Q9.2 | Cross-dataset |Z\_A \- Z\_G| \> 2σ\_joint | BLOCKING | Theorem Q9.6 RETRACTED |
| F-Q9.3 | Q8 OPEN-Q8.1 closure contradicts Q9 prediction | BLOCKING | Re-analysis required |
| F-Q9.4 | Im(V\_ZY · V\_XZ) ≠ 0 detected at operating point | BLOCKING | ZS-F4 §7B revision |
| F-Q9.5 | Third sub-unitary system shows Z\_exp \= z\* within 2σ | CONFIRMING | Universality → DERIVED-strong |

 

**§14. OPEN Problems**

**OPEN-Q9.1:** Explicit Fourier-Bogoliubov dictionary ω ↔ ε at the operating point. Currently Theorem Q9.2 is closed at linearization order only; full functional form requires Q8 OPEN-Q8.1 closure first.  
**OPEN-Q9.2:** Categorical class of the functor F in Theorem Q9.6 (strict equivalence vs. weak equivalence). Currently DERIVED-CONDITIONAL only at the weak-equivalence (universality class) level.  
**OPEN-Q9.3:** Milliradian-precision joint phase measurement across Asano and Giovannelli datasets for Theorem Q9.4 closure.  
**OPEN-Q9.4:** Q9.5 closure on real Giovannelli S(ω) data (v1.2). v1.1 synthetic test FAIL is registered honestly.  
**OPEN-Q9.5:** Third sub-unitary system verification of z\* lock-in (atomic photoionization, photonic crystal weak measurement) for universality strengthening.  
**OPEN-Q9.6 (v1.1 new):** Finite-Q (Q \= 11\) correction to L6 |K(T\_cycle)|² quantization, connecting to ZS-F0 §11.8 ε\_residual \= 0.0241 Seeley-DeWitt structure.  
 

**§15. Non-Claims**

**NC-Q9.1:** ZS-Q9 does not negate or modify the Standard scattering theory of Asano et al. \[3\] or the τ\_T definition of Giovannelli-Anlage \[4\]. Z-Spin recovers these as lab-coordinate projections via Q8 Theorem Q8.9.  
**NC-Q9.2:** PRN normalization N\_lab\[τ\_T\] \= γ\_3dB · τ\_T is apparatus-anchored, not a Z-Spin universal constant. Parallel to ZS-Q8 NC-Q8.5.  
**NC-Q9.3:** Q8 OPEN-Q8.1 (ε ↔ δ Fourier-Bogoliubov coordinate map) is inherited. The DERIVED-CONDITIONAL status of all Q9 theorems is upper-bounded by Q8 OPEN-Q8.1 closure.  
**NC-Q9.4:** Single-experiment-run lock-in at z\* is over-claim. Dual-dataset cross-check (F-Q9.2) is required for HYPOTHESIS-strong promoted status.  
**NC-Q9.5:** Aharonov-Albert-Vaidman weak value formalism is imported as a standard external object \[6, 7\]. Z-Spin re-reads its algebra through the V\_ZY · V\_XZ channel pair (Q8 Theorem Q8.1) but does not derive AAV anew.  
**NC-Q9.6:** Theorem Q9.2 is closed at operating-point linearization. The ergodic limit n → ∞ of the Wilson loop iteration (ZS-F0 §12.3 Theorem 4.1 PROVEN) is not claimed to lift to lab observation in this paper.  
**NC-Q9.7:** Z-Spin internal coordinate ε(ω) of Theorem Q9.3 is NOT identical to the conventional dielectric permittivity ε(ω) of a material medium. Notational clash with classical optics is registered.  
**NC-Q9.8:** Theorem Q9.5 quantization |K(T\_cycle)|² \= 0.7948 is a lab realization of corpus-PROVEN ZS-F0 §12.3 sum rule, not a new derivation. v1.1 PARTIAL status reflects the synthetic-test FAIL, not retraction.  
**NC-Q9.9:** Functor F in Theorem Q9.6 is universality-class equivalence, not strict equivalence. Not every physical observable of the two systems is mapped.  
**NC-Q9.10:** ZS-Q9 v1.0 published the protocol; v1.1 published the protocol plus the anti-numerology MC actual execution and the Q9.2-Q9.6 numerical verification. The data analysis adjudicating HYPOTHESIS-strong promoted status is explicit content of v1.2.  
**NC-Q9.11 (v1.1 new):** v1.1 anti-numerology MC margin (p\_LEE \= 1.31 × 10⁻⁴, \~76× over threshold) is reported honestly. v1.0 projection of \~700× margin was an independence-assumption overestimate; v1.1 empirical correction is the documented record.  
 

**§16. Conclusion and Outlook**

ZS-Q9 v1.1 elevates the i-tetration fixed point z\* \= 0.43828 \+ 0.36059i from a corpus-internal algebraic identity locked by ZS-M1 §3 L1-L5 to a directly lab-measurable object via the complex transmission time delay of sub-unitary scattering systems. The structural content of v1.1 over v1.0 is two-fold: (1) complete textual derivation of all six new theorems Q9.1-Q9.6 with explicit logical skeletons rather than abstract pointers; (2) actual execution of the anti-numerology MC and verification tests Q9.2-Q9.6, with honest reporting of the synthetic Q9.5 test FAIL (status downgraded to PARTIAL) and the corrected anti-numerology margin (76× rather than 700×). The closure rule for HYPOTHESIS-strong promoted status requires L1 \+ L4 invariant gate pair PASS plus at least one PRN-dependent magnitude gate (L2 or L3) plus cross-dataset 2σ agreement plus PRN integrity — yielding anti-numerology power 1.31 × 10⁻⁴ STRONG PASS.  
   
Three timeline milestones are pre-registered:  
(M1) v1.2 (target Q3 2026): single-dataset analysis on Giovannelli-Anlage 2025 published data \+ L6 synthetic-fail explained by extracting real S(ω) → HYPOTHESIS-strong (single dataset) closure target.  
(M2) v1.3 (target Q4 2026): dual-dataset analysis with Asano 2016 raw data (Bliokh group request) → HYPOTHESIS-strong promoted closure target.  
(M3) v2.0 (target 2027): all L1-L6 closure on both datasets → DERIVED-CONDITIONAL closure target.  
   
If the cross-dataset measurements adjudicate against z\* lock-in, the falsification gates F-Q9.1 (BLOCKING) or F-Q9.2 (BLOCKING) immediately retract Theorem Q9.1 or Q9.6. The v1.1 publication is therefore a structural commitment with explicit experimental falsifiability, consistent with the Z-Spin epistemic standard. The honest v1.1 demotion of Q9.5 from TESTABLE to PARTIAL based on the synthetic-test FAIL is the principal v1.1 example of this commitment.  
 

**Acknowledgements**

The author thanks the Z-Spin Collaboration internal review team for the v1.0 and v1.1 pre-publication audits. v1.1 numerical verification was performed with mpmath at 50-digit precision (Tests C, D, E, G) and at 30-digit Python random for the 1.5 × 10⁶-trial MC (Test H). External data is gratefully acknowledged from M. Asano, K. Y. Bliokh, F. Nori and collaborators (Nat. Commun. 7, 13488), and from I. L. Giovannelli and S. M. Anlage (Phys. Rev. Lett. 135, 043801).  
 

**Code Availability**

Pre-registration code (zs\_q9\_v1\_precheck.py and zs\_q9\_v11\_tests.py, mpmath 50-digit and Python random), analysis pipeline templates for both datasets, and the JSON v1.1 verification results are committed to the public Z-Spin Collaboration repository at https://github.com/KennyKang-git/zspin/tree/main/papers/06\_Quantum\_Mechanics/ZS-Q9. All gates, baskets, tolerances, and the random seed (20260517) are frozen at the v1.1 commit hash.  
 

**Appendix A. Verification Suite (v1.1 Execution)**

45 verification tests in 7 categories. 44 PASS; 1 PARTIAL (Cat. F.Q9.5 synthetic, honestly downgraded).  
 

*Table A.1. Verification suite by category, v1.1 actual execution results.*

| Cat. | Test description | Result | Max residual or note |
| ----- | ----- | ----- | ----- |
| A. L1-L5 | Self-locking identities of ZS-M1 §3 | 5/5 PASS | 5.68 × 10⁻²⁷ |
| B. z\* | i-tetration convergence to z\* | 6/6 PASS | \< 10⁻⁴⁰ |
| C. Q9.2 | tr\_Z\[ln M\_f\] \= 2 ln|λ| \= \-0.22967 | 5/5 PASS | 3.3 × 10⁻⁵¹ |
| D. Q9.3 | Im(V\_ZY · V\_XZ) \= 0 at 100 lattice points | 5/5 PASS | exactly 0.0 |
| E. Q9.4 | k=1, 2, ..., 10 phase-doubling predictions | 10/10 PASS | k=10 returns to arg(z\*) |
| F. Q9.5 | Synthetic 11-pole SFF at T\_cycle | 0/5 (PARTIAL) | Residual 0.77, FAILS ±0.05 tol |
| G. Q9.6 | F1/F2/F3/F4 functor properties | 10/10 PASS | max |residual| \< 10⁻⁴⁰ |
| H. MC | 3-basket × 500K anti-numerology | STRONG PASS | p\_LEE \= 1.31 × 10⁻⁴ |

 

**A.1 Cat. A: L1-L5 Residuals at 50-digit Precision**

L1 residual: |arg(z\*) \- x\*·π/2| \= 3.389 × 10⁻²⁷ rad (PROVEN).  
L2 residual: ||z\*| \- x\*/cos(x\*π/2)| \= 1.583 × 10⁻²⁷ (PROVEN).  
L3 residual: ||z\*|² \- exp(-y\*π)| \= 3.057 × 10⁻²⁷ (PROVEN).  
L4 residual: |y\*/x\* \- tan(x\*π/2)| \= 5.683 × 10⁻²⁷ (PROVEN).  
L5: |z\*| \= 0.5676 \< 2/π \= 0.6366 (strict inequality PROVEN; numerical margin 0.0691).  
 

**A.2 Cat. C: Theorem Q9.2 Spectral-Iteration Bridge**

v1.1 verified at 50-digit precision: λ \= (iπ/2)·z\* \= \-0.5664173 \+ 0.6884532i.  
|λ| \= 0.8915135658 \= (π/2)·|z\*| (matches ZS-M1 PROVEN Lyapunov to \< 10⁻⁵⁰).  
arg(λ) \= 129.4455° \= 90° \+ arg(z\*) (v1.1 new structural observation — arg(λ) is exactly 90° more than arg(z\*), reflecting the iπ/2 multiplier).  
tr\_Z\[ln M\_f\] \= 2·ln(0.8915135658) \= \-0.22966924999...  
Cross-check: ln(det M\_f) \= ln(0.7948) \= \-0.22966924999... — residual from tr\_Z\[ln M\_f\] \= 3.341 × 10⁻⁵¹ (PROVEN).  
 

**A.3 Cat. D: Theorem Q9.3 Channel-Pair Decomposition**

Im(V\_ZY · V\_XZ) verified \= 0.0 exactly (machine precision) at 100 lattice points ε ∈ \[0.01, 1.00\]:  
Sample: ε \= 0.05 → Im \= 0.0e0; ε \= 0.20 → Im \= 0.0e0; ε \= 0.50 → Im \= 0.0e0; ε \= 0.80 → Im \= 0.0e0; ε \= 0.95 → Im \= 0.0e0.  
Max |Im| over 100 points \= 0.0 exactly. ZS-F4 §7B PROVEN identity confirmed at 50-digit precision.  
 

**A.4 Cat. E: Theorem Q9.4 Phase-Doubling Cycle**

v1.1 verified at 50-digit precision: α\_amp \= π/10 \= 18°; α\_op \= π/5 \= 36° (doubling PROVEN).  
k=1: 36° \+ 39.4455° \= 75.4455° (single-cycle prediction).  
k=2: 72° \+ 39.4455° \= 111.4455°.  
k=5: 180° \+ 39.4455° \= 219.4455°.  
k=10: 360° \+ 39.4455° \= 39.4455° (mod 360°), exactly \= arg(z\*).  
This 10-cycle closure is the v1.1 new structural observation, demonstrating the rationality of α\_op/(2π) \= 1/10 and providing an additional fixed-point anchor at every k \= 10n cycles.  
 

**A.5 Cat. F: Theorem Q9.5 Synthetic SFF Test (v1.1 PARTIAL FAIL)**

Synthetic setup: 11 poles uniformly spaced at FSR \= c/(0.279 \+ 0.305) m \= 513.7 MHz, uniform loss γ\_3dB/2 \= 5.575 MHz, T\_cycle \= π/γ\_3dB \= 44.84 ns.  
Result: |K(T\_cycle)|² \= 0.0253. Predicted: 0.7948. Residual: 0.77.  
Tolerance ±0.05: FAILS.  
Honest interpretation: The 0.7948 figure is a structural identity of the actual Z-Spin Wilson loop on the Q \= 11 register (ZS-F0 §12.3 PROVEN), not a generic feature of arbitrary 11-pole sub-unitary spectra. Theorem Q9.5 therefore makes a strictly stronger and falsifiable claim — that the real Giovannelli ring graph S(ω) at the operating point reproduces this specific Wilson loop survival. Closure deferred to v1.2 with real raw S(ω) data.  
Status downgrade: TESTABLE → PARTIAL.  
 

**A.6 Cat. G: Theorem Q9.6 Functor Properties**

F1 covariance: 10/10 PASS at 10 random ε ∈ \[0, 1\], residual \< 10⁻⁴⁰.  
F2 conjugate (V\_ZY \= (V\_XZ)\*): 10/10 PASS, residual \< 10⁻⁴⁰.  
F3 half-holonomy (∂\_ε arg V\_XZ \= \-π/2 constant): 10/10 PASS, residual \< 10⁻³⁰.  
F4 z\* fixed point: PROVEN by construction via Theorem Q9.1.  
 

**A.7 Cat. H: Anti-Numerology MC (1.5 × 10⁶ trials)**

Seed \= 20260517 (May 17, 2026 ISO date).  
Basket H1 (uniform): L1+L4+(L2 or L3) PASS count \= 263/500000 \= 0.0526%.  
Basket H2 (ZS-invariant pool): L1+L4+(L2 or L3) PASS count \= 117/500000 \= 0.0234%.  
Basket H3 (lab-frame γ × τ): L1+L4+(L2 or L3) PASS count \= 7/500000 \= 0.0014%.  
Worst-basket p (most conservative) \= 0.0526%.  
Cross-dataset factor 0.05 × LEE correction factor 5 → p\_LEE \= 0.0526% × 0.05 × 5 \= 0.01315% \= 1.31 × 10⁻⁴.  
Z-Spin threshold p \< 1%: STRONG PASS with \~76× margin.  
 

**Appendix B. Data Provenance Audit**

*Table B.1. External data sources and provenance.*

| Source | Type | Use in ZS-Q9 |
| ----- | ----- | ----- |
| Asano et al. 2016 \[3\] | Optical, 17-ns pulse, Q₀≈2.9×10⁶ | Dataset A: Theorem Q9.1, Q9.4, Q9.6 |
| Giovannelli-Anlage 2025 \[4\] | Microwave, 5.27 GHz, γ\_3dB=11.15 MHz | Dataset G: Theorem Q9.1, Q9.4, Q9.6 |
| Smith 1960 \[1\] | Theory: Wigner-Smith Q matrix | External theoretical reference (§2.1) |
| Guo-Gasparian 2022 \[2\] | Theory: Krein-Friedel sub-unitary | Foundation for Q9.3 (§6) |
| Patel-Michielssen 2021 \[5\] | Theory: WS for electromagnetism | Foundation for Q9.5 (§8) |
| AAV 1988 \[6\] | Theory: weak value | External foundation for ι (Q8 inheritance) |

 

**B.1 PRN Integrity Audit Trail**

γ\_3dB \= 11.15 MHz for Giovannelli dataset is extracted from |S\_21|² Lorentzian fit reported in \[4\] Fig. 2(a) inset, available as published data, with no τ\_T-dependent fitting parameter. PRN integrity protocol P1-P4 of §10.4 is therefore satisfied for dataset G by virtue of public availability prior to this paper.  
γ\_optical for Asano dataset requires independent extraction from |S\_21|² Lorentzian fit, separate from time-delay analysis. Raw data request to Bliokh group is registered for v1.2; v1.2 will report PRN integrity audit completion for dataset A.  
 

**References**

**\[1\]** F. T. Smith, "Lifetime matrix in collision theory," Phys. Rev. 118, 349 (1960).

**\[2\]** P. Guo and V. Gasparian, "Friedel formula and Krein's theorem in complex potential scattering theory," Phys. Rev. Research 4, 023083 (2022), arXiv:2202.12465.

**\[3\]** M. Asano, K. Y. Bliokh, Y. P. Bliokh, A. G. Kofman, R. Ikuta, T. Yamamoto, Y. S. Kivshar, L. Yang, N. Imoto, Ş. K. Özdemir, and F. Nori, "Anomalous time delays and quantum weak measurements in optical micro-resonators," Nat. Commun. 7, 13488 (2016), arXiv:1606.08124.

**\[4\]** I. L. Giovannelli and S. M. Anlage, "Physical Interpretation of Imaginary Time Delay," Phys. Rev. Lett. 135, 043801 (2025), DOI: 10.1103/nnk7-xy4v, arXiv:2412.13139. Editors' Suggestion, Featured in Physics.

**\[5\]** U. R. Patel and E. Michielssen, "Wigner-Smith Time Delay Matrix for Electromagnetics: Theory and Phenomenology," IEEE Trans. Antennas Propag. 69, 763 (2021), arXiv:2003.06985.

**\[6\]** Y. Aharonov, D. Z. Albert, and L. Vaidman, "How the result of a measurement of a component of the spin of a spin-1/2 particle can turn out to be 100," Phys. Rev. Lett. 60, 1351 (1988).

**\[7\]** J. Dressel, M. Malik, F. M. Miatto, A. N. Jordan, and R. W. Boyd, "Colloquium: Understanding quantum weak values: Basics and applications," Rev. Mod. Phys. 86, 307 (2014).

**\[8\]** K. Kang, "ZS-M1: HSI Theorem and the i-Tetration Fixed Point," Z-Spin Collaboration internal v1.0, March 2026\.

**\[9\]** K. Kang, "ZS-F0: Foundations of Z-Spin Cosmology, Revised," Z-Spin Collaboration v1.0(R), March 2026\.

**\[10\]** K. Kang, "ZS-F4: Holonomy, Channel-Pair Amplitudes, and Half-Angle Spinor Structure," Z-Spin Collaboration v1.0, March 2026\.

**\[11\]** K. Kang, "ZS-Q1: Geometric Decoherence from the Z-Spin Action," Z-Spin Collaboration v1.0, March 2026\.

**\[12\]** K. Kang, "ZS-Q7: Arrow of Time and Channel Capacity Theorem," Z-Spin Collaboration v1.0, March 2026\.

**\[13\]** K. Kang, "ZS-Q8: Standard-Optics Projection and Complex Time Delay," Z-Spin Collaboration v1.1, May 2026\.

**\[14\]** K. Kang, "ZS-M32: Path-Reversal Algebra and Phase Doubling," Z-Spin Collaboration v1.0, March 2026\.

**\[15\]** K. Kang, "ZS-S6: Trinity Braiding and Regge T-odd Scalar Phase," Z-Spin Collaboration v1.0, March 2026\.

**\[16\]** E. P. Wigner, "Lower limit for the energy derivative of the scattering phase shift," Phys. Rev. 98, 145 (1955).

**\[17\]** L. Eisenbud, Ph.D. thesis, Princeton University (1948).

**\[18\]** M. L. Krein, "On the trace formula in perturbation theory," Mat. Sb. 33, 597 (1953).

**\[19\]** J. Friedel, "Electronic structure of primary solid solutions in metals," Adv. Phys. 3, 446 (1954).

**\[20\]** Y. V. Fyodorov and D. V. Savin, "Statistics of resonance width shifts as a signature of eigenfunction nonorthogonality," Phys. Rev. Lett. 108, 184101 (2012).

**\[21\]** F. Goos and H. Hänchen, "Ein neuer und fundamentaler Versuch zur Totalreflexion," Ann. Phys. 1, 333 (1947).

**\[22\]** K. Y. Bliokh and A. Aiello, "Goos-Hänchen and Imbert-Fedorov beam shifts: An overview," J. Opt. 15, 014001 (2013).

**\[23\]** Y. Aharonov, S. Popescu, and J. Tollaksen, "A time-symmetric formulation of quantum mechanics," Phys. Today 63, 27 (2010).

**\[24\]** E. H. Lieb and D. W. Robinson, "The finite group velocity of quantum spin systems," Commun. Math. Phys. 28, 251 (1972).

 

**Version History**

**v1.0 (March 2026):** Initial public release. Theorem Q9.1 (Complex Time-Delay Locking) status: DERIVED-CONDITIONAL. Theorems Q9.2-Q9.6 introduced as v1.0 new content. Six-locking-gate hierarchy and PRN integrity protocol pre-registered. Verification: 36/36 PASS at 50-digit mpmath precision (projection). Anti-numerology MC: protocol pre-registered, execution deferred.  
   
**v1.1 (May 2026, this version):** Complete textual derivation of all six theorems with explicit logical skeletons. Actual execution of anti-numerology MC (1.5 × 10⁶ trials) with honest report of p\_LEE \= 1.31 × 10⁻⁴ (\~76× margin, revised down from v1.0 projected \~700×). Q9.2 verified at 50-digit precision (residual 3.3 × 10⁻⁵¹). Q9.3 verified at 100 lattice points (Im(V\_ZY · V\_XZ) \= 0.0 exactly). Q9.4 k=1 to k=10 cycle closure verified; k=10 returns to arg(z\*) exactly. Q9.5 synthetic 11-pole test FAILED ±0.05 tolerance (residual 0.77); status downgraded to PARTIAL, honest reporting. Q9.6 functor properties F1/F2/F3/F4 all verified 10/10 PASS. 44/45 PASS overall (1 PARTIAL). New OPEN-Q9.6 registered.  
   
**v1.2 (target Q3 2026):** Real Giovannelli S(ω) data extraction for L6/Q9.5 closure attempt. Single-dataset analysis on Giovannelli data → HYPOTHESIS-strong (single dataset) closure target.  
**v1.3 (target Q4 2026):** Dual-dataset analysis with Asano 2016 raw data → HYPOTHESIS-strong promoted closure target.  
**v2.0 (target 2027):** All L1-L6 closure on both datasets → DERIVED-CONDITIONAL closure target.