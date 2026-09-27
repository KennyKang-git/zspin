**ZS-M51**  
**Lambert–Dottie Stability of the Exponential Fixed-Point Family, with a Fixed-Point Census and Certified Periodic Exponential Words**

**The Exact Critical Threshold s\_c \= e^{sin ρ}, the General Lambert Mean Identity, the Saddle/Repeller Census of the Cyclotomic Skew Product, and a Krawczyk-Certified Coexistence — with Polygon Tetration as an Arithmetic Specialization**

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Date:** July 2026  
**Theme / Paper code:** Mathematical Spine — **ZS-M51**  
**Parents:** ZS-M1 v1.0 (fixed point z\\\*, polygon family, n\_c); ZS-M50 v1.3 (two directions, two-clock cocycle)

**Verification: 93/93 checks PASS, including two Krawczyk-certified cycles (four interval assertions) | Zero Free Parameters | Gates H-UFC, H-2s1u CLOSED-NEGATIVE; H-PH, H-ORBIT, H-INV OPEN**

***Structure (external-first).** Part I is standalone complex/dynamical mathematics about the one-parameter exponential family f\_s(z) \= e^{isz}; it does not use any Z-Spin constant. Part II specializes to s \= 2π/n (polygon tetration). Part III records the Z-Spin corpus interface. This ordering makes the general theorems primary and the corpus recovery (n\_c) a corollary, not the headline.  **This is the terminal v1.3 revision.** It integrates three external review rounds. v1.0 → v1.1 corrected the genre and the frozen/genuine confusion. **v1.1 → v1.2** (i) gave the full **saddle/repeller/neutral** classification of the base-fixed points (the stable dimension is \*not\* uniformly 2), (ii) fixed the census count to **⌈x\_c(m−1)⌉−1**, (iii) upgraded the periodic-orbit coexistence to **PROVEN** via a **Krawczyk interval certification**, (iv) split the too-broad "global partial hyperbolicity is false" into **H-UFC/H-2s1u CLOSED-NEGATIVE** vs the still-**OPEN** centre-type gate **H-PH**, (v) unified the two average identities into one **General Lambert Mean Identity**, and (vi) corrected the branch-cut statement and the period definition. **v1.2 → v1.3** (this version) is a closing polish with **no new mathematics**: it corrects the T1 Lambert-substitution sign (W \= −isz), adds **Lemma T4.0 (injectivity)** to complete the measure-zero argument, re-scopes the Krawczyk uniqueness as **local (in-box)**, and gives the external references in full (Walkden–Withers; Urbański–Zdunik). H-INV, H-ORBIT, and the arithmetic-word-distribution programme are handed to ZS-M52.*

**§0. Abstract**

For s \> 0 let f\_s(z) \= e^{isz} be the exponential self-map of ℂ. Its principal fixed point is z\\\*\_s \= −W₀(−is)/(is), and its multiplier collapses to a single Lambert curve, **|f\_s′(z\\\*\_s)| \= |W₀(−is)|** (Theorem T1). Writing W₀(−is) \= u − iv with u,v \> 0, the parametrisation u \= v tan v, |W₀| \= v sec v shows v ↦ s(v) \= v sec v·e^{v tan v} is a strictly increasing bijection (0, π/2) → (0, ∞), giving **analytic** existence and uniqueness of the stability threshold; the boundary |W₀| \= 1 is v \= cos v, solved by the **Dottie number ρ \= cos ρ \= 0.7390851332…**, so

**s\_c \= e^{sin ρ} \= 1.9613088464595… (Theorem T2):**

for s \< s\_c the fixed point is attracting, for s \> s\_c repelling. A single closed identity governs all Lambert averages — the **General Lambert Mean Identity**

**(1/X)∫₀^X log|W₀(−2πix)| dx \= log|W\_X| − Re W\_X/|W\_X|², W\_X := W₀(−2πiX) (Theorem T3),**

whose two natural evaluations give the band mean −sin ρ (at X \= x\_c) and the full-base mean Λ\_sec \= \+0.00186237… (at X \= 1).

Over the expanding base T\_m(x) \= {mx} on \[0,1) we study the fibred cocycle F\_m(z,x) \= (e^{2πixz}, {mx}). The frozen fixed-point family z\\\*(x) is **not** an invariant graph — z\\\*(T\_m x) ≠ z\\\*(x), and the exceptional coincidence set has **Lebesgue measure zero** (Theorem T4, with a per-branch analytic argument). At the genuine invariant sets the dynamics is exact: each interior base-fixed point x₀ \= j/(m−1) gives a genuine hyperbolic fixed point of F\_m whose real 3×3 Jacobian has eigenvalue moduli {|W₀(−2πix₀)|, |W₀(−2πix₀)|, m}; hence it is a **saddle of stable index 2** when x₀ \< x\_c and a **three-dimensional repeller (unstable index 3\)** when x₀ \> x\_c (neutral at x₀ \= x\_c) — the **Fixed-Point Census Theorem** (Theorem T5–T6), with contracting-saddle count **N\_m \= ⌈x\_c(m−1)⌉−1** and N\_m/(m−1) → x\_c; the first contracting saddle appears at **m \= 5, x₀ \= ¼**. Finally, viewing a cyclotomic base cycle as an arithmetic word x \= (x₀,…,x\_{q−1}) with **exponential word map** G\_x \= f\_{x\_{q−1}}∘⋯∘f\_{x\_0} and **monodromy multiplier** M\_x \= ∏ 2πi x\_j z\_{j+1}, we **certify by the Krawczyk operator** (rigorous complex-interval arithmetic) a **locally unique** attracting fibre cycle — unique within an explicitly certified box — for the word (1/7; m=2) (|G′| ∈ \[0.198, 0.208\] \< 1\) and a **locally unique** repelling fibre cycle for (1/3; m=2) (|G′| ∈ \[1.609, 1.643\] \> 1\) — Theorem T7. Their coexistence **rules out** any global uniformly contracting fibre and any global {dim E^s \= 2, dim E^u \= 1} splitting (gates H-UFC, H-2s1u **CLOSED-NEGATIVE**), while it does **not** rule out a centre-type partially hyperbolic structure on a compact invariant set (H-PH **OPEN**).

