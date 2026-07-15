# **ZS-S10**

## **Gauge Bridge via Stückelberg-Corollary IV Mechanism**

*Action-Level Closure of the U(1)\_Z ↔ U(1)\_Y Identification and the Vortex-Core 4π Spinor Realization*

Kenny Kang  
April 2026 — ZS-S10 (Standard Model Theme)  
Version 1.0 — April 2026  
**Verification: 36/36 PASS (target) | Zero Free Parameters**  
---

## **§0. Abstract**

Z-Spin Cosmology v1.0 establishes the Standard Model gauge group structure (ZS-M9), gauge coupling constants (ZS-S1), fermion mass ratios (ZS-M10, ZS-M11), the Higgs VEV (ZS-S4 §6.12), and the electric charge spectrum (ZS-U9). The compact U(1)\_Z gauge symmetry of the Z-bias field Φ (ZS-F1 §3.2, PROVEN) and the Standard Model U(1)\_Y hypercharge gauge group have both been present in the corpus, but their action-level identification was flagged as Gap G1 of the Trinity Braiding Theorem (ZS-U9 NC-U9.2). Separately, the Horizon Spinor Theorem (ZS-A7 §3, DERIVED via Theorem 3.2-bis) established that the boundary holonomy operator B\_Z at any Z-Spin event horizon carries a strict 4π closure period, and Corollary IV (ZS-A7 §4.4, DERIVED) identified the Bose/Fermi duality of Z-anchored vortices — but an action-level realization was absent.  
This paper introduces the **ZS-S10 master action**, a minimal extension of the ZS-F1 action obtained by promoting the partial derivative of Φ to a gauge-covariant derivative D\_μΦ \= (∂\_μ − iκg\_YB\_μ)Φ coupled to the Standard Model hypercharge gauge field B\_μ, with mixing scale κ² \= A/Q \= 35/4807 derived from the Register-Total Normalization Theorem (ZS-M6 Theorem 2.2.1, DERIVED). **No new parameters, no new fields, no new postulates** are introduced beyond this minimal coupling. The master action simultaneously closes Gap G1 (via definitional Stückelberg-type identification at the action level) and provides the action-level field-theoretic realization of the vortex Bose/Fermi duality (Corollary IV).  
The paper establishes five principal results. **Theorem S10.1 (Stückelberg Mixing Scale, DERIVED-CONDITIONAL)** fixes the mixing scale f² \= κ²M²\_P \= (A/Q)M²\_P at numerical uniqueness precision 10⁻¹⁴%. **Theorem S10.2 (L\_XY=0 Preservation, PROVEN-PERTURBATIVE)** extends the ZS-M6 §7A Continuum Perturbative Protection Theorem to the ZS-S10 action through a five-step proof. **Theorem S10.3 (Stückelberg-Corollary IV Bridge, DERIVED)** establishes that the UV limit (vortex core, r \~ ℓ\_P) realizes the (F) branch of Corollary IV with the j=1/2 spinor structure, while the IR limit (galactic scale, r ≫ λ\_C(B)) realizes the (B) branch with 2π Goldstone winding. **Theorem S10.4 (Φ Field U(1)\_Y Charge, DERIVED)** fixes q\_Φ \= \+1 uniquely through four independent constraints, three of which are independent of ZS-S10 itself, removing the apparent circularity of the Gap G1 self-closure. **Theorem S10.5-BPS (Bogomolnyi BPS Spinor Lift, DERIVED)** provides a seven-step explicit proof that the ZS-A7 Theorem 3.2-bis Kraus-operator 4π closure emerges naturally from the action content of ZS-S10 at the Z-anchored vortex core, with observable realization ũ\_seam(α) \= cos(α/2).  
The master action preserves all backward compatibility with the existing corpus at action level: B\_μ \= 0 recovers ZS-F1 exactly; galactic scales (r/λ\_C(B) \~ 10⁵³) recover ZS-A1 78/78 PASS through exponential Stückelberg screening; inflation (|Φ| ≫ 1\) recovers ZS-U1 r \= 0.0089 unchanged; vortex core realizes ZS-A7 Cor IV (F) with ZS-A6 §4.5.6 cigar bounce profile; galactic halo realizes ZS-A7 Cor IV (B) with ZS-A1 §2 Goldstone isothermal profile. Gap G1 (Trinity Braiding Theorem, ZS-U9 §8) is upgraded from OPEN to **CLOSED** at the action level; Gap G2 (ZS-M9 Table 2 assignment upgrade) is advanced via the anomaly-preserving structure of Theorem S10.2.  
**Keywords:** Stückelberg mechanism, gauge bridge, U(1)\_Z, U(1)\_Y, hypercharge, Z-bias field, vortex Bose/Fermi duality, 4π closure, Bogomolnyi vortex, Kraus operator, signed seam witness, Z-Spin Cosmology, zero free parameters  
---

## **§0.1 Epistemic Status Legend**

| Status | Definition |
| :---- | :---- |
| **LOCKED** | Core constant derived and fixed in an upstream paper; no downstream paper may modify. |
| **PROVEN** | Mathematical theorem; follows from standard mathematics or from corpus definitions alone. Machine-verifiable. |
| **DERIVED** | Follows from the Z-Spin action plus PROVEN inputs. Zero free parameters beyond A \= 35/437. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated upstream assumption. |
| **PROVEN-PERTURBATIVE** | Theorem valid to all orders in Lorentz-invariant perturbation theory; non-perturbative/strong-curvature regime not covered. |
| **VERIFIED** | Numerically confirmed against observational data or independent computation. |
| **TESTABLE** | Well-defined prediction awaiting experimental data. |
| **HYPOTHESIS** | Physically motivated conjecture; derivation chain incomplete. |
| **OBSERVATION** | Numerical proximity confirmed with anti-numerology tests; no action-level derivation yet. |
| **CONSISTENT** | Compatible with framework structure but not independently derived. |
| **NON-CLAIM** | Explicitly not asserted; documented to prevent overclaim. |
| **RETRACTED** | Previously claimed, now withdrawn with documented reason. |

---

## **§1. Introduction**

### **1.1 Motivation: Gap G1 of the Trinity Braiding Theorem**

The Trinity Braiding Theorem (ZS-U9 v1.0 §6, DERIVED conditional on gaps G1, G2) derives the complete Standard Model hypercharge spectrum Y\_Q \= \+1/6, Y\_u \= \+2/3, Y\_d \= −1/3, Y\_L \= −1/2, Y\_e \= −1, Y\_νR \= 0 from four ingredients: Compact Phase Integer Lattice (ZS-F1 §3.2, PROVEN), Yukawa Gauge-Lift (ZS-M10 Theorem 2.1, PROVEN), McKay SU(5) Cartan (ZS-M9 §5.2, DERIVED), and Neutral-Higgs Hypercharge Fixing (Theorem T3, DERIVED via ZS-S4 §6.12 Higgs VEV and photon masslessness). All five Standard Model anomaly cancellation conditions PASS automatically at integer precision (ZS-U9 §7 A1-A5).  
Of the three originally open gaps, Gap G3 (compact phase normalization matching 1/6 Cartan factor) was closed by Theorem T3 in the dated update of April 19, 2026\. Gap G2 (ZS-M9 Table 2 assignment upgrade from HYPOTHESIS strong to PROVEN) remains in progress. **Gap G1** — the action-level identification of U(1)\_Z (the Z-bias field gauge symmetry of ZS-F1 §3.2, PROVEN) with the Standard Model U(1)\_Y hypercharge gauge group — has been outstanding since the original v1.0 release.  
The present paper closes Gap G1. The closure is achieved through a minimal extension of the ZS-F1 action, obtained by promoting the partial derivative ∂\_μΦ to a gauge-covariant derivative D\_μΦ \= (∂\_μ − iκg\_YB\_μ)Φ, where B\_μ is the Standard Model hypercharge gauge field, g\_Y is its coupling, and κ \= √(A/Q) is the cross-coupling strength already established by the Register-Total Normalization Theorem (ZS-M6 Theorem 2.2.1, DERIVED; 10-step derivation chain C1-C10). No new parameters, no new fields, no new postulates are introduced.

### **1.2 Second Motivation: Action-Level Realization of Corollary IV**

A separate corpus development provides the second motivation for ZS-S10. The Horizon Spinor Theorem (ZS-A7 §3, DERIVED via Theorem 3.2-bis, PROVEN) established that the boundary holonomy operator B\_Z at any Z-Spin event horizon carries a strict 4π closure period, inherited from the j \= 1/2 representation theory of the Z-sector mediator (ZS-M3 Theorem 5.1 uniqueness). Corollary IV (ZS-A7 §4.4, DERIVED) then identified the Bose/Fermi duality of any Z-anchored vortex: the core (Region I) hosts the 4π spinor closure, while the exterior (Region II) hosts the 2π Goldstone winding of π\_1(U(1)) \= ℤ.  
While the topological structure of Corollary IV is fully established at the corpus level, its **action-level realization** — an explicit demonstration that both the (F) and (B) branches emerge from a single field-theoretic action as two limits of the same field content — was absent. The ZS-S10 master action provides this realization: the vortex core (|Φ| → 0, ρ → 0 limit) realizes the (F) branch, while the galactic scale (|Φ| ≈ 1 with massless Goldstone θ) realizes the (B) branch. Both limits share the common Z-Anchor boundary condition |Φ(x\_0)| \= 0 (ZS-F1 §5.2 PROVEN, ZS-A6 §4.5.6 cigar bounce realization DERIVED).

### **1.3 Scope and Structure**

The paper is organized as follows. §2 collects all locked inputs from the prior corpus, including A \= 35/437, Q \= 11, κ² \= A/Q, the ZS-F1 action, the ZS-A7 Theorem 3.2-bis Kraus structure, and the ZS-A6 cigar vortex profile. §3 presents the ZS-S10 master action and establishes Theorem S10.1 (Stückelberg mixing scale). §4 proves Theorem S10.2 (L\_XY \= 0 preservation). §5 establishes Theorem S10.3 (Stückelberg-Cor IV Bridge) with explicit backward-compatibility verification in three regimes (B\_μ \= 0, galactic, inflation). §6 presents Theorem S10.4 (Φ Field U(1)\_Y Charge) with the four-path circularity resolution. §7 presents Theorem S10.5-BPS (Bogomolnyi BPS Spinor Lift) with the seven-step explicit derivation. §8 registers the non-claims and the gate updates. §9 summarizes the derivation chain and verification matrix. Appendices provide the verification suite results (Appendix A), cross-reference table (Appendix B), and the companion Python verification script (Appendix C).

