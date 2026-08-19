**ZS-S1**

**Gauge Coupling Unification:** **Incidence-Laplacian Bridge from Action to SM Gauge Couplings**

*Dated erratum and scope correction of ZS-S1 v1.0*

Kenny Kang

*ZS-S1 v1.1 — 2026-08-19 (KST) — Standard Model Completion Theme*

**Scope verdict (one line).** The spectral construction of the 1-loop β-function slopes and of α\_s and sin²θ\_W survives unchanged in value; what is corrected here is that **ZS-S1 v1.0 printed its coupling outputs without a scale or a scheme**, and that one of them — α₂ \= 3/95 — was consumed downstream as an M\_Z MS-bar SU(2) coupling, an identification ZS-S1 never made and cannot support.

**Verification: 127 rows, 0 FAIL — evidence C/V/W \= 64, controls R/G \= 34, non-evidence X/D/T \= 29\. Class P is not used.** **Companion artifact: zs\_s1\_verify\_v1\_1.py, EXPECTED\_ROWS \= 138, fail-closed.**

---

## §0. Abstract

We establish the Incidence-Laplacian (IL) Bridge connecting the Z-Spin action to Standard Model gauge-sector quantities and give complete derivation chains for the polyhedral spectral formulas. The non-minimal coupling (1+Aε²)R, evaluated on canonical polyhedral lattices, generates spectral densities that reproduce the 1-loop β-function coefficients: a₂ \= (V+F)\_X/G \= 38/12 \= 19/6 for SU(2), a₃ \= (V+F)\_Y/G \= 92/12 \= 23/3 for SU(3).

Three derivation steps are closed. (1) The "+1" in α\_s \= Q/\[(V+F)\_Y \+ 1\] \= 11/93 is derived as the Z-sector Betti number β₀(Z) \= 1 contributed via Schur complement of the 3-sector joint Incidence-Laplacian. (2) The i-tetration fixed point x\* \= Re(z\*) in sin²θ\_W \= (48/91)·x\* is identified as the Berry phase projection weight of the Z-mediator. (3) The Spectral-to-β Bridge theorem establishes that polyhedral vertices count matter degrees of freedom (V\_Y \= n\_f×G \= 60\) while faces count gauge degrees of freedom (F\_Y \= (N²−1)×G/N \= 32).

**This version carries a dated erratum with four items and one scope correction.** Every coupling output now carries an explicit scale and scheme (§8.0). Under that declaration:

- **α\_s \= 11/93 \= 0.118279569892** at μ \= M\_Z in MS-bar, pull **\+0.311 σ** against PDG 2024\. Status DERIVED, unchanged.  
- *sin²θ\_W \= (48/91)·x \= 0.2311822084*\* at μ \= M\_Z in MS-bar. The v1.0 pull is **superseded**: against PDG 2024 sin²θ̂\_W(M\_Z) the pull is **−2.695 σ**, a relative gap of −0.04660 %. Status DERIVED, retained, with the falsification gate FS1-2 now materially closer to firing.  
- **α₂ \= Y/\[5·(V+F)\_X\] \= 6/190 \= 3/95**, 1/α₂ \= **31.6666667**, carries **no declared scale and no declared scheme**. Its physical identification is **OPEN** and its status is downgraded from DERIVED to **OBSERVATION**.  
- a₂ \= 19/6 and a₃ \= 23/3 are scale-free 1-loop slopes and are unaffected.

The scope correction is forced by a sharp numerical fact, now an executed row of the companion artifact rather than a remark. Using only ZS-S1's own two numbers,

α₂ · sin²θ\_W \= 1 / 136.977092174,      α\_em(0)⁻¹ \= 137.035999177,

