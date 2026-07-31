**ZS-S27**  
**The Character-Coefficient Criterion for the Z-Spin Slab Action**  
**Conditional Negative Closure of F-S24.18, the Squared-Transfer Route, and a Zero-Fit Internal Spectral Ratio**

**Kenny Kang**  
Z-Spin Cosmology Collaboration (independent)  
Paper code: ZS-S27  |  Theme: Standard-Model / Yang–Mills transfer-positivity \+ scheme audit  |  July 2026

**Version 1.6**  
**Verification: 69/69 checks PASS (zs\_s27\_verify\_v1\_6.py; 8 proof-weight \[5 exact \+ 3 exhaustive\] \+ 30 float-verify \+ 2 numerical-band \+ 6 control \+ 21 cross/decl \+ 2 correction) | No external fitted number | Renumbered from internal draft ZS-S25 v1.6**

# 

# **§0. Abstract**

ZS-S24 v1.9 established a gapped, reflection-positive transfer operator on the truncated-icosahedron carrier only conditionally: its tier-(ii) Hamiltonian gap required a positivity property (R2+) that was left as the open gate F-S24.18. This paper closes F-S24.18 not by identifying an action but by a finite SIGN test. Using the Lüscher criterion — a temporal kernel k(U)=Σ\_R c\_R χ\_R(U) has a strictly positive transfer matrix if and only if every character coefficient c\_R is positive — we reduce F-S24.18 to counting the signs of the SU(3) character coefficients of the kernel produced by the cellwise-constant Whitney reduction of the ZS-S14 action. That reduction is Manton-type (squared-geodesic). We compute its coefficients on a certified SU(3) Weyl-integration pipeline and find them strictly negative for every tested coupling at and below β≈4, including the Z-Spin point β=3.25. Hence F-S24.18 closes negative CONDITIONALLY on the Whitney-to-Manton identification (gate F-S27.2): the Manton kernel is not reflection positive, but that ZS-S14 reduces to the Manton kernel is DERIVED-CONDITIONAL, so the closure is stated at that reduced status rather than as an unconditional headline.  
Two conditions frame the result and are stated up front. First, that the Whitney reduction is Manton-type is DERIVED-CONDITIONAL: in the non-abelian case the face flux is not exactly the plaquette holonomy (ZS-S23 §3.1), so “Manton not reflection positive” is proven but “ZS-S14 is Manton” is conditional, and the closure is stated as CLOSED-NEGATIVE-CONDITIONAL (gate F-S27.2). Second, the negativity is confined to irreps of dimension ≥ 45; the low irreps used by ZS-S24 Prop. S24.15′ (1, 3, 3̄, 6̄, 8\) are all positive, so no ZS-S24 first-order result is retracted. The negative (5,5) coefficient is enclosed by a conservative convergence band: c\_(5,5) ∈ \[−6.46, −6.41\]×10⁻⁸ (standalone 40-digit block; the integrated suite reproduces the same zero-separated band on the same M=40, 60, 80M=40, 60, 80M=40, 60, 80 grid at dps \=25=25=25, while the standalone block repeats the accumulation at 40-digit precision), grid-converged and 0-separated — a numerical witness, not a rigorous interval enclosure, so the formal interval proof stays OPEN. We give the squared-transfer route (T² ≥ 0 under site-reflection) as a theorem-candidate under an explicit action decomposition, with the gap-unchanged property VERIFIED on the tested coupling grid. For the dimensional bridge, the α\_s fixed point of ZS-S18 §6.3 has no root in the bare-lattice scheme; the failure is a scheme error, and adopting the heat-kernel discretisation (a canonical reflection-positive choice; Wilson is equally reflection positive) gives a SCHEME-ESTIMATED SU(3) Λ ratio ≈ 2.03 (conventions spread 1.82–4.93). Traced through scale-setting this gives λ\_t ≈ 6.26, and diagonalising the 32-face one-flux-loop effective sector (a carrier-wide one-loop truncation, not the full 90-link Hilbert space) leaves an \+11% λ\_t residual, which maps to a \+2.9% internal ratio. Diagonalising the two-gluon hyperfine operator Q\_Z on T₁⊗T₁ \= A\_g ⊕ T₁ ⊕ H yields the INTERNAL isotype ratios m\_H/m\_A \= 1.541 and m\_{T₁}/m\_A \= 1.208 (degeneracies 1, 3, 5). These are HYPOTHESIS-CONDITIONAL internal ratios, not physical glueball masses: identifying (A\_g, T₁, H) with (0++, 1+-, 2++) requires an intertwiner and a 2+1→3+1 emergence map that are OPEN (gate F-S27.1), so comparison with the 3+1 SU(3) lattice value 1.497 is indicative only. The one coefficient the ratio uses, 0.298805, is shown corpus-internal — the DERIVED closed-form exchange G\_exch \= 0.313264 plus a geometry-computed seagull — so the ratio is zero-fit (it imports no external fitted number) but rests on scheme/scale anchors, so it is not a parameter-free physical prediction, remaining conditional on F-S27.1, on the O(g²) hyperfine relation used at λ\_t ≈ 6 (the non-perturbative test is the 496-mode ZS-S18 Gate C), and on the numerical seagull and scheme-estimated Λ ratio, whose status propagates downstream.

# 

# **Epistemic Status Legend**

**PROVEN** theorem with a complete proof or exhaustive/closed-form verification.   **IMPORTED-PROVEN** an externally proven result placed in Z-Spin notation.   **DERIVED** follows from prior corpus results plus a stated construction.   **DERIVED-CONDITIONAL** derived under an explicitly flagged, not-yet-closed hypothesis.   **HYPOTHESIS-strong** supported by computation but missing one identified input.   **HELD** a result withheld pending an anti-numerology decision.   **OPEN** a well-posed but unclosed computation.   **NON-CLAIM** a numerical coincidence with no mechanism, explicitly not asserted.   **RETRACTED** a statement withdrawn within this paper's audit trail.  
**Renumbering note.** This paper was developed as the internal draft ZS-S25 v1.6. The code ZS-S25 was already assigned in the corpus to the gravitational-redirection paper (ZS-S25 v2.1 FINAL), whose successor ZS-S26 is in preparation. To protect citation stability this transfer-positivity and glueball-scheme audit is released publicly as ZS-S27 (present release v1.6); the internal draft is retained only for audit as ZS-S25X\_v1.6\_INTERNAL\_DO\_NOT\_CITE. Logical dependency: ZS-S24 → {ZS-S25 cubic/double-copy audit, ZS-S27 transfer-positivity and scheme audit} → ZS-S26 gravitational closure.  
**Gate and status summary.**

