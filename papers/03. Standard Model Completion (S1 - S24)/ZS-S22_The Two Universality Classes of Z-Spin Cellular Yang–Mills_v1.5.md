# **ZS-S22**

# **The Two Universality Classes of Z-Spin Cellular Yang–Mills: Goldberg–Coxeter Refinement, the Defect-Support Theorem, and the Re-attribution of the Orbit-Blind Postulate**

**Author:** Kenny Kang **Affiliation:** Z-Spin Cosmology Collaboration **Date:** July 2026 **Theme / Paper Code:** Standard Model — **ZS-S22** **Version:** v1.5 — TERMINAL. Supersedes v1.4, v1.3, v1.2, v1.1 and v1.0 (July 2026\) **Locked inputs (never re-fitted):** **A** \= 35/437, **Q** \= 11, dim(**Z**) \= 2, λ₁ \= 1.2428416164, λ\_h \= 7.5210904061 **Immediate predecessor:** ZS-S21 v1.2 TERMINAL **Does not supersede:** ZS-S21. S21 remains terminal on the finite-K\_TI Hodge-measure selection question. **Companion:** zs\_s22\_verify\_v1\_5.py — one self-contained file. No data assets, no imported mesh files, no auxiliary scripts.

---

**Verification: 139 verification-ledger entries PASS | 125 executable checks (C) \+ 13 computed diagnostics (X) \+ 1 proxy (P) | 39 declarative (D) | 0 FAIL | Zero Free Parameters | A \= 35/437, Q \= 11, dim Z \= 2, λ₁, λ\_h all LOCKED and none re-fitted | SHA256(companion) \= 860a1d7bb2350cf79233c53e5635858a829cdea24388f33c251c242f7c716141**

*Ledger wording note (v1.5).* **"139 PASS" counts ledger entries, not mathematical theorems.** Recounted for v1.5, this paper contains **six PROVEN results** (Lemma S22.0, Theorems S22.1, S22.2, S22.3(a), S22.8, Lemma S22.10a), **one PROVEN-CONDITIONAL theorem** (S22.10, on (C1) ∧ (Z-A2) ∧ (C3)), **one PROVEN-CONDITIONAL corollary** (S22.2a), **two DERIVED-CONDITIONAL theorems** (S22.4a, and S22.9's sufficiency direction, which inherits S22.4a's conditionality) and **one numerically-supported conjecture** (S22.4c); the remaining entries are executable assertions, convergence diagnostics, one proxy and declarative registry statements. The breakdown is carried in the banner precisely so that the count cannot be mistaken for a theorem count.

---

# §0. Scope, Abstract, Registers

## §0.0 Scope Declaration

**Read this before the abstract.** ZS-S22 studies the behaviour of the ZS-S21 *cellular instrument* under a canonical refinement of its carrier. It is a theorem-plus-computation paper about a **quadratic Hodge operator on a two-dimensional cell complex**. It is not a continuum Yang–Mills paper.

Specifically, and stated once so that no later paper can borrow the result beyond its scope, ZS-S22 does **not** establish: the existence of a continuum Yang–Mills measure on K\_n × a\_tℤ; an SU(3) mass gap; any 3+1-dimensional Clay-form statement; the exact Wilson quartic; the non-Abelian Gauss–Coulomb–Faddeev–Popov reduction; or the continuum scheme-matching programme. Every O(g²) statement of ZS-S17 to ZS-S20 remains DERIVED-PERT-COND at λ\_t ≈ 5.54 and is not improved here.

What ZS-S22 does supply is narrower and, we argue, more consequential than the question it was seeded to answer: an exact locality theorem for orbit-weight perturbations, and the identification of **two** — not one — inequivalent refinement limits of the ZS-S21 instrument, together with the determination of which of the three ZS-S21 hypotheses actually selects between them.

## §0.1 Abstract

ZS-S21 proved that the cellular transfer matrix fixes the *form* of the Hodge measure but not its two orbit weights σ \= m₅₆/m₆₆ and ρ \= β₅/β₆, and closed the sub-bridge at DERIVED-CONDITIONAL on (H-W) ∧ (Z-A0) ∧ (Z-A1). On a single truncated-icosahedron carrier that is the honest terminus. This paper changes the question from selection to universality by embedding K\_TI as the first member of the icosahedral Goldberg–Coxeter family **K\_n \= GP(n,n)**, n ≥ 1, in which the 12 pentagonal curvature defects and their 60 adjacent edges remain finite while the hexagonal bulk grows as 30n².

**Lemma S22.0** reduces the entire computation exactly: for a 2-sphere cell complex, B₂B₂ᵀ is the graph Laplacian of the dual 1-skeleton, so Δ\_n(σ,ρ) is a weighted Laplacian on the class-II geodesic triangulation {3,5⁺}\_{n,n}. Verified to exact zero at n \= 1, 2, 3\.

**Theorem S22.1** proves the exact census V\_n \= 60n², E\_n \= 90n², F\_n \= 30n²+2, with exactly 12 pentagons, 30n²−10 hexagons, 60 (5,6) edges and 90n²−60 (6,6) edges, verified on every generated n ≤ 12 (F₁₂ \= 4322).

**Theorem S22.2** sharpens the seeded rank target. The difference Δ\_n(σ,ρ) − Δ\_n(1,1) is not merely finite rank: it is **exactly supported on the closed graph neighbourhood N\[P\] of the defect set**, a principal block of dimension 12 \+ 60 \= **72**, independent of n. Hence rank ≤ 72, with sub-bounds exactly 60 when ρ \= 1 and exactly 24 when σ \= 1\. The seeded bound 84 \= 12+60+12 is correct but not sharp: it double-counts the 12 pentagon directions, which already lie in range(B P\_e). Retraction S22-R1. Corollary S22.2a gives sup\_x |F\_{n,σ,ρ}(x) − F\_{n,1,1}(x)| ≤ 72/(30n²+2) → 0\.

**Theorem S22.3, reported against interest, and split by grade.** **S22.3(a) — PROVEN:** the number of I\_h edge orbits of K\_n is at least E\_n/|**I\_h**| \= 3n²/4 and therefore diverges, so the orbit complexity a metric prescription must resolve grows without bound. **S22.3(b) — COMPUTED over the audited range n ≤ 8:** the circumcentric DEC weights of a shape-regular geodesic realisation acquire 42 distinct edge values by n \= 8 and their bulk deviation from uniformity *grows* to 0.349 rather than decaying, so the **implemented** metric branch escapes the finite-defect class over that range. Version 1.5 carries this split into the abstract as well as §6: **it is not proved that the DEC weights escape finite-defect support at every n.** (a) proves growing orbit complexity; (b) computes the escape of the implemented branch for n ≤ 8\. The seed's branch table placed S-DEC and P-DEC inside W\_def(c,C); that placement is wrong over the audited range and is retracted (S22-R2).

**Result S22.4 — the main result, in three separately-graded parts.** The held-out extrapolation supports **two inequivalent candidate limits**, not one. The word *candidate* is load-bearing and v1.5 restores it throughout the abstract: no limit operator is constructed, so both the existence of the Class-MF limit and the separation of the two are **Conjecture S22.4c**, numerically supported. Version 1.1 splits the v1.0 statement, whose uniform "Theorem" heading over-graded a numerically-supported conjecture (review item 1).

- **Class MF (metric-free, finite-defect-supported).** Every audited uniformly bounded branch whose weights differ from counting on **O(1) cells** — counting (σ \= ρ \= 1), the ZS-S21 metric values frozen as a two-orbit perturbation, the flat-cone P1 reference, and both pre-registered ψ adversaries — **extrapolates toward a single common candidate limit**, with the five extrapolated values of λ₃/λ₁ agreeing to 0.0207 %. **The tested ratio is supported across two audited GC families**: the independent class-I family GP(n,0) returns 5.555733 against 5.555969, a difference of 0.0043 %. This is a proxy on one ratio, not a proof of carrier-family independence of the operator or of the low spectrum; §7.5 states the restriction and v1.4 no longer overstates it here.  
- **Class M (metric).** The genuine circumcentric DEC branch extrapolates instead toward the **round-sphere Laplace–Beltrami spectrum**, reproducing λ\_k/λ₁ \= l(l+1)/2 \= 1, 3, 6, 6, 10, 10, 15 to five or six digits.

**S22.4a (Class-MF invariance) — DERIVED-CONDITIONAL.** Any two uniformly bounded branches whose weights differ from counting on **O(1) cells** share the candidate limit, conditional on uniform low-mode delocalization **and** gradient control — for which ℒ₅ verifies only the absence of pentagon-mass concentration; the full L^∞ and gradient conditions remain **assumptions**, gate F-S22.28. This is a consequence of Theorem S22.2, not an extrapolation. **S22.4b (Class-M identification) — IMPORTED-PROVEN theorem \+ DERIVED-CONDITIONAL application \+ VERIFIED numerically.** DEC/FEEC consistency gives the round-sphere limit; the hypothesis-matching audit for this implementation is not performed, gate F-S22.29; the five-to-six-digit agreement was not fitted. **S22.4c (existence of the Class-MF limit operator and the class separation) — CONJECTURE, NUMERICALLY SUPPORTED.** No limit operator is constructed. This part, and only this part, rests on the held-out 1/n² protocol.

The two candidate limits are inequivalent under the audited protocol, and the discriminator is qualitative and gauge-group independent: **the metric class restores the full 2l+1 SO(3) degeneracy while the metric-free class does not.** The l \= 3 multiplet splits into T₂u(3) ⊕ G\_u(4) with a limiting splitting of **13.239 %** in Class MF against **−0.002 %** in Class M, the latter decaying monotonically 1.84 % → 0.12 % over n \= 3 → 12\.

**Theorem S22.9 — a sufficient finite-defect class with counterexamples, and a fourth retraction.** Version 1.0 wrote that "every branch whose weights are determined by combinatorial data alone" converges to the Class MF limit. That is **false**, and v1.1 retracts it (S22-R4). Three pre-registered global Layer-C adversaries — a *decaying* defect halo 1 \+ 0.8/(1+d), a diameter-normalized ramp 1 \+ 0.8·d/D, and a distance-parity weight 1 \+ 0.4·(d mod 2\) — are all uniformly bounded and use only combinatorial data, and **all three escape**, landing at 5.629673, 5.176935 and 5.512425 against the class value 5.555969. Even decay is not enough. Uniform boundedness **plus support on O(1) cells** is a **sufficient** condition for the audited Class-MF invariance — it is exactly the hypothesis of Theorem S22.2 — and the five audited branches all satisfy it, with total support ≤ 72 faces at every n. **Necessity remains OPEN**, gate F-S22.27: only **O(1) support ⟹ same candidate limit** is asserted, never the converse. The adversaries show the class is not *all* of Layer-C; they show nothing about what sharing the limit requires.

**Theorem S22.8 — I\_h isotypes, certified.** Version 1.0 assigned isotypes by multiplicity and continuity. Version 1.1 constructs the 120 elements of I\_h explicitly and the ten character projectors P\_α \= (d\_α/120) Σ\_g χ\_α(g)\* U\_n(g), with idempotence ≤ 2.8 × 10⁻¹⁶, mutual orthogonality ≤ 3.5 × 10⁻¹⁷, exact dimension sum, and isotype residuals ≤ 2.2 × 10⁻¹⁴. The decomposition Ω²(K₁) \= 2A\_g ⊕ 2T₁u ⊕ 2T₂u ⊕ H\_g² ⊕ G\_g ⊕ G\_u reproduces ZS-S21 erratum E-1a exactly, and the low-level labels reproduce ZS-S21 Table 9.1 exactly.

**Theorem S22.10 — the Mediation-Saturation Carrier Theorem.** Version 1.0 left carrier selection as an open recommendation for ZS-S23. Version 1.1 proves the combinatorial half. Impose (C1) twelve isolated pentagons, (C2) mediation saturation N\[P\] \= F(K) — no face lies outside the defect neighbourhood — and (C3) vertex-transitivity. Then (C1) gives |N\[P\]| ≤ 72; (C2) gives F \= 10T \+ 2 ≤ 72, hence T ≤ 7, hence T ∈ {1, 3, 4, 7} by Loeschian arithmetic; and (C3) requires |V| \= 20T to divide |Aut| ≤ |**I\_h**| \= 120 \= **Q**² − 1, which kills T \= 4 (V \= 80 ∤ 120\) and T \= 7 (V \= 140 \> 120). T \= 1 is the dodecahedron and violates (C1). Therefore **K \= GP(1,1) \= K\_TI, uniquely.** Crucially, saturation **alone** does not suffice: GP(2,0) also saturates, with F \= 42 \= |N\[P\]|, and is eliminated only by (C3). Any carrier-selection argument resting on saturation by itself is incomplete, and v1.1 records this because it is the kind of near-miss that would otherwise be reported as a success.

**Consequences for the ZS-S21 axiom register, stated symmetrically.**

1. **(Z-A1) is demoted.** Within the class the seed pre-registered, Outcome A fires: orbit-blindness is a finite-carrier regulator convention. It has no effect on any audited observable in the limit. This is a negative result about a Z-Spin postulate and we report it as one.  
2. **(Z-A0) is promoted.** The load-bearing choice is not orbit-blindness but the metric-free carrier itself. Against the metric class, Outcome C fires: the two prescriptions define genuinely different universality classes, and the separation *survives* regulator removal.  
3. **Gate F-S21.8 is re-attributed, not retired.** Its discriminator D₁ \= ω(T₂u,1)/ω(T₁u,1) separates the branches by 11.65 % at n \= 1 and by 3.92 % in the limit (2.357110 against 2.449497 \= √6). It remains a live experimental gate, but it tests (Z-A0), not (Z-A1).

The seed's preferred Outcome B — bulk universality with a surviving defect-localized sector — is **refuted**. No low mode is defect-localized: the witness ℒ₅ stays below 2.65 across the first fifteen levels at n \= 12 and the branch-sensitive modes sit at the *top* of the spectrum, where ℒ₅ → 0.24. Retraction S22-R3.

**The physics bridge is split off into ZS-S23 and ZS-S24, and one v1.2 claim is retracted here.** The action-to-Hessian bridge is now **ZS-S23 v1.0** and the finite-carrier SU(3) gap is now **ZS-S24 v1.0**. One correction must be recorded in this paper because it changes how §17.1 reads. Version 1.2 asserted that a literal metric reduction *forces* Class M, on the ground that "the I\_h-invariant conformal structure is unique, so all residual freedom is in the cell decomposition". **That is false and is retracted as S22-R6.** In two spatial dimensions the magnetic term sees the metric only through the area measure, so an I\_h-invariant conformal factor is an admissible **infinite-dimensional** freedom; ZS-S23 Theorem S23.2 **numerically realises** σ \= ρ \= 1 (residual 1.6 × 10⁻¹⁴, under finite quadrature on a fixed round-path network) for **two distinct audited conformal profiles**. That is enough to **refute** the earlier uniqueness / no-go claim; **a continuum of exact conformal solutions is not proved**, since establishing one would require an implicit-function argument with a non-singular Jacobian, which ZS-S23 does not supply. The geometric route therefore does not select Class M, and the honest reading is **non-identifiability** — the ZS-S20 shape recurring one level up, at the metric rather than at the measure. Section §17.1's layer-order reading survives as an interpretive frame, but it is no longer supported by any metric no-go, and none is claimed.

**The reframing, stated plainly, because v1.0 stopped one step too early.** Read narrowly, S22 says that a quadratic Hodge refinement cannot close Yang–Mills. That reading is correct and useless. The correct reading is that S22 *removes a false premise and locates the two remaining closure points*. The false premise is that the refinement limit is the physics: **conditional on (C1), (Z-A2) and (C3), Theorem S22.10 uniquely selects K\_TI \= GP(1,1); unconditional physical carrier selection remains OPEN.** Under those conditions the refinement family is a **diagnostic instrument** that identifies which universality class the finite theory belongs to, not a limit the theory must be taken to. What remains for closure is then exactly two things, both finite-carrier problems and both stated in §17: **exact holonomy reduction** — derive (H-W) from ZS-S14 by Whitney expansion instead of assuming it — and the **finite-carrier SU(3) spectral gap** on K\_TI itself. Neither is the Clay problem, and neither is claimed to be.

Finally, the limit of Class MF is identified structurally rather than numerically: it is the Laplace–Beltrami spectrum of the **flat singular metric with twelve cone points of angle 5π/3**, whose deficits sum to 12 × (π/3) \= 4π \= 2πχ \= 2π·dim(**Z**) — the corpus's own Spinor–Descartes–Euler identity. Under this reading the refinement limit does not dissolve Z-Spin geometry; it promotes the Regge/polyhedral concentration of curvature from a lattice regulator to a continuum geometric statement carrying a sharp degeneracy-based falsification test. That identification is registered at HYPOTHESIS-strong with gate F-S22.20, not asserted.

## §0.2 Hypothesis Register

**Version 1.4 correction, superseding the v1.2 correction.** Version 1.0 stated that ZS-S22 introduces no new hypothesis. That was true of v1.0 and false thereafter. After the three-way split, the hypotheses **belonging to this paper** are exactly two:

> **(Z-A2)** mediation saturation, §16.3; **(H-deloc)** the uniform low-mode delocalization and gradient-control hypotheses of Theorem S22.4a, §7.3.

**(Z-A3)**, carrier-clock identification, is **not** an axiom of this paper. It was introduced in ZS-S22 v1.2 §19, and that section is now **ZS-S23 v1.0 §4**; (Z-A3) is registered there and is audited there against ZS-S20's (H-PSM-2) and ZS-F40's √2 refusal. Version 1.3 left a stale reference to it in this register, and v1.4 removes it. Both remaining hypotheses are named, registered and gated. What remains true throughout is that ZS-S22 introduces **no new numerical constant and no fitted parameter**.

ZS-S22 imports the three named statements of ZS-S21 v1.2 unchanged and determines their fate under refinement.

**Table 0.1.** The imported hypothesis register, and what ZS-S22 does to each.

