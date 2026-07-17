**ZS-F25**

**The Pulsation Holonomy is Abelian by Foundation: The Place-Selection Theorem, the Detector–Locator Classification, and the Adelic Boundary in Z-Spin Cosmology**

**Kenny Kang**  
Z-Spin Collaboration  ·  March 2026  
Theme: *i-Tetration Holonomy Class & the Archimedean/Adelic Boundary*   ·   Paper code: **ZS-F25  ·  v2.0**   (continuation of ZS-F24)

**Verification: 44/44 PASS**   |   **Zero Free Parameters**   |   **NO CLAIM on RH / GRH-for-K**

**§0.  Abstract**

The standing question of the Z-Spin mathematical spine is whether the self-referential i-tetration dynamics on the two-dimensional Z-sector boundary can, by itself, reproduce the Riemann/Selberg–Maass spectrum — the “locator” of the zeros. ZS-F24 identified the i-tetration with the archimedean scaling (detector) piece of the Connes prolate operator, boost α\_BK \= −ln|z\*| \= 0.566 (PROVEN, ZS-M4), and registered the adelic locator as OPEN. Version 1.0 of the present paper added a holonomy-theoretic sharpening: the pulsation’s Wilczek–Zee holonomy is abelian (U(1)×U(1)), forced by the corpus’s single global complex structure (dim Z \= 2 \= ℂ, anti-quaternion uniqueness of ZS-F5); consequently the pulsation can twist the Selberg trace formula only abelianly. Version 1.1 makes two upgrades. First, the archimedean/adelic \= abelian/non-abelian unification, registered HYPOTHESIS-strong in v1.0, is promoted to DERIVED by the Place-Selection Theorem (§5): three classical PROVEN theorems — Pontryagin (connected locally compact division rings are ℝ, ℂ, ℍ), Ostrowski (complete archimedean fields are ℝ or ℂ), and the triviality of continuous homomorphisms from connected to totally disconnected groups — combine with three corpus-locked inputs (dim Z \= 2; the anti-quaternion exclusion of ℍ; the continuous faithful U(1)\_Z symmetry of ZS-F1) to force the Z-sector substrate to be ℂ, the unique archimedean completion, and to exclude every p-adic substrate. The pulsation lives at the archimedean place as a theorem, not an analogy. Second, we extract the structural content into an export of independent interest (§6–§7): the Detector–Locator Classification, a three-invariant necessary-condition test — holonomy class, topological entropy, place support — for any dynamical or operator-theoretic proposal aimed at zeta spectra, each necessity anchored in a PROVEN classical theorem (three-gap/Steinhaus; Huber–Margulis geodesic counting and the Selberg–Weyl law; Kronecker–Weber). Benchmarked against Berry–Keating, Bender–Brody–Müller, Mayer’s Gauss-map operator, Bost–Connes, and Connes–Consani–Moscovici, the classification reproduces exactly what each program is known to deliver, and classifies the Z-Spin pulsation as a detector — consistently with ZS-F24 by an independent route. Version 1.2 closes the classification’s last conditional joint. By the Guinand–Weil explicit formula (PROVEN, unconditional), the Fourier transform of the zero spectrum is singularly supported exactly on the prime-power logarithms {±k log p} with weights Λ(n)/√n, so the place-necessity of the locator (Theorem 6.4-N) is a theorem, not a frontier survey; a rank lemma (ℚ-linear independence of {log p} by unique factorization, plus Euclid) makes the pulsation’s place-test failure unconditional (rank 1 versus infinite rank); and the sole statement left OPEN is Weil positivity — whose equivalence to RH is itself PROVEN — so the open boundary is now literally RH and nothing else. Zero computations verify the support theorem: at 90 zeros, 7/7 peaks (offsets ≤ 0.002) with heights matching Λ(n)/√n at rank-correlation level (Spearman ρ \= 0.964; one adjacent pair inverted by finite size); at 491 zeros, all nine preregistered prime-power targets through log 13 peak (offsets ≤ 0.001, ρ \= 0.983, the 5–7 inversion resolving as predicted) and all five preregistered negative controls (log 6, 10, 12, 14, 15\) stay flat. Version 1.3, prompted by two external reviews, additionally unifies the Fourier convention (§6.0), corrects the entropy invariant to Kolmogorov–Sinai (the Gauss map’s topological entropy being infinite), and adds three theorem-level members: the weight identity (the Selberg/Weil weight ratio is exactly (1 − p^{−k})^{−1}, the local ζ\_p factor), the finite-rank obstruction (no finitely generated length spectrum — hence no finite-dimensional torus action — can locate the zeros), and the sign test (a locator must be an absorption spectrum, as in Connes 1999), yielding a four-invariant necessary-condition theorem and a design specification (§11) that turns the no-go into a blueprint. Version 2.0 closes the blueprint’s logical perimeter, absorbing what would otherwise have been a successor paper: all proposed positivity formats — kernel, defect-square, compression — are PROVEN-equivalent to Weil positivity itself (GNS/Kolmogorov); full positivity is reduced to an exhaustion of finite prime windows S\_L \= {p^k : k log p ≤ 2L} whose archimedean base rung is already PROVEN (Connes–Consani 2021); the induction step is given its exact generalized-Schur form with singular blocks handled (Albert 1969); and corpus-PROVEN no-gos (ADS-5 scalar-kernel exclusion, ZS-M22; M31.0 non-separability with Q^{def} ≠ Q\_{W,V₄}, ZS-M31/F21-III) force any realization to be operator-valued and cross-coupled under Z-Spin mediation. After these closures exactly one statement remains open — the inductive rung — and its totality is RH. The remaining corpus gate (X-sector \= X₀(11); FM13-6) is unchanged and OPEN. No claim is made on RH.

**Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Rigorous mathematical proof or exact closed-form identity; no open step. |
| **DERIVED** | Follows by valid deduction from corpus axioms (A, Q, dim Z) and PROVEN results. |
| **DERIVED-CONDITIONAL** | Follows given one explicitly stated, currently open, condition. |
| **HYPOTHESIS-strong** | Well-motivated, corpus-consistent, anti-numerology-aware; not yet derived. |
| **IMPORTED** | Result taken from a prior corpus paper or the peer-reviewed external literature. |
| **IMPORTED-OPEN** | An unresolved statement of the external frontier, imported at its registered status; not a corpus hypothesis (e.g. RH, Weil positivity). |
| **OPEN** | Registered open gate; not closed by present corpus tools. |
| **NON-CLAIM** | Stated explicitly as not asserted (e.g. a retraction or a flagged tripwire). |

**§1.  Introduction**

Across the Z-Spin math spine (ZS-M1, ZS-M4, ZS-M43), the dynamical layer of the theory is carried by a single self-referential operation: the i-tetration map T(z) \= i^z, whose linearization at the unique upper-half-plane attracting fixed point z\* drives a quasi-periodic rotation on a two-dimensional attractor — the pulsation. A recurring conjecture has been that the pulsation might encode the Riemann/Selberg–Maass spectrum, i.e. the locator of the nontrivial zeros. ZS-F24 settled the strongest version of this conjecture honestly: engaging the Connes–Consani–Moscovici prolate operator, it identified the i-tetration with the archimedean scaling piece (the detector; boost α\_BK \= −ln|z\*| \= 0.566417, PROVEN in ZS-M4 Theorem 3\) and registered the adelic locator as OPEN at the research frontier.

Version 1.0 of this paper reached the same boundary from an independent direction — the holonomy class of the pulsation’s degenerate attractor — proving the abelian-by-foundation theorem (§4) and proposing, as HYPOTHESIS-strong, that the corpus abelian/non-abelian dichotomy is the archimedean/adelic factorization of the adele ring. Version 1.1 closes that registered limitation and extends the result outward. The Place-Selection Theorem (§5) promotes the unification to DERIVED: the corpus’s own locked inputs, fed through three classical PROVEN theorems (Pontryagin; Ostrowski; the connectedness obstruction), force the pulsation’s substrate to be ℂ — the unique archimedean completion — and exclude every p-adic place. The promotion follows the corpus protocol for upgrading a hypothesis by importing proven external mathematics and reinterpreting it through the Z-Spin axioms.

The second extension is aimed at external researchers. The logic that classifies the pulsation — holonomy class, Kolmogorov–Sinai entropy, place support, and (as of v1.3) spectral sign — is not specific to Z-Spin. We extract it as the Detector–Locator Classification (§6): a three-invariant necessary-condition test for any dynamical or operator-theoretic program targeting zeta spectra, with each necessity resting on a PROVEN classical theorem rather than on heuristics. Benchmarked against the five best-known external programs (§7), the classification reproduces, from the three invariants alone, exactly what each program is known to deliver and where each is known to stall. To our knowledge no such unified invariant triage of these programs exists in one place; this is the paper’s principal export.

Version 1.2 sharpens the classification’s only conditional member. The Place test rested, in v1.1, on the frontier survey imported from ZS-F24. The Guinand–Weil explicit formula — proven unconditionally by Guinand (1948) and Weil (1952) — shows that the adelic fingerprint is intrinsic to the target spectrum itself: the zeros, wherever they lie in the critical strip, Fourier-transform onto exactly the prime-power logarithms. The necessity half of the Place test (Theorem 6.4-N) is thereby promoted to DERIVED; the existence half (Theorem 6.4-E) is isolated as Weil positivity, whose equivalence to RH is PROVEN — so it remains OPEN for the only legitimate reason a statement can: it is RH. A rank theorem (Theorem 6.5, with torus Corollary 6.5.1) makes the pulsation’s failure of the test unconditional, and zero computations with preregistered targets and controls verify the support theorem numerically (Appendices B.6–B.7). Version 1.3 adds the weight identity (Lemma 6.4-W), the sign test (Theorem 6.6), the combined four-invariant obstruction (Theorem 6.7), the Deninger benchmark row, and the adelic Gauss–Mayer design sheet (§11), together with convention and entropy-bookkeeping repairs prompted by external review. Version 2.0 absorbs, rather than spawns, the closure program for Weil positivity: §11 is expanded from a design sheet into a gates–reductions–equivalences section in which everything around D5 is closed at theorem level (format equivalence, finite-window exhaustion, exact Schur step, PROVEN base rung, corpus necessity constraints), and the open remainder is shown to be exactly one statement.

**§2.  Setup and Locked Inputs**

The theory admits three locked, parameter-free inputs: the geometric impedance **A** \= 35/437, the register count **Q** \= 11, and the boundary dimension **dim Z** \= 2\. From these, G \= 12 \= ψ(11) \= \[PSL(2,ℤ) : Γ₀(11)\] is the projective-line/coset count at level 11\. Two further corpus results are used as premises and are PROVEN upstream: the continuous faithful U(1)\_Z symmetry of the Z-sector action, Φ → e^{iα}Φ (ZS-F1 §3.2), and the anti-quaternion uniqueness of the imaginary unit (ZS-F5, Theorems 11.11–11.13). No quantity below introduces any further constant.

