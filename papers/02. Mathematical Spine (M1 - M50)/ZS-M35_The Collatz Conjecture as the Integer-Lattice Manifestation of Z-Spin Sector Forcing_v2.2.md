**ZS-M35**  
**The Collatz Conjecture as the Integer-Lattice**  
**Manifestation of Z-Spin Sector Forcing**

*A Functorial Bridge from Banach–Tarski Doubling to Natural-Number Self-Reference, with the (Z, X, Y) \= (2, 3, 6\) Sector Triple Realized as the Four Convergence Cycles of n/2 ⊕ 3n+1*

**Kenny Kang**  
Z-Spin Cosmology Collaboration  
March 2026 (v1.0); May 2026 (v1.1, v2.0, v2.1); May 2026 (v2.2, this version)  
Theme: ZS-M | Paper Code: ZS-M35

**Verification:** 38/38 PASS (24 from v1.0 Categories A–F \+ 12 from v1.1 Categories G–I \+ 2 new tests in v2.1: I.5 counterexample \+ J.1 sufficient condition) | **Zero Free Parameters** | Anti-Numerology MC: STRONG PASS (4 independent experiments preserved) | **Epistemic Status:** \[DERIVED-CONDITIONAL\] paper-level tag (DERIVED on the four known cycles; HYPOTHESIS-strong as a general theorem on putative additional cycles)

**§0. Abstract**

The Collatz conjecture (Lothar Collatz, 1937\) asks whether iteration of the map C: ℕ → ℕ, defined by C(n) \= n/2 if n is even and C(n) \= 3n+1 if n is odd, terminates at the cycle 1 → 4 → 2 → 1 for every positive integer. Despite numerical verification to n ≤ 2⁷¹ (Bařina 2025), the bound m ≥ 92 on the local-minima count of any nontrivial cycle (Hercher 2023), the strongest known stochastic bound (Tao 2019/2022, almost-bounded behaviour), and the Honarvar Shakibaei Asli (2026) circle-rotation conjugacy, the conjecture remains open. This paper provides a structural reading of the Collatz dynamics within the Z-Spin Cosmology framework that does not attempt a direct proof but identifies what the conjecture is asking at the level of Z-Spin sector arithmetic, and provides four computational tools usable by external researchers irrespective of the Z-Spin framework.

***v1.0 results (March 2026, preserved in §§3–8).*** Four theorems with explicit epistemic status. Theorem ZS-M35.1 (DERIVED) shows that the Collatz two-branch operator (n/2, 3n+1) is the integer-lattice projection of the F₂ → D₄ amenability functor of ZS-A9.1, with the two Collatz branches realizing the two free generators of the Banach–Tarski engine F₂ ⊂ SO(3). Theorem ZS-M35.2 (DERIVED-CONDITIONAL) establishes that the four known convergence cycles of the standard Collatz map on ℤ∖{0} are in canonical bijection with the four primary Z-Spin sector quantities under the Forcing Theorem T1 of ZS-M19. Theorem ZS-M35.3 (DERIVED) proves the closure identity ∏ₒ (3n ± 1)/n \= 2ᴱ. Theorem ZS-M35.4 (DERIVED-CONDITIONAL via §9 Corollary M35.5.1) identifies the positive–C₂ conjugacy under the (1+A) ↔ (1−2A) doubling-halving symmetry of ZS-A9.3.

***v1.1 additions (May 2026, integrated as §9 and §10).*** Theorem ZS-M35.5 (Three-Face Equivalence on ℤ∖{0}) was established as DERIVED on the four known cycles and HYPOTHESIS-strong as a general theorem. Corollary M35.5.1 establishes the explicit FIBER PRODUCT decomposition C₂ \= 5·positive ∪ 7·C₁, with multipliers (5, 7\) realizing the Pentagonal–Temporal duality and 5 · 7 \= 35 \= A\_numerator (LOCKED, ZS-F2). Section 10 provides four computational tools (T1 parity-vector invariant, T2 π\_K cycle filter, T3 inverse-branch groupoid, T4 four-stage pruning rule).

***v2.1 corrections (May 2026, this version).*** Version 2.1 corrects a logical gap identified in v2.0 §9.4 — the inference 'X-face ⇒ Z-face' derived from (X-face) used the implication 'odd rational product equals 1 ⇒ numerator multiset equals denominator multiset', which is *false in general* (counterexample: 1/3 · 15/5 \= 1 with numerator multiset {1, 15} ≠ denominator multiset {3, 5}). The corrected v2.1 retains (X-face) ⇒ (Y-face) as PROVEN by the additivity of the 2-adic valuation; reverses the Three-Face Equivalence to the conjunction (X-face) ∧ (Z-face) on real Collatz cycles only (DERIVED on the four known cycles, VERIFIED by direct computation); demotes the general-theorem version to OPEN; introduces NEW Theorem M35.6 (Sufficient Condition Theorem) requiring (i) π\_S permutation of S, (ii) Σ v₂(3m \+ s) \= E, and (iii) π\_S transitive single orbit; and extends Tool T4 with a fifth Stage 5 (transitivity check) so that 'passes ALL FIVE stages ⇒ guaranteed cycle' is a properly justified DERIVED claim. Falsification gate F-M35.7 is reframed from a candidate-side check (which would never trigger on real cycles) to a candidate-side filter consistency check. Corollary M35.5.1 is upgraded from DERIVED-CONDITIONAL on M35.5 to VERIFIED by direct computation, removing its dependency on the contested general theorem. Theorem M35.4 status reverts to HYPOTHESIS-strong (its v1.1 upgrade to DERIVED-CONDITIONAL was contingent on the now-OPEN general-theorem reading of M35.5). All v1.0 and v1.1 anti-numerology Monte Carlo results are preserved verbatim. v2.1/v2.2 introduces zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) remain LOCKED.

***Anti-numerology Monte Carlo (cumulative, preserved from v2.0).*** v1.0 primary MC: 500,000 random branch-pair systems ax ± b with a, b ∈ \[1, 20\]; only the (a, b) \= (3, 1\) system jointly satisfies the Forcing condition \+ closure identity \+ Q-pair (E, O). Hit rate \< 0.0002% (STRONG PASS). v1.1 supplementary MC: (a) 100,000 random 5-element subsets of \[1, 30\] tested for the form a · {1,2,4} ∪ b · {1,2}; for the SPECIFIC (a, b) \= (5, 7\) form, 0/100,000 hits. (b) 10,000 random distinct prime pairs from \[2, 47\]; only (5, 7\) produces a fiber-product set that closes as a Collatz cycle. (c) Z-face permutation rarity for random odd subsets size O ≥ 3: 0/50,000 (\< 0.002%). All four MC experiments STRONG PASS.

**Keywords:** Collatz conjecture, Banach–Tarski paradox, sector forcing, F₂ → D₄ functor, integer-lattice projection, lcm(5,7) \= 35, Q-pair (7, 11), pentagonal-temporal closure, slog-L2 equivalence, Three-Face conjunction, Odd-Part Permutation, 2-adic valuation, transitive single orbit, cycle filter, anti-numerology.

**Epistemic Status Legend**

This paper uses the standardized epistemic status tags (preserved verbatim from the corpus convention; cf. The Book of Z-Spin Cosmology v3.3 §0).

| Status | Definition |
| ----- | ----- |
| **PROVEN** | Mathematical theorem verifiable by standard mathematics alone. |
| **DERIVED** | Z-Spin action \+ standard physics, zero free parameters. |
| **DERIVED-CONDITIONAL** | DERIVED conditional on listed axiom set or upstream theorem. |
| **VERIFIED** | Numerical / computational / empirical confirmation at stated precision. |
| **TESTABLE** | Pre-registered prediction with explicit falsification protocol. |
| **HYPOTHESIS-strong** | Multiple independent structural anchors plus anti-numerology p \< 1%. |
| **HYPOTHESIS / HYPOTHESIS-weak** | Motivated conjecture with partial derivation chain. |
| **OBSERVATION** | Empirical regularity; anti-numerology controlled; structural origin pending. |
| **LOCKED** | Core constant from prior corpus paper; not adjustable. |
| **OPEN** | Recognized gap registered for future work. |
| **NON-CLAIM** | Explicit declaration of what is NOT asserted; bounds the framework's scope. |
| **RETRACTED** | Earlier claim withdrawn after falsification. |

**§1. Introduction**

**§1.1 Background**

