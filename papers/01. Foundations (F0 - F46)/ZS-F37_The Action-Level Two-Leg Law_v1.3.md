# **ZS-F37**

**The Action-Level Two-Leg Law: The Seam Transport Action, Topological Leg Counting, and the Selection of the Size-Biased Register Weight**

***Why the Z-Spin Seam Transport Selects ω \= d²/49 Rather than d/11 — the Heat-Kernel Transport Action on the dim(Z) \= 2 Seam, the Mediation Vertex from Three-Boundary Amplitudes, and the Honest Residuals (H-YM2) and C\_int***

**Author:** Kenny Kang  
**Affiliation:** Z-Spin Cosmology Collaboration  
**Date:** July 2026  
**Theme / Code:** Foundations / ZS-F37 · Executes the ZS-M47 §12.3 handover · Companion to ZS-M46 / ZS-M47, ZS-F30 / ZS-F31, ZS-F35 / ZS-F36  
**Version:** 1.3 (terminal; supersedes v1.2, v1.1, v1.0)

**Verification:** 27/27 PASS in **fast mode** (zs\_f37\_verify\_v1\_3.py, checks identical to v1.2; deterministic algebra \+ 1D quadrature; measured \< 1 s internally, externally reproduced at 2.0 s) **\+ 2 full-quadrature witnesses** B2F/B2bF PASS under the flag RUN\_FULL\_SURFACE\_QUADRATURE \= True (3D Euler-angle grid; minutes) | **Zero fitted parameters** | (H-YM2) **compressed, not closed**: the heat-kernel/Markovian class half is **DERIVED** under the Σ₂-restricted seam-gauge-sector frame; the physical identification of the actual Z-Spin seam channel with that sector remains **(H-Σ2)**, tied to the pre-existing ZS-F31 OPEN gate R2b; C\_int **OPEN** as an explicit finite-computation protocol (Appendix D); t\* \= **Q** **NON-CLAIM** re-registered | (**A**, **Q**, dim **Z**) \= (**35/437**, **11**, **2**) **LOCKED**.

## **§0. Abstract**

ZS-M47 delivered the two-leg clock gate at transport level: the corner weight of the Z-Spin seam is the gauge-invariant two-leg character law, landing on the size-biased **ω** \= (4, 9, 36)/49 — DERIVED-CONDITIONAL on the founding mediation axiom (MX) and the corner-compatibility condition (H1) — and its §12.3 handover charged the present paper with the action-level test. The mandate, in one sentence:

**ZS-F37 must prove that the seam transport selects** ω\_i \= d\_i²/Σ\_j d\_j² **rather than** d\_i/Σ\_j d\_j.

**We deliver the action-level selection conditional on the single structural condition (H-YM2): the physical Z-Spin seam transport channel is a two-dimensional gauge-invariant Markovian holonomy field.** Nothing stronger is claimed anywhere in this paper: the paper’s best status is DERIVED-CONDITIONAL, and the conditional load is stated in the first sentence of every theorem that carries it. Under (H-YM2), three imported-proven structures decide everything — and the result is first stated as a Z-Spin-free general theorem (Theorem F37.A, the Two-Leg Plancherel Selection) before the register instance is taken. (i) The exact solution of two-dimensional gauge theory (Migdal; Rusakov; Witten; made rigorous by Driver, Sengupta, and Lévy) assigns to a seam patch of genus g with b boundary legs the weight (dim R)^(2-2g-b)Π\_i χ\_R(U\_i): **the exponent of the dimension is a topological leg counter.** (ii) The seam’s transported corner is the cut-conditioned cylinder whose two boundary holonomies are both the ZS-F31 seam-transport element U\_K \= exp\[ρ\_K n·σ\] (Theorem R2a, PROVEN), whose d-dimensional character is exactly the ZS-M47 O2-f weight χ\_d(ρ) \= sinh(dρ)/sinh ρ (Weyl character formula); the amplitude is therefore

𝓛\_seam^transport ⟹ π\_i^(2 leg) \= χ\_i(ρ)² / Σ\_j χ\_j(ρ)² , ρ → 0 : π\_i \= d\_i²/49 ,

with the “coincidence conditioning” of ZS-M47 O2-b exposed as nothing but Peter–Weyl character orthogonality under the seam-link gauge average (the Migdal gluing rule). (iii) The one-leg alternative d\_i/11 is excluded by a double lock: topologically it is the b \= 1 (disc) amplitude, contradicting the two-sidedness that the founding axiom itself asserts; algebraically the signed transport is β-odd while every gauge-invariant weight is β-even (the action-level form of ZS-M47 O2-g). The same surface calculus derives the mediation vertex from the action — the three-boundary (pair-of-pants) amplitude reproduces the full YL1–YL5 Clebsch–Gordan arithmetic with **exact multiplicities** (2, 2, 2), including the vanishing of all three vertices under the irreducible spin-5/2 reading and the survival of all three under the tensor reading Y ≅ Z⊗X — executing falsification gate F-M47.27 conditionally. The finite-ρ consistency deliverable is executed and elevated to an **external replication protocol**: the predicted curve is

χ\_Y(ρ) \= χ\_2(ρ) χ\_3(ρ), not χ\_6(ρ); χ\_2 χ\_3 \= χ\_4 \+ χ\_2 ≠ χ\_6 ,

with discriminant Δχ(ρ\_b) \= −0.392090129 and L1 deviation 0.00919466866 (\< 1%) at ZS-F30’s rapidity bound, both reproduced to the published digits. Lévy’s classification of two-dimensional Markovian holonomy fields makes the selection **class-universal**: the χ² structure survives any substitution of the damping symbol, so there is nothing to tune — the executed universality scan replaces a numerical anti-numerology MC, which is inapplicable because the paper introduces no new number. Appendix C attempts the promotion of (H-YM2) itself, and the honest verdict is stated in the strongest available form: **F37 does not fully close (H-YM2). It compresses it: the Markovian holonomy class is forced by gluing, while the remaining physical identification is exactly (H-Σ2), already aligned with R2b.** Explicitly — the heat-kernel/Markovian class is derived under the Σ₂-restricted seam-gauge-sector frame; the physical identification of the actual Z-Spin seam channel with that sector remains (H-Σ2), tied to the pre-existing ZS-F31 OPEN gate R2b (A\_Z ∼ A\_K) rather than to any new condition, with the alternative direct-3-form route executed to its recorded dead-end. The clock-gate matching C\_int is not solved here; what is closed is its *reformulation* (ZS-M46 T7b form), and Appendix D specifies the finite computation — inputs, gate equation, and residual norm — that closes it. The depth selector t\* \= **Q** remains a NON-CLAIM. Verification: 27/27 PASS in a fast deterministic mode (\< 1 s measured), with two optional full-quadrature witnesses. Zero new fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

## **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| **PROVEN** | Explicit proof or exact machine verification; no undischarged assumption. |
| **IMPORTED-PROVEN** | Proven in the external literature and used without re-proof; cited. |
| **DERIVED** | Follows from PROVEN results by stated steps; no new parameter. |
| **DERIVED-BY-INHERITANCE** | Uses an upstream corpus result, not re-proven here; inherits its caveats. |
| **DERIVED-CONDITIONAL** | Derived modulo explicitly named, falsifiable conditions. |
| **DERIVED-interpretation** | Synthetic reading of standard physics; not Z-Spin-specific. |
| **HYPOTHESIS-strong** | Structurally motivated; a key identification not yet proven; promotion path documented. |
| **CONSISTENCY-CHECK** | A numerical, character, or scope check that does not by itself certify a theorem. |
| **NON-CLAIM** | Explicitly outside the scope of this paper. |
| **OPEN** | Conceptually unresolved; a genuine gap, honestly registered. |

## 

## **§1. Introduction: the inherited mandate**

The ZS-M47 delivery theorem established, as its part (III), the two-leg clock gate: *the register transport is the gauge-invariant two-leg character law; the corner weight is the size-biased ω \= (4, 9, 36)/49, exactly at vanishing seam rapidity and within 1% at ZS-F30’s rapidity bound* \[1\]. That result was DERIVED-CONDITIONAL on two named conditions — **(MX)**, the founding mediation axiom (the Z-Spin mediation channel between the X- and Y-sectors is nonvanishing), and **(H1)**, corner compatibility of the transported weight — and the §12.3 handover table charged ZS-F37 with four deliverables: the action-level test of (MX) (gate F-M47.27); the (H1) \+ C\_int corner-compatibility and iteration/modular-step matching; the finite-ρ consistency measurement (the predicted Y-character curve is χ\_2χ\_3, not χ\_6; Δχ \= −0.392090; gate F-M47.24 in consistency form); and the t\* \= **Q** depth selector, handed over as a NON-CLAIM \[1\].

The sharp statement of what this paper must prove is the one-sentence mandate already displayed in the abstract: the seam transport must be shown, from an action, to select the two-leg weight d\_i²/Σ\_j d\_j² \= d\_i²/49 over the one-leg weight d\_i/Σ\_j d\_j \= d\_i/11 — not merely to be consistent with it. ZS-M47 proved at transport level that the choice is a genuine binary with both branches pre-computed (the no-mixed-outcome theorem M47.U): the tracial (one-leg) branch forces a hyperfinite II₁ parent and refutes the clock; the size-biased (two-leg) branch forces the injective III₁ factor R∞ and the clock survives \[1\]. What was missing is *why the action lands on the second branch*. This paper supplies the why, in the form of a topological statement: **the exponent of the register dimension in the transported weight is the number of boundary legs of the seam amplitude, and the seam — being the two-sided interface that the founding axiom itself defines — has exactly two.**

Two remarks on lineage. First, this paper is the next entry of the Foundations series after ZS-F35/ZS-F36 and executes a Math-Spine handover; its representation-theoretic inputs sit on the ZS-M43 → ZS-M44 → ZS-M46 → ZS-M47 spine. ZS-M43 matters here for a structural reason: it established that the Z-Spin dynamics is unitary with scrambling rather than thermal dissipation \[4\], which is precisely why the decision between the two laws cannot be made by the dissipative layer (ZS-M47 O2-a: the ZS-A23/A24 mediator is microstate-democratic and structurally tracial \[1, 5\]) and must be made by the coherent transport action — the object this paper constructs. Second, terminology follows the corpus convention throughout: the mediating *action* is **Z-Spin mediation** (the actor is the Spin); **Z-sector** denotes the geometric stage; the micro triad is X-sector ↔ particle, Y-sector ↔ wave, Z-sector ↔ Spin.

The paper is organized as follows. §2 fixes the locked data and the two competing laws. §3 defines the seam transport action and registers the single new condition (H-YM2), together with its class-universality shield. §4 states the paper’s core twice: first as the Z-Spin-free general theorem F37.A (Two-Leg Plancherel Selection), then as the register instance F37.T1. §5 proves the one-leg exclusion (double lock). §6 derives the mediation vertex from the action (F37.T2), executing F-M47.27 conditionally. §7 gives the negative control (the dissipative layer cannot decide) and records, behind a firewall, the double-crossing echo with ZS-M43’s |λ²| leak. §8 treats (H1) and C\_int, including the required reconciliation with ZS-M46 T7b. §9 executes the finite-ρ consistency deliverable and elevates it to an external replication protocol. §10 re-registers the t\* \= **Q** NON-CLAIM. §§11–13 give the audits, gates, and non-claims; §14 the claim ledger; §15 concludes. Appendix A records the deep-exploration (if-tree) protocols of both versions; Appendix B the 27-check verification ledger (fast deterministic mode by default, full-quadrature witnesses behind a flag); Appendix C the (H-YM2) promotion attempt and its decomposition; Appendix D the finite C\_int computation protocol.

