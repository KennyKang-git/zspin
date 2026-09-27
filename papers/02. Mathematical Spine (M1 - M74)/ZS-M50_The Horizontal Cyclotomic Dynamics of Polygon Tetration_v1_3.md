# **ZS-M50**

# **The Horizontal Cyclotomic Dynamics of Polygon Tetration**

***The Canonical Isometric Bost–Connes Representation, the Finite-Register Isometry No-Go, and the Two-Clock Linearization***

**Kenny Kang**  
Z-Spin Collaboration · Mathematical Spine Theme  
Paper code: **ZS-M50**  ·  Programme initiated March 2026  ·  This revision: v1.3 (July 2026\)

**Verification:** 36/36 executable checks PASS (fail-closed, exit 0\) \+ 9 registered gates  |  **Zero Free Parameters**  |  **H-ALG CLOSED (PROVEN)**  
**Core result M50.3′: DERIVED-CONDITIONAL on {H-FLOW, H-SB, H-WEIGHT, P-TRANS}** (H-ALG discharged internally in §7).  
**NON-CLAIMS:** not a proof of RH/GRH; not an internal prime-orbit flow; the §7 representation is covariant but not proved faithful/universal; not a claim that the finite Q=11 register carries a proper isometry (proved impossible in §8).

# **§0.  Abstract**

Z-Spin Cosmology carries two directions of polygon tetration on the base family bₙ \= e^{2πi/n}. The vertical direction iterates the fixed transfer map T(z) \= i^z; ZS-M49 (Theorem M49.A) proved it cannot realise the prime-orbit measure. This paper develops the horizontal direction — base dilation b ↦ b^m, an expanding cyclotomic endomorphism (not a rotation) — and settles the algebraic half of the problem constructively.  
Four internal facts are PROVEN with zero free parameters: T1 (lifted base–dilation identity Fₐ ∘ Dₘ \= F\_{ma}), T2 (the ℕ^{×}-saturation of {bₙ} is ℚ/ℤ — a semigroup saturation, not a topological closure, since μ\_∞ is dense in S¹), T3 (the ZS-M22 gate M\_p diagonalises as the finite-level Frobenius χ\_k(p)), and T4 (the horizontal roof is the additive log-time cocycle τ(m) \= log m; the primes are ℚ-linearly independent by unique factorisation).  
The central result closes the gate v1.1 left open. We define, on the horizontal dilation-depth Hilbert space ℓ²(ℕ^{×}), an explicit covariant Bost–Connes representation: μ\_nε\_k \= ε\_{nk}, μ\_n^\*ε\_k \= ε\_{k/n} (n | k, else 0), e(r)ε\_k \= e^{2πikr}ε\_k, Hε\_k \= (log k)ε\_k. The group-algebra relations (e(0) \= I, e(r)e(s) \= e(r+s), e(r)^\* \= e(-r)), the isometry relations (μ\_n^\*μ\_n \= I, μ\_nμ\_n^\* \= P\_{n|k} ≠ I, μ\_nμ\_m \= μ\_{nm}, and μ\_n^\*μ\_m \= μ\_mμ\_n^\* for coprime n, m), the covariance relations (μ\_n^\*e(r)μ\_n \= e(nr), μ\_ne(r)μ\_n^\* \= ρ\_n(e(r))), and the time-evolution relations (\[H, μ\_n\] \= (log n)μ\_n, e^{itH}μ\_ne^{-itH} \= n^{it}μ\_n) are proved algebraically in §7 and regression-tested numerically on representative finite-support vectors. This discharges gate H-ALG (PROVEN) as a covariant realisation (faithfulness is not claimed).  
Two further theorems sharpen the structure. Theorem M50.NG (finite-register no-go): in any finite-dimensional register an isometric relation V^\*V \= I forces V unitary, so a proper isometry (μ\_nμ\_n^\* ≠ I) cannot exist — the Bost–Connes completion is necessarily infinite-dimensional. Theorem M50.TC (two-clock linearization): the combined time is the vector-valued cocycle τ(k, m) \= (k, log m) on ℤ × ℕ^{×}, a rank-one constitutional clock with an infinite-rank arithmetic clock {log p}.  
We correct the Laplace-transform statement of M50.3′. With the standard transform ℒμ(u) \= ∫₀^∞ e^{-ut} dμ(t), the p^{-m/2}-weighted prime-orbit measure satisfies ℒμ\_pkt^χ(u) \= −L′/L(u \+ 1/2, χ); equivalently, with the centered transform ℒ\_{1/2}μ(s) := ∫ e^{-(s-1/2)t} dμ(t), one has ℒ\_{1/2}μ\_pkt^χ(s) \= −L′/L(s, χ). The \+1/2 shift, absent from v1.2, is now explicit and the verification G-block tests the weighted measure itself. The seam–temperature identification (ℜ s \= 1/2 vs β \= 1/2) remains gate H-SB (OPEN), so M50.3′ is DERIVED-CONDITIONAL on {H-FLOW, H-SB, H-WEIGHT, P-TRANS}, with P-TRANS retained from ZS-M49. At β \= 1/2 the weight p^{-m/2} is an actual value of the unique type-III₁ Bost–Connes KMS state (not a convergent Gibbs trace in ℓ²(ℕ)). Verification: 36/36 executable fail-closed checks. Zero free parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