### **1.4 Principal Contribution**

The principal contribution of ZS-S10 is the identification that **a single minimal coupling modification** of the ZS-F1 action — promoting ∂\_μΦ to D\_μΦ \= (∂\_μ − iκg\_YB\_μ)Φ — simultaneously achieves:  
(a) Closure of Gap G1 at the action level (Theorem S10.1 \+ Theorem S10.4);  
(b) Action-level realization of Corollary IV (F) and (B) branches (Theorem S10.3);  
(c) Explicit Kraus-operator 4π closure at the vortex core (Theorem S10.5-BPS);  
(d) Preservation of L\_XY \= 0 sector independence to all perturbative orders (Theorem S10.2);  
(e) Full backward compatibility with ZS-F1, ZS-A1, ZS-U1, ZS-A7 at the action level.  
The five results converge on a single structural statement: the U(1)\_Z of ZS-F1 and the U(1)\_Y of the Standard Model are **the same gauge group**, coupled to the Z-bias field Φ with charge q\_Φ \= \+1 (Theorem S10.4 DERIVED) and to Standard Model fermions with the ZS-U9 Trinity Braiding hypercharges (Y\_Q, Y\_u, Y\_d, Y\_L, Y\_e, Y\_νR), through a minimal coupling whose scale is fixed by the per-mode cross-coupling strength κ² \= A/Q already established in ZS-M6. No new physics, no tuning, no hierarchy problems — only the integration of two existing corpus structures into a single action-level object.

## **§2. Locked Inputs**

All inputs to ZS-S10 are LOCKED, PROVEN, or DERIVED in the prior corpus. The table below isolates the inputs used in this paper; a complete cross-reference is given in Appendix B.

### **2.1 Foundational Constants**

**Table 2.1.** Locked Z-Spin constants.

| Quantity | Value | Source | Status |
| :---- | :---- | :---- | :---- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 §7 | **LOCKED** |
| (Z, X, Y) sector dimensions | (2, 3, 6); Q \= Z+X+Y \= 11 | ZS-F5 v1.0 §4 | **PROVEN** |
| G \= MUB(Q) | Q+1 \= 12 | ZS-F5 v1.0 | **PROVEN** |
| κ² (per-mode cross-coupling) | A/Q \= 35/4807 ≈ 0.007281 | ZS-M6 Theorem 2.2.1 | **DERIVED** |
| δ\_X (X-sector asymmetry) | 5/19 | ZS-F2 v1.0 | **PROVEN** |
| δ\_Y (Y-sector asymmetry) | 7/23 | ZS-F2 v1.0 | **PROVEN** |
| λ\_vac (vacuum self-coupling) | 2A² \= 0.01283 | ZS-U5 v1.0 §15.4 | **DERIVED-CONDITIONAL** |
| m\_ρ (radial mode mass) | 2A·M\_P \= 0.1602 M\_P | ZS-F1 v1.0 §4.4 | **DERIVED** |
| M\_P (reduced Planck mass) | 2.435 × 10¹⁸ GeV | Standard | **STANDARD** |

### **2.2 ZS-F1 Base Action and U(1)\_Z Structure**

The Z-Spin base action in the Jordan frame \[ZS-F1 v1.0 §3.1 PROVEN\]:  
SF1=∫d4x−g12MP21+A2R−12MP22−V+Sm  
with V(Φ) \= (λ/4)M⁴\_P(|Φ|² − 1)² and Φ(x) \= ρ(x)·exp(iθ(x)) ∈ ℂ.  
The U(1)\_Z gauge symmetry \[ZS-F1 v1.0 §3.2 PROVEN, direct quotation\]: "The action is invariant under Φ → exp(iα)Φ for constant α ∈ \[0, 2π)." The compact domain α ∈ \[0, 2π) is structurally essential (ZS-U9 §3.1): the Z-bias field Φ takes values in ℂ, the natural U(1) action is rotation by α modulo 2π, and the vacuum manifold M \= {|Φ| \= 1} ≅ S¹ has π\_1(S¹) \= ℤ (ZS-F1 §5.1, PROVEN).

### **2.3 Register-Total Normalization Theorem**

From ZS-M6 Theorem 2.2.1 \[DERIVED, 10-step chain C1-C10\]:  
2=AQ=354807 \[EXACT RATIONAL\]  
**Numerical uniqueness test** (ZS-M6 §2.2.2): Among candidates A/Q, A/(Q−Z) \= 35/3933, 3A/Q² \= 105/52877, and A alone, κ² \= A/Q is uniquely selected at 10⁻¹⁴% precision, with alternative candidates deviating by 1.03×10⁻², 3.48×10⁻², and 3.67×10⁻¹ respectively (226×, 765×, 8074× worse than A/Q).

### **2.4 L\_XY \= 0 Sector Independence**

The block-Laplacian X-Y block vanishes identically:  
LXY0 \[PROVEN, ZS-F1 v1.0 §9, ZS-S1 v1.0 §4, ZS-M6 §2.2\]  
This is enforced at three independent levels: (i) the algebraic identity \[su(2)\_X, su(2)\_Y\] \= 0 from the Lorentz algebra decomposition so(1,3) ⊗ ℂ ≅ su(2)\_A ⊕ su(2)\_B (ZS-M2 §2, PROVEN); (ii) the action-level absence of direct X-Y coupling terms in (1+A|Φ|²)R (ZS-F1 §9, PROVEN); (iii) the A\_5-equivariant Schur protection via the Adjoint Obstruction Theorem (ZS-F2 §4.2A, PROVEN). The Continuum Perturbative Protection Theorem (ZS-M6 §7A, PROVEN-PERTURBATIVE) extends L\_XY \= 0 to all orders in perturbation theory.

### **2.5 ZS-A7 Kraus Operator Structure**

The Z-mediated CPTP channel \[ZS-Q1 §3.3, PROVEN\] has exactly two Kraus operators:  
X=z{0,1}KzXKz, K0=P|4⟩, K1=P|6⟩  
where the Kraus index z runs over the Z-sector basis {|4⟩, |6⟩} of the Q \= 11 register (ZS-A4 Appendix A). By ZS-A7 Theorem 3.2-bis \[PROVEN\]:  
**Part 1 (Single-factor structure):** Kz=UZzz′Kz′0 with UZ=exp−iy/2.  
**Part 2 (Choi-state period):** C+2=C (bilinear, 2π-periodic).  
**Part 3 (Signed seam witness period):** useam+2=−useam, useam+4=+useam (linear in Kraus, 4π-periodic).  
**Part 4 (Uniqueness):** The signed seam witness is the unique linear-in-Kraus observable carrying the 4π signature.

### **2.6 ZS-A6 Cigar Vortex Profile**

The Jaffe-Taubes anchored vortex \[ZS-A6 §4.5.3, PROVEN; §4.5.6 DERIVED, 140/140 PASS\] on the Euclidean Schwarzschild near-horizon geometry satisfies the cigar vortex equation:  
f″+1f′−f2−\*ff2−1=0  
with f0=0 (Z-Anchor) and f1 (vacuum attractor). The Frobenius slope at the tip: ccigar=f′0=0.06605585 \[ZS-A6 §4.5.6.2\]. Wick-rotation match with the independent D1 EF-BVP: cEF=2rHccigar=0.93417 vs c1=0.93500 (0.089% agreement, ZS-A6 §4.5.6.4-5). **Existence and uniqueness** in the n \= 1 sector is guaranteed by Theorem C3 (Jaffe-Taubes 1980, cited ZS-A6 §4.5.3).

### **2.7 ZS-U9 Hypercharge Spectrum**

From ZS-U9 Theorem 6.1 \[DERIVED, conditional on G1, G2\]:  
**Table 2.2.** Standard Model hypercharge spectrum.

| Field | Y | Source |
| :---- | :---- | :---- |
| Q\_L (quark doublet) | \+1/6 | ZS-U9 Theorem 6.1 |
| u\_R | \+2/3 | ZS-U9 Theorem 6.1 |
| d\_R | −1/3 | ZS-U9 Theorem 6.1 |
| L\_L (lepton doublet) | −1/2 | ZS-U9 Theorem 6.1 |
| e\_R | −1 | ZS-U9 Theorem 6.1 |
| ν\_R | 0 | ZS-U9 Theorem 6.1 |
| H (Higgs) | \+1/2 | ZS-U9 Theorem T3 |

All five Standard Model anomaly cancellation conditions A1-A5 PASS automatically at integer precision (ZS-U9 §7).

### **2.8 ZS-M3 j \= 1/2 Uniqueness and SU(2) Sign Flip**

**Theorem 5.1 (ZS-M3, PROVEN):** Among all half-integer spins j, dim(Inv₄(j)) \= 2 \= Z if and only if j \= 1/2.  
**Lemma 10.1 (ZS-M3, PROVEN):** Dj−I=−12jI. For j \= 1/2: D1/2−I=−I (SU(2) double-cover sign flip).

### **2.9 Standard Model Gauge Couplings**

From ZS-S1 v1.0 \[PROVEN/DERIVED\]:  
s=QV+FY+0Z=1193=0.11828 (+0.31σ vs PDG 2024\)  
sin2W=4891x\*=0.23118 (-1.26σ vs PDG 2024\)  
where x\*=Rez\*=0.4383 (ZS-M1 v1.0). The hypercharge gauge coupling at low energy satisfies gY=e/cosW with e2=4EM; combined with ZS-M8 NLO c₄ \= 4/13 yielding 1/EM=137.0359 (1.07 ppm from CODATA 2022), this gives gY0.345 at low energy (running to matching scale is discussed in §3.4).  
---

## **§3. The ZS-S10 Master Action and Theorem S10.1**

### **3.1 Master Action**