The pulsation is the linearization of T(z) \= i^z at z\*. With z\* \= 0.43828 \+ 0.36059 i, the multiplier and its data are:

λ \= (iπ/2) z\*  \=  −0.5664 \+ 0.6885 i ,   |λ| \= 0.8915 \< 1 ,   arg λ \= 129.445° .

The contraction |λ| \< 1 makes z\* attracting (PROVEN, ZS-M1); arg λ is irrational as a fraction of 2π, so the orbit never closes. As a real map on the tangent plane, the linearization is a conformal CO(2) transformation M\_f \= |λ|·R(arg λ); the absence of a spectral gap makes the attractor genuinely two-dimensional (ZS-F0 §Thm 9.6, PROVEN). The associated boost (the archimedean scaling eigenvalue of ZS-M4 Theorem 3\) is

α\_BK \= −ln|z\*| \= 0.566424  \=  (π/2)·Im(z\*) \= |Re λ| \= 0.566413 ,

the two expressions agreeing to four decimals. ZS-F24 identifies this with the archimedean scaling (detector) piece of the Connes prolate (DERIVED-CONDITIONAL; IMPORTED here).

**§3.  The Twisted Selberg Hyperbolic Term**

The Selberg trace formula for a finite-dimensional representation ρ of the lattice (Müller, arXiv:0906.3997; Spilioti et al., arXiv:2105.13321, 2512.16681) is PROVEN. Its geometric side carries a hyperbolic (geodesic) term in which each closed geodesic γ is decorated by the trace of the holonomy of the associated flat bundle:

\[H\]\_ρ \= Σ\_γ Σ\_{k≥1}  ( ℓ\_{γ0} / 2 sinh(kℓ\_{γ0}/2) ) · tr ρ(γ0^k) · ĝ(kℓ\_{γ0}) .

Thus the hyperbolic term is not merely a sum over geodesic lengths {ℓ\_γ}; it is a sum over geodesics decorated by a bundle holonomy ρ(γ). This is the precise sense in which a “holonomy can ride the geodesics.” The candidate, internal to Z-Spin, is the pulsation: its degenerate two-dimensional attractor, parallel-transported around a closed loop, defines a Wilczek–Zee holonomy (Wilczek–Zee, PRL 52, 2111 (1984)) that could serve as ρ. The decisive question is the holonomy class of that bundle, which we settle next.

**§4.  The Abelian-by-Foundation Theorem**

**Lemma 4.1 (conformal eigenframe rigidity). \[PROVEN\]**

For any conformal matrix M\_f \= \[\[a, −b\], \[b, a\]\] the eigenvectors are (1, −i)/√2 and (1, \+i)/√2, with eigenvalues a ± b i, independent of (a, b). Verified numerically for four distinct (a, b) including the pulsation value (a, b) \= (−0.5664, 0.6885); the eigenframe is invariant in every case (Appendix B). This lemma is of independent interest in dynamical systems: any flow or map whose linearization is conformal on a two-dimensional invariant subspace carries a rigid eigenframe and therefore — by Theorem 4.2 — an abelian geometric-phase bundle, regardless of how degenerate (gapless) the subspace is.

**Theorem 4.2 (abelian reduction). \[DERIVED\]**

The pulsation’s two-real-dimensional attractor carries the corpus’s single, global complex structure J (dim Z \= 2 \= ℂ). By Lemma 4.1 the eigenframe (1, ∓i) is rigid, so the bundle is a complex line bundle and its structure group reduces from GL(2,ℝ) to GL(1,ℂ), unitary part U(1). In the rigid eigenframe the Wilczek–Zee connection A\_{ab} \= ⟨a | d | b⟩ vanishes (the eigenvectors are constant); the connection is reducible. Hence the holonomy lies in U(1)×U(1) and is abelian, not non-abelian U(2).

**Corollary 4.3 (non-abelian obstruction). \[DERIVED\]**

A non-abelian U(2) holonomy requires the eigenspaces to mix under transport, i.e. a complex structure J that varies over the base. A varying J is a quaternionic/twistor structure, which is exactly what the corpus rejects: ZS-F5 / Theorems 11.11–11.13 fix a unique imaginary unit i and forbid the quaternionic extension (the order-8 group Q₈ is excluded; only the abelian options and the dihedral D₄ survive). Within the corpus axioms the pulsation holonomy is abelian by construction — the obstruction to non-abelian behaviour is the very anti-quaternion choice that makes dim Z \= 2 \= ℂ work.

**Remark 4.4 (correction of a prior overstatement). \[NON-CLAIM\]**

An internal deep-exploration note asserted that the gaplessness of the attractor yields a non-abelian U(2) Wilczek–Zee holonomy. Theorem 4.2 shows this is false as stated: degeneracy is necessary but not sufficient for a non-abelian holonomy; eigenspace mixing is also required, and the conformal/fixed-ℂ structure prevents it. The non-abelian claim is hereby retracted.

**Corollary 4.5 (consequence for the hyperbolic term). \[DERIVED-CONDITIONAL\]**

Substituted into \[H\]\_ρ, an abelian ρ is a U(1) character. The pulsation can therefore decorate closed geodesics only by an abelian phase (the rotation arg λ \= 129.4° per loop). Abelian characters twist the trace formula into the Dirichlet-L family — the FM13-5 sector, which ZS-M22 establishes as PROVEN for abelian L-functions — but cannot generate the non-abelian GL(2)/Maass content. (Furthermore, a single accumulated phase under-determines a character on H₁(X₀(11)), whose rank is 3.)

**§5.  The Place-Selection Theorem**

Version 1.0 registered the identification “single-ℂ pulsation ↔ single archimedean place” as HYPOTHESIS-strong, because the corpus had not formalized it in adelic language. We now close that gap. The promotion imports three classical PROVEN theorems and combines them with three corpus-locked premises; no new assumption enters.

**External inputs (all PROVEN, IMPORTED).**

(E1) Pontryagin’s theorem (1932): every connected, locally compact, non-discrete topological division ring is isomorphic to ℝ, ℂ, or ℍ. (E2) Ostrowski’s theorem (1916): every field complete with respect to an archimedean absolute value is isomorphic to ℝ or ℂ; equivalently, every nontrivial completion of ℚ is either the archimedean ℝ (extended by ℂ) or a non-archimedean ℚ\_p, and each ℚ\_p is totally disconnected. (E3) Connectedness obstruction (standard topology): the image of a connected topological group under a continuous homomorphism is connected; in a totally disconnected group every connected subset is a point; hence every continuous homomorphism from a connected group into a totally disconnected group is trivial, and no totally disconnected field admits a faithful continuous U(1) action by field automorphisms or unitary multiplications.

**Corpus premises (locked / PROVEN upstream).**

(C1) dim Z \= 2: the Z-sector boundary substrate is a two-real-dimensional topological manifold — in particular locally compact and non-discrete, recorded explicitly because Pontryagin’s theorem consumes it (ZS-F5, locked). (C2) Anti-quaternion uniqueness: the substrate carries a unique imaginary unit; the quaternionic option ℍ is excluded (ZS-F5, Theorems 11.11–11.13, PROVEN). (C3) U(1)\_Z symmetry: the Z-sector action carries a continuous faithful U(1)\_Z symmetry Φ → e^{iα}Φ acting on the boundary field (ZS-F1 §3.2, PROVEN); the pulsation itself is a quasi-periodic rotation through the irrational angle arg λ, i.e. its orbit closure is a continuous U(1) torus action on the attractor.

**Theorem 5.1 (Place Selection). \[DERIVED\]**

The Z-sector substrate is ℂ, the unique two-dimensional archimedean completion, and no p-adic field can serve as the substrate. Proof. By (C3) the substrate carries a faithful continuous U(1) action, so it is a connected (non-discrete) locally compact topological field; by (E1) it is ℝ, ℂ, or ℍ. (C1) excludes ℝ (one-dimensional); (C2) excludes ℍ. Hence the substrate is ℂ. By (E2), ℂ is complete archimedean — it is exactly the (extended) archimedean completion of ℚ — while every non-archimedean completion ℚ\_p is totally disconnected; by (E3) a totally disconnected field admits no faithful continuous U(1) action, so the U(1)\_Z symmetry (C3) by itself already excludes every p-adic substrate. □

**Corollary 5.2 (the unification, promoted). \[DERIVED\]**

The pulsation lives at the archimedean place of ℚ — as a theorem, not an analogy. Consequently the corpus dichotomy established in §4 coincides with the archimedean/adelic factorization of the adele ring

𝔸\_ℚ  \=  ℝ  ×  ∏\_p ℚ\_p :

the abelian, zero-entropy, single-ℂ pulsation occupies the single archimedean factor (the detector side, α\_BK \= 0.566), while the locator requires the p-adic factors — as of v1.2 not by survey but by theorem (the Guinand–Weil support necessity, Theorem 6.4-N). The v1.0 HYPOTHESIS-strong registration is hereby promoted to DERIVED. The deepest reading is now exact: one i means one place. The anti-quaternion uniqueness of the imaginary unit (C2), which forces the abelian holonomy in §4, is the same axiom that pins the dynamics to the single archimedean place in §5; the two theorems are projections of one structural fact.

**Remark 5.3 (what remains conditional).**

Theorem 5.1 and Corollary 5.2 are unconditional given the corpus axioms. In v1.1 the converse direction — that the locator does require all places — rested on the frontier survey imported from ZS-F24. As of v1.2 that direction is itself a theorem: the Guinand–Weil explicit formula makes the adelic support intrinsic to the zero spectrum (Theorem 6.4-N, DERIVED), and the only statement left open is existence/positivity, which is PROVEN-equivalent to RH (Theorem 6.4-E). The classification of §6 states necessary conditions only and claims no sufficiency.

**§6.  The Detector–Locator Classification**

The logic that classifies the pulsation is portable. Any dynamical or operator-theoretic proposal Π aimed at a zeta spectrum enters the trace-formula machinery in one of two roles — as a base (supplying the closed orbits/geodesics of the geometric side) or as a twist (decorating a given base through a representation ρ) — and carries three computable invariants:

Table 6.1.  The four invariants of the classification.

