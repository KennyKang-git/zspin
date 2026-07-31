# **ZS-S28**

# **A Formal Event Exists; the Reduction Does Not Select It**

Terminal release of ZS-S28 — the formal event is constructed, the declared reduction does not select it, and the positive-energy modular suspension problem passes to ZS-M59

**Author:** Kenny Kang · **Affiliation:** Z-Spin Cosmology Collaboration  
**Theme / Paper Code:** Standard Model — **ZS-S28 v3.1 · TERMINAL**  
**Date:** July 2026  
**Companion:** zs\_s28\_verify\_v3\_1.py  
**Ledger:** **56 ANALYTIC · 118 NUMERIC · 3 PROXY · 18 DECLARATION · 0 FAIL · exit 0**  
**Scope of this release.** All active statements, tables and conclusions below are written under the v3.1 scope. The superseded claims of v3.0 are retained **only** in the version-history record at the end, each marked HISTORICAL — SUPERSEDED / RETRACTED.

## Terminal statement

**A formal pointer-QND event with multiplier lambda exists and is constructed exactly.**  
**The declared Whitney/DEC/S14 reduction does not select the physical event.**  
**The positive-energy modular suspension problem passes to ZS-M59, where it is open.**

# §0. Abstract

Thirty-one versions of this line asked for one complex number. It has not been derived, and the terminal position is three sentences long.  
**The formal event exists and is written down completely.** With r \= |lambda| \= 0.891513565776047, chi \= arg lambda \= 2.259249553902599, p \= (1+r)/2 and q \= (1−r)/2, the Kraus pair  
  K0 \= sqrt(p) · U\_chi,  K1 \= sqrt(q) · U\_chi · Z,  U\_chi \= exp(i chi Z / 2\)  
is completely positive and trace preserving with residual 3.17 × 10^−17, commutes with the pointer **exactly** (‖\[K\_r, Z\_path\]‖ \= 0), fixes both populations to 2.24 × 10^−17, and has coherence multiplier lambda to 2.48 × 10^−16. Its Choi operator has spectrum {1.891513565776047, 0.108486434223953, 0, 0}, rank two, and trace-out residual 3.17 × 10^−17. A collision model on an eleven-dimensional carrier — evading the ZS-M56 tensor-factor no-go — reproduces it to 1.11 × 10^−16 with a **real, positive** environment overlap of 0.891513565776047. As a semigroup it is positive dephasing at Gamma \= 0.153112833328013 per Planck time together with the bounded Hermitian Hamiltonian H\_Z \= −1.506166369268 Z. Its action path a(s) \= exp(s · ell), ell \= −0.114834624996010 \+ 2.259249553902599 i, is nonvanishing with winding zero.  
**The declared reduction does not select it.** The admissible I\_h-invariant diagonal measure family on K\_TI has 1 vertex orbit, 2 edge orbits and 2 face orbits, so five parameters and, modulo scale, an **admissible cone of dimension four**. The two eigenvalues that carry the corpus's downstream physics move across it by factors of **4.397** and **6.918**, with the locked pair (1.2428416, 7.5210904) recovered only at rho \= sigma \= 1\. The phase is absent from every sector constructed: quantised to {0, pi} in the two exact ones (Theorems T and W), and short by two to three orders of magnitude in the two numerical probes (Theorem U's scan, |arg| ≤ 0.085071, and the fermionic probe, \[−0.001067, 0.009303\]). Eleven of the thirteen fields the clock paper needs can be written down, and **all eleven are read off the target rather than derived from the action: 0 of 13 are S14-derived**.  
**The clock problem passes to ZS-M59, correctly scoped.** On the pointed minimal unitary dilation, the harmonic density lies in \[0.0573542988, 17.4354846876\], so the support is the full circle and the event unitary has spectrum the whole circle. Its **principal** logarithmic suspension is multiplication by the principal argument, with closed spectrum \[−pi, pi\]: bounded and two-sided, hence never unitarily equivalent to the M46 positive-energy generator, which is unbounded with spectrum \[0, infinity).  
**Principal-Suspension Obstruction. \[DERIVED\]** The *principal* logarithmic suspension of the minimal discrete dilation is bounded and two-sided, and therefore cannot be intertwined with the M46 positive-energy generator.  
**That statement is scoped to one branch, and only one.** The same unitary admits other logarithms. The branch theta\_plus in \[0, 2pi) gives a **positive** self-adjoint generator with closed spectrum \[0, 2pi\] satisfying exp(i P\_plus) \= U\_event to 8.01 × 10^−16, and integer-valued measurable branches give **positive unbounded** generators satisfying the same equation to 4.46 × 10^−10.  
**A single discrete unitary determines neither the boundedness nor the positivity nor the spectrum of its continuous generator.** The measurable functional calculus admits a family of logarithms; the principal branch is one choice among them, not *the* generator. **What is open is the selection of an admissible positive-energy suspension, not the existence of a positive one.**  
**And the Hardy projection is not a standard subspace.** A modular standard subspace is a closed **real**\-linear subspace with H\_R intersect i·H\_R \= {0} and H\_R \+ i·H\_R dense. The Hardy space H² is **complex**\-linear, so i·H² \= H² and the intersection is H² itself: on a 64-dimensional model it has dimension 64 where standardness requires 0\. A positive-frequency projection is not a standard subspace. Neither H\_R for the event nor its pointing has been constructed, and neither have the Tomita operator, the modular conjugation, the modular operator, a standardness proof, a half-sided inclusion or Borchers covariance.  
**ZS-S28 terminates here.** ZS-M59 begins as a separate paper whose first task is a single well-posed choice: **specify an admissible positive-energy logarithmic suspension together with a standard real subspace and a pointing.**

