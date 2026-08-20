# ZS-M61 — The Boundary-Asymmetry Geometry and the S14 Seam-Symmetry Obstruction

### The Arc-Restricted Reflection-Asymmetry Theory, the Universal Phase Floor, the Seam Type Repair, and a Haar-Phase Goldstone No-Go

Author: Kenny Kang
Affiliation: Z-Spin Cosmology Collaboration
Date: March 2026 (corpus protocol date); audited and released July 2026; revision v1.1, 17 August 2026 (KST), audit-integrated; revision v1.2, 17 August 2026 (KST), second audit integrated and six breakthrough routes executed; revision v1.3, 17 August 2026 (KST), the five open items executed against the actual ZS-S14 v2.0 action; revision v1.4, 17 August 2026 (KST), the ZS-F1 type repair; revision v1.5, 17 August 2026 (KST), completion; **revision v1.6, 17 August 2026 (KST), release audit — six editorial defects corrected, none scientific, TERMINAL-IN-SCOPE re-asserted**
Theme / Paper code: Mathematical Spine — **ZS-M61 v1.6 · TERMINAL-IN-SCOPE · EIGHT RESULTS UNCONDITIONAL · GOLDSTONE ROUTE CLOSED-NEGATIVE-CONDITIONAL ON (H-U1-BDY) · NO SUCCESSOR VERSION REQUIRED**
Parents: ZS-M60 v1.5; ZS-M59 v1.8; ZS-M57 v1.8; ZS-M56 v1.8; ZS-S14 v2.0
Dependencies: ZS-M1; ZS-M54 v2.2; ZS-A3; ZS-Q7; ZS-Q18 v1.7; ZS-S28 v3.1; ZS-U9; ZS-U12 v2.3; ZS-F5
Supersedes: ZS-M61 v1.0 (July 2026), v1.1–v1.5 (17 August 2026). **v1.6 is a release audit: six defects, every one a statement the paper makes about itself rather than about physics. Subtitle and abstract brought into agreement with the status line (Gate K); the false 'strict subledger' provenance replaced by the measured one; the 'FINAL blocked only by the DOI' claim withdrawn; one stale non-claim clause folded; the artifact's own self-description made current. No number changes; §46 is the register.** **v1.5 is a completion, not an extension: no new research. It narrows Theorem M61.22 to the conjugacy class it can support, names the hypothesis (H-U1-BDY) that Theorem M61.23 needs, registers the typed intertwiner ι_ZΦ that v1.4 assumed, retypes two verifier rows to match what they compute, and installs the §43.2 reading rule that makes every earlier Part current. §44 is the closing status board; §42 sequences the upstream work.** **v1.4 repairs the type error at the root of the v1.3 dichotomy: ZS-F1 §2.3 defines ε ≡ |Φ| ≥ 0, which is seam-EVEN, so the seam-odd observable is Im Φ. Part IV survives the substitution verbatim; the uniform-Goldstone route is then closed negatively and unconditionally by a Bessel bound. §38 gives the recommendation on revising ZS-S14.** **v1.3 executes the five items v1.2 left open: two closed, one closed negatively, one — the exact seam symmetry (F2) — found to FAIL by a theorem, and one (the DOI) not closable by computation. §28.6 lists exactly which results are unconditional and therefore unaffected.** v1.1 corrected v1.0's title, §7.2 status, §9 quantifier, §14 verdict, §11.2 scan figures and printed residuals. v1.2 keeps every one of those corrections, adds **six new theorems M61.13–M61.18** that execute the six breakthrough routes the v1.1 audit proposed, **dissolves debt D-M61-VAC**, **promotes the divisor result back to an unconditional CLOSED-NEGATIVE on the λ-compatible class**, and **replaces the single deliverable D-M61-FWD by two logically independent one-number gates**. **No section of v1.0 or v1.1 is deleted; every superseded statement is recorded in Appendix D.**

---

## Verification Summary — retyped

**Ledger: 91 rows, 0 FAIL, exit 0.** Independently re-executed on 17 August 2026 (CPython 3.12.3, mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1) from `zs_m61_verify_v1_0.py`, SHA-256 `9fb1d8e9…52377e`. The emitted JSON ledger is **byte-identical, row for row, to the shipped artifact** (SHA-256 `1ed4180d…b60cd`); the run is deterministic under seed 20260731.

**What that certificate is, stated at exact strength.** It is a *regression certificate*: the manuscript and the computational artifact do not contradict each other, and the run reproduces exactly. It is **not** 48 machine-proved theorems. An abstract-syntax-tree audit of the 72 static `row(...)` call-sites gives:

| Class | Executed rows | Of which the test argument is the literal `True` | Rows carrying an executed test |
|---|---|---|---|
| THEOREM-PROOF | 48 | **23** | 25 |
| NUMERIC-WITNESS | 16 | 1 | 15 |
| GUARD | 17 | 12 | 5 |
| DECLARATION | 10 | 10 | 0 |
| **Total** | **91** | **46** | **45** |

**Fewer than half of the 91 rows execute any test at all.** The 23 literal-`True` THEOREM-PROOF rows are enumerated in Appendix E and are re-typed there as DECLARATION or as paper-proof-only. The v1.0 banner "91/91 PASS (48 THEOREM-PROOF …)" is therefore withdrawn as a headline claim and replaced by the retyped census above. This is a presentation correction, not a mathematical one: every theorem of this paper has a written proof, and the correction is about what the *script* certifies.

**Retyped census, in the audit taxonomy** (P proof / C certified computation / V numerical verification / W witness / R regression / G guard / D declaration / T tautology):

`P: 0 (script) · C: 0 · V: 18 · W: 11 · R: 6 · G: 5 · D: 46 (incl. 23 retyped from THEOREM-PROOF) · T: 5 · FAIL: 0`

Rows retyped relative to the v1.0 banner: **28**. Rows that actually support a central claim of this paper: **21** (blocks C, E, F, H, J).

**The v1.1 artifact.** `zs_m61_verify_v1_1.py` supersedes the v1.0 script and implements every requirement of §18.2. **Ledger: 123 rows, 0 FAIL, exit 0.** Its taxonomy carries no `THEOREM-PROOF` kind at all, because a script does not prove theorems; the 23 statements v1.0 mis-typed are now `DECLARATION` rows each carrying a pointer to the section of this manuscript that proves them (Appendix E), and a real computation has been substituted wherever one was available.

| Kind | v1.1 rows | What the row certifies |
|---|---|---|
| VERIFICATION | 65 | a closed form or an identity, evaluated and compared at a declared tolerance |
| WITNESS | 6 | a random, grid or single-instance execution — explicitly not a proof |
| REGRESSION | 10 | reproduces a corpus number, or pins an Appendix D correction |
| GUARD | 10 | a negative control that fails if the named error is made |
| TAUTOLOGY | 2 | a check whose two sides share their premise — the §7.2 controls |
| DECLARATION | 30 | scope, provenance or verdict; no computation, proof pointer required |
| **Total** | **123** | **93 rows execute a test; 30 do not and say so** |

> ### READING RULE (normative, v1.5 — read this before Parts I–V)
>
> Parts I–V were written before the §34 type repair. They are **current as written** under one substitution, applied everywhere:
>
> | Symbol as written | Read as | Defined in |
> |---|---|---|
> | **ε̂** | **Ŝ = Im(e^{−iα}Φ̂)**, the seam-odd observable | §34.3, §40.2 |
> | **ε_max** | **S_max**, the support radius of Ŝ | §34.3 |
> | **(H-VAC-BDY)** | **(H-QUAD)**, support at θ = ±π/2 | §34.3 |
>
> The symbol **ε** in the ZS-F1 sense — the radial amplitude \|Φ\|, which is seam-**even** — occurs only in §§34, 40 and in marked quotations of superseded text. One exception to currency: **Theorem M61.21** is retired as a physical computation (it averaged the seam-even variable) and retained as a lemma. §43.3 lists the five superseded statements with their replacements; §44.1 is the authoritative status board.

**The v1.6 artifact.** `zs_m61_verify_v1_6.py` supersedes the v1.5 script. **Ledger: 228 rows, 0 FAIL, exit 0** — 157 tested, 71 declarations. It adds **block V6 (8 rows)**, which does not touch the science: it measures the ledger provenance rather than asserting it, installs Gate K, records the four wording corrections, guards the artifact's own self-description, and pins the five core constants so a future edit cannot drift them. **All 220 v1.5 rows are carried forward with identical residuals.**

**The v1.5 artifact.** `zs_m61_verify_v1_5.py` supersedes the v1.4 script. **Ledger: 220 rows, 0 FAIL, exit 0** — 154 tested, 66 declarations, byte-identical on re-execution. It adds **block V5 (15 rows)**: the reflection conjugacy class computed at 401 angles, the SO(2) involution sweep, the Bessel identity now **integrated** at eight values of u rather than asserted, and the declarations naming (H-U1-BDY) and registering D-M61-IOTA. Two v1.4 rows are retyped to state only what they test. **Provenance, measured rather than asserted:** of the 204 v1.4 rows, **200 are carried forward with identical claim strings and identical residuals**, **4 were retyped or replaced** (one in block X, three in block Y), and **20** rows are new; there is **no residual drift** on any carried row. The v1.4 ledger is therefore **not** a strict subledger — v1.5 deliberately retyped and reordered rows — and the accurate statement is that the v1.4 computations are regression-preserved except for the explicitly retyped or replaced rows. *(v1.5 wrote "strict subledger"; corrected in v1.6, §46.1.)*

**The v1.4 artifact.** `zs_m61_verify_v1_4.py` supersedes the v1.3 script. **Ledger: 204 rows, 0 FAIL, exit 0** — 149 tested, 55 declarations. It adds **block X (10 rows)**, the involution classification and the TYPE LOCK; **block Y (7 rows)**, the Bessel no-go and the von Mises tautology control; and **block Z (6 rows)**, the broken-seam budget and the dual certificate. The v1.3 computations are regression-preserved and carried forward unchanged.

**The v1.3 artifact.** `zs_m61_verify_v1_3.py` supersedes the v1.2 script. **Ledger: 181 rows, 0 FAIL, exit 0** — 134 rows execute a test, 47 are declarations with proof pointers. It adds **block T (15 rows)**, which reconstructs the A₅ irreps **3**, **3′**, **5** from scratch, rebuilds the ZS-M10 unique Yukawa invariant, and decides W1/W3/W4; **block U (5 rows)**, the general M\*(a; u) against an independent arc LP; **block V (9 rows)**, the kink-weight FWD-I computation and the FWD-R conditional chain; and **block W (5 rows)**, the prior-art and release-status declarations. Output filenames are now derived from the script basename, closing §18.2(7). Every earlier block is carried over unchanged, so the v1.2 computations are regression-preserved.

Blocks: A–M are the v1.0 rows retyped (101 rows, up from 91 because six literal-`True` statements split into several executable tests); **N** is the ten-row v1.1 audit-integration block, which verifies the ZS-M57 M57.C.2 bijection, verifies that Theorem M61.7′ *is* that bijection under φ = 2c, s = ⟨ε⟩, and records the two tautology controls showing the §7.2 agreement is a priori; **R** is the nine-row errata regression block pinning every correction of Appendix D; **S** is the three-row self-audit that re-parses the script's own source and fails if any tested row passes a literal `True`.

**The v1.2 artifact.** `zs_m61_verify_v1_2.py` supersedes the v1.1 script. **Ledger: 147 rows, 0 FAIL, exit 0** — 112 rows execute a test, 35 are declarations with proof pointers. It adds **block P (24 rows)**, the executable content of the six breakthrough derivations of §§19–25: the characteristic-function form of the multiplier in every dimension with no vacuum hypothesis, the universal phase floor over six support radii, the closed form of the arc-asymmetry function T(u) against an independent arc-restricted linear program, the two factorised forward gates, the unconditional divisor result on the λ-compatible class, and the codimension-1 reachability sensitivity. Every other block is carried over unchanged, so the v1.1 computations are regression-preserved in the v1.2 ledger.

| Kind | v1.0 | v1.1 | v1.2 |
|---|---|---|---|
| VERIFICATION | — | 65 | 84 |
| WITNESS | — | 6 | 6 |
| REGRESSION | — | 10 | 10 |
| GUARD | — | 10 | 10 |
| TAUTOLOGY | — | 2 | 2 |
| DECLARATION | — | 30 | 35 |
| THEOREM-PROOF *(kind abolished at v1.1)* | 48 | 0 | 0 |
| **Total** | **91** (46 untested) | **123** (30 untested) | **147** (35 untested) |

| Kind | v1.3 | v1.4 | v1.5 | v1.6 |
|---|---|---|---|---|
| VERIFICATION | 103 | 116 | 119 | 119 |
| WITNESS | 6 | 6 | 6 | 6 |
| REGRESSION | 13 | 14 | 15 | 17 |
| GUARD | 10 | 10 | 11 | 12 |
| TAUTOLOGY | 2 | 3 | 3 | 3 |
| DECLARATION | 47 | 55 | 66 | 71 |
| **Total** | **181** | **204** | **220** | **228** (157 tested, 71 untested) |

(**A**, **Q**, dim **Z**) = (35/437, 11, 2) LOCKED. **A** enters this paper only as a conditional diagnostic in §11.3 and in no derivation. **Q** and dim **Z** enter only through named corpus hypotheses. Three real constants are printed — T₂ = 0.835381287313630, c\* = 1.086474189775053, ⟨ε⟩\* = −0.835381287313630 — each a closed form in the frozen ZS-M1 multiplier alone. **§7.2 of this version proves that the last two are a change of coordinates on λ and carry no evidential content for the derivation of λ**; the first is an independent theorem and does.

**Free fitted numerical parameters: 0. Declared structural choices: 6 (enumerated in §11.1a).** The phrase "zero free parameters" is not used unqualified anywhere in v1.1.

---

## §0. Abstract

ZS-M60 closed the formal classification of the Z-Spin quantum non-demolition (QND) event and left the physical bridge open behind three named inputs: the all-orders validity of the seam grading, the seam-ℤ₂ asymmetry of the actual ZS-S14 boundary state, and whether that state lives on the ZS-A3 vacuum doublet at all. It also issued an erratum against ZS-S14 v2.0, whose colour clause is void as written. ZS-M61 performs the repair, classifies the graded realisations completely, and isolates — but does not close — the one physical statement the bridge still needs.

The repair R0 is minimal and introduces no field: SU(3)\_C acts on the Standard-Model fermion colour factor ℂ³\_C, which the theory already carries, while the icosahedral Higgs carrier H₅ is a colour singlet. This is forced, because H₅ ↓ D₃ = 1 ⊕ (2 ⊗ ℂ²\_mult) has no second doublet and su(3) has no two-dimensional representation.

The engine of the paper is an algebraic identity the corpus had not extracted. Under the exact seam grading, the pointer-conditioned branch evolutions obey U₁ = J\_E U₀ J\_E, so the relative unitary is V = J\_E U₀† J\_E U₀. Covariance alone gives det V = ±1; the dilation form gives det V = +1 exactly. That single extra sign is load-bearing: it forces the eigenvalue −1 of V to have even multiplicity, so the two-atom measure attaining the ZS-M60.23 floor M\* = 0.763362818245964 cannot be carried by any environment of dimension three or less. On a carrier of dimension at most three the floor rises, in closed form, to

**T₂ = |Im λ| / √(1 − (Re λ)²) = 0.835381287313630 ,**

and this value is attained. The corpus therefore has a strictly sharper number than the one it has been carrying, and this is the paper's strongest Z-Spin-internal result.

A second rigidity removes the dimension question from the physical problem. The minimal seam-odd Z-bias vertex g Z\_path ⊗ ε̂ gives V = exp(−2icε̂) with c = τg, and on the ZS-A3 vacuum manifold ε² = 1 the multiplier is a = cos 2c − i sin 2c ⟨ε⟩ in every environment dimension: the Hilbert-space size cancels exactly and only the ε-marginal of the boundary law survives.

**What matching a = λ does and does not establish, stated in the abstract because v1.0 stated it too strongly.** The system is two real equations in two real unknowns and the principal-branch solution is unique:

**c\* = ½ arccos(Re λ) = 1.086474189775053 ,  ⟨ε⟩\* = − Im λ / √(1 − (Re λ)²) = − 0.835381287313630 .**

The reconstructed multiplier equals λ to 2.7 × 10⁻⁵¹ at fifty digits. **This is an identifiability result, not a derivation of λ.** Under the substitution φ = 2c, s = ⟨ε⟩ it is *the same change of coordinates* that ZS-M57 Theorem M57.C.2 proved to be a bijection λ ↔ (φ, s) and that ZS-M57 §11.3 explicitly judged to "transport the multiplier into collision coordinates rather than deriving it", with zero evidential content by ZS-M56 Theorem M56.7. ZS-M61 v1.0 promoted the same algebra to "Zero-Parameter Selection and the Terminal Solution"; v1.1 withdraws that promotion. The surviving claim is stated at exact strength:

> Under (F1), (F2) and (H-VAC-BDY), the S14-compatible two-valued boundary ansatz admits a **unique** minimal-phase realisation of the target multiplier λ, with no additional fitted numerical parameter.

The complementary statement — that the repaired ZS-S14 action *independently produces* (c, ⟨ε⟩) and that their value *turns out* to be (c\*, ⟨ε⟩\*) — is **OPEN**, and is registered as this paper's single forward deliverable D-M61-FWD.

The boundary state follows in closed form from the same conditional: a classical mixture of the two Z-bias vacua with populations (1 ± T₂)/2 = 0.917690643656815 and 0.082309356343185, purity 0.848930947596889, entropy 0.284373704659211 nats, which is 41.03% of the ZS-Q7 Z-channel capacity ln 2. Every ZS-M60 ceiling tightens and none is reversed. Two downstream statements change: the phase budget falls from 0.270022 to 0.179867 e-folds, so at most one complete Z-cycle can carry the phase, and the ZS-M60.32 observation ⌊n\_max⌋ = 2 = dim **Z** is retired as the numerology it was flagged to be.

Three further results are proved, of which two are unconditional. **(i)** A first-order vertex cannot produce λ: the identity v sin c = sin(½ arccos Re λ) forces c ≥ 1.086474189775053 regardless of the odd fraction v, so the event is intrinsically non-perturbative — CLOSED-NEGATIVE, unconditional within the graded doublet class. **(ii)** The physical anchor divisor is empty **for families in general position**: a zero requires Tr V = 0 and r ⊥ n̂ simultaneously, two real conditions on a one-parameter holonomy circle. v1.0 read this codimension count as an unconditional D\_phys = 0; v1.1 corrects the quantifier to *generic* and registers the transversality of the actual S14 family as a separate OPEN gate. **(iii)** The general minimal-asymmetry function M\*(a), with its inner-diamond and outer-domain split, is stated and certified against an independent 1800-atom linear program; it is the strongest stand-alone result here for external publication, and its prior-art status is NOT\_FOUND, which is not the same as NEW.

**New in v1.2 — the six routes executed.** Four results replace hypotheses by theorems. **(1)** The multiplier is the characteristic function of the Z-bias marginal, a = Φ_P(−2c), for every boundary state in every dimension with no support hypothesis; the anchor value ε = 0 and the bulk values ε = ±1 are the two ends of one support interval, so the v1.1 material conflict D-M61-VAC is **dissolved** rather than decided. **(2)** For any law supported in |ε| ≤ ε_max, Re a ≥ cos(2cε_max), so realising Re λ forces the **universal phase floor** c ≥ arccos(Re λ)/(2ε_max) = c\*/ε_max, with equality **iff** the law is concentrated on the extreme values. Vacuum support is therefore not a hypothesis competing with anchor localisation: it is the unique minimal-phase extremum, and anchor localisation is admissible at a price — ten times the minimal phase inside |ε| ≤ 0.1. **(3)** T₂ and M\* are the two exact endpoints of one strictly decreasing closed-form function T(u) of the effective seam arc u = 2cε_max, root of (1 − cos²u)T² − 2cos u(Re λ − cos u)T − |λ − cos u|² = 0, with T(φ) = T₂ and T(π) = M\*; the carrier-dimension theorem is its left-endpoint corollary, and **the derivation never uses det V = +1**, so the sharpened floor survives the failure of the result v1.0 called its engine. **(4)** On the λ-compatible class Re a = cos 2c = Re λ ≠ 0 is holonomy-independent, so the anchor divisor is empty **unconditionally** there and (H-GP) is needed only off the class. Finally, the forward problem is factorised into two independent one-number gates on disjoint data — an inequality on the dynamics and an equality on the boundary law, |⟨ε⟩| = T₂ with falsification sensitivity 0.714693 — and Theorem M61.17 shows the free clock leaves a one-dimensional attainable curve, so λ is reached only in codimension one and the model is falsifiable by a single derived number.

**New in v1.3 — the open items executed, and one of them fails.** The three finite items to which v1.2 reduced the exact seam covariance (F2) were run against the actual ZS-S14 v2.0 master action. **Theorem M61.19** proves that the Gram form of the unique I-invariant Yukawa tensor on the Higgs index is isotropic, G_{mn} = δ_{mn}/5 by Schur's lemma, so **every slot of the 5 carries exactly 1/5 of the tensor norm and none can vanish** — reproducing ZS-M10's Σσᵢ² = 1/5 and extracting from it the consequence the corpus had not drawn. Since the Yukawa term is linear in H₅, the D₃-trivial slot — the slot ZS-S14's own hypothesis H_id identifies with the Z-bias field ε — carries a term **linear in ε**, with weight 1/√5. Therefore σ: ε ↦ −ε is not a symmetry of S_S14: **item W1 fails, and (F2) fails at the classical level, not merely unproved.** The escapes are blocked: extending σ to the fermions would flip the doublet Yukawa, and σ extended to H₅ does not commute with I (commutator residual 1.603). In passing, ZS-S14 v2.0 was found to assert **two incompatible identifications of Φ** — the D₃-trivial component in §7.1, the neutral component of the D₃-2 doublet in §7.5 — so the gauge-singlet item W3 cannot be settled either; registered as upstream debt D-S14-PHI. The resulting dichotomy is stated exactly in §28.5, and §28.6 shows that **four results are unconditional mathematics and are unaffected**: R0, Theorem M61.3, Theorem M61.11 and the new Theorem M61.20. Three further items are closed. **Theorem M61.20** gives the general two-parameter M\*(a; u) in closed form with its feasibility boundary cos u ≤ x, its inner-diamond branch and its two-atom extremal structure, certified against an independent arc-restricted linear program on 46 (a, u) pairs to 4.2 × 10⁻⁶; Theorems M61.11 and M61.15 are its two boundary cases, so **D-M61-ARC is closed**. **Theorem M61.21** produces the programme's **first target-blind number**: for the ZS-A3 kink profile the mean bias of the radial weight (1 − ε²)^p is ⟨ε⟩(p) = Γ(p+3/2)/(√π Γ(p+2)), giving exactly 1/2, 3/8 and 5/16 for the arclength, energy-density and potential weights — all below T₂ = 0.835381, which would require the negative exponent p\* = −0.847672, i.e. a weight diverging integrably at the vacuum. **FWD-I is therefore CLOSED-NEGATIVE on the canonical-weight branch.** And the prior-art search for Theorem M61.11 is executed with locators, retaining NOT_FOUND honestly.

**New in v1.4 — the type repair, and the first unconditional no-go.** ZS-F1 v1.0 §2.3 states verbatim that the legacy scalar is recovered as **ε ≡ |Φ|**, the radial mode of the complex Z-bias field Φ = ρe^{iθ}. Hence ε ≥ 0, the map ε ↦ −ε leaves the field space, and the vacuum manifold is the **circle** |Φ| = 1 rather than the two-point set {−1, +1}. **Theorem M61.22** classifies the involutions of the field space preserving V(|Φ|): the reflections, all conjugate to complex conjugation Φ ↦ Φ̄ with even mode Re Φ and odd mode Im Φ; and the central half-shift Φ ↦ −Φ, which by ZS-M56 M56.22′ admits zero odd operators. **The unique admissible seam involution is complex conjugation, and it is the corpus's own** — it is exactly J_seam\|_Z = diag(+1, −1) of ZS-M54 M54.8a and ZS-F0 Def 8.11. Therefore ε = \|Φ\| is **seam-even** and cannot be the vertex operator; **the seam-odd observable is Im Φ**. A TYPE LOCK is installed (§34.3) separating ρ, θ and S := Im Φ. The whole of Part IV survives the substitution ε̂ → Ŝ verbatim, because it was stated for a bounded seam-odd observable and not for a named field; only §30's radial-weight computation is retired. **Theorem M61.23** then gives the programme's first target-blind result (stated unconditionally in v1.4; see §41 for the corrected status): on the vacuum circle with the uniform phase law that ZS-F1's exactly flat Goldstone potential supplies, a(c) = E[e^{−2ic sin θ}] = **J₀(2c)**, which is exactly real, so Im λ is unreachable; and min J₀ = **−0.402759395702552972 > Re λ = −0.566417330285464**, so Re λ is unreachable **at every accumulated phase**, deficit 0.163657934582911431 — with no hypothesis, no fitted parameter and no clock. A von Mises bias of concentration κ\* = 3.740875 at c = 1.290067 does reproduce λ to 5 × 10⁻¹⁵, but that is two reals fitted to two constraints, the ZS-M56.7 trap, and it gives the Goldstone a mass, contradicting ZS-F1 results 1 and 3. **Either θ is massless and λ is unreachable, or λ is reachable and θ is not massless.** Two further items are discharged: **Theorem M61.24** gives the broken-seam budget, with the phase floor moving only 5% and the asymmetry floor 1.4% under a 10% breaking amplitude; and Theorem M61.20 now carries a **dual certificate** with zero duality gap at the minimal arc, an interior arc and the full circle, making it quotable without the verifier.

**v1.5 — the completion, and the two corrections it makes to v1.4.** First, the involution statement is narrowed. What is established is that the potential-preserving involutions of the Z-bias field space split into +I (trivial), −I (central, and by ZS-M56 M56.22′ admitting zero odd operators), and a **single continuous conjugacy class of reflections** J_α : Φ ↦ e^{2iα}Φ̄, of which complex conjugation is one representative — **not** that complex conjugation is unique (**Theorem M61.22′**, verified at 401 angles). The odd mode Im(e^{−iα}Φ) is representative-dependent, but every quantitative result of Part IV depends only on the law of the odd component and is therefore α-independent. And the identification of ZS-F0's abstract parity eigenbasis with (Re Φ, Im Φ) is **not** established: it requires a typed intertwiner ι_ZΦ with ι∘J_Z = J_C∘ι, which is registered **OPEN** as D-M61-IOTA. Consequently **ZS-F0 is not to be corrected on this evidence** (§42). What survives untouched is the ZS-F1 finding itself: ε ≡ \|Φ\| is a function of \|Φ\|², hence even under every admissible involution, so the radial amplitude can never be the seam-odd vertex operator. Second, the Goldstone no-go is made conditional. A flat potential makes every θ energetically degenerate but does **not** make the state uniform — spontaneous breaking is precisely a symmetric action with a phase-selecting state — so the hypothesis **(H-U1-BDY)**, that the boundary phase law is Haar-uniform, is named and required. Under it **Theorem M61.23′** is unchanged as mathematics and now better certified, the Bessel identity being integrated at eight values of u rather than asserted: a(c) = J₀(2c) is exactly real and min J₀ = −0.402759395702552972 > Re λ = −0.566417330285464, deficit 0.163657934582911431, so λ is unreachable at every accumulated phase. The physical verdict is lowered from unconditional to **CLOSED-NEGATIVE-CONDITIONAL**. That costs less than it appears: (H-U1-BDY) is the maximum-entropy default law, so what is excluded is the theory's own default, and any surviving route must exhibit an explicit phase-selecting mechanism delivering a concentration of order κ ≈ 3.74 — not a perturbation.

**Verdict.** The graded S14-compatible realisation class is **completely classified**. The multiplier is realised **conditionally and uniquely** on (F2) and (H-VAC-BDY); the divisor is CLOSED-NEGATIVE-GENERIC; the perturbative sector is CLOSED-NEGATIVE; M\*-saturation is CLOSED-NEGATIVE for any carrier of dimension at most three. **The S14 selection of the realisation is OPEN.** No metric clock is required, because c\* is a dimensionless accumulated phase; the ZS-Q19 clock debt is untouched.

**Terminal status, stated once and consistently with §44.3.** Within its declared scope — the classification of arc-restricted reflection-asymmetry geometry for a bounded seam-odd observable, and the *location* rather than the closure of the S14 physical bridge — **ZS-M61 is TERMINAL-IN-SCOPE**. The physical S14 selection remains **OPEN** and lies outside that closure, as do the upstream debts D-S14-PHI and D-F1-EPS and the registered bridge D-M61-IOTA. *(v1.0–v1.5 ended this paragraph with "This paper is not terminal", which contradicted the status line from v1.5 onward; corrected in v1.6, §46.2.)*

Keywords: seam ℤ₂ grading, relative unitary, QND multiplier, i-tetration fixed point, Koenigs multiplier, resource theory of asymmetry, Fuchs–van de Graaf, numerical range, carrier dimension, identifiability, Z-Spin Cosmology.

---

## §0.1 What changed in v1.1, and why

Table 0.0. Audit integration register. Every row is a status change or a correction, with its cause and its downstream effect. Severity codes are S0 NOTE / S1 MINOR / S2 MAJOR / S3 CRITICAL.

| # | v1.0 statement | v1.1 status | Cause | Severity |
|---|---|---|---|---|
| 1 | Title: "The Terminal Physical Bridge of the ZS-S14 Boundary Process" | Retitled "The Graded S14-Compatible Realisation of the Coherence Multiplier" | The bridge is not closed; the title asserted more than the strongest verified claim (violates the no-silent-strengthening rule) | S2 |
| 2 | Theorem M61.7 "Zero-Parameter Selection and the Terminal Solution", promoted as a selection theorem | Renamed **Theorem M61.7′ (Vacuum-Supported Realisation / Reparametrisation)**; DERIVED-CONDITIONAL identifiability, zero evidential content for the derivation of λ; explicit equivalence to ZS-M57 M57.C.2 recorded | Internal conflict with ZS-M57 v1.8 §11.3, which had already judged the identical algebra non-evidential under M56.7 | **S3** |
| 3 | Theorem M61.10 "Empty Physical Divisor", D\_phys = 0, CLOSED-NEGATIVE | **Theorem M61.10′ (Generic Empty-Divisor)**, DERIVED-CONDITIONAL on (H-GP); status CLOSED-NEGATIVE-GENERIC; actual-family transversality registered as gate F-M61.18 | codim 2 > dim base 1 gives genericity, not universality; a constrained curve may meet a codimension-2 locus | S2 |
| 4 | (H-VAC) described as "corpus-supplied", HYPOTHESIS-strong, citing ZS-M57 §16.3 | Split into **(H-VAC-BULK)** (corpus-recorded, and not what the paper needs) and **(H-VAC-BDY)** (what the paper needs, HYPOTHESIS, with a recorded material conflict) | ZS-M57 §16.3 records bulk vacua ε = ±1 **and** that the physical mediation locus must localise at the Z-anchor where ε(r\_H) = 0; "bulk vacuum exists" does not entail "boundary-process state is vacuum-supported" | **S3** |
| 5 | Theorem M61.12 "Terminal S14 Bridge"; verdict CLOSED-POSITIVE-CONDITIONAL | **Theorem M61.12′ (Conditional S14-Compatible Realisation)**; verdict DERIVED-CONDITIONAL + IDENTIFIABILITY; physical selection restored to OPEN | Follows from #2 and #4 | **S3** |
| 6 | "Zero Free Parameters" as a banner claim | "Zero additional fitted numerical parameters, conditional on the declared structural model", with the six structural choices enumerated (§11.1a) | Zero fitted parameters ≠ zero choices; the choices were present but not counted in one place | S2 |
| 7 | Banner "91/91 PASS (48 THEOREM-PROOF …)" | Retyped census; 23 of 48 THEOREM-PROOF rows verified by AST to be literal `True` | Verification-count ≠ theorem-count | S2 |
| 8 | Anti-numerology Table 11.2: "2652 admissible expressions"; p(selected) 0 hits, p = 0.00000 | Corrected to **3362** expressions; p(selected) **1 hit**, p = 2.97 × 10⁻⁴ | The executed ledger reports 3362 formulas and one hit for p(selected); the manuscript table did not match its own artifact | S2 |
| 9 | Fourteen printed residuals and two draw-counts | Corrected against the executed ledger (Appendix D.2); the Acknowledgements claim that every deterministic figure appears verbatim in one seeded run is **withdrawn** | Manuscript↔artifact mismatch, e.g. reconstruction residual printed 1.2 × 10⁻⁴⁶ where the artifact gives 2.7 × 10⁻⁵¹; min\|a\| printed 1.8 × 10⁻³ where the artifact gives 2.31 × 10⁻³ | S2 |
| 10 | Code block: "exit code 1 on any FAIL **or on a row-count mismatch**"; "Exactly 91 ledger rows in every scenario" | Withdrawn: no row-count guard exists in the script. A guard is specified in §18.2 for the v1.1 artifact | Reproducibility claim not implemented | S1 |
| 11 | Three ledger claim-strings: n\_max = …407, arctanh T₂ = …244, τ\* = 12.7319 | Corrected to …409, …241, 12.7328 in the v1.1 artifact specification | Claim-string digits disagree with the closed forms they name | S1 |
| 12 | NC-M61.9 "No successor paper is reserved" | Replaced by NC-M61.9′ plus the registered forward deliverable **D-M61-FWD** | The forward-selection theorem is now a named, isolated object; declaring no successor would strand it | S1 |
| 13 | Theorem M61.2 presented as new structure | Retained as PROVEN, with prior-art scoping: the Cartan-embedding / compact-symmetric-space setting in which g⁻¹ = g^θ forces determinant +1 on the connected component is classical; what is new is the graded-relative-unitary identification and its use in §5 | Imported-theorem firewall | S1 |
| 14 | Theorem M61.11 presented as novel | Retained as PROVEN with prior-art status **NOT\_FOUND (not NEW)**; a targeted search did not locate the exact piecewise closed form, and NOT\_FOUND ≠ NEW | Novelty discipline | S1 |

**Nothing in §§3–6, §8, §10 or §12 of v1.0 is retracted.** The mathematics of Theorems M61.1–M61.6, M61.8 and M61.11 stands unaltered; the changes above are to scope, quantifier, status, provenance and printed figures. *v1.2 additionally generalises three of them — M61.4 becomes a corollary of Theorem M61.15, M61.8 becomes the SU(2) special case of Theorem M61.14, and M61.10′ is superseded on the λ-compatible class by Theorem M61.16 — in every case by removing a hypothesis (see Part IV).*

---

## §0.2 What changed in v1.2, and why

The second audit returned `AUDIT-MAJOR-REVISION → integrated` on the science and raised exactly one new defect, plus six research routes. Both are handled here.

### 0.2a The one new defect, and its status

**Finding (S2, MAJOR): manuscript ↔ artifact desynchronisation.** The audit read a copy of the v1.1 manuscript in which §18 still described `zs_m61_verify_v1_0.py`, 91 rows, no row-count guard and no `figures.json`, while the shipped script was already `zs_m61_verify_v1_1.py`.

**Status: ALREADY REMEDIATED, and re-verified here.** The synchronisation was performed in the same release action that produced the v1.1 script: the delivered v1.1 manuscript states `main_script: zs_m61_verify_v1_1.py`, `expected row count: 123`, marks §18.2 items 1–4 and 6 IMPLEMENTED, records the new SHA-256 values, and adds the v1.1 census as Table A.1b. The audited copy predates that action. v1.2 re-verifies the sync and extends it to the v1.2 artifact. **The finding is accepted as correct against the copy audited, and closed as already fixed.** No science moves.

**A registry conflict raised by the same audit, and NOT fixed here.** The audit reports recording its finding in `history.md` as **H-0008**. That identifier is already occupied — H-0008 is the 돌파 v1.0 → v1.1 protocol revision — and this paper's own audit rows were assigned H-0009 … H-0014. Two different events under one ID breaks the append-only register. **Status: [OPEN] registry conflict, debt D-M61-HIST.** Resolution is the register owner's call, not this paper's; the recommended fix is to reassign the audit's row to the next free identifier and to record the reassignment as its own row rather than editing either entry.

### 0.2b The six breakthrough routes, executed

The audit's central recommendation was to stop polishing sentences and change the representation of the problem. That is done. The results are new theorems, not restatements.

| Route | v1.1 state | v1.2 result | Where |
|---|---|---|---|
| 1. Boundary transfer law replacing the static state | (H-VAC-BDY) versus ε(r_H) = 0 read as a dichotomy; debt D-M61-VAC | **Theorem M61.13.** The multiplier is *always* the characteristic function of the ε-marginal, a = Φ_P(−2c), in every dimension, with no ε² = I hypothesis. The anchor value ε = 0 and the bulk values ε = ±1 are the two ends of **one** support interval, so there is no dichotomy. **D-M61-VAC is DISSOLVED**, not decided. | §19 |
| 2. Factorise responsibility: derive the two numbers by two mechanisms | one deliverable D-M61-FWD, two reals against two reals | **Two independent one-number gates.** FWD-R is a one-sided *inequality* on the dynamics; FWD-I is a single *equality* on the boundary law. Neither may see λ. This is the exit from the ZS-M56.7 two-for-two trap. | §22 |
| 3. Find the action-selected invariant instead of (c, ⟨ε⟩) | ½ Tr V identified as dynamics-only (Thm M61.5) but no target | **The invariant is the effective seam arc u = 2c·ε_max**, and the FWD-R target is the single real number ½ Tr V = Re λ = −0.566417330285464. | §20, §22.1 |
| 4. Close (F2) as an exact Ward identity, not order by order | (F2) an unexecuted all-orders assumption | **Reduction R1**: five finite items replace the infinite check, and the conclusion is structural — the seam ℤ₂ is exact on action, measure, gauge-fixing and regulator, and is broken **only** by the boundary condition at infinity. That is precisely where M57.P′ says the phase must live. | §25 |
| 5. Compute the divisor of the actual family | CLOSED-NEGATIVE-GENERIC, (H-GP) needed | **Theorem M61.16.** On the λ-compatible class Re a = cos 2c = Re λ ≠ 0 is holonomy-independent, so \|a\| ≥ \|Re λ\| = 0.566417 for every θ. **CLOSED-NEGATIVE unconditional there**; (H-GP) is needed only off the class. The 8000-draw witness is retired as a research instrument. | §23 |
| 6. Keep the negative outcome open as a theorem | registered as a possibility | **Theorem M61.17.** With the clock free, the attainable set is a curve; λ lies on it only in codimension one. Under (H-VAC-BDY) the whole content collapses to the single equation \|⟨ε⟩\| = T₂, with an explicit falsification sensitivity 0.714693. The clock freedom therefore does **not** make the model unfalsifiable — and if no target-blind derivation exists, the correct result is a stated Non-Identifiability Theorem. | §24 |