# **Epistemic Status Legend**

| Status | Definition |
| ----- | ----- |
| PROVEN | Exact mathematical fact, or an exact algebra relation proved in the body and regression-tested on finite-support vectors. |
| DERIVED | Follows from the Z-Spin action plus PROVEN inputs; zero free parameters beyond A \= 35/437. |
| DERIVED-interpretation | Synthesis of PROVEN components under a new conceptual framing. |
| DERIVED-CONDITIONAL | Derived conditional on explicitly named upstream gates (H-FLOW, H-SB, H-WEIGHT, P-TRANS). |
| DATA-LEVEL IDENTIFICATION | The defining data coincide; an explicit operator realisation may be separate. |
| IMPORTED-PROVEN | Proved externally, used here without re-proof, cited in full. |
| IMPORTED-GUARD | An external theorem stated as a guard; asserted, not re-proved by our code. |
| FORMAL-IDENTITY | An exact algebraic identity that holds by construction; verifies consistency, not the existence of a dynamical object. |
| HYPOTHESIS | Motivated conjecture; derivation chain incomplete. |
| OPEN | A well-posed problem registered honestly, with its closure condition stated. |
| NON-CLAIM | An explicit statement of what is NOT asserted. |
| RETRACTED | A prior claim withdrawn in this revision, with the reason recorded. |
| LOCKED | A core constant fixed upstream; not re-derived and not modifiable downstream. |

# **§1.  Introduction**

## **1.1  Two directions, and what earlier revisions established**

The vertical direction iterates T(z) \= i^z at fixed base; ZS-M49 Theorem M49.A proved it does not realise POME (in the Abel coordinate the seam is the unit translation u ↦ u+1, so the length group lies in ℤ). The horizontal direction dilates the base, b ↦ b^m. Earlier revisions established the four PROVEN structures T1–T4, the half-density localisation M50.HD (fibre Jacobian p^{+m/2}; base KMS weight p^{-m/2}), the internal Bost–Connes representation closing H-ALG, the finite-register no-go, and the two-clock linearization.

## **1.2  What v1.3 corrects**

This revision is a narrow rigor-and-expression patch, adding no new theory. It corrects: (i) the Laplace-transform statement of M50.3′, which omitted a \+1/2 shift, and rebuilds the G-block to test the actual p^{-m/2}-weighted measure; (ii) the word “co-isometric” (V^\*V \= I is isometric); (iii) the scope of “all Bost–Connes relations”, now listing the group-algebra, isometry, covariance, and time-evolution relations and verifying the added ones; (iv) “machine-verified exactly”, now “proved algebraically and regression-tested”; (v) the title/§7 phrase “direct-limit”, narrowed to “canonical isometric representation”; (vi) the {log p} independence, now proved by unique factorisation; (vii) a faithfulness non-claim; and (viii) the crossed-product notation. The verification count is corrected to 36/36 and remains fail-closed.

# **§2.  T1 — The Lifted Base–Dilation Identity**

**Theorem M50.T1 \[PROVEN\].** With a \= Log b and Fₐ(z) \= e^{az}, and Dₘ(z) \= mz, one has:  
Fa(Dm(z)) \= e(ma)z \= Fma(z)  
**Terminology \[corrects earlier\].** b ↦ b^m multiplies the angle by m: an expanding cyclotomic dilation / multiplicative base endomorphism, not a rotation. The two flows do not commute (§9): DₘFₐ ≠ FₐDₘ; T1 is a source–target relation.