# §1. What each version claimed about the clock, and what is true

| version | claim | verdict |
| ----- | ----- | ----- |
| v2.8 | closed negative — discrete lattice against absolutely continuous spectrum | wrong argument: exp(t·ell) is a contraction semigroup, not a unitary group, and three spaces were conflated |
| v2.9 | prerequisites met, conditional on a multiplicity | declared, not computed: no generator was ever constructed |
| v3.0 | no positive generator exists on the discrete dilation | generalised a principal-branch statement into a global no-go |
| **v3.1** | **the principal branch is obstructed; the general suspension question is open** | **computed, and scoped** |

The sequence is worth stating plainly because it is the shape of the whole line: a negative asserted too fast, a positive asserted too fast in reaction, a second negative asserted too broadly, and then the object actually built and correctly bounded in scope.

# §2. The dilation and its suspensions

## 2.1 The pointed minimal unitary dilation

For a scalar contraction with |lambda| \< 1 the pointed minimal unitary dilation is L²(circle, mu\_lambda) with mu\_lambda the harmonic measure, the event unitary acting as multiplication by z, and the vacuum the constant function.

| quantity | measured (N \= 200 000\) |
| ----- | ----- |
| total mass of mu\_lambda | 1.00000000000000 |
| minimum density | 0.0573542988 |
| maximum density | 17.4354846876 |
| moments against lambda^n, n \= 0 to 5 | errors at most 4.0 × 10^−16 |

Stable across N \= 2 000, 20 000 and 200 000\. Since the density never vanishes, the support is the full circle and the event unitary has spectrum the full circle. **(LAC-01.)**

## 2.2 The principal branch

The principal suspension generator is multiplication by the principal argument. Since the essential range closure of a multiplication operator is closed, its spectrum is the **closed** interval  
  sigma(P\_principal) \= \[−pi, pi\].  
Bounded, two-signed, not positive. Against M46:

|  | bounded? | spectrum | spectral type |
| ----- | ----- | ----- | ----- |
| event, principal branch | **yes** | **\[−pi, pi\]** | absolutely continuous |
| M46 | **no** | **\[0, infinity)** | absolutely continuous |

Spectral type is **not** the obstruction — both are absolutely continuous. Boundedness is a unitary invariant, so the principal branch cannot be intertwined with M46. **This is scoped to that branch and to no other.** **(LAC-02.)**

## 2.3 Other branches exist, and they are positive

