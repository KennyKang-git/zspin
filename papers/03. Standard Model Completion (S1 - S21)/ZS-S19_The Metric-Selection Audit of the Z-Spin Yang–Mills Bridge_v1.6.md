# **ZS-S19**

# **The Metric-Selection Audit of the Z-Spin Yang–Mills Bridge**

**The Anchoring Defect Identity, the Regge-Moduli Exclusion of Circumcentric Hodge Stars, the Corrected Magnus Quartic, and the Finite Gauss–Faddeev–Popov Programme**

Author: Kenny Kang  
Affiliation: Z-Spin Cosmology Collaboration  
Date: July 2026  
Theme / Paper Code: Standard Model — ZS-S19  
Version: v1.6 (fifth major revision; v1.1–v1.5 were internal)  
Immediate predecessors: ZS-S18 v1.6 FINAL, ZS-S17 v2.2 FINAL  
**Epistemic tags: counting-star selection DERIVED-CONDITIONAL on (R\_C); circumcentric-Regge exclusion PROVEN, and its bearing on metric selection conditional on (H-UA)**

**Verification: 95/95 computed & proof checks PASS | 7 OPEN gates printed and NOT counted | Zero Free Parameters | A \= 35/437, Q \= 11, dim(Z) \= 2 LOCKED, unchanged | Retraction ledger updated; three headline retractions and additional internal corrections fully documented: the ZS-S18 §7 quartic sign, the −3.868 % alarm as a ledger statement, and this paper's own v1.0 necessity claim**  
*Companion code: zs\_s19\_verify\_v1\_6.py — one self-contained file, requiring numpy, scipy and mpmath, no data assets, writes nothing, runtime ≈ 36 s.*

## **§0. Abstract**

ZS-S18 v1.6 handed forward four debts, of which the metric-weight gate F-S18.16 was flagged as the one able to invalidate the corpus: applying the corpus's own discrete-exterior-calculus (DEC) metric to the truncated icosahedron (TI) was reported to shift the face-Laplacian gap from the locked λ₁ \= 1.2428416164 to 1.1947657995, a change of −3.868 %, outside the anti-numerology band 89/3600 \= 2.4722 %. This paper audits that gate. It does not close it. It reduces it, precisely, to one residual ratio, with its counting selection conditional on the axiom (R\_C) and the circumcentric-route exclusion separately conditional on the axiom (H-UA), and it shows that the alarm as stated was not a well-posed comparison.

Four results are established. Theorem S19.1 (Normalization Ambiguity): the DEC edge star ⋆₁ \= |dual|/|primal| is a ratio of lengths and is unambiguous, whereas the face star ⋆₂ \= 1/(a\_TI² A\_f) carries dimension L⁻² and is defined only once an edge length is declared. At the natural choice a\_TI \= 1 the full-DEC gap is 0.3600376672, a shift of −71.031 %; the locked value is reproduced at a\_TI \= 0.5382277383; and the handover's 1.1947657995 corresponds to the undeclared implicit choice a\_TI \= 0.5489498022. A single genuine rescaling already sweeps λ₁ over (0, ∞), so the −3.868 % comparison is retracted as a ledger statement.

Theorem S19.2 (Anchoring Defect Identity): for every I\_h-invariant diagonal DEC metric and every eigen-channel λ of Δ₂, the departure of the ZS-S18 harmonic anchoring identity from exactness has the closed form dev(λ) \= −\[W₅₆ S₅₆(λ) \+ W₆₆ S₆₆(λ)\], where W\_o is the orbit-wise compatibility defect — the sum of the two adjacent face stars minus twice the edge star — and S\_o(λ) is the share of the coexact-potential norm carried by edge orbit o. Residual below 10⁻¹² over six random metrics and nine channels; observed residuals are O(10⁻¹⁴) and BLAS-dependent, so the ledger records the threshold and not the run value.

That identity forces a retraction of this paper's own v1.0 claim. v1.0 asserted that the λ₁-channel anchoring identity is equivalent to pointwise star compatibility. It is not: in one channel it is a single scalar condition on three independent metric ratios, and an external reviewer's explicit counterexample — (M₁,₅₆, M₁,₆₆, M₂,₅, M₂,₆) \= (1, 2, 1.3231366438740746, 1\) — satisfies it to 1.6 × 10⁻¹⁵ while violating compatibility. It is reproduced here. Quantitatively the single-channel condition is worthless: along its zero locus λ₁ spans 0.804719 to 1.249689, that is −35.3 % to \+0.6 %. The v1.0 necessity claim is RETRACTED.

Theorem S19.2′ (Universal Anchoring) restores necessity in a strictly stronger and honest form. Because Lemma S18.A and the fact that every edge of a closed 2-complex bounds exactly two faces are both channel-agnostic, the anchoring identity is naturally read as a property of the complex rather than of one mode. Demanding it in two or more channels with independent (S₅₆, S₆₆) rows is equivalent to W₅₆ \= W₆₆ \= 0, that is to pointwise star compatibility: the 9 × 2 channel matrix has rank two on every metric sampled, minimum second singular value 0.0532, and the (λ₁, λ\_h) determinant at the counterexample is −0.009825. This universality is registered as an added structural axiom (H-UA), not as a theorem of ZS-S14. Under it, compatibility eliminates the scale gauge outright and reduces three metric ratios to one.

Two consequences follow. The Euclidean circumcentric DEC metric is excluded for every edge length: it meets the λ₁ channel only at a\_TI\* \= 0.5429961198, where λ₁ \= 1.2211091536, but there the λ\_h channel is violated at −4.4 × 10⁻³. And the residual one-parameter family is the compatibility line ρ\_E \= (1 \+ ρ\_F)/2, along which the gap remains threefold at all sampled points of the audited domain ρ\_F ∈ \[10⁻⁴, 10⁶\], thirteen decades — so the T₁ identification remains verified throughout the audited domain, although no global no-crossing theorem is claimed — and along which, over ρ\_F ∈ \[1, A₆/A₅\], λ₁ moves by at most 0.992 % and Λ\_QCD stays within 261.5–264.1 MeV, inside the quenched lattice bar 260 ± 20 MeV.

The last ratio is not closed by the Haar measure, and v1.0's argument that it was is WITHDRAWN: the product Haar measure fixes the form of the electric term but not its coefficients, and a bi-invariant metric on a product group admits an independent positive scale on each factor, so I\_h symmetry alone permits κ₅₆ ≠ κ₆₆. A second correction is issued against v1.2 of this paper. Performing the Legendre transform, Π \= (1/g²)M₁Ω gives H\_E \= (g²/2)ΠᵀM₁⁻¹Π, so the Hamiltonian electric coefficient is κ\_e \= (M₁⁻¹)\_e and star compatibility reads κ\_e \= 2/(β\_{f₁} \+ β\_{f₂}), the HARMONIC mean; v1.2 printed the arithmetic mean, which is the Lagrangian relation mislabelled. The two coincide at the counting point, so no ledger number moves, and the equation of motion returns the same Δ₂ either way, but the physical reading off that point differs. What compatibility does supply is that the electric weights are not independent data, so exactly one ratio β₅/β₆ remains.

Theorem S19.6 (Regge-Moduli Exclusion) settles the diagonal circumcentric Regge-metric route completely, and in closed form. Because the TI has two edge orbits, an I\_h-invariant piecewise-flat metric with cyclic faces is a two-parameter family: a scale s and a shape t \= ℓ₆₆/ℓ₅₆. Compatibility imposes two conditions, the scale cancels, and one scalar equation Q(t) \= 1 remains. Writing u for the cotangent of the hexagon half-angle and c \= cot(π/5), the defect is a rational function, Q − 1 \= P(u)/\[20c(√3u − 1)(u \+ c)\], with P(u) \= 3√3u³ \+ (27 − 20√3c)u² \+ (15√3 \+ 40c − 20√3c²)u \+ (20c² \+ 20√3c − 9). Exactly, c² \= (5 \+ 2√5)/5, a₀ \= 11 \+ 8√5 \+ 20√3c and a₁ \= −5√3 \+ 40c − 8√15, all positive. P′ has two positive roots, 0.4484088862 and 2.2047424786, so P rises, falls and rises on \[0, ∞) and min\_{u≥0} P \= min(P(0), P(u₊)) \= min(76.5678121575, 65.7130202935) \= 65.7130202935 \> 0\. No discriminant is needed. The bound is certified by outward-rounded interval arithmetic, P(\[2.20, 2.21\]) ≥ 64.8013718922, and corroborated by an independent tail argument (for u ≥ 4, a₃u \+ a₂ \= 0.1053413533 \> 0, so P is positive termwise). Hence Q(t) \> 1 for EVERY t \> 0, on the physical domain u \> 1/√3 where the denominator is positive. This is a certified proof, not the 4000-point scan v1.3 offered. The true minimum is Q \= 1.1463953345 at t \= 2.4107050485, a floor of 14.64 % on the defect; particular realizations give 1.3986482220 (intrinsic flat), 1.3782723424 (Euclidean embedding) and 1.4146772905 (geodesic sphere). The intersection of the compatibility submanifold with the circumcentric metric-induced locus is EMPTY.

Theorem S19.7 (Counting-Trace Selection): if the regulator integral on the cell complex is the cellular counting trace — axiom (R\_C), every oriented k-cell carrying unit measure irrespective of its boundary degree — then ⋆\_k \= |⋆σ| / |σ| \= 1 identically, so M₁ \= M₂ \= I, compatibility holds identically, and Δ₂ \= B₂B₂ᵀ with λ₁ \= 1.2428416164. (R\_C) is a NEW axiom, strictly stronger than ZS-S7 §1's regulator axiom (R): (R) denies an ambient metric, but a weight w\_f \= ψ(n\_f) is metric-free too, and since n\_f takes only the values 5 and 6, ψ realizes ANY positive ratio ρ\_F \= ψ(5)/ψ(6). v1.2 claimed the counting star followed from (R) alone and described the residual as a finite list of five candidates; both claims are RETRACTED. The residual under (R) alone is a continuous one-parameter family, and the five candidates audited below are natural choices, not a classification.

The two results must not be bundled, and v1.4 bundled them. (R\_C) by itself gives M₁ \= M₂ \= I and hence λ₁ \= 1.2428416164; (H-UA) is not needed for that step. (H-UA) is what makes star compatibility the criterion, and hence what gives Theorem S19.6 its bearing on metric selection. So the correct tags are: the counting-star selection and ρ \= (1,1) are DERIVED-CONDITIONAL on (R\_C) ALONE; Theorem S19.6 is PROVEN outright as geometry, and the exclusion of the circumcentric route as a selection statement is PROVEN under (H-UA); and the fact that the two point the same way is joint corroboration, not a shared dependency. The audited candidates leave the gap 3-fold, move λ₁ within \[−4.040 %, \+0.955 %\], and give Λ\_QCD ∈ \[261.6, 275.3\] MeV, inside the quenched lattice bar; one exceeds the internal anti-numerology band and is recorded rather than suppressed. A third self-retraction is issued here: v1.3 claimed that band held over the whole compatibility line. It does not — Λ\_QCD diverges as ρ\_F → 0 and tends to 429.7 MeV as ρ\_F → ∞ — so the band belongs to the audit window only, and the associated falsification gate is rewritten. F-S18.16 is therefore reduced and conditionally selected, not closed. What remains, F-S19.6, is the explicit cellular reduction of the ZS-S14 action and its Legendre transform, with four outcomes pre-registered; three of the four would force revision of this paper, so it is a decision gate, not a confirmation.

Independently of the metric line, Lemma S19.4 derives the O(g⁴) Wilson–Magnus combination analytically as Tr(Y₂² \+ 2Y₁Y₃ − Y₁⁴/12) and retracts the sign carried in the ZS-S18 §7 hand-off, the two candidates being separated by five orders of magnitude in residual at N \= 2, 3, 4\. §6 sets Part II up as a finite-matrix problem and reports its exact zeroth-order content, det′Δ₀ \= 60τ with τ \= 375291866372898816000 (Kirchhoff), together with the spectral gap 0.2434017461 and the associated norm scale σ\_min \= 0.4933576250; neither is claimed as a Gribov radius. §7 certifies the Part III census, Sym² of the 31 physical modes being 496 \= A\_g 12 ⊕ H\_g 140 (28 copies), and confirms independently the ZS-S18 correction to ZS-S7 §2.2. Seven gates remain OPEN.

*Keywords: Yang–Mills mass gap, discrete exterior calculus, Hodge star, truncated icosahedron, anchoring defect identity, star compatibility, normalization ambiguity, Wilson action, Magnus expansion, Faddeev–Popov operator, geometric impedance, zero free parameters, Z-Spin Cosmology.*

## **§0.1 Epistemic Status Legend**

*Rule box. Every claim carries exactly one tag. A tag is never claimed above what the evidence supports; an OPEN gate is never counted as a PASS; a value obtained in a degenerate eigenbasis never enters the ledger unless exactly invariant under rotations of that eigenspace; and — added as disciplines 16 and 17 — an equivalence is never asserted from a restricted slice of the parameter space.*  
Table 0.1. Epistemic Status Legend as used in ZS-S19 v1.6.

| Status | Definition | Used in ZS-S19 v1.6 for |
| ----- | ----- | ----- |
| LOCKED | Core constant fixed upstream; no downstream paper may modify. | A, Q, dim(Z), v |
| PROVEN | Mathematical theorem, standard mathematics alone, machine-verifiable. | Thm S19.1, Thm S19.2, Thm S19.2′, Cor S19.2a, Thm S19.6 (interval-certified), Lemma S19.4 |
| DERIVED | Z-Spin action plus standard physics, zero free parameters. | no headline result of this paper carries this tag |
| DERIVED-CONDITIONAL | DERIVED conditional on a listed axiom or upstream theorem. | Thm S19.7; ρ \= (1,1) and λ₁, on (R\_C) ALONE |
| CONDITIONAL-BOUNDED | Conditional, with the residual freedom explicitly bounded. | Λ\_QCD ∈ \[261.6, 275.3\] MeV over the audited candidates |
| VERIFIED | Numerical confirmation at a stated precision. | the 95-check suite |
| CERTIFIED | Machine precision with an explicit invariance assertion. | block census 496 \= A\_g 12 ⊕ H\_g 140 |
| COMPUTED | A number extracted numerically; no closed form asserted. | det′Δ₀, spectral gap 0.2434, σ\_min 0.4934 |
| TESTABLE | Pre-registered prediction with a falsification protocol. | F-S19.5 |
| HYPOTHESIS-strong | Multiple structural anchors; promotion path documented. | (H-UA) universality; (R\_C) the cellular counting trace |
| OBSERVATION | Empirical regularity, origin pending. | flatness of λ₁ along the compatibility line |
| NON-CLAIM | Explicit declaration of what is NOT asserted. | NC-S19.1 – NC-S19.21 |
| OPEN | Recognized gap, honestly registered. | F-S19.1 – F-S19.4, F-S19.6 – F-S19.8 |
| RETRACTED | Earlier claim withdrawn after falsification. | ZS-S18 §7 quartic sign; the −3.868 % ledger statement; v1.0's necessity claim, Haar argument and four-gauge table; v1.2's Hamiltonian compatibility relation, its (R)-only selection and its finite-residual claim |
| IMPORTED | Proved externally or upstream, used without re-proof, cited. | axiom (R) from ZS-S7 §1; Kirchhoff, Peter–Weyl, Dodziuk–Patodi |