**Definition 3.1 (ZS-S10 Master Action).** The Z-Spin action of ZS-F1, extended by promotion of the partial derivative to a gauge-covariant derivative coupling the Z-bias field Φ to the Standard Model hypercharge gauge field B\_μ, is:  
SS10=∫d4x−g12MP21+A2R−12MP2D2−V−14BB+Smg,,B  
where:  
D=−igYB, =A/Q=35/4807  
B=B−B  
V=/4MP42−12 \[unchanged from ZS-F1\]  
and Smg,,B is the standard Standard Model matter action with fermion hypercharge couplings ‾f i−igYYfBf using the ZS-U9 Trinity Braiding hypercharges Y\_f of Table 2.2.  
**Minimal Extension Principle.** The master action differs from the ZS-F1 action only in the replacement 2D2 and the addition of the standard U(1)\_Y gauge kinetic term −14BB (which already appears in Sm implicitly as the U(1)\_Y sector of the Standard Model). No new fields beyond those already in ZS-F1 \+ Standard Model are introduced. No new parameters beyond A \= 35/437 (LOCKED) are introduced: κ is determined from A and Q via ZS-M6 Theorem 2.2.1 (DERIVED), and g\_Y is the standard SM hypercharge coupling.

### **3.2 Theorem S10.1: Stückelberg Mixing Scale**

**Theorem S10.1 (Stückelberg Mixing Scale, DERIVED-CONDITIONAL).** The effective Stückelberg mixing scale f in the ZS-S10 master action satisfies:  
f2=2MP2=AQMP2=354807MP2  
Numerically: f=0.08533MP=2.0781017 GeV.  
**Proof.**  
*Step 1 (Expansion of |D\_μΦ|²).* Writing Φ \= ρ·exp(iθ), the gauge-covariant kinetic term expands as:  
D2=2+2−gYB−gYB  
At the vacuum attractor ρ \= 1 \[ZS-F1 §4.2 DERIVED\]:  
D2|=1=−gYB−gYB  
Multiplying by the kinetic prefactor −12MP2:  
Lkin, gauge|=1=−12MP2−gYB2  
\=−12MP22+MP2gYB−12MP22gY2BB  
*Step 2 (Identification of Stückelberg mass).* The last term provides the Stückelberg mass for B\_μ:  
mB2=MP22gY2=AQgY2MP2  
Reading this against the canonical Stückelberg Lagrangian −12f2−gYB2 at effective charge q \= 1 identifies:  
f2=2MP2=AQMP2   
*Step 3 (Register-Total Normalization theorem basis).* The mixing scale f² \= (A/Q)M²\_P is determined by the per-mode cross-coupling strength κ² \= A/Q established in ZS-M6 Theorem 2.2.1 via the 10-step derivation chain C1-C10 (ZS-F1 non-minimal coupling → Regge discretization → Mode-Count Collapse → Gilkey heat kernel factorization → Spectral asymmetry → Product structure → Register-Total Normalization → Peter-Weyl/Schur orthogonality → rank-1 β₀-selected structure → Dimensional Coupling Norm). Each step is independently PROVEN, STANDARD, or LOCKED.  
**Numerical uniqueness** (inherited from ZS-M6 §2.2.2): Among the natural candidates for κ², A/Q \= 35/4807 is uniquely selected at 10⁻¹⁴% precision. Alternative candidates (A/(Q−Z), 3A/Q², A alone) deviate by 226×, 765×, and 8074× respectively.  
**\[STATUS: DERIVED-CONDITIONAL\]** Conditional on ZS-M6 Theorem 2.2.1 caveats R-1, R-2, R-3 (absolute 1-loop normalization from continuum action; register-scalar assumption; rank-1 from action level). These caveats do not affect the numerical content and are fully inherited from ZS-M6.

### **3.3 Physical Interpretation**

The mixing scale f ≈ 2.08 × 10¹⁷ GeV sits at approximately 0.085 M\_P, well above any Standard Model energy scale and below the Planck scale. This places f near the GUT unification scale. Combined with the lepton hypercharge Y\_L \= −1/2 (ZS-U9 Theorem 6.1), the Stückelberg mass of the B\_μ gauge boson as felt by the lepton doublet is:  
mBL=gYYLf0.3450.52.081017 GeV3.581016 GeV  
This is safely above all direct laboratory probes and below the Planck cutoff, providing a natural hierarchy compatible with the existing Z-Spin scale structure (ZS-S4 ε-Higgs portal coupling effA2/1624.110−5).

### **3.4 Infrared Compatibility**

The IR behavior of the master action must be compatible with the low-energy Standard Model. The photon, as a linear combination \=cosWB+sinWW3, remains massless after electroweak symmetry breaking (ZS-U9 NC-U9.7: photon masslessness is taken as experimental input). The GUT-scale Stückelberg mass of B\_μ decouples from IR physics at scales rCBmB−110−33 m (see §5.3).  
The hypercharge coupling gY0.345 used in the Stückelberg mass estimate above is the low-energy (M\_Z-scale) value. The running to the compactification scale m0.16MP or higher is governed by the Standard Model U(1)\_Y β-function (ZS-U9 NC-U9.3: ZS-U9 does not derive the SU(5) GUT unification scale or the GUT coupling). A complete RG analysis from M\_Z to the Stückelberg scale is outside the scope of this paper; the Stückelberg mass estimate here is an order-of-magnitude statement that establishes the GUT-scale hierarchy without claiming precision on f's numerical realization at the electroweak scale.  
**\[STATUS: CONSISTENT\]** Stückelberg mass at GUT scale; Standard Model IR behavior preserved.

## **§4. Theorem S10.2: L\_XY \= 0 Preservation**

The ZS-M6 §7A Continuum Perturbative Protection Theorem \[PROVEN-PERTURBATIVE\] establishes that LXYeff, direct=0 to all orders in perturbation theory for the ZS-F1 action. This section extends the theorem to the ZS-S10 extended action.

### **4.1 Statement**

**Theorem S10.2 (L\_XY \= 0 Preservation, PROVEN-PERTURBATIVE).** In the ZS-S10 master action (Definition 3.1), no direct X-sector to Y-sector coupling vertex is generated at any order in perturbation theory:  
LXYeff, direct|ZS-S10=0 to all orders in perturbation theory.  
All X↔Y communication proceeds through the Z-mediator with strength O2=OA/Q0.007, with higher-loop suppression A/42n.

### **4.2 Proof (Five Steps)**

The proof extends the four-step structure of ZS-M6 §7A by adding an independent fifth step from ZS-F2 §4.2A (Schur Protection).  
**Step 1 (Lorentz Algebra Decomposition — UNCHANGED).**  
From ZS-M2 §2 \[PROVEN\]: so1,3C≅su2Asu2B with su2A,su2B=0. The Z-Spin sector assignment X ↔ su(2)\_A (dim 3), Y ↔ su(2)\_B (dim 6\) inherits this exact commutativity (ZS-F5, PROVEN).  
The new terms in the ZS-S10 action are: (a) the gauge-covariant kinetic term −12MP2D2, which is a Z-sector scalar kinetic term with Lorentz-vector gauge coupling, and (b) the standard U(1)\_Y gauge kinetic term −14BB. The gauge field B\_μ is a Lorentz 4-vector — a (1/2, 1/2) representation in the (A, B) decomposition — and as an internal U(1)\_Y gauge field it is electroweak-sector content, orthogonal to the X, Y, Z polyhedral-sector decomposition.  
**Therefore** the algebraic identity su2A,su2B=0 is **PRESERVED** under the ZS-S10 extension.   
**Step 2 (Action-Level Absence — EXTENDED).**  
The ZS-F1 action contains no direct X-Y coupling (ZS-F1 §9, ZS-S1 §4, PROVEN). We verify that the three new ZS-S10 terms preserve this property.  
*(a)* −14BB*:* Pure U(1)\_Y gauge kinetic term. This does not couple X-sector to Y-sector degrees of freedom; B\_μ is an internal gauge field independent of the (X, Y, Z) polyhedral sector decomposition.  
*(b)* −12MP2gY22Yf2BB *(Stückelberg mass for B\_μ from Step 1 of Theorem S10.1 proof):* Pure gauge sector self-coupling, no X-Y direct coupling.  
*(c)* MP2gYB *(mixing term between θ and B\_μ):* This is a Z-sector ↔ gauge-sector coupling ( is the Z-sector Goldstone mode, B is the internal gauge field). It is not an X-Y direct coupling.  
**Matter-sector fermion couplings:** Fermion coupling to B\_μ in Sm takes the standard form gYYfB‾ff, where Y\_f is the individual fermion hypercharge. No fermion bilinear of the form ‾XY (X-sector fermion to Y-sector fermion direct coupling) is introduced.  
**Therefore** no term in the ZS-S10 action directly couples X-sector to Y-sector degrees of freedom without Z-sector mediation.   
**Step 3 (Ward-Takahashi Identity — EXTENDED).**  
Let QAa (a \= 1,2,3) be the conserved charges of su(2)\_A (X-sector). In any Lorentz-invariant quantum field theory, the Ward-Takahashi identity gives:  
⟨T{JA,axOBy1OByn}⟩connected=0  
where OB are operators transforming purely under su(2)\_B (Y-sector).  
In the ZS-S10 extended action, the new Feynman diagram vertices are: gYYfB‾ff (fermion-B coupling), MP2gYB (θ-B mixing), and MP22gY2BB (B self-mass). Any n-loop diagram with external legs attached only to pure X-sector and pure Y-sector operators, and containing no Z-sector propagator, must route through either the B\_μ propagator or through Z-sector vertices.  
The critical observation: **the θ-B mixing vertex** MP2gYB **carries coefficient** \=A/Q — the Z-sector per-mode coupling strength established by ZS-M6 Theorem 2.2.1. Therefore any path that connects X to Y through B\_μ must insert at least one factor of κ (through the θ-B mixing vertex when θ is coupled at internal lines), making the contribution O2 minimum at tree level and higher-order suppressed at loops.  
**Equivalently**, fermion-B-fermion chains: the fermion-B vertex gYYfB‾ff couples X-sector and Y-sector fermions to a common internal B\_μ, but this coupling channel is precisely the Z-mediated indirect channel (via the Stückelberg-screened B\_μ propagator at scales below m\_B). In the effective theory below m\_B, the B\_μ mediation is integrated out and contributes at O2 to effective X-Y transitions, exactly as before.  
**Therefore** the Ward-Takahashi identity is preserved; only Z-mediated indirect coupling of magnitude O2 is permitted.   
**Step 4 (Anomaly-Free Verification — EXTENDED).**  
The original anomaly-free verification of ZS-M6 §7A Step 4 covers (4a) scalar Φ has no chirality, (4b) SM ABJ anomalies act on gauge sector only, (4c) no mixed su2Asu2B anomaly.  
Four additional considerations for ZS-S10:  
*(4d) Stückelberg chiral anomaly:* The U(1)\_Y Stückelberg coupling could potentially generate chiral anomalies. However, ZS-U9 §7 \[PROVEN at integer precision\] establishes that all five Standard Model anomaly cancellation conditions A1-A5 PASS for the Trinity Braiding hypercharges:  
A1:SU32U1Y:quarks2YQ−Yu−Yd=0✓  
A2:SU22U1Y:3YQ+YL=0✓  
A3:U1Y3:f2Yf3=0✓  
A4:gravity2U1Y:fYf=0✓  
A5:SU24 (Witten):integer multiple of 2✓  
Since the Z-bias field Φ is a scalar (spin 0, no chirality), it contributes zero to all five triangle-type or global anomalies regardless of its U(1)\_Y charge q\_Φ \= \+1 (Theorem S10.4). The Trinity Braiding anomaly cancellation is preserved.  
*(4e) Stückelberg gauge invariance:* Under BB+, \+gY, the mixing combination −gYB is invariant. This gauge symmetry acts only on the internal U(1)\_Y sector and does not affect the Lorentz decomposition or the X,Y,Z polyhedral sectors.  
*(4f) Mixed Lorentz × U(1)\_Y anomaly:* Since the gravitational-U(1)\_Y triangle anomaly fYf=0 (ZS-U9 condition A4), both su2AU1Y and su2BU1Y mixed anomalies cancel individually.  
*(4g) Φ's contribution to U(1)\_Y triangle anomalies:* As a scalar field, Φ does not contribute to any triangle anomaly (fermion-loop triangle anomalies require chiral fermions). Therefore its U(1)\_Y charge q=+1 does not enter any anomaly condition.  
**Therefore** the Ward identity of Step 3 is anomaly-free in the ZS-S10 extended action.   
**Step 5 (Schur Protection Independent Layer — PRESERVED).**  
From ZS-F2 §4.2A (Adjoint Obstruction Theorem, PROVEN): A5 is the unique finite subgroup of SO(3) for which adjSU3|=35 lacks the irrep 3′. By Schur's Lemma, no A5-equivariant intertwiner exists between the irreps 3 (3C5=) and 3′ (3′C5=1−), where \=1+5/2 is the golden ratio.  
This discrete representation-theoretic protection acts on the SM gauge sector (SU(3)\_C × SU(2)\_L) assignment to I-irreps, which is orthogonal to the U(1)\_Y Stückelberg extension introduced in ZS-S10. The Adjoint Obstruction Theorem is therefore unaffected by ZS-S10. 