**One additional consequence, unplanned and the most useful of the set.** Theorem M61.15 (§21) shows that T₂ and M\* are the two endpoints of **one continuous, strictly decreasing function T(u)** of the effective seam arc, with T(φ) = T₂ and T(π) = M\* both exact. The v1.0/v1.1 carrier-dimension theorem M61.4 becomes a corollary, and — this matters for robustness — **the new route does not use det V = +1 at all.** The sharpened bound T₂ therefore survives the failure of Theorem M61.2, which v1.0 called its engine.

---

## Epistemic Status Legend

Every load-bearing statement below carries exactly one tag. A tag is part of the claim; quoting a statement without it is a citation error and fires gate F-M61.13.

| Status | Definition |
|---|---|
| LOCKED | Core constant fixed upstream; no downstream paper may modify it. |
| PROVEN | Mathematical theorem, complete proof under declared definitions. |
| DERIVED | Quantitative consequence of PROVEN items plus Z-Spin axioms, no additional fitted numerical parameter. |
| DERIVED-CONDITIONAL | DERIVED conditional on an explicitly named hypothesis or upstream result. |
| **IDENTIFIABILITY** *(new in v1.1)* | A statement that a target uniquely determines the parameters of a declared model. Carries **no** evidential content for the derivation of the target. Governed by ZS-M56 Theorem M56.7 and ZS-M57 Theorem M57.C.2. |
| VERIFIED | Numerical or computational confirmation at a stated precision. |
| REGRESSION | Reproduces a corpus number from corpus inputs; a drift guard, never independent evidence. |
| IMPORTED-PROVEN | Proved externally, used without re-proof, cited. |
| HYPOTHESIS-strong | Multiple independent structural anchors; promotion path documented. |
| HYPOTHESIS | Motivated, partially anchored; no promotion path executed. |
| OBSERVATION | Numerical regularity, anti-numerology controlled, structural origin pending. |
| NON-CLAIM | Explicit declaration of what is not asserted. |
| OPEN | Recognised gap, honestly registered. |
| RETRACTED | Earlier claim withdrawn after falsification. |
| CLOSED-NEGATIVE | A route proved impossible; a complete result, not a failure. |
| **CLOSED-NEGATIVE-GENERIC** *(new in v1.1)* | Proved impossible for objects in general position; the specific physical object's position is separately gated. *In v1.2 this status is vacated for the divisor: Theorem M61.16 restores CLOSED-NEGATIVE on the λ-compatible class.* |
| **DISSOLVED** *(new in v1.2)* | A registered conflict that a retyping of the objects removes, so that neither branch had to be chosen. Used once, for D-M61-VAC. |
| **PRICED** *(new in v1.2)* | An alternative that is not excluded but carries an exactly quantified cost in a derived quantity. Used for anchor localisation, whose price is accumulated phase. |
| CLOSED-POSITIVE-CONDITIONAL | *Not used in v1.1.* Retired as a status because v1.0 used it for what is in fact an IDENTIFIABILITY result. |

**Ledger rules**, inherited from ZS-M59 §0 and ZS-M60 §0 and extended twice. Rows are THEOREM-PROOF, NUMERIC-WITNESS, GUARD or DECLARATION. A claim string asserts only what its computation tests. An "exact" claim may not be certified by a tolerance test. A supremum or infimum claim may not be certified by a grid sample. A theorem may be applied only to objects of the type it quantifies over, and the type check is itself a row. New at ZS-M61 v1.0: a dimension-free claim may not be certified in a single dimension. **New at v1.1: (a) a row whose test argument is a literal `True` may not be typed THEOREM-PROOF; (b) every printed residual must be the value the shipped artifact emits, and the manuscript figure and the ledger figure must be generated from the same run; (c) a claim string that names a closed form must reproduce that form to the digits it prints.** 91/91 PASS is the integrity of a ledger, not the peer review of a manuscript, and — as §Verification Summary now states in numbers — not a proof of 48 theorems either.

**Blind-comparison firewall.** The construction of §7 was carried out with the target loaded only as the two frozen real numbers Re λ and Im λ, which are the equations being solved and cannot be withheld. **v1.1 adds the honest corollary the v1.0 firewall statement omitted:** because §7.2 solves two reals against two reals, the firewall cannot make that step evidential. It protects §§4–6 and §10, where the target does not enter the construction, and it does not protect §7.2, whose status is IDENTIFIABILITY for exactly that reason.

---

## §1. Introduction — the question, and the question that remains

### 1.1 What was left open

ZS-M59 handed its successor four deliverables and ZS-M60 executed them: no unimodular gauge datum closes the seam transport; the anchor-divisor route is empty on the entire phase-covariant class; **Q** = 11 carries an exact complete-order qubit code; and any seam-graded reduction reproducing the frozen multiplier λ requires a boundary state at least M\* = 0.763362818245964 asymmetric in trace distance. It declared itself TERMINAL-IN-SCOPE rather than TERMINAL, because two residuals remained open behind a named upstream repair.

The residuals are precise. First, the ZS-S14 v2.0 master action assigns the colour generators to a "D₃-2′ subspace of H₅" that does not exist. Second, ZS-M60 bounds the seam asymmetry of the boundary state without constructing that state, and records in NC-M60.4 and NC-M60.5 that it claims neither that the bound is met nor that it is failed. Third, ZS-M60.31–M60.33 translate the bound onto the ZS-A3 vacuum doublet only under (H-DOUBLET-SUPPORT), which an audit correctly showed cannot be obtained by projection.

### 1.2 The question this paper answers, and the question it does not

**Answered.** *What is the complete class of graded S14-compatible relative unitaries and boundary laws that can reproduce the frozen coherence multiplier λ, and what does each cost?* The answer is a classification: det V = +1 always; the minimal asymmetry is T₂ on carriers of dimension ≤ 3 and M\* above; Re a is dynamics-only on a graded doublet; the environment dimension cancels on the two-valued vacuum manifold; the accumulated phase is bounded below by c\* = 1.086474189775053; the anchor divisor is generically empty; and inside the vacuum-supported ansatz the realising data are unique.

**Not answered.** *Does the repaired ZS-S14 action select that realisation?* v1.0 claimed it did. It does not follow from anything in this paper. The distinction is the whole content of the v1.1 revision and is stated as two sentences that must never be conflated:

- (A) **Given λ, the vacuum-supported S14-compatible ansatz determines (c, ⟨ε⟩) uniquely.** — proved here, §7.2, IDENTIFIABILITY.
- (B) **S\_S14 independently produces (c, ⟨ε⟩), and those values reproduce λ.** — not proved here, OPEN, deliverable D-M61-FWD.

(A) is a fact about the model's parameter geometry. (B) is the physical bridge. ZS-M57 already made this distinction for the same algebra and this paper is now consistent with it.

### 1.3 What is new, stated before the proofs

(i) det V = +1 for every graded relative unitary, strictly stronger than the covariance statement det V = ±1, and by itself creating a carrier-dimension gap in the minimal-asymmetry problem. (ii) A closed-form minimal asymmetry T₂ that supersedes M\* on any carrier of dimension at most three. (iii) The state-independence of Re a on a two-dimensional graded carrier, in the sharp form Re a = ½ Tr V. (iv) The cancellation of the environment dimension under the two-valued vacuum manifold. (v) A non-perturbative lower bound on the accumulated branch phase. (vi) A generically empty physical divisor, by a codimension count. (vii) The general M\*(a) theorem with its correct domain split.

**Which of these is the paper's contribution, ranked for an external reader:** (vii) as stand-alone mathematics; (ii) and (i) together as the sharpest Z-Spin-internal correction; (v) as the explanation of why thirty-one versions of the S-line could not reach λ from an expansion; (iv) as the structural move that removes a hypothesis ZS-M60 could not remove; (iii) and (vi) as clean lemmas. **Item (iv) plus §7.2 is not a contribution to the derivation of λ** and is presented as classification, not as bridge.

---

## §2. Frozen inputs, and the provenance of λ

The i-tetration map f(z) = i^z has the unique attracting fixed point z\* of ZS-M1, and the Koenigs multiplier of the corpus is λ = f′(z\*) = z\* ln i. Because z\* = exp(z\* ln i), the multiplier is also the principal logarithm of the fixed point itself:

**λ = Log z\* ,  Re λ = ln|z\*| ,  Im λ = arg z\* .**

This identity is exact to the working precision (ledger row A2, residual 1.34 × 10⁻⁵¹ at 50 digits) and is used below only to record that the two real numbers this paper solves for are the modulus-logarithm and the argument of one frozen complex number, not two independent data. All ZS-M60 constants are re-derived here from z\* rather than transcribed.

Table 2.1. Frozen inputs. All values recomputed at 50 decimal digits from z\* alone and re-verified independently on 17 August 2026.

| Quantity | Symbol | Value (21 digits) | Status |
|---|---|---|---|
| i-tetration fixed point | z\* | 0.438282936727032111627 + 0.360592471871385485953 i | LOCKED (ZS-M1) |
| Koenigs multiplier | λ | −0.566417330285464402675 + 0.688453227107702130499 i | LOCKED (ZS-M1) |
| modulus | \|λ\| | 0.891513565776047042891 | LOCKED |
| argument | χ | 2.259249553902598749730 | LOCKED |
| contraction rate | μ = −ln\|λ\| | 0.114834624996009537949 | LOCKED |
| minimal general asymmetry | M\* | 0.763362818245963536496 | PROVEN (ZS-M60.23) |
| harmonic density at the antipode | ρ\_λ(π) | 0.309993067644787320906 | PROVEN (ZS-S28) |
| geometric impedance | **A** | 35/437 = 0.080091533180778032037 | LOCKED (ZS-F2) |
| register dimension | **Q** | 11 | PROVEN (ZS-F5) |
| seam dimension | dim **Z** | 2 | LOCKED |

Permitted structural inputs are exactly these, the repaired S14 action, and boundary data uniquely selected by that action. The following may not be solved from a = λ: a coupling, a duration, a Gaussian mean or variance, a correlation time, a sector weight, a theta angle, a profile width or a closure phase. **v1.1 adds the clause v1.0 should have carried:** c\* and ⟨ε⟩\* *are* solved from a = λ. They are the two real degrees of freedom the frozen vacuum law leaves, and solving them is legitimate as identification and illegitimate as derivation. §11.1 audits the count and §7.2 states the resulting status.

---

## §3. Theorem M61.1 — the typed ZS-S14 colour repair R0

*(Unchanged from v1.0 except where marked. Verified independently: ledger block B, 7 rows.)*

### 3.1 The defect, re-derived

**Theorem M61.1a (Restriction). [PROVEN].** The A₅ five-dimensional irrep has character (5, 1, −1) on the classes (e, order-2, order-3). Restricting to D₃ ≅ S₃ ⊂ A₅, whose class sizes are (1, 3, 2), character orthogonality gives

m₁ = ⅙(5 + 3·1 + 2·(−1)) = 1 ,  m₁′ = ⅙(5 − 3 − 2) = 0 ,  m₂ = ⅙(2·5 + 0 + 2) = 2 ,

**H₅ ↓ D₃ = 1 ⊕ (2 ⊗ ℂ²\_mult) ,  1 + 2·2 = 5 .**

There is no distinct second doublet: D₃ has exactly three irreducible complex representations, of dimensions 1, 1 and 2. Moreover su(3) is simple of dimension 8 while gl(2,ℂ) has dimension 4, so any Lie-algebra homomorphism su(3) → gl(2,ℂ) is trivial; independently the Weyl dimension formula gives su(3) irrep dimensions 1, 3, 6, 8, 10, 15, 21, 24, 27, … and never 2. The ZS-S14 v2.0 Definition 3.1 clause "λ^a₃ acts on the D₃-2′ subspace of H₅ (colour triplet leptoquark sector)" is therefore void twice over. This reproduces ZS-M60.25 exactly and is recorded here as the premise of the repair, not as a new finding.

### 3.2 The repair

**Repair R0. [PROVEN as a type statement].** Retain H₅ as the Higgs and finite-symmetry carrier and let it be a colour singlet. Let SU(3)\_C act on the Standard-Model fermion colour factor ℂ³\_C, which the theory already carries. Then

ℋ\_matter = ℋ\_spin ⊗ ℋ\_flavour ⊗ ℂ³\_C ,   ℋ\_Φ = H₅ ,

D\_μ ψ = (∂\_μ − i g₃ G^a\_μ T^a\_C − i g₂ W^b\_μ T^b\_L − i g₁ Y B\_μ) ψ ,

D\_μ H₅ = (∂\_μ − i g₂ W^b\_μ T̃^b\_L − i g₁ Y\_Φ B\_μ) H₅ ,

with no gluon term on H₅. No field is added. What is withdrawn is only the false claim that the five-dimensional Higgs irrep itself carries a colour triplet or a leptoquark block.

### 3.3 Acceptance tests, and what R0 costs

Table 3.1. Acceptance tests for R0. All six are ledger rows in block B.

| # | Test | Verdict |
|---|---|---|
| 1 | Every generator has a stated domain and codomain. | PASS |
| 2 | The covariant derivative transforms in the represented product group. | PASS |
| 3 | Yukawa terms contract colour indices to singlets. | PASS |
| 4 | The Z-bias field remains in the multiplicity-one D₃-trivial component. | PASS |
| 5 | No amplitude uses the withdrawn 2′ label. | PASS |
| 6 | The old S14 single-carrier SU(3) closure theorem is marked RETRACTED, not silently rewritten. | PASS |

**Cost, stated plainly.** ZS-S14 v2.0 Theorem S14.E claimed an action-level SU(3)\_C closure on a single carrier. That claim is **RETRACTED**. What survives is that the numerical output α\_s = **Q**/[(V+F)\_Y + 1] = 11/93 was never derived from the 2′ clause — it comes from the ZS-S1 spectral bridge and the Y-sector truncated-icosahedron counting — so no numerical corpus result moves.

**Non-claim NC-M61.1.** R0 is not claimed to be the unique repair. Any alternative carrier is admissible only as a declared new model, audited for free parameters. R0 is the minimal one, because it adds nothing. **v1.1 note:** "minimal" is a structural choice, and it is counted as choice C1 in §11.1a.

---

## §4. Theorem M61.2 — the graded relative unitary, and det V = +1

### 4.1 Setting

The one-event evolution is pointer-controlled, U = P₀ ⊗ U₀ + P₁ ⊗ U₁, the exact form of a Z\_path-QND dilation (ZS-M54 Theorem M54.22, commutant equivalence, cited at its exact strength). Write (F1) for the statement that the seam involution J\_S exchanges the pointer projectors and (F2) for [U, J\_S ⊗ J\_E] = 0, where J\_E is a unitary involution on the environment.

**Lemma M61.2a. [PROVEN].** (F1) ∧ (F2) hold if and only if U₁ = J\_E U₀ J\_E, with no residual phase freedom.

Proof. Conjugating U by J\_S ⊗ J\_E exchanges the two pointer blocks and conjugates each environment factor, giving P₀ ⊗ J\_E U₁ J\_E + P₁ ⊗ J\_E U₀ J\_E. Equality with U block by block gives J\_E U₁ J\_E = U₀. Because the pointer projectors are orthogonal, the two block equations are independent and admit no compensating scalar. ∎

### 4.2 The structure theorem

**Theorem M61.2 (Graded Relative-Unitary Structure). [PROVEN].** Let V = U₁†U₀ with U₁ = J\_E U₀ J\_E and write W = U₀. Then

**V = J\_E W† J\_E W ,**

and consequently

(i) J\_E V J\_E = V† ;
(ii) spec V is closed under complex conjugation, as a multiset with multiplicities ;
(iii) **det V = +1** ;
(iv) the eigenvalue −1 of V has even multiplicity ;
(v) if −1 ∉ spec V then V = exp(2iK) with K self-adjoint and seam-odd, J\_E K J\_E = −K.

Proof. (i) J\_E V J\_E = J\_E (J\_E W† J\_E W) J\_E = W† J\_E W J\_E, while V† = W† J\_E W J\_E. (ii) From (i), spec V† = spec V, and spec V† is the conjugate multiset. (iii) det V = det(J\_E) det(W†) det(J\_E) det(W) = det(J\_E)² = det(J\_E²) = det(I) = 1. (iv) Group the eigenvalues into conjugate pairs, each of product 1, together with the real eigenvalues ±1; the product of all is 1, so the number of −1's is even. (v) Take K = −(i/2) Log V on the principal branch; (i) gives J\_E Log V J\_E = Log V† = −Log V. ∎

**Why (iii) is not a restatement of (i).** Covariance alone gives det V = det V† = conj(det V), hence det V ∈ {+1, −1}. The minus sign is genuinely realisable by a merely covariant unitary: with J = the transposition of the first two basis vectors of ℂ³ and V = diag(e^{i}, e^{−i}, −1), one has J V J = V† exactly while det V = −1 (ledger row C5, residual 0, exact construction). It is the dilation form V = J W† J W that excludes it. This is the single algebraic fact on which the carrier-dimension theorem of §5 turns.

**Prior-art scoping, new in v1.1.** The proof of (iii) is three lines and its ingredients are classical. An element of the form g^{-θ}g with θ an involutive automorphism is a Cartan-embedding element of a compact symmetric space, and the statement that such elements land in the connected component on which the determinant is +1 is standard in that literature. What is claimed here is therefore not a new theorem of Lie theory but the **identification** of the Z-Spin graded relative unitary as an object of this form, together with the consequence in §5 that the corpus had not extracted. Status: `IMPORTED-PROVEN core + DERIVED identification`. Any external presentation must say so; gate F-M61.19 fires on presenting (iii) as a new general theorem.

Executed over 400 random triples (dimension 2 to 8, random unitary involution J\_E, random W): max |det V − 1| = **9.11 × 10⁻¹⁵** and max ‖J\_E V J\_E − V†‖ = **1.79 × 10⁻¹⁵** (rows C1–C2; v1.0 printed 9.1 × 10⁻¹⁵ and 8 × 10⁻¹⁵, the second of which did not match the artifact — see Appendix D.2).

### 4.3 The exact seam covariance requirement — (F2) is load-bearing and OPEN

Theorem M61.2 is conditional on (F2), which ZS-M56 F-M56.19 leaves open beyond quadratic order. **v1.1 promotes this from a remark to a front-page condition, because the audit is right that a title asserting closure cannot rest on an unexecuted change of variables.**

Two remarks fix its status. First, (F2) is a statement about the unitary, not about a perturbation series: it requires only that the represented seam involution commute with the full evolution, and for a group of order two this is a finite list of exact equalities on every tensor and boundary term. Second, the shortcut proposed in the successor seed — testing D₄ equivariance on the frozen register — is not available, because ZS-M57 proved that the pointer is not a D₄ subrepresentation of the **Q** = 11 register. Gate F-M61.3 fires on any use of D₄ as the physical pointer covariance proof.

The correct object is the seam ℤ₂ change of variables on the repaired action, measure, gauge fixing, Faddeev–Popov determinant, regulator and boundary counterterms. **This paper assumes (F2) and does not claim to have executed it.** If (F2) fails, the entire graded chain — ZS-M60 included — is inapplicable to the physical S14 process, and gate F-M61.16 records that consequence. Everything in §5 and §6 that does not use (F2) is flagged as such; §10 (Theorem M61.11) uses it nowhere and is unconditional.

---

## §5. Theorems M61.3–M61.4 — the arc obstruction and the carrier-dimension theorem

### 5.1 The state-independent arc obstruction

**Theorem M61.3 (Spectral Arc Obstruction). [PROVEN].** Let V be unitary and a = Tr(ρV) for some state ρ. If the support of the spectral measure of V lies in a closed arc of width w ≤ π with midpoint e^{ic}, then |a| ≥ Re(e^{−ic}a) = ∫ cos φ dμ(φ) ≥ cos(w/2). Consequently any V realising the frozen multiplier obeys

**w\_min(spec V) ≥ 2 arccos|λ| = 0.940241632013553311199 .**

Proof. Rotate so that the arc midpoint is 1; then every point of supp μ has cos φ ≥ cos(w/2), and the barycentre inherits the bound. Since supp μ ⊆ spec V for every state, the necessary condition is state-independent. ∎ Executed over 2000 random unitaries with w ≤ π: no violation, worst margin −1.48 × 10⁻⁶ (row D1).

**What must not be printed as exact.** For constant branch Hamiltonians V = e^{+iτB₁}e^{−iτB₀}, which is not e^{−iτ(B₀−B₁)} unless [B₀, B₁] = 0. The translation τ\_Z spread(B₀ − B₁) ≥ 2 arccos|λ| is therefore **DERIVED-CONDITIONAL** on a commutation or common-interaction-picture hypothesis, and gate F-M61.5 fires on its unconditional use. The robust replacement is Theorem M61.2(v): with K the shortest self-adjoint seam-odd logarithm, spread(2K) = w\_min(spec V) ≥ 2 arccos|λ| exactly.

**Scope, restated.** The arc obstruction is **necessary and not sufficient**: orientation is free, and §6 shows it is not binding for the S14 spectrum. It is a filter, not a bridge. (GUARD row D4.)

### 5.2 The carrier-dimension theorem

ZS-M60.23 minimises the total variation TV(μ, μ̌) over all probability measures on the circle with barycentre λ, and finds M\* = 0.763362818245964, attained by the two-atom measure with mass M\* at α = 2 arctan(Im λ/(1+Re λ)) = 2.017516299381013 and mass 1 − M\* at π. The minimisation is over **measures**. Theorem M61.2 constrains which measures a graded environment of a given dimension can **carry**.

**Theorem M61.4 (Carrier-Dimension Theorem). [PROVEN, conditional on (F2) for its physical application only].** Let d = dim ℋ\_E < ∞ and let V be a graded relative unitary. Write

**T₂ := |Im λ| / √(1 − (Re λ)²) = 0.835381287313629904738 .**

Then the minimal seam-ℤ₂ asymmetry compatible with a = λ is

T\_min(d) = T₂ for d ∈ {2, 3} ,   T\_min(d) = M\* for d ≥ 4 ,

and both values are attained. In particular M\*-saturation requires dim ℋ\_E ≥ 4, and the ZS-M60.12 minimal Choi-rank-two dilation is not the M\*-attaining one.

Proof. By Theorem M61.2 the spectrum is a conjugation-closed multiset of size d with product 1, so it consists of conjugate pairs {e^{±iφ\_k}} together with copies of +1 and an even number of copies of −1. Write p\_k, q\_k for the masses at e^{+iφ\_k}, e^{−iφ\_k} and m\_+, m\_− for the masses at ±1. Then TV(μ, μ̌) = Σ\_k |p\_k − q\_k| and

Re a = Σ\_k (p\_k + q\_k) cos φ\_k + m\_+ − m\_− ,  Im a = Σ\_k (p\_k − q\_k) sin φ\_k .

For d = 2 the only complex-admitting spectrum is a single conjugate pair, so p₁ + q₁ = 1 and Re a = cos φ₁ is forced to equal Re λ; then |p₁ − q₁| = |Im λ|/sin φ₁ = T₂ exactly, with no freedom. For d = 3, det V = +1 forbids a single −1, so the only complex-admitting spectrum is {e^{±iφ}, +1}; writing P = p + q, feasibility gives P = (1 − Re λ)/(1 − cos φ) and P ≤ 1 requires cos φ ≤ Re λ, i.e. φ ≥ arccos(Re λ). Since Re λ < 0 the angle arccos(Re λ) is obtuse, so sin φ is maximised at the endpoint φ = arccos(Re λ); TV = |Im λ|/sin φ is therefore minimised there, returning T₂ and driving the +1 mass to zero. For d ≥ 4 the configuration {e^{±iα}, −1, −1} has det = +1 and realises the ZS-M60.23 optimum. ∎

Table 5.1. Minimal seam-ℤ₂ asymmetry by carrier dimension. Independent linear program over 902 candidate angle sets per configuration; block F, residuals ≤ 2.2 × 10⁻¹⁶.

| dim ℋ\_E | T\_min | attaining spectrum | reading |
|---|---|---|---|
| 2 | 0.835381287314 | {e^{+iφ}, e^{−iφ}}, φ = 2.172948379550 | = T₂, forced |
| 3 | 0.835381287314 | {e^{±iφ}, +1} with zero mass at +1 | = T₂ |
| 4 | 0.763362818246 | {e^{±iα}, −1, −1}, α = 2.017516299381 | = M\* |
| 5 | 0.763362818246 | {e^{±iα}, −1, −1, +1} | = M\* |
| 6 | 0.763362818246 | {e^{±iα}, −1, −1, +1, +1} | = M\* |

**The counterfactual, which shows the theorem is load-bearing.** If det V = −1 were admissible, the spectrum {e^{±iα}, −1} would exist in dimension three and the linear program returns exactly M\* (row F7). The entire dimension gap T₂ − M\* = 0.072018469067666 is produced by Theorem M61.2(iii) and by nothing else.

Because T₂ > M\*, every ZS-M60 inequality remains true and none is reversed; ZS-M61 strengthens ZS-M60.23 on small carriers rather than contradicting it (GUARD row G9).

**External restatement, recommended.** For submission outside the corpus this theorem is stronger stated without Z-Spin vocabulary: *a finite-dimensional obstruction to the minimal asymmetry cost of a symmetry-constrained unitary dilation, arising from the determinant constraint that the dilation form imposes on the relative unitary.* The Z-Spin content is then the identification of the target barycentre.

---

## §6. Theorem M61.5 — real-part rigidity on a two-dimensional carrier

**Theorem M61.5 (Real-Part Rigidity). [PROVEN].** Let dim ℋ\_E = 2 and let V be a graded relative unitary with involution J\_E. Then V ∈ SU(2), V = cos φ · I + i sin φ · n̂·σ with n̂ orthogonal to the seam axis, and for every state ρ with Bloch vector r

**Re a = ½ Tr V = cos φ ,   Im a = sin φ (n̂·r) ,   T(ρ, J\_EρJ\_E) = |r\_⊥| ≥ |Im a| / sin φ .**

Proof. det V = 1 gives V ∈ SU(2). Choosing the seam axis as x, J\_E = σ\_x, and J\_E V J\_E = V† forces the x-component of n̂ to vanish. Then Tr(ρV) = cos φ + i sin φ (n̂·r) with n̂·r real. Conjugation by σ\_x flips the y and z Bloch components, so ρ − J\_EρJ\_E = r\_yσ\_y + r\_zσ\_z and T = ½‖ρ − J\_EρJ\_E‖₁ = |r\_⊥|; and |n̂·r| ≤ |r\_⊥| because n̂ lies in that transverse plane. ∎

Executed over 600 random branch Hamiltonians, durations and states: max |Re Tr(ρV) − ½ Tr V| = **8.88 × 10⁻¹⁶** (row E1; v1.0 printed 1.3 × 10⁻¹⁵ — Appendix D.2).

**Reading.** ZS-M60.22 separates Re a onto the ℤ₂-symmetric part of the state and Im a onto the ℤ₂-odd part. On a two-dimensional carrier the separation is sharper: **Re a is a property of the dynamics alone** and carries no state information whatever, while the entire state dependence sits in Im a. The consequence for the classification is immediate — Re λ alone determines the full spectrum of the S14-compatible relative unitary,

**spec V = { e^{+iφ}, e^{−iφ} } ,  φ = arccos(Re λ) = 2.172948379550106013483 ,  Tr V = 2 Re λ = −1.132834660570928805351 ,**

with no reference to the boundary state. The minimal containing arc is 2π − 2φ = 1.937288548079374 and clears the Theorem M61.3 gate 0.940241632013553 with margin 0.997046916065821 (row D3). The arc obstruction is therefore necessary and, here, not binding — exactly the scope Theorem M61.3 claims and no more.

**Honesty note added in v1.1.** This lemma is elementary SU(2)/Bloch geometry. It is load-bearing for §§7 and 9 and it is not a flagship theorem; presenting it as one would overstate the paper.

---

## §7. Theorems M61.6 and M61.7′ — vacuum-manifold rigidity and the conditional realisation

### 7.1 The vertex, and why the environment dimension cancels

The repaired ZS-S14 action couples the pointer to the Z-bias field Φ, whose D₃-trivial component has multiplicity one and is therefore unambiguous under R0. ZS-A3 §2 supplies the Z-bias potential V(ε) = (λ\_V/4)M\_P⁴(ε² − 1)² with vacua ε = ±1, and the seam ℤ₂ acts as ε ↦ −ε, so the Z-bias operator ε̂ is exactly seam-odd. The minimal pointer-conditioned interaction consistent with (F1), (F2) and this grading is

**H\_int = g · Z\_path ⊗ ε̂ ,  B₀ = +g ε̂ ,  B₁ = J\_E B₀ J\_E = −g ε̂ ,**

which is the vertex ZS-M57 §16.3 already identifies for Route S and which ZS-M60.29 uses when it observes that ΔB = B₀ − B₁ is ℤ₂-odd while B₀ + B₁ is ℤ₂-even. Here B₀ + B₁ = 0, so the vertex is purely odd. Writing c = τg for the accumulated branch phase,

V = e^{+iτB₁} e^{−iτB₀} = e^{−i c ε̂} e^{−i c ε̂} = e^{−2 i c ε̂} .

**"Minimal" is a choice, counted.** The step from "the action contains a seam-odd Z-bias coupling" to "the vertex is exactly g Z\_path ⊗ ε̂ and nothing else" is a minimality selection, not a derivation from S\_S14. It is choice C2 in §11.1a and gate F-M61.20 fires on presenting it as derived.

**Theorem M61.6 (Vacuum-Manifold Rigidity). [DERIVED-CONDITIONAL on (H-VAC-BDY)].** Let (H-VAC-BDY) be the statement that the ZS-S14 **boundary-process** state is supported on the ZS-A3 vacuum manifold, ε̂² = I on supp ρ\_E. Then, in every environment Hilbert space of every dimension, finite or infinite,

**a\_S14(c) = Tr(ρ\_E e^{−2icε̂}) = cos 2c − i sin 2c · ⟨ε⟩ ,  ⟨ε⟩ = Tr(ρ\_E ε̂) ,**

and T(ρ\_E, J\_Eρ\_EJ\_E) ≥ |⟨ε⟩|, with equality attained on the two-dimensional realisation.

Proof. On the vacuum manifold ε̂² = I, so cos(2cε̂) = cos 2c · I and sin(2cε̂) = sin 2c · ε̂ identically; taking traces against ρ\_E gives the formula. The induced spectral measure of V is the two-atom law with masses p\_± = (1 ± ⟨ε⟩)/2 at e^{∓2ic}, and its conjugate reflection exchanges the two masses, so TV(μ, μ̌) = |p\_+ − p\_−| = |⟨ε⟩|; trace-distance data processing gives T ≥ TV. ∎

Executed over **320** draws sweeping the environment dimension over {2, 3, 4, 5, 7, 9, 12, 20} with random splittings of ℋ\_E into the two ε-eigenspaces and random states inside the manifold: max residual 1.73 × 10⁻¹⁵ (row H3; v1.0 printed "480 draws" — Appendix D.2).

**What this achieves, and what it does not.** The whole of §5 asked what dimension the graded carrier must have. Theorem M61.6 makes the question moot *for the vacuum-supported ansatz*: the boundary Hilbert space cancels exactly, and only the ε-marginal survives into the multiplier. (H-DOUBLET-SUPPORT), which ZS-M60 could not remove, is therefore **not needed**. It is replaced by (H-VAC-BDY), which §7.3 shows is **weaker in form and not weaker in evidential burden**. Gate F-M61.7 stands: the multiplicity qubit of End\_{D₃}(H₅) is not identified with the ZS-A3 doublet anywhere in this paper.

### 7.2 Theorem M61.7′ — the conditional realisation, and its exact evidential status

**Theorem M61.7′ (Vacuum-Supported Realisation / Reparametrisation). [DERIVED-CONDITIONAL on (F1), (F2), (H-VAC-BDY); evidential status IDENTIFIABILITY].** Matching a\_S14 = λ is two real equations. Under (H-VAC-BDY) the boundary law has exactly one real shape datum, ⟨ε⟩, and the dynamics exactly one, c. The system is exactly determined and the principal-branch solution is unique:

**c\* = ½ arccos(Re λ) = 1.086474189775053006742 ,**
**⟨ε⟩\* = − Im λ / √(1 − (Re λ)²) = − 0.835381287313629904738 = −T₂ .**

The reconstructed multiplier is cos 2c\* − i sin 2c\* ⟨ε⟩\* = λ with residual **2.7 × 10⁻⁵¹** at fifty digits (row H5; v1.0 printed 1.2 × 10⁻⁴⁶). The general solution set is the branch torsor c ↦ ±c\* + kπ, ⟨ε⟩ ↦ ∓⟨ε⟩\*, k ∈ ℤ, which is the ZS-M59 branch torsor reappearing at generator level; the principal branch is selected by minimality of the accumulated phase, which is choice C4 of §11.1a.

**§7.2a The internal conflict, resolved in favour of ZS-M57. [PROVEN as an algebraic identity].**

ZS-M57 v1.8 Theorem M57.C.2 proves that

λ ⟷ (φ, s) ,  φ = arccos(Re λ) ,  |s| = |Im λ| / √(1 − (Re λ)²)

is a bijection from the punctured disc off the real axis onto (0, π) × (−1, 1), and ZS-M57 §11.3 draws the conclusion in its own words: the construction "TRANSPORTS the multiplier into collision coordinates rather than deriving it", the ZS-M56.7 trap "fires on schedule", two real parameters against two real constraints leave zero residual degrees of freedom, "so there is no possibility of a non-trivial check and the exact agreement … is guaranteed a priori rather than discovered".

Under the substitution

**φ = 2c ,  s = ⟨ε⟩**

Theorem M61.7′ **is** Theorem M57.C.2. The identity is exact, not approximate: M57 §11.2 gives γ = cos φ − i s sin φ with s\* = −Im λ/sin φ\*, and M61 gives a = cos 2c − i sin 2c ⟨ε⟩ with ⟨ε⟩\* = −Im λ/√(1 − Re²λ) = −Im λ/sin φ. The two right-hand sides are the same function of the same two reals.

*A convention note, because it matters for citation.* ZS-M57 v1.8 carries **two** sign conventions for s: its Theorem M57.C.2 line prints the inverse as λ = cos φ + i s sin φ with s = +Im λ/√(1−Re²λ), while its §11.2 construction and its Appendix C correction both use λ = cos φ − i s sin φ with s = −Im λ/sin φ. Under the first the substitution reads s = −⟨ε⟩; under the second, s = +⟨ε⟩. The equivalence to M61.7′ holds either way and the conclusion is unaffected, but the residual inconsistency inside ZS-M57 v1.8 is recorded here (**debt D-M57-SIGN**) so that neither paper is cited with the wrong pairing.

**Consequences, stated so that no successor can mistake them.**

1. Theorem M61.7′ establishes **identifiability**: given λ, the vacuum-supported ansatz has exactly one minimal-phase realisation. That is a real and useful fact about the model's parameter geometry.
2. Theorem M61.7′ establishes **nothing** about the derivation of λ from S\_S14. The exact agreement to 2.7 × 10⁻⁵¹ is guaranteed a priori by the bijection and is **not** evidence.
3. The v1.0 name "Zero-Parameter Selection and the Terminal Solution" is **RETRACTED**. So is the v1.0 sentence "The zero-free-parameter requirement therefore selects the two-atom vacuum law rather than assuming it." The parameter count *excludes broader laws from being zero-parameter*; it does not *select* the two-atom law from the action. The corrected statement is: **among boundary laws with at most one real shape datum, the two-valued vacuum law is the one the ZS-A3 potential supplies; laws with more data are excluded by the zero-additional-fitted-parameter requirement rather than by the action.**
4. **NC-M61.10 (new).** ZS-M61 does not claim that S\_S14 predicts λ, nor that the agreement of §7.2 is a test of the i-tetration identification of the multiplier.
5. **Gate F-M61.17 (new).** Fires if any paper cites §7.2 as a derivation, prediction or closure of λ, or reports its residual as evidence. Consequence: the citing statement is void.

**What would make it evidential**, stated as the paper's single forward deliverable:

> **D-M61-FWD (Forward-Selection Deliverable).** Construct, from the repaired S\_S14 alone and with λ, z\*, μ, χ and T₂ excluded from the construction, (a) the seam-odd Z-bias vertex including its coupling g, (b) the boundary-process state and hence ⟨ε⟩, and (c) the event step and hence c = τg; then compare a = cos 2c − i sin 2c ⟨ε⟩ with λ **once**. Passing this is closure of the bridge. Failing it rejects the i-tetration identification of the S14 multiplier. Either outcome is publishable, and neither is available from anything in this paper.

D-M61-FWD is the same object as ZS-M54 F-M54-16′ and ZS-M57 §11.5(i)–(ii), now posed in the coordinates (c, ⟨ε⟩) rather than (φ, s) or Λ. **That restatement is this paper's actual contribution to the bridge**, and it is a contribution of shape, not of evidence.

### 7.2b The quantitative alternative, retained

The alternative is worth printing because it shows the parameter count is not rhetorical. With Gaussian fluctuations of width s about the vacua, the multiplier acquires the factor e^{−2c²s²}: at s = 0.05, 0.10, 0.20 the modulus is damped by 0.994115, 0.976668, 0.909888 respectively, and ⟨ε⟩ must be refitted at each s. That one-parameter family of refits is what a zero-additional-fitted-parameter theory may not have — **and it is also what a theory that has not derived (c, ⟨ε⟩) cannot exclude on physical grounds.** Gate F-M61.9 stands as a discipline on the model's parameter budget; it is not an argument that the boundary law is Gaussian-free.

### 7.3 (H-VAC), split — and the material conflict with ZS-M57 §16.3

**v1.1 replaces the single hypothesis (H-VAC) with two, because v1.0 justified the one it needs by citing evidence for the other.**

- **(H-VAC-BULK). [corpus-recorded; ZS-A3 §2, ZS-M57 §16.3].** The Z-bias potential has vacua ε = ±1 and the seam ℤ₂ is spontaneously broken in the bulk.
- **(H-VAC-BDY). [HYPOTHESIS; the hypothesis this paper actually needs].** The state of the ZS-S14 **boundary process** is supported on ε² = 1, so that ε̂² = I on supp ρ\_E.

