# ZS-M71 v1.4.1 — The bandwidth cost of separable rotational references under charge and energy conservation

**Version:** 1.4.1 · English manuscript · 2026-09-13 KST
**Author:** human authorship and final responsibility rest with the project owner; AI assistance is disclosed in Appendix C.
**Output role:** SUPPORT / METHOD · **Output form:** research paper · **PAPER QUALIFICATION:** PASS
**RESEARCH GRADE:** 3 · **CANDIDATE GRADE:** NONE · **TARGET GRADE:** 4 (not attained) · **qualified-human anchor:** NONE

The main result is T-SBC in §7.5. Sections 2–6 develop the calibrated absorptive detector that motivates it; §7 states and proves the joint and separable bandwidth laws; §8 fixes the operational scope and falsifiers; §9 compares the result with the nearest prior work. A companion verifier reproduces every finite computation and table in this paper (Appendix B); it certifies finite instances, not the universal statements, which are proved by hand. Version 1.4.1 adds the separable-reference comparison of §9.1.2, aligns the novelty wording of §9.2 with §9.3 and corrects three internal cross-references; no theorem, proof, numerical table or verification row is changed.

## Abstract

We study the discrimination of zero-Hamiltonian qubit states $|\pm x\rangle$ with a rotor of charge $M$ and energy $\Delta M^2$, and a neutral compensator with levels $0,\Delta,\ldots,N\Delta$. Measurement effects conserve total charge and bare total energy. At the same bandwidth, with the same permitted effects and a fixed physical rotor–compensator split, the optimal joint total variation is $\mathcal D_N^{\rm all}=\cos[\pi/(2\lfloor\sqrt N\rfloor+2)]$. A stationary curved-shell state attains it. Every finite $N\ge1$ has a strict separability gap, and we prove $N(1-\mathcal D_N^{\rm sep})\to\pi$, $N(1-\mathcal D_N^{\rm all})\to\pi^2/8$ and the error ratio $8/\pi$. The same limits hold with the common additional mean rotor-energy budget $\langle M^2\rangle\le N$. The separable argument combines a uniform mode-envelope upper relaxation with one Gaussian–sine product construction. It does not assume simultaneous attainability of separate mode maxima or an exact finite-band sine optimiser. An arithmetic resonance classification and a distinct finite-time detuning witness delimit applicability. General battery-state-set theorems encompass the invariant-measurement reduction, while earlier reference-frame alignment already supplies entanglement-assisted and internal-multiplicity constructions. The contribution claimed here is the evaluated shared-compensator constraint together with its strict and sharp preparation comparison, not those established methods. The calibrated-readout frontier, the exact static certificates and the distinct no-click limit paths of §§2–6 are retained and delimited. The comparison with prior work is carried out against the nearest battery, asymmetry, reference-frame alignment and separate-storage results at assumption–statement level. No action-selected Z-Spin apparatus, autonomous clock, stable physical event or cosmological observation is derived.


## 1. Problem, scope and the dependency structure of the results

### 1.1 Question and one-sentence contribution

**Central question.** At fixed compensator bandwidth, does enforcing independent rotor–compensator preparation impose an unavoidable single-shot discrimination cost when charge and energy are both conserved, and what is its sharp large-bandwidth size?

**Contribution.** Within the declared resonant model, separability changes the leading optimal error from $\pi^2/(8N)$ to $\pi/N$; finite-state constructions, a strict finite-$N$ obstruction, a shared-mode optimisation bracket and a complete asymptotic squeeze establish the comparison and its operational scope.

This question differs from the one answered by the externally preset bin phases of §§2–6, and it is not answered by comparing different observation windows or different measurement classes. The unrestricted joint ceiling uses standard chain mathematics. The nontrivial candidate contribution is the evaluated **single shared compensator** constraint, together with the strict preparation comparison. Section 9 maps the strongest known battery framework onto this model, including its ability to encompass both conserved quantities with one effective generator. That mapping prevents an artificial novelty claim based on the number of conservation laws.

**Scope and role.** The result is a statement about a declared model, not about a physical apparatus: removing the Z-Spin labels leaves the mathematics intact, so its role in the wider programme is SUPPORT/METHOD rather than a bridge claim. No locked Z-Spin constant enters §§2–8. Appendix A is a conditional calculation, logically independent of §§2–7, and is the only place where an upstream model enters. The physical requirements that this paper does **not** discharge — an action-derived instrument, a derived preparation and split, a clock, a normalised packet and a stable physical event — are listed in §8.3 and remain open.

**Reading map.** Section 7 is self-contained except for the explicitly proved quadratic-form, discrete oscillator and localisation identities (28)–(30) in §6.2. Sections 2–6 analyse the calibrated instrument; §8 distinguishes its limits from the new apparatus and develops conditional Z-Spin interpretations. A single summary of every claim, its proof locator and its strongest attack is given in §9.2.

### 1.2 Declared model and working assumptions

With `ℏ=1`, the rotor reference is declared as follows.

$$
\mathcal H_R=\ell^2(\mathbb Z),\qquad M|m\rangle=m|m\rangle,\quad L:=M,\qquad H_R=\Delta M^2,\qquad
\zeta(\sigma):=\operatorname{tr}(\sigma M^2)=\sum_m m^2\sigma_{mm},\qquad \delta:=\Delta/\hbar .
\tag{1}
$$

1. **Inputs and charge.** The qubit charge is `N_S=|1⟩⟨1|`, the total charge is `N_S+L`, and the two inputs to be distinguished are `|±x⟩=(|0⟩±|1⟩)/√2`. The reference state `σ` is an arbitrary density operator whose phases are known to the controller. The qubit has zero Hamiltonian during readout; on the undecayed subspace the generator is `I_S⊗δM²`.
2. **Readout apparatus (declared input).** In each total-charge sector `q`, on the doublet `{|0,q⟩,|1,q−1⟩}` we place absorptive jumps `L_{q,r}=√κ|d_{q,r}⟩⟨q,r(β)|` with `|q,r(β)⟩=(|0,q⟩+re^{iβ_{q,j}}|1,q−1⟩)/√2`, `r=±1`. The flags are mutually orthogonal absorbing states with total charge `q` and no outgoing jumps; in a singleton sector the hazard is split as `√(κ/2)` over two flags. The time bins are `[jh,(j+1)h)`, `j=0,…,B−1`, `T=Bh`, and no-click is included. The total hazard is the same `κ` in every sector. **The pre-set phase `β_{q,j}` per sector and per bin is a control input chosen before the measurement**, not a post-processing of stored signs.
3. **Record size.** `D` is the total variation between the output distributions (all flags × bins, plus no-click) of the two inputs. Write `S_w(σ)=Σ_m w_m|σ_{m,m+1}|`. For the calibrated instrument, `D=(1−e^{−κT})S_w`. Because the click probability is the same for both inputs, `S_w` is also their click-conditioned TV. Conditional normalisation does not create additional unconditional information.
4. **Energy budget.** We distinguish two problems: exact energy `ζ(σ)=ζ` and budget `ζ(σ)≤ζ`. The theorems address the latter; §5.2 makes the difference explicit.
5. **Idealisations.** The infinite charge register, phase control in every sector and the exact clock are mathematical idealisations. This paper does not derive their cost.

**Dependency freeze.** Sections 2–6 of this manuscript depend only on the declared model above and on standard mathematics (Perron–Frobenius, Cauchy–Schwarz, the Sips expansion of Mathieu characteristic values); they do not use the locked constants of Z-Spin (`Q, A, λ, z*`). Only Appendix A depends on an upstream source. That source declares the *forms* — the two-dimensional positive-energy Dirac band, the momentum relation and the exponential profile family — while the *numerical instance* used in Appendix A is chosen here; the appendix tabulates that split item by item and its conclusions are conditional. The open physical requirements listed in §8.3 are not changed by this paper.

**Material outside the present verification scope.** A set of fixed-$X$ readout laws (discarding of the click time, the rectification floor $2/\pi$, resonance, rational orbits, jitter) appears in earlier project material. Their status is not inherited here: they lie outside this paper and outside its executable claims.

### 1.3 Distinct quantities and shared notation

| Model | Supplied resource and restriction | Operational quantity and limiting parameter |
|---|---|---|
| Calibrated absorptive detector, §§2–6, 8.1 | Rotor state $\sigma$; external sector/bin phase control, common hazard; charge-preserving apparatus | $D^{\rm cal}=(1-e^{-\kappa T})S_w$; bin scale $\varepsilon=\delta h$, rotor mean energy $\zeta$ |
| Joint charge–energy measurement, §7.1–§7.6 | Rotor–compensator state $\rho$; same effects commuting with charge and bare energy for both preparation classes | $\mathcal D_N^{\rm all}$ or $\mathcal D_N^{\rm sep}$; compensator bandwidth $N\Delta$ |
| Finite-time detuning witness, §7.7 | Fixed resonant state and effects averaged over a finite time window | $D_{N,T}(r)$; dimensionless duration $\tau=\Delta T/\hbar$; exact detuned energy invariance is not imposed |

The notation $M$ in the rotor sections is an integer-valued charge operator; the scalar $M=4$ of Appendix A is the independently declared band mass. The edge gap $d_m=2m+1$ in §7 is distinct from the local finite difference $d_m=f_{m+1}-f_m$ used only inside §6.2's proofs. No relation $N\leftrightarrow h$ or identification of either with a locked project constant is assumed.

**Label convention.** Parenthesised (R1)–(R19) are equations in §7. The zero-padded identifier `R01` is a regression row in the verification ledger of Appendix B, and the model falsifiers of §8.2 are F1…F7. These are separate namespaces.

## 2. Single-shot bound of invariant measurements — T-CAP

Let `𝒢` be the U(1) twirl of the total charge `N_S+L`.

**Theorem T-CAP.** For every density operator σ,

$$
\frac12\Big\|\mathcal G\big[(|{+}x\rangle\langle{+}x|-|{-}x\rangle\langle{-}x|)\otimes\sigma\big]\Big\|_1
=\sum_m|\sigma_{m,m+1}|=:C(\sigma).
\tag{2}
$$

**Proof.** `|+x⟩⟨+x|−|−x⟩⟨−x|=X`, and a component `|0,m⟩⟨1,m′|` of `X⊗σ` conserves total charge iff `m′=m−1`; for the opposite direction iff `m′=m+1`. What survives the twirl is, for each charge `q`, a 2×2 block with zero diagonal and off-diagonal entries `σ_{q,q−1}` and its conjugate; with eigenvalues `±|σ_{q,q−1}|` its trace norm is `2|σ_{q,q−1}|`. Multiplying the sum by ½ gives (2). The adjacent entries of a positive state are absolutely summable, so the expression is defined for infinite support as well. □

Equation (2) is the **single-shot distinguishability bound of invariant measurements** for the given input pair and reference; it is not a definition of channel capacity. It is a specialisation of the standard asymmetry argument and no novelty is claimed (V01: error `1.1×10⁻¹⁶` on 100 random mixed states).

## 3. Energy bounds of the ideal readout — T-EC, T-ASY

**Theorem T-EC.** For every σ and finite `ζ=ζ(σ)`,

$$
C(\sigma)\ \le\ \min\{1,\sqrt{2\zeta}\},
\tag{3}
$$

$$
|\psi_\zeta\rangle=\sqrt{\zeta/2}\,|{-}1\rangle+\sqrt{1-\zeta}\,|0\rangle+\sqrt{\zeta/2}\,|1\rangle\quad(0\le\zeta\le1):\qquad
C_\zeta=\sqrt{2\zeta(1-\zeta)},\ \ \zeta(\psi_\zeta)=\zeta,
\tag{4}
$$

$$
C(\sigma)\ \le\ \sqrt{\frac{4\zeta}{1+4\zeta}}\qquad\Big(\text{circular uncertainty } \tfrac{S_1^2}4\le\operatorname{Var}_a(M)\langle Y_c^2\rangle\le\zeta(1-S_1^2)\Big).
\tag{5}
$$

**Proof.** Let `a_m=√σ_mm≥0`, `Σa_m²=1`. Positive semidefiniteness gives `|σ_{m,m+1}|≤a_ma_{m+1}`, hence `C≤S_1:=Σa_ma_{m+1}`. For finite support, an index shift and Cauchy–Schwarz give

$$
S_1=\sum_m m\,a_m(a_{m-1}-a_{m+1}),
\tag{3a}
$$

$$
S_1^2\le\Big(\sum_mm^2a_m^2\Big)\Big(\sum_m(a_{m-1}-a_{m+1})^2\Big)=\zeta\,(2-2S_2)\le2\zeta,\qquad S_2:=\sum_ma_ma_{m+2}\ge0,
\tag{3b}
$$

and `S_1≤1`, which is (3). For finite ζ, `(ma_m)` and `(a_{m−1}−a_{m+1})` are in ℓ², so the same identity follows by truncation and a limit. (4) is a direct computation; since `C_ζ/√(2ζ)=√(1−ζ)→1`, the `√2` in (3) cannot be improved at low energy. (5): with `U|m⟩=|m+1⟩`, `X_c=(U+U†)/2`, `Y_c=(U−U†)/(2i)`, `[M,Y_c]=−iX_c`. For real a, `⟨Y_c⟩=0` and `⟨X_c⟩=S_1`, so the Robertson inequality together with `X_c²+Y_c²=I` and `⟨X_c²⟩≥⟨X_c⟩²` yields the bracket in (5); rearranging gives `S_1²≤4ζ/(1+4ζ)`. A finite second moment guarantees that the quadratic form of the unbounded `M` applies. □

Equation (5) is Hradil et al. (2006) Eq.(7), the dispersion relation `D²(ΔL)²≥(1−D²)/4`, applied after domination by the pure state with `a=√diag σ` (IMPORTED-PROVEN; setting `C(σ)` directly equal to `|tr σU|` would let the phases of the adjacent entries cancel, so the pure-state reduction is necessary — this reduction is the mapping contribution of this manuscript and is DERIVED). C01 checks (3a)–(3b) with exact coefficients on finite support; V02 and V03 check (3) and (4) numerically.

**A retained upper bound and its subsumption.** The seed lineage proved a separate high-energy upper bound

$$
C(\sigma)\le1-\frac{1}{8(1+\sqrt\zeta)^2}
\tag{6}
$$

but with `x=√ζ`, `U_{\rm old}=1−1/[8(1+x)²]` and `U_B²=4x²/(1+4x²)`,

$$
U_{\rm old}^2-U_B^2=\frac{49+224x+308x^2+128x^3}{64(1+x)^4(1+4x^2)}>0
\tag{7}
$$

so (5) is strictly stronger than (6) at every finite ζ. (6) is true but not a new result (C02 checks the exact coefficients of (7); R01 is a regression check that (6) is never violated), and it is excluded from the central contribution of this manuscript.

**Standard form of the optimisation.** For `A_0=(U+U†)/2`,

$$
F_0(\zeta):=\sup_{a\ge0,\ \|a\|=1,\ \langle M^2\rangle\le\zeta}\langle a,A_0a\rangle
=\inf_{\nu\ge0}\{\nu\zeta+e_0(\nu)\},\qquad
e_0(\nu)=\sup\operatorname{spec}(A_0-\nu M^2)=-\frac\nu4\,a_0(-2/\nu)
\tag{8}
$$

where `a_0` is the Mathieu characteristic value (in the angle representation `A_0−νM²=\cos θ+ν∂_θ²`, `θ=2x`). This is the same problem as Parhizkar–Barbotin–Vetterli (2013) Eq.(17) and Theorem 2 (a reparametrisation with `σ_ω²=S_1^{−2}−1`; the ε-sequence `εδ_{n+1}+√(1−2ε²)δ_n+εδ_{n−1}` of their §2 is (4)); V04 compares the two computational routes.

**Theorem T-ASY (imported).** Inserting the Sips expansion of DLMF 28.8.1, `a_0(q)=−2q+2√q−¼−1/(32√q)+O(q^{−1})`, into (8) and taking the infimum,

$$
1-F_0(\zeta)=\frac1{8\zeta+\tfrac12}-\frac1{512(2\zeta+\tfrac18)^3}+O(\zeta^{-4})
=\frac1{8\zeta}-\frac1{128\zeta^2}+O(\zeta^{-3}),\qquad\zeta\to\infty .
\tag{9}
$$

Writing `x=√(ν/2)`, `νζ+e_0(ν)=1−x+(2ζ+⅛)x²+x³/64+O(x⁴)`, and the minimiser `x_0=1/(2(2ζ+⅛))` gives (9). Hence **the product of the coherence deficit and the energy of the ideal readout obeys `(1−F_0(ζ))ζ→1/8`**. V05 reproduces (9) at ζ≈10, 30, 100, 300 with relative error `≤1.9×10⁻⁷`. We do not claim that the Gaussian is the exact optimal state at finite ζ.

## 4. The weighted record law — L-CAL

The Bohr frequency of edge $(m,m+1)$ is

$$
\omega_m=\delta[(m+1)^2-m^2]=\delta(2m+1).
\tag{10}
$$

**Lemma L-CAL [DERIVED].** Under §1.2, for arbitrary reference state $\sigma$, the maximum over the preset sector/bin phases is

$$
D^{\rm cal}_{h,T}(\sigma)=(1-e^{-\kappa T})\sum_m w_m(h)|\sigma_{m,m+1}|.
\tag{11}
$$

Fix the Schrödinger convention $\rho(t)=e^{-iHt}\rho(0)e^{iHt}$ and the ket $|q,r(\beta)\rangle=(|0,q\rangle+r e^{i\beta}|1,q-1\rangle)/\sqrt2$. The corresponding kernel and control are

$$
I^-_{q,j}=\int_{jh}^{(j+1)h}\kappa e^{-\kappa t-i\omega_{q-1}t}\,dt,
\qquad \beta_{q,j}=-\arg(\sigma_{q,q-1}I^-_{q,j})\pmod\pi.
\tag{11a}
$$

If the complex product is zero, any phase is allowed. Otherwise the formula fixes the modulus of the real part; adding $\pi$ exchanges the two flag names. The same reference and the same control are used for both qubit inputs.

$$
w_m(h)=\frac{\kappa|1-e^{-(\kappa+i\omega_m)h}|}
 {\sqrt{\kappa^2+\omega_m^2}(1-e^{-\kappa h})}\in(0,1].
\tag{12}
$$

For a fixed phase per sector and an infinite window with click time discarded,

$$
w_m^{\rm stat}=\frac{\kappa}{\sqrt{\kappa^2+\omega_m^2}},\qquad
D_{\rm stat}^{\rm opt}(\sigma)=\sum_m w_m^{\rm stat}|\sigma_{m,m+1}|.
\tag{13}
$$

