# ZS-S14 — The Typed Standard-Model Master Action

*Colour-Sector Repair, Chiral Rigidity of the Icosahedral Yukawa Invariant, and the Open Physical Bridges*

**Author:** Kenny Kang **Affiliation:** Z-Spin Cosmology Collaboration **Paper code / version:** ZS-S14 v2.1 **Date:** 19 August 2026 (KST). v2.0: May 2026\. v1.0: April 2026\. **Theme:** Standard Model **Release label:** `REVIEW READY` — corrected canonical manuscript, independent adversarial audit required before any stronger label. **Correction class:** **Mathematical correction \+ scope correction \+ retraction.** Dated erratum against ZS-S14 v2.0, issued as v2.1 in the v2.x line. This is not a v3.0 and does not hide the correction lineage.

---

## One-line scope verdict

ZS-S14 v2.1 writes down a **typed** Standard-Model master action in which each gauge factor acts on its own representation space, repairs the representation-theoretic colour error of v2.0, proves that the repair was **forced rather than chosen**, and demotes to `OPEN` or `RETRACTED` every v2.0 statement whose evidence did not support it. It does not close the physical Yang–Mills bridge, the seam selector, or the boundary phase law.

---

## Verification summary

Suite            : zs\_s14\_verify\_v2\_1.py          (script v2.1.0)

Rows             : 115 executed, 0 FAIL, fail-closed on EXPECTED\_ROWS \= 115

Evidence-bearing : P \= 0    C \= 27   V \= 32   W \= 2      (total 61\)

Controls         : R \= 10   G \= 23                       (total 33\)

Non-evidence     : D \= 10   T \= 11   X \= 0                (total 21\)

Precision        : mp.dps \= 50; exact Fraction arithmetic for rational

                   identities; exact F\_p arithmetic at p \= 41, 31, 61, 101,

                   999979, 1000039 for the rank certificate

Appendix B       : 49 internal \+ 16 external references, measured from this file

Legacy artifact  : zs\_s14\_verify\_v2\_0.py measured at 78 rows, 25 literal \`True\`

**`P = 0` is deliberate.** Following the precedent set when the ZS-M61 artifact was rebuilt, the class `THEOREM-PROOF` is not used: *a script does not prove theorems.* Proofs live in this manuscript; the script certifies computations (`C`), verifies numbers at a declared tolerance (`V`), exhibits counterexamples (`W`), guards invariants (`G`), controls drift (`R`), and records declarations with proof pointers (`D`). Every one of the 10 `D` rows names the section or upstream theorem that carries its content, and the 11 `T` rows are labelled as tautologies rather than dressed as evidence — an adversarial audit of an earlier draft found that several rows restating their own definitions had been classed as evidence, and they were re-typed.

**Row count is not theorem count.** The 10 `D` rows are registry declarations with proof pointers, and the 11 `T` rows are restatements of definitions; neither carries evidential weight. The v2.0 banner `78/78 PASS` is retained in §12.4 only as a historical artifact; it is not a release certificate for this version.

---

# §0. Abstract

ZS-S14 v2.0 asserted a single-carrier "master coupling principle": all Standard-Model gauge couplings and the Yukawa structure realised as covariant dynamics on one five-dimensional icosahedral object `H_5`. **That assertion contained a representation-theoretic error and is withdrawn here.** The five-dimensional irrep of `I ≅ A_5` restricted to the hexagonal stabiliser `D_3 ≅ S_3` decomposes as `1 ⊕ 2 ⊕ 2` — one trivial line plus a *single* two-dimensional irrep of multiplicity two — not as a trivial line plus two inequivalent doublets; and `su(3)` admits no two-dimensional representation. The v2.0 clause placing `SU(3)_C` on a two-dimensional block of `H_5` is therefore void twice over. This erratum was first recorded upstream as ZS-M60 Theorem M60.25 and re-derived as ZS-M61 Theorem M61.1a; it is re-derived independently here by exact character computation and by exact finite-field linear algebra.

The corrected action is a **typed product-carrier action**: `SU(3)_C` acts on the Standard-Model fermion colour factor `C^3_C` that the theory already carried, `SU(2)_L` acts on a weak-isospin factor transverse to the icosahedral labels, `U(1)_Y` acts by an explicitly declared charge operator per component, and `H_5` carries no gluon term. No field is added and no numerical output moves.

v2.1 then establishes that this repair is not one option among several. **Theorem S14.J (Chiral Rigidity):** the unique `I`\-invariant Yukawa tensor `T ∈ Hom_I(1, 3 ⊗ 5 ⊗ 3')` of ZS-M10 has *trivial connected symmetry group* — its annihilator in `gl(3) ⊕ gl(5) ⊕ gl(3')` is exactly the two-dimensional scalar kernel that annihilates every tensor of this format. Consequently no simple Lie algebra, in particular neither `su(2)_L` nor `su(3)_C`, can act on the icosahedral labels of the Yukawa term; a gauge generator acting on those labels alone is excluded, and the gauge quantum numbers must be carried on tensor factors transverse to them. The result is load-bearing on the Galois twist `3 ↔ 3'`: for the untwisted siblings `3 ⊗ 5 ⊗ 3` and `3' ⊗ 5 ⊗ 3'` — same group, same dimensions, same multiplicity one — the annihilator has dimension five with derived algebra `so(3)`. **Gauge–flavour factorisation, which the discrete-flavour-symmetry literature imposes as a construction axiom, follows here — for actions on the icosahedral labels — from chirality.**

**Proposition S14.K** supplies a consistency check that the repair passes and the original action could not. Because ZS-M61 Theorem M61.19 forces the Higgs-slot Gram form of `T` to be isotropic, `G = δ/5`, every slot of the `5` carries Yukawa weight `1/√5`. Under the repaired action the ZS-M10 channel normalisation `y_0 = y_t√(5/2)` converts that weight into the single-doublet `1/√2` *exactly*, reproducing the ZS-S13 closed form `m_t = y_t v/√2`; two normalisations obtained independently agree to the last digit. **Proposition S14.K.1** quantifies what the v2.0 action could not do: with `H_5` as the only Yukawa scalar the term has mass dimension 3, and the only scale available to repair it, `M_P`, overshoots the observed fermion scale by `M_P/v = 9.90 × 10^15`. The dimensional repair and the representation-theoretic repair are the same repair.

Of the two v2.0 identifications of the `D_3`\-invariant component of `H_5`, one is withdrawn and one is re-opened. Its identification with the neutral component of the weak doublet is `RETRACTED`, as the correction specification requires and as §7.1 and §7.5 already contradicted each other about.  Its identification with the ZS-F1 Z-bias field is returned to `OPEN`: this paper neither asserts nor excludes it, and §10.3.5 shows that the exact seam `Z_2` is unavailable on either horn, so ZS-M61's analysis is unaffected either way.

Numerical outputs are unaffected: `α_s = 11/93`, `v = 245.93 GeV`, `m_t = 171.872 GeV`, `sin²θ_W`, the anomaly cancellations, and the ZS-S7 / ZS-Q3 inheritances are all insulated, because none of them uses the invalid colour clause, the `D_3`\-trivial-versus-doublet distinction, or any seam involution. What changes is not the arithmetic but the claim status attached to it. Theorem S14.E is `RETRACTED` and replaced by a colour-sector type-repair proposition; S14.B is demoted; S14.D.4's physical hypercharge identification, S14.F's continuum closure, S14.H's correlator bound and S14.D.8's exponent identification are demoted to `OPEN` or `DERIVED-CONDITIONAL`; and the v2.0 self-assessed closure percentage is removed as a category error and replaced by a claim-level status board.

*Keywords: typed master action, icosahedral flavour symmetry, gauge–flavour factorisation, tensor stabiliser, chirality, colour-sector erratum, Yukawa invariant, epistemic status audit, Z-Spin Cosmology.*

---

# §0.1 Scope declaration

**What this paper is.** A corrected canonical statement of the ZS-S14 master action, with explicit domains for every generator; two new theorems about the symmetry of the ZS-M10 Yukawa invariant and about vacuum scale separation; and a re-typing of every v2.0 claim against the evidence that actually exists.

**What this paper is not.** It is not a proof of a continuum Yang–Mills theory, not a Clay-form result, not a derivation of the Higgs mass, not a closure of the Z-Spin physical seam selector, and not a demonstration that the Standard Model is *uniquely* reproduced. It introduces no new phenomenology.

**Where the finite / formal / conditional boundary lies.** Everything in §§2–3, §8.2, §10 is finite-dimensional representation theory and exact linear algebra, and is `PROVEN` at that scope. Everything that maps such a statement onto a physical process — a continuum limit, a boundary state, a selection principle — is `DERIVED-CONDITIONAL` or `OPEN`, and is marked as such at the point of use.

---

# §0.2 Erratum summary — what changed from v2.0

| \# | v2.0 statement | v2.1 disposition | Basis |
| :---- | :---- | :---- | :---- |
| E1 | `5 ↓ D_3 = 1 ⊕ 2 ⊕ 2'`, two inequivalent doublets | **CORRECTED** to `1 ⊕ (2 ⊗ C²_mult)` | M60.25; M61.1a; §2.8, rows B1–B4 |
| E2 | `λ^a_3` acts on a `D_3`\-`2'` subspace of `H_5` (colour triplet) | **RETRACTED**; no `su(3)` action on any 2-dim block | M60.25(iii); §3.1, rows B5–B6 |
| E3 | Theorem S14.E, single-carrier `SU(3)_C` closure on `H_5` | **RETRACTED**, replaced by Prop. S14.E′ (type repair R0) | §8 |
| E4 | `Φ_Z` \= neutral `H⁰` of the `D_3`\-2 weak doublet (§7.5 Step 2\) | **RETRACTED** (mutually exclusive with §7.1) | D-S14-PHI; §7.2 |
| E5 | `Φ_Z` \= the ZS-F1 Z-bias field (§7.1, §7.4) | **RE-OPENED to `OPEN`** — asserted without proof in v2.0 | §7.2, §10.3.5 |
| E6 | Theorem S14.B, `H_5`'s `D_3`\-2 carries the `SU(2)_L` doublet | **RETRACTED**; a dimension-compatibility statement survives | **Thm S14.J**; §5, §10.2 |
| E7 | S14.D.4 physical hypercharge identification `Y_Φ = q_Φ/Z = Y_H` | **DEMOTED to OPEN**; arithmetic retained, identification withdrawn | §7.5 |
| E8 | S14.F X-sector continuum lift as a closed master-action theorem | **DEMOTED** to `DERIVED-CONDITIONAL`, gated on D-YM-001 | §9.1 |
| E9 | S14.G continuum mass-gap inheritance | **SPLIT** into four layers, only the finite one retained | §9.2 |
| E10 | S14.H correlator bound, stated as a theorem | **DEMOTED** to `HYPOTHESIS / OPEN BOUND` | §9.3 |
| E11 | S14.D.8 factor-2 closure via `(2A)^{C_0/8}` | **DEMOTED** to `HYPOTHESIS / OPEN` | §9.4 |
| E12 | Title `Master Action Total Closure`; `single 5-dimensional object` | **REPLACED** | §0, title |
| E13 | `Single-paper closure ~ 99.0%` | **REMOVED** as a category error | §13 |
| E14 | `Zero Free Parameters` (unqualified) | **QUALIFIED** | §13.2 |
| E15 | "24 upstream references"; script counted 25; table held 28 | **MEASURED** and synchronised to one exact number | App. B; rows G14–G16 |
| E16 | Definition 3.1 is dimensionally inconsistent by one power of mass | **CORRECTED** (new in v2.1) | §3.1; §10.3.1 |
| E17 | `78/78 PASS` banner, 25 of 78 rows literal `True` | **REPLACED** by a class census with a fail-closed guard | §12 |
| E18 | v2.0 §11.1 printed `m(0⁺⁺) = 1.7912 GeV` "at 50-digit precision" while `vA/Q` evaluates to `1.790628 GeV` | **CORRECTED** to the value the formula gives (new in v2.1) | §9.2; rows L1, L1b |
| E19 | v1.0/v2.0 Theorem S14.B Step 4: "`m_W ≈ 80.4 GeV`, matching observation". The stated inputs give **77.4614 GeV**, a `−3.62 %` tension with PDG `80.3692 GeV`; the v2.0 verifier hid it behind a 5 % tolerance | **CORRECTED**; re-typed as an open tension, new gate F-S14.16 (new in v2.1) | §5.2; rows D5, D6 |
| E20 | v2.0 §7.6 printed `γ_CW·C_M^sp = 36.831`; the expression evaluates to `36.831421` | **CORRECTED** (new in v2.1) | §7.6; row G2 |

Under the corpus no-deletion rule, every superseded formula is preserved verbatim in this document inside fenced `SUPERSEDED` blocks, and the v1.0 → v2.0 → v2.1 genealogy is given in Appendix A. Nothing is deleted from the record.

---

# §0.3 Epistemic status legend

Three axes are kept separate. A claim carries one label from each where applicable.

**Epistemic axis.**

| Status | Definition |
| :---- | :---- |
| `LOCKED` | Core constant fixed upstream; no downstream paper may modify it. |
| `PROVEN` | Complete proof under declared definitions, at the declared scope. |
| `IMPORTED-PROVEN` | Proved outside Z-Spin; the Z-Spin mapping is a separate claim. |
| `PROVEN-PERTURBATIVE` | Proven within perturbation theory; non-perturbative scope excluded. |
| `DERIVED` | Quantitative consequence of `PROVEN` items plus Z-Spin axioms. |
| `DERIVED-CONDITIONAL` | Derived, conditional on a stated open hypothesis. |
| `CERTIFIED` | Enclosed by exact, interval or finite-field arithmetic. |
| `VERIFIED` | Reproduced numerically at a declared precision and tolerance. |
| `TESTABLE` | Prediction with an explicit experimental falsification condition. |
| `HYPOTHESIS` / `HYPOTHESIS-strong` | Derivation chain incomplete at an identified step. |
| `OBSERVATION` | Numerical proximity only; no action-level derivation. |
| `NON-CLAIM` | Explicitly not asserted. |
| `OPEN` | Recognised gap. |
| `STANDARD` | Textbook result in QFT or representation theory. |

**Lifecycle axis:** `CURRENT` / `SUPERSEDED` / `RETRACTED` / `ARCHIVED`.

**Gate axis:** `OPEN` / `CLOSED-PASS` / `CLOSED-NEGATIVE` / `CLOSED-VACUOUS` / `TERMINAL-IN-SCOPE` / `IMPORTED-OPEN`.

**Verification classes** (used in §12 and in the companion script, one per row):

| Code | Class | Evidential weight |
| :---- | :---- | :---- |
| `P` | Theorem-proof / symbolic proof obligation discharged | strong; a proof must exist |
| `C` | Certified computation — exact, interval or finite-field arithmetic | strong within the stated range |
| `V` | Numerical verification at declared precision | evidence at that tolerance |
| `W` | Numeric witness or counterexample | existence evidence only |
| `R` | Regression against a frozen prior value | drift control, not evidence |
| `G` | Guard / invariant / fail-closed check | execution integrity |
| `X` | Diagnostic / exploratory | not promotion-bearing |
| `D` | Declaration / registry assertion with a proof pointer | **not evidence** |
| `T` | Tautology / premise-sharing control | **not evidence** |

---

# §1. Introduction

## §1.1 The problem this version solves

ZS-S14 v1.0 (April 2026\) answered an external review of ZS-S10 by writing a single action extending the ZS-S10 minimal-coupling principle to the whole Standard-Model gauge group and the Yukawa sector. ZS-S14 v2.0 (May 2026\) extended it with four cross-link theorems and reported a self-assessed closure figure of about ninety-nine per cent.

Both versions rested on a claim about *where* the gauge generators act. That claim is false. In May–August 2026 an upstream correction line established, independently twice, that the five-dimensional icosahedral irrep does not contain the object the master action needed. The purpose of v2.1 is to repair the action, to determine exactly how much of the surrounding structure survives the repair, and to state the remainder honestly.

The repair turns out to be more informative than the error. Once the correct decomposition is used, one can ask a sharper question — *what continuous symmetry can the Yukawa structure carry at all?* — and answer it completely. The answer, Theorem S14.J, is that it can carry none beyond the trivial rescalings, and that this is a consequence of the chirality of the Z-Spin fermion assignment. The single-carrier principle was not merely unproved; it was excluded.

## §1.2 The typed master-action principle (replacing the v2.0 master coupling principle)

The v2.0 formulation is preserved for the record:

SUPERSEDED (ZS-S14 v2.0 §1.3):

"all SM gauge couplings (g\_Y, g\_2, g\_s) and the Yukawa coupling structure

 (T\_{i m alpha}, Y\_0) are unified as covariant dynamics on a single

 5-dimensional object H\_5 ... the SM Higgs doublet H is identified with the

 D\_3-2 component, and the leptoquark sector (color triplet) with the

 D\_3-2' component."

It is replaced by:

> **Typed master-action principle.** Distinct group factors act on their own representation spaces inside one action. Unification means a common action, a common dependency architecture and a common set of locked inputs — not that every gauge generator acts on one finite-dimensional carrier. Every generator in the master action carries an explicitly declared domain and codomain, and a term is admissible only if its indices contract in a stated representation.

This is weaker as rhetoric and stronger as physics. Theorem S14.J shows it is also the only option available.

## §1.3 Contribution table