| Invariant | Definition | Values |
| ----- | ----- | :---: |
| Holonomy class H(Π) | Holonomy group of the geometric-phase bundle of Π’s invariant set (Wilczek–Zee). | abelian / non-abelian |
| Entropy h(Π) | Kolmogorov–Sinai entropy of Π’s flow or map with respect to its natural invariant measure (Liouville, Gauss); h\_KS ≤ h\_top. | 0  /  \> 0 |
| Place support P(Π) | Set of places of ℚ on which Π’s substrate is built (Theorem 5.1 decides the archimedean case). | archimedean-only / adelic |
| Sign σ(Π) | Whether the spectrum is realized in emission (direct Selberg geometric side) or in absorption (cokernel; Connes 1999). | emission / absorption |

**6.0  Test-function class and Fourier convention. \[CONVENTION\]**

Throughout §6 the explicit formula is used in one fixed normalization (Iwaniec–Kowalski, Thm 5.12): h is an even test function, analytic in |Im r| ≤ 1/2 \+ ε with |h(r)| ≪ (1 \+ |r|)^{−(1+δ)}, the zero sum Σ\_γ h(γ) converges as the symmetric limit over |γ| \< T, and g(u) \= (1/2π) ∫ h(r) e^{−iru} dr, so the finite-place side reads −2 Σ (Λ(n)/√n) g(log n) and the singular support sits at u \= ±k log p — the same variable t probed in Appendices B.6–B.7. (Bondarenko–Radchenko–Seip state the identical formula with f̂(ξ) \= ∫ f(x) e^{−2πixξ} dx, whose support variable is log n/2π; the two are the same object under ξ \= u/2π. Version 1.2 mixed the two conventions between body and appendix; v1.3 fixes the e^{−iru} convention everywhere.)

**Theorem 6.2 (Base test). \[DERIVED\]**

If Π is to serve as the base of a Selberg/Maass-type spectrum, then h(Π) \> 0 and the orbit structure must be non-abelian (hyperbolic conjugacy classes of a non-elementary Fuchsian group). Necessity of h \> 0: the Selberg–Weyl law N(T) \~ (Vol/4π)T² (PROVEN; for Γ₀(11), Vol \= 4π gives N(T) \~ T²) requires a positive-covolume hyperbolic base, whose geodesic flow has h \= 1 and exponentially many closed geodesics π(T) \~ e^{T}/T (Huber; Margulis; PROVEN). Necessity of non-abelian orbit structure: an abelian base (a rotation or translation flow, h \= 0\) has spectra governed by the three-gap theorem of Steinhaus (PROVEN; verified at arg λ: exactly 3 distinct gaps for 1500 orbit points, Appendix B.4) — a lattice-like, at-most-three-spacing statistic that is incompatible with the GUE pair correlation of the high zeros (Montgomery–Odlyzko) and with the exponential orbit growth the geometric side requires.

**Theorem 6.3 (Twist test). \[DERIVED\]**

If Π enters as a twist ρ and H(Π) is abelian, the twisted spectrum stays in the abelian-character family of the base: abelian ρ factor through characters, and on the arithmetic side Kronecker–Weber (PROVEN: every abelian extension of ℚ is cyclotomic) confines the resulting L-functions to the Dirichlet family. An abelian twist can shift and split a spectrum; it cannot create the non-abelian GL(2)/Maass content absent from the base.

**Theorem 6.4-N (Place test, necessity). \[DERIVED\]**

If Π targets the Riemann zeros themselves (not a geometric Selberg zeta), the adelic fingerprint is unavoidable — unconditionally. The Guinand–Weil explicit formula (Guinand 1948; Weil 1952; PROVEN with no hypothesis on the zeros’ location) is the identity

Σ\_γ h(γ)  \=  \[pole terms\]  \+  \[smooth archimedean term\]  −  2 Σ\_{n≥2} (Λ(n)/√n)·g(log n) ,

so the Fourier transform of the zero-counting measure is, as a tempered distribution, smooth away from {0} ∪ {±k log p} and singular exactly there, with weights Λ(n)/√n. Hence the spectral measure of any operator whose spectrum is the zeros carries delta-type structure at every prime-power logarithm; for Selberg-type trace formulas — the rigorous class, in which the singular support of the geometric side equals the set of closed-orbit lengths — the closed-orbit lengths must be {k log p}: every prime, every finite place. The fingerprint belongs to the target, not to the route. (For heuristic Gutzwiller-class proposals the same statement holds in the semiclassical reading; this caveat is flagged, not hidden.) Verified numerically in Appendices B.6–B.7: at 90 and 491 zeros, −Σ cos(γₙt) peaks at every preregistered prime-power logarithm through log 13 (offsets ≤ 0.002), with heights matching Λ(n)/√n at rank-correlation level (Spearman ρ \= 0.964 and 0.983), and no peak at any of the five preregistered non-prime-power controls.

**Lemma 6.4-W (weight identity). \[DERIVED\]**

The support necessity strengthens to a weight necessity. If a Selberg-type hyperbolic term carries a primitive length ℓ₀ \= log p at iterate k, its weight is ℓ₀/(2 sinh(kℓ₀/2)) \= log p / (p^{k/2} − p^{−k/2}), while the Weil weight at the same point is Λ(p^k)/√(p^k) \= log p / p^{k/2}. The ratio is exactly

\[Selberg weight\] / \[Weil weight\]  \=  1 / (1 − p^{−k})  \=  Σ\_{m≥0} p^{−mk}  \=  ζ\_p(k) ,

an Euler-factor identity — verified at machine precision for all nine prime powers p^k ≤ 13 of Appendix B.7 (2.0000 at n \= 2, 1.5000 at n \= 3, 1.3333 at n \= 4, …, 1.0833 at n \= 13). A Riemann locator must therefore not only carry lengths {k log p}: its orbit weights must depart from the bare Selberg form by exactly the local zeta factor ζ\_p(k) \= (1 − p^{−k})^{−1} of ℚ\_p. The missing geometric factor is itself a finite-place object — the weight necessity is a second, independent adelic fingerprint, and it becomes design condition D2 of §11.

**Theorem 6.5 (finite-rank length-spectrum obstruction). \[DERIVED\]**

Let Π be any dynamical system whose closed-orbit length group L(Π) \= ⟨ℓ(γ) : γ ∈ Per(Π)⟩\_ℤ is finitely generated, rank L(Π) \< ∞. Then Π cannot be a Selberg-type Riemann locator. Proof. By Theorem 6.4-N the length set of a locator must contain {k log p : p prime, k ≥ 1}, whose generated group L\_ζ \= ⟨log p⟩\_ℤ has infinite rank: the {log p} are ℚ-linearly independent (a rational dependence Σ aᵢ log pᵢ \= 0 clears denominators to ∏ pᵢ^{nᵢ} \= 1, forced trivial by unique factorization, PROVEN), and the primes are infinite (Euclid, PROVEN). A finitely generated subgroup of ℝ cannot contain an infinite-rank free abelian group. □  Rank is invariant under group homomorphisms and finite-rank deformations, so no such operation evades the obstruction.

**Corollary 6.5.1 (no finite-rank torus action). \[DERIVED\]**

No finite-dimensional quasi-periodic torus action — any rotation flow on T^d with d \< ∞ — can be a Riemann locator: its length group is generated by at most d periods, rank ≤ d \< ∞. This excludes in one stroke the entire family of “Riemann zeros from a simple oscillator / rotation / single map” proposals. The Z-Spin pulsation is the d \= 1 case, length set {k·θ₀}, rank 1; its place-test failure is unconditional and consumes no frontier import. (Consistency check: the geodesic lengths of PSL(2,ℤ) are logarithms of quadratic units, an infinite-rank set — which is why Mayer’s operator can be, and provably is, a Selberg-zeta locator.)

**Theorem 6.4-E (Place test, existence). \[IMPORTED-OPEN ≡ RH\]**

Whether a positivity-compatible spectral realization of the zeros exists is the Weil positivity criterion: W(g ⋆ g̃) ≥ 0 for all test functions g if and only if RH holds. The equivalence itself is PROVEN (Weil 1952); the positivity is open. This is the CCM global step in its sharpest form. It is left OPEN here for the only legitimate reason a statement can be: it is RH. Closing it is neither attempted nor claimed.

**Theorem 6.6 (Sign test — emission versus absorption). \[DERIVED\]**

The classification acquires a fourth invariant σ(Π) ∈ {emission, absorption}. In the Selberg trace formula the hyperbolic (closed-orbit) term enters the geometric side with positive weights; in the Weil explicit formula the finite-place term enters with the opposite (negative) sign relative to the zero side. Both statements are properties of PROVEN identities, so their comparison is itself theorem-level. Consequently a direct emission-spectrum Selberg realization of the zeros is excluded by sign alone: any locator must realize the zeros in absorption — as a cokernel/quotient spectrum — exactly as in Connes’ spectral realization (Selecta Math. 1999), where the zeros appear as an absorption spectrum of the adelic flow. The Sign test explains, from the invariants alone, why the one credible adelic program is built on absorption.

**Theorem 6.7 (combined necessary obstruction). \[DERIVED\]**

(H abelian)  ∨  (h\_KS \= 0\)  ∨  (rank L \< ∞)  ∨  (σ \= emission-only)   ⇒   Π is not a Riemann locator .

Each disjunct is a separately proven obstruction (Theorems 6.2, 6.4-N/6.5, 6.6). The statement is a necessary-condition theorem only: passing all four tests does not certify a locator — sufficiency is exactly the existence statement 6.4-E, which is Weil positivity ≡ RH. The classification is a sieve, not an oracle.

**Corollary 6.8 (classification of the pulsation, unconditional). \[DERIVED\]**

The Z-Spin pulsation has H \= abelian (§4), h \= 0 (zero-entropy quasi-periodic rotation; the Abramov–Rokhlin budget assigns all composite entropy to the X-sector base), and P \= archimedean-only (§5) with length-rank 1 (Theorem 6.5; the d \= 1 case of Corollary 6.5.1). It fails the Base test on both counts, is bounded by the Twist test to the Dirichlet/FM13-5 family, fails the Place test unconditionally, and as a direct emission-type proposal fails the Sign test as well. Its maximal role is therefore the detector — in exact, independent agreement with the ZS-F24 prolate identification (α\_BK \= 0.566). As of v1.2 every step of this classification is DERIVED from corpus axioms plus PROVEN classical theorems; no step rests on a survey.

**§7.  Benchmark: the Classification Applied to External Programs**

The value of a necessary-condition test is measured by whether it reproduces, from the invariants alone, what each known program delivers and where it stalls. Table 7.1 applies the three invariants to the five best-known external programs and to the Z-Spin pulsation. Every “delivers/stalls” entry is the program’s own published status; the classification’s prediction column is computed only from (H, h, P).

