# **ZS-S23**

# **The Action-to-Hessian Bridge on the Physical Z-Spin Carrier: the Metric Route, the Clock Route, and the Central-Hessian Theorem**

**Author:** Kenny Kang · Z-Spin Cosmology Collaboration **Date:** July 2026 **Theme / paper code:** ZS-S23 — Standard Model line, action-to-Hessian bridge **Version:** v1.3 TERMINAL (third review-response revision; supersedes v1.2) **Companion:** zs\_s23\_verify\_v1\_3.py

**Verification: 98 executable entries PASS \= 87 theorem-bearing checks (C) \+ 11 COMPUTED diagnostics (X) | 12 declarative (D) | 0 FAIL | ZERO NEW FITTED PHYSICAL PARAMETERS | A \= 35/437, Q \= 11, dim Z \= 2, λ₁, λ\_h all LOCKED and none re-fitted | SHA256(companion) \= c15927799cfdd821128fa5615dd93a9852088e480e6557ecdc16cd8141dad3f6**

> **On the C/X split, new in v1.3.** Version 1.2 recorded all 95 entries as kind **C**, while its own text demoted eight of them to COMPUTED status. A ledger that grades an entry differently from the manuscript is a ledger that cannot be audited. In v1.3 the eleven entries whose content is numerical evidence with measured but unbounded discretisation error — the quadrature convergence study, the true-residual figure, the sampled monotonicity audit, the multistart minimality test, the Jacobian, the non-uniqueness and third-profile roots, and the geodesic-corrected root — are recorded as kind **X**, carrying no proof weight. The remaining **87** entries are kind **C** and carry proof weight.  
>   
> **On "zero parameters".** The conformal probe coordinates **t**, **a**, **w** of §3.5 are *not* physical parameters and are *not* fitted to any observation. They are search coordinates on the space of I\_h-invariant metrics, introduced for the sole purpose of demonstrating **non-identifiability**, and no physical quantity in this paper depends on their values. Version 1.1's front-matter phrase "Zero Free Parameters" was literally inaccurate in their presence and is replaced throughout by **Zero New Fitted Physical Parameters**.

---

# §0. Abstract

ZS-S21 assumed, and ZS-S22 could not decide, the two statements on which the whole S-line rests: **(Z-A0)**, that the cellular reduction of the ZS-S14 master action is metric-free, and **(Z-A1)**, that its orbit weights are blind to the pentagon/hexagon distinction, σ \= ρ \= 1\. This paper attacks both at the level of the action, and reports a mixed and largely negative result, because that is what the calculations give.

**Step A, metric route.** Under a cellwise-constant Whitney reduction the face weight is β\_f \= 1/A\_f. **Theorem S23.1** shows that in the **round** metric the one-parameter I\_h truncation family never reaches σ \= ρ \= 1\. Version 1.0 called this "PROVEN by exhibition"; that phrase is withdrawn and replaced by an actual proof. Section §3.2 supplies closed forms — **tan r₅(t) \= t√(1−c²)/(1 − t(1−c))** with c \= 1/√5, **A₅ \= 10 arctan(cot(π/5)/cos r₅) − 3π**, **A₆ \= (π − 3A₅)/5**, **l₅₆ \= 2 arcsin(sin r₅ sin(π/5))**, **l₆₆ \= 2 arctan((1−2t)√((1−c)/(1+c)))**, and the exact t-independent dual arcs **cos d₅₆ \= √(1/3 \+ 2√5/15)**, **cos d₆₆ \= √5/3** — from which strict monotonicity of both σ and ρ follows analytically, root uniqueness follows from monotonicity, and the strict separation is certified at the single rational point t \= 7/20 by a genuine **interval-arithmetic enclosure** (new in v1.2), which returns σ(7/20) ∈ \[0.764687452808418, 0.764687452808418\] and ρ(7/20) ∈ \[1.304973571261295, 1.304973571261295\] at enclosure widths below 10⁻⁴⁸, so that σ(7/20) \< 765/1000 \< 1 \< 1304/1000 \< ρ(7/20) rigorously. Gate F-S23.9 is therefore **CLOSED-PASS** and the PROVEN status no longer sits beside an open certification gate. No numerical root-find enters the proof. The equal-area point admits the closed form **cos r₅ \= cot(π/5)·cot(5π/16)**, equivalently A₅ \= π/8.

**Step A, conformal correction.** ZS-S22 v1.2 concluded that geometry *forces* Class M. **Theorem S23.2 provides strong computed counterevidence against that conclusion** — v1.2 said "refutes", which overstates what a COMPUTED application can deliver — and v1.0 offered a solver residual and called it a proof. Three corrections are made. First, **Lemma S23.2a** proves that the carrier data v1.0 held fixed are *not* an approximation: the pentagon and hexagon circumcentres are the isolated fixed points of C₅ᵥ and C₃ᵥ and are therefore metric-independent for every I\_h-invariant metric, and the two dual arcs together with the primal (6,6) edge lie in mirror planes of I\_h, hence are **stationary geodesics** of every I\_h-invariant metric. Version 1.2 narrows the wording from *geodesy* to *stationary geodesy*, since totally geodesic does not by itself give global minimality; the DEC lengths are accordingly fixed by an explicit **Convention D-len**, and any reinterpretation as global metric distance must first discharge the new gate F-S23.12. Exactly **one** of the four arcs — the primal (5,6) edge — is not mirror-contained, and it is the sole residual approximation, measured at a relative length gap of **5.33 × 10⁻³**. Second, the reachability claim is re-proved by the **intermediate value theorem** rather than by fsolve, and in v1.2 the resulting status is **split in two**: the abstract IVT statement, **Lemma S23.2b**, is PROVEN-CONDITIONAL on hypotheses (D1)–(D3), while its *application* to the audited discretisation is VERIFIED for (D1) and (D3) and only **COMPUTED** for (D2), because a finite grid plus a sampled curvature bound covers the t-direction but not the amplitude direction. Version 1.1's "each VERIFIED, therefore existence at proof strength" was one grade too strong and is retracted. Third, the published residual **1.6 × 10⁻¹⁴ is retracted as a solver residual**: re-evaluated at the full-mode reference quadrature (384, 96\) the v1.0 root has a true geometric residual of **2.07 × 10⁻³**, eleven orders of magnitude larger. The metric route therefore still **under-determines** — that conclusion strengthens — but its numerical support is restated at its honest precision.

**Step A, clock route.** **Theorem S23.3** transfers ZS-F38's proved unique-ergodicity result to the carrier under a new named axiom **(Z-A3)**, yielding σ \= ρ \= 1\. Section §4.3 states the objection rather than burying it: a stationary **probability** is not a kinetic **stiffness**, and ZS-S20 already named this step an unresolved bridge **(H-PSM-2)**. ZS-F40's physical clock discharge returned CLOSED-NEGATIVE with a Frobenius deviation of exactly **√2**, unreconciled here. **(Z-A1) is relocated, not eliminated, and the corpus axiom count is unchanged.** Version 1.0 contradicted itself on this point within a single subsection; the contradiction is removed.

**Step B.** **Theorem S23.4** proves that for compact simple G any C² central Φ has Ad-invariant identity-Hessian, hence by Schur equal to κ\_Φ times the Killing form; **Lemma S23.5** proves centrality is *equivalent* to gauge invariance for a single-plaquette term. **Theorem S23.6** corrects the type error inherited from ZS-S22 v1.2: the Hessian is a **90 × 90 edge-space** operator, Δ\_{S21} is a **32 × 32 face-space** operator, and they are **nonzero-isospectral**, not equal. Single-plaquette locality is exactly **(H-W)**, which remains OPEN, so Step B is **PROVEN-CONDITIONAL on (H-W)**.

**The honest one-line summary.** The action-to-Hessian bridge is closed in its *algebraic* half — the Hessian's form is forced, conditionally on (H-W) — and open in its *selection* half: neither the metric route nor the clock route determines the orbit weights, and the class question is now OPEN in one specific, named place, the density-versus-rate identification.

---

# Epistemic Status Legend

> **PROVEN** — a complete mathematical proof is given or cited. **PROVEN-CONDITIONAL** — a complete proof, contingent on explicitly named hypotheses. **DERIVED** / **DERIVED-CONDITIONAL** — follows from corpus results by stated steps, unconditionally or under named hypotheses. **IMPORTED-PROVEN** — proved in the external literature and applied here. **VERIFIED** — reproduced numerically by the companion at stated precision, on the actual Z-Spin object. **COMPUTED** — a number produced by an approximate numerical prescription whose discretisation error is measured but not bounded rigorously. Carries no proof weight. *(New in v1.1; introduced because v1.0 had no status able to hold the conformal root honestly.)* **CONJECTURE** — a statement the authors expect to hold, with the missing steps named. *(New in v1.1.)* **TESTABLE** — a falsifiable consequence with a stated gate. **CLOSED-PASS** — a falsification gate that has been executed and did not fire. *(New in v1.2; F-S23.9 is the first.)* **HYPOTHESIS-strong** — a conjecture with convergent evidence from structurally independent routes and a named path to proof. *(Used in v1.3 for Corollary S23.2e.)* **HYPOTHESIS** / **OPEN** / **NON-CLAIM** / **RETRACTED** — as in ZS-S22 v1.3.

---

# §1. What ZS-S21 Assumed and ZS-S22 Could Not Decide

ZS-S21 v1.2 proved that its transfer-matrix construction **propagates** rather than **selects** the orbit weights σ \= m₅₆/m₆₆ and ρ \= β₅/β₆, closing DERIVED-CONDITIONAL on (H-W) ∧ (Z-A0) ∧ (Z-A1). ZS-S22 v1.3 then proved that the Goldberg refinement family carries **two** inequivalent universality classes, separated by 7.993 % in λ₃/λ₁, and that the finite-defect class is characterised by uniform boundedness plus O(1) support. Under ZS-S22 Theorem S22.10 the physical carrier is GP(1,1) \= K\_TI, conditionally on (Z-A2) ∧ (C3).

What neither paper could do is say **which class the physical theory occupies**, because that is a question about the action, not about the instrument. This paper asks it at the action level.

---

# §2. Scope, and What Is Not Attempted

This paper works entirely at n \= 1 on K\_TI and makes no refinement claim. It does **not** perform the explicit integration of the ZS-S14 curvature term over the 32 faces and 90 temporal prisms of K\_TI × a\_tℤ; that remains the single most valuable open computation in the S-line and is gate F-S23.6. It makes no claim about the Yang–Mills mass gap. It introduces one new axiom, **(Z-A3)**, and one new falsification gate for each of the statements it declines to close.

**What v1.3 adds over v1.2.** No new physics and no new claims. Six corrections, five of them demotions or repairs: Corollary S23.2e demoted from DERIVED to COMPUTED / HYPOTHESIS-strong (§3.6); hypothesis **(D2b)** added to Lemma S23.2b, without which its existence step is invalid (§3.5); Tables 3.2, 3.2a, 3.4 and 3.4a reconciled with what the companion actually computes, including the w \= 0.45 audit and the geodesic-corrected root, both now run in-suite (§3.3–§3.5); the eleven COMPUTED ledger entries reclassified from kind C to kind X (Appendix A); and the C²/O(a³) regularity of Theorem S23.4 corrected (§5). **This is the terminal version of ZS-S23.**

**What v1.2 added over v1.1.** An interval-arithmetic certificate closing gate F-S23.9 (§3.2); a status split for Theorem S23.2 separating the abstract lemma from its numerical application (§3.5); a narrowing of Lemma S23.2a from *geodesy* to *stationary geodesy*, with global minimality moved to a new gate F-S23.12 (§3.3); a logically repaired F-S23.1 (§6); and reconciliation of the companion's banner, quadrature grid, residual figures and FAST-mode labelling with this manuscript (§6, Retraction S23-R13).

**What v1.1 added over v1.0.** Three proofs that v1.0 asserted without giving (Theorem S23.1, Lemma S23.2a, the IVT half of Theorem S23.2); one quantitative audit that v1.0 omitted (the quadrature-convergence study of §3.4); one internal contradiction removed (§4.3); and a full rewrite of the companion's declaration ledger, which in v1.0 printed statements the v1.0 body had already retracted.

---

# §3. Step A — the Metric Route, and Why It Under-Determines

## §3.1 What the two-dimensional Hodge star does and does not force

The magnetic term of ZS-S14 is ∫ Tr(F ∧ ⋆F). On a **two-dimensional** spatial carrier, ⋆ maps Ω² → Ω⁰, so in local coordinates F \= F₁₂ dx¹∧dx² and ⋆F \= F₁₂, hence

**∫\_f Tr(F ∧ ⋆F) \= ∫\_f Tr(F₁₂²) dA \= Tr(Φ\_f²)/A\_f**,  Φ\_f := ∫\_f F.

**This identity is not exact in general, and ZS-S22 v1.2 over-claimed it.** In general ∫\_f Tr(F²) ≠ Tr((∫\_f F)²)/A\_f; Cauchy–Schwarz gives only Tr((∫\_f F)²)/A\_f ≤ ∫\_f Tr(F²), with equality iff F is constant on f. The right-hand side is what one obtains under a **cellwise-constant, lowest-order Whitney / mass-lumped projection**. In the non-abelian case there is a further gap: Φ\_f \= ∫\_f F is not the plaquette holonomy, because of path ordering and the non-abelian Stokes theorem. The honest statement is therefore