**Part II** substitutes s \= 2π/n: |f′(z\\\*(1/n))| \= |W₀(−2πi/n)| reproduces ZS-M1's polygon-stability table, the triangle (n=3) is the unique unstable polygon, and s\_c \= e^{sin ρ} gives **n\_c \= 2π/s\_c \= 2π e^{−sin ρ} \= 3.20356751489…**, matching ZS-M1's critical index exactly; the frozen exponent equals ZS-M1's Lyapunov–Lambert rapidity, χ\_fr(x) \= log(2πx) − α(x). **Part III** records the corpus interface (two-clock cocycle, LOCKED n\_c, F47 handoff). Zero free parameters; anti-numerology passes as inequalities. Verification: **93/93 PASS**.

**Epistemic Status Legend**

| Status | Meaning |
| ----- | ----- |
| **PROVEN** | Exact mathematical fact (standard mathematics alone), or exact algebra \+ a machine-checked identity, **or a rigorous computer-assisted (interval) certification.** |
| **VERIFIED** | High-precision numerical confirmation (regression, not a proof). |
| **DERIVED** | Follows from the object family \+ PROVEN inputs; zero free parameters. |
| **IMPORTED-PROVEN** | Proved in a parent paper / externally, cited, used without re-proof. |
| **LOCKED** | A constant fixed upstream; not re-derived here. |
| **CLOSED-NEGATIVE** | A gate resolved in the negative (the asserted structure provably fails). |
| **OPEN** | Well-posed; closure condition stated; unresolved. |
| **NON-CLAIM / RETRACTED / RETRACTED-as-numerology** | As standard. |

**PART I — STANDALONE MATHEMATICS (no Z-Spin constant used)**

**§1. The Exponential Fixed-Point Family and the Multiplier Theorem**

For a real parameter s \> 0 consider the entire self-map f\_s(z) \= e^{isz} of ℂ.

**Theorem T1 (Multiplier Theorem). \[PROVEN\]**  
The principal fixed point of f\_s is

**z\\\*\_s \= −W₀(−is)/(is),   and   |f\_s′(z\\\*\_s)| \= |W₀(−is)| .    (1.1)**

\*Proof.\* Put a \= is and **W \= −az \= −isz** (the sign is essential). At a fixed point z \= e^{az}, so e^{az} \= z and

**W e^{W} \= (−az)·e^{−az} \= (−az)/e^{az} \= (−az)/z \= −a \= −is .**

Hence W \= W₀(−is) on the principal branch, giving z\\\*\_s \= −W/a \= −W₀(−is)/(is). The multiplier is f\_s′(z) \= a·e^{az} \= a·z at the fixed point, so |f\_s′(z\\\*\_s)| \= |a·z\\\*\_s| \= |−W₀(−is)| \= |W₀(−is)| \[9\].

Thus the entire stability question of the family reduces to the single special function s ↦ |W₀(−is)|.

**§2. The Dottie Critical Threshold s\_c \= e^{sin ρ}**

**Theorem T2 (Dottie Threshold \+ Analytic Uniqueness). \[PROVEN\]**  
Write W₀(−is) \= u − iv with u, v \> 0 (valid for s ∈ (0, ∞) with v \< π/2 on the relevant range; the path −is lies on the negative imaginary axis and is **disjoint from the principal-branch cut (−∞, −1/e\]** \[9\]). From W e^{W} \= −is,

**u \= v tan v,   |W₀(−is)| \= v sec v,   s \= v sec v · e^{v tan v}.    (2.1)**

Both v sec v and s(v) are strictly increasing on (0, π/2), so v ↦ s is a strictly increasing bijection and |W₀(−is)| \= v sec v is strictly increasing in s. Hence the stability boundary |W₀(−is)| \= 1 has a **unique** solution, at v \= ρ satisfying v sec v \= 1 ⟺ **v \= cos v** (the Dottie number ρ \= 0.7390851332…), giving u\_c \= sin ρ and

**s\_c \= e^{sin ρ} \= 1.9613088464595… ;   f\_s attracting ⟺ s \< s\_c,  repelling ⟺ s \> s\_c.    (2.2)**

\*Proof.\* The parametrisation is the real/imaginary decomposition of W e^{W} \= −is (Appendix A.1). Monotonicity gives the bijection and the unique crossing; v sec v \= 1 ⟺ v \= cos v ⟺ v \= ρ. Machine-checked: |W₀(−i s\_c)| \= 1 to 30 digits; v(s) strictly increasing and \< π/2 across the tested range.

**§3. The General Lambert Mean Identity**

**Theorem T3 (General Lambert Mean Identity, LM). \[PROVEN\]**  
For every X \> 0, with W\_X := W₀(−2πiX),

**(1/X) ∫₀^X log|W₀(−2πix)| dx \= log|W\_X| − Re W\_X/|W\_X|² .    (3.1)**