**Derivation.** In a charge-$q$ doublet the off-diagonal difference of the input states is $\sigma_{q,q-1}e^{-i\omega_{q-1}t}$. Projecting onto the declared detector ket and integrating gives
$p_+(q,r,j)-p_-(q,r,j)=r\operatorname{Re}(e^{i\beta_{q,j}}\sigma_{q,q-1}I^-_{q,j})$.
The factor $1/2$ in TV cancels the sum over the two opposite flags. Equation (11a) maximises each sector/bin contribution simultaneously. The modulus of $I^-_{q,j}$ equals $e^{-\kappa jh}\kappa|1-e^{-(\kappa+i\omega_{q-1})h}|/\sqrt{\kappa^2+\omega_{q-1}^2}$. Summing the geometric series gives (11). No-click has probability $e^{-\kappa T}$ for each input. At finite reference cutoffs, singleton sectors also have equal probabilities and the same total hazard; neither contributes to TV. In the full infinite rotor every charge sector is a doublet. Absolute convergence follows from (2). Merging all bins before choosing a fixed sector phase and taking $T\to\infty$ gives (13). □

The modulus in (12) is unchanged by complex conjugation, but the implementing phase in (11a) is not. For reference $(|0\rangle+|1\rangle)/\sqrt2$ and $\kappa=\delta=h=T=1$, the corrected control gives TV $0.303686323067$; the former opposite-sign control gives $0.204182609168$. The static opposite-sign prescription gives zero instead of $1/(2\sqrt2)$. These are implementation counterexamples, not counterexamples to the corrected optimum. V06/V07 retain direct quadrature and GKSL checks; V15 evaluates the displayed convention on real and complex references.

**Coherence versus score.** At each fixed edge, $w_m(h)\to1$ as $h\to0$; dominated convergence gives $D^{\rm cal}_{h,T}\to(1-e^{-\kappa T})C(\sigma)$ for a fixed state and compatible windows. For fixed $h>0$, the weights have an $O(1/|m|)$ envelope. They need not be globally monotone because the bin response has side lobes. Fast-edge coherence can therefore contribute little to the same detector's score. A single-frequency factor cannot replace the edge-dependent sum.

## 5. The weighted frontier: duality, finite-energy saturation, certified enclosures

### 5.1 Definitions and T-WR

For a weight sequence with `0≤w_m≤1`,

$$
(A_wa)_m=\tfrac12\big(w_{m-1}a_{m-1}+w_ma_{m+1}\big),\qquad
F_w(\zeta):=\sup_{\operatorname{tr}\sigma M^2\le\zeta}\ \sum_mw_m|\sigma_{m,m+1}| .
\tag{14}
$$

**Theorem T-WR.** For every `ζ>0`,

$$
F_w(\zeta)=\max_{a\ge0,\ \|a\|=1,\ \langle M^2\rangle\le\zeta}\langle a,A_wa\rangle
=\inf_{\nu\ge0}\big[\nu\zeta+\sup\operatorname{spec}(A_w-\nu M^2)\big],
\tag{15}
$$

and the first maximum is attained. At `ζ=0` both sides are 0; this does not mean that the dual infimum is attained at a finite ν.

**Proof.** By positivity every adjacent entry is dominated by `√(p_mp_{m+1})`, and the pure state `a=√p` with the same diagonal attains all of these simultaneously, so the pure-state reduction is exact. The set of energy-constrained density operators is trace-norm compact, by the compact resolvent of `M²` and the tail estimate `Σ_{|m|>L}p_m≤ζ/(L+1)²`; the objective is the support function of a bounded phase-weighted shift and hence trace-norm continuous, so the maximum exists. Since `p↦Σw_m√(p_mp_{m+1})` is concave, `F_w` is finite, concave and nondecreasing in ζ, and for ζ>0 choosing the slope `ν≥0` of a supporting line gives the same value as the Lagrangian upper bound. The supremum of the energy-penalised objective over all budgets is the top spectral value of the self-adjoint `A_w−νM²`, which gives (15). At ζ=0, by (3), `sup spec(A_w−νM²)≤sup_{E≥0}(√(2E)−νE)=1/(2ν)`, so the dual infimum is also 0 as ν→∞. □

No novelty is claimed for the dualisation or for the Jacobi tools themselves.

### 5.2 Finite-energy saturation — T-SAT

**Theorem T-SAT.** For the weights (12) (`h>0, κ>0, δ>0`) or (13), `0<w_m<1` and `w_m=O((1+|m|)^{−1})`. Consequently `A_w` is compact and self-adjoint, has a positive top eigenvalue `Λ_w∈(0,1)` and a (unique) normalised strictly positive eigenvector `v`, and

$$
\zeta_{\rm crit}:=\sum_mm^2v_m^2<\infty,\qquad
F_w(\zeta)=\Lambda_w\quad\text{for every }\zeta\ge\zeta_{\rm crit}.
\tag{16}
$$

**Proof.** Since `w_m→0`, the finite matrix truncations converge in operator norm and `A_w` is compact. A two-point trial state shows that a positive spectral value exists. All connection weights are positive, so the Rayleigh quotient can only increase under taking absolute values, and if one component of a top eigenvector vanished the eigenvalue equation would force its neighbours to vanish too; hence all components are positive. If there were another top eigenvector, there would be a sign-changing vector orthogonal to the positive one whose absolute value is also a top vector, contradicting the strict triangle inequality on a positive edge. From `sup w_m<1` and `Σa_ma_{m+1}≤1` we get `Λ_w<1`. `MA_w` is bounded (its two weighted-shift coefficients `mw_m`, `mw_{m−1}` are bounded). From `v=Λ_w^{−1}A_wv` it follows that `Mv∈ℓ²`, i.e. `ζ_crit<∞`, and as soon as v satisfies the budget it attains the spectral upper bound exactly. □

**Exact energy versus budget.** If `ζ>ζ_crit` must be spent **exactly**, the supremum is still `Λ_w` but it is not attained (equality would require the diagonal to be `v²`, hence the energy to be `ζ_crit`). On the other hand

$$
\sigma_N=(1-\epsilon_N)|v\rangle\langle v|+\epsilon_N|N\rangle\langle N|,\qquad
\epsilon_N=\frac{\zeta-\zeta_{\rm crit}}{N^2-\zeta_{\rm crit}}
\tag{17}
$$

has energy exactly ζ and score `(1−ε_N)Λ_w→Λ_w`. The statement "a larger budget lowers performance" is false; what is false is **the strategy of investing more energy into a particular family of states**.

**Counterexample W01 (high coherence does not ensure high record).** A Gaussian of width `s→∞` has `C→1` but converges weakly to 0, so by compactness of `A_w`, `⟨a_s,A_wa_s⟩→0`. At `κ=δ=1`, `s=30`, `C=0.999861` and the static record is `0.063669`, whereas the lower-energy v obtains `0.525281`.

### 5.3 Certified enclosures — T-CERT

Let `P_L` keep `|m|≤L`, let `ℓ_L` be the finite top eigenvalue, `t_L` an upper bound for the outer block, and `b_L` an upper bound for the norm of the connecting block. If `u_L≥ℓ_L` and `u_L>t_L`, then

$$
\sup\operatorname{spec}(A_w-\nu M^2)\ \le\ u_L+\frac{b_L^2}{u_L-t_L}
\tag{18}
$$

(dominate the block quadratic form by `[[u_L,b_L],[b_L,t_L]]` and take the Schur complement). If the static ratio `r=δ/κ` is rational, the squared off-diagonals `1/[4(1+r²(2m+1)²)]` of the finite matrix are rational, so the positive definiteness of the finite truncation of `xI−(A_w−νM²)` can be decided by an **exact rational LDL**, and combining with

$$
t_L=\frac1{r(2L+1)}-\nu(L+1)^2,\qquad b_L=\frac1{2r(2L+1)}
\tag{19}
$$

yields an upper bound on the infinite lattice. The lower bound is computed from an actual state with integer amplitudes and exact norm, and an `isqrt`-based rational lower bound for the square root. **Theorem T-CERT** is the statement that this procedure yields a valid certificate in the four declared cases; the table below gives the outward-rounded intervals of those rationals (C03). Floating-point eigenvectors propose witnesses and brackets; rational LDL positivity, exact feasibility and rational square-root bounds validate the final certificate independently of that proposal.

<!-- CERT-TABLE -->
| static δ/κ | energy budget | certified lower bound | certified upper bound |
|---:|---|---:|---:|
| 1 | none | 0.525281008518 | 0.525372710540 |
| 4 | none | 0.176554418992 | 0.176571354718 |
| 1 | ζ≤1/10 | 0.300452633015 | 0.300452672026 |
| 4 | ζ≤1/10 | 0.102990315389 | 0.102990324808 |
<!-- /CERT-TABLE -->

At δ/κ=1, ζ≤0.1, the static record of the three-point witness (4) is exactly 0.3, and the certified lower bound exceeds 0.300452633015, so **a strict improvement obtained by changing the state under the same energy budget and the same static readout** is confirmed without numerical conjecture. The improvement is small. The first term of `t_L` could be reduced to `1/(r(2L+3))` using `|2m+1|≥2L+3`, but this was not used here (the looser choice remains valid).

### 5.4 Numerical table of finite-resolution saturation

Below are the values of `Λ_w` and `ζ_crit` for the weights (12) and (13), agreeing at two cutoffs (`L=160, 240`) (V08; these are not certified enclosures).

<!-- CEILING-TABLE -->
| Readout | δ/κ | κh | saturated record Λ_w | critical energy ζ_crit |
|---|---:|---:|---:|---:|
| static phase per sector, infinite window | 1 | — | 0.525281009 | 0.708680740 |
| static phase per sector, infinite window | 4 | — | 0.176554419 | 0.619895967 |
| static phase per sector, infinite window | 20 | — | 0.036299641 | 0.613733975 |
| calibrated phase per sector and bin | 1 | 0.5 | 0.868443653 | 1.799291256 |
| calibrated phase per sector and bin | 1 | 0.1 | 0.971634805 | 8.713058855 |
| calibrated phase per sector and bin | 1 | 0.03 | 0.991384809 | 28.918328446 |
| calibrated phase per sector and bin | 1 | 0.01 | 0.997118251 | 86.652809625 |
<!-- /CEILING-TABLE -->

For the last four, finite-bin rows, the unconditional maximum at `T=Bh` is `(1−e^{−κT})Λ_w(h)`. The static rows use an infinite observation window and cannot be converted to a finite-window response by the prefactor alone (§8.2). Section 6 studies the finite-bin `h` dependence.

## 6. The resolution–energy boundary layer — T-BL

### 6.1 Statement

Fix κ, δ>0 and let `h→0`. Put `ε:=δh`, `a:=κh=(κ/δ)ε`, `ω:=ε/√3`, let the phase of edge `m` be `θ_m:=ω_mh=2ε(m+½)`, let `w_m=w(θ_m)` be (12), and let `Λ_w=Λ_w(h)` and `ζ_crit(h)` be the quantities of T-SAT.

**Theorem T-BL [PROVEN in the declared model; replacement proof in §6.3].**

$$
1-\Lambda_w(h)=\frac{\delta h}{2\sqrt3}\Big(1+O\big((\delta h)^{1/2}\big)\Big),
\tag{20}
$$

$$
\zeta_{\rm crit}(h)=\frac{\sqrt3}{2\,\delta h}\Big(1+O\big((\delta h)^{1/4}\big)\Big),
\tag{21}
$$

$$
\boxed{\;\lim_{h\to0}\big(1-\Lambda_w(h)\big)\,\zeta_{\rm crit}(h)=\frac14 .\;}
\tag{22}
$$

More precisely, for all sufficiently small ε,

$$
\frac{\varepsilon}{2\sqrt3}\big(1-C_-\sqrt\varepsilon\big)\ \le\ 1-\Lambda_w(h)\ \le\ \frac{\varepsilon}{2\sqrt3}+C_+\varepsilon^2,\qquad
C_+=\frac13+\frac{(\kappa/\delta)^2}{24},
\tag{23}
$$

where `C₋` is a finite constant depending only on κ/δ. A numerical value of `C₋` is not claimed; (32) supplies a directly evaluable lower expression. The statement is existential for sufficiently small ε, not a certified numerical threshold ε₀. The exponents ½ and ¼ in the O(·) terms are artefacts of the method of proof and no optimality is claimed (numerically both quantities show O(ε) relative error, §6.4).

**Reading.** The limit (22) concerns the click-conditioned optimum at the exact onset of saturation. Neither the no-click probability nor an arbitrary joint energy/resolution path is included in $\Lambda_w$. At this same energy, $\Lambda_w\le F_0(\zeta_{\rm crit})$ follows from $w_m\le1$. The ideal frontier has limit $1/8$ by (9); this comparison is consistent with existing uncertainty bounds and does not surpass them. Section 8.1 states the additional conditions for unconditional TV.

### 6.2 Lemmas

**L1 — exact identity for the weights and elementary inequalities.** With `ρ:=(a/2)/\sinh(a/2)∈(0,1]`, for all `a>0` and `θ∈ℝ`,

$$
1-w(\theta)^2=\frac{\theta^2-4\rho^2\sin^2(\theta/2)}{a^2+\theta^2}.
\tag{24}
$$

*Proof.* Inserting `|1−e^{−a+iθ}|²=(1−e^{−a})²+4e^{−a}\sin²(θ/2)` into (12) gives `w²=[a²+4ρ²\sin²(θ/2)]/(a²+θ²)`. □ (C04.) From `x/\sinh x≥1−x²/6` (series coefficients `1/(2n+1)!≤6^{−n}`) we get `1−a²/12≤ρ²≤1`; `θ²−θ⁴/12≤4\sin²(θ/2)≤θ²−θ⁴/12+θ⁶/360` (alternating series); and for `y:=1−w²∈[0,1]`, `1−w≥y/2` and `1−w=y/(1+w)≤y/(2−y)≤y/2+y²/2`. Therefore

$$
\theta^2\le30:\ \ 1-w\ge\frac{\theta^2}{24}\Big(1-\frac{\theta^2}{30}\Big)-\frac{a^2}{24};\qquad
a^2\le12:\ \ 1-w\le\frac y2+\frac{y^2}2,\ \ y\le\frac{\theta^2+a^2}{12},
\tag{25}
$$

(for the lower bound, `θ⁴/(a²+θ²)≥θ²−a²`; for the upper bound, `θ²−4ρ²\sin²(θ/2)≤θ⁴/12+a²θ²/12`). Tail: if `a≤½`, then for all `θ>0`

$$
1-w(\theta)\ \ge\ \min\Big\{\frac{\theta^4}{36(a^2+\theta^2)},\ 0.27\Big\}
\tag{26}
$$

(for θ≤π, `θ²−4\sin²(θ/2)≥(θ⁴/12)(1−π²/30)≥θ⁴/18`; for θ≥π, `≥θ²(1−4/π²)`). Monotonicity: the sign of `d(w²)/dθ` is that of `2a²(ρ²\sinθ−θ)−2ρ²θf(θ)` with `f(θ)=2(1−\cosθ)−θ\sinθ`; since `ρ²\sinθ≤θ` and `f≥0` on `[0,2π]` (write `t=θ/2` and `f=4 sin(t)[sin(t)−t cos(t)]`, whose bracket has derivative `t sin(t)≥0`), `w` is nonincreasing on `[0,2π]`. For $\theta\ge2\pi$ and $a\le1/2$, the identity in (24) gives

$$
w(\theta)^2\le\frac{a^2+4}{a^2+\theta^2}\le\frac{17}{16\pi^2}<\frac14.
\tag{27}
$$

This coarse estimate is enough for the replacement exterior envelope. It avoids importing a numerical maximum of the side lobes. V12 retains finite-grid diagnostics; these do not prove the global inequalities.

**L2 — quadratic-form identity.** To keep the damping parameter $a$ distinct, vector arguments in L2–L4 and Steps 1–2 are denoted by $f$. For real `f∈ℓ²(ℤ)` with `Σm²f_m²<∞`, `d_m:=f_{m+1}−f_m`, and `V_m:=½[(1−w_{m−1})+(1−w_m)]≥0`,

$$
Q(f):=\|f\|^2-\langle f,A_wf\rangle=\frac12\sum_mw_md_m^2+\sum_mV_mf_m^2 .
\tag{28}
$$

*Proof.* `½Σw_m(f_m²+f_{m+1}²)=Σ_kf_k²(w_{k−1}+w_k)/2` and `Σ_kf_k²[(w_k+w_{k−1})/2+V_k]=‖f‖²`. □ (C05.) Hence `1−Λ_w=\inf_{‖f‖=1}Q(f)`, and since `A_w` is bounded this equals the infimum over finitely supported f.

**L3 — discrete harmonic-oscillator inequality.** For every `ω>0` and every real f of finite energy,

$$
\boxed{\;\frac12\sum_m(f_{m+1}-f_m)^2+\frac{\omega^2}2\sum_m\Big(m^2+\frac14\Big)f_m^2\ \ge\ \frac\omega2\sum_mf_m^2 .\;}
\tag{29}
$$

*Proof.* Let `s_m:=f_{m+1}+f_m`. For finite support, telescoping gives `Σ_m(m+½)d_ms_m=Σ_m(m+½)(f_{m+1}²−f_m²)=−Σf_k²` (C06). Hence `0≤Σ_m[d_m+(ω/2)(m+½)s_m]²=‖d‖²−ω‖f‖²+(ω²/4)Σ(m+½)²s_m²`, and from `s_m²≤2(f_m²+f_{m+1}²)`, `(ω²/4)Σ(m+½)²s_m²≤ω²Σ_k(k²+¼)f_k²`. Rearranging gives (29); infinite support follows by truncation and a limit. □ Equality is impossible except for `f≡0`, and the Gaussian `e^{−ωm²/2}` gives a ratio `1+O(ω)` (V09). This lemma is the discrete version of the completed-square uncertainty argument and no novelty is claimed for it.

**L4 — discrete IMS localisation.** If `χ_1²+χ_2²≡1`, then `Σ_i[(χ_if)_{m+1}−(χ_if)_m]²=d_m²+f_mf_{m+1}Σ_i(χ_{i,m+1}−χ_{i,m})²`, so

$$
Q(f)\ \ge\ Q(\chi_1f)+Q(\chi_2f)-\frac L2\|f\|^2,\qquad L:=\sup_m\sum_i(\chi_{i,m+1}-\chi_{i,m})^2,
\tag{30}
$$

(using `|w_mf_mf_{m+1}|≤(f_m²+f_{m+1}²)/2`). With `χ_1=1` (|m|≤K), `\cos(π(|m|−K)/2K)` (K≤|m|≤2K), `0` (|m|≥2K), and `χ_2=√(1−χ_1²)`, one has `L=4\sin²(π/4K)≤π²/(4K²)`. (C05.)

**L5 — positive supersolution and maximum principle.** If `u_m>0` and `u_m→0` (m≥m_1) satisfies `(A_wu)_m≤Λ_wu_m` (m≥m_1+1) and `w_j<Λ_w` (j≥m_1), then `v_m≤(v_{m_1}/u_{m_1})u_m` (m≥m_1).

*Proof.* Let `z:=v−(v_{m_1}/u_{m_1})u`; `z_{m_1}=0`, `z→0`. For `m≥m_1+1`, `Λz_m≤½(w_{m−1}z_{m−1}+w_mz_{m+1})`. If z were positive somewhere, its maximum would be attained at some `m*≥m_1+1`, and `Λz_{m*}≤½(w_{m*−1}+w_{m*})z_{m*}<Λz_{m*}`, a contradiction. □