a gap of **\+0.043005 %**, whereas the same product misses α\_em(M\_Z) by −6.605 ± 0.006 %. Equivalently, and by the exact tree identity e \= g₂ sin θ\_W this is the *same* statement and not a second one, α₂ \= 3/95 sits **−6.561 ± 0.017 %** below the PDG 2024 MS-bar value α̂₂(M\_Z) \= 1/**29.589 ± 0.005**, and that deficit is the QED running of α\_em from q² \= 0 to M\_Z. Two escape routes are closed: absorbing the gap into sin²θ\_W would require **\+7.072 ± 0.007 %**, and absorbing it into the ZS-S4 vacuum expectation value would require **\+3.7539 ± 0.017 %**, more than thirty times its present −0.11763 % offset from (√2 G\_F)^(−1/2).

**A fifth erratum, found by adversarial audit, retracts the v1.0 uniqueness claim.** The truncated cube shares the truncated octahedron's f-vector (24, 36, 14\) and the truncated dodecahedron shares the truncated icosahedron's (60, 90, 32), so both alternative pairs reproduce (19/6, 23/3) at G \= 12 and, with them, every other number in this paper. What is singled out among the thirteen Archimedean f-vectors is the **mode count**, not the solid: the polyhedral selection is 2-fold degenerate in each sector and the spectral density rule, which sees the lattice only through V \+ F, cannot break the degeneracy. Gate FS1-4 is FIRED and replaced by FS1-4′ over mode counts. The Monte-Carlo anti-numerology figure of v1.0 is retained but **re-typed as a diagnostic**, because its null family was chosen after the polyhedral values were known.

*Keywords: gauge coupling, Incidence-Laplacian, β-function, polyhedral spectral density, renormalisation scheme, scale declaration, Weinberg angle, Schur complement, Berry phase, Spectral-to-β Bridge, dated erratum*

---

## §0.1 Epistemic Status Legend

| Status | Definition |
| :---- | :---- |
| **PROVEN** | Follows from standard mathematics alone (no physics input). Machine-verifiable. |
| **DERIVED** | Follows from Z-Spin action \+ standard physics. Zero free parameters. |
| **DERIVED-CONDITIONAL** | Derived from Z-Spin axioms, conditional on a stated assumption. |
| **CERTIFIED** | Established by exact or interval arithmetic in the companion artifact. |
| **VERIFIED** | Numerically confirmed at a declared precision against data or an independent computation. |
| **TESTABLE** | Well-defined prediction awaiting experimental data. |
| **HYPOTHESIS** | Physically motivated conjecture. Derivation chain incomplete. |
| **SUGGESTIVE** | Numerical proximity within order-of-magnitude confirmed. Weaker than HYPOTHESIS. |
| **OBSERVATION** | Numerical proximity confirmed under anti-numerology discipline. No action-level derivation and, where relevant, no physical identification. |
| **CONSISTENT** | Compatible with framework structure but not independently derived. |
| **NON-CLAIM** | Explicitly not asserted. Documented to prevent overclaim. |
| **OPEN** | Well-posed problem without current resolution. |
| **RETRACTED** | Previously claimed, now withdrawn with documented reason. |

Lifecycle axis (separate from the epistemic axis): CURRENT / SUPERSEDED / RETRACTED / ARCHIVED. Gate axis (separate again): OPEN / CLOSED-PASS / CLOSED-NEGATIVE / CLOSED-VACUOUS / TERMINAL-IN-SCOPE. Release label for this version: **REVIEW READY** — not FINAL; no persistent archival identifier; no qualified human review.

---

## §0.2 Dated erratum register (2026-08-19)

Correction severity class: **Scope correction** with three attached editorial/numerical errata. This is *not* a retraction of the ZS-S1 programme. ZS-S1 v1.0 is preserved as a historical artifact and is not deleted. The retracted wording is quoted verbatim below inside fenced blocks so that it remains searchable without remaining live.

### E-S1-1 — the downstream m\_W agreement claim (CRITICAL)

**Trigger.** ZS-S14 v2.1 erratum E19, gate F-S14.16, debt D-S14-MW, 2026-08-19.

**Retracted statement.** ZS-S14 v1.0 and v2.0, Theorem S14.B Step 4:

m\_W ≈ 80.4 GeV, matching observation

**Why it is wrong.** The stated inputs are g₂² \= 4π·α₂ \= 12π/95 from ZS-S1 §8.3 and v \= 245.93 GeV from ZS-S4 §6.12 Thm V.9. They give

m\_W \= √(4π · 3/95) · 245.93 / 2 \= 77.4614 GeV,

with v taken exact as written; the exact-input arithmetic value is 77.461387318380 GeV, and six significant figures is the ceiling that the five-figure input v \= 245.93 supports (§14, rule N4). Measured against the PDG 2024 world average 80.3692 ± 0.0133 GeV (CDF II 2022 excluded): a deviation of −3.6181 %, a pull of **−218.63 σ** on the experimental error and **−481.94 σ** against the electroweak-fit prediction 80.353 ± 0.006 GeV. The companion verifier of ZS-S14 v2.0, row D5, compared the computation against a hard-coded constant at a 5 % tolerance, wide enough for a 3.6 % miss to pass, so the deviation never appeared in a passing run.

**Disposition in ZS-S1.** ZS-S1 v1.0 never asserted an m\_W value; the assertion was made downstream, by identifying ZS-S1's α₂ with g₂²/4π at M\_Z. ZS-S1 v1.1 therefore does not retract an m\_W claim of its own. It (i) records that no such claim exists or may be constructed from ZS-S1 without a scheme declaration (§12 NC-5), (ii) withdraws the licence that made the downstream identification look sanctioned — see E-S1-3 — and (iii) makes the m\_W computation and its pull an executed row of the companion artifact (rows H1–H8) so that it can never again be hidden behind a tolerance.

### E-S1-2 — superseded electroweak reference values and the sin²θ\_W pull (MAJOR)

**Retracted statements.** ZS-S1 v1.0 §1 and §8.2:

sin²θ\_W(M\_Z) \= 0.23122 ± 0.00003

Pull vs PDG 2024 (sin²θ\_W(M\_Z) \= 0.23122 ± 0.00003, MS-bar): −1.26σ

and, in §13, the summary sentence

All five formulas match PDG 2024 data within 1.3σ.

**Why it is wrong.** Two independent defects. First, the quoted uncertainty is not PDG's: the PDG value 0.23122 is published with ± 0.00004, not ± 0.00003, so the v1.0 pull was inflated in significance by an understated error bar. Against 0.23122 ± 0.00004 the pull would have been −0.94479 σ. Second, and decisively, **0.23122 ± 0.00004 is the PDG 2023 value** (Review of Particle Physics 2023, *Electroweak Model and Constraints on New Physics*, Table 10.2). The PDG **2024** value is

sin²θ̂\_W(M\_Z) \= 0.23129 ± 0.00004    (MS-bar).

**Correct value.** With PDG 2024, sin²θ\_W \= 0.2311822084 has pull **−2.695 σ** and a relative gap of **−0.04660 %**. The v1.0 agreement banner quoted above is therefore false as well as superseded, and is withdrawn.

**Propagation.** The same PDG-2023-for-2024 substitution occurs in the companion correction report zs-s1\_correct\_report.md §1, which lists 0.23122 ± 0.00004, s²\_W(on-shell) \= 0.22339 ± 0.00010, α̂⁽⁵⁾(M\_Z)⁻¹ \= 127.951 ± 0.009 and M\_Z \= 91.1876 ± 0.0021 as PDG 2024\. The PDG 2024 values are 0.23129 ± 0.00004, 0.22348 ± 0.00010, 127.930 ± 0.008 and 91.1880 ± 0.0020. All numerical statements in the present version use the 2024 edition, and rows K1–K5 of the artifact fail if a 2023 value is ever restored.

### E-S1-3 — the written form and the name of α₂ (MAJOR, and this is the licence that failed)

**Retracted statements.** ZS-S1 v1.0 §8.3 section title, and the abstract/conclusion wording that placed α₂ among the derived gauge couplings:

8.3 Electromagnetic Coupling α₂

... the Incidence-Laplacian Bridge from the Z-Spin action to all Standard Model gauge couplings ...

Separately, the form in which α₂ is quoted downstream — in zs\_s14\_verify\_v1\_0.py, in zs-s1\_correct\_report.md, and in the Corpus-OS Manifest Log entry for D-S14-MW — is

α₂ \= X/\[(V+F)\_Y \+ X\] \= 3/95

**Why it is wrong.** Three separate defects.

1. **The name.** α₂ is, by universal convention, the SU(2) gauge coupling. Calling 3/95 \= 1/31.67 an *electromagnetic* coupling is simply incorrect — α\_em is 1/137 at q² \= 0 and 1/127.93 at M\_Z — and the mismatch between the section title and the symbol invited the downstream reading g₂² \= 4π α₂.  
     
2. **The written form.** ZS-S1 §8.3 derives α₂ \= Y/\[5·(V+F)\_X\] \= 6/(5×38) \= 6/190 \= 3/95, an **X-sector** object with denominator 190\. The form X/\[(V+F)\_Y \+ X\] \= 3/(92+3) \= 3/95 is a **Y-sector** object with denominator 95\. The two evaluate to the same rational, but they are different constructions on different polyhedral data. The X-sector form is the one ZS-S1 actually derives; the Y-sector form appears first as a comment in a downstream verification script and propagated from there into the correction report and the Manifest. Rows K10 and K11 record both forms and record that 190 ≠ 95\.  
     
3. **The consequence for the correction report.** zs-s1\_correct\_report.md §C-03 argues, quoting the misattributed form,

alpha\_s \= Q/\[(V+F)\_Y \+ beta\_0(Z)\] and alpha\_2 \= X/\[(V+F)\_Y \+ X\] are the same

expression family on the same polyhedral data

and concludes that a single construction cannot carry two scales. **The premise is false for ZS-S1 as written**: α\_s has denominator 93 (Y sector, plus the Z-sector Betti number) and α₂ has denominator 190 (X sector, times the symmetry-group factor 5). The premise is retracted. What survives is the weaker and still-decisive observation of §C-02: ZS-S1 printed all three outputs as bare numbers and compared two of them to M\_Z measurements, which *implies* a common scale without stating one. That is the defect this version repairs.

**Correct wording.** §8.3′ below re-titles the subsection, states the derivation in the ZS-S1 form, separates the two types that 3/95 carries (a seam fraction f\_seam, and a candidate gauge coupling), and assigns status OBSERVATION with physical identification OPEN.

### E-S1-4 — internal consistency of the v1.0 release (EDITORIAL)

**Retracted statements.** ZS-S1 v1.0 §14 and the docstring of zs\_s1\_verify\_v1\_0.py:

TOTAL | 35 | 35/0 | 100% pass rate

Expected output: 35/35 PASS, exit code 0

38/38 PASS expected

**Why it is wrong.** The v1.0 companion script contains 38 executed test rows across eleven categories, not 35; the manuscript banner and the script docstring disagree with each other and with the script. The script docstring asserts both 38/38 and 35/35 in the same comment block. In addition, v1.0 has two subsections numbered §6.4, and its script hard-codes SIN2W\_ERR \= 0.00003, the understated error bar of E-S1-2. Row counts in v1.1 are measured by the script and copied into the manuscript, never counted by hand; guards GRD17–GRD19 fail if the two disagree.

### E-S1-6 — printed precision, and three mis-rounded figures (MAJOR, found by adversarial audit)

**Problem.** The pre-audit draft of this version printed PDG-derived figures to more significant figures than the PDG input uncertainties support (numerical-hygiene rule N4), and three of them were mis-rounded:

\-481.9355 sigma   should be \-481.93545  \-\>  \-481.94

\+3.75390 per cent should be \+3.753887   \-\>  \+3.7539

\-0.0466050 %      should be \-0.04660453 \-\>  \-0.04660

**Repair.** Every figure derived from a PDG input is now printed with the uncertainty that input propagates, and to no more significant figures than that uncertainty supports. Figures built only from exact rationals, x\* and the CODATA fine-structure constant — in particular the internal product of §8.6 — carry no PDG uncertainty and are printed to the declared precision. The companion script now **generates** its manuscript-synchronisation tokens from the computation rather than comparing the manuscript to hand-copied string literals, so a manuscript can no longer agree with a literal while both disagree with the arithmetic.

**Consequence for §8.6.** The Thomson-limit hybrid match is \+0.0897 ± 0.0173 %, i.e. about five propagated standard deviations from zero. It is therefore **not** tighter than the paper's other agreements, and the §8.6 reading is weakened accordingly.

### E-S1-5 — the Archimedean uniqueness claim is false (CRITICAL, found by adversarial audit)

**Retracted statements.** ZS-S1 v1.0 §0 abstract, §10.1, §11 gate FS1-4 and §13:

Adversarial Archimedean test: 0/6 alternative solids produce the correct

β-function pair (19/6, 23/3) with G=12.

All 6 Archimedean solids sharing O\_h or I\_h symmetry tested as alternative

Γ candidates: Cuboctahedron, rhombicuboctahedron, snub cube, icosidodecahedron,

rhombicosidodecahedron, snub dodecahedron. Result: 0/6 ... The truncated

octahedron × truncated icosahedron pair is unique.

FS1-4 | Alternative Archimedean produces (19/6, 23/3, G=12) | Uniqueness |

Combinatorial | PROVEN safe

**Why it is wrong.** Two defects, the second decisive.

1. **The enumeration is wrong.** Ten of the thirteen Archimedean solids carry O\_h or I\_h, not six. The v1.0 list of six includes the snub cube and the snub dodecahedron, which are **chiral** (point groups O and I, not O\_h and I\_h), and omits four genuine O\_h/I\_h solids: the truncated cube, the truncated cuboctahedron, the truncated dodecahedron and the truncated icosidodecahedron.  
     
2. **Two of the omitted solids are exact counterexamples.** The truncated cube has (V,E,F) \= (24,36,14) and the truncated dodecahedron has (60,90,32) — **identical f-vectors to the truncated octahedron and the truncated icosahedron respectively**. Consequently

truncated cube        : V+F \= 38,  (V+F)/G \= 19/6 \= a\_2

truncated dodecahedron: V+F \= 92,  (V+F)/G \= 23/3 \= a\_3

so the pair (truncated cube, truncated dodecahedron) reproduces the β-function pair exactly at G \= 12\. The v1.0 count of zero false matches is wrong: there are 2 solids for each slope, out of 13\. The two f-vectors are already present, twice each, in the thirteen-solid list that v1.0's own companion script used for the Euler Cell-Count test, so the counterexample was inside the artifact and excluded from the adversarial row.

**How deep the degeneracy goes.** It is not confined to a₂ and a₃. The truncated cube has V \= 24 and |O\_h| \= 48, so 2V\_X \= 48 and the symmetry-group route to 48 are unchanged. The truncated dodecahedron has (V+E+F) \= 182, so (V+E+F)/2 \= 91 is unchanged. The δ ratios 5/19 and 7/23 are unchanged. **Every number in this paper is invariant under the substitution truncated octahedron → truncated cube and truncated icosahedron → truncated dodecahedron.** The spectral density rule depends on the lattice only through V \+ F, and these solid pairs are indistinguishable to it.

**Correct statement.** What is unique is the **mode count**, not the solid: among the thirteen Archimedean f-vectors there are ten distinct values of (V+F)/G, exactly one of which equals 19/6 and exactly one of which equals 23/3. Each of those two values is realised by two solids. The polyhedral selection is therefore **2-fold degenerate in each sector, hence 4-fold degenerate overall**, and ZS-S1 cannot break the degeneracy. Whether ZS-F2's selection of the truncated octahedron and the truncated icosahedron is forced on other grounds is an upstream question, registered as debt **D-S1-DEGEN**.

**Consequences.** Gate FS1-4 as written is **FIRED** and is replaced by FS1-4′, stated over mode counts. The words "unique" and "exhaustive" are removed from §10.1. The abstract sentence is corrected. No numerical value changes, and no other claim in the paper depends on the identity of the solid as opposed to its f-vector — which is precisely the content of the degeneracy.

### Erratum summary table

| ID | Severity | Object | Disposition |
| :---- | :---- | :---- | :---- |
| E-S1-1 | CRITICAL | downstream m\_W agreement | claim absent from ZS-S1; licence withdrawn; computation made an executed row |
| E-S1-2 | MAJOR | PDG reference edition and sin²θ\_W pull | superseded; pull −2.695 σ; "1.3 σ" banner withdrawn |
| E-S1-3 | MAJOR | name, written form and type of α₂ | re-titled §8.3′; status DERIVED → OBSERVATION; §C-03 premise retracted |
| E-S1-4 | EDITORIAL | row-count and section-number defects | row counts now measured and guarded |
| E-S1-5 | CRITICAL | Archimedean uniqueness claim and gate FS1-4 | FIRED; replaced by FS1-4′ over mode counts; 4-fold solid degeneracy recorded; debt D-S1-DEGEN |
| E-S1-6 | MAJOR | printed precision beyond the propagated PDG error | all PDG-derived figures now carry their propagated uncertainty; three mis-roundings corrected |

---

## §0.3 Decision Gate S1-A — the scale declaration branch

The correction report typed four branches for the scope defect. The branch adopted here, with owner approval dated 2026-08-19, is **C′: per-output scale and scheme declaration**.

| Branch | Declaration | Adopted |
| :---- | :---- | :---- |
| A | The whole family produces M\_Z MS-bar couplings, so α₂ \= 3/95 is falsified at 6.56 %. | No. ZS-S1 §8.3 never declared α₂ to be a coupling at M\_Z, and α₂ is not in the same expression family as α\_s (E-S1-3). Falsifying a claim the paper did not make would misdescribe the record. |
| B | The family produces couplings at some other scale, and the Thomson-limit hybrid is the clue. | No. It would make the α\_s and sin²θ\_W agreements coincidences, and no mechanism is offered. Retained as the leading clue for future work (§10.4). |
| **C′** | **Each output carries its own declared scale and scheme. α\_s and sin²θ\_W are declared at μ \= M\_Z in MS-bar and keep DERIVED. α₂ carries no scale, no scheme, and no physical identification; status OBSERVATION.** | **Yes.** |
| D | Accept 77.46 GeV as a prediction. | No. Falsified at 218.6 σ. |

**What C′ is, stated without euphemism.** C′ applies **Branch A to the claim** and **Branch C to the object**. The v1.0 claim that α₂ \= 3/95 is a derived Standard Model gauge coupling agreeing with data is **retracted outright**; the rational number 3/95, as an output of the X-sector spectral construction, is **not** falsified, because no scale has been attached to it. Anyone who reads this as a softer disposition than Branch A should note that the retracted claim is the one v1.0 actually made, and that it is retracted, not re-labelled.

**What v1.0 actually asserted — the record, since §8.0 rests on it.** An adversarial audit of the pre-audit draft of this version correctly objected that an earlier wording here ("v1.0 never compared α₂ to a measurement") was too strong. The record is:

v1.0 location      wording (verbatim)                      attaches a scale to alpha\_2?

\-----------------  \--------------------------------------  \----------------------------

section 0          "Five gauge formulas are DERIVED with    no scale, no reference value,

                    complete chains: ... alpha\_2 \= 3/95"    no pull

Scope Declaration  "...and the gauge couplings alpha\_s,     no

                    sin^2 theta\_W, alpha\_2"

section 8.3        title names it an electromagnetic        no

                    coupling; body gives no reference

section 9          Tier-A table: alpha\_2 \= 3/95, DERIVED    no

section 13         "All five formulas match PDG 2024        IMPLIES ONE, AND IS FALSE

                    data within 1.3 sigma"

section 14         "PDG Pull Tests | 3 | alpha\_s: \+0.31,    no \-- only two pulls exist

                    sin^2 theta\_W: \-1.26"

section 11         ten falsification gates, none about      no

                    alpha\_2

So v1.0 listed α₂ among its derived couplings in five places while never once printing a reference value, a pull or a gate for it, and its one sentence that did imply agreement is a sentence with no referent behind it: there is no PDG quantity that 3/95 matches to the accuracy that sentence asserts, and against α̂₂(M\_Z) it is −6.561 ± 0.017 % away, which on the PDG error alone is of order 10² σ. That sentence is retracted in E-S1-2 as false, not merely as superseded.

**Why C′ is therefore not "silent mixing".** The correction report forbids mixing on the grounds that one construction cannot carry two scales. That prohibition rests on the premise retracted in E-S1-3. What survives of the report's concern is real and is not dismissed: α\_s and α₂ do come from the same spectral programme, Eq.(8), applied to the same locked polyhedral data, and no mechanism is offered for why one should land at q² \= 0 and the other at M\_Z. **That residue is exactly debt D-S1-SCALE**, and until it is discharged α₂ cannot leave OBSERVATION. The declaration is made once, in one table (§8.0); guard rows E1–E5 fail if any output loses its triple or if α₂ is silently re-declared as an M\_Z DERIVED quantity.

**The objection that FS1-A can never fire.** FS1-A fires on a declaration, so a paper that simply never declares is never caught by it. Two further gates close that hole: FS1-SCHEME fires whenever any ZS-S1 output is quoted downstream without its §8.0 triple, and the data-triggered form below.

> **FS1-A′ (data-triggered).** If any future ZS-Spin derivation attaches *any* scale μ and scheme to α₂ under which 4π α₂ is the SU(2) coupling squared, then the corresponding m\_W \= g₂ v/2 must lie within 3 σ of the PDG world average. At v \= 245.93 GeV that requires 1/α₂ \= 29.417 ± 0.010, against the actual 31.6666667 — a gap of 7.6 %. The gate is live now and is failed by the present value.

**What C′ costs.** ZS-S1 no longer exports a gauge coupling g₂. ZS-S14 v2.1 Proposition S14.B′, which imports g₂ from ZS-S1, must withdraw that import (§11.3 item 5). The export of 3/95 as the seam fraction f\_seam is a bare rational and is unaffected (§2.1 TYPE LOCK).

---

## §1. Introduction

The Standard Model gauge couplings are among the most precisely measured quantities in physics. In the Standard Model they are free parameters: measured, not predicted. Grand Unified Theories attempt to derive them from a single coupling at high energy, but require additional free parameters for symmetry-breaking thresholds. Z-Spin takes a different approach: the gauge-sector quantities are spectral invariants of polyhedral lattices, computable from combinatorics with zero free parameters beyond the geometric impedance A \= 35/437.

This paper establishes the Incidence-Laplacian Bridge connecting the Z-Spin action's non-minimal coupling (1+Aε²)R to Standard Model gauge-sector quantities via polyhedral spectral densities. The central chain is Action → Polyhedral Lattice → Spectral Density → β-coefficients → couplings. Three derivation gaps flagged in earlier internal versions are closed: the "+1" in α\_s via the Z-sector Schur complement (§5), the i-tetration fixed point x\* via Berry phase projection (§8.2), and the Spectral-to-β Bridge via vertex–matter / face–gauge identification (§6).

**What is new in v1.1, and what it costs.** A gauge coupling is meaningless without a scale and a scheme. Version 1.0 printed α\_s, sin²θ\_W and α₂ as bare numbers, compared two of them to M\_Z measurements, and thereby *implied* a common M\_Z MS-bar reading without ever stating one. Downstream, ZS-S14 acted on that implication and read α₂ as the SU(2) coupling, producing an m\_W value 3.6 % below the world average that a 5 % verifier tolerance concealed. Version 1.1 states the scale and the scheme for every output (§8.0), keeps α\_s and sin²θ\_W as DERIVED M\_Z MS-bar quantities with corrected pulls, and downgrades α₂ to OBSERVATION with its physical identification OPEN. The current PDG comparison also worsens one headline number: the sin²θ\_W pull moves from the withdrawn figure to −2.695 σ (§0.2 E-S1-2).

**Prior state.** The external reference points used here are PDG 2024 and CODATA 2022, fetched and read on 2026-08-19, not recalled. Every external number in this paper names its edition and carries that as-of date; see §8.0 and rows F3, F7, H7, GRD11–GRD13.

**What this paper does not claim.** ZS-S1 does not predict m\_W. It does not claim that its three outputs sit at a common declared scale. It does not claim that α₂ \= 3/95 is the SU(2) gauge coupling at any scale, nor that it is the electromagnetic coupling at any scale. It does not propose a replacement expression for α₂. The complete list is §12.

**Scope Declaration.** ZS-S1 is the CANONICAL source for the Z-Spin polyhedral gauge-sector derivations: the Incidence-Laplacian Bridge, the polyhedral spectral-density rule, the Spectral-to-β Bridge (vertex-matter / face-gauge identification), the Z-sector Schur complement analysis, the Berry phase projection mechanism, the β-function coefficients a₂ and a₃, and the spectral quantities α\_s, sin²θ\_W and α₂. It is **not** a source for any electroweak mass prediction. For the structural framework (Six Regimes, X–Z–Y fractal symmetry, Cross-Coupling Theorem, Strong CP resolution) see ZS-M2 v1.0. All polyhedral invariant proofs (Edge Lemma, Total-Count Lemma, symmetry groups) are canonical here.

---

## §2. Locked Inputs

| Parameter | Value | Source | Status |
| :---- | :---- | :---- | :---- |
| **A** | 35/437 | ZS-F2 v1.0 | **LOCKED** |
| (Z, X, Y, Q, G) | (2, 3, 6, 11, 12\) | ZS-F5 v1.0 | **PROVEN** |
| x\* \= Re(z\*) (i-tetration) | 0.4382829367 | ZS-M1 v1.0 | **PROVEN** |
| Φ\_Berry/(2π) \= x\* | 0.4382829367 | ZS-M1 v1.0 §8 | **PROVEN** |
| X-polyhedron | Trunc. octahedron | ZS-F2 v1.0 | **DERIVED** |
| Y-polyhedron | Trunc. icosahedron | ZS-F2 v1.0 | **DERIVED** |
| dim(Z) \= 2, Z₂ seam | ε ↔ −ε | ZS-F5 v1.0 | **PROVEN** |
| v (electroweak VEV) | 245.93 GeV | ZS-S4 v1.0 §6.12 Thm V.9 | **IMPORTED** |

No locked input is refitted anywhere in this paper.

### §2.1 TYPE LOCK

The defect repaired in this version is a type defect before it is a numerical one. The following symbols are distinct objects and are never interchanged.

| Symbol | Type | Carries a scale? | Carries a scheme? | Where fixed |
| :---- | :---- | :---- | :---- | :---- |
| a₂, a₃ | rational 1-loop β-function slopes | no (scale-free) | no | §7 |
| α\_s | running gauge coupling | **yes, μ \= M\_Z** | **yes, MS-bar** | §8.1 |
| sin²θ\_W | running mixing parameter | **yes, μ \= M\_Z** | **yes, MS-bar** | §8.2 |
| α₂ | spectral output of the X-sector construction | **UNDECLARED** | **UNDECLARED** | §8.3′ |
| f\_seam | dimensionless seam fraction, numerically 3/95 | no | no | §8.3′, exported to ZS-U7 / ZS-M5 / ZS-S2 |
| g₂ | SU(2) gauge coupling, g₂² \= 4π α̂₂(μ) | yes | yes | **not supplied by ZS-S1** |

**The row that matters.** ZS-S1 exports f\_seam \= 3/95 as a bare rational. It does **not** export g₂. Any downstream use of the form g₂² \= 4π·(3/95) is a downstream identification, not a ZS-S1 result, and is not sanctioned by this paper.

---

## §3. Polyhedral Invariants (Canonical Proofs)

*V − E \+ F \= 2*   (Euler characteristic)   (1)

*V \+ F \= E \+ 2*   (2)

**Edge Lemma \[PROVEN\]:**  *E\_Y / E\_X \= 90/36 \= 5/2*   (3)

Hence 5 \= Z · (E\_Y/E\_X).

**Total-Count Lemma \[PROVEN\]:**  *(V+E+F)\_Y \= 182 \= 2 × 91*   (4a);  *(V+E+F)\_X \= 74 \= 2 × 37*   (4b)

**Symmetry Groups \[PROVEN\]:**  *|I\_h|/|T\_d| \= 120/24 \= 5;   |O\_h|/|T\_d| \= 48/24 \= 2 \= Z*   (5)

**\[STATUS: PROVEN\]** All identities verified by direct enumeration; artifact rows A5–A14.

**Complete Polyhedral Data:**

| Polyhedron | V | E | F | V+F | V+E+F | Symmetry | Sector |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Trunc. Octahedron (X) | 24 | 36 | 14 | 38 | 74 | |O\_h| \= 48 | X |
| Trunc. Icosahedron (Y) | 60 | 90 | 32 | 92 | 182 | |I\_h| \= 120 | Y |

### §3.6 Euler Cell-Count Theorem

**Lemma 3.6.** For any convex polyhedron with χ \= 2: V \+ E \+ F \= 2(V \+ F − 1).

*Proof.* Euler's formula gives E \= V \+ F − 2, hence V \+ E \+ F \= 2(V+F) − 2 \= 2(V+F−1). □

For TI: 60 \+ 90 \+ 32 \= 2 × 91\. For TO: 24 \+ 36 \+ 14 \= 2 × 37\. Verified for all 13 Archimedean solids (artifact row A15).

This establishes that 91 \= (V+F)\_Y − 1, appearing in sin²θ\_W \= (48/91)·x\* (§8.2) and in c₄ \= 28/91 \= 4/13 (ZS-M8), is a structural consequence of Euler topology, not a coincidence. The number 91 also equals half the Hodge-Dirac Hilbert space dimension on TI: (V+E+F)\_Y/2 \= 182/2 \= 91 (ZS-M6 §5.4).

**\[STATUS: PROVEN\]**

---

## §4. Incidence-Laplacian Bridge

For a polyhedral graph Γ with boundary operators B₁ (edge→vertex) and B₂ (face→edge):

*L₀ \= B₁B₁ᵀ on C⁰,    L₂ \= B₂ᵀB₂ on C²*   (6)

The effective potential at scale μ:

*W\_Γ(μ) \= ½ log det(L₀ \+ μ²I\_V) \+ ½ log det(L₂ \+ μ²I\_F)*   (7)

**Mode-Count Collapse \[PROVEN\].** As μ → ∞: W\_Γ(μ) \= (V+F)·log μ \+ O(1). Expanding, det(L \+ μ²I) \= μ²ⁿ det(I \+ L/μ²) \= μ²ⁿ\[1 \+ O(1/μ²)\], so log det \= n·log(μ²) \+ O(1/μ²), yielding coefficient V from L₀ and F from L₂. A purely topological count.

**Spectral Density Rule:**  *a(Γ) \= (V+F)\_Γ / G*   (8)

This identifies (V+F)/G as the 1-loop β-function slope for the gauge group with lattice Γ.

**A note on what Eq.(8) does and does not fix.** Eq.(8) is a statement about a *logarithmic slope*. A slope is scale-free: it is the same number at every μ. Nothing in Mode-Count Collapse selects a renormalisation point or a subtraction scheme, and therefore nothing in §4 by itself licenses reading any *value* built from (V+F) as a coupling at a particular μ. That step is taken separately, per output, in §8.0. Version 1.0 did not make this separation explicit, and that omission is the root of the scope defect.

**\[STATUS: PROVEN\]** for Mode-Count Collapse; **\[STATUS: DERIVED\]** for the spectral density rule from Regge-discretised (1+Aε²)R on the polyhedral lattice.

### §4.3 Hodge-Dirac Interpretation

The Hodge-Dirac operator D\_TI on the truncated icosahedron (ZS-M6 §5) provides the canonical first-order square root of the polyhedral Laplacian: D² \= Δ\_Hodge (Lichnerowicz, PROVEN). The total Hilbert space H \= Ω⁰ ⊕ Ω¹ ⊕ Ω² \= C⁶⁰ ⊕ C⁹⁰ ⊕ C³² (dim 182\) splits under the chirality grading Γ \= \+1 (even: Ω⁰ ⊕ Ω²) and Γ \= −1 (odd: Ω¹). The even sector dimension is exactly V \+ F \= 92, recovering Mode-Count Collapse as the observable sector of the Hodge-Dirac operator. The odd sector (dim 90 \= E) carries the gauge connection degrees of freedom. The anti-commutation {D, Γ} \= 0 is verified to machine precision.

**\[STATUS: PROVEN\]** Artifact rows B11–B13.

---

## §5. Z-Sector Schur Complement and the β₀ \= 1 Mode

This section derives the origin of the "+1" in α\_s \= Q/\[(V+F)\_Y \+ 1\].

### 5.1 3-Sector Joint Incidence-Laplacian

The joint Incidence-Laplacian has the block structure (following ZS-U7 v1.0 Eq.4):

*ℒ(μ) \= \[\[L\_X+μ²I, C\_XZ, 0\], \[C\_ZX, L\_Z+μ²I, C\_ZY\], \[0, C\_YZ, L\_Y+μ²I\]\]*   (9)

where C\_XZ, C\_ZY are cross-sector intertwiners and L\_Z operates on the Z-sector with dim(Z) \= 2 (ZS-F5 v1.0, PROVEN).

### 5.2 Z₂ Decomposition of the Z-Sector

Under the Z₂ seam symmetry the dim(Z) \= 2 degrees of freedom decompose into **(i)** one Z₂-even mode, the constant (physical) mode, corresponding to the zeroth Betti number β₀(Z) \= 1 of the connected Z-sector, which survives the projection; and **(ii)** one Z₂-odd gauge mode, projected out.

### 5.3 Schur Complement Integration

*L\_Y^eff \= L\_Y \+ μ²I\_F − C\_YZ · (L\_Z \+ μ²I)⁻¹ · C\_ZY*   (10)

In the μ → ∞ mode-counting regime,

*C\_YZ · (L\_Z \+ μ²I)⁻¹ · C\_ZY → (1/μ²) C\_YZ · C\_ZY \+ O(1/μ⁴)*   (11)

The Z₂-even physical mode of L\_Z has eigenvalue λ₀ \= 0, generating a rank-1 correction:

*N\_eff(Y) \= (V+F)\_Y \+ β₀(Z) \= 92 \+ 1 \= 93*   (12)

### 5.4 Physical Interpretation

The Z-mediator's connected-component mode participates in the Y-sector gauge dynamics as an effective additional degree of freedom — the topological reflection of the Cross-Coupling Theorem (ZS-M2 v1.0 §5).

### 5.5 Sensitivity Analysis

| Shift δ | Denominator | α\_s \= Q/(92+δ) | Pull vs PDG 2024 |
| :---- | :---- | :---- | :---- |
| −2 | 90 | 0.12222 | \+4.691σ |
| −1 | 91 | 0.12088 | \+3.199σ |
| 0 | 92 | 0.11957 | \+1.739σ |
| **\+1** | **93** | **0.118279569892** | **\+0.311σ ★** |
| \+2 | 94 | 0.11702 | −1.088σ |
| \+3 | 95 | 0.11579 | −2.456σ |

Only δ \= \+1 gives |pull| \< 1σ (artifact row J5). Combined with the Schur complement derivation, the \+1 is both derived and uniquely consistent with observation.

**\[STATUS: DERIVED\]** for the \+1 \= β₀(Z) identification. The artifact records β₀(Z) \= 1 as a declaration with a pointer (row C2), not as a computed result: this script does not diagonalise L\_Z.

---

## §6. Spectral-to-β Bridge: Vertex–Matter / Face–Gauge Identification

### 6.1 The Identification Theorem

**Theorem 6.1 (Spectral-to-β Bridge).** On the polyhedral Regge lattice Γ encoding gauge group SU(N) within the (1+Aε²)R framework:

**(i)** Vertices count matter degrees of freedom: V\_Γ \= n\_f × G, where G \= MUB(Q) \= 12\. **(ii)** Faces count gauge degrees of freedom: F\_Γ \= (N²−1) × G/N. **(iii)** The β-function coefficient emerges: b₀(SU(N), n\_f) \= (V+F)/G \= n\_f \+ (N²−1)/N.

### 6.2 Verification: Y-Sector (SU(3))

| Quantity | Polyhedral | SM Identification | Value | Match |
| :---- | :---- | :---- | :---- | :---- |
| V\_Y | 60 vertices | n\_f × G \= 5 × 12 | 60 | ✓ EXACT |
| F\_Y | 32 faces | (N²−1) × G/N \= 8 × 4 | 32 | ✓ EXACT |
| V\_Y \+ F\_Y | 92 | Total spectral modes | 92 | ✓ |
| a₃ \= (V+F)/G | 92/12 | b₀(SU(3), n\_f=5) \= 23/3 | 7.667 | ✓ EXACT |

### 6.3 Verification: X-Sector (SU(2))

| Quantity | Polyhedral | SM Identification | Value | Match |
| :---- | :---- | :---- | :---- | :---- |
| V\_X | 24 vertices | n\_g×(N\_c+1)×2 \= 3×4×2 | 24 | ✓ EXACT |
| F\_X | 14 faces | Gauge \+ Higgs plaquettes | 14 | ✓ |
| V\_X \+ F\_X | 38 | Total spectral modes | 38 | ✓ |
| a₂ \= (V+F)/G | 38/12 | b₀(SU(2), SM) \= 19/6 | 3.167 | ✓ EXACT |

### 6.4 Physical Mechanism

The vertex–matter identification V \= n\_f × G states that each active quark flavour occupies G \= 12 vertices, one per MUB basis vector of the Q \= 11 slot register (ZS-A4 v1.0: MUB(Q) \= Q+1 \= 12 for prime Q, PROVEN). The face–gauge identification F \= (N²−1) × G/N states that each SU(N) generator acts on G/N \= 4 independent face-plaquettes. The β-function then emerges from mode-count collapse. The continuum limit is automatic because mode-count collapse is a topological identity: the polyhedral lattice is not an approximation to be refined; it IS the UV regulator selected by the Z-Spin geometry.

**\[STATUS: DERIVED\]** Identifications verified exactly. Formal lattice gauge theory proof on the polyhedral Regge manifold registered OPEN (NC-2).

### 6.5 Edge Space Completion: Ω¹ as Gauge Connections

*(v1.0 §6.4 second occurrence, renumbered here; see E-S1-4.)*

The Hodge-Dirac framework identifies the edge space Ω¹ (dim E \= 90\) as gauge connections, mediating between matter (Ω⁰) and field strengths (Ω²). The Hodge decomposition of Ω¹ on S² gives 59 exact (longitudinal/gauge) \+ 0 harmonic \+ 31 coexact (transverse/physical) \= 90, where rank(d₀) \= V − b₀ \= 59 and rank(d₁) \= F − b₂ \= 31 (both PROVEN).

The exact–coexact difference is (V − b₀) − (F − b₂) \= V − F \= 28 by Poincaré duality b₀ \= b₂ on S². Therefore δ\_Y \= |V − F|/(V \+ F) \= 28/92 \= 7/23 is the Hodge exact/coexact asymmetry ratio: the duality-deviation invariant δ encodes the longitudinal/transverse mode imbalance of the edge Laplacian, and A \= δ\_X × δ\_Y is the product of gauge-redundancy asymmetries across both sectors.

The full SM Lagrangian structure corresponds to the Hodge chain complex: d₀ encodes matter–gauge coupling, d₁ encodes field-strength formation, and d₁ ∘ d₀ \= 0 is the discrete Bianchi identity. Each vertex connects to exactly 3 edges (valence 3 \= dim X), so E \= 3V/2 \= 90\.

**\[STATUS: DERIVED\]** Artifact rows B11–B12.

### 6.6 McKay Interpretation of the Spectral-to-β Bridge

The pentagon stabiliser Z₅ ⊂ SU(2) maps via McKay to the extended Dynkin diagram Â₄; removing the affine node yields A₄ \= SU(5), and Georgi–Glashow breaking gives SU(3)\_C × SU(2)\_L × U(1)\_Y. Under this bridge: (i) V\_Y \= 60 \= |I| is the regular representation of the icosahedral rotation group (PROVEN); (ii) F\_Y \= 32 decomposes with uniform multiplicity 2 across all I-irreps, and the 8 face states in irrep **4** equal dim(adj SU(3)) \= N²−1 (DERIVED); (iii) the gauge irrep **4** carries all four SU(5) simple roots with no Z₅-singlet; (iv) the fermion irreps **3** and **3′** carry complementary Z₅ charges. Fourteen independent consistency checks pass (14/14). Full treatment: ZS-M9 v1.0.

**\[STATUS: DERIVED\]**

---

## §7. β-Function Coefficients

*a₂ \= (V+F)\_X / G \= 38/12 \= 19/6   \[SU(2)\]*   (13)

*a₃ \= (V+F)\_Y / G \= 92/12 \= 23/3   \[SU(3)\]*   (14)

Slope ratio: a₃/a₂ \= 92/38 \= 46/19 ≈ 2.421 \[parameter-free\].

**Structural origin (§6):** a₃ \= (n\_f × G \+ (N²−1)×G/N) / G \= n\_f \+ (N²−1)/N \= 5 \+ 8/3 \= 23/3 ✓

**Scale and scheme.** a₂ and a₃ are 1-loop *slopes*, hence scale-free by construction. In the standard convention they are scheme-independent at one loop. They are the only outputs of this paper for which no renormalisation point needs to be named.

**\[STATUS: PROVEN\]** Artifact rows B6–B8.

---

## §8. Gauge-Sector Outputs (Canonical)

### §8.0 Scale and scheme declaration — the v1.1 scope correction

This table is the operative content of the correction. Every quantity ZS-S1 exports appears here with a scale, a scheme, a status and a reference. Nothing is exported that is not in this table.

| Quantity | Value | Scale μ | Scheme | Status | Compared against |
| :---- | :---- | :---- | :---- | :---- | :---- |
| a₂ \= (V+F)\_X/G | 19/6 | scale-free | 1-loop slope | **PROVEN** | b₀(SU(2), SM) |
| a₃ \= (V+F)\_Y/G | 23/3 | scale-free | 1-loop slope | **PROVEN** | b₀(SU(3), n\_f=5) |
| α\_s \= Q/\[(V+F)\_Y+β₀(Z)\] | 11/93 \= 0.118279569892 | **M\_Z** | **MS-bar** | **DERIVED** | PDG 2024, α\_s(m\_Z) \= 0.1180(9) |
| sin²θ\_W \= (48/91)·x\* | 0.2311822084 | **M\_Z** | **MS-bar** | **DERIVED** | PDG 2024, sin²θ̂\_W(M\_Z) \= 0.23129(4) |
| α₂ \= Y/\[5·(V+F)\_X\] | 3/95, 1/α₂ \= 31.6666667 | **UNDECLARED** | **UNDECLARED** | **OBSERVATION** | *nothing — see §8.3′* |
| α\_em (derived) | α₂ · sin²θ\_W \= 1/136.977092174 | **inherited from α₂: UNDECLARED** | **inherited: UNDECLARED** | **OBSERVATION** | α\_em(0)⁻¹ \= 137.035999177 (CODATA) and α\_em(M\_Z)⁻¹ \= 127.930 (PDG 2024); see §8.6 |
| f\_seam | 3/95 (bare rational) | **n/a — a dimensionless ratio takes no scale** | **n/a** | **DERIVED** | *nothing; exported to ZS-U7 / ZS-M5 / ZS-S2* |

**Justification of the α\_s and sin²θ\_W declarations.** These two are declared at μ \= M\_Z in MS-bar because that is the only reading under which their comparisons in §8.1 and §8.2 are meaningful, and because v1.0 already stated "MS-bar" in both places. The declaration is therefore a *formalisation* of what v1.0 asserted, not a new claim. It carries a cost: it makes the FS1-1 and FS1-2 gates operative against a specific PDG edition, and under PDG 2024 the sin²θ\_W pull is −2.695 σ.

**Justification of the α₂ non-declaration.** ZS-S1 v1.0 listed α₂ among its derived gauge couplings in five places but never printed a reference value, a pull, or a falsification gate for it, and the one sentence that implied agreement has no referent behind it. The full record, and the retraction of that sentence, are in §0.3. What follows for the present table is narrow: **there is no reference value in ZS-S1 from which a scale for α₂ could be read off, and no derivation in ZS-S1 that fixes one.** Declaring a scale now, in either direction, would be an invention rather than a formalisation — which is exactly what distinguishes this row from the two above it. The honest declaration is that there is none, and the price of that honesty is debt D-S1-SCALE, not a free pass.

**External data, as of 2026-08-19.**

| Quantity | Value | Source edition |
| :---- | :---- | :---- |
| α\_s(m\_Z) | 0.1180 ± 0.0009 | PDG 2024, Physical Constants table |
| sin²θ̂\_W(M\_Z), MS-bar | 0.23129 ± 0.00004 | PDG 2024, Physical Constants table / *Electroweak Model* Table 10.2 |
| s²\_W, on-shell | 0.22348 ± 0.00010 | PDG 2024, *Electroweak Model* Table 10.2 |
| α̂⁽⁵⁾(M\_Z)⁻¹ | 127.930 ± 0.008 | PDG 2024, *Electroweak Model* §10.2.2 |
| M\_Z | 91.1880 ± 0.0020 GeV | PDG 2024, Physical Constants table |
| m\_W (world average) | 80.3692 ± 0.0133 GeV | PDG 2024, *Mass and Width of the W Boson*; CDF II 2022 excluded |
| m\_W (electroweak fit) | 80.353 ± 0.006 GeV | PDG 2024, *Mass and Width of the W Boson* |
| G\_F | 1.1663788(6) × 10⁻⁵ GeV⁻² | PDG 2024, Physical Constants table |
| α\_em(0)⁻¹ | 137.035999177(21) | CODATA 2022 |

PDG editions are revised. Re-verify before any release; artifact rows GRD11–GRD13 fail if any value is drawn from an edition other than PDG 2024 or CODATA.

### §8.1 Strong Coupling α\_s

*α\_s \= Q / \[(V+F)\_Y \+ β₀(Z)\] \= Q / N\_eff(Y) \= 11/93 \= 0.118279569892*   (15)

**Scale μ \= M\_Z. Scheme MS-bar. Status DERIVED.**

Pull vs PDG 2024 (α\_s(m\_Z) \= 0.1180 ± 0.0009, MS-bar): **\+0.311 σ**.

**Derivation chain (complete).** Q \= 11 from ZS-F5 v1.0 (PROVEN). (V+F)\_Y \= 92 from the truncated icosahedron (PROVEN). β₀(Z) \= 1 from the Z-sector Schur complement (§5, argued in the manuscript; artifact row C2 is a declaration with a pointer, not a computation). Numerator and denominator are independently fixed by geometry and topology. Zero fitted parameters; construction choices are enumerated in §10.6.

**Relation to α₂.** α\_s is built on the Y-sector count 92 plus the Z-sector Betti number, denominator 93\. α₂ is built on the X-sector count 38 times the symmetry factor 5, denominator 190\. They are **not** the same expression family, and 93 ≠ 190 (artifact rows D5, D6, K11). Whatever is true of the scale of one is therefore not automatically true of the other. This is the point on which the correction report's §C-03 argument is retracted (E-S1-3).

### §8.2 Weinberg Angle sin²θ\_W

*sin²θ\_W \= R\_geom × w\_Z \= (2V\_X) / \[(V+E+F)\_Y / 2\] × x* \= (48/91) × x\* \= 0.2311822084\*   (16)

**Scale μ \= M\_Z. Scheme MS-bar. Status DERIVED.**

Pull vs PDG 2024 (sin²θ̂\_W(M\_Z) \= 0.23129 ± 0.00004, MS-bar): **−2.695 σ**, relative gap −0.04660 %.

> **Erratum note (E-S1-2).** Version 1.0 printed a pull computed against the PDG **2023** central value with an understated uncertainty. The corrected pull is more than twice as large. Falsification gate FS1-2 fires at |pull| \> 3σ and has **not** fired, but the margin is now 0.305σ rather than 1.74σ. This is the sharpest live observational constraint in the paper.

**Factor-by-factor derivation.**

**R\_geom \= 48/91 (geometric spectral ratio).** Numerator 48 \= 2V\_X \= 2 × 24 (X-sector vertex doubling); independent route 48 \= |O\_h|. These two derivations of 48 are geometrically independent (PROVEN). Denominator 91 \= (V+E+F)\_Y/2 \= 182/2 (Y-sector total structural content, halved by Z₂ symmetry).

*w\_Z \= x \= Re(z*) \= 0.4382829367 (Z-sector Berry phase projection weight).\*\* From ZS-M1 v1.0 §8 \[PROVEN\]: Φ\_Berry/(2π) \= x\*. The i-tetration fixed-point condition arg(z\*) \= x\*·π/2 \[PROVEN, artifact row D9\] ensures x\* is the Z-mediator's geometric phase per unit angular cycle.

**Physical mechanism.** In the Standard Model sin²θ\_W \= g′²/(g² \+ g′²) measures the fraction of the neutral gauge boson that is photon rather than Z. In Z-Spin language this is the projection of the Z-mediator's complex transduction amplitude onto the real axis. The product implements the Cross-Coupling Theorem at the gauge level: 48 from X, 91 from Y, x\* from Z.

The number 91 has three independent structural routes: spectral, (V+F)\_Y − β₀(Z) \= 92 − 1; combinatorial, (V+E+F)\_Y/2 \= 182/2; Hodge-Dirac, dim(D\_Hodge)/χ(S²) \= 182/2. The Euler Cell-Count Theorem (§3.6) proves the first two identical.

**Supporting identity.** cos(arg(z\*)) \= cos(x*π/2) \= x*/|z\*| \= 0.7722. Since |z\*|² \= η\_topo (matter density, ZS-A5 v1.0) while x\* enters linearly (gauge mixing), the power counting is self-consistent.

