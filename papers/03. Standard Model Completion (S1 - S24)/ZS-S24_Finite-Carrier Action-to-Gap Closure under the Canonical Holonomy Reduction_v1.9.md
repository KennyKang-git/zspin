# **ZS-S24**

# **Finite-Carrier Action-to-Gap Closure under the Canonical Holonomy Reduction: The Reflection-Positive Slab Realisation, the Two-Tier Transfer-Matrix Gap, and the Exact Electric-Limit Spectrum of the Z-Spin SU(3) Carrier**

**Author:** Kenny Kang · Z-Spin Cosmology Collaboration **Date:** July 2026 **Theme / paper code:** ZS-S24 — Standard Model line, finite-carrier spectral gap **Version:** v1.9 **FINAL** (supersedes v1.8–v1.0, July 2026\) **Companion:** zs\_s24\_verify\_v1\_9.py

**Verification: 100 ledger entries | 69 executable checks (C: 36 closed-form, 14 exhaustive, 13 control, 6 confirmation) | 16 math-theorem blocks (M) | 15 consistency gates (X) | 0 FAIL | Zero Free Parameters | A \= 35/437, Q \= 11, dim Z \= 2, λ₁ \= 1.2428416164, λ\_h all LOCKED and none re-fitted | SHA256(companion) \= 6876ed2b7d388494d67b6da28857480c0bb20184ba9c2e325b0a10525d67ee4c**

---

# §0. Abstract

**The theorem.** On a finite cell complex with E edges, G \= SU(3), **M** \= G^E, let **L** be real, symmetric, **uniformly elliptic**, essentially self-adjoint on C^∞(**M**), with **\[L, U(h)\] \= 0** for every h in the local gauge group G^V, and let V ∈ C(**M**, ℝ) be gauge invariant. Then H\_g \= g²L \+ g^{−2}V has compact resolvent, a positivity-improving heat semigroup, a unique strictly positive — hence gauge-invariant — ground state, and a strictly positive physical gap for every g \> 0 (**Theorem S24.2**). Theorem S24.2′ builds such an L from a coefficient tensor by Friedrichs extension, which settles operator ordering for U-dependent coefficients.

**The admissible class.** Uniform ellipticity **(E)** and gauge commutation **(G)** are logically independent in both directions (negative controls C133, C137). **Proposition S24.2d** gives the necessary and sufficient condition for (G) — Ad-equivariance of the coefficient tensor — and K1, K2, K3 are *sufficient certificates*, never a classification.

**The reduction.** §4 declares **(R1)**: link variables are the edge holonomies U\_e \= P exp ∫\_e A; and **(R2)**: the discrete action is a real, continuous, gauge-invariant, time-reflection-symmetric **(RS)** function of the plaquette holonomies of K × ℤ. No homogeneous linear coefficient map can be equivariant (Proposition S24.3a), so (R1) is the canonical exact equivariant choice. The product complex fixes only the **support** of the variables: it forces neither edge-additivity (retracted, S24-R9) nor time-locality (retracted, S24-R11), and negative control C158 exhibits an action built from two-slice variables that is non-Markov in time.

**Time-locality, derived.** **Theorem S24.12** replaces the retracted inferences with a proof: under (R1) every configuration variable is slice- or slab-supported, so if the master Lagrangian is local and contains **no time derivatives beyond first order** — hypothesis **(S1)**, which the ZS-S14 action satisfies term by term — then ∫dt splits over slabs and, after integrating the slab-interior variables against a slab-factorised reduction measure **(S2)**, the partition function is an exact one-step transfer product with kernel K(U\_t, U\_{t+1}) \= ∫dW\_t e^{−S\_t(U\_t, W\_t, U\_{t+1})}.

**The gap, in tiers.** **Theorem S24.9(i)**: the one-step kernel is the exponential of a real continuous function, hence continuous, symmetric and pointwise strictly positive on the compact **M**; T is Hilbert–Schmidt, self-adjoint, gauge-commuting and positivity improving; Perron–Frobenius gives a simple top eigenvalue with a strictly positive, hence gauge-invariant, eigenvector, so the **correlation-decay gap log(t₀/|t₁^phys|) is strictly positive**. **Theorem S24.9(ii)**: if T is additionally **positive and injective on the physical subspace** — hypothesis **(R2⁺)**, equivalently reflection positivity with a non-degenerate form — then H \= −log T is self-adjoint and **Δ\_phys \= log(t₀/t₁^phys) ∈ (0, ∞)**.

**The constructive step, new in v1.6.** (R2⁺) is not imported. **Theorem S24.14** *realises* it from the corpus's own data: for any L satisfying (E) ∧ (G) and any bounded gauge-invariant V, the slab family

**T\_a \= e^{−aV/2} e^{−aL} e^{−aV/2} \= S\*S,  S \= e^{−aL/2} e^{−aV/2},  a \> 0**

is manifestly positive, injective, compact, positivity improving with a continuous strictly positive kernel, and gauge-commuting; the multi-slab measure it generates is reflection positive by construction; and −(1/a) log T\_a → L \+ V by symmetric Trotter, in operator norm for each fixed t because V is bounded and L has compact resolvent, so the finitely many lowest eigenvalues converge. In the coupling-scaled form the family is **T\_{a,g} \= e^{−ag^{−2}V/2} e^{−ag²L} e^{−ag^{−2}V/2}**, matching H\_g \= g²L \+ g^{−2}V. Hence **the ZS-S14 finite reduction admits a canonical reflection-positive symmetric-semigroup realisation**, and tier (ii) holds for it without any appeal to the Wilson action.

The first-order structure of the 24-fold level. Beyond Δ\_{E,1} \= (10/3)g² with d₁ \= 24 and Δ\_{E,2} \= 4g² with d₂ \= 40 (Theorem S24.4), Proposition S24.15′ resolves the magnetic operator on the first eigenspace for an arbitrary real class function. For a plaquette f ≠ C, every non-trivial character component has vanishing matrix elements within P₁, while the trivial component contributes only a common scalar. For f \= C, the diagonal receives only the 1 and 8 characters and is identical on the two orientations, while the orientation flip receives only the 3 and 6̄ characters. Writing μ \= a\_3\*\*^{(5)} \+ a\_6̄^{(5)}\*\*, one obtains

P₁V\_BP₁ \= c₀P₁ \+ Σ\_C \[ μ|C, 3̄⟩⟨C, 3| \+ conj(μ)|C, 3⟩⟨C, 3̄| \],

with spectrum c₀ ± |μ|, each 12-fold. Thus the level splits 24 → 12 ⊕ 12 if and only if μ ≠ 0; the two branches are separated by 2|μ|. For charge-conjugation-even actions the block is pure σ\_x; the Wilson form is the special case μ \= −κ₅/6. After subtracting the vacuum first-order shift, the lowest physical gap satisfies

Δ(g) \= (10/3)g² \+ \[a\_8\*\*^{(5)} − |μ|\]g^{−2} \+ O(g^{−6}), g → ∞.\*\*

Each 12-dimensional sector carries A ⊕ T₁ ⊕ T₂ ⊕ H under the rotational icosahedral group I ≅ A₅. The v1.6 claim that P₁V\_BP₁ vanished is retracted (S24-R12): it contracted the bra without conjugation.

**What remains.** Gate **F-S24.18** — whether the *exact* Whitney-integrated ZS-S14 slab action coincides with a member of the canonical family T\_a, or is otherwise reflection positive — and gate **F-S24.14**, edge-additivity, which affects only the differential picture. **F-S24.19** ((S1)) is closed by inspection of the ZS-S14 Lagrangian. Weak coupling is unchanged: Inv(**8**) \= 0 while Inv(**8**⊗**8**) \= 1, so the candidate is 2√(rλ₁) (**Proposition S24.6**).

---

# Epistemic Status Legend

> **PROVEN** — proved here or in a cited Z-Spin paper from stated hypotheses. **PROVEN-CONDITIONAL** — proved, but conditional on a named hypothesis or declaration. **DERIVED-CONDITIONAL** — follows from a controlled approximation whose error is not yet bounded. **DECLARATION** — an axiom-level choice, recorded as such and never counted as a proof. **OPEN** — a well-posed question this paper does not answer. **RETRACTED** — previously claimed here or upstream, now withdrawn with a documented reason. **NON-CLAIM** — explicitly outside the paper's scope. **CONTROL / CONFIRMATION** — companion checks. A *control* tests whether a hypothesis is automatic; a *confirmation* is a finite check of a statement proved over an infinite range. Neither is evidence for a physical value (Appendix D).

---

# §1. Introduction

## §1.1 What ZS-S20 to ZS-S23 could not close

ZS-S20 to ZS-S23 repeatedly reached the same wall. The Hodge measure on the carrier was not identified (ZS-S20); the orbit weights σ \= m₅₆/m₆₆ and ρ \= β₅/β₆ were not selected (ZS-S21); the single-plaquette locality assumption (H-W) was carried unproved (ZS-S23 §5.1); and the exact face-and-prism integration constants κ\_p were left as gate F-S23.6. Each paper concluded that one computation stood between the corpus and a physical gap.

The reframing of this line is that **none of those quantities is needed for the gap to exist**. They set its *value*. This paper proves the existence statement for a class wide enough to contain every candidate the earlier papers could not narrow, and keeps the value questions in a separate column throughout (Table 2.1).

## §1.2 Version history of the argument, in one paragraph

v1.0 split the result out of ZS-S22 but shipped a companion inherited from ZS-S22 that contradicted its own retractions (S24-R4). v1.1 proved a general gap theorem but inferred local gauge invariance from positivity of the edge coupling, which is false for non-abelian G (S24-R6). v1.2 corrected that but treated the three kinetic templates as a classification (S24-R8) and mismatched a transporter convention. v1.3 closed the equivariance gate but inferred edge-additivity of the action from the support of the cells (S24-R9). v1.4 corrected that and then made the same inference one level up, reading cell time-support as action time-locality (S24-R11). v1.5 corrected that, derived time-locality from the Lagrangian instead, and left the reflection positivity of the slab action as the residue. **v1.6 removes that residue constructively** (§4.6b) and adds a sharper strong-coupling statement (§6.2). The repeated error — inferring a property of the *action* from the *support* of the cells — is registered permanently as gate F-S24.20.

## §1.3 What v1.9 changes

**(i) The projected magnetic operator is Hermitian, not σ\_x (§6.2, S24-C27).** v1.8 generalised Proposition S24.15′ to arbitrary real class functions but kept a *real* coefficient μ and a pure σ\_x block. That step is wrong: SU(3) characters are complex, and reality of Φ imposes only **a\_{R̄} \= conj(a\_R)**. The function Φ \= i\[χ\_**3** − χ\_**3̄**\] is real-valued with a\_**3** \= i and projects to **σ\_y** *(negative control C172)*. The correct general statement is

> **P₁V\_BP₁ \= c₀P₁ \+ Σ\_C \[ μ|C, 3̄⟩⟨C, 3| \+ conj(μ)|C, 3⟩⟨C, 3̄| \],  spectrum c₀ ± |μ|,**  
>   
> with eigenvectors (|C, **3**⟩ ± e^{i arg μ}|C, **3̄**⟩)/√2. The σ\_x form and the orientation-even/odd eigenvectors are recovered exactly when the action is **charge-conjugation-even**, Φ(U^{−1}) \= Φ(U), which the Wilson form is *(C173)*.

**(ii) The splitting is conditional (§6.2, all summaries).** The level splits 24 → 12 ⊕ 12 **if and only if μ ≠ 0**. A magnetic class function built only from the **1** and **8** characters leaves it degenerate at first order. Abstract, Terminal Ledger, M216 and Conclusion are unified on this wording.

**(iii) "Every f ≠ C term annihilates P₁" is false (§6.2, S24-C28).** The trivial character of a distant plaquette acts as the identity *(C174)*. Only the **non-trivial** components annihilate; the trivial ones contribute the common scalar already present in c₀.

**(iv) The proof's conjugation line is corrected.** dim Inv(**3**⊗R⊗**3**) \= mult(R̄, **3**⊗**3**) with **3**⊗**3** \= **6**⊕**3̄** — not, as v1.8 wrote, a multiplicity in **3̄**⊗**3̄**. The irrep lists were right; the intermediate identity was not.

**(v) C170 is re-weighted (Appendix D, S24-C29).** It scans p, q ≤ 3, which is a finite window, not all irreps. The authority for the selection rules is now the pair of closed-form decompositions **3̄**⊗**3** \= **1**⊕**8** and **3**⊗**3** \= **6**⊕**3̄**, which prove them for every irrep; C170 is a **confirmation**.

**(vi) Three declared repairs that did not land (§9.4, S24-C30).** v1.8 §1.3 stated that five stale companion declarations had been repaired. Two were. M205 still closed F-S24.12 by the retracted Theorem S24.7 route, M207 still omitted (T) from its second clause, and M215 still said "strong resolvent sense". All three are repaired here, and new gate **X313** now **scans the shipped companion source** for every string this version claims to have removed, so that a declared repair which fails to apply becomes a build failure rather than a claim.

**(vii) Excited-energy shift and physical-gap shift are separated (§6.2, S24-C31).** The eigenvalues c₀ ± |μ| are first-order shifts of the excited cluster, not yet the physical-gap correction. The electric vacuum shifts by Σ\_f a\_1^{(f)}, so subtraction gives the exact first-order coefficient a\_8\*\*^{(5)} − |μ|\*\* and, by bounded perturbation theory for the isolated cluster,

Δ(g) \= (10/3)g² \+ \[a\_8\*\*^{(5)} − |μ|\]g^{−2} \+ O(g^{−6}).\*\*

Abstract, Proposition S24.15′, Terminal Ledger, Conclusion and companion M216 are synchronised on this formula.

## §1.4 What v1.8 changed

**(i) Proposition S24.15′ is generalised, not narrowed (§6.2).** The v1.7 statement was posed for an arbitrary real class function Φ\_f but proved only for the fundamental Wilson form, and the two are not the same hypothesis: ⟨C, **3**|χ\_**8**|C, **3**⟩ \= dim Inv(**3̄**⊗**8**⊗**3**) \= 1, so the diagonal does **not** vanish in general. The gap in the argument is real. Its resolution, however, strengthens rather than restricts the result: an exhaustive scan over all irreps shows the diagonal element is non-zero only for R \= **1** and R \= **8** and is **identical on |C, 3⟩ and |C, 3̄⟩**, so the diagonal part is a multiple of the identity on P₁ and cannot split anything, while the orientation-flip element is non-zero only for R \= **3** and R \= **6̄** *(C170)*. The f ≠ C exclusion is likewise general, since |∂f \\ C| ≥ 5 forces those edges to carry the loop irrep itself *(C171)*. Hence **P₁V\_BP₁ \= c₀P₁ \+ μΣ\_Cσ\_x^{(C)} for every real class function**, with μ \= a₃ \+ a\_**6̄**; the Wilson form is the special case μ \= −κ₅/6.

**(ii) The icosahedral statement is attributed to the rotational group I (§6.2, S24-C24).** Check C169 uses the order-60 character table of **I ≅ A₅**, with classes 1 \+ 12 \+ 12 \+ 20 \+ 15\. It therefore establishes the decomposition for **I**, whereas the full icosahedral group has order 120 and requires parity labels the companion never examines. All such statements now say *rotational icosahedral group I*; the full I\_h parity decomposition is a new non-claim, NC-S24.14. New gate **X312** fails on the loose wording in either file.