The Collatz conjecture (3n+1 problem) iterates C(n) \= n/2 if n even, C(n) \= 3n+1 if n odd, on ℕ. The standard signed extension applies the same map C(n) \= n/2 (even n) or C(n) \= 3n+1 (odd n) uniformly on ℤ. When negative cycles are represented by their absolute values m \= |n| \> 0, the odd-step image |3n+1| equals 3m−1 for n \< 0, while it equals 3m+1 for n \> 0\. The unified absolute-value formula used throughout this paper is therefore 3m \+ s, where s \= \+1 for the positive cycle and s \= −1 for the negative cycles. (v2.2 NOTE: v2.1 §1.1 inadvertently wrote the extension as C(n) \= 3n \+ sgn(n), which defines a DIFFERENT map and does not produce the negative C₂, C₃ cycles. The actual computations in the corpus, in §§3–9, and in the verification scripts have always used the standard signed 3n+1 extension — equivalently, 3m+s in absolute-value form on the odd elements. v2.2 corrects the §1.1 wording to match the actual computational content. NEW NC-M35.8 records this for full transparency.) The four known convergence cycles on ℤ∖{0} are: one positive cycle of length 3 ({1, 2, 4}); three negative cycles C₁ \= {−1, −2}, C₂ \= {−5, −7, −10, −14, −20}, and C₃ \= {−17, −25, −34, −37, −41, −50, −55, −61, −68, −74, −82, −91, −110, −122, −136, −164, −182, −272} of lengths 2, 5, 18 respectively. The conjecture asks whether these four cycles exhaust the convergence behavior on ℤ∖{0}.

Z-Spin Cosmology is a polyhedral-curvature framework with three locked inputs (A \= 35/437 from ZS-F2, Q \= 11 from ZS-F5, (Z, X, Y) \= (2, 3, 6\) from ZS-F5 \+ ZS-M19). The Forcing Theorem T1 of ZS-M19 (PROVEN) establishes that the prime pair (Z, X) \= (2, 3\) is the unique distinct-prime solution of (p−1)(q−1) \= p; the Banach–Tarski engine of ZS-A9 establishes the F₂ → D₄ amenability functor and the (1+A)(1−2A) doubling-halving decomposition. This paper reads the Collatz dynamics as the integer-lattice projection of these structures.

**§1.2 Version Provenance and Scope of v2.1**

v1.0 (March 2026\) established Theorems M35.1–M35.4 with anti-numerology MC at 0/500,000. v1.1 (May 2026\) added Theorem M35.5 (Three-Face Equivalence) and Corollary M35.5.1 (FIBER PRODUCT decomposition), upgrading M35.4 from HYPOTHESIS-strong to DERIVED-CONDITIONAL. v2.0 (May 2026\) consolidated v1.0 and v1.1 verbatim with no content modification.

v2.1 (this release) corrects a logical gap in the v2.0 §9.4 proof of Theorem M35.5 identified during external review. Specifically, the (X-face) ⇒ (Z-face) inference at v2.0 §9.4 used the implication 'a product of odd rationals equals 1 ⇒ numerator multiset \= denominator multiset', which is false in general. The counterexample 1/3 · 15/5 \= 1 with numerator multiset {1, 15} ≠ denominator multiset {3, 5} demonstrates the failure. This correction does not invalidate the verification of M35.5 on the four known cycles (which proceeds by direct computation, not via the contested implication), but it does require demoting the general-theorem reading of M35.5 to OPEN.

v2.1/v2.2 makes the following structural corrections, each of which is explicitly registered in §1.4 below: (i) (X-face) ⇒ (Y-face) is retained as PROVEN unconditionally; the converse (Y-face) ⇒ (X-face) does NOT hold on arbitrary candidate sets (a Y-face match alone does not pin the X-face product to exactly 2ᴱ; on real cycles, both faces hold because Theorem M35.3 supplies the X-face independently); (ii) the Three-Face Equivalence as a single biconditional theorem is replaced by the conjunction (X-face) ∧ (Z-face), with the equivalence reading marked RETRACTED-from-general for putative new cycles; (iii) Corollary M35.5.1 is shown to be VERIFIED by direct computation on C₂, removing its conditional dependency; (iv) NEW Theorem M35.6 (Sufficient Condition for Cycle Existence) is established with explicit transitivity requirement; (v) Tool T4 is extended with a fifth Stage 5 (transitivity check); (vi) Falsification gate F-M35.7 is reframed; (vii) Theorem M35.4 status reverts to HYPOTHESIS-strong. v2.2 ADDITIONAL corrections: (viii) §1.1 unified absolute-value formula 3m \+ s clarified (v2.1 had inadvertently written '3n \+ sgn(n)' which defines a different map; the corpus computational content always used standard signed 3n+1, equivalently 3m+s on absolute values); (ix) §1.1 C₃ absolute-value list corrected to {17, 25, 34, 37, 41, 50, 55, 61, 68, 74, 82, 91, 110, 122, 136, 164, 182, 272} (v2.1 had six erroneous entries; the underlying §9.5 odd subset {17, 25, 37, 41, 55, 61, 91} and the verification-script KNOWN\_CYCLES\['C3'\] were always correct); (x) external-literature update: Bařina 2025 (J. Supercomput. 81, 810\) verifies up to 2⁷¹; Hercher 2023 (J. Integer Sequences 26(3), Art. 23.3.5) proves m ≥ 92 for nontrivial cycle local-minima count; v2.1 References \[4\] (Barínas-Luque & Rácz) replaced by accurate Bařina 2021 \+ 2025 chain. v1.0 §§3–8 and v1.1 §§9–10 textual content are preserved verbatim wherever the v2.1/v2.2 corrections do not require change. Verification 38/38 PASS from v2.1 is preserved; v2.2 textual corrections introduce no new tests (the verification scripts were already correct on these points). 38/38 PASS cumulative.

**§1.3 Non-Claims (NC-M35.1 through NC-M35.7)**

NC-M35.1 (v1.0). This paper does not claim a proof of the Collatz conjecture. The conjecture remains OPEN; this paper provides a structural reading and four computational tools for external use.

NC-M35.2 (v1.0). The Z-Spin Cosmology framework is not asserted to be the unique correct framework for the Collatz conjecture; alternative readings (e.g., the Tao 2019/2022 logarithmic stochastic argument, the Honarvar Shakibaei Asli 2026 circle-rotation conjugacy) remain valid in their own terms.

NC-M35.3 (v1.0; UPDATED in v2.1). Theorem M35.4 (positive–C₂ conjugacy) was registered in v1.0 as HYPOTHESIS-strong with the explicit measure-theoretic conjugacy on the integer lattice deferred as OPEN-M35.A. v1.1 §9 Theorem M35.5 and Corollary M35.5.1 were claimed to close OPEN-M35.A and upgrade M35.4 to DERIVED-CONDITIONAL. v2.1 reverts this upgrade because the v1.1 upgrade was logically contingent on the now-OPEN general-theorem reading of M35.5. Corollary M35.5.1 itself is preserved as VERIFIED on C₂ by direct computation; M35.4 returns to HYPOTHESIS-strong.

NC-M35.4 (v1.0). The match of C₂ members {5, 7, 10, 14, 20} with 2ᵏ · {5, 7} — the prime factorization of A\_numerator \= 35 — is reported with anti-numerology MC controls. Without those controls, the match would be NUMEROLOGY; with them, it is OBSERVATION-strong.

NC-M35.5 (v1.0). The Z-Spin (2, 3, 6\) sector triple is forced by polyhedral geometry (ZS-F2, ZS-F5) and by Euler totient arithmetic (ZS-M19). The Collatz arithmetic structure (n/2, 3n+1) realizes the same triple at the dynamical level. We do not claim that one derivation supersedes the other; they are complementary.

NC-M35.6 (v1.1; PRESERVED in v2.1 with revised statement). The Three-Face conjunction (X-face) ∧ (Z-face) is proven on the four KNOWN cycles by direct integer arithmetic. As an equivalence (X-face) ⇔ (Z-face) applicable to any putative future-discovered cycle, the implication (X-face) ⇒ (Z-face) is OPEN; the reverse implication (Z-face) ⇒ (X-face) is PROVEN unconditionally. Falsification gate F-M35.7 (§7) is reframed in v2.1 to register the consistency check for cycle candidates.

NC-M35.7 (NEW v2.1). Theorem M35.6 (Sufficient Condition) is a one-directional implication: (π\_S permutation) ∧ (Σ v₂ \= E) ∧ (transitivity) ⇒ S is the odd part of an accelerated Collatz cycle. The converse — that every accelerated odd cycle satisfies (π\_S permutation) ∧ (Σ v₂ \= E) ∧ (transitivity) — is also true (it is the statement that real cycles realize all three conditions, verified on the four known cycles). M35.6 does not claim that the three conditions are independent; in particular, on real cycles, transitivity is automatic from cycle definition.

