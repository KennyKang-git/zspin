# ZS-M63

# Finite-Observable Saturation and Rigidity of Reflection Asymmetry

### 

### Maximal ambiguity on truncated moment fibers, co-monotone quadrature families and sharp reflection-free atom counts, an exact arc characterization, and the structure that restores selection

**Paper code:** `ZS-M63 v1.6.2` **Project:** Z-Spin Cosmology **Date:** 2026-08-21 KST **Supersedes:** `ZS-M63 v1.6.1` (771 lines), audited **AUDIT-PASS-MINOR / Minor Revision**, highest severity `S1`, **`RELEASE-BLOCKING: NO`**, recorded as "the best-written version of the M63 line". Earlier: v1.6 (also `AUDIT-PASS-MINOR`), and v1.5–v1.0, all `AUDIT-MAJOR-REVISION` or `AUDIT-CORRECTION-REQUIRED`. **Nature of this revision:** **CONSISTENCY PATCH.** No new theory, no new result, no proof change, and **nothing removed**. Four `S1` consistency items are closed: a missing contribution-table row, stale theorem labels inside the verification registry, stale round counts in the companion document, and incomplete artifact isolation for degraded runs. One guard is widened so that the class of defect which produced the second of these becomes machine-detectable. **Release label:** **MANUSCRIPT DRAFT — CONSISTENCY PATCH APPLIED; PROPOSED FREEZE FOR EXTERNAL REVIEW.** `REVIEW READY` is still not claimed. Eight review rounds have run, all at independence `ι ≈ 0.2` (same AI lineage, continuous context) — these are **low-independence self-audits**, not independent peer review. No qualified human proof review; `D-M63-PRIOR` is `0 %`; no DOI. **Audit response:** round-by-round tables are in `ZS-M63_audit_response_v1_6_2.md`. Exploratory derivation scripts, restored to the bundle as a supplement, are in `supplement_exploration/` and are **not** part of the verification contract. **Verification artifact:** `zs_m63_verify_v1_6_2.py` — 1734 lines, `sha256(py) = d9eb1a898786b1d6…`, registry row map `sha256 = f28193ef464249f8…` — **68 rows, 0 FAIL, exit 0**, JSON byte-identical on re-run and machine-independent (the ledger records only the manuscript basename). Pinned runtime embedded (`--print-requirements`); degraded path testable (`--no-sympy`); manuscript guard **fail-closed**; artifact names carry the run profile **including the degraded mode**, so neither a `--quick` nor a `--no-sympy` run can touch a canonical deliverable.

---

## 0\. Consistency patch v1.6.2

The v1.6.1 audit returned **AUDIT-PASS-MINOR** with **`RELEASE-BLOCKING: NO`**, confirmed the four fixed-environment replays (`FULL` 68/0, `QUICK` 68/0, `--no-sympy` 60/8 exit 1, `QUICK --no-manuscript` 66/2 exit 1), reproduced the ledger digest `a2d0bd5d…` byte-for-byte, and re-checked the proof of Theorem 9.8 as sound. Four `S1` consistency items remained; all are closed here, and **nothing is removed**.

| \# | Item | Where | Correction |
| :---- | :---- | :---- | :---- |
| **V1** | **The contribution table stopped at Theorem 9.6 and never listed Theorem 9.8** — the result that raised the paper's mathematical value most. | Contribution table | Row 21 added, with the audit's own wording: own strengthening, Stone–Weierstrass imported, independent proof review pending, evidence `§9.8` proof and `F8` as a **sampled** diagnostic |
| **V2** | **The verification registry still carried pre-renumbering labels**: `F3` said "Thm 9.4", `F4`–`F6` said "Thm 9.5", and the `F7` call site said "Remark 9.3". Because `S3` only checks that the manuscript table is *byte-identical to the registry*, a wrong label present in **both** was invisible. | `ROW_SPEC`, row map, observations, JSON | Labels corrected to `9.5` / `9.6` / `9.4` and all four artifacts regenerated together. **`S5` is widened**: every `Thm x.y`, `Prop x.y`, `Remark x.y`, `Lem x.y`, `Cor x.y` label appearing in `ROW_SPEC` must exist as the corresponding heading in the manuscript. This is exactly the hole that let `V2` survive two rounds |
| **V3** | **The companion response document still said "three of the four rounds" and "a fifth audit outside this lineage"**, which no longer matches an eight-round history; and the superseded `N = 8` record carried no pointer to its correction. | `ZS-M63_audit_response_v1_6_2.md` | Counts brought up to date; the `N = 8` entry now carries an explicit "superseded by W3: the true first value is `N = 7`" annotation, so the lineage of that number is readable |
| **V4** | **Degraded runs were not artifact-isolated.** `--no-sympy` wrote the canonical output names, so a failing ledger could overwrite a good `FULL` one, and a stale certificate left on disk could let `S7` pass. | verifier | The profile suffix now records the degraded mode too (`.no_sympy`), so a degraded run never writes a canonical artifact and `S7` cannot be satisfied by a leftover file |

**Explicitly not done, and explicitly not removed.** No new theorem, no strengthening, no new verification row, and no deletion of existing content — the explicit chamber polynomials of §7.3, the exact Gram certificate tables of Proposition 7.6, the full imported-results table and the objection list are all retained verbatim. §7.3 exhaustiveness stays `[열림]` under `D-M63-ATLAS`; `D-M63-PRIOR` stays at `0 %`.

**Restored to the bundle.** At the reviewer's prompting we re-checked what earlier rounds had dropped from the delivery. The exploratory derivation scripts — the searches that produced Lemma 5.2, Propositions 5.6–5.7, the Yang–Xie normalization mapping, the exact Gram certificate and Theorem 9.8 — were removed from the bundle in the v1.2 cleanup. They are restored under `supplement_exploration/`, clearly marked **exploratory, class `X`, not part of the verification contract**, because they document how each result was found and let a reviewer retrace it. Nothing else was found missing: the v1.4 relocation of the round-by-round tables to a companion document was audit-endorsed, and the superseded manuscript versions are deliberately not shipped.

---

## 0′. Completion patch v1.6.1 (retained for the record)

The v1.6 audit returned **AUDIT-PASS-MINOR**: central contribution survives, highest severity `S1`, and the explicit recommendation *not* to add theory but to close the remaining local items and freeze. All eleven were accepted; none required a proof change.