**L6 — uniform exterior envelope and second moment.** Suppose $0<q<\Lambda_w$ and $w_j\le q$ for all $j\ge m_1$. Define

$$
p=\operatorname{arccosh}(\Lambda_w/q),\quad
u_m=e^{-p(m-m_1)}\quad(m\ge m_1),\quad r=e^{-2p}.
\tag{30a}
$$

For $m\ge m_1+1$, both adjacent edges are bounded by $q$, hence
$ (A_wu)_m/u_m\le q(e^p+e^{-p})/2=\Lambda_w$.
L5 yields $v_m\le v_{m_1}e^{-p(m-m_1)}$ on the entire positive exterior. Consequently,

$$
\sum_{m>m_1}m^2v_m^2\le v_{m_1}^2\,r
\left[\frac{m_1^2}{1-r}+\frac{2m_1}{(1-r)^2}+\frac{1+r}{(1-r)^3}\right].
\tag{30b}
$$

The three terms are the exact sums of $r^k$, $kr^k$, and $k^2r^k$, $k\ge1$. Thus (30b) controls an infinite second moment, not merely tail probability. C09 checks the rational recurrence for these sums; V11 tests the supersolution numerically.

### 6.3 Proof

**Vertex reflection.** The weights satisfy $w_{-m-1}=w_m$ on edges. On vertices, $(Rv)_m=v_{-m}$ commutes with $A_w$. Simplicity and positivity of the normalised top vector therefore imply

$$
v_{-m}=v_m.
\tag{30c}
$$

Reflection about $-1/2$ is not a symmetry of the vertex eigenvector. V16 directly attacks that distinction.

*Step 1 — the upper bound, right-hand side of (23).* Let `s²:=√3/(2ε)` and `f_m:=Z_s^{−1/2}e^{−m²/(4s²)}`. Since `Λ_w≥⟨f,A_wf⟩`, (28) and `w≤1` give `1−Λ_w≤Q(f)≤(1−S_1)+ΣV_mf_m²`. By Poisson summation, `1−S_1≤1/(8s²)+O(q)`, `ζ_s=s²+O(s⁴q)`, `μ_4:=Σm⁴f_m²=3s⁴+O(s⁶q)`, with `q=e^{−2π²s²}`. From the upper bound in (25), `V_m≤(θ_{m−1}²+θ_m²+2a²)/48+[(θ_{m−1}²+a²)²+(θ_m²+a²)²]/576`, and with `θ_{m−1}²+θ_m²=8ε²(m²+¼)`, `(x+a²)²≤2x²+2a⁴`, and `Σ[(m+½)⁴+(m−½)⁴]f_m²=2μ_4+3ζ_s+⅛`,

$$
1-\Lambda_w\le\frac1{8s^2}+\frac{\varepsilon^2}6\Big(s^2+\frac14\Big)+\frac{a^2}{24}+\frac{\varepsilon^4}{18}\Big(2\mu_4+3\zeta_s+\frac18\Big)+\frac{a^4}{144}+O(q)
=\frac{\varepsilon}{2\sqrt3}+\varepsilon^2\Big(\frac7{24}+\frac{(\kappa/\delta)^2}{24}\Big)+O(\varepsilon^3).
$$

For small ε, `C_+=⅓+(κ/δ)²/24` absorbs the O(ε³) term (on the grid of V10 the actual coefficient is ≈−0.05).

*Step 2 — the lower bound, left-hand side of (23).* Take a finitely supported f with `‖f‖=1`, `K=⌈ε^{−3/4}⌉`, the `χ_1,χ_2` of L4, `b:=χ_1f`, `c:=χ_2f`. (i) The phases of the edges met by b satisfy `|θ|≤Θ:=2ε(2K+3/2)`; by (25), `w_m≥1−η` with `η:=y/2+y²/2`, `y:=(Θ²+a²)/12`, and `V_m≥(ε²/6)(1−Θ²/30)(m²+¼)−a²/24`. Putting `ω̃:=ω\sqrt{1−Θ²/30}` and using (28) and (29) (with frequency `ω̃/\sqrt{1−η}`),

$$
Q(b)\ \ge\ \frac{1-\eta}2\|d_b\|^2+\frac{\tilde\omega^2}2\sum\Big(m^2+\frac14\Big)b_m^2-\frac{a^2}{24}\|b\|^2
\ \ge\ \Big[\frac{\sqrt{1-\eta}\,\tilde\omega}2-\frac{a^2}{24}\Big]\|b\|^2 .
\tag{31}
$$

(ii) The two edge phases where c lives, `|m|≥K`, satisfy `|θ|≥θ_K:=2ε(K−½)`, so by (26) `V_m≥V_{\rm tail}:=\min\{θ_K⁴/(36(a²+θ_K²)),0.27\}` and `Q(c)≥V_{\rm tail}‖c‖²`. (iii) From (30) and `‖b‖²+‖c‖²=1`,

$$
1-\Lambda_w=\inf_fQ(f)\ \ge\ \min\Big\{\frac{\sqrt{1-\eta}\,\tilde\omega}2-\frac{a^2}{24},\ V_{\rm tail}\Big\}-2\sin^2\frac\pi{4K}.
\tag{32}
$$

Orders of magnitude: `Θ≈4ε^{1/4}`, `η≈(2/3)ε^{1/2}`, `1−Θ²/30≈1−(8/15)ε^{1/2}`, `V_{\rm tail}≈ε^{1/2}/9≫ω/2≈0.29ε`, `2\sin²(π/4K)≈π²ε^{3/2}/8`. Hence the right-hand side of (32) is `(ε/(2√3))(1−C_−ε^{1/2})`. V10 checks (32)≤`1−Λ_w` on a 12-point grid (the lower bound is loose: 0.845 times the leading term at ε=10⁻³).

*Step 3 — the energy (21).* Let `v` be the top eigenvector, `b=χ_1v`, `c=χ_2v`, `z_b:=Σ(m²+¼)b_m²/‖b‖²`. Writing (29) with a free frequency ω′ and choosing `ω′=1/(2z_b)` gives `½‖d_b‖²≥‖b‖²/(8z_b)`, so the first inequality of (31) becomes, with `α:=\sqrt{1−η}` and `z_*:=α/(2ω̃)`,

$$
Q(b)\ \ge\ \Big[\frac{\alpha\tilde\omega}2+\frac{\tilde\omega^2}2\frac{(z_b-z_*)^2}{z_b}-\frac{a^2}{24}\Big]\|b\|^2
\qquad\Big(\frac{\alpha^2}{8z}+\frac{\tilde\omega^2z}2-\frac{\alpha\tilde\omega}2=\frac{(2\tilde\omega z-\alpha)^2}{8z}\Big).
\tag{33}
$$

Combining `Q(v)=1−Λ_w≤ε/(2√3)+C_+ε²` from Step 1 with (30) and (ii) gives `(ε/(2√3))(1+2√3C_+ε)≥[αω̃/2−a²/24]‖b‖²+(ω̃²/2)(z_b−z_*)²/z_b·‖b‖²+V_{\rm tail}‖c‖²−2\sin²(π/4K)`. The first coefficient is `(ω/2)(1−O(ε^{1/2}))` and `V_{\rm tail}≫ω/2`, so (a) `‖c‖²≤O(ε^{3/2})/V_{\rm tail}=O(ε)` and `‖b‖²≥1−O(ε)`; (b) `(ω̃²/2)(z_b−z_*)²/z_b≤(ω/2)O(ε^{1/2})`. If `z_b>2z_*`, the left-hand side would be `≥ω̃²z_*/8≈ω/16`, contradicting (b); hence `z_b≤2z_*` and therefore `|z_b−z_*|/z_*≤O(ε^{1/4})`. From `ζ_crit=Σm²b_m²+Σm²c_m²` (χ_1²+χ_2²=1):

- Lower bound: `ζ_crit≥(z_b−¼)‖b‖²=(\sqrt3/(2ε))(1−O(ε^{1/4}))`.
- Transition region: for $|m|\le m_1:=2K$, $\sum m^2c_m^2\le m_1^2\|c\|^2=O(\varepsilon^{-1/2})$.
- Infinite exterior: put $\theta_1:=2\varepsilon(m_1+1/2)$ and $q_\varepsilon:=w(\theta_1)$. For sufficiently small $\varepsilon$, $a\le1/2$, $0<\theta_1<2\pi$ and $q_\varepsilon>1/2$. Monotonicity on $[0,2\pi]$ and (27) show $w_j\le q_\varepsilon$ for every $j\ge m_1$, including all side lobes. The upper and lower estimates in (25), together with $K=\lceil\varepsilon^{-3/4}\rceil$, yield

$$
1-q_\varepsilon=\frac23\sqrt\varepsilon+O(\varepsilon),\quad
\Lambda_w-q_\varepsilon=\frac23\sqrt\varepsilon+O(\varepsilon)>0,\quad
p_\varepsilon:=\operatorname{arccosh}(\Lambda_w/q_\varepsilon)
=\frac2{\sqrt3}\varepsilon^{1/4}(1+O(\sqrt\varepsilon)).
\tag{33a}
$$

Here $\theta_1^2=16\sqrt\varepsilon+O(\varepsilon^{5/4})$, the error $O(\theta_1^4+a^2)$ is $O(\varepsilon)$, and $\operatorname{arccosh}(1+x)=\sqrt{2x}(1+O(x))$ gives the final relation. These are consequences of uniform inequalities, not sampled eigenvectors. At $m_1=2K$, $c_{m_1}=v_{m_1}$, so $v_{m_1}^2\le\|c\|^2=O(\varepsilon)$. L6 and the correct reflection (30c), with $1-e^{-2p_\varepsilon}\asymp\varepsilon^{1/4}$, now give

$$
\sum_{|m|>m_1}m^2v_m^2
\le 2v_{m_1}^2 e^{-2p_\varepsilon}
\left[\frac{m_1^2}{1-e^{-2p_\varepsilon}}
 +\frac{2m_1}{(1-e^{-2p_\varepsilon})^2}
 +\frac{1+e^{-2p_\varepsilon}}{(1-e^{-2p_\varepsilon})^3}\right]
=O(\varepsilon^{-3/4}).
\tag{33b}
$$

The three terms, after multiplying by $O(\varepsilon)$, have orders $\varepsilon^{-3/4}$, $\varepsilon^{-1/4}$ and $\varepsilon^{1/4}$. Thus $\sum m^2c_m^2=O(\varepsilon^{-3/4})$. Combining with $\sum m^2b_m^2=(z_b-1/4)\|b\|^2$, $\|b\|^2=1-O(\varepsilon)$ and $z_b=z_*(1+O(\varepsilon^{1/4}))$ proves both sides of (21). Multiplying (20) and (21) proves (22). □

This proof replaces an earlier phase-$\pi$ middle/far split and variable-rate supersolution. A weaker exterior bound is sufficient because its contribution is $O(\varepsilon^{1/4})$ relative to the leading energy.

**Legacy-bound regression.** To document the precise retired error, let $M_0=\lfloor\pi/(2\varepsilon)-1/2\rfloor$ and $w_*=w(3.8)$. For sufficiently small $\varepsilon$, monotonicity up to $2\pi$ and (27) imply the valid common upper bound

$$
q^{\rm old}_\varepsilon=\max\{w_{M_0},w_*\},\qquad
p_j\ge\operatorname{arccosh}(\Lambda_w/q^{\rm old}_\varepsilon)>1
\quad(j\ge M_0),
\tag{33c}
$$

where $p_j=\operatorname{arccosh}(\Lambda_w/\max\{w_j,w_*\})$. Indeed $q^{\rm old}_\varepsilon\to2/\pi$ and $\Lambda_w\to1$, so the bound tends to $\operatorname{arccosh}(\pi/2)>1$. The retired expression using only $w_*$ is larger than the actual $p_{M_0}$ and is false. This diagnostic, checked in V17, is not used in the replacement proof.



The proof uses only the exact form of (12) (L1), positivity and compactness (T-SAT), elementary series inequalities, telescoping, completing the square, and partition of unity with the maximum principle; it does not invoke the general theory of Mathieu functions, Γ-convergence or WKB. All techniques are standard (§9.1).

### 6.4 Second-order terms (Conjecture C-2) and the numerical table

**Conjecture C-2 [HYPOTHESIS: formal expansion + numerical agreement].** Expanding (28) in the small parameter `ω=ε/√3` gives `Q≈½p²−p⁴/24−(ε²/12)\,p\,m²p+(ε²/6)(m²+¼)−(ε⁴/120)m⁴+⋯` (using `1−\cos k=k²/2−k⁴/24`, `1−w(θ)=θ²/24−θ⁴/1920+O(θ⁶)`, and the mass term `−½Σ(1−w_m)d_m²`), and first-order perturbation of the harmonic-oscillator ground state gives `⟨0|H_1|0⟩=−ω²/32−3ω²/16−9ω²/160+ω²/8=−3ω²/20`, `⟨2|H_1|0⟩=−\sqrt2ω²/20`, `δ⟨m²⟩=1/20`. That is,

$$
1-\Lambda_w(h)=\frac{\varepsilon}{2\sqrt3}-\frac{\varepsilon^2}{20}+O(\varepsilon^3),\quad
\zeta_{\rm crit}(h)=\frac{\sqrt3}{2\varepsilon}+\frac1{20}+O(\varepsilon),\quad
(1-\Lambda_w)\zeta_{\rm crit}=\frac14-\frac{\varepsilon}{20\sqrt3}+O(\varepsilon^2).
\tag{34}
$$

**Local coefficient correction.** The smooth joint expansion at $(a,\theta)=(0,0)$ is

$$
1-w(\theta)=\frac{\theta^2}{24}-\frac{\theta^4}{1920}-\frac{a^2\theta^2}{480}
 +O((|a|+|\theta|)^6).
\tag{34a}
$$

For clarity, $\rho^2=1-a^2/12+a^4/240+O(a^6)$ and (24) give $w^2=1-\theta^2/12+a^2\theta^2/240+\theta^4/360+O((|a|+|\theta|)^6)$. Taking the positive square root proves (34a); C08 checks the exact coefficient algebra. The joint smoothness also follows by writing $w$ as the modulus of the characteristic function of the normalised density proportional to $e^{-at}$ on $[0,1]$, which is nonzero near the origin. On the boundary-layer scale $a=O(\varepsilon)$ and $\theta=O(\sqrt\varepsilon)$ the corrected mixed term is $O(\varepsilon^3)$. This neither proves nor refutes the spectral coefficients of (34). X01 retains the Richardson diagnostic, but (34) remains HYPOTHESIS because a controlled operator perturbation remainder has not been proved.

The table below gives the numerics at δ/κ=1 (V10). `(1−Λ_w)/ε→1/(2√3)=0.288675`, `ζ_crit·ε→√3/2=0.866025`, product→`1/4`; the last two columns are the proved inequality (32) and the Gaussian upper bound of Step 1, each divided by the leading term.

<!-- BL-TABLE -->
| ε=δh | (1−Λ_w)/ε | ζ_crit·ε | (1−Λ_w)ζ_crit | lower bound (32) / leading term | Gaussian upper bound / leading term |
|---:|---:|---:|---:|---:|---:|
| 0.03 | 0.287173 | 0.867550 | 0.2491369 | 0.1345 | 0.994802 |
| 0.01 | 0.288175 | 0.866528 | 0.2497116 | 0.5117 | 0.998268 |
| 0.003 | 0.288525 | 0.866176 | 0.2499134 | 0.7355 | 0.999480 |
| 0.001 | 0.288625 | 0.866075 | 0.2499711 | 0.8453 | 0.999827 |
<!-- /BL-TABLE -->

Correcting with (34), at ε=0.01 one gets `(ε/(2√3)−ε²/20)(√3/(2ε)+1/20)=0.249711`, in agreement with the table. V13 confirms monotone convergence to the two constants at `L=900`, `κh=0.1…0.001` (deviation `5.3×10⁻³→5.0×10⁻⁵`).

## 7. Joint charge–energy references: a separability cost at fixed bandwidth

### 7.1 A second measurement class and the central question

The phase controls in §4 are external inputs. This section asks a different, precisely specified implementation question: how well can the same zero-Hamiltonian qubit be read if all measurement effects conserve both total charge and the bare energy of a rotor plus an explicitly supplied energy compensator? The two preparation classes below have the **same apparatus spectrum and the same allowed measurements**. Their only difference is whether the initial rotor–compensator state may be entangled. This comparison does not assert an identity between bandwidth and the bin width of §4.

Let the compensator have nondegenerate levels $|k\rangle$, $k=0,\ldots,N$, where $N\ge0$ is an integer, and put

$$
K_C=\sum_{k=0}^N k|k\rangle\langle k|,\qquad
Q=N_S+M,\qquad H_{RC}/\Delta=M^2+K_C.
\tag{R1}
$$

The compensator carries zero $Q$ charge. A reference $\rho$ is an arbitrary density operator on $\mathcal H_R\otimes\mathbb C^{N+1}$, supplied independently of the input sign. The allowed POVMs on $SRC$ have effects commuting with $Q$ and every spectral projection of $H_{RC}$. No additional asymmetric reference is supplied. These are restrictions on the full statistics-generating effects, not merely on a selected Hamiltonian term. An invariant effect admits a symmetry-preserving dilation with a neutral pointer; choosing that dilation, preparing the state, timing the interaction and producing a stable record are separate implementation obligations.

Write $\mathcal D_N^{\rm all}$ for the largest output TV between $|\pm x\rangle\langle\pm x|\otimes\rho$, optimised over all references and allowed POVMs. Write $\mathcal D_N^{\rm sep}$ for the same supremum with $\rho$ separable across the **fixed physical split $R:C$**, including the trace-norm closure of finite convex mixtures. Both are unconditional single-shot quantities; there is no click postselection in their definition. A common independent erasure with probability $\eta$ multiplies both by $1-\eta$.

The compensator is not automatically a clock. In fact the optimal joint state below is stationary and its compensator marginal is diagonal in energy. It provides relational matrix elements at matched energy differences; no ticking observable or elapsed-time estimator has yet been constructed.

### 7.2 Resonant-chain reduction — T-JCE

For $d_m=2m+1$, define an edge of the reference graph by

$$
(m,k)\longleftrightarrow(m+1,k-d_m),\qquad
k\in\{0,\ldots,N\},\quad k-d_m\in\{0,\ldots,N\}.
\tag{R2}
$$

Each edge stays within one energy shell $e=m^2+k$. Let $\mathsf A_N$ have entry $1/2$ on these edges and zero elsewhere.

**Theorem T-JCE (exact operational reduction).** For a fixed reference,

$$
\sup_{\rm invariant\ POVM}D(\rho)
=\frac12\|\mathcal G_{Q,H}(X\otimes\rho)\|_1
=\Gamma_N(\rho):=
\sum_{m,k\,\text{as in (R2)}}
|\rho_{(m,k),(m+1,k-d_m)}|.
\tag{R3}
$$

Consequently $\mathcal D_N^{\rm all}=\sup\operatorname{spec}\mathsf A_N$. The graph is a disjoint union of finite paths, with vertices in shell $e$ given by

