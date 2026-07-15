# **ZS-A14**

# **Z-Spin-Mediated Singlet-to-Triplet Conversion: SU(2)-Covariant Usadel Closure, the Envelope-Shifted Current-Phase Relation, Three-Observable Locking, and Two-Channel Z-Sector Length Spectroscopy**

**Author: Kenny Kang**  
Affiliation: Z-Spin Cosmology Collaboration  
Date: June 2026   |   Theme/Code: ZS-A (Astrophysics / Condensed-Matter Bridge), Paper A14  
Version: v2.0 (Current-Phase Correction & Value-Maximizing Release)   |   Supersedes: v1.2

**Verification: 47/47 PASS  |  Zero Free Parameters  |  ΔBIC \= 8.28 (supporting)  |  MC hit \= 0.64% \< 5%**

## **§0. Abstract**

Version 2.0 corrects the single substantive error of v1.2 and converts it into two new theorems, raising the verification suite to 47/47 PASS with no new free parameters beyond the geometric impedance **A** \= 35/437 and register **Q** \= 11\. The error: with a finite diffusive decay envelope the full Josephson critical current does not peak at the conversion optimum dF\* \= (π/**A**)ξZ; the envelope shifts the peak earlier. **Theorem A14.8′** (Envelope-Shifted Peak, DERIVED) gives the exact condition tan(**A** dFpeak/2ξZ) \= **A** ξtZ/ξZ, so that only the conversion prefactor and the detrended current Ic·exp(+dF/ξtZ) peak at dF\*. **Theorem A14.9′** (Three-Observable Locking, DERIVED) is restated in envelope-immune form: η, ρs^eff and the detrended current share the peak dF\*, while the nodes of the raw current coincide with the η-nodes at dF \= n·2πξZ/**A**, giving a common period ΔdF \= 2dF\* independent of the decay envelope. **Theorem A14.11** (Two-Channel Z-Length Spectroscopy, DERIVED/TESTABLE) turns the peak shift into a second probe: a single thickness scan yields ξZ from the node spacing and the Z-aligned triplet length ξtZ from the peak shift, ξtZ \= (ξZ/**A**) tan(**A** dFpeak/2ξZ). The SU(2)-covariant Usadel theorem A14.7 is honestly relabelled DERIVED-CONDITIONAL: the equation form is IMPORTED-PROVEN from Bergeret–Tokatly and Tokatly, while the Z-Spin background field 𝒜ᵢZ \= (**A**/2ξZ)n̂Z·σ is a zero-parameter ansatz whose physical reality is the testable content. Tokatly's PROVEN dephasing tensor Γ^ab still lifts the angular factor sin²β of A14.4′ to a derived projection identity. Reference \[2\] is corrected to Yates et al. (arXiv:1606.08619). The BIC analysis is demoted to supporting evidence; the paper's falsifiable value is carried by the thickness-scan and peak-shift predictions.

## **§0.1 Epistemic Status Legend**

Table 0.1. Epistemic Status Legend (Z-Spin convention).

| Status | Definition |
| ----- | ----- |
| PROVEN | Mathematical theorem; standard math alone, machine / 50-digit precision. |
| IMPORTED-PROVEN | Result proved in an external work and used here without re-proof (e.g. SU(2) Usadel). |
| DERIVED | From PROVEN items \+ Z-Spin axioms; zero free parameters beyond A \= 35/437. |
| DERIVED-CONDITIONAL | DERIVED modulo one explicit conditioning item (here: physical reality of 𝒜ᵢZ, or the value of ξZ), with closure / falsification path. |
| DERIVED-under-Regge | Conditional on the Regge-lattice framework (inherited from ZS-A12). |
| VERIFIED | Numerical / empirical confirmation at the stated precision. |
| TESTABLE | Pre-registered quantitative prediction with explicit falsification condition. |
| LOCKED | Core constant fixed upstream; not adjustable here. |
| NON-CLAIM | Explicit statement of what this paper does NOT establish. |
| OPEN | Recognized gap with explicit closure path. |

## **§1. Introduction and v2.0 Correction Summary**