**(iii) Five stale companion declarations are repaired (S24-C25).** The \[S14\] section header still printed the retracted title; M207 omitted (T) from the hypotheses of the edge-diagonal route; M213 and M214 still derived (T) from (R1) ∧ (S1) without (S2); M205 still closed F-S24.12 by Theorem S24.7, the v1.3 route retracted as S24-R9; and the X310 message still named the retracted proposition. None changed a computed result, but this line has twice shipped a companion asserting what the manuscript denied, so they are removed before termination.

**(iv) Numbering and scope wording.** §1.3 to §1.6 renumbered; the X302 description updated; the companion docstring's "one of three weights" corrected to four; and C161's message narrowed to f ≠ C, the f \= C case being a genuine exception rather than an instance.

## §1.5 What v1.7 changed

**(0) The v1.6 first-order claim is retracted (§6.2, S24-R12).** ZS-S24 v1.6 asserted that P₁V\_BP₁ vanishes on the first electric eigenspace and inferred an error estimate three powers sharper than Weyl's. The matrix element of a plaquette character between loop states is ∫ conj(χ\_{R′})χ\_fχ\_R, so the bra enters conjugated; v1.6's check evaluated the *diagonal* element, which does vanish, and drew a conclusion about the whole block. The orientation-flip element is 1/2, because **3** ⊗ **3** \= **3̄** ⊕ **6**. **Proposition S24.15′** replaces the claim: the degeneracy splits at first order into two 12-fold levels, the error estimate reverts to O(g^{−2}), and the coefficient is now identified with the pentagon plaquette weight κ₅. New gate **X311** fails on the retracted wording, and gate **F-S24.22** records the general lesson — a matrix element is not a multiplicity until the bra is conjugated.

**(0′) Theorem S24.14's convergence statement is tightened (§4.6b).** The universal O(a²) rate is withdrawn: C164 is a finite-dimensional control and no infinite-dimensional rate is claimed. Convergence of individual eigenvalues is justified explicitly, V being bounded and L having compact resolvent, and the coupling-scaled family **T\_{a,g}** is written out. "Canonical" is softened to "canonical symmetric choice" (S24-C23).

## §1.6 What v1.6 changed

**(i) (R2⁺) is realised, not assumed (§4.6b, Theorem S24.14).** The corpus already owns a self-adjoint non-negative gauge-commuting L (Theorem S24.2′) and a bounded gauge-invariant V. The symmetric splitting T\_a \= e^{−aV/2}e^{−aL}e^{−aV/2} is of the form S\*S, hence positive and injective; it commutes with the gauge group because it is a product of functions of L and of V; its kernel is continuous and strictly positive; and symmetric Trotter returns L \+ V as a → 0\. Reflection positivity is therefore available canonically, without adopting the Wilson action.

**(ii) Theorem S24.12 is completed with the slab-interior integration (§4.5b).** v1.5 passed from "each variable is slab-supported" to "S\_step depends on U\_t and U\_{t+1}" in one step. A slab also carries interior variables W\_t — temporal links and interior profiles. The correct statement integrates them out, K(U\_t, U\_{t+1}) \= ∫dW\_t e^{−S\_t(U\_t, W\_t, U\_{t+1})}, and requires the reduction measure to factorise over slabs, hypothesis **(S2)**.

**(iii) C159 is re-weighted (Appendix D).** It tested a deliberately factorised scalar model, so it verified the factorisation identity and the test, not Theorem S24.12. It is now a **control**, not a closed-form check.

**(iv) (S1) is stated correctly and its gate is closed (§4.4, §9.1).** "First order in ∂\_t" was misleading: the Yang–Mills density is *quadratic* in ∂\_tA\_i. The condition is that the Lagrangian contain **no time derivatives beyond first order**, which the ZS-S14 terms −¼G^a\_{μν}G^{aμν}, |D\_μH₅|² and ψ̄iγ^μD\_μψ satisfy term by term. Gate F-S24.19 is **closed by inspection**.

**(v) Proposition S24.15′ (§6.2).** The 24-fold degeneracy **is** split at first order, into two 12-fold levels, by the pentagon's own plaquette acting as σ\_x in the orientation index. Each level carries A ⊕ T₁ ⊕ T₂ ⊕ H under the rotational icosahedral group I.

**(vi) Stale conditions removed (§9.3, S24-C20).** Four places still carried superseded hypotheses: the companion's declaration of tier (ii), its closing summary, Table 4.1's last row, the Terminal Ledger's description of (R1), and §3.5's restriction of admissibility to the three templates. All are corrected and gate **X310** now fails on their wording.

## §1.7 What is not claimed

No statement about ℝ⁴, the continuum limit, renormalisation, or the Clay problem. No claim that the SU(3) spectrum has been computed: Theorem S24.4 gives two levels of a *diagonal* operator and Theorem S24.5 the leading asymptotics. No numerical constant is derived, predicted or fitted; A, Q, dim Z, λ₁ and λ\_h enter only as inherited LOCKED values.

---

# §2. Scope: the Two-Column Discipline

**Table 2.1.** Existence inputs versus value inputs.

| input | needed for gap existence? | needed for gap value? |
| ----- | :---: | :---: |
| finiteness of the carrier | **yes** | yes |
| uniform ellipticity (E) | **yes** | yes |
| gauge commutation (G) | **yes** | yes |
| gauge equivariance of the reduction | **yes** — closed by (R1), §4.2 | yes |
| no time derivatives beyond first order (S1) | **yes** — supplies time-locality, §4.5b | yes |
| slab factorisation of the reduction measure (S2) | **yes** — §4.5b | yes |
| positivity \+ injectivity of T (R2⁺) | only for the **Hamiltonian** tier; realised by §4.6b | yes |
| temporal edge-additivity (L) | only for the **differential** tier | yes |
| boundedness of the magnetic form | **yes** | yes |
| exact κ\_p (F-S23.6), orbit weights σ, ρ, the Hodge measure | **no** | yes |
| single-plaquette locality (H-W) | **no** | yes |
| identity of K as K\_TI \= GP(1,1) | **no** | yes (value and degeneracy only) |

Only §5–§7 carry conditions beyond this table: **(C-K)** the carrier is K\_TI \= GP(1,1) (ZS-S22 S22.10); **(C-U)** the electric metric is uniform; **(L)** and **(T)**, since writing an electric Hamiltonian presupposes a one-step edge-additive temporal sector; and **(C-W)** the weak-coupling normalisation r.

**Evidential weight.** Because the v1.1 error survived a run in which every check passed, each executable check carries a weight: *closed-form*, *exhaustive*, *control*, or *confirmation*. Appendix D tabulates all sixty-nine. **\[STATUS: declaration; gate F-S24.13\]**

---

# §3. The General Finite-Carrier Gap Theorem

## §3.1 Theorem S24.1

> **Theorem S24.1.** Let H \= (g²/2)Σ\_e Δ\_e \+ g^{−2}Σ\_f Φ\_f on L²(SU(3)^E), with Δ\_e the Laplace–Beltrami operator of the e-th factor and each Φ\_f a real-valued continuous class function of a plaquette holonomy. Then H is self-adjoint with compact resolvent, its spectrum is discrete, and its physical ground state is unique.

**Proof.** SU(3)^E is a compact connected Lie group, so Σ\_eΔ\_e has compact resolvent by Peter–Weyl; a continuous function on a compact space is bounded, so Kato–Rellich preserves self-adjointness and compactness of the resolvent; the Feynman–Kac representation with a bounded real potential preserves strict positivity of the heat kernel; Perron–Frobenius gives uniqueness.

**\[STATUS: PROVEN — M200. In the language of §3.4 this Hamiltonian is of class K1 with equal weights, which is why gauge commutation may be asserted without further argument.\]**

## §3.2 Theorem S24.2 — the Commuting-Elliptic Gap Theorem

> **Theorem S24.2.** Let **M** \= G^E with G \= SU(3), acted on by G^V through U(h)ψ(U)*e \= ψ(h*{s(e)}^{−1}U\_e h\_{t(e)}). Let L be real, symmetric, second order on C^∞(**M**), with **(E)** σ\_L(x, ξ) ≥ c|ξ|² uniformly, c \> 0 — *L is **uniformly elliptic***; and **(G)** **\[L, U(h)\] \= 0** for all h ∈ G^V. Let V ∈ C(**M**, ℝ) be gauge invariant and H\_g \= g²L \+ g^{−2}V. Then **(a)** L is essentially self-adjoint with compact resolvent; **(b)** V is bounded, so H\_g is self-adjoint, bounded below, with compact resolvent; **(c)** e^{−tH\_g} is positivity improving; **(d)** the ground state ψ₀ is unique and strictly positive; **(e)** by (G), U(h)ψ₀ \= ψ₀, so ψ₀ ∈ ℋ\_phys \= P\_Gℋ with **P\_G \= ∫\_{G^V} U(h) dh**; **(f)** hence **Δ\_phys(g) \> 0 for every g \> 0**.

**Proof.** (a) Gårding plus Rellich–Kondrachov on a closed manifold. (b) Kato–Rellich. (c) (E) makes the diffusion non-degenerate, so the heat kernel is strictly positive on the connected **M**, and Feynman–Kac gives e^{−tH\_g}(x,y) ≥ e^{−t sup|V|/g²}p\_t(x,y) \> 0\. (d) Perron–Frobenius. (e) U(h)ψ₀ is another ground state by (G); uniqueness forces equality. (f) Discreteness.

**\[STATUS: PROVEN — M201. Both hypotheses are load-bearing: (e)–(f) fail without (G), and (a), (c) fail without (E).\]**

## §3.3 Why (E) does not imply (G)

> **Proposition S24.2a.** With X\_e^a the left-invariant fields on the e-th factor, the source-vertex action is a left translation and leaves X\_e^a fixed, while the target-vertex action conjugates by the adjoint: X\_e^a ↦ Σ\_b Ad(h\_{t(e)}^{−1})\_{ba}X\_e^b. The map **Ad : SU(3) → SO(8)** is orthogonal with unit determinant *(C132)*.  
>   
> **Proposition S24.2b.** Hence Σ\_a X\_e^a X\_{e′}^a transforms by Ad(h\_{t(e)})ᵀAd(h\_{t(e′)}). If t(e) \= t(e′) this is the identity and the term is invariant; if t(e) ≠ t(e′) the two group elements are independent and the deviation is at least 6 × 10^{−1} over 500 random pairs. An **untransported off-diagonal coupling between links with distinct targets does not satisfy (G)**, however positive the coefficient matrix *(negative control C133, positive control C134)*.

**\[STATUS: PROVEN. This refutes the v1.1 form of Theorem S24.2, retracted as S24-R6.\]**

## §3.4 Admissible kinetic operators: criterion, certificates, construction

> **Proposition S24.2d (necessary and sufficient).** Fix the convention 𝕏\_e ↦ 𝕏\_e Ad(h\_{t(e)}) for the row vector of left-invariant fields. The quadratic form 𝕏\_e C\_{ee′}(U) 𝕏\_{e′}ᵀ is gauge invariant **iff**  
>   
> **C\_{ee′}(h·U) \= Ad(h\_{t(e)})ᵀ C\_{ee′}(U) Ad(h\_{t(e′)})  for all h ∈ G^V.**  
>   
> The tensors satisfying this form a module: closed under real linear combination with gauge-invariant scalar coefficients, under composition of transporters, and under sums over paths *(C150)*.

**\[STATUS: PROVEN. Membership in one of the templates below is *sufficient*, never necessary — S24-R8, S24-C9. Coefficient tensors satisfying the criterion but lying in no single template include a Wilson-loop trace times a transported term, and sums over distinct paths.\]**

**Three sufficient certificates.** **(K1)** L \= −½ Σ\_e a\_e Σ\_a (X\_e^a)², a\_e \> 0: each summand is a bi-invariant Casimir, so (G) is automatic and (E) holds with c \= min a\_e *(C132)*. **(K2)** Untransported blocks among links sharing a target vertex: all such links carry the same Ad(h\_v), the assembled matrix is block diagonal *(C134)*. **(K3)** Ad-transported cross terms. **Convention, fixed once:** P\_{ee′}(U) transports from t(e) to t(e′), so P\_{ee′} ↦ h\_{t(e)}^{−1}P\_{ee′}h\_{t(e′)}; setting C\_{ee′} \= A\_{ee′}Ad(P\_{ee′}) satisfies the criterion by **Ad(h) Ad(h^{−1}Ph′) Ad(h′)ᵀ \= Ad(P)** *(C135)*, with cocycle form P\_{ee′} \= P\_e^{−1}P\_{e′} *(C136)*.

> **Theorem S24.2′ (Friedrichs construction).** Let C(U) be real, symmetric, continuous, satisfying Proposition S24.2d, with inf\_U λ\_min(C(U)) \= c \> 0\. Define q\[ψ\] \= ½∫ Σ (X\_e^aψ)\* C^{ab}*{ee′}(U) (X*{e′}^bψ) dμ. Then q is closable, symmetric, non-negative, gauge invariant, and q\[ψ\] ≥ c‖∇ψ‖², so its form domain is H¹(**M**). Its Friedrichs extension L is self-adjoint, non-negative, commutes with every U(h), has compact resolvent by Rellich–Kondrachov, and generates a positivity-improving semigroup. Hence L satisfies (E) and (G).

**Proof.** Symmetry and non-negativity from those of C(U); gauge invariance by substituting the transformation rules and using orthogonality of Ad with invariance of Haar measure; the two-sided bound c‖∇ψ‖² ≤ q\[ψ\] ≤ ‖C‖\_∞‖∇ψ‖² identifies the form domain; positivity improvement because q is a Dirichlet form and the diffusion is irreducible on the connected **M**.

**\[STATUS: PROVEN — M210. This is the operator-theoretic content that "symmetrised" left undetermined; S24-C11.\]**

> **Proposition S24.2c.** (G) does not imply (E). For a **cocycle** transporter family the twisted symbol is orthogonally equivalent to A ⊗ I₈ and inherits the ellipticity constant of A *(C136)*; for a non-cocycle family — generic in the presence of curvature — the twisted symbol can be indefinite even for positive definite A, with minimum eigenvalue below −2.9 in a seeded search *(negative control C137)*.

**\[STATUS: PROVEN. With C133 this shows (E) and (G) are independent in both directions.\]**

## §3.5 What Theorem S24.2 removes

| obstruction | why it does not obstruct existence |
| ----- | ----- |
| single-plaquette locality (H-W) | V is an arbitrary continuous gauge-invariant function; cross-face terms are allowed |
| orbit weights σ, ρ | they set entries of the kinetic tensor, never whether (E) or (G) holds |
| exact κ\_p | likewise; the ellipticity constant is positive for every admissible choice |
| diagonal mass lumping | not needed: K2 and K3 admit genuine off-diagonal coupling |
| Hodge-measure non-identifiability | the whole non-identified family lies in the hypothesis class, provided the reduced operator satisfies (E) and (G) |
| identity of K | E is arbitrary finite; only the *value* needs K \= K\_TI |

**\[STATUS: PROVEN, corollary of Theorem S24.2\]**

---

# §4. Action-to-Gap: the Canonical Reduction and the Closure of F-S24.12

## §4.1 Corollary S24.3