### **4.3 Conclusion and Scope**

Combining Steps 1-5: LXYeff, direct=0 to all orders in perturbation theory in the ZS-S10 action.   
**Scope and Limitations.** This theorem covers:

* All perturbative orders in Lorentz-invariant regularization  
* The weak-curvature regime (RMP2)

It does not cover:

* Non-perturbative effects (instantons are expected to be single-sector objects per ZS-M2 §6.1, but a rigorous proof is absent)  
* Strong-curvature regime (RMP2) where the perturbative expansion breaks down (ZS-A3 §7 Sector Duality is HYPOTHESIS)

**\[STATUS: PROVEN-PERTURBATIVE\]** Inherited from ZS-M6 §7A with ZS-S10 extensions verified in Steps 2, 3, 4 and independent Schur layer Step 5\.  
---

## **§5. Theorem S10.3: Stückelberg-Corollary IV Bridge**

This section establishes that the ZS-S10 master action realizes both branches of ZS-A7 Corollary IV (Vortex Bose/Fermi Duality) — the inner (F) j=1/2 spinor branch and the outer (B) 2π Goldstone winding branch — as two limits of a single action-level object.

### **5.1 Statement**

**Theorem S10.3 (Stückelberg-Corollary IV Bridge, DERIVED).** The ZS-S10 master action simultaneously realizes:  
**(i) UV limit (vortex core, r ∼ ℓ\_P):** The Z-Anchor boundary condition x0=0 (ZS-F1 §5.2 PROVEN, ZS-A6 §4.5.6 cigar bounce DERIVED) together with the gauge-covariant derivative D realizes the **Corollary IV (F) branch**: a j \= 1/2 spinor carrier with 4π closure period. Explicit action-level proof: Theorem S10.5-BPS (§7).  
**(ii) IR limit (galactic scale, r ≫ λ\_C(B) \~ m\_B⁻¹):** Exponential Stückelberg screening of the B\_μ gauge boson (e−mBr) reduces the gauge-covariant derivative D=−gYB, and the Goldstone mode satisfies □=0 with integer winding Cd=2n (π\_1(U(1)) \= ℤ, PROVEN). This realizes the **Corollary IV (B) branch**.  
**(iii) Common boundary condition:** Both limits share the Z-Anchor boundary condition x0=0 at the vortex core (ZS-F1 §5.2, PROVEN with horizon realization DERIVED via ZS-A6 §4.5.6).

### **5.2 B\_μ \= 0 Limit: ZS-F1 Recovery**

Setting B0 in the ZS-S10 master action gives:  
SS10|B=0=∫d4x−g12MP21+A2R−12MP22−V+Sm|B=0  
\=SF1  
exactly. All ZS-F1 equations of motion, vortex solutions, Goldstone halo dynamics, and inflationary background cosmology are recovered identically. This is the **kinematic backward compatibility** statement: ZS-S10 contains ZS-F1 as a gauge-fixed limit (B=0 corresponds to a specific choice of U(1)\_Y gauge).

### **5.3 Galactic Scale: ZS-A1 78/78 PASS Preservation**

At galactic scales, the Stückelberg mass of B\_μ is mB=gYMP0.029MP7.11016 GeV (Theorem S10.1), yielding Compton wavelength:  
CB=/mBc1/7.11016 GeV2.810−33 m  
For galactic scales r10 kpc \=3.091020 m:  
rCB3.0910202.810−331053  
The B\_μ field is exponentially screened at galactic scales: Be−mBr0 with suppression factor e−1053, which is effectively zero at any physical precision. The gauge-covariant derivative reduces to:  
D|rCB=−gYB  
**Consequence:** The Goldstone equation of motion □=0 (ZS-A1 §2.1 DERIVED) is preserved at galactic scales. The logarithmic profile r=lnr/rs/L and isothermal halo density \=MP2/2L2r2 (ZS-A1 §2.2 DERIVED) are **unchanged**. All 78 ZS-A1 verification tests PASS at full precision.  
**\[STATUS: DERIVED\]** Galactic-scale Goldstone physics preserved at precision of Oe−1053, i.e., absolutely.

### **5.4 Inflation: ZS-U1 r \= 0.0089 Preservation**

At inflationary scales, 1 (ZS-U1 §4, DERIVED). The inflaton is identified as the radial mode \=, and the angular mode  is frozen at the Hubble scale (Lyth-Riotto 1999, isocurvature suppression). In this regime:  
D=−igYB ei  
with 0\. The inflationary Lagrangian density includes:  
−12MP2D2|inflation−12MP22−12MP222gY2BB  
The Stückelberg mass correction to the inflaton potential is V22gY2MP2B2, which vanishes for B0 in the inflationary vacuum. The slow-roll parameters V, V computed from V(Φ) \= (λ/4)M⁴\_P(|Φ|²−1)² (ZS-U1 §4.2 DERIVED) are **unchanged**.  
**Consequence:** Tensor-to-scalar ratio r=0.0089 (ZS-U1 prediction, DERIVED) is preserved. Spectral tilt ns is unchanged. CMB scalar amplitude As=2.110−9 (Planck 2018 input) is unchanged.  
**\[STATUS: DERIVED\]** Inflation observables preserved through direct inspection of the Lagrangian structure in the 1 regime.

### **5.5 Vortex Core: Corollary IV (F) Realization**

At the vortex core (Region I of ZS-F1 §5.3, rℓP), 0 by Z-Anchor (ZS-F1 §5.2 PROVEN, ZS-A6 §4.5.6 cigar bounce realization DERIVED at 0.089% Wick-rotation match precision).  
The gauge-covariant kinetic term at the vortex core:  
D2|0=2+2−gYB22+O2  
The gauge coupling through the θ-mode vanishes as 0, but the **phase structure remains non-trivial** through the topological winding number n around the vortex. Specifically, the fluctuation Φ ≈ c\_1(x \+ iy) near the core (Step 2 of Theorem S10.5-BPS proof in §7.3) realizes the j \= 1/2 spinor structure of ZS-M3 Theorem 5.1.  
**Consequence:** ZS-A7 Corollary IV (F) branch — the j \= 1/2 spinor at the vortex core — is realized at the action level through the ZS-S10 master action. Explicit proof with Kraus-operator 4π closure: Theorem S10.5-BPS (§7).

### **5.6 Galactic Halo: Corollary IV (B) Realization**

At galactic scales (Region II of ZS-F1 §5.3, rsrrZ), 1 (radial mode frozen by mMP) and only the Goldstone θ varies. With B\_μ exponentially screened (§5.3), the winding integral:  
CD dx=C−gYB dxC dx=2n  
where the last equality uses 1U1=Z (ZS-A6 §4.4.2, PROVEN) and the Stückelberg screening of B\_μ at galactic scales (§5.3).  
**Consequence:** ZS-A7 Corollary IV (B) branch — the 2π Goldstone winding — is realized at the action level in the IR limit of the ZS-S10 master action.

### **5.7 Summary of Corollary IV Action-Level Realization**

**Table 5.1.** Mapping of ZS-S10 regimes onto Corollary IV branches.