\*Proof.\* Put t \= 2πx, T \= 2πX. Since |W₀(−it)| e^{Re W₀(−it)} \= t, one has log|W₀(−it)| \= log t − Re W₀(−it). Using ∫ W₀(σ)dσ \= σ(W₀(σ) − 1 \+ 1/W₀(σ)) and the endpoint limit σ(W₀ − 1 \+ 1/W₀) → 1 as σ → 0,

∫₀^T log|W₀(−it)| dt \= T log T − T − Re∫₀^T W₀(−it) dt \= T log T − T − T(Re W\_T − 1 \+ Re W\_T/|W\_T|²),

and dividing by T and using log|W\_T| \= log T − Re W\_T gives (3.1). Verified to 10⁻³⁵ at X \= 0.15, 0.25, 0.5, 0.8, 1.0 (Appendix A.2).

**Corollary T3.1 (Band mean). \[PROVEN\]** At X \= x\_c (where |W\_X| \= 1, Re W\_X \= sin ρ):  
**(1/x\_c) ∫₀^{x\_c} log|W₀(−2πix)| dx \= −sin ρ \= −0.67361202918…**

**Corollary T3.2 (Section mean / frozen diagnostic). \[PROVEN identity; VERIFIED sign\]** At X \= 1:  
**Λ\_sec \= ∫₀¹ log|W₀(−2πix)| dx \= log|W₀(−2πi)| − Re W₀(−2πi)/|W₀(−2πi)|² \= \+0.00186237422388… \> 0\.**

Both former "separate theorems" of v1.1 are now the two evaluations of one identity. (Λ\_sec is a \*frozen\* diagnostic — its dynamical meaning is discussed in §5, §11: it is **not** the a.e. orbit exponent.)

**§4. The Expanding-Base Cocycle: Genre, Descent, Real Jacobian**

Write the expanding base on its fundamental domain, T\_m(x) \= {mx}, x ∈ \[0,1), a degree-m piecewise-linear map with m branches, discontinuities at x \= i/m, unique ACIM Lebesgue, and h\_top \= log m \[10\]. The fibred cocycle is

**F\_m(z, x) \= ( e^{2πixz} ,  {mx} ) .    (4.1)**

**NON-CLAIM (ℝ/ℤ descent).** F\_m does not descend to a smooth map of ℂ × (ℝ/ℤ): F\_m(z,0) \= (1,0) ≠ F\_m(z,1) \= (e^{2πiz},0). It is a piecewise-smooth measurable cocycle over an expanding base; no global smooth circle skew product is invoked. Genuine invariant points below lie in the interior of continuity intervals and avoid all discontinuities (§6, §7), where F\_m is real-analytic.

On any smooth piece the complex Jacobian is block-triangular with spectral diagonal {2πix·e^{2πixz}, m}. Since z is complex, the honest real Jacobian is 3×3: with a \= 2πix·e^{2πixz} (= 2πix z\\\* at a frozen fixed point) and b \= 2πiz·e^{2πixz},

**D\_ℝF\_m \= \[ Re a  −Im a  Re b \]**  
         **\[ Im a   Re a  Im b \]  with eigenvalue moduli { |a|, |a|, m } .    (4.2)**  
         **\[  0      0     m  \]**

The complex-fibre modulus appears **twice**; the base contributes m. This is the origin of the correct dimension bookkeeping (§6).

**§5. The Invariant-Graph Separation No-Go (with measure-zero support)**

A graph h is F\_m-invariant iff h(T\_m x) \= f\_x(h(x)). For the frozen family h \= z\\\*(x) \= −W₀(−2πix)/(2πix) (the fixed point of f\_x), the right side is z\\\*(x), so invariance would demand z\\\*(T\_m x) \= z\\\*(x).

**Lemma T4.0 (Injectivity of the frozen family). \[PROVEN\]**  
z\\\*(·) is injective on (0,1). Indeed, suppose z\\\*(x) \= z\\\*(y) \= z. Then e^{2πixz} \= z \= e^{2πiyz}, so e^{2πi(x−y)z} \= 1, i.e. **(x−y)z ∈ ℤ ⊂ ℝ**. The principal fixed point has **Im z\\\*(x) \> 0** for all x ∈ (0,1) (verified; min ≈ 0.0063), so for real x − y the product (x−y)z has imaginary part (x−y)·Im z, which is real only if x − y \= 0\. Hence x \= y.

**Theorem T4 (Invariant-Graph Separation No-Go). \[PROVEN\]**  
The defect Δ\_m(x) := z\\\*(T\_m x) − z\\\*(x) is not identically zero; e.g. |z\\\*(½) − z\\\*(¼)| \= 0.184566561531… Moreover, on each branch I\_j \= (j/m, (j+1)/m) the map Δ\_{m,j}(x) \= z\\\*(mx − j) − z\\\*(x) is real-analytic. It vanishes identically on I\_j only if z\\\*(mx − j) \= z\\\*(x) throughout I\_j, which by **Lemma T4.0 (injectivity)** forces mx − j \= x throughout, i.e. (m−1)x \= j identically — impossible for m ≥ 2 (it holds at the single point x \= j/(m−1) only). Hence Δ\_{m,j} is **not identically zero** on any branch. By the identity theorem its zero set is discrete on each branch; a finite union of m branches gives a **countable**, hence **Lebesgue-null**, exceptional coincidence set. Therefore the frozen family is an F\_m-invariant graph on **no** set of positive measure.