> **Corollary S24.3.** Suppose **(1)** ZS-S14 supplies a positive Yang–Mills kinetic form 𝒦(α, α) ≥ 0 vanishing only on the zero form; **(2)** the reduction uses a finite, linearly independent Galerkin basis {w\_e}; **(3)** the magnetic sector is a continuous gauge-invariant function of the holonomies; **(4)** the finite reduction intertwines local gauge transformations and the reduced kinetic operator commutes with G^V. Then A\_{ee′} \= 𝒦(w\_e, w\_{e′}) is symmetric positive definite, supplying **(E)**; the magnetic term is bounded and real; **(4)** supplies **(G)**; and **Δ\_phys(g) \> 0 for every g \> 0**.

**Proof.** cᵀAc \= 𝒦(Σc\_ew\_e, Σc\_ew\_e) \> 0 by linear independence; on a finite-dimensional space positive definiteness is uniform ellipticity. Compactness gives boundedness. Then Theorem S24.2.

**\[STATUS: PROVEN-CONDITIONAL on (1)–(4) — M202. Hypothesis (4) is not implied by (1)–(3); Proposition S24.2b is the counterexample. Membership in K1, K2 or K3 is a sufficient certificate for it. Controls C124, C125 test the Gram step on *generic* vectors and exhibit the failure mode; they do NOT test the ZS-S14 Whitney basis, and C126 does not test admissibility.\]**

## §4.2 Which reduction is equivariant

> **Proposition S24.3a.** No homogeneous linear map W, injective on the Galerkin space, can satisfy W(A^g) \= ρ(g)W(A) for a representation ρ: setting A \= 0 gives W(g^{−1}dg) \= 0 for every g, contradicting injectivity, since the pure-gauge connections span a non-zero subspace. The gauge action A ↦ g^{−1}Ag \+ g^{−1}dg is affine and inhomogeneous; a linear map is homogeneous. **\[PROVEN — M209\]**  
>   
> **Theorem S24.3′.** For every gauge transformation g, **hol\_e(A^g) \= g(s(e))^{−1} hol\_e(A) g(t(e))**, by naturality of parallel transport under bundle automorphisms \[37\]. The holonomy map therefore intertwines the continuum gauge action with U\_e ↦ h\_{s(e)}^{−1}U\_e h\_{t(e)}. **\[PROVEN — M205; cf. \[7\], \[8\], \[35\]\]**

## §4.3 Gate F-S24.12, stated correctly

> **Gate F-S24.12.** Does the reduced kinetic operator satisfy **(E)** and **(G)**?

The v1.2 phrasing in terms of membership in the three templates was too narrow (S24-R8). The gate is coefficient-free: no κ\_p, no orbit weight, no measure selection. §4.4–§4.6b settle it.

## §4.4 The canonical reduction and the hypothesis sets

> **(R1) Link variables.** The Z-Spin finite reduction is the **holonomy map** U\_e \= P exp ∫\_e A. The linear Whitney coefficient map is retained only as a *value* instrument. **(R2) Discrete action.** Real, continuous, gauge-invariant and time-reflection-symmetric **(RS)** in the plaquette holonomies of K × ℤ. **(S1) Derivative order.** The master Lagrangian is local and contains **no time derivatives beyond first order**. **(S2) Slab factorisation.** The reduction measure factorises over time slabs: dμ \= Π\_t dμ\_slab(W\_t) Π\_t dU\_t. **(R2⁺) Operator positivity.** T is positive **and injective** on ℋ\_phys: ⟨ψ, Tψ⟩ \> 0 for every non-zero physical ψ. Equivalently, reflection positivity with a non-degenerate form. *Tier (ii) only.* **(L) Edge-additivity.** S\_step \= Σ\_e s\_e(U\_{0e}). *Tier (iii) only.*

**\[STATUS: (R1)–(R2) are a DECLARATION, registered as Z-A-R. (S1), (S2) are structural properties of the master action and of the reduction, free of coefficients. (R2⁺) and (L) are hypotheses invoked where named.\]**

**On (S1).** "First order in ∂\_t" would be wrong: the Yang–Mills density is *quadratic* in ∂\_tA\_i, since F\_{0i}F^{0i} is. The condition is on the **derivative order**, not the power. The ZS-S14 terms −¼G^a\_{μν}G^{aμν}, |D\_μH₅|² and ψ̄iγ^μD\_μψ each contain at most one time derivative per field, so (S1) holds term by term and gate **F-S24.19 is CLOSED by inspection** (S24-C21).

**On (R1).** Proposition S24.3a excludes homogeneous linear coefficient maps. It does not exclude every equivariant construction — functions of holonomies, composites of transporters and gauge-covariant non-linear maps remain possible. The holonomy map is the **canonical exact equivariant choice**, not a unique one (S24-C15, NC-S24.8).

**On (R2).** It asserts no positivity; positivity is (R2⁺), which §4.6b then realises. There is no circularity.

## §4.5 What the product complex forces — and what it does not

> **Theorem S24.7.** For K × ℤ: **(a)** 2-cells are spatial, f × {t}, or temporal, e × \[t, t+1\]; **(b)** every temporal 2-cell carries exactly one spatial edge *(C138)*; **(c)** every **individual** plaquette variable is supported on at most two consecutive slices *(C157)*; **(d)** under **(L)** and **(T)** the one-step kernel factorises over edges and the generator is a sum of single-edge central operators — exactly τ\_eΔ\_e for a heat-kernel s\_e, class **K1** *(C145)*, or class **K1\*** for a Bernstein φ\_e (Theorem S24.11).

**Two inferences that do not follow.** **S24-R9.** From (b) it does **not** follow that the temporal action is edge-additive: Σ\_{e≠e′} c\_{ee′} Re tr(U\_{0e}) Re tr(U\_{0e′}) is real, continuous, gauge invariant and supported on temporal plaquettes without being additive. **S24-R11.** From (c) it does **not** follow that the *action* is one-step in time: S \= Σ\_t Re tr(U\_{p,t})·Re tr(U\_{q,t+5}) is assembled from two-slice variables and is non-Markov, violating the three-slice conditional-independence test by O(1) *(negative control C158)*.

Both are the same error — reading cell **support** as a constraint on the **functional form** of the action — and it is registered permanently as gate **F-S24.20**.

**\[STATUS: (a)–(c) PROVEN; (d) PROVEN-CONDITIONAL on (L) ∧ (T) — M207.\]**

## §4.5b Theorem S24.12 — where time-locality actually comes from

> **Theorem S24.12 (Slab decomposition).** Assume **(R1)**, **(S1)** and **(S2)**. Then  
>   
> **Z \= ∫ Π\_t dU\_t Π\_t K(U\_t, U\_{t+1}),  K(U\_t, U\_{t+1}) \= ∫ dμ\_slab(W\_t) e^{−S\_t(U\_t, W\_t, U\_{t+1})},**  
>   
> with each K real, continuous, gauge invariant, and symmetric if the continuum action is time-reflection symmetric. Hypothesis **(T)** therefore holds and a one-step transfer operator exists.

**Proof.** Under (R1) a spatial link at slice t is the holonomy of a path in K × {t}; a temporal link is the holonomy of a path in {v} × \[t, t+1\]; a temporal plaquette holonomy is the ordered product around ∂(e × \[t, t+1\]). **Every configuration variable is therefore slice- or slab-supported** *(C138, C157)*. Write the slab variables as U\_t, U\_{t+1} (bounding slices) and W\_t (temporal links and interior profiles). By (S1) the action is ∫dt∫\_K ℒ with ℒ local and of first derivative order in time, so ∫dt \= Σ\_t∫\_t^{t+1} and the integrand on the slab \[t, t+1\] is determined by the connection restricted to that slab, hence by (U\_t, W\_t, U\_{t+1}) after reduction: **S \= Σ\_t S\_t(U\_t, W\_t, U\_{t+1})**. By (S2) the measure factorises over slabs, so the W\_t integrals may be performed slab by slab, giving the displayed product. Reality, continuity and gauge invariance survive the integration because dμ\_slab is gauge invariant and the integrand is; symmetry follows from that of ℒ under time reflection.

**\[STATUS: PROVEN-CONDITIONAL on (R1) ∧ (S1) ∧ (S2) — M213.\]**

**What (S2) is doing, and why v1.5 was incomplete.** ZS-S24 v1.5 passed directly from "each variable is slab-supported" to "S\_step depends on the two bounding slices". That skips the slab interior. A slab carries temporal links and interior connection profiles which are *not* determined by U\_t and U\_{t+1}; they must be integrated out, and the integration is legitimate slab-by-slab only if the reduction measure factorises. (S2) is the explicit statement of that, and it is structural — a property of how the reduction is defined, not of any coefficient. Gate **F-S24.21** records it.

**What this buys.** The external reviews identified the arrow *ZS-S14 ⇒ a one-step transfer action* as the missing first link of the bridge. Theorem S24.12 supplies it from a property ZS-S14 manifestly has. No κ\_p, no measure selection and no orbit weight enters. What it does not supply is positivity — that is §4.6b.

## §4.6 Theorem S24.9 — the two-tier transfer-matrix gap

> **Theorem S24.9.** Assume (R1), (R2) and **(T)**, so S \= Σ\_t S\_step(U\_t, U\_{t+1}) with S\_step real, continuous, gauge invariant, symmetric. Let 𝒦(U, U′) \= exp(−½S\_mag(U) − S\_step(U, U′) − ½S\_mag(U′)) and (Tψ)(U) \= ∫𝒦(U, U′)ψ(U′)dU′.  
>   
> **Tier (i).** **(a)** 𝒦 is continuous on the compact **M** × **M**, so T is Hilbert–Schmidt, hence compact with discrete spectrum; **(b)** 𝒦 is symmetric, so T is self-adjoint; **(c)** 𝒦 is the exponential of a finite real number, hence **pointwise strictly positive**, so T is positivity improving; **(d)** T commutes with every U(h); **(e)** by Perron–Frobenius ‖T‖ is a simple eigenvalue t₀ with a strictly positive — hence gauge-invariant — eigenvector, and |λ| \< t₀ for every other spectral value; **(f)** hence **log(t₀/|t₁^phys|) \> 0**. **Tier (ii).** If in addition **(R2⁺)** holds, **H \= −log T** is self-adjoint and bounded below and **Δ\_phys \= log(t₀/t₁^phys) ∈ (0, ∞)**.

**Proof.** (a) A continuous kernel on a compact measure space is square integrable. (b) Time-reflection symmetry. (c) exp of a real continuous function on a compact space is bounded away from zero. (d) Invariance of 𝒦 and of Haar measure. (e) Reed–Simon XIII.44 \[10\]; compactness makes ‖T‖ an eigenvalue, and −‖T‖ is not one for a positivity-improving operator; strict positivity of ψ₀ with uniqueness forces U(h)ψ₀ \= ψ₀. (f) Discreteness. Tier (ii): positivity gives a spectral logarithm, injectivity keeps t₁^phys \> 0\.

**\[STATUS: tier (i) PROVEN under (R1) ∧ (R2) ∧ (T); tier (ii) PROVEN-CONDITIONAL on (R2⁺) — M208. This is the Osterwalder–Seiler / Lüscher construction \[4\], \[17\] on the Z-Spin carrier.\]**

**Controls fixing the hypothesis boundaries.** **C155**: a deliberately non-additive action whose kernel is *not* a positive operator (minimum eigenvalue ≈ −22) still yields a simple top eigenvalue, a strictly positive eigenvector and |t₁|/t₀ ≈ 0.44 — tier (i) uses neither (L) nor (R2⁺). **C156**: a pointwise positive but rank-deficient kernel has t₁ ≈ 10^{−14}, so −log T does not exist. **C160**: Σ\_α c\_α f\_α(x)f\_α(y) is positive for c\_α ≥ 0 but injective only for c\_α \> 0 — which is why (R2⁺) names injectivity (S24-C18).

## §4.6b Theorem S24.14 — a canonical symmetric reflection-positive slab realisation

Tier (ii) needed (R2⁺) from somewhere. Importing it from the Wilson action would presuppose that ZS-S14 reduces to Wilson's form, which the corpus has not proved — ZS-S21 carries the orbit-blind Wilson reduction as the postulate Z-A1, not as a theorem. The alternative is to *build* a reflection-positive slab operator out of what the corpus already owns.

> **Theorem S24.14 (Canonical symmetric reflection-positive slab realisation).** Let L be self-adjoint and non-negative on L²(**M**) satisfying **(E)** and **(G)** — for instance the Friedrichs operator of Theorem S24.2′ — and let V ∈ C(**M**, ℝ) be gauge invariant. For a \> 0 define  
>   
> **T\_a \= e^{−aV/2} e^{−aL} e^{−aV/2}.**  
>   
> Then, with **S \= e^{−aL/2} e^{−aV/2}**: **(a) Positivity and injectivity.** T\_a \= S\*S, so ⟨ψ, T\_aψ⟩ \= ‖Sψ‖² ≥ 0; and e^{−aV/2} is multiplication by a function bounded above and below by positive constants, while e^{−aL} is injective by the spectral theorem, so S is injective and **⟨ψ, T\_aψ⟩ \> 0 for every ψ ≠ 0**. Hence **(R2⁺) holds**. **(b) Gauge commutation.** \[L, U(h)\] \= 0 and V gauge invariant give \[e^{−aL}, U(h)\] \= \[e^{−aV/2}, U(h)\] \= 0, so **\[T\_a, U(h)\] \= 0** and ℋ\_phys is preserved. **(c) Compactness and kernel.** e^{−aL} is trace class on the compact **M**, so T\_a is compact, with continuous kernel **K\_a(U, U′) \= e^{−aV(U)/2} p\_a^L(U, U′) e^{−aV(U′)/2}**, symmetric and **strictly positive** because p\_a^L \> 0 by (E). Hence T\_a is positivity improving and Theorem S24.9 applies to it at **both** tiers. **(d) Reflection positivity by construction.** The multi-slab measure with density Π\_t K\_a(U\_t, U\_{t+1}) is reflection positive about any slice: reflection pairing produces Π of S\*S blocks, and ⟨F, ΘF⟩ \= ‖(Π S)F‖² ≥ 0\. **(e) Trotter–Kato.** For a \= t/n, T\_{t/n}^n \= (e^{−tV/2n}e^{−tL/n}e^{−tV/2n})^n → e^{−t(L+V)} by the symmetric Trotter product formula \[40\], \[41\], L \+ V being self-adjoint by Kato–Rellich. Because V is **bounded** and L has **compact resolvent**, the convergence holds in operator norm for each fixed t \> 0; norm convergence of a compact semigroup implies convergence of each of its finitely many largest eigenvalues, hence **Δ\_a := −(1/a) log(t₁^phys/t₀) → Δ\_phys(L \+ V) \> 0**. Independently, **Δ\_a \> 0 for every a \> 0** by (a)–(c) and Theorem S24.9(ii), so no limit is needed for positivity.  
>   
> **(f) Coupling-scaled form.** Matching H\_g \= g²L \+ g^{−2}V, the family is  
>   
> **T\_{a,g} \= e^{−ag^{−2}V/2} e^{−ag²L} e^{−ag^{−2}V/2},**  
>   
> and (a)–(e) hold verbatim with L → g²L and V → g^{−2}V, for every g \> 0 and every slab spacing a \> 0\.