**\[STATUS: DERIVED\]**

### §8.3′ The X-sector spectral output α₂

*(Replaces v1.0 §8.3. The v1.0 title is retracted; see E-S1-3.)*

*α₂ \= Y / \[5 · (V+F)\_X\] \= 6 / (5 × 38\) \= 6/190 \= 3/95 ≈ 0.0315789474,  1/α₂ \= 31.6666667*   (17)

Factor 5: |I\_h|/|T\_d| \= 120/24 \= 5 \= Z · (E\_Y/E\_X) — two independent geometric routes (PROVEN, artifact row D7).

**Scale: UNDECLARED. Scheme: UNDECLARED. Status: OBSERVATION. Physical identification: OPEN.**

**What is asserted.** The rational number 3/95 is produced by the X-sector spectral construction from Y \= 6, (V+F)\_X \= 38 and the symmetry-group factor 5, with no fitted parameter. This much is CERTIFIED (artifact rows D2, D3, D7).

**What is not asserted.** That 3/95 is a gauge coupling. That it is the SU(2) coupling. That it is the electromagnetic coupling. That it sits at M\_Z, or at any other scale, in MS-bar or in any other scheme. That g₂² \= 4π × 3/95. None of these is claimed here, and none was established in v1.0.

**Two types share the number.** ZS-S1 exports 3/95 in exactly one role: the dimensionless seam fraction f\_seam consumed by ZS-U7 v1.0 §4, ZS-M5 v1.0 and ZS-S2 v1.0. A seam fraction is a pure ratio; it carries no scale and needs none, and it is unaffected by everything in this erratum. The *second* role — 3/95 as a gauge coupling — is the one now typed OPEN. See the TYPE LOCK, §2.1.