\*Consequence.\* The frozen exponent χ\_fr(x) := log|W₀(−2πix)| (T1 with s \= 2πx) is the Lyapunov rate of the \*autonomous\* map f\_x at its fixed point, **not** the fibre exponent of an F\_m-orbit; and Λ\_sec (T3.2) is only a frozen diagnostic — see §11 for the honest measure-level status.

**§6. The Fixed-Point Census Theorem (saddle / repeller / neutral)**

The base map T\_m has interior fixed points x₀ \= j/(m−1), j \= 1,…,m−2 (from {m x₀} \= x₀). They never coincide with a discontinuity i/m (j/(m−1) \= i/m ⟹ m | i, impossible), so F\_m is real-analytic there and (z\\\*(x₀), x₀) is a genuine fixed point of F\_m.

**Theorem T5–T6 (Fixed-Point Census). \[PROVEN (structural); VERIFIED (values)\]**  
At each interior base-fixed point the real Jacobian (4.2) has eigenvalue moduli

**{ |W₀(−2πix₀)|,  |W₀(−2πix₀)|,  m } .    (6.1)**

Hence every interior base-fixed point is **hyperbolic unless x₀ \= x\_c**, and:

* **x₀ \< x\_c:** |W₀| \< 1 \< m ⇒ **saddle of stable index 2** (dim\_ℝ E^s \= 2, dim\_ℝ E^u \= 1);  
* **x₀ \> x\_c:** |W₀| \> 1 (\< m) ⇒ **three-dimensional repeller, unstable index 3** (dim\_ℝ E^s \= 0, dim\_ℝ E^u \= 3);  
* **x₀ \= x\_c:** neutral (non-hyperbolic fibre boundary).

The number of contracting saddles is

**N\_m \= ⌈x\_c(m−1)⌉ − 1,   R\_m \= (m−2) − N\_m repellers,   with |N\_m/(m−1) − x\_c| \< 1/(m−1),  so N\_m/(m−1) → x\_c .    (6.2)**

The **first** contracting saddle appears at the least m with 1/(m−1) \< x\_c ⟺ m−1 \> n\_c \= 3.2036, i.e. **m \= 5, x₀ \= ¼**.

\*Proof.\* (6.1): the 2×2 conformal block \[\[Re a, −Im a\],\[Im a, Re a\]\] has both eigenvalues of modulus |a| \= |W₀(−2πix₀)| (T1); block-triangularity gives spectrum {a, ā, m}. Index counts follow by comparing each modulus to 1\. Count: N\_m \= \#{j : 1 ≤ j, j/(m−1) \< x\_c} \= \#{integers in \[1, x\_c(m−1))} \= ⌈x\_c(m−1)⌉ − 1 (valid whether or not x\_c(m−1) ∈ ℤ; **no** irrationality of x\_c is assumed). Machine-verified for m \= 2,…,15: census counts equal (6.2), real 3×3 moduli equal (6.1) to 18 digits, and the saddle⟺(x₀ \< x\_c) dichotomy holds in every sampled case (Appendix B, T5–T6).

\*Correction of record.\* v1.1 stated dim\_ℝ E^s \= 2, dim\_ℝ E^u \= 1 uniformly and count ⌊x\_c(m−1)⌋; both are here corrected — the stable dimension is 2 **only** below x\_c (it is 0 above), and the robust count is ⌈·⌉ − 1\.

**§7. Certified Periodic Exponential Words (Krawczyk)**

**Arithmetic word dynamics.** Let x₀ \= k/n with gcd(k,n) \= gcd(m,n) \= 1 (equivalently define the period as q \= min{r ≥ 1 : m^r k ≡ k (mod n)}). The base cycle x \= (x₀,…,x\_{q−1}), x\_{j+1} \= {m x\_j}, avoids all discontinuities (a/n \= i/m ⟹ n | a, impossible), and defines the **exponential word map** and its **monodromy multiplier**

**G\_x \= f\_{x\_{q−1}} ∘ ⋯ ∘ f\_{x\_0},   M\_x \= G\_x′(z₀) \= ∏\_{j=0}^{q−1} 2πi x\_j z\_{j+1}  (z\_{j+1} \= f\_{x\_j}(z\_j)),    (7.1)**

with genuine periodic-orbit exponent λ\_V \= (1/q) log|M\_x|.

**Theorem T7 (Certified Coexistence). \[PROVEN — computer-assisted, Krawczyk\]**  
Applying the Krawczyk operator K(𝕏) \= ẑ − Y·F(ẑ) \+ (1 − Y·F′(𝕏))(𝕏 − ẑ) to F \= G\_x − id on an explicit complex-interval box 𝕏 \= ẑ \+ \[−r, r\]² (rigorous mpmath.iv arithmetic, r \= 10⁻³):

* **word (1/7; m \= 2), q \= 3:** K(𝕏) ⊂ int(𝕏) ⇒ a **locally unique** fibre periodic point in 𝕏 (unique within the certified box), with |G\_x′| ∈ **\[0.198, 0.208\] \< 1** ⇒ genuinely **attracting**;  
* **word (1/3; m \= 2), q \= 2:** K(𝕏) ⊂ int(𝕏) ⇒ a **locally unique** fibre periodic point in 𝕏 (unique within the certified box), with |G\_x′| ∈ **\[1.609, 1.643\] \> 1** ⇒ genuinely **repelling**.

*(The certification establishes existence and uniqueness of the fibre-cycle root **inside the explicit box 𝕏**; it does not assert that the same word map has no other fibre cycle in some other region of ℂ.)*

Hence genuine attracting and genuine repelling fibre cycles **coexist** — a fully certified statement, not a numerical one.