**Proof.** (a) The factorisation is immediate since e^{−aV/2} is self-adjoint and e^{−aL} \= (e^{−aL/2})²; injectivity of a product of injective operators. (b) Functions of commuting operators. (c) Peter–Weyl for trace-class heat semigroups on a compact group, Gaussian bounds for p\_a^L from uniform ellipticity, and boundedness of V. (d) Direct computation of the reflection pairing. (e) Symmetric Trotter with a bounded perturbation, and continuity of the finitely many lowest eigenvalues.

**\[STATUS: PROVEN — M215; checks C163 (S\*S factorisation exact, minimum eigenvalue 2.97 × 10^{−1} \> 0), C165 (gauge commutation inherited), C164 (spectral error 1.18 × 10^{−1} → 1.36 × 10^{−4} with successive ratios 8.9, 8.8, 11.1). C164 is a finite-dimensional confirmation: the O(a²) behaviour it exhibits is *not* claimed as a universal infinite-dimensional rate, which would require commutator regularity or semigroup norm estimates beyond what is proved here. Gate F-S24.23.\]**

**What this closes and what it does not.** It closes the question *whether a reflection-positive one-step slab realisation of the Z-Spin finite reduction exists*: one does, canonically, built from the corpus's own kinetic operator and potential, with no appeal to Wilson. The honest declaration is therefore

> **The ZS-S14 finite reduction admits a canonical symmetric reflection-positive semigroup realisation, and on that realisation the physical Hamiltonian gap is strictly positive for every slab spacing a \> 0 and every coupling g \> 0, converging as a → 0 to the gap of L \+ V.**

"Canonical symmetric" rather than "canonical": T\_a is the *symmetric* splitting of the pair (L, V), which is the natural and reflection-symmetric choice, but other reflection-positive realisations of the same pair exist (S24-C23).

It does **not** prove that integrating the ZS-S14 master action over one temporal slab *returns* T\_a for some a. That identification is gate **F-S24.18**, and it is now a comparison between two explicitly written operators rather than an open-ended question about which action to adopt.

## §4.7 The closure, tier by tier

| conclusion | hypotheses | status |
| ----- | ----- | ----- |
| every configuration variable is slice- or slab-supported | (R1) | **PROVEN** *(C138, C157)* |
| cell support ⇏ edge-additivity; cell time-support ⇏ time-locality | — | **PROVEN** *(C158)*; S24-R9, S24-R11 |
| one-step transfer representation, hypothesis (T) | (R1) ∧ (S1) ∧ (S2) | **PROVEN**, Theorem S24.12 |
| correlation-decay gap log(t₀/|t₁^phys|) \> 0 | \+ (RS) | **PROVEN**, Theorem S24.9(i) |
| Hamiltonian gap Δ\_phys ∈ (0, ∞) | \+ (R2⁺) | **PROVEN**, Theorem S24.9(ii) |
| **(R2⁺) is realisable canonically** | (E) ∧ (G) ∧ V bounded | **PROVEN**, Theorem S24.14 |
| edge-diagonal generator, K1 or K1\* | \+ (L) | **PROVEN**, Theorem S24.7(d), Theorem S24.11 |
| the exact ZS-S14 slab action equals T\_a for some a, or is otherwise reflection positive | — | **OPEN — F-S24.18** |
| the exact ZS-S14 slab action is edge-additive | — | **OPEN — F-S24.14** (tier iii only) |
| the reduction measure factorises over slabs (S2) | — | **OPEN — F-S24.21**, structural |

**Gate F-S24.12 is CLOSED** under (R1) ∧ (S1) ∧ (S2) ∧ (RS), and tier (ii) is closed on the canonical realisation of Theorem S24.14. Nothing in the argument uses κ\_p, σ, ρ, the Hodge measure, single-plaquette locality, or the identity of K.

**Honest terminal wording.** *ZS-S24 closes the finite-carrier action-to-gap theorem under an explicitly time-local canonical holonomy reduction, and exhibits a canonical reflection-positive slab realisation on which the Hamiltonian gap is strictly positive. Identification of the exact ZS-S14 slab action with that realisation remains outside the theorem and is registered as F-S24.18.* No unconditional ZS-S14 → Hamiltonian-gap closure is claimed.

---

# §5. Theorem S24.4 — the Exact Electric-Limit Spectrum

Take K \= K\_TI **(C-K)**, a uniform electric metric **(C-U)**, and tier (iii), hence **(T)** ∧ **(L)** — writing an electric Hamiltonian presupposes a one-step edge-additive temporal sector. Then in the gauge-invariant spin-network basis

**H\_E \= (g²/2) Σ\_e C₂(R\_e),**

diagonal, with states labelled by an irrep per link and an intertwiner per vertex.

**Four facts.** **(F1)** Gauss law: a vertex with exactly one non-trivial link carries no singlet, since dim Inv(R) \= 0 for R non-trivial, so every non-vacuum support has minimum degree two and therefore contains a cycle *(C110)*. **(F2)** Along a two-valent chain dim Inv(R ⊗ R̄) \= 1 and dim Inv(R ⊗ R) \= 0, so the irrep is constant and the orientation alternates *(C111, C112)*. **(F3)** girth(K\_TI) \= 5, with 12 simple 5-cycles, 20 simple 6-cycles and no 7-cycles *(C103–C106)*. **(F4)** C₂(p,q) \= (p² \+ q² \+ pq \+ 3p \+ 3q)/3 has minimum 4/3 over non-trivial irreps, attained only on **3** and **3̄**; the next values are C₂(**8**) \= 3 and C₂(**6**) \= 10/3 *(C107–C109)*.

**Provenance.** In v1.1 (F1) and (F2) rested on Weyl integration alone. They are now cross-checked against the closed-form decompositions **3**⊗**3̄** \= **1**⊕**8**, **3**⊗**3** \= **3̄**⊕**6**, **3**^{⊗3} \= **1**⊕**8**⊕**8**⊕**10**, **3**⊗**8** \= **3**⊕**6̄**⊕**15**, **8**⊗**8** \= **1**⊕**8**⊕**8**⊕**10**⊕**10̄**⊕**27**, each verified by exact dimension count *(C140–C144)*.

> **Theorem S24.4.** Under (C-K) ∧ (C-U) ∧ (T) ∧ (L), the two lowest non-vacuum eigenvalues of H\_E and their exact degeneracies are  
>   
> **Δ\_{E,1} \= (10/3) g², d₁ \= 24;  Δ\_{E,2} \= 4 g², d₂ \= 40;  Δ\_{E,2}/Δ\_{E,1} \= 6/5.**

**Proof.** By (F1) every non-vacuum support contains a cycle, hence at least girth \= 5 links; by (F2) the irrep is constant along it; by (F4) the cheapest is **3** or **3̄**, giving (g²/2)·5·(4/3) \= (10/3)g², attained by the 12 pentagons in two orientations, so d₁ \= 24\. The next support is a 6-cycle, giving 4g² and d₂ \= 20 × 2 \= 40\. Competitors are excluded exhaustively: a pentagon in any higher irrep costs at least (g²/2)·5·3 \= 7.5g² \> 4g²; a mixed pentagon with four **3** links and one **8** is forbidden by dim Inv(**3**⊗**8**) \= 0 and would in any case cost 25/6 g² \> 4g²; 7-link supports do not exist on K\_TI and 8-link supports cost at least (g²/2)·8·(4/3) \= 16/3 g² \> 4g² *(C115–C123)*.

**\[STATUS: PROVEN-CONDITIONAL on (C-K) ∧ (C-U) ∧ (T) ∧ (L). Electric-limit values only; the finite-g claim of ZS-S22 v1.2 is retracted as S24-R1.\]**

> **Proposition S24.4′ (weighted, diagonal case).** For class **K1** with weights a\_e \> 0, Δ\_{E,1} \= (g²/2)(4/3)·min{Σ\_{e∈C} a\_e : C a cycle}, the **minimum-weight cycle**, with eigenspace spanned by the minimising cycles in **3** and **3̄**. **\[PROVEN; gate F-S24.8\]**

**Withdrawal.** The v1.1 two-sided bound for a non-diagonal coefficient matrix is **retracted (S24-R5)**: it neglected non-vanishing cross-term expectations on the loop states, and by Proposition S24.2b it was stated for an operator that is not gauge invariant. The admissible off-diagonal case (K2, K3) is **OPEN**.

---

# §6. Strong Coupling

## §6.1 Theorem S24.5 — leading asymptotics

> **Theorem S24.5.** Write H/g² \= H\_E^{(0)} \+ g^{−4}V\_B with ‖V\_B‖ ≤ B. Weyl's perturbation inequality gives |E\_k(H/g²) − E\_k(H\_E^{(0)})| ≤ g^{−4}B for every k, hence  
>   
> **Δ(g) \= (10/3) g² \+ O(g^{−2}),  |Δ(g) − (10/3)g²| ≤ 2Bg^{−2}.**  
>   
> **Corollary S24.5a.** In units of g² the electric levels are 0, 10/3, 4, so the binding spacing is **4 − 10/3 \= 2/3**, not the vacuum-to-first spacing 10/3. Two clusters approach by at most 2Bg^{−4}, so ordering is preserved once **g⁴ \> 3B**, and with a one-third margin once **g⁴ \> 9B**.

**\[STATUS: PROVEN-CONDITIONAL on (C-K) ∧ (C-U) — M203. The v1.1 threshold compared the perturbation with the wrong spacing and is corrected as S24-C5.\]**

## §6.2 Proposition S24.15′ — the first-order structure of the 24-fold level

Theorem S24.5 bounds the error but says nothing about how the 24-fold degeneracy actually moves. It reduces, for **any** admissible magnetic term, to twelve independent 2 × 2 Hermitian blocks.

> **Proposition S24.15′.** Let P₁ project onto the 24-dimensional first electric eigenspace of K\_TI, spanned by the 12 pentagon loops in **3** and **3̄**. Let V\_B \= Σ\_f Φ\_f with each Φ\_f a **real class function** of the plaquette holonomy, character expansion Φ\_f \= Σ\_R a\_R^{(f)}χ\_R, weights depending only on face type. Reality of Φ means **a\_{R̄} \= conj(a\_R)**; it does *not* make the coefficients real. Then  
>   
> **(i)** every **non-trivial** character component of a plaquette f ≠ C has vanishing matrix elements within P₁; the **trivial** components act as the identity and contribute only a common scalar; **(ii)** for f \= C the diagonal receives only R \= **1** and R \= **8** and is **the same on |C, 3⟩ and |C, 3̄⟩**; the orientation-flip element receives only R \= **3** and R \= **6̄**; **(iii)** hence, with **c₀ \= Σ\_f a\_1^{(f)} \+ a\_8^{(5)}** and **μ \= a\_3^{(5)} \+ a\_6̄^{(5)}**,  
>   
> **P₁V\_BP₁ \= c₀P₁ \+ Σ\_C \[ μ |C, 3̄⟩⟨C, 3| \+ conj(μ) |C, 3⟩⟨C, 3̄| \],**  
>   
> block-diagonal with 12 identical Hermitian blocks **c₀I \+ Re(μ)σ\_x \+ Im(μ)σ\_y**; **(iv)** its spectrum is **c₀ ± |μ|**, each 12-fold, with eigenvectors **|C, ±⟩ \= (|C, 3⟩ ± e^{i arg μ}|C, 3̄⟩)/√2**. The level therefore splits **24 → 12 ⊕ 12 if and only if μ ≠ 0**; (v) the vacuum first-order shift is ν₀ \= Σ\_f a\_1\*\*^{(f)}, while the lower first-excited branch has shift ν₁ \= c₀ − |μ| \= Σ\_f a\_1^{(f)} \+ a\_8^{(5)} − |μ|\*\*. Therefore  
>   
> Δ(g) \= (10/3)g² \+ \[a\_8\*\*^{(5)} − |μ|\]g^{−2} \+ O(g^{−6}), g → ∞.\*\*  
>   
> The displacement of each branch from c₀ is |μ| and the branch separation is 2|μ|; neither is, by itself, the physical-gap correction; **(vi)** each 12-dimensional sector carries the permutation representation **A ⊕ T₁ ⊕ T₂ ⊕ H** (dimensions 1 \+ 3 \+ 3 \+ 5\) of the **rotational icosahedral group I ≅ A₅**, so it splits no further than into four I multiplets.  
>   
> **When the blocks are σ\_x.** If the action is **charge-conjugation-even**, Φ(U^{−1}) \= Φ(U), then a\_{R̄} \= a\_R, which with a\_{R̄} \= conj(a\_R) forces **μ ∈ ℝ**; the block is pure σ\_x and the eigenvectors are the orientation-even and orientation-odd combinations. The fundamental Wilson form Φ\_f \= κ\_f\[1 − ⅓ Re tr U\_f\] is such an action, with a\_**3** \= a\_**3̄** \= −κ\_f/6, a\_**6̄** \= 0, hence **μ \= −κ₅/6**.

**Proof.** The matrix element of a plaquette character between loop states is ⟨C′, R′|χ\_R(U\_f)|C, R″⟩ \= ∫ conj(χ\_{R′})χ\_Rχ\_{R″}, so the bra enters through its **conjugate** and the multiplicity is dim Inv(R̄′ ⊗ R ⊗ R″).

*(i)* For R trivial, χ\_**1** \= 1 and the operator is the identity, contributing a\_**1**^{(f)} to every diagonal entry — this is why the claim that *every* f ≠ C term annihilates P₁ would be false *(C174)*. For R non-trivial, acting with χ\_R(U\_f) assigns R to every edge of ∂f \\ C. Exhaustively, |∂f \\ C| ≥ 5 over all 384 (pentagon, face) pairs *(C171)*, so those edges carry R itself and a target in P₁ forces R ∈ {**3**, **3̄**}. For that case the target support satisfies **C △ ∂f ⊆ S ⊆ C ∪ ∂f**, and |C △ ∂f| ≥ 9 \> 5 for every f ≠ C *(C161, C167)*, so |S| ≥ 9 and no target is a 5-cycle.

*(ii)* For f \= C the two entries are

**⟨C, 3|χ\_R|C, 3⟩ \= dim Inv(3̄ ⊗ R ⊗ 3\) \= mult(R̄, 3̄ ⊗ 3),  3̄ ⊗ 3 \= 1 ⊕ 8;** **⟨C, 3̄|χ\_R|C, 3⟩ \= dim Inv(3 ⊗ R ⊗ 3\) \= mult(R̄, 3 ⊗ 3),  3 ⊗ 3 \= 6 ⊕ 3̄.**

These two closed-form decompositions **prove** the selection rules for *all* irreps: the diagonal is non-zero exactly for R̄ ∈ {**1**, **8**}, i.e. R ∈ {**1**, **8**}, and the flip exactly for R̄ ∈ {**6**, **3̄**}, i.e. R ∈ {**6̄**, **3**}. Conjugating everything shows the diagonal takes the same value on |C, 3̄⟩ as on |C, 3⟩. Check **C170** confirms both rules over p, q ≤ 3; it is a confirmation, not the proof. The fundamental case is the character identity **χ\_3(U\_C)² \= χ\_6(U\_C) \+ χ\_3̄(U\_C)**, giving ⟨C, **3̄**|Re tr U\_C|C, **3**⟩ \= ½ and vanishing diagonal *(C166)*.