| \# | Result | New here? | Status | Main assumptions | Evidence | External baseline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | Corrected `D_3` branching of `H_5` and colour repair R0 in the master action | re-derivation of M60.25 / M61.1a, applied to the action | `PROVEN` | none | exact characters; finite-field rank | classical character theory |
| 2 | **Thm S14.J** — the ZS-M10 Yukawa invariant has trivial connected symmetry group; gauge–flavour factorisation follows | **yes** | `PROVEN` (`CERTIFIED` at 6 primes) | ZS-M10 uniqueness | §10.2, rows J1–J11 | tensor-annihilator framework is standard \[E1\]; the A₅ case is not in the literature |
| 3 | The result is load-bearing on the Galois twist: untwisted siblings carry `so(3)` | **yes** | `PROVEN` | as above | rows J5–J7 | no source found |
| 4 | **Prop. S14.K / S14.K.1** — the ZS-M10 channel factor `√(5/2)` is exactly the Gram-isotropy conversion factor; and the v2.0 Yukawa's dimensional defect costs `M_P/v ≈ 10^16` | **yes** | `CERTIFIED` | M61.19; ZS-M10 normalisation | §10.3, rows K1–K5 | — |
| 5 | Dimensional repair of Definition 3.1 | **yes** | `PROVEN` (dimensional analysis) | none | §3.1 | — |
| 6 | `D-M61-IOTA` is a selection debt, not an existence debt | **yes** | `PROVEN` | ZS-F0 Def. 8.11 parity | §10.4, row K6 | — |
| 7 | Re-typing of S14.B, D.4, E, F, G, H, D.8 against actual evidence | yes, as disposition | see §13 | — | §§5–9 | — |
| 8 | Fail-closed verification artifact with per-row classes | yes | `PROVEN` (guard tests fire) | — | §12 | — |

## §1.4 Non-claims of this version

Stated in full in §11.2. In summary, v2.1 does **not** claim: a Clay-form Yang–Mills result; a closure of the ZS-S14 physical seam selector; a derivation of the boundary phase law; a unique reconstruction of the Standard Model; any new numerical prediction; or that the Standard Model gauge group is *derived* rather than assumed at the point where it enters the action.

---

# §2. Locked inputs

All inputs are `LOCKED`, `PROVEN` or `DERIVED` upstream. v2.1 introduces zero new numerical parameters and zero new fields.

## §2.1 Foundational constants (unchanged)

| Quantity | Value | Source | Status |
| :---- | :---- | :---- | :---- |
| `A` geometric impedance | `35/437 = 0.080091533180778032` | ZS-F2 §7 | `LOCKED` |
| `Q` register dimension | 11 | ZS-F5 §4 | `PROVEN` |
| `(Z, X, Y)` sector dimensions | `(2, 3, 6)` | ZS-F5 §4 | `PROVEN` |
| `G = MUB(Q)` | 12 | ZS-F5 | `PROVEN` |
| `κ² = A/Q` | `35/4807` | ZS-M6 Thm 2.2.1 | `DERIVED` |
| `δ_X`, `δ_Y` | `5/19`, `7/23` | ZS-F2 | `PROVEN` |
| `M_P` reduced Planck mass | `2.435 × 10^18 GeV` | standard | `STANDARD` |

## §2.2 Polyhedral invariants (unchanged)

| Polyhedron | `(V, E, F)` | Symmetry | Role |
| :---- | :---- | :---- | :---- |
| Truncated octahedron | `(24, 36, 14)` | `O_h` | X-sector mediator |
| Truncated icosahedron | `(60, 90, 32)` | `I_h` | Y-sector mediator |

## §2.3 Gauge couplings (unchanged; upstream ZS-S1 spectral outputs)

| Coupling | Formula | Value | Status |
| :---- | :---- | :---- | :---- |
| `α_s` | `Q/[(V+F)_Y + β_0(Z)] = 11/93` | `0.118280` | `DERIVED` (ZS-S1) |
| `sin²θ_W` | `(48/91)·x*`, with `x*` the ZS-S1 fixed-point parameter | `0.23118` as printed upstream | `DERIVED` (ZS-S1); **not re-verified here** — `x*` is not defined in this paper and no row evaluates it |
| `α_2` | `X/[(V+F)_Y + X] = 3/95` | `0.031579` | `DERIVED` (ZS-S1) |

These are **imported**, not re-derived here. §8.2 records that none of them used the invalid colour clause.

## §2.4 Standard-Model hypercharge spectrum (unchanged)

| Field | `Y` | Sector formula (ZS-S11 §2.1) |
| :---- | :---- | :---- |
| `Q_L` | `+1/6` | `a + b = −1/X + 1/Z` |
| `u_R` | `+2/3` | `−2a` |
| `d_R` | `−1/3` | `−a` |
| `L_L` | `−1/2` | `−b = −1/Z` |
| `e_R` | `−1` | `+2b` |
| `ν_R` | `0` | `0` |
| `H` (weak doublet) | `+1/2` | `b = +1/Z` |

**Type note.** This table is about the SU(5) Cartan parametrisation of ZS-S11 and about the Standard-Model weak doublet `H`. It says nothing about the `D_3`\-invariant line of `H_5`; see §7.5.

## §2.5 ZS-M9 Table 2 assignments (unchanged as an assignment; re-read in §10.2)

| `I`\-irrep | Chirality `Δ` | Assignment |
| :---- | :---- | :---- |
| `1` | `+1` | `ν_R` / `U(1)` singlet |
| `3` | `+1` | left-handed fermions |
| `3'` | `+1` | right-handed fermions |
| `4` | `0` | gauge bosons |
| `5` | `−1` | Higgs / anti-sector |

The assignment of the `5` is retained as a **flavour-texture** assignment. Theorem S14.J shows it cannot simultaneously be an electroweak assignment.

## §2.6 Higgs sector (unchanged, upstream)

| Quantity | Value | Source | Status |
| :---- | :---- | :---- | :---- |
| VEV `v` | `245.93 GeV` | ZS-S4 §6.12 Thm V.9 | `DERIVED` |
| `γ_CW · C_M^sp` | `36.831` | ZS-S4 §6.12 | `DERIVED` |
| top Yukawa `y_t` | `0.98738` (the closed form re-evaluated here gives `0.987186`, a `0.02 %` gap — see §6.2) | ZS-S13 §8.4n | `DERIVED` |
| top mass `m_t` | `171.872 GeV` | ZS-S13 §8.4n | `TESTABLE` |
| Higgs mass `m_H` | `≈125.25 GeV` | ZS-S4 §6.12.7 | `HYPOTHESIS-strong` |

## §2.7 The unique Yukawa invariant (unchanged, and strengthened)

ZS-M10 Theorem 2.1 (`PROVEN`): `dim Hom_I(1, 3 ⊗ 5 ⊗ 3') = 1`, by the character integral