| branch | spectrum | positive? | bounded? | exponential residual |
| ----- | ----- | ----- | ----- | ----- |
| principal | \[−pi, pi\] | **no** | yes | — |
| theta\_plus in \[0, 2pi) | **\[0, 2pi\]** | **yes** | yes | **8.01 × 10^−16** |
| theta \+ 2 pi n(theta), n integer-valued measurable and unbounded | **unbounded, contained in \[0, infinity)** | **yes** | **no** | **4.46 × 10^−10** |

The third row's operator statement is simply: P\_n is positive, P\_n is unbounded, and exp(i P\_n) \= U\_event almost everywhere. The numerical figures for it are a sampled range on a 200 000-point grid, not a spectrum. **(LAD-01.)**  
**Positive self-adjoint logarithms exist abstractly.** What is missing is an action-selected or otherwise admissible logarithmic suspension equipped with the standard real subspace, pointing, spectral multiplicity and cyclic measure required for comparison with M46.

## 2.4 Where positivity would have to come from, and what a Hardy projection is not

In the Hudson–Parthasarathy limit the noise one-particle space is L²(half-line, dt) with dt the **collision time**, whose shift generator on L²(line, dt) has spectrum the whole line. A positive-frequency projection restricts it: on a 4096-point model the full generator range is \[−2048, 2047\] and the projected range is \[0, 2047\].  
**A Hardy space is complex-linear and is therefore not a modular standard real subspace.** On a 64-dimensional model, H² intersect i·H² has dimension 64 where standardness requires 0\. A standard **pair** is a closed real subspace together with a one-parameter unitary group whose generator is positive and which maps the real subspace into itself for positive times. **(LAD-02.)**  
Not constructed: the event's standard real subspace, its pointing, the Tomita operator, the modular conjugation, the modular operator, a standardness proof, a half-sided inclusion, Borchers covariance, and any intertwiner between L²(half-line, dt) and M46's L²(half-line, dp).  
**Notation trap, recorded:** dt is collision time; dp is the positive-energy spectral variable. The two spaces share a symbol but not a meaning.

# §3. The authoritative ZS-M59 gate table

This table supersedes every earlier M59 verdict in this line, including v2.8's closed-negative and v2.9's positive-conditional. **(LAC-05.)**

| gate | status |
| ----- | ----- |
| B0 input freeze | FORMAL artifact only; physical artifact **0 of 13 S14-derived** |
| B1 pointed minimal dilation | **DERIVED** — harmonic measure, moments to 4 × 10^−16 |
| B2 bilateral chain and record algebra | NOT CONSTRUCTED |
| **B3 continuous suspension** | **OPEN** — positive logarithmic suspensions exist abstractly, but the discrete event does not select an admissible positive-energy suspension or a pointed standard pair |
| **B4-principal** | **CLOSED-NEGATIVE** — the principal branch is bounded with closed spectrum \[−pi, pi\] and cannot match M46 |
| **B4-general** | **OPEN** — no frozen admissible branch, multiplicity, cyclic measure, standard real subspace, pointing or intertwiner has been supplied |
| B5 explicit one-particle intertwiner | NOT STARTED |
| B6 Fock lift and record MASA | NOT STARTED |
| B7 modular cocycle | NOT STARTED |
| HP construction | coefficients DERIVED; collision-to-HP convergence OPEN; **noise leg, not clock leg** |

The correct name for the work of v2.9 is **dilation and collision preliminaries executed**, not "B1 through B4 executed."

# §4. What ZS-S28 established, and what it did not

## 4.1 Established