$$
I_e=\{m\in\mathbb Z:e-N\le m^2\le e\}.
\tag{R4}
$$

*Proof.* The difference of the two input density operators is $X$. Pinching $X\otimes\rho$ by $(Q,H)$ leaves, for every edge (R2), one two-dimensional block on $|1,m,k\rangle$ and $|0,m+1,k-d_m\rangle$. Its diagonal entries vanish and its off-diagonal entries are the indicated matrix element and its conjugate. Distinct edges give orthogonal blocks, including at adjacent rotor charges because the system label is different. Half the trace norm of a block is the modulus of its off-diagonal entry. Singleton blocks contribute zero. The blockwise Helstrom effects commute with both generators and attain the sum. For arbitrary trace-class $\rho$, the finite-rank pinching argument extends in trace norm. The sum is bounded by one: positivity bounds each summand by the geometric mean of its endpoint populations, and the graph has maximum degree two.

If $a_{m,k}=\sqrt{\rho_{(m,k),(m,k)}}$, positivity gives $\Gamma_N(\rho)\le\langle a,\mathsf A_Na\rangle$. Every such bound is attained by the pure nonnegative state with amplitudes $a$. Energy conservation gives (R4); only consecutive $m$ are connected. Its components are finite because $e$ is finite. This proves the reduction. □

The block-twirl method is standard symmetry-restricted discrimination. The path spectrum and sine states used below are also standard [10, §5.3 and Appendix E]. The proposed additional result is the **evaluated separable-versus-joint optimisation with the nonlinear gap $d_m=2m+1$**, especially T-SBC; T-JCE alone is not presented as new general theory.

### 7.3 Exact joint ceiling and a strict separation — T-JB

**Theorem T-JB (joint bandwidth ceiling).** With $n=\lfloor\sqrt N\rfloor$,

$$
\boxed{\mathcal D_N^{\rm all}=\cos\!\frac{\pi}{2n+2}.}
\tag{R5}
$$

It is attained by the stationary state

$$
|\Psi_N\rangle=\sum_{m=-n}^{n}s_m|m,N-m^2\rangle,
\qquad
s_m=\frac1{\sqrt{n+1}}\cos\!\frac{\pi m}{2n+2}.
\tag{R6}
$$

For every $N\ge1$,

$$
\mathcal D_N^{\rm sep}<\mathcal D_N^{\rm all},\qquad
\mathcal D_1^{\rm sep}=\frac1{2\sqrt2},\quad
\mathcal D_2^{\rm sep}=\frac12.
\tag{R7}
$$

The ceiling (R5) is unchanged if the common additional rotor budget $\operatorname{tr}\rho M^2\le N$ is imposed: (R6) is supported on $|m|\le n$.

*Proof of (R5).* If $0\le e\le N$, the shell is the central path from $-\lfloor\sqrt e\rfloor$ to $\lfloor\sqrt e\rfloor$, with at most $2n+1$ vertices. If $e>N$, its components lie strictly on one side of zero. A positive component $a,\ldots,b$, $a\ge1$, obeys $b^2-a^2\le N$. Were it to have at least $2n+1$ vertices, $b\ge a+2n$ would imply $b^2-a^2\ge4n(n+1)>N$ for $n\ge1$. Thus those components are shorter. For $N=0$ no adjacent squares have equal energy, so there are no edges. A path of $L$ vertices with off-diagonal $1/2$ has top eigenvalue $\cos[\pi/(L+1)]$, as follows directly by substituting $\sin[\pi j/(L+1)]$ in its recurrence with two zero boundary values. Shell $e=N$ reaches $L=2n+1$ and gives (R6). Its norm is one by the finite trigonometric sum. □

*Separable reduction and strictness.* The functional in (R3) is convex and trace-norm continuous. Therefore its supremum on separable states equals its supremum on products. Positivity in each factor reduces that supremum to nonnegative pure products $a_m b_k$. An edge can occur only when $|2m+1|\le N$, so a product optimiser can be taken in a finite central rotor interval and the finite compensator space. The maximum is attained.

Suppose a product attains (R5), for $N\ge1$. It must lie in the top eigenspace of $\mathsf A_N$. The only longest paths are the central shells $e=n^2,\ldots,N$: if a central shell is shorter its spectral radius is smaller, and the preceding one-sided estimate excludes another longest path. Thus a top vector has amplitudes $s_m c_{m^2+k}$, where $c_e=0$ outside $[n^2,N]$. For a nonnegative product this would require
$a_0b_k=s_0c_k$ and $a_1b_k=s_1c_{k+1}$ for every $k=0,\ldots,N$, with $a_0,a_1>0$. At $k=N$ the second equation gives $b_N=0$; the first then gives $c_N=0$. Descending induction forces all $b_k=0$, a contradiction. Strict inequality follows from attainment. This proof also covers mixed separable states through the product reduction.

For $N=1,2$, only $d_m=\pm1$ survives. The rotor factor is maximised on $m=-1,0,1$, with amplitudes $(1/2,1/\sqrt2,1/2)$ and edge sum $1/\sqrt2$. The maximal compensator nearest-neighbour coherence is $\cos[\pi/(N+2)]$, respectively $1/2$ and $1/\sqrt2$. Their products yield (R7), with explicit sine-state witnesses. □

At $N=1$, (R6) is
$\tfrac12|-1,0\rangle+\tfrac1{\sqrt2}|0,1\rangle+\tfrac12|1,0\rangle$.
Its rotor marginal has no adjacent-charge coherence; the compensator marginal is $I/2$. Nevertheless the invariant joint measurement has TV $1/\sqrt2$. Replacing this state by the product of its two marginals gives zero. The available information is relational across $R:C$. This does not identify entanglement with coherence in every reference-frame convention; the operational split and generators are fixed throughout.

### 7.4 A computable separability bound and a common-state lower bound — T-SB

For a compensator amplitude vector $b\ge0$ of norm one, set

$$
c_d(b)=\sum_{k=0}^{N-d}b_kb_{k+d},\quad 1\le d\le N,
\qquad c_d=0\quad(d>N).
$$

**Theorem T-SB (shared-mode optimisation and bracket).** The exact separable problem is

$$
\mathcal D_N^{\rm sep}
=\max_{a,b\ge0,\ \|a\|=\|b\|=1}
\sum_m a_ma_{m+1}c_{|2m+1|}(b).
\tag{R8}
$$

Define, for positive integers $d$,

$$
g_N(d)=
\begin{cases}
\cos\!\dfrac{\pi}{\lfloor N/d\rfloor+2},&d\le N,\\
0,&d>N,
\end{cases}
\qquad u_{m,N}=g_N(|2m+1|).
\tag{R9}
$$

For $B=N+2$, let $b_k^{\sin}=\sqrt{2/B}\sin[\pi(k+1)/B]$. Its autocorrelation is

$$
\ell_{m,N}=c_d(b^{\sin})=
\left(1-\frac dB\right)\cos\frac{\pi d}B
+\frac{\cot(\pi/B)}B\sin\frac{\pi d}B,
\qquad d=|2m+1|\le N,
\tag{R10}
$$

and zero otherwise. For the finite active Jacobi matrices with these edge weights,

$$
\boxed{\lambda_{\max}(A_{\ell,N})\le\mathcal D_N^{\rm sep}
\le\lambda_{\max}(A_{u,N}).}
\tag{R11}
$$

*Proof.* In a product state the matrix element in (R3) factors. Summing over $k$ gives (R8), with phases removed by the same positivity argument as above. For fixed $d$, the graph $k\leftrightarrow k+d$ on $0,\ldots,N$ is a union of residue-class paths; the longest has $\lfloor N/d\rfloor+1$ vertices. Its spectral radius is (R9), so $c_d(b)\le g_N(d)$ for every **single** state $b$. This gives the upper bound. The separate optimisers of different $d$ need not coincide: replacing (R8) by the upper matrix is a relaxation, not an equality. Substituting one common sine state and summing $2\sin x\sin y=\cos(x-y)-\cos(x+y)$ gives (R10). Optimising only $a$ then gives the lower bound. Both matrices are finite because their edge weights vanish outside $|2m+1|\le N$. □

An output contrast greater than the right-hand side of (R11) witnesses nonseparability of the supplied $R:C$ state under (R1) and the declared measurement restrictions. It is not a device-independent entanglement test. For $N>2$ neither side of (R11) is asserted to be the exact separable optimum.

<!-- BAND-TABLE -->
| $N$ | $\lambda_{\max}(A_{\ell,N})$ | $\lambda_{\max}(A_{u,N})$ | $\mathcal D_N^{\rm all}$ | Bracket for $N(1-\mathcal D_N^{\rm sep})$ |
|---|---:|---:|---:|---:|
| 1 | 0.353553391 | 0.353553391 | 0.707106781 | 0.646447–0.646447 |
| 2 | 0.500000000 | 0.500000000 | 0.707106781 | 1.000000–1.000000 |
| 3 | 0.576219423 | 0.624303010 | 0.707106781 | 1.127091–1.271342 |
| 4 | 0.629152870 | 0.661437828 | 0.866025404 | 1.354249–1.483389 |
| 8 | 0.752377405 | 0.770658841 | 0.866025404 | 1.834729–1.980981 |
| 16 | 0.850487104 | 0.871884193 | 0.951056516 | 2.049853–2.392206 |
| 64 | 0.955235761 | 0.959310388 | 0.984807753 | 2.604135–2.864911 |
| 256 | 0.988125721 | 0.988880210 | 0.995734176 | 2.846666–3.039815 |
| 1024 | 0.996971580 | 0.997058817 | 0.998867339 | 3.011771–3.101102 |
| 4096 | 0.999237287 | 0.999250960 | 0.999708014 | 3.068067–3.124071 |
| 16384 | 0.999808745 | 0.999810358 | 0.999925865 | 3.107088–3.133526 |
<!-- /BAND-TABLE -->

The bracket is printed as error lower–upper, so its endpoints reverse the contrast bracket. V24 generates these double-precision values; they are not interval-arithmetic certificates. The table uses (R8) without an extra rotor budget. The upper contrast bound remains valid under additional constraints, while the mean-budget asymptotic construction is proved separately in §7.5.

**Finite-$N$ interpretation.** Both error-bracket endpoints at $N=16384$ are below $\pi$: approximately $3.107088$ and $3.133526$. The bracket encloses the finite quantity $N(1-\mathcal D_N^{\rm sep})$, not its limit. Across the displayed large-$N$ samples, and in an independent extension to $N=65536$, both endpoint sequences move toward $\pi$ from below; the roughly $N^{-1/2}$ gap is an empirical trend. No monotonicity theorem or $O(N^{-1/2})$ remainder for the unknown optimum is asserted. This finite behaviour is consistent with (R12); its proof is the analytic squeeze in §7.5, not extrapolation.

At $N=4$, the upper matrix has edge weights $(1/2,\sqrt3/2,\sqrt3/2,1/2)$ and off-diagonals half those weights. Its monic characteristic polynomial $\det(xI-A_{u,4})$ is $x(x^2-1/16)(x^2-7/16)$, giving the exact upper bound $\sqrt7/4$ (C12). At $N=3$, the unique positive maximiser of $c_1$ is the sine state, whose $c_3=(5-\sqrt5)/20\simeq0.1381966$, whereas $\max c_3=1/2$; thus these two individual maxima cannot be used as if they belonged to one state (W05).

**Exact finite counterexample to sine optimality (C13).** Numerical searches for product optimisers give no global certificate for $N>2$. A simple exact witness makes the relevant implication rigorous. At $N=3$, choose

$$
b=(2,3,3,2)/\sqrt{26},\qquad c_1=21/26,\quad c_3=2/13,
\qquad \lambda_b^2=(c_3^2+2c_1^2)/4=449/1352.
$$

On rotor sites $m=-2,\ldots,2$ the four edge weights are $(c_3,c_1,c_1,c_3)$. The positive normalised rotor vector
$a=(c_3/(4\lambda_b),1/2,c_1/(2\lambda_b),1/2,c_3/(4\lambda_b))$
is its Perron eigenvector. Hence this single product state attains
$\lambda_b=\sqrt{449/1352}\simeq0.5762816948$.
For the common sine compensator the corresponding top eigenvalue instead has square
$(33+9\sqrt5)/160$ and value $0.5762194233$. Their squared difference is
$(3403-1521\sqrt5)/27040>0$, since $3403,1521>0$ and $3403^2-5\cdot1521^2=13204>0$.
C13 checks the rational correlations, the monic characteristic-polynomial recurrence and this exact comparison. This proves a finite improvement over the sine lower bound; it does **not** identify $\mathcal D_3^{\rm sep}$ or invalidate the sine state's asymptotic optimality in T-SBC. The unchanged BAND-TABLE intentionally continues to report its original common-sine lower bound.

### 7.5 Sharp asymptotic cost of separability — T-SBC

**Theorem T-SBC (bandwidth asymptotics).** As integer $N\to\infty$,

$$
\boxed{
\lim N(1-\mathcal D_N^{\rm sep})=\pi,\qquad
\lim N(1-\mathcal D_N^{\rm all})=\frac{\pi^2}{8},\qquad
\lim\frac{1-\mathcal D_N^{\rm sep}}{1-\mathcal D_N^{\rm all}}=\frac8\pi.
}
\tag{R12}
$$

The same three limits hold when both preparation classes additionally obey $\operatorname{tr}\rho M^2\le N$. The ratio compares **errors** $1-D$, not contrasts $D$ or total energies. It is unrelated to the saturation-path ratio between $1/4$ and $1/8$ in §§6–8.

*Proof, lower bound on the separable error.* We show
$1-\lambda_{\max}(A_{u,N})\ge\pi/N-o(N^{-1})$.
Fix $K=\lceil N^{3/4}\rceil$. For $d\le4K+3$, write
$\lfloor N/d\rfloor+2=N/d+\xi$ with $1<\xi\le2$. Uniformly on these edges, Taylor's theorem gives

$$
1-g_N(d)=\frac{\pi^2d^2}{2N^2}\{1+O(N^{-1/4})\},
\qquad g_N(d)=1-O(N^{-1/2}).
\tag{R13}
$$

Here and below the constants are independent of $d,N$ in the stated range; $d\ge1$ removes a zero-denominator issue. The floor function produces a bounded $\xi$, so no differentiability of $g_N$ is assumed. Also $g_N(d)$ is nonincreasing in $d$; at $d>N$ its value is zero. Consequently the site potential
$V_{m,N}=1-(u_{m-1,N}+u_{m,N})/2$
is at least $cK^2/N^2$ on $|m|\ge K$ for some fixed $c>0$ and all sufficiently large $N$.

Apply the exact form identity and IMS cutoffs of §6.2 to $u_N$, with the inner cutoff equal to one on $[-K,K]$ and zero outside $[-2K,2K]$. For the inner vector $f$, (R13) bounds its form below by

$$
\frac{\alpha_N}{2}\sum_m(f_{m+1}-f_m)^2
+\frac{\beta_N}{2}\sum_m(m^2+1/4)f_m^2,
\quad
\alpha_N=1-O(N^{-1/2}),\quad
\beta_N=\frac{4\pi^2}{N^2}\{1-O(N^{-1/4})\}.
$$

The completed-square inequality (29), applied with frequency $\sqrt{\beta_N/\alpha_N}$, gives a lower bound
$\sqrt{\alpha_N\beta_N}\|f\|^2/2=(\pi/N)\{1-O(N^{-1/4})\}\|f\|^2$.
For the outer vector the potential bound is $cN^{-1/2}\|f\|^2$, larger than $\pi\|f\|^2/N$ for large $N$. The squared cutoff norms sum to the original norm and the IMS error is $O(K^{-2})=O(N^{-3/2})$. Combining these bounds proves the desired uniform lower bound for all normalised vectors, including any optimiser. Equation (R11) gives
$\liminf N(1-\mathcal D_N^{\rm sep})\ge\pi$.

*Proof, attainable upper bound on the separable error.* Use the common sine state in (R10), and rotor amplitudes proportional to
$\exp[-m^2/(4v_N)]$, with $v_N=N/(4\pi)$. Their normalised adjacent products define a Gaussian on the half-integer lattice with variance $v_N$. Poisson summation of the Gaussian gives

$$
C_N:=\sum_m a_ma_{m+1}=1-\frac1{8v_N}+O(N^{-2}),\qquad
\sum_m(2m+1)^2a_ma_{m+1}=4v_N+O(1).
\tag{R14}
$$

For completeness, the sums at integer and half-integer centres differ from their Gaussian integrals by $O(e^{-2\pi^2v_N})$ relatively; differentiating that absolutely convergent Poisson series yields the second-moment statement. On $d\le N^{3/4}$, expanding the explicit finite expression (R10) gives

$$
c_d(b^{\sin})=1-\frac{\pi^2d^2}{2N^2}
+O\!\left(\frac{d^2+d^3+d}{N^3}+\frac{d^4}{N^4}\right).
\tag{R15}
$$

The weighted sums of $d,d^2,d^3,d^4$ are respectively $O(N^{1/2}),O(N),O(N^{3/2}),O(N^2)$. The complement $d>N^{3/4}$ has Gaussian weight $O(e^{-c\sqrt N})$, where $0\le c_d\le1$ bounds its contribution. Therefore this **single product state** has

$$
1-D=\frac1{8v_N}+\frac{2\pi^2v_N}{N^2}+O(N^{-3/2})
=\frac\pi N+O(N^{-3/2}).
\tag{R16}
$$

Its rotor energy is $v_N+O(e^{-cN}N^2)<N$ for large $N$. If finite support is desired, truncation at $|m|\le\lfloor\sqrt N\rfloor$ would lose a nonvanishing Gaussian tail and is **not** used. Truncation at the active rotor interval $|m|\le\lceil N/2\rceil$ instead has exponentially small error and preserves the mean-energy bound. Thus the result also holds with the common mean rotor budget. This proves the matching $\limsup$.

Finally (R5) and $N/(\lfloor\sqrt N\rfloor+1)^2\to1$ give the joint limit; dividing the two positive error limits gives $8/\pi$. The proof establishes the limits. It does not determine a second-order coefficient of the separable optimum or claim that the sine compensator is its exact finite-$N$ optimiser. □

This result answers a shared-resource question that a single-mode coherence maximum leaves open. Independent optimisation of every compensator mode supplies only the upper relaxation. The lower construction proves that one state reaches the same leading constant despite that compatibility restriction. Joint preparation uses a curved, fixed-energy chain instead and has a different leading error. The finite witness (R7), the strict finite separation and the asymptotic squeeze are complementary parts of the contribution.

### 7.6 Exact resonance is a material assumption — T-AR

Replace $H_{RC}/\Delta$ by $M^2+rK_C$, $r>0$, while keeping charge conservation and exact commutation of all effects. Let $\mathcal D_N^{\rm all}(r)$ denote the corresponding joint optimum, without an additional rotor budget away from $r=1$.

**Theorem T-AR (arithmetic resonance classification).** For irrational $r$, the optimum is zero. For a reduced rational $r=p/q$, $p,q\in\mathbb N$,