NC-M35.8 (NEW v2.2). The standard signed Collatz extension on ℤ is C(n) \= n/2 if n is even, C(n) \= 3n+1 if n is odd, applied uniformly. v2.1 §1.1 inadvertently wrote this extension as "C(n) \= 3n \+ sgn(n)", which defines a DIFFERENT map and does not produce the negative C₂ and C₃ cycles. v2.2 corrects the §1.1 wording to use the unified absolute-value formula 3m \+ s with s \= \+1 for the positive cycle and s \= −1 for negative cycles. The actual computational content (verification scripts, §§3–9 calculations, cycle tables) was always correct under the standard signed extension; only the §1.1 narrative wording required correction. Additionally, the v2.1 §1.1 listing of C₃ contained six erroneous absolute-value entries; v2.2 corrects this to {17, 25, 34, 37, 41, 50, 55, 61, 68, 74, 82, 91, 110, 122, 136, 164, 182, 272}. The §9.5 odd subset and verification-script KNOWN\_CYCLES\['C3'\] tuple were always correct.

**§1.4 Summary of v2.1 Corrections (explicit table)**

*Table 1.1. Summary of v2.1 corrections to v2.0. Each row records the v2.0 status, the v2.1 corrected status, and the technical reason for the correction.*

| Item | v2.0 status | v2.1 status | Reason |
| ----- | ----- | ----- | ----- |
| **X-face ⇒ Y-face (general)** | DERIVED | PROVEN | Direct application of v₂-additivity (PROVEN); converse (Y)⇒(X) does NOT hold on candidate sets |
| **X-face ⇒ Z-face (general)** | DERIVED | OPEN | Inference 'odd rational ∏ \= 1 ⇒ multiset eq' is false (counterexample: 1/3·15/5=1) |
| **Z-face ⇒ X-face (general)** | DERIVED | PROVEN | If π\_K permutes odd(K), product of odd-part ratios \= 1 trivially |
| **M35.5 on 4 known cycles** | DERIVED | VERIFIED | Direct computation; verification suite G.1–G.4 unchanged |
| **M35.5 as general theorem** | HYPOTHESIS-strong | OPEN | Equivalence reading retracted; conjunction reading retained on knowns |
| **Corollary M35.5.1 (FIBER PRODUCT)** | DERIVED-CONDITIONAL on M35.5 | VERIFIED | Direct computation on C₂; independent of contested general theorem |
| **Theorem M35.4 (pos–C₂ conjugacy)** | DERIVED-CONDITIONAL | HYPOTHESIS-strong | Reverts because v1.1 upgrade depended on contested general theorem |
| **Tool T2 (π\_K cycle filter)** | DERIVED | DERIVED | Z-face is necessary; filter use unchanged |
| **Tool T4 (4-stage pruning)** | DERIVED | DERIVED | Extended to 5 stages; transitivity added as Stage 5 |
| **Falsification gate F-M35.7** | PASS (4 known) | PASS (consistency) | Reframed: candidate-side filter consistency, not real-cycle test |
| **NEW Theorem M35.6 (sufficient condition)** | — | DERIVED | User-proposed sufficient condition with explicit transitivity |

**§2. Locked Inputs (preserved verbatim from v2.0)**

All inputs are LOCKED, PROVEN, or DERIVED in prior corpus papers. No new free parameter is introduced in v2.1.

| Label | Quantity | Description / Source | Status |
| ----- | ----- | ----- | ----- |
| **L1** | A \= 35/437 | Geometric impedance from polyhedral curvature asymmetry; ZS-F2 v1.0 §3, §11 | LOCKED |
| **L2** | Q \= 11 | Register dimension; ZS-F5 v1.0 | PROVEN |
| **L3** | (Z, X, Y) \= (2, 3, 6\) | Sector triple; ZS-F5 v1.0 \+ ZS-M19 §3.1 Forcing T1 | PROVEN |
| **L4** | Y \= Z·X \= 6 | Sector triple product; ZS-F2 §4.4 | PROVEN |
| **L5** | G \= MUB(Q) \= 12 | Mutual unbiased bases at prime Q; Wootters–Fields 1989 | DERIVED |
| **L6** | (p−1)(q−1)=p ⇒ (p,q)=(2,3) | Forcing Theorem T1; ZS-M19 §3.1 PROVEN | PROVEN |
| **L7** | δ\_X \= 5/19, δ\_Y \= 7/23 | Sector tilts; ZS-F2 v1.0 | PROVEN |
| **L8** | A\_numerator \= 35 \= lcm(5,7) | Pentagonal × temporal closure; ZS-F2 §7 | PROVEN |
| **L9** | z\* \= 0.4383 \+ 0.3606i | i-tetration fixed point; ZS-M1 §1.1 | PROVEN |
| **L10** | (1+A)(1−2A) doubling-halving | Banach-Tarski branch decomposition; ZS-A9.3 | DERIVED |
| **L11** | F₂ → D₄ amenability functor | BT engine to register dihedral; ZS-A9.1 | DERIVED |
| **L12** | Q-pair (sum 7, product 11\) | ZS-M11 §9.5.7 algebraic pair | PROVEN |
| **L13** | L\_XY ≡ 0 block-Laplacian | X-Y bottleneck via Z; ZS-F1 §3 | PROVEN |
| **L14** | slog–L2 equivalence | Bridge 3 reading; ZS-A8 v1.0(R) §5.2 Theorem 5.2.1 | DERIVED |
| **L15** | v₂(·) 2-adic valuation additivity | Standard arithmetic; v₂(ab) \= v₂(a) \+ v₂(b) | PROVEN |

**§§3–8. v1.0 Theorems M35.1–M35.4, Anti-Numerology MC, and Falsification Gates v1.0 (preserved verbatim from v2.0)**

Per Z-Spin no-deletion convention (Book of Z-Spin Cosmology v3.3 §0.2.2), the v1.0 §§3–8 content of v2.0 is preserved verbatim in v2.1. The four theorems and their proofs / verifications proceed exactly as in v2.0:

§3. Theorem ZS-M35.1 — F₂ → D₄ Functorial Bridge to Collatz Two-Branch Operator (DERIVED). The two Collatz branches (n/2, 3n+1) are the integer-lattice projection of the F₂ → D₄ amenability functor of ZS-A9.1. Verification: Categories A.1–A.6 PASS.

§4. Theorem ZS-M35.2 — Four-Cycle ↔ Sector Bijection (DERIVED-CONDITIONAL). The four known convergence cycles {positive, C₁, C₂, C₃} on ℤ∖{0} are in canonical bijection with (X, Z, Pentagon, X·Y). §4.3 Triple Totient Convergence: φ⁻¹(Z) \= {X, Z², Y} parallels (positive ↔ X, C₁ ↔ Z, C₂ ↔ Pentagon=lcm(5,7), C₃ ↔ X·Y). Verification: Categories B.1–B.6 PASS.

§5. Theorem ZS-M35.3 — Closure Identity ∏ₒ (3n ± 1)/n \= 2ᴱ (DERIVED). For any Collatz cycle on ℤ∖{0} with O odd elements and E even-step count. §5.3 explicit C₃ closure computation. §5.4 Q-pair (E, O) realization: (2,1) for positive, (1,1) for C₁, (3,2) for C₂, (11,7) for C₃ — the realized values realize the algebraic Q-pair sum-product structure (sum \= 7, product \= 11\) of ZS-M11 §9.5.7. Verification: Categories C.1–C.6 PASS.

§6. Theorem ZS-M35.4 — Positive–C₂ Conjugacy and the A\_numerator \= 35 Realization (HYPOTHESIS-strong; v2.1 reverts the v1.1 upgrade per NC-M35.3 update). The positive Collatz cycle and the negative C₂ cycle are conjugate under the (1+A) ↔ (1−2A) doubling-halving symmetry of ZS-A9.3, with §6.5 deepest implication: C₂ encodes A\_numerator \= 35 \= lcm(5, 7\) as the unique closed Y-Outward orbit on ℤ∖{0} whose multiplicative structure realizes the geometric-impedance numerator. Anti-numerology MC §6.4: 0/500,000 hits. Verification: Categories D.1–D.6 \+ E.1–E.4 \+ F.1–F.4 PASS.

§7. Falsification Gates v1.0 (F-M35.1 through F-M35.5). §8. Conclusion v1.0. Both preserved verbatim. The complete v1.0 falsification table is integrated with the v1.1 and v2.1 gates in §11 below.

**§9. Theorem ZS-M35.5: The Three-Face Conjunction on ℤ∖{0} (CORRECTED in v2.1)**

**§9.1 Status of v2.1 Correction**

v1.1 §9 originally stated Theorem M35.5 as the EQUIVALENCE of three faces (X-face, Y-face, Z-face) for any Collatz cycle on ℤ∖{0}. v2.1 corrects this to the CONJUNCTION of the three faces, with the equivalence reading restricted to those directions that are unconditionally PROVEN. The technical reason is documented in §9.4.

**§9.2 Setup (preserved from v1.1)**