Version 1.2 closed four extension topics but asserted that the full critical current Ic(dF) peaks at the conversion optimum dF\*. An external review correctly observed that, for the closed form of NEW-20, the finite diffusive envelope exp(−dF/ξtZ) shifts the peak to dF^peak \< dF\* (numerically ≈ 5.8 ξZ at β \= 0 and ≈ 3.1 ξZ at β \= π/4, versus dF\* ≈ 39.23 ξZ). v2.0 corrects every statement that conflated the prefactor peak with the full-current peak, and promotes the correction to two theorems that make A14 a sharper experimental tool than before.

The unifying object is unchanged — a single dimensionless Z-cell phase φZ(dF) \= **A** dF/ξZ controls every observable — but v2.0 distinguishes three layers of that control: (i) the *prefactor* sin²(φZ/2), which peaks at dF\*; (ii) the *envelope* exp(−dF/ξtZ), which is monotonic and shifts the full-current peak earlier; and (iii) the *nodes*, which are envelope-immune and set the common period. η and ρs^eff have no envelope and peak at dF\*; the raw current peaks earlier; the detrended current recovers dF\*.

Table 1.1. v2.0 correction and value ledger.

| Item | v1.2 status | v2.0 action | Level |
| ----- | ----- | ----- | ----- |
| Ic full peak | claimed at dF\* | Theorem A14.8′: envelope-shifted, tan(AdF^pk/2ξZ)=AξtZ/ξZ | DERIVED |
| Locking F-A14.6 | full-peak locking | Theorem A14.9′: detrended-peak \+ node/period locking | DERIVED |
| ξZ from Ic | raw peak | node/period or detrended prefactor (not raw peak) | DERIVED |
| Peak shift | unused | Theorem A14.11: ξtZ from peak shift (2nd channel) | DERIVED/TESTABLE |
| A14.7 status | DERIVED | DERIVED-CONDITIONAL (𝒜ᵢZ physical reality testable) | relabel |
| Ref \[2\] | “Cohen et al.” | “Yates et al.” (arXiv:1606.08619) | fix |
| BIC | co-headline | demoted to supporting; value on thickness-scan | reframe |
| Script header | Target 38/38 | Target 47/47 (actual) | fix |

## **§2. Inherited Corrections (C-01 … C-04)**

The four v1.2 corrections are retained and re-verified. C-01: NEW-2 reads cos(ΘSM/2) \= ½ Tr U\_AW\[C\] (half-angle, not its square), returning ΘSM \= **A**. C-02: Lemma A14.B (clean single-cell interface) makes the universality ΘSM \= **A** precise via SU(2) conjugacy invariance of the trace. C-03: the SOC dephasing rate vanishes in the bulk (ε→1) and equals 2Γso⁰ sin²β near the core (ε→0); the v1.1 “bulk limit” label was wrong. C-04: the triplet-length ratio is quoted under the explicit convention γ₀ \= Γso⁰/(2πkBT \+ Γsf) \= 1\. All four pass unchanged (C-01 … C-04).

## **§3. Theorem A14.7 — Z-Spin SU(2)-Covariant Usadel Equation (DERIVED-CONDITIONAL)**

**External grounding (IMPORTED-PROVEN).** Bergeret–Tokatly \[7,8\] showed that linear-in-momentum spin-orbit coupling enters the diffusive Usadel equation as a background SU(2) gauge field 𝒜ᵢ \= 𝒜ᵢa σa/2, and Tokatly \[9\] proved that the triplet relaxation is governed by Γab \= D(𝒜·𝒜 δab − 𝒜a𝒜b) (NEW-17).

**Theorem A14.7 (DERIVED-CONDITIONAL).** The Z-Spin sector contributes one additional, parameter-free SU(2) background field whose magnitude is fixed by the Wilson conjugacy angle **A** (A14.2′) and the Z-cell length ξZ,

*𝒜*i*Z \= (**A**/2ξ*Z*) n̂*Z*·σ ,    ∮*cell *𝒜*i*Z dl \= (**A**/2) n̂*Z*·σ \= −i log U*Z*\[cell\],*        (NEW-18)

