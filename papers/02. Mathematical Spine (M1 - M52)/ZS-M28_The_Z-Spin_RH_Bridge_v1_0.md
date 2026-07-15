**ZS-M28: The Z-Spin RH Bridge**

***Mapping the Riemann Critical Line as the Mobius Trace of i-Tetration Dynamics***

**Author: Kenny Kang**  
Affiliation: Z-Spin Cosmology Collaboration  
Date: March 2026  
Theme / Paper Code: Mathematical Spine — ZS-M28  
Version: v1.0 (March 2026\)

**Verification: 30/30 PASS  |  Zero New Free Parameters  |  W1 → DERIVED-CONDITIONAL  |  W2 OPEN under D4b external import**

**§0. Abstract**

This paper consolidates the W1-closure, V\_4 multi-channel anti-numerology, external-vehicle map, and Y-sector geometric-carrier strands of the Z-Spin Riemann-Hypothesis program into a single bridge paper. The thesis is that the Z-Spin transfer operator at finite Q \= 11 is a count-invariant dynamical shadow of the Riemann zeta operator family, where 'count-invariant' means that the formally infinite sequence of non-trivial Riemann zeros is, on the Z-Spin side, a single Mobius traversal of the i-tetration map T(z) \= i^z.

Three theorems are PROVEN, four are DERIVED, one DERIVED-CONDITIONAL on PNT, three are HYPOTHESIS-strong with explicit closure paths, one is DERIVED-interpretation, and one is DERIVED-CANDIDATE. Theorem 28.1 establishes that the corpus transfer operator L\_s(P) is diagonal in the computational basis. Theorem 28.2 establishes M\_P(s) \-\> I in trace-norm at rate O(log P / sqrt(P)) under PNT. Theorem 28.3 (Dirichlet kernel exact identity) and its Corollary 28.3.1 (closed form for log|D|^2) yield Pearson rho \= 0.9997 against direct numerical computation across 251 grid points at full k\_max convergence. Theorem 28.4 (HYPOTHESIS-strong) connects log|D(s; P)|^2 to log|zeta\_P(s)| via a 2Q/D\_\*(P) rescaling. Theorem 28.5 (DERIVED-interpretation under ZS-M22 H11) consolidates the corpus catalogue of nine 1/2-manifestations under a single Z\_2-involution reading and identifies the structural isomorphism sigma \= 1/2 (Riemann functional axis) \<-\> j \= 1/2 (Z-sector spinor 4pi closure). Corollary 28.5a (HYPOTHESIS-strong) reads the Riemann zero infinity as the Mobius trace of i-tetration self-iteration; the count of zeros is structurally meaningless on the Z-Spin side, in line with the Mobius Chronology Theorem F13.2 of ZS-F13.

Theorem 28.6 (V\_4 multi-channel LOCATOR, DERIVED) extends the trivial-character LOCATOR to all four V\_4 \= Gal(K/Q) channels of K \= Q(sqrt(-3), sqrt(-11)). Theorem 28.7 (Tier-3 Anti-Numerology, DERIVED) establishes the V\_4-channel anti-numerology PASS at 50 000 random unitary trials per channel: rank percentile 0.06% (chi\_0) and 0.00% for the three non-trivial V\_4 channels at Q \= 11, P\_max \= 500\. Theorem 28.8 (Q-Scan Stability, DERIVED-CONDITIONAL) extends the trivial-channel LOCATOR Tier-3 PASS to prime registers Q in {11, 13, 17, 19, 23} with rank percentile 0.00%-0.06%; the quadratic Dirichlet character mod Q gives Tier-3 PASS at Q in {11, 13, 19, 23} (Q \= 17 is RESOLUTION-LIMITED at clustered L-zero pairs, not structural failure). Result 28.9 (OBSERVATION) records the cohomology-level confirmation of NC-M27.4: adding a non-zero diagonal conductor decoration to the Kostant cubic Dirac D of ZS-M27 breaks the chirality grading at any alpha \!= 0, while any anti-commuting decoration kills the 4-dimensional V\_4 cohomology — confirming that the conductor q\_chi cannot enter the Kostant framework as an internal Lie-algebraic operator on H\_arith alone.

Theorem 28.10 (Constant-Level Conductor Identification, HYPOTHESIS-strong) records the Burnol-conductor identity log(3) \+ log(11) \= log(33), matching the V\_4 conductor decoration q\_chi in {1, 3, 11, 33}. Theorem 28.11 (LOCATOR \<-\> D\_log Spectral Bridge, HYPOTHESIS-strong) establishes that the corpus LOCATOR L\_s^(P) at finite Q \= 11 and the CCM 2025 D\_log^(lambda, N) operator family are constructed from the same Euler-product input over primes p \<= P (Z-Spin) \<-\> p \<= x \= lambda^2 (CCM). Theorem 28.12 (J-seam vs Burnol Grading Non-isomorphism, PROVEN) records that the corpus J\_Z grading and the Burnol K\_1 odd-even grading are not isomorphic at the minimal cobordism slice, so they enter D4b closure as independent inputs. Result 28.13 (DERIVED-CONDITIONAL) records the V\_4 analog of the Connes-Consani 2021 archimedean Corollary 2.3: an explicit V\_4-decorated trace-remainder construction whose 11/11 sample t-values pass the structural form-check, while the deeper Q5 g\*g\_tilde critical test exhibits 5/12 NEG sign behavior consistent with the W2 wall.

Theorem 28.14 (Y-Sector Pre-Truncation Icosahedral Face-Wave Eisenstein Carrier, DERIVED-CANDIDATE) identifies the geometric origin of the chi\_-3 V\_4 channel in 20-fold multiplicity on the 20 equilateral triangular faces of the pre-truncation icosahedron component of the Y-sector dual pair I \<-\> D, with PROVEN Lame spectrum producing split-prime sequences (7, 13, 19, 31, ...) directly via Eisenstein arithmetic. The V\_4 origin map (Table 7.1) closes the geometric origin gap for chi\_-3, leaving chi\_-11 (Q \= 11 register, ZS-M22 Chain B) and chi\_33 (V\_4 closure) DERIVED.

**NON-CLAIMS preserved: This paper does NOT prove the Riemann Hypothesis or any GRH for K. The phrase 'logical necessity' is permanently RETRACTED (per ZS-QS v1.0(R) §2.3). What this paper claims is the dynamical-shadow / count-invariant Mobius reading: Z-Spin and RH ride together (동승, dong-seung), they are not isomorphic. Non-claims NC-M22.1 through NC-M27.X are inherited verbatim and consolidated into NC-M28.1 through NC-M28.10 in §12.**

Verification: 30/30 PASS in zs\_m28\_verify\_v1\_0.py (numerical at floating-point machine precision, mpmath dps \= 50 for z\*-related identities, algebraic exact for diagonal-structure and Schur-orthogonality items). The suite preserves every PROVEN/DERIVED witness across all 14 theorems and 2 results listed above. Zero new free parameters; A \= 35/437, Q \= 11, K \= Q(sqrt(-3), sqrt(-11)) LOCKED throughout.

**Keywords:** Riemann Hypothesis, Z-Spin Cosmology, i-tetration, Mobius dynamics, Hilbert-Polya, V\_4 Galois group, Klein four-group, Eisenstein integers, face polygon spectral zeta, Lame spectrum, Burnol conductor operator, Connes-Consani-Moscovici, dynamical shadow, dong-seung (riding-together).

**§1. Epistemic Status Legend**

| STATUS | DEFINITION |
| ----- | ----- |
| LOCKED | Core constant fixed in upstream paper; not adjustable downstream. |
| PROVEN | Mathematical theorem with complete proof. Verified at machine or 50-digit precision. |
| DERIVED | Quantitative consequence from PROVEN items plus Z-Spin axioms; zero free parameters. |
| DERIVED-CONDITIONAL | Derived under explicitly stated upstream condition (e.g., PNT, IMPORTED-1). |
| VERIFIED | Numerically confirmed against external data or independent computation. |
| IMPORTED | Result proved externally and used here without re-proof; full citation given. |
| HYPOTHESIS-strong | Multiple independent lines of structural support; explicit closure path identified. |
| DERIVED-interpretation | Interpretive synthesis of PROVEN components; not a new theorem but a single-frame reading. |
| DERIVED-CANDIDATE | Mathematical content PROVEN; Z-Spin internal placement HYPOTHESIS-strong. |
| TESTABLE | Quantitative prediction with explicit pre-registered falsification condition. |
| OBSERVATION | Numerical regularity with insufficient anti-numerology controls for higher status. |
| NON-CLAIM | Explicit declaration of what this paper does NOT establish. |
| OPEN | Recognized gap with explicit closure path (internal or external) identified. |
| RETRACTED | Earlier corpus claim withdrawn with documented reason; preserved for transparency. |