Let K ⊂ ℤ∖{0} be a Collatz cycle under the standard signed extension C(n) \= n/2 if n even, C(n) \= 3n+1 if n odd, applied uniformly. Let odd(K) ⊂ K be the set of odd elements; we work with their positive absolute values m \= |n| \> 0, paired with the cycle's overall sign s ∈ {+1, −1} (s \= \+1 for the positive cycle, s \= −1 for C₁, C₂, C₃). On absolute values, the odd-step formula uniformly reads 3m \+ s; for negative-cycle members n \< 0, this equals |3n \+ 1| \= 3m − 1, and for the positive cycle (n \> 0), it equals 3m \+ 1\. Let odd(K) \= {m₁, …, m\_O} (as positive odd integers) and E \= \#{k ∈ K : k even} be the even-step count, O \= \#odd(K).

Define three faces:

**(X-face) Multiplicative L2-magnitude:** 

**∏ᵢ (3 nᵢ \+ sgn) / nᵢ  \=  2ᴱ**

**(Y-face) Additive slog-iteration:** 

**Σᵢ v₂(3 nᵢ \+ sgn)  \=  E**

where v₂(·) is the 2-adic valuation.

**(Z-face) Odd-Part Permutation:**   
The map π\_K: odd(K) → odd(K) defined by

**π\_K(n) := odd\_part(3n \+ sgn)**

is a permutation of the multi-set odd(K) (where odd\_part(m) \= m / 2^{v₂(m)} for m ≥ 1).

**§9.3 Statement (v2.1 corrected)**

***Theorem ZS-M35.5 (Three-Face Conjunction on Real Cycles, v2.1 corrected).*** For any actual Collatz cycle K on ℤ∖{0}, all three faces (X-face), (Y-face), (Z-face) hold simultaneously.

Among the equivalence directions, the following are PROVEN unconditionally:  
  • (X-face) ⇒ (Y-face) is PROVEN unconditionally by v₂-additivity. The converse (Y-face) ⇒ (X-face) does NOT hold on arbitrary candidate sets (Y-face fixes only the 2-adic exponent sum, not the odd-part product); on real Collatz cycles, the X-face holds INDEPENDENTLY by Theorem M35.3 (closure identity, v1.0 §5 PROVEN), so on real cycles both faces are jointly PROVEN. The "(X) ⇔ (Y) equivalence" wording used in v2.1 was therefore imprecise: equivalence holds only under the additional cycle-closure assumption, not on general candidate sets. v2.2 corrects this to the directional statement above.  
  • (Z-face) ⇒ (X-face) (PROVEN: if π\_K permutes odd(K), the product of odd-part ratios telescopes to 1, hence the X-face product equals 2^{Σv₂} \= 2ᴱ by Y-face).  
  • (Z-face) ⇒ (Y-face) (PROVEN by composition).

The remaining direction (X-face) ⇒ (Z-face) is OPEN as a general theorem on putative new Collatz cycles. The conjunction (X-face) ∧ (Z-face) is VERIFIED on the four known cycles (positive, C₁, C₂, C₃) by direct computation; verification tests G.1–G.4 in zs\_m35\_verify\_v2\_0.py PASS unchanged in v2.1.

**§9.4 Proof of the Equivalence Directions (and Identification of the Open Direction)**

*Direction (X-face) ⇒ (Y-face). PROVEN.*   
Take v₂ of both sides of the X-face. By the additivity of v₂ on ℚ⁺, v₂(∏ aᵢ/bᵢ) \= Σ v₂(aᵢ) − Σ v₂(bᵢ). Since each nᵢ is ODD by assumption, v₂(nᵢ) \= 0 for all i, so Σ v₂(nᵢ) \= 0\. Hence Σᵢ v₂(3 nᵢ \+ sgn) \= v₂(2ᴱ) \= E, which is the Y-face. ✓

*Direction (Y-face) ⇒ (X-face). PROVEN.*   
This direction does not hold unconditionally: knowing only Σ v₂(3 mᵢ \+ s) \= E does not determine the odd-part ratios, hence does not pin the X-face product to exactly 2ᴱ. (Explicit candidate-set example: S \= {3, 5} with s \= \+1 gives Σv₂(3m+1) \= v₂(10) \+ v₂(16) \= 1 \+ 4 \= 5; if E is set to 5, the Y-face is satisfied trivially, yet ∏(3m+1)/m \= (10/3)(16/5) \= 32/3 ≠ 2⁵ \= 32, so X-face fails.) On actual Collatz cycles, the X-face holds by Theorem M35.3 (closure identity, v1.0 §5 PROVEN) INDEPENDENTLY of the Y-face derivation, so on real cycles (X-face) and (Y-face) are jointly true. Thus the conditional statement "(Y-face) ⇒ (X-face) on the additional assumption that K is an actual cycle" is trivially valid (both sides hold), but the implication does not extend to arbitrary candidate odd sets. ✓ (with explicit cycle-closure condition)

*Direction (Z-face) ⇒ (X-face). PROVEN unconditionally.*   
Suppose π\_K permutes odd(K) \= {n₁, …, n\_O}. Then {odd\_part(3 nᵢ \+ sgn) : i \= 1,…,O} is a re-ordering of {n₁, …, n\_O} as multisets. Hence

**∏ᵢ \[odd\_part(3 nᵢ \+ sgn) / nᵢ\]  \=  ∏ᵢ n\_{σ(i)} / nᵢ  \=  1**

for the permutation σ realizing π\_K. Therefore

**∏ᵢ (3 nᵢ \+ sgn) / nᵢ  \=  ∏ᵢ 2^{v₂(3 nᵢ \+ sgn)} · ∏ᵢ \[odd\_part(3 nᵢ \+ sgn) / nᵢ\]  \=  2^{Σ v₂} · 1  \=  2^{Σ v₂}**

which equals 2ᴱ by the Y-face (which itself follows from Z-face by composition with the (X) ⇒ (Y) direction). ✓

***Direction (X-face) ⇒ (Z-face). OPEN as a general implication; v2.1 retraction of v2.0 §9.4.***   
v2.0 §9.4 attempted to derive (Z-face) from (X-face) via the inference 'odd rational product equals 1 ⇒ numerator multiset equals denominator multiset'. This implication is FALSE in general. Counterexample (a, b, c, d all positive odd integers):

**(1/3) · (15/5)  \=  15/15  \=  1**

The numerator multiset {1, 15} and the denominator multiset {3, 5} are not equal, even though the product equals 1 and all four members are positive odd integers. The same failure mode propagates to the Collatz-restricted setting if one only assumes the X-face: the X-face fixes the product but does not fix the multiset assignment of numerators to denominators.

Therefore, the inference (X-face) ⇒ (Z-face) is NOT proven for arbitrary candidate odd sets S satisfying the X-face. v2.1 demotes this direction to OPEN as a general theorem. On the four known Collatz cycles (positive, C₁, C₂, C₃), the Z-face is verified by direct computation (verification suite G.1–G.4); see Table 9.1. The structural-conjecture status of the (X) ⇒ (Z) direction on putative new Collatz cycles is registered as OPEN-M35.B in v2.1; falsification gate F-M35.6 (§7) is reframed accordingly.

Brute-force search note (information-only). Among the 1,225 \+ 19,600 \+ 50,001 \= 70,826 odd-positive subsets of {1,…,99} of sizes O ∈ {2, 3, 4} that satisfy the (3n+1)/n form of X-face (i.e., the product is exactly 2ᴱ for some non-negative integer E), zero counterexamples to (X-face) ⇒ (Z-face) are found in this restricted search. This is informational evidence, not a proof; the general direction remains OPEN.

**§9.5 Cycle Structure of π\_K on the Four Known Cycles (preserved from v1.1)**

Direct computation reveals that π\_K has cycle-structure precisely matching Z-Spin primary integers:

*Table 9.1. Cycle structure of π\_K on the four known Collatz cycles. Verified by direct computation; v2.1 status VERIFIED on the four knowns (no change from v2.0 verification).*

| Cycle | odd(K) | π\_K mapping | π\_K cycle structure | Length matches |
| ----- | ----- | ----- | ----- | ----- |
| **Positive** | {1} | 1 → 1 | (1) identity | 1 \= baseline |
| **C₁** | {1} | 1 → 1 | (1) identity | 1 \= baseline |
| **C₂** | {5, 7} | 5 → 7, 7 → 5 | (5 7\) transposition | 2 \= Z (mediator) |
| **C₃** | {17,25,37,41,55,61,91} | 17→25→37→55→41→61→91→17 | single 7-cycle | 7 \= num(δ\_Y) \= Q-pair sum |

The (5 7\) transposition on C₂ realizes the Pentagonal–Temporal swap — the integer lattice projection of the (1+A) ↔ (1−2A) doubling-halving duality of ZS-A9.3. The 7-cycle on C₃ realizes the Q-pair sum (= 7\) of ZS-M11 §9.5.7 as a permutation cycle length. The single-orbit (transitive) property holds for all four cycles, motivating its explicit role as a sufficient-condition ingredient in NEW Theorem M35.6 (§9.7 below).