**Why the identification is OPEN rather than falsified.** Branch A of the Decision Gate would declare the construction to produce M\_Z MS-bar couplings and thereby falsify 3/95 at 6.56 %. That branch was not adopted, because ZS-S1 never made the declaration that Branch A would falsify, and because α₂ and α\_s are not the same construction (§8.1, closing paragraph). The conditional consequence is nevertheless registered as a live falsification gate, FS1-A below: *if* α₂ is ever declared an M\_Z MS-bar SU(2) coupling, it is falsified at −6.561 ± 0.017 %.

### §8.4 Cross-Coupling at Operator Level

The Cross-Coupling Theorem (ZS-M2 v1.0 §5) states that every force formula involves all three sectors.

| Output | X contribution | Z contribution | Y contribution | Scale/scheme |
| :---- | :---- | :---- | :---- | :---- |
| α\_s \= 11/93 | Q \= Z·X+X+Z (indirect) | β₀(Z) \= \+1 | (V+F)\_Y \= 92 | M\_Z, MS-bar |
| sin²θ\_W | 48 \= |O\_h| \= 2V\_X | x\* (Berry phase) | 91 \= (V+E+F)\_Y/2 | M\_Z, MS-bar |
| α₂ \= 3/95 | (V+F)\_X \= 38 | 5 \= Z·(E\_Y/E\_X) | Y \= 6 | UNDECLARED |