## **§1. Introduction**

### **1.1 Where the bridge stood**

The Z-Spin physical bridge is the chain S14 action → measurement instrument → L\_Z transfer operator → gauge observable → data. ZS-Q18 v1.7 closed the measurement layer to better than ninety per cent, ZS-M53 v1.5 proved mean-channel closure for the operator layer, ZS-S17 v2.2 closed the antisymmetric gauge-observable channel, and ZS-S18 v1.6 closed the symmetric channel, the gauge-covariant cubic action bridge and the entire leading exchange sector, the last of these analytically through Theorem S18.6A′, G\_exch \= (9/4)√λ₁ Σ\_r c²\_{r,pol} \= 0.313264316799300.

What remained was not more representation theory. It was the Hamiltonian: four named debts — F-S18.16 (metric weight), F-S18.4 (full-mode dynamics), F-S18.10 (non-abelian Gauss law) and F-S18.13 (coupling scheme and scale). Every one is a finite problem on a 60 / 90 / 32 cell complex, requiring no new geometry and no new constant.

### **1.2 The alarm this paper answers**

The ZS-S18 handover raised one of the four to the top of the queue and marked it urgent. ZS-S7's λ₁ \= 1.2428416164 is the spectral gap of the unweighted combinatorial face Laplacian B₂ᵀB₂. ZS-S17 had, separately, computed circumcentric dual weights on the same complex — dual/primal edge ratio φ \= 1.618034 on the hexagon–hexagon edges and 1.4734 on the pentagon–hexagon edges. Applying the corpus's own DEC metric consistently, edge star M₁ together with face star ⋆₂ ∝ 1/A\_f, was reported to give

lambda\_1(full DEC) \= 1.1947657995     vs   locked 1.2428416164     shift  \-3.868 %

which lies outside the corpus's own anti-numerology band 89/3600 \= 2.4722 %. Downstream, Λ\_QCD ∝ 1/λ₁ would move 264.1 → 274.7 MeV, and c₁, G\_exch, G\_∞ and λ\_t would all shift. A pre-registered hard fork was written into the handover: if the ZS-S14 action forces ρ ≠ (1,1), stop, rewrite ZS-S7 first, and only then resume Parts II–IV.

### **1.3 What this paper does, and what v1.0 claimed wrongly**

v1.0 of this paper claimed outcome 1 of the pre-registered trichotomy: ρ \= (1,1) forced, F-S18.16 closed, the metric convention derived. External review refuted two of its three supporting arguments; a second cycle found two further defects in the repair, and a third found a scan presented as a proof. This version, v1.6, is the result. It does not claim a closure. It establishes an exact defect identity for the anchoring condition (§4.2), retracts the necessity claim built on it (§4.3), restores necessity in a strictly stronger multi-channel form under a named axiom (§4.4), uses that to exclude the circumcentric candidate outright (§4.5), and reduces the metric freedom from three ratios to one with a bounded consequence for Λ\_QCD (§4.6). The Haar-democracy argument that v1.0 used to close the last ratio is withdrawn (§4.7); the metric route is closed negatively over the full Regge moduli (§4.9); the counting star is selected by an explicitly new axiom (R\_C) rather than by the corpus axiom (R), which does not suffice (§4.10); and the real action-level gate is registered OPEN as F-S19.6 with four pre-registered outcomes. §5 to §7 discharge what can be discharged of Parts I.b, II and III.

The reviewer's counterexample is reproduced in the companion code and is the pivot of the revision. It is stated in full at §4.3 rather than paraphrased, because a retraction that hides its own falsifier is not a retraction.

### **1.4 A correction issued against a predecessor**

In the course of Part I.b this paper retracts a formula of its own predecessor. ZS-S18 §7 hands forward the exact Wilson quartic as the Magnus combination Tr(Ω₂² \+ 2Ω₁Ω₃ \+ Ω₁⁴/12). The sign of the last term is wrong. Lemma S19.4 derives −Ω₁⁴/12 analytically and confirms it numerically against an independent extraction. ZS-S18's own §4.1 body text already carried the correct sign, so the error is confined to the hand-off sentence; it is corrected here before it can propagate.

### **1.5 Organization**

§2 collects locked inputs and audits the zero-free-parameter claim. §3 proves the Normalization-Ambiguity Theorem and withdraws v1.0's four-gauge table. §4 is the core: the Anchoring Defect Identity (§4.2), the retraction of the v1.0 necessity claim with the reviewer's counterexample in full (§4.3), the restoration of necessity under the axiom (H-UA) (§4.4), the exclusion of the circumcentric Euclidean star (§4.5), the residual one-parameter family (§4.6), the withdrawal of the Haar argument together with the corrected Legendre dictionary (§4.7), the Regge-moduli exclusion (§4.9), the Counting-Trace Selection Theorem under the new axiom (R\_C) (§4.10), and the status of F-S18.16 (§4.8). §5 gives Part I.b and the Magnus quartic. §6 gives Part II at zeroth order. §7 gives the Part III block census. §8 reports Part IV status. §9 is the cross-paper dependency audit. §10 is the external-data confrontation. §11 registers the multi-layer falsification gates, §12 the non-claims, §13 the verification suite, §14 the conclusions.

## **§2. Locked Inputs and the Zero-Free-Parameter Audit**

### **2.1 Imported constants**

ZS-S19 introduces zero new fitted numerical parameters, zero new geometric constants and zero new fields. It DOES introduce two new structural hypotheses, (H-UA) and (R\_C), which are stated explicitly, firewalled, and carried in every status tag that depends on them; the claim is zero free parameters, not zero new assumptions. Every numerical quantity below is LOCKED, PROVEN or DERIVED upstream.  
Table 2.1. Locked and imported inputs. No entry is re-fitted in this paper.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080091533 | ZS-F2 §7 | LOCKED |
| Q (register dimension) | 11 | ZS-F5 §4 | PROVEN |
| (Z, X, Y) sector dimensions | (2, 3, 6\) | ZS-F5 §4 | PROVEN |
| δ\_X , δ\_Y | 5/19 , 7/23 | ZS-F2 | PROVEN |
| v (electroweak VEV) | 245.93 GeV | ZS-S4 §6.12 | DERIVED |
| TI complex | V \= 60, E \= 90, F \= 32, χ \= 2 | ZS-F5, ZS-M6 §5 | PROVEN |
| λ₁ (TI face-Laplacian gap) | 1.2428416164 | ZS-S7 §2 | LOCKED → DERIVED-CONDITIONAL on (R\_C) |
| λ\_h (second T₁ copy) | 7.5210904061 | ZS-S17 | CERTIFIED |
| Λ\_QCD | 264.1 MeV | ZS-S7 §5 | DERIVED-CONDITIONAL |
| m(0⁺⁺) | vA/Q \= 1.7906 GeV | ZS-S7 §6 | DERIVED-CONDITIONAL |
| α\_s(M\_Z) | 11/93 \= 0.118280 | ZS-S1 | DERIVED |
| anti-numerology band | 89/3600 \= 2.4722 % | ZS-S17 | LOCKED |
| DEC circumcentric ratios | (6,6): φ \= 1.6180339887 ; (5,6): 1.4733704196 | ZS-S17; recomputed here | COMPUTED |
| TI face areas (edge \= 1\) | A₅ \= 1.7204774006 ; A₆ \= 2.5980762114 | this paper | COMPUTED |
| TI edge orbits | 60 (5,6)-edges \+ 30 (6,6)-edges | this paper | PROVEN |
| harmonic anchoring value | −0.6092155054875 | ZS-S18 Thm S18.4 | PROVEN |
| G\_exch | 0.313264316799300 | ZS-S18 Thm S18.6A′ | DERIVED-PERT-COND |

### **2.2 Notation warning, carried forward**

Four distinct objects share the letter λ and must not be confused: λ, the i-tetration multiplier of ZS-M1 with |λ| \= 0.891514; λ₁ \= 1.2428416164, the TI face-Laplacian gap; λ\_h \= 7.5210904061, the second T₁ copy; and λ\_t \= g²N ≈ 5.54, the 't Hooft coupling.

### **2.3 Anti-numerology and the zero-free-parameter audit**

The results of this paper are identities and exclusions, not numerical coincidences. Theorem S19.2 is an exact algebraic identity with residual below 10⁻¹² over random metrics and all nine channels, realized residuals being O(10⁻¹⁴) and BLAS-dependent; there is no hypothesis of chance agreement to test, so no Monte-Carlo control is applicable and none is claimed. Theorem S19.2′ is a rank statement about a 9 × 2 matrix. The exclusion of the circumcentric metric is a sign statement about a residual, not a proximity claim. Nothing in this paper is asserted on the strength of a numerical near-coincidence, and in particular ρ\_F \= 1 is NOT asserted on the strength of λ₁ landing near the locked value — that flatness is registered as an OBSERVATION and explicitly denied evidential force (NC-S19.5).

The audit trail for zero free parameters is as follows. A \= δ\_Xδ\_Y \= (5/19)(7/23) \= 35/437 is a ratio of cell counts and is metric-independent; the verifier confirms δ\_Y \= |V − F|/(V \+ F) \= 28/92 \= 7/23 directly from the TI census. Q \= 11 and dim(Z) \= 2 are PROVEN upstream and are not touched. The only quantity this paper could have tuned is the metric quadruple, and it is not tuned: it is constrained and the residual freedom is reported rather than fixed. No fudge factor, no fitted coefficient and no external constant enters any derivation in §§3–7. The one external number consumed anywhere in the paper is the buckyball spanning-tree count used as an independent check on det′Δ₀, and it is a combinatorial invariant, not a physical input.

## **§3. Part I.a, Step One — The Normalization-Ambiguity Theorem**

### **3.1 The parameter count, and a correction to ZS-S18 §4.7**

ZS-S18 v1.6 §4.7 reduced F-S18.16 to a single ratio ρ \= w₅/w₆ by observing that pentagons and hexagons are each one I\_h orbit. That reduction is incomplete. The 90 edges also split into two I\_h orbits, 60 pentagon–hexagon and 30 hexagon–hexagon, so the edge star contributes a second ratio.

**Proposition S19.0.** Every I\_h-invariant diagonal DEC metric on the truncated icosahedron is a quadruple (M₁,₅₆, M₁,₆₆, M₂,₅, M₂,₆) of positive numbers, that is three independent ratios after one overall scale. v1.0 of this paper worked, without saying so, on the two-dimensional slice M₁,₆₆ \= M₂,₆ \= 1, and that restriction is the source of its principal error. \[PROVEN\]

The generalized eigenproblem is

M1^{-1} B2^T M2 B2  a  \=  lambda a ,  
equivalently   Delta\_2 \= B2 M1^{-1} B2^T M2   on 2-cochains.

### **3.2 Theorem S19.1 (Normalization Ambiguity)**

**Theorem S19.1.** The DEC edge star ⋆₁ \= |dual edge| / |primal edge| is a ratio of two lengths and is therefore scale-free and unambiguous. The DEC face star ⋆₂ \= |dual vertex| / |primal face| \= 1/(a\_TI² A\_f) carries dimension L⁻², so under a uniform rescaling of the TI edge length the full-DEC spectrum obeys λ(a\_TI) \= λ(1)/a\_TI². Since the ZS-S14 master action assigns the internal complex no length scale — every locked corpus output referencing the TI, namely V, E, F, δ\_Y \= 28/92, α\_s \= 11/93, C\_M^sp and A \= δ\_Xδ\_Y, is a counting invariant — the full-DEC gap is not a number until a\_TI is declared, and no corpus paper declares it. \[PROVEN\]

Executed consequence.  
Table 3.1. The full-DEC gap as a function of the undeclared edge length. Computed by the companion code.

| a\_TI | λ₁(full DEC) | shift vs locked | remark |
| ----- | ----- | ----- | ----- |
| 1.0000000000 (natural) | 0.3600376672 | −71.031 % | the geometrically natural choice |
| 0.5489498022 | 1.1947654996 | −3.868 % | the choice implicit in the ZS-S18 handover, never stated |
| 0.5382277383 | 1.2428416164 | 0.000 % | the choice that reproduces the locked value exactly |

**Corollary S19.1a (retraction).** The statement 'λ₁ shifts by −3.868 % under the corpus's own DEC metric, outside the anti-numerology band' is RETRACTED as a ledger statement. It is a statement about an undeclared normalization, not about the metric. The companion asserts the number appears in no ledger entry.

**Withdrawal of a v1.0 argument.** v1.0 supported this theorem with a table of four 'scale gauges' — arithmetic mean, geometric mean, hexagon star, (6,6) edge star — spanning 18.39 %. That table is WITHDRAWN. Renormalizing M₁ is not a length rescaling, because ⋆₁ is scale-free; the table therefore conflated a genuine one-parameter rescaling with an arbitrary change of metric, and its 'gauge orbit' reading was unjustified. The single-parameter statement above is both correct and strictly stronger, since one genuine rescaling already sweeps λ₁ over the whole positive axis. Whether a full transformation (M₁, M₂, A\_e, g) ↦ (M₁′, M₂′, A\_e′, g′) leaving the Hamiltonian invariant exists for the wider family is OPEN and is not needed for anything in this paper.

## **§4. Part I.a, Step Two — The Anchoring Defect Identity**

### **4.1 Setting**

Fix an I\_h-invariant metric (M₁, M₂), let λ be any eigenvalue of Δ₂ with M₂-orthonormal eigenvectors u\_α, and let