\*Method.\* Approximate roots from Newton; the return map and its derivative are propagated as complex intervals through the composition (7.1); K(𝕏) ⊂ int(𝕏) yields existence and uniqueness of a root of F in 𝕏 (interval Newton / Krawczyk), and the interval enclosure of |G\_x′| over 𝕏 classifies the multiplier. Both certifications are reproduced by zs\_m51\_verify\_v1\_3.py (checks T7).

**Open programme (arithmetic word dynamics).** Let A\_m \= {k/n : G\_x has an attracting fibre cycle}. The density of A\_m, its distribution across denominators n, the relation between ord\_n(m) and λ\_V, and a large-deviation law for M\_x are natural open problems this construction poses; they belong to a genuine dynamical-systems programme (candidate ZS-M52), not to M51.

**PART II — POLYGON SPECIALIZATION (s \= 2π/n)**

**§8. The Frozen Polygon Table, n\_c, and the Rapidity Bridge**

Setting s \= 2π/n (x \= 1/n) in Part I: the multiplier is |f′(z\\\*(1/n))| \= |W₀(−2πi/n)| (T1), reproducing ZS-M1 §7's polygon-stability column, and the frozen sign theorem χ\_fr(1/n) \< 0 ⟺ n ≥ 4 follows from T2:

| n | \\ | W₀(−2πi/n)\\ |  | χ\_fr | frozen sign |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 3 | **1.033042** | \+0.032508 | unstable (unique) |  |  |
| 4 | 0.891514 | −0.114835 | stable (first) |  |  |
| 5 | 0.787789 | −0.238525 | stable |  |  |
| 6 | 0.707242 | −0.346383 | stable |  |  |
| 8 | 0.588454 | −0.530257 | stable |  |  |
| 12 | 0.440264 | −0.820380 | stable |  |  |

The Dottie threshold gives the polygon critical index as a corollary of s\_c:

**n\_c \= 2π/s\_c \= 2π e^{−sin ρ} \= 3.20356751489… ,   the triangle/square boundary,    (8.1)**

matching ZS-M1's n\_c \= 3.2036 exactly. The frozen exponent equals ZS-M1's Lyapunov–Lambert rapidity (DERIVED):

**χ\_fr(x) \= log(2πx) − α(x),   α(x) \= Re W₀(−2πix) \= −log|z\\\*(x)| ,    (8.2)**

so at n \= 4: α(¼) \= Re W₀(−iπ/2) \= α\_BK \= 0.5664, log(π/2) \= 0.4516, χ\_fr \= −0.1148. The Fixed-Point Census (§6) specialises to a stability table across (m, n): the first contracting saddle of F\_m is the square (x₀ \= ¼) at m \= 5\.

**PART III — Z-SPIN CORPUS INTERFACE**

**§9. Dependency, the Two-Clock Cocycle, and the F47 Handoff**

M51 consumes only three corpus objects, read-only: z\\\*(x) and n\_c from ZS-M1 \[1\], and the two-clock cocycle from ZS-M50.TC \[2\]. The impedance A \= 35/437, the register Q \= 11, and dim Z \= 2 are **not consumed by any M51 proof**.

**Two-Clock Cocycle. \[IMPORTED-PROVEN from ZS-M50.TC\]** τ(k, m) \= (k, log m) on ℤ × ℕˣ is a cocycle; the horizontal leg's rate family is χ\_H(m) \= log m \= h\_top(T\_m), and {log p} is ℚ-independent by unique factorisation (clear denominators, exponentiate, apply UFD \[16\]). This is exactly the "horizontal" side of Part I: the base expansion rate.

**Cross-consistency.** n\_c (M51 Dottie corollary, 8.1) \= n\_c (ZS-M1 §7) to 12 figures — a cross-check, LOCKED, not a fit. No M1/M50 result feeding downstream ZS-S/ZS-U chains is altered. **F47 handoff:** the physical crossed X/Y complementarity and the A8 wave-contraction conflict (gate F-M51.1) are **not** in M51; they are deferred to ZS-F47.

**§10. Relation to External Literature (adjacent, not identical)**

The object of Part I sits next to three established directions; we position, not appropriate, them.

\*Invariant graphs of skew products over expanding/Markov bases\* study h(Tx) \= g\_x(h(x)) and ask about graph existence, regularity, and dimension. Walkden and Withers \[12\] treat exactly the regime where the **fibre Lyapunov exponent is zero on a set of periodic orbits**, proving that the invariant graph is then either a \*quasi-graph\* ("bony graph") or as smooth as the dynamics — the closest existing analogue to gate H-INV. Their fibre maps are, however, **real homeomorphisms** g\_x : ℝ → ℝ; M51's fibre is a **complex entire, non-invertible exponential** map, so the H-INV problem sits outside their setting. We are not aware of a treatment of this exact object in the literature, but we have **not** performed an exhaustive novelty search, and record H-INV as open pending one.

\*Ergodic theory of exponential entire maps\*, including random/non-autonomous forcing, studies conformal/invariant measures and Lyapunov structure. Urbański and Zdunik \[13\] iterate λe^z on the quotient cylinder ℂ/(2πiℤ) under **random** driving; M51 replaces random forcing by the **deterministic arithmetic forcing** x ↦ {mx} on the \*same\* cylinder geometry. M51 is thus an arithmetic-deterministic neighbour of that theory — adjacent literature, not the same theorem class.

\*Computer-assisted complex dynamics\* certifies fixed points and multipliers via interval Newton / Krawczyk / radii-polynomial methods; Theorem T7 is exactly such a certification and is stated at that standard.