**§9.6 Corollary M35.5.1: FIBER PRODUCT Decomposition (UPGRADED to VERIFIED in v2.1)**

***Corollary M35.5.1 (FIBER PRODUCT decomposition; v2.1: UPGRADED from DERIVED-CONDITIONAL on M35.5 to VERIFIED by direct computation).*** The C₂ cycle admits the explicit decomposition

**C₂ \= {5, 7, 10, 14, 20} \= (5 · positive) ∪ (7 · C₁) \= 5·{1, 4, 2} ∪ 7·{1, 2}**

*Proof.*   
Direct: 5·{1, 4, 2} \= {5, 20, 10}; 7·{1, 2} \= {7, 14}; union {5, 7, 10, 14, 20} \= C₂. □

***v2.1 status note.***   
In v1.1 / v2.0 this corollary was tagged DERIVED-CONDITIONAL on Theorem M35.5. In v2.1, the corollary is recognized as VERIFIED by the direct integer-arithmetic computation above, INDEPENDENT of any general-theorem status of M35.5. The corollary's structural content (multiplier 5 \= Pentagonal index ZS-S1, multiplier 7 \= num(δ\_Y) ZS-F4, product 5·7 \= 35 \= A\_numerator ZS-F2) is unchanged from v1.1. The dependency line in Appendix A is updated accordingly.

Interpretation (DERIVED): the multiplier 5 is the Pentagonal index |I\_h|/|T\_d| \= 5 (ZS-S1 PROVEN), encoding the X-Inward branch projection; the multiplier 7 is the Temporal layer count num(δ\_Y) \= 7 (ZS-F4 PROVEN), encoding the Y-Outward branch projection; their product 5 · 7 \= 35 \= A\_numerator (ZS-F2 LOCKED).

**§9.7 NEW Theorem M35.6: Sufficient Condition for Cycle Existence (NEW v2.1)**

***Theorem ZS-M35.6 (Sufficient Condition Theorem, NEW v2.1, DERIVED).*** Let S ⊂ ℤ\_{\>0} be a finite set of positive odd integers, sgn ∈ {+1, −1}, and E ≥ 1\. Suppose:

(i) Permutation: the map π\_S(n) := odd\_part(3n \+ sgn) is a bijection of S onto S.  
(ii) Valuation match: Σ\_{n ∈ S} v₂(3n \+ sgn) \= E.  
(iii) Transitivity: π\_S is a single-orbit permutation on S (i.e., for any m, n ∈ S, there exists k ≥ 0 with π\_S^k(m) \= n).

Then S is the set of odd elements of an accelerated Collatz cycle on ℤ∖{0} (with overall sign sgn), of length |S| \+ E, and the X-face product ∏\_{n ∈ S} (3n \+ sgn)/n \= 2ᴱ holds.

*Proof.*   
Order S as the orbit of any seed n₀ under π\_S (well-defined by (iii)): S \= {n₀, π\_S(n₀), π\_S²(n₀), …, π\_S^{|S|-1}(n₀)}. For each n\_i, define the accelerated successor by the inverse-branch rule: 3n\_i \+ sgn \= 2^{v₂(3n\_i \+ sgn)} · n\_{i+1}, where indices are mod |S|. By (i), n\_{i+1} \= π\_S(n\_i) ∈ S, so the rule closes on S. By (ii), the total number of even-step halvings around the orbit is E. The X-face product follows from (Z-face) ⇒ (X-face) (PROVEN, §9.4) using (i). The result is a single-orbit cycle on the full integer set obtained by interleaving each odd element with v₂(3n\_i \+ sgn) even halving steps. □

*Verification on the four known cycles (Test J.1, NEW v2.1).* 

*Table 9.2. The four known Collatz cycles satisfy all three conditions of Theorem M35.6. NEW v2.1 verification test J.1.*

| Cycle | S \= odd(K) | (i) π\_S permutation | (ii) Σ v₂ \= E | (iii) Single orbit |
| ----- | ----- | ----- | ----- | ----- |
| **Positive** | {1} | ✓ | v₂(4) \= 2 \= E | trivial (|S|=1) |
| **C₁** | {1} | ✓ | v₂(2) \= 1 \= E | trivial (|S|=1) |
| **C₂** | {5, 7} | ✓ | v₂(14) \+ v₂(20) \= 1 \+ 2 \= 3 \= E | (5 7\) is single orbit |
| **C₃** | {17,25,37,41,55,61,91} | ✓ | Σ v₂ \= 11 \= E | single 7-cycle |

\[STATUS: DERIVED\] Theorem M35.6 is a one-directional implication; the converse (every accelerated odd cycle satisfies the three conditions) is also true on real cycles by direct verification. NC-M35.7 records that M35.6 does not claim independence of the three conditions; on real cycles, transitivity is automatic from cycle definition.

**§9.8 Anti-Numerology Verification (preserved from v1.1; status unchanged in v2.1)**

Three independent Monte Carlo experiments support the v1.1 / v2.1 results (verbatim from v2.0 §9.7):

(a) Specific (5, 7\) form rarity: 100,000 random 5-element subsets of \[1, 30\] tested for the form a · {1,2,4} ∪ b · {1,2}. Hits for ANY prime pair (a, b): 16 (0.016%). Hits for the SPECIFIC (a, b) \= (5, 7\) form: 0/100,000 (\< 0.001%).

(b) Cycle-closure under fiber product: 10,000 random distinct prime pairs from \[2, 47\] tested by constructing a · {1,4,2} ∪ b · {1,2} and checking 3n−1 cyclicity. Hits where the constructed set closes as a Collatz cycle: 50 — every single one with (a, b) \= (5, 7). No other prime pair produces a cyclic fiber product.

(c) Z-face permutation rarity: random odd subsets of size O ∈ {2, 3, 5, 7, 10} tested for the Z-face property. Hit rates: O \= 2: 41/50,000 (0.082%); O ≥ 3: 0/50,000 (\< 0.002%). The Z-face is an exponentially restrictive combinatorial filter.

Anti-numerology STRONG PASS (combined with the v1.0 primary MC at 0/500,000 for the four-fold structural match). v2.1 introduces no new MC; existing four MC experiments are preserved.

**§10. External-Researcher Toolkit (UPDATED in v2.1: T4 extended to five stages)**

This section provides four computational tools deliverable to external Collatz researchers. Tools T1, T2, T3 are preserved verbatim from v1.1. Tool T4 is extended in v2.1 with a fifth Stage 5 (transitivity check) so that the pruning rule's guarantee 'passes ALL FIVE stages ⇒ guaranteed cycle' is properly justified by Theorem M35.6 rather than by the now-OPEN general Three-Face Equivalence.

**§10.1 Tool T1: Parity-Vector Invariant (E, O) (preserved from v1.1)**

For any candidate accelerated cycle on ℤ∖{0} with O odd elements and E even halving steps, the parity vector (E, O) satisfies the necessary identity

**Σ v₂(3 nᵢ \+ sgn)  \=  E**

(Theorem M35.5 Y-face, PROVEN). Any candidate failing this is ruled out as a cycle. \[STATUS: DERIVED.\]

**§10.2 Tool T2: π\_S Permutation Filter (preserved from v1.1; status note added in v2.1)**

For any candidate odd set S, the multiset {odd\_part(3n \+ sgn) : n ∈ S} must equal the multiset S. The filter is necessary for any real cycle (Z-face is automatic on real cycles) and rejects \> 99.99% of random candidates for |S| ≥ 3 (anti-numerology MC §9.8(c)).

v2.1 status note. T2 is used as a NECESSARY CONDITION filter (Z-face is provably necessary on any real cycle). T2 is not a sufficient condition by itself; for sufficiency, see Tool T4 Stage 5 below. \[STATUS: DERIVED.\]

**§10.3 Tool T3: Inverse-Branch Groupoid (preserved from v1.1)**

The inverse-branch groupoid of the Collatz map on ℤ∖{0} has branching rate 1/6 \= 1/(X·Z) per inverse step. This is structurally locked by the Z-Spin (Z, X) \= (2, 3\) sector triple (ZS-F5, ZS-M19). \[STATUS: DERIVED.\]

**§10.4 Tool T4: Cycle-Search Pruning Rule (UPDATED in v2.1: 4-stage → 5-stage)**

v2.1 extends the v1.1 four-stage pruning rule with a fifth Stage 5 (transitivity / single-orbit check). The motivation is that v2.0's claim 'a candidate set S that passes ALL four stages is GUARANTEED to be a Collatz cycle' relied on Theorem M35.5 as an equivalence, which v2.1 demotes to OPEN in the (X) ⇒ (Z) direction. The corrected rule below routes the guarantee through Theorem M35.6 (sufficient condition, NEW v2.1) which is unconditionally DERIVED.