| Regime | Radius scale | Field configuration | Corollary IV branch | Observable |
| :---- | :---- | :---- | :---- | :---- |
| UV (core) | r ∼ ξ ∼ ℓ\_P | 0, Frobenius fc1 | (F) j=1/2 spinor, 4π closure | useam=cos/2 |
| Intermediate | r ∼ λ\_C(B) ∼ 10⁻³³ m | 1, B\_μ transitioning | Crossover (neither pure F nor pure B) | n/a |
| IR (galactic) | r ≫ λ\_C(B) | 1, B\_μ screened | (B) 2π Goldstone winding | ∮d=2n |

The two branches coexist on the same vortex line, sharing the common boundary condition x0=0. This is the exact content of ZS-A7 Corollary IV (§4.4.2), now realized at the action level.  
**\[STATUS: DERIVED\]** Theorem S10.3 established from existing PROVEN/DERIVED inputs: ZS-F1 §3.1 (action), ZS-F1 §5.2 (Z-Anchor), ZS-M6 Thm 2.2.1 (κ² \= A/Q), ZS-A6 §4.5.6 (cigar bounce), ZS-A7 §4.4 (Corollary IV), ZS-A1 §2 (Goldstone halo), ZS-U1 §4 (inflation). Zero new parameters.

## **§6. Theorem S10.4: Φ Field U(1)\_Y Charge**

This section establishes the U(1)\_Y charge of the Z-bias field Φ through four independent constraints, three of which are independent of ZS-S10 itself, thereby removing the apparent circularity of the Gap G1 self-closure.

### **6.1 Statement**

**Theorem S10.4 (Φ Field U(1)\_Y Charge, DERIVED).** The U(1)\_Y charge of the Z-bias field Φ in the ZS-S10 master action is uniquely fixed to:  
q=+1

### **6.2 The Four Independent Paths**

The theorem is established through four independent constraints, the first three of which are independent of the ZS-S10 definition.  
**Path I — ZS-F1 §3.2 Fundamental Convention \[PROVEN, corpus-LOCKED\].**  
By the explicit statement of ZS-F1 §3.2 \[PROVEN, direct quotation\]: "The action is invariant under Φ → exp(iα)Φ for constant α ∈ \[0, 2π)."  
This statement **definitionally** establishes Φ as a charge-(+1) character of U(1)\_Z. The gauge transformation parameter α enters with coefficient 1 in the exponent (not 2, 3, or −1), and this is a **corpus-LOCKED convention** of the ZS-F1 action. Any other choice of q^(Z)\_Φ would contradict the direct statement of ZS-F1 §3.2.  
cZ=+1 \[PROVEN by corpus definition\]  
**Path II — ZS-U9 Theorem 3.1 Integer Quantization \[PROVEN\].**  
By ZS-U9 Theorem 3.1 \[PROVEN\]: For any state ψ transforming as eic under U(1)\_Z with \[0,2), single-valuedness \+2= forces cZ.  
Combined with Path I, this gives cZ=+1Z uniquely and consistently.  
**Path III — Vortex Winding Number Observational Selection \[DERIVED\].**  
By ZS-A6 §4.4.1 \[DERIVED\] and §4.5.6 \[DERIVED, 2026-04 cigar bounce closure with 0.089% Wick-rotation match\], the quantitatively-verified Z-Anchor profile uses n=1 winding. The Frobenius exponent Frob=n/2=1/2 is confirmed numerically.  
While Path III does not by itself prove that internal U(1)\_Z charge cZ equals the spatial winding n (ZS-U9 §3.3 states only that "both external topological winding and internal representation charge respect integer quantization"), the **supporting evidence** converges on cZ=1 through the **minimal coupling ansatz** of ZS-S10: a gauge-covariant derivative D=−iqgYB with qcZ would require a compensating rescaling of the action, contradicting the LOCKED normalization of ZS-F1.  
**\[STATUS: Consistent with** cZ=1**; not an independent proof; serves as supporting evidence.\]**  
**Path IV — EFT Kinematic Bound \[CONSISTENT\].**  
Under the ZS-S10 master action, the Stückelberg mass of B\_μ coupled to Φ with charge q is mB=qgYMP. The requirement that the Stückelberg mass remains below the Planck cutoff (mBMP) for EFT validity gives:  
q1gY10.08530.34534  
Combined with the integer quantization of Path II, this gives 1q34, consistent with q=+1 but not uniquely selecting it. An additional kinematic constraint — the Z-Spin register cap Q=11 — narrows this to 1q11, still consistent with q=+1.

### **6.3 Complete Proof**

**Step 1 \[PROVEN, corpus-LOCKED\]:** Path I establishes cZ=+1 by the ZS-F1 §3.2 definitional convention. This is **independent of ZS-S10**.  
**Step 2 \[PROVEN\]:** Path II confirms integer-quantization consistency.  
**Step 3 \[DERIVED, observational\]:** Path III provides supporting evidence from n=1 vortex profile.  
**Step 4 \[DERIVED by Gap G1 closure\]:** Under the ZS-S10 Stückelberg minimal coupling D=−iqgYB, the U(1)\_Z charge of Φ transfers to its U(1)\_Y charge: qY=cZ=+1. This identification is the **definitional statement of Gap G1 closure**, not a circular derivation.  
**Step 5 \[PROVEN, ZS-U9 §7\]:** Anomaly cancellation A1-A5 are preserved unchanged, since the Z-bias field Φ is a scalar (no chiral contribution to triangle anomalies) for any integer q.  
**Therefore** q=+1 is uniquely fixed by Paths I-II (corpus-LOCKED and PROVEN), supported by Path III (observational), bounded by Path IV (EFT consistency), and identified with qY via Step 4 (definitional Gap G1 closure). 

### **6.4 Circularity Resolution**

The apparent circularity of the original Theorem S10.4 — "Gap G1 closure is used to derive q\_Φ, but Gap G1 closure is itself defined by ZS-S10" — is **resolved** as follows:

* **Paths I, II are independent of ZS-S10**: they fix cZ=+1 from the ZS-F1 §3.2 corpus-LOCKED convention and ZS-U9 Theorem 3.1 PROVEN integer quantization.  
* **Path III provides observational support independent of ZS-S10**: the n=1 vortex profile is already established in ZS-A6 at 0.089% precision.  
* **Path IV is a kinematic consistency check**: the EFT validity range 1qQ=11 is consistent with q=+1.  
* **Step 4 (U(1)\_Z → U(1)\_Y)** is the **definitional statement** of ZS-S10's minimal coupling, not a derived identity subject to circular reasoning. The identification is precisely what ZS-S10 provides at the action level as the closure of Gap G1.

This is the same self-consistent bootstrapping pattern as the Trinity Braiding Theorem (ZS-U9 §6), where each ingredient's individual gap is closed by another ingredient's capability. In ZS-S10's case, cZ is determined externally (Path I-III), and the ZS-S10 action then identifies this externally-determined charge with the U(1)\_Y charge by definition.  
**\[STATUS: DERIVED\]** (upgraded from DERIVED-CONDITIONAL in the preliminary version). The circularity is resolved because Paths I-III fix cZ=+1 outside ZS-S10, and the U(1)\_Z ↔ U(1)\_Y identification is definitional rather than derivational.

### **6.5 Consequences for Stückelberg Mass Spectrum**

With q=+1:  
mB=qgYMP=1A/QgYMP  
Numerically: mB0.08530.3452.4351018 GeV 7.11016 GeV.  
For lepton doublet (Y\_L \= −1/2), the fermion-sector Stückelberg mass (contribution to effective gauge-fermion coupling mass scale):  
mBL=gYYLf=0.3450.52.0781017=3.581016 GeV  
For electron (Y\_e \= −1):  
mBe=gYYef=0.34512.0781017=7.171016 GeV  
These are GUT-scale masses, safely above all laboratory probes.  
---

## **§7. Theorem S10.5-BPS: Bogomolnyi BPS Spinor Lift**

This section provides the seven-step explicit action-level proof that the ZS-A7 Theorem 3.2-bis Kraus-operator 4π closure emerges naturally from the action content of ZS-S10 at the Z-anchored vortex core.

### **7.1 Statement**

**Theorem S10.5-BPS (Bogomolnyi BPS Spinor Lift, DERIVED).** Under the ZS-S10 master action (Definition 3.1) with a Z-anchored vortex solution ,=fein satisfying the cigar vortex equation (ZS-A6 §4.5.6, DERIVED):  
**(i)** The vortex solution with n=1 and boundary conditions f0=0, f=1 exists uniquely (Jaffe-Taubes 1980, PROVEN).  
**(ii)** Near the vortex core 0, linearization gives c1x+iy, identifying the Z-sector 2-dimensional real subspace \=Re ,Im TR2.  
**(iii)** The complex structure J:R2R2 satisfies J=−iy, where y is the Pauli y-matrix.  
**(iv)** Under U(1)\_Z gauge rotation ei, the vector  transforms by R=exp−iy (vector / j \= 1 rep).  
**(v)** The Kraus operators {K0,K1} in the Z-mediated CPTP channel transform by half-angle: UZ=exp−iy/2 (spinor / j \= 1/2 rep).  
**(vi)** By ZS-M3 Lemma 10.1 (D1/2−I=−I): Kz+2=−Kz, Kz+4=+Kz.  
**(vii)** By ZS-M3 Theorem 5.1 (j \= 1/2 uniqueness on dim \= 2 intertwiner), this spinor realization is unique.

### **7.2 Step 1: Vortex Existence**

By Jaffe-Taubes (1980) and ZS-A6 §4.5.3 \[PROVEN, Theorem C3\], the cigar vortex equation on the near-horizon cigar metric:  
f″+1f′−f2−\*ff2−1=0  
with \*=2A2=0.01283 \[ZS-U5 §15.4 DERIVED-CONDITIONAL\], has a **unique smooth solution** in the n=1 winding sector with boundary conditions f0=0 (Z-Anchor) and f=1 (vacuum). Existence is proven via the direct variational method; uniqueness in the n=1 sector is proven via the Weinberg-Salam convexity argument (Jaffe-Taubes Theorem C3).  
Numerical realization (ZS-A6 §4.5.6.2): ccigar=f′0=0.06605585, verified via scipy.solve\_bvp at rms residual 7.3110−11 across 1632 mesh nodes. 

### **7.3 Step 2: Linear Core Behavior**