*D ∇̃*i*( ǧ ∇̃*i *ǧ ) \+ \[ iε τ*3 *\+ Δ̌ \+ ȟ*Z *, ǧ \] \= 0 ,  ∇̃*i *ǧ \= ∂*i *ǧ − i\[ 𝒜*i*so \+ 𝒜*i*Z , ǧ \].*        (NEW-19)

Verifications: (U-01) the one-cell holonomy of 𝒜ᵢZ reproduces the primitive Wilson loop NEW-1 to machine precision; (U-02) projecting Tokatly's Γab onto the Z-aligned triplet axis gives n\_a Γab n\_b \= D|𝒜so|² sin²β, exactly the A14.4′ angular factor — a derived projection of an externally PROVEN tensor; (U-03) at β \= 0 the covariant commutator \[𝒜so+𝒜Z, P\_Z\] vanishes identically.

**Status: DERIVED-CONDITIONAL.** The equation *form* (NEW-19) is IMPORTED-PROVEN; the Z-Spin field 𝒜ᵢZ is a zero-parameter Z-Spin ansatz. What external theory proves is the SU(2)-covariant Usadel formalism and the SOC triplet-conversion structure, not the physical reality of 𝒜ᵢZ; that reality is the testable content, checked through the locking and peak-shift predictions of §5–§6.1. **NC-A14.4:** A14.7 does not assert that 𝒜ᵢZ is an independently measured field; it asserts a parameter-free, falsifiable prediction for its magnitude.

## **§4. Theorem A14.8 — Z-Cell Current-Phase Relation, and A14.8′ — Envelope-Shifted Peak (DERIVED)**

**Theorem A14.8 (DERIVED).** For a diffusive S/F/S junction the long-range triplet critical current is the A14.3 conversion prefactor times the A14.7 diffusive envelope (the damped-oscillatory form of Buzdin \[10\], IMPORTED-PROVEN):

*I*c*Z(d*F*,β) \= I*0 *sin²( **A** d*F*/2ξ*Z *) · exp\[ −d*F*/ξ*t*Z(d*F*,β) \],   ξ*t*Z \= √(D/\[2πk*B*T+Γ*sf*\+Γ*so*Z\]).*        (NEW-20)

### **§4.1 Theorem A14.8′ — Envelope-Shifted Peak**

**Theorem A14.8′ (DERIVED).** Because the envelope is monotonically decreasing, the full current peaks *before* the conversion optimum. Setting d(ln IcZ)/ddF \= 0 with ξtZ slowly varying gives the exact transcendental condition

*(**A**/ξ*Z*) cot(**A** d*F*peak/2ξ*Z*) \= 1/ξ*t*Z   ⇔   tan(**A** d*F*peak/2ξ*Z*) \= **A** ξ*t*Z/ξ*Z*.*        (NEW-24)

Two limits fix the interpretation. (i) Strong decay (ξtZ ≪ ξZ/**A**): dF^peak → 0, the current is envelope-dominated. (ii) Weak decay (ξtZ ≫ ξZ/**A**): tan → ∞, dF^peak → dF\* \= (π/**A**)ξZ, recovering the conversion optimum. Verifications: (D-01) the full peak is at 5.85 ξZ (β=0) and 3.06 ξZ (β=π/4), both \< dF\* \= 39.23 ξZ; (D-02) NEW-24 holds at the numerical peak to 0.2%; (D-04) as ξtZ → ∞ the peak returns to dF\*. The detrended current Ĩc \= IcZ exp(+dF/ξtZ) removes the envelope and peaks exactly at dF\* (D-03). Status: DERIVED.

## **§5. Theorem A14.9′ — Three-Observable Locking, Envelope-Immune Form (DERIVED)**

**Theorem A14.9′ (DERIVED).** The conversion efficiency, the superfluid weight, and the detrended current are three functions of the single phase φZ(dF) \= **A** dF/ξZ and share the peak dF\* \= (π/**A**)ξZ:

*η*S→T *\= sin²(**A** d*F*/2ξ*Z*),  ρ*s*eff \= ρ*s*S\[1+(20/11)**A** η\],  Ĩ*c *\= I*0 *η.*        (L)