a\_alpha \= M1^{-1} B2^T M2 u\_alpha / lambda   ,   so   B2 a\_alpha \= u\_alpha ,  
                                                 \<a\_a, a\_b\>\_{M1} \= delta\_ab / lambda .

Let h span ker B₂ᵀ, the all-ones 2-cochain, which is metric-independent. Lemma S18.A gives the basepoint-free symmetric cup product

**Θ(x, y)(f) \= (δx)(f)·(δy)(f) − Σ\_{t ∈ ∂f} x(t)·y(t) ,**

an expression that is purely combinatorial and carries no metric. Define the orbit-wise compatibility defect and the coexact norm shares

W\_o  \=  ( M2\_{f1} \+ M2\_{f2} )  \-  2 M1\_e        for e in orbit o  (o \= 56, 66\)  
S\_o(lambda)  \=  SUM\_{e in orbit o}  a\_alpha(e)^2      (independent of alpha, by Schur)

### **4.2 Theorem S19.2 (Anchoring Defect Identity)**

**Theorem S19.2.** For every I\_h-invariant diagonal DEC metric and every eigen-channel λ,

**⟨h, Θ(a\_α, a\_β)⟩\_{M₂} − δ\_{αβ}(λ − 2)/λ  \=  − δ\_{αβ} \[ W₅₆ S₅₆(λ) \+ W₆₆ S₆₆(λ) \] .**

*Residual below 10⁻¹² over six random metrics and nine channels; observed values are O(10⁻¹⁴) and BLAS-dependent. \[PROVEN — Check 16\]*

Proof. Expanding the pairing and using δa\_α \= u\_α,

\<h, Theta(a\_a, a\_b)\>\_{M2}  
   \= SUM\_f M2\_f (B2 a\_a)\_f (B2 a\_b)\_f  \-  SUM\_f M2\_f SUM\_{t in df} a\_a(t) a\_b(t)  
   \= \<u\_a, u\_b\>\_{M2}  \-  SUM\_{t in E} a\_a(t) a\_b(t) ( M2\_{f1(t)} \+ M2\_{f2(t)} ) ,

the second line because every edge of a closed 2-complex bounds exactly two faces. Writing M₂,f₁ \+ M₂,f₂ \= 2M₁,t \+ W\_t and using ⟨a\_α, a\_β⟩\_{M₁} \= δ\_{αβ}/λ gives δ\_{αβ}(λ − 2)/λ − Σ\_t a\_α a\_β W\_t. Since W takes only two values, one per edge orbit, and the off-diagonal parts vanish by Schur on the irreducible eigenspace, the sum is δ\_{αβ}(W₅₆ S₅₆ \+ W₆₆ S₆₆).

### **4.3 Corollary S19.2b — retraction of the v1.0 necessity claim**

**Corollary S19.2b.** In a single channel the identity is one scalar condition on three independent metric ratios; its zero locus is a codimension-one surface, not the compatibility line. Explicit counterexample, supplied by external review and reproduced here: (M₁,₅₆, M₁,₆₆, M₂,₅, M₂,₆) \= (1, 2, 1.3231366438740746, 1\) has W₅₆ \= \+0.323137 and W₆₆ \= −2 yet satisfies the λ₁-channel identity to 1.6 × 10⁻¹⁵, because the two defect contributions cancel. The v1.0 statement 'the identity holds if and only if M₁,t \= ½(M₂,f₁ \+ M₂,f₂)' is therefore RETRACTED. Sufficiency survives unchanged and is the W \= 0 sublocus. \[PROVEN — Checks 17, 18\]

The error is diagnosable and worth recording. v1.0's necessity proof argued by Schur that κ \= W₅₆S₅₆ \+ W₆₆S₆₆ \= 0, then asserted that W₆₆ \= 0 'because both faces adjacent to a (6,6) edge are hexagons'. That is not an inference from κ \= 0; it is a restatement of the slice M₁,₆₆ \= M₂,₆ \= 1 on which the numerical scan had been run, and on which W₆₆ vanishes identically by construction. One linear condition was mistaken for two. The numerical evidence — eight roots matching ρ\_E \= (1 \+ ρ\_F)/2 to 10⁻¹⁵ — was real but confined to that slice, and the residual was small for the same reason the claim was wrong.

Quantitatively, the single-channel condition carries almost no information:  
Table 4.1. λ₁ along the single-channel anchoring locus, d \= 1, with a solved for from each (b, c). The condition constrains λ₁ by a factor of 1.55.

| M₁,₆₆ | M₂,₅ | M₁,₅₆ (root) | λ₁ | shift |
| ----- | ----- | ----- | ----- | ----- |
| 0.500 | 0.700 | 2.68100417 | 0.8047193278 | −35.252 % |
| 0.750 | 1.000 | 1.46222868 | 1.1328193683 | −8.852 % |
| 1.000 | 1.000 | 1.00000000 | 1.2428416164 | 0.000 % |
| 1.000 | 1.500 | 1.25000000 | 1.2496888754 | \+0.551 % |
| 1.500 | 1.500 | 1.08214572 | 1.1739414520 | −5.544 % |
| 3.000 | 1.500 | 1.07920227 | 0.9881199194 | −20.495 % |

### **4.4 Theorem S19.2′ — universality restores necessity**

The proof of the identity never uses λ₁. Lemma S18.A is combinatorial, and 'every edge bounds exactly two faces' is a property of the complex. The natural reading of the anchoring identity is therefore channel-universal, and that reading is exactly what recovers the selection.

**Axiom (H-UA), Universal Harmonic Anchoring.** The identity ⟨h, Θ(a\_α, a\_β)⟩ \= δ\_{αβ}(λ − 2)/λ holds in every eigen-channel of Δ₂, not merely in the λ₁ channel. \[HYPOTHESIS-strong; motivated by the channel-agnostic proof, but not a theorem of ZS-S14 — registered as F-S19.7\]

**Theorem S19.2′.** Under (H-UA), and for any metric at which two channels have linearly independent rows (S₅₆, S₆₆), the anchoring identity holds if and only if W₅₆ \= W₆₆ \= 0, that is if and only if pointwise star compatibility M₁,t \= ½(M₂,f₁ \+ M₂,f₂) holds. Verified: the 9 × 2 channel matrix S has rank two on every metric sampled, minimum second singular value 0.0532; at the counterexample point the (λ₁, λ\_h) determinant is −0.009825 and every channel other than λ₁ is violated by at least 9.3 × 10⁻³; and over random metrics 'universal anchoring' and 'both defects vanish' coincide exactly. \[PROVEN — Checks 19–21\]

**Corollary S19.2a.** Under compatibility, M₂ → sM₂ forces M₁ → sM₁ and Δ₂ is exactly invariant, so the normalization ambiguity of Theorem S19.1 is eliminated rather than chosen. Verified at s ∈ {0.25, 1, 4, 17.3}. \[PROVEN — Check 22\]

### **4.5 The Euclidean DEC metric is excluded for every edge length**

With ⋆₁ fixed at the unambiguous circumcentric ratios and ⋆₂ \= 1/(a\_TI² A\_f), the λ₁-channel condition has a unique root at

**a\_TI\* \= 0.5429961198 ,   λ₁ \= 1.2211091536   (−1.749 %) ,**

but at that point the λ\_h channel is violated at −4.4 × 10⁻³. Under (H-UA) the circumcentric Euclidean metric is therefore excluded outright, for every choice of edge length. This is the sharpest available disposal of the ZS-S18 alarm: it does not depend on a normalization convention and does not require the alarm's arithmetic to be wrong — which it is not. \[PROVEN — Checks 23, 24\]

### **4.6 The residual one-parameter family**

Compatibility relates the two sectors and leaves the face ratio ρ\_F \= w₅/w₆ free, with ρ\_E \= (1 \+ ρ\_F)/2 and the scale determined:  
Table 4.2. λ₁ on the compatibility line. The gap remains threefold at all sampled points of the audited domain ρ\_F ∈ \[10⁻⁴, 10⁶\], so the T₁ identification underpinning ZS-S17 and ZS-S18 Part I is safe throughout that range; no no-crossing theorem is claimed (NC-S19.20).

| ρ\_F | ρ\_E | λ₁ | shift | mult. | Λ\_QCD / MeV |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 0.800000 | 0.900000 | 1.2073064127 | −2.859 % | 3 | 271.9 |
| 0.900000 | 0.950000 | 1.2290183428 | −1.112 % | 3 | 267.1 |
| 1.000000 | 1.000000 | 1.2428416164 | 0.000 % | 3 | 264.1 |
| 1.100000 | 1.050000 | 1.2508516793 | \+0.644 % | 3 | 262.4 |
| 1.200000 | 1.100000 | 1.2545633521 | \+0.943 % | 3 | 261.6 |
| 1.250000 | 1.125000 | 1.2551678546 | \+0.992 % (max) | 3 | 261.5 |
| 1.510087 \= A₆/A₅ | 1.255044 | 1.2492510166 | \+0.516 % | 3 | 262.8 |
| 2.000000 | 1.500000 | 1.2185135590 | −1.957 % | 3 | 269.4 |

Over ρ\_F ∈ \[1, A₆/A₅\] the residual freedom moves λ₁ by at most 0.992 % and confines Λ\_QCD to 261.5–264.1 MeV, inside the quenched lattice bar 260 ± 20 MeV. This is recorded as CONDITIONAL-BOUNDED: it is what can be asserted about Λ\_QCD without closing F-S19.6, and it is an OBSERVATION about the flatness of λ₁, not evidence for ρ\_F \= 1\. \[COMPUTED — Checks 25–27\]

### **4.7 The last ratio: withdrawal of the Haar argument**

**Withdrawal of Theorem S19.3 (Haar democracy).** v1.0 argued that the product Haar measure on SU(N)^E treats every link identically and therefore forces M₁ ∝ I. That argument is WITHDRAWN. The Haar measure fixes the invariant integration measure on each factor, and hence the form of the electric term as a sum of link Casimirs; it does not fix the coefficients. A bi-invariant Riemannian metric on a product group carries an independent positive scale on each factor, and since the TI edges form two I\_h orbits, symmetry alone permits

**H\_E \= (g²/2) \[ κ₅₆ Σ\_{e ∈ E₅₆} E\_e·E\_e \+ κ₆₆ Σ\_{e ∈ E₆₆} E\_e·E\_e \] ,   κ₅₆ ≠ κ₆₆ allowed.**

The same objection applies to the magnetic leg: on an irregular complex a single gauge coupling is compatible with face-dependent plaquette weights β\_f induced by cell geometry, and such weights are fixed coefficients, not fitted parameters. v1.0's appeal to the zero-free-parameter axiom conflated 'derived from geometry' with 'freely chosen'.

### **4.8 The Legendre dictionary, and a retraction against v1.2**

What survives the withdrawal is a cross-sector relation, but v1.2 stated it in the wrong variables. The correction matters for the physical reading and is issued here. Starting from the Lagrangian of the cellular gauge quantum mechanics,

L   \= (1/2g^2) Omega^T M1 Omega  \-  (2/g^2) SUM\_f beta\_f \[ N \- Re Tr U\_f \] ,  
Pi  \= dL/dOmega \= (1/g^2) M1 Omega ,  
H\_E \= (g^2/2) Pi^T M1^{-1} Pi   ,   H\_B \= (2/g^2) SUM\_f beta\_f \[ N \- Re Tr U\_f \] ,

equation of motion:   qddot \+ M1^{-1} B2^T M2 B2 q \= 0   (Delta\_2 unchanged).

The Hamiltonian electric coefficient is therefore the inverse mass matrix, κ\_e \= (M₁⁻¹)\_e, not M₁ itself. Star compatibility is a statement about M₁ and M₂ \= diag(β\_f), so it takes two different forms in the two pictures:

**(M₁)\_e \= ½ ( β\_{f₁} \+ β\_{f₂} )   \[Lagrangian, arithmetic mean\]  ;   κ\_e \= 2 / ( β\_{f₁} \+ β\_{f₂} )   \[Hamiltonian, harmonic mean\].**

**Corollary S19.7b (retraction against v1.2).** v1.2 §4.7 printed κ\_e \= ½(β\_{f₁} \+ β\_{f₂}) and called it the Hamiltonian relation. That is the Lagrangian relation mislabelled; the Legendre inverse was omitted. RETRACTED. At the counting point β₅ \= β₆ \= 1 both forms give 1, so no ledger number is affected; off that point the two differ and the physical reading of the residual family changes. The generalized eigenproblem, and hence Δ₂ and every spectral number in this paper, is unaffected, because the equation of motion carries M₁⁻¹B₂ᵀM₂B₂ either way. \[PROVEN — Checks 39–42\]

So the electric weights are not independent data: of the four weights, (H-UA) removes two and the overall scale removes one, leaving exactly one ratio β₅/β₆. §4.9 and §4.10 address that ratio without any appeal to the Haar measure.

### **4.9 Theorem S19.6 — the Regge-moduli exclusion**

The reviewer's second priority was to compute the intersection of the anchoring submanifold with the locus of metric-induced Hodge stars. v1.2 answered it by checking two realizations and asserting, from vertex-transitivity, that they were the only ones. That inference was too quick: the TI has two edge orbits, so an I\_h-invariant piecewise-flat metric need not have equal edge lengths. The correct statement requires classifying the moduli, and the classification is short.

**Proposition S19.6a (moduli).** An I\_h-invariant piecewise-flat (Regge) metric on the TI assigns one length to each edge orbit, ℓ₅₆ and ℓ₆₆. Pentagons are then regular with side ℓ₅₆; hexagons have sides alternating ℓ₅₆, ℓ₆₆. Requiring each face to be cyclic, so that a circumcentric dual exists at all, fixes the face shapes uniquely. The moduli space is therefore two-dimensional: a scale s and a shape t \= ℓ₆₆/ℓ₅₆ \> 0\. \[PROVEN\]

**Theorem S19.6.** Star compatibility imposes one condition per edge orbit, hence two conditions on the two moduli. Written as demands on the common scale they read s² \= (1/A₆)/r₆₆ and s² \= ½(1/A₅ \+ 1/A₆)/r₅₆, so the scale cancels from their ratio and one scalar equation Q(t) \= 1 remains. Q(t) \> 1 for every t ∈ (0, ∞). Hence no I\_h-invariant Regge metric on the truncated icosahedron carries star-compatible circumcentric Hodge stars, and the intersection of the compatibility submanifold with the metric-induced locus is EMPTY. \[PROVEN — Checks 30–38\]

