# M70 v1.5 — Recoil-inclusive spectra of a boundary Dirac current and PEC packet-tail decay theorems

> **English edition and notation.** This is the complete English rendering of M70 v1.5; the research version remains 1.5. Mathematical notation is written in Unicode and plain text: _(index) denotes a subscript, and ^(expression) retains a superscript when Unicode superscripts are unavailable (a power, component, or label as appropriate); fractions retain explicit grouping, and hat(·), bar(·), column(·; ·), and nested matrix rows preserve their original meanings. All source judgments, historical records, references, and execution metadata are retained. The verifier commands, hashes, and recorded scientific test results below refer to the original manuscript–verifier pair, not to a new execution against this translated edition.

**Recoil-inclusive spectra of a boundary Dirac current: moment-free PEC decay, a high-energy boundary layer, and packet-tail rates**

**Version:** 1.5 · 2026-09-11 UTC · companion verifier 1.5.0  
**Document role:** RESEARCH PAPER / SUPPORT-METHOD  
**PAPER QUALIFICATION:** PASS · **RESEARCH GRADE:** 3 · **CANDIDATE GRADE:** NONE · **TARGET GRADE:** 4 (not attained)  
**Scope of assessment:** A content assessment under the project criteria, based on the primary-source comparisons in §7 and the proofs in the manuscript. The v1.5 assessment is an author-side assessment of the integrated content and does not mean that an independent external review has been passed.  
**Central contributions:** LM-D / LM-L / LM-P; integrated supplements LM-B0 / LM-E / LM-Q. **qualified-human anchor:** NONE.  
**Integration lineage:** A = the preceding Codex v1.4; B = the attached Claude v1.4. A's LM-D/L/P, KRS correspondence, and high-precision verification are integrated, with corrections, with B's bound of 18 and photon-energy lower bound. B receives a partially cross-lineage review; A and LM-Q receive author-side review.  
**Rules applied:** KERNEL / RESEARCH / BREAKTHROUGH / AUDIT / MANUSCRIPT / VERIFY v2.3, Z-Spin Research Mission v1.6.

## Abstract

We study a declared model in which one occupied channel of a 2D positive-energy Dirac band with mass `M>0` and nonzero charge couples to a 3D transverse Maxwell field through a normal density `ρ ≥ 0`, `ρ ∈ L¹ ∩ L²(ℝ_(+))`, `∫ρ=1`. The time dependence is an external pulse, and the results are restricted to the order-`e_(ch)²` inclusive channel.

The two v1.4 versions are integrated while preserving the recoil kernel and current identities, the bound `J_(B) ≤ 18J_(∞)`, the `L²/H^(1/2)` switching criteria for every normalized packet, and the free/PMC soft laws. When the PEC profile has finite first moment `d`, the following three central theorems of version A are preserved.

1. **Moment-free decay (LM-D).** Under `I_(ρ)=∫ B_(PEC)(z)/∣z∣ dz<∞`, the bound `J_(PEC) ≤ C_(ρ)Ω` holds for all `k,Ω`, and the Gaussian response of every fixed normalized `L²` packet tends to 0. No assumption on the packet's mean energy or logarithmic moment is required. An explicit finite-time tail bound is also obtained.
2. **Boundary layer and nonuniformity (LM-L).** We derive a positive function `L_(ρ)(η)` in the limit `E → ∞, EΩ=η` with the product held fixed. It satisfies `L_(ρ) ∼ e_(ch)²d²η²/(3π²M²)` and `L_(ρ) → e_(ch)²I_(ρ)/(4π²)`. Every fixed packet decays, but the decay is not uniform over all packets.
3. **Exact tail-dependent rates (LM-P).** Packets with energy density `f_(α)(E)=α E_(0)^(α) E^(-1-α)`, `E ≥ E_(0) ≥ M, 0<α<2` satisfy `ℛ_(τ) ∼ K_(α)τ^(-α)`, with `K_(α)>0` given by an explicit Mellin integral. The range `1<α<2` realizes finite mean energy together with decay slower than `τ⁻²`.

The supplement from attached version B proves `Ω ≤ 2ω` at every on-shell point, establishes `ℰ_(γ) ≥ ℰ_(total)/2`, and hence gives the necessity of `H^(1/2)` switching. For packets of finite mean energy, finite photon energy is equivalent to `H^(1/2)`. The integration also adds the fixed-frequency high-energy limit `Q_(B)`, yielding the exact lower bound `64/(5π)>4` on the globally optimal constant. The upper bound 18, the exact lower bound, and the numerical witness 4.110216 are distinguished by the type of evidence supporting them.

The v1.3 necessary-and-sufficient PEC `E²`-moment theorem is retained. The limit of `τ²ℛ_(τ)` is finite only when the `E²` moment is finite. This version connects that theorem to decay of every fixed packet, failure of a common decay rate, and exact power-tail rates. In the correspondence with the general recoil and finite-measurement-time formulas of KRS, the common vertex is imported; an external pulse without cancellation between the pre- and post-measurement amplitudes is not identified with a detector instrument. The additional analysis provides the basis for research grade 3. Grade-4 innovation, completion of the full Z-Spin mission, and experimental verification are not claimed.

## 1. Problem, scope, and dependencies among the results

In M69, stationary spatial smearing and a moving boundary current were different objects. Applying the spatial Fourier cutoff of a stationary source directly to a recoiling charged particle replaces the sum over final fermion states by a projection onto the initial packet. The question of this manuscript is: **What is the actual spectral weight of one inclusive channel in a specified boundary band, and what temporal regularity is required for a finite response?**

The central results of v1.5 are **LM-D/L/P** in §§5.9–5.11, supported by the recoil analysis and uniform bounds in §§5.2–5.8. LM-D removes the packet-moment restriction for PEC, and the boundary layer in LM-L leads to the exact tail-dependent rates in LM-P. The existing moving-sector results are preserved as follows. The current identities and two exact representations in LM-K yield the uniform bound LM-B, the soft theorem LM-S, and the plateau limit LM-R. LM-B gives the packet-level temporal-regularity criteria LM-T; LM-B and LM-S give the adiabatic dichotomy LM-A, including the PEC `E²`-moment trichotomy. LM-E includes the photon-energy lower bound for every packet, and LM-Q in §5.12 gives a distinct high-energy limit at fixed frequency. LC-K/U/I/T from v1.1 are preserved as specializations to initial momentum `k=0`, and V11 compares the `k=0` reduction of the LM representations with LC4. LA in Appendix A and LB in Appendix B are separate supporting results for different models. The LC and LM proofs do not depend on LA or LB, and no claim is made that the three models have been connected to the same physical code or detection apparatus.

The ownership and lineage of results already present in M70 seed v2.1 are retained. The v1.1 contributions—exact factors, restoration of omitted proofs, explicit separation of total and photon observables, and an error-detecting verification package—are preserved. The new contribution in v1.2 was LM in §5. The new contributions in v1.3 were the theorem sharpening the PEC condition of LM-A to a necessary-and-sufficient `E²`-moment condition (LM-A(b), (LM10)) and a third independent numerical route supporting it. The derivation of this `E²` bound was proposed by the external v1.2 auditor (OpenAI Codex, Appendix A of the audit report), then adopted after the authors (Claude) independently rederived it and checked it symbolically (C15) and numerically (V17). The same mathematical result is not counted as two separate debt closures in the seed and the paper.

### 1.1 Declared inputs and assumptions

We use `ℏ=c_(light)=1`, and `e_(ch) ≠ 0` is the charge. This common nonzero-charge assumption applies to positive coefficients and necessary-and-sufficient theorems. In the degenerate model `e_(ch)=0`, every response is 0 and those necessity statements are not asserted. Planar momenta are denoted by `k,p ∈ ℝ²`, the normal coordinate by `y>0`, and the normal photon momentum by `z ∈ ℝ`. The variable `z` is not a position coordinate.

```text
h(k)=k_(x)σ_(x)+k_(y)σ_(y)+Mσ_(z),
E(k)=√(|k|²+M²), P_(+)(k)=(I+h(k)/E(k))/(2), M>0;
ρ ∈ L¹ ∩ L²(ℝ_(+)), ρ ≥ 0, ∫_(0)^(∞)ρ(y) dy=1.

(LC1)
```

1. **Band and occupation:** One particle is prepared in the positive band, with the photons initially in the vacuum. The other final states in that band are empty. The negative band, sea, and edge-to-bulk channels are excluded.
2. **Normal profile:** The normal overlap densities of charge and current are both declared to be `ρ`. Numerical calculations use the example `ρ(y)=ae^(-ay)`, `a>0`. Then `‖ρ‖_(2)²=a/2`, and the first moment is `d=1/a`.
3. **Photon modes:** Free-space modes and the specified PEC/PMC half-space transverse modes are used. Extending these modes to arbitrarily high frequency is a mathematical idealization. Dispersion, losses, and lattice cutoffs of a real mirror are not included.
4. **Coupling and perturbative order:** The coupling is linear between the projected planar Pauli current and the transverse field. The response is of order `e_(ch)²`. This is not a full-QED theorem resolving the Coulomb sector and gauge dressing.
5. **Initial state:** The single `J_(B)` of LC-K/I/T concerns initial momentum `k=0`. The prescription starts from a normalized `k=0` state in a finite planar box and sends the area to infinity. An unnormalized plane wave on the infinite plane is not called an `L²` packet. The LM sector in §5 instead allows an arbitrary normalized initial state `φ ∈ L²(ℝ²)`. Since `{k=0}` has measure 0 for a normalized packet, the LC infrared and adiabatic laws are read as results of the rest prescription, not as the physical laws of a packet (S1–S6 in Appendix C).

To connect with the boundary mode of M67, one may use the conditional inputs `a=2m∣ cos bar(θ) ∣` and `M=∣m sin bar(θ) ∣`. Only the region requiring `a,M>0` is considered. M67 supplies the free boundary carrier; the PEC/PMC Maxwell coupling in this manuscript is an additionally declared extension. This does not mean that the Z-Spin action has selected `bar(θ)`, the occupation, the mode family, or the switching.

### 1.2 Mode normalization and vertex

```text
F(z)=∫_(0)^(∞)ρ(y)e^(izy) dy=C(z)+iS(z),
B_(free)=|F|², B_(PEC)=2S², B_(PMC)=2C².

(LC2)
```

Delta-normalized creation and annihilation operators use `d²p dz` for free photons and `d²k` for the charged band. We impose `u_(+)(k)† u_(+)(k)=1`. The creation part of the free vertex is

```text
V⁺=(e_(ch))/(√(2(2π)³))
Σ_(λ)∫ (d²p dz d²k)/(√(ω))
F(z) u_(+)(k-p)†
(ε_(λ x)*σ_(x)+ε_(λ y)*σ_(y))u_(+)(k)
b_(k-p)† b_(k) a_(p,z,λ)†,
ω=√(|p|²+z²).
```

Its Hermitian conjugate is added, and real switching multiplies `V(t)`. PEC/PMC use delta-normalized half-space modes with `z>0`. Relative to the free normalization, the sine/cosine amplitudes of the planar mode components are respectively `2S,2C`. Replacing their squared amplitudes integrated over positive `z` by even integrands over all `z` gives `2S²,2C²` in (LC2). No additional half-space factor is therefore multiplied in. The sum over the planar components of the two polarizations is `Π_(ab)=δ_(ab)-p_(a)p_(b)/ω²`, `a,b ∈ {x,y}`.

This mode normalization is an assumption that enters the constants of the results directly. The manuscript does not prove that a physical sample jointly realizes this normal profile and these boundary modes.

## 2. Inclusive current and exact rest spectrum — LC-K

Apply the vertex to one particle with initial state `φ ∈ L²(ℝ²)`, `‖φ‖_(2)=1`, and sum over the final fermion and photon. At fixed `(k_(f),p,z)`, only one initial momentum contributes: `k=k_(f)+p`. Orthogonality of distinct `k_(f)` eliminates cross terms, giving the following cutoff norm.

```text
𝒩_(𝒞)
=(e_(ch)²)/(2(2π)³)
∫_(𝒞)(d²p dz)/(ω) B(z)
∫ d²k |φ(k)|²𝒯(k,p,z),
𝒯(k,p,z)
=Σ_(a,b=x,y)(δ_(ab)-(p_(a)p_(b))/(ω²))
tr [P_(+)(k-p)σ_(a)P_(+)(k)σ_(b)],
𝒯(0,p,z)
=(1-M/E_(f))/(2)(1+(z²)/(ω²)), E_(f)=√(|p|²+M²).

(LC3)
```

Here `𝒞` is a photon region that is initially kept finite. The inequality `𝒯 ≥ 0` follows from a sum of squared matrix elements for each polarization. The four components of the rest spinor tensor are `(1-M/E_(f))/2` multiplied by `([[1, -i]; [i, 1]])`. A check that merely removes the antisymmetric imaginary components is insufficient. The diagonal Kronecker delta and the full `ω²=∣p∣²+z²` must be used to obtain the magnitude in (LC3). Verifier C01 checks all four components and the complete contraction.

For a general packet response including the time integral, the integrand contains `∣ hat(χ) (E(k-p)+ω-E(k))∣²`. It is therefore also incorrect to conclude that packet dependence disappears entirely. Wick reduction for quasifree many-body occupation gives `f_(i)(1-f_(f))`, but this is not extended to a formula for arbitrary correlated many-body states.