$$
\mathcal D_N^{\rm all}(p/q)=
\begin{cases}
\cos\!\dfrac{\pi}{2\lfloor\sqrt{\lfloor N/q\rfloor}\rfloor+2},&p=1,\\
1/2,&p\ge3\text{ odd and }N\ge q,\\
0,&p\text{ even, or }p\ge3\text{ odd and }N<q.
\end{cases}
\tag{R17}
$$

*Proof.* The two charge-compatible branches can share energy only if $2m+1=r\ell$ for a nonzero integer compensator displacement $|\ell|\le N$. An irrational ratio permits none. For reduced $p/q$, the condition is $p\mid(2m+1)$ and $\ell=q(2m+1)/p$. An even $p$ permits none. For odd $p\ge3$, permissible rotor edges are spaced by $p$ and cannot be adjacent. All reference-graph components are singletons or isolated pairs. A pair exists precisely when $N\ge q$, by taking $2m+1=p$, and its maximum is $1/2$. For $p=1$, displacements are $q(2m+1)$; decompose the compensator into residues modulo $q$. In each residue the longest effective ladder has at most $\lfloor N/q\rfloor+1$ vertices. Applying the shell argument of T-JB to the longest residue gives the first line. □

Thus the exact-invariance model is discontinuous in the ratio of bare level spacings. More bandwidth alone does not justify using a perfectly resonant formula on a detuned apparatus. Nonresonance under exact conservation is an established limitation [10, §3.2]; (R17) evaluates it for the odd quadratic rotor gaps. It is not a no-go theorem for finite-duration physical experiments.

### 7.7 A finite-time detuning witness — T-DT

To separate exact invariance from finite resolution, keep the state (R6) and the charge-preserving sector-resolved projectors that attain it at $r=1$. Average these effects over a uniformly unknown time in $[-T/2,T/2]$ under $\Delta(M^2+rK_C)/\hbar$. This is a valid POVM and preserves charge. For finite $T$ it generally **does not commute with the detuned Hamiltonian** and therefore lies outside T-AR's exact-invariance class. Let $\tau=\Delta T/\hbar$ and $\operatorname{sinc}x=\sin x/x$, continuously extended at zero. Keeping sector labels gives the exact witness contrast

$$
D_{N,T}(r)=\sum_{m=-n}^{n-1}s_ms_{m+1}
\left|\operatorname{sinc}\!\left(\frac{(1-r)\tau(2m+1)}2\right)\right|,
\tag{R18}
$$

with the nonasymptotic bound

$$
0\le \mathcal D_N^{\rm all}(1)-D_{N,T}(r)
\le\frac{(1-r)^2\tau^2}{24}
\sum_{m=-n}^{n-1}(2m+1)^2s_ms_{m+1}
\le\frac{(1-r)^2\tau^2n^2}{6}.
\tag{R19}
$$

*Proof.* The two states on each occupied edge have detuned energy difference $\Delta(1-r)(2m+1)$. Averaging its phase gives the sinc in (R18); the sign of that real coefficient does not change its sector-resolved TV contribution. For real $x$, $|\operatorname{sinc}x|\le1$ and $1-|\operatorname{sinc}x|\le x^2/6$: the latter follows from $\operatorname{sinc}x=\int_0^1\cos(tx)dt\ge1-x^2/6$. Substitute $x=(1-r)\tau(2m+1)/2$ and use $|2m+1|\le2n-1$ and $\sum s_ms_{m+1}\le1$. □

For this construction, $|1-r|\tau\sqrt N\to0$ suffices for vanishing absolute detuning loss, while $|1-r|\tau N\to0$ suffices to make that loss $o(N^{-1})$ and preserve the joint leading constant. These are sufficient conditions from a bound, not necessary conditions or an optimised clock-cost theorem. At fixed nonzero detuning every occupied edge in this particular state averages to zero as $T\to\infty$, even when another state could attain the isolated-pair optimum of (R17). The limits $r\to1$ and $T\to\infty$ do not commute for this witness. A uniform finite-time response window, state preparation and readout remain declared resources.

### 7.8 Result, contribution and physical boundary

T-JCE through T-DT have the analytic proofs given above. Their proof status is distinct from the question of novelty, which §9 treats separately. The companion verifier attacks finite blocks, incompatible modes, path boundaries and limit normalisations; the exact finite certificate C13 and the roundoff regression V28 have the narrower scopes stated in Appendix B. The reusable contribution is T-SBC together with the strict comparison and the matched constructions, not the mere existence of relational coherence. The prior-art mapping in §9 tests that proposition against the general battery-state-set theorem, asymmetry modes, relational entanglement, reference-frame alignment including multiplicity-assisted constructions, references that store several conserved quantities in separate parts, and recent quantitative WAY bounds.

No finite Z-action has been shown to select $M^2+K_C$, the split $R:C$, the state (R6), or its instrument. The new model adds exact energy conservation to an explicitly supplied energy compensator; it does not derive the original bin controls, supply a free clock, conserve the full interacting action automatically, or establish a cosmological prediction. Its value to the Z-Spin programme is a precise alternative to treating reference preparation as independent local data, with an operational test and a quantified resonance vulnerability.

## 8. Operational interpretation, falsifiers and open physical requirements

### 8.1 Click conditioning, observation window and path dependence

For a saturated budget $\zeta\ge\zeta_{\rm crit}$,

$$
D^{\max}_{h,T}=(1-e^{-\kappa T})\Lambda_w(h),\qquad
(1-D^{\max}_{h,T})\zeta_{\rm crit}
=e^{-\kappa T}\zeta_{\rm crit}
 +(1-e^{-\kappa T})(1-\Lambda_w)\zeta_{\rm crit}.
\tag{35}
$$

This is an exact algebraic identity. It separates missed clicks from the detector-weighted deficit. Let $n_h=e^{-\kappa T(h)}$ and $\varepsilon=\delta h$ with fixed $\kappa,\delta$.

| Observation regime, always $T(h)=B(h)h$ | Limit of $(1-D^{\max}_{h,T(h)})\zeta_{\rm crit}$ |
|---|---|
| Fixed positive $T$, along compatible integer-bin sequences | $+\infty$ |
| $n_h=o(\varepsilon)$ | $1/4$ |
| $n_h/\varepsilon\to c\in(0,\infty)$ | $1/4+c\sqrt3/2$ |
| $n_h/\varepsilon\to\infty$ | $+\infty$ |

The table follows directly from (20)–(22) and (35). For example, choose $B(h)=\lceil 2\log(1/\varepsilon)/(\kappa h)\rceil$ when $0<\varepsilon<1$; then $n_h\le\varepsilon^2$. This explicitly respects the bin constraint. At $\kappa=\delta=T=1$ and $\varepsilon=0.001$, the normalised product is approximately $0.249971$ but the unconditional product is approximately $318.769$. V18 computes both and the three window sequences; it does not infer asymptotics from the samples.

**A different positive-resolution path.** Let $a_m(z)$ be the normalised Gaussian $e^{-m^2/(4z)}$ with $z\to\infty$, and set $\varepsilon=z^{-2}$. Its actual energy is $z+O(z^2e^{-2\pi^2z})$. Poisson summation gives $1-S_1=1/(8z)+O(z^{-2})$. From (25), $1-w_m\le C(\theta_m^2+a^2+\theta_m^4+a^4)$ uniformly, for fixed $\kappa/\delta$ and small $a$. Therefore

$$
0\le S_1-S_w(a(z))\le C\{\varepsilon^2(z+1)+\varepsilon^4(z^2+1)\},\quad
\lim_{z\to\infty}(1-S_w(a(z)))\,\zeta(a(z))=\frac18.
\tag{36}
$$

The first inequality uses $a_ma_{m+1}\le(a_m^2+a_{m+1}^2)/2$ and Gaussian moments. Multiplying its bound by $z$ makes the extra loss vanish along $\varepsilon=z^{-2}$. Every bin width is positive, while $\varepsilon\zeta(a(z))\to0$, so these states are below the saturation energy. A window with $e^{-\kappa T(z)}z\to0$ transfers the same $1/8$ limit to unconditional TV. W03 supplies finite witnesses. Hence $1/4$ is not an unavoidable cost for every finite-resolution experiment.

**Why $1/4$ occurs.** The leading Gaussian objective is $1/(8z)+\varepsilon^2z/6$. Its minimiser is $z_*=\sqrt3/(2\varepsilon)$, where the two terms are equal and the product with $z_*$ is $1/4$. This explains the constant by a kinetic/potential balance. The infinite-lattice proof in §6 is needed to justify the optimisation and moment limit. The numerical contrast with $1/8$ is not evidence that a previous uncertainty limit was exceeded, and it does not price the clock, phase controls or register.

### 8.2 Falsification conditions in the declared model

| ID | Valid claim and comparison | What would contradict it |
|---|---|---|
| F1 | Same state, hazard, Hamiltonian, integer bins and actually applied control (11a); include all flags and no-click | Direct Born TV differs from (11) beyond demonstrated numerical or experimental error |
| F2 | Same weights; optimise over the budget $\zeta\ge\zeta_{\rm crit}$ | A feasible score exceeds $\Lambda_w$, or the top vector fails to realise it; unconditional TV includes the prefactor in (35) |
| F3 | Broad-Gaussian sequence under the same static readout | Its score fails to vanish while the assumptions of W01 hold |
| F4 | T-CERT encloses the **optimum**, not every observation | A feasible score exceeds its upper endpoint, or a demonstrated global optimum lies outside the interval; the supplied feasible witness validates the lower endpoint |
| F5 | Fixed $\kappa,\delta>0$; saturated states; $h\downarrow0$ | A rigorous asymptotic incompatibility with (20)–(22); finite-$h$ deviations alone are not a contradiction |
| F6 | Formal second-order proposal (34) only | A proved differing coefficient or controlled asymptotic counterexample refutes C-2, not the leading theorem |
| F7 | Unconditional TV and the specified window regime | A contradiction to (35) or its stated limiting regime |

For F4, $|0\rangle\langle0|$ is feasible and has zero score. It may lie below every positive optimum lower endpoint without any inconsistency. For a finite-$T$ **fixed-phase, time-discarded** detector, use the finite-window weights $\kappa|1-e^{-(\kappa+i\omega_m)T}|/[\sqrt{\kappa^2+\omega_m^2}(1-e^{-\kappa T})]$ and the common click prefactor. The static certificates in T-CERT use the $T=\infty$ weights (13); multiplying those intervals by $1-e^{-\kappa T}$ alone does not turn them into certificates for a different finite-window response. A prefactor rescaling is valid only when the normalised weights are actually the same (for example an independent input-blind erasure of the declared static output). This refines the audit's prefactor instruction using the instrument definition.

These are model-level tests. They do not falsify or confirm the entire Z-Spin programme.

### 8.3 What this result does not supply

The mathematics of §§2–7 is a statement about a declared model. Four requirements separate it from a physical claim, and none is discharged here.

| Requirement | State of the art in this paper | What would discharge it |
|---|---|---|
| An action-derived instrument | The detector of §§2–6 and the invariant effects of §7 are *declared* inputs; their phase controls, hazard and split are assumptions. | Derive the operation space and the instrument, or an equivalence class of instruments, from a finite action rather than assuming them. |
| A derived preparation and subsystem split | The comparison in §7 prices separability across one explicitly chosen physical split $R:C$. | Derive the split, the admissible preparations and their costs; a different factorisation defines a different optimisation problem (§8.4). |
| A physical record and its stability | (R3) identifies which joint coherences a single-shot invariant measurement could use. | Exhibit a single definite record with Born weighting in a physical carrier and environment, with a stated stability criterion. |
| A normalised packet and error budget | Appendix A computes a conditional witness on four selected states with an explicitly declared instance. | Supply one actual model and one normalised packet or window and derive $\epsilon_\pm$ so that $\nu_{\rm det}\eta\lvert\cos\beta\rvert-\epsilon_+-\epsilon_->0$. |

Refining $\eta$ inside an arbitrarily chosen four-state detector cannot close any of these. Sections 2–8 survive the removal of every Z-Spin label, which is precisely why their role is SUPPORT/METHOD rather than a physical bridge.

### 8.4 Z-Spin through relational preparation, boundary references and return histories

The initial-idea document asks how change, return, structure and observation can coexist. Mission 1.7 §1.3 turns this into a heuristic about return without repetition; the 11D seed separates existence, dynamics and observation. None identifies a measured rotor, compensator or pointer. The following are **typed research hypotheses**, with the exact conditional contribution of §7 distinguished from the proposed physical map.