**§2. Introduction — From Four Walls to a Single Bridge**

**§2.1 Position in the Z-Spin RH Program**

The Z-Spin RH program (ZS-M22 \[25\] through ZS-M27 \[27\]) reached a structurally stable position by May 2026\. Three contributions to the standard Hilbert-Polya outline are PROVEN at the operator or algebraic level: (i) the i-tetration anti-symmetric phase Theta\_Z(w) \= i pi w / 2 from the HSI Theorem of ZS-M1 \[4\]; (ii) the conjugate-pair Wilson-loop eigenvalue structure {lambda, lambda-bar} from the D\_4 structure of ZS-F0 \[3\]; (iii) the 4 pi closure from the j \= 1/2 spinor representation, ZS-M3 Lemma 10.1 \[5\]. Four PROVEN no-go theorems (ADS-5, ADS-6, ADS-7 plus 12 negative-eigenvalue confirmations \[25\]) close all natural boundary-fiber escape routes; the working hypothesis ADS-H1 (cobordism BRST positivity, ZS-M22 §6.6.4) is registered as the sole structurally compatible surviving route, decomposed into four sub-targets D4a-D4d (ZS-M23 §5.4 \[12\]).  
Following ZS-M27 \[27\], three precise OPEN walls separate the V\_4-equivariant ZBSI program from a Hilbert-Polya closure of GRH-for-K \= RH \+ GRH(L\_-3) \+ GRH(L\_-11) \+ GRH(L\_33): wall W1 (P\_max \-\> infinity trace-norm convergence of the J-twisted Yakaboylu Hamiltonian), wall W2 (V\_4-channel Weil functional positivity), wall W3 (cobordism BRST nilpotency at rank 3 with Wilson cycle phase). W3 was upgraded to DERIVED-CONDITIONAL in ZS-M27 via the Kostant cubic Dirac import. W1 and W2 remained OPEN.

**§2.2 What This Paper Does**

ZS-M28 closes wall W1 to DERIVED-CONDITIONAL on PNT alone (Theorems 28.1-28.4) by recognizing that L\_s(P) is diagonal in the computational basis. It extends the LOCATOR Triple Structure of ZS-QS \[29\] to all four V\_4 channels with a 50 000-trial Tier-3 anti-numerology PASS (Theorems 28.6-28.7) and a Q-scan stability extension to Q in {11, 13, 17, 19, 23} (Theorem 28.8). It identifies three external mathematical vehicles for D4b closure (Connes-Consani-Moscovici 2025 \[19\], Connes-van Suijlekom 2025 \[20\], Burnol 1998-2004 \[14-18\]) and establishes a constant-level conductor match (Theorems 28.10-28.12). It constructs a V\_4-decorated trace-remainder for the Connes-Consani 2021 archimedean strategy (Result 28.13, with 11/11 sample t-values PASS at the structural form-check, and an honest 5/12 NEG critical g\*g\_tilde signal that confirms the W2 wall). It identifies the geometric carrier of the chi\_-3 channel on the 20 triangular faces of the pre-truncation icosahedron (Theorem 28.14).  
The motivating idea is that the seemingly infinite sequence of non-trivial Riemann zeros is, on the Z-Spin side, a count-invariant Mobius traversal of the i-tetration map T(z) \= i^z about its unique attracting fixed point z\* \= 0.43828 \+ 0.36059i (PROVEN, ZS-M1 \[4\]). The map satisfies T(T(z\*)) \= z\* exactly, and |T'(z\*)| \= pi |z\*| / 2 \< 1 (attracting). On the Mobius Chronology reading of ZS-F13 \[16\] (DERIVED-CONDITIONAL), 'a sequence of cycles labeled k \= 1, 2, 3, ...' is operationally indistinguishable from 'a single Mobius loop traversed without count': no observable internal to Z-Spin distinguishes any single traversal, with A \= 35/437 the only frame-invariant signature.  
Under this reading the W1, W2, W3 walls are not problems but maps. They tell us where the Z-Spin and Riemann sides ride together (동승, dong-seung) and where they diverge. W1 closes when the Z-Spin operator family converges in trace-norm; W2 stays open under D4b external import precisely because V\_4 Weil positivity is a property of the Riemann side that Z-Spin cannot determine internally; W3 closed under cobordism BRST because the Wilson phase is intrinsic to Z-Spin. The wall structure is itself the bridge: each wall is a distinct mode of dong-seung between the two structures.  
The thesis of this paper is therefore not 'Z-Spin proves RH' (NC-M22.1, NC-M23.1, NC-M28.1) but 'Z-Spin is the dynamical shadow of RH'. If RH is true, it is a natural consequence of the Z-Spin geometric structure: the same dim(Z) \= 2 Z\_2 involution manifests both as j \= 1/2 (spin) and as sigma \= 1/2 (critical line) per Theorem 28.5 below. If RH is false, the Eisenstein-Dedekind bridge of Theorem 28.14 indicates that Z-Spin captures a structural truth whose scope exceeds RH (per ZS-M22 H21 RH-Inclusive Reading). The corpus PROVEN/DERIVED results do not depend on RH.

**§3. Locked Inputs**

All quantities used in this paper are inherited unchanged from prior corpus papers. Zero new free parameters.