| Result | Status | Gate |
| ----- | :---: | :---: |
| Manton kernel has negative SU(3) character coefficients | VERIFIED (grid-converged, 0-separated numerical witness; formal interval proof OPEN) | — |
| F-S24.18 closes negative | CLOSED-NEGATIVE-CONDITIONAL on Whitney→Manton | F-S27.2 |
| Squared-transfer T² ≥ 0 (site-reflection) | THEOREM-CANDIDATE (stated decomposition) | — |
| Gap unchanged under |.| ordering | VERIFIED on tested coupling grid | — |
| Lanczos ε₀(g) reproduces ZS-S24 Δ\_E | exact at x=0 (A); VERIFIED to 10 digits across g | — |
| Heat-kernel Λ\_HK/Λ\_W ≈ 2.03 | SCHEME-ESTIMATE / HYPOTHESIS-strong | — |
| 32-face one-loop λ\_t \= 6.134 (+11% vs 5.539) | DERIVED-CONDITIONAL (one-loop truncation) | F-S27.3 |
| Residual mapped to observable m(2++)/m(0++) reading | THREE-READING DISCRIMINATION (extraction/prediction/truncation) | F-S27.4 |
| Internal ratio m\_H/m\_A \= 1.541, m\_{T1}/m\_A \= 1.208 | HYPOTHESIS-CONDITIONAL (not physical J^PC) | F-S27.1 |
| 0.298805 is corpus-internal (no external number) | DERIVED exchange \+ computed seagull | — |

# 

# **§1. Introduction**

## 

## **1.1 The conditional close of ZS-S24**

The Standard-Model carrier arc ZS-S17 → ZS-S24 sought a mass gap for SU(3) gauge theory on the truncated icosahedron K\_TI. ZS-S24 v1.9 proved that a finite cell complex with edge holonomies, uniform ellipticity and gauge-commutation carries a strictly positive gap for the transfer kernel at the level of correlation decay (its Theorem S24.9, tier (i)). Promoting this to a genuine Hamiltonian gap Δ\_phys ∈ (0,∞) needed a further property, that the one-step transfer operator be a positive operator, labelled (R2+). ZS-S24 realised (R2+) constructively via a symmetric-Trotter operator T\_a \= e^{−aV/2} e^{−aL} e^{−aV/2} but left OPEN, as gate F-S24.18, whether the actual Whitney-integrated ZS-S14 slab action equals a member of that positive family.  
This paper does not attempt to identify the two operators. It observes that the question of positivity is answered by a criterion older and cheaper than the identification.

## 

## **1.2 The Lüscher criterion as the decisive tool**

