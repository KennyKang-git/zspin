# ZS-M62 v1.4.2

## Oriented-Mass Geometry of Reflection Asymmetry

### Peeling duality, sharp atomic extremizers, an exact semidefinite form, and a closed-form asymmetry price for complex contractions

**Paper code / version:** `ZS-M62 v1.4.2` **Date:** 2026-08-19 (KST) **Supersedes:** `ZS-M62 v1.4.1`, which superseded `v1.4` (both release-package patches only — **the mathematics is bit-identical**), which superseded `v1.3`, `v1.2`, `v1.1`, `v1.0` (all retained as historical artifacts, none deleted). The digest published for `v1.4` remains the digest of `v1.4`; this version carries its own, so one version label never names two contents. **Project:** Z-Spin Cosmology **Release label:** `REVIEW READY` (scientific content) — **five** independent adversarial audits performed and fully incorporated (v1.0: `AUDIT-MAJOR-REVISION`, release-blocking; v1.1: `REVIEW READY` maintained; v1.2: `AUDIT-CORRECTION-REQUIRED`, blocking for external submission; v1.3: scientific content `REVIEW READY`, **release package** `ARTIFACT CORRECTION REQUIRED` — the delivered manuscript had been Markdown-escaped in transit, which broke two guards and the byte hash; v1.4: scientific content `REVIEW READY`, one **artifact** finding — the copy the auditor held had drifted from the verified one and `M8` detected it correctly but could not say **where**). Neither the fourth nor the fifth audit found a mathematical error. `FINAL` is withheld: there is no persistent archival identifier, no qualified-human proof review, and the prior-art sweep `D-M62-PRIOR` is open — and it has now fired **twice**. **Article class:** full research paper (mathematics with a physical-bridge section) **Primary audience:** convex geometry / measure theory / moment problems; mathematical physics **Predecessors:** ZS-M61 v1.6, ZS-M60 v1.5, ZS-S14 v2.1, ZS-M1, ZS-F1 **Verification artifact:** `zs_m62_verify_v1_4_2.py` (91 rows, 0 FAIL, exit 0), ledger `zs_m62_verify_v1_4_2.json`. Fast identity check: `python3 zs_m62_verify_v1_4_2.py --identify` (sub-second).

> **v1.4.2 correction notice.** A second release-package patch, **self-detected, with no audit in between**, and it is the plainest instance yet of the class the last three versions have been about. The artifact manifest quotes `sha256(script)`. **No row checked it.** It went stale the moment `v1.4.1`'s own repair edited the script *after* the hash had been written into the manuscript, and the entire 90-row suite then passed — `M8` green, `M9` green, `--identify` clean — with a wrong hash printed on the page. The reason is exact and worth stating without softening: every self-referential row added in `v1.4` and `v1.4.1` certifies the manuscript **against itself**, and the manifest also makes a claim **about a different file**, which nothing was pointed at. Row `M10` now recomputes the running script's SHA-256 and fails unless the manuscript declares it. The ledger hash is the one manifest claim that *cannot* be guarded this way — the ledger records the outcome of every row, so a row verifying the ledger's own hash has no fixed point — and that limit is now printed in the manifest as a limitation rather than left for a reader to discover. Mathematics unchanged; parts `B` and `C` still carry the `v1.4` digests. Register `E-M62-23`; gate `F-M62.30`.  
>   
> **v1.4.1 correction notice (retained).** This is a **release-package patch**. Not one theorem, proof, constant, extremizer, table of numbers or Z-Spin value differs from `v1.4`; parts B and C of this manuscript — Sections 2–9 and Sections 10–11 — are unchanged, and their digests are published below so that claim is checkable rather than asserted. The fifth audit ran the `v1.4` artifact pair against its own copy of the manuscript and `M8` fired: the declared transport digest did not match the recomputed one, while the SHA-256 of the *script* matched exactly. Two things follow. First, `M8` was **right** — the copy had drifted, and the copy in the author's hands had not (it still recomputes to the published `v1.4` value); the fault is in the path between them, and unlike the `v1.3` failure it was not reproducible by any escaping, dash, quote, Unicode-normalisation, line-ending or accent transformation, all of which were tried and none of which yields the auditor's digest. Second, and this is what the patch fixes: `M8` was **binary**. It said *different* and stopped, leaving the reader with no way to see what had changed — which is precisely the defect class of `E-M62-17` (a guard that cannot localise) and `E-M62-21` (an anchor that cannot localise), one level up, now applied to identity itself. This version therefore publishes a **fixed-point digest for each of five parts** of the manuscript, so a mismatch names the part that drifted and a reader can tell a bookkeeping edit in Part D from a change to the mathematics in Part B; and it adds a **`--identify` mode** that answers the identity question in well under a second, without running the suite. The register entry is `E-M62-22`; the fifth-audit record is §15.6.  
>   
> **v1.4 correction notice (retained).** The fourth audit found **no new mathematical error** and confirmed the scientific content as `REVIEW READY`. It found instead that the *delivered release package* was broken: the manuscript had been Markdown-escaped somewhere in transit (`Theorem 17\.`, `\+`, `\<=`), so the two guards that read the raw bytes — `M6` and `M7` — failed on the copy the auditor actually held, and the SHA-256 of the delivered file did not match the one printed here. The verifier had been checking a normal form in some places and raw bytes in others. Three things follow, and all three are in this version. (i) Every manuscript guard now runs on a **transport-invariant normal form** (`transport_norm`, with backslash-unescaping iterated to a fixpoint), and the manuscript is additionally identified by a **transport-invariant digest** that is unchanged by escaping, whitespace and Unicode dash variation; the byte hash is retained but is no longer the only identifier. (ii) The guard suite is now **self-referentially verified**: row `M9` re-runs every manuscript guard on a synthetically escaped copy of this manuscript and fails unless every verdict agrees and the digest is invariant, and row `M8` makes the manuscript certify its own transport-invariant digest as a fixed point. `M9` caught a real defect in its own repair while this version was being written — `normalise()` undid one level of escaping where two were present — which is recorded as part of erratum `E-M62-18`. (iii) The semidefinite claims of Section 7 now carry **solver-free evidence** (rows `F5`, `F6`), so an environment without `cvxpy` — the fourth auditor's environment, and the first's — still verifies the mathematics of Theorems 13 and 14 rather than only recording four fail-closed rows. The full register is §15.1; the fourth-audit record is §15.5.  
>   
> **v1.1 correction notice (retained).** Three genuine defects of v1.0 were corrected in v1.1, not paraphrased away: Theorem 3 was **false** at the quantifier level once the observables are only assumed bounded and measurable; the dual formula (5.1) of Theorem 6 was **missing an outer** `max{0, .}` and could return a negative value; Theorem 18 had the **wrong orientation sign** for negative accumulated phase. The entropy floor of Theorem 20 was **retyped from a contributed result to an imported one**. Two artifact defects were also fixed.  
>   
> **v1.3 correction notice.** The third audit found **one genuine mathematical error and one prior-art collision**, both load-bearing for external submission and neither affecting the architecture or any Z-Spin number. (i) Theorem 17(iv) stated the `Psi >= pi` value of `A*` by a **single** formula; it is false on `|Re lambda| + |Im lambda| <= 1`, and at `lambda = 0` it returns `1/2` where the true value is `0`. It is now stated piecewise, in agreement with Eq. (8.5), with an explicit counterexample (Remark 17.3) and a regression that also refutes the superseded form. (ii) Theorem 2, the peeling identity, is **retyped from `OPEN-NOVELTY` to `IMPORTED CORE + SPECIALIZED`**: a second proof is given showing it is two lines from the classical overlapping-coefficient identity, and the trimming/contamination pointer supplied by the audit is recorded with its verification status. The external-novelty case now rests on Theorems 3, 5, 7–9 and 15–17. The full register is §15.1; the third-audit record is §15.4.  
>   
> **v1.2 correction notice (retained).** The second audit found **no release-blocking defect and no new mathematical error**. It reported two wording inconsistencies left over from the v1.1 repair — the Introduction still called the observables "bounded measurable" after `(H-CONT)` had been declared, and the Abstract wrote `Psi` with `c` where the general theorem needs `|c|` — and one reproducibility obstacle: the suite did not finish inside the auditor's 180-second budget. All three are fixed, each with a guard or a documented profile. In addition, v1.2 adds **block `Y`**: exact symbolic certification, in a computer-algebra system, of the algebraic steps inside the proofs of Theorems 7, 8, 9, 11, 16, 17 and 20\. That block narrows — it does not close — the standing gap that the ledger is not a proof checker. The full register is §15.1; the second-audit record is §15.3.

---

## Scope declaration

This is a paper about the convex geometry of one extremal problem:

> among all probability measures on a reflection-invariant compact set whose prescribed linear data are fixed, which one is closest to being reflection-symmetric, and how close is it?

It is **not** a paper about the Standard Model, about cosmological dynamics, or about the derivation of a boundary state from an action. Sections 2–9 use no physical input whatsoever and remain valid if every Z-Spin premise is deleted. Section 10 applies the mathematics to one specific Z-Spin object — the seam-odd contraction multiplier — and produces a **conditional, quantitative obstruction**, not a physical derivation. Every step across the formal/physical boundary is flagged, and the standing open debts (`D-M61-IOTA`, `D-M61-GOLD`, `D-M61-WARD`) are not closed here.

**Standing hypothesis (H-CONT).** Every observable family `Phi` in Sections 3–10 is **continuous** on the compact carrier. This is not cosmetic: Remark 3.3 exhibits a bounded measurable `Phi` for which the master theorem, stated with closed convex hulls, is false. All applications used here — truncated Fourier data and the multiplier kernel — are continuous, so nothing in the paper is lost.

The single-sentence contribution:

> Under the total-variation convention locked in Section 2, we prove that the minimum reflection asymmetry of a measure with prescribed linear data equals the minimum *mass fraction that has to be removed to leave a symmetric measure*, that this is a nested-convex-body threshold problem with no duality gap, with reflection-coupled atom bound `n + floor(n/2) + 1`, with an exact semidefinite representation on the circle and on any arc, and with a closed-form first-order solution; applied to the Z-Spin contraction multiplier this converts an infinite-dimensional state-selection problem into the single scalar inequality `||S_o||_inf >= 1.00422493384939229`.

---

## Verification summary

Artifact       : zs\_m62\_verify\_v1\_4\_2.py   (one-command run: python3 zs\_m62\_verify\_v1\_4\_2.py)

Result         : 91 rows PASS / 0 FAIL, exit 0        \[FULL profile\]

Evidence-bearing : C \= 22 (certified: exact symbolic algebra, or mp.dps \= 40\)

                   V \= 30 (numerical, declared tolerance)

                   W \= 10 (witness / counterexample / contact count / extremiser exhibition)

                   R \=  1 (independent-implementation regression)

Controls         : G \= 19 (fail-closed guards, incl. manuscript integrity, scope consistency,

                           the statement guard for Theorems 2 and 17(iv), the SELF-IDENTIFYING

                           and part-localizing digest row M8, the SELF-REFERENTIAL

                           guard-invariance row M9, and the CROSS-ARTIFACT hash row M10)

Non-evidence     : D \=  5 (declarations with proof pointers; incl. the profile declaration)

                   T \=  4 (tautology / premise-sharing controls)

                   X \=  0

                   P \=  0   \-- class P is not used: the script does not prove theorems

Profiles         : FULL  50-75 s single core \-- the only profile that may be quoted

                   QUICK \~25 s single core   \-- python3 zs\_m62\_verify\_v1\_4\_2.py \--quick

                   IDENTIFY  \< 1 s          \-- python3 zs\_m62\_verify\_v1\_4\_2.py \--identify

                                               prints the whole-document digest and all five

                                               part digests, compares them with what this

                                               manuscript declares, and exits 1 on any

                                               mismatch.  It runs no evidence row and is not a

                                               certificate; it answers only "is this the

                                               manuscript that was verified, and if not, which

                                               PART differs" (erratum E-M62-22).

                                                smoke test with reduced sample counts;

                                                prints a runtime banner saying it is NOT a

                                                certificate, and records certificate=false in

                                                the ledger

Audit block N    : eight rows, one per mathematical finding of the three audits.  N1, N2 and

                   N7 are the counterexamples that kill the superseded statements of

                   Theorems 3, 6 and 17(iv); N8 is the classical identity that retypes

                   Theorem 2\.  Every one of them fails if the defect is reintroduced.

Certificate flag : the ledger records certificate=false for any quick run AND for any run with

                   a failing row, so a partial run can never be quoted (erratum E-M62-15).

Symbolic block Y : nine rows of exact computer-algebra certification of proof steps

                   (Theorems 7, 8, 9, 11, 16, 17, 20\)

Solver-free block: rows F5 and F6 verify the semidefinite content of Theorems 13 and 14 using

                   numpy eigenvalue decompositions only, with NO semidefinite solver.  They are

                   the evidence that survives in an environment without cvxpy, where F1-F4 are

                   fail-closed (erratum E-M62-19).

Self-reference   : THREE rows have the release package's own apparatus as their subject.

                   M8 recomputes the transport-invariant digest declared in the manifest below,

                   as a fixed point (the declaring line is blanked before hashing), so the

                   manuscript certifies its own identity.  M9 re-runs ALL EIGHT manuscript guards

                   on a synthetically Markdown-escaped copy of this manuscript and requires every

                   verdict to agree and the digest to be unchanged.  Together they close

                   E-M62-18: the guard suite is verified against the transformation that broke the

                   previous delivery, by the guard suite.  M10 is the third and points OUTWARD:

                   it checks the manuscript's claim about a DIFFERENT artifact, the SHA-256 of

                   the running script, which through v1.4.1 no row checked at all (E-M62-23).

Manuscript id    : TRANSPORT-INVARIANT DIGEST, not only a byte hash, and LOCALIZING, not only

                   binary.  The digest is the SHA-256 of the manuscript after Unicode NFKC,

                   removal of zero-width characters, unification of dash variants, iterated

                   undoing of Markdown backslash escapes, and removal of all whitespace.  It is

                   invariant under the transformation that broke the v1.3 delivery.  Since v1.4.1

                   the manuscript additionally carries one digest per PART \--

                     A  title, scope, verification summary, abstract, introduction

                     B  Sections 2-9   : the Z-Spin-free mathematics

                     C  Sections 10-11 : the physical bridge and its numbers

                     D  Sections 12-15 : gates, verification, prior art, audit record

                     E  conclusion, statements, version history, appendices

                   \-- so a mismatch names the part that drifted instead of only announcing that

                   something did.  In particular a release-package patch such as v1.4.1 is

                   verifiable AS a release-package patch: parts B and C must be unchanged.

**PASS row count is not a theorem count.** Every theorem below carries a written proof; the ledger checks numerics, witnesses, guards, regressions and — new in v1.2 — the exact algebra inside several proofs. What is still **not** certified anywhere: the logical structure of the proofs themselves. There is no proof-assistant formalization and no qualified-human proof review. A reader who wants the theorems, rather than their algebra and their numbers, must read Sections 3–10.

---

# 0\. Abstract

Let `R` be an involution of a compact set `Omega`, let `Phi : Omega -> R^N` be **continuous**, and consider

> `A(v) := min { d_TV(mu, R#mu) : mu in P(Omega), integral Phi dmu = v }`.

We prove a *peeling identity*: for every `mu`, `d_TV(mu, R#mu)` equals the least mass that must be removed from `mu` to leave a nonnegative `R`\-invariant measure. It follows that `A(v)` is the threshold at which `v` enters the Minkowski interpolation `A * M + (1-A) * M_sym` of the attainable moment body `M = conv Phi(Omega)` and its symmetric sub-body `M_sym = conv Phi_e(Omega)`; the family is nested, so `A` is a genuine threshold and is convex in `v`. Continuity of `Phi` is not a convenience: with closed convex hulls in place of attainable sets the identity is false, and we exhibit the counterexample. Because both bodies are compact and convex, strong duality holds for every feasible `v` including boundary data, with no interiority hypothesis; the dual is a fractional support-function problem — with an outer truncation at zero that is easy to lose and that we make explicit — equivalently a trigonometric-polynomial programme with contact conditions.

For the truncated Fourier data `(m_1,...,m_n)` on a symmetric arc of half-width `u` we prove a reflection-coupled atomicity bound: some optimizer uses at most `n` oriented and at most `floor(n/2)+1` symmetric orbit atoms, hence at most `n + floor(n/2) + 1` orbit atoms, strictly better than the generic linear-programming bound `2n+1`. We give an exact semidefinite representation on the full circle and, using the localizing Toeplitz condition for an arc, on every arc; both are linear in the asymmetry variable, so no bisection is needed. For `n = 1` we obtain the complete solution on every arc: a three-branch closed form, a two-orbit-atom extremizer, a closed-form dual certificate whose feasibility and complementary slackness we verify algebraically, and the exact gradient. We prove that the hierarchy `A_n` increases to the true asymmetry of the underlying measure, that the problem with the even data unconstrained is exactly the Minkowski gauge of an explicit convex body, and we compute that body in closed form at second order on the circle.

The physical application concerns the seam-odd contraction multiplier `a(c) = E_mu[exp(-2 i c sin phi)]` of the Z-Spin measurement arc. The Jacobi–Anger expansion and its truncation error are not needed: the map `phi -> 2 c sin phi` transports the problem exactly onto the first-order problem on the rescaled arc `Psi = min(2 |c| sin(min(u,pi/2)), pi)`, for either sign of `c`. Hence `lambda` is realizable if and only if `|lambda| <= 1` and `Re lambda >= cos Psi`, and the minimum reflection asymmetry compatible with `a(c) = lambda` is `A_1(Re lambda, |Im lambda|; Psi)` in closed form, attained by an explicit three-atom law. Writing `h` for the density of the oriented part with respect to the orbit measure, we prove the identities `d_TV(mu,R#mu) = integral |h| dsigma` and `D_KL(mu||R#mu) = 2 integral |h| artanh|h| dsigma` for arbitrary measures, which specialize for finite-volume Gibbs boundary laws to `d_TV = < |tanh S_o| >_w` and `D_KL = 2 < S_o tanh S_o >_w`, giving the ceiling `d_TV <= tanh ||S_o||_inf`; the resulting floor `D_KL >= 2 A artanh(A)`, sharper than Pinsker's `2A^2`, is the involution specialization of a known sharp Jeffreys-versus-total-variation bound and is credited as such. For the frozen Z-Spin multiplier this yields, target-blind, `Psi_min = 2.17294837955010601`, `c_min = 1.08647418977505301` for `u >= pi/2`, an unconditional asymmetry price `A* = 0.763362818245963536`, and the requirement `||S_o||_inf >= 1.00422493384939229` on the odd part of any finite-volume effective boundary action.

---

## 0.1 Epistemic status legend

Three independent axes are used and never merged.

**Epistemic axis.** `PROVEN` (complete proof in this paper) · `IMPORTED-PROVEN` (proved elsewhere, used as stated) · `DERIVED` · `DERIVED-CONDITIONAL` · `CERTIFIED` (arbitrary-precision / exact arithmetic enclosure) · `VERIFIED` (numerical reproduction at declared tolerance) · `OBSERVATION` · `HYPOTHESIS` · `NON-CLAIM` · `OPEN`.

**Lifecycle axis.** `CURRENT` · `SUPERSEDED` · `RETRACTED` · `ARCHIVED`.

**Gate axis.** `OPEN` · `CLOSED-PASS` · `CLOSED-NEGATIVE` · `CLOSED-VACUOUS` · `TERMINAL-IN-SCOPE` · `IMPORTED-OPEN`.

Corpus status tokens `[검증됨] / [가설] / [열림]` are used only in the Z-Spin sections and map to `PROVEN or CERTIFIED or VERIFIED` / `DERIVED-CONDITIONAL or HYPOTHESIS` / `OPEN`.

---

# 1\. Introduction

## 1.1 The problem

Fix a compact metric space `Omega`, a homeomorphic involution `R : Omega -> Omega`, and a finite family of **continuous** observables assembled into `Phi : Omega -> R^N` — this is the standing hypothesis `(H-CONT)` of the scope declaration, and Remark 3.3 shows it cannot simply be dropped; Proposition 3.2 records what survives when `Phi` is only assumed bounded and measurable. Write `R#mu` for the pushforward and

d\_TV(P,Q) := sup\_A |P(A) \- Q(A)| \= (1/2) ||P \- Q||\_var        in \[0,1\].

The object of study is the **minimum reflection asymmetry under prescribed linear data**,