| result | grade |
| ----- | ----- |
| **A–C** exact factorisation of the K\_TI face Laplacian; the two T1 eigenvalues in closed form over the field of the square root of five; **root sum 22** by Galois cancellation | ANALYTIC |
| **D** the degree commutant, codimension 20 400 | ANALYTIC |
| the dual-to-primal ratio on hexagon–hexagon edges equals the golden ratio | NUMERIC |
| **G** explicit Koenigs linearizer of i to the power z, to order 60, radius about 0.89 | ANALYTIC |
| **J** the two near-miss expressions are not identities, Krawczyk-certified | ANALYTIC |
| **L** Slab No-Go: the canonical slab preserves the harmonic register only when it acts trivially on it | ANALYTIC |
| **N** Action-Selection No-Go: admissible measure cone of dimension four, spectrum moving by factors 4.397 and 6.918 | ANALYTIC |
| **R** equivariant compression is a projective line; isotypic decompositions of the face and defect spaces | ANALYTIC |
| **T, W** real-symmetric compression and the Kato holonomy both give argument in {0, pi} | ANALYTIC, global |
| **U** quadrant bound: argument at most pi/2 for positive kernels | ANALYTIC, scan |
| **V** Phase-Separation Counterexample: positive dephasing with a Hermitian Hamiltonian realises **any** multiplier | ANALYTIC |
| **X** the residue is asymmetric: attenuation reachable, phase absent | ANALYTIC |
| **Y** fourfold phase deficit — two obstructions and two probes | ANALYTIC, scoped |
| the slab as a genuine three-complex, Betti numbers (1, 0, 1, 0\) | ANALYTIC |
| the harmonic-measure dilation and the exact collision scaling | ANALYTIC |
| **Principal-Suspension Obstruction** | **DERIVED, branch-scoped** |

**Independent of the framework**, and usable by a reader who accepts none of it: the closed-form face spectrum with its Galois explanation, the golden-ratio dual star, the degree commutant, the Koenigs linearizer, the Krawczyk-certified non-identities, the isotypic decompositions, the quadrant bound, the quantisation of the Kato holonomy on a real symmetric family, and the branch analysis of logarithms of a unitary dilation.

## 4.2 Not established

* **The physical channel.** The measure is undetermined by a four-dimensional cone; the phase is absent from four tested constructions; the artifact is 11 of 13 target-instantiated and **0 of 13 S14-derived**.  
* **The S14 fermion determinant.** The Wilson-like probe is edge-order dependent — relabelling shifts the determinant argument by up to 6.2 × 10^−3 — and lacks the gauge representations, the Higgs sector, the Yukawa coupling, a spin structure, a vielbein and BFV conditions.  
* **The clock.** Positive logarithms of the discrete event unitary exist, but **no admissible positive-energy pointed standard-pair suspension has been selected or constructed**, and no standard real subspace or pointing has been supplied.

## 4.3 The retraction register

"(H-QND) closed" · "Theorem S28.20" · "(H-PROC) all three clauses closed" · "S2 to S6 executed" · "dim Z equals 2 is an index" · "Theorem S28.19" · "alpha is not a locked-constant combination" · "closed negative" · "no structural gate remains" · "three independent checks" · "147 of 147 PASS" · "M59 blocked on the same integral" · "both lanes are closed" · "the target requires an indefinite Hermitian boundary action" · "Theorem K proven" · "the physical slab" (which was not a complex) · "Result Z, clock no-go" · "spectral prerequisites met" · "B1 through B4 executed" · **"the discrete dilation cannot supply a positive generator at all"** · **"that Hardy subspace is the standard real subspace"**.  
**Twenty-one retractions across thirty-one versions.** Every one is in the ledger with the measurement that caused it.

## 4.4 The semantic guard

A zero-FAIL count does not detect semantic contradiction: a ledger can carry two opposite verdicts and still pass. Version 3.1 therefore adds a guard that scans every ANALYTIC, NUMERIC and PROXY row for retracted phrases. Rows whose claim carries an explicit correction marker are exempt, since a correction must quote what it retracts; every other active row must be clean.

| quantity | value |
| ----- | ----- |
| active rows scanned | **164** |
| correction rows exempt | **11** |
| **violations** | **0** |

**(W7-SEMANTIC.)**

# §5. Handing off ZS-M59

**A — mathematical, conditional: may start now.** Input restricted to the abstract QND event: the channel, its multiplier, the pointer algebra and the pointer observable. Question: can a given abstract pointer-QND event be lifted to the same pointed modular clock as the M46 standard pair? Suggested title: *The Spectral and Modular Compatibility Problem for the Z-Spin QND Event*.  
**B — physical: blocked.** Requires 13 of 13 S14-derived fields and a frozen hash. Not to be titled *The Physical Clock of the ZS-S14 Measurement Event*.  
**The first task for ZS-M59 v1.0** is a single well-posed choice: **select an admissible positive-energy logarithmic suspension, and equip it with a standard real subspace and a pointing.** Everything downstream depends on it — B4's spectral audit, B5's explicit intertwiner with its domains, measures, Radon–Nikodym factors and real-subspace actions, B6's Fock lift with the record algebra kept **separate** from the clock algebra, and B7's modular cocycle with the central and weight-preserving results kept **separate**.