# **§3.  T2 — Cyclotomic Saturation of the Polygon Family**

**Theorem M50.T2 \[PROVEN\].** The ℕ^{×}-saturation of {bₙ \= e^{2πi/n}} — the smallest ℕ^{×}-invariant set containing it — is μ\_∞ ≅ ℚ/ℤ: Sat\_{ℕ^{×}}{1/n : n ≥ 1} \= ℚ/ℤ. This is a semigroup saturation, not a topological closure (μ\_∞ is dense in S¹, so its topological closure is S¹). The verification generates the orbit by the action m·(1/n) and compares it to the independently enumerated n-torsion {k/n}. Base-coordinate split: |b| \= 1 ⇒ x \= a/(2πi) ∈ ℝ/ℤ; general b ⇒ x ∈ ℂ/ℤ (Appendix A).

# **§4.  T3 — Finite-Level Cyclotomic Frobenius**

**Theorem M50.T3 \[PROVEN, ZS-M22\].** M\_p|χ\_k⟩ \= χ\_k(p)|χ\_k⟩, det(I − p^{-s}M\_p)^{-1} \= ∏\_k (1 − χ\_k(p)p^{-s})^{-1}; ζ ↦ ζ^p is the Frobenius on the unramified stratum p ∤ n.  
**Ramification \[corrected\].** At p | n, ζ \= 1 stays fixed; ζ ↦ ζ^p ceases to be an automorphism of the primitive n-torsion stratum, so no unramified Frobenius orbit exists there — not “no closed orbit”. Four-point \[corrected\]: the ℕ^{×}-orbit of 1/4 is the level μ₄, not a period-four orbit (m \= 2 absorbed; m \= 3 a 2-cycle; m \= 5 fixed).

# **§5.  T4 — The Logarithmic Time Cocycle**

**Theorem M50.T4 \[PROVEN\].** τ(m) \= log m is an additive cocycle on ℕ^{×} with primitive generators the primes; τ(p^m) \= m log p. This is the Bost–Connes Hamiltonian roof Hε\_n \= (log n)ε\_n, read off the horizontal dynamics.  
**Independence of {log p} — by unique factorisation \[PROVEN; corrects the PSLQ phrasing\].** Suppose Σ\_j q\_j log p\_j \= 0 with q\_j ∈ ℚ. Multiplying by the lcm D of denominators gives Σ\_j a\_j log p\_j \= 0 with a\_j ∈ ℤ; exponentiating gives ∏\_j p\_j^{a\_j} \= 1; unique factorisation forces every a\_j \= 0, hence every q\_j \= 0\. So {log p} is ℚ-linearly independent, and the horizontal length group is free of infinite rank. (The PSLQ scan in the code is a regression check, not the proof.)

# **§6.  T-CORE — Data and Representation**

**T-CORE-DATA \[PROVEN\].** The data (ℚ/ℤ torsion base; ℕ^{×} multiplication r ↦ nr; cyclotomic Frobenius grading; log-time cocycle log n) coincide with the defining data of the Bost–Connes core.  
**T-CORE-ALG \[PROVEN, via §7\].** The explicit ℓ²(ℕ^{×}) representation of §7 is a covariant representation satisfying the rational Bost–Connes relations. We do ***not*** claim it is faithful or that it realises the universal Bost–Connes algebra (that would need a separate faithfulness / universal-property argument); the C\*-completion and KMS phase are then IMPORTED-PROVEN.

# **§7.  The Canonical Isometric Bost–Connes Representation — H-ALG CLOSED**