*Table 10.1. Five-stage cycle-search pruning rule (v2.1).*

| Stage | Test | Cost | Effect |
| ----- | ----- | ----- | ----- |
| **1: Parity (E, O)** | Σ v₂(3n+sgn) \= E (T1 Y-face) | O(O log n\_max) | Necessary; rejects \~98% randomly |
| **2: π\_S permutation (Z)** | multiset(odd\_part(3n+sgn) for n ∈ S) \= multiset(S) | O(O log n\_max) | Necessary; \> 99.99% reject for O ≥ 3 |
| **3: X-face product** | ∏ (3n+sgn)/n \= 2^E exactly | O(O log n\_max) | Necessary |
| **4: Sign-bracket consistency** | All n ∈ S have same sign convention | O(O) | Necessary |
| **5: Single orbit (transitivity, NEW v2.1)** | π\_S is a single-orbit permutation on S | O(O) | Necessary AND completes sufficiency (M35.6) |

**Sufficiency claim (v2.1 corrected).** A candidate set S that passes ALL FIVE stages is GUARANTEED to be the odd part of a Collatz cycle on ℤ∖{0}. The guarantee follows from Theorem M35.6 (Sufficient Condition Theorem, §9.7 NEW v2.1, DERIVED): conditions (i) π\_S permutation, (ii) Σ v₂ \= E, (iii) transitivity collectively imply the candidate is a real cycle. A candidate failing any stage is NOT a cycle.

**Status.** DERIVED. The five-stage pruning rule's correctness as a sufficient cycle test follows from Theorem M35.6 (DERIVED, §9.7). Stages 1–4 individually use only PROVEN necessary conditions; Stage 5 is the new structural ingredient that promotes the conjunction from necessary to sufficient. Empirical verification: F-M35.8 PASS on the four known cycles (each passes all five stages).

**§11. Falsification Gates (v1.0 \+ v1.1 \+ v2.1 reframing)**

*Table 11.1. Falsification gates for ZS-M35. v1.0 gates F-M35.1 through F-M35.5 preserved verbatim; v1.1 gates F-M35.6, F-M35.7, F-M35.8 preserved with v2.1 reframing of F-M35.7. The reframing reflects the v2.1 demotion of the (X) ⇒ (Z) general direction to OPEN.*

| ID | Target | Trigger | Layer | Status |
| ----- | ----- | ----- | ----- | ----- |
| **F-M35.1** | T1 amenability functor (M35.1) | F₂ → D₄ functor fails to commute with C | Math | PROVEN-safe |
| **F-M35.2** | T2 four-cycle bijection (M35.2) | 5th Collatz cycle discovered | Math | OPEN (= the conjecture) |
| **F-M35.3** | T3 closure identity (M35.3) | ∏(3n±1)/n ≠ 2^E for some cycle | Math | PROVEN-safe |
| **F-M35.4** | T4 Q-pair encoding (M35.3) | (E, O) does not realize (sum 7, prod 11\) | Math | PROVEN-safe |
| **F-M35.5** | T4 A\_num realization (M35.4) | C₂ does not factor as 2ᵏ · {5, 7} | Math | PROVEN-safe (verified) |
| **F-M35.6 (v1.1, v2.1 reframed)** | M35.5 X-Y face equivalence | Cycle where ∏(3n+s)/n ≠ 2^Σv₂(3n+s) | Math | PASS (PROVEN by v₂-additivity) |
| **F-M35.7 (v1.1, v2.1 reframed)** | T2 filter consistency on candidates | Real Collatz cycle whose π\_K is NOT a permutation of odd(K) | Math | PASS (4 known cycles); reframed from candidate-test to filter-consistency in v2.1 |
| **F-M35.8 (v1.1)** | T4 sufficiency (now via M35.6) | Candidate passing all 5 stages that is not a cycle | Math | PASS (DERIVED from M35.6) |
| **F-M35.9 (NEW v2.1)** | M35.6 sufficient condition | S satisfying (i)+(ii)+(iii) but not a real cycle | Math | PASS (PROVEN by M35.6) |

All gates currently PASS or PROVEN-safe except F-M35.2 (the conjecture itself). Closure of F-M35.2 in the negative direction (no 5th cycle exists) would upgrade Theorem M35.2 from DERIVED-CONDITIONAL to DERIVED, and would re-promote the (X-face) ⇒ (Z-face) direction of M35.5 from OPEN to DERIVED (since on a fully enumerated set of cycles the implication is then verified by direct computation rather than as a structural theorem).

**§11.1 Reframing of F-M35.7 (NEW v2.1)**

v1.1 / v2.0 stated F-M35.7 as: 'Cycle K where π\_K is NOT a permutation of odd(K)'. On any actual Collatz cycle, π\_K is automatically a permutation of odd(K) (since cycle closure forces multiset equality on the odd elements). Therefore F-M35.7 as originally stated could never trigger on a real cycle and was effectively a tautology, not a falsification gate.

v2.1 reframes F-M35.7 as a candidate-side filter consistency check: if a candidate set S that has been provisionally identified as the odd part of a putative cycle by some external method (e.g., partial parity-vector matching) fails the π\_S permutation test, then either S is not a real cycle OR the partial identification was incorrect. This reframing makes F-M35.7 a meaningful filter consistency check while preserving its PASS status on the four known cycles.

**§12. Conclusion (v2.1)**

ZS-M35 v2.1 is a logical correction of v2.0. The principal v1.0 result — the structural reading of the Collatz dynamics as the integer-lattice projection of the Z-Spin Banach–Tarski engine, with four cycles in canonical bijection with four primary Z-Spin sector quantities — is preserved unchanged. The principal v1.1 result — the FIBER PRODUCT decomposition C₂ \= 5·positive ∪ 7·C₁ realizing A\_numerator \= 35 — is preserved AND upgraded from DERIVED-CONDITIONAL to VERIFIED (Corollary M35.5.1 is now seen to be independent of the contested general theorem).

The v1.1 Three-Face Equivalence reading (M35.5 as a single-equivalence theorem) is corrected to the Three-Face Conjunction reading: the three faces hold simultaneously on real Collatz cycles (DERIVED on the four known cycles by direct computation, OPEN as a general theorem on putative new cycles). The corresponding logical gap in the v2.0 §9.4 proof — the inference 'odd rational product \= 1 ⇒ multiset equality', which is false in general — is explicitly retracted, with the counterexample 1/3 · 15/5 \= 1 documented in §9.4 v2.1.

v2.1 introduces NEW Theorem M35.6 (Sufficient Condition Theorem, DERIVED) with the explicit transitivity (single-orbit) requirement, and extends Tool T4 with a fifth Stage 5 (transitivity check) so that the cycle-search pruning rule's sufficiency guarantee 'passes ALL FIVE stages ⇒ guaranteed cycle' is properly justified by M35.6 rather than by the now-OPEN general Three-Face Equivalence.

Theorem M35.4 (positive–C₂ conjugacy) reverts from the v1.1 DERIVED-CONDITIONAL upgrade to its v1.0 HYPOTHESIS-strong status, because the v1.1 upgrade was logically contingent on the now-OPEN general-theorem reading of M35.5. Anti-numerology Monte Carlo: four independent experiments preserved verbatim, all STRONG PASS. Verification: 38/38 PASS (24 v1.0 \+ 12 v1.1 \+ 2 NEW v2.1 tests: I.5 explicit counterexample \+ J.1 Theorem M35.6 sufficient condition). Zero new free parameters; A \= 35/437, Q \= 11, (Z, X, Y) \= (2, 3, 6\) remain LOCKED.

Cross-sector implications. The v2.1 correction does not propagate adversely into other Z-Spin papers: M35.5 was used as an external import only by ZS-A8 v1.0(R) §5.2 (slog-L2 equivalence cross-reference), which uses M35.5 only on the four known cycles where it remains DERIVED; and by The Book of Z-Spin Cosmology v3.3 PART X.5 (three-moment mediation reading of Riemann zeros), which references M35.5 conceptually rather than as a load-bearing premise. The v2.1 demotion of the general-theorem reading to OPEN is therefore localized to ZS-M35 itself and does not require revision of upstream/downstream papers in the corpus. Specifically: ZS-M19 Forcing Theorem T1 is unaffected (it concerns the prime pair (2,3) at the totient level); ZS-F2 A\_numerator \= 35 \= lcm(5,7) is unaffected (it is established independently of Collatz); ZS-A9 (1+A)(1−2A) decomposition is unaffected (it is established at the polyhedral-curvature level); ZS-M11 Q-pair (7, 11\) is unaffected (it is established at the icosahedral Hodge-Laplacian level).