# §6. Falsification gates carried into ZS-M59

* **F-M59.1** An admissible positive-energy logarithmic suspension is selected and equipped with a standard real subspace and a pointing, so that the compressed generator is positive and the pair is standard. Then B3 closes and B4-general becomes runnable.  
* **F-M59.2** An explicit intertwiner between the collision-time space and M46's spectral space is constructed, preserving the standard real subspace. Then the notation trap of §2.4 is resolved.  
* **F-M59.3** The collision family is shown to satisfy the Attal–Pautrat hypotheses. Then HP convergence closes.  
* **F-M59.4** M46's spectral multiplicity is read from its own representation rather than assumed. Then B4-general's multiplicity clause becomes checkable.  
* **F-M59.5** A branch is exhibited whose obstruction matches the principal one, for reasons independent of branch choice. Then the Principal-Suspension Obstruction generalises after all.  
* **Retained from ZS-S28:** the clean-room release gate and the surviving falsification gates of the S28 series.

# §7. Conclusion

The formal event exists, and it is written down completely: two Kraus operators commuting exactly with the pointer, a Choi operator of rank two with spectrum {1.8915, 0.1085, 0, 0}, a collision model on an eleven-dimensional carrier whose environment overlap is real and positive, a semigroup generator with positive dephasing and a bounded Hermitian Hamiltonian, an action path of winding zero, and a pointed minimal unitary dilation whose moments reproduce the multiplier's powers to four parts in ten to the sixteenth.  
The declared reduction does not select it. The Hodge measure is free in four dimensions and the spectrum moves across that freedom by factors of four and seven. The phase is absent from every sector constructed — quantised to nothing or half a turn in the two exact ones, two to three orders of magnitude short in the two probes. Eleven of the thirteen fields the clock paper needs can be written down, and all eleven are read off the target rather than derived from the action.  
And the clock is neither closed nor obstructed by this line's work. What is established is narrower and cleaner than three previous versions claimed. **The principal logarithmic suspension is bounded and cannot match M46.** But alternative logarithms of the same unitary exist and are positive, one of them bounded and others unbounded, so **the discrete unitary alone neither closes nor obstructs the clock bridge**. What remains open is the selection of an admissible logarithmic suspension together with a standard real subspace, a pointing and the modular data — and a Hardy projection, being complex-linear, is not that subspace.  
**ZS-S28 terminates here.** Its role was to separate formal existence from physical selection and to fix both, and that is done. The positive-energy modular suspension problem is not S28's to close; it passes intact to ZS-M59.

# Acknowledgements and Code Availability

Developed with AI assistance; the author is responsible for all content. Twenty-one retractions stand in the register, and most were supplied by external review — including the last two, which turned a global no-go into a branch statement and removed an identification that could not hold.  
Companion: zs\_s28\_verify\_v3\_1.py, emitting zs\_s28\_verify\_v3\_1.json. Ledger **56 ANALYTIC · 118 NUMERIC · 3 PROXY · 18 DECLARATION · 0 FAIL · exit 0**, including the semantic guard of §4.4.

# Appendix A — Layers AC and AD

| Row | Content | Result |
| ----- | ----- | ----- |
| **LAC-01** | principal logarithmic suspension constructed | density in \[0.0573542988, 17.4354846876\]; support the full circle; sigma(P\_principal) \= \[−pi, pi\], closed, bounded, not positive |
| **LAC-02** | principal-branch comparison | bounded against unbounded; scoped to the principal branch only |
| **LAC-03** | where positivity would have to come from | full generator range \[−2048, 2047\]; positive-frequency projection \[0, 2047\]; a Hardy space is **not** a standard real subspace; collision-time and spectral spaces are distinct |
| **LAC-05** | **authoritative M59 gate table** | B1 derived; B3 open; B4-principal closed-negative; B4-general open; B2 and B5 to B7 not started |
| **LAD-01** | error 1 corrected | positive bounded branch, residual 8.01 × 10^−16; positive unbounded branch, residual 4.46 × 10^−10; global no-go retracted |
| **LAD-02** | error 2 corrected | H² intersect i·H² has dimension 64 where standardness requires 0 |
| **LAD-03** | terminal statement | unchanged by the corrections |
| **W7-SEMANTIC** | semantic guard | 164 rows scanned, 11 exempt, **0 violations** |