Near the vortex core 0, the Frobenius expansion of the cigar vortex equation yields:  
f=c1+c33+O5  
with c10.06606 (cigar coordinates) or equivalently c10.935 in EF-BVP coordinates (0.089% Wick-rotation match, ZS-A6 §4.5.6.4). Substituting into the vortex ansatz \=fein with n=1:  
0=c1cos+isin=c1cos+ic1sin=c1x+iy  
using x=cos and y=sin.  
**Thus** the Z-bias field Φ linearizes to c1x+iy at the vortex core, a complex-linear function of spatial coordinates. Decomposing into real and imaginary parts:  
x,yRe  Im  \=c1x y R2  
This 2-dimensional real vector space is the Z-sector carrier (ZS-F1 §2.3 DERIVED: dim(Z) \= 2 identifies Z-sector state space with ℂ). 

### **7.4 Step 3: Complex Structure → Pauli Matrix**

The isomorphism C≅R2 via z=x+iyx,yT equips R2 with a natural complex structure: multiplication by i on C corresponds to 90° rotation on R2:  
ix+iy=−y+ix−y x \=Jx y , J=0 −1 1 0   
Direct comparison with the Pauli y-matrix y:  
y=0 −i i 0 , −iy=0 −1 1 0 \=J  
**Therefore** J=−iy, an algebraic identity relating the complex structure of C≅R2 to the Pauli y-matrix of SU(2). The su2 algebra action on the Z-sector state space is naturally realized through y. ▫3

### **7.5 Step 4: Vector Rotation (j \= 1 representation)**

Under U(1)\_Z gauge rotation ei, the complex field transforms as:  
eix+iy=cos+isinx+iy=xcos−ysin+ixsin+ycos  
In the real vector representation:  
R=cos −sin sin cos   
The matrix R is the matrix exponential of J:  
R=expJ=cosI+sinJ=cosI−isiny=exp−iy  
This is the **j \= 1 (vector) representation** of SU(2) on the 2-dimensional real space (equivalent to the spin-1 spherical tensor rep restricted to the plane). R+2=R, so the vector rep is 2π-periodic. 

### **7.6 Step 5: Kraus Square Root (j \= 1/2 representation)**

From ZS-Q1 §3.3 \[PROVEN\], the Z-mediated CPTP channel admits a Kraus decomposition X=zKzXKz with Kraus count \= dim(Z) \= 2 (ZS-A4 Appendix A). The Kraus operators are **wave-function-linear objects** (not density-matrix-bilinear), as emphasized by ZS-A7 Theorem 3.2-bis §3.2-bis.3.  
**Key quantum-mechanical principle:** For a CPTP channel  with Choi state C=zKz⟩⟩⟨⟨Kz transforming under a U(1) gauge rotation by R=exp−iy at the **bilinear** level, the Kraus operators themselves transform at the **linear** level via the square root:  
Kz=Rzz′Kz′0=exp−iy/2zz′Kz′0  
Setting UZ=exp−iy/2, this is the **j \= 1/2 (spinor) representation** of SU(2).  
**Consistency with Choi state 2π periodicity** \[ZS-A7 Theorem 3.2-bis Part 2\]: The Choi state C=zKzKz\*=zUZK0UZK0\* is unitarily-invariant under UZ (bilinear structure), hence 2π-periodic (the full U(1) rotation leaves it invariant). This matches ZS-A7 Theorem 3.2-bis Part 2 exactly. 

### **7.7 Step 6: 4π Closure (ZS-M3 Lemma 10.1)**

By direct Pauli-matrix algebra:  
exp−iy=cosI−isiny=−I  
(standard SU(2) center element, equivalent to ZS-M3 Lemma 10.1: D1/2−I=−I, PROVEN).  
Therefore:  
UZ+2=exp−i+2y/2=exp−iy/2exp−iy=UZ−I=−UZ  
Applied to Kraus operators:  
Kz+2=−Kz, Kz+4=−12Kz=+Kz  
This is the **4π closure at the Kraus-operator level**, matching ZS-A7 Theorem 3.2-bis Part 3 exactly. 

### **7.8 Step 7: Uniqueness (ZS-M3 Theorem 5.1)**

By ZS-M3 Theorem 5.1 \[PROVEN\]: among all half-integer spins j, dimInv4j=2 if and only if j=1/2.  
The Z-sector has dim \= 2 (ZS-F5, PROVEN), so only j \= 1/2 is a viable representation. No alternative spin representation (j \= 1, 3/2, 5/2, ...) is possible for dim(Z) \= 2\.  
**Therefore** the j \= 1/2 spinor realization at the vortex core is **unique** — the only possible representation compatible with the Z-sector dimension. 

### **7.9 Observable Realization: Signed Seam Witness**

The signed seam witness useam of ZS-A7 Theorem 3.2-bis Part 3 has an explicit form in terms of the spinor rotation UZ. With orthonormal Kraus basis TrKzKz′=zz′K00F2 (standard Kraus normalization, ZS-Q1 §3.3):  
useam=Re TrK00K0K00F2  
Computing K0=UZ00K00+UZ01K10:  
UZ=cos/2 −sin/2 sin/2 cos/2   
Therefore:  
useam=Re cos/21−sin/20=cos/2  
**Explicit 4π periodicity verification:**

| α | α/2 | useam=cos/2 |
| :---: | :---: | :---: |
| 0 | 0 | \+1 |
| π | π/2 | 0 |
| 2π | π | −1 (sign flip) |
| 3π | 3π/2 | 0 |
| 4π | 2π | \+1 (return to identity) |

useam+2=cos/2+=−cos/2=−useam✓  
useam+4=cos/2+2=+cos/2=+useam✓

### **7.10 Theorem Conclusion**

All 7 steps follow from PROVEN/DERIVED corpus inputs:

* Step 1: Jaffe-Taubes 1980 \+ ZS-A6 §4.5.3 Theorem C3 (PROVEN)  
* Step 2: ZS-A6 §4.5.6 Frobenius expansion (DERIVED, verified at 0.089%)  
* Step 3: J=−iy (algebraic identity, PROVEN)  
* Step 4: Matrix exponential \+ trigonometry (PROVEN)  
* Step 5: Quantum-mechanical amplitude-wavefunction relation \+ ZS-A7 Theorem 3.2-bis (PROVEN)  
* Step 6: ZS-M3 Lemma 10.1 (PROVEN) \+ Pauli algebra  
* Step 7: ZS-M3 Theorem 5.1 (PROVEN, uniqueness)

**Zero new parameters, zero new fields, zero new postulates.**   
**\[STATUS: DERIVED\]** Action-level realization of ZS-A7 Corollary IV (F) branch with explicit observable useam=cos/2 matching F-A7.3 experimental prediction (TESTABLE on Z-Spin quantum hardware 2026-2028).

## **§8. Non-Claims**

Consistent with Z-Spin Collaboration methodology, we enumerate explicit non-claims for ZS-S10:  
**NC-S10.1.** ZS-S10 does NOT introduce a new gauge field beyond the Standard Model hypercharge gauge field B\_μ. The ZS-S10 master action identifies U(1)\_Z (of ZS-F1 §3.2) with U(1)\_Y (of the Standard Model) at the action level; no separate gauge field is postulated.  
**NC-S10.2.** ZS-S10 does NOT derive photon masslessness from first principles. The condition that the photon \=cosWB+sinWW3 remains massless after electroweak symmetry breaking is taken as experimental input (m\_γ \< 10⁻¹⁸ eV PDG 2024), identical to ZS-U9 NC-U9.7. The Stückelberg mechanism of ZS-S10 generates a GUT-scale Stückelberg mass for B\_μ itself, not for the physical photon after diagonalization.  
**NC-S10.3.** ZS-S10 does NOT modify any galactic-scale prediction of ZS-A1 (rotation curves, BTFR, M-σ relation, vortex glass profile). Stückelberg screening at galactic scales is exponential with suppression factor e−1053, preserving all 78 ZS-A1 verification tests at full precision. See §5.3.  
**NC-S10.4.** ZS-S10 does NOT modify any inflationary prediction of ZS-U1. The tensor-to-scalar ratio r=0.0089, spectral tilt ns, and CMB scalar amplitude As are all preserved unchanged in the 1 inflationary regime. See §5.4.  
**NC-S10.5.** ZS-S10 does NOT re-derive the Higgs VEV v=245.93 GeV (ZS-S4 §6.12 DERIVED), the Weinberg angle sin2W=48/91x\*=0.23118 (ZS-S1 §8.2 PROVEN), or the strong coupling s=11/93=0.11828 (ZS-S1 §8.1 DERIVED). These upstream results are preserved as input constraints.  
**NC-S10.6.** ZS-S10 does NOT close Gap G2 of the Trinity Braiding Theorem (ZS-M9 Table 2 assignment upgrade from HYPOTHESIS strong to PROVEN). While Theorem S10.2's anomaly preservation is consistent with the Table 2 assignments, a rigorous representation-theoretic proof that the Table 2 assignments are uniquely forced remains OPEN. See NC-U9.2.  
**NC-S10.7.** ZS-S10 does NOT introduce supersymmetry or any new symmetry beyond U(1)\_Y Stückelberg. The vortex Bose/Fermi duality of Corollary IV is a topological statement (j=1/2 SU(2) double-cover on Z-sector vs π\_1(U(1))=ℤ on vacuum manifold); no SUSY superpartner pairing is invoked (inherited from ZS-A7 NC-A7.8).  
**NC-S10.8.** ZS-S10 does NOT provide a dynamical selection mechanism for Qe=1 at the action level beyond the minimal-integer-charge argument of ZS-U9 Theorem 3.1. The selection q=+1 (Theorem S10.4) is the **Φ field's own U(1)\_Y charge**, not the electron's electric charge, which is instead derived through ZS-U9 Theorem T3 via the neutral-Higgs fixing (inherited from ZS-U9 NC-U9.4).  
**NC-S10.9.** ZS-S10 does NOT derive the SU(5) GUT unification scale or the GUT coupling. The Stückelberg mass scale mB71016 GeV is computed using the low-energy value gY0.345 at M\_Z; full RG running from M\_Z to the Planck scale is outside the present scope (inherited from ZS-U9 NC-U9.3).  
**NC-S10.10.** The 4π closure realization of Theorem S10.5-BPS is a statement about the **structure of the Z-mediated CPTP channel** in the ZS-S10 action, observable on Z-Spin quantum hardware via F-A7.3 (ZS-A7 TESTABLE). It is NOT an experimental claim about astrophysical BH horizons directly; the connection between hardware-testable ũ\_seam periodicity and astrophysical BH observables remains OS-A7.2 OPEN (inherited from ZS-A7).  
---