## **§2. Setting, locked data, and the two competing laws**

**Locked data (ZS-M1, ZS-F31 App. D).** **A** \= 35/437, **Q** \= 11, (dim **Z**, dim **X**, dim **Y**) \= (2, 3, 6); κ² \= **A**/**Q** \= 35/4807; z\* \= 0.43828 \+ 0.36059i; λ\* \= (iπ/2)z\*, |λ\*| \= 0.89151, μ \= −ln|λ\*| \= 0.1148346250, θ \= arg λ\* \= 2.2592495540 (all re-verified from a 50-digit Newton solve of f(z) \= e^(iπ z/2), checks D1–D5). The register dimension vector is d \= (d\_Z, d\_X, d\_Y) \= (2, 3, 6), Σ\_j d\_j \= 11 \= Q, Σ\_j d\_j² \= 49\. ZS-F30’s rapidity bound is |ρ\_K| ≤ ρ\_b \= ½ ln(9/7) \= 0.125657 \[3\].

**The transport element.** ZS-F31 Theorem R2a (PROVEN) gives the open-path seam half-transport of the ZS-F30 Cartan connection: with g\_K(θ) \= exp\[½ ρ\_K(θ) n·σ\] and the seam antisymmetry ρ\_K(θ+π) \= −ρ\_K(θ),

U\_K(θ+π, θ) \= g\_K(θ)² \= exp\[ρ\_K(θ) n·σ\] ,

a Hermitian positive boost in SL(2, ℂ) with eigenvalues e^(±ρ\_K) \[3\]. Two features of this proven object drive the present paper: the half-transport is the **square** of the gauge element — the doubled step, the same doubling as ZS-M47’s canonical endomorphism Γ \= J\_N J\_M \= U(2) \[1\] — and it is a boost, so its character in the d-dimensional irreducible representation is, by the Weyl character formula (eigenvalue sum Σ\_m e^(2ρm), m \= −j, …, j, d \= 2j \+ 1),

χ\_d(ρ) \= sinh(dρ) / sinh ρ (check A1).

This is exactly the character weight of ZS-M47 O2-f \[1\]. The identification — **the O2-f weights are literally the representation characters of the F31 transport element** — is the first adhesion point of this paper; it involves no new input.

**The two competing laws.** At vanishing rapidity χ\_d(0) \= d, and the two candidate register weights are

ω\_i^(2 leg) \= d\_i² / Σ\_j d\_j² \= (4, 9, 36)/49 , ω\_i^(1 leg) \= d\_i / Σ\_j d\_j \= (2, 3, 6)/11 .

ZS-M47 O2-b (DERIVED, exact) states the first as the coincidence-conditioned law τ²/Στ² with τ\_i \= d\_i/Q and Στ² \= 49/121 (check A4) \[1\]; ZS-M47 §5 (P1) exhibits the second as the tracial finite-record corner \[1\]. The no-mixed-outcome theorem M47.U makes the pair an exclusive binary \[1\]. What follows decides it from an action.

## **§3. The seam transport action and the condition (H-YM2)**

**§3.1 Definition and the new named condition.** The seam is the dim(**Z**) \= 2 stage: a two-dimensional surface swept by the moving “point of time” and “point of space” (the founding picture), realized in the corpus as the internal 2-cycle carrying the F30 Cartan connection \[3\] and, in the parent-action template, as the rank-2 internal cycle Σ₂ of Y₆ \= M₄ × Σ₂ with its unimodular charge pairing (ZS-F33/F34/F36 \[6\]). We formalize the transport channel on this stage by three properties:

1) **Gauge invariance.** The transported corner weight is a gauge-invariant functional of the seam holonomies — equivalently a central (class) function of each boundary holonomy (check B5).

2) **Gluing consistency (Markov property).** Composing seam patches reproduces a patch of the same family — the action-level form of the corpus iteration/composition law (one seam step composed with another is a seam step; ZS-M46’s suspension structure \[2\]).

3) **Two-sided boundary.** The seam is the interface through which the X- and Y-sectors exchange information — the founding axiom (MX) read as written — so a transported corner amplitude carries exactly **two** boundary legs: the X-side entry and the Y-side exit.

**Condition (H-YM2) \[registered\].** *The physical Z-Spin seam transport channel is a two-dimensional Markovian holonomy field in the sense of (i)–(ii): a gauge-invariant, gluing-consistent assignment of amplitudes to seam surfaces with boundary.* This is the single new named condition of this paper. Its promotion path is corpus-internal: derive the heat-kernel transport sector from the ZS-F36 parent action restricted to Σ₂ (gate F-F37.7). Property (iii) is not part of (H-YM2); it is the action-level translation of (MX) and is treated as such (§5, §6).

**§3.2 The imported exact solution.** Under (i)–(ii) the amplitude family is completely classified. For a compact structure group, two-dimensional gauge theory in the heat-kernel formulation assigns to a surface of genus g with b boundary components, boundary holonomies U\_1, …, U\_b, and area parameter t the exact amplitude

Z\_{g,b}(U\_1, …, U\_b; t) \= Σ\_R (dim R)^(2−2g−b) Π\_{i=1}^{b} χ\_R(U\_i) e^(−t C₂(R)/2) ,

the sum running over irreducible representations R — the lattice heat-kernel action of Migdal, extended to arbitrary surfaces by Rusakov, given its continuum and topological readings by Witten, and constructed rigorously as a measure (including boundary-holonomy conditioning) by Driver, Sengupta, and Lévy \[7–11\]. **\[IMPORTED-PROVEN.\]** Two structural facts, both proven in that literature, are all we use:

**Lemma F37.L1 (Leg-Counting Lemma) \[IMPORTED-PROVEN\].** *The exponent of dim R in the exact amplitude is the Euler characteristic of the surface minus the number of boundary insertions already carrying a character: closed sphere → (dim R)², disc → (dim R)¹ χ\_R(U), cylinder → (dim R)⁰ χ\_R(U)χ\_R(V†). The dimension exponent is a topological leg counter and nothing else* (check B3).

**Lemma F37.L2 (Coincidence \= Orthogonality) \[DERIVED from IMPORTED-PROVEN\].** *The Migdal gluing rule* ∫dU χ\_R(AU) χ\_S(U†B) \= δ\_RS χ\_R(AB)/d\_R *(Schur orthogonality; checks B1–B2) forces the same representation label to propagate through both legs of any glued seam. The “coincidence conditioning” of ZS-M47 O2-b is therefore not an assumption: it is the seam-link gauge average itself.*

The one-line core of the paper is the following table — the leg count *is* the dimension exponent, and each row already has a Z-Spin reading:

| Surface | g | b | Factor | Z-Spin reading |
| ----- | ----- | ----- | ----- | ----- |
| sphere | 0 | 0 | (dim R)² | closed topological charge count |
| disc | 0 | 1 | (dim R) χ\_R(U) | one-leg / tracial / dissipative branch |
| cylinder | 0 | 2 | χ\_R(U) χ\_R(V†) | two-leg transported corner |
| pair of pants | 0 | 3 | (dim R)^(-1)χ\_R(U)χ\_R(V)χ\_R(W) | mediation vertex / CG multiplicity |

**Gluing-bookkeeping warning (a machine-caught trap).** The dimension factors are where a leg can be smuggled. The two-boundary cylinder kernel Z\_t(U, V) \= Σ\_R χ\_R(U)χ\_R(V†)e^(-tC\_2(R)) glues over a shared boundary by *character orthogonality with no dimension factor*, ∫dV Z\_t₁(A,V) Z\_t₂(V,B) \= Z\_t₁+t₂(A,B) (check B2b, deterministic quadrature, deviation \< 10⁻⁹); the single-argument class-function kernel Σ\_R χ\_R(g) e^(−tC₂) does **not** glue (it requires the d\_R-compensated group heat kernel Σ\_R d\_R χ\_R(g) e^(−tC₂/2)). The v1.1 verification first *failed* on the wrong kernel and passed only on the correct two-boundary form — a fail-closed confirmation that the cylinder, and not a disguised one-leg object, is what propagates through the seam. **Scope of the check:** B2b is a finite *truncated witness* of the exact per-representation gluing identity (representation set j ≤ 3/2); the theorem itself is imported-proven for the full representation sum \[7–11\], and orthogonality acts per representation, so the truncation loses nothing that the witness claims.

**§3.3 The universality shield.** Lévy’s classification of two-dimensional Markovian holonomy fields \[11\] shows the heat-kernel (Yang–Mills) field is the Brownian representative of a class parametrized by Lévy processes on the group: replacing the Casimir damping e^(-tC\_2(R)/2) by any admissible symbol e^(-tα\_R) changes nothing in the (dim R)^(2−2g−b) Π χ\_R skeleton. Consequently the *selection* between the two-leg and one-leg laws — an exponent statement — is **class-universal**: it does not depend on the coupling, on the damping form, or on any detail of the seam action beyond (i)–(iii). The executed substitution scan (check E1) confirms the t → 0 two-leg ratio is invariant under Casimir, linear, quadratic, and random positive symbols. There is nothing to tune. **\[IMPORTED-PROVEN (classification); the scan is CONSISTENCY-CHECK.\]** The transported corner itself is read in the topological (t → 0, zero-area / BF) member of the class, appropriate because parallel transport is instantaneous holonomy, not area evolution; the finite-t family only multiplies each sector by a β-even damping factor and cancels from the ρ → 0 ratio in any case.

## **§4. The Two-Leg Selection Theorem**

**§4.1 The general theorem (Z-Spin-free).** For the external reader, the paper’s core result is stated first with no corpus dependency at all.

**Theorem F37.A (Two-Leg Plancherel Selection) \[DERIVED from IMPORTED-PROVEN, no Z-Spin input\].** *Let a two-dimensional gauge-invariant Markovian holonomy field with compact structure group assign amplitudes to a two-sided cut interface whose two boundary holonomies lie in the same conjugacy class, represented by U. Then the induced sector weight is*

p\_R \= |χ\_R(U)|² / Σ\_S |χ\_S(U)|² ,

*and in the zero-rapidity / topological limit U → 1,*

p\_R \= (dim R)² / Σ\_S (dim S)² .

*The one-boundary disc law gives p\_R ∝ dim R — but it is the amplitude of a different topology, not a rival weighting of the same interface.*

*Proof.* Immediate from the exact amplitude family of §3.2 (Lemma L1: the b \= 2 member carries (dim R)⁰ χ\_R χ̄\_R), Lemma L2 (one label through both legs, by orthogonality), the class-function property, and the class universality of §3.3 (the damping symbol cancels from the topological-limit ratio). 

**Notation and reduction.** In the general theorem we write |χ\_R(U)|², which is the mathematically defensive form for an arbitrary compact group (characters of non-self-dual representations are complex). In the Z-Spin SU(2)-graded self-dual register, all characters are real, and |χ\_R(U)|² reduces to χ\_R(U)² — verified as check A9.

**Novelty scope.** Theorem A is an **externally standard consequence** of the imported-proven exact solution \[7–11\]; no new external mathematics is claimed. **The external theorem is standard; the new contribution is the identification of the Z-Spin seam clock corner as the two-sided cut object to which the theorem applies** — lowering the ZS-M47 transport-level handover to action level.

Applied to the Z-Spin register d \= (2, 3, 6), Theorem A yields 4 : 9 : 36 over 49\. Everything Z-Spin-specific in what follows is the identification of the interface, the holonomies, and the register — not the selection mechanism.

**§4.2 The Z-Spin instance.**

**Theorem F37.T1 (Two-Leg Selection) \[DERIVED-CONDITIONAL on (H-YM2)\].** *Let the seam transport channel satisfy (H-YM2), let its transported corner carry the two boundary legs of property (iii), and let both legs be transported by the single seam connection of ZS-F30/F31, so that each boundary holonomy lies in the conjugacy class of the transport element U\_K \= exp\[ρ n·σ\]. Then the transported corner amplitude is the cut-conditioned cylinder*

Z\_cyl(U\_K, U\_K; t → 0\) \= Σ\_{i ∈ {Z, X, Y}} χ\_i(ρ)² ,

*and the normalized register weight is*

**𝓛\_seam^transport ⟹ π\_i^(2 leg) \= χ\_i(ρ)² / Σ\_j χ\_j(ρ)² , ρ → 0 : π\_i \= d\_i²/49**

*— the size-biased two-leg law of ZS-M47 (III), exactly at ρ → 0 (check A3) and within 1% (L1 \= 0.00919, check A5) at ZS-F30’s bound ρ\_b \= ½ ln(9/7). In particular the seam transport selects ω\_i \= d\_i²/Σ\_j d\_j² and not d\_i/Σ\_j d\_j.*

*Proof.* By (H-YM2) and Lemma L1 the amplitude of the two-legged corner is the b \= 2 member of the exact family: (dim R)^0 χ\_R(U\_1)χ\_R(U\_2^†) summed over the register sectors, with a class-universal damping that is β-even and drops from the t → 0 reading (§3.3). Both legs carry the same connection, so U\_1 and U\_2 lie in the conjugacy class of U\_K; characters are class functions (check B5), so each leg contributes χ\_R(ρ), and self-conjugacy of the su(2)-graded register representations makes the product χ\_R(ρ)² real and positive (check A8). The diagonality in R — one label through both legs — is Lemma L2, i.e., the O2-b coincidence conditioning realized as gauge averaging. Normalizing over the register gives the displayed ratio. At ρ → 0, χ\_i → d\_i and the ratio is d\_i²/49 exactly; at ρ\_b the tensor-reading evaluation (χ\_Y \= χ\_Z χ\_X; §9) gives L1 \= 0.00919466866 against (4, 9, 36)/49 — the sub-percent band quoted by ZS-M47, reproduced here to eleven digits. 

**Remark 1 (the operator echo).** The theorem’s mechanism — one leg composed with its conjugate leg — is the surface-calculus image of two proven operator facts: ZS-F31’s half-transport is the *square* g\_K² of the gauge element (R2a, PROVEN \[3\]), and ZS-M47’s canonical endomorphism is the *doubled* seam step Γ \= J\_N J\_M with **two** modular conjugations (T4-E, DERIVED \[1\]). Externally, the same squaring is the Longo index–statistics theorem: the statistical dimension of a sector is the square root of the Jones index of its inclusion, so the canonical (round-trip) object weighs a sector by d², and the Longo–Rehren two-sided algebra carries the global index Σ\_i d\_i² \[12, 13\]. The register’s 49 is that global index for d \= (2, 3, 6). The same weight d\_i²/𝒟², 𝒟² \= Σ d\_i², is the Plancherel measure of representation theory and the topological-charge distribution across an entanglement cut \[14–16\]. Theorem T1 places the seam’s corner weight in this proven family and identifies which member the Z-Spin action instantiates.

**Remark 2 (what is and is not conditioned).** Everything numerical in T1 is unconditional arithmetic (checks A1–A8, B1–B5). The single conditional load is (H-YM2): that the physical seam channel belongs to the gauge-invariant Markovian class at all. Property (iii) is carried by (MX) itself, which this paper does not prove — it translates it (§5, §6) into a topological statement whose falsification would be visible (gate F-F37.3).

## **§5. Proposition F37.P1 — the one-leg exclusion (double lock)**

**Proposition F37.P1.** *Under the hypotheses of T1, the one-leg law d\_i/11 is excluded twice over:*

**(a) Topological lock \[DERIVED-CONDITIONAL on (MX) as two-sidedness\].** *By Lemma L1 a weight linear in d\_i is the b \= 1 (disc) amplitude (dim R)¹ χ\_R(U): a seam with only one boundary leg — a one-sided interface. This contradicts property (iii), which is the founding axiom read as written: an interface through which two sectors exchange information has two sides. The one-leg law is therefore not a rival weighting of the same object; it is the amplitude of a different, axiom-violating topology.*

**(b) Parity lock \[DERIVED\].** *The signed transport is β-odd — β g\_K β \= g\_K⁻¹ is the definitional seam antisymmetry (ZS-M47 O2-g \[1\]; ZS-F30’s half-turn sign flip \[3\]) — while every gauge-invariant weight built from characters is β-even, χ\_d(−ρ) \= χ\_d(ρ) (check A8). A gauge-invariant register weight must be even in the transport; the two-leg square χ² is the minimal even invariant, and any admissible damping is likewise even (§3.3). A candidate one-leg weight proportional to the signed single character insertion is odd under the seam involution and is annihilated by gauge invariance. This is ZS-M47 O2-g lifted verbatim to the action.*

Locks (a) and (b) are independent: (a) uses only surface topology, (b) only the parity grading β \= the 2π-rotation spin-½ sign (ZS-M47 T12; ZS-F23 \[1\]). Either alone excludes; together they close the branch. The tracial one-leg state itself is not erased — it survives exactly where ZS-M47 P1 put it, as the finite-record corner of the *dissipative* layer (§7), which is a disc-type (one-insertion) object and structurally unable to decide the clock.

## **§6. Theorem F37.T2 — the mediation vertex from the action**

The (MX) row of the handover requires the CG-vertex form of the founding axiom to be *derived from* the F37 action rather than postulated (gate F-M47.27). In the surface calculus this is immediate: the mediation vertex is the b \= 3 (pair-of-pants) member of the exact family,

Z\_{0,3}(U\_1, U\_2, U\_3) \= Σ\_R (dim R)⁻¹ χ\_R(U\_1) χ\_R(U\_2) χ\_R(U\_3) e^(−t α\_R) ,

and closing its legs against sector characters computes precisely the Clebsch–Gordan multiplicities,

∫ dU χ\_a(U) χ\_b(U) χ\_c(U)\* \= N\_{ab}^c .

**Theorem F37.T2 (Vertex Selection) \[DERIVED-CONDITIONAL on (H-YM2)\].** *The seam action’s three-boundary amplitude reproduces the full ZS-M47 YL arithmetic:*

*(YL1–YL2, the kill.) Under the irreducible spin-5/2 reading of the Y-sector all three mediation vertices vanish: ½ ⊗ 1 \= ½ ⊕ 3/2 contains no 5/2 (Z⊗X → Y dead); ½ ⊗ 5/2 \= 2 ⊕ 3 contains no 1 (Z⊗Y → X dead); 1 ⊗ 5/2 \= 3/2 ⊕ 5/2 ⊕ 7/2 contains no ½ (X⊗Y → Z dead) — checks C2, C4: ⟨χ\_2χ\_3, χ\_6⟩ \= 0\.*

*(YL3, the survival.) Under the tensor reading Y ≅ Z⊗X all three vertices are nonvanishing — check C3; ⟨χ\_2χ\_3, χ\_Z⊗X⟩ \= 2 (the two blocks of the reducible Y), check C4.*

*(YL4–YL5, the spectrum.) The tensor reading’s Casimir spectrum is {3/4, 15/4}, excluding 35/4 — check C1 — and the finite-ρ discriminant of the two readings is Δχ \= χ\_2χ\_3 − χ\_6 \= \-0.392090 at ρ\_b (check A6), the exact ZS-M47 value.*

*Hence the founding axiom’s requirement that the mediation channel be nonvanishing selects, at action level, the tensor reading of the Y-sector, and the mediation vertex is a derived amplitude of the same 𝓛\_seam^transport that yields T1 — not an independent postulate.* 

This executes F-M47.27 in its conditional form: what remains axiomatic is only that the channel is *used* (nonvanishing), not its vertex structure. An F37-level refutation of (MX) would now have to exhibit a one-sided or vertex-free seam, which gates F-F37.3/F-F37.5 make maximally visible.

## **§7. The negative control: the dissipative layer cannot decide**

ZS-M47 O2-a (DERIVED) established that the ZS-A23/A24 mediator — the dimension-weighted GKLS generator q\_i→ j \= Γ\_0 κ² d\_j, one power of d, doubly stochastic, stationary state \= trace — is structurally tracial and structurally unable to decide the clock gate (O2-d) \[1, 5\]. The present construction explains this at the level of topology: a GKLS jump inserts **one** register leg per event — it is the disc-type, single-character object of Lemma L1 — while the clock weight is a **closed two-legged circuit**. The dissipative layer lives at exponent 1; the coherent transport lives at exponent 2; and by ZS-M43 the Z-Spin dynamics is unitary with scrambling, so the physically operative layer for the transported corner is the coherent one \[4\]. **\[DERIVED-BY-INHERITANCE (O2-a); the topological reading is DERIVED-interpretation.\]**

**Firewalled observation (the double-crossing echo).** ZS-M43’s i-tetration cycle X → Z → Y → Z → X crosses the seam **twice** per cycle, and its per-cycle leak is governed by |λ²| ≈ 0.795 — the *square* of the multiplier — for that same reason \[4\]. The two-leg weight (square of the character) and the |λ²| leak (square of the multiplier) thus share a double-crossing origin. This is registered as a structural observation only; no quantitative identification between χ² and |λ|² is asserted, and none is used anywhere in this paper. **\[Registered; NON-identification.\]**

## **§8. (H1), C\_int, and the clock gate**

**§8.1 Corner compatibility (Theorem F37.T3).** ZS-M47.W (DERIVED) reduces the surviving clock condition CRT-4a to weight proportionality via the Connes cocycle calculus \[1\]. The present action contributes the following:

**Theorem F37.T3 (Centrality of the transported weight) \[DERIVED-CONDITIONAL on (H-YM2)\].** *The T1 weight π^(2 leg)(ρ) is a class function of the transport element in each sector, hence lies in the register’s sector center; it therefore commutes with the register action, defines a state compatible with the corner decomposition, and on the E1 branch satisfies the weight-proportionality form of CRT-4a with the size-biased ω — the branch on which ZS-M47 P3 places the injective III₁ parent R∞.* 

This discharges the *structural* half of (H1): the transported weight is corner-compatible by construction. The *dynamical* half — the iteration/modular-step matching — is C\_int, treated next.

**§8.2 C\_int: the reconciliation of record and the OPEN registration.** The M47 handover row transmits “(H1) \+ C\_int … the F31 App. D ratio,” i.e., the matching \-μ/ω\_Z \= θ/ν\_Z with μ \= 0.1148346250 and θ \= 2.2592495540 (checks D3–D4; per-step contraction distinct from α\_BK \= −ln|z\*| \= 0.5664173, check D5) \[1, 3\]. However, ZS-M46 T7b (OPEN-REFORMULATION) records that after the role reversal — the seam realized as a translation, not a dilation — the pre-role-reversal ratio test **is not used**, and the clock gate must be rewritten in terms of the translation generator P\_K, the A24 modular Hamiltonian K\_A, and the central Connes cocycle: Φ(P\_K) \= P\_A, or (Dφ\_K ∘ Φ⁻¹ : Dφ\_A)\_t ∈ 𝕋·1, coinciding with CRT-4a \[2\]. This paper adopts the T7b reformulated gate as the operative form and carries the App. D ratio only as its consistency-form shadow (the locked numbers μ, θ are re-verified here, checks D1–D5). This is a **wording-level reconciliation between two corpus rows; no upstream status is altered** (ZS-M46 T7b and the ZS-M47 handover text are both preserved as written).

**C\_int is not solved in this paper. What is closed here is its reformulation: the obsolete ratio test is retired, and the remaining computation is a finite matrix/cocycle comparison on the explicit ZS-F31 seam diagonalization.** Appendix D specifies that computation completely — the gate equation, the four inputs, and the centrality residual norm ε\_C\_int — so that C\_int is a *closable finite gate*, not a vague OPEN. **C\_int status: OPEN** (Appendix D protocol; gate F-F37.6). The clock gate’s condition budget after this paper: (MX) translated to topology (§5–§6), (H1) structurally discharged (T3) with its dynamical half \= C\_int OPEN, everything riding on the single structural condition (H-YM2), itself decomposed in Appendix C.

## **§9. The finite-ρ consistency deliverable (F-M47.24, consistency form)**

The handover’s third row requires the predicted finite-rapidity Y-character curve to be χ\_2χ\_3 — the tensor reading, exact by fusion multiplicativity χ\_Y \= χ\_Z χ\_X (check A2) — and **not** χ\_6, with the discriminant pre-computed. Executed values (Appendix B):

| Quantity | Value | Check |
| ----- | ----- | ----- |
| ρ\_b \= ½ ln(9/7) | 0.125657 | — |
| π^(2 leg)(ρ\_b), tensor reading | (0.078774, 0.181935, 0.739291) | B4 |
| target (4, 9, 36)/49 | (0.081633, 0.183673, 0.734694) | A3 |
| L1 deviation (tensor reading) | **0.00919466866** (\< 1%) | A5 |
| Δχ \= χ\_2χ\_3 − χ\_6 at ρ\_b | **−0.392090129** | A6 |
| L1 deviation of the one-leg branch vs the two-leg target | 0.3416 | E2 |

The tensor curve reproduces ZS-M47’s quoted band and discriminant to all published digits; the irreducible curve is separated from it by a discriminant thirty times the two-leg band, so any finite-ρ read-out of the corner weight discriminates the readings cleanly. A measured (or independently derived) corner weight following χ\_6 fires F-F37.2 \= F-M47.24.

**External replication targets.** This section is elevated from a consistency check to a *discrimination protocol*: an independent calculator who reproduces the two numbers

Δχ(ρ\_b) \= χ\_2(ρ\_b) χ\_3(ρ\_b) − χ\_6(ρ\_b) \= −0.392090129 , L1( ω^(2)(ρ\_b), ω^(2)(0) ) \= 0.00919466866 \< 1%

from the three inputs d \= (2, 3, 6), χ\_d(ρ) \= sinh(dρ)/sinh ρ, and ρ\_b \= ½ ln(9/7) has independently verified which reading the seam takes; a computation of the corner weight from any alternative seam dynamics that lands on the χ\_6 curve instead falsifies the tensor reading outright. The protocol requires no corpus access. **\[CONSISTENCY-CHECK, executed; replication protocol registered.\]**

## **§10. t\* \= Q: NON-CLAIM re-registration**

ZS-M47 T4-E′ delivers the canonical tunnel (the ZS-M46 T6 depth chain) with **no rung selected**, and hands the depth selector t\* \= **Q** to this paper explicitly as a NON-CLAIM \[1, 2\]. Nothing in the present surface calculus selects a rung: the leg counter is a boundary invariant, blind to tunnel depth, and any numerological association of **Q** \= 11 with a depth index would be exactly the kind of unforced identification the corpus firewalls. **The item is re-registered as a NON-CLAIM, untouched.**

## **§11. Zero-parameter and anti-numerology audit (protocol 3.1)**

**Zero fitted parameters \[PASS\].** Inputs: the locked (**A**, **Q**, dim **Z**) \= (35/437, 11, 2); the register d \= (2, 3, 6); the ZS-M1 germ (z\*, λ\*, μ, θ — re-derived at 50 digits, checks D1–D5); ZS-F30’s bound ½ ln(9/7); the exponent 2 − 2g − b, which is the Euler characteristic of a surface (a theorem, not a dial). Every number in this paper is an exact evaluation on these (49 \= Σd², 49/121 \= Στ², (4, 9, 36)/49, 0.00919, −0.392090). No coupling, damping form, or normalization is chosen anywhere: §3.3’s class universality removes the choice, and the executed substitution scan (check E1) demonstrates it.

**Anti-numerology.** This paper introduces **no new numerical constant**, so a numerical Monte Carlo is inapplicable; the anti-tuning instrument is the executed Lévy-symbol universality scan (E1), which shows the selected law is invariant across the entire admissible action class. Three declinations are recorded: (i) 49 is the register’s global index Σd² and is **not** claimed to be the order of any group (the Plancherel analogy of Remark 1 is structural, not arithmetic); (ii) the double-crossing echo with |λ²| (§7) is firewalled as a non-identification; (iii) no rung of the depth tunnel is associated with **Q** (§10).

## **§12. Cross-version safety (protocol 3.2)**

Consumed verbatim, no status reversed: ZS-M47 O2-a/b/f/g, M47.W, M47.U, M47.YM (YL1–YL5), T4-E/E′, the (MX)/(H1) registry and the §12.3 handover \[1\]; ZS-M46 KH1–KH4 context and T7b \[2\]; ZS-F30’s rapidity bound and seam antisymmetry, ZS-F31 R2a and App. D (z\*, λ\*, μ, θ re-verified to locked digits) \[3\]; ZS-M43’s unitary-scrambling verdict and the |λ²| leak \[4\]; ZS-A23/A24’s mediator structure \[5\]; ZS-F33/F34/F36’s Σ₂ internal cycle as the (H-YM2) promotion target \[6\]. The single reconciliation of record is §8.2 (M47 handover wording vs. M46 T7b), resolved at wording level with both sources preserved. Downstream: ZS-A32 receives T1’s weight on the E1 branch unchanged; the (H-2D)/P2/(★\_w)/(TT) items remain with ZS-A32 per the handover, untouched here. z\* digits match ZS-M1/ZS-F31 App. D at every use.

**Observational non-collision (protocol 3.3) \[PASS\].** No dimensionful prediction is made; Planck 2018 ΛCDM values and Standard-Model couplings are untouched; the Buckingham-π no-go on absolute scales (ZS-F36.T7 / ZS-A27 / ZS-A28) is inviolate — the paper’s outputs are dimensionless register weights and exact character identities.

## **§13. Falsification gates and non-claims (protocol 3.5)**

**Tier 1 — mathematical / immediate rejection.** **F-F37.1:** if the exact character identities fail — fusion multiplicativity χ\_2χ\_3 \= χ\_4 \+ χ\_2, Peter–Weyl orthogonality on (2, 3, 6), the Migdal gluing identity, the ρ → 0 limit (4, 9, 36)/49 — the paper is void (checks A1–A4, B1–B2 recompute in seconds). **F-F37.2 (= F-M47.24):** a finite-ρ corner weight following χ\_6 rather than χ\_2χ\_3 (discriminant −0.392090 at ρ\_b) refutes the tensor reading and, with it, T2. **F-F37.5:** exhibition of a non-diagonal seam propagation (different register labels on the two legs surviving the gauge average) refutes Lemma L2 and the coincidence identity.

**Tier 2 — structural / conditional.** **F-F37.3:** if the physical seam is shown to be one-sided at action level (b \= 1), the topological lock P1(a) fails together with ZS-M47 (III) — this is the action-level image of F-M47.6’s “an F37 refutation of (MX) reopens the Y-leg.” **F-F37.4 (= F-M47.14 adjacent):** exhibition of a β-odd gauge-invariant register weight collapses the parity lock P1(b). **F-F37.6:** the T7b-form C\_int computation (Φ(P\_K) \= P\_A on the explicit ZS-F31 seam diagonalization) returning incompatibility fails (H1)’s dynamical half and reopens the clock gate (fires F-M47.6). **F-F37.8:** failure of (H-YM2) itself — a demonstration that the seam channel is not gauge-invariant or not gluing-consistent — voids T1/T2/T3 and Theorem A’s applicability simultaneously; maximally informative. After Appendix C this gate localizes to its residual: a refutation of (H-Σ2) (the physical channel is *not* the Σ₂-restricted gauge sector of the seam connection) is what would now fire it.

**Tier 3 — scope / promotion.** **F-F37.7 (promotion gate; PARTIALLY EXECUTED in v1.1):** Appendix C closes the heat-kernel-class half of (H-YM2) on the Σ₂ restriction (gauge invariance \+ gluing consistency, machine-checked); the remaining promotion — (H-Σ2), tied to ZS-F31’s R2b (A\_Z ∼ A\_K) plus the Σ₂ localization — promotes T1/T2 → DERIVED when closed (a promotion gate, not a refutation).

**Non-Claims.** **NC-F37.1:** no rung of the depth tunnel is selected; t\* \= **Q** remains a NON-CLAIM (§10). **NC-F37.2:** the seam 2-cycle is *not* claimed to be a closed sphere; the transported corner is the cut-conditioned cylinder, and the Koenigs-torus statement χ(T²) \= 0 of ZS-F36 is untouched (an integrated — rather than conditioned — boundary would give the democratic torus weight, a different object). **NC-F37.3:** the |λ²| double-crossing echo is a registered observation, not an identification (§7). **NC-F37.4:** no absolute scale, no dimensionful quantity, no cosmological identification. **NC-F37.5:** the Plancherel / topological-charge analogies of Remark 1 are placements in a proven mathematical family, not claims that the Z-Spin register is an anyon system or that 49 is a group order.

## **§14. Claim ledger**

| \# | Claim | Status | Confidence | Conditions |
| ----- | ----- | ----- | ----- | ----- |
| L1 | Leg-Counting Lemma (dimension exponent \= 2 − 2g − b) | IMPORTED-PROVEN | — | compact structure group |
| L2 | Coincidence conditioning \= Peter–Weyl / Migdal gluing | DERIVED | 90% | (H-YM2) family |
| A | Two-Leg Plancherel Selection (general abs(χ\_R(U))² form; externally standard consequence, internally new application)  | DERIVED | 90% | Markovian class; two-sided cut; same conjugacy class |
| T1 | Two-Leg Selection: π\_i \= χ\_i(ρ)²/Σ\_j χ\_j(ρ)², ρ → 0: d\_i²/49 | DERIVED-CONDITIONAL | 90% | (H-YM2) \= class half (DERIVED, App. C) \+ (H-Σ2); legs on the F30/F31 connection |
| P1(a) | One-leg exclusion, topological lock | DERIVED-CONDITIONAL | 90% | (MX) as two-sidedness |
| P1(b) | One-leg exclusion, parity lock | DERIVED | 90% | none beyond O2-g inputs |
| T2 | Mediation vertex from the action; YL1–YL5 reproduced; F-M47.27 executed | DERIVED-CONDITIONAL | 90% | (H-YM2) |
| §7 | Dissipative layer \= one-insertion (disc-type) object, cannot decide | DERIVED-BY-INHERITANCE \+ interpretation | 60% | O2-a verbatim |
| §7 | abs(λ)² double-crossing echo | Registered observation | 30% (as future identification) | firewalled |
| T3 | Corner compatibility (structural half of (H1)) | DERIVED-CONDITIONAL | 90% | (H-YM2); E1 branch |
| §8.2 | C\_int (T7b reformulated finite computation) | OPEN | — | ZS-F31 seam diagonalization |
| §3.3 | Class universality of the selection | IMPORTED-PROVEN \+ scan | 90% | Markovian class |
| App. C | (H-YM2) class half: gauge invariance \+ gluing on the Σ₂ restriction | DERIVED | 90% | Σ₂ restriction of the seam gauge sector |
| (H-Σ2) | Physical channel \= Σ₂-restricted seam gauge sector | HYPOTHESIS-strong | 60% | tied to ZS-F31 R2b (A\_Z ∼ A\_K) \+ Σ₂ localization; F-F37.7 residual |
| App. C | Route (b) — direct abelian 3-form induction of the register sector | CLOSED-NEGATIVE (this route) | 90% | recorded dead-end; disciplines (H-Σ2) |
| §10 | t\* \= **Q** | NON-CLAIM | — | — |

## 

## **§15. Conclusion**

The mandate is discharged at the promised level. The seam transport, formalized as a gauge-invariant, gluing-consistent holonomy field on the dim(**Z**) \= 2 stage, selects the two-leg law because *the exponent of the register dimension is a topological leg counter and the seam has two legs*: the transported corner is the cut-conditioned cylinder whose two boundary holonomies are the proven ZS-F31 transport element, its amplitude is the squared character χ\_i(ρ)² with the O2-b coincidence exposed as Peter–Weyl orthogonality, and the ρ → 0 weight is exactly the size-biased ω \= (4, 9, 36)/49 on which ZS-M47’s clock survives and the R∞ parent branch stands. The one-leg alternative is excluded twice — as the amplitude of an axiom-violating one-sided topology and as a β-odd candidate annihilated by gauge invariance — and the mediation vertex, far from being postulated, is the three-boundary amplitude of the same action, reproducing the complete YL arithmetic including the pre-computed discriminant Δχ \= −0.392090. The selection is class-universal: nothing was tunable, so nothing was tuned.

The state of the paper in four lines:

**Closed:** the d²/49 vs d/11 branch selection, conditional on (H-YM2) — whose heat-kernel-class half is itself closed in Appendix C.

**Closed:** the χ\_2χ\_3 tensor-Y vertex survives; the χ\_6 irreducible-Y vertex dies — with exact multiplicities (2, 2, 2\) and the replication targets Δχ \= −0.392090129, L1 \= 0.00919466866.

**Open:** the (H-Σ2) residual of the parent-action derivation (tied to ZS-F31 R2b), and C\_int^(T7b) (Appendix D finite protocol).

**Non-claim:** t\* \= **Q**; any absolute scale; any anyon / group-order identification of 49\.

The paper’s honest budget is therefore short and *shorter than v1.0’s*: the v1.0 condition (H-YM2) has been decomposed, its class half DERIVED, and its residual (H-Σ2) tied to a pre-existing corpus gate rather than left as a free-standing hypothesis. One finite computation, C\_int in its ZS-M46 T7b form, remains OPEN with a complete closing protocol. One item, t\* \= **Q**, remains a NON-CLAIM by design. **Closure condition.** Therefore F37 should be closed as a DERIVED-CONDITIONAL action-level selection paper unless one wants to execute C\_int itself; that execution is better scoped to ZS-F38 or to a short v1.x computational addendum executing Appendix D. Per the v1.2 external review’s terminal verdict, no further theory-level modification is made inside this paper: (H-Σ2) and C\_int are fixed as the pre-registered ZS-F38 gates (Appendix C.5, Appendix D), and **this v1.3 is the terminal version of ZS-F37**. The through-line extends ZS-M47’s by one clause: the Z-sector supplies the stage; the Z-Spin supplies every action on it; **and the stage’s own two-dimensionality is what counts the legs** — the seam weighs the register by the square because a two-sided interface is crossed twice. (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED.

## **§16. Acknowledgements & Code Availability**

This paper consolidates three internal Z-Spin Collaboration deep-exploration sessions (July 2026): the v1.0 session executing the ZS-M47 §12.3 handover, the v1.1 session integrating the first external review (verification hardening; the (H-YM2)-promotion opportunity), and the v1.2 session integrating the second external review (notation robustness; verifier executability; epistemic sharpening) — all recorded in Appendix A. Both reviews are gratefully acknowledged. AI tools (Anthropic Claude) were used for corpus and external-literature search, cross-paper integration, symbolic/numerical verification, and drafting, under Kenny Kang’s editorial direction; the author assumes full responsibility for all content. The verification script zs\_f37\_verify\_v1\_3.py (checks identical to v1.2 — the v1.3 edits are text-only) reproduces all 27 checks in its default fast mode (deterministic algebra \+ 1D quadrature; measured \< 1 s internally; externally reproduced at 27/27 PASS, 2.0 s, in the v1.2 review of record) and the two full-quadrature witnesses B2F/B2bF under the flag (NumPy \+ mpmath 50-digit Newton); the superseded v1.2/v1.1/v1.0 scripts are retained for the record. To reproduce:

python zs\_f37\_verify\_v1\_3.py  
and, for the optional full-quadrature witnesses, set in the script header:

RUN\_FULL\_SURFACE\_QUADRATURE \= True

## **Appendix A. Deep-exploration (if-tree) record, v1.0**

**Step 0 (long list, 7).** (1) 2D heat-kernel gauge action on the seam with Euler-characteristic leg counting; (2) subfactor route — Γ \= J\_N J\_M as two modular conjugations, Longo index d²; (3) Peter–Weyl/Plancherel route — coincidence as character orthogonality; (4) Born-rule/modular route — one leg \= amplitude, two legs \= amplitude × conjugate, β-parity selection; (5) dissipative (GKLS) route as negative control; (6) (MX) vertex as the pair-of-pants amplitude; (7) (H1)+C\_int in the ZS-M46 T7b reformulated form. **Dropped:** the t\* \= **Q** depth selector (an eighth candidate) — handed over as a NON-CLAIM and carrying the corpus’s highest numerology risk; re-registered only.

**Step 1 (MECE issue list, 4, by impact).** **I1** \= the action-level two-leg selection theorem {1 \+ 2 \+ 3 \+ 4 merged: the four routes are one theorem seen from surface topology, operator algebra, harmonic analysis, and parity}; **I2** \= the vertex from the same action {6}; **I3** \= the negative control {5}; **I4** \= the reformulated clock gate {7}. **Dropped from the list:** none beyond the Step-0 drop; the merge of (1)–(4) into I1 is the decomposition’s main act.

**Step 2 (if-tree, dependency order).** I1 → I2 (consumes the same surface calculus) → I3 (the contrapositive of I1) → I4 (consumes I1’s weight).

**Step 3 (exploration, statuses).** I1a cylinder kernel \[IMPORTED-PROVEN\]; I1b U\_K boost character \= O2-f weight \[PROVEN, both sides\]; I1c two legs from (MX) two-sidedness \+ the squared half-transport \[DERIVED-CONDITIONAL, (H-YM2) registered\]; I1c′ Lévy class universality \[IMPORTED-PROVEN\]; I1d coincidence \= orthogonality \[DERIVED\]; I1e ρ → 0 arithmetic \[PROVEN\]; I1f one-leg exclusion \[DERIVED (parity) / DERIVED-CONDITIONAL (topology)\]; I2 vertex integrals reproduce YL1–YL5 \[DERIVED-CONDITIONAL\]; I3 disc/circuit dichotomy \[inherited DERIVED \+ interpretation\]; I4 T3 centrality \[DERIVED-CONDITIONAL\], C\_int \[OPEN\].

**Step 4 (convergence).** Cycle 1: two nodes changed state — the finite-ρ L1 was first computed on the χ₆ curve (0.0552) and corrected to the tensor curve (0.00919, matching ZS-M47 and thereby *validating in practice* the handover’s “χ₂χ₃, not χ₆” clause); C\_int was updated from “OPEN ratio computation” to “OPEN in T7b reformulated form.” Cycle 2: zero nodes changed. **Converged** (2 → 0).

**Step 5 (scoring).** Converged \+ no corpus collision \+ no new numerical constant (numerical MC inapplicable; the executed E1 universality scan is the anti-tuning instrument) → the two-leg selection registers at DERIVED-CONDITIONAL on the single condition (H-YM2), itself HYPOTHESIS-strong with a documented promotion path. Exploration value: the transport-level ZS-M47 (III) result is lowered to action level on three imported-proven pillars, with the condition registry *shortened* — (MX)+(H1) traded for (H-YM2) \+ one OPEN finite computation.

**Self-referential audit.** The “import an exactly solved external framework onto the seam” move resembles prior corpus patterns (ZS-M43’s Anosov/Selberg model; ZS-F30’s Cartan realization), and that familiarity is itself a bias risk for (H-YM2). The two defenses adopted: conditioning on the *class* (Lévy universality) rather than a model, and keeping the losing branch alive in the text (§5, §7) with explicit exclusion arguments rather than silence. The confirmation-bias risk of knowing ZS-M47’s answer in advance is mitigated by the pre-computed both-branch structure inherited from M47.U: both laws were evaluated at every step (checks A3/A7, E2), and the discriminants (Δχ, the L1 pair) are published numbers that either reading could have failed.

### **A.2 The v1.1 deep-exploration record (review integration)**

**Step 0 (long list, 7).** (1) Appendix C route (a): the seam gauge sector \= the F30/F31 su(2) connection restricted to Σ₂, heat-kernel regularization, Migdal gluing invariance, Lévy measure — decompose (H-YM2); (2) route (b): induce the register gauge sector directly from the ZS-F36 abelian 3-form S\_6; (3) extract the Z-Spin-free general theorem (external-reader packaging); (4) verification hardening (B2 quadrature, new Markov check, B4 split, C3 exact multiplicities, D1 ten digits, E2 comment); (5) the finite C\_int computation protocol as an appendix; (6) the surface-topology table \+ replication-target elevation; (7) full C\_int closure inside F37. **Dropped:** (7) — per the external review’s own recommendation, closing C\_int in-paper would blur the paper’s two delivered results; the protocol (5) is the correct scope. (2) is not dropped silently but *executed to its dead-end* and recorded (Appendix C, route (b), CLOSED-NEGATIVE for this route).

**Step 1 (MECE issue list, 4, by impact).** **I1** \= the (H-YM2) promotion attempt {1, with 2’s dead-end as input}; **I2** \= verification hardening {4}; **I3** \= external-reader packaging {3 \+ 6}; **I4** \= the C\_int protocol {5}. **Dropped from the list:** none beyond the Step-0 drop.

**Step 2 (if-tree).** I1 → I2 (the new B2b check is I1’s machine witness) → I3 → I4.

**Step 3 (exploration, statuses).** I1: gauge invariance on Σ₂ \[DERIVED\]; gluing \= heat-kernel/cylinder convolution \[IMPORTED-PROVEN \+ new deterministic check B2b\]; the class is *forced* by gluing (Lévy classification) \[IMPORTED-PROVEN\]; the residual identification (H-Σ2) \[HYPOTHESIS-strong, tied to ZS-F31 R2b — *condition reuse*, no new registry entry\]; route (b) \[CLOSED-NEGATIVE: an abelian 3-form cannot induce the nonabelian su(2)-graded register holonomies by itself\]. I2: all six hardening items \[executed; one genuine catch — the wrong kernel fails gluing, §3.2 warning\]. I3: Theorem F37.A \[DERIVED\]; table and replication targets \[presentation\]. I4: protocol \[OPEN, fully specified\].

**Step 4 (convergence).** Cycle 1: three nodes changed — B2b’s kernel corrected from the single-argument class function to the two-boundary cylinder (the machine-caught trap); (H-YM2) re-expressed as class-half \+ (H-Σ2); route (b) moved from candidate to recorded dead-end. Cycle 2: zero nodes changed. **Converged (3 → 0).**

**Step 5 (scoring).** Converged \+ no corpus collision \+ no new numerical constant (MC inapplicable; the E1 scan and the new B2b fail-closed check are the anti-tuning instruments) → the v1.1 registry is strictly shorter than v1.0’s: (H-YM2) → class half DERIVED \+ (H-Σ2) ⊆ {R2b, Σ₂ localization}, both pre-existing corpus items. Exploration value: high — every review item is closed or protocolized, and the one attempted promotion (I1) succeeded at the decomposition level while honestly failing at full closure, with the failure surface (route (b)) recorded rather than hidden.

### **A.3 The v1.2 deep-exploration record (second review integration)**

**Step 0 (long list, 7).** (1) Notation overhaul: OMML/LaTeX math → corpus-house-style Unicode plaintext (extraction-robust; diagnosed from the reviewer’s breakage pattern — ρ dropped, ½ → “12”, χ stripped — which is characteristic of OMML extraction, while plain-text Unicode such as “H-Σ2” survived the same pipeline); (2) fast/full verifier split, with a fast B2 via exact analytic (α, γ) Fourier reduction and a fast B2b via 1D Weyl character orthogonality; (3) |χ\_R(U)|² generalization of Theorem A with the A9 reduction check; (4) epistemic sharpening — the “compression, not closure” framing and the explicit class-vs-physical-identification separation sentence; (5) the route-(b) one-line summary box; (6) the closure-condition sentence scoping C\_int execution to ZS-F38; (7) executing C\_int itself in a computational addendum. **Dropped:** (7) — per the review’s own §2.3/§2.6 recommendation and the v1.1 Step-0 precedent: out of this paper’s scope, cleanly scoped to ZS-F38.

**Step 1 (MECE issue list, 4, by impact).** **I1** \= presentation robustness {1 \+ the Appendix-D formula recovery — the single largest external-quality item}; **I2** \= verifier executability {2, fast \< 30 s}; **I3** \= epistemic sharpening {4 \+ 5 \+ 6}; **I4** \= general-theorem safety {3}. **Dropped from the list:** none beyond the Step-0 drop.

**Step 2 (if-tree).** I1 → I2 (the fast verifier is what an external reader runs first) → I4 → I3.

**Step 3 (exploration, statuses).** I1: the Unicode-plaintext conversion \[executed; presentation — and it is the corpus house style, so the change is a *return* to convention, not an invention\]; I2: fast B2 Fourier reduction \[DERIVED — the γ-average over the 4π period is an exact Kronecker delta on half-integer frequencies, and parity mismatch kills cross terms exactly, leaving only a 1D β-integral\]; fast B2b via class-function orthogonality \[DERIVED, deviation 4.4 × 10⁻¹⁵\]; full-mode witnesses retained and re-run \[PASS\]; I4: |χ|² general form \[DERIVED — standard\]; A9 reduction \[machine-checked\]; I3: framing sentences \[presentation/epistemic\].

**Step 4 (convergence).** Cycle 1: two nodes changed — the fast-B2 method was selected (Fourier reduction over a cached-grid alternative: exact rather than approximate), and the notation target was fixed to corpus-house Unicode after diagnosing the reviewer’s extraction pattern. Cycle 2: zero nodes changed. **Converged (2 → 0).**

**Step 5 (scoring).** Converged \+ no corpus collision \+ no new numerical constant (one new check A9 verifies a reduction, not a new number) → v1.2 changes are presentation, executability, and epistemic sharpening only; no theorem statement, status, or numerical value of v1.1 is altered. Exploration value: the paper’s *external reproducibility* rises from “logically hardened but heavy” to “one-command, sub-second verification,” and the notation is now robust to the very extraction pipeline that twice degraded the review copy.

### **A.4 The v1.3 deep-exploration record (terminal editorial closure)**

**Step 0 (long list, 7).** (1) Table-safety sweep — escape the vertical bars of |χ\_R(U)|² and |λ²| inside claim-ledger cells (the pipes were being parsed as column delimiters, breaking the ledger’s two rows and truncating the Theorem A row to fewer than five columns); (2) markdown-emphasis safety sweep — audit the whole underscore-after-punctuation class ()\_t, |\_{ …), not just the two Version-History instances the review caught, and de-italicize the two flagged prose emphases; (3) front-load the novelty sentence and add the README-style reproduction lines with the external-reproduction datum (27/27 PASS, 2.0 s, v1.2 review of record); (4) pre-register the ZS-F38 gate with its drift-proof proof target (A\_Z ∼ A\_K restricted to Σ₂; the holonomy-conjugacy form); (5) terminal-version declaration and version-history discipline; (6) execute Appendix D (the ε\_C\_int computation) inside F37; (7) further compress Appendix C. **Dropped:** (6) and (7) — both per the review’s own final verdict (“더 이상 같은 논문 안에서 C\_int나 H-Σ2를 닫으려는 반복 수정은 권하지 않습니다”): the paper’s identity is the action-level selection, and both items are scoped to ZS-F38.

**Step 1 (MECE issue list, 3, by impact).** **I1** \= rendering-safety sweeps {1 \+ 2 — the only remaining publication blockers}; **I2** \= external-value front-loading {3}; **I3** \= forward-scope fixation {4 \+ 5}. **Dropped from the list:** none beyond the Step-0 drops.

**Step 2 (if-tree).** I1 → I2 → I3.

**Step 3 (exploration, statuses).** I1 \[executed; presentation\]: the class sweep additionally surfaced one *content* item the review did not catch — the v1.2 batch edit that was to insert the route-(b) summary box into Appendix C.4 had **silently failed** (an unasserted string replacement missed on a G₆/G\_6 mismatch), so the box existed in the v1.2 Version History but not in the v1.2 body; v1.3 applies it and records the correction of record inside C.4. All v1.3 replacements are assert-guarded. I2 \[executed; presentation\]. I3 \[executed; NON-CLAIM discipline maintained — the F38 pre-registration adds a target, not a claim\].

**Step 4 (convergence).** Cycle 1: three nodes changed — the two review-flagged rendering classes, plus the self-found C.4 silent-failure repair. Cycle 2: zero nodes changed. **Converged (3 → 0).**

**Step 5 (scoring).** Converged \+ no corpus collision \+ no new number, theorem, or status (the C.4 repair restores already-recorded v1.2 content; every other edit is presentation or pre-registration) → v1.3 is the terminal editorial release. Exploration value: modest by design — its one genuine find is the silent-edit failure, and the methodological lesson is recorded for the corpus: **batch text edits in a release pipeline must be assert-guarded, or the version history can outrun the body.**

## **Appendix B. Verification ledger (27/27 PASS; fast/full architecture)**

**Script architecture (v1.2, per external review).** One script, two modes:

| Script / mode | Purpose | Runtime |
| ----- | ----- | ----- |
| zs\_f37\_verify\_v1\_3.py (default, fast; checks identical to v1.2) | all 27 checks; deterministic algebra \+ 1D Gauss/Weyl quadrature; B2 via exact analytic (α, γ) Fourier reduction | measured \< 1 s internal; 2.0 s external (v1.2 review of record) |
| same script, RUN\_FULL\_SURFACE\_QUADRATURE \= True | adds B2F/B2bF: the 3D Euler-angle grid witnesses of v1.1 | minutes |

The fast mode is the canonical verifier; the full-quadrature witnesses are retained so that no v1.1 check is silently weakened. Reproduction is one command — python zs\_f37\_verify\_v1\_3.py — with the full witnesses enabled by RUN\_FULL\_SURFACE\_QUADRATURE \= True in the script header; the fast mode has been externally reproduced (27/27 PASS, 2.0 s; v1.2 review of record). NumPy \+ mpmath (50-digit Newton); seed 437 is used only for the fixed generic test matrices A, B, U, V — every *judgment* is deterministic. Five blocks; ● marks v1.1 hardenings, ◆ marks v1.2 changes.

**A — character / two-leg core (9).** A1 χ\_d(ρ) \= sinh(dρ)/sinh ρ \= boost trace in the spin-(d−1)/2 representation (d \= 2, 3, 4, 6). A2 fusion multiplicativity χ\_2χ\_3 \= χ\_4 \+ χ\_2 exact, and ≠ χ\_6. A3 ρ → 0 two-leg \= (4, 9, 36)/49 exact (Fractions). A4 Στ² \= 49/121 exact. A5 L1 at ρ\_b (tensor reading) \= 0.00919466866 \< 1%. A6 Δχ(ρ\_b) \= −0.392090129. A7 one-leg branch (2, 3, 6)/11 pre-computed. A8 β-evenness χ\_d(−ρ) \= χ\_d(ρ). ◆ A9 (NEW) su(2) register self-duality: χ\_R(U) real, hence |χ\_R(U)|² \= χ\_R(U)² — the reduction that specializes Theorem A’s general |χ|² form to the register.

**B — surface calculus (7).** B1 Peter–Weyl orthogonality on (2, 3, 6\) via Weyl integration (Gauss–Legendre, 400 nodes, \< 10⁻¹⁰). ●◆ B2 Migdal gluing ∫dU χ\_R(AU)χ\_S(U†B) \= δ\_RS χ\_R(AB)/d\_R — fast mode: **exact analytic (α, γ) Fourier reduction** (the γ-average over \[0, 4π) is an exact Kronecker delta; parity mismatch kills R ≠ S cross terms exactly) \+ 1D Gauss β-quadrature, deviation \< 10⁻⁹; full mode adds the 3D-grid witness B2F. ●◆ B2b cylinder Markov/gluing ∫dV Z\_{t₁}(A, V) Z\_{t₂}(V, B) \= Z\_{t₁+t₂}(A, B) — fast mode via 1D Weyl character orthogonality (class functions), deviation 4.4 × 10⁻¹⁵; **a finite truncated witness (j ≤ 3/2) of the imported-proven per-representation identity**; full mode adds B2bF; the check fails on the single-argument kernel (§3.2 warning), the intended fail-closed behavior. B3 leg counting d², d¹, d⁰ for (g, b) \= (0, 0), (0, 1), (0, 2). ● B4a cut-conditioned cylinder, **tensor** reading: normalization to 10⁻¹⁴, componentwise 10⁻¹², L1 cross-consistent with A5. ● B4b the **irreducible χ\_6 control** cylinder, clearly separated: normalized 10⁻¹², L1 \= 0.05524 \> 0.00919 exhibited as the control. B5 class-function invariance χ(VUV†) \= χ(U) (\< 10⁻⁹).

**C — mediation vertex (4).** C1 ½ ⊗ 1 \= ½ ⊕ 3/2; Casimir {3/4, 15/4}; 35/4 excluded. C2 all three vertices vanish under the irreducible spin-5/2 reading. ● C3 tensor reading: **exact multiplicities (a₁, a₂, a₃) \= (2, 2, 2\)** — consistent with C4’s inner product. C4 pair-of-pants integrals: ⟨χ\_2χ\_3, χ\_2χ\_3⟩ \= 2, ⟨χ\_2χ\_3, χ\_6⟩ \= 0 (\< 10⁻⁸).

**D — Koenigs / clock-gate data (5).** ● D1 z\* \= **0.4382829367 \+ 0.3605924719i** at ten locked digits (50-digit Newton; |f(z\*) − z\*| \< 10⁻⁴⁰). D2 |λ\*| \= 0.89151. D3 μ \= 0.1148346250. D4 θ \= 2.2592495540. D5 μ ≠ α\_BK \= 0.5664173303 (distinctness of the per-step contraction from the Berry–Keating rapidity).

**E — universality / anti-tuning (2).** E1 t → 0 two-leg ratio invariant under damping-symbol substitution (Casimir, linear, quadratic, random positive; \< 10⁻⁴). ● E2 discrimination at ρ\_b: L1(one-leg vs two-leg target) \= **0.3416** ≫ 0.00919.

## **Appendix C. The (H-YM2) promotion attempt: decomposition on the ZS-F36 Σ₂ restriction**

**C.1 Mandate.** v1.0 registered (H-YM2) — *the physical Z-Spin seam transport channel is a two-dimensional gauge-invariant Markovian holonomy field* — with a promotion path via the ZS-F36 parent action. This appendix executes the attempt. The outcome is a **decomposition, not a full closure**: the *class* half of (H-YM2) is derived on the Σ₂ restriction, and the residual is isolated as a strictly smaller identification statement tied to a pre-existing corpus gate.

**C.2 Route (a): the seam gauge sector on Σ₂ \[executed\].** ZS-F33/F34/F36 place the seam’s internal geometry on the rank-2 cycle of Y₆ \= M₄ × Σ₂ \[6\], and ZS-F30/F31 supply the seam connection: the sl(2, ℂ)-valued pure-gauge Cartan boost A\_K \= g\_K⁻¹ dg\_K with fixed axis, whose compact real form carries the register’s su(2) grading (ZS-M47.HR: X \= spin-1, Z \= spin-½, Y ≅ Z⊗X \[1\]). Restrict the connection to the 2-cycle, A\_Σ \= A|\_Σ₂, and take the minimal gauge-invariant action on the stage,

S\_{Σ₂} \= (1/2g\_Z²) ∫\_{Σ₂} Tr( F\_Σ ∧ \*\_Σ F\_Σ ) (or its topological/BF limit g\_Z² → ∞).

Three facts, each imported-proven, now close the two defining properties of (H-YM2) on this restriction:

**(C-i) Gauge invariance \[DERIVED\].** S\_Σ₂ and every boundary-holonomy amplitude built from it are invariant under seam gauge transformations by construction; the transported corner weight is a class function of each boundary holonomy (check B5).

**(C-ii) Gluing / Markov consistency \[DERIVED; machine-checked\].** The lattice heat-kernel regularization of S\_Σ₂ assigns the plaquette weight Σ\_R d\_R χ\_R(V) e^(−tC₂(R)/2), and Migdal’s defining property — integrating a shared link exactly reproduces the same weight on the merged plaquette — makes the regularization *self-similar under composition*: this is the Markov property, and it survives the continuum limit as the Driver–Sengupta–Lévy measure with boundary-holonomy conditioning \[7–11\]. On the paper’s own object it reads

∫ dV Z\_{t₁}(A, V) Z\_{t₂}(V, B) \= Z\_{t₁+t₂}(A, B) , Z\_t(U, V) \= Σ\_R χ\_R(U) χ\_R(V†) e^(−t C₂(R)) ,

verified deterministically to 10⁻⁹ (check B2b; a finite truncated witness of the imported-proven per-representation identity). The bookkeeping subtlety of §3.2 — the single-argument kernel does *not* glue — was caught by the machine, confirming that the gluing-consistent two-boundary cylinder is the unique correct propagating object.

**(C-iii) The class is forced, not chosen \[IMPORTED-PROVEN\].** By Lévy’s classification, *any* two-dimensional gauge-invariant field satisfying (C-i)–(C-ii) is a Markovian holonomy field parametrized by a Lévy process on the group \[11\]; the heat-kernel action is merely the Brownian representative, and the selection theorem is class-universal (§3.3, check E1). Hence no additional assumption about the *form* of the seam action was ever needed: gluing consistency alone puts the channel in the class where Theorems A/T1 operate.

**C.3 The residual (H-Σ2) \[isolated\].** What (C-i)–(C-iii) do **not** prove is that the *physical* transport channel — the one whose corner ZS-M47 (III) weighs — is this Σ₂-restricted gauge sector rather than something else. This residual identification is named

**(H-Σ2):** *the physical Z-Spin seam transport channel is the gauge sector of the physical seam connection A\_Z restricted to the corpus-forced 2-cycle Σ₂.*

Crucially, (H-Σ2) is not a new free-standing hypothesis: it is contained in already-registered corpus items. Its connection half is exactly ZS-F31’s OPEN gate **R2b** (A\_Z ∼ A\_K: the physical connection is gauge-equivalent to the F30 Cartan connection \[3\]), and its localization half is the ZS-F36 placement of the seam’s internal cycle (with its own inherited caveats \[6\]). Closing R2b \+ the Σ₂ localization closes (H-Σ2), and with it (H-YM2) entirely — promoting T1/T2 to DERIVED (gate F-F37.7). **Status: (H-Σ2) HYPOTHESIS-strong; the v1.1 condition registry is strictly shorter than v1.0’s.**

**Forward scope (pre-registered; not executed here).** The closure of (H-Σ2) is fixed as the next-paper gate, with the suggested scoping *ZS-F38 — The Physical Seam Identification Gate: Closing (H-Σ2) via the A\_Z ∼ A\_K Connection Equivalence*. Its proof target, stated now so that F38 cannot drift: A\_Z restricted to Σ₂ is gauge-equivalent to A\_K restricted to Σ₂ — equivalently, Hol\_{A\_Z}(γ) \= g⁻¹ Hol\_{A\_K}(γ) g for the physical seam loops γ ⊂ Σ₂. Executing Appendix D (the ε\_C\_int computation) may ride in the same paper or in a short v1.x addendum. Nothing in F37 depends on the outcome; a negative F38 verdict fires F-F37.8 exactly as registered.

**C.4 Route (b): the direct 3-form induction \[CLOSED-NEGATIVE for this route\].** The alternative derivation was attempted and terminated. Summary box:

**G₆ alone cannot generate the nonabelian su(2)-graded character sector; A\_Z restricted to Σ₂ must enter.**

An abelian 3-form field strength cannot by itself supply the nonabelian su(2)-graded holonomies that the register characters require; the nonabelian structure enters through the F30 connection, not through G₆. The dead-end is recorded (not silently dropped) because it disciplines (H-Σ2): the seam gauge sector must come from the connection side of the corpus (F30/F31/R2b), and any future closure attempt routed purely through the 3-form is pre-registered as unpromising. *(Correction of record: this summary box was described in the v1.2 Version History but a silent edit failure left it out of the v1.2 body; v1.3 applies it. No content of C.4 changes.)*

**C.5 Net effect on Theorem T1.** After this appendix the theorem’s honest label may be read two equivalent ways: *T1 \= DERIVED-CONDITIONAL on (H-Σ2)* (the strictly smaller residual), or *T1 \= DERIVED under the F36 Σ₂ restriction* (taking the restriction as the working frame). Both readings are recorded in the claim ledger; the abstract and §4 carry the first, conservative one.

## **Appendix D. The finite C\_int computation protocol (T7b form)**

C\_int is not solved in this paper; this appendix makes it a *closable finite gate* by specifying the computation completely, per ZS-M46 T7b \[2\].

**D.1 Gate equation.** The reformulated clock-gate condition is

C\_int^T7b : Φ(P\_K) \= P\_A or ( Dφ\_K ∘ Φ⁻¹ : Dφ\_A )\_t ∈ 𝕋·1 ,

i.e., the intertwiner carries the seam translation generator to the mediator modular Hamiltonian, equivalently the relative Connes cocycle between the transported and mediator states is a central phase — coinciding with CRT-4a \[1, 2\]. The obsolete pre-role-reversal ratio \-μ/ω\_Z \= θ/ν\_Z is retired (§8.2); the locked Koenigs numbers μ \= 0.1148346250, θ \= 2.2592495540 (checks D3–D4) enter only as consistency shadows.

**D.2 Inputs (four, all corpus-explicit).** (1) The ZS-F31 seam diagonalization matrix — the explicit spectral data of the seam GKLS/transport generator \[3\]; (2) the translation generator P\_K of the seam suspension (ZS-M46 role-reversal frame \[2\]); (3) the ZS-A24 modular Hamiltonian K\_A of the mediator corner \[5\]; (4) the candidate intertwiner Φ (the corner embedding fixed by Theorem T3’s central weight).

**D.3 Residual norm and verdict.** Compute the centrality residual

ε\_C\_int \= ‖ Φ(P\_K) − P\_A ‖ / ‖ P\_A ‖ (equivalently, for a conjugation intertwiner: ‖ Φ P\_K Φ⁻¹ − P\_A ‖ / ‖ P\_A ‖).

Verdict: ε\_C\_int \= 0 (to working precision) closes C\_int and discharges (H1) entirely; ε\_C\_int ≠ 0 fires F-F37.6 (= F-M47.6) and reopens the clock gate. The computation is finite (matrix/cocycle comparison on the explicit F31 data), well-posed, and requires no input beyond (1)–(4). **Status: OPEN, protocolized; scoped to ZS-F38 or a v1.x execution of this appendix.**

## **References**

\[1\] Z-Spin Collaboration, ZS-M47 v2.0, *The Z-Spin Seam Inclusion: Canonical Structure, Faithful Genuineness, the Two-Leg Clock, and the Metric-Dimension-3 Dirac Operator* (Z-Spin corpus, 2026), esp. §5–§6, §12.  
\[2\] Z-Spin Collaboration, ZS-M46, *the Koenigs-to-standard-pair construction (KH1–KH4), T6/T7, and T7b* (Z-Spin corpus, 2026).  
\[3\] Z-Spin Collaboration, ZS-F30 v1.4; ZS-F31 v1.4, *Covariant Cosmic Reality — the Exact Modular GKLS Spectrum, the Seam-Transport Realization (R2a), and App. D* (Z-Spin corpus, 2026).  
\[4\] Z-Spin Collaboration, ZS-M43 v1.4, *The Z-Goldstone Is a Coherent Superfluid, and Its Dissipation Is Scrambling* (Z-Spin corpus, 2026).  
\[5\] Z-Spin Collaboration, ZS-A23 v3.3; ZS-A24 v2.1, *Dimension-Weighted Mediator Semigroups* (Z-Spin corpus, 2026).  
\[6\] Z-Spin Collaboration, ZS-F33 v1.8; ZS-F34 v1.8; ZS-F36 v2.1, *the odd three-form, the Koenigs torus Σ₂, and the parent-action template* (Z-Spin corpus, 2026).

\[7\] A. A. Migdal, “Recursion equations in gauge field theories,” Zh. Eksp. Teor. Fiz. **69**, 810 (1975) \[Sov. Phys. JETP **42**, 413 (1975)\].  
\[8\] B. E. Rusakov, “Loop averages and partition functions in U(N) gauge theory on two-dimensional manifolds,” Mod. Phys. Lett. A **5**, 693 (1990).  
\[9\] E. Witten, “On quantum gauge theories in two dimensions,” Commun. Math. Phys. **141**, 153 (1991).  
\[10\] B. K. Driver, “YM₂: Continuum expectations, lattice convergence, and lassos,” Commun. Math. Phys. **123**, 575 (1989); A. Sengupta, *Gauge Theory on Compact Surfaces*, Mem. Amer. Math. Soc. **126**, no. 600 (1997).  
\[11\] T. Lévy, *Yang–Mills Measure on Compact Surfaces*, Mem. Amer. Math. Soc. **166**, no. 790 (2003); T. Lévy, *Two-Dimensional Markovian Holonomy Fields*, Astérisque **329** (Soc. Math. France, 2010).  
\[12\] R. Longo, “Index of subfactors and statistics of quantum fields. I,” Commun. Math. Phys. **126**, 217 (1989); “II. Correspondences, braid group statistics and Jones polynomial,” Commun. Math. Phys. **130**, 285 (1990).  
\[13\] R. Longo and K.-H. Rehren, “Nets of subfactors,” Rev. Math. Phys. **7**, 567 (1995).  
\[14\] A. Yu. Kitaev, “Anyons in an exactly solved model and beyond,” Ann. Phys. (N.Y.) **321**, 2 (2006).  
\[15\] A. Kitaev and J. Preskill, “Topological entanglement entropy,” Phys. Rev. Lett. **96**, 110404 (2006); M. Levin and X.-G. Wen, “Detecting topological order in a ground state wave function,” Phys. Rev. Lett. **96**, 110405 (2006).  
\[16\] P. Bonderson, M. Freedman, and C. Nayak, “Measurement-only topological quantum computation via anyonic interferometry,” Ann. Phys. (N.Y.) **324**, 787 (2009), arXiv:0808.1933.  
\[17\] A. W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, Princeton, 1986\) (the Weyl character formula).

## **Version History**

v1.3 (July 2026\) — **Terminal editorial release.** Integrates the third external review (of v1.2), whose verdict was that the paper is substantively closable and only editorial items remain; accordingly, **no theorem statement, epistemic status, numerical value, or condition is changed**. (1) Claim-ledger table repair: the vertical bars of |χ\_R(U)|² and |λ²| are escaped so they no longer parse as column delimiters; the Theorem A row carries all five columns. (2) Emphasis-artifact sweep: the two flagged prose italics are removed (translation; connection), and the underscore-after-punctuation class ()\_t; |\_{Σ₂}) is escaped throughout, fixing the two Version-History artifacts the review caught. (3) Correction of record: the route-(b) summary box described in the v1.2 Version History had been dropped from the v1.2 body by a silent (unasserted) edit failure; it is now applied in Appendix C.4 with the correction noted in place. (4) The novelty sentence is front-loaded in §4.1 (“The external theorem is standard; the new contribution is the identification of the Z-Spin seam clock corner as the two-sided cut object to which the theorem applies”). (5) README-style reproduction lines are added to §16 and Appendix B, together with the external-reproduction datum (27/27 PASS, 2.0 s; v1.2 review of record). (6) The ZS-F38 gate is pre-registered in Appendix C.5 with a drift-proof target — A\_Z restricted to Σ₂ gauge-equivalent to A\_K restricted to Σ₂; equivalently Hol\_{A\_Z}(γ) \= g⁻¹ Hol\_{A\_K}(γ) g for physical seam loops γ ⊂ Σ₂ — and the conclusion declares v1.3 terminal, scoping (H-Σ2) and the Appendix-D ε\_C\_int execution to ZS-F38 or a short addendum. The verification script zs\_f37\_verify\_v1\_3.py is check-identical to v1.2 (27/27 PASS fast mode; B2F/B2bF witnesses PASS under the flag); the v1.3 edits are text-only. Zero new fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes following the external review of ZS-F37 v1.2.)

v1.2 (July 2026): Second review-integration release, following a detailed external review of v1.1. **Presentation (the decisive item):** all mathematics is converted from OMML/LaTeX-rendered equations to corpus-house-style Unicode plaintext, after diagnosing that the review pipeline strips OMML content (ρ dropped, ½ read as “12”, χ stripped) while plain-text Unicode survives; every display equation the review flagged is restored in explicit form — ω\_i^(2 leg) \= d\_i²/Σ\_j d\_j² \= d\_i²/49 vs ω\_i^(1 leg) \= d\_i/Σ\_j d\_j \= d\_i/11; Z\_{g,b} \= Σ\_R (dim R)^(2−2g−b) Π χ\_R(U\_i) e^(−tC₂/2); χ\_Y(ρ) \= χ\_2(ρ)χ\_3(ρ) ≠ χ\_6(ρ) with χ\_2χ\_3 \= χ\_4 \+ χ\_2; Δχ(ρ\_b) \= −0.392090129; ρ\_b \= ½ ln(9/7) \= 0.125657; and Appendix D’s ε\_C\_int \= ‖Φ(P\_K) − P\_A‖/‖P\_A‖ with the conjugation variant and the Connes-cocycle form (Dφ\_K ∘ Φ⁻¹ : Dφ\_A)\_t ∈ 𝕋·1. **Theorem A safety:** the general statement now uses |χ\_R(U)|², with the explicit reduction |χ|² → χ² on the self-dual su(2) register (new check A9) and a novelty-scope note (externally standard consequence; internally new application). **Verifier executability (26 → 27 checks):** fast/full architecture — the default fast mode runs all 27 checks in \< 1 s (B2 via an exact analytic (α, γ) Fourier reduction \+ 1D Gauss β-quadrature; B2b via 1D Weyl character orthogonality, deviation 4.4 × 10⁻¹⁵, explicitly labeled a finite truncated witness of the imported-proven per-representation identity), and the v1.1 3D Euler-angle grid checks are retained as the optional witnesses B2F/B2bF (both PASS) behind RUN\_FULL\_SURFACE\_QUADRATURE. **Epistemic sharpening:** the abstract and conclusion carry the compression framing (“F37 does not fully close (H-YM2); it compresses it”) and the explicit class-vs-physical-identification separation; route (b) is condensed to its one-line summary box (G₆ alone cannot generate the nonabelian su(2)-graded character sector; A\_Z|\_{Σ₂} must enter); the conclusion adds the closure condition scoping any C\_int execution to ZS-F38 or a v1.x addendum. No theorem statement, epistemic status, numerical value, or upstream item of v1.1 is altered. Zero new fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes following the external review of ZS-F37 v1.1.)

v1.1 (July 2026): Review-integration release, following a detailed external review of v1.0. **Content additions:** (1) Appendix C executes the (H-YM2) promotion attempt and delivers a **decomposition** — gauge invariance and gluing/Markov consistency are DERIVED on the Σ₂ restriction of the seam gauge sector (the Markovian class is *forced* by gluing, Lévy classification), leaving the strictly smaller residual (H-Σ2) tied to the pre-existing ZS-F31 OPEN gate R2b plus the ZS-F36 Σ₂ localization (condition reuse; no new registry entry); the alternative direct-3-form route is executed to its dead-end and recorded CLOSED-NEGATIVE. (2) Theorem F37.A (Two-Leg Plancherel Selection) is stated Z-Spin-free before the register instance, for the external reader. (3) The surface-topology table (sphere/disc/cylinder/pair-of-pants with Z-Spin readings) and the gluing-bookkeeping warning (the single-argument kernel does not glue — a machine-caught trap) are added to §3. (4) §9 is elevated to an external replication protocol with the two targets Δχ \= −0.392090129 and L1 \= 0.00919466866. (5) Appendix D specifies the finite C\_int computation completely (T7b gate equation, four inputs, residual norm ε\_C\_int); C\_int remains OPEN by design. (6) The conclusion carries the four-line closed/open/non-claim summary. **Presentation corrections:** the (H-YM2) conditionality is stated in the abstract’s second sentence; all discriminant statements are written in explicit displayed form (χ\_Y \= χ\_2χ\_3, not χ\_6; χ\_2χ\_3 \= χ\_4 \+ χ\_2 ≠ χ\_6) to remove any rendering ambiguity. **Verification hardening (24 → 26 checks, all PASS):** B2 Haar MC replaced by deterministic Euler-angle quadrature (\< 10⁻⁹); NEW B2b cylinder Markov/gluing check (the machine witness of (H-YM2)’s gluing half, fail-closed on the wrong kernel); B4 split into B4a (tensor, componentwise 10⁻¹²) and B4b (irreducible χ\_6 control, separated); C3 upgraded from “nonzero” to exact multiplicities (2, 2, 2); D1 upgraded to ten locked digits z\* \= 0.4382829367 \+ 0.3605924719i; the E2 script comment corrected of record (0.3416). No numerical value, theorem statement, or upstream status of v1.0 is reversed; the v1.0 condition registry is strictly shortened. Zero new fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes following the external review of ZS-F37 v1.0.)

v1.0 (July 2026): Initial public release. Executes the ZS-M47 §12.3 handover to ZS-F37: the action-level Two-Leg Selection Theorem (F37.T1, DERIVED-CONDITIONAL on the single new named condition (H-YM2)); the one-leg exclusion by the topological and parity double lock (F37.P1); the mediation vertex derived from the three-boundary amplitude of the same action, reproducing YL1–YL5 and executing F-M47.27 conditionally (F37.T2); the structural half of (H1) discharged by centrality (F37.T3), with C\_int carried OPEN in its ZS-M46 T7b reformulated form (a wording-level reconciliation of record between the M47 handover row and M46 T7b, no upstream status altered); the finite-ρ consistency deliverable executed (χ₂χ₃ curve, Δχ \= −0.392090129, L1 \= 0.00919466866 at ½ln(9/7)); and the t\* \= **Q** depth selector re-registered as a NON-CLAIM. Imported-proven pillars: the exact two-dimensional heat-kernel gauge amplitude and its rigorous measure (Migdal; Rusakov; Witten; Driver; Sengupta; Lévy, including the Markovian-holonomy-field classification used as the class-universality shield), the Longo index–statistics theorem and the Longo–Rehren global index, and the Plancherel / topological-charge d²/𝒟² family. Verification 24/24 PASS (zs\_f37\_verify\_v1\_0.py). Zero new fitted parameters; (**A**, **Q**, dim **Z**) \= (35/437, 11, 2\) LOCKED. (Consolidated from internal Z-Spin Collaboration deep-exploration notes following ZS-F36 v2.1 and ZS-M47 v2.0.)