# ZS-M74 v1.1.1

# Population-only sign identifiability of two-branch Hamiltonians

## Generic graph classification, sharp witness order, finite certificates, and correlated redundant records

**Version:** 1.1.1, 27 September 2026 (KST). **Language:** English. **Form:** RESEARCH PAPER, project-internal; FREEZE READY / TERMINAL-IN-SCOPE recommended, neither submitted nor published. **Code:** ZS-M74. **Lineage:** seed v1.1–v1.3 → paper v1.0 → paper v1.1 → this correction-only release. The attached v1.1 manuscript (SHA-256 90264dcc7e0577346aa578e030b4998d0231ec083e67681321432f8c90a95dbf), complete package and Claude audit evidence are preserved unchanged in provenance.

| Release field | Current statement |
|---|---|
| Central mathematical contribution | Theorem M: generic population blindness on independent mixed real/free-complex supports iff $\mathrm U_*\lor\mathrm A_*$, decidable in linear graph time; Theorem J: the witness order $2d$ is optimal; the constructive witness calculus of §5 |
| Fixed and tied models | Theorem S: exact merged-frequency criterion; Theorem F: derivatives through $2d(d-1)$ suffice for any fixed pair; Corollary T: a finite polynomial certificate for tied polynomial families |
| Operational extension | Theorem Q: a coefficient gives an explicit finite-time signal and perturbation budget; Theorem R: history-uniform error bounds give stochastic domination and exponentially reliable majority decoding despite interactions |
| Corrections integrated | All v1.1 repairs retained; F12-01 separates the known matrix locator from its mixing theorem; F12-02 distinguishes author assessment from the H-0421 cross-lineage review; F12-03 supplies the correct L/V-dependent path gauges |
| Verification scope | The unchanged v1.1 18-row mathematical suite is rerun; the v1.1.1 regression ledger separately checks coloured-path gauges, jets, mixed parity and the two previously declared operational claims. The supplied auditor scripts are replayed with declarations excluded from calculated-evidence counts. Final run details are in §13 and the freeze report |
| Grade / role | Research grade **4 maintained**, project-internal and restricted to M/J and the constructive witness calculus. H-0421 supplies the cross-lineage assessment; this correction-only review checks its continued applicability. Qualification PASS; SUPPORT/METHOD for FQ2/RQ3, no CORE promotion |
| Review status | v1.0: frozen AUDIT-MAJOR-REVISION. v1.1: Claude AUDIT-PASS-MINOR, S1=3, S0=3, S2+=0, as recorded in H-0421. v1.1.1: correction-only integration and post-write verification by Codex/GPT; no new independent full-audit claim. qualified-human anchor: NONE |
| Physical realization | OPEN: action-derived carrier, physical instrument, selected reference/control state, single events, Born weights and identification of clocks |

## Abstract

For two finite Hermitian Hamiltonians $H_\pm=L\pm V$, we determine when the branch sign is detectable using only configuration preparations and population readouts. On a connected support whose allowed real entries and real and imaginary parts of complex entries are independent, generic blindness holds exactly under one of two graph conditions: switching balance $\mathrm U_*$, or conjugation balance $\mathrm A_*$. The latter additionally requires all free-complex edges to be bridges. A spanning-tree and bridge algorithm decides the alternatives in $O(d+|\mathcal E|)$. When neither holds, a walk-interference coefficient of order at most $2d$ is a nonzero polynomial; an endpoint-detuned path attains this bound for every matrix entry. The proof includes explicit real odd–odd and complex odd–even dumbbell witnesses.

Fixed matrices need not satisfy either gauge condition: a known skew-conference $K_4$ signing gives an exact exception to an unconditional propagator-gauge necessity statement. Merged Bohr frequencies give the exact fixed-pair criterion. We further prove that derivatives through order $2d(d-1)$ suffice, and convert this into a polynomial identity test for tied finite-dimensional families. A Taylor remainder and a perturbation estimate turn any nonzero coefficient into a finite-time signal certificate, while showing why topology alone gives no uniform signal strength.

For sequential interacting dual-rail writes, the final population law is exactly an adapted history chain. A uniform conditional error envelope $p_*=\alpha^2/(4w^2)<1/2$ implies stochastic domination by independent Bernoulli errors and majority error at most $[4p_*(1-p_*)]^{R/2}$; thus $\alpha<\sqrt2w$ is sufficient even though actual records may be correlated. Passive-bus resource inequalities, an active qubus construction and robust writing schedules are retained with explicit domains. Reference costs are stated relative to a named group: logical dual-rail rotations conserve total charge but need not respect independent rail phases. Direct connections to Repo1 distinguish mathematical transport, observable access, subsystem realization and instrument selection. No physical realization from the Z-Spin action is claimed.

## 1. Question, contract and contribution

### 1.1 Three questions with different inputs

The support problem asks whether generic independent entries permit any population distinction; M/J solve it with a graph criterion and a sharp witness order. The fixed-pair problem asks whether particular matrices, including tied exceptional examples, are blind; S/F solve it by a finite algebraic test. The operational problem asks how much signal or decoding reliability follows from specified coefficients and controls; Q/R give sufficient quantitative certificates. These questions must not be interchanged. A graph decision is not parameter estimation, a nonzero polynomial is not a noise floor, and high trace-distance distinguishability is not automatically population distinguishability.

### 1.2 Exact contract

| Item | Assumptions and quantifiers |
|---|---|
| Space and observation | $\mathcal H=\mathbb C^d$ with fixed basis $\{\vert{}a\rangle\}$; $\hbar=1$; $M_H(t)_{ba}=\vert{}\langle b\vert{}e^{-itH}\vert{}a\rangle\vert{}^2$; blindness means $\Delta M=M_{H_+}-M_{H_-}=0$ for every $a,b,t$ |
| Independent family, M/J | Every allowed off-diagonal $L$ or $V$ entry is independently real or free complex; a complex entry has two independent real coordinates. Diagonal entries are independently real; componentwise scalar shifts are discarded. Generic means outside a proper real algebraic zero set |
| Fixed and tied families, S/F/T | Any fixed Hermitian pair for S/F. In T, entries are polynomials in shared real parameters of degree at most $m$, Hermitian on a nonempty open domain. No independence among entries is required |
| Components | The graph statement is applied separately to every connected component; different components may use different gauge types and scalar shifts; isolated vertices are blind |
| Record model | Initially unflipped dual rails, one active exchange window at a time, fixed real diagonal cross-couplings, and the specified resonance. Errors can depend on the entire prior history |
| Time and resources | M/J/S/F/T concern static matrices. B1 extends to time-dependent matrices with one fixed gauge. Q gives a calibrated finite-time bound; W and BUS-G have separately specified control schedules |
| Not derived | An action-selected subsystem, initial apparatus state, instrument or outcome rule; physically free controls; a uniform signal bound from graph topology; infinite-dimensional or thermodynamic uniformity from finite truncations |

### 1.3 Contribution and attribution

| Result | Contribution class | Proof and executable coverage | Closest baseline |
|---|---|---|---|
| B1, DUAL, C | Imported/specialized gauge mechanisms | §3; C01, historical checks | Signed/gain switching and conjugation |
| M and mixed witness calculus | Central classification contribution, originating in seed v1.3 | §§4–5; C02–C03, C08–C09; reconstructed proof | Cycle-gain switching is sufficient but does not characterize fixed population equality |
| J, sharp $2d$ | Central sharp-order contribution | §6; C04 | Short-time walk expansions; general observability is a different problem |
| S and $K_4$ application | Spectral specialization; known matrix used to separate fixed from generic claims | §7.1–7.2; C05–C07 | Biamonte–Turner; Levine et al. |
| Q | New integration of standard analytic bounds into the witness method | §6.1–6.2; V01 | Taylor tails, Duhamel stability, Bernoulli concentration |
| F/T | Refined finite certificate and tied-family consequence; elementary finite-exponential/polynomial methods | §7.3–7.4; C06–C07 | Finite observability and system-identification methods, not a new general identifiability principle |
| A/C/D | Elementary cross-parity identity and imported mode selection | §8 | Marvian–Spekkens; invariant-observable algebras |
| E/W and ARCH-1/2M | Declared-model write laws and error estimates | §§9–10.2; V02, V04–V05 | Two-level resonance and adiabatic bounds |
| R | New conditional envelope and decoding consequence for this interacting-write model | §10.4; C10, V03, W01 | Standard stochastic domination/Chernoff methods; no independence assumption on actual records |
| BUS-P/G | Applied Gram inequality and known qubus mechanism | §11; C11 | Schur/Gram positivity; conditional oscillator displacement |
| Corpus bridges | Typed conditional mappings, not new action derivations | §12; C12 and source map | Repo1 primary texts at specified versions |

The substantial external change is a complete generic decision procedure with a sharp certificate order for arbitrary finite mixed supports, together with explicit separation from nongeneric fixed-pair equivalence. The added finite, signal and decoding certificates make the method usable on tied parametrizations and on calibrated record architectures. Grade 4 rests on the classification and sharpness, not on treating standard inequalities as discoveries.

## 2. Model, symmetries and definitions

### 2.1 Observation model

For a Hermitian $H$ on $\mathbb C^d$ and the configuration basis, $M_H(t)_{ba}=\lvert\langle b\rvert e^{-itH}\lvert a\rangle\rvert^2$. Every diagonal preparation and diagonal effect gives a probability that is a convex combination of entries of $M_H(t)$, so the branches are indistinguishable by population data at time $t$ if and only if $\Delta M(t)=0$. Equality of a single return probability or of a single input row is strictly weaker (Section 3.3).

### 2.2 Configuration multigraph

Write $H_z=D_L+zD_V+W_L+zW_V$ with $D$ diagonal and $W$ off-diagonal. The multigraph $\Gamma$ has an $L$-edge where $(W_L)_{ab}\ne0$ and a $V$-edge where $(W_V)_{ab}\ne0$; a pair carrying both is an L/V digon. $\#L(C)$ and $\#V(C)$ count edge types on a cycle $C$; $\Phi_C=\arg\prod_C(H_+)_{\text{next},\text{cur}}$ is the flux of $H_+$ around $C$. All statements are per connected component; $d=1$ is blind.

### 2.3 Three symmetries