*(iii)* Collecting: the diagonal is a multiple of the identity on P₁ and cannot lift any degeneracy; the flip in one direction carries μ and, by hermiticity of V\_B, the reverse carries conj(μ). (iv) The block c₀I \+ Re(μ)σ\_x \+ Im(μ)σ\_y has eigenvalues c₀ ± |μ| with the stated eigenvectors, all twelve pentagons being equivalent under I. (v) Put ε \= g^{−4} in H/g² \= H\_E \+ εV\_B. For the electric vacuum |Ω⟩, character orthogonality gives ν₀ \= ⟨Ω|V\_B|Ω⟩ \= Σ\_f a\_1\*\*^{(f)}. The lower branch of the first electric cluster has ν₁ \= c₀ − |μ| \= Σ\_f a\_1^{(f)} \+ a\_8^{(5)} − |μ|. Hence the gap of H/g² is 10/3 \+ ε\[a\_8\*\*^{(5)} − |μ|\] \+ O(ε²), and multiplication by g² gives the stated O(g^{−6}) remainder. The O(ε²) expansion follows from bounded perturbation theory for the isolated first electric cluster, whose unperturbed separation from the next cluster is 2/3. (vi) The 12 pentagon centroids are equidistant from the origin with exactly five nearest neighbours each, hence the vertices of an icosahedron (C168); the 12-vertex permutation character of I is (12, 2, 2, 0, 0\) on the classes (E, 12C₅, 12C₅², 20C₃, 15C₂), whose inner products with the irreducible characters give multiplicity 1 for A, T₁, T₂ and H and 0 for G (C169).

**\[STATUS: PROVEN-CONDITIONAL on (C-K) ∧ (C-U) ∧ (T) ∧ (L) — M216. No hypothesis on the *form* of the magnetic class function is used, only reality and I-symmetry of the weights.\]**

> **Why the coefficients need not be real (S24-C27).** ZS-S24 v1.8 wrote the projected operator as c₀P₁ \+ μΣ\_Cσ\_x^{(C)} with μ real. That is wrong for a general real class function: SU(3) characters are complex, and reality of Φ imposes only a\_{R̄} \= conj(a\_R). The function **Φ(U) \= i\[χ\_3(U) − χ\_3̄(U)\]** is real-valued, since χ\_3̄ \= conj(χ\_3), yet has a\_**3** \= i, μ \= i, and projected block exactly **σ\_y** *(negative control C172)*. The v1.8 eigenvectors (|C, 3⟩ ± |C, 3̄⟩)/√2 are then not eigenvectors at all. The Hermitian form above is the correct general statement, and it reduces to v1.8's whenever the action is charge-conjugation-even *(C173)*.

**What this costs and what it buys.** The projected first electric cluster still consists of two 12-fold branches at c₀ ± |μ|, distinct if and only if μ ≠ 0\. The displacement of each branch from the cluster centre is |μ| and the full branch separation is 2|μ|. The physical-gap correction is different because the vacuum receives the common trivial-character shift: it is a\_8\*\*^{(5)} − |μ|, not |μ| alone. For the Wilson form a\_8\*\*^{(5)} \= 0 and |μ| \= κ₅/6, so for κ₅ \> 0,

Δ(g) \= (10/3)g² − (κ₅/6)g^{−2} \+ O(g^{−6}).

The block structure is fixed by SU(3) representation theory and the girth-5 geometry; the two value inputs a\_8^{(5)} and μ remain outputs of the ZS-S23 face-and-prism integration (gate F-S23.6).

> **Retraction S24-R12 (against ZS-S24 v1.6).** The v1.6 Proposition S24.15 asserted that the first eigenspace is not split by the magnetic term, and inferred an error estimate three powers sharper than Weyl's. Both are **RETRACTED.** The error was in the bra: check C162 evaluated dim Inv(**3̄**⊗**3**⊗**3**) \= 0, which is the **diagonal** element and does vanish, and treated it as if it settled the whole block. The orientation-flip element uses dim Inv(**3**⊗**3**⊗**3**) \= 1 — already in the companion as C113 — and equals 1/2. Check **C162 is withdrawn**.

**Still open.** The second-order effective Hamiltonian P₁V\_B(E₁ − H\_E)^{−1}V\_BP₁, which contributes at O(g^{−6}) and would resolve each 12-dimensional sector into its A ⊕ T₁ ⊕ T₂ ⊕ H multiplets, is a well-posed finite computation and is not attempted here (**gate F-S24.10**). The parity refinement under the full icosahedral group I\_h is separately a **NON-CLAIM (NC-S24.14).**

---

# §7. Proposition S24.6 — the Weak-Coupling Gauge-Singlet Gap

> **Proposition S24.6.** In the weak-coupling limit: **(a)** maximal-tree gauge fixing removes 8(V − 1\) of the 8E link degrees of freedom, leaving 8(E − V \+ 1\) \= 8 × 31 \= **248 tree-gauge-fixed link variables** on K\_TI — not physical variables, since the residual global SU(3) quotient is taken only at step (f); **(b)** flat connections on a simply connected carrier form a single gauge orbit, and H¹(S²) \= 0 removes non-gauge zero modes; **(c)** the Hessian about the vacuum is **L\_spatial ⊗ I\_adj**, so each normal mode carries an adjoint index; **(d)** the unprojected one-quantum frequency is √(rλ₁) with λ₁ \= 1.2428416164 the ZS-S21 eigenvalue and r a normalisation; **(e)** one quantum transforms in **8** under the residual global SU(3), and **dim Inv(8) \= 0** *(C129)*, so it is not a physical state; **(f)** the lowest invariant polynomial in the adjoint oscillators is quadratic, since **dim Inv(8 ⊗ 8\) \= 1** *(C130)*; hence the leading gauge-singlet candidate is  
>   
> **Δ\_weak → 2√(rλ₁).**

**\[STATUS: DERIVED-CONDITIONAL on (C-W). Anharmonic corrections, tunnelling between Gribov copies, the action-level determination of r, and possible level reordering are all OPEN (F-S24.3, F-S24.9). √(rλ₁) is retained only as the *unprojected normal-mode frequency*, never as a gap; S24-C1, S24-R2. ZS-S7 uses λ₁ linearly, so the factor of two does not propagate to m(0⁺⁺) \= 1.791 GeV.\]**

---

# §8. Terminal Bridge Ledger

| object | status |
| ----- | ----- |
| gap existence for uniformly elliptic, gauge-commuting L and bounded gauge-invariant V | **CLOSED — PROVEN** (§3.2) |
| the criterion for (G), and K1/K2/K3 as sufficient certificates | **CLOSED — PROVEN** (§3.4) |
| independence of (E) and (G), both directions | **CLOSED — PROVEN**, C133, C137 |
| Friedrichs construction for U-dependent coefficients | **CLOSED — PROVEN**, Theorem S24.2′ |
| no homogeneous linear reduction is equivariant; holonomy reduction is | **CLOSED — PROVEN**, §4.2 |
| product complex ⇒ edge-additive action | **RETRACTED (S24-R9)** |
| product complex ⇒ time-local action | **RETRACTED (S24-R11)** |
| one-step transfer representation (T) | **CLOSED — PROVEN** from (R1) ∧ (S1) ∧ (S2), Theorem S24.12 |
| correlation-decay gap | **CLOSED — PROVEN**, Theorem S24.9(i) |
| Hamiltonian gap given (R2⁺) | **CLOSED — PROVEN**, Theorem S24.9(ii) |
| **a canonical reflection-positive slab realisation exists, with Δ\_phys \> 0 for every a \> 0** | **CLOSED — PROVEN**, Theorem S24.14 |
| **P₁V\_BP₁ reduces to 12 Hermitian 2 × 2 blocks with spectrum c₀ ± |μ|, μ \= a₃ \+ a\_6̄; the level splits 24 → 12 ⊕ 12 iff μ ≠ 0; after vacuum subtraction, Δ(g) \= (10/3)g² \+ \[a₈^{(5)} − |μ|\]g^{−2} \+ O(g^{−6})** | **CLOSED — PROVEN**, Proposition S24.15′ |
| σ\_x form and orientation-even/odd eigenvectors | **CLOSED — PROVEN** for charge-conjugation-even actions, including Wilson (μ \= −κ₅/6) |
| the v1.6 claim P₁V\_BP₁ \= zero and its O(g^{−6}) estimate | **RETRACTED (S24-R12)** — bra not conjugated |
| content of each 12-fold level under the rotational group I: A ⊕ T₁ ⊕ T₂ ⊕ H | **CLOSED — PROVEN**, C168, C169; the I\_h parity refinement is **NON-CLAIM** NC-S24.14 |
| strong-coupling leading coefficient (10/3)g², d₁ \= 24; ratio 6/5, d₂ \= 40 | **CLOSED — PROVEN-CONDITIONAL** on (C-K) ∧ (C-U) |
| weighted diagonal (K1) generalisation: minimum-weight cycle | **CLOSED — PROVEN** |
| weak-coupling singlet coefficient 2√(rλ₁) | **DERIVED-CONDITIONAL**; anharmonic and tunnelling control **OPEN** |
| identity of the carrier; measure and orbit weights; exact κ\_p | needed for **value only**; κ\_p still **OPEN** (F-S23.6) |
| single-plaquette locality (H-W) | **not needed at all** for existence |
| exact ZS-S14 slab action \= T\_a, or otherwise reflection positive | **OPEN — F-S24.18** |
| exact ZS-S14 slab action edge-additive | **OPEN — F-S24.14** (tier iii only) |
| slab factorisation of the reduction measure (S2) | **OPEN — F-S24.21**, structural |
| first electric gap for an admissible off-diagonal operator | **OPEN**; the v1.1 bound is retracted (S24-R5) |
| the full finite-g function Δ(g); second-order I-multiplet resolution; full I\_h parity refinement | **OPEN / NON-CLAIM —** separate finite problems |
| Clay 3+1D Yang–Mills mass gap | **NON-CLAIM**, F-S24.1 |

**Reading.** Relative to v1.5, hypothesis (R2⁺) moves from *assumed* to *constructed*: Theorem S24.14 exhibits a canonical reflection-positive slab family built from the corpus's own kinetic operator, so the Hamiltonian tier no longer waits on an identification with Wilson. Theorem S24.12 gains the slab-interior integration it was missing, at the cost of the explicit structural hypothesis (S2). Relative to v1.6 the strong-coupling sharpening is **withdrawn** and replaced by a determination of the first-order eigenstructure; relative to v1.7 that determination is **widened** to every real magnetic class function, and relative to v1.8 it is **corrected to Hermitian form**, the character coefficients of a real class function being complex in general. The projected operator has spectrum c₀ ± |μ|, so the level splits 24 → 12 ⊕ 12 if and only if μ ≠ 0; after subtracting the vacuum shift, the first physical-gap correction is a\_8^{(5)} − |μ| and the next unresolved term is O(g^{−6}); the residual content of each sector under the rotational icosahedral group is A ⊕ T₁ ⊕ T₂ ⊕ H. One gate closes by inspection (F-S24.19) and three open (F-S24.21, F-S24.22, F-S24.23).

**One sentence.** *Because the master Lagrangian carries no time derivative beyond first order, the holonomy reduction of the Z-Spin carrier has an exact one-step transfer representation; its kernel is pointwise positive, so a correlation-decay gap follows; and the corpus's own kinetic operator generates a canonical reflection-positive slab family on which the Hamiltonian gap is strictly positive — leaving only the identification of the exact ZS-S14 slab action with that family.*

---

# §9. Gates, Retractions, Corrections, Non-Claims

## §9.1 Falsification gates

Classes: **M** mathematical collapse (immediate rejection); **S** simulation or internal-consistency collapse (revision); **O** observational collapse.

| gate | fires if | class | status |
| ----- | ----- | :---: | ----- |
| **F-S24.1** | Theorem S24.1 or S24.2 is presented as bearing on the Clay problem | M | **OPEN, permanent** |
| **F-S24.2** | a gauge-invariant electric state on K\_TI is found below (10/3)g² | S | **OPEN** |
| **F-S24.3** | a controlled semiclassical analysis shows the singlet gap does not approach 2√(rλ₁) | M | **OPEN** |
| **F-S24.4** | Rayleigh–Ritz / Temple–Lehmann bracketing fails to bound Δ(g) from zero for an operator satisfying (E) ∧ (G) | S | **OPEN** |
| **F-S24.5** | the magnetic term derived from ZS-S14 is unbounded | M | **OPEN** |
| **F-S24.6** | Δ\_phys \> 0 is cited without stating which hypotheses of Corollary S24.3 are assumed | M | **OPEN, permanent** |
| **F-S24.7** | the ZS-S14 Galerkin basis is linearly dependent | M | **OPEN**; control C125 is the fail-closed test |
| **F-S24.8** | exact integration returns a non-uniform or non-diagonal kinetic matrix | S | **OPEN, expected live**; replaces girth 5 by a minimum-weight cycle, and requires class K2 or K3 for admissibility |
| **F-S24.9** | a singlet-projected weak-coupling computation returns √(rλ₁) | S | **OPEN** |
| **F-S24.10** | under the hypotheses of Proposition S24.15′, a controlled strong-coupling calculation returns a g^{−2} gap coefficient different from a\_8^{(5)} − |μ| | M | **OPEN;** firing would refute the vacuum-subtracted first-order calculation. The second-order effective Hamiltonian contributes at O(g^{−6}) and resolves the I multiplets | |
| **F-S24.22** | any paper reports a matrix element ⟨R′|χ\_f|R⟩ as a multiplicity without conjugating the bra | M | **OPEN, permanent.** Registered because this error produced S24-R12 while every companion check passed; the correct object is dim Inv(R̄′ ⊗ f ⊗ R) |
| **F-S24.25** | a version declares a repair to its companion that is not present in the shipped source | S | **OPEN, permanent.** Registered after v1.8 declared five repairs and applied two; enforced by gate X313, which scans the companion for every string the manuscript claims to have removed |
| **F-S24.24** | a Version History entry names a companion file or hash belonging to a different version | S | **OPEN, permanent — now ENFORCED by gate X314.** Recurred three times during version preparation, each time through a global substitution; the archived entries are part of the retraction record and must survive editing |
| **F-S24.23** | a universal infinite-dimensional convergence *rate* is claimed for the Trotter step of Theorem S24.14 on the strength of a finite-dimensional control | S | **OPEN, permanent**; C164 is a confirmation, not a rate theorem |
| **F-S24.11** | a companion ships a claim string the manuscript retracts | S | **OPEN, permanent**; gates X300–X310 |
| **F-S24.12** | the reduced kinetic operator fails **(E)** or **(G)** | M | **CLOSED** under (R1) ∧ (S1) ∧ (S2) ∧ (RS) |
| **F-S24.13** | an executable-check count is reported without its evidential-weight breakdown, or a control is cited as evidence for a value | S | **OPEN, permanent** |
| **F-S24.14** | the exact ZS-S14 slab action is not edge-additive | M | **OPEN**; tier (iii) only |
| **F-S24.15** | K1/K2/K3 are presented as an exhaustive classification, or Corollary S24.3 is invoked without naming the reduction | M | **OPEN, permanent**; gates X306, X307 |
| **F-S24.16** | a positivity claim about a convolution or subordinated kernel rests on a truncated character series | S | **OPEN, permanent**; control C154 |
| **F-S24.17** | a printed count disagrees with the run-time ledger, or a declared line count with the file | S | **OPEN, permanent**; gate X308 |
| **F-S24.18** | the exact ZS-S14 slab action is neither equal to some T\_a nor otherwise reflection positive with a non-degenerate form | M | **OPEN — the residue of tier (ii).** Does not affect tier (i), and does not affect the canonical realisation of Theorem S24.14 |
| **F-S24.19** | the ZS-S14 Lagrangian contains time derivatives beyond first order or a non-local time kernel | M | **CLOSED by inspection**: −¼G^a\_{μν}G^{aμν}, |D\_μH₅|², ψ̄iγ^μD\_μψ each carry at most one time derivative per field |
| **F-S24.20** | any paper infers a property of the **action** from the **support** of the cells or variables it is built from | M | **OPEN, permanent**; committed twice (S24-R9, S24-R11); controls C158, C159 |
| **F-S24.21** | the reduction measure does not factorise over time slabs, so **(S2)** fails | M | **OPEN**; would void the slab-by-slab integration in Theorem S24.12 |