> **Under a cellwise-constant (mass-lumped, lowest-order Whitney) reduction, β\_f \= 1/A\_f.**

and *not* "two dimensions forces β\_f \= 1/A\_f exactly". Likewise ⋆ on 1-forms gives m\_e \= |⋆e|/|e| under the same convention. **\[STATUS: DERIVED-CONDITIONAL on the cellwise-constant Whitney reduction; the exact face-and-prism integration remains OPEN, gate F-S23.6.\]**

*(Retraction S23-R2, against ZS-S22 v1.2 §18.1: the word "exactly" and the claim that the reduction is "forced, not chosen" are withdrawn. What is forced is the structural form — a face weight inversely proportional to an area — not the identity itself.)*

In two dimensions the magnetic term depends on the metric **only through the area measure**, and the *continuum* electric term is conformally invariant (⋆ on k-forms in d dimensions is conformally invariant iff 2k \= d, here k \= 1, d \= 2). Version 1.2 concluded that the I\_h-invariant conformal structure is unique and that all residual freedom sits in the cell decomposition. **That conclusion is false.** Uniformization says every *conformal structure* on S² is the standard one; it does **not** say the *metric* is. An I\_h-invariant conformal factor e^{2φ} is an admissible, and **infinite-dimensional**, freedom, and it changes every A\_f.

## §3.2 Theorem S23.1 — the round-metric no-go, now with a proof

Version 1.0 wrote "PROVEN by exhibition within the audited family". The external review is correct that this is not a proof: a no-go over a continuum requires monotonicity, root uniqueness, and strict separation, none of which follows from evaluating a solver at two points. This subsection supplies all three in closed form. Every identity below is verified against the independently constructed spherical geometry of the companion to better than 10⁻¹¹ (checks T170a–T170c).

**Setup.** Let c := V\_i · V\_j \= 1/√5 for adjacent icosahedron vertices on the unit sphere. The carrier K\_TI(t) has primal vertices P(i,j) \= normalise((1−t)V\_i \+ tV\_j), t ∈ (0, ½), with t \= ⅓ the Archimedean carrier.

**(i) The pentagon circumradius.** Decompose (1−t)V\_i \+ tV\_j into its component along V\_i and its orthogonal complement. The parallel component is 1 − t(1−c) and the perpendicular component has norm t√(1−c²), whence

**tan r₅(t) \= t√(1−c²) / (1 − t(1−c))**.

On (0, ½) the numerator is positive and strictly increasing and the denominator is positive and strictly decreasing, since 1/(1−c) \= 1.809 \> ½. Therefore **r₅ is strictly increasing**, with values in (0, π/2).

**(ii) The pentagon area.** The pentagon is regular by the C₅ᵥ stabiliser of V\_i. Decomposing a regular spherical n-gon of circumradius r into 2n right triangles and applying Napier's rule cos c \= cot A cot B,

**A₅(t) \= 10 arctan(cot(π/5)/cos r₅) − 3π**.

cos r₅ is strictly decreasing in r₅ on (0, π/2), so the argument of arctan is strictly increasing, so **A₅ is strictly increasing in t**.

**(iii) The hexagon area is not independent.** Area closure 12A₅ \+ 20A₆ \= 4π holds identically (check T170), so A₆ \= (π − 3A₅)/5 and

**ρ(t) \= A₆/A₅ \= π/(5A₅) − 3/5**,

which is **strictly decreasing in A₅**, hence strictly decreasing in t.

**(iv) The two primal edge lengths.** The pentagon edge subtends 2π/5 at V\_i, so l₅₆ \= 2 arcsin(sin r₅ sin(π/5)), **strictly increasing**. For the (6,6) edge, write V\_i \= αm − βn and V\_j \= αm \+ βn in the orthonormal frame of the edge midpoint m, with α \= √((1+c)/2), β \= √((1−c)/2). Then (1−t)V\_i \+ tV\_j \= αm − (1−2t)βn, so

**l₆₆(t) \= 2 arctan((1−2t)√((1−c)/(1+c)))**,

**strictly decreasing** on (0, ½).

**(v) The dual arcs are exact constants.** The dual vertices are I\_h fixed points (Lemma S23.2a(i)), hence t-independent, and their arcs are algebraic:

**cos d₅₆ \= √(1/3 \+ 2√5/15) \= 0.7946544723**,  d₅₆ \= 0.6523581398; **cos d₆₆ \= √5/3 \= 0.7453559925**,  d₆₆ \= 0.7297276562.

**(vi) Conclusion.** σ(t) \= (d₅₆/d₆₆)·(l₆₆/l₅₆) is a positive constant times a strictly decreasing function over a strictly increasing function, hence **strictly decreasing**.

**Table 3.1.** The one-parameter carrier family, from the closed forms. Areas close exactly (check T170).

| t | A₅ | A₆ | ρ \= A₆/A₅ | σ |
| ----- | ----- | ----- | ----- | ----- |
| 0.10 | 0.021203 | 0.615597 | 29.034041 | 7.405648 |
| 0.20 | 0.093987 | 0.571927 | 6.085191 | 2.732973 |
| 0.25 | 0.154107 | 0.535854 | 3.477157 | 1.808367 |
| **⅓ (Archimedean)** | 0.295072 | 0.451275 | **1.529372** | **0.893975** |
| **7/20 (separator)** | 0.329831 | 0.430420 | **1.304974** | **0.764687** |
| 0.40 | 0.447902 | 0.359578 | 0.802805 | 0.443541 |
| 0.45 | 0.587082 | 0.276069 | 0.470239 | 0.196176 |

> **Theorem S23.1 (Round-Metric No-Go).** In the **round** metric, no member of the one-parameter I\_h truncation family satisfies σ \= ρ \= 1\.  
>   
> **Proof.** By (iii) and (vi), ρ and σ are each strictly decreasing on (0, ½); hence each equation ρ \= 1, σ \= 1 has **at most one** root. Each has **at least one** root by the intermediate value theorem, since ρ(0.25) \= 3.477 \> 1 \> 0.803 \= ρ(0.40) and σ(0.25) \= 1.808 \> 1 \> 0.444 \= σ(0.40). Write t\_ρ, t\_σ for these unique roots. At the single rational point t \= 7/20, **σ(7/20) \= 0.7646874528084178 \< 1 \< 1.3049735712612953 \= ρ(7/20)**. Strict monotonicity converts these two inequalities into **t\_σ \< 7/20 \< t\_ρ**, so t\_σ ≠ t\_ρ and no t satisfies both.  
>   
> **Quantitatively:** t\_ρ \= 0.3777168088 with σ \= 0.5757737581 there; t\_σ \= 0.3208400418 with ρ \= 1.7228685918 there; |t\_ρ − t\_σ| \= 5.688 × 10⁻². The equal-area point has the closed form **A₅ \= π/8**, equivalently **cos r₅ \= cot(π/5)·cot(5π/16) \= 0.9196689969**.  
>   
> **\[STATUS: PROVEN, and scoped to the ROUND metric. Monotonicity is analytic; the separator and both IVT brackets are certified by interval enclosure — checks T170, T170a–T170f, T170f-iv, T170f-r, T170f-b, T171–T173, declarations D174, D174a\]**

**The separator is certified, not merely evaluated (new in v1.2).** The external review of v1.1 observed, correctly, that calling a high-precision floating-point evaluation "certified" while simultaneously leaving gate F-S23.9 open is not a position one can hold. Version 1.2 removes the tension by doing the enclosure. All six closed-form quantities at t \= 7/20 are evaluated in mpmath's **interval context** at 50 digits, with arccos and arcsin rewritten through atan2 so that every operation is an outer-rounded interval operation.

**Table 3.0.** Rigorous outer enclosures at t \= 7/20. Every entry is an interval, not a rounded number.

| quantity | enclosure | width |
| ----- | ----- | ----- |
| r₅ | \[0.3702459995538744722356, 0.3702459995538744722356\] | 3.3 × 10⁻⁵¹ |
| A₅ | \[0.3298305762331100822820, 0.3298305762331100822820\] | 1.3 × 10⁻⁴⁹ |
| l₅₆ | \[0.4286481590486501596092, 0.4286481590486501596092\] | 1.0 × 10⁻⁵⁰ |
| l₆₆ | \[0.3666567186863415585458, 0.3666567186863415585458\] | 4.7 × 10⁻⁵¹ |
| **σ(7/20)** | **\[0.7646874528084177306485, 0.7646874528084177306486\]** | **4.9 × 10⁻⁵⁰** |
| **ρ(7/20)** | **\[1.3049735712612953801793, 1.3049735712612953801794\]** | **7.5 × 10⁻⁴⁹** |

Hence **sup σ(7/20) \< 765/1000 \< 1** and **inf ρ(7/20) \> 1304/1000 \> 1**, both rigorously. The two bracketing evaluations used by the existence half of the proof are enclosed as well: at t \= 1/4 both σ and ρ are rigorously above 1, at t \= 2/5 both are rigorously below 1\. **Gate F-S23.9 is CLOSED-PASS.** **\[Checks T170f-iv, T170f-r, T170f-b\]**

One residual caveat is recorded rather than hidden. The monotonicity step is carried by the *analytic* argument (i)–(vi) above — sign of a derivative read off from the structure of the closed forms — and the companion's grid evaluation of dρ/dt and dσ/dt (check T170d) is a numerical corroboration of that argument, not its substitute. It is the algebra, not the grid, that proves monotonicity.

Theorem S23.1 says nothing about metrics other than the round one, and §3.3 shows why that scope restriction is the whole story.

## §3.3 Lemma S23.2a — what conformal freedom cannot move

The external review raised the sharpest objection in the paper: the v1.0 companion held the dual vertices fixed and integrated conformal lengths along **round** great circles, neither of which is obviously legitimate once the metric changes. This subsection answers that objection with a proof rather than a demotion, and finds that three quarters of it dissolves and one quarter survives and is measurable.

> **Lemma S23.2a (Symmetry-Forced *Stationary* Geodesy).** Let g \= e^{2φ}g\_round with φ any I\_h-invariant function on S². Then: **(i)** The pentagon circumcentre (an icosahedron vertex) and the hexagon circumcentre (an icosahedron face centroid) are the **isolated fixed points** of their local stabilisers C₅ᵥ and C₃ᵥ, of orders 10 and 6 respectively. Since these subgroups act by g-isometries, each circumcentre is metric-**independent**. **(ii)** I\_h has **15 mirror planes**. The dual arc d₅₆, the dual arc d₆₆, and the primal (6,6) edge each lie in a mirror plane. The fixed-point set of an isometry is totally geodesic \[21\], so each is a **stationary geodesic of g for every I\_h-invariant φ**, and its g-length is the exact conformal line integral along the round great circle. **(iii)** The primal (5,6) pentagon edge is **not** mirror-contained, though its midpoint lies on a mirror. It is therefore the **only** arc whose g-geodesic differs from the round great circle, and the only residual approximation in the audited discretisation. **\[STATUS: PROVEN — (i) and (ii) are standard Riemannian geometry applied to the explicitly reconstructed |I\_h| \= 120 and its 15 mirrors; checks T170g–T170j, declaration D174b\]**

**Stationary is not the same as minimising, and v1.2 says so (review item 2.3).** "Totally geodesic" delivers a *stationary* geodesic; it does not by itself deliver the *globally shortest* path between the two endpoints. If the DEC primal and dual lengths were read as **metric distances**, that extra step would be needed, because a distance is by definition an infimum over all paths.

This paper resolves the issue by **definition rather than by proof**, and states the definition explicitly so that no downstream paper inherits an unnoticed assumption:

> **Convention D-len.** The DEC primal and dual lengths of the audited discretisation 𝒟 are **defined** as the lengths of the symmetry-selected geodesics of Lemma S23.2a(ii). Under this definition Lemma S23.2a(ii) is exact and nothing further is required.  
>   
> **Gate F-S23.12 (new).** Fires if any paper reinterprets the lengths of Convention D-len as **global metric distances** without first establishing that the mirror-contained geodesics are globally minimising. **\[STATUS: OPEN, and permanent for the corpus.\]**

**Table 3.2a.** Multistart evidence, consistent with global minimality but not a proof of it. **Six** random restarts per arc in an eight-mode normal-displacement basis, Nelder–Mead, at the FULL-mode root. Version 1.2's caption said twelve; the companion ran a different number, and the caption is corrected here (Retraction S23-R16).

| arc | mirror-contained | round-path L | best of 6 starts | relative gain |
| ----- | :---: | ----- | ----- | ----- |
| dual d₅₆ | yes | 1.0783360460 | 1.0783360460 | 9.7 × 10⁻¹³ |
| dual d₆₆ | yes | 0.9506948201 | 0.9506948201 | 3.7 × 10⁻¹³ |
| primal (6,6) | yes | 0.6054445722 | 0.6054445722 | 5.7 × 10⁻¹² |
| primal (5,6) | **no** | 0.6867377186 | 0.6830582147 | **5.4 × 10⁻³** |