For a diagonal unitary $g$ and a real $c$:
$$
\mathrm U:\ gH_+g^\dagger=H_-+cI,\qquad
\mathrm A:\ gH_+g^\dagger=-\overline{H_-}+cI,\qquad
\mathrm C:\ gH_+g^\dagger=-H_-+cI. \tag{2.1}
$$
For pure-sign supports (no digon), with (2.1) read entrywise and multiplied around cycles,
$$
\mathrm U\iff D_V\ \text{scalar on the component and }\#V(C)\ \text{even for all }C;\qquad
\mathrm A\iff D_L\ \text{scalar and }e^{2i\Phi_C}=(-1)^{\#L(C)}\ \text{for all }C. \tag{2.2}
$$
(C) holds iff $D_L$ is scalar and $\#L(C)$ is even for all $C$, independently of fluxes. In the real class (C) coincides with (A).

### 2.4 Structural conditions for the independent family

| Condition | Requirements on the support |
|---|---|
| $\mathrm U_*$ | no L/V digon; no non-constant $D_V$ freedom; every cycle has an even number of $V$-edges |
| $\mathrm A_*$ | no L/V digon; no non-constant $D_L$ freedom; every cycle has an even number of $L$-edges; every free-complex edge is a bridge |

"Non-constant $D_V$ freedom" means an allowed branch-odd diagonal at some but not all vertices, or at all vertices with independent values (a uniform $D_V$ is $cI/2$ and is removed). A bridge is an edge whose removal disconnects the component.

### 2.5 Physical symmetry groups (for Sections 8–11)

Within one total-charge sector the two configurations of a dual rail carry total-$U(1)$-invariant information; requiring independent $U(1)$ per rail as a free symmetry would forbid the exchange itself. The record models assume total-charge-conserving control. A diagonal unitary is a basis-phase redefinition that fixed preparations and readouts cannot see; it does not mean that fluxes, timings or control phases are free in a device.

## 3. Sufficiency, duality and the return-only symmetry

### 3.1 Theorem B1 (sufficiency)

*If (U) or (A) holds on a component, then $\Delta M(t)=0$ on that component for all $t$. For time-dependent $H_z(t)$ the same holds if one fixed $g$ and one fixed type satisfy (2.1) at all times.*

*Proof.* Under (U), $H_-=gH_+g^\dagger-cI$, so $e^{-itH_-}=e^{+itc}\,g\,e^{-itH_+}g^\dagger$, so every amplitude acquires only start and end phases. Under (A), $H_-=-\bar g\,\overline{H_+}g^{\mathsf T}+cI$, so $e^{-itH_-}=e^{-itc}\,\bar g\,\overline{e^{-itH_+}}\,g^{\mathsf T}$, so amplitudes are conjugated; moduli are preserved. For time dependence, differentiate the propagator equation with the fixed $g$. A $g(t)$ chosen separately at each time adds a gauge term and is not sufficient (seed v1.1, row W04). $\square$

The combinatorial forms (2.2) are the switching/balance criteria of signed and gain graphs applied to the pair (Zaslavsky; Reff Lemma 1.1; Kadyan–Bhattacharjya Theorem 2.2). We do **not** claim (2.1) as a necessary condition for a fixed matrix pair (Section 7).

### 3.2 Lemma DUAL (real-part duality)

For any Hermitian $H$, $M_H(t)=M_{-\overline H}(t)$. Hence the pair $(L,V)$ has the same population statistics as
$$
(L',V')=(\operatorname{Re}V+i\operatorname{Im}L,\ \operatorname{Re}L+i\operatorname{Im}V), \tag{3.1}
$$
since $H'_+=H_+$ and $H'_-=-\overline{H_-}$. In the real class this swaps $L$ and $V$; it exchanges (U) and (A) with the same $c$ and swaps $D_L\leftrightarrow D_V$.

### 3.3 The return-only symmetry (C)

*If (C) holds then $M_{H_+}(t)=M_{H_-}(t)^{\mathsf T}$; in particular all return probabilities coincide.* Indeed $\langle b\rvert e^{-itH_+}\lvert a\rangle=\langle b\rvert e^{-itc}g^\dagger e^{itH_-}g\lvert a\rangle$ and $\lvert\langle b\rvert e^{itH_-}\lvert a\rangle\rvert=\lvert\langle a\rvert e^{-itH_-}\lvert b\rangle\rvert$. In the complex class (C) does not imply full blindness; it implies that every witness on a (C)-symmetric substructure must be a transfer probability, never a return probability. A test that looks only at return probabilities on even $L$-cycles is designed to fail.

## 4. Theorem M: complete generic classification

> **Theorem M.** Let $\Gamma$ be a connected support on $d\ge2$ vertices in the independent family of Section 1.2. Then $\Delta M(t)\equiv0$ for generic parameters if and only if $\mathrm U_*\lor\mathrm A_*$. If both fail, there exist $a,b$ and $k\le2d$ such that $[t^k]\Delta M_{ba}(t)$ is a non-zero real polynomial in the independent entries; hence the sign is visible for almost every value. Deciding $\mathrm U_*\lor\mathrm A_*$ takes $O(d+\lvert\mathcal E\rvert)$ (bridge search and two $\mathbb Z_2$ balance checks).

The complexity statement concerns the decision on the support, not the estimation of couplings or the size of the signal.

### 4.1 Sufficiency

If $\mathrm U_*$ holds, give $V$-edges the sign $-1$ and $L$-edges $+1$; the product around every cycle is $1$, so vertex signs defined on a spanning tree extend consistently and give (U). If $\mathrm A_*$ holds, all cycle edges are real with even $\#L$, so the required gauge ratios multiply to $1$ around every cycle; the phase of a free-complex bridge is absorbed into the relative gauge of the two sides. Special zero values are included by continuity. $\square$

### 4.2 Necessity — real specialization

Set the imaginary coordinates of all free-complex entries to zero. A nonzero coefficient at any such specialization proves that the full real polynomial is not identically zero; the witness is allowed to set unused edges to zero, even when generic entries on the declared support are nonzero. Assume first that the resulting real family violates both U and A. A digon already gives T1, so suppose there are no digons.

Call a $D_V$ freedom or a $V$-odd cycle a V-obstruction, and a $D_L$ freedom or an $L$-odd cycle an L-obstruction. Both types exist. If both diagonal types exist, retain a shortest path between their vertices. Distinct endpoints give (5.2) with $a=b=1$; if both freedoms are at the same vertex, keep any incident edge and use T4. Connectivity and $d\ge2$ guarantee that edge. A scalar diagonal freedom alone is excluded by definition.

If one obstruction is a diagonal and the other a cycle, retain a shortest path from the diagonal to that cycle. If the cycle has both odd parities it is an even real T2 and already suffices. Otherwise it is an odd cycle of the opposite obstruction type; the retained lollipop is (5.2), with one length equal to one. The case with L and V interchanged is covered by DUAL.

If both obstructions are cyclic, choose a spanning tree. Cycle parity is a linear functional over the binary cycle space, so each failed balance is witnessed by a fundamental cycle. Label a cycle by $(\#V,\#L)\bmod2$. A fundamental cycle of label $(1,1)$ gives real T2. If none exists, there are fundamental cycles of labels $(1,0)$ and $(0,1)$. Their tree paths intersect in either an empty set, one vertex, or a path with an edge. In the last case the symmetric difference is a simple cycle with label $(1,1)$, hence T2. A single-vertex intersection gives an odd–odd figure eight. Disjoint cycles, joined by the unique shortest tree path, give an odd–odd dumbbell. Formula (5.2) handles both. This exhausts the real case without invoking an unproved reduction in a seed report.

### 4.3 Necessity — the mixed case

In the remaining case every cycle is $L$-even, there is no non-scalar $D_L$ freedom, and (A) fails only because some free-complex edge lies on a cycle; (U) fails because of a $D_V$ or a $V$-odd cycle. Choose a simple cycle $C_e$ containing a free-complex edge $e_c$ and a spanning tree containing $C_e\setminus\{e_c\}$, so $C_e$ is fundamental. If $C_e$ is $V$-odd, it is a complex T2 with a generic flux (transfer witness). Otherwise $C_e$ is $V$-even and $L$-even, hence of even length. If a $D_V$ exists, keep the shortest path from it to $C_e$: formula (5.4) is a witness for every cycle length and tail length. If there is no $D_V$, take a $V$-odd fundamental cycle $C_f$; if it contains a free-complex edge it is a complex T2; otherwise $C_f$ is real, $L$-even and of odd length. If $C_e$ and $C_f$ share an edge, the shared segment lies in the real cycle $C_f$, so the symmetric difference is a $V$-odd simple cycle that still contains $e_c$: complex T2. If they share only a vertex or are disjoint, the substructure is a real-odd/complex-even figure eight or dumbbell, and formula (5.3) is a non-zero transfer witness. $\square$

### 4.4 Decision algorithm and disconnected supports

In each component, reject both alternatives at once if an L/V digon occurs. Otherwise label every edge by its V-parity and run a binary potential assignment on a spanning tree; any inconsistent non-tree edge fails the V-balance test. Repeat with L-parity. A depth-first low-link computation finds all bridges. U* is the V-balance test plus absence of a non-scalar branch-odd diagonal freedom; A* is the L-balance test plus absence of a non-scalar branch-even diagonal freedom and absence of any free-complex non-bridge edge. Each pass visits each vertex and edge a bounded number of times.

The whole graph is generically blind iff **each component** satisfies at least one alternative. It is not necessary for every component to choose the same alternative, because amplitudes between components vanish and componentwise scalar phases are unobservable. A one-vertex component is always blind, whatever its scalar energy. The released classify_support function implements precisely this decision; C08 checks a disconnected combination where one component uses U and another A. Constructing or simplifying all witness polynomials is a separate task and is not included in the linear-time complexity assertion.

## 5. Exact leading-order witnesses

Split the transition amplitude into $V$-even and $V$-odd walk sums, $A_z=\alpha+z\beta$; then
$$
\Delta P=4\operatorname{Re}(\alpha\overline\beta). \tag{5.1}
$$
All coefficients come from walk sums of $H^k$ divided by $k!$; other entries of the support are set to zero.

### 5.1 Basic witnesses

| Substructure | Non-zero coefficient |
|---|---|
| T1: one edge carrying $l+zv$ | $\Delta P_{\rm transfer}=4\operatorname{Re}(l\bar v)\,t^2+O(t^4)$ |
| T2: $V$-odd cycle of length $n$, adjacent input/output | $\dfrac{4}{(n-1)!}\operatorname{Re}\!\big[i(-i)^{n-1}\Omega_C\big]t^n$, with $\Omega_C=\overline{(H_+)_{ba}}\cdot\prod_{\text{long way }a\to b}(H_+)_{\text{next},\text{cur}}$; zero iff $e^{2i\Phi_C}=(-1)^{\#L(C)}$ |
| T4 ($k=0$): $\epsilon+z\chi$ at one vertex, neighbouring edge $w$ | $\Delta P_{\rm return}=\tfrac13\epsilon\chi\lvert w\rvert^2t^4+O(t^6)$ |

The orientation convention for $\Omega_C$ matters for odd $n$ (the other orientation flips the sign); it is fixed as written. In the real class the T2 coefficient is non-zero exactly when $n$ is even, i.e. $\#L$ odd; with a free-complex edge the flux can be chosen to make it non-zero for every $n$.

### 5.2 Odd–odd dumbbell (unified form of T3, T4, T5, T6)

Let the first object be a real cycle of odd length $a$ with $\#V$ odd and $\#L$ even (or, for $a=1$, a branch-odd diagonal $\chi$), the second a real cycle of odd length $b$ with $\#V$ even and $\#L$ odd (or, for $b=1$, a branch-even diagonal $\epsilon$), joined by a path of $\ell$ edges; return at the junction on the first object. With $\mu_i=2\prod_{C_i}w_e$ for real cycles, $\mu_1=\chi$, $\mu_2=\epsilon$ for loops of length one, $W_P=\prod_{\rm path}\lvert w_e\rvert^2$ and $N=a+b+2\ell$,
$$
\Delta P_{00}(t)=4(-1)^{N/2}\mu_1\mu_2W_P\left[\frac{2}{N!}-\frac{1}{a!\,(b+2\ell)!}\right]t^N+O(t^{N+2}). \tag{5.2}
$$
*Proof.* Real return probabilities are even in $t$; a term odd in the sign and even in total length must contain both odd objects, so the minimal order is $N$. The interference of the constant amplitude with the order-$N$ amplitude has two orderings of the two objects and multiplicity $\mu_1\mu_2$, giving $8(-1)^{N/2}\mu_1\mu_2W_P/N!$; the interference of the order-$a$ and order-$(b+2\ell)$ amplitudes gives $-4(-1)^{N/2}\mu_1\mu_2W_P/[a!(b+2\ell)!]$. Backtracks or repeated loops violate the minimal length or the parity requirements. The bracket vanishes iff $\binom Na=2$, impossible except for the excluded single-vertex scalar case. $\square$ The case $\ell=0$ with two distinct nontrivial cycles is the figure eight; a length-one object may instead lie at the other cycle's junction. The combination $a=b=1,\ell=0$ is a single scalar vertex and is excluded; if both diagonals occur at one vertex of a larger graph, use T4. For $a=b=1,\ell=d-1\ge1$, the formula gives (6.1).

### 5.3 Odd–even mixed dumbbell

Let the first object be as above (real odd cycle of length $a\ge3$ with $\#V$ odd, or a branch-odd diagonal for $a=1$), the second an even cycle of length $b\ge4$ with $\#V$ and $\#L$ even carrying a free flux $\Phi$ (defined by $\Phi=\arg(\overline S\,T)$, where $S$ is the direct junction-to-neighbour amplitude and $T$ the product along the other side of the second cycle in that same direction), joined by a path of $\ell\ge0$ edges; start at the first junction, read at the neighbour of the second junction adjacent to the flux edge. Put $p=\ell+1$, $q=\ell+b-1$, $N=a+p+q$, $W_2=\prod_{C_2}\lvert w_e\rvert$. Then
$$
\Delta P_{\rm end\leftarrow start}(t)=4\mu_1W_PW_2(-1)^{(a+b-3)/2}\left[\frac{1}{p!\,(a+q)!}-\frac{1}{q!\,(a+p)!}\right]\sin\Phi\;t^N+O(t^{N+2}). \tag{5.3}
$$
*Proof.* One branch-parity class of walks from start to end has lengths $p$ and $q$; the opposite-parity walks, which wind the first object once, have lengths $a+p$ and $a+q$. Interferences that use the same second-cycle path have zero real part because $a$ is odd and the first object is real. The two remaining pairs carry opposite phase factors $(-1)^{(a+b-3)/2}\sin\Phi$ and factorials $p!(a+q)!$, $q!(a+p)!$; the branch difference and conjugate pair give the factor 4. Since $q>p$ and $a>0$, $(x+a)!/x!$ is strictly increasing, so the bracket is non-zero. The complete retained substructure has no branch-even diagonal and all its cycles are L-even, so symmetry (C) holds. Hence $\Delta M(t)=M_{H_+}(t)-M_{H_+}(-t)$ is odd in time; the error is $O(t^{N+2})$. This also avoids assuming that the path itself has even V-parity. $\square$

For $a=1$ this closes the complex even-cycle case left open in v1.2:
$$
\Delta P=\frac{4(-1)^{b/2}(b-2)}{(\ell+2)!\,(\ell+b)!}\,\chi\,W_PW_2\sin\Phi\;t^{b+2\ell+1}+O(t^{b+2\ell+3}), \tag{5.4}
$$
which at $\ell=0$ gives $2(-1)^{b/2}(b-2)\chi W_2\sin\Phi/b!$, the coefficients $1/6,-1/90,1/3360$ for $b=4,6,8$ found in v1.2. Mixed $L/V$ colourings of the path and cycles with the stated parities give the same formulas. Verification: v1.3 checked 22 weighted and mixed cases in exact arithmetic; the v1.0 audit checked six further cases $(a,b,\ell)\in\{(3,4,0),(3,8,1),(5,6,1),(1,10,0),(1,4,3),(7,4,0)\}$ (its row C01) and its referee seven more, as historical exact-arithmetic evidence. Current C03 checks the additional cases listed in §13.

## 6. Theorem J: the sharp order $2d$

> **Theorem J.** In the setting of Theorem M, if $\mathrm U_*$ and $\mathrm A_*$ both fail then some entry of $\Delta M$ has a non-zero coefficient of order $\le2d$. The bound is attained: on a $d$-vertex path ($d\ge2$), with each edge assigned exclusively to $L$ or $V$ and nonzero real hoppings $w_0,\dots,w_{d-2}$, nonzero branch-odd diagonal $\chi$ at one end and nonzero branch-even diagonal $\epsilon$ at the other, every entry of $\Delta M$ vanishes below order $2d$ and
$$
[t^{2d}]\Delta M_{00}=\frac{8(d-1)(-1)^{d-1}}{(2d)!}\,\chi\,\epsilon\prod_{j=0}^{d-2}w_j^2\ \ne0. \tag{6.1}
$$

*Proof.* Upper bound: each witness of Section 5 has order at most twice the number of vertices it uses (T1: 2 on 2; T2: $n$ on $n$; (5.2): $N=a+b+2\ell\le2(a+b+\ell-1)$; (5.3): $N=a+b+2\ell\le2(a+b+\ell-1)$, and with $a=1$, $N=b+2\ell+1\le2(b+\ell)$), and a sub-support has at most $d$ vertices. For the lower-bound construction take $d\ge2$ and assign each path edge exclusively to $L$ or $V$, with real nonzero hopping $w_j$; the only diagonal entries are $V_{00}=\chi$ and $L_{d-1,d-1}=\epsilon$. Define vertex signs recursively from $u_0=a_0=1$ by
$$
u_{j+1}=\begin{cases}u_j,&j\text{ is an }L\text{-edge},\\-u_j,&j\text{ is a }V\text{-edge},\end{cases}
\qquad
a_{j+1}=\begin{cases}-a_j,&j\text{ is an }L\text{-edge},\\a_j,&j\text{ is a }V\text{-edge}.\end{cases}
$$
Put $g_U=\operatorname{diag}(u_j)$ and $g_A=\operatorname{diag}(a_j)$. When $\chi=0$, $g_UH_+g_U^\dagger=H_-$; when $\epsilon=0$, $g_AH_+g_A^\dagger=-H_-$, which is (A) because the matrices are real. These statements follow edge by edge and include every L/V colouring. The special choices $g_U=I$ and $a_j=(-1)^j$ apply to the all-$L$ path only. Thus every coefficient polynomial is divisible by both $\chi$ and $\epsilon$. A contributing pair of walks with the same endpoints combines into a closed walk visiting both ends of the path. It traverses each of the $d-1$ edges at least twice and contains the two diagonal steps, so its total degree is at least $2d$. Homogeneity of the order-$k$ coefficient now gives all-entry vanishing for $k<2d$. Each path-edge sign occurs an even number of times in the minimal return walk; (5.2) with $a=b=1$, $\ell=d-1$ gives (6.1) for every colouring. $\square$

The theorem, coefficient and sharp order are unchanged. F12-03 corrects the displayed gauges and makes the path's exclusive edge assignment explicit. The original C04 checks all lower-order entries for the all-$L$ path at $d=2,\ldots,6$; the v1.1.1 R01/R02 regressions check every L/V colouring at $d=2,\ldots,6$ (62 coloured paths) with exact arithmetic and signed, unequal weights. Finite regressions supplement the preceding arbitrary-$d$ proof. The packaged historical checks also include paths through $d=8$.

### 6.1 Theorem Q — a finite-time signal and robustness certificate

Let a particular transition of a fixed pair have first nonzero coefficient $c_r=[t^r]\Delta M_{ba}\ne0$. Choose scalar shifts of each Hamiltonian so that $\|H_\pm\|\le h$, with $h>0$; these shifts do not change population data. For $t\ge0$,
$$
|\Delta M_{ba}(t)-c_rt^r|
\le \frac{2e^{2ht}(2ht)^{r+1}}{(r+1)!}. \tag{6.2}
$$
Consequently, define
$$
t_*=\min\left\{\frac1{2h},
\frac{|c_r|(r+1)!}{4e(2h)^{r+1}}\right\}.
\quad 0<t\le t_*\ \Longrightarrow\
|\Delta M_{ba}(t)|\ge\frac{|c_r|t^r}{2}. \tag{6.3}
$$
For perturbed static Hamiltonians $\widetilde H_z=H_z+D_z$, put
$\varepsilon_z=\inf_{c\in\mathbb R}\|D_z-cI\|$. At the same time,
$$
|\Delta\widetilde M_{ba}(t)|
\ge \frac{|c_r|t^r}{2}-t(\varepsilon_++\varepsilon_-).
\tag{6.4}
$$
The right side is a useful visibility certificate only when positive.

*Proof.* With $P_a=|a\rangle\langle a|$ and $\mathcal L_z=-i[H_z,\cdot]$, the induced trace-norm bound $\|\mathcal L_z\|_{1\to1}\le2h$ gives
$|\operatorname{tr}P_b(\mathcal L_+^k-\mathcal L_-^k)(P_a)|\le2(2h)^k$.
The exponential-series tail is bounded by $2e^{2ht}(2ht)^{r+1}/(r+1)!$, proving (6.2). On the interval in (6.3), $e^{2ht}\le e$ and the tail is at most $|c_r|t^r/2$. For any input state, Duhamel's formula for the two channels bounds their output trace distance by $t\varepsilon_z$: the trace norm of a commutator is at most $2\varepsilon_z$, while trace distance includes $1/2$. An effect $0\le P_b\le I$ cannot increase trace distance. Apply the bound separately to the two branches and use the triangle inequality. $\square$

The estimate is deliberately conservative. It certifies a sign of contrast and a nonempty mathematical observation interval; it does not select an optimal experimental time. In particular, an order-$r>1$ signal can be overwhelmed by an $O(t)$ perturbation at very small times. A real experiment must check (6.4) at an accessible time and calibrate its preparation, readout and timing error separately.

### 6.2 Sampling cost and the absence of a topology-only signal floor

If the two calibrated Bernoulli probabilities of one transition are separated by $\gamma>0$, $N$ independently reset trials with a threshold at their midpoint have each conditional misclassification probability at most
$$
\exp(-N\gamma^2/2),\qquad
N\ge 2\gamma^{-2}\log(1/\delta)\ \Longrightarrow\ P_{\rm error}\le\delta .
\tag{6.5}
$$
Indeed, an error requires the empirical mean to deviate from its branch mean by at least $\gamma/2$; the usual Bernoulli exponential-moment argument gives the bound. These repeated trials are an assumption about experiments, not independence of the interacting memories in §10.

No positive uniform $\gamma$ follows from M/J and the support alone. Scale $V$ to $\eta V$ without deleting its allowed entries. For generic nonzero $\eta$, the support verdict is unchanged, whereas Duhamel gives
$\sup_{0\le t\le T}|\Delta M_{ba}(t)|\le2T|\eta|\|V\|$.
It tends to zero at every fixed $T$. Thus Q adds a parameter-dependent operational certificate rather than converting a derivative order into a universal sample bound. The short-time path expansions of Szigeti et al. [R5] are the relevant method baseline; the new use here is to attach this certificate to the branch-coloured witness calculus.

## 7. Fixed matrices: the $K_4$ exception and the exact criterion

### 7.1 The $K_4$ counterexample

Let
$$
A=\begin{pmatrix}0&1&1&1\\-1&0&-1&1\\-1&1&0&-1\\-1&-1&1&0\end{pmatrix},\qquad H=iA,\qquad A^2=-3I. \tag{7.1}
$$
Then $e^{-itH}=e^{tA}=\cos(\sqrt3t)I+\sqrt3^{-1}\sin(\sqrt3t)A$: every diagonal probability is $\cos^2(\sqrt3t)$ and every off-diagonal probability is $\sin^2(\sqrt3t)/3$. So $M_H(t)=M_H(t)^{\mathsf T}=M_{\overline H}(t)$ for all $t$ (time-symmetric). A diagonal gauge $g$ with $gHg^\dagger=-H$ would need $g_i\overline{g_j}=-1$ on every edge, contradicting the triangle $(0,1,2)$; and $H_{01}H_{12}H_{20}=-i$ is a gauge-invariant non-real cycle product, so $H$ is not gauge-equivalent to a real matrix. For every time with $\sin(\sqrt3t)\ne0$, a diagonal gauge of $U(t)$ to $U(t)^{\mathsf T}=U(t)^\dagger$ would require the same inconsistent edge ratios $-1$. At revival times $\sin(\sqrt3t)=0$, $U(t)=\pm I$ and the gauge equality is trivial. Thus no such equality can hold for all times, even if the diagonal gauge is allowed to vary with time. Biamonte–Turner (arXiv:1703.02542v2, §II, "The vanishing of the quantum probability current") state that $U(t)$ is time-symmetric if and only if such a $\Lambda$ exists, with the necessity argued in their Methods by passing from equal entrywise probabilities to a channel equivalence; (7.1) is an exact counterexample to that sentence read as an unconditional statement about a fixed Hamiltonian (their support-level theorems — bipartite support or absence of Aharonov–Bohm phases — are not affected). A signing diagonally gauge-equivalent to (7.1), through $g=\operatorname{diag}(-1,1,1,1)$, appears in Levine et al. (arXiv:2605.04414v2, §2, Fig. 2); its uniform mixing at $t=\pi/(3\sqrt3)$ is proved in §4, Claim 2; the matrix is not new, only its use here. The example is not stable: changing $A_{01}\to2$, $A_{10}\to-2$ gives $\Delta M_{2,0}=2t^3-\tfrac{19}{6}t^5+\dots$, consistent with Theorem M (the family is tied).

### 7.2 Theorem S (per-frequency criterion)

Let $H=\sum_\lambda\lambda E_\lambda$ be the spectral decomposition over distinct eigenvalues and $\circ$ the entrywise product. Define $B_H(\omega)=\sum_{\lambda-\mu=\omega}E_\lambda\circ\overline{E_\mu}$. Then
$$
M_H(t)=\sum_\omega e^{-i\omega t}B_H(\omega),\qquad M_{H_+}\equiv M_{H_-}\iff B_{H_+}(\omega)=B_{H_-}(\omega)\ \text{for every }\omega \tag{7.2}
$$
(absent gaps count as zero; equal gaps are merged first). *Proof:* spectral expansion and linear independence of finitely many distinct exponentials. $\square$ For time-reversal alone, $M_H-M_H^{\mathsf T}=-4\sum_{\omega>0}C_\omega\sin\omega t$ with $C_\omega=\sum_{\lambda_s-\lambda_r=\omega}\operatorname{Im}(E_r\circ\overline{E_s})$, so time symmetry is exactly $C_\omega=0$ for all $\omega>0$. Two-eigenvalue Hamiltonians ($H=cI+\lambda Q$, $Q^2=I$) are always time-symmetric because the off-diagonal propagator is proportional to $-i\sin(\lambda t)Q_{ij}$; this is why (7.1) can escape the gauge criterion.

**Non-resonance lemma.** If all positive gaps between distinct eigenvalues are distinct and some eigenprojector is $E_0=vv^\dagger$ with all $v_i\ne0$, then $M_H(t)=M_H(t)^{\mathsf T}$ for all $t$ iff $H$ is diagonally gauge-equivalent to a real matrix. (Distinct gaps separate the cancellations; choosing the gauge with $v>0$ makes $E_0$ positive entrywise, so every $E_\lambda$ is real.) This is what is recovered when the degeneracies exploited by (7.1) are removed.

### 7.3 Theorem F — finite derivative certificate for a fixed pair

Let $\Omega$ be the union of the distinct Bohr gaps of $H_+$ and $H_-$, including zero, with $n=|\Omega|$. Then
$$
\Delta M\equiv0
\quad\Longleftrightarrow\quad
\Delta M^{(k)}(0)=0\quad(0\le k<n).
\qquad n\le2d(d-1)+1. \tag{7.3}
$$
In particular it suffices to test $k=0,1,\ldots,2d(d-1)$, using
$$
J_{ba,k}=\operatorname{tr}\!\left[P_b(\mathcal L_+^k-\mathcal L_-^k)(P_a)\right],
\qquad \mathcal L_z=-i[H_z,\cdot].
\tag{7.4}
$$
These $J$ are derivatives, not Taylor coefficients; divide by $k!$ when comparing with §5.

*Proof.* Each entry of the difference has the expansion
$\sum_{\omega\in\Omega}b_\omega e^{-i\omega t}$.
Vanishing of the first $n$ derivatives gives the square system
$\sum_\omega(-i\omega)^k b_\omega=0$, $0\le k<n$.
Its Vandermonde determinant is nonzero because the frequencies in $\Omega$ are distinct. Thus every $b_\omega=0$, which is precisely S. A Hermitian $d$-dimensional matrix has at most $d(d-1)$ nonzero distinct ordered eigenvalue differences. Zero is shared by the two spectra, so their union has at most $2d(d-1)+1$ elements. Formula (7.4) follows by differentiating the unitary channel. $\square$

Repeated gaps must be merged; their coefficients can cancel, as the $K_4$ example illustrates. Exact Liouvillian iteration avoids numerical decisions about nearly equal gaps. Over exact algebraic coefficients this is a terminating fixed-pair algorithm. The gap-count bound need not be optimal for a particular pair; no claim of universal sharpness is made for F.

The former bound $k<2d^2$ follows directly by Cayley–Hamilton on $\mathcal L_+\oplus\mathcal L_-$. It was incorrectly called a specific theorem of D'Alessandro in v1.0. D'Alessandro [R6, §2, Theorem 1] concerns controlled state observability; it supplies methodological context, not that literal pairwise dimension bound. Neither quadratic bound contradicts J: J is a generic existence statement on independent supports, whereas F must decide every exceptional fixed pair.

### 7.4 Corollary T — exact generic test for tied polynomial families

Suppose $H_\pm(x)$ are Hermitian on a nonempty open parameter domain $U\subset\mathbb R^q$ and each entry is a polynomial of total degree at most $m$. Put $N_*=2d(d-1)$. The blind locus is exactly
$$
\mathcal B=U\cap\bigcap_{\substack{a,b\\0\le k\le N_*}}
\{x:J_{ba,k}(x)=0\},\qquad \deg J_{ba,k}\le mk. \tag{7.5}
$$
The family is generically blind iff every polynomial in (7.5) is identically zero, in which case it is blind at every point of $U$. Otherwise it is visible outside a proper real algebraic set, and hence for almost every $x\in U$.

*Proof.* Each commutator step raises polynomial degree by at most $m$, establishing the degree bound. Apply F at each $x$, including points where gaps merge. If one jet polynomial is nonzero it cannot vanish on an open set and its zero set has Lebesgue measure zero; the blind locus lies inside it. Conversely, identical vanishing of all jets invokes F at every point. $\square$

One exact implementation starts with $X_{z,a}^{(0)}=P_a$, recursively computes
$X_{z,a}^{(k+1)}=-i[H_z(x),X_{z,a}^{(k)}]$, and reduces the diagonal differences as polynomials. It either returns a nonzero polynomial witness or exhausts $k\le N_*$. With Gaussian-rational input coefficients, ordinary symbolic polynomial arithmetic gives a finite certificate. This algorithm is not linear in graph size; degrees, number of monomials and arithmetic complexity can grow rapidly. Numerical nonzero samples can find witnesses but cannot certify a polynomial identity.

For example, the tied family $H_\pm(x)=\pm ixA$ with $A$ from (7.1) has every jet zero although its independent complex support fails both U* and A*. C06 checks this symbolic family exactly. Changing one independent edge breaks the special relation $A^2=-3I$ and produces an order-three witness. Thus T supplies a decision method for finite polynomial ties, not a graph-only classification of arbitrary many-body models. Nonpolynomial ties, an unspecified domain constraint, infinite-dimensional limits and uniform truncation error require further arguments. Identifiability work based on similarity transformations and finite observable realizations [R7] is the method baseline; (7.5) is the explicit population-pair specialization used here.

## 8. Cross-parity, symmetry modes and the allowed readout

### 8.1 Theorem A — normalized cross-parity identity

Let $\rho$ be a density matrix and $0\le M\le I$ an effect. Let $\Theta$ be a unitary or antiunitary involution. On Hermitian operators define the real-linear involution $\mathcal T(X)=\Theta X\Theta^{-1}$ and $X_s=(X+\mathcal T X)/2$, $X_a=(X-\mathcal T X)/2$. Write $\Phi_+^t(X)=U_+(t)XU_+(t)^\dagger$. The transformed channel is $\Phi_\Theta^t=\mathcal T\Phi_+^t\mathcal T$, generated by
$H^\Theta(t)=\Theta H_+(t)\Theta^{-1}$ for unitary $\Theta$, and by its negative for antiunitary $\Theta$.

For $p_z(M)=\operatorname{tr}M\Phi_z^t(\rho)$ and $\Delta(t)=H_-(t)-H^\Theta(t)$,
$$
p_+(M)-p_-(M)=
2\operatorname{tr}[M_s\Phi_+^t(\rho_a)]
+2\operatorname{tr}[M_a\Phi_+^t(\rho_s)]+\epsilon_M,
\qquad
|\epsilon_M|\le
\int_0^t\inf_{c\in\mathbb R}\|\Delta(s)-cI\|\,ds . \tag{8.1}
$$
The integrable finite-dimensional generators and $t\ge0$ are assumed. The scalar can be optimized at each time.

*Proof.* For Hermitian $X,Y$, $\operatorname{tr}XY$ is real, and conjugation by either kind of $\Theta$ preserves this real pairing. Thus
$p_\Theta(M)=\operatorname{tr}(\mathcal TM)\Phi_+^t(\mathcal T\rho)$.
Subtract this from $p_+(M)$, expand $M=M_s+M_a$ and $\rho=\rho_s+\rho_a$, and cancel the equal-parity terms. The remaining terms give the displayed identity with $\epsilon_M=p_\Theta-p_-$. Duhamel's channel formula and trace-norm contraction of unitary conjugation bound the output trace distance by the integral in (8.1), exactly as in Q. This bounds the difference of any normalized effect probabilities. $\square$

The identity locates state asymmetry, measurement asymmetry and dynamical symmetry defect separately. It does not imply that all corpus no-record statements have identical hypotheses. M61's branch intertwining is a QND symmetry input; M65 also fixes a measurement axis; M68 concerns a specified commutative coupling algebra and stationary structure. Section 12 makes those distinctions explicit.

### 8.2 Theorem C — mode selection with a named group

For a specified compact torus representation $U_\phi=e^{i\phi\cdot Q}$ let
$\mathcal G(X)=\int U_\phi XU_\phi^\dagger\,d\phi$ be its normalized twirl. If
$\mathcal G(\Delta\rho)=0$, then
$$
\operatorname{tr}\!\left[M\mathcal E(\Delta\rho)\right]=0
\tag{8.2}
$$
for every $G$-covariant channel $\mathcal E$ and every invariant effect $M$.
Indeed $\mathcal G\mathcal E=\mathcal E\mathcal G$ and $\operatorname{tr}MX=\operatorname{tr}M\mathcal G(X)$, so the expression vanishes. This is the mode-preservation theorem of Marvian–Spekkens [R8, Eq. (2.10), Proposition 1], specialized to a branch difference.

The representation is indispensable. In the one-particle dual-rail code
$|0_L\rangle=|10\rangle$, $|1_L\rangle=|01\rangle$, total charge is $N_1+N_2=I$ on the code. Every logical operator is then mode zero, and logical X/Y rotations conserve total charge. For the relative generator $Q_{\rm rel}=|1_L\rangle\langle1_L|$, the same off-diagonal operators have modes $\pm1$. Rotations that analyze these modes need relative-phase control and are not covariant under that relative group. An overall total-charge reference requirement cannot be inferred from a relative-group obstruction.

### 8.3 Proposition D — invariant effects and populations

If the joint eigenspaces of the chosen local charges are one-dimensional, their commutant consists of configuration-diagonal operators: entry $M_{ab}$ must vanish whenever some charge distinguishes $a$ and $b$. Thus invariant effects are population effects. If only total charge is imposed, degenerate charge sectors allow off-diagonal effects. This elementary commutant calculation specifies when “invariant” really means “population-only.”

A common calibrated analyzer can serve multiple memories. The number of records by itself counts neither independent reference states nor their energy or degradation. If a nontrivial physical charge representation is actually selected, M71 supplies additional resource bounds (§12), but those bounds cannot be transferred to a scalar representation by terminology.

## 9. Writing one population record

### 9.1 Proposition E (dual-rail conditional resonance)

For $h_z=wX+\tfrac{\delta+z\chi}{2}Z$ from $\lvert0\rangle$, $P_z(t)=\frac{w^2}{w^2+(\delta+z\chi)^2/4}\sin^2\!\big(t\sqrt{w^2+(\delta+z\chi)^2/4}\big)$. With $\delta=-\chi$, $\chi=\sqrt{4k^2-1}\,w$ and $\tau=\pi/(2w)$: $P_+=1$, $P_-=0$ ($k=1$: $\chi=\sqrt3w$). For an ideal infinite uniform time average, the contrast is $\overline P_+-\overline P_-=\tfrac12-\tfrac1{8k^2}$, equal to $3/8$ for $k=1$. Other uncertain-time distributions require their own averaging. This is the resonant-$\pi$/off-resonant-$2\pi$ mechanism of two-level control and is not central novelty.

### 9.2 Lemma E (write-error function)

With $f(x)=\sin^2(\tfrac\pi2\sqrt{1+x^2})/(1+x^2)$ and $e(x)=\max\{1-f(x),f(x-\sqrt3)\}$,
$$
e(x)\le\min(1,x^2)\quad\text{for all }x\in\mathbb R,\qquad 1-f(x)=x^2+O(x^4). \tag{9.1}
$$
*Proof.* First restrict to $|x|\le1$. Then $1-f(x)=\frac{x^2+\sin^2(\pi(u-1)/2)}{1+x^2}\le\frac{x^2+\pi^2x^4/16}{1+x^2}\le x^2$ with $u=\sqrt{1+x^2}$. For $\lvert x\rvert\le1$ put $v=\sqrt3-x\ge\sqrt3-1$, $u=\sqrt{1+v^2}$; then $f(x-\sqrt3)\le x^2\big[\tfrac{\pi(v+\sqrt3)}{2u(u+2)}\big]^2$ and $r(v)=(v+\sqrt3)/(u(u+2))$ is decreasing for $v\ge\sqrt3-1$ (the numerator of $r'$ has the sign of $1-v^2-2\sqrt3v+2(1-\sqrt3v)/u<0$), so the bracket is at most its value at $v=\sqrt3-1$, which the rational bounds $\sqrt3<26/15$, $u^2>23/15$, $u>6/5$, $\pi/2<11/7$ put below $407/413<1$. For $\lvert x\rvert>1$, $e\le1$. $\square$ The rational inequalities above prove the bound; the numerical maximum of the squared bracket, approximately $0.930$, is not an additional exact certificate. Current V02 is only a grid countercheck.

### 9.3 Theorem W (robust writing under an unknown static offset)

For $h_{z,\beta}(t)=w(t)X+\tfrac{u(t)+(z-1)\chi+\beta}{2}Z$ with an unknown offset $\beta\in[-b,b]$ fixed during the write: if $b\ge\chi$ the worst-case error is at least $1/2$ (two branch/offset pairs give the same Hamiltonian); if $b<\chi$ the adiabatic schedule $w(s)=w_0\sin\pi s$, $u(s)=\chi(2s-1)$, $s=t/T$, has a uniform gap $g_*=2w_0(\chi-b)/\sqrt{\chi^2+4w_0^2}$ and error $p_T\le\min(1,C_*^2/T^2)$ with $C_*=\frac{2A_1+A_2}{g_*^2}+\frac{7A_1^2}{g_*^3}$, $A_1=\sqrt{\chi^2+\pi^2w_0^2}$, $A_2=\pi^2w_0$ (Jansen–Ruskai–Seiler, applied). For a square resonant pulse a Duhamel bound $p\le\min\{1,(\pi b/4w)^2\}$ holds per history.

*Proof.* If $b\ge\chi$, choose $(z,\beta)=(+,-\chi)$ and $(-,+\chi)$. The two generators coincide for the entire schedule, so no final decision can have error below $1/2$ for both labels. If $b<\chi$, both initial detunings are negative and $w(0)=0$, so $|0\rangle$ is the ground state for both branches. At $s=1$, the plus detuning is positive and the minus detuning negative: ground-state following writes $|1\rangle$ for plus and $|0\rangle$ for minus.

For the plus branch put $D=\chi-b>0$ and $r=\min(s,1-s)$. The gap obeys
$G(s)^2\ge16w_0^2r^2+(D-2\chi r)_+^2$,
using $\sin\pi s\ge2r$ and the reverse triangle inequality. Minimizing this quadratic lower envelope yields $G\ge g_*$. For the minus branch the detuning is always at most $-D$, so its gap is at least $D\ge g_*$. The first two derivative norms are bounded by $A_1,A_2$. Applying Jansen–Ruskai–Seiler [R9, Theorem 3, Eq. (6)] to the nondegenerate ground projection, with the two endpoint terms and the integral over $s\in[0,1]$, gives the amplitude bound $C_*/T$ and hence the stated error. Finally an offset contributes $\beta Z/2$ to a square pulse. Its propagator error from the perfectly writing ideal pulse is at most $\tau b/2=\pi b/(4w)$; projection onto the wrong basis state squares this amplitude bound. $\square$


## 10. Sequential redundant population records

### 10.1 ARCH-1 (exact history distribution)

Memories $j=1,\dots,R$ are dual rails with rail variables $s_j=\pm1$ (initially $+1$; correct record $s_j=-z$). During the $j$-th window
$$
H^{(j)}=\sum_k\frac{\delta_k+z\chi_k}{2}s_k+\sum_{k<l}\frac{gK_{kl}}{2}s_ks_l+w_jX_j, \tag{10.1}
$$
with all other $X_k$ off, $K$ real symmetric with zero diagonal. *The joint distribution of $(s_1,\dots,s_R)$ conditioned on $z$ is the history chain $\Pr(s_1,\dots,s_R\mid z)=\prod_j\Pr(s_j\mid z,s_{<j})$, where in window $j$, with $\Delta_j=\delta_j+z\chi_j+g\sum_{k<j}K_{jk}s_k+g\sum_{k>j}K_{jk}$ and $x_j=\Delta_j/(2w_j)$, the error probability is $1-f(x_j)$ for $z=+$ and $f(x_j)$ for $z=-$.* *Proof.* The population projector of a written memory commutes with every later unitary (deferred measurement), so measuring at the end equals measuring after each window; conditioned on the previous configuration the active memory evolves as a two-level system; each final configuration has a unique history, so there is no interference. Coherence may remain in the joint state; block-diagonality of the state is not assumed. $\square$ (v1.2 row V29 and the v1.2 referee: full 8-dimensional quantum simulation equals the chain to $10^{-15}$.)

### 10.2 ARCH-2M (uniform bound)

Take $g\ge0$ and $w_j>0$ (a common sign of $g$ can be absorbed in $K$), and assume the uniform resonance $\chi_j=\sqrt3w_j$, $\delta_j=-\chi_j$. With error indicators $E_k$, $s_k=-z(1-2E_k)$, $F^*_j(z)=-z\sum_{k<j}K_{jk}+\sum_{k>j}K_{jk}$ and $p_j=\Pr(E_j=1\mid z)$, Lemma E and Minkowski's inequality give
$$
\sqrt{p_j}\le\frac{g\lvert F^*_j\rvert}{2w_j}+\sum_{k<j}\frac{g\lvert K_{jk}\rvert}{w_j}\sqrt{p_k}, \tag{10.2}
$$
without any independence assumption. With $d_j=g\lvert F^*_j\rvert/(2w_j)$ and the strictly lower-triangular $T_{jk}=g\lvert K_{jk}\rvert/w_j$, $\sqrt{\boldsymbol p}\le(I-T)^{-1}\boldsymbol d$ for every finite $R$. If $w_j=w$, $\sigma=g\sup_{j,z}\lvert F^*_j\rvert$ and $\alpha=g\sup_j\sum_{k\ne j}\lvert K_{jk}\rvert$ are finite over all $R$, then
$$
\alpha<w\ \Longrightarrow\ p_{\max}\le\min\Big\{1,\frac{\sigma^2}{4(w-\alpha)^2}\Big\}. \tag{10.3}
$$
On the common domain $\sqrt2\alpha<w$ this is never worse than the v1.2 bound $\sigma^2/(2(w^2-2\alpha^2))$ (the difference of denominators is $2(w-2\alpha)^2\ge0$). Since $\lvert F^*_j\rvert\le\sum_k\lvert K_{jk}\rvert$, $\sigma\le\alpha$ is always admissible. The finite pair-state kernel estimates mentioned in the seed lineage are not used as all-$R$ hypotheses here. The original v1.0 V03 rerun retains its 600-chain check; current §10.4 supplies a stronger history-uniform envelope and an additional decoding guarantee.

### 10.3 ARCH-3 — scaling limit of the sufficient condition

Consider a three-dimensional array of fixed density and spacing, a point source with fixed multipole strengths, fixed memory moments, and an interaction kernel for which at least one fixed nonzero neighbour coupling persists as $R$ grows. The last assumption gives an $R$-independent lower bound $\alpha\ge\alpha_0>0$; spacing alone does not give it if angular factors or engineering cancel all such couplings. Let the largest source–memory distance satisfy $L\gtrsim aR^{1/3}$. A fixed monopole source couples to a memory moment of multipole order $\ell$ with $|\chi_{\min}|\lesssim L^{-(\ell+1)}$ (or smaller if angular cancellation occurs). A common resonant exchange rate chosen proportional to this weakest signal then satisfies
$$
\alpha/w\gtrsim R^{(\ell+1)/3}. \tag{10.4}
$$
This includes $R^{2/3}$ for a dipole and $R$ for a quadrupole. Consequently the hypotheses of (10.3), and of the uniform decoding bound below, eventually cease to hold. This is failure of these sufficient conditions, not proof that the actual process fails. Nonuniform rates, dilute arrays, distributed or growing sources, relays, moving sources and selective connection change the resource assumptions.

For a fresh memory with the *only* branch dependence in
$h_z(t)=h_0(t)+z\chi_j(t)Z_j/2$, and the same initial joint state and branch-independent environment dynamics, Duhamel gives
$D_j^{\rm pop}(T)\le\min\{1,\int_0^T|\chi_j(t)|dt\}$.
The normalization $1/2$ is part of this statement. If another subsystem already contains a branch record and interacts with the memory, this direct-signal bound does not apply without including that additional branch dependence. Signed interaction sums, absolute row sums and actual error rates are different quantities; divergence of one must not be reported as divergence of another.

### 10.4 Theorem R — correlated records with exponentially reliable majority decoding

Keep ARCH-1 and the $k=1$ resonance of ARCH-2M. Define
$$
\alpha_j=g\sum_{k\ne j}|K_{jk}|,\qquad
p_j^*=\min\left\{1,\frac{\alpha_j^2}{4w_j^2}\right\}.
\tag{10.5}
$$
For either branch and every prior history of positive probability,
$$
\Pr(E_j=1\mid z,E_1,\ldots,E_{j-1})\le p_j^*.
\tag{10.6}
$$
Moreover the error vector is stochastically dominated, for every increasing event, by independent Bernoulli variables $B_j$ with success probabilities $p_j^*$. In particular,
$$
\Pr\!\left(\sum_{j=1}^R E_j\ge q\mid z\right)
\le
\Pr\!\left(\sum_{j=1}^R B_j\ge q\right)
\le
\inf_{t>0}e^{-tq}\prod_{j=1}^R(1-p_j^*+p_j^*e^t).
\tag{10.7}
$$
For equal $w_j=w$ and a common row envelope $\alpha$, let
$p_*=\alpha^2/(4w^2)<1/2$. Majority decoding, with ties counted as errors for a conservative bound, obeys
$$
P_{\rm maj}(z)\le
\Pr\{\operatorname{Bin}(R,p_*)\ge\lceil R/2\rceil\}
\le \exp[-R D(1/2\|p_*)]
= [4p_*(1-p_*)]^{R/2}.
\tag{10.8}
$$
Here $D(u\|p)=u\log(u/p)+(1-u)\log((1-u)/(1-p))$ uses natural logarithms. Thus $\alpha<\sqrt2\,w$ is sufficient for exponentially small majority error. At $p_*=0$, every write is exact and the limiting bound is zero.

*Proof.* Condition on an entire past configuration. The dimensionless residual offset is
$x_j=g\sum_{k\ne j}K_{jk}s_k/(2w_j)$,
with future rails still equal to $+1$. Whatever the history, $|s_k|=1$, so $|x_j|\le\alpha_j/(2w_j)$. For the plus branch the error is $1-f(x_j)$; for the minus branch it is $f(x_j-\sqrt3)$. Lemma E proves (10.6), without estimating a marginal or assuming independent past errors.

For completeness, construct the joint law using independent uniforms $U_j$ on $[0,1]$. Recursively set
$E_j=1_{\{U_j\le q_j(E_{<j})\}}$, where $q_j$ is the actual conditional error probability; null histories can be assigned any value at most $p_j^*$. On the same probability space set $B_j=1_{\{U_j\le p_j^*\}}$. The $B_j$ are independent and $E_j\le B_j$ coordinatewise. This proves stochastic domination and the first bound in (10.7). Markov's inequality applied to the independent Bernoulli moment-generating function proves the second. For a uniform envelope, use the threshold $R/2$ and minimize at $e^t=(1-p_*)/p_*$, obtaining (10.8). $\square$

There are two useful improvements over v1.0. First, on its previous domain $\alpha<w$, the direct conditional envelope already gives $p_*<1/4$ and the majority result follows without an extra physical assumption. Second, a majority guarantee continues on $w\le\alpha<\sqrt2w$, where the denominator of (10.3) is not usable. For signed kernels with very small $\sigma$, (10.3) can still be the stronger *marginal* estimate. Both estimates can be retained:
$$
p_j\le \min\left\{p_j^*,\big[(I-T)^{-1}\boldsymbol d\big]_j^2,1\right\}.
\tag{10.9}
$$
The criterion $\alpha<\sqrt2w$ is sufficient, not necessary or an optimal threshold.

Let $\mu_\pm$ be the final classical population laws. If a fixed majority decoder has conditional error at most $\epsilon$ on both branches, its decision event $A$ satisfies
$\mu_+(A)-\mu_-(A)\ge1-2\epsilon$. Therefore
$$
\|\mu_+-\mu_-\|_{\rm TV}\ge\max\{0,1-2\epsilon\},
\qquad
P_{\rm Bayes}^{\rm equal\ prior}\le\epsilon.
\tag{10.10}
$$
The trace distance of the corresponding quantum states is at least this classical total variation because the population measurement is a channel. This is a guarantee for the joint readout of a declared instrument, not derivation of that instrument or a spectrum-broadcast structure.

Marginal bounds alone would not suffice: if $E_1=\cdots=E_R=B$ with $\Pr(B=1)=p<1/2$, every marginal is $p$ but the majority error stays $p$ for every $R$. W01 encodes this counterexample. Our theorem avoids it by proving a conditional bound for every history. It neither makes the records independent nor claims that the probability of *all* records being correct tends to one. Full-Hilbert evolution versus the deferred-measurement chain is checked separately in V04; C10 and V03 probe the domination statement, including correlated histories.

## 11. Buses

### 11.1 BUS-P (passive quadratic bus)

For $H_B=\tfrac12p^{\mathsf T}p+\tfrac12q^{\mathsf T}Aq-q^{\mathsf T}(fz+Gs)$ with $A\succ0$, completing the square at fixed $s$ gives $E(z,s)=E_{\rm vac}-\tfrac12F-zh^{\mathsf T}s-\tfrac12s^{\mathsf T}Ks$ with $F=f^{\mathsf T}A^{-1}f$, $h=G^{\mathsf T}A^{-1}f$, $K=G^{\mathsf T}A^{-1}G$; in ARCH notation $\chi_j=-2h_j$, $gK^{\rm ARCH}_{jk}=-2K_{jk}$. The following is a standard Gram/Schur consequence, specialized to the declared bus, not a new matrix inequality. Since $\begin{pmatrix}F&h^{\mathsf T}\\h&K\end{pmatrix}$ is a Gram matrix, $h\in\operatorname{ran}K$, $h^{\mathsf T}K^+h\le F$, and with $S=\max_j\sum_k\lvert K_{jk}\rvert$,
$$
\lVert h\rVert_2^2\le F\lVert K\rVert_2\le FS. \tag{11.1}
$$
If $\lvert h_j\rvert\ge h_{\min}$, $K_{jj}\le\kappa_0$ and $\sum_{k\ne j}\lvert K_{jk}\rvert\le\kappa$ for all $j$, then $F\ge Rh_{\min}^2/(\kappa_0+\kappa)$: a fixed passive bus with uniform signal and bounded cross-talk needs a source response resource growing linearly in $R$. A single common mode ($K=hh^{\mathsf T}/F$) forces $\sum_{k\ne j}\lvert K_{jk}\rvert\ge(R-1)h_{\min}^2/F$. For $\mu>0,\kappa\ge0,g,f_0\ge0$, the distributed source $A=\mu^2I+\kappa\mathsf L$, $G=gI$, $f=f_0\mathbf 1$ on a graph Laplacian $\mathsf L$ attains equality: $h=(gf_0/\mu^2)\mathbf1$, $S=g^2/\mu^2$, $F=f_0^2R/\mu^2$. On a finite graph of maximum degree $\Delta>0$, a source supported on $\mathcal S$ with $|f_j|\le f_0$ is screened: $\lvert h_j\rvert\le(gf_0/\mu^2)\rho^{\,\mathrm{dist}(j,\mathcal S)}$ with $\rho=\kappa\Delta/(\mu^2+\kappa\Delta)<1$, and $R_{\rm good}h_0^2\le g^2f_0^2\lvert\mathcal S\rvert/\mu^4$; a surface source cannot supply a uniform lower bound to a volume of memories in a gapped local bus, so "the seam is a boundary, hence uniform" is not available by name. For the screening estimate write
$A=(\mu^2+\kappa\Delta)(I-\rho P)$ with $P=I-\mathsf L/\Delta$, a nonnegative stochastic matrix. The Neumann expansion has no path from $j$ to $\mathcal S$ in fewer than $\mathrm{dist}(j,\mathcal S)$ steps; its remaining geometric tail gives the displayed bound. The resource-count bound follows independently from $\|A^{-1}\|\le\mu^{-2}$ and $\|f\|^2\le f_0^2|\mathcal S|$.

Turning on $wX_j$ during a static Schur elimination re-dresses the flip by $\exp[\pm2i(A^{-1}g_j)^{\mathsf T}p]$ (polaron overlap $\exp[-g_j^{\mathsf T}A^{-3/2}g_j]$), so the static Ising coefficients do not by themselves give an oscillator write theorem.

### 11.2 BUS-G (explicit active record)

Connect one memory at a time to a bus $H^{(j)}=\omega a^\dagger a+(a+a^\dagger)F_j$, $F_j=fz+gs_j$, for $\tau=2\pi/\omega$. Completing the square and using $e^{-2\pi ia^\dagger a}=I$,
$$
U_j(\tau)=e^{2\pi iF_j^2/\omega^2}\otimes I_B=e^{i\phi_0}e^{i\theta zs_j}\otimes I_B,\qquad\theta=4\pi fg/\omega^2, \tag{11.2}
$$
for any initial bus state. With $fg=\omega^2/16$, $\theta=\pi/4$; the sequence $R_x(\pi/2)\,e^{i\pi zZ_j/4}\,R_y(\pi/2)$ from $\lvert0\rangle$ sends $z=+$ to $\lvert1\rangle$ and $z=-$ to $\lvert0\rangle$; repeating over the memories writes the same correct configuration into all $R$ memories with no induced cross-terms (only one memory connected at a time). This is the qubus principle (Spiller et al.; van Loock et al.), used as a positive existence construction with explicit control and time resources.

### 11.3 What BUS-G requires, and which group charges that resource

The sequence in §11.2 uses a calibrated relative angle between two logical transverse rotations. In the restricted two-$\pi/2$-pulse sequence around a phase gate with $\theta=\pi/4$, equal axes give populations $1/2,1/2$, while orthogonal axes give $1,0$. An axis separation $\pi/4$ gives $(1+1/\sqrt2)/2$ and $(1-1/\sqrt2)/2$; reversing the angle reverses the label. This calculation is about that sequence. It does not exclude more general protocols using one drive axis together with a branch-independent logical $Z$ rotation, which itself changes the effective transverse angle.

For a dual-rail implementation the two logical rotations can be generated by charge-conserving hopping. Their control phases and timing must be calibrated across the bus window, but the total-charge representation is scalar on the code; C11 explicitly checks both perfect readout and commutation with total charge. No external *total-charge-asymmetric state* is mathematically required by Theorem C in this representation. Under the independent-rail or relative logical phase group, the same transverse controls are noncovariant and constitute an asymmetry resource. The v1.0 statement that BUS-G was universally a mode-$\pm1$ record and therefore not reference-free is withdrawn.

| Resource | Declared cost or assumption |
|---|---|
| Bus coupling and reset | One memory connected at a time; exactly one oscillator period; ideal harmonic dynamics; the bus returns for any initial state |
| Coupling area | $fg=\omega^2/16$ for the selected phase |
| Logical control | Two calibrated rotations, or an equivalent controlled relative angle; $R$ sequential windows |
| Total-charge symmetry | Preserved in the one-particle dual-rail encoding |
| Relative-rail symmetry | Broken by the transverse analyzer when this stronger symmetry defines the allowed operations |
| Physical imperfections | Loss, leakage, switching transients and calibration noise require separate bounds |

The construction establishes an ideal finite-$R$ existence result with explicit controls. It does not turn an action-selected physical implementation into a free resource, and it does not assert an unavoidable reference-energy scaling without specifying the apparatus representation.

## 12. Corpus mathematics and the conditional physical interface

### 12.1 Primary-source map and scope of reuse

The Repo3 manifest, core, constants/lemmas, debt gates, claim ledger, dependency graph and current M70–M73 manifest log were read before selecting assets. The table uses direct Repo1 primary texts, not only index summaries. Source snapshots, observed versions, Drive URLs and hashes are recorded in the release source map. These are local connection checks; they are not a fresh audit of every theorem in those papers. The direct folder inventory contained 231 items; it is not a proof of completeness for all nested or private corpus locations.

| Source and exact locator | Mathematical asset actually used | Connection to M74 | Assumption or boundary retained |
|---|---|---|---|
| M54 v2.2, M54.8b–8c, M54.10–11, M54.16 | $K_{2,9}$ mediator skeleton; quantum coupling blocks; rank-one collective route; transport package; purifier distinguishability | Exact block switching and branch-even Schur term, §12.2 | Static conductance and quantum couplings have different normalizations; a physical clock and the branch-sign assignment are conditional |
| M56 v1.8, §2.2 Theorem M56.21′; §3 M56.22′ | Register grading multiplicities $(10,1)$ and a graded tensor-subsystem obstruction | A population classifier cannot manufacture the carrier/environment factorization, §12.3 | Complete-order channel embedding does not imply grading-preserving action-subsystem embedding |
| M58 v1.7, §6 M58.6–7; §8 M58.8 | Same unpointed bilateral dilation may realize different scalar contractions; pointed state/filter/clock data matter | Equality of unitaries or population laws does not select an instrument or clock | Pointed intertwining is a stronger, conditional requirement |
| M60 v1.5, §5 M60.5–6; §11 M60.16–17 | Pure pointer-diagonal gauge copies give a constant coherence-multiplier family; seam covariance requires an invariant environment state | B1 is the configuration-population counterpart; A separates state and dynamical symmetry | The initial-state assumption can fail; no unconditional bulk no-record conclusion |
| M61 v1.6, §4.1 Lemma M61.2a | In a pointer-QND dilation, joint-grading commutation iff $U_1=J_EU_0J_E$, with no residual phase | Supplies a unitary branch-intertwining input to A | QND and pointer exchange are explicit; $J_E$ is not the diagonal graph-switching gauge |
| M65 v4.0, §3 T-RC, §4 T-PF | Fresh-ancilla contrast $P_+(+)-P_-(+)=-n_y\sin2\theta$; pushforward equivalence of relabelled record laws | Separates branch distinction from axis selection; R handles a different interacting-memory architecture | T-RC's nondegenerate prior and $\sin2\theta\ne0$ condition; action does not choose $n$ or $\theta$ |
| M68 v1.4.1, §5.1 Theorem 5.1; §§5.8–5.9, Cor. 5.12 | Commutative carrier coupling yields Kraus operators in $\mathbb C[X_E]$, unital flip covariance; survival and joint-grading conditions differ | A/C diagnose allowed observations after specifying the actual algebra | Not a theorem that every finite-time state has no record; longitudinal resources and $w=\pm e_J$ selection remain distinct |
| M71 v1.4.1, §2 T-CAP, §3 T-EC, §7.1 | For a nontrivial charged qubit plus rotor reference, invariant-readout contrast is $\sum_m\vert{}\sigma_{m,m+1}\vert{}$ with energy bounds; joint charge-energy apparatus has additional assumptions | Quantifies a reference only after its representation is fixed, §12.4 | Cannot apply these bounds to a scalar total-charge dual-rail code; apparatus preparation and conservation classes are not interchangeable |
| M73 v2.2.1, §2.4 Eqs. (2.11)–(2.12), §8.17 NP-SQRTLOG | Echo-defined memory coherence, trace-distance records and full-model $\sqrt{\log R}$ confinement theorem in the declared model | Separates trace-distance from population distinguishability, §12.4 | Current version is 2.2.1; oscillator preparation, geometry, time window and all-$R$ assumptions remain as in the source |
| S14 v2.1, §10.3.5 NC-S14.19; §10.4 Proposition S14.L; §10.5 | Higgs-slot identification dilemma; existing intertwiners with two real scaling freedoms; action/selection distinction | Identifies what must be selected to instantiate an M74 family, §12.5 | Existing algebraic intertwiners are not absent; their physical selection is unresolved |

M57 v1.8 was also retrieved as lineage background. No new M57 theorem is used as a hidden premise of M/J. The current Repo1 inventory did not establish an issued M75 paper, so numerical constants assigned that code in the old manuscript are retained only in the unchanged historical package, not used as current proof inputs.

### 12.2 Corollary Z — M54 block switching, including tied couplings

Suppose the branch acts as a common sign on inter-block mediator couplings:
$$
H_z=
\begin{pmatrix}D_A&zB\\zB^\dagger&D_B\end{pmatrix},
\qquad
g=\operatorname{diag}(I_A,-I_B).
\tag{12.1}
$$
The branch-even Hermitian blocks $D_A,D_B$ may contain arbitrary within-block couplings; the entries of $B$ may be tied, complex or rank one. Direct multiplication gives $gH_+g^\dagger=H_-$, so B1 proves blindness of all node populations. For time dependence the same fixed $g$ works at every instant. This is an exact sufficiency statement and does not require M's independence hypothesis.

For M54's $K_{2,9}$ skeleton, $d=11$, $|\mathcal E|=18$, the cycle-space dimension is $18-11+1=8$, and the girth is four. Even cycles do not remove the common-sign gauge. Where the resolvent exists, eliminating block B gives
$D_A+z^2 B(E-D_B)^{-1}B^\dagger$, also branch-even. This does not identify the static Laplacian conductance normalization with the quantum Hamiltonian. Nor is $g$ the corpus seam involution: $g$ changes coefficient phases within a fixed node basis, whereas $J_{\rm seam}$ exchanges distinguished pointer sectors.

The hypothesis that the physical branch has form (12.1) remains conditional. Adding an edge within a block but keeping it branch-even still preserves the displayed gauge. Other added terms need classification by their branch colour, diagonal content and phase constraints. In particular, “one extra X–Y edge makes a record” is not generally valid. With $L=0$ and real $V$, any graph is blind by A.

### 12.3 Grading, dilation and instrument are different interfaces

M56's obstruction can be seen directly. A balanced pointer has grading multiplicities $(1,1)$. If its environment carries both grading parities, then the negative eigenspace of $J_S\otimes J_E$ has dimension $\dim E\ge2$. A grading-preserving isometry into a register with negative multiplicity one is impossible. A channel can nevertheless have a complete-order embedding without furnishing that action-compatible tensor subsystem. None of M, T or R changes this dimension argument.

M58 adds a second distinction: an unpointed unitary dilation does not identify the cyclic environment vector, measurement filter or event clock. M61 provides a branch-intertwining relation only after the QND pointer and grading are specified. M65 then shows explicitly how a measurement axis controls record contrast, and how relabelling can preserve the probability law. Accordingly, a certificate that two supplied Hamiltonians have different populations is downstream of subsystem and instrument selection, not a substitute for either.

### 12.4 M73 coherence records and the correct use of M71

In the M73 diagonal-label construction, each memory starts in $|+x\rangle$ and keeps diagonal entries $1/2$ in its logical Z basis. Writing its conditional off-diagonal coefficient as $c_\pm$ gives
$$
\rho_{\pm,j}=\frac12
\begin{pmatrix}1&c_\pm\\\bar c_\pm&1\end{pmatrix},
\qquad
D_j=\frac12\|\rho_{+,j}-\rho_{-,j}\|_1
=\frac12|c_+-c_-|,
\qquad
D_j^{\rm pop}=0.
\tag{12.2}
$$
The source's $c_\pm$ are the appropriate averages of oscillator echoes. A transverse Helstrom analyzer can distinguish these states; a Z-diagonal effect cannot. This elementary calculation connects the exact observable definitions without changing M73's trace-distance result.

M73 v2.2.1's NP-SQRTLOG uses
$\Omega_R=10^4\sqrt{1+\log\lceil R^{1/3}\rceil}$ and proves $D_j\ge0.98853$ on its declared window for every $R\ge2$ and memory. Its source signal scales as $O(R^{-2})$ and its time window as $O(R^2)$. M74 does not replace that theorem, solve its fixed-confinement question, or transplant its preparation assumptions to ARCH.

For the relative logical phase group, the difference in (12.2) has no mode-zero component and C applies. For total charge on a dual-rail one-particle encoding, the representation is scalar and C gives no obstruction. If instead the physical encoding is the nontrivially charged qubit of M71, invariant effects on it plus a rotor reference have contrast
$C(\sigma)=\sum_m|\sigma_{m,m+1}|$ and the source's energy bounds apply under their stated apparatus assumptions. Thus M71 supplies a conditional resource calculation, not a universal cost per M73 memory. This distinction repairs the v1.0 BUS-G interpretation at the same time.

### 12.5 Carriers, action selection and debts

A dual rail with one charge in two positions has a dipole difference and an $r^{-3}$ pair-interaction tail. A neutral point-symmetric breathing encoding
$\rho_{0,1}=q(\delta_{\pm a}-2\delta_0),\,q(\delta_{\pm b}-2\delta_0)$
has zero dipole and a nonzero second-moment difference, leading to an $r^{-5}$ tail, absolutely summable on a separated three-dimensional lattice. It requires a two-particle logical flip and leakage control; it is not obtained by renaming a dipole qubit. No unverified numerical kernel constant from a candidate paper is needed for these multipole statements.

S14 §10.3.5 leaves the identification of the seam field with the Higgs slot unresolved: if identified, the Yukawa slot obstructs the exact seam symmetry; if separate, that branch supplies no derived seam vertex. Proposition S14.L nevertheless establishes an intertwiner family with two real scaling freedoms. The missing item there is selection of the intertwiner and scales, not algebraic existence. To instantiate an M74 record model one must supply a typed source-to-branch map, the carrier and environment, the selected coupling coefficients and non-gauge branch dependence, preparation and control windows, leakage bounds, and the actual instrument/readout class.

The live corpus debts D-S14-EVENT-001, D-M69-INSTRUMENT, K17/K18 and D-HCLK-001 remain OPEN. QND record time is not identified with modular or metric time here. M54's transport package, M56's grading, M58's pointedness, M65's readout axis and S14's action data are distinct obligations. The Mission gain is a sharper diagnostic and a conditional quantitative record theorem for FQ2/RQ3; no physical bridge, CORE assertion or remote SSOT state is promoted.

## 13. Reproducibility and the limits of executable evidence

The active manuscript is ZS-M74_v1_1_1.md. The unchanged v1.1 mathematical driver is preserved at provenance/m74_verify_v1_1.py, alongside its original ledger. The new driver m74_verify_v1_1_1.py runs that suite, then four correction-focused regressions. From the package root:

~~~bash
python m74_verify_v1_1_1.py --output m74_verify_v1_1_1.json
python evidence/replay_auditor.py --output evidence/rechecks/auditor_replay.json
~~~

The first command reports the 18 scientific rows separately from the four regression rows; the second replays the auditor's unmodified formula and operational scripts and records raw rows, declaration exclusions and failures. P remains zero: neither command proves universally quantified theorems or assigns a research grade. The supplied random-search and nested legacy results remain historical evidence; they are not represented as fresh executions in this patch release. Exact runtime versions and tolerances are in the ledgers and requirements.txt.

The following 18 mathematical rows and their scientific classes are carried over unchanged from v1.1.

| Evidence row | Class | Executed scope |
|---|---|---|
| C01 | C | Exact generators for a non-real diagonal gauge; detects the old antiunitary formula |
| C02 | C | 60 V-odd colourings of cycles of lengths 3–6, signed weights and a Gaussian-rational flux |
| C03 | C | Five mixed dumbbells, including nonzero tails; exact leading order and next-order parity |
| C04 | C | All-entry lower jets and the sharp path coefficient for $d=2,\ldots,6$ |
| C05 | C | Exact $A^2=-3I$, triangle product and inconsistent gauge ratios, computed rather than asserted |
| C06 | C | Fixed and symbolic tied $K_4$ jets through the finite bound; perturbed first witness |
| C07 | C | Merged-frequency Vandermonde calculation at an exact example |
| C08 | C | Componentwise U-only/A-only decisions and isolated vertices |
| C09 | C | 96 fixed Gaussian-integer mixed instances, $d=2,\ldots,5$, compared by exact jets; finite instances only |
| V01 | V | High-precision numerical Q remainder/signal counterchecks for three path dimensions |
| V02 | V | Numerical grid countercheck of Lemma E; analytic proof is §9.2 |
| C10 | C | Exact rational adapted, positively dependent examples for $R=3,5,7,9$; every error-count tail dominated |
| W01 | W | Perfectly correlated errors refute majority concentration from marginals alone |
| V03 | V | 32 interacting history-chain cases: $R=3,5,7,9$, four row envelopes up to 1.39, both branches; all histories enumerated with floating trigonometric arithmetic |
| V04 | V | Full $2^R$-dimensional quantum evolution versus history laws, $R=3,4$, both branches |
| C11 | C | Exact BUS-G rotations and total versus relative charge commutators |
| C12 | C | Tied rank-one block-switching example with within-block couplings |
| V05 | V | Both-branch numerical countercheck of W's uniform gap bound |

**Scientific-suite census:** 18 rows, P=0, C=12, V=5, W=1. The v1.1.1 driver adds R=4, not four new scientific discoveries. R01 checks the two gauges on every one of 62 coloured paths. R02 checks their all-entry lower jets and exact coefficient (6.1). R03 explicitly computes the next-order parity coefficients for the three cases left as declarations in the supplied auditor script. R04 computes the robust-write endpoint inequalities and the correlated-error counterexample formerly asserted by two operational declaration rows. The ledgers report actual PASS/FAIL totals.

The auditor formula script prints 139 rows, but three next-order checks use a literal true condition; only the other 136 are evaluated checks. The operational script prints 32 rows, including two literal-true declarations; only 30 are evaluated checks. The original files and counts are preserved as provenance, and are not silently rewritten or counted as 171 independent calculations. R03/R04 supply the missing calculations separately. Replaying their code is deterministic reproduction of the supplied audit, not a new independent review.

The five original fault-injection controls (gauge→C01, cycle→C02, sharp→C04, majority→C10, finite→C06) are preserved in the v1.1 package. For the actual changed proof, the new driver has a targeted old-gauge injection that must fail R01; a sharp-coefficient injection must fail R02. The freeze report records which controls were executed in this release.

The v1.0 13/13 suite and its nested classifier 19,720/0 are supplied historical results. As already disclosed in v1.1, its old C03 contains floating arithmetic and a hard-coded gauge flag and is not an exact gauge certificate. The unchanged current C05 supplies the actual calculation. Executable evidence remains finite; correctness, novelty, importance and grade are evaluated from the proofs and source comparisons, not a PASS total.

## 14. Prior art, novelty boundary and external use

### 14.1 Exact before/after comparisons

The primary-source comparison was refreshed on 27 September 2026 KST. The following locators refer to the explicitly linked arXiv versions; journal pagination or typesetting is not silently substituted. The result is a bounded literature assessment, not a proof that no similar result exists anywhere.

| Source and exact locator | Assumptions, object and conclusion in the source | What is additionally proved here |
|---|---|---|
| Biamonte–Turner [R1], section “Vanishing of the Quantum Probability Current,” Methods; cycle-invariant and bipartite results | Time-reversal transition symmetry, diagonal-gauge sufficiency and a stated unconditional propagator-gauge necessity; topology and gauge flux | (7.1) defeats that necessity when read for each fixed Hamiltonian, without disputing the separate support theorems. M treats general $L\pm V$, diagonal freedoms, digons and mixed independent parameters |
| Kadyan–Bhattacharjya [R2], Theorem 2.2, Corollaries 2.4–2.5, Theorem 2.7 | On the same graph, Hermitian unit-gain adjacency matrices are switching-equivalent iff fundamental-cycle gains match; bridges do not constrain flux; switching to the negative matrix is tied to bipartiteness | This supplies gauge tests after magnitudes match, not necessity of entrywise probability equality. M needs the constructive real/mixed reduction and §5 interference coefficients; the fixed $K_4$ exception shows why the distinction matters |
| Levine et al. [R3], §2, Fig. 2 (matrix); §4, Claim 2 (uniform mixing); §2.1 (mixing-matrix definition) | A known oriented $K_4$ signing has simple mixing properties | The matrix is credited, including its diagonal switching. Its role here is an exact fixed-pair exception and a test case for F/T |
| Szigeti et al. [R5], Proposition 1 Eq. (12), Proposition 2 Eqs. (22)/(30), §III C | Short-time quantum-walk amplitudes from shortest paths, remainder bounds, on-site-potential treatment and phase cancellations | The branch-coloured *difference* classification and the endpoint-path lower bound require additional cancellation/parity arguments. J proves the worst-case $2d$ order across all entries; Q specializes standard remainder tools to those witnesses |
| D'Alessandro [R6], §2, Theorem 1 | Controlled quantum-state observability through an invariant observable algebra | The former attribution of a literal $2d^2$ two-Hamiltonian test was incorrect. F instead has a direct merged-gap/Vandermonde proof and improves the elementary fixed-pair sufficient cutoff |
| Wang et al. [R7], §III Eq. (13), §III A/B, Theorem 1; §VI B | Similarity-transformation tests for observable realizations; minimal/nonminimal distinctions; exchange-chain identification modulo signs; a Taylor-based identification algorithm | M decides structural branch-sign visibility with all basis preparations and population effects. T explicitly characterizes the blind algebraic locus of a supplied polynomial pair; it is not the first finite algebraic approach to Hamiltonian identification |
| Marvian–Spekkens [R8], Eq. (2.10), Proposition 1 Eq. (2.11) | A covariant channel preserves asymmetry modes for a specified representation | C is an application; its contribution here is correct typing of the observable and control group, including the dual-rail counterexample to the old interpretation |
| Jansen–Ruskai–Seiler [R9], Theorem 3 Eq. (6) | Finite-time adiabatic projection error with gap and derivative control | W supplies an explicit two-branch schedule and uniform offset gap; the adiabatic theorem is imported |
| Conditional-displacement/qubus literature [R10] | Oscillator-mediated geometric phases and gates | BUS-G is a declared-model record construction with calibrated controls; it is not a new gate principle |
| Repo1 M54/M56/M58/M60/M61/M65/M68/M71/M73/S14 | Transport, grading, branch symmetry, instrument direction, reference bounds and coherence records under their own hypotheses | §12 gives exact interfaces and non-implications; R adds a correlated population-decoding theorem for the separate ARCH model |

The standard Gram inequality in BUS-P, the finite-exponential argument in F, mode selection, Taylor tails and Bernoulli concentration are not counted as novel mathematical principles. Q/F/T/R are useful new integrations and consequences within this manuscript. The main originality assessment concerns M, the constructive mixed witness reduction and sharpness J.

### 14.2 Strongest objections and responses

**“This is only signed-graph switching.”** Switching proves sufficiency. It cannot establish necessity of population equality for a fixed matrix, as (7.1) shows. For independent families, the nonzero witness polynomial and the complete obstruction reduction establish the missing necessity. The reduction is what allows a support decision without searching over times or weights.

**“Shortest-path expansions already give the derivative order.”** Those expansions describe amplitudes; two branch probabilities can agree at all shorter orders because of both gauge alternatives and interference. The endpoint-detuned path proves that every entry can remain equal below $2d$, not merely that one chosen amplitude has a long path. The comparison with [R5] prevents counting walk expansions themselves as new.

**“Genericity is useless for physically tied models.”** M is not extended by assertion. T gives an exact finite polynomial test for such finite models, while the tied $K_4$ family demonstrates the need for a separate method. A practical many-body structural classification remains open.

**“Correlated errors invalidate a binomial tail.”** That objection is correct for marginal bounds. R proves a uniform conditional bound and a pathwise coupling to dominating independent Bernoulli variables; it never assumes independence of the actual records.

**“The reference cost is a group-label artefact.”** The group dependence is now part of the result: total-charge and relative-rail covariance define different allowed controls. BUS-G's calibrated phase is a control input; whether it consumes charge asymmetry depends on the physical representation.

### 14.3 Reusable output and remaining literature uncertainty

An external researcher can use the componentwise support algorithm to eliminate unidentifiable sign hypotheses before fitting couplings; use the exact witness coefficient to choose an observable and certify a small-time signal; apply F/T to exceptional or tied finite models; and use R to prove collective decoding in a sequential interacting array from a row-sum bound. The Python functions expose the support predicate, exact jet iteration and history enumeration as concrete examples.

This assessment does not claim experimental adoption or a published correction of [R1]. Its arXiv statement has been checked; the journal's typesetting has not been independently compared. Foundational sufficiency-side sources listed under [R11] were retained from the lineage without a new equation-level audit here. These are not hidden premises for the necessity proof. A prior theorem with matching hypotheses and conclusions, or a flaw in the obstruction reduction, would reopen the novelty or correctness verdict respectively.

## 15. Limitations, falsifiers and OPEN obligations

1. M/J require independent allowed entries. T handles finite polynomial ties but is not a linear-time graph classification, and does not certify nonpolynomial or infinite-dimensional models without extra work.
2. The sharp derivative order alone gives no signal floor. Q requires actual coefficients and norm bounds; calibration and model error can make (6.4) nonpositive.
3. R assumes the exact sequential diagonal-coupling model and the history-uniform envelope. Simultaneous writes, state leakage, uncontrolled hopping, branch-dependent initial environments or changing couplings require another proof. It gives collective decoding, not independent records or objectivity by itself.
4. ARCH-3 excludes the sufficient bound only under its stated nonzero-neighbour and fixed-resource assumptions; actual failure of all point-source protocols is not established.
5. BUS-P is a static elimination. BUS-G assumes ideal oscillator periods, single-memory connection and calibrated logical controls. Their physical implementation and noise budget remain open.
6. A group-covariance no-go must specify the representation. The dual-rail total-charge sector does not inherit a nontrivial charged-qubit reference bound merely because both use two logical levels.
7. The five named corpus debts in §12.5 stay OPEN. No Born rule, single-event selection or equality of event and geometric clocks follows from the probability calculations.

Reversal triggers are explicit: a generic blind independent support outside U* or A*; a nonzero population difference on a support satisfying either condition; a counterexample to the mixed dumbbell coefficient or graph reduction; a lower-order path witness; a fixed pair with all jets in F zero but later visibility; a history satisfying (10.6) that violates (10.7); or a prior theorem that subsumes M/J under the same hypotheses. Loss of a calibrated experimental margin would invalidate that experiment's Q certificate, not the graph theorem.

## 16. Research-grade and qualification card

**Target:** grade at least 4. **Maintained research grade:** **4**, project-internal and restricted to M/J and the constructive witness calculus. **Candidate grade:** none. **Grade 5:** not claimed. **Role:** SUPPORT/METHOD, FQ2/RQ3; no CORE promotion. **Qualified-human anchor:** NONE.

The v1.0 AUDIT-MAJOR-REVISION verdict remains historical. The H-0420 v1.1 grade and qualification language was the generating GPT lineage's assessment, not an independent referee verdict (F12-02). H-0421 separately records Claude's v1.1 full audit: AUDIT-PASS-MINOR, three S1 findings, three S0 observations, no S2+, all four qualification axes PASS, and grade 4 confirmed in the stated mathematical scope. The supplied evidence ZIP authenticates its scripts and logs, but the narrative audit report referenced by H-0421 was not supplied. The three S0 observations therefore have no available item-level descriptions and are not invented or marked individually closed.

This v1.1.1 review is a correction-only integration with a post-write delta verification, not a fresh independent full audit. The author/verifier overlap remains explicit. The grade is maintained because its load-bearing mathematical statements, witness coefficients, complete reduction and external comparison are retained, while the incorrect gauge shorthand in J is replaced by the edgewise proof in §6. The grade is not inferred from the requested target or from the size of a test suite.

| Mission §1.4 axis | Assessment and continuing basis |
|---|---|
| Correctness | PASS in the declared scope. M and the complete real/mixed obstruction reduction (§§4–5) are unchanged. J now supplies the correct two gauges for all exclusive L/V path assignments. Q/F/T/R and the remaining proofs retain their assumptions and conclusions. No unresolved substantive mathematical finding is identified by the available H-0421 record or this delta verification |
| Novelty | PASS for M/J and the witness calculus. The exact before/after comparison in §14 distinguishes generic probability blindness from gain switching and shortest-path amplitudes. [R3] is correctly divided into the matrix and mixing-theorem locators; the known matrix and standard supporting tools are credited. This remains a bounded literature assessment |
| Significance | PASS. Arbitrary finite mixed independent supports admit a linear-time structural decision and an optimal finite witness order; fixed/tied exceptions are kept separate. These mathematical decisions and constructive witnesses can be reused without assuming Z-Spin physics |
| Verification basis | PASS internally. The displayed proofs, H-0421 cross-lineage opposition, exact witness/jet code and recorded finite searches remain available. The original 18-row suite, auditor formula/operational scripts and focused correction regressions are rerun. Historical results, declarations, numerical checks and universal arguments are kept distinct |

The grade-4 additional requirements remain located: the precise prior-limit comparison (§14.1), the substantive change in decidable problems and sharp order (§§4–6, 14.3), and adversarial objections/counterexamples (§§7, 14.2–15 and the supplied audit evidence). Routine corrections, repeated checks, Taylor/Duhamel/Chernoff/Vandermonde arguments and the known $K_4$ signing are not counted as new breakthroughs.

**Independence.** As H-0421 records, M/J, Q/F/T/R, S/$K_4$, W and the bus results received cross-lineage Claude review. A/B1/DUAL/E/ARCH-1 belong to Claude's earlier lineage, with its second same-lineage review recorded there; this patch does not reset that counter or perform another such full review. The current Codex/GPT correction and deterministic reproduction are disclosed as such. No blank-context or human review is claimed.

**PAPER QUALIFICATION:** PASS. **OUTPUT FORM:** RESEARCH PAPER, internal. **RELEASE LABEL:** FREEZE READY. **Scope disposition:** TERMINAL-IN-SCOPE recommended for this mathematical method after the documented S1 repairs. This does not close the physical selector/instrument debts in §12.5 or terminate the Z-Spin programme. The missing S0 descriptions are a documentary limitation, not evidence of an unreported scientific closure; receiving them can prompt a cosmetic follow-up. A counterexample, proof gap or matching prior theorem under §15 reopens the relevant scientific assessment. H-0421 recommends moving the next substantive research effort to the RQ3 selector rather than expanding this paper solely to increase its version or length.

## 17. Conclusion

Population-only branch-sign identifiability has three distinct mathematical layers. Independent finite supports admit the complete U*/A* classification and the sharp $2d$ witness order. Fixed or polynomially tied matrices admit a finite merged-gap or jet certificate, including exceptional blind families without either gauge. Calibrated coefficients and sequential write controls then support quantitative signal and correlated-decoding bounds. The corpus connections identify exactly which transport, subsystem, symmetry, reference and instrument inputs must be supplied before those mathematical conclusions become a physical record model.

## Availability, AI use and references

**Availability.** The companion package contains the manuscript, executable checker and JSON, release manifest and hashes, frozen audit, integration report, source map and selected private corpus snapshots, current logs, append-only history, and byte-identical original v1.0 upload/package. External primary papers are linked rather than redistributed. No public DOI or public repository has been established.

**AI_TOOL_RECORD.** Seed v1.1–v1.2: Claude, as recorded in the supplied lineage. Seed v1.3: Codex/GPT, including M/J, the mixed witnesses, S/$K_4$, ARCH-2M and the bus analyses. Paper v1.0: Claude audit/integration, with its own packaged referee evidence. Paper v1.1: Codex/GPT audit of v1.0, source verification, deterministic checks, Q/F/T/R derivations and integration. No subagents were used in this v1.1 session. The present checker and prose share an authoring agent. Human direction is the project owner's task instruction; no qualified human scientific review is claimed. The exact original package preserves its own model labels and historical audit statements. Paper v1.1 audit: Claude, as recorded in H-0421 and the supplied evidence. Paper v1.1.1: Codex/GPT correction-only integration, direct [R3] locator check, deterministic reproduction, coloured-path proof repair and freeze-scope review. No subagents were used for v1.1.1.

**Primary references used for the refreshed comparison**

- **[R1]** J. Biamonte and J. Turner, *Topological classification of time-asymmetry in unitary quantum processes*, Journal of Physics A 54, 235301 (2021). [arXiv:1703.02542v2](https://arxiv.org/abs/1703.02542v2). The author initial “N. Turner” in v1.0 was incorrect. Relevant locations: the quantum-probability-current subsection, Methods, cycle-gauge and bipartite results.
- **[R2]** M. Kadyan and B. Bhattacharjya, *Switching equivalence of Hermitian adjacency matrices of mixed graphs*, Australasian Journal of Combinatorics 85(3), 228–247 (2023). [arXiv:2103.13632v2](https://arxiv.org/abs/2103.13632v2). Theorem 2.2, Corollaries 2.4–2.5, Theorem 2.7.
- **[R3]** L. Levine, J. J. Mesapam, B. Mustico, C. Tamon, G. Tucker and H. Zhan, *Uniform Mixing in Chiral Quantum Walks* (2026). [arXiv:2605.04414v2](https://arxiv.org/abs/2605.04414v2). §2, Fig. 2 (matrix); §4, Claim 2 (uniform mixing time). The signing is known.
- **[R4]** N. Reff, *Spectral properties of complex unit gain graphs*, Linear Algebra and its Applications 436, 3165–3176 (2012). [arXiv:1110.4554](https://arxiv.org/abs/1110.4554). Lemma 1.1, inherited switching background; fresh exact comparison is [R2].
- **[R5]** B. E. Szigeti, G. Homa, Z. Zimborás and N. Barankai, *Short time behavior of continuous time quantum walks on graphs*, Physical Review A 100, 062320 (2019). [arXiv:1905.03914v2](https://arxiv.org/abs/1905.03914v2). Proposition 1 Eq. (12), Proposition 2 Eqs. (22)/(30), §III C.
- **[R6]** D. D'Alessandro, *On quantum state observability and measurement*, Journal of Physics A 36, 9721 (2003). [arXiv:quant-ph/0307127](https://arxiv.org/abs/quant-ph/0307127). §2, Theorem 1; corrected attribution in §7.3.
- **[R7]** Y. Wang, D. Dong, A. Sone, I. R. Petersen, H. Yonezawa and P. Cappellaro, *Quantum Hamiltonian Identifiability via a Similarity Transformation Approach and Beyond*, IEEE Transactions on Automatic Control 65(11), 4632–4647 (2020). [arXiv:1809.02965v1](https://arxiv.org/abs/1809.02965v1). §III Eq. (13), §III A/B, Theorem 1; §VI B.
- **[R8]** I. Marvian and R. W. Spekkens, *Modes of asymmetry: the application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, Physical Review A 90, 062110 (2014). [arXiv:1312.0680v2](https://arxiv.org/abs/1312.0680v2). Eq. (2.10), Proposition 1 Eq. (2.11).
- **[R9]** S. Jansen, M.-B. Ruskai and R. Seiler, *Bounds for the adiabatic approximation with applications to quantum computation*, Journal of Mathematical Physics 48, 102111 (2007). [arXiv:quant-ph/0603175](https://arxiv.org/abs/quant-ph/0603175). Theorem 3 Eq. (6).
- **[R10]** T. P. Spiller et al., *Quantum computation by communication*. [arXiv:quant-ph/0509202](https://arxiv.org/abs/quant-ph/0509202). P. van Loock et al., *Hybrid quantum computation in quantum optics*. [arXiv:quant-ph/0701057](https://arxiv.org/abs/quant-ph/0701057). Retained qubus background; the bus identities used here are derived directly in §11.
- **[R11]** Additional lineage background, not a newly audited premise of M/J: T. Zaslavsky, *Signed graphs* (1982) and [survey arXiv:1303.3083](https://arxiv.org/abs/1303.3083); Brown et al., [arXiv:1211.0505](https://arxiv.org/abs/1211.0505); Lu et al., [arXiv:1405.6209](https://arxiv.org/abs/1405.6209); Zimborás et al., [arXiv:1208.4049](https://arxiv.org/abs/1208.4049); Zhang–Sarovar, [arXiv:1401.5780](https://arxiv.org/abs/1401.5780); S.-T. Wang, D.-L. Deng and L.-M. Duan, [arXiv:1505.00665](https://arxiv.org/abs/1505.00665); Sone–Cappellaro, [arXiv:1609.09446](https://arxiv.org/abs/1609.09446); Bartlett–Rudolph–Spekkens, Reviews of Modern Physics 79, 555 (2007). The 2015 Wang reference is not the 2018/2020 Wang et al. source [R7].

Corpus references are the observed versions in §12.1; their exact titles, source URLs, snapshot hashes and usage locators are provided in source_map.json and corpus_connections.md.

## Appendix A. Audit integration and preservation

The original v1.0 Appendix A is a historical Claude audit of seed v1.3, not this audit. It remains byte-identical inside the original upload and package. Its finding F10-01 assigned an unqualified transverse-reference cost; current F11-01 corrects that interpretation rather than silently citing the old “no S2” verdict as current evidence.

| Frozen v1.0 finding | Integrated disposition | Present locator |
|---|---|---|
| F11-01: group-dependent reference cost | Universal total-charge cost withdrawn; relative-phase controls specified | §§8.2–8.3, 11.3, 12.4 |
| F11-02: propagator phases and conjugated gauge | Corrected identities, exact complex-gauge check | §3; C01 |
| F11-03: $K_4$ revivals and matrix attribution | Non-revival qualifier and explicit gauge to the known signing | §7.1; C05 |
| F11-04: observability attribution | Direct proof and sharper finite cutoff; tied-family polynomial criterion | §§7.3–7.4, 14 |
| F11-05: Lemma E domain and averaged contrast | $\vert{}x\vert{}\le1$ proof domain; correct squared-bracket description and general $k$ average | §9 |
| F11-06: ARCH scaling/normalization and BUS-P novelty | Explicit neighbour hypothesis and $1/2$ normalization; Gram inequality credited | §§10.3, 11.1 |
| F11-07: missing definitions/proof and stale locators | Cross-parity proof and self-contained real/mixed reduction | §§4–5, 8.1 |
| F11-08: corpus version and overbroad connection | Current primary-source map and exact observable distinctions | §12 |
| F11-09: stale history and candidate code | Existing H-0418/H-0419 preserved; one new H-0420; no unverified future paper dependency | Appendix B |
| F11-10: evidence taxonomy and independence | Exact gauge calculation; legacy/current evidence separated; low independence disclosed | §§13, 16 |

The valid scientific content of v1.0 is retained: B1, DUAL, C, M, the six witness types and unified coefficients, J, K4/S and the non-resonance lemma, A/C/D, E and Lemma E, W, ARCH-1/2M/3, BUS-P/G and the conditional corpus interface. Changed claims are repaired or narrowed at their main location, not left contradicted by an added erratum. Added results Q, F/T and R appear in the mathematical body with proofs. Obsolete release metadata and unsupported numerical/candidate-code applications are preserved only as provenance.

## Appendix B. Version lineage and append-only history

| Stage | Origin and contribution |
|---|---|
| Successor seed v1.0 | Claude; original question and route plan |
| Seed v1.1 | Claude; cross-parity, gauge sufficiency, partial real classification, two-level writing; actual H-0418 records this seed |
| Seed v1.2 | Claude; duality, real witness work, ARCH development; no retroactive use of H-0419 |
| Seed v1.3 | Codex/GPT; M/J/S, mixed witnesses, fixed exception, ARCH-2M, buses and robust writing |
| Paper v1.0 | Claude; integrated paper, audit of seed v1.3 and historical grade card |
| Paper v1.1 | Codex/GPT; frozen v1.0 audit, corrected integrated paper, Q/F/T/R, source-level corpus comparison and new checker |
| Paper v1.1 audit | Claude; H-0421, cross-lineage and same-lineage scopes disclosed separately |
| Paper v1.1.1 | Codex/GPT; S1 corrections, current verification and freeze-scope review; no new scientific result claimed |

The v1.1 package preserves its H-0420 event and earlier history. For this release the supplied authoritative history ends at H-0421, the Claude audit event. The companion history preserves those bytes and appends only H-0422 for v1.1.1; H-0420 is not rewritten. Its author-assessment status is clarified in the new entry and §16. No remote history, Manifest Log, Mission, rule or corpus manuscript was modified. Repo1 connections and source snapshots are inherited at the supplied v1.1 versions, with their hashes checked; this patch does not claim a new live inventory of Repo1.

## Appendix C. Load-bearing claim map

| Claim | Quantifier and status | Novelty/role | Proof and falsifier |
|---|---|---|---|
| M74.B1 / DUAL / C | All specified finite pairs; time dependence only with fixed gauge for B1; PROVEN | Imported/specialized | §3; counterexample to the stated identity |
| M74.M | Almost every parameter in each independent mixed support; PROVEN | Central classification | §§4–5; blind independent family outside both alternatives |
| M74.WITNESS | Exact leading coefficients on retained substructures; PROVEN | Constructive proof asset | §5; coefficient or orientation mismatch |
| M74.J | Generic upper order and all-entry lower path order; PROVEN | Central sharpness | §6; witness below $2d$ on the path |
| M74.Q | Fixed coefficient, norms and calibrated perturbations; PROVEN | Quantitative specialization | §6.1; violation of the analytic remainder bound |
| M74.K4 / S | Fixed-matrix exception and exact merged-frequency equality; PROVEN | Known matrix, new application; spectral criterion specialized | §§7.1–7.2; gauge at a non-revival time or failed expansion |
| M74.F / T | All fixed pairs / polynomial tied families in a nonempty open real domain; PROVEN | Finite certificate and algebraic consequence | §§7.3–7.4; all tested jets zero but later visibility |
| M74.A / C / D | Normalized states/effects and named representations; PROVEN | Elementary/imported | §8; covariance or normalization violation |
| M74.E / W | Declared two-level controls and static offsets; PROVEN | Specialized control laws | §9; invalid domain or gap estimate |
| M74.ARCH1 / 2M | Exact sequential model, all finite $R$; PROVEN | History identity and marginal bound | §§10.1–10.2; full distribution mismatch |
| M74.R | Conditional envelope at every history, all finite $R$; PROVEN | Correlated decoding extension | §10.4; domination failure under the actual hypotheses |
| M74.ARCH3 | Fixed density, source/moments and persistent nonzero neighbour; PROVEN only as sufficient-condition failure | Resource diagnosis | §10.3; missing lower-bound hypothesis |
| M74.BUSP / BUSG | Static positive quadratic bus / ideal active controls; PROVEN in model | Standard inequality / known mechanism | §11; model or control mismatch |
| M74.Z | Block-sign sufficiency exact; physical assignment conditional | Corpus interface | §12.2; a different branch assignment does not falsify the theorem |
| M74.PHYSICAL | Action-derived carrier/instrument and clock identification | OPEN | §12.5; no closure or CORE promotion |

## Appendix D. v1.1.1 correction and freeze record

| Finding | Integrated disposition | Verification |
|---|---|---|
| F12-01, S1: [R3] locator | §7.1, §14.1 and [R3] distinguish §2 Fig. 2 from §4 Claim 2 | Direct arXiv v2 source comparison; the matrix attribution is preserved |
| F12-02, S1: review/grade provenance | Front card, §16 and Appendix B identify H-0420 as author assessment and H-0421 as the subsequent Claude review | Original history preserved; current statements scoped to the supplied audit record and this correction-only verification |
| F12-03, S1: J path gauges | §6 supplies $g_U,g_A$ recursively for every exclusive L/V colouring; (6.1) and the $2d$ bound are retained | Edgewise proof for arbitrary $d$; 62 exact coloured-path regressions; old-gauge and wrong-sign injections |
| Three S0 observations in H-0421 | Detailed audit narrative absent from the supplied inputs | No invented IDs, remedies or item-level closure; no S2+ is reported in H-0421 |
| Additional evidence-accounting correction | Auditor's three formula and two operational declarations excluded from calculated-evidence counts | Original files retained; R03/R04 compute the omitted cases and report their own scope |

The machine-readable edit register and unified diff record every manuscript change. Numbered equations, central mathematical sections outside the J repair and the source snapshots are checked for preservation. The post-write report provides the final hashes, actual run results, remaining scope limitations, stop rule and reopening conditions. No universal theorem or research grade is certified by a file-integrity check.