Proof. Let x be the half-angle subtended at the hexagon circumcentre by a pentagon–hexagon edge, u \= cot x, and c \= cot(π/5). Elementary trigonometry on the cyclic faces gives the closed forms

t   \= ( sqrt3 u \- 1 ) / 2 ,          r\_56 \= ( c \+ u ) / 2 ,  
r\_66 \= ( u \+ sqrt3 ) / ( sqrt3 u \- 1 ) ,  
A\_6 \= (3/16)( sqrt3 u^2 \+ 6u \- sqrt3 ) ,   A\_5 \= 5c/4 ,   domain  u \> 1/sqrt3 ,

whence Q \= \[r₆₆/(2r₅₆)\](A₆/A₅ \+ 1\) is a rational function of u and

**Q − 1  \=  P(u) / \[ 20c ( √3 u − 1 )( u \+ c ) \] ,**

P(u) \= 3 sqrt3 u^3 \+ (27 \- 20 sqrt3 c) u^2  
       \+ (15 sqrt3 \+ 40 c \- 20 sqrt3 c^2) u \+ (20 c^2 \+ 20 sqrt3 c \- 9\) .

The denominator is strictly positive on u \> 1/√3. For the numerator, note first the exact algebraic forms c² \= (5 \+ 2√5)/5, a₀ \= 11 \+ 8√5 \+ 20√3c and a₁ \= −5√3 \+ 40c − 8√15, from which a₀ \> 0 and a₁ \> 0 without any floating-point appeal. Now P′(u) \= 3a₃u² \+ 2a₂u \+ a₁ has two positive roots, u₋ \= 0.4484088862 and u₊ \= 2.2047424786, so P rises on \[0, u₋\], falls on \[u₋, u₊\] and rises on \[u₊, ∞). Hence

**min\_{u ≥ 0} P  \=  min( P(0), P(u₊) )  \=  min( 76.5678121575, 65.7130202935 )  \=  65.7130202935  \>  0 ,**

so P(u) \> 0 for every u ≥ 0, in particular on the physical domain, and therefore Q(t) \> 1 for every t \> 0\.

Certification. The bound above is verified by outward-rounded interval arithmetic: enclosing u₊ in the rational interval \[2.20, 2.21\] and evaluating P there gives P(\[2.20, 2.21\]) ⊆ \[64.8013718922, 66.6253551746\], whose lower endpoint is strictly positive. Two independent corroborations are recorded: the discriminant of P is −3822266.5485 \< 0 with unique real root −1.4019488874 \< 0, which gives the same conclusion by root location; and for u ≥ 4 one has a₃u \+ a₂ \= 0.1053413533 \> 0, so P \= u²(a₃u \+ a₂) \+ a₁u \+ a₀ is positive termwise. \[PROVEN, interval-certified end to end — Checks 30–42\]

**Remark (correction to v1.3).** v1.3 asserted this theorem from a 4000-point scan and quoted 'infimum 1.1463967982 at t ≈ 2.415994'. A scan cannot exclude a narrow dip between sample points, and the quoted numbers were grid values, not the infimum. Both defects are repaired here: the positivity is now proved by root location, and the true minimum, obtained from stationarity, is Q \= 1.1463953345 at t \= 2.4107050485. \[PROVEN\]  
Table 4.4. The compatibility defect Q(t) over the Regge moduli, and at the three named realizations. Compatibility requires Q \= 1; the defect never falls below 14.64 %. r\_o is the scale-free edge star |⋆e|/|e| on orbit o.

| Point of the moduli | t \= ℓ₆₆/ℓ₅₆ | Q | defect | verdict |
| ----- | ----- | ----- | ----- | ----- |
| intrinsic flat, equal edges | 1.000000 | 1.3986482220 | \+39.86 % | excluded |
| flat Euclidean embedding (chordal dual) | 1.000000 | 1.3782723424 | \+37.83 % | excluded |
| geodesic unit sphere | 1.000000 | 1.4146772905 | \+41.47 % | excluded |
| true minimum of the defect over the moduli | 2.4107050485 | 1.1463953345 | \+14.6395 % | excluded |
| every other t \> 0 | (0, ∞) | \> 1 by P(u) \> 0 | ≥ \+14.6395 % | excluded |

The intrinsic and embedded flat rows differ because the intrinsic dual length is the sum of the two face apothems, measured in the unfolded piecewise-flat surface, whereas the embedded one is the chord between circumcenters in R³. The intrinsic value is the correct DEC quantity for a piecewise-flat surface; both are reported, and both are excluded. \[PROVEN\]

**Scope, stated explicitly.** Theorem S19.6 excludes diagonal circumcentric Hodge stars on I\_h-invariant Regge metrics with cyclic faces. It does NOT exclude non-circumcentric orthogonal duals, nor non-diagonal Whitney–Galerkin mass matrices, nor abstract cellular inner products not arising from any piecewise-flat metric. Those are registered as NC-S19.16 and as Route W of the pre-registration in §4.11.

### **4.10 Theorem S19.7 — the counting trace selects the star, and (R) does not**

Theorem S19.6 says the Z-Spin inner product on the TI cannot be a diagonal circumcentric star of any I\_h-invariant cyclic Regge metric. The corpus says something adjacent, for an independent reason, and has said so since ZS-S7 §1: the polyhedral lattice is not an approximation to be refined toward a continuum limit but is itself the UV regulator. Call that (R). v1.2 of this paper claimed the counting star followed from (R). It does not, and the claim is retracted.

**Corollary S19.7a (retraction against v1.2).** (R) denies an ambient metric; it does not assign measures. A weight w\_f \= ψ(n\_f) is metric-free too, since n\_f is read off the boundary operator, and because n\_f takes only the values 5 and 6 the function ψ realizes ANY positive ratio ρ\_F \= ψ(5)/ψ(6). The residual under (R) alone is therefore a continuous one-parameter family, not a finite list. v1.2's phrases 'the residual ambiguity is finite, enumerated' and 'three continuous ratios → five discrete candidates' are RETRACTED. \[PROVEN\]

What is needed is an explicit integration prescription, and it must be stated as an axiom rather than smuggled in as a reading of (R).

**Axiom (R\_C), cellular counting trace.** The regulator integral on the cell complex is the cellular counting trace: ∫\_K f := Σ\_{σ ∈ K} f(σ). Equivalently, every oriented k-cell carries unit measure, irrespective of its type or boundary degree, and so does every dual cell. \[HYPOTHESIS-strong; NEW in this paper; strictly stronger than (R) — registered as F-S19.6\]

**Theorem S19.7.** Under (R\_C), ⋆\_k \= |⋆σ| / |σ| \= 1 for every k, that is M₁ \= M₂ \= I. This star satisfies star compatibility identically, ½(1 \+ 1\) \= 1, hence satisfies (H-UA) in every channel; and it gives Δ₂ \= B₂B₂ᵀ exactly, λ₁ \= 1.2428416164. Note the dependency: this step uses (R\_C) ALONE. (H-UA) plays no part in it, and v1.4 wrongly bundled the two. \[DERIVED-CONDITIONAL on (R\_C) — Checks 43–45\]

Two remarks. First, (R\_C) and Theorem S19.6 are logically independent and must be tagged separately. (R\_C) alone selects the counting star and fixes λ₁. Theorem S19.6 is PROVEN geometry, needing no axiom at all; what (H-UA) supplies is the reason star compatibility is the relevant criterion, and hence the reason the theorem excludes anything. The two point the same way, and that agreement is the strongest structural result of the paper — but it is joint corroboration, not a shared dependency, and not proof. Second, the honest accounting of new assumptions is two, and they are load-bearing for different things: tagging every result with their conjunction, as v1.4 did, understates what each achieves. v1.2's claim that only existing corpus axioms were used is withdrawn.  
Table 4.5. Audit of natural non-counting weights w\_f \= ψ(n\_f), each carried through star compatibility. This is an audit of representative choices, NOT a classification: under (R) alone ρ\_F ranges over all of (0, ∞). The gap remains 3-fold throughout, and Λ\_QCD remains inside the quenched lattice bar even where the internal anti-numerology band is exceeded.

| ψ | ρ\_F | λ₁ | shift | inside 2.4722 % band | Λ\_QCD / MeV |
| ----- | ----- | ----- | ----- | ----- | ----- |
| ψ \= 1 (counting measure) | 1.000000 | 1.2428416164 | 0.000 % | yes | 264.1 |
| ψ \= 1/n\_f | 1.200000 | 1.2545633521 | \+0.943 % | yes | 261.7 |
| ψ \= 1/(n\_f − 2\) | 1.333333 | 1.2547087463 | \+0.955 % | yes | 261.6 |
| ψ \= n\_f | 0.833333 | 1.2155777721 | −2.194 % | yes | 270.1 |
| ψ \= n\_f − 2 | 0.750000 | 1.1926356414 | −4.040 % | NO | 275.3 |
| circumcentric metric star (any Regge metric) | — | — | — | excluded by Thm S19.6 | — |

### **4.11 Pre-registration of the three reduction routes**

So that F-S19.6 cannot be settled after the fact, the three candidate cellular reductions of the ZS-S14 action are pre-registered here with their consequences.  
Table 4.6. Pre-registered routes for the cellular reduction, and what each would do to this paper.

| Route | Inner product | M₁, M₂ | Consequence for ZS-S19 |
| ----- | ----- | ----- | ----- |
| C — counting regulator | ⟨α,β⟩ \= Σ\_σ α(σ)β(σ) | I₉₀ , I₃₂ | confirms (R\_C) at action level; ρ \= (1,1) promoted toward DERIVED |
| W — Whitney / Galerkin | ∫ W\_σ ∧ ⋆W\_{σ′} | generally NON-diagonal | the entire diagonal-star analysis of §§3–4 would have to be rewritten in terms of the full matrices |
| D — mass-lumped circumcentric DEC | |⋆σ| / |σ| | diagonal, metric-induced | excluded by Theorem S19.6 for every Regge metric; if the action selected it, (H-UA) would have to be abandoned |

### **4.12 Execution of F-S18.16: reduced and conditionally selected, not closed**

Table 4.3. Status of the pre-registered trichotomy of F-S18.16 after v1.6.

| Pre-registered outcome | Verdict | Consequence |
| ----- | ----- | ----- |
| 1\. ρ \= (1,1) forced | NOT established. v1.0 claimed it; the claim rested on the withdrawn Haar leg and on a necessity argument now retracted. | F-S18.16 remains OPEN |
| 2\. a specific ρ ≠ (1,1) forced | did not occur; the circumcentric Regge candidate is excluded by Theorem S19.6 under (H-UA) | the hard fork of the handover §4.0 does NOT fire |
| 3\. ρ not determined by the action | still live. Under (R) alone the residual is a continuous one-parameter family; only (R\_C) removes it, and (R\_C) is not derived from ZS-S14. | F-S19.6 remains a decision gate with four pre-registered outcomes |
| (new) 4\. reduced to one ratio plus two named axioms | OCCURRED | three ratios → one; every circumcentric metric star excluded over the full Regge moduli; the audited candidates give Λ\_QCD ∈ 261.6–275.3 MeV, inside the quenched bar |

The honest summary. ZS-S19 v1.6 converts F-S18.16 from an open convention with an unbounded consequence into one named ratio conditioned on two named axioms, with the entire circumcentric metric family excluded and the residual audited. Both conditioning axioms are new: (R\_C) for the selection and (H-UA) for the exclusion. What v1.0 claimed by an invalid Haar argument, and v1.2 by an over-read of the corpus regulator axiom, is here obtained from an explicitly stated integration prescription, and independently corroborated by a moduli-wide geometric exclusion. That is a selection, not a closure. F-S18.16 remains open at action level, and F-S19.6 is a decision gate: three of its four pre-registered outcomes would force revision of this paper.

## **§5. Part I.b — The Wilson Quartic and a Correction to ZS-S18 §7**

ZS-S18 v1.6 extracted the Wilson quartic by a Cauchy contour, stable to 1.6 × 10⁻¹³, and correctly labelled the result a machine-precision extraction rather than a closed form, leaving Proposition S18.6B and Corollary S18.6C at COMPUTED. The Magnus route closes the structure.

**Lemma S19.4 (Magnus quartic).** Let U\_f \= exp(iY) with Y Hermitian traceless and Y \= gY₁ \+ g²Y₂ \+ g³Y₃ \+ O(g⁴). Then

N \- Re Tr U\_f \= (g^2/2) Tr Y1^2  \+  g^3 Tr(Y1 Y2)  
              \+ g^4 \[ (1/2) Tr Y2^2 \+ Tr(Y1 Y3) \- (1/24) Tr Y1^4 \] \+ O(g^5) ,

so with  V(g) \= (2/g^2) SUM\_f \[ N \- Re Tr U\_f \]  the quartic coefficient is

   V2 \= SUM\_f \[ Tr Y2^2 \+ 2 Tr(Y1 Y3) \- (1/12) Tr Y1^4 \] .

Proof. Re Tr exp(iY) \= Tr(I − Y²/2 \+ Y⁴/24 − …), the odd powers contributing nothing to the real part because Tr Y^{2k+1} is real and multiplied by an odd power of i. Substituting the expansion of Y and collecting g⁴: from the Y² term, −½(Tr Y₂² \+ 2 Tr Y₁Y₃); from the Y⁴ term, \+(1/24) Tr Y₁⁴. The Y³ term contributes to the imaginary part only. Subtracting from N and multiplying by 2/g² gives the stated V2. \[PROVEN\]

**Corollary S19.4a (retraction of a predecessor formula).** The ZS-S18 §7 hand-off sentence transmits the quartic as Tr(Ω₂² \+ 2Ω₁Ω₃ \+ Ω₁⁴/12). The sign of the last term is wrong; it is −Ω₁⁴/12. ZS-S18 §4.1 body text carried the correct sign, so the defect is confined to the hand-off. It is RETRACTED here before propagating into any Part I.b computation.

Independent numerical confirmation. For random Hermitian traceless Y₁, Y₂, Y₃ the quartic coefficient is extracted from N − Re Tr exp(iY) by three-point Richardson extrapolation, which removes the O(g) and O(g²) contamination without using the formula under test. Residuals are normalized by the scale of the individual traces.  
Table 5.1. Discrimination between the two candidate signs. The − 1/12 form matches the independent extraction to better than 2 × 10⁻⁶; the \+ 1/12 form is off by 0.09 to 1.1, a separation exceeding five orders of magnitude.