| Tag | Statement (ZS-S21 v1.2) | Fate under ZS-S22 refinement | Gate |
| ----- | ----- | ----- | ----- |
| **(H-W)** | The cellular reduction of ZS-S14 onto K × a\_tℤ is a Wilson-type group-valued plaquette action. | **Unchanged.** ZS-S22 does not prove or weaken it. Everything downstream still rests on it. | F-S21.11 (OPEN) |
| **(Z-A0)** | Metric-Free Carrier: K enters with incidence data (B₁, B₂) and the I\_h action only. | **PROMOTED** from one of two removal axioms to the sole load-bearing physical branch choice. Its negation defines a distinct, computable continuum universality class. | F-S21.7 (OPEN), F-S22.20 (NEW) |
| **(Z-A1)** | Orbit-Blind Plaquette Reduction: β\_e \= β\_t for all edges and β\_f \= β\_s for all faces. | **DEMOTED** to a finite-carrier regulator convention for every audited observable. Its removal changes no limit inside the metric-free class. | F-S21.10 (RE-SCOPED) |

Two additional items are honest disclosures rather than hypotheses.

**(L-AMB) Layer ambiguity.** ZS-S21's metric values σ \= 0.8973272361 and ρ \= 1.5100902868 belong to the *Archimedean* realisation of K\_TI. The canonical spherical-Voronoi realisation of the same combinatorial carrier returns σ \= 0.6157786465 and ρ \= 1.0623043176 at n \= 1\. Both are legitimate; neither is canonical. Every metric branch is embedding-dependent, whereas the metric-free branch is not. Registered as gate F-S22.22 and used in §9.3.

**(R-IDX) Regulator index.** n is a regulator index sent to infinity. It is not a fitted physical parameter, it is never chosen to match a number, and no result below depends on stopping at a particular n. This is the anti-numerology firewall on the family itself.

## §0.3 Pre-registered Outcomes and Realisation

Outcomes A–F were pre-registered in the ZS-S22 seed report before any K\_n with n ≥ 2 was generated.

**Table 0.2.** Outcome registry. A–F are pre-registered. The realised result is a *conjunction* on two different branch classes; the conjunction itself was not pre-registered and is labelled post-hoc.