# Appendix B — The complete negative-control record

* A positive bounded logarithm and a positive unbounded logarithm of the same event unitary — the global no-go falls.  
* H² intersect i·H² has dimension 64 where standardness requires 0\.  
* v2.9's spectral table was typed, not computed.  
* The real part of the suspension exponent is negative: v2.8's "unitary group" was a contraction semigroup.  
* Harmonic density bounded below by 0.0574 — absolutely continuous, not discrete.  
* v2.7's slab violated the first chain identity by 2.000.  
* Edge relabelling shifts the determinant argument by 6.2 × 10^−3.  
* The wrong gauge-conjugation sign gives residual 31.5.  
* A pure-gauge background gives relative determinant phase exactly 0\.  
* The Kato holonomy is exactly −1 on one loop.  
* The v2.5 gauge-fixing term had no dependence on one cone coordinate.  
* Theorem V refutes v2.4's "indefinite kernel required".  
* The positive-kernel phase peaks at 0.085071.  
* Trivial multiplicity two in the defect space; the harmonic two-cochain compresses the contraction to zero.  
* The sigma-derivative of the propagator is positive definite: no measure-blind source.  
* Defect indices (29, 29).  
* Admissible cone dimension four; spectrum factors 4.397 and 6.918.  
* Canonical slab harmonic leakage 0.10510088.  
* Vortex proxy phase errors 2.350 and 1.752.  
* PSLQ relations found at 70 digits vanish at 150\.  
* Twenty thousand random CPTP channels: none fixes the pointer.  
* Torus carrier: nullity four, index zero.  
* Anti-numerology: 154 777 unique values, p \= 0.3615.  
* Clean-room release execution on both input configurations, exit 0\.  
* **Semantic guard: 164 active rows, 0 retracted phrases.**

# References