| Group | extracted V2 | − 1/12 form | residual | \+ 1/12 form | residual |
| ----- | ----- | ----- | ----- | ----- | ----- |
| SU(2) | \+1.2349470901 | \+1.2349473454 | 1.9 × 10⁻⁷ | \+1.3769218489 | 1.0 × 10⁻¹ |
| SU(3) | \+0.3403411862 | \+0.3403627084 | 1.7 × 10⁻⁶ | \+12.6759885165 | 9.5 × 10⁻¹ |
| SU(4) | −18.5845172464 | −18.5844952056 | 6.0 × 10⁻⁷ | \+22.4975580842 | 1.1 |

In the TI application Y₁ \= δA, the oriented edge sum around the face, and Y₂ \= (i/2)Σ\_{j\<k}\[A\_j, A\_k\], the cup-product curvature with the ZS-S18 value μ \= −1/2 already verified; Y₃ is the third-order Baker–Campbell–Hausdorff term for an ordered product of n\_f exponentials. By I\_h equivariance and Schur, the quartic on the symmetric two-gluon sector is H₄ \= s\_A(N)P\_A \+ s\_H(N)P\_H, so only two numbers are required and the full quartic tensor must not be built. Evaluating s\_A(N) and s\_H(N) in closed form is left OPEN as F-S19.4, and is registered as such by the companion code (v1.0 described it as OPEN in the text but omitted it from the gate register); what Lemma S19.4 supplies is the correct combination to evaluate. Proposition S18.6B and Corollary S18.6C therefore remain at COMPUTED and COMPUTED-EXTRAP respectively, and are not promoted here.

## **§6. Part II — The Non-Abelian Gauss Law as a Finite-Matrix Problem**

ZS-S18's gauge fixing dim Ω¹ \= 90 \= 59 ⊕ 31 is the linearized Hodge decomposition. On the TI the full problem is finite-dimensional, which is why it belongs in a polyhedral paper rather than a continuum one. The objects are

D\[A\] \= B1 \+ g ad(A) ,          M\[A\] \= D\[A\]^dagger D\[A\] ,  
log det M\[A\] \= log det M0 \- (g^2/2) Tr( M0^{-1} M1 M0^{-1} M1 ) \+ ... ,  
H\_Coul \= (g^2/2) rho^a K^{ab}\[A\] rho^b ,     K \= M^{-1} (-Delta\_0) M^{-1} .

This paper reports the exact zeroth-order content and registers the O(g²) content as OPEN.  
Table 6.1. Exact zeroth-order Faddeev–Popov data on the truncated icosahedron. All values computed by the companion code.

| Quantity | Value | Status |
| ----- | ----- | ----- |
| gauge census dim Ω¹ \= 59 (gradients) \+ 31 (physical) | rank B₁ᵀ \= 59, rank B₂ᵀ \= 31 | CERTIFIED |
| M₀ \= Δ₀ \= B₁B₁ᵀ, zero modes | 1 (b₀ \= 1\) | PROVEN |
| λ\_min(Δ₀) — spectral gap of the g \= 0 FP operator | 0.2434017461399 | COMPUTED |
| σ\_min(B₁) \= √λ\_min — the associated norm scale | 0.4933576249942 | COMPUTED |
| a certified Gribov radius | not established | OPEN (F-S19.8) |
| λ\_max(Δ₀) | 4 \+ φ \= 5.6180339887499 | COMPUTED |
| log det′ Δ₀ | 51.46858026968669 | COMPUTED |
| det′ Δ₀ / V \= spanning trees τ(TI) | 375291866372898816000 | PROVEN (Kirchhoff, exact integer match) |
| Δμ\_A^FP, Δμ\_H^FP, Δμ\_A^Coul, Δμ\_H^Coul | not computed | OPEN (F-S19.1) |

Two remarks. First, the Kirchhoff identity det′Δ₀ \= V·τ with τ \= 375291866372898816000 is an exact integer check on the Faddeev–Popov determinant at g \= 0, matching the known spanning-tree count of the buckyball graph to full double precision; it is the cleanest available regression test on the whole Part II setup. Second, and correcting v1.0: 0.2434017461 is the spectral gap of Δ₀ and is NOT a certified Gribov radius. The standard Faddeev–Popov operator is the Hessian of a gauge-fixing functional, of the form −∂·D\[A\], and is not in general D\[A\]†D\[A\]; and a rank-stability bound on D₀ \+ δD is governed by the smallest nonzero singular value σ\_min \= 0.4933576250, not by the eigenvalue. Both numbers are reported; neither is claimed as a horizon, and the lattice gauge-fixing functional is not specified here. This is registered as F-S19.8. The fundamental modular region is not a technicality here: ZS-S17's polynomial reduction carried a spurious vacuum with face holonomies |tr W|/3 \= 0.40–0.49, not pure gauge, and any Part II result that ignores the fundamental modular region will reproduce that failure. The flux-tube construction of Pavel, with its Faddeev–Popov determinant and six Gribov horizons separating six Weyl chambers, remains the template.

## **§7. Part III — The Two-Gluon Block Census**

Theorem S18.9 already closed the one-gluon exchange space: the fully polarised cubic vertex couples two external T₁(λ₁) legs into T₁(λ₁) ⊕ T₁(λ\_h) and nowhere else among the 31 physical modes. What remains for Part III is the staged diagonalization of H \= H\_E \+ H\_B. This paper certifies the kinematic prerequisites and does not run the Lanczos.

The signed I\_h action is constructed explicitly as 120 signed permutation matrices on the 90 edges, with the induced action on faces fixed by P\_F B₂ \= B₂ P\_E. Both equivariance and \[P\_F, L₂\] \= 0 hold with residual exactly zero, and the ten conjugacy classes have the correct sizes (1, 12, 12, 20, 15 | 1, 12, 12, 20, 15).  
Table 7.1. Isotype census. Labels are for the signed (orientation-twisted) action; under the parity dictionary of ZS-S18 Theorem S18.8 the Hodge star supplies the det twist, so these labels are the ZS-S18 labels tensored with A\_u. The twist squares to the identity, so the Sym² labels agree with ZS-S18 exactly.

| Space | Dimension | Isotype decomposition | Status |
| ----- | ----- | ----- | ----- |
| faces Ω² (signed) | 32 | 2A\_u ⊕ 2T₁g ⊕ 2T₂g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u | CERTIFIED |
| edges Ω¹ | 90 | A\_u ⊕ 3T₁g ⊕ 2T₁u ⊕ 3T₂g ⊕ 2T₂u ⊕ 3G\_g ⊕ 3G\_u ⊕ 3H\_g ⊕ 4H\_u | CERTIFIED |
| physical (coexact) modes | 31 | A\_u ⊕ 2T₁g ⊕ 2T₂g ⊕ G\_g ⊕ G\_u ⊕ 2H\_u | CERTIFIED |
| Sym² of the 31 physical modes | 496 | A\_g 12 ⊕ H\_g 140 (28 copies) ⊕ T₁u 45 ⊕ T₂u 45 ⊕ G\_g 68 ⊕ G\_u 64 ⊕ H\_u 85 ⊕ T₁g 18 ⊕ T₂g 18 ⊕ A\_u 1 | CERTIFIED |

The two blocks that carry the glueball physics are therefore the 12-dimensional scalar A\_g block and the 140-dimensional tensor H\_g block, exactly as the ZS-S18 handover recorded, and the parity dictionary assigns A → 0⁺⁺ and H → 2⁺⁺ with C \= \+ unconditionally. \[CERTIFIED — Checks 40–47\]

**Corollary S19.5 (independent confirmation of a ZS-S7 correction).** ZS-S7 §2.2 asserts that the 32-dimensional face representation contains all ten I\_h irreducibles exactly once. ZS-S18 corrected this. The correction is confirmed here independently by character projection: the face representation carries six distinct irreducibles, four of them with multiplicity two. The statement is non-load-bearing for ZS-S7's Λ\_QCD and glueball results, which depend only on λ₁, its multiplicity and the topological cancellation.

The convergence criterion for the eventual Lanczos is pre-registered here, unchanged from the handover: |R(n\_max \+ 2\) − R(n\_max)| / R(n\_max) \< 1 %, with convergence never read from two points. ZS-S17 lost a cycle to a Richardson extrapolation that looked convergent at n\_max \= 3, 4 and was exposed as an artifact only at n\_max \= 7\.

## **§8. Part IV — Scale Matching: Status**

No part of Part IV is executed here. The position is recorded so that the OPEN gate is precise. With ε₀(λ\_t) the dimensionless scalar eigenenergy from Part III, the zero-parameter fixed point is

lambda\_t  \=  12 pi alpha\_s^{S14} ( m\_{0++}^{ZS} / eps\_0(lambda\_t) ) ,

the argument being a ratio, not a product. The lattice requires λ\_t \= 5.5387 ± 0.11 given Corollary S18.6C, against λ\_t(M\_Z) \= 4.4590 from ZS-S1, implying α\_s \= 0.1475 and a one-loop μ\_TI ≈ 30 GeV. Three items are unresolved: the scheme relation g\_{S14} \= Z\_g(a\_TI, μ) g\_MS-bar(μ) is not derived; a\_TI must be fixed from an independent observable, the string tension or Λ\_QCD, never the 2⁺⁺/0⁺⁺ ratio; and λ\_t ≈ 5.5 is not small, so no perturbative statement in Parts I or II is inside its domain of control. \[OPEN — F-S19.3\]

## **§9. Cross-Paper Dependency and Version-Conflict Audit**

The requirement is not internal algebraic consistency alone but a traced dependency audit: a change in an upstream object must be followed through every paper that consumes it. ZS-S19 changes the epistemic status of λ₁ (assumed convention → DERIVED-CONDITIONAL on (R\_C)) and changes no numerical value anywhere. The chain from ZS-M1 downward is therefore untouched: the i-tetration fixed point z\* \= 0.4382829367 \+ 0.3605924719 i, its multiplier and μ, δ of ZS-Q18 enter Parts I–IV nowhere, so no version-conflict can arise on that branch.  
Table 9.1. Downstream dependency trace. Every consumer of λ₁ is listed with the effect of ZS-S19.

| Consumer | Object consumed | Effect of ZS-S19 | Value after |
| ----- | ----- | ----- | ----- |
| ZS-S7 §5 | Λ\_QCD \= vA/(λ₁ V\_Y) | value unchanged; status becomes DERIVED-CONDITIONAL on (R\_C) | 264.1 MeV, unchanged |
| ZS-S7 §6 | m(0⁺⁺) \= vA/Q | none — λ₁ cancels topologically | 1.7906 GeV, unchanged |
| ZS-S7 §2.2 | face isotype claim | corrected (Cor. S19.5); non-load-bearing | six irreps, four doubled |
| ZS-S14 §2.10 | inherits ZS-S7 outputs | none | unchanged |
| ZS-S17 | λ₁, λ\_h, Layer-Lift R \= 1 \+ 3λ₁/4 | none | R \= 1.3900, unchanged |
| ZS-S18 | Ω₀ \= √λ₁, c₁, G\_exch, G\_∞, λ\_t | none numerically; §4.7 corrected, §7 quartic sign retracted, NC-S18.13 reinstated | G\_exch \= 0.313264316799300, unchanged |
| ZS-S1 | α\_s \= 11/93; δ\_Y \= 7/23 | none — counting invariants | unchanged |
| ZS-M6 §5 | Hodge-Dirac dim 182 \= 2 × 91 | none — dimension counts | unchanged |
| ZS-U1, ZS-M1 | no dependence on λ₁ | none | unchanged |

Two upstream statements are amended and one predecessor formula is retracted, all recorded in §13 Version History: NC-S18.13 superseded, ZS-S18 §4.7's one-ratio reduction corrected to two ratios (Proposition S19.0), and ZS-S18 §7's quartic sign retracted. No corpus value is deleted or modified, in keeping with the no-deletion rule.

## **§10. Confrontation with External Data**

The requirement is that no result conflict with established observation. Because ZS-S19 moves no number, the confrontation is a regression check rather than a new prediction, and is reported as such.  
Table 10.1. External confrontation. Lattice values are quenched SU(3); α\_s is PDG 2024\.

| Quantity | Z-Spin | External | Pull | Status |
| ----- | ----- | ----- | ----- | ----- |
| m(0⁺⁺) | vA/Q \= 1.7906 GeV | 1.73 ± 0.05 GeV (quenched lattice) | \+1.21 σ | DERIVED-CONDITIONAL |
| Λ\_QCD | 264.1 MeV at ρ\_F \= 1; 261.6–275.3 MeV over the audited candidates (NOT over the whole compatibility line) | 260 ± 20 MeV (quenched) | \+0.21 σ at the selected point | DERIVED-CONDITIONAL |
| α\_s(M\_Z) | 11/93 \= 0.118280 | 0.1180 ± 0.0009 (PDG) | \+0.31 σ | DERIVED |
| m(2⁺⁺)/m(0⁺⁺) | R \= 1.3900 (Layer-Lift) | 1.4971 (Athenodorou–Teper SU(∞)) | refuted at a \= 0 | F-S18.5 closed-negative, carried |
| 1/N² slope | a\_geom · λ\_t ≈ −0.029 | a\_lat ≈ −3.06 ± 0.95 | ≈ 1 % of observed | EXTERNAL, carried |

The last two rows are inherited negatives from ZS-S18, restated so that this paper cannot be read as claiming more than it does. The pure-geometry Layer-Lift g\_hf(∞) \= λ₁ with vanishing 1/N² slope is refuted by continuum SU(N) data, and ZS-S19 does not repair it; whether the full Hamiltonian does is exactly the content of Parts III and IV. There is no conflict with Planck 2018 ΛCDM, since no cosmological quantity is touched, and none with the Standard Model couplings, since α\_s, sin²θ\_W and α₂ are consumed unchanged from ZS-S1. The Λ\_QCD row is now a band rather than a point, which is the honest reflection of the residual metric freedom.

## **§11. Falsification Gates**

Gates are stratified by the layer at which failure would occur. A failure at Layer 1 is immediate rejection; Layer 2 requires revision of this paper; Layer 3 is decided by external data and does not by itself falsify the geometry.  
Table 11.1. Layer 1 — mathematical / theoretical collapse. Immediate rejection of ZS-S19.