No shorter path is found for any mirror arc; the non-mirror arc improves by 0.53 %, as Lemma S23.2a(iii) predicts. This is **evidence**, not proof: the displacement basis is finite and the optimiser is local. **\[STATUS: COMPUTED — check T170k, declaration D174c\]**

**Table 3.2.** The residual approximation, measured. Conformal length of the round great-circle path against the true g-geodesic, at the reference conformal profile (a \= 0.6866, w \= 0.60), geodesic obtained by minimising conformal length over normal displacements in a six-mode sine basis.

| arc | mirror-contained | round-path length | true geodesic | relative gap |
| ----- | :---: | ----- | ----- | ----- |
| primal (5,6) | **no** | 0.6860279181 | 0.6823682092 | **5.33 × 10⁻³** |
| primal (6,6) | yes | 0.6051013996 | 0.6051013996 | 4.56 × 10⁻¹¹ |
| dual d₅₆ | yes | 1.0773110386 | 1.0773110385 | 1.37 × 10⁻¹¹ |
| dual d₆₆ | yes | 0.9502277232 | 0.9502277232 | 0.00 |

The three mirror rows are at solver noise, which is Lemma S23.2a(ii) confirmed numerically rather than assumed, and is exact under Convention D-len. The single non-mirror row carries the entire systematic error of the conformal computation, and it is **0.53 %**, not the 10⁻¹⁴ that v1.0 implied. Recomputing the root with the true (5,6) geodesic in place of the round arc does **not** destroy it. Version 1.2 quoted this from an off-line calculation the companion did not perform; **v1.3 computes it in-suite** (entry T170m, kind X). Against the round-arc root t\* \= 0.332282802, a\* \= 0.687823981 on the same grid, the geodesic-corrected root is

**t\* \= 0.332756333,  a\* \= 0.681385753,  (σ, ρ) \= (1.000000000, 1.000000000)**,

a systematic shift of Δt\* \= 4.74 × 10⁻⁴ and Δa\* \= 6.44 × 10⁻³. **Existence survives the correction; only digits move.** This is the quantitative content of gate F-S23.11.

## §3.4 The quadrature audit, and the retraction of the published residual

Version 1.0 reported "σ \= ρ \= 1 exactly (residual 1.6 × 10⁻¹⁴)". The review is right that this is a **solver** residual on an approximate functional, and says nothing about the accuracy of the underlying continuum problem. Version 1.1 measures the difference.

**Table 3.3.** Convergence of the root under refinement of the arc quadrature (n\_arc midpoint panels) and the area quadrature (n\_area centroid subdivisions), profile width w \= 0.60.

| n\_arc | n\_area | t\* | a\* |
| ----- | ----- | ----- | ----- |
| 24 | 12 | 0.3323285058 | 0.6905212930 |
| **48** | **18** | **0.3323071505** | **0.6891576432** ← v1.0 published |
| 96 | 36 | 0.3322789294 | 0.6876216840 |
| 192 | 64 | 0.3322650775 | 0.6868824810 |
| **384** | **96** | **0.3322588460** | **0.6865529707** ← FULL-mode reference |

The root converges — successive increments in t\* fall as 2.1, 2.8, 1.4, 0.6 × 10⁻⁵ — so **existence is robust and the digits are not**. Re-evaluating the v1.0 published root at the FULL-mode reference grid (384, 96\) gives (σ, ρ) \= (1.0000136137, 0.9979286437), a **true geometric residual of 2.07 × 10⁻³**.

**The residual figure is resolution-dependent, and v1.2 stops pretending otherwise.** It is not a constant of nature but a property of the grid one compares against: (192, 64\) returns 1.81 × 10⁻³ and the reduced FAST grid (96, 32\) returns 1.06 × 10⁻³. Version 1.1 hard-coded a single value in the companion docstring while the manuscript quoted another. In v1.2 the companion computes and prints the figure together with the grid and the mode that produced it, and this manuscript quotes the **FULL-mode value, 2.07 × 10⁻³ at (384, 96\)**. What is invariant across all three grids, and is the actual content of the retraction, is that the true residual exceeds the quoted 1.6 × 10⁻¹⁴ by **eleven orders of magnitude**.

> **Retraction S23-R8 (new in v1.1).** "σ \= ρ \= 1 exactly, residual 1.6 × 10⁻¹⁴" is **RETRACTED**. That figure is a fsolve residual on a fixed-quadrature functional. The honest figures are: quadrature drift of the published root Δt\* \= 4.8 × 10⁻⁵, Δa\* \= 2.6 × 10⁻³; true geometric residual of the published root 2.07 × 10⁻³ at the FULL reference grid (resolution-dependent, §3.4); additional systematic shift from the (5,6) geodesic correction Δt\* \= 4.7 × 10⁻⁴. **\[Check T175b\]**

## §3.5 Theorem S23.2 — conformal reachability, re-proved by the intermediate value theorem

With Lemma S23.2a fixing the geometry and §3.4 fixing the error budget, the reachability claim can be re-established without appeal to any solver residual.

**Definition (the audited discretisation 𝒟).** I\_h combinatorics of K\_TI(t); symmetry-forced dual vertices (Lemma S23.2a(i)); mirror-geodesic arcs for d₅₆, d₆₆ and the (6,6) edge under **Convention D-len** (Lemma S23.2a(ii) and §3.3); round-arc approximation for the (5,6) edge, with error measured in Table 3.2; midpoint arc quadrature at n\_arc and centroid area quadrature at n\_area, at the orders of Table 3.3.

Version 1.1 stated a single theorem with the status "PROVEN-CONDITIONAL on (D1)–(D3), each VERIFIED". The external review is right that this conflates two different things: a piece of pure analysis, which is genuinely proved, and a claim about a specific discretised functional, whose hypotheses are checked on a finite grid. Version 1.2 separates them.

> **Lemma S23.2b (Abstract IVT Reachability).** Let σ\_w, ρ\_w : \[t₀, t₁\] × \[a₀, a₁\] → ℝ and suppose **(D1)** σ\_w and ρ\_w are continuous; **(D2)** σ\_w(·, a) is strictly decreasing in t for **every** a ∈ \[a₀, a₁\]; **(D2b)** σ\_w(t₀, a) \> 1 \> σ\_w(t₁, a) for **every** a ∈ \[a₀, a₁\] *(uniform root bracketing)*; **(D3)** g\_w(a₀) \> 0 \> g\_w(a₁), where g\_w(a) := ρ\_w(t\_w(a), a) − 1 and t\_w(a) is the root of σ\_w(·, a) \= 1\. Then there is a\* ∈ (a₀, a₁) with σ\_w \= ρ\_w \= 1 exactly. **Proof.** By **(D2b)** and (D1), σ\_w(·, a) − 1 changes sign on \[t₀, t₁\], so t\_w(a) **exists**; by **(D2)** it is **unique**. By (D1) and strict monotonicity it depends continuously on a, hence g\_w is continuous; by (D3) and the intermediate value theorem g\_w has a zero. **\[STATUS: PROVEN-CONDITIONAL on (D1), (D2), (D2b), (D3). This is pure analysis and contains no numerics.\]**

*(Retraction S23-R15, new in v1.3, against ZS-S23 v1.2 §3.5. The v1.2 proof read "By (D2), t\_w(a) exists and is unique for each a." **Strict monotonicity delivers uniqueness, not existence** — a strictly decreasing function may remain above 1 on the whole interval, in which case no root exists and g\_w is undefined. Hypothesis **(D2b)** is added to supply existence. The omission was a genuine gap in the pure-analysis half of the argument, not merely in its application. The companion now tests (D2b) over the entire amplitude grid at both widths: min\_a σ(0.28, a) \= 1.414801 \> 1 \> 0.559944 \= max\_a σ(0.40, a). **\[Check T176a2\]**)*

> **Application S23.2 (Conformal Reachability within 𝒟).** For the audited conformal profile families, Lemma S23.2b applies on \[0.28, 0.40\] × \[0, 0.90\] and yields a\*, t\* with σ \= ρ \= 1\. **\[STATUS, graded by hypothesis: (D1) continuity — VERIFIED; the discretised functionals are finite compositions of continuous maps, the only non-smooth ingredient being a max over twelve axes, which is continuous. (D3) endpoint signs — VERIFIED; two evaluations per profile, far from zero (Table 3.4). (D2) strict monotonicity over the whole rectangle — COMPUTED; see Table 3.4a. (D2b) uniform root bracketing over the whole amplitude interval — COMPUTED; checked on the 13-point amplitude grid at both widths, not enclosed. Therefore the application carries the weakest of these, and its honest status is COMPUTED, not proof strength. — entries T176a, T176a.45, T176a2, T176b.60, T176b.45, T176, all kind X\]**

*(Retraction S23-R12, new in v1.2, against ZS-S23 v1.1 §3.5: the status line "PROVEN-CONDITIONAL on (D1)–(D3), each VERIFIED" is **RETRACTED**. (D2) is a statement about a continuum of amplitudes and was checked at three, later thirteen, sampled amplitudes; a finite sample does not verify a global monotonicity claim. The lemma keeps its status; the application is demoted to COMPUTED.)*

**Table 3.4a.** What the (D2) and (D2b) evidence actually covers. Grid over \[0.28, 0.40\] × \[0, 0.90\], monotonicity quadrature (48, 18). **Both rows are computed by the companion in v1.3**; v1.2 tabulated the w \= 0.45 row but computed only w \= 0.60.

| profile w | grid | worst secant ∂σ/∂t | max |∂²σ/∂t²| sampled | ½·curv·Δt | t-direction | (D2b) min\_a σ(0.28,a) | (D2b) max\_a σ(0.40,a) | a-direction |
| ----- | :---: | ----- | ----- | ----- | :---: | ----- | ----- | :---: |
| 0.60 | 17 × 13 | −5.702152 | 92.088 | 0.34533 | **COVERED** | 1.414801 | 0.528904 | sampled only |
| 0.45 | 17 × 13 | −5.702152 | 86.528 | 0.32448 | **COVERED** | 1.414801 | 0.559944 | sampled only |

The t-direction *is* covered between grid points: the sampled curvature bound gives a worst-case interpolation error of 0.345, an order of magnitude below the monotonicity margin of 5.70, so ∂σ/∂t \< 0 holds on the whole t-interval at each sampled amplitude. (D2b) holds with a wide margin at both widths. The **a-direction is not covered**: no bound on ∂²σ/∂t∂a is computed. Closing (D2) and (D2b) would need either an interval enclosure of ∂\_t σ over the rectangle or an analytic Lipschitz bound in a; both are registered at gate F-S23.13.

*(Retraction S23-R17, new in v1.3. Version 1.2 attributed the missing a-direction coverage to the conformal potential being "only piecewise smooth in a because it takes a maximum over twelve axes". **That attribution is wrong.** The potential φ(p) \= a·exp(−(d(p)/w)²) depends on the amplitude a **linearly, hence smoothly**. The maximum over twelve axes is non-smooth in the **spatial** argument p, and therefore in t as cell vertices cross Voronoi boundaries of the twelve pentagon axes — not in a. The obstruction to covering the a-direction is simply that no mixed-derivative bound was computed, which is a gap in effort, not in regularity.)*

**Table 3.4.** The bracketed roots, on the **stated IVT working grid (96, 32\)**. All values are printed by the FULL-mode companion; v1.2 quoted (192, 64\) numbers that its own companion did not produce (Retraction S23-R16).

| profile family | w | IVT root a\* | t\* | (σ, ρ) attained |
| ----- | ----- | ----- | ----- | :---: |
| 5-fold bump | 0.60 | 0.6878239814 | 0.3322828018 | (1.0000000000, 1.0000000000) |
| 5-fold bump | 0.45 | 0.5192547298 | 0.3308303516 | (1.0000000000, 1.0000000000) |
| 3-fold bump | 0.50 | **−0.598021224** | 0.336285762 | (1.0000000000, 1.0000000000) |
| 3-fold bump | 0.70 | **−0.877189324** | 0.336280556 | (1.0000000000, 1.0000000000) |

**On the two grids, stated once so they are not confused.** The **quadrature-table grid** of Table 3.3 runs out to (384, 96\) and exists to measure how the root moves under refinement; it is what produces the honest residual of §3.4. The **IVT working grid** is (96, 32\) and exists to give the existence argument a single fixed discretisation. Running the IVT bracketing at (384, 96\) costs some 390 s and buys nothing epistemically, since 𝒟 is defined at a stated resolution and the existence claim is a claim about 𝒟. Version 1.2 left this distinction implicit and consequently tabulated numbers from a third grid, (192, 64), that neither block computed.

The third and fourth rows are new in v1.1 and are the anti-artefact control. They use a **structurally different** I\_h-invariant profile — a bump on the twelve 3-fold hexagon axes rather than the twelve 5-fold pentagon axes — and reach the orbit-blind point at **negative** amplitude. Reachability is therefore not a property of the pentagon-axis ansatz. **\[Check T177b\]**