\[1\] B. Sz.-Nagy, *Acta Scientiarum Mathematicarum* **15**, 87 (1953); B. Sz.-Nagy and C. Foias, *Harmonic Analysis of Operators on Hilbert Space* (North-Holland, 1970; revised Springer, 2010).  
\[2\] R. L. Hudson and K. R. Parthasarathy, *Communications in Mathematical Physics* **93**, 301 (1984); K. R. Parthasarathy, *An Introduction to Quantum Stochastic Calculus* (Birkhauser, 1992); S. Attal and Y. Pautrat, *Annales Henri Poincare* **7**, 59 (2006).  
\[3\] H.-J. Borchers, *Journal of Mathematical Physics* **41**, 3604 (2000); H.-W. Wiesbrock, *Communications in Mathematical Physics* **157**, 83 (1993); R. Longo, *Real Hilbert Subspaces, Modular Theory, SL(2,R) and CFT* (2008) — standard real subspaces, standard pairs and half-sided modular inclusions.  
\[4\] K. Hoffman, *Banach Spaces of Analytic Functions* (Prentice-Hall, 1962\) — Hardy spaces.  
\[5\] M. Takesaki, *Theory of Operator Algebras II* (Springer, 2003\) — Connes cocycles; central versus weight-preserving equivalence.  
\[6\] G. Lindblad, *Communications in Mathematical Physics* **48**, 119 (1976); V. Gorini, A. Kossakowski and E. C. G. Sudarshan, *Journal of Mathematical Physics* **17**, 821 (1976); W. F. Stinespring, *Proceedings of the American Mathematical Society* **6**, 211 (1955); M.-D. Choi, *Linear Algebra and its Applications* **10**, 285 (1975); A. Fujiwara and P. Algoet, *Physical Review A* **59**, 3290 (1999).  
\[7\] T. Kato, *Perturbation Theory for Linear Operators* (Springer, 1966); M. V. Berry, *Proceedings of the Royal Society of London A* **392**, 45 (1984); C. A. Mead and D. G. Truhlar, *Journal of Chemical Physics* **70**, 2284 (1979).  
\[8\] W. V. D. Hodge, *The Theory and Applications of Harmonic Integrals* (Cambridge, 1941); A. N. Hirani, *Discrete Exterior Calculus*, PhD thesis, Caltech (2003); J.-P. Serre, *Linear Representations of Finite Groups* (Springer, 1977); F. Zhang, editor, *The Schur Complement and Its Applications* (Springer, 2005).  
\[9\] G. Koenigs, *Annales Scientifiques de l'Ecole Normale Superieure* (3) **1**, Supplement 3 (1884); J. Milnor, *Dynamics in One Complex Variable*, third edition (Princeton, 2006); R. Krawczyk, *Computing* **4**, 187 (1969); H. R. P. Ferguson, D. H. Bailey and S. Arno, *Mathematics of Computation* **68**, 351 (1999).  
\[10\] K. G. Wilson, *Physical Review D* **10**, 2445 (1974); M. Creutz, *Quarks, Gluons and Lattices* (Cambridge, 1983); P. W. Fowler and D. E. Manolopoulos, *An Atlas of Fullerenes* (Oxford, 1995).  
\[11\] K. Kang, ZS-M3, ZS-M9, ZS-M46, ZS-M51, ZS-M54, ZS-M56, ZS-M57, ZS-M58, ZS-S10, ZS-S14, ZS-S20, ZS-S21, ZS-S23, ZS-S24, ZS-S27, ZS-Q13, ZS-Q18.  
\[12\] K. Kang, *Integrated Successor Seed Report*, version 1.1; *Compass, Spear and Shield*, version 3.2.

# Version History

**v3.1 (July 2026): TERMINAL RELEASE OF ZS-S28.** Ledger **56 ANALYTIC · 118 NUMERIC · 3 PROXY · 18 DECLARATION · 0 FAIL · exit 0**.  
*Terminal statement.* A formal pointer-QND event with multiplier lambda exists and is constructed exactly. The declared Whitney/DEC/S14 reduction does not select the physical event. The positive-energy modular suspension problem passes to ZS-M59, where it is open.  
*Scope discipline.* All active statements, tables and conclusions are written under the v3.1 scope. Superseded claims appear only in this record, marked HISTORICAL. A semantic guard scans every active row for retracted phrases: 164 rows scanned, 11 correction rows exempt, **0 violations**.  
*Corrections carried in this release.* The principal-branch obstruction is **DERIVED**; positive logarithms of the same unitary are exhibited, one bounded with closed spectrum \[0, 2pi\] and residual 8.01 × 10^−16, one unbounded with residual 4.46 × 10^−10. Spectra of self-adjoint operators are written as closed intervals throughout. The Hardy projection is **not** identified with a standard real subspace: on a 64-dimensional model the intersection with its own imaginary multiple has dimension 64 where standardness requires 0\. The M59 gate table separates B3 (open), B4-principal (closed-negative) and B4-general (open). Metadata, companion name, ledger counts, retraction count and version count are unified.  
*HISTORICAL — SUPERSEDED / RETRACTED, retained for the record only:*

* **v3.0** claimed "the discrete dilation cannot supply a positive generator at all" and identified the Hardy subspace with the standard real subspace. **Both RETRACTED.**  
* **v2.9** claimed the spectral prerequisites for the intertwiner were met, conditional on a multiplicity. **RETRACTED** — the table had been entered by hand, not computed.  
* **v2.8** claimed a clock no-go from a discrete-versus-continuous spectral comparison. **RETRACTED** — the family compared was a contraction semigroup, not a unitary group.  
* **v2.7 and earlier:** the remaining eighteen entries of the retraction register in §4.3.

*Closure.* ZS-S28 is closed. Its result is the separation and fixing of formal existence and physical non-selection. The positive-energy modular suspension problem passes to ZS-M59.