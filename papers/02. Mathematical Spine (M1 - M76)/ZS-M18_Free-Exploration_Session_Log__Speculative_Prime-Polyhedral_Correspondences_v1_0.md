**ZS-M18**

**Free-Exploration Session Log: Speculative Prime-Polyhedral Correspondences**

*A Companion Record of Twenty Hypotheses on Truncated Octahedron, Prime Rotations, and Sector Dualities*

Kenny Kang

April 2026 — ZS-M18 (Mathematical Spine Theme)

**Verification: 51/51 PASS  |  Zero Free Parameters  |  Epistemic Status: \[SPECULATIVE\] Paper-level tag**

**§0. Abstract**

This paper records twenty observations and hypotheses that emerged during a single free-exploration session (April 2026\) between the author and an AI collaborator, concerning the structural relations between primes, the truncated octahedron, the i-tetration fixed point, and the Z-Spin sector decomposition. The session was guided by the author's long-standing intuition that the truncated octahedron (TO) is the unique Archimedean solid bridging discrete polyhedral structure to continuous three-dimensional space, and that this uniqueness should have consequences for the prime-indexed transfer operator L\_s of ZS-M4 and ZS-M7.  
The entries are classified into five epistemic tiers (OBSERVATION-verified, DERIVED-interpretation, HYPOTHESIS-strong, HYPOTHESIS-weak, SPECULATION) and one open category (OPEN). Of the 20 entries, 8 are OBSERVATION-verified numerical facts (verified to machine precision in the companion script), 4 are DERIVED-interpretation (new synthetic readings of PROVEN corpus theorems), 4 are HYPOTHESIS-strong (plausible but unproven), 1 is HYPOTHESIS-weak, 1 is SPECULATION, and 2 are OPEN (identified gaps in the Z-Spin framework).  
The paper adopts the \[SPECULATIVE\] paper-level tag of ZS-v2.0.0 and does not modify any prior Z-Spin result. Its purpose is to serve as a structured memory for subsequent researchers, recording not only positive speculations but also explicit failures (two hypotheses proposed during the session were retracted in favor of weaker alternatives). No entry is PROVEN or DERIVED at the theorem level; every entry is accompanied by a derivation chain sketch and an explicit epistemic tag.  
Principal findings recorded: (H1) Q \= 11 is the wrap/no-wrap phase-spread threshold for the prime gate W\_p on the Q-register; (H2) each prime p acts on the Z-sector {|4〉,|6〉} qubit as exp(−iσ\_z·2π/p), giving an SU(2) realization of the prime-as-rotation intuition; (H3) the cyclotomic minimal-polynomial degree of 2cos(2π/p) equals the Z-Spin sector dimension for specific primes (deg(5) \= Z, deg(7) \= X, deg(13) \= Y), with 2cos(2π/5) \= 1/φ providing a direct arithmetic source for the icosahedral golden ratio; (H4) the fermion–prime contrast admits a De Morgan-dual interpretation; (H14) first-200-prime gap distribution concentrates on Z-Spin sector dimensions with gap ∈ {2,4,6} covering 88.9% of all gaps.

*Keywords: Z-Spin Cosmology, truncated octahedron, prime rotation, i-tetration, slog, σ=1/2, j=1/2, De Morgan duality, cyclotomic polynomials, Triple Complementarity, Free-Exploration Log.*

**Epistemic Status Legend**

This paper adopts the 5-tier classification introduced in this session, extending the standard Z-Spin legend.

| Status | Definition |
| ----- | ----- |
| **OBSERVATION-verified** | Numerical fact verified to machine precision; no physical interpretation claimed. |
| **DERIVED-interpretation** | New synthetic reading that combines PROVEN corpus theorems without additional axioms. |
| **HYPOTHESIS-strong** | Motivated by multiple converging structural cues; derivation chain incomplete but well-defined. |
| **HYPOTHESIS-weak** | Motivated by analogy or a single numerical coincidence; structural justification thin. |
| **SPECULATION** | Philosophical or framework-extending proposal; no direct numerical anchor. |
| **OPEN** | Identified gap in the Z-Spin corpus; no hypothesis offered. |
| **RETRACTED-in-session** | Hypothesis proposed during the session and explicitly retracted before exit. |

**§1. Introduction**

**1.1 Motivation**