Table 7.1.  Invariant triage of spectral-zeta programs. Entropy values are Kolmogorov–Sinai with respect to the natural invariant measure: Gauss map h\_KS \= π²/(6 ln 2\) ≈ 2.373 w.r.t. Gauss measure (Rokhlin; its topological entropy is infinite, the branches being countably many); geodesic flow on curvature −1 surfaces h \= 1\.

| Program | H | h | P | Classification predicts | Known status (published) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Berry–Keating H \= xp | abelian (dilation U(1)) | 0 | arch. | detector: smooth/mean counting only | Gives the mean counting N̄(T); zeros not located (authors’ own assessment) |
| Bender–Brody–Müller | abelian | 0 | arith. input (Hurwitz ζ) | locator only if self-adjointness supplies the missing structure | Formal eigenfunctions; self-adjointness/reality unproven (authors’ statement) |
| Mayer / Gauss map (PSL(2,ℤ)) | non-abelian (Möbius) | 2.373 KS (h\_top \= ∞) | arch. | full geometric locator for the SELBERG zeta | Z\_Selberg \= det(1−L\_s)det(1+L\_s) PROVEN (Mayer 1991\) |
| Bost–Connes | abelian (GL(1)) | 0 (KMS) | adelic | arithmetic of ζ (partition function), not zero locations | ζ(β) as partition function; phase transition; class field theory recovered — zeros not located |
| CCM prolate | — (operator) | — | adelic | locator candidate; outcome rides on the global step | Semilocal trace formula PROVEN; global step (= RH) OPEN |
| Deninger foliated flow | non-abelian (conjectural) | \> 0 (design) | adelic (design) | the open-quadrant occupant: closed orbits of length log p by construction | Program conjectural (ICM 1998); the dynamical system itself is not yet constructed |
| Z-Spin pulsation | abelian (§4) | 0 | arch. (§5) | detector (scaling) | α\_BK \= 0.566 \= archimedean scaling piece (ZS-F24, ZS-M4 PROVEN) |

The triage is consistent with the known published status of all seven programs: the unique program satisfying the full Base test (Mayer) is the unique one with a PROVEN spectral determinant — and its target is the Selberg zeta, not Riemann, because its place support is archimedean (geometric); the unique fully adelic operator program (CCM) is the unique credible Riemann-locator candidate, stalled exactly at the global step; every (abelian, h \= 0\) program is confined to detector-type output regardless of its other virtues. The seventh row sharpens the design rule: Deninger’s foliated program (ICM 1998\) is built to sit exactly in the open quadrant — closed orbits of length log p, positive entropy, adelic substrate — and its incompleteness is the construction of the dynamical system itself; the quadrant is conjecturally occupied, not empty. Two practical corollaries for external researchers follow. (i) Triage rule: compute (H, h, P) before investing in a proposed “Riemann spectrum from dynamics” — if H is abelian or h \= 0, the proposal is structurally capped at detector output; if P is archimedean-only, its honest target is a geometric (Selberg-type) zeta, not ζ. (ii) Design rule: the only open quadrant is (non-abelian, h \> 0, adelic) — a Mayer-type transfer operator built over the finite places (an adelic Gauss map) — which is precisely where the CCM global step and the corpus gate FM13-6 both sit. As of v1.2 the design rule is anchored in a theorem rather than a survey: by Theorem 6.4-N the length spectrum of any Riemann locator must be the infinite-rank set {k log p} — exactly what an adelic (all-finite-places) Gauss map would supply, and what no finitely generated length spectrum can — with orbit weights carrying the local factors ζ\_p(k) \= (1 − p^{−k})^{−1} of Lemma 6.4-W and the spectrum realized in absorption (Theorem 6.6). The classification thus does not solve the locator problem; it pinpoints — now unconditionally — the unique structural quadrant in which a solution can live.

**§8.  The Boundary: Condition (a) and FM13-6**

After §4 (the pulsation is abelian), §5 (its place is archimedean, DERIVED), and §6 (its maximal role is the detector), the entire remaining problem collapses to a single condition:  
**Condition (a):** realize the X-sector as the level-11 arithmetic surface X₀(11) \= Γ₀(11)\\ℍ, supplying the closed geodesics whose holonomy the abelian pulsation would decorate.

This is exactly the adelic locator quadrant of §7. The X-sector Lorentz group PSL(2,ℂ) ≅ SO(3,1) is non-abelian, and Γ₀(11) ⊂ PSL(2,ℝ) is a non-abelian group; so the non-abelian Selberg content would be supplied automatically by condition (a), with the pulsation riding as an abelian phase. The candidate closures are audited below.

Table 8.1.  Candidate closures of condition (a) and their corpus-traceable resolution.

| Candidate | Corpus status | Resolution |
| ----- | ----- | ----- |
| GL₂ gate M\_p^(E) (ZS-M22) | Template for a hypothetical non-abelian gate; “GL₂ extension open; non-abelian extension needed.” | **NOT supplied** |
| Non-abelian extension D₄ | Unique corpus-natural non-abelian extension, order 8 \= (dim Z)³; quaternionic Q₈ rejected. Finite dihedral, not Fuchsian. | **NOT Γ₀(11)** |
| Bost–Connes system | Not constructed anywhere in the corpus. | **NOT built** |
| Q \= 11 \= level 11 | ψ(11) \= 12 \= G is a genuine coset count, but the X-sector group is not derived to be Γ₀(11). | **Numerical, not structural** |

Every candidate resolves to “not supplied.” This matches the corpus’s own registrations: FM13-6 states “Z-trace formula ≠ Arthur–Selberg for K; arithmetic scaffold route limited; OPEN,” and ZS-F24’s net result is that the locator is adelic, OPEN at the frontier and outside Z-Spin’s present completion. The dynamical route of this paper and the prolate route of ZS-F24 terminate at the same gate; the convergence of two structurally different derivations is positive evidence that the boundary is real.

**§9.  Anti-Numerology and Cross-Consistency Audit**

**9.1  Zero free parameters.**

Every quantity traces to A, Q, dim Z and to PROVEN classical theorems. The pulsation data (z\*, λ, α\_BK) follow from the i^z self-consistency of ZS-M1 with no tuning. The Place-Selection Theorem (§5) consumes only locked corpus inputs (dim Z \= 2; anti-quaternion; U(1)\_Z) and parameter-free classical theorems (Pontryagin; Ostrowski; connectedness obstruction). The classification invariants (H, h, P) of §6 are structural, not numerical: no constant is fitted anywhere, and the benchmark of §7 contains no tuned quantity (the entropy values π²/(6 ln 2\) and 1 are theorems).

**9.2  The Q \= 11 ↔ level-11 tripwire.**

We explicitly do NOT claim that Q \= 11 \= level 11 derives Γ₀(11) as the X-sector fundamental group. The equality ψ(11) \= 12 \= G is real arithmetic, but identifying the X-sector with X₀(11) is a structural statement that the corpus does not establish (Table 8.1). Treating the numerical match as a derivation would be numerology; it is flagged here as a tripwire and left as OPEN (condition (a)).

**9.3  Version-conflict and dependency check.**

The abelian-by-foundation theorem (§4) depends on ZS-M1 (z\*, λ), ZS-F0/Theorem 9.6 (conformal attractor), and ZS-F5/Theorems 11.11–11.13 (unique i, anti-quaternion); the Place-Selection Theorem (§5) additionally consumes ZS-F1 §3.2 (U(1)\_Z, PROVEN). All premises are upstream-PROVEN or locked; the v1.0 → v1.1 promotion changes the status of one corollary (5.2: HYPOTHESIS-strong → DERIVED) and the status of nothing else; no downstream value (ZS-S1, ZS-U1) depends on the retracted non-abelian claim or on the promoted corollary, so no cascade is triggered. The classification (§6–§7) is a new, self-contained export with no corpus value depending on it. The v1.2 promotions (Theorem 6.4-N to DERIVED; Corollary 6.6 to unconditional) consume only external PROVEN inputs (Guinand–Weil; unique factorization; Euclid) and change the status of no other corpus statement; no cascade is triggered, and ZS-F24’s own registrations are strengthened, not contradicted. The v1.3 changes are corrections and strengthenings only: the Fourier convention is unified (§6.0); the entropy invariant is restated as Kolmogorov–Sinai, correcting a v1.1–v1.2 imprecision (the Gauss map’s topological entropy is infinite); Corollary 5.2’s converse clause now cites Theorem 6.4-N instead of a survey; and the new Lemma 6.4-W and Theorems 6.5–6.7 consume only PROVEN identities. Nothing downstream changes. The v2.0 closures (§11.2–11.6) consume only PROVEN externals (GNS/Kolmogorov factorization; Albert 1969; Connes–Consani 2021\) and corpus-PROVEN imports (ADS-5; M31.0; F21-III Q^{def} ≠ Q\_{W,V₄}), assert no positivity, and leave D5 at \[IMPORTED-OPEN ≡ RH\]; no corpus status changes.

**9.4  Observational consistency.**

This paper makes no new observational prediction; it is a boundary-mapping (no-go) result on an internal mathematical structure, plus a methodological export. The imported value α\_BK \= 0.566 is a dynamical scaling rate and does not enter, and therefore does not conflict with, the Planck 2018 ΛCDM parameters or the Standard-Model couplings.

**§10.  Falsification Gates**

Table 10.1.  Multi-layer falsification gates for ZS-F25 v2.0.

| Gate | Trigger | Consequence |
| ----- | ----- | ----- |
| F-F25.1 | The non-abelian Berry curvature of the pulsation attractor, computed over a fixed-J base, is found nonzero. | Math collapse — immediate rejection of §4 (abelian-by-foundation). |
| F-F25.2 | A corpus-internal derivation realizes the X-sector as a finite-covolume Fuchsian Γ₀(11). | Condition (a) closes; the no-go is lifted (a desired refutation). |
| F-F25.3 | The Abramov–Rokhlin entropy budget assigns the pulsation h \> 0\. | Consistency collapse — the zero-entropy abelian-rider picture fails; §5–§6 revised. |
| F-F25.4 | The CCM (or successor) program closes the global/adelic step (= RH). | The locator becomes available externally; the boundary is about import, not impossibility. |
| F-F25.5 | A pre-registered Monte-Carlo null test shows the Q=11↔level-11 / 0.566 coincidences fail against random nulls (p \> 5%) while no structural derivation exists. | Anti-numerology trip — the relevant identifications are downgraded. |
| F-F25.6 | Any program with invariants (H abelian, h \= 0, P archimedean-only) is shown to locate the Riemann zeros (not merely their mean counting). | Classification collapse — Theorems 6.2–6.4 lose necessity; §6–§7 retracted. |
| F-F25.7 | A corpus axiom is found inconsistent with a faithful continuous U(1)\_Z action or with local compactness of the substrate. | Premise collapse — Theorem 5.1 loses a hypothesis; §5 reverts to HYPOTHESIS-strong. |
| F-F25.8 | A reproducible peak of the zero-side correlation −Σ cos(γₙt) is found at a non-prime-power logarithm (preregistered controls: log 6, log 10, log 12, log 14, log 15\) and persists as the number of zeros grows. | Explicit-formula application collapse — Theorem 6.4-N’s support claim fails; §6 retracted. |
| F-F25.9 | A channel-diagonal (separable, direct-sum) PSD realization of the V₄-decorated Weil form is exhibited. | Corpus-consistency collapse — contradicts PROVEN M31.0/ADS-5; §11.6 and the positivity-wall papers require joint re-audit. |