| \# | Item | Where | Correction |
| :---- | :---- | :---- | :---- |
| **W1** | `Ψ = S` was used without stating `S ∈ C(Ω_u;ℝ^p)` | Thm 9.6 / Cor 9.7 | Continuity of `S` is now a hypothesis of Theorem 9.6, inherited by Corollary 9.7 and Theorem 9.8 |
| **W2** | Row `F8` reported `η` as if it were a uniform lower bound on `λ_{\min}(\mathrm{Cov}_bS)` over the convex box, when it was a minimum over six sampled `b` | `F8`, §9.8 | Relabelled `\hatη` and declared a **sampled diagnostic**, not a certified uniform bound. Interval-arithmetic certification is recorded as an open item, not claimed |
| **W3** | `F8` said "first `N = 8`" while testing a non-contiguous ladder | `F8`, §9.8 | The ladder is contiguous over `1..12`. **The corrected value is `N = 7`, not `8`** — the audit's suspicion was right, and the skipped rungs had hidden it |
| **W4** | The abstract fell back to `e^{−ρn^α}` after §9.5 had fixed it | Abstract | Unified to `e^{−ρ(n+1)^α}` with the logarithmic form named as such |
| **W5** | "By Weierstrass" left the classical input unnamed | Thm 9.8 | Named: **Stone–Weierstrass** (equivalently Weierstrass's second approximation theorem for continuous `2π`\-periodic functions) |
| **W6** | Contribution row 15 still said "Thm 7.3" after §7.3 was demoted | Contribution table | Now "§7.3 candidate chamber reduction (not a theorem)" |
| **W7** | Import `I-15` and §9.1 still pointed at pre-renumbering theorems | §9.1, §11 | Cross-references synchronised to `9.3 / 9.4 / 9.5 / 9.6 / 9.7 / 9.8` |
| **W8** | A second `§9.7` heading appeared after Corollary 9.7 and Theorem 9.8 | §9 | The phase diagram is now **§9.9** |
| **W9** | The manifest said "66 rows" while the suite emits 68 | §12 | Corrected; the count is also machine-checked by `S2` and `S5` |
| **W10** | The bundle claimed a canonical FULL JSON that was not shipped | delivery | The FULL ledger JSON is shipped, and the ledger digest is now machine-independent because `S3` records only the manuscript basename |
| **W11** | The audit-response document said "six independent audits", contradicting `ι ≈ 0.2` | companion | Reworded to "**low-independence self-audits**" throughout |

**Explicitly not done.** No new theorem, no strengthening, no new verification row. §7.3 exhaustiveness stays `[열림]` under `D-M63-ATLAS`; `D-M63-PRIOR` stays at `0 %`.

---

## Abstract

Let `Ω` be a compact space with an involution `R`, and `𝒜(μ) = d_TV(μ, R_#μ) ∈ [0,1]`. Given finitely many observables `∫Φ dμ = v`, the compatible measures form a fiber on which `𝒜` ranges over `𝓘(v) = [A⁻(v), A⁺(v)]` of width `W(v)`.

The width is maximal wherever the data are not extreme. If the carrier has a dense `R`\-free selector, every `v` in the relative interior of the attainable data body admits a representing measure mutually singular to its reflection, so `A⁺(v) = 1` with support at most `d+1`. For truncated trigonometric moments this gives `A_n⁺(m) = 1` on the circle and on every symmetric arc, hence a minimax law `Δ_n := \sup_m W_n(m) = 1` at every finite order.

The atom count is then sharpened to `n+1`, which is optimal. Two ingredients combine: an annihilator lemma making distinct minimal representations disjointly supported; and a first-order eigenvalue perturbation identity showing the canonical one-parameter quadrature families move **co-monotonically**. On the circle the family is a unitary upper Hessenberg matrix whose last diagonal entry carries the parameter, with `dθ_j/dφ = |v_j(N)|² > 0` and `Σ_j|v_j(N)|² = 1`; on a proper arc, after tangent half-angle transport to a Hausdorff moment problem, the parameter is the free last Jacobi diagonal entry `σ` and `dλ_j/dσ = |v_j(N)|² > 0`. The admissible set is the single interval `Σ = [σ_-, σ_+]` with Schur-complement endpoints, and

`σ_+ − σ_- = 2T·det L / det(T²I − J_n²) > 0  ⟺  L ≻ 0  ⟺  m ∈ ri 𝓜_{n,u}`,

so existence is self-contained. Given that existence, collisions are finite by co-monotonicity, and the count is sharpened algebraically: the node polynomial is affine in `σ`, so the eliminant `Res_x(p(x;σ), p(−x;σ))` has degree at most `2n+1`, with leading coefficient `−2\,\mathrm{Res}(p_n, p_n∘(−\mathrm{id}))` — exactly `2n+1` precisely when no two order-`n` Gauss nodes are mutual reflections, and strictly smaller when they are.

On the boundary the representing measure is unique and `W_n = 0`; assuming `A_n⁻` is continuous up to the boundary, the jump of `W_n` equals `1 − 𝒜(μ_m)`.

Quantitatively, `A_n⁻(m) = 1 − t_*` with `t_*` the largest symmetric submass. At `n = 2` this reduces to a one-variable semialgebraic feasibility problem, and the odd-data stratum has the closed form `A₂^{odd}(y_1,y_2) = |y_2|` if `y_2² ≥ 2y_1²`, else `2y_1²/√(4y_1²−y_2²)`. Five explicit chamber polynomials of degrees `5, 4, 3, 2, 2` are printed, with a degree-`8` eliminant whose leading coefficient is `256(4y_1²−y_2²)²` — the same discriminant that bounds the odd-gauge formula. The dual side carries an **exact rational Gram certificate**: nonnegativity of `1−P` and of `−(P+P∘R)` is certified on the whole circle by rational Hermitian Gram matrices with exactly positive leading minors, giving certified rational lower bounds on `A_2⁻`. On a proper arc the residual cone is `T_2(r) ⪰ 0` together with a `2×2` localizing Toeplitz matrix that we verify **equals `2×` the Yang–Xie localizer**, so the arc characterization is exact, not conditional.

Finally: on Sobolev balls `Δ_n` is pinned two-sidedly with constant ratio `π/√2`; on Gevrey classes it decays like `e^{−ρ(n+1)^α}` in a declared regime, with `\log Δ_n ∼ −ρn^α` as the only claim in the cruder exponent; on a regular minimal `p`\-parameter Gibbs family over a convex compact box the mean-parameter map is injective with an explicit inverse modulus. The Z-Spin application is a conditional full-circle diagnostic only.

Priority is not claimed for any statement: `D-M63-PRIOR` is OPEN and the words *new*, *first*, *novel*, *unique* are not used as priority claims.

---

## Contribution table

| \# | Result | Own vs imported | Status | Evidence |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Thm 4.1 dense-selector saturation `A⁺(v)=1`, support `≤ d+1` | own statement; `ri(cl C)=ri C` \+ Carathéodory imported | `[검증됨]` | `G3` |
| 2 | Cor 4.3 / 4.4 Fourier saturation, circle and arc | specialization | `[검증됨]` | `B3`, `C7` |
| 3 | Lem 5.1 disjoint supports of minimal representations | own, elementary | `[검증됨]` | `C8` |
| 4 | Lem 5.2 co-monotonicity identity `dθ_j/dφ = dλ_j/dσ = |v_j(N)|² > 0` | own derivation; classical perturbation theory | `[검증됨]` | `B5`–`B7`, `C3`–`C4` |
| 5 | Thm 5.3 circle `κ_R(m) = n+1` | own reflection argument; Szegő quadrature imported | `[가설]` awaiting re-audit | `B1`–`B8` |
| 6 | **Prop 5.6 arc admissible interval and exact non-degeneracy** | **own** | `[검증됨]` | `C9`, `C10` |
| 7 | **Prop 5.7 collision eliminant: `\deg ≤ 2n+1`, leading coefficient `−2Res(p_n,p_n∘(−id))`, exact degree iff that resultant `≠ 0`** | **own** | `[검증됨]` in the corrected conditional form; the universal exact-degree claim of v1.3 is **withdrawn** | `C11` |
| 8 | Thm 5.5 proper arc `κ_R(m;u) = n+1` | own; Jacobi/Gauss family imported | `[가설]` — now self-contained via Prop 5.6–5.7 | `C1`–`C11` |
| 9 | Thm 6.2 dichotomy | synthesis | boundary half `[검증됨]` imported; interior half inherits §5 | `E1`, `G1` |
| 10 | Thm 6.3 fragility identity | own | `[가설]` — continuity hypothesis in the theorem line | `G1` |
| 11 | Thm 6.4 minimax `Δ_n = 1` | corollary | `[검증됨]` | `G2` |
| 12 | Thm 6.1 `n=1` closed form | **not own** — M62 Thm 8 at `u=π` | `[검증됨]` cross-route | `E1`, `E1b`, `E2` |
| 13 | Thm 7.1 matrix peeling | reformulation of M62 Thm 2–3 (corrected scope) | `[검증됨]` | `A3` |
| 14 | Thm 7.2 `n=2` one-variable reduction, `0<t<1` | own | `[검증됨]` | `A1`–`A3`, `E6`, `E13` |
| 15 | §7.3 candidate chamber reduction with **explicit** polynomials (not a theorem) | own | `[열림]` — active-set completeness not proved | `E8`, `E9` |
| 15b | **Prop 7.6 exact rational Gram certificate and certified lower bound on `A_2⁻`** | **own**; Fejér–Riesz imported | `[검증됨]` | `E12` |
| 16 | Thm 7.4 odd-gauge closed form | own formula; M62 Thm 16 supplies the body | `[검증됨]` | `E3`–`E5` |
| 17 | **Thm 8.3 arc `n=2` exact characterization** | own; Yang–Xie Thm 2 imported, **normalization now verified** | `[검증됨]` — `F-M63.ARC` CLOSED | `E7`, `E11` |
| 18 | Thm 9.3 Sobolev two-sided constants, ratio `π/√2` | own sharpening | `[검증됨]` in the declared regime | `F1`, `F2` |
| 19 | Thm 9.5 Gevrey law, `n ≥ n_0` | specialization | `[가설]` | `F3` |
| 20 | Thm 9.6 Gibbs exact selection on a convex box | imported mechanism | `[가설]` | `F4`–`F6` |
| 21 | **Thm 9.8 finite Fourier saturation: `N_0(𝓒) ≤ N < ∞` for every continuous `S`** | **own strengthening**; Stone–Weierstrass imported; replaces the withdrawn Corollary 9.6′ of v1.5 | `[검증됨]`, **independent proof review pending** | proof §9.8; `F8` (a **sampled** diagnostic, not a certified instance) |

---

## Non-claims

**NC-1.** Nothing derives a physical boundary state, an effective action, or the Z-Spin intertwiner. `D-M61-IOTA` is OPEN and untouched. **NC-2.** §10 is a diagnostic on the *relaxed full circle*, not an arc statement. **NC-3.** The quadrature families of §5 are classical; the own contributions are Lemmas 5.1–5.2, Propositions 5.6–5.7, the reflection-avoidance argument, and the optimality statements. **NC-4.** `D-M63-PRIOR` is `0 %`. "Own" means *not derived from a source we have read*, never *not in the literature*. **NC-5.** No script row proves a theorem; class `P = 0` by construction. **NC-6.** §7.3 prints its chamber polynomials but does **not** prove that the active-set list is complete, nor recover extremizers in closed form. It is a reduction, not an atlas. **NC-7.** Row `E12` certifies a **shifted** rational dual point; the certified value lies below the LP optimum by at most the reported gap (`1.0·10⁻⁴` in the tested cases). The certificate is exact for that shifted point; it does **not** certify LP optimality.

---

# 1\. Introduction

## 1.1 The question

Given finitely many exact observables, how much of the symmetry-breaking functional `𝒜(μ) = d_TV(μ, R_#μ)` is determined? Without structural restrictions, nothing beyond a floor; with structure, the ambiguity collapses at a computable rate or exactly.

## 1.2 What is at stake

Classical is: finitely many moments do not determine a measure. Not classical, and what this paper is about: the exact **value** of the upper envelope of a symmetry functional over a truncated fiber; the **sharp atom count** of a reflection-free representing measure on the circle and on an arc; and an exact reduction of the second-order lower envelope, closed in the odd stratum and, on the arc, characterized exactly.

## 1.3 Revision history of the technical core

v1.0 deduced finiteness of the reflection-collision set from monotonicity of individual nodes, which is invalid. v1.1 replaced that with a common-direction identity. v1.2 corrected a false quantitative claim in that repair (the per-node shift), supplied the missing existence proof for the arc admissible interval, and added an algebraic bound on the collision set — a bound that *sharpens* an existence already obtained, not an independent one. v1.3 replaced a grid-based "certificate" with an exact rational Gram certificate. v1.4 is correction-only: it withdraws an over-general degree claim, fixes a margin constant and an arithmetic slip, repairs the dependency-failure path, and adds self-referential guards.

---

# 2\. Setting and conventions

`Ω` compact metric, continuous involution `R`, `R² = id`. `𝒜(μ) := d_TV(μ, R_#μ) = ½‖μ − R_#μ‖_var` (locked; rows `D1`, `T1`).

`Φ : Ω → ℝ^d` continuous; `M := conv Φ(Ω)`; `𝓕(v) := {μ : ∫Φ dμ = v}`.

Trigonometric case: `Ω_u = [−u,u]`, `0 < u ≤ π`; `R(θ) = −θ`; `Φ_n(θ) = (\cos θ, \sin θ, …, \cos nθ, \sin nθ)`, `d = 2n`; `m_k = ∫e^{ikθ}dμ`, `m_0 = 1`, `m_{−k} = \bar m_k`; `T_n(m) = [m_{j−k}]`; `𝓜_{n,u} := conv Φ_n(Ω_u)`. `𝓕_n(m;𝕋) ≠ ∅ ⟺ T_n(m) ⪰ 0`; `m ∈ int 𝓜_{n,π} ⟺ T_n(m) ≻ 0`.

Row `A1` (symbolic difference exactly `0`): `det T_2 = 1 − 2|m_1|² − |m_2|² + 2\Re(m_1²\bar m_2)`.

---

# 3\. The identification interval

**Definition 3.1.** `A⁻ := \inf_{𝓕(v)}𝒜`, `A⁺ := \sup_{𝓕(v)}𝒜`, `𝓘 := [A⁻,A⁺]`, `W := A⁺ − A⁻`. `A⁻` is attained by weak compactness; `A⁺` is asserted only where a maximizer is constructed.

**Lemma 3.2.** `|𝒜(μ) − 𝒜(ν)| ≤ 2d_TV(μ,ν)`. Baseline.

**Proposition 3.3.** `A_n⁻ ≤ A_{n+1}⁻`, `A_n⁺ ≥ A_{n+1}⁺`, `W_{n+1} ≤ W_n` (row `G4`).

**Lemma 3.4.** For finitely atomic `μ`, `𝒜(μ) = 1` iff `supp μ ∩ R(supp μ) = ∅`.

---

# 4\. Saturation

## Theorem 4.1 (Dense-selector saturation)

*If `Ω` is compact, `Φ` continuous, and `Ω` has a dense `R`\-free subset `D`, then every `v ∈ ri M` has a representing `μ_v` with `supp μ_v ⊂ D`, `|supp μ_v| ≤ d+1`, so `A⁺(v) = 1`, attained.*

**Proof.** `C := conv Φ(D)` satisfies `\overline C = M` by density and compactness. For nonempty convex `C ⊂ ℝ^d`, `ri(\overline C) = ri C`, so `v ∈ ri M = ri C ⊆ C`. Carathéodory gives `x_0,…,x_d ∈ D` with `v = Σp_jΦ(x_j)`. The support lies in the `R`\-free set `D`; apply Lemma 3.4. ∎

**Corollary 4.3 (circle).** `T_n(m) ≻ 0 ⟹ A_n⁺(m;𝕋) = 1`. **Corollary 4.4 (arc).** `0<u<π`, `m ∈ ri 𝓜_{n,u} ⟹ A_n⁺(m;Ω_u) = 1`, support `≤ 2n+1` (row `G3`).

---

# 5\. Sharp reflection-free atomic complexity

## Lemma 5.1 (Disjoint supports of minimal representations)

*Let `V` have dimension `N` with the property that any `q ≤ N` distinct points give an evaluation matrix of rank `q`. If `μ ≠ μ'` represent the same `V`\-data with at most `(N+1)/2` atoms each, their supports are disjoint.*

**Proof.** `ν := μ − μ' ≠ 0` annihilates `V`, so `|supp ν| ≥ N+1`; but `|supp μ|+|supp μ'| ≤ N+1`, forcing disjointness. ∎ (row `C8`)

**Lemma 5.1′.** `T_n(m) ≻ 0` implies every `μ ∈ 𝓕_n(m)` has at least `n+1` atoms (row `B8`).

## Lemma 5.2 (Co-monotonicity identity)

*For a differentiable family of normal matrices with simple spectrum,* *(a) `H(φ) = U_0·diag(1,…,1,e^{iφ})` unitary, eigenvalues `e^{iθ_j(φ)}`: `dθ_j/dφ = |v_j(N)|²`;* *(b) `H(σ) = J + σ e_N e_N^*` Hermitian: `dλ_j/dσ = |v_j(N)|²`.* *Both are strictly positive when the last eigenvector component is nonzero, so **all eigenvalues move in the same direction**. In case (a), unitarity additionally gives `Σ_j|v_j(N)|² = 1`.*

**Proof.** (a) `dH/dφ = iHP_N`; for a simple eigenvalue of a normal matrix `dλ_j/dφ = v_j^*(dH/dφ)v_j = i\,v_j^*HP_Nv_j = iλ_j|v_j(N)|²`, and `λ_j = e^{iθ_j}`. (b) `dH/dσ = P_N`. The trace identity `Σ_j|v_j(N)|² = (V^*V)_{NN} = 1` holds because `V` is unitary. ∎

**Positivity of the last component.** For a unitary upper Hessenberg matrix with positive subdiagonal, or a Jacobi matrix with positive off-diagonal, the eigenvector components obey a nondegenerate recursion in which the last component cannot vanish. Rows `B6` (`4.4·10⁻¹⁰`, `min|v(N)|² = 1.8·10⁻²`), `B7` (`Σ = 1` to `8.9·10⁻¹⁶`), `C3` (`2.1·10⁻¹⁰`).

**Correction of a v1.1 statement (audit Q1).** v1.1 asserted that each node advances by exactly `2π/(n+1)` over a full turn. That is **false**: only the *sum* of the advances is `2π`, which is precisely `Σ_j|v_j(N)|² = 1` integrated. Row `B5` records measured per-node shifts such as `(0.2907, 0.3124, 0.3969)` turns at `n=2` — unequal, summing to `1`. Nothing downstream depends on the false clause: the collision argument uses only the total `Σ_lΔ_l = 2π`, applied **separately** to `j < k` and to `j = k` as in Step 5 of Theorem 5.3.

## Theorem 5.3 (circle: `κ_R(m) = n+1`)

*Let `T_n(m) ≻ 0`. For all but finitely many `τ ∈ 𝕋`, the `(n+1)`\-node Szegő rule generated by `B_τ(z) = zΦ_n(z) − \barτΦ_n^*(z)` gives `μ_τ ∈ 𝓕_n(m;𝕋)` with reflection-disjoint support. Hence `A_n⁺(m;𝕋) = 1` and `κ_R(m) = n+1`, optimal.*

**Proof.** *Steps 1–2 (imported).* `Φ_n` exists with zeros in the open disk, so `Φ_n^*` is nonvanishing on `|z| ≥ 1` (row `B1`); `B_τ` has `n+1` simple zeros on `𝕋` carrying positive Szegő weights exact on `Λ_{−n,n}` (row `B3`). *Step 3 (own).* A common root of `B_τ, B_{τ'}` forces `Φ_n^*(z_0) = 0` with `|z_0| = 1`, impossible (row `B2`). *Step 4 (own).* The node polynomial is the characteristic polynomial of `G(φ) = G_0⋯G_{n−1}·diag(1,…,1,e^{iφ})`; Lemma 5.2(a) gives a **common direction** for all nodes, with total advance `Σ_jΔ_j = 2π` (row `B5`). *Step 5 (own; corrected in v1.3, audit A3).* Write `N = n+1`. Two cases must be separated. For `j < k`, the sum `θ_j + θ_k` increases over one turn by `Δ_j + Δ_k < Σ_lΔ_l = 2π` (strict because the remaining `N−2 ≥ 1` increments are positive when `N ≥ 3`), so it meets `0 \bmod 2π` **at most once**. For `j = k`, the collision condition is `2θ_j ≡ 0 \bmod 2π`, i.e. `θ_j ∈ \{0, π\}`; since `θ_j` advances by `Δ_j < 2π`, it passes each of the two fixed points **at most once**, so at most twice in total. Hence `|𝓑| ≤ \binom N2 + 2N = N(N+3)/2`, with **no exceptional case**: when `N = 2` the pair sum increases by exactly `2π`, so on the parameter circle it winds once and meets `0` exactly once, and `\binom22 + 2·2 = 5 = N(N+3)/2` — v1.3 added a spurious `+1` here (audit Z4). v1.2 wrote `Δ_j+Δ_k ≤ 2π` for **all** pairs including `j = k`, which is false; the correction changes only the constant. Row `B4`, class `X`. *Step 6\.* Choose `τ ∉ 𝓑`; Lemma 3.4 and Lemma 5.1′ finish. ∎

## Theorem 5.5 (proper arc: `κ_R(m;u) = n+1`)

*Let `0<u<π`, `m ∈ ri 𝓜_{n,u}`. There is `μ ∈ 𝓕_n(m;Ω_u)` with exactly `n+1` atoms, positive weights, reflection-disjoint support. Hence `A_n⁺(m;Ω_u) = 1` and `κ_R(m;u) = n+1`, optimal.*

**Proof.** *Step 1 (transport).* With `z = \tan(θ/2) ∈ [−T,T]`, `T = \tan(u/2)`, and `e^{ikθ} = (1+iz)^{2k}(1+z²)^{−k}`, set `dν := (1+z²)^{−n}dμ`. Then `m_k = ∫(1+iz)^{2k}(1+z²)^{n−k}dν` and `1 = ∫(1+z²)^ndν`, all of degree `≤ 2n`, and the induced map on `ℝ^{2n+1}` is a bijection preserving positivity, atoms and `z ↦ −z`. **The arc problem is the truncated Hausdorff moment problem of order `2n` on `[−T,T]`** (row `C1`, `1.7·10⁻¹⁶`). *Step 2 (parametrization).* `ν_0,…,ν_{2n}` determine `a_0,…,a_{n−1}` and `b_1,…,b_n`, while `a_n` is **free** — it is the image of the free moment `ν_{2n+1}`. Put `J(σ) := \mathrm{tridiag}(b;(a_0,…,a_{n−1},σ);b)`. Its Gauss rule has `n+1` nodes, positive weights, and is exact to degree `2n` for every `σ` (row `C2`). *Step 3 (co-monotonicity).* `J(σ) = J + σe_{n+1}e_{n+1}^*`, so Lemma 5.2(b) gives `dλ_j/dσ = |v_j(n+1)|² > 0` for every `j` (rows `C3`, `C4`). *Step 4 (existence, Prop 5.6).* `Σ := {σ : λ_j(σ) ∈ [−T,T]\ ∀j}` is a single interval `[σ_-,σ_+]` with the explicit endpoints and the exact non-degeneracy identity of Proposition 5.6; `m ∈ ri 𝓜_{n,u}` gives `σ_- < σ_+`. *Step 5 (finiteness).* Here `σ` runs over an interval, not a circle, so no self-pair subtlety arises: each `λ_j + λ_k` (including `j = k`, which is `2λ_j`) is strictly increasing and therefore vanishes at most once. With `N = n+1` the collision set has at most `\binom N2 + N = N(N+1)/2` points (row `C6`, class `X`). Proposition 5.7 then sharpens the count algebraically — **on top of this existence argument, not independently of it**. *Step 6\.* Pick a collision-free `σ` and transport back (row `C7`). Optimality: `r ≤ n` atoms would place `m` on `∂𝓜_{n,u}`. ∎

## Proposition 5.6 (arc admissible interval; audit Q2)

*Write `J_n` for the leading `n×n` block of `J(σ)`, `e_n` for the last coordinate vector of `ℝ^n`, `b_n > 0` for the coupling entry. Then*

`Σ = [σ_-, σ_+]`, `σ_- = −T + b_n²\,e_n^{\!*}(J_n + T I)^{-1}e_n`, `σ_+ = T − b_n²\,e_n^{\!*}(T I − J_n)^{-1}e_n`,

*and, with `M_0 := T²I − J_n²` and `L := M_0 − b_n² e_ne_n^{\!*}`,*

`σ_+ − σ_- = 2T\bigl(1 − b_n²\,e_n^{\!*}M_0^{-1}e_n\bigr) = 2T\,\dfrac{\det L}{\det M_0}`.

*`L` is the moment matrix of `(T²−x²)\,dν` in the orthonormal polynomial basis, so `Σ` is nondegenerate **iff** `L ≻ 0` **iff** `m ∈ ri 𝓜_{n,u}`.*

**Proof.** `λ_{\min}(J(σ)) ≥ −T ⟺ J(σ)+TI ⪰ 0`. Since `J(σ)+TI` is `[[J_n+TI, b_ne_n],[b_ne_n^*, σ+T]]`, and `J_n+TI ≻ 0` because the order-`n` Gauss nodes lie in `(−T,T)`, the Schur complement gives `σ + T − b_n²e_n^*(J_n+TI)^{-1}e_n ≥ 0`, i.e. `σ ≥ σ_-`. Symmetrically `TI − J(σ) ⪰ 0 ⟺ σ ≤ σ_+`. Diagonalizing `J_n` with eigenvalues `ξ_i ∈ (−T,T)` and writing `w_i` for the components of `e_n`,

`e_n^*(J_n+TI)^{-1}e_n + e_n^*(TI−J_n)^{-1}e_n = Σ_i w_i²\bigl[\tfrac1{T+ξ_i}+\tfrac1{T−ξ_i}\bigr] = 2T\,e_n^*M_0^{-1}e_n`,

which gives the first identity; the matrix determinant lemma gives the second. Finally, in the orthonormal basis `p_0,…,p_{n−1}`, `⟨p_i, x²p_j⟩_ν = (J²)_{ij} = (J_n²)_{ij} + b_n²δ_{i,n−1}δ_{j,n−1}` for `i,j ≤ n−1` — independent of `σ`, as it must be — so `⟨p_i,(T²−x²)p_j⟩_ν = (M_0 − b_n²e_ne_n^*)_{ij} = L_{ij}`. For the order-`2n` Hausdorff problem on `[−T,T]`, `m` is interior iff the Hankel matrix and this localizing matrix are both positive definite. Since `M_0 ≻ 0`, the rank-one criterion gives `L ≻ 0 ⟺ b_n²e_n^*M_0^{-1}e_n < 1 ⟺ σ_+ > σ_-`. ∎

Rows `C9` (Schur endpoints vs a direct scan, `1.6·10⁻⁴` at scan step `6.8·10⁻⁵`) and `C10` (both identities to `2.2·10⁻¹⁵`; `\min λ_{\min}(L) = 3.8·10⁻²` over all cases).

## Proposition 5.7 (collision eliminant: degree bound and conditional exactness)

*The node polynomial satisfies `p_{n+1}(x;σ) = (x−σ)\,p_n(x) − b_n²\,p_{n−1}(x)`, hence is **affine in `σ`**. Put `𝓔(σ) := \mathrm{Res}_x\bigl(p_{n+1}(x;σ),\,p_{n+1}(−x;σ)\bigr)`. Then*

`\deg_σ 𝓔 ≤ 2n+1`,  `[σ^{2n+1}]\,𝓔 = −2\,\mathrm{Res}\bigl(p_n,\;p_n∘(−\mathrm{id})\bigr)`,

*so the degree is **exactly** `2n+1` **if and only if** `\mathrm{Res}(p_n, p_n∘(−\mathrm{id})) ≠ 0`, i.e. iff no two order-`n` Gauss nodes are mutual reflections (in particular no node sits at `0`). Whenever `𝓔 ≢ 0`, the reflection-collision set lies in `\{𝓔 = 0\} ∩ Σ` and has at most `2n+1` points.*

**Proof.** Expanding `\det(xI − J(σ))` along the last row gives the three-term identity, and `σ` occurs only in the entry `J_{n+1,n+1}`. The Sylvester matrix is `(2n+2)×(2n+2)` with entries affine in `σ`; the coefficient of `σ^{2n+2}` vanishes because the leading `x`\-coefficients of both arguments are `σ`\-free, and the next coefficient collects the resultant of the pure-`σ` parts `−σ p_n(x)` and `−σ p_n(−x)`, giving the stated leading term. A common root of `p_{n+1}(·;σ)` and `p_{n+1}(−·;σ)` is exactly a pair `λ_j = −λ_k`, including `λ_j = 0`. ∎

**Withdrawal of the v1.3 form (audit Z1).** v1.3 asserted `\deg_σ 𝓔 = 2n+1` *universally*. That is **false**. Take `n = 1` and `a_0 = 0` — a symmetric interior datum, realizable for any `0 < b_1 < T`. Then `p_1(x) = x`, `p_2(x;σ) = x² − σx − b_1²`, `p_2(−x;σ) = x² + σx − b_1²`, and

`𝓔(σ) = −4b_1²σ²`,  `\deg_σ 𝓔 = 2 < 3 = 2n+1`,

consistently with `\mathrm{Res}(p_1, p_1∘(−\mathrm{id})) = \mathrm{Res}(x,−x) = 0`. The same collapse occurs at `n = 2` with `a_0 = a_1 = 0`, where `p_2(x) = x² − b_1²` carries the reflection pair `±b_1` and the degree drops from `5` to `3`. Row `C11` now carries both cases as explicit **negative controls** alongside the generic checks; v1.3's `C11` tested only asymmetric data and therefore could not see the failure.

**Why nothing downstream moves.** No other statement in this paper used the exact-degree form. Theorem 5.5 obtains finiteness of the collision set from co-monotonicity (Step 5), and Proposition 5.7 only sharpens the resulting count. Remark 5.9 uses the bound `B ≤ 2n+1`, which survives verbatim under the hypothesis `𝓔 ≢ 0`.

**Scope (retained from the previous round).** Proposition 5.7 is **not** an independent second existence proof. The hypothesis `𝓔 ≢ 0` comes from Proposition 5.6 (which makes `Σ` a nondegenerate interval) together with Step 5 of Theorem 5.5 (which exhibits collision-free parameters in `Σ`). What it adds is a sharper purely algebraic bound — at most `2n+1` bad parameters against `N(N+1)/2` — plus a checkable criterion for when the eliminant degenerates.

**Remark 5.9 (a first quantitative consequence).** Combining Propositions 5.6 and 5.7, the admissible interval has exact length `L := |Σ| = 2T\,\det L_{\mathrm{loc}}/\det(T²I − J_n²)` and, when `𝓔 ≢ 0`, contains at most `B ≤ 2n+1` bad parameters. Those `B` points cut `Σ` into `B+1 ≤ 2n+2` subintervals, so the longest has length `≥ L/(2n+2)` and its midpoint `σ^\star` is collision-free with distance at least `L/(4n+4)` to the nearest bad parameter and to `∂Σ`. (v1.3 wrote `L/(2n+3)`, which the counting does not give — audit Z3.) This is a crude but explicit margin; converting it into a lower bound on the *reflection gap* `\min_{j,k}|λ_j + λ_k|` requires controlling `dλ_j/dσ = |v_j(N)|²` from below, which is open (`D-M63-QUANT`).

**Remark 5.8.** Lemma 5.2 unifies the two carriers: in both cases the free parameter is the **last diagonal entry**, i.e. the one moment the truncated data leave undetermined — `τ` on the circle, `ν_{2n+1}` on the arc.

---

# 6\. Dichotomy, fragility, minimax

## Theorem 6.1 (`n=1` closed form, full circle)

*For `m_1 = x+iy`, `x²+y² ≤ 1`, `a := 1−|x|`: `A_1⁻ = |y|` if `|y| ≤ a`; `A_1⁻ = (y²+a²)/(2a)` if `|y| > a`; and **`A_1⁻ = 0` when `a = 0`**, i.e. `m_1 = ±1`.*

**Proof.** Region I: `2|y| ≤ 2𝒜` with equality attained by `|y|δ_{i·\mathrm{sgn}\,y}` plus a symmetric remainder, feasible iff `|x| ≤ 1−|y|`. Region II: a two-atom construction at `\tan(θ^*/2) = a/|y|`. Dual: Theorem 7.5 at `n=1` returns the same value, so the gap is zero. `a = 0` is degenerate: the unique representing measure is a point mass at a fixed point. ∎ (rows `E1`, `E1b`, `E2`)

This equals `ZS-M62 v1.4.2` Theorem 8 at `u = π` and is **not** a contribution; it is a cross-route certificate reproducing `A_* = 0.763362818245963536` to double-precision zero.

## Theorem 6.2 (saturation–rigidity dichotomy)

`W_n(m;u) = 1 − A_n⁻(m;u)` on `ri 𝓜_{n,u}`;  `W_n(m;u) = 0` on `∂𝓜_{n,u}`.

**Proof.** Interior: Theorems 5.3 / 5.5. Boundary: `c ∈ \ker T_n` gives `∫|p|²dμ = 0`, so every representing measure sits on the finite zero set of `p`, and Carathéodory–Fejér gives uniqueness; on a proper arc, T-system boundary uniqueness. ∎

## Theorem 6.3 (fragility identity)

*Assume `A_n⁻` is continuous up to `m^∂ ∈ ∂𝓜_{n,u}` with unique representing measure `μ_{m^∂}`. Then `W_n(m^∂) = 0` and `\lim_{m→m^∂,\,m∈ri}W_n(m) = 1 − 𝒜(μ_{m^∂})`.*

The continuity hypothesis is verified only at `n = 1`; otherwise `D-M63-CONT`. Row `G1`: at the fixed point `+1`, `W → 1.00000` (predicted jump `1`); at four other boundary arguments `W → 8.9·10⁻⁴` or less (predicted `0`).

## Theorem 6.4 (minimax impossibility)

`Δ_n := \sup_m W_n(m;u) = 1` for every finite `n`; `N_ε = ∞` for every `ε < 1`.

**Proof.** Take `m` from a symmetric measure of full support: `A_n⁻ = 0`, and §5 gives `A_n⁺ = 1`. ∎ (row `G2`)

---

# 7\. Second-order geometry on the full circle

## Theorem 7.1 (matrix peeling)

`A_n⁻(m) = 1 − t_*`, `t_* = \max\{s_0 : s \text{ real}, S_n(s) ⪰ 0, T_n(m) − S_n(s) ⪰ 0\}`,

*equivalently `A_n⁻(m) = \min\{A : m ∈ (1−A)𝓢_n + A𝓜_n\}`.* Restatement of `ZS-M62` Thms 2–3 in their corrected form; not a contribution.

## Theorem 7.2 (`n=2` one-variable reduction)

*Assume `0 < t < 1`, `A := 1−t ∈ (0,1)`. With `u_1 := \Re r_1` (so `\Im r_1 = y_1` is fixed),*

`X := Ax_2 − u_1² + y_1²`, `Y := Ay_2 − 2u_1y_1`, `R := A² − u_1² − y_1²`, `D := R² − Y²`,

*`t` is feasible iff there is `u_1` with `|x_1−u_1| ≤ t`, `R ≥ 0`, `D ≥ 0`, and*

`\bigl[\tfrac{u_1²−y_1²−\sqrt D}{A}, \tfrac{u_1²−y_1²+\sqrt D}{A}\bigr] ∩ \bigl[x_2−t,\ x_2+t−\tfrac{2(x_1−u_1)²}{t}\bigr] ≠ ∅`.

*Then `A_2⁻(m) = 1 − \sup\{\text{feasible }t\}`.*

**Degenerate clause (audit Q8).** `t = 0` is always feasible (take the symmetric part to be zero) and is handled before any division; `A = 0` occurs only for data attainable by a purely symmetric measure, where `A_2⁻ = 0` directly. Row `E13`.

**Proof.** Row `A2` gives `S_2 ⪰ 0 ⟺ −1 ≤ c ≤ 1,\ 2c²−1 ≤ d ≤ 1`; row `A3` gives `A\det T_2(r) = (A²−|r_1|²)² − |Ar_2−r_1²|²`, so residual positivity is a disk in the complex `r_2`\-plane. Only `u_2 := \Re r_2` is free, because **symmetric measures have real moments and cannot move `y_1, y_2`**. ∎ (row `E6`)

## 7.3 Candidate chamber reduction (not a theorem)

The optimum of Theorem 7.2 is attained where some subset of the constraints is active. The five active sets **detected** in the reduction are listed below with their defining polynomials and guards. **No claim of exhaustiveness is made**, so this is a candidate list, not a classification theorem (audit X3). Writing `A = 1−t`, `c = (x_1−u_1)/t`:

| Chamber | Active constraint | `\deg_t` | `\deg_{u_1}` | Guards |
| :---- | :---- | :---- | :---- | :---- |
| I | `d = 2c²−1` | 5 | 4 | `R ≥ 0`, \` |
| II | \` | Y | \= R\` | 4 |
| III | `d = 1` | 3 | 2 | `R ≥ 0`, \` |
| IV⁺ | `u_1 = x_1 − t` | 2 | — | `R ≥ 0` |
| IV⁻ | `u_1 = x_1 + t` | 2 | — | `R ≥ 0` |

Explicitly, in expanded form,

F\_II  \= t^4 \- 4t^3 \- 2t^2 u1^2 \- 2t^2 y1^2 \- t^2 y2^2 \+ 6t^2 \+ 4t u1^2

        \- 4t u1 y1 y2 \+ 4t y1^2 \+ 2t y2^2 \- 4t \+ u1^4 \- 2u1^2 y1^2

        \- 2u1^2 \+ 4 u1 y1 y2 \+ y1^4 \- 2y1^2 \- y2^2 \+ 1

F\_III \= \-2t^3 x2 \+ 2t^3 \+ t^2 x2^2 \+ 4t^2 x2 \+ 4t^2 y1^2 \+ t^2 y2^2 \- 5t^2

        \+ 2t u1^2 x2 \- 2t u1^2 \+ 4t u1 y1 y2 \- 2t x2^2 \- 2t x2 y1^2 \- 2t x2

        \- 6t y1^2 \- 2t y2^2 \+ 4t \- 2u1^2 x2 \+ 2u1^2 \- 4u1 y1 y2 \+ x2^2

        \+ 2 x2 y1^2 \+ 2y1^2 \+ y2^2 \- 1

F\_IV± \= 4t^2 x1^2 ∓ 8t^2 x1 \- 4t^2 y1^2 ± 4t^2 y1 y2 \- t^2 y2^2 \+ 4t^2

        ∓ 4t x1^3 \+ 4t x1^2 ± 4t x1 y1^2 \- 4t x1 y1 y2 ± 4t x1 \+ 4t y1^2

        ∓ 4t y1 y2 \+ 2t y2^2 \- 4t \+ x1^4 \- 2x1^2 y1^2 \- 2x1^2

        \+ 4 x1 y1 y2 \+ y1^4 \- 2y1^2 \- y2^2 \+ 1

with `F_I` (the quintic, 41 terms) and the full eliminant printed in the companion artifact `zs_m63_chambers_v1_6_2.txt`. Row `E8` verifies all degrees `(5,4,4,4,3,2)` symbolically.

**Two structural checks.**

1. `F_II` factors exactly as `\bigl[A(A−y_2) − (u_1−y_1)²\bigr]\cdot\bigl[A(A+y_2) − (u_1+y_1)²\bigr]`, which are precisely the two factors of Theorem 7.4 — the chamber and the odd-gauge derivation agree.  
2. Eliminating `u_1` from Chamber II after interior stationarity gives a degree-`8` polynomial in `t` whose **leading coefficient is `256\,(4y_1²−y_2²)²`**. Its vanishing locus `y_2² = 4y_1²` is exactly where the odd-gauge closed form of Theorem 7.4 degenerates. The two computations therefore share their discriminant.

**Status `[열림]` (NC-6).** The polynomials and guards are explicit and reproducible, and row `E12` supplies whole-circle exact dual-feasibility certificates at three specified data points (Proposition 7.6). What remains unproved: that this list of active sets is exhaustive; the behaviour on double boundaries and repeated roots; closed-form recovery of the extremal atoms by rank factorization. Until those are supplied this is a reduction, not an atlas, and `D-M62-N2` is **reduced, not closed** (`D-M63-ATLAS`).

## Theorem 7.4 (odd-data gauge, closed form)

*Let `(y_1,y_2)` lie in the attainable odd-data body*

`Y_2(π) = \bigl\{(y_1,y_2) : |y_2| ≤ 1,\; 2y_1² − 1 ≤ \sqrt{1−y_2²}\bigr\}`

*— that is, `(y_1,y_2) = (\Im m_1, \Im m_2)` for some probability measure on `𝕋` (audit Y4; the domain was omitted in v1.4). If only `y_1, y_2` are prescribed and the real parts are free, then `A₂^{odd}(y_1,y_2) = |y_2|` if `y_2² ≥ 2y_1²`, and `= 2y_1²/\sqrt{4y_1²−y_2²}` otherwise.*

**Proof.** With real parts free only `D ≥ 0` survives, and `|Y| ≤ R` is the conjunction of `(u_1−y_1)² ≤ A(A−y_2)` and `(u_1+y_1)² ≤ A(A+y_2)`; the admissible set is an intersection of two intervals, nonempty iff `A ≥ |y_2|` and `2|y_1| ≤ \sqrt{A(A−y_2)}+\sqrt{A(A+y_2)}`, i.e. `2y_1² ≤ A² + A\sqrt{A²−y_2²}`. At the threshold, `A = 2y_1²/\sqrt{4y_1²−y_2²}` satisfies the two **exact rational identities** `A²−y_2² = (2y_1²−y_2²)²/(4y_1²−y_2²)` and `A² + A\sqrt{A²−y_2²} = 2y_1²`, valid while `y_2² ≤ 2y_1²`; otherwise `A = |y_2|` binds. Branches agree at `y_2² = 2y_1²`. ∎ (rows `E3`, `E4`, `E5`)

## Theorem 7.5 (dual formula)

`A_n⁻(m;𝕋) = \max\{∫P\,dμ_m : \deg P ≤ n,\ P(θ)+P(−θ) ≤ 0,\ P(θ) ≤ 1\}`.

Row `E10` (gap `≤ 1.8·10⁻⁵`); row `E9` is a **numerical dual candidate on a grid** and is labelled as such.

## Proposition 7.6 (exact rational Gram certificate; audit A1)

*Let `P` be a real trigonometric polynomial of degree `n` with rational coefficients, and write `a(θ) = (1,e^{iθ},…,e^{inθ})^{\!T}`. Suppose there are Hermitian matrices `G_1, G_2 ∈ ℚ(i)^{(n+1)×(n+1)}` with*

`Σ_i (G_1)_{i,i+k} = c_k(1−P)` and `Σ_i (G_2)_{i,i+k} = c_k\bigl(−(P+P∘R)\bigr)` for `0 ≤ k ≤ n`,

*and every leading principal minor of `G_1` and of `G_2` exactly positive. Then `1−P = a^*G_1a ≥ 0` and `−(P+P∘R) = a^*G_2a ≥ 0` **on the whole circle**, so `P` is dual-feasible and*

`A_n⁻(m) ≥ ∫P\,dμ_m`

*is a certified rational lower bound. No discretization enters the certificate.*

**Proof.** `a^*Ga = Σ_{i,j}G_{ij}e^{i(j−i)θ}`, whose `e^{ikθ}` coefficient is `Σ_iG_{i,i+k}`; the hypotheses make these coincide with the target coefficients, and positive leading minors give `G ⪰ 0` by Sylvester's criterion, hence `a^*Ga ≥ 0` pointwise. Dual feasibility plus Theorem 7.5 gives the bound. ∎

**Construction (row `E12`).** Solve the LP numerically, round the dual coefficients to rationals, subtract a rational shift so both constraints hold with a strict margin, peel a rational constant, factor the remainder numerically once to obtain a starting Gram matrix, rationalize it, repair the coefficient identity **exactly**, and add `(s/(n+1))I` to restore strict definiteness. Everything after the single numerical factorization is exact rational arithmetic. Certified results at `n = 2`:

| `m_1` | `m_2` | certified `A_2⁻ ≥` | LP value | gap |
| :---- | :---- | :---- | :---- | :---- |
| `1/5 + 3i/10` | `−1/10 + i/5` | `159049/500000 = 0.318098` | `0.3181986` | `1.0·10⁻⁴` |
| `−1/4 + i/4` | `1/5 − i/10` | `510111/2000000 = 0.2550555` | `0.2551557` | `1.0·10⁻⁴` |
| `3/10 − 2i/5` | `1/10 + i/4` | `105247/250000 = 0.420988` | `0.4210894` | `1.0·10⁻⁴` |

These are **three whole-circle exact dual-feasibility certificates, each within `1.1·10⁻⁴` of the numerical LP value** — they certify that the shifted rational `P` satisfies both dual constraints everywhere, **not** that the LP optimum has been attained (audit Y5; NC-7). The Gram matrices and their exact minors are written to `zs_m63_certificate_v1_6_2.txt`; for the first datum the minors of `G_1` are `26773/1500000`, `13296101/1.8·10^{12}`, `7197594893/2.7·10^{19}`, all exactly positive rationals. Row `E12b` retains the purely numerical factorization as a diagnostic, with its grid-measured residual stated as such (NC-7).

---

# 8\. Second-order geometry on a proper arc

## Proposition 8.1 (symmetric arc strip)

*For a symmetric measure on `Ω_u`, `γ := \cos u`, `c = E[\cos θ]`, `d = E[\cos 2θ]`: `γ ≤ c ≤ 1` and `2c²−1 ≤ d ≤ 2(1+γ)c − 2γ − 1`. These are necessary and sufficient.*

**Proof.** With `X = \cos θ ∈ [γ,1]`, Jensen gives the lower bound and `(X−γ)(1−X) ≥ 0` the upper; the pair `(E[X], E[X²])` ranges over exactly the order-2 Hausdorff moment body of `[γ,1]`, and every such measure lifts to a symmetric measure on the arc. ∎ (row `A4`)

## Proposition 8.2 (arc-localized residual cone — converse now available)

*Let `g(θ) = \cos θ − γ` and `L_g(r) = \begin{pmatrix} ℓ & \bar h\\ h & ℓ\end{pmatrix}`, `ℓ = \Re r_1 − γA`, `h = \tfrac{A+r_2}{2} − γ r_1`. Then `r` is the moment vector of a positive measure supported in `Ω_u` **if and only if** `T_2(r) ⪰ 0` and `L_g(r) ⪰ 0`.*

**Proof (normalization mapping; audit Q4).** Yang–Xie work on `𝕋 = [0,1]` with `t_j = ∫e^{−i2πjf}dμ`, `T_{mn} = t_{n−m}`, and for `𝓘 = [f_L,f_H]` set `r_0 = −2\cos[π(f_H−f_L)]\,\mathrm{sgn}(f_H−f_L)`, `r_1 = e^{iπ(f_L+f_H)}\,\mathrm{sgn}(f_H−f_L)`, `[T_g]_{mn} = r_1t_{n−m+1} + r_0t_{n−m} + \bar r_1t_{n−m−1}`. Their domain is `𝕋 = [0,1]`, so the wrap-around arc through `0` must be written with endpoints **inside** that domain (audit A5):

`f_L = 1 − \dfrac{u}{2π}`,  `f_H = \dfrac{u}{2π}`,  so `f_L > f_H` and their convention `𝓘 := 𝕋∖(f_H,f_L)` applies, with `\mathrm{sgn}(f_H−f_L) = −1`. Then

`r_0 = −2\cos u = −2γ`,  `r_1 = 1`,  so `g_{YX}(θ) = 2(\cos θ − γ) = 2g(θ)`.

With `t_j = \bar r_j` and `N = 3`, the entries evaluate to `[T_g]_{00} = [T_g]_{11} = 2ℓ` and `[T_g]_{10} = A + r_2 − 2γr_1 = 2h`, i.e. `T_g = 2\,L_g`. PSD-ness is invariant under multiplication by `2`, so Yang–Xie Theorem 2 — `T ⪰ 0` and `T_g ⪰ 0` iff `T` admits a Vandermonde decomposition with all frequencies in `𝓘` — gives both directions. ∎

Row `E11`: the parameter check and the entrywise comparison both agree to `2.4·10⁻¹⁶`. **Gate `F-M63.ARC` is CLOSED.**

## Theorem 8.3 (arc `n=2` exact characterization)

*Assume `0 < t < 1`, `A = 1−t`, `e := td`, and set*

`r_1 := m_1 − tc`,  `ℓ := \Re r_1 − γA`,  `Z := Am_2 − r_1²`, `R := A² − |r_1|²`,  `ρ := \sqrt{R² − (\Im Z)²}`,  `h_0 := \tfrac{A+m_2}{2} − γ r_1`,  `ρ' := \sqrt{ℓ² − (\Im h_0)²}`

*(all functions of `t` and of the symmetric first moment `c`; `r_1` and `ℓ` were used undefined in v1.4 — audit Y3). Then `t` is feasible **iff** some `c ∈ [γ,1]` makes `|r_1| ≤ A`, `ℓ ≥ 0`, `|\Im Z| ≤ R`, `|\Im h_0| ≤ ℓ`, and*

`\bigl[t(2c²−1),\,t(2(1+γ)c−2γ−1)\bigr] ∩ \bigl[\tfrac{\Re Z−ρ}{A},\tfrac{\Re Z+ρ}{A}\bigr] ∩ \bigl[2(\Re h_0−ρ'),\,2(\Re h_0+ρ')\bigr] ≠ ∅`.

*The degenerate cases `t = 0` and `A = 0` are handled as in Theorem 7.2.*

**Proof.** `d` enters the Schur disk and the localizer affinely and really, so each condition cuts a real interval; Proposition 8.1 supplies the third, and Proposition 8.2 makes both directions valid. ∎

Only `c` is discretized; `d` is eliminated exactly. Row `E7`: deviation `6.4·10⁻⁵` against the arc grid LP over nine cases. **Status upgraded from `DERIVED-CONDITIONAL` to `[검증됨]`** by Proposition 8.2.

## 8.4 Active sets on the arc

Symmetric lower/upper endpoints; Schur tangency; localizer tangency; simultaneous double tangency; `|r_1| = A`; `c = γ`; `c = 1`. Completeness is not proved, as in §7.3.

---

# 9\. What restores selection

## 9.1 Definitions

Throughout, `dσ = dθ/2π`, `\hat f(k) = ∫f e^{−ikθ}dσ`, and for a probability density `f` on the circle

`‖f‖_{H^s}^2 := Σ_k (1+k²)^s|\hat f(k)|²`,  `‖f‖_{𝓖_{ρ,α}}^2 := Σ_k e^{2ρ|k|^α}|\hat f(k)|²`.

The two model classes used below are (audit Y2 — these were previously used undefined)

`𝓒_{s,B} := \{f ≥ 0 : ∫f\,dσ = 1,\ ‖f‖_{H^s} ≤ B\}`,  `𝓖_{ρ,α,B} := \{f ≥ 0 : ∫f\,dσ = 1,\ ‖f‖_{𝓖_{ρ,α}} ≤ B\}`,

with `ρ, α, s > 0` and `B > 1`; both are convex and weakly closed, and `B > 1` is forced because `\hat f(0) = 1` already contributes `1`.

Two **distinct** complexities are attached to a class `𝓒`, and they must not be conflated (audit Y1):

`W_{n,𝓒}(m) := \sup\{|𝒜(μ)−𝒜(ν)| : μ,ν ∈ 𝓒 ∩ 𝓕_n(m)\}`,  `Δ_n(𝓒) := \sup_m W_{n,𝓒}(m)`,

* **Fourier-order complexity** `N_ε(𝓒) := \inf\{n : Δ_n(𝓒) ≤ ε\}` — how high a *trigonometric truncation* must go. This is the quantity in Theorems 6.4, 9.3 and 9.5.  
* **Observable-count complexity** `M_ε(𝓒) := \inf\{q : ∃\,Ψ = (Ψ_1,…,Ψ_q) ∈ C(Ω_u;ℝ^q)` such that `\sup_v \mathrm{diam}\,𝒜\bigl(𝓒 ∩ 𝓕_Ψ(v)\bigr) ≤ ε\}` — how many *real observables of any kind* suffice, where `𝓕_Ψ(v) = \{μ : ∫Ψ\,dμ = v\}`. This is the quantity in Corollary 9.7.

Always `M_ε ≤ 2N_ε` when a trigonometric truncation achieves the tolerance, since `Φ_n` has `2n` components; the converse fails, and `M_ε` may be finite while `N_ε = ∞`.

## 9.2 Regime I — unrestricted

`Δ_n = 1` for all finite `n`, hence `N_ε = ∞` for `ε < 1`. Nothing is asserted about `M_ε` here.

## Theorem 9.3 (Sobolev two-sided constants)

*With `Λ_n = (1+(n+1)²)^{−s/2}` and `B > 1`,*

`Δ_n(𝓒_{s,B}) ≤ 2\sqrt{B²−1}\,Λ_n`,  and, provided `\sqrt{2(B²−1)}\,Λ_n ≤ 1`,  `Δ_n(𝓒_{s,B}) ≥ \tfrac{2\sqrt2}{π}\sqrt{B²−1}\,Λ_n`.

*The ratio is exactly `π/\sqrt2 = 2.221441469079…`, independent of `B, s, n`; hence `Δ_n ≍ \sqrt{B²−1}\,n^{−s}` and `N_ε ≍ ε^{−1/s}`.*

**Proof.** Upper: `\hat f(0) = \hat g(0) = 1` and the parallelogram identity give `‖h‖_{H^s} ≤ 2\sqrt{B²−1}`, and `W ≤ ‖h_{odd}‖_1 ≤ ‖h‖_2 ≤ Λ_n‖h‖_{H^s}`. Lower: `f_a(θ) = 1 + a\sin((n+1)θ)` shares all modes `|k| ≤ n` with Haar, has `𝒜 = 2|a|/π`, and the largest admissible `a` is `\sqrt{2(B²−1)}Λ_n`. ∎ (rows `F1`, `F2`)

## Remark 9.4 (residual constant, normalization)

The exact constant is `C_{s,n} := \sup\{‖h‖_1 : h` odd, `\hat h(k) = 0` for `|k| ≤ n`, `‖h‖_{H^s} ≤ 1\}`. Since `‖h‖_1 ≤ ‖h‖_2 ≤ Λ_n‖h‖_{H^s}`, the correct normalization is

`\hat C_{s,n} := C_{s,n}/Λ_n ∈ \bigl[\tfrac{2\sqrt2}{π},\,1\bigr]`,

and v1.1's `[2\sqrt2/π,1]` for `C_{s,n}` itself was missing the factor `Λ_n`. By `‖h‖_1 = \sup_{‖g‖_∞≤1}∫hg` and duality,

`C_{s,n} = \sup_{‖g‖_∞ ≤ 1}\Bigl(\textstyle\sum_{|k|>n}(1+k²)^{−s}\,|\widehat{g_{odd}}(k)|²\Bigr)^{1/2}`,

with the weight exponent `−s`, not `+s`. Evaluating this at `g = \mathrm{sgn}\,\sin((n+1)θ)` gives `\hat C_{s,n} ≥ 0.9071, 0.9010, 0.9234` at `(s,n) = (1,4), (2,6), (0.5,10)` — **strictly above** `2\sqrt2/π = 0.900316`, so the single sine is *not* the extremizer (row `F7`). Determining `\lim_n \hat C_{s,n}` is `D-M63-CONST`.

## Theorem 9.5 (Gevrey law, declared regime)

*Write `E_n := e^{−ρ(n+1)^α}`. For every `n`,*

`Δ_n(𝓖_{ρ,α,B}) ≤ 2\sqrt{B²−1}\,E_n`,  *and, provided `\sqrt{2(B²−1)}\,E_n ≤ 1`, i.e. `n ≥ n_0(ρ,α,B) := \min\{n : \sqrt{2(B²−1)}E_n ≤ 1\}`,*  `Δ_n(𝓖_{ρ,α,B}) ≥ \tfrac{2\sqrt2}{π}\sqrt{B²−1}\,E_n`.

*Hence `Δ_n ≍ \sqrt{B²−1}\,E_n` with the same constant ratio `π/\sqrt2`, and `N_ε ≍ (ρ^{−1}\log(1/ε))^{1/α}`.*

**Warning on the exponent (audit X2).** The two-sided statement holds with `E_n = e^{−ρ(n+1)^α}` and **not** with `e^{−ρn^α}`: the ratio is `\exp\{−ρ[(n+1)^α − n^α]\}`, which tends to `0` when `α > 1`, so the two are not equivalent up to constants. Where the cruder exponent is convenient, only the logarithmic form is claimed:

`\log Δ_n(𝓖_{ρ,α,B}) ∼ −ρ\,n^α`  as `n → ∞`.

`N_ε ≍ (ρ^{−1}\log(1/ε))^{1/α}` is unaffected, since it inverts the logarithm.

**Proof.** Exactly parallel to Theorem 9.3, with `(1+k²)^s` replaced by `e^{2ρ|k|^α}`. *Upper:* if `f,g ∈ 𝓖_{ρ,α,B}` share all modes `|k| ≤ n` then `h = f−g` is supported on `|k| ≥ n+1`, and since `\hat f(0) = \hat g(0) = 1` the parallelogram identity gives `‖h‖²_{𝓖} = 2‖f‖² + 2‖g‖² − ‖f+g‖²_{𝓖} ≤ 4B² − 4`. The weight is increasing in `|k|`, so `‖h‖_2 ≤ E_n‖h‖_{𝓖}`, and `W ≤ ‖h_{odd}‖_1 ≤ ‖h‖_2 ≤ 2\sqrt{B²−1}E_n`. *Lower:* `f_a(θ) = 1 + a\sin((n+1)θ)` shares every mode `|k| ≤ n` with Haar, has `𝒜(f_aσ) = 2|a|/π`, and `‖f_a‖²_{𝓖} = 1 + \tfrac{a²}{2}e^{2ρ(n+1)^α}`, so the largest admissible `a` is `\sqrt{2(B²−1)}E_n`, admissible as a density exactly when that is `≤ 1`. Haar lies in the same fiber with `𝒜 = 0`. ∎

Row `F3` checks that the witness is admissible in the declared regime, reporting `n_0 = 1` and `n_0 = 8` at the tested parameters; it is a check of the hypothesis, not of the proof.

## Theorem 9.6 (finite Gibbs family on a convex domain)

*Let `dμ_b ∝ \exp(E + b·S)dθ` be regular and minimal with **`S ∈ C(Ω_u;ℝ^p)`**, and `K ⊂ ℝ^p` **convex** compact with `λ_{\min}(\mathrm{Cov}_bS) ≥ η > 0` on `K`. Then `∇ψ = E_b[S]`, `∇²ψ = \mathrm{Cov}_b(S) ≻ 0`, `b ↦ E_b[S]` is injective on `K`, and `‖b−b'‖ ≤ η^{-1}‖E_b[S]−E_{b'}[S]‖`.* Convexity is needed so the segment `[b,b']` stays in `K`. (rows `F4`–`F6`, `η ≥ 0.288` on `[−1.2,1.2]³`)

**Corollary 9.7 (which complexity this controls).** Under the hypotheses of Theorem 9.6 — in particular `S ∈ C(Ω_u;ℝ^p)`, so that `Ψ := S` is an admissible observable map — take `𝓒 = \{μ_b : b ∈ K\}`. Injectivity makes `𝓒 ∩ 𝓕_S(v)` a single point for every attainable `v`, so `M_0(𝓒) ≤ p`. This is a statement about the **observable-count** complexity; the Fourier-order complexity is settled separately by Theorem 9.8.

## Theorem 9.8 (finite Fourier saturation of a Gibbs family)

*Let `dμ_b ∝ \exp(E + b·S)dθ` be regular and minimal with `S ∈ C(Ω_u;ℝ^p)`, let `K` be convex compact with `λ_{\min}(\mathrm{Cov}_bS) ≥ η > 0` on `K`, and put `L := ‖S‖_{∞,2} = \sup_θ|S(θ)|`. Suppose `T_N ∈ (\mathrm{span}\,Φ_N ⊕ ℝ)^p` satisfies*

`δ_N := ‖T_N − S‖_{∞,2} < \dfrac{η}{2L}`.

*Then `F_N(b) := E_b[T_N]` is differentiable with `DF_N(b) = \mathrm{Cov}_b(T_N, S)`, and for every `x ∈ ℝ^p`*

`x^{\!\top}DF_N(b)\,x ≥ (η − 2Lδ_N)\,‖x‖^2 > 0`,

*so `F_N` is strongly monotone and injective on `K`. Since `E_b[T_N]` is a linear function of the trigonometric moments of order `≤ N`, those moments determine `b`, hence `μ_b`. Therefore*

`Δ_N(𝓒) = 0`  and  `N_0(𝓒) ≤ N < ∞`.

*By the Stone–Weierstrass theorem — equivalently Weierstrass's second approximation theorem, which makes trigonometric polynomials uniformly dense in `C(𝕋)` — such an `N` exists for every continuous `S`, so `N_0(𝓒)` is **always finite**.*

**Proof.** Differentiating `E_b[T_{N,i}] = ∫T_{N,i}\,dμ_b` in `b_j` gives `∂_j E_b[T_{N,i}] = \mathrm{Cov}_b(T_{N,i}, S_j)`, which is the stated Jacobian. Write `Δ := T_N − S`. Then

`x^{\!\top}DF_N x = \mathrm{Cov}_b(x·T_N,\; x·S) = \mathrm{Cov}_b(x·S,\;x·S) + \mathrm{Cov}_b(x·Δ,\;x·S)`.

The first term is `≥ η‖x‖²`. For the second, `|\mathrm{Cov}_b(U,V)| ≤ 2‖U‖_∞‖V‖_∞` with `‖x·Δ‖_∞ ≤ δ_N‖x‖` and `‖x·S‖_∞ ≤ L‖x‖`, giving `|\mathrm{Cov}_b(x·Δ,x·S)| ≤ 2Lδ_N‖x‖²`. Convexity of `K` lets one integrate along the segment `[b,b']`, so `(b−b')·(F_N(b)−F_N(b')) ≥ (η−2Lδ_N)‖b−b'‖²`, whence injectivity. ∎

**Withdrawal of Corollary 9.6′ of v1.5 (audit X1).** v1.5 asserted that with non-trigonometric statistics `N_ε` "need not be finite at all" and `Δ_n(𝓒) > 0` could hold for every `n`. Theorem 9.8 shows the opposite under the very hypotheses already assumed. The exact span condition `S_j ∈ \mathrm{span}\,Φ_{n_0}` is a convenient **sufficient** condition giving the explicit bound `N_0 ≤ n_0`; it is not necessary. Row `F8` exhibits a deliberately non-band-limited `S` — three Poisson-kernel type statistics with geometric Fourier decay — for which `L = 2.3203`; the Jacobian identity holds to `3.4·10^{-12}` and the sampled monotonicity modulus `0.1275` exceeds `\hatη − 2Lδ_N`. **Two scope limits are declared (audit W2, W3).** First, `\hatη = 0.098036` is the minimum of `λ_{\min}(\mathrm{Cov}_bS)` over a fixed set of six sampled `b`; it is a **sampled diagnostic**, not a certified uniform bound over the box, and certifying `η` globally by interval arithmetic is an open item. Second, the search over `N` is now contiguous on `1..12`, and the first `N` with `2Lδ_N < \hatη` is **`N = 7`**; v1.6 reported `N = 8` because its ladder skipped `5` and `7`. Neither limit touches Theorem 9.8, whose hypotheses are `η` and `δ_N`, not their numerical estimation.

## 9.9 Phase diagram

| Class | `Δ_n` | `N_ε` (Fourier order) | `M_ε` (observable count) |
| :---- | :---- | :---- | :---- |
| unrestricted `𝒫(Ω_u)` | `1`, every finite `n` | `∞` for `ε<1` | not asserted |
| Sobolev `𝓒_{s,B}` | `≍ \sqrt{B²−1}\,n^{−s}`, ratio `π/\sqrt2` | `≍ ε^{−1/s}` | `≤ 2N_ε` |
| Gevrey `𝓖_{ρ,α,B}`, `n ≥ n_0` | `≍ \sqrt{B²−1}\,e^{−ρ(n+1)^α}`; only `\log Δ_n ∼ −ρn^α` in the cruder exponent | `≍ (ρ^{−1}\log(1/ε))^{1/α}` | `≤ 2N_ε` |
| regular minimal `p`\-Gibbs on convex `K`, `S` continuous | `0` on the fiber of `S`; `Δ_N = 0` for `N` as in Thm 9.8 | `N_0 ≤ N < ∞` **always** (Thm 9.8); `≤ n_0` if `S_j ∈ \mathrm{span}\,Φ_{n_0}` | `M_0 ≤ p` |

---

# 10\. Z-Spin: conditional full-circle diagnostic

`λ = −0.5664173302854644027 + 0.6884532271077021305i`, `|λ| = 0.891513565776047 < 1`, so `T_1(λ) ≻ 0` (row `Z1`). Theorem 6.1 gives `A_1⁻(λ;𝕋) = 0.763362818245963536…`, reproducing the M62 constant `A_*` to 18 digits — a cross-route confirmation, not a new number. Theorem 5.3 gives `A_1⁺ = 1`. Hence `𝓘_1(λ;𝕋) = [0.7633628182459635,\,1]`, `W_1 = 0.2366371817540365`.

`λ` is a strong asymmetry **witness** and not a state **selector**. Scope: full circle only; the arc version needs the M62 effective-arc convention (gate `F-M63.11`). `D-M61-IOTA` remains OPEN.

---

# 11\. Imported results

| Import | Statement | Source | Role |
| :---- | :---- | :---- | :---- |
| I-1 | `ri(\overline C) = ri C` | Rockafellar 1970 | Thm 4.1 |
| I-2 | Carathéodory | classical | Thm 4.1 |
| I-3 | `𝓕_n ≠ ∅ ⟺ T_n ⪰ 0` | Carathéodory–Toeplitz | §2, §6 |
| I-4 | OPUC zeros in the open disk | Szegő; Simon *OPUC I* | Thm 5.3 |
| I-5 | POPUC: `n+1` simple zeros on `𝕋`; Szegő quadrature positive, exact on `Λ_{−n,n}` | Jones–Njåstad–Thron 1989 | Thm 5.3 |
| I-6 | POPUC as characteristic polynomials of unitary upper Hessenberg matrices; rank-one picture | Gragg 1993; Simon *JMAA* 329 (2007) | Lem 5.2(a) |
| I-7 | Gauss quadrature of a Jacobi matrix: positive weights, exactness, simple spectrum, nonvanishing end components | classical | Lem 5.2(b), Thm 5.5 |
| I-8 | Interior of the order-`2n` Hausdorff moment cone on `[a,b]` \= Hankel and localizing matrix both `≻ 0` | classical | Prop 5.6 |
| I-9 | Rank-deficient PSD Toeplitz: unique Vandermonde decomposition | Carathéodory–Fejér | Thm 6.2 |
| I-10 | T-system boundary uniqueness; index bookkeeping | Karlin–Studden 1966; Dette–Schorning 2013 | Thm 5.5, 6.2 |
| I-11 | **Yang–Xie Theorem 2**: `T ⪰ 0` and `T_g ⪰ 0` iff `T` has a Vandermonde decomposition with all frequencies in `𝓘`; unique if either is rank-deficient | Yang–Xie, *Signal Processing* **142** (2018) 157–167 | **Prop 8.2, now with the normalization verified** |
| I-12 | Fejér–Riesz spectral factorization of nonnegative trigonometric polynomials | classical | row `E12` |
| I-13 | Peeling identity; strong duality; Minkowski interpolation (corrected scope) | `ZS-M62 v1.4.2` Thm 2, 3, 6 | Thm 7.1, 7.5 |
| I-14 | `n=1` arc closed form; gauge body `Y_2(π)`; multiplier price theorem, `A_*` | `ZS-M62 v1.4.2` Thm 8, 16, 17 | Thm 6.1, 7.4, §10 |
| I-15 | Regular minimal exponential families: `∇ψ = E[S]`, `∇²ψ = Cov(S)` | classical | Thm 9.6 |
| I-16 | Stone–Weierstrass / Weierstrass second approximation theorem: trigonometric polynomials are uniformly dense in `C(𝕋)` | classical | Thm 9.8 |

**Upstream warning.** The `ZS-M62` audit (`H-0089`) accepted statement errors in its Theorems 3 and 6; all uses of I-13 are to the corrected `v1.4.2` statements.

---

# 12\. Verification

`zs_m63_verify_v1_6_2.py`, one command, fail-closed.

ARTIFACT\_MANIFEST

paper\_code/version : ZS-M63 v1.6.2

main\_script        : zs\_m63\_verify\_v1\_6\_2.py

dependencies       : EMBEDDED in the script; print with \--print-requirements

                     numpy==2.4.4, scipy==1.17.1, sympy==1.14.0, CPython 3.13

seed               : 20260821 (fixed)   LP grid N \= 3000   TOL\_LP \= 5e-4

run                : python3 zs\_m63\_verify\_v1\_6\_2.py

                     python3 zs\_m63\_verify\_v1\_6\_2.py \--quick

                     python3 zs\_m63\_verify\_v1\_6\_2.py \--no-sympy

                     python3 zs\_m63\_verify\_v1\_6\_2.py \--no-manuscript   (records a

                       declared skip of S3/S5 as a FAILURE, not a pass)

                     python3 zs\_m63\_verify\_v1\_6\_2.py \--manuscript ZS-M63\_v1\_6\_2.md

                     python3 zs\_m63\_verify\_v1\_6\_2.py \--print-requirements

expected rows      : EXPECTED\_ROWS \= 68, fail-closed

expected census    : C=7 V=30 W=11 X=2 R=3 G=8 D=4 T=3, P=0, fail-closed

observed           : rows \= 68, FAIL \= 0, exit 0

evidence rows      : C+V+W \= 48   (X is NOT evidence; R rows are controls)

artifact profile   : output names carry the profile (…\_v1\_6\_2.quick.… / …\_v1\_6\_2.no\_sympy.… vs …\_v1\_6\_2.…)

                     and the JSON records it, so a \--quick run cannot overwrite a

                     FULL deliverable; guard S7 checks the certificate count for

                     the profile and against the manuscript

fail-closed        : the manuscript is auto-discovered; if absent, S3 and S5

                     FAIL.  \--no-manuscript is an explicit opt-out recorded as

                     a failure, so a default run cannot silently pass them.

degraded replay    : \--no-sympy emits all 68 rows with exactly 8 failures

                     (D3, A1, A2, A3, C11, E4, E8, E12) and no abort; the

                     structural row map is byte-identical in both modes

self-reference     : S5 audits the manuscript and S6 audits the script for

                     stale filenames and declared-vs-actual count disagreement

row registry       : ROW\_SPEC (frozen id \-\> class, name); row() ignores call-site

                     class/name; row S4 guards emitted ids against the registry

companion outputs  : zs\_m63\_rowmap\_v1\_6\_2.md        (generated FROM THE REGISTRY)

                     zs\_m63\_observations\_v1\_6\_2.md  (observed values, per run)

                     zs\_m63\_chambers\_v1\_6\_2.txt     (explicit chamber polynomials)

                     zs\_m63\_certificate\_v1\_6\_2.txt  (exact rational Gram matrices)

determinism        : JSON byte-identical on re-run (verified)

**Class discipline.** `C` is **symbolic or exact-rational only** — in this suite that is exactly the **seven** rows `A1, A2, A3, C11, E4, E8, E12`, matching the declared `C=7`. Every floating-point or random check is `V` or `W`; `B7, C8, F1, Z1` were re-tagged from `C` accordingly. Heuristic counts (`B4`, `C6`) are `X` and are **not** evidence. Regression controls (`E2`, `E5`, `Z2`) are `R` and are **not** evidence. `P = 0` by construction.

**Environment invariance (audit A2).** v1.2 claimed invariance but did not achieve it: row names changed when sympy was absent, so the generated table changed and `S3` failed. In v1.3 the table below is generated **from the frozen `ROW_SPEC` registry**, not from the run, so it is identical on every machine regardless of which optional dependency is present. Observed values go to `zs_m63_observations_v1_6_2.md`. Row `S3` fails the run if the manuscript does not contain this table byte-for-byte; row `S4` fails if the emitted rows do not match the registry in content and order.

| row | class | check |
| :---- | :---- | :---- |
| `D1` | `D` | convention lock d\_TV \= 1/2//.//\_var in \[0,1\] |
| `D2` | `D` | class P \= 0 by construction: no row proves a theorem |
| `D3` | `D` | dependency declaration (R6): sympy required for the C rows |
| `T1` | `T` | TV control on an explicitly known pair |
| `T2` | `T` | premise control: reflection-symmetric support has gap 0 |
| `T3` | `T` | negative control: closed form disagrees with a perturbed datum |
| `A1` | `C` | det T\_2 \= 1-2/m1/^2-/m2/^2+2Re(m1^2 conj m2) |
| `A2` | `C` | det S\_2 \= t^3(1-d)(1+d-2c^2) |
| `A3` | `C` | Schur identity A det R\_2 \= (A^2-/r1/^2)^2-/A r2-r1^2/^2 |
| `A4` | `V` | arc symmetric strip 2c^2-1 \<= d \<= 2(1+g)c-2g-1 (50 samples) |
| `A5` | `V` | T\_2(m) PSD for 200 random atomic measures |
| `A6` | `G` | rejection guard: PSD implies det T\_2 \>= 0 |
| `B1` | `W` | OPUC zeros lie in the open unit disk (counterexample search) |
| `B2` | `W` | node sets of B\_tau, B\_tau' are disjoint for tau \!= tau' |
| `B3` | `W` | circle: reflection-free (n+1)-atom representation exists (n=1..6) |
| `B4` | `X` | bad-set cardinality (heuristic) vs the corrected bound C(N,2)+2N \= N(N+3)/2, N=n+1 (audit S1: self-pair j=k separated) |
| `B5` | `W` | circle: ALL nodes co-monotone; SUM of shifts \= 2pi; the shifts are NOT individually 2pi/(n+1) (v1.1 audit Q1) |
| `B6` | `V` | circle derivative identity d theta\_j/d phi \= /v\_j(last)/^2 \> 0 |
| `B7` | `V` | unitarity identity sum\_j /v\_j(last)/^2 \= 1 (total shift \= 2pi) |
| `B8` | `V` | atom lower bound: r \<= n atoms forces rank T\_n \<= n |
| `C1` | `V` | tan-half transport: arc trig moments \<-\> Hausdorff moments on \[-T,T\] |
| `C2` | `V` | arc: sigma-family is exact to degree 2n with positive weights, n+1 atoms |
| `C3` | `V` | arc derivative identity d lambda\_j/d sigma \= /v\_j(last)/^2 (audit repair R1) |
| `C4` | `W` | arc: ALL n+1 nodes strictly increasing in sigma (common direction) |
| `C5` | `W` | arc: admissible sigma set is a SINGLE interval |
| `C6` | `X` | arc collision count (heuristic) vs bound N(N+1)/2, N=n+1 |
| `C7` | `W` | arc: a reflection-free rule exists (max reflection gap \> 0\) |
| `C8` | `V` | annihilator lemma: q \<= 2n+1 distinct nodes give full column rank |
| `E1` | `V` | Thm 6.1 n=1 full-circle closed form vs grid LP |
| `E1b` | `V` | Thm 6.1 edge case a=0, i.e. m1 \= \+-1: A\_1^- \= 0 (audit repair R7) |
| `E2` | `R` | regression: A\_1^-(lambda) reproduces the M62 constant A\* |
| `E3` | `V` | Thm 7.4 n=2 odd-gauge closed form vs odd-data LP |
| `E4` | `C` | Thm 7.4 exact: two rational identities certify the radical solution (audit repair R5, no point substitution) |
| `E5` | `R` | regression against M62 Thm 16 body {/w/\<=1, 2v^2-1 \<= sqrt(1-w^2)} |
| `E6` | `V` | Thm 7.2 n=2 full-circle Schur reduction vs grid LP |
| `E7` | `V` | Thm 8.3 arc n=2 system (strip+Schur+localizer, exact d-elimination) vs arc LP |
| `E8` | `C` | chamber polynomials incl. Chamber I quintic (audit repair R2) |
| `E9` | `W` | n=2 numerical dual candidate on a 40001-point grid (not a certificate) |
| `E10` | `V` | Thm 7.5 dual formula vs primal LP |
| `F1` | `V` | Sobolev upper/lower constant ratio \= pi/sqrt(2), independent of (B,s,n) |
| `F2` | `V` | Sobolev witness: positivity, //f\_a//\_Hs \= B, A(f\_a) \= 2a/pi |
| `F3` | `V` | Thm 9.5 Gevrey witness admissible in the declared large-n regime |
| `F4` | `V` | Thm 9.6 grad psi \= E\_b\[S\] (numerical gradient) |
| `F5` | `W` | Thm 9.6 Hess psi \= Cov\_b(S) \> 0 on the declared convex box \[-1.2,1.2\]^3 (repair R7) |
| `F6` | `V` | Thm 9.6 strong monotonicity on the box (segment stays inside) |
| `G1` | `V` | Thm 6.3 fragility: boundary jump of W\_n equals 1 \- A(mu\_m) |
| `G2` | `W` | Thm 6.4 minimax Delta\_n \= 1: Haar fiber holds both A=0 and A=1 |
| `G3` | `W` | Thm 4.1 dense selector: R-free grid represents interior data, support \<= 2n+1 |
| `G4` | `V` | Prop 3.3 monotonicity A\_n^- \<= A\_{n+1}^-, hence W\_{n+1} \<= W\_n |
| `Z1` | `V` | T\_1(lambda) positive definite, /lambda/ \< 1 |
| `Z2` | `R` | full-circle diagnostic interval I\_1(lambda) \= \[A\*, 1\] |
| `Z3` | `D` | scope: full-circle diagnostic only; arc version needs the M62 effective-arc convention; D-M61-IOTA remains OPEN |
| `C9` | `V` | Prop 5.6 arc admissible set Sigma \= \[sigma\_-, sigma\_+\] by Schur complement, vs direct scan (audit Q2) |
| `C10` | `V` | Prop 5.6 identity sigma\_+-sigma\_- \= 2T(1-b\_n^2\<e,(T^2I-J\_n^2)^-1 e\>) \= 2T detL/detM \> 0 iff L \> 0 (audit Q2) |
| `C11` | `C` | Prop 5.7: p\_{n+1}(x;sigma) is affine in sigma; deg\_sigma of the collision eliminant is at most 2n+1 with leading coefficient \-2 Res(p\_n, p\_n o (-id)); exact degree 2n+1 iff that resultant is nonzero, with a symmetric negative control where it vanishes |
| `E11` | `V` | F-M63.ARC closure: Yang-Xie Thm 2 localiser with f\_L \= 1-u/2pi, f\_H \= u/2pi in T=\[0,1\] equals 2 x our L\_g coefficient by coefficient |
| `E12` | `C` | EXACT rational Gram (SOS) certificate: 1-P and \-(P+P(-.)) are a(th)^\* G a(th) with G rational, Hermitian, coefficient identity exact and all leading principal minors exactly positive \-- no grid |
| `E12b` | `V` | numerical approximate Fejer-Riesz factorisation (diagnostic only; superseded as a certificate by E12) |
| `E13` | `V` | declared degenerate points of Thm 7.2 / 8.3: t=0 and A=0 handled outside the 1/A, 1/t formulas (audit Q8) |
| `F7` | `V` | Remark 9.4 corrected normalisation hatC \= C/Lambda\_n in \[2sqrt2/pi, 1\]; the square wave beats the single sine strictly (audit Q8) |
| `F8` | `V` | Thm 9.8 Gibbs finite-Fourier saturation with NON-trigonometric statistics, SAMPLED diagnostic: eta\_hat is the minimum of lambda\_min(Cov\_b S) over a FIXED FINITE set of b and is not a certified uniform bound over the box; checks DF\_N(b) \= Cov\_b(T\_N,S), the quadratic bound and strong monotonicity at those b, and reports the first N in the contiguous tested range 1..12 with 2 L delta\_N \< eta\_hat |

**What verification does not do.** No row proves any theorem; class `P` is `0`. `W` rows are counterexample searches; `V` rows validate implementations against an independent route at a declared tolerance; `X` rows are heuristics labelled as such in the registry text. Row `E12` is the one row whose *conclusion* is exact — it certifies a shifted rational dual point by exact rational arithmetic — but it certifies feasibility of that point, not optimality of the LP (NC-7). Row `E12b` is explicitly a numerical diagnostic and is not a certificate.

---

# 13\. Strongest objections

**O1 (novelty).** Theorem 4.1 uses relative-interior calculus and Carathéodory; the quadrature families are classical. Own: Lemmas 5.1–5.2, Propositions 5.6–5.7, the reflection argument, optimality, and the synthesis. `D-M63-PRIOR` is `0 %`. **Handled by scope.**

**O2 (the interior theorem flattens the diagram).** With `A_n⁺ ≡ 1` on the relative interior, `W_n = 1 − A_n⁻` adds nothing beyond the lower envelope. The weight sits in §7–§9. **Answered by re-weighting.**

**O3 (§7.3 is not an atlas, and no longer claims to be a theorem).** Accepted three times from audit. The polynomials are printed and whole-circle exact dual-feasibility certificates exist at three specified data points, but active-set completeness and extremizer recovery are open, so §7.3 is now a **candidate** reduction rather than a classification. **NC-6, `D-M63-ATLAS`.**

**O4 (fragility needs continuity).** In the theorem line; verified only at `n=1`. **`D-M63-CONT`.**

**O5 (review independence).** **Eight** rounds at `ι ≈ 0.2`, same AI lineage and continuous context. These are **low-independence self-audits**, not independent peer review, and the paper does not describe them as such anywhere. No qualified human proof review. Lemma 5.2, Propositions 5.6–5.7, Proposition 7.6 and the Yang–Xie mapping are load-bearing and were produced *and* checked inside that lineage. Each round has found real errors in the previous one — a false monotonicity inference (v1.0), a false per-node shift (v1.1), a certificate that was not a certificate and an invariance claim that was not invariant (v1.2), an over-general degree claim refuted by a symmetric datum and a dependency path that aborted (v1.3), a measurement-type error in the selection-complexity table and a fail-closed guard that still passed on an absent manuscript (v1.4), a false corollary about non-trigonometric statistics, an asymptotic that fails for `α > 1`, and a "theorem" that declared its own hypothesis unproved (v1.5) — which is evidence that the process works and equally that it has not yet converged. **This is the main reason the release label is not restored.**

**O6 (external value is concentrated).** The paper's external value now rests on two things: whether the reflection-free `n+1`\-atom theorem is absent from the literature, and whether §7.3 or §8.3 can be closed. §8.3 is closed in this version; §7.3 is not. **Partially answered.**

**O7 (physics).** Nothing derives a Z-Spin boundary state. **NC-1, NC-2.**

---

# 14\. Gates, debts, open problems

## Gates

| Gate | Fires if | Status |
| :---- | :---- | :---- |
| `F-M63.1` | an interior `T_n ≻ 0` datum has every representing measure overlapping its reflection | open |
| `F-M63.2` | an interior arc datum admits no reflection-free `(n+1)`\-atom rule | open |
| `F-M63.2′` | the last eigenvector component vanishes for some admissible parameter | open |
| `F-M63.2″` | `σ_- ≥ σ_+` for some `m ∈ ri 𝓜_{n,u}` | open — would contradict Prop 5.6 |
| `F-M63.3` | a source proves `A_n⁺ = 1` at equal or greater generality | open |
| `F-M63.4` | a truncated-moment diameter theorem in TV subsumes §4–§6 | open |
| `F-M63.ARC` | the degree-one localizer is insufficient at `n = 2` | **CLOSED** (Prop 8.2, row `E11`) |
| `F-M63.CONT` | `A_n⁻` is discontinuous at `∂𝓜_n` | open |
| `F-M63.ATLAS` | the active-set list of §7.3 / §8.4 is incomplete | open |
| `F-M63.MET` | a Wasserstein bound is used as a TV bound | open |
| `F-M63.FIT` | a model class is chosen after inspecting `λ` | open |
| `F-M63.11` | a full-circle result is applied to the M62 effective arc without convention matching | open |
| `F-M63.VER` | PASS counts are stated as theorem counts, or `R`/`X` rows are counted as evidence | open |
| `F-M63.SYNC` | the manuscript structural row map diverges from the registry-generated table | open — rows `S3`, `S4` |
| `F-M63.CERT` | a Gram matrix in `zs_m63_certificate_v1_6_2.txt` fails the exact coefficient identity or has a nonpositive leading minor | open — row `E12` |
| `F-M63.SELF` | the manuscript or the script references a superseded artifact filename, or a declared count disagrees with the constant used | open — rows `S5`, `S6` |
| `F-M63.DEP` | the suite aborts, rather than degrading row-wise, when an optional dependency is missing | open — `--no-sympy` replay |
| `F-M63.CLOSED` | a guard reports PASS for a check it did not actually perform (absent manuscript, skipped artifact) | open — rows `S3`, `S5` fail closed |
| `F-M63.TYPE` | a complexity stated in one unit (Fourier order) is compared with a quantity in another (observable count, parameter count) | open — §9.1, Corollary 9.7 |
| `F-M63.PROFILE` | a shipped artifact was produced by a different run or profile than the shipped ledger | open — row `S7`, profile-suffixed outputs |
| `F-M63.ASYMP` | a two-sided `≍` is asserted between expressions whose ratio is unbounded in the stated regime | open — Theorem 9.5 warning |
| `F-M63.SAMPLE` | a quantity estimated on a finite sample is reported as a uniform bound over a set | open — row `F8` is declared sampled |
| `F-M63.INDEP` | an internal self-audit is described as an independent audit | open — §13 O5, companion document |
| `F-M63.LABEL` | a theorem/proposition label used in the verification registry does not exist as a heading in the manuscript | open — row `S5` cross-check |

## Debts

`D-M63-PRIOR` (`0 %`) · `D-M63-ATLAS` (active-set completeness, extremizers, chamber-wise certificates) · `D-M63-CONT` (continuity of `A_n⁻`) · `D-M63-CONST` (`\lim_n \hat C_{s,n}`) · `D-M63-BAD` (exact collision count; Prop 5.7 bounds it by `2n+1` when `𝓔 ≢ 0`) · `D-M63-QUANT` (turn Remark 5.9, margin `L/(4n+4)`, into a genuine reflection-gap lower bound) · `D-M63-REAUDIT` (the first review **outside** this AI lineage — the v1.6 audit recommends freezing here and going to external mathematical review and prior-art search rather than an eighth internal round) · `D-M63-ETA` (certify `η = \min_K λ_{\min}(\mathrm{Cov}_bS)` globally by interval arithmetic, rather than sampling it as row `F8` does).

## Open problems

1. Exact collision count: is it `n+2` in general position, against the proved bound `2n+1`? Equivalently, how many roots of `𝓔` are real and lie in `Σ`, and how does the count change on the degenerate stratum `\mathrm{Res}(p_n,p_n∘(−\mathrm{id})) = 0` where the degree drops?  
2. `\lim_{n}\hat C_{s,n}`; the square wave beats the sine but leaves `H^s` for `s ≥ 1/2`, so the extremizer is intermediate. 2b. Is `M_ε(𝓒_{s,B}) ≍ N_ε(𝓒_{s,B})`, or can non-trigonometric observables beat the Fourier order on a Sobolev ball? 2c. In Theorem 9.8, how does the saturation order `N_0` scale with `η`, `L` and the smoothness of `S`? The proof gives only `2Lδ_N < η`; a sharp exponent is open. 2d. Certify `η` over a convex box by interval arithmetic, so that the `F8` diagnostic becomes a proof-grade instance rather than a sampled one (`D-M63-ETA`).  
3. Continuity of `A_n⁻` on the closed moment body.  
4. Prove the `n = 2` active-set list exhaustive; handle double boundaries and repeated roots; recover extremizers by rank factorization; attach an exact Gram certificate of the kind of Proposition 7.6 chamber by chamber rather than pointwise.  
5. Push Proposition 5.6 to a *quantitative* statement: how does `σ_+ − σ_- = 2T\det L/\det(T²I−J_n²)` degenerate as `m → ∂𝓜_{n,u}`, and — beyond the pigeonhole margin of Remark 5.9 — does it control the reflection gap through a lower bound on `|v_j(N)|²`?  
6. Generalize `𝒜` from `ℤ₂` to a compact group.  
7. Model mismatch: bound `\mathrm{diam}(𝓕_n(m) ∩ 𝓝_δ(𝓖_p))`.  
8. Can `ZS-S14` derive an independent `m_2` without using `λ`?  
9. Can `D-M61-IOTA` be constructed or refuted independently?  
10. `D-M63-PRIOR` axes: "reflection-free representing measure with prescribed moments", "involution-asymmetry range over moment fibers", "symmetry-constrained Carathéodory number", "maximal TV to a reflected measure under moment constraints", "co-monotone canonical quadrature families and support avoidance", "Schur-complement characterization of the free-moment interval".

---

# 15\. References

1. R. T. Rockafellar, *Convex Analysis*, Princeton University Press, 1970\.  
2. S. Karlin and W. J. Studden, *Tchebycheff Systems: With Applications in Analysis and Statistics*, Wiley, 1966\.  
3. M. G. Kreĭn and A. A. Nudel'man, *The Markov Moment Problem and Extremal Problems*, AMS Transl. Math. Monogr. **50**, 1977\.  
4. W. B. Jones, O. Njåstad and W. J. Thron, "Moment theory, orthogonal polynomials, quadrature, and continued fractions associated with the unit circle," *Bull. London Math. Soc.* **21** (1989), 113–152.  
5. B. Simon, *Orthogonal Polynomials on the Unit Circle*, Parts I–II, AMS Colloquium Publications **54**, 2005\.  
6. B. Simon, "Rank one perturbations and the zeros of paraorthogonal polynomials on the unit circle," *J. Math. Anal. Appl.* **329** (2007), 376–382; arXiv:math/0606037.  
7. W. B. Gragg, "Positive definite Toeplitz matrices, the Hessenberg process for isometric operators, and the Gauss quadrature on the unit circle," *J. Comput. Appl. Math.* **46** (1993), 183–198.  
8. K. Castillo, "On monotonicity of zeros of paraorthogonal polynomials on the unit circle," arXiv:1706.05709; K. Castillo and J. Petronilho, arXiv:1706.05706.  
9. H. Dette and K. Schorning, "Complete classes of designs for nonlinear regression models and principal representations of moment spaces," *Ann. Statist.* **41** (2013), 1260–1267.  
10. Z. Yang and L. Xie, "Frequency-selective Vandermonde decomposition of Toeplitz matrices with applications," *Signal Processing* **142** (2018), 157–167. DOI 10.1016/j.sigpro.2017.07.024; arXiv:1605.02431. **Theorem 2 read at statement and proof level; normalization mapped in Prop 8.2.**  
11. B. Dumitrescu, *Positive Trigonometric Polynomials and Signal Processing Applications*, Springer, 2007\.  
12. J.-P. Gabardo, "Truncated trigonometric moment problems and determinate measures," *J. Math. Anal. Appl.* **239** (1999), 349–370. `SOURCE-READ REQUIRED`.  
13. L. Tardella, "A note on estimating the diameter of a truncated moment class," *Statist. Probab. Lett.* **54** (2001), 115–124. `SOURCE-READ REQUIRED — closest novelty collision`.  
14. E. J. Candès and C. Fernandez-Granda, "Towards a mathematical theory of super-resolution," *Comm. Pure Appl. Math.* **67** (2014), 906–956.  
15. P. Catala, M. Hockmann, S. Kunis and M. Wageringel, *Constr. Approx.* **60** (2024), 405–442. (Wasserstein-1; metric firewall.)  
16. D. Henrion, M. Kružík and S. Weis, "Extreme points and faces in the moment problem," arXiv:2606.21391. `SOURCE-READ REQUIRED`.  
17. `ZS-M62 v1.4.2`, *Oriented-Mass Geometry of Reflection Asymmetry* (corpus canonical).  
18. `ZS-M61 v1.6` (corpus canonical).

---

**END OF ZS-M63 v1.6.2**  