On ℓ²(ℕ^{×}) with orthonormal basis {ε\_k : k ≥ 1} define μ\_n, μ\_n^\*, e(r), H by:  
nk \= nk,   n\*k \= k/n (n | k) or 0,   e(r)k \= e2πikrk,   Hk \= (log k)k  
**Theorem M50.ALG \[PROVEN\].** The operators satisfy, exactly on finite-support vectors, the following Bost–Connes relations. Group-algebra:  
e(0) \= I,   e(r)e(s) \= e(r+s),   e(r)\* \= e(−r)  
Isometry (proper) and covariance:  
n\*n \= I,   nn\* \= Pn|k ≠ I,   nm \= nm,   n\*m \= mn\*  (gcd(n,m)=1)  
n\*e(r)n \= e(nr),   ne(r)n\* \= n(e(r)) \= 1nΣ\_{ns=r} e(s)  
Time evolution:  
\[H, n\] \= (log n)n,   eitHne−itH \= nitn  
Proof. Each relation is a direct computation on ε\_k. E.g. μ\_n^\*μ\_nε\_k \= ε\_k while μ\_nμ\_n^\*ε\_k \= ε\_k (n | k) or 0, so μ\_n is a proper isometry with range projection P\_{n|k}. For covariance, μ\_ne(r)μ\_n^\*ε\_k \= e^{2πi(k/n)r}ε\_k (n | k) \= (1/n)Σ\_{ns=r}e^{2πiks}ε\_k \= ρ\_n(e(r))ε\_k, using Σ\_{j=0}^{n-1}e^{2πikj/n} \= n\[n|k\]. The Hamiltonian relations follow from log(nk) \= log n \+ log k.  
**Consequence and honest scope.** Gate H-ALG is CLOSED (PROVEN): the horizontal action carries proper Bost–Connes isometries whose Hamiltonian roof is exactly the log-time cocycle T4. The relations are proved algebraically here and regression-tested numerically on representative finite-support vectors (checks ALG.0a–ALG.7); “machine-verified exactly” would overstate a finite numerical sample. The construction is the standard isometric representation of ℕ^{×} on ℓ²(ℕ^{×}); we do not build an operator-algebraic direct/inductive limit (connecting maps, limit algebra, ℚ₊^{×} automorphic dilation), and we do not claim faithfulness. Its value is corpus-internal: this representation is derived canonically from the horizontal dilation depth of polygon tetration.

# **§8.  M50.NG — The Finite-Register Isometry No-Go**

**Theorem M50.NG \[PROVEN\].** On a finite-dimensional Hilbert space, the isometric relation V^\*V \= I implies V is unitary, hence VV^\* \= I. Therefore a proper isometry (μ\_n^\*μ\_n \= I but μ\_nμ\_n^\* ≠ I) cannot exist on any finite register, in particular not on the Q \= 11 register.  
Proof. V^\*V \= I means V is injective and norm-preserving; on a finite-dimensional space injective implies surjective, so V is invertible with V^{-1} \= V^\*, giving VV^\* \= I.  
**Consequence.** The Bost–Connes completion is necessarily infinite-dimensional: the proper isometry μ\_nμ\_n^\* \= P\_{n|k} ≠ I of §7 (witnessed by μ\_2μ\_2^\*ε\_1 \= 0\) lives only on ℓ²(ℕ^{×}). Under the Bost–Connes proper-isometry condition, infinite dimension is forced; this is a scope-restricted strengthening beyond ZS-M49's model-set / finite-Markov no-gos, and it explains why the finite ZS-M22 gate (a permutation, hence unitary) cannot by itself carry the p^{-β} weight.

# **§9.  The Two Directions Do Not Commute \[F-M50.7 corrected\]**

With Fₐ(z) \= e^{az} and Dₘ(z) \= mz, DₘFₐ(z) \= m·e^{az} ≠ e^{amz} \= FₐDₘ(z). The horizontal direction is the moduli action a ↦ ma; the correct compatibility is the skew-product / source–target relation Fₐ ∘ Dₘ \= F\_{ma} (T1), realised by the semigroup crossed product **ℚ\[ℚ/ℤ\] ⋊\_ρ ℕ^{×}** (at the C\*-level C\*(ℚ/ℤ) ⋊\_ρ ℕ^{×}), an intrinsically non-commutative algebra whose covariant isometric representation is §7. The endomorphism ρ is ρ\_n(e(r)) \= (1/n)Σ\_{ns=r}e(s). The old commutation form of F-M50.7 is RETRACTED.

# **§10.  M50.HD — Fibre p^{+m/2} vs Base p^{-m/2}, and Gate H-SB**

