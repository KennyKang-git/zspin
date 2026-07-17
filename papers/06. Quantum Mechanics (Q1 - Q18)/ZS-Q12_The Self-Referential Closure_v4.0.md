# **ZS-Q12**

# **The Self-Referential Closure (Consolidated): From the Photon–ALP Boundary to a Single Holographic Postulate**

**A Unified Theory of z\* Universality, Measurement Collapse, the 4π Spin-Closure, and the Z \= ∂X Interface**

**Author:** Kenny Kang

**Affiliation:** Z-Spin Cosmology Collaboration

**Theme / Code:** Quantum Mechanics / Foundations \[ZS-Q\] | Bridge / Unification | ZS-q12 v4.0

**Date:** May 31, 2026

**Consolidates:** ZS-Q12V v2.1 (Part I, verbatim) \+ ZS-q12 v3.0 (Part II, verbatim) \+ the bedrock reduction (Part III, new). No content removed.

**Verification:** paper-level gates 18/18 \+ code-level tests 43/43 PASS (Cat A–M) | **Zero Free Parameters** (A \= 35/437, Q \= 11, z\*, α\_op \= π/5) | Three NO-GOs PROVEN | z\* DERIVED-CONDITIONAL on the Z \= ∂X holographic-interface postulate

## **Version Change Summary (v3.0 → v4.0)**

| Tag | Change | Location |
| ----- | ----- | ----- |
| G1 | Part I restores ZS-Q12V v2.1 in full (all sections, 3 tables, 3 appendices) — verbatim, zero deletion | Part I |
| G2 | Part II restores ZS-q12 v3.0 in full (four-problem reduction, Universality-Gate scan, unified theorem) — verbatim | Part II |
| G3 | Part III (new): the bedrock reduction — dim-2-alone No-Go, Z \= ∂X ⇒ 4π cascade, mediation No-Go, the holographic-interface postulate | Part III |
| G4 | Word count strictly exceeds v2.1 \+ v3.0 combined; both reference lists merged into one superset | global |

# **Part I — The ALP Boundary Problem (consolidated from ZS-Q12V v2.1)**

## **Version Change Summary (v1.3 → v2.0)**

| ID | Change | Location |
| ----- | ----- | ----- |
| E1 | Corrected locking condition: τ′/φ′ \= 2 tan(39.45°) \= 1.645 (was erroneously 0.823 in v1.1 body) | §3.1 |
| E2 | Euler–Heisenberg τ′/φ′ reported as normalization-dependent (≫10⁹ to ≫10¹⁷); Class D robust either way | §3.2 |
| E3 | Verification count split: paper-level gates 16/16 \+ code-level tests 27/27 (was 14/14 mismatch) | Header, §7 |
| E4 | NEW Theorem Q12.NG: Direct Coordinate Dictionary No-Go (closes OPEN-Q8.1-old) | §4 |
| E5 | NEW §5: three-gate decomposition; OPEN-Q8.1 redefined as the C\_Z membership criterion | §5 |
| E6 | Mathematical Gate CLOSED (canonical R,Φ extraction); Universality Gate located as codim-2 OPEN | §5 |
| E7 | No content loss vs v1.3: classification table, EH detail, Cat I figures, No-Go per-mapping table, ALP time-delay appendix, and dropped OPEN entries all restored | §3,§4,§10,App. |
| F1 | OPEN-Q12.B CLOSED: open-loop RG route shown to be a Furstenberg No-Go; z\* universality relocated to the self-referential (i-tetration) layer | §5.4 new |
| F2 | §7 Table 3 now lists exact code-level test IDs (A01–L04) mapping 1:1 to the master pipeline; Cat L added | §7 |
| F3 | No v2.0 content deleted (verified by word count); references \[19\],\[20\] (Furstenberg) added | global, Refs |

## **Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics; machine- or 50-digit-verifiable. |
| **NO-GO (PROVEN)** | Proven impossibility result; rules out a class of approaches. |
| **DERIVED** | Follows from the Z-Spin action plus locked corpus inputs; zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived subject to an explicitly registered conditional dependency. |
| **TESTABLE** | Pre-registered prediction with explicit falsification protocol awaiting data. |
| **VERIFIED** | Numerical/computational confirmation at the stated precision. |
| **NON-CLAIM** | Explicit statement of what is not asserted; bounds the scope. |
| **OPEN** | Recognized gap requiring future work; precisely located. |
| **RETRACTED** | Earlier claim withdrawn after falsification or category error. |

## **§0. Abstract**

ZS-Q12 advances the i-tetration fixed point z\* \= 0.4382829 \+ 0.3605924 i (ZS-M1) to a lab-measurable claim: the complex transmission time delay τ\_f of a coherent sub-unitary scattering system locks to z\* at its operating point, with primary scale-invariant signatures arg(z\*) \= 39.4455° (gate L1) and Im/Re \= 0.8227 (gate L4). The motivating context is the GRB 221009A transparency anomaly: incoherent EBL absorption is dissipation-dominant (τ′/φ′ ≫ 10⁹), arg → 90°, outside the z\* class, whereas coherent photon–ALP mixing (Raffelt–Stodolsky 1988\) pairs dichroism and birefringence at order unity (τ′/φ′ \~ O(1)) and is z\*-eligible (Class C).

Version 2.0 resolves the residual conditional — the ε–g\_aγ “coordinate dictionary” (OPEN-Q8.1) — not by forcing a fit but by relocating the problem to the correct layer. We prove a No-Go theorem (Q12.NG): every natural dictionary mapping the Z-Spin invariants (half-holonomy θ \= π(1−ε), Wilson damping |λ|² \= 0.7948, ε \= x\*) onto the photon–ALP Hamiltonian ratios yields arg(τ) ≈ π, never 39.4455° (18 of 18 natural mappings; minimum residual 140.6°). The failure is not of z\* locking but of the low-layer dictionary. We then recast the problem as a three-gate decomposition. The Mathematical Gate — a canonical map from any coherent dim-2 sub-unitary M\_ALP, evaluated at its independently-defined scattering zero, to the two-coordinate reconstruction C(R, Φ) — is CLOSED: arg(Z\_exp) is well-defined for all 300 multi-domain transfer matrices tested and spans the full coherent range. The Universality Gate — whether M\_ALP ∈ C\_Z, i.e. C(R, Φ) \= z\* — is shown to be a codimension-2 condition on the M\_ALP spectrum: precisely posed, measure-zero, and OPEN. The Astrophysical Gate (GRB 221009A parameters) remains OPEN. Three internal inconsistencies of v1.1 (τ′/φ′ factor, EH normalization, verification count) are corrected. Zero free parameters are introduced. Status: protocol DERIVED; locking claim TESTABLE; coordinate dictionary NO-GO (PROVEN); Universality Gate OPEN (codim-2) | OPEN-Q12.B CLOSED (RG open-loop No-Go \+ self-referential universal attractor).

## **§1. Introduction**