## §9.2 Retractions

| id | against | content |
| ----- | ----- | ----- |
| **S24-R1** | ZS-S22 v1.2 | (10/3)g², 4g², 6/5 as *exact finite-g* values, and the ratio as experimentally testable. They are **electric-limit** values under (C-K) ∧ (C-U), falsifiable by computation, not experiment. |
| **S24-R2** | ZS-S22 v1.2 | λ₁ as *the weak-coupling limit of the finite-carrier gap*. §7 gives 2√(rλ₁). |
| **S24-R3** | ZS-S22 v1.2 | the claim that the chain through the Hodge measure was closed. §4 closes a different and weaker chain that avoids the measure. |
| **S24-R4** | ZS-S24 v1.0 | the v1.0 companion, a partially renamed ZS-S22 regression script whose declarations contradicted the manuscript's own retractions. **WITHDRAWN.** |
| **S24-R5** | ZS-S24 v1.1 | the two-sided bound on Δ\_{E,1} for a non-diagonal coefficient matrix: it neglected cross-term expectations and was posed on an operator failing (G). |
| **S24-R6** | ZS-S24 v1.1 | that a symmetric positive definite edge coupling implies local gauge invariance. False for non-abelian G; Proposition S24.2b is the counterexample. The functional-analytic content survives under (E) ∧ (G). |
| **S24-R7** | ZS-S24 v1.1 companion | C127 (sampling replaced by the analytic declaration M206) and C131 (the tautology |2.0 − 2.0| \< 10^{−12}, deleted); C124 and C126 relabelled. |
| **S24-R8** | ZS-S24 v1.2 | that the three templates exhausted the gauge-commuting constructions. No completeness theorem holds; Proposition S24.2d is the criterion. |
| **S24-R9** | ZS-S24 v1.3 | that a product complex forces an edge-additive temporal action. Cell support does not constrain the functional form of the action. |
| **S24-R10** | ZS-S24 v1.3 | the classification of the Wilson action as class K1\*. Positive coefficients do not make the generator a Bernstein function of the Casimir alone. |
| **S24-R11** | ZS-S24 v1.4 | that a product complex forces a time-local action. Same error as S24-R9, one level up; control C158. |
| **S24-R12** | ZS-S24 v1.6 | Proposition S24.15, the vanishing of P₁V\_BP₁, and the O(g^{−6}) error estimate that followed. The bra was not conjugated: v1.6's C162 evaluated the diagonal element, which does vanish, and treated it as the whole block. The orientation-flip element is 1/2, by **3** ⊗ **3** \= **3̄** ⊕ **6**. Check **C162 is withdrawn**; M216 is replaced by Proposition S24.15′. |

## §9.3 Corrections

**S24-C1** weak-coupling representative √(rλ₁) → 2√(rλ₁). **S24-C2** "Φ\_f central" → "real-valued continuous class function"; "E₁" → "E₁^phys"; Trotter → Feynman–Kac. **S24-C3** strong-coupling CANDIDATE → PROVEN-CONDITIONAL. **S24-C4** the v1.0 "bracket" title withdrawn, no Rayleigh–Ritz or Temple–Lehmann bound having been constructed. **S24-C5** ordering threshold compared with the binding spacing 2/3, giving g⁴ \> 3B and g⁴ \> 9B. **S24-C6, S24-C7** C124, C126 relabelled as controls on generic vectors. **S24-C8** every check carries an evidential weight. **S24-C9** "exhaust" → "sufficient certificates"; F-S24.12 restated as (E) and (G). **S24-C10** K3 transporter direction and cocycle convention unified between manuscript and companion. **S24-C11** the K3 operator defined by Friedrichs extension rather than by "symmetrised". **S24-C12** 248 relabelled tree-gauge-fixed link variables. **S24-C13** four finite checks relabelled CONFIRMATION. **S24-C14** all printed counts reconciled with the run-time ledger; gate X308. **S24-C15** "the only available choice" → "the canonical exact equivariant choice". **S24-C16** tier (ii) hypothesis strengthened to injectivity. **S24-C17** positivity removed from (R2) and isolated as (R2⁺), removing the circularity with its own gate. **S24-C18** (R2⁺) restated at operator level, coefficient positivity demoted to a sufficient certificate for the class-function family. **S24-C19** C138, C157 stopped printing retracted propositions; X302 now tests the current header. **S24-C20** (new) four residual statements still carried superseded hypotheses — the companion's tier-(ii) declaration and closing summary, the last row of Table 4.1, the Terminal Ledger's description of (R1), and the §3.5 restriction of admissibility to the three templates. All corrected; gate **X310** fails on their wording. **S24-C21** (new) (S1) restated as *no time derivatives beyond first order* rather than "first order in ∂\_t", the Yang–Mills density being quadratic in ∂\_tA\_i; gate F-S24.19 closed by inspection. **S24-C27** (new) the projected magnetic operator restated in Hermitian form c₀P₁ \+ Σ\_C\[μ|C, 3̄⟩⟨C, 3| \+ conj(μ)|C, 3⟩⟨C, 3̄|\], since a real class function has a\_{R̄} \= conj(a\_R) and not real coefficients; the σ\_x form holds for charge-conjugation-even actions only (control C172, C173). **S24-C28** (new) "every f ≠ C term annihilates P₁" corrected to "every non-trivial character component of a plaquette f ≠ C", the trivial component acting as the identity (C174). **S24-C29** (new) C170 re-weighted from exhaustive to **confirmation**: it scans p, q ≤ 3, whereas the selection rules are proved for all irreps by **3̄**⊗**3** \= **1**⊕**8** and **3**⊗**3** \= **6**⊕**3̄**. **S24-C30** (new) three of the five companion repairs declared by v1.8 had not in fact been applied — M205, M207 and M215; all are applied here, and gate X313 now verifies every declared repair against the shipped source. **S24-C24** every icosahedral statement attributed to the **rotational** group I ≅ A₅, whose order-60 character table is what check C169 actually uses; the full I\_h parity decomposition becomes NC-S24.14, and gate X312 fails on the loose wording in either file. **S24-C25** (new) five stale companion declarations repaired: the \[S14\] section header, which still printed the retracted title; M207, which omitted (T); M213 and M214, which derived (T) without (S2); M205, which still closed F-S24.12 by the Theorem S24.7 route retracted as S24-R9; and the X310 message, which still named the retracted proposition. Also the docstring's "one of three weights" → four, and C161's message narrowed to f ≠ C. **S24-C26** (new) Proposition S24.15′ was stated in v1.7 for an arbitrary real class function but proved only for the Wilson form; the gap is closed by proving the general statement (C170, C171), not by narrowing the hypothesis. **S24-C23** Theorem S24.14's universal O(a²) rate withdrawn — C164 is a finite-dimensional control — with eigenvalue convergence justified instead by norm convergence of a compact semigroup, the coupling-scaled family T\_{a,g} written out, and "canonical" softened to "canonical symmetric choice". **S24-C22** C159 re-weighted from closed-form to **control**: it tested a deliberately factorised scalar model, hence the factorisation identity and the test itself, not Theorem S24.12.  
**S24-C31** (completion) the first-excited cluster shift c₀ − |μ| is distinguished from the physical-gap shift by subtracting the vacuum contribution Σ\_f a\_**1**^{(f)}; the resulting coefficient is a\_**8**^{(5)} − |μ| and the remainder is O(g^{−6}). Abstract, §6.2, Terminal Ledger, Conclusion and M216 are synchronised. 

## §9.4 Consistency discipline

Five distinct failure modes have now been seen in this line, and each has a standing gate. A hash may match a file that does not match the paper (v1.0; X300–X303). Every check may pass while the load-bearing hypothesis goes unexamined (v1.1; the negative controls C133, C137 and gate F-S24.13). A count may drift between manuscript and companion (v1.3; X308). A companion check may **assert a proposition the manuscript has retracted** and still report PASS, because its message text is not compared against the retraction register (v1.4; X309, which scans both files). And a gate may be satisfied by the document's own history rather than by its current claims (v1.4; X302 now tests the header line). Underlying two of the retractions is a single reasoning error, inferring a property of the action from the support of the cells, now gate **F-S24.20**. A sixth mode appeared in v1.6 and is the sharpest of all: **manuscript and companion may agree perfectly and both be wrong**, if they share the same incorrect formula. C162 and M216 used the same unconjugated contraction, so every gate passed while the headline result was false. The remedy is not another consistency gate but a *cross-check against an independently computed quantity* — here the companion's own C113, dim Inv(**3**⊗**3**⊗**3**) \= 1, which contradicted C162 the moment the two were placed side by side. Gate **F-S24.22**. A seventh mode is editorial rather than mathematical and has now recurred twice: a **global string substitution while preparing a new version rewrites the archived Version History**, so that an earlier release appears to have shipped the current companion. Both instances were caught by re-reading the history against the file names, and it recurred a third time while preparing this version, which is why **F-S24.24 is no longer a declared discipline but an executable one**: gate **X314** parses the Version History and fails if any entry names a companion belonging to a different version. A discipline that has failed three times should not be enforced by prose. An eighth mode is the most embarrassing and the most instructive: **a version may declare a repair that never happened.** ZS-S24 v1.8 §1.3 listed five stale companion declarations as repaired; three of the substitutions silently failed to match and shipped unchanged, while the manuscript asserted otherwise. Prose about what was fixed is not evidence that it was fixed. Gate **X313** now scans the shipped companion source for every string the current version claims to have removed, so that the claim and the artefact cannot diverge. Gate **F-S24.25**.

## §9.5 Non-claims

**NC-S24.1** nothing about ℝ⁴, the continuum limit, renormalisation or the Clay problem. **NC-S24.2** the SU(3) spectrum is not computed; Theorem S24.4 gives two levels of a diagonal operator. **NC-S24.3** the two coupling ends are not two limits of a *computed* function. **NC-S24.4** no numerical constant is derived, predicted or fitted. **NC-S24.5** no claim about the physical mass unit; converting Δ\_phys to MeV needs the ZS-S17 scale bridge. **NC-S24.6** gauge equivariance of the Z-Spin reduction is a consequence of the declaration (R1), not a theorem about the ZS-S14 action. **NC-S24.7** K1, K2, K3 do not classify the gauge-commuting operators. **NC-S24.8** the holonomy map is not claimed unique among equivariant reductions. **NC-S24.9** the correlation-decay gap of tier (i) is not a Hamiltonian spectral gap without tier (ii). **NC-S24.10** the exact ZS-S14 slab action is not identified, integrated, or shown reflection positive; Theorem S24.14 constructs *a* canonical realisation and does not claim ZS-S14 reduces to it. **NC-S24.11** the product complex constrains the support of the variables and nothing else. **NC-S24.12** the second-order effective Hamiltonian on the 24-dimensional space, and the resolution of each 12-fold level into its A ⊕ T₁ ⊕ T₂ ⊕ H multiplets, are not computed. **NC-S24.15** (new) no claim that μ ≠ 0 for the physical magnetic term; whether the ZS-S14 slab action has a non-vanishing **3** or **6̄** component is part of gate F-S23.6. **NC-S24.14** the decomposition A ⊕ T₁ ⊕ T₂ ⊕ H is established for the **rotational** icosahedral group I only; no parity refinement under the full group I\_h is computed or claimed. **NC-S24.13** no infinite-dimensional convergence *rate* is claimed for the Trotter step of Theorem S24.14, and T\_a is not claimed to be the unique reflection-positive realisation of (L, V).

---

# §10. Zero-Free-Parameter and Anti-Numerology Audit

**Table 10.1.** Every symbol carrying a number.

| symbol | provenance | free? |
| ----- | ----- | ----- |
| A \= 35/437, Q \= 11, dim Z \= 2 | inherited LOCKED, ZS-F0 and ZS-M1; **not used** in any theorem of §3–§4 | **no** |
| λ₁ \= 1.2428416164, λ\_h \= 7.5210904061 | inherited LOCKED, ZS-S21; enter only §7 | **no** |
| V \= 60, E \= 90, F \= 32, girth 5, 12 pentagons, 20 hexagons | combinatorics of K\_TI, recomputed from exact coordinates in Appendix B | **no** |
| 4/3, 3, 10/3 | C₂(p,q) at (1,0), (1,1), (2,0) | **no** |
| 10/3, 4, 6/5, 24, 40 | products of the two rows above | **no** |
| 2/3 \= 4 − 10/3; thresholds 3B, 9B | differences of those levels; B is a symbolic operator norm | **no** |
| the factor 2 in 2√(rλ₁) | dim Inv(**8**) \= 0, dim Inv(**8**⊗**8**) \= 1 | **no** |
| r | ZS-S21 normalisation, carried symbolically, never given a value | **no** |
| a, the slab spacing | a free *parameter of the construction* in Theorem S24.14, not of the theory; every a \> 0 gives a positive gap and the a → 0 limit is the Hamiltonian gap | **no** |

**Anti-numerology.** A Monte-Carlo test asks how often a random re-derivation reproduces a *measured* quantity by chance. This paper contacts no measured quantity: 10/3, 6/5, 24 and 40 are integers and small rationals fixed by girth, Casimir and cycle census, each independently recomputed in the companion, and 2√(rλ₁) is not a number until r is supplied elsewhere. The test is therefore **NOT-APPLICABLE with stated reason**, not pending. The structural falsifiers that replace it are F-S24.2 (a lower electric state), F-S24.8 (non-uniform integration), F-S24.10 (a mismatch in the derived g^{−2} coefficient), F-S24.12 (failure of (E) or (G)) and F-S24.20 (support-to-action inference). **\[STATUS: declaration\]**

---

# §11. Conclusion

**What v1.6 got wrong.** Manuscript and companion agreed perfectly, all 88 entries passed, and the headline strong-coupling result was false, because both encoded the same unconjugated contraction. The check that refuted it — dim Inv(**3**⊗**3**⊗**3**) \= 1 — was already in the companion as C113. No consistency gate can catch this; only cross-checking a claim against an independently computed quantity can, which is now gate F-S24.22.

**A repeated error, and what removed it.** Two versions of this paper inferred a property of the *action* from the *support* of the cells it is built from — first edge-additivity, then time-locality. Both passed a full companion run. Both are retracted with executable negative controls attached, and the pattern is now a standing gate. What replaced the second is a theorem: time-locality follows from the **derivative order of the Lagrangian**. The ZS-S14 terms carry no time derivative beyond first order, so under the holonomy reduction every variable lives in one slab, the time integral splits, and — after integrating the slab interior against a slab-factorised measure — the partition function is an exact one-step transfer product.

