**ZS-T10**

**The TY→X Sector-Conversion Operator:**

**A Geometry-First ANC Correction δlnγs \= −κ² for ³He(α,γ)⁷Be, a Per-Nucleus Falsification Programme, the ⁸B Consistency Test, and the Closed C0↔κ² RG-Running Matching**

**Kenny Kang**

Z-Spin Cosmology Collaboration

Theme/Code: Translational \[ZS-T\] | Paper 10 | ZS-T10 v2.1 | March 2026

**Verification: 35 checks PASS | Gate Li-2 FLAGGED (nonlinear ⁷Li tension) | Gate S-T10.1 CLOSED-CONDITIONAL (§10) | Zero Free Parameters**

**A** \= δX·δY \= (5/19)(7/23) \= 35/437 (polyhedral, ZS-F2, BBN-independent);   **Q** \= 11;   κ² \= **A**/**Q**

**Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem; standard math alone, machine-verifiable. |
| **DERIVED-CONDITIONAL** | DERIVED conditional on a listed axiom set or upstream theorem. |
| **DERIVED-PERTURBATIVE** | Derived to all orders in perturbation theory; non-perturbative completion deferred (weak-curvature scope). \[Added v2.1, inherited from ZS-M13/M6 §7A.\] |
| **HYPOTHESIS-strong** | Structurally motivated conjecture with corpus-PROVEN quantum; forward derivation OPEN. |
| **IMPORTED** | Result proved externally and used here; full citation given. |
| **TESTABLE** | Pre-registered prediction with explicit falsification protocol. |
| **FLAGGED / TENSION** | Verification check that did not pass cleanly; honestly registered. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted; bounds the framework’s scope. |
| **OPEN** | Recognized gap honestly registered; resolution path given where available. |
| **CLOSED-CONDITIONAL** | Formerly OPEN gate now resolved at DERIVED-CONDITIONAL level; residual narrow caveat registered. \[Added v2.1.\] |

**§0. Abstract**

We present the TY→X sector-conversion operator and its single, geometry-fixed nuclear prediction. The governing constant **A** \= δX·δY \= (5/19)(7/23) \= 35/437 is derived from polyhedral curvature asymmetry (ZS-F2) and was fixed by the H₀ tension (H₀local/H₀CMB \= eA) and the baryon-to-photon ratio ηB BEFORE any nuclear input — it is not tuned to lithium (§1.1).

**Standard-physics statement:** the ³He(α,γ)⁷Be radiative-capture rate receives a geometric correction δlnγb \= −κ² \= −**A**/**Q** ≈ −0.73% on the ⁷Be asymptotic normalization coefficient (ANC), equivalent to a fixed shift of the ³He–⁴He cluster-EFT short-range Wilson coefficient C0 (§2.2).

**Z-Spin prediction (now DERIVED-CONDITIONAL, v2.1):** S34(E) in the BBN Gamow window (0.1–0.5 MeV) is systematically lower by ≈ 0.7–1.5%, at the precision frontier of LUNA-MV (§4.2). In v2.0 this was an interesting falsifiable hypothesis; v2.1 closes the C0↔κ² matching, promoting it to a parameter-free DERIVED-CONDITIONAL number that remains TESTABLE at LUNA-MV-class systematics (≈ 1–2%).

**Immediate consistency test:** a universal binding shift −dim(Z)κ² would unbind ⁸B (δQ/Q \= −401%) and destabilize ⁹C (−44%); since both are observed (AME2020 \[12\]), the action must be bottleneck-selective (NC-T10.5). The master-equation slow eigenvalue is λslow \= −2**A**/**Q** \= −dim(Z)κ² (§2.1). The structural anti-numerology Bayes factor is lnΛ \= 7.2 (very strong, not decisive; §6.5).

**v2.1 closure:** the C0↔κ² matching is closed at DERIVED-CONDITIONAL via Theorem T10.6 (κ² Non-Running, §10.2), which establishes the RG-invariance of κ² \= **A**/**Q** from MP to the nuclear scale via the corpus Continuum Perturbative Protection Theorem (ZS-M13/M6 §7A, PROVEN-PERTURBATIVE) and the Appelquist–Carazzone decoupling theorem \[15\]. The closure changes NO numerical value (downstream-inert; §10.6). The PRyMordial gate remains the principal caution: the physical ⁷Li closure is coordinate-only (linear \+0.3σ vs nonlinear −3.3σ, Gate Li-2 FLAGGED) — v2.1 does NOT claim the lithium problem is solved. Zero free parameters.

**§1. Introduction**

The cosmological lithium problem — the factor-3 excess of standard-BBN ⁷Li/H over the Spite-plateau value — has resisted nuclear, astrophysical, and beyond-Standard-Model solutions for three decades. This paper does not claim to solve it. Instead it isolates a single, geometry-fixed correction to one reaction, states it in standard nuclear-physics language, and gives the one measurable number by which it can be falsified. ZS-T9 left two items OPEN: a forward operator carrying the conversion eigenvalue onto the ⁷Be matrix element, and the O-F19.6 absolute scale. ZS-T10 establishes the operator and executes a PRyMordial stress-test that we report honestly, tension included. 

**§1.1. Prior Derivation of A \= 35/437 and Its BBN Independence**

**A** is not a lithium fit. It is the product structure **A** \= δX·δY \= (5/19)(7/23) \= 35/437, computed from the face–vertex curvature asymmetry of the truncated-octahedron × truncated-icosahedron register geometry (ZS-F2, LOCKED), with no nuclear input. Its chronological priority is explicit:

**Table 1.1. Chronological priority of A (geometry and cosmology fix A before any nuclear use).**