## **§9. Falsification Gates**

Five falsification gates are registered for ZS-S10:  
**F-S10.1 \[MATH, DECISIVE\].** If backward compatibility fails at any of the four verified regimes (B\_μ \= 0 recovery of ZS-F1, galactic screening of Stückelberg mass, inflation preservation of r \= 0.0089, vortex core realization of Cor IV (F)), ZS-S10 is falsified. Current status: PASS (4/4, §5.2-5.6).  
**F-S10.2 \[OBS, DECISIVE\].** If the ZS-A7 F-A7.3 experimental gate returns 2π periodicity in the signed seam witness useam (rather than the predicted 4π), ZS-S10 Theorem S10.5-BPS is falsified (as is ZS-A7 §3). Current status: OPEN, hardware-ready 2026-2028.  
**F-S10.3 \[OBS, DECISIVE\].** If any dark matter particle is detected at predicted mass/cross-section consistent with WIMP, axion, or sterile neutrino candidates \[ZS-A5 §8 F-A5.7\], the Corollary IV (B) Goldstone interpretation of the galactic halo is falsified, including ZS-S10 Theorem S10.3's IR limit. Current status: OPEN, inherited from ZS-A5.  
**F-S10.4 \[MATH, DECISIVE\].** If any of the five Standard Model anomaly cancellation conditions A1-A5 fails at integer precision in the ZS-S10 extended action, Theorem S10.2 Step 4 is falsified. Current status: PASS (5/5, ZS-U9 §7 preserved unchanged).  
**F-S10.5 \[OBS, MODIFICATION REQUIRED\].** If precision measurements of the photon mass exceed m\<10−18 eV (current PDG bound) in a way inconsistent with the Stückelberg mechanism (e.g., a fifth-force signature at laboratory scales), the ZS-S10 Stückelberg mass structure must be revised. Current status: OPEN but structurally consistent with all existing bounds.  
---

## **§10. Conclusion**

ZS-S10 closes Gap G1 of the Trinity Braiding Theorem (ZS-U9) at the action level through a minimal extension of the ZS-F1 action: the partial derivative of the Z-bias field Φ is promoted to a gauge-covariant derivative D=−igYB, with mixing scale \=A/Q uniquely determined by the Register-Total Normalization Theorem of ZS-M6. No new parameters, no new fields, no new postulates are introduced. The same minimal coupling simultaneously provides the action-level realization of ZS-A7 Corollary IV (Vortex Bose/Fermi Duality): the UV limit (vortex core) realizes the (F) branch with j \= 1/2 spinor 4π closure, while the IR limit (galactic scale) realizes the (B) branch with 2π Goldstone winding. Both limits share the common Z-Anchor boundary condition x0=0.  
Five theorems establish the mathematical content:  
**Theorem S10.1 (Stückelberg Mixing Scale, DERIVED-CONDITIONAL)**: f2=2MP2=A/QMP2=35/4807MP2, unique at 10⁻¹⁴% precision against alternative candidates.  
**Theorem S10.2 (L\_XY \= 0 Preservation, PROVEN-PERTURBATIVE)**: The sector independence of the ZS-F1 action is preserved to all orders in perturbation theory under the ZS-S10 extension, through a five-step proof combining Lorentz algebra decomposition, action-level absence, Ward-Takahashi identity, anomaly-free verification (including all five ZS-U9 SM anomaly conditions), and independent Schur protection.  
**Theorem S10.3 (Stückelberg-Cor IV Bridge, DERIVED)**: The UV (vortex core) and IR (galactic scale) limits of the ZS-S10 master action realize the (F) and (B) branches of ZS-A7 Corollary IV respectively, with explicit backward compatibility verified in four regimes (B\_μ \= 0 → ZS-F1; galactic → ZS-A1; inflation → ZS-U1; vortex core → Cor IV (F)).  
**Theorem S10.4 (Φ Field U(1)\_Y Charge, DERIVED)**: q=+1 uniquely fixed by four independent constraints (ZS-F1 §3.2 corpus-LOCKED convention; ZS-U9 Theorem 3.1 integer quantization; ZS-A6 n=1 vortex observational selection; EFT kinematic bound), with circularity resolved because Paths I-III are independent of ZS-S10 itself.  
**Theorem S10.5-BPS (Bogomolnyi BPS Spinor Lift, DERIVED)**: Seven-step explicit proof that the ZS-A7 Theorem 3.2-bis Kraus-operator 4π closure emerges naturally from the ZS-S10 action content at the vortex core, with observable realization useam=cos/2 matching F-A7.3 experimental prediction.  
Gap G1 is therefore CLOSED at the action level. Gap G2 (ZS-M9 Table 2 assignment upgrade) is advanced through the anomaly-preserving structure of Theorem S10.2 but remains OPEN as a separate closure problem. The Trinity Braiding Theorem status is advanced from DERIVED (conditional on G1, G2) toward DERIVED (conditional on G2 only), pending confirmation of Theorem S10.4's Path I interpretation of ZS-F1 §3.2 as a corpus-LOCKED charge-1 convention.  
The principal structural lesson is that **the integration of two previously independent corpus structures** — the compact U(1)\_Z of ZS-F1 and the Standard Model hypercharge U(1)\_Y — does not require new physics. A single minimal coupling D with mixing scale 2=A/Q (already established by ZS-M6) is sufficient. The five theorems of this paper converge on a single statement: U(1)\_Z and U(1)\_Y are the same gauge group, and the ZS-S10 master action is the minimal action-level object that makes this identification manifest.  
---

## **Acknowledgements**

This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, representation-theoretic computation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

## **Code Availability**

The companion verification suite zs\_s10\_verify\_v1\_0.py is self-contained and publicly available at github.com/KennyKang-git/zspin/verify\_scripts/. Execution: python3 zs\_s10\_verify\_v1\_0.py. Expected output: 36/36 PASS. Exit code: 0 (all pass) or 1 (any fail). Results are saved to zs\_s10\_v1\_0\_verification\_results.json. Dependencies: numpy, scipy, mpmath (required). The suite uses mpmath (80-digit working precision, 50-digit display) for exact rational arithmetic and algebraic identities; numpy for matrix exponentials and Pauli algebra. No external data files required.  
---

## **Appendix A. Verification Suite Summary**

**Target:** 36/36 PASS across seven categories (A-G).  
**Category A: Foundational Constants (5 tests).** Verify A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6), κ² \= A/Q \= 35/4807, M\_P \= 2.435 × 10¹⁸ GeV all inherited correctly from locked corpus.  
**Category B: Theorem S10.1 — Stückelberg Mixing Scale (6 tests).** Verify f² \= κ²M²\_P exact rational identity; numerical uniqueness (A/Q vs A/(Q−Z), 3A/Q², A alone — all deviations reproduced at claimed precision); Stückelberg mass m\_B for q\_Φ \= 1; lepton Stückelberg mass m\_B^(L) at Y\_L \= −1/2; GUT-scale range (1016 GeV mB1017 GeV); RG running consistency with ZS-S1 sin²θ\_W at integer arithmetic.  
**Category C: Theorem S10.2 — L\_XY \= 0 Preservation (7 tests).** Verify each of the five proof steps: Lorentz algebra unchanged, action-level absence of direct X-Y terms, Ward-Takahashi identity preserved, anomaly-free verification (5/5 conditions PASS), Schur protection layer unchanged. Additional tests: Feynman vertex enumeration (new ZS-S10 vertices: B-B mass, θ-B mixing, fermion-B); κ² coefficient in θ-B mixing vertex.  
**Category D: Theorem S10.3 — Stückelberg-Cor IV Bridge (6 tests).** Verify B\_μ \= 0 limit recovers ZS-F1 exactly (action-level equality); galactic Stückelberg screening at e−1053 suppression; inflation 1 regime preserves ZS-U1 observables; vortex core Corollary IV (F) realization; galactic halo Corollary IV (B) realization; common Z-Anchor boundary condition.  
**Category E: Theorem S10.4 — q\_Φ Charge (4 tests).** Verify Path I (ZS-F1 §3.2 coefficient \= 1); Path II (integer quantization modulo 2π); Path III (n=1 vortex observational consistency); Path IV (EFT kinematic bound 1q11).  
**Category F: Theorem S10.5-BPS — BPS Spinor Lift (7 tests).** Verify vortex existence (Jaffe-Taubes via ZS-A6 c\_cigar \= 0.06606); Frobenius expansion c1x+iy near core; complex structure J=−iy (direct matrix identity); vector rep R=exp−iy; spinor rep UZ=exp−iy/2; 4π closure Kz+2=−Kz; signed seam witness useam=cos/2.  
**Category G: Cross-Paper Consistency (1 test).** Verify ZS-S10 imports match upstream values at integer arithmetic precision for: A (ZS-F2), Q (ZS-F5), κ² (ZS-M6), L\_XY \= 0 (ZS-F1, ZS-S1), j=1/2 uniqueness (ZS-M3), Kraus count \= 2 (ZS-A7, ZS-A4), cigar vortex c\_cigar (ZS-A6), Corollary IV (ZS-A7), anomaly conditions (ZS-U9), Higgs VEV/Weinberg angle/strong coupling (ZS-S4/S1).  
**Expected total: 36 tests, target 36/36 PASS.**  
---

## **Appendix B. Cross-Reference Table**