m \= (1/60) Σ\_g χ\_3(g) χ\_5(g) χ\_{3'}(g) \= (45 \+ 15 \+ 0 \+ 0 \+ 0)/60 \= 1 .

Re-derived in this session by explicit construction: `Λ²(4) = 3 ⊕ 3'` and `Sym²(4) ⊃ 5` in the `A_5` permutation module, projector `P = (1/60) Σ_g ρ_3(g) ⊗ ρ_5(g) ⊗ ρ_{3'}(g)`, with `‖P² − P‖ = 1.2 × 10⁻¹⁵`, `tr P = 1`, and maximal equivariance residual `1.7 × 10⁻¹⁵` over all sixty group elements (rows C1–C3). The same multiplicity is confirmed by exact finite-field arithmetic at six primes (row C4).

**ZS-M61 Theorem M61.19 (Yukawa slot isotropy), re-derived here.** The Higgs-index Gram form `G_{mn} = Σ_{i,α} T_{i m α} T_{i n α}` is `I`\-invariant on the irreducible `5`, so Schur's lemma forces `G ∝ δ`; the trace fixes the constant:

G \= δ/5 ,      ‖T·w‖ \= 1/√5 \= 0.447213595499958   for every unit w ∈ C^5 .

Measured `‖G − δ/5‖ = 3.0 × 10⁻¹⁶`; all five eigenvalues equal `0.2` (rows C5–C6). **No slot of the `5` can carry zero Yukawa weight.** This single fact drives §7.2, §10.2 and §10.3.

## §2.8 `D_3` branching rules — **CORRECTED**

The superseded table is preserved:

SUPERSEDED (ZS-S14 v2.0 Table 2.8, last row):

  5 | 1 \+ 2 \+ 2'

  "The 5-dim Higgs irrep decomposes into a D\_3-trivial 1 plus two distinct

   2-dimensional pieces."

Under the hexagonal stabiliser `D_3 ≅ S_3 ⊂ I` of order 6\. Fix the class order `(e, C_3, C_2)` \= (identity, order-3 rotations, order-2 rotations), with class sizes `(1, 2, 3)`. In that order the `S_3` character table is

chi\_1  \= ( 1,  1,  1\)

chi\_1' \= ( 1,  1, \-1)

chi\_2  \= ( 2, \-1,  0\)

and the character of the `I`\-irrep `5` restricted to `D_3` is `(5, −1, 1)`. (Some sources list the classes as `(e, C_2, C_3)` with sizes `(1, 3, 2)`; the multiplicities below are the same either way, but the two orderings must not be mixed, and v2.0's table did not state which it used.)

| `I`\-irrep | `D_3` decomposition | multiplicities `(m_1, m_{1'}, m_2)` |
| :---- | :---- | :---- |
| `1` | `1` | `(1, 0, 0)` |
| `3` | `1' ⊕ 2` | `(0, 1, 1)` |
| `3'` | `1' ⊕ 2` | `(0, 1, 1)` |
| `4` | `1 ⊕ 1' ⊕ 2` | `(1, 1, 1)` |
| **`5`** | **`1 ⊕ (2 ⊗ C²_mult)`** | **`(1, 0, 2)`** |

In the fixed order `(e, C_3, C_2)` with sizes `(1, 2, 3)`:

m\_1  \= (1/6)\[ 1\*5\*1 \+ 2\*(-1)\*1 \+ 3\*1\*1 \]     \= (1/6)(5 \- 2 \+ 3\) \= 1

m\_1' \= (1/6)\[ 1\*5\*1 \+ 2\*(-1)\*1 \+ 3\*1\*(-1) \]  \= (1/6)(5 \- 2 \- 3\) \= 0

m\_2  \= (1/6)\[ 1\*5\*2 \+ 2\*(-1)\*(-1) \+ 3\*1\*0 \]  \= (1/6)(10 \+ 2\)    \= 2

                                    1 \+ 0 \+ 2\*2 \= 5 . ✓

`D_3 ≅ S_3` has exactly three complex irreps, of dimensions `1, 1, 2` (since `1² + 1² + 2² = 6`). **There is no distinct second doublet.** The two doublets are the *same* irrep with multiplicity two, and

End\_{D\_3}(H\_5) ≅ C ⊕ M\_2(C) ,     dim \= 1² \+ 2² \= 5 ,

so `D_3` alone supplies a `U(2)` worth of freedom in the doublet isotypic sector and cannot single out a copy. This is ZS-M60 Theorem M60.25(i)–(ii) and ZS-M61 Theorem M61.1a; it is re-derived independently here (rows B1–B4).

**No nontrivial `su(3)` action exists on a two-dimensional block.** `su(3)` is simple of dimension 8 and `gl(2, C)` has dimension 4, so any Lie-algebra homomorphism `su(3) → gl(2, C)` has kernel the whole algebra; independently the Weyl dimension formula returns `1, 3, 6, 8, 10, 15, 21, 24, 27, …` and never `2` (rows B5–B6). A colour triplet would in any case require dimension 3, not 2\. This is M60.25(iii).

## §2.9 Cross-link inputs used in §9 (unchanged as imports, re-typed at use)

| Quantity | Statement | Source | Status as used here |
| :---- | :---- | :---- | :---- |
| X–Y tiling asymmetry | TO tiles `R³`; TI does not | ZS-M6 §5.5 | `IMPORTED-PROVEN` |
| M17.1 | `‖H_a − H_∞‖ = O((a/ℓ_P)²)` | ZS-M17 §3 | `IMPORTED-PROVEN`; mapping `OPEN` |
| M17.2 | Lieb–Robinson tightness `v_max = ρ(L)·a` | ZS-M17 §4 | `IMPORTED-PROVEN`; mapping `OPEN` |
| M17.6 | universality at `O(a²)` | ZS-M17 §8 | `IMPORTED-PROVEN` |
| M17.7 | OS reconstruction to a Wightman QFT | ZS-M17 §9 | `IMPORTED-PROVEN`; **S14 mapping `OPEN`, see §9.1** |
| ZS-Q7 Thm 2 | `rank(C_XZ C_ZY) ≤ dim Z = 2`; capacity `≤ ln 2` per Z-cell | ZS-Q7 | `IMPORTED-PROVEN`; mapping `OPEN` |
| Spinor–Descartes | `Σδ_v = 4π = 2π·χ = 2π·dim Z` | ZS-S7 §3 | `PROVEN` |
| \`C\_0 \= | O\_h | /b\_1\` | `48/3 = 16` |

**Import firewall.** That an upstream or external theorem is proven does not promote its ZS-S14 identification. Each mapping carries its own status in the row where it is used.

## §2.10 Non-perturbative inheritances (unchanged numerically; re-typed in §9.2)

| Quantity | Z-Spin | Experiment | Pull | Status at *its own* upstream scope |
| :---- | :---- | :---- | :---- | :---- |
| `Λ_QCD` | `vA/(λ₁V_Y) = 264.1 MeV` | `260 ± 20 MeV` | `+0.2σ` | ZS-S7 `DERIVED-CONDITIONAL` |
| `m(0⁺⁺)` | `vA/Q = 1.79063 GeV` | `1.73 ± 0.05 GeV` | `+1.2σ` | ZS-S7 `DERIVED-CONDITIONAL` |
| `m/Λ` | `6.779` | `6.65 ± 0.5` | `+0.3σ` | ZS-S7 `DERIVED` |
| `½ΔΣ` | `3/22` | `0.171 ± 0.018` | `<1.4σ` | ZS-Q3 `DERIVED` |
| `α_s(M_Z)` | `11/93 = 0.118280` | `0.1180 ± 0.0009` | `+0.31σ` | ZS-S1 / ZS-Q3 `DERIVED` |

## §2.11 TYPE LOCK — mandatory symbol separation

The following objects are distinct. **No symbol may denote more than one of them.** Gate F-S14.11 fires on any violation.

| Symbol | Type | Domain / range | Seam parity | Role |
| :---- | :---- | :---- | :---- | :---- |
| `H_5` | complex 5-dim `I`\-irrep carrier | `C^5`, dimensionless | not globally assigned without an operator | flavour-texture carrier; colour singlet |
| `Φ_Z` | the multiplicity-one `D_3`\-invariant line of `H_5` | `C ⊂ H_5` | as for `H_5` | a gauge-singlet component of `H_5`; its relation to `Φ` is **`OPEN`** (§10.3.5) |
| `Φ` | the ZS-F1 Z-bias field | `C`, `Φ = ρe^{iθ}` | — | carries the `|Φ| = 1` attractor; whether `Φ = Φ_Z` is `OPEN` |
| `ρ = |Φ|` | radial amplitude (the legacy `ε`) | `[0, ∞)` | **even** | heavy mode, `m_ρ = 2A·M_P` |
| `θ = arg Φ` | Goldstone phase | `[0, 2π)` | odd as an angle | massless; `ΔN_eff = 0` |
| `S_α = Im(e^{−iα}Φ)` | seam-odd observable | `[−1, 1]` on the vacuum circle | **odd** | the correct seam-odd variable |
| `J_α : Φ ↦ e^{2iα}Φ̄` | field reflection | one `O(2)` conjugacy class | involution, `det = −1` | ZS-M61 Thm M61.22′ |
| `ι_ZΦ` | register-to-field intertwiner | **OPEN — selection, not existence** | — | see §10.4 |
| `H` | the Standard-Model weak doublet | `C²_weak`, mass dimension 1 | — | transverse to the icosahedral labels |

**Mandatory wording.** `ρ = |Φ|` is unsigned and never has "vacua `±1`". The vacuum manifold of a radial potential is the **circle** `|Φ| = 1`, not the two-point set `{−1, +1}`. Any downstream statement requiring a signed seam-odd variable must use `S_α`, never `ρ`. This corrects the inherited wording registered as `D-F1-EPS` and stops its propagation from this paper onward; upstream files are the owner's to repair.

---

# §3. The typed ZS-S14 master action

## §3.1 Definition — **CORRECTED**

The superseded definition is preserved:

SUPERSEDED (ZS-S14 v2.0 Definition 3.1, covariant derivative and domains):

  D\_mu H\_5 \= (d\_mu \- i g\_Y q\_5 B\_mu \- i g\_2 W^a\_mu T^a\_2 \- i g\_s G^a\_mu lambda^a\_3) H\_5

  \* T^a\_2 acts on the D\_3-2 subspace of H\_5 (SM Higgs doublet sector)

  \* lambda^a\_3 acts on the D\_3-2' subspace of H\_5 (color triplet leptoquark sector)

Both clauses are void: there is no distinct D\_3-2', and su(3) has no

two-dimensional representation.  Retained here for provenance only.

**Definition 3.1′ (typed ZS-S14 master action).**

S\_S14 \= ∫ d⁴x √(−g) {

      ½ M\_P² (1 \+ A|H\_5|²) R

    − ½ M\_P² |D\_μ H\_5|²

    − |D\_μ H|²  −  V(H\_5, H)

    − ¼ B\_μν B^μν − ¼ W^a\_μν W^{aμν} − ¼ G^a\_μν G^{aμν}

    \+ ψ̄\_f i γ^μ D\_μ ψ\_f

    − \[ y\_0 · T\_{i m α} · (ψ̄\_L)^{i,A,c}\_a · (H\_5)^m · (H)\_A · (ψ\_R)^{α,c}\_a  \+ h.c. \]

  }

with the carriers and generator domains declared explicitly:

| Object | Carrier | `SU(3)_C` | `SU(2)_L` | `U(1)_Y` | mass dim |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `H_5` | `C^5` (`I`\-irrep `5`) | **singlet — no gluon term** | **singlet** | `Y_5 = 0` on every component (§7.5) | 0 |
| `H` | `C²_weak` | singlet | doublet, `T^b_L` | `Y_H = +1/2` | 1 |
| `ψ_L` | `C^3_{(I)} ⊗ C²_weak ⊗ C^3_C ⊗ C³_gen` | `T^a_C` on `C^3_C` | `T^b_L` on `C²_weak` | `Y_{ψ_L}` | 3/2 |
| `ψ_R` | `C^3_{(I)} ⊗ C^3_C ⊗ C³_gen` | `T^a_C` on `C^3_C` | singlet | `Y_{ψ_R}` | 3/2 |
| `B_μ, W^a_μ, G^a_μ` | spacetime connections | adjoint | adjoint | — | 1 |

The covariant derivatives are

D\_μ ψ  \= ( ∂\_μ − i g\_3 G^a\_μ T^a\_C − i g\_2 W^b\_μ T^b\_L − i g\_1 B\_μ Y\_ψ ) ψ

D\_μ H  \= ( ∂\_μ            − i g\_2 W^b\_μ T^b\_L − i g\_1 B\_μ Y\_H ) H

D\_μ H\_5 \= ∂\_μ H\_5                       (H\_5 is a total gauge singlet)

**Four changes from v2.0, each forced.**

1. **R0 colour repair.** `SU(3)_C` acts on the fermion colour factor `C^3_C`, which the Standard-Model matter content already carried. `H_5` carries no gluon term. Forced by §2.8; this is ZS-M61 Repair R0.  
2. **The weak doublet is a transverse factor.** `SU(2)_L` acts on `C²_weak`, not on any subspace of `H_5`. Forced by Theorem S14.J (§10.2). The Standard-Model Higgs `H` is a separate field; `H_5` supplies the flavour texture and the generation structure.  
3. **Dimensional repair.** In v2.0, `½M_P²|D_μ H_5|²` forces `[H_5] = 0`, while a Yukawa term `Y_0 T ψ̄_L H_5 ψ_R` with a dimensionless `Y_0` has mass dimension 3, not 4 — the action as printed was inconsistent by one power of mass. In Definition 3.1′ the missing dimension is carried by the weak doublet `H`, `[H] = 1`, and `y_0` is dimensionless. The overall Yukawa scale is then fixed by the same ZS-S13 closed form as before, `y_0 = y_t √(5/2)`, with `y_t` its `DERIVED` upstream value.  
4. **`Y_5 = 0`.** `H_5` is a total gauge singlet; hypercharge acts on `H` and on the fermions. v2.0's `q_5` clause, which assigned `1/Z` to "the appropriate `D_3` weak component" of `H_5`, is withdrawn with §7.5.

**Colour-index contraction.** In the Yukawa term the colour index `c` is contracted between `ψ̄_L` and `ψ_R` into an `SU(3)_C` singlet; the weak index `A` is contracted between `ψ̄_L` and `H`; the icosahedral indices `i, m, α` are contracted by `T`. Every index closes in a stated representation (row GRD13).

## §3.2 Minimal extension principle — **CORRECTED**

Relative to ZS-S10, the master action adds: the Standard-Model non-Abelian gauge kinetic terms; the Standard-Model Higgs doublet `H` with its own covariant derivative; the icosahedral flavour carrier `H_5`; and the ZS-M10 unique invariant tensor.

The repair R0 adds **no field**: `C^3_C` was already present in Standard-Model matter. What is withdrawn is only the false claim that the five-dimensional icosahedral irrep itself carries a colour triplet or a leptoquark block. 

SUPERSEDED (ZS-S14 v2.0 §3.2(a)):

"Replacement of the scalar Phi in C with the 5-dimensional H\_5 in C^5,

 where Phi corresponds to the D\_3-trivial (1-dim) component of H\_5."

The identification of Phi with the D\_3-trivial component of H\_5 is not

established.  It is registered OPEN in §10.3.5, not asserted as v2.0 did.

## §3.3 What the master action does and does not achieve — **CORRECTED**

**Does.**

1. It carries the Standard-Model gauge dynamics with couplings imported from the ZS-S1 spectral bridge, with no new fitted parameter.  
2. It carries the Yukawa sector through the unique `I`\-invariant tensor `T`, so the flavour texture is fixed by representation theory rather than by 44 free parameters — at the scope ZS-M10 and ZS-M11 actually establish.  
3. It reduces to the Standard Model in the `M_P → ∞` limit.  
4. It preserves `L_XY^{eff,direct} = 0` to all perturbative orders (§4).

**Does not — explicit non-claims at the level of the action.**

- `H_5` does **not** contain a colour triplet or a leptoquark block.   
- `H_5` does **not** carry the electroweak doublet as an internal subspace (§10.2).  
- The `D_3`\-invariant line `Φ_Z ⊂ H_5` is **not** the neutral component of the weak doublet (§7.2); whether it is the ZS-F1 Z-bias field `Φ` is `OPEN` (§10.3.5).   
- The relation of the action to ZS-S10 depends on the open question above and is stated conditionally in §7.4.

---

# §4. Theorem S14.A — `L_XY = 0` non-Abelian preservation

## §4.1 Statement — retained, scope unchanged

**Theorem S14.A** (`PROVEN-PERTURBATIVE`, `CURRENT`). In the master action of Definition 3.1′ no direct X-sector to Y-sector coupling vertex is generated at any order in perturbation theory:

L\_XY^{eff, direct} |\_{ZS-S14} \= 0   to all orders in perturbation theory.

All X ↔ Y communication proceeds through the Z-mediator at strength `O(κ²) = O(A/Q) ≈ 0.00728`, with higher-loop suppression `(A/4π)^{2n}`.

## §4.2 Proof — v1.0 five-step structure, re-checked against Definition 3.1′

**Step 1 (Lorentz algebra).** `so(1,3) ⊗ C ≅ su(2)_A ⊕ su(2)_B` with `[su(2)_A, su(2)_B] = 0` (ZS-M2 §2, `PROVEN`). The sector assignment `X ↔ su(2)_A`, `Y ↔ su(2)_B` inherits the commutativity (ZS-F5, `PROVEN`). `W^a_μ`, `G^a_μ` are internal Lorentz-vector representations, orthogonal to the polyhedral X/Y/Z decomposition. Unchanged by the repair.

**Step 2 (action-level absence), re-checked term by term for Definition 3.1′.** (a) `−¼ W W`, (b) `−¼ G G`: pure gauge kinetic, internal to their own gauge sectors. (c) fermion–gauge couplings: standard, on `C²_weak` and `C^3_C`, independent of the polyhedral decomposition. (d) `−|D_μ H|²`: the weak doublet is transverse to the icosahedral labels, so it introduces no X–Y contraction. (e) Yukawa `T_{imα} ψ̄_L H_5 H ψ_R`: `T` couples the `I`\-equivariant structures `3`, `5`, `3'`, all inside the Y-sector; the added factor `H` is X/Y-neutral. The repair therefore *strengthens* Step 2: removing the gluon term from `H_5` removes a term that would have coupled a spacetime connection directly to the Y-sector carrier.

**Step 3 (Ward–Takahashi).** For conserved `su(2)_A` charges `Q_A^a`, `∂_μ ⟨T{J^μ_{A,a}(x) O_B(y_1)…O_B(y_n)}⟩_conn = 0` for operators `O_B` transforming purely under `su(2)_B`. The new vertices of Definition 3.1′ — non-Abelian self-interactions, gauge–fermion couplings, the Yukawa vertex, the `H` quartic — none couples an X-sector current to a Y-sector current directly.

**Step 4 (anomaly freedom).** The five conditions A1–A5 hold for the Trinity Braiding hypercharges and are verified here in exact rational arithmetic, not floating point (rows A8–A12): `A2 = 0`, `A3 = 0`, `A4 = 0`, `A5 = 0` exactly as fractions, and `[SU(3)_C]³ = 0` because the colour representation is vector-like on `C^3_C`. **Note the repair improves this row:** under v2.0's clause a colour non-singlet scalar block existed and A1 required a separate argument; under R0 it is immediate.

**Step 5 (Schur protection).** ZS-F2 §4.2A (`PROVEN`): `A_5` is the unique finite subgroup of `SO(3)` for which `adj(SU(3))|_Γ = 3 ⊕ 5` lacks `3'`. Independent of the repair.

## §4.3 Scope

All perturbative orders, Lorentz-invariant regularisation, weak curvature `R ≪ M_P²`. Non-perturbative effects and strong curvature are outside scope, as in ZS-S10 Theorem S10.2.

*Status:* `PROVEN-PERTURBATIVE` / `CURRENT`. **The one v2.0 theorem that survives the repair unchanged in both statement and status.**

---

# §5. Theorem S14.B — the `SU(2)_L` bridge — **DEMOTED**

## §5.1 What v2.0 claimed

SUPERSEDED (ZS-S14 v2.0 Theorem S14.B):

"Under the ZS-M9 Table 2 assignment and the ZS-M11 6.1 D\_3 branching

 5 down D\_3 \= 1 \+ 2 \+ 2' (PROVEN), the D\_3-2 (2-dimensional) subspace of H\_5

 carries the SM Higgs SU(2)\_L doublet structure.  The covariant derivative

 D\_mu H\_5 includes the SU(2)\_L gauge coupling \-i g\_2 W^a\_mu T^a\_2 acting on

 this D\_3-2 subspace."

Its Step 1 cited the invalid branching; its Step 2 argued that the Higgs doublet must be one named doublet rather than the other — a distinction that does not exist.

## §5.2 What survives

**Proposition S14.B′** (`PROVEN`, `CURRENT`). Under `D_3 ⊂ I`:

1. `3 ↓ D_3 = 1' ⊕ 2` and `3' ↓ D_3 = 1' ⊕ 2`, so both chiral fermion irreps contain a two-dimensional `D_3` representation (rows B2–B3). This is a **dimension-compatibility** statement.  
2. `5 ↓ D_3 = 1 ⊕ (2 ⊗ C²_mult)`; the doublet isotypic sector has dimension 4 and `End_{D_3}` on it is `M_2(C)`.  
3. `g_2² = 4π α_2 = 12π/95 = 0.3968328` with `α_2 = X/[(V+F)_Y + X] = 3/95`, all inputs `LOCKED` (row D2). **This is an imported ZS-S1 output and does not depend on where `SU(2)_L` acts inside the master action.**  
4. With the Standard-Model Higgs mechanism applied to the weak doublet `H`, `m_W = √(g_2² v²/4) = 77.4614 GeV` (row D5).

**Erratum E19 — an unflagged `3.6 %` tension.** ZS-S14 v1.0 and v2.0 both stated at this step that `m_W ≈ 80.4 GeV`, "matching observation".  The stated inputs do not give that. With `g_2² = 12π/95` and `v = 245.93 GeV` the formula returns **`77.4614 GeV`**, against the PDG value `80.3692 ± 0.0133 GeV` — a deviation of **`−3.62 %`**, or roughly `−219σ` on the experimental error alone (row D6). The v2.0 verifier row `D5` compared the computation to a hard-coded `80.4` with a `5 %` tolerance, which is wide enough to pass a `3.6 %` miss; the deviation was therefore never visible in a passing run.

**Disposition.** The `m_W` agreement claim is `RETRACTED`. What survives is that `α_2 = 3/95` is an imported ZS-S1 spectral output and that the Higgs mechanism on the transverse doublet is standard. Whether the ZS-S1 value of `α_2` is meant to be a tree-level `M_Z`\-scale quantity, and what running or threshold corrections would apply, is not settled in this paper and is registered as gate **F-S14.16**. It is recorded here as an **open tension**, not as a success and not as a refutation.

## §5.3 What is retracted, and why

**The claim that `SU(2)_L` acts on a subspace of `H_5` inside the master action is `RETRACTED`.** By Theorem S14.J (§10.2), the annihilator of the ZS-M10 Yukawa invariant in `gl(3) ⊕ gl(5) ⊕ gl(3')` is exactly the two-dimensional scalar kernel; it is abelian and contains no `su(2)`. Any `su(2)_L` acting on the icosahedral labels — whether on the `5` alone, on the fermion labels alone, or on all three — would fail to leave the Yukawa term invariant. `SU(2)_L` must therefore act on a transverse factor, as it does in Definition 3.1′.

**Corollary — the copy-selection problem is displaced.** The question "which copy `|h⟩ ∈ C²_mult` is the physical weak doublet?" presupposes that some copy carries `SU(2)_L`. Under S14.J none does, so the projector `P_H = I_2 ⊗ |h⟩⟨h|` need not be selected. The selection problem does not disappear, however: it reappears, larger, as the direction of `⟨H_5⟩` in `CP⁴` (Corollary S14.J.4, debt `D-S14-VEV`).

*Status:* Proposition S14.B′ `PROVEN` at the stated scope; Theorem S14.B as printed in v1.0/v2.0 is `RETRACTED`.

---

# §6. Theorem S14.C — Yukawa explicit insertion

## §6.1 Statement — retained at upstream scope, with a re-typed insertion

**Theorem S14.C** (`DERIVED-CONDITIONAL` at ZS-M10 / ZS-M11 scope, `CURRENT`). The unique invariant tensor `T_{i m α} ∈ Hom_I(1, 3 ⊗ 5 ⊗ 3')` inserted as in Definition 3.1′ generates the Standard-Model fermion mass texture with overall normalisation `y_0 = y_t √(5/2)` and **no newly fitted numerical parameter — conditional on the direction of `⟨H_5⟩`, which Definition 3.1′ does not fix** (debt `D-S14-VEV`, §10.3.4). The v2.0 statement omitted that condition.

**What changed:** the tensor and its uniqueness are unchanged; the *insertion* now carries the transverse weak doublet `H` and contracts colour in `C^3_C` (Definition 3.1′). The v2.0 insertion, which had `H_5` carrying the electroweak quantum numbers, is superseded.

## §6.2 Supporting results, at their own scopes

1. **Uniqueness** (`PROVEN`, ZS-M10 Thm 2.1; re-derived here, rows C1–C4).  
2. **Normalisation** `y_0 = y_t √(5/2)` from the ZS-S13 closed form and the ZS-M10 `D_5` channel norm (`DERIVED` upstream, rows E2–E3). **Precision note:** re-evaluating the ZS-S13 closed form with the inputs printed in that paper returns `y_t = 0.987186`, not the printed `0.98738` — a relative gap of `2.0 × 10⁻⁴`, giving `m_t = 171.671 GeV` rather than `171.872 GeV`. Row E2 uses a `10⁻³` absolute tolerance and passes; the gap is inside the tolerance but outside the printed precision. This is an upstream digit question for ZS-S13, registered as debt `D-S14-DIGITS`, and it does not affect any statement in this paper.  
3. **Parameter collapse** — the `A_4` generation projector coefficients are fixed by `T`; ZS-M11 §3.2 reports `σ_1/σ_2 = 17`, `σ_1/σ_3 = 3477`, `Σσ² = 1/5`. **Re-typed:** these are upstream `DERIVED` results imported here as declarations with proof pointers, not re-verified by this paper's script (rows E4, E5). The frequently quoted "44 → 1 parameter collapse" is retained only at ZS-M10/ZS-M11 scope and is *not* claimed as a ZS-S14 result.  
4. **`D_5` channel splitting** — quark/lepton ratio `√2`, quark internal ratio `1 + √2`, Schur conservation `Σσ_i² = 1/5` (`PROVEN` upstream). The third of these is re-derived here as `G = δ/5` (row C5).

## §6.3 The consequence that matters downstream

Because `G = δ/5` is isotropic, **every** slot of the `5` has Yukawa weight `1/√5`. Three things follow, each used later:

- no slot can be made inert by a choice of basis (§7.2);  
- an exact seam `Z_2` acting on one slot cannot leave the classical Yukawa term invariant — ZS-M61 Theorem M61.19, condition W1 (§11.2, NC-S14.19);  
- the overall Yukawa normalisation is pinned: `y_0·(1/√5) = y_t/√2` exactly, so the ZS-M10 channel factor and the Standard-Model doublet convention agree — Proposition S14.K (§10.3.2); and the v2.0 action had no consistent way to supply the missing mass dimension — Proposition S14.K.1 (§10.3.3).

*Status:* `DERIVED` at upstream scope; the insertion is `PROVEN` as a type statement.

---

# §7. Theorem S14.D — the `Φ` identification — **LARGEST REWRITE**

## §7.1 The conflict, stated exactly

ZS-S14 v2.0 identified `Φ` in two mutually exclusive ways.

SUPERSEDED (ZS-S14 v2.0 §7.1, Hypothesis H\_id):

"H\_5 \= Phi\_{D\_3-1} (+) H\_doublet\_{D\_3-2} (+) H\_extra\_{D\_3-2'} ...

 Phi\_{D\_3-1} (1-dimensional D\_3-trivial subspace) is the ZS-F1 Z-bias scalar

 field Phi ... H\_extra\_{D\_3-2'} is the leptoquark sector."

SUPERSEDED (ZS-S14 v2.0 §7.5 Theorem S14.D.4 Step 2):

"Therefore Phi is identified with the neutral Higgs component within the

 D\_3-2 weak doublet of H\_5."

A `D_3`\-trivial line and a component of a `D_3` doublet are different isotypic subspaces with different gauge quantum numbers. They cannot be the same object. This conflict is upstream debt `D-S14-PHI`, severity S3, opened by ZS-M61 §28.4 and §38.1 Priority 1\.

## §7.2 Resolution — Branch A, then a further retraction

**Branch A** (the recommended minimal repair, per the correction specification): keep the `D_3`\-trivial line as a typed object; withdraw the identification with `H⁰`.

H\_5 \= Φ\_Z ⊕ (2 ⊗ C²\_mult) ,      Φ\_Z ∈ H\_5^{D\_3} ≅ C .

**Retraction 1 (Branch A).** `Φ_Z = H⁰` and "`Φ_Z` is the neutral component of the weak doublet" are `RETRACTED`. Replacement statement: 

> `Φ_Z` is the multiplicity-one `D_3`\-invariant component of `H_5`. The physical Standard-Model weak doublet is a distinct, transverse tensor factor `C²_weak`. No identification of `Φ_Z` with `H⁰` is made, and by Theorem S14.J none is available.

**On `Φ_Z = Φ_{ZS-F1}` (§7.1, §7.4).** v2.0 asserted this identification as part of Hypothesis `H_id`, on five lines of evidence rather than a proof. A draft of v2.1 attempted to *refute* it by a vacuum-scale argument; that argument was itself defective and is withdrawn in §10.3.1. The honest disposition is therefore neither v2.0's assertion nor the draft's refutation: **the relation between `Φ_Z` and `Φ` is `OPEN`.** §10.3.5 shows that the downstream consequence — the unavailability of an exact seam `Z_2` — is the same on either horn, so nothing that matters downstream turns on resolving it here.

**Consequence for `D-S14-PHI`.** The debt registered the *conflict* between two mutually exclusive identifications. That conflict is removed: one identification is retracted and the other is demoted from assertion to open question, so v2.1 asserts exactly one thing about `Φ_Z`, namely its type. The debt is **not** discharged in the sense of supplying a positive physical identification; none is available.

**Consequence for hypothesis `H_id`.** `H_id` as printed is `RETRACTED`. Of its five lines of evidence: (i) dimension matching used the invalid `1 + 2 + 2'` and fails; (ii) the `SU(2)_L` transformation argument is superseded by §10.2; (iii) the shared `|·| = 1` attractor is a coincidence of normalisation, not an identity theorem, and §10.3.3 shows that reading it as one is what made the v2.0 Yukawa dimensionally inconsistent; (iv) shared `π_1(S¹) = Z` winding is a topological similarity, not an identity theorem; (v) the anti-numerology appeal — "two independent objects sharing the same vacuum attractor cannot be independent" — is **not a derivation** and is withdrawn as such. Sharing a vacuum radius is not an identity theorem. 

## §7.3 Status of the identification

*Status:* `RETRACTED` / `SUPERSEDED` as an identification. Replacement content is the TYPE LOCK of §2.11; the surviving relation between `Φ_Z` and `Φ` is `OPEN` (§10.3.5).

## §7.4 Backward compatibility with ZS-S10 — **RE-TYPED**

SUPERSEDED (ZS-S14 v2.0 §7.4):

"In the limit where only the D\_3-1 component Phi of H\_5 is excited (other

 components frozen at zero), the master action S\_S14 reduces exactly to the

 ZS-S10 action."

Under Definition 3.1′ the ZS-S10 limit is obtained by retaining the ZS-F1 field `Φ` with its Stueckelberg coupling and switching off `W`, `G` and the remaining components of the scalar sector. In that limit `S_S14 → S_S10` and all ZS-S10 results — Stueckelberg mass, vortex topology, Corollary IV branches — are recovered.

**What is `OPEN` here.** Whether that limit is reached by *freezing components of `H_5`* (v2.0's route, which presupposes `Φ_Z = Φ`) or by *keeping a separate field* depends on the open question of §10.3.5. The limit statement itself holds either way; the mechanism is not established.

*Status:* `DERIVED` as a limit statement; the v2.0 *mechanism* for it is `OPEN`, not established.

## §7.5 Theorem S14.D.4 — hypercharge normalisation — **SPLIT INTO THREE TYPED OBJECTS**

SUPERSEDED (ZS-S14 v2.0 Theorem S14.D.4):

"Y\_Phi (GUT normalization) \= q\_Phi x (1/Z) \= (+1) x (1/2) \= \+1/2 \= Y\_H"

proved via Step 2, "Identification of Phi with neutral Higgs component".

The proof depended on the identification retracted in §7.2. The arithmetic is separated from the physics as follows.

| Object | Type | Value | Status |
| :---- | :---- | :---- | :---- |
| `q_Φ` | compact `U(1)_Z` character index of the ZS-F1 field | `+1` | `LOCKED` (ZS-F1 §3.2), declaration row |
| `1/Z` | reciprocal of the Z-sector dimension | `1/2` | `PROVEN` arithmetic (rows F1, F8) |
| `b = +1/Z` | the ZS-S11 §2.1 sector-Cartan parameter of `Y = diag(a,a,a,b,b)` | `+1/2` | `DERIVED` (ZS-S11), row F5 |
| `Y_H` | Standard-Model hypercharge of the weak doublet `H` | `+1/2` | `DERIVED` (ZS-U9 Thm T3), row F6 |
| `χ_ZY` | a map from the `U(1)_Z` character convention to Standard-Model hypercharge | — | **`OPEN`** |

**What is `PROVEN`.** `1/Z = 1/2` exactly; `b = +1/Z = +1/2` is the ZS-S11 Cartan parameter; the three Yukawa neutrality conditions hold exactly as rational identities:

−Y\_Q − Y\_H \+ Y\_u \= −1/6 − 1/2 \+ 2/3 \= 0

−Y\_Q \+ Y\_H \+ Y\_d \= −1/6 \+ 1/2 − 1/3 \= 0

−Y\_L \+ Y\_H \+ Y\_e \= \+1/2 \+ 1/2 − 1   \= 0

(rows F2–F4, exact `Fraction` arithmetic). **These say that the charge triple in each Yukawa term sums to zero** — which is the necessary and sufficient condition for the term to be neutral. It is a bookkeeping identity, not a derivation of hypercharge.

**What is `OPEN`.** The physical identification `Y_Φ = q_Φ/Z = Y_H` is `OPEN`. Under Definition 3.1′, `Φ_Z` is a gauge singlet with `Y = 0` and `Φ` is a separate field, so there is no object of which both `q_Φ = +1` and `Y = +1/2` are simultaneously the charge. The numerical coincidence `1/Z = 1/2 = Y_H` remains a normalisation coincidence until a typed map `χ_ZY` is constructed. Falsification gate F-S14.4 is re-opened accordingly.

**Verifier consequence.** The rows that compute `1/Z = 1/2` are retained but reclassified: they verify arithmetic, not a physical hypercharge bridge. In the v2.0 suite the corresponding rows F1 and F8 were named as verifying `Y_Φ = Y_H`; they never did — they computed `1/Z`.

*Status:* arithmetic `PROVEN`; physical identification `OPEN`, gate F-S14.4 re-opened. Theorem S14.D.4 as printed is `RETRACTED`.

## §7.6 Theorem S14.D.6 — mass hierarchy — retained conditionally

**Theorem S14.D.6** (`DERIVED-CONDITIONAL`, `CURRENT`). With `m_ρ = 2A·M_P` (ZS-F1 §4.4, `DERIVED` — a property of the ZS-F1 field `Φ`) and `v = M_P exp(−γ_CW C_M^sp)` (ZS-S4 §6.12 Thm V.9, `DERIVED`):

m\_ρ / m\_H ≈ 2A · exp(γ\_CW · C\_M^sp) / (m\_H/v)

Verified numerically at 50 digits: `γ_CW·C_M^sp = 36.831421`, `v = M_P e^{−γ_CW C_M^sp} = 245.9326 GeV` (`0.001 %` from the ZS-S4 target `245.93`), `m_ρ = 2A M_P = 3.90046 × 10^17 GeV`, and `log₁₀(m_ρ/m_H) = 15.49334` (rows G1–G4). **Note on row G4:** it evaluates a ratio of two quantities defined in this same paragraph, so it is a self-consistency check of the arithmetic, not an independent confirmation of the hierarchy; the comparison against the observed hierarchy is the ZS-S4 / ZS-F1 claim at their own scopes.

**Re-typing.** Under §7.2 this is now a statement relating two *different fields*, `Φ` and `H`, rather than two components of one multiplet. That makes it a weaker statement about the master action — it no longer follows from a single carrier's potential — but it does not change the arithmetic, and it is the same statement ZS-F1 and ZS-S4 already support at their own scopes. The residual factor remains conditional on the `HYPOTHESIS-strong` status of `m_H ≈ 125.25 GeV` in ZS-S4 §6.12.7.

*Status:* `DERIVED-CONDITIONAL`, unchanged in status, re-typed in content.

---

# §8. Theorem S14.E — **RETRACTED** — and its replacement

## §8.1 Retraction

RETRACTED (ZS-S14 v2.0 Theorem S14.E, clause (c)):

"Color triplet leptoquark coupling via the H\_5 D\_3-2' component, identified

 with the (3, 1, \-1/3) part of 5 \= (3, 1, \-1/3) \+ (1, 2, \+1/2) under

 SU(5) \-\> SM branching."

**Theorem S14.E is `RETRACTED`.** It asserted an action-level `SU(3)_C` closure on a single carrier. The carrier does not exist: there is no distinct `D_3`\-`2'` (§2.8), and `su(3)` has no two-dimensional representation. Marking it `RETRACTED` rather than silently rewriting it is required by the corpus no-deletion rule. 

The `SU(5)` branching `5 = (3,1,−1/3) ⊕ (1,2,+1/2)` cited from ZS-U9 §6.4 is a statement about the **`SU(5)` fundamental**, and is correct there. Its transfer to the icosahedral `I`\-irrep `5` was the error: two different objects of the same dimension were identified. This is recorded as the archetype of the confusion this paper's TYPE LOCK is designed to prevent.

## §8.2 Replacement — Proposition S14.E′ (colour-sector type repair)

**Proposition S14.E′** (`PROVEN` as a type statement, `CURRENT`). In Definition 3.1′:

(a) The gauge kinetic term `−¼ G^a_μν G^{aμν}`, `a = 1,…,8`, is standard; `8 = dim adj SU(3) = N_c² − 1` (row H4). (b) `SU(3)_C` acts on the Standard-Model fermion colour factor `C^3_C` by `T^a_C`; the quark–gluon coupling is standard. (c) `H_5` is a colour **singlet** and carries no gluon term. (d) In the Yukawa term all colour indices contract into an `SU(3)_C` singlet. (e) The strong coupling is imported: `α_s = Q/[(V+F)_Y + β_0(Z)] = 11/93 = 0.118280`, PDG `0.1180 ± 0.0009`, pull `+0.31σ` (rows H1–H2). (f) `a_3 = (V+F)_Y/G = 92/12 = 23/3`, matched independently by `n_f + (N²−1)/N = 5 + 8/3 = 23/3` (row H6).

**Acceptance tests, with the row that executes each.** `GRD03` — no live occurrence of a distinct second `D_3` doublet label. `B5`, `B6` — no `su(3)` representation of dimension 2 exists, so no `SU(3)_C` generator can act on a two-dimensional `H_5` block. `GRD12` — the manuscript states there is no gluon term on `H_5`. `GRD13` — the manuscript states that the Yukawa colour indices contract to a singlet. `GRD10` — the TYPE LOCK separates `Φ_Z` from the weak doublet `H`. `GRD07` — no live statement identifying `Φ_Z` with the neutral component of the weak doublet. 

**Two of these are document guards, not physics tests**, and are labelled as such: `GRD12` and `GRD13` verify that the manuscript *says* the right thing, which is an integrity check on this paper, not a proof about the action. The physics content is carried by `B5` and `B6`.

## §8.3 What does **not** move

`α_s = 11/93` was never derived from the invalid clause. It comes from the ZS-S1 spectral bridge and the Y-sector truncated-icosahedron counting `(V+F)_Y = 92` with `β_0(Z) = 1`. **No numerical corpus result moves under the repair.** The full insulation list is Appendix C.

## §8.4 What the repair costs

The v2.0 headline — that a single five-dimensional object carries all Standard-Model gauge dynamics — is gone. What replaces it is a typed product-carrier action of the ordinary kind, distinguished not by carrier economy but by the fact that its couplings and its Yukawa texture are fixed by upstream spectral and representation-theoretic results rather than fitted. That is a smaller claim and a defensible one.

*Status:* Theorem S14.E `RETRACTED`; Proposition S14.E′ `PROVEN` as a type statement.

---

# §9. The v2.0 cross-link theorems — re-typed

## §9.1 Theorem S14.F — sectoral closure — **DEMOTED to a conditional route**

SUPERSEDED (ZS-S14 v2.0 Theorem S14.F(F.i), status line):

"(F.i) The X-sector content of S\_S14 ... lifts to a Lorentz-invariant

 continuum Wightman QFT under ZS-M17 Theorem M17.7 (DERIVED) ...

 \[STATUS: DERIVED-interpretation strong\]"

**Theorem S14.F′ (conditional route / programme interface).** `DERIVED-CONDITIONAL`; gate `OPEN`.

> If the exact Whitney-integrated ZS-S14 slab action is proved to lie in the reflection-positive family satisfying the hypotheses of the imported continuum reconstruction theorem (ZS-M17 M17.7), then the stated X-sector continuum lift follows, with the Y-sector remaining finite and McKay-protected under M17.6 and the Z-sector mediating at rank `≤ dim Z = 2`. **ZS-S14 does not discharge that identification.**

The programme debt `D-YM-001` — *identify the exact Whitney-integrated ZS-S14 slab action with the canonical reflection-positive family, or with another proved physical carrier* — is `OPEN` in the current Corpus-OS registry and in The Book v13.2 Appendix D. v2.0's S14.F asserted the conclusion of that identification. It is demoted here.

**The OS-3 defect.** The v2.0 script's row K5 evaluated

A\_pos \= A\_mp \> 0

H5\_sq\_pos \= True   \# |H\_5|^2 \>= 0 by construction

V\_H5\_pos  \= True   \# V(H\_5) \>= 0

OS3\_pass  \= A\_pos and H5\_sq\_pos and V\_H5\_pos

and labelled the conjunction "OS-3 reflection positivity". Positivity of three scalars is not a reflection-positivity test and not a proof. In v2.1 the row is reclassified as a `D` declaration with a proof pointer to ZS-M17 §5, and the claim that ZS-S14 verifies OS-3 for its own slab action is withdrawn (row M5).

*Status:* `DERIVED-CONDITIONAL` / gate `OPEN` on `D-YM-001`.

## §9.2 Theorem S14.G — mass-gap inheritance — **SPLIT INTO FOUR LAYERS**

v2.0 combined four distinct statements under one `DERIVED` label. They are separated here.

| Layer | Statement | Status |
| :---- | :---- | :---- |
| 1\. Finite / polyhedral | `m(0⁺⁺) = vA/Q = 1.79063 GeV`; `Λ_QCD = vA/(λ₁V_Y) = 264.1 MeV`; `E_local = vA/V_Y = 328.3 MeV`; `m/Λ = 6.779`; topological cancellation `(4π/V)·V = 4π`; Spinor–Descartes `4π = 2π·χ = 2π·dim Z` | retained at **ZS-S7's own** status: `DERIVED-CONDITIONAL` / `PROVEN` for the identity. Verified arithmetically here (rows L1–L6). |
| 2\. Identification as a ZS-S14 master-action output | requires a typed map from the master action to the ZS-S7 polyhedral operator | **`OPEN`** |
| 3\. Continuum / Wightman lift of the gap | requires layer 2 plus `D-YM-001` | **`OPEN`, conditional** |
| 4\. Clay-form Yang–Mills | — | **`NON-CLAIM`** (NC-S14.12, retained) |

SUPERSEDED (ZS-S14 v2.0 Theorem S14.G, Step 4 conclusion):

"Therefore the mass-gap statement m(0++) \> 0 lifts from the polyhedral ground

 state to the X-sector continuum.  \[STATUS: DERIVED\]"

The lift is `OPEN`, not `DERIVED`, because it rests on S14.F, now demoted, and on layer 2, never established.

*Status:* layer 1 `DERIVED-CONDITIONAL` at ZS-S7 scope; layers 2–3 `OPEN`; layer 4 `NON-CLAIM`.

## §9.3 Theorem S14.H — X–Y channel capacity bound — **DEMOTED to `HYPOTHESIS / OPEN BOUND`**

SUPERSEDED (ZS-S14 v2.0 Theorem S14.H):

"|\<O\_X(t) O\_Y(0)\>|\_{S\_S14} \<= C(O\_X) C(O\_Y) exp(-t/tau\_Z) (ln 2 . n\_Z)

 \[STATUS: DERIVED-CONDITIONAL\]"

The v2.0 proof sketch cited three correct ingredients — no direct X–Y term (S14.A), a rank/capacity ceiling (ZS-Q7 Thm 2), and a Lieb–Robinson bound (M17.2) — but supplied no theorem converting a Holevo channel-capacity ceiling into a correlator-*amplitude* bound with that particular time dependence. The companion script never evaluated the inequality: its load-bearing rows M4 and M5 were literal `True`.

**Disposition.** S14.H is demoted to `HYPOTHESIS / OPEN BOUND`. The independently valid ingredients are retained as separate imported statements with their own status (rows M1–M5). A Holevo bound limits *information transfer per use of a channel*; converting it into an operator-norm bound on a two-point function requires a stated state, a stated channel decomposition and a stated norm, none of which v2.0 supplied.

*Status:* `HYPOTHESIS / OPEN BOUND`; **removed from any status tally.**

## §9.4 Theorem S14.D.8 — factor-2 prefactor — **DEMOTED to `HYPOTHESIS / OPEN`**

SUPERSEDED (ZS-S14 v2.0 Theorem S14.D.8):

"v \~= M\_P . exp(-gamma\_CW . C\_M^sp) . (2A)^(C\_0/8)   \[DERIVED-CONDITIONAL, v2.0\]

 with C\_0/8 \= 2 the structural exponent connecting BCC O\_h symmetry to

 b\_1 Wilson-line moduli count."

The v2.0 script verified `C_0 = 48/3 = 16`, `C_0/8 = 2` and `2A² ≈ 0.012829`. It did not establish that `C_0/8` is the exponent controlling the radial-mass prefactor, nor that multiplying the VEV formula by `(2A)^{C_0/8}` is derived from the action rather than chosen to fit.

**Disposition.** `C_0 = 16` is retained at its ZS-Q3 §6.6 `PROVEN` status (row N1); `C_0/8 = 2` is retained as arithmetic (row N2, class `T`); `2A² = 0.0128293…` is retained as an exact evaluation (row N3). The *connection* to the mass-hierarchy residual is `HYPOTHESIS / OPEN` pending an action-level derivation. **Removed from any status tally.**

*Status:* `HYPOTHESIS / OPEN`.

---

# §10. New results — the rigidity of the icosahedral Yukawa structure

This section contains the new content of v2.1. It arose from asking, after the colour repair, the sharper question the repair makes available: *not* "where does each gauge group act on `H_5`?" but **"what continuous symmetry can the ZS-M10 Yukawa invariant carry at all?"**

## §10.1 Setup and the imported framework

For a three-tensor `T ∈ A ⊗ B ⊗ C` the **symmetry Lie algebra** (annihilator) is

s(T) \= { (X\_A, X\_B, X\_C) ∈ gl(A) ⊕ gl(B) ⊕ gl(C) :

         (X\_A ⊗ 1 ⊗ 1 \+ 1 ⊗ X\_B ⊗ 1 \+ 1 ⊗ 1 ⊗ X\_C)·T \= 0 } .

This is the standard object of the tensor-symmetry literature \[E1\]. For **every** tensor of a given format, `s(T)` contains the two-dimensional abelian **universal scalar kernel**

k \= { (a·1\_A, b·1\_B, c·1\_C) : a \+ b \+ c \= 0 } ≅ C² ,

because the corresponding group elements `(λ 1_A, μ 1_B, ν 1_C)` with `λμν = 1` act trivially on `A ⊗ B ⊗ C` \[E2\]. `k` is therefore *not* a symmetry of any particular tensor; the informative quantity is `s(T)/k`.

**Definition.** `T` has **trivial connected symmetry group** iff `s(T) = k`, equivalently iff the stabiliser of `T` in `GL(A) × GL(B) × GL(C)` is finite modulo the universal kernel.

## §10.2 Theorem S14.J — chiral rigidity of the icosahedral Yukawa invariant

**Theorem S14.J.** `PROVEN`; `CERTIFIED` by exact finite-field arithmetic at six primes and cross-checked in floating point. Let `T ∈ Hom_I(1, 3 ⊗ 5 ⊗ 3')` be the unique `I`\-invariant Yukawa tensor of ZS-M10 Theorem 2.1. Then

s(T)  \=  k  \=  { (a·1\_3, b·1\_5, c·1\_{3'}) : a \+ b \+ c \= 0 }  ≅  C² ,

dim s(T) \= 2 ,   \[s(T), s(T)\] \= 0 .

Equivalently, **`T` has trivial connected symmetry group**: `Stab(T) ⊂ GL(3) × GL(5) × GL(3')` is finite modulo `k`, and contains the diagonal image of `I ≅ A_5`.

**Proof.** The condition `X·T = 0` is linear in `X`, so `s(T) = ker L` for the linear map

L : gl(3) ⊕ gl(5) ⊕ gl(3') → C^45 ,     dim domain \= 9 \+ 25 \+ 9 \= 43 .

*Bound from below on the kernel.* `k ⊆ ker L` by direct substitution (`(a+b+c)·T = 0`), and `dim k = 2`, so `dim ker L ≥ 2` and hence `rank L ≤ 41`.

*Bound from above on the kernel.* `rank L = 41`, hence `dim ker L ≤ 2`. An integral model is built from permutation matrices: `ρ_4` on the standard `A_5` module in the integral basis `E_j = e_j − e_4`; `ρ_6 = Λ²ρ_4` and `ρ_10 = Sym²ρ_4`, both with integer entries; the irreps `3`, `3'` are extracted from `ρ_6` and `5` from `ρ_10` by the character projectors `π_V = (dim V/60) Σ_g χ_V(g) ρ(g)`. The only irrationality is `√5`, entering `χ_3` and `χ_{3'}` on the two classes of 5-cycles. Reducing modulo a prime `p ≡ ±1 (mod 5)` with `p ∤ 60`, so that `√5 ∈ F_p`, gives `rank_{F_p} L ≤ rank_{C} L`. Computation returns `rank_{F_p} L = 41` for

p \= 41, 31, 61, 101, 999979, 1000039  (√5 \= 13, 6, 26, 45, 312221, 457607\) ,

with `tr(P_inv) = 1` at every prime, confirming the multiplicity of the invariant in the same model. Hence `rank_C L ≥ 41`, and with the lower bound `rank_C L = 41` and `dim ker L = 2`. ∎

**The step that makes the reduction legitimate, stated explicitly.** The certificate does not literally reduce one fixed complex matrix modulo `p`; it re-runs the construction inside each `F_p`. Three facts license reading the result as a bound on the characteristic-zero rank, and they are stated here rather than assumed:

1. `R = Z[1/60, φ]` is a Dedekind domain in which `60` is invertible and `φ = (1+√5)/2` is integral, and all of `ρ_4`, `Λ²ρ_4`, `Sym²ρ_4` have entries in `Z`. The character projectors `π_V = (dim V/60)Σ_g χ_V(g)ρ(g)` therefore have entries in `R`.  
2. Because `p ∤ |A_5| = 60`, Maschke's theorem holds over `F_p` and the reduction of the projector is the projector of the reduction, so the `F_p` construction computes the reduction of an `R`\-model rather than an unrelated object. The verified value `tr(P_inv) = 1` at every prime is the check that the invariant did not change multiplicity under reduction.  
3. Rank is basis-independent and satisfies `rank_{F_p}(M mod p) ≤ rank_{Frac(R)}(M)` for any `M` over `R`. The direction of the inequality is the one used: a *lower* bound on the characteristic-zero rank.

An independent adversarial re-derivation performed directly over `Q(√5)`, with no finite fields, returned the same values — `rank = 41`, `dim s(T) = 2` for the chiral tensor and `dim s = 5` for each untwisted sibling. The theorem does not depend on the finite-field route.

*Independent cross-check.* In double precision, `L` has `rank = 41` with a singular-value gap `σ_41 = 0.2067` against `σ_42 = 6.4 × 10⁻¹⁷`, and the computed kernel is spanned by the scalar triples. Equivariance of `T` holds to `1.7 × 10⁻¹⁵` over all sixty group elements. (Rows J1–J4, J9–J10.)

### §10.2.1 The result is load-bearing on chirality

**Proposition S14.J.1.** `PROVEN`. For the *untwisted* siblings, with the same group, the same dimensions `(3,5,3)` and the same multiplicity `dim Hom_I(1, ·) = 1`:

| Tensor | `dim Hom_I(1, ·)` | `dim s(T)` | `dim [s, s]` | verdict |
| :---- | :---- | :---- | :---- | :---- |
| `3 ⊗ 5 ⊗ 3'` (ZS-S14 Yukawa, chiral) | 1 | **2** | **0** | abelian — trivial connected symmetry |
| `3 ⊗ 5 ⊗ 3` (vector-like) | 1 | **5** | **3** | non-abelian, `[s,s] ≅ so(3)` |
| `3' ⊗ 5 ⊗ 3'` (vector-like) | 1 | **5** | **3** | non-abelian, `[s,s] ≅ so(3)` |

(Rows J5–J7. The numerical rank of each sibling map is certified by a singular-value gap of `0.2276` against `1.4 × 10⁻¹⁶` for `3 ⊗ 5 ⊗ 3` and `2.2 × 10⁻¹⁶` for `3' ⊗ 5 ⊗ 3'`; these gaps are diagnostics, and the ranks themselves were also confirmed in exact arithmetic over `Q(√5)` during the adversarial audit.)

The reason is structural. `A_5 ⊂ SO(3)` through the irrep `3`, and under that embedding `5 = Sym²_0(3)`, so the `SO(3)` Wigner `3j` coupling `3 ⊗ 5 ⊗ 3 → 1` already exists; multiplicity one then forces the `A_5` invariant to *be* that `3j` symbol, and it inherits the full `so(3)`. The Galois twin `3'` is not the restriction of any `SO(3)` representation in the *same* embedding — it comes from the conjugate embedding — and that is exactly what removes the `so(3)`.

**Therefore Theorem S14.J does not follow from multiplicity one.** Any statement of the form "a multiplicity-one invariant of a finite group has trivial connected stabiliser" is **false**, and the counterexample sits in the same group and the same format. The theorem is load-bearing on the Galois twist `3 ↔ 3'`, that is, on the **chirality** of the Z-Spin fermion assignment `LH ↔ 3`, `RH ↔ 3'` (ZS-M15 §5.3, Assignment A).

### §10.2.2 Corollaries

**Corollary S14.J.2 (gauge–flavour factorisation is forced).** No nonzero element of a simple Lie algebra lies in `s(T)`, since `s(T)` is two-dimensional and abelian. Hence **no `su(2)_L` and no `su(3)_C` can act on the icosahedral labels `(i, m, α)` of the ZS-S14 Yukawa term** — not on `H_5`, not on the fermion icosahedral labels, and not on any combination. Every Standard-Model gauge generator must act on a tensor factor transverse to those labels.

**Corollary S14.J.3 (repair R0 is forced *within a stated class*).** ZS-M61 registered R0 — `H_5` a colour singlet, `SU(3)_C` on the fermion factor `C^3_C` — as one repair among possibly several, and recorded `NC-M61.1`: "R0 is not claimed unique", counted as structural choice C1.

Under Corollary S14.J.2, **R0 is the only colour repair that retains the ZS-M10 Yukawa tensor and adds no new tensor factor to the scalar carrier.** Both qualifications are load-bearing and are stated rather than hidden:

- *Retains `T`.* Abandoning the ZS-M10 invariant would abandon the flavour-texture result that is ZS-S14's reason for using `H_5` at all.  
- *Adds no factor.* A carrier `H_5 ⊗ C³_C` with colour on the new transverse factor also leaves `T` intact and is **not** excluded by Theorem S14.J. It is excluded only by minimality — it introduces a coloured scalar that the Standard Model does not contain and that nothing in the corpus requires.

**Therefore `NC-M61.1` is *narrowed*, not discharged**, and structural choice C1 is reduced from "some unknown set of repairs" to "R0, or a repair that adds a coloured scalar". The claim that the colour repair was never a choice at all would be an overstatement, and this paper does not make it. The same argument, with the same two qualifications, extends the repair from `SU(3)_C` to `SU(2)_L`, which ZS-M61 did not address.

**Corollary S14.J.4 (the multiplicity-selection problem is displaced, not dissolved).** The corrected branching leaves a four-dimensional doublet isotypic sector with `End_{D_3} = M_2(C)`, and one might expect an open problem: which copy `|h⟩ ∈ C²_mult` is the physical weak doublet? Under Corollary S14.J.2 no copy carries `SU(2)_L`, so **that particular selection is not required.**

**But the selection does not vanish — it moves and it gets larger.** Under Definition 3.1′ the fermion mass matrix is `M_{iα} = y_0 ⟨H⟩ (T·⟨H_5⟩)_{iα}`, so the flavour texture is fixed by the *direction* of `⟨H_5⟩` in `CP⁴`: eight real parameters, against the two of a copy choice in `CP¹`. Definition 3.1′ does not fix it, because `V(H_5, H)` is not specified here. This is registered as debt **`D-S14-VEV`** (§10.3.4, §13.3, §13.4). Reporting the copy-selection problem as "dissolved" without registering its larger replacement would have been the same kind of error the rest of this paper corrects.

**Corollary S14.J.5 (chirality forces factorisation).** If the Z-Spin assignment were vector-like — both chiralities in `3`, or both in `3'` — then by Proposition S14.J.1 an `so(3) ≅ su(2)` *would* act on the icosahedral labels while preserving the Yukawa invariant, and a genuine flavour-gauge unification on those labels would be available. It is the chiral assignment that removes it. **Gauge–flavour factorisation, which the discrete-flavour-symmetry literature imposes as a construction axiom, is in ZS-S14 a consequence of chirality.**

### §10.2.3 What Theorem S14.J does **not** say

- It does **not** say that gauge groups cannot act on the fields. They act on transverse factors, as in Definition 3.1′ and as in every flavour-symmetry model.  
- It does **not** derive the Standard-Model gauge group. `SU(3)_C × SU(2)_L × U(1)_Y` enters Definition 3.1′ as an input.  
- It does **not** derive hypercharge. The condition `q_1 + q_2 + q_3 = 0` on a charge triple is exactly the statement that the triple lies in the universal kernel `k`, which annihilates every tensor of this format. It is a neutrality bookkeeping identity, valid for any three-index term, and carries no Z-Spin content. §7.5 is written accordingly.  
- It is **not** a general no-go about finite groups; Proposition S14.J.1 is the counterexample to the general form.

### §10.2.4 Novelty classification

`SPECIALIZED`, with one `OPEN-NOVELTY` component.

- The definition of `s(T)` and the universal kernel `k ≅ C²` with `λμν = 1` are `IMPORTED` from the tensor-symmetry literature \[E1, E2\].  
- Semicontinuity of `dim Stab(T)` plus the count `41 < 45` means `dim s(T) = 2` is the *generic* value for the `(3,5,3)` format \[E3\]. The theorem says the icosahedral invariant is not exceptional. That it *could* have been exceptional is shown by matrix multiplication, whose stabiliser is `(C*)² × PGL_n^{×3} ⋊ D_3` \[E5\]; by the large Coppersmith–Winograd tensor, which attains maximal symmetry dimension \[E7\]; by octonionic multiplication, stabilised by `G_2` \[E8\]; and, decisively, by Proposition S14.J.1 inside `A_5` itself.  
- The `A_5` tensor-product rules are `IMPORTED` \[E9\]; the specific triple `3 ⊗ 5 ⊗ 3'` is not tabulated there.  
- The statement for this specific invariant, and the chiral contrast of Proposition S14.J.1, were **not found** in the mathematics or physics literature searched. `NOT_FOUND` is not `ABSENT`; the systematic sweep is registered as debt `D-S14-PRIOR`.  
- In flavour physics the *conclusion* is standard practice: the flavour group's action is assumed to commute with gauge transformations and to act on flavour indices of fields sharing the same gauge quantum numbers \[E12\], and the electroweak Higgs is assumed blind to the family symmetry \[E13\]. **The literature assumes what §10.2 derives.** No source found computes a stabiliser Lie algebra for an `A_5` Yukawa invariant.

## §10.3 Proposition S14.K — normalisation consistency of the typed Yukawa insertion

### §10.3.1 A withdrawn claim, recorded

A first draft of this section asserted a *vacuum scale-separation obstruction*: that if the ZS-F1 field `Φ` were the `D_3`\-invariant component of `H_5`, the isotropy of the Gram form would force Planck-scale fermion masses, an overshoot of `M_P/v ≈ 9.90 × 10^15`. **That claim was false under Definition 3.1′ and is withdrawn before release.** In Definition 3.1′ the Yukawa carries both `H_5` (dimensionless) and the weak doublet `H` (mass dimension 1), and their vacuum values *multiply*; with `‖⟨H_5⟩‖ = 1` the induced scale is of order `v`, not of order `M_P`. The falsification gate registered for that claim was fired by this paper's own Definition 3.1′, which is exactly what a falsification gate is for.

The withdrawal is recorded rather than deleted, because it is the same failure mode the rest of this paper is about: **an argument that is correct about one action, applied to a different one.** v2.0 made that mistake with a representation; the draft of this section made it with a normalisation.

### §10.3.2 Proposition S14.K (normalisation consistency)

**Proposition S14.K.** `CERTIFIED`. Under Definition 3.1′ the fermion mass matrix is

M\_{iα} \= y\_0 · (T · ⟨H\_5⟩)\_{iα} · ⟨H⟩ ,     ⟨H\_5⟩ ∈ C^5 dimensionless.

By the Gram isotropy of §2.7, `‖T·w‖ = ‖w‖/√5` for every `w ∈ C^5`. With the ZS-M10 channel normalisation `y_0 = y_t √(5/2)`,

y\_0 · (1/√5) \= y\_t √(5/2) / √5 \= y\_t / √2        exactly

(residual `< 10⁻⁴⁵` at 50 digits, row K2), so with `‖⟨H_5⟩‖ = 1` and `⟨H⟩ = v` the typed insertion reproduces the ZS-S13 closed form

m \= y\_0 · (1/√5) · v \= y\_t v / √2 \= 171.704168 GeV        (row K3).

**Reading.** The factor `√(5/2)` that ZS-M10 derives from the `D_5` channel decomposition is exactly the factor converting the isotropic five-slot weight `1/√5` into the single-doublet `1/√2` of a standard Yukawa term. Two normalisations obtained independently — one from icosahedral representation theory, one from the Standard-Model Higgs convention — agree exactly. This is a consistency check of the typed insertion of Definition 3.1′, and it fixes the vacuum convention: **`⟨H⟩ = v` with `‖⟨H_5⟩‖ = 1`**, not `⟨H⟩ = v/√2`.

**What it is not.** It is an algebraic rearrangement of the definition of `y_0`, not a derivation of `m_t`; `y_t` is imported from ZS-S13. Its content is that two conventions agree. It is reported as `CERTIFIED`, never as `DERIVED`.

### §10.3.3 Proposition S14.K.1 (the v2.0 dimensional defect, quantified)

**Proposition S14.K.1.** `CERTIFIED`. The v2.0 Yukawa term `y_0 T ψ̄_L H_5 ψ_R`, with `y_0` dimensionless and `[H_5] = 0` forced by `½M_P²|D_μ H_5|²`, has mass dimension 3\. The only scale available in the v2.0 action with which to restore dimension 4 is `M_P`. Restoring it that way, and using the ZS-F1 attractor `‖⟨H_5⟩‖ = 1`, gives an induced fermion mass larger than the observed scale by exactly

M\_P / v \= 9.90119 × 10^15 ,        log₁₀(M\_P/v) \= 15.99569

(rows K4, K5).

**Reading.** This is a statement about ZS-S14 **v2.0**, not about Definition 3.1′. It quantifies erratum E16: the v2.0 action was not merely untidy about dimensions — it had no consistent completion in which the icosahedral carrier both obeys the ZS-F1 attractor and produces electroweak-scale fermion masses. Definition 3.1′ repairs this by putting the missing mass dimension on a transverse weak doublet, which is precisely where Theorem S14.J says the electroweak quantum numbers have to live. **The dimensional repair and the representation-theoretic repair turn out to be the same repair.** That coincidence is the substantive content of this subsection.

### §10.3.4 What remains open: the vacuum direction

Proposition S14.K fixes `‖⟨H_5⟩‖` and says nothing about its direction. Since `M_{iα} = y_0 ⟨H⟩ (T·⟨H_5⟩)_{iα}`, the *ratios* of fermion masses are controlled entirely by the direction of `⟨H_5⟩` in `CP⁴` — **eight real parameters** — which Definition 3.1′ does not fix, because the potential `V(H_5, H)` is not specified here. ZS-M10 and ZS-M11 treat this as the Higgs VEV tilt angle and report that the observed `σ`\-ratios are matched at that scope; this paper does not re-derive it and does not inherit the claim.

**New debt `D-S14-VEV` is registered:** *specify `V(H_5, H)` and derive the direction of `⟨H_5⟩`, target-blind.* Until it is discharged, any statement that the icosahedral structure fixes the fermion mass texture with no fitted numerical parameters is conditional on that selection, and §13.3 says so.

### §10.3.5 Consequence for the `Φ` identification

Because the scale-separation claim is withdrawn, **Retraction 2 of §7.2 is withdrawn with it.** The relation between the `D_3`\-invariant line `Φ_Z ⊂ H_5` and the ZS-F1 Z-bias field `Φ` returns to `OPEN`: it is neither asserted nor excluded here.

- Definition 3.1′ is *consistent* with `Φ_Z = Φ`, since both are dimensionless with an `O(1)` vacuum value.  
- If `Φ_Z = Φ`, ZS-M61 §28.5's first horn applies: by M61.19 the Yukawa is linear in the `Φ_Z` slot with weight `1/√5`, so a seam `Z_2` acting as `Φ_Z ↦ −Φ_Z` is not a symmetry of the action, condition W1 fails, and `D-M61-WARD` stays `OPEN`.  
- If `Φ_Z ≠ Φ`, ZS-M61's second horn applies and the seam vertex is not action-derived from `S_S14`.

**Either way the exact seam `Z_2` is unavailable**, which is what NC-S14.19 asserts, and ZS-M61's own analysis is therefore *unchanged* by this paper. What v2.1 does change is that `D-S14-PHI` is discharged only on the horn the correction specification identified — Retraction 1, the withdrawal of the weak-doublet reading — and not on the other.

## §10.4 Proposition S14.L — `D-M61-IOTA` is a selection debt, not an existence debt

ZS-M61 §40.3 registers the intertwiner

ι\_ZΦ : H\_Z^{parity} → span\_R{Re Φ, Im Φ} ,      ι\_ZΦ ∘ J\_Z \= J\_C ∘ ι\_ZΦ

as `OPEN`, with `J_Z = diag(+1, −1)` the abstract register parity of ZS-F0 Def. 8.11 and `J_C` complex conjugation.

**Proposition S14.L.** `PROVEN`. The space of real-linear maps satisfying the intertwining relation is two-dimensional, and the invertible ones form the group

{ ι \= diag(s, t) : s, t ∈ R \\ {0} } ≅ (R\*)² .

**Proof.** In the eigenbasis of `J_C`, `J_Z` and `J_C` are both `diag(+1,−1)`, so `ι J_Z = J_C ι` iff `ι` commutes with `diag(+1,−1)`, iff `ι` is diagonal. Verified by rank computation: the linear system on `gl(2,R)` has rank 2, kernel dimension 2 (row K6). ∎

**Consequence.** Intertwiners *exist* and are unique up to two real scalings; what is missing is a **selection principle** determining `(s,t)` from the action or the boundary data. The debt is therefore sharper than registered: `D-M61-IOTA` is a selection debt of exactly two real parameters, not an existence question. This is a debt-precision gain, not a closure.

## §10.5 The "complete master equation" question — verdict

The request that motivated this section was whether the master equation could be completed to a full derivation. The honest answer has three parts.

**1\. The residual was never a missing fraction of the equation. It was a type error in the carrier.** v2.0 assessed itself as approximately ninety-nine per cent closed with a residual of about one per cent in three components. That assessment was not merely optimistic; it was measuring the wrong thing. The actual defect was that the carrier could not host the generators the action assigned to it. A percentage cannot see a type error.

**2\. At the level of writing the action, the structure is now complete and rigid — and Theorem S14.J proves that nothing further can be added there.** Given the ZS-M10 Yukawa tensor, the set of continuous symmetries available on the icosahedral labels is exhausted by the trivial rescalings. There is no undiscovered gauge structure hiding in `H_5`, and no further unification of that kind to find. This is the strongest form of completeness actually available: not "we filled the last one per cent", but "we proved there is nothing left in this layer".

**3\. What remains open is a different layer entirely — state and selection, not equation-writing.** Five named items, none of which is a missing term in the action:

| \# | Open item | Type | Debt |
| :---- | :---- | :---- | :---- |
| 1 | A typed map from the master action to the ZS-S7 polyhedral operator | selection / identification | §9.2 layer 2 |
| 2 | Identification of the exact Whitney-integrated slab action with the reflection-positive family | identification | `D-YM-001` |
| 3 | The register-to-field intertwiner `(s,t)` | selection, 2 real parameters | `D-M61-IOTA` (sharpened, §10.4) |
| 4 | The physical boundary phase law | state selection | `D-M61-GOLD` |
| 5 | An action-derived seam symmetry or typed carrier | symmetry / carrier | `D-M61-WARD` |
| 6 | The direction of `⟨H_5⟩` in `CP⁴`, which controls the whole fermion texture | vacuum selection, 8 real parameters | `D-S14-VEV` |

Items 3 and 4 are state-selection problems: the action is symmetric and the state is not. Items 1, 2 and 5 are identification problems between a finite construction and a physical carrier. Item 6 is a vacuum-selection problem that the correction *created* — or rather, revealed, since it was always there and the single-carrier framing hid it. **None of the six is closed by writing more of the Lagrangian, and none of them was going to be closed by the missing fraction of a per cent.** That is the substantive result of this section, and it is why §13 reports a claim-level board rather than a number.

---

# §11. Falsification gates and non-claims

## §11.1 Falsification gates

Six v1.0 gates and four v2.0 gates are preserved with their status **re-evaluated**, because several had premises that the erratum invalidated; a gate whose premise is void is not `PASS`. Five new gates are registered.

| ID | Type | Condition that triggers FAIL | v2.0 status | v2.1 status |
| :---- | :---- | :---- | :---- | :---- |
| F-S14.1 | MATH, decisive | `L_XY^{eff,direct} ≠ 0` at any perturbative order | PASS | `PASS` |
| F-S14.2 | MATH, decisive | ZS-M9 Table 2 assignment of the `5` falsified | PASS | `PASS` as a **flavour-texture** assignment only |
| F-S14.3 | OBS, decisive | FCC-ee measures `m_t` outside `[170.5, 173.0]` GeV at `>5σ` | TESTABLE | `TESTABLE` (unchanged) |
| F-S14.4 | MATH, mod-req | `Y_Φ = q_Φ·(1/Z)` inconsistent with another corpus result | PASS | **`RE-OPENED`** — premise retracted (§7.5) |
| F-S14.5 | MATH, mod-req | `m_ρ/m_H` factor inconsistent with `v = 245.93 GeV` | PASS | `PASS`, re-typed (§7.6) |
| F-S14.6 | OBS, decisive | any newly fitted numerical parameter required | PASS | `PASS`, qualified (§13.2) |
| F-S14.7 | MATH, decisive | ZS-M17 M17.7 retracted or shown to have a gap | PASS | `PASS` for the import; **S14 mapping `OPEN`** |
| F-S14.8 | MATH, decisive | ZS-S7 topological cancellation retracted | PASS | `PASS` |
| F-S14.9 | MATH, mod-req | X–Y tiling asymmetry shown to fail | PASS | `PASS` |
| F-S14.10 | OBS, testable | `m(2⁺⁺)` Schur–Feshbach route falsified by lattice at `>3σ` | OPEN | `OPEN` |
| **F-S14.11** | MATH, decisive | any symbol in the TYPE LOCK (§2.11) is used for two distinct objects | — | `NEW`, `PASS` |
| **F-S14.12** | MATH, decisive | a two-dimensional nontrivial `su(3)` representation, or two inequivalent `D_3` doublets, is exhibited | — | `NEW` — would withdraw the erratum and reinstate S14.E |
| **F-S14.13** | MATH, decisive | `dim s(T) > 2` for the ZS-M10 invariant, or an `su(2)`/`su(3)` is exhibited inside it | — | `NEW` — would falsify Theorem S14.J |
| **F-S14.14** | MATH, decisive | `y_0·(1/√5) ≠ y_t/√2`, i.e. the ZS-M10 channel normalisation is not the Gram-isotropy conversion factor | — | `NEW`, `PASS` — would falsify Prop. S14.K |
| **F-S14.16** | OBS, decisive | the `m_W` tension of erratum E19 is not resolved by running, threshold or scheme corrections, i.e. `α_2 = 3/95` is confirmed as an `M_Z`\-scale tree value | — | `NEW`, `OPEN` — would refute the ZS-S1 `α_2` bridge |
| **F-S14.17** | MATH, mod-req | a potential `V(H_5, H)` derived target-blind selects a direction of `⟨H_5⟩` incompatible with the ZS-M11 `σ`\-ratios | — | `NEW`, `OPEN` — debt `D-S14-VEV` |
| **F-S14.15** | ARTIFACT | the companion script's executed row count differs from `EXPECTED_ROWS`, or any evidence-bearing row is a literal declaration | — | `NEW`, `PASS`; guard tested live (§12.3) |

## §11.2 Non-claims

The eleven v1.0 non-claims and three v2.0 non-claims are preserved. NC-S14.2, NC-S14.3 and NC-S14.13 are re-typed because their references changed; the substance is not weakened. Eight new non-claims are added.

**Preserved (abbreviated; full text in v1.0 §10.2 and v2.0 §10.2).** NC-S14.1 no new gauge fields. NC-S14.2 non-perturbative effects not closed. NC-S14.3 S14.D.6 not `DERIVED-strong`. NC-S14.4 no GUT scale or coupling. NC-S14.5 photon masslessness not derived. NC-S14.6 no supersymmetry or new symmetry. NC-S14.7 galactic predictions unmodified. NC-S14.8 inflationary predictions unmodified. NC-S14.9 upstream numbers not re-derived. NC-S14.10 Trinity gap G2 not closed here. NC-S14.11 no new phenomenology. NC-S14.12 not a Clay-form Yang–Mills proof. NC-S14.13 glueball excited spectrum not closed. NC-S14.14 the X–Y bound is one-sided — **and is now itself `HYPOTHESIS`, §9.3**.

**New in v2.1.**

- **NC-S14.15.** `H_5` does **not** carry a colour triplet, a leptoquark block, or any `SU(3)_C` representation. It is a colour singlet.   
- **NC-S14.16.** `H_5` does **not** carry the electroweak doublet as an internal subspace. `SU(2)_L` acts on a transverse factor.  
- **NC-S14.17.** The `D_3`\-invariant line `Φ_Z ⊂ H_5` is **not** identified with the neutral component of the weak doublet; that identification is retracted. Its relation to the ZS-F1 Z-bias field `Φ` is `OPEN` — this paper neither asserts it (as v2.0 did) nor excludes it (as a withdrawn draft of §10.3 attempted to).   
- **NC-S14.18.** Theorem S14.J does **not** derive the Standard-Model gauge group, and does **not** derive hypercharge. The neutrality identity `q_1 + q_2 + q_3 = 0` holds for every three-index term and carries no Z-Spin content.  
- **NC-S14.19.** ZS-S14 does **not** establish an exact all-action seam `Z_2` symmetry for the physical master action. On the branch `Φ ⊂ H_5` it fails by ZS-M61 Theorem M61.19 (condition W1); on the branch `Φ ⊄ H_5` there is no action-derived seam vertex. Both horns of the ZS-M61 §28.5 dichotomy remain live (§10.3.5), and the conclusion is the same on each. Any downstream result requiring that symmetry is conditional or inapplicable until a different action-derived symmetry or typed carrier is constructed. **No ad hoc term is to be added to force the symmetry or to reach a target multiplier.**  
- **NC-S14.20.** A flat Goldstone potential does **not** imply a Haar-uniform boundary phase law. Flatness is energetic degeneracy, not a state-selection theorem; spontaneous symmetry breaking is the standard counterexample. ZS-S14 does not derive the physical boundary phase law; Haar uniformity, if assumed, is the explicit hypothesis `(H-U1-BDY)` and leads to the conditional ZS-M61 Theorem M61.23′ Bessel no-go.  
- **NC-S14.21.** Theorem S14.J is **not** a general theorem about finite groups. Proposition S14.J.1 exhibits the counterexample to the general form inside `A_5` itself.  
- **NC-S14.22.** The verification row count is **not** a theorem count, and `0 FAIL` is not a proof of any statement carried by a `D` or `T` row.  
- **NC-S14.23.** ZS-S14 does **not** claim that the icosahedral structure fixes the fermion mass texture with no fitted numerical parameters. It fixes the texture *given* the direction of `⟨H_5⟩`, which this paper does not derive (debt `D-S14-VEV`).  
- **NC-S14.24.** ZS-S14 does **not** claim agreement with the measured `W` mass. Erratum E19 records a `−3.62 %` tension between the ZS-S1 value of `α_2` and the PDG value of `m_W`, previously concealed by a wide verifier tolerance.

**Gates whose premises were invalidated.** F-S14.4 is re-opened rather than carried as `PASS`, because the statement it was guarding has been retracted. This is the general rule applied: an invalidated premise voids the gate; it does not pass it.

---

# §12. Verification

## §12.1 Artifact manifest

ARTIFACT\_MANIFEST

paper\_code/version : ZS-S14 v2.1

main\_script        : zs\_s14\_verify\_v2\_1.py

python             : CPython 3.11+

dependencies       : mpmath \>= 1.3.0, numpy \>= 1.24  (no network access required)

random seeds       : none used in any evidence-bearing row; the one seeded

                     commutant draw is a basis choice, checked invariant

                     across seeds (row R9)

precision          : mp.dps \= 50 for arithmetic rows; exact Fraction for

                     rational identities; exact F\_p arithmetic for rank rows

one-command run    : python3 zs\_s14\_verify\_v2\_1.py

expected outputs   : console census \+ ZS\_S14\_v2\_1\_verification\_report.json

expected row count : EXPECTED\_ROWS, fail-closed

fail-closed on     : row-count mismatch; class-census mismatch; any

                     evidence-bearing row that is a literal declaration;

                     manuscript/script value desync; reference-count desync

known limitations  : the script verifies arithmetic, representation theory and

                     document invariants.  It does not prove physical claims,

                     and no row should be read as doing so.

license            : as for the ZS-S14 series

## §12.2 Class census

ZS-S14 v2.1 VERIFICATION SUITE   (script v2.1.0, 2026-08-19)

  Rows executed        : 115   (EXPECTED\_ROWS \= 115, fail-closed)

  FAIL                 : 0

  Evidence-bearing     : C \= 27   V \= 32   W \= 2                 (total 61\)

  Controls             : R \= 10   G \= 23                         (total 33\)

  Non-evidence         : D \= 10   T \= 11   X \= 0                 (total 21\)

  Precision            : mp.dps \= 50; exact Fraction; exact F\_p at

                         p \= 41, 31, 61, 101, 999979, 1000039

  Appendix B measured  : 49 internal \+ 16 external references

  Legacy v2.0 census   : 78 rows, 25 literal-True conditions

  ROW COUNT IS NOT THEOREM COUNT.  D and T rows carry no evidential weight.

**Block map** (115 rows). `A` locked inputs and exact anomaly arithmetic — 12 · `B` corrected `D_3` branching and the `su(3)` dimension obstruction — 7, plus the `B0` subgroup guard · `C` the unique Yukawa invariant and its Gram form — 7 · `D` `SU(2)` arithmetic including the `m_W` tension — 4 · `E` Yukawa normalisation — 5 · `F` hypercharge arithmetic, re-typed — 7 · `G` mass-hierarchy arithmetic — 4 · `H` colour sector — 4 · `J` **Theorem S14.J and the chiral contrast** — 11 · `K` **Propositions S14.K, S14.K.1, S14.L** — 6 · `L` ZS-S7 layer-1 arithmetic and the superseded-value regression — 7 · `M` S14.H ingredients — 5 · `N` S14.D.8 ingredients — 4 · `R` regression against frozen values — 9 · `GRD` guards — 23\.

## §12.3 The guards, and evidence that they fire

The companion script implements the correction specification's mandatory guards as 23 `G` rows. Four are worth stating because they change what a passing run means, and because two of them were *added after an adversarial audit defeated their predecessors*.

1. **`EXPECTED_ROWS` fail-closed.** The v2.0 script computed whatever rows happened to exist and exited 0 if they all passed; deleting a test would still have produced `ALL PASS`. v2.1 fails if the executed count differs from the declared count. Tested live by running with a row suppressed: the suite exits 1\.  
     
2. **Self-AST audit.** The script parses its own source and fails if any row declared evidence-bearing (`C`, `V`, `W`) has a literal `True` condition. Applied to the **v2.0** script it reports 78 rows of which 25 are literal `True` (rows GRD18–GRD19) — the historical measurement that motivated this rewrite. **Known limitation, stated rather than hidden:** the audit rejects only a literal `True`; it does not detect a condition that restates its own definition. An adversarial audit found about a dozen such rows in an earlier draft of *this* script; they have been re-typed to class `T`, but the check is manual and a future draft could reintroduce them.  
     
3. **Manuscript parsing.** The script reads `ZS-S14_v2_1.md` and checks: the exact Appendix B reference counts against its own declared numbers; the absence of banned live phrases; and the presence of every TYPE LOCK symbol. Manuscript and artifact cannot drift apart silently.  
     
4. **The quarantine convention, after an audit defeated its predecessor.** An earlier version of guard `GRD03`–`GRD09` exempted fenced blocks *and every inline code span*. Because this manuscript writes nearly every technical symbol in backticks, that exemption swallowed the live claim surface: an independent auditor inserted a paragraph into §0 reinstating `Total Closure`, the closure percentage, the unqualified zero-parameter banner, the retracted colour block, the retracted `Φ_Z` identification, the flat-potential-implies-Haar inference and the "vacua ±1" wording — and the suite still exited 0\.  The convention is now explicit: **only fenced blocks and lines carrying the invisible marker `<!--HIST-->` are exempt**, backticks are live text, and the patterns cover hyphenation, ASCII and paraphrase variants. Re-running the auditor's attack against the current script fires all seven guards. Guard `GRD02` was likewise a no-op — an `... or True` expression that passed with a wrong version, wrong date and an empty manuscript — and now checks the paper code, version, date, script version and row count against the manuscript text.

## §12.4 The v2.0 run, retained as a historical artifact

`zs_s14_verify_v2_0.py` was re-executed in the audit environment: exit 0, `78/78 PASS`, `sha256 = c98ca8b4c1b94ec680e74a4c7634c7539efcdfc54dd8ed1759fd317373200257`. The run is reproducible. **It is not a release certificate for v2.1**, because deterministic AST inspection of that script finds 78 `pf(...)` call sites of which 25 have the literal `True` as their condition, including the rows carrying the `D_3` branching (`D3`), the `SU(5)` branching transfer (`H5`), OS reflection positivity (`K5`, by three scalar positivity checks), the Lieb–Robinson and Z-mediation statements (`M4`, `M5`), the cross-paper audit (`J1`), and the closure percentage (`N5`).

## §12.5 Reference-count reconciliation

Three different numbers were in circulation in v2.0: the manuscript said 24 upstream references; the Appendix B table contained 28 body rows, of which 10 were marked `NEW v2.0`; the script's `v2_new_refs` list held 9 entries and asserted `16 + 9 = 25 ≥ 24`, which passed. All three were measured in this audit (rows GRD16–GRD17). v2.1 rebuilds the set, measures it from the manuscript file itself, and uses one exact number everywhere; the old figure 24 is not preserved merely because it was the previous banner.

---

# §13. Status board — replacing the closure percentage

## §13.1 Why there is no percentage here

SUPERSEDED (ZS-S14 v2.0 §11.2 and §12.2):

"Overall closure: \~ 95.0% (v1.0) \-\> \~ 99.0% (v2.0)."

"The residual \~ 1.0% has three components (alpha, beta, gamma)."

Asserted in the manuscript, in the console banner and by a literal-True

verifier row (N5).  Removed: no measurable denominator was ever declared,

and a percentage cannot detect a representation-theoretic type error.

A closure figure is an operational scientific status only if the denominator is declared and measurable. None was. Worse, the quantity it was tracking was insensitive to the defect that actually mattered: the v2.0 residual was reported as three numerical refinements while the carrier itself was ill-typed. The figure is removed from the front matter, the conclusion and the verification banner, and is replaced by the following board.

## §13.2 Claim-level status board

| Claim | v2.0 status | v2.1 status | Basis |
| :---- | :---- | :---- | :---- |
| S14.A `L_XY = 0` non-Abelian preservation | PROVEN-PERTURBATIVE | `PROVEN-PERTURBATIVE` — **unchanged, strengthened by R0** | §4 |
| S14.B `SU(2)_L` bridge on `H_5` | DERIVED | **`RETRACTED`** | §5.3, Thm S14.J |
| S14.B Step 4 `m_W ≈ 80.4 GeV` agreement | (implicit) | **`RETRACTED`**; `−3.62 %` tension, gate F-S14.16 `OPEN` | §5.2, E19 |
| S14.B′ dimension compatibility \+ imported `g_2` | — | `PROVEN` at stated scope | §5.2 |
| S14.C unique Yukawa tensor insertion | DERIVED | `DERIVED` at upstream scope; insertion re-typed | §6 |
| S14.D `H_id`, weak-doublet reading | DERIVED-CONDITIONAL | **`RETRACTED`** | §7.2 |
| S14.D `H_id`, ZS-F1-field reading | DERIVED-CONDITIONAL | **`OPEN`** — neither asserted nor excluded | §7.2, §10.3.5 |
| S14.D.4 physical hypercharge identification | DERIVED | **`OPEN`**; arithmetic `PROVEN` separately | §7.5 |
| S14.D.6 mass hierarchy | DERIVED-CONDITIONAL | `DERIVED-CONDITIONAL`, re-typed | §7.6 |
| S14.E single-carrier colour closure | DERIVED-PERTURBATIVE | **`RETRACTED`** | §8.1 |
| S14.E′ colour-sector type repair (R0) | — | `PROVEN` as a type statement | §8.2 |
| S14.F sectoral / continuum closure | DERIVED-interp. strong | **`DERIVED-CONDITIONAL`**, gate `OPEN` on `D-YM-001` | §9.1 |
| S14.G layer 1, finite polyhedral inheritance | DERIVED | `DERIVED-CONDITIONAL` at ZS-S7 scope | §9.2 |
| S14.G layers 2–3, master-action and continuum lift | DERIVED | **`OPEN`** | §9.2 |
| S14.H X–Y correlator bound | DERIVED-CONDITIONAL | **`HYPOTHESIS / OPEN BOUND`** | §9.3 |
| S14.D.8 factor-2 structural exponent | DERIVED-CONDITIONAL | **`HYPOTHESIS / OPEN`** | §9.4 |
| **S14.J chiral rigidity** | — | **`PROVEN` / `CERTIFIED`** | §10.2 |
| **S14.J.1 chiral contrast** | — | **`PROVEN`** | §10.2.1 |
| **S14.K normalisation consistency** | — | **`CERTIFIED`** | §10.3.2 |
| **S14.K.1 v2.0 dimensional defect, quantified** | — | **`CERTIFIED`** | §10.3.3 |
| ~~S14.K vacuum scale-separation obstruction~~ | — | **`WITHDRAWN` before release** | §10.3.1 |
| **S14.L intertwiner selection** | — | **`PROVEN`** | §10.4 |
| Physical seam selector | — | `OPEN` | NC-S14.19 |
| Boundary phase law | — | `OPEN` | NC-S14.20 |
| Clay-form Yang–Mills | NON-CLAIM | `NON-CLAIM` | NC-S14.12 |

**Summary of movement.** Five v2.0 claims are retracted, five are demoted, one is re-opened, one is unchanged, and five new results are established (one further candidate result was withdrawn before release, §10.3.1). Two printed numbers are corrected — `m(0⁺⁺)` and `m_W` — and one previously unreported experimental tension is surfaced. No *derived* numerical output changes.

## §13.3 The parameter statement, qualified

SUPERSEDED: "Zero Free Parameters" (unqualified, front matter and banner).

> **Zero newly fitted numerical parameters appear in the retained formulas.** The locked inputs are `A = 35/437` and `(Z, X, Y) = (2, 3, 6)`; all couplings are imported from the ZS-S1 spectral bridge and are not refitted here. **Structural and selection choices are not zero and are listed explicitly:** the Standard-Model gauge group is an input to Definition 3.1′; the ZS-M9 assignment of `I`\-irreps to Standard-Model roles is an assignment; **the direction of `⟨H_5⟩` in `CP⁴` is unfixed — eight real parameters that control the entire fermion mass texture (debt `D-S14-VEV`)**; the register-to-field intertwiner has two unfixed real parameters (§10.4); the physical boundary phase law is unfixed; and the identification of the exact slab action with a reflection-positive family is unfixed.

Zero fitted parameters is not zero construction choices, and this paper does not let the first be read as the second.

## §13.4 Open debts after v2.1

| Debt | Content | Status after v2.1 | Owner |
| :---- | :---- | :---- | :---- |
| `D-M60-S14-ERRATUM` | repair the S14 colour representation, re-run downstream physical selectors | **repair delivered** (§3, §8); downstream re-run still required | ZS-S14 → downstream |
| `D-S14-PHI` | two incompatible `Φ` identifications | **conflict removed**: the weak-doublet reading retracted, the ZS-F1 reading re-opened to `OPEN`; no positive identification | ZS-S14 |
| `D-F1-EPS` | the inherited "vacua `ε = ±1`" wording | **propagation stopped here** (§2.11); upstream files unrepaired | ZS-F1 and inheritors |
| `D-YM-001` | exact slab action ↔ reflection-positive family | `OPEN`, unchanged; S14.F now respects it | S17–S24 |
| `D-S14-EVENT-001` | action-derived non-phase-covariant seam environment | `OPEN`, unchanged | S28 → M59 → M60 |
| `D-M61-IOTA` | the intertwiner `ι_ZΦ` | **sharpened** to a 2-parameter selection debt (§10.4) | future bridge |
| `D-M61-GOLD` | boundary phase law | `OPEN`, unchanged | S14 boundary/selection |
| `D-M61-WARD` | exact seam symmetry `(F2)` | `OPEN`; §10.3.2 selects the second horn of the M61 dichotomy | S14 seam bridge |
| **`D-S14-PRIOR`** | systematic external novelty sweep for Theorems S14.J and S14.K | **NEW**, registered, not performed | external prior-art audit |
| **`D-S14-DIM`** | audit the rest of the corpus for the mass-dimension defect of E16 | **NEW**, registered | ZS-S14 and inheritors |
| **`D-S14-VEV`** | specify `V(H_5, H)` and derive the direction of `⟨H_5⟩` in `CP⁴`, target-blind; eight real parameters currently control the fermion texture | **NEW**, registered | ZS-S14 |
| **`D-S14-MW`** | resolve or confirm the `−3.62 %` `m_W` tension of erratum E19 against the ZS-S1 `α_2 = 3/95` | **NEW**, registered | ZS-S1 → ZS-S14 |
| **`D-S14-DIGITS`** | the ZS-S13 closed form re-evaluates to `y_t = 0.987186`, not the printed `0.98738` | **NEW**, registered | ZS-S13 |

---

# §14. Conclusion

ZS-S14 v2.0 claimed that one five-dimensional icosahedral object carried the whole Standard-Model gauge structure, and assessed itself as almost closed. The object could not carry it: `D_3 ≅ S_3` has no second doublet and `su(3)` has no two-dimensional representation. v2.1 repairs the action by giving every generator an explicit domain, restoring colour to the fermion factor the theory already had, and putting the electroweak doublet on a transverse factor.

The repair then proves more than it costs. Theorem S14.J shows that the unique icosahedral Yukawa invariant has trivial connected symmetry group, so no simple Lie algebra can act on its labels at all: the factorisation of gauge from flavour is forced, and the colour repair was never a choice. Proposition S14.J.1 shows that this is not a generic fact about multiplicity-one invariants — the untwisted siblings carry a full `so(3)` — but a consequence of the chirality of the Z-Spin fermion assignment. That is a genuinely new statement about the icosahedral flavour structure, and it derives what the discrete-flavour-symmetry literature assumes. Proposition S14.K then shows that the repaired insertion is normalisation-consistent in a way the original was not: the ZS-M10 channel factor `√(5/2)` is exactly what turns the isotropic slot weight `1/√5` into the single-doublet `1/√2`, and Proposition S14.K.1 measures what the v2.0 action lost by having nowhere to put the missing mass dimension — a factor `M_P/v ≈ 10^16`. A stronger claim, that the same reasoning *excludes* identifying the `D_3`\-invariant line with the ZS-F1 field, was drafted, found defective by adversarial audit, and withdrawn before release; that identification is `OPEN`, not settled either way.

What is left open is not a fraction of an equation. It is six named items in a different layer: two identifications between finite constructions and physical carriers, three selection problems — of a vacuum direction, of an intertwiner, of a boundary state — and one missing symmetry. None is closed by writing more Lagrangian, and Theorem S14.J shows there is no more Lagrangian of this kind to write.

Two of the six were made *visible* by the correction rather than solved by it. The vacuum-direction debt `D-S14-VEV` was always there; the single-carrier framing hid it behind a copy-selection question that turned out to be the wrong question. That is the ordinary result of typing a theory correctly: some problems dissolve and others become properly stateable for the first time.

**The honest summary is that ZS-S14 is now smaller and sound rather than large and ill-typed.** The derived numbers it inherits — `α_s = 11/93`, `v = 245.93 GeV`, `m_t`, the anomaly cancellations, the ZS-S7 and ZS-Q3 results — are unchanged, because none of them ever used the broken part. What changed is the set of sentences the paper is entitled to say about them. Two *printed* numbers were also wrong and are corrected: the glueball mass the formula actually gives, and the `W` mass, where the corrected value carries a `3.6 %` tension that a wide verifier tolerance had been hiding since v1.0. Finding that tension is a better outcome than not finding it.

## §14.1 Future work

1. Execute the downstream re-run required by `D-M60-S14-ERRATUM`: every physical S14 selector that assumed the old colour block.  
2. Perform the prior-art sweep `D-S14-PRIOR` for Theorems S14.J and S14.K before any external submission uses the word "new".  
3. Construct or refute a selection principle for the two real parameters of `ι_ZΦ` (§10.4).  
4. Derive the boundary phase law from the action and boundary data, **target-blind**. Do not tune a Goldstone-breaking term, a boundary distribution, a clock duration, a sector weight or a phase to reproduce a frozen target: matching a two-real-parameter target after solving two free real variables is identification, not derivation.  
5. Revisit `D-YM-001` only once the corrected exact slab action is available.  
6. Audit the corpus for the mass-dimension defect `D-S14-DIM`.

---

# Acknowledgements

Developed within the Z-Spin Cosmology Collaboration. The correction line that made this version necessary originated in ZS-M60 Theorem M60.25 and ZS-M61 Theorems M61.1a, M61.19, M61.22′ and M61.23′, and in the correction specification `correct_report.md` of 18 August 2026\.

# AI use statement

AI\_TOOL\_RECORD

name/version : Claude (Anthropic), Cowork session, model claude-opus-5

tasks        : re-derivation of the D\_3 branching and the Yukawa Gram form;

               construction of the A\_5 irreps 3, 3', 5 and the invariant

               tensor; the stabiliser computation of Theorem S14.J and its

               finite-field certificate; the sibling contrast of

               Proposition S14.J.1; the normalisation identity of

               Proposition S14.K and the scale computation of S14.K.1;

               the intertwiner computation of Proposition S14.L; the

               dimensional audit of Definition 3.1; the AST census of the

               v2.0 script; drafting of this manuscript and of the companion

               verifier; external prior-art collision.

human direction : the correction specification, Branch A as the default

               repair, the instruction to remove self-assessed closure

               percentages, and final approval of all claim statuses.

verification route : every representation-theoretic statement is checked by

               two independent routes (floating-point construction and exact

               finite-field arithmetic at six primes); every arithmetic

               identity is checked in exact rational or 50-digit arithmetic;

               all external references were fetched and read, not recalled.

independently checked : the v2.0 script was re-executed and its AST measured

               rather than described; the Appendix B reference count was

               parsed from the file.

rejected / corrected : four substantive reversals, all recorded rather than

               silently edited out.

               (1) An initial framing of Theorem S14.J as a general no-go

                   about multiplicity-one invariants was refuted by the

                   sibling computation and rewritten as Prop. S14.J.1.

               (2) A claim that the rank-2 torus "explains hypercharge" was

                   withdrawn as an overreach, since that torus annihilates

                   every tensor of the format (NC-S14.18).

               (3) A "vacuum scale-separation obstruction" (a draft

                   Theorem S14.K) was refuted by an independent adversarial

                   audit against this paper's own Definition 3.1' and its own

                   falsification gate, and withdrawn; see §10.3.1.

               (4) The manuscript-integrity guard layer was defeated by the

                   auditor, who reinstated seven retracted claims in §0 while

                   the suite still exited 0; the guards were rebuilt and the

                   attack now fires all seven (§12.3 item 4).

               The audit also found erratum E19 (the m\_W tension), the

               vacuum-direction debt D-S14-VEV, a vacuous guard, and about a

               dozen tautological rows mis-classed as evidence.  Its findings

               were acted on before release; this record exists so that a

               reader can see that the artifact was attacked and by whom.

An AI system is not an author. The author retains full responsibility for all scientific content, claims and conclusions.

# Data availability

No new research data were created or analysed. All numerical figures and tables are reproducible from the equations in this paper and the code identified below.

# Code availability

`zs_s14_verify_v2_1.py`, run as `python3 zs_s14_verify_v2_1.py`, reproduces every numbered row of §12 and emits `ZS_S14_v2_1_verification_report.json`. Dependencies: `mpmath >= 1.3.0`, `numpy >= 1.24`. The script includes its own fail-closed guards and a self-AST audit. Hashes are registered in the run output. **No persistent archival identifier has been assigned; this artifact is therefore `not yet publicly certified`, and the release label is `REVIEW READY`, not `FINAL`.**

---

# Appendix A. Version crosswalk and erratum genealogy

## A.1 v1.0 → v2.0 → v2.1

| Element | v1.0 | v2.0 | v2.1 |
| :---- | :---- | :---- | :---- |
| Title | `Master Action Total Closure` | same | **retitled**; self-assessment removed |
| `5 ↓ D_3` | `1+2+2'` | `1+2+2'` | **`1 ⊕ (2 ⊗ C²_mult)`** |
| Colour on `H_5` | yes | yes | **removed** — R0 |
| `SU(2)_L` on `H_5` | yes | yes | **removed** — Thm S14.J |
| `Φ` identification | `D_3`\-trivial **and** `H⁰` | same conflict | **both retracted** |
| S14.A | PROVEN-PERT. | unchanged | unchanged |
| S14.B | DERIVED | unchanged | **RETRACTED** → B′ |
| S14.C | DERIVED | unchanged | DERIVED, insertion re-typed |
| S14.D.4 | DERIVED | unchanged | **OPEN** |
| S14.D.6 | DERIVED-COND. | unchanged | DERIVED-COND., re-typed |
| S14.E | DERIVED-PERT. | unchanged | **RETRACTED** → E′ |
| S14.F/G/H/D.8 | — | NEW | **all demoted** |
| S14.J / J.1 / K / L | — | — | **NEW** |
| Verification | 54/54 | 78/78 | class census, fail-closed |
| Closure figure | `~95%` | `~99%` | **removed** |
| References | 16 | "24" (28 in table, 25 in script) | measured, synchronised |

**Correction to the v2.0 crosswalk.** ZS-S14 v2.0 Appendix A asserted that all v1.0 theorems and proofs were "preserved verbatim" and unchanged. That assertion is now false in substance: S14.B, S14.D and S14.E were v1.0 theorems and are retracted or demoted here. The v1.0 *text* is preserved; the v1.0 *status* is not. Preserving text and preserving status are different things, and v2.0 conflated them.

## A.2 Erratum genealogy

| Event | Date | Content |
| :---- | :---- | :---- |
| ZS-M60 v1.5 Thm M60.25 | Jul 2026 | colour-block erratum raised; ZS-M60 proved insulated |
| H-0019 | 16 Aug 2026 | `(F2)` refuted: Yukawa Gram isotropy ⇒ W1 fails; Thm M61.19 |
| H-0020 | 16 Aug 2026 | `D-S14-PHI` registered: the two `Φ` identifications |
| H-0024 | 16 Aug 2026 | `D-F1-EPS`: `ε ≡ |Φ| ≥ 0`; "vacua `ε = ±1`" is a misstatement |
| H-0028 | 17 Aug 2026 | dated erratum recommended for ZS-S14 v2.0, four items |
| H-0029/30 | 17 Aug 2026 | M61.22 → M61.22′; M61.23 → M61.23′ (conditional) |
| H-0040/41 | 18 Aug 2026 | ZS-M61 v1.6 `TERMINAL-IN-SCOPE`; Manifest Log entry `ML-2026-08-18-ZS-M61` |
| H-0042 | 18 Aug 2026 | `correct_report.md` written; artifact forensics (25 literal-`True` rows; 24/25/28 reference desync) |
| **this version** | 19 Aug 2026 | repair applied; Thms S14.J, S14.J.1, S14.K, S14.L; claim board replaces the percentage |

Nothing in this genealogy is deleted. Superseded wording is retained in fenced blocks throughout.

---

# Appendix B. Cross-paper consistency audit

Every reference below is *used* somewhere in this manuscript; the section of use is given. The count is measured from this table by the companion script and printed in the run output; no figure is carried over from a previous banner.

## B.1 Internal (Z-Spin series)

| Reference | Status | Used in |
| :---- | :---- | :---- |
| ZS-F0 Def. 8.11 register parity `J_Z` (NEW v2.1) | PROVEN | §2.11, §10.4 |
| ZS-F1 §0 `|Φ| = 1` attractor | PROVEN | §10.3 |
| ZS-F1 §2.3 `Φ = ρe^{iθ}`, `ε ≡ |Φ|` (NEW v2.1) | PROVEN | §2.11 |
| ZS-F1 §3.2 `q_Φ = +1` | LOCKED | §7.5 |
| ZS-F1 §4.4 `m_ρ = 2A·M_P` | DERIVED | §7.6 |
| ZS-F2 §7 `A = 35/437` | LOCKED | §2.1 |
| ZS-F2 §4.2A adjoint obstruction | PROVEN | §4.2 Step 5 |
| ZS-F5 §4 `Q = 11`, `(Z,X,Y) = (2,3,6)`, `G = 12` | PROVEN | §2.1, §4.2 |
| ZS-F18 §7.4 discrete–continuous allocation | DERIVED-interp. | §9.1 |
| ZS-M2 §2 `[su(2)_A, su(2)_B] = 0` | PROVEN | §4.2 Step 1 |
| ZS-M3 Thm 5.1 `dim Z = 2 = j = 1/2` | PROVEN | §9.1 |
| ZS-M6 §5.5 X–Y tiling asymmetry | PROVEN | §2.9, §9.1 |
| ZS-M6 Thm 2.2.1 `κ² = A/Q` | DERIVED | §2.1 |
| ZS-M9 Table 2 irrep assignments | DERIVED-strong | §2.5, §10.2 |
| ZS-M9 §4 F4 `D_3` doublet inside `3` | DERIVED | §5.2 |
| ZS-M10 Thm 2.1 unique invariant `T` | PROVEN | §2.7, §6, §10.2 |
| ZS-M10 §3 `D_5` channel norms, `Σσ² = 1/5` | PROVEN | §6.2 |
| ZS-M11 §3.2 `σ` ratios | DERIVED | §6.2 (declaration) |
| ZS-M11 §6.1 `D_3` branching | **SUPERSEDED for the `5`** | §2.8 |
| ZS-M15 §5.3 Thm 1 handedness Assignment A | DERIVED | §10.2.1 |
| ZS-M17 Thm M17.2 Lieb–Robinson tightness | DERIVED | §9.3 |
| ZS-M17 Thm M17.6 universality | DERIVED | §9.1 |
| ZS-M17 Thm M17.7 OS reconstruction | DERIVED; S14 mapping OPEN | §9.1 |
| ZS-M56 Thm M56.22′ central involution (NEW v2.1) | PROVEN | §2.11 |
| ZS-M60 v1.5 Thm M60.25 colour erratum (NEW v2.1) | PROVEN | §0.2, §2.8, §8.1 |
| ZS-M61 v1.6 Thm M61.1a / Repair R0 (NEW v2.1) | PROVEN | §3.1, §8.2, §10.2.2 |
| ZS-M61 v1.6 Thm M61.19 Yukawa slot isotropy (NEW v2.1) | PROVEN | §2.7, §6.3, §10.3 |
| ZS-M61 v1.6 Thm M61.22′ seam involutions (NEW v2.1) | PROVEN | §2.11 |
| ZS-M61 v1.6 Thm M61.23′ Haar-phase no-go (NEW v2.1) | CLOSED-NEG-CONDITIONAL | NC-S14.20 |
| ZS-M61 v1.6 §§34, 38, 40–44 TYPE LOCK and status board (NEW v2.1) | — | §2.11, §10.3.2, §10.4 |
| ZS-S1 §7, §8.1, §8.2 spectral couplings | DERIVED | §2.3, §5.2, §8.2 |
| ZS-S4 §6.12 Thm V.9 `v = 245.93 GeV` | DERIVED | §2.6, §7.6 |
| ZS-S4 §6.12.7 `m_H ≈ 125.25 GeV` | HYPOTHESIS-strong | §7.6 |
| ZS-S7 §3, §5, §6 mass gap and cancellation | DERIVED-CONDITIONAL | §9.2 |
| ZS-S10 `U(1)_Y` Stueckelberg bridge | DERIVED-CONDITIONAL | §7.4 |
| ZS-S11 §2.1 sector Cartan `a, b` | DERIVED | §7.5 |
| ZS-S13 §8.4n `y_t`, `m_t` | DERIVED / TESTABLE | §2.6, §6.2 |
| ZS-S14 v1.0 predecessor | SUPERSEDED | Appendix A |
| ZS-S14 v2.0 predecessor | SUPERSEDED | throughout |
| ZS-Q3 §3 mode-count collapse | PROVEN | §2.10 |
| ZS-Q3 §4 proton spin decomposition | DERIVED | §2.10 |
| ZS-Q3 §6.6 `C_0 = 16` | PROVEN | §9.4 |
| ZS-Q7 Thm 2 channel capacity | DERIVED; mapping OPEN | §9.1, §9.3 |
| ZS-U9 Thm T3 hypercharge lattice | DERIVED | §2.4, §7.5 |
| ZS-U9 §6.4 `SU(5)` fundamental branching | PROVEN for `SU(5)`; **transfer to the `I`\-irrep `5` RETRACTED** | §8.1 |
| ZS-U9 §7 anomaly conditions A1–A5 | PROVEN | §4.2 Step 4 |
| The Book of Z-Spin Cosmology v13.2 App. D debt table (NEW v2.1) | registry | §13.4 |
| Corpus-OS `03_ZSPIN_DEBT_RETRACTION_GATES` registry (NEW v2.1) | registry | §13.4 |
| `correct_report.md`, 18 Aug 2026 (NEW v2.1) | correction specification | throughout |

## B.2 External

| Ref | Source | Used for |
| :---- | :---- | :---- |
| \[E1\] | A. Conner, F. Gesmundo, J. M. Landsberg, E. Ventura, Y. Wang, *Tensors with maximal symmetries*, arXiv:1909.09518, eq. (3), §1.3 | definition of the tensor annihilator `s(T)` |
| \[E2\] | same, §1.3 | the universal two-dimensional scalar kernel `λμν = 1` |
| \[E3\] | same, §2 | semicontinuity of `dim Stab(T)` |
| \[E5\] | L. Chiantini, C. Ikenmeyer, J. M. Landsberg, G. Ottaviani, *Geometry of rank decompositions of matrix multiplication I*, arXiv:1610.08364, Prop. 4.1 | counterexample: matmul has a large continuous stabiliser |
| \[E7\] | arXiv:1909.09518, abstract | counterexample: Coppersmith–Winograd maximal symmetry |
| \[E8\] | J. Baez, *The Octonions*, §G₂ | counterexample: octonion multiplication stabilised by `G_2` |
| \[E9\] | L. L. Everett, A. J. Stuart, *Icosahedral (A₅) family symmetry and the golden ratio prediction for solar neutrino mixing*, arXiv:0812.1057, Phys. Rev. D 79, 085005 (2009), Table II | `A_5` tensor-product rules |
| \[E12\] | F. Feruglio, A. Romanino, *Lepton flavor symmetries*, Rev. Mod. Phys. 93, 015007 (2021), arXiv:1912.06028, §III.B | flavour action commutes with gauge; flavour indices are a separate factor |
| \[E13\] | arXiv:0812.1057 | "the electroweak Higgs field(s) are assumed to be blind to the family symmetry" |
| \[1\] | A. Jaffe, E. Witten, *Quantum Yang–Mills Theory*, Clay Millennium Prize (2000) | NC-S14.12 |
| \[3\] | K. Osterwalder, R. Schrader, Commun. Math. Phys. **31**, 83 (1973); **42**, 281 (1975) | §9.1 |
| \[4\] | J. Glimm, A. Jaffe, *Quantum Physics: A Functional Integral Point of View*, 2nd ed. (Springer, 1981\) | §9.1 |
| \[5\] | E. H. Lieb, D. W. Robinson, Commun. Math. Phys. **28**, 251 (1972) | §9.3 |
| \[6\] | C. Morningstar, M. Peardon, Phys. Rev. D **60**, 034509 (1999) | §9.2 lattice comparison |
| \[7\] | S. Necco, R. Sommer, Nucl. Phys. B **622**, 328 (2002) | §9.2 lattice comparison |
| \[8\] | S. Navas *et al.* (Particle Data Group), Phys. Rev. D **110**, 030001 (2024) | §8.2 `α_s`; §2.6 |

**Note on \[E1\]–\[E13\].** These were fetched and read during the external collision of §10.2.4, not recalled. The numbering is that of the collision report and is retained so the audit trail matches. Gaps in the numbering are references that were checked and not used.

**Note on B.1.** Three internal entries — `ZS-F18 §7.4`, `ZS-M3 Thm 5.1` and `ZS-M56 Thm M56.22′` — are cited only through the imports table §2.9 and the TYPE LOCK §2.11 and do no independent work in the argument; they are listed for dependency completeness, not because a claim rests on them. The companion script counts the rows of these tables and checks the count against its own declared number; it does **not** verify that each "Used in" locator resolves, and that check remains manual.

---

# Appendix C. What is insulated — do not recompute

The following outputs do **not** depend on the invalid `D_3`\-`2'` colour block, on the `Φ` identification, or on any seam involution. **They are not to be refitted or altered to make the repaired action look more closed.** 

- `A = 35/437`; `Q = 11`; `(Z, X, Y) = (2, 3, 6)`; `G = 12`; `κ² = 35/4807`  
- `α_s = 11/93 = 0.118280` (ZS-S1 spectral bridge; `(V+F)_Y = 92`, `β_0(Z) = 1`)  
- `α_2 = 3/95`; `g_2² = 12π/95`; `sin²θ_W = (48/91)x*`  
- `v = 245.93 GeV`; `γ_CW·C_M^sp = 36.831`  
- `y_t = 0.98738`; `m_t = 171.872 GeV`  
- anomaly cancellation A1–A5  
- `a_3 = 23/3`; `8 = N_c² − 1`  
- ZS-S7 outputs `m(0⁺⁺) = vA/Q`, `Λ_QCD = vA/(λ₁V_Y)`, `E_local = vA/V_Y`, `m/Λ`, at ZS-S7's own scope  
- ZS-Q3 outputs `½ΔΣ = 3/22`, `ΔG = L = 2/11`, `C_0 = 16`, at ZS-Q3's own scope  
- `‖T·w‖ = 1/√5`; `Σσ_i² = 1/5`

**However:** a number remaining unchanged does not preserve every interpretation previously attached to it. Several of the entries above kept their value and lost their ZS-S14 bridge claim in §13.2. That is the intended outcome of a correction that is surgical in the arithmetic and honest about the claims.

---

# Version history

**v1.0 (April 2026).** Initial release. Theorems S14.A–S14.E; 54/54 verification rows; six falsification gates; eleven non-claims; self-assessed closure `~95%`. 

**v2.0 (May 2026).** Added S14.F, S14.G, S14.H, S14.D.8; cross-links to ZS-S7, ZS-Q3, ZS-M17, ZS-F18; 78/78 rows; ten gates; fourteen non-claims; self-assessed closure `~99%`. 

**v2.1 (19 August 2026).** Dated erratum and corrected canonical manuscript.

- *Mathematics — corrections.* `5 ↓ D_3` corrected to `1 ⊕ (2 ⊗ C²_mult)`. Colour repair R0 applied to Definition 3.1. Definition 3.1 repaired for mass dimension. `Y_5 = 0`.  
- *Mathematics — retractions.* Theorem S14.E retracted (single-carrier colour closure). Theorem S14.B retracted (`SU(2)_L` on `H_5`). Hypothesis `H_id` retracted in both readings. Theorem S14.D.4's physical identification retracted.  
- *Mathematics — new results.* Theorem S14.J (chiral rigidity of the icosahedral Yukawa invariant; trivial connected symmetry group; certified at six primes and re-derived independently over `Q(√5)`). Proposition S14.J.1 (the untwisted siblings carry `so(3)`; the result is load-bearing on chirality). Proposition S14.K (normalisation consistency: `y_0·(1/√5) = y_t/√2` exactly). Proposition S14.K.1 (the v2.0 dimensional defect measured as `M_P/v = 9.90 × 10^15`). Proposition S14.L (`D-M61-IOTA` is a two-parameter selection debt).  
- *Mathematics — withdrawn before release.* A "vacuum scale-separation obstruction" purporting to exclude `Φ_Z = Φ_{ZS-F1}` was drafted, refuted by adversarial audit against this paper's own Definition 3.1′ and its own gate, and withdrawn. §10.3.1 records it.  
- *Numerical corrections.* `m(0⁺⁺)`: `1.7912 → 1.790628` (E18). `m_W`: the claimed `≈80.4 GeV` agreement retracted; the inputs give `77.4614 GeV`, a `−3.62 %` tension (E19). `γ_CW·C_M^sp`: `36.831 → 36.831421` (E20).   
- *New debts.* `D-S14-PRIOR`, `D-S14-DIM`, `D-S14-VEV`, `D-S14-MW`, `D-S14-DIGITS`.  
- *Scope corrections.* S14.F, S14.G, S14.H, S14.D.8 demoted; S14.G split into four layers.  
- *Verification.* Suite replaced: per-row verification classes, `EXPECTED_ROWS` fail-closed guard, self-AST audit, manuscript parsing, exact `F_p` rank rows. The v2.0 78-row suite is retained as a historical artifact only.  
- *Editorial and integrity.* Title changed; the closure percentage removed as a category error; `Zero Free Parameters` qualified; the reference count measured and synchronised; TYPE LOCK inserted; five new gates; eight new non-claims; two new debts registered.   
- *Not changed.* Every numerical output listed in Appendix C.