| Gate | Falsifier | Status |
| ----- | ----- | ----- |
| F-S19.A | Some I\_h-invariant metric and channel violate the defect identity dev(λ) \+ W₅₆S₅₆(λ) \+ W₆₆S₆₆(λ) \= 0; Theorem S19.2 is then rejected. NOTE: v1.0’s form of this gate asserted that no incompatible metric can satisfy the anchoring identity. That proposition is FALSE and was refuted by this paper’s own counterexample; it survived as a stale PASS through v1.3 and is removed here. | PASS (residual \< 10⁻¹², 6 metrics × 9 channels) |
| F-S19.A′ | Under (H-UA) the channel matrix S has rank \< 2 on some physical metric, so universal anchoring no longer forces both orbit defects to vanish. | PASS (min second singular value 0.0532) |
| F-S19.B | Δ₂ fails to be invariant under M → sM on the compatibility line, so Corollary S19.2a is false and the scale gauge survives. | PASS (s ∈ {0.25, 1, 4, 17.3}) |
| F-S19.C | The face-Laplacian gap ceases to be 3-fold under the derived weight; the T₁ identification, and with it ZS-S17 and ZS-S18 Part I, collapses. | PASS (threefold at all sampled points, ρ\_F over 13 decades) |
| F-S19.D | Under (R\_C) the counting star does not reproduce M₁ \= M₂ \= I, or fails to give Δ₂ \= B₂B₂ᵀ, so λ₁ ≠ 1.2428416164. | PASS (residual \< 10⁻¹²) |
| F-S19.I | The circumcentric Euclidean metric satisfies universal anchoring at some edge length, so the ZS-S18 alarm would be reinstated. | PASS (dev(λ\_h) \= −4.4 × 10⁻³ at the only λ₁ root) |
| F-S19.E | The O(g⁴) Wilson coefficient is not Tr(Y₂² \+ 2Y₁Y₃ − Y₁⁴/12); Lemma S19.4 and its retraction fail. | PASS (residual \< 2 × 10⁻⁶ at N \= 2, 3, 4\) |

Table 11.2. Layer 2 — simulation / internal-consistency collapse. Revision required, corpus not rejected.

| Gate | Falsifier | Status |
| ----- | ----- | ----- |
| F-S19.1 | The four O(g²) Faddeev–Popov and Coulomb numbers Δμ\_A^FP, Δμ\_H^FP, Δμ\_A^Coul, Δμ\_H^Coul are computed and (μ\_H − μ\_A)\_total proves gauge-dependent. | OPEN (not counted) |
| F-S19.2 | The staged Lanczos in the A\_g 12 and H\_g 140 blocks moves G\_∞ \= 0.29880491 by more than 10 %, so the perturbative exchange sector was never the answer. | OPEN (not counted) |
| F-S19.4 | s\_A(N) and s\_H(N) admit no exact rational form, so Proposition S18.6B cannot be promoted from COMPUTED to DERIVED. | OPEN (not counted) |
| F-S19.F | det′Δ₀ / V fails to equal the buckyball spanning-tree count, indicating an error in the TI complex or the boundary operators. | PASS (exact integer match) |
| F-S19.G | The Sym² census differs from 496 \= A\_g 12 ⊕ H\_g 140 ⊕ …, invalidating the Part III block structure. | PASS |
| F-S19.6 | Discretizing the ZS-S14 canonical action on the TI and Legendre-transforming yields β₅ ≠ β₆, contradicting the regulator selection of Theorem S19.7. | OPEN (not counted) |
| F-S19.J | Some I\_h-invariant cyclic Regge metric on the TI has star-compatible diagonal circumcentric Hodge stars, reinstating the metric-induced family and with it the ZS-S18 alarm. | PASS (interval-certified: min P \= 65.7130 \> 0; true minimum defect \+14.6395 % at t \= 2.4107050485) |
| F-S19.L | The Legendre transform of the cellular Lagrangian does not return the generalized eigenproblem M₁⁻¹B₂ᵀM₂B₂ a \= λ a, so Δ₂ as used throughout is not the physical operator. | PASS (equation of motion recovers it identically) |
| F-S19.K | The counting star fails star compatibility, or fails to reproduce Δ₂ \= B₂B₂ᵀ. | PASS (both exact) |
| F-S19.7 | (H-UA) is shown to be incompatible with the ZS-S14 reduction, or is shown to be an empty demand because the λ₁ channel is the only one for which Lemma S18.A's consequence is physically meaningful. | OPEN (not counted) |
| F-S19.8 | A properly derived lattice Faddeev–Popov operator has a positivity radius unrelated to either 0.2434017461 or 0.4933576250. | OPEN (not counted) |

Table 11.3. Layer 3 — observational collapse. Decided by external data.

| Gate | Falsifier | Status |
| ----- | ----- | ----- |
| F-S19.3 | Scale matching fails to produce a unique fixed point of λ\_t \= 12πα\_s(m\_{0⁺⁺}/ε₀), so a\_TI is not determined without a lattice input. | OPEN (not counted) |
| F-S19.5 (TESTABLE) | Once F-S19.6 fixes ρ\_F, the resulting POINT prediction for Λ\_QCD is confronted with a future quenched determination; at ρ\_F \= 1 the prediction is 264.1 MeV and a value outside 240–280 MeV would falsify it. NOTE: v1.3's form of this gate claimed that data outside 255–275 MeV would exclude the entire compatibility line. That is FALSE — Λ\_QCD diverges as ρ\_F → 0 and tends to 429.7 MeV as ρ\_F → ∞ — and the claim is RETRACTED here. | PRE-REGISTERED, conditional on F-S19.6 |
| F-S19.H | Athenodorou–Teper per-N extraction, done properly and covariance-aware, shows the multi-channel test cannot be passed by any Hamiltonian of this class. | OPEN, inherited from F-S18.15 |

## **§12. Non-Claims**

NC-S19.1. No Clay Millennium claim is made or implied; the inherited NC-S18.5 stands, and no continuum Wightman statement is asserted anywhere in this paper.  
NC-S19.2. λ\_t is not derived, and λ\_t \= 5.539 is not a prediction; it is what the lattice implies given Corollary S18.6C.  
NC-S19.3. The selection of ρ \= (1,1) is not variational, and it is not unconditional. λ₁ is not stationary at ρ\_F \= 1, and on the compatibility line its maximum lies near ρ\_F ≈ 1.25. No extremal principle is claimed.  
NC-S19.10. F-S18.16 is NOT closed. ρ \= 1 is selected conditionally on (R\_C) alone; (H-UA) is separately load-bearing for the circumcentric-route exclusion. Neither axiom is derived from ZS-S14. NC-S18.13 stands.  
NC-S19.17. This paper does not claim to use only pre-existing corpus axioms. It introduces two: (H-UA) and (R\_C). v1.2's statement that (R) alone sufficed is withdrawn.  
NC-S19.18. The residual weight family under (R) alone is continuous, not finite. The five entries of Table 4.5 are an audit of natural choices and confer no bound on λ₁ or Λ\_QCD in the absence of (R\_C).  
NC-S19.19. No claim is made that κ\_e \= ½(β\_{f₁} \+ β\_{f₂}). That relation, printed in v1.2, is the Lagrangian one; the Hamiltonian relation is the harmonic mean.  
NC-S19.15. Theorem S19.7 is not a theorem about the ZS-S14 action. It derives the star from the NEW counting-trace axiom (R\_C), not from (R). If a future discretization of that action produced geometry-induced β\_f, Theorem S19.6 shows the result could not be star-compatible, and the conflict would have to be resolved against (H-UA) or (R), not by adjusting λ₁.  
NC-S19.16. Theorem S19.6 excludes diagonal circumcentric stars on I\_h-invariant Regge metrics with cyclic faces, and the paper nowhere claims to settle the metric route in any wider sense. Non-circumcentric orthogonal duals, non-diagonal Whitney–Galerkin mass matrices, and abstract cellular inner products not arising from any piecewise-flat metric are neither considered nor excluded.  
NC-S19.11. The Haar measure does not determine the electric-sector coefficients. No claim is made that group-invariance alone forces κ₅₆ \= κ₆₆; v1.0's Theorem S19.3 is withdrawn in full.  
NC-S19.12. (H-UA) is an added structural axiom, not a theorem of ZS-S14, and it is not claimed to follow from Lemma S18.A. What follows from Lemma S18.A is that the identity's proof does not privilege any channel; that is motivation, not proof.  
NC-S19.13. The four normalizations tabulated in v1.0 §3 are not a gauge orbit and that table is withdrawn. Whether a Hamiltonian-preserving transformation relating them exists is OPEN and is not used anywhere.  
NC-S19.14. 0.2434017461 is not a Gribov radius, and neither is 0.4933576250. Both are spectral data of the g \= 0 vertex Laplacian.  
NC-S19.4. Theorem S19.1 does not assert that the truncated icosahedron has no metric; it asserts that the ZS-S14 action supplies none, so that a metric-dependent comparison requires a declared gauge.  
NC-S19.20. The 3-fold multiplicity of the gap is VERIFIED at every sampled point of the compatibility line over ρ\_F ∈ \[10⁻⁴, 10⁶\], thirteen decades. No no-crossing theorem is proved, and the word everywhere is not used of it.  
NC-S19.21. Machine-precision residuals are reported against thresholds, not as fixed values. The defect identity is asserted below 10⁻¹²; the last digits are BLAS-dependent and are not part of the ledger.  
NC-S19.5. The flatness of λ₁ along the compatibility line is an OBSERVATION recorded to bound a counterfactual. It is not evidence for ρ\_F \= 1 and is not used in any derivation.  
NC-S19.6. Part II is set up, not solved. Only the g \= 0 operator and its spectrum are reported; the gauge-fixing functional is not specified, the fundamental modular region is not constructed, and no statement is made about Gribov copies at finite g.  
NC-S19.7. Part III is censused, not diagonalized. No glueball mass, no G\_∞ and no convergence claim is made here.  
NC-S19.8. Lemma S19.4 supplies the correct O(g⁴) combination; it does not supply s\_A(N) or s\_H(N), and it does not promote Proposition S18.6B or Corollary S18.6C.  
NC-S19.9. The SHA256 of the result block certifies the canonically rounded ledger in the recorded environment. It is not a proof of bit-identical reproducibility across BLAS implementations, and no such claim is made.

## **§13. Verification Suite**

Table 13.1. Verification suite summary. 95/95 computed and proof checks PASS. Seven OPEN gates are printed by the companion and are NOT counted.

| Section | Content | Checks | Result |
| ----- | ----- | ----- | ----- |
| §1 | TI complex: cell counts, Euler characteristic, face census, Bianchi identity, edge orbits, areas, circumcentric ratios | 8 | 8/8 PASS |
| §2 | Unweighted spectrum: λ₁, 3-fold degeneracy, λ\_h, 5 ± √3, exact integers 6 and 8 | 5 | 5/5 PASS |
| §3 | Theorem S19.1: scale-freeness of ⋆₁, full DEC at a\_TI \= 1, the implicit a\_TI behind the handover value | 3 | 3/3 PASS |
| §4 | defect identity; anchoring value; the reviewer counterexample and the failure of every other channel there; single-channel span; rank of S; universality ⇔ compatibility; scale elimination; Euclidean DEC exclusion; compatibility line, 3-foldness, Λ\_QCD band; conditional ρ \= (1,1) | 20 | 20/20 PASS |
| §4B | spherical TI closes the sphere; flat and spherical compatibility defects; counting star satisfies compatibility and reproduces B₂B₂ᵀ; the five-candidate audit and its Λ\_QCD band | 10 | 10/10 PASS |
| §4C | closed-form reduction; the exact cubic identity; discriminant and root the exact coefficient forms; the min-of-P certificate and its interval enclosure; the true minimum; Legendre dictionary and the harmonic-mean correction; invariance of Δ₂; continuity of the residual; the compatibility-line retraction; outcome-B sensitivity; metric-freeness of the 59 \+ 31 census | 21 | 21/21 PASS |
| §5 | Lemma S19.4: per-group agreement with the − 1/12 form and refutation of the \+ 1/12 form | 5 | 5/5 PASS |
| §6 | Part II zeroth order: zero mode, Kirchhoff, gauge census, spectral gap, σ\_min, λ\_max | 6 | 6/6 PASS |
| §7 | Part III: group order, signed equivariance, commutation, class sizes, ZS-S7 correction, one-gluon census, Sym² dimension, A\_g 12, H\_g 140 | 9 | 9/9 PASS |
| §8 | Downstream and external: m(0⁺⁺), Λ\_QCD, α\_s, A \= δ\_Xδ\_Y, δ\_Y from cell counts, zero free parameters | 7 | 7/7 PASS |
| §9 | Anti-regression against retracted values, including v1.0's own | 3 | 3/3 PASS |
| Total | — | 95 | 95/95 PASS; 7 OPEN gates not counted |

Verifier conventions, carried from ZS-S18: every check asserts on a recomputed quantity — v1.3 still carried two checks that passed a literal True, and both are replaced here by assertions on the actual orbit counts; the checks are independent assertions but not independent derivations, since the Regge block shares one closed-form map, and no claim of 95 independent evidences is made; OPEN gates are printed and excluded from the pass count; one self-contained file; no files written; no external data assets; the result block is hashed with the environment recorded; and an explicit anti-regression block asserts that retracted values — ZS-S18 v1.2's G \= 1.1025394066, v1.4's G\_exch \= 0.3127381927, the 61.9257 % ledger value, the raw vertex projection 0.0095045494, the −3.868 % shift, and the v1.0 value 1.2492508718 as a headline — are produced by no code path. The declarative check that v1.0 passed as a literal True is gone; the zero-free-parameter assertion is recomputed from (A, Q, v, TI census).

## **§14. Conclusions**