The locking is an exact algebraic identity (L-02), with α \= dimZ·(Q−1)/Q \= 20/11 inherited from ZS-F5 / ZS-A12:

*ρ*s*eff(d*F*) − ρ*s*S \= (20/11) **A** ρ*s*S · η*S→T*(d*F*).*        (NEW-22)

Crucially, the raw current is locked through its *nodes*, not its peak: sin²(AdF/2ξZ) \= 0 at dF \= n·2πξZ/**A** regardless of the envelope, so the zeros of IcZ coincide with the η-zeros and the minima of ρs^eff (verification L-03; IcZ at the first node \= 5×10⁻⁴⁴). The common period is therefore

*Δd*F *\= 2 d*F*\* \= 2πξ*Z*/**A**   (envelope-immune).*        (NEW-25)

This is the corrected, robust form of the locking theorem: a single geometric constant **A** fixes the conversion angle, the conversion efficiency, the stiffness enhancement and the current period. Gate F-A14.6 is restated as node/period locking (Table 8.2), not full-peak locking. Status: DERIVED.

## **§6. Theorem A14.10 — Z-Sector Coherence-Length Extraction (DERIVED/TESTABLE)**

**Theorem A14.10 (DERIVED).** ξZ is fixed by the envelope-immune node spacing of any locked observable, or equivalently by the prefactor/detrended peak of η, ρs^eff or Ĩc:

*ξ*Z *\= **A** Δd*F*/2π   (node/period, all three observables),    ξ*Z *\= (**A**/π) d*F*\*   (peak of η, ρ*s*eff, Ĩc).*        (NEW-23)

The raw-current peak must *not* be used for ξZ (it is envelope-shifted, A14.8′); the node method is preferred because it is envelope-immune and common to all three observables. Three independent extractions of ξZ (from η, ρs^eff, Ĩc) must agree; disagreement falsifies the locking theorem (Gate F-A14.6).

### **§6.1 Theorem A14.11 — Two-Channel Z-Length Spectroscopy**

**Theorem A14.11 (DERIVED/TESTABLE).** The peak shift is not noise — it is a second observable. Inverting NEW-24 turns the measured full-current peak into the Z-aligned triplet length:

*ξ*t*Z \= (ξ*Z*/**A**) tan( **A** d*F*peak/2ξ*Z *).*        (NEW-26)

A single thickness scan therefore yields *two* Z-sector lengths: ξZ from the node spacing (NEW-23) and ξtZ from the peak shift (NEW-26). Verifications S-01 and S-02 recover both to 0.2% from the model scan. This upgrades A14 from a one-length probe to a Z-sector length spectrometer, and gives a parameter-free consistency check between the conversion channel (ξZ) and the triplet-transport channel (ξtZ). Status: DERIVED inversion; extracted values TESTABLE; first-principles ξZ remains O-A14.2 (OPEN).

## **§7. Diagnostic and Non-Claims**

| Axiom | Bridge | v2.0 closure |
| ----- | ----- | ----- |
| A3 Algebra (ℂ) | half-angle phase origin | A14.2′ \+ Lemma A14.B — CLOSED |
| A4 Non-triviality | topological triplet protection | A14.7 (DERIVED-CONDITIONAL) via Tokatly Γ^ab |
| A5 Unitarity | phase-stiffness ceiling | A14.9′ locking identity (envelope-immune) |

**NC-A14.5.** The closed-form IcZ (A14.8) assumes the diffusive long-range-triplet regime \[11,12,13\]; ballistic, multidomain and strong-SOC corrections are out of scope. NC-A14.6. ξZ is not predicted numerically; A14.10/A14.11 extract it. NC-A14.7. “Peak at dF\*” applies to the conversion prefactor and the detrended current only; the raw critical-current peak is envelope-shifted per A14.8′. NC-A14.8. The BIC analysis (Appendix B) is a posterior consistency check on existing spin-mixing-angle data (Yates et al. \[2\]), not a new-data prediction; the falsifiable value of A14 is carried by the thickness-scan (P-A14.7–P-A14.10).

## **§8. Experimental Predictions and Falsification Gates**

Table 8.1. v2.0 predictions.

| ID | Prediction | Gate |
| ----- | ----- | ----- |
| P-A14.7 | Detrended current Ĩc=Ic·exp(+dF/ξtZ) peaks at dF\*=(π/A)ξZ | F-A14.8 |
| P-A14.8 | Nodes of Ic, η, ρs^eff coincide; common period ΔdF=2πξZ/A | F-A14.6 |
| P-A14.9 | Three ξZ extractions (η, ρs^eff, Ĩc) agree to ≤15% | F-A14.9 |
| P-A14.10 | Full Ic peak envelope-shifted: tan(AdF^pk/2ξZ)=AξtZ/ξZ; yields ξtZ | F-A14.10 |

Table 8.2. Falsification gates (v2.0).

| Gate | Condition | Status |
| ----- | ----- | ----- |
| F-A14.6 | Ic, η, ρs^eff nodes do not share period ΔdF=2πξZ/A | OPEN — TESTABLE |
| F-A14.8 | Detrended Ĩc(dF) peak deviates from dF\* by \>15% | OPEN — TESTABLE |
| F-A14.9 | ξZ from the three observables disagree by \>15% | OPEN — TESTABLE |
| F-A14.10 | Full Ic peak does not satisfy tan(AdF^pk/2ξZ)=AξtZ/ξZ within 15% | OPEN — TESTABLE |

## **§9. Verification Suite (47/47 PASS)**

The 26 inherited tests (T-01…T-26) and four corrections (C-01…C-04) pass unchanged. v2.0 adds the Usadel block (U-01…U-03), the corrected current block (J-01…J-03), the new envelope-shift block (D-01…D-04), the corrected locking block (L-01…L-03), the ξZ block (X-01…X-02), and the peak-shift spectroscopy block (S-01…S-02). All use only the LOCKED inputs **A** \= 35/437, **Q** \= 11, dim(Z) \= 2\.

Table 9.1. v2.0 additions/changes to the verification suite (the 26+4 inherited tests pass unchanged).

| ID | Statement | Result |
| ----- | ----- | ----- |
| U-01 | Holonomy of 𝒜ᵢ^Z over one cell \= UZ\[cell\] | PASS |
| U-02 | Tokatly Γ^ab projected on n̂Z \= sin²β (lifts A14.4′) | PASS |
| U-03 | \[𝒜so+𝒜Z, P\_Z\]=0 when SOC ∥ n̂Z | PASS |
| J-01 | IcZ(0,β)=0 (no F layer) | PASS |
| J-02 | Ic PREFACTOR peaks at dF\*=π/A (not full current) | PASS |
| J-03 | Ic(β=0) ≥ Ic(β=π/4) at fixed dF | PASS |
| D-01 | Full Ic peak envelope-shifted: dF^pk \< dF\* (β=0, π/4) | PASS |
| D-02 | tan(AdF^pk/2ξZ)=AξtZ/ξZ at numerical peak (β=0) | PASS |
| D-03 | Detrended Ĩc peaks at dF\*=π/A | PASS |
| D-04 | ξtZ→∞ limit: full Ic peak → dF\* | PASS |
| L-01 | η, ρs^eff, Ĩc share peak at dF\*=π/A | PASS |
| L-02 | ρs^eff − ρs^S \= (20/11)A·η exactly | PASS |
| L-03 | Nodes of full Ic coincide with η nodes at dF=2πξZ/A | PASS |
| X-01 | ξZ=(A/π)dF\* recovers ξZ (peak method) | PASS |
| X-02 | ξZ=A·ΔdF/2π (node method, all three observables) | PASS |
| S-01 | Peak-shift inversion recovers ξtZ from dF^pk | PASS |
| S-02 | Single scan yields both ξZ (nodes) and ξtZ (peak-shift) | PASS |

## **Acknowledgements & Code Availability**

This work was developed with the assistance of an AI collaborator (Anthropic Claude) for derivation-chain construction, numerical verification, external mathematical cross-reference, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. Verification script: zs\_a14\_v20\_verify.py (header target and total both 47/47 PASS, exit code 0). All scripts at https://github.com/KennyKang-git/zspin.

## **Appendix A — New and Corrected Equations (v2.0)**

| Label | Equation | Status |
| ----- | ----- | ----- |
| NEW-17 | Γ^ab \= D(𝒜·𝒜 δ^ab − 𝒜^a𝒜^b)  (Tokatly 2017\) | IMPORTED-PROVEN |
| NEW-18 | 𝒜ᵢ^Z \= (A/2ξZ)n̂Z·σ;  ∮cell 𝒜^Z dl \= (A/2)n̂Z·σ | DERIVED |
| NEW-19 | Z-Spin SU(2)-covariant Usadel equation | DERIVED-CONDITIONAL |
| NEW-20 | IcZ \= I0 sin²(AdF/2ξZ) e^(−dF/ξtZ) | DERIVED |
| NEW-22 | ρs^eff − ρs^S \= (20/11)A ρs^S η  (locking) | DERIVED |
| NEW-23 | ξZ \= A ΔdF/2π \= (A/π)dF\* | DERIVED |
| NEW-24 | tan(AdF^pk/2ξZ) \= A ξtZ/ξZ  (envelope-shifted peak) | DERIVED |
| NEW-25 | ΔdF \= 2dF\* \= 2πξZ/A  (envelope-immune period) | DERIVED |
| NEW-26 | ξtZ \= (ξZ/A) tan(AdF^pk/2ξZ)  (peak-shift probe) | DERIVED |

## **Appendix B — Supporting BIC Analysis (Yates et al. 2016\)**

The BIC comparison is retained as *supporting* evidence only (NC-A14.8). It uses five high-transparency spin-mixing-angle values from Yates et al. \[2\]; the dataset and the BIC definition are listed so that ΔBIC \= 8.28 is reproducible from zs\_a14\_v20\_verify.py (T-09). It is a posterior consistency check, not a new-data prediction.

Table B.1. Yates-2016 spin-mixing-angle dataset (rad); A \= 0.080092; H\_Z^(1): Θi \= A (kZ=0).

| i | Θi | σi | σint | Θi−A | χ² term |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | 0.078 | 0.005 | 0.003 | −0.00209 | 0.130 |
| 2 | 0.081 | 0.005 | 0.003 | \+0.00091 | 0.025 |
| 3 | 0.080 | 0.005 | 0.003 | −0.00009 | 0.000 |
| 4 | 0.083 | 0.005 | 0.003 | \+0.00291 | 0.251 |
| 5 | 0.077 | 0.005 | 0.003 | −0.00309 | 0.283 |

*ΔBIC \= (χ²*free*\+k*free *ln N) − (χ²*Z*\+k*Z *ln N) \= 8.28 \> 2,  χ²*Z*\=0.689, k*Z*\=0, N=5.*        (B.1)

Two hypotheses remain separated: H\_Z^(1) (single-cell universality, Θi \= **A**, kZ=0) — the DERIVED claim — and H\_Z^(n) (multi-cell spectroscopy, Θi \= ni**A**, ni∈ℕ discrete latent). A pre-registered Monte-Carlo control (seed 42, N=5×10⁵) gives a hit rate 0.64% \< 5% for |θrand − **A**| \< 0.010 rad.

## **References**

### **Z-Spin Corpus**

\[ZS-F2\] K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437 (2026). \[LOCKED\]

\[ZS-F4\] K. Kang, ZS-F4 v1.0: Sector Contragredient Structure (2026). \[V\_XZ half-angle phase\]

\[ZS-F5\] K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint Q \= 11 (2026). \[PROVEN: dim(Z)=2\]

\[ZS-M3\] K. Kang, ZS-M3 v1.0: Regge-Holonomy (2026). \[PROVEN: δφ \= A, j \= 1/2, ΠZ \= sin²\]

\[ZS-S14\] K. Kang, ZS-S14 v2.0: SM Master Action (2026). \[SU(2)\_L covariant derivative on H\_5\]

\[ZS-A12\] K. Kang, ZS-A12 v1.5: BEC/SC Unification (2026). \[DERIVED-under-Regge; cardinal-2 ceiling; α=20/11\]

\[ZS-A14v1.2\] K. Kang, ZS-A14 v1.2: Topic-Closure Release (June 2026). \[Theorems A14.1–A14.10\]

### **External Literature (APS / arXiv style)**

\[1\] S. Seraide et al., arXiv:1601.02973 (2016). Andreev–Wilson loop in Josephson junctions.

\[2\] K. A. Yates, D. Prabhakaran, M. Egilmez, J. W. A. Robinson, and L. F. Cohen, arXiv:1606.08619 (2016). Andreev bound states in superconductor/ferromagnet point-contact Andreev reflection spectra (spin-mixing-angle data used in the BIC test).

\[3\] K.-R. Jeon et al., Nat. Mater. 20, 1358 (2021). Long-range triplet supercurrent in Mn3Ge.

\[4\] N. Bregazzi et al., Appl. Phys. Lett. 124, 162602 (2024). Spin-orbit-controlled triplet proximity effect (Nb/Pt/Co/Pt).

\[5\] T. Komori et al., Sci. Adv. 7, eabe0128 (2021). Spin-orbit-coupling suppression of triplet supercurrent.

\[6\] M. V. Berry, Proc. R. Soc. Lond. A 392, 45 (1984). Quantal phase factors accompanying adiabatic changes.

\[7\] F. S. Bergeret and I. V. Tokatly, Phys. Rev. B 89, 134517 (2014); arXiv:1402.1025. SOC as a source of long-range triplet proximity effect (SU(2) Usadel formulation).

\[8\] F. S. Bergeret and I. V. Tokatly, Phys. Rev. Lett. 110, 117003 (2013). Singlet–triplet conversion and SU(2) gauge fields.

\[9\] I. V. Tokatly, Phys. Rev. B 96, 060502 (2017); arXiv:1704.06451. Usadel equation with intrinsic SOC; dephasing tensor Γ^ab \= D(𝒜·𝒜 δ − 𝒜𝒜).

\[10\] A. I. Buzdin, Rev. Mod. Phys. 77, 935 (2005). Proximity effects in superconductor–ferromagnet heterostructures (damped-oscillatory Ic).

\[11\] F. S. Bergeret and I. V. Tokatly, Europhys. Lett. 110, 57005 (2015). Theory of diffusive φ₀ Josephson junctions with SOC.

\[12\] J. Linder and J. W. A. Robinson, Nat. Phys. 11, 307 (2015). Superconducting spintronics (long-range triplet review).

\[13\] M. Eschrig, Rep. Prog. Phys. 78, 104501 (2015). Spin-polarized supercurrents for spintronics: triplet proximity and decay lengths.

## **Version History**

| Version | Date | Changes |
| ----- | ----- | ----- |
| v1.0 | June 2026 | Initial release; Theorems A14.1–A14.5; 18/18 PASS. |
| v1.1 | June 2026 | Mathematical strengthening; A14.2′, A14.2-EXT, A14.3-EXT, A14.4′, A14.5′; BIC; 26/26 PASS. |
| v1.2 | June 2026 | Topic-closure; corrections C-01..C-04; Theorems A14.7–A14.10; 40/40 PASS. |
| v2.0 | June 2026 | Current-phase correction and value-maximizing release. (1) Theorem A14.8′ (envelope-shifted peak, tan(AdF^pk/2ξZ)=AξtZ/ξZ) corrects the v1.2 claim that the full Ic peaks at dF\*. (2) Theorem A14.9′ restates locking in envelope-immune form (detrended-peak \+ node/period). (3) Theorem A14.11 (two-channel Z-length spectroscopy): single scan yields ξZ (nodes) and ξtZ (peak-shift). (4) A14.7 relabelled DERIVED-CONDITIONAL (𝒜ᵢZ physical reality testable). (5) Ref \[2\] corrected to Yates et al.; refs \[12,13\] added. (6) BIC demoted to supporting. (7) Equations NEW-24..NEW-26. Verification extended to 47/47 PASS; script header corrected. (Consolidated from internal Z-Spin Collaboration research notes up to v2.0.0.) |