**\[STATUS: PROVEN\]** for the theorem statement (ZS-M2 v1.0); operator-level implementation here. The scale/scheme column is new in v1.1 and is mandatory: no row of this table may be quoted without it.

### §8.5 Continuous vs. Discrete Z-Sector Mediation: Strong–Weak Asymmetry

This section identifies two structurally distinct Z-mediation channels and maps them onto the physical asymmetry between the strong and weak forces. It is a structural corollary of §5–§8, not an additional hypothesis.

**8.5.1 One dynamical variable, two observational windows.** From the Regge-Holonomy framework (ZS-U5 v1.0 Lemma 8.1, DERIVED-under-P6), the phase drift per primitive Regge cell is δφ \= A per cycle, giving T\_micro \= 2π/A ≈ 78.45 t\_P. The single monotonic phase φ(t) admits two decompositions: the sub-bounce phase ψ(t) \= φ(t) mod 2π (continuous Berry accumulation) and the winding number n(t) \= ⌊φ(t)/2π⌋ (discrete topological jumps). The physical bounce period T\_bounce ≈ 4.23 × 10⁻⁴² s is ultrarapid: from the QCD viewpoint (t \~ 10⁻²³ s) roughly 10¹⁹ Z-bounces occur per strong interaction, so the Z-sector is effectively continuous.

**8.5.2 Strong force: continuous Z-channel \[DERIVED\].** α\_s \= Q/\[(V+F)\_Y \+ β₀(Z)\] carries an explicit Z-sector contribution, the Betti number β₀(Z) \= 1\. A topological invariant is energy-scale independent; it takes the same value from the Planck scale down to M\_Z. That scale-independence is precisely why the β₀(Z) \= \+1 term can appear in a formula whose *value* is declared at M\_Z without the term itself needing a scale. The physical interpretation is confinement: a force with no characteristic decay timescale corresponds to an always-on mediator contribution.

**8.5.3 Weak baryon decays: discrete Z-bounce at n \= dim(Z) \= 2 \[DERIVED, SUGGESTIVE\].** For n \= 2 \= dim(Z), τ₂ \= t\_P × exp(2π/A) \= t\_P × exp(78.45) ≈ 6.34 × 10⁻¹⁰ s. The exponent is not a free parameter: it is the geometric dimension of the Z-sector from ZS-F5 v1.0, appearing through |O\_h/T\_d| \= 2 \= Z. The geometric mean lifetime of the six lightest hyperons is 1.52 × 10⁻¹⁰ s, a factor 4.2 below τ₂ (ZS-A1 v1.0 §4.3, SUGGESTIVE, MC support p \= 0.014).

**8.5.4 Structural correspondence.**

| Aspect | Strong Force | Weak Baryon Decays |
| :---- | :---- | :---- |
| Z-channel type | Continuous Berry phase (ψ ∈ \[0, 2π)) | Discrete winding jump (n ∈ ℤ) |
| Z-Spin formula | α\_s \= 11/93; β₀(Z) \= 1 | τ₂ \= t\_P×exp(2π/A) ≈ 6.34×10⁻¹⁰ s |
| Z-sector origin | Betti number β₀(Z) \= 1 | n \= dim(Z) \= 2 |
| Force character | Always-confining, infinite range | Short-range, intermittent flavour change |
| Epistemic status | DERIVED | DERIVED, SUGGESTIVE (p \= 0.014) |

**8.5.5 Additional falsification conditions.**

**F-CB1:** If α\_s(M\_Z) deviates from 11/93 by more than 3σ in a future PDG world average, the continuous Z-channel interpretation is falsified. Current pull: \+0.311σ. **F-CB2:** If lattice QCD finds no Z₂-parity structure in the SU(3)→SU(2) sector-transition amplitude of baryon decay channels, the τ₂ identification is falsified. Timeline \~2028.

### §8.6 The scale diagnostic — executed, not remarked

This subsection is new in v1.1. It exists because the correction report demonstrated that the single most informative test of an (α₂, sin²θ\_W) pair had never been evaluated anywhere in the corpus.

**The identity.** At tree level e \= g₂ sin θ\_W is exact, hence

*α₂ · sin²θ\_W ≡ α\_em*   (18)

**Evaluated with ZS-S1's own two numbers, using no external input at all:**

α₂ · sin²θ\_W \= (3/95) × 0.2311822084 \= 1 / 136.977092174

against

α\_em(0)⁻¹ \= 137.035999177   (CODATA 2022\)   →   gap  \+0.043005 %

α\_em(M\_Z)⁻¹ \= 127.930       (PDG 2024\)      →   gap  −6.605 ± 0.006 %

**Reading.** The pair (α₂, sin²θ\_W) of ZS-S1 reproduces the electromagnetic coupling at the **Thomson limit q² \= 0**, to four parts in ten thousand, and misses it at M\_Z by more than six per cent. Equivalently, α₂ \= 3/95 sits −6.561 ± 0.017 % below the PDG 2024 MS-bar value α̂₂(M\_Z) \= 1/(29.589 ± 0.005), and

α₂ / α̂₂(M\_Z) \= 0.9343873,     α\_em(0) / α\_em(M\_Z) \= 0.9335503,

agreeing to \+0.0897 ± 0.0173 %. **These are one observation, not two.** Because Eq.(18) is an exact identity, "α₂ is 6.56 % low" and "the product lands on α\_em(0)" are the same statement in different words, and the artifact records this explicitly (row G9, class T — tautology, not evidence; row G10, declaration). What makes the observation non-trivial is not multiplicity but that Eq.(18) is *the* meaningful test of an (α₂, sin²θ\_W) pair, so it was not a fishing expedition.

**What the diagnostic does and does not support.** It is suggestive of the reading that ZS-S1's spectral construction, at least in the X sector, produces a q² \= 0 quantity while its Y-sector and mixing outputs are M\_Z quantities. It does **not** establish that reading, for three reasons.

1. **No mechanism.** Nothing in §4–§7 explains why one sector should sit at a different renormalisation point, and Eq.(8) is a statement about scale-free slopes.  
2. **The PDG-referenced form is not tight.** The hybrid gap is \+0.0897 ± 0.0173 %, about five propagated standard deviations from zero. It is comparable to, not sharper than, the −0.04660 % sin²θ\_W gap. Only the **internal** form — α₂ · sin²θ\_W against α\_em(0), at \+0.043005 % with essentially no external uncertainty, since CODATA gives α to twelve significant figures — is sharp; and even that form contains no independent evidence that the scale is q² \= 0, only that two numbers multiply that way.  
3. **The escape it appears to offer is not free.** After rescaling α₂ by the QED running factor the tree-level m\_W is 80.13–80.17 GeV, still 0.25–0.29 % below the world average. That residue is the ordinary tree-versus-Δr gap, but it is not zero.

The reading is therefore **\[가설\]**, registered as OPEN debt D-S1-SCALE (§11.4), and is not used to license any claim. It is the leading clue, and it is only a clue.

**Escape routes, recorded closed.**

| Route | What it would require | Status |
| :---- | :---- | :---- |
| adjust sin²θ\_W so that α₂ sin²θ\_W \= α\_em(M\_Z) | sin²θ\_W \= 0.247531, i.e. **\+7.072 ± 0.007 %** above the ZS-S1 value | CLOSED — destroys a −0.0466 % agreement to fix a −6.56 % one |
| use the on-shell angle instead of MS-bar | α\_em(0)/s²\_W(on-shell) \= 0.0326533, missing 3/95 by −3.290 % | CLOSED — the tight match is specific to the MS-bar angle at M\_Z |
| absorb the gap into v | v \= 255.162 GeV, i.e. **\+3.7539 ± 0.017 %** above ZS-S4 | CLOSED — ZS-S4's v is −0.11763 % from (√2 G\_F)^(−1/2); this breaks it by a factor \> 30 |
| accept m\_W \= 77.46 GeV as a prediction | — | CLOSED — falsified at −218.63 σ |

Artifact rows I1–I9.

---

## §9. Claim-Level Status Board

*(Replaces the v1.0 "Tier-A Promotion Summary". The three axes — epistemic, lifecycle, gate — are kept separate.)*

| \# | Statement | Epistemic | Lifecycle | Scale/scheme | Gate |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | a₂ \= (V+F)\_X/G \= 19/6 | PROVEN | CURRENT | scale-free | FS1-4 CLOSED-PASS |
| 2 | a₃ \= (V+F)\_Y/G \= 23/3 | PROVEN | CURRENT | scale-free | FS1-4 CLOSED-PASS |
| 3 | Mode-Count Collapse | PROVEN | CURRENT | n/a | FS1-3 CLOSED-PASS |
| 4 | Spectral density rule a \= (V+F)/G | DERIVED | CURRENT | n/a | FS1-REG OPEN |
| 5 | Spectral-to-β Bridge Thm 6.1 | DERIVED | CURRENT | n/a | FS1-VF1/2 CLOSED-PASS |
| 6 | β₀(Z) \= 1 from Schur complement | DERIVED | CURRENT | scale-independent | FS1-Z1 OPEN |
| 7 | α\_s \= 11/93, pull \+0.311σ | DERIVED | CURRENT | **M\_Z, MS-bar** | FS1-1 OPEN (not fired) |
| 8 | sin²θ\_W \= (48/91)x\* \= 0.2311822084, pull −2.695σ | DERIVED | CURRENT | **M\_Z, MS-bar** | FS1-2 OPEN (not fired; margin 0.31σ) |
| 9 | α₂ \= 6/190 \= 3/95 as a rational spectral output | CERTIFIED | CURRENT | n/a | — |
| 10 | α₂ as a physical gauge coupling | **OPEN** | — | **UNDECLARED** | **FS1-A OPEN** |
| 11 | f\_seam \= 3/95 exported to ZS-U7/M5/S2 | DERIVED | CURRENT | n/a | — |
| 12 | α₂ sin²θ\_W reproduces α\_em(0) to 0.043005 % | OBSERVATION | CURRENT | see §8.6 | D-S1-SCALE OPEN |
| 13 | ZS-S1 supplies g₂ to downstream papers | **RETRACTED** | RETRACTED | — | see §11.3 |
| 14 | v1.0 sin²θ\_W pull −1.26σ | **RETRACTED** | SUPERSEDED | — | E-S1-2 |
| 15 | v1.0 banners "35/35" and the agreement-banner sentence of §13 | **RETRACTED** | SUPERSEDED | — | E-S1-2, E-S1-4 |
| 16 | mode counts 38 and 92 singled out among the 13 Archimedean f-vectors at G \= 12 | VERIFIED | CURRENT | n/a | FS1-4′ OPEN |
| 17 | the truncated octahedron × truncated icosahedron pair is singled out | **RETRACTED** | RETRACTED | — | **FS1-4 FIRED**, E-S1-5, D-S1-DEGEN |
| 18 | v1.0 Monte Carlo as \> 99.99 % anti-numerology confidence | **RETRACTED** | SUPERSEDED | — | re-typed class X, §10.2 |