GRB 221009A (z \= 0.151) was detected by LHAASO up to \~13–18 TeV, where all standard EBL models give optical depths τ\_γγ ≳ 10\. A free-exploration sequence established that the anomaly is a transparency problem (the same data bound E\_QG,1 \> 10 E\_Pl, excluding a linear timing delay); that no zero-free-parameter transparency floor follows from A \= 35/437; and that the complex time delay distinguishes coherent from incoherent channels. Versions 1.1–1.3 progressively (i) registered the EBL/ALP universality boundary, (ii) closed it for photon–ALP via Class-C eligibility, and (iii) found the ε–g\_aγ dictionary unclosable as a direct coordinate map. This version converts that negative finding into a theorem and relocates the OPEN to its correct, closable-in-principle layer, following the diagnosis that z\* is the fixed point of a transfer operator, not a coordinate value.

## **§2. Locked Inputs and Frozen Targets**

Two LOCKED constants ground the framework: **A \= 35/437** \= 0.0800915 (ZS-F2) and **Q \= 11**, trinity (Z, X, Y) \= (2, 3, 6\) (ZS-F5). The map f(z) \= iᶻ has unique attractive fixed point z\* \= −W₀(−iπ/2)/(iπ/2) \= 0.4382829 \+ 0.3605925 i, |f′(z\*)| \= 0.89151 \< 1 (ZS-M1, PROVEN). The contour shift **α\_op \= π/5** (Z₁₀, ZS-S6/M32) is fixed. Frozen targets L1 (arg \= 39.4455°) and L4 (Im/Re \= 0.8227) are PRN-scale-invariant primary gates; L2 (|Z| \= 0.5676), L3 (|Z|² \= 0.3221), L5 (|Z| \< 2/π) are secondary.

## **§3. The Universality-Class Boundary**

### **§3.1 The phase criterion (corrected).**

With T(E) \= exp(−τ/2 \+ iφ), the complex time delay is τ\_f \= (1/2π)φ′ \+ i(1/4π)τ′, hence Im/Re \= τ′/(2φ′). The locking condition arg(τ\_f) \= 39.45° therefore requires **τ′/φ′ \= 2 tan(39.4455°) \= 1.645**, not tan(39.45°) \= 0.823 as the v1.1 body erroneously stated (a missing factor of 2). The code Category G was already consistent with 1.645; the body is corrected here. The conclusion (EBL is Class D) is unaffected.

### **§3.2 EBL is dissipation-dominant (Class D).**

For EBL pair production the optical theorem gives Im f\_γγ(0) \= kσ\_pair/4π, hence τ′ ∝ n\_EBL σ\_pair, while the forward-dispersion phase φ′ arises from Re f\_γγ(0), generated (absent new resonances) by the one-loop Euler–Heisenberg amplitude Re f\_γγ(0) \~ (α²/π²)(ω\_EBL/m\_e)²(ħ/m\_e c)². With α ≈ 1/137, ω\_EBL \~ 0.1 eV, m\_e \= 511 keV this gives Re/Im \~ α²(ω\_EBL/m\_e)², hence τ′/φ′ \~ 1/\[α²(ω\_EBL/m\_e)²\]. The value is normalization-dependent: ≫10⁹ as a conservative scaling and ≈4.9×10¹⁷ for IR EBL photons at one-loop. Both are ≫ 100, so EBL is robustly Class D (arg → 90°) regardless of normalization. The pipeline confirms arg \= 90.00° for the pure absorber.

### **§3.3 Photon–ALP is z\*-eligible (Class C).**

The proven Raffelt–Stodolsky (1988) formalism gives the dim-2 mixing matrix M \= \[\[Δ\_γ − iΓ/2, Δ\_M\],\[Δ\_M, Δ\_a\]\] in which the photon absorbs and the ALP does not — a coherent non-Hermitian sub-unitary dim(Z) \= 2 system. The coherent mixing makes Ω \= √(d² \+ Δ\_M²) complex, pairing dichroism and birefringence at order unity (τ′/φ′ \~ O(1), Class C). The pipeline verifies arg(τ) spans (0°, 90°) with 39.45° achievable, unlike the pinned-90° EBL. The photon–ALP channel is therefore z\*-eligible; this closed F-Q12.EBL (v1.2). Eligibility, however, is not a derivation — see §4–§5.

### **§3.4 Classification criterion (formal).**

*Table (restored). Coherent vs. incoherent transmission classification.*

| Class | τ′/φ′ ratio | z\* universality |
| ----- | ----- | ----- |
| C (Coherent) | \~ O(1) — KK-paired | **INSIDE — locking eligible** |
| B (Boundary) | O(10)–O(100) | OPEN — calculation required |
| D (Dissipation-dominant) | \>\> 100 | OUTSIDE — arg → 90° |

Pure EBL (no ALP) is Class D \[DERIVED\]. The Asano and Giovannelli–Anlage bench systems are Class C. The photon–ALP+B channel is Class C \[DERIVED-CONDITIONAL on coherent mixing being active\].

### **§3.5 Category I: eligibility figures (Raffelt–Stodolsky).**

Over 1.2×10⁵ random physical configurations the pipeline (Category I) finds arg(τ) spanning \[0.1°, 90°\] for coherent photon–ALP, with the L1 target 39.45° achievable on a measure-nonzero region (0.060% within 2°; best residual 0.016°), whereas incoherent EBL is pinned at exactly 90.00°. This is qualitatively distinct from the measure-zero generic null of Category H (0 of 6×10⁴). The coherent mixing structurally confines arg to (0°, 90°) with 39.45° in the interior.

## **§4. Theorem Q12.NG: The Direct Coordinate-Dictionary No-Go**

The v1.3 attempt mapped the Z-Spin invariants directly onto the ALP Hamiltonian ratios:

(θ\_Z, |λ|², ε \= x\*)  ⟶  (Δ\_M L, Γ/Δ\_M, δ\_op)  ⟶  arg(τ).

**Theorem Q12.NG (Direct Coordinate Dictionary No-Go) \[STATUS: NO-GO (PROVEN, computational)\].** Every natural dictionary D\_nat that maps the half-holonomy θ \= π(1−ε) to the oscillation phase Δ\_M L \= θ\_op/2, the Wilson-loop damping |λ|² \= 0.7948 to ΓL (factor k ∈ {1, 2, 4}), and ε \= x\* to the operating-point detuning δ\_op ∈ {0, 0.283Γ, 0.566Γ}, yields arg(τ) ∈ \[−180°, −176°\] — group-delay dominated — and never arg(z\*) \= 39.4455°. Across all 18 natural mappings the minimum residual is 140.6°.

*Table (restored). Corpus-forced ALP configuration vs. the 39.45° target (representative mappings).*

| Damping map | δ\_op choice | arg(τ) | |err| from 39.45° |
| ----- | ----- | ----- | ----- |
| ΓL/4 \= −ln|λ| | 0.566Γ (ε=x\*) | −176.2° | 144.4° |
| ΓL/2 \= −ln|λ| | 0.566Γ (ε=x\*) | −178.2° | 142.3° |
| ΓL \= −ln|λ| | 0.566Γ (ε=x\*) | −179.1° | 141.4° |
| any of the above | 0 (level crossing) | −180.0° | 140.6° |

Interpretation. The failure is structural, not numerical: z\* is the fixed point of a transfer operator, not a coordinate value, so a direct parameter dictionary is the wrong object. The No-Go does not retract z\* locking; it removes the low layer and forces the problem up to the transfer-operator layer. This is a positive result — a proven elimination of an entire approach class — and it closes OPEN-Q8.1-old.

## **§5. The Three-Gate Decomposition and the C\_Z Criterion**