## §3.6 Non-uniqueness, the local branch, and what "continuum" may and may not mean

Version 1.0 wrote that two distinct solutions establish a continuum. The review is right that this does not follow, and v1.1 separates three statements of decreasing strength.

> **Proposition S23.2b (Non-Uniqueness).** Four solutions in two structurally distinct profile families are exhibited, with t\* spread 5.46 × 10⁻³ and a\* spanning both signs, from −0.8767 to \+0.6869. **Non-uniqueness within 𝒟 is established.** **\[STATUS: COMPUTED — check T177a\]**  
>   
> **Proposition S23.2c (Local C¹ Branch).** The Jacobian ∂(σ, ρ)/∂(t, a) is nonsingular and well conditioned at both audited roots: det J \= \+6.9976, cond J \= 23.57 at w \= 0.60; det J \= \+9.1615, cond J \= 17.26 at w \= 0.45. By the implicit function theorem \[22\], the solution set therefore contains a locally unique **C¹ arc** w ↦ (t\*(w), a\*(w)) through each root. A one-parameter continuum of solutions exists locally. **\[STATUS: DERIVED-CONDITIONAL on the numerically computed Jacobian — check T177\]**  
>   
> **Conjecture S23.2d (Global Continuum).** The orbit-blind point is realised on a continuum of solutions over the full infinite-dimensional space of I\_h-invariant conformal profiles, one per profile. **\[STATUS: CONJECTURE. Missing: a global continuation argument or an interval enclosure of the Jacobian along the branch. Gate F-S23.10.\]**

*(Retraction S23-R9, new in v1.1, against ZS-S23 v1.0 §3.3 and companion check T177: "the solutions are distinct, so (1,1) is realised on a CONTINUUM of metrics" is **RETRACTED**. Two points do not make a continuum. The correct ladder is Proposition S23.2b for non-uniqueness, Proposition S23.2c for a local arc, and Conjecture S23.2d for the global statement.)*

> **Corollary S23.2e (Metric Non-Identifiability).** Within the audited discretisation 𝒟, multiple convergent roots in two structurally distinct profile families provide **strong evidence** that the metric route is non-identifying — that it does not select between Class MF and Class M. A **proof** requires closure of gates F-S23.13 (certified (D2)/(D2b)) and F-S23.11 (full conformal DEC). **\[STATUS: COMPUTED / HYPOTHESIS-strong.\]**