**§11. Gate Registry (what is closed, what remains open)**

| Gate | Statement | Status |
| ----- | ----- | ----- |
| **T1–T3, T5–T6** | Multiplier, Dottie threshold, Lambert Mean Identity, census structure | **PROVEN** (values VERIFIED) |
| **T7** | Coexistence of a certified attracting and a certified repelling fibre cycle | **PROVEN** (Krawczyk) |
| **H-UFC** | Global **uniform** contraction of the 2-real-dim fibre | **CLOSED-NEGATIVE** (T7 repelling cycle) |
| **H-2s1u** | Global hyperbolic splitting with dim E^s \= 2, dim E^u \= 1 | **CLOSED-NEGATIVE** (T7) |
| **H-PH** | \*Some\* partially hyperbolic **compact invariant set** with a fibre **centre** bundle E^s ⊕ E^c ⊕ E^u | **OPEN / NON-CLAIM** (not ruled out by T7) |
| **H-ORBIT** | Genuine a.e. fibre Lyapunov exponent (6.3-type) over the base ACIM | **OPEN** (needs an invariant graph / natural extension; Λ\_sec is only a frozen diagnostic) |
| **H-INV** | Nontrivial F\_m-invariant graphs on sub-bands | **OPEN** (No-Go §5 excludes only the frozen family) |
| **F-M51.1** | A8 wave-contraction vs horizontal wave-expansion | Deferred to ZS-F47 |