1\. The −3.868 % alarm is not a well-posed comparison. ⋆₁ is scale-free and unambiguous; ⋆₂ carries dimension L⁻² and is defined only once an edge length is declared. At the natural a\_TI \= 1 the full-DEC gap is 0.3600376672 (−71.031 %); the locked value is recovered at a\_TI \= 0.5382277383; the handover's number corresponds to an undeclared a\_TI \= 0.5489498022. The statement is retracted as a ledger item. \[PROVEN\]  
2\. The anchoring condition has an exact closed-form defect: dev(λ) \= −\[W₅₆ S₅₆(λ) \+ W₆₆ S₆₆(λ)\], residual below 10⁻¹² across random metrics and all nine channels. This is the central new mathematics of the paper and it is what makes both the retraction and the repair precise. \[PROVEN\]  
3\. v1.0's necessity claim is false and is retracted. One channel is one scalar condition on three ratios; the reviewer's counterexample (1, 2, 1.3231366438740746, 1\) satisfies it to 1.6 × 10⁻¹⁵ with W₅₆ \= \+0.323 and W₆₆ \= −2, and along the single-channel locus λ₁ spans −35.3 % to \+0.6 %. v1.0's proof mistook a restriction of its own numerical slice for an inference. \[RETRACTED\]  
4\. Necessity is restored in a strictly stronger form. Under (H-UA) — the identity holding in every channel, which is what its channel-agnostic proof suggests — any two independent channels force W₅₆ \= W₆₆ \= 0, since the 9 × 2 channel matrix has rank two (minimum second singular value 0.0532). Compatibility then eliminates the normalization ambiguity outright. \[PROVEN under (H-UA)\]  
5\. The circumcentric Euclidean metric — the specific candidate that raised the alarm — is excluded for every edge length: its only λ₁ root is a\_TI\* \= 0.5429961198, and the λ\_h channel is violated there at −4.4 × 10⁻³. This disposes of the alarm on its own terms, without appeal to a convention. \[PROVEN under (H-UA)\]  
6\. The Haar leg is withdrawn. The product Haar measure fixes the form of the electric term, not its coefficients, and I\_h symmetry permits κ₅₆ ≠ κ₆₆; geometry-induced β\_f are likewise permitted and are not fitted parameters. What compatibility gives is that the electric weights are not independent data — in Hamiltonian variables κ\_e \= 2/(β\_{f₁} \+ β\_{f₂}), the harmonic mean, per conclusion 9\. \[RETRACTED / reduced\]  
7\. No I\_h-invariant Regge metric on the TI carries star-compatible circumcentric Hodge stars. The moduli are two-dimensional — scale s and shape t \= ℓ₆₆/ℓ₅₆ — compatibility gives two conditions, the scale cancels, and the residual equation Q(t) \= 1 has no solution: Q \> 1 everywhere, by an interval-certified bound min\_{u≥0} P \= 65.7130202935 \> 0, with true minimum Q \= 1.1463953345 at t \= 2.4107050485. The three named realizations give 1.3986 (intrinsic flat), 1.3783 (Euclidean embedding) and 1.4147 (geodesic sphere). This supersedes v1.2's two-point argument, whose appeal to vertex-transitivity overlooked the second edge orbit. \[PROVEN\]  
8\. The counting star is selected, but by a new axiom and not by the corpus. ZS-S7 §1's regulator axiom (R) denies an ambient metric; it does not assign measures, and since n\_f ∈ {5, 6} a metric-free weight ψ(n\_f) realizes any positive ρ\_F. v1.2's derivation from (R), and its description of the residual as five discrete candidates, are RETRACTED. What does the work is (R\_C), the cellular counting trace, stated here as an explicit new axiom: under it ⋆\_k \= 1, compatibility holds identically, and Δ₂ \= B₂B₂ᵀ. This step uses (R\_C) ALONE; v1.4's bundling of it with (H-UA) is corrected. \[DERIVED-CONDITIONAL on (R\_C)\]  
9\. A second self-retraction: the Legendre transform. The Hamiltonian electric coefficient is κ\_e \= (M₁⁻¹)\_e, so star compatibility reads κ\_e \= 2/(β\_{f₁} \+ β\_{f₂}) in Hamiltonian variables — the harmonic mean — while v1.2 printed the arithmetic mean, which is the Lagrangian relation. The two agree at the counting point, so no ledger number moves; the equation of motion returns the same Δ₂ either way. But the correction shows that the action-level reduction is not a formality: it fixes the Hamiltonian convention as well as the last ratio. \[PROVEN\]  
10\. Net position on F-S18.16: reduced and conditionally selected, not closed. ρ \= (1,1) and λ₁ \= 1.2428416164 follow from (R\_C) alone; (H-UA) is load-bearing instead for the exclusion of the circumcentric route. The audited alternatives keep the gap 3-fold, move λ₁ within \[−4.040 %, \+0.955 %\], and keep Λ\_QCD within 261.6–275.3 MeV, inside the quenched bar; one exceeds the internal band. The pre-registered hard fork does not fire. F-S19.6 is a decision gate with four pre-registered outcomes, three of which would force revision. \[CONDITIONAL\]  
11\. Independent of the metric line, the Magnus quartic is Tr(Y₂² \+ 2Y₁Y₃ − Y₁⁴/12) and the ZS-S18 §7 sign is retracted; Part II's exact zeroth-order content is established including det′Δ₀ \= 60 · 375291866372898816000; and Part III's block structure is certified at 496 \= A\_g 12 ⊕ H\_g 140\. Seven gates remain OPEN, of which F-S19.6, the action-level derivation of the four Hamiltonian weights, is the single highest-value target, and it must precede rather than follow the non-perturbative Lanczos of the A\_g 12 and H\_g 140 blocks, since outcomes B and C would change the operator the Lanczos is meant to diagonalize. The recommended order is: cellular reduction, Legendre transform, (M₁, M₂, G\_v), then Lanczos with a sensitivity run over ρ\_F.

A methodological note. v1.0 of this paper made exactly the error it had accused its predecessor of making. It found a number that was not invariant under a transformation the problem admits — and then, one section later, asserted an equivalence from a slice of parameter space it had not declared it was working on. The two failures have the same shape: a restriction treated as a generality. The discipline added here, discipline 16, is that an equivalence must be tested on the full parameter space of its own hypothesis, and that the parameter count must be stated before the scan is run, not inferred from it afterwards. It is worth adding that v1.0's residual, 2.4 × 10⁻¹⁵, was genuinely small and genuinely reproducible; small residuals certify arithmetic, not scope. The counterexample that broke the claim came from outside, which is the argument for external review, and it is recorded here in full rather than paraphrased. v1.2 then repeated the pattern once more in a milder form: it replaced an invented axiom with a corpus axiom that did not quite reach, and it called a continuous residual finite. Discipline 17, added here: when a selection is claimed from an axiom, write the axiom out as a formula and check that the formula, and not its paraphrase, does the work.

## **Acknowledgements & Code Availability**

This paper exists because four external review cycles of ZS-S18 established the discipline that made the present retractions findable, and above all because three external review cycles of ZS-S19 itself found, in turn, a false equivalence, a false derivation and a scan presented as a proof. The reviewer's counterexample (M₁,₅₆, M₁,₆₆, M₂,₅, M₂,₆) \= (1, 2, 1.3231366438740746, 1\) is the pivot of §4.3 and is reproduced verbatim in the companion code, as is the reviewer's factorization of the Regge defect, which is what made Theorem S19.6 provable rather than merely sampled.

The verifier zs\_s19\_verify\_v1\_6.py is a single self-contained file requiring numpy, scipy and mpmath, reading no data assets and writing no files. It performs 95 computed and proof checks, prints seven OPEN gates without counting them, emits a machine-readable result block between BEGIN\_ZS\_S19\_RESULTS and END\_ZS\_S19\_RESULTS, and hashes the canonically rounded ledger with the environment recorded. Runtime is approximately thirty-six seconds; the flag \--extended adds N \= 5 and N \= 6 to the Magnus discrimination as non-ledger exploratory values. Corpus repository: https://github.com/KennyKang-git/zspin

## **Appendix A. Construction and Conventions of the TI Complex**

The truncated icosahedron is built from the standard Cartesian coordinate set, namely all even permutations of (0, ±1, ±3φ), (±1, ±(2 \+ φ), ±2φ) and (±φ, ±2, ±φ³), rescaled so that the edge length is one. Edges are vertex pairs at unit distance; faces are the planar cycles of the convex hull, ordered by angle about the face centroid so that each carries a consistent orientation. This yields V \= 60, E \= 90, F \= 32 with twelve pentagons and twenty hexagons, χ \= 2, and B₂B₁ᵀ \= 0 with residual exactly zero. Faces being regular, the circumcenter coincides with the centroid, so the circumcentric dual is well defined; the dual edge length is the straight-line distance between adjacent face centroids, giving φ exactly on the thirty hexagon–hexagon edges and 1.4733704196 on the sixty pentagon–hexagon edges. Face areas at unit edge are A₅ \= 1.7204774006 and A₆ \= 2.5980762114, ratio 0.6622120602.

The signed icosahedral action is generated by two five-fold rotations, closed to sixty proper elements and extended by the inversion to the full group of order 120\. Each element acts on the edges as a signed permutation, with the sign recording orientation reversal, and the induced action on faces is fixed by the equivariance P\_F B₂ \= B₂ P\_E, which holds with residual exactly zero for all 120 elements, as does \[P\_F, L₂\] \= 0\. The ten conjugacy classes are identified by the pair (det g, tr g), giving sizes (1, 12, 12, 20, 15\) for the proper classes and the same for the improper ones, and isotype multiplicities are obtained by character projection against the standard I\_h table constructed from the A₅ character table by the rule χ\_u(i·c) \= −χ(c).

## **Appendix B. Why the Combinatorial–versus-DEC Dichotomy Is False**

The ZS-S18 handover framed Part I.a as a choice between the unweighted combinatorial Laplacian and the diagonal circumcentric DEC Laplacian, and cited Dodziuk and Patodi as the relevant authority. That reference in fact undermines the dichotomy. Dodziuk–Patodi establish that the combinatorial Laplacian converges to the metric Hodge–de Rham Laplacian under refinement when the correct inner product is the L² product of Whitney forms, whose mass matrices are not diagonal. The diagonal circumcentric star is a mass-lumped approximation to that Galerkin object, and its accuracy is a statement about a refinement limit. The truncated icosahedron admits no such limit within Z-Spin: ZS-S7 states explicitly that the polyhedral lattice is not an approximation to be refined but is itself the UV regulator selected by the geometry. There is therefore no continuum metric being approximated, no refinement parameter, and no sense in which the diagonal star is closer to a true answer than the identity. What replaces the dichotomy is the compatibility condition of Theorem S19.2, which is a statement internal to the complex and requires no ambient geometry at all.

## **Appendix C. Cross-Reference Table**

Table C.1. Upstream references consumed by ZS-S19 v1.6.

| Paper | Object consumed | Role in ZS-S19 | Status |
| ----- | ----- | ----- | ----- |
| ZS-F2 | A \= 35/437, δ\_X, δ\_Y | §2.1, §2.3 | LOCKED |
| ZS-F5 | Q \= 11, dim(Z) \= 2, (Z,X,Y) \= (2,3,6) | §2.1 | PROVEN |
| ZS-S4 | v \= 245.93 GeV | §10 | DERIVED |
| ZS-M6 §5 | TI Hodge complex, dim 182 \= 2 × 91 | §3, App. A | PROVEN |
| ZS-S1 §6.4 | α\_s \= 11/93, δ\_Y as Hodge asymmetry | §2.3, §10 | DERIVED |
| ZS-S7 §1 | the regulator axiom (R): the polyhedron IS the UV regulator | §4.10, App. B | IMPORTED; NOT sufficient for the selection |
| ZS-S7 | λ₁, Λ\_QCD, m(0⁺⁺) | §1, §3, §9, §10 | DERIVED-CONDITIONAL |
| ZS-S14 | master action, Wilson reduction, zero-parameter axiom | §4.5 | DERIVED |
| ZS-S17 v2.2 | DEC circumcentric M₁, λ\_h, Layer-Lift | §2.1, §3, §4.5, §6 | CERTIFIED |
| ZS-S18 v1.6 | Lemma S18.A, Thm S18.4, Thm S18.8, Thm S18.9, Gate A, §4.7, §7 | §4, §5, §7 | PROVEN / partly RETRACTED here |

## **References**