A(v) \= min { d\_TV(mu, R\#mu) : mu in P(Omega),  integral Phi dmu \= v }.

The canonical instance is `Omega = Omega_u := {theta : |theta| <= u}` on the circle with `R(theta) = -theta` and `Phi(theta) = (cos theta, ..., cos n theta, sin theta, ..., sin n theta)`, i.e. prescribed truncated Fourier moments `m_k = integral exp(i k theta) dmu`. Write `A_n(m;u)` for that instance.

Two features make the problem non-classical. First, the objective is not a linear functional of `mu` but a distance between `mu` and its own image under a nonlinear (albeit affine-in-`mu`) operation, so it is a *self-involution* extremal problem rather than a standard moment problem. Second, the constraint couples an unsigned object (the symmetric part, seen by the real moments) to a signed object (the oriented part, seen by the imaginary moments) through a pointwise domination that is not itself a moment condition.

## 1.2 Prior state

The predecessor ZS-M61 v1.6 solved one instance of this problem — `n = 1` on a symmetric arc, Theorem M61.20 — by a direct analysis producing a feasibility boundary, an inner/outer branch structure, a two-atom extremizer and a numerically checked dual certificate. It left open (i) whether the two-atom structure was accidental to `n = 1`, (ii) whether strong duality survives at the boundary of the moment cone, (iii) any exact statement for `n >= 2`, and (iv) a physically usable bridge: the reachability of the frozen contraction multiplier `lambda` was addressed through a Jacobi–Anger expansion whose truncation error had to be controlled by a certified Bessel tail.

The design document that preceded this paper proposed to attack (i)–(iv) by building a hierarchy of moment problems together with certified Bessel truncations. The present paper takes a different route and, as a consequence, the hierarchy is *still useful* but the Bessel truncation is *not needed at all* for the physical question.

## 1.3 What is proved here

The organizing observation is elementary and is stated as Theorem 2:

> **the reflection asymmetry of a state equals the smallest fraction of that state that has to be removed in order to leave a perfectly symmetric state.**

Everything else follows from taking this seriously. Removing mass `A` and leaving a symmetric remainder means the data `v` splits as `A p + (1-A) q` with `p` an arbitrary moment point and `q` a symmetric moment point; minimizing `A` is therefore a **threshold problem for a nested family of Minkowski interpolations of two fixed compact convex bodies** (Theorem 3). Compactness and convexity are all that is needed for exact duality (Theorem 6), the contact geometry of the dual polynomials produces a sharp atom count (Theorem 5), Carathéodory–Toeplitz produces an exact semidefinite form (Theorems 13–14), and the classification of the exposed faces of a two-dimensional lens produces the complete first-order solution (Theorems 7–11).

## 1.4 Contribution table

| \# | Result | New here? | Status | Main assumptions | Evidence | External baseline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Lem. 1 | orbit dictionary `mu <-> (sigma, delta)` | folklore-level | PROVEN | `Omega` compact, `R`\-invariant | proof §3.1 | standard |
| Thm 2 | peeling identity | **IMPORTED CORE \+ SPECIALIZED** | PROVEN | none beyond Lem. 1 | two proofs §3.2; row **N8** | two lines from the overlapping-coefficient identity `d_TV = 1 - int(p^q)`; cf. the trimming/contamination line |
| Thm 3 | oriented-mass reduction (master theorem) | OPEN-NOVELTY | PROVEN | **`Phi` continuous** (H-CONT); Prop. 3.2 covers bounded measurable with attainable sets | proof §4.1; rows B1, B3, **N1** | not located |
| Cor. 4 | nesting, convexity, attainment | — | PROVEN | Thm 3 | proof §4.2; row B3 | standard once Thm 3 holds |
| Thm 5 | atom bound `n + floor(n/2) + 1` | OPEN-NOVELTY | PROVEN under Def. 5.2 non-degeneracy | arc support | proof §6; rows D1–D3 | strictly stronger than generic `2n+1` |
| Thm 6 | strong duality with no interiority hypothesis; corrected fractional dual (5.1) | EXTENDED | PROVEN | compactness only | proof §5.1; rows C3, **N2** | strengthens measure-LP duality |
| Thm 7 | closed-form dual certificate, `n = 1` | OPEN-NOVELTY | PROVEN | arc support | proof §5.3; rows C1, C2, C4 | replaces ZS-M61 numerical certificate |
| Thm 8 | exact `n = 1` closed form on every arc | EXTENDED (of M61.20) | PROVEN | arc support | proof §8.2; rows E1–E3 | generalizes ZS-M61 Thm M61.20 |
| Thm 9 | constructive two-atom extremizer | EXTENDED | PROVEN | arc support | proof §8.1; rows E4, E5 | derives the M61.20 structure |
| Cor. 10 | recovery of ZS-M61 Thm M61.20 | — | DERIVED | — | §8.4 | internal |
| Thm 11 | exact gradient / condition number | OPEN-NOVELTY | PROVEN | non-degenerate branch | proof §8.5; row E6 | — |
| Thm 12 | monotone hierarchy converging to `d_TV` | EXTENDED | PROVEN | compact support only | proof §9.1; rows B4, H1, H2 | removes a determinacy hypothesis |
| Thm 13 | exact circle SDP, linear in `A` | SPECIALIZED | PROVEN | Carathéodory–Toeplitz (IMPORTED) | proof §7.1; rows F1, F2 | new wrapper on classical result |
| Thm 14 | exact arc SDP via localizing Toeplitz | SPECIALIZED | DERIVED-CONDITIONAL on the imported arc representation | arc K-moment theorem (IMPORTED) | §7.2; rows F3, F4 | new wrapper on classical result |
| Thm 15 | odd-data-only problem is a gauge | OPEN-NOVELTY | PROVEN | — | proof §9.2; row G1 | sharpens a naive dual bound |
| Thm 16 | `Y_2(pi)` in closed form | OPEN-NOVELTY | PROVEN | — | proof §9.3; rows G2–G4 | — |
| Thm 17 | multiplier asymmetry price; reachability criterion | OPEN-NOVELTY | PROVEN | field-side phase law only | proof §10.2; rows I1, I2 | supersedes the Bessel-truncation route |
| Thm 18 | explicit three-atom extremal boundary law | OPEN-NOVELTY | PROVEN | as Thm 17; **orientation sign depends on sign(c)** | proof §10.3; rows I3, **N3** | — |
| Thm 19 | Gibbs asymmetry identity and ceiling | likely known in some form | PROVEN | finite-volume Gibbs law | proof §10.5; rows J1, J2 | sweep pending |
| Thm 20 | orbit identity \`D\_KL \= 2 int | h | artanh | h | dsigma\` (general) | OPEN-NOVELTY |
| Cor. 20.1 | floor `D_KL >= 2A artanh A` | **IMPORTED / SPECIALIZED** | IMPORTED-PROVEN | none | §10.6; rows J4, N5, **N6** | Gilardoni; Sason–Verdu — involution specialization |
| Cor. 20.2 | Gibbs forms of the two identities | EXTENDED | PROVEN | finite-volume Gibbs law | proof §10.6; rows J1, J3 | sweep pending |

Novelty classes marked `OPEN-NOVELTY` mean the systematic prior-art sweep (debt `D-M62-PRIOR`) has **not** been completed. No claim of priority is made anywhere in this paper.

## 1.5 Non-claims

Collected in §11.2 as `NC-M62.1` … `NC-M62.6`. In brief: nothing here selects a physical state, nothing here identifies the abstract Z-register parity basis with `(Re Phi, Im Phi)`, nothing here promotes a mathematical divergence to a physical entropy production, and the finite-volume Gibbs results are not claimed for infinite-volume spontaneously selected states.

---

# 2\. Setting, conventions, and dependency freeze

## 2.1 Convention lock

Throughout,

d\_TV(P,Q) := sup\_A |P(A) \- Q(A)| \= (1/2) ||P \- Q||\_var ,        0 \<= d\_TV \<= 1\.

A different total-variation convention rescales every displayed quantity by a fixed factor; the convention above is used in the statements, the proofs, and the verification artifact without exception (ledger row A1 checks the two forms agree numerically; row A2 checks the range).

`P(Omega)` denotes Borel probability measures on `Omega`; `M(Omega)` the finite signed Borel measures; `||.||_var` the total variation norm; `conv` the convex hull, `cl conv` its closure.

## 2.2 Geometry

`S^1 = R / 2 pi Z`. For `0 < u <= pi`,

Omega\_u := { theta in S^1 : |theta| \<= u },     R(theta) := \-theta,

so `R` is an involution of `Omega_u` with fixed-point set `{0}` (and `{0, pi}` when `u = pi`). A reflection about a general axis `alpha` is conjugate to this one by the rotation `theta -> theta - alpha`; every statement below is therefore `alpha`\-covariant and no choice of axis is made.

Truncated Fourier data:

m\_k := integral exp(i k theta) dmu(theta) ,   x\_k := Re m\_k ,   y\_k := Im m\_k ,   k \= 1..n,

c(t) := (cos t, ..., cos n t) ,   s(t) := (sin t, ..., sin n t).

Write

A\_n(m; u) := min { d\_TV(mu, R\#mu) : mu in P(Omega\_u),  integral exp(i k theta) dmu \= m\_k , k \= 1..n }.

## 2.3 Dependency freeze

corpus\_as\_of        : 2026-08-19 KST

paper\_code/version  : ZS-M62 v1.4.2

active upstream     : ZS-M61 v1.6 (Thms M61.20, M61.22', M61.23', M61.24)

                      ZS-S14 v2.1 (typed master action; boundary law OPEN)

                      ZS-M1      (i-tetration map, multiplier lambda)

                      ZS-F1      (Z-bias field Phi \= rho exp(i theta); rho seam-even)

                      ZS-M56 v1.8, ZS-M57 v1.8, ZS-M59 v1.8, ZS-M60 v1.5

locked constants    : A \= 35/437 , Q \= 11 , dim(Z) \= 2   (not used in Sections 2-9)

                      z\* \= 0.4382829367270321116269752 \+ 0.3605924718713854859529405 i

                      lambda \= (i pi/2) z\*

open gates relevant : D-M61-IOTA , D-M61-GOLD , D-M61-WARD , M56.7 identifiability trap

retracted inputs checked : the signed seam-odd scalar of ZS-M61 v1.0-v1.3 (retyped in M61.22');

                      ZS-S14 v2.0 field identifications (superseded by v2.1); neither is used here.

verification artifact : zs\_m62\_verify\_v1\_4\_2.py  (91 rows, 0 FAIL)

Sections 2–9 use **none** of the Z-Spin inputs above; they are listed because Section 10 does.

---

# 3\. The orbit dictionary and the peeling identity

## 3.1 Lemma 1 (orbit dictionary)

**Lemma 1\.** `PROVEN`. Let `mu in P(Omega_u)`. Define measures on the orbit space `[0,u]` by

sigma(E) := mu(E) \+ mu(-E)     for Borel E subset (0,u\],      sigma({0}) := mu({0}),

delta(E) := mu(E) \- mu(-E)     for Borel E subset (0,u\],      delta({0}) := 0,

(with the analogous convention at `theta = pi` when `u = pi`, that point being `R`\-fixed). Then `mu -> (sigma, delta)` is a bijection onto

D\_u := { (sigma, delta) : sigma in P(\[0,u\]),  delta in M(\[0,u\]),  |delta| \<= sigma,

         delta({0}) \= 0  (and delta({pi}) \= 0 if u \= pi) },

and for every bounded Borel `F` on `Omega_u`, with `F_e(theta) = (F(theta)+F(-theta))/2` and `F_o(theta) = (F(theta)-F(-theta))/2`,

integral\_{Omega\_u} F dmu \= integral\_0^u F\_e dsigma \+ integral\_0^u F\_o ddelta,          (3.1)

d\_TV(mu, R\#mu) \= ||delta||\_var.                                                        (3.2)

In particular `Re m_k = integral_0^u cos(kt) dsigma` and `Im m_k = integral_0^u sin(kt) ddelta`.

**Proof.** The inverse map sends `(sigma, delta)` to the measure whose restriction to `(0,u]` is `(sigma+delta)/2`, whose restriction to `[-u,0)` is the reflection of `(sigma-delta)/2`, and which puts `sigma({0})` at `0` (and `sigma({pi})` at `pi`). Nonnegativity of both halves is exactly `|delta| <= sigma`; total mass is `sigma([0,u]) = 1`. The two maps are mutually inverse by construction. Formula (3.1) is the decomposition of `F` into even and odd parts followed by the definitions of `sigma` and `delta`; the odd part integrates against `delta` and is insensitive to the `R`\-fixed atoms because `F_o` vanishes there. For (3.2), the signed measure `mu - R#mu` restricted to `(0,u]` is `delta`, its restriction to `[-u,0)` is the reflection of `-delta`, and it has no mass at the fixed points; hence `||mu - R#mu||_var = 2 ||delta||_var`, and the convention of §2.1 gives `d_TV = ||delta||_var`. `QED`

Ledger: row A6 records that Lemma 1 is a restatement of definitions and is therefore a control, not evidence.

## 3.2 Theorem 2 (peeling identity)

**Theorem 2\.** `PROVEN`. Let `Omega` be compact, `R` an involution of `Omega`, `mu in P(Omega)`. Then

d\_TV(mu, R\#mu) \= min { tau(Omega) : tau in M(Omega),  0 \<= tau \<= mu,  R\#(mu \- tau) \= mu \- tau }.   (3.3)

The minimum is attained; on `Omega_u` the minimizer is unique and equals the measure with orbit data `(|delta|, delta)`.

**Proof.** It suffices to prove it on `Omega_u` and then transport, since the general case follows verbatim by replacing the orbit space `[0,u]` with the quotient `Omega / R` and Lemma 1 with its evident analogue (the fixed-point set carries no `delta`).

Let `tau` be admissible and let `(sigma_tau, delta_tau)` be its orbit data (Lemma 1 applies to nonnegative measures of arbitrary mass after normalization; we use the same formulas). Since `mu - tau >= 0` and `R#(mu-tau) = mu-tau`, the orbit datum `delta_{mu-tau}` vanishes; by linearity of `delta` in the measure, `delta_tau = delta_mu`. Since `tau >= 0`, Lemma 1 forces `|delta_tau| <= sigma_tau`, hence

tau(Omega\_u) \= sigma\_tau(\[0,u\]) \>= || delta\_tau ||\_var \= || delta\_mu ||\_var \= d\_TV(mu, R\#mu),

the last equality by (3.2). Conversely take `sigma_tau := |delta_mu|` and `delta_tau := delta_mu`; then `|delta_tau| <= sigma_tau` holds with equality, so this pair defines a nonnegative measure `tau` of mass `||delta_mu||_var`, and `tau <= mu` because `sigma_tau = |delta_mu| <= sigma_mu` and the two halves of `tau` are dominated by the corresponding halves of `mu`. Finally `mu - tau` has vanishing `delta`, i.e. is `R`\-invariant. Uniqueness: any minimizer must satisfy `delta_tau = delta_mu` and `sigma_tau([0,u]) = ||delta_mu||_var` together with `sigma_tau >= |delta_tau| = |delta_mu|`, which forces `sigma_tau = |delta_mu|`. `QED`

**Second proof (via the overlapping coefficient).** `PROVEN`. Recall the classical identity, for probability measures `P, Q` with densities `p, q` against any common dominating measure,

d\_TV(P,Q) \= 1 \- integral (p ^ q) ,                                                         (3.4)

so that `P ^ Q` is the largest common sub-measure of `P` and `Q`, of mass `1 - d_TV(P,Q)`. Apply this with `Q = R#mu`. Because `R` is an involution and the lattice operation commutes with pushforward,

R\#( mu ^ R\#mu ) \= R\#mu ^ R\#R\#mu \= R\#mu ^ mu \= mu ^ R\#mu ,

so the maximal common sub-measure is automatically `R`\-invariant. Hence `tau* := mu - (mu ^ R#mu)` is nonnegative, has mass `d_TV(mu, R#mu)` by (3.4), and leaves an `R`\-invariant remainder; and no admissible `tau` can be lighter, since `mu - tau` being `R`\-invariant and `<= mu` forces `mu - tau <= mu ^ R#mu`. In orbit coordinates `tau* = (mu - R#mu)^+`, which is the measure with data `(|delta|, delta)` produced by the orbit argument above. `QED`

**Remark 2.3 (erratum `E-M62-14`; novelty status).** The second proof shows that Theorem 2 is **two lines** from the overlapping-coefficient identity (3.4), which is classical. Its novelty class is therefore **`IMPORTED CORE + SPECIALIZED`**, not `OPEN-NOVELTY`: what is contributed is the observation that the maximal common sub-measure of `mu` and `R#mu` is automatically `R`\-invariant — hence the *symmetric* remainder is free — together with the use of that observation as the reduction engine of Theorem 3\. The third audit further points to the trimming / contamination literature, where the equivalence between a total-variation bound and the existence of a common trimmed core is developed systematically (P. C. Álvarez-Esteban, E. del Barrio, J. A. Cuesta-Albertos, C. Matrán, *Similarity of samples and trimming*, Bernoulli **18** (2012) 606–634, arXiv:1205.1950). **Verification status of that pointer:** the paper's exact theorem statement has *not* been read at source in the preparation of this version, so it is recorded as a locator, not as an entailment; the retyping above does not depend on it, resting instead on (3.4), which is verified directly (ledger row `N8`). Closing the pointer is part of `D-M62-PRIOR`.

**Remark 2.1.** Identity (3.3) is where the entire paper comes from. It replaces a distance between two measures by a **mass**, and a signed-measure optimization by a decomposition of `mu` into "a part that may be anything" plus "a part that is symmetric". The three-copy linear programme over `(c, e_+, e_-)` used in earlier treatments is precisely the coordinate expression of (3.3) in the orbit chart of Lemma 1\.

**Remark 2.2 (interpretation).** `d_TV(mu, R#mu) = A` says exactly: a fraction `A` of the probability mass is *oriented*, and the complementary fraction `1 - A` can be arranged to be perfectly reflection-symmetric. "Asymmetry" is therefore literally a mass fraction, not an abstract distance.

---

# 4\. The oriented-mass reduction

## 4.1 Theorem 3 (master theorem)

**Definition 4.1.** For `Phi : Omega -> R^N` put `Phi_e(w) := (Phi(w) + Phi(R w))/2` and define the **attainable moment sets**

M\_Phi     := { integral Phi dpi   : pi in P(Omega) } ,

M\_Phi^sym := { integral Phi dpi   : pi in P(Omega),  R\#pi \= pi }

           \= { integral Phi\_e dpi : pi in P(Omega) }  subset M\_Phi .

**Lemma 4.2 (barycentre identification).** `PROVEN`. For bounded `Phi`, `M_Phi = conv Phi(Omega)` and `M_Phi^sym = conv Phi_e(Omega)`. If in addition `Phi` is continuous and `Omega` is compact, both sets are **compact**, and `conv = cl conv`.

*Proof.* `conv Phi(Omega) subset M_Phi` because finitely supported measures are admissible. Conversely let `b = integral Phi dpi` and suppose `b notin conv Phi(Omega)`; separate: there is `w` with `<w,b> >= sup_{S} <w,.>` where `S := Phi(Omega)`. Since `<w,b> = integral <w,Phi> dpi <= sup_S <w,.>`, equality holds, forcing `<w,Phi> = sup_S <w,.>` `pi`\-a.e.; so `pi` is carried by the exposed face `S_w`, and one recurses on the lower-dimensional set `conv S_w`. The recursion terminates, giving `b in conv S`. If `Phi` is continuous and `Omega` compact then `S = Phi(Omega)` is compact, and the convex hull of a compact subset of `R^N` is compact by Carathéodory. `QED`

**Remark 3.3 (why continuity is needed — a counterexample to the closed-hull form).** `PROVEN`. Let `Omega = {0} u {1/n : n >= 1}` with the topology induced from `R` (compact), `R = identity`, `N = 1`, and

Phi(0) := 1 ,      Phi(1/n) := 1/n .

`Phi` is bounded and Borel but discontinuous at `0`. Here `Phi(Omega) = {1} u {1/n}`, so `conv Phi(Omega) = (0,1]` while `cl conv Phi(Omega) = [0,1]`. Since `R` is the identity every measure is `R`\-invariant and `d_TV(mu,R#mu) = 0`, so the left-hand side of (4.1) equals `0` for attainable `v` and `+infinity` otherwise. At `v = 0` the left-hand side is `+infinity` — no probability measure on `Omega` has barycentre `0`, because `integral Phi dpi >= inf Phi > 0` on every finite truncation and `Phi > 0` everywhere. But `0 in cl conv Phi(Omega)`, so the version of (4.1) written with **closed** hulls would return `0`. Hence the closed-hull form of the master theorem is false for bounded measurable `Phi`; the correct general statement uses the attainable sets of Definition 4.1, and continuity restores compactness and attainment. (Ledger row `N1`.)

**Theorem 3\.** `PROVEN` under (H-CONT). Let `Omega` be compact, `R` a continuous involution, and `Phi : Omega -> R^N` **continuous**. Then for every `v in R^N`,

min { d\_TV(mu, R\#mu) : mu in P(Omega),  integral Phi dmu \= v }

   \= min { A in \[0,1\] : v in A \* M\_Phi \+ (1-A) \* M\_Phi^sym } ,                        (4.1)

with the convention `min emptyset = +infinity` on both sides. Moreover:

(i) `K(A) := A * M_Phi + (1-A) * M_Phi^sym` is compact and convex for each `A`; (ii) `K(A') subset K(A)` whenever `A' <= A` (nesting), so the right-hand side is a genuine threshold; (iii) the minimum on the left is attained whenever it is finite.

**Proposition 3.2 (general bounded measurable case).** `PROVEN`. If `Phi` is only bounded and measurable, identity (4.1) still holds verbatim with `M_Phi`, `M_Phi^sym` the **attainable** sets of Definition 4.1 (equivalently `conv Phi(Omega)`, `conv Phi_e(Omega)`, *not* their closures), and with `min` replaced by `inf` on both sides. Nesting (ii) is unchanged. Compactness and attainment may fail, as Remark 3.3 shows.

**Proof.**

*Upper bound (`<=` of the left side by the right side).* Suppose `v = A p + (1-A) q` with `p in M_Phi`, `q in M_Phi^sym`. Choose `pi_1 in P(Omega)` with `integral Phi dpi_1 = p`; this is possible by Definition 4.1, since `M_Phi` *is* the attainable set, and by Lemma 4.2 it equals `conv Phi(Omega)`, which under (H-CONT) is compact. Choose `pi_2 in P(Omega)` with `integral Phi_e dpi_2 = q` and set `pi_2^s := (pi_2 + R#pi_2)/2`, which is `R`\-invariant and satisfies `integral Phi dpi_2^s = integral Phi_e dpi_2 = q`. Put

mu := A pi\_1 \+ (1-A) pi\_2^s .

Then `mu in P(Omega)` and `integral Phi dmu = A p + (1-A) q = v`. Since `mu - A pi_1 = (1-A) pi_2^s` is nonnegative and `R`\-invariant, Theorem 2 gives `d_TV(mu, R#mu) <= A pi_1(Omega) = A`.

*Lower bound.* Let `mu` be feasible and `A := d_TV(mu, R#mu)`. By Theorem 2 there is `tau` with `0 <= tau <= mu`, `tau(Omega) = A`, and `pi := mu - tau` nonnegative, `R`\-invariant, of mass `1-A`. If `0 < A < 1`, then `p := A^{-1} integral Phi dtau in M_Phi` and `q := (1-A)^{-1} integral Phi dpi = (1-A)^{-1} integral Phi_e dpi in M_Phi^sym` (the second equality because `pi` is `R`\-invariant, so `integral (Phi - Phi_e) dpi = 0`). Hence `v = A p + (1-A) q in K(A)`. The degenerate cases `A = 0` and `A = 1` are immediate.

*(i)* Under (H-CONT), Lemma 4.2 makes both bodies compact convex; a Minkowski combination of compact convex sets is compact convex. Without continuity this step, and only this step, fails, which is exactly the content of Remark 3.3.

*(ii)* `M_Phi^sym subset M_Phi` because `Phi_e(w) = (Phi(w) + Phi(Rw))/2 in conv Phi(Omega)`. Hence for `A' <= A`,

K(A') \= A' M\_Phi \+ (A \- A') M\_Phi^sym \+ (1-A) M\_Phi^sym

      subset A' M\_Phi \+ (A \- A') M\_Phi \+ (1-A) M\_Phi^sym \= K(A),

using convexity of `M_Phi` in the last step (`a M + b M = (a+b) M` for convex `M` and `a,b >= 0`).

*(iii)* By (i) and (ii) the set `{ A : v in K(A) }` is a closed subinterval of `[0,1]` of the form `[A*, 1]` or empty; the construction in the upper-bound step realizes `A*`. `QED`

**Corollary 3.1 (Fourier specialization).** With `Omega = Omega_u` and `Phi = (c, s)`,

A\_n(m;u) \= min { A : (x, y) in A \* C\_n^pm(u) \+ (1-A) \* C\_n^0(u) } ,

C\_n^pm(u) := conv { (c(t), eps s(t)) : t in \[0,u\], eps \= \+-1 } ,

C\_n^0(u)  := conv { (c(t), 0\) : t in \[0,u\] } .

Indeed `Phi(theta) = (c(theta), s(theta))` and `Phi_e(theta) = (c(theta), 0)`, while `Phi(Omega_u) = {(c(t), eps s(t))}` because `c` is even and `s` is odd.

**Verification.** Row B1 (class R) compares three *independent* implementations at `n = 1, 2, 3`: a raw total-variation linear programme over `mu` on a symmetric grid with auxiliary variables and no orbit reduction; the three-copy orbit programme; and the oriented-mass programme of Corollary 3.1. Maximum pairwise deviation over 24 instances: `1.20e-13` at grid `N = 200`.

## 4.2 Corollary 4 (nesting, convexity, attainment)

**Corollary 4\.** `PROVEN`. The function `v -> A(v)` defined by (4.1) is convex on its (convex) domain, lower semicontinuous, and attained.

**Proof.** Convexity: let `v_1 in K(A_1)`, `v_2 in K(A_2)`, `lam in [0,1]`, and put `A := lam A_1 + (1-lam) A_2`. Then

lam v\_1 \+ (1-lam) v\_2  in  lam K(A\_1) \+ (1-lam) K(A\_2)

   \= (lam A\_1 \+ (1-lam) A\_2) M\_Phi \+ (lam(1-A\_1) \+ (1-lam)(1-A\_2)) M\_Phi^sym \= K(A),

using `a M + b M = (a+b) M` for the convex bodies. Hence `A(lam v_1 + (1-lam) v_2) <= A`. Lower semicontinuity and attainment follow from compactness of `K(A)` and the nesting of Theorem 3(ii). `QED`

Ledger row B3 checks convexity on 60 random convex combinations at `n = 1` (0 violations); rows B2 and B4 check nesting and hierarchy monotonicity.

---

# 5\. Duality

## 5.1 Theorem 6 (strong duality, no interiority hypothesis)

For a compact convex `K subset R^N` let `h_K(w) := max_{p in K} <w, p>` be its support function.

**Theorem 6\.** `PROVEN`. For every `v` and every `A in [0,1]`,

v in K(A)   \<=\>   \<w, v\> \<= A h\_{M\_Phi}(w) \+ (1-A) h\_{M\_Phi^sym}(w)   for all w in R^N .

Consequently, writing `D := { w : h_{M_Phi}(w) > h_{M_Phi^sym}(w) }`, the datum `v` is feasible (i.e. `v in K(1)`) if and only if

\<w,v\> \<= h\_{M\_Phi}(w)   for all w notin D ,                                                (5.0)

and in that case

A(v) \= max { 0 ,  sup\_{w in D}  \[ \<w,v\> \- h\_{M\_Phi^sym}(w) \] / \[ h\_{M\_Phi}(w) \- h\_{M\_Phi^sym}(w) \] } .   (5.1)

The right-hand side equals the minimum in (4.1): **the duality gap is zero for every feasible `v`, including data on the boundary of the moment cone, with no Slater or interiority condition.**

**Proof.** `K(A)` is compact and convex (Theorem 3(i)), and its support function is `h_{K(A)} = A h_{M_Phi} + (1-A) h_{M_Phi^sym}` because support functions are additive under Minkowski sums and positively homogeneous. The bidual (Hahn–Banach separation for a compact convex set) gives the stated equivalence. For (5.1): for `w notin D` one has `h_{M_Phi}(w) = h_{M_Phi^sym}(w)` (the inequality `>=` always holds since `M_Phi^sym subset M_Phi`), so the constraint reads `<w,v> <= h_{M_Phi}(w)` independently of `A`; that is condition (5.0). For `w in D` the constraint is equivalent to `A >= [ <w,v> - h_{M_Phi^sym}(w) ] / [ h_{M_Phi}(w) - h_{M_Phi^sym}(w) ]`. The admissible set of `A` is therefore the intersection of `[0,1]` with a half-line, and its left endpoint is the **maximum of `0` and the supremum of the ratios**. Omitting the outer `max{0,.}` is a genuine error: see Remark 6.2. `QED`

**Remark 6.2 (the outer maximum is not decorative).** `PROVEN`. Let `Omega = {a,b,c}`, let `R` swap `a` and `b` and fix `c`, and let `N = 1` with

Phi(a) \= \-1 ,   Phi(b) \= 1 ,   Phi(c) \= 1 ,        so   Phi\_e(a) \= Phi\_e(b) \= 0 ,  Phi\_e(c) \= 1 ,

M\_Phi \= \[-1,1\] ,   M\_Phi^sym \= \[0,1\] .

Take `v = 1/2`. The `R`\-invariant measure `mu = (1/4) delta_a + (1/4) delta_b + (1/2) delta_c` has `integral Phi dmu = 1/2` and `d_TV(mu, R#mu) = 0`, so `A(v) = 0`. Here `h_{M_Phi}(w) = |w|` and `h_{M_Phi^sym}(w) = max(0,w)`, so `D = {w < 0}` and for every `w < 0` the ratio equals `(w/2 - 0)/(-w - 0) = -1/2`. The uncorrected right-hand side of (5.1) therefore returns `-1/2`, which is not even a total-variation distance. With the outer maximum it returns `0`, the correct value. (Ledger row `N2`.)

**Remark 6.3 (what survives).** The trigonometric programme (5.3) below is unaffected, because it optimizes over an affine family that always contains the zero certificate `(a_0,a,b) = (0,0,0)` of value `0`; consequently every downstream first-order computation of Sections 5.3 and 8 is unchanged. The defect was confined to the abstract fractional form.

**Remark 6.1.** This is where the present formulation pays off. In the signed-measure formulation the dual is an infinite-dimensional conic programme and strong duality needs a Slater point, which fails exactly on the boundary of the moment cone — precisely the interesting stratum. Here the primal has already been reduced to membership in a compact convex subset of `R^N`, and separation is unconditional.

## 5.2 The trigonometric-polynomial form

For `Omega_u` and truncated Fourier data, write `w = (a_1..a_n, b_1..b_n)` and

C\_a(t) := sum\_{k=1}^n a\_k cos(k t) ,      S\_b(t) := sum\_{k=1}^n b\_k sin(k t).

Then `h_{C_n^pm(u)}(w) = max_{[0,u]} ( C_a + |S_b| )` and `h_{C_n^0(u)}(w) = max_{[0,u]} C_a`, so (5.1) reads

A\_n(m;u) \= sup\_{a,b} \[ \<a,x\> \+ \<b,y\> \- max\_{\[0,u\]} C\_a \] / \[ max\_{\[0,u\]} (C\_a \+ |S\_b|) \- max\_{\[0,u\]} C\_a \].  (5.2)

Absorbing the normalization into a constant term `a_0` and writing `C := a_0 + C_a`, `S := S_b`, (5.2) is equivalent to the linear programme

maximise    a\_0 \+ \<a,x\> \+ \<b,y\>

subject to  C(t) \<= 0        and      C(t) \+ |S(t)| \<= 1        for all t in \[0,u\].        (5.3)

**Complementary slackness.** If `(sigma, delta)` is primal-optimal with oriented part `tau` (Theorem 2\) and symmetric remainder `pi`, and `(a_0,a,b)` is dual-optimal, then

supp(pi\_orbit)      subset { t in \[0,u\] : C(t) \= 0 } ,

supp(tau\_orbit^+)   subset { t : C(t) \+ S(t) \= 1 } ,

supp(tau\_orbit^-)   subset { t : C(t) \- S(t) \= 1 } ,                                      (5.4)

where `tau^+` and `tau^-` are the positively and negatively oriented parts. Indeed the duality gap equals `integral (-2C) d(pi/2) + integral (1 - C - S) dtau^+ + integral (1 - C + S) dtau^-`, a sum of three nonnegative terms.

A contact point cannot carry both orientations: `C + S = 1` and `C - S = 1` force `S = 0` and `C = 1 > 0`, contradicting `C <= 0`.

## 5.3 Theorem 7 (closed-form dual certificate at `n = 1`)

At `n = 1` the dual data are three numbers `(a_0, a_1, b_1)`. We exhibit them in closed form and prove feasibility and complementary slackness algebraically, so that any reader can certify a value of `A_1` by hand.

**Theorem 7\.** `PROVEN`. Let `0 < u <= pi`, `x >= cos u`, `y > 0`, `x^2 + y^2 <= 1`. Let `gamma in {1, cos u}` be a *reservoir position*, let `t_1 in (0, pi)` satisfy

A cos t\_1 \+ (1-A) gamma \= x ,        A sin t\_1 \= y ,                                       (5.5)

for some `A in (0,1]`, and set

kappa := 1 / (1 \- gamma cos t\_1) ,   a\_1 := kappa cos t\_1 ,   b\_1 := kappa sin t\_1 ,

a\_0 := A \- a\_1 x \- b\_1 y .                                                                 (5.6)

Then, with `C(t) = a_0 + a_1 cos t` and `S(t) = b_1 sin t`,

C(t) \+ S(t) \= a\_0 \+ kappa cos(t \- t\_1) ,                                                   (5.7)

C(t\_1) \+ |S(t\_1)| \= 1 ,        C(t\_gamma) \= 0     where cos t\_gamma \= gamma,               (5.8)

and the dual objective equals `A`. If in addition

* `gamma = 1` and `t_1 < pi/2`, or  
* `gamma = cos u < 0` and `t_1 > pi/2`,

then `C <= 0` and `C + |S| <= 1` on `[0,u]` provided `t_1 <= u`, i.e. `(a_0,a_1,b_1)` is dual-feasible and certifies `A_1(x,y;u) = A`.

Separately, `(a_0,a_1,b_1) = (0, 0, 1/s_1(u))` with `s_1(u) := sin(min(u,pi/2))` is always dual-feasible and certifies the value `y / s_1(u)`.

**Proof.** From (5.5), `kappa > 0` because `gamma cos t_1 < 1` in both admissible cases. Identity (5.7): `a_1 cos t + b_1 sin t = kappa (cos t_1 cos t + sin t_1 sin t) = kappa cos(t - t_1)`, and on `[0,u] subset [0,pi]` we have `sin t >= 0` and `b_1 > 0`, so `|S| = S`.

Dual objective: `a_0 + a_1 x + b_1 y = A` by the definition of `a_0`.

First identity of (5.8). Using `x = A cos t_1 + (1-A) gamma` and `y = A sin t_1`,

a\_1 x \+ b\_1 y \= kappa ( x cos t\_1 \+ y sin t\_1 )

              \= kappa ( A cos^2 t\_1 \+ (1-A) gamma cos t\_1 \+ A sin^2 t\_1 )

              \= kappa ( A \+ (1-A) gamma cos t\_1 ),

hence

C(t\_1) \+ S(t\_1) \= a\_0 \+ kappa \= A \- kappa( A \+ (1-A) gamma cos t\_1 ) \+ kappa

                \= A \+ kappa (1-A) ( 1 \- gamma cos t\_1 ) \= A \+ (1-A) \= 1 .

Second identity of (5.8). With `cos t_gamma = gamma`,

C(t\_gamma) \= a\_0 \+ a\_1 gamma \= A \- kappa ( A \+ (1-A) gamma cos t\_1 ) \+ kappa gamma cos t\_1

           \= A \- kappa ( A \- A gamma cos t\_1 ) \= A \- kappa A (1 \- gamma cos t\_1) \= A \- A \= 0 .

Feasibility. `C(t) = a_0 + a_1 cos t` is affine in `cos t` and vanishes at `cos t = gamma`. If `gamma = 1` and `a_1 > 0`, then `C(t) = a_1 (cos t - 1) <= 0` on all of `[0,pi]`; and `a_1 > 0 <=> cos t_1 > 0 <=> t_1 < pi/2`. If `gamma = cos u < 0` and `a_1 < 0`, then `C(t) = a_1 (cos t - cos u) <= 0` for `t <= u` because `cos t >= cos u` there; and `a_1 < 0 <=> cos t_1 < 0 <=> t_1 > pi/2` (recall `kappa > 0`). By (5.7), `max_{[0,u]} (C + |S|) = a_0 + kappa max_{[0,u]} cos(t - t_1) = a_0 + kappa = 1` provided `t_1 in [0,u]`.

The harmonic certificate: `C == 0 <= 0`, and `C + |S| = sin t / s_1(u) <= 1` on `[0,u]` by the definition of `s_1(u)`, with equality at `t = min(u, pi/2)`. Its objective is `b_1 y = y/s_1(u)`. `QED`

**Verification.** Rows C1 and C2 evaluate the closed-form triple on 4000 random feasible `(x,y,u)`: zero constraint violations (max violation `2.9e-11`, attributable to floating point) and maximum `|dual value - A_1|` equal to `8.1e-13`. Row C3 compares against a grid linear programme at `N = 4000` on five reference instances (max gap `< 5e-6`, i.e. grid scale). Row C4 exhibits complementary slackness numerically: `C(t_0) = 0` and `C(t_1) + |S(t_1)| = 1` to `1e-8` on three instances of different branches.

---

# 6\. Sharp atomicity

## 6.1 Statement

**Definition 6.1 (orbit atoms).** An *orbit atom* of `mu in P(Omega_u)` is an atom of its orbit measure `sigma` (Lemma 1). An orbit atom at `t in (0,u)` corresponds to at most two atoms of `mu`, at `+t` and `-t`.

**Definition 6.2 (dual non-degeneracy).** A dual optimum `(a_0, a, b)` of (5.3) is *non-degenerate* if `C notequiv 0` on `[0,u]` and `F := (1 - C)^2 - S^2 notequiv 0` on `[-u,u]`.

**Theorem 5\.** `PROVEN under Definition 6.2`. Let `n >= 1`, `0 < u <= pi`, and let `m` be feasible. If some dual optimum is non-degenerate, then there is a primal optimum whose orbit support consists of

* at most `n` **oriented** orbit atoms, and  
* at most `floor(n/2) + 1` **symmetric** orbit atoms,

hence at most

n \+ floor(n/2) \+ 1                                                                        (6.1)

orbit atoms in total, and at most `2 (n + floor(n/2) + 1)` atoms of `mu` on `Omega_u`. Without the non-degeneracy hypothesis the generic linear-programming bound `2n + 1` orbit atoms holds.

For `n = 1, 2, 3` the bound (6.1) reads `2, 4, 5`, against the generic `3, 5, 7`.

## 6.2 Proof

By (5.4) the symmetric mass lives on `{C = 0}` and the oriented mass on `{C + |S| = 1}`.

*Symmetric atoms.* `C(t) = a_0 + sum_{k=1}^n a_k cos(k t)` is a cosine polynomial of degree `n`, hence `C(t) = P(cos t)` for a real algebraic polynomial `P` of degree at most `n`. The constraint is `P <= 0` on `I := [cos u, 1]`. Zeros of `P` interior to `I` are local maxima of a nonpositive function and therefore have even multiplicity, i.e. multiplicity at least `2`; zeros at the two endpoints of `I` may be simple. If `P` has `j` interior zeros and `e in {0,1,2}` endpoint zeros then `2j + e <= deg P <= n`, and the number of distinct zeros is `j + e <= floor((n-e)/2) + e`, whose maximum over `e in {0,1,2}` is `floor(n/2) + 1` (attained at `e = 2` for `n >= 2`, at `e = 1` for `n = 1`).

*Oriented atoms.* Consider `F := (1 - C)^2 - S^2`, a trigonometric polynomial of degree `2n`. On `[-u,u]` the dual constraints give `|S| <= 1 - C`, and `1 - C >= 1 > 0` there because `C <= 0`; hence `F >= 0` on `[-u,u]`, and `F(t) = 0` exactly at the oriented contact points. `C` is even and `S` is odd, so `F` is even and its zeros come in pairs `+-t`. At `t = 0` we have `S(0) = 0` and `F(0) = (1 - C(0))^2 >= 1 > 0`, so the origin is never a contact point. A trigonometric polynomial of degree `2n` that is not identically zero has at most `4n` zeros on `S^1` counted with multiplicity. If there are `j` contact points in the open interval `(0,u)` and `e in {0,1}` at the endpoint `t = u`, then by evenness the multiplicity count is at least `4j + 2e`, since interior zeros of a nonnegative function have multiplicity at least `2` and occur in `+-` pairs. Hence `4j + 2e <= 4n`, so `j <= n` when `e = 0` and `j <= n - 1` when `e = 1` (because `4j <= 4n - 2` and `j` is an integer). In both cases `j + e <= n`. Finally §5.2 shows a contact point cannot carry both orientations, so the oriented support has at most `n` points.

Adding the two counts gives (6.1). The unconditional fallback is the standard basic-solution bound for a linear programme with `2n+1` equality constraints (mass, `n` cosine, `n` sine). `QED`

**Remark 5.1.** The `2n+1` bound is a restatement of the number of equality constraints and is recorded as a control row (ledger D5), not as evidence.

**Remark 5.2 (`n = 1`).** The bound gives one oriented and one symmetric orbit atom. This *derives* the two-atom structure that ZS-M61 Theorem M61.20 obtained by direct analysis, and answers the question of why the first-order case collapses further than the generic count suggests: the answer is that a degree-`1` cosine polynomial nonpositive on an interval has a single zero.

**Remark 5.3 (degenerate duals).** If `C == 0` the symmetric contact set is all of `[0,u]` and the argument gives no information; this happens exactly on the harmonic branch of §8, where the symmetric reservoir position is genuinely free. If `F == 0` then `|S| == 1 - C` identically, which forces `n >= 1` with `S` of constant modulus on the arc — a codimension-positive event. Extending Theorem 5 to these strata, and to `n >= 4`, is registered as debt `D-M62-DEG` and gate `F-M62.3'`.

**Verification.** Rows D1–D3 recover the dual multipliers of the oriented-mass linear programme (`scipy` HiGHS equality marginals), reconstruct `C` and `S`, and count contact clusters on a `2000`\-node grid for `n = 1, 2, 3` across 18 random instances: every instance satisfies both bounds, and dual feasibility (`max C <= 0`, `max (C + |S|) <= 1`) holds to `1e-7`. Row D4 records that the general-`n` argument is a manuscript proof and that the ledger block is a witness.

---

# 7\. Semidefinite representation

## 7.1 Theorem 13 (full circle)

For `d in R` and `w in C^n` let `T_n[d; w]` denote the `(n+1) x (n+1)` Hermitian Toeplitz matrix with constant diagonal `d` and `k`\-th superdiagonal `conj(w_k)` (equivalently `k`\-th subdiagonal `w_k`).

**Imported ingredient (Carathéodory–Toeplitz).** `IMPORTED-PROVEN`. For `d >= 0`, a vector `w in C^n` satisfies `T_n[d;w] >= 0` if and only if there is a nonnegative Borel measure `nu` on `S^1` with `nu(S^1) = d` and `integral exp(i k theta) dnu = w_k` for `k = 1..n`.

**Theorem 13\.** `PROVEN` (given the imported ingredient). For `u = pi`,

A\_n(m; pi) \= min A

   subject to   T\_n\[A; P\] \>= 0 ,   T\_n\[1 \- A; Q\] \>= 0 ,   Q in R^n ,   P \+ Q \= m ,        (7.1)

a semidefinite programme whose data are **linear** in `(A, P, Q)`. There is no relaxation: (7.1) is an exact reformulation.

**Proof.** By Theorem 2, `mu` with `d_TV(mu,R#mu) = A` decomposes as `tau + pi` with `tau >= 0` of mass `A` arbitrary and `pi >= 0` of mass `1-A` reflection-invariant. Setting `P_k := integral exp(i k theta) dtau` and `Q_k := integral exp(i k theta) dpi`, the imported ingredient says `T_n[A;P] >= 0` characterizes the admissible `P`, and `T_n[1-A;Q] >= 0` characterizes the admissible `Q` among nonnegative measures of mass `1-A`; reflection invariance of `pi` is equivalent to `Q_k = conj(Q_k)`, i.e. `Q in R^n`. Conversely any feasible triple produces such a pair of measures, hence a feasible `mu` with `d_TV <= A` by Theorem 2\. Minimizing `A` gives (7.1). `QED`

**Reading.** `P` is the moment vector of the piece that has to be peeled off, `Q` that of the symmetric remainder. Theorem 13 is the semidefinite avatar of Theorem 2\.

**Verification.** Row F1: at `n = 1`, the SDP value agrees with the exact closed form of Theorem 8 to `2.6e-9` over six instances. Row F2: at `n = 2, 3`, the grid linear programme at `N = 200, 600, 1800` converges monotonically to the SDP value (errors `2.8e-4 -> 3.7e-5 -> 1.8e-6`), confirming absence of a relaxation gap.

## 7.2 Theorem 14 (arbitrary arc)

Let `g_u(theta) := cos theta - cos u`, so `Omega_u = { g_u >= 0 }`. For a moment vector `m` (with mass `m_0`) define the localized sequence

(g\_u . m)\_k := (1/2)( m\_{k-1} \+ m\_{k+1} ) \- cos(u) m\_k ,      m\_{-k} := conj(m\_k).        (7.2)

**Imported ingredient (arc `K`\-moment representation).** `IMPORTED-PROVEN`. A truncated sequence `(m_0, ..., m_N)` is the moment sequence of a nonnegative measure supported in `Omega_u` if and only if `T_N[m_0; m] >= 0` and `T_{N-1}[(g_u.m)_0; g_u.m] >= 0`.

**Theorem 14\.** `DERIVED-CONDITIONAL` on the imported ingredient. For `0 < u <= pi` and `N := n + 1`,

A\_n(m;u) \= min A

  subject to  T\_N\[A;P\] \>= 0 ,  T\_{N-1}\[(g\_u.P)\_0 ; g\_u.P\] \>= 0 ,

              T\_N\[1-A;Q\] \>= 0 ,  T\_{N-1}\[(g\_u.Q)\_0 ; g\_u.Q\] \>= 0 ,

              Q in R^N ,   P\_k \+ Q\_k \= m\_k  for k \= 1..n ,                                (7.3)

with `P_{n+1}, Q_{n+1}` free. Again the programme is linear in `(A,P,Q)`.

**Proof.** Identical to Theorem 13 with the arc representation in place of Carathéodory–Toeplitz; the extra free moment of order `n+1` is required because the localizing matrix of size `N` involves `m_{N}`. `QED`

**Verification.** Row F3 compares (7.3) with the grid linear programme at `N_grid = 4000` for `n = 1,2,3` and random `u in (0.5, 3.0)`: maximum deviation `< 5e-5` over nine instances. Row F4 records the import status: the representation theorem is not proved here; only the min-`A` wrapper is contributed. This closes the internal debt `D-M62-ARC` conditionally on the imported statement.

---

# 8\. The complete first-order solution

Throughout this section `n = 1`, `x := Re m_1`, `y := Im m_1`, and by the symmetry `mu -> R#mu` we may assume `y >= 0`. Feasibility is `x >= cos u` and `x^2 + y^2 <= 1`, i.e. `(x,y) in C_1^pm(u) = { p^2 + q^2 <= 1, p >= cos u }`, the *lens* `L_u`. Also `C_1^0(u) = [cos u, 1] x {0}`, a horizontal segment. Put `s_1(u) := sin(min(u, pi/2))`.

## 8.1 Theorem 9 (constructive form and extremizers)

**Theorem 9\.** `PROVEN`. Suppose `y > 0` and `(x,y) in L_u`. Then

A\_1(x,y;u) \= min { y / sin t\_1 : t\_1 in T(x,y,u) } ,                                       (8.1)

where `T(x,y,u)` is the set of `t_1 in (0, u]` such that, with `A := y / sin t_1 <= 1`, the number

c\_0 := ( x \- A cos t\_1 ) / ( 1 \- A )                                                       (8.2)

lies in `[cos u, 1]` (with the convention that `t_1` is admissible when `A = 1` and `x = cos t_1`). The minimum is attained at one of at most three candidates:

(H)  t\_1 \= min(u, pi/2)                                          "harmonic"

(R)  t\_1 \= atan2(y, x-1)     \+ arcsin( \-y / sqrt((x-1)^2 \+ y^2) )    "right reservoir"  (gamma \= 1\)

(L)  t\_1 \= atan2(y, x-cos u) \+ arcsin( \-y cos u / sqrt((x-cos u)^2 \+ y^2) )  "left reservoir" (gamma \= cos u)

and an optimizer is the **two-orbit-atom** measure

mu\* \= A delta\_{sign(y) t\_1}  \+  ((1-A)/2) ( delta\_{t\_0} \+ delta\_{-t\_0} ) ,    cos t\_0 \= c\_0 ,   (8.3)

which has exactly the prescribed first moment, total mass `1`, and `d_TV(mu*, R#mu*) = A`.

**Proof.** *Reduction to two atoms.* By Theorem 3 the optimal `A` is the threshold at which `(x,y)` enters `K(A) = A L_u + (1-A) [cos u,1]`. At `A = A*` the point `(x,y)` lies on the boundary of the compact convex set `K(A*)`, so there is `w = (a_1,b_1) neq 0` with `<w, (x,y)> = h_{K(A*)}(w)`, and any decomposition `(x,y) = A* p + (1-A*) q` must have `p` maximizing `<w,.>` over `L_u` and `q` maximizing `<w,.>` over `[cos u,1] x {0}`.

The exposed face of the segment in direction `w` is: the endpoint `gamma = 1` if `a_1 > 0`; the endpoint `gamma = cos u` if `a_1 < 0`; the whole segment if `a_1 = 0`. The exposed face of the lens `L_u` in direction `w` with `b_1 > 0` (which holds since `y > 0`) is the single arc point at angle `t_1 = atan2(b_1, a_1)` if that angle lies in `[0,u]`, and the arc endpoint `t_1 = u` otherwise. In all cases `p = (cos t_1, sin t_1)` is a single point and `q = (gamma, 0)` may be taken to be a single point. Hence a two-orbit-atom optimizer exists, with the oriented atom at `t_1` carrying mass `A` (all of it on one side, the sign fixed by the sign of `y`) and the symmetric reservoir at `t_0` with `cos t_0 = gamma` carrying mass `1-A` split evenly between `+-t_0`.

*The equations.* Matching the first moment of (8.3) gives exactly (5.5): `A cos t_1 + (1-A) cos t_0 = x` and `A sin t_1 = y`. The second equation gives `A = y / sin t_1`; the first then determines `cos t_0 = c_0` by (8.2). Admissibility is `A in [0,1]`, `t_1 in (0,u]`, `c_0 in [cos u, 1]`. Minimizing `A` is minimizing `y / sin t_1`, i.e. maximizing `sin t_1`, over the admissible set; this is (8.1).

*The three candidates.* By the face analysis, at the optimum either `a_1 = 0` — in which case `t_1` maximizes `sin` on `[0,u]`, i.e. `t_1 = min(u,pi/2)`, case (H) — or `a_1 neq 0` and the reservoir sits at an endpoint `gamma in {1, cos u}`. In the latter case eliminate `A` between the two equations of (5.5):

(x \- gamma) sin t\_1 \- y cos t\_1 \= \- y gamma ,

i.e. `sqrt((x-gamma)^2 + y^2) sin( t_1 - beta ) = - y gamma` with `beta = atan2(y, x-gamma)`, which is the displayed formula. (For `gamma = 1` this simplifies to `t_1 = pi - 2 arctan( y/(1-x) )`.)

*The extremizer.* `mu*` in (8.3) has orbit data `sigma = A delta_{t_1} + (1-A) delta_{t_0}` and `delta = sign(y) A delta_{t_1}`, so `|delta| <= sigma` and, by (3.2), `d_TV(mu*, R#mu*) = ||delta||_var = A`. `QED`

**Verification.** Row E3 compares (8.1) with the closed form of Theorem 8 on 30000 random feasible triples (maximum deviation `8.3e-8`, concentrated at the degenerate corner `A -> 1`, and no instance without a solution). Row E4 checks that the exhibited measure (8.3) reproduces `m_1`, has mass `1`, and has reflection asymmetry exactly `A`: maximum residual `2.8e-15` over 3000 instances. Row E5 checks that at most two orbit atoms are ever used.

## 8.2 Theorem 8 (closed form)

**Theorem 8\.** `PROVEN`. With `R_gamma := x - gamma` and `d_gamma := -gamma`,

A\_1(x,y;u) \= max { y / s\_1(u) ,  Q(1-x, 1\) ,  \[cos u \< 0\] \* Q(x \- cos u, |cos u|) } ,      (8.4)

where `Q(R,d)` is `-infinity` when `y <= R/d` (that reservoir does not bind) and otherwise

Q(R,d) \= ( \-R d \+ sqrt( R^2 d^2 \+ (1-d^2)(R^2 \+ y^2) ) ) / (1 \- d^2)      for d \< 1,

Q(R,1) \= ( R^2 \+ y^2 ) / ( 2 R ) .

**Proof.** By Theorem 3, `A_1` is the least `A` with `(x,y) in A L_u + (1-A)[cos u,1]`, i.e. such that there exists `xi in [(1-A) cos u, (1-A)]` with `p := x - xi` satisfying `p >= A cos u` and `p^2 + y^2 <= A^2`. Writing `rho := sqrt(A^2 - y^2)` (so `A >= y` is necessary), the existence of `p` is the nonemptiness of

\[ max(A cos u, x \- (1-A), \-rho) ,  min( x \- (1-A) cos u , rho ) \] .

Six pairwise comparisons must hold. Two are automatic (`x - (1-A) <= x - (1-A) cos u`, and `A cos u <= x - (1-A) cos u` which is `x >= cos u`, the support condition). The remaining ones are:

* `A cos u <= rho`. If `cos u <= 0` this is automatic given `A >= y`; otherwise squaring gives `A sin u >= y`. Together: `A >= y / s_1(u)`.  
* `x - (1-A) <= rho`. Writing `R := 1-x`, this holds if `A <= R`, and otherwise squaring gives `A >= (R^2+y^2)/(2R)`. Since `(R^2+y^2)/(2R) <= R` iff `y <= R`, the condition is: automatic if `y <= R`, and `A >= (R^2+y^2)/(2R)` if `y > R`. This is `Q(1-x,1)`.  
* `-rho <= x - (1-A) cos u`. If `cos u >= 0` this follows from `x >= cos u >= (1-A) cos u`. If `cos u < 0`, put `d := -cos u in (0,1]` and `R_2 := x + d`; the left side of the inequality is `R_2 - A d >= -rho`, automatic when `A <= R_2/d`, and otherwise equivalent to `(R_2 - A d)^2 <= A^2 - y^2`, i.e. `A^2(1-d^2) + 2 R_2 d A - R_2^2 - y^2 >= 0`, whose positive root is `Q(R_2,d)`. Again the branch binds only when `y > R_2/d`.

Taking the largest of the three lower bounds gives (8.4). `QED`

**Verification.** Row E1 compares (8.4) against a `40`\-digit bisection of the nested family (Theorem 3(ii)) on 113 random feasible triples: maximum deviation `1.7e-37`. Row E2 compares against the raw total-variation linear programme on a `1001`\-node grid: `5.5e-6`, the grid scale.

## 8.3 The three branches, read structurally

| branch | active when | dual sign | reservoir | oriented atom |
| :---- | :---- | :---- | :---- | :---- |
| harmonic | the reservoir is not exhausted | `a_1 = 0` | free, any `t_0` with (8.2) | `t_1 = min(u, pi/2)` |
| right | `y > 1-x` | `a_1 > 0` | `t_0 = 0` (`cos t_0 = 1`) | `t_1 = pi - 2 arctan( y/(1-x) ) < pi/2` |
| left | `cos u < 0` and \`y \> (x \- cos u)/ | cos u | \` | `a_1 < 0` |

The branch structure is therefore **not** an artefact of algebra: it is the classification of the exposed faces of the segment `C_1^0(u)`, which has exactly two endpoints and one relative interior.

Full circle, `u = pi`: `s_1 = 1`, `cos u = -1`, and (8.4) collapses to the `x`\-symmetric form

A\_1(x,y;pi) \= |y|                                 if |x| \+ |y| \<= 1,

            \= ( (1-|x|)^2 \+ y^2 ) / ( 2 (1-|x|) )  otherwise.                              (8.5)

## 8.4 Corollary 10 (recovery of ZS-M61 Theorem M61.20)

**Corollary 10\.** `DERIVED`. Theorem 8 restricted to `n = 1` on a symmetric arc reproduces the feasibility region, the inner/outer branch structure, the two-atom extremizer, and the dual equality certificate of ZS-M61 Theorem M61.20; the earlier "inner" and "outer" branches are the right-reservoir and harmonic branches above, and the earlier numerically certified duality gap `< 1e-8` is replaced by the exact certificate of Theorem 7\.

Ledger rows E1–E5 and C1–C4 are the corresponding checks. Gate `F-M62.1` ("if the general framework does not reproduce M61.20, the formulation is wrong") is **passed**.

## 8.5 Theorem 11 (exact gradient and condition number)

**Theorem 11\.** `PROVEN`. On the interior of each branch, `A_1` is differentiable and

grad A\_1 (x,y) \= ( a\_1 , b\_1 ) ,

the dual pair of Theorem 7\. Explicitly, in the budget branches with reservoir `gamma` and oriented angle `t_1`,

dA/dx \= kappa cos t\_1 ,   dA/dy \= kappa sin t\_1 ,   || grad A\_1 || \= kappa \= 1/(1 \- gamma cos t\_1),

and on the harmonic branch `grad A_1 = (0, 1/s_1(u))`, of norm `1/s_1(u)`. Consequently `A_1` is locally Lipschitz with modulus `kappa`, and for arbitrary `n` the subdifferential of `A_n` at `m` is the set of optimal dual pairs `(a,b)` of (5.2), so that

| A\_n(m';u) \- A\_n(m;u) |  \<=  ||m' \- m|| \* sup { ||(a,b)|| : (a,b) dual-optimal at m or m' } .

**Proof.** Convexity (Corollary 4\) plus the envelope theorem for the concave dual (5.2): the maximizing `w` is a subgradient. Differentiability on branch interiors follows from uniqueness of the exposed faces there. The explicit values are (5.6). `QED`

**Verification.** Row E6 compares the analytic gradient with symmetric finite differences (`h = 1e-6`) at four points spanning all three branches; agreement to `1e-5` or better in every component. For example at `(x,y,u) = (0.5, 0.7, pi)` the right branch gives `grad = (0.48, 1.4)` and `kappa = 1.4799`, matching `||grad|| = 1.48`.

---

# 9\. Hierarchy, odd-data-only problem, and second order

## 9.1 Theorem 12 (monotone hierarchy and convergence)

**Theorem 12\.** `PROVEN`. Let `mu in P(Omega_u)` have Fourier moments `m_k`, and set `A_n := A_n(m_1,...,m_n; u)`. Then

(i)   0 \<= A\_1 \<= A\_2 \<= ... \<= 1 ;

(ii)  lim\_{n-\>infinity} A\_n \= d\_TV(mu, R\#mu) .

No determinacy hypothesis is needed.

**Proof.** (i) The feasible set `F_n := { nu in P(Omega_u) : integral exp(ik theta) dnu = m_k, k <= n }` decreases with `n`, so the minimum increases.

(ii) `P(Omega_u)` is weak-\* compact, each `F_n` is weak-\* closed, and `F_1 supset F_2 supset ...`. By Stone–Weierstrass the trigonometric polynomials are dense in `C(Omega_u)`, so `intersect_n F_n = {mu}`: the full moment sequence determines the measure on a compact subset of the circle. The functional `nu -> d_TV(nu, R#nu) = (1/2) || nu - R#nu ||_var` is weak-\* lower semicontinuous (it is a supremum of the weak-\* continuous functionals `nu -> integral f d(nu - R#nu)` over `f in C(Omega_u)` with `||f||_inf <= 1`, halved). Pick `nu_n in F_n` attaining `A_n`. By compactness a subnet converges weak-\* to some `nu_infinity`, which lies in every `F_n`, hence equals `mu`. Lower semicontinuity gives `d_TV(mu,R#mu) <= liminf A_n`. The reverse inequality is (i) together with `A_n <= d_TV(mu,R#mu)` (because `mu in F_n`). `QED`

**Verification.** Row H1 exhibits the monotone sequence for the Gibbs law with `S_e = 0.7 cos t`, `S_o = 0.9 sin t + 0.4 sin 2t` on the full circle:

A\_1..A\_6 \= 0.343544856, 0.345241349, 0.388444065, 0.389219895, 0.402265646, 0.402676637

d\_TV(mu, R\#mu) \= 0.417836268

Row H2 checks `A_n <= d_TV` throughout, with residual gap `1.5e-2` at `n = 6`; row H3 records that convergence itself is proved in the manuscript and only witnessed by the ledger.

## 9.2 Theorem 15 (odd data only)

Define the *odd body*

Y\_n(u) := conv { \+- ( sin t, sin 2t, ..., sin n t ) : t in \[0,u\] }  subset R^n ,

a centrally symmetric compact convex body, and let `gamma_{Y_n(u)}` be its Minkowski gauge.

**Theorem 15\.** `PROVEN`. If only the odd data `y = (y_1,...,y_n)` are prescribed and the even data are free, then

min { d\_TV(mu,R\#mu) : mu in P(Omega\_u), Im m\_k \= y\_k, k \= 1..n } \= gamma\_{Y\_n(u)}(y)

   \= sup { \<b, y\> : || sum\_k b\_k sin(k t) ||\_{L^infinity\[0,u\]} \<= 1 } .                    (9.1)

Moreover `gamma_{Y_n(u)}(y)` is always a lower bound for `A_n(m;u)`, and equality holds if and only if the residual even budget is feasible, i.e.

x in { x' : (x', y) in A\_0 C\_n^pm(u) } \+ (1 \- A\_0) C\_n^0(u) ,      A\_0 := gamma\_{Y\_n(u)}(y).  (9.2)

**Proof.** Apply Theorem 3 with `Phi = (c, s)` and project onto the last `n` coordinates. The projection of `A C_n^pm(u) + (1-A) C_n^0(u)` onto the `y`\-block is `A * proj(C_n^pm(u)) = A Y_n(u)`, since `proj(C_n^0(u)) = {0}`. Hence `y` is attainable at cost `A` iff `y in A Y_n(u)`, i.e. `A >= gamma_{Y_n(u)}(y)`. The support-function formula for `gamma` is the second equality in (9.1). The lower bound for the constrained problem is immediate (dropping constraints cannot increase the minimum), and equality is exactly the statement that the fibre over `y` at level `A_0` meets the translated even body, which is (9.2). `QED`

**Remark 15.1.** The right-hand side of (9.1) is precisely the naive dual bound obtained by testing the odd part against odd trigonometric polynomials. Theorem 15 identifies it as an exact value of a well-posed problem and gives the *precise* criterion (9.2) for when it is sharp for the full problem — replacing the vague statement "this bound is generally not sharp".

**Verification.** Row G1: the linear programme with even data free agrees with the gauge linear programme to `9.4e-7` over 24 instances at `n = 1,2,3`.

## 9.3 Theorem 16 (the second-order odd body on the circle)

**Theorem 16\.** `PROVEN`.

Y\_2(pi) \= { (v,w) in R^2 : |w| \<= 1  and  2 v^2 \- 1 \<= sqrt(1 \- w^2) } ,                   (9.3)

equivalently `|v| <= 1` and `|w| <= psi(|v|)` with `psi(V) = 1` for `V <= 1/sqrt 2` and `psi(V) = 2 V sqrt(1-V^2)` for `V >= 1/sqrt 2`. Its gauge is

gamma\_{Y\_2(pi)}(y\_1,y\_2) \= max { |y\_2| ,  2 y\_1^2 / sqrt( 4 y\_1^2 \- y\_2^2 ) }               (9.4)

whenever the second entry is real and exceeds `|y_2|`, and `|y_2|` otherwise.

**Proof.** Parametrize the generating curve by `v = sin t`. For `t in [0,pi/2]`, `sin 2t = 2 v sqrt(1-v^2)`; for `t in [pi/2,pi]`, `sin 2t = -2 v sqrt(1-v^2)`; the `+-` symmetrization then gives the generating set `{ (v, +- phi(|v|)) : |v| <= 1 }` with `phi(V) := 2 V sqrt(1-V^2)`.

`phi` is concave on `(0,1)`: `phi'(V) = 2(1-2V^2)/sqrt(1-V^2)` and

phi''(V) \= 2 V ( 2V^2 \- 3 ) / (1-V^2)^{3/2}  \< 0    for V in (0,1),

since `2V^2 - 3 < 0`. Its maximum is at `phi'(V) = 0`, i.e. `V = 1/sqrt 2`, with `phi(1/sqrt2) = 1`.

The upper boundary of `conv` is the least concave majorant of `V -> phi(|V|)` on `[-1,1]`. That function is concave on `[0,1]` and on `[-1,0]` but has a downward corner at `0`. The function `psi` defined above is concave (it is constant on `[-1/sqrt2, 1/sqrt2]`, equals the concave `phi` outside, and the two pieces meet with matching value `1` and matching derivative `0` at `+-1/sqrt2`), and it dominates `phi(|.|)` since `phi <= 1`. Any concave majorant must be `>= 1` at `+-1/sqrt2` and hence, by concavity and symmetry, `>= 1` on the middle interval, and `>= phi` outside; so `psi` is the least one. This gives the second description; the first follows by squaring: for `|v| >= 1/sqrt2`, `w^2 <= 4v^2(1-v^2)` is equivalent to `1 - w^2 >= (2v^2-1)^2`, i.e. `sqrt(1-w^2) >= 2v^2-1`, and for `|v| <= 1/sqrt2` the inequality `2v^2 - 1 <= 0 <= sqrt(1-w^2)` is automatic while `|w| <= 1` is the binding constraint; `|v| > 1` is excluded because then `2v^2-1 > 1 >= sqrt(1-w^2)`.

Gauge: `gamma(y) = min { A > 0 : y/A in Y_2(pi) }`. The constraint `|y_2|/A <= 1` gives `A >= |y_2|`. If `2 y_1^2 <= A^2` the second constraint is automatic; otherwise squaring `(2y_1^2/A^2 - 1)^2 <= 1 - y_2^2/A^2` gives `4 y_1^4 / A^2 <= 4 y_1^2 - y_2^2`, i.e. `A >= 2 y_1^2 / sqrt(4 y_1^2 - y_2^2)` (which requires `4 y_1^2 > y_2^2`). `QED`

**Corollary 16.1.** Combining Theorems 15 and 16 gives a closed-form value of the second-order problem on the full circle on the whole stratum where the even data are unconstrained — an exact `n = 2` result.

**Verification.** Row G2 compares (9.4) with the gauge linear programme at `N = 4000` on 600 random points: maximum deviation `2.1e-7`. Row G3 checks the concavity of `phi` numerically on `2e5` nodes; row G4 certifies `phi(1/sqrt2) = 1`.

---

# 10\. The physical bridge

This section is the only one that uses Z-Spin input. It is written so that every mathematical statement (Theorems 17–20) is independent of any physical interpretation, and every physical reading is separated out and flagged.

## 10.1 The object

ZS-F1 fixes the Z-bias field as `Phi = rho exp(i theta)` with `rho = |Phi|` reflection-even. ZS-M61 Theorem M61.22' establishes that the admissible seam involutions of field space form the single reflection conjugacy class `J_alpha : Phi -> exp(2 i alpha) conj(Phi)`, whose odd mode is `S_alpha(Phi) = Im( exp(-i alpha) Phi )`; on the vacuum circle `rho = 1` this is `S_alpha = sin(theta - alpha)`. The seam-odd contraction multiplier generated by a boundary phase law `mu` at accumulated phase `c` has the characteristic-function form

a(c) \= E\_mu\[ exp( \-2 i c S\_alpha ) \] \= integral exp( \-2 i c sin phi ) dmu(phi) ,    phi := theta \- alpha.  (10.1)

Everything below is `alpha`\-covariant: rotating the axis rotates `phi` and nothing else. In particular no identification of the abstract Z-register parity basis with `(Re Phi, Im Phi)` is used, so the unresolved intertwiner debt `D-M61-IOTA` is not touched (non-claim `NC-M62.3`).

The support of `mu` is allowed to be any reflection-invariant arc `Omega_u`, `0 < u <= pi`; `u = pi` is the unrestricted case.

## 10.2 Theorem 17 (multiplier asymmetry price and reachability)

**Theorem 17\.** `PROVEN`. Fix `c neq 0` and `0 < u <= pi`, and set

Psi := min( 2 |c| sin( min(u, pi/2) ) , pi ) .                                             (10.2)

Define the *asymmetry-budget attainable set*

Lambda\_A(c,u) := { a(c) : mu in P(Omega\_u),  d\_TV(mu, R\#mu) \<= A } .

Then

(i)   Lambda\_A(c,u) \= A \* L\_Psi \+ (1-A) \* \[cos Psi, 1\] ,      L\_Psi := conv{ exp(i psi) : |psi| \<= Psi } ;

(ii)  a target lambda is realizable, i.e. lambda in Lambda\_1(c,u), iff  |lambda| \<= 1  and  Re lambda \>= cos Psi ;

(iii) the minimum reflection asymmetry compatible with a(c) \= lambda is

          A\*(lambda; c, u) \= A\_1( Re lambda , |Im lambda| ; Psi ) ,                        (10.3)

      the first-order value of Theorem 8 evaluated on the rescaled arc of half-width Psi;

(iv)  A\*(lambda; c, u) is non-increasing in |c| and in u; for Psi \>= pi it is constant and equal to

          A\*\_inf(lambda) \= |Im lambda|                                        if |Re lambda| \+ |Im lambda| \<= 1,

                         \= ( (1-|Re lambda|)^2 \+ (Im lambda)^2 )              otherwise.

                           \-------------------------------------

                                  2 ( 1 \- |Re lambda| )

**Proof.** Apply Theorem 3 with `Omega = Omega_u`, `R(phi) = -phi`, and the two-dimensional observable

Phi(phi) := ( cos(2 c sin phi) , \- sin(2 c sin phi) ) ,   identified with the complex number exp(-2 i c sin phi).

`Phi` is bounded and measurable, `Phi_e(phi) = ( cos(2 c sin phi) , 0 )`.

The image `Phi(Omega_u)` is `{ exp(-i psi) : psi = 2 c sin phi , |phi| <= u }`. As `phi` runs over `[-u,u]`, `sin phi` runs over the interval `[-s, s]` with `s = sin(min(u,pi/2))`, continuously and onto; hence `psi` runs over `[-2|c| s, 2|c| s]` onto. If `2|c| s >= pi` the image is the whole unit circle and `conv Phi(Omega_u)` is the closed unit disc, which is `L_pi`; otherwise `conv Phi(Omega_u) = L_Psi` with `Psi = 2|c| s`. In both cases `M_Phi = L_Psi` with `Psi` as in (10.2). Likewise `Phi_e(Omega_u) = { cos psi : |psi| <= Psi }`, whose convex hull is `[cos Psi, 1]` when `Psi <= pi` and `[-1,1] = [cos pi, 1]` when `Psi = pi`. So `M_Phi^sym = [cos Psi, 1] x {0}`. Theorem 3 gives (i).

(ii) `Lambda_1 = L_Psi = { z : |z| <= 1, Re z >= cos Psi }`.

(iii) The pair `(M_Phi, M_Phi^sym) = (L_Psi, [cos Psi,1] x {0})` is *identical* to the pair `(C_1^pm(Psi), C_1^0(Psi))` appearing in the first-order Fourier problem on the arc `Omega_Psi` (§8). Hence the two threshold problems coincide, and the value is `A_1` evaluated at the data `(Re lambda, -Im lambda)` on the arc of half-width `Psi`; since `A_1` depends on the second entry only through its modulus, (10.3) follows.

(iv) `Psi` is non-decreasing in `|c|` and in `u`, and `A -> K(A)` is nested (Theorem 3(ii)) while `Psi -> L_Psi` and `Psi -> [cos Psi, 1]` are both non-decreasing; so the threshold is non-increasing in `Psi`. For `Psi >= pi` the arc is the full circle and (10.3) reduces to `A_1(Re lambda, |Im lambda|; pi)`, which is exactly the two-branch formula (8.5); substituting gives the displayed piecewise expression. `QED`

**Remark 17.3 (erratum `E-M62-13`; the branch condition is not optional).** Versions 1.0–1.2 of this paper stated (iv) with the second branch only, as a single formula. That statement is **false** on the region `|Re lambda| + |Im lambda| <= 1`. The cleanest counterexample is `lambda = 0`: by (i) with `A = 0` the attainable set at `Psi = pi` is the real segment `[cos pi, 1] = [-1,1]`, which contains `0`, so a reflection-symmetric law realizes `lambda = 0` and `A*_inf(0) = 0`; the single formula returns `(1-0)^2/(2) = 1/2`. Over `200000` feasible targets the single formula deviates from the true value by as much as `0.4975`, while the piecewise form of (iv) agrees to `0` in floating point. The error is confined to the general statement: the two branches meet continuously on `|Re lambda| + |Im lambda| = 1`, and the frozen Z-Spin target has

|Re lambda| \+ |Im lambda| \= 1.2548705574 \> 1 ,

so it lies strictly inside the second branch and every number of §11 is unaffected. (Ledger row `N7`, which also checks that the superseded single formula *fails* the same test, so the regression has teeth.)

**Remark 17.1 (why no series truncation is needed).** The Jacobi–Anger expansion `exp(-2 i c sin phi) = sum_k (-1)^k J_k(2c) exp(i k phi)` re-expresses `a(c)` through the Fourier moments of `mu` and therefore requires, for a finite-data statement, a certified tail bound on `sum_{|k|>N} |J_k(2c)|`. Theorem 17 bypasses this entirely: the map `phi -> 2 c sin phi` is a measurable surjection onto an interval, and the extremal problem only sees the *image* of the observable, not its harmonic content. The whole harmonic-analysis apparatus is therefore unnecessary for this observable, and the associated failure mode "the tail is too large to decide" cannot occur.

**Remark 17.2 (relation to the reflection-symmetric default).** Setting `A = 0` in (i) gives `Lambda_0(c,u) = [cos Psi, 1] subset R`. Hence any reflection-symmetric boundary law produces a **real** multiplier, and the Haar-uniform law is one point of that segment. This recovers, as the `A = 0` section of a one-parameter family, the earlier statement that the uniform phase law yields `a(c) = J_0(2c) in R` (ZS-M61 Theorem M61.23'), and converts it from a qualitative exclusion into a priced one.

**Verification.** Row I1 compares (10.3) with a direct linear programme for the multiplier problem (grid `N = 1500`) on 30 random `(c, u, lambda)` triples, `lambda` generated from random measures so as to be attainable: maximum deviation `1.96e-5`, the grid scale. Row I2 tests criterion (ii) against the finiteness of (10.3) on 400 random `(lambda, c, u)`: zero mismatches. Row I4 guards monotonicity in `c`.

## 10.3 Theorem 18 (an explicit extremal boundary law)

**Orientation bookkeeping.** The rescaling of Theorem 17 uses `psi := 2|c| sin t >= 0`. Because `sin` is odd,

sin( 2 c sin t ) \= sign(c) \* sin( 2|c| sin t ) ,

so the odd half of (10.1) reads `Im a(c) = - sign(c) integral sin(psi) d(delta)`. The datum handed to the first-order problem on the arc `Omega_Psi` is therefore

X := Re lambda ,        Y := \- sign(c) \* Im lambda .                                       (10.3a)

`A_1` depends on `Y` only through `|Y| = |Im lambda|`, so Theorem 17 is untouched; but the **orientation of the extremal atom is not**.

**Theorem 18\.** `PROVEN`. Let `c neq 0`, let `lambda` be realizable at `(c,u)`, put `A := A*(lambda;c,u)`, and let `(t_1^psi, t_0^psi)` be the two-orbit-atom data of Theorem 9 for the first-order problem with datum `(X,Y)` of (10.3a) on the arc `Omega_Psi`. Define

t\_j := arcsin( t\_j^psi / (2|c|) )   for j \= 0,1 ,

sgn := sign(Y) \= \- sign(c) \* sign( Im lambda ) ,                                           (10.4a)

mu\* := A delta\_{ sgn \* t\_1 }  \+  ((1-A)/2) ( delta\_{t\_0} \+ delta\_{-t\_0} ) .                (10.4)

Then `mu* in P(Omega_u)`, `a(c) = lambda` exactly, and `d_TV(mu*, R#mu*) = A`. In particular the minimum is attained by a measure with **three atoms**, i.e. two orbit atoms.

**Proof.** By construction `2|c| sin(t_j) = t_j^psi`, so the pushforward of `mu*` under `phi -> 2|c| sin phi` is the two-atom solution of the rescaled first-order problem for the datum `(X,Y)`; the identity `Im a(c) = -sign(c) integral sin(psi) d(delta)` then converts `Y` back to `Im lambda`, and Theorem 9 gives both the moment identity and the asymmetry value. Lemma 1 transports the total-variation computation back. Admissibility `t_j <= u` holds because `t_j^psi <= Psi <= 2|c| sin(min(u,pi/2))`. `QED`

**Erratum E-M62-3.** Version 1.0 of this paper stated (10.4) with `sgn = sign(-Im lambda)`, i.e. it dropped `sign(c)`. That is correct for `c > 0` and **wrong for `c < 0`**, where the constructed measure realizes the complex conjugate `conj(lambda)` instead of `lambda`. The value statements (Theorem 17\) were unaffected; only the exhibited extremizer was. Version 1.0's verification block `I3` tested six pairs, all with `c > 0`, and therefore could not see the defect. Row `N3` of v1.1 tests four negative-`c` instances and additionally checks that the v1.0 convention *fails* there, so the regression has teeth.

**Verification.** Row I3 constructs (10.4) for the frozen Z-Spin target at six `(c,u)` pairs with `c > 0` and checks `|a(c) - lambda| <= 1.6e-16`, `|d_TV(mu*,R#mu*) - A*| = 0`, and total mass `1` to machine precision. Row N3 repeats this at `c = -1.2, -pi/2, -2, -1.5`: the corrected sign gives `|a(c) - lambda| < 1e-14` while the v1.0 sign gives a residual of order `2 |Im lambda|`.

## 10.4 What the action must supply

Theorems 17 and 18 give lower bounds on the asymmetry of any admissible state. To convert a lower bound into an obstruction one needs an **upper** bound on the asymmetry that the dynamics can produce. Theorems 19 and 20 supply exactly that for finite-volume Gibbs boundary laws, and reduce the requirement to a single scalar.

## 10.5 Theorem 19 (Gibbs asymmetry identity and ceiling)

**Theorem 19\.** `PROVEN`. Let `S_b : S^1 -> R` be measurable with `exp(-S_b) integrable`, and let

dmu \= exp(-S\_b(theta)) dtheta / Z ,   Z \= integral exp(-S\_b) dtheta .

Decompose `S_b = S_e + S_o` into its even and odd parts about the reflection axis. Then

d\_TV(mu, R\#mu) \= integral exp(-S\_e) |sinh S\_o| / integral exp(-S\_e) cosh S\_o

               \= \< |tanh S\_o| \>\_w ,        w := exp(-S\_e) cosh S\_o ,                       (10.5)

where `< . >_w` is the average with respect to the probability measure `w dtheta / integral w dtheta`. Consequently

d\_TV(mu, R\#mu) \<= tanh || S\_o ||\_{L^infinity} ,                                            (10.6)

with equality if and only if `|S_o|` is `w`\-almost everywhere constant.

**Corollary 19.1.** If `S_o == 0` (an exactly reflection-even finite-volume action) then `d_TV(mu,R#mu) = 0` and, by Remark 17.2, `a(c)` is real for every `c`.

**Proof.** `R#mu` has density `exp(-S_e + S_o)/Z`, so

d\_TV \= (1/2) integral | exp(-S\_e-S\_o) \- exp(-S\_e+S\_o) | dtheta / Z

     \= integral exp(-S\_e) |sinh S\_o| dtheta / Z .

Also `Z = integral exp(-S_e) exp(-S_o) = integral exp(-S_e) cosh S_o`, because `exp(-S_e) sinh S_o` is odd and integrates to zero. Dividing gives (10.5) after writing `|sinh S_o| = |tanh S_o| cosh S_o`. Inequality (10.6) and its equality case are immediate from `|tanh S_o| <= tanh ||S_o||_inf`. `QED`

**Verification.** Rows J1 and J2: over 150 random finite-Fourier actions (`J <= 4` harmonics, Gaussian coefficients), the identity (10.5) reproduces a direct total-variation quadrature on `4e5` nodes to `1.7e-15`, and the ceiling (10.6) is never violated.

## 10.6 Theorem 20 (reflection entropy: an orbit identity and an imported floor)

Version 1.0 stated this result only for Gibbs laws and typed its inequality as a contribution. Both are corrected: the identity holds for **every** measure, and the inequality is an **imported** result specialized to involution pairs.

**Theorem 20\.** `PROVEN`. Let `Omega` be compact, `R` an involution, `mu in P(Omega)`, and let `(sigma, delta)` be the orbit data of Lemma 1\. If `mu` is not absolutely continuous with respect to `R#mu` then `D_KL(mu || R#mu) = +infinity`. Otherwise let `h := d delta / d sigma`, a Borel function with values in `[-1,1]`, and let `A := d_TV(mu, R#mu)`. Then

A \= integral |h| dsigma ,                                                                  (10.6a)

D\_KL( mu || R\#mu ) \= 2 integral |h| artanh|h| dsigma ,                                     (10.7)

A \<= || h ||\_{L^infinity(sigma)} .                                                         (10.7b)

**Corollary 20.1 (entropy floor; `IMPORTED / SPECIALIZED`).**

D\_KL( mu || R\#mu )  \>=  2 A artanh(A)  \>=  2 A^2 ,                                         (10.8)

the last inequality being Pinsker's. Both inequalities are sharp: equality throughout the first holds for the two-point involution pair `mu = ((1+A)/2, (1-A)/2)` with `R` the transposition.

**Corollary 20.2 (Gibbs specialization).** For a finite-volume Gibbs law as in Theorem 19 one has `h = - tanh S_o` and `dsigma = w dtheta / integral w` with `w = exp(-S_e) cosh S_o`, hence

d\_TV(mu, R\#mu) \= \< |tanh S\_o| \>\_w ,        D\_KL( mu || R\#mu ) \= 2 \< S\_o tanh S\_o \>\_w ,     (10.9a)

and (10.7b) becomes the ceiling `d_TV <= tanh || S_o ||_infinity` of Theorem 19\.

**Proof of Theorem 20\.** Formula (10.6a) is (3.2) rewritten, since `||delta||_var = integral |h| dsigma`. On the positive half of a non-fixed orbit the densities of `mu` and `R#mu` with respect to `sigma` are `(1+h)/2` and `(1-h)/2`; on the negative half they are exchanged; at a fixed point they agree and `h = 0`. Hence

D\_KL \= integral\_{+} ((1+h)/2) log((1+h)/(1-h)) dsigma \+ integral\_{-} ((1-h)/2) log((1-h)/(1+h)) dsigma

     \= integral h log((1+h)/(1-h)) dsigma

     \= 2 integral h artanh(h) dsigma \= 2 integral |h| artanh|h| dsigma ,

using `log((1+h)/(1-h)) = 2 artanh h` and the evenness of `t -> t artanh t`. Absolute continuity fails precisely when `|h| = 1` on a set of positive `sigma`\-measure, where the integrand is `+infinity`, consistent with the convention. Inequality (10.7b) is immediate from (10.6a) and `sigma(Omega) = 1`. `QED`

**Proof of Corollary 20.1.** `g(t) := t artanh t` is convex on `[0,1)`: `g'(t) = artanh t + t/(1-t^2)` and `g''(t) = 1/(1-t^2) + (1+t^2)/(1-t^2)^2 > 0`. Since `sigma` is a probability measure, Jensen gives

integral |h| artanh|h| dsigma \= integral g(|h|) dsigma  \>=  g( integral |h| dsigma ) \= g(A) \= A artanh A ,

so `D_KL >= 2 A artanh A`. Finally `artanh(A) >= A` on `[0,1)`. Equality in Jensen forces `|h|` to be `sigma`\-a.e. constant, which together with `A = |h|` gives the two-point pair. `QED`

**Erratum E-M62-6 (attribution).** Version 1.0 listed (10.8) as `OPEN-NOVELTY`. It is not new. For an involution, `D(mu || R#mu) = D(R#mu || mu)` — apply `R` to both arguments and use `R#R#mu = mu` — so the Jeffreys divergence satisfies `J(mu, R#mu) = 2 D(mu || R#mu)`. The sharp lower bound of the Jeffreys divergence in terms of total variation, due to Gilardoni and restated by Sason and Verdu, is

J(P,Q)  \>=  2 eps log( (1+eps)/(1-eps) )  \=  4 eps artanh(eps) ,      eps := d\_TV(P,Q),

attained by the two-point pair `P = ((1+eps)/2, (1-eps)/2)`, `Q = ((1-eps)/2, (1+eps)/2)` — which is itself an involution pair. Dividing by two gives exactly (10.8). Corollary 20.1 is therefore `IMPORTED / SPECIALIZED`; the proof above is an independent short derivation in the involution case, not a new inequality. What remains contributed here is the **orbit identity** (10.7) and its Gibbs form (10.9a). (Ledger row `N6` verifies the saturation to 40 digits and the involution symmetry `J = 2D` on 2000 random involutions; row `N5` verifies the floor and the ceiling on 3000 measures with no Gibbs structure.)

**Verification.** Rows J3 and J4 verify (10.9a) and (10.8) on 150 random finite-Fourier actions: the identity reproduces a direct Kullback–Leibler quadrature to `9.8e-15`; the floor is never violated, and the observed improvement over Pinsker reaches `2.65` nats. Rows N4 and N5 verify (10.7), (10.8) and (10.7b) on 3000 random measures that are **not** Gibbs laws, to `1e-12`.

## 10.7 The reduced physical obligation

Combining Theorems 17, 19 and 20:

a(c) \= lambda   with a finite-volume Gibbs boundary law

  \==\>  tanh || S\_o ||\_inf  \>=  d\_TV(mu,R\#mu)  \>=  A\*(lambda;c,u)

  \==\>  || S\_o ||\_{L^infinity}  \>=  artanh A\*(lambda;c,u) .                                 (10.9)

The physical task is therefore no longer "derive the boundary phase law", nor even "derive a finite list of its Fourier moments": it is the single scalar question

> does the effective boundary action have an odd part, and is its supremum norm at least `artanh A*`?

The possible outcomes are:

* `CLOSED-NEGATIVE` — the reduction yields `||S_o||_inf < artanh A*` (in particular `S_o == 0`);  
* `PRICED` — `A*` is finite and the reduction does not supply the required odd content;  
* `OPEN` — the reduction does not bound `||S_o||_inf` at all;  
* `CLOSED-PASS-CONDITIONAL` — the reduction supplies the required odd content without any coefficient having been solved from `lambda`.

Because the requirement is one inequality on one functional, the identifiability trap of ZS-M56 Theorem M56.7 (equal numbers of free coefficients and constraints, giving a tautological fit) is structurally harder to trigger here than in a moment-matching formulation.

---

# 11\. Application to the frozen Z-Spin multiplier

Every object of Sections 2–10 was defined and verified without reference to `lambda`. The comparison below is performed once.

## 11.1 The constants

ZS-M1 fixes the i-tetration map `T(z) = i^z` with attracting fixed point `z*` and multiplier `lambda = (i pi/2) z* = f'(z*)`, `|lambda| < 1`. Recomputing at `mp.dps = 40` (ledger rows K1–K3):

z\*      \= 0.4382829367270321116269752 \+ 0.3605924718713854859529405 i     (solves z \= i^z)

lambda  \= \-0.5664173302854644027 \+ 0.6884532271077021305 i

|lambda| \= 0.891513565776047043   \< 1

`Re lambda = -0.566417330285464` agrees with the corpus SSOT value to every printed digit (row K2; source: corpus history entry H-0026). `Im lambda = 0.688453227107702` to the printed precision.

## 11.2 The gate

Reachability threshold (Theorem 17(ii)), row K4:

Psi\_min := arccos( Re lambda ) \= 2.17294837955010601   rad.

Since `Psi = 2 c sin(min(u,pi/2))`, the multiplier is unreachable — for *every* boundary law, at *any* asymmetry, including `A = 1` — unless

2 c sin( min(u, pi/2) )  \>=  2.17294837955010601 .

For `u >= pi/2` this is `c >= c_min` with (row K5)

c\_min \= Psi\_min / 2 \= 1.08647418977505301 ,

which is exactly the phase lower bound `c >= (1/2) arccos(Re lambda)` of ZS-M61 Theorem M61.24, here re-derived independently and extended to an arbitrary support arc as `c >= 1.08647418977505301 / sin u` for `u <= pi/2`. This is a **geometric** obstruction: it does not depend on the state at all, only on the range of the observable.

## 11.3 The price

For `u >= pi/2`, evaluating (10.3) (rows K6, K9). The table lists positive accumulated phases; for general `c` the arc parameter is `Psi = min(2 |c| , pi)` and `A*` depends on `c` only through `|c|`, and note that `A*` depends on `c` only through `|c|` (Theorem 17(iii)), while the *orientation* of the extremal law does depend on `sign(c)` (Theorem 18).

| `c` (positive) | `Psi` | `A*(lambda; c)` | status |
| ----: | ----: | ----: | :---- |
| `< 1.08647418977505301` | `< Psi_min` | — | not realizable |
| `1.08647418977505301` | `2.172948380` | `0.835381287` | CERTIFIED |
| `1.10` | `2.20` | `0.832310663` | VERIFIED |
| `1.20` | `2.40` | `0.809606714` | VERIFIED |
| `1.30` | `2.60` | `0.789157930` | VERIFIED |
| `1.40` | `2.80` | `0.773814576` | VERIFIED |
| `1.50` | `3.00` | `0.765166432` | VERIFIED |
| `>= pi/2` | `pi` | `0.763362818245963536` | CERTIFIED |

The infimum over all accumulated phases and all support arcs is attained for `Psi >= pi`. By Theorem 17(iv) the relevant branch is selected by the sign of `|Re lambda| + |Im lambda| - 1`, and for the frozen target

|Re lambda| \+ |Im lambda| \= 0.566417330285464 \+ 0.688453227107702 \= 1.2548705574 \> 1 ,

so the second branch applies and

A\*\_inf \= ( (1 \- |Re lambda|)^2 \+ (Im lambda)^2 ) / ( 2 (1 \- |Re lambda|) ) \= 0.763362818245963536 .   (11.1)

(Had the target satisfied `|Re lambda| + |Im lambda| <= 1`, the value would instead be `|Im lambda|`. Stating (11.1) without its branch condition was erratum `E-M62-13`; see Remark 17.3.)

For comparison, the elementary bound `d_TV >= |Im lambda| = 0.688453227107702` obtained by testing the odd part of the observable against a single bounded function is weaker by the factor `1.108808541` (row K10).

## 11.4 Consequences

**\[검증됨\] C1 — the boundary phase law cannot be a small perturbation of a symmetric law.** By (11.1), realizing `lambda` requires that at least `76.3362818245963536 %` of the probability mass be oriented, i.e. that more than three quarters of the state must be removed before the remainder is reflection-symmetric. This is not a perturbative regime.

**\[검증됨\] C2 — the odd part of any finite-volume effective boundary action is bounded below.** By (10.9) and row K7,

|| S\_o ||\_{L^infinity}  \>=  artanh( 0.763362818245963536 ) \= 1.00422493384939229 .

This is a quantitative, target-blind requirement on the upstream reduction, and it is the whole of what is established.

**\[가설\] C2' — the size reading.** Version 1.0 added that "in a dimensionless action this is an `O(1)` odd term: it cannot be produced by a small radiative or anomaly-scale contribution". That sentence is **downgraded to a hypothesis**. The bound `|| S_o ||_infinity >= 1.00422493384939229` is a statement about a specific functional of a specific effective action in a specific normalization; excluding a particular generating mechanism additionally requires the coupling normalization, the measure and Jacobian conventions, and the derivation of the effective boundary action itself — none of which is supplied here. See `NC-M62.7`.

**\[검증됨\] C3 — reflection-divergence floors.** With `A = A*_inf` (row K8),

D\_KL( mu || R\#mu )  \>=  2 A^2                \= 1.16544558456   nats     (Pinsker),

D\_KL( mu || R\#mu )  \>=  2 A artanh(A)        \= 1.53317595131   nats     (Cor. 20.1, all measures).

Corollary 20.1 is an imported sharp bound (§10.6, erratum `E-M62-6`), so this floor carries no novelty claim; what is used here is only its numerical value at `A = A*_inf`.

**\[열림\] C4 — the physical reading of `D_KL`.** Calling `D_KL(mu || R#mu)` an entropy production requires identifying `R` with the physically relevant time-reversal operation and supplying a path-space interpretation. That identification is not made here; gate `F-M62.10` stays open.

**\[가설\] C5 — oriented boundary content and the measurement arc.** If the seam reflection is the microscopic orientation-reversing operation relevant to a measurement event, then `A*_inf` is a quantitative lower bound on the oriented boundary content required to generate a complex contraction. The antecedent is exactly the content of the unresolved debt `D-M61-IOTA`, so this reading is conditional.

## 11.5 Non-claims

* **NC-M62.1.** `A*` is a lower bound on a property of *states*. Nothing here shows that the Z-Spin dynamics *selects* such a state. Existence, value, selection and realization remain distinct.  
* **NC-M62.2.** Theorems 19 and 20 concern finite-volume Gibbs laws. They are not claimed for infinite-volume spontaneously selected pure states, where an even action can coexist with an asymmetric state; gate `F-M62.9` stays open.  
* **NC-M62.3.** No statement identifies the abstract Z-register parity basis with `(Re Phi, Im Phi)`. All results are `alpha`\-covariant on the field side and do not use the intertwiner `iota_{Z Phi}`.  
* **NC-M62.4.** `c` is an upstream datum. It was not solved from `lambda`: the family `Lambda_A(c,u)` was defined and verified before `lambda` was loaded, and the comparison is performed once, in §11.  
* **NC-M62.5.** The statement "no Bessel expansion is needed" applies to the specific observable `exp(-2 i c sin phi)`. If the upstream reduction supplies Fourier moments rather than a law, the hierarchy of Sections 4–9 is still the right instrument.  
* **NC-M62.6.** No priority is claimed for any result. The prior-art sweep `D-M62-PRIOR` is open, and `NOT FOUND` is not `DOES NOT EXIST`. In particular the entropy floor of Corollary 20.1 is explicitly credited to the existing literature.  
* **NC-M62.7.** The inequality `|| S_o ||_infinity >= 1.00422493384939229` is not, by itself, an exclusion of any named generating mechanism. Translating a bound on a sup-norm into a statement about radiative, anomalous or topological contributions requires a normalization convention and an effective-action derivation that this paper does not provide (`C2'`, debt `D-M62-ACT`).

## 11.6 Anti-numerology record

quantity                      : A\*\_inf , Psi\_min , c\_min , artanh(A\*)

formula fixed before comparison?: yes \-- Theorems 3, 8, 17, 19, 20 are lambda-free

comparison target             : lambda (frozen upstream by ZS-M1)

null family                   : the whole one-parameter family Lambda\_A(c,u), A in \[0,1\]

search multiplicity           : none \-- no choice of n, u, c, truncation order or dual family was made

                                after seeing lambda; there is no truncation order in the argument

tolerance pre-registered?     : yes \-- mp.dps \= 40 for certified rows; grid tolerances declared per row

hidden-choice ledger          : TV convention (§2.1, locked); reflection axis alpha (covariant, no choice);

                                orbit chart (bijective, Lemma 1); numerical grids (verification only,

                                not used in any proof)

result                        : reachability is possible only above c\_min ; the price is A\*\_inf

status consequence            : the physical judgement stays CONDITIONAL (NC-M62.2), the mathematics is PROVEN

---

# 12\. Falsification gates, open debts, strongest objection

## 12.1 Gates

| Gate | Statement | Status |
| :---- | :---- | :---- |
| `F-M62.1` | if the general framework fails to reproduce ZS-M61 Thm M61.20 at `n = 1`, the formulation is wrong | **passed** (Corollary 10\) |
| `F-M62.2` | a certified primal/dual gap at some feasible datum | **dissolved** — Theorem 6 gives a zero gap unconditionally |
| `F-M62.3'` | an optimizer requiring more than `n + floor(n/2) + 1` orbit atoms, or a degenerate dual defeating §6.2 | **active**; untested for `n >= 4` and on the degenerate strata of Remark 5.3 |
| `F-M62.4` | the full-circle semidefinite programme admits a moment vector with no representing measure | **dissolved** by Carathéodory–Toeplitz |
| `F-M62.4'` | the arc localizing conditions admit a fake sequence with no arc-supported representing measure | **active**; Theorem 14 is conditional on the imported representation |
| `F-M62.5` | no exact result beyond `n = 1` | **partially passed** — Theorem 16 with Theorem 15 gives an exact second-order value on an explicit stratum; a full piecewise formula for `A_2(m_1,m_2;u)` is open (`D-M62-N2`) |
| `F-M62.6` | the harmonic tail is too large to decide reachability | **dissolved** — Theorem 17 contains no truncation |
| `F-M62.7` | the boundary reduction leaves free coefficients matching the number of constraints (ZS-M56 M56.7 trap) | **active**, but reduced: the requirement is one inequality on \` |
| `F-M62.8` | any statement treating the field reflection basis as the Z-register parity basis without `iota_{Z Phi}` | **passed** (NC-M62.3) |
| `F-M62.9` | an even action used to exclude spontaneously selected asymmetric states in an infinite-volume limit | **active** — Theorem 19 and Corollary 20.2 are finite-volume statements (Theorem 20 itself is general) |
| `F-M62.10` | \`D\_KL(mu |  |
| `F-M62.11` | the rescaling `Psi = 2 c sin u` is invalidated by an upstream change in the definition of `c` or `u` | **active**; ledger row I1 is the regression |
| `F-M62.12` | Theorems 2 and 3 applied outside compact, `R`\-invariant support | **active**; extension needs closure/approximation arguments |
| `F-M62.13` | a prior-art item that subsumes Theorem 2, 3, 5, 15 or 17 | **active** — `D-M62-PRIOR`; **fired once already** for Corollary 20.1, which is now credited as imported |
| `F-M62.14` | Theorem 3 applied to a discontinuous observable, or with closed hulls in place of attainable sets | **fired in v1.0, now closed by scope**; regression `N1` |
| `F-M62.15` | the fractional dual (5.1) used without the outer `max{0,.}` | **fired in v1.0, now closed**; regression `N2` |
| `F-M62.16` | the extremizer of Theorem 18 used at `c < 0` with the v1.0 orientation | **fired in v1.0, now closed**; regression `N3` |
| `F-M62.17` | a bound on \` |  |
| `F-M62.18` | a `--quick` run quoted as a reproducibility certificate | **active**; the quick profile prints a runtime banner denying it and records `certificate: false` in the ledger; row `S4` declares the profile |
| `F-M62.19` | block `Y` read as a certification of the theorems rather than of the algebra inside their proofs | **active**; block `Y` is class `C`, class `P` remains empty, and §13.2 states the distinction |
| `F-M62.20` | the observables described as bounded measurable, or a `Psi` written without \` | c |
| `F-M62.21` | a value of `A*` quoted at `Psi >= pi` without its branch condition, or Eq. (8.5) used with one branch only | **fired in v1.0–v1.2, now closed**; guard `M7`, regression `N7` |
| `F-M62.22` | a result whose novelty class survives only because the corresponding classical identity was not looked for | **active**; it has now fired twice (Cor. 20.1, Thm 2). Every remaining `OPEN-NOVELTY` label is to be read as *not yet searched*, not as *new* |
| `F-M62.23` | a manuscript guard that passes because the string it looks for survives somewhere other than the place it is about | **fired in the drafting of v1.3, now closed** by anchoring `M7`; every future guard of this kind must be live-fired in the direction that deletes, not only in the direction that adds |
| `F-M62.24` | a byte hash of the manuscript quoted as *the* identifier of the release, without a transport-invariant digest beside it | **fired in the v1.3 delivery, now closed**; §13.1 prints both, and the digest is what the guards use |
| `F-M62.25` | a manuscript guard that reads the delivered bytes rather than a normal form invariant under the delivery channel | **fired in the v1.3 delivery, now closed**; every guard runs on `transport_norm`, and row `M8` re-runs all of them on an escaped copy and requires agreement |
| `F-M62.26` | a promotional-innovation adjective applied to this paper's own results while `D-M62-PRIOR` is open | **active**; guard `M5` carries the adjective list. Quoted auditor verdicts are exempt by being quotations, and the guard list is chosen so that they do not trip it |
| `F-M62.27` | a semidefinite claim whose only evidence is a row that fails closed when no solver is installed | **fired in audits 1 and 4, now closed** by the solver-free rows `F5`, `F6`; `F1`\-`F4` remain, but they are no longer the whole of the evidence |
| `F-M62.28` | an integrity check that reports *that* something differs without reporting *what* | **fired in audit 5, now closed** by the five part digests and `--identify`; a detector that cannot localise is the identity-level form of `F-M62.23`, and every future integrity check must name the region it is unhappy about |
| `F-M62.29` | two different contents published under one version label, or a version increment used to hide a mathematical change | **active**; every release carries its own whole-document digest, and a patch release must additionally exhibit the *unchanged* part digests of the release it patches. `v1.4.1` and `v1.4.2` do so for parts `B` and `C` |
| `F-M62.30` | an artifact manifest that quotes a hash, a row count or a filename which no row checks | **fired in `v1.4.1`, now closed for the script hash** by `M10`; **permanently open for the ledger hash**, which admits no fixed point and is therefore published as a locator, not as a guarded claim. Every future manifest line must be classified as *guarded* or *locator* when it is added |

## 12.2 Open debts registered by this paper

* `D-M62-PRIOR` — systematic prior-art sweep for Theorems **2, 3, 5, 7, 8, 9, 15, 16, 17** and the orbit identity of Theorem 20\. Search axes: peeling / trimming distance to invariant measures; minimum asymmetry with prescribed moments; involution-constrained truncated moment problems; total-variation projection onto `G`\-invariant measures; Minkowski interpolation of moment bodies; symmetry resource monotones with prescribed data; one-sided polynomial approximation and Markov–Krein index theory (the dual of §5 is a one-sided approximation problem); Chebyshev-system contact bounds for trigonometric families on an arc. The sweep has already produced one correction (Corollary 20.1, erratum `E-M62-6`), which is itself evidence that the remaining `OPEN-NOVELTY` labels are not to be read as novelty claims.  
* `D-M62-ARC` — **conditionally closed** by Theorem 14, pending an independent check of the imported arc representation at the exact truncation orders used.  
* `D-M62-N2` — full piecewise closed form for `A_2(m_1, m_2; u)`. Theorem 5 bounds the orbit support by four, so the remaining task is a finite enumeration of contact patterns.  
* `D-M62-DEG` — Theorem 5 on the degenerate strata of Remark 5.3 and for `n >= 4`.  
* `D-M62-INF` — an analogue of Theorem 19 for infinite-volume spontaneously selected states.  
* `D-M62-XPORT` — **conditionally closed in v1.4.** The release package must survive its delivery channel. Row `M8` establishes invariance under Markdown escaping, iterated to a fixpoint, and under NFKC, zero-width and dash normalisation. It does **not** establish invariance under lossy channels — PDF re-flow, a converter that rewrites tables, an editor that hard-wraps lines — and the digest deliberately ignores all whitespace, so a channel that *merges tokens* would defeat it. Closing this properly requires a persistent archival identifier, which is also what `FINAL` waits on.  
* `D-M62-ACT` — the upstream reduction from the ZS-S14 v2.1 master action to an effective boundary action, and the sign and size of its odd part.

## 12.3 Strongest objection

> *Theorems 19 and 20 are statements about finite-volume Gibbs laws. Spontaneous symmetry breaking is precisely the phenomenon in which a reflection-even action selects, in the infinite-volume limit, a pure state with maximal asymmetry. So the chain (10.9) may simply not apply to the physical situation, and the quantitative requirement on `||S_o||_inf` could be vacuous.*

This objection is correct and is not answered here. It is **bounded by scope**: §10.7 states the chain only for finite-volume Gibbs laws, `NC-M62.2` records the restriction, gate `F-M62.9` keeps it open, and `D-M62-INF` registers the missing theorem. Note that the mathematical core is untouched by the objection: Theorems 17 and 18 are lower bounds valid for *every* state on the arc, so the reachability threshold `c >= c_min` and the price `A* >= 0.763362818245963536` survive regardless of how the state is selected. What the objection removes is only the *upper* bound, i.e. the ability to close the gate negatively from the action alone.

---

# 13\. Verification and reproducibility

## 13.1 Ledger

ARTIFACT\_MANIFEST

paper\_code/version   : ZS-M62 v1.4.2

main\_script          : zs\_m62\_verify\_v1\_4\_2.py

identity-only mode   : python3 zs\_m62\_verify\_v1\_4\_2.py \--identify \[manuscript.md\]

                       Sub-second.  Prints byte hash, whole-document digest and all five part

                       digests, compares each with what the manuscript declares, and exits 1 on

                       any mismatch.  An auditor should run this BEFORE the suite: if it reports

                       a mismatch, the suite is being run against a different document and every

                       downstream verdict is about that document, not about this one.

ledger               : zs\_m62\_verify\_v1\_4\_2.json

manuscript           : DISCOVERED, not hard-coded.  The script takes an optional .md argument;

                       otherwise it globs its own directory for ZS-M62\_v1\_4\_2.md, then ZS\*M62\*.md.

                       This removes the v1.0 dependency on one exact filename (erratum E-M62-5).

manuscript identity  : TWO identifiers, answering different questions.

                       (a) TRANSPORT-INVARIANT DIGEST \-- SHA-256 of the manuscript after NFKC,

                           removal of zero-width characters, unification of dash variants,

                           ITERATED undoing of Markdown backslash escapes, and removal of all

                           whitespace.  This is the identifier of the SCIENTIFIC CONTENT: it is

                           unchanged by the escaping that broke the v1.3 delivery, and it is what

                           every manuscript guard is evaluated against (erratum E-M62-18).

                           It is printed below, INSIDE the manuscript it identifies.  That is

                           possible because the digest is computed as a FIXED POINT: the three

                           manifest lines that identify the release \-- the digest itself and the

                           two artifact hashes beside it \-- are blanked to a canonical

                           placeholder before hashing.  Three and not one, because the ledger's

                           own content records the digest, so a digest covering the ledger hash

                           would have no fixed point.  Everything else in this manuscript \--

                           every theorem, proof, constant, table and gate \-- is covered.  Row M8

                           recomputes the value and fails if the declared one is wrong or absent,

                           so this manuscript verifies its own identity.  Since v1.4.1 the same

                           construction is applied PART BY PART, so a mismatch is localised

                           rather than merely detected; the five part digests are printed below

                           and are checked by the same row.  This is what lets a reader confirm

                           that a release-package patch really did leave the mathematics alone:

                           parts B and C of v1.4.1 must digest to the same values as v1.4.

                       (b) sha256(manuscript bytes) \-- the identifier of ONE delivered file.  It

                           is fragile by design: any channel that touches a byte changes it, and

                           no file can contain its own byte hash, so it is NOT embedded here;

                           the script prints it at runtime and it is quoted in the delivery note.

                           A mismatch in (b) with (a) intact means the delivery was re-encoded,

                           not that the paper changed.  Gate F-M62.24 forbids quoting (b) alone.

dependencies         : numpy, scipy, mpmath, sympy, and OPTIONALLY cvxpy (CLARABEL or SCS).

                       Without cvxpy, rows F1-F4 fail closed and the run exits 1, but the

                       semidefinite content of Theorems 13 and 14 is still verified by the

                       solver-free rows F5 and F6, which use numpy eigenvalues only

                       (erratum E-M62-19).  sympy is REQUIRED for the symbolic block Y.

runtime              : CPython 3.11, numpy 2.4.4, scipy 1.17.1, cvxpy 1.9.2 (CLARABEL),

                       mpmath 1.4.1, sympy 1.14.0

profiles             : FULL   python3 zs\_m62\_verify\_v1\_4\_2.py          50-75 s, ledger

                              certificate=true.  This is the only profile that may be quoted.

                       QUICK  python3 zs\_m62\_verify\_v1\_4\_2.py \--quick  \~25 s, reduced sample

                              counts, ledger certificate=false, written to a SEPARATE file

                              zs\_m62\_verify\_v1\_4\_2\_quick.json so it can never overwrite the

                              certificate, and a runtime banner denying certificate status.  Added because the second audit could not

                              finish the full run inside a 180 s budget (erratum E-M62-11).

                              A quick run is a smoke test, not a public certificate.

precision            : mpmath mp.dps \= 40 for the arbitrary-precision class C rows; block Y is

                       exact symbolic computation with no tolerance at all

random seeds         : numpy PCG64 seeds 620001 (main), 620019 (Gibbs block), 620041 (audit block N)

one-command run      : python3 zs\_m62\_verify\_v1\_4\_2.py

expected row count   : 91 rows, 0 FAIL, exit 0   (identical in both profiles)

sha256(script)       : 1dbdc5cb6f25bee977af34af88904db4d827b14cf1160356d3c067d29c7ff75b

sha256(ledger, FULL) : b22ef8c008561551a5173ec5d53c96e5d1fd3e1342b3d00c44648b22346c77ae

transport digest     : df2d8771cf797a6082b1a8e6bc3921e563a1f0aa2b9e5a098e8acfda587b7f28

part digest A        : 1299c39f65401dfcf4e3db66d7aea36656c229123ceccbd86e79b70da0f5c7b0

part digest B        : d14aaa5e9dc138aef9814dfaadacc1d3058cb0187239be1202fc3073c1900c9e

part digest C        : 3b6002cbd27d48e1b17b6547c20142bd0b57fe7a63f360ba5d0de099e347a95a

part digest D        : 8de952775927c5a8e9d4077e03ca7c9354429c78f36ff0582091fd596afeb945

part digest E        : 4fa87665a5a12234015b44006125d975236da1930b7b093dde61cb2a5cadb6d1

label-blind rule     : the digests above ignore the lines that NAME the release \-- the three

                       hash lines, paper\_code/version, verification artifact, main\_script and

                       ledger.  The hash lines must be ignored because they are fixed-point

                       lines.  The label lines must be ignored for a different and less obvious

                       reason, found by this instrument on its own first run: relabelling v1.4

                       as v1.4.1 moved the digest of part B \-- Sections 2-9, the mathematics \--

                       because the Section 2.3 dependency freeze names the release.  An

                       identifier of CONTENT must not move when only the LABEL moves, or the

                       sentence "the mathematics is unchanged" can never be expressed.  The

                       residual is closed by row M8, which additionally requires all four

                       version-label sites in the manuscript to agree.

v1.4 comparison      : under that rule, parts B and C of v1.4 digest to

                       B d14aaa5e9dc138aef9814dfaadacc1d3058cb0187239be1202fc3073c1900c9e

                       C 3b6002cbd27d48e1b17b6547c20142bd0b57fe7a63f360ba5d0de099e347a95a

                       and MUST be identical above.  That equality is the machine-checkable

                       form of the claim "v1.4.1 changed no mathematics"; if it fails, the

                       claim is false and the label is wrong.  Parts A, D and E differ from

                       v1.4 by construction: they carry the v1.4.1 notice, the register entry

                       E-M62-22, the fifth-audit record, the new gates and the version history.

                       The v1.4 whole-document digest as PUBLISHED in v1.4, retained for the

                       record: cf7fd64efd463638950b201589486752d5104a1e16855ad00c5911b453637c33

                       (that value predates the label-blind rule and is therefore not

                       comparable with the whole-document digest above; the part digests are)

re-run reproducibility: ledger JSON byte-identical on a second run at the same profile; the ledger

                       is independent of manuscript edits (the manuscript digest is printed to

                       stdout, not stored)

fail-closed          : row-count guard, class-census guard, AST self-audit (no literal-True in

                       evidence rows), manuscript-integrity guards, scope-consistency guard,

                       anchored statement guard, the self-identifying and PART-LOCALIZING

                       digest row M8, the self-referential guard-invariance row M9, and the

                       cross-artifact script-hash row M10; any failure returns exit 1

known limitations    : the LEDGER hash quoted above is NOT checked by any row, and cannot be:

                       the ledger records the outcome of every row, so a row that verified the

                       ledger's own hash would have no fixed point.  It is a locator, not a

                       guarded claim.  The SCRIPT hash is guarded, by row M10 (E-M62-23);

                       grid linear programmes are discretizations, tolerances declared per row;

                       semidefinite rows use solver default tolerances; class P is not used;

                       block Y certifies the ALGEBRA inside proofs, not the proofs;

                       the transport digest ignores whitespace entirely, so a channel that MERGES

                       tokens would defeat it (D-M62-XPORT); the script is not a proof checker

license              : to be assigned with the archival release

Blocks: `A` conventions and degenerate guards · `B` the reduction and its three independent implementations · `C` duality and the closed-form certificate · `D` atomicity contact counts · `E` the first-order solution, extremizers, gradients and the ill-conditioned corner · `F` semidefinite forms on the circle and on arcs, of which `F5` and `F6` are **solver-free** · `G` the odd-data-only problem and `Y_2(pi)` · `H` hierarchy convergence · `I` the multiplier price and the explicit extremal law · `J` Gibbs identities · `K` Z-Spin constants and the gate · **`N` audit-driven regressions (one row per finding of the first audit)** · **`Y` exact symbolic certification of proof algebra** · `M` manuscript-integrity, scope-consistency and statement guards, of which `M8` is the **self-identifying** digest row and `M9` the **self-referential** guard-invariance row · `S` self-audit and profile declaration.

## 13.2 What the ledger does *not* do

It does not prove any theorem. Class `P` is deliberately absent. Rows of class `D` and `T` are declarations and controls and are excluded from the evidence count. Random-sample rows are `V` or `W`, never a substitute for the written proofs of Sections 3–10.

Block `Y`, new in v1.2, requires a sharper statement than the rest. Its nine rows are exact symbolic computations in a computer-algebra system: they establish, with no tolerance and no sampling, that specific algebraic identities used inside the proofs hold identically in their free variables — for example that `C(t) + S(t) = a_0 + kappa cos(t - t_1)`, that `C(t_1) + S(t_1) = 1` for **every** admissible `(A, t_1, gamma)` rather than at tested points, that `Q(R,d)` is a root of the tangency equation, that `phi''(v)` has the claimed sign, and that `h = -tanh S_o` in the Gibbs case. This closes off a class of error — an algebraic slip inside an otherwise correct argument — that sampling can miss. It does **not** certify the logical steps: the case analyses, the quantifier structure, the appeals to separation, compactness, Carathéodory, Jensen and Chebyshev, and the counting arguments of Theorem 5 are checked only by reading. The honest summary is that v1.2 has certified the algebra of the proofs and none of their logic, and that no proof-assistant formalization or qualified-human review exists.

The class assignment follows from this: block `Y` is `C` (certified computation), not `P`. `F-M62.19` is the gate against reading it otherwise.

Two further boundaries are new in v1.4 and are stated here rather than left to be discovered.

**Solver dependence.** Rows `F1`–`F4` call a semidefinite solver and fail closed without one; two of the four audits ran in exactly that environment, so for two of four audits the semidefinite section of this paper carried *no positive evidence at all* — only four correctly-reported absences. Rows `F5` and `F6` remove that. They are solver-free: `F5` takes the optimum of an independent grid linear programme and checks, by symmetric eigenvalue decomposition alone, that the induced Toeplitz matrices `T_n[A;P]` and `T_n[1-A;Q]` are positive semidefinite with `Q` real and `P + Q = m`, which is the *forward* direction of Theorem 13; `F6` builds arc-supported measures, checks that the localizing Toeplitz matrix of `g_u = cos t - cos u` is positive semidefinite, and checks that the same measures perturbed by mass outside the arc are detected as infeasible, which is the *discriminating* content of Theorem 14\. What the solver rows still add is the converse and the numerical value; what the solver-free rows guarantee is that a reader without `cvxpy` is not left with an empty section. The distinction is recorded as gate `F-M62.27`.

**Localisation.** An integrity check has two jobs and they are not the same job: *detect* a difference, and *characterise* it. Through `v1.4` this manuscript did the first and not the second, and the fifth audit walked straight into the gap — `M8` correctly refused a drifted copy and then had nothing more to say, so neither the auditor nor the author could tell whether the difference was a reformatted table or a changed theorem. Five part digests fix that at the granularity that matters here, because the parts are chosen along the paper's own fault line: `B` and `C` are the mathematics and the numbers, `A`, `D` and `E` are apparatus. A patch release is then a *checkable* claim rather than a promise — `v1.4.1` asserts that it changed no mathematics, and the manifest publishes the `v1.4` digests of parts `B` and `C` so that assertion can be refuted in one command. What this does **not** give is a diff: a mismatch names a part, not a line, and a part is still tens of pages. Finer granularity is available by the same construction and is deliberately not taken here, because a per-section digest table would itself become a large block of the manuscript that no reader checks.

One consequence of building this had to be absorbed rather than argued away, and it arrived on the instrument's first run. The digests are taken **label-blind**: the lines that *name* the release — the version string and the artifact filenames, wherever they occur — are blanked along with the three hash lines. Without that rule, relabelling `v1.4` as `v1.4.1` moved the digest of part `B`, the Z-Spin-free mathematics, because the dependency freeze of §2.3 names the release; and an identifier of content that moves when only the label moves cannot express the sentence this patch exists to assert. Blanking those lines opens a hole of its own — the digest then cannot see a version label at all, so a manuscript whose title and dependency freeze disagreed about which release it is would pass — and that hole is closed inside the same row, which requires the four version-label sites to agree. This is the ordinary shape of the work: each repair opens a smaller gap, and the discipline is to name the smaller gap in the same breath rather than to stop when the first one closes.

**Outward reference.** `M10` is the only manuscript row that checks a claim about a *different* file, and it exists because the absence of such a row was invisible for three versions. The manifest is a list of assertions, and until `v1.4.2` they fell into two undistinguished kinds: those about this document, which `M8` and `M9` cover, and those about the script, the ledger and the environment, which nothing covered. The script hash is now guarded. The ledger hash cannot be — a row verifying it would be recorded in the file it verifies — and so it is labelled a locator in the manifest itself. The general rule is `F-M62.30`: classify each manifest line as guarded or locator when you write it, and name the row if it is guarded.

**Self-reference and its limit.** Rows `M8` and `M9` have this manuscript's own verification apparatus as their subject, and it is worth being exact about what that can and cannot establish. `M8` closes a fixed point: the manuscript declares a transport-invariant digest — and, since `v1.4.1`, one per part — and each is recomputed with the declaring lines blanked, so the declaration is checkable rather than circular. `M9` closes a *conjugation*: for the escaping map `E`, it requires `guard(E(text)) = guard(text)` for every manuscript guard, and `digest(E(text)) = digest(text)`. Neither row can establish that the guards test the right thing — a suite of eight guards that all returned `True` unconditionally would satisfy both. What they establish is that the suite is *invariant under the delivery channel*, which is precisely and only the defect the fourth audit found. The guards' adequacy is still carried by the live-fire table §13.3, where each of them is made to fail on demand.

## 13.3 Guard live-fire test

Guards that never fire are not guards. Thirty-five attacks have been executed across v1.1–v1.4.2; every one behaved as designed, and the four that did *not* behave as designed on first execution are recorded below with their failed outcome, because that is where the errata came from. Attacks `A9a`–`A13` are the audit-driven additions; `A1`, `A6`–`A8` were carried over from v1.0 and re-executed against v1.1.

| \# | attack | expected | observed |
| :---- | :---- | :---- | :---- |
| `A1` | change one load-bearing numeral in the manuscript by one unit in the last place | `M1` fires | `M1` FAIL, exit 1 |
| `A2` | append a retracted programme-level sentence | `M2` fires | `M2` FAIL, exit 1 |
| `A3` | append priority language | `M5` fires | `M5` FAIL, exit 1 |
| `A4` | the same sentence obfuscated with emphasis and inline-code spans | `M2` fires | `M2` FAIL, exit 1 |
| `A5` | delete the manuscript | `M1`–`M5` fire | five FAIL, exit 1 |
| `A6` | delete one ledger row | `S3` fires | `S3` FAIL, exit 1 |
| `A7` | retype a control row as evidence while keeping its literal `True` | `S1` fires | `S1` FAIL, exit 1 |
| `A8` | perturb the closed form of Theorem 8 by a relative `1e-7` | scientific regression fires | `C2`, `I3`, `N3` FAIL, exit 1 |
| `A9a` | escape the convention sentence with Markdown backslashes (`d\_TV`, `sup\_A`) | **no** spurious failure | exit 0 — the v1.0 defect `E-M62-4` is repaired |
| `A9b` | re-run attack `A2` with a backslash inserted inside three words of the retracted phrase | `M2` fires | `M2` FAIL, exit 1 |
| `A10` | rename the manuscript to `ZSM62_v1_1.md` | run still succeeds | exit 0 — `E-M62-5` is repaired |
| `A11` | revert the orientation of Theorem 18 to the v1.0 convention | `N3` fires | `N3` FAIL, 70/71, exit 1 |
| `A12` | drop the outer `max{0,.}` from the dual evaluation | `N2` fires | `N2` FAIL, 70/71, exit 1 |
| `A13` | simulate a missing semidefinite solver (the first auditor's environment) | exactly four `F` rows fail, row count preserved | `F1`–`F4` FAIL, exit 1 — `E-M62-8` is repaired |
| `A14` | revert §1.1 to the superseded "bounded measurable" wording | `M6` fires | `M6` FAIL, exit 1 |
| `A15` | rewrite one `Psi` in the Abstract without `|c|` | `M6` fires | `M6` FAIL, exit 1 |
| `A16` | perturb the `Q(R,d)` closed form used by the symbolic block | `Y5` fires exactly, with no tolerance | `Y5` FAIL, exit 1 |
| `A18` | restore the v1.2 single-branch form of Theorem 17(iv) in the code | `N7` fires | `N7` FAIL, exit 1, `certificate: false` |
| `A19` | delete the branch condition from the Theorem 17(iv) **statement** | `M7` fires | first attempt: **did not fire** (see `E-M62-17`); after the guard was anchored: `M7` FAIL, exit 1 |
| `A20` | retype the Theorem 2 **table row** back to `OPEN-NOVELTY` | `M7` fires | first attempt: **did not fire**; after anchoring: `M7` FAIL, exit 1 |
| `A21` | make one symbolic identity of block `Y` false by a factor `101/100` | `Y` rows fire with no tolerance | `Y1`, `Y2`, `Y3` FAIL, exit 1 |
| `A22` | change the branch-check numeral of §11.3 in the last digit | `M1` fires | `M1` FAIL, exit 1 |
| `A17` | run `--quick` | passes, writes a *separate* ledger file, denies certificate status | exit 0; banner printed; `zs_m62_verify_v1_4_quick.json` created with `certificate: false`; the full ledger is never touched |
| `A23` | Markdown-escape the **entire** manuscript, as the v1.3 delivery channel did, and run the v1.3 verifier against it | reproduce the fourth audit's failure | `M7` FAIL, `85/86`, exit 1 — the auditor's finding reproduced exactly |
| `A24` | the same fully escaped manuscript, v1.4 verifier | **no** spurious failure; digest unchanged | `90/90`, exit 0; the declared and recomputed digests are both `8217eab5…`, identical to the unescaped file; `M9` detail records `disagreements = []` |
| `A25` | **doubly** escape the manuscript (apply the escaping map twice) | `M9` fires if any guard's verdict moves | first attempt: `M9` **FAIL** — `normalise()` undid one escape level where two were present; after `normalise()` was made to reuse the iterated `de_escape`: `90/90`, exit 0 |
| `A26` | corrupt one hex character of the declared transport digest | `M8` fires, and only `M8` | `M8` FAIL, `89/90`, exit 1; the detail prints the declared and recomputed values side by side |
| `A27` | delete the `transport digest` line from the manifest | `M8` fires | `M8` FAIL, `89/90`, exit 1, detail `declared = <absent>`; note the recomputed value also moves, since deleting a line changes the content the digest covers |
| `A28` | reproduce the Theorem 17 statement anchor a second time in the manuscript | `M7` fires on anchor non-uniqueness | first attempt: **did not fire** (the v1.3 guard took the first occurrence); after the uniqueness requirement was added: `M7` FAIL with `hits = ['Theorem 17 statement anchor occurs 2 times, expected exactly 1']`, exit 1 (`M8` also fires, correctly: the probe changed the content) |
| `A30` | alter one character in Section 13 only (part `D`) and re-run | `M8` fires **and names part `D`**; parts `A`, `B`, `C`, `E` still match | `M8` FAIL, `89/90`, detail `DRIFT LOCALISED TO PART(S) ['D']` |
| `A31` | alter one character in Section 8 only (part `B`, the mathematics) and re-run | `M8` fires and names part `B` — the case that must never be confused with a bookkeeping edit | `M8` FAIL, detail `DRIFT LOCALISED TO PART(S) ['B']` |
| `A32` | run `--identify` against the canonical manuscript, then against a drifted copy | exit 0 with `identical to the verified manuscript`; exit 1 naming the part, in under a second | both observed; measured `0.57 s` wall clock, no evidence row executed |
| `A33` | rename a top-level section so a part boundary disappears | `M8` fires on the boundary rather than silently absorbing the region into its neighbour | `M8` FAIL, `89/90`; detail reports `DRIFT LOCALISED TO PART(S) ['C', 'D']` — the two parts that merged — **and** `boundary problem: '(?m)^# 12\. ' occurs 0 times`, which is the diagnosis rather than the symptom |
| `A34` | change the version label at one of its four sites only, leaving the other three | `M8` fires on label inconsistency — this is the hole the label-blind digest rule would otherwise open | `M8` FAIL, detail `version labels disagree` |
| `A35` | corrupt one hex character of the declared `sha256(script)` | `M10` fires; nothing else moves, since the hash line is blanked from every digest | `M10` FAIL, `90/91`, exit 1, detail printing declared against actual. Re-run against the **`v1.4.1`** artifact pair, the same corruption produces **no failure at all** — which is the erratum |
| `A29` | uninstall the semidefinite solver and run again | exactly four `F` rows fail; the solver-free rows still pass; the row count is preserved | `86/90`, `F1`–`F4` FAIL, `F5` and `F6` PASS in **both** profiles — the semidefinite section retains positive evidence instead of four reported absences |

Attacks `A1`–`A13` were executed in the full profile; `A14`–`A17` in the quick profile, which exercises the same guards with reduced sample counts. Attacks `A23`–`A29` are the v1.4 additions and were executed in the quick profile, except `A29`, which was executed in both. Attacks `A30`–`A34` are the v1.4.1 additions and were executed in the quick profile; `A32` runs no profile at all. `A35` is the v1.4.2 addition and was executed against both the `v1.4.1` and the `v1.4.2` pair, because the contrast between them *is* the evidence.

Four of these deserve comment.

`A8` is the mathematical stress test: a perturbation four orders of magnitude below the coarsest declared tolerance is caught, because the dual certificate and the extremal construction are cross-checked against each other rather than against a stored constant. In v1.1 it now also trips `N3`, which is a second independent path to the same defect.

`A9a` and `A9b` are the two halves of the guard defect that the independent audit found in v1.0: the normaliser did not undo Markdown backslash escapes, so escaped text produced a *false* failure of `M4` (`A9a`) while an attacker could have used the same escapes to *hide* forbidden text from `M2` (`A9b`; the attack string is not reproduced here, because the repaired guard would then fire on this very manuscript — as it did on the first draft of this table). One fix repairs both directions, and both directions are now tested.

`A13` reproduces the first auditor's environment. In v1.0 a missing solver caused `F1` to fail and suppressed `F2`–`F4`, which additionally broke the row-count guard — one cause reported as two unrelated defects. From v1.1 on, the row count is invariant and exactly the four solver-dependent rows fail.

`A19` and `A20` are recorded with their first, *failed* outcome because that failure is the point. The guard `M7` was written as a global substring test, and a global substring test cannot localise: deleting the branch condition from the theorem statement left it standing in Remark 17.3, §11.3, the register and the appendix, so the guard saw nothing; likewise for the novelty class of Theorem 2\. `M7` is now **anchored** — it reads the text between the bolded Theorem 17 statement heading and the opening words of its proof, and the single table line beginning `| Thm 2 |` — and both attacks fire. (In v1.4 the anchor is additionally required to be *unique*; see `E-M62-21`.) This is erratum `E-M62-17`, self-detected while live-firing the guards written for `E-M62-13` and `E-M62-14`. The general lesson is the one already learned in v1.1 with the escaped text: a guard that is not tested is a guess, and a guard tested only in the direction where it happens to work is worse than a guess.

`A18` is the regression for the error the third audit found. It is worth noting what would *not* have caught it: every numerical row of v1.2 passed, because none of them evaluated the published formula of Theorem 17(iv) — the code used the correct piecewise `A_1` throughout, and only the prose was wrong. `N7` closes that gap by testing the *published statement* against the *implementation*, and `M7` closes it in the other direction by testing that the manuscript still carries the branch condition. A statement that no row evaluates is a statement no ledger can defend.

`A17` closes the obvious failure mode of the quick profile: a smoke test that silently overwrote the certificate ledger would let a short run masquerade as the long one. The quick profile therefore writes to its own filename and marks the ledger `certificate: false`; the guard against quoting it anyway is `F-M62.18`.

`A23`–`A25` are the reason this version exists, and they are recorded in the order they were run because the order is the argument. `A23` reproduces the fourth auditor's failure against the *previous* artifact, which establishes that the finding was about the delivery and not about the auditor. `A24` shows the repair works in the direction that matters. `A25` is the one that earned its place: applying the escaping map twice made `M9` fail, because `normalise()` undid one level of escaping where two were present — a defect *in the repair for `E-M62-18`*, found by the self-referential row written to close `E-M62-18`, before any auditor saw it. That is the whole case for self-referential verification, and it is a weak case made honestly: the row did not find a deep error, it found a shallow one, but it found it in the only place a guard suite is systematically blind, namely itself.

`A28` is the same lesson one level up. Writing the v1.4 prose introduced a second copy of the Theorem 17 statement anchor into the manuscript; the anchored guard of v1.3 took the first occurrence and so kept working *by the accident of document order*. The guard now requires the anchor to occur exactly once, and the contribution-table row for Theorem 2 likewise. An anchor that is not unique is not an anchor — this is erratum `E-M62-21`, and it is `E-M62-17` recurring in a new disguise, which is itself the evidence that the class of defect is not yet exhausted.

`A30`–`A33` are the localisation tests, and the pair `A30`/`A31` is the point of the whole patch. Both attacks change exactly one character; the old guard would have returned the same verdict for both, namely *the digest does not match*. The new guard distinguishes a stray edit in the audit record from an edit to the closed form of Theorem 8, which is the distinction a reader actually needs in order to know whether to keep reading. `A33` covers the failure mode introduced by the repair itself: parts are defined by section headings, so a renamed heading could have made two parts silently merge, and the boundary count is therefore part of the check rather than an assumption of it — the same discipline `E-M62-21` imposed on the statement anchors.

`A35` is the shortest entry in the table and the most uncomfortable. It changes one character of a hash that the manuscript prints about the script, and against the `v1.4.1` artifact pair — the pair that had just added a self-identifying digest, a guard-invariance row and a sub-second identity mode — **nothing happens**. Ninety rows pass. The lesson is not that a check was forgotten; it is that *self*\-reference has an edge, and the edge is where the document stops talking about itself and starts talking about something else. Three versions of increasingly careful self-verification did not reach across it, because they were not looking outward. `F-M62.30` generalises the response: a manifest line is either *guarded* by a named row or declared a *locator*, and it must be classified at the moment it is written.

`A16` is the sharpest test in the table. Attack `A8` perturbs a formula by `1e-7` and is caught by numerical rows at their declared tolerance; `A16` perturbs the same kind of object and is caught by a **symbolic** row, which has no tolerance to hide inside: a wrong closed form simply fails to satisfy the defining equation identically. That is the specific value block `Y` adds over sampling.

## 13.4 Reproduction

Place `zs_m62_verify_v1_4_2.py` and this manuscript in the same directory and run the script. **Run `--identify` first**: it takes under a second, and if it reports a mismatch then the suite you are about to run is describing a different document from the one this manuscript is about. The manuscript-integrity block re-reads the manuscript, checks that every load-bearing numeral printed here is the one the script computes, checks the absence of retracted programme-level phrasing and of promotional-innovation adjectives, verifies the manuscript's declared transport-invariant digest against a fixed-point recomputation, re-runs the whole guard set on a synthetically escaped copy and requires the verdicts to agree, and fails closed if the manuscript is missing.

Every manuscript check runs on the **transport-invariant normal form**, not on the delivered bytes. This matters for reproduction: if the copy you hold has been Markdown-escaped, re-encoded to NFC/NFD, or had its dashes or whitespace rewritten by a mail client, a converter or an editor, the guards will still pass and the transport digest printed by the script will still match the one in §13.1. The byte-level SHA-256 will not match, and that is expected — see the *manuscript identity* entry of the manifest. If the transport digest does **not** match, the content has changed; `--identify` will name the part, and the right response is to report which part rather than to work around it. If the part named is `A`, `D` or `E`, the difference is in apparatus; if it is `B` or `C`, the difference is in the mathematics or in the Z-Spin numbers, and nothing downstream should be quoted until it is resolved.

---

# 14\. Prior art and novelty positioning

The following external mathematics is used or is adjacent, and is treated as imported. No claim is made that any of it is reproduced or improved here.

* **Extreme points of moment sets.** I. Pinelis, *On the extreme points of moments sets*, arXiv:1204.0249. Finite atomicity under finitely many generalized moment constraints. Used as the baseline against which the reflection-coupled bound of Theorem 5 must be compared; the generic bound is `2n+1` and Theorem 5 improves it to `n + floor(n/2) + 1`, so the improvement — not the atomicity — is what is contributed.  
* **Extreme points and faces in the moment problem.** D. Henrion, M. Kružík, S. Weis, arXiv:2606.21391. Current baseline for face structure of moment-constrained measure sets.  
* **Total-variation extremum problems with linear constraints.** C. D. Charalambous, I. Tzortzis, S. Loyka, T. Charalambous, *Extremum Problems with Total Variation Distance and their Applications*, arXiv:1301.4763. Baseline for total-variation optimization with linear functional constraints. The present problem differs in that the second argument of the distance is the *image of the optimization variable under a fixed involution*, so the objective is not linear in `mu`.  
* **Truncated trigonometric moment problem, Carathéodory–Toeplitz.** Classical; used verbatim in Theorem 13\.  
* **Frequency-selective Vandermonde decomposition of Toeplitz matrices.** Z. Yang, L. Xie, arXiv:1605.02431. Interval-supported spectral measures, localizing Toeplitz conditions; the arc representation used in Theorem 14 belongs to this circle of results.  
* **Toeplitz, Hankel, de Branges and truncated matrix moment problems.** K. Dhara, H. Dym, arXiv:2412.11522.  
* **Resource theory of asymmetry / trace-norm asymmetry.** Adjacent but different: that literature measures the asymmetry of a *given* state, whereas the present problem is the inverse one — the minimum asymmetry over all states with prescribed data.  
* **Overlapping coefficient / Scheffé identity.** `d_TV(P,Q) = 1 - integral (p ^ q)`, classical. This is the imported core of Theorem 2 (second proof, §3.2): the peeling identity is its involution specialization, the only added observation being that `mu ^ R#mu` is automatically `R`\-invariant. Verified directly in ledger row `N8`.  
* **Trimming and contamination.** P. C. Álvarez-Esteban, E. del Barrio, J. A. Cuesta-Albertos, C. Matrán, *Similarity of samples and trimming*, Bernoulli **18** (2012) 606–634, arXiv:1205.1950, and the surrounding literature on `alpha`\-trimmed common cores. Supplied by the third audit as the systematic development of the same circle of ideas. **Its exact theorem statement has not been read at source in preparing this version**, so it is cited as a locator and not relied upon; the retyping of Theorem 2 rests on the overlapping-coefficient identity, which is verified here. Closing this pointer is part of `D-M62-PRIOR`.  
* **Sharp Jeffreys-versus-total-variation bound.** G. L. Gilardoni, *On the minimum f-divergence for given total variation*, C. R. Acad. Sci. Paris 343 (2006) 763–766, doi:10.1016/j.crma.2006.10.027; restated with the explicit Jeffreys corollary in I. Sason and S. Verdú, *Tight bounds for symmetric divergence measures and a refined bound for lossless source coding*, IEEE Trans. Inform. Theory 61 (2015), arXiv:1403.7164. Used in §10.6: for an involution `J(mu, R#mu) = 2 D(mu || R#mu)`, so the sharp bound `J >= 2 eps log((1+eps)/(1-eps))` specializes to Corollary 20.1. The constant was checked here by direct minimization of `J` at fixed total variation over two-, three- and four-point pairs, which returns `4 eps artanh eps` and is saturated by the two-point involution pair.

**Second partial sweep (v1.2).** An additional independent search was performed for results directly subsuming the combination contributed here. It returned `NOT_FOUND`. Per the corpus rule this is recorded as evidence of *search effort*, not of novelty: `NOT_FOUND` is not `DOES NOT EXIST`, and the sweep `D-M62-PRIOR` remains open. The one item the sweeps have actually settled went the other way — Corollary 20.1 was retyped from contributed to imported.

**Positioning.** The contributed elements are: the peeling identity (Theorem 2\) and the resulting reduction of the whole problem to a nested Minkowski threshold (Theorem 3); the unconditional strong duality that follows (Theorem 6); the reflection-coupled atom count (Theorem 5); the complete first-order solution with a hand-checkable dual certificate (Theorems 7–11); the identification of the naive odd dual bound as an exact gauge with a sharpness criterion (Theorem 15\) and its second-order closed form (Theorem 16); and the transport of the multiplier problem onto the first-order problem (Theorems 17–18) together with the Gibbs identities (Theorems 19–20). Each is marked `OPEN-NOVELTY` in §1.4 pending the sweep `D-M62-PRIOR`. After the retyping of Corollary 20.1 **and of Theorem 2**, the external-novelty question rests on Theorems 3, 5, 7–9 and 15–17; the orbit identity (10.7) of Theorem 20 is a further candidate, but its Gibbs form is elementary enough that a prior occurrence would not be surprising.

---

# 15\. Audit record and correction register

## 15.1 Correction register

Severity follows the project taxonomy: *editorial* (no science), *scope correction* (status or range of a theorem), *mathematical correction* (proof or result), *retraction* (claim withdrawn), *artifact correction*.

| ID | Severity | Location | What was wrong | What the correcting version does | Regression |
| :---- | :---- | :---- | :---- | :---- | :---- |
| `E-M62-1` | **mathematical correction** | Thm 3, Def. 4.1 | The master theorem was stated for bounded measurable `Phi` with `M_Phi := cl conv Phi(Omega)`. That statement is false: a point of the closed hull need not be the barycentre of any probability measure. | Standing hypothesis `(H-CONT)`; Lemma 4.2 identifies the attainable sets; Theorem 3 assumes `Phi` continuous; Proposition 3.2 gives the general bounded measurable version with attainable sets and `inf`; Remark 3.3 exhibits the counterexample. All applications in this paper are continuous. | `N1` |
| `E-M62-2` | **mathematical correction** | Thm 6, Eq. (5.1) | The fractional dual omitted the outer `max{0,.}` and could return a negative number, which is not a total-variation distance. | (5.0) split out as the feasibility condition; (5.1) corrected; Remark 6.2 gives a three-point counterexample; Remark 6.3 delimits what was unaffected. | `N2` |
| `E-M62-3` | **mathematical correction** | Thm 18, Eq. (10.4) | The orientation of the extremal atom was `sign(-Im lambda)`, valid only for `c > 0`; at `c < 0` the construction realizes `conj(lambda)`. | Orientation bookkeeping made explicit as (10.3a); `sgn = -sign(c) sign(Im lambda)` in (10.4a). Theorem 17 was never affected. | `N3` |
| `E-M62-4` | artifact correction | verifier `normalise()` | Markdown backslash escapes (`d\_TV`, `sup\_A`) survived normalisation, so guard `M4` could be walked past; the audit's independent run reported `M4` FAIL for exactly this reason. | `normalise()` now removes backslash escapes; attack `A9` live-fire tests it. | live-fire `A9` |
| `E-M62-5` | artifact correction | verifier manuscript path | One filename was hard-coded, so a renamed attachment made the advertised one-command run fail. | The manuscript is discovered: optional `.md` argument, then a glob of the script directory. | live-fire `A10` |
| `E-M62-6a` | scope correction | Thm 20 | The reflection-entropy identity was stated only for finite-volume Gibbs laws. | Upgraded to arbitrary measures via the orbit density `h`; the Gibbs statements become Corollary 20.2. | `N4` |
| `E-M62-6b` | **retraction (novelty)** | Thm 20 / Cor. 20.1 | The floor `D_KL >= 2 A artanh A` was labelled `OPEN-NOVELTY`. | Retyped `IMPORTED / SPECIALIZED`: it is the involution specialization of the sharp Jeffreys-versus-total-variation bound of Gilardoni, restated by Sason and Verdu. The proof given here is an independent short derivation, not a new inequality. | `N6` |
| `E-M62-7` | scope correction | §11.4 C2 | "An `O(1)` odd term cannot be produced by a small radiative or anomaly-scale contribution" was carried at `[검증됨]`. | Split into `C2` (`[검증됨]`, the inequality) and `C2'` (`[가설]`, the size reading); recorded as `NC-M62.7` and gate `F-M62.17`. | — |
| `E-M62-8` | artifact correction | verifier Block F | A missing solver made `F1` fail *and* suppressed `F2`–`F4`, so one cause produced two failures and broke the row-count guard. | Block F always emits four rows; a missing solver now produces exactly four explicit fail-closed rows. | — |
| `E-M62-9` | editorial (scope wording) | §1.1 | The Introduction still described the observables as "bounded measurable" after `(H-CONT)` had been declared in the scope declaration, so a reader could re-acquire the v1.0 scope from the Introduction alone. No theorem was affected. | §1.1 now says *continuous*, points at `(H-CONT)`, at Remark 3.3 and at Proposition 3.2. | guard `M6` |
| `E-M62-10` | editorial (notation) | Abstract, §11.3, row `I1` | The Abstract wrote the rescaled arc parameter with `c` where the general theorem needs \` | c | `. The` I1`claim string had the same slip, and rows`I1`,` I2`sampled only positive`c\`. |
| `E-M62-11` | artifact correction | verifier runtime | The full suite did not finish inside the second auditor's 180-second budget, so the advertised result could not be independently reproduced in that environment. | A documented `--quick` profile (\~30 s) with reduced sample counts, an explicit runtime banner denying certificate status, `certificate: false` in the ledger, and row `S4` declaring the profile. The `FULL` profile remains the only quotable one. | row `S4`, gate `F-M62.18` |
| `E-M62-12` | verification strengthening | new block `Y` | The ledger checked numerics and witnesses but nothing symbolic, so an algebraic slip inside a proof would be caught only if sampling happened to hit it. | Nine exact computer-algebra rows certifying the algebra of Theorems 7, 8, 9, 11, 16, 17 and 20 identically in their free variables. Class `C`, not `P`. | block `Y`, gate `F-M62.19` |

| `E-M62-13` | **mathematical correction** | Thm 17(iv), §11.3 | The `Psi >= pi` value of `A*` was stated by a single formula. It is false on `|Re lambda| + |Im lambda| <= 1`; at `lambda = 0` it returns `1/2` where the true value is `0`, and it deviates by up to `0.4975` over the feasible set. | Stated piecewise, in agreement with Eq. (8.5); Remark 17.3 records the counterexample and the branch check for the frozen target; §11.3 now displays `|Re lambda| + |Im lambda| = 1.2548705574 > 1`. No Z-Spin number changes. | `N7`, guard `M7` | | `E-M62-14` | **retraction (novelty)** | Thm 2 | The peeling identity was labelled `OPEN-NOVELTY`. | Retyped `IMPORTED CORE + SPECIALIZED`. A second proof is given deriving it in two lines from the overlapping-coefficient identity `d_TV = 1 - int(p ^ q)`; the contributed observation is isolated (`mu ^ R#mu` is automatically `R`\-invariant). The trimming/contamination pointer is recorded with an explicit *not read at source* status. | `N8`, guard `M7` | | `E-M62-17` | self-detected (guard defect) | guard `M7` | `M7` was written as a global substring test, so deleting the Theorem 17(iv) branch condition from the *statement*, or the retyped novelty class from the *table row*, left the guard passing because the same strings survive elsewhere in the document. Live-firing exposed it immediately. | `M7` is anchored to the blocks it is about: the text of the Theorem 17 statement and the single contribution-table line for Theorem 2; it also requires the branch condition to be stated in at least three places, and the branch-check numeral `1.2548705574` is now computed in row `K6` and required by `M1`. | live-fire `A19`, `A20`, `A22` | | `E-M62-16` | self-detected (conditioning, not error) | rows `E3`, `E7` | Trimming the FULL sample counts changed the random stream and surfaced a latent limitation: the constructive form of Theorem 9 divides by `1 - A`, so in double precision it can reject data within about `1e-6` of the feasibility boundary. The old `E3` demanded a solution everywhere and would have masked this by luck of the draw. | `E3` re-scoped to `A <= 1 - 1e-6`, publishing the size of the corner; new row `E7` certifies the closed form there at 40 digits against the *independent* geometric bisection (`6.27e-39`) and bounds the constructive form's residual by the distance to the boundary (`2.08e-12` against `3.80e-6`). | `E3`, `E7` | | `E-M62-15` | artifact correction | ledger flag, FULL runtime | The ledger set `certificate: true` for any non-quick run, including runs with failing rows; and the FULL profile carried sample counts far above what its tolerances require. | `certificate` is now `true` only for a full run with zero failures; a missing solver additionally prints the remediation command. FULL trimmed from \~70 s to \~45 s with no tolerance changed. | live-fire `A18` |

| `E-M62-18` | **artifact correction (release package)** | verifier `normalise()` / guards `M6`, `M7`; §13.1 | The manuscript delivered for the fourth audit had been **Markdown-escaped in transit** (`Theorem 17\.`, `\+`, `\<=`). Guards `M6` and `M7` read the raw text for their structural anchors, so both failed on the copy the auditor held, and the byte-level SHA-256 of that copy did not match the value the release quoted. The science was untouched; the *release package* did not survive its own delivery channel. | Every manuscript guard is now evaluated on a **transport-invariant normal form** (`transport_norm`: NFKC, zero-width removal, dash unification, and backslash-unescaping **iterated to a fixpoint**), and the manuscript is identified by a **transport-invariant digest** as well as by a byte hash. Two new self-referential rows close the class: `M8` recomputes the digest the manuscript declares, as a fixed point; `M9` re-runs every manuscript guard on a synthetically escaped copy and requires all verdicts to agree. Gates `F-M62.24`, `F-M62.25`; debt `D-M62-XPORT`. **Self-detected during the repair:** `normalise()` initially undid one escape level where two were present, so `M9` failed on the doubly escaped copy; it now reuses the iterated `de_escape`. | `M8`, `M9`, live-fire `A23`–`A27` | | `E-M62-19` | verification strengthening | verifier Block `F` | Every row of the semidefinite section called a solver. Two of the four audits ran without `cvxpy`, so in those environments Theorems 13 and 14 had **no positive evidence at all** — the four fail-closed rows correctly reported an absence and nothing more. A fail-closed row is a control, not a certificate. | Two **solver-free** rows added. `F5` verifies the forward direction of Theorem 13 by symmetric eigenvalue decomposition of the Toeplitz matrices induced by an independent grid linear programme; `F6` verifies the localizing condition of Theorem 14 on arc-supported measures **and** its discriminating power against measures with mass outside the arc. `numpy` only. Gate `F-M62.27`. | `F5`, `F6`, live-fire `A29` | | `E-M62-20` | editorial (positioning) | guard `M5`, §14 | The novelty-language guard listed explicit priority claims but not the promotional adjectives that do the same work indirectly. The fourth audit's positioning note is that such language belongs after `D-M62-PRIOR` closes, not before. | `M5`'s list extended to the promotional-innovation adjectives, in English and in Korean. Quoted auditor verdicts remain quotable: the list is chosen so that the auditors' own wording, retained verbatim in §15.2–§15.5, does not trip it. Gate `F-M62.26`. | `M5` | | `E-M62-21` | self-detected (guard anchoring) | guard `M7` | Writing the v1.4 prose introduced a **second occurrence** of the Theorem 17 statement anchor into the manuscript. The v1.3 guard took the first occurrence, so it continued to localise correctly only by the accident of document order; a paragraph inserted above the theorem would have widened the window to most of the paper and silently disabled the guard. This is `E-M62-17` recurring in a new disguise. | `M7` now requires the Theorem 17 statement anchor and the Theorem 2 contribution-table row to occur **exactly once** each, and reports the count when they do not. The manuscript's own prose was rewritten to describe the anchor rather than reproduce it. | live-fire `A28` |

| `E-M62-22` | **artifact correction (integrity diagnostics)** | guard `M8`; §13.1, §13.2 | The self-identifying digest introduced in `v1.4` was **binary**. When the fifth audit ran the `v1.4` pair against its own copy of the manuscript, `M8` correctly reported a mismatch and then stopped: it could not say whether the drift was a whitespace-level reformat of a table, an edited sentence in the audit record, or a changed theorem. A detector that cannot localise leaves the reader with no proportionate response, and is the identity-level form of the defect already recorded as `E-M62-17` (a guard that cannot localise) and `E-M62-21` (an anchor that cannot localise). Note what was **not** wrong: the script hash matched, `M7` passed, and the author's copy still recomputed to the published value, so the `v1.3` failure mode — guards broken by the channel — did **not** recur. | The manuscript is split into five parts at top-level section boundaries and carries a **fixed-point digest for each**, so a mismatch names the part that drifted; part-boundary uniqueness is itself checked, so a renamed section is reported rather than absorbed. The manifest additionally publishes the `v1.4` digests of parts `B` and `C`, which makes *"this patch changed no mathematics"* a refutable claim rather than a promise. A new **`--identify`** mode answers the identity question in under a second without running the suite, so an auditor establishes *which document they hold* before spending fifty seconds describing it. Gates `F-M62.28`, `F-M62.29`. **Self-detected during the repair:** the digests had to be made *label-blind* — relabelling `v1.4` as `v1.4.1` moved part `B`, the mathematics, because §2.3 names the release — and the hole that opens, a manuscript whose version-label sites disagree, is closed by a label-consistency clause in the same row. | `M8`, live-fire `A30`–`A34` |

| `E-M62-23` | **artifact correction (cross-artifact claim)** | artifact manifest §13.1; guard `M10` | The manifest quotes `sha256(script)` and **no row checked it**. In `v1.4.1` the hash was written into the manuscript, the script was then edited by that same version's repair, and the full suite passed — every self-referential row green — with a stale hash on the page. The defect is structural, not clerical: `M8` and `M9` certify the manuscript **against itself**, and a manifest also asserts things **about other files**, which nothing was pointed at. Every prior member of this family was a guard that could not localise; this one is a claim with no guard at all. | Row `M10` recomputes the SHA-256 of the running script and requires the manuscript to declare it; because it lives inside the guard set, `M9` re-runs it on the escaped copy too. The **ledger** hash is explicitly excluded and the exclusion is published: the ledger records the outcome of every row, so a row verifying the ledger's own hash has no fixed point, and it is therefore a locator rather than a guarded claim. Gate `F-M62.30` requires every future manifest line to be classified as guarded or locator when it is added. | `M10`, live-fire `A35` |

Nothing in this register is deleted from the record. Version 1.0 remains a historical artifact and is marked `SUPERSEDED`, not `RETRACTED`: its mathematical core survives, and the three mathematical defects are repairs of scope, of a formula, and of a sign, not of the architecture.

## 15.2 What the audit did **not** overturn

The audit's own summary is retained here without softening: *mathematical density very high; physical-bridge breakthrough yes, closure no; "all derivations verified" false; internal value high, external novelty unverified.* Concretely, the following were examined and stood:

* the peeling identity and the reduction to a nested Minkowski threshold (Theorems 2, 3 — the latter after the scope repair);  
* the reflection-coupled atom bound `n + floor(n/2) + 1` and its contact-geometry proof (Theorem 5);  
* the complete first-order solution, its closed-form dual certificate and its extremizers (Theorems 7–11);  
* the exact semidefinite representations on the circle and on arcs (Theorems 13, 14);  
* the transport of the multiplier problem onto the first-order problem, and hence the reachability criterion and the price (Theorem 17\) — the audit describes this as a stronger simplification than the design document anticipated;  
* every number in §11.

## 15.3 Second audit (v1.1) — findings and disposition

Verdict: **`REVIEW READY` maintained; no release-blocking defect; no new mathematical error.** The auditor's scoring is retained verbatim: mathematical density *very high, 9/10*; mathematical correctness *substantially improved, core architecture survives*; physical bridge *the same meaningful breakthrough, not a closure*; computation and verification *strengthened, but not full theorem verification*; internal Z-Spin value *very high*; external novelty *promise increased, still `OPEN`*.

| Finding | Severity as reported | Disposition |
| :---- | :---- | :---- |
| §1.1 still described the observables as "bounded measurable" | `S1` polish | accepted, `E-M62-9`, guarded |
| Abstract writes `Psi` with `c` instead of \` | c | `; verifier` I1\` claim string likewise |
| the full suite did not finish inside a 180 s budget, so `71/71` was not independently reproduced | reproducibility | accepted, `E-M62-11`; a documented non-certifying quick profile added |
| "all derivations verified" would still be an overstatement: `P = 0`, no qualified-human proof review, imported-theorem mappings need separate audit | standing | accepted and *not* argued against. §13.2 now states precisely what is and is not certified; block `Y` narrows the gap for algebra only |
| the entropy-floor retraction of v1.1 is correct; external novelty now rests on Theorems 2, 3, 5, 7–9, 15–17 | confirmation | recorded in §14; `D-M62-PRIOR` stays open |
| an additional independent search found nothing directly subsuming that combination | partial sweep | recorded as `NOT_FOUND`, which is **not** a novelty proof; `D-M62-PRIOR` stays open |

The auditor also recorded what it approved of in the v1.0 → v1.1 transition, and that judgement is kept here because it constrains future revisions: the repair narrowed Theorem 3, corrected Theorem 6, corrected Theorem 18, withdrew a novelty claim and downgraded a physical reading, while *widening* the scope of the general orbit identity — i.e. the paper was made weaker where it had been wrong and broader only where it could be proved.

## 15.4 Third audit (v1.2) — findings and disposition

Verdict: **`AUDIT-CORRECTION-REQUIRED`** — not a request to rewrite the architecture, but blocking for external submission. The auditor's scoring is retained: mathematical density *very high, \~9/10*; completeness relative to v1.1 *clearly improved*; physical bridge *meaningful reduction breakthrough, not closed*; all derivations verified *no*; internal Z-Spin value *very high*; external mathematical value *high potential, but novelty must be revised downward*.

| Finding | Severity | Disposition |
| :---- | :---- | :---- |
| Theorem 17(iv) states a single formula where Eq. (8.5) is piecewise; `lambda = 0` gives `1/2` instead of `0` | **mathematical error, general quantifier** | accepted, `E-M62-13`. Stated piecewise; Remark 17.3 records the counterexample; regression `N7` also refutes the superseded form; guard `M7` |
| Theorem 2 is a specialization of the trimming/contamination equivalence | **prior-art collision** | accepted, `E-M62-14`. Retyped `IMPORTED CORE + SPECIALIZED`; a second, two-line proof from the overlapping-coefficient identity is added; regression `N8` |
| the auditor's run gave `78/82` in the QUICK profile, the four failures being `F1`–`F4` from a missing solver, exactly as designed | confirmation of the fail-closed design | recorded. `E-M62-15` additionally makes such a run record `certificate: false`, and prints the remediation command |
| the FULL profile again did not complete inside the auditor's time budget | reproducibility | FULL trimmed to \~45 s with no tolerance changed; QUICK remains available and non-certifying |
| "all derivations verified" would still be an overstatement | standing | accepted and unchanged. §13.2 states the boundary; block `Y` certifies algebra only |
| external novelty should be re-centred on Theorems 3, 5, 7–9, 15–17 | positioning | accepted; §14 and §1.4 updated |

The auditor also confirmed that the Z-Spin numerical bridge survives the Theorem 17(iv) correction, because the frozen target lies strictly inside the second branch. That is checked in §11.3 and in ledger row `N7`.

Two audits have now produced a novelty retraction each (Corollary 20.1, then Theorem 2). The correct reading is the one gate `F-M62.22` records: an `OPEN-NOVELTY` label in this paper means *not yet searched*, and the base rate of such labels surviving a real search is, on this paper's own evidence, not high.

## 15.5 Fourth audit (v1.3) — findings and disposition

Verdict: **scientific content `REVIEW READY`; current attached release package `ARTIFACT CORRECTION REQUIRED`.** This is the first audit to separate those two judgements, and the separation is the finding. The auditor's scoring is retained: mathematical density *very high*; the v1.2 → v1.3 corrections *correctly integrated*; **no new mathematical error found**; physical bridge *unchanged, still a reduction and not a closure*; external novelty *correctly narrowed, sweep still open*.

| Finding | Severity | Disposition |
| :---- | :---- | :---- |
| the delivered manuscript had been Markdown-escaped in transit, so guards `M6` and `M7` failed on the copy the auditor held | **artifact, release-blocking for the package** | accepted, `E-M62-18`. All guards moved onto a transport-invariant normal form; a transport-invariant digest published; self-referential rows `M8`, `M9` added; gates `F-M62.24`, `F-M62.25`; debt `D-M62-XPORT` |
| the SHA-256 of the delivered file did not match the value the release quoted | **artifact** | accepted, same erratum. Two identifiers are now published and their different fragility is stated; a byte hash may no longer be quoted alone |
| the semidefinite block was not re-verified in the auditor's environment, which has no `cvxpy` | verification gap | accepted, `E-M62-19`. Solver-free rows `F5`, `F6` added; gate `F-M62.27` |
| the external-novelty candidates are correctly narrowed to Theorems 3, 5, 7–9, 15–17 | confirmation | recorded; `D-M62-PRIOR` stays open and has still fired twice |
| promotional language about this paper's own results should wait until `D-M62-PRIOR` closes | positioning | accepted, `E-M62-20`. Guard `M5` extended; gate `F-M62.26` |
| no new mathematical error | confirmation | recorded without softening. It is the first audit of the four to find none, and on this paper's own base rate that is weak evidence of correctness, not strong |

Two errata in this cycle were **self-detected**, both by the machinery written to close the audit's finding: `E-M62-18`'s own repair failed on a doubly escaped copy until `normalise()` was made to iterate, and `E-M62-21` — a second occurrence of a guard anchor introduced by writing this very section. Neither would have been visible to a reader; both were visible to a guard that was asked to test itself. That is the specific thing `M8` and `M9` buy, and §13.2 states just as plainly what they do not buy.

## 15.6 Fifth audit (v1.4) — findings and disposition

Verdict: **scientific content `REVIEW READY`, and better than `v1.3`; the attached release package not yet closable.** No mathematical error. The auditor's own framing is retained because it is the correct one: `v1.3 → v1.4` was *not* a mathematical advance — `v1.4` says so itself — but the version that makes the paper a solid research artifact fit to send outside. The four improvements the auditor credits are the transport-invariant guard evaluation, the `M8`/`M9` self-verification structure, the reduced environment dependence of the semidefinite evidence, and the strengthened guard against promotional novelty language while `D-M62-PRIOR` is open.

| Finding | Severity | Disposition |
| :---- | :---- | :---- |
| running the `v1.4` pair in `QUICK` gave `85/90`; four failures are `F1`–`F4` from a missing solver, as designed | confirmation of the fail-closed design | recorded. `F5` and `F6` passed in that same environment, which is exactly what `E-M62-19` was for |
| the fifth failure is `M8`: the declared transport digest `cf7fd64e…` did not match the value recomputed from the auditor's copy, while the *script* SHA-256 matched exactly | **artifact — content drift in the delivered manuscript** | accepted as a true positive. The author's copy still recomputes to `cf7fd64e…`, and the drift was **not reproducible** here: em- and en-dash rewriting, `§`/`·`/`→` substitution, de-accenting, NFC/NFD/NFKC, CRLF, BOM, de-escaping, emphasis stripping and Hangul loss were applied singly and in all pairs and triples, and none yields the auditor's digest. The fault therefore lies in the delivery path and is **not** a transformation the normal form can absorb |
| `M8` detected the drift but could not say **where** | **diagnostic gap** | accepted, `E-M62-22`. Five part digests, part-boundary uniqueness checking, published `v1.4` digests for the unchanged parts, and a sub-second `--identify` mode. Gates `F-M62.28`, `F-M62.29` |
| `M7` passed and the guards did not break — the `v1.3` failure mode did not recur | confirmation | recorded. It is the one piece of evidence that `E-M62-18` was repaired at the right level |
| the remaining large tasks are unchanged: qualified-human or proof-assistant proof review, and closing `D-M62-PRIOR` | standing | accepted without softening; both are why `FINAL` is withheld (§15.8) |
| the correct next step is a release-package patch, not a mathematical revision | versioning | accepted. This version is `v1.4.1`: the mathematics is bit-identical, and parts `B` and `C` are published with the `v1.4` digests so that the label can be checked rather than trusted |

The methodological content of this audit is narrow and worth stating exactly. It did not find an error in the paper; it found that an instrument added in the previous version reported a real condition at insufficient resolution. That is the third time in four versions that the finding has been about the *verification apparatus* rather than the mathematics, and each time the fix has been the same shape: make the check localise. `F-M62.23` said it for statement guards, `E-M62-21` said it for anchors, and `E-M62-22` says it for identity.

## 15.7 Auditor independence

audits performed       : 5 (on v1.0, v1.1, v1.2, v1.3 and v1.4)

auditor\_independence   : same model family, separate context, independent re-execution of the

                         attached artifact pair.  Audit 1 recomputed the script SHA-256, confirmed

                         it matched the manuscript, and ran the suite in an environment without

                         cvxpy.  Audit 2 confirmed the code-level repairs by reading, and could

                         not complete the full run inside its time budget.  Audit 3 executed the

                         QUICK profile independently (78/82, the four failures being the

                         solver-dependent Block F rows, as designed) and found the Theorem 17(iv)

                         error by reading the statement against Eq. (8.5).  Audit 4 attempted an

                         independent re-execution and found the DELIVERY broken rather than the

                         science: the manuscript it received had been Markdown-escaped, so two

                         guards failed and the byte hash did not match.  Independence

                         coefficient is LOW for all four.  Audit 5 executed the QUICK profile

                         against its own copy of the v1.4 manuscript (85/90: F1-F4 solver-absent

                         as designed, plus M8) and thereby produced the first TRUE POSITIVE of

                         the self-identification machinery: the copy it held had drifted from the

                         verified one.  Independence coefficient LOW for all five.

qualified-human anchor : NONE

deterministic re-checks: the auditor's run reproduced 59/62 rows PASS; the three failures were

                         M4 (a genuine verifier defect, E-M62-4), F1 (missing cvxpy) and S3

                         (row-count, caused by the suppressed F2-F4, E-M62-8).  Both artifact

                         defects are fixed in v1.1 and both are now live-fire tested.

findings accepted      : audit 1 \-- 3 mathematical (E-M62-1,2,3), 1 novelty retraction

                         (E-M62-6b), 1 claim reduction (E-M62-7), 3 artifact (E-M62-4,5,8);

                         audit 2 \-- 2 editorial (E-M62-9,10), 1 reproducibility (E-M62-11),

                         plus one standing observation acted on voluntarily (E-M62-12);

                         audit 3 \-- 1 mathematical (E-M62-13), 1 novelty retraction (E-M62-14),

                         plus 1 artifact hardening acted on voluntarily (E-M62-15);

                         audit 4 \-- 2 artifact (E-M62-18, E-M62-19), 1 positioning (E-M62-20),

                         plus 2 self-detected during the repair (the iterated-unescape defect

                         inside E-M62-18, and E-M62-21);

                         audit 5 \-- 1 artifact diagnostic gap (E-M62-22); no mathematical finding

findings rejected      : none

mathematical errors    : 4 found by audit across v1.0-v1.2 (Thms 3, 6, 18, 17(iv)); all four

                         were errors of scope, formula, sign and branch \-- none touched the

                         architecture, and none changed a Z-Spin number.  Audits 4 and 5 found

                         none; both, however, ran without a semidefinite solver, and audit 5 ran

                         against a manuscript that had drifted \-- so neither had full working

                         access to the artifact, and their clean verdicts are correspondingly

                         weak evidence.

self-detected errata   : E-M62-16, E-M62-17, E-M62-21 and the iterated-unescape defect inside

                         E-M62-18.  All four were found by live-firing or self-referencing the

                         guard suite, not by reading; none was found by an auditor.

## 15.8 Standing judgement

`ZS-M62 v1.4.1` is `REVIEW READY`. It is **not** `FINAL` and **not** `TERMINAL-IN-SCOPE`. Five adversarial audits have now been performed and incorporated; all five were of low independence, so they do not substitute for the blocking items, which are, in order: a **qualified-human proof review** (or a proof-assistant formalization) — block `Y` certifies algebra, not logic, and three of the four mathematical errors found so far were errors of *statement*, which is exactly what a formalization would catch; the prior-art sweep `D-M62-PRIOR`, which has now fired **twice**; and the absence of a persistent archival identifier, which is also what `D-M62-XPORT` ultimately waits on.

The fourth and fifth audits found no mathematical error, and the honest reading of that is narrow. Both ran in environments without a semidefinite solver; the fourth held a manuscript that had been re-encoded in transit and the fifth held one that had drifted outright. These are the two audits with the least working access to the artifact, and a clean verdict from a constrained audit is weak evidence. What they do license is a change of emphasis rather than of label: the class of defect these versions close is no longer mathematical but **infrastructural**. `v1.4` repaired a guard suite broken by its delivery channel; `v1.4.1` repaired the instrument that repair introduced, which reported a real condition at insufficient resolution. Three of the last four findings have been about the verification apparatus rather than the paper, and two of them were defects in the repair of a defect — which is the signature of a class that is not yet exhausted, and a reason to expect the next finding in the same place rather than in the mathematics.

The empirical record still argues against declaring the paper finished on internal evidence: each of the first three audits found something real, and the two that searched the literature each removed a novelty claim. Until an audit that *can* run the artifact, against a manuscript that *matches its published digest*, finds nothing, the prior on there being nothing left to find is weak. `--identify` exists so that the second half of that condition is cheap to establish. The physical bridge is **not** closed, and §12.3 states the objection that keeps it open without weakening it.

---

# 16\. Conclusion

The minimum reflection asymmetry of a probability measure with prescribed linear data is the threshold at which the data enter a nested Minkowski interpolation between the full moment body and its symmetric sub-body. That single reformulation makes strong duality unconditional, sharpens the atom count from `2n+1` to `n + floor(n/2) + 1`, yields exact semidefinite representations on the circle and on every arc, and produces the complete first-order solution together with a dual certificate that a reader can check by hand. Applied to the Z-Spin contraction multiplier the same theorem removes the need for any harmonic truncation: the multiplier problem *is* the first-order problem on a rescaled arc. The resulting statements are quantitative and target-blind — a reachability threshold `c >= 1.08647418977505301` for `u >= pi/2`, an unconditional asymmetry price `0.763362818245963536`, and, for finite-volume Gibbs boundary laws, the requirement `|| S_o ||_inf >= 1.00422493384939229`.

What remains open is stated plainly: the infinite-volume analogue of the Gibbs ceiling, the upstream reduction that would decide whether the required odd content exists, the degenerate strata of the atomicity theorem, a full second-order piecewise formula, and the prior-art sweep.

Two methodological remarks are worth recording, because they are the reason this version and its predecessor exist. Version 1.0 shipped with a verification suite of sixty-five rows, none of which failed, and with three genuine mathematical defects: a quantifier that was too generous, a missing truncation at zero in a dual formula, and a sign that was correct on the half of the parameter space the tests happened to sample. A passing ledger measures what it was built to measure. The defects were found by reading the statements against their own quantifiers, and the only durable response is the one taken here — turn each finding into a row that fails when the defect returns, and say plainly which results were repaired, which were narrowed, and which were never ours to claim.

The second remark is the reason for v1.4, and it is about a boundary the first remark does not reach. The fourth audit found no mathematical error; what it found was that the *delivered package* had been altered by its own delivery channel, so that two guards failed on a manuscript whose content was correct. A verification suite that reads the bytes it was handed is verifying the channel as much as the document. The repair is to verify a normal form invariant under the channel, and — since a guard suite is exactly the thing no reader independently checks — to make the suite test itself: to require that every guard return the same verdict on a transformed copy, and that the document certify its own transport-invariant identity as a fixed point. Doing so immediately found two further defects, both of them in the repair rather than in the paper. That is not a triumph; it is a measurement of how thin the layer of self-inspection had been. The general form of the lesson, which now has three instances in this paper — an escaped guard token, an unanchored guard, a non-unique anchor — is that verification code is the part of a release with no auditor, and it earns trust only by being made to fail on demand and by being pointed at itself.

---

## Acknowledgements

This work is part of the Z-Spin Cosmology programme and builds directly on ZS-M61 v1.6, whose first-order result is recovered here as Corollary 10\.

## AI use statement

AI\_TOOL\_RECORD

name/version        : Claude (Anthropic), model identifier claude-opus-5, session of 2026-08-19

tasks               : hypothesis-space transformation from the predecessor design document;

                      derivation and drafting of Sections 2-11; authoring of the verification suite

inputs/scope        : the ZS-M62 successor seed report, the corpus rule files, ZS-M61/ZS-S14/ZS-M1

                      status entries retrieved from the project store

human direction     : the research target, the priority ("mathematical density first"), and the

                      instruction to derive and verify every displayed identity were set by the user

verification route  : every displayed identity is either given a written proof in this manuscript or

                      recomputed independently in zs\_m62\_verify\_v1\_4\_2.py; the first-order closed form

                      was cross-checked against a 40-digit bisection and against a raw

                      total-variation linear programme that shares no code with the closed form

what was checked    : all numerals in Section 11; the dual certificate feasibility; the extremizer

                      constructions; the three-route agreement of Section 4

what was corrected  : v1.0 drafting \-- a sign error in the orientation of the extremal atom of

                      Theorem 18 for positive c (detected by the residual |a(c)-lambda| \= 2|Im lambda|);

                      an edge case of the left-reservoir branch at x \= cos u; an atomicity test that

                      measured solver-returned basic solutions rather than minimal-support optimisers.

                      v1.1 revision \-- the three mathematical defects, the novelty retraction and the

                      two artifact defects of the correction register (Section 15.1) were identified by

                      an INDEPENDENT adversarial audit of v1.0, not by the drafting model, and were

                      then re-derived, repaired and turned into executable regressions here.  The

                      attribution of Corollary 20.1 was settled by an external source check plus a

                      direct minimisation of the Jeffreys divergence at fixed total variation.

                      v1.4 revision \-- the fourth audit found no mathematical error; its findings

                      were about the RELEASE PACKAGE (a delivery channel that Markdown-escaped the

                      manuscript, and a semidefinite block with no solver-free evidence).  Both

                      were reproduced before being repaired: the v1.3 verifier was run against a

                      fully escaped copy of the v1.3 manuscript and produced exactly the auditor's

                      failure, 85/86 with M7 FAIL.  Two further errata were then found by the

                      repair's own self-referential row, not by any reader.

                      v1.4.1 revision \-- the fifth audit found no mathematical error.  Its finding

                      was that the self-identification row added in v1.4 was binary: it correctly

                      refused a drifted copy of the manuscript and could not say which region had

                      drifted.  The drift itself was NOT reproducible here \-- eighteen candidate

                      channel transformations were applied singly and in all pairs and triples,

                      and none reproduces the auditor's digest \-- so it is recorded as a delivery

                      fault, not as a normalisation gap.  The repair is diagnostic, not

                      mathematical: five part digests, boundary-uniqueness checking, and a

                      sub-second \--identify mode.

An AI system is not an author. Final responsibility rests with the human author. The proofs in this manuscript have **not** yet been reviewed by an independent qualified human; all five adversarial audits were performed by systems of the same model family, so their independence coefficient is low (§15.7). The release label is `REVIEW READY`, not `FINAL`.

## Data availability

No new research data were created or analysed. Every number in this paper is reproducible from the equations herein and from the script identified in the Code availability statement.

## Code availability

`zs_m62_verify_v1_4_2.py` (main), with ledger `zs_m62_verify_v1_4_2.json`. Run with `python3 zs_m62_verify_v1_4_2.py`, and check identity first with `python3 zs_m62_verify_v1_4_2.py --identify`. Dependencies: `numpy`, `scipy`, `mpmath`, `sympy`, and optionally `cvxpy` (CLARABEL) — without it, rows `F1`–`F4` fail closed but the solver-free rows `F5`, `F6` still verify the semidefinite content. The manuscript is identified by the transport-invariant digest and the five part digests printed in §13.1, which are what a reader should check; the byte-level SHA-256 is emitted by the script at runtime and is expected to change if the file passes through any re-encoding channel. No persistent archival identifier has been assigned; the artifact is therefore not yet publicly certified and the label `FINAL` is withheld.

## Version history

v1.0 (2026-08-19)

\- Mathematics: first release. Theorems 1-20 as stated.

\- Verification: zs\_m62\_verify\_v1\_0.py, 65 rows, 0 FAIL. Class P not used.

\- Scope: Sections 2-9 are Z-Spin-free; Sections 10-11 are conditional and carry NC-M62.1..6.

\- Status: SUPERSEDED by v1.1. Retained as a historical artifact; not deleted.

v1.1 (2026-08-19) \-- major revision after one independent adversarial audit

                     (verdict on v1.0: AUDIT-MAJOR-REVISION, release-blocking)

\- Mathematical correction  E-M62-1: Theorem 3 was FALSE once the observables are only assumed

    bounded and measurable and the moment bodies are taken to be closed convex hulls. Restricted to

    continuous Phi (standing hypothesis H-CONT); Proposition 3.2 gives the general bounded

    measurable version with attainable sets; Remark 3.3 exhibits the counterexample. Every

    application in the paper is continuous, so no downstream result is lost.

\- Mathematical correction  E-M62-2: the fractional dual (5.1) of Theorem 6 was missing an outer

    max{0, . } and could return a negative number. Corrected, feasibility condition (5.0) split

    out, and Remark 6.2 gives an explicit three-point counterexample. The trigonometric dual (5.3)

    and all first-order computations were unaffected (Remark 6.3).

\- Mathematical correction  E-M62-3: Theorem 18 exhibited the wrong orientation for c \< 0\. The sign

    now carries sign(c); the value statements of Theorem 17 were never affected.

\- Scope extension       E-M62-6a: Theorem 20 upgraded from finite-volume Gibbs laws to arbitrary

    measures via the orbit density h; the Gibbs identities become Corollary 20.2.

\- Novelty retraction    E-M62-6b: the entropy floor 2 A artanh A is RETYPED from OPEN-NOVELTY to

    IMPORTED / SPECIALIZED (Gilardoni; Sason-Verdu). No priority is claimed for it.

\- Claim reduction       E-M62-7: the "O(1) odd term cannot come from a small radiative or anomaly

    contribution" reading is downgraded from \[검증됨\] to \[가설\] (C2') and recorded as NC-M62.7.

\- Artifact correction   E-M62-4: normalise() now strips Markdown backslash escapes; guard M4 was

    walkable in v1.0 and is now live-fire tested (attack A9).

\- Artifact correction   E-M62-5: the manuscript is discovered (optional argument, then a glob)

    instead of hard-coded, so a renamed attachment no longer breaks the one-command run (A10).

\- Artifact correction   E-M62-8: Block F always emits four rows, so a missing solver produces one

    cause rather than two (a missing cvxpy previously also broke the row-count guard).

\- Verification: 65 \-\> 71 rows, 0 FAIL. New block N carries one executable regression per audit

    finding. Census C=12, V=28, W=8, R=1, G=14, D=4, T=4, X=0, P=0.

\- Editorial: gates F-M62.14..17 added; D-M62-PRIOR scope widened; live-fire table extended to 12

    attacks; version and filename unified to v1.1.

\- Status: SUPERSEDED by v1.2. Retained as a historical artifact; not deleted.

v1.2 (2026-08-19) \-- polish and verification strengthening after a SECOND independent

                     adversarial audit (verdict on v1.1: REVIEW READY maintained, no

                     release-blocking defect, no new mathematical error)

\- Editorial (scope)    E-M62-9 : Section 1.1 still described the observables as bounded

    measurable after (H-CONT) had been declared. Unified to continuous, with pointers to

    Remark 3.3 and Proposition 3.2. No theorem changed.

\- Editorial (notation) E-M62-10: the Abstract, Section 11.3 and the row I1 claim string wrote

    Psi with c where the general statement needs |c|. Unified; rows I1 and I2 now sample both

    signs of c. No theorem changed.

\- Reproducibility      E-M62-11: a documented \--quick profile (\~30 s) added because the second

    audit could not finish the full run inside a 180 s budget. It is a smoke test: it prints a

    banner denying certificate status and records certificate=false in the ledger. The FULL

    profile (\~70 s) remains the only quotable one.

\- Verification         E-M62-12: new block Y \-- nine rows of exact computer-algebra

    certification of the algebra inside the proofs of Theorems 7, 8, 9, 11, 16, 17 and 20\.

    Class C, not P. Section 13.2 states exactly what this does and does not certify.

\- Guards: M6 (scope consistency: the superseded "bounded measurable" wording absent, every Psi carries |c|,

    (H-CONT) and Proposition 3.2 declared); S4 (profile declaration).

    Gates F-M62.18..20 added.

\- Verification: 71 \-\> 82 rows, 0 FAIL. Census C=21, V=28, W=8, R=1, G=15, D=5, T=4, X=0, P=0.

\- Live-fire table extended to 17 attacks.

\- Mathematics: unchanged. No theorem statement, proof, constant or numerical result was altered

    in v1.2.

\- Status: SUPERSEDED by v1.3. Retained as a historical artifact; not deleted.

v1.3 (2026-08-19) \-- targeted correction after a THIRD independent adversarial audit

                     (verdict on v1.2: AUDIT-CORRECTION-REQUIRED)

\- Mathematical correction  E-M62-13: Theorem 17(iv) gave the Psi \>= pi value of A\* by a SINGLE

    formula. That statement is false on |Re lambda| \+ |Im lambda| \<= 1; at lambda \= 0 it returns

    1/2 where the true value is 0, and it deviates by up to 0.4975 over the feasible set. Now

    stated piecewise in agreement with Eq. (8.5), with the counterexample in Remark 17.3 and the

    branch check displayed in Section 11.3. No constant and no Z-Spin number changes: the frozen

    target has |Re lambda| \+ |Im lambda| \= 1.2548705574 \> 1\.

\- Novelty retraction       E-M62-14: Theorem 2 retyped from OPEN-NOVELTY to IMPORTED CORE \+

    SPECIALIZED. A second proof derives it in two lines from the overlapping-coefficient identity

    d\_TV \= 1 \- int(p ^ q); the contributed observation is isolated as the R-invariance of the

    maximal common sub-measure. The trimming/contamination pointer supplied by the audit is

    recorded with an explicit not-read-at-source status.

\- Artifact hardening       E-M62-15: the ledger records certificate=false for any run with a

    failing row, not only for quick runs; a missing solver prints its remediation command; the

    FULL profile is trimmed from \~70 s to \~45 s with no tolerance changed.

\- Guards: M7 (statement guard for Theorems 2 and 17(iv)). Gates F-M62.21, F-M62.22 added.

\- Self-detected            E-M62-16: trimming the FULL sample counts changed the random stream

    and exposed a latent CONDITIONING limitation, not an error: the constructive form of

    Theorem 9 divides by 1 \- A when it locates the symmetric reservoir, so in double precision

    it can reject data lying within about 1e-6 of the feasibility boundary. Row E3 is re-scoped

    to the well-conditioned set A \<= 1 \- 1e-6 and publishes the size of the residual corner;

    new row E7 settles that corner at 40 digits against the INDEPENDENT geometric bisection of

    the nested family (agreement 6.27e-39), and shows the constructive form's residual there is

    5 orders of magnitude below the distance to the boundary. Nothing was weakened: the corner

    is now covered by a stronger check than the one that used to skip it.

\- Verification: 82 \-\> 86 rows, 0 FAIL. New rows N7 (Theorem 17(iv) piecewise, with the

    superseded form refuted), N8 (the classical identity behind Theorem 2\) and E7 (the

    ill-conditioned corner at 40 digits).

    Census C=22, V=29, W=9, R=1, G=16, D=5, T=4, X=0, P=0.

\- Self-detected            E-M62-17: guard M7 was a global substring test and did not fire when

    the branch condition was deleted from the Theorem 17(iv) statement, or when the Theorem 2

    table row was retyped, because the same strings survive elsewhere. M7 is now anchored to

    those two blocks, requires the branch condition in at least three places, and the branch

    check |Re lambda| \+ |Im lambda| \= 1.2548705574 is computed in row K6 and required by M1.

\- Live-fire table extended to 22 attacks, two of which are recorded with their first, failed

    outcome because that failure is what produced E-M62-17.

\- Positioning: the external-novelty case is re-centred on Theorems 3, 5, 7-9 and 15-17.

\- Status: SUPERSEDED by v1.4. Retained as a historical artifact; not deleted.

v1.4 (2026-08-19) \-- release-package repair and self-referential verification, after a FOURTH

                     independent adversarial audit (verdict on v1.3: scientific content

                     REVIEW READY, attached release package ARTIFACT CORRECTION REQUIRED,

                     NO new mathematical error)

\- Mathematics: UNCHANGED.  No theorem statement, proof, constant, extremiser or numerical result

    was altered in v1.4.  Every Z-Spin number is bit-identical to v1.1, v1.2 and v1.3:

    A\*\_inf \= 0.763362818245963536, c\_min \= 1.08647418977505301,

    ||S\_o||\_inf \>= 1.00422493384939229, branch check |Re lam| \+ |Im lam| \= 1.2548705574 \> 1\.

\- Artifact correction      E-M62-18: the manuscript delivered for the fourth audit had been

    Markdown-escaped in transit, so guards M6 and M7 \-- which read the raw text for their

    structural anchors \-- failed on the copy the auditor held, and the byte hash did not match.

    The failure was REPRODUCED before being repaired: running the v1.3 verifier against a fully

    escaped copy of the v1.3 manuscript gives exactly 85/86 with M7 FAIL.  All manuscript guards

    now run on a transport-invariant normal form (NFKC, zero-width removal, dash unification, and

    backslash-unescaping ITERATED to a fixpoint), and the manuscript is identified by a

    transport-invariant digest as well as by a byte hash.  Gates F-M62.24, F-M62.25; debt

    D-M62-XPORT.

\- Self-referential verification: two new rows whose subject is the guard suite itself.

    M8 \-- the manuscript declares its own transport-invariant digest in the artifact manifest and

      the row recomputes it as a FIXED POINT, blanking the declaring line before hashing, so the

      manuscript certifies its own identity without circularity.

    M9 \-- every manuscript guard, M8 included, is re-run on a synthetically Markdown-escaped copy

      of this manuscript; the row fails unless every verdict agrees and the digest is unchanged.

    Section 13.2 states the limit of both: they establish invariance under the delivery channel,

    not adequacy of the guards, which is still carried by the live-fire table.

\- Self-detected (inside the repair): normalise() undid ONE level of escaping where two were

    present, so M9 failed on a doubly escaped copy.  It now reuses the iterated de\_escape.

    Recorded inside E-M62-18; live-fire A25.

\- Self-detected            E-M62-21: writing the v1.4 prose introduced a SECOND occurrence of the

    Theorem 17 statement anchor, which the v1.3 guard tolerated only by the accident of document

    order.  M7 now requires that anchor and the Theorem 2 contribution-table row to occur exactly

    once each.  Live-fire A28.

\- Verification strengthening E-M62-19: rows F5 and F6 verify the semidefinite content of

    Theorems 13 and 14 with NO semidefinite solver \-- numpy eigenvalues only \-- so an environment

    without cvxpy retains positive evidence for Section 7 instead of four fail-closed rows.

    Two of the four audits ran in exactly that environment.  Gate F-M62.27.

\- Editorial (positioning)  E-M62-20: guard M5's novelty-language list extended to promotional-

    innovation adjectives, in English and Korean, per the fourth audit's positioning note that

    such language belongs after D-M62-PRIOR closes.  Gate F-M62.26.

\- Verification: 86 \-\> 90 rows, 0 FAIL.  New rows F5, F6 (solver-free semidefinite), M8

    (self-identifying digest), M9 (self-referential guard invariance).

    Census C=22, V=30, W=10, R=1, G=18, D=5, T=4, X=0, P=0.

\- Live-fire table extended to 29 attacks; A23 reproduces the fourth audit's failure against the

    v1.3 artifact, A25 and A28 are recorded with their first, failed outcome.

\- Gates F-M62.24..27 added; debt D-M62-XPORT registered and conditionally closed.

\- Status: SUPERSEDED by v1.4.1. Retained as a historical artifact; not deleted. Its published

    transport digest cf7fd64e...53637c33 remains the digest of v1.4 and is not reused.

v1.4.1 (2026-08-20) \-- RELEASE-PACKAGE PATCH after a FIFTH independent adversarial audit

                     (verdict on v1.4: scientific content REVIEW READY and better than v1.3;

                     no mathematical error; one artifact finding)

\- Mathematics: UNCHANGED, and now CHECKABLY unchanged.  Parts B (Sections 2-9) and C (Sections

    10-11) must digest to the values published for v1.4 \--

    B d14aaa5e...c1900c9e, C 3b6002cb...e347a95a \-- and the manifest prints both so that the

    claim can be refuted in one command rather than trusted.  Every Z-Spin number is

    bit-identical from v1.1 onward.

\- Artifact correction      E-M62-22: the self-identifying digest of v1.4 was BINARY.  Audit 5 ran

    the v1.4 pair against its own copy, M8 correctly reported a mismatch (declared cf7fd64e...,

    recomputed 577b4fef...) while the script SHA-256 matched exactly \-- a true positive \-- and

    then had nothing further to say.  The drift was not reproducible here: eighteen candidate

    channel transformations (dash rewriting, section-sign and middle-dot substitution, arrow

    expansion, de-accenting, NFC/NFD/NFKC, CRLF, BOM, de-escaping, emphasis stripping, Hangul

    loss, quote curling, entity encoding) were applied singly and in all pairs and triples and

    none yields the auditor's value, so it is recorded as a delivery fault rather than a gap in

    the normal form.  The repair is diagnostic: five part digests computed by the same fixed-point

    construction, part-boundary uniqueness checked rather than assumed, the v1.4 digests of the

    unchanged parts published for comparison, and a \--identify mode that settles identity in

    under a second without running the suite.  Gates F-M62.28, F-M62.29.

\- What was NOT wrong, and is recorded because it is the evidence that v1.4 repaired the right

    thing: the script hash matched, M7 passed, the guards were not broken by the channel, and the

    author's copy still recomputes to the published digest.  The v1.3 failure mode did not recur.

\- Verification: 90 rows, 0 FAIL, unchanged in number and in class census

    (C=22, V=30, W=10, R=1, G=18, D=5, T=4, X=0, P=0).  M8's CLAIM and DETAIL changed; no row was

    added, because nothing new is being evidenced \-- an existing control was made diagnostic.

\- Self-detected, by the new instrument on its first run: relabelling v1.4 as v1.4.1 moved the

    digest of part B, the mathematics, because the Section 2.3 dependency freeze NAMES the

    release.  Digests are therefore taken label-blind \-- paper\_code/version, verification

    artifact, main\_script and ledger are blanked with the three hash lines \-- and the residual,

    that the digest can no longer see a version label at all, is closed by a label-consistency

    clause in M8 requiring all four version-label sites to agree.  Live-fire A34.

\- Live-fire table extended to 34 attacks: A30 (single-character edit confined to part D \-\> M8

    names D), A31 (the same in part B, the mathematics \-\> M8 names B), A32 (--identify on a clean

    and on a drifted copy), A33 (a renamed section heading \-\> the boundary check fires instead of

    two parts silently merging), A34 (change the version label in one site only \-\> M8 fires on

    label inconsistency, which is the failure mode the label-blind rule would otherwise open).

\- Status: SUPERSEDED by v1.4.2. Retained as a historical artifact; not deleted.  Its published

    transport digest 525ae6de...37e0cc1d7d remains the digest of v1.4.1 and is not reused.

    NOTE, recorded because it is the reason v1.4.2 exists: the v1.4.1 manuscript printed

    sha256(script) \= d09f0e86...96748228 while the script it shipped with hashed to

    3fa5b703...21b12748.  The suite passed 90/90 regardless, because no row checked it.

v1.4.2 (2026-08-20) \-- SECOND release-package patch, SELF-DETECTED, no audit in between

\- Mathematics: UNCHANGED, and checkably so.  Parts B and C must still digest to the v1.4 values

    B d14aaa5e...c1900c9e, C 3b6002cb...e347a95a.  Every Z-Spin number bit-identical from v1.1 on.

\- Artifact correction      E-M62-23: the artifact manifest quotes sha256(script) and NO ROW

    CHECKED IT.  In v1.4.1 the hash was written into the manuscript, that same version's repair

    then edited the script, and the full suite passed with a stale hash on the page \-- M8 green,

    M9 green, \--identify clean.  The defect is structural: every self-referential row added in

    v1.4 and v1.4.1 certifies the manuscript AGAINST ITSELF, while a manifest also asserts things

    ABOUT OTHER FILES, and nothing was pointed outward.  New row M10 recomputes the running

    script's SHA-256 and requires the manuscript to declare it; it sits inside the guard set, so

    M9 re-runs it on the escaped copy as well.

\- Stated limit, not repaired because it cannot be: the LEDGER hash admits no such row.  The

    ledger records the outcome of every row, so a row verifying the ledger's own hash has no

    fixed point.  It is published as a LOCATOR and labelled as one in the manifest.

\- Gate F-M62.30: every manifest line must be classified as GUARDED (naming the row) or LOCATOR

    at the moment it is written.  Closed for the script hash, permanently open for the ledger.

\- Verification: 90 \-\> 91 rows, 0 FAIL.  New row M10 (class G).

    Census C=22, V=30, W=10, R=1, G=19, D=5, T=4, X=0, P=0.

\- Live-fire table extended to 35 attacks: A35 corrupts one hex character of the declared script

    hash \-- M10 fires against v1.4.2 and NOTHING fires against v1.4.1, which is the erratum.

\- Status: CURRENT.

---

# Appendix A. Formula sheet

A0   d\_TV(P,Q) \= sup\_A |P(A)-Q(A)| \= (1/2)||P-Q||\_var

A1   peeling identity   (IMPORTED CORE \+ SPECIALIZED, see Remark 2.3)

     d\_TV(mu, R\#mu) \= min{ tau(Omega) : 0 \<= tau \<= mu , R\#(mu \- tau) \= mu \- tau }

     minimiser       tau\* \= mu \- (mu ^ R\#mu) \= (mu \- R\#mu)^+ ,  and mu ^ R\#mu is R-invariant

     classical core  d\_TV(P,Q) \= 1 \- int (p ^ q)

A2   master theorem   (Phi CONTINUOUS on compact Omega; see A2' for the general case)

     min{ d\_TV(mu,R\#mu) : int Phi dmu \= v } \= min{ A : v in A M\_Phi \+ (1-A) M\_Phi^sym }

     M\_Phi \= conv Phi(Omega) ,  M\_Phi^sym \= conv Phi\_e(Omega) ,  Phi\_e \= (Phi \+ Phi o R)/2

A2'  bounded measurable Phi : same identity with ATTAINABLE sets and inf in place of min.

     Closed convex hulls are WRONG here (Remark 3.3).

A3   fractional dual  (the outer max{0,.} is not optional \-- Remark 6.2)

     feasible  \<=\>  \<w,v\> \<= h\_M(w)  for all w with h\_M(w) \= h\_{M^sym}(w)

     A(v) \= max{ 0 , sup\_w \[ \<w,v\> \- h\_{M^sym}(w) \] / \[ h\_M(w) \- h\_{M^sym}(w) \] }

A4   trigonometric dual

     max a\_0 \+ \<a,x\> \+ \<b,y\>   s.t.  C \<= 0 , C \+ |S| \<= 1  on \[0,u\] ,

     C \= a\_0 \+ sum a\_k cos kt , S \= sum b\_k sin kt

A5   atom bound            \#orbit atoms \<= n \+ floor(n/2) \+ 1

                           (oriented \<= n , symmetric \<= floor(n/2) \+ 1\)

A6   n \= 1 closed form

     A\_1(x,y;u) \= max{ y/s\_1(u) , Q(1-x,1) , \[cos u\<0\] Q(x-cos u,|cos u|) } ,  s\_1(u)=sin(min(u,pi/2))

     Q(R,d) \= ( \-Rd \+ sqrt(R^2 d^2 \+ (1-d^2)(R^2+y^2)) ) / (1-d^2) ,  active only if y \> R/d

     Q(R,1) \= (R^2+y^2)/(2R)

A7   n \= 1 constructive form

     A\_1 \= min{ y/sin t\_1 : t\_1 admissible } ,  candidates t\_1 \= min(u,pi/2) ,

           t\_1 \= atan2(y,x-gamma) \+ arcsin( \-y gamma / sqrt((x-gamma)^2+y^2) ) , gamma in {1, cos u}

     extremiser  mu\* \= A delta\_{sgn(y) t\_1} \+ ((1-A)/2)(delta\_{t\_0} \+ delta\_{-t\_0}) ,

                 cos t\_0 \= (x \- A cos t\_1)/(1-A)

A8   n \= 1 dual certificate

     kappa \= 1/(1 \- gamma cos t\_1) , a\_1 \= kappa cos t\_1 , b\_1 \= kappa sin t\_1 , a\_0 \= A \- a\_1 x \- b\_1 y

     C \+ S \= a\_0 \+ kappa cos(t \- t\_1) ,  C(t\_gamma) \= 0 ,  C(t\_1)+S(t\_1) \= 1

     grad A\_1 \= (a\_1,b\_1) ,  || grad A\_1 || \= kappa

A9   full-circle SDP

     A\_n(m;pi) \= min A  s.t.  T\_n\[A;P\] \>= 0 , T\_n\[1-A;Q\] \>= 0 , Q real , P \+ Q \= m

A10  arc SDP  (g\_u \= cos theta \- cos u , N \= n+1)

     A\_n(m;u) \= min A  s.t.  T\_N\[A;P\] \>= 0 , T\_{N-1}\[g\_u.P\] \>= 0 ,

                             T\_N\[1-A;Q\] \>= 0 , T\_{N-1}\[g\_u.Q\] \>= 0 , Q real , P+Q \= m on 1..n

A11  odd-data-only problem

     value \= gauge of Y\_n(u) \= conv{ \+-(sin t,...,sin nt) : t in \[0,u\] }

     Y\_2(pi) \= { |w| \<= 1 , 2v^2 \- 1 \<= sqrt(1-w^2) }

     gauge   \= max{ |y\_2| , 2 y\_1^2 / sqrt(4 y\_1^2 \- y\_2^2) }

A12  hierarchy      A\_1 \<= A\_2 \<= ... \-\> d\_TV(mu, R\#mu)

A13  multiplier     Psi \= min( 2|c| sin(min(u,pi/2)) , pi )

     Lambda\_A(c,u) \= A conv{ e^{i psi} : |psi| \<= Psi } \+ (1-A) \[cos Psi, 1\]

     reachable  \<=\>  |lambda| \<= 1 and Re lambda \>= cos Psi

     A\*(lambda;c,u) \= A\_1( Re lambda , |Im lambda| ; Psi )

     Psi \>= pi :  A\*\_inf \= |Im lambda|                        if |Re lambda| \+ |Im lambda| \<= 1

                         \= ((1-|Re lam|)^2+(Im lam)^2)/(2(1-|Re lam|))   otherwise   \[PIECEWISE\]

     first-order datum  (X,Y) \= ( Re lambda , \-sign(c) Im lambda ) ;

     extremal atom at  sgn \* t\_1  with  sgn \= sign(Y) \= \-sign(c) sign(Im lambda)

A14  orbit form     h \= d delta / d sigma in \[-1,1\] ,  A \= int |h| d sigma \<= ||h||\_inf

     D\_KL(mu||R\#mu) \= 2 int |h| artanh|h| d sigma  \>= 2 A artanh(A) \>= 2 A^2

     (the first inequality is IMPORTED: involution specialisation of the sharp Jeffreys-TV bound)

     Gibbs case  h \= \-tanh S\_o , d sigma prop. e^{-S\_e} cosh S\_o d theta :

       d\_TV \= \< |tanh S\_o| \>\_w \<= tanh ||S\_o||\_inf ,   D\_KL \= 2 \< S\_o tanh S\_o \>\_w

A15  Z-Spin numbers Psi\_min \= 2.17294837955010601 , c\_min \= 1.08647418977505301 (u \>= pi/2) ,

     A\*\_inf \= 0.763362818245963536 , artanh(A\*\_inf) \= 1.00422493384939229 ,

     2 A\*^2 \= 1.16544558456 nats , 2 A\* artanh(A\*) \= 1.53317595131 nats

# Appendix B. Worked certificate

Take `u = pi`, `x = 0.5`, `y = 0.7`. Then `R = 1 - x = 0.5 < y`, so the right-reservoir branch is active. Theorem 9 gives

t\_1 \= pi \- 2 arctan(y/R) \= pi \- 2 arctan(1.4) \= 1.240497   (rad) ,

A   \= y / sin t\_1 \= 0.74 ,

cos t\_0 \= (x \- A cos t\_1)/(1-A) \= 1  ,  t\_0 \= 0 ,

mu\* \= 0.74 delta\_{1.240497} \+ 0.13 delta\_0 \+ 0.13 delta\_0 \= 0.74 delta\_{1.240497} \+ 0.26 delta\_0 .

Check: `0.74 exp(1.240497 i) + 0.26 = 0.5 + 0.7 i`. Theorem 8 gives the same value directly, `A = (R^2+y^2)/(2R) = (0.25+0.49)/1 = 0.74`.

Theorem 7 gives `kappa = 1/(1-cos t_1) = 1.479999`, `a_1 = kappa cos t_1 = 0.48`, `b_1 = kappa sin t_1 = 1.4`, `a_0 = 0.74 - 0.48*0.5 - 1.4*0.7 = -0.48`. Then `C(t) = 0.48(cos t - 1) <= 0` with equality at `t = 0` (the symmetric atom), and `C(t) + S(t) = -0.48 + 1.48 cos(t - 1.240497)` attains `1` exactly at `t = t_1` (the oriented atom). The dual objective is `-0.48 + 0.48*0.5 + 1.4*0.7 = 0.74`. Primal and dual agree; the pair `(mu*, (a_0,a_1,b_1))` is a self-contained certificate requiring no computer.

**END OF ZS-M62 v1.4.2**  