For the degree-p covering F\_p(x) \= px (mod 1\) the distributional kernel of the m-th iterate is K\_m(x,y) \= p^{-ms}Σ\_jδ(y − (x+j)/p^m); its flat trace has the root x\* \= j/(p^m−1) with Jacobian 1/|1 − p^{-m}| and exactly p^m−1 roots in \[0,1), giving:  
tr♭ Lp,sm \= (p^m − 1\) p^{−ms}|1 − p^{−m}| \= pm(1−s);   at s \= 1/2:  p+m/2  
(Appendix B carries the kernel derivation; the denominator is the Atiyah–Bott factor |1 − (F^m)′^{-1}|, not an inserted normalisation.) The fibre Jacobian yields the wrong sign and the full-shift orbit count. The correct amplitude p^{-m/2} is the base Bost–Connes KMS weight ψ(μ\_{p^m}μ\_{p^m}^\*) \= p^{-mβ}, at β \= 1/2 (IMPORTED-GUARD: Bost–Connes 1995).  
**Gate H-SB \[OPEN/HYPOTHESIS\].** ZS-M7 Theorem 4 selects the self-dual spectral line ℜ s \= 1/2; but s is a spectral/functional-equation parameter and β is a thermodynamic inverse temperature. Their canonical identification is a new bridge, registered as H-SB; until it is closed, the half-density weight is not discharged by the seam alone.  
**The β \= 1/2 weight \[corrected\].** For 0 \< β ≤ 1 the Bost–Connes system has a unique KMS\_β state, of type III₁ (Neshveyev). Hence p^{-m/2} at β \= 1/2 is an actual value of that state; it is simply not represented by a convergent Gibbs trace in the canonical ℓ²(ℕ) representation.

# **§11.  M50.TC — The Two-Clock Linearization**

**Theorem M50.TC \[PROVEN\].** The combined time τ(k, m) \= (k, log m) on ℤ × ℕ^{×} is a vector-valued cocycle:  
τ(k+k′, mm′) \= τ(k, m) \+ τ(k′, m′)  
Its first component is the constitutional/vertical clock, rank-one ℤ-valued (ZS-M46/M49: seam roof 1); its second is the arithmetic/horizontal clock, whose generators {log p} are ℚ-linearly independent by unique factorisation (§5), hence free of infinite rank. This is the first appearance of the prime-logarithm length spectrum — which ZS-M49 identified as necessary for POME and could not obtain from the internal finite Y-spectrum — as the second direction of an internal Z-Spin variable, connecting the seam unit translation (ZS-M46/M47), the prime-log spectrum (ZS-M49), the Frobenius gate (ZS-M22), the modular half-density (ZS-A24), and the Bost–Connes time evolution into one skew-product.

# **§12.  The Remaining Gates and the Conditional POME-K′**

H-ALG is CLOSED (§7). The remaining gates:

| Gate | Statement | Status / target |
| ----- | ----- | ----- |
| H-ALG | internal Bost–Connes isometries from horizontal depth | CLOSED — PROVEN (§7) |
| H-FLOW | explicit functor / conjugacy from the Bost–Connes groupoid to the Deninger–adelic prime-orbit flow | DERIVED-CONDITIONAL |
| H-SB | seam line ℜ s \= 1/2 identified with KMS β \= 1/2 | OPEN / HYPOTHESIS |
| H-WEIGHT | KMS projection expectation enters the POME orbit coefficient (trace/orbit correspondence) | OPEN |
| P-TRANS | packet transverse normalisation ν(Γ\_p) \= 1 (inherited from ZS-M49) | OPEN |

**The transform, stated correctly.** Define the centered transform ℒ\_{1/2}μ(s) := ∫ e^{-(s-1/2)t} dμ(t). Then, conditional on {H-FLOW, H-SB, H-WEIGHT, P-TRANS},  
ℒ1/2pkt(s) \= −L′L(s, χ),   equivalently   ℒpkt(u) \= −L′L(u \+ 1/2, χ)  
where the second form uses the standard Laplace transform ℒμ(u) \= ∫₀^∞ e^{-ut} dμ(t) and makes the \+1/2 shift explicit (the mass at t \= m log p is χ(p^m)(log p)p^{-m/2}, so ℒμ(u) \= Σ χ(p^m)(log p)p^{-m(u+1/2)}). Equivalently the dynamical Euler product is ∏\_p (1 − χ(p)p^{-s})^{-1} \= L(s,χ).  
**The G-block, correctly scoped.** The verification now constructs the p^{-m/2}-weighted measure and checks (G.1, G.2) its centered transform at s \= 3 against −ζ′/ζ(3) and −L′/L(3, χ), and (G.3) the explicit \+1/2 shift ℒμ(u) \= −L′/L(u \+ 1/2, χ), confirming it differs from −L′/L(u). This is a FORMAL-IDENTITY, not an orbit construction.