*(Retraction S23-R14, new in v1.3, against ZS-S23 v1.2 §3.6. Version 1.2 graded this corollary **DERIVED** while grading the Application it rests on **COMPUTED**, and its own Epistemic Status Legend defines COMPUTED as carrying **no proof weight**. A DERIVED consequence cannot be drawn from a premise with no proof weight; the two gradings could not both stand. The corollary is demoted. The substance is unchanged and remains the paper's operative conclusion — four roots, two structurally distinct families, amplitudes of both signs, robust under a 5 × 10⁻³ systematic error and under quadrature refinement — but it is evidence, and v1.3 calls it evidence.)*

The demotion is worth one sentence of interpretation, because it is easy to over-read. Non-identifiability is a claim about the **abundance** of solutions, and abundance is the kind of claim that survives coarse error bars far better than a specific value would: nothing in the error budget of §3.4 could plausibly convert four exhibited roots into zero. That is why the corollary is graded **HYPOTHESIS-strong** rather than merely COMPUTED. But "very likely true" is not "proved", and the S-line has been damaged before by treating the two as interchangeable.

**Corrected verdict, replacing ZS-S22 v1.2's.** Version 1.2 declared that the geometric route fires Outcome B and selects Class M. That verdict is **RETRACTED (S23-R3, and ZS-S22 Retraction S22-R6)**. The corrected verdict is that the geometric route is **non-identifying** — the same shape ZS-S20 found at the level of the measure, recurring one level up at the level of the metric. This means no metric argument can settle the class either way, and the burden falls entirely on the dynamical route of §4 — where, as §4.3 records, it does not discharge either.

---

# §4. Step A — the Clock Route, and Why It Also Does Not Close

## §4.1 The corpus has met a binary of this shape before

**ZS-M44** faced the binary "mode-count measure versus metric measure" for the **Q** \= 11 register, and its exact arrowhead inverse-eigenvalue solve **excluded the metric benchmark to 0.45 %** in favour of mode-count democracy. **ZS-F38 Theorem F38.T1′** then supplied the derivation rather than the evidence:

> If the one-tick register transition P is an irreducible doubly stochastic (unital) matrix on the **Q** slots, then its unique stationary measure is **ρ\_Q \= I\_Q/Q**, the democratic (mode-count) measure, and the Cesàro time average of every slot observable converges to the democratic average. \[ZS-F38, mathematics IMPORTED-PROVEN via Perron–Frobenius and Birkhoff–von Neumann; physical instance DERIVED-CONDITIONAL on (H-CLK) ∧ (H-mix).\]

The Class MF / Class M dichotomy of Theorem S22.4 is the same binary at the carrier level: mode-count (orbit-blind counting) against metric (area and dual-length).

## §4.2 The transfer, and the axiom it needs

**Axiom (Z-A3) — Carrier-Clock Identification.** The measure carried by the Z-sector carrier cells is the stationary measure of the register clock.

> **Theorem S23.3 (Measure Transfer).** Under (Z-A3) together with ZS-F38's (H-CLK) ∧ (H-mix), the carrier cell measure is the uniform measure ρ\_Q \= I\_Q/**Q**. Hence β\_f is constant across faces and m\_e is constant across edges, so **σ \= ρ \= 1**, and (Z-A1) holds. **\[STATUS: DERIVED-CONDITIONAL on (H-CLK) ∧ (H-mix) ∧ (Z-A3) — checks T180–T182, declaration D183. See §4.3: (Z-A3) carries an unresolved objection and this status is an upper bound on what the transfer delivers.\]**

## §4.3 The density-versus-rate objection, and the ZS-F40 cross-audit

This is the weakest joint in the paper and it is stated before the conclusion rather than after it.

**The objection.** ρ\_Q \= I\_Q/**Q** is a **stationary probability measure**. M₁⁻¹ is an **electric stiffness**, i.e. a *rate*, and M₂ is a face measure entering the action. A uniform stationary distribution does **not** determine the generator's rates: distinct doubly stochastic transition matrices share the uniform stationary measure and have different spectral gaps. So register democracy **supports** uniformity but does not **derive** M₁ ∝ I and M₂ ∝ I. ZS-S20 already named exactly this step an unresolved physical bridge, **(H-PSM-2)**, and recorded that the map from the gauge-invariant Hilbert space down to the 1342-component register is not defined. **\[STATUS: OPEN — this paper does not resolve it; gate F-S23.4\]**

**Consequence for the axiom count, stated once and without contradiction.** ZS-S22 v1.2 wrote that Theorem S23.3 "reduces the corpus's axiom count by one". **That is RETRACTED (S23-R4).** (Z-A1) is not eliminated; it is **replaced** by a higher-layer identification axiom (Z-A3) of the form *stationary state ↔ cellular stiffness*, which is precisely the density-versus-rate identification ZS-S20 flagged. The honest accounting is a **relocation, not a reduction: the corpus axiom count is unchanged.**

What the relocation does buy, stated exactly and without inflation. (Z-A1) was, through ZS-S19, ZS-S20, ZS-S21 and ZS-S22 v1.1, an **isolated postulate** with no derivation anywhere in the corpus, and ZS-S21 §15.4 called it "the single load-bearing choice of the S-line". After Theorem S23.3 the same statement has a **proof-shaped parent**: it is an instance of a proved unique-ergodicity selection theorem, carrying exactly the conditionality that theorem already carries, plus one new identification (Z-A3) which is adjacent to a named, pre-existing gate. That is a **structural improvement in the corpus's dependency graph, not a decrement of its axiom count**, and the two must not be conflated.

*(Retraction S23-R10, new in v1.1, against ZS-S23 v1.0 §4.3: the sentence "That is a genuine reduction in the corpus's axiom count, not a relabelling" is **RETRACTED**. It directly contradicted the paragraph three lines above it, which correctly said "a relocation, not a reduction". The relocation reading is the one retained. The stale cross-references in the same subsection — "Theorem S22.12", "Theorem S22.11", "§19.3" — are corrected to Theorem S23.3, Theorem S23.1 and §4.4 respectively.)*

**The ZS-F40 cross-audit.** ZS-F38's T1′ is itself conditional on (H-CLK) ∧ (H-mix). ZS-F40's attempted physical discharge of the clock returned a **CLOSED-NEGATIVE** result: the Frobenius deviation between the cyclic shift and the canonical clock is exactly **√2**. Any use of F38 in the S-line must therefore say which clock identification it is invoking and how that differs from the one F40 refused. This paper invokes the *abstract* T1′ statement — an irreducible unital transition on **Q** slots — and makes **no** claim that the physical clock of ZS-F40 is that transition. Whether (Z-A3) can be satisfied by a clock consistent with F40's √2 refusal is **OPEN**, gate F-S23.5. Writing, as ZS-S22 v1.2 did, that "the corpus has already solved the identical binary" is an over-claim and is **RETRACTED (S23-R5)**.

Nor does Theorem S23.3 contradict Theorem S23.1: the two routes genuinely disagree, and §4.4 says what that means.

## §4.4 Where the two routes leave the class question

| route | mechanism | verdict | status |
| ----- | ----- | ----- | ----- |
| **Metric** (§3) | ⋆ in 2D sees the metric only through the area measure; conformal factor is an infinite-dimensional freedom | **does not select — under-determines**, on strong computed evidence | Corollary S23.2e, **COMPUTED / HYPOTHESIS-strong**, resting on Lemma S23.2b (PROVEN-CONDITIONAL) \+ Application S23.2 (COMPUTED) \+ Proposition S23.2b (COMPUTED) |
| **Clock** (§4) | register clock's unique stationary measure is democratic | **would select Class MF**, but only across the density→rate identification | DERIVED-CONDITIONAL on (H-CLK) ∧ (H-mix) ∧ (Z-A3), with (Z-A3) itself OPEN per §4.3 |

**Neither route closes the class question.** The metric route is non-identifying on strong computed evidence; the clock route is identifying only if one grants an axiom that ZS-S20 has already flagged as an unresolved bridge and that ZS-F40's √2 refusal has not been reconciled with. ZS-M44's 0.45 % arrowhead solve is the corpus's only empirical discriminator and it favours mode-count over metric, but it is evidence, not derivation, and it is evidence about the **register**, not about the **carrier**.

The correct statement of where the S-line stands is therefore: **the class question is OPEN, and it is now OPEN in one specific place — the density-versus-rate identification (Z-A3) / (H-PSM-2).** That is a substantially better position than the S-line occupied before ZS-S22, and substantially worse than ZS-S22 v1.2 claimed. **\[STATUS: declaration D184\]**

---

# §5. Step B — the Central-Hessian Theorem

Step B asked whether the ZS-S21 quadratic operator is really the identity-neighbourhood Hessian of whatever group-valued action Step A produces. The answer is yes in the precise sense of §5.2, it does not require knowing which action Step A produces, and it does require single-plaquette locality.

> **Theorem S23.4 (Central-Hessian Theorem).** Let G be a compact **simple** Lie group with Lie algebra 𝔤, and let Φ : G → ℝ be C² and central, Φ(hgh⁻¹) \= Φ(g). *(C² suffices for everything below except the order of the Taylor remainder; see the regularity note.)* Then the Hessian of Φ at the identity is Ad-invariant, and since 𝔤 is simple the space of Ad-invariant symmetric bilinear forms on 𝔤 is one-dimensional (Schur). Hence **Hess Φ|₁ \= κ\_Φ ⟨·,·⟩\_K** for a single real number κ\_Φ, where ⟨·,·⟩*K is the Killing form. **Corollary.** For any plaquette action S\_cell\[U\] \= Σ\_p Φ\_p(U\_p) with U\_p \= ∏*{e ⊂ ∂p} U\_e^{ε\_pe} and each Φ\_p central, writing U\_e \= exp(i a A\_e) and using Baker–Campbell–Hausdorff, U\_p \= exp(i a (B A)\_p \+ O(a²)), so **S\_cell\[e^{iaA}\] \= S\_cell\[𝟙\] \+ (a²/2) ⟨A, Bᵀ diag(κ\_p) B A⟩ \+ o(a²)**  for Φ\_p ∈ C², and with remainder **O(a³)** if Φ\_p ∈ C³. The identity-neighbourhood Hessian is therefore the **edge-space operator** H\_edge \= B₂ᵀ diag(κ\_p) B₂, with β\_p \= κ\_p. Its relation to the ZS-S21 face operator is stated precisely in §5.2, and it is **not** equality.  
>   
> **\[STATUS: PROVEN for the Hessian's form, gauge-group independent for simple G; the *applicability* to the ZS-S14 reduction is PROVEN-CONDITIONAL on single-plaquette locality (H-W) — checks T190, T191, T192, declaration D193\]**

**Regularity note (Retraction S23-R18, new in v1.3).** Versions 1.0 to 1.2 assumed Φ ∈ C² and wrote the expansion with remainder O(a³). **C² gives only o(a²)**; an O(a³) remainder needs Φ ∈ C³, or at least a bounded third derivative on a neighbourhood of the identity. Either statement may be used and both are recorded above. Nothing downstream changes: the Hessian **Hess Φ|₁ \= κ\_Φ ⟨·,·⟩\_K** is a statement about the second derivative alone and is fully delivered by C², and every result of §5 concerns that quadratic form. The Wilson action and the truncated character sums of Table 5.1 are real-analytic, so for the actions actually audited the O(a³) form holds; the correction matters only for the general statement.

**Table 5.1.** Numerical audit on SU(3) in the orthonormal basis T^a \= λ^a/2, Tr(T^aT^b) \= ½δ^{ab} (residual 1.1 × 10⁻¹⁶). The "heat kernel" entries are a **truncated character sum** over six low SU(3) irreps, not the full heat kernel; the paper calls them a proxy throughout.

| central action Φ | ‖Hess − κI‖/κ | κ \= Φ″(0) |
| ----- | ----- | ----- |
| Wilson, β \= 1 | 0.000 × 10⁰ | 0.16666666 |
| Wilson, β \= 2.7 | 0.000 × 10⁰ | 0.44999999 |
| truncated heat-kernel proxy, t \= 0.4 | 0.000 × 10⁰ | 0.33918490 |
| truncated heat-kernel proxy, t \= 1.1 | 0.000 × 10⁰ | 0.25061624 |
| **control: Φ(U) \= Re(U₀₀)², non-central** | **1.000 × 10⁰** | — |

The control row is the point: the proportionality is a consequence of centrality, not an artefact of the numerics.

## §5.1 Lemma S23.5 — centrality is forced by gauge invariance

> **Lemma S23.5 (Centrality is Forced).** Let the cellular action contain a single-plaquette term Φ\_f(U\_f), where U\_f is the ordered product of link variables around f based at a vertex w. A gauge transformation g\_w at that vertex acts by **U\_f ↦ g\_w U\_f g\_w⁻¹**. Hence gauge invariance of the term is **equivalent** to Φ\_f(gUg⁻¹) \= Φ\_f(U) for all g ∈ G, which is the definition of a class function. Centrality is therefore not an assumption on the reduction; it is forced by gauge invariance together with single-plaquette locality. **\[STATUS: PROVEN — checks T195, T196, declaration D197\]**

**Table 5.2.** Numerical confirmation of the converse direction, 2000 random conjugations on SU(3).

| plaquette functional | max |Φ(gUg⁻¹) − Φ(U)| | gauge invariant |
| ----- | ----- | :---: |
| Wilson | 4.441 × 10⁻¹⁶ | yes |
| truncated heat-kernel proxy, t \= 0.7 | 8.235 × 10⁻¹² | yes |
| **Re(U₀₀)², non-central** | **8.742 × 10⁻¹** | **no** |

> **Corollary S23.5a.** Combining Lemma S23.5 with Theorem S23.4: any gauge-invariant **single-plaquette** cellular action — whatever the explicit face-and-prism integration of ZS-S14 produces — has identity-neighbourhood Hessian H\_edge \= B₂ᵀ diag(κ\_p) B₂ with κ\_p \= Φ\_p″(0). The constructive half of Step A is therefore not required for the *form* of the Hessian, only for the *values* κ\_p. **\[STATUS: PROVEN-CONDITIONAL on single-plaquette locality (H-W).\]**

**The conditionality is real and ZS-S22 v1.2 dropped it.** Gauge invariance forces centrality; it does **not** forbid gauge-invariant *multi-plaquette* terms — products of holonomies over adjacent faces, or larger Wilson loops — which would add terms outside B₂ᵀ diag(κ\_p) B₂. Excluding them is exactly the content of (H-W), which ZS-S21 registered as OPEN and which this paper does not close. Version 1.2's description of Step B as "closed unconditionally" is **RETRACTED (S23-R6)**; the correct status is PROVEN-CONDITIONAL on (H-W).

## §5.2 Theorem S23.6 — the correct relation is nonzero-isospectral, not equality

ZS-S22 v1.2 wrote that the identity-neighbourhood Hessian "is exactly Δ\_{S21}". **That is a type error and is RETRACTED (S23-R1).** The Hessian is an operator on **edge** space,

**H\_edge \= M₁^{−1/2} B₂ᵀ M₂ B₂ M₁^{−1/2}**,  dimension E × E \= **90 × 90** on K\_TI,

whereas the ZS-S21 operator is the **face** operator

**Δ₂ \= M₂^{1/2} B₂ M₁^{−1} B₂ᵀ M₂^{1/2}**,  dimension F × F \= **32 × 32**.

These act on different spaces and cannot be equal. Writing X \= M₂^{1/2} B₂ M₁^{−1/2}, they are XᵀX and XXᵀ.

> **Theorem S23.6 (Edge–Face Isospectrality).** H\_edge and Δ₂ share their entire **nonzero** spectrum, with multiplicities. Their kernels differ in dimension by E − F \= 58\. **\[STATUS: PROVEN (XᵀX and XXᵀ) \+ VERIFIED — checks T198, T199\]**

**Table 5.3.** Verified at three weight points on K\_TI.

| (σ, ρ) | edge operator | face operator | rank | max spectral deviation |
| :---- | :---: | :---: | ----: | ----: |
| (1.0000, 1.0000) | 90 × 90 | 32 × 32 | 31 | 1.07 × 10⁻¹⁴ |
| (0.8940, 1.5294) | 90 × 90 | 32 × 32 | 31 | 7.11 × 10⁻¹⁵ |
| (1.3000, 0.7000) | 90 × 90 | 32 × 32 | 31 | 1.15 × 10⁻¹⁴ |

The correct sentence is: **the gauge-fixed quadratic edge operator of the group-valued action is nonzero-isospectral to the ZS-S21 face operator.** Every spectral statement of ZS-S21 and ZS-S22 survives this correction unchanged, because all of them concern nonzero eigenvalues; only the identification of the operators is withdrawn.

## §5.3 Consequences, and what λ₁ is

1. **Step B does not depend on the value of Step A.** Whatever positive central class function the ZS-S14 integration produces, its quadratic content is B₂ᵀ diag(κ\_p) B₂. The Wilson form is not privileged. Conditional on (H-W).  
2. **The orbit-weight question is exactly the question of the κ\_p.** Sections §3 and §4 are therefore not side issues; they are the whole remaining content of (Z-A0)/(Z-A1) at the action level, and neither closes it.  
3. **λ₁ acquires a precise but modest meaning.** λ₁ \= 1.2428416164 is the lowest nonzero eigenvalue of the identity-neighbourhood Hessian of a gauge-invariant single-plaquette cellular action with counting weights. ZS-S22 v1.2 further asserted that λ₁ *is* the weak-coupling limit of the finite-carrier quantum gap. **That is RETRACTED (S23-R7).** Passing from a classical quadratic form to the first energy gap of the quantum Hamiltonian requires gauge fixing and zero-mode removal, uniqueness of the vacuum, an action-level normalisation of r, control of anharmonic corrections, and exclusion of tunnelling between minima — none of which is carried out here or in ZS-S24.

>   
> **λ₁ is the lowest quadratic normal-mode eigenvalue candidate of the group-valued action, conditional on its reduction to the ZS-S21 quadratic form. It is NOT established as the weak-coupling limit of the quantum gap.** **\[STATUS: DERIVED-CONDITIONAL for the classical statement; the semiclassical bridge is OPEN, gate F-S23.7\]**

---

# §6. Gate Registry, Retraction Register, Non-Claims

**Table 6.1.** Falsification gates. Class M \= mathematical / theoretical collapse (immediate rejection); Class S \= simulation or internal-consistency collapse (revision required); Class O \= observational collapse (rejection by external data).

| gate | fires if | class | status |
| ----- | ----- | :---: | ----- |
| **F-S23.1** *(rewritten in v1.2)* | an independent reimplementation, or a certified evaluation, of the audited discretisation 𝒟 fails to reproduce either the (D3) sign bracket or the existence of a root for one of the four declared profile families | S | **Does not fire.** Four roots reproduced across five quadrature grids. *(The v1.1 wording — "a metric outside the audited family makes σ \= ρ \= 1 impossible" — was logically void: Theorem S23.2 is an existence claim inside named families, and a metric elsewhere admitting no solution contradicts nothing. Retraction S23-R13. Full-DEC destruction of the root is F-S23.11's business, not this gate's.)* |
| **F-S23.2** | any paper cites Theorem S23.1 without its round-metric scope restriction | M | **OPEN and permanent** |
| **F-S23.3** | any paper describes the metric route as *selecting* a class | M | **OPEN and permanent.** ZS-S22 v1.2 did; retracted here |
| **F-S23.4** | the density→rate identification (Z-A3)/(H-PSM-2) is shown to be inconsistent, e.g. two generators with the same stationary measure and demonstrably different carrier stiffness both admissible | M | **OPEN and live.** This is the load-bearing gate of the paper |
| **F-S23.5** | (Z-A3) is shown to require a clock excluded by the ZS-F40 √2 Frobenius refusal | M | **OPEN.** Not reconciled here |
| **F-S23.6** | the explicit face-and-prism integration of the ZS-S14 curvature term does not reduce to a positive central **single-plaquette** function | M | **OPEN.** Would falsify (H-W) and void Corollary S23.5a |
| **F-S23.7** | a semiclassical analysis shows the quantum gap does not approach √(rλ₁) at weak coupling | M | **OPEN.** The semiclassical bridge is not built |
| **F-S23.8** | a gauge-invariant multi-plaquette term is derived from ZS-S14, so H\_edge ≠ B₂ᵀ diag(κ\_p) B₂ | M | **OPEN.** Excluded only by (H-W) |
| **F-S23.9** | a certified interval enclosure of σ(7/20) or ρ(7/20) fails to separate them from 1, so Theorem S23.1's separator is not rigorous | S | **CLOSED-PASS in v1.2.** mpmath interval enclosure at 50 dps gives sup σ \< 765/1000 \< 1 \< 1304/1000 \< inf ρ, widths ≤ 7.5 × 10⁻⁴⁹; the IVT brackets t \= 1/4 and t \= 2/5 are enclosed too — checks T170f-iv, T170f-r, T170f-b |
| **F-S23.10** *(new)* | the solution branch of Proposition S23.2c fails to continue globally, or the Jacobian degenerates somewhere on the profile space | S | **OPEN.** Conjecture S23.2d is not proved |
| **F-S23.11** | a full conformal DEC reconstruction — recomputing the (5,6) geodesic self-consistently at every step rather than perturbatively — destroys the root rather than shifting it | S | **OPEN but expected not to fire.** Perturbative correction shifts the root by Δt\* \= 4.7 × 10⁻⁴ (Table 3.2) |
| **F-S23.12** *(new)* | any paper reads the DEC primal or dual lengths of **Convention D-len** as **global metric distances** without first establishing that the mirror-contained stationary geodesics are globally minimising | M | **OPEN and permanent.** Lemma S23.2a(ii) delivers stationarity, not minimality. Multistart evidence is consistent with minimality (Table 3.2a) but does not close the gate |
| **F-S23.13** | an interval enclosure of ∂\_t σ over \[0.28, 0.40\] × \[0, 0.90\], or an analytic Lipschitz bound on ∂²σ/∂t∂a, shows **(D2)** or **(D2b)** to fail somewhere off the audited grid | S | **OPEN and live.** This is the one gate whose closure would raise Application S23.2 from COMPUTED to VERIFIED, and with it Corollary S23.2e from HYPOTHESIS-strong to DERIVED. Scope widened in v1.3 to cover (D2b) |

**Retraction register.** Retractions S23-R1 to S23-R7 are against ZS-S22 v1.2. S23-R8 to S23-R11 were issued in v1.1 against **v1.0**. S23-R12 and S23-R13 were issued in v1.2 against **v1.1**. S23-R14 to S23-R18 are new in v1.3 and are against **v1.2**.

- **S23-R1.** "The identity-neighbourhood Hessian is exactly Δ\_{S21}" — RETRACTED as a type error. Correct relation: nonzero-isospectral (§5.2).  
    
- **S23-R2.** "In two dimensions β\_f \= 1/A\_f is forced exactly" — RETRACTED. Holds under a cellwise-constant / mass-lumped Whitney reduction (§3.1).  
    
- **S23-R3.** "The geometric route fires Outcome B and selects Class M" — RETRACTED. The metric route under-determines (§3.6).  
    
- **S23-R4.** "Theorem S23.3 reduces the corpus's axiom count by one" — RETRACTED. (Z-A1) is relocated to (Z-A3), not eliminated (§4.3).  
    
- **S23-R5.** "The corpus has already solved the identical binary" — RETRACTED as an over-claim (§4.3).  
    
- **S23-R6.** "Step B closes unconditionally" — RETRACTED. PROVEN-CONDITIONAL on (H-W) (§5.1).  
    
- **S23-R7.** "λ₁ is the weak-coupling limit of the finite-carrier gap" — RETRACTED (§5.3).  
    
- **S23-R8** *(against v1.0)*. "σ \= ρ \= 1 exactly, residual 1.6 × 10⁻¹⁴" — RETRACTED. Solver residual, not geometric; true geometric residual 2.07 × 10⁻³ at the FULL reference grid (§3.4).  
    
- **S23-R9** *(new, against v1.0)*. "The solutions are distinct, so (1,1) is realised on a continuum of metrics" — RETRACTED. Two points do not make a continuum; replaced by Propositions S23.2b, S23.2c and Conjecture S23.2d (§3.6).  
    
- **S23-R10** *(new, against v1.0)*. "That is a genuine reduction in the corpus's axiom count, not a relabelling" — RETRACTED. It contradicted the same subsection's correct "relocation, not a reduction" (§4.3).  
    
- **S23-R11** *(against the v1.0 companion)*. The v1.0 declaration ledger printed "geometric route selects Class M" (D184), "identity-Hessian EXACTLY Delta\_S21" (D193, D197) and "STEP B is closed unconditionally" (D193) — all three already retracted in the v1.0 **body** — together with pre-split theorem numbers S22.12, S22.13, S22.15 and non-existent numbers S24.1, S24.2, S24.3, S24.4, S24.5. A single run therefore emitted mutually contradictory epistemic declarations. The entire ledger is rewritten in v1.1; no declaration now contradicts the body.  
    
- **S23-R12** *(new, against v1.1 §3.5)*. The status line "Theorem S23.2 … PROVEN-CONDITIONAL on (D1)–(D3), each VERIFIED" — RETRACTED. (D2) asserts strict monotonicity for **every** amplitude in a continuum and was checked at three, later thirteen, sampled amplitudes; a finite sample does not verify a global claim. The abstract statement is split off as **Lemma S23.2b** and keeps PROVEN-CONDITIONAL; the **application** to 𝒟 is demoted to **COMPUTED** (§3.5, Table 3.4a, gate F-S23.13).  
    
- **S23-R13** *(new, against v1.1 §6 and the v1.1 companion)*. Four items. **(a)** Gate F-S23.1 as worded in v1.1 was logically void and is rewritten above. **(b)** The v1.1 companion still printed the banner "ZS-S22 v1.2 verification companion" and a declaration D000 naming ZS-S22; both are corrected to ZS-S23. **(c)** The v1.1 manuscript quoted a (384, 96\) row that the v1.1 companion's quadrature grid did not compute; the grid now includes it. **(d)** The v1.1 companion hard-coded a single residual figure in its docstring while running at grids that produce others, and printed "91 executable checks PASS" identically in FAST and FULL modes. The figure is now computed and printed with its grid, and FAST mode announces MODE \= FAST / NON-PUBLICATION VERIFICATION at entry and repeats the warning at exit.  
    
- **S23-R14** *(new, against v1.2 §3.6 and NC-S23.6)*. Corollary S23.2e graded **DERIVED** — RETRACTED, demoted to **COMPUTED / HYPOTHESIS-strong**. A DERIVED conclusion cannot rest on a COMPUTED premise, and v1.2's own legend defines COMPUTED as carrying no proof weight. The clause "what is claimed at proof strength is existence within 𝒟" is deleted from NC-S23.6 for the same reason.  
    
- **S23-R15** *(new, against v1.2 §3.5)*. The proof step "By (D2), t\_w(a) exists and is unique" — RETRACTED as invalid. Strict monotonicity gives uniqueness only; a strictly decreasing function may stay above 1\. Hypothesis **(D2b)**, uniform root bracketing, is added to Lemma S23.2b and tested at check T176a2.  
    
- **S23-R16** *(new, against v1.2 Tables 3.2, 3.2a and 3.4)*. Three table/companion mismatches — RETRACTED and corrected. **(a)** Table 3.4 quoted (192, 64\) roots that neither companion block computed; it now quotes the stated IVT working grid (96, 32). **(b)** Table 3.2a's caption said twelve multistart restarts; the companion ran six, and the caption and values are corrected. **(c)** The geodesic-corrected root was quoted from an off-line run; it is now computed in-suite at entry T170m, giving t\* \= 0.332756333, a\* \= 0.681385753.  
    
- **S23-R17** *(new, against v1.2 §3.5)*. "The conformal potential is only piecewise smooth **in a** because it takes a maximum over twelve axes" — RETRACTED as a misattribution. Dependence on the amplitude is linear and smooth; the max is non-smooth in the **spatial** argument, hence in t at Voronoi boundaries.  
    
- **S23-R18** *(new, against v1.0–v1.2 §5)*. "Φ ∈ C² … \+ O(a³)" — RETRACTED as a regularity error. C² delivers o(a²); O(a³) requires C³ or a bounded third derivative. The Hessian statement itself is unaffected, being a second-derivative statement.

**Non-claims.**

- **NC-S23.1.** No claim that the ZS-S14 reduction has been performed. Only its structural form under a stated quadrature convention is derived.  
- **NC-S23.2.** No claim that (Z-A3) is derived, nor that it is consistent with ZS-F40.  
- **NC-S23.3.** No claim that the class question is settled. It is OPEN, and §4.4 says exactly where.  
- **NC-S23.4.** The "heat kernel" of Tables 5.1 and 5.2 is a **truncated character sum** over six low SU(3) irreps. No claim about the full heat kernel is made.  
- **NC-S23.5.** No numerical constant is derived, predicted or fitted. The companion's checks verify general mathematics and internal reproducibility; they do **not** test the physical justification of (Z-A3).  
- **NC-S23.6** *(amended in v1.3)*. No claim that the conformal roots (t\*, a\*) of Tables 3.3 and 3.4 are accurate beyond the three or four digits supported by Table 3.3. Their status is COMPUTED. **No claim in §3.5 or §3.6 is made at proof strength.** Version 1.2 ended this non-claim with "what is claimed at proof strength is existence within 𝒟", which contradicted its own demotion of Application S23.2 to COMPUTED one page earlier; that clause is **deleted** (Retraction S23-R14). What holds at proof strength in §3 is Theorem S23.1, Lemma S23.2a and Lemma S23.2b — and the last of these is conditional on hypotheses that are themselves only COMPUTED for 𝒟.  
- **NC-S23.7**. No claim that a full self-consistent conformal DEC has been constructed. Lemma S23.2a proves that three of the four arcs and both dual vertices need no reconstruction; the fourth is treated perturbatively and its effect is measured, not bounded.  
- **NC-S23.8** *(new in v1.2)*. No claim that the mirror-contained arcs are **globally minimising** paths. Lemma S23.2a(ii) establishes stationarity only, and the DEC lengths are fixed by **Convention D-len**, a definition. Gate F-S23.12.  
- **NC-S23.9** *(new in v1.2)*. No claim that hypothesis (D2) has been verified over the rectangle. It is COMPUTED on a 17 × 13 grid with a curvature bound covering the t-direction only. Gate F-S23.13.  
- **NC-S23.11** *(new in v1.3)*. No claim that hypothesis (D2b) has been verified over the amplitude interval. It is COMPUTED on a 13-point grid at two widths. Gate F-S23.13.  
- **NC-S23.12** *(new in v1.3)*. No claim that the eleven kind-X ledger entries carry proof weight. They are numerical diagnostics with measured but unbounded discretisation error, and the companion prints this definition alongside its totals.  
- **NC-S23.10** *(new in v1.2)*. The phrase "zero free parameters" is **not** claimed for the conformal probe coordinates t, a, w. The claim made is **zero new fitted physical parameters**: t, a, w are search coordinates used to demonstrate non-identifiability, no physical quantity depends on their values, and none is fitted to observation.

---

# §7. Conclusion

The algebraic half of the bridge is solid and is the paper's positive content. Gauge invariance forces centrality; centrality forces the Hessian to be a Killing-form multiple on each plaquette; the resulting edge operator is nonzero-isospectral to the ZS-S21 face operator. That chain is proved, is gauge-group independent for simple G, and needs nothing from the explicit integration except the numbers κ\_p. Its one hypothesis, single-plaquette locality, is exactly (H-W) and is named.

The selection half is not solid, and the paper's main service is to say so precisely. Version 1.1 strengthens that service in two directions at once. It makes the negative result **stronger** — Theorem S23.1 is now proved rather than exhibited, and Lemma S23.2a shows that most of the conformal computation is exact by symmetry rather than approximate by convention — and it makes the positive numerical claim **weaker and honest**, retracting eleven orders of magnitude of spurious precision. Both moves point the same way: the metric route appears, on strong computed evidence, to reach the orbit-blind point on a non-unique family of conformal metrics, and the clock route buys uniformity of a *stationary measure* where what is needed is uniformity of a *stiffness*. The distance between those two is a named, pre-existing, unresolved corpus bridge, (H-PSM-2), and ZS-F40's √2 refusal sits unreconciled beside it.

There is a methodological lesson worth recording, because the corpus has now met it twice. A residual of 10⁻¹⁴ measures how well a solver solved the equations it was given; it does not measure how well those equations represent the geometry. The two numbers differed here by a factor of 10¹¹. The discipline that catches this is the convergence study of Table 3.3, which costs one afternoon and should precede any quoted residual in the S-line from now on.

Version 1.2 adds a second lesson, of the opposite sign. Three of this paper's four review criticisms were answered not by lowering a claim but by **doing the mathematics the claim had presupposed**: an interval enclosure where a floating-point evaluation had stood (F-S23.9, now CLOSED-PASS), a symmetry argument where an unexamined convention had stood (Lemma S23.2a), and a definition made explicit where an ambiguity had stood (Convention D-len). Only the fourth, hypothesis (D2), resisted and was correctly demoted. A demotion is the right response to a gap; it is the wrong response to a gap that an afternoon of algebra would close, and telling the two apart is the whole skill.

**On the title.** *Action-to-Hessian Bridge* is accurate for what §5 proves — the algebraic universality of the identity-neighbourhood Hessian for any gauge-invariant single-plaquette action — and would be an over-claim if read as a derivation of the physical Hessian from ZS-S14. The one-line statement of the paper's reach is therefore: **ZS-S23 establishes the action-to-Hessian *algebraic universality theorem*; it does not perform the Z-Spin action-to-physical-Hessian *derivation*.** The chain single-plaquette gauge invariance ⇒ central class function ⇒ Ad-invariant Hessian ⇒ κ\_p Killing form is closed. The chain ZS-S14 master action ⇒ cellular action ⇒ {κ\_p} is not, and (H-W), (Z-A0), (Z-A1), the density-versus-rate identification and the semiclassical bridge all sit on it.

**A closing word on grading, since this is the terminal version.** Across three review cycles ZS-S23 moved one claim up (Theorem S23.1, to PROVEN with a certified separator) and four down (Application S23.2 to COMPUTED, Corollary S23.2e to COMPUTED / HYPOTHESIS-strong, Lemma S23.2a to *stationary* geodesy, the Taylor remainder from O(a³) to o(a²)). That asymmetry is the honest signature of a paper whose positive content is algebraic and whose numerical content is evidential. The one thing v1.3 refuses to do is let the two mix: a COMPUTED premise does not yield a DERIVED conclusion, and a ledger entry does not get to be graded C in the code and COMPUTED in the prose. Version 1.2 did both, and both are repaired here.

**The single most valuable next computation is unchanged and is now the only one:** integrate ∫√(−g) Tr(F ∧ ⋆F) explicitly over the 32 faces and 90 temporal prisms of K\_TI × a\_tℤ. Its output is the set {κ\_p}, and {κ\_p} decides (Z-A0), (Z-A1), (H-W) and the class question at once. Everything else in this paper is scaffolding around that one integral.

---

# Acknowledgements and Code Availability

This paper was consolidated from Z-Spin Collaboration research notes and revised across three external review cycles. The v1.0 review is addressed in §3.2, §3.3–§3.5, §3.6, §4.3 and Retraction S23-R11; the v1.1 review is addressed in §3.2 (interval certificate, F-S23.9 CLOSED-PASS), §3.3 (stationary versus minimising geodesy, Convention D-len, F-S23.12), §3.5 (the Lemma/Application split, S23-R12), §3.4 (resolution-dependent residuals), §6 (F-S23.1 rewritten) and Retraction S23-R13; the v1.2 review is addressed in §3.6 (S23-R14, the corollary demotion), §3.5 (S23-R15, hypothesis (D2b); S23-R17, the regularity misattribution), §3.3–§3.5 (S23-R16, three table/companion mismatches), §5 (S23-R18, C² versus O(a³)) and Appendix A (the C/X ledger split).

The companion verification suite is zs\_s23\_verify\_v1\_2.py. It rebuilds K\_TI from vertex coordinates with no imported data file, emits its results between the delimiters BEGIN\_ZS\_S23\_RESULTS and END\_ZS\_S23\_RESULTS, prints its mode, its wall-clock runtime and its own SHA256, and exits non-zero on any FAIL. Environment: Python 3.12.3+, numpy 2.4+, scipy 1.17+, sympy 1.14+, mpmath 1.3.0. Deterministic seed 20260320\.

**Two modes, and they are not interchangeable.** The default is MODE \= FULL (publication): it runs the quadrature grid out to (384, 96), the 17 × 13 monotonicity and bracketing grid at **both** profile widths, six multistart restarts per arc, and the in-suite geodesic-corrected root, and it reproduces every number in this manuscript. Version 1.2 claimed the same and did not deliver it: three tables quoted values from grids the companion did not run. That is repaired in v1.3, and it is the reason the runtime figure and the grid of each table are now stated explicitly. Wall-clock runtime on the reference environment is **147 s** in v1.3, down from 280 s in v1.2 because the IVT bracketing now runs on its own stated (96, 32\) working grid rather than on the (384, 96\) quadrature-table grid; this is environment-dependent and is disclosed because the v1.1 review reported being unable to complete a full run inside four minutes. Setting ZS\_S23\_FAST=1 selects MODE \= FAST / NON-PUBLICATION VERIFICATION, which runs FAST mode executes the same 98 ledger entries—87 C and 11 X—on reduced numerical grids.. **FAST results are not the publication ledger**: the residual of entry T175b, in particular, is resolution-dependent and prints 1.06 × 10⁻³ under FAST against 2.07 × 10⁻³ under FULL. The suite announces its mode at entry and repeats the warning at exit so that the two cannot be confused.

---

# Appendix A. Verification Ledger Summary, v1.3

Fail-closed ledger. Kinds: **C** \= theorem-bearing executable check on a number computed inside the suite, carrying proof weight; **X** \= COMPUTED diagnostic, numerical evidence with measured but unbounded discretisation error, carrying **no** proof weight; **D** \= declarative registry statement with no numerical content. The suite exits non-zero on any FAIL and prints these definitions with its totals. The C/X split is new in v1.3; v1.2 recorded every entry as C while demoting eight of them in prose.

**Table A1.** New and changed entries in v1.1, v1.2 and v1.3. Entries T001–T169, T180–T199 and D199a are inherited from v1.0 unchanged. Entries marked in bold text are new in v1.2.

| tag | kind | content |
| ----- | :---: | ----- |
| T170a | C | closed-form A₅(t) reproduces the constructed spherical area, dev \< 10⁻¹² |
| T170b | C | exact dual arcs cos d₅₆ \= √(1/3 \+ 2√5/15), cos d₆₆ \= √5/3, dev \< 10⁻¹² |
| T170c | C | closed-form σ(t) reproduces the constructed σ, dev \< 10⁻¹¹ |
| T170d | C | dρ/dt ≤ −4.11 \< 0 and dσ/dt ≤ −3.67 \< 0 on \[0.05, 0.49\]: both strictly decreasing |
| T170e | C | closed form for the equal-area point: ρ \= 1 ⟺ A₅ \= π/8 ⟺ cos r₅ \= cot(π/5)cot(5π/16) |
| T170f | C | separator t \= 7/20 in floating point at 40 dps: σ \= 0.7646874528 \< 1 \< 1.3049735713 \= ρ |
| T170f-iv | C | **interval enclosure** at t \= 7/20: sup σ \< 1 \< inf ρ, widths ≤ 7.5 × 10⁻⁴⁹ — closes F-S23.9 |
| T170f-r | C | certified rational bounds σ(7/20) \< 765/1000 and ρ(7/20) \> 1304/1000 |
| T170f-b | C | IVT brackets enclosed: at t \= 1/4 both ratios rigorously \> 1, at t \= 2/5 both \< 1 |
| T170g | C | full icosahedral group reconstructed, |I\_h| \= 120 |
| T170h | C | I\_h has 15 distinct mirror planes |
| T170i | C | dual vertices are isolated fixed points of C₅ᵥ (|Stab| \= 10\) and C₃ᵥ (|Stab| \= 6\) |
| T170j | C | exactly three of the four arcs are mirror-contained; only the primal (5,6) edge is not |
| T170k | **X** | multistart: no shorter path found for any mirror arc (gain ≤ 5.7 × 10⁻¹²) vs 5.4 × 10⁻³ for the non-mirror arc — evidence for, not proof of, global minimality |
| T170m | **X** | *(new in v1.3)* geodesic-corrected root computed in-suite: t\* \= 0.332756333, a\* \= 0.681385753 |
| T175a | **X** | the conformal root converges under quadrature refinement |
| T175b | **X** | honest residual, printed with its grid and mode: 2.07 × 10⁻³ at FULL (384, 96\) |
| T176a | **X** | (D2) 17 × 13 grid, worst secant slope −5.702152, curvature bound covers the t-direction only |
| T176a.45 | **X** | *(new in v1.3)* the same audit executed for w \= 0.45: slope −5.702152, curvature 86.528 |
| T176a2 | **X** | *(new in v1.3)* **(D2b)** uniform bracketing: min\_a σ(0.28,a) \= 1.414801 \> 1 \> 0.559944 \= max\_a σ(0.40,a) |
| T176b.60 / T176b.45 | C | (D3) sign change of g, so the IVT gives an exact root — an existence proof |
| T177 | **X** | Jacobian nonsingular at both roots (det \= \+6.9885, \+9.1498), IFT gives a local C¹ branch |
| T177a | **X** | the roots are distinct: non-uniqueness within 𝒟 (does **not** establish a continuum) |
| T177b | **X** | a third, structurally independent profile family also attains (1,1), at negative amplitude |
| D174 / D174a | D | Theorem S23.1 is PROVEN, and scoped to the round metric |
| D174b | D | Lemma S23.2a (Symmetry-Forced **Stationary** Geodesy), with Convention D-len |
| D174c | D | gate F-S23.12: stationary ≠ globally minimising |
| D178 | D | Theorem S23.2 **split**: Lemma S23.2b PROVEN-CONDITIONAL, Application COMPUTED; continuum a conjecture |
| D183 | D | Theorem S23.3, with the relocation-not-reduction accounting |
| D184 | D | neither route closes the class question |
| D193 | D | Theorem S23.4, with H\_edge ≠ Δ\_{S21} and (H-W) conditionality |
| D197 | D | Lemma S23.5 and Corollary S23.5a, with gate F-S23.8 left OPEN |

Totals: **98 executable entries PASS \= 87 C \+ 11 X, 12 declarative, 0 FAIL** (v1.2: 95 C, 12 D; v1.1: 91 C, 11 D; v1.0: 74 C, 9 D). Identical totals in FAST and FULL modes, on different grids — see the Acknowledgements.

---

# References

\[1\] M. Goldberg, "A class of multi-symmetric polyhedra," *Tôhoku Math. J.* **43**, 104 (1937). \[2\] G. Brinkmann, P. Goetschalckx and S. Schein, "Goldberg, Fuller, Caspar, Klug and Coxeter and a general approach to local symmetry-preserving operations," arXiv:1705.02848 (2017). \[3\] J. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Phys. Rev. D* **11**, 395 (1975). \[4\] M. Lüscher, "Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories," *Commun. Math. Phys.* **54**, 283 (1977). \[5\] N. H. Christ, R. Friedberg and T. D. Lee, "Gauge theory on a random lattice," *Nucl. Phys. B* **210**, 310 (1982). \[6\] N. H. Christ, R. Friedberg and T. D. Lee, "Weights of links and plaquettes in a random lattice," *Nucl. Phys. B* **210** \[FS6\], 337 (1982). \[7\] S. H. Christiansen and T. G. Halvorsen, "A gauge invariant discretization on simplicial grids of the Schrödinger eigenvalue problem in an electromagnetic field," *J. Math. Phys.* **53**, 033501 (2012). \[8\] T. G. Halvorsen and T. Sørensen, "Simplicial gauge theory and quantum gauge theory simulation," arXiv:1107.1420 (2011). \[9\] Z. D. Bai, "Methodologies in spectral analysis of large dimensional random matrices, a review," *Statistica Sinica* **9**, 611 (1999), Lemma 2.2. \[10\] N. V. Dang and E. Nohra, "Universal scaling limit of two-dimensional lattice Yang–Mills," arXiv:2602.08591 (2026). \[11\] B. K. Driver, "YM₂: continuum expectations, lattice convergence, and lassos," *Commun. Math. Phys.* **123**, 575 (1989). \[12\] T. Lévy, "Yang–Mills measure on compact surfaces," *Mem. Amer. Math. Soc.* **166**, no. 790 (2003). \[13\] C. Davis and W. M. Kahan, "The rotation of eigenvectors by a perturbation. III," *SIAM J. Numer. Anal.* **7**, 1 (1970). \[14\] D. N. Arnold, R. S. Falk and R. Winther, "Finite element exterior calculus, homological techniques, and applications," *Acta Numerica* **15**, 1 (2006). \[15\] A. N. Hirani, *Discrete Exterior Calculus*, Ph.D. thesis, California Institute of Technology (2003). \[16\] K. Osterwalder and E. Seiler, "Gauge field theories on a lattice," *Ann. Phys.* (N.Y.) **110**, 440 (1978). \[17\] M. Creutz, "Gauge fixing, the transfer matrix, and confinement on a lattice," *Phys. Rev. D* **15**, 1128 (1977). \[18\] K. G. Wilson, "Confinement of quarks," *Phys. Rev. D* **10**, 2445 (1974). \[19\] A. Jaffe and E. Witten, "Quantum Yang–Mills Theory," Clay Mathematics Institute Millennium Prize Problem description (2000). \[20\] I. Todhunter, *Spherical Trigonometry*, 5th ed. (Macmillan, London, 1886), §§ 60–70. *(Napier's rules and the spherical excess; used for A₅(r₅) in §3.2(ii).)* \[21\] S. Kobayashi, "Fixed points of isometries," *Nagoya Math. J.* **13**, 63 (1958). *(Used for Lemma S23.2a: the fixed-point set of an isometry is a totally geodesic submanifold.)* \[22\] S. G. Krantz and H. R. Parks, *The Implicit Function Theorem: History, Theory, and Applications* (Birkhäuser, Boston, 2002). *(Used for Proposition S23.2c.)* \[23\] R. E. Moore, R. B. Kearfott and M. J. Cloud, *Introduction to Interval Analysis* (SIAM, Philadelphia, 2009). *(Cited as the route to closing gate F-S23.9.)* \[24\] W. Tucker, *Validated Numerics: A Short Introduction to Rigorous Computations* (Princeton University Press, 2011). *(Cited for the same purpose as \[23\].)* \[25\] H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, New York, 1973), ch. 3\. *(Icosahedral symmetry data used in Lemma S23.2a.)*

**Z-Spin Collaboration internal references.**

\[26\] K. Kang, *Geometric Impedance: A \= 35/437*, ZS-F2 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[27\] K. Kang, *Gauge Symmetry Constraint: Why Q \= 11*, ZS-F5 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[28\] K. Kang, *The Spinor Mass Gap*, ZS-S7 v1.0 (Z-Spin Cosmology Collaboration, April 2026). \[29\] K. Kang, *Master Action Total Closure*, ZS-S14 v2.0 (Z-Spin Cosmology Collaboration, May 2026). \[30\] K. Kang, *The Glueball Hyperfine Structure from a Truncated-Icosahedron Cochain Vertex*, ZS-S17 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026). \[31\] K. Kang, *The Normalization-Ambiguity Theorem and the Regge-Moduli Exclusion*, ZS-S19 (Z-Spin Cosmology Collaboration, 2026). \[32\] K. Kang, *Non-Identifiability of the Hodge Measure*, ZS-S20 v2.2 FINAL (Z-Spin Cosmology Collaboration, July 2026). \[33\] K. Kang, *The Instrument Construction: Closing the Cellular Transfer-Matrix / Hodge-Measure Sub-Bridge of Z-Spin Yang–Mills*, ZS-S21 v1.2 TERMINAL (Z-Spin Cosmology Collaboration, July 2026). \[34\] K. Kang, *The Hodge–Dirac Complex of the Truncated Icosahedron*, ZS-M6 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[35\] K. Kang, *Register Unique Ergodicity and the Democratic Measure*, ZS-F38 (Z-Spin Cosmology Collaboration, 2026). \[36\] K. Kang, *The Physical Clock Discharge: a CLOSED-NEGATIVE Result*, ZS-F40 (Z-Spin Cosmology Collaboration, 2026). \[37\] K. Kang, *The Arrowhead Inverse-Eigenvalue Solve for the Q \= 11 Register*, ZS-M44 (Z-Spin Cosmology Collaboration, 2026).

---

# Version History

**v1.3 TERMINAL (July 2026, current): Third review-response revision — editorial and epistemic closure.** No new physics, no new claims, no new computations beyond making the companion compute what the manuscript already quoted. Six corrections, all raised by the v1.2 review. **(1) Corollary S23.2e demoted DERIVED → COMPUTED / HYPOTHESIS-strong; Retraction S23-R14.** v1.2 graded the corollary DERIVED while grading the Application it rests on COMPUTED, and its own legend defines COMPUTED as carrying no proof weight; the two gradings could not both stand. The Abstract's "refutes" becomes "provides strong computed counterevidence", the §4.4 route table is regraded, and the clause "what is claimed at proof strength is existence within 𝒟" is deleted from NC-S23.6. The substance — four roots, two structurally distinct families, both amplitude signs — is unchanged and is now called evidence. New legend entry **HYPOTHESIS-strong**. **(2) Lemma S23.2b gains hypothesis (D2b), uniform root bracketing; Retraction S23-R15.** v1.2's proof read "By (D2), t\_w(a) exists and is unique". Strict monotonicity gives **uniqueness, not existence** — a decreasing function may stay above 1\. (D2b) supplies existence and is tested over the whole amplitude grid at both widths: min\_a σ(0.28, a) \= 1.414801 \> 1 \> 0.559944 \= max\_a σ(0.40, a). New entry T176a2; new non-claim NC-S23.11; gate F-S23.13 widened to cover (D2b). **(3) Three table/companion mismatches repaired; Retraction S23-R16.** Table 3.4 quoted (192, 64\) roots that no companion block computed and now quotes the stated IVT working grid (96, 32), with the two grids and their distinct purposes stated explicitly; Table 3.2a's caption said twelve multistart restarts against the companion's six, and caption and values are corrected; the geodesic-corrected root, quoted in v1.2 from an off-line run, is now computed in-suite at entry T170m as t\* \= 0.332756333, a\* \= 0.681385753, a shift of Δt\* \= 4.74 × 10⁻⁴. The w \= 0.45 row of Table 3.4a, tabulated but not computed in v1.2, is now computed (new entry T176a.45). **(4) Ledger split into kinds C and X.** The eleven entries the manuscript grades COMPUTED — T175a, T175b, T176a, T176a.45, T176a2, T176, T177, T177a, T177b, T170k, T170m — are recorded as kind **X**, carrying no proof weight; the remaining **87** are kind **C**. The companion prints both definitions with its totals. New non-claim NC-S23.12. **(5) Theorem S23.4 regularity corrected; Retraction S23-R18.** Φ ∈ C² delivers a remainder o(a²), not O(a³); O(a³) requires C³ or a bounded third derivative. Both forms are now stated. The Hessian identity itself is a second-derivative statement and is unaffected, and the audited actions are real-analytic. **(6) The "non-smooth in a" attribution withdrawn; Retraction S23-R17.** The conformal potential depends on the amplitude linearly and smoothly; the max over twelve axes is non-smooth in the **spatial** argument, hence in t at Voronoi boundaries. The obstruction to covering the a-direction is an uncomputed mixed-derivative bound, not a regularity failure. Runtime falls from 280 s to **147 s** because the IVT block now runs on its own stated working grid. Ledger: **98 executable entries PASS \= 87 C \+ 11 X, 12 declarative, 0 FAIL**. Companion zs\_s23\_verify\_v1\_3.py, SHA256 c15927799cfdd821128fa5615dd93a9852088e480e6557ecdc16cd8141dad3f6. **ZS-S23 is terminal at v1.3.** The remaining open items are not S23's to close: F-S23.13 (certified (D2)/(D2b)) and F-S23.11 (full conformal DEC) would sharpen a conclusion that is already load-bearing as evidence, while the decisive computation — the explicit face-and-prism integration of ∫√(−g) Tr(F ∧ ⋆F) yielding {κ\_p} — belongs to a successor paper.

**v1.2 (July 2026): Second review-response revision.** No new physics. Three claim grades move, two up and one down, and every item raised by the v1.1 review is closed or explicitly re-registered. **(1) Gate F-S23.9 CLOSED-PASS.** The v1.1 separator was a 40-digit floating-point evaluation described as "certified" while F-S23.9 remained open — a position that cannot be held. Version 1.2 performs the enclosure: all six closed-form quantities at t \= 7/20 are evaluated in mpmath's interval context at 50 digits, with arccos and arcsin rewritten through atan2, giving σ(7/20) ∈ \[0.7646874528084177306485, …6486\] and ρ(7/20) ∈ \[1.3049735712612953801793, …1794\] at widths 4.9 × 10⁻⁵⁰ and 7.5 × 10⁻⁴⁹, hence the rigorous rational bounds σ \< 765/1000 \< 1 \< 1304/1000 \< ρ; the IVT bracket endpoints t \= 1/4 and t \= 2/5 are enclosed as well. Theorem S23.1 retains PROVEN, now without a contradicting open gate. New checks T170f-iv, T170f-r, T170f-b; new Table 3.0. **(2) Theorem S23.2 SPLIT; Retraction S23-R12.** v1.1's "PROVEN-CONDITIONAL on (D1)–(D3), each VERIFIED" conflated a piece of analysis with a claim about a discretised functional. The abstract statement is split off as **Lemma S23.2b** (PROVEN-CONDITIONAL, no numerics) and the **Application S23.2** is graded by hypothesis: (D1) VERIFIED, (D3) VERIFIED, (D2) **COMPUTED**. The (D2) evidence is strengthened from 3 × 9 to 17 × 13 evaluations with a sampled curvature bound showing the t-direction is covered between grid points (worst secant slope −5.702152 against an interpolation bound of 0.345) while the a-direction is only sampled; new Table 3.4a and new gate **F-S23.13**, whose closure is the one step that would raise the application to VERIFIED. **(3) Lemma S23.2a narrowed to *stationary* geodesy; new gate F-S23.12.** Totally geodesic gives stationarity, not global minimality, and a DEC length read as a metric distance would need the latter. The paper now fixes the lengths by **Convention D-len** — an explicit definition — under which Lemma S23.2a(ii) is exact, and registers F-S23.12 against any downstream reinterpretation as global distance. Multistart evidence is added (Table 3.2a, check T170k, declaration D174c): eight restarts in an eight-mode displacement basis find nothing shorter than any mirror arc (gain ≤ 1.8 × 10⁻¹¹) while the non-mirror (5,6) arc improves by 5.3 × 10⁻³. Labelled evidence, not proof; new non-claim NC-S23.8. **(4) Gate F-S23.1 rewritten; Retraction S23-R13(a).** The v1.1 wording was logically void — Theorem S23.2 is an existence claim inside named families, so a metric elsewhere admitting no solution contradicts nothing. It now fires on failure to reproduce the (D3) bracket or a root within 𝒟, leaving full-DEC destruction of the root to F-S23.11. **(5) Companion reconciled with the manuscript; Retraction S23-R13(b)–(d).** The stale banner "ZS-S22 v1.2 verification companion" and declaration D000 are corrected to ZS-S23; the quadrature grid now includes the (384, 96\) row the manuscript quotes; the residual figure is computed and printed with its grid and mode instead of hard-coded, and the manuscript's quoted value is corrected from the (192, 64\) figure 1.81 × 10⁻³ to the FULL-mode figure **2.07 × 10⁻³**; FAST mode announces MODE \= FAST / NON-PUBLICATION VERIFICATION at entry and repeats the warning at exit, and wall-clock runtime is disclosed (FULL: 271 s). **(6) "Zero Free Parameters" → "Zero New Fitted Physical Parameters".** The conformal probe coordinates t, a, w are search coordinates on the space of I\_h-invariant metrics used solely to demonstrate non-identifiability; no physical quantity depends on their values and none is fitted to observation. New non-claim NC-S23.10. Also: new non-claim NC-S23.9 on (D2); the Conclusion adds an explicit statement of the paper's reach — ZS-S23 establishes the action-to-Hessian **algebraic universality theorem**, not the Z-Spin action-to-physical-Hessian **derivation**. Ledger grows from 91 C / 11 D to **95 C / 12 D, 0 FAIL**. Companion zs\_s23\_verify\_v1\_2.py, SHA256 022327ac220a001813d995976b4b0e812fedd366e5fcefd2122ac47952c6d782. **Superseded by v1.3** in the grade of Corollary S23.2e, in the hypotheses of Lemma S23.2b, in Tables 3.2, 3.2a, 3.4 and 3.4a, in the ledger's C/X classification, and in the regularity of Theorem S23.4.

**v1.1 (July 2026): Review-response revision.** No new physics; the paper's verdicts are unchanged and its negative results are strengthened. Six external-review items are addressed. **(1) Theorem S23.1 upgraded from "PROVEN by exhibition" to PROVEN**, by new closed forms tan r₅(t) \= t√(1−c²)/(1 − t(1−c)), A₅ \= 10 arctan(cot(π/5)/cos r₅) − 3π, l₅₆ \= 2 arcsin(sin r₅ sin(π/5)), l₆₆ \= 2 arctan((1−2t)√((1−c)/(1+c))), the exact dual arcs cos d₅₆ \= √(1/3 \+ 2√5/15) and cos d₆₆ \= √5/3, an analytic monotonicity chain, root uniqueness, and the certified separating rational point t \= 7/20; the equal-area point acquires the closed form A₅ \= π/8. New checks T170a–T170f, declaration D174a. **(2) New Lemma S23.2a (Symmetry-Forced Geodesy, PROVEN)**, answering the review's conformal-DEC objection: the dual vertices are isolated C₅ᵥ / C₃ᵥ fixed points and hence metric-independent, and three of the four arcs lie in the 15 mirror planes of I\_h and are therefore totally geodesic for every I\_h-invariant metric; only the primal (5,6) edge is approximate, at a measured relative gap of 5.33 × 10⁻³. New checks T170g–T170j, declaration D174b. **(3) Theorem S23.2 re-proved by the intermediate value theorem**, status PROVEN-CONDITIONAL on the named and verified hypotheses (D1)–(D3), replacing v1.0's appeal to a solver residual; a third, structurally independent conformal profile family (3-fold axes, negative amplitude) is added as an anti-artefact control. New checks T176a, T176b, T177b. **(4) Retraction S23-R8**: the published residual 1.6 × 10⁻¹⁴ is withdrawn as a solver residual; a quadrature-convergence study (Table 3.3) establishes the true geometric residual of the v1.0 root as 1.8 × 10⁻³. New check T175a, T175b. **(5) Retraction S23-R9**: "two distinct solutions, therefore a continuum" is withdrawn and replaced by the three-step ladder Proposition S23.2b (non-uniqueness, COMPUTED), Proposition S23.2c (local C¹ branch by the implicit function theorem, DERIVED-CONDITIONAL on a nonsingular Jacobian, det J \= \+6.998 and \+9.162), and Conjecture S23.2d (global continuum, CONJECTURE, gate F-S23.10). New check T177. **(6) Retraction S23-R10**: the §4.3 sentence asserting "a genuine reduction in the corpus's axiom count" is deleted as a direct self-contradiction; the relocation-not-reduction reading is retained and the stale cross-references S22.11, S22.12 and §19.3 are corrected to S23.1, S23.3 and §4.4. **(7) Retraction S23-R11**: the companion's declaration ledger is rewritten in full, removing the pre-split theorem numbers (S22.12, S22.13, S22.15) and the non-existent ones (S24.1–S24.5), and removing three declarations that the v1.0 body had already retracted — "geometric route selects Class M", "identity-Hessian EXACTLY Delta\_S21", "STEP B closed unconditionally". New statuses COMPUTED and CONJECTURE added to the Epistemic Status Legend; new gates F-S23.9, F-S23.10, F-S23.11; new non-claims NC-S23.6, NC-S23.7. Ledger grows from 74 C / 9 D to **91 C / 11 D, 0 FAIL**. Companion zs\_s23\_verify\_v1\_1.py, SHA256 bb02df009540c227ec3c1c7234c4fd2303c2b6d316cda83bb8187c98db259ae5. **Superseded by v1.2** in the status of Application S23.2, in the scope of Lemma S23.2a, in the wording of gate F-S23.1, in the quoted residual figure, and in the companion's banner, grid and mode labelling.

**v1.0 (July 2026): Initial public release.** Consolidated from internal Z-Spin Collaboration research notes and split out of ZS-S22 v1.2 §18–§20 on the recommendation of external review. Renumbering: S22.11 → S23.1, the new conformal result → S23.2, S22.12 → S23.3, S22.13 → S23.4, S22.15 → S23.5, and the new isospectrality result → S23.6. Seven retractions (S23-R1 to S23-R7) issued against ZS-S22 v1.2. New axiom (Z-A3) named; gates F-S23.1 to F-S23.8. 74 verification-ledger entries PASS, 9 declarative, 0 FAIL. Companion zs\_s23\_verify\_v1\_0.py, SHA256 43f06a20139eebf82be8bb4e183259181e021ec0999a498b5d21beb6011899e4. **Superseded by v1.1** in the status of Theorems S23.1 and S23.2, in the continuum claim, in the §4.3 axiom accounting, and in the entire companion declaration ledger.

---

*Document formatting specification (for the typeset release): base text Times New Roman 11 pt, line spacing 1.15, paragraph spacing 0 pt, left aligned, blank line between paragraphs; title 16 pt bold left, section headings 13 pt bold left, subsection headings 12 pt bold left; footnotes and references 9 pt, APS style; table captions 10 pt left, table header labels 9 pt bold centred on background \#f3f3f3, borders 0.75 pt black, table body 9 pt, tables held at maximum width; block equations centred, with the constants **A**, **Q** and the core variables in bold; metadata 10 pt, epistemic tags upper-case bold.*  