**The constructive step.** Tier (ii) previously waited on reflection positivity of an action the corpus had not identified. It no longer does. The corpus already owns a self-adjoint non-negative gauge-commuting L and a bounded gauge-invariant V, and the symmetric splitting **T\_a \= e^{−aV/2}e^{−aL}e^{−aV/2} \= S\*S** is positive, injective, compact, positivity improving, gauge-commuting, reflection positive by construction, and Trotter-convergent to L \+ V. So the Z-Spin finite reduction **admits a canonical reflection-positive symmetric-semigroup realisation**, with a strictly positive Hamiltonian gap at every slab spacing.

**The first excited level, resolved.** v1.6 claimed the 24-fold level was untouched at first order because it omitted conjugation of the bra in dim Inv(R̄′ ⊗ f ⊗ R). The corrected general result is Hermitian: non-trivial components of plaquettes f ≠ C vanish within P₁, while trivial components give a common scalar; the pentagon's own plaquette produces twelve blocks c₀I \+ Re(μ)σ\_x \+ Im(μ)σ\_y with spectrum c₀ ± |μ|. Thus the level splits 24 → 12 ⊕ 12 if and only if μ ≠ 0; the branch separation is 2|μ|. After subtracting the electric-vacuum shift, the physical gap is

**Δ(g) \= (10/3)g² \+ \[a\_**8\*\*^{(5)} − |μ|\]g^{−2} \+ O(g^{−6}).\*\*

For the Wilson form μ \= −κ₅/6 and a\_**8**^{(5)} \= 0, so the correction is −κ₅g^{−2}/6 for κ₅ \> 0\. Each 12-dimensional sector carries A ⊕ T₁ ⊕ T₂ ⊕ H under the rotational icosahedral group I ≅ A₅; the full I\_h parity refinement is not claimed.

**What is left.** One identification: whether integrating the ZS-S14 master action over a slab returns a member of the canonical family, gate F-S24.18. It is now a comparison of two explicitly written operators. Beside it sit the full finite-g function Δ(g), the O(g^{−6}) second-order I-multiplet resolution, and the separate full-I\_h parity refinement. 

> **ZS-S24 closes the finite-carrier action-to-gap theorem under an explicitly time-local canonical holonomy reduction, and exhibits a canonical reflection-positive slab realisation carrying a strictly positive Hamiltonian gap. Identification of the exact ZS-S14 slab action with that realisation remains outside the theorem and is registered as F-S24.18.**

No unconditional ZS-S14 → Hamiltonian-gap closure is claimed, and none should be quoted from this paper.

---

# Acknowledgements and Code Availability

This version responds to an external review of ZS-S24 v1.5, which observed that Theorem S24.12 omitted the slab-interior variables and the measure factorisation, that C159 tested a deliberately factorised model rather than the theorem, that (S1) was misphrased and its gate needlessly left open, that four residual statements still carried superseded hypotheses, and — most usefully — that the constructive route T\_a \= e^{−aV/2}e^{−aL}e^{−aV/2} was available and had not been taken. Theorem S24.14 is that route. Earlier versions responded to reviews of v1.4 through v1.0. Errors that remain are the author's.

The companion zs\_s24\_verify\_v1\_9.py (1319 lines, Python 3, NumPy only) reconstructs the carrier from exact vertex coordinates; computes cycle censuses and the pentagon–face incidence by exhaustive enumeration; computes SU(3) singlet multiplicities by Weyl integration and cross-checks them against closed-form tensor decompositions; evaluates the Ad-covariance algebra with two negative controls; computes the Peter–Weyl spectrum of the Wilson temporal kernel across four decades of β; tests complete monotonicity by a truncation-free criterion; runs the three-slice conditional-independence test separating cell support from action locality; verifies the S\*S factorisation, positivity, injectivity, gauge commutation and finite-dimensional Trotter behaviour of the canonical symmetric slab family; verifies the corrected orientation-flip matrix element, the pentagon–face exclusion, the icosahedral geometry of the pentagon centroids and their decomposition under the rotational icosahedral group I; and runs fifteen static consistency gates, including a numerical self-consistency gate and a retracted-proposition gate that scans both files. It performs **no** Hamiltonian diagonalisation and claims **no** numerical verification of Theorems S24.1, S24.2, S24.2′, S24.3′, S24.7, S24.9, S24.11, S24.12, S24.13 or S24.14, of Lemma S24.10, or of Proposition S24.15′, all of which appear in its ledger as math-theorem blocks. SHA256: 6876ed2b7d388494d67b6da28857480c0bb20184ba9c2e325b0a10525d67ee4c.

---

# Appendix A. Verification Ledger

**Table A.1.** Executable checks. *CF* closed-form, *EX* exhaustive, *CT* control, *CN* confirmation. All PASS.

| id | w | content |
| ----- | :---: | ----- |
| C100–C102 | CF | V \= 60, E \= 90, 3-regular primal skeleton of K\_TI |
| C103–C106 | EX | girth 5; 12 simple 5-cycles; 20 simple 6-cycles; no 7-cycles |
| C107–C109 | CF/EX | C₂(**3**) \= 4/3; C₂(**8**) \= 3; minimal non-trivial Casimir 4/3 attained only on **3**, **3̄** |
| C110–C114 | CF | dim Inv of **3**; **3**⊗**3̄**; **3**⊗**3**; **3**^{⊗3}; **3**⊗**8** |
| C115–C119 | CF | Δ\_{E,1} \= (10/3)g²; Δ\_{E,2} \= 4g²; ratio 6/5; d₁ \= 24; d₂ \= 40 |
| C120–C123 | EX/CF | exhaustive exclusion of higher irreps on a pentagon, and of 7- and 8-link supports |
| C124–C126 | CT | Gram positivity on **generic** vectors; linear dependence as the failure mode; off-diagonal entries with gauge admissibility untested |
| C129–C130 | CF | dim Inv(**8**) \= 0; dim Inv(**8**⊗**8**) \= 1 |
| C132, C134 | CF | Ad : SU(3) → SO(8) orthogonal (class K1); links sharing a target rotate together (class K2) |
| C133 | CT | **negative:** Ad(h)ᵀAd(h′) ≠ I for distinct targets — refutes the v1.1 hypothesis |
| C135–C136 | CF | transporter covariance Ad(h)Ad(h^{−1}Ph′)Ad(h′)ᵀ \= Ad(P); cocycle equivalence to A ⊗ I₈ |
| C137 | CT | **negative:** a non-cocycle family makes the twisted symbol indefinite for positive definite A |
| C138 | EX | 90 temporal 2-cells, one spatial edge each — **cell support only**, no additivity inferred |
| C140–C144 | CF | closed-form su(3) decompositions with exact dimension counts |
| C145–C148 | CF/CN | heat-kernel generator exactly τΔ; Wilson coefficients positive and non-increasing in C₂; kernel pointwise positive; kernel symmetric |
| C150 | CF | the Ad-equivariance condition is closed under composition and gauge-invariant combination |
| C151–C153 | CN | occurrence of (p,q) in **3**^{⊗p}⊗**3̄**^{⊗q}; Wilson positivity over β ∈ \[0.01, 60\]; complete monotonicity at four α |
| C154 | CT | **method control:** truncated character series give spurious negatives falling with the cutoff |
| C155–C156 | CT | tier (i) needs neither (L) nor (R2⁺); tier (ii) needs strict injectivity |
| C157 | EX | each plaquette variable spans ≤ 2 consecutive slices — **cell support only** |
| C158 | CT | **negative:** a t ↔ t+2 action violates one-step factorisation by O(1) |
| C159 | CT | **positive control:** a deliberately factorised scalar model satisfies the factorisation identity — it does not test Theorem S24.12 |
| C160 | CT | positivity for c\_α ≥ 0, injectivity only for c\_α \> 0 |
| C161 | EX | over all 384 (pentagon, face) pairs: shared edges ≤ 1, |C △ ∂f| ∈ {0, 9, 10, 11}; f \= C is a genuine exception |
| ~~C162~~ | — | **WITHDRAWN (S24-R12)** — contracted the bra without conjugation |
| C166 | CF | ⟨C, **3̄**|Re tr U\_C|C, **3**⟩ \= 1/2, diagonal 0, by **3**⊗**3** \= **3̄**⊕**6** — the f \= C plaquette acts as ½σ\_x |
| C167 | EX | |C △ ∂f| ≥ 9 \> 5 for every f ≠ C, and any target support contains C △ ∂f — all f ≠ C terms vanish |
| C168 | EX | the 12 pentagon centroids are equidistant with 5 nearest neighbours each: an icosahedron |
| C169 | CF | the 12-vertex permutation representation of the **rotational** group I ≅ A₅ decomposes as A ⊕ T₁ ⊕ T₂ ⊕ H, with G absent |
| C170 | CN | confirms over p, q ≤ 3 the selection rules proved from **3̄**⊗**3** \= **1**⊕**8** and **3**⊗**3** \= **6**⊕**3̄**: diagonal only for R \= **1**, **8**, equal on both orientations; flip only for R \= **3**, **6̄** |
| C172 | CT | **negative:** Φ \= i\[χ\_**3** − χ\_**3̄**\] is real-valued yet gives μ \= i and a **σ\_y** block — a real class function need not have real coefficients |
| C173 | CF | charge-conjugation-even ⇒ μ ∈ ℝ ⇒ pure σ\_x; Wilson gives μ \= −κ/6 |
| C174 | CT | **negative:** the trivial character of a plaquette f ≠ C acts as the identity, so it does not annihilate P₁ |
| C171 | EX | |∂f \\ C| ≥ 5 for every f ≠ C, so those edges carry the loop irrep itself — the f ≠ C exclusion holds for any class function |
| C163, C165 | CF | T\_a \= S\*S with strictly positive spectrum; gauge commutation inherited from (G) |
| C164 | CN | −(1/a)log T\_a → L \+ V at the O(a²) symmetric-Trotter rate |

Weight totals: **36 CF \+ 14 EX \+ 13 CT \+ 6 CN \= 69**.

**Table A.2.** Math-theorem blocks — declarations; proofs in the manuscript, **no numerical PASS claimed**.

| id | theorem | id | theorem |
| ----- | ----- | ----- | ----- |
| M200 | Theorem S24.1 | M208 | Theorem S24.9, two tiers |
| M201 | Theorem S24.2, (E) ∧ (G) | M209 | Proposition S24.3a |
| M202 | Corollary S24.3 | M210 | Theorem S24.2′, Friedrichs |
| M203 | Theorem S24.5 and Corollary S24.5a | M211 | Lemma S24.10 |
| M204 | NON-CLAIM on the Clay problem | M212 | Theorem S24.11, K1\*; Wilson excluded |
| M205 | Theorem S24.3′, holonomy equivariance | M213 | Theorem S24.12, slab decomposition |
| M206 | analytic boundedness of the magnetic term | M214 | Theorem S24.13, assembled bridge |
| M207 | Theorem S24.7, support and adjacency only | M215 | **Theorem S24.14, canonical RP slab** |
|  |  | M216 | **Proposition S24.15′, Hermitian first-order block and vacuum-subtracted gap correction**  |

**Table A.3.** Consistency gates. All PASS.

| id | content |
| :---- | :---- |
| X300, X301 | companion free of inherited ZS-S22 claim strings; no finite-g quantity advertised as exact |
| X302 | manuscript declares all v1.9 objects and carries the current header |
| X303 | no v1.0/v1.1 stale claim strings |
| X304 | both hypotheses of Theorem S24.2 stated literally |
| X305 | the equivariance gate, the negative result and S24-R6 registered |
| X306 | the canonical reduction, the transfer-matrix theorem and the residual gate declared |
| X307 | K1/K2/K3 nowhere presented as an exhaustive classification |
| X308 | every printed count matches the run-time ledger, including the companion's line count |
| X309 | neither file asserts a retracted locality proposition; the slab-decomposition objects are declared |
| X310 | no v1.5 stale hypothesis wording; Theorem S24.14, Proposition S24.15′ and F-S24.19 declared |
| X311 | no v1.6 first-order-splitting claim survives; S24-R12, Proposition S24.15′, T\_{a,g} and σ\_x declared |
| X312 | the icosahedral statement is attributed to the rotational group I in **both** files; S24-C24 and (S2) declared |
| X313 | every companion repair this version declares is present in the shipped source, and the manuscript states the Hermitian form |
| X314 | every Version History entry names its own companion file |

Ledger totals: **69 C \+ 16 M \+ 15 X \= 100 entries, 0 FAIL.**

---

# Appendix B. Independent Carrier Reconstruction

The companion imports no carrier from any prior Z-Spin file. It generates the 60 vertices as the even permutations of (0, ±1, ±3φ), (±2, ±(1 \+ 2φ), ±φ) and (±1, ±(2 \+ φ), ±2φ) with φ the golden ratio, joins pairs at minimal separation, and verifies V \= 60, E \= 90 and 3-regularity before any cycle counting. The face list used in Proposition S24.15 is the set of simple 5- and 6-cycles found by the same enumeration.

# Appendix C. Singlet Multiplicities: Two Routes

**Weyl integration.** dim Inv(R₁ ⊗ ⋯ ⊗ R\_k) \= ∫ Πχ\_{R\_i} dU on the maximal torus with density |Δ(z)|²/6, characters by the Weyl formula with l \= (p \+ q \+ 2, q \+ 1, 0). The integrand is a trigonometric polynomial, so a uniform product grid is exact; the grid is shifted off the Weyl walls to avoid a 0/0 evaluation.

**Closed-form decomposition.** The same multiplicities follow from the su(3) tensor products of §5, each confirmed by an exact dimension count using dim(p,q) \= (p+1)(q+1)(p+q+2)/2. Where §5 to §7 rely on a multiplicity, the closed-form route is the authority and the integration is the cross-check.

# Appendix D. Evidential Weight

The banner reports "69 executable checks (36 closed-form, 14 exhaustive, 13 control, 6 confirmation)" rather than a bare count, because the v1.1 error survived a run in which every entry passed.

- **Closed-form**: an identity exact in exact arithmetic. Failure means a coding error.  
- **Exhaustive**: a complete search over a finite space; its strength is exactly the completeness of the enumeration, which the manuscript must argue (Appendix B, §5, §6.2).  
- **Control**: a test of whether a hypothesis is automatic. A passing *negative* control shows a hypothesis is not free. C133 and C137 exist to stop a future version repeating the v1.1 inference; C155, C156 and C160 place the tier boundaries; C154 is a control on *method*; C158 and C159 are the pair that separates cell support from action locality — and C159 is a control, not a proof, because it tests a deliberately factorised model (S24-C22).  
- **Confirmation**: a finite check of a statement proved over an infinite range — twelve values of β for a lemma valid at all β, four values of α for Bernstein's theorem, four values of a for a Trotter limit — the last of which exhibits O(a²) behaviour without establishing any infinite-dimensional rate (F-S24.23). It raises confidence that a proof was transcribed correctly. Citing one as a proof is the error this weight exists to prevent (F-S24.13). And v1.6 showed the residual danger that no weight can remove: a *closed-form* check is only as sound as the formula it encodes. C162 was closed-form, exact, and wrong (F-S24.22).

# References