| Perspective and primary connection | Concrete Z-Spin question and mathematical interface | Result available here | Missing map and falsifier |
|---|---|---|---|
| Relational information; [de la Hamette–Ludescher–Müller, Theorem 1](https://arxiv.org/pdf/2112.00046), [Loveridge, §§4.4–5.1](https://arxiv.org/pdf/2006.07047) | Can a seam's observable information be a joint matrix element of a carrier and its reference, with locally uninformative marginals? Candidate interface: an action-derived state and invariant effect mapped to $\rho_{RC}$ and (R3). | The stationary $N=1$ witness has zero record after replacement by its marginal product but joint TV $1/\sqrt2$. T-SB supplies a separability threshold. | Derive the actual algebras, generators and state. If the admissible effects cannot read the resonant matrix elements, the proposed physical record vanishes. A relational entropy measure is not automatically the TV in this paper. |
| Boundary reference rather than a numerical seam label; [Carrozza–Höhn, §4.2 and §6.2.2](https://arxiv.org/html/2109.06184v4) | Can the finite Z-action supply a boundary reference and a dressed observable, then select an instrument on it? A candidate map must send a physical seam algebra into $\mathcal B(SRC)$ and preserve the relevant conserved quantities. | The required output of such a map is explicit: the edge selection (R2), bandwidth $N$, and admissible readout. | Derive boundary conditions and the physical split from the actual action. Different admissible boundary choices giving inequivalent output TV would refute uniqueness of the proposed selector. Boundary dressing alone does not derive a quantum instrument. |
| Return with changed reference history; [Collins et al., §§II, VI](https://arxiv.org/html/2603.25485v1) | Can a closed-base return update a persistent reference and therefore alter the next record? Specify a channel on a retained reference, rather than reset it silently after each traversal. | Equation (R3) identifies which joint coherences the next single-shot measurement could use. It supplies no repeated-use channel or memory theorem. | Construct one charge/energy-preserving interaction with a neutral outcome register and follow its conditional reference states. If the claimed update is gauge only or leaves all accessible statistics fixed, that return carries no operational memory. |
| A compensator versus a clock; [Woods–Silva–Oppenheim, abstract](https://arxiv.org/abs/1607.04591), [Marvian–Spekkens, §II](https://arxiv.org/pdf/1312.0680) | Can the proposed physical system supply timing, rather than merely an energy-matching coherence? | T-AR exposes exact resonance dependence; T-DT gives an explicit finite-window response. The joint optimum is stationary and has no constructed tick observable. | Derive timing resolution, backreaction, preparation and a physical response kernel. The bound (R19) fails to justify the ideal leading error unless detuning is controlled on its stated scale. |
| Fixed subsystem split and changing description; [Giacomini–Castro-Ruiz–Brukner](https://arxiv.org/html/1712.07207v2) | Does a proposed frame change preserve the accessible algebra and resource split used to price a Z-Spin reference? | The entanglement advantage is defined for one physical $R:C$ split and shared POVMs. | Transport states, observables, generators and subsystem identification together. Calling an entangled state a product after changing the split does not implement a free preparation in the original experiment. |

The first row narrows a live construction question: local state data need not determine the available reference record. The second exposes the instrument-selection requirement of §8.3. The third preserves Mission's return heuristic while keeping it separate from an actual memory dynamics. The fourth gives an immediate kill test for a proposed compensator. These are more specific research interfaces, not inferred existence of new cosmological degrees of freedom.

**The physical split is part of the hypothesis.** The alignment protocols [21, (17)–(19)] and [22, (10)–(11)] use representation–multiplicity correlations within the transmitted system. Their relevance here is a constraint on interpretation: §7 prices separability across the explicitly chosen physical $R:C$ split, not across every possible factorisation. No universal need for remote entanglement follows. A proposed Z-Spin interpretation must identify the physical preparation operations and observable algebras before applying the separability threshold; an internal-degrees encoding with different preparation constraints requires a new comparison. [Primary representation–multiplicity construction](https://arxiv.org/pdf/quant-ph/0405095v2), [internal-correlation construction](https://arxiv.org/pdf/quant-ph/0405082v2).

For a proposed finite Z-model, an admissible next calculation would first supply its Hamiltonian, conserved charge, preparation channel and output instrument on one normalised state. It would then establish a controlled embedding into (R1), or compute the actual graph if that embedding fails. Only afterwards could a measured contrast be compared with (R11). Locked constants cannot be inserted as $N$, $r$ or $\tau$ without a derived dimensional and spectral map. The formal contraction phase, holonomy phase and physical time increment remain different typed objects. The requirements of §8.3 remain open.

## 9. Relation to prior work

### 9.1 Source comparison at assumption–statement level

#### 9.1.1 The central claim and its strongest possible subsumption

The comparison below is bounded to the declared apparatus, preparation constraint and error functional. It covers the nearest identified battery theorem, the asymmetry and discrimination methods, the relational interpretation and recent general WAY bounds. Located passages were opened in the primary sources; a title or abstract match alone is never used to establish novelty.

| Primary result actually inspected | Assumptions, object and conclusion compared | Contribution retained or excluded here |
|---|---|---|
| [Navascués–Popescu, §5.2; Appendix D, Theorem 2, (81)–(83); §5.3, (32)–(34)](https://arxiv.org/pdf/1211.2101) [10] | Energy-conserving qubit measurements are characterised through battery coherence, including optimisation over a specified set of battery states. Finite chains yield sine states and a cosine ceiling. | T-JCE and the chain method of T-JB fall within this framework by the explicit mapping below. They cannot carry the novelty claim. The additional question is the evaluated separable set on a nonlinear rotor–compensator spectrum. |
| [Marvian–Spekkens, §II, (2.8)–(2.16), Propositions 1 and 4](https://arxiv.org/pdf/1312.0680) [11] | Symmetry components compose by matching modes; averaging a group action multiplies modes by Fourier coefficients. | Mode matching in (R2) and the sinc mechanism are specialisations. A framework for modes alone does not evaluate the coupled maximum over one $b$ in (R8). |
| [Ahmadi–Jennings–Rudolph, §II.E and §III.B, (17), (19)](https://arxiv.org/pdf/1209.0921) [12] | Optimal discrimination of twirled ensembles and optimal phase-reference states already connect WAY restrictions to operational asymmetry. | Binary discrimination, amplitude positivity and a sine-state construction are excluded as standalone novelty. The rotor's varying odd gaps and shared compensator constraint require the extra comparison (R8)–(R16). |
| [de la Hamette–Ludescher–Müller, Definition 1, (2)–(3), Theorems 1–2](https://arxiv.org/pdf/2112.00046) [13] | For their internal reference-frame setting, conditional asymmetry defined through a Haar average is related to Rényi-2 entanglement; perspective changes constrain the comparison. | This supplies an established relational interpretation. Its objective is not the binary TV (R3), and no identification of its entropy with $\Gamma_N$ is asserted. |
| [Loveridge, §4.4, theorem (21) and (22); §5.1](https://arxiv.org/pdf/2006.07047) [19] | Localised references approximate non-invariant observables by relational ones; the apparatus also provides a reference. | The interpretation of a detector as a reference is established. The located approximation result does not specify the present finite-band separable frontier or its leading constant. |
| [Hokkyo–Tajima, Theorem 1, (7); Theorems 2–3](https://arxiv.org/pdf/2607.09075) [16] | Worst-case purified-distance measurement/gate bounds constrain the fidelity of symmetry-transformed resources, for unitary and antiunitary symmetries. Our objective is the TV of a fixed binary input pair. | The general limitation is broader than continuous energy conservation. The inspected bounds do not evaluate (R8). No claim is made to improve them as general inequalities. |
| [Giacomini et al.](https://arxiv.org/html/1712.07207v2) [14]; [Collins et al., §§II, VI and Appendix A](https://arxiv.org/html/2603.25485v1) [15] | Reference changes alter subsystem descriptions; networks expose the physical role of correlated preparation histories. | These support the fixed-split and preparation-history caveats of §8.4. They do not supply a repeated-use theorem for this instrument. |
| [Carrozza–Höhn, §4.2, (62)–(64); §6.2.2](https://arxiv.org/html/2109.06184v4) [17] | Boundary reference fields dress gauge quantities; the boundary action depends on the admitted boundary conditions/polarisation. | This is a candidate interface for the seam, not a derivation of the Z-action or of a Born instrument. |

**An explicit encompassing map to [10] (our inference).** Fix an irrational $\alpha>0$ and define
$G_{RC}=M+\alpha(M^2+K_C)$ and $G_{SRC}=N_S+G_{RC}$.
Since total charge and shell energy are integers, two basis states have equal $G_{SRC}$ eigenvalues exactly when both their charge and energy coincide. Its spectral pinching therefore equals $\mathcal G_{Q,H}$. The reference spectrum $m+\alpha(m^2+k)$ is nondegenerate and bounded below; its unit-spaced links are precisely (R2). Thus a single effective-generator battery description already includes our two-generator block problem. This is a mathematical correspondence, not a claim that $G_{SRC}$ is the physical Hamiltonian. In [10]'s battery-state-set formulation, choosing the state set to be separable across the specified $R:C$ split leaves (R8) as an optimisation still to be evaluated.

**Reference-frame alignment.** To avoid overloading $N$, write $n_s$ for the number of transmitted spin-$1/2$ systems in the following sources. Their $n_s$ is not the compensator bandwidth $N$ in (R1). The passages below were read in the primary PDFs during v1.3; [23] is a contextual review of the same work, not an independent discovery or another vote for novelty.

| Primary passage | Assumptions and optimised object | Method and conclusion | Precise comparison with §7 |
|---|---|---|---|
| [Bagan–Baig–Muñoz-Tapia, (1)–(3), (15)–(19), (23)](https://arxiv.org/pdf/quant-ph/0303019v2) [20] | Shared entangled state of two $n_s$-spin registers; unknown SU(2) rotation on one register; collective measurement; Haar-averaged frame-alignment error $\bar h=6-2\langle\chi_1\rangle$. | A tridiagonal problem gives sine coefficients and $\bar h_{\min}=4[1-\cos(2\pi/(n_s+3))]\sim8\pi^2/n_s^2$. | Entanglement-assisted reference information and sine/cosine spectra are established. These equations do not impose the present quadratic energy matching and one compensator state shared by all odd gaps. |
| [Chiribella–D'Ariano–Perinotti–Sacchi, (1)–(4), (8), (14)–(19)](https://arxiv.org/pdf/quant-ph/0405095v2) [21] | $n_s$ spins; unknown SU(2) rotation; representation and multiplicity spaces both available; no entanglement between sender and receiver is required. | Correlations between representation and multiplicity spaces yield a fixed tridiagonal matrix, with $\bar e\sim8\pi^2/n_s^2$. | The tensor factors here differ from the fixed physical $R:C$ split. This is a direct warning against interpreting T-JB as a universal necessity of distant-party entanglement. |
| [Bagan–Baig–Muñoz-Tapia, (7)–(11), (17)–(22)](https://arxiv.org/pdf/quant-ph/0405082v2) [22] | Reference alignment or unknown qubit-gate estimation using internal degrees of $n_s$ spins. | Multiplicity correlations replace spectator-spin correlations; for the odd-$n_s$ sequence treated explicitly, a tridiagonal comparison gives $\langle\chi_1\rangle_{\rm opt}=3-4\pi^2/n_s^2+O(n_s^{-3})$. | A closely related resource saving already exists. The present contribution cannot be “internal correlations can replace an external reference” or the existence of a matched spectral squeeze. |
| [Bartlett–Rudolph–Spekkens, §V.D.2, (5.70)–(5.80); §V.F, (5.97)](https://arxiv.org/pdf/quant-ph/0610030v3) [23] | Review of covariant alignment and ancilla-assisted parameter estimation. | Organises the character, multiplicity and spectral constructions in [20]–[22]. | Establishes the adjacent baseline and terminology; it is not counted as independent evidence for a result already obtained in those primary papers. |

**Response to the strongest subsumption objection.** The effective-generator map above deliberately concedes more than a similarity: the battery-state-set expression [10, Appendix D, Theorem 2, (81)–(83)] applies to this invariant-measurement problem. Substituting the separable state set gives the variational question (R8); it does not, by that substitution alone, evaluate it. The following identifies exactly where the claimed additional knowledge enters.

| Stage | What the encompassing framework or alignment spectra already supply | Additional statement and proof actually present here |
|---|---|---|
| Measurement reduction | Optimise adjacent coherence along energy-compatible chains; a finite unrestricted path has a cosine ceiling. | T-JCE and the path part of T-JB are credited as specialisations. They are excluded as standalone central novelty. |
| Fixed preparation constraint | The battery set can be declared to be separable; the general theorem still contains an optimisation over that set. The alignment matrices in [20]–[22] have coefficients fixed by their representation problem. | In (R8), all coefficients $c_{\lvert2m+1\rvert}(b)$ must come from **one** normalised vector $b$. Thus $\max_b\lambda_{\max}(A[c(b)])$ remains to be solved, rather than the eigenvalue of one already specified matrix. |
| Finite separation | The joint path spectrum identifies where equality would have to occur. | The descending-support argument in §7.3 excludes every product vector from the top eigenspace and proves strict separation for **all** $N\ge1$, including mixtures by the stated compact reduction. At $N=3$, W05 shows why the independently optimal modes cannot simply be assembled. |
| Sharp bandwidth cost | Single-mode cosine bounds and discrete harmonic estimates are established tools. | Equations (R13)–(R16) control the varying floor-dependent gap envelope uniformly and produce one admissible Gaussian–sine product. The two bounds match at $\pi/N$, including the additional mean rotor budget, and give the error ratio $8/\pi$ against the joint shell construction. |
| New usable decision within this model | A generic battery formula supplies a criterion conditional on an unevaluated set optimum. | An output TV exceeding $\lambda_{\max}(A_{u,N})$ excludes all separable preparations under (R1); the stationary state (R6) gives an explicit attainable comparison. At $N=4$, the thresholds $\sqrt7/4<\sqrt3/2$ are exact even though the separable optimum is not known in closed form. |

This is a non-subsumption **argument about the inspected results**, not a theorem that no other paper exists. Merely observing U(1) rather than SU(2), binary TV rather than estimation loss, or $N^{-1}$ rather than $n_s^{-2}$ would not suffice. Nor is “not one fixed Jacobi matrix” sufficient by itself: known tools can solve a new variational problem. The substantive claim is the completed strictness proof and matching constrained optimum with an operational consequence. The finite sine construction is not even exact at every small $N$ (§7.4), so its asymptotic optimality cannot be obtained by simply declaring the familiar sine vector globally optimal in (R8).

An attempted transfer from [21] or [22] must preserve the physical state set, bandwidth, conserved operators and output statistic. Relabelling representation and multiplicity degrees as $R$ and $C$ without transporting those constraints would change the optimisation problem. Conversely, a source that **does** transport them and yields the same strict or sharp comparison would subsume the corresponding claim; it need not reproduce the whole manuscript. No claim of improving the general battery theorem, a general WAY bound, or the SU(2) protocols is made.

The question this comparison leaves is whether the evaluated constraint is a substantive addition or a routine specialisation of the encompassing framework. Section 9.3 states the answer taken here, together with the evidence for it and the conditions that would reverse it.


#### 9.1.2 References that store several conserved quantities in separate parts

A further adjacent family treats a reference system that is deliberately **split into separate parts, one per conserved quantity**. This is the closest published framing to the fixed split $R:C$ used here, so it is mapped at primary-text level. The passages were opened in the primary sources; the comparison in the third column is our inference.

| Primary passage | Assumptions, object and conclusion | Precise comparison with §7 |
|---|---|---|
| [Popescu–Sainz–Short–Winter, Theorem 1 with (1)–(3); construction (4)–(6); error bounds (12)–(14)](https://arxiv.org/pdf/1908.02713) [24] | A reference frame of spin-$1/2$ particles is *assumed* to have product form $\rho_R=\rho_R^{(x)}\otimes\rho_R^{(y)}\otimes\rho_R^{(z)}$, one part per component of total angular momentum; the conserved quantities are **non-commuting**. For every $\varepsilon,\delta>0$ such a frame and a joint conserving unitary exist which implement an arbitrary system unitary to accuracy $\varepsilon$ with separation $\delta$; the error is $O(1/N)$ after $N$ steps of $O(1/N^2)$. The statement is **achievability**: the product form sits inside the existential quantifier, and no converse, no optimisation over frame states and no comparison against an entangled frame appears. | The question "can different conserved quantities be stored in different parts of the reference?" is genuinely anticipated here, and this is the correct citation for it. What is not anticipated is the **optimisation**: there the product form is a sufficient construction, here it is a constraint over which the optimum is taken and then compared with the joint optimum at equal spectrum and equal allowed effects. The symmetry class (non-commuting SU(2) components versus a commuting charge/energy pair), the task (unitary synthesis versus binary discrimination) and the figure of merit (operator distance versus unconditional total variation) all differ. No quadratic rotor spectrum, position-dependent Bohr gap, multi-lag autocorrelation constraint or constant-factor gap appears. |
| [Guryanova–Popescu–Short–Silva–Skrzypczyk](https://arxiv.org/abs/1512.01190) [25] | The commuting-case antecedent that [24] cites. Each conserved quantity is extracted into **its own battery**; the results are thermodynamic, a generalised second law $\sum_i\beta_iW_{a_i}\le-\Delta\tilde F_S$ for extraction against a generalised bath. | Establishes separate per-charge batteries for commuting conserved quantities, the structural setting closest to (R1). Its objective is extraction against a bath, not single-shot discrimination; it contains no optimisation over separable versus entangled reference states, no rotor with a quadratic spectrum and no total-variation figure of merit. |

A separate line of work optimises directly over **separable reference states**, and is the closest prior art to the optimisation carried out in §7.4.

| Primary passage | Assumptions, object and conclusion | Precise comparison with §7 |
|---|---|---|
| [Paterek–Kurzyński–Oi–Kaszlikowski, §5, (11)–(12); §7, (16)–(19)](https://arxiv.org/pdf/1004.5184) [26] | Under a particle-number superselection rule, a shared reference enables CHSH violation through the coherence $\mathcal V=\operatorname{Re}\operatorname{tr}[(R_+\otimes R_-)\rho_{A'B'}]$, with $S=2\sqrt{1+\mathcal V^2}$. Optimising over **separable** references, the objective factorises exactly as $\mathcal V=f_Ng_M$ with $f_N=\sum_n\mathfrak a_n\mathfrak a_{n+1}$ and $g_M=\sum_m\mathfrak b_m\mathfrak b_{m+1}$: two independent nearest-neighbour sums over disjoint amplitude vectors at the single fixed shift $\Delta=1$. Each factor is maximised by a sine vector, with $\max f_N=\cos[\pi/(N+2)]$. For the minimal two-particle frame there is a finite entangled/separable gap ($\mathcal V\le1/2$ against $\mathcal V\le1/4$); for large frames the separable optimum approaches the maximum. | This is the nearest prior optimisation over separable references, and the sine optimiser together with the cosine ceiling is credited to it and to [10]; §7.4 claims neither. The difference is one of **coupling, not technique**. There the separable objective splits into two one-lag sums over disjoint vectors, so it reduces to independent tridiagonal eigenproblems with a closed-form sine solution and no competition between lags. In (R8) a single vector $b$ must supply $c_{\lvert2m+1\rvert}(b)$ at **every** odd lag at once, which is why the upper relaxation and the lower construction have to be matched rather than solved. Their setting also carries one superselection charge with no accompanying energy constraint and no quadratic spectrum. Finally, the separable penalty there **vanishes** for large frames, whereas the penalty established in §7.5 persists as the constant factor $8/\pi$. |

**What this family settles and what it leaves.** It settles that separate storage per conserved quantity is an established question with an established positive answer in both the commuting and the non-commuting case, so no novelty may be claimed for that framing, and §7 does not claim any. It settles further that optimising over separable references, and finding sine optimisers with a cosine ceiling, is itself established practice [26]. It leaves untouched the quantity actually computed in §§7.3–7.5: the **value** of the optimum when one shared vector is coupled to every odd lag at once, its strict finite-$N$ separation from the joint optimum, and the sharp leading constant that does not vanish with bandwidth. In the language of [10], this literature supplies an admissible battery-state set; it does not evaluate $\tau$ on it.

#### 9.1.3 The detector sections and withdrawn assertions

For §§2–6 a targeted primary-source comparison was performed, not an exhaustive absence search. Directly checked: Hradil et al. 2006, (7), (9)–(13); Parhizkar–Barbotin–Vetterli, Lemmas 2–3 and the adjacent discussion, §3.2 (17)–(18); DLMF 28.8.1; Mišta–Mišta–Hradil v3, (4)–(5), §III (29)–(32); Folge et al., title/abstract and relevant finite-window framing; Klein–Rosenberger, Hypothesis 1.1 and Theorem 1.3. Earlier reported full readings are historical provenance and are not claimed as fresh readings here.

| Primary source and exact locator | Correspondence and remaining distinction |
|---|---|
| [Hradil et al. 2006, (7), (9)–(13)](https://arxiv.org/pdf/quant-ph/0605137) | Circular uncertainty and a variational problem at fixed dispersion **or fixed angular-momentum variance** are already present. T-EC/T-ASY do not introduce energy constraints as a new idea. |
| [Parhizkar et al., Lemmas 2–3, §3.2 (17)–(18)](https://arxiv.org/pdf/1302.2082) | Nonnegative-amplitude reduction, second-moment optimisation at fixed adjacent coherence and the equivalent inverse frontier precede this work. The unweighted problem (8) is imported/specialised. |
| [DLMF 28.8.1](https://dlmf.nist.gov/28.8#E1) | Mathieu large-parameter coefficients supply (9); the mapping is displayed in §3. |
| [Mišta–Mišta–Hradil 2024, (4)–(5), (29)–(32)](https://arxiv.org/html/2403.02498v3) | The variational unweighted problem and moment-based rotor uncertainty family overlap substantially. Both their objective and $\langle a,A_wa\rangle$ involve quadratic forms; that label cannot prove non-subsumption. Compare the actual hopping coefficients, state dependence, constraints and operational objective. |
| [Folge et al. 2026](https://arxiv.org/pdf/2602.20962) | Finite observation windows and rotor-based joint time/frequency estimation are adjacent. Their estimation objective is not identified here with the binary TV of (11). The first author is **P. Folge (Patrick Folge)**. |
| [Klein–Rosenberger, Hypothesis 1.1; Theorem 1.3](https://arxiv.org/pdf/1706.06357) | For smooth reversible difference-operator coefficients, nondegenerate wells and the stated uniform bounds, low eigenvalues have harmonic-oscillator asymptotics $E_k(\varepsilon)=\varepsilon e_k+O(\varepsilon^{6/5})$. This is the strongest identified methodological overlap. |

For our own operator, take $x=\varepsilon m$ and the unitarily reindexed $H_\varepsilon=I-A_w$ on $\ell^2(\varepsilon\mathbb Z)$. The edge response tends to $g(x)=|\sin x/x|$, $g(0)=1$. The local kinetic symbol is $g(x)(1-\cos\xi)$ and the potential is $1-g(x)$. Near $(0,0)$ their sum is $\xi^2/2+x^2/6+O(\xi^4+x^2\xi^2+x^4)$. Thus the leading oscillator and $1/4$ balance are expected from standard harmonic approximation.

The global correspondence requires additional care: $g$ is not smooth at nonzero zeros of $\sin x$, its hopping vanishes there, and uniform expansion/positivity hypotheses cannot be imported globally without a modification-and-localisation argument. Section 6 supplies a direct whole-lattice eigenvalue and second-moment proof. The cited general eigenvalue theorem alone does not establish the particular unbounded-moment estimate (21), yet the need for that estimate does not by itself prove a significant new contribution. **The detector contribution of §§2–6 remains OPEN-NOVELTY as a standalone contribution; it is not the central novelty claim of this paper.**

Two earlier claims are withdrawn: that prior work carries no energy budget, and that a quadratic form versus a Jacobi matrix by itself proves non-subsumption. A source need not contain every section of this paper at once to subsume a central claim. Not read in full: Breitenberger; Řeháček 2008; Hradil 2010; Kim 2000; Nam 2013. None of these is used as affirmative evidence of novelty.

### 9.2 Summary of claims

PROVEN refers to the displayed mathematical argument under the stated assumptions; it is not a declaration of formal verification, of novelty, or of physical realisation. No row of the companion verifier is a proof object.

| Claim | Mathematical status; proof | Novelty class | Assumptions, strongest attack and reversal |
|---|---|---|---|
| T-CAP | PROVEN, §2 | SPECIALIZED | Every density operator; charge twirl. Absolute summability prevents an infinite-support gap. |
| T-EC | PROVEN / IMPORTED-PROVEN with DERIVED mapping, §3 | IMPORTED/SUBSUMED | Finite second moment; pure-amplitude domination is essential when phases cancel. |
| T-ASY | IMPORTED-PROVEN with explicit mapping, §3 | IMPORTED | $\zeta\to\infty$; no finite-energy exact Gaussian claim. |
| L-CAL | DERIVED, §4 (11a) | OPEN-NOVELTY for the apparatus integration | Known reference phases; common hazard; preset sector/bin controls. Reverse if direct output probabilities disagree. |
| T-WR | PROVEN, §5.1 | SPECIALIZED method / OPEN-NOVELTY integration | Any $0\le w_m\le1$; attained primal, infimum dual; operator compactness not assumed. |
| T-SAT | PROVEN, §5.2 | OPEN-NOVELTY | Positive decaying weights as in (12)/(13); finite second moment of top vector; exact-energy nonattainment above threshold. |
| T-CERT | CERTIFIED, four cases in §5.3 | METHOD; OPEN-NOVELTY as an independent contribution | Exact feasible witness plus rational LDL/Schur upper bound. General finite-bin cases remain numerical. |
| T-BL | PROVEN by replacement proof, §6 | Standard harmonic method / OPEN-NOVELTY contribution | Fixed positive $\kappa,\delta$; complete exterior envelope and moment summation. Any violation of L6 or a hidden uniformity assumption reopens (21)–(22). |
| LOCAL-TAYLOR | DERIVED, (34a) | Mathematical correction | Joint local expansion only; not a spectral remainder estimate. |
| C-2 | HYPOTHESIS, (34) | OPEN | Formal perturbation and diagnostics only. |
| RECORD-SCOPE | DERIVED, (35)–(36) and their arguments | Scope correction / SPECIALIZED | No-click probability and limit path fixed explicitly; not a universal cost law. |
| A-CUR | DERIVED-CONDITIONAL, Appendix A | SPECIALIZED METHOD | A self-chosen numerical instance of the band and profile *forms* declared upstream (provenance table in Appendix A); packet, full-current error and action-selected detector remain OPEN. |
| T-JCE | PROVEN, §7.2 | SPECIALIZED / encompassed by battery framework | All trace-class states; exact simultaneous pinching, absolute convergence and blockwise Helstrom readout. V20 attacks confusion with charge-only pinching. |
| T-JB | PROVEN, §7.3 | Path ceiling SPECIALIZED; the strict comparison is part of the assessed T-SBC contribution, with no separate priority claim | Same fixed split and allowed effects; finite $N\ge1$ strictness, $N=0$ degeneracy, no hidden postselection. |
| T-SB | PROVEN, §7.4 | Single-mode bound IMPORTED/SPECIALIZED; common-state bracket DERIVED | Convex separable closure, positive pure products, shared compensator. Modewise upper envelope is not asserted attainable. |
| T-SBC | PROVEN, §7.5 (R12)–(R16) | Central contribution; novelty ASSESSED-NOVEL against the inspected results (§§9.1.1–9.1.2, §9.3), which is not a proof of worldwide absence | Integer $N\to\infty$, exact resonant model; uniform floor-envelope localisation and one product construction. Same leading limits under common mean rotor budget. A failed uniform bound or subsuming exact optimisation reopens the claim/status. |
| T-AR | PROVEN, §7.6 | DERIVED arithmetic classification; general nonresonance SPECIALIZED | Exact effects, reduced rational/irrational spacing ratio; no extra rotor budget away from $r=1$. Not a finite-time physical no-go. |
| T-DT | DERIVED, §7.7 | Fourier averaging SPECIALIZED; explicit witness/bound DERIVED | Uniform finite-time window, fixed resonant state and sector labels; generally outside exact detuned invariance. Sufficient scaling conditions only. |

### 9.3 What is new, and what is not

Three statements summarise the comparison above, and each is bounded by what was actually inspected.

**Credited to prior work.** The measurement reduction of §7.2 and the path spectrum behind the joint ceiling (R5) are a specialisation of the battery framework of [10]: with the effective-generator map of §9.1.1, the two-generator block problem here is contained in that framework, and $\mathcal D_N^{\rm all}=\cos[\pi/(2n+2)]$ is its finite-chain cosine ceiling. Sine states, tridiagonal reductions and matched spectral squeezes are established tools, present in [10] and, for SU(2) frame alignment, in [20]–[22]. Optimising over separable reference states is established as well: under a superselection rule [26] solves exactly that problem, obtains the sine optimiser and the ceiling $\cos[\pi/(N+2)]$, and finds a separable penalty that vanishes with frame size. The idea of storing different conserved quantities in different parts of a reference is established in [24]–[25]. None of this is claimed as new.

**Claimed as the addition.** In (R8) all coefficients $c_{\lvert2m+1\rvert}(b)$ must be produced by **one** normalised compensator vector, so the separable problem is a coupled maximisation over two vectors rather than the top eigenvalue of a prescribed matrix. What is added is its evaluation: the descending-support argument of §7.3 excludes every product vector from the top eigenspace and gives strict separation for all $N\ge1$ including mixtures; the uniform floor-envelope bound and the single Gaussian–sine construction of §7.5 match at $\pi/N$, including under a common mean rotor budget, and yield the error ratio $8/\pi$ against the joint shell construction. The modes genuinely conflict at finite $N$ — W05 at $N=3$, and the exact witness C13 shows the common sine state is not even optimal there — so the matching of the two bounds is not a restatement of single-mode optimality. It is also not an instance of the factorised separable problem of [26]: because one vector serves every odd lag, the objective does not split into independent single-lag factors, and the resulting penalty stays at order $1/N$ with a constant strictly larger than the joint one instead of vanishing. The operational consequence is a computable threshold: an output contrast exceeding $\lambda_{\max}(A_{u,N})$ excludes every separable preparation under (R1), and at $N=4$ the exact thresholds $\sqrt7/4<\sqrt3/2$ separate the two classes in closed form.

**What the comparison cannot establish.** No inspected source evaluates the separable optimum, the shared-state odd-lag constraint, the strict finite-$N$ separation, or the constant $\pi$; but this is a statement about the results that were opened, not a proof that no such source exists. A paper that transports the state set, bandwidth, conserved operators and output statistic of (R1) and reaches the same strict or sharp comparison would subsume the corresponding claim, and it need not reproduce the rest of this work to do so. Merely observing U(1) rather than SU(2), a binary total variation rather than an estimation loss, or $N^{-1}$ rather than $n_s^{-2}$ would not suffice, and neither would the observation that the problem is not one fixed Jacobi matrix: known tools can solve a new variational problem. No improvement of the general battery theorem, of a general WAY bound, or of the SU(2) protocols is claimed.

### 9.4 Objections considered

| Strong attack | Actual response | Remaining scope |
|---|---|---|
| Two conserved quantities merely rename one battery generator | The irrational effective-generator map in §9.1 explicitly concedes this encompassing description. | Only the evaluated separable problem is claimed as the addition. |
| The joint advantage spends more bandwidth, hides postselection or changes the POVM class | Both preparations use $k=0,\ldots,N$ and exactly the same invariant effects; TV is unconditional. The leading comparison survives a common mean rotor budget. | Total preparation cost, total mean energy and a common hard rotor cutoff are not claimed to be equal. |
| Independently optimised modes are illegally combined into one compensator | (R11) is an upper relaxation. W05 demonstrates incompatibility at $N=3$; (R10) uses one explicit common state. | The exact finite-$N$ separable optimum is open for $N>2$. |
| A finite plot cannot prove a sharp constant | The uniform discrete upper relaxation bound and the Gaussian–sine lower construction prove both sides in §7.5. | V24/V27 are diagnostics and finite witnesses, not a universal proof certificate. |
| Exact resonance is unstable or a rational floating-point accident | T-AR is proved arithmetically; C11 enumerates rational cases with exact arithmetic. Finite-time T-DT is explicitly a different measurement class. | No robustness claim for an unknown physical Hamiltonian or response kernel. |
| A stationary marginal cannot serve as a free clock | No clock is asserted. Joint matrix elements carry the matched reference record; timing and preparation are independent obligations. | D-HCLK-001 and the action-selected apparatus remain OPEN. |

Each row states an objection that would, if sustained, remove or narrow the contribution, together with the specific response and the scope that remains open. None of them is answered by the number of verification rows.

## 10. Scope of the results

The central new result is a matched preparation comparison: $1-\mathcal D_N^{\rm sep}\sim\pi/N$ while $1-\mathcal D_N^{\rm all}\sim\pi^2/(8N)$. It quantifies a cost of separability across one fixed physical split and yields finite nonseparability thresholds. Exact resonance enables the curved stationary chain; detuning reveals a real limitation of that construction. The finite-time witness is a controlled alternative model, not a way to evade its assumptions silently.

The earlier detector results remain useful and fully integrated. Their click-conditioned saturation product is $1/4$; unconditional TV depends on the no-click window, and a different non-saturating path has product $1/8$. These constants have different denominators and limits from the bandwidth comparison. The repaired local Taylor series still does not prove the second-order spectral conjecture.

The extended Z-Spin interpretation identifies a precise role for joint reference preparation, boundary observables and preparation history. It supplies no action-selected compensator, clock, stable event or observation. What is added relative to the nearest prior results, and what is credited to them, is stated in §9.3, together with the conditions that would reverse either judgement. The physical limitations of §8.3 do not obstruct reuse of the mathematical results within the declared scope.

## Appendix A. Conditional boundary-current witness — A-CUR

This appendix is a **conditional** computation that substitutes an explicitly chosen numerical instance into the two-dimensional positive-energy Dirac band and planar Pauli vertex whose *forms* are declared in the upstream M70 v1.5 §1.1–§2; it is logically independent of §§2–7. Which items are inherited and which are chosen here is tabulated at the end of this appendix. There is no claim that the action selected the modes, the packet or the detector.

$$
h(k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z,\quad M=4,\quad k_0=(3,0),\ k_1=(-3,0),\ k_f=(0,0);\qquad
u_0=\tfrac1{\sqrt{10}}\binom31,\ u_1=\tfrac1{\sqrt{10}}\binom3{-1},\ u_f=\binom10,\quad E_0=E_1=5,\ E_f=4.
\tag{A1}
$$

The two photon modes have `p_0=(3,0)`, `p_1=(−3,0)`, a common normal momentum `z=1` and `ε=(0,1,0)`, and satisfy `k_a=k_f+p_a`. The declared planar current is

$$
j_0=u_f^\dagger\sigma_yu_0=-\frac i{\sqrt{10}},\qquad j_1=u_f^\dagger\sigma_yu_1=+\frac i{\sqrt{10}},\qquad j_0^*j_1=-\frac1{10}\ne0,
\tag{A2}
$$

and with `ρ(y)=2e^{−2y}`, `F(1)=(4+2i)/5` and the declared prefactor `γ=1/2` (for verification purposes; not derived from the locked values), setting `g_a=γFj_a` gives `g_1=−g_0`, `g_0^*g_1=−1/50`, `|g_0|²=1/50` (C07). For the four selected states `|i_a⟩=|k_a,+;vac⟩`, `|o_a⟩=|k_f,+;μ_a⟩` and `Ω=E_f+ω−E_a=√10−1`,

$$
H_4=\sum_{a=0,1}\big[\Omega|o_a\rangle\langle o_a|+g_a|o_a\rangle\langle i_a|+g_a^*|i_a\rangle\langle o_a|\big],
\tag{A3}
$$

$$
\eta(T)=\frac{4|g_0|^2}{R^2}\sin^2\frac{RT}2,\quad R=\sqrt{\Omega^2+4|g_0|^2},\qquad
U_T|i_a\rangle=B_T|i_a\rangle+A_a(T)|o_a\rangle,\ \ A_1=-A_0,\ |A_a|^2=\eta,
\tag{A4}
$$

$$
E_r(T,\beta)=\frac\eta2\begin{pmatrix}1&-re^{-i\beta}\\-re^{i\beta}&1\end{pmatrix},\quad E_\varnothing=(1-\eta)I,\qquad
\boxed{D_{\rm record}=\eta(T)\,|\cos\beta|}
\tag{A5}
$$

where the external detector reads `|d_r(β)⟩=(|o_0⟩+re^{iβ}|o_1⟩)/√2` and `|±x⟩` is `(|i_0⟩±|i_1⟩)/√2`. At `T=1, γ=½, β=0`, `η=0.0132293583` and no-click `0.986770642`; at `β=π/2`, or with a momentum-resolved detector, `D=0` (V14). If the coherence between the detected modes is reduced by `ν_det∈[0,1]`, then `D=ν_detη|\cosβ|`. This construction is a substitution into standard quantum erasure, and **the truncation error of the full current, the packet normalisation and the detector selection are OPEN**. If the TV errors `ε_±` against the actual physical output were proved, `D_{\rm physical}≥ν_detη|\cosβ|−ε_+−ε_-` would be a sufficient condition for a robust record, but this manuscript does not declare `ε_±`.


**Provenance of the declarations used above.** The upstream source declares the *forms* below; the numerical instance is chosen in this paper. The distinction matters because only the forms carry upstream authority.

| Item used in (A1)–(A5) | Provenance |
|---|---|
| $h(k)=k_x\sigma_x+k_y\sigma_y+M\sigma_z$, its positive-energy projector and $E(k)=\sqrt{\lvert k\rvert^2+M^2}$ | Declared upstream as a form, with $M>0$ |
| Momentum relation $k_a=k_f+p_a$ | Declared upstream |
| Profile family $\rho(y)=ae^{-ay}$, $a>0$, and the definition $F(z)=\int_0^\infty\rho(y)e^{izy}\,dy$ | Declared upstream as a family and a definition |
| Band-mass value $M=4$ | **Chosen here** |
| $k_0,k_1,k_f$ and $E_0=E_1=5$, $E_f=4$ | **Chosen here** |
| Spinors $u_0,u_1,u_f$ | **Chosen here**, consistent with the upstream normalisation condition |
| $p_0,p_1$, normal momentum $z=1$, polarisation $\varepsilon=(0,1,0)$ | **Chosen here** |
| $a=2$, hence $\rho(y)=2e^{-2y}$ and $F(1)=(4+2i)/5$ | **Chosen here**, an instance of the upstream family |
| Prefactor $\gamma=1/2$ | **Chosen here**; the upstream paper contains no such prefactor |

Nothing in this table changes a number in (A1)–(A5) or the exact checks C07 and V14; it fixes only what the appendix may claim to inherit. The appendix remains conditional, and §§2–7 do not use it.

## Appendix B. Reproducibility and theorem verification contract

### B.1 Standalone paired execution

The two delivered files are `ZS-M71_v1_4_1.md` and `zs_m71_verify_v1_4_1.py`. Python 3.10+ with NumPy and SciPy is required; there is no network access, old-script import, hidden seed file or project-source dependency at execution time.

```bash
python3 zs_m71_verify_v1_4_1.py --paper ZS-M71_v1_4_1.md --output zs_m71_verify_v1_4_1.json
```

The optional JSON records each row, runtime versions, generated tables and both file hashes. It is generated by the user command and is not a third required delivery. Default paired execution fails if the manuscript is missing or a live displayed formula cannot be parsed. `--math-only` explicitly uses the verifier's declared model defaults and skips the paired document checks. It must not be reported as validation of the paper.

```bash
python3 zs_m71_verify_v1_4_1.py --paper ZS-M71_v1_4_1.md --self-test --output zs_m71_verify_v1_4_1.json
```

Self-test runs the fault injections and clean/degraded controls in separate processes. It prints progress to stderr and the full JSON to stdout. Exit 0 means no registered check or requested self-test failed; exit 1 means failure; exit 2 reports missing dependencies with no rows falsely counted as executed. `--self-test` requires the paired profile. This is not a proof-assistant package, an external review or a licence grant for material inherited from the input files.

### B.2 Numerical and independence contract

The inherited deterministic seeds remain 71303 (mixed-state checks), 20260911 (regression), 71525 (Born quadrature), and 71707 (finite lemma attacks). Rational calculations use `fractions.Fraction`, integers and `isqrt`. Floating-point eigensolvers are double precision. The tridiagonal route and the additional sparse ARPACK route use the same declared Jacobi coefficients but different algorithms. ARPACK uses a fixed starting vector. V15 computes complete Born distributions from Schrödinger evolution and the phase parsed from the printed formula. This is independent of the weighted-TV implementation, while sharing the physical model.

Tolerances and finite ranges are in each emitted row: Born differences $10^{-12}$ in V15; eigensolver comparison $2\times10^{-12}$ for the eigenvalue, $10^{-7}$ for the second moment in V19; residual $10^{-10}$. V11 uses a $10^{-13}$ component noise floor only for numerical eigenvector domination comparisons. The analytic bound (30b) contains no numerical noise cutoff. C03 certifies the four rational static cases, including feasible-state energy and the infinite-lattice upper bound. Finite-bin eigenvalues and moment limits are not interval-certified by the script. C04 checks 50 exact rational core samples; its former floating-point transcendental component is explicitly moved to V12. Neither row is a symbolic proof of the entire theorem.

Several numerical routines descend from an earlier verifier for the detector sections, so the script is not wholly independent of that lineage. Within it, the paper-fed Born probabilities and the sparse-eigenpair route target distinct failure mechanisms, and the document-consistency module shares no code with the scientific rows. P = 0: no universal theorem is proved by execution. The analytic proofs, the source comparison and the finite computations have separate roles and are not substitutes for one another.

### B.3 Generated run summary and claim mapping

<!-- RUN-SUMMARY -->
**Paired run: 55 PASS / 0 FAIL / 3 SKIP, 58 rows.**

Evidence: P=0, C=13, V=28, W=5 (46 rows). Controls: R=1, G=7 (8 rows). Non-evidence: X=1, D=3 (4 rows). D01–D03 are SKIP. The mathematical profile has 49 PASS and 9 SKIP; it does not validate the manuscript.

Actual self-test: **43/43 mutations detected; 4/4 controls PASS.** The injected faults include a destabilised small-bin weight, a swapped finite-witness ratio, an altered proof text, an inflated boundary-layer bound, a broken supersolution, a falsified spectral certificate, and edits to each live formula the script parses. Every injection was detected by the row predicted for it.

Executed environment: Python 3.11.15, NumPy 2.4.4, SciPy 1.17.1. The four generated mathematical table blocks are emitted by the run and compared against the printed tables. No scientific row changed in v1.4. Counts do not establish a universal theorem, novelty or research grade.
<!-- /RUN-SUMMARY -->

| Claim / obligation | Rows | Actual executable scope |
|---|---|---|
| T-CAP | V01 | Finite charge twirl on 100 mixed states |
| T-EC | C01–C02, V02–V04, R01 | Finite exact identities, sampled bounds/witnesses, four-point Mathieu mapping and retained-bound regression |
| T-ASY | V05 | Four finite high-energy cases; imported asymptotic proof remains separate |
| L-CAL / F1 | V06–V07, V15 | Full Born quadrature, independent GKSL route, displayed phase and three real/complex references |
| T-WR/T-SAT | V08, W01 | Two-cutoff ceilings, critical energies and broad-Gaussian witness; duality/compactness are analytic |
| T-CERT / F4 | C03, W02 | Four exact feasible/dual certificates and the zero-record quantifier counterexample |
| T-BL | C04–C06, C09, V09–V13, V16–V17, V19 | Finite algebra and inequalities, constant-envelope supersolution, reflection, retired-bound attack, two eigensolvers; no formal universal proof |
| LOCAL-TAYLOR / (34a) | C08 | Exact local coefficient algebra, separate from C-2 |
| RECORD-SCOPE / F7 | V18, W03, V28 | Integer-bin window sequences, no-click identity, finite-window/static distinction, Gaussian counterpath and stable small-bin quadrature check |
| C-2 | X01 | Richardson diagnostic only, non-evidence class X |
| A-CUR | C07, V14 | Exact spinor/current calculation and nine H4 unitary/detector cases |
| T-JCE | C10, V20 | Exact conservation on 406 edges; full complex mixed-state joint pinching and direct Helstrom Born distributions on 18 finite cases |
| T-JB | V21, W04 | Longest paths for N=0,…,64, finite graph eigenvalues; stationary joint and marginal-product witnesses, partial transpose |
| T-SB | V22–V23, W05, C12–C13, V25 | 60 complex-product factorisations; direct common-sine correlations; incompatible-mode witness; exact N=4 polynomial, exact N=3 product improvement; two spectral algorithms |
| T-SBC | V24, V27 | Finite upper/lower spectra through N=16384; four single Gaussian–sine products with mean-energy checks; analytic limit proof remains separate |
| T-AR | C11 | 252 exact rational-resonance cases; irrational classification is analytic, not a finite rational approximation |
| T-DT | V26 | 27 direct phase-quadrature/Born cases; loss bound, sinc argument and half factor |
| Document/package | G01–G07 | File/version/hash, tag coverage, generated tables, census, status/command relations, narrow live-formula fields and optimum-lower-endpoint counterexample |
| Not certified | D01–D03, all SKIP | Novelty/grade, full formal proof, action-derived physical selection/mission |

**Ledger composition.** Of the 58 rows, 46 are evidence (C, V, W), 8 are controls (R, G) and 4 are non-evidence (X, D). The detector sections contribute C01–C09, V01–V19, W01–W03, R01 and X01; the joint charge–energy sections contribute C10–C13, V20–V28 and W04–W05; G01–G07 check the paper/script/ledger contract. Rows are added when a new finite claim needs an attack and are not removed silently.

G02 confirms required tag and label presence and that the §7.5 proof text has not drifted, not that an equation or argument is true. The legacy parser and the §7 parser are deliberately narrow: they connect selected displayed formulae to executed probes. The new fields connect the odd rotor gap, joint chain length, separable leading constant, upper-bound inequality and sinc half factor to distinct tests. This is not a semantic verifier of all prose, derivations or imported mathematics. A prose-only error elsewhere may still require a mathematical audit.

### B.4 Proof obligations and review scope

| Theorem-lane obligation | Resolution in this version |
|---|---|
| Exact statement, type and quantifier | Fixed reference space, bounded Jacobi objective, budget versus exact energy, and conditional versus unconditional TV are defined in §§1–7. |
| Declared versus used assumptions | T-WR needs bounded nonnegative weights, not compactness. T-SAT and T-BL use the actual positive decaying weights. T-BL holds for each fixed positive $\kappa/\delta$, not uniformly over ratios growing with $1/h$. |
| Dependencies and imported mapping | Unweighted Mathieu/circular results are imported; §9.1 identifies the general harmonic-method overlap. Appendix A is conditional and cannot promote the main text to physical CORE. |
| Boundary and degenerate cases | $\zeta=0$, zero coherence/undefined phase, finite-support singleton sectors, nonattained exact-energy supremum above saturation, fixed versus growing observation windows are handled. |
| Whole-lattice moment | Correct vertex reflection, uniform exterior envelope, a decaying supersolution and the infinite geometric second moment are proved in (30a)–(33b). |
| Minimal counterexamples | Opposite phase sign, wrong vertex reflection, the retired M0 lower bound, diagonal zero score, fixed-window divergence and the Gaussian $1/8$ path are retained as attacks. |
| Proof/computation separation | Finite probes are C/V/W, controls R/G, diagnostics/declarations X/D. PROVEN in §9.2 refers to the analytic proof, not the number of passing rows. |
| Independence | §7 and the detector sections were produced and reviewed by different assistants, and the reviews were not blind; the review of §§2–6 shares a lineage with the text it reviews and is reported as low-independence. No formal proof assistant and no qualified human reviewer has checked this paper: `qualified-human anchor: NONE`. Appendix C gives the disclosure. |

The finite checks of §7 use one reproducible random stream seeded with 712020 for mixed/product states, direct matrix trace norms and Born probabilities, exact integers/Fractions for conservation and rational resonance, and the explicit sine sum versus a separately evaluated closed form. V25 compares tridiagonal eigenvalues to ARPACK with a fixed start. The finite-time check integrates complex phases rather than reusing the sinc formula. Per-row ranges and tolerances are recorded in the emitted JSON. Code C10–C12 certifies only its finite enumerations/identity, not every N or every irrational ratio.

The finite constants implicit in the asymptotic estimates, and a numerical uniform $\varepsilon_0$, are not certified outputs; their absence is not a defect in an existential asymptotic theorem. Neither they, nor the still-open optimal error exponents and the C-2 operator remainder, affect the leading-order theorem. C13 does not close the exact finite separable optimum.

## Appendix C. AI assistance and review disclosure

Parts of this manuscript were drafted with AI assistance, and the review history is disclosed here rather than implied.

The detector analysis of §§2–6 and Appendix A originate in an earlier draft produced with one assistant; the joint charge–energy sections §7–§9, the repairs to §§2–6 and the companion verifier were produced with a second, different assistant. Reviews were carried out by an assistant of a lineage different from the one that generated §7, which is the part carrying the central claim; those reviews reconstructed the analytic proofs, reproduced the companion verifier in a different environment, and rebuilt the principal results independently from the equations printed here. The review of §§2–6 shares a lineage with the draft that produced them and is therefore reported as low-independence rather than as an independent check. The prior-art reading of §9.1 and the final integration were performed by that same reviewing lineage, so the novelty assessment in §9.3 and the text that states it share one lineage; a further review by that lineage would be a self-review and is not claimed.

No formal proof assistant was used, and no qualified human expert has reviewed this paper: `qualified-human anchor: NONE`. Where a statement rests on an assistant's reconstruction rather than on an executed computation or an opened primary source, the text says so. Human authorship and final responsibility remain with the project owner.

## References

Primary texts were opened for [3]–[8], [10]–[17] and [19]–[26]; [18] was available only at abstract level. The exact passages consulted are named in §9.1.

1. Earlier versions of this manuscript and their companion verifiers (project-internal).
2. Project research mission and rule package, and the project's internal corpus indexes (project-internal).
3. Z. Hradil, J. Řeháček, Z. Bouchal, R. Čelechovský, L. L. Sánchez-Soto, *Minimum uncertainty measurements of angle and angular momentum*, Phys. Rev. Lett. 97, 243601 (2006), [primary preprint](https://arxiv.org/pdf/quant-ph/0605137), (7), (9)–(13).
4. R. Parhizkar, Y. Barbotin, M. Vetterli, *Sequences with minimal time–frequency uncertainty*, [primary preprint](https://arxiv.org/pdf/1302.2082), Lemmas 2–3, §3.2 (17)–(18).
5. NIST Digital Library of Mathematical Functions, [§28.8.1](https://dlmf.nist.gov/28.8#E1), large-parameter Mathieu characteristic-value expansion.
6. L. Mišta Jr., M. Mišta, Z. Hradil, *Unifying uncertainties for rotor-like quantum systems*, Phys. Rev. A 110, 032208 (2024), [primary preprint v3](https://arxiv.org/html/2403.02498v3), (4)–(5), (29)–(32).
7. **P. Folge**, L. Serino, L. Mišta Jr., B. Brecht, C. Silberhorn, J. Řeháček, Z. Hradil, *Quantum-limited detection of arrival time and carrier frequency of time-dependent signals*, [primary preprint](https://arxiv.org/pdf/2602.20962) (2026).
8. M. Klein and E. Rosenberger, *Harmonic approximation of difference operators*, [primary preprint](https://arxiv.org/pdf/1706.06357), Hypothesis 1.1 and Theorem 1.3. Methodological comparison, not an imported full proof of (21).
9. Not read in full, and not used as affirmative evidence: Breitenberger 1985; Řeháček et al. 2008; Hradil et al. 2010; Kim et al. 2000; Nam 2013. The upstream source for Appendix A is project-internal; the appendix states every declaration it uses and marks which are inherited.
10. M. Navascués and S. Popescu, *How energy conservation limits our measurements*, Phys. Rev. Lett. 112, 140502 (2014). [Primary extended preprint](https://arxiv.org/pdf/1211.2101); [publisher record](https://link.aps.org/doi/10.1103/PhysRevLett.112.140502). Equation numbers in §9.1 refer to the extended PDF, including Appendix D.
11. I. Marvian and R. W. Spekkens, *Modes of asymmetry: the application of harmonic analysis to symmetric quantum dynamics and quantum reference frames*, [primary preprint](https://arxiv.org/pdf/1312.0680) (2014 version).
12. M. Ahmadi, D. Jennings and T. Rudolph, *The WAY theorem and the quantum resource theory of asymmetry*, New J. Phys. 15, 013057 (2013); [primary preprint](https://arxiv.org/pdf/1209.0921) (2012).
13. A.-C. de la Hamette, S. L. Ludescher and M. P. Müller, *Entanglement-asymmetry correspondence for internal quantum reference frames*, [primary preprint](https://arxiv.org/pdf/2112.00046) (2022 version).
14. F. Giacomini, E. Castro-Ruiz and Č. Brukner, *Quantum mechanics and the covariance of physical laws in quantum reference frames*, Nature Communications 10, 494 (2019). [Primary text](https://arxiv.org/html/1712.07207v2); [publisher](https://www.nature.com/articles/s41467-018-08155-0).
15. D. Collins, C. M. Ferrera, I. L. Paiva and S. Popescu, *Networks of quantum reference frames and the nature of conserved quantities*, [primary preprint v1](https://arxiv.org/html/2603.25485v1) (2026). Preprint, not represented as a peer-reviewed publication.
16. A. Hokkyo and H. Tajima, *Quantitative Wigner–Araki–Yanase Theorems for Unitary and Antiunitary Symmetries*, [primary preprint](https://arxiv.org/pdf/2607.09075) (2026). Preprint status retained.
17. S. Carrozza and P. A. Höhn, *Edge modes as reference frames and boundary actions from post-selection*, [primary text v4](https://arxiv.org/html/2109.06184v4). The boundary-field comparison uses the specified sections, not a claimed derivation of a Z-Spin instrument.
18. M. P. Woods, R. Silva and J. Oppenheim, *Autonomous quantum machines and the finite sized Quasi-Ideal clock*, [primary abstract and preprint record](https://arxiv.org/abs/1607.04591). Abstract-only use in this revision; no quantitative bound imported from unavailable full text.
19. L. Loveridge, *A relational perspective on the Wigner–Araki–Yanase theorem*, J. Phys.: Conf. Ser. 1638, 012009 (2020). [Primary preprint](https://arxiv.org/pdf/2006.07047), §4.4, (21)–(22), and §5.1.

20. E. Bagan, M. Baig and R. Muñoz-Tapia, *Entanglement assisted alignment of reference frames using a dense covariant coding*, Phys. Rev. A 69, 050303 (2004). [Primary PDF v2](https://arxiv.org/pdf/quant-ph/0303019v2); [bibliographic record](https://arxiv.org/abs/quant-ph/0303019).
21. G. Chiribella, G. M. D'Ariano, P. Perinotti and M. F. Sacchi, *Efficient use of quantum resources for the transmission of a reference frame*, Phys. Rev. Lett. 93, 180503 (2004). [Primary PDF v2](https://arxiv.org/pdf/quant-ph/0405095v2); [bibliographic record](https://arxiv.org/abs/quant-ph/0405095).
22. E. Bagan, M. Baig and R. Muñoz-Tapia, *Quantum reverse-engineering and reference frame alignment without non-local correlations*, Phys. Rev. A 70, 030301 (2004). [Primary PDF v2](https://arxiv.org/pdf/quant-ph/0405082v2); [bibliographic record](https://arxiv.org/abs/quant-ph/0405082).
23. S. D. Bartlett, T. Rudolph and R. W. Spekkens, *Reference frames, superselection rules, and quantum information*, Rev. Mod. Phys. 79, 555 (2007). [Review PDF v3](https://arxiv.org/pdf/quant-ph/0610030v3); [bibliographic record](https://arxiv.org/abs/quant-ph/0610030). Contextual synthesis; not an independent primary discovery for the constructions in [20]–[22].

24. S. Popescu, A. B. Sainz, A. J. Short and A. Winter, *Reference frames which separately store non-commuting conserved quantities*, Phys. Rev. Lett. 125, 090601 (2020). [Primary preprint](https://arxiv.org/pdf/1908.02713): Theorem 1 with (1)–(3), construction (4)–(6), error bounds (12)–(14).

25. Y. Guryanova, S. Popescu, A. J. Short, R. Silva and P. Skrzypczyk, *Thermodynamics of quantum systems with multiple conserved quantities*, Nature Communications 7, 12049 (2016). [Primary record](https://arxiv.org/abs/1512.01190). The commuting-case antecedent cited by [24]; separate per-charge batteries with thermodynamic objectives.

26. T. Paterek, P. Kurzyński, D. K. L. Oi and D. Kaszlikowski, *Reference frames for Bell inequality violation in the presence of superselection rules*, New J. Phys. 13, 043027 (2011). [Primary preprint](https://arxiv.org/pdf/1004.5184): §5, (11)–(12) for the minimal frame; §7, (16)–(19) for the separable optimisation, its factorisation and the sine optimiser.

## Machine-readable run metadata

This block identifies the delivered pair and the claim states for the companion verifier. It does not certify mathematical logic, novelty or physical realisation.

<!-- M71-META
{
  "paper": "ZS-M71_v1_4_1.md",
  "paper_version": "1.4.1",
  "script": "zs_m71_verify_v1_4_1.py",
  "script_version": "1.4.1",
  "script_sha256": "eeba11555fe4436b8c1f13475de887b08462630437ffb5677a7b210fcb3f2154",
  "qualification": "PASS",
  "qualification_basis": "substantive_novelty_resolved",
  "research_grade": "3",
  "candidate_grade": "NONE",
  "target_grade": "4",
  "role": "RESEARCH PAPER / SUPPORT-METHOD",
  "rows": 58,
  "census": {
    "V": 28,
    "C": 13,
    "R": 1,
    "W": 5,
    "X": 1,
    "G": 7,
    "D": 3
  },
  "ledger": {
    "V01": [
      "V",
      "T-CAP"
    ],
    "C01": [
      "C",
      "T-EC"
    ],
    "V02": [
      "V",
      "T-EC"
    ],
    "V03": [
      "V",
      "T-EC"
    ],
    "C02": [
      "C",
      "T-EC"
    ],
    "R01": [
      "R",
      "T-EC"
    ],
    "V04": [
      "V",
      "T-EC"
    ],
    "V05": [
      "V",
      "T-ASY"
    ],
    "V06": [
      "V",
      "L-CAL"
    ],
    "V07": [
      "V",
      "L-CAL"
    ],
    "C03": [
      "C",
      "T-CERT"
    ],
    "V08": [
      "V",
      "T-SAT"
    ],
    "W01": [
      "W",
      "T-SAT"
    ],
    "C04": [
      "C",
      "T-BL"
    ],
    "C05": [
      "C",
      "T-BL"
    ],
    "C06": [
      "C",
      "T-BL"
    ],
    "V09": [
      "V",
      "T-BL"
    ],
    "V10": [
      "V",
      "T-BL"
    ],
    "V11": [
      "V",
      "T-BL"
    ],
    "V12": [
      "V",
      "T-BL"
    ],
    "V13": [
      "V",
      "T-BL"
    ],
    "X01": [
      "X",
      "C-2"
    ],
    "C07": [
      "C",
      "A-CUR"
    ],
    "V14": [
      "V",
      "A-CUR"
    ],
    "V15": [
      "V",
      "L-CAL"
    ],
    "V16": [
      "V",
      "T-BL"
    ],
    "V17": [
      "V",
      "T-BL"
    ],
    "C08": [
      "C",
      "LOCAL-TAYLOR"
    ],
    "C09": [
      "C",
      "T-BL"
    ],
    "W02": [
      "W",
      "T-CERT"
    ],
    "V18": [
      "V",
      "RECORD-SCOPE"
    ],
    "W03": [
      "W",
      "RECORD-SCOPE"
    ],
    "V19": [
      "V",
      "T-BL"
    ],
    "C10": [
      "C",
      "T-JCE"
    ],
    "V20": [
      "V",
      "T-JCE"
    ],
    "V21": [
      "V",
      "T-JB"
    ],
    "C11": [
      "C",
      "T-AR"
    ],
    "W04": [
      "W",
      "T-JB"
    ],
    "V22": [
      "V",
      "T-SB"
    ],
    "V23": [
      "V",
      "T-SB"
    ],
    "W05": [
      "W",
      "T-SB"
    ],
    "C12": [
      "C",
      "T-SB"
    ],
    "V24": [
      "V",
      "T-SBC"
    ],
    "V25": [
      "V",
      "T-SB"
    ],
    "V26": [
      "V",
      "T-DT"
    ],
    "V27": [
      "V",
      "T-SBC"
    ],
    "V28": [
      "V",
      "RECORD-SCOPE"
    ],
    "C13": [
      "C",
      "T-SB"
    ],
    "G07": [
      "G",
      "PACKAGE"
    ],
    "G01": [
      "G",
      "PACKAGE"
    ],
    "G02": [
      "G",
      "PACKAGE"
    ],
    "G03": [
      "G",
      "PACKAGE"
    ],
    "G04": [
      "G",
      "PACKAGE"
    ],
    "G05": [
      "G",
      "PACKAGE"
    ],
    "G06": [
      "G",
      "PACKAGE"
    ],
    "D01": [
      "D",
      "NOVELTY"
    ],
    "D02": [
      "D",
      "PROOF"
    ],
    "D03": [
      "D",
      "MISSION"
    ]
  },
  "operational_contract": {
    "lower_endpoint": "optimum_only",
    "upper_endpoint": "all_feasible_states",
    "no_click": "included",
    "one_quarter_path": "saturation"
  },
  "claims": {
    "T-CAP": "PROVEN",
    "T-EC": "PROVEN/IMPORTED-PROVEN",
    "T-ASY": "IMPORTED-PROVEN",
    "L-CAL": "DERIVED",
    "T-WR": "PROVEN",
    "T-SAT": "PROVEN",
    "T-CERT": "CERTIFIED-FOUR-STATIC-CASES",
    "T-BL": "PROVEN-REPLACEMENT-PROOF",
    "LOCAL-TAYLOR": "DERIVED",
    "C-2": "HYPOTHESIS",
    "RECORD-SCOPE": "DERIVED",
    "A-CUR": "DERIVED-CONDITIONAL",
    "T-JCE": "PROVEN-ANALYTIC",
    "T-JB": "PROVEN-ANALYTIC",
    "T-SB": "PROVEN-ANALYTIC",
    "T-SBC": "PROVEN-ANALYTIC",
    "T-AR": "PROVEN-ANALYTIC",
    "T-DT": "DERIVED-FINITE-TIME-MODEL",
    "C13-FINITE-SINE-COUNTEREXAMPLE": "CERTIFIED-EXACT-N3-ONLY"
  },
  "limits": [
    "finite samples and grids are not universal proofs; the universal statements are proved by hand",
    "no formal verification; no qualified human review",
    "novelty is assessed against the inspected results in section 9, not proved absent worldwide"
  ]
}
-->