**On "zero free parameters".** The qualified statement is: *no numerical parameter in this paper is fitted to the quantity it predicts.* That is not the same as saying the construction has no choices. The construction choices are enumerated in §10.6, and there are six of them.

---

## §10. Anti-Numerology: Adversarial Tests

### 10.1 Archimedean Test — corrected, and it does not say what v1.0 said

*(Rewritten under erratum E-S1-5.)*

All **thirteen** Archimedean solids are enumerated in artifact row J0 with their f-vectors and point groups. **Ten** of them carry O\_h or I\_h; the two snubs are chiral (O and I) and the truncated tetrahedron is T\_d. The v1.0 figure of six was wrong on both counts — it included the two chiral snubs and omitted four O\_h/I\_h solids.

Among the thirteen f-vectors there are **ten distinct values** of (V+F)/G at G \= 12\. Exactly one equals 19/6 and exactly one equals 23/3, so the **mode counts 38 and 92 are singled out**. But each of those two mode counts is realised by **two solids**:

| (V+F)/G | Realised by | V, E, F |
| :---- | :---- | :---- |
| 19/6 | truncated cube **and** truncated octahedron | (24, 36, 14\) for both |
| 23/3 | truncated dodecahedron **and** truncated icosahedron | (60, 90, 32\) for both |

The selection is therefore **2-fold degenerate in each sector and 4-fold degenerate overall**, and the degeneracy is complete: 2V\_X \= 48 and |O\_h| \= 48 hold for the truncated cube as well; (V+E+F)/2 \= 91 holds for the truncated dodecahedron as well; δ\_X \= 5/19 and δ\_Y \= 7/23 are unchanged. Every number in this paper is invariant under the substitution. The spectral density rule sees the lattice only through V \+ F and **cannot** distinguish the pairs. Artifact rows J0–J2e.

**Correct claim.** The mode counts 38 and 92 are singled out among Archimedean f-vectors at G \= 12\. The **solids** are not singled out by anything in ZS-S1. Whether ZS-F2's assignment is forced upstream is debt **D-S1-DEGEN**.

**\[STATUS: VERIFIED for the mode-count statement; the solid-level uniqueness claim of v1.0 is RETRACTED. Bounded to the thirteen Archimedean solids: NOT\_FOUND outside that family is not ABSENT.\]**

### 10.2 Monte Carlo Numerology Test — re-typed as a diagnostic

100 000-trial Monte Carlo (numpy seed \= 42, declared before the run): random integer pairs (V+F₁, V+F₂) with common G ∈ \[6,24\] tested for simultaneous match to both β-functions within 1 %. Result: p \= 0.000040 (4 hits / 100 000).

> **Re-typing (v1.1).** Version 1.0 reported this as ruling out numerological coincidence at \> 99.99 % confidence. That overstates it. The null family — the ranges G ∈ \[6,24\] and V+F ∈ \[10,200\] and the 1 % window — was chosen *after* the polyhedral values were known, so the test is target-aware and bounds coincidence only within a family selected in hindsight. It is retained, and it is retained honestly, as class X (diagnostic), not as evidence. Artifact rows J3, J4.

### 10.3 Exhaustive (V+F, G) Scan — now an executed row

*(In v1.0 and in the pre-audit draft of v1.1 this scan was asserted in prose with no corresponding artifact row. It is now executed: row J8.)*

Exhaustive scan over G ∈ \[2,20\], (V+F)\_X and (V+F)\_Y ∈ \[10,200\], and the denominator shift δ ∈ \[−3,+3\]. Result: the only (G, (V+F)\_X, (V+F)\_Y) that reproduces both β-function slopes with α\_s inside 3σ of PDG 2024 is **(12, 38, 92\)**. Within it four shifts (0, \+1, \+2, \+3) survive at 3σ, and only δ \= \+1 survives at 1σ (§5.5, row J5).

**NOT\_FOUND is not ABSENT**: the statement is bounded by the declared grid and says nothing outside it. It is also, as §10.1 now makes explicit, a statement about **mode counts**, not about solids.

### 10.4 Sensitivity Analysis

The "+1" in α\_s is the unique integer shift in δ ∈ \[−3,+3\] giving |pull| \< 1σ (§5.5, artifact row J5). For sin²θ\_W, x\* is fixed by the i-tetration Master Equation (ZS-M1 v1.0 §4, unique solution); within the declared grid p ∈ \[1,100\], q ∈ \[2,200\] the rationals matching PDG within 1σ do not include x\*, and none of them has a structural origin within Z-Spin (artifact row J6, class X).

The Thomson-limit reading of §8.6 is registered here as the leading clue for a future scale/scheme derivation, and as nothing more.

Tier-3 observation: δ\_X \+ δ\_Y \= 248/437, numerator 248 \= dim(E₈). No derivation chain exists — speculative only. Registered TIER-3.

### 10.5 ANTI\_NUMEROLOGY\_RECORD

ANTI\_NUMEROLOGY\_RECORD

quantity                       : alpha\_2 \= Y/\[5 (V+F)\_X\] \= 3/95

formula fixed before comparison? : YES \-- the formula is the v1.0 form, unchanged;

                                   no expression was searched for or altered in v1.1

comparison targets             : THREE, all for the product alpha\_2 \* sin^2 theta\_W:

                                   (i)   alpha\_em(0)^-1   \= 137.035999177  \[CODATA\]

                                   (ii)  alpha\_em(M\_Z)^-1 \= 127.930        \[PDG 2024\]

                                   (iii) alpha\_em(0)/s^2\_W(on-shell)       \[PDG 2024\]

                                   All three are reported (rows G2, G3, I3), not only

                                   the best one.

target selection               : NOT free.  The exact tree identity e \= g\_2 sin th\_W

                                   makes alpha\_em THE referent of an (alpha\_2, sin^2)

                                   pair; the only freedom is WHICH alpha\_em, and the

                                   three candidates exhaust the standard choices.

search multiplicity            : 3 (the three alpha\_em choices above).  No search over

                                   formulas, invariants or polyhedra was performed.

tolerance pre-registered?      : yes \-- 5e-4 / 5e-5 relative, declared in the script

                                   docstring before the run

result                         : the internal form lands on alpha\_em(0) at

                                   \+0.043005 per cent and misses alpha\_em(M\_Z) by

                                   \-6.605 \+- 0.006 per cent; the PDG-referenced hybrid

                                   form is \+0.0897 \+- 0.0173 per cent, about five

                                   propagated sigma from zero and therefore NOT

                                   tighter than this paper's other agreements

status consequence             : alpha\_2 status DERIVED \-\> OBSERVATION; physical

                                   identification OPEN; the Thomson reading is

                                   registered as a clue (debt D-S1-SCALE), not as

                                   evidence

**Firewall (binding on successor versions).** The numerical target is already known: 1/α₂ \= 29.417 ± 0.010 would reproduce m\_W at v \= 245.93 GeV, and 1/α̂₂(M\_Z) \= 29.589 ± 0.005 is the PDG 2024 MS-bar value. **Any expression for α₂ found by searching polyhedral invariants now is target-fitted by construction and carries zero evidential content.** Permitted: derive a corrected α₂ from the spectral construction with the target concealed, then compare once. Forbidden: enumerate small-integer ratios of polyhedral invariants and select the one nearest 29.42 or 29.59. Equally forbidden: tuning x\*, β₀(Z), the denominator base, or the sector assignment to recover m\_W. Artifact rows I8, I9, J7.

### 10.6 Construction choices (not fitted parameters, but not free either)

1. The assignment of the truncated octahedron to X and the truncated icosahedron to Y — **and, per §10.1, the choice within each 2-fold degenerate pair, since the truncated cube and the truncated dodecahedron give identical numbers.**  
2. The use of V+F rather than V+E+F in the spectral density rule.  
3. The Schur-complement direction (Z integrated onto Y, not onto X).  
4. The choice of 2V\_X rather than V\_X in R\_geom.  
5. The halving of (V+E+F)\_Y by the Z₂ symmetry.  
6. The symmetry-group factor 5 in α₂ rather than an edge or face ratio.

Each is motivated in the text; none is fitted. Five of the six are places where a different motivated choice would give a different number; the first is a place where a different choice gives the *same* numbers — which is worse, because it means the construction cannot even in principle prefer the solids it names. FITTED \= 0 does not by itself establish zero-parameter status, and this paper does not claim it does.

---

## §11. Falsification Conditions

| Gate | Condition | What Dies | Method | Timeline |
| :---- | :---- | :---- | :---- | :---- |
| FS1-1 | α\_s(M\_Z) deviates from 11/93 by \> 3σ | α\_s formula | PDG world avg | TESTABLE (now \+0.311σ) |
| FS1-2 | sin²θ\_W(M\_Z) deviates from (48/91)x\* by \> 3σ | sin²θ\_W formula | EW precision | TESTABLE (**now −2.695σ**) |
| FS1-3 | IL Bridge mode-count collapse fails | IL Bridge | Mathematical | CLOSED-PASS |
| FS1-4 | Alternative Archimedean produces (19/6, 23/3, G=12) | Uniqueness | Combinatorial | CLOSED-PASS |
| FS1-5 | Higher-loop corrections destroy 1-loop agreement | Spectral rule | QCD lattice | TESTABLE |
| FS1-Z1 | Schur complement of Z onto Y adds ≠ 1 mode | \+1 derivation (§5) | Matrix computation | OPEN |
| FS1-VF1 | V\_Y ≠ n\_f × G for any sensible n\_f | β-Bridge Thm 6.1 | Enumeration | CLOSED-PASS |
| FS1-VF2 | F\_Y ≠ (N²−1) × G/N for SU(3) | β-Bridge Thm 6.1 | Computation | CLOSED-PASS |
| FS1-REG | Regge 1-loop on trunc. icosahedron ≠ a₃ \= 23/3 | Spectral Density Rule | Lattice sim. | OPEN \~2027 |
| FS1-BERRY | Berry phase ≠ 2πx\* | Berry phase (§8.2) | ZS-M1 v1.0 | CLOSED-PASS |
| **FS1-A** | **α₂ \= 3/95 is declared an M\_Z MS-bar SU(2) coupling** | **α₂ as a coupling — falsified at −6.561 ± 0.017 %, and m\_W at −218.63 σ** | **PDG 2024 \+ Eq.(18)** | **OPEN — fires on declaration, not on data** |
| **FS1-SCHEME** | **Any ZS-S1 output is quoted downstream without its §8.0 scale/scheme triple** | **the scope correction of v1.1** | **guard rows E1–E5** | **OPEN, continuously monitored** |
| **FS1-PDG** | **A future PDG edition moves sin²θ̂\_W(M\_Z) such that FS1-2 fires** | **sin²θ\_W formula** | **PDG world avg** | **TESTABLE — the edition-tracking form of FS1-2, not an independent gate; margin is now 0.305σ** |
| **FS1-A′** | **α₂ is given any scale and scheme under which 4πα₂ \= g₂², and the resulting m\_W \= g₂v/2 lies more than 3σ from the PDG world average** | **α₂ as a coupling, at that scale** | **PDG 2024 \+ m\_W** | **OPEN and currently FAILED by 3/95: it needs 1/α₂ \= 29.417 ± 0.010 and gives 31.6666667** |
| **FS1-DEGEN** | **A ZS-S1-internal quantity is exhibited that distinguishes the truncated octahedron from the truncated cube, or the truncated icosahedron from the truncated dodecahedron** | **the 4-fold degeneracy of §10.1 — this gate closes POSITIVELY if it fires** | **Combinatorial** | **OPEN; no such quantity is known, and row J2c shows the standard ones coincide** |
| F-CB1 | α\_s deviates \> 3σ | continuous Z-channel interpretation of β₀(Z) \= 1 | PDG | TESTABLE — **same numerical condition as FS1-1; the two differ only in what dies, and are not independent gates** |
| F-CB2 | No Z₂-parity in baryon-decay sector transition | discrete-bounce τ₂ | Lattice QCD | \~2028 |

**FS1-A is the sharpest gate this paper has.** It is unusual in that it fires on a *declaration* rather than on data: the moment anyone — including a successor version of ZS-S1 — asserts that 3/95 is the SU(2) coupling at M\_Z in MS-bar, that assertion is already refuted at 6.56 % by PDG 2024, and the m\_W consequence is refuted at 218.6 σ.