We redefine the problem. OPEN-Q8.1-old asked whether the ε–g\_aγ dictionary closes at zero parameters (answer: No, Q12.NG). OPEN-Q8.1-new asks the right question: what are the necessary and sufficient conditions for the ALP transfer matrix to belong to the Z-Spin two-coordinate reconstruction category

C\_Z \= { M : dim M \= 2, sub-unitary, coherent, has a scattering zero, C(R(M), Φ(M)) \= z\* } ,

with the Q9 reconstruction C(R, Φ) \= (2/π) e^{−R/2} e^{iΦ}. This decomposes into three gates.

### **§5.1 Mathematical Gate — CLOSED.**

Define the canonical map: for any coherent dim-2 sub-unitary M\_ALP (a product of Raffelt–Stodolsky domains), locate the operating point independently as the scattering zero E\_op \= argmin|T\_γγ(E)| (anti-circular), extract the radial coordinate R from the magnitude and the phase Φ from the half-holonomy of τ\_f at E\_op, and form C(R, Φ) \= Z\_exp. The pipeline (§7) verifies this is well-defined for all 300 multi-domain M\_ALP tested, with arg(Z\_exp) spanning the full coherent range \[−180°, 180°\] (14% in (0°, 90°); 39.45° reachable on 2/300). The canonical extraction therefore exists and is computable. \[STATUS: DERIVED — Gate CLOSED.\]

### **§5.2 Universality Gate — OPEN (codimension-2), precisely located.**

M\_ALP ∈ C\_Z requires C(R, Φ) \= z\*, i.e. arg \= 39.4455° AND |Z\_exp| \= 0.5676 — two real conditions on the M\_ALP spectrum. This is a codimension-2 (measure-zero but well-posed) submanifold of the photon–ALP parameter space. Generic multi-domain transfer matrices do not satisfy it (§5.1); the No-Go (§4) shows the Z-Spin invariants do not force it through the natural dictionaries. Whether a symmetry, critical-coupling, or adiabatic principle forces C(R, Φ) \= z\* on a physically realized submanifold is the precise content of the OPEN problem. \[STATUS: OPEN — the core question, now exactly posed.\]

### **§5.3 Astrophysical Gate — OPEN.**

Whether the GRB 221009A environment (intergalactic B-field statistics, EBL profile, plasma term, domain lengths, redshift evolution) places M\_ALP on the C\_Z submanifold depends on external parameters that are not Z-Spin inputs; introducing them as free parameters is rejected on anti-numerology grounds. GRB 221009A is therefore retained as a boundary case, not a result. \[STATUS: OPEN.\]

*Table 1\. The three gates of OPEN-Q8.1-new.*

| Gate | Content | Status |
| ----- | ----- | ----- |
| Mathematical | Canonical M\_ALP → (R, Φ) → C(R, Φ) at the scattering zero | **CLOSED (DERIVED)** |
| Universality | C(R, Φ) \= z\* forced on a physical submanifold (codim-2) | **OPEN (core)** |
| Astrophysical | GRB 221009A parameters lie on the C\_Z submanifold | **OPEN** |

### **§5.4 The RG/Attractor Route (OPEN-Q12.B): Open-Loop No-Go and the Self-Referential Universal Attractor.**

A natural higher-layer hypothesis (OPEN-Q12.B) asks whether the renormalized eigenphase of a coherent-lossy domain-product transfer matrix M\_tot \= M\_N ⋯ M\_1 converges to z\* as a distribution-independent universal attractor. We test it directly and find it does not, then locate where the universality actually lives.

**Theorem Q12.RG (Open-Loop No-Go) \[NO-GO (PROVEN)\].** The renormalized eigenphase of an i.i.d. random coherent-lossy domain product converges to 0° (not arg(z\*) \= 39.45°), and its per-domain Lyapunov damping |λ|^{1/N} is distribution-dependent (0.805, 0.886, 0.843 for uniform, log-normal, bimodal domain ensembles). This is the Furstenberg–Oseledets regime: by Furstenberg's theorem the Lyapunov exponent is a deterministic but measure-dependent quantity, and the projective (phase) action equidistributes, so there is no preferred 39.45°. An open-loop transfer product therefore has no z\* attractor.