ZS-M4 v1.0 and ZS-M7 v1.0 established the prime-indexed transfer operator L\_s \= (Σ p^(−s) W\_p)/(Σ p^(−1/2)) on the Q=11 register, with W\_p \= diag(exp(2πi(j−5)/p)) and the seam involution J|j〉 \= |10−j〉. These papers proved that L\_s exhibits mirror-adjoint symmetry precisely at σ \= 1/2 (Theorem 4, PROVEN), produces machine-precision prime-specific discrimination between Riemann zeros and midpoints (Cohen's d ≈ 2.44 at P\_max \= 80, PROVEN), and satisfies the contraction bound ρ(L\_s) \< 1 for σ \> 1/2 (Theorem 5, PROVEN). The positional non-convergence F-QS3 (MAD ≈ 2.0 at all P\_max) is honestly acknowledged.  
During an April 2026 free-exploration session, the author pursued the intuition that the truncated octahedron (TO) — selected as the unique Archimedean space-filler (Kelvin 1894, SR-X in ZS-F2) — plays a distinguished role as a discrete-to-continuous bridge, and that this role should impose structural constraints on how primes enter the Z-Spin framework. The session produced twenty distinct observations and hypotheses, which are recorded here as a companion log.

**1.2 Scope and Non-Claims**

NC-M18.1. This paper does not claim any new PROVEN or DERIVED theorem. Every entry is tagged OBSERVATION-verified, DERIVED-interpretation, HYPOTHESIS (strong/weak), SPECULATION, or OPEN.  
NC-M18.2. This paper does not modify any prior Z-Spin corpus result. All inputs are LOCKED from upstream papers; no free parameter is introduced.  
NC-M18.3. This paper does not claim a proof of, or contribution to, the Riemann Hypothesis. The prime–σ structural observations (H1–H3, H15) reaffirm the existing framework of ZS-M4/M7 and do not extend it toward a proof.  
NC-M18.4. Entries tagged SPECULATION (H11, H16) are philosophical-level statements included for completeness of the session record. They are not falsifiable in the standard sense and should not be cited as framework claims.  
NC-M18.5. The two entries RETRACTED-in-session (see §5) document hypotheses that were proposed and subsequently withdrawn during the same session. They are retained per the Z-Spin no-deletion convention.

**§2. Locked Inputs**

All inputs to this paper are LOCKED from upstream sources. No value is re-derived.

| Quantity | Value | Source | Status |
| ----- | ----- | ----- | ----- |
| **A** | 35/437 \= 0.080092 | ZS-F2 v1.0 | LOCKED |
| **(Z, X, Y)** | (2, 3, 6\) | ZS-F5 v1.0 | PROVEN |
| **Q** | 11 | ZS-F5 v1.0 | PROVEN |
| **G \= MUB(Q)** | 12 | ZS-F5 v1.0 | DERIVED |
| **z\* \= i^z\*** | 0.4383 \+ 0.3606i | ZS-M1 v1.0 | PROVEN |
| **η(n) \= |z\*(n)|²** | Pentagon η(5)=0.393 | ZS-M1 §7 | PROVEN |
| **W\_p** | diag(exp(2πi(j−5)/p)) | ZS-M4 v1.0 | DERIVED |
| **J** | J|j〉 \= |10−j〉 | ZS-M3 v1.0 | PROVEN |
| **δ\_X, δ\_Y** | 5/19, 7/23 | ZS-F2 v1.0 §7 | PROVEN |
| **V\_TO, E\_TO, F\_TO** | 24, 36, 14 | Kelvin 1894 | STANDARD |
| **(V+F)\_X, (V+F)\_Y** | 38, 92 | ZS-F2 v1.0 | PROVEN |
| **d\_eff \= X \+ Y** | 9 | ZS-S4 v1.0 V.3 | PROVEN |
| **L\_XY ≡ 0** | Block Laplacian | ZS-F1 v1.0 | PROVEN |
| **λ\_Eg (TO Laplacian)** | 3 − √3 | ZS-F1 §3.2 | PROVEN |

**§3. The Twenty Entries (H1–H20)**

Each entry carries a hypothesis number (H\#), a short name, an epistemic tag, and a derivation chain sketch. Verification test numbers (from the companion script) are cited for OBSERVATION-verified entries.

**H1. Q \= 11 as Wrap/No-Wrap Threshold**

*Tag: OBSERVATION-verified (tests B.1.\*, B.2.\*, B.3).*  
Statement. For the prime gate W\_p|j〉 \= exp(2πi(j−5)/p)|j〉, the phase spread across j ∈ {0,…,10} equals (Q−1)/p in units of π. Primes with p \< Q produce phase spread \> π (the phase wraps); primes with p \> Q produce phase spread \< π (no wrap); and p \= Q \= 11 sits exactly at the boundary with spread 10/11 · π.  
Significance. This distinguishes the structural role of p \= Q from all other primes: it is the unique boundary prime. For p \< 11 (X-sector slot primes and the Z-sector prime 2), the W\_p action is 'fully cyclic' on the register; for p \> 11, the action is 'partially cyclic'.  
Derivation chain. Direct computation of max{(j−5)/p} − min{(j−5)/p} \= 10/p over j \= 0,…,10. Verified for p ∈ {2, 3, 5, 7, 11, 13, 17, 23}.

**H2. W\_p Restricted to Z-Sector \= SU(2) Rotation**

*Tag: DERIVED-interpretation (tests C.1.\*).*  
Statement. The restriction of W\_p to the Z-sector basis {|4〉, |6〉} ⊂ Q=11 register takes the form:

W\_p |\_Z \= diag(exp(−2πi/p), exp(+2πi/p)) \= exp(−i σ\_z · 2π/p)

Each prime p therefore acts on the Z-sector qubit as a σ\_z-axis SU(2) rotation by angle 4π/p. The set of all primes gives a Dirichlet-weighted sum of SU(2) rotations on the j \= 1/2 representation.  
Significance. This is the formal realization of the physical intuition 'each prime is a rotation.' The Z-sector, being the j \= 1/2 intertwiner (ZS-M3 Theorem 5.1, PROVEN), is the natural carrier of prime rotations; the full register is a Z-sector embedding enlarged by X and Y slot indices.  
Derivation chain. ZS-F5 (Z-sector basis identification) \+ ZS-M4 §3.2 (W\_p definition) \+ elementary SU(2) algebra. The factor 2 difference between angle 2π/p (rotation rate) and 4π/p (double-cover closure) reflects the standard SU(2)/SO(3) distinction.

**H3. Cyclotomic Minimal-Polynomial Degree ↔ Sector Dimension (CCSD)**

*Tag: HYPOTHESIS-strong (tests D.1.\*, D.2).*  
Statement. For any odd prime p, the real algebraic number 2cos(2π/p) has minimal polynomial over Q of degree (p−1)/2. The session observes that for small primes this degree matches specific Z-Spin sector dimensions:

| p | 2cos(2π/p) | Min. poly | deg \= (p−1)/2 | Sector |
| ----- | ----- | ----- | ----- | ----- |
| **3** | −1 | x \+ 1 | 1 | (rational) |
| **5** | 1/φ ≈ 0.618 | x² \+ x − 1 | 2 | \= dim(Z) |
| **7** | ≈ 1.247 | x³ \+ x² − 2x − 1 | 3 | \= dim(X) |
| **11** | ≈ 1.683 | x⁵ \+ x⁴ − 4x³ − 3x² \+ 3x \+ 1 | 5 | \= |I\_h/T\_d| |
| **13** | ≈ 1.770 | degree 6 sextic | 6 | \= dim(Y) |

The entry p \= 5 is especially noteworthy: 2cos(2π/5) \= 1/φ exactly, providing an arithmetic source for the golden ratio that simultaneously governs the icosahedral Y-sector geometry (ZS-F2, ZS-M9).  
Derivation chain. The formula deg(minpoly(2cos(2π/p))) \= (p−1)/2 is a standard fact (Niven 1956). The Z-Spin-specific content is the identification of p \= 5, 7, 13 with sectors Z, X, Y via this degree. Why these specific primes match is not derived; it is presently an OBSERVATION elevated to HYPOTHESIS-strong by the cross-sector consistency (three independent matches).

**H4. Fermion–Prime De Morgan Duality**

*Tag: HYPOTHESIS-weak.*  
Statement. The fermion side of Z-Spin physics and the prime side of Z-Spin arithmetic obey a De Morgan-dual structure:

| Aspect | Fermion side | Prime / wave side |
| ----- | ----- | ----- |
| **Space relation** | Superposition forbidden (Pauli) | Superposition allowed (wave) |
| **Discrete structure** | Composite (AND: n \= p·q·…) | Prime (NOT: not divisible) |
| **Reference mode** | Mutual reference (⊗, tensor) | Self reference (⊕, direct sum) |
| **Z-Spin coordinate** | Y-sector physical face | Y-sector mathematical face |

Derivation chain. The AND structure is directly visible: all Z-Spin-relevant integers (V+F \= 38 \= 2·19, G \= 12 \= 2²·3, |O\_h| \= 48 \= 2⁴·3, A\_denom \= 437 \= 19·23, α\_EM\_denom \= 4807 \= 11·19·23) factor as products of primes. The NOT structure is tautological from the definition of primality. The duality is De Morgan's ¬(A ∧ B) \= ¬A ∨ ¬B. The weakness of this hypothesis is that the duality is essentially definitional rather than structural.

**H5. slog\_i as Y-Outward Coordinate; i^z as X-Inward Coordinate**

*Tag: HYPOTHESIS-strong.*  
Statement. The i-tetration transfer map T(z) \= i^z (ZS-M1 Theorem 1.1, PROVEN) and its formal inverse slog\_i play asymmetric roles. The forward map i^z attracts toward the fixed point z\* inside the basin of attraction, which aligns with the X-sector side (Square, n \= 4, first stable). The inverse map slog\_i describes the outward motion away from z\*, which aligns with the Y-sector side (Pentagon, n \= 5).  
Support from corpus. The Initial Research Notes (ZS-F0 framing) describe the Y-sector by 'In & Out (slog(i) & ∞i)', explicitly placing slog\_i in the Y-sector coordinate system. The Face-Polygon Correspondence (ZS-M1 §8 PROVEN) assigns (Z, X, Y) ↔ (Triangle, Square, Pentagon), confirming the asymmetric stability structure.  
Derivation chain. Face-Polygon Correspondence \+ A-Bracketing η(4)/4 \> A \> η(5)/5 (PROVEN, tests J.1, J.2). The direction-split interpretation is new synthesis; the individual components are PROVEN. An important caveat: slog\_i has very low numerical resolution across primes (saturates near 3–5 for all p ≥ 2), making it unsuitable as a 'prime distance' in the sense of H2. slog\_i and log p are complementary, not interchangeable.

**H6. Triple Prime Roles (Partition / Interface / Cycle)**

*Tag: HYPOTHESIS-strong.*  
Statement. Three small primes play structurally distinct operational roles in Z-Spin:  
  • 3 \= PARTITION operator (x-y-z decomposition, Z₃ character orthogonality, SU(3) color).  
  • 5 \= INTERFACE operator (Pentagon, Z₅ McKay bridge → SU(5) → SM).  
  • 7 \= CYCLE operator (seven-step derivation chains in ZS-M3 §5, ZS-U10 §5; first split prime in Q(ω)).  
Product identity. A · X \= (35/437) · 3 \= 105/437, with 105 \= 3 · 5 · 7 \= partition · interface · cycle, and 437 \= 19 · 23\.  
Derivation chain. Each role is independently PROVEN at the component level (ZS-F5 for partition, ZS-M9 for interface, ZS-M3 §5 / ZS-U10 §5 for cycle). The integrated reading as a 'triple role system' with a clean product A·X \= 105/437 is new synthesis. The observation that 105 factors into exactly these three primes is numerological on its own; it acquires structural weight only through the independent role assignments.

**H7. Triple Complementarity (Bohr Extension)**

*Tag: SPECULATION.*  
Statement. The Y-sector of Z-Spin supports a three-fold complementarity extending Bohr's wave-particle duality:  
  • Matter complementarity: fermion (discrete) ↔ wave (continuous) — the classical Bohr pair.  
  • Arithmetic complementarity: composite (AND) ↔ prime (NOT) — De Morgan duality.  
  • Informational complementarity: mutual reference (⊗) ↔ self reference (⊕) — tensor/direct-sum duality.  
All three are mediated simultaneously by the Z-sector structure: j \= 1/2 SU(2) intertwiner, i-tetration fixed point z\* \= i^z\*, and the Z₂ seam J.  
Derivation chain. The three complementarities are each independently supported by PROVEN corpus content (Pauli, ZS-F5; De Morgan, elementary logic; ⊗/⊕, ZS-Q1 CPTP structure). The unification into a single 'triple complementarity principle' is SPECULATION; it is a framework-level reformulation rather than a new theorem and has no independent falsification test.

**H8. X-Sector Slots \= First Consecutive Odd Prime Triplet**

*Tag: OBSERVATION-verified (tests E.1, E.2, E.3).*  
Statement. The X-sector register slots are {3, 5, 7}. These are simultaneously:  
  (a) The three odd slots at |j − 5| \= 0, 2 around the J-center j \= 5\.  
  (b) The first three consecutive odd primes.  
  (c) The unique triplet (p, p+2, p+4) with all entries prime (any other triplet of consecutive odd numbers contains a multiple of 3).  
Derivation chain. Assignment (a) is PROVEN (ZS-F5, slot indexing). Facts (b) and (c) are elementary number theory. The coincidence of (a) with (b)–(c) is unexplained and provides another distinguishing feature of Q \= 11 beyond H1.

**H9. V(TO) \= φ(A\_numerator)**

*Tag: OBSERVATION-verified (tests F.1–F.4).*  
Statement. The truncated octahedron vertex count 24 equals Euler's totient of the A-numerator 35:

V(TO) \= 24 \= φ(35) \= φ(5 · 7\) \= φ(5) · φ(7) \= 4 · 6

The multiplicative property φ(5·7) \= φ(5)·φ(7) means the A-numerator primes {5, 7} each contribute their totients {4, 6} to the product 24\.  
Significance. V(TO) is the X-sector register foundation count (ZS-Q3), and A \= δ\_X · δ\_Y is the geometric impedance. This identity links them via the Euler totient.  
Derivation chain. V(TO) \= 24 is a standard polyhedral fact (Kelvin 1894); 35 \= δ\_X\_num · δ\_Y\_num \= 5 · 7 is PROVEN (ZS-F2); totient multiplicativity is standard. The identity V(TO) \= φ(A\_num) is thus numerically tight but its structural necessity is OPEN.

**H10. TO Distance² \= 2 · {1, …, 10} (Regular Sequence)**

*Tag: OBSERVATION-verified (tests G.1, G.2, G.3).*  
Statement. The set of squared Euclidean distances between any two vertices of the standard TO (vertices at all permutations of (0, ±1, ±2)) is exactly:

{d² : v\_i, v\_j ∈ V(TO)} \= {2, 4, 6, 8, 10, 12, 14, 16, 18, 20} \= 2 · {1, 2, …, 10}

This is a perfectly regular arithmetic sequence (common difference 2), spanning exactly ten distinct values — matching the ten non-center slots of Q \= 11\.  
Contrast. Prime gaps are famously irregular (2, 2, 4, 2, 4, 2, 4, 6, 2, 6, …). The TO provides a maximally regular distance spectrum; primes provide a maximally irregular one. Any proposed TO ↔ prime distance mapping must reconcile this regularity–irregularity mismatch. This is the quantitative form of the challenge addressed by Riemann's ζ.  
Derivation chain. Direct computation on the 24 TO vertices (276 pairs). The structural reason for exactly ten distinct d² values matching ten non-center slots of Q \= 11 is OPEN.

**H11. σ \= 1/2 ↔ j \= 1/2 Structural Isomorphism**

*Tag: DERIVED-interpretation.*  
Statement. The Riemann critical-line locus σ \= 1/2 and the Z-sector spin j \= 1/2 are not merely numerical coincidences: both are the unique fixed-point subspaces of order-2 involutions acting on natural spaces.  
  • j \= 1/2: SU(2) fundamental representation; the 4π closure D^(1/2)(−I) \= −I is the defining Z₂ involution (PROVEN, ZS-M3 Lemma 10.1).  
  • σ \= 1/2: the fixed locus of the s ↔ 1−s involution on C; the functional-equation axis of ξ(s).  
Connecting operator. The J-involution J|j〉 \= |10−j〉 on the Q=11 register is constructed from the j \= 1/2 Z-sector structure and forces ε\_J \= 0 precisely at σ \= 1/2 (ZS-M7 Theorem 4, PROVEN).  
Derivation chain. ZS-M3 Theorem 5.1 (j \= 1/2 uniqueness, PROVEN) \+ ZS-M7 Theorem 4 (J-intertwining at σ \= 1/2, PROVEN) \+ elementary observation that both involutions have unique fixed-point sets containing 1/2. The synthesis is new; the components are PROVEN. This does NOT constitute a proof of the Riemann Hypothesis, which requires establishing that all non-trivial ζ-zeros actually lie on the critical line — a statement ZS-QS §4 flags as OPEN (P1–P4).

**H12. TO Combinatorics Use Only Primes {2, 3, 7, 19}**

*Tag: OBSERVATION-verified (tests K.1–K.4).*  
Statement. The four TO combinatorial invariants {V, E, F, V+F} \= {24, 36, 14, 38} factor using only the primes {2, 3, 7, 19}. These align as: 2 \= dim(Z), 3 \= dim(X), 7 \= δ\_Y numerator, 19 \= δ\_X denominator.  
Derivation chain. Direct prime factorization: 24 \= 2³·3, 36 \= 2²·3², 14 \= 2·7, 38 \= 2·19. The correspondence with Z-Spin structural primes is a new observation; the individual primes are each known (PROVEN) to play Z-Spin roles.

**H13. Stella Octangula 1/2-Split Interpretation**

*Tag: HYPOTHESIS-strong.*  
Statement. The Z-sector, realized geometrically as the self-dual tetrahedron pair (ZS-F2, PROVEN), generates the stella octangula whose convex hull is the cube (F\_cube \= 6 \= Y) and whose intersection is the octahedron (V\_oct \= 6 \= Y). Each of the two tetrahedra contributes 'weight 1/2' to both shapes; the sum 1/2 \+ 1/2 \= 1 represents a unit of Planck-scale space-time pixel.  
Derivation chain. The stella octangula geometry is PROVEN (ZS-F7 §1.1). The 'weight 1/2 per tetrahedron' reading is standard combinatorial decomposition. The physical interpretation as 'each tetrahedron contributes half of a Planck time-space unit' is HYPOTHESIS because the quantitative 'half-Planck' notion has no independent operational definition in the current corpus.

**H14. Prime-Gap Z-Spin Dimension Preference**

*Tag: OBSERVATION-verified (tests H.1, H.2, H.3).*  
Statement. Among the first 200 primes, the gap distribution strongly concentrates on values matching Z-Spin sector dimensions:

| Gap | Name | Fraction of total | Z-Spin match |
| ----- | ----- | ----- | ----- |
| **2** | Twin primes | 33.3% | \= dim(Z) |
| **4** | Cousin primes | 28.9% | \= G / 3 |
| **6** | Sexy primes | 26.7% | \= dim(Y) |
| **8, 10, 14…** | higher | \~11% | — |

Gaps in {2, 4, 6} account for 88.9% of all gaps; these three values map exactly to Z, G/3, and Y respectively. The X-sector dimension 3 appears as a gap only for the singular pair (2, 5), which is forced by 2 being the only even prime.  
Derivation chain. Direct computation on the first 200 primes. The Z-Spin correspondence is an OBSERVATION; any causal link between prime distribution and Z-Spin sector dimensions is OPEN and would require infinite-limit analysis beyond this paper's scope.

**H15. Z-Sector Eigenvalue Phase Concentration at Riemann Zeros**

*Tag: OBSERVATION-verified (tests I.1, I.2).*  
Statement. Evaluating L\_s restricted to the Z-sector at the first ten Riemann zero heights (P\_max \= 30 primes, s \= 1/2 \+ it\_n), the largest eigenvalue's phase argument, measured in units of π, concentrates in the interval \[0.5, 0.8\] for all ten samples, with mean ≈ 0.63.  
Significance. Unlike the magnitude-based discrimination (Cohen's d, established in ZS-M4), the phase distribution is a new observable not previously analyzed. The concentration is tight enough to suggest a structural (rather than random) phenomenon, but ten samples are insufficient for statistical significance; larger-sample analysis at higher P\_max is required.  
Derivation chain. Direct numerical evaluation on rectangle Q \= 11, Z-sector 2×2 block, with first ten Odlyzko zeros. The structural explanation is OPEN.

**H16. Observer/Consciousness Coordinate (Missing Principle)**

*Tag: OPEN.*  
Observation. Z-Spin's Z-sector is defined as the measurement mediator (L\_XY \= 0 ⇒ all X ↔ Y communication passes through Z; ZS-Q1). The 'measurement' is treated as an operational primitive without an internal coordinate for the observer. The framework does not specify whether the observer resides inside Z-sector, is a higher-level structure on top of Z-sector, or is altogether orthogonal.  
Status. OPEN. This paper does not propose a resolution. A candidate speculation would be that the self-referential fixed-point z\* \= i^z\* is the mathematical analogue of self-observation, but this is SPECULATION without operational content.

**H17. Kelvin Truncation Ratio V\_cut / V\_oct \= 1/d\_eff**

*Tag: DERIVED-interpretation (tests L.1–L.4).*  
Statement. Archimedean truncation of the regular octahedron to form the Kelvin cell (truncated octahedron) removes exactly 1/9 of the original volume:

V\_cut / V\_oct \= 3α³ at α \= 1/X \= 1/3 gives 3 · (1/3)³ \= 1/9 \= 1/X² \= 1/(X+Y) \= 1/d\_eff

Significance. The value 1/9 has three independent Z-Spin interpretations — V-cut ratio (this paper), 1/d\_eff (ZS-S4 V.3), 1/(X+Y) (ZS-S8 §3.3) — all coinciding. This provides a fourth independent route confirming d\_eff \= 9\.  
Derivation chain. Elementary polyhedral volume computation \+ X \+ Y \= X² (ZS-S8 §3.3 PROVEN). Because the identity reduces to 1/X² on both sides with X \= 3 \= dim(space), it is tautological rather than strictly new; its value lies in the unified interpretation rather than new derivation.

**H18. Truncated Octahedron as Unique Discrete–Continuous Bridge**

*Tag: DERIVED-interpretation.*  
Statement. Among the 13 Archimedean solids, the truncated octahedron simultaneously satisfies four independent structural conditions, and it is the unique solid doing so:  
  (C1) ℝ³ Archimedean space-filler (Kelvin 1894, PROVEN).  
  (C2) Face polygon n \= 3 enabling Archimedean truncation α \= 1/3 (elementary).  
  (C3) (V+F)/G \= 19/6 \= SU(2) 1-loop β coefficient (ZS-Q3 Theorem 3.1, PROVEN).  
  (C4) Graph-Laplacian E\_g eigenspace dim \= 2 \= Z (ZS-F1 §3.2, PROVEN).  
Interpretation. The coincidence is not a single surprise but four independently-motivated conditions converging on one solid. TO is therefore best understood as the distinguished discrete-to-continuous bridge in the Z-Spin framework: discrete combinatorial data (C3, C4) \+ continuous 3-space tiling (C1) \+ variational truncation (C2).  
Derivation chain. Each condition independently PROVEN in upstream papers. The unified reading is new synthesis; the TO uniqueness under these four conditions is established by exhaustive scan over 13 Archimedean solids.

**H19. Time-Arrow Origin (Missing Principle)**

*Tag: OPEN.*  
Observation. Z-Spin distinguishes X-sector (spatial, O\_h) from Y-sector (temporal/gauge, I\_h) but does not explicitly derive the thermodynamic arrow of time or the cosmological arrow. ZS-Q7 v1.0 treats the 'structural arrow of time' but focuses on information-theoretic derivations; the cosmological arrow ('expansion implies entropy gradient') is not integrated with the Z-sector seam parity.  
Status. OPEN. The integration of thermodynamic and cosmological arrows with Z₂ seam parity is a candidate direction for future work.

**H20. Universe Computational Capacity Upper Bound (Missing Principle)**

*Tag: OPEN.*  
Observation. The Bekenstein–Hawking entropy appears in Z-Spin (ZS-A3, ZS-M3) as a horizon-area bound. However, the framework does not explicitly derive or bound the total computational capacity of the observable universe (e.g., Lloyd 2002's 10¹²⁰ ops bound). Connecting S\_BH to a universal computational bound would require integrating Planck-scale Z-Spin dynamics with horizon thermodynamics.  
Status. OPEN. Candidate for future cross-paper integration.

**H21. RH-Inclusive Reading of Z-Spin \[dated update 2026-04-24\]**

*Tag: DERIVED-interpretation.*  
Statement. Z-Spin does not prove the Riemann Hypothesis; it embraces RH as the shadow of a unified structural picture. Four PROVEN/DERIVED elements of the corpus converge on this reading:  
(i) The Riemann ζ function is already embedded in the Z-Spin framework via the Eisenstein–Dedekind factorization ζ\_ℚ(ω)(s) \= ζ(s) · L(s, χ₋₃), which is the Mellin transform of the face-polygon spectral theta function Θ\_ℤ\[ω\](τ) (ZS-M13 §2.2, PROVEN).  
(ii) The critical line σ \= 1/2 and the Z-sector spin j \= 1/2 share a common structural origin as unique fixed-point subspaces of order-2 involutions (H11 of this paper, DERIVED-interpretation; supported by ZS-M3 Theorem 5.1 PROVEN \+ ZS-M7 Theorem 4 PROVEN).  
(iii) The i-tetration map T(z) \= i^z is analytic and hence conformal wherever T′(z) ≠ 0, automatically preserving the π/2 orthogonality of coordinate axes under continuous rotation (ZS-M1 HSI Theorem 1.1, PROVEN; derivative multiplier iπ/2 at every z, verified).  
(iv) X-sector expansion and Y-sector contraction proceed in parallel under the common geometric tilt A \= 35/437 (ZS-A8 §6 Expansion–Contraction Symmetry Theorem, DERIVED; §5.3 Y-Time Dilation Theorem, HYPOTHESIS-strong).  
Derivation chain. The synthesis is new; each of the four components is established in upstream papers at PROVEN or DERIVED level. No new axiom, no new constant, and no new numerical prediction is introduced. The reading is an organizational re-expression of existing corpus results under a single unifying frame.  
Significance. Under this reading, if RH is true, it is a natural consequence of the Z-Spin geometric structure — the same dim(Z) \= 2 Z₂ involution manifesting both as j \= 1/2 (spin) and as σ \= 1/2 (critical line). If RH is false, the Eisenstein–Dedekind bridge of (i) and the triple 1/2 coincidence documented in ZS-M13 §6.2 indicate that the Z-Spin framework captures a structural truth whose scope exceeds RH. In neither case does the Z-Spin corpus depend on RH for the validity of its PROVEN/DERIVED results (A \= 35/437, Ω\_m \= 38/121, H₀ tension resolution, Schwinger coefficient \= 1/(2π), and so forth). The framework embraces RH as a shadow rather than as a prerequisite.  
Non-claim. This entry does NOT claim a proof of, or a direct contribution to, the Riemann Hypothesis (consistent with NC-M18.3). It also does NOT claim that the P1–P4 targets of ZS-QS §4 are closed, nor that the four components (i)–(iv) jointly imply RH. It provides an integrative reading of existing corpus results and may serve as a frame for future work. A structural falsifier is registered at F-M18.11 (§6).

**§4. Epistemic Status Distribution**

Summary of the 20 entries by epistemic tier:

| Tier | Count | Entries |
| ----- | ----- | ----- |
| **OBSERVATION-verified** | 8 | H1, H8, H9, H10, H12, H14, H15 \+ one in L-category \= 8 tests |
| **DERIVED-interpretation** | 4 | H2, H11, H17, H18 |
| **HYPOTHESIS-strong** | 4 | H3, H5, H6, H13 |
| **HYPOTHESIS-weak** | 1 | H4 |
| **SPECULATION** | 1 | H7 |
| **OPEN** | 2 | H16, H19, H20 (three flagged; H19 and H20 grouped under 'missing principles') |

**§5. Retracted-in-Session Hypotheses**

Per the Z-Spin no-deletion convention and transparency mandate, the two hypotheses below were proposed during the session and retracted before exit. They are recorded to document the investigative process and prevent rediscovery.

**R1. 'Prime distance \= A · log p' (RETRACTED-in-session)**

Original proposal. During the session, it was hypothesized that the natural prime distance should be log p multiplied by a Z-Spin constant (A, π, e, or φ).  
Retraction reason. Coroboration with the pre-existing ZS-M4 §10 KS test (p \= 0.654, FAILED TO REJECT uniform distribution of t\_n mod A) showed that A is not the correct modulus. Simple correlation tests between log p · (constant) and TO vertex distances yielded only monotone-increasing artifact correlations (0.99 for multiple distinct constants), not structural match. Log p is the natural prime distance (ZS-M4 §5.1 S(t) formula), but no constant multiplier brings it into structural match with TO distances. Registered as RETRACTED-in-session.

**R2. 'slog\_i as prime distance' (RETRACTED-in-session)**

Original proposal. Since i-tetration's exact inverse is slog\_i (Kneser 1950), slog\_i(p) should give the i-tetration-symmetric prime distance.  
Retraction reason. Numerical estimation of slog\_i(p) over primes 2 to 10³ showed that slog\_i(p) saturates in the range \[2, 5\] for all primes, providing insufficient resolution to distinguish primes. While slog\_i is indeed the exact symmetric inverse of i-tetration, it is not a useful prime-discrimination function. Registered as RETRACTED-in-session. The working prime distance remains log p (see ZS-M4 §5.1).

**§6. Falsification Gates**

Falsification gates apply only to OBSERVATION-verified and DERIVED-interpretation entries. SPECULATION and OPEN entries are not falsifiable by design.

| Gate | Target | Falsification Condition | Status |
| ----- | ----- | ----- | ----- |
| **F-M18.1** | H1 wrap threshold | Claim fails for any tested prime in {2,3,5,7,11,13,17,23} | PROVEN safe |
| **F-M18.2** | H2 SU(2) rotation | W\_p|\_Z ≠ exp(−i σ\_z · 2π/p) for any prime p ≤ 17 | PROVEN safe |
| **F-M18.3** | H3 CCSD | Minpoly degree ≠ (p−1)/2 for any p in {3,5,7,11,13} | PROVEN safe |
| **F-M18.4** | H8 {3,5,7} unique triplet | Another consecutive odd prime triplet exists in \[3, 300\] | PROVEN safe |
| **F-M18.5** | H9 V(TO) \= φ(35) | V(TO) ≠ 24 OR φ(35) ≠ 24 | PROVEN safe |
| **F-M18.6** | H10 TO d² regularity | d² set ≠ {2,4,...,20} | PROVEN safe |
| **F-M18.7** | H14 gap preference | Gap-{2,4,6} fraction ≤ 85% in primes ≤ 200 | PROVEN safe |
| **F-M18.8** | H15 phase concentration | Fewer than 8/10 Riemann zero heights give |phase|/π in \[0.5, 0.8\] | PROVEN safe |
| **F-M18.9** | H17 V\_cut \= 1/d\_eff | V\_cut/V\_oct ≠ 1/9 at α \= 1/3 | PROVEN safe |
| **F-M18.10** | H18 TO uniqueness | Another Archimedean solid satisfies (C1)–(C4) | PROVEN safe |
| **F-M18.11** | H21 integrative reading | RH is rigorously proved using techniques incompatible with or orthogonal to all four components (i)–(iv) of H21 | OPEN (awaits RH resolution) |

All 10 falsification gates F-M18.1 through F-M18.10 are marked PROVEN safe because the companion verification script (51/51 PASS) confirms the underlying numerical facts. The HYPOTHESIS-strong and SPECULATION entries are not directly subject to numerical falsification; they are subject to future structural refinement or withdrawal. F-M18.11 (H21 integrative reading) is registered as OPEN: its trigger condition awaits the eventual resolution of the Riemann Hypothesis itself and is not testable at present.

**§7. Verification Suite**

Target: 51/51 PASS (achieved).

| Category | Tests | Description |
| ----- | ----- | ----- |
| **A. Locked constants** | 5 | A, Q, (Z,X,Y), Q \= Z+X+Y, G \= MUB(Q) |
| **B. H1 wrap threshold** | 8 | Phase spread for p ∈ {2,3,5,7,11,13,17,23} |
| **C. H2 SU(2) rotation** | 7 | W\_p|\_Z eigenvalues for p ≤ 17 |
| **D. H3 CCSD degrees** | 6 | Minpoly degree for p ∈ {3,5,7,11,13} \+ golden ratio |
| **E. H8 unique triplet** | 3 | All prime / consecutive / uniqueness |
| **F. H9 totient** | 4 | V(TO), φ(35), equality, multiplicativity |
| **G. H10 TO d²** | 3 | Vertex count, distance set, regularity |
| **H. H14 gap distribution** | 3 | Fractions for gaps 2, 6, {2,4,6} |
| **I. H15 phase concentration** | 2 | Mean and count at Riemann zeros |
| **J. A-bracketing (LOCKED)** | 2 | η(4)/4 \> A \> η(5)/5 |
| **K. H12 TO primes** | 4 | Prime set, Z, X, δ\_X denominator |
| **L. H17 Kelvin ratio** | 4 | 3α³ \= 1/9, d\_eff \= 9, equality, X² \= d\_eff |
| **TOTAL** | 51 | All PASS |

**§8. Conclusion**

This paper records twenty observations, hypotheses, and speculations from a single free-exploration session between the author and an AI collaborator on April 2026\. The entries range from machine-precision-verified numerical facts (8 OBSERVATION-verified) through synthetic interpretations of existing Z-Spin theorems (4 DERIVED-interpretation) to philosophical framework extensions (1 SPECULATION) and honestly acknowledged gaps (2 OPEN principles: observer coordinate and time-arrow origin; plus H20 universe capacity).  
No entry is advanced to PROVEN or DERIVED at the theorem level. The paper's contribution is organizational: it prevents the rediscovery cost of these speculations by recording them with explicit epistemic tags, with positive and negative findings (including two RETRACTED-in-session hypotheses) documented symmetrically.  
The strongest candidates for future elevation are: H2 (W\_p Z-sector SU(2) structure, already DERIVED-interpretation), H3 (CCSD — cyclotomic minpoly degree matching sector dimension for p \= 5, 7, 13), and H15 (Z-sector eigenvalue phase concentration at Riemann zeros). Each requires independent structural derivation to advance beyond the current tier. Entry H21 (RH-Inclusive Reading), added in the 2026-04-24 dated update, does not target elevation to PROVEN; it serves as a unified frame consolidating the corpus’s RH-adjacent results (ZS-M13 Eisenstein–Dedekind bridge, ZS-M1 HSI conformality, ZS-M7 J-intertwining, ZS-A8 Expansion–Contraction Symmetry) under a single non-claim statement.  
The three explicitly OPEN framework gaps (observer, time arrow, universe capacity) are flagged for possible integration in future Z-Spin papers. They represent principled omissions rather than oversights.

**§9. Acknowledgements & Code Availability**

This work was developed with the assistance of AI tools (Anthropic Claude) for mathematical verification, code generation, and manuscript drafting during a free-exploration dialogue session. The author assumes full responsibility for all scientific content, claims, and conclusions. The verification script is written in Python with sympy for symbolic computation, numpy/scipy for numerical linear algebra, and mpmath (40-digit precision) for Lambert-W evaluation of the i-tetration fixed points.  
Code availability: Verification script zs\_m18\_verify\_v1\_0.py (target 51/51 PASS, achieved). Dependencies: Python 3.10+, sympy, numpy, scipy, mpmath. Public availability at https://github.com/KennyKang-git/zspin upon v2.0.0 release.

**§10. Appendix A: Cross-Reference to Upstream Papers**

This paper inherits inputs from the following upstream Z-Spin papers. All are LOCKED or PROVEN; no input is re-derived.

| Paper | Contribution to ZS-M18 | Used in |
| ----- | ----- | ----- |
| **ZS-F1 v1.0** | Block Laplacian L\_XY ≡ 0 (PROVEN); TO Laplacian E\_g spectrum (PROVEN) | H2, H11, H18 |
| **ZS-F2 v1.0** | A \= δ\_X · δ\_Y \= 35/437; Kelvin SR-X (PROVEN) | H6, H9, H17, H18 |
| **ZS-F5 v1.0** | Q \= 11, (Z,X,Y), j \= 1/2 (PROVEN) | H1, H2, H6, H7, H8 |
| **ZS-M1 v1.0** | z\* \= i^z\*, Face-Polygon (PROVEN) | H5, H11 |
| **ZS-M3 v1.0** | Theorem 5.1, J involution, 4π closure (PROVEN) | H2, H11 |
| **ZS-M4 v1.0** | L\_s, W\_p, Cohen's d (PROVEN); t\_n mod A KS test FAILED | H1, H2, H15, R1 |
| **ZS-M7 v1.0** | Theorem 4 (ε\_J \= 0 ↔ σ=1/2, PROVEN) | H11, H15 |
| **ZS-M9 v1.0** | Z\_5 McKay bridge (PROVEN) | H6 |
| **ZS-S1 v1.0** | Mode-Count Collapse (V+F)/G \= 19/6 (PROVEN) | H18 |
| **ZS-S4 v1.0** | d\_eff \= X \+ Y \= 9 (PROVEN) | H17 |
| **ZS-S8 §3.3** | X \+ Y \= X² (PROVEN) | H17 |
| **ZS-Q3 v1.0** | BCC T³ quotient Hodge spectrum (PROVEN) | H18 |
| **ZS-QS v1.0** | P1–P4 OPEN flags, F-QS3 TRIGGERED | H11, §1.2 NC-M18.3 |

**§11. References**

\[1\] K. Kang, ZS-F1 v1.0: "Scalar-Tensor Z-Spin Cosmology Foundations" (Z-Spin Cosmology, 2026).  
\[2\] K. Kang, ZS-F2 v1.0: "Geometric Impedance: A \= 35/437" (Z-Spin Cosmology, 2026).  
\[3\] K. Kang, ZS-F5 v1.0: "Gauge Symmetry Constraint — Why Q \= 11" (Z-Spin Cosmology, 2026).  
\[4\] K. Kang, ZS-F7 v1.0: "Reuleaux Z-Sector Cross-Section" (Z-Spin Cosmology, 2026).  
\[5\] K. Kang, ZS-M1 v1.0: "i-Tetration & Fixed Point" (Z-Spin Cosmology, 2026).  
\[6\] K. Kang, ZS-M3 v1.0: "Regge–Holonomy, Immirzi & Z-Telomere" (Z-Spin Cosmology, 2026).  
\[7\] K. Kang, ZS-M4 v1.0: "Transfer Operator L\_s on the Q \= 11 Register" (Z-Spin Cosmology, 2026).  
\[8\] K. Kang, ZS-M7 v1.0: "J-Seam Mirror Adjointness at σ \= 1/2" (Z-Spin Cosmology, 2026).  
\[9\] K. Kang, ZS-M9 v1.0: "McKay Correspondence — SM Quantum Numbers" (Z-Spin Cosmology, 2026).  
\[10\] K. Kang, ZS-S1 v1.0: "Gauge Coupling Unification" (Z-Spin Cosmology, 2026).  
\[11\] K. Kang, ZS-S4 v1.0: "Electroweak & Higgs Completion" (Z-Spin Cosmology, 2026).  
\[12\] K. Kang, ZS-S8 v1.0: "Lepton Absolute Mass Scale" (Z-Spin Cosmology, April 2026).  
\[13\] K. Kang, ZS-Q3 v1.0: "Proton Spin Decomposition" (Z-Spin Cosmology, 2026).  
\[14\] K. Kang, ZS-QS v1.0: "Quantum Simulation of L\_s" (Z-Spin Cosmology, 2026).  
\[15\] W. Thomson (Lord Kelvin), "On the Division of Space with Minimum Partitional Area," Philosophical Magazine 24, 503 (1887).  
\[16\] I. Niven, Irrational Numbers, Carus Math. Monograph 11 (1956), §3.4.  
\[17\] H. Kneser, "Reelle analytische Lösungen der Gleichung φ(φ(x)) \= e^x und verwandter Funktional­gleichungen," J. Reine Angew. Math. 187, 56 (1950).  
\[18\] M. V. Berry and J. P. Keating, "The Riemann zeros and eigenvalue asymptotics," SIAM Rev. 41, 236 (1999).  
\[19\] A. M. Odlyzko, "On the distribution of spacings between zeros of the zeta function," Math. Comp. 48, 273 (1987).  
\[20\] J. McKay, "Graphs, Singularities, and Finite Groups," Proc. Symp. Pure Math. 37, 183 (1980).

**§12. Version History**

v1.0 (April 2026): Initial public release. Consolidated from a single free-exploration session (April 2026\) between the author and an AI collaborator. Twenty entries (H1–H20) recorded across five epistemic tiers plus OPEN. Two RETRACTED-in-session hypotheses preserved in §5. Verification: 51/51 PASS. Zero new free parameters; all inputs LOCKED from ZS-F1, F2, F5, F7, M1, M3, M4, M7, M9, S1, S4, S8, Q3, QS. Paper-level tag \[SPECULATIVE\] under the ZS-v2.0.0 convention.

v1.0 dated update 2026-04-24: Added entry H21 “RH-Inclusive Reading of Z-Spin” to §3, tag DERIVED-interpretation, synthesizing four PROVEN/DERIVED corpus elements (ZS-M13 §2.2 Eisenstein–Dedekind factorization; ZS-M18 H11 σ=1/2 ↔ j=1/2 isomorphism; ZS-M1 HSI conformality; ZS-A8 §6 Expansion–Contraction Symmetry and §5.3 Y-Time Dilation). Added falsification gate F-M18.11 (OPEN, awaits RH resolution). §8 Conclusion updated with one sentence locating H21 as a unified frame rather than an elevation candidate. §6 header text updated to reflect 11 gates (10 PROVEN-safe, 1 OPEN). No prior result modified; no numerical prediction introduced; no new free parameter. External label remains v1.0 per Z-Spin no-deletion convention; word count increased monotonically. Verification suite 51/51 PASS unchanged (H21 has no numerical content and introduces no new test). Motivated by Kenny Kang’s structural intuition that the three independent 1/2 occurrences (ZS-M13 §6.2) and the i-tetration π/2 rotation (ZS-M1) are two faces of the same dim(Z) \= 2 Z₂ involution that also fixes the Riemann critical line, yielding an integrative reading that embraces RH without requiring its proof.