By contrast, **exclusive** postselection onto the same outgoing packet can involve an overlap such as `⟨φ,T_(p)φ⟩`. For example, `φ(k)=1/2` on `[-1,1]²` and 0 elsewhere has norm 1. The shifted packet at `p=(3,0)` has disjoint support, so the overlap is 0, whereas the inclusive-current integral in (LC3) is positive at `z=1`. W01 calculates the actual packet norm, shifted norm, overlap, and spinor-current integral. This example shows that a fictitious stationary cutoff can remove a genuine channel. The inclusive/exclusive distinction itself is also explicit in earlier radiation research. [Kazinski–Lazarenko, Introduction and §3](https://arxiv.org/html/2010.05236v2).

### Theorem LC-K

Under the assumptions of §1, define `Ω=E_(f)+ω-M>0` as the **total excitation mismatch**. The order-`e_(ch)²` rest spectral density of this channel is

```text
J_(B)(Ω)=(e_(ch)²)/(32π²(Ω+M)²)
∫_(-Ω)^(Ω)(Ω²-z²)B(z)
[1+(4(Ω+M)²z²)/({Ω(Ω+2M)+z²}²)]dz.

(LC4)
```

**Proof.** Insert `δ(Ω+M-E_(f)-ω)` into the rest integrand of (LC3). With `W=Ω+M`, the shell solutions are

```text
E_(f)=(W²+M²-z²)/(2W),
ω=(W²-M²+z²)/(2W),
|∂_(p)(E_(f)+ω)|=(pW)/(E_(f)ω).
```

The condition `p²=E_(f)²-M² ≥ 0` is equivalent to `∣z∣ ≤ Ω`. The planar angular integral gives `2π`. Multiplying `p dp/ω`, the delta-function Jacobian, and the tensor factor `(1-M/E_(f))/2` gives `(E_(f)-M)/(2W)=(Ω²-z²)/(4W²)`. The remaining polarization factor is the expression in square brackets, and the overall constant is that of (LC4). The boundary `p=0` has measure 0 and is taken as the limit of the interior change of variables. □

The original phase-space integral and the reduced expression describe the same declared model. The verifier's photon spherical-coordinate route uses different variables and a different Jacobian but assumes the same physical vertex. Agreement between the two numerical routes is not independent experimental verification of that physical premise.

## 3. UV plateau, bare norm, and infrared classification — LC-U/I

### Theorem LC-U

Under the normal-profile assumptions of §1, the three mode families satisfy

```text
∫_(ℝ)B(z) dz=2π‖ρ‖_(2)²,
J_(B)(Ω) → J_(∞)=(e_(ch)²‖ρ‖_(2)²)/(16π),
∫_(0)^(Λ) J_(B)(Ω) dΩ=J_(∞)Λ+o(Λ).

(LC5)
```

In particular, if `e_(ch) ≠ 0`, the bare inclusive norm diverges.

**Proof.** Fourier transforming the zero extension of `ρ` on `ℝ` gives the first equality for the free family by Plancherel. Half-line sine/cosine Plancherel gives `∫_(0)^(∞) S²dz=∫_(0)^(∞) C²dz=(π/2)‖ρ‖_(2)²`, respectively, so PEC/PMC have the same constant. This uses the assumption that `ρ` is real.

Define the dimensionless factor multiplying `B(z)` in (LC4), on the entire real line, by

```text
Q_(Ω)(z)=𝟙_(|z| ≤ Ω)(Ω²-z²)/((Ω+M)²)
(1+(z²)/(ω(Ω,z)²))
```

On the shell, `ω ≥ ∣z∣`, hence `0 ≤ Q_(Ω) ≤ 2`; for fixed `z`, `Q_(Ω) → 1`. Since `B ∈ L¹`, dominated convergence yields the plateau. The limit of averages gives the last formula. Moreover, `J_(B) ≤ 2J_(∞)` for every `Ω>0`. □

**A limited auxiliary result for moving packets.** The ultraviolet divergence of the bare norm persists for a normalized `φ` with compact momentum support. Write `p=r n`, `n=( cos α, sin α)`, and keep `z,k` bounded. As `r → ∞`, the final Bloch vector is `(-n_(x),-n_(y),0)`, and the initial Bloch vector is `v(k)=(k_(x),k_(y),M)/E(k)`. Contraction of the actual Pauli tensor with `I-nnᵀ` gives

```text
𝒯(k,rn,z) → (1+n· v_(∥)(k))/(2),
∫_(0)^(2π)(1+n· v_(∥)(k))/(2) dα=π.
```

This convergence is uniform on compact sets of `k,z`. We have `r/ω → 1`, and a finite `Z` can be chosen such that `∫_(-Z)^(Z)B(z)dz>0`. For sufficiently large `r`, the angular and `k` integrals are bounded below by a positive constant, so `∫^(∞) dr` diverges. C02 symbolically contracts the actual limiting tensor. Uniform convergence and the infinite-interval argument themselves belong to this analytic proof and are not automatically proved by C02. This auxiliary result does not state that the full `J_(B)` of a general packet equals the rest formula. **v1.2 scope clarification (S3).** LM-B and LM-R in §5 supersede this auxiliary argument. The bare norm diverges for every normalized packet, but convergence to the plateau is not uniform in `k`; in the window `max (M,a) ≪ Ω ≪ E(k)`, `J_(B)/J_(∞)` grows to values close to the upper bound 4 of `Φ(λ)` (grid maximum 4.0694). The v1.1 text already qualified this auxiliary result as “not a theorem for general packets,” so S3 replaces it by a new theorem rather than correcting an error in the v1.1 theorem (Appendix C, Round 2).

### Theorem LC-I

The free/PMC results require only the assumptions of §1; the following leading PEC coefficient additionally assumes `d=∫_(0)^(∞) yρ(y)dy<∞`. A normalized nonnegative density has `d>0`. As `Ω ↓ 0`,

```text
J_(free)(Ω) ∼ (e_(ch)²Ω³)/(20π²M²),
J_(PMC)(Ω) ∼ (e_(ch)²Ω³)/(10π²M²),
J_(PEC)(Ω) ∼ (e_(ch)²d²Ω⁵)/(42π²M²).

(LC6)
```

**Proof.** Substitute `z=Ω u`, `∣u∣ ≤ 1`. From `C(0)=1,S(0)=0`, the free/PMC weights tend to 1 and 2, respectively. With a finite first moment, `S(z)/z → d` and `∣S(z)∣ ≤ d∣z∣`, so PEC has the factor `2d²Ω²u²`. The square bracket tends to `1+u²`, and the denominator to `M²`. Dominated convergence on compact `u`, together with

```text
(1)/(32)∫_(-1)¹(1-u²)(1+u²)du=(1)/(20),
(1)/(32)∫_(-1)¹ 2u²(1-u²)(1+u²)du=(1)/(42)
```

gives the coefficients. □

This theorem does not assert that the relative correction is always `O(Ω²)`. Even the specified exponential profile has a first-order `Ω` correction in the kinematic factor. `M=0` and a nonnormalizable delta-layer lie outside the assumptions; the same IR and UV theorems do not apply.

**Scope clarification in v1.2 (S1).** The `Ω³/Ω⁵` orders in LC-I hold only at `k=0`. If `k ≠ 0`, LM-S changes the orders to `Ω¹` for free/PMC and `Ω³` for PEC. Thus LC-I is not the IR law for normalized packets; only the hierarchy of PEC suppression across boundary mode families survives as a relative factor `Ω²`.

## 4. Response, total excitation energy, and photon energy — LC-T

Let `χ ∈ L¹(ℝ)` be real, with `hat(χ) (Ω)=∫χ(t)e^(iΩ t)dt`. Distinguish the two energy observables.

```text
ℛ_(χ)=∫_(0)^(∞) J_(B)(Ω)| hat(χ) (Ω)|²dΩ,
ℰ_(total)=∫_(0)^(∞)Ω J_(B)(Ω)| hat(χ) (Ω)|²dΩ,
J_(γ,B)(Ω)=(e_(ch)²)/(32π²(Ω+M)²)
∫_(-Ω)^(Ω)(Ω²-z²)B(z)
(1+(z²)/(ω(Ω,z)²))ω(Ω,z) dz,
ℰ_(γ)=∫_(0)^(∞) J_(γ,B)(Ω)| hat(χ) (Ω)|²dΩ,
ω(Ω,z)=(Ω(Ω+2M)+z²)/(2(Ω+M)).

(LC7)
```

`ℰ_(total)` includes the fermion recoil `E_(f)-M`. Thus `Ω` must not be read as the photon frequency. Each observable is a leading-order perturbative quantity; there is no guarantee that `ℛ_(χ)` is an exact probability or is at most 1 for arbitrary charge. The dimensions are `[J_(B)]=energy`, `[J_(γ,B)]=energy²`, `[ℛ]=1`, and `[ℰ]=energy`.

### Theorem LC-T

Under the assumptions of §1, with `e_(ch) ≠ 0` and real `χ ∈ L¹`,

```text
ℛ_(χ)<∞ ⇔ χ ∈ L²(ℝ),
ℰ_(total)<∞ ⇔ ℰ_(γ)<∞ ⇔ χ ∈ H^(1/2)(ℝ),
(1)/(2)ℰ_(total) ≤ ℰ_(γ) ≤ ℰ_(total).

(LC8)
```

**Proof.** By LC-U, `J_(∞)/2 ≤ J_(B) ≤ 2J_(∞)` for sufficiently large `Ω`, and `J_(∞)>0`. At low frequencies, `J_(B)` and `∣ hat(χ) ∣ ≤ ‖χ‖_(1)` are bounded. Finiteness of the response is therefore equivalent to the positive high-frequency Fourier tail belonging to `L²`. The reality of `χ` makes the moduli at positive and negative frequencies symmetric, so the converse direction of Plancherel also applies. Energy introduces the weight `Ω`. Combined with low-frequency boundedness, this is equivalent to `∫(1+Ω²)^(1/2)∣ hat(χ) ∣²dΩ<∞` over the full Fourier space.

Furthermore, at `∣z∣ ≤ Ω`,

```text
ω-(Ω)/(2)=(MΩ+z²)/(2(Ω+M)) ≥ 0,
Ω-ω=(Ω²-z²)/(2(Ω+M)) ≥ 0.
```

Multiplying this inequality by the positive integration weight gives the comparison between the two energies and the equivalence for photon energy. □

This iff does not extend unchanged to `e_(ch)=0` or to complex switching. If the charge is 0, all responses are 0; complex switching lacks symmetry between the positive and negative Fourier tails. `χ ∈ L¹` is an assumption actually used for low-frequency control and the Fourier definition.

**Final correction to the scope of the comparison inequality.** The upper bound `ℰ_(γ) ≤ ℰ_(total)` in (LC8) is restricted to rest and fails for moving states (W04). The lower bound `ℰ_(γ) ≥ ℰ_(total)/2` holds for every normalized packet by the Lipschitz argument in §5.8. The earlier S4 description “rest only” does not apply to the lower bound. LM-T extends the iff statements for response and total excitation energy to every normalized packet.

### 4.1 Distinct logarithmic coefficients for sharp switching

If `χ=𝟙_([0,T])` and `T>0`, then `∣ hat(χ) ∣²=4 sin²(Ω T/2)/Ω²`. Consequently, `ℛ_(T)` is finite, whereas both energies diverge. For any fixed reference energy `Ω_(0)>0`,

```text
ℰ_(total,Λ)=2J_(∞) log (Λ/Ω_(0))+o( log (Λ/Ω_(0))),
ℰ_(γ,Λ)=J_(∞) log (Λ/Ω_(0))+o( log (Λ/Ω_(0))),
(J_(γ,B)(Ω))/(Ω) → (J_(∞))/(2).

(LC9)
```

**Proof.** At fixed `z`, `ω/Ω → 1/2`, and `0 ≤ ω/Ω ≤ 1` throughout the shell. The same dominated-convergence argument as in LC-U gives the final limit. Use `4 sin²(Ω T/2)=2(1- cos Ω T)`. The cosine integral `∫_(Ω_(0))^(Λ) cos (Ω T)dΩ/Ω` of the constant plateau is bounded, and only the mean term contributes `log Λ`. Since the plateau error is `o(1)`, its integral is `o( log Λ)`. The photon expression contains half the plateau and therefore half the coefficient. □

Verifier V06 compares the increments at `T=1` and cutoffs `1000 → 2000` with both coefficients, allowing finite errors. This cannot replace a universal asymptotic proof. R01 separately checks the error of confusing a total-energy calculation with a photon-detector result.

### 4.2 Gaussian switching, boundary-dependent time orders, and numerical table

```text
χ_(τ)(t)=e^(-t²/(2τ²)), | hat(χ)_(τ)(Ω)|²=2πτ²e^(-τ²Ω²),
ℛ_(τ)=2πτ∫_(0)^(∞) J_(B)(x/τ)e^(-x²)dx.

(LC10)
```

At `τ → ∞`, LC-I can be applied to this integral. Near the origin, `J_(B) ≤ CΩ³`, while PEC gives `J_(B) ≤ CΩ⁵` under the additional first-moment assumption. Outside that region, use the global boundedness from LC-U and the Gaussian tail. Since `∫_(0)^(∞) x³e^(-x²)dx=1/2` and `∫_(0)^(∞) x⁵e^(-x²)dx=1`, this gives (LC12) below.

The numerical cross-check uses the photon radius `r=ω` and direction cosine `u=z/r`. Writing `A=Ω(Ω+2M)` and `W=Ω+M`,

```text
r(u)=(A)/(W+√(W²-Au²)), E_(f)(u)=√(M²+r(u)²(1-u²)),
J_(B)(Ω)=(e_(ch)²)/(8π²)∫_(-1)¹
(r(u)B(r(u)u))/(1+r(u)(1-u²)/E_(f)(u))
(r(u)²(1-u²))/(2E_(f)(u)(E_(f)(u)+M))(1+u²) du.

(LC11)
```

Here the delta Jacobian is `1+r(1-u²)/E_(f)`. Equation (LC11) is integrated separately without calling the code for (LC4). The comparison covers 27 points across `(M,a)=(1,1),(0.7,1.9),(2.3,0.4)`, `Ω=0.07,0.8,4.2`, and the three mode families.

```text
L_(free)(τ)=(e_(ch)²)/(20π M²τ²),
L_(PMC)(τ)=(e_(ch)²)/(10π M²τ²),
L_(PEC)(τ)=(e_(ch)²d²)/(21π M²τ⁴),
ℛ_(B,τ) ∼ L_(B)(τ).

(LC12)
```

The following values are computed directly at `M=a=e_(ch)=1` and `d=1`. For the M67 parameter correspondence, this is a comparison point with `m=√(5)/2`, not a value adjusted to an observational target. The final column, `leading_family`, is the **entire leading term for the corresponding mode** in (LC12). `τ²` is not applied to PEC.

<!-- NUMERIC-TABLE -->
| mode | J(1) | R_tau1 | R_tau1000 | R_tau1000 / leading_family(tau1000) |
|---|---:|---:|---:|---:|
| free | 0.00111771541068 | 0.00284979225075 | 1.58752752223e-08 | 0.997472960239 |
| PEC | 0.000329409703373 | 0.000887533499119 | 1.51106759525e-14 | 0.996903359828 |
| PMC | 0.00190602111798 | 0.00481205100237 | 3.17505353338e-08 | 0.997472485523 |
<!-- /NUMERIC-TABLE -->

For the exponential profile, the response at finite `τ` is positive and its adiabatic limit is 0. For general profiles with e_ch≠0, the positive UV plateau in LC-U and the Gaussian factor, positive at every frequency, give the same positivity. This is compatible with the prohibition of vacuum on-shell intraband radiation in a massive positive band. Indeed, `E(k)-E(k-p)<∣p∣ ≤ ω`, so no nontrivial on-shell radiation exists. The declared switching supplies the finite-time mismatch energy. Switching is not treated as a clock derived from the Z-Spin action.

**Scope clarification in v1.2 (S2).** The `τ⁻²` and `τ⁻⁴` laws in the table and (LC12), and the statement that the adiabatic limit is 0, are results of the `k=0` plane-wave prescription. LM-A governs the long-time response of a normalized packet: free/PMC converges to a constant different from 0 `π∫∣φ∣²c_(B)` or diverges, while PEC has a finite coefficient at rate `τ⁻²`, or slower decay, depending on its `E²`-moment.

The claim that the relative error in the asymptotic leading term is always `O(τ⁻²)` is withdrawn. For the exponential free example, `1-ℛ_(τ)/L_(free)` is approximately 0.0248263, 0.0125355, and 0.00252704 at `τ=100,200,1000`, displaying first-order `τ⁻¹` behavior. A universal error rate requires additional profile moments and control of the remainder.

## 5. Moving-packet sector — LM

### 5.1 Setup and observables

Retain the assumptions of §1 and take the initial state to be one positive-band particle with normalized `φ ∈ L²(ℝ²)`. In (LC3), only the initial momentum `k=k_(f)+p` contributes to fixed `(k_(f),p,z)`, so there are no cross terms. The response and energies are therefore diagonal in `k`.

```text
ℛ_(χ)(φ)=∫|φ(k)|²ℛ_(χ)(k) d²k,
ℛ_(χ)(k)=∫_(0)^(∞) J_(B)(Ω;k)| hat(χ) (Ω)|²dΩ,
J_(B)(Ω;k)=(e_(ch)²)/(2(2π)³)∫(d²p dz)/(ω)B(z) 𝒯(k,p,z) δ(Ω-E(k-p)-ω+E(k)).
```

`ℰ_(total)(φ)` and `ℰ_(γ)(φ)` are the same integrals with weights `Ω` and the photon frequency `ω`, respectively. Since `E(k)-E(k-p)<∣p∣ ≤ ω`, `Ω>0`. The notation is `E=E(k)`, `v=∣k∣/E`, `K=(E,k)`, `K_(f)=(E_(f),k_(f))`, `k_(f)=k-p`, `N=Ω(2E+Ω)`, `s=M²+N`, `γ_(c)=(E+Ω)/√(s)`, and `β_(c)=∣k∣/(E+Ω)`. The inner product `K· K_(f)=EE_(f)-k· k_(f)` is the 2+1-dimensional Minkowski inner product.

### 5.2 Current identities and two exact representations — LM-K

**Theorem LM-K.** For all `k,p ∈ ℝ²` and `z ∈ ℝ`,

```text
𝒯(k,p,z)=(K· K_(f)-3M²)/(2EE_(f))+|j⁰|² (Ω(2ω-Ω))/(ω²),
|j⁰|²= tr [P_(+)(k_(f))P_(+)(k)]=(EE_(f)+k· k_(f)+M²)/(2EE_(f)),
K· K_(f)-M²=ωΩ-(Ω²+z²)/(2).

(LM1)
```

Furthermore, let `n_(∥)` be the planar component and `u` the normal component of the photon direction `n ∈ S²`, and set `D=E+Ω-k· n_(∥)`. Then

```text
ω=(N)/(D+√(Δ)), Δ=D²-u²N, ∂_(ω)(E_(f)+ω)=(√(Δ))/(E_(f)),
J_(B)(Ω;k)=(e_(ch)²)/(16π³)∫_(S²)ω B(ω u) 𝒯 (E_(f))/(√(Δ)) d²n,

(LM2)
```

```text
J_(B)(Ω;k)=(e_(ch)²)/(16π³√(s))∫_(|z|<√(s)-M)dz B(z)∫_(0)^(2π)dθ* E_(f) 𝒯,
ω=γ_(c)(ω*+β_(c)p* cos θ*), ω*=(N+z²)/(2√(s)), p*²=([N-z(2M+z)][N+z(2M-z)])/(4s).

(LM3)
```

**Proof.** Set `j⁰=u_(+)(k_(f))† u_(+)(k)` and `j^(a)=u_(+)(k_(f))†σ_(a)u_(+)(k)`. The sum over the two polarizations is `𝒯=∣j∣²-∣p· j∣²/ω²`. The eigenvalue equation and `h(k_(f))-h(k)=-p·σ` give `p· j=(E-E_(f))j⁰=(ω-Ω)j⁰`. This is planar current conservation. The planar Pauli sum `Σ_(a=x,y)σ_(a)(h·σ)σ_(a)=-2h_(z)σ_(z)` and the trace formula give `∣j∣²-∣j⁰∣²=(K· K_(f)-3M²)/(2EE_(f))` and `∣j⁰∣²=(EE_(f)+k· k_(f)+M²)/(2EE_(f))`. Combining the two expressions gives the first formula in (LM1). If `Q=K-K_(f)=(ω-Ω,p)`, then `Q²=z²-2ωΩ+Ω²`, and `K· K_(f)=M²-Q²/2` gives the final formula. This form can be evaluated without cancellation at large `∣k∣`.

Equation (LM2) follows as follows. The derivative of `g(ω)=E(k-ω n_(∥))+ω` is `1+n_(∥)·(p-k)/E_(f)`; since `∣n_(∥)·(p-k)∣<E_(f)`, `g'>0`. Thus the physical root is unique. We have `Q(ω)=(E+Ω-ω)²-E_(f)(ω)²=u²ω²-2Dω+N`, and `Q>0` for `ω ≥ 0` below the physical root `ω_(0)`. Therefore `ω_(0)` is the smaller root `N/(D+√(Δ))`, and `g'(ω_(0))=(D-u²ω_(0))/E_(f)=√(Δ)/E_(f)`. The radial integral `∫ω²dω δ/ω` gives (LM2).

Equation (LM3) follows from planar momentum conservation and the 2+1-dimensional invariant 2-body phase space `∫(d²p)/(2ω)(d²k_(f))/(2E_(f))δ³(P-p-k_(f))=∫ dθ*/(4√(s))`, `P=(E+Ω,k)`, and `P²=s` with masses `M,∣z∣`. Numerical route 2 uses `tan (θ*/2)=ρ tan (ψ/2)`, `ρ²=(A+B)/(A-B)`, `A=γ_(c)ω*`, and `B=γ_(c)β_(c)p*`. Then `dθ*/(A+B cos θ*)=dψ/√(γ_(c)²z²+p*²)` (C14). At `k=0`, (LM2) and (LM3) reduce to (LC4) and (LC11). □

**Third exact representation (analytic elimination of the angular integral).** The `θ*` integral in (LM3) can be evaluated in closed form. Set `W=E+Ω`, `C=(Ω²+z²)/2`, `A_(0)=2EW+C`, and `B_(0)=2E+Ω`, and insert `K· K_(f)-M²=ωΩ-C` and `E_(f)=W-ω` into (LM1). Then

```text
E_(f) 𝒯=(1)/(2E)[Ωω-C-2M²-2B_(0)Ω+(2A_(0)Ω+B_(0)Ω²)/(ω)-(A_(0)Ω²)/(ω²)],
```

and, for `ω=a_(0)+b_(0) cos θ*`, `a_(0)=γ_(c)ω*`, `b_(0)=γ_(c)β_(c)p*`, and `a_(0)²-b_(0)²=γ_(c)²z²+p*²`, we have `⟨ω⟩=a_(0)`, `⟨ω⁻¹⟩=(a_(0)²-b_(0)²)^(-1/2)`, `⟨ω⁻²⟩=a_(0)(a_(0)²-b_(0)²)^(-3/2)`, and `⟨ω²⟩=a_(0)²+b_(0)²/2`. Thus `J_(B)` and `J_(γ,B)` become 1-dimensional integrals over `z`. This reduction was presented by the v1.2 auditor (OpenAI Codex) in Appendix B of the audit report; the authors symbolically rechecked the identities and angular averages (C15). The verifier implements this as **route 3**, evaluating the normal direction by adaptive quadrature with the substitution `z=a tan θ` and reporting an error estimate.

C11 symbolically checks the two trace identities as polynomial remainders under the relation `E²,E_(f)²`. V11 compares (LM2), (LM3), and route 3 at 54 moving-state points using different coordinates and tensor formulas; the maximum relative difference among the three routes is `5.3 × 10⁻¹⁴`. Their `k=0` reductions differ from (LC4) by at most `4.1 × 10⁻¹³` at 9 points.

### 5.3 Uniform bound — LM-B

**Lemma LM-B0 (monotonicity of the CM denominator, introduced in version B).** Let `q(z):=p*(z)/γ_(c)`. For every `∣z∣<z_(max)`,

```text
z²+q(z)²-q(0)²=(z²(4|k|²+4EΩ+2Ω²+z²))/(4(E+Ω)²) ≥ 0,

G(z):=(Ω)/(√(z²+q(z)²)) ≤ G(0)=(2(E+Ω))/(2E+Ω) ∈ (1,2].

(LM18)
```

**Proof.** We have `q(0)=N/(2(E+Ω))`. Substituting `p*²=[(N-z²)²-4M²z²]/(4s)` and `γ_(c)²=(E+Ω)²/s` and expanding gives the identity above. The bracket on the right-hand side is positive, so the denominator is minimized at `z=0`. We have `G(0)=Ω/q(0)=2(E+Ω)/(2E+Ω)`, `2-G(0)=2E/(2E+Ω)>0`, and `G(0)-1=Ω/(2E+Ω)>0`. □

**Theorem LM-B.** Under the assumptions of §1, for all `k ∈ ℝ²` and `Ω>0` and all three mode families,

```text
0 ≤ J_(B)(Ω;k) ≤ 18 J_(∞),
J_(B)(Ω;k) ≤ Ω[(18J_(∞))/(M)+(e_(ch)²‖B‖_(∞))/(2π²) log((14E(k))/(M)) ], ‖B‖_(∞) ≤ 2.

(LM4)
```

**Proof.** (i) *Decomposition.* Denote the first term in (LM1) by `𝒯_(1)` and the second by `𝒯_(2)`. Since `K· K_(f) ≥ M²`, `𝒯_(1) ≤ (K· K_(f)-M²)/(2EE_(f))`. We have `∣j⁰∣² ≤ 1`, and `Ω(2ω-Ω)/ω²=1-(1-Ω/ω)² ≤ 1` implies `𝒯_(2) ≤ min {1, 2Ω/ω}`. Both bounds hold pointwise, and the integration weight is positive.

(ii) *The `𝒯_(1)` part.* In the CM frame, the direction of `k_(f)*` is uniform with respect to `θ*`, so `∫_(0)^(2π)(K· K_(f)-M²)dθ*=2π(E*E_(f)*-M²)`. Here `E*=K· P/√(s)=(M²+EΩ)/√(s)` and `E_(f)*=(s+M²-z²)/(2√(s)) ≤ √(s)`. Using `(M²+EΩ)/E ≤ M+Ω` and `∫ B dz=2π‖ρ‖_(2)²`, this part is bounded by `e_(ch)²‖ρ‖_(2)²(M+Ω)/(8π√(s))=2J_(∞)(M+Ω)/√(s)`. Since `s-(M+Ω)²=2Ω(E-M) ≥ 0`, `√(s) ≥ M+Ω`, and this part is therefore at most `2J_(∞)`.

(iii) *The `𝒯_(2)` part.* Since `E_(f) ≤ E+Ω` and `∫_(0)^(2π)dθ*/ω=2π/√(γ_(c)²z²+p*²)`, `𝒯_(2) ≤ 2Ω/ω` and `(E+Ω)/(√(s) γ_(c))=1` bound this part by `(e_(ch)²/4π²)∫ B(z)G(z) dz`. Equation (LM18) gives `G ≤ G(0) ≤ 2`, hence

```text
(e_(ch)²)/(4π²)∫ B(z)G(z) dz ≤ (e_(ch)²)/(4π²) G(0) 2π‖ρ‖_(2)²=8J_(∞) G(0) ≤ 16J_(∞) .
```

The sum is `18J_(∞)`.

(iv) *Soft form.* Suppose `Ω ≤ E`. We have `(K· K_(f)-3M²)⁺ ≤ K· K_(f)-M² ≤ ωΩ`. Using `∫ dθ*ω=2πγ_(c)ω* ≤ 2πγ_(c)N/√(s)`, `z_(max)² ≤ N`, and `s^(3/2) ≥ 2EΩ M`, the first part is at most `6J_(∞)Ω/M`.

The logarithmic integral does not use `q(z) ≥ q(0)`. For `∣z∣ ≤ z_(max)/2`,
`s-(M+∣z∣)² ≥ N/2` and `s-(M-∣z∣)² ≥ N/2`. The first expression follows because the gap at the endpoint is `(√(s)-M)²/4 ≥ 0` and decreases over the interval. For the second, use `(M-∣z∣)² ≤ M²` if `∣z∣ ≤ 2M`, and `(M-∣z∣)² ≤ z_(max)²/4 ≤ N/4` otherwise. Therefore `p*(z) ≥ p*(0)/2` and `q(0)=N/[2(E+Ω)] ≥ Ω/2`, and
```text
G(z) ≤ (Ω)/(√(z²+Ω²/16))
(|z| ≤ z_(max)/2),
G(z) ≤ (Ω)/(|z|)
(|z|>z_(max)/2).
```
Integrating each expression over the half-line and doubling by evenness bounds the second part by
```text
(e_(ch)²‖B‖_(∞))/(2π²)Ω
[ arsinh((2z_(max))/(Ω)) + log 2]
≤ (e_(ch)²‖B‖_(∞))/(2π²)Ω log((14E)/(M))
```
The last inequality uses `z_(max) ≤ 3EΩ/(2M)`, `arsinh x ≤ log (2x+1)`, and `E/M ≥ 1`. For `Ω>E ≥ M`, `J ≤ 18J_(∞) ≤ 18J_(∞)Ω/M`. These two regions and `6 ≤ 18` give (LM4). `‖B‖_(∞) ≤ 2` follows from `‖ρ‖_(1)=1`. □

**Integration correction.** Part (iv) of the attached v1.4-B stated `G ≤ Ω/√(z²+q(0)²)`. This does not follow from (LM18). If `M=E=Ω=1, z=1/2`, then `q(z)²=105/256<q(0)²=9/16`, so the actual `G=16/13 ≃ 1.23077` exceeds its proposed right-hand side `4/√(13) ≃ 1.10940`. W10 checks both this exact counterexample and the repaired inner bound above. The proof of the constant 18 in parts (i)–(iii) remains valid independently of this error.

The constant 18 is not claimed to be optimal. V14 covers four `(M,a)` pairs × 9 momenta × 8 frequencies × three mode families, or 864 points in total. The largest observed `J/J_(∞)` is 4.069420334, and the soft-bound ratio is approximately 0.525273. Recomputing the extended search point `(M,a,∣k∣,Ω/E)=(1,2.401,1.4739 × 10⁷,2.56 × 10⁻⁷)`, PMC, from the attached v1.4-B with a 50-digit angular average gives **4.1102159588** (W09). Its relative difference from the 256-node CM route is approximately `2.35 × 10⁻⁹`. This number is not an interval certificate; §5.12 distinguishes it from the rigorous lower bound `64/(5π)>4` and the global upper bound 18.

### 5.4 Temporal regularity of every packet — LM-T

**Theorem LM-T.** For `e_(ch) ≠ 0`, real `χ ∈ L¹(ℝ)`, and normalized `φ ∈ L²(ℝ²)`,

```text
ℛ_(χ)(φ)<∞ ⇔ χ ∈ L²,
ℰ_(total)(φ)<∞ ⇔ χ ∈ H^(1/2),
∫|φ|²E d²k<∞, χ ∈ H^(1/2) ⇒ ℰ_(γ)(φ) ≤ ℰ_(total)(φ)+∫|φ(k)|²(E(k)-M)ℛ_(χ)(k) d²k<∞ .

(LM5)
```

**Proof.** LM-B gives `ℛ_(χ)(k) ≤ 18J_(∞)∫_(0)^(∞)∣ hat(χ) ∣²dΩ=18π J_(∞)‖χ‖_(2)²`. This bound is uniform in `k`, so it can be integrated against `∣φ∣²`. The converse follows from LM-R(a). At each `k`, `J_(B)(Ω;k) → J_(∞)>0`; therefore, if `χ ∉ L²`, then `ℛ_(χ)(k)=∞` for every `k`, and `ℛ_(χ)(φ)=∞`. For energy, insert the weight `Ω` and use the same low-frequency boundedness as in LC-T. Bound photon energy by `ω ≤ Ω+E-M`, which follows from `E_(f) ≥ M`. □

LC-T in v1.1 was a criterion for the plane-wave prescription at `k=0`. LM-T gives the same criterion for **every normalized packet**, with constants independent of packet shape. LM-E closes the necessary condition for photon energy as `χ ∈ H^(1/2)`. Within the packet class `∫∣φ∣²E<∞`, this condition is necessary and sufficient. The optimal packet condition outside that class remains OPEN.

### 5.5 Soft theorem and classical correspondence — LM-S

**Theorem LM-S.** Fix `k ≠ 0` and suppose `0<v<1`. As `Ω ↓ 0`, `J_(B)(Ω;k)=c_(B)(v)Ω^(p_(B))(1+o(1))`, with `p_(free)=p_(PMC)=1` and `p_(PEC)=3`.

```text
c_(free)(v)=(e_(ch)²)/(2π²)((artanh v)/(v)-1),
c_(PMC)=2c_(free),
c_(PEC)(v)=(e_(ch)²d² [3v-2v³-3(1-v²) artanh v])/(3π²v³(1-v²)).

(LM6)
```

For general profiles, the free/PMC coefficient is proportional to `B(0)=1,2`, while PEC requires a finite first moment `d`.

**Proof.** Set `μ=n· hat(k)` in (LM2). If `Ω ≤ E(1-v)²/6`, then `D ≥ E(1-v)`, `Δ ≥ E²(1-v)²/2`, `ω ≤ N/D ≤ 3Ω/(1-v)`, and `𝒯 ≤ 2`. Thus the integrand divided by `Ω` is bounded. Pointwise, `ω/Ω → (1-vμ)⁻¹`, `E_(f)/√(Δ) → (1-vμ)⁻¹`, and `B(ω u) → B(0)`. Moreover, `p → 0` gives `P_(+)(k_(f))σ_(a)P_(+)(k) → b_(a)P_(+)(k)`, hence `𝒯 → b_(∥)ᵀ(I-n_(∥) n_(∥)ᵀ)b_(∥)=v²(1-μ²)`. By dominated convergence,

```text
J_(B) ∼ (e_(ch)²B(0)v²Ω)/(16π³)∫_(S²)(1-μ²)/((1-vμ)²)d²n
=(e_(ch)²B(0)v²Ω)/(8π²)∫_(-1)¹(1-μ²)/((1-vμ)²)dμ
```

and the integral value `4( artanh v-v)/v³` gives the first formula. For PEC, `∣S(z)∣ ≤ d∣z∣` and `S(z)/z → d` give `B(ω u)/Ω² → 2d²u²(1-vμ)⁻²`. The azimuthal average `(1-μ²)/2` of `u²`, together with `∫_(-1)¹(1-μ²)²(1-vμ)⁻⁴dμ=8[3v-2v³-3(1-v²) artanh v]/(3v⁵(1-v²))`, gives the final formula (C12). □

At `v → 0`, `c_(free) ≈ e_(ch)²v²/(6π²)` and `c_(PEC) ≈ 2e_(ch)²d²v²/(15π²)`. At `γ → ∞`, `c_(free) ∼ (e_(ch)²/2π²) log 2γ` and `c_(PEC) ∼ e_(ch)²d²γ²/(3π²)` (`(1-v²)c_(PEC) → e_(ch)²d²/(3π²)`; C15). The first integral has the same `Ω → 0` form as the photon-number spectrum emitted by the classical current `e_(ch)vχ(t)δ²(x-vt)ρ(y)` with velocity `v`. `(1-vμ)⁻²` is the formation factor for edge/transition radiation. PEC suppression by `Ω²` agrees with the classical picture of an antiparallel image current for a tangential current, while the factor of 2 for PMC agrees with a parallel image current. V12 confirms that the six ratios from the two routes at `Ω=10⁻⁴` and `∣k∣ ∈ {0.5,2}` each lie within `[0.999655,0.999872]`. **The soft factor itself is subsumed by the known edge-radiation factor and is not claimed as novel** (§7).

### 5.6 Adiabatic limit and moment classification — LM-A

**Theorem LM-A.** Assume `e_(ch) ≠ 0` throughout. Let `χ_(τ)(t)=e^(-t²/(2τ²))`, and let `φ ∈ L²(ℝ²)` be a normalized packet.

(a) **free/PMC.**

```text
lim_(τ → ∞)ℛ_(τ)(φ)=π∫|φ(k)|²c_(B)(v(k)) d²k (∫|φ|² log (E/M)<∞),
∫|φ|² log (E/M)=∞ ⇒ ℛ_(τ)(φ) → ∞ .
```

(b) **PEC** (finite first moment `d`). Finiteness of the `E²`-moment is equivalent to the existence of a finite limit of `τ²ℛ_(τ)(φ)`.

```text
∫|φ|²E²<∞ ⇒ τ²ℛ_(τ)(φ) → π∫|φ|²c_(PEC)<∞;
∫|φ|²E²=∞ ⇒ τ²ℛ_(τ)(φ) → ∞ .

(LM7)
```

(c) **PEC: decay itself.** Under finite `d`, every normalized packet satisfies `ℛ_(τ)(φ) → 0`. The proof removing the log-moment restriction of v1.3 is LM-D in §5.9. The same decay also holds under the weaker profile assumption `I_(ρ)<∞` alone.

The first limit in (a) is positive if `φ ≠ 0`. In the second cases of both (a) and (b), `ℛ_(τ)(φ)` is still finite at each `τ` by LM-T. Version v1.2 stated the first assertion of (b) under an `E³`-moment assumption but omitted that condition in the abstract and F5 (Appendix C, Round 3, F01). Since `E ≥ M`, the `E³`-moment condition implies the `E²`-moment condition; the `E²`-moment is now the necessary and sufficient condition for a finite limit.

**Proof.** We have `ℛ_(τ)(k)=2π∫_(0)^(∞)τ J_(B)(x/τ;k)e^(-x²)dx`.

(a) The soft form of LM-B gives `τ J_(B)(x/τ;k) ≤ A_(B)(k)x`, and `A_(B)(k)=18J_(∞)/M+(e_(ch)²‖B‖_(∞)/2π²) log (14E/M)` (at `Ω>E`, `J_(B) ≤ 18J_(∞) ≤ 18J_(∞)Ω/M`, so the same bound holds for every `Ω`). LM-S gives `τ J_(B)(x/τ;k) → c_(B)(v)x`, and dominated convergence in `x` yields `ℛ_(τ)(k) → π c_(B)(v)`. If the log-moment is finite, `π A_(B)(k)` dominates the integrand with respect to `k`. Otherwise, `artanh v/v ≥ artanh v= log ((1+v)γ) ≥ log (E/M)` implies `c_(free) ≥ (e_(ch)²/2π²)( log (E/M)-1)`. Fatou's lemma makes the limit inferior infinite.

(b) First construct an `Ω³` dominating function valid for all `Ω>0` and all `k`. Write `√(s)=R` and `z_(m)=√(s)-M`, and insert `B_(PEC)(z) ≤ 2d²z²` into parts (i)–(iii) of LM-B. Let `0<Ω ≤ M`. Since `𝒯_(1) ≤ (K· K_(f)-M²)/(2EE_(f)) ≤ ωΩ/(2EE_(f))` (C15: `ωΩ-(K· K_(f)-M²)=(Ω²+z²)/2 ≥ 0`), the `θ*` integral `∫ω dθ*=2πγ_(c)ω*` in (LM3), together with `ω* ≤ N/R` (`z² ≤ z_(m)² ≤ N`), `∫_(-z_(m))^(z_(m))2d²z²dz=4d²z_(m)³/3`, `N ≤ s`, `z_(m) ≤ R`, and `(E+Ω)/E ≤ 2`, gives

```text
J_(1)⁺ ≤ (e_(ch)²Ωγ_(c))/(16π²ER)∫_(-z_(m))^(z_(m))2d²z² ω*(z) dz
≤ (e_(ch)²d²Ωγ_(c)Nz_(m)³)/(12π²Es)
≤ (e_(ch)²d²Ω z_(m)²)/(6π²).
```

For the `𝒯_(2)` part, apply the outer bound `G ≤ Ω/∣z∣` from LM-B(iii) over the entire interval to obtain `J_(2)⁺ ≤ (e_(ch)²/4π²)∫_(-z_(m))^(z_(m))2d²z²(Ω/∣z∣)dz=e_(ch)²d²Ω z_(m)²/(2π²)`. These are positive upper bounds; the two summands themselves need not each be positive. Their sum is `(2/3)e_(ch)²d²Ω z_(m)²/π²`, and `z_(m)=N/(R+M) ≤ Ω(2E+Ω)/(2M) ≤ 3EΩ/(2M)` (`Ω ≤ E`; C15), hence

```text
0 ≤ J_(PEC)(Ω;k) ≤ (3e_(ch)²d²E(k)²)/(2π²M²) Ω³ (0<Ω ≤ M),
(J_(PEC)(Ω;k))/(Ω³) ≤ H(k):=(3e_(ch)²d²E(k)²)/(2π²M²)+(18J_(∞))/(M³) (Ω>0).

(LM10)
```

The `Ω>M` part of the second expression is `J ≤ 18J_(∞) ≤ 18J_(∞)Ω³/M³` from LM-B. Then `τ³J_(PEC)(x/τ;k) ≤ H(k)x³` and `∫_(0)^(∞) x³e^(-x²)dx=1/2`. LM-S gives `τ³J_(PEC)(x/τ;k) → c_(PEC)(v)x³`, so dominated convergence in `x` yields `τ²ℛ_(τ)(k) → π c_(PEC)(v)`. Since `H(k)=O(E²)`, if `∫∣φ∣²E²<∞`, then `π H(k)` dominates `k`, giving the first limit. Conversely, `(1-v²)c_(PEC) → e_(ch)²d²/(3π²)`, and `c_(PEC)` is continuous and positive on `(0,1)`, so there exists `E_(0)` such that `c_(PEC) ≥ e_(ch)²d²E²/(6π²M²)` on `E ≥ E_(0)`. If `∫∣φ∣²E²=∞`, then `∫∣φ∣²c_(PEC)=∞`; applying Fatou to the nonnegative integrand `∣φ∣²τ²ℛ_(τ)(k)` gives `liminf τ²ℛ_(τ)(φ)=∞`.

(c) uses `π C_(ρ)` from §5.9, uniformly in momentum. The proof of LM-D does not depend on LM-A(c), so the argument is not circular. □

The bound in (LM10) is the authors' rederivation of the argument in Appendix A of the v1.2 audit report. C15 checks its integer and rational constants and identities; V17 checks it on a grid (360 points; maximum `J_(PEC)/(Ω³H)` of 0.204). The necessary and sufficient condition for a finite PEC limit of `τ²ℛ_(τ)` is the `E²`-moment. Section 5.9 resolves decay itself without packet-moment assumptions. V15 computes the ratios of `τ=300,3000` at `∣k∣=1` using route 3: free 0.995792→0.999577, PMC 0.995785→0.999576, and PEC (with the `τ²` correction) 0.990141→0.999008.

**Normalized-packet counterexample 1 (W05: breakdown of the rest law).** Let `∣φ(k)∣²=e^(-∣k∣²/σ²)/(πσ²)`, `σ=0.3`, `τ=1000`, free, and `M=a=e_(ch)=1`.
- Computed response: `ℛ_(τ)(φ)=0.00446923`
- Rest law (LC12): `1/(20πτ²)=1.59155e-08` (ratio `2.808e+05`)
- LM-A prediction: `π∫∣φ∣²c_(free)=0.00447418` (ratio `0.998894`)

The leading estimate for a small momentum spread `⟨∣k∣²⟩ ≪ M²` is `π⟨ c_(free)⟩ ≈ e_(ch)²⟨∣k∣²⟩/(6π M²)`. Equating this to the rest law gives the crossover time `τ_(*) ≈ (0.3/⟨∣k∣²⟩)^(1/2)`. Thus the rest law describes a **transition region** visible only when the switching time is shorter than the inverse momentum spread of the packet. This crossover expression is a leading-order estimate, not a theorem.

**Normalized-packet counterexample 2 (W06: breakdown of the PEC `τ⁻²` rate).** Let `M=e_(ch)=a=1`, `d=1`, and `φ(k)=1/(√(π)(1+∣k∣²))`. The energy density of `∣φ∣²d²k` is `2/E³` on `E ≥ 1`, and

```text
∫|φ|²d²k=1, ∫|φ|²E=2, ∫|φ|² log (E/M)=(1)/(2), ∫|φ|²E²=∞ .
```

This packet is therefore normalized and has finite mean energy and log-moment, but (b) gives `τ²ℛ_(τ)(φ) → ∞`. Meanwhile, (c) gives `ℛ_(τ)(φ) → 0`. What fails is the `τ⁻²` **rate**, not decay itself. W06 symbolically checks the four moments and `∫∣φ∣²c_(PEC)=∞`; X01 diagnostically shows an increase from `τ=10,30,100` to `τ²ℛ_(τ)(φ)=0.186,0.370,0.607` (not a proof). This counterexample was presented in the v1.2 audit (F01).

### 5.7 Nonuniformity of the plateau — LM-R

**Theorem LM-R.** (a) At fixed `k`, as `Ω → ∞`, `J_(B)(Ω;k) → J_(∞)` and `J_(γ,B)(Ω;k)/Ω → J_(∞)/2`. (b) Fix `λ>0`. If `∣k∣ → ∞` and `Ω=λ E(k)`, then `J_(B)(λ E;k) → Φ(λ)J_(∞)`.

```text
Φ(λ)=4(1+λ)-(4λ+7)√((λ)/(λ+2))
=(4)/(π)∫_(0)^(π)[(1)/(2)+(1-2 cos²α+r_(1) cos α)/(2r_(2))](r_(2) dα)/(1+λ- cos α),
r_(1)=(λ(2+λ))/(2(1+λ- cos α)), r_(2)=1+λ-r_(1) .

(LM8)
```

We have `Φ(0⁺)=4` and `Φ(λ)=1+λ⁻¹+O(λ⁻²)`. Writing `r=√(λ/(λ+2)) ∈ (0,1)`, `Φ=r-4+8/(1+r)` is strictly decreasing in `r`, so `1<Φ(λ)<4` for every `λ>0` (C13).

**Proof.** Fix `z` in (LM3). Parts (ii) and (iii) of LM-B bound the `z` integrand by `C B(z)`, permitting dominated convergence.

(a) As `Ω → ∞`, `M,∣k∣,z` becomes small relative to `√(s)`, with `β_(c) → 0` and `γ_(c) → 1`. The CM angular average of the limiting tensor `(1+n· v_(∥))/2` from C02 is 1/2, and `E_(f)/√(s) → 1/2`. Thus the value at each `z` tends to `π/2`, and `J_(B) → e_(ch)²‖ρ‖_(2)²(π/2)/(8π²)=J_(∞)`. Inserting `ω/Ω → 1/2` into the same argument gives the photon expression.

(b) All kinematic quantities are homogeneous of degree 1 in `E`, while `𝒯` is homogeneous of degree 0. Since `γ_(c)=(1+λ)/√(λ(2+λ))` is bounded, `ω ≥ ω*/(2γ_(c))` even at backward angles. Thus the integrand converges boundedly to the massless, `z=0` configuration. Evaluated in the lab frame, this is an integral over the ellipse `∣p∣+∣k-p∣=∣k∣(1+λ)` with foci `0` and `k`. The radial Jacobian from the focus `0` is `r_(2)/(1+λ- cos α)`. The massless tensor is `(1)/(2)(1-c· b)+c· b-(c· hat(p) )(b· hat(p) )`. Together they give the integral in (LM8), with `J_(B) → e_(ch)²‖ρ‖_(2)²K/(8π²)` and `Φ=2K/π`. If `t= tan (α/2)`, the integrand becomes `(λ t²+λ+4t²)²/[(t²+1)²((λ+2)t²+λ)²]`, and elementary integration gives the closed form. □

C13 symbolically checks this reduction, the exact integrals `Φ(1/4)=7/3` and `Φ(1/12)=43/15`, the two limits, and the stable form `r-4+8/(1+r)` and its monotonicity. V13 confirms a maximum relative difference `5.3 × 10⁻¹³` between closed form and quadrature at six values of `λ`. The following values are direct evaluations of (LM3) at finite `∣k∣` (`M=a=e_(ch)=1`, free; route 3, quadrature error estimate `<2 × 10⁻¹¹`; V16 compares them with the 128/256-node values from route 2).

<!-- MOVING-TABLE -->
| kappa | lambda | J(lambda E; k) / J_inf | Phi(lambda) |
|---:|---:|---:|---:|
| 1000 | 1 | 1.64897093875 | 1.64914703891 |
| 10000 | 0.01 | 3.54317833361 | 3.54343668644 |
| 100000 | 0.001 | 3.84722194672 | 3.84742493773 |
<!-- /MOVING-TABLE -->

Thus `J_(∞)` in LC-U is a limit at fixed `k`, whereas in the window `max (M,a) ≪ Ω ≪ E(k)` a moving carrier sees a plateau near `Φ(λ)J_(∞)`, approaching `4J_(∞)`. `1<Φ<4` is a property of the fixed-`λ` limit, not a global bound at finite `k,Ω`. Indeed, the grid maximum `J/J_(∞)=4.0694` in V14 exceeds 4. The proved global bound is 18; the exact global bound between these values remains OPEN. The sharp-switching logarithmic coefficient `2J_(∞)` (total energy) remains the asymptotic coefficient for each `k`. For a heavy-tail packet, however, finite-cutoff increments follow the packet average of `Φ(Λ/E)`; no uniform asymptotic theorem for this behavior is presented.

### 5.8 Moving sector of the energy observables — LM-E

**Theorem LM-E.** Under the assumptions of §1, the following hold.

(a) **(Introduced in version B)** For every `k` and every on-shell point, `Ω ≤ 2ω`. (b) Consequently, for every normalized packet `φ` and real `χ ∈ L¹`, at least half of the total excitation energy lies in the photon sector.

```text
Ω ≤ 2ω ( every on-shell point ),

(1)/(2)ℰ_(total)(φ) ≤ ℰ_(γ)(φ) ( every normalized φ),

0<ω ≤ Ω+E(k)-M .

(LM19)
```

In particular, `ℰ_(γ)(φ)<∞ ⇒ χ ∈ H^(1/2)(ℝ)`.

(c) For `0<v<1` and free/PMC,

```text
lim_(Ω ↓ 0)(J_(γ,B)(Ω;k))/(Ω J_(B)(Ω;k))=(∫_(-1)¹(1-μ²)(1-vμ)⁻³dμ)/(∫_(-1)¹(1-μ²)(1-vμ)⁻²dμ)>1 .

(LM9)
```

**Proof.** (a) The dispersion `E(k)=√(∣k∣²+M²)` is 1-Lipschitz because `∣∇ E∣=∣k∣/E<1`. Let `p` be the planar photon momentum and `z` its normal component. Then `∣p∣ ≤ ω=√(∣p∣²+z²)`, and

```text
E_(f)=E(k-p) ≤ E(k)+|p| ≤ E(k)+ω
⇒
Ω=E_(f)+ω-E(k) ≤ 2ω .
```

The inequality is strict at finite `M>0` for a nonzero photon. For `z=0` and backward emission with planar photon momentum `p=-ω hat(k)`, taking `∣k∣/M → ∞` gives `E_(f)-E → ω`, approaching equality. The final fermion momentum `k-p` is then in the same direction as `k`. The second inequality follows from `E_(f) ≥ M`.

(b) By (a), the photon weight on the shell is `ω ≥ Ω/2`. Multiplication by the positive integration weight in (LC7) gives `J_(γ,B)(Ω;k) ≥ (1)/(2)Ω J_(B)(Ω;k)` pointwise. Integrating against `∣φ∣²` and `∣ hat(χ) ∣²` gives the first expression. LM-T gives `ℰ_(total)<∞ ⇔ χ ∈ H^(1/2)`, proving necessity.

(c) This is the same dominated-convergence argument as for `ω/Ω → (1-vμ)⁻¹` in the proof of LM-S. Subtracting the denominator from the numerator gives `v∫μ(1-μ²)(1-vμ)⁻³dμ`, which is positive after pairing `μ` and `-μ`. □

**Scope correction relative to v1.3 (T3).** S4 in v1.3 marked the **entire** comparison inequality `(1)/(2)ℰ_(total) ≤ ℰ_(γ) ≤ ℰ_(total)` as restricted to `k=0`. By (a), **the lower-half bound holds at every initial momentum**; only the upper bound fails at `k ≠ 0` (W04). Thus the “necessary condition for `ℰ_(γ)`” left OPEN in v1.3 is closed: **`χ ∈ H^(1/2)` is necessary.** The sufficient condition is `∫∣φ∣²E<∞` from LM-T, and its optimality (necessity) remains OPEN. The exact criterion for `ℰ_(γ)<∞` is now narrowed to the interval between “`H^(1/2)` necessary” and “`H^(1/2)` plus an E-moment sufficient.”

W04 checks two points. At `k=(3,0)`, `p=(1,0)`, and `z=0`, `ω/Ω=13.5519`, and the tensor is positive. The integrated ratio at `∣k∣=2` and `Ω=10⁻³` is `2.75094` (routes 2 and 3 agree within `10⁻⁸`), while the soft prediction is `2.75715`. Consequently, with narrow-band switching, `ℰ_(γ)` for a moving packet can exceed `ℰ_(total)`, because fermion kinetic energy is converted into photon energy. V21 checks 2268 on-shell points and 96 spectral points across the three mode families. The sampled maximum of `Ω/(2ω)` is 0.999999999777, and the sampled minimum of `J_(γ)/(Ω J)` is 0.5049509901. These are finite samples; the universal proof is the Lipschitz argument above.

**Complete criterion within the finite-mean-energy class.** Fix real `χ ∈ L¹`, nonzero charge, and `∫∣φ∣²E<∞`. Then
```text
ℰ_(γ)(φ)<∞ ⇔ χ ∈ H^(1/2)(ℝ).
```
Necessity requires no packet moment, while sufficiency uses the bound from LM-T. The same iff is not claimed for every packet with infinite mean energy. The comparison inequality is first interpreted in the extended-real order for nonnegative integrals; no subtraction of one infinite quantity from another is performed.

### 5.9 Moment-free PEC decay — LM-D

**Theorem LM-D (Dini bound).** In the model of §1, let `B=B_(PEC)` and

```text
I_(ρ):=∫_(ℝ)(B_(PEC)(z))/(|z|) dz<∞,
C_(ρ):=(18J_(∞))/(M)+(e_(ch)² I_(ρ))/(4π²).
0 ≤ J_(PEC)(Ω;k) ≤ C_(ρ)Ω (∀ k, ∀Ω>0).

(LM11)
```

This integrability is a sufficient condition and is not claimed to be necessary. A finite first moment `d=∫ yρ(y)dy` guarantees it. Indeed, for any `b>0`,

```text
I_(ρ) ≤ 2d²b²+(2π‖ρ‖_(2)²)/(b)<∞;
ρ(y)=ae^(-ay) ⇒ I_(ρ)=2.
```

For every normalized packet with Gaussian switching,

```text
0 ≤ ℛ_(τ)(φ) ≤ π C_(ρ),
lim_(τ → ∞)ℛ_(τ)(φ)=0,
φ ∈ L²(ℝ²), ‖φ‖_(2)=1.

(LM12)
```

No mean-energy, log-energy, or `E²` moment condition on the packet is imposed here. The Dini condition on the PEC profile remains a required assumption. Under finite (d), more specifically,

```text
ℛ_(τ)(φ) ≤
π∫ d²k |φ(k)|² min (C_(ρ),(H(k))/(τ²))
≤ (π)/(τ²)∫_(E ≤ K)|φ|² H d²k
+π C_(ρ) Pr_(φ)(E>K), K ≥ M,

(LM13)
```

holds. `H` is the explicit dominating function in (LM10). This is a packet-tail error bound usable at finite time.

**Proof.** The `G(z)=Ω/√(z²+p*²/γ_(c)²)` in LM-B(iii) satisfies `G ≤ Ω/∣z∣` for every `z ≠ 0`. A positive upper bound on the integral of `𝒯_(2)` is therefore `e_(ch)²Ω I_(ρ)/(4π²)`. At `Ω ≤ E`, the bound on the `𝒯_(1)` part is `6J_(∞)Ω/M` from LM-B(iv). If `Ω>E ≥ M`, the full `J ≤ 18J_(∞) ≤ 18J_(∞)Ω/M`. These two regions give (LM11). This uses a bound on the sum for the original positive `𝒯`, without assuming that `𝒯_(1),𝒯_(2)` are individually positive.

Using `B_(PEC) ≤ 2d²z²` at `∣z∣ ≤ b` and `1/∣z∣ ≤ 1/b` outside gives the Dini bound. For the exponential profile, `B=2a²z²/(a²+z²)²`, so `I_(ρ)=4a²∫_(0)^(∞) z/(a²+z²)²dz=2` (C16).

At fixed `k`, `B_(PEC)(0)=0`. Along the photon-sphere route in the proof of LM-S, the integrand divided by `J/Ω` tends to 0 by dominated convergence, using `B(ω u) → 0`, bounded `B`, and fixed `v<1`. This step does not require finite (d). `k=0` is handled by boundedness along the same spherical route. Now `τ J(x/τ;k) ≤ C_(ρ) x` and `∫_(0)^(∞) xe^(-x²)dx=1/2`, so applying dominated convergence first in `x` and then in `k` gives (LM12). Under finite (d), integrating (LM10) also gives `ℛ_(τ)(k) ≤ π H(k)/τ²`. Taking the smaller of the two pointwise bounds and splitting into `E ≤ K` and `E>K` gives (LM13). □

**Closure of an existing open problem.** The log-moment condition required by LM-A(c) in v1.3 is removed for PEC with finite (d). For example, take `M=1` and the energy density

```text
f(E)=(𝟙_(E ≥ exp (1)))/(E( log E)²),
|φ(k)|²=(f(E(k)))/(2π E(k))
```

which is normalized by `d²k=2π E dE` and satisfies `⟨ log E⟩=∞` (W07). The free/PMC response of this same packet diverges by LM-A(a), whereas its PEC response tends to 0. Its mean energy is infinite, so it is not used as an example of physical preparation at finite energy. LM-P supplies a slow-decay example with finite mean energy.

### 5.10 The `EΩ` boundary layer and nonuniformity over packets — LM-L

**Theorem LM-L.** For a PEC profile with finite (d), fix `E → ∞`, `Ω=η/E`, and `0<η<∞`. This differs from the fixed-`Ω/E=λ` UV limit of LM-R. Define the following positive function.

```text
s_(η)=M²+2η, r_(η)=√(s_(η)), b_(η)=r_(η)-M,
K_(η)(z)=(4η r_(η))/(z)-2s_(η)+(η²)/(s_(η))
-(M²+η)/(2s_(η))z²,
L_(ρ)(η)=(e_(ch)²)/(8π²r_(η)η)
∫_(0)^(b_(η))B_(PEC)(z)K_(η)(z) dz
= lim_(E → ∞)(J_(PEC)(η/E;√(E²-M²)))/(η/E).

(LM14)
```

By rotational symmetry, the direction of the vector `k` is immaterial. Writing `r=r_(η)`,

```text
K_(η)'(z)<0,
K_(η)(b_(η))=(M(M²-2Mr+5r²))/(2r)>0.
```

Consequently, `L_(ρ)(η)>0`. Since `d>0`, `S(z)/z>0` for sufficiently small positive `z`. This function satisfies the following two asymptotic formulas and global bound.

```text
L_(ρ)(η) ∼ (e_(ch)²d²)/(3π²M²)η² (η ↓ 0),
L_(ρ)(η) → L_(∞)^(layer):=(e_(ch)²I_(ρ))/(4π²) (η → ∞),
0<L_(ρ)(η) ≤ min (C_(ρ),Aη²),
A=(3e_(ch)²d²)/(2π²M²).

(LM15)
```

Here `L_(∞)^(layer)` and the UV spectrum `J_(∞)` are distinct objects, even in their dimensions.

**Proof — angular average and interchange of limits.** Substitute `Ω=η/E` into the exact angular average of §5.2. At fixed `z>0`, `s → s_(η)`, `γ_(c)/E → 1/r_(η)`, `a_(0)/E → (2η+z²)/(2s_(η))`, and `√(a_(0)²-b_(0)²)/E → z/r_(η)`. Separating the terms and taking their limits gives

```text
E⟨ E_(f)𝒯⟩ →
(1)/(2)[(η(2η+z²))/(2s_(η))-(z²)/(2)-2M²-4η
+(4η r_(η))/(z)]=(1)/(2)K_(η)(z).
```

The contribution of the `1/ω²` term tends to 0 in this limit. The constant obtained from the positive-`z` half of the even integrand and the angular average in (LM3) is `e_(ch)²/(4π²√(s))`. This yields the factor in (LM14).

Interchanging the integral and limit is not justified by pointwise substitution alone. The `J/Ω` integrand of `𝒯_(2)` is dominated by a constant multiple of `B(z)/∣z∣`. Inserting `E_(f)𝒯_(1) ≤ ωΩ/(2E)` and `⟨ω⟩=γ_(c)ω*` into the positive bound on `𝒯_(1)` gives domination by a constant multiple of `B(z)` for fixed `η` and sufficiently large `E`. The integration interval is bounded; its endpoint `b_(η)` and the origin have measure zero. Apply dominated convergence using the sum of the two integrable functions. Positivity of the original tensor supplies absolute-value domination.

**Proof — asymptotics at both ends.** For small `η`, `z=η t/M`, `b_(η) M/η → 1`, `B(z)=2d²z²(1+o(1))`, and `K_(η)(η t/M) → M²(4/t-2)`. The dominating function `t²(1+1/t)`, together with

```text
(1)/(8π²)∫_(0)¹ 2t²(4/t-2)dt=(1)/(3π²)
```

gives the first asymptotic formula. For large `η`, the first term of `K` gives `e_(ch)²/(2π²)∫_(0)^(b_(η))B(z)/z dz`. The remaining integral of the constant term is `O(1/r_(η))∫ B`, and `z² ≤ b_(η)² ≤ r_(η)²` also bounds the quadratic term by `O(1/r_(η))∫ B`. Both tend to 0. The final bound follows by inserting `Ω=η/E` into (LM11) and into (LM10) with `Ω ≤ M`, then taking the limit. □

**Closed form for the exponential profile.** Set `b=b_(η)`. Then

```text
I_(1)(b)=∫_(0)^(b) B(z)z⁻¹dz=(b²)/(a²+b²),
I_(0)(b)=∫_(0)^(b) B(z)dz=a arctan (b/a)-(a²b)/(a²+b²),
I_(2)(b)=∫_(0)^(b) B(z)z²dz=2a²b-3a³ arctan (b/a)+(a⁴b)/(a²+b²).
```

Consequently, `L_(ρ)=e_(ch)²[4η r_(η) I_(1)+(-2s_(η)+η²/s_(η))I_(0)-(M²+η)I_(2)/(2s_(η))]/(8π²r_(η)η)`. C17 differentiates the three primitives and checks the leading angular-average terms and endpoint positivity. V19 compares this closed form with the original spectrum at finite `E`, and V20 compares it with separate `z` quadrature.

**Corollary LM-L(b): separation of strong decay from norm decay.** Fix `u>0`. Then

```text
lim_(τ → ∞)ℛ_(τ)(E=uτ)=F_(ρ)(u)
:=2π∫_(0)^(∞) x L_(ρ)(ux)e^(-x²)dx>0,
F_(ρ)(u) → π L_(∞)^(layer) (u → ∞),
liminf_(τ → ∞) sup_(‖φ‖_(2)=1)ℛ_(τ)(φ)
≥ (e_(ch)²I_(ρ))/(4π)>0.

(LM16)
```

**Proof.** At `Ω=x/τ` and `E=uτ`, `EΩ=ux`, and `τ J(x/τ;uτ) → xL_(ρ)(ux)`. Dominated convergence uses `C_(ρ) xe^(-x²)` from (LM11). The same dominating function for `u → ∞` gives `F → π L_(∞)^(layer)`. Choose a normalized energy density `τ⁻¹g(E/τ)`, with `g` supported in a bounded positive interval and integrating to 1. For sufficiently large `τ`, this density lies in `E ≥ M`, and the response of the corresponding `L²` packet tends to `∫ g(u)F_(ρ)(u)du`. Place `g` near the desired `u`, then take `u` large to obtain the final inequality. These packets have finite energy at each `τ`, but no common energy bound. □

Decay for every fixed packet thus differs from decay uniform over all packets. Defining `A_(τ)` as a bounded multiplication operator on `ℛ_(τ)(k)`, `A_(τ) → 0` is strong convergence but not norm convergence. For a class with a fixed energy-moment bound, (LM13) gives a separate common rate. The impossibility of imposing `τ⁻²` on the general normalized class is not a no-go theorem for the adiabatic theorem of full QED.

### 5.11 Exact tail-dependent decay rates for finite-energy packets — LM-P

**Theorem LM-P.** Assume finite (d), `e_(ch) ≠ 0`, `M>0`, PEC, and Gaussian switching. Fix `E_(0) ≥ M` and `0<α<2`, and

```text
f_(α)(E)=α E_(0)^(α) E^(-1-α)𝟙_(E ≥ E_(0)),
|φ_(α)(k)|²=(f_(α)(E(k)))/(2π E(k)),
ℛ_(τ)(φ_(α)) ∼ K_(α)τ^(-α),
K_(α)=πα E_(0)^(α)Γ(1+α/2)
∫_(0)^(∞)η^(-1-α)L_(ρ)(η)dη ∈ (0,∞).

(LM17)
```

An arbitrary phase gives the same inclusive response. If `1<α<2`, the mean energy is `⟨ E⟩=α E_(0)/(α-1)<∞`, with `⟨ E²⟩=∞`. In particular, `α=3/2` gives a normalized packet **with finite mean energy and decay `τ^(-3/2)`**. This extends the v1.3 statement that “finite energy cannot guarantee `τ⁻²`” to an exact rate and positive coefficient.

**Proof.** Normalization and moments follow directly from the radial relation `d²k=2π E,dE`. The substitution `E=τ u` gives

```text
τ^(α)ℛ_(τ)(φ_(α))
=α E_(0)^(α)∫_(E_(0)/τ)^(∞) u^(-1-α)ℛ_(τ)(E=τ u)du
```

Writing `H(E)=AE²+B_(0)` and `B_(0)=18J_(∞)/M³`, the pointwise bound from (LM13) becomes, over the integration interval,

```text
ℛ_(τ)(E=τ u) ≤ π min {C_(ρ),(A+B_(0)/E_(0)²)u²}
```

The function multiplied by `u^(-1-α)` is integrable at both ends precisely for `0<α<2`. By LM-L(b) and dominated convergence, the limit is `α E_(0)^(α)∫ u^(-1-α)F_(ρ)(u)du`. Applying Tonelli to the positive integrand and substituting `η=ux` gives

```text
∫_(0)^(∞) u^(-1-α)F_(ρ)(u)du
=2π∫_(0)^(∞) x^(1+α)e^(-x²)dx
∫_(0)^(∞)η^(-1-α)L_(ρ)(η)dη.
```

The first integral is `(1)/(2)Γ(1+α/2)`. Together with `L_(ρ) ≤ min (C_(ρ),Aη²)` and positivity, this proves finiteness and strict positivity of the coefficient. □

**Endpoints and scope of use.** For `α>2`, the finite `τ⁻²` coefficient of the existing LM-A(b) applies. At `α=2`, (LM13) gives an `O(τ⁻² log τ)` bound, while LM-A(b) gives `τ²ℛ_(τ) → ∞`. No exact equivalent or logarithmic coefficient at the endpoint `α=2` is claimed here. A packet with a physical cutoff eventually returns to the finite-`E²` class at sufficiently long times, so the order of the infinite power-tail and finite-cutoff limits must also be distinguished.

**Falsifiable mathematical prediction.** For the exponential profile and `M=a=E_(0)=e_(ch)=1`, the closed form in (LM14) and the Mellin integral in (LM17) determine `K_(α)` without a freely fitted constant. The numerical table and integral-tail bound appear in Appendix D and V20. This is a computational prediction of the declared model, not an experimental prediction unique to Z-Spin.

### 5.12 High-energy limit at fixed frequency — LM-Q (additional result obtained during integration)

Between the fixed-`Ω/E=λ>0` limit of LM-R and the fixed-`EΩ=η>0` limit of LM-L lies a high-energy limit at fixed `Ω>0`. This limit is calculated to distinguish analytically the numerical witness in the attached v1.4-B. A finite-`d` assumption is not needed in this section.

**Theorem LM-Q.** Under the profile assumptions of §1, fix `Ω>0`. Then

```text
Q_(B)(Ω):= lim_(E → ∞)
J_(B)(Ω;√(E²-M²))
=(e_(ch)²)/(4π²)∫_(0)^(∞)
B(z)(Ω(Ω²+2z²))/((Ω²+z²)^(3/2)) dz,
ρ(y)=ae^(-ay), B=B_(PMC), Ω=a
⇒
(Q_(PMC)(a))/(J_(∞))=(64)/(5π)>4.

(LM20)
```

Thus the **analytic range** for the globally optimal constant `C_(*):= sup_(M,ρ,B,k,Ω)J_(B)/J_(∞)` of the declared model is
```text
(64)/(5π) ≤ C_(*) ≤ 18.
```
This lower bound is obtained in a limit; equality at a finite energy is not claimed. Since `64/(5π)>4`, it follows that points exceeding 4 exist at sufficiently large finite energies. The finite-point numerical value `4.1102159588` provides stronger numerical evidence, but is not an interval certificate replacing this exact lower bound.

**Proof.** Use the analytic angular average in §5.2. Set `D=Ω²+z²`. At fixed `z`,
```text
(s)/(E) → 2Ω,
(a_(0))/(E) → (1)/(2),
(a_(0)²-b_(0)²)/(E) → (D)/(2Ω),
(A_(0))/(E²) → 2, (B_(0))/(E) → 2.
```
Only the `1/ω` and `1/ω²` terms of the angular average leave finite leading contributions to `⟨ E_(f)𝒯⟩/√(s)`. Their sum is
```text
(2Ω)/(√(D))-(Ω³)/(D^(3/2))
=(Ω(Ω²+2z²))/(D^(3/2)).
```
The remaining terms vanish at order `O(E^(-1/2))` or smaller. This order is a statement at fixed `z`, not a uniform error rate over the entire interval.

Extend the integrand by 0 beyond the moving endpoint `z_(max) → ∞`. Positivity of the original tensor and LM-B(ii)–(iii) give the following spectral density on the half-line:
```text
0 ≤ (e_(ch)²)/(4π²√(s))
B(z)⟨ E_(f)𝒯⟩
≤ ((e_(ch)²)/(8π²)
+(e_(ch)²)/(π²))B(z).
```
The first term uses `(M+Ω)/√(s) ≤ 1`, and the second uses `G ≤ 2`. Since `B ∈ L¹`, dominated convergence gives the first formula in (LM20).

For PMC with the exponential profile, `B(z)=2a⁴/(a²+z²)²` and `J_(∞)=e_(ch)²a/(32π)`. Set `z=at` and `Ω=a`. Then
```text
(Q_(PMC)(a))/(J_(∞))
=(16)/(π)∫_(0)^(∞)(1+2t²)/((1+t²)^(7/2))dt
=(16)/(π)∫_(0)¹(1+u²)(1-u²)du
=(64)/(5π).
```
The intermediate substitution is `t= tan θ, u= sin θ`. The strict inequality follows from `π<22/7<16/5`. LM-B supplies the upper bound. □

**Scope of the three limits.**

| Quantity held fixed | Spectral limit | Application |
|---|---|---|
| `Ω/E=λ>0` | `J_(B) → Φ(λ)J_(∞)` (LM-R) | recoil plateau; `1<Φ<4` |
| `EΩ=η>0`, PEC | `J_(PEC)/Ω → L_(ρ)(η)` (LM-L) | `E ∼ τ` packet-tail decay |
| `Ω>0` | `J_(B) → Q_(B)(Ω)` (LM-Q) | High energy at fixed frequency; response exceeding 4 |

The limit in one row cannot be transferred to another as a uniform approximation. C21 checks the leading angular-average algebra and exact integration coefficient; V22 compares finite-energy spectra across all three mode families with a separate `Q_(B)` integral. LM-Q is classified as additional limit analysis from a known vertex (EXTENDED), and is not used to support a new radiation principle or research grade 4.


## 6. Physical interpretation and mission debt

The observables are leading-order inclusive responses obtained by multiplying the declared Hamiltonian by external switching. `ℛ` is an order-`e_(ch)²` coefficient; a full probability distribution bounded between 0 and 1 to all orders has not been constructed. The numerical choice `e_(ch)=1` is a normalization for checking constants. LM-D controls PEC sine-mode cancellation up to high energies, while LM-L/P establishes how the order of the high-energy-tail and long-time limits changes the decay rate.

Three conclusions are directly usable. If the PEC profile has finite `d`, every fixed normalized packet decays. To use a finite coefficient of `τ⁻²`, one must check the `E²`-moment. Even an upper bound on the energy tail alone allows (LM13) to bound the response at finite time. This is a reusable methodological result for choosing a rest approximation, packet cutoff, and switching time.

### 6.1 BEFORE → AFTER and open physical connections

Mission v1.6 §§1.4 and 5.6 and rules v2.3 were applied. The status of the catalog and debt ledger directly inspected in version A is preserved as lineage input and checked against the scope of the Mission, Book, and history attached here. This integration is not interpreted as ledger registration or closure of all debt.

| Object or mission question | Through v1.3 | Additions preserved or integrated in v1.5 | Remaining status |
|---|---|---|---|
| Declared occupied-current subproblem of D-M69-MOVING; supports FQ2 / RQ3 and RQ5 | Recoil kernel, temporal regularity, condition for the PEC `E²` rate | Removal of the PEC log-moment restriction; finite-time tail bound; `EΩ` boundary layer; power-tail decay rate; bound 18; photon necessary condition; fixed-frequency limit | **Analytic sub-obligations for this channel extended or closed** |
| D-M69-MOVING as a whole | A common finite-time error for packet motion, recoil, bulk, projection, and Coulomb effects is required | Bulk, projection, and Coulomb errors are not newly derived | **OPEN** |
| D-M69-INSTRUMENT; K17/K18 | Physical operation space, readout, and record are required | Exact reason and test for the failure to identify KRS with an external pulse | **OPEN**; not counted as construction of an actual instrument |
| M67/S14 carrier → interacting current | Conditional input `a=2m∣ cos bar(θ) ∣ , M=∣ m sin bar(θ) ∣` | Restricted calculation within the same massive band | Selection of profile, current, and occupation from the action remains **OPEN** |
| 11D ontology → metric/connection/action → observation | Formal assets and bridge research | No new evidence for 11D existence, selection, or dynamics | **OPEN** |
| Clock, cosmology, and GR/SM reduction; FQ1 and others | Switching is external input | No corresponding derivation | **OPEN** |

**MISSION ROLE: SUPPORT/METHOD.** Applicability to every massive 2D Dirac band benefits external reuse, but does not establish an origin in an action unique to Z-Spin. The chain reached is conditional carrier → declared current and environment → leading-order spectrum → packet/switching criteria. The original detector, state-update, and record objectives have not been replaced by a smaller goal and declared complete.

### 6.2 Integrated falsification conditions

This table is a comparison contract within the declared model. It is not identified with experimental predictions unique to Z-Spin or with falsification conditions for the entire program.

| ID | Computational prediction | Required conditions for a falsifying comparison |
|---|---|---|
| F1 | At fixed `k` and the same `‖ρ‖_(2)`, all three mode families have the same UV plateau `J_(∞)` | Same charge, inclusive channel, and normalization; the limit `Ω ≫ E(k)` |
| F2 | At rest, PEC/free `∼ (10/21)d²Ω²` and PMC/free `→ 2` | The `k=0` prescription; apply F4 to normalized packets |
| F3 | Sharp-switching logarithmic coefficients for total/photon energy are `2J_(∞),J_(∞)`, respectively | Fixed `k`, same cutoff change; do not confuse a finite band with the infinite-UV model |
| F4 | Moving-state free/PMC has order `Ω`, PEC order `Ω³`, with coefficients in LM6 | Fixed `v<1`, same profile, finite `d` for PEC; validity of the soft window |
| F5 | A finite coefficient of PEC `τ⁻²` exists only when the `E²`-moment is finite | Gaussian switching, same fixed packet; `τ²R_(τ) → ∞` when `E²` is infinite |
| F6 | In `Ω/E=λ>0`, `J/J_(∞) → Φ(λ) ∈ (1,4)` | Fixed-`λ` limit; a finite value exceeding 4 does not refute this statement |
| F7 | On every shell, `Ω ≤ 2ω`, hence `E_(γ) ≥ E_(total)/2` | Same channel, mismatch, and detection band; a single exact opposing shell point suffices |
| F8 | Under the Dini condition, every fixed normalized PEC packet decays | External Gaussian pulse; apply F9 if the packet itself depends on `τ` |
| F9 | A positive boundary layer remains for the `E ∼ τ` packet class | The same scaling as LM-L; do not read it as a residual response of a fixed packet |
| F10 | If `f_(α) ∝ E^(-1-α)` and `0<α<2`, then `R_(τ) ∼ K_(α)τ^(-α)` | Order of the infinite-tail and cutoff-removal limits, finite `d`, same normalization; excludes `α=2` |
| F11 | At fixed `Ω=a`, the PMC exponential profile gives `J/J_(∞) → 64/(5π)` | `E → ∞`, fixed mass, profile, and frequency; distinguish the LM-R/LM-L limits |

Also apply the distinction in LM-A(a): the free/PMC Gaussian packet limit is `π∫∣φ∣²c_(B)` with a finite log-moment and infinity with an infinite log-moment. Finiteness of numerical values alone does not determine the infinite-time limit.


## 7. KRS correspondence, external novelty, and research grade

### 7.1 Closest source and exact correspondence

The PDF of [Kazinski–Ryakin–Shevchenko (KRS), arXiv:2406.19429v1](https://arxiv.org/pdf/2406.19429) was checked at §4 (34)–(46), §5.1 (49), (67)–(69), and §5.2 (130)–(134). This resolves the v1.3 status of “read only through (104).” Equations (49) and (67)–(69) are in **§5.1**, not §4.

| Target | KRS location and object | M70 correspondence and difference |
|---|---|---|
| Observation probability | (34)–(39), (130): intermediate measurement and photon record | Inclusive response to an external pulse; a different event sequence |
| Initial state and sum | (130), (134): one-particle density and final-state sum | `ϱ=∣ φ⟩⟨φ∣`, summed final band states |
| Radiation amplitude | (49): Dirac vertex, mode, and mismatch | §1.2 `V⁺`, `u_(+)†σ_(a) u_(+)`, planar recoil |
| Normal direction | Spatial overlap of the 3D mode | Declared overlaps `ρ` and `F,S,C`; boundary modes are additional input |
| Polarization and measure | Photon projector `D_(γ bar(γ))` | `D_(γ)=I`, transverse sum; half-space factor in §1.2 |
| Measurement operator | (130): `V_(>)D_(e)+D_(e)V_(<)` | M70 has no `D_(e)`, only `T_(χ)` |
| Finite measurement time | (40)–(46): dressed projector and `V_(>)+V_(<)=V_(full)` | A pulse and projector dressing are different operations |
| Temporal factor | (67)–(69): `λ=1 → 0, h=-λ', ∫ h=1` | `χ ∈ L¹` pulse; `λ ∉ L¹` |

The source objects above are grounded in the [corresponding KRS equations](https://arxiv.org/pdf/2406.19429). What follows is **this paper's derivation** for comparing those objects with M70.

**Common-vertex level.** Restricting the particle matrix element of the general creation amplitude to the declared band current and integrating the normal-mode overlap gives `F(z)`, or `S(z),C(z)` for PEC/PMC. Converting box normalization to the delta normalization of §1.2 and summing final band states and polarizations gives the tensor in (LC3) and `B(z)`. Appending the external time integral `-i hat(χ) (Ω)` gives (LM2)/(LM3). This is a **specialization** of the given vertex. It does not prove a new inclusive principle, unitary equivalence between a free 4D spinor and a boundary band, or projection from an action.

**Full measurement-probability level.** Massive intraband kinematics gives, for finite `k` and a nonzero photon,
```text
E(k-p)+√(|p|²+z²)-E(k)>0
```
because the gradient magnitude of `E` is less than 1. This time-independent channel has no energy-conserving one-photon radiation, and `V_(full)=0`. In the same channel and mode in KRS form,
```text
𝒜_(D)=V_(>)D_(e)+D_(e)V_(<)=V_(>)D_(e)-D_(e)V_(>)=[V_(>),D_(e)].
```
For a diagonal projector `D_(e)(k)=d(k) ∈ {0,1}`, `(𝒜_(D))_(fi)=(d_(i)-d_(f))(V_(>))_(fi)`. Thus the result equals 0 when `D_(e)=I`. By contrast, `T_(χ)=-iW hat(χ) (Ω)` is generally different from 0. W08 checks both the finite-matrix cancellation and a positive sample of the actual PEC spectrum. This difference alone does not prove novelty, but it rules out identifying M70 with the full KRS measurement probability. Unitary dressing also preserves the identity.

**Temporal-factor level.** For `Ω>0`, the Abel prescription and integration by parts give
```text
hat(λ) (Ω)=(hat(h) (Ω))/(iΩ), h=-λ'
```
Using `h` as a pulse changes the Fourier weight by `Ω²`. Matching dimensions additionally requires declaring a fixed time scale `T_(0)` to define the external pulse as `χ=T_(0)h`; the ratio is `T_(0)²Ω²` (C19 uses `T_(0)=1` units). M70's fixed-amplitude Gaussian family and the normalized measurement-time derivative family also scale differently in amplitude. M70's `L²/H^(1/2)` criterion therefore cannot be transferred to a regularity theorem for the KRS detector.

**Correction to version B's correspondence table.** Version B's explanations that “M70 differs from KRS by including recoil” and that “measurement and an external gate have the same mathematical role” are not adopted. KRS (130) and (67) already include the amplitudes before and after measurement and an energy denominator, respectively. Nor does `B ≡ 1` alone reduce a massive 2D band to a free 3+1D Dirac model. Reusability of mode/current substitutions is distinguished from identity of the full probabilities.

The idea in version B's X02 is preserved as a diagnostic, not evidence. At fixed `Ω`, the right-hand side of the soft form of (LM4) diverges because of `log E`, while the uniform bound 18 remains valid. This means only that “this soft estimate alone cannot prove the uniform criterion.” It is neither evidence that no other proof is possible in the KRS source nor a novelty certificate. A different subject of study alone does not justify NEW.

### 7.2 Proofs needed beyond the general formula

| Result | Imported structure | Additional proof or discriminating test | External status |
|---|---|---|---|
| LM-K/S/E, LC | Inclusive sum, spinor, recoil, soft factor, Fourier smearing | Specification of the declared band and modes | **SPECIALIZED**; this part alone does not warrant grade 3 |
| LM-B/T | Vertex and phase space | Bound for all `k,Ω` and packet iff; boundedness at fixed `k` does not permit interchange with packet integration | **EXTENDED** |
| LM-A/R | Soft coefficient and exact recoil | `E²` iff and `Ω/E` plateau; misuse of the fixed-`k` limit fails W05/W06 | **EXTENDED** |
| **LM-D** | CM decomposition and sine cancellation | Uniform Dini bound, decay of every fixed packet, finite-time tail bound; the existing `log E` dominating function cannot handle W07 | **NEW** |
| **LM-L** | Exact angular average | `EΩ` boundary layer, asymptotics at both ends, strong/norm separation; the fixed-`k` soft approximation is nonuniform at `E ∼ τ` | **NEW** |
| **LM-P** | Gaussian integral and energy density | Exact `τ^(-α)` for `0<α<2` with a positive Mellin coefficient; finite-energy counterexample at `α=3/2` | **NEW** |
| LM-E lower bound / LM-Q | Lipschitz dispersion / exact angular average | Photon necessary condition and finite-mean-energy iff / fixed-frequency limit and exact lower bound on the supremum | **SPECIALIZED / EXTENDED** |

The general recoil formulas in KRS are not restricted to small recoil. The argument “it includes recoil, therefore it is new” is not used. The ability of a general formula to contain this calculation is distinct from an existing theorem with the same assumptions, quantifiers, and conclusion. The central contribution is the additional universal and scaling-limit analysis in LM-D/L/P.

### 7.3 Adjacent research and scope of the subsumption check

| Source and location checked | Overlapping asset | Boundary with the central novelty claim |
|---|---|---|
| [Kazinski–Lazarenko, PRA 103, 012216 (2021), §§2–3, (5), (8), (21)–(27)](https://arxiv.org/html/2010.05236v2) | Recoil and inclusive radiation of a 3D packet crossing a mirror | Its subject does not supply the Dini, `EΩ`, or packet-tail theorems for a bound 2D band |
| [Kazinski–Solovyev, EPJC 82, 790 (2022), §2, (40)](https://link.springer.com/article/10.1140/epjc/s10052-022-10739-6) | General QED packet probabilities and the coherent/incoherent distinction | This structure is imported; the probability formula itself is not counted as a new theorem |
| [Hodgkinson–Louko, §2 (2.3)–(2.4), §§6–7](https://arxiv.org/html/1109.4377v3) | Scalar worldline detector and switching regularity | Different objects from the recoil-band, PEC-profile, and energy-tail analysis in LM-L/P |
| [Teber–Kotikov, §II](https://arxiv.org/html/1801.10385v2) | Reduced QED with 2+1D fermions and 3+1D photons | Mixed dimensionality itself is not new; limit analysis for the finite-width massive channel is additional |

Absence from search results was not used as proof of originality. The closest sources above were checked for reduction to their general formulas and for the proof obligations that remain. The 2026 [soft-QED open-system study (arXiv:2606.27498)](https://arxiv.org/abs/2606.27498) found in the search was accessible only as an abstract; its full text was not obtained, so it was not used to decide subsumption or nonsubsumption. The novelty judgment is a **research judgment based on comparing the stated theorems with the closest literature actually read**, not proof of priority over every unpublished result worldwide.

LA's OPEN-NOVELTY is retained as an appendix asset, and LB remains a SPECIALIZED supporting result. Neither supplies the central novelty for this paper's qualification.

### 7.4 Freezing the two v1.4 judgments and reviewing the content of v1.5

**Version A** is the immediately preceding Codex manuscript, and **version B** is the Claude manuscript attached in this turn. The same version number does not imply the same document or verification rows. Exact input hashes and equation/row correspondence appear in Appendix C and the comparison report.

Version A previously displayed PAPER QUALIFICATION PASS / RESEARCH GRADE 3, but this was an author-side content review. Version B was NOTE / HOLD / UNASSESSED / CANDIDATE 3. Version B's new bound 18 and photon lower bound are valid, but its intermediate soft inequality has a counterexample and its KRS correspondence was incomplete. Version B is therefore not promoted unchanged, and version A's PASS is not automatically inherited by the new integrated manuscript.

| Required axis | v1.5 content judgment | Grounds and limits |
|---|---|---|
| Correctness | **PASS — declared model, author-side integration review** | Bound 18 and repaired soft proof in LM-B; Lipschitz lower bound in LM-E; dominated-convergence and Mellin arguments for version A's LM-D/L/P; integrable dominating function in LM-Q. Finite numerical success is not used as universal certification |
| Novelty | **PASS — content judgment centered on LM-D/L/P** | Source correspondence and additional proof obligations in §§7.1–7.3. Inclusive sums, recoil, soft factors, and the elementary Lipschitz lower bound are not counted as new principles. LM-Q is additional limit analysis (EXTENDED) |
| Significance | **PASS — SUPPORT/METHOD** | Unconditional decay of each fixed packet, failure of a common decay rate, exact slow decay at finite mean energy, finite-time tail bound. Three high-energy limits are distinguished to exclude incorrect plateau approximations |
| Verification basis | **PASS — within the stated scope** | Analytic proofs, symbolic identities, multiple numerical routes, exact counterexamples, and actual fault injection. The code is not claimed to certify theorems, novelty, or grades themselves |
| **PAPER QUALIFICATION** | **PASS — content judgment under project criteria** | Result of reviewing all four axes against the new evidence. This does not mean approval for publication/submission or independent expert review |

**RESEARCH GRADE: 3. CANDIDATE GRADE: NONE. TARGET GRADE: 4 (not attained). OUTPUT FORM: RESEARCH PAPER / SUPPORT-METHOD.**

Research grade 3 rests on the universal control and decay-rate classification of the central LM-D/L/P results. Improved constants, editing, and increased row counts are not independent grounds for promotion. Externally usable conclusions concern which decay rates a given energy tail permits and which bounds can guide packet-cutoff and switching-time choices. External significance sufficient for grade 4—substantially changing an important limitation of the field—has not been established. The Z-Spin action, instrument, and record connections also remain OPEN.

**Independence limits.** The current review of version B's new LM-B0/LM-E is a cross-family Claude → Codex review, but it shares some lineage with earlier Codex-derived algebra. Version A's LM-D/L/P and the present LM-Q are Codex author-side work and are not counted as independent re-audits. Version A received a second semantic review following the earlier author-side review. Version B's record of exhausting 2 same-lineage rounds is not reset. Multiple verifier processes are not separate scientific reviewers. **qualified-human anchor: NONE.** This document must therefore not be cited as “a grade-3 paper established by independent review.”

Reversal conditions are a counterexample to the dominating functions or limit interchanges in LM-D/L/P/Q, a prior theorem with the same assumptions, quantifiers, and conclusion, failure of a core rerun, or an upstream change in the actual action connection. The next independent review should target **LM14, LM17, LM20, and the KRS correspondence**, by another family or an expert, rather than create another self-audit round. This follow-up does not block completion or delivery of the present integration, and unperformed reviews are not marked as performed.


### 7.5 Deep-exploration and breakthrough record

The criteria maintained before searching were “a central theorem beyond routine specialization, exact source correspondence, and an actual change in computational judgment.”

| Route | Discriminating test | Result and disposition |
|---|---|---|
| R1: Direct identification with the full KRS probability | `D_(e)=I`, amplitudes before and after measurement, dimensions of `λ'` | Direct identification fails. Correspondence debt resolved; not counted as a new radiation principle |
| R2: Removal of the log-moment | `B/∣ z∣`, `G ≤ Ω/∣ z∣` | Uniform soft bound succeeds. **ESTABLISHED, LM-D** |
| R3: Tail-dependent rates | `EΩ=η`, exact angular limit and tail integral | Boundary layer, strong/norm separation, and `τ^(-α)`. **ESTABLISHED, LM-L/P** |
| Endpoint `α=2` | Uniform remainder for the exact logarithmic coefficient | Bound and divergence of `τ²R` established; exact equivalent remains **OPEN** |

The local breakthrough is the proof of decay for all packets, previously obstructed by moment assumptions, together with its nonuniformity. This is not equated with a physical breakthrough for the entire program or grade-4 innovation. Research diligence, achievement, and grade were assessed separately.

## 8. Scope of the results

Controlling PEC normal-mode cancellation by a Dini integral makes the Gaussian response of every fixed packet decay without packet-moment assumptions. A positive boundary layer remains in the `E ∼ τ` packet class, preventing common decay. For energy density `E^(-1-α)` with `0<α<2`, the exact rate is `τ^(-α)`. This classification provides computable constants and a finite-time tail bound.

Paper qualification and research grade 3 are confined to this methodological contribution. They do not include derivation of an instrument, record, or observable from the Z-Spin action, or attainment of grade 4. A subsequent reviewer can prioritize attacks on the dominating functions and order of limits in LM11–LM20 and the source correspondence in §7.

## Appendix A. Positive subgap spectrum of a spherical chiral bag — LA

This appendix concerns a massive 3D Dirac ball, separate from LC. Here `m>0` is a 3D mass, distinguished in notation and role from the band mass `M` in LC. Spinors regular at the origin are used. The operator on the ball `B_(R)` is `H_(D)=-ibold(α)·∇+β m`, and the boundary domain consists of `H¹(B_(R),ℂ⁴)` spinors satisfying the following condition.

```text
iγ· n_(out) e^(-iθγ⁵)ψ=-ψ,
ψ=column(U; V), V=(i)/(cos θ)(σ· n_(out)+ sin θ)U,
cos θ<0, c=| cos θ| ∈ (0,1].

(LA1)
```

The representation is `γ⁰= diag (I,-I)`, `γ^(i)=([[0, σ_(i)]; [-σ_(i), 0]])`, and `γ⁵=([[0, I]; [I, 0]])`, making the two forms in (LA1) agree. Since `2 Re (U†σ· n V)=0`, the normal current is 0. The theorem below concerns the **regular separated positive subgap sector** of this domain. It does not assert a new self-adjointness theorem for the full boundary domain or a complete classification of other energy sectors.

### A.1 Derivation of the radial boundary determinant

At `j=l+1/2` and `l ∈ ℕ_(0)`, choose spin spherical harmonics so that `σ· n Ω_(l)=-Ω_(l+1)` and `σ· n Ω_(l+1)=-Ω_(l)`. Include both parity channels with the same `j,m_(j)`. For `p²=E²-m²`, `η_(p)=p/(E+m)`, and `E ≠ -m`, the regular radial solution is

```text
U=A j_(l)(pr)Ω_(l)+B j_(l+1)(pr)Ω_(l+1),
V=iη_(p){B j_(l)(pr)Ω_(l)-A j_(l+1)(pr)Ω_(l+1)}.
```

This follows from `V=(σ·(-i∇))U/(E+m)` and the spherical-Bessel recurrence. Setting `f=j_(l)(pR)`, `g=j_(l+1)(pR)`, `b= cos θ`, and `s_(θ)= sin θ`, the two harmonic coefficients at the boundary are

```text
Kcolumn(A; B)=0,
K=[[-s_(θ) f, bη_(p) f+g]; [f-bη_(p) g, -s_(θ) g]],
det K=-b{b(1-η_(p)²)fg+η_(p)(f²-g²)}.
```

The eigenvalue condition for this domain with `b ≠ 0` is therefore

```text
cos θ(1-η_(p)²)j_(l)(pR)j_(l+1)(pR)
+η_(p){j_(l)(pR)²-j_(l+1)(pR)²}=0,
0<E<m, q=√(m²-E²):
2mc i_(l)(qR)i_(l+1)(qR)
=q{i_(l)(qR)²+i_(l+1)(qR)²}.

(LA2)
```

The second expression follows by substituting `p=iq`, `j_(l)(ix)=i^(l) i_(l)(x)`, and `η_(p)=iq/(E+m)` into the first and using `1+q²/(E+m)²=2m/(E+m)`. `i_(l)` is the modified spherical Bessel function. As an algebraic check of the boundary equation, at `m=0,E>0`, `η_(p)=1`, leaving `j_(l)²-j_(l+1)²=0` and eliminating `θ`. This does not extend the subgap theorem to `m=0`.

### A.2 Existence, uniqueness, and energy ordering

```text
ν=l+(1)/(2), x=qR, s=mcR,
r_(ν)(x)=(I_(ν+1)(x))/(I_(ν)(x)),
h_(ν)(x)=(x)/(2)(r_(ν)+(1)/(r_(ν)))
=ν+1+(x)/(2)(r_(ν)+r_(ν+1)), h_(ν)(x)=s.

(LA3)
```

The final recurrence representation is essential for monotonicity of `h`. One must not infer that `r+1/r` also increases merely from `r'>0`.

**Theorem LA.** For each `l`, the positive subgap branch

```text
R>R_(l)=(l+3/2)/(mc)
⇔ exists uniquely ;
n= max {0,⌈ mcR-3/2⌉}, N_(+, edge)=n(n+1).

(LA4)
```

Writing its energy as `E_(l)(R,c)`, we have `∂_(R)E_(l)<0`, and `E_(l)<E_(l+1)` among coexisting branches.

**Proof.** For `ν ≥ 1/2`,

```text
Z_(ν)(x)=∫_(-1)¹e^(xt)(1-t²)^(ν-1/2)dt
```

is proportional to `x^(-ν)I_(ν)(x)` in the modified-Bessel integral representation. Hence `∂_(x) log Z_(ν)=r_(ν)` and `r'_(ν)= Var_(x)(t)>0`. Under the positively tilted symmetric distribution with `x>0`, `0<r_(ν)<1`. The Bessel recurrence `I_(ν)-I_(ν+2)=2(ν+1)I_(ν+1)/x` connects the two representations in (LA3). Differentiating the second gives

```text
h'_(ν)=(1)/(2)(r_(ν)+r_(ν+1))+(x)/(2)(r'_(ν)+r'_(ν+1))>0.
```

At the origin, `h_(ν) → ν+1`, and at infinity, `r_(ν) → 1`, so `h_(ν) → ∞`. Thus a unique `x>0` exists exactly when `s>ν+1`. Moreover, `h_(ν)>x` implies `q=x/R<mc ≤ m`, so the constructed energy indeed satisfies `0<E<m`. The solution `x=0` at `R=R_(l)` is the threshold `E=m`, excluded from the open subgap.

Increasing `x` alone does not suffice for radial monotonicity of the energy. From (LA3),

```text
q=mc (2r_(ν)(x))/(1+r_(ν)(x)²)
```

follows. For `0<r_(ν)<1`, the right-hand side increases in `r_(ν)`, and `x` also increases with `R`, so `q` increases and `E=√(m²-q²)` decreases.

For order comparison, use `I_(ν+1)²>I_(ν) I_(ν+2)`. The domain of this imported Turán inequality includes the present `x>0,ν ≥ 1/2`. [Baricz–Ponnusamy, §1, equation (2)](https://arxiv.org/html/1010.3346v1). Thus `r_(ν)>r_(ν+1)`; because `r+1/r` decreases in `(0,1)`, `h_(ν)<h_(ν+1)`. At the two roots with the same `s`, `x_(l)>x_(l+1)`, hence `E_(l)<E_(l+1)`.

The strict inequality at each threshold gives the branch count `n`. In the subgap, `η=q/(E+m) ∈ (0,1)`, and one entry of the boundary matrix is `i_(l)-cη i_(l+1)>0` up to a phase. Even when its determinant is 0, the matrix is not identically 0, so its rank is 1 and only one radial mixture remains for each `j,m_(j)`. No additional multiplicity from the two parities is included. Summing the magnetic degeneracy `2j+1=2(l+1)` gives `Σ_(l=0)^(n-1)2(l+1)=n(n+1)`. Regular radial functions are normalizable on the finite ball. □

### A.3 Contact slope, large radius, and unresolved proxy

The small-`x` Bessel series and the recurrence in (LA3) give

```text
h_(ν)(x)=l+(3)/(2)+(2l+4)/((2l+3)(2l+5))x²+O(x⁴),
-E_(l)'(R_(l)⁺)=(m²c³(2l+5))/((2l+3)(l+2)),
lim_(R → ∞)E_(l)(R,c)=m√(1-c²),
c=1: E_(l)(R,1) ∼ (l+1)/(R).

(LA5)
```

Denoting the coefficient in the first expression by `A_(l)`, `x²=(mc/A_(l))(R-R_(l))+O((R-R_(l))²)` and `E=m-x²/(2mR²)+O(x⁴)` give the slope. At `l=1`, `7m²c³/15` is recovered. `r_(ν) → 1` gives the large-radius limit. For `c=1`, combining `r_(ν)=1-(l+1)/x+O(x⁻²)`, `E/m=(1-r_(ν)²)/(1+r_(ν)²)`, and `x ∼ mR` gives the final expression.

The global proxy `E_(1) ≤ 2E_(0)` and maximality remain **OPEN**. At `c=1`, the `s=3,5,10` samples of `(E_(1)-E_(0))/(2E_(0))` are approximately 0.470896, 0.495503, and 0.499854. The earlier value 0.454832 at `s=2.5` used the **threshold limit** of `E_(1)=m`; it does not mean that a positive subgap `l=1` branch exists there. Samples and a large-radius limit do not prove a global inequality. The actual next detection gap, including bulk channels, occupation, and selection rules, differs from this proxy and remains unresolved.

## Appendix B. Endpoint leakage and reachability in the same basis — LB

### B.1 Objects and all-time envelope

The basis in this appendix is fixed **throughout as `(e,g,ℓ)`**. With `v,w>0` and `δ ∈ ℝ`, the initial state and leakage are

```text
H_(δ)=[[0, v, 0]; [v, 0, w]; [0, w, δ]],
ψ(0)=|e⟩=(1,0,0)ᵀ,
P_(ℓ)(t)=|⟨ℓ|e^(-itH_(δ))|e⟩|².

(LB1)
```

The star matrix `([[0, v, w]; [v, 0, 0]; [w, 0, δ]])` printed in v1.0 is permutation-equivalent to (LB1) when its ordering is `(g,e,ℓ)`. For the matrix `S` that swaps the first two axes, `H_(old)=SH_(δ) Sᵀ`, and the initial vector must also become `S(1,0,0)ᵀ=(0,1,0)ᵀ`. The claim that transformed only the matrix while leaving the initial state unchanged is withdrawn.

**Theorem LB.** For eigenvalues `λ_(1)<λ_(2)<λ_(3)`, gap `d_(1)=λ_(2)-λ_(1)`, and `d_(2)=λ_(3)-λ_(2)`,

```text
p(z)=z³-δ z²-(v²+w²)z+δ v²,
[(zI-H_(δ))⁻¹]_(ℓ e)=(vw)/(p(z)),
A_(ℓ e)(t)=Σ_(j=1)³a_(j)e^(-iλ_(j)t), a_(j)=(vw)/(p'(λ_(j))),
P_(ℓ)(t) ≤ ℬ=(4v²w²)/(d_(1)²d_(2)²) ≤ 1 (t ∈ ℝ).

(LB2)
```

**Proof.** This is a real symmetric tridiagonal matrix with every off-diagonal link nonzero, so its spectrum is simple. Directly, if the first component of an eigenvector were 0, the first row would force the second to be 0 and the second row would force the third to be 0, giving the zero vector. Each eigenspace is uniquely determined by its first component, and a symmetric matrix is diagonalizable, so repeated eigenvalues cannot occur.

Cofactor expansion gives the resolvent formula. The residues are `+,-,+`, respectively; since `vw/p(z)=O(z⁻³)` at `z → ∞`, `a_(1)+a_(2)+a_(3)=0`. Thus `a_(1)+a_(3)=-a_(2)=vw/(d_(1)d_(2))`. The triangle inequality gives `∣A∣ ≤ Σ∣a_(j)∣=2vw/(d_(1)d_(2))`. Writing the orthogonal eigenvector matrix as `U`, we have `a_(j)=U_(ℓ j)U_(ej)`, and Cauchy–Schwarz gives `Σ_(j)∣a_(j)∣ ≤ ‖U_(ℓ·)‖_(2)‖U_(e·)‖_(2)=1`. Squaring yields (LB2). □

If `v=0` or `w=0`, the endpoint decouples and `P_(ℓ) ≡ 0`. Repeated eigenvalues can occur in this degenerate case, so the formula with gap denominators must not be substituted unconditionally.

### B.2 Distinguishing the supremum from exact finite-time attainment

```text
d_(1)/d_(2) | sup_(t) P_(ℓ)(t)=ℬ | ∃ t finite :P_(ℓ)(t)=ℬ
irrational | yes | no
p/q reduced, p,q odd | yes | yes
p/q reduced, one even | no | no

(LB3)
```

**Proof.** Factoring out `e^(-iλ_(2)t)`, equality in the maximal triangle inequality requires the positive `a_(1),a_(3)` terms to have the same phase as the negative `a_(2)` term. This means that `d_(1)t=(2r+1)π` and `d_(2)t=(2s+1)π` must hold simultaneously. Their ratio must be a reduced odd/odd rational number; conversely, that condition permits construction of a common `t`.

If the gap ratio is irrational, `(d_(1)t,d_(2)t) mod 2π` is dense in the 2-torus. The target phases can therefore be approached arbitrarily closely, so the supremum equals the envelope. Exact attainment at finite `t` is impossible, however, by the rationality condition above. For a rational gap ratio, the probability is periodic. Unless the ratio is odd/odd, this continuous function never reaches the target equality on a compact period, so its maximum is strictly smaller. □

This is the distinction between exact transfer and pretty-good approximation. General spectral phase conditions are standard background; the calculation for this finite block is not claimed as a separate new principle of quantum transfer. [Eisenberg–Kempton–Lippner, §2.2](https://arxiv.org/html/1804.01645v1).

### B.3 Resonance layer and far detuning

For fixed `v>0`, bounded `ζ`, and `w ↓ 0`, set `δ=v+ζ w`. Then

```text
λ_(1)=-v+O(w²/v),
λ_(2,3)=v+(w)/(2){ζ ∓ √(ζ²+2)}+O(w²/v),
ℬ(v,w,v+ζ w) → (1)/(ζ²+2),
ℬ(v,w,δ) ∼ (w²)/(δ²) (|δ| → ∞, v,w fixed ).

(LB4)
```

**Proof.** At `w=0` and `δ=v`, `(∣e⟩+∣g⟩)/√(2)` and `∣ℓ⟩` are the two states with eigenvalue `v`. The first-order perturbation in this subspace is `w([[0, 1/√(2)]; [1/√(2), ζ]])`, and the gap to the remaining state is `2v`. The finite-dimensional Schur-complement expansion has a uniform `O(w²/v)` remainder for bounded `ζ`. Hence `d_(1) ∼ 2v` and `d_(2) ∼ w√(ζ²+2)`; substituting into (LB2) gives the limit. The negative resonance point is treated identically with `H_(-δ)=-DH_(δ) D` and `D= diag (1,-1,1)`. For large `∣δ∣`, the two finite eigenvalues are `± v+o(1)` and the remaining one is `δ+o(∣δ∣)`, so the gap product is `2v∣δ∣(1+o(1))`. □

Protection is therefore not determined merely by calling the tension large. What matters is whether the relevant matrix element and energy mismatch lie outside the resonance layer. The formulas above are asymptotics for the **envelope**, not a claim that the actual maximum is identical at every rational gap ratio.

### B.4 Rigorous rational witness and limits of the physical interpretation

For `v=√(3),w=√(2),δ=2`, the eigenvalues are `(-2,1,3)` and the gap ratio is `3/2`. Writing `x= cos t`,

```text
P_(ℓ)(t)=(2)/(75)(x-1)²(48x³+96x²+64x+17),
max_(t) P_(ℓ)(t)=(5+√(5))/(12)<(2)/(3)=ℬ.

(LB5)
```

For the proof, compare the values using this polynomial's derivative `(4)/(5)(x-1)(2x+1)(4x²+2x-1)`, interval endpoints `± 1`, and interior stationary points `-1/2,(-1 ± √(5))/4`. C07 checks this exact algebraic comparison; W03 checks the actual matrix exponential at the maximum point.

The counterexample to the incorrect first-state proposition of v1.0 is also preserved. With `v=1,w=2,δ=0` and an initial state on the first axis in the old star matrix, `P_(ℓ)(π/(2√(5)))=4/5>16/25`. The correct endpoint initial state in (LB1) gives `16/25` at `t=π/√(5)`. W02 computes the two separately.

The gauge interpretation is restricted to the **declared effective block**. Assuming that all three states lie in the same Gauss kernel, set the electric energies to `E_(g)^(el)=0,E_(e)^(el)=τ,E_(ℓ)^(el)=2τ` and `τ=g²a_(lat)/2`. Subtracting the energy of `e` gives `δ=τ+ε_(ℓ)-ε_(e)`. **Making both `e,g` diagonal entries in (LB1) 0 requires separate resonance tuning.** Before correction, the detuning of `g` is `Δ_(g)=ε_(g)-ε_(e)-τ`. An effective control canceling this must be assumed to obtain (LB1); uniform matter sites alone do not derive the resonance. After that tuning, uniform matter gives `δ=τ`. Without tuning, the different problem `diag (0,Δ_(g),δ)` must be solved.

For states in the same Gauss kernel, the `Σ G²` penalty equals 0 for all of them and does not automatically suppress this leakage. Identification of an invariant subspace, actual control, matrix elements, and detuning in the full Kogut–Susskind/Schwinger Hamiltonian remains **OPEN**. This block is not called an already implemented gauge simulator.


## Appendix C. Audit responses and correction lineage

Rounds 1–4 are historical records preserving the judgments and locations at the time; the current v1.5 judgment is in §7.4 and Round 6.

The target versions, finding prefixes, and counts for five rounds are registered in `audit_rounds` in the execution metadata. Verifier G04 checks each round's heading and table-row prefixes and counts against that registration (VERIFY §12.1 round parser).

### Round 1 — v1.0 audit (8 findings, A1–A8), response v1.1

The table and following paragraph record v1.1; location references (§ and row IDs) are preserved relative to v1.1. From v1.2 onward, the corresponding material is in §7 (novelty and qualification) and Appendix D (verification).

| ID | v1.0 audit finding | v1.1 response and location | Current disposition and recheck |
|---|---|---|---|
| A1 | Inconsistent LB matrix, basis, and initial state, S2 | Standardized Appendix B to (e,g,ℓ), tridiagonal H, and initial (1,0,0); stated permutation and effective-resonance assumptions | Repair implemented. C06, V07, W02; `lb-initial-state` fault |
| A2 | Irrational supremum described as finite-time attainment, S2 | Separated exact finite-time attainment from supremum in (LB3); proved a strict maximum for rational even/odd ratios | Repair implemented. C07, W03; universal phase argument in Appendix B.2 |
| A3 | Total excitation confused with photon energy and logarithmic coefficients, S2 | Specified separate spectra, comparison inequality, and coefficients in (LC7)–(LC9); corrected F3 | Repair implemented. C05, V03, V06, R01; `photon-as-total` fault |
| A4 | Damaged attached Markdown; 38/38 not reproduced, S2 | Removed broken embedded script; intact formula source and single-companion contract; final-file hashes and paired run | Repair implemented. G01–G05, missing-document and isolated reproduction |
| A5 | Literal PASS, incorrect projector, substitute-integral check, S2 | Actual compact packet, four tensor components, actual moving tensor, observable-specific integrals; P=0 and separation of C/V/W/R/G/D | Repair implemented. C01, C02, W01 and functional faults; no automatic certification of prose proofs or novelty |
| A6 | Novelty HOLD lifted without additional evidence | Restored OPEN-NOVELTY, qualification HOLD, and UNASSESSED in §6; explicitly designated a research note | Status strings again departed from Mission vocabulary in v1.2 (F03); v1.3 restored four fields: HOLD, UNASSESSED, CANDIDATE 3, TARGET 4. **Novelty debt itself remains OPEN**, D01 SKIP |
| A7 | PEC table τ²/τ⁴ error and overstated correction order, S1 | (LC12) and mode-specific leading denominator; removed unsupported universal relative-error rate | Repair implemented. V05, R02, G03; `pec-tau-power` and `doc-table` faults |
| A8 | Omitted LA proof, reversed abstract meaning, bibliographic errors, S1 | Restored boundary domain, radial determinant, recurrence, and q monotonicity; corrected inclusive/exclusive sentence, UDW summary, and bibliography | Repair implemented. C08, C09, V09, V10, W01; source comparison in §7 and references |

“Repair implemented” denotes author-side re-examination. The v1.0 judgment of highest severity S2 and AUDIT-MAJOR-REVISION remains attached to that historical artifact. This version does not withdraw the central results or retroactively certify novelty or CORE success.

### Round 2 — v1.1 author-side scope corrections (6 findings, S1–S6), response v1.2

The following are not external audit findings, but **scope** issues in v1.1 identified by the authors while deriving LM in v1.2. Following F04 of the v1.2 audit, v1.3 reclassifies each as `scope clarification / new extension / actual correction`. Item 5 of §1.1 in the original v1.1 (sha256 `b00a337b…`) explicitly says that LC-K/I/T concern initial momentum `k=0`. The auxiliary result in §3 states that it is “not a theorem equating the full `J_(B)` of a general packet with the rest formula,” and §2 explains that a general packet's switching factor depends on `k`. The v1.1 abstract, the condition column of F2, and the adiabatic discussion in §4.2 did not repeat the rest condition. None of these items therefore shows that a v1.1 theorem is false at `k=0`.

| ID | v1.1 statement | v1.2 correction and location | v1.3 reclassification (F04) | Recheck |
|---|---|---|---|---|
| S1 | LC-I's `Ω³/Ω⁵` IR orders (rest restriction not repeated in the abstract) | Restricted to `k=0`; note in §3, LM-S | **Scope clarification** (abstract/summary level) + **new extension** (LM-S) | V12, W05 |
| S2 | `τ⁻²/τ⁻⁴` law and 0 adiabatic limit in (LC12) and the numerical table | Restricted to the rest plane-wave prescription; packets governed by LM-A | **Scope clarification** + **new extension** (LM-A) | V15, W05, W06, R04, `rest-ir-for-packet` |
| S3 | Auxiliary moving-packet argument and plateau `J_(∞)` | Divergence for every packet, nonuniform plateau; note in §3, LM-B and LM-R | **Replacement by new theorems**. v1.1 did not claim uniformity, so v1.2's phrase “implicit uniformity” is withdrawn | V13, V14, V16, R05, `uniform-plateau` |
| S4 | `(1)/(2)ℰ_(total) ≤ ℰ_(γ) ≤ ℰ_(total)` | Rest only; moving-sector counterexample; note in §4, LM-E | **Scope clarification** + **new extension** (LM-E; the moving sector was outside the theorem's scope) | W04, `photon-total-moving` |
| S5 | LC-T iff applied only to the plane-wave rest prescription | Extended to every normalized packet; LM-T | **New extension** (not an error in the old theorem) | V14 and proof in §5.4 |
| S6 | Rest restriction absent from the comparison-condition column of F2 | Marked rest only and added moving-sector F4; §6 | **Scope clarification** (F2 condition column) + **new extension** (F4–F6) | V12 |

S1–S6 belong to the same author-side lineage; they do not mean that the v1.1 numerics or theorems were wrong at `k=0`. No item is classified as an actual correction. S1–S6 are not summed as six new theorems or debt closures.

### Round 3 — v1.2 audit (5 findings, F01–F05), response v1.3

External auditor: OpenAI Codex (also the author of v1.1, so the audit itself disclosed possible self-preference in the inherited LC/LA/LB parts). Judgment: AUDIT-MAJOR-REVISION, highest severity S2, PAPER QUALIFICATION FAIL in the current form, RESEARCH GRADE UNASSESSED, CANDIDATE 3, Significance PASS, Verification basis PASS. The audit evidence package (hash in C.1) was reproduced by an isolated rerun in the v1.3 session at the time: 43 PASS / 0 FAIL / 3 SKIP, self-test 19/19, independent calculations 9/10 reproduced with 1 mismatch = F05, and the same node-convergence diagnostic. Each row uses `current claim / problem / replacement / verifier / post-repair status / routing`.

| ID | Audit finding (severity) | v1.3 replacement and location | Recheck rows and live-fire | Post-repair status | Routing |
|---|---|---|---|---|---|
| F01 | PEC `τ⁻²` statements in abstract item 3 and F5 omit packet-moment conditions; a log-moment alone is insufficient (S2, RELEASE-BLOCKING). Counterexample: `φ=1/(√(π)(1+∣ k∣²))` | Separated conditions in the abstract, F5b, LM-A(b), and card. Rederived the `E²`-moment bound from audit Appendix A and integrated it into (LM10) and the necessary-and-sufficient theorem LM-A(b); preserved the counterexample as W06 in §5.6 | C15 (constants/identities), V17 (grid dominating function), W06 (moments/divergence), X01 (τ²-growth diagnostic), `pec-logmoment-only` fault | Author-side repair complete; Correctness **HOLD** pending re-audit | VERIFY → AUDIT(Targeted) |
| F02 | Novelty comparison does not reach KRS's general recoil and finite-time formulas in §4 (34)–(39), §5.2 (130)–(134), and §5.1 (67)–(69) (S2, promotion-blocking; novelty HOLD) | Specified source coverage in the §7 table (v1.3 read only through (104); (130)–(134) marked unread); stated correspondence-table plan (i)–(iii) and conditions for lifting HOLD in §7.1; withdrew EXTENDED-CANDIDATE | D01 SKIP (non-executable); G04/G05 check only vocabulary/status-string consistency | **Incomplete — Novelty HOLD retained** | RESEARCH |
| F03 | PAPER QUALIFICATION, RESEARCH GRADE, CANDIDATE, and TARGET replaced by strings outside Mission vocabulary; A6, cover, §7.3, manifest, and G04 inconsistent (S2, RELEASE-BLOCKING) | Split the cover, §7.3, manifest, and verifier constants into HOLD / UNASSESSED / 3 / 4; updated A6; G04 checks vocabulary sets and agreement among cover, manifest, and script | G04, `doc-vocabulary` and `doc-ledger` faults; G05 checks stale strings, `doc-version` fault | Repair complete (not counted as scientific debt closure) | OPS / MANUSCRIPT |
| F04 | v1.1's explicit rest restriction confused with an “implicit generalization error”; no actual claim location for S3's “implicit uniformity” (S1) | Checked exact text in §§1.1-5, 2, and 3 of the hash-matched v1.1; added a reclassification column to Round 2; withdrew “implicit uniformity” in S3; renamed prose notes “scope clarification” | Document check (G04 round parser) | Repair complete | MANUSCRIPT |
| F05 | No error assessment for fixed 128-node angular quadrature; warnings globally suppressed; relative difference 4.53×10⁻⁷ at the grid maximum (S1) | Introduced analytic angular-integration route 3 (audit Appendix B, C15 certification); switched V14 to route 3 (adaptive quadrature, error estimate); V16 reports 128/256-node and node-doubling errors; records warnings per row; meta-audit M1 extends the error scope to the full grid | V14, V16, `angular-nodes-8` fault; execution JSON `warnings` field | Repair complete (printed 6-digit values unchanged) | VERIFY |

**Current status of the re-audit acceptance conditions specified by the audit.** Correctness can be reassessed after the F01 repair (re-audit pending); F02 keeps PAPER QUALIFICATION on HOLD. If everything proves to be routine specialization, Novelty is FAIL; grade 3 can be reviewed if a new nontrivial universal result and practical value are established. Grade 4 additionally requires external limitations, impact, and independent adversarial review. Version v1.3 inherited these conditions unchanged at the time.

### Round 4 — v1.2 meta-audit (8 findings, M1–M8), response v1.3

The audit of the v1.2 audit itself (“audit of the audit”) was performed by the author-side lineage (Claude), so its independence is low. Audit findings were judged only through deterministic reruns, symbolic checks, and source comparison. Results: F01, F03, and F05 [verified: deterministic reproduction]; F04 [verified: comparison with original v1.1]; F02 [hypothesis: source §4 and (67)–(73) checked, (130)–(134) unread]. No false-positive audit finding was identified. The following items were missed or understated by the audit. The full meta-audit report is a separate file, `m70_v1_2_audit_meta_audit.md`.

| ID | Meta-audit finding | Incorporated into v1.3 | Recheck |
|---|---|---|---|
| M1 | F05 extends beyond one point: among 864 grid points, 44 have relative difference `>10⁻⁸` and 8 have `>10⁻⁶` (maximum `2.4 × 10⁻⁶`; all `∣ k∣ ≥ 10⁴`, `Ω ≤ 10⁻²`). Bound 36 and printed 6-digit values are unchanged | Disclosed error distribution in §5.3 and Appendix D.2; switched V14 to route 3; added 2 worst points to V16 | V14, V16 |
| M2 | The grid description in §5.3, “M∈{1,0.3}, a∈{0.1,1,10},” suggests 6 pairs, but the actual 4 pairs are ((1,0.1),(1,1),(1,10),(0.3,1)) | Corrected the description to the actual 4 pairs | V14 data `samples`=864 |
| M3 | No verification row numerically checks the soft-form bound of LM-B(iv) used in LM-A(a) | Added the soft-form ratio to V14 (maximum 0.506) | V14 |
| M4 | “D-M69-MOVING resolved in this channel” in §6.1 is stronger than the ledger's closure condition (a common finite-time error); audit §7.2 mentioned it but did not register it as a finding | Corrected to sub-obligations resolved, overall debt OPEN | Document |
| M5 | “Maximum approximately `4J_(∞)`” does not distinguish a property of the fixed-`λ` limit from the global bound at finite `k,Ω` (OPEN; grid 4.0694>4); mentioned in the audit claim table but not registered as a finding | Made the distinction explicit in the abstract, §3, §5.7, and F6; added stable form and monotonicity to C13 | C13, V14 |
| M6 | The novelty label “EXTENDED-CANDIDATE” lies outside MANUSCRIPT §4 vocabulary (IMPORTED/SPECIALIZED/EXTENDED/NEW/OPEN-NOVELTY) | Corrected to OPEN-NOVELTY (candidate for EXTENDED); G05 checks live use of stale strings | G05 |
| M7 | The manifest lacks machine registration of the author-side S round and audit-response structure (CPN6–CPN8), preventing the round parser from operating | Added `audit_rounds` registration and the G04 round parser; `doc-round` fault | G04 |
| M8 | Formal omissions in the audit report: no per-finding routing or `verifier / status after repair` fields; no RESEARCH-GRADE CARD fields; the reproduction table's description of P rows (“rows counting literal assertions as evidence”) differs from VERIFY's definition of P (proof object). No effect on the substantive judgment | Added routing, verifier, and post-repair-status columns to Round 3; incorporated card fields in §7.3 | Document |

Lineage fact confirmed by the meta-audit: v1.1 C.1 had already recorded that the hash of m70_v1_0.md in history H-0337 (`a4642a94…`) differs from that of the attached v1.0 targeted by the v1.0 audit, v1.1, and v1.2 (`fab1bea6…`). Version v1.3 inherits this fact; the verifier hash `78254bce…` is identical.

### Round 5 — v1.3 audit (4 findings, Q1–Q4), response v1.4

The statuses in Rounds 1–4 preserve their historical context. HOLD and pending re-audit in those tables are not the current v1.4 status. The v1.3 audit was frozen before adding new theorems.

| ID | v1.3 audit item | v1.4 integration and check | Status |
|---|---|---|---|
| Q1 | S1: Download suffix causes G01 failure | Normalized only the suffix; retained content hash; operational rename test | Repaired |
| Q2 | S1: e_ch=0 degeneracy condition | Common nonzero-charge assumption in §1; explicit in LM-A | Repaired |
| Q3 | S1: 14 roundoff warnings in V14 | 50-digit angular averages; reran the same 864 points | Repaired |
| Q4 | S0, promotion-blocking: KRS correspondence incomplete | §§7.1–7.3, C19/W08; LM-D/L/P are separate new contributions | Correspondence complete; qualification reassessed |

Direct-input SHA-256:

- v1.3 manuscript: 6b445e28fbe4a071302c8914a4099aa9660309ed748bebe0b59bae7ac27ddfe4
- v1.3 verifier: f4c1c5ffd3a8725accd5f678d0f0f91777b50fc9b3ed8f59dd91c943b0df923e
- v1.3 evidence ZIP: 15d2cb109d2e47de88473247037c9a43a50868265c32a36b8b7ce20556749a7c

Sections C.1–C.2 below are upstream history retained by v1.3; they do not mean that every past run was repeated in this turn.

### Round 6 — v1.4 A/B comparison (7 findings, U1–U7), response v1.5

Round 5 belongs to version A's lineage. Version B's separate Round 5, T01–T05, is preserved in its original evidence ZIP and does not overwrite the same round number. The following is the fixed mapping from pre-integration defects to their repairs.

| ID | Pre-integration finding | v1.5 disposition | Evidence |
|---|---|---|---|
| U1 | Exact counterexample to B's intermediate soft denominator inequality (S2) | Restored inner/outer proofs; preserved bound 18 | LM18, C20, W10 |
| U2 | Recoil, measurement, and pulse identified in B's KRS correspondence; source coverage incomplete (S2) | Rechecked PDF (130), (67), and (45); integrated A's correspondence and commutator counterexample | §7.1, C19, W08 |
| U3 | Inconsistent scope of the rest lower bound across the two versions and OPEN necessary-condition label within B (S1) | Extended photon lower bound to every packet; iff for the finite-mean-energy class | LM19, C20, V21 |
| U4 | 16 roundoff warnings despite B's paired PASS (S1) | Applied A's 50-digit angular average to every photon weight as well | V14, V21 |
| U5 | Numerical lower bound on the supremum mixed with rigorous evidence (S1) | Preserved numerical value 4.110216; separately proved exact lower bound 64/(5 pi) | LM20, C21, V22, W09 |
| U6 | Different qualification, grade, and independence judgments under the same 1.4 version number (S1) | Preserved input judgments; rewrote content assessment; retained the self-audit limit | §7.4 |
| U7 | Equation/verification-row ID collisions and risk of omitted downstream constants (S1) | Froze original names and hashes; semantic mapping and downstream propagation of 18 | Correspondence table below, G01–G05 |

| Object | Version A → v1.5 | Version B → v1.5 |
|---|---|---|
| Dini / layer / tail / KRS checks | C16–C19, V18–V20, W07–W08 retained | Not applicable |
| CM denominator / photon lower bound | Not applicable | C16 → C20; V18 → V21 (extended to three mode families) |
| Finite point exceeding 4 / soft-estimate diagnostic | Not applicable | W07 → W09; X02 → X02 |
| Equation numbers | LM1–LM17 retained | LM11 → LM18; LM12 → LM19 |
| Added during integration | LM20, C21, V22, W10 | Generated by comparing both versions |

Input SHA-256 (these two manuscripts and verifiers were not modified):

- A manuscript: `0a287d32eb3e1e92f62b7056bcb888e46d76078c06c53c4fb5005a5c8bdd61e8`
- A code: `ac230025b97dd2e7bca8f99b09a925dfe846ebea6d88df1262b765d05e04b8a1`
- B manuscript: `120b76aaad7e43a777f2e3c49b5a74b5914e02bac7fbb9d69f3f97ff3a66014d`
- B code: `86c71c1fe100844558855916f32a867896895a7654a624010970ee33809eac1e`

### C.1 Frozen upstream identity

| Object | SHA-256 | Purpose |
|---|---|---|
| Attached m70_v1_2.md | `00187d0cdc086f99c70d3ed49aa48f6948736a6818886b9a6f63e30a9fe9b0ab` | Direct input during v1.3; target of the v1.2 audit |
| Attached m70_v1_2_verify.py | `a17af533d17a02af42d89119b32f64d852b800438fc7b8b9ed9eda8802eee1a4` | Starting code for the v1.3 verifier |
| m70_v1_2_audit.md (OpenAI Codex) | `ae2ca14554152ec196af61776e7d0516f00d81b87712bdfe6320c8d196144e40` | Round 3 audit report |
| m70_v1_2_audit_checks.py | `67576301c5422ca883d2122e44f9fe56763cf00f48d4c635edaa9080d85af057` | Auditor's independent calculations (source of route 3) |
| m70_v1_2_convergence_probe.py | `9b5447e0308e1db3b805bbc70ffd9e3e23991bb5067e4e3f4871235afd657452` | F05 diagnostic |
| v12_paired.json / v12_selftest.json / v12_independent.json / v12_convergence.json | `9081d110…9842` / `6300c44b…8b65` / `e1daea3c…2bd6` / `1a48c229…d917` | Audit evidence (reproduced byte for byte during the v1.3 session) |
| Attached m70_v1_1.md | `b00a337bf6d10a7b80f4216e42c53ca4a51fc6ed04ad799da9511051ed3fb3e0` | F04 exact-text comparison |
| Attached m70_v1_1_verify.py | `9a3d170c109a2ecd8d60a328cb1952eeb72e476264c9badb859258bf6ff2dca6` | Starting code for the v1.2 verifier |
| Attached m70_v1_0.md | `fab1bea66c957a203ec4b9301bf5148d846de101dd8841da790c4e3c7a13922e` | Target of the v1.0 audit |
| Attached m70_v1_0_verify.py | `78254bce06f71ac56ecbd424f1b94edbb83b159c8c8b619e3bcef5e2d08b0c6c` | Original v1.0 verifier |
| m70_seed_report_v2_1(1).md | `053f3f8e48333a92177bb2879c503795c73946af8cc95884a0e1adb07e8cf0e3` | Precursor for LA/LB/LC and the grade requirements in §11 |
| m70_seed_verify_v2_1(1).py | `4d12a7abec8b3f55b456530c2526859ab745c0fe46fd414daf026463b49cc039` | Preceding executable ledger |

Version v1.3 likewise does not duplicate the full Python script in Markdown. The manuscript records the companion `.py` hash; the verifier reads that hash, declarations, formulas, two numerical tables, status fields, and round registrations. The manuscript's own hash is recorded in the execution JSON.

### C.2 Expansion of the verification ledger (46 rows in v1.2 → 52 in v1.3)

An identifier is the pair `(artifact version, row ID)`. The rows are composed as follows.

- **Rows rerun in v1.3 with the same functions (34):** C01–C12, C14, V01–V10, V13, W01–W03, W05, R01–R04
- **Rows changed in v1.3 (retyped/replaced, 8):** C13 (added stable form and monotonicity), V11 (added route 3), V12 (added route-3 ratios), V14 (replaced by route 3, error estimates, and the soft-form ratio; previous 128-node grid value 4.06942218 → 4.06942033), V15 (route 3), W04 (added route-3 comparison), R05 (route 3), G04 (replaced by vocabulary and round parser)
- **New rows (9):** C15, V16, V17, W06, X01, G05 + (D01–D03 retain the same declarations as v1.2 and are not rerun)
- **Declaration rows (3):** D01–D03
- **Deleted rows:** None

Residuals of carried-forward rows are unchanged (same functions and inputs; V15 uses route 3 and retains the same printed 6-digit values as v1.2). This was checked by comparing the execution JSON in D.3 with `v12_paired.json` from the v1.2 audit evidence.


### C.3 Increment in version A of v1.4 (history)

The existing 52 rows were preserved, and 9 rows—C16–C19, V18–V20, W07–W08—were added, giving 61 rows. Angular-average precision and the policies for new equations, tables, ledger entries, and filenames in G01–G05 were updated. Earlier identifiers are interpreted together with their versions. Version v1.5 adds 7 rows for a total of 68 and follows the Round 6 mapping above.

## Appendix D. Verification contract and actual results

### D.1 Reproduction

Python 3.10 or later, numpy, scipy, sympy, and mpmath are required. After installation, verification runs offline. The manuscript and verifier are the two input files; the evidence ZIP is archival.

```bash
python m70_v1_5_verify.py --paper m70_v1_5.md
python m70_v1_5_verify.py --paper m70_v1_5.md --self-test
```

--math-only explicitly excludes only document checks. Normal completion exits 0, a row failure exits 1, and dependency/invocation errors exit 2. A missing document appears as G01–G05 failures. --fault changes the implementation or input, not expected values. The execution environment is Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0, and mpmath 1.3.0.

### D.2 Numerical methods and errors

The rest-route adaptive-quad/polar comparison is retained. Moving route 1 uses photon-sphere 400×96 Gauss–Legendre quadrature; route 2 uses covariant half-angle 128-node quadrature (with a 256-node comparison); route 3 analytically eliminates the angular average, substitutes `z=a tan θ`, and uses adaptive quad. **Route 3 computes the entire angular average with mpmath at 50 digits before passing it to outer binary64 quad.** The outer request remains epsrel=1e-11. The routes share the same vertex, band, and modes, so they are not independent experimental tests of the physical assumptions.

The Gaussian `x` integral uses 64 nodes on [0,7]. The omitted part can be bounded by `36πτ J_(∞)∫_(7)^(∞) e^(-x²)dx` from LM-B. For PEC, LM-D gives the `τ,k`-independent bound `π C_(ρ) e⁻⁴⁹`. The former must not be read as a constant common to every `τ`. Gaussian packets use 24-node Laguerre quadrature; the X01 heavy-tail diagnostic uses a 24-node energy integral.

There were 14 roundoff warnings in v1.3 V14. Version A's normal run had 0 warnings; the original rerun of version B had 16. Version v1.5 adopts high-precision angular averages and records the final run's warning count in JSON. Warnings are collected per row, not globally suppressed. Quad errors are estimates, not interval enclosures. The finite-`E` differences below are asymptotic errors, distinct from quadrature errors. The 864 points of V14 comprise four `(M,a)` pairs × 9 momenta × 8 frequencies × 3 modes, not a Cartesian product of independent M and a values.

### D.3 Numerical use of the new results

`M=a=e_(ch)=1`. L is the closed form in (LM14), and J is the original finite-energy spectrum.

<!-- LAYER-TABLE -->
| eta | E | L | J_over_Omega |
|---:|---:|---:|---:|
| 0.01 | 10000 | 3.335497482e-6 | 3.335496581e-6 |
| 0.1 | 10000 | 0.0002986255911 | 0.0002986255017 |
| 1 | 10000 | 0.01113213196 | 0.01113212364 |
| 10 | 10000 | 0.03604367274 | 0.03604303300 |
| 100 | 100000 | 0.04585413416 | 0.04585349105 |
<!-- /LAYER-TABLE -->

The table's largest asymptotic relative difference is `1.775 × 10⁻⁵`. The maximum relative difference between L's closed form and separate normal-direction integration was at most `2.3 × 10⁻¹⁶`; this does not replace a universal convergence proof. V19 checks 10 points in total, with two samples tending toward large E for each case.

The Mellin coefficients for `E_(0)=1` are shown below. The integration interval is `η ∈ [10⁻¹²,10¹⁰]`, and analytic bounds for the omitted tails at both ends are
```text
πα E_(0)^(α)Γ(1+α/2)
[(Aε^(2-α))/(2-α)+(C_(ρ) R^(-α))/(α)].
```

| alpha | Approximation to `K_(α)` | Analytic tail bound | Quad error estimate |
|---:|---:|---:|---:|
| 0.5 | 0.09923 | 6.55e-6 | 6.1e-13 |
| 1.0 | 0.11739604 | 6.44e-11 | 3.9e-12 |
| 1.5 | 0.26410 | 1.32e-6 | 2.8e-12 |

Print-rounding error must be added separately. This table is not a rigorous interval certificate. The finite-mean-energy packet with `α=3/2` decays approximately as `0.26410 τ^(-3/2)`, with the exact coefficient given by (LM17). The norm lower bound over all packets is `I_(ρ)/(4π)=1/(2π) ≃ 0.159155`. This is not a residual response of a fixed packet.

### D.3b Numerical values and exact formulas for the integrated additions

| Check | Result | Nature of evidence |
|---|---|---|
| V18: Maximum PEC soft-bound ratio against strengthened C_rho | 0.7310751813 | Counterexample search at 288 points |
| V21: Minimum J_gamma/(Omega J) | 0.5049509901 | 96 points across three mode families; theoretical lower bound 1/2 |
| W09: J/J_inf at the attached PMC point | 4.1102159588 | 50-digit angular average plus binary64 outer quadrature; not an interval certificate |
| LM-Q / C21 | 64/(5 pi) = 4.0743665432 | Analytically proved lower bound on the global supremum |
| V22: Maximum relative difference from Q_B at E=10^7 | 0.00081005 | Three mode families, two frequencies; finite-E convergence diagnostic |

The constant 18 is propagated to H in LM10, C_rho in LM11, the tail bound in LM13, and the Mellin-tail error. K_alpha itself and the boundary layer L_rho are unchanged. Improved error bounds are therefore not interpreted as a different decay rate or physical model.

### D.4 Census and claim correspondence

<!-- RUN-SUMMARY -->
**Normal paired profile: 65 PASS / 0 FAIL / 3 SKIP, 68 rows total, exit 0.**

| Category | C | V | W | R | X | G | D | P |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Registered rows | 21 | 22 | 10 | 5 | 2 | 5 | 3 | 0 |
| Normal run | PASS | PASS | PASS | PASS | PASS | PASS | SKIP | Unregistered |

Evidence C/V/W: 53 rows; controls R/G: 10 rows; non-evidence X/D: 5 rows. Math-only gives 60 PASS / 0 FAIL / 8 SKIP. P=0.
<!-- /RUN-SUMMARY -->

| Claim | Evidence and controls | Actual scope |
|---|---|---|
| LC-K/U/I/T | C01–C05, C10, V01–V06, W01, R01/R02 | Rest tensor·shell·IR/UV·Gaussian·sharp-switch |
| LM-K/B/T/S/A/R/E | C11–C15, V11–V17, W04–W06, R04/R05 | Three routes; 864-point bound; soft behavior, moments, plateau, and photon comparison |
| LM-D | C16, V18, W07 | Dini constant, uniform soft bound at 288 points, infinite-log-moment example |
| LM-L | C17, V19/V20 | Leading terms, endpoints, primitives; finite E versus boundary layer; normal-direction quadrature |
| LM-P | C18, V20, W07 | Jacobian, Gaussian Mellin factor, coefficient, finite-energy example |
| KRS-MAP | C19, W08 | Cancellation of amplitudes before/after measurement, temporal factor, identity counterexample |
| LA/LB | C06–C09, V07–V10, W02/W03, R03 | Separate models in the preserved appendices |
| LM-B0/E | C20, V21, W10 | Strengthened constant, 2268 shells, 96 photon weights, exact counterexample |
| LM-Q | C21, V22, W09 | Fixed-frequency limit, exact integral, numerical value exceeding 4 |
| PACKAGE | G01–G05 | Names, hashes, formulas, tables, ledger, version, and status strings |
| Non-evidence | X01/X02, D01–D03 | Growth and nonuniform-estimate diagnostics; novelty, full instrument, and universal formal certification are SKIP |

**Self-test:** Executes 29 functional/structural fault injections and 5 operational scenarios. Each fault actually recomputes the designated failing row in a new process using --only-row, with all other rows marked SKIP. The normal baseline and operational reproduction execute the full ledger. Coverage includes detection of the designated failing row, missing document, math-only, missing dependencies under python -S, two isolated runs with only the two files copied, and a run of both files with download suffixes. Results and exact hashes are in v15_selftest.json in the evidence ZIP. Isolation uses the same installed environment and does not mean an independently installed environment.

### D.5 Universal-theorem review card

| Theorem | Proof obligation and dominating function | Assumptions and attacks that prevent failure |
|---|---|---|
| LM-B/T | CM tensor bound; `18J_(∞)`; positive UV plateau at fixed k | Real `χ ∈ L¹`, nonzero charge; interchange with packet limits |
| LM-A(b) | `H(E)=AE²+B_(0)`, positive `c_(PEC)/E²` limit; DCT/Fatou | Finite d; infinite-E² counterexample W06 |
| LM-D | `B+B/∣ z∣`, `π C_(ρ)`, `B(0)=0` at fixed k | Dini is a sufficient assumption; no necessary profile condition claimed |
| LM-L | `B+B/∣ z∣` at fixed eta; `C_(ρ) xe^(-x²)` for the Gaussian | z=0 and the moving endpoint have measure zero; distinguish the two limits |
| LM-P | `u^(-1-α) min (C,(A+B_(0)/E_(0)²)u²)` | Integrable precisely for `0<α<2`; no equivalent at alpha=2 claimed |

Counterexample attacks included e_ch=0, k=0, infinite log/E² moments, moving packets with E~tau, alpha=2, the identity projector, and the order of finite-cutoff limits. Numerical success is not universal machine certification. Version A has received 2 author-side semantic reviews including the present comparison; these are distinguished from the cross-family review of version B's new parts. Earlier same-lineage review counts are not reset by changing versions or counted as a 3rd independent review.

## Appendix E. Authorship lineage and subsequent review

The LC/LA/LB results from the seed and v1.1, Claude's v1.2 moving sector, the E² bound and angular average from the earlier Codex audit, and Claude's v1.3 rederivations and repairs are preserved. Version A supplied the KRS correspondence between amplitudes before and after measurement, LM-D/L/P, and 50-digit angular averages; version B supplied bound 18, the photon lower bound, and an extended numerical witness. The present v1.5 integrates these with corrections and adds LM-Q. Earlier results are not counted again as new contributions.

The input manuscripts, verifiers, ledgers, and history were not modified. No external review request was sent, and no human review was received. Subsequent attacks should target the limit interchanges in LM14, LM17, and LM20 and the existence of identical prior theorems relevant to §7. The exact logarithmic coefficient at alpha=2, optimal packet condition for photon energy, globally optimal constant, optimality of the Dini condition, and common errors for an actual instrument, bulk, and Coulomb effects remain OPEN.

## References

Internal materials identify definitions and lineage; they are not counted as independent external novelty reviews.

1. M70 seed report v2.1, §§2.1, 6.6, 7.2, 11–12, 20.2, 22–25; attached `m70_seed_report_v2_1(1).md` and companion `m70_seed_verify_v2_1(1).py`. Direct precursor for central LC, supporting LA/LB, and the prior-research ledger.
2. M70 v1.0 and v1.0 audit, 2026-09-10; M70 v1.1 manuscript and verifier; M70 v1.2 manuscript and verifier, 2026-09-10; M70 v1.2 audit (OpenAI Codex, 2026-09-10) and evidence package. Target hashes and A1–A8, S1–S6, F01–F05, and M1–M8 are recorded in Appendix C.
3. [M67 v3.4.1](https://drive.google.com/file/d/1NMOQH5EucwT061J0W4PTL-3FGxqdSFMh/view), Thm 15 and normal overlap: conditional boundary-carrier input.
4. [M69 v2.0](https://drive.google.com/file/d/16df9VwZ93iUy5HVAQyR0BH_KZ4X7Izfa/view), §8 T7–T8, §§10.3–10.4: current tensor, on-shell exclusion, and remaining bridge.
5. Z-Spin Research Mission v1.6, §1.4 and RQ3; project rules v2.3 KERNEL / MANUSCRIPT / VERIFY / AUDIT; Repo3 [Manifest](https://drive.google.com/file/d/1VZPMX_3CclyIuVxJXHhJHYtpGiE8PIKy/view), [Debt/Retraction/Gates](https://drive.google.com/file/d/15glYyDFt4LAz9muDwWXSmTJh_-lNYzRq/view), [Paper Catalog](https://drive.google.com/file/d/1LJh1_MI2FEPqHjYKwPPTmaOeC5HMhxD3/view). Operational basis for mission and status.
6. P. O. Kazinski and **G. Yu. Lazarenko**, *Transition radiation from a Dirac particle wave packet traversing a mirror*, Physical Review A **103**, 012216 (2021), [arXiv:2010.05236v2](https://arxiv.org/html/2010.05236v2). See the §7 table for the scope of direct comparison.
7. L. Hodgkinson and J. Louko, *How often does the Unruh-DeWitt detector click beyond four dimensions?*, Journal of Mathematical Physics **53**, 082301 (2012), [arXiv:1109.4377v3](https://arxiv.org/html/1109.4377v3).
8. S. Teber and A. V. Kotikov, *Field theoretic renormalization study of reduced quantum electrodynamics and applications to the ultra-relativistic limit of Dirac liquids*, Physical Review D **97**, 074004 (2018), [arXiv:1801.10385v2](https://arxiv.org/html/1801.10385v2).
9. Á. Baricz and S. Ponnusamy, *On Turán type inequalities for modified Bessel functions*, [arXiv:1010.3346v1](https://arxiv.org/html/1010.3346v1) (2010).
10. O. Eisenberg, M. Kempton and G. Lippner, *Pretty good quantum state transfer in asymmetric graphs via potential*, [arXiv:1804.01645v1](https://arxiv.org/html/1804.01645v1) (2018).
11. P. O. Kazinski, V. A. Ryakin and P. S. Shevchenko, *Radiation from Dirac fermions caused by a projective measurement*, [arXiv:2406.19429](https://arxiv.org/pdf/2406.19429) (2024). Closest source for the subsumption test in §7.1; v1.4 checked PDF §4 (34)–(46), §5.1 (49), (67)–(69), and §5.2 (130)–(134).
12. P. O. Kazinski and T. V. Solovyev, *Coherent radiation of photons by particle wave packets*, European Physical Journal C **82**, 790 (2022), [link](https://link.springer.com/article/10.1140/epjc/s10052-022-10739-6).
13. H.-P. Breuer and F. Petruccione, *Destruction of quantum coherence through emission of bremsstrahlung*, Physical Review A **63**, 032102 (2001), [link](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.63.032102).
14. S. Weinberg, *Infrared photons and gravitons*, Physical Review **140**, B516 (1965).
15. *Radiative loss of coherence in free electrons: a long-range quantum phenomenon*, Light: Science & Applications (2023), [link](https://www.nature.com/articles/s41377-023-01361-6). Author bibliographic information was checked only through the link.

Satz's switching paper and the 2D macroscopic-QED paper by Svendsen et al. are background sources whose abstracts and bibliographic information were checked during the audit, but they are not load-bearing sources for this version. Novelty is not judged on the basis of full-text material that was not actually read.


The closest sources in §7 were read during this work. The remaining references in Appendices LA/LB preserve the existing lineage; this does not mean that all of them were exhaustively reverified in this turn.

## Execution metadata

Only declaration consistency is checked; novelty and grade are not computed. The manuscript hash is output in the execution JSON.

<!-- M70-META
{
  "paper": "m70_v1_5.md",
  "paper_version": "1.5",
  "script": "m70_v1_5_verify.py",
  "script_version": "1.5.0",
  "script_sha256": "e1a7c3f0bb728d51a6dea99a63960fa95f3d1b99d54206a043312730a48f7636",
  "qualification": "PASS",
  "research_grade": "3",
  "candidate_grade": "NONE",
  "target_grade": "4",
  "novelty": "PER-CLAIM: LM-D/LM-L/LM-P NEW; LM-B/LM-T/LM-A/LM-R EXTENDED; LM-Q EXTENDED; LM-K/LM-S/LM-E/LC SPECIALIZED; LA OPEN-NOVELTY (appendix only)",
  "role": "RESEARCH PAPER / SUPPORT-METHOD",
  "audit_rounds": [
    {
      "round": 1,
      "audited_version": "1.0",
      "response_version": "1.1",
      "prefix": "A",
      "findings": 8,
      "kind": "external audit"
    },
    {
      "round": 2,
      "audited_version": "1.1",
      "response_version": "1.2",
      "prefix": "S",
      "findings": 6,
      "kind": "author-side scope corrections"
    },
    {
      "round": 3,
      "audited_version": "1.2",
      "response_version": "1.3",
      "prefix": "F",
      "findings": 5,
      "kind": "external audit"
    },
    {
      "round": 4,
      "audited_version": "1.2-audit",
      "response_version": "1.3",
      "prefix": "M",
      "findings": 8,
      "kind": "meta-audit of the v1.2 audit"
    },
    {
      "round": 5,
      "audited_version": "1.3",
      "response_version": "1.4",
      "prefix": "Q",
      "findings": 4,
      "kind": "targeted audit and research integration"
    },
    {
      "round": 6,
      "audited_version": "1.4-A/B",
      "response_version": "1.5",
      "prefix": "U",
      "findings": 7,
      "kind": "cross-lineage B comparison; low-independence A integration review"
    }
  ],
  "rows": 68,
  "census": {
    "C": 21,
    "V": 22,
    "W": 10,
    "R": 5,
    "X": 2,
    "G": 5,
    "D": 3
  },
  "ledger": {
    "C01": [
      "C",
      "LC-K"
    ],
    "C02": [
      "C",
      "LC-U"
    ],
    "C03": [
      "C",
      "LC-K"
    ],
    "C04": [
      "C",
      "LC-I"
    ],
    "C05": [
      "C",
      "LC-T"
    ],
    "C06": [
      "C",
      "LB"
    ],
    "C07": [
      "C",
      "LB"
    ],
    "C08": [
      "C",
      "LA"
    ],
    "C09": [
      "C",
      "LA"
    ],
    "C10": [
      "C",
      "LC-T"
    ],
    "C11": [
      "C",
      "LM-K"
    ],
    "C12": [
      "C",
      "LM-S"
    ],
    "C13": [
      "C",
      "LM-R"
    ],
    "C14": [
      "C",
      "LM-B"
    ],
    "C15": [
      "C",
      "LM-A"
    ],
    "C16": [
      "C",
      "LM-D"
    ],
    "C17": [
      "C",
      "LM-L"
    ],
    "C18": [
      "C",
      "LM-P"
    ],
    "C19": [
      "C",
      "KRS-MAP"
    ],
    "C20": [
      "C",
      "LM-B/E"
    ],
    "C21": [
      "C",
      "LM-Q"
    ],
    "V01": [
      "V",
      "LC-K"
    ],
    "V02": [
      "V",
      "LC-U"
    ],
    "V03": [
      "V",
      "LC-U"
    ],
    "V04": [
      "V",
      "LC-I"
    ],
    "V05": [
      "V",
      "LC-T"
    ],
    "V06": [
      "V",
      "LC-T"
    ],
    "V07": [
      "V",
      "LB"
    ],
    "V08": [
      "V",
      "LB"
    ],
    "V09": [
      "V",
      "LA"
    ],
    "V10": [
      "V",
      "LA"
    ],
    "V11": [
      "V",
      "LM-K"
    ],
    "V12": [
      "V",
      "LM-S"
    ],
    "V13": [
      "V",
      "LM-R"
    ],
    "V14": [
      "V",
      "LM-B"
    ],
    "V15": [
      "V",
      "LM-A"
    ],
    "V16": [
      "V",
      "LM-K"
    ],
    "V17": [
      "V",
      "LM-A"
    ],
    "V18": [
      "V",
      "LM-D"
    ],
    "V19": [
      "V",
      "LM-L"
    ],
    "V20": [
      "V",
      "LM-L/P"
    ],
    "V21": [
      "V",
      "LM-E"
    ],
    "V22": [
      "V",
      "LM-Q"
    ],
    "W01": [
      "W",
      "LC-K"
    ],
    "W02": [
      "W",
      "LB"
    ],
    "W03": [
      "W",
      "LB"
    ],
    "W04": [
      "W",
      "LM-E"
    ],
    "W05": [
      "W",
      "LM-A"
    ],
    "W06": [
      "W",
      "LM-A"
    ],
    "W07": [
      "W",
      "LM-D/P"
    ],
    "W08": [
      "W",
      "KRS-MAP"
    ],
    "W09": [
      "W",
      "LM-B/Q"
    ],
    "W10": [
      "W",
      "LM-B"
    ],
    "R01": [
      "R",
      "LC-T"
    ],
    "R02": [
      "R",
      "LC-T"
    ],
    "R03": [
      "R",
      "LA"
    ],
    "R04": [
      "R",
      "LM-A"
    ],
    "R05": [
      "R",
      "LM-R"
    ],
    "X01": [
      "X",
      "LM-A"
    ],
    "X02": [
      "X",
      "LM-B"
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
    "D01": [
      "D",
      "NOVELTY"
    ],
    "D02": [
      "D",
      "MISSION"
    ],
    "D03": [
      "D",
      "PROOF"
    ]
  }
}
-->