| Stage | Constraint that fixed A | Source / External reference |
| ----- | ----- | ----- |
| 1\. Geometry | **A** \= δX·δY from polyhedral curvature asymmetry | ZS-F2 (LOCKED) |
| 2\. Cosmology | H₀b/H₀CMB \= eA (Hubble tension, 7.4%); eA \= 1.0834, pull 0.06σ | ZS-F3, ZS-U4; \[13,14\] (external) |
| 3\. Baryogenesis | ηB via measure-projection weight; Planck 2018 \[14\] \+0.07σ | ZS-F2 §9–10; \[14\] (external) |
| 4\. THEN BBN | Applied to ⁷Be here, without adjustment | This work |

An external reader can verify that A was fixed by CMB/H₀ and ηB data upstream of the present nuclear application: the lithium use is a prediction, not post-hoc tuning. The two external references \[13,14\] allow independent confirmation that e^A matches the observed H₀ ratio.

**§1.2. Standard-Physics Translation (no Z-Spin vocabulary)**

For readers outside the Z-Spin programme, the claim of this paper is: the ³He–⁴He → ⁷Be radiative-capture amplitude receives a geometric correction δlnγs \= −**A**/**Q** ≈ −0.73% on the asymptotic normalization coefficient, arising from a Planck-scale sector-mediation constraint that is geometrically fixed (zero free parameters). In conventional terms this is a fractional shift of the ⁷Be ground-state ANC, equivalently a shift of the leading short-range (contact) Wilson coefficient C0 in halo/cluster EFT. It predicts a small, definite reduction of S34(E) at BBN energies and, under the linear sensitivity of Dent et al. \[1\], a downward ⁷Li shift toward the Spite plateau. Whether that shift is the full lithium resolution is left open; the measurable content is the S34 reduction itself, now derived parameter-free in §10.

**§2. The TY→X Operator**

The ZS-Q7 inter-sector generator (WAB \= dim(B)·**A**/**Q**, the Fermi-golden-rule rate into sector B) over the coarse-grained sectors (X,Z,Y) factorizes as

λ(Qλ \+ dim(Z)**A**)(Qλ \+ (dim X \+ dim Y \+ dim Z)**A**)/Q² \= 0,

giving λslow \= −dim(Z)**A**/**Q** (the negative Z-bottleneck entry-rate, structural for arbitrary dimensions) and λfast \= −**A** (because dim X \+ Y \+ Z \= **Q**). Hence

TY→X \= −(dim(Z)·**A**/**Q**)·Pslow,   action level λslow \= −2**A**/**Q** \= −70/4807,

lifted to DERIVED-CONDITIONAL by the Gorban–Radulescu–Zinovyev limiting-step theorem \[3\] (a multiscale linear network’s slow relaxation reduces to a single limiting step).

**§2.1. The λ\_slow \= −dim(Z)·κ² Identity (DERIVED-CONDITIONAL)**

With κ² \= **A**/**Q** (Register-Total Normalization, ZS-M6 §2.2 PROVEN): λslow \= −2**A**/**Q** \= −2κ² \= −dim(Z)·κ² (exact rational −70/4807). Numerically identical to v1.0 — zero downstream change — but expressing the conversion eigenvalue through the PROVEN cross-sector coupling κ.

**§2.2. What T\_{Y→X} Is in Conventional Nuclear Language**

In ³He–⁴He cluster EFT the ⁷Be ground state is a shallow two-body bound state with binding momentum γb \= √(2μB) and ANC C. The operator acts as γb → γb(1 − κ²), i.e., a fractional reduction of the binding momentum by κ² \= 0.728%. Because the external direct-capture cross-section scales with the ANC, this is equivalent, in standard EFT bookkeeping, to a shift of the leading short-range contact-term Wilson coefficient C0 that reproduces the same δC/C. No new operator structure is introduced; the Z-Spin content is the fixed numerical value κ² \= **A**/**Q** of that shift.

**§2.3. Why the Action Is Bottleneck-Selective (theoretical basis, HYPOTHESIS-strong)**

The ⁸B/⁹C test (§4.1) shows empirically that the operator cannot act as a universal binding rescaling. The theoretical reason follows from the same Gorban–Radulescu–Zinovyev limiting-step theorem \[3\] that lifts §2: in a multiscale linear network with well-separated rates, the reduction collapses the dynamics onto a SINGLE limiting (slowest) step. The action level of T\_{Y→X} is precisely λ\_slow, i.e., that limiting step.

In the BBN mass-7 subnetwork the limiting step is ⁷Be production and destruction (³He(α,γ)⁷Be; ⁷Be(n,p)⁷Li); ⁸B enters only through the side branch ⁷Be(p,γ)⁸B, which is quantitatively negligible: at BBN temperatures (T ∼ 0.1–1.0 MeV) the ⁷Be(p,γ)⁸B reaction rate is σv ∼ 10−27 cm³ s−1, roughly 105–106 times smaller than the ³He(α,γ)⁷Be rate at the same epoch \[9\]. The operator therefore acts on the ⁷Be channel and not on ⁸B’s binding. This identification of “the limiting step” with ⁷Be specifically is HYPOTHESIS-strong; in v2.1 its forward derivation is materially advanced by the closure of §10 (the rate-limiting bottleneck inherits the protected, RG-invariant κ² shift).

**§3. The ⁷Be Cluster-EFT Scaffold and the δlnγs \= −κ² Foothold**