For a temporal kernel of the form k(U'U†) with k a class function, expand k in the Peter–Weyl basis, k \= Σ\_R c\_R χ\_R. Lüscher (1977) showed, and Osterwalder–Seiler placed on rigorous footing, that the transfer matrix built from such a kernel is strictly positive if and only if every character coefficient c\_R is strictly positive. This turns F-S24.18 from an open property into a finite sign test on one function on SU(3). We state it as F-S24.18′: are all c\_R of the ZS-S14 slab kernel non-negative?

## 

## **1.3 Summary of results**

Five results follow. (i) The cellwise-constant Whitney reduction of the ZS-S14 action yields a Manton (squared-geodesic) kernel, whose SU(3) character coefficients we compute and find strictly negative at and below β ≈ 4; F-S24.18 closes negative conditionally on the Whitney-to-Manton identification (§5). (ii) The negativity lives only in irreps of dimension ≥ 45, leaving every ZS-S24 first-order result intact (§5.3). (iii) Site-reflection positivity needs no coefficient condition, so T² ≥ 0 as a theorem-candidate and the gap-unchanged property is verified on the tested grid (§6). (iv) A single-face Lanczos computation reproduces the exact ZS-S24 strong-coupling gaps and supplies ε₀(g) across the crossover (§7). (v) The α\_s fixed point fails in the bare-lattice scheme; the failure is a scheme error whose repair is the heat-kernel discretisation, whose SU(3) Λ ratio is a scheme-estimate from the SU(2) anchor (§8–§9).

# 

# **§2. Setup and Certification**

All numbers below run on a pipeline certified before any physics is computed. The certification is fail-closed: each check asserts on a computed value and the suite halts on the first failure. Two blocks of certification precede the experiments.

## 

## **2.1 The SU(3) geodesic distance**

The squared bi-invariant geodesic distance from the identity is d(U)² \= min { Σ\_i θ\_i² : θ\_i \= φ\_i − 2π m\_i, Σ\_i m\_i \= k }, where e^{iφ\_i} are the eigenvalues of U and k \= (Σφ\_i)/2π. The constraint Σ m\_i \= k is the coset of the coroot lattice that preserves tracelessness of the logarithm; minimising over it is the pull-back into the fundamental alcove. The naive alternative of subtracting the mean angle is not a lattice operation and gives d²=0 for the centre elements, a fatal error; the certified implementation reproduces the analytic centre value d² \= 8π²/3 exactly.  
Table 2.1. Block-1 certification of the geodesic distance (6 checks in the companion suite, 0 FAIL; the six are listed below).

| Check | Quantity | Result |
| ----- | :---: | :---: |
| C1 | d(I) \= 0 | 0 (exact) |
| C2 | d(exp X) \= ‖X‖, ‖X‖ ≤ 1 | 4.4×10⁻¹⁶ |
| C3 | conjugation invariance | 7.1×10⁻¹⁵ |
| C4 | inversion symmetry | 7.1×10⁻¹⁵ |
| C6 | centre ωI, ω²I: d² \= 8π²/3 | 26.3189450696 (exact) |
| C9 | reconstruction exp(X)=U, Tr X=0, ‖X‖²=d² | 1.3×10⁻¹⁵ |

## 

## **2.2 The Weyl-integration pipeline**

Characters are evaluated by the Weyl formula and integrated against the SU(3) Haar measure on the maximal-torus grid. The pipeline is certified by Schur orthonormality and by an analytic control: the heat-kernel coefficients recovered by the same quadrature must equal d\_R e^{−tC₂(R)} in closed form.  
Table 2.2. Block-2 certification of the character pipeline (5 checks in the companion suite, 0 FAIL; the five are listed below).

| Check | Quantity | Result |
| ----- | :---: | :---: |
| W1 | Haar normalisation ∫dμ \= 1 | 0 (exact) |
| W3a | Schur diagonal ⟨χ\_R,χ\_R⟩ \= 1 | 2.2×10⁻¹⁶ |
| W3b | Schur off-diagonal ⟨χ\_R,χ\_S⟩ \= 0 | 1.1×10⁻¹⁶ |
| W4 | heat-kernel analytic control | 2.2×10⁻¹⁶ |
| W5 | C₂(1,0)=4/3, C₂(1,1)=3, C₂(2,0)=10/3 | matches ZS-S24 Table 10.1 |

# 

# **§3. The Lüscher Reduction of F-S24.18**

By the Lüscher criterion the tier-(ii) positivity (R2+) holds if and only if the temporal kernel has non-negative character coefficients. Two facts fix which kernel to test. First, ZS-S24 Theorem S24.14's own factor e^{−aL}, with L the link Laplace–Beltrami operator, has coefficients c\_R \= d\_R e^{−a C₂(R)/2} \> 0 automatically; this is the heat-kernel action, and under it F-S24.18 would close positive trivially. Second, ZS-S23 §3.1 established that the cellwise-constant, mass-lumped, lowest-order Whitney reduction of Tr(F ∧ ⋆F) yields Tr(Φ\_f²)/A\_f, which is a Manton (squared-geodesic) kernel exp(−(β/2N) d(U)²). The physically load-bearing question is therefore the Manton one.  
We record the exact status: the identity of the heat-kernel factor as e^{−aL} is DERIVED and confirms ZS-S24.14 is IMPORTED-PROVEN (it is the standard Menotti–Onofri construction). The identity of the Whitney reduction as Manton is DERIVED-CONDITIONAL: in the non-abelian case Φ\_f \= ∫\_f F is not exactly the plaquette holonomy, a gap ZS-S23 itself flagged. F-S24.18 is therefore closed below under that stated condition.

# 

# **§4. The Pre-Registered Sign Test (AN-S27.1)**

We register two hypotheses before computing. H0: all Manton c\_R ≥ 0 over p+q ≤ PQMAX for every tested β, so F-S24.18 closes positive. H1: some c\_R \< 0, grid-stable, so it closes negative. The decision statistic is ρ \= min\_R c\_R / max\_R |c\_R|; ρ \< −10⁻⁹ and stable under grid refinement accepts H1. Two controls are mandatory: the Wilson kernel must show no negative coefficient (Lüscher's theorem), and the heat kernel must be positive by construction. Grids M ∈ {180, 300, 480} and truncations PQMAX ∈ {10,12,14,16} are swept.  
Table 4.1. AN-S27.1: decision statistic ρ \= min c\_R / max|c\_R| by kernel and coupling. Wilson and heat-kernel are controls.

| β | Wilson (control) | Heat (control) | Manton | argmin (p,q) | verdict |
| ----- | :---: | :---: | :---: | :---: | :---: |
| 0.50 | −7.8×10⁻¹⁸ | −4.9×10⁻¹⁷ | −1.3473×10⁻² | (2,0) | H1 |
| 1.00 | \+1.9×10⁻¹⁷ | −4.1×10⁻¹⁷ | −2.1715×10⁻³ | (2,2) | H1 |
| 2.00 | \+1.7×10⁻¹⁴ | −5.8×10⁻¹⁷ | −1.2788×10⁻⁴ | (3,3) | H1 |
| 3.2497 | \+1.1×10⁻¹¹ | \+6.6×10⁻¹⁵ | −2.1704×10⁻⁶ | (5,5) | H1 |
| 4.00 | \+1.7×10⁻¹⁰ | \+4.8×10⁻¹² | −2.2511×10⁻⁷ | (5,5) | H1 |

Both controls pass at every β. The Manton statistic is grid-stable to five figures and truncation-stable: at β=3.2497 the minimum is ρ \= −2.170441×10⁻⁶ with argmin (5,5) for every PQMAX in {10,12,14,16}, an interior irrep of dimension 216, not a truncation boundary. H1 is accepted. Gate F-S24.18 closes negative on the Whitney/Manton route, at the status CLOSED-NEGATIVE-CONDITIONAL on the Whitney-to-Manton identification (gate F-S27.2). The witness is strengthened from bare grid-stability to a conservative convergence band: with deterministic Gauss–Legendre quadrature refined across M \= 40, 60, 80 (and reconfirmed at 40-digit mpmath in the standalone block), the (5,5) coefficient lies in c\_(5,5) ∈ \[−6.46×10⁻⁸, −6.41×10⁻⁸\], from the publication run (the suite’s \--full mode and the standalone block, both on the same M \= 40, 60, 80 Gauss–Legendre grid; the standalone repeats the accumulation at 40 digits, successive difference 8×10⁻¹¹). The FAST smoke mode uses the coarser M \= 32, 48 grid and returns the wider but equally zero-separated band \[−6.58, −6.33\]×10⁻⁸; the publication band is the one cited here. It is grid-converged and separated from zero. We state this precisely as a grid-converged, zero-separated numerical witness — NOT a rigorous interval enclosure: it carries no quadrature-remainder bound and no ball arithmetic, so the formal interval proof remains OPEN. Nothing in the conclusion depends on more than the 0-separation, which is robust across grids and precisions.

## 

## **4.1 The negativity is invisible to first order**

The negative coefficients begin only at dimension 45\. At the Z-Spin point the low irreps are all positive: c\_R/max|c| \= \+0.875 for the trivial, \+1.000 for 3 and 3̄, \+0.460 for 6̄, \+0.786 for 8\. These are exactly the irreps entering ZS-S24 Prop. S24.15′. Consequently the ZS-S24 first-order results — μ \= a₃ \+ a\_6̄, the 24 → 12 ⊕ 12 splitting, and Δ(g) \= (10/3)g² \+ \[a₈⁽⁵⁾ − |μ|\]g⁻² — are untouched by this run. The reflection-positivity failure is real but perturbatively invisible.

# 

# **§5. The Squared-Transfer Escape (Theorem-Candidate S27.1)**

**Theorem-Candidate S27.1 (status: stated under an explicit action decomposition, verified on the tested grid; a general theorem for arbitrary real gauge-invariant time-reflection-symmetric actions is broader than the cited Wilson-type results and is NOT claimed).** Let S be real, gauge invariant and time-reflection symmetric, satisfying (R1) and (S1) of ZS-S24 §4.4. Reflect about a plane containing sites. Then S \= S₊ \+ θ(S₊) \+ S₀(plane) with no term coupling t \> 0 to t \< 0 directly, and for every F in the positive-time algebra ⟨θ(F̄)F⟩ \= ∫dU\_plane e^{−S₀} |∫dU₊ e^{−S₊} F|² ≥ 0, which requires no condition on the character coefficients. Hence T² ≥ 0 always; T² \> 0 iff no coefficient vanishes; and H₂ \= −(1/2a) log T² is self-adjoint and bounded below on the even-time sublattice, with gap Δ⁽²⁾ \= log(|t₀|/|t₁|).  
Every hypothesis is one ZS-S24 already proved: (R1) is its own declaration, (S1) is closed by inspection at F-S24.19, time-reflection symmetry is part of (R2), and the slab support is Theorem S24.12. We separate two claims at different status: T² ≥ 0 under the stated decomposition is a theorem-candidate, while the statement that the physical gap is unchanged holds because the top of the spectrum does not reorder under the absolute-value ordering — this we VERIFY on the tested coupling grid (§5.1), not prove in general.

## 

## **5.1 The gap is unchanged**

Theorem-Candidate S27.1 replaces the signed ordering of the transfer spectrum by the absolute ordering. A pre-registered check (E2) asks whether taking absolute values reorders the top of the spectrum, which would change the physical gap. It does not, at any tested coupling: at β=3.2497 the top two eigenvalues under signed and absolute ordering are the same pair, and |Δ\_T − Δ\_T²| \= 0 exactly. The reason is quantitative — the negative coefficients have magnitude ≤ 10⁻⁶ — so the same smallness that hides the failure from first-order perturbation theory also keeps it out of the spectral top. This is one fact, not two.

# 

# **§6. The Single-Face Gap Function ε₀(g)**

The physical scale requires the dimensionless gap ε₀(g) across the whole coupling range, not only its strong-coupling end. On a single closed n-link face the Kogut–Susskind Hamiltonian in the character basis is H/g² \= (n/2) C₂(R) − (1/g⁴) Re Tr U, so the entire crossover is governed by the single parameter x \= 1/g⁴, with no free normalisation once the Wilson/KS form is declared. The magnetic term is the symmetric hopping matrix of 3 ⊗ R and 3̄ ⊗ R.  
The certification is exact: at x \= 0 the pentagon (n=5) gap is 10/3 g² and the hexagon (n=6) gap is 4 g², reproducing ZS-S24 Theorem S24.4 (Δ\_E,1 and Δ\_E,2) to ten digits. Truncation converges by P \= 6 to seven figures. Away from x=0 the gap/g² is a mild function with a minimum near g² ≈ 1; because the carrier has no continuum limit (ZS-S24 NC-S24.1), ε₀ does not tend to zero at weak coupling. The correction to the leading (10/3)g² is at most a few percent at the Z-Spin point (ratio 0.96 at g²=1.85).  
Table 6.1. Single-face Lanczos gap versus the ZS-S24 leading strong-coupling term (pentagon).

| g² | λ\_t \= 3g² | gap/g² | ε₀ Lanczos | (10/3)g² | ratio |
| ----- | :---: | :---: | :---: | :---: | :---: |
| 4.000 | 12.00 | 3.30260 | 13.2104 | 13.3333 | 0.9908 |
| 1.846 | 5.54 | 3.19883 | 5.9051 | 6.1533 | 0.9596 |
| 1.000 | 3.00 | 3.00335 | 3.0034 | 3.3333 | 0.9010 |
| 0.600 | 1.80 | 3.51176 | 2.1071 | 2.0000 | 1.0535 |

# 

# **§7. The Scale-Setting Route and its Scheme**

ZS-S18 §6.3 proposed the fixed point λ\_t \= 12π α\_s^{S14}(m\_{0++}/ε₀(λ\_t)), which would fix the lattice spacing without any lattice input. Executed literally in the bare-lattice scheme, with α\_s anchored at 11/93 and run in MS-bar, this fixed point has no root: F(λ) − λ \> 0 everywhere F is defined, with minimum \+3.12. The scale a\_TI⁻¹ implied by ε₀ ≈ 6 is below Λ\_QCD, where the perturbative α\_s the recipe calls for does not exist.  
The failure is a scheme error, not a corpus defect. The coupling in the ZS-S24 Hamiltonian is the bare lattice coupling g\_lat(a), not g\_MS̄(1/a); the two differ by the finite renormalisation encoded in the Λ ratio. Reinstating Λ\_lat \= Λ\_MS̄/28.809 (Hasenfratz–Hasenfratz; Dashen–Gross) produces a root: λ\_t\* \= 4.74 (Wilson), a\_TI ≈ 0.34 GeV. This retraction, R27-2, corrects the Block-5 diagnosis that attributed the 87-fold mismatch to a missing full gap function.

## 

## **7.1 Two corpus values were never required to meet**

A related retraction, R27-3, concerns the apparent 35% inconsistency between λ\_t \= 5.539 and m(0++) \= 1.7906 GeV. These are set by two independent routes: m(0++) \= vA/Q is algebraic, with λ₁ cancelling topologically and no dependence on the lattice spacing (ZS-S19 Table 9.1); λ\_t \= g\_hf(∞)/0.298805 is lattice, with no dependence on v, A, Q. Nothing in the corpus multiplies one by a spacing to obtain the other; the a\_TI that would connect them is exactly what F-S18.13 leaves open. The 35% figure is a property of imposing the naive Wilson scale-setting, not a contradiction between corpus values.

# 

# **§8. The Heat-Kernel Scheme and its Λ Ratio (scheme-estimate)**

The tension between §4 (Manton not reflection positive) and §7 (scale-setting) is resolved by a single choice: adopt the heat-kernel discretisation, which is ZS-S24 Theorem S24.14's own T\_a \= e^{−aL}. Under it (a) reflection positivity holds automatically, since c\_R \= d\_R e^{−g²C₂/2} \> 0 (§3), and (b) the Λ ratio to Wilson is a known, computable finite shift. This is a declaration, not a theorem: it replaces the naive Whitney reduction by the heat-kernel action, and the honest cost is that it selects a standard lattice action rather than deriving one from the Z-Spin geometry — a tension §8.2 records rather than hides.

## 

## **8.1 The SU(3) finite shift from the SU(2) anchor**

The heat-kernel action is normalised to coincide with Wilson in the continuum; the Λ ratio is set by the finite coupling shift in its short-time expansion, K\_t(U) \= (4πt)^{−D/2} e^{−d²/4t}\[1 \+ (t/6)R\_scalar \+ …\], whose curvature term is the shift. For SU(2) the shift is known exactly: β\_HK \= 4/(aq²) \+ 1/3, i.e. Δ(1/g²) \= 1/12 and Λ\_HK/Λ\_W(SU2) \= 2.45. The SU(3) value follows from the convention-free curvature ratio R\_Tr(SU3)/R\_Tr(SU2) \= (dimG₃/2·3)/(dimG₂/2·2) \= 16/9, giving Δβ(SU3) \= 16/27, Δ(1/g²) \= 8/81, and with b₀(SU3) \= 11/(16π²),  
*Λ\_HK / Λ\_W (SU3) \= exp\[(8/81)/(2b₀)\] \= 2.03 .*  
Three physically motivated curvature conventions bracket this: \[1.82, 2.03, 4.93\], with the two smaller favoured because the SU(2) anchor already fixes the overall size. We report Λ\_HK/Λ\_W(SU3) ≈ 1.8–2.4.

## 

## **8.2 The λ\_t residual: both natural actions overshoot**

Tracing the derived ratio Λ\_HK/Λ\_W \= 2.03 through the scale-setting map gives λ\_t \= 6.26, whereas the lattice-derived value is 5.539: the heat-kernel discretisation OVERSHOOTS by \+13%. The Wilson scheme undershoots (λ\_t \= 4.74). The value of the ratio that would reproduce 5.539 exactly is 1.544, which lies between Wilson (1.0) and heat-kernel (2.03).  
The v1.0 conjecture that the corpus’s own Manton action — whose low character coefficients lie between Wilson and heat-kernel — would therefore carry a Λ ratio in \[1, 2\] bracketing 1.544 is REFUTED here (retraction R27-4). A continuum-matched weak-coupling computation of the three actions’ mean-plaquette free energies, with the leading slopes agreed to 0.5% as a control, orders the quartic-to-quadratic ratios as |q|\_Manton \= 0.400 \> |q|\_Heat \= 0.305 \> |q|\_Wilson \= 0.058. The weak-coupling quartic ordering suggests, but does not prove, a larger Manton finite shift than the heat-kernel shift. A direct determination of ΛManton/ΛW\\Lambda\_{\\rm Manton}/\\Lambda\_WΛManton/ΛW remains OPEN. ; a direct determination of Λ\_Manton/Λ\_W remains OPEN (scheme-diagnostic R27-4). Were that indication confirmed, the resulting scale-setting value would overshoot λt=5.539\\lambda\_t=5.539λt=5.539 by more than 13%.   
The scheme comparison therefore gives a negative-leaning verdict: the sign of the scheme correction is favourable (both natural actions move λ\_t up from the Wilson undershoot toward and past the lattice value), but the magnitude for both reflection-positive candidate discretisations overshoots. The MeV bridge does not close by scheme adoption. What remains is a single, quantified, falsifiable residual: the reflection-positive natural discretisation predicts λ\_t about 13% above the corpus’s lattice-derived value. Whether that residual is closed by the finite-cell corrections of the actual K\_TI carrier (as opposed to the single-plaquette proxy used here) is the next gate, F-S27.3.

## 

## **8.3 Is the residual a finite-cell artefact? (F-S27.3)**

The overshoot was computed with the single-face gap (10/3)g². The carrier K\_TI has 90 links and 32 faces; the single face omits all inter-face coupling. We test whether reinstating it closes the tension. At strong coupling the lightest excitation is a single fundamental flux loop around one face, with electric cost (n\_f/2)(4/3)g²: 10/3 g² for a pentagon, 4 g² for a hexagon. The magnetic term hops such a loop between faces sharing an edge, so the one-loop sector is a tight-binding Hamiltonian on the FACE-ADJACENCY graph of K\_TI, H\_eff/g² \= diag(E\_f) − x² C⊙A, with x \= 1/g⁴ and A the 32×32 adjacency built exactly from the truncated-icosahedron geometry (12 pentagons each adjacent to 5 hexagons; 20 hexagons each adjacent to 3 pentagons and 3 hexagons; 90 shared edges).  
The inter-face hopping is second order in x with a group/energy coefficient c\_ij \= 1/E\_i \+ 1/E\_j (two-loop intermediate; non-adjacent hops are area-law suppressed). Diagonalising the full 32×32 effective Hamiltonian, and using the single-face Lanczos gap as the diagonal so that the face self-energy is included, the gap at the self-consistent point (g² \= 2.045, x² \= 0.057, inside the strong-coupling domain) is lowered by only about 2%. Propagated through scale-setting with the heat-kernel Λ ratio, λ\_t moves from 6.260 (naive) to 6.157 (with self-energy) to 6.134 (with inter-face hopping). The one-loop-sector corrections close only about one-sixth of the \+13% overshoot, and the conclusion is robust: doubling the hopping amplitude still leaves λ\_t \= 6.05, a \+9.3% residual.  
F-S27.3 therefore returns a definite answer: the leading correction within the complete 32-face one-flux-loop sector does not remove the 13% overshoot; higher-order and multi-loop corrections remain OPEN. A residual of about \+11% survives at leading order within the 32-face one-flux-loop effective sector. The corpus’s lattice-derived λ\_t \= 5.539 and its natural reflection-positive discretisation, which predicts λ\_t ≈ 6.1, genuinely disagree. The honest readings are three: either the ZS-S18 extraction of 5.539 from the Athenodorou–Teper data (via the geometric factor 0.298805) is what the discretisation challenges; or λ\_t ≈ 6.1 is a genuine prediction to be tested against improved lattice input; or the strong-coupling truncation, though inside its nominal domain here, is itself the limitation. Distinguishing these is gate F-S27.4.

## 

## **8.4 The residual on the observable m(2++)/m(0++) (F-S27.4)**

The λ\_t residual admits three readings: that the ZS-S18 extraction of 5.539 is challenged; that λ\_t ≈ 6.1 is a genuine prediction; or that the strong-coupling truncation is the limitation. They are distinguished by mapping the abstract coupling onto a measured quantity. In the corpus, λ\_t is not independent: it is the continuum glueball ratio repackaged through λ\_t \= g\_hf/0.298805 with g\_hf \= (4/3)(R² − 1\) and R \= m(2++)/m(0++). Combining, R² \= 1 \+ ¾·0.298805·λ\_t, so the value λ\_t \= 5.539 is exactly the lattice R \= 1.497 in disguise.  
Under this map the discretisation’s λ\_t \= 6.134 predicts R \= 1.541, a \+2.9% overshoot of the lattice 1.497: the square root compresses the 11% coupling tension to under 3% in the observable. For comparison, the corpus’s kinematic Layer-Lift predicts R \= 1.390, a −7.1% undershoot that closed F-S18.5 negative. The dynamical prediction is thus closer to the lattice than the corpus’s own kinematic one, and on the opposite side, so the two bracket the datum: 1.390 (kinematic) \< 1.497 (lattice) \< 1.541 (dynamical).  
This discriminates the readings. Reading 1 would require replacing 0.298805 by 0.270 to absorb the residual, a 9.7% shift with no corpus mechanism (0.298805 is already unidentified at NC-S18.6); it is disfavoured. Readings 2 and 3 share the residual: the discretisation yields the internal ratio m\_H/m\_A \= 1.54 (mapped to a physical prediction only if F-S27.1 closes) that overshoots by 2.9%, and the finite-cell correction of §8.3 lowers the gap, hence λ\_t, hence R toward the data — the sign of the sub-leading strong-coupling correction is exactly the one that removes the overshoot. Closing the residual quantitatively requires the sub-leading strong-coupling spectrum (orders x⁴, x⁶), registered as F-S27.1-diag. The honest status is a \+2.9% numerical proximity that becomes an observable comparison only under the conditional F-S27.1 reading, dynamical in origin and reducible in principle — not a corpus falsification.

## 

## **8.5 The internal two-mode hyperfine ratio (gate F-S27.1)**

Section 8.4 obtained R by converting λ\_t through the corpus relation. To make R a spectral quantity, we diagonalise the operator directly. The 2++ is not a single face-loop but the tensor (H, spin-2) channel of the two-gluon sector. ZS-S17 established the exact operator identity on the T₁ active space: the coproduct defect is I\_Z \= g·S₁·S₂ and the mass-squared referral is Q\_Z \= ¼(I\_Z \+ 2g·I), with T₁⊗T₁ \= A\_g ⊕ T₁ ⊕ H (SO(3): 1⊗1 \= 0⊕1⊕2). Building S₁·S₂ explicitly from spin-1 matrices reproduces its spectrum {−2, −1, \+1} with degeneracies {1, 3, 5}, confirming the A\_g/T₁/H assignment; Q\_Z then has eigenvalues {0, g/4, 3g/4} on {A\_g, T₁, H}, so M²/M₀² \= 1 for the 0++ and 1 \+ ¾g for the 2++.  
With the dynamical coupling g\_hf \= 0.298805·λ\_t and the discretisation value λ\_t \= 6.134, the diagonalisation gives m(0++)/m₀ \= 1 (A\_g), m(2++)/m₀ \= 1.541 (H), and R \= m(2++)/m(0++) \= 1.541 as an eigenvalue ratio. For comparison the kinematic value g \= λ₁ gives R \= 1.390 and the lattice-repackaged g\_hf \= 1.655 gives R \= 1.497, both reproduced by the same operator. Crucially the coupling here is the discretisation λ\_t, not the lattice glueball ratio, so R \= 1.541 is now independent of the datum it is confronted with; its only residual input is the exchange coefficient 0.298805, which is DERIVED-PERT-COND in ZS-S18. The operator additionally predicts the intermediate 1+- (T₁) glueball at m/m₀ \= 1.208 — a new internal ratio (physical identification conditional on F-S27.1) the conversion-only route could not yield.  
F-S27.1-diag thus upgrades the \+2.9% overshoot of §8.4 from a converted number to an internal eigenvalue ratio: the two-gluon operator places the H isotype at m\_H/m\_A \= 1.541, with A\_g and H at degeneracies {1, 5}. Whether this is the physical m(2++)/m(0++) \= 1.497 is exactly the open gate F-S27.1, so the proximity is indicative, not a confirmed identification. Fully removing the remaining dependence — deriving 0.298805 from the K\_TI two-gluon exchange rather than importing it — is exactly ZS-S18 Gate C (F-S18.4), which remains open; that computation, together with the isotype-to-spin gate F-S27.1, is what a parameter-free physical prediction would require end to end.

## 

## **8.6 Is the last coefficient external? Gate-C accounting**

Section 8.5 left R \= 1.541 dependent on the exchange coefficient 0.298805, described in v1.5 as an outside-world input. That description is corrected here (correction R27-5): 0.298805 is corpus-internal. ZS-S18 Corollary S18.6C gives g\_hf(N)/λ\_t \= G\_exch \+ (4/3)(s(N)/N)/√λ₁, where G\_exch \= (9/4)√λ₁(c₁² \+ c\_{h,pol}²) \= 0.313264 is a closed form (Theorem S18.6A′, DERIVED, exact and N-independent at O(g²)), and the seagull s(N) is computed from the truncated-icosahedron vertex tensor. No external number enters; reconstructing the decomposition reproduces G(3) \= 0.298223 and G\_∞ \= 0.298805 from the corpus channel coefficients.  
The weight of the two ingredients is asymmetric. Using the DERIVED exchange closed form alone, g\_hf \= 0.313264·λ\_t gives R \= 1.562 (+4.4% vs lattice); the numerical seagull then refines this to R \= 1.540 (+2.9%), a −1.4% shift. So R is about 96% carried by the closed form, and the one numerical ingredient moves it by 0.022 absolute — in the right direction, toward the data. The glueball ratio therefore imports no external fitted number — it is built from the discretisation λ\_t, the DERIVED exchange, and a corpus-computed seagull — but it is not a parameter-free physical prediction: it stays behind the isotype-to-spin gate F-S27.1 and the scheme-estimate status of the Λ ratio.  
Two internal conditions remain, and both plausibly reduce the residual overshoot. The seagull is numerical rather than closed-form; deriving it (the Magnus quartic route ZS-S18 hands to ZS-S19) would lift S18.6C from COMPUTED to DERIVED but move R by at most its present 1.4%. More importantly, the relation g\_hf \= G·λ\_t is O(g²), used at λ\_t ≈ 6 outside its nominal domain (ZS-S18 NC-S18.9); the O(g⁴) coefficient is unknown, and if higher orders screen the hyperfine coupling — as strong-coupling corrections generically do — R falls further toward the lattice. Testing this is the full non-perturbative Gate C: the A\_g (dim 12\) and H (dim 140\) blocks of the 496-dimensional two-gluon Sym² space by sparse Lanczos (ZS-S18 F-S18.4, open). That computation, not this one, would close the \+2.9% into a controlled number; the present work reduces the question to it and shows the sign of the two computed corrections move the ratio toward the lattice value; the signs of the uncomputed corrections remain open.

# 

# **§9. Conclusion**

F-S24.18 is closed by a finite sign test, at the status CLOSED-NEGATIVE-CONDITIONAL on the Whitney-to-Manton identification: the Manton temporal kernel is not reflection positive on SU(3), the failure confined to irreps of dimension ≥ 45 and invisible to the ZS-S24 first-order spectrum. The gap survives via site-reflection positivity and the squared transfer operator (a theorem-candidate under the stated decomposition, gap-unchanged verified on the tested grid). The dimensional bridge does not fail at the reflection-positivity gate or at a missing full gap function, as two corrected diagnoses had it, but at a scheme quantity, the Λ ratio of the corpus action — a scheme-estimate that overshoots. The heat-kernel discretisation (a canonical reflection-positive choice aligned with the Laplace–Beltrami factor; Wilson is equally reflection positive, so “unique” is not claimed) gives a scheme-estimated Λ ratio ≈ 2.03 and λ\_t ≈ 6.26; the Manton action plausibly overshoots more (scheme-diagnostic R27-4; Λ\_Manton not directly computed). Diagonalising the one-flux-loop effective sector on the 32-face adjacency graph (a carrier-wide one-loop truncation, not a diagonalisation of the full 90-link SU(3) Hilbert space) closes only about one-sixth of the overshoot within this sector. Mapped onto the internal ratio the residual is \+2.9%: the operator gives m\_H/m\_A \= 1.541, whose proximity to the 3+1 lattice m(2++)/m(0++) \= 1.497 is indicative only, since identifying the internal H isotype with the physical 2++ is the open gate F-S27.1. The two-gluon operator makes m\_H/m\_A \= 1.541 an internal eigenvalue ratio, with A\_g and H at degeneracies {1, 5} and an intermediate T₁ mode at 1.208; their physical identification is not asserted.  
The net movement of this paper is to convert a five-stage obstruction into a single, sharp, conditional number: the discretisation yields the internal ratio (mapped to a physical glueball ratio only if F-S27.1 closes) m\_H/m\_A corresponding to m(2++)/m(0++) \= 1.541 against the lattice 1.497, a \+2.9% overshoot. It arrives at this through F-S24.18 (closed negative by sign), the squared-transfer escape, the Λ-ratio overshoot, the 32-face one-flux-loop-sector finite-cell computation, and finally the map onto the observable, which compresses an 11% coupling tension to under 3% on a measured ratio and places the dynamical prediction closer to the data than the corpus’s own kinematic one. No physical MeV prediction is claimed. The bridge is not crossed, but it is narrowed to a \+2.9% observable overshoot whose sign the sub-leading strong-coupling spectrum should reduce (F-S27.1-diag). By the map onto the observable and the direct two-gluon diagonalisation, the framework yields the internal ratios m\_H/m\_A \= 1.541 and, conditional on F-S27.1, would map these to m(2++)/m(0++) and m(1+-)/m(0++) \= 1.208 as operator eigenvalue ratios, using its own discretisation coupling and — once the exchange coefficient is recognised as corpus-internal (closed-form exchange plus a geometry-computed seagull, R27-5) — zero-fit (importing no external fitted number, though resting on scheme and scale anchors). The DERIVED closed form alone gives R \= 1.562, the seagull refining it to 1.540, so the ratio imports no external number, though it is not a parameter-free physical prediction: it stays conditional on the isotype-to-spin gate F-S27.1, the scheme-estimate Λ ratio, the seagull’s numerical status, and the non-perturbative validity of the O(g²) hyperfine relation at λ\_t ≈ 6 (ZS-S18 Gate C, open) — with the two computed corrections moving toward the data and the uncomputed ones open. That a self-consistent framework yields so specific, reducible, and now spectrally-grounded a target is, by the corpus’s own standards, the intended outcome.

# 

# **Acknowledgements & Code Availability**

This work was carried out with AI-assisted structural verification and adversarial review. All executable checks reported in this paper are consolidated in a single companion suite, zs\_s27\_verify\_v1\_6.py (69 checks; 8 carry proof weight — 5 exact-arithmetic identities and 3 exhaustive enumerations — the remaining 61 being floating-point verifications, numerical bands, controls, cross-checks, declarations, and corrections). The FAST mode is a non-publication smoke and regression run; the publication run uses \--full. A standalone high-precision block, zs\_s27\_block15\_interval\_cert\_v0\_1.py, evaluates the central (5,5) coefficient at 40-digit mpmath. Earlier zs\_s25\_\* development blocks are internal audit history, not required to reproduce this release. The suite is fail-closed on all A, E, V, N, K and X checks (the central numerical band included), uses deterministic Gauss–Legendre quadrature with an exact coroot-lattice geodesic search, and writes no files; the central (5,5) coefficient is additionally evaluated at 40-digit mpmath in the standalone block. The reflection-positivity result rests on externally proven mathematics (Lüscher 1977; Osterwalder–Seiler 1978\) placed in the Z-Spin carrier setting.

# 

# **Appendix A. Retraction Ledger**

This paper's development recorded five corrections (R27-1..R27-5), listed here as part of the audit trail. R27-1: the claim that the earlier SU(3) probe mis-implemented the geodesic distance (the fundamental-alcove rule) is WITHDRAWN; that rule agrees with the certified minimiser to machine precision, and the earlier inconclusiveness was due to irrep truncation, not the alcove. R27-2: the diagnosis that the α\_s fixed point fails because of a missing full gap function (NC-S24.3) is WITHDRAWN; it fails because of a bare-lattice-versus-MS̄ scheme error, repaired by the Λ ratio. R27-3: the claim of a 35% internal inconsistency between λ\_t and m(0++) is WITHDRAWN; the two are independent quantities the corpus never required to coincide. R27-4: the v1.0 §8.2 conjecture that the Manton Λ ratio would fall in \[1,2\] and bracket the required 1.544 is WITHDRAWN; R27-4: the prior conjecture that the Manton Λ\\LambdaΛ ratio must lie in \[1,2\]\[1,2\]\[1,2\] is WITHDRAWN. The computed quartic ordering suggests a larger finite shift than heat-kernel but does not determine ΛManton/ΛW\\Lambda\_{\\rm Manton}/\\Lambda\_WΛManton/ΛW, which remains OPEN. R27-5: the v1.5 characterisation of the exchange coefficient 0.298805 as an outside-world dependency is CORRECTED; it is corpus-internal, decomposing into the DERIVED closed-form exchange G\_exch \= 0.313264 and a seagull computed from the truncated-icosahedron geometry, so the glueball ratio uses no external number.

# 

# **Appendix B. Anti-Numerology Register**

AN-S27.1 (the sign test) contacts no measured quantity and needs no Monte-Carlo null; its controls (Wilson, heat kernel) validate the pipeline's discriminating power. AN-S27.2 (scale-setting) does contact the lattice λ\_t: a pre-registered null with Λ\_MS̄ \~ U(180,320) MeV, m(0++) \~ U(1.4,2.2) GeV, Λ ratio \~ U(10,60), and ε₀ model and face count varied, over 20000 draws, gives P(|λ\_t\*−5.539|/5.539 \< 15%) \= 0.316. The 15% agreement is therefore not significant, and the scale-setting result is reported as HELD, not as support. The bracketing of the required 1.544 by the heat-kernel scalings \[1.49, 1.82\] is a NON-CLAIM: two of four conventions land there and the target inherits the naive scale-setting.

# 

# **References**

\[1\] M. Lüscher, “Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories,” Commun. Math. Phys. 54, 283 (1977).  
\[2\] K. Osterwalder and E. Seiler, “Gauge field theories on a lattice,” Ann. Phys. 110, 440 (1978).  
\[3\] P. Menotti and E. Onofri, “The action of SU(N) lattice gauge theory in terms of the heat kernel on the group manifold,” Nucl. Phys. B 190, 288 (1981).  
\[4\] E. Onofri, “SU(N) lattice gauge theory with Villain’s action,” Nuovo Cim. A 66, 293 (1981).  
\[5\] N. S. Manton, “An alternative action for lattice gauge theories,” Phys. Lett. B 96, 328 (1980).  
\[6\] A. Hasenfratz and P. Hasenfratz, “The connection between the Λ parameters of lattice and continuum QCD,” Phys. Lett. B 93, 165 (1980).  
\[7\] R. Dashen and D. J. Gross, “The relationship between lattice and continuum definitions of the gauge theory coupling,” Phys. Rev. D 23, 2340 (1981).  
\[8\] M. Göckeler et al., “Perturbative determination of c\_SW …,” arXiv:0807.0345 (2008), eqs. 71–72.  
\[9\] C. Lanczos, “An iteration method for the solution of the eigenvalue problem of linear differential and integral operators,” J. Res. Natl. Bur. Stand. 45, 255 (1950).  
\[10\] A. Athenodorou and M. Teper, “The glueball spectrum of SU(3) gauge theory in 3+1 dimensions,” JHEP 11, 172 (2020); “SU(N) gauge theories in 3+1 dimensions,” JHEP 12, 082 (2021).  
\[11\] A. Jaffe and B. Janssens, “Reflection positive doubles,” arXiv:1607.07126 (2016).  
\[12\] A. Skouroupathis and H. Panagopoulos, “Λ-parameter of lattice QCD with Symanzik improved gluon actions,” arXiv:0709.3239 (2007).  
\[13\] ZS-S24 v1.9, ZS-S23 v1.3, ZS-S21 v1.2, ZS-S19 v1.3, ZS-S18 v1.6, ZS-S17 v2.2, ZS-S14 v2.0, ZS-S7 (Z-Spin Cosmology Collaboration, 2026).

# 

# **Version History**

This paper began as the internal draft ZS-S25 v1.6 and was renumbered ZS-S27 for public release because ZS-S25 was already assigned in the corpus (to the gravitational-redirection paper). The scientific content — the character-coefficient sign test closing F-S24.18 negative-conditional, the squared-transfer route, the heat-kernel scheme analysis, the one-loop-sector finite-cell computation, the two-gluon internal-isotype ratios, and the Gate-C decomposition of the exchange coefficient — was stable from the first internal draft; no scientific number has changed across the public revisions.  
The public revision sequence v1.0–v1.5 responded to successive external audits and consisted entirely of status-honesty and internal-consistency corrections: renaming residual ZS-S25 identifiers to ZS-S27; downgrading the Manton negative-coefficient result from a headline to a conditional close (gate F-S27.2) and its witness to a grid-converged, zero-separated numerical band (with a formal interval enclosure left OPEN); marking the heat-kernel Λ ratio as a scheme-estimate; keeping the internal isotypes A\_g, T₁, H distinct from the physical J^PC glueballs behind the intertwiner gate F-S27.1; restating the glueball ratio as zero-fit (importing no fitted number, but resting on scheme and scale anchors) rather than parameter-free; reclassifying the verification ledger so that only the eight exact and exhaustive checks carry proof weight; making mpmath a hard dependency and unifying the central band to a single M \= 40, 60, 80 grid; and, in v1.5, unifying the finite-cell coupling to λ\_t \= 6.134 throughout, adding the observable-reading gate F-S27.4 to the summary table, and softening the Lanczos row to “exact at x \= 0, verified to ten digits across g”. The present release is v1.6; the detailed per-version change logs are retained in the internal audit trail (ZS-S25X, not for citation).