# **§13.  Non-Claims and Null Controls**

| Tag | Statement |
| ----- | ----- |
| NC-M50.1 | T-CORE-DATA is a data-level identification; the operator realisation is T-CORE-ALG / §7. |
| NC-M50.2 | At β \= 1/2 the weight is an actual type-III₁ KMS value, not an analytic continuation; only the Gibbs trace diverges. |
| NC-M50.3 | The seam–temperature identification (H-SB) is not proved; H-HD is not discharged by the seam alone. |
| NC-M50.4 | No prime is derived; primes are the generators of ℕ^{×}. No progress on RH/GRH (ZS-M49 F-M49.5 applies). |
| NC-M50.5 | ℚ\[ℚ/ℤ\] ⋊\_ρ ℕ^{×}, the log n roof, the n^{-β} weight, and the type-III₁ phase are not externally new; the corpus novelty is their internal derivation from polygon tetration. |
| NC-M50.6 | The §7 representation is covariant, satisfying the rational Bost–Connes relations; it is NOT proved faithful, and no universal / isomorphic realisation is claimed. |
| Null control | The stable-base measure matches no corpus constant (A, Q, z\*); reported as a negative result. |
| Null control | The type-III₁ factor identity carries zero information (the unique injective III₁ factor equals itself); not counted. |

# **§14.  Falsification Gates**

| Layer | Gate | Condition |
| ----- | ----- | ----- |
| Mathematical — immediate | F-M50.1 | If any Bost–Connes relation of §7 fails on finite-support vectors, H-ALG and T-CORE-ALG collapse. |
| Mathematical — immediate | F-M50.2 | If a finite register carries a proper isometry (V^\*V \= I, VV^\* ≠ I), M50.NG collapses. |
| Mathematical — immediate | F-M50.3 | If the kernel flat trace is not p^{+m/2} (Appendix B), §10's fibre/base separation is void. |
| Mathematical — immediate | F-M50.8 (new) | If ℒμ\_pkt^χ(u) ≠ −L′/L(u+1/2, χ) (the \+1/2 shift), M50.3′'s transform statement is wrong. |
| Consistency — revision | F-M50.4 | If H-SB is refuted (ℜ s \= 1/2 ≠ β \= 1/2 canonically), the half-density route loses the seam selection. |
| Consistency — revision | F-M50.7 (corrected) | If no skew-product/cocycle relates Fₐ to a ↦ ma, the two-direction interpretation collapses (commutation form RETRACTED). |
| Scope — immediate | F-M50.5 | If any Z-Spin paper infers RH/GRH progress from these gates, that inference is rejected on sight. |
| Cross-paper | F-M50.6 | If H-FLOW is refuted, ZS-M49 NC-M49.6 strengthens to an unrestricted horizontal no-go. |

# **§15.  Forward Direction \[NON-CLAIM — deferred to ZS-M51 / ZS-F47\]**

The vertical direction is contractive (z\* is attracting, |f′(z\*)| \< 1\) while the horizontal direction is expanding (b ↦ b^m is a degree-m endomorphism). A forward direction — not asserted here — asks whether this contraction/expansion pairing is the operator-level image of gravity's complementary action across the sectors: macroscopic time contraction with spatial expansion, and, complementarily, microscopic wave expansion with particle contraction. This has no observable, no prediction, and no action-level derivation in the present paper; it is a NON-CLAIM, deferred to ZS-M51 / ZS-F47. Any promotion of the radial coordinate Im(Log b / 2πi) to an RG / dissipative / cosmological scale flow requires an action-level derivation absent here.

# **§16.  Conclusion**