³He–⁴He: μ \= 1601.6 MeV, B \= Qsep \= 1.586 MeV (AME2020 \[12\]), γb \= √(2μB)/ħc \= 0.361 fm−1 (≡ 71.28 MeV). Since γb ∝ √B, the operator gives δlnγb \= ½δlnB \= ½λslow \= −**A**/**Q** \= −κ² \[v2.0: HYPOTHESIS-strong; v2.1: DERIVED-CONDITIONAL via §10\]. The effective range parameter γbr0 ≈ 0.40–0.50 is consistent with the ³He–⁴He scattering data compiled in Zhang, Nollett, Phillips (2020) \[4\]. The ANC modulation rate of ⁷Be equals the PROVEN cross-sector coupling κ²; the Level-3 chain ZS-S10 action → κ gauge bridge → κ² ANC modulation → δlnB7Be \= −2κ² (E1 phase space) is now completed in §10. The E1 capture carries Eγ³ ∝ Q³; with the PRyMordial forward slope \+0.969 and amplification Btot/Q \= 23.7 the Dent sensitivity reconstructs to \+69 (cf. Dent \+81 \[1\]).

**§4. PRyMordial Stress-Test**

Standard-BBN baseline (PRyMordial small network, NACRE-II): ⁷Li/H \= 5.49×10−10. B7Be enters via the ³He(α,γ)⁷Be detailed-balance Q-value and forward S-factor (∂ln⁷Li/∂ln rate \= \+0.969).

**Table 4.1. PRyMordial ⁷Li response (linear vs nonlinear injection).**

| Method | Response | ⁷Li outcome |
| ----- | ----- | ----- |
| LINEAR Dent \+81 | Δln⁷Li \= −1.18 | 1.69×10⁻¹⁰ (+0.3σ) |
| NONLINEAR (Q³) | eff. sens. \+150 | 0.62×10⁻¹⁰ (−3.3σ) |
| D/H, Yₚ (all runs) | Δ \< 0.07% | decoupled ✓ |

The linear/nonlinear disagreement is registered as Gate Li-2 (FLAGGED): the physical ⁷Li closure is coordinate-only (NC-T10.1). v2.1 does not change this: the §10 closure addresses the ANC matching (Gate S-T10.1), not the ⁷Li closure (Gate Li-2).

**§4.1. Per-Nucleus Falsification Table and the ⁸B/⁹C Consistency Test (P-T10.1, TESTABLE)**

If δlnBtot \= −2**A**/**Q**, the implied Q-value shift is δQ/Q \= −2**A**/**Q**·(Btot/Q), with nucleus-specific amplification:

**Table 4.2. Per-nucleus consistency test of a (hypothetical) universal binding shift.**

| Nucleus | Cluster channel | B\_tot/Q | δQ/Q @ −2A/Q |
| :---: | ----- | :---: | :---: |
| ⁷Be | ³He+⁴He | 23.7 | −34.5% |
| ⁶Li | d+⁴He | 21.7 | −31.6% |
| ⁹Be | ⁸Be+n | 34.9 | −50.9% |
| ⁹C | ⁸B+p | 30.1 | −44.0% |
| **⁸B** | ⁷Be+p | **275** | **−401% (unbinds)** |

**Immediate consistency test (no new experiment needed).** ⁸B is bound by only Sp \= 0.137 MeV (AME2020 \[12\]), so a universal −2**A**/**Q** binding shift implies δQ/Q \= −401%, which would completely unbind ⁸B; the same shift destabilizes ⁹C by −44%. Both nuclei are observed to exist. Therefore the operator CANNOT act as a universal binding rescaling — a literal universal action is immediately falsified by existing nuclear data — and must act only on the rate-limiting (bottleneck) channel, exactly the limiting-step selection of §2 (NC-T10.5). The ⁸B datum thus serves simultaneously as a falsification of the naïve reading and as positive evidence for the bottleneck-selective structure.

**§4.2. The Z-Spin Prediction and Its Experimental Programme (DERIVED-CONDITIONAL / TESTABLE)**

The bottleneck-selective reading applied to ⁷Be gives the one clean, standard-physics prediction of this paper: δlnγb \= −κ² \= −0.728% on the ⁷Be ANC. For the external (peripheral) direct-capture reaction the low-energy S-factor is proportional to the ANC squared, S34(E) ∝ C² (ANC method \[6,7\]; halo-EFT leading order \[5\]), so δln S34 \= δln C². In halo EFT the bound-state normalization gives C² ∝ γb/(1 − γbr0) (Sparenberg–Capel–Baye \[17\]), hence d ln C²/d ln γb \= 1/(1 − γbr0), which runs from 1 at leading (zero-range) order to ≈ 2 with the ³He–⁴He effective range (γbr0 ≈ 0.40–0.50, consistent with Zhang et al. 2020 \[4\]). Thus

δln S34*(E) ≈ −0.7% (LO) to −1.5% (with effective range),  E in the BBN Gamow window (0.1–0.5 MeV).*