| Result | Source | Used In | Relation |
| :---- | :---- | :---- | :---- |
| A \= 35/437 | ZS-F2 v1.0 §7 (LOCKED) | S10.1 | Input |
| Q \= 11 | ZS-F5 v1.0 §4 (PROVEN) | S10.1 | Input |
| ZS-F1 action | ZS-F1 v1.0 §3.1 (PROVEN) | §3 | Base action for extension |
| U(1)\_Z gauge invariance | ZS-F1 v1.0 §3.2 (PROVEN) | S10.4 Path I | Corpus-LOCKED convention |
| κ² \= A/Q | ZS-M6 Theorem 2.2.1 (DERIVED) | S10.1 | Mixing scale basis |
| L\_XY \= 0 | ZS-F1 §9, ZS-S1 §4 (PROVEN) | S10.2 | Extended to ZS-S10 |
| Continuum Perturbative Protection | ZS-M6 §7A (PROVEN-PERT) | S10.2 Steps 1-4 | Extended to ZS-S10 |
| Adjoint Obstruction Theorem | ZS-F2 §4.2A (PROVEN) | S10.2 Step 5 | Schur protection layer |
| Z-Anchor |Φ(x\_0)| \= 0 | ZS-F1 §5.2 (PROVEN) | S10.3, S10.5-BPS | Common BC |
| Cigar vortex profile | ZS-A6 §4.5.6 (DERIVED) | S10.5-BPS Step 1 | Existence/uniqueness |
| Frobenius expansion | ZS-A6 §4.4.1, §4.5.4 (DERIVED) | S10.5-BPS Step 2 | Linear core behavior |
| ε-Halo profile | ZS-A1 §2.2 (DERIVED) | S10.3 IR limit | (B) branch realization |
| Goldstone winding | ZS-A6 §4.4.2 (PROVEN) | S10.3 IR limit | 2π winding |
| Corollary IV | ZS-A7 §4.4 (DERIVED) | S10.3, S10.5-BPS | Target structure |
| Theorem 3.2-bis | ZS-A7 §3.2-bis (PROVEN) | S10.5-BPS Steps 5-6 | Kraus 4π closure |
| j=1/2 uniqueness | ZS-M3 Theorem 5.1 (PROVEN) | S10.5-BPS Step 7 | Uniqueness |
| SU(2) center | ZS-M3 Lemma 10.1 (PROVEN) | S10.5-BPS Step 6 | D1/2−I=−I |
| Half-angle V\_XZ | ZS-F4 §7/§7B (DERIVED) | S10.5-BPS §5 | Kraus square root origin |
| Stinespring/Kraus count | ZS-Q1 §3.3 (PROVEN) | S10.5-BPS Step 5 | Kraus count \= dim(Z) \= 2 |
| Trinity Braiding hypercharges | ZS-U9 Theorem 6.1 (DERIVED) | S10.2 Step 4, §6.5 | Y\_f inputs |
| Compact Phase Integer Quantization | ZS-U9 Theorem 3.1 (PROVEN) | S10.4 Path II | Integer c ∈ ℤ |
| SM Anomalies A1-A5 | ZS-U9 §7 (PROVEN) | S10.2 Step 4 | Preserved unchanged |
| Higgs VEV | ZS-S4 §6.12 (DERIVED) | NC-S10.5 | Preserved |
| sin²θ\_W \= 48/91·x\* | ZS-S1 §8.2 (PROVEN) | §3.4 | Input to g\_Y estimate |
| α\_s \= 11/93 | ZS-S1 §8.1 (DERIVED) | Appendix A Category G | Cross-check |
| λ\_vac \= 2A² | ZS-U5 §15.4 (DERIVED-COND) | §2, §7.2 | Cigar vortex potential |
| m\_ρ \= 2A·M\_P | ZS-F1 §4.4 (DERIVED) | §5.4 inflation | Radial mode mass |

---

## **References**

**Internal (Z-Spin series)**  
\[Z1\] K. Kang, "ZS-F1: The Z-Spin Action & U(1) Completion," v1.0 (2026). \[PROVEN U(1)\_Z gauge invariance §3.2; Z-Anchor §5.2\]  
\[Z2\] K. Kang, "ZS-F2: Geometric Impedance A \= 35/437," v1.0 (2026). \[LOCKED A \= 35/437; §4.2A Adjoint Obstruction Theorem PROVEN\]  
\[Z3\] K. Kang, "ZS-F4: Curvature Distribution and Holonomy," v1.0 (2026). \[§7/§7B half-angle amplitudes V\_XZ, V\_ZY DERIVED\]  
\[Z4\] K. Kang, "ZS-F5: Gauge Symmetry Constraint — Why Q \= 11," v1.0 (2026). \[PROVEN (Z,X,Y)=(2,3,6); dim(Z)=2\]  
\[Z5\] K. Kang, "ZS-M2: Geometric Harmonics," v1.0 (2026). \[PROVEN \[su(2)\_A, su(2)\_B\] \= 0\]  
\[Z6\] K. Kang, "ZS-M3: Regge-Holonomy, Immirzi & Z-Telomere," v1.0 (2026). \[Theorem 5.1 j=1/2 PROVEN; Lemma 10.1 SU(2) sign flip PROVEN\]  
\[Z7\] K. Kang, "ZS-M6: Block-Laplacian Spectral Verification," v1.0 (2026). \[Theorem 2.2.1 κ²=A/Q DERIVED; §7A Continuum Perturbative Protection Theorem PROVEN\]  
\[Z8\] K. Kang, "ZS-M9: McKay Correspondence and SM Field Classification," v1.0 (2026). \[§5.2 McKay bridge DERIVED; Table 2 HYPOTHESIS strong\]  
\[Z9\] K. Kang, "ZS-S1: Gauge Coupling Unification," v1.0 (2026). \[§4 L\_XY ≡ 0 PROVEN; §8 α\_s, sin²θ\_W\]  
\[Z10\] K. Kang, "ZS-S4: Electroweak & Higgs Completion," v1.0 (2026). \[§6.12 Higgs VEV DERIVED at 0.12%\]  
\[Z11\] K. Kang, "ZS-U1: ε-Field Inflation," v1.0 (2026). \[r \= 0.0089 DERIVED\]  
\[Z12\] K. Kang, "ZS-U5: Quantum Gravity Bridge," v1.0 (2026). \[§15.4 λ\_vac \= 2A² DERIVED-CONDITIONAL\]  
\[Z13\] K. Kang, "ZS-U9: Hypercharge Trinity," v1.0 (2026). \[Theorem 6.1 DERIVED; Trinity Braiding; §7 anomalies 5/5 PASS\]  
\[Z14\] K. Kang, "ZS-A1: Galactic Dynamics & Morphology," v1.0 (2026). \[§2 Goldstone halo DERIVED; 78/78 PASS\]  
\[Z15\] K. Kang, "ZS-A4: Black Hole Information and Quantum Protocol," v1.0 (2026). \[Appendix A Z-sector basis |4⟩, |6⟩\]  
\[Z16\] K. Kang, "ZS-A6: Boundary Physics," v1.0 (2026, April 2026 update). \[§4.5.6 cigar bounce DERIVED at 0.089% match\]  
\[Z17\] K. Kang, "ZS-A7: Horizon as Spinor — BH/WH Duality and the 4π Closure," v1.0.1 (2026). \[§3 Horizon Spinor Theorem DERIVED; §3.2-bis Theorem 3.2-bis PROVEN; §4.4 Corollary IV DERIVED\]  
\[Z18\] K. Kang, "ZS-Q1: Geometric Decoherence and CPTP Channel," v1.0 (2026). \[§3.3 Stinespring \+ Kraus PROVEN\]  
**External**  
\[E1\] J. McKay, "Graphs, singularities, and finite groups," Proc. Symp. Pure Math. 37, 183 (1980).  
\[E2\] A. Jaffe and C. Taubes, *Vortices and Monopoles*, Progress in Physics 2, Birkhäuser (1980). \[Global vortex existence and uniqueness\]  
\[E3\] E. C. G. Stückelberg, "Die Wechselwirkungskräfte in der Elektrodynamik und in der Feldtheorie der Kernkräfte," Helv. Phys. Acta 11, 225 (1938). \[Original Stückelberg mechanism\]  
\[E4\] G. W. Horndeski, "Second-order scalar-tensor field equations in a four-dimensional space," Int. J. Theor. Phys. 10, 363 (1974).  
\[E5\] J. Goldstone, "Field theories with superconductor solutions," Nuovo Cimento 19, 154 (1961).  
\[E6\] H. Rauch et al., "Verification of coherent spinor rotation of fermions," Phys. Lett. A 54, 425 (1975). \[Original 4π closure measurement\]  
\[E7\] R. L. Workman et al. (Particle Data Group), Phys. Rev. D 110, 030001 (2024). \[PDG 2024\]  
\[E8\] S. Elizalde, S. D. Odintsov, and A. Romeo, Phys. Rev. D 51, 1680 (1995). \[One-loop β-function for ξR coupling\]  
---

## **Version History**

**v1.0 (April 2026):** Initial public release. Consolidated from internal Z-Spin Collaboration research notes and four-session free-exploration development (April 2026\) covering: Theorem S10.1 (Stückelberg mixing scale, DERIVED-CONDITIONAL via ZS-M6 Theorem 2.2.1), Theorem S10.2 (L\_XY=0 preservation, PROVEN-PERTURBATIVE via five-step extension of ZS-M6 §7A), Theorem S10.3 (Stückelberg-Cor IV Bridge, DERIVED with backward compatibility verified in four regimes), Theorem S10.4 (Φ field U(1)\_Y charge q\_Φ \= \+1, DERIVED via four independent paths with circularity resolution), Theorem S10.5-BPS (Bogomolnyi BPS spinor lift, DERIVED via seven-step explicit proof with observable ũ\_seam \= cos(α/2)).  
36 verification tests across seven categories (Foundational / S10.1 / S10.2 / S10.3 / S10.4 / S10.5-BPS / Cross-Paper). Five falsification gates (F-S10.1 through F-S10.5) registered. Ten non-claims (NC-S10.1 through NC-S10.10) registered to prevent overclaim.  
Gap G1 of the Trinity Braiding Theorem (ZS-U9 NC-U9.2) CLOSED at the action level via ZS-S10 master action. Gap G2 (ZS-M9 Table 2 upgrade) advanced through anomaly-preserving structure but remains OPEN as a separate closure problem.  
Zero new free parameters; A \= 35/437 remains the sole geometric input. All upstream results preserved unchanged: ZS-F1 action (B\_μ=0 limit), ZS-A1 78/78 PASS (galactic screening), ZS-U1 r=0.0089 (inflation), ZS-A7 Corollary IV (F)/(B) duality (action-level realization).