| Outcome | Trigger | Realised |
| ----- | ----- | ----- |
| **A** — full low-energy universality | Every pre-registered low isotype ratio converges to a common branch-independent limit; no branch-separated defect outliers. | **YES, on the metric-free class W\_def.** Five branches agree to 0.0207 %. |
| **B** — bulk universality \+ defect branching (seed's preferred outcome) | A finite set of defect-localized modes retains distinct limits. | **NO — REFUTED.** ℒ₅ ≤ 2.65 on all low modes; branch-sensitive modes are at the spectral top. Retraction S22-R3. |
| **C** — global branching | A positive density of levels remains branch-dependent, or the difference is not finite rank. | **YES, against the metric class.** The metric branch is not finite rank (Thm S22.3) and its limit differs by 7.993 % in λ₃/λ₁. |
| **D** — orbit-blind selection by stability | Counting converges while every orbit-sensitive branch fails a non-arbitrary gate. | **NO.** Both ψ adversaries converge, and to the counting limit. |
| **E** — no canonical continuum family | GP(n,n) fails shape regularity or admits no comparison. | **NO.** The family is regular and the held-out 1/n² protocol is SUPPORTED for every branch. |
| **F** — quadratic/group-valued split | Compact U(1)/SU(2) observables remain branch-dependent beyond the defect sector. | **NOT TESTED.** The group-valued tier is out of scope in this paper. ZS-S23 v1.0 executes the action-to-Hessian half and ZS-S24 v1.0 the spectral half. |
| **A ∧ C** (post-hoc label) | Outcome A on W\_def *and* Outcome C across (Z-A0). | **REALISED.** This conjunction was not pre-registered and is labelled as such. |

## §0.4 Epistemic Status Legend

**Table 0.3.** Epistemic status legend used throughout ZS-S22.

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Mathematical theorem or exact arithmetic identity, established symbolically or verified to machine precision. |
| **IMPORTED-PROVEN** | Standard result of the external literature, cited and used but not re-proved here. |
| **DERIVED** | Quantitative consequence of PROVEN items plus LOCKED Z-Spin axioms. No new postulate. |
| **DERIVED-CONDITIONAL** | DERIVED given one explicitly named additional axiom, registered as a gate. |
| **VERIFIED** | Numerical confirmation on the actual Z-Spin object by an executable check in the companion. |
| **COMPUTED** | Numerical convergence or extrapolation result. **Not** a theorem, and never reported as one. |
| **PROXY** | Auxiliary family or generic model. Never counted as verification of the Z-Spin object. |
| **TESTABLE** | A number the framework predicts that an external measurement can contradict. |
| **HYPOTHESIS-strong** | Structural pattern with a coherent derivation sketch but no completed chain. |
| **OBSERVATION** | Numerical proximity, anti-numerology tested, with no derivation. Carries no evidential weight. |
| **OPEN** | Recognised gap requiring future work. |
| **NON-CLAIM** | Quantity explicitly NOT derived; honest acknowledgement of a framework limitation. |
| **RETRACTED** | A statement previously asserted in this corpus or in this paper's seed, and withdrawn, with the withdrawal recorded. |
| **RE-ATTRIBUTED** | A gate that remains live but is shown to test a different hypothesis than the one it was registered against. |
| **SUPERSEDED-BY-REFINEMENT** | A finite-K₁ branch dependence proved to vanish in the specified limit. |

**Do not use VERIFIED for an extrapolated n → ∞ value.** Every class limit in §7 and §8 is COMPUTED.

---

# §1. From S21 Selection to S22 Universality

## §1.1 What ZS-S21 proved

ZS-S21 constructed the Osterwalder–Seiler / Lüscher transfer matrix on K\_TI × a\_tℤ and obtained three things ZS-S20 could not. First, M₁ and M₂ are diagonal in the edge and face bases, necessarily and for *every* weight assignment, so the non-diagonal family is an empty set. Second, the 90 temporal plaquettes are congruent as primal cells, so no weight built from a plaquette's own primal geometry can separate the electric orbits. Third, the residual is not a continuum of undetermined directions but exactly two dimensionless ratios,

**σ \= m₅₆ / m₆₆**,  **ρ \= β₅ / β₆**,

on which exactly two families compete: the dual-measure family, removed by (Z-A0), and the ambient-combinatorial family, removed by (Z-A1). \[STATUS: IMPORTED-PROVEN — ZS-S21 v1.2 §4–§6\]

## §1.2 What ZS-S21 could not decide

The transfer matrix **proves diagonality but propagates, rather than selects, orbit weights**. ZS-S21 §15.4 stated the terminus in one sentence: nothing internal to a metric-free cell complex distinguishes the counting weight from any other function of the ambient combinatorial type. On one carrier that is final.

## §1.3 The new regulator-removal question

A statement can be underdetermined on every finite carrier and nevertheless become universal in the limit; conversely a finite number of topological defects can retain isolated modes. ZS-S21 has one carrier and cannot decide either possibility. ZS-S22 therefore asks a different question on a different logical layer:

> **Do the scale-free physical observables of Δ\_n(σ,ρ) become independent of (σ,ρ) as n → ∞?**

and breaks it into four non-equivalent sub-questions: bulk empirical spectral distribution (§6), fixed low modes (§7), representation content (§8), and group-valued observables (§10). The first is proved exactly. The second and third are computed with a held-out protocol. The fourth is out of scope here and is executed in ZS-S23 v1.0 and ZS-S24 v1.0.

**The paragraph written before K₂ was generated, preserved because it remained true.**

> ZS-S21 proved that the cellular transfer matrix fixes the form of the Hodge measure but not its two orbit weights. On a single truncated-icosahedron carrier that is the honest terminus: the orbit-blind rule is a postulate. ZS-S22 changes the question from selection to universality. The truncated icosahedron is the first member of an icosahedral Goldberg–Coxeter family in which the 12 pentagonal defects and 60 adjacent edges remain finite while the hexagonal bulk grows quadratically. Orbit-weight changes are therefore finite-rank perturbations of an increasing operator family. This paper proves the resulting bulk spectral universality theorem and then asks the only question that theorem cannot answer: whether the physical low-energy modes dissolve into the universal bulk or remain as a finite, defect-localized branch sector.

The answer to the closing question turned out to be neither of the two anticipated alternatives, and §7 says so.

---

# §2. The Goldberg–Coxeter Carrier Family

## §2.1 Definition

Let **K\_n := GP(n,n)**, n \= 1, 2, …, be the icosahedrally symmetric Goldberg polyhedron obtained from the (n,n) Goldberg–Coxeter construction \[1,2\]. Its dual is the class-II geodesic triangulation {3,5⁺}\_{n,n} of the icosahedron with triangulation number

**T\_n \= n² \+ n·n \+ n² \= 3n²**.

The generator is implemented in the companion from the 12 icosahedron vertices and the Eisenstein lattice patch, followed by radial projection and convex-hull triangulation. **No mesh file is imported.** \[STATUS: PROVEN — companion §S1\]

## §2.2 Theorem S22.1 — exact census

> **Theorem S22.1 (Goldberg Carrier Census).** For every n ≥ 1, V\_n \= 20T\_n \= **60n²**, and since the graph is cubic, E\_n \= (3/2)V\_n \= **90n²**, and Euler gives F\_n \= 2 \+ E\_n − V\_n \= **30n² \+ 2**. Every fullerene has exactly 12 pentagons, so F₅,n \= **12** and F₆,n \= **30n² − 10**. In the isolated-pentagon GP(n,n) sequence, E₅₆,n \= **60** and E₆₆,n \= **90n² − 60**. Consequently the face- and edge-defect fractions vanish as F₅,n/F\_n \= 12/(30n²+2) \= O(n⁻²),  E₅₆,n/E\_n \= 60/90n² \= 2/(3n²).

**\[STATUS: PROVEN — checks T010–T015, verified on n ∈ {1,2,3,4,5,6,8,10,12}\]**

**Table 2.1.** Executable census. All entries are computed from the generated complex, not quoted. K₁ is the truncated icosahedron of ZS-S17–S21.

| n | V\_n | E\_n | F\_n | pentagons | (5,6) edges | pentagons isolated |
| ----- | ----- | ----- | ----- | ----- | ----- | :---: |
| 1 | 60 | 90 | 32 | 12 | 60 | yes |
| 2 | 240 | 360 | 122 | 12 | 60 | yes |
| 3 | 540 | 810 | 272 | 12 | 60 | yes |
| 4 | 960 | 1440 | 482 | 12 | 60 | yes |
| 5 | 1500 | 2250 | 752 | 12 | 60 | yes |
| 6 | 2160 | 3240 | 1082 | 12 | 60 | yes |
| 8 | 3840 | 5760 | 1922 | 12 | 60 | yes |
| 10 | 6000 | 9000 | 3002 | 12 | 60 | yes |
| 12 | 8640 | 12960 | 4322 | 12 | 60 | yes |

Euler characteristic χ \= V − E \+ F \= 2 is verified at every n (check T014), and the cubic relation 3V \= 2E at every n (check T015).

## §2.3 Why GP(n,n) is the correct primary family

It satisfies all five requirements simultaneously: K₁ \= K\_TI exactly; I\_h symmetry is retained at every n; the 12 pentagonal curvature defects remain topologically fixed; the hexagonal bulk grows as O(n²); and the mesh size tends to zero on the unit sphere. This isolates exactly the ZS-S21 question: the orbit-sensitive terms remain attached to a fixed number of defects while the bulk becomes large.

## §2.4 Lemma S22.0 — the dual-graph reduction

This lemma is the computational spine of the paper and is stated separately because it is what makes n \= 12 (F₁₂ \= 4322\) tractable at all.

> **Lemma S22.0 (Dual-Graph Reduction).** Let K be a cell complex on S² with signed face–edge incidence B₂. Then B₂B₂ᵀ is the graph Laplacian L(G) of the dual 1-skeleton G, whose vertices are the faces of K and whose edges are the edges of K. For K\_n \= GP(n,n), G\_n is the geodesic triangulation {3,5⁺}\_{n,n}, with 30n²+2 vertices of which exactly 12 have degree 5\. Consequently, with S \= diag(√β\_f) and L\_w the weighted graph Laplacian carrying edge weight 1/m\_e, **Δ\_n(σ,ρ) \= M₂^{1/2} B₂ M₁⁻¹ B₂ᵀ M₂^{1/2} \= S L\_w S.** Under this dictionary the 12 pentagons of K\_n are the 12 degree-5 vertices of G\_n, and the 60 (5,6) edges of K\_n are the 60 edges of G\_n incident to a degree-5 vertex.

**\[STATUS: PROVEN — checks T020.1–T020.3, max |B₂B₂ᵀ − Δ\_n(1,1)| \= 0.000e+00 at n \= 1, 2, 3\]**

The lemma also explains the ZS-S21 spectrum structurally: the eigenvalues of B₂B₂ᵀ on K\_TI are exactly the graph-Laplacian eigenvalues of the pentakis dodecahedron, whose degree sum 12·5 \+ 20·6 \= 180 \= 2E reproduces Tr Δ₂ \= 2E without any convention being imposed.

## §2.5 Geometry layers — never mixed

Three distinct objects are maintained throughout, and every branch declares which layer supplies its measures.

- **Layer C — combinatorial carrier.** Incidence, orientation, face degree, edge-star type, I\_h action. This is the (Z-A0) carrier. The counting theorem consumes **only** Layer C.  
- **Layer S — canonical spherical embedding.** Radial projection of the geodesic triangulation onto the unit sphere; spherical circumcentric dual lengths and areas.  
- **Layer P — intrinsic polyhedral embedding.** Planar polygonal faces in ℝ³ with chordal circumcentric dual data.

Layer S and Layer P are **not** the same metric and are never described as such. §9.3 shows that at n \= 1 they do not even agree with the Archimedean realisation whose values ZS-S21 audited.

---

# §3. The Admissible Branch Class and the Normalization Firewall

## §3.1 The two-orbit model and the bounded-defect class

The minimal family inherited from ZS-S21 is

**M̂₁,n(σ) \= I\_{E\_n} \+ (σ−1) P₅₆,n**,  **M̂₂,n(ρ) \= I\_{F\_n} \+ (ρ−1) P₅,n**,

where P₅₆,n projects onto the 60 (5,6) edges and P₅,n onto the 12 pentagons, so rank P₅₆,n \= 60 and rank P₅,n \= 12 for every n. The operator is

**Δ\_n(σ,ρ) \= S\_{ρ,n} B₂,n D\_{σ,n} B₂,nᵀ S\_{ρ,n}**,  S\_{ρ,n} \= M̂₂,n(ρ)^{1/2},  D\_{σ,n} \= M̂₁,n(σ)⁻¹.

The theorems of §5 are proved for the whole bounded-defect class

**𝒲\_def(c,C) \= { (σ\_n, ρ\_n) : 0 \< c ≤ σ\_n, ρ\_n ≤ C \< ∞ }**,

so that no result depends on the particular ZS-S21 numerical values.

## §3.2 The audited branches, pre-registered

**Table 3.1.** The six branches, their layer, and their role. Only the first five were used for the class-limit determination; P-DEC is an independent-realisation control.

| Branch | Layer | 1/m\_e | β\_f | Role |
| ----- | ----- | ----- | ----- | ----- |
| **C** — counting | C | 1 | 1 | the (Z-A1) orbit-blind branch |
| **S21f** — ZS-S21 metric frozen | C | 1/0.8973272361 on (5,6) | 1.5100902868 on pentagons | the ZS-S21 full-metric values continued as a two-orbit member of 𝒲\_def |
| **FLAT** — flat-cone P1 reference | C | 1 | 6/deg | the consistent P1 finite-element Laplacian of an equilateral triangulation |
| **ψ₊** — combinatorial adversary | C | 12/(deg u \+ deg v) | deg/6 | pre-registered adversary, not a candidate Z-Spin theory |
| **ψ₋** — reciprocal adversary | C | (deg u \+ deg v)/12 | 6/deg | pre-registered adversary |
| **S-DEC** — spherical circumcentric DEC | S | |⋆e|/|e|, spherical | 1/A\_f, spherical | the genuine metric branch (Christ–Friedberg–Lee class \[5,6\]) |
| **P-DEC** — chordal circumcentric DEC | P | |⋆e|/|e|, chordal | 1/A\_f, planar | independent-realisation control |

The ψ branches are **not** candidate Z-Spin theories. They are adversarial prescriptions registered in advance to show whether any result is specific to two metric examples.

## §3.3 Normalization firewall

A branch-dependent overall rescaling is full rank and would obscure every finite-rank statement. Therefore, and without exception:

1. The rank theorem of §5 is proved with the hexagon and (6,6) bulk weights normalized to 1\.  
2. Low-energy comparisons use only the **scale-free** ratios λ\_k/λ₁ and ω\_k/ω₁ \= √(λ\_k/λ₁).  
3. For the K₁ regression only, the ZS-S21 convention (H-TR), Tr Δ₂ \= 2E \= 180, is applied so that the comparison is like-for-like.  
4. **No branch is ever compared under a different scale convention from another.** Gate F-S22.7 is registered against any such comparison.

The scale r \= β\_s/(β\_t a\_t²) remains a calibration and is not part of (σ, ρ).

---

# §4. K₁ Regression — the Gate That Must Fire First

Before any refinement claim, the construction is required to reproduce ZS-S21 exactly on its own carrier. This is gate F-S22.1 and it is the first thing the companion executes.

**Table 4.1.** K₁ regression against ZS-S21 v1.2 Table 6.2, in the (H-TR) convention. Nine levels are compared for each metric branch and eight for the counting branch.

| Branch | (σ, ρ) | levels compared | max |computed − ZS-S21| | check |
| ----- | ----- | ----- | ----- | ----- |
| counting | (1, 1\) | 8 | 4.987 × 10⁻¹¹ | T030.counting |
| spatial CFL | (1, 1.5100902868) | 9 | 8.187 × 10⁻¹¹ | T030.cfl |
| full metric | (0.8973272361, 1.5100902868) | 9 | 1.033 × 10⁻¹⁰ | T030.fullmetric |

The two LOCKED corpus numbers are reproduced from a carrier rebuilt from scratch:

**λ₁ \= 1.2428416164** (deviation 1.49 × 10⁻¹¹, check T031) and **λ\_h \= 7.5210904061** (deviation 1.47 × 10⁻¹¹, check T032).

Both are reproduced, not re-fitted. The reordering that ZS-S21 §6.5 identified as its sharpest discriminator is reproduced as well: at n \= 1 the third-lowest excitation has multiplicity 3 and isotype T₂u in the counting branch and multiplicity 4 and isotype G\_u in both metric branches. **Gate F-S22.1 does not fire.** \[STATUS: VERIFIED\]

---

# §5. Theorem S22.2 — the Defect-Support Theorem

## §5.1 Statement

The seed targeted rank ≤ 84 \= 12 \+ 60 \+ 12\. The correct statement is stronger in kind, not only in size: the perturbation is not merely of finite rank, it is **supported on a finite principal block**.

Let P ⊂ F(K\_n) be the set of 12 pentagons and let **N\[P\]** be its closed neighbourhood in the dual graph G\_n, that is P together with every face sharing an edge with a pentagon. Since pentagons are isolated and pentagonal, each pentagon has exactly 5 hexagonal neighbours, all distinct across pentagons, so

**|N\[P\]| \= 12 \+ 60 \= 72**,  independent of n, for every n ≥ 2\.

> **Theorem S22.2 (Defect-Support Theorem).** For every n ≥ 1 and every σ, ρ \> 0, **Δ\_n(σ,ρ) − Δ\_n(1,1) is zero outside the principal block N\[P\] × N\[P\].** Consequently **rank\[ Δ\_n(σ,ρ) − Δ\_n(1,1) \] ≤ |N\[P\]| \= 72**, independent of n, with the sub-bounds **60** when ρ \= 1 and **24** when σ \= 1\.

**\[STATUS: PROVEN — checks T040–T044\]**

## §5.2 Proof

By Lemma S22.0 write Δ\_n(σ,ρ) \= S L\_w S with S \= diag(√β\_f) and L\_w the weighted graph Laplacian of G\_n. The entries are, for u ≠ v adjacent,

(Δ\_n)*{uv} \= −√(β\_u β\_v) · w*{uv},  and  (Δ\_n)*{uu} \= β\_u · Σ*{e ∋ u} w\_e .

*Off-diagonal.* The entry (u,v) differs from its counting value iff β\_u ≠ 1, or β\_v ≠ 1, or w\_{uv} ≠ 1\. In the two-orbit model β\_u ≠ 1 requires u ∈ P, and w\_{uv} ≠ 1 requires the edge uv to be a defect edge, which by the census happens exactly when one endpoint is in P. In all three cases at least one of u, v lies in P and the other, being adjacent to it, lies in N\[P\]. Hence both indices lie in N\[P\].

*Diagonal.* The entry (u,u) differs from its counting value iff β\_u ≠ 1 or some incident edge is a defect edge, that is iff u ∈ P or u is adjacent to a pentagon; in both cases u ∈ N\[P\].

Therefore every nonzero entry of the difference has both indices in N\[P\], so the difference equals its own N\[P\] × N\[P\] principal block padded by zeros, and its rank is at most |N\[P\]| \= 72\.

*Sub-bounds.* If ρ \= 1 then S \= I and the difference is B₂(D − I)B₂ᵀ with rank(D − I) ≤ 60\. If σ \= 1 then D \= I and, writing s \= S − I with rank 12, the difference is sX \+ Xs \+ sXs with X \= B₂B₂ᵀ, whose range lies in span(range s) \+ span(X · range s), of dimension at most 24\.

## §5.3 Sharpness audit and the correction to the seed

**Table 5.1.** Observed exact ranks at five (σ, ρ) test points, together with the support test. Test points: (1.3, 1), (1, 1.7), (1.3, 1.7), (0.8973272361, 1.5100902868), (0.4, 2.9).

| n | |N\[P\]| | observed ranks at the five test points | support outside N\[P\]×N\[P\] |
| ----- | ----- | ----- | :---: |
| 1 | 32 | 31, 24, 32, 32, 32 | 0 |
| 2 | 72 | 60, 24, 72, 72, 72 | 0 |
| 3 | 72 | 60, 24, 72, 72, 72 | 0 |
| 4 | 72 | 60, 24, 72, 72, 72 | 0 |
| 5 | 72 | 60, 24, 72, 72, 72 | 0 |
| 6 | 72 | 60, 24, 72, 72, 72 | 0 |

The bound **72 is sharp for generic (σ, ρ) and every n ≥ 2**, and the two sub-bounds 60 and 24 are attained exactly (checks T043, T044). At n \= 1 the bound degenerates to F₁ \= 32 because rank B₂ \= 31 there; the defect neighbourhood already exhausts the carrier, which is precisely the sense in which K\_TI is *all defect*.

> **Retraction S22-R1 (against the ZS-S22 seed).** The seed's target bound rank ≤ 84 \= 12 \+ 60 \+ 12 is a true but non-sharp bound. The decomposition (S−I)BDBᵀS \+ B(D−I)BᵀS \+ BBᵀ(S−I) counts the 12 pentagon directions twice: range(B P\_e) already contains the 12 pentagon indicators, because every defect edge is incident to exactly one pentagon. The sharp constant is 72, and the sharp statement is support, not rank. **\[STATUS: RETRACTED and replaced\]**

## §5.4 Corollary S22.2a — bulk empirical spectral universality

For Hermitian N × N matrices, Bai's rank inequality \[9\] gives sup\_x |F\_A(x) − F\_B(x)| ≤ rank(A−B)/N. With Theorem S22.2,

> **Corollary S22.2a.** For every n and every (σ, ρ) ∈ 𝒲\_def(c,C), **sup\_x | F\_{n,σ,ρ}(x) − F\_{n,1,1}(x) | ≤ 72 / (30n² \+ 2\) \= O(n⁻²).** Hence if the counting-branch empirical spectral measures converge along K\_n, every branch in 𝒲\_def converges to the same limiting empirical spectral measure. Orbit weights cannot define different bulk spectral universality classes on this family.

**\[STATUS: PROVEN, conditional on existence of one bulk limit — checks T050.2–T050.6\]**

**Table 5.2.** The bound against the measured Kolmogorov distance between the counting and S21f branches. The bound is never violated and is never tight, as expected for a worst-case rank bound.

| n | F\_n | measured sup\_x |F − F| | bound 72/F\_n |
| ----- | ----- | ----- | ----- |
| 2 | 122 | 0.147541 | 0.590164 |
| 3 | 272 | 0.073529 | 0.264706 |
| 4 | 482 | 0.053942 | 0.149378 |
| 5 | 752 | 0.029255 | 0.095745 |
| 6 | 1082 | 0.025878 | 0.066543 |

**What the theorem does not prove.** It does not imply λ\_{n,k}(σ,ρ) − λ\_{n,k}(1,1) → 0 for fixed k. A rank-72 perturbation can shift up to 72 eigenvalues by O(1), and by Cauchy interlacing it can shift any eigenvalue by at most 72 *index positions*. Since the target low-mode window is K \= 30 \< 72, the theorem is silent exactly where the physics lives. This limitation is not a weakness; it identifies the only place where branch physics could survive, and §7 goes there.

---

# §6. Theorem S22.3 — Growing Orbit Complexity (PROVEN) and the Escape of the Implemented Metric Branch (COMPUTED, n ≤ 8\)

## §6.1 Reported against interest

The seed's Table of admissible branches placed S-DEC and P-DEC inside the two-orbit class 𝒲\_def(c,C), so that Theorem S22.2 would apply to them. That placement is **false for n ≥ 2** and is retracted before it is used.

The reason is geometric and unavoidable. On K₁ \= K\_TI the hexagons are all congruent and the (6,6) edges are all congruent, so a metric prescription produces exactly two edge values and two face values. On K\_n with n ≥ 2 the hexagons of a Goldberg polyhedron are **not** congruent: the geodesic realisation distorts cells continuously between the icosahedral vertex neighbourhoods and the face interiors, and this distortion converges to a fixed smooth field rather than decaying.

> **Theorem S22.3 (The Metric Class Escapes the Defect Neighbourhood; sharpened in v1.1).** **(a) PROVEN.** The number of I\_h edge orbits of K\_n is at least E\_n/|I\_h| \= 90n²/120 \= **3n²/4**, by orbit–stabiliser, and therefore diverges. A metric prescription is constant on orbits and generically distinct across them. **(b) COMPUTED over the audited range n ≤ 8\.** For the spherical circumcentric DEC branch the number of distinct edge weights is 2, 4, 9, 13, 19, 26, 42 at n \= 1, 2, 3, 4, 5, 6, 8, and the bulk deviation ε\_n := max\_{e ∉ E₅₆} | 1/m\_e − 1 | is non-decreasing over that range. Consequently Δ\_n^{DEC} − Δ\_n(1,1) is not supported on N\[P\] × N\[P\], Theorem S22.2 does not apply, and the metric branch is not a member of 𝒲\_def(c,C).

**\[STATUS: (a) PROVEN — checks T150.1–T150.6; (b) COMPUTED over the audited range, NOT asserted to grow without bound — checks T060, T061, T062\]**

*Version 1.1 correction (review item 4).* Version 1.0 wrote "the number of distinct edge weights grows without bound" and presented it as proved. Only the orbit count is proved; the weight count is a finite computation over n ≤ 8\. The claim is split accordingly. The proved half is already sufficient for the theorem's use, since a two-orbit model cannot represent an operator constant on ≥ 3n²/4 orbits with generically distinct values.

**Table 6.0.** Orbit lower bound against measurement.

| n | E\_n | proved bound 3n²/4 | measured I\_h edge orbits | distinct DEC weights |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 90 | 0.75 | 2 | 2 |
| 2 | 360 | 3.00 | 5 | 4 |
| 3 | 810 | 6.75 | 10 | 9 |
| 4 | 1440 | 12.00 | 16 | 13 |
| 5 | 2250 | 18.75 | 24 | 19 |
| 6 | 3240 | 27.00 | 33 | 26 |

**Table 6.1.** The genuine metric branch escapes the defect neighbourhood. Bulk deviations are measured over the (6,6) edges and hexagonal faces only, after normalizing the bulk median to 1\.

| n | distinct edge weights | max |1/m\_e − 1| on the bulk | max |β\_f − 1| on the bulk |
| ----- | ----- | ----- | ----- |
| 1 | 2 | 0.000000 | 0.000000 |
| 2 | 4 | 0.095101 | 0.126335 |
| 3 | 9 | 0.121157 | 0.233284 |
| 4 | 13 | 0.200855 | 0.286623 |
| 5 | 19 | 0.253512 | 0.377059 |
| 6 | 26 | 0.308233 | 0.393983 |
| 8 | 42 | 0.349216 | 0.462407 |

> **Retraction S22-R2 (against the ZS-S22 seed).** The seed's branch table assigned S-DEC and P-DEC a "spherical dual/primal ratio" and a "spherical area ratio" as if these were two numbers (σ\_n, ρ\_n). They are not. For n ≥ 2 they are 30n²-dimensional weight fields with O(1) bulk variation. The seed's §4.2 branch table is corrected accordingly. **\[STATUS: RETRACTED and replaced\]**

## §6.2 Why this is the important discovery, not a nuisance

The natural reading of Theorem S22.3 is that the metric branch is "badly behaved". It is the opposite. A shape-regular circumcentric DEC operator is precisely the object that is *guaranteed* to converge to the Laplace–Beltrami operator of the underlying smooth surface, and its consistency is independent of how distorted the mesh is \[14,15\]. The uniform-weight graph Laplacian carries no such guarantee, because it has no access to any metric at all.

So the two prescriptions are not two approximations of one thing. They are approximations of two different things, and §7 identifies both.

---

# §7. Result S22.4 — the Two Universality Classes (S22.4a DERIVED-CONDITIONAL, S22.4b IMPORTED-PROVEN, S22.4c CONJECTURE)

## §7.1 Protocol, pre-registered

The convergence protocol was fixed before the n ≥ 2 spectra were inspected.

1. Compute the first eight nonzero levels with multiplicities for each branch on n ∈ {3, 4, 5, 6, 8, 10, 12}.  
2. Fit **L \+ a/n² \+ b/n⁴** on n ∈ {3, 4, 5, 6, 8, 10}.  
3. **Hold n \= 12 out.** Call the extrapolation SUPPORTED only if the held-out value is reproduced to better than 5 × 10⁻³.  
4. Compare branch limits only after each branch passes its own held-out test.  
5. Label every extrapolated limit **COMPUTED**, never PROVEN.  
6. Match levels by multiplicity and I\_h isotype, never by ordinal index alone, since the ordering changes between branches.

No convergence claim below rests on n \= 1, 2, 3 alone.

## §7.2 The measured sequences

**Table 7.1.** λ₃/λ₁ — the level carrying I\_h isotype T₂u with multiplicity 3 in every metric-free branch. The five metric-free branches converge together; S-DEC converges elsewhere.

| n | C | S21f | FLAT | ψ₊ | ψ₋ | S-DEC |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 3 | 5.33316 | 5.43888 | 5.39847 | 5.24166 | 5.41237 | 5.73836 |
| 4 | 5.42942 | 5.49012 | 5.46628 | 5.37645 | 5.47468 | 5.84981 |
| 5 | 5.47456 | 5.51403 | 5.49815 | 5.44053 | 5.50350 | 5.90303 |
| 6 | 5.49924 | 5.52701 | 5.51562 | 5.47569 | 5.51924 | 5.93234 |
| 8 | 5.52393 | 5.53985 | 5.53313 | 5.51083 | 5.53504 | 5.96176 |
| 10 | 5.53542 | 5.54574 | 5.54130 | 5.52713 | 5.54244 | 5.97547 |
| **12** | **5.54167** | **5.54892** | **5.54576** | **5.53597** | **5.54650** | **5.98294** |

**Table 7.2.** Held-out extrapolation. Every branch passes; gate F-S22.10 does not fire.

| Branch | L\_∞ | prediction at n \= 12 | actual at n \= 12 | |Δ| | verdict |
| ----- | ----- | ----- | ----- | ----- | :---: |
| C | 5.555831 | 5.541633 | 5.541674 | 4.09 × 10⁻⁵ | SUPPORTED |
| S21f | 5.556412 | 5.549041 | 5.548918 | 1.23 × 10⁻⁴ | SUPPORTED |
| FLAT | 5.555778 | 5.545696 | 5.545757 | 6.11 × 10⁻⁵ | SUPPORTED |
| ψ₊ | 5.556486 | 5.536131 | 5.535972 | 1.60 × 10⁻⁴ | SUPPORTED |
| ψ₋ | 5.555337 | 5.546320 | 5.546505 | 1.85 × 10⁻⁴ | SUPPORTED |
| S-DEC | 6.000033 | 5.982962 | 5.982944 | 1.81 × 10⁻⁵ | SUPPORTED |

The five metric-free limits agree to a spread of **0.0207 %**. The metric limit sits **7.993 %** away and does not move toward them.

The pre-registered 1/n² ansatz is justified rather than assumed: the local convergence exponent measured on consecutive pairs is 1.968, 1.979, 1.986, 1.992, 2.000, **2.008**, converging to 2 (check T090).

## §7.3 Statement

**Version 1.1 restatement (review item 1).** Version 1.0 gave this a single "Theorem" heading while its own status line said COMPUTED. That is an over-grading and is corrected here by splitting the statement into three parts with three different statuses. Only part (c) rests on extrapolation.

> **Theorem S22.4a (Class-MF Invariance).** Let (w\_e, w\_f) and (w′\_e, w′\_f) be two weight assignments that are uniformly bounded, 0 \< c ≤ w ≤ C \< ∞, and that each differ from the counting weights on a set of cells of size **O(1) independent of n**. If the counting-branch low eigenfunctions are asymptotically delocalized, then for every fixed k the scale-free ratios λ\_k/λ₁ of the two assignments have the same limit. *Proof sketch.* By Theorem S22.2 each difference is supported on a principal block of fixed dimension B ≤ 72\. In the generalized Rayleigh quotient λ\_k \= min-max Q(v)/N(v) with Q(v) \= Σ\_e (1/m\_e)(dv)\_e² and N(v) \= Σ\_f v\_f²/β\_f, a delocalized low mode has |v\_f|² \~ ⟨v²⟩ and (dv)\_e² \~ O(h²) \= O(n⁻²) uniformly, so N receives a relative change O(B/F\_n) \= O(n⁻²) and Q a relative change O(B·n⁻² / (E\_n·n⁻²)) \= O(B/E\_n) \= O(n⁻²). Hence λ\_k(w)/λ\_k(w′) \= 1 \+ O(n⁻²) for fixed k. **\[STATUS: DERIVED-CONDITIONAL on uniform low-mode delocalization AND uniform gradient control; NUMERICALLY SUPPORTED by the ℒ₅ witness of §8.1 and by the observed 0.0207 % spread across five audited branches. Version 1.2 weakens v1.1's wording: ℒ₅ \< 3 witnesses absence of pentagon mass concentration, but the proof sketch additionally requires a uniform L^∞ bound on fixed-k eigenfunctions, a gradient-energy bound on the defect edges, absence of newly created low localized states, and uniformity in n. Only the first is directly measured. Gate F-S22.28.\]**  
>   
> **Theorem S22.4b (Class-M Identification).** Every shape-regular circumcentric DEC branch on a spherical realisation of K\_n converges to the round-sphere Laplace–Beltrami spectrum, λ\_k/λ₁ \= l(l+1)/2. **\[STATUS: IMPORTED-PROVEN theorem \[14,15\] \+ DERIVED-CONDITIONAL application \+ VERIFIED numerically. Version 1.2 downgrades v1.1's flat IMPORTED-PROVEN: the general DEC/FEEC consistency theorems exist, but a theorem-level audit matching this implementation to their hypotheses — spherical Delaunay condition, positive circumcentric dual, mesh shape regularity, mass-lumping convention, spectral-convergence hypothesis, and the exact equivalence of S L\_w S to the standard generalized eigenproblem — is NOT carried out here. Gate F-S22.29. The numerical agreement is to five or six digits — 1, 3.000001, 6.000033, 5.999959, 9.999953, 9.999954, 15.000048 — a sequence that was not fitted and that independently validates the extrapolation protocol\]**  
>   
> **Conjecture S22.4c (Class Separation), numerically supported.** The Class-MF limit operator exists, and the two class limits are distinct: λ₃/λ₁ \= 5.5560 ± 0.0012 against 6, a separation of 7.993 % that does not decay with n. **\[STATUS: CONJECTURE, NUMERICALLY SUPPORTED — held-out 1/n² protocol passed by all six branches, measured convergence exponent 2.008. No limit operator is constructed, and this is NOT a theorem.\]**

**Table 7.3.** The two class limits, extrapolated. The Class-MF column is a Conjecture S22.4c object; the Class-M column is Theorem S22.4b and its agreement with l(l+1)/2 is the control. Multiplicities are those observed at n \= 12\. Class M reproduces l(l+1)/2 \= 1, 3, 6, 6, 10, 10, 15 to five or six digits — an independent confirmation that the extrapolation protocol is sound, since that answer was not fitted.

| level | I\_h content | Class MF limit λ\_k/λ₁ | mult | Class M limit λ\_k/λ₁ | mult | round-sphere l(l+1)/2 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | T₁u | 1.000000 | 3 | 1.000000 | 3 | 1 (l \= 1\) |
| 2 | H\_g | 2.990865 | 5 | 3.000001 | 5 | 3 (l \= 2\) |
| 3 | T₂u | **5.555831** | 3 | 6.000033 | 3 | 6 (l \= 3\) |
| 4 | G\_u | **6.343491** | 4 | 5.999959 | 4 | 6 (l \= 3\) |
| 5 | H\_g | **9.588904** | 5 | 9.999953 | 5 | 10 (l \= 4\) |
| 6 | G\_g | **10.563319** | 4 | 9.999954 | 4 | 10 (l \= 4\) |
| 7 | T₁u | 13.862185 | 3 | 15.000048 | 5 | 15 (l \= 5\) |

## §7.4 The qualitative discriminator: degeneracy restoration

The sharpest statement needs no percent-level accuracy at all. In Class M the SO(3) multiplet structure is restored: the l \= 3 septet fuses and the l \= 4 nonet fuses. In Class MF they do not.

**Table 7.4.** The l \= 3 splitting (λ₄ − λ₃) / mean, per n. Class M decays monotonically toward zero; Class MF stabilises at a finite value.

| n | Class MF (counting) | Class M (S-DEC) |
| ----- | ----- | ----- |
| 3 | 14.3197 % | 1.8406 % |
| 4 | 13.8573 % | 1.0773 % |
| 5 | 13.6390 % | 0.6997 % |
| 6 | 13.5186 % | 0.4899 % |
| 8 | 13.3966 % | 0.2779 % |
| 10 | 13.3389 % | 0.1785 % |
| 12 | 13.3071 % | 0.1242 % |
| **extrapolated** | **13.239 %** | **−0.002 %** |

**\[STATUS: COMPUTED — checks T074, T075, T075b, T076\]**

This is the result the seed's item 6 anticipated could not be settled by the rank theorem, and it is settled: the surviving branch dependence is **not** carried by defect-localized modes, it is carried by the presence or absence of a metric in the bulk, and it shows up as an exact symmetry statement.

## §7.5 Carrier-family independence

If the Class MF limit were an artefact of GP(n,n) it would not be a universality class. It is not.

**Table 7.5.** The independent class-I family GP(n,0), generated by the same code with (h,k) \= (n,0), whose census is 10n²+2 dual vertices with 12 pentagons — a *different* carrier family with a different combinatorial law.

| family | census of dual | n used | extrapolated λ₃/λ₁ |
| ----- | ----- | ----- | ----- |
| class-II GP(n,n) | 30n² \+ 2 | 3–12 | 5.555969 |
| class-I GP(n,0) | 10n² \+ 2 | 4–12 | 5.555733 |
|  |  |  | **difference 0.0043 %** |

**\[STATUS: SUPPORTED ACROSS TWO AUDITED GC FAMILIES — proxy P081. This is *not* a proof of carrier-family independence. One ratio, λ₃/λ₁, was compared across two families. Neither the full operator nor the full low spectrum has been shown to be family independent, and v1.1 declines the stronger wording used in v1.0 (review item 3).\]**

Within that audited scope the Class MF limit behaves like a property of the *underlying singular surface* rather than of the refinement family, and §9.1 offers a structural identification of that surface — again as a hypothesis with a gate, not as a theorem.

---

# §8. Defect Localization: the Seed's Preferred Outcome Is Refuted

## §8.1 The witness

For a normalized face eigenvector u, define **ℒ₅(u) \= (F\_n/12) Σ\_{f ∈ pentagons} |u(f)|²**. Then ℒ₅ ≈ 1 for a bulk-delocalized state, ℒ₅ ≫ 1 for pentagon-defect localization, and ℒ₅ → 0 for a defect-avoiding state. The threshold τ \= 3 was fixed before inspection.

**Table 8.1.** Localization witness in the counting branch, over the first fifteen nonzero levels and over the eight highest levels.

| n | F\_n | ℒ₅ over low modes 1–15 | ℒ₅ over the top 8 modes |
| ----- | ----- | ----- | ----- |
| 4 | 482 | \[0.000, 2.722\] | \[0.000, 0.421\] |
| 8 | 1922 | \[0.000, 2.660\] | \[0.000, 0.294\] |
| 12 | 4322 | \[0.000, 2.644\] | \[0.000, 0.243\] |

No low mode exceeds τ \= 3, and the maximum *decreases* with n. **No low-lying state is defect-localized.** \[STATUS: VERIFIED — checks T100.4, T100.8, T100.12\]

## §8.2 Where the branch sensitivity actually lives

**Table 8.2.** Relative shift of the sorted normalized spectrum at n \= 6, by quantile. "in-class" compares counting against S21f, both in Class MF; "cross-class" compares counting against S-DEC.

| quantile | 0.02 | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 | 0.98 | 1.00 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| in-class | 0.0036 | 0.0023 | 0.0029 | 0.0028 | 0.0049 | 0.0008 | 0.0026 | 0.1361 |
| cross-class | 0.0535 | 0.0152 | 0.0010 | 0.0309 | 0.0076 | 0.0763 | 0.2495 | 0.5347 |

Within Class MF the shift is below 0.5 % everywhere except the single extreme eigenvalue, exactly as Theorem S22.2 requires: a rank-72 perturbation of a 1082-dimensional operator can move a handful of extremal eigenvalues and nothing else. Across classes the shift reaches 53 % at the top and stays at the several-percent level throughout the bulk. \[STATUS: VERIFIED — checks T110, T111\]

> **Retraction S22-R3 (against the ZS-S22 seed).** The seed nominated Outcome B, "universal bulk ⊕ finite defect sector", as the preferred and most informative outcome, and predicted that the physically important low modes might "become localized on the 12 curvature defects". This is **refuted**. The finite defect sector exists and is exactly 72-dimensional as an operator support, but it does **not** produce low-energy branch-separated states: the modes it moves are extremal. The physically informative split is not bulk-versus-defect but **metric-versus-metric-free**. **\[STATUS: RETRACTED; the seed's item 7 is replaced by Theorem S22.4\]**

---

# §9. The Fate of (Z-A0) and (Z-A1)

## §9.1 What the metric-free limit is

The identification is structural and is offered as a hypothesis with a gate, not as a theorem.

A GP(n,n) carrier whose dual triangles are all *equilateral* is exactly the boundary surface of the regular icosahedron subdivided into 3n² equilateral triangles per face. On such a triangulation the cotangent weight of every edge is (cot 60° \+ cot 60°)/2 \= 1/√3, a **constant**, and the lumped mass is proportional to the vertex degree. That is precisely the FLAT branch of Table 3.1, and the counting branch differs from it by a rank-24 perturbation, which by Theorem S22.2 cannot change the limit — as Table 7.2 confirms (5.555778 against 5.555831).

> **Hypothesis S22.5 (Cone-Metric Identification).** The Class MF limit is the Laplace–Beltrami spectrum of the **flat singular metric on S² with twelve conical singularities of cone angle 5π/3**, i.e. the intrinsic metric of the regular icosahedron's boundary surface. The twelve angle deficits are each π/3 and sum to **Σ δ\_v \= 12 × (π/3) \= 4π \= 2πχ(S²) \= 2π · dim(Z)**, which is the corpus's Spinor–Descartes–Euler identity (Book §8.4i, PROVEN).

**\[STATUS: HYPOTHESIS-strong — supported by (a) the exact equilateral-cotangent argument, (b) the 0.0043 % agreement of two independent carrier families, (c) the SO(3)-breaking-to-I\_h degeneracy pattern of Table 7.3. Gate F-S22.20 fires against it. NOT used to support any other claim in this paper.\]**

A consistency remark that is *derived* rather than observed: Weyl's law fixes the mean level density from the total area alone, so the two classes must share multiplet-averaged eigenvalues to leading order even while individual multiplets split. This is what Table 9.1 shows.

**Table 9.1.** SO(3) multiplet means in Class MF against the round-sphere values. The multiplet mean is nearly preserved; the *splitting within* the multiplet is the physical signal.

| l | I\_h content | Class MF multiplet mean | round value | deviation |
| ----- | ----- | ----- | ----- | ----- |
| 2 | H\_g (5) | 2.990865 | 3 | −0.304 % |
| 3 | T₂u (3) ⊕ G\_u (4) | 6.005922 | 6 | \+0.099 % |
| 4 | H\_g (5) ⊕ G\_g (4) | 10.021978 | 10 | \+0.220 % |

## §9.2 (Z-A1) is a regulator convention

Within Class MF, the orbit weights σ and ρ are free to take any bounded values — including the ZS-S21 metric numbers, including both ψ adversaries — and the limit does not move by more than 0.0207 %. Every observable ZS-S21 registered as branch-discriminating at n \= 1 is therefore, *inside this class*, a finite-carrier effect.

> **Verdict on (Z-A1).** Under refinement, (Z-A1) is **SUPERSEDED-BY-REFINEMENT** for every audited observable. Outcome A fires on the pre-registered class 𝒲\_def. The postulate is unnecessary in the refinement limit, and ZS-S21's characterisation of it as "the single load-bearing choice of the S-line" is, at the level of continuum observables, **incorrect**. **\[STATUS: COMPUTED; gate F-S21.10 is RE-SCOPED to finite carriers\]**

We state this against interest. (Z-A1) was the corpus's most heavily defended postulate in the S-line and this paper removes its continuum content.

## §9.3 (Z-A0) is the load-bearing axiom

What replaces it is the axiom ZS-S21 treated as the easier of the two.

> **Verdict on (Z-A0).** Under refinement, (Z-A0) is **PROMOTED**. Outcome C fires across it: metric-free and metric prescriptions define genuinely different continuum universality classes, separated by 7.993 % in λ₃/λ₁, by 3.92 % in the ZS-S21 discriminator D₁, and — qualitatively and without any precision requirement — by whether the 2l+1 SO(3) degeneracy is restored. **\[STATUS: COMPUTED; gate F-S21.7 remains OPEN and is now the decisive gate of the S-line\]**

Three supporting observations, in the order a sceptical reader will want them.

**(i) Only the metric-free branch is well posed on the carrier the corpus actually postulates.** (Z-A0) supplies incidence data and the I\_h action and nothing else. A metric branch therefore requires an embedding that the axiom does not provide, and different embeddings of the *same* combinatorial carrier give different weights. At n \= 1 the Archimedean realisation ZS-S21 audited gives (σ, ρ) \= (0.8973272361, 1.5100902868), whereas the canonical spherical-Voronoi realisation of the identical carrier gives (0.6157786465, 1.0623043176). Neither is more canonical than the other. Registered as gate F-S22.22.

**(ii) But the metric class nonetheless has an embedding-independent limit.** This is the honest counterweight to (i), and it must be stated. Because circumcentric DEC is consistent on any shape-regular family \[14,15\], every such realisation converges to the *same* round-sphere spectrum. So the metric class is ill-defined at finite n and well-defined in the limit, while the metric-free class is well-defined at every n. The asymmetry is real but it does not favour either side automatically.

**(iii) Gate F-S21.8 is re-attributed, not retired.**

**Table 9.2.** The ZS-S21 discriminator D₁ \= ω(T₂u,1)/ω(T₁u,1) \= √(λ₃/λ₁), at the finite carrier and in the limit.

|  | Class MF | Class M | separation |
| ----- | ----- | ----- | ----- |
| n \= 1 (ZS-S21 v1.2 §6.5) | 1.9742883436 | 2.2042305068 / 2.2154919435 | 11.65 % / 12.21 % |
| n → ∞ (this paper) | **2.357110** | **2.449497** (= √6) | **3.92 %** |

The gate survives regulator removal with a reduced but non-vanishing separation, and its decision threshold in the limit is the midpoint 2.403304. What changes is what it tests: at n \= 1 ZS-S21 read it as orbit-blind versus orbit-sensitive; in the limit it reads as metric-free versus metric. **\[STATUS: RE-ATTRIBUTED — declaration D078\]**

## §9.4 The zero-parameter falsifiable table

**Table 9.3.** The physical excitation ratios ω\_k/ω₁ \= √(λ\_k/λ₁) of the two classes in the refinement limit. Both columns are parameter-free once the class is chosen. This is the falsifiable content of ZS-S22.

| level | mult | I\_h isotype | Class MF (Z-Spin, metric-free) | Class M (metric / round) |
| ----- | ----- | ----- | ----- | ----- |
| 1 | 3 | T₁u | 1.000000 | 1.000000 |
| 2 | 5 | H\_g | 1.729412 | 1.732051 |
| 3 | 3 | T₂u | **2.357081** | 2.449497 |
| 4 | 4 | G\_u | **2.518629** | 2.449481 |
| 5 | 5 | H\_g | **3.096596** | 3.162270 |
| 6 | 4 | G\_g | **3.250126** | 3.162270 |
| 7 | 3 | T₁u | 3.723196 | 3.872990 |

**\[STATUS: TESTABLE — the level-3/level-4 splitting is the sharpest entry: 13.239 % in Class MF against 0 in Class M\]**

*Note on the two Class MF figures quoted in this paper.* Table 9.3 is computed from the **counting branch** limits of Table 7.3 (λ₃/λ₁ \= 5.555831, hence ω₃/ω₁ \= 2.357081). Table 9.2 quotes the **five-branch class mean** (5.555969, hence 2.357110). The two differ in the fifth decimal, which is the size of the class spread (0.0207 %) and is itself the honest uncertainty on the class limit. Neither figure is quoted to more precision than that spread warrants elsewhere in the paper.

---

# §10. The Group-Valued Tier — Out of Scope (executed in ZS-S23 v1.0 and ZS-S24 v1.0)

Everything above concerns the **quadratic** transfer-matrix output. To claim Yang–Mills universality rather than Hodge-spectrum universality requires a group-valued audit, and this paper does not perform one.

- **Tier G1 (compact U(1) on K\_n × ℤ\_{N\_t}):** plaquette expectation, Wilson loops enclosing zero, one and several pentagons, bulk and defect correlation lengths, with the five pre-registered branches. **NOT EXECUTED. \[STATUS: OPEN\]**  
- **Tier G2 (SU(2) heat-bath, n ≤ 4):** tests whether the two-class pattern survives non-Abelian compact dynamics. **NOT EXECUTED. \[STATUS: OPEN\]**  
- **Tier G3 (SU(3)):** **\[STATUS: OPEN\]** — the incidence and defect-support theorems are gauge-group independent, but survival of the class split under full non-Abelian dynamics is not established. Gate F-S22.17 forbids presenting any U(1) or SU(2) result as SU(3) verification.

The finite-rank theorem does suggest a sharper group-valued statement worth pre-registering now: loops whose support stays a fixed graph distance from every pentagon should become class-insensitive only if the *bulk* is class-insensitive, which §8.2 shows it is not. We therefore predict, in advance, that the group-valued audit will find the class split in **bulk** loops rather than in defect-linking loops — the reverse of the seed's expectation. Gate F-S22.16 is registered against this prediction.

**Do not call the quadratic theorem a continuum Yang–Mills theorem.** Dang and Nohra \[10\] prove universality of two-dimensional Yang–Mills measures for broad lattice actions on compact surfaces; that result is the methodological ceiling for what a complete universality paper looks like, and it is not an imported proof for K\_n × a\_tℤ. \[STATUS: NON-CLAIM\]

---

# §11. Comparison with External Universality Programmes

**Table 11.1.** External results, the exact role each plays here, and the exact difference in scope.

| Result | Reference | Role in ZS-S22 | Difference in scope |
| ----- | ----- | ----- | ----- |
| Goldberg / icosahedral fullerene construction | \[1\], \[2\] | Defines GP(n,n) and the symmetry-preserving refinement architecture. | Combinatorics only; no spectral content. |
| Lattice Hamiltonian | \[3\] | Imported ZS-S21 instrument, not re-proved. | Hypercubic; congruent cells. |
| Positive transfer matrix | \[4\] | Positivity and existence of H under the Wilson hypotheses. | Independent of the spatial complex. |
| Irregular-lattice plaquette weights | \[5\], \[6\] | Defines the metric adversarial branch (Class M). | Their weights are a prescription, not a theorem about which is right. |
| Simplicial gauge consistency | \[7\], \[8\] | Benchmark for gauge-invariant discrete actions and approximation-theoretic consistency. | Approximation of a *given* smooth theory; ZS-S22 asks which smooth theory is being approximated. |
| 2D discrete-to-continuum YM | \[11\], \[12\] | Rigorous template for holonomy measures on surfaces. | Group-valued, 2D, smooth surface; not the 2+1 quadratic instrument. |
| Universal scaling limit of 2D lattice YM | \[10\] | **Methodological ceiling only.** Defines what a complete universality paper looks like. | Their universality is *across actions on one surface*. ZS-S22's non-universality is *across two surfaces*. These are compatible, not contradictory. |
| Rank inequality | \[9\] | Converts Theorem S22.2 into Corollary S22.2a. | Worst-case; never tight here. |
| Spectral-subspace perturbation | \[13\] | Would control isotype rotation; **used only where a gap is certified**, and no Davis–Kahan claim is made in v1.0. | — |
| DEC / FEEC consistency | \[14\], \[15\] | Supplies the Class M identification as IMPORTED-PROVEN. | Requires a metric; therefore inapplicable under (Z-A0). |

The single most important scope statement: **\[10\] is not cited as proving anything about ZS-S22.** Their theorem says that many lattice actions on a fixed smooth surface flow to one continuum measure. Theorem S22.4 says that two prescriptions on a fixed *combinatorial* family flow to two different surfaces. Both can be true at once, and §9.1 explains why: the metric-free prescription never had a smooth surface to converge to.

---

# §12. Anti-Numerology and Zero-Parameter Audit

## §12.1 Zero free parameters

ZS-S22 introduces **no constant, no fitted variable and no fudge factor**. The audit, carried out per §3.1 of the corpus protocol:

- **A \= 35/437, Q \= 11, dim Z \= 2** are declared in the companion header and used **nowhere** in any derivation. They appear only in the LOCKED banner and in the §4 regression banner. Removing them changes no computed number in this paper.  
- **λ₁ \= 1.2428416164, λ\_h \= 7.5210904061** are used **only** as regression targets in §4 and are reproduced, not fitted (deviations 1.49 × 10⁻¹¹ and 1.47 × 10⁻¹¹).  
- **n** is a regulator index sent to infinity, never a fitted parameter (declaration R-IDX).  
- **σ, ρ** are not parameters of ZS-S22; they are the objects whose relevance is being tested, and the theorems are proved for the whole class 𝒲\_def(c,C).  
- The class limits of Table 7.3 are outputs of a pre-registered extrapolation whose form (L \+ a/n² \+ b/n⁴) was fixed in advance and whose exponent was then *measured* to be 2.008.

## §12.2 The integers that appear, and where they come from

- **12** pentagons — fullerene topology, forced by Euler's formula.  
- **60** defect edges — 12 × 5 with isolated pentagons.  
- **72** — the closed neighbourhood 12 \+ 60 \= 12 × (1 \+ 5). Derived in the proof of Theorem S22.2, not matched.  
- **O(n⁻²)** — exact counts.

**None of these may be linked to Q, G \= 12, A or dim Z without a separate theorem.** In particular: 12 pentagons is **not** read as Q \+ 1; 60 defect edges is **not** read as a particle count; and 72 is **not** read as a register invariant. The pre-registered Monte-Carlo null over the locked corpus integer pool {2, 3, 5, 6, 11, 12, 19, 23, 35, 120, 437} with 200 000 draws returns **p \= 0.0277** for hitting 72 by a simple two- or three-term combination — low, but the point is moot, because 72 is *derived* and not matched. Declaration D121 firewalls it. \[STATUS: check T120, declaration D121\]

## §12.3 The one proximity, disclosed and denied

The Class MF limit λ₃/λ₁ extrapolates to **5.555969**, and 50/9 \= 5.555556, a deviation of **0.0074 %**. The null "a random p/q with p, q ≤ 60 lands within 0.02 % of this value" returns **p \= 0.00032** on 200 000 draws.

We nevertheless register this as **OBSERVATION with no evidential weight**, for a reason that is decisive and has nothing to do with the p-value: **the extrapolation uncertainty is of the same order as the deviation.** The held-out residual at n \= 12 is 4 × 10⁻⁵ absolute, and the spread across the five Class MF branches is 0.0207 %, which is three times the claimed proximity. The quantity is therefore not determined precisely enough for the comparison to mean anything yet, and it is used nowhere in this paper.

Gate **F-S22.21** pre-registers the tighter test: extend to n ≤ 20 with Richardson extrapolation and a certified sparse eigensolver, and either exclude 50/9 or exhibit a theorem for it. Until then no connecting statement is made. \[STATUS: OBSERVATION; declaration D122\]

## §12.4 What is explicitly not used as evidence

The near-preservation of SO(3) multiplet means in Table 9.1 is **derived** from Weyl's law, not observed, and is not offered as evidence for Hypothesis S22.5. The agreement of the class-I and class-II families to 0.0043 % is a proxy consistency test, not a proof of the cone-metric identification. And the fact that σ \= ρ \= 1 returns the LOCKED λ₁ at n \= 1 is, exactly as ZS-S21 §13 insisted, a consistency check between two computations and **not** evidence for (Z-A1) — a denial that this paper's §9.2 makes moot in any case.

---

# §13. Cross-Paper Dependency Audit

Per §3.2 of the corpus protocol, the effect of ZS-S22 on every paper that could inherit from it.

**Table 13.1.** Dependency and version-collision audit. "Moves?" asks whether any ledger number of that paper changes.

| Upstream / downstream paper | What it supplies or inherits | Moves? | Note |
| ----- | ----- | :---: | ----- |
| **ZS-M1** (i-tetration fixed point z\*) | z\*, x\* | **NO** | ZS-S22 uses no tetration quantity. No propagation path exists. |
| **ZS-F2 / ZS-F9R** (A \= 35/437) | A from polyhedral curvature asymmetry | **NO** | A is not used. §9.1 touches the same *geometric* motif (concentrated curvature) but derives nothing from A and asserts no link. |
| **ZS-F5 / ZS-M19** (Q \= 11, (Z,X,Y) \= (2,3,6)) | register structure | **NO** | Not used. Firewalled in §12.2. |
| **ZS-S1** (α\_s \= 11/93, sin²θ\_W) | gauge couplings | **NO** | ZS-S22 makes no coupling claim. |
| **ZS-S7** (Λ\_QCD, m(0⁺⁺), λ₁) | λ₁ \= 1.2428416164 | **NO** | Reproduced exactly at n \= 1 (§4). ZS-S22 does not claim λ₁ survives refinement — under Theorem S22.4 it does not, and §14.3 says what that means. |
| **ZS-S14** (master action) | the group-valued action being reduced | **NO** | (H-W) unchanged; ZS-S22 does not exhibit the reduction. |
| **ZS-S17 / ZS-S18** (λ\_h, glueball vertex) | λ\_h \= 7.5210904061 | **NO** | Reproduced exactly at n \= 1 (§4). |
| **ZS-S19 / ZS-S20** (R\_C, non-identifiability) | the counting axiom and its negative theorems | **NO** | Imported unchanged; ZS-S22 re-scopes their conclusion to finite carriers, which is a status change, not a numerical one. |
| **ZS-S21** (the instrument) | (H-W), (Z-A0), (Z-A1), Table 6.2 | **NO** | All three branch spectra reproduced to ≤ 1.03 × 10⁻¹⁰. Gate F-S21.8 re-attributed; gate F-S21.10 re-scoped. **ZS-S21 is not superseded.** |
| **ZS-U1** (inflation r, n\_s) | — | **NO** | No path. |
| **ZS-A1** (galactic scale) | — | **NO** | No path. |

**No ledger number in the corpus moves.** \[STATUS: VERIFIED — declaration NC-S22.4\]

**External-data audit (§3.3 of the protocol).** ZS-S22 makes no claim contacting Planck 2018 ΛCDM parameters, the PDG gauge couplings, or any measured glueball mass. Its only externally-facing prediction is Table 9.3, which concerns a dimensionless excitation-ratio pattern of a cellular instrument and is currently untested by any experiment. Therefore **no conflict with existing observational data is possible, and none is claimed.** The absence of such contact is a limitation, not a success, and is recorded as NC-S22.2.

---

# §14. Gate Registry, Retraction Register, Non-Claims

## §14.1 Falsification gates

Multi-layer, per §3.5 of the protocol: **M** \= mathematical / theoretical collapse (immediate rejection); **S** \= simulation / internal-consistency collapse (revision required); **O** \= observational collapse (external data).

**Table 14.1.** ZS-S22 gate registry.

| Gate | Condition that fires it | Layer | Status |
| ----- | ----- | :---: | ----- |
| F-S22.1 | K₁ is not exactly isomorphic to the ZS-S21 truncated icosahedron, including orbit labels | M | Does not fire (T030–T032) |
| F-S22.2 | a generated K\_n violates (60n², 90n², 30n²+2) | M | Does not fire (T010) |
| F-S22.3 | the sequence lacks exactly 12 pentagons and 60 (5,6) edges | M | Does not fire (T011–T013) |
| F-S22.4 | B₂B₂ᵀ is not the dual graph Laplacian | M | Does not fire (T020) |
| F-S22.5 | rank\[Δ\_n(σ,ρ) − Δ\_n(1,1)\] \> 72 for some n ≥ 2 | M | Does not fire (T040–T044) |
| F-S22.6 | the ESD Kolmogorov distance exceeds 72/F\_n | M | Does not fire (T050) |
| F-S22.7 | a branch claim depends on branch-specific full-rank rescaling | S | Does not fire (§3.3 firewall) |
| F-S22.10 | the pre-registered 1/n² extrapolation fails the held-out test at n \= 12 | S | Does not fire (T070, all six branches SUPPORTED) |
| F-S22.13 | two independent constructors give non-isomorphic complexes | S | **OPEN / NOT EXECUTED (v1.5).** Versions 1.0–1.4 recorded this closed on the strength of the class-I / class-II spectral agreement of 0.0043 % (P081). Those are different tests: comparing two GC *families* by a spectral proxy is not comparing two independent *constructors* of the same complex, and the companion contains one Goldberg constructor. **Retraction S22-R8** |
| **F-S22.20 (NEW, decisive)** | the Class MF limit is found to restore the full 2l+1 degeneracy, i.e. to equal the round sphere | M | **OPEN** — this is the gate on Hypothesis S22.5 and on the entire two-class claim |
| **F-S22.21 (NEW)** | a tighter extrapolation excludes λ₃/λ₁ \= 50/9, or establishes it exactly without a theorem | S | **OPEN** — see §12.3 |
| **F-S22.22 (NEW)** | an embedding-independent canonical metric branch is exhibited at finite n, contradicting the layer-ambiguity disclosure | M | **OPEN** — see §9.3(i) |
| F-S22.16 | the group-valued audit finds the class split in defect-linking loops rather than bulk loops | S | **OPEN** — pre-registered prediction, §10 |
| F-S22.17 | any U(1) or SU(2) result is presented as SU(3) verification | M | **OPEN** — registered against future papers |
| F-S22.18 | a 2-surface or 2+1-dimensional result is called a proof of 3+1 Clay-form Yang–Mills | M | **OPEN** — registered against future papers |
| F-S22.19 | bulk ESD universality is reported as low-mode universality | M | **OPEN** — registered against future papers |
| F-S21.7 (inherited) | (Z-A0) is contradicted: ZS-S14 supplies K with a metric or dual measure | M | **OPEN — now the decisive gate of the S-line** (§9.3) |
| F-S21.8 (inherited) | D₁ measured above the branch midpoint, or the third excitation found with multiplicity 4 | O | **OPEN — RE-ATTRIBUTED** to (Z-A0); limit threshold 2.403304 (§9.3 iii) |
| F-S21.10 (inherited) | (Z-A1) is contradicted by an orbit-sensitive reduction | M | **OPEN — RE-SCOPED to finite carriers** (§9.2) |
| F-S21.11 (inherited) | (H-W) is contradicted | M | **OPEN — unchanged**; everything here still rests on it |
| F-S21.12 (inherited) | the transfer matrix is shown to *select* rather than propagate an orbit weight | M | Does not fire; ZS-S22 attributes no selection to the construction |
| **F-S22.23 (NEW v1.1)** | a chiral Goldberg carrier GP(h,k) with 0 \< k \< h is exhibited that satisfies (C1)–(C3), contradicting Theorem S22.10 | M | **OPEN** — excluded analytically by |V| \= 20T \> 120 for T \= 7; the constructor is audited only for achiral families |
| **F-S22.24 (NEW v1.1)** | a paper asserts carrier selection from mediation saturation alone, without (C3) | M | **OPEN** — GP(2,0) also saturates (§16.3) |
| **F-S22.25 (NEW v1.1)** | (Z-A2) mediation saturation is contradicted: a ZS-S14 face outside N\[P\] at n \= 2 is shown to receive a non-zero leading-order Z–Y coupling | M | **OPEN** — this immediately kills the carrier-selection route |
| **F-S22.26** | the Step-A holonomy reduction yields a metric-dependent Φ\_p, i.e. Class M | M | **MOVED to ZS-S23.** v1.2's "FIRED" verdict is RETRACTED (S22-R6): under conformal freedom the reduction does not force Class M |
| **F-S22.27 (NEW v1.2)** | a globally supported bounded Layer-C branch is exhibited that shares the Class MF limit, showing O(1) support is not necessary | S | **OPEN** — only sufficiency is proved in §16.2 |
| **F-S22.28 (NEW v1.2)** | a fixed-k low mode is found without a uniform L^∞ or gradient bound, invalidating the Theorem S22.4a proof sketch | M | **OPEN** — ℒ₅ measures only one of the four required conditions |
| **F-S22.29 (NEW v1.2)** | the implemented S L\_w S operator is shown not to satisfy the hypotheses of the DEC/FEEC consistency theorems | M | **OPEN** — the hypothesis-matching audit for Theorem S22.4b is not carried out |
| F-S22.11 | ordinal and multiplicity matching disagree | S | **CLOSED in v1.1** by explicit character projectors (§16.1) |

## §14.2 Retraction register

ZS-S22 inherits the ten ZS-S20 retractions and the three ZS-S21 retractions unchanged, and adds **eight** of its own: S22-R1, S22-R2 and S22-R3 against its own seed, S22-R4 in v1.1 against v1.0, S22-R5 in v1.2 against v1.1, S22-R6 in v1.3 against v1.2, S22-R7 in v1.4 against v1.3, and S22-R8 in v1.5 against the whole prior gate registry. Every one was issued before the corresponding result was used.

- **Retraction S22-R1 (§5.3).** The seeded rank bound 84 \= 12 \+ 60 \+ 12 is true but not sharp; it double-counts the 12 pentagon directions. Replaced by the support statement with the sharp constant 72\.  
- **Retraction S22-R2 (§6.1).** The seeded branch table placed the metric branches S-DEC and P-DEC inside the two-orbit class 𝒲\_def(c,C). False for n ≥ 2: they carry 30n²-dimensional weight fields with O(1) bulk variation.  
- **Retraction S22-R3 (§8.2).** The seeded preferred Outcome B — a surviving defect-localized low sector — is refuted. No low mode is defect-localized, and the branch-sensitive modes are extremal.  
- **Retraction S22-R8 (v1.5, against v1.0–v1.4, gate registry).** Gate F-S22.13 — "two independent constructors give non-isomorphic complexes" — was recorded as not firing, on the evidence of the class-I / class-II spectral agreement. That evidence tests a different proposition. The gate is restored to **OPEN / NOT EXECUTED**. This is the fourth instance in this paper's history of one test being credited against a different claim, and it is recorded rather than quietly re-scoped.  
- **Retraction S22-R7 (v1.4, against v1.3 §16.2).** Version 1.3's status line for Theorem S22.9 — "PROVEN for the sufficiency direction" and "the necessity direction is COMPUTED" — is RETRACTED on both halves. Sufficiency inherits the conditionality of Theorem S22.4a and is **DERIVED-CONDITIONAL**. The three escaping adversaries refute broader Layer-C universality but establish **nothing** about necessity, which stays OPEN under gate F-S22.27. This is the third time in this paper's history that a property verified on the members of a class has been written as a characterisation of the class; the pattern is recorded rather than quietly narrowed.  
- **Retraction S22-R6 (v1.3, against v1.2 §18).** Version 1.2's Step-A verdict — "the geometric route fires Outcome B; (Z-A1) is not recoverable from any I\_h spherical geometry" — and its supporting assertion that the I\_h-invariant conformal structure is unique are both RETRACTED. The round-metric no-go survives and is now ZS-S23 Theorem S23.1; the verdict drawn from it does not. ZS-S23 Theorem S23.2 reaches (σ, ρ) \= (1,1) exactly under an I\_h-invariant conformal factor, for two distinct profiles. Corrected verdict: metric **non-identifiability**, not selection.  
- **Retraction S22-R5 (§16.2 title, §7.3 statuses, §0.2, v1.2 against v1.1).** Version 1.1's title "the exact boundary of the metric-free class" is RETRACTED: only sufficiency plus counterexamples is established, not necessity (gate F-S22.27). Version 1.1's status "DERIVED-CONDITIONAL on delocalization, which is VERIFIED by the ℒ₅ witness" is RETRACTED as too strong — ℒ₅ measures only one of four required conditions (gate F-S22.28). Version 1.1's flat "IMPORTED-PROVEN" for Theorem S22.4b is RETRACTED in favour of "IMPORTED-PROVEN theorem \+ DERIVED-CONDITIONAL application \+ VERIFIED numerically", since no hypothesis-matching audit was carried out (gate F-S22.29). Version 1.1's §0.2 claim that ZS-S22 introduces no new hypothesis is RETRACTED: (Z-A2) and (Z-A3) are new named axioms.  
- **Retraction S22-R4 (§16.2, v1.1 against v1.0 of this paper).** Version 1.0's characterisation of the metric-free class as "every branch whose weights are functions of Layer-C data alone" is RETRACTED as too broad. Three bounded Layer-C adversaries escape, including a decaying one. The class is uniformly bounded **and** finite-defect-supported. Version 1.0's uniform "Theorem S22.4" heading over an admittedly COMPUTED result, its claim that the metric weight count "grows without bound", and its phrase "carrier-family independent" are likewise corrected in §7.3, §6.1 and §7.5.

The shape of R2 is worth naming, because it is the shape the corpus has now recorded fourteen times: a property verified on one carrier (two orbits on K\_TI) assumed to persist on a family where it does not. K₁ is the *only* member of the family on which a metric prescription is a two-parameter object, precisely because K₁ is entirely defect.

## §14.3 Non-claims

- **NC-S22.1.** ZS-S22 does NOT prove existence of a continuum Yang–Mills measure on K\_n × a\_tℤ.  
- **NC-S22.2.** ZS-S22 does NOT establish an SU(3) mass gap and makes no 3+1-dimensional Clay-form claim. It contacts no measured quantity.  
- **NC-S22.3.** ZS-S22 does NOT derive (H-W), (Z-A0) or (Z-A1) from the ZS-S14 action. It determines their fate under refinement, which is a different and lesser thing.  
- **NC-S22.4.** ZS-S22 moves no corpus ledger number. λ₁ and λ\_h are unchanged at n \= 1\.  
- **NC-S22.5.** ZS-S22 does NOT claim that the physical Z-Spin carrier is the n → ∞ limit. **Carrier selection is OPEN** and is discussed in §15.3.  
- **NC-S22.6.** All class limits are COMPUTED extrapolations, not PROVEN eigenvalues of a limit operator. No limit operator is constructed in v1.0.  
- **NC-S22.7.** Hypothesis S22.5 is not used to support any other statement in this paper, and removing it changes nothing else.  
- **NC-S22.8 (v1.3).** ZS-S22 makes **no** claim about the Yang–Mills mass gap in any form. All spectral-gap statements live in ZS-S24 v1.0 and are finite-carrier statements there.  
- **NC-S22.9 (v1.3).** ZS-S22 does **not** decide which universality class the physical theory occupies. It measures the classes and their discriminator; the decision is attempted, conditionally, in ZS-S23 §4.  
- **NC-S22.10 (v1.3).** No result of ZS-S22 v1.3 depends on ZS-S23 or ZS-S24. Where those papers are cited here it is as a *reading*, never as a premise.

---

# §15. Conclusion

## §15.1 What was shown

ZS-S21 reduced the Hodge-measure question to two numbers and could not select them. ZS-S22 embedded its carrier in the canonical Goldberg–Coxeter family and asked whether those two numbers matter after the regulator is removed. Four things follow.

First, the orbit-weight perturbation is not merely finite rank but **finitely supported**, on the 72-dimensional closed neighbourhood of the twelve defects, for every n. The seeded bound 84 is replaced by the sharp constant 72 and by a locality statement that is stronger in kind.

Second, bulk spectral universality follows exactly, with sup\_x |ΔF| ≤ 72/(30n²+2).

Third, and against the seed's expectation, the finite defect sector produces **no** low-energy branch separation. The low modes are delocalized; the modes the defect block moves are extremal.

Fourth, and this is the result: the refinement limit is **not one limit**. Every audited uniformly bounded, finite-defect-supported prescription converges to one operator; every shape-regular metric prescription converges to a different one. The qualifier matters and is not decorative: §16.2 exhibits bounded Layer-C prescriptions, including a *decaying* one, that converge to neither. The separation does not decay, the discriminator is a symmetry statement rather than a number, and the identification of the metric-free limit as a flat metric with twelve π/3 cone deficits summing to 4π \= 2π·dim(**Z**) is offered as a hypothesis with a gate on it.

## §15.2 The verdict, stated symmetrically

Over-claiming and under-claiming are the same failure. Both halves are said here and neither is softened.

> **ZS-S22 verdict.** Under Goldberg–Coxeter refinement of the ZS-S21 cellular instrument, the orbit-blind postulate **(Z-A1) is SUPERSEDED-BY-REFINEMENT**: it is a finite-carrier convention with no effect on any audited continuum observable. The metric-free carrier axiom **(Z-A0) is PROMOTED** to the sole load-bearing branch choice of the S-line: metric-free and metric prescriptions define inequivalent continuum universality classes, separated qualitatively by SO(3) degeneracy restoration and quantitatively by 7.993 % in λ₃/λ₁ and 3.92 % in D₁. Gate F-S21.8 survives and is **RE-ATTRIBUTED** from (Z-A1) to (Z-A0). The exact theorems are Theorem S22.1 (census, PROVEN), Lemma S22.0 (dual reduction, PROVEN), Theorem S22.2 (defect support with sharp constant 72, PROVEN), Corollary S22.2a (bulk ESD universality, PROVEN-CONDITIONAL) and Theorem S22.3 (the metric class is not finite-defect, PROVEN). Theorem S22.4 is **COMPUTED** with a held-out protocol passed by all six branches, and is not a theorem. The group-valued tier is **OPEN**. No continuum Yang–Mills, SU(3), or 3+1-dimensional claim is made.

What this verdict does **not** license, spelled out so no later paper can borrow it: it does not license calling the Yang–Mills bridge closed; it does not license treating Table 9.3 as a measured prediction, since nothing has measured it; it does not license reading the twelve cone deficits as a derivation of **A** or of **Q**; and it does not license asserting Theorem S22.4 as PROVEN, because no limit operator was constructed.

What it does license, equally plainly: reporting that a heavily defended corpus postulate has been shown to be a regulator convention is not a defeat, and declining to state that result to protect (Z-A1) would have been the failure.

## §15.3 The one sentence on what remains impossible, and the question this paper creates

After refinement, no observable in the audited class distinguishes orbit-blind from orbit-sensitive weighting, so (Z-A1) cannot be tested even in principle in the continuum; it can only be tested at finite carrier size, which means it can only be tested if the carrier size is itself physical.

And that is the question ZS-S22 creates rather than answers. The corpus does not treat K\_TI as a regulator. It treats it as a Planck-scale physical object: Q \= 11, |I\_h| \= Q² − 1 \= 120, **A** \= 35/437 from polyhedral curvature asymmetry, and λ₁, λ\_h as locked physical numbers all use K\_TI-specific data. Under that reading, Theorem S22.4 says something uncomfortable and important: **the physical content of Z-Spin cellular Yang–Mills is precisely the part that does not survive refinement.** The n \= 1 spectrum of Table 4.1 and the n → ∞ spectrum of Table 9.3 are different theories, and the corpus has been using the first.

There are exactly two honest ways forward, and the next paper must choose one rather than blur them.

**(a) The carrier is a regulator.** Then Table 9.3 is the physics, λ₁ \= 1.2428416164 is a lattice artefact, and every downstream number that used it must be re-derived in the limit. This is a large and destructive programme and should not be entered casually.

**(b) The carrier is physical and n \= 1 is selected.** Then a **carrier-selection theorem** is required: something that forces GP(1,1) and forbids GP(n,n) for n ≥ 2\. ZS-S22 makes this gap visible for the first time by exhibiting the family that the selection must exclude, and §5.3 supplies the first structural hint — K₁ is the unique member for which N\[P\] exhausts the carrier, i.e. the unique member that is *entirely defect*. Whether that is a selection principle or a coincidence is not decided here.

**Version 1.1 supplies a conditional combinatorial route toward (b); it does not settle (b) outright.** Theorem S22.10 of §16.3 shows that under (C1) isolated pentagons, (C2) mediation saturation — a **named axiom (Z-A2), not derived from ZS-S14** — and (C3) vertex-transitivity — also **not derived**, and load-bearing, since GP(2,0) satisfies (C1) ∧ (C2) — the Goldberg family selects **GP(1,1) \= K\_TI uniquely** — with the honest caveat that saturation alone does *not* suffice, since GP(2,0) also saturates. Route (a) is therefore not forced: λ₁ \= 1.2428416164 is not shown to be a lattice artefact, because the lattice is not a lattice. The refinement family is a diagnostic instrument, and Table 9.3 is the control experiment that identifies the class, not the prediction.

What remains is not an open-ended continuum programme but **three finite-carrier steps**, set out in §17.2: **(A)** derive (H-W) by exact Whitney holonomy reduction of ZS-S14 on K\_TI × a\_tℤ, which simultaneously decides F-S21.7, F-S21.10 and F-S21.11; **(B)** re-attribute Δ\_{S21} as the identity-neighbourhood Hessian of the resulting group-valued action, which is what would license reading λ₁ as anything physical; and **(C)** construct the SU(3) transfer matrix on the finite physical carrier and bound its spectral gap above and below. None of the three is the Clay problem, and none is claimed to be.

**Version 1.5 is TERMINAL at this scope.** The action-to-Hessian bridge is **ZS-S23 v1.0** and the finite-carrier SU(3) gap is **ZS-S24 v1.0**. What ZS-S22 establishes and hands forward is exactly this, with each clause carrying its own grade.

- The refinement family supports **two inequivalent candidate limits**, separated by 7.993 % with no decay, and the discriminator between them is qualitative and gauge-group independent. The existence of the Class-MF limit operator is **Conjecture S22.4c**; no limit operator is constructed.  
- Uniform boundedness **plus O(1) support** is a **sufficient** condition for membership of the audited metric-free class. **Necessity is OPEN**, gate F-S22.27. Layer-C computability is *not* sufficient, since even a *decaying* Layer-C halo escapes.  
- The metric branch's escape is split by grade: growing orbit complexity is **PROVEN** (S22.3(a)); the escape of the implemented DEC branch is **COMPUTED over n ≤ 8** (S22.3(b)).  
- Every isotype label in the S-line is **certified** by explicit I\_h character projectors (S22.8), and the |Aut| ≤ 120 step of the carrier theorem is now discharged by proof and by an embedding-free automorphism count (Lemma S22.10a).  
- **Conditional on (C1), (Z-A2) and (C3)**, Theorem S22.10 uniquely selects K\_TI \= GP(1,1), with the near-miss GP(2,0) recorded because saturation alone does not select. **Unconditional physical carrier selection remains OPEN.** Only under those conditions is the refinement family a **diagnostic instrument** rather than a limit the physical theory must be taken to.

**What ZS-S22 does not decide.** Which class the physical theory occupies. Version 1.2 believed it had settled this negatively on geometric grounds and was wrong (Retraction S22-R6). The corrected position is that the geometric route under-determines, so the decision rests on the dynamical route and is taken up, conditionally and with its own unresolved density-versus-rate objection, in ZS-S23 §4.

**ZS-S22 v1.5 is complete at this scope, and TERMINAL.** There is no further refinement calculation to perform on the quadratic instrument. The one computation that would move the S-line — the explicit integration of the ZS-S14 curvature term over the 32 faces and 90 temporal prisms of K\_TI × a\_tℤ — belongs to **ZS-S23 v1.0**, where it is gate F-S23.6, and is not this paper's to perform. Restating the present result in new language would be the seventeenth instance of a pattern this corpus has now recorded sixteen times.

---

# §16. Certified Symmetry Bookkeeping, the Class Boundary, and Carrier Selection

## §16.1 Theorem S22.8 — I\_h isotypes, certified rather than inferred

Version 1.0 assigned I\_h labels from multiplicity plus continuity in (σ, ρ), validated against ZS-S21's independently computed n \= 1 labels, and registered the absence of character projectors as OPEN. That gap is now closed.

The 120 elements of **I\_h** are constructed as the orthogonal 3 × 3 maps preserving the icosahedron vertex set. Writing **I\_h ≅ I × ℤ₂**, every g decomposes as g \= ε·r with ε \= det g and r ∈ I, so χ\_{Xg}(g) \= χ\_X(r) and χ\_{Xu}(g) \= ε·χ\_X(r). The character orthogonality residual of the resulting table is 2.2 × 10⁻¹⁶. The projectors are

*P\_α \= (d\_α / |I\_h|) Σ\_{g ∈ I\_h} χ\_α(g) U\_n(g)*\*,  |I\_h| \= 120\.

**Table 16.1.** Projector audit on Ω²(K\_n). All three audits are at machine precision.

| n | F\_n | idempotence ‖P²−P‖ | orthogonality max‖P\_αP\_β‖ | dimension-sum residual | isotype residual |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 1 | 32 | 1.7 × 10⁻¹⁶ | 3.3 × 10⁻¹⁷ | 0 | 7.6 × 10⁻¹⁵ |
| 2 | 122 | 1.7 × 10⁻¹⁶ | 3.3 × 10⁻¹⁷ | 0 | 6.2 × 10⁻¹⁵ |
| 3 | 272 | 1.7 × 10⁻¹⁶ | 3.3 × 10⁻¹⁷ | 0 | 1.2 × 10⁻¹⁴ |
| 4 | 482 | 2.8 × 10⁻¹⁶ | 3.5 × 10⁻¹⁷ | 0 | 2.2 × 10⁻¹⁴ |

**Table 16.2.** Certified isotypic decompositions.

| n | Ω²(K\_n) |
| ----- | ----- |
| 1 | 2A\_g ⊕ 2T₁u ⊕ 2T₂u ⊕ 2H\_g ⊕ G\_g ⊕ G\_u |
| 2 | 4A\_g ⊕ T₁g ⊕ 5T₁u ⊕ T₂g ⊕ 5T₂u ⊕ 4G\_g ⊕ 4G\_u ⊕ 7H\_g ⊕ 3H\_u |
| 3 | 6A\_g ⊕ 4T₁g ⊕ 10T₁u ⊕ 4T₂g ⊕ 10T₂u ⊕ 9G\_g ⊕ 9G\_u ⊕ 14H\_g ⊕ 8H\_u |
| 4 | 9A\_g ⊕ A\_u ⊕ 8T₁g ⊕ 16T₁u ⊕ 8T₂g ⊕ 16T₂u ⊕ 16G\_g ⊕ 16G\_u ⊕ 24H\_g ⊕ 16H\_u |

The n \= 1 row reproduces **ZS-S21 erratum E-1a exactly** — six irreps occur, not ten, with multiplicities 2, 2, 2, 2, 1, 1 — from an independent construction, and the low-level labels T₁u, H\_g, T₂u, G\_u, H\_g, T₁u reproduce ZS-S21 Table 9.1 exactly. Every isotype statement in §7 and §9 is therefore group-theoretically certified. **\[STATUS: PROVEN \+ VERIFIED — checks T130–T137; gate F-S22.11 CLOSED\]**

## §16.2 Theorem S22.9 — a sufficient finite-defect class, and counterexamples

Version 1.0 §7.3(i) wrote "every branch whose weights are functions of Layer-C data alone converges to a common limit". This is **false and is retracted**. The claim was tested rather than defended.

Three global Layer-C adversaries were pre-registered. Each is uniformly bounded, each uses only the combinatorial datum d(f, P) \= graph distance to the nearest pentagon, and none uses any metric.

**Table 16.3.** The class boundary, measured. Class MF reference λ₃/λ₁ \= 5.555969; Class M \= 6.000033.

| adversary | character | support | extrapolated λ₃/λ₁ | distance from Class MF | verdict |
| ----- | ----- | ----- | ----- | ----- | :---: |
| 1 \+ 0.8/(1+d) | Layer-C, bounded, **decaying** | all cells, decaying tail | 5.629673 | 0.0737 | **ESCAPES** |
| 1 \+ 0.8·d/D | Layer-C, bounded, O(1) in the bulk | all cells | 5.176935 | 0.3790 | **ESCAPES** |
| 1 \+ 0.4·(d mod 2\) | Layer-C, bounded, non-decaying | all cells | 5.512425 | 0.0435 | **ESCAPES** |

The first row is the decisive one. A weight that **decays** with distance from the defects still escapes the class, because the number of cells at distance d grows linearly in d, so a 1/d weight carries O(n) total deviation rather than O(1).

> **Theorem S22.9 (A Sufficient Finite-Defect Universality Class, and Counterexamples to Layer-C Universality).** *Version 1.2 renames this from "the exact boundary": only sufficiency is proved, together with counterexamples. Necessity — that a common limit forces O(1) support — is NOT proved, and a sufficiently fast n-dependent amplitude decay or a gauge-equivalent deformation could in principle share the limit while being globally supported. Registered as gate F-S22.27.* The metric-free universality class is **not** the class of Layer-C branches. Uniform boundedness **together with support on O(1) cells** is **sufficient** for membership — precisely the hypothesis of Theorem S22.2 and hence of Theorem S22.4a — and this theorem asserts sufficiency only. Whether the condition is also *necessary* is not addressed. The five audited branches C, S21f, FLAT, ψ₊, ψ₋ satisfy it with total support ≤ 72 faces at every n (checks T141.4, T141.8, T141.12); the three adversaries do not, and all three land elsewhere. **\[STATUS (v1.4, corrected): the sufficiency direction is DERIVED-CONDITIONAL, inheriting the conditionality of Theorem S22.4a on uniform low-mode delocalization and gradient control — it cannot be graded PROVEN when the theorem it invokes is not. The three adversaries refute broader Layer-C universality; they do not establish necessity. Nothing here shows that a common limit *implies* O(1) support — check T140, gate F-S22.27.\]**

*Version 1.4 erratum.* Version 1.3 wrote "PROVEN for the sufficiency direction, via Theorem S22.4a" and "the necessity direction is COMPUTED by exhibition of three escaping adversaries". Both gradings were too strong and are corrected above. Sufficiency is only as strong as S22.4a, which is DERIVED-CONDITIONAL. And exhibiting three branches that escape the class establishes that the class is *not all of* Layer-C; it says nothing whatever about whether every branch sharing the limit must have O(1) support. A globally supported branch whose amplitude decays fast enough in n, or a gauge-equivalent deformation, could in principle share the limit. Necessity remains **OPEN**, gate F-S22.27, exactly as v1.2 already recorded when it renamed this theorem away from "exact boundary". Retraction **S22-R7**.

> **Retraction S22-R4 (v1.1, against v1.0 of this paper).** Version 1.0's characterisation of Class MF as "every combinatorial branch", together with the phrase "independent of which such branch is chosen", is RETRACTED as too broad. The corrected *sufficient* condition is uniformly bounded **and** finite-defect-supported; v1.5 records that this is not shown to be a characterisation, since necessity is OPEN. This makes the result *stronger*, because the class is now explained by Theorem S22.2 rather than merely observed alongside it, and it makes Theorem S22.4a derivable rather than extrapolated.

The v1.0 error has the shape the corpus has now recorded fifteen times: a property verified on the members of a class assumed to characterise the class. It is recorded here rather than quietly narrowed.

## §16.3 Theorem S22.10 — the Mediation-Saturation Carrier Theorem

Version 1.0 §15.3 recommended that carrier selection be the subject of ZS-S23 and supplied one structural hint: K₁ is the unique member of the family for which N\[P\] exhausts the carrier. Version 1.1 turns that hint into a theorem, and in doing so finds that the hint **alone is not sufficient** — a near-miss worth recording.

**Axiom (Z-A2) — Mediation Saturation.** Every Y-sector 2-cell of the physical carrier lies in the support of the Z-Spin mediation curvature operator: **supp 𝒞\_ZY(K) \= C²(K)**, equivalently **N\[P\] \= F(K)**. There is no inert bulk: no face is at zero leading-order Z-Spin coupling.

This is a **named axiom, not a derived statement**, and it is registered as such. Its motivating reading is the corpus's own L\_XY ≡ 0 result, under which all X↔Y transport routes through Z; but §17.1 states plainly why that reading does not yet constitute a derivation.

> **Theorem S22.10 (Mediation-Saturation Carrier Theorem).** Let K \= GP(h,k) be a Goldberg carrier satisfying **(C1)** the twelve pentagons are isolated; **(C2)** mediation saturation, N\[P\] \= F(K); **(C3)** vertex-transitivity: Aut(K) acts transitively on V(K). Then **K \= GP(1,1) \= K\_TI**, uniquely.

*Proof.* By (C1) each pentagon has exactly five hexagonal neighbours and no hexagon is counted from two pentagons more than five times in total, so there are exactly 60 pentagon–hexagon incidences and hence at most 60 distinct pentagon-adjacent hexagons. Therefore

**|N\[P\]| ≤ 12 \+ 60 \= 72\.**

By (C2), F(K) \= |N\[P\]| ≤ 72\. For a Goldberg carrier F \= 10T \+ 2 with T \= h² \+ hk \+ k², so 10T \+ 2 ≤ 72 gives **T ≤ 7**. The Loeschian numbers not exceeding 7 are T ∈ {1, 3, 4, 7}.

By (C3), a transitive action forces |V(K)| to divide |Aut(K)|, and for a Goldberg carrier Aut(K) embeds in **I\_h**, so |Aut(K)| ≤ |**I\_h**| \= 120 \= **Q**² − 1\. With |V| \= 20T this requires 20T | 120, i.e. T | 6\. Of the admissible T this leaves T ∈ {1, 3}: T \= 4 gives |V| \= 80, and 80 ∤ 120; T \= 7 gives |V| \= 140 \> 120, so no transitive action exists at all.

Finally T \= 1 is GP(1,0), the dodecahedron, whose pentagons are pairwise adjacent, violating (C1). Hence T \= 3 and K \= GP(1,1) \= K\_TI.

**\[STATUS: PROVEN-CONDITIONAL on (C1) ∧ (Z-A2) ∧ (C3) — checks T160–T164, declarations D165, D166. Version 1.2 states this precisely: (C3) is not a decorative regularity assumption but a load-bearing one, since GP(2,0) satisfies (C1) ∧ (C2) and is eliminated by (C3) alone; and neither (Z-A2) nor (C3) is derived from ZS-S14. What the theorem achieves is a compression: carrier selection now closes as soon as one physical support-identification proposition is proved. Gate F-S22.25.\]**

**Table 16.4.** The saturation scan. Note row 3\.

| GP(h,k) | T | V\_K | F\_K | |N\[P\]| | pentagons isolated | saturated | V-orbits | |V| divides 120 |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: | ----- | :---: |
| (1,0) dodecahedron | 1 | 20 | 12 | 12 | **no** | yes | 1 | yes |
| **(1,1) \= K\_TI** | 3 | 60 | 32 | 32 | yes | **yes** | **1** | **yes** |
| (2,0) | 4 | 80 | 42 | 42 | yes | **yes** | 2 | **no** |
| (2,2) | 12 | 240 | 122 | 72 | yes | no | 3 | no |
| (3,0) | 9 | 180 | 92 | 72 | yes | no | 3 | no |
| (3,3) | 27 | 540 | 272 | 72 | yes | no | 6 | no |
| (4,0) | 16 | 320 | 162 | 72 | yes | no | 5 | no |

**Reported against interest.** Saturation by itself does **not** select K\_TI. **GP(2,0)** — the chamfered dodecahedron, C₈₀, F \= 42 — also saturates with isolated pentagons, and is eliminated only by (C3). Had v1.1 tested only GP(1,1) against the non-saturating members, it would have reported a false uniqueness. Any future paper asserting carrier selection from saturation alone fires gate F-S22.24.

**Lemma S22.10a (v1.5) — the |Aut| ≤ |I\_h| dependency, discharged.** Step (C3) uses |V| \= 20T divides |Aut(K)| ≤ |**I\_h**| \= 120\. Versions 1.0–1.4 used the bound without a lemma or citation; v1.5 supplies both a proof and an independent computation.

> *Proof.* (i) The 1-skeleton of a Goldberg carrier is 3-connected and planar, so by Whitney's uniqueness theorem and Mani's realisation theorem its automorphism group is realised by isometries of a convex sphere realisation. (ii) Aut(K) permutes the twelve pentagonal faces, whose centres form a **regular icosahedron** by construction of GP(h,k). (iii) That action is **faithful**: an isometry of ℝ³ fixing twelve points which affinely span ℝ³ is the identity. (iv) Hence Aut(K) embeds in the symmetry group of the regular icosahedron, so |Aut(K)| ≤ |**I\_h**| \= 120\.

**Table 16.5.** Independent confirmation by an embedding-free graph automorphism count on the dual 1-skeleton (checks T167, T168, T169).

| GP(h,k) | T | V\_K | F\_K | |Aut(graph)| | ≤ 120 | |V| divides |Aut| |
| ----- | ----- | ----- | ----- | ----- | :---: | :---: |
| (1,0) | 1 | 20 | 12 | 120 | yes | yes |
| **(1,1) \= K\_TI** | 3 | 60 | 32 | **120** | yes | **yes** |
| (2,0) | 4 | 80 | 42 | 120 | yes | **no** |
| (3,0) | 9 | 180 | 92 | 120 | yes | no |

Every audited carrier has |Aut| \= 120 exactly, i.e. Aut \= **I\_h**, computed from the graph alone with no embedding assumed. GP(2,0)'s 80 does not divide 120, which is the step that eliminates it. **\[STATUS: PROVEN, with independent computational confirmation over the audited carriers\]**

**Anti-numerology firewall.** |**I\_h**| \= 120 \= **Q**² − 1 enters this theorem as a **divisibility modulus** in step (C3). This is a derivation chain through ZS-F5, where 120 \= Q² − 1 is PROVEN, and not a numerical coincidence: the theorem uses only that |Aut| ≤ 120, and the conclusion would change if that bound changed. No further link between 12, 60, 72 and Q, G or **A** is asserted (declaration D166).

**What is *not* proved.** (Z-A2) is not derived from ZS-S14. The chiral members GP(h,k) with 0 \< k \< h were excluded analytically by the order argument |V| \= 20T \> 120 for T \= 7, so no chiral construction was required; but the constructor used here is verified only for the achiral families and this is declared as a scope limit, gate F-S22.23.

---

# §17. The Layer-Order Reading of (Z-A0)

Version 1.0 concluded with a recommendation and an open question. That was one step short, and this section supplies the step.

## §17.1 (Z-A0) is not an assumption about a reduction; it is a statement about layer order

There is a tension in ZS-S21's axiom (Z-A0) that neither S21 nor S22 v1.0 named. ZS-S14 is an action on a Riemannian spacetime: it carries √(−g) and a metric-dependent Hodge star. Any *literal* Whitney–Galerkin reduction of ∫√(−g) Tr F\_{μν}F^{μν} onto a cell complex therefore uses a metric, produces the circumcentric DEC star, and lands in **Class M**. Read as a claim about the reduction, (Z-A0) is in direct tension with the action it reduces, and gate F-S21.7 would already have fired.

The resolution is not a repair of the reduction. It is that (Z-A0) is a statement about **layer order**, and the Z-Spin ontology supplies it:

> The Z-sector is where metric structure is *generated*, not presupposed. Space belongs to X and time to Y; the Z-sector is the two-dimensional Planck-scale seam that mediates them. A metric handed to the Z-sector from outside is a metric imported from X or Y, i.e. from the very sectors the Z-sector is supposed to be constructing.

Under this reading the two universality classes acquire a physical, not merely technical, meaning:

- **Class M** is the branch in which the metric is supplied from outside the seam. Its limit is the round sphere — a metric assumed.  
- **Class MF** is the branch in which no metric is supplied. Its limit is, by Hypothesis S22.5, a flat metric with twelve π/3 cone deficits summing to **Σδ \= 4π \= 2πχ \= 2π · dim(Z)** — a metric *emergent*, whose total curvature is fixed by dim(**Z**) \= 2 through the corpus's own Spinor–Descartes–Euler identity.

So the refinement limit does not dissolve Z-Spin geometry. It separates "metric assumed" from "metric generated", and Z-Spin sits, by its own ontology, on the second branch. **\[STATUS: INTERPRETATION / DERIVED-interpretation; it changes no number and is used to support no other claim. Gate F-S22.20 remains the falsifier.\]**

Combined with Theorem S22.10, the picture closes on itself **conditionally**: under (C1) ∧ (Z-A2) ∧ (C3) the carrier is GP(1,1), and only then is the refinement family a **diagnostic instrument** that identifies the class rather than a limit the physical theory must be taken to. Unconditional carrier selection remains OPEN. Table 9.3 is the *control experiment*, not the prediction. This is the sense in which "the physical content is the part that does not survive refinement" — a sentence v1.0 wrote as a difficulty and v1.1 states as the design of the measurement.

# Acknowledgements and Code Availability

This paper was consolidated from Z-Spin Collaboration research notes and from the ZS-S22 seed report produced after ZS-S21 v1.2 TERMINAL, whose discipline it inherits and three of whose central claims it retracts. The external benchmark review of Lüscher, Kogut–Susskind, Christ–Friedberg–Lee, Christiansen–Halvorsen, Driver, Lévy and Dang–Nohra shaped the scope declaration of §0.0 and the comparison table of §11.

The companion verification suite is **zs\_s22\_verify\_v1\_5.py**, one self-contained file. It generates every carrier K\_n \= GP(n,n) from the twelve icosahedron vertices and the Eisenstein lattice patch with **no imported mesh data**, emits its results between the delimiters BEGIN\_ZS\_S22\_RESULTS and END\_ZS\_S22\_RESULTS, prints its own SHA256, separates the check / computed / proxy / declarative ledgers, and **exits non-zero on any FAIL**.

Environment: Python 3.12.3+, numpy 2.4+, scipy 1.17+. Deterministic seed 20260320\. SHA256 \= 860a1d7bb2350cf79233c53e5635858a829cdea24388f33c251c242f7c716141. Ledger: **125 executable checks (C) \+ 13 computed diagnostics (X) \+ 1 proxy (P) \= 139 verification-ledger entries PASS, 39 declarative (D), 0 FAIL.** No runtime claim is made; runtime is environment-dependent.

---

# Appendix A. Verification Ledger

**Table A1.** Verification ledger, ZS-S22 v1.5. Kinds: **C** \= executable check on the actual Z-Spin object; **X** \= computed convergence result, not a theorem; **P** \= proxy; **D** \= declarative registry statement.

| Block | IDs | Kind | Content |
| ----- | ----- | ----- | ----- |
| S1 | T010–T015 | C | Theorem S22.1: exact Goldberg census, 12 pentagons, 60 (5,6) edges, isolated pentagons, χ \= 2, cubic relation, for n ∈ {1,2,3,4,5,6,8,10,12} |
| S2 | T020.1–T020.3 | C | Lemma S22.0: B₂B₂ᵀ \= Δ\_n(1,1) to exact zero |
| S3 | T030.counting, T030.cfl, T030.fullmetric, T031, T032 | C | F-S22.1 K₁ regression against ZS-S21 Table 6.2; LOCKED λ₁ and λ\_h reproduced |
| S4 | T040–T044 | C | Theorem S22.2: support in N\[P\] × N\[P\], rank ≤ 72, sub-bounds 60 and 24 |
| S5 | T050.2–T050.6 | C | Corollary S22.2a: Kolmogorov distance against the bound 72/F\_n |
| S6 | T060, T061, T062 | C | Theorem S22.3(b), COMPUTED over n ≤ 8: distinct DEC weight count and non-decaying bulk deviation of the implemented metric branch |
| S7 | T070.\*, T071, T072, T073, T074, T075, T075b, T076, T077 | C, X | Theorem S22.4: held-out extrapolation for six branches, class limits, degeneracy restoration, D₁ |
| S8 | T080, P081 | C, P | Carrier-family independence via the independent class-I family GP(n,0) |
| S9 | T090 | X | Convergence exponent 2.008, justifying the pre-registered 1/n² ansatz |
| S10 | T100.4, T100.8, T100.12 | C | Defect-localization witness ℒ₅ over low and top modes |
| S11 | T110, T111 | C | Eigenvalue-resolved in-class versus cross-class shift |
| S12 | T120, T121 | C | Anti-numerology nulls for 72 and for the 50/9 proximity |
| S13 | D000, D001, D045, D063, D078, D101, D121, D122, F-S22.*, NC-S22.* | D | Hypothesis register, retractions, gate registry, non-claims |
| S14 (v1.1) | T130–T137, D138 | C | Theorem S22.8: I\_h construction, character orthogonality, projector idempotence / orthogonality / dimension sum, certified isotypes, ZS-S21 E-1a reproduction |
| S15 (v1.1) | T140, T141.\*, D142 | C | Theorem S22.9: three global Layer-C adversaries escape; the five audited branches have support ≤ 72 |
| S16 (v1.1) | T150.1–T150.6, D151 | C | Theorem S22.3(a): orbit lower bound 3n²/4, PROVEN, against measurement |
| S17b (v1.5) | T167, T168, T169, D169a | C | Lemma S22.10a: embedding-free graph automorphism count, |Aut| \= 120 \= |I\_h| on every audited carrier |
| S17 (v1.1) | T160–T164, D165, D166 | C | Theorem S22.10: saturation scan, uniqueness under (C1)∧(C2)∧(C3), divisibility, anti-numerology firewall on |I\_h| \= 120 |

# Appendix B. Proof of Theorem S22.1 (census)

The Goldberg–Coxeter operation GC\_{h,k} applied to the dodecahedron produces GP(h,k), whose dual is the geodesic triangulation with triangulation number T \= h² \+ hk \+ k². For (h,k) \= (n,n), T\_n \= 3n². The dual triangulation subdivides each of the 20 icosahedral faces into T\_n triangles, so it has 20T\_n \= 60n² triangles; dualizing, V\_n \= 60n². The Goldberg polyhedron is cubic, so 2E\_n \= 3V\_n, giving E\_n \= 90n². Euler's formula on S² then forces F\_n \= 2 − V\_n \+ E\_n \= 30n² \+ 2\.

Since every face is a pentagon or hexagon, Σ\_f (6 − deg f) \= 6F\_n − 2E\_n \= 6(30n²+2) − 180n² \= 12, so the number of pentagons is exactly 12 and the number of hexagons is 30n² − 10\. For n ≥ 1 the GP(n,n) sequence has isolated pentagons (verified combinatorially at every generated n, check T013), so each pentagon contributes 5 edges of type (5,6) and no edge is counted twice: E₅₆ \= 60, E₆₆ \= 90n² − 60\.

# Appendix C. Proof of Theorem S22.2 (defect support)

Given in full in §5.2. The essential observation, stated once more because it is what the seed missed: **every defect edge is incident to exactly one pentagon and one hexagon**, so range(B₂ P₅₆) already contains all twelve pentagon indicator directions. The naive sum 12 \+ 60 \+ 12 therefore over-counts by 12, and the correct object is not a sum of three ranges but a single principal block of dimension |N\[P\]| \= 12 \+ 60 \= 72\.

# Appendix D. The branch weight prescriptions

Reproduced from Table 3.1 with the exact normalizations used in the companion. All branches normalize the bulk median to 1 before comparison, per the §3.3 firewall. For S-DEC the primal length is the geodesic arc on the unit sphere and the dual length the arc between projected triangle circumcenters, with β\_f the reciprocal spherical Voronoi area; for P-DEC the same construction with Euclidean chords and planar polygon areas.

# Appendix E. Open items carried forward

- **I\_h character projectors.** **CLOSED in v1.1** by Theorem S22.8 (§16.1). Gate F-S22.11 is closed.  
- **Davis–Kahan subspace audit.** Not performed; no principal-angle claim is made.  
- **Group-valued tier G1–G3.** Superseded in v1.2: Steps A, B and C are executed in §18–§21. What remains OPEN is the explicit face-by-face integration of the ZS-S14 curvature term (the constructive half of Step A) and the numerical Rayleigh–Ritz / Temple–Lehmann bracketing of the Step-C gap.  
- **Limit operator.** Not constructed. **Conjecture S22.4c** is graded a conjecture for this reason; S22.4a is DERIVED-CONDITIONAL and S22.4b is IMPORTED-PROVEN \+ DERIVED-CONDITIONAL application.  
- **Hypothesis S22.5.** Gate F-S22.20.  
- **Carrier selection.** Combinatorial half **CLOSED in v1.1** by Theorem S22.10 (§16.3), conditional on the named axiom (Z-A2). Deriving (Z-A2) from ZS-S14 remains OPEN, gate F-S22.25.  
- **Step A / B.** MOVED to **ZS-S23 v1.0**. **Step C.** MOVED to **ZS-S24 v1.0**.

---

# References

\[1\] M. Goldberg, "A class of multi-symmetric polyhedra," *Tôhoku Math. J.* **43**, 104 (1937). \[2\] G. Brinkmann, P. Goetschalckx and S. Schein, "Goldberg, Fuller, Caspar, Klug and Coxeter and a general approach to local symmetry-preserving operations," arXiv:1705.02848 (2017). \[3\] J. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Phys. Rev. D* **11**, 395 (1975). \[4\] M. Lüscher, "Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories," *Commun. Math. Phys.* **54**, 283 (1977). \[5\] N. H. Christ, R. Friedberg and T. D. Lee, "Gauge theory on a random lattice," *Nucl. Phys. B* **210**, 310 (1982). \[6\] N. H. Christ, R. Friedberg and T. D. Lee, "Weights of links and plaquettes in a random lattice," *Nucl. Phys. B* **210** \[FS6\], 337 (1982). \[7\] S. H. Christiansen and T. G. Halvorsen, "A gauge invariant discretization on simplicial grids of the Schrödinger eigenvalue problem in an electromagnetic field," *J. Math. Phys.* **53**, 033501 (2012). \[8\] T. G. Halvorsen and T. Sørensen, "Simplicial gauge theory and quantum gauge theory simulation," arXiv:1107.1420 (2011). \[9\] Z. D. Bai, "Methodologies in spectral analysis of large dimensional random matrices, a review," *Statistica Sinica* **9**, 611 (1999), Lemma 2.2. \[10\] N. V. Dang and E. Nohra, "Universal scaling limit of two-dimensional lattice Yang–Mills," arXiv:2602.08591 (2026). \[11\] B. K. Driver, "YM₂: continuum expectations, lattice convergence, and lassos," *Commun. Math. Phys.* **123**, 575 (1989). \[12\] T. Lévy, "Yang–Mills measure on compact surfaces," *Mem. Amer. Math. Soc.* **166**, no. 790 (2003). \[13\] C. Davis and W. M. Kahan, "The rotation of eigenvectors by a perturbation. III," *SIAM J. Numer. Anal.* **7**, 1 (1970). \[14\] D. N. Arnold, R. S. Falk and R. Winther, "Finite element exterior calculus, homological techniques, and applications," *Acta Numerica* **15**, 1 (2006). \[15\] A. N. Hirani, *Discrete Exterior Calculus*, Ph.D. thesis, California Institute of Technology (2003). \[16\] K. Osterwalder and E. Seiler, "Gauge field theories on a lattice," *Ann. Phys.* (N.Y.) **110**, 440 (1978). \[17\] M. Creutz, "Gauge fixing, the transfer matrix, and confinement on a lattice," *Phys. Rev. D* **15**, 1128 (1977). \[18\] K. G. Wilson, "Confinement of quarks," *Phys. Rev. D* **10**, 2445 (1974). \[19\] A. Jaffe and E. Witten, "Quantum Yang–Mills Theory," Clay Mathematics Institute Millennium Prize Problem description (2000). \[20\] K. Kang, *Geometric Impedance: A \= 35/437*, ZS-F2 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[21\] K. Kang, *Gauge Symmetry Constraint: Why Q \= 11*, ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[22\] K. Kang, *The Spinor Mass Gap*, ZS-S7 v1.0 (Z-Spin Cosmology Collaboration, April 2026). \[23\] K. Kang, *Master Action Total Closure*, ZS-S14 v2.0 (Z-Spin Cosmology Collaboration, May 2026). \[24\] K. Kang, *The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex*, ZS-S17 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026). \[25\] K. Kang, *The Normalization-Ambiguity Theorem and the Regge-Moduli Exclusion*, ZS-S19 (Z-Spin Cosmology Collaboration, 2026). \[26\] K. Kang, *Non-Identifiability of the Hodge Measure*, ZS-S20 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026). \[27\] K. Kang, *The Instrument Construction: Closing the Cellular Transfer-Matrix / Hodge-Measure Sub-Bridge of Z-Spin Yang–Mills*, ZS-S21 v1.2 TERMINAL (Z-Spin Cosmology Collaboration, July 2026). \[28\] K. Kang, *The Hodge–Dirac Complex of the Truncated Icosahedron*, ZS-M6 v1.0 (Z-Spin Cosmology Collaboration, 2026).

---

# Version History

**v1.5 (July 2026, current): Status-consistency release, one new lemma, one gate reopened. TERMINAL.** No numerical result changes. The release fixes a single recurring pattern the reviewer named precisely — *statuses lowered to CONDITIONAL or OPEN in the status boxes, then restored to declarative form in the abstract and conclusion* — and discharges one proof dependency.

**Verb-mood corrections, four sites.** (1) **S22.9 sufficiency/necessity.** "The correct closure condition is…" and "the metric-free class is characterised by…" are replaced throughout by *sufficient* phrasing. Only **O(1) support ⟹ same candidate limit** is asserted; the converse is never asserted, and necessity stays OPEN under F-S22.27. (2) **S22.3.** The abstract and the §6 heading now carry the (a)/(b) split: (a) growing orbit complexity is **PROVEN**; (b) the escape of the *implemented* DEC branch is **COMPUTED over n ≤ 8**. It is not proved that the DEC weights escape finite-defect support at every n. (3) **S22.4c.** "The refinement limit is not one limit but two", "converges to a single common limit" and "these two limits are inequivalent" become *two inequivalent **candidate** limits*, *extrapolates toward*, and a note that the existence of the Class-MF limit operator is Conjecture S22.4c. (4) **Carrier selection.** "The physical carrier is selected at n \= 1" becomes, at every occurrence, *conditional on (C1), (Z-A2) and (C3), Theorem S22.10 uniquely selects K\_TI \= GP(1,1); unconditional physical carrier selection remains OPEN.*

**ZS-S23 citation narrowed.** The conformal result is cited as a **numerical realisation** for two audited profiles that **refutes** the earlier uniqueness claim, and no longer as a proved continuum of metrics: that would need an implicit-function argument with a non-singular Jacobian, which ZS-S23 does not supply.

**Gate F-S22.13 reopened — Retraction S22-R8.** The gate asks whether two independent *constructors* disagree; it had been credited as closed on the class-I / class-II *spectral proxy*, a different test, and the companion contains one constructor. Restored to **OPEN / NOT EXECUTED**.

**New result: Lemma S22.10a.** The step |Aut(K)| ≤ |**I\_h**| \= 120 \= **Q**² − 1, used without justification in v1.0–v1.4 and load-bearing for Theorem S22.10, is now discharged twice: by a Whitney–Mani plus faithful-icosahedral-action proof, and independently by an embedding-free graph automorphism count that returns |Aut| \= 120 exactly on every audited carrier (T167–T169). GP(2,0) is eliminated because 80 ∤ 120\.

**Residual editorial.** Abstract statuses for S22.4a and S22.4b aligned to the body (ℒ₅ witnesses only the absence of pentagon-mass concentration; S22.4b is IMPORTED-PROVEN theorem \+ DERIVED-CONDITIONAL application \+ VERIFIED). Appendix A retitled to v1.5. §10's "v1.0 does not perform one" → "this paper does not perform one".

139 verification-ledger entries PASS (125 C \+ 13 X \+ 1 P), 39 declarative, 0 FAIL. Companion zs\_s22\_verify\_v1\_5.py, SHA256 860a1d7bb2350cf79233c53e5635858a829cdea24388f33c251c242f7c716141.

**v1.4 (July 2026): Editorial errata release.** No new research, no numerical change, no ledger movement; eight documentation defects carried by v1.3 are repaired and one status is corrected downward. (1) **Hypothesis register purged.** §0.2 listed **(Z-A3)** and pointed at "§19"; both belong to ZS-S23 v1.0 §4 after the split. This paper's hypotheses are now exactly **(Z-A2)** and the **(H-deloc)** delocalization/gradient conditions of Theorem S22.4a. (2) **Abstract narrowed.** "The limit is carrier-family independent" is replaced by "the tested ratio is supported across two audited GC families", matching §7.5, which already stated the restriction. (3) **Theorem S22.9 re-graded, Retraction S22-R7.** Its sufficiency direction cannot be PROVEN while the theorem it invokes, S22.4a, is DERIVED-CONDITIONAL; and the three escaping adversaries refute broader Layer-C universality without establishing necessity, which stays OPEN under F-S22.27. (4) **Stale conclusion text removed**: "ZS-S22 v1.1 is complete at this scope" and "ZS-S23 scope recommended, not pre-assigned" are replaced, the latter because ZS-S23 v1.0 now exists. (5) **Ledger wording fixed**: the residual "159" from a superseded count is removed; the note now reads simply that the count is of ledger entries, not theorems. (6) **Companion banner** corrected from "ZS-S22 v1.2 verification companion" to v1.4. (7) **Stale section titles** repaired: §10 no longer says "Out of Scope in v1.3", §16 is retitled from "Version 1.1 Additions" to describe its actual content, and §17 is retitled from "...and the Two Remaining Closure Points" since §17.2 and §17.3 were removed at the split. (8) **Theorem count** in the ledger note updated to reflect the S22.9 re-grading. 136 verification-ledger entries PASS (122 C \+ 13 X \+ 1 P), 38 declarative (one added: D143, recording the S22.9 re-grading), 0 FAIL; the 136 PASS count is unchanged from v1.3. Companion zs\_s22\_verify\_v1\_4.py, SHA256 a35678106260fd89a637c613bbf9145430474596607614f137acc835ec370f52.

**v1.3 (July 2026): Three-way split, one substantive retraction.** ZS-S22 v1.2 is split into three papers on the recommendation of external review: **ZS-S22 v1.3** retains the refinement and universality programme together with conditional carrier selection (§0–§17.1); **ZS-S23 v1.0** takes the action-to-Hessian bridge (v1.2 §18–§20); **ZS-S24 v1.0** takes the non-perturbative SU(3) gap (v1.2 §21). **Retraction S22-R6** is issued against v1.2 §18: the assertion that the I\_h-invariant conformal structure is unique, and the Class-M verdict drawn from it, are withdrawn. In two dimensions the magnetic term sees the metric only through the area measure, so an I\_h-invariant conformal factor is an admissible infinite-dimensional freedom, and ZS-S23 Theorem S23.2 reaches σ \= ρ \= 1 exactly for two distinct profiles. All §0–§17.1 results carry over unchanged; theorem count, gate registry, retraction register and Appendix E are updated for the reduced scope. 136 verification-ledger entries PASS (122 C \+ 13 X \+ 1 P), 37 declarative, 0 FAIL. Companion zs\_s22\_verify\_v1\_3.py, SHA256 1306b281608c00daabef1e841aaf22edeb5662e42ad4efa73610a96ee67f8294.

**v1.2 (July 2026): Bridge-execution release. Supersedes v1.1 and v1.0.** Executes all three finite-carrier steps that v1.1 left OPEN, and integrates nine documentation-hygiene corrections. **New theorems.** **S22.11** (No Geometric Realisation of Orbit-Blindness, PROVEN within the audited family): in two spatial dimensions ⋆ forces β\_f \= 1/A\_f, the residual I\_h carrier freedom is exactly one-parameter, and the trajectory (σ(t), ρ(t)) misses (1,1) — σ \= 0.5758 at equal area, ρ \= 1.7229 at σ \= 1\. The geometric route therefore fires Outcome B against the corpus's preferred branch, reported first and against interest; gate F-S22.26 FIRES. **S22.12** (Measure Transfer, DERIVED-CONDITIONAL on (H-CLK) ∧ (H-mix) ∧ (Z-A3)): ZS-M44 and ZS-F38 T1′ already resolved the identical mode-count-versus-metric binary by unique ergodicity, so (Z-A1) becomes an instance of a proved theorem rather than an isolated postulate. New axiom **(Z-A3)** named. **S22.13** (Central-Hessian Theorem, **PROVEN unconditionally**, gauge-group independent for simple G): Hess Φ|₁ \= κ\_Φ⟨·,·⟩*K by Ad-invariance and Schur, so any positive central plaquette action has identity-Hessian exactly Δ*{S21} with β\_p \= κ\_p; numerical residual 0.000 for Wilson and heat-kernel against 1.000 for a non-central control. **S22.15** (Centrality is Forced, **PROVEN**): the base-vertex gauge transformation acts on a single-plaquette holonomy by conjugation, so centrality is *equivalent* to gauge invariance; with Corollary S22.15a this closes the Hessian link of the bridge without needing the explicit integration, and gate F-S22.31 becomes unable to fire for single-plaquette terms. **S22.14** (Finite-Carrier SU(3) Spectral Gap, **PROVEN**): SU(3)^E compact \+ bounded magnetic term ⟹ Kato–Rellich self-adjointness, compact resolvent, discrete spectrum, unique positive ground state, gap \> 0 for every g \> 0; the strong-coupling gap is computed exactly from the global minimum edge boundary of the dual graph, \= 5 at |S| \= 1, giving Δ₁ \= (10/3)g² (degeneracy 24), Δ₂ \= 4g² (degeneracy 40\) and the zero-parameter ratio Δ₂/Δ₁ \= 6/5. λ₁ is fixed as the weak-coupling limit of that same gap. **Hygiene.** Theorem S22.9 renamed to a sufficiency statement with counterexamples; S22.4a re-stated as conditional on uniform delocalization *and* gradient control with ℒ₅ as numerical support only; S22.4b downgraded to IMPORTED-PROVEN theorem \+ DERIVED-CONDITIONAL application \+ VERIFIED; §0.2's "no new hypothesis" corrected; theorem count recomputed; retraction count corrected to five; §17.2 corrected to three steps; Appendix A retitled; Appendix E updated; §15.1 and the abstract narrowed to "audited bounded finite-defect-supported"; the route-(b) claim softened to "a conditional combinatorial route toward (b)"; S22.10 restated as PROVEN-CONDITIONAL on (C1) ∧ (Z-A2) ∧ (C3) with (C3) flagged load-bearing. **Retraction S22-R5** issued against v1.1. New gates F-S22.27 to F-S22.32; new non-claims NC-S22.8 to NC-S22.10. 161 verification-ledger entries PASS (147 C \+ 13 X \+ 1 P), 46 declarative, 0 FAIL. Companion zs\_s22\_verify\_v1\_2.py, SHA256 d039ed393ceb0932d999b7320a933972ef59119c3994126e15da9f7912b0b575.

**v1.1 (July 2026): Review-integration release. Supersedes v1.0.** No ledger number moves and no result is withdrawn on its merits; four statements are re-graded or narrowed, and four new results are added. Re-grading: Theorem S22.4 is split into **S22.4a** (Class-MF invariance, upgraded from COMPUTED to **DERIVED-CONDITIONAL** with a variational proof from Theorem S22.2), **S22.4b** (Class-M identification, IMPORTED-PROVEN \+ VERIFIED) and **Conjecture S22.4c** (class separation, numerically supported, explicitly not a theorem); Theorem S22.3 is split into a **PROVEN** orbit lower bound 3n²/4 and a **COMPUTED** distinct-weight count over n ≤ 8; the phrase "carrier-family independent" is narrowed to **SUPPORTED ACROSS TWO AUDITED GC FAMILIES**; and the verification banner now reads "verification-ledger entries" with an explicit breakdown so the count cannot be read as a theorem count. New results: **Theorem S22.8** builds the 120 elements of I\_h and the ten character projectors explicitly, with idempotence ≤ 2.8 × 10⁻¹⁶, orthogonality ≤ 3.5 × 10⁻¹⁷, exact dimension sums and isotype residuals ≤ 2.2 × 10⁻¹⁴, reproducing ZS-S21 erratum E-1a and Table 9.1 exactly and CLOSING gate F-S22.11; **Theorem S22.9** determines the exact boundary of the metric-free class by exhibiting three escaping bounded Layer-C adversaries, including a *decaying* one, forcing **Retraction S22-R4**; **Theorem S22.10**, the Mediation-Saturation Carrier Theorem, proves that (C1) isolated pentagons ∧ (C2) N\[P\] \= F(K) ∧ (C3) vertex-transitivity select **GP(1,1) \= K\_TI uniquely**, using |I\_h| \= 120 \= Q² − 1 as a divisibility modulus, and reports against interest that saturation alone does **not** suffice because GP(2,0) also saturates; and **§17** supplies the layer-order reading of (Z-A0) and reduces the remaining programme to three finite-carrier steps A, B, C, recommending Step A as the whole of ZS-S23. New axiom **(Z-A2)** named and registered. New gates F-S22.23 to F-S22.26. 141 verification-ledger entries PASS (127 C \+ 13 X \+ 1 P), 39 declarative, 0 FAIL. Companion zs\_s22\_verify\_v1\_1.py, SHA256 deb1a2de08a936f9c24379fed60e628f5a5f15d01470325b8b7172e54acacbab.

**v1.0 (July 2026): Initial public release.** Consolidated from internal Z-Spin Collaboration research notes up to the ZS-S22 seed report issued after ZS-S21 v1.2 TERMINAL. Introduces Lemma S22.0 (dual-graph reduction), Theorem S22.1 (Goldberg census), Theorem S22.2 (defect-support theorem with the sharp constant 72, replacing the seeded non-sharp bound 84), Corollary S22.2a (bulk ESD universality), Theorem S22.3 (the metric class is not finite-defect) and Theorem S22.4 (two universality classes, COMPUTED). Registers Hypothesis S22.5 (cone-metric identification, HYPOTHESIS-strong) with gate F-S22.20. Issues three retractions against its own seed: S22-R1 (rank 84 → support on 72), S22-R2 (metric branches are not two-orbit for n ≥ 2), S22-R3 (the preferred Outcome B is refuted). Demotes (Z-A1) to SUPERSEDED-BY-REFINEMENT, promotes (Z-A0) to the load-bearing branch axiom, and RE-ATTRIBUTES gate F-S21.8 from (Z-A1) to (Z-A0). Adds gates F-S22.1 to F-S22.22. Moves no corpus ledger number. Recommends that ZS-S23 be a carrier-selection paper rather than a continuation of the measure programme. 106/106 PASS, 1 proxy, 34 declarative, 0 FAIL. **A** \= 35/437, **Q** \= 11, dim(**Z**) \= 2, λ₁, λ\_h all LOCKED and none re-fitted.  