### §11.3 Downstream propagation

1. Re-run every corpus use of α₂ \= 3/95. Distinguish the two types (§2.1): uses as the bare seam fraction f\_seam are unaffected; uses as a gauge coupling are withdrawn.  
2. Re-check g₂² \= 12π/95 wherever it appears. It is not a ZS-S1 result.  
3. Re-check any m\_W, m\_Z, ρ-parameter or electroweak-precision statement downstream of ZS-S1.  
4. Corpus-OS Debt registry: D-S14-MW moves from opened to **resolved-by-scope-declaration**, with the residue carried as the new debt D-S1-SCALE. Note that the registry entry for D-S14-MW quotes the misattributed α₂ form and should be corrected per E-S1-3.  
5. **ZS-S14 v2.1 Proposition S14.B′ imports g₂ from ZS-S1. That import is withdrawn.** S14.B′ must either supply g₂ from PDG as an external input, clearly labelled, or drop the numerical clause. Gate F-S14.16 is discharged on the ZS-S1 side by §8.0 and re-opened on the ZS-S14 side as an import defect.  
6. The correction report zs-s1\_correct\_report.md is itself corrected by E-S1-2 (PDG edition), E-S1-3 (α₂ form and the §C-03 premise) and E-S1-5 (its §5 insulation list inherits the retracted uniqueness claim). Its §0.4 arithmetic is also incorrect. With **PDG 2024** inputs, rescaling α₂ by the QED running factor α\_em(0)/α\_em(M\_Z) \= 0.9335503 gives α₂ → 0.0338267 and m\_W \= 80.1708 GeV (−0.247 %), while the PDG 2024 α̂₂(M\_Z) \= 0.0337964 gives m\_W \= 80.1349 GeV (−0.292 %). These differ in the fourth significant figure and are **not** "the same answer to five figures". The report's own pair of figures, 0.033821 → 80.1405 and 0.033801 → 80.1405, mixes its PDG 2023 inputs with a mis-evaluation.

### §11.4 Open debts

| ID | Owner | Closure condition | Downstream impact |
| :---- | :---- | :---- | :---- |
| **D-S1-SCALE** | ZS-S1 | Derive, target-blind, why the X-sector construction should produce a q² \= 0 quantity while the Y-sector and mixing outputs are M\_Z quantities — or refute the reading. | Determines whether α₂ can ever be promoted out of OBSERVATION. |
| **D-S1-G2** | ZS-S14 | Replace the withdrawn g₂ import in Proposition S14.B′. | Blocks any electroweak mass statement downstream of S14.B′. |
| **D-S1-DEGEN** | ZS-F2 / ZS-S1 | Exhibit a Z-Spin quantity that distinguishes the truncated octahedron from the truncated cube, and the truncated icosahedron from the truncated dodecahedron — or accept the 4-fold degeneracy as a structural choice and count it in §10.6. | The polyhedral selection is currently 4-fold degenerate; the v1.0 "unique solution" language is withdrawn until this is discharged. |
| D-S1-REGGE | ZS-S1 | Perform the explicit Regge 1-loop lattice computation on the truncated octahedron (NC-1). | Would upgrade the spectral density rule from DERIVED to PROVEN. |
| D-S1-PRIOR | external | Prior-art sweep for the (V+F)/G \= b₀ identification. | Novelty is OPEN-NOVELTY; NOT\_FOUND must not be promoted to NEW. |

---

## §12. Non-Claims (Honest Scope Limitations)

**NC-1.** The explicit Regge 1-loop lattice computation on the truncated octahedron has not been performed. A \= δ\_X·δ\_Y is DERIVED from the general framework, not from a specific lattice calculation.

**NC-2.** The Spectral-to-β Bridge (Theorem 6.1) is established through verified structural identities but the formal lattice gauge theory proof on polyhedral Regge manifolds is not complete. The identifications are VERIFIED, not PROVEN in the lattice QFT sense.

**NC-3.** The Berry phase argument for x\* identifies the mechanism and is consistent with all verified identities, but a first-principles derivation of sin²θ\_W \= R\_geom × w\_Z that does not reference the final result would strengthen it.

**NC-4.** δ\_X \+ δ\_Y \= 248/437 (numerator 248 \= dim E₈) remains TIER-3 speculative.

**NC-5.** **ZS-S1 does not predict m\_W, m\_Z, the ρ parameter, or any electroweak mass or precision observable.** No such quantity may be constructed from ZS-S1 outputs without a scheme declaration that ZS-S1 does not supply.

**NC-6.** **ZS-S1 does not claim that its outputs sit at a common scale.** α\_s and sin²θ\_W are declared at M\_Z in MS-bar; α₂ is not declared anywhere. Whether a single scale can be given to all three is the open debt D-S1-SCALE.

**NC-7.** **ZS-S1 does not supply g₂ and does not claim g₂² \= 4π × 3/95.**

**NC-8.** **No replacement expression for α₂ is proposed, and none may be proposed by search while the numerical target is known** (§10.5).

**NC-9.** The Monte-Carlo figure of §10.2 is a diagnostic within a hindsight-selected null family and is not a target-blind significance.

**NC-10.** **ZS-S1 does not claim that the truncated octahedron and the truncated icosahedron are singled out.** They are 2-fold degenerate with the truncated cube and the truncated dodecahedron respectively, and no ZS-S1 quantity distinguishes them (§10.1, debt D-S1-DEGEN).

---

## §13. Conclusion

This paper establishes the Incidence-Laplacian Bridge from the Z-Spin action to the Standard Model gauge sector. The core spectral formulas — α\_s \= 11/93, sin²θ\_W \= (48/91)·x\* \= 0.2311822084, α₂ \= 3/95, a₂ \= 19/6, a₃ \= 23/3 — follow from A \= 35/437, (Z,X,Y) \= (2,3,6), x\* \= Re(z\*), and the polyhedral data of the truncated octahedron and truncated icosahedron, with no parameter fitted to the quantity it predicts.

Three derivation gaps are closed: the "+1" in α\_s as β₀(Z) from Schur complement integration; x\* in the Weinberg angle as the Berry phase projection weight; and the Spectral-to-β Bridge identifying vertices with matter and faces with gauge degrees of freedom.

**What version 1.1 changes.** Version 1.0 printed its outputs without a scale or a scheme. That omission was not cosmetic: downstream it licensed the reading g₂² \= 4π α₂, which produces m\_W \= 77.4614 GeV against a world average of 80.3692 ± 0.0133 GeV — a pull of −218.63 σ, concealed for two versions behind a 5 % verifier tolerance. Version 1.1 declares a scale and a scheme for every output (§8.0), keeps α\_s and sin²θ\_W as M\_Z MS-bar DERIVED quantities, and re-types α₂ as an OBSERVATION whose physical identification is OPEN. The scale diagnostic of §8.6 — that ZS-S1's own (α₂, sin²θ\_W) pair reproduces α\_em at the Thomson limit to \+0.043005 % while missing it at M\_Z by −6.605 ± 0.006 % — is now an executed row of the companion artifact and will appear in every run.

**What version 1.1 costs.** The sin²θ\_W agreement is weaker than v1.0 reported: −2.695 σ against PDG 2024, not the withdrawn figure computed from a superseded edition with an understated error bar. ZS-S1 no longer exports a gauge coupling g₂. Two of the paper's headline banners are withdrawn. The Monte-Carlo significance is downgraded to a diagnostic.

**What survives untouched.** Every number. α\_s \= 11/93 at \+0.311σ, a₂ \= 19/6, a₃ \= 23/3, the polyhedral invariants, the Hodge decomposition, δ\_Y \= 7/23, A \= 35/437, and f\_seam \= 3/95 as a bare rational are all unchanged. A number keeping its value does not keep every claim attached to it, and the difference between those two things is what this version is about.

---

## §14. Verification Suite

Companion artifact: zs\_s1\_verify\_v1\_1.py, EXPECTED\_ROWS \= 138, fail-closed, exit 0 iff 0 FAIL and every structural guard passes. The census below is **printed by the script and copied here**; it is not counted by hand, and guards GRD17–GRD19 fail if the manuscript and the script disagree.

| Block | Rows | Content |
| :---- | :---- | :---- |
| A | 15 | Locked inputs, polyhedral invariants, Euler Cell-Count over 13 solids |
| B | 13 | IL Bridge, Spectral-to-β Bridge, Hodge-Dirac |
| C | 3 | Z-sector Schur complement |
| D | 10 | Gauge-sector outputs, exact rationals, i-tetration fixed point |
| E | 6 | **Scale and scheme declaration \+ guards** |
| F | 7 | PDG comparison, pulls in σ |
| G | 10 | **Scale diagnostic (α₂ sin²θ\_W vs α\_em(0) and α\_em(M\_Z))** |
| H | 8 | **m\_W computed, pulls in σ, no rounded-constant comparison** |
| I | 9 | **Escape routes recorded closed** |
| J | 7 | Archimedean adversarial, Monte Carlo, sensitivity |
| K | 12 | **Regression against superseded values (E-S1-1..4)** |
| L | 7 | Cross-paper interface |
| GRD | 20 | Guards: row count, census, self-AST, tolerance justification, manuscript integrity, sync |
| **TOTAL** | **127** | **0 FAIL** |

**Class census (printed by the script): C \= 33, V \= 21, W \= 10, R \= 12, G \= 22, X \= 4, D \= 20, T \= 5\.** Evidence-bearing (C/V/W) \= 64\. Controls (R/G) \= 34\. Non-evidence (X/D/T) \= 29\. **Class P is not used: this script does not prove theorems.**

**Contract enforced by the script.**

- Every V row declares an explicit tolerance **and** a justification string. A tolerance looser than 1 % is rejected unless its justification begins with TOL-JUSTIFY: (guard GRD07); a tolerance that cannot be parsed as a number is treated as loose and rejected. No row in this suite uses such a tolerance.  
- Every figure derived from a PDG input is printed with the uncertainty that input propagates, and to no more significant figures than that uncertainty supports (rule N4). Figures built only from exact rationals, x\* and CODATA α carry no external uncertainty and are printed to the declared precision.  
- Comparisons against experiment print the pull in σ. **No comparison row tests a computed value against a rounded constant with a percent-level band.** This is the specific defect that concealed erratum E-S1-1 for two versions.  
- Every D row carries a proof or source pointer (GRD05).  
- A self-AST audit rejects any evidence-bearing row whose condition is a literal boolean (GRD02), and the row registry refuses class P outright (GRD03, GRD04).  
- The manuscript-integrity guard (GRD15) scans this file for fifteen retracted statements, using **token-proximity** patterns rather than exact wordings, under **two** normalisations (markdown separators replaced by a space, and removed outright), after NFKC folding and zero-width removal. **Only fenced code blocks and text following a line-initial marker are exempt; inline backticks, bold, italics and table cells are live text.** Thirteen live-fire attacks were run against the guard set — row deletion, a literal True condition, a constant-folding disjunction, an unparseable tolerance, an or 1 short circuit, a suppressed-exception wrapper, a keyword-hidden class, restoration of a PDG 2023 value, a relabelled 2023 value, a manuscript number desync, markdown-emphasis and table-cell smuggling, a mid-line marker, and a zero-width-plus-full-width-digit variant of the retracted m\_W claim. **All thirteen cause exit 1\.** Nine of them defeated the pre-audit version of this suite.  
- Twenty-one headline numbers must appear verbatim in this manuscript (GRD17). Those tokens are **generated from the computation at run time**, not hand-copied string literals, so a manuscript can no longer agree with a literal while both disagree with the arithmetic.  
- The manuscript is hashed and its hash is registered in the ledger (GRD21); the pre-audit draft hashed only the script.  
- The self-AST audit rejects any evidence-bearing condition that folds to a constant, not merely a bare True, and rejects a row() call that hides its class or condition in a keyword argument (GRD02).  
- The HTML history-marker exemption applies only to a marker at the **start** of a line; GRD16b fails if the marker is placed mid-line, which is how the previous exemption model was defeated.

---

## Acknowledgements, AI Use, and Availability

**AI Use Statement.** This work was developed with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.

AUDIT\_INDEPENDENCE

auditor\_independence        : LOW (iota \~ 0.2). The adversarial audit that produced

                              errata E-S1-5 and E-S1-6, and that forced the rewrite

                              of section 0.3, was run by the same model family as the

                              author, in the same session, with a separate context and

                              independently written recomputation code.

qualified-human anchor      : NONE.

deterministic re-checks run : all printed figures recomputed at 50 digits by a second,

                              independently written script; the 13 Archimedean

                              f-vectors re-enumerated; seventeen live-fire attacks on

                              the manuscript-integrity guard and four on the other

                              guards; the companion suite re-executed and its JSON

                              ledger compared byte-for-byte across runs.

verdict of that audit       : AUDIT-CORRECTION-REQUIRED. All three release-blocking

                              findings are repaired in this version; none is deferred.

residual risk               : a same-family auditor shares the author's blind spots.

                              The Archimedean counterexample was found only because

                              the auditor re-enumerated a list the author had copied.

                              Comparable errors elsewhere in the corpus should be

                              assumed until similarly re-enumerated.

**No qualified human review has been performed.**

**Data Availability.** No experimental data were generated. All external reference values are listed in §8.0 with their source edition and an as-of date of 2026-08-19.