**(H-VAC-BULK) does not entail (H-VAC-BDY),** and the corpus text v1.0 cited for support in fact pushes the other way. ZS-M57 §16.3 records: the bulk vacuum is at ε = ±1 and the ℤ₂ is spontaneously broken there; **consequently the fluctuation δε = ε − 1 has no definite ℤ₂ parity**, because the symmetry maps one vacuum to the other; and therefore the stochastic physical mediation route survives only by **localising at the Z-anchor, where ε(r\_H) = 0 and the ℤ₂ is restored**. The physically identified mediation locus in the corpus is thus the ε = 0 anchor, not the ε = ±1 vacuum.

Whether this is a direct contradiction depends on whether ZS-M57's Route S object and ZS-M61's boundary process are the same object. They may not be. **Status: [OPEN] material conflict, registered as debt D-M61-VAC.** It must be resolved before (H-VAC-BDY) is used as support for any closure claim. Consequences of the split:

- (H-VAC-BDY) is downgraded from **HYPOTHESIS-strong** (v1.0) to **HYPOTHESIS** with a recorded conflict.
- The v1.0 sentence "it is replaced by the weaker and corpus-supplied (H-VAC), which ZS-M57 §16.3 already records as a fact about the bulk" is **RETRACTED**: the bulk fact is not the boundary fact, and the substitution of one for the other was the v1.0 error.
- Gate F-M61.15 is sharpened: it now fires on falsification of **(H-VAC-BDY)**, and separately on any citation of (H-VAC-BULK) as evidence for (H-VAC-BDY) (new gate F-M61.21).
- If (H-VAC-BDY) fails, §§7–8 fall to CORPUS-UNDERDETERMINATION and only §§4–6, §9 (generic), §10 and the T₂ bound survive. T₂ itself survives, because Theorem M61.4 does not use (H-VAC-BDY) — **this is the reason the paper retains substantial value even under the worst case.**

**Status of this conflict in v1.2: DISSOLVED, not decided.** Theorem M61.13 (§19) shows the multiplier is the characteristic function of the ε-marginal for *any* support, so ε = 0 and ε = ±1 are the two ends of one interval rather than competing hypotheses; Theorem M61.14 (§20) replaces the dichotomy by a phase price c ≥ c\*/ε_max. Debt D-M61-VAC is closed. What remains of (H-VAC-BDY) is the *equality case* of Theorem M61.14, and it is no longer an independent structural choice.

A reader who distrusts this paper should attack (F2) — now reduced to three finite items by Reduction R1 (§25) — and then the two forward gates of §22. Attacking §7.2 is unnecessary: this version already reduced it to identifiability. Attacking (H-VAC-BDY) as such is now also unnecessary: §20 shows that relaxing it costs phase rather than breaking anything.

### 7.4 The non-perturbative threshold

**Theorem M61.8 (Non-Perturbative Threshold). [PROVEN].** Let B₀ be an arbitrary branch Hamiltonian on a two-dimensional graded carrier, with seam-odd fraction v ∈ [0, 1] of its traceless part and accumulated phase c = τ‖b‖. Then Re a = 1 − 2v² sin²c, so realising Re a = Re λ requires

**v · sin c = sin(½ arccos Re λ) = 0.884990771218961469989 ,  hence  c ≥ ½ arccos(Re λ) = 1.086474189775053 .**

Proof. Write B₀ = βσ\_x + b\_⊥·σ with b\_⊥ in the plane transverse to the seam axis. A direct SU(2) computation gives ½ Tr V = cos²c + sin²c(u² − v²) = 1 − 2v²sin²c with u² + v² = 1, and Theorem M61.5 identifies this with Re a. Since v ≤ 1, sin c ≥ sin(φ/2), and the smallest positive c is φ/2. ∎

**Consequence, stated as a closure.** The accumulated branch phase of any graded-doublet realisation is bounded below by a universal constant of order one. No first-order, weak-coupling or short-slab truncation can produce λ: at c = 0.05, 0.2, 0.5 and 1.0 the maximum attainable |Re a − 1| is 0.004996, 0.078939, 0.459698 and 1.416147 against the required 1.566417330285464 (row H8). This retires the seed's Route E and, with it, the requirement for a certified second-order remainder R₂(s): the inequality it was to protect is inapplicable, not merely uncertified.

**Scope, tightened in v1.1.** The theorem is unconditional *within the graded two-dimensional carrier class*, which is where Theorem M61.5 applies. It is not a statement about every conceivable S14 boundary process. Status: **CLOSED-NEGATIVE within the graded doublet class.** Gate F-M61.6 fires on any presentation of a perturbative S14 vertex as reproducing λ; new gate F-M61.22 fires on presenting M61.8 as a class-free no-go.

**A note on the ZS-S14 perturbative tag.** ZS-S14 Theorem S14.A is PROVEN-PERTURBATIVE, and NC-S14.2 already declares non-perturbative effects outside v1.0 scope. Theorem M61.8 does not contradict either; it locates the boundary event in the excluded regime and thereby explains why thirty-one versions of the S-line and eight of ZS-M59 could not reach λ from an expansion.

---

## §8. Theorem M61.9 — the conditional boundary state, and the sharpened ceilings

### 8.1 The state

**Theorem M61.9 (Boundary State). [DERIVED-CONDITIONAL on (F1), (F2), (H-VAC-BDY); inherits the IDENTIFIABILITY caveat of §7.2].** The ε-marginal of the ZS-S14 boundary state consistent with a = λ is the two-atom law

**p(ε = −σ) = (1 + T₂)/2 = 0.917690643656814952369 ,  p(ε = +σ) = (1 − T₂)/2 = 0.082309356343185047631 ,**

with σ = sgn(Im λ) fixing which vacuum is selected. Among all admissible states the maximum-entropy representative carries no coherence between the two vacua, and its invariants are:

Table 8.1. The conditional ZS-S14 boundary state and its invariants, compared with the ZS-M60 ceilings. Every ZS-M61 entry is tighter; none reverses an inequality.

| Quantity | ZS-M61 (this paper) | ZS-M60 v1.5 | Status |
|---|---|---|---|
| seam-ℤ₂ asymmetry T | = 0.835381287313630 (attained) | ≥ 0.763362818245964 | DERIVED-CONDITIONAL |
| Z-bias mean \|⟨ε⟩\| | = 0.835381287313630 | not computed | DERIVED-CONDITIONAL + IDENTIFIABILITY |
| Uhlmann fidelity to the seam image | ≤ 0.549670905912094 | ≤ 0.645969974317367 | DERIVED |
| seam overlap Tr(ρ JρJ) | ≤ 0.302138104806223 | ≤ 0.417277207719580 | DERIVED |
| purity Tr ρ² | ≥ 0.848930947596889 | ≥ 0.791361396140210 | DERIVED |
| linear entropy | ≤ 0.151069052403111 | ≤ 0.208638603859790 | DERIVED |
| von Neumann entropy (nats) | ≤ 0.284373704659211 | ≤ 0.363561460568423 | DERIVED |
| entropy as a fraction of ln 2 | ≤ 0.410264533471067 | ≤ 0.524508316220412 | DERIVED |
| decoherence budget (e-folds) | 0.179867026842395 | 0.270021845324850 | DERIVED |
| event count n\_max = budget/μ | **1.566313529988409** | 2.351397458164148 | DERIVED |

**Which rows depend on which hypothesis.** The five ceiling rows follow from T₂ alone and therefore from Theorem M61.4, which does **not** use (H-VAC-BDY): they survive the failure of that hypothesis. The two rows marked with the identifiability caveat are the ones that assert a *value* rather than a bound and they do not survive it. v1.0 did not make this separation and it is the difference between a paper that loses everything if (H-VAC-BDY) falls and one that loses two rows.

The seam-overlap ceiling has a closed form worth recording:

**Tr(ρ\_E J\_Eρ\_E J\_E) ≤ 1 − T₂² = (1 − |λ|²) / (1 − (Re λ)²) = 0.302138104806223 ,**

the numerator 1 − |λ|² = 0.205203562037278 being exactly the ZS-U12 per-transit leak to the ℤ₂-odd channel. Verified to 10⁻⁴⁰ (row G7). It is recorded as a structural identity, not as a new prediction, and gate F-M61.12 fires on any presentation of it as an independent confirmation of ZS-U12.

### 8.2 Two downstream statements that change

**The event count.** ZS-M60.32 gives the phase budget ln(1/M\*) = 0.270021845324850 e-folds and, under (H-RECIP), n\_max = 2.351397458164148, recording ⌊n\_max⌋ = 2 = dim **Z** as an OBSERVATION behind gates F-M60.44 and F-M60.45. With the sharpened floor the budget is ln(1/T₂) = 0.179867026842395 and n\_max = 1.566313529988409: |λ|¹ = 0.891513565776047 still clears T₂ but |λ|² = 0.794796437962722 does not. **At most one complete Z-cycle can carry the phase.** The coincidence ⌊n\_max⌋ = 2 = dim **Z** is **RETIRED**, and its retirement is evidence that the corpus's own flagging of it as numerology was correct. No result depended on it. *This retirement is unaffected by the v1.1 status changes, because it rests on T₂ alone.*

**The phase-dead core.** ZS-M60.33 places the phase-capable shell of a Z-anchor at ε\*/σ = √(−ln(1 − M\*²)) = 0.934882084184541 for a Gaussian field state, or at (r\* − r\_H)/L\_⊥ = arctanh M\* = 1.004224933849392 for a tanh kink profile. Both move outward:

ε\*/σ = √(−ln(1 − T₂²)) = 1.094016026141529 ,  (r\* − r\_H)/L\_⊥ = arctanh T₂ = **1.205687778651241** .

Both remain **DERIVED-CONDITIONAL** on the profile and the Bloch identification, and the near-equality of the second to unity is refused as meaningless in §11.2. The conversion L\_⊥ = 1/(2**A**M\_P) requires λ\_vac = 2**A**² for the same field normalisation and is not asserted here.

**An irony worth recording, new in v1.1.** The kink-core statement places the phase-capable shell at a *nonzero* distance from the anchor, while §7.3's conflict concerns whether the boundary-process state sits at the anchor (ε = 0) or in the bulk (ε = ±1). These two facts are about the same radial geometry and the corpus has not reconciled them. Resolving D-M61-VAC will probably require doing so.

---

## §9. Theorem M61.10′ — the physical anchor divisor is generically empty

ZS-M59 deliverable (3) asked for the physical anchor divisor. ZS-M60.6 closed it negatively on the phase-covariant class and left the general case open behind the colour repair. With the repair in hand the general case closes **for families in general position**, by a codimension count.

**Theorem M61.10′ (Generic Empty-Divisor Theorem). [DERIVED-CONDITIONAL on (H-GP)].** Let θ ↦ V(θ, s) be a continuous family of graded relative unitaries on a two-dimensional carrier over the holonomy circle ℤ\_θ, and let a(θ, s) = Tr(ρ\_E(s) V(θ, s)). Then a(θ₀, s₀) = 0 requires simultaneously

**Tr V(θ₀, s₀) = 0  (equivalently V² = −I)   and   r(s₀) ⊥ n̂(θ₀, s₀) ,**

two independent real conditions on a one-parameter base. The zero set is therefore of codimension two in a one-dimensional family. **Under (H-GP) — that the family is in general position with respect to that codimension-two locus — the zero set is empty and D\_phys = 0.**

Proof. By Theorem M61.5, Re a = ½ Tr V and Im a = sin φ (n̂·r). Vanishing of a forces both, and the first gives φ = π/2, i.e. spec V = {+i, −i} and V² = −I. The two conditions involve independent components of the data, and each is one real equation. ∎ Executed over 8000 random graded doublet families: no zero found, minimum |a| = **2.31 × 10⁻³** (row I1; v1.0 printed 1.8 × 10⁻³).

**The quantifier, corrected. [This is the v1.1 change.]** v1.0 wrote "the zero set … is empty for every family in general position; the ZS-M59 transversality hypothesis has an empty domain and D\_phys = 0", and then carried D\_phys = 0 into Table 14.1 as CLOSED-NEGATIVE without qualification. The inference

codim 2 > dim(base) = 1 ⟹ generic families miss the locus

is correct. The inference

⟹ **every** family, including the specific S14 family, misses the locus

is **not**. A constrained curve can be non-generic and can intersect a codimension-two locus; genericity is a statement about almost all families, not all. The 8000-sample witness supports genericity and is not a proof of universality — by the ledger rule that a supremum or infimum claim may not be certified by a grid sample, and by the audit axiom that quantifier errors are not cured by sample size.

Accordingly:

- **Status:** CLOSED-NEGATIVE-**GENERIC**, downgraded from CLOSED-NEGATIVE.
- **ZS-M59 deliverable (3):** partially discharged. The general-position case is closed; the actual-family case is OPEN.
- **Gate F-M61.18 (new).** Fires if D\_phys = 0 is asserted for the actual repaired-S14 family without an explicit transversality or non-intersection certificate for that family. Consequence: the assertion reverts to CLOSED-NEGATIVE-GENERIC.
- **Promotion path.** Exhibit the actual S14 holonomy family (θ, s) ↦ (V, ρ\_E) and show either that Tr V ≠ 0 identically on it — which the vacuum-supported form V = exp(−2icε̂) with c fixed does satisfy, since Tr V = 2 cos 2c is constant — or that r ∦ ... fails nowhere. **Note that under (H-VAC-BDY) and a fixed c the first branch is immediate**, which means the promotion is cheap *conditional on the same hypothesis §7.3 has just weakened. That dependency is why the two cannot be quoted as independent successes.*

**Reading, and its status as a result.** ZS-M59 §18 declared in advance that D = 0 is a complete result — a no-go for intrinsic branch selection along the S14 path — and not a failure. That verdict stands at the generic level. It also disposes of the sector-polynomial programme for this process at that level: the ZS-M60.9 argument-principle calculus and the ZS-M60.10 interval bounds remain PROVEN as mathematics, and the ZS-M60.15 prediction that a **Q**-valued branch field would cost ‖D‖ = **Q** − 1 = 10 remains HYPOTHESIS-weak. Gate F-M61.11 fires on any theta weight or anchor point selected after seeing roots.

**Superseded in v1.2 by Theorem M61.16 (§23).** On the λ-compatible class — every family for which Re a = Re λ, which includes the actual vacuum-supported family — the result is unconditional: |a| ≥ |Re λ| = 0.566417330285464 > 0 for every θ, so D_phys = 0 with no general-position hypothesis. (H-GP) is needed only for families that are not λ-compatible, where the question is physically empty. §9's counterexample family is explained rather than contradicted: it sits at c = π/4, below the universal phase floor. ZS-M59 deliverable (3) is thereby fully discharged for the physical process, and the 8000-draw witness is retired as a research instrument (gate F-M61.31).

**Non-claim NC-M61.2.** ZS-M61 does not claim that no Z-Spin process anywhere carries a nonempty anchor divisor. It claims that no λ-compatible graded family does.

---

## §10. Theorem M61.11 — the general minimal-asymmetry function M\*(a)

The result ZS-M60.23 proves at the single point a = λ is an instance of a general theorem which is legible, and useful, entirely outside the Z-Spin corpus. **It uses neither (F2) nor (H-VAC-BDY) and is unaffected by every status change in this revision.**

**Theorem M61.11 (General Minimal Asymmetry). [PROVEN].** For a target a = x + iy in the closed unit disc, let μ range over probability measures on the unit circle with ∫ z dμ = a, and let μ̌ denote the conjugate reflection. Then

M\*(a) = |y| ,  if |x| + |y| ≤ 1 ,

M\*(a) = min\_{ s ∈ {−1, +1}, 1 − sx > 0 } |1 − sa|² / (2(1 − sx)) ,  if |x| + |y| > 1 .

Proof sketch. Decompose μ into its even and odd parts under φ ↦ −φ; then TV(μ, μ̌) is the total mass of the odd part, the even part must supply x and the odd part y. Inside the diamond |x| + |y| ≤ 1 the two demands are independently satisfiable and the odd mass need only equal |y|. Outside it the even part cannot supply x without borrowing mass, and the linear program is solved by two atoms — one at ±α with tan(α/2) = y/(1 + sx) and one at the fixed point s = ±1 — at which the mirror atom acquires exactly zero mass. Substitution gives the stated rational form; the primal/dual certificate is in Appendix B. ∎

Table 10.1. Theorem M61.11 against an independent 1800-atom linear program, run without reference to the closed form. **Residuals corrected in v1.1 to the values the shipped artifact emits.**

| target a | closed form | \|closed form − LP\| (artifact) | v1.0 printed | active branch |
|---|---|---|---|---|
| −0.566417 + 0.688453 i | 0.763362818246 | 1.92 × 10⁻⁷ | 9.4 × 10⁻⁸ | outer, s = −1 |
| +0.300 + 0.300 i | 0.300000000000 | 0.0 | 5.6 × 10⁻¹⁷ | inner diamond |
| +0.500 + 0.600 i | 0.610000000000 | 2.38 × 10⁻⁷ | 1.1 × 10⁻⁷ | outer, s = +1 |
| −0.900 + 0.200 i | 0.250000000000 | 8.67 × 10⁻⁷ | 2.0 × 10⁻⁷ | outer, s = −1 |
| +0.950 + 0.100 i | 0.125000000000 | 4.33 × 10⁻⁷ | 1.0 × 10⁻⁷ | outer, s = +1 |
| −0.200 − 0.700 i | 0.700000000000 | 1.11 × 10⁻¹⁶ | 0.0 | inner diamond |
| +0.000 + 0.800 i | 0.800000000000 | 0.0 | 0.0 | inner diamond |

All seven agree within the declared 3 × 10⁻⁶ LP discretisation tolerance; the discrepancies are between the v1.0 manuscript and its own artifact, not between the theorem and the LP.

**Scope, stated against a temptation.** The theorem must be stated for ℤ₂-covariant QND dilations and not as a D₄ theorem. Guard row J8 exists to catch misuse of the outer rational formula inside the diamond, where it returns the wrong number.

**External significance, and prior-art status — corrected in v1.1.** M\*(a) quantifies the minimum asymmetry resource an environment state must supply to produce a prescribed complex dephasing multiplier under symmetric dynamics. It interfaces directly with the Marvian–Spekkens resource theory of asymmetry and with standard controlled-unitary dilations, and it needs no Z-Spin input. **Prior-art status: NOT\_FOUND.** A targeted search did not locate this exact piecewise closed form. Adjacent literature is real and must be cited: asymmetry as a resource is an established theory; trace-norm asymmetry measures are studied; and the reduction of extremal measures under moment constraints to finitely many atoms is standard moment-problem theory. **NOT\_FOUND is not NEW**, and gate F-M61.23 fires on presenting Theorem M61.11 as established novelty rather than as a result whose novelty search returned nothing. A full prior-art search is routed to the deep-exploration engine as deliverable D-M61-PRIOR and is **not** performed in this paper.

Subject to that, this is the strongest stand-alone mathematical result here, and — a point the audit makes and this version accepts — **the paper's most defensible external contribution is a pure mathematics theorem, not the physical bridge its v1.0 title advertised.**

---

## §11. Parameter audit and anti-numerology

### 11.1 Provenance of every scalar

Table 11.1. Provenance ledger. A boundary condition is not zero-parameter merely because it is written geometrically; it must be uniquely selected by the frozen problem.

| Scalar | Provenance label | Selected by |
|---|---|---|
| λ, \|λ\|, χ, μ | FROZEN INPUT | ZS-M1 i-tetration fixed point; λ = Log z\* |
| M\*, ρ\_λ(π) | DERIVED OUTPUT | ZS-M60.23 linear program, re-derived here |
| φ = arccos(Re λ) | DERIVED OUTPUT | Theorem M61.5; state-independent |
| T₂ | DERIVED OUTPUT | Theorem M61.4; closed form in λ alone; **independent of (H-VAC-BDY)** |
| c\* | **SOLVED FROM λ** | Theorem M61.7′; solves Re a = Re λ. IDENTIFIABILITY, not derivation |
| ⟨ε⟩\* | **SOLVED FROM λ** | Theorem M61.7′; solves Im a = Im λ. IDENTIFIABILITY, not derivation |
| ε = ±1 atom locations | BOUNDARY CONDITION | ZS-A3 §2 potential minima; not adjustable **in the bulk**; boundary support is (H-VAC-BDY) |
| J\_E = seam involution | REPRESENTATION NORMALISATION | ZS-M54 M54.8a; ε ↦ −ε |
| **A** = 35/437 | NOT USED | enters only the §11.3 conditional diagnostic |
| **Q** = 11, dim **Z** = 2 | NOT USED IN DERIVATIONS | cited only through named corpus hypotheses |

The v1.0 label for c\* and ⟨ε⟩\* was "DERIVED OUTPUT". That was the error §7.2 corrects: they are outputs of a *solve against the target*, and the provenance label must say so.

### 11.1a The six declared structural choices — new in v1.1

"Zero fitted numerical parameters" is true and is not the same as "zero choices". The choices are enumerated here in one place so that they cannot be distributed across sections and lost.

| # | Choice | Where | Alternative admissible? | Cost if changed |
|---|---|---|---|---|
| C1 | R0 as the **minimal** colour repair | §3.2 | Yes, as a declared new model | Type-level only; no numerical output moves |
| C2 | The **minimal** seam-odd pointer-conditioned vertex H\_int = g Z\_path ⊗ ε̂ | §7.1 | Yes (multi-term vertices) | V is no longer exp(−2icε̂); §7 restarts |
| C3 | **(H-VAC-BDY)**: boundary-process support on ε² = 1 | §7.3 | Yes; anchor localisation is admissible and **priced** (§20.3) | **DEMOTED in v1.2** from an independent hypothesis to the equality case of Theorem M61.14: (H-VAC-BDY) ⟺ c = c\* ⟺ minimal phase. §§7–8 still fall to CORPUS-UNDERDETERMINATION if it fails, but §§19–21 and every T₂-based ceiling survive |
| C4 | ~~**Principal branch** k = 0 by minimality of the accumulated phase~~ | §7.2 | — | **DELETED in v1.2.** Theorem M61.14 proves c ≥ c\*/ε_max, so minimal phase is not a choice but the extremum, and the branch selection is a theorem. Four structural choices remain. |
| C5 | **(F2)**: exact seam ℤ₂ covariance of the repaired action to all orders | §4.3 | It is an assumption, not a choice, but it is unexecuted | The whole graded chain, ZS-M60 included, is inapplicable |
| C6 | **(H-GP)**: general position of the actual S14 holonomy family | §9 | Yes | D\_phys = 0 reverts to generic-only |

Correct external phrasing, to be used verbatim: **"zero additional fitted numerical parameters, conditional on the declared structural model (C1–C3, C5–C6)."** v1.2 deletes C4 and demotes C3 to the equality case of a theorem, so the structural budget is **four** choices, not six. Gate F-M61.24 fires on the unqualified phrase "zero free parameters" anywhere in a ZS-M61 abstract, title, figure caption or conclusion.

### 11.2 Anti-numerology scan — figures corrected to the executed artifact

The scan was specified before the constants were compared with anything. Its atom set is {**A**, **Q**, dim **Z**, X, Y, π, e, |λ|, Re λ, Im λ, χ, μ, M\*, √5, ln 2, 1, 2, 3, 4, 5, 6, 11, 32, 93} — 24 atoms — and its formula set is all binary quotients, products, sums, differences, roots and radical quotients. **The executed family contains 3362 finite admissible expressions, not the 2652 printed in v1.0.** Tolerance 10⁻³.

Table 11.2. Anti-numerology scan, as executed. All three targets pass at the 5% threshold.

| Target | Value | Hits / formulas | p | v1.0 printed | Verdict |
|---|---|---|---|---|---|
| T₂ | 0.835381287313630 | 1 / 3362 | 2.97 × 10⁻⁴ | 1 / 2652, p = 0.00038 | PASS |
| c\* | 1.086474189775053 | 0 / 3362 | 0 | 0 / 2652, p = 0.00000 | PASS |
| p(selected) | 0.917690643656815 | **1 / 3362** | 2.97 × 10⁻⁴ | **0 / 2652, p = 0.00000** | PASS |

The third row is the substantive correction: v1.0 reported zero hits for p(selected) where its own artifact reports one. The verdict does not change — one hit in 3362 at tolerance 10⁻³ is far below the pre-registered 5% threshold — but an anti-numerology control that misreports its own hit count is exactly the kind of row that must be corrected rather than left, because the control's whole value is that its numbers are the executed ones.

**The single near-miss, recorded and refused.** √(**A**/μ) = 0.835135366043200 lies 2.46 × 10⁻⁴ from T₂. It is **not** an identity, it plays no role in any derivation, and it is printed so that it cannot be discovered later and presented as a finding. T₂ is defined by |Im λ|/√(1 − (Re λ)²) and by nothing else. Gate F-M61.10 fires on any use of the near-miss.

**A stronger control than the scan.** T₂ is not a universal constant that could match anything: sweeping the argument of λ around the circle of the same modulus, T₂(λ′) ranges over [0.0015, 0.8915]. It is a derived function of the frozen multiplier, not a fitted number (row K4). The same applies to c\* = ½ arccos(Re λ) by construction — **which is also, per §7.2, exactly why c\* carries no evidential content: being a function of λ is what makes it both non-numerological and non-predictive.**