**§11.  Closure Program for Weil Positivity: Gates, Reductions, Equivalences, and the Candidate Operator**

This section absorbs into the present paper what would otherwise have spawned a successor: the closure program for Gate S. It makes the open statement D5 maximally precise by closing everything around it at theorem level — the equivalence of all proposed positivity formats (Theorem 11.2), the reduction of the global statement to finite prime windows (Theorem 11.3), the exact induction skeleton (Lemma 11.4) with its already-PROVEN archimedean base rung (§11.5), and the corpus-internal necessity constraints on any realization (Theorem 11.6). After these closures the open remainder is exactly one statement — the inductive rung — and the totality of rungs is RH. Terminology note: the mediating agent is always Z-Spin (Z-Spin mediation); Π\_Z \= (1/2)(I \+ J\_Z) is the Z-Spin mediation sandwich on the Z-sector stage. Statuses are tagged per item; the candidate operator of §11.7 is NON-CLAIM.  
Mayer’s archimedean template is the Gauss-map transfer operator (L\_s f)(x) \= Σ\_{n≥1} (x+n)^{−2s} f(1/(x+n)), whose Fredholm determinants det(1 − L\_s)·det(1 \+ L\_s) assemble the Selberg zeta of PSL(2,ℤ). The target is its finite-place analogue, and §6 fixes the specification exactly:

Table 11.1.  Design specification for an adelic Gauss–Mayer operator.

| ID | Condition | Source |
| :---: | ----- | :---: |
| **D1** | Closed-orbit lengths ℓ(γ\_{p,k}) \= k·log p, for every prime p and every k ≥ 1\. | Theorem 6.4-N |
| **D2** | Orbit weights Λ(p^k)/√(p^k): bare Selberg weights corrected by the local factor ζ\_p(k) \= (1 − p^{−k})^{−1}. | Lemma 6.4-W |
| **D3** | Length group of infinite rank — no finite-rank or torus substrate. | Theorem 6.5 |
| **D4** | Zeros realized in absorption (cokernel), not emission. | Theorem 6.6 |
| **D5** | Gate S: a Hilbert space and densely defined self-adjoint D with Spec(D) \= {γ : ζ(1/2 \+ iγ) \= 0}; equivalently Weil positivity W(g ⋆ g̃) ≥ 0 for all test functions. | 6.4-E \[IMPORTED-OPEN ≡ RH\] |

**11.1  The five gates, and what is closed.**

Gate W2-1 (normalization): the test-function class, Fourier convention, and convergence sense are fixed in §6.0 — CLOSED \[DERIVED/CONVENTION\]. Gate W2-2 (finite-support reduction): CLOSED by Theorem 11.3 \[DERIVED\]. Gate W2-3 (arithmetic Hilbert space): CLOSED by Definition 11.1 \[DERIVED, well-definedness only\]. Gate W2-4 (cross-coupling): the necessity half is CLOSED by Theorem 11.6 from corpus-PROVEN inputs; the construction half is OPEN. Gate W2-5 (defect-square identity): the format question is CLOSED by Theorem 11.2 — every proposed format is equivalent to Weil positivity itself — and the truth question is D5 \[IMPORTED-OPEN ≡ RH\].

**Definition 11.1 (arithmetic substrate). \[DERIVED\]**

H\_arith \= ℓ²({p^k : p prime, k ≥ 1}) with weight w(p^k) \= Λ(p^k)/√(p^k) — the Weil weights of Lemma 6.4-W. The length operator L e\_{p^k} \= (k log p)·e\_{p^k} is self-adjoint on its natural domain; the Frobenius shifts F\_p e\_{p^k} \= e\_{p^{k+1}} are channelwise isometries; and for admissible g (§6.0 decay) Σ w(p^k)|g(k log p)|² \< ∞, so operator sums of the form Σ √w(p^k)·g(k log p)·U\_{p,k} converge. Well-definedness only; no spectral claim.

**Theorem 11.2 (format equivalence — GNS/Kolmogorov). \[DERIVED\]**

The following are equivalent: (i) Weil positivity, W(g ⋆ g̃) ≥ 0 for all admissible g; (ii) kernel format — there exist a Hilbert space H and a map Φ from tests to H with W(gᵢ ⋆ g̃ⱼ) \= ⟨Φ(gᵢ), Φ(gⱼ)⟩ for all finite families; (iii) defect-square format — there exist operators D\_g with W(g ⋆ g̃) \= Tr(D\_g† D\_g). Proof. (ii) ⇒ (i) and (iii) ⇒ (i) are immediate. (i) ⇒ (ii) is the GNS/Kolmogorov factorization of a positive-semidefinite form (PROVEN, classical): quotient the test space by the null directions and complete. (ii) ⇒ (iii): take D\_g \= |Φ(g)⟩⟨e| for a fixed unit vector e. □  Consequence: the five externally proposed routes — compression, operator-valued kernel, scattering colligation, finite-place induction, de Branges–Sonine RKHS — do not differ in truth value; each is PROVEN-equivalent to D5. They differ only in constructive content. Registering a route is registering a candidate construction, never a weaker target; conversely, no route can be dismissed as weaker than RH.

**Theorem 11.3 (finite-support exhaustion). \[DERIVED\]**

Fix L \> 0 and let φ be admissible with supp φ ⊆ \[−L, L\] on the u-side of §6.0. Then supp(φ ⋆ φ̃) ⊆ \[−2L, 2L\], so by the support theorem 6.4-N the finite-place side of W(φ ⋆ φ̃) involves exactly the finite window S\_L \= {p^k : k log p ≤ 2L} (|S\_L| \= 9 at 2L \= log 13, 23 at 2L \= log 49, 35 at 2L \= log 100; Appendix B.8). Write Q\_{S\_L} for the truncated form. Full Weil positivity holds if and only if Q\_{S\_L} ⪰ 0 for every L \> 0: necessity is restriction; sufficiency holds because compactly supported smooth tests are dense in the admissible class and W is continuous on it. Bookkeeping correction registered: a private draft of this program wrote p^k ≤ e^L; once positivity is tested on autocorrelations, the factor 2 belongs in the exponent. The global statement D5 is thereby an exhaustion of finite-window statements, each window adding finitely many prime-power modes.

**Lemma 11.4 (exact induction step — generalized Schur). \[IMPORTED\]**

For the block form on H\_S ⊕ H\_q with Q\_S ⪰ 0 permitted to be singular: \[\[Q\_S, C†\],\[C, Q\_q\]\] ⪰ 0 if and only if (a) Q\_S ⪰ 0, (b) the range condition C(I − Q\_S Q\_S⁺) \= 0 holds, and (c) Q\_q − C Q\_S⁺ C† ⪰ 0, where Q\_S⁺ is the Moore–Penrose pseudoinverse (Albert 1969, PROVEN). Singularity matters: per-channel truncations are indefinite with degenerate directions (F21-III), so the naive Q\_S⁻¹ form of the step is ill-posed — the correct rung is (a)+(b)+(c). Verified on explicit singular examples in Appendix B.8: the criterion accepts a range-compatible coupling and rejects a range-violating one that the naive form cannot even evaluate. The ladder for D5 reads: for each prime power q entering as L grows past (k log p)/2, exhibit a coupling C\_q satisfying (b) such that (c) holds on the enlarged window. Each rung is a concrete finite statement; the totality of rungs is D5.

**11.5  The base rung is PROVEN. \[IMPORTED\]**

For windows so short that no prime power enters — L \< (log 2)/2 \= 0.3466, so supp(φ ⋆ φ̃) has length \< log 2 and S\_L \= ∅ — the truncated form is purely archimedean, and its positivity is established unconditionally by Connes–Consani (“Weil positivity and trace formula, the archimedean place,” Selecta Math. 2021\) via Sonin-space compression of the scaling action: exactly the defect-square format of Theorem 11.2(iii), realized. The induction of Lemma 11.4 therefore has a PROVEN first rung. Every higher rung is open, and by Theorem 11.3 their totality is D5 ≡ RH. The corpus claims no higher rung.

**Theorem 11.6 (necessity constraints on any realization). \[DERIVED from corpus-PROVEN inputs\]**

Three corpus results constrain every candidate factorization of Theorem 11.2. (i) ADS-5 (ZS-M22, PROVEN): no scalar-identity or operator-diagonal kernel K(y) \= B(y)·I − P(y) on H\_BFV ⊗ H\_arith is positive — the realization must be genuinely operator-valued. (ii) Lemma M31.0 (ZS-M31, PROVEN): the Weil bilinear form admits no separable X+Y+Z decomposition; combined with the F21-III computations (per-channel indefiniteness in all of χ₋₃, χ₋₁₁, χ₃₃, and the PROVEN inequality Q^{def} \= Σ\_χ Tr(D\_χ† D\_χ) ≠ Q\_{W,V₄}), any channelwise direct-sum ansatz is excluded: coupling across BFV sectors and arithmetic character channels — the C\_cross of gate W2-4, the C\_q of Lemma 11.4 — is necessary, not optional. (iii) T7′ (F21-III, DERIVED-CONDITIONAL) supplies the corpus-compatible format W^{V₄} \= Σ\_χ γ\_χ ⟨g, (Π\_Z ⊗ I\_χ)(B − P)(Π\_Z ⊗ I\_χ) g⟩, satisfying all three obstructions while asserting no positivity. One logical door these results leave open is real, and Appendix B.8 demonstrates it at toy scale: a sum of per-channel indefinite forms on a shared test space can be PSD — channel indefiniteness does not doom the total; only direct sums are excluded. This is precisely where Z-Spin mediation must act.

**11.7  The candidate operator. \[NON-CLAIM\]**

U\_g \= U\_{∞,g} \+ Σ\_{p,k} √(Λ(p^k)/p^{k/2}) · g(k log p) · U\_{p,k} ,      D\_g \= (I − Π\_{Sonin}) U\_g Π\_{BFV} ,