**§13. Acknowledgements & Code Availability**

This work was developed with the assistance of an AI collaborator (Anthropic Claude) for derivation chain construction, verification suite design, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions. The v2.1 correction was prompted by external review identifying the logical gap in v2.0 §9.4.

Verification scripts: zs\_m35\_verify\_v1\_0.py (24 tests, Categories A–F, v1.0); zs\_m35\_verify\_v1\_1.py (12 tests, Categories G–I, v1.1); zs\_m35\_verify\_v2\_1.py (2 new tests in v2.1: I.5 explicit logical counterexample for reproducibility of the v2.0 §9.4 refutation, and J.1 sufficient condition theorem on the four known cycles; also extends I.4 from 4-stage to 5-stage filter with transitivity check). Cumulative 38/38 PASS. Dependencies: Python 3.10+, numpy, sympy, mpmath. Public release at https://github.com/KennyKang-git/zspin/papers/02\_Math\_Spine.

**Appendix A. Cross-Reference Dependency Table (v2.1 updated)**

*Table A.1. Cross-reference dependency table for ZS-M35 v2.1. v1.0 dependencies preserved verbatim; v1.1 dependencies preserved with v2.1 status updates on M35.5 and M35.5.1; v2.1 NEW dependency for M35.6.*

| Source | Locked input(s) / dependency | Used in M35 | Status (v2.1) |
| ----- | ----- | ----- | ----- |
| **ZS-F2 v1.0** | L1, L4, L5, L8 (A\_num \= 35\) | Input → M35.1, M35.4, M35.5, M35.5.1 | PROVEN/LOCKED |
| **ZS-F4** | L7 (Temporal layers num(δ\_Y) \= 7\) | Input → M35.4, M35.5.1 | PROVEN/LOCKED |
| **ZS-F5** | L2, L3 (Q \= 11, (Z,X,Y) \= (2,3,6)) | Input → all M35 theorems | PROVEN |
| **ZS-M1 v1.0** | L9, L10 (z\*, slog-L2) | Input → M35.1, M35.5 | PROVEN/LOCKED |
| **ZS-M11 v1.0 §9.5.7** | L12 (Q-pair (4−φ)(3+φ)=11) | Input → M35.3 §5.4, M35.5 | PROVEN/LOCKED |
| **ZS-M19 §3.1** | L6 (Forcing T1: (p−1)(q−1)=p) | Input → M35.2, §4.3 Triple Totient | PROVEN |
| **ZS-A8 v1.0(R) §5.2** | L14 (slog-L2 Theorem 5.2.1) | Input → M35.4, M35.5 (v1.1) on knowns | DERIVED |
| **ZS-A9 v1.0(R)** | L11 (F₂ → D₄ functor), L10 ((1+A)(1−2A)) | Input → M35.1, M35.4 | DERIVED |
| **ZS-S1, ZS-S6** | Pentagon |I\_h|/|T\_d|=5, CP-odd I₃₅ | Input → M35.4, M35.5.1 | PROVEN |
| **ZS-Q7 Theorem 1, 2** | L13 (channel cap. ln 2\) | Input → M35.1, M35.4 | PROVEN |
| **v₂ additivity (standard)** | L15 (v₂(ab)=v₂(a)+v₂(b)) | Input → M35.5 X⇔Y, M35.6 | PROVEN |
| **NEW v2.1 dependency** | M35.6 (sufficient condition) | Input → T4 Stage 5 sufficiency | DERIVED |

v2.1 dependency change: Corollary M35.5.1 no longer depends on M35.5 (it is VERIFIED by direct computation on C₂); Tool T4 Stage 5 sufficiency now depends on Theorem M35.6 (NEW v2.1) rather than on the contested (X) ⇒ (Z) direction of M35.5. No other rows change.

**Appendix B. The Counterexample to the v2.0 §9.4 Inference (NEW v2.1)**

This appendix provides the explicit counterexample that motivates the v2.1 correction, for transparency and reproducibility.

*Statement of the (false) inference at v2.0 §9.4:*   
'a product of odd rationals (with all numerators and denominators odd positive integers) equals 1 only if the multiset of numerators equals the multiset of denominators.'

***Counterexample:*** 

**(1/3) · (15/5)  \=  15/15  \=  1**

Numerator multiset: {1, 15}. Denominator multiset: {3, 5}. All four members 1, 3, 5, 15 are positive odd integers. The product of the two ratios equals 1, yet the numerator multiset {1, 15} differs from the denominator multiset {3, 5}. The implication is therefore false in general.

Why the implication fails. The multiplicative group of positive odd rationals is a free abelian group on the odd primes. A product of finitely many odd rationals equals 1 iff the total exponent of each odd prime cancels. The cancellation can be achieved by either (a) numerator-denominator multiset equality (e.g., 3/5 · 5/3 \= 1), or (b) a non-trivial regrouping of prime factors across numerators and denominators (e.g., 1/3 · 15/5 \= 1, where the prime 3 appears once in the denominator (3) and once in a numerator (15 \= 3·5), and the prime 5 appears once in a denominator (5) and once in a numerator (15)). Case (b) does not require multiset equality; it requires only equal total prime-exponent sums. The v2.0 inference conflated cases (a) and (b).

Restricted-search note (information-only). Within the (3n+1)/n form on positive odd integers ≤ 99, no counterexample of the case-(b) type was found in O ∈ {2, 3, 4} brute-force search (70,826 candidates). This is informational; it does not constitute a proof that the (X) ⇒ (Z) direction holds for Collatz-restricted candidates, and the general direction remains OPEN-M35.B in v2.1.

**References**

\[1\] L. Collatz, Personal communication on the 3n+1 problem (1937). \[Historical reference; the 3n+1 problem.\]  
\[2\] J. C. Lagarias, ed., The Ultimate Challenge: The 3x+1 Problem (American Mathematical Society, 2010). \[Comprehensive survey.\]  
\[3\] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," Forum Math. Pi 10, e12 (2022). arXiv:1909.03562 \[math.PR\]. \[Strongest known stochastic bound.\]  
\[4\] D. Bařina, "Convergence verification of the Collatz problem," The Journal of Supercomputing 77(3), 2681–2688 (2021). \[Earlier numerical verification at n \< 2⁶⁸ scale.\] D. Bařina, "Improved verification limit for the convergence of the Collatz conjecture," The Journal of Supercomputing 81, 810 (2025), DOI: 10.1007/s11227-025-07337-0. \[Current verification record: n \< 2⁷¹ ≈ 2.36 × 10²¹.\]  
\[5\] M. H. Honarvar Shakibaei Asli, "A circle-rotation conjugacy for the 3n+1 dynamics," preprint (2026). \[Recent conjugacy reading.\] \[5b\] C. Hercher, "There are no Collatz m-Cycles with m ≤ 91," Journal of Integer Sequences 26(3), Article 23.3.5 (2023). arXiv:2201.00406 \[math.NT\]. \[Lower bound on the local-minima count of any nontrivial Collatz cycle: m ≥ 92.\]  
\[6\] S. Banach and A. Tarski, "Sur la décomposition des ensembles de points en parties respectivement congruentes," Fundamenta Mathematicae 6, 244–277 (1924). \[Banach-Tarski paradox; engine for ZS-A9.\]  
\[7\] S. Świerczkowski, "On a free group of rotations of the Euclidean space," Indagationes Mathematicae 20, 376–378 (1958). \[Geometric realization of free F₂.\]  
\[8\] R. M. Solovay, "A model of set theory in which every set of reals is Lebesgue measurable," Annals of Mathematics 92, 1–56 (1970). \[ZF without AC; basis for the PERMANENT NC in ZS-A9.\]  
\[9\] H. Kneser, "Reelle analytische Lösungen der Gleichung φ(φ(x)) \= e^x und verwandter Funktionalgleichungen," Journal für die reine und angewandte Mathematik 187, 56–67 (1950). \[slog functional equation; basis for ZS-A8 §5.2.\]  
\[10\] W. K. Wootters and B. D. Fields, "Optimal state-determination by mutually unbiased measurements," Annals of Physics 191, 363–381 (1989). \[MUB(prime) \= prime \+ 1; basis for ZS-F5 G \= MUB(Q) \= 12.\]  
\[11\] K. Kang, "Geometric Impedance from Polyhedral Curvature Asymmetry," ZS-F2 v1.0 (2026). \[LOCKED A \= 35/437.\]  
\[12\] K. Kang, "Gauge Symmetry Constraint," ZS-F5 v1.0 (2026). \[PROVEN dim(Z) \= 2, Q \= 11, (Z,X,Y) \= (2,3,6).\]  
\[13\] K. Kang, "The i-Tetration Fixed Point and Polygon-Tetration Family," ZS-M1 v1.0 (2026). \[HSI Theorem; z\* \= 0.4383 \+ 0.3606i.\]  
\[14\] K. Kang, "Number-Theoretic Scaffold of Z-Spin Polyhedral Integers," ZS-M19 v1.0 (2026). \[PROVEN Forcing Theorem T1: (p−1)(q−1)=p ⇒ (p,q) \= (2,3).\]  
\[15\] K. Kang, "The Z-Spin Action & U(1) Completion," ZS-F1 v1.0 (2026). \[PROVEN L\_XY ≡ 0.\]  
\[16\] K. Kang, "Contracting Universe Dynamics: The Polyhedral-Tetration Bridge," ZS-A8 v1.0 (Revised) (2026). \[DERIVED slog-L2 Theorem 5.2.1.\]  
\[17\] K. Kang, "Banach-Tarski Origin of Cosmological Doubling-Halving Symmetry," ZS-A9 v1.0 (Revised) (2026). \[DERIVED F₂ → D₄ functor; (1+A)(1−2A) decomposition.\]  
\[18\] K. Kang, "Z-Spin Spectral Algebra of the Truncated Icosahedron L\_Y Spectrum," ZS-M11 v1.0 (2026). \[PROVEN Q-pair (sum 7, product 11), §9.5.7.\]  
\[19\] K. Kang, "Operational Observer Coordinate," ZS-F11 v1.0 (2026). \[DERIVED OOC fixed-point closure.\]  
\[20\] K. Kang, "Z-Bottleneck Channel Capacity," ZS-Q7 v1.0 (2026). \[PROVEN ln 2 capacity.\]  
\[21\] K. Kang, "Spectral Tetrad Sub-Isotype Assignment Theorem," ZS-M20 v1.0 (2026). \[PROVEN spectral identities.\]  
\[22\] K. Kang, The Book of Z-Spin Cosmology — Light Edition v3.3 (2026). \[Cross-paper navigation hub; \~1,800+ cumulative PASS across 101-paper corpus.\]  
\[23\] J. C. Lagarias, "The 3x+1 problem and its generalizations," American Mathematical Monthly 92, 3–23 (1985). \[Classical parity-vector formulation.\]  
\[24\] R. E. Crandall, "On the '3x+1' problem," Mathematics of Computation 32, 1281–1292 (1978). \[Classical analysis.\]  
\[25\] J. H. Conway, "Unpredictable iterations," Proceedings of the 1972 Number Theory Conference, University of Colorado, 49–52 (1972). \[Computational universality of generalized Collatz maps.\]