\[1\] K. G. Wilson, "Confinement of quarks," *Phys. Rev. D* **10**, 2445 (1974). \[2\] J. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Phys. Rev. D* **11**, 395 (1975). \[3\] M. Creutz, *Quarks, Gluons and Lattices* (Cambridge University Press, Cambridge, 1983). \[4\] K. Osterwalder and E. Seiler, "Gauge field theories on a lattice," *Ann. Phys.* **110**, 440 (1978). \[5\] T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed. (Springer, Berlin, 1976). \[6\] M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, New York, 1978). \[7\] S. H. Christiansen and T. G. Halvorsen, "A gauge invariant discretization on simplicial grids of the Schrödinger eigenvalue problem in an electromagnetic field," *SIAM J. Numer. Anal.* **49**, 331 (2011). \[8\] T. G. Halvorsen and T. M. Sørensen, "Simplicial gauge theory and quantum gauge theory simulation," *Nucl. Phys. B* **854**, 166 (2012). \[9\] B. Simon, "Schrödinger semigroups," *Bull. Amer. Math. Soc.* **7**, 447 (1982). \[10\] M. Reed and B. Simon, *Methods of Modern Mathematical Physics IV*, Theorem XIII.44 (Perron–Frobenius for positivity-improving semigroups). \[11\] H. Weyl, "Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen," *Math. Ann.* **71**, 441 (1912). \[12\] R. Gilmore, *Lie Groups, Lie Algebras, and Some of Their Applications* (Wiley, New York, 1974). \[13\] C. Rovelli and L. Smolin, "Spin networks and quantum gravity," *Phys. Rev. D* **52**, 5743 (1995). \[14\] J. C. Baez, "Spin network states in gauge theory," *Adv. Math.* **117**, 253 (1996). \[15\] A. Ashtekar and J. Lewandowski, "Representation theory of analytic holonomy C\*-algebras," in *Knots and Quantum Gravity* (Oxford University Press, Oxford, 1994). \[16\] M. Lüscher and P. Weisz, "Definition and general properties of the transfer matrix in continuum limit improved lattice gauge theories," *Nucl. Phys. B* **240**, 349 (1984). \[17\] M. Lüscher, "Construction of a self-adjoint, strictly positive transfer matrix for Euclidean lattice gauge theories," *Commun. Math. Phys.* **54**, 283 (1977). \[18\] A. Jaffe and E. Witten, "Quantum Yang–Mills theory," in *The Millennium Prize Problems* (Clay Mathematics Institute, Cambridge MA, 2006). \[19\] I. Montvay and G. Münster, *Quantum Fields on a Lattice* (Cambridge University Press, Cambridge, 1994). \[20\] M. Goldberg, "A class of multi-symmetric polyhedra," *Tôhoku Math. J.* **43**, 104 (1937). \[21\] H. S. M. Coxeter, *Regular Polytopes*, 3rd ed. (Dover, New York, 1973). \[22\] A. Bossavit, *Computational Electromagnetism* (Academic Press, Boston, 1998). \[23\] D. N. Arnold, R. S. Falk and R. Winther, "Finite element exterior calculus," *Acta Numerica* **15**, 1 (2006). \[24\] H. Whitney, *Geometric Integration Theory* (Princeton University Press, Princeton, 1957). \[25\]–\[31\] K. Kang, ZS-S7, ZS-S14, ZS-S17, ZS-S20, ZS-S21, ZS-S22 v1.2, ZS-S23 v1.0 (Z-Spin Cosmology Collaboration, 2026). \[32\] K. Kang, *The Hodge–Dirac Complex of the Truncated Icosahedron*, ZS-M6 v1.0 (2026). \[33\] W. Fulton and J. Harris, *Representation Theory: A First Course*, GTM **129** (Springer, New York, 1991), Ch. 13\. \[34\] H. Georgi, *Lie Algebras in Particle Physics*, 2nd ed. (Westview, Boulder, 1999), Ch. 8\. \[35\] S. H. Christiansen and T. G. Halvorsen, "Discretizing the Maxwell–Klein–Gordon equation by the lattice gauge theory formalism," *IMA J. Numer. Anal.* **31**, 1 (2011). \[36\] A. Grigor'yan, *Heat Kernel and Analysis on Manifolds*, AMS/IP **47** (AMS, Providence, 2009), Ch. 7\. \[37\] I. Kolář, P. W. Michor and J. Slovák, *Natural Operations in Differential Geometry* (Springer, Berlin, 1993), Ch. 11\. \[38\] R. L. Schilling, R. Song and Z. Vondraček, *Bernstein Functions*, 2nd ed., de Gruyter Studies in Mathematics **37** (de Gruyter, Berlin, 2012), Ch. 3, 13\. \[39\] S. Bochner, *Harmonic Analysis and the Theory of Probability* (University of California Press, Berkeley, 1955), Ch. 4\. \[40\] H. F. Trotter, "On the product of semi-groups of operators," *Proc. Amer. Math. Soc.* **10**, 545 (1959). \[41\] T. Kato, "Trotter's product formula for an arbitrary pair of self-adjoint contraction semigroups," in *Topics in Functional Analysis*, Adv. Math. Suppl. Stud. **3** (Academic Press, New York, 1978), p. 185\.

---

# Version History

**v1.9 (July 2026): FINAL.** Response to external review of v1.8. The mathematical correction is **S24-C27**: the projected magnetic operator is Hermitian, not σ\_x. v1.8 generalised Proposition S24.15′ to arbitrary real class functions but retained a real coefficient; reality of Φ imposes only **a\_{R̄} \= conj(a\_R)**, and Φ \= i\[χ\_**3** − χ\_**3̄**\] is real-valued with a\_**3** \= i, projecting to **σ\_y** (**C172**). The correct form is P₁V\_BP₁ \= c₀P₁ \+ Σ\_C\[μ|C, 3̄⟩⟨C, 3| \+ conj(μ)|C, 3⟩⟨C, 3̄|\], spectrum c₀ ± |μ|, eigenvectors (|C, **3**⟩ ± e^{i arg μ}|C, **3̄**⟩)/√2; the σ\_x form is recovered exactly for **charge-conjugation-even** actions, Wilson included (**C173**). The splitting is stated throughout as 24 → 12 ⊕ 12 **if and only if μ ≠ 0**. Statement (i) is corrected: the trivial character of a distant plaquette acts as the identity, so only **non-trivial** components annihilate P₁ (**S24-C28**, **C174**). The proof's conjugation line is fixed to mult(R̄, **3**⊗**3**) with **3**⊗**3** \= **6**⊕**3̄**, and the two closed-form decompositions are made the authority for the selection rules, with **C170** re-weighted to **confirmation** over p, q ≤ 3 (**S24-C29**). Finally, three of the five companion repairs that v1.8 *declared* had not in fact been applied — M205 still closed F-S24.12 by the retracted Theorem S24.7 route, M207 still omitted (T), M215 still said "strong resolvent sense". All three are applied here, and new gate **X313** scans the shipped companion for every string the manuscript claims to have removed, making a failed repair a build failure (**S24-C30**, gate **F-S24.25**). New non-claim **NC-S24.15**. Companion zs\_s24\_verify\_v1\_9.py, 1319 lines, SHA256 6876ed2b7d388494d67b6da28857480c0bb20184ba9c2e325b0a10525d67ee4c; ledger 69 C \+ 16 M \+ 15 X \= 100 entries, 0 FAIL.

**v1.8 (July 2026): superseded.** Response to external review of v1.7, which recommended a scope-and-consistency patch. The scope defect was real: **Proposition S24.15′** was stated for an arbitrary real class function but proved only for the fundamental Wilson form, and the diagonal element does not vanish in general — ⟨C, **3**|χ\_**8**|C, **3**⟩ \= dim Inv(**3̄**⊗**8**⊗**3**) \= 1\. Rather than narrow the hypothesis, v1.8 **proves the general statement** (**S24-C26**): an exhaustive scan over all irreps shows the diagonal is non-zero only for R \= **1**, **8** and is *identical on both orientations*, hence a multiple of the identity on P₁, while only R \= **3**, **6̄** contribute to the orientation flip (**C170**); and |∂f \\ C| ≥ 5 for every f ≠ C makes the f ≠ C exclusion independent of the class function (**C171**). So **P₁V\_BP₁ \= c₀P₁ \+ μΣ\_Cσ\_x^{(C)}** with μ \= a₃ \+ a\_**6̄** for *every* admissible magnetic term, the Wilson form being μ \= −κ₅/6. The icosahedral statement is re-attributed to the **rotational** group I ≅ A₅, whose order-60 character table is what C169 uses; the full I\_h parity decomposition becomes **NC-S24.14** and new gate **X312** fails on the loose wording in either file (**S24-C24**). Five stale companion declarations are repaired — the \[S14\] header, M207 (missing (T)), M213 and M214 (missing (S2)), M205 (still closing F-S24.12 by the retracted Theorem S24.7 route), and the X310 message — together with the docstring weight count and C161's scope (**S24-C25**). Sections §1.3–§1.6 renumbered. Companion zs\_s24\_verify\_v1\_8.py, 1240 lines, SHA256 6876ed2b7d388494d67b6da28857480c0bb20184ba9c2e325b0a10525d67ee4c; ledger 66 C \+ 16 M \+ 13 X \= 95 entries, 0 FAIL.

**v1.7 (July 2026): superseded.** Response to external review of v1.6. The decisive change is **S24-R12**: the v1.6 Proposition S24.15, its claim that the magnetic term leaves the 24-dimensional first electric eigenspace unmoved at leading order, and the O(g^{−2})-beating error estimate that followed, are **retracted**. The matrix element of a plaquette character between loop states is ∫conj(χ\_{R′})χ\_fχ\_R \= dim Inv(R̄′ ⊗ f ⊗ R); v1.6's check C162 evaluated the *diagonal* element and treated it as the whole block. **Proposition S24.15′** replaces it: plaquettes f ≠ C still annihilate the level, since any target support contains C △ ∂f and |C △ ∂f| ≥ 9 \> 5 (**C161**, **C167**), but the pentagon's own plaquette acts as ½**σ\_x** in the orientation index because **3** ⊗ **3** \= **3̄** ⊕ **6** (**C166**), so the level splits at first order into two 12-fold multiplets |C, ±⟩, the error estimate reverts to Theorem S24.5's O(g^{−2}), and the coefficient is identified with the pentagon plaquette weight κ₅. The residual I\_h content of each level is **A ⊕ T₁ ⊕ T₂ ⊕ H**, the 12 pentagon centroids forming an icosahedron (**C168**, **C169**). Check **C162 is withdrawn**; new gate **X311** fails on the retracted wording, and new gate **F-S24.22** registers the general lesson. **Theorem S24.14** keeps its constructive content unchanged but its convergence statement is tightened (**S24-C23**): the universal O(a²) rate is withdrawn as a finite-dimensional control only (gate **F-S24.23**), eigenvalue convergence is justified by norm convergence of a compact semigroup, the coupling-scaled family **T\_{a,g}** is written out, and "canonical" is softened to "canonical symmetric choice". New non-claim **NC-S24.13**. Companion zs\_s24\_verify\_v1\_7.py, 1188 lines, SHA256 0cda1326b6e2984a072e565b5f67bd737a08f1eae5a98a3d4b4534da51989d83; ledger 64 C \+ 16 M \+ 12 X \= 92 entries, 0 FAIL.

**v1.6 (July 2026): superseded.** Response to external review of v1.5, which recommended taking the constructive route rather than leaving reflection positivity open. **Theorem S24.14** does so: for any L satisfying (E) ∧ (G) and any bounded gauge-invariant V, the slab family T\_a \= e^{−aV/2}e^{−aL}e^{−aV/2} \= S\*S is positive, injective, compact, positivity improving with a continuous strictly positive kernel, gauge-commuting, reflection positive by construction, and Trotter-convergent to L \+ V (**C163**, **C164**, **C165**). Hypothesis **(R2⁺)** is therefore realised canonically rather than imported from Wilson. **Theorem S24.12** is completed with the slab-interior integration K(U\_t, U\_{t+1}) \= ∫dμ\_slab(W\_t)e^{−S\_t}, under the new structural hypothesis **(S2)**, gate **F-S24.21**. **Proposition S24.15** claimed that P₁V\_BP₁ vanishes on the 24-dimensional first electric eigenspace and sharpened Theorem S24.5 accordingly — **both retracted in v1.7 as S24-R12**, the bra having been contracted without conjugation. **(S1)** is restated as *no time derivatives beyond first order*, since the Yang–Mills density is quadratic in ∂\_tA\_i, and gate **F-S24.19** is closed by inspection of the ZS-S14 terms (**S24-C21**). **C159** is re-weighted from closed-form to control (**S24-C22**). Four residual superseded hypotheses are corrected and policed by new gate **X310** (**S24-C20**). New non-claim **NC-S24.12**. The manuscript is compressed by roughly 40% with no theorem, gate, retraction or correction removed. Companion zs\_s24\_verify\_v1\_6.py, 1122 lines, SHA256 720b61e72d8ebae02639a8efddc8a9ba9495b77d35316722b1f526c5bb7a13ba; ledger 61 C \+ 16 M \+ 11 X \= 88 entries, 0 FAIL.

**v1.5 (July 2026): superseded.** Retracted the v1.4 inference from cell time-support to action time-locality (**S24-R11**, control C158, gate F-S24.20); derived temporal Markov locality from the Lagrangian instead (Theorem S24.12); restated (R2⁺) at operator level (S24-C18); assembled the chain as Theorem S24.13; corrected two companion checks that were printing retracted propositions and added gate X309 (S24-C19). Companion 984 lines; ledger 56 C \+ 14 M \+ 10 X \= 80 entries.

**v1.4 (July 2026): superseded.** Retracted the v1.3 inference from cell support to edge-additivity (**S24-R9**); restructured the closure into tiers (i)–(iii) and showed tier (i) needs neither additivity nor positive definiteness; strengthened tier (ii) to strict positive definiteness (S24-C16); excluded Wilson from K1\* (S24-R10); softened the uniqueness claim for the holonomy reduction (S24-C15); introduced the CONFIRMATION weight (S24-C13) and gate X308 (S24-C14). Companion 887 lines; ledger 53 C \+ 12 M \+ 9 X \= 74 entries.

**v1.3 (July 2026): superseded.** Adopted the canonical holonomy reduction (R1)–(R2), justified by Proposition S24.3a; proved Lemma S24.10 and Theorem S24.11; demoted K1/K2/K3 to sufficient certificates (S24-R8); defined the U-dependent operator by Friedrichs extension (S24-C11); unified the transporter convention (S24-C10). Companion 799 lines; ledger 50 C \+ 12 M \+ 8 X \= 70 entries.

**v1.2 (July 2026): superseded.** Retracted the v1.1 claim that positivity implies gauge commutation (**S24-R6**); re-hypothesised Theorem S24.2 on (E) and (G); corrected the strong-coupling threshold to g⁴ \> 3B (S24-C5); withdrew the off-diagonal bound (S24-R5). Companion 524 lines; ledger 40 C \+ 7 M \+ 6 X \= 53 entries.

**v1.1 (July 2026): superseded.** Introduced the general gap theorem and the action-to-gap corollary; promoted the electric-limit spectrum to a theorem with degeneracies 24 and 40; corrected the weak-coupling candidate to 2√(rλ₁); withdrew the v1.0 companion (S24-R4). Companion 372 lines; ledger 32 C \+ 5 M \+ 4 X \= 41 entries.

**v1.0 (July 2026): initial public release.** Split out of ZS-S22 v1.2 §21 on external recommendation; renumbering S22.14 → S24.1; retractions S24-R1 to S24-R3; gates F-S24.1 to F-S24.6.  