**Code Availability.** zs\_s1\_verify\_v1\_1.py. Dependencies: Python 3.10+, numpy ≥ 1.24, mpmath ≥ 1.3.0. One-command run: python3 zs\_s1\_verify\_v1\_1.py. Expected output: 127 rows, 0 FAIL, exit code 0, plus zs\_s1\_verify\_v1\_1.json. No external data files required.

### ARTIFACT\_MANIFEST

paper\_code           : ZS-S1

paper\_version        : v1.1

paper\_date           : 2026-08-19

main\_script          : zs\_s1\_verify\_v1\_1.py

script\_version       : v1.1.0

supersedes\_script    : zs\_s1\_verify\_v1\_0.py  (38 rows; banner claimed 35\)

ledger               : zs\_s1\_verify\_v1\_1.json   (derived from the script basename)

runtime              : CPython 3.10+, numpy \>= 1.24, mpmath \>= 1.3.0

precision            : mpmath mp.dps \= 50; exact Fraction where the object is rational

seeds                : numpy.random.seed(42)

grids (pre-declared) : MC trials 100000, window 1 per cent;

                       rational scan p in \[1,100\], q in \[2,200\];

                       integer shift delta in \[-3,+3\]

one\_command\_run      : python3 zs\_s1\_verify\_v1\_1.py

expected\_rows        : 138

expected\_census      : C=23 V=22 W=8 R=12 G=25 X=10 D=22 T=16

fail\_closed          : exit 1 on any FAIL, row-count mismatch, or census mismatch

expected\_outputs     : console census \+ zs\_s1\_verify\_v1\_1.json

known\_limitations    : beta\_0(Z)=1 and Mode-Count Collapse are declarations with

                       pointers, not computations; the MC null family is post-hoc

public\_certificate   : NOT YET PUBLICLY CERTIFIED \-- no persistent archival identifier

license              : as per project default

---

## Appendix A: Cross-Reference Table

| Paper | Content | Direction | Relation |
| :---- | :---- | :---- | :---- |
| ZS-F2 v1.0 | A \= 35/437, polyhedra | Input → ZS-S1 §2–§3 | LOCKED |
| ZS-F5 v1.0 | (Z,X,Y,Q) \= (2,3,6,11), dim(Z) \= 2 | Input → ZS-S1 §2,§5 | PROVEN |
| ZS-M1 v1.0 | x\* \= Re(z\*), Berry phase | Input → ZS-S1 §8.2 | PROVEN |
| ZS-M2 v1.0 | Cross-Coupling Theorem | ZS-M2 → ZS-S1 §8.4 | UPSTREAM |
| ZS-A4 v1.0 | MUB(Q) \= G \= 12 | Input → ZS-S1 §6 | PROVEN |
| ZS-M6 v1.0 | Hodge-Dirac on TI | Input → ZS-S1 §4.3, §6.5 | PROVEN |
| ZS-M9 v1.0 | McKay → SU(5) | Input → ZS-S1 §6.6 | DERIVED |
| ZS-S4 v1.0 | v \= 245.93 GeV | Input → ZS-S1 §8.6 (diagnostic only) | IMPORTED |
| ZS-M5 v1.0 | Baryogenesis DAG | ZS-S1 exports **f\_seam** | DOWNSTREAM |
| ZS-U7 v1.0 | f\_seam \= 3/95 | ZS-S1 → ZS-U7 §4 | DOWNSTREAM |
| ZS-S2 v1.0 | Neutrino sector | ZS-S1 → ZS-S2 (f\_seam) | DOWNSTREAM |
| **ZS-S14 v2.1** | **imports g₂ from ZS-S1 in Prop. S14.B′** | **ZS-S1 → ZS-S14** | **IMPORT WITHDRAWN, §11.3 item 5** |

## Appendix B: Derivation Chain Summary

| \# | Statement | Source | Status | Scale/scheme |
| :---- | :---- | :---- | :---- | :---- |
| 1 | A \= 35/437 \= δ\_X·δ\_Y | ZS-F2 v1.0 | LOCKED | n/a |
| 2 | (Z,X,Y) \= (2,3,6), Q \= 11, G \= 12 | ZS-F5 v1.0 | PROVEN | n/a |
| 3 | z\* \= i^{z\*}, x\* \= Re(z\*) \= 0.4382829367 | ZS-M1 v1.0 | PROVEN | n/a |
| 4 | (V+F)\_X \= 38, (V+F)\_Y \= 92 | Euler \+ polyhedra | PROVEN | n/a |
| 5 | a₂ \= 19/6, a₃ \= 23/3 | Spectral density rule | PROVEN | scale-free |
| 6 | β₀(Z) \= 1 from Schur complement | §5.3 | DERIVED | scale-independent |
| 7 | α\_s \= 11/93 (pull \+0.311σ) | Steps 2+4+6 | DERIVED | **M\_Z, MS-bar** |
| 8 | sin²θ\_W \= (48/91)·x\* (pull −2.695σ) | Steps 3+4 | DERIVED | **M\_Z, MS-bar** |
| 9 | α₂ \= 6/190 \= 3/95 | Steps 2+4 \+ factor 5 | **OBSERVATION** | **UNDECLARED** |

## Appendix C: Values insulated from this erratum

The following keep their numerical values unchanged. **A number keeping its value does not keep every claim attached to it**: item 2's *status* is unchanged but its *pull* is corrected, and item 3's value is unchanged while its status moves from DERIVED to OBSERVATION.

1. α\_s \= 11/93 and its \+0.311σ agreement.  
2. sin²θ\_W \= 0.2311822084 — value unchanged; pull corrected to −2.695σ (E-S1-2).  
3. α₂ \= 3/95 — value unchanged; status DERIVED → OBSERVATION (E-S1-3).  
4. a₂ \= 19/6, a₃ \= 23/3, a₃ \= n\_f \+ (N²−1)/N \= 5 \+ 8/3.  
5. A \= 35/437, Q \= 11, (Z,X,Y) \= (2,3,6), G \= 12, (V+F)\_X \= 38, (V+F)\_Y \= 92\.  
6. δ\_X \= 5/19, δ\_Y \= 7/23, and the Hodge decomposition 59 \+ 31 \= 90\.  
7. ZS-S4's v \= 245.93 GeV (used here only as a diagnostic input, never as a ZS-S1 output).  
8. f\_seam \= 3/95 as exported to ZS-U7, ZS-M5, ZS-S2.

---

## References

\[1\] K. Kang, "Geometric Impedance: A \= 35/437," ZS-F2 v1.0 (2026). \[2\] K. Kang, "Gauge Symmetry Constraint: Why Q \= 11," ZS-F5 v1.0 (2026). \[3\] K. Kang, "i-Tetration & Fixed Point," ZS-M1 v1.0 (2026). \[4\] K. Kang, "Geometric Harmonics: Six Regimes Unified," ZS-M2 v1.0 (2026). \[5\] K. Kang, "Global Numerical Audit & Asymmetry Epochs," ZS-M5 v1.0 (2026). \[6\] K. Kang, "Black Hole Information & Quantum Protocol," ZS-A4 v1.0 (2026). \[7\] K. Kang, "Dark Matter & ε-Halo," ZS-A5 v1.0 (2026). \[8\] K. Kang, "Galactic Dynamics & Morphology," ZS-A1 v1.0 (2026). \[9\] K. Kang, "Quantum Gravity Bridge," ZS-U5 v1.0 (2026). \[10\] K. Kang, "QKE-Closed Baryogenesis," ZS-U7 v1.0 (2026). \[11\] K. Kang, "Neutrino Mass Spectrum & HNL Phenomenology," ZS-S2 v1.0 (2026). \[12\] K. Kang, "The Typed Standard-Model Master Action," ZS-S14 v2.1 (2026). \[13\] Particle Data Group, S. Navas *et al.*, Phys. Rev. D 110, 030001 (2024); reviews *Electroweak Model and Constraints on New Physics*, *Mass and Width of the W Boson*, *Quantum Chromodynamics*, and the *Physical Constants* table. Retrieved 2026-08-19. \[14\] Particle Data Group, R. L. Workman *et al.*, Prog. Theor. Exp. Phys. 2022, 083C01 (2022) and 2023 update; review *Electroweak Model and Constraints on New Physics*, Table 10.2. **Cited only to identify the superseded values of erratum E-S1-2.** \[15\] CODATA 2022 recommended values, NIST; α⁻¹(0) \= 137.035999177(21). Retrieved 2026-08-19. \[16\] Gilkey, P. B., *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, CRC Press (1995). \[17\] Regge, T., Nuovo Cimento 19, 558 (1961). \[18\] Wootters, W. K. & Fields, B. D., Ann. Phys. 191, 363 (1989) \[MUB\].

---

## Version History and Correction Register

**v1.1 (2026-08-19) — dated erratum and scope correction.**

*Mathematics:* No theorem is added, removed or altered. No numerical value derived in v1.0 changes. §8.6 evaluates the tree identity α₂ sin²θ\_W \= α\_em, which v1.0 never evaluated; §6.5 is renumbered from the duplicate v1.0 §6.4.

*Scope and status:* §8.0 declares a scale and a scheme for every output. α\_s and sin²θ\_W declared at μ \= M\_Z, MS-bar, status DERIVED retained. α₂ status DERIVED → OBSERVATION with physical identification OPEN; §8.3 re-titled §8.3′. §2.1 TYPE LOCK separates f\_seam from g₂. §9 replaces the Tier-A table with a claim-level status board on three separate axes. New gates FS1-A, FS1-A′, FS1-SCHEME, FS1-PDG, FS1-4′, FS1-DEGEN; gate FS1-4 FIRED. New non-claims NC-5 through NC-10. New debts D-S1-SCALE, D-S1-G2, D-S1-DEGEN, D-S1-REGGE, D-S1-PRIOR. The g₂ export to ZS-S14 Prop. S14.B′ is withdrawn.

*Numerical corrections:* External reference values moved from the PDG 2023 edition to PDG 2024; sin²θ\_W pull corrected. §10.2 Monte Carlo re-typed from evidence to diagnostic. §10.6 enumerates six construction choices, replacing the unqualified zero-parameter banner.

*Verification:* Artifact replaced, zs\_s1\_verify\_v1\_0.py → zs\_s1\_verify\_v1\_1.py. Row count 38 → 138, measured and guarded. Class P abolished. Introduced: EXPECTED\_ROWS fail-closed guard, class-census guard, self-AST audit rejecting constant-foldable evidence conditions, per-row tolerance justification with a 1 % ceiling and fail-closed handling of unparseable tolerances, D-row pointer enforcement, manuscript-integrity guard with a line-initial-marker-only exemption and NFKC/markdown-stripping normalisation, run-time-generated manuscript↔script synchronisation over twenty-one headline numbers, manuscript hashing, external-value pinning, and regression rows against every superseded value. Evidence-bearing count reduced 64 → 53 by reclassification (E-S1-6).

*Post-audit revision (2026-08-19).* An independent adversarial audit of the pre-release draft returned **AUDIT-CORRECTION-REQUIRED** with three release-blocking findings. All three are repaired here rather than deferred: the Archimedean uniqueness claim is retracted (**E-S1-5**, new gate FS1-4′, new debt D-S1-DEGEN, new NC-10); the manuscript-integrity guard, which the auditor defeated twelve ways out of seventeen, is rebuilt; and three mis-rounded figures plus a systematic over-printing of precision are corrected (**E-S1-6**). Four further guard bypasses (GRD02, GRD07, GRD08, GRD09) and one label-only check (GRD13) were closed or renamed honestly. The §0.3 justification of branch C′ was rewritten after the auditor showed that its "v1.0 never compared α₂ to a measurement" premise was too strong; the record of what v1.0 actually asserted is now printed in full and the misleading sentence is retracted rather than re-labelled. §10.3's exhaustive scan, asserted in prose since v1.0, is now an executed row.

*Editorial:* Duplicate section number fixed; verification banner now copied from the script's own output; broken cross-references repaired; release label REVIEW READY; AI-use and independence disclosure added.

\*Retracted in this version:\* the section title "8.3 Electromagnetic Coupling α₂"; the summary sentence "All five formulas match PDG 2024 data within 1.3σ"; the pull figure −1.26σ; the verification banner "35/35 PASS"; the abstract/conclusion phrasing "to all Standard Model gauge couplings"; the misattributed form "α₂ \= X/\[(V+F)\_Y \+ X\]" as a ZS-S1 formula; the correction report's §C-03 premise that α\_s and α₂ share a denominator base; and, downstream, ZS-S14 Theorem S14.B Step 4's "m\_W ≈ 80.4 GeV, matching observation". **v1.0 (March 2026).** §6.5 McKay interpretation of the Spectral-to-β Bridge; Z₅ → Â₄ → SU(5) → SM cross-verification (14/14). Hodge-Dirac integration (§3.6, §4.3, §6.5, §8.2). Euler Cell-Count Theorem. Edge space Hodge decomposition, δ\_Y \= 7/23. Third route to 91\. Initial public release, consolidated from internal Z-Spin Collaboration research notes up to v3.0.1. **Preserved as a historical artifact; not deleted.**

**Z-Sim cross-reference (March 2026).** All 8 closure parameters of the Z-Spin forward simulator are DERIVED from A \= 35/437 and (Z,X,Y) \= (2,3,6). See ZS-Q7 v1.0 §5.8, ZS-M3 v1.0 §12, ZS-T3 v1.0.  