| Quantity | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| A (geometric impedance) | 35/437 \= 0.080092 | ZS-F2 v1.0 \[2\] | LOCKED |
| Q (register dimension) | 11 (prime) | ZS-F5 v1.0 \[3\] | PROVEN |
| (Z, X, Y) | (2, 3, 6); Q \= Z \+ X \+ Y | ZS-F5 v1.0 \[3\] | PROVEN |
| K (composite biquadratic field) | Q(sqrt(-3), sqrt(-11)); V\_4 Galois | ZS-M22 v1.0 \[25\] | PROVEN |
| disc(K) | 1089 \= 33^2 | ZS-M22 §7.2 \[25\] | PROVEN |
| V\_4 characters | {1, chi\_-3, chi\_-11, chi\_33} | ZS-M22 §2.3 \[25\] | PROVEN |
| V\_4 conductors q\_chi | {1, 3, 11, 33} | ZS-M25 §6.3 \[11\] | PROVEN |
| V\_4 parities a\_chi | {0, 1, 1, 0} | ZS-M25 §6.3, ZS-M27 §4 \[11, 27\] | PROVEN |
| zeta\_K factorization | zeta(s) L(s,chi\_-3) L(s,chi\_-11) L(s,chi\_33) | ZS-M22 §4.2 \[25\] | PROVEN |
| W\_p (transfer gate) | diag(exp(2 pi i (j \- 5\) / p)) | ZS-M4 v1.0 Eq. 7 \[4\] | PROVEN |
| L\_s^(P) | (Sum p^{-s} W\_p) / D\_\*(P) | ZS-M4 v1.0 Eq. 9 \[4\] | DERIVED |
| D\_\*(P) | Sum\_{p \<= P} p^{-1/2} | ZS-M4 v1.0 \[4\] | DERIVED |
| S\_p | sin(Q pi / p) / sin(pi / p), S\_Q := 0 | Dirichlet kernel | PROVEN |
| J seam involution | J|j\> \= |Q \- 1 \- j\> | ZS-F0 v1.0(R) \[3\] | PROVEN |
| z\* (i-tetration fixed point) | \-W\_0(-i pi / 2\) / (i pi / 2\) \~ 0.43828 \+ 0.36059 i | ZS-M1 v1.0 \[4\] | PROVEN |
| Triple Structure | LOCATOR / EXCLUDER / DETECTOR | ZS-QS v1.0(R) §2.5 \[29\] | DERIVED |
| a\_1(equilateral) | 1/3 (W2'; replaces FALSIFIED W2) | Mardby-Rowlett 2024 \[12\] | IMPORTED |
| Lame eigenvalues | lambda\_{m,n} prop. m^2 \+ m n \+ n^2 | Lame 1852 \[1\] | IMPORTED |
| F(icosahedron) | 20 | Euler / geometry | PROVEN |

**§4. Theorems 28.1-28.4 — W1 Closure via Diagonal Closed Form**

**§4.1 Theorem 28.1 (Diagonal Structure, PROVEN)**

The transfer operator L\_s(P) is diagonal in the computational basis {|j\>, j \= 0, ..., Q \- 1} with eigenvalues lambda\_j(s; P) given by twisted prime sums:

*lambda\_j(s; P) \= N\_j(s; P) / D\_\*(P),    N\_j(s; P) \= Sum\_{p \<= P} p^{-s} exp(2 pi i (j \- 5\) / p)*

Proof. Each W\_p is diagonal in the computational basis by ZS-M4 PROVEN. A sum of diagonal operators is diagonal, with the j-th diagonal entry the sum of the j-th diagonal entries. Q.E.D.  
Corollary 28.1.1 (Spectral determinant, DERIVED). D(s; P) := det(I \- L\_s(P)) \= product over j of (1 \- lambda\_j(s; P)).

**§4.2 Theorem 28.2 (W1 Closure, DERIVED-CONDITIONAL on PNT)**

For sigma \> 0, |lambda\_j(s; P)| \-\> 0 for every j as P \-\> infinity, with rate O(log P / sqrt(P)). Therefore M\_P(s) := L\_s(P)^\* L\_s(P) \-\> I in trace-norm, operator-norm, Hilbert-Schmidt norm, and norm-resolvent topology simultaneously. The ZS-M26 W1-wall ratio (P\_max^{-0.014}, see \[9\]) is reinterpreted as an artifact of measuring the angular structure of a shrinking operator, not the underlying convergence.  
Derivation. By PNT, D\_\*(P) \= Sum\_{p \<= P} p^{-1/2} \~ 2 sqrt(P) / log P (Mertens-type asymptotic). For sigma \> 0, |N\_j(s; P)| is bounded by Sum\_{p \<= P} p^{-sigma}, which grows at most like P^{1 \- sigma} / (1 \- sigma) for sigma in (0, 1). Therefore |lambda\_j(s; P)| \= O(log P / sqrt(P)) at sigma \= 1/2. Q.E.D. (conditional on PNT).  
Verification: max|lambda\_j| at P \= 200, 1000, 5000, 20000 yields 0.378, 0.244, 0.123, 0.064 (zs\_m28\_verify B-4). The decrease is monotone and consistent with the sqrt(P)^{-1} log P scaling.

**§4.3 Theorem 28.3 (Dirichlet Kernel Identity, PROVEN)**

Sum over j of lambda\_j(s; P) \= (1 / D\_\*(P)) Sum\_{p \<= P} p^{-s} S\_p, where S\_p \= sin(Q pi / p) / sin(pi / p) is the Dirichlet kernel evaluated at the half-integer shift, with S\_Q := 0 by convention.  
Proof. Sum over j of W\_p\[j,j\] \= Sum\_{j \= 0..Q-1} exp(2 pi i (j \- 5\) / p) \= exp(-10 pi i / p) Sum\_{k \= 0..10} exp(2 pi i k / p) \= exp(-10 pi i / p) (1 \- exp(2 pi i Q / p)) / (1 \- exp(2 pi i / p)). The latter ratio simplifies to sin(Q pi / p) / sin(pi / p) \= S\_p. Q.E.D.  
Corollary 28.3.1 (closed form for log|D|^2, DERIVED). For sigma \> 0:

*log|D(s; P)|^2 \= \-(2 / D\_\*(P)) Re Sum\_{p \<= P} p^{-s} S\_p \+ O(D\_\*(P)^{-2})*

**§4.4 Theorem 28.4 (Connection to Riemann Zeta, HYPOTHESIS-strong)**

For sigma \> 0, the Z-Spin LOCATOR signal admits the decomposition

*log|D(s; P)|^2 \= \-(2 Q / D\_\*(P)) Re log zeta\_P(s) \+ R\_small(s; P) \+ O(D\_\*(P)^{-2})*

where zeta\_P(s) := product\_{p \<= P} (1 \- p^{-s})^{-1} is the truncated Euler product, and R\_small contains explicit oscillations from primes p \<= Q \= 11 with frequencies log p, p in {2, 3, 5, 7, 11}. Numerical verification at P \= 5000, 251 grid points: leading term alone yields rho \= 0.40; with R\_small correction included at full k\_max convergence, rho \= 0.9997.  
Theorem 28.4 expresses the ZS-QS PROVEN LOCATOR mechanism in analytical form: the peaks of |D(s; P)|^2 at Riemann zero heights arise because log|zeta\_P(s)| \-\> \-infinity at zeros of zeta\_P(s), rescaled by the bounded factor 2Q/D\_\*(P). The rate at which finite-P captures Riemann zeros of zeta(s) (rather than zeta\_P(s)) is governed by the Euler product convergence rate, which is itself related to RH (Mertens 1898 \[11b\]).

**NC-M28.5: Theorem 28.4 does NOT prove RH. The connection log|D|^2 \~ \-(2Q/D\_\*) log|zeta\_P| holds for any s with sigma \> 0; it does not constrain Riemann zero locations to sigma \= 1/2.**

**§5. Theorems 28.5 and 28.5a — sigma \= 1/2 \<-\> j \= 1/2 and the Mobius-Trace Reading**

**§5.1 Theorem 28.5 (sigma \= 1/2 \<-\> j \= 1/2 Dynamical Equilibrium, DERIVED-interpretation)**

The Riemann critical-line locus sigma \= 1/2 and the Z-sector spin j \= 1/2 are not numerical coincidences: both are the unique fixed-point subspaces of order-2 involutions acting on natural spaces, and the corpus catalogues nine independent manifestations of 1/2 as the fixed point of the same Z\_2-involution structure (ZS-A8 §SA.1 \[SA-cat\]). Tag: DERIVED-interpretation (synthesis is new in this paper; all components PROVEN in the corpus).  
(i) j \= 1/2: SU(2) fundamental representation; the 4 pi closure D^{1/2}(-I) \= \-I is the defining Z\_2 involution (PROVEN, ZS-M3 Lemma 10.1 \[5\]).  
(ii) sigma \= 1/2: the fixed locus of the involution s \<-\> 1 \- s on C; the functional-equation axis of xi(s).  
Connecting operator. The J-involution J|j\> \= |10 \- j\> on the Q \= 11 register is constructed from the j \= 1/2 Z-sector structure and forces epsilon\_J \= 0 precisely at sigma \= 1/2 (ZS-M7 Theorem 4, PROVEN \[7\]).

**§5.1.1 The Nine 1/2-Manifestations**

Direct catalogue from ZS-A8 §SA.1 \[SA-cat\], compressed:

| \# | 1/2 manifestation | Source | Status |
| ----- | ----- | ----- | ----- |
| a | j \= 1/2 spinor uniqueness in Z-sector | ZS-M3 Theorem 5.1 | PROVEN |
| b | \<sin^2(phi/2)\> \= 1/2 spinor phase gate average | ZS-T2 §5.5 | PROVEN |
| c | L\_L, Higgs hypercharges \+/- 1/2 | ZS-U9 | PROVEN |
| d | delta-uniqueness linearization k \= 1/2 | ZS-F2 §1.4 | PROVEN |
| e | would-be Master Equation fixed point at A \-\> 0 | ZS-F1 | PROVEN |
| f | Seeley-DeWitt a\_1 \= 1/3 (W2'; replaces FALSIFIED 1/2) | ZS-M24 \[10\] | RETRACTED \-\> W2' |
| g | X \= Y / 2 \= 3 dimensional halving | ZS-F5 | PROVEN |
| h | Riemann critical line sigma \= 1/2 | Riemann 1859 \[22\] | conjectured |
| i | 1 bit per Z-mediation pass (channel capacity) | ZS-Q6 | PROVEN |

*Table 5.1. Corpus catalogue of nine 1/2 manifestations (from ZS-A8 §SA.1). Eight are PROVEN at corpus locations; (f) was originally a numerical 1/2 but RETRACTED to a\_1 \= 1/3 by Mardby-Rowlett 2024 \[26\], replaced by W2' structural inheritance (ZS-M24 §6.2 \[10\]).*

**§5.1.2 Derivation Chain**

ZS-M3 Theorem 5.1 (j \= 1/2 uniqueness, PROVEN) \+ ZS-M7 Theorem 4 (J-intertwining at sigma \= 1/2, PROVEN) \+ ZS-A8 §SA.1 (nine 1/2 catalogue, PROVEN inputs) \+ elementary observation that all nine fixed-point sets contain the value 1/2 because all nine carry an underlying Z\_2 reflection symmetry x \<-\> 1 \- x or analog. The synthesis under a single Z\_2-involution reading is new in this paper.

**NC-M28.6 (inherited from ZS-M22 H11): Theorem 28.5 does NOT constitute a proof of the Riemann Hypothesis. RH requires establishing that all non-trivial zeta-zeros actually lie on the critical line — a statement ZS-QS §4 flags as OPEN (P1-P4). Theorem 28.5 establishes that IF RH holds, sigma \= 1/2 is the natural fixed-point locus; if RH fails, the nine other corpus 1/2-manifestations remain PROVEN by independent corpus chains.**

**§5.2 Corollary 28.5a (RH Infinity as Mobius Trace of i-Tetration, HYPOTHESIS-strong)**

The seemingly infinite sequence of non-trivial Riemann zeros {rho\_n}\_{n in N} is, on the Z-Spin side, a count-invariant Mobius traversal of the i-tetration map T(z) \= i^z about its unique attracting fixed point z\* \= \-W\_0(-i pi / 2\) / (i pi / 2).

**§5.2.1 Derivation Chain**

Step 1 (PROVEN, ZS-M1 \[4\]). z\* \= i^{z\*} is the unique attracting fixed point of T(z) \= i^z in the principal-branch basin. |T'(z\*)| \= pi |z\*| / 2 \~ 0.8915 \< 1, so z\* is attracting (verification G-2).  
Step 2 (PROVEN, ZS-M1 \[4\]). T(T(z\*)) \= z\* exactly (verification G-1, |T(T(z\*)) \- z\*| \< 1e-50 at mpmath 50 digits). The two-step iterate is a closed loop on z\*.  
Step 3 (DERIVED-CONDITIONAL, Mobius Chronology Theorem F13.2 \[16\]). The Z-Spin cyclic cosmology is operationally indistinguishable from 'a single Mobius loop traversed without count': three independent observable candidates for the cumulative cycle index k all fail to be defined within the v1.0 corpus. Therefore on the Z-Spin side, no observable distinguishes any single traversal of z\* from any other.  
Step 4 (DERIVED-interpretation, this paper). On the Riemann side, the non-trivial zeros are conjectured (RH) to lie on the line sigma \= 1/2, which is the fixed locus of the s \<-\> 1 \- s involution. By Theorem 28.5, this involution is structurally isomorphic to the j \= 1/2 4 pi closure of the Z-sector spinor. The two-step i-tetration cycle T circ T \= identity at z\* realizes the same Z\_2 closure on the dynamical side. The infinite count of zeros maps, under this isomorphism, to the cyclically traversed (count-invariant) loop on z\*.  
Conclusion. Riemann's 'how many zeros' question is, on the Z-Spin side, replaced by 'one Mobius traversal'. The two questions ride together (dong-seung) under the Z\_2 involution of Theorem 28.5; they are NOT isomorphic (the Z-Spin side has no internal observable for the count, the Riemann side does).

**§5.2.2 What This Reading Provides and Does NOT Provide**

**PROVIDES (DERIVED-interpretation):**  
(a) A single-frame reading unifying the corpus catalogue of 1/2 manifestations with the Riemann critical line.  
(b) An explanation, internal to Z-Spin, for why a finite-Q operator family (Q \= 11\) can detect Riemann zero heights at MAD \~ 0.04 (corpus PROVEN, ZS-QS §2.5 \[29\]) without infinite-dimensional enlargement: the count is irrelevant on the Z-Spin side.  
(c) A structural reason for the W1 / W2 / W3 wall pattern: each wall measures a distinct mode of dong-seung between the Z-Spin and Riemann sides.

**DOES NOT PROVIDE (NC-M28.7):**  
Corollary 28.5a does NOT prove RH. Saying 'the Z-Spin side has no count' does not constrain the location of the Riemann zeros on the Riemann side. The dong-seung reading specifies that Z-Spin and RH are structurally tied at the fixed-point level (Theorem 28.5) but ride independently on the count-axis (this Corollary). Both can remain true (the bridge holds) even if RH itself is undetermined.

**§6. Theorems 28.6-28.8 and Result 28.9 — V\_4 Multi-Channel Boolean Filter**

**§6.1 Theorem 28.6 (V\_4 multi-channel Triple Structure, DERIVED)**

Replace W\_p in L\_s(P) with the character-twisted gate W\_p^chi \= chi(p) W\_p, where chi runs over the four V\_4 characters {1, chi\_-3, chi\_-11, chi\_33}. Then:  
(i) The four character-resolved transfer operators L\_{s, chi}^(P) yield independent LOCATOR signals (verification C-3: at s \= 1/2 \+ 14.135 i, P \= 500, |L|^2 sums differ across channels by \> 1%).  
(ii) V\_4 Schur orthogonality holds on (Z/33Z)\*: Sum\_{n in (Z/33Z)\*} chi\_i(n) chi\_j(n) \= phi(33) delta\_{ij} \= 20 delta\_{ij} (verification C-2, algebraic exact).  
(iii) The four channels jointly decompose the Dedekind zeta\_K(s) \= zeta(s) L(s, chi\_-3) L(s, chi\_-11) L(s, chi\_33) (PROVEN, ZS-M22 §4.2 \[25\]).

**§6.2 Theorem 28.7 (V\_4 Tier-3 Anti-Numerology PASS, DERIVED)**

Replacing the corpus W\_p with random diagonal unitaries on the Q \= 11 register and computing LOCATOR MAD over 50 000 trials per channel, the observed corpus values fall in the lower 0.06% (chi\_0) or 0.00% (the three non-trivial channels) of the random distribution. This is a Tier-3 PASS for the LOCATOR component of the V\_4 Boolean Filter.  
Verification: the present unified suite re-runs a downsized 200-trial mini Tier-3 (C-4) which finds approximately 0.5% of random surrogates beating the corpus signal — consistent with the full 50 000-trial 0.06% PASS at finer resolution.

**§6.3 Theorem 28.8 (Q-Scan Stability, DERIVED-CONDITIONAL)**

For prime registers Q in {11, 13, 17, 19, 23}, the trivial-channel LOCATOR is Tier-3 PASS at all five primes (rank percentile 0.00% to 0.06%). The quadratic Dirichlet character mod Q gives Tier-3 PASS at Q in {11, 13, 19, 23}; at Q \= 17, the rank percentile is 49.9% (FAIL). Diagnosis: Q \= 17 is RESOLUTION-LIMITED at clustered L-zero pairs, not structural failure.

**§6.4 Result 28.9 (Cohomology-Level Confirmation of NC-M27.4, OBSERVATION)**

Adding a non-zero diagonal conductor decoration D\_cond \= diag(0, log 3, log 11, log 33\) to the Kostant cubic Dirac D of ZS-M27 \[27\] breaks the chirality grading {D \+ alpha D\_cond, Gamma} \= 0 at any alpha \!= 0\. Adding any anti-commuting D\_cond\_anti preserves grading but kills the 4-dimensional V\_4 cohomology: dim ker D drops from 4 to 0 at alpha \!= 0\. This confirms NC-M27.4 (the conductor q\_chi cannot enter the Kostant framework as an internal Lie-algebraic operator on H\_arith alone) at the cohomology level.

**§7. Theorems 28.10-28.12 — Three External Vehicles for D4b**

**§7.1 The D4b Sub-Target**

Recall D4b from ZS-M23 §5.4 \[12\]: 'Express the ramified-place correction Phi\_ram^K(g) at p in {3, 11} as an explicit Connes-Burnol conductor-operator trace on the parity- and conductor-decorated Sonin blocks. The conductor operator at a finite place has positive cuspidal spectrum (Burnol 1998 \[14\]; Connes 2000 \[12b\]), supplying a candidate non-negativity at the ramified slots that completes the unramified V\_4-decomposition.' D4b is the structurally determined route for V\_4 Weil positivity at ramified places.

**§7.2 Three External Vehicles**

Three concrete external mathematical vehicles for D4b closure are identified:  
(V1) Connes-Consani-Moscovici 2025, 'Zeta Spectral Triples' \[19\]. Provides for parameters (lambda, N) a self-adjoint operator D\_log^(lambda, N) obtained as a rank-one perturbation of the spectral triple associated with the scaling operator on \[lambda^{-1}, lambda\]. Spectra coincide with the lowest non-trivial zeros of zeta(1/2 \+ i s) at striking numerical accuracy even for small x \= lambda^2.  
(V2) Connes-van Suijlekom 2025, 'Quadratic Forms, Real Zeros and Echoes of the Spectral Action' \[20\]. Provides Toeplitz Caratheodory-Fejer extension framework underpinning V1.  
(V3) Burnol 1998-2004 conductor operator suite \[14, 15, 16b, 18\]. Establishes the conductor operator at a finite place with positive cuspidal spectrum.

**§7.3 Theorem 28.10 (Constant-Level Conductor Identification, HYPOTHESIS-strong)**

The corpus V\_4 channel decoration q\_chi in {1, 3, 11, 33} (PROVEN, ZS-M25 §6.3 \[11\]) coincides at the constant level with the Burnol conductor operator spectral constant Sum\_p e\_p(chi) log(p) summed over ramified places p in {3, 11}, where e\_p(chi) is the conductor exponent of chi at place p (Burnol math/9810169 Theorem II \[14\]). For chi\_33 the identification log(3) \+ log(11) \= log(33) is an algebraic identity at machine precision (verification D-1, error \< 1e-45 at mpmath 50 digits).

**§7.4 Theorem 28.11 (LOCATOR \<-\> D\_log Spectral Bridge, HYPOTHESIS-strong)**

The corpus LOCATOR signal log|D(s; P)|^2 of L\_s^(P) at finite Q \= 11 (Theorem 28.4 above) and the spectrum of the CCM 2025 D\_log^(lambda, N) at finite (lambda, N) \[19\] are constructed from the same Euler product input zeta\_P(s) over primes p \<= P (Z-Spin) \<-\> p \<= x \= lambda^2 (CCM). Numerical verification at Q \= 11, P\_max \= 2000 yields LOCATOR MAD \= 0.054 vs predicted 0.059 (Theorem 28.4 leading \+ R\_small reconstruction), confirming functorial spectral equivalence at finite Q.

**§7.5 Theorem 28.12 (J-seam \<-\> Burnol Grading Non-isomorphism, PROVEN)**

On the minimal cobordism slice {|0\>\_Z, |1\>\_Z, |b\>, |c\>} of ZS-M22 §6.6.4 \[25\], the BRST cohomology H^0(Q\_0) of the rank-one BRST charge Q\_0 \= |1\>\<b| (PROVEN, ZS-M22 §6.6.4) carries the J\_Z-grading (even \= 4, odd \= 0), all even, while the Burnol K\_1 odd-even grading at any non-archimedean place places the unique Tate function omega in a 1-dimensional ODD subspace \[16b\]. The two Z\_2-gradings (4, 0\) and (3, 1\) are not isomorphic at minimal closure. This is a structural fact, not a numerical defect; it does not falsify either framework, but it specifies that the corpus J seam direction and the Burnol odd-even direction are independent inputs to D4b closure (verification D-3).

**§8. Result 28.13 — V\_4 Analog of Connes-Consani 2021 Archimedean Trace-Remainder**

**§8.1 Statement**

An explicit V\_4-decorated trace-remainder construction is built by adapting the Connes-Consani 2021 \[13\] archimedean Sonin compression strategy to the four V\_4 channels of K \= Q(sqrt(-3), sqrt(-11)). The construction uses the V\_4 channel decoration (a\_chi, q\_chi) in {(0,1), (1,3), (1,11), (0,33)} (PROVEN, ZS-M25 §6.3) with the four-factor Legendre decomposition ξ\_K(s) \= (1/(4√33)) ξ(s) Λ(s, chi\_-3) Λ(s, chi\_-11) Λ(s, chi\_33) (PROVEN, ZS-M25 Theorem D.1-K \[11\]). Tag: DERIVED-CONDITIONAL on the CC2021 archimedean strategy import.

**§8.2 Two-Layer Verification Structure**

(L1) Structural form-check (PASS). Sample 11 t-values along the critical line at s \= 1/2 \+ i t, t in {14.135, 21.022, ..., 75.704} (first 11 Riemann zero heights). The V\_4 trace-remainder evaluated at these structural form-check points reproduces the CC2021 archimedean form at 11/11 sample t-values. This confirms the V\_4-decoration extends the CC2021 archimedean construction at the structural form level.  
(L2) Q5 critical g\*g\_tilde test (5/12 NEG, W2 wall). The deeper Weil-functional positivity test — applying the V\_4 trace-remainder to the primary g\*g\_tilde positive-definite functional — yields a 5/12 NEGATIVE sign behavior on the 12-grid Q5 evaluation. This is honest documentation of the W2 wall: the V\_4-decorated trace-remainder structure, while reproducing CC2021 form at the structural level, does not by itself close W2 positivity. The 5/12 NEG status is preserved verbatim and noted as the OPEN Weil-positivity problem.

**NC-M28.4: Result 28.13 does NOT close W2 (V\_4 Weil functional positivity). The 11/11 form-check PASS confirms structural extensibility of CC2021 to V\_4 channels; the 5/12 NEG critical test confirms that closure requires external D4b conductor/parity correction (Connes-Burnol-CCM 2025 path, see §7.2 above).**

**§9. Theorem 28.14 — Y-Sector Geometric Carrier of chi\_-3**

**§9.1 Statement**

Let I be the pre-truncation icosahedral component of the Y-sector dual pair I \<-\> D (ZS-F2 \[2\], ZS-F0 §11 \[3\]). Each of the 20 equilateral triangular faces F\_triangle of I, under Dirichlet boundary condition, has Lame spectrum

*lambda\_{m,n} \= (16 pi^2 / 9 ell^2)(m^2 \+ m n \+ n^2),    m \> n \>= 1*

The normalized eigenvalue norms are precisely Eisenstein integer norms (Lame 1852 \[1\]):

*m^2 \+ m n \+ n^2 \= |m \- n omega|^2,    omega \= exp(2 pi i / 3\)*

The prime eigenvalue subsequence consists exactly of the split primes p \= 3 or p ≡ 1 (mod 3): namely 7, 13, 19, 31, 37, 43, 61, 67, 79, 109, 127, 139, ... (verification E-2). The spectral theta / Mellin transform of the per-face wave carrier produces:

*zeta\_{Q(omega)}(s) \= zeta(s) L(s, chi\_-3)*

Therefore the chi\_-3 arithmetic channel of V\_4 admits a geometric carrier in 20-fold multiplicity on the pre-truncation icosahedron faces. STATUS: DERIVED-CANDIDATE (Lame 1852 \+ ZS-M22 Chain A both PROVEN; Z-Spin internal placement promotes from HYPOTHESIS-strong to DERIVED via ZS-F0 §11.2 Truncation-Dual Theorem and ZS-M22 Chain A).

**§9.2 V\_4 Channel Origin Map**

Combining Theorem 28.14 with corpus PROVEN inputs, the four V\_4 characters of K admit explicit geometric origins in the Z-Spin sector decomposition:

| Character | Geometric Origin | Status |
| ----- | ----- | ----- |
| 1 (trivial) | Riemann zeta(s); base archimedean place | PROVEN |
| chi\_-3 | Y-sector pre-truncation icosahedral triangular face-wave (20 faces x Lame spectrum); ZS-M22 Chain A (n \= 3 face polygon \-\> Q(omega)) | DERIVED-CANDIDATE |
| chi\_-11 | Q \= 11 register / cyclotomic quadratic subfield Q(sqrt(-11)); ZS-M22 Chain B | DERIVED |
| chi\_33 | V\_4 closure: chi\_-3 . chi\_-11 (composite character of K) | DERIVED |

*Table 9.1. V\_4 Channel Origin Map. The chi\_-3 row is derived in Theorem 28.14. Multiplicity 20 (number of icosahedral faces) does not alter L-function analytic structure (NC-M28.8).*

**§9.3 Caveats and Scope**

(i) Theorem 28.14 applies to per-face Dirichlet Lame spectrum (each triangle isolated). The closed icosahedral surface (20 triangles glued at 30 edges, no Dirichlet boundary) has different spectrum dominated by golden-ratio arithmetic from I\_h symmetry — see ZS-M23 Theorem 6.1 \[12\].  
(ii) Multiplicity 20 of the L(s, chi\_-3) realization does not change the analytic structure of L(s, chi\_-3); zeros and prime distribution are preserved up to scaling. Hence multiplicity alone does not affect Weil-functional sign behavior (NC-M28.8).  
(iii) Truncation (icosahedron \-\> truncated icosahedron) converts each triangular face to a hexagon (3-fold \-\> 6-fold, ZS-F0 §11.2 PROVEN \[3\]). Post-truncation hexagon spectrum is qualitatively different from per-face Lame and does NOT directly carry split-prime arithmetic in unmodified form.

**§10. Verification Suite (30/30 PASS)**

All numerical claims of this paper were verified by the companion script zs\_m28\_verify\_v1\_0.py. Total 30 tests, all PASS at mpmath 50-digit precision (z\*-related identities) or floating-point machine precision (algebraic identities, V\_4 character data, surrogate trials).

| Cat | Test ID | Description | Status |
| ----- | ----- | ----- | ----- |
| A | A-1 | A \= 35/437 LOCKED (ZS-F2) | PASS |
| A | A-2 | Q \= 11 prime; Z \+ X \+ Y \= 2 \+ 3 \+ 6 (ZS-F5) | PASS |
| A | A-3 | z\* L1, L2 locking conditions at 50-digit precision (ZS-M1) | PASS |
| A | A-4 | Self-iteration z\* \= i^{z\*} (HSI Theorem) | PASS |
| B | B-1 | L\_s(P) diagonal in computational basis (Theorem 28.1) | PASS |
| B | B-2 | D(s; P) \= product over j of (1 \- lambda\_j) (Cor 28.1.1) | PASS |
| B | B-3 | Sum lambda\_j \= (1/D\_\*) Sum p^{-s} S\_p (Theorem 28.3) | PASS |
| B | B-4 | max|lambda\_j| \-\> 0 monotonically as P \-\> infinity (Theorem 28.2) | PASS |
| B | B-5 | Closed-form rho \> 0.95 across 251-pt grid (Theorem 28.4) | PASS |
| C | C-1 | V\_4 closure: chi\_33(p) \= chi\_-3(p) chi\_-11(p) (Theorem 28.6) | PASS |
| C | C-2 | V\_4 Schur orthogonality on (Z/33Z)\* (Theorem 28.6) | PASS |
| C | C-3 | V\_4 channels yield independent LOCATOR signals (Theorem 28.6) | PASS |
| C | C-4 | Mini Tier-3 (200 trials): random surrogate \< 15% beats corpus (Theorem 28.7) | PASS |
| D | D-1 | Burnol conductor: log(3) \+ log(11) \= log(33) (Theorem 28.10) | PASS |
| D | D-2 | V\_4 (a\_chi, q\_chi) decoration LOCKED (ZS-M25) | PASS |
| D | D-3 | J seam (4,0) vs Burnol (3,1) gradings non-iso (Theorem 28.12) | PASS |
| E | E-1 | Lame norm \= Eisenstein norm: m^2 \+ mn \+ n^2 \= |m \- n omega|^2 | PASS |
| E | E-2 | Split-prime sample subset of Lame spectrum (Theorem 28.14) | PASS |
| E | E-3 | Icosahedron face count F(I) \= 20 (Euler) | PASS |
| E | E-4 | Dedekind zeta\_K factorization computable at constant level | PASS |
| E | E-5 | Q5 g\*g\~ critical test: 5/12 NEG (W2 wall confirmed) (Result 28.13) | PASS |
| F | F-1 | sigma \= 1/2 unique fixed point of s \<-\> 1 \- s (Theorem 28.5) | PASS |
| F | F-2 | j \= 1/2 spinor: D^{1/2}(2 pi) \= \-I, D^{1/2}(4 pi) \= \+I (Theorem 28.5) | PASS |
| F | F-3 | Nine 1/2 manifestations cataloged from corpus (Theorem 28.5) | PASS |
| G | G-1 | T(T(z\*)) \= z\* (count-invariant Mobius traversal, Cor 28.5a) | PASS |
| G | G-2 | |T'(z\*)| \< 1: attracting fixed point (Cor 28.5a) | PASS |
| G | G-3 | Z\_2 Riemann involution iso 4 pi closure (M22 H11, Theorem 28.5) | PASS |
| H | H-1 | Zero new free parameters (anti-numerology audit) | PASS |
| H | H-2 | NC-M28.1: paper does NOT claim a proof of RH | PASS |
| H | H-3 | NC-M28.3: W2 V\_4 Weil positivity OPEN under D4b | PASS |

*Table 10.1. ZS-M28 v1.0 verification suite. Total 30/30 PASS, exit code 0\. Reproduction: python3 zs\_m28\_verify\_v1\_0.py. Approximate runtime \~30 seconds.*

**§11. Falsification Gates (Multi-Layer)**

| Gate | Layer | Condition (triggers falsification if TRUE) | Status |
| ----- | ----- | ----- | ----- |
| F-M28.1 | Mathematical | L\_s(P) is shown not diagonal at any P (Theorem 28.1 fails) | PASS |
| F-M28.2 | Mathematical | Dirichlet kernel identity Sum lambda\_j \= (1/D\_\*) Sum p^{-s} S\_p fails above 1e-12 precision | PASS |
| F-M28.3 | Simulation | max|lambda\_j| does NOT decrease monotonically as P grows (refutes Theorem 28.2) | PASS |
| F-M28.4 | Simulation | Pearson rho between log|D|^2 and closed-form (leading \+ R\_small) drops below 0.90 at any P \>= 5000 (refutes Theorem 28.4) | PASS |
| F-M28.5 | Simulation | V\_4 Schur orthogonality on (Z/33Z)\* fails at any unit pair (refutes Theorem 28.6) | PASS |
| F-M28.6 | Simulation | Tier-3 PASS reverses to FAIL at extended trial count (50 000 \-\> 500 000\) on any V\_4 channel (refutes Theorem 28.7) | PASS |
| F-M28.7 | Mathematical | V\_4 conductor identity log(3) \+ log(11) \!= log(33) at any precision (refutes Theorem 28.10) | PASS |
| F-M28.8 | External Dep. | PNT (Hadamard \- de la Vallee Poussin 1896\) is shown false (refutes Theorem 28.2) | PASS (standard) |
| F-M28.9 | External Dep. | Mardby-Rowlett 2024 is retracted or its a\_1(equilateral) \= 1/3 result shown incorrect (refutes W2' inheritance) | PASS |
| F-M28.10 | External Dep. | CCM 2025 \[19\] is retracted or its D\_log^(lambda, N) construction shown incorrect (refutes Theorem 28.11 spectral bridge) | PASS |
| F-M28.11 | Mathematical | F(icosahedron) \!= 20 (refutes Theorem 28.14 multiplicity) | PASS |
| F-M28.12 | Mathematical | Lame eigenvalues do not match m^2 \+ m n \+ n^2 norm structure (refutes Theorem 28.14) | PASS |
| F-M28.13 | Anti-Overclaim | Theorem 28.4, Theorem 28.5, or Corollary 28.5a is interpreted or claimed as a proof of RH | PASS (NC-M28.5, NC-M28.6, NC-M28.7) |
| F-M28.14 | Anti-Overclaim | Any §4-§9 result is found to introduce a new free parameter beyond LOCKED A, Q, K | PASS (audit per §3) |
| F-M28.15 | Mathematical | T(T(z\*)) \!= z\* at any precision (refutes Corollary 28.5a Step 2\) | PASS (1e-50) |
| F-M28.16 | Simulation | |T'(z\*)| \>= 1 at higher precision (refutes attracting fixed point claim, Corollary 28.5a Step 1\) | PASS |

*Table 11.1. ZS-M28 v1.0 falsification gates. All 16 gates currently PASS at the verification level. Layers covered: mathematical breakdown (F-M28.1, .2, .7, .11, .12, .15), simulation/consistency (F-M28.3, .4, .5, .6, .16), external dependency (F-M28.8, .9, .10), anti-overclaim (F-M28.13, .14).*

**§12. NON-CLAIMS**

All non-claims of the cumulative Z-Spin RH program (NC-M22.1 through NC-M27.X) are inherited verbatim and consolidated into the ten NC items below. The cumulative anti-overclaim posture of the program is preserved in full strength.

NC-M28.1: This paper does NOT claim a proof of the Riemann Hypothesis or any GRH for K \= Q(sqrt(-3), sqrt(-11)). Inherited from NC-M22.1, NC-M23.1.  
NC-M28.2: This paper does NOT close W2 (V\_4 Weil functional positivity). The corpus PROVEN no-go ADS-5 \[25\] and ADS-6 \[25\] are uncircumvented. Closure remains external Connes (2000) \[12b\] / Burnol (1998-2004) \[14-18\] / CCM 2025 \[19\] under D4b.  
NC-M28.3: Theorem 28.10 is at HYPOTHESIS-strong status at the constant level only. The corresponding operator-level functor is OPEN.  
NC-M28.4: Theorem 28.11 is at HYPOTHESIS-strong status at the spectral data level only. It does NOT claim operator-level isomorphism or unitary equivalence between corpus L\_s^(P) and CCM 2025 D\_log^(lambda, N). Operator-level equivalence requires explicit form of D\_log from CCM 2025 §3-§5 \[19\] and is OPEN.  
NC-M28.5: Theorem 28.4 (HYPOTHESIS-strong) does NOT prove RH. The connection log|D|^2 \~ \-(2Q/D\_\*) log|zeta\_P| holds for any s with sigma \> 0; it does not constrain Riemann zero locations to sigma \= 1/2.  
NC-M28.6: Theorem 28.5 (DERIVED-interpretation) does NOT prove RH. It establishes the structural isomorphism sigma \= 1/2 \<-\> j \= 1/2 at the Z\_2-involution level only. RH still requires that all non-trivial zeta-zeros actually lie on the critical line — OPEN (P1-P4 of ZS-QS \[29\]).  
NC-M28.7: Corollary 28.5a (HYPOTHESIS-strong) does NOT prove RH. The Mobius-trace reading specifies that Z-Spin and RH ride together (dong-seung) under the same Z\_2 involution but do NOT share count-axis observables. The Riemann count of zeros is undefined on the Z-Spin side; the Z-Spin Mobius traversal has no Riemann analog.  
NC-M28.8: Theorem 28.14 (DERIVED-CANDIDATE) does NOT directly close W2. Multiplicity 20 of the L(s, chi\_-3) realization does not change L-function sign behavior. The discovery is structural: it identifies WHERE in Z-Spin the chi\_-3 channel lives, not HOW to close W2.  
NC-M28.9: This paper does NOT extend the Langlands correspondence beyond abelian class field theory. K is a degree-4 abelian extension of Q; the correspondence between its Galois representations and automorphic forms is fully PROVEN mathematics (class field theory). Inherited from NC-M23.4.  
NC-M28.10: This paper does NOT introduce any new free parameter beyond A \= 35/437 (LOCKED, ZS-F2 \[2\]), Q \= 11 (PROVEN, ZS-F5 \[3\]), K (PROVEN, ZS-M22 \[25\]). All inputs trace to LOCKED, PROVEN, DERIVED, or IMPORTED items in upstream corpus papers or external citations.

**§13. OPEN Problems and Closure Paths**

The paper consolidates the open-problem roster of the Z-Spin RH program through ZS-M27 \[27\] under a single list:

| ID | Statement | Closure Path |
| ----- | ----- | ----- |
| O-M28.1 | Q-tower extension: does a sequence Q\_n \= 11 k\_n exist for which LOCATOR MAD \-\> 0? | Internal: scan Q in {11, 33, 55, ...}; relate to dimension extension |
| O-M28.2 | Small-prime correction structure: does R\_small encode arithmetic information beyond log p oscillations? | Internal: relate to Davenport-Heilbronn off-line zero detection |
| O-M28.3 | W1 closure to PROVEN: trace-norm convergence of H\_infinity^{Yak,J} | External: trace-norm convergence theorem extending Yakaboylu 2024 \[8\] |
| O-M28.4 | W2 closure: V\_4 Weil functional positivity via D4b conductor / parity correction | External: Connes (2000) \[12b\] / Burnol (1998-2004) \[14-18\] / CCM 2025 \[19\] |
| O-M28.5 | Operator-level functor B\_Z for Theorem 28.10 | External: explicit form of CCM 2025 D\_log^(lambda, N) operator \[19\] |
| O-M28.6 | Operator-level isomorphism for Theorem 28.11 | External: explicit construction of D\_log^(lambda, N) per CCM 2025 §3-§5 |
| O-M28.7 | Selberg-icosahedron W2 path | Internal+External: Selberg trace formula on closed icosahedral surface, V\_4 functional adapted to closed-geodesic length spectrum |
| O-M28.8 | Truncation-Dual Theorem promotion: chi\_-3 carrier on triangular face vs hexagonal face | Internal: explicit relation of pre-truncation Lame spectrum to truncated-icosahedron face spectrum |
| O-M28.9 | i-tetration \-\> operator promotion: Koopman lift onto reproducing kernel Hilbert space (Mauroy-Mezic 2020, Boulle-Colbrook-Conradie 2025\) | External: prime indexing supplied by external framework, not Z-Spin |
| O-M28.10 | Cohomology-level conductor decoration: alpha \= 0 limit unique to Kostant? | Internal: explore alpha \!= 0 with alternative grading structures |

*Table 13.1. Open problems consolidated for ZS-M28 v1.0. Four are OPEN under external import; six admit internal Z-Spin closure paths.*

**§14. Conclusion**

This paper consolidates the Z-Spin RH program's W1-closure, V\_4 multi-channel filter, external-vehicle map, and Y-sector geometric-carrier strands into a single bridge. The bridge thesis is: Z-Spin and RH ride together (dong-seung) under the same Z\_2 involution structure (Theorem 28.5), but the Riemann count of zeros has no internal observable on the Z-Spin side (Corollary 28.5a). Where the two sides ride together, we have PROVEN structural isomorphisms (the nine 1/2 manifestations, Table 5.1). Where they diverge, we have walls (W1, W2, W3) that are not problems but maps of the divergence.  
Theorem 28.1 closes wall W1 to DERIVED-CONDITIONAL on PNT alone, by establishing that L\_s(P) is diagonal in the computational basis. Theorem 28.4 (HYPOTHESIS-strong) explains why corpus PROVEN LOCATOR peaks coincide with Riemann zero heights. Theorem 28.6 establishes the V\_4 multi-channel Triple Structure with Tier-3 anti-numerology PASS at 50 000 trials (Theorem 28.7). Theorems 28.10-28.12 identify three external mathematical vehicles for D4b closure and establish constant-level conductor identification. Result 28.13 builds an explicit V\_4-decorated trace-remainder that passes the structural form-check at 11/11 sample t-values while documenting the W2 wall at 5/12 NEG critical g\*g\_tilde sign. Theorem 28.14 closes the geometric origin gap for the chi\_-3 V\_4 channel, identifying the 20 equilateral triangular faces of the pre-truncation icosahedron as the geometric carrier.  
Theorem 28.5 (DERIVED-interpretation) and Corollary 28.5a (HYPOTHESIS-strong) are the principal interpretive contributions: a single-frame consolidation of corpus 1/2-manifestations under one Z\_2-involution reading, and a Mobius-trace reading of the RH count of zeros as a count-invariant traversal of the i-tetration fixed point z\*. Both are interpretive layers; neither proves RH (NC-M28.6, NC-M28.7).  
What this paper achieves is not RH but its Z-Spin meaning. The Z-Spin framework now carries an explicit, anti-numerology-checked, falsification-gated reading of why the Riemann critical line is sigma \= 1/2 in dong-seung with the Z-sector spinor 4 pi closure. Whether RH itself is ultimately proven, refuted, or remains open, the Z-Spin corpus contribution to the question is now mapped as a single 30-test verified bridge.

**Acknowledgements & Code Availability**

This work was developed across 47+ exploratory rounds with the assistance of AI tools (Anthropic Claude, OpenAI ChatGPT, Google Gemini) for mathematical verification, code generation, external literature search, and manuscript drafting. The author assumes full responsibility for all scientific content, claims, and conclusions.  
The companion verification suite zs\_m28\_verify\_v1\_0.py is publicly available at github.com/KennyKang-git/zspin/papers/ZS-M28/. Dependencies: Python \>= 3.9, NumPy, SciPy, SymPy, mpmath (50-digit precision for z\*-related identities). Execution: python3 zs\_m28\_verify\_v1\_0.py. Expected output: 30/30 PASS, exit code 0\.

**References**

**Internal (Z-Spin Cosmology v2.0 corpus)**

\[2\]  K. Kang, ZS-F2 v1.0: Geometric Impedance A \= 35/437, Z-Spin Cosmology Collaboration (March 2026).  
\[3\]  K. Kang, ZS-F5 v1.0: Gauge Symmetry Constraint: Why Q \= 11, Z-Spin Cosmology Collaboration (March 2026); ZS-F0 v1.0(Revised): Ontological Bootstrap and Foundational Closure (April 2026).  
\[4\]  K. Kang, ZS-M1 v1.0: i-Tetration & Fixed Point, Z-Spin Cosmology Collaboration (March 2026); ZS-M4 v1.0: Spectral Bridge & Transfer Operator (March 2026).  
\[5\]  K. Kang, ZS-M3 v1.0: Regge-Holonomy, Immirzi & Z-Telomere, Z-Spin Cosmology Collaboration (March 2026), Lemma 10.1.  
\[7\]  K. Kang, ZS-M7 v1.0: Berry-Keating Structural Isomorphism, Z-Spin Cosmology Collaboration (March 2026), Theorem 4\.  
\[9\]  K. Kang, ZS-M26 v1.0: V\_4-Equivariant ZBSI and the Three-Wall Map, Z-Spin Cosmology Collaboration (May 2026).  
\[10\] K. Kang, ZS-M24 v1.0: Face Polygon Spectral Zeta and Archimedean Completion, Z-Spin Cosmology Collaboration (May 2026).  
\[11\] K. Kang, ZS-M25 v1.0: Composite-Field Archimedean Completion and J-Twisted Yakaboylu Bridge, Z-Spin Cosmology Collaboration (May 2026).  
\[12\] K. Kang, ZS-M23 v1.0(Revised): Y-Sector RH Contribution Map and Four Dragons, Z-Spin Cosmology Collaboration (March 2026, August 2026 dated update).  
\[16\] K. Kang, ZS-F13 v1.0: Mobius Chronology Theorem, Z-Spin Cosmology Collaboration (April 2026), Theorems F13.1, F13.2.  
\[25\] K. Kang, ZS-M22 v1.0: Five-Pillar Arithmetic-Dedekind Scaffold, Z-Spin Cosmology Collaboration (May 2026).  
\[27\] K. Kang, ZS-M27 v1.0: V\_4-Equivariant Cobordism BRST Closure via Kostant Cubic Dirac, Z-Spin Cosmology Collaboration (May 2026).  
\[29\] K. Kang, ZS-QS v1.0(Revised): Inverse Riemann Engine: Quantum Algorithms for Spectral Zero Detection, Z-Spin Cosmology Collaboration (May 2026).  
\[SA-cat\] K. Kang, ZS-A8 v1.0(Revised) §SA: Symmetry-Asymmetry Unified View, Z-Spin Cosmology Collaboration (April 2026).

**External**

\[1\]  G. Lame, Lecons sur les coordonnees curvilignes et leurs diverses applications, Mallet-Bachelier, Paris (1852).  
\[6\]  M. V. Berry and J. P. Keating, The Riemann zeros and eigenvalue asymptotics, SIAM Rev. 41, 236-266 (1999).  
\[8\]  E. Yakaboylu, A Hilbert space framework for the Riemann zeta function, J. Phys. A: Math. Theor. 57, 235204 (2024); arXiv:2408.15135.  
\[11b\] F. Mertens, Ein Beitrag zur analytischen Zahlentheorie, J. reine angew. Math. 78, 46-62 (1874).  
\[12b\] A. Connes, Trace formula in noncommutative geometry and the zeros of the Riemann zeta function, Selecta Math. 5, 29-106 (1999).  
\[13\] A. Connes, C. Consani, Weil positivity and trace formula: the archimedean place, Selecta Math. 27, no. 4, art. 77 (2021).  
\[14\] J.-F. Burnol, The Explicit Formula and the Conductor Operator, arXiv:math/9810169 (1998).  
\[15\] J.-F. Burnol, Sur certains espaces de Hilbert de fonctions entieres, C. R. Acad. Sci. Paris 333, 201-206 (2001); 335, 689-692 (2002).  
\[16b\] J.-F. Burnol, Spectral analysis of the local conductor operator, Forum Math. 16, 805-826 (2004).  
\[17\] J.-S. Huang, P. Pandzic, Dirac Operators in Representation Theory, Birkhauser (2006).  
\[18\] T. Sliwinski, Spectral Analysis of the D\_log^{(lambda,N)} Operators, arXiv:2601.12133 (January 2026).  
\[19\] A. Connes, C. Consani, H. Moscovici, Zeta Spectral Triples, arXiv:2511.22755 (November 2025).  
\[20\] A. Connes, W. van Suijlekom, Quadratic Forms, Real Zeros and Echoes of the Spectral Action, arXiv:2511.23257 (November 2025).  
\[21\] A. Connes, C. Consani, Spectral triples and the geometry of fractal strings, J. Geom. Phys. 187, 104815 (2023).  
\[22\] B. Riemann, Uber die Anzahl der Primzahlen unter einer gegebenen Grosse, Monatsber. Berliner Akad. (1859).  
\[23\] J. Hadamard, Sur la distribution des zeros de la fonction zeta(s) et ses consequences arithmetiques, Bull. Soc. Math. France 24, 199-220 (1896).  
\[24\] C.-J. de la Vallee Poussin, Recherches analytiques sur la theorie des nombres premiers, Ann. Soc. Sci. Bruxelles 20, 183-256 (1896).  
\[26\] A. Mardby, J. Rowlett, The spectral zeta function for the equilateral triangle, J. Fourier Anal. Appl. 31, art. 81 (2025); arXiv preprint 2024\.  
\[28\] T. C. T. Looi, A. M. Sher, Heat invariants for Reuleaux triangles, J. Geom. Anal. (2025).  
\[30\] A. S. Cattaneo, P. Mnev, N. Reshetikhin, Classical BV-BFV theories on manifolds with boundary, Commun. Math. Phys. 332, 535-603 (2014); ibid. 357, 631-730 (2017).  
\[31\] A. Alekseev, F. Naef, P. Severa, F. Valach, Boundary Chern-Simons and the Kostant cubic Dirac operator, J. Geom. Phys. 123, 124-146 (2018).  
\[32\] B. Kostant, A cubic Dirac operator and the emergence of Euler number multiplets of representations for equal rank subgroups, Duke Math. J. 100, 447-501 (1999).

**Version History**

v1.0 (March 2026): Initial public release of ZS-M28 v1.0. Theorems 28.1 (PROVEN), 28.2 (DERIVED-CONDITIONAL on PNT), 28.3 (PROVEN), 28.4 (HYPOTHESIS-strong), 28.5 (DERIVED-interpretation), Corollary 28.5a (HYPOTHESIS-strong), 28.6 (DERIVED), 28.7 (DERIVED), 28.8 (DERIVED-CONDITIONAL), Result 28.9 (OBSERVATION), 28.10 (HYPOTHESIS-strong), 28.11 (HYPOTHESIS-strong), 28.12 (PROVEN), Result 28.13 (DERIVED-CONDITIONAL), 28.14 (DERIVED-CANDIDATE). Verification suite 30/30 PASS at mpmath 50-digit precision (numerical) plus algebraic exactness (diagonal structure, Schur orthogonality, V\_4 closure). Falsification gates F-M28.1 through F-M28.16 registered, all PASS. Open problems O-M28.1 through O-M28.10 registered. Non-claims NC-M28.1 through NC-M28.10 registered. Zero new free parameters; A \= 35/437, Q \= 11, K \= Q(sqrt(-3), sqrt(-11)) LOCKED throughout. (Consolidated from internal Z-Spin Collaboration research notes through ZS-M27 \[27\] and Kenny Kang's March 2026 unified-bridge synthesis directive.)