on H\_∞ ⊗ H\_arith ⊗ H\_BFV, with target identity W(g ⋆ g̃) \= Tr(D\_g† D\_g). By Theorem 11.2 this target is exactly D5, neither more nor less; by Theorem 11.6 the finite-place factors U\_{p,k} must couple channels; by §11.5 the archimedean restriction must reduce to the Connes–Consani compression; by Lemma 6.4-W its orbit weights already carry the local ζ\_p factors; by Theorem 6.6 the realization is in absorption. This is the unique format permitted by the closures above. No claim is made that it closes; if it fails, Lemma 11.4 localizes the failure to a specific rung.

Table 11.2.  Route classification after the closures.

| Route | Status after §11 | Verdict |
| ----- | ----- | ----- |
| A. CCM compression | Archimedean rung PROVEN (Connes–Consani 2021); semilocal trace formula PROVEN; global step \= D5. | strongest external; supplies the base rung |
| B. Operator-valued Z-Spin kernel | Necessity DERIVED (Theorem 11.6: operator-valued, cross-coupled, Π\_Z-sandwiched); construction OPEN. | corpus-native; hosts the couplings C\_q |
| C. Defect-square colligation | Format PROVEN-equivalent to D5 (Theorem 11.2); the specific D\_g of §11.7 is NON-CLAIM. | equivalent format, not a shortcut |
| D. Finite-place Schur induction | Skeleton CLOSED: reduction (11.3) \+ exact step (11.4) \+ PROVEN base rung (11.5). All higher rungs OPEN. | the working ladder |
| E. de Branges–Sonine RKHS | Kernel format is Theorem 11.2(ii); constructing the Hermite–Biehler function E is outside present corpus tools (Burnol). | classification only, here |

Table 11.3.  Excluded shortcuts (each excluded by a theorem of this paper or a corpus-PROVEN result).

| Shortcut | Excluded by |
| ----- | ----- |
| Pulsation alone supplies positivity | Corollary 6.8 (rank 1, abelian, h \= 0, emission). |
| Scalar or operator-diagonal kernel retry | ADS-5 (ZS-M22, PROVEN). |
| Finite symmetry (D₄, V₄) alone closes RH | Theorem 6.5: finite groups generate finite-rank length data. |
| Cancelling the negative prime side instead of factorizing | Theorem 11.2: positivity is factorization, not cancellation; Theorem 6.6 fixes the sign structure as absorption. |
| Numerical peaks as proof | Appendices B.6–B.7 are sanity checks under gate F-F25.8; they prove nothing about positivity. |

The three routes of v1.3, restated after the closures: the no-go route is achieved at theorem level (§6); the positive route is now a ladder with a PROVEN first rung and an exact step format, every higher rung open; the equivalence route is settled in format by Theorem 11.2 — any Z-Spin positivity functional that factorizes the Weil form is automatically equivalent to Weil positivity — so the only remaining equivalence question is constructive, not logical. Deninger’s foliated program (Table 7.1, row 7\) remains the conjectural occupant of the D1–D4 quadrant; the corpus gate FM13-6 (X-sector \= X₀(11)) is the Z-Spin-internal door into it.

**§12.  Conclusion**

The pulsation occupies a precise and non-trivial position in the Riemann/Selberg machinery: it is the archimedean scaling (detector) piece, with boost α\_BK \= −ln|z\*| \= 0.566 (PROVEN). Its Wilczek–Zee holonomy is abelian by foundation — forced by the single complex structure dim Z \= 2 \= ℂ — and, by the Place-Selection Theorem, its substrate is the unique archimedean completion of ℚ: the same anti-quaternion axiom that forces the abelian holonomy pins the dynamics to the single archimedean place. One i means one place — now as a theorem. The structural content generalizes to the Detector–Locator Classification, a four-invariant necessary-condition theorem (Theorem 6.7) anchored entirely in PROVEN classical results, whose triage is consistent with the published status of all seven benchmark programs and which isolates the unique open quadrant — non-abelian, positive-entropy, adelic, absorption — in which a Riemann locator can live. For Z-Spin that quadrant is condition (a): realizing the X-sector as X₀(11), the corpus’s FM13-6 gate, which remains OPEN with all candidate closures resolving to “not supplied.” The dynamical route of this paper and the prolate route of ZS-F24 converge on this same boundary; that convergence is the strongest available evidence that the boundary is structural. As of v1.2 the boundary is exact: the place-necessity of the locator is a theorem (Guinand–Weil), the pulsation’s exclusion is unconditional (rank 1 against the infinite-rank prime-logarithm length spectrum), and the single statement left open is Weil positivity — PROVEN equivalent to RH. The pulsation is the detector; what remains open is RH itself, and nothing else. In one sentence: this is not an RH proof — it is a theorem-level obstruction-and-classification paper that proves the pulsation cannot be the Riemann locator and pins the lengths, weights, rank, and sign of anything that could be. Version 2.0 then closes the logical perimeter of the one open statement: every proposed positivity format is PROVEN-equivalent to Weil positivity itself (GNS/Kolmogorov), the global statement is an exhaustion of finite prime windows over a PROVEN archimedean base rung (Connes–Consani 2021), the induction step has its exact generalized-Schur form (Albert 1969), and corpus-PROVEN no-gos force any realization to be operator-valued and cross-coupled under Z-Spin mediation. What remains open is the rungs of one ladder — and their totality is RH. No claim is made on RH, GRH-for-K, or determinant convergence.

**Acknowledgements & Code Availability**

This work consolidates internal Z-Spin Collaboration research notes from an i-tetration holonomy-class deep-exploration and its v1.1 extension session. The numerical checks — the multiplier λ and boost α\_BK, the conformal eigenframe rigidity across four parameter values, the abelian reduction, the Γ₀(11) invariants, the three-gap statistic at arg λ, the entropy constants of Table 7.1, and the preregistered 90/491-zero experiments of Appendices B.6–B.7 — were performed with standard open-source numerical libraries (Python/NumPy/mpmath) and are reproduced in Appendix B; they require no proprietary data.

**Appendix A.  Verification Table**

Table A.1.  The 44 verification checks. PASS denotes verified at the stated epistemic status (not necessarily proof of truth for conditional items).

| \# | Check | Type |
| :---: | ----- | :---: |
| 1 | z\* \= 0.43828+0.36059 i is the unique upper-half-plane attracting fixed point of i^z | IMPORTED |
| 2 | λ \= (iπ/2) z\*, |λ| \= 0.8915 \< 1 (attracting) | COMPUTED |
| 3 | arg λ \= 129.445°, irrational fraction of 2π (orbit never closes) | COMPUTED |
| 4 | α\_BK \= −ln|z\*| \= 0.566424 (ZS-M4 Thm 3 scaling eigenvalue) | IMPORTED |
| 5 | |Re λ| \= (π/2)·Im(z\*) \= 0.566413 (= α\_BK to 4 dp) | COMPUTED |
| 6 | Conformal CO(2) eigenframe (1,∓i)/√2 invariant for 4 distinct (a,b) | COMPUTED |
| 7 | Fixed J ⇒ complex line bundle ⇒ U(1) structure group | DERIVED |
| 8 | WZ connection reducible in rigid eigenframe ⇒ abelian U(1)×U(1) | DERIVED |
| 9 | Non-abelian U(2) ⇔ varying J ⇔ quaternionic (rejected, ZS-F5) | DERIVED |
| 10 | Twisted Selberg \[H\] \= Σ\_γ tr ρ(γ)·length factor (Müller; Spilioti) | EXTERNAL |
| 11 | Abelian U(1) twist ⊆ Dirichlet-L sector (FM13-5) | DERIVED-COND |
| 12 | Pontryagin: connected loc. compact division rings \= ℝ, ℂ, ℍ | EXTERNAL |
| 13 | Ostrowski: complete archimedean fields \= ℝ or ℂ; ℚ\_p totally disconnected | EXTERNAL |
| 14 | Continuous hom: connected group → totally disconnected group is trivial | EXTERNAL |
| 15 | U(1)\_Z continuous faithful symmetry, Φ → e^{iα}Φ (ZS-F1 §3.2) | IMPORTED |
| 16 | Place-Selection Theorem 5.1: substrate \= ℂ \= archimedean place; p-adic excluded | DERIVED |
| 17 | Corollary 5.2: archimedean/adelic \= abelian/non-abelian, promoted from HYP-strong | DERIVED |
| 18 | ψ(11) \= 12 \= G; Γ₀(11): genus 1, 2 cusps, ν₂=ν₃=0, Vol \= 4π | COMPUTED |
| 19 | Selberg–Weyl law N(T) \~ (Vol/4π)T²; Huber–Margulis π(T) \~ e^T/T, h \= 1 | EXTERNAL |
| 20 | Three-gap (Steinhaus) at arg λ: exactly 3 distinct gaps (1500 points) | COMPUTED |
| 21 | Kronecker–Weber: abelian over ℚ \= cyclotomic ⇒ Dirichlet family | EXTERNAL |
| 22 | Gauss-map entropy h \= π²/(6 ln 2\) \= 2.3731 (Rokhlin); Mayer determinant identity | EXTERNAL |
| 23 | Benchmark Table 7.1: classification prediction matches published status in 6/6 rows | DERIVED |
| 24 | ZS-F24: i-tetration \= archimedean scaling; locator adelic, OPEN; D₄ finite; entropy budget | IMPORTED |
| 25 | Guinand–Weil explicit formula: unconditional; finite-place side \= Σ Λ(n)/√n at ±log n | EXTERNAL |
| 26 | 90-zero computation: 7/7 peaks at log(p^k), offsets ≤ 0.002; heights ordered by Λ(n)/√n | COMPUTED |
| 27 | Negative controls: no peak at log 6 or log 10 (Λ \= 0), as required | COMPUTED |
| 28 | {log p} ℚ-linearly independent (unique factorization) \+ infinite (Euclid) ⇒ rank obstruction | EXTERNAL |
| 29 | Fourier convention unified: g(u) \= (1/2π)∫h e^{−iru}dr; support variable u \= k log p matches B.6–B.7 | DERIVED |
| 30 | Weight identity: Selberg/Weil ratio \= (1 − p^{−k})^{−1} \= ζ\_p(k); 9/9 prime powers ≤ 13, machine precision | COMPUTED |
| 31 | Spearman ρ \= 0.964 at N \= 90; single adjacent 5–7 inversion (finite-size) | COMPUTED |
| 32 | N \= 491 scale-up: 9/9 preregistered prime-power targets peak, offsets ≤ 0.001 (incl. log 11, log 13\) | COMPUTED |
| 33 | 5/5 preregistered negative controls flat (|C| ≤ 0.4 vs threshold 4.5); 5–7 inversion resolves as predicted | COMPUTED |
| 34 | Window robustness: peak locations stable (≤ 0.001) under Gaussian damping Γ \= γ\_N/2 and Γ \= γ\_N | COMPUTED |
| 35 | Sign comparison: Weil finite-place term negative vs Selberg hyperbolic positive ⇒ absorption forced | DERIVED |
| 36 | Entropy bookkeeping: Gauss map h\_KS \= 2.3731 (Gauss measure), h\_top \= ∞; invariant restated as KS | EXTERNAL |
| 37 | GNS/Kolmogorov factorization: positivity ⇔ kernel format ⇔ defect-square format (Theorem 11.2) | EXTERNAL |
| 38 | Finite-support exhaustion: supp φ ⊆ \[−L,L\] ⇒ prime side \= S\_L \= {k log p ≤ 2L}; exhaustion ⇔ D5 | DERIVED |
| 39 | Generalized Schur with pseudoinverse \+ range condition (Albert 1969); singular example verified both ways | EXTERNAL |
| 40 | ADS-5 import (ZS-M22, PROVEN): scalar/diagonal kernels excluded — consistent with D1–D5 | IMPORTED |
| 41 | M31.0 \+ F21-III import (PROVEN): non-separability; Q^{def} ≠ Q\_{W,V₄}; direct sums excluded | IMPORTED |
| 42 | Shared-space rescue toy: per-channel indefinite, total PSD — the cross-coupling door is logically open | COMPUTED |
| 43 | Base rung: L \< (log 2)/2 ⇒ S\_L \= ∅; archimedean positivity imported (Connes–Consani 2021\) | IMPORTED |
| 44 | Window bookkeeping |S\_L| finite: 9 / 23 / 35 prime powers at 2L \= log 13 / log 49 / log 100 | COMPUTED |