\[1\] K. Kang, “Geometric Impedance: A \= 35/437,” ZS-F2 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[2\] K. Kang, “dim(Z) \= 2 from Q \= 11,” ZS-F5 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[3\] K. Kang, “The Spinor Mass Gap: Deriving Λ\_QCD and the Glueball Mass from Polyhedral Hodge Spectral Theory,” ZS-S7 v1.0, Z-Spin Cosmology Collaboration (April 2026).  
\[4\] K. Kang, “Master Action Total Closure,” ZS-S14 v2.0, Z-Spin Cosmology Collaboration (May 2026).  
\[5\] K. Kang, “The Antisymmetric Two-Body Sector and the Hyperfine Structure of the Z-Spin Master Action,” ZS-S17 v2.2 FINAL, Z-Spin Cosmology Collaboration (July 2026).  
\[6\] K. Kang, “The Symmetric Two-Body Sector of the Z-Spin Master Action,” ZS-S18 v1.6 FINAL, Z-Spin Cosmology Collaboration (July 2026).  
\[7\] K. Kang, “Spectral-to-β Bridge,” ZS-S1 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[8\] K. Kang, “Register-Total Normalization and the Y-Sector Hodge–Dirac Operator,” ZS-M6 v1.0, Z-Spin Cosmology Collaboration (2026).  
\[9\] K. G. Wilson, “Confinement of quarks,” Phys. Rev. D 10, 2445 (1974).  
\[10\] J. Kogut and L. Susskind, “Hamiltonian formulation of Wilson’s lattice gauge theories,” Phys. Rev. D 11, 395 (1975).  
\[11\] M. Creutz, Quarks, Gluons and Lattices (Cambridge University Press, Cambridge, 1983).  
\[12\] W. Magnus, “On the exponential solution of differential equations for a linear operator,” Comm. Pure Appl. Math. 7, 649 (1954).  
\[13\] F. Peter and H. Weyl, “Die Vollständigkeit der primitiven Darstellungen einer geschlossenen kontinuierlichen Gruppe,” Math. Ann. 97, 737 (1927).  
\[14\] A. Haar, “Der Massbegriff in der Theorie der kontinuierlichen Gruppen,” Ann. Math. 34, 147 (1933).  
\[15\] J. Dodziuk and V. K. Patodi, “Riemannian structures and triangulations of manifolds,” J. Indian Math. Soc. 40, 1 (1976).  
\[16\] J. Dodziuk, “Finite-difference approach to the Hodge theory of harmonic forms,” Amer. J. Math. 98, 79 (1976).  
\[17\] H. Whitney, Geometric Integration Theory (Princeton University Press, Princeton, 1957).  
\[18\] A. N. Hirani, Discrete Exterior Calculus, Ph.D. thesis, California Institute of Technology (2003).  
\[19\] M. Desbrun, A. N. Hirani, M. Leok and J. E. Marsden, “Discrete exterior calculus,” arXiv:math/0508341 (2005).  
\[20\] A. Bossavit, Computational Electromagnetism (Academic Press, San Diego, 1998).  
\[21\] G. Kirchhoff, “Über die Auflösung der Gleichungen, auf welche man bei der Untersuchung der linearen Verteilung galvanischer Ströme geführt wird,” Ann. Phys. Chem. 72, 497 (1847).  
\[22\] V. N. Gribov, “Quantization of non-Abelian gauge theories,” Nucl. Phys. B 139, 1 (1978).  
\[23\] D. Zwanziger, “Fundamental modular region, Boltzmann factor and area law in lattice gauge theory,” Nucl. Phys. B 412, 657 (1994).  
\[24\] H.-P. Pavel, “SU(3) Yang–Mills quantum mechanics in the flux-tube gauge,” arXiv:1611.06542 (2016).  
\[25\] H.-P. Pavel, “Unconstrained SU(3) Yang–Mills theory and the Gribov problem,” arXiv:2112.06248 (2021).  
\[26\] C. Lanczos, “An iteration method for the solution of the eigenvalue problem of linear differential and integral operators,” J. Res. Natl. Bur. Stand. 45, 255 (1950).  
\[27\] M. Lüscher, “Some analytic results concerning the mass spectrum of Yang–Mills gauge theories on a torus,” Nucl. Phys. B 219, 233 (1983).  
\[28\] P. van Baal, “The small-volume expansion of gauge theories,” Nucl. Phys. B 264, 548 (1986).  
\[29\] A. Athenodorou and M. Teper, “SU(N) gauge theories in 3+1 dimensions: glueball spectrum, string tensions and topology,” JHEP 12, 082 (2021), arXiv:2106.00364.  
\[30\] A. Athenodorou and M. Teper, “The glueball spectrum of SU(3) gauge theory in 3+1 dimensions,” JHEP 11, 172 (2020), arXiv:2007.06422.  
\[31\] C. J. Morningstar and M. J. Peardon, “Glueball spectrum from an anisotropic lattice study,” Phys. Rev. D 60, 034509 (1999).  
\[32\] R. E. Moore, R. B. Kearfott and M. J. Cloud, Introduction to Interval Analysis (SIAM, Philadelphia, 2009), ch. 8\.  
\[33\] A. Jaffe and E. Witten, “Quantum Yang–Mills theory,” Clay Mathematics Institute Millennium Prize problem description (2000).  
\[34\] Particle Data Group, R. L. Workman et al., “Review of Particle Physics,” Prog. Theor. Exp. Phys. 2022, 083C01 (2022), and 2024 web update.

## **Version History**

v1.0 (July 2026): Initial public release. (Consolidated from internal Z-Spin Collaboration research notes up to v0.9.4 and from the ZS-S18 v1.6 handover seed report.) Claimed closure of F-S18.16 in outcome 1, on the strength of a Scale-Gauge Theorem, a Star-Compatibility Selection Theorem stated as an equivalence, and a Haar-democracy theorem. Verification 57/57 PASS, three OPEN gates, nine non-claims.

v1.1 (internal, July 2026): First response to external review. Retracted the necessity half of Theorem S19.2 on the reviewer's counterexample; withdrew Theorem S19.3 (Haar) and the four-gauge table; introduced the anchoring defect identity and Theorem S19.2′; separated the Faddeev–Popov spectral gap from any Gribov claim; corrected the gate register to seven OPEN. Left ρ \= (1,1) conditional on the ad-hoc hypothesis (H-β). Verification 64/64. Superseded before public release by v1.2 and retained only for the audit trail.

v1.2 (internal, July 2026): Added Theorem S19.6 in a two-realization form and Theorem S19.7 deriving the counting star from the corpus regulator axiom (R); withdrew (H-β). Verification 74/74. Superseded before public release by v1.3, which retracts three of its statements.

v1.3 (internal, July 2026): Following a second external review cycle. Retractions against v1.2. (i) The derivation of the counting star from (R) alone is RETRACTED; (R) denies an ambient metric but assigns no measures, and since n\_f ∈ {5, 6} a metric-free ψ(n\_f) realizes any ρ\_F \> 0\. The explicit axiom (R\_C), the cellular counting trace, is introduced in its place and labelled NEW and strictly stronger than (R). (ii) The description of the residual as 'finite, enumerated' and 'five discrete candidates' is RETRACTED; the residual under (R) alone is continuous, and Table 4.5 is relabelled an audit. (iii) The Hamiltonian relation κ\_e \= ½(β\_{f₁} \+ β\_{f₂}) is RETRACTED; the Legendre inverse gives κ\_e \= (M₁⁻¹)\_e and hence the harmonic mean, the arithmetic mean being the Lagrangian relation. Extensions. (iv) Theorem S19.6 is strengthened from two realizations to the full I\_h-invariant Regge moduli: Proposition S19.6a classifies the moduli as two-dimensional, and Q(t) \> 1 is verified on 4000 points with infimum 1.1463967982 at t ≈ 2.4160 and divergence at both ends. (v) The Legendre dictionary is derived and its regression to the generalized eigenproblem checked (gate F-S19.L). (vi) The three reduction routes C, W and D are pre-registered in §4.11, and F-S19.6 is restored to a decision gate with four pre-registered outcomes. Editorial. (vii) Gate F-S19.A is rewritten: v1.2 still carried a Layer-1 gate asserting the proposition v1.2 itself had refuted, and it is replaced by the defect-identity gate plus F-S19.A′. (viii) All residual v1.1 and v1.2 strings, check counts and (H-β) references are removed; §1.5 is rewritten to the current section structure; §9 records λ₁ as CONDITIONAL on (R\_C) ∧ (H-UA). Non-claims NC-S19.17–NC-S19.19 added, NC-S19.10 and NC-S19.16 rewritten. Verification 83/83 PASS, 7 OPEN, nineteen non-claims, twenty falsification gates across three layers. Unchanged since v1.0: Lemma S19.4 and its retraction of the ZS-S18 §7 sign, the Part II zeroth-order content, the Part III census, Corollary S19.5, and every numerical value in the corpus ledger.

v1.4 (internal, July 2026): Following a third external review cycle. Mathematical. (i) Theorem S19.6 is upgraded from a 4000-point scan to a PROOF. Reducing the Regge defect in closed form gives Q − 1 \= P(u)/\[20c(√3u − 1)(u \+ c)\] with P an explicit cubic; P has positive leading coefficient, P(0) \= 76.5678121575 \> 0, discriminant −3822266.5485 \< 0 and therefore a single real root, located at −1.4019488874 \< 0, so P \> 0 on the physical domain and Q(t) \> 1 for every t \> 0\. The v1.3 phrase 'infimum 1.1463967982 at t ≈ 2.415994' is corrected: those were grid values, and the true minimum is Q \= 1.1463953345 at t \= 2.4107050485. Retractions. (ii) v1.3's claim that Λ\_QCD is confined to 261–275 MeV over the whole compatibility line, and the associated gate F-S19.5 asserting that data outside 255–275 MeV would exclude the entire line, are RETRACTED: Λ\_QCD diverges as ρ\_F → 0 and tends to 429.7 MeV as ρ\_F → ∞. The band belongs to the audited window only, and F-S19.5 is rewritten as a point-prediction gate conditional on F-S19.6. (iii) The Layer-1 gate F-S19.A, which through v1.3 still declared PASS on the proposition that no incompatible metric can satisfy the anchoring identity — the very proposition this paper refutes — is replaced by the defect-identity gate and F-S19.A′. New. (iv) An outcome-B sensitivity table for the ZS-S17/S18 ledger, showing Ω₀ \= √λ₁ and hence G\_exch moving by under 2.5 % across the audited window. (v) A proof that the 90 \= 59 \+ 31 gauge census is the rank of the metric-free boundary operators and therefore survives every outcome of F-S19.6. Editorial. (vi) The abstract, which through v1.3 still carried the withdrawn hypothesis (H-β) and the superseded arithmetic-mean Hamiltonian relation because two earlier edits silently failed to match, is rewritten in full; the cover companion-code name, stale through three versions, is corrected; §2.1's 'zero new postulates' is corrected to 'zero new fitted parameters, two new structural hypotheses, explicitly firewalled'; §9's 'λ₁ status upgraded' becomes DERIVED-CONDITIONAL on (R\_C) ∧ (H-UA); NC-S19.15 is corrected from (R) to (R\_C); conclusion 6 no longer repeats the arithmetic-mean relation; the Acknowledgements section, dropped by an editing error in an internal revision, is restored. (vii) The two literal-True checks in the companion are replaced by assertions on the actual orbit counts, and the verification note now states that the checks are independent assertions but not independent derivations. Verification 89/89 PASS, 7 OPEN, nineteen non-claims, twenty-one falsification gates across three layers. Unchanged since v1.0: Lemma S19.4 and its retraction of the ZS-S18 §7 sign, the Part II zeroth-order content, the Part III census, Corollary S19.5, and every numerical value in the corpus ledger.

v1.5 (internal, July 2026): Following a fourth external review cycle. Epistemic. (i) The dependency of the headline results is UNBUNDLED. v1.4 tagged ρ \= (1,1) and λ₁ as conditional on (R\_C) ∧ (H-UA), but (R\_C) alone gives M₁ \= M₂ \= I and hence λ₁; (H-UA) is load-bearing instead for the criterion that makes Theorem S19.6 an exclusion. The correct tags are now carried throughout: counting-star selection DERIVED-CONDITIONAL on (R\_C) alone, Theorem S19.6 PROVEN as geometry with its selection bearing conditional on (H-UA), and their agreement recorded as joint corroboration rather than a shared dependency. Mathematical. (ii) Theorem S19.6 is given a certified proof that needs no discriminant: exactly c² \= (5 \+ 2√5)/5, a₀ \= 11 \+ 8√5 \+ 20√3c and a₁ \= −5√3 \+ 40c − 8√15 are positive; P′ has two positive roots, so min\_{u≥0} P \= min(P(0), P(u₊)) \= 65.7130202935 \> 0\. The bound is certified by outward-rounded interval arithmetic, P(\[2.20, 2.21\]) ≥ 64.8013718922, and corroborated by the discriminant argument and by an independent tail argument for u ≥ 4\. v1.4's positivity rested on double-precision evaluation of a discriminant and root count; that is now a corroboration, not the certificate. Scope. (iii) 'settles the metric route completely' is narrowed to 'settles the diagonal circumcentric Regge-metric route completely', in line with NC-S19.16. (iv) The claim that the gap is 3-fold 'everywhere' is replaced by verification over an audited domain, ρ\_F ∈ \[10⁻⁴, 10⁶\], thirteen decades, with NC-S19.20 stating that no no-crossing theorem is proved. (v) Machine-precision residuals are reported against thresholds rather than as fixed values, since the last digits are BLAS-dependent (NC-S19.21). Editorial. (vi) The v1.3 strings that survived into v1.4 are corrected: Table 4.3's caption, the §4.12 summary, conclusion 7's superseded minimum, gate F-S19.J's superseded minimum, and §9's opening sentence. Verification 93/93 PASS, 7 OPEN, twenty-one non-claims, twenty-one falsification gates across three layers. Unchanged since v1.0: Lemma S19.4 and its retraction of the ZS-S18 §7 sign, the Part II zeroth-order content, the Part III census, Corollary S19.5, and every numerical value in the corpus ledger.

v1.6 (July 2026): Public release, following a fifth external review cycle. No substantive claim is added, withdrawn or changed; the revision closes the last gaps between what the paper asserts and what its companion certifies. Dependencies. (i) The (R\_C) / (H-UA) separation introduced in v1.5 is now carried into the four places that still bundled them: Table 2.1, Table 9.1, gate F-S19.D and NC-S19.10, together with the F-S19.6 gate text emitted by the companion, which had continued to print the conjunction. Certification. (ii) The interval certificate is completed. v1.5 enclosed P on \[2.20, 2.21\] rigorously but located the critical point in that interval by a double-precision comparison. v1.6 adds three outward-rounded checks that close the gap end to end: P′(2.20) ≤ −0.1294914960 \< 0 and P′(2.21) ≥ \+0.1443741028 \> 0, so a critical point lies in the interval; P′′(\[2.20, 2.21\]) ≥ 27.2306753047 \> 0, so P is strictly convex there and that critical point is unique and is a minimum; and P(\[2.20, 2.21\]) ≥ 64.8013718922 \> 0\. (iii) mpmath is promoted from an optional import to a declared dependency: the companion now raises on ImportError rather than degrading to an eighth OPEN gate, so 95/95 PASS with seven OPEN gates is a fixed specification rather than an environment-dependent one, and the description 'numpy and scipy only' is corrected throughout to 'numpy, scipy and mpmath'. Reporting discipline. (iv) The fixed value 6.7 × 10⁻¹⁵ for the defect-identity residual, which survived in the abstract, §2.3, the statement of Theorem S19.2, gate F-S19.A and conclusion 2 despite NC-S19.21, is replaced everywhere by the threshold 10⁻¹² with the observation that realized residuals are O(10⁻¹⁴) and BLAS-dependent. (v) The phrase '3-fold everywhere', which survived in the abstract, the caption of Table 4.2 and gate F-S19.C despite NC-S19.20, is replaced by 'threefold at all sampled points of the audited domain ρ\_F ∈ \[10⁻⁴, 10⁶\]', with the absence of a no-crossing theorem stated each time. Editorial. (vi) §1.3's version string, Appendix C's caption, the independent-evidence count in the verification note, and the companion's own section comment and check-count narration are brought to v1.6. Verification 95/95 PASS, 7 OPEN, twenty-one non-claims, twenty-one falsification gates across three layers. Unchanged since v1.0: Lemma S19.4 and its retraction of the ZS-S18 §7 sign, the Part II zeroth-order content, the Part III census, Corollary S19.5, and every numerical value in the corpus ledger.

*Note on dating. The ZS-S19 template carries March 2026 as its metadata example. This paper is dated July 2026 because its immediate predecessors ZS-S17 v2.2 FINAL and ZS-S18 v1.6 FINAL are dated July 2026, and a paper cannot predate the handover it executes. The deviation is deliberate and recorded rather than silently applied.*