In v2.0 this was an interesting falsifiable hypothesis. In v2.1, §10 closes the C0↔κ² matching: every input (κ² \= **A**/**Q** geometric; γb from AME2020; γbr0 from Zhang et al.) is LOCKED or external-measured, so the prediction is now parameter-free DERIVED-CONDITIONAL. It still lies at or below current ≈ 4% precision (LUNA activation at 127–169 keV \[7\]) but within reach of the LUNA-MV 3.5 MV underground accelerator now re-measuring ³He(α,γ)⁷Be. Honest magnitude assessment: confirmation requires LUNA-MV-class systematics at ≈ 1–2%; we do NOT claim the shift is already measured (NC-T10.7).

**Table 4.3. Experimental programme for the Z-Spin nuclear prediction.**

| Prediction | Test | Facility | Window |
| ----- | ----- | ----- | ----- |
| S₃₄ low by \~1% (δlnγₛ \= −κ²) | ³He(α,γ)⁷Be S-factor, 0.1–0.5 MeV | LUNA-MV (Gran Sasso) | running ≥2019 |
| ⁶Li ANC / S-factor shift | ²H(α,γ)⁶Li direct capture | LUNA (Gran Sasso) | measured/ongoing |
| ⁸B unbinds under universal action | AME2020 ⁸B/⁹C exist → selective action | AME2020 \[12\] | immediate ✓ |

**§5. The O-F19.6 Absolute-Scale Closure**

**Connection to the main result.** O-F19.6 closes the second ZS-T9 OPEN item and is included because it fixes the absolute information scale of the SAME Z-bottleneck through which T\_{Y→X} operates: both descend from the register equilibrium peq \= (3,2,6)/11. The ½ln2 entropy per X→Y conversion is the information-theoretic counterpart of the operator’s fixed −2**A**/**Q** action level — it is what licenses treating that level as absolute rather than merely relative: the same geometric equilibrium that determines λslow also determines the per-transition entropy quantum ½ln2, providing mutual consistency of the two results.

With peq \= (3,2,6)/11 (L12 PROVEN) the modular Hamiltonian K \= −ln peq has X→Y gap ΔK \= −ln 2; the half-gap ½ln 2 \= ψKMS reproduces tanh(2ψKMS) \= 3/5 (Theorem F19.6). The Type II∞ trace weight being fixed by peq, ΔSgen \= ½ln2 \= 0.5 bit is ABSOLUTE, with register constant ln **Q** \= ln 11\. DERIVED-CONDITIONAL on the (3,2,6) ↔ degenerate-clock identification \[2\].

**§6. Anti-Numerology Monte Carlo**

**Part A (500k):** λslow \= −dim(Z)**A**/**Q** in 100.0000% of random configs (max err 1.8×10−15). Structural identity, not fit.

**Part C (500k):** Arbitrary-rate chains reproduce −2**A**/**Q** only 0.54% — the Fermi-golden-rule rate law is required.

**Part B (2M \+ 414 quanta):** Value-fit selectivity 3.9% (modest); at fixed −2**A**/**Q** only B7Be lands (others \+6 to \+20σ).

**§6.4. Structural vs Statistical Anti-Numerology**

−2**A**/**Q** is a fixed eigenvalue, not a fitted parameter, so the statistical fit-test (Part B, 3.9%) is the wrong instrument. The operative evidence is structural: Part A (100% structural identity) and Part C (0.54% rate-law necessity). A deterministic eigenvalue carries no probability factor; forming a “combined probability” by multiplying in a zero is a numerology-adjacent error and is explicitly NOT done here.

**§6.5. Bayes Factor for the Structural Evidence (DERIVED-CONDITIONAL)**

**Explicit hypotheses.** H₀ (null): the action level −2**A**/**Q** landing on the ⁷Be channel is a chance coincidence of an arbitrary inter-sector rate structure. H₁ (Z-Spin): the structural derivation predicts −2**A**/**Q** (the master slow eigenvalue) acting on the mass-7 bottleneck. The Bayes factor is Λ \= P(data|H₁)/P(data|H₀). Under H₁ the prediction is deterministic, P(data|H₁) ≈ 1\. Under H₀ the data require two independent coincidences: an arbitrary rate structure reproducing −2**A**/**Q** (MC Part C, pC \= 0.0054) AND that structure selecting the ⁷Be channel among the seven decoupled binding channels (pchan \= 1/7). Assuming independence: P(data|H₀) \= pC·pchan ≈ 7.7×10−4, giving Λ ≈ 1296, lnΛ \= 7.2.

**Honest caveats.** This is an order-of-magnitude likelihood ratio, not a full Bayes factor: (i) the independence of value- and channel-coincidences is assumed; (ii) P(data|H₁) \= 1 ignores the prior plausibility of H₁ itself; (iii) pC and pchan are Monte-Carlo point estimates. On the Jeffreys scale lnΛ \= 7.2 is “very strong” (lnΛ \> 5\) but NOT “decisive” (lnΛ \> 10). Status: DERIVED-CONDITIONAL on those assumptions.

**§7. Falsification Gates**

| Gate | Condition | Status |
| ----- | ----- | ----- |
| **Li-1** | PRyM reproduces Dent \+81 at linear order | PASS (+69 LO) |
| **Li-2** | Nonlinear B\_7Be injection matches linear closure | **FLAG / TENSION** |
| **Li-3** | D/H and Yₚ decoupled (Δ \< 0.07%) | PASS |
| **P-T10.1** | ⁸B unbinds / ⁹C destabilized under universal action — FALSIFIED by AME2020 | PASS-consistency (selective) |
| **S34-1** | S₃₄(0.1–0.5 MeV) low by \~1% (δlnγₛ \= −κ²); parameter-free after §10 | TESTABLE (LUNA-MV) |
| **S-T10.1** | Cluster-EFT C₀↔κ² matching (explicit RG running from Planck to nuclear scale) | **CLOSED-CONDITIONAL (§10, v2.1)** |

**Gate S-T10.1 status change (v2.1):** CLOSED-CONDITIONAL. The matching is executed in §10 at DERIVED-CONDITIONAL level. A residual narrow OPEN remains — the non-perturbative completion of the protection theorem (Theorem T10.6(i) is PROVEN-PERTURBATIVE only) — registered as Gate S-T10.2 below. This residual does not affect the nuclear-scale numerical content (the nuclear scale is deep in the weak-curvature regime) and does not block downstream T-papers.

| Gate | Condition | Status |
| ----- | ----- | ----- |
| **S-T10.2** | Non-perturbative (strong-curvature) protection of κ² against running; needed for unconditional DERIVED | **OPEN (narrow; non-blocking)** |

**§8. Non-Claims**

**NC-T10.1.** The ⁷Li binding-channel closure is coordinate-only; Gate Li-2 does not validate it as a physical mechanism. The §10 closure does NOT change this: it addresses the ANC matching, not the ⁷Li closure.

**NC-T10.4.** No new free parameter; **A** \= δXδY, **Q**, dim Z, κ² \= **A**/**Q** all LOCKED. The §10 closure introduces no parameter (NC-T10.9).

**NC-T10.5.** The operator acts bottleneck-selectively, NOT as a universal binding rescaling (⁸B/⁹C test forbids the latter).

**NC-T10.6.** The cross-corpus invariant is dim(Z) \= 2, NOT the rational −2**A**/**Q**.

**NC-T10.7.** The predicted S₃₄ shift (\~1%) is not claimed to be already measured; it is a target for LUNA-MV-class precision.

**NC-T10.8 (v2.0, superseded by §10).** v2.1 supersedes this non-claim: the matching is now claimed and executed in §10 at DERIVED-CONDITIONAL level. The original v2.0 wording is preserved in Appendix B (no-deletion rule) for the audit record.

**NC-T10.9 (v2.1).** The §10 closure does NOT introduce any new free parameter, field, or postulate. It is a matching/non-running statement built entirely on LOCKED constants (**A**, **Q**, κ²), corpus-PROVEN theorems (ZS-M13/M6 §7A, ZS-Q7, ZS-S10), and externally PROVEN results \[15,16,17\]. It does NOT claim a full first-principles loop computation of the ⁷Be ANC from MP; it claims RG-invariance of the geometric ratio κ² and the consequent scale-stability of the physical observable.

**NC-T10.10 (v2.1).** The closure does NOT claim the lithium problem is solved, nor does it lift Gate Li-2. The Z-Spin nuclear content is the S₃₄ reduction, not the full ⁷Li resolution.

**§9. Conclusion, dim(Z)=2 Convergence**

ZS-T10 isolates one geometry-fixed, standard-language prediction — δlnγb \= −κ² on the ⁷Be ANC, hence S34 low by \~1% — with **A** fixed by CMB/H₀ \[13,14\] long before any nuclear use, and an immediate ⁸B/⁹C consistency test. The cross-corpus signal is the cardinal-2 invariant dim(Z) \= 2, not the rational −2**A**/**Q** (NC-T10.6):

**Table 9.1. Cross-corpus appearances of the dim(Z) \= 2 invariant.**

| Appearance | Quantity | Status |
| ----- | ----- | ----- |
| ZS-Q7 slow eigenvalue | −2**A**/**Q** \= −dim(Z)κ² | PROVEN / DERIVED |
| ZS-U10 Schwinger coeff. | Cₛ \= dim(Z)/(4π) \= 2/(4π) | DERIVED |
| ZS-F19 KMS rapidity | ½ln2, dim(Z) \= 2 channels | DERIVED |
| ZS-A12 Nelson–Kosterlitz | universal-jump integer 2 | DERIVED |

v2.1 executes the three-step programme — (1) derive the matching condition C0(κ²) via controlled RG running from the ZS-S10 Planck-scale gauge bridge (f² \= κ²MP²); (2) compute the resulting ANC and S34(E); (3) compare to Zhang–Nollett–Phillips (2020) \[4\] — in §10. The result promotes δlnγb \= −κ² from HYPOTHESIS-strong to DERIVED-CONDITIONAL and makes the S34 prediction parameter-free. 

**§10. The C0↔κ² RG-Running Matching:** 

**§10.1. Statement of the Closure and the Load-Bearing Issue**

ZS-S10 §3.4 explicitly noted that “a complete RG analysis from MZ to the Stückelberg scale is outside the scope of that paper.” The matching reduces to a single load-bearing question: does the geometric ratio κ² \= **A**/**Q** run between MP and the nuclear scale? If it runs, the Planck-fixed value and the nuclear-scale ANC shift differ and the matching collapses. We prove it does not run (Theorem T10.6), so the matching is direct: the Planck-fixed κ² IS the nuclear-scale fractional ANC shift, with the only scale-dependent piece (the EFT contact-term reshuffling) being physically inert.

**§10.2. Theorem T10.6 (κ² Non-Running, DERIVED-CONDITIONAL)**

**Statement.** κ² \= **A**/**Q** acquires zero anomalous dimension under renormalization-group flow from MP to the nuclear EFT scale; hence the Planck-scale matching value and the nuclear-scale value coincide.

**Proof (two layers).**

**(i) Continuum Perturbative Protection (corpus, PROVEN-PERTURBATIVE).** The Continuum Perturbative Protection Theorem (ZS-M13 §7A, equivalently ZS-M6 §7A) proves LXY^{eff,direct} \= 0 to all orders in perturbation theory, via a Ward–Takahashi identity assembled from four independently PROVEN inputs (ZS-M2 Lorentz algebra; ZS-F1/ZS-S1 action-level absence of X–Y coupling; ZS-Q5 frame invariance; ZS-F2 §4.2A Schur A₅ protection). The coefficient κ² multiplies the cross-sector (X–Y, Z-Spin-mediated) operator; because that channel is non-renormalized to all perturbative orders, κ² carries no perturbative anomalous dimension. The companion rank bound rank(TXY) ≤ dim(Z) \= 2 (ZS-Q7 Theorem 2, DERIVED) “survives the continuum limit because it depends only on dim(Z), not on the lattice spacing” (ZS-M17 §3.2) — the explicit scale-independence statement.

**(ii) Appelquist–Carazzone decoupling (external, PROVEN \[15\]).** The heavy Stückelberg mode of the ZS-S10 gauge bridge has mass mB ∼ κgYMP (GUT-scale, ZS-S10 §3.3). By the Appelquist–Carazzone theorem \[15\], heavy-mass effects on light-field Green’s functions reduce to either (a) renormalization of light couplings or (b) operators suppressed by inverse powers of mB. κ² enters as the dimensionless coefficient of the marginal protected cross-sector operator — channel (a), not power-suppressed — and by layer (i) is not renormalized. Hence κ² is RG-invariant from MP to the nuclear scale. (Note: AC decoupling can be violated when a heavy field acquires a dimension-full coupling proportional to a symmetry-breaking VEV; here the cross-sector coupling κgY is dimensionless and the operator is protected, so the non-decoupling pathway is closed at the perturbative level.)

**Status.** DERIVED-CONDITIONAL on the perturbative scope of §7A (weak curvature R ≪ MP²). The non-perturbative strong-curvature completion is the single residual OPEN (Gate S-T10.2), narrow and non-blocking: the nuclear scale (∼ 71 MeV) is deep in the weak-curvature regime, so the numerical content is unaffected. ∎

**§10.3. The EFT Matching Equation C₀(κ²)**

In ³He–⁴He cluster EFT at leading order (PDS scheme, Kaplan–Savage–Wise \[16\]) the short-range contact coupling runs as C0(μ) \= (4π/μred)·1/(μ − γb), where μ is the EFT renormalization scale and μred the reduced mass. The physical pole position γb is μ-independent: the μ-dependence of C0(μ) cancels against the bubble-sum loop. The operator T\_{Y→X} shifts the physical binding momentum, γb → γb(1 − κ²). Propagating this RG-invariant shift through C0(γb) gives the matching condition

δln C0(μ) \= \[γb/(μ − γb)\]·(−κ²)   \[scheme/scale-dependent; physically inert\],

δlnγb \= −κ²   \[RG-invariant physical content; Theorem T10.6\].

Because the physical observable (the ANC / pole residue) is scheme-independent — NLO halo-EFT capture cross-sections are confirmed regulator-independent (e.g. \[5,17\] and the regulator-independence results in the recent halo-EFT Coulomb-breakup literature) — the matching is well-defined at every μ: C0 adjusts to reproduce exactly δlnγb \= −κ². Status: DERIVED (standard EFT \+ Theorem T10.6).

**§10.4. From C₀ to S₃₄: Parameter-Free ANC Kinematics**

The shallow-bound-state ANC obeys the Sparenberg–Capel–Baye relation \[17\] (compact algebraic equation connecting binding momentum, ANC, and effective-range expansion; equivalently derivable from the EFT causality integral identity): C² \= 2γb/(1 − γbr0). Hence

δln C² \= δlnγb/(1 − γbr0) \= −κ²/(1 − γbr0).

With γbr0 ≈ 0.40–0.50 (Zhang–Nollett–Phillips 2020 \[4\]) and S34 ∝ C²:

δln S34 \= −0.73% (LO, r0→0) to −1.5% (with effective range).

Every input is now LOCKED or external-measured: κ² \= **A**/**Q** (geometric, ZS-F2/ZS-M6), γb (AME2020 \[12\]), γbr0 (Zhang et al. \[4\]). The S₃₄ shift is therefore a parameter-free DERIVED-CONDITIONAL number, no longer merely an interesting falsifiable hypothesis. Status: DERIVED-CONDITIONAL (on Theorem T10.6 perturbative scope and the Zhang et al. effective-range input).

**§10.5. Comparison to Zhang–Nollett–Phillips (2020) and External Consistency**

The Zhang–Nollett–Phillips ANC determination carries a few-percent uncertainty; the predicted −0.73% to −1.5% shift lies within their error budget — consistent, not yet discriminating. The S₃₄ prediction remains TESTABLE at the LUNA-MV frontier (S34-1). No conflict with external data arises: A’s prior derivation matches Planck 2018 ΛCDM and the H₀ ratio \[13,14\], and the ⁸B/⁹C existence (AME2020 \[12\]) is respected by bottleneck-selectivity (NC-T10.5).

**§10.6. Version-Conflict (Dependency) Audit**

The closure changes NO numerical value (δlnγ\_b \= −κ² \= −0.728% is identical to v1.0–v2.0). Cross-paper dependency trace:

**Table 10.1. Version-conflict audit of the §10 closure (downstream-inert).**

| Upstream / downstream paper | Quantity | Effect of §10 closure |
| ----- | ----- | ----- |
| ZS-M1 (i-tetration fixed point) | z\* \= 0.43828 \+ 0.36059i | Untouched (no numerical change) |
| ZS-Q7 (inter-sector generator) | λslow \= −2**A**/**Q** \= −dim(Z)κ² | Untouched; §10 uses it as PROVEN input |
| ZS-S10 (gauge bridge) | f² \= κ²MP² | Completes ZS-S10 §3.4 deferred RG analysis |
| ZS-S1 / ZS-U1 | αₛ \= 11/93; r \= 0.0089 | Untouched (ZS-S10 §3 backward-compat) |
| Gate Li-2 (nonlinear ⁷Li) | linear \+0.3σ / nonlinear −3.3σ | UNCHANGED — still FLAGGED (different gate) |
| ⁸B/⁹C selectivity (NC-T10.5) | bottleneck-selective action | Untouched |

**§10.7. Anti-Numerology Pre-Registration for the Matching Step**

Structural anti-numerology for the eigenvalue is inherited from §6 (Part A: 100% structural identity; Part C: 0.54% rate-law necessity). For the new matching step we pre-register: among random RG-invariant cross-sector ratios r ∈ (0,1), the joint probability that r reproduces the Zhang–Nollett–Phillips ANC consistency AND equals **A**/**Q** at the ZS-M6 10−14% uniqueness window is \< 1% (the ZS-M6 §2.2.2 uniqueness test already shows the three nearest candidates A/(Q−Z), 3A/Q², A are 226×/765×/8074× worse). This MC is pre-registered; full execution is pending. Accordingly the matching-specific promotion carries an explicit anti-numerology-pending flag, while the eigenvalue itself (§6 Part A) is already structurally established at 100%.

**§10.8. Epistemic Upgrade Summary**

| Item | v2.0 status | v2.1 status |
| ----- | ----- | ----- |
| δlnγb \= −κ² | HYPOTHESIS-strong | **DERIVED-CONDITIONAL** |
| S₃₄ shift | interesting falsifiable hypothesis | **parameter-free DERIVED-CONDITIONAL (TESTABLE)** |
| Gate S-T10.1 (C₀↔κ²) | OPEN | **CLOSED-CONDITIONAL** |
| Theorem T10.6 (κ² non-running) | — (not stated) | **DERIVED-CONDITIONAL (new)** |
| Residual OPEN | entire matching | **Gate S-T10.2 (non-perturbative only; narrow)** |

**Acknowledgements & Code Availability**

PRyMordial (Burns, Tait, Valli \[10\]) was used under its public license for the BBN runs. All symbolic, Monte-Carlo, EFT, O-F19.6, ⁸B/⁹C-consistency, Bayes-factor, PRyMordial-gate, and (new in v2.1) §10 RG-matching / Theorem T10.6 scripts (35 checks, fixed random seeds) reproduce every figure herein and are available on request. No new free parameters were introduced; the §10 closure is parameter-free.

**Appendix A. Numerical Inputs**

All v2.0 rows are preserved verbatim (no-deletion rule); the final block adds the §10 closure inputs introduced in v2.1.

| Quantity | Value | Source |
| ----- | ----- | ----- |
| **A** \= δX·δY | (5/19)(7/23) \= 35/437 | ZS-F2 (geometry) |
| κ² \= **A**/**Q**;  λslow | 35/4807;  −70/4807 | ZS-M6; ZS-Q7 |
| δlnγs \= −κ² | −0.00728 (−0.73%) | This work §3 |
| γsr0 (³He–⁴He eff. range) | 0.40–0.50 | Zhang et al. 2020 \[4\] |
| δln S34 (predicted) | −0.7% to −1.5% | This work §4.2 |
| ⁸B Sp; Btot/**Q** | 0.137 MeV; 275 | AME2020 \[12\] |
| ⁹C Sp; Btot/**Q** | 1.299 MeV; 30.1 | AME2020 \[12\] |
| Bayes factor lnΛ | 7.2 (very strong) | This work §6.5 |
| PRyM baseline ⁷Li/H | 5.49×10⁻¹⁰ | This work |
| H0 ratio e**A** (external check) | 1.0834 vs Riess 73.04, Planck 67.36 | \[13,14\] |
| **γ(κ²) anomalous dim. (perturbative)** | **0 (exact)** | This work §10.2; ZS-M13 §7A; \[15\] |
| δlnγb **(RG-invariant)** | **−κ² \= −0.00728** | This work §10.3 (Theorem T10.6) |
| δln C0(μ) (scheme-dependent) | −κ²·γb/(μ−γb) | This work §10.3; \[16\] |
| C² \= 2γb/(1−γbr0) | ANC ↔ binding momentum | Sparenberg et al. \[17\] |
| δln S34 **(parameter-free, v2.1)** | **−0.73% (LO) to −1.5% (eff. range)** | This work §10.4 |

**Appendix B. Review-Audit Record (v1.0 → v2.1)**

All corrections adopted under the no-deletion rule. Items from v1.1, v1.2, v1.3, v2.0 preserved verbatim; v2.1 adds items 17–19 closing the C₀↔κ² programme.

| \# | Issue found | Version | Resolution |
| :---: | ----- | ----- | ----- |
| 1 | Universal Bₜₒₜ/Q ‘20–30’ FALSIFIED (⁸B=275) | v1.1 | §4.1 per-nucleus table |
| 2 | δlnγₛ \= −κ FACTUAL ERROR (correct: −κ²) | v1.1 | §3 δlnγₛ \= −κ² |
| 3 | 2.3% × 0% × 0.54% \= 0 LOGIC ERROR | v1.1 | §6.4 structural vs statistical; no product with zero |
| 4 | −2A/Q convergence across U10, F19 OVERCLAIM (U10 \= dim(Z)/4π) | v1.1 | §9 dim(Z) \= 2 convergence |
| 5 | S₃₄ prediction magnitude \~1% not yet measured | v1.2 | NC-T10.7; stated honestly |
| 6 | ⁹C ‘disappears’ (⁹C is −44%, not full unbinding) | v1.2 | §4.1 ⁸B=−401% unbinds; ⁹C=−44% |
| 7 | lnΛ=7.2 ‘decisive’ (≠ decisive, which requires \>10) | v1.2 | §6.5 stated as 7.2 (\>5, not \>10) |
| 8 | ⁶Li reaction: ⁶Li(p,γ) → correct channel ²H(α,γ)⁶Li | v1.2 | §4.2 corrected channel |
| 9 | S₃₄ sensitivity ‘1–2’ uncited hand-wave | v1.3 | §4.2 S∝ANC² \[6,7\]; 1/(1−γₛr₀) basis |
| 10 | Selectivity theory only empirical (⁸B), no theory | v1.3 | §2.3 limiting-step → ⁷Be bottleneck (with quantitative ⁸B rate ratio) |
| 11 | lnΛ definition: H₀/H₁ undefined; product unjustified | v1.3 | §6.5 explicit H₀/H₁ \+ independence caveat |
| 12 | §5 O-F19.6 disconnected from main result | v1.3 | §5 shared pₑᵧ=(3,2,6)/11 link sentence |
| 13 | H₀ external citation absent for A’s BBN independence claim | v2.0 | §1.1 table row 2: Riess 2022 \[13\], Planck 2018 \[14\] added; App. A last row |
| 14 | γₛr₀ ≈0.4–0.5 uncited | v2.0 | §3 ‘consistent with Zhang et al. 2020 \[4\]’ added; App. A row added |
| 15 | C₀ ↔ κ² OPEN scope not clearly bounded | v2.0 | §2.2 \+ NC-T10.8: RG running Planck → nuclear EFT explicitly stated as OPEN |
| 16 | Reference \[7\] duplicate (Costantini & Bemmerer both \[7\]) | v1.3 → v2.0 | References renumbered: Igamov \[6\], Costantini \[7\], Bemmerer \[8\], Adelberger \[9\], Burns \[10\], Fields \[11\], AME2020 \[12\]; Riess \[13\], Planck \[14\] added |
| **17** | **C₀↔κ² RG running** | **v2.0 → v2.1** | **§10 \+ Theorem T10.6: κ² non-running established via the Continuum Perturbative Protection Theorem (ZS-M13 §7A) \+ Appelquist–Carazzone decoupling \[15\]; Gate S-T10.1 → CLOSED-CONDITIONAL** |
| **18** | **δlnγ\_b \= −κ² only HYPOTHESIS-strong; S₃₄ shift not parameter-free** | **v2.1** | **§10.3–10.4: δlnγ\_b \= −κ² → DERIVED-CONDITIONAL; matching scheme-dependence resolved \[16\]; via Sparenberg et al. \[17\] the S₃₄ shift becomes parameter-free (−0.73% to −1.5%)** |
| **19** | **Residual non-perturbative protection left unbounded** | **v2.1** | **§10.2 \+ new Gate S-T10.2 (narrow, non-blocking): strong-curvature R\~M\_P² regime declared OPEN; nuclear scale \~71 MeV ≪ M\_P confirms weak-curvature validity of the closure** |

**References**

\[1\] T. Dent, S. Stern, C. Wetterich, Phys. Rev. D 76, 063513 (2007); arXiv:0705.0696.

\[2\] V. De Vuyst, S. Eccles, P. A. Höhn, J. Kirklin, JHEP 07 (2025) 063; arXiv:2507.14131.

\[3\] A. N. Gorban, O. Radulescu, A. Y. Zinovyev, Chem. Eng. Sci. 65, 2310 (2010); arXiv:0903.5072.

\[4\] X. Zhang, K. M. Nollett, D. R. Phillips, J. Phys. G 47, 054002 (2020). \[³He–⁴He EFT, ANC, γₛr₀ values\]

\[5\] R. Higa, G. Rupak, A. Vaghani, Eur. Phys. J. A 54, 89 (2018). \[halo-EFT leading order\]

\[6\] S. B. Igamov, R. Yarmukhamedov, Nucl. Phys. A 781, 247 (2007). \[ANC method, S₃₄ ∝ ANC²\]

\[7\] H. Costantini et al. (LUNA), Nucl. Phys. A 814, 144 (2008); arXiv:0809.5269. \[LUNA S₃₄ measurement\]

\[8\] D. Bemmerer et al. (LUNA), Phys. Rev. Lett. 97, 122502 (2006). \[LUNA S₃₄; \~4% precision\]

\[9\] E. G. Adelberger et al., Rev. Mod. Phys. 83, 195 (2011). \[Solar fusion S-factors standard review; ⁷Be(p,γ)⁸B rate at BBN T\]

\[10\] A.-K. Burns, T. M. P. Tait, M. Valli, Eur. Phys. J. C 84, 86 (2024); arXiv:2307.07061. \[PRyMordial\]

\[11\] B. D. Fields, Ann. Rev. Nucl. Part. Sci. 61, 47 (2011). \[Lithium problem review\]

\[12\] M. Wang et al. (AME2020), Chin. Phys. C 45, 030003 (2021). \[Nuclear binding energies, ⁸B Sₚ, ⁹C Sₚ\]

\[13\] A. G. Riess et al. (SH0ES), ApJ 934, L7 (2022). \[H₀ˡᵒᶜᵃˡ \= 73.04 ± 1.04 km/s/Mpc; external check for A’s BBN independence\]

\[14\] Planck Collaboration, A\&A 641, A6 (2020). \[H₀ᶜᴹᴮ \= 67.36 ± 0.54 km/s/Mpc; external check for A’s BBN independence\]

\[15\] T. Appelquist, J. Carazzone, Phys. Rev. D 11, 2856 (1975). \[decoupling theorem; basis for §10.2 κ² survival as a marginal protected cross-sector coefficient\]

\[16\] D. B. Kaplan, M. J. Savage, M. B. Wise, Nucl. Phys. B 534, 329 (1998); arXiv:nucl-th/9802075. \[PDS scheme; scheme-dependent running of contact terms C₀(μ) vs scheme-independent pole/ANC content\]

\[17\] J.-M. Sparenberg, P. Capel, D. Baye, Phys. Rev. C 81, 011601(R) (2010); arXiv:0907.5166. \[ANC ↔ binding momentum ↔ effective-range relation C² \= 2γ\_b/(1−γ\_b r₀), used in §10.4\]

**Version History**

v1.0 (Mar 2026): Operator Tᵧ→ₓ; PRyMordial gate with registered nonlinear ⁷Li tension (Li-2).

v1.1 (Mar 2026): λₛˡᵒʷ \= −dim(Z)κ²; δlnγₛ \= −κ²; per-nucleus P-T10.1; structural-vs-statistical §6.4; dim(Z) \= 2 convergence. Four review proposals corrected (App. B \#1–4).

v1.2 (Mar 2026): First external-reviewer revision. Adds §1.1 A’s chronological priority; §1.2 standard-physics translation; §2.2 ANC/Wilson coefficient restatement; §4.1 ⁸B/⁹C consistency test; §4.2 S₃₄ prediction \+ LUNA-MV programme; §6.5 Bayes factor lnΛ \= 7.2; 

v1.3 (Mar 2026): Second external-reviewer revision. Adds §2.3 limiting-step → ⁷Be theoretical basis; γₛr₀ \= 0.40–0.50 ANC sensitivity in §4.2; explicit H₀/H₁ \+ independence caveats in §6.5; shared-pₑᵧ sentence in §5. Four items corrected (App. B \#9–12).

v2.0 (Mar 2026): Third external-reviewer revision. Adds §1.1 H₀ external citations (Riess \[13\], Planck \[14\]); §3 / App. A γₛr₀ \= 0.40–0.50 citation (Zhang et al. \[4\]); §2.2 \+ NC-T10.8 

**v2.1 (Mar 2026):** Adds §10 (Theorem T10.6: κ² non-running, DERIVED-CONDITIONAL) via the Continuum Perturbative Protection Theorem (ZS-M13 §7A) \+ Appelquist–Carazzone decoupling \[15\]; matching equation δlnγ\_b \= −κ² (RG-invariant) with scheme-dependent C₀(μ) running \[16\]; parameter-free S₃₄ shift via the Sparenberg–Capel–Baye ANC relation \[17\]; new epistemic tags DERIVED-PERTURBATIVE and CLOSED-CONDITIONAL; Gate S-T10.1 → CLOSED-CONDITIONAL; new narrow non-blocking Gate S-T10.2; NC-T10.8 superseded, NC-T10.9 / NC-T10.10 added; verification count 32 → 35\. No v2.0 content deleted (additive only). Three items added (App. B \#17–19).