v1.3 is a rigor-and-expression patch that leaves the theory unchanged and finalises the algebraic content. The four PROVEN structures T1–T4 re-discover the Bost–Connes arithmetic core (T-CORE-DATA); the explicit ℓ²(ℕ^{×}) representation of §7 satisfies the group-algebra, isometry, covariance, and time-evolution relations (T-CORE-ALG), closing gate H-ALG as a covariant realisation. The finite-register no-go (M50.NG) forces an infinite-dimensional completion, and the two-clock linearization (M50.TC) exhibits the rank-one vertical clock and the infinite-rank arithmetic clock as one vector-valued cocycle.  
The corrected Laplace-transform statement — ℒμ\_pkt^χ(u) \= −L′/L(u \+ 1/2, χ), equivalently ℒ\_{1/2}μ\_pkt^χ(s) \= −L′/L(s, χ) — fixes the one substantive error of v1.2, and the G-block now tests the weighted measure itself. With M50.3′ DERIVED-CONDITIONAL on {H-FLOW, H-SB, H-WEIGHT, P-TRANS} (P-TRANS retained from ZS-M49), and with H-FLOW, H-SB, H-WEIGHT, P-TRANS deliberately left for separate work, M50 stands as the paper that establishes H-ALG closure and the two-clock architecture. Verification: fail-closed 36/36, count matching the manuscript.

# **Acknowledgements & Code Availability**