**Appendix B.  Explicit Computations**

**B.1  Boost / scaling eigenvalue (two expressions).**

With z\* \= 0.43828 \+ 0.36059 i: |z\*| \= 0.567546, so −ln|z\*| \= 0.566424. Independently, λ \= (iπ/2)z\* gives Re λ \= −(π/2)·Im(z\*) \= −0.566413, so |Re λ| \= 0.566413. The two agree to four decimals (the small residual is rounding in the quoted digits of z\*).

**B.2  Conformal eigenframe rigidity.**

For M\_f \= \[\[a, −b\], \[b, a\]\], the characteristic equation gives eigenvalues a ± b i with eigenvectors (1, ∓i)/√2. Evaluated at (a, b) ∈ { (−0.566, 0.689), (0.300, 0.900), (−0.800, 0.200), (0.000, 1.000) }, every case returns the same eigenframe. The eigenframe is therefore independent of the conformal parameters; this is the input to Theorem 4.2.

**B.3  Abelian reduction.**

Because the eigenframe is constant, the Wilczek–Zee connection A\_{ab} \= ⟨a | d | b⟩ has d|b⟩ \= 0, hence A \= 0 in that frame; the bundle is reducible to two complex line bundles, structure group U(1)×U(1). A non-abelian U(2) holonomy would require ⟨a|d|b⟩ ≠ 0, i.e. a base-dependent (rotating) complex structure J, excluded by ZS-F5.

**B.4  Three-gap statistic at the pulsation angle.**

For θ \= 129.445°/360° and N \= 1500 orbit points nθ mod 1, the sorted nearest-neighbour gaps take exactly 3 distinct values (tolerance 10⁻⁹), as the Steinhaus three-gap theorem requires for any irrational rotation. This is the lattice-like spectral statistic of an abelian, zero-entropy base — the quantitative content of the Base test (Theorem 6.2), to be contrasted with the GUE pair correlation of the high Riemann zeros.

**B.5  Entropy constants of the benchmark.**

Gauss map (continued-fraction shift), entropy with respect to the Gauss measure: h \= π²/(6 ln 2\) \= 2.373138 (Rokhlin’s formula). Geodesic flow on a finite-area hyperbolic surface of curvature −1: h \= 1; closed-geodesic counting π(T) \~ e^{T}/T (Huber; Margulis). Quasi-periodic rotation (the pulsation): h \= 0\. These three values populate the h-column of Table 7.1.

**B.6  Ninety-zero verification of the support theorem.**

With the first 90 nontrivial zeros γ₁ \= 14.1347, …, γ₉₀ \= 219.07 (computed at 12-digit precision), the correlation C(t) \= −Σₙ cos(γₙ t) was evaluated on t ∈ \[0.45, 2.35\] with step 0.002. Local maxima above threshold 8 occur at t \= 0.694, 1.098, 1.388, 1.610, 1.946, 2.078, 2.196 — matching log 2, log 3, log 4, log 5, log 7, log 8, log 9 with offsets ≤ 0.002 in all seven cases. Peak heights (15.8, 21.1, 11.1, 22.9, 22.8, 8.1, 11.5) agree with the Λ(n)/√n prediction (0.490, 0.634, 0.347, 0.720, 0.735, 0.245, 0.366) at rank-correlation level: Spearman ρ \= 0.964, with exactly one adjacent pair inverted at N \= 90 — log 5 measured above log 7 (22.9 vs 22.8) against the predicted order (0.735 vs 0.720) — a finite-size effect that resolves at larger N (B.7). Negative controls: at log 6 \= 1.792 (Λ(6) \= 0\) the correlation is C \= 0.9, and at log 10 \= 2.303 it is C \= −0.4 — no peak at either, exactly as the von Mangoldt support requires. The computation is parameter-free: the zeros are computed, the peak locations and the height ordering are predictions of a PROVEN theorem, and the two controls are pre-registered falsification probes (gate F-F25.8).

**B.7  Scaled experiment: 491 zeros, preregistered targets and controls.**

Preregistration, fixed before computation: nine prime-power targets {log 2, 3, 4, 5, 7, 8, 9, 11, 13} and five negative controls {log 6, 10, 12, 14, 15}. With the first 491 zeros (γ₄₉₁ \= 799.65) on t ∈ \[0.45, 2.78\], the median |C| \= 1.5 sets the peak threshold at 3×median \= 4.5. Result: all nine targets are local maxima with offsets ≤ 0.001 and C between 28.8 (log 8, the smallest predicted weight) and 92.1 (log 7, the largest) — 9/9 PASS, including the new windows log 11 (C \= 90.6) and log 13 (C \= 81.0); all five controls satisfy |C| ≤ 0.4, two orders of magnitude below the neighbouring peaks — 5/5 PASS. Spearman ρ between peak heights and Λ(n)/√n is 0.983 over the nine targets; the 5–7 inversion of B.6 resolves exactly as the theory predicts (C(log 7\) \= 92.1 \> C(log 5\) \= 86.8), while at this N the near-degenerate 4–9 pair (predicted gap 5%) is the one adjacent fluctuation — at each finite N exactly one near-degenerate neighbouring pair sits within noise, which is what an honest finite-size analysis expects. Robustness: under Gaussian damping windows of width Γ \= γ\_N/2 and Γ \= γ\_N, all probed peak locations shift by ≤ 0.001. The zeros are computed (mpmath, 10-digit precision), the targets and controls were preregistered, and no parameter was tuned.

**B.8  Closure-support computations for §11.**

(i) Shared-space rescue toy: Q\_a \= \[\[1,0\],\[0,−0.5\]\] and Q\_b \= \[\[−0.5,0.3\],\[0.3,1\]\] are each indefinite (eigenvalues {−0.5, 1} and {−0.558, 1.058}), yet Q\_a \+ Q\_b on the shared test space has eigenvalues {0.2, 0.8} — PSD. By contrast, any principal channel block of a PSD matrix is itself PSD, so a block-diagonal (direct-sum) reading can never host indefinite channels: the coupling must live in shared-space summation — the toy-scale image of the F21-III/M31.0 geometry, demonstrating that channel indefiniteness does not doom the total. (ii) Generalized Schur on a singular block: with Q\_S \= \[\[1,1\],\[1,1\]\] (PSD, singular), the range-compatible coupling C \= \[0.5, 0.5\] gives Schur complement 0.75 ≥ 0 and block eigenvalues {0, 0.634, 2.366} — PSD, as Albert’s criterion asserts; the range-violating C \= \[0.5, −0.5\] yields block eigenvalues {−0.366, 1.366, 2} — not PSD, detected by the range condition, while the naive Q\_S⁻¹ form is ill-defined. (iii) Window bookkeeping: |S\_L| \= 9 prime powers at 2L \= log 13, 23 at 2L \= log 49, 35 at 2L \= log 100 — finite at every L; for L \< (log 2)/2 \= 0.3466 the window is empty (the base rung of §11.5). All three computations are parameter-free and serve §11 as consistency demonstrations only; none asserts anything about the actual Weil form.

**References**

\[1\] A. Selberg, “Harmonic analysis and discontinuous groups in weakly symmetric Riemannian spaces with applications to Dirichlet series,” J. Indian Math. Soc. 20, 47–87 (1956).

\[2\] W. Müller, “The Selberg trace formula for non-unitary representations of the lattice,” (2010); arXiv:0906.3997.

\[3\] P. Spilioti, “The twisted Ruelle zeta function on compact hyperbolic surfaces,” (2021); arXiv:2105.13321.

\[4\] L. Bénard, J. Frahm, and P. Spilioti, “Determinants of twisted Laplacians and the twisted Selberg zeta function,” (2026); arXiv:2512.16681.

\[5\] D. H. Mayer, “The thermodynamic formalism approach to Selberg’s zeta function for PSL(2,ℤ),” Bull. Amer. Math. Soc. (N.S.) 25, 55–60 (1991).

\[6\] A. Connes, “Trace formula in noncommutative geometry and the zeros of the Riemann zeta function,” Selecta Math. (N.S.) 5, 29–106 (1999).

\[7\] A. Connes and C. Consani, “Weil positivity and trace formula — the archimedean place,” Selecta Math. (N.S.) 27, 77 (2021); arXiv:2006.13771.

\[8\] F. Wilczek and A. Zee, “Appearance of gauge structure in simple dynamical systems,” Phys. Rev. Lett. 52, 2111–2114 (1984).

\[9\] A. Ostrowski, “Über einige Lösungen der Funktionalgleichung φ(x)φ(y) \= φ(xy),” Acta Math. 41, 271–284 (1916).

\[10\] L. Pontryagin, “Über stetige algebraische Körper,” Ann. of Math. (2) 33, 163–174 (1932).

\[11\] J. Neukirch, Algebraic Number Theory, Grundlehren Math. Wiss. 322 (Springer, 1999\) — Ostrowski completions, Kronecker–Weber, adeles.