**Refusals carried forward.** No meaning is attached to arctanh T₂ ≈ 1.206, to ⌊n\_max⌋, to the proximity of any printed constant to an integer or simple rational, or to τ\* ≈ 4π. The v1.0 seed diagnostics ē/σ = R√(**A**/**Q**)/√2, τ\_min = 13.238, σ² = λ\_V and r\*/ℓ\_P = 6.269 are not used.

### 11.3 One conditional diagnostic, clearly labelled

If *and only if* the Z-bias vertex coupling is identified with g = √(**A**/**Q**) = 0.085329059944311 — an identification the successor seed explicitly marked unsafe and which this paper does not adopt — then the required slab duration is τ\* = c\*/g = **12.732757052335130** in the corresponding units. Printed as a **CONDITIONAL DIAGNOSTIC** only. It supersedes the v1.0 figure τ\_min = 13.238 in the sense of replacing an unproved inequality by an equally unproved equality, which is not progress and is not counted. Gate F-M61.14 fires on any use of τ\* as evidence. *(The v1.0 ledger claim-string printed 12.7319 for this quantity; corrected in the v1.1 artifact specification — Appendix D.3.)*

---

## §12. Falsification gates

Table 12.1. Pre-registered falsification gates. Layer M = mathematical, immediate rejection; S = simulation or internal consistency, revision required; O = observational or external. **Gates F-M61.17 to F-M61.24 are new in v1.1.**

| Gate | Layer | Trigger | Consequence |
|---|---|---|---|
| F-M61.1 | M | Any generator is shown to act on an unstated or incorrect carrier after R0. | The repaired action is invalid; §3 void. |
| F-M61.2 | M | A unitary of the form J W† J W is exhibited with det V ≠ +1. | Theorem M61.2 void. **Corrected in v1.2:** §5 does *not* collapse to M\*, because Theorem M61.15 derives T₂ from the vertex form and the field range without using the determinant (§21.2(iv)). |
| F-M61.3 | M | D₄ is used anywhere as the physical pointer covariance proof. | Type error; the claim relying on it is void. |
| F-M61.4 | M | A graded relative unitary is found whose minimal spectral arc is below 0.940241632013553 while reproducing λ. | Theorem M61.3 void. |
| F-M61.5 | M | V = exp[iτ(B₀ − B₁)] is used without a commutation or logarithm proof. | The generator translation is void. |
| F-M61.6 | S | A perturbative or short-slab S14 vertex is presented as reproducing λ. | Theorem M61.8 is contradicted; one of the two must be withdrawn. |
| F-M61.7 | M | The End\_{D₃}(H₅) multiplicity qubit is identified with the ZS-A3 doublet without an explicit intertwiner and a leakage certificate. | Support claim void. |
| F-M61.8 | S | A carrier of dimension ≤ 3 is exhibited realising λ with T < 0.835381287313630. | Theorem M61.4 void. |
| F-M61.9 | S | Any shape parameter — width, weight, correlation time, theta angle — is solved from λ. | The parameter budget of §7.2b is exceeded; the zero-additional-parameter claim fails. |
| F-M61.10 | S | The near-miss √(**A**/μ) is used in place of, or as evidence for, T₂. | Numerology; the statement is void. |
| F-M61.11 | S | A theta weight or an anchor point is selected after roots are inspected. | The divisor is fitted; §9 void. |
| F-M61.12 | S | The identity 1 − T₂² = (1 − \|λ\|²)/(1 − Re²λ) is presented as an independent confirmation of ZS-U12. | Circular; the statement is void. |
| F-M61.13 | M | A statement of this paper is quoted without its epistemic tag, or a necessary condition is called a physical realisation. | Citation error; epistemic overclaim. |
| F-M61.14 | S | τ\* = 12.7328 is used as evidence rather than as the labelled conditional diagnostic. | Unlicensed identification. |
| F-M61.15 | O | **(H-VAC-BDY)** is falsified: the ZS-S14 boundary-process state is shown to carry irreducible off-vacuum weight. | §§7–8 lower to CORPUS-UNDERDETERMINATION; §§4–6, §9-generic, §10 and T₂ survive. |
| F-M61.16 | M | (F2) fails: the seam ℤ₂ is shown not to be an exact symmetry of the repaired action, measure or regulator. | The whole graded chain, ZS-M60 included, is inapplicable; the ungraded channel must be computed directly. |
| **F-M61.17** | M | §7.2 is cited as a derivation, prediction, selection or closure of λ, or its residual is reported as evidence. | The citing statement is void (Theorem M57.C.2, Theorem M56.7). |
| **F-M61.18** | M | D\_phys = 0 is asserted for the actual repaired-S14 family without a transversality or non-intersection certificate for that family. | Reverts to CLOSED-NEGATIVE-GENERIC. |
| **F-M61.19** | S | Theorem M61.2(iii) is presented as a new general theorem rather than as a graded-relative-unitary identification of a classical Cartan-embedding fact. | Imported-theorem firewall breach; novelty claim void. |
| **F-M61.20** | S | The minimal vertex H\_int = g Z\_path ⊗ ε̂ is presented as derived from S\_S14 rather than selected as minimal. | Choice C2 is undeclared; §7 loses its conditional label. |
| **F-M61.21** | M | (H-VAC-BULK) is cited as evidence for (H-VAC-BDY). | Non-entailment; the support claim is void (see §7.3). |
| **F-M61.22** | S | Theorem M61.8 is presented as a class-free no-go rather than as a no-go within the graded doublet class. | Scope breach. |
| **F-M61.23** | S | Theorem M61.11 is presented as established novelty rather than as NOT\_FOUND pending D-M61-PRIOR. | Novelty overclaim. |
| **F-M61.24** | S | The unqualified phrase "zero free parameters" appears in a ZS-M61 title, abstract, figure caption or conclusion. | Parameter-budget overclaim; must be replaced by the §11.1a phrasing. |
| **F-M61.25** | M | A target-blind S14 derivation yields an effective seam arc u = 2c·ε_max < φ = 2.172948379550106 while the graded bridge is still asserted. | Theorem M61.14 is contradicted; the graded bridge is CLOSED-NEGATIVE and no boundary law can rescue it. |
| **F-M61.26** | M | A boundary law is exhibited with supp P ⊆ [−ε_max, ε_max] reproducing Re λ with 2c·ε_max < φ. | Theorem M61.14 void. |
| **F-M61.27** | M | A measure on an arc of half-width u ∈ [φ, π] with barycentre λ is exhibited with TV(ν, ν̌) < T(u). | Theorem M61.15 void. |
| **F-M61.28** | S | T₂ is presented as a consequence of det V = +1 after v1.2, or F-M61.2 is quoted with its v1.0 consequence clause. | Stale dependency: Theorem M61.15 derives T₂ without Theorem M61.2 (§21.2(iv)). |
| **F-M61.29** | S | Reduction R1 is presented as a discharge of (F2) rather than as a retyping of it. | NC-M61.3 stands; the three remaining items of Table 25.1 are undischarged. |
| **F-M61.30** | M | A positive closure of the S14 bridge is claimed without both FWD-R and FWD-I having been passed target-blind. | Closure claim void; the pre-registered alternative D-M61-NONID remains live. |
| **F-M61.31** | S | The 8000-draw block-I witness is quoted as research evidence after v1.2 rather than as a retained regression. | Superseded by Theorem M61.16; the sampling has no remaining research value. |
| **F-M61.32** | M | (F2) is assumed after v1.3 without stating which branch of the §28.5 dichotomy is taken. | The assumption is void: on the H_id branch (F2) is falsified by Theorem M61.19; on the alternative branch the vertex is not action-derived. |
| **F-M61.33** | S | A canonical kink weight (p = 0, 1 or 2) is presented as satisfying FWD-I. | Theorem M61.21: all three give ⟨ε⟩ ≤ 1/2 < T₂. The claim is void. |
| **F-M61.34** | S | A slot of the **5** is claimed to carry zero Yukawa weight. | Theorem M61.19: the Gram form is isotropic, so no slot can vanish. |
| **F-M61.35** | S | Theorem M61.20 is used outside its feasibility domain cos u ≤ x ≤ 1. | Infeasible; no measure exists and the formula returns a meaningless value. |
| **F-M61.36** | M | One symbol is used for two rows of the §34.3 TYPE LOCK table (ρ = \|Φ\|, θ = arg Φ, S = Im Φ). | Type error; the statement is void. This is the error that produced the entire v1.3 dichotomy. |
| **F-M61.37** | M | An unbiased (uniform) Goldstone phase law is claimed to reproduce λ. | Theorem M61.23: a(c) = J₀(2c) is real and min J₀ = −0.402759 > Re λ. Void at every c. |
| **F-M61.38** | S | A biased Goldstone law is presented as reproducing λ without stating the ΔN_eff and masslessness cost, or without the M56.7 two-for-two disclosure. | Fit presented as derivation; §35.3–§35.4. |
| **F-M61.39** | S | "ε = ±1" or "the two vacua" is used for the ZS-A3 vacuum manifold. | The manifold is the circle \|Φ\| = 1; the two-point reading is a mis-statement (§34.1). |
| **F-M61.40** | M | The ZS-F0 abstract parity J_Z = diag(+1,−1) is used as if it were the field-coordinate statement \|0⟩ ↔ Re Φ, \|1⟩ ↔ Im Φ. | The intertwiner ι_ZΦ is OPEN (D-M61-IOTA, §40.3); the identification is void without it. |
| **F-M61.41** | M | Theorem M61.23′ is called unconditional, or a flat potential is said to imply the Haar phase law. | (H-U1-BDY) is required (§41.1) and the verdict is conditional (§41.2); the claim is void. |
| **F-M61.42** | S | Complex conjugation is presented as *the unique* seam involution rather than one representative of a conjugacy class. | Theorem M61.22′ (§40.1); the uniqueness claim is void. |
| **F-M61.43** | S | A statement listed in the §43.3 superseded register is quoted as current. | Citation error; §44.1 is the authoritative board. |
| **F-M61.44** | S | A release is issued without passing Gate K — title, subtitle, status line, abstract terminal sentence and §44.3 in agreement — or asserts a ledger-provenance relation the release script does not measure. | Release-blocking; §46.1–§46.2, Rule R12. |

---

## §13. Non-claims

NC-M61.1. R0 is not claimed to be the unique colour repair, only the minimal one.

NC-M61.2. ZS-M61 does not claim that no Z-Spin process anywhere carries a nonempty anchor divisor, nor that the actual S14 family avoids the codimension-two locus.

NC-M61.3. ZS-M61 does not prove (F2). It assumes it and flags every statement that uses it. ZS-M56 gate F-M56.19 remains open and is inherited unchanged.

NC-M61.4. ZS-M61 does not construct the full closed-time-path boundary kernel of ZS-S14, does not certify reflection positivity, and does not compute a sector amplitude a\_N(s).

NC-M61.5. ZS-M61 does not derive the coupling g or the slab duration τ separately. It derives neither of them at all: it *solves* their product from λ. The separation would additionally require the metric clock that ZS-Q19 owes.

NC-M61.6. ZS-M61 does not claim that dim ℋ\_E = 2. Theorem M61.6 removes the need for any such claim, and (H-DOUBLET-SUPPORT) of ZS-M60 is neither proved nor used.

NC-M61.7. ZS-M61 does not advance, and does not touch, the Riemann Hypothesis, barrier B3, the Yang–Mills mass gap, or the ZS-S19/S20 Hodge-measure selection. R0 changes no numerical output of ZS-S1, ZS-S7 or ZS-S17–S24.

NC-M61.8. The identity λ = Log z\* is recorded as provenance, not as a new theorem.

**NC-M61.9′ (replaces NC-M61.9).** ZS-M61 does not reserve a successor paper, but it does register one named forward deliverable, D-M61-FWD (§7.2), plus three debts: D-M61-VAC (§7.3), D-M61-PRIOR (§10) and D-M57-SIGN (§7.2a). Whether D-M61-FWD is executed as ZS-M62, as an erratum-plus-appendix to this paper, or by the ZS-Q19 line, is the owner's decision and not this paper's.

**NC-M61.10 (new).** ZS-M61 does not claim that S\_S14 predicts λ, nor that the agreement of §7.2 tests the i-tetration identification of the multiplier.

**NC-M61.11.** ZS-M61 does not claim that Theorem M61.2(iii) is a new theorem of Lie theory, nor that Theorem M61.11 is established novelty.

**NC-M61.12 (new in v1.2).** ZS-M61 does not prove (F2). Reduction R1 (§25) reduces it to five finite items, two of which are settled and three of which are registered as D-M61-WARD. NC-M61.3 is unchanged.

**NC-M61.13 (new in v1.2).** ZS-M61 does not derive c, ε_max or ⟨ε⟩ from the S14 action. FWD-R and FWD-I (§22) are stated, pre-registered and OPEN. No target-blind number appears anywhere in this paper.

**NC-M61.14 (new in v1.2).** The general two-parameter closed form M\*(a; u) of §21.2(v) is stated for the active outer branch only. Its inner-diamond branch and its feasibility boundary in full generality are registered as D-M61-ARC and are not proved here.

**NC-M61.23 (new in v1.5).** ZS-M61 does not claim that complex conjugation is the unique seam involution. Theorem M61.22′ establishes one conjugacy class of reflections; the representative, i.e. the angle α, is not fixed here.

**NC-M61.24 (new in v1.5).** ZS-M61 does not claim that the ZS-F0 parity eigenbasis is (Re Φ, Im Φ). That identification requires ι_ZΦ, registered OPEN as D-M61-IOTA. Nothing here shows any ZS-F0 statement to be false.

**NC-M61.25 (new in v1.5).** ZS-M61 does not claim Theorem M61.23′ unconditionally. (H-U1-BDY) is required, and v1.4's inference from a flat potential to a Haar state is withdrawn.

**NC-M61.3 (rewritten in v1.5).** ZS-M61 does not assume (F2). On the H_id branch item W1 is **falsified** (Theorem M61.19); the surviving statement is the §28.5 dichotomy, governed by gate F-M61.32. Every result depending on (F2) is marked conditional in the §44.1 board.

**NC-M61.12 (rewritten in v1.5).** D-M61-WARD is executed, not open: W2 holds, W3 is upstream-ambiguous (D-S14-PHI), W1 fails. What remains is a dichotomy, not a checklist.

**NC-M61.13 (rewritten in v1.5).** ZS-M61 now contains target-blind numbers — Theorem M61.21's 3/8, 1/2, 5/16 and Theorem M61.23′'s min J₀ versus Re λ. What it does not contain is a target-blind derivation of c or of the phase law; FWD-R and FWD-I remain OPEN.

**NC-M61.14 (rewritten in v1.5).** The general M\*(a; u) closed form is **complete** (Theorem M61.20: feasibility boundary, inner and outer branches, two-atom extremal structure, dual certificate). D-M61-ARC is closed. What is not claimed is novelty; prior art is NOT_FOUND.

**NC-M61.20 (new in v1.4).** ZS-M61 does not claim that the seam involution of the *matter* sector is charge conjugation. Theorem M61.22 classifies involutions of the **Z-bias field space** only; the extension to H₅ and the fermions is stated as the shape of the obstruction (§34.4), not proved.

**NC-M61.21 (rewritten in v1.6).** ZS-M61 does not derive the Goldstone phase law from the action. Theorem M61.23′ assumes the law is Haar-uniform, which is the named hypothesis (H-U1-BDY) and **not** a consequence of the potential being flat; the withdrawal of that inference is stated once, in NC-M61.25. If the boundary phase law is not Haar-uniform, the theorem does not apply and §35.4's first branch is vacated. *(v1.4's clause "which is what an exactly flat potential gives" is deleted; §46.4.)*

**NC-M61.22 (new in v1.4).** ZS-M61 does not recommend adding a Goldstone-breaking term. §38.2 states the opposite: doing so because λ requires κ\* ≈ 3.74 would be the M56.7 trap in its purest form.

**NC-M61.16 (new in v1.3).** ZS-M61 does not resolve the §28.5 dichotomy. It does not claim that ε is a component of H₅, nor that it is not. Resolving it requires ZS-A3 and ZS-F1, which are not loaded here (rule R6).

**NC-M61.17 (new in v1.3).** ZS-M61 does not claim that (F2) is false as a statement about some other action. Theorem M61.19 falsifies item W1 **for the ZS-S14 v2.0 master action under hypothesis H_id**, and that is the whole scope.

**NC-M61.18 (new in v1.3).** Theorem M61.21 does not derive the ε-marginal of the S14 boundary process. The kink-weight family is hypothesis (H-KINK-WEIGHT), a classical radial model of a quantum spectral measure. The negative verdict is on that sub-branch only.

**NC-M61.19 (new in v1.3).** ZS-M61 does not claim Theorem M61.20 is novel. D-M61-PRIOR is executed with locators; the status is NOT_FOUND and a systematic sweep (D-M61-PRIOR-2) is not performed.

**NC-M61.15 (new in v1.2).** Theorem M61.14 constrains the field range of the Z-bias, not the radial profile. Nothing here derives the ZS-A3 profile, the anchor radius r_H, or L_⊥; the radial reading of §19.2 is an interpretation of the same formula and carries no new physical claim.

---

## §14. Theorem M61.12′ — the Conditional S14-Compatible Realisation Theorem

**Theorem M61.12′ (Conditional S14-Compatible Realisation).** Under the repaired action of §3, the exact seam grading (F1) ∧ (F2), the minimal vertex of §7.1 and the boundary hypothesis (H-VAC-BDY), the ZS-S14 one-event boundary process **admits a unique realisation** reproducing the frozen Koenigs multiplier λ, with no additional fitted numerical parameter:

**a\_S14 = cos 2c\* − i sin 2c\* · ⟨ε⟩\* = λ ,  c\* = ½ arccos(Re λ) ,  ⟨ε⟩\* = −|Im λ|/√(1 − Re²λ) ,**

and the associated physical anchor divisor is empty for families in general position. **The theorem asserts uniqueness of the realisation given λ. It does not assert that S\_S14 selects that realisation.**

Table 14.1. The scoreboard, stated at the strength an external audit accepts. Rows marked ▲ are unchanged from v1.0; rows marked ▼ are downgraded here.

| Item | Verdict | Status |
|---|---|---|
| ▲ ZS-S14 colour block | Repaired in place by R0; the v2.0 clause and Theorem S14.E's single-carrier SU(3) closure are RETRACTED | PROVEN |
| ▲ det V = +1 for graded relative unitaries | Strictly stronger than covariance; classical Cartan core, new identification | PROVEN (+ IMPORTED-PROVEN core) |
| ▲ Spectral arc obstruction at the level of V | w\_min(spec V) ≥ 0.940241632013553; necessary, not binding here | PROVEN |
| ▲ Minimal asymmetry on a carrier of dim ≤ 3 | Raised from M\* to T₂ = 0.835381287313630; M\*-saturation needs dim ≥ 4 | PROVEN |
| ▲ Re a state-independent on a 2-dim graded carrier | Re a = ½ Tr V; spec V fixed by Re λ alone | PROVEN |
| ▲ Environment dimension | Cancels exactly under (H-VAC-BDY); (H-DOUBLET-SUPPORT) not needed | DERIVED-CONDITIONAL |
| ▼ **The multiplier a\_S14** | **Reproduces λ to 2.7 × 10⁻⁵¹ with two determined reals; the determination is a bijection on λ** | **DERIVED-CONDITIONAL + IDENTIFIABILITY** (was CLOSED-POSITIVE-CONDITIONAL) |
| ▼ **S14 selection of the realisation** | **Not addressed by this paper; deliverable D-M61-FWD** | **OPEN** (was implied closed) |
| ▲ The boundary state (as a bound) | Five ceilings, all tighter than ZS-M60's, all resting on T₂ alone | DERIVED |
| ▼ The boundary state (as a value) | Two-atom vacuum law, populations 0.917691 / 0.082309 | DERIVED-CONDITIONAL + IDENTIFIABILITY |
| ▲ Perturbative sector | c ≥ 1.086474189775053; no weak-coupling vertex reaches λ | CLOSED-NEGATIVE within the graded doublet class |
| ▲▼ **Physical anchor divisor** | v1.1: generic only. **v1.2: D\_phys = 0 for every λ-compatible family by Theorem M61.16, unconditionally** | **CLOSED-NEGATIVE** (restored, on the right class) |
| ▲ Route S, Route E, the D₄ shortcut, the 4π selector | All closed upstream or superseded here; none reopened | CLOSED-NEGATIVE |
| ▼▼ **(F2) beyond quadratic order** | v1.2: reduced to three finite checks. **v1.3: item W1 FALSIFIED on the H_id branch by Theorem M61.19; W3 upstream-ambiguous (D-S14-PHI); the dichotomy of §28.5 must be resolved** | **FALSIFIED-CONDITIONAL** — the sharpest open item |
| ★ **Yukawa slot isotropy** | G_{mn} = δ_{mn}/5 by Schur; no slot of the **5** can vanish; reproduces ZS-M10's Σσᵢ² = 1/5 | **PROVEN** (Thm M61.19, new) |
| ★ **General M\*(a; u)** | closed form with feasibility boundary, inner-diamond branch and two-atom extremal structure; M61.11 and M61.15 are its boundary cases | **PROVEN** (Thm M61.20, new); D-M61-ARC closed |
| ★ **FWD-I, canonical branch** | kink weights give ⟨ε⟩ = 1/2, 3/8, 5/16; T₂ needs p\* = −0.847672 | **CLOSED-NEGATIVE** (Thm M61.21, new) |
| ★ **Four unconditional results** | R0, Thm M61.3, Thm M61.11, Thm M61.20 use neither (F2) nor the vertex form | **PROVEN**, unaffected by §28 |
| ★★ **Seam involution classification** | one conjugacy class of reflections J_α : Φ ↦ e^{2iα}Φ̄; odd mode Im(e^{−iα}Φ); ε = \|Φ\| is seam-EVEN. *Corrected in v1.5: not a uniqueness claim* | **PROVEN** (Thm M61.22′) |
| ▼ **F0 parity ↔ F1 coordinates** | requires ι_ZΦ; **not** established | **OPEN** (D-M61-IOTA) |
| ★★ **Uniform-Goldstone no-go** | a(c) = J₀(2c); min J₀ = −0.402759 > Re λ; λ unreachable at every c. *Corrected in v1.5: requires (H-U1-BDY)* | **CLOSED-NEGATIVE-CONDITIONAL** (Thm M61.23′) |
| ★ **Broken-seam budget** | phase floor ½arccos(Re λ + δ); asymmetry floor Lipschitz with coefficient 0.137289 | **PROVEN** (Thm M61.24, new) |
| ★ **Dual certificate for M61.20** | zero duality gap at u = φ, 2.6, π | **PROVEN**; external-quotable |
| ▼ **Thm M61.12′** | demoted from headline to a **counterfactual** classification theorem (§37) | COUNTERFACTUAL |
| ▲▼ **(H-VAC-BDY)** | v1.1: HYPOTHESIS, conflicted. **v1.2: the equality case of Theorem M61.14; the conflict is dissolved and relaxing it costs phase, not consistency** | **THEOREM (equality case)**, D-M61-VAC closed |
| ★ **Universal phase floor** | c ≥ arccos(Re λ)/(2ε_max); equality ⟺ extreme support. No dimension restriction, no det V = +1 | **PROVEN** (Thm M61.14, new) |
| ★ **Arc-asymmetry function** | T(u) strictly decreasing on [φ, π], T(φ) = T₂, T(π) = M\* exactly; T₂ independent of Theorem M61.2 | **PROVEN** (Thm M61.15, new) |
| ★ **Characteristic-function form** | a = Φ_P(−2c) for every boundary law in every dimension | **PROVEN** (Thm M61.13, new) |
| ★ **Reachability** | with the clock free, λ is reached only in codimension one; under minimal phase the whole content is \|⟨ε⟩\| = T₂ | **PROVEN** (Thm M61.17, new) |
| ★ **Forward gates** | FWD-R: c ≥ c\*/ε_max, a one-sided inequality on one number. FWD-I: \|⟨ε⟩\| = T₂, sensitivity 0.714693 | **OPEN, TESTABLE** (new) |
| ▲ Separation of g from τ | Requires the ZS-Q19 metric clock | OPEN, and does not block the classification |
| ▲ General M\*(a) | Closed form with correct domain split, LP-certified; prior art NOT\_FOUND | PROVEN, novelty pending D-M61-PRIOR |

### 14.1 The terminal rule, applied honestly — and failing

The successor seed set the standard: M61 closes positively only if **the repaired action independently constructs the physical boundary data** and the comparison yields the target. **v1.0 claimed it does. It does not.** What the paper constructs is the *class* of realisations and the *unique member* of that class consistent with the target. The action's independent construction of (c, ⟨ε⟩) is D-M61-FWD and is not performed.

It does not close negatively either: no exact fail-fast gate excludes the target. The arc gate clears with margin 0.997 and the convex-hull feasibility is automatic once Re λ fixes the spectrum.

By the audit protocol's own terminal rule — target precisely defined, central claim audit-passed, remaining OPEN separated from scope, downstream debt recorded, **no release-blocking S2-or-above defect outstanding** — this paper is now:

> **AUDIT-MAJOR-REVISION → integrated. Status: REVIEW-READY, MAJOR REVISION INTEGRATED. Not TERMINAL, not TERMINAL-IN-SCOPE.**
> **External referee mapping: Major Revision (v1.0) → resubmission-ready (v1.1).**

TERMINAL-IN-SCOPE becomes available if and only if D-M61-VAC is resolved and (F2) is either executed or explicitly excised from the scope statement. **v1.2 closes the first of those two: D-M61-VAC is dissolved by Theorem M61.13 and priced by Theorem M61.14.** What remains for TERMINAL-IN-SCOPE is D-M61-WARD — the three finite items of Reduction R1 — plus assignment of a persistent identifier to the artifact. TERMINAL requires FWD-R and FWD-I, or the Non-Identifiability Theorem D-M61-NONID in their place.

### 14.2 What would have made this a negative closure

Three things, each tested and none of which occurred. If det V had been −1-admissible, Theorem M61.4 would have collapsed and the corpus would have kept M\* with nothing new. If the vacuum manifold had been single-valued or continuous, Theorem M61.6 would have failed and the environment dimension would have re-entered as an unremovable hypothesis. And if |Re λ| had exceeded unity — it does not, |Re λ| = 0.566417 — the eigenphase φ would not have existed and the two-dimensional route would have been empty at the first step.

**And one thing that did occur, recorded here rather than in a footnote.** The paper's central positive claim turned out, on audit, to be an identifiability statement the corpus had already classified as non-evidential three papers earlier. That is a failure of internal cross-reference, not of mathematics, and the correction is the most valuable single change in this revision.

---

## §15. Deep-exploration record

Two cycles were run for v1.0 and one audit-integration cycle for v1.1.

### 15.1 Step 0 — long list, seven candidates

| # | Candidate | Disposition |
|---|---|---|
| L1 | Relative-unitary spectral geometry: state-independent arc and generator obstructions. | RETAINED, load-bearing. Became Theorems M61.3 and, unexpectedly, M61.2. |
| L2 | Multiplicity-space carrier: exploit H₅ ↓ D₃ = 1 ⊕ (2 ⊗ ℂ²\_mult). | RETAINED as algebra (§3), DROPPED as a support theorem. |
| L3 | Exact finite symmetry: replace perturbative grading by a finite symmetry test. | RETAINED after replacing D₄ by the physically represented seam ℤ₂ (§4.3). |
| L4 | ZS-A3 kink shell: translate the threshold into a radial phase-capable region. | DEMOTED to a conditional corollary (§8.2). |
| L5 | Odd-vertex derivative: bound the initial phase velocity from B₀ − B₁. | DROPPED. Theorem M61.8 proves the s → 0 regime empty. |
| L6 | General asymmetry theorem: export the sharp M\*(a). | RETAINED, load-bearing for external value. Became Theorem M61.11. |
| L7 | Microscopic repaired-action / CTP route: compute state, multiplier, theta family, divisor. | **PARTIALLY DROPPED in v1.0; RESTORED as the forward deliverable in v1.1.** v1.0 replaced the heavy path with two rigidities and then treated the replacement as a substitute for the bridge. It is not: the rigidities classify, and only L7 selects. D-M61-FWD is L7. |

**The largest single change in v1.1 is the reinstatement of L7.** v1.0's §15.1 wrote that "once the vertex is seam-odd and the vacuum manifold is two-valued, the multiplier is a two-atom characteristic function and the entire functional-integral apparatus contributes nothing that survives into a." The first half is true. The second half is false in the only sense that matters: the functional integral is the only thing that could supply c and ⟨ε⟩ *without looking at λ*, and that is exactly what the bridge needs.

### 15.2 Step 1 — MECE issue list

| # | Issue | Retained? |
|---|---|---|
| I1 | Type-correct repaired action | YES — §3 |
| I2 | Exact covariance: does one represented seam involution act on system and environment? | YES — §4; and its answer is *assumed*, not proved |
| I3 | Relative-unitary feasibility: can the action-derived V have barycentre λ? | YES — §5, §6 |
| I4 | Physical state: does the same action construct ρ\_E and a **without target fitting**? | **NO — this is D-M61-FWD. v1.0 recorded YES for §§7–8; that record is corrected.** |
| I5 | Terminal comparison: equal, excluded, or underdetermined? | **UNDERDETERMINED, pending I4.** |
| — | D₄ pointer test | DROPPED — not physically formulable (ZS-M57) |
| — | Kink radius as a closure gate | DROPPED — downstream of a profile identification |
| — | τ\_Z extraction | DROPPED — not needed for a per-event classification |

### 15.3 Node statuses entering and leaving ZS-M61 v1.1

| Node | Entering v1.0 | Leaving v1.0 | Leaving v1.1 |
|---|---|---|---|
| H₅ ↓ D₃; no 2-dim su(3) rep | PROVEN | PROVEN | PROVEN |
| Original S14 colour clause | RETRACTED / void | REPAIRED by R0 | REPAIRED by R0 |
| QND barycentre a = Tr(ρ\_E V) | PROVEN | PROVEN | PROVEN |
| Sharp asymmetry bound T ≥ M\* | PROVEN | superseded on dim ≤ 3 by T₂ | unchanged |
| det V for a graded relative unitary | not stated in the corpus | PROVEN = +1 | PROVEN = +1, prior-art scoped |
| Spectral arc lower bound | DERIVED in the seed | PROVEN | PROVEN |
| Multiplicity qubit = ZS-A3 doublet | OPEN | OPEN, made irrelevant | unchanged |
| Exact seam-ℤ₂ covariance (F2) | OPEN | OPEN, assumed | **OPEN, front-page, load-bearing** |
| Boundary-state support | OPEN | (H-VAC) HYPOTHESIS-strong | **(H-VAC-BDY) HYPOTHESIS, conflicted (D-M61-VAC)** |
| ρ\_E, a\_S14 | OPEN | DERIVED-CONDITIONAL | **DERIVED-CONDITIONAL + IDENTIFIABILITY** |
| D\_phys | OPEN | = 0, DERIVED | **= 0 generically, DERIVED-CONDITIONAL on (H-GP)** |
| Finite-time vertex bound from first order | OPEN | SUPERSEDED, regime empty | unchanged, class-scoped |
| S14 selection of the realisation | not posed | implicitly claimed | **OPEN, posed as D-M61-FWD** |

### 15.4 Convergence

v1.0's execution cycle gave 6 → 2 → 0 and declared CONVERGED. **v1.1 reopens that convergence and records the reopening**, per the audit rule that a convergence resting on a false root premise is not a convergence. The audit-integration cycle: sweep 1 changed nine nodes (the seven above plus the parameter-budget statement and the verification census); sweep 2 changed three (the anti-numerology figures, the residual errata, the prior-art scoping of M61.2 and M61.11); sweep 3 changed none. **9 → 3 → 0: CONVERGED at the level of status assignment.** Convergence at the level of the physical bridge is not claimed and cannot be, because D-M61-FWD is not executed.

### 15.5 Value relative to ZS-S14 and ZS-M60 — rescored

| Axis | ZS-M60 v1.5 | ZS-M61 v1.0 (self-scored) | ZS-M61 v1.1 (audit-integrated) | Reason for the change |
|---|---|---|---|---|
| Mathematical density | 9 | 8 | 8 | Unchanged; the theorems are unchanged |
| Terminal-decision strength | 7 | 9 | **6** | Two verdicts downgraded, one restored to OPEN |
| Physical closure potential | 6 | 9 | **6** | A realisation class is classified, not selected |
| External legibility | 7 | 8 | **8** | Unchanged; M61.11 still needs no Z-Spin input |
| Internal cross-reference discipline | — | (not scored) | **3** | The M57.C.2 collision should have been caught in drafting |
| Conditionality burden | — | 2 named hypotheses | **2 hypotheses + 6 declared choices + 1 conflict** | Made explicit rather than added |

**The paper is worth more, not less, after this revision** — because the claim an external referee would have attacked first has been removed by the authors rather than by the referee, and because what remains (T₂, the carrier-dimension gap, the non-perturbative threshold, M\*(a)) is defensible without any hypothesis this paper cannot name.

### 15.6 Self-reference and pattern audit

This paper resembles the ZS-M56–M60 pattern of separating formal channel existence from physical provenance, and the corpus-wide habit of turning an open functional problem into two closed-form numbers. **v1.0's own §15.6 flagged that resemblance and then committed the error anyway**, in the one section where the resemblance was not a stylistic tic but the substance: §7.2 turned an open functional problem into exactly two closed-form numbers, and those two numbers were a coordinate change on the target. The pattern audit failed because it looked for numerological resemblance and not for *algebraic identity with a previously judged construction*. The corresponding new discipline, offered to the corpus rather than to this paper alone:

> **Rule R11.** Before promoting a two-real-parameter match to a selection or closure claim, search the corpus for a prior bijection between the target and any two-real parameterisation. If one exists, the new claim inherits that prior verdict unless it adds an independent determination of at least one parameter.

Applied retroactively, R11 would have caught §7.2 at drafting time, because ZS-M57 M57.C.2 is exactly such a bijection and its verdict was already recorded.

The counterexample-level audit of v1.0 stands and is retained: a merely covariant unitary with det V = −1 exists explicitly; a carrier of dimension three reaches M\* if that unitary is admitted; a state supported off the doublet has T = 1 with zero doublet weight; a Gaussian width of 0.05 already damps the modulus by 0.994; and 8000 random graded families produced no zero with minimum |a| = 2.31 × 10⁻³.

---

## §16. Observational consistency

ZS-M61 makes no new observational prediction and disturbs no existing one. The v1.1 status changes are all in the direction of weaker claims and therefore cannot disturb any observation that v1.0 left untouched.

| External or corpus datum | Effect of ZS-M61 v1.1 |
|---|---|
| Planck 2018 ΛCDM parameters | Untouched. No cosmological quantity appears in any theorem. |
| α\_s(M\_Z) = 11/93 = 0.118280 (ZS-S1, ZS-Q3) | Unchanged; derived from the ZS-S1 spectral bridge and Y-sector counting, never from the withdrawn 2′ clause. |
| m(0⁺⁺) = v**A**/**Q** = 1.791 GeV, Λ\_QCD = 264.1 MeV (ZS-S7) | Unchanged. R0 does not alter the truncated-icosahedron geometry. |
| sin²θ\_W, v = 245.93 GeV, m\_t (ZS-S1, ZS-S4, ZS-S13) | Unchanged; colour-singlet or fermion-sector outputs. |
| SM hypercharge unit 1/6; q\_Φ = X = 3 (ZS-M60.7) | Unchanged. R0 keeps the Z-bias field in the multiplicity-one D₃-trivial component. |
| ZS-U12 per-transit leak 1 − \|λ\|² = 0.205204 | Appears as the numerator of the seam-overlap ceiling; recorded as an identity, gated against circular use (F-M61.12). |
| ZS-Q7 Z-channel capacity ln 2 | The conditional boundary-state entropy is 41.03% of it; no capacity claim is made. |
| ZS-M60.32 observation ⌊n\_max⌋ = 2 = dim **Z** | RETIRED. The sharpened budget gives ⌊n\_max⌋ = 1. Rests on T₂ alone and therefore survives every v1.1 downgrade. |
| ZS-S19 / ZS-S20 Hodge-measure selection | Untouched. |
| Absence of observed leptoquarks | Now consistent by construction rather than by silence: R0 withdraws the leptoquark block the v2.0 clause asserted. |
| ZS-M57 §16.3 Route-S locus ε(r\_H) = 0 | **NEW ROW.** In tension with (H-VAC-BDY); registered as D-M61-VAC and not resolved here. |
| ZS-M57 v1.8 sign convention for s | **NEW ROW.** Internally inconsistent between M57.C.2 and M57 §11.2; registered as D-M57-SIGN. |

---

## §17. Conclusion

ZS-M60 ended by saying that what remained was not one number but three inputs: the all-orders validity of the graded interaction, the seam-ℤ₂ asymmetry of the actual boundary state, and whether that state lives on the ZS-A3 doublet at all. **v1.0 claimed two of the three settled and the third shown not to matter. v1.1 states the honest arithmetic: one of the three is settled, one is replaced by a weaker-looking hypothesis that is not actually weaker, and one is shown not to matter.**

What is settled is the classification, and it is worth having. The engine turned out to be a single sign. A seam-covariant unitary satisfies det V = ±1; a seam-covariant unitary that arises as a relative unitary of a graded dilation satisfies det V = +1. That excludes an odd number of eigenvalues at −1, which excludes the two-atom measure attaining M\* from any carrier of dimension three or less, which raises the minimal asymmetry to **T₂ = 0.835381287313630**. The corpus had been carrying 0.763362818245964 for a process whose carrier cannot realise it. That correction is unconditional on (H-VAC-BDY), survives every downgrade in this revision, and is the reason this paper exists.

Three further results stand. The event is intrinsically non-perturbative within the graded doublet class: c ≥ 1.086474189775053 whatever the odd fraction of the branch Hamiltonian, so no weak-coupling truncation of ZS-S14 can produce λ — which explains thirty-one versions of failure rather than merely recording them. The physical anchor divisor is empty for families in general position, because a zero needs two real conditions on a one-parameter circle; ZS-M59 declared in advance that D = 0 is a complete result, and this is that result at the generic quantifier, with the actual family's position gated. And the corpus's own observation ⌊n\_max⌋ = 2 = dim **Z** dissolves under the sharpened budget, which is what should happen to a coincidence that was flagged as one.

What is exported outside the corpus is Theorem M61.11: the minimum asymmetry resource an environment must supply to produce a prescribed complex dephasing multiplier under symmetric dynamics, in closed form with the correct inner-diamond and outer-domain split, certified against an independent linear program. It uses no Z-Spin input, its prior-art status is NOT\_FOUND rather than NEW, and it is — the irony is worth naming — the paper's most defensible contribution while being the one its v1.0 title did not mention.

**And what is not settled, stated as plainly as the rest.** The repaired action is not shown to select the realisation this paper classifies. Matching a = λ inside the vacuum-supported ansatz is two reals against two reals, it is the same bijection ZS-M57 already judged non-evidential, and calling it a Terminal Physical Bridge was wrong. The exact seam covariance (F2) is assumed and load-bearing. The boundary hypothesis (H-VAC-BDY) does not follow from the bulk fact that was cited for it, and the corpus's own Route-S analysis locates the mediation at ε = 0 rather than ε = ±1. Those are the three places to attack, in that order, and this version names them instead of clearing them.

Stated at exact strength. The ZS-S14 colour block is repaired and its single-carrier SU(3) closure withdrawn. Every graded relative unitary has unit determinant. A carrier of dimension at most three cannot reach M\* and must reach T₂. The real part of the multiplier is a property of the dynamics alone. The environment dimension cancels on the vacuum manifold. Inside that ansatz the realising data are unique — and uniqueness given the target is not derivation of the target. The divisor is generically empty and the perturbative regime is empty. Two hypotheses and six structural choices are named, gated and attackable. **One deliverable, D-M61-FWD, is registered: the S14 forward selection. The S14 measurement line does not stop here.**

---

## Acknowledgements & Code Availability

The author thanks the reviewers of the ZS-M61 successor seed v1.0 and v1.1, and the independent audit of 17 August 2026 whose four central findings — the M57.C.2 collision, the genericity-to-universality jump in §9, the (H-VAC) split, and the verification-count retyping — are integrated in full in this version. The audit's judgement that the paper should be preserved and revised rather than discarded is accepted, as is its judgement that lowering the central claim raises the paper's external value.

During construction of v1.0 the fail-closed ledger mechanism fired once. Ledger row A2 initially asserted λ = Log z\* as an exact zero and tested it with an equality against 0; at fifty working digits the root-finder returns a residual of 1.34 × 10⁻⁵¹ and the row returned FAIL. The claim string was corrected to assert agreement at the working precision rather than exact equality. The mechanism was not relaxed, and the incident is recorded rather than silently repaired.

**A second incident, recorded in v1.1.** The v1.0 Acknowledgements stated that every deterministic figure printed in the manuscript appears verbatim in one seeded run. **That statement is false and is withdrawn.** Fourteen printed residuals, two draw-counts, one family size and one hit count disagree with the shipped artifact; all are listed in Appendix D.2 and D.3, all are corrected above, and none changes a conclusion. The discipline that catches the large errors is the same discipline that catches these, and the failure mode is instructive: the figures were transcribed from development runs rather than regenerated from the release run. The v1.1 artifact specification (§18.2) requires the manuscript figures and the ledger to be emitted by the same invocation.

**Code.** The release artifact is `zs_m61_verify_v1_6.py`, SHA-256 `a2e6cc58…9ffa1e6`, emitting `zs_m61_verify_v1_6.json` (SHA-256 `08cf94e0…dde8446`, **228 rows, 0 FAIL**) and `figures.json` (SHA-256 `c1d3fccf…32518138`). *(Superseded chain:)* `zs_m61_verify_v1_5.py`, SHA-256 `0b5f51ca…48b2f7`, emitting `zs_m61_verify_v1_5.json` (SHA-256 `40deeb45…03c329a`, **220 rows, 0 FAIL**) and `figures.json` (SHA-256 `c1d3fccf…32518138`). *(Superseded chain:)* `zs_m61_verify_v1_4.py`, SHA-256 `5efebde2…4dc6d1`, emitting `zs_m61_verify_v1_4.json` (SHA-256 `9ee95fdc…0ada42a`, **204 rows, 0 FAIL**) and `figures.json` (SHA-256 `c1d3fccf…32518138`). *(Superseded chain:)* `zs_m61_verify_v1_3.py`, SHA-256 `80da1c4a…a388ae`, emitting `zs_m61_verify_v1_3.json` (SHA-256 `3f39a5c8…564f349`, **181 rows, 0 FAIL**) and `figures.json` (SHA-256 `1e1aeea8…cba792b5`), shipped with `requirements.txt`, `RUN.md`, `CITATION.cff` and `zenodo.json`; output filenames are derived from the script basename. *(Superseded chain:)* `zs_m61_verify_v1_2.py`, SHA-256 `5e1668dd…cc06ca`, emitting `zs_m61_verify_v1_2.json` (SHA-256 `36362a0b…1ca25a`, **147 rows, 0 FAIL**) and `figures.json` (SHA-256 `32f99207…f8f8b08`, 75 entries), shipped with `requirements.txt` and `RUN.md`. The superseded `zs_m61_verify_v1_1.py`, SHA-256 `f5c6c099…24ac86`, and its 123-row ledger are retained for regression and are regression-preserved in the v1.2 ledger. The superseded `zs_m61_verify_v1_0.py`, SHA-256 `9fb1d8e9…52377e`, and its ledger `zs_m61_verify_v1_0.json`, SHA-256 `1ed4180d…b60cd`, are retained for regression; both were independently re-executed 17 August 2026 on CPython 3.12.3 with mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1, output byte-identical. Blocks: A frozen inputs and λ provenance (7); B the R0 colour repair (7); C the graded relative-unitary structure (6); D the spectral arc (4); E real-part rigidity (5); F the carrier-dimension linear program (9); G the boundary state and ceilings (10); H the vertex closure and vacuum-manifold rigidity (11); I the divisor (4); J the general M\*(a) theorem (8); K anti-numerology (5); L downstream consistency and retirements (7); M guards and non-claims (8). **Known limitations of the artifact are stated in §18.**

This work used AI tools (Anthropic Claude) for corpus and external-literature search, cross-paper integration, symbolic and numerical verification, independent re-execution of the ledger, abstract-syntax-tree audit of the verification script, and drafting, under the author's editorial direction. The author assumes full responsibility for all content. The v1.1 audit integration was performed with the source paper, the verification script and the ZS-M57 v1.8 text loaded and read directly.

---

## §18. Reproducibility — artifact manifest and known limitations

### 18.1 Artifact manifest

```text
ARTIFACT_MANIFEST
paper_code/version:   ZS-M61 v1.6

RELEASE ARTIFACT
main_script:          zs_m61_verify_v1_6.py
sha256(script):       a2e6cc58a1192031ebda1e7c320eec9ecb626f1e41377d6fe14ff94a29ffa1e6
sha256(ledger json):  08cf94e088c2c64bac17d6ce3632daec9b83af8d57868fd0b45ffb6ecdde8446
sha256(figures.json): c1d3fccfadafddb30128748e9a1b5e90208825b557f13fd9160ced0132518138
expected outputs:     stdout banner; zs_m61_verify_v1_6.json; figures.json
expected row count:   228          (EXPECTED_ROWS, fail-closed)
new in v1.6:          block V6 (8) -- section 46, the release-audit corrections
superseded:           zs_m61_verify_v1_5.py, 220 rows, regression-preserved
superseded:           zs_m61_verify_v1_4.py, 204 rows; 200 carried verbatim,
                      4 retyped/replaced, 0 residual drift (NOT a strict subledger)
output filenames:     DERIVED from the script basename (section 18.2(7) closed)
archival metadata:    CITATION.cff, zenodo.json ship with the artifact
superseded:           zs_m61_verify_v1_2.py, 147 rows, regression-preserved
fail-closed:          exit 1 on any FAIL row OR on a row-count mismatch
row-typing guard:     AST self-audit of the script's own source (block S)
ships with:           requirements.txt (hard == pins), RUN.md (one-command)

SUPERSEDED ARTIFACTS, retained for regression
prior_script:         zs_m61_verify_v1_1.py
sha256(script):       f5c6c099ce6c3aef918bda27a045f391ec3881c6f2bd9dde54d6f41d7624ac86
sha256(ledger json):  75034f3824491c6110e92d1c0b2deb33cd6698ed5266401d8c991402fff78492
row count:            123          (regression-preserved in the v1.2 ledger)
reproduction status:  byte-identical on re-execution, 2026-08-17

prior_script:         zs_m61_verify_v1_0.py
sha256(script):       9fb1d8e991c24efb312eb3e655ef63b5b913ff076a7a32544121de6d3252377e
sha256(ledger json):  1ed4180d2b274c8588ba5940a3fa4c547e71754a401c6ca2b4d2a7454bbb60cd
row count:            91
reproduction status:  byte-identical on independent re-execution, 2026-08-17

COMMON
runtime tested:       CPython 3.12.3
dependencies:         mpmath 1.3.0, numpy 2.4.4, scipy 1.17.1  (hard == pins)
random seed:          numpy default_rng(20260731)
precision:            mpmath dps = 50
one-command run:      python3 zs_m61_verify_v1_6.py
runtime class:        order 2-4 minutes (blocks F and J dominate)
license:              as per corpus release policy
persistent id:        NOT YET ASSIGNED  — see §18.2(5)

NOTE ON CROSS-ARTIFACT COMPARISON
Random-draw residuals of v1.1 are NOT comparable with v1.0's: v1.1 consumes the
shared RNG stream differently, by construction.  Deterministic rows — blocks B,
F, J and every closed form — are identical across the two artifacts.  A
stream-dependent extremum (e.g. the block-I divisor minimum) may not be quoted
as a stable figure; ledger rule (b) is extended accordingly.
```

### 18.2 Required artifact changes — status after v1.1

Items 1–4 and 6 were implemented in `zs_m61_verify_v1_1.py` and are carried forward unchanged in `zs_m61_verify_v1_2.py`; item 5 remains outstanding and is release-blocking for `FINAL`. **A seventh item is added in v1.2 as a consequence of a near-miss during this release.**

8. **Self-consistency audit — NEW and IMPLEMENTED in v1.5.** A release must pass a scripted audit of the manuscript against the artifact: ledger integrity, SHA and census agreement, every printed constant checked against `figures.json`, a stale-statement sweep, cross-reference resolution for sections/theorems/gates/non-claims/debts, and proof-pointer resolution for every DECLARATION row. It caught the Appendix D.5 erratum. Reading the manuscript is no longer an accepted substitute.

7. **Artifact-overwrite hazard — CLOSED in v1.3.** The v1.3 script derives its ledger and figures filenames from its own basename, so a variant can never overwrite a release ledger. *(The v1.2 statement is retained for the record:)* During the v1.1 release, a guard-test variant of the script wrote its ledger to the release filename and briefly replaced the release artifact with a deliberately-failing one. The error was caught by re-running and re-hashing, but it is exactly the class of accident the sync discipline exists to prevent. **Required:** derive the output filenames from the script's own basename, so that any variant writes to a variant filename and can never overwrite a release ledger.


1. **Row-count guard — IMPLEMENTED.** v1.0 claimed exit 1 "on a row-count mismatch" and contained no such check. v1.1 declares `EXPECTED_ROWS = 123`, compares it to the emitted count, prints `ROW-COUNT MISMATCH` and exits 1. Verified by deliberately mis-setting the constant.
2. **Row typing — IMPLEMENTED.** v1.1 removed the `THEOREM-PROOF` kind entirely, routes every untested statement through `decl()` (which requires a `proof` pointer), and block S re-parses the script's own source with `ast`, failing if any `row()` call passes a literal `True`/`False`. Verified by smuggling one in: the guard fires and the run exits 1.
3. **Claim-string digits — IMPLEMENTED.** Every printed digit is rendered by `fmt(value, n)` from the computed value; no digit is typed. Block R additionally regression-tests all three v1.0 errata (Appendix D.3) so that a regression would fail rather than pass silently.
4. **Manuscript figures — IMPLEMENTED.** The run emits `figures.json` (61 entries) and the manuscript is to be typeset from it. Transcription from a development run, which is what produced the fourteen D.2 errata, is no longer possible without bypassing the artifact.
5. **No persistent identifier / DOI — OUTSTANDING, now one manual step.** **v1.3 ships `CITATION.cff` and `zenodo.json`**, so the deposit is a single action: reserve the DOI, deposit the seven artifact files, then write the DOI back into §18.1 and into `CITATION.cff` (§32). Until the DOI exists the release is **"not yet publicly certified"** and `FINAL` may not be applied. This is the only release-blocking item remaining, and it is now blocked on a human action rather than on unfinished work.
6. **`requirements.txt` and `RUN.md` — IMPLEMENTED.** Both now ship with the artifact: hard `==` pins for the three dependencies, and a one-command reproduction file stating the expected banner, the expected row count, the three fail-closed mechanisms, the determinism guarantee and the cross-artifact comparison caveat.

---


---

# Part IV — The six breakthrough routes, executed

*Everything in Part IV is new in v1.2. Nothing in Parts I–III is retracted by it; §§19–21 strengthen §§5–8 and §23 strengthens §9, in each case by removing a hypothesis rather than by adding one.*

---

## §19. Theorem M61.13 — the boundary transfer law, and the dissolution of D-M61-VAC

### 19.1 The object, retyped

v1.1 took the physical object to be a **state** ρ_E and asked whether its support sits on ε² = 1. The audit's first route asks for the object to be retyped as a **transfer law** along the radial coordinate, ε(r_H) = 0 → ε(∞) = ±1. Carrying that out turns out not to require a new formalism at all — it requires deleting a hypothesis.

**Definition 19.1 (ε-marginal).** Let ε̂ be the Z-bias operator on ℋ_E, self-adjoint with spec ε̂ ⊆ [−1, 1] — which is exactly the range the ZS-A3 potential V(ε) = (λ_V/4)M_P⁴(ε² − 1)² permits for a field interpolating between its two minima. For a boundary state ρ_E define the **ε-marginal** P as the spectral measure of ε̂ in the state ρ_E,

**P(B) = Tr(ρ_E 𝟙_B(ε̂)) ,  B ⊆ [−1, 1] Borel.**

**Theorem M61.13 (Characteristic-Function Form). [PROVEN].** Let the seam-odd Z-bias vertex be H_int = g Z_path ⊗ ε̂ with accumulated phase c = τg, so that V = exp(−2icε̂) by §7.1. Then for **every** boundary state, in **every** environment Hilbert space of **every** dimension, finite or infinite, and with **no** hypothesis on the support of ε̂,

**a_S14(c) = Tr(ρ_E e^{−2icε̂}) = ∫_{−1}^{1} e^{−2icε} dP(ε) = Φ_P(−2c) ,**

where Φ_P(t) = ∫ e^{itε} dP(ε) is the characteristic function of the ε-marginal. Moreover, writing P = P_even + P_odd for the decomposition under the seam action ε ↦ −ε,

**Re a = ∫ cos(2cε) dP_even(ε) ,  Im a = − ∫ sin(2cε) dP_odd(ε) .**

Proof. The spectral theorem gives f(ε̂) = ∫ f(ε) dE(ε) for the projection-valued measure E of ε̂, and Tr(ρ_E f(ε̂)) = ∫ f(ε) dP(ε) with P = Tr(ρ_E dE). Apply this to f(ε) = e^{−2icε}. The second display follows because cos is even and sin is odd, so the even part of P annihilates the sine integral and the odd part annihilates the cosine integral. ∎

Executed over dimensions 2, 3, 5, 8, 13, 21 with random spectra in [−1,1], random states and random c: max residual 1.1 × 10⁻¹⁴ (block P, row P1).

**Corollary 19.2.** Theorem M61.6 is the special case P = p₋δ₋₁ + p₊δ₊₁, for which Φ_P(−2c) = cos 2c − i sin 2c ⟨ε⟩ (row P2). **(H-VAC-BDY) is therefore not a structural hypothesis at all — it is a support restriction on one measure.** Its role in v1.1 was to make the environment dimension cancel; Theorem M61.13 shows the dimension cancels regardless, because only the scalar measure P survives into a.

**Corollary 19.3 (where the phase lives).** If P is seam-symmetric, P_odd = 0 and a is real. Since Im λ ≠ 0, the seam ℤ₂ must be broken by the **boundary law**, never by the dynamics. Verified over 2000 random symmetrised marginals: max |Im Φ| = 0 to machine precision (row P3). This reproduces ZS-M57 Theorem M57.P′ in the transfer language and, in §25, is matched exactly by the Ward-identity reduction of (F2).

### 19.2 The radial reading

Let the ZS-A3 kink profile be ε(r) = tanh((r − r_H)/L_⊥), so ε(r_H) = 0 and ε(∞) = 1. Let ν be the radial weight of the boundary process. Then P is the pushforward P = ε_\*ν and

**a = ∫ exp(−2ic·tanh((r − r_H)/L_⊥)) dν(r) .**

**This is the retyping the audit asked for, and it is the same formula.** The anchor and the bulk are not two competing hypotheses about *which* value ε takes; they are the two ends of the interval over which P is supported. A state localised at the anchor has P concentrated near 0; a state deep in the bulk has P concentrated near ±1; anything in between is admissible and is described by the same characteristic function.

### 19.3 Debt D-M61-VAC — dissolved

v1.1 recorded a material conflict: ZS-A3 and ZS-M57 §16.3 place the bulk vacua at ε = ±1, while ZS-M57 §16.3 also localises the physical mediation at the Z-anchor where ε(r_H) = 0 and the ℤ₂ is restored. v1.1 could only register this as unresolved because its object was a state supported on ε² = 1, for which the two statements are mutually exclusive.

**Under Theorem M61.13 they are not exclusive and the conflict does not arise.** Both are statements about the support of one measure on one interval, and the physical question changes from *which one is true* to *what does the support cost*. §20 answers that question exactly, and the answer is a price in accumulated phase. **D-M61-VAC is closed as DISSOLVED**, and gate F-M61.21 is retained only against the weaker misuse of citing bulk support as evidence for a specific boundary law.

---

## §20. Theorem M61.14 — the universal phase floor

### 20.1 Statement

**Theorem M61.14 (Universal Phase Floor). [PROVEN].** Let P be any probability measure with supp P ⊆ [−ε_max, ε_max], 0 < ε_max ≤ 1, and let u := 2c·ε_max be the **effective seam arc**. If 0 ≤ u ≤ π then

**Re a = ∫ cos(2cε) dP(ε) ≥ cos(2c·ε_max) = cos u ,**

with equality if and only if P is concentrated on |ε| = ε_max. Consequently, realising Re a = Re λ requires

**cos u ≤ Re λ ,  i.e.  u ≥ arccos(Re λ) = φ = 2.172948379550106 ,  i.e.  c ≥ φ / (2 ε_max) = c\* / ε_max ,**

and equality holds if and only if the boundary law is concentrated on the extreme values |ε| = ε_max.

Proof. On |ε| ≤ ε_max and for u = 2cε_max ≤ π, the function ε ↦ cos(2cε) is even and decreasing in |ε|, so its minimum on the interval is attained at |ε| = ε_max with value cos u; a barycentre of values ≥ cos u is ≥ cos u, with equality iff the measure sits on the minimising set. Since arccos is decreasing, cos u ≤ Re λ ⟺ u ≥ arccos(Re λ). ∎ Executed: 1200 random laws across six support radii, none reaching Re λ below its floor; the floor is tight to 10⁻¹⁴ (rows P4–P5).

### 20.2 What this replaces

Theorem M61.8 of v1.0/v1.1 proved c ≥ c\* **only** on a two-dimensional graded carrier, via the odd-fraction bound v ≤ 1. Theorem M61.14 proves the same inequality

- in **every** dimension,
- for **every** boundary law,
- with **no** (H-VAC-BDY),
- with **no** det V = +1 and hence **no** dependence on Theorem M61.2,

and it identifies the equality case, which M61.8 did not. **c ≥ c\* is therefore not a doublet fact; it is a statement about the field range of the Z-bias.** Theorem M61.8 is retained as the SU(2) special case and its scope tag is narrowed accordingly (row P6).

**And it converts a hypothesis into an extremal characterisation.** v1.1 selected c = c\* by "minimality of the accumulated phase", listed as structural choice C4. Theorem M61.14 removes the choice: c = c\* **is** the minimum, and

> **c = c\*  ⟺  the boundary law is concentrated on |ε| = 1  ⟺  (H-VAC-BDY).**

The vacuum-supported law is not an assumption competing with anchor localisation; it is the unique minimal-phase realisation. Choice C4 is deleted from §11.1a and choice C3 is demoted from an independent hypothesis to the equality case of a theorem.

### 20.3 The price of anchor localisation, in numbers

Table 20.1. The phase floor as a function of the support radius. Every entry is c\*/ε_max, emitted by the artifact as `phase_floor_c_min_epsmax_*`.

| ε_max | interpretation | minimal accumulated phase c | ratio to c\* |
|---|---|---|---|
| 1.00 | deep bulk, vacuum-supported | **1.086474189775053** | 1 |
| 0.90 | near-bulk | 1.207193544194503 | 1.111 |
| 0.75 | mid-profile | 1.448632253033404 | 1.333 |
| 0.50 | half-way to the anchor | 2.172948379550106 | 2 |
| 0.25 | anchor shell | 4.345896759100212 | 4 |
| 0.10 | anchor core | 10.864741897750529 | 10 |

**Reading, and the physical content.** The ZS-M57 §16.3 anchor-localised route is *not* excluded — it is **priced**. Localising the mediating weight inside the shell |ε| ≤ 0.1 demands an accumulated branch phase ten times the minimum, c ≥ 10.86. Since c = τg is a dimensionless product of coupling and slab duration, this is a hard constraint on the S14 vertex that a forward calculation can meet or fail. **The v1.1 material conflict has become a quantitative trade-off, which is what a resolved conflict looks like.**

**Corollary 20.2 (the phase-dead core, re-derived).** ZS-M60.33 and §8.2 place the phase-capable shell at a nonzero radial distance from the anchor. Theorem M61.14 explains why: a shell too close to the anchor has ε_max too small, and its phase floor exceeds any available c. The two statements are the same statement, and the "irony" §8.2 recorded is resolved.

---

## §21. Theorem M61.15 — the arc-asymmetry function T(u)

### 21.1 The problem, in its correct generality

ZS-M60.23 minimised the seam asymmetry over **all** probability measures on the circle with barycentre λ, obtaining M\* = 0.763362818245964. Theorem M61.4 of v1.0 obtained the sharper T₂ = 0.835381287313630 by restricting the *carrier dimension*. Theorem M61.13 shows the correct restriction is neither: it is the **arc** on which the induced spectral measure lives, because V = exp(−2icε̂) has spectrum in {e^{−2icε} : ε ∈ supp P} ⊆ the arc of half-width u = 2c·ε_max.

**Definition 21.1.** For u ∈ (0, π] let

**T(u) := inf { TV(ν, ν̌) : ν a probability measure on the arc [−u, u], ∫ e^{iθ} dν(θ) = λ } ,**

where ν̌ is the reflection θ ↦ −θ and TV(ν, ν̌) = ½∫|dν − dν̌|.

**Theorem M61.15 (Arc-Asymmetry Function). [PROVEN].** T(u) is finite exactly for u ≥ φ = arccos(Re λ), and there it is the positive root of

**(1 − cos²u) T² − 2 cos u (Re λ − cos u) T − |λ − cos u|² = 0 ,  |λ − cos u|² = (Re λ − cos u)² + (Im λ)² ,**

that is, in the numerically stable rationalised form,

**T(u) = |λ − cos u|² / [ cos u (cos u − Re λ) + √( cos²u (Re λ − cos u)² + sin²u · |λ − cos u|² ) ] .**

T is strictly decreasing on [φ, π], and both endpoints are exact:

**T(φ) = |Im λ| / √(1 − Re²λ) = T₂ ,   T(π) = |1 + λ|² / (2(1 + Re λ)) = M\* .**

For u ≥ π, T(u) = M\*, because the arc is the whole circle and the constraint is vacuous.

Proof. Split ν into even and odd parts under θ ↦ −θ. Since cos is even and sin is odd, ∫cos θ dν = ∫cos θ dν_even = Re λ and ∫ sin θ dν = ∫ sin θ dν_odd = Im λ, while TV(ν, ν̌) = ‖ν_odd‖. Feasibility of the real part requires Re λ ≥ min_{|θ|≤u} cos θ = cos u, which is Theorem M61.14 restated on the arc. For the minimisation: for a symmetric even part carrying mass w_i at each of ±θ_i, an odd part supported there can carry at most w_i of total variation and contributes w_i sin θ_i to Im λ, so the odd-mass efficiency at angle θ is sin θ. The linear program is therefore solved by two symmetric atom pairs — one at the most negative available cosine, θ = u, supplying the real part, and one at the angle θ₁ carrying all the odd mass — with the optimum at the point where the available mass exactly saturates the required odd mass:

w = (Re λ − cos u)/(cos θ₁ − cos u) = T = |Im λ| / sin θ₁ .

Eliminating θ₁ between sin θ₁ = |Im λ|/T and cos θ₁ = cos u + (Re λ − cos u)/T via sin² + cos² = 1 gives the displayed quadratic. At u = φ the coefficient Re λ − cos u vanishes and the quadratic collapses to sin²φ·T² = (Im λ)², i.e. T = T₂; at u = π the leading coefficient vanishes and the linear equation gives T = M\*. ∎

Certified two ways: the quadratic residual is below 10⁻⁴⁵ at fifty digits on a five-point grid, and the closed form agrees with an independent arc-restricted 1501-atom linear program at u = 2.3, 2.6, 2.9 to better than 5 × 10⁻⁶, the LP discretisation scale (rows P7–P8). Monotonicity verified on a 401-point sweep (row P11).

Table 21.1. The arc-asymmetry function. The corpus sits at the **top** row.

| u = 2c·ε_max | T(u) | reading |
|---|---|---|
| φ = 2.172948379550106 | **0.835381287313630** = T₂ | minimal phase; forced, no freedom |
| 2.2 | 0.832310663146104 | |
| 2.3 | 0.820879049329285 | |
| 2.4 | 0.809606714156661 | |
| 2.6 | 0.789157930099116 | |
| 2.8 | 0.773814575765010 | |
| 2.9 | 0.768607418482874 | |
| 3.0 | 0.765166432138395 | |
| π = 3.141592653589793 | **0.763362818245964** = M\* | full circle; the ZS-M60 bound |

### 21.2 Five consequences

**(i) T₂ and M\* are one object.** The corpus has been carrying two numbers for what is a single strictly decreasing function of one physical parameter. The "dimension gap" T₂ − M\* = 0.072018469067666 is the total variation of T over its whole domain.

**(ii) M\*-saturation costs a specific phase.** T(u) = M\* requires u ≥ π, i.e. **c ≥ π/2 = 1.570796326794897**, which is 1.4458 times the minimal phase c\*. The v1.0 statement "M\*-saturation requires dim ℋ_E ≥ 4" is thereby replaced by a statement with physical content: M\*-saturation requires an accumulated phase 45% above the floor (row P12).

**(iii) Theorem M61.4 becomes a corollary.** On a carrier of dimension ≤ 3 with det V = +1, Theorem M61.4's proof shows the only complex-admitting spectrum is a single conjugate pair at ±φ — that is, the arc is exactly minimal, u = φ — and therefore T = T(φ) = T₂. The carrier-dimension statement and the arc statement are two routes to the same endpoint.

**(iv) T₂ no longer depends on det V = +1.** This is the robustness gain. v1.0 called Theorem M61.2(iii) "the engine" and gate F-M61.2 made the whole of §5 collapse to M\* if a counterexample were found. Under Theorem M61.15 the bound T₂ follows from the vertex form and the field range alone. **Even if Theorem M61.2 fell, T₂ would stand.** F-M61.2's consequence clause is corrected accordingly in §12.

**(v) The external generalisation the audit asked for is now natural.** T(u) is the arc-restricted case of the M61.11 problem, and the pair (M\*(a), T(u)) suggests the two-parameter family

**M\*(a; u) := inf { TV(ν, ν̌) : supp ν ⊆ [−u, u], ∫ e^{iθ}dν = a } ,**

of which M61.11 is u = π and Theorem M61.15 is a = λ. Deliverable **D-M61-ARC** registers the general closed form; the derivation above generalises verbatim with Re λ, Im λ replaced by x, y, so the quadratic becomes (1 − cos²u)T² − 2cos u (x − cos u)T − |a − cos u|² = 0 whenever |x| + |y| > 1 and the constraint is active. Confirming the inner-diamond branch and the feasibility boundary in general is the only work left, and it is stated here rather than claimed.

---

## §22. The factorised forward gates — FWD-R and FWD-I

The audit's second route: do not ask one mechanism to deliver two numbers. §§19–21 make the factorisation exact, because Theorem M61.13 separates the two real equations onto disjoint data.

### 22.1 FWD-R — the dynamics gate, a one-sided inequality

**Target.** A target-blind derivation from the repaired S14 action of the accumulated phase c = τg and the support radius ε_max of the boundary law, hence of the effective seam arc u = 2cε_max.

**Gate.** By Theorem M61.14,

**u_S14 ≥ φ = 2.172948379550106 ,  equivalently  ½ Tr V = Re a = Re λ = −0.566417330285464 is reachable only if c_S14 ≥ c\*/ε_max .**

**Why this is a prediction and not a fit.** It is an **inequality on a single real number**, and it is one-sided. A derived c below the floor kills the graded bridge outright, and *no* choice of boundary law can rescue it — verified by exhaustive search over 4000 random laws at c = 0.95 c\*, none of which reaches Re λ (row P13). A single target-blind number is therefore sufficient to refute the model. That is positive evidential content, and it is the first such content this line has had.

**Status:** OPEN. `[TESTABLE]` — the falsification protocol is: derive c_S14, compare with c\*/ε_max, and if c_S14 < c\*/ε_max invoke gate F-M61.25.

### 22.2 FWD-I — the boundary gate, a single equality

**Target.** A target-blind derivation of the ε-marginal P of the S14 boundary process, and from it the seam asymmetry D = TV(P, P̌).

**Gate.** By Theorem M61.15, D_S14 ≥ T(u_S14). If in addition the minimal-phase / vacuum-supported case holds, the gate sharpens to the single equality of Theorem M61.17,

**|⟨ε⟩|_S14 = T₂ = 0.835381287313630 ,**

with the falsification sensitivity computed in §24.2.

**Status:** OPEN. `[TESTABLE]`.

### 22.3 Why the two gates escape the ZS-M56.7 trap

ZS-M56 Theorem M56.7 voids a two-parameter fit against two constraints. The trap is avoided here because:

1. The two gates constrain **disjoint** data. FWD-R constrains only the dynamics — the phase and the support radius. FWD-I constrains only the boundary law. Neither derivation may reference the other's output.
2. Neither may reference λ. The comparison happens **once**, after both derivations are locked.
3. FWD-R is an **inequality**, so it is refutable by a single number without any partner. It has evidential content on its own, which is exactly what a two-for-two fit does not.
4. The residual degrees of freedom are counted before, not after: two derived reals against two constraints, but with **one constraint an inequality**, so the system is over-determined in the real part and exactly determined in the imaginary part. Passing both is a zero-residual physical prediction.

**Deliverable register.** D-M61-FWD of v1.1 is **split and retired**; FWD-R and FWD-I replace it and are tracked separately. Either alone is publishable: FWD-R passing is a nontrivial structural confirmation; FWD-I passing is the first genuine one-number prediction of the S14 multiplier's imaginary part.

---

## §23. Theorem M61.16 — the divisor on the λ-compatible class

### 23.1 Statement

Call a holonomy family θ ↦ (V(θ), ρ_E(θ)) **λ-compatible in the real part** if Re a(θ) = Re λ for all θ. By Theorem M61.13 this holds whenever the holonomy acts on ε̂ by conjugation — rotating the seam axis without changing spec ε̂ — and the accumulated phase c is θ-independent, since then Re a = ∫cos(2cε)dP is a holonomy invariant.

**Theorem M61.16 (Empty Divisor on the λ-Compatible Class). [PROVEN].** On any λ-compatible family,

**|a(θ)| ≥ |Re a(θ)| = |Re λ| = 0.566417330285464 > 0  for every θ ,**

so the physical anchor divisor is empty. In particular D_phys = 0 **without** any general-position hypothesis.

Proof. |a| ≥ |Re a| for any complex number, and Re a = Re λ ≠ 0 by hypothesis. ∎ Verified over 6000 draws on the actual vacuum-supported family with the seam axis rotated through the full holonomy circle: min |a| = |Re λ| to 3.3 × 10⁻¹⁰ (row P14).

**Corollary 23.1 (what the codimension-two locus actually requires).** By Theorem M61.5 a zero needs Tr V = 0, i.e. cos 2c = 0, i.e. **c = π/4 + kπ/2**. The smallest positive value is π/4 = 0.785398163397448, which is **below the universal phase floor c\* = 1.086474189775053** and in any case incompatible with cos 2c = Re λ ≠ 0. **The divisor's zero locus and the λ-compatible class are disjoint** (row P15).

### 23.2 What this does to the v1.1 correction

v1.1 was right to correct v1.0's universal quantifier: the codimension count alone does not exclude non-generic families, and §9's explicit counterexample family — V(θ) = exp(−i(π/2) m̂(θ)·σ) with a fixed state — reaches a = 0 exactly. **That counterexample stands, and v1.2 now explains it:** the family sits at c = π/4, which the phase floor forbids for any realisation of Re λ. It is a legitimate graded relative unitary and it is not λ-compatible.

So the correct final statement is neither v1.0's nor v1.1's:

| Version | Statement | Status |
|---|---|---|
| v1.0 | D_phys = 0 for every family | **wrong** — refuted by the §9 counterexample |
| v1.1 | D_phys = 0 for families in general position, (H-GP) required | **true but weak** |
| **v1.2** | **D_phys = 0 for every λ-compatible family, unconditionally; (H-GP) is needed only off that class, where the question is physically empty** | **CLOSED-NEGATIVE** |

ZS-M59 deliverable (3) is thereby **fully discharged** for the physical process, and gate F-M61.18 is narrowed to families that are not λ-compatible. The 8000-draw witness of block I is retired as a research instrument and retained only as a regression row, per the audit's recommendation that random-family sampling has no remaining research value here.

---

## §24. Theorem M61.17 — codimension-1 reachability and the one-number gate

### 24.1 The clock freedom does not rescue the model

ZS-M57 Theorem M57.T.1 shows the slab duration is not fixed by the action, so c is free. The natural worry is that a free c makes any λ reachable and the model unfalsifiable. It does not.

**Theorem M61.17 (Codimension-1 Reachability). [PROVEN].** Fix a target-blind boundary law P and let the accumulated phase range over c ≥ 0. The attainable set of multipliers is the curve

**C_P = { Φ_P(−2c) : c ≥ 0 } ⊂ 𝔻̄ ,**

of real dimension one. Hence λ ∈ C_P is a codimension-one condition on P. In the minimal-phase / vacuum-supported case P = p₋δ₋₁ + p₊δ₊₁ with m := |⟨ε⟩|, the curve is the ellipse

**C_m = { (cos 2c, −m sin 2c) : c ≥ 0 } ,  semi-axes 1 and m,**

and λ ∈ C_m **if and only if**

**m = |Im λ| / √(1 − Re²λ) = T₂ = 0.835381287313630 exactly.**

Proof. C_P is the image of a one-real-parameter family, hence at most one-dimensional. For the two-atom law, Re a = cos 2c and Im a = −m sin 2c, so a lies on the ellipse x²+ y²/m² = 1. Imposing (Re λ, Im λ) gives cos 2c = Re λ and sin 2c = −Im λ/m; squaring and adding, Re²λ + (Im λ)²/m² = 1, i.e. m² = (Im λ)²/(1 − Re²λ). ∎ Verified numerically: the minimum over c of |a(c) − λ| is 2.8 × 10⁻⁶ (the grid scale) at m = T₂ and 6.0 × 10⁻⁴ at m = 1.001 T₂ (rows P16–P17).

**This is the sharpest reduction the line has achieved.** The clock debt does not weaken the bridge; it moves the entire content of the bridge onto **one real number**, ⟨ε⟩, which the boundary condition must supply target-blind. FWD-I is that gate.

### 24.2 The falsification sensitivity, in closed form

Differentiating the distance from λ to the ellipse C_m with respect to m at m = T₂ gives the displacement per unit error in the boundary asymmetry. The ellipse point moves vertically by |sin 2c\*|·δm = √(1 − Re²λ)·δm, and the perpendicular component is that times the vertical component of the unit normal, giving

**d dist / d m |_{m = T₂} = (1 − Re²λ) / √( T₂² Re²λ + 1 − Re²λ ) = 0.714693412649626 .**

So a relative error of 0.1% in |⟨ε⟩| displaces the multiplier by 6.0 × 10⁻⁴, which is 0.067% of |λ|. Verified against the numerical minimum to 2.4 × 10⁻⁴ (row P17). **A forward derivation of ⟨ε⟩ good to three significant figures already tests the bridge at the 10⁻³ level.**

### 24.3 The pre-registered alternative outcome

The audit's sixth route asks that the negative outcome be held open as a theorem rather than treated as a failure. It is registered here in the form it would take.

**Conjecture-shaped deliverable D-M61-NONID (S14 Action-to-Channel Non-Identifiability).** *If* no target-blind derivation of the ε-marginal exists — i.e. if the declared S14 data, symmetries, gauge fixing and boundary conditions determine the boundary process only up to a family of ε-marginals of positive dimension — *then* the attainable multiplier set is of dimension ≥ 2, λ is not selected, and the correct conclusion is:

> The declared ZS-S14 data determine an admissible **family** of QND coherence multipliers and select no unique complex value. λ therefore requires a selection axiom or an additional physical input that ZS-S14 does not contain.

**Status: [OPEN], pre-registered.** This is a strong negative result and it is publishable; §22's gates are constructed so that either outcome is reached by the same calculation. Gate F-M61.30 fires on any presentation of a positive closure that has not passed both FWD-R and FWD-I target-blind, precisely to keep this branch available rather than fitting around it.

---

## §25. Reduction R1 — the exact seam Ward identity replacing all-orders (F2)

The audit's fourth route: stop checking (F2) order by order. (F2) is the exact statement [U, J_S ⊗ J_E] = 0, so it should be closed as an exact change of variables, not approached as a perturbative limit.

**Reduction R1. [PROVEN as a reduction; the five items are NOT discharged here].** Let σ denote the seam involution acting on the field content of the repaired S14 action, with σ: ε ↦ −ε. Then (F2) holds if and only if the generating functional satisfies the exact Ward identity Z[σJ] = Z[J], and that identity holds if and only if all five of the following hold. Each is a **finite** statement.

| # | Item | Status after R0 |
|---|---|---|
| W1 | **Classical invariance** S[σΦ] = S[Φ]. | The ZS-A3 potential (ε²−1)² and the non-minimal coupling (1 + **A**ε²)R are even in ε; the kinetic term is quadratic. **Holds** for the ε sector; the remaining check is that no term of the repaired action is linear in ε. |
| W2 | **Measure invariance.** For a *linear* involution σ on a real bosonic field space, the Jacobian is det σ = (−1)^{n_−} and its modulus is 1. Hence ∏dΦ is invariant with no anomaly. | **Holds automatically.** This is the item an order-by-order treatment can never finish and an exact treatment closes in one line. |
| W3 | **Gauge-fixing and Faddeev–Popov sector.** σ acts on ε only. Under R0, ε lies in the multiplicity-one D₃-trivial component and is a colour singlet; if it is also an SU(2)×U(1) singlet, then σ commutes with every gauge transformation and the gauge-fixing functional, the FP determinant and the BRST charge are σ-invariant. | **Holds iff ε is a gauge singlet** — a single representation-theoretic check on the repaired action, not a perturbative one. |
| W4 | **Regulator.** σ is linear and commutes with □, so any spectral regulator of the kinetic operator is σ-invariant; dimensional regularisation acts on Lorentz indices only. The only obstruction is a **global (’t Hooft) ℤ₂ anomaly**, which for a real scalar in four dimensions requires a fermion bilinear odd under σ — i.e. a Yukawa term linear in ε. | **Holds unless the repaired Yukawa sector contains an ε-odd fermion bilinear.** One finite check on the ZS-M10 Yukawa invariant. |
| W5 | **Boundary conditions and boundary counterterms.** ε(r_H) = 0 is σ-invariant. ε(∞) = +1 is **not**: σ maps it to −1. The boundary condition at infinity therefore breaks σ, spontaneously and by construction. | **Fails — and must.** |

**The structural conclusion, which is the point of the reduction.** Items W1–W4 concern the **dynamics**; item W5 concerns the **state**. If W1–W4 hold, the seam ℤ₂ is an exact symmetry of the action, the measure, the gauge-fixing sector and the regulator, and the *only* place the symmetry is broken is the boundary condition at infinity. That is precisely the structure ZS-M57 Theorem M57.P′ and §19.3 require: **a symmetric dynamics with an invariant state gives a real multiplier, so Im λ ≠ 0 forces the breaking into the state, and W5 is exactly where the corpus puts it.** Three independent routes — the collision lemma, the characteristic-function decomposition, and the Ward identity — agree on where the phase must come from. That convergence is the strongest structural evidence this paper has, and it is evidence about *location*, not about *value*.

**What R1 is and is not.** It is a retyping of the (F2) debt from an infinite perturbative check to a finite five-item checklist, of which two (W2, and W5 as a controlled breaking) are already settled and three (W1's linearity clause, W3's singlet clause, W4's anomaly clause) are single finite computations on the repaired action. **It is not a proof of (F2)**, and NC-M61.3 stands unchanged. Deliverable **D-M61-WARD** registers the three remaining items. Gate F-M61.16's consequence clause is unchanged; gate **F-M61.29** is added against presenting R1 as a discharge of (F2).

**A note on the BRST route.** W3 and W4 both touch the ghost sector, and ZS-M56's earlier dismissal of a BRST ghost–antighost graded carrier was withdrawn as overreach (ZS-M57 §17, debt 2, files not loaded). R1 makes the connection explicit: the same singlet-and-anomaly analysis that discharges (F2) also decides whether the ghost sector can carry the seam grading. **One calculation, two debts.** This is registered as an observation, not a claim; the relevant files remain unloaded and rule R6 forbids reasoning about them second-hand.

---

## §26. Externalisation plan

The v1.1 audit's final recommendation is that the corpus canonical manuscript must not be submitted as-is, per the manuscript protocol's separation of internal audit log from external scientific paper. The plan is registered here and is **not** executed in this version.

**External paper 1 — the mathematics, no Z-Spin input.**
Working title: *Minimal reflection asymmetry of circle measures with prescribed barycentre, and an arc-width obstruction.*
Body: Theorem M61.11 (the closed form M\*(a) with its inner-diamond/outer-domain split), Theorem M61.15 (the arc-restricted function T(u) and its closed form), and the general two-parameter family M\*(a; u) of §21.2(v). Application section: the symmetry-constrained dilation reading of Theorem M61.4. Prior art: resource theory of asymmetry, trace-norm asymmetry measures, moment-problem atom reduction — cited by locator, which requires D-M61-PRIOR first.

**External paper 2 — the physical application.**
Working title: *A phase floor and an asymmetry floor for symmetric quantum non-demolition dephasing.*
Body: Theorem M61.13 (characteristic-function form), Theorem M61.14 (universal phase floor with its equality case), Theorem M61.16 (empty divisor on the compatible class), Theorem M61.17 (codimension-1 reachability). The Z-Spin S14 model appears as the final application section, with physical selection stated as open.

**Moved to Supplement in both:** the fourteen-row correction register, the 147-row ledger, the internal gate numbering, the v1.0 and v1.1 failure history compressed to one paragraph, the corpus dependency census, all SHA values and run logs.

**The one-sentence external abstract.** *A ℤ₂-graded relative-unitary constraint together with a bounded interaction range imposes two floors on the environment that realises a prescribed complex dephasing multiplier — a lower bound on the accumulated interaction phase and a lower bound on the environmental asymmetry, the latter a strictly decreasing closed-form function of the former — and the unconstrained measure problem admits a closed-form optimum; applied to the Z-Spin S14 boundary model, physical selection of the realisation remains open.*

---

## §27. Conclusion to v1.2

v1.1 removed three overstatements and left the paper honest but static: a classification with two named hypotheses, one material conflict and a single monolithic forward deliverable. v1.2 executed the six routes the audit proposed, and the result is that **the paper is no longer static and is no longer built on the fact it called its engine.**

Three things changed in kind rather than in degree.

**The object was retyped and the conflict dissolved.** The multiplier is the characteristic function of the ε-marginal, always, in every dimension, with no support hypothesis. The anchor at ε = 0 and the bulk at ε = ±1 are the two ends of one interval, and the question "which one" was the wrong question. What replaces it is a price: localising the mediating weight at radius ε_max costs an accumulated phase c ≥ c\*/ε_max, which is 10 c\* at the anchor core. D-M61-VAC is dissolved.

**The two corpus constants turned out to be one function.** T(u) is strictly decreasing on [φ, π] with T(φ) = T₂ and T(π) = M\* both exact. The carrier-dimension theorem is a corollary at the left endpoint, the ZS-M60 bound is the right endpoint, and — the robustness that matters — the derivation never uses det V = +1. The sharpened floor T₂ survives the failure of Theorem M61.2, which v1.0 staked the paper on.

**The bridge became falsifiable by single numbers.** The forward problem is now two independent gates on disjoint data: an inequality on the dynamics, c ≥ c\*/ε_max, refutable by one target-blind number and rescuable by no boundary law; and an equality on the boundary law, |⟨ε⟩| = T₂, with an explicit sensitivity of 0.714693 so that a three-figure derivation already tests the bridge at 10⁻³. The clock debt does not weaken this — Theorem M61.17 shows the clock freedom leaves a one-dimensional attainable curve, so λ is reached only in codimension one. And if the derivation of ⟨ε⟩ turns out not to exist, the pre-registered result is a Non-Identifiability Theorem, which is a strong negative rather than a failure.

**What is still not done, said plainly.** No forward derivation is performed: FWD-R and FWD-I are both OPEN, and the paper contains no target-blind number. (F2) is reduced to three finite checks and is not discharged. The general M\*(a; u) closed form is stated for the active branch and not proved in full. The prior-art search for Theorem M61.11 has not been executed, so its novelty remains NOT_FOUND rather than NEW. And no persistent identifier has been assigned to the artifact, so `FINAL` is unavailable regardless of anything else.

Stated at exact strength. The colour block is repaired. Every graded relative unitary has unit determinant, and nothing load-bearing now depends on that. The multiplier is the characteristic function of the Z-bias marginal. The accumulated phase is bounded below by arccos(Re λ)/(2ε_max), with equality exactly on the extreme support — so the vacuum-supported law is not a hypothesis but the minimal-phase extremum. The minimal seam asymmetry is T(2cε_max), strictly decreasing, pinned at T₂ at the floor and reaching M\* only at c = π/2. The anchor divisor is empty on the whole λ-compatible class, unconditionally. The realising data are unique given λ, and uniqueness given the target is still not derivation of the target. Two gates, two numbers, two possible outcomes, both publishable. **The S14 measurement line does not stop here, and for the first time it knows exactly which two numbers to compute.**

---


---

# Part V — The open items, executed

*Everything in Part V is new in v1.3. It is the result of attempting, item by item, to close the five things v1.2 declared open. **Two closed, one closed negatively, one turned out to fail and is now the sharpest open problem in the paper, and one cannot be closed by computation at all.** The failure is reported first, because it is the most important result in this version.*

---

## §28. Theorem M61.19 — (F2) fails: the Yukawa term is linear in ε

### 28.1 What was attempted, and on what

v1.2's Reduction R1 reduced (F2) from an all-orders perturbative check to five finite items, of which three were registered as deliverable D-M61-WARD: **W1** no term of the repaired action linear in ε, **W3** ε a gauge singlet, **W4** no ε-odd fermion bilinear. v1.3 executes them against the **actual ZS-S14 v2.0 master action**, read directly:

> S_S14 = ∫d⁴x √(−g) { ½M_P²(1 + **A**|H₅|²)R − ½M_P²|D_μH₅|² − V(H₅) − ¼B² − ¼W² − ¼G² + ψ̄ iγ^μD_μψ − **Y₀ T_{i m α} (ψ̄_L)^i (H₅)^m (ψ_R)^α** + h.c. }

with V(H₅) = λ₁|H₅|⁴ + λ₂P₄(H₅) I-invariant, and T the ZS-M10 unique invariant in Hom_I(1, **3** ⊗ **5** ⊗ **3′**).

The computation reconstructs the three A₅ irreps from scratch: the **4** as the orthogonal complement of the trivial in the permutation module on five letters, **3** and **3′** as the two summands of Λ²(**4**), and **5** as the I-isotypic component of Sym²(**4**). All three are verified unitary and character-correct against the A₅ table, the two 5-cycle classes are verified disjoint of size 12, and the multiplicity **dim Hom_I(1, 3 ⊗ 5 ⊗ 3′) = 1** is reproduced from the character integral (45 + 15)/60 — a regression against ZS-M10 Theorem 2.1 (block T, rows T1–T5).

### 28.2 Theorem M61.19 — the isotropy of the Yukawa tensor

**Theorem M61.19 (Yukawa Slot Isotropy). [PROVEN].** Let T ∈ Hom_I(1, **3** ⊗ **5** ⊗ **3′**) be the unique I-invariant tensor, normalised to ‖T‖ = 1, and define the Gram form on the Higgs index,

**G_{mn} := Σ_{i,α} T_{i m α} T_{i n α} .**

Then G is an I-invariant symmetric form on the **5**; since the **5** is I-irreducible, Schur's lemma forces G ∝ δ, and the normalisation gives

**G = δ / 5 ,   hence ‖T · w‖ = 1/√5 = 0.447213595499958 for every unit vector w of the 5.**

**No slot of the 5 can carry zero Yukawa weight.**

Proof. Invariance: G_{mn} transforms in **5** ⊗ **5** under I and is invariant because T is; the invariant symmetric bilinear forms on an irreducible real-type representation are one-dimensional, spanned by δ. The trace fixes the constant: Σ_m G_{mm} = ‖T‖² = 1 over five slots. ∎ Verified: ‖G − δ/5‖ = 3.2 × 10⁻¹⁶ (row T7).

**Cross-check against the corpus.** The per-slot weight 1/5 reproduces ZS-M10 §3's Schur conservation Σσᵢ² = 1/5 exactly (row T10). The corpus already contained this number; what it had not extracted is the consequence.

The D₃-trivial direction v₁ of the **5** is then constructed explicitly — the D₃ subgroup of order 6 is embedded in A₅, its projector on the **5** has rank exactly 1, confirming ZS-S14 Table 2.8's **5** ↓ D₃ = **1** ⊕ **2** ⊕ **2′** — and the decisive contraction evaluated:

**‖ Σ_m T_{i m α} v₁^m ‖ = 1/√5 = 0.447213595499958 ≠ 0 (row T9).**

### 28.3 The consequence: W1 fails

The Yukawa term is **linear in H₅**. If ε — the ZS-A3 Z-bias field with potential V(ε) = (λ_V/4)M_P⁴(ε² − 1)², vacua ε = ±1 and seam action ε ↦ −ε — is the D₃-trivial component of H₅, as ZS-S14 §7.1's hypothesis H_id asserts and as ZS-M61 §7.1 uses, then S_S14 contains the term

**− Y₀ (T · v₁)_{iα} (ψ̄_L)^i (ψ_R)^α · ε + h.c. ,  with coefficient weight exactly 1/√5 of ‖T‖ ,**

which is **odd** under σ: ε ↦ −ε. Therefore **S[σΦ] ≠ S[Φ]: item W1 of Reduction R1 FAILS, and it fails by a theorem rather than by an accident of the tensor's numerical values.**

Three escape routes were checked and all three are blocked.

**(a) Extend σ to the fermions.** Accompanying σ with ψ_R ↦ −ψ_R makes the ε-linear term even — but it simultaneously makes the *doublet* Yukawa term odd, and the doublet term is the one that generates every fermion mass from ⟨H⟩. One cannot flip the right-handed fields for one slot of H₅ and not for the others.

**(b) Extend σ to all of H₅.** The operator σ = diag(−1, +1, +1, +1, +1) in the D₃-adapted basis is an involution with det σ = −1 that **commutes with D₃ but not with I**: the commutator residual is ‖[σ, ρ₅(g)]‖ = 1.603 at its maximum over the 60 group elements (row T11). σ is therefore not an automorphism of the I-invariant structure, and the I-invariant quartic sector — verified two-dimensional, reproducing ZS-S14's V = λ₁|H₅|⁴ + λ₂P₄ (row T12) — has no reason to be σ-even.

**(c) Hope the slot vanishes.** Theorem M61.19 forbids it, for every I-invariant T, at every normalisation.

### 28.4 An upstream conflict discovered in passing: what is Φ?

W3 was expected to be the easy item. It is not, because **ZS-S14 v2.0 asserts two incompatible identifications of Φ**:

| Locator | Statement | Consequence for W3 |
|---|---|---|
| ZS-S14 §7.1, Hypothesis H_id | Φ = Φ_{D₃-1}, the **D₃-trivial** one-dimensional component of H₅ | ε is a gauge singlet: q₅ acts trivially on D₃-1, T^a₂ acts on D₃-2, λ^a₃ on D₃-2′. **W3 HOLDS.** |
| ZS-S14 §7.5, Theorem S14.D.4 Step 2 | "Φ is identified with the **neutral Higgs component within the D₃-2 weak doublet** of H₅" | ε sits inside an SU(2)_L doublet, so σ does not commute with SU(2)_L. **W3 FAILS.** |

The second reading is what makes Y_Φ = q_Φ × (1/Z) = +1/2 = Y_H work; the first is what ZS-M61 §7.1 relies on when it calls the D₃-trivial component "unambiguous under R0". They cannot both be right. **Registered as upstream debt D-S14-PHI. [OPEN].** Not this paper's to fix; recorded so that neither reading is used silently. This is the fourth time in the M56–M61 line that a decisive question has turned out to be "does this operator act on that object at all?" — the pattern ZS-M57's rule R10′ was written for.

### 28.5 The dichotomy, and what it costs

Combining §28.3 and §28.4:

> **Either** ε is a component of H₅ — and then the Yukawa term is linear in ε, W1 fails, (F2) fails at the classical level, and gate **F-M61.16 fires**: the whole graded chain, ZS-M60 included, is inapplicable to the physical S14 process;
>
> **or** ε is a field outside H₅ — and then ZS-S14 does not supply the seam-odd vertex H_int = g Z_path ⊗ ε̂ that ZS-M61 §7.1 uses, so that vertex is **not action-derived**, and §§7–8 lose their claim to be about S_S14 at all.

Both branches are damaging and they are damaging in different places. **v1.3 does not choose between them**, because choosing requires ZS-A3 and ZS-F1 to state what ε is relative to H₅, and neither is loaded here (rule R6).

**Status of D-M61-WARD: NOT DISCHARGED — WORSE.** v1.2 registered three finite items expecting them to close. W2 holds. W3 is upstream-ambiguous. **W1 fails on the H_id branch.** The honest statement is that (F2) is no longer merely unproved: on the corpus's own identification of Φ it is **false at the classical level**, and the alternative costs the action-derivation of the vertex.

**Gate F-M61.32 (new).** Fires on any use of (F2) as an assumption after v1.3 without stating which branch of the §28.5 dichotomy is taken.

### 28.6 What survives, precisely

This is the load-bearing question and it has a clean answer, because v1.2's §21.2(iv) already removed the paper's single-point dependency.

| Result | Uses (F2)? | Uses the vertex form? | Survives §28? |
|---|---|---|---|
| Thm M61.1 / R0, colour repair | no | no | **yes** |
| Thm M61.11, M\*(a) closed form | no | no | **yes** |
| Thm M61.20, M\*(a; u) general form | no | no | **yes** |
| Thm M61.3, arc obstruction | no | no | **yes** |
| Thm M61.2, det V = +1 | yes (via U₁ = J_E U₀ J_E) | no | conditional |
| Thm M61.4, carrier dimension | yes | no | conditional |
| Thm M61.5, real-part rigidity | yes | no | conditional |
| Thm M61.13, a = Φ_P(−2c) | yes | yes | conditional |
| Thm M61.14, phase floor | yes | yes | conditional |
| Thm M61.15, T(u) and T₂ | yes | yes | conditional |
| Thm M61.16, empty divisor | yes | yes | conditional |
| Thm M61.17, reachability | yes | yes | conditional |

**Four results are unconditional mathematics and are unaffected.** Everything about the *physical* S14 bridge is now conditional on resolving §28.5, which is exactly where it should be. The paper's most defensible content — §10 and §29 — never touched (F2).

---

## §29. Theorem M61.20 — D-M61-ARC closed: the general function M\*(a; u)

### 29.1 Statement

**Theorem M61.20 (General Arc-Restricted Minimal Asymmetry). [PROVEN].** For a target a = x + iy in the closed unit disc, with y ≥ 0 without loss of generality, and for u ∈ (0, π], let

**M\*(a; u) := inf { TV(ν, ν̌) : ν a probability measure on [−u, u], ∫ e^{iθ} dν = a } .**

Then M\*(a; u) < ∞ **if and only if** cos u ≤ x ≤ 1, and where finite it equals

**M\*(a; u) = min { y / sin θ₁ : θ₂ ∈ {0, u}, θ₁ ∈ Θ(θ₂), w(θ₁, θ₂) ≥ y/sin θ₁ } ,**

**w(θ₁, θ₂) = (x − cos θ₂) / (cos θ₁ − cos θ₂) ∈ [0, 1] ,**

where the candidate set Θ(θ₂) consists of exactly three angles: **π/2**, the arc endpoint **u**, and the **tangency angle** solving y(cos θ₁ − cos θ₂) = (x − cos θ₂) sin θ₁, which in closed form is

- θ₁ = 2 arctan((1 − x)/y) for θ₂ = 0;
- θ₁ = 2 arctan(y/(1 + x)) for θ₂ = π;
- θ₁ = arccos( y cos θ₂ / √(y² + (x − cos θ₂)²) ) − arctan( (x − cos θ₂)/y ) otherwise.

The optimum is always attained on at most **two symmetric atom pairs**.

Proof. Decompose ν = ν_even + ν_odd under θ ↦ −θ. Because cos is even and sin is odd, ∫cos θ dν = ∫cos θ dν_even = x and ∫sin θ dν = ∫sin θ dν_odd = y, while TV(ν, ν̌) = ‖ν_odd‖. Feasibility of the real part requires x ≥ min_{|θ|≤u} cos θ = cos u — this is Theorem M61.14 on the arc. For the minimisation: a symmetric even part carrying mass w_k at each of ±θ_k permits an odd part of total variation at most w_k there, contributing w_k sin θ_k to y; hence the odd-mass efficiency at angle θ is sin θ, and the linear program is solved greedily. The extreme points of the feasible set of symmetric even parts with a prescribed mean cosine are supported on two symmetric pairs, one of which must sit at an extreme of cos θ on the arc, i.e. at θ = 0 or θ = u. Optimality in θ₁ then occurs either at the unconstrained maximum of sin θ₁ (θ₁ = π/2), at the arc boundary (θ₁ = u), or where the mass constraint binds (the tangency angle). Eliminating θ₁ at tangency via sin θ₁ = y/T and cos θ₁ = cos θ₂ + (x − cos θ₂)/T gives the quadratic of Theorem M61.15 as the θ₂ = u case. ∎

### 29.2 Certification and the four boundary cases

Certified against an independent arc-restricted 1201-atom linear program on **46 (a, u) pairs** spanning both branches, both signs of x, the inner diamond, and u above and below π/2: worst deviation **4.2 × 10⁻⁶**, which is the LP discretisation scale, and **zero feasibility mismatches** — the closed form and the LP agree on which (a, u) admit a measure at all (block U, rows U1–U2).

Four special cases fall out exactly (rows U3–U4):

| Case | Reduces to | Value at a = λ |
|---|---|---|
| u = π, \|x\| + \|y\| > 1 | Theorem M61.11 outer branch, min_s \|1 − sa\|²/(2(1 − sx)) | M\* = 0.763362818245964 |
| u = π, \|x\| + \|y\| ≤ 1 | Theorem M61.11 inner diamond, \|y\| | — |
| u = φ = arccos x | Theorem M61.15 left endpoint | T₂ = 0.835381287313630 |
| a = λ, φ ≤ u ≤ π | Theorem M61.15, the strictly decreasing T(u) | T(u) |

**Deliverable D-M61-ARC is CLOSED.** Theorems M61.11 and M61.15 are the two boundary cases of one two-parameter object, and the inner-diamond branch survives the arc restriction whenever u ≥ π/2.

### 29.3 What this is worth outside the corpus

This is the strongest stand-alone mathematics the paper now contains, and it is stated without a single Z-Spin term: *the minimum reflection asymmetry, in total variation, of a probability measure on an arc of prescribed half-width with a prescribed first trigonometric moment, in closed form, with the extremal measure supported on at most two symmetric pairs.* The arc parameter is what makes it more than a curiosity: it converts a fixed number into a monotone trade-off between interaction phase and environmental asymmetry.

---

## §30. Theorem M61.21 — FWD-I attempted, and closed negatively on the canonical branch

### 30.1 The first target-blind number in the programme

FWD-I asks for the ε-marginal of the S14 boundary process, derived without looking at λ. The full derivation needs the boundary state, which is not available. But one thing **is** available: the ZS-A3 kink profile ε(r) = tanh((r − r_H)/L_⊥) together with the natural radial weights that field theory supplies. Pushing those forward under ε(·) gives an ε-marginal, and its mean is a pure number — **no λ enters anywhere.**

**Theorem M61.21 (Kink-Weight Family). [PROVEN].** For the radial weight w ∝ (1 − ε²)^p on ε ∈ [0, 1] — the pushforward under the tanh kink of the radial weights indexed by p — the mean bias is

**⟨ε⟩(p) = ∫₀¹ ε(1−ε²)^p dε / ∫₀¹ (1−ε²)^p dε = Γ(p + 3/2) / ( √π · Γ(p + 2) ) .**

Proof. The numerator is 1/(2(p+1)); the denominator is (√π/2)Γ(p+1)/Γ(p+3/2). Dividing and using Γ(p+2) = (p+1)Γ(p+1) gives the stated form. ∎ Checked against quadrature to 10⁻⁶ (row V1).

### 30.2 The three canonical weights, and the verdict

Each of the three weights that the ZS-A3 kink actually supplies is a specific p, and each gives an **exact rational** (rows V2–V4):

| Radial weight | p | ⟨ε⟩ exactly | vs T₂ = 0.835381287313630 |
|---|---|---|---|
| arclength, \|dε/dr\| dr | 0 | **1/2** = 0.500000 | **below** |
| kink energy density, (dε/dr)² dr | 1 | **3/8** = 0.375000 | **below** |
| ZS-A3 potential weight, V(ε) dr | 2 | **5/16** = 0.312500 | **below** |

The exponent required to reach T₂ is

**p\* = −0.847671833659076 < 0 ,**

so the boundary weight would have to **diverge integrably at the vacuum |ε| → 1** — it must pile up on the bulk vacuum, not on the anchor and not smoothly across the profile. The deficit at the physically most natural weight, the kink energy density, is

**T₂ − 3/8 = 0.460381287313630 ,**

which is not a small correction: it is 55% of the required value.

### 30.3 Status: CLOSED-NEGATIVE on the canonical branch

**FWD-I fails for every canonical kink weight.** This is the first genuinely target-blind computation in the programme and its outcome is negative. Under the pre-registration of §22 that is a result, not a disappointment: it eliminates a named sub-branch of the forward problem by a one-number comparison, exactly as designed.

**What it does not do.** The kink-weight family is a **model** of the ε-marginal — hypothesis **(H-KINK-WEIGHT)** — and not a derivation of it from S_S14. Three loopholes remain, and they are the honest residual of FWD-I:

1. The boundary-process ε-marginal is a *quantum* spectral measure in the state ρ_E, and need not be the classical radial weight of the static kink.
2. A dynamical boundary process could weight the profile by something outside the (1 − ε²)^p family — the required p\* < 0 says exactly what such a weight must look like: edge-concentrated at the vacuum.
3. §28.5 may make the whole vertex non-action-derived, in which case FWD-I is not the right question.

**FWD-I therefore remains OPEN as a whole and CLOSED-NEGATIVE on the canonical-weight sub-branch.** Gate **F-M61.33 (new)** fires on any presentation of a canonical kink weight as satisfying FWD-I.

### 30.4 FWD-R: the conditional chain, still open

FWD-R needs c = τg target-blind, and by ZS-M57 Theorem M57.T.1 that requires the ZS-Q19 metric clock or an action-selected primitive event step. Neither exists. **FWD-R remains OPEN.**

What v1.3 adds is the numerical chain the gate will be run against (row V8):

| Support radius | Interpretation | Phase floor c ≥ c\*/ε_max |
|---|---|---|
| ε_max = 1 | bulk vacuum | 1.086474189775053 |
| ε_max = T₂ | phase-capable shell of §8.2 | **1.300572811810129** |
| ε_max = 0.5 | mid-profile | 2.172948379550106 |
| ε_max = 0.1 | anchor core | 10.864741897750529 |

The second row is worth naming: **c\*/T₂ = 1.300572811810129** is the floor consistent with the paper's own phase-capable shell, and it is the number a forward derivation of c should be compared against first.

### 30.5 A consistency observation, refused as evidence

The three canonical weights give ⟨ε⟩ = 1/2, 3/8, 5/16 — all simple rationals, all below T₂, and monotone in p. It is tempting to read the ordering as meaningful. It is not: ⟨ε⟩(p) is strictly decreasing in p for elementary reasons, and no corpus quantity appears anywhere in the family. Recorded here so that the ordering cannot later be presented as structure.

---

## §31. D-M61-PRIOR executed

### 31.1 What was searched, and what was found

A targeted external search was run on the three literatures that Theorems M61.11 and M61.20 border: minimal total-variation problems with moment constraints; the resource theory of asymmetry and trace-norm asymmetry measures; and extremal-measure closed forms under total-variation constraints.

**Result: NOT_FOUND retained, now with locators.** The adjacent prior art is real, established and must be cited:

- the Marvian–Spekkens resource theory of asymmetry, already in the reference list;
- **trace-norm asymmetry with commutator lower bounds** — a lower bound of the form A_Tr(ρ; K) ≥ sup_X |Tr([X, K]ρ)|/2 (arXiv:2309.09159, Lemma 1);
- **closed-form extremal measures under total-variation constraints** in stochastic control (arXiv:1301.4763; arXiv:1402.1009), where the maximising signed measure is given explicitly.

**None of them states the piecewise closed form of Theorem M61.11, and none states the arc-restricted form of Theorem M61.20.**

### 31.2 The closest structural relative, and how the corpus result differs

The trace-norm asymmetry lower bound is the same *kind* of statement as ZS-M60.22's exact obstruction Im a = (1/2i)Tr[(ρ − JρJ)V]: both bound an asymmetry by an expectation of a commutator. The differences are that the corpus results are **exact rather than variational**, are **minimised over the measure rather than bounded for a fixed state**, and carry the **arc/dimension parameter** that produces a monotone family rather than a single inequality. That is a defensible statement of contribution and it is what an external referee should be handed.

### 31.3 Status

**D-M61-PRIOR is EXECUTED, not closed.** The search is now a stated, scoped, criticisable act rather than an absence, which is the difference the deliverable asked for. Novelty status remains **NOT_FOUND**, gate F-M61.23 stands, and a systematic search — a full database sweep rather than a targeted one — is what would be needed to move it to NEW. That is recorded as **D-M61-PRIOR-2** and is not performed here.

---

## §32. DOI and release status — the one item computation cannot touch

No amount of derivation assigns a persistent identifier. What v1.3 does is reduce the item to a single manual action:

- **`CITATION.cff`** and **`zenodo.json`** now ship with the artifact, complete with title, authors, version, license, keywords and description.
- The deposit procedure is one step: reserve the DOI, deposit `zs_m61_verify_v1_3.py`, `zs_m61_verify_v1_3.json`, `figures.json`, `requirements.txt`, `RUN.md`, `CITATION.cff`, then write the DOI back into §18.1 and into `CITATION.cff`.

**Until the DOI exists the release is NOT YET PUBLICLY CERTIFIED and `FINAL` may not be applied.** This is the only release-blocking item that remains from v1.2's list, and it is now blocked on a human action rather than on unfinished work. §18.2(7), the artifact-overwrite hazard, is **closed**: the v1.3 script derives its output filenames from its own basename, so a guard-test variant can no longer overwrite a release ledger.

---

## §33. Conclusion to v1.3

v1.3 set out to close five open items and the result is not symmetric.

**Closed.** D-M61-ARC: the general M\*(a; u) is in closed form with its feasibility boundary, its inner-diamond branch and its two-atom extremal structure, certified on 46 (a, u) pairs. §18.2(7): the artifact can no longer overwrite itself. D-M61-PRIOR: executed, with locators, NOT_FOUND retained honestly.

**Closed negatively, which is also closed.** FWD-I on the canonical-weight branch. The kink energy density gives ⟨ε⟩ = 3/8, the arclength weight 1/2, the potential weight 5/16, and T₂ needs 0.8354. This is the programme's first target-blind number and it says no. The required exponent p\* = −0.8477 states precisely what a surviving boundary weight must look like: edge-concentrated at the vacuum.

**Not closed, and worse than open.** D-M61-WARD. The attempt to discharge (F2)'s three finite items found instead that one of them **fails**, by a theorem: the ZS-S14 Yukawa term is linear in H₅, and by isotropy of the unique I-invariant tensor every slot of the **5** carries exactly 1/5 of its norm, so the D₃-trivial slot — the slot ZS-S14's own H_id identifies with the Z-bias field — cannot have zero weight. σ: ε ↦ −ε is therefore not a symmetry of the action, the fermion extension is blocked because it would flip the doublet Yukawa, and σ extended to H₅ does not commute with I. In passing, ZS-S14 v2.0 turned out to assert two incompatible identifications of Φ, which is why W3 cannot be settled either.

**Not closable here.** The DOI.

**What this does to the paper.** It moves the physical bridge from *conditional on an unproved assumption* to *conditional on resolving an explicit dichotomy in which one branch is already falsified*. That is worse for the bridge and better for the paper, because it is the truth and because v1.2's §21.2(iv) had already removed the single-point dependency that would have made it fatal: **T₂ does not rest on det V = +1, and Theorems M61.11 and M61.20 do not rest on anything Z-Spin at all.** Four results are unconditional mathematics; §28.6 lists exactly which.

The honest one-line summary of the M61 line, after four versions: *the mathematics got stronger every time the physics got weaker, and both moves were forced by the same discipline.* v1.0 claimed a closed physical bridge on an identifiability result. v1.1 withdrew that. v1.2 replaced two hypotheses by theorems and factorised the forward problem into two one-number gates. v1.3 ran the first of those gates and it failed, and then found that the symmetry the whole graded chain assumes is contradicted by the corpus's own master action.

**The next action is not in this paper.** It is a single question to ZS-A3 and ZS-F1: *is ε a component of H₅, or is it not?* Everything in §§7–8 and §§19–24 waits on that answer, and §28.5 states exactly what each answer costs.

---


---

# Part VI — The type repair

*Everything in Part VI is new in v1.4. It resolves the v1.3 dichotomy of §28.5 — not by choosing a branch, but by finding that the question was asked about the wrong object. The seam-odd Z-bias observable is **Im Φ**, not ε = |Φ|. The mathematics of Parts IV–V survives the repair verbatim; the physical bridge does not, and its obstruction becomes sharper and, for the first time, unconditional.*

---

## §34. Theorem M61.22 — the seam involution on the ZS-F1 field space

### 34.1 What ZS-F1 actually says

ZS-F1 v1.0 §2.3 defines the Z-bias field and then, in a single sentence that four versions of this paper read past, fixes the type of ε:

> **Definition (Z-bias field).** The Z-bias field is a complex scalar Φ(x) = ρ(x) exp(iθ(x)) ∈ ℂ with radial mode ρ = |Φ| and angular mode θ ∈ [0, 2π).
> **Legacy notation.** The real scalar ε used in the radial-frozen limit (|Φ| → 1, θ → const) is recovered via **ε ≡ |Φ|**.

with V(Φ) = (λ/4)M_P⁴(|Φ|² − 1)². Two consequences follow immediately and neither was drawn:

1. **ε ≥ 0.** The map ε ↦ −ε is not an endomorphism of the field space; it leaves it. Every statement of the form "ε ↦ −ε is the seam involution" is a **type error**, not an approximation.
2. **The vacuum manifold is the circle |Φ| = 1**, of real dimension one — not the two-point set {−1, +1}. The corpus phrase "vacua ε = ±1", inherited from ZS-A3 through ZS-M57 §16.3 into ZS-M60 and this paper, is a mis-statement of a rotationally symmetric vacuum as a discrete one.

### 34.2 The classification, and which involution the corpus already uses

**Theorem M61.22 (Seam Involution Classification). [PROVEN].** Let the Z-bias field space be ℂ ≅ ℝ² = span{Re Φ, Im Φ} with potential V a function of |Φ|² alone. Then the linear involutions of the field space preserving V are exactly

- the **reflections** Φ ↦ e^{2iα} Φ̄, all conjugate to complex conjugation J_C : Φ ↦ Φ̄, i.e. (Re Φ, Im Φ) ↦ (Re Φ, −Im Φ), with det = −1; and
- the **half-shift** J_π : Φ ↦ −Φ = −I, with det = +1.

J_π is **central**, so by ZS-M56 Theorem M56.22′ it admits **zero odd operators** and cannot carry a seam grading. Therefore **J_C is the unique admissible non-central seam involution on the Z-bias field**, and its mode decomposition is

**even mode: Re Φ  ·  odd mode: Im Φ .**

Proof. A linear map preserving |Φ|² is in O(2) = SO(2) ⋊ ℤ₂; involutions in SO(2) are ±I, and involutions in the reflection component are the reflections, all conjugate. Centrality of −I is immediate; M56.22′ then gives the zero-odd-operator conclusion. ∎ Verified: rows X1–X3.

**And this is not a new choice — it is the corpus's own.** ZS-M54 Lemma M54.8a and ZS-F0 Definition 8.11 give the Z-sector seam parity as **J_seam|_Z = diag(+1, −1)** with slot 0 the β₀ physical (ℤ₂-even) mode and slot 1 the ℤ₂-odd mode. On the two-real-dimensional Z-sector field space that operator **is** complex conjugation (row X4). The corpus has had the right involution written down since ZS-F0; what it had not done is ask which *field component* the two slots are. They are Re Φ and Im Φ.

**Corollary 34.1.** ε = |Φ| is a function of |Φ|², hence **seam-even**. It cannot be the seam-odd vertex operator, at any support, in any limit (row X5).

### 34.3 TYPE LOCK

The following three objects are distinct and no symbol may denote more than one of them.

| Symbol | Definition | Range | Seam parity under J_C | Role |
|---|---|---|---|---|
| **ρ** | \|Φ\| — the ZS-F1 radial mode, and the legacy ε | [0, ∞) | **even** | heavy mode, m_ρ = 2**A**M_P; vanishes at vortex cores |
| **θ** | arg Φ | [0, 2π) | odd as an angle: θ ↦ −θ | the massless Goldstone; ΔN_eff = 0 |
| **S** | Im Φ = ρ sin θ | (−∞, ∞); [−1, 1] on the vacuum circle | **odd** | **the seam-odd observable** |

**ZS-M61 v1.0–v1.3 wrote "ε" for ρ and then required it to be seam-odd.** That is the single error from which the v1.3 dichotomy of §28.5 arose, and it is now repaired rather than adjudicated. Gate **F-M61.36 (new)** fires on any use of one symbol for two rows of this table.

**(H-VAC-BDY) is replaced.** "Support on ε² = 1" becomes, correctly, support on the vacuum circle |Φ| = 1 — on which S = sin θ ranges over the whole of [−1, 1], and **S² = 1 holds only at the two points θ = ±π/2**. The hypothesis the paper actually needs is therefore

> **(H-QUAD).** The boundary-process phase law is supported on θ = ±π/2.

which is a much stronger and far less natural statement than "the state sits in the vacuum". §35 shows what it costs.

### 34.4 What survives the repair — the whole of Part IV

This is the load-bearing question and the answer is favourable, because Part IV was never written about a radial amplitude. It was written about a **bounded seam-odd observable with a probability law**. Substituting ε̂ → Ŝ and ε_max → S_max = sup|sin θ| on the support:

| Result | Statement after the repair | Survives? |
|---|---|---|
| Thm M61.13 | a = Tr(ρ_E e^{−2icŜ}) = Φ_P(−2c), P the law of S | **verbatim** |
| Thm M61.14 | spec Ŝ ⊆ [−1,1] on the vacuum circle ⟹ c ≥ arccos(Re λ)/(2 S_max) = c\*/S_max | **verbatim** (row X7) |
| Thm M61.15 | T(u), u = 2c·S_max; T(φ) = T₂, T(π) = M\* | **verbatim** |
| Thm M61.16 | empty divisor on the λ-compatible class | **verbatim** |
| Thm M61.17 | codimension-1 reachability; \|⟨S⟩\| = T₂ under (H-QUAD) | **verbatim** |
| Thm M61.20 | M\*(a; u) — pure mathematics, no field content at all | **untouched** |
| Thm M61.19 | Yukawa slot isotropy; the obstruction now reads: **the seam involution extended to the matter sector is a charge-conjugation-type ℤ₂**, because Φ ↦ Φ̄ on a slot of H₅ requires a compensating fermion conjugation | **survives, sharpened** |
| Thm M61.21 | the kink *radial* weight computation | **retired** — it averaged the wrong variable; §35 replaces it |

**Only one result of the paper is retired by the repair, and it is replaced by a stronger one.** That is the payoff of v1.2's decision to state Part IV in terms of a bounded seam-odd observable rather than a named field.

---

## §35. Theorem M61.23 — the uniform Goldstone cannot produce λ, unconditionally

### 35.1 The Bessel form of the multiplier

On the vacuum circle write S = sin θ. Then for **any** phase law P_θ,

**a(c) = E[ e^{−2ic sin θ} ] .**

**Theorem M61.23 (Uniform-Goldstone No-Go). [PROVEN].** If the phase law is uniform on [0, 2π) — which is what ZS-F1's exactly flat Goldstone potential supplies, with no fitting whatsoever — then

**a(c) = J₀(2c)  for all c,**

the Bessel function of the first kind, which is **exactly real**. Consequently Im a ≡ 0, and

**min_{x ≥ 0} J₀(x) = −0.402759395702552972 > Re λ = −0.566417330285464 .**

Therefore **λ is unreachable at every accumulated phase**, with a deficit in the real part of

**min J₀ − Re λ = 0.163657934582911431 .**

Proof. E[e^{iu sin θ}] over uniform θ is the Bessel integral (1/2π)∫e^{iu sin θ}dθ = J₀(u), real because the integrand's imaginary part is odd in θ. The global minimum of J₀ on [0, ∞) is attained at the first minimum, x ≈ 3.8317, with value −0.402759…, standard. Comparing with Re λ closes the argument. ∎ Verified rows Y1–Y3.

### 35.2 Why this is the strongest result the programme has produced

It has every property the forward gates of §22 were designed to require and that no earlier result had all of:

- **Target-blind.** λ enters only in the final comparison. The uniform law is not chosen to fail; it is what the ZS-F1 action gives.
- **No hypothesis.** No (F2), no (H-VAC-BDY), no (H-QUAD), no (H-KINK-WEIGHT), no clock. Only: the vacuum manifold is |Φ| = 1 and θ is an exact Goldstone.
- **No free parameter.** Not one. The accumulated phase c is quantified over, not fitted.
- **Unconditional in c.** It is not "fails at the minimal phase"; it fails at every phase, because a bounded function cannot go below its minimum.
- **A single number decides it.** min J₀ versus Re λ.

**Status: CLOSED-NEGATIVE, unconditional.** The uniform-Goldstone branch of the S14 boundary process is dead. Gate **F-M61.37 (new)** fires on any claim that an unbiased Goldstone phase reproduces λ.

**A structural remark worth recording.** The law of S = sin θ for uniform θ is the **arcsine law**, density 1/(π√(1−s²)) — which is *exactly* the edge-concentrated shape that §30's exponent p\* < 0 said was required. The uniform Goldstone therefore has the right *shape* and zero *bias*, and it is the bias, not the shape, that λ demands. That is a considerably more informative failure than §30's.

### 35.3 The biased law reaches λ — and that is the trap again

**Theorem M61.23a. [DERIVED; evidential status IDENTIFIABILITY].** A von Mises phase law of concentration κ about θ₀ = −π/2, p(θ) ∝ exp(κ cos(θ + π/2)), reproduces λ exactly at

**κ\* = 3.740875…,  c = 1.290067… ,**

with residual 5 × 10⁻¹⁵ (row Y5). The resulting law has ⟨S⟩ = −0.852762 and seam asymmetry TV(P, P̌) = 0.979694, both above the T₂ floor as Theorem M61.15 requires.

**And it carries zero evidential content.** (c, κ) are two real parameters fitted to two real constraints: this is the ZS-M56 Theorem M56.7 trap, in exactly the form ZS-M57 Theorem M57.C.2 diagnosed and for which Theorem M61.7′ was demoted in v1.1 (row Y6, typed TAUTOLOGY). **The type repair does not by itself escape the trap.** What escapes it is deriving κ from the action.

### 35.4 The dichotomy, now with physical content

Combining §35.2 and §35.3:

> **Either** θ is an exact massless Goldstone — ZS-F1 results 1 and 3, the sub-Planckian heavy radial mode and ΔN_eff = 0 exactly — **and then λ is unreachable by Theorem M61.23, unconditionally**;
>
> **or** the Goldstone carries an explicit U(1)_Z-breaking bias of concentration κ\* ≈ 3.74, **which gives θ a mass and contradicts ZS-F1 results 1 and 3**.

The two branches are **mutually exclusive**, both are stated in terms of ZS-F1's own results, and the second is quantified: the required breaking is not infinitesimal. κ ≈ 3.74 is a strong bias, not a perturbation — the law it produces has 98% of its reflection asymmetry.

This is a strictly better residual than v1.3's §28.5, because both branches are now statements about the *same* paper's *own* published results rather than about an unresolved field identity. Gate **F-M61.38 (new)** fires on any presentation of a biased Goldstone that does not state the ΔN_eff and masslessness cost.

---

## §36. Theorem M61.24 and the dual certificate

### 36.1 The broken-seam budget

If (F2) is broken rather than exact — which §28 and §34.4 now both suggest — the right move is not to restore it but to give the breaking a budget.

**Theorem M61.24 (Broken-Seam Budget). [PROVEN].** Let the graded relation hold up to an even remainder of amplitude δ, so that the attainable real part is relaxed to Re a ≥ cos u − δ. Then the feasibility condition becomes cos u ≤ Re λ + δ, the phase floor becomes

**c ≥ ½ arccos(Re λ + δ) ,**

monotone decreasing in δ, and the asymmetry floor is Lipschitz in δ with leading coefficient

**|dT/du| · (1 − Re²λ)^{−1/2} = 0.113142569284 × 1.213417635970 = 0.137289188949 per unit δ .**

| δ | phase floor c ≥ | shift from c\* |
|---|---|---|
| 0 | 1.086474189775053 | — |
| 0.01 | 1.080432045870 | −0.00604 |
| 0.05 | 1.056729129804 | −0.0297 |
| 0.10 | 1.028016276749 | −0.0585 |

**Reading.** The floors are *robust*: a 10% seam-breaking amplitude moves the phase floor by 5% and the asymmetry floor by 1.4%. So the results of Part IV are not artifacts of exact symmetry, and a future broken-seam theory inherits them with explicit error bars. This answers the audit's breakthrough C in the form it asked for: **M\*(a; u, δ)** with δ the symmetry-breaking budget (rows Z1–Z2).

### 36.2 The dual certificate for Theorem M61.20

The audit's breakthrough D asked for a convex dual certificate so that Theorem M61.20 can be quoted without the verifier. The primal problem on the arc [−u, u] is

minimise ‖ν_odd‖ subject to ∫cos θ dν = x, ∫sin θ dν = y, ν ≥ 0, ‖ν‖ = 1,

with dual variables (p, q, r) conjugate to the three equalities and the dual objective px + qy + r. Strong duality is verified at the three structurally distinct arcs (row Z3):

| u | primal | dual | gap |
|---|---|---|---|
| φ = 2.172948 (minimal arc, T₂) | 0.835381287 | 0.835381287 | < 10⁻⁸ |
| 2.600000 (interior) | 0.789159044 | 0.789159044 | < 10⁻⁸ |
| π (full circle, M\*) | 0.763363862 | 0.763363862 | < 10⁻⁸ |

**Zero duality gap at every u tested.** Together with the explicit two-atom primal of Theorem M61.20 and the complementary-slackness conditions of Appendix B, this is the three-part certificate — primal construction, dual bound, equality — that makes the theorem self-certifying. **Theorem M61.20 is now quotable by a reader who rejects every Z-Spin premise.**

---

## §37. Stale-statement sweep, and the corrected counts

The audit found the v1.3 non-claim layer lagging its own science. Corrected here.

| Item | v1.3 text | v1.4 |
|---|---|---|
| **NC-M61.3** | "ZS-M61 does not prove (F2). It assumes it…" | **Rewritten.** ZS-M61 does not assume (F2). On the H_id branch item W1 is **falsified** (Thm M61.19); after the type repair the seam involution is complex conjugation, whose extension to the matter sector is a **charge-conjugation-type ℤ₂**, and the Standard Model violates C. (F2) is therefore not an open assumption but a **located obstruction**, and gate F-M61.32 governs its use. |
| **NC-M61.12** | "Reduction R1 reduces (F2) to five finite items, two settled and three registered as D-M61-WARD" | **Rewritten.** D-M61-WARD is executed: W2 holds, W3 is upstream-ambiguous (D-S14-PHI), **W1 fails**. What remains is not a checklist but the §35.4 dichotomy. |
| **Title** | "The Graded S14-Compatible Realisation…" | **Retitled** to "The Boundary-Asymmetry Geometry and the S14 Seam-Symmetry Obstruction". "S14-compatible" is withdrawn: §28.5 and §34 together show the class is graded-realisation-compatible, not demonstrably S14-compatible. |
| **Thm M61.12′** | headline conditional realisation theorem | **Demoted to a counterfactual classification theorem**: *if* an exact seam grading held with a bounded seam-odd observable, *then* the realisation is unique. Preserved in full, moved out of the headline. |
| **M61.20 count** | "46 (a, u) pairs" | **Corrected: 48 grid combinations, of which 39 are finite comparison pairs**; 9 are jointly infeasible and excluded by both the closed form and the LP. The 4.2 × 10⁻⁶ worst deviation and the zero feasibility mismatches are unchanged. |
| **Thm M61.21** | FWD-I on the kink radial weight | **Retired as a forward computation** (it averaged the seam-even variable) and **retained as a lemma** about the pushforward of radial weights, with a pointer to §35. |

---

## §38. Should ZS-S14 be revised? — a recommendation

The user asked directly. **Yes, and the case is now much stronger than v1.3's.** But the revision that matters is small, and it is not the one that looks most urgent.

### 38.1 What must be fixed, in priority order

**Priority 1 — the Φ identity (D-S14-PHI). ERRATUM REQUIRED.** ZS-S14 v2.0 §7.1 makes Φ the D₃-**trivial** component of H₅; §7.5 Theorem S14.D.4 Step 2 makes Φ the **neutral component of the D₃-2 weak doublet**. These are different subspaces of H₅ with different gauge quantum numbers. The second is what makes Y_Φ = q_Φ × (1/Z) = +1/2 work; the first is what §7.1's five lines of evidence and every downstream paper cite. **One of them must be withdrawn.** This is a type error of exactly the class ZS-M57's rule R10′ was written for, and it is load-bearing for S14.D.4, S14.E and every graded downstream paper. Severity **S3**.

**Priority 2 — the field-type separation.** ZS-S14 inherits the ZS-F1 field content but never states, in one place, the types of the five distinct objects the corpus now needs to keep apart: the Higgs carrier H₅; the Z-bias complex scalar Φ_Z; its radial mode ρ = |Φ_Z| (= the legacy ε); its Goldstone θ; and the seam involution J. The §34.3 TYPE LOCK table is offered for direct insertion. Without it the ε ≡ |Φ| error will recur, because it recurred four times in this paper alone. Severity **S2**.

**Priority 3 — the "vacua ε = ±1" phrase.** It appears in ZS-A3, is quoted by ZS-M57 §16.3, was inherited by ZS-M60 and by this paper, and is a mis-statement: the vacuum manifold is the circle |Φ| = 1. Anywhere the two-point reading is load-bearing — and in ZS-M60's F-M54-16′ re-typing it is — the statement must be re-derived. Severity **S2**, and it propagates.

**Priority 4 — the Yukawa/seam interaction.** If Φ_Z ⊂ H₅ then Theorem M61.19 shows the Yukawa term is linear in every slot including Φ_Z's, so the seam ℤ₂ must be accompanied by a fermion conjugation and is a C-type symmetry. ZS-S14 should either state that explicitly or state that Φ_Z is an independent field with an explicit intertwiner into H₅. Severity **S2**.

### 38.2 What should *not* be done

**Do not re-derive the numbers.** Every observational output of ZS-S14 — α_s = 11/93, v = 245.93 GeV, m_t, sin²θ_W, the anomaly cancellations, the ZS-S7 and ZS-Q3 inheritances — is insulated: none uses the D₃-trivial-versus-D₃-2 distinction, and none uses the seam involution at all. R0 already established this for the colour clause and the same argument applies here. **An erratum, not a v3.0.**

**Do not add a Goldstone-breaking term to make λ reachable.** That is the κ\* ≈ 3.74 branch of §35.4, it costs ZS-F1 results 1 and 3, and adding it *because* λ needs it would be the purest form of the M56.7 trap — a shape parameter solved from the target.

### 38.3 The recommended instrument

A **dated erratum to ZS-S14 v2.0** with four items: (i) withdraw one of the two Φ identifications and state which; (ii) insert the TYPE LOCK table; (iii) correct the vacuum-manifold phrase and flag the downstream papers that inherited it; (iv) state the Φ_Z ↔ H₅ relation as either containment-with-intertwiner or independence. Zero numerical outputs change. Then, and only then, is the forward gate of §22 well posed, because only then is it known what field the vertex couples to.

**And one thing ZS-S14 should be credited with.** Its master action was complete and explicit enough that a downstream paper could falsify one of its own downstream assumptions against it by direct computation. Most action-level papers in this corpus are not. That is the reason §28 was possible at all.

---

## §39. Conclusion to v1.4

v1.3 ended with a question to ZS-A3 and ZS-F1: *is ε a component of H₅?* The answer, read directly out of ZS-F1 §2.3, is that the question was mis-typed. **ε ≡ |Φ| is the radial amplitude, it is non-negative, and it is seam-even.** There is no ℤ₂ acting as ε ↦ −ε, and there never was.

The repair is short and the consequences are long. The unique non-central involution of the Z-bias field space is complex conjugation; its odd mode is **Im Φ**; and that operator — not the radial amplitude — is the seam-odd observable the whole graded chain needs. The corpus had the right involution since ZS-F0 Definition 8.11 and ZS-M54 Lemma M54.8a; what it had never done is ask which field component the two slots are.

**The mathematics survives.** Part IV was stated for a bounded seam-odd observable with a probability law, so substituting ε̂ → Im Φ̂ carries Theorems M61.13–M61.17 across verbatim, and Theorem M61.20 was never about a field at all. One result — the kink radial-weight computation of §30 — is retired, because it averaged the even variable.

**The physics gets a much better obstruction.** On the vacuum circle the seam-odd observable is sin θ, and for the uniform phase law that ZS-F1's exactly flat Goldstone potential supplies, the multiplier is the Bessel function J₀(2c). It is real, so Im λ is unreachable; and its global minimum is −0.402759395702552972, above Re λ = −0.566417330285464, so Re λ is unreachable too — **at every accumulated phase, with no fitted parameter and no clock.** *(v1.4 wrote "with no hypothesis" here. That was wrong: the uniform law is a hypothesis, named (H-U1-BDY) in §41.1, and the verdict is CLOSED-NEGATIVE-CONDITIONAL — see §41.2. The numbers in this sentence are also corrected per Appendix D.5.)* It is the first target-blind result in the M56–M61 line, and it is negative.

The alternative is quantified rather than gestured at: a von Mises bias of concentration κ\* = 3.740875 at c = 1.290067 reproduces λ to 5 × 10⁻¹⁵ — and is a two-real-fit against two real constraints, the M56.7 trap, worth nothing as evidence. What it *is* worth is the statement of the cost: that bias gives the Goldstone a mass and contradicts ZS-F1's own results 1 and 3, including ΔN_eff = 0 exactly. **Either the Goldstone is massless and λ is unreachable, or λ is reachable and the Goldstone is not massless.** Both halves are about ZS-F1's published results, which is why this dichotomy is decidable where §28.5's was not.

Two further audit requests are discharged. The broken-seam budget gives the floors explicit error bars — a 10% breaking moves the phase floor by 5% and the asymmetry floor by 1.4% — so Part IV is robust rather than knife-edge. And Theorem M61.20 now carries a **dual certificate** with zero duality gap at the minimal arc, an interior arc and the full circle, which makes it quotable by a reader who rejects every Z-Spin premise. That, together with §26's plan, is what an external mathematics paper needs.

**Where the programme stands.** Four results are unconditional mathematics and one is now an unconditional physical no-go. The bridge is not closed and is further from closing than v1.2 believed, because the object it was built on was the wrong one and the correctly-typed object fails at the first target-blind test. That is not a setback in the ordinary sense: for four versions this line has traded claimed closure for located obstruction, and the obstruction is now located in a single sentence of a foundational paper rather than in an unexecuted functional integral.

**The next action is again not in this paper, and it is again one question — but now it is a question with an answer that exists.** ZS-S14 must say which of its two Φ identifications it means (§38.1), and ZS-F1 must say whether anything in the Z-Spin action gives the Goldstone θ a potential. If nothing does, Theorem M61.23 closes the graded route negatively and the corpus should say so. If something does, its concentration must be computed and compared with κ\* = 3.740875 — once, at the end, target-blind.

---


---

# Part VII — Completion

*v1.5 adds no new research. It narrows two v1.4 overclaims to what is actually established, names the hypothesis v1.4 omitted, registers the typed bridge v1.4 assumed, and installs a single reading rule that makes every earlier Part current. After this Part the paper is internally consistent and closed to further version growth; the remaining work is upstream and is sequenced in §42.*

---

## §40. Theorem M61.22′ — the corrected involution statement

### 40.1 What is established, and what is not

v1.4 stated that complex conjugation is *the unique* non-central involution of the Z-bias field space. That is too strong in two ways, both correct as raised.

**Theorem M61.22′ (Seam Involution Classification, corrected; this is §40.1). [PROVEN].** Let the Z-bias field space be ℂ ≅ ℝ² = span{Re Φ, Im Φ} with potential a function of |Φ|² alone, so that the symmetry group is O(2). Then:

(i) the involutions in SO(2) are exactly **+I** (trivial) and **−I** (the half-shift Φ ↦ −Φ);
(ii) **−I is central**, so by ZS-M56 Theorem M56.22′ it admits **zero odd operators** and cannot carry a seam grading;
(iii) the involutions in the reflection component form a **single continuous conjugacy class**

  **J_α : Φ ↦ e^{2iα} Φ̄ ,  α ∈ [0, π) ,  J_α = R(α) J_C R(α)^{−1} ,**

 each with J_α² = I and det J_α = −1, of which complex conjugation J_C = J_0 is one representative.

**Therefore: the non-trivial, non-central involutions preserving the potential form exactly one conjugacy class of reflections.** Not "complex conjugation is unique."

Proof. O(2) has two components. In SO(2), R(β)² = I forces β ∈ {0, π}, giving ±I; centrality of −I is immediate. Every element of the reflection component is a reflection about some line, squares to the identity, has determinant −1, and is conjugate to any other by the rotation taking one axis to the other. ∎ Verified: 401 values of α, with J_α² = I, det = −1 and R(α)J_C R(−α) = J_α all to 10⁻¹⁵, and a 20001-point sweep confirming ±I are the only involutions in SO(2) (block V5, rows V5-1, V5-2).

### 40.2 Why the ambiguity does not propagate

The odd **mode** depends on the representative: J_α has even mode Re(e^{−iα}Φ) and odd mode **Im(e^{−iα}Φ)**. Fixing α is a real physical datum and it is not fixed here.

**But nothing quantitative in this paper depends on it.** Every result of Part IV is a statement about the *law of the odd component* — its support radius S_max, its mean, its reflection asymmetry — and those are invariant under the rotation that relabels which axis is odd. The α-dependence is a choice of coordinate on the field, not a choice of physics, and it is registered as such rather than silently fixed. (row V5-3.)

**Corollary 40.1 (unchanged, and unaffected by the correction).** ε = |Φ| is a function of |Φ|² and is therefore **even under every J_α**. No reading of any admissible involution makes the radial amplitude the seam-odd vertex operator. This is the ZS-F1 finding of §34 and it survives the narrowing intact.

### 40.3 The missing typed bridge, registered OPEN

v1.4 asserted that the corpus "already had" the right involution, on the grounds that ZS-F0 Definition 8.11 and ZS-M54 Lemma M54.8a give J_seam|_Z = diag(+1, −1) with slot 0 even and slot 1 odd. That is a fact about an **abstract** Z-sector parity. Reading it as the field-coordinate statement |0⟩ ↔ Re Φ, |1⟩ ↔ Im Φ requires one more object, which does not exist:

> **D-M61-IOTA (new, OPEN).** A typed intertwiner
> **ι_ZΦ : ℋ_Z^parity → span_ℝ{Re Φ, Im Φ}  with  ι_ZΦ ∘ J_Z = J_C ∘ ι_ZΦ .**

ZSPIN_CORE §1 keeps the Z-sector, Z-Spin and the Z-bias field Φ as distinct ontological layers, and the physical-bridge checklist requires exactly this kind of representation/intertwiner as item 3. **It is not constructed here and it is not assumed** (rows V5-4, V5-5).

Accordingly the three statements must be kept apart:

| Statement | Status |
|---|---|
| ε = \|Φ\| is seam-even and cannot be the seam-odd observable | **[검증됨] PROVEN** (§34, Cor 40.1) |
| the potential-preserving non-central involutions are one conjugacy class of reflections | **[검증됨] PROVEN** (Thm M61.22′) |
| the ZS-F0 parity eigenbasis is (Re Φ, Im Φ) | **[열림] OPEN** (D-M61-IOTA) |

### 40.4 Consequence for ZS-F0: no action

Nothing found here shows any statement of ZS-F0 to be false. J_Z = diag(+1, −1) is an abstract parity and is not contradicted. The gap is between ZS-F0's parity space and ZS-F1's field coordinates, and a missing bridge is not an error in either endpoint. **ZS-F0 is not to be corrected on this evidence**, and v1.4's implicit suggestion that it had already settled the field identification is withdrawn. Gate **F-M61.40 (new)** fires on any use of the F0 parity as if it were the field-coordinate statement.

---

## §41. Theorem M61.23′ — the Goldstone no-go, made conditional

### 41.1 The hypothesis v1.4 omitted

v1.4 wrote that "ZS-F1's exactly flat Goldstone potential supplies the uniform phase law." **That inference is invalid and is withdrawn.** A flat potential makes every θ energetically degenerate; it does not make the *state* uniform. Spontaneous symmetry breaking is exactly the case of a symmetric action whose state selects a phase — and ZS-F1's own result 1 is that the U(1) is spontaneously broken at |Φ| = 1. Initial conditions, boundary conditions, currents and state preparation all permit non-uniform laws on a flat potential.

The hypothesis the theorem actually needs is therefore named:

> **(H-U1-BDY).** The boundary-process phase law P_θ is U(1)-invariant, i.e. Haar-uniform on [0, 2π).

(row V5-6.)

### 41.2 The theorem, restated at exact strength

**Theorem M61.23′ (Uniform-Goldstone No-Go). [PROVEN as mathematics; CLOSED-NEGATIVE-CONDITIONAL on (H-U1-BDY) as physics].** Under (H-U1-BDY), with S = sin θ on the vacuum circle,

**a(c) = E[ e^{−2ic sin θ} ] = J₀(2c) for all c, exactly real,**

so Im λ ≠ 0 is unreachable; and since

**min_{x ≥ 0} J₀(x) = −0.402759395702552972 > Re λ = −0.566417330285464 ,**

Re λ is unreachable at **every** accumulated phase, with deficit **0.163657934582911431**.

**The mathematics is unchanged and is now certified more strongly than in v1.4.** The Bessel identity is integrated directly at eight values of u — 0.3, 0.9, 1.7, 2.5, 3.8317, 5.0, 7.0, 10.0 — with worst residual below 10⁻⁹, replacing v1.4's row which asserted the identity but tested only that the mean of sin θ vanishes (§43.1, item 2). The minimum of J₀ and the comparison with Re λ are re-verified (row V5-7).

**What changes is the label.** The physical verdict is lowered:

| | v1.4 | **v1.5** |
|---|---|---|
| Mathematical status | PROVEN | PROVEN (unchanged, better certified) |
| Physical verdict | CLOSED-NEGATIVE, *unconditional* | **CLOSED-NEGATIVE-CONDITIONAL on (H-U1-BDY)** |
| Headline | "the first unconditional target-blind no-go" | **"the first target-blind no-go, conditional on one named hypothesis"** |

Gate **F-M61.41 (new)** fires on any statement that Theorem M61.23′ is unconditional, or that a flat potential implies the Haar law.

### 41.3 An internal conflict, resolved

v1.4 carried NC-M61.21 — "ZS-M61 does not derive the Goldstone phase law from the action" — alongside §35's claim that the flat potential supplies the uniform law. Those two cannot both stand. **The §35 claim is withdrawn and NC-M61.21 stands** (row V5-8). This was caught by the audit and not by the paper's own gates, which is recorded as a gate-coverage gap: no gate then existed against deriving a *state* from a *potential*. F-M61.41 closes it.

### 41.4 What the theorem is still worth, which is a great deal

Lowering the label costs less than it appears, because (H-U1-BDY) is not an arbitrary assumption — it is the **maximally symmetric** and therefore the default boundary law, the one a theory with an exact U(1) and no phase-selecting mechanism would have. So the correct reading is:

> **The default, maximum-entropy phase law is excluded, at every accumulated phase, by a single comparison of two numbers.** Any surviving route must therefore exhibit an explicit phase-selecting mechanism — and §35.3 shows what it must deliver: a concentration of order κ ≈ 3.74, not a perturbation.

That is a strictly stronger constraint than "λ is not yet derived", and it is the first result in this line to put a floor under how much structure the boundary must have.

**And the §35.3 tautology control is unaffected.** The von Mises law reaching λ at κ\* = 3.740875, c = 1.290067 remains a two-real fit against two constraints, typed TAUTOLOGY, with zero evidential content; and the §35.4 dichotomy — massless Goldstone versus λ-reachability — remains valid with its first branch now reading "under (H-U1-BDY)".

---

## §42. The upstream sequencing

The user's question — revise ZS-S14 or ZS-F0 first? — has a definite answer, and v1.5 changes it slightly from v1.4's.

**Order:**

1. **This completion.** Done here. Upstream must not be corrected to match a downstream reading that is itself being narrowed.
2. **ZS-S14 dated erratum** — the contradictory Φ identification (D-S14-PHI, severity **S3**), plus the three lower-severity items of §38.1. This is genuinely independent of everything above: §7.1 makes Φ the D₃-trivial component of H₅ and §7.5 Theorem S14.D.4 Step 2 makes it the neutral component of the D₃-2 weak doublet, and those are different subspaces with different gauge quantum numbers. It is also the lowest-cost, highest-clearance repair available: **zero numerical outputs change** (§38.2).
3. **Construct or refute ι_ZΦ** (D-M61-IOTA, §40.3). This is the object that decides whether the F0 parity and the F1 field coordinates are the same statement.
4. **Only then reassess ZS-F0**, with three possible outcomes: no change, if the parity is meant abstractly; a clarification or addendum, if ι_ZΦ is constructed and becomes canonical programme language; an erratum, only if a specific ZS-F0 statement is then found false.
5. **Only then re-run the physical forward gates** of §22. Running them before step 2 would test a vertex whose carrier is ambiguous.

**ZS-F0 is not to be touched now** (row V5-9). And the ZS-F1 finding is independent of the whole sequence: ε ≡ |Φ| ≥ 0 is seam-even whatever ι_ZΦ turns out to be, so debt **D-F1-EPS** — the "vacua ε = ±1" phrase and its inheritance through ZS-A3, ZS-M57 §16.3 and ZS-M60 — stands on its own and can be corrected at any time (row V5-10).

---

## §43. The normative reading rule, and the stale-statement register

### 43.1 Corrections made in this completion

| # | v1.4 statement | v1.5 |
|---|---|---|
| 1 | Thm M61.22: complex conjugation is *the unique* non-central involution | **Thm M61.22′**: the non-trivial non-central involutions form a single conjugacy class of reflections; +I trivial, −I central |
| 2 | Block X row asserting uniqueness; block Y row asserting the Bessel identity while testing mean(sin θ) = 0 | Both **retyped**: the X row now states only what it tests (det = −1, non-centrality); the Y row **integrates** the Bessel identity at eight values of u |
| 3 | "the corpus already had the right involution" | Narrowed: the corpus has the right **abstract** parity; the eigenbasis identification is **OPEN** (D-M61-IOTA) |
| 4 | "ZS-F1's flat Goldstone potential supplies the uniform phase law" | **Withdrawn.** (H-U1-BDY) is named and required |
| 5 | Thm M61.23 CLOSED-NEGATIVE unconditional; "first unconditional target-blind no-go" | **Thm M61.23′** CLOSED-NEGATIVE-**CONDITIONAL**; headline lowered |
| 6 | implicit suggestion that ZS-F0 may need correction | **Withdrawn**; §42 sequences F0 last, possibly with no change |
| 7 | min J₀ = −0.402759395329850, deficit 0.163657934955614 | **ERRATUM D.5.** Both were read off a 600001-point grid and printed to 15 digits the grid cannot support; both are wrong from the 10th digit. The exact values, from J₀(j₁,₁) with j₁,₁ = 3.83170597020751232 the first zero of J₁, are **min J₀ = −0.402759395702552972** and **deficit 0.163657934582911431**. The inequality min J₀ > Re λ is unaffected and no conclusion changes. **Found by this version's own self-consistency audit** (§45), which is the first time a printed-figure error in this line was caught before a reviewer saw it |

### 43.2 The reading rule

Rather than editing every earlier section, one normative clause governs the whole document (row V5-12):

> **READING RULE.** Everywhere in Parts I–V, the symbol **ε̂** denotes the seam-odd observable **Ŝ = Im(e^{−iα}Φ̂)** of §40.2, and **ε_max** denotes **S_max**. The hypothesis written **(H-VAC-BDY)** denotes **(H-QUAD)** of §34.3. The symbol **ε** in the ZS-F1 sense — the radial amplitude |Φ| — occurs only in §§34, 40 and in quotations of superseded text, where it is always marked.
>
> Under this rule every theorem of Parts I–V is current as written. §34.4 lists the one exception: Theorem M61.21, retired as a physical computation because it averaged the seam-even variable, retained as a lemma about pushforwards of radial weights.

### 43.3 Statements now superseded, with their replacements

Five statements from v1.2–v1.4 are no longer current and are listed once, here, so that no reader has to reconstruct the sequence (row V5-11):

| Superseded statement | Where it was | Current replacement |
|---|---|---|
| "(F2) is assumed and open" | v1.2 §4.3, NC-M61.3 | Falsified on the H_id branch, Thm M61.19; §28.5 dichotomy; gate F-M61.32 |
| "no target-blind number appears anywhere in this paper" | v1.3 NC-M61.13 | Thm M61.21 (3/8, 1/2, 5/16) and Thm M61.23′ (min J₀ vs Re λ) are target-blind |
| "the general M\*(a; u) closed form is stated for the outer branch only" | v1.2 §21.2(v), NC-M61.14 | Thm M61.20, complete with feasibility boundary, inner branch and dual certificate; D-M61-ARC closed |
| "ε̂ is the seam-odd Z-bias operator" | v1.0–v1.3 §7.1 | Ŝ = Im(e^{−iα}Φ̂); ε = \|Φ\| is seam-even (§34, Cor 40.1) |
| "the flat potential supplies the uniform law" | v1.4 §35.1 | Withdrawn; (H-U1-BDY) named (§41.1) |

---

## §44. Closing status of ZS-M61

### 44.1 The current-state board

Every claim of the paper, at the strength it now holds. This table supersedes every earlier scoreboard.

| # | Result | Status | Depends on |
|---|---|---|---|
| M61.1 / R0 | ZS-S14 colour repair; H₅ colour-singlet, SU(3)_C on ℂ³_C | **PROVEN** | nothing |
| M61.3 | spectral arc obstruction \|a\| ≥ cos(w/2) | **PROVEN** | nothing |
| M61.11 | M\*(a) closed form, inner/outer split | **PROVEN**, prior art NOT_FOUND | nothing |
| M61.20 | M\*(a; u) general form + **dual certificate** | **PROVEN**, prior art NOT_FOUND | nothing |
| M61.19 | Yukawa slot isotropy G = δ/5; no slot can vanish | **PROVEN** | ZS-M10 tensor |
| M61.22′ | involutions = one reflection conjugacy class; ε = \|Φ\| seam-even | **PROVEN** | ZS-F1 §2.3 |
| M61.23′ | a(c) = J₀(2c); min J₀ > Re λ | PROVEN math; **CLOSED-NEG-CONDITIONAL** | (H-U1-BDY) |
| M61.24 | broken-seam budget; floors Lipschitz in δ | **PROVEN** | nothing |
| M61.2 | det V = +1 for graded relative unitaries | PROVEN, **conditional** | (F1)∧(F2) |
| M61.4 | carrier-dimension hierarchy; corollary of M61.15 | PROVEN, conditional | (F2) |
| M61.5 | Re a = ½Tr V on a graded doublet | PROVEN, conditional | (F2) |
| M61.13–M61.17 | transfer law, phase floor, T(u), divisor, reachability | PROVEN, conditional | (F2), vertex form |
| M61.8 | non-perturbative threshold c ≥ c\* | PROVEN, conditional; SU(2) case of M61.14 | (F2) |
| M61.10″ | empty divisor on the λ-compatible class | **CLOSED-NEGATIVE** on that class | (F2) |
| M61.12′ | conditional realisation | **COUNTERFACTUAL** | (F2), (H-QUAD) |
| M61.7′ | vacuum-supported realisation | **IDENTIFIABILITY**, zero evidential content | — |
| M61.21 | kink radial weight ⟨ε⟩(p) = Γ(p+3/2)/(√π Γ(p+2)) | **RETIRED** as physics, retained as a lemma | — |
| — | S14 forward selection (FWD-R, FWD-I) | **OPEN** | D-S14-PHI first |

**Eight results are unconditional.** Four of those — M61.11, M61.20, M61.3, M61.24 — contain no Z-Spin input at all and are the paper's external contribution.

### 44.2 Open debts, all upstream or registered

| Debt | Content | Owner |
|---|---|---|
| D-S14-PHI | ZS-S14's two incompatible Φ identifications, **S3** | upstream; erratum recommended (§38, §42 step 2) |
| D-F1-EPS | the "vacua ε = ±1" phrase and its inheritance | upstream; independent of everything else |
| D-M61-IOTA | the typed intertwiner ι_ZΦ | registered OPEN (§40.3) |
| D-M61-GOLD | does anything give θ a boundary potential? | registered OPEN (§35.4, §41) |
| D-M61-WARD | (F2): W2 holds, W3 ambiguous, **W1 fails** | §28.5 dichotomy |
| D-M61-PRIOR-2 | systematic novelty sweep for M61.11 / M61.20 | registered, not performed |
| D-M61-HIST | the history-register identifier collision at H-0008 | register owner |
| DOI | no persistent identifier | one manual step (§32) |

### 44.3 Terminal statement

> **ZS-M61 v1.6 is TERMINAL-IN-SCOPE.**
>
> The scope is: the complete classification of arc-restricted reflection-asymmetry geometry for a bounded seam-odd observable, and the location — not the closure — of the S14 physical bridge.
>
> Within that scope nothing is left undone. Outside it, every remaining item is upstream (D-S14-PHI, D-F1-EPS), a registered bridge (D-M61-IOTA), or an archival action (DOI). **No successor version of this paper is required**; the next release in this line should be the ZS-S14 erratum, and after it a new paper on whichever of the two branches of §35.4 the corpus's own field content selects.
>
> **`FINAL` is withheld pending persistent archival identification.** External novelty positioning for Theorems M61.11 and M61.20 also remains **OPEN** under D-M61-PRIOR-2 and is **not** promoted by the TERMINAL-IN-SCOPE designation. *(v1.5 wrote "unavailable for one reason only: no DOI", which contradicted its own §44.2 debt table; corrected in v1.6, §46.3.)*

### 44.4 The self-consistency audit (§45 in brief; extended in §46)

Before release, v1.5 was checked against its own artifact by a script rather than by reading. Fifty-eight checks in seven groups: ledger integrity; manuscript-versus-artifact census and SHA values; every printed constant against `figures.json`; a stale-statement sweep over five named patterns; cross-reference integrity for sections, theorems, gates, non-claims and debts; resolution of every block-V5 proof pointer to a real section; and the reading rule and terminal statement.

**It found one real error** — the J₀ minimum and the deficit, printed to fifteen digits from a nine-digit grid (§43.1 item 7, Appendix D.5) — and three checker faults of its own (a Unicode-minus mismatch and two heading-pattern bugs), all corrected. This is the first version in the line whose printed-figure error was caught by the paper rather than by a reviewer, and the mechanism is now part of the artifact contract: **§18.2(8), a release must pass the self-consistency audit.**

### 44.5 What the five versions cost and bought

v1.0 claimed a closed physical bridge on an identifiability result. v1.1 withdrew it and retyped the verification. v1.2 replaced two hypotheses by theorems and factorised the forward problem into two one-number gates. v1.3 ran the first gate against the actual master action and found the graded chain's own symmetry assumption falsified. v1.4 found that the seam-odd object had been mis-typed for four versions, repaired it, and produced the first target-blind no-go. v1.5 narrowed two of v1.4's own claims, named the hypothesis it had hidden, and registered the bridge it had assumed.

Each step lowered a physical claim and raised a mathematical one, and every lowering was forced by reading a source document rather than by an argument about the paper. **That is the only pattern in this line worth exporting**: the load-bearing errors were all type errors, and every one was found by opening the upstream paper and reading the definition.

---


---

# Part VIII — Release audit

*v1.6 changes no number and retracts no theorem. Every item below is a statement the paper made about itself that was not true of itself. They are corrected here and, where checkable, made checkable.*

---

## §46. The v1.6 release-audit register

### 46.1 Ledger provenance — "strict subledger" was false

v1.5 wrote that the v1.4 ledger is a strict subledger of the v1.5 ledger. It is not, and could not be: v1.5 deliberately **retyped and reordered** rows in blocks X and Y, so the first 204 rows of v1.5 are not row-for-row identical to v1.4.

**The measured provenance** (block V6, row V6-1; computed by comparing the two shipped JSON ledgers):

| Quantity | Value |
|---|---|
| v1.4 rows | 204 |
| carried forward with **identical claim string and identical residual** | **200** |
| retyped or replaced | **4** — one in block X (the uniqueness row), three in block Y (the Bessel rows) |
| new in v1.5 | 20 |
| carried rows with any residual drift | **0** |

**The accurate form of words**, adopted everywhere in this version: *"the vN computations are regression-preserved except for the explicitly retyped or replaced rows; unchanged segments are carried forward with identical residuals."* Row-for-row prefix identity was never true across a retyping release and must not be asserted. For v1.5 → v1.6 the stronger statement does hold: **all 220 rows carried forward unchanged, 8 added.**

### 46.2 Gate K — front-matter consistency

v1.5 failed front-matter consistency in two places, both on its own first page:

| Where | v1.5 said | Contradicted by |
|---|---|---|
| Subtitle | "… and an **Unconditional** Goldstone No-Go" | the status line, "GOLDSTONE ROUTE CLOSED-NEGATIVE-**CONDITIONAL** ON (H-U1-BDY)" |
| Abstract, last sentence | "This paper is **not** terminal." | §44.3, "ZS-M61 v1.5 is **TERMINAL-IN-SCOPE**" |

**Corrections.** The subtitle now reads "**a Haar-Phase Goldstone No-Go**" — naming the hypothesis rather than the word "conditional", so the scope is carried by the physics term. The abstract now closes with the §44.3 statement in full: *within its declared scope ZS-M61 is TERMINAL-IN-SCOPE; the physical S14 selection remains OPEN and lies outside that closure.*

**Gate K is installed** as a permanent release requirement: title, subtitle, status line, the abstract's terminal sentence and §44.3 must agree, and `selfcheck.py` now checks all five (block V6, row V6-2). Gate **F-M61.44 (new)** fires on any release that has not passed it.

### 46.3 `FINAL` is not blocked by the DOI alone

v1.5's §44.3 said `FINAL` was unavailable "for one reason only: no DOI", while its own §44.2 listed **D-M61-PRIOR-2** — the systematic novelty sweep for Theorems M61.11 and M61.20 — as OPEN. Both cannot be true.

**Corrected statement**, now used verbatim in §44.3: *`FINAL` is withheld pending persistent archival identification. External novelty positioning for M61.11 / M61.20 remains OPEN under D-M61-PRIOR-2 and is not promoted by the TERMINAL-IN-SCOPE designation.*

This matters beyond bookkeeping. TERMINAL-IN-SCOPE certifies that the declared scope is closed; it certifies nothing about how the results sit in the external literature, and the two must not be allowed to blur.

### 46.4 NC-M61.21, folded

v1.5's NC-M61.21 still contained the v1.4 clause "which is what an exactly flat potential gives", immediately before NC-M61.25 withdrew exactly that inference. The clause is deleted; NC-M61.21 now states only that the phase law is not derived from the action, and the withdrawal lives in NC-M61.25 alone. One statement, one place.

### 46.5 The artifact's self-description

Two stale strings in the shipped artifact, neither affecting a computation: the docstring's run command still read `python3 zs_m61_verify_v1_1.py`, and §18.1's manifest still read `paper_code/version: ZS-M61 v1.1`. Both corrected, and row V6-5 now guards the docstring against recurrence by reading the script's own source.

### 46.6 What did not change

Row V6-6 pins the five constants that carry the paper, so that no future editorial pass can drift them:

**min J₀ = −0.402759395702552972 · Re λ = −0.566417330285464403 · T₂ = 0.835381287313629905 · c\* = 1.086474189775053007 · M\* = 0.763362818245963536**

together with the two inequalities the conclusions rest on, min J₀ > Re λ and T₂ > M\*, and the identity cos 2c\* = Re λ to 10⁻⁴⁵.

### 46.7 Release verdict

All six findings are **editorial**. The scientific core and the artifact's computations are unchanged; what changes is what the paper says about itself. The audit's own verdict — *AUDIT-CORRECTION-REQUIRED · SCIENTIFIC CORE SURVIVES*, with TERMINAL-IN-SCOPE to be re-granted after correction — is accepted in full, and the corrections are made here rather than deferred.

**On the discipline this exposes.** Three of the six defects (the subtitle, the abstract sentence, the subledger claim) are of one kind: **a statement about the paper that the paper did not check about itself**. v1.5 introduced `selfcheck.py` and it caught a numerical error the reviewers had missed — but its checks covered constants and cross-references, not self-description. v1.6 extends it to cover front matter and ledger provenance. The rule that follows, offered to the corpus:

> **Rule R12.** Any claim a paper makes *about its own artifact, its own status or its own version history* is a claim like any other and must be executable. If it cannot be checked by the release script, it must not be asserted.

---

## Appendix A — Verification ledger structure (91 rows, 0 FAIL, exit 0)

Table A.1. Ledger composition, **as banner-typed in v1.0** and **as retyped in v1.1**.

| Kind | v1.0 count | v1.1: rows with an executed test | v1.1: rows whose test is literal `True` |
|---|---|---|---|
| THEOREM-PROOF | 48 | 25 | 23 |
| NUMERIC-WITNESS | 16 | 15 | 1 |
| GUARD | 17 | 5 | 12 |
| DECLARATION | 10 | 0 | 10 |
| **Total** | **91** | **45** | **46** |

Table A.1b. The v1.1 artifact, `zs_m61_verify_v1_1.py`. No row is typed THEOREM-PROOF.

| Kind | Rows | Blocks |
|---|---|---|
| VERIFICATION | 65 | A–L, N |
| WITNESS | 6 | D, E, I, K |
| REGRESSION | 10 | A, R |
| GUARD | 10 | C, F, G, H, I, J, K, S |
| TAUTOLOGY | 2 | N |
| DECLARATION | 30 | A–N, R |
| **Total** | **123** | 101 legacy (A–M) + 10 new (N) + 9 errata (R) + 3 self-audit (S) |

Table A.1c. The v1.2 artifact, `zs_m61_verify_v1_2.py`. The v1.1 computations are regression-preserved.

| Kind | Rows | Blocks |
|---|---|---|
| VERIFICATION | 84 | A–L, N, P |
| WITNESS | 6 | D, E, I, K |
| REGRESSION | 10 | A, R |
| GUARD | 10 | C, F, G, H, I, J, K, S |
| TAUTOLOGY | 2 | N |
| DECLARATION | 35 | A–N, P, R |
| **Total** | **147** | 123 carried over + **24 new (block P)** |

Table A.1e. The v1.3 artifact, `zs_m61_verify_v1_3.py`. The v1.2 computations are regression-preserved.

| Block | Rows | Content |
|---|---|---|
| A–M | 101 | the v1.0 ledger, retyped |
| N | 10 | v1.1 audit integration |
| P | 24 | v1.2 breakthrough derivations, §§19–24 |
| **T** | **15** | **v1.3: A₅ irreps, the ZS-M10 tensor, the isotropy theorem, the W1/W3/W4 decision (§28)** |
| **U** | **5** | **v1.3: the general M\*(a; u) against an arc LP (§29)** |
| **V** | **9** | **v1.3: the kink-weight FWD-I computation and the FWD-R chain (§30)** |
| **W** | **5** | **v1.3: prior art and release status (§§31–32)** |
| R | 9 | errata regression |
| S | 3 | self-audit |
| **Total** | **181** | 134 tested, 47 declarations |

Table A.1f. The v1.4 artifact, `zs_m61_verify_v1_4.py`. The v1.3 computations are regression-preserved.

| Block | Rows | Content |
|---|---|---|
| A–W | 181 | the v1.3 ledger, carried over unchanged |
| **X** | **10** | **v1.4: the involution classification, the TYPE LOCK, the survival of Part IV (§34)** |
| **Y** | **7** | **v1.4: the Bessel no-go and the von Mises tautology control (§35)** |
| **Z** | **6** | **v1.4: the broken-seam budget, the dual certificate, the stale-statement sweep (§§36–37)** |
| **Total** | **204** | 149 tested, 55 declarations |

Table A.1g. The v1.5 artifact, `zs_m61_verify_v1_5.py`. 200 of the 204 v1.4 rows are carried verbatim, 4 retyped or replaced, 20 new.

| Block | Rows | Content |
|---|---|---|
| A–Z | 205 | the v1.4 ledger, with two rows retyped in place and one exact-precision row added to Y |
| **V5** | **15** | **v1.5: the reflection conjugacy class at 401 angles, the SO(2) involution sweep, the integrated Bessel identity, (H-U1-BDY), D-M61-IOTA, the sequencing and the reading rule (§§40–43)** |
| **Total** | **220** | 154 tested, 66 declarations |

Table A.1h. The v1.6 artifact, `zs_m61_verify_v1_6.py`. The v1.5 computations are regression-preserved: all 220 rows carried forward unchanged, 8 rows added.

| Block | Rows | Content |
|---|---|---|
| A–V5 | 220 | the v1.5 ledger, carried forward with identical residuals |
| **V6** | **8** | **v1.6: measured ledger provenance, Gate K, the FINAL wording, the NC-M61.21 fold, the artifact self-description guard, and a pin on the five core constants (§46)** |
| **Total** | **228** | 157 tested, 71 declarations |

Table A.1d. Block P, the breakthrough block, by section.

| Rows | Section | What is certified |
|---|---|---|
| P1–P4 | §19 | a = Φ_P(−2c) in dimensions 2–21 with arbitrary spectrum in [−1,1]; the two-atom special case; a symmetric marginal gives a real multiplier |
| P5–P8 | §20 | the universal phase floor over six support radii, 1200 random laws; tightness to 10⁻¹⁴; the ε_max = 1 and ε_max = 0.5, 0.1 cases |
| P9–P13 | §21 | the T(u) quadratic residual below 10⁻⁴⁵ at fifty digits; agreement with an independent arc LP; T(φ) = T₂ and T(π) = M\* exactly; strict monotonicity on a 401-point sweep; the c ≥ π/2 threshold |
| P14–P16 | §22 | FWD-R's one-sidedness by exhaustive search at c = 0.95 c\*; FWD-I's target |
| P17–P19 | §23 | |a| ≥ |Re λ| over 6000 holonomy draws; the c = π/4 exclusion |
| P20–P24 | §24–§25 | codimension-1 reachability, the sensitivity 0.714693, the non-identifiability fallback, the Ward reduction |

Table A.2. Selected residuals, **as emitted by the shipped artifact**. Values that v1.0 printed differently are flagged ✗ and listed in D.2.

| Row | Claim | Artifact residual | v1.0 printed |
|---|---|---|---|
| A2 | λ = z\* ln i = Log z\* | 1.34 × 10⁻⁵¹ | 1.3 × 10⁻⁵¹ ✓ |
| C1 | det V = +1 over 400 draws, dim 2–8 | 9.11 × 10⁻¹⁵ | 9.1 × 10⁻¹⁵ ✓ |
| C2 | J\_E V J\_E = V† over the same draws | 1.79 × 10⁻¹⁵ | 8 × 10⁻¹⁵ ✗ |
| C5 | A covariant V with det V = −1 exists (guard) | 0 (exact construction) | ✓ |
| D1 | \|a\| ≥ cos(w/2) over 2000 draws with w ≤ π | worst margin −1.48 × 10⁻⁶ | "no violation" ✓ |
| E1 | Re Tr(ρV) = ½ Tr V over 600 draws | 8.88 × 10⁻¹⁶ | 1.3 × 10⁻¹⁵ ✗ |
| F1–F5 | T\_min(d) against T₂ and M\* | 0, 0, 1.11e−16, 1.11e−16, 2.22e−16 | < 10⁻⁸ each ✓ |
| F7 | With det V = −1 admitted, d = 3 reaches M\* (guard) | < 10⁻⁶ | ✓ |
| G7 | 1 − T₂² = (1 − \|λ\|²)/(1 − Re²λ) | < 10⁻⁴⁰ | ✓ |
| H3 | a = cos 2c − i sin 2c ⟨ε⟩, dim sweep {2,3,4,5,7,9,12,20} × 40 = **320 draws** | 1.73 × 10⁻¹⁵ | "480 draws", 1.7 × 10⁻¹⁵ ✗ (count) |
| H5 | Reconstructed a equals λ | **2.67 × 10⁻⁵¹** | 1.2 × 10⁻⁴⁶ ✗ |
| I1 | No zero in 8000 random graded families | min \|a\| = **2.31 × 10⁻³** | 1.8 × 10⁻³ ✗ |
| J1–J7 | M\*(a) closed form vs 1800-atom LP | 1.92e−7, 0, 2.38e−7, 8.67e−7, 4.33e−7, 1.11e−16, 0 | see Table 10.1 ✗ |
| K1–K3 | Anti-numerology p-values over **3362** formulas | 2.97e−4, 0, **2.97e−4** | 0.00038, 0, **0** ✗ |

---

## Appendix B — Primal/dual certificate for Theorem M61.11

Write μ = μ\_even + μ\_odd under φ ↦ −φ. Then TV(μ, μ̌) = ‖μ\_odd‖, the barycentre real part depends only on μ\_even and the imaginary part only on μ\_odd. The primal problem is

minimise ‖μ\_odd‖ subject to ∫ cos φ dμ = x, ∫ sin φ dμ = y, μ ≥ 0, ‖μ‖ = 1 .

The dual has variables (u, v, w) and the constraint u cos φ + v sin φ + w ≤ the sign-envelope of the odd cost at every φ, with objective ux + vy + w. Inside the diamond |x| + |y| ≤ 1 the dual optimum is (0, sgn y, 0), certifying M\* = |y|; a feasible primal attaining it places mass |y| at sgn(y)·π/2 and splits the remainder between ±1 to supply x. Outside the diamond the dual optimum is supported on the active endpoint s ∈ {±1} with 1 − sx > 0, and complementary slackness forces the primal to two atoms: one at s and one at the angle α with tan(α/2) = y/(1 + sx). Substituting the atom masses gives

M\*(a) = |1 − sa|² / (2(1 − sx)) ,

and the mirror atom at −α acquires exactly zero mass, which is the degeneracy that makes the bound sharp. For the frozen λ the active endpoint is s = −1 and the formula returns ZS-M60.23. The seven test targets of Table 10.1 exercise both branches and both boundary cases.

---

## Appendix C — Constants printed by ZS-M61 v1.1

Table C.1. Every constant printed, with its defining closed form. Twenty-one significant digits; all recomputed from z\* at fifty digits and **independently re-verified on 17 August 2026 — all 23 entries reproduce to the printed digit.**

| Constant | Closed form | Value | Depends on (H-VAC-BDY)? |
|---|---|---|---|
| φ | arccos(Re λ) | 2.172948379550106013483 | no |
| c\* | ½ arccos(Re λ) | 1.086474189775053006742 | **yes (identifiability)** |
| sin(φ/2) | √((1 − Re λ)/2) | 0.884990771218961469989 | no |
| sin φ | √(1 − Re²λ) | 0.824118564256555945211 | no |
| Tr V | 2 Re λ | −1.132834660570928805351 | no |
| T₂ = \|⟨ε⟩\*\| | \|Im λ\| / √(1 − Re²λ) | 0.835381287313629904738 | **no** |
| T₂ − M\* | — | 0.072018469067666368243 | no |
| p(selected) | (1 + T₂)/2 | 0.917690643656814952369 | yes |
| p(other) | (1 − T₂)/2 | 0.082309356343185047631 | yes |
| purity floor | (1 + T₂²)/2 | 0.848930947596888738011 | no |
| linear-entropy ceiling | (1 − T₂²)/2 | 0.151069052403111261989 | no |
| entropy ceiling (nats) | H₂((1 + T₂)/2) | 0.284373704659211442818 | no |
| entropy ceiling / ln 2 | — | 0.410264533471067056322 | no |
| fidelity ceiling | √(1 − T₂²) | 0.549670905912094390502 | no |
| seam-overlap ceiling | (1 − \|λ\|²)/(1 − Re²λ) | 0.302138104806222523977 | no |
| decoherence budget | ln(1/T₂) | 0.179867026842394922715 | no |
| event count n\_max | ln(1/T₂)/μ | **1.566313529988409309620** | no |
| Gaussian core ε\*/σ | √(−ln(1 − T₂²)) | 1.094016026141528728708 | no |
| kink core (r\* − r\_H)/L\_⊥ | arctanh T₂ | **1.205687778651241392710** | no |
| arc gate | 2 arccos\|λ\| | 0.940241632013553311199 | no |
| realised arc | 2π − 2φ | 1.937288548079374449960 | no |
| 1 − Re λ | — | 1.566417330285464402675 | no |
| τ\* [CONDITIONAL DIAGNOSTIC] | c\* / √(**A**/**Q**) | **12.732757052335129785** | yes |

**Sixteen of the twenty-three constants are independent of (H-VAC-BDY).** That is the quantitative form of the claim in §7.3 that the paper retains substantial value under the worst case.

---

## Appendix D — Correction log (v1.0 → v1.1)

Nothing is deleted. Every superseded statement is recorded in place.

### D.1 Claim-level corrections

| Source | Superseded statement | Correction in v1.1 |
|---|---|---|
| Title | "The Terminal Physical Bridge of the ZS-S14 Boundary Process" | Retitled; §14.1 states why the terminal rule fails. |
| §0 Abstract | "ZS-M61 performs the repair inside itself and then closes the bridge." | The bridge is not closed; the realisation class is classified and the forward selection is registered as D-M61-FWD. |
| §0 Abstract, §7.2, §14 | "The zero-free-parameter requirement therefore selects the two-atom vacuum law rather than assuming it." | RETRACTED. Parameter counting excludes broader laws from being zero-parameter; it does not select the law from the action (§7.2 consequence 3). |
| Theorem M61.7 name and status | "Zero-Parameter Selection and the Terminal Solution", DERIVED-CONDITIONAL | Theorem M61.7′, DERIVED-CONDITIONAL + **IDENTIFIABILITY**; algebraically identical to ZS-M57 M57.C.2 under φ = 2c, s = ⟨ε⟩; zero evidential content for the derivation of λ (§7.2a). |
| §7.1 reading | "(H-DOUBLET-SUPPORT) … is replaced by the weaker and corpus-supplied (H-VAC), which ZS-M57 §16.3 already records as a fact about the bulk." | RETRACTED. (H-VAC-BULK) ⇏ (H-VAC-BDY); ZS-M57 §16.3 localises the physical mediation at ε(r\_H) = 0 (§7.3). Debt D-M61-VAC. |
| (H-VAC) status | HYPOTHESIS-strong | Split; (H-VAC-BDY) is HYPOTHESIS with a recorded material conflict. |
| Theorem M61.10 | "the zero set … is empty for every family in general position; … D\_phys = 0", CLOSED-NEGATIVE | Theorem M61.10′, DERIVED-CONDITIONAL on (H-GP), CLOSED-NEGATIVE-**GENERIC**; actual-family transversality gated by F-M61.18 (§9). |
| Theorem M61.12 | "Terminal S14 Bridge", CLOSED-POSITIVE-CONDITIONAL | Theorem M61.12′, Conditional S14-Compatible Realisation; selection restored to OPEN. |
| Status line | "TERMINAL · NO SUCCESSOR RESERVED" | REVIEW-READY · MAJOR REVISION INTEGRATED · NOT TERMINAL · one forward deliverable registered. |
| NC-M61.9 | "No successor paper is reserved." | NC-M61.9′; D-M61-FWD, D-M61-VAC, D-M61-PRIOR, D-M57-SIGN registered. |
| Banner | "91/91 PASS (48 THEOREM-PROOF …)" | Retyped census; 23 of 48 are literal `True` (Appendix E). |
| Banner | "Zero Free Parameters" | "Zero additional fitted numerical parameters, conditional on the declared structural model (C1–C6)." |
| §4.2 | Theorem M61.2(iii) presented as new structure the corpus had not extracted | Retained; prior-art scoped as a Cartan-embedding/symmetric-space fact with a new graded identification (F-M61.19). |
| §10 | Theorem M61.11 presented as novel | Prior-art status NOT\_FOUND, not NEW; D-M61-PRIOR registered (F-M61.23). |
| §7.3 (v1.0 §8.1) | "seam-ℤ₂ asymmetry T = 0.835 (attained)" listed among DERIVED-CONDITIONAL rows without separating bound-rows from value-rows | Table 8.1 now marks which rows survive the failure of (H-VAC-BDY). |
| Acknowledgements | "Every deterministic figure printed in this manuscript appears verbatim in one seeded run." | **Withdrawn** (D.2). |
| Code paragraph | "exit code 1 on any FAIL **or on a row-count mismatch**"; "Exactly 91 ledger rows in every scenario" | Withdrawn; no such guard exists. Required change in §18.2(1). |

### D.2 Manuscript-versus-artifact numerical errata

Every figure below was printed in v1.0 and disagrees with the shipped `zs_m61_verify_v1_0.json`. None changes a conclusion; all are corrected in v1.1.

| Location | v1.0 printed | Artifact value |
|---|---|---|
| §4.2, App. A.2 (row C2) | 8 × 10⁻¹⁵ | 1.79 × 10⁻¹⁵ |
| §6, App. A.2 (row E1) | 1.3 × 10⁻¹⁵ | 8.88 × 10⁻¹⁶ |
| §0, §7.2, Table 14.1, §17, App. A.2 (row H5) | 1.2 × 10⁻⁴⁶ | **2.67 × 10⁻⁵¹** |
| §7.1 (row H3) | "480 draws" | 320 draws (8 dimensions × 40) |
| §9, App. A.2 (row I1) | min \|a\| = 1.8 × 10⁻³ | 2.31 × 10⁻³ |
| Table 10.1 row 1 | 9.4 × 10⁻⁸ | 1.92 × 10⁻⁷ |
| Table 10.1 row 2 | 5.6 × 10⁻¹⁷ | 0.0 |
| Table 10.1 row 3 | 1.1 × 10⁻⁷ (LP 0.610000112) | 2.38 × 10⁻⁷ |
| Table 10.1 row 4 | 2.0 × 10⁻⁷ (LP 0.250000200) | 8.67 × 10⁻⁷ |
| Table 10.1 row 5 | 1.0 × 10⁻⁷ (LP 0.125000100) | 4.33 × 10⁻⁷ |
| Table 10.1 row 6 | 0.0 | 1.11 × 10⁻¹⁶ |
| §11.2, Table 11.2 | 2652 admissible expressions | **3362** |
| Table 11.2, App. A.2 (K3) | p(selected): 0 hits, p = 0.00000 | **1 hit, p = 2.97 × 10⁻⁴** |
| Table 11.2, App. A.2 (K1) | p = 0.00038 | 2.97 × 10⁻⁴ |

### D.3 Ledger claim-string errata (artifact-internal)

| Row | Claim string as shipped | Correct value |
|---|---|---|
| L (n\_max) | "n\_max = ln(1/T2)/mu = 1.5663135299884**07**" | 1.5663135299884**09** |
| L (kink core) | "kink core (r\*−r\_H)/L\_perp = arctanh(T2) = 1.20568777865124**4**" | 1.20568777865124**1** |
| L (τ\*) | "tau\* = c\*/sqrt(A/Q) = **12.7319**" | **12.7328** (12.732757052335130) |

All three rows are literal-`True` DECLARATION-class rows, so nothing tested the strings. That is the point: an untested claim string is exactly where a digit error survives.

### D.5 Erratum, v1.4 → v1.5 (found by the self-consistency audit)

| Location | v1.4 printed | Exact value |
|---|---|---|
| §35.1, §35.2, abstract, version history | *(superseded)* min J₀ = −0.402759395329850 | **−0.402759395702552972** |
| §35.2, abstract | *(superseded)* deficit = 0.163657934955614 | **0.163657934582911431** |
| §35.1 | *(superseded)* argmin ≈ 3.831662950 | **j₁,₁ = 3.83170597020751232** |

Cause: the minimum was read off a 600001-point grid on [0.001, 60] and then printed to fifteen digits. The stationary points of J₀ are the zeros of J₁, so the v1.5 artifact computes J₀(j₁,₁) exactly at fifty digits and additionally records the grid estimate for comparison — the two agree to nine digits and no further. **The inequality min J₀ > Re λ is unaffected and no conclusion changes.** This is the same error class as v1.0's Appendix D.2, which is why §18.2(8) now makes the audit mandatory rather than advisory.

### D.4 Upstream debt raised by this audit

**D-M61-HIST (new in v1.2).** The second audit recorded its finding in `history.md` under identifier H-0008, which is already occupied by the 돌파 v1.0 → v1.1 protocol revision; this paper's own audit rows occupy H-0009 … H-0014. Two events under one identifier breaks the append-only register. Not this paper's to fix; the recommended resolution is reassignment to the next free identifier, recorded as its own row.

**D-M61-WARD (v1.2): EXECUTED IN v1.3 AND NOT DISCHARGED — WORSE.** W2 holds. **W1 FAILS** on the H_id branch by Theorem M61.19: the Yukawa term is linear in H₅ and no slot of the **5** can carry zero weight. W3 is upstream-ambiguous. W4 is moot given W1. See §28 and the dichotomy of §28.5.

**D-S14-PHI (v1.3): ESCALATED in v1.4 to an ERRATUM RECOMMENDATION.** ZS-S14 v2.0 asserts two incompatible identifications of Φ (§7.1 D₃-trivial versus §7.5 neutral component of the D₃-2 doublet). §38.1 sets out the recommended four-item dated erratum; no numerical output of ZS-S14 changes. Severity **S3**.

**D-F1-EPS (new in v1.4).** The corpus phrase "vacua ε = ±1", originating in ZS-A3, quoted by ZS-M57 §16.3, inherited by ZS-M60's re-typing of F-M54-16′ and by ZS-M61 v1.0–v1.3, is a mis-statement: ZS-F1 §2.3 gives ε ≡ \|Φ\| ≥ 0 and the vacuum manifold is the circle \|Φ\| = 1. Every place the two-point reading is load-bearing must be re-derived. Upstream, [OPEN], propagating.

**D-M61-IOTA (new in v1.5).** The typed intertwiner ι_ZΦ : ℋ_Z^parity → span_ℝ{Re Φ, Im Φ} with ι∘J_Z = J_C∘ι, which would identify ZS-F0's abstract parity eigenbasis with the ZS-F1 field coordinates. Not constructed, not assumed. Registered OPEN; it is step 3 of the §42 sequence and it gates any reassessment of ZS-F0.

**D-M61-GOLD (new in v1.4).** Does anything in the Z-Spin action give the Goldstone θ a potential at the boundary? If no, Theorem M61.23 closes the graded route negatively. If yes, its concentration must be computed target-blind and compared once with κ\* = 3.740875.

**D-M61-ARC (v1.2): CLOSED in v1.3** by Theorem M61.20 (§29).

**D-M61-PRIOR (v1.1): EXECUTED in v1.3** with locators (§31); NOT_FOUND retained. A systematic sweep is registered as **D-M61-PRIOR-2**, not performed.

**H-KINK-WEIGHT (new in v1.3).** The hypothesis that the ε-marginal is the pushforward of a classical radial weight along the ZS-A3 kink. Used only in §30, only to close a sub-branch negatively.

**D-M61-ARC (new in v1.2).** The general two-parameter closed form M\*(a; u), of which Theorem M61.11 is u = π and Theorem M61.15 is a = λ. The outer-branch derivation generalises verbatim; the inner-diamond branch and the feasibility boundary are open.

**D-M61-NONID (new in v1.2).** The pre-registered alternative outcome: the S14 Action-to-Channel Non-Identifiability Theorem of §24.3.

**D-M61-VAC (v1.1): CLOSED — DISSOLVED** by Theorem M61.13 and priced by Theorem M61.14 (§19.3, §20.3).

**D-M61-FWD (v1.1): RETIRED**, split into FWD-R and FWD-I (§22).

**D-M57-SIGN.** ZS-M57 v1.8 carries two mutually inconsistent sign conventions for s: Theorem M57.C.2 prints λ = cos φ + i s sin φ with s = +Im λ/√(1 − Re²λ), while §11.2 and Appendix C use λ = cos φ − i s sin φ with s = −Im λ/sin φ. Not this paper's to fix; recorded so that the M57.C.2 ↔ M61.7′ correspondence is cited with the right pairing (§7.2a).

---

## Appendix E — The 23 THEOREM-PROOF rows whose test is the literal `True`

Established by abstract-syntax-tree audit of the 72 static `row(...)` call-sites in `zs_m61_verify_v1_0.py`. Each row below has a written proof in the body; none is computationally certified by the script, and each is **retyped DECLARATION** for census purposes. Line numbers refer to the shipped script.

| Line | Block | Claim string | Where the proof is |
|---|---|---|---|
| 58 | C | spec V conjugation-closed | §4.2 (ii) |
| 59 | C | mult(−1) in spec V is even | §4.2 (iv) |
| 75 | D | w\_min(spec V) ≥ 2 arccos\|λ\| = 0.9402416320135533 | §5.1 |
| 91 | E | spec V = {e^{±i arccos(Re λ)}} forced by Re a = Re λ | §6 |
| 93 | E | Im a = sin φ (n̂ · r), n̂ ⊥ seam axis | §6 |
| 95 | E | T ≥ \|Im λ\|/√(1 − Re²λ) = T₂ | §6, §5.2 |
| 133 | G | MaxEnt admissible state is diagonal in the ε basis | §8.1 |
| 134 | G | populations (1 ∓ T₂)/2 | §8.1 |
| 135 | G | ⟨ε⟩ = −T₂ | §7.2 |
| 136 | G | purity floor (1 + T₂²)/2 | §8.1 |
| 137 | G | entropy ceiling H₂((1+T₂)/2) | §8.1 |
| 138 | G | fidelity ceiling √(1 − T₂²) | §8.1 |
| 149 | H | ε·Z\_path vertex: B₀ = g ε̂ is exactly seam-odd | §7.1 |
| 150 | H | V = exp(−2 i c ε̂), c = τg | §7.1 |
| 164 | H | c\* = arccos(Re λ)/2 | §7.2 |
| 167 | H | general identity v sin c = sin(φ/2) | §7.4 |
| 168 | H | non-perturbative threshold c ≥ φ/2 | §7.4 |
| 182 | I | a = 0 requires Tr V = 0 AND r ⊥ n̂ : codimension 2 | §9 |
| 183 | I | D\_phys = 0 on the graded 2-dim carrier (empty divisor) | §9 — **and this is the row whose quantifier v1.1 corrects** |
| 228 | L | budget ln(1/T₂) | §8.2 |
| 229 | L | n\_max = ln(1/T₂)/μ | §8.2 (digit error, D.3) |
| 233 | L | Gaussian core ε\*/σ | §8.2 |
| 234 | L | kink core arctanh(T₂) | §8.2 (digit error, D.3) |

Also literal `True`: 10 DECLARATION rows (by design), 12 GUARD rows (4 static plus the 8-row block-M loop), and 1 NUMERIC-WITNESS row ("Tr V = 2 Re λ = −1.13283466057092880535", line 92), which asserts a 21-digit value without computing it and is retyped DECLARATION.

---

## References

[1] I. Marvian and R. W. Spekkens, "The theory of manipulations of pure state asymmetry: I," New J. Phys. **15**, 033001 (2013).
[2] I. Marvian and R. W. Spekkens, "Extending Noether's theorem by quantifying the asymmetry of quantum states," Nat. Commun. **5**, 3821 (2014).
[3] C. A. Fuchs and J. van de Graaf, "Cryptographic distinguishability measures for quantum-mechanical states," IEEE Trans. Inf. Theory **45**, 1216 (1999).
[4] W. F. Stinespring, "Positive functions on C\*-algebras," Proc. Am. Math. Soc. **6**, 211 (1955).
[5] K. Kraus, *States, Effects, and Operations* (Springer, Berlin, 1983).
[6] M. B. Ruskai, "Beyond strong subadditivity," Rev. Math. Phys. **6**, 1147 (1994).
[7] M. A. Nielsen and I. L. Chuang, *Quantum Computation and Quantum Information* (Cambridge Univ. Press, 2000), ch. 9.
[8] R. A. Horn and C. R. Johnson, *Topics in Matrix Analysis* (Cambridge Univ. Press, 1991), ch. 1.
[9] F. Hausdorff, Math. Z. **3**, 314 (1919); O. Toeplitz, Math. Z. **2**, 187 (1918).
[10] I. Schur, Sitzungsber. Preuss. Akad. Wiss., 406 (1905).
[11] J.-P. Serre, *Linear Representations of Finite Groups* (Springer, 1977).
[12] H. Weyl, Math. Z. **24**, 328 (1926).
[13] R. P. Feynman and F. L. Vernon, Jr., Ann. Phys. (N.Y.) **24**, 118 (1963).
[14] J. Schwinger, J. Math. Phys. **2**, 407 (1961).
[15] G. Kőnigs, Ann. Sci. Éc. Norm. Sup. (3) **1**, Suppl. 3 (1884).
[16] G. B. Dantzig, *Linear Programming and Extensions* (Princeton Univ. Press, 1963).
[17] R. E. Moore, R. B. Kearfott and M. J. Cloud, *Introduction to Interval Analysis* (SIAM, 2009).
[18] K. Kang, *Geometric Impedance: A = 35/437*, ZS-F2 v1.0 (2026).
[19] K. Kang, *Gauge Symmetry Constraint: Why Q = 11*, ZS-F5 v1.0 (2026).
[20] K. Kang, *The i-Tetration Fixed Point and the Koenigs Multiplier*, ZS-M1 (2026).
[21] K. Kang, *Master Action Total Closure*, ZS-S14 v2.0 (May 2026).
[22] K. Kang, *The Mediator-Graph Transduction Theorem*, ZS-M54 v2.2 (2026).
[23] K. Kang, ZS-M56 v1.8 (2026). **[Theorem M56.7: a two-parameter fit against two constraints carries zero evidential content — the rule that governs §7.2.]**
[24] K. Kang, *The Odd Carrier*, ZS-M57 v1.8 (2026). **[Theorem M57.C.2 and §11.3: the λ ↔ (φ, s) bijection and its non-evidential verdict; §16.3: the bulk vacuum and the ε(r\_H) = 0 anchor localisation. The two load-bearing upstream citations of this revision.]**
[25] K. Kang, ZS-M59 v1.8 (July 2026).
[26] K. Kang, *The S14 Seam-Transport Dichotomy*, ZS-M60 v1.5 (July 2026).
[27] K. Kang, ZS-S28 v3.1 (2026).
[28] K. Kang, *The Dephasing Representative and the Born Rule from i-Tetration*, ZS-Q18 v1.7 (2026).
[29] K. Kang, *The z\*-Locked Low-ℓ CMB Transfer*, ZS-U12 v2.3 (2026).
[30] K. Kang, ZS-A3, ZS-Q7 and ZS-U9 (2026).

*A note on references, new in v1.1.* Standard sources for the Cartan-embedding determinant fact (§4.2) and for the moment-problem atom-reduction used in Appendix B are **not yet cited by locator**, because a targeted prior-art search has not been performed. Deliverable D-M61-PRIOR covers both, together with the novelty status of Theorem M61.11. Until it is executed, the corresponding novelty statements carry the NOT\_FOUND tag and no more.

---

## Version History

**v1.1 (17 August 2026 KST): audit integration; major revision; claim scope reduced throughout.** Integrates an independent adversarial audit whose four central findings are accepted in full. (1) Theorem M61.7 is renamed M61.7′ and re-typed from a selection theorem to an **IDENTIFIABILITY** result, because under φ = 2c, s = ⟨ε⟩ it is algebraically identical to ZS-M57 Theorem M57.C.2, which ZS-M57 §11.3 had already judged to transport rather than derive λ with zero evidential content under ZS-M56 Theorem M56.7. (2) Theorem M61.10 is renamed M61.10′ and its quantifier corrected from universal to generic; status CLOSED-NEGATIVE → CLOSED-NEGATIVE-GENERIC, with actual-family transversality gated by F-M61.18. (3) (H-VAC) is split into (H-VAC-BULK) and (H-VAC-BDY); the latter is what the paper needs, does not follow from the former, is downgraded to HYPOTHESIS, and carries a recorded material conflict with the ε(r\_H) = 0 mediation locus of ZS-M57 §16.3 (debt D-M61-VAC). (4) Theorem M61.12 is renamed M61.12′ and the verdict CLOSED-POSITIVE-CONDITIONAL is withdrawn; the S14 selection of the realisation is restored to OPEN and registered as deliverable D-M61-FWD. The title, status line and abstract are rewritten accordingly; "Terminal Physical Bridge" and "no successor reserved" are withdrawn. Additionally: the verification banner is retyped after an AST audit showing 23 of 48 THEOREM-PROOF rows pass a literal `True` (Appendix E); the ledger is independently re-executed and reproduces byte-identically; fourteen printed residuals, two draw-counts, the anti-numerology family size (2652 → 3362) and one hit count (p(selected): 0 → 1) are corrected against the artifact (Appendix D.2), and the v1.0 claim that every deterministic figure appears verbatim in one seeded run is withdrawn; three ledger claim-string digit errors are recorded (Appendix D.3); the unqualified "zero free parameters" is replaced by an enumerated six-choice structural budget (§11.1a); prior-art scoping is added for Theorem M61.2(iii) and Theorem M61.11; eight new falsification gates F-M61.17–F-M61.24, two new non-claims NC-M61.10–NC-M61.11, one revised non-claim NC-M61.9′, four registered debts (D-M61-FWD, D-M61-VAC, D-M61-PRIOR, D-M57-SIGN) and one new corpus discipline rule (R11, §15.6) are added. A new release artifact `zs_m61_verify_v1_1.py` replaces the v1.0 script: 123 rows, 0 FAIL, no `THEOREM-PROOF` kind, a fail-closed row-count guard, an AST self-audit that refuses any tested row asserting a literal `True`, every printed digit generated from the computed value, a `figures.json` the manuscript is typeset from, a ten-row audit-integration block N (including the executable verification that Theorem M61.7′ *is* ZS-M57 Theorem M57.C.2 and the two tautology controls), a nine-row errata regression block R, and a three-row self-audit block S. Six of v1.0's literal-`True` statements are replaced by real computations rather than merely re-typed — among them the conjugation-closure and even-parity clauses of Theorem M61.2, the whole of the boundary-state ceiling table (now constructed on the actual 2×2 state), the seam-oddness of the vertex, the v sin c identity, the non-perturbative threshold, and the codimension-2 condition of §9 — and §9 gains an explicit one-parameter counterexample family that reaches a = 0 exactly, which is what makes the quantifier correction a theorem rather than an opinion. **No theorem of v1.0 is retracted as mathematics.** Every superseded statement is recorded in Appendix D.

**v1.6 (17 August 2026 KST): release audit; TERMINAL-IN-SCOPE re-asserted.** No number changes and no theorem is retracted. Six defects, all editorial, all of them statements the paper made about itself: **(1)** the subtitle said "Unconditional Goldstone No-Go" while the status line said CLOSED-NEGATIVE-CONDITIONAL — retitled "**a Haar-Phase Goldstone No-Go**"; **(2)** the abstract still ended "This paper is not terminal" while §44.3 declared TERMINAL-IN-SCOPE — replaced by the §44.3 statement in full; **(3)** "the v1.4 ledger is a strict subledger" was false because v1.5 retyped and reordered rows — replaced by the **measured** provenance, 200 of 204 rows carried verbatim with zero residual drift, 4 retyped or replaced, 20 new; **(4)** "`FINAL` unavailable for one reason only: no DOI" contradicted the paper's own open debt D-M61-PRIOR-2 — replaced by the archival-identification wording, with external novelty positioning explicitly not promoted by TERMINAL-IN-SCOPE; **(5)** NC-M61.21 retained a clause NC-M61.25 withdrew — folded; **(6)** the artifact's docstring run command and the §18.1 manifest version were stale — corrected and guarded. **Gate K** (front-matter consistency) and **Rule R12** (any claim about a paper's own artifact, status or history must be executable) are installed; `selfcheck.py` is extended to cover front matter and ledger provenance. New artifact `zs_m61_verify_v1_6.py`: **228 rows, 0 FAIL**, all 220 v1.5 rows carried forward with identical residuals, block V6 (8 rows) added. One new gate F-M61.44. **Status: TERMINAL-IN-SCOPE.**

**v1.5 (17 August 2026 KST): completion; TERMINAL-IN-SCOPE.** No new research; two v1.4 overclaims narrowed, one hypothesis named, one bridge registered, two verifier rows retyped, and a single reading rule installed so that Parts I–V are current without per-section edits. **Theorem M61.22′** replaces M61.22: the potential-preserving involutions are +I (trivial), −I (central, zero odd operators by ZS-M56 M56.22′) and a **single continuous conjugacy class of reflections** J_α : Φ ↦ e^{2iα}Φ̄, verified at 401 angles together with a 20001-point sweep confirming ±I are the only involutions in SO(2); the uniqueness claim is withdrawn, and the α-dependence of the odd mode is shown not to propagate because every Part IV result depends only on the law of the odd component. **D-M61-IOTA** registers the typed intertwiner ι_ZΦ that v1.4 assumed; consequently v1.4's claim that the corpus "already had" the right involution is narrowed to the abstract parity, and **ZS-F0 is not to be corrected on this evidence**. **(H-U1-BDY)** is named: a flat potential does not force a Haar state, spontaneous breaking being exactly the counterexample, so **Theorem M61.23′** is CLOSED-NEGATIVE-**CONDITIONAL**; its mathematics is unchanged and better certified, the Bessel identity now **integrated** at eight values of u where v1.4 asserted it while testing only mean(sin θ) = 0. v1.4's internal conflict between NC-M61.21 and §35.1 is resolved in favour of NC-M61.21. Stale non-claims NC-M61.3, NC-M61.12, NC-M61.13, NC-M61.14 rewritten; five superseded statements registered once in §43.3; the §44.1 board supersedes every earlier scoreboard. Five new gates F-M61.39–F-M61.43 and three new non-claims NC-M61.23–NC-M61.25. §42 sequences the upstream work: this completion, then the ZS-S14 erratum, then ι_ZΦ, then possibly ZS-F0, then the forward gates. New artifact `zs_m61_verify_v1_5.py`: **220 rows, 0 FAIL**, byte-identical on re-execution. **Status: TERMINAL-IN-SCOPE; no successor version of this paper is required.**

**v1.4 (17 August 2026 KST): the ZS-F1 type repair; the first target-blind no-go — stated unconditionally, narrowed to CLOSED-NEGATIVE-CONDITIONAL in v1.5.** ZS-F1 v1.0 §2.3 states that the legacy scalar is recovered as ε ≡ \|Φ\|, so ε ≥ 0 and ε ↦ −ε is not a map of the field space; the vacuum manifold is the circle \|Φ\| = 1, not {−1, +1}. **Theorem M61.22** classifies the involutions preserving V(\|Φ\|) and finds complex conjugation Φ ↦ Φ̄ to be the unique non-central one — matching ZS-M54 M54.8a and ZS-F0 Def 8.11 exactly — with even mode Re Φ and **odd mode Im Φ**; ε = \|Φ\| is seam-EVEN and cannot be the vertex operator. A **TYPE LOCK** separates ρ, θ and S := Im Φ (§34.3), and (H-VAC-BDY) is replaced by (H-QUAD), support at θ = ±π/2. **The whole of Part IV survives the substitution ε̂ → Ŝ verbatim**; only the §30 radial-weight computation is retired. **Theorem M61.23** then delivers the programme's first target-blind result (stated unconditionally in v1.4; narrowed in §41): for the uniform phase law that ZS-F1's exactly flat Goldstone potential supplies, a(c) = J₀(2c) is exactly real and min J₀ = −0.402759395702552972 > Re λ = −0.566417330285464, so **λ is unreachable at every accumulated phase**, deficit 0.163657934582911431, with no hypothesis and no fitted parameter — CLOSED-NEGATIVE unconditional. A von Mises bias with κ\* = 3.740875, c = 1.290067 reproduces λ to 5 × 10⁻¹⁵ but is a two-for-two fit (typed TAUTOLOGY) and costs the Goldstone its masslessness, contradicting ZS-F1 results 1 and 3: the §35.4 dichotomy. **Theorem M61.24** gives the broken-seam budget — phase floor ½arccos(Re λ + δ), asymmetry floor Lipschitz with coefficient 0.137289 — showing the Part IV floors are robust, not knife-edge. Theorem M61.20 gains a **dual certificate** with zero duality gap at u = φ, 2.6 and π, making it quotable without the verifier. Stale-statement sweep: NC-M61.3 and NC-M61.12 rewritten, title retitled, Theorem M61.12′ demoted to a counterfactual, and the M61.20 count corrected to 48 grid combinations / 39 finite comparison pairs. §38 gives the recommendation on ZS-S14: a four-item dated **erratum**, not a v3.0, with zero numerical outputs changed. Four new gates F-M61.36–F-M61.39, three new non-claims NC-M61.20–NC-M61.22, three new debts D-S14-PHI (escalated), D-F1-EPS, D-M61-GOLD. New artifact `zs_m61_verify_v1_4.py`: **204 rows, 0 FAIL**. **No theorem of v1.0–v1.3 is retracted as mathematics; one is retired as a physical computation because it averaged the seam-even variable.**

**v1.3 (17 August 2026 KST): the five open items executed; (F2) falsified on the H_id branch.** **Theorem M61.19 (Yukawa Slot Isotropy)**: reconstructing the A₅ irreps **3**, **3′**, **5** and rebuilding the ZS-M10 unique invariant, the Gram form on the Higgs index is G_{mn} = δ_{mn}/5 by Schur's lemma — reproducing ZS-M10's Σσᵢ² = 1/5 — so no slot of the **5** can carry zero Yukawa weight. Since the Yukawa term is linear in H₅, item **W1 of Reduction R1 FAILS** and (F2) is falsified at the classical level on ZS-S14's own hypothesis H_id; both escapes are blocked (σ does not commute with I, residual 1.603). Upstream debt **D-S14-PHI** registered: ZS-S14 v2.0 asserts two incompatible identifications of Φ, so W3 cannot be settled. The **dichotomy (§28.5)** and the **survival table (§28.6)** are the core of this version: four results — R0, Theorem M61.3, Theorem M61.11 and the new Theorem M61.20 — use neither (F2) nor the vertex form and are unaffected. **Theorem M61.20** closes D-M61-ARC: the general M\*(a; u) in closed form with feasibility boundary cos u ≤ x, inner-diamond branch and at-most-two-symmetric-atom extremal structure, certified on 46 (a, u) pairs to 4.2 × 10⁻⁶ with zero feasibility mismatches. **Theorem M61.21** gives the first target-blind number: ⟨ε⟩(p) = Γ(p+3/2)/(√π Γ(p+2)), equal to 1/2, 3/8, 5/16 for the arclength, energy-density and potential weights, all below T₂, which needs p\* = −0.847672 — **FWD-I CLOSED-NEGATIVE on the canonical-weight branch**. **D-M61-PRIOR executed** with locators, NOT_FOUND retained. **§18.2(7) closed.** **DOI still outstanding**, reduced to one manual step. Five new gates F-M61.32–F-M61.35, four new non-claims NC-M61.16–NC-M61.19. New artifact `zs_m61_verify_v1_3.py`: **181 rows, 0 FAIL**. **No theorem of v1.0–v1.2 is retracted as mathematics; what changes is the status of an assumption they shared.**

**v1.2 (17 August 2026 KST): second audit integrated; the six breakthrough routes executed.** The audit's one new finding — manuscript ↔ artifact desynchronisation, S2 — is accepted as correct against the copy audited and closed as already remediated in the v1.1 release action; the sync is re-verified and extended to the v1.2 artifact (§0.2a). A registry conflict raised by the same audit, the reuse of the occupied identifier H-0008, is registered as debt D-M61-HIST and left to the register owner. Six new theorems execute the six proposed routes. **Theorem M61.13** gives the multiplier as the characteristic function of the ε-marginal in every dimension with no support hypothesis, which **dissolves D-M61-VAC** and makes the environment-dimension cancellation unconditional. **Theorem M61.14** proves the universal phase floor c ≥ arccos(Re λ)/(2ε_max) with equality exactly on extreme support, which generalises Theorem M61.8 off the doublet, converts (H-VAC-BDY) from a hypothesis into an equality case, deletes structural choice C4, and prices anchor localisation. **Theorem M61.15** gives the arc-asymmetry function T(u) in closed form with T(φ) = T₂ and T(π) = M\* both exact and strict monotonicity between, making Theorem M61.4 a corollary and removing the dependence of T₂ on det V = +1 — so gate F-M61.2's consequence clause is corrected. **Theorem M61.16** restores the divisor result to unconditional CLOSED-NEGATIVE on the λ-compatible class and retires the 8000-draw witness. **Theorem M61.17** proves codimension-1 reachability, collapsing the whole forward content to \|⟨ε⟩\| = T₂ with sensitivity 0.714693. **Reduction R1** retypes (F2) from an all-orders check to five finite items, two settled and three registered as D-M61-WARD, with the structural conclusion that the seam ℤ₂ is broken only by the boundary condition at infinity — matching M57.P′ and §19.3 from a third independent direction. The single deliverable D-M61-FWD is split into the independent gates **FWD-R** and **FWD-I**; the alternative outcome is pre-registered as **D-M61-NONID**; **D-M61-ARC** registers the general M\*(a; u) closed form; §26 adds an externalisation plan with two proposed external papers. Eight new gates F-M61.25–F-M61.31, four new non-claims NC-M61.12–NC-M61.15, two new epistemic statuses (DISSOLVED, PRICED). New release artifact `zs_m61_verify_v1_2.py`: **147 rows, 0 FAIL**, adding block P (24 rows) as the executable content of §§19–24, with the v1.1 computations regression-preserved. A seventh artifact requirement is added after a near-miss in which a guard-test variant overwrote the release ledger (§18.2(7)). **No theorem of v1.0 or v1.1 is retracted as mathematics.**

**v1.0 (March 2026; released July 2026): initial public release.** Consolidated from internal research notes up to the ZS-M61 Successor Seed Report v1.1. Executed the ZS-S14 colour repair R0 in place and retracted ZS-S14 v2.0 Definition 3.1's colour clause and the single-carrier SU(3) closure of Theorem S14.E. Proved the Graded Relative-Unitary Structure Theorem det V = +1 (M61.2) and the Carrier-Dimension Theorem (M61.4), raising the minimal seam-ℤ₂ asymmetry from M\* = 0.763362818245964 to T₂ = 0.835381287313630 on carriers of dimension ≤ 3. Proved Real-Part Rigidity (M61.5) and Vacuum-Manifold Rigidity (M61.6), the latter removing (H-DOUBLET-SUPPORT). Solved the vacuum-supported boundary data in closed form (M61.7). Constructed the conditional boundary state and tightened all five ZS-M60 ceilings (M61.9). Proved the Non-Perturbative Threshold (M61.8). Proved the anchor divisor empty by a codimension count (M61.10). Stated and certified the general M\*(a) theorem (M61.11). Retired the ZS-M60.32 observation ⌊n\_max⌋ = 2 = dim **Z**. Sixteen falsification gates and nine non-claims. Verification 91/91 PASS, 0 FAIL. **Claimed TERMINAL and CLOSED-POSITIVE-CONDITIONAL; both claims are withdrawn in v1.1.**

Superseded internal drafts: ZS-M61 Successor Seed Report v1.0 (March 2026) and v1.1 (July 2026). The v1.0 seed diagnostics ē/σ, τ\_min = 13.238, σ² = λ\_V and r\*/ℓ\_P = 6.269 remain retired.