This revision integrates a third external rigor review (of v1.2). The verification suite (zs\_m50\_verify\_v1\_3.py) is fail-closed: it aborts with a non-zero exit code if any of the 36 executable checks fails or if the executed count differs from EXPECTED\_CHECKS \= 36\. The ALG-block constructs the ℓ²(ℕ^{×}) representation and verifies the group-algebra, isometry, covariance, and time-evolution relations on finite-support vectors; the G-block constructs the p^{-m/2}-weighted measure and verifies its centered transform and the \+1/2 shift. OPEN gates and external imports are logged via register() and not counted. Zero fitted parameters; (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED.

# **Appendix A — The Base-Coordinate Split**

General base a \= Log b ∈ ℂ, ℕ^{×} action a ↦ ma (T1). Unit circle |b| \= 1 ⇒ x \= a/(2πi) ∈ ℝ/ℤ and Sat\_{ℕ^{×}}{1/n} \= ℚ/ℤ (T2). General b ∈ ℂ^{×}: x ∈ ℂ/ℤ; the imaginary part log|b|/2π is the radial coordinate, outside the cyclotomic torus. All arithmetic-core statements live on the unit-circle layer.

# **Appendix B — Distributional-Kernel Flat Trace**

F\_p(x) \= px (mod 1); (L\_{p,s}f)(x) \= p^{-s}Σ\_{k=0}^{p-1}f((x+k)/p); K\_m(x,y) \= p^{-ms}Σ\_{j=0}^{p^m-1}δ(y − (x+j)/p^m). With g\_j(x) \= x(1 − p^{-m}) − j p^{-m}, the root is x\* \= j/(p^m−1), g′ \= 1 − p^{-m}, δ(g\_j) \= δ(x − x\*)/(1 − p^{-m}); exactly p^m−1 of j ∈ {0,…,p^m−1} give x\* ∈ \[0,1). Hence tr♭ L\_{p,s}^m \= p^{-ms}(p^m−1)/(1 − p^{-m}) \= p^{m(1-s)}; at s \= 1/2, p^{+m/2}. The denominator is the Atiyah–Bott factor |1 − (F^m)′^{-1}| \= |1 − p^{-m}|. Check HD.1 reconstructs this from the root count and Jacobian, not the closed form.

# **Appendix C — The ℓ²(ℕ^{×}) Representation Relations (Explicit)**

On ε\_k (k ≥ 1): e(0)ε\_k \= ε\_k; e(r)e(s)ε\_k \= e^{2πik(r+s)}ε\_k \= e(r+s)ε\_k; e(r)^\*ε\_k \= e^{-2πikr}ε\_k \= e(-r)ε\_k; μ\_n^\*μ\_nε\_k \= ε\_k; μ\_nμ\_n^\*ε\_k \= ε\_k \[n|k\] ; μ\_nμ\_mε\_k \= ε\_{nmk}; for gcd(n,m)=1, μ\_n^\*μ\_mε\_k \= μ\_mμ\_n^\*ε\_k \= ε\_{mk/n}\[n|k\]; μ\_n^\*e(r)μ\_nε\_k \= e(nr)ε\_k; μ\_ne(r)μ\_n^\*ε\_k \= ρ\_n(e(r))ε\_k; \[H,μ\_n\]ε\_k \= (log n)μ\_nε\_k; e^{itH}μ\_ne^{-itH}ε\_k \= n^{it}μ\_nε\_k. Checks ALG.0a–ALG.7 verify each on finite-support vectors.

# **References**

\[1\] K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-M7 v1.0: Berry–Keating Structural Isomorphism for a Finite-Dimensional Z₂ Transfer Operator (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-M22 v1.0: Arithmetic-Dedekind Scaffold of Z-Spin Cosmology (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-M48, ZS-M49 (Z-Spin Cosmology, 2026); POME-K, POME-K′, the P-TRANS / P-HALF conventions, no-gos NG1/NG2, and gate F-M49.7.  
\[5\] J.-B. Bost and A. Connes, “Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory,” Selecta Math. (N.S.) 1, 411–457 (1995).  
\[6\] M. Laca, “Semigroups of \*-endomorphisms, Dirichlet series, and phase transitions,” J. Funct. Anal. 152, 330–378 (1998).  
\[7\] M. Laca, N. S. Larsen and S. Neshveyev, “On Bost–Connes type systems for number fields,” J. Number Theory 129, 325–338 (2009).  
\[8\] S. Neshveyev, “Von Neumann algebras arising from Bost–Connes type systems,” (0 \< β ≤ 1 KMS states are type III₁), arXiv:0907.1456.  
\[9\] B. Sz.-Nagy, C. Foias, H. Bercovici, L. Kérchy, Harmonic Analysis of Operators on Hilbert Space (Springer, 2010).  
\[10\] C. Deninger, “Some analogies between number theory and dynamical systems on foliated spaces,” Doc. Math., Extra Vol. ICM I, 23–46 (1998); arXiv:1807.06400 (in press). \[Cited by statement.\]  
\[11\] A. Connes and C. Consani, “Knots, primes and class field theory,” Contemp. Math. (in press). \[Cited by statement.\]  
\[12\] M. Morishita, “On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces,” arXiv:2508.15971 (2026). \[Cited by statement.\]  
\[13\] D. Ruelle, “Zeta-functions for expanding maps and Anosov flows,” Invent. Math. 34, 231–242 (1976); V. Baladi, Positive Transfer Operators and Decay of Correlations (World Scientific, 2000).

# **Version History**

v1.3 (July 2026): Rigor-and-expression patch; no new theory. Corrected the Laplace-transform statement of M50.3′ to ℒμ\_pkt^χ(u) \= −L′/L(u+1/2, χ) (equivalently ℒ\_{1/2}μ(s) \= −L′/L(s,χ)) and rebuilt the G-block to test the p^{-m/2}-weighted measure and the \+1/2 shift (F-M50.8 added). Fixed ‘co-isometric’ → ‘isometric’; narrowed ‘all/full Bost–Connes relations’ to the group-algebra, isometry, covariance, and time-evolution relations and added checks ALG.0a–ALG.0c and ALG.3b; changed ‘machine-verified exactly’ → ‘proved algebraically and regression-tested’; narrowed the ‘direct-limit’ title/§7 to ‘canonical isometric representation’ (no inductive-limit construction claimed); replaced the PSLQ phrasing for {log p} independence with the unique-factorisation proof; added faithfulness non-claim NC-M50.6; corrected the crossed-product notation to ℚ\[ℚ/ℤ\] ⋊\_ρ ℕ^{×} (C\*(ℚ/ℤ) ⋊\_ρ ℕ^{×}). Converted key block equations to Word (OMML) and applied Word heading styles. Verification 36/36 fail-closed (was 30/30).  
v1.2 (July 2026): Constructive-closure revision. Constructed the internal ℓ²(ℕ^{×}) Bost–Connes representation (closing H-ALG); added M50.NG and M50.TC; split T-CORE; re-decomposed H-BC into {H-ALG, H-FLOW, H-SB, H-WEIGHT} \+ P-TRANS; fixed the β \= 1/2 wording, ‘saturation’ terminology, and the T2.2 tautology; rebuilt the suite fail-closed 30/30. (Superseded: M50.3′'s Laplace transform omitted the \+1/2 shift and the G-block did not test the weighted measure; ‘co-isometric’, ‘all relations’, ‘machine-verified’, ‘direct-limit’, and PSLQ-as-proof are all corrected in v1.3.)  
v1.1 / v1.0 (July 2026): honest-closure and initial releases; superseded as recorded in v1.2.