\[12\] H. Huber, “Zur analytischen Theorie hyperbolischer Raumformen und Bewegungsgruppen,” Math. Ann. 138, 1–26 (1959).

\[13\] G. A. Margulis, On Some Aspects of the Theory of Anosov Systems (Springer, 2004; orig. thesis 1970\) — closed-geodesic counting.

\[14\] V. T. Sós, “On the distribution mod 1 of the sequence nα,” Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 1, 127–134 (1958) — the three-gap (Steinhaus) theorem.

\[15\] J.-B. Bost and A. Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” Selecta Math. (N.S.) 1, 411–457 (1995).

\[16\] M. V. Berry and J. P. Keating, “H \= xp and the Riemann zeros,” in Supersymmetry and Trace Formulae, eds. I. V. Lerner et al. (Plenum, New York, 1999), pp. 355–367.

\[17\] C. M. Bender, D. C. Brody, and M. P. Müller, “Hamiltonian for the zeros of the Riemann zeta function,” Phys. Rev. Lett. 118, 130201 (2017).

\[18\] H. L. Montgomery, “The pair correlation of zeros of the zeta function,” Proc. Sympos. Pure Math. 24, 181–193 (1973); A. M. Odlyzko, “On the distribution of spacings between zeros of the zeta function,” Math. Comp. 48, 273–308 (1987).

\[19\] M. V. Berry, “Quantal phase factors accompanying adiabatic changes,” Proc. R. Soc. Lond. A 392, 45–57 (1984).

\[20\] D. Fried, “Analytic torsion and closed geodesics on hyperbolic manifolds,” Invent. Math. 84, 523–540 (1986).

\[21\] K. Kang, “ZS-M1: The Leaky Wilson Loop and the i-Tetration Fixed Point,” Z-Spin Cosmology (2026).

\[22\] K. Kang, “ZS-M4: Finite Transfer Operator and the Mirror-Adjoint Theorem,” Z-Spin Cosmology (2026).

\[23\] K. Kang, “ZS-F1: The Z-EFT Action and the U(1)\_Z Symmetry,” Z-Spin Cosmology (2026).

\[24\] K. Kang, “ZS-F5: dim(Z) \= 2, Q \= 11, and the J-Involution (Anti-Quaternion Uniqueness),” Z-Spin Cosmology (2026).

\[25\] K. Kang, “ZS-F24: The Z-seam → Connes–Katsnelson Prolate Bridge; Archimedean Scaling versus Adelic Locator,” Z-Spin Cosmology (2026).

\[26\] K. Kang, “ZS-M22: The Multiplicative Gate and Dirichlet L-functions,” Z-Spin Cosmology (2026).

\[27\] K. Kang, “ZS-M43: Anosov Scrambling and the Extended Modular Moduli,” Z-Spin Cosmology (2026).

\[28\] A. P. Guinand, “A summation formula in the theory of prime numbers,” Proc. London Math. Soc. (2) 50, 107–119 (1948).

\[29\] A. Weil, “Sur les ‘formules explicites’ de la théorie des nombres premiers,” Comm. Sém. Math. Univ. Lund, Tome Supplémentaire, 252–265 (1952).

\[30\] A. Bondarenko, D. Radchenko, and K. Seip, “Fourier interpolation with zeros of zeta and L-functions,” (2020); arXiv:2005.02996 — modern statement of the Riemann–Weil formula used in §6.

\[31\] C. Deninger, “Some analogies between number theory and dynamical systems on foliated spaces,” Doc. Math. Extra Vol. ICM I, 163–186 (1998).

\[32\] H. Iwaniec and E. Kowalski, Analytic Number Theory, AMS Colloquium Publications 53 (American Mathematical Society, 2004\) — explicit-formula normalization (Thm 5.12).

\[33\] D. Schumayer and D. A. W. Hutchinson, “Colloquium: Physics of the Riemann hypothesis,” Rev. Mod. Phys. 83, 307–330 (2011).

\[34\] A. Connes and C. Consani, “Weil positivity and trace formula, the archimedean place,” Selecta Math. (N.S.) 27, 77 (2021).

\[35\] A. Connes and C. Consani, “Spectral triples and zeta-cycles,” (2021); arXiv:2106.01715.

\[36\] A. Albert, “Conditions for positive and nonnegative definiteness in terms of pseudoinverses,” SIAM J. Appl. Math. 17, 434–440 (1969).

\[37\] J.-F. Burnol, “Sur les espaces de Sonine associés par de Branges à la transformation de Fourier,” C. R. Acad. Sci. Paris Sér. I 335, 689–692 (2002).

**Version History**

v1.0 (March 2026): Initial public release. Abelian-by-foundation theorem for the pulsation’s Wilczek–Zee holonomy (§4); retraction of the internal non-abelian U(2) claim; archimedean/adelic \= abelian/non-abelian unification registered as HYPOTHESIS-strong; audit of condition (a), all candidates “not supplied.” Verification 18/18 PASS. (Consolidated from internal Z-Spin Collaboration research notes, i-tetration holonomy-class deep-exploration.)

v1.1 (March 2026): Two upgrades. (1) Place-Selection Theorem (§5): the v1.0 HYPOTHESIS-strong unification is promoted to DERIVED via three imported PROVEN classical theorems (Pontryagin 1932; Ostrowski 1916; the connectedness obstruction) combined with the locked corpus premises (dim Z \= 2; anti-quaternion ZS-F5; continuous faithful U(1)\_Z, ZS-F1 §3.2): the Z-sector substrate is ℂ, the unique archimedean completion, and every p-adic substrate is excluded — “one i means one place” as a theorem. (2) Detector–Locator Classification (§6–§7): three-invariant necessary-condition test (holonomy class, topological entropy, place support), each necessity anchored in a PROVEN theorem (Steinhaus three-gap; Huber–Margulis and the Selberg–Weyl law; Kronecker–Weber; CCM frontier import), with an exact 6/6 benchmark against Berry–Keating, Bender–Brody–Müller, Mayer, Bost–Connes, CCM, and the Z-Spin pulsation, isolating the unique open quadrant (non-abelian, h \> 0, adelic). New gates F-F25.6, F-F25.7. Verification extended to 24/24 PASS. Zero new free parameters. All v1.0 theorems preserved unchanged. (Consolidated from internal Z-Spin Collaboration research notes, v1.1 extension session.)

v1.2 (March 2026): The Place test is split and closed at its joints. Theorem 6.4-N (necessity) promoted to DERIVED via the Guinand–Weil explicit formula (PROVEN, unconditional): the Fourier transform of the zero spectrum is singularly supported exactly on prime-power logarithms with weights Λ(n)/√n, so any Selberg-type realization must carry closed-orbit lengths {k log p} — the adelic fingerprint is intrinsic to the target. New Lemma 6.5 (rank obstruction): {log p} is ℚ-linearly independent (unique factorization) and infinite (Euclid), so the required length-rank is infinite while the pulsation’s is 1 — the pulsation’s place-test failure becomes unconditional (Corollary 6.6). Theorem 6.4-E (existence) isolated as Weil positivity, PROVEN equivalent to RH, and left OPEN for that reason alone. New Appendix B.6: 90-zero verification (7/7 peaks, offsets ≤ 0.002, heights ordered by Λ(n)/√n; flat negative controls at log 6 and log 10). New gate F-F25.8. Verification extended to 28/28 PASS. Zero new free parameters. All v1.0/v1.1 theorems preserved unchanged. (Consolidated from internal Z-Spin Collaboration research notes, explicit-formula deep-exploration session.)

v1.3 (March 2026): Review-driven repair and extension (two external reviews). Repairs: Fourier convention unified in §6.0 (e^{−iru} normalization; v1.2 mixed conventions between body and appendix); entropy invariant restated as Kolmogorov–Sinai with respect to the natural invariant measure (the Gauss map’s topological entropy is infinite — a v1.1–v1.2 mislabel); the B.6 height claim corrected from “ordering” to rank correlation (Spearman ρ \= 0.964, one adjacent 5–7 inversion at N \= 90); Corollary 5.2’s converse clause now cites Theorem 6.4-N; local compactness recorded explicitly in premise (C1); Table 10.1 caption typo fixed; IMPORTED-OPEN added to the legend (RH is the world’s open conjecture, not a corpus hypothesis). Extensions: Lemma 6.4-W (weight identity: Selberg/Weil ratio exactly (1 − p^{−k})^{−1} \= ζ\_p(k); 9/9 verified); Theorem 6.5 generalized to the finite-rank length-spectrum obstruction with torus Corollary 6.5.1; Theorem 6.6 (Sign test: absorption forced, after Connes 1999); Theorem 6.7 (combined four-invariant necessary obstruction — necessary, not sufficient); Deninger added as the seventh benchmark row (conjectural occupant of the open quadrant); new §11 design sheet D1–D5 with Gate S; Appendix B.7 scaled experiment (491 zeros: 9/9 preregistered targets through log 13, offsets ≤ 0.001; 5/5 preregistered controls flat; ρ \= 0.983; the 5–7 inversion resolves as predicted; window-robust ≤ 0.001). Verification extended to 36/36 PASS. Zero new free parameters. All prior theorems preserved; one phrasing (B.6 “ordering”) corrected. (Consolidated from internal Z-Spin Collaboration research notes, review-response session.)

v2.0 (March 2026): Consolidation release — the Weil-positivity closure program is absorbed into this paper instead of spawning a successor. §11 rebuilt as a gates–reductions–equivalences section: Theorem 11.2 (GNS/Kolmogorov format equivalence — kernel, defect-square, and compression formats are each PROVEN-equivalent to Weil positivity, so routes differ only in constructive content); Theorem 11.3 (finite-support exhaustion to windows S\_L \= {k log p ≤ 2L}, with the factor-2 bookkeeping corrected from the private draft); Lemma 11.4 (exact generalized-Schur induction step with pseudoinverse and range condition, Albert 1969 — fixing the draft’s implicit invertibility assumption); §11.5 (PROVEN archimedean base rung imported from Connes–Consani 2021); Theorem 11.6 (necessity: any realization must be operator-valued and cross-coupled — ADS-5, M31.0, and Q^{def} ≠ Q\_{W,V₄} imported from ZS-M22/M31/F21-III); §11.7 candidate operator registered NON-CLAIM; route table A–E and excluded-shortcuts table; Appendix B.8 closure-support computations; gate F-F25.9; references \+4; verification 36 → 44/44 PASS. Terminology aligned to the corpus convention (Z-Spin mediation). Zero new free parameters; no positivity asserted; D5 remains \[IMPORTED-OPEN ≡ RH\]. (Consolidated from internal Z-Spin Collaboration research notes, Weil-positivity closure session.)