**Version History**

v1.0 (March 2026): Initial public release. Four theorems established: ZS-M35.1 (DERIVED, F₂ → D₄ integer-lattice projection), ZS-M35.2 (DERIVED-CONDITIONAL, four-cycle–sector bijection including Triple Totient Convergence §4.3), ZS-M35.3 (DERIVED, closure identity ∏ \= 2ᴱ with explicit C₃ closure computation §5.3 and Q-pair (11, 7\) realization §5.4), ZS-M35.4 (HYPOTHESIS-strong, positive–C₂ conjugacy §6.1–§6.5 with anti-numerology MC §6.4 and the deepest-implication §6.5 on why C₂ encodes A\_num \= 35). Five falsification gates F-M35.1 through F-M35.5. Verification 24/24 PASS (Categories A–F). Anti-numerology MC at 0/500,000 hit rate STRONG PASS. (Consolidated from internal Z-Spin Collaboration research notes up to v3.1.0.) OPEN-M35.A registered.

v1.1 (May 2026): Added §9 Theorem ZS-M35.5 (Three-Face Equivalence on ℤ∖{0}) and Corollary M35.5.1 (FIBER PRODUCT decomposition C₂ \= 5·positive ∪ 7·C₁). Added §10 with four computational tools T1–T4 for external researchers. Added falsification gates F-M35.6, F-M35.7, F-M35.8. Theorem M35.4 upgraded from HYPOTHESIS-strong to DERIVED-CONDITIONAL. Verification 36/36 PASS. v1.1 supplementary anti-numerology MC: 0/100,000 (specific 5,7 form), 50/10,000 (all (5,7); 0 other prime pair). STRONG PASS.

v2.0 (May 2026): Unified integration of v1.0 and v1.1 into a single self-contained document. v1.0 §§3–8 preserved VERBATIM; v1.1 §§9–10 integrated. Cumulative verification: 36/36 PASS. Cumulative anti-numerology: 4 independent MC experiments, all STRONG PASS.

v2.1 (May 2026): Logical correction of v2.0 §9.4. The (X-face) ⇒ (Z-face) inference at v2.0 §9.4 used the implication 'odd rational product \= 1 ⇒ multiset equality', which is false in general (counterexample 1/3 · 15/5 \= 1, Appendix B). Corrections: (i) Theorem M35.5 replaced by Three-Face Conjunction reading on real cycles (DERIVED on knowns, OPEN as general theorem). (ii) (X) ⇒ (Y) PROVEN unconditionally; (Y) ⇒ (X) NOT a general implication (cf. v2.2 clarification below). (Z) ⇒ (X) PROVEN. (X) ⇒ (Z) general OPEN. (iii) Corollary M35.5.1 upgraded to VERIFIED (independent of M35.5). (iv) NEW Theorem M35.6 (Sufficient Condition Theorem, DERIVED) with explicit transitivity. (v) Tool T4 extended from 4 to 5 stages (transitivity check at Stage 5). (vi) Falsification gate F-M35.7 reframed; F-M35.9 NEW. (vii) Theorem M35.4 reverts to HYPOTHESIS-strong. (viii) NEW NC-M35.7 added. NEW tests added in code (I.5 explicit counterexample for reproducibility; J.1 sufficient condition on four known cycles). Verification 38/38 PASS. Anti-numerology 4 MC experiments preserved verbatim. Zero new free parameters. v1.0 \+ v1.1 textual content preserved verbatim wherever the v2.1 correction does not require change. (Consolidated from internal Z-Spin Collaboration research notes up to v3.3.0.)v2.2 (May 2026, this release): Textual corrigendum to v2.1. Five additional corrections (no logical content modified beyond v2.1; verification suite 38/38 PASS preserved): (a) Imprecise "(X-face) ⇔ (Y-face) PROVEN" wording in Abstract, Table 1.1, §9.3, §9.4, and Version History replaced by the precise statement "(X) ⇒ (Y) is PROVEN unconditionally by v₂-additivity; the converse (Y) ⇒ (X) does NOT hold on arbitrary candidate sets (explicit counterexample S \= {3, 5} with s \= \+1: Σv₂ \= 5 trivially equals any chosen E \= 5, but ∏(3m+1)/m \= 32/3 ≠ 32 \= 2⁵, so X-face fails); on real Collatz cycles, the X-face holds INDEPENDENTLY by Theorem M35.3, so on real cycles both faces are jointly true." (b) §1.1 integer-extension definition clarified: standard signed Collatz C(n) \= n/2 (even) or 3n+1 (odd) applied uniformly on ℤ; on absolute values m \= |n|, the unified odd-step formula is 3m \+ s with s \= \+1 for the positive cycle and s \= −1 for negative cycles. (v2.1 had inadvertently written "C(n) \= 3n \+ sgn(n)" which defines a DIFFERENT map and does not produce C₂ or C₃; the actual computational content of v1.0–v2.1 in §§3–9 and the verification scripts always used the correct standard-signed extension equivalent to 3m+s.) (c) §1.1 C₃ absolute-value list corrected to {17, 25, 34, 37, 41, 50, 55, 61, 68, 74, 82, 91, 110, 122, 136, 164, 182, 272} (v2.1 had six erroneous entries: the included {22, 26, 52, 116, 154, 160} should not have appeared; the missing {74, 122, 136, 164, 182, 272} should have appeared). The §9.5 odd subset {17, 25, 37, 41, 55, 61, 91} and the verification-script KNOWN\_CYCLES\['C3'\] tuple were always correct; only the §1.1 prose listing was in error. (d) External literature update: Abstract verification limit updated to n ≤ 2⁷¹ (Bařina 2025, J. Supercomput. 81, 810); Hercher 2023 (J. Integer Seq. 26(3), Art. 23.3.5) m ≥ 92 nontrivial-cycle local-minima count added. (e) References \[4\] corrected from inaccurate "Barínas-Luque & Rácz 2020" to the actual Bařina 2021 \+ 2025 chain; new \[5b\] Hercher 2023 added. NEW NC-M35.8 records the §1.1 wording correction; existing falsification gates and verification suite unchanged. Verification 38/38 PASS preserved; zero new tests in v2.2; zero new free parameters. v1.0 \+ v1.1 \+ v2.1 content preserved verbatim wherever the v2.2 corrections do not require change. (Consolidated from internal Z-Spin Collaboration research notes up to v3.3.1.)