**Honest scope statement.** The coexistence of contracting and expanding fibre periodic data rules out a global uniformly contracting fibre and a global {2s, 1u} hyperbolic splitting; it does **not** by itself rule out every possible centre-type partially hyperbolic structure. Moreover the phase space ℂ × \[0,1) is non-compact and piecewise-smooth, so a "global partial hyperbolicity" statement would first require specifying a compact invariant set and a splitting; we therefore make **no** such claim (correcting v1.1's over-broad "global partial hyperbolicity is false").

**§12. Anti-Numerology**

| m | χ\_H \= log m | m·\\ | W₀(−iπ/2)\\ |  | χ\_H \+ χ\_fr(¼) |
| ----- | ----- | ----- | ----- | ----- | ----- |
| 2 | 0.693147 | 1.783027 | \+0.578313 |  |  |
| 3 | 1.098612 | 2.674541 | \+0.983778 |  |  |
| 5 | 1.609438 | 4.457568 | \+1.494603 |  |  |

m·|f′| ≠ 1 and χ\_H \+ χ\_fr ≠ 0 (no reciprocal/conservation law). Λ\_sec \= \+0.00186237… is not forced to 0 and is not asserted equal to any structural constant. Any χ\_H \= −χ\_fr or m|f′| \= 1 is **RETRACTED-as-numerology**. The threshold s\_c (hence n\_c) is derived independently in Part I and matches ZS-M1 — a cross-check, not a fit.

**§13. Non-Claims**

* **NON-CLAIM (physics):** none; crossed X/Y table and H-INT deferred to ZS-F47.  
* **NON-CLAIM (ℝ/ℤ smoothness):** F\_m is a piecewise cocycle over T\_m \= {mx}.  
* **NON-CLAIM (frozen \= genuine):** χ\_fr and Λ\_sec are frozen; not orbit/measure-level exponents.  
* **NON-CLAIM (uniform stable dimension):** dim\_ℝ E^s is 2 only below x\_c, 0 above (§6).  
* **NON-CLAIM (global partial hyperbolicity):** not asserted; only H-UFC and H-2s1u are closed-negative (§11).  
* **NON-CLAIM (all periodic rows proven):** only the two Krawczyk-certified words are PROVEN; the exploration table (Appendix C) is VERIFIED-numerical.  
* **NON-CLAIM (arithmetic nature of x\_c/s\_c):** no irrationality/transcendence of x\_c is used or claimed.  
* **NON-CLAIM (i-tetration → operator):** classical pre-quantum map only.

**§14. Conclusion**

The natural object is the one-parameter exponential family f\_s(z) \= e^{isz}: its multiplier is |W₀(−is)| (T1), its stability threshold is the **Dottie value s\_c \= e^{sin ρ}** proved unique analytically (T2), and all its Lambert averages follow from one **General Lambert Mean Identity** (T3), whose two evaluations are the band mean −sin ρ and the frozen section mean Λ\_sec. Over the expanding base T\_m the frozen family is not an invariant graph, with a measure-zero exceptional set (T4); the genuine invariant sets obey an exact **Fixed-Point Census** — saddles of stable index 2 below x\_c, three-dimensional repellers above, count ⌈x\_c(m−1)⌉−1, first at m \= 5 (T5–T6); and a **Krawczyk certification** proves the coexistence of a genuine attracting and a genuine repelling fibre cycle (T7), which closes H-UFC and H-2s1u negatively while leaving centre-type H-PH, the a.e. exponent H-ORBIT, and sub-band invariant graphs H-INV honestly open. Polygon tetration is the arithmetic specialization s \= 2π/n, recovering ZS-M1's n\_c \= 3.2036 as a corollary (Part II). The genuine measure-level theory — invariant graphs and natural extensions for a non-invertible complex-exponential fibre over an expanding arithmetic base — is the natural sequel (candidate ZS-M52). Verification: **93/93 PASS**, including two Krawczyk-certified cycles (four interval assertions).

**Acknowledgements & Code Availability**

Developed with AI assistance for symbolic checking, high-precision and **rigorous interval** verification (Python / mpmath and mpmath.iv), and drafting; the author is responsible for all content. The fail-closed suite zs\_m51\_verify\_v1\_3.py reproduces every affirmative statement — the general multiplier (T1), the Dottie threshold and uniqueness witness (T2), the Lambert Mean Identity and its two corollaries (T3), the invariant-graph separation and branch non-vanishing (T4), the full census counts and real-3×3 classification (T5–T6), the **two Krawczyk certifications** (T7), the polygon table and rapidity bridge (Part II), and the two-clock/anti-numerology checks (Part III) — asserting **93/93 PASS** or aborting, and printing the CLOSED-NEGATIVE / OPEN gate registry it does not (and cannot) resolve numerically.

**Appendix A — Key Derivations**

**A.1 Dottie parametrisation.** For W \= u − iv (u, v \> 0), W e^{W} \= (u − iv)e^{u}(cos v − i sin v). Equating to −is (pure imaginary) forces the real part to vanish: u cos v \= v sin v ⇒ u \= v tan v; the imaginary part gives s \= e^{u}(u sin v \+ v cos v) \= e^{v tan v}·v sec v; and |W| \= √(u² \+ v²) \= v sec v. Monotonicity of v sec v and v sec v·e^{v tan v} on (0, π/2) is immediate; |W| \= 1 ⟺ v sec v \= 1 ⟺ v \= cos v \= ρ, whence u\_c \= sin ρ and s\_c \= e^{sin ρ}.

**A.2 Lambert Mean Identity.** With ∫ W₀(σ)dσ \= σ(W₀ − 1 \+ 1/W₀) and the σ → 0 limit \+1 (since σ/W₀ → 1), the computation in §3 gives (3.1). The only subtle endpoint is σ \= 0, handled by that limit.

**A.3 Real Jacobian block.** The complex multiplier a acts on the real fibre plane as \[\[Re a, −Im a\],\[Im a, Re a\]\], characteristic polynomial λ² − 2(Re a)λ \+ |a|², roots a, ā of common modulus |a| — the source of the double modulus in (6.1) and dim\_ℝ E^s \= 2 when |a| \< 1 (0 when |a| \> 1).

**A.4 Krawczyk certification (T7).** For F \= G\_x − id with approximate root ẑ, Y ≈ F′(ẑ)⁻¹, and box 𝕏 \= ẑ \+ \[−r,r\]², if the Krawczyk image K(𝕏) \= ẑ − Y F(ẑ) \+ (1 − Y F′(𝕏))(𝕏 − ẑ) satisfies K(𝕏) ⊂ int(𝕏), then F has a unique zero in 𝕏 (standard interval-Newton theory). The interval enclosure of |G\_x′| over 𝕏 then bounds the multiplier away from 1\. Both words are certified with r \= 10⁻³ at 34-digit interval precision.

**Appendix B — Verification Ledger (93/93 PASS)**

| Block | Tests | Scope |
| ----- | ----- | ----- |
| T1 | 4 | General multiplier \\ |
| T2 | 6 | Dottie threshold; \\ |
| T3 | 7 | Lambert Mean Identity (5 X-values) \+ band & section corollaries |
| T4 | 3 | Injectivity (Im z\*\>0); invariant-graph separation; branch non-vanishing |
| T5 | 29 | Census counts N\_m, R\_m for m=2..15; first at m=5 |
| T6 | 14 | Real 3×3 moduli {\\ |
| **T7** | **4** | **Krawczyk: locally-unique attracting (1/7;2) & repelling (1/3;2), certified in box** |
| P (polygon) | 17 | Frozen table vs ZS-M1; n\_c; rapidity bridge |
| C \+ AN | 9 | Two-clock; {log p} scan; anti-numerology inequalities |
| **Total** | **93** | **100% PASS, fail-closed** |

Registered but not machine-tested (genuinely open/closed-negative by argument): H-UFC, H-2s1u (CLOSED-NEGATIVE via T7); H-PH, H-ORBIT, H-INV (OPEN).

**Appendix C — Exploration Table (VERIFIED-numerical, not certified)**

Numerically located fibre-cycle multipliers |M\_x| (Newton, 40 digits; **not** interval-certified — for exploration only). Only the T7 rows (1/7;2 and 1/3;2) are PROVEN.

| word (k/n; m) | q | \\ | M\_x\\ | of a located cycle | λ\_V | located behaviour |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1/7; 2 | 3 | 0.20295 | −0.531605 | attracting **(certified, T7)** |  |  |
| 1/13; 2 | 12 | 0.04528 | −0.257899 | attracting (numerical) |  |  |
| 1/8; 3 | 2 | 0.80826 | −0.106438 | attracting (numerical) |  |  |
| 1/11; 3 | 5 | 0.04132 | −0.637289 | attracting (numerical) |  |  |
| 1/3; 2 | 2 | 1.62557 | \+0.242929 | repelling **(certified, T7)** |  |  |
| 1/9; 2 | 6 | 1.31144 | \+0.045188 | repelling (numerical) |  |  |
| 1/4; 3 | 2 | 1.72827 | \+0.273561 | repelling (numerical) |  |  |

**References**

\[1\] K. Kang, \*ZS-M1 v1.0: The i-Tetration Fixed Point and Polygon-Tetration Family\* (Z-Spin Cosmology Collaboration, March 2026).  
\[2\] K. Kang, \*ZS-M50 v1.3: Two Directions of Polygon Tetration — Base–Dilation, ℚ/ℤ Saturation, Frobenius Grading, the Log-Time Cocycle, the Bost–Connes Representation, and the Two-Clock Cocycle\* (Z-Spin Cosmology Collaboration, July 2026).  
\[3\] K. Kang, \*ZS-M46 v1.5: Koenigs Linearization and Half-Sided Modular Inclusions\* (Z-Spin Cosmology Collaboration, July 2026).  
\[4\] K. Kang, \*ZS-M49: The Prime-Log Length Spectrum and POME\* (Z-Spin Cosmology Collaboration, July 2026).  
\[5\] K. Kang, \*ZS-F2 v1.0 / ZS-F5 v1.0\* (Z-Spin Cosmology Collaboration, March 2026). \[Context only; A, Q, dim Z not consumed by any M51 proof.\]  
\[6\] K. Kang, \*ZS-A8: The Contracting-Sector Construction\* (Z-Spin Cosmology Collaboration, 2026). \[Conflict gate F-M51.1, deferred to F47.\]

\[7\] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, "On the Lambert W function," \*Adv. Comput. Math.\* **5**, 329–359 (1996).  
\[8\] P. Walters, \*An Introduction to Ergodic Theory\*, GTM **79** (Springer, 1982).  
\[9\] R. E. Moore, R. B. Kearfott, and M. J. Cloud, \*Introduction to Interval Analysis\* (SIAM, 2009). \[Krawczyk operator / interval Newton, T7.\]  
\[10\] A. Katok and B. Hasselblatt, \*Introduction to the Modern Theory of Dynamical Systems\* (Cambridge University Press, 1995).  
\[11\] The Dottie number ρ \= cos ρ ≈ 0.739085 (unique real fixed point of cosine); see E. W. Weisstein, "Dottie Number," \*MathWorld — A Wolfram Web Resource\*.  
\[12\] C. P. Walkden and T. Withers, "Invariant graphs of a family of non-uniformly expanding skew products over Markov maps," \*Nonlinearity\* **31**(6), 2726–2755 (2018); DOI 10.1088/1361-6544/aab596; arXiv:1701.06320.  
\[13\] M. Urbański and A. Zdunik, "Random non-hyperbolic exponential maps," arXiv:1805.08050 (2018).  
\[14\] G. H. Hardy and E. M. Wright, \*An Introduction to the Theory of Numbers\*, 6th ed. (Oxford University Press, 2008).  
\[15\] K. Kang (ed.), \*The Book of Z-Spin Cosmology — Light Edition (OS for AI), v11.0\* (Z-Spin Cosmology Collaboration, July 2026).

**Version History**

**v1.3 (July 2026\) — final.** Closing polish integrating the v1.2 external review; **no new mathematics**, four corrections plus two editorial edits. **(i)** T1 proof corrected: the Lambert substitution is W \= −az \= −isz (the sign was garbled in v1.2), giving W e^{W} \= −is cleanly. **(ii)** T4 augmented with **Lemma T4.0 (injectivity of z\\\*(·) on (0,1))** via Im z\\\*(x) \> 0, which supplies the previously-asserted per-branch non-vanishing and completes the measure-zero argument. **(iii)** T7 uniqueness re-scoped as **local uniqueness within the explicitly certified box** (in Abstract and statement), not global. **(iv)** External references \[12\] (Walkden–Withers, \*Nonlinearity\* **31**(6), 2726–2755, 2018\) and \[13\] (Urbański–Zdunik, arXiv:1805.08050, 2018\) given in full, with the §10 novelty claim qualified (no exhaustive novelty search performed) and the Walkden–Withers zero-fibre-exponent/quasi-graph result stated as the closest analogue to H-INV. Cover phrasing corrected to "two Krawczyk-certified cycles (four interval assertions)." This is the intended terminal M51 version; H-INV, H-ORBIT, and the arithmetic-word-distribution programme are handed to ZS-M52.

**v1.2 (July 2026):** Rigor/positioning revision integrating the v1.1 external review (superseded by v1.3). **Restructured** external-first (Part I standalone f\_s(z)=e^{isz} math; Part II polygon; Part III corpus). **Adds** the General Multiplier Theorem and the Dottie threshold s\_c \= e^{sin ρ} for the general family (T1–T2); the **General Lambert Mean Identity** unifying the two averages (T3); the measure-zero support for the Invariant-Graph Separation No-Go (T4); the full **Fixed-Point Census** with the corrected count ⌈x\_c(m−1)⌉−1 and the saddle/repeller/neutral classification (T5–T6); and a **Krawczyk interval certification** upgrading the periodic-cycle coexistence to PROVEN (T7). **Corrects** v1.1's uniform stable-dimension claim (now saddle index 2 below x\_c, repeller index 3 above), the floor→ceil count, the period definition (gcd(k,n)=1 / minimal period), the branch-cut statement (−is disjoint from (−∞,−1/e\]), and the over-broad "global partial hyperbolicity is false" (now H-UFC/H-2s1u CLOSED-NEGATIVE vs H-PH OPEN). Verification re-based to 92/92 (4 rigorous certifications). Adjacent external literature (invariant graphs; random exponential dynamics; computer-assisted dynamics) added.

**v1.1 (July 2026):** Honesty revision — piecewise-expanding genre, frozen/genuine split, real-dimension fix, Dottie boundary, band/section averages, invariant-graph separation, genuine fixed-point/periodic results; retracted v1.0's skew-product partial hyperbolicity. (Superseded by v1.2.)

**v1.0 (July 2026):** Initial release; over-promoted frozen calculation to skew-product partial hyperbolicity. (Superseded.)  