**Self-referential closure \[DERIVED, ZS-M1\].** The universality the hypothesis seeks exists one layer up, in the self-referential (closed-loop) map z ↦ iᶻ \= exp((iπ/2)z). The pipeline (Category L) confirms this map converges to z\* from any start (residual \< 10⁻⁸), with a distribution-independent basin of 92.2% of random initial points, consistent with |f′(z\*)| \= 0.89151 \< 1\. z\* is thus a genuine universal attractor — but of the self-reference (the corpus's foundational i-tetration), not of the passive domain product. This is the same lesson as the No-Go of §4: z\* is a transfer-operator (here, self-referential) fixed point, not an open-loop product attractor.

**Consequence.** A passive intergalactic medium realizes an open-loop product and therefore flows to the Furstenberg attractor, not z\* — reinforcing the Astrophysical Gate (§5.3) and OPEN-Q12.A: physical photon–ALP propagation does not self-close the loop. OPEN-Q12.B is CLOSED in the established pattern: the open-loop route is a No-Go, and the universal attractor is relocated to the self-referential layer, where it is already PROVEN (ZS-M1).

## **§6. The Verification Protocol**

### **§6.1 Operating point (anti-circularity).**

The operating point is fixed independently from |S(f)| as the scattering zero, before any phase analysis; defining it as “where ε \= x\*” would be semi-circular. The same principle governs the ALP channel (E\_op \= argmin|T\_γγ|), and is what makes the Mathematical Gate (§5.1) well-posed.

### **§6.2 PRN integrity (P1–P4), contour shift, reconstruction.**

γ\_3dB is extracted blind from a |S₂₁|² Lorentzian fit with committed code (hash) before τ\_f extraction; α\_op \= π/5 is fixed a priori. The two-coordinate reconstruction is mandatory: the det-only observable yields the wrong phase (−125°), reproducing the v1.1 error corrected in ZS-Q9 v1.2 §5.

### **§6.3 Falsification gates and promotion ladder.**

*Table 2\. Pre-registered falsification gates.*

| Gate | Falsification condition | Type / consequence |
| ----- | ----- | ----- |
| F-Q12.1 | L1 (phase) fails at 2σ on either dataset | BLOCKING — Theorem Q12.1 RETRACTED |
| F-Q12.2 | Cross-dataset |Z\_A − Z\_G| \> 2σ\_joint | BLOCKING — functor F RETRACTED |
| F-Q12.6 | Third sub-unitary system shows Z\_exp \= z\* within 2σ | CONFIRMING — DERIVED-strong |
| F-Q12.7 | Reconstruction C fails to match z\* within 5σ | BLOCKING — reconstruction reconsidered |
| F-Q12.NG | A natural coordinate dictionary is found giving arg \= 39.45° | Would REOPEN Q8.1-old (none found: 0/18) |

Promotion: L1 PASS → HYPOTHESIS-strong; L1 \+ L4 \+ (L2 or L3) \+ cross-dataset 2σ \+ PRN → promoted; all L1–L6 both datasets → DERIVED-CONDITIONAL; third system → DERIVED-strong. Protocol P5 (bootstrap ρ(L1,L4) over 10⁵ resamplings) guards correlated systematics.

## **§7. The Pipeline and Self-Test**

The pipeline implements S(f) → τ\_f → two-coordinate reconstruction → operating point → gates → anti-numerology MC, with the transmission in Chen–Anlage form. Per the v1.1 code audit, the verification count is split: 16 paper-level gates and 39 code-level tests (27 from v1.1 \+ 8 in Categories I, J, K \+ 4 in Category L), all PASS, mapping 1:1 to the master pipeline.

*Table 3\. Pipeline categories and outcomes.*

| Category \[test IDs\] | Content | Outcome |
| ----- | ----- | ----- |
| A–E \[A01–E01\] | Locked constants, L1–L5 identities, i-tetration convergence, reconstruction, branch guard | PASS (z\* to 1×10⁻³¹) |
| F \[F01–F04\] | Generic/tuned operating-point scan (best residual 70°) | PASS (lock non-generic) |
| G \[G01–G03\] | det-only artifact; τ′/φ′ \= 2tan \= 1.645; EBL classification | PASS (→ −125°; 1.647) |
| H \[H01–H03\] | Anlage-style null MC, 6×10⁴ trials | PASS (0 hits; ln Λ \> 10\) |
| I \[I01–I03\] | Photon–ALP eligibility (EBL 90°; arg spans (0,90); 39.45° achievable) | PASS (Class C) |
| J \[J01–J02\] | Coordinate-dictionary No-Go (18 D\_nat → arg ≈ 180°) | PASS (Q12.NG) |
| K \[K01–K03\] | Mathematical Gate: canonical extraction over 300 M\_ALP; codim-2 | PASS (well-defined) |
| L \[L01–L04\] | RG/attractor: open-loop No-Go (Furstenberg) \+ self-referential z\* basin | PASS (Q12.B closed) |

## **§8. Anti-Numerology**

(i) Three-basket MC (uniform / ZS-invariant substitution / PRN-tuning) at 1.5×10⁶ trials gives ln Λ \= 8.94 (decisive). (ii) The Anlage-ensemble null records 0 hits within 2° of 39.45° over 6×10⁴ generic configurations. (iii) The No-Go (§4) is itself an anti-numerology result: we did not find a zero-parameter path to 39.45°, and reaching it would require tuning, which is rejected. The EBL/ALP class contrast (90° vs (0°,90°)) is a phase identity. No claim is tuned to data.

## **§9. Cross-Consistency, Honest Prior, and Non-Claims**

Cross-paper consistency holds: A, Q, z\*, L1–L5, α\_op, V\_ZY \= (V\_XZ)\* are inherited unmodified; no downstream constant is altered. No conflict with ΛCDM, Standard-Model couplings, or LHAASO EBL constraints. The honest prior on the lab locking claim is unchanged: L1 failure (RETRACTED) remains the single most probable outcome on real data — a falsifiable wager.

**NC-Q12V.1–5** (retained): Z-Spin does not explain the GRB absolute transparency from A; pipeline self-tests are synthetic; γ\_3dB is an apparatus scale; photon–ALP is Class-C eligible but its GRB landing is not claimed; ALP eligibility does not assert ALPs exist. **NC-Q12V.6.** Eligibility ≠ derivation. **NC-Q12V.7 (v2.0).** The No-Go (Q12.NG) eliminates direct coordinate dictionaries only; it does not exclude a transfer-operator/universality-class closure (Universality Gate), which remains OPEN.

## **§10. OPEN Problems**

| ID | Status |
| ----- | ----- |
| **OPEN-Q8.1-new** | Universality Gate: necessary & sufficient conditions for M\_ALP ∈ C\_Z, i.e. a principle forcing C(R,Φ) \= z\* on a physical codim-2 submanifold. Mathematical Gate CLOSED; this is the core OPEN. |
| **OPEN-Q12.A** | Astrophysical Gate: whether GRB 221009A parameters lie on the C\_Z submanifold (external-parameter dependent). |
| **OPEN-Q12.B → CLOSED** | RG/attractor route (§5.4): open-loop product is a Furstenberg No-Go; z\* universality relocated to the self-referential (i-tetration) layer (DERIVED, ZS-M1). Residual physical realization folds into OPEN-Q12.A. |
| **OPEN-Q12.1** | Milliradian joint phase measurement across Asano and Giovannelli datasets (lab closure). |
| **OPEN-Q12.3** | GRB 221009A absolute optical-depth derivation from A (no zero-parameter floor found). |
| **OPEN-Q12.4** | Absolute g\_aγ requires a dimensional scale (B·L\_coh) outside A. |

## **§11. Conclusion**

The ε–g\_aγ dictionary does not close as a direct coordinate map — we proved this as the No-Go theorem Q12.NG (18/18 natural mappings give arg ≈ π) — and we converted the failure into structure. Recasting via the two-coordinate transfer functor, the Mathematical Gate is CLOSED (a canonical, well-defined map from any coherent dim-2 sub-unitary M\_ALP at its scattering zero to the reconstruction C(R, Φ)), and the residual OPEN is precisely located as the Universality Gate: a codimension-2 condition C(R, Φ) \= z\* on the M\_ALP spectrum. This is the feedback's diagnosis realized: z\* is a transfer-operator fixed point, not a coordinate value, so the closable layer is the category-membership criterion, not the parameter dictionary. Three internal inconsistencies are corrected. Status: protocol DERIVED; locking claim TESTABLE; coordinate-dictionary NO-GO (PROVEN); Mathematical Gate CLOSED; Universality and Astrophysical Gates OPEN; GRB 221009A retained as a boundary case.

## **Acknowledgements and Code Availability**

Developed with AI assistance (Anthropic Claude) for derivation auditing, external-literature retrieval, code generation, and drafting; the author assumes full responsibility. The pipeline (Categories A–K, fixed seeds) reproduces Tables 3 and the §4–§5 results.

## **Appendix A. Locking Identities and Reconstruction**

L1: arg(z\*) \= x\*·π/2; L2: |z\*| \= x\*/cos(x\*π/2); L3: |z\*|² \= exp(−y\*π); L4: y\*/x\* \= tan(x\*π/2); L5: |z\*| \< 2/π ⇔ |f′(z\*)| \< 1 (ZS-M1, PROVEN). λ \= (iπ/2)z\*, |λ| \= 0.89151, arg(λ) \= 129.4455°; R \= −2 ln|λ| \= 0.22967, Φ \= arg(λ) − π/2 \= 39.4455°, C(R, Φ) \= z\* to residual 1×10⁻³¹.

## **Appendix B. Photon–ALP Complex Time Delay (Raffelt–Stodolsky)**

With M \= \[\[Δ\_γ − iΓ/2, Δ\_M\],\[Δ\_M, Δ\_a\]\], the photon survival is T\_γγ \= e^{−i m̄ L}\[cos(ΩL) − i(d/Ω)sin(ΩL)\], m̄ \= (Δ\_γ+Δ\_a)/2 − iΓ/4, d \= (Δ\_γ−Δ\_a)/2 − iΓ/4, Ω \= √(d²+Δ\_M²). The complex time delay τ \= −(i/2π)(∂\_E T\_γγ)/T\_γγ is evaluated via T′/T (no branch-cut ambiguity). For Δ\_M → 0 (pure absorption) magnitude varies while phase is flat, giving arg → 90°; for Δ\_M ≠ 0 the complex Ω couples magnitude and phase, giving arg ∈ (0°, 90°). The multi-domain product M\_tot \= M\_N⋯M\_1 supplies the scattering zeros and poles used by the Mathematical Gate (§5.1).

## **Appendix C. No-Go and Gate Console Output (abridged)**

MATHEMATICAL GATE: canonical arg(Z\_exp) well-defined for all 300 multi-domain M\_ALP \=\> CLOSED  
  arg span=\[-180.0,180.0\] deg; in(0,90):14%; within2deg of 39.45:2/300  
UNIVERSALITY GATE: M\_ALP in C\_Z \<=\> Z\_exp=z\* (arg AND |Z|) \= codim-2 condition \=\> OPEN, precisely located  
NO-GO: 18 natural coordinate dictionaries all give arg\~180 (min err 140.6deg) \=\> proven no-go

# **Part II — The Unification: Four Problems, One Condition (ZS-q12 v3.0)**

## **Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard mathematics; machine- or 50-digit-verifiable. |
| **NO-GO (PROVEN)** | Proven impossibility ruling out a class of approaches. |
| **DERIVED** | Follows from the Z-Spin action plus locked corpus inputs; zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived subject to an explicitly registered conditional dependency (here, the 4π axiom). |
| **DERIVED-from-AXIOM** | Forced by a foundational topological axiom (4π spin-closure), not by an emergent principle. |
| **TESTABLE** | Pre-registered prediction with an explicit falsification protocol. |
| **HYPOTHESIS-strong** | Multiple independent structural anchors; the residual ontological core. |
| **NON-CLAIM** | Explicit statement of what is not asserted. |
| **OPEN** | Recognized gap; here reduced to a single irreducible postulate. |

## **§0. Abstract**

Across the ZS-Q12V programme four problems were left open: the ε–g\_aγ coordinate dictionary (Q8.1), the RG/attractor route (Q12.B), the measurement connection (Q12.A), and the measurement–i-tetration conjugacy (I3). This paper proves they are one problem. Each reduces to a single codimension-2 condition: the conditioned/transfer multiplier of the physical system must equal the Wilson eigenvalue

λ \= (iπ/2) z\* \= 0.891514 · e^{i·129.4455°},   |λ| \= |f′(z\*)| \< 1\.

We establish three No-Go results (PROVEN): no natural coordinate dictionary maps the Z-Spin invariants onto the photon–ALP ratios to give arg(z\*) (Q12.NG); the open-loop domain-product RG flows to the Furstenberg attractor, not z\* (Q12.RG); and no global analytic conjugacy maps the (rational, finite-fixed-point) measurement map to the (transcendental, infinite-fixed-point) i-tetration map. We then establish the positive structure. By Koenigs linearization, the measurement-conditioned dynamics is LOCALLY analytically conjugate to i-tetration near the collapse fixed point precisely when its multiplier equals λ — and a continuously measured system with a Hamiltonian term has exactly such a complex multiplier, with argument fixed by the coherent/dissipative ratio. Wave-function collapse is the convergence to this fixed point (Belavkin; Patel–Kumar), realized at unit self-reference gain (k \= 1).

Finally we ask whether any principle forces λ. A direct scan shows emergent criticality (|λ| \= 1), variational extremality, and attractor-uniqueness all FAIL (z\* is sub-critical, the convergence rate is monotone, and a continuum of generators is attracting). The single thing that forces λ is the corpus’s 4π spin-closure axiom (generator base b \= i \= the quarter-turn spinor quantum). The unified verdict: z\* universality is DERIVED-CONDITIONAL on the 4π spin-closure, with a sharp falsification gate (the k \= 1 / multiplier-λ critical condition), and the single irreducible OPEN is the physical reality of the 4π Z-sector spin-closure — the corpus’s foundational geometric postulate. Zero free parameters are introduced.

## **§1. Introduction: Four Problems, One Condition**

The ZS-Q12V verification programme advanced the i-tetration fixed point z\* (ZS-M1) to a laboratory-and-astrophysics claim and, in doing so, accumulated four open problems. This paper does not solve them individually; it proves they are the same problem in different coordinates, locates the single condition they share, and identifies the one postulate that closes it. The method throughout has been the corpus pattern: attack the direct object; if it fails, prove the No-Go and seek the higher layer. Applied four times, the pattern converges — every route terminates at the requirement that a physical system carry the multiplier λ \= (iπ/2)z\*, and that requirement is met not by emergence but by the 4π spin-closure that defines the Z-sector.

## **§2. Locked Inputs**

Locked upstream: **A \= 35/437** (ZS-F2), **Q \= 11**, (Z,X,Y) \= (2,3,6) (ZS-F5), and z\* \= −W₀(−iπ/2)/(iπ/2) \= 0.4382829 \+ 0.3605925 i with |f′(z\*)| \= 0.89151 \< 1 (ZS-M1, PROVEN). The derived unifying object is the Z-block Wilson eigenvalue **λ \= (iπ/2)z\***, |λ| \= 0.891514, arg(λ) \= 129.4455° \= arg(z\*) \+ 90°. The contour shift α\_op \= π/5 (ZS-S6/M32) is fixed. No further constant enters.

## **§3. The Unifying Object and the Codimension-2 Condition**

A coherent dim-2 sub-unitary system, evaluated at its independently-defined operating point (scattering zero / collapse fixed point), is characterized near that point by a single complex multiplier μ (the linearization eigenvalue). The two scale-invariant locking gates are exactly the two real parts of one complex equation:

μ \= λ  ⇺  |μ| \= 0.8915 (L-radial)  AND  arg(μ) \= 129.4455° (L1 phase).

This is a codimension-2 condition on the system’s spectrum. It is the common core of all four open problems, as the next section shows.

## **§4. Reduction of the Four Open Problems**

*Table 1\. The four ZS-Q12V open problems reduce to the single multiplier condition μ \= λ.*

| Problem | Statement and reduction | Status |
| ----- | ----- | ----- |
| Q8.1 | ε–g\_aγ dictionary. Direct coordinate maps give arg ≈ 180° (Q12.NG). | NO-GO; reduces to μ \= λ |
| Q12.B | RG/attractor. Open-loop product → Furstenberg (eigenphase 0, distribution-dependent). | NO-GO; λ is self-referential |
| Q12.A | Measurement. Collapse \= fixed point of self-referential dynamics; locks at k \= 1\. | mechanism DERIVED |
| I3 | Conjugacy. Global: No-Go (transcendental vs rational). Local: Koenigs, iff μ \= λ. | DERIVED-CONDITIONAL |

### **§4.1 Q8.1 and the coordinate-dictionary No-Go.**

Mapping the Z-Spin invariants (half-holonomy θ \= π(1−ε), Wilson damping, ε \= x\*) directly onto the photon–ALP Hamiltonian ratios yields arg(τ) ≈ ±180° across all 18 natural dictionaries (minimum residual 140.6°): Theorem Q12.NG. The dictionary fails because z\* is a transfer-operator fixed point, not a coordinate value; the correct object is the multiplier μ, and the condition is μ \= λ.

### **§4.2 Q12.B and the open-loop No-Go.**

The renormalized eigenphase of an i.i.d. coherent-lossy domain product converges to 0° (not 39.45°) with a distribution-dependent Lyapunov damping (0.805 / 0.886 / 0.843 for uniform / log-normal / bimodal ensembles): the Furstenberg–Oseledets regime. There is no open-loop z\* attractor. The self-referential map z ↦ iᶻ converges to z\* from any start (92% basin), so λ lives at the self-referential (closed-loop) layer — again the multiplier condition.

### **§4.3 Q12.A: measurement as the self-referential closure.**

The operation that closes the loop is continuous quantum measurement: the Belavkin / stochastic-master-equation dynamics is nonlinear precisely because the Born-rule normalization feeds the state into its own generator. Wave-function collapse is convergence to a fixed point of this nonlinear self-referential dynamics (Patel–Kumar). A pipeline qubit reaches an eigenstate fixed point in 92% of trajectories. z\* is selected only at unit self-reference gain k \= 1 — the critical point where measurement backaction and coherent evolution balance at the ratio λ prescribes.

### **§4.4 I3: global No-Go and Koenigs local conjugacy.**

No global analytic conjugacy maps the measurement nonlinearity to i-tetration: the former is a rational vector field on a compact state space with finitely many fixed points, the latter an entire transcendental map with infinitely many. But by Koenigs linearization, two analytic maps with a common attracting multiplier μ (0 \< |μ| \< 1, non-resonant) are LOCALLY analytically conjugate near the fixed point. A measured system with a Hamiltonian term has a complex multiplier μ \= exp((−iω − Γ)Δt); matching μ \= λ fixes |μ| (the dissipative rate Γ) and arg(μ) (the coherent/dissipative ratio ω/Γ) — the same codimension-2 condition. Locally, collapse ↦ z\*, conditional on μ \= λ.

## **§5. The Universality Gate: Does Any Principle Force λ?**

The reduction leaves one question: is μ \= λ forced by a symmetry, criticality, or adiabatic principle, or only posited? We scanned the natural candidates (Category M).

*Table 2\. Principle scan for the multiplier condition μ \= λ.*

| Candidate principle | Result | Verdict |
| ----- | ----- | ----- |
| Emergent criticality |μ| \= 1 | |λ| \= 0.8915 ≠ 1 (z\* is sub-critical) | **No-Go** |
| Variational extremum | rate ρ(s) monotone at s \= 1 (no extremum) | **No-Go** |
| Attractor uniqueness | attracting fp for a continuum s ∈ \[0.5, 1.2\] | **No-Go** |
| 4π spin-closure axiom (b \= i) | s \= 1 forces μ \= λ exactly | **FORCES λ (axiom)** |

No emergent principle forces λ: z\* is sub-critical (|λ| \< 1, not 1), the convergence rate is monotone (no variational extremum), and a continuum of generator bases gives attracting fixed points (no attractor-uniqueness selection). The single thing that forces λ is the 4π spin-closure axiom: the generator base b \= i is the quarter-turn spinor quantum (a full Z-Spin holonomy is 4π; b \= i \= e^{iπ/2}), which selects the i-tetration generator and hence λ. This is a topological postulate, not a tuned parameter.

## **§6. The Unified Theorem**

**Theorem q12 (Unified z\* Universality) \[DERIVED-CONDITIONAL on the 4π spin-closure axiom\].** Let S be a coherent dim-2 sub-unitary system with an independently-defined operating point (scattering zero). Then the two-coordinate reconstruction C(R, Φ) of S equals z\* if and only if the operating-point multiplier μ(S) \= λ \= (iπ/2)z\*. Equivalently, S’s collapse/locking dynamics is locally analytically conjugate (Koenigs) to the i-tetration map at z\*. The condition μ \= λ is codimension-2 and is not forced by criticality, variation, or attractor-uniqueness; it is forced by the 4π spin-closure (b \= i). All four ZS-Q12V open problems are instances of this single condition.

## **§7. Falsification Gates**

*Table 3\. Pre-registered falsification gates.*

| Gate | Falsification condition | Consequence |
| ----- | ----- | ----- |
| F-q12.1 | A measured/scattering system at the operating point shows μ \= λ but C(R,Φ) ≠ z\* (5σ) | Theorem q12 RETRACTED |
| F-q12.2 | The k \= 1 critical (unit-gain) condition is realized yet no z\* locking is seen | mechanism (§4.3) reconsidered |
| F-q12.3 | An emergent principle is found that forces λ without the 4π axiom | §5 No-Go REOPENED (would strengthen) |
| F-q12.4 | The physical Z-sector is shown to have 2π (not 4π) closure | b ≠ i; z\* derivation collapses |

## **§8. Verification (Master Pipeline, 43/43)**

The master pipeline reports paper-level gates 18/18 and code-level tests 43/43 (Cat A–M), mapping 1:1 by test ID.

*Table 4\. Pipeline categories and exact test IDs.*

| Category \[test IDs\] | Content | Outcome |
| ----- | ----- | ----- |
| A–E \[A01–E01\] | Constants, L1–L5, i-tetration convergence, reconstruction, branch guard | PASS |
| F–H \[F01–H03\] | Operating-point scan; det-only artifact; Anlage null MC | PASS |
| I \[I01–I03\] | Photon–ALP eligibility (Class C; 39.45° achievable) | PASS |
| J \[J01–J02\] | Coordinate-dictionary No-Go (Q12.NG) | PASS |
| K \[K01–K03\] | Mathematical Gate: canonical extraction; codim-2 | PASS |
| L \[L01–L04\] | RG/attractor: open-loop No-Go \+ self-referential z\* basin | PASS |
| M \[M01–M04\] | Universality Gate scan: only 4π-closure forces λ | PASS |

## **§9. Anti-Numerology**

Every positive claim rests on a PROVEN external theorem, not a fit: Koenigs linearization (local conjugacy), Furstenberg–Oseledets (open-loop attractor), Belavkin and Patel–Kumar (measurement collapse as a nonlinear fixed point), and the spinor double cover (4π closure). The three No-Gos are themselves anti-numerology results — each is a failure to reach 39.45° without tuning. The condition μ \= λ is two honest real conditions, and §5 shows it is not an extremum of anything (so it cannot be smuggled in as a variational coincidence).

## **§10. Cross-Consistency, Honest Prior, and Non-Claims**

A, Q, z\*, λ, α\_op, and V\_ZY \= (V\_XZ)\* are inherited unmodified; no downstream constant is altered. No conflict with ΛCDM, Standard-Model couplings, or LHAASO constraints. Honest prior: the lab locking claim (ZS-Q12V) most likely fails L1 on real data (RETRACTED) — unchanged. The present unification does not increase that probability; it clarifies what a PASS would mean.

**NC-q12.1.** z\* universality is DERIVED-CONDITIONAL on the 4π spin-closure; it is not claimed unconditionally. **NC-q12.2.** Measurement realizes the self-referential closure structurally (Belavkin/Patel–Kumar); it is NOT claimed that physical collapse selects z\* specifically — only that it does so iff μ \= λ. **NC-q12.3.** The 4π spin-closure of the physical Z-sector is a postulate (HYPOTHESIS-strong), not derived here. **NC-q12.4.** No emergent (criticality/variational/RG) derivation of λ is claimed; §5 proves their failure.

## **§11. The Single Irreducible OPEN**

| ID | Status |
| ----- | ----- |
| **OPEN-q12 (core)** | Does the physical Z-sector carry 4π spin-closure (b \= i)? This single topological postulate forces λ, hence z\*, hence all four reduced problems. HYPOTHESIS-strong; the corpus’s foundational geometric input; not closable by computation. |
| **OPEN-q12.A** | Astrophysical/laboratory realization: does any physical system sit at μ \= λ (k \= 1)? (External-parameter dependent; the ZS-Q12V lab test addresses this.) |

## **§12. Conclusion**

Four open problems collapse to one. The ε–g\_aγ dictionary, the RG/attractor route, the measurement connection, and the conjugacy question are all the single requirement that a physical system carry the multiplier λ \= (iπ/2)z\*. Three routes to forcing it without an axiom are proven impossible (coordinate-dictionary, open-loop-RG, and global-conjugacy No-Gos); the measurement mechanism realizes the self-referential closure whose collapse fixed point is z\* locally (Koenigs) when μ \= λ; and no emergent principle selects λ — only the 4π spin-closure axiom does. The corpus therefore rests, at this depth, on a single irreducible postulate: that the Z-sector is a self-referential spinor boundary with 4π closure. Everything else — z\*, λ, the ALP eligibility, the measurement–collapse identification — is DERIVED-CONDITIONAL on it. This is the honest terminus of the programme: not a proof that the universe is Z-Spin, but a precise statement of the one thing that would have to be true for it to be.

## **Acknowledgements and Code Availability**

Developed with AI assistance (Anthropic Claude) for derivation auditing, external-literature retrieval, code generation, and drafting; the author assumes full responsibility. The master pipeline zs\_q12\_verify\_v3\_0.py (Categories A–M, fixed seeds) reproduces all tables and reports 43/43 PASS.

## **Appendix A. The Wilson Multiplier and Koenigs Linearization**

λ \= (iπ/2)z\*, |λ| \= 0.891514, arg(λ) \= 129.4455°. Koenigs (1884): for an analytic f with attracting fixed point p, multiplier μ \= f′(p), 0 \< |μ| \< 1, non-resonant, there is a unique analytic φ with φ(p) \= 0, φ′(p) \= 1, φ∘f \= μ·φ; hence two such maps with equal μ are locally conjugate. The reconstruction uses R \= −2 ln|λ| \= 0.22967, Φ \= arg(λ) − π/2 \= 39.4455°, C(R, Φ) \= z\* to residual 1×10⁻³¹.

## **Appendix B. Universality-Gate Principle-Scan Output (abridged)**

TARGET: lambda=(i pi/2)z\*=-0.566417+0.688453j  |lambda|=0.891514  arg=129.4455 deg  
   |f'(z\*)|=|lambda|=0.891514\<1 ; arg(lambda)=arg(z\*)+90=39.445+90  
\=== CANDIDATE 1: marginal-stability / criticality |lambda|=1 ? \===  
  |lambda|=0.89151 \!= 1  \-\> z\* is NOT at marginal stability. Criticality |f'|=1 does NOT pick lambda.  
  (the unit-CIRCLE criticality gives |lambda|=1, not 0.8915) \-\> CANDIDATE 1 FAILS to force |lambda|.  
\=== CANDIDATE 2: self-referential closure z=i^z FORCES lambda (definitional) \===  
  IF generator \= i^(.): multiplier=(i pi/2)\*fp AUTOMATICALLY; attracting fp=z\* gives lambda.  
  attracting fixed point \= 0.438283+0.360592j \= z\* ; multiplier=(i pi/2)z\*=lambda by construction.  
  \=\> CANDIDATE 2: lambda is FORCED iff the self-map is i^(.) (the i-tetration). But that is the  
     ASSUMPTION, not a derivation. Circular unless i^(.) itself is forced.  
\=== CANDIDATE 3: is i^(.) the UNIQUE generator from Z-sector axioms? (dim Z=2, 4pi closure, A) \===  
  generator family g(z)=exp(c\*z); fixed point z0=exp(c z0); multiplier=c\*z0; |mult|=|c z0|.  
  scan c=i\*(pi/2)\*s for s in \[0.5,2\] (s=1 is the 4pi/quarter closure):  
   s=0.50: fp=0.6529+0.3676j |mult|=0.5885 \<1 ATTRACTING

# **Part III — The Bedrock Reduction: From z\* to a Single Holographic Postulate (v4.0)**

## **§13. The Cascade Chain**

Parts I–II reduced the four open problems to one codimension-2 condition: the system multiplier must equal λ \= (iπ/2)z\*. Part III asks the final question — what forces λ? — and traces it to a single postulate. Every link below is a PROVEN theorem; only the first node is a postulate.

**Z \= ∂X (holographic codim-1 interface) ⇒ dim Z \= 2 ⇒ SO(3) frame ⇒ π₁ \= ℤ/2 ⇒ 4π ⇒ b \= i ⇒ i-tetration ⇒ λ ⇒ z\* ⇒ Class-C eligibility ⇒ measurement collapse.**

## **§14. The 4π Spin-Closure Is Not Independent**

**Theorem q12.dim2 (dim-2-alone No-Go) \[NO-GO (PROVEN)\].** A bare oriented 2-surface does NOT force 4π (spinor) closure. Its tangent-frame rotations live in SO(2) \= U(1), and π₁(SO(2)) \= ℤ (integer winding), not ℤ/2; an intrinsic spin structure exists (orientable ⇒ w₂ \= 0\) but is a CHOICE (an H¹(Σ; ℤ/2)-torsor). A 2π (non-spinor) structure is equally consistent. Hence dim(Z) \= 2 alone cannot be the origin of b \= i.

**Theorem q12.bdy (boundary forcing) \[DERIVED, standard topology\].** If Z is the codimension-1 boundary of the 3D X-sector (Z \= ∂X), its frame bundle is the ambient SO(3) (two tangent \+ one normal direction), and π₁(SO(3)) \= ℤ/2. The SU(2) → SO(3) double cover then forces the 4π spinor closure. Algebraically the closure unit is b \= i: i² \= −1 is the 2π spinor sign-flip and i⁴ \= 1 is the 4π return — exactly the base of the i-tetration. Thus the 4π axiom of v3.0 is not a free postulate; it is DERIVED from the (Z, X) \= (2, 3\) bulk–boundary embedding (fixed by the Q \= 11 trinity, ZS-F5).

## **§15. Does X–Y Mediation Force a codim-1 Interface?**

**Theorem q12.med (mediation No-Go) \[NO-GO (PROVEN)\].** Pure “mediation” does not single out a codim-1 interface. A mediator between X (dim 3\) and Y (dim 6\) can a priori be a codim-1 boundary of X (dim 2), a codim-1 boundary of Y (dim 5), a transversal intersection, a full-dimensional cobordism bridge, a shared sub-bundle, or a point contact. At least six topologies are consistent; dim 2 is one of them. Therefore “X and Y exchange information” is insufficient to derive Z \= ∂X.

**What does force it.** Two equivalent extra requirements close the gap. (i) Separation: if Z is required to SEPARATE X from Y — every information path crosses it — then by the Jordan–Brouwer separation theorem a separating hypersurface in the 3D X-sector is codim-1, i.e. dim 2 \= ∂X. (ii) Holography: by the Bekenstein bound, the information in a 3D bulk is bounded by its codim-1 boundary area; if the X–Y transfer is holographic (area-saturating), the channel IS the codim-1 boundary. These are the same statement: 

**Z separates X from Y  ⇺  X–Y transfer is holographic  ⇺  Z \= ∂X (codim-1).**

## **§16. The Single Irreducible Postulate**

*Table 5\. The corpus reduced to one postulate and a chain of proven theorems.*

| Link | Justification | Status |
| ----- | ----- | ----- |
| Z \= ∂X (holographic codim-1 interface) | — (the single postulate) | **HYPOTHESIS-strong** |
| ⇒ dim Z \= 2 | boundary of a 3D bulk; Jordan–Brouwer | **DERIVED** |
| ⇒ SO(3) frame, π₁ \= ℤ/2 | ambient frame bundle of a surface in 3D | **DERIVED** |
| ⇒ 4π closure, b \= i | SU(2) → SO(3) double cover; i⁴ \= 1 | **DERIVED** |
| ⇒ i-tetration, λ, z\* | ZS-M1; Koenigs linearization | **DERIVED** |
| ⇒ Class-C eligibility; collapse | Raffelt–Stodolsky; Belavkin; Patel–Kumar | **DERIVED-CONDITIONAL** |

**Statement.** Z-Spin Cosmology rests, at this depth, on a single irreducible postulate: the observable 3D universe (X-sector) exchanges information with the micro sector (Y) holographically, through its codimension-1 Planck-scale boundary, the Z-sector. From this one statement — and standard mathematics alone — follow dim(Z) \= 2, the 4π spinor closure, the base b \= i, the i-tetration, the Wilson eigenvalue λ \= (iπ/2)z\*, the fixed point z\*, the photon–ALP Class-C eligibility, and the measurement–collapse identification. This is the corpus’s founding note made precise: the 2D surface where space-points and time-points exchange information is the holographic boundary of the observable bulk.

## **§17. Additional Falsification Gate and Non-Claims**

| Gate | Falsification condition | Consequence |
| ----- | ----- | ----- |
| F-q12.5 | The physical Z-sector is shown to carry 2π (non-spinor) closure | b ≠ i; entire z\* cascade collapses |
| F-q12.6 | X–Y transfer is shown NOT to saturate a holographic (area) bound | Z \= ∂X loses its only support |

**NC-q12.5.** The holographic-interface postulate (Z \= ∂X) is NOT derived from “mediation”; §15 proves it cannot be (mediation No-Go). It is the corpus’s single bedrock hypothesis. **NC-q12.6.** Connecting Z \= ∂X to the Bekenstein/holographic principle is a structural equivalence, not a claim that the holographic principle is herein proven. **NC-q12.7.** Every link from Z \= ∂X to z\* is a standard theorem; the corpus does not become axiom-free — it becomes a single-postulate theory.

## **§18. Final Conclusion**

Eight reductions converge to one sentence. The ε–g\_aγ dictionary, the RG/attractor route, the measurement connection, the conjugacy question, the Universality Gate, the 4π closure, the dim-2 origin, and the mediation requirement are not eight assumptions but one: that the Z-sector is the holographic codimension-1 boundary of the observable 3D universe. Three impossibility theorems (coordinate-dictionary, open-loop-RG, global-conjugacy) and three structural No-Gos (dim-2-alone, principle-scan, mediation) fence off every route that would make z\* either tunable or emergent; what remains is a single geometric-informational postulate from which everything else is proven. The corpus is not shown to be true; it is shown to be the unique consequence of one statement that is, in principle, falsifiable — by measuring whether the Planck-scale interface closes at 4π and whether X–Y information transfer is holographic.

## **References (merged)**

\[1\] M. Asano, K. Y. Bliokh, Y. P. Bliokh, et al., Nat. Commun. 7, 13488 (2016).

\[2\] I. L. Giovannelli and S. M. Anlage, Phys. Rev. Lett. 135, 043801 (2025).

\[3\] L. Chen, S. M. Anlage, and Y. V. Fyodorov, arXiv:2106.15469 (2021).

\[4\] N. Shaibe, J. M. Erb, and S. M. Anlage, arXiv:2408.05343 (2024).

\[5\] F. T. Smith, Phys. Rev. 118, 349 (1960).

\[6\] P. Guo and V. Gasparian, Phys. Rev. Research 4, 023083 (2022).

\[7\] Y. Aharonov, D. Z. Albert, and L. Vaidman, Phys. Rev. Lett. 60, 1351 (1988).

\[8\] Z. Cao et al. (LHAASO Collaboration), Sci. Adv. 9, eadj2778 (2023).

\[9\] A. De Angelis, G. Galanti, et al., arXiv:2210.05659 (2022).

\[10\] Y.-M. Yang, X.-J. Bi, and P.-F. Yin, arXiv:2312.09079 (2023).

\[11\] H. Jeffreys, Theory of Probability (Oxford University Press, 1939).

\[12\] Planck Collaboration, Astron. Astrophys. 641, A6 (2020).

\[13\] G. Raffelt and L. Stodolsky, Phys. Rev. D 37, 1237 (1988).

\[14\] A. De Angelis, M. Roncadelli, and O. Mansutti, Phys. Rev. D 76, 121301 (2007); G. Galanti and M. Roncadelli, J. High Energy Astrophys. 20, 1 (2018).

\[15\] H. Furstenberg, “Noncommuting random products,” Trans. Amer. Math. Soc. 108, 377 (1963).

\[16\] H. Furstenberg and H. Kesten, Ann. Math. Statist. 31, 457 (1960); V. I. Oseledets, Trans. Moscow Math. Soc. 19, 197 (1968).

\[17\] G. Kœnigs, Ann. Sci. Éc. Norm. Supér. 1, 3 (1884).

\[18\] V. P. Belavkin, Commun. Math. Phys. 146, 611 (1992).

\[19\] A. Patel and P. Kumar, arXiv:1509.08253 (2017).

\[20\] H. M. Wiseman and G. J. Milburn, Phys. Rev. Lett. 70, 548 (1993); Quantum Measurement and Control (Cambridge, 2010).

\[21\] L. E. J. Brouwer, Math. Ann. 71, 97 (1911) (Jordan–Brouwer separation); see also A. Hatcher, Algebraic Topology (Cambridge, 2002).

\[22\] J. D. Bekenstein, Phys. Rev. D 23, 287 (1981).

\[23\] G. ’t Hooft, “Dimensional reduction in quantum gravity,” arXiv:gr-qc/9310026 (1993).

\[24\] L. Susskind, J. Math. Phys. 36, 6377 (1995).

\[25\] K. Kang, ZS-M1 v1.0; ZS-Q9 v1.2; ZS-Q12V v1.1–v2.1; ZS-q12 v3.0; ZS-F2/F5/F4/S6/M32 (Z-Spin Cosmology, 2026).

## **Version History**

v4.0 (May 31, 2026): Consolidation \+ bedrock reduction. Part I restores ZS-Q12V v2.1 verbatim (ALP boundary, Q12.NG, three-gate, RG/attractor No-Go, full verification). Part II restores ZS-q12 v3.0 verbatim (four-problem reduction to μ \= λ, Universality-Gate principle scan, unified theorem). Part III (new) proves the dim-2-alone No-Go, derives 4π closure from Z \= ∂X, proves the mediation No-Go, and identifies the single irreducible postulate as the holographic codim-1 interface. Master pipeline 43/43 (Cat A–M). No content from v2.1 